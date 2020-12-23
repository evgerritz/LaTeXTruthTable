from  ttable import *

def gentable(exp):
    table = []

    varlst = getvars(exp)
    numVars = len(varlst)
    inputs = binarycount(numVars)

    for binstr in inputs:
        temp = makeprefix(parenstolist(sub_into_exp(exp, binstr)))
        result = combineevals(temp)
        table.append(binstr + result)
    return table

def latexexp(exp):
    exp = exp.replace('(', '( ')
    exp = exp.replace(')', ' )')
    exp = exp.replace('AND', '&\\land&')
    exp = exp.replace('XOR', '&\\oplus&')
    exp = exp.replace('OR', '&\\lor&')
    exp = exp.replace('NOT', '&\\neg&')
    exp = exp.replace('IMPLIES', '&\\rightarrow&')
    exp = exp.replace('IFF', '&\\iff&')

    return exp
    

def genlatex(exp):
    varlst = getvars(exp)
    numVars = len(varlst)
    table = gentable(exp)
    latex = "\\begin{tabular}{"

    for _ in varlst:
        latex += " c"
    latex += " | c"

    for _ in table[0][numVars:]:
        latex+= " c c"
    latex += " }\n"

    latex += "\t "
    for var in varlst:
        latex += var +" & "

    latex += "$"
    latex += latexexp(exp)
    latex += "$\\\\ \n"
    latex += "\t \\hline \n"

    for row in table:
        latex += "\t "
        for i in range(numVars-1):
            latex += row[i] + " & "
        for i in range(numVars-1, len(row)):
            latex += row[i] + " && "
        latex = latex[:-3] + "\\\\ \n"

    latex += "\\end{tabular}"

    return latex


while True:     
    exp = input("Enter Boolean expression: ")
    print(genlatex(exp))
