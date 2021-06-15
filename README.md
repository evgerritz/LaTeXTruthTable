# LaTeX Truth Table
Generates a well formatted and highly readable truth table in LaTeX for any propositional formula. This truth table will also include all intermediate values of every nested propositional formula, skipping propositional variables.

# Usage
Accepted operators (uppercase or lowercase):  
`NOT, OR, AND, XOR, IFF, IMPLIES, NOR, NAND`

The following symbols are also aliased to the previous operators:  
`NOT: ~, !, <>`  
`OR: |, +`  
`AND: &, *`  
`XOR: ^`  
`IMPLIES: =>, ->`  
`IFF: <=>, <->`  

A propositional formula is defined as follows:  
Any string of letters (except for those strings which are also operators) is a propositional formula.  
If p and q are propositional formulae, then the following are also propositional formulae:
```
NOT p
p OR q
p AND q
p XOR q
p IFF q
p IMPLIES q
```
Parentheses can be added around any nested or top-level PF to control the order of evaluation. If no parentheses are present, evaluation will be determined by the following precedence hierarchy (from highest to lowest precedence, all operators assume right-to-left associativity):
1. `NOT`  
2. `AND`  
3. `XOR/NOR/NAND`  
4. `OR`  
5. `IMPLIES/IFF`  


Example usage:  
```
(a OR b) IFF (b AND (NOT (c AND d)))
=> '\begin{tabular}{ c c c c | c c c c c c c c c c c }
	 a & b & c & d & $( a &\lor& b ) &\iff& ( b &\land& ( &\neg& ( c &\land& d ) ) )$\\ 
	 \hline 
	 0 & 0 & 0 & 0 && 0 && 1 && 0 && 1 && 0 \\ 
	 0 & 0 & 0 & 1 && 0 && 1 && 0 && 1 && 0 \\ 
	 0 & 0 & 1 & 0 && 0 && 1 && 0 && 1 && 0 \\ 
	 0 & 0 & 1 & 1 && 0 && 1 && 0 && 0 && 1 \\ 
	 0 & 1 & 0 & 0 && 1 && 1 && 1 && 1 && 0 \\ 
	 0 & 1 & 0 & 1 && 1 && 1 && 1 && 1 && 0 \\ 
	 0 & 1 & 1 & 0 && 1 && 1 && 1 && 1 && 0 \\ 
	 0 & 1 & 1 & 1 && 1 && 0 && 0 && 0 && 1 \\ 
	 1 & 0 & 0 & 0 && 1 && 0 && 0 && 1 && 0 \\ 
	 1 & 0 & 0 & 1 && 1 && 0 && 0 && 1 && 0 \\ 
	 1 & 0 & 1 & 0 && 1 && 0 && 0 && 1 && 0 \\ 
	 1 & 0 & 1 & 1 && 1 && 0 && 0 && 0 && 1 \\ 
	 1 & 1 & 0 & 0 && 1 && 1 && 1 && 1 && 0 \\ 
	 1 & 1 & 0 & 1 && 1 && 1 && 1 && 1 && 0 \\ 
	 1 & 1 & 1 & 0 && 1 && 1 && 1 && 1 && 0 \\ 
	 1 & 1 & 1 & 1 && 1 && 0 && 0 && 0 && 1 \\ 
    \end{tabular}'
```



