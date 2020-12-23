# LaTeXTruthTable
Generates a truth table in LaTeX for any propositional formula. This truth table will also include all intermediate values of every nested propositional formula, skipping propositional variables.

# Usage
Accepted operators:
`NOT, OR, AND, XOR, IFF, IMPLIES`

A propositional formula is defined as follows:  
Any string of letters (except for those strings which are also operators) is a propositional formula.  
If p and q are propositional formulae, then the following are also propositional formulae:
```
(NOT p)
(p OR q)
(p AND q)
(p XOR q)
(p IFF q)
(p IMPLIES q)
```

The top-level parentheses are optional.

Example usage:  
```
((a XOR b) AND (c IMPLIES d)) AND (NOT c)
=> '\begin{tabular}{ c c c c | c c c c c c c c c }
	 a & b & c & d & $( ( a \oplus b ) &\land ( c &\rightarrow d ) ) &\land ( &\neg c )$\\
	 \hline
	 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1\\
	 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1\\
	 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
	 0 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0\\
	 0 & 1 & 0 & 0 & 1 & 1 & 1 & 1 & 1\\
	 0 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 1\\
	 0 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 0\\
	 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0\\
	 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1\\
	 1 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1\\
	 1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0\\
	 1 & 0 & 1 & 1 & 1 & 1 & 1 & 0 & 0\\
	 1 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1\\
	 1 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & 1\\
	 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
	 1 & 1 & 1 & 1 & 0 & 0 & 1 & 0 & 0\\
   \end{tabular}'
```
