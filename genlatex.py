from ttable import getvars, binarycount, makeprefix, sub_into_exp, combineevals
import parser

#gentable: returns the main rows of the truth table 
#           where each row consists of the values of variables
#           followed by the evaluations of the PFS with those values
def gentable(listpf, textrepr, varlst):
    table = []

    numVars = len(varlst)
    inputs = binarycount(numVars)

    for binstr in inputs:
        temp = makeprefix(parser.splitByPrecedence(sub_into_exp(textrepr, binstr)))
        allowSingles = True if temp in ('0', '1') else False
        result = combineevals(temp, allowSingles)
        table.append(binstr + result)
    return table

#latexexp: converts the word-based OPs in exp to LaTeX commands
def latexexp(exp):
    exp = exp.replace('(', '( ')
    exp = exp.replace(')', ' )')
    exp = exp.replace(' AND', ' &\\land&')
    exp = exp.replace('XOR', ' &\\oplus&')
    exp = exp.replace(' OR', '&\\lor&')
    exp = exp.replace('NOT', '&\\neg&')
    exp = exp.replace('IMPLIES', '&\\rightarrow&')
    exp = exp.replace('IFF', '&\\iff&')
    exp = exp.replace('NOR', '&NOR&')
    exp = exp.replace('NAND', '&NAND&')
    return exp
    

#genlatex: produces a truth table formatted in LaTeX for exp
def genlatex(textrepr, listpf, varlst, texttable):
    numVars = len(varlst)
    latex = "\\begin{tabular}{"

    for _ in varlst:
        latex += " c"
    latex += " | c"

    for _ in texttable[0][numVars:]:
        latex+= " c c"
    latex += " }\n"

    latex += "\t "
    for var in varlst:
        latex += var +" & "

    latex += "$"
    latex += latexexp(textrepr)
    latex += "$\\\\ \n"
    latex += "\t \\hline \n"

    for row in texttable:
        latex += "\t "
        for i in range(numVars-1):
            latex += row[i] + " & "
        for i in range(numVars-1, len(row)):
            latex += row[i] + " && "
        latex = latex[:-3] + "\\\\ \n"

    latex += "\\end{tabular}"

    return latex

