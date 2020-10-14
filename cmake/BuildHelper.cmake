function(add_bin_from_elf elfTarget binFileName)
    add_custom_command(TARGET ${elfTarget} POST_BUILD
            COMMAND COMMAND ${CMAKE_OBJCOPY} -Obinary $<TARGET_FILE:${elfTarget}> $<TARGET_FILE_DIR:${elfTarget}>/${binFileName}
            COMMENT "Creating ${binFileName}" VERBATIM )
endfunction(add_bin_from_elf)

function(create_lst_file elfName)
    # Generate assembly listing.
    add_custom_command(
            TARGET ${elfName}.elf
            COMMAND "arm-none-eabi-objdump"
            ARGS "-S" "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${elfName}.elf" ">>" "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${elfName}.lst")
endfunction(create_lst_file)

# The trick is that makefiles generator defines a [sourcefile].s target for each sourcefile of a target to generate the listing
# of that file. We hook a command after build to invoke that target and copy the result file to our ourput directory:
# Source https://gist.github.com/Manu343726/64c0a75c089ad96d22cb
#
function(create_assembly TARGET SOURCE_FILENAME ASSEMBLY_LISTING_FILE)
    add_custom_command(TARGET ${TARGET}
        POST_BUILD
        COMMAND make ARGS ${SOURCE_FILENAME}.s
        COMMAND ${CMAKE_COMMAND} -E copy
        "${CMAKE_BINARY_DIR}/CMakeFiles/${TARGET}.dir/${SOURCE_FILENAME}.cpp.s"
        "${CMAKE_BINARY_DIR}/${ASSEMBLY_LISTING_FILE}"
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
endfunction(create_assembly)
