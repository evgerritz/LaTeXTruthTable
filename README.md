# LaTeXTruthTable
Generates a truth table in LaTeX for any boolean expression. This truth table will also include all intermediate values of every nested boolean expression, skipping boolean variables.

# Usage
Accepted operators:
`NOT, OR, AND, XOR, IFF, IMPLIES`

A Boolean expression is defined as follows:  
Any string of letters (except for those strings which are also operators) is a Boolean expression.  
If p and q are Boolean expressions, then the following are also Boolean expressions:
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
((a XOR b) AND (c IMPLIES d)) AND (NOT c)'))
\begin{tabular}{ c c c c | c c c c c c c c c }
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
\end{tabular}
```
