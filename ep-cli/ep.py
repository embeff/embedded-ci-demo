import argparse
import os.path
import yaml
import cbor2
import json
from collections import OrderedDict
from rabbit_rpc import RabbitRPC
from tabulate import tabulate

from pathlib import Path
import pika.exceptions


parser = argparse.ArgumentParser(description='Execute binary on ExecutionPlatform')
# All arguments starting with two dashes can also be specified in a configuration file.
parser.add_argument('File', help='file to execute')
parser.add_argument('-type', default="execute", help='Supported modes are: execute, benchmark')
parser.add_argument('--target', help='Target')
parser.add_argument('--url', default=None, help='Connection url')
parser.add_argument('--cpuspeed', default=None, type=int, help='Target clock speed in Hz. Default uses the configured clock speed for the given target.')
parser.add_argument('--timeout', default=5, type=int, help='Timeout for processing this request on the ExecutionPlatform.')
parser.add_argument('-outputs',
                    default='0',
                    help='Outputs to capture default 0 (eg. --outputs "0,1" for output 0 and 1)')
parser.add_argument('-config', help='Configuration file')
parser.add_argument('-showconfig', action='store_true', default=False, help='Only show the configuration which will be used.')

args = parser.parse_args()
configuration_file = args.config
outputs = args.outputs

command_line_configuration = {}
if args.url is not None:
    command_line_configuration['url'] = args.url
if args.cpuspeed is not None:
    command_line_configuration['cpuspeed'] = args.cpuspeed
if args.target is not None:
    command_line_configuration['target'] = args.target
if args.timeout is not None:
    command_line_configuration['timeout'] = args.timeout


configuration = {}
user_configuration_file = os.path.join(str(Path.home()), '.executionplatform')
local_configuration_file = '.executionplatform'


if os.path.exists(user_configuration_file):
    configuration = yaml.load(open(user_configuration_file, "r"), yaml.Loader)

if os.path.exists(local_configuration_file):
    local_config = yaml.load(open(local_configuration_file, "r"), yaml.Loader)
    configuration = {**configuration, **local_config}

if configuration_file is not None and os.path.exists(configuration_file):
    configuration = {**configuration, **yaml.load(configuration_file, yaml.Loader)}

configuration = {**configuration, **command_line_configuration}

if args.showconfig:
    print("Configuration:")
    print(configuration)
    exit(0)

# Check minimum configuration
if not 'target' in configuration:
    print("You have to specify a target to execute on. For example: --target STM32F407")
    exit(1);

if not 'url' in configuration:
    print("You have to a specify the ExecutionPlatform connection settings. For example: --url amqp://node:node@ep-a0-200072-1:5672")
    exit(1);

with open(args.File, 'rb') as fileContent:
    request = {
        'file': fileContent.read(),
        'headers': {
            'type': args.type,
            'outputs': f"[{outputs}]",
            'timeout': args.timeout
        }
    }

    if 'cpuspeed' in configuration:
        request['headers']['cpuspeed'] = configuration['cpuspeed']

    try:
        # rabbit request
        res = RabbitRPC(timeout_s=60,
                        url=configuration['url'])\
            .call(configuration['target'], cbor2.dumps(request))

        if res is not None:
            result = json.loads(res)
            del result["execution_platform_id"]

            if (args.type == "benchmark"):
                printResults = []
                for res in result['data']:
                    d = OrderedDict()
                    d['Arguments'] = res['args']
                    d['Result'] = res['out']
                    d['Cycles'] = res['cyc']

                    if 'cpu_speed' in result:
                        d['Time (μs)'] = float(1E6 * res['cyc']) / result['cpu_speed']

                    printResults.append(d)

                print(tabulate(printResults, headers="keys", stralign="right", numalign="right", floatfmt=".3f"))

            if "outputs" in result:
                printHeader = (len(result["outputs"].items()) > 1)
                for no, out in result["outputs"].items():
                    if (printHeader):
                        print(f"Output({no}):\n")
                    print(f"{out}")

            if result["return_code"] != 0:
                if result["return_code"] == -4:
                    print(f"A timeout occured. The timeout used was {args.timeout}s. You may consider to increase this time with the --timeout option.")
                elif result["return_code"] == -6:
                    print("Execution error")
                else:
                    print("An error occured during execution.")
                    print(result)
                exit(-1)


    except pika.exceptions.ConnectionClosed as e:
        print("Can't connect to server: " + str(e))
