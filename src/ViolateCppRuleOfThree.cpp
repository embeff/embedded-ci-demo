struct S {
    S(int val) 
        : m_value(val) 
    { }

    // No user-defined Copy Constructor!

    // User-Defined Assginment Operator
    inline S &operator=(S const &rhs) {		
        m_value = rhs.m_value;		
        return *this;		
    }

    int m_value;
};

void ViolateCppRuleOfThree() {
    // The rule of three (also known as the Law of The Big Three or The Big Three) 
    // is a rule of thumb in C++ that claims that if a class defines any of the 
    // following then it should probably explicitly define all three:
    // - destructor
    // - copy constructor
    // - copy assignment operator
    //
    // See https://en.wikipedia.org/wiki/Rule_of_three_(C%2B%2B_programming)

    // Since gcc 9.2 the Compiler canissue a warning
    // when it detects that the rule is violated (-Wdeprecated-copy)
    // 
    S original(42);
    S copy(original);

    (void)copy; // prevent warning that `copy` is unused
}