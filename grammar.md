$$

\text{<BASE\_TYPES>} \to \text{
    number |
    string |
    bool
}

\\

\text{<LIST\_TYPES>} \to \text{list.<BASE\_TYPES>}

\\

\text{<SUPPORTED\_TYPES>} \to \text{
    <BASE\_TYPES> |
    <LIST\_TYPES>
}

\\

\text{<TYPE\_HINT>} \to \text{: <SUPPORTED\_TYPES>}

\\

\text{<NUMBER>} \to \text{d+(.d+)?}

\\

\text{<STRING>} \to \text{"w*"} | \text{'w*'}

\\

\text{<BASE\_TYPES\_VALUES>} \to \text{
    <STRING> |
    <NUMBER> |
    true |
    false
}

\\

\text{<LIST>} \to \text{
    [<BASE\_TYPES\_VALUES> | <LIST>] |
    []
}

\\

\text{<IDENTIFIER>} \to \text{w(w|d|\_)*}

\\

\text{<VARIABLE\_DECLRATION>} \to \text{
    let <IDENTIFIER><TYPE\_HINT>;
}

\\

\text{<FUNCTION\_DECLARATION>} \to \text{
    fn <IDENTIFIER>(<FUNCTION\_ARGUMENTS\_DECLARATION\_OPT>)<TYPE\_HINT> <CODE\_BLOCK>
}

\\

\text{<FUNCTION\_ARGUMENTS\_DECLARATION>} \to \text{
    <FUNCTION\_ARGUMENTS\_DECLARATION>, <IDENTIFIER><TYPE\_HINT> |
    <IDENTIFIER><TYPE\_HINT>
}

\\

\text{<FUNCTION\_ARGUMENTS\_DECLARATION\_OPT>} \to \text{
    <FUNCTION\_ARGUMENTS\_DECLARATION> |
    E
}

\\

\text{<CODE\_BLOCK>} \to \text{
    \{<CODE\_BLOCK\_STATEMENTS\_OPT>\}
}

\\

\text{<CODE\_BLOCK\_STATEMENTS\_OPT>} \to \text{
    <CODE\_BLOCK\_STATEMENTS> |
    E
}

\\

\text{<CODE\_BLOCK\_STATEMENTS>} \to \text{
    <CODE\_BLOCK\_STATEMENTS> |
    <EXPRESSION>
}


\\

\text{<EXPRESSION>} \to \text{
   <LOGICAL\_OR\_EXPRESSION> |
   <IDENTIFIER> = <LOGICAL\_OR\_EXPRESSION>
}

\\

\text{<LOGICAL\_OR\_EXPRESSION>} \to \text{
   <LOGICAL\_AND\_EXPRESSION> |
   <LOGICAL\_OR\_EXPRESSION> OR <LOGICAL\_AND\_EXPRESSION>
}

\\

\text{<LOGICAL\_AND\_EXPRESSION>} \to \text{
   <EQ\_EXPRESSION> |
   <LOGICAL\_AND\_EXPRESSION> AND <EQ\_EXPRESSION>
}

\\

\text{<EQ\_EXPRESSION>} \to \text{
   <INEQ\_EXPRESSION> |
   <EQ\_EXPRESSION> EQ <INEQ\_EXPRESSION>
}

\\

\text{<INEEQ\_EXPRESSION>} \to \text{
   <LIST\_EXPRESSION> |
   <INEQ\_EXPRESSION> INEQ <LIST\_EXPRESSION>
}

\text{<LIST\_EXPRESSION>} \to \text{
   <LIST\_EXPRESSION> |
   <INEQ\_EXPRESSION> INEQ <LIST\_EXPRESSION>
}

$$
