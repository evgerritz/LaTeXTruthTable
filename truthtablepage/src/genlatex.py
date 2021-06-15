from src.ttable import getvars, binarycount, makeprefix, sub_into_exp, combineevals
import src.parser as parser

#gentable: returns the main rows of the truth table 
#           where each row consists of the values of variables
#           followed by the evaluations of the PFS with those values
def gentable(textrepr, numVars, verbose=False):
    table = []

    inputs = binarycount(numVars)

    for binstr in inputs:
        RHS = makeprefix(parser.splitByPrecedence(sub_into_exp(textrepr, binstr)))
        verbose = verbose or RHS in ('0', '1') 
        result = combineevals(RHS, verbose)
        table.append(binstr + result)
    return table

#latexexp: converts the word-based OPs in exp to LaTeX commands
def latexexp(exp, varlst, verbose=False):
    terminalAligner = '&' if not verbose else ''
    exp = exp.replace('(', '( ')
    exp = exp.replace(')', ' )')
    exp = exp.replace(' AND', ' &\\land' + terminalAligner)
    exp = exp.replace('XOR', ' &\\oplus' + terminalAligner)
    exp = exp.replace(' OR', ' &\\lor' + terminalAligner)
    exp = exp.replace('NOT', '&\\neg' + terminalAligner)
    exp = exp.replace('IMPLIES', '&\\rightarrow' + terminalAligner)
    exp = exp.replace('IFF', '&\\iff' + terminalAligner)
    exp = exp.replace('NOR', '&NOR' + terminalAligner)
    exp = exp.replace('NAND', '&NAND' + terminalAligner)

    if verbose:
        for var in varlst:
            exp = exp.replace(f' {var} ', f' &{var} ')

    return exp
    

#genlatex: produces a truth table formatted in LaTeX for exp
def genlatex(textrepr, listpf, varlst, texttable, verbose=False):
    numVars = len(varlst)
    latex = "$\\begin{array}{"

    for _ in varlst:
        latex += " c"
    latex += " | c" if not verbose else " | c c"

    for _ in texttable[0][numVars:]:
        latex+= " c c" if not verbose else " c"
    latex += " }\n"

    latex += "\t"
    for var in varlst:
        latex += var +" & "

    latex += latexexp(textrepr, varlst, verbose)
    latex += "\\\\ \n"
    latex += "\t\\hline \n"

    varSep = " & "
    valSep = " && " if not verbose else varSep
    for row in texttable:
        latex += "\t"
        for val in row[:numVars]:
            latex += val + varSep
        latex=latex[:-3]
        latex += " &" if verbose else ""
        for val in row[numVars:]:
            latex += valSep + val
        latex += " \\\\ \n"
            
    latex += "\\end{array}$"

    return latex

if __name__ == '__main__':
    def tablewrapper(rawtext):
        return gentable(parser.textrepr(rawtext), getvars(rawtext), verbose=True)
