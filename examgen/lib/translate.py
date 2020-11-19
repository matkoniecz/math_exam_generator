# encoding: utf-8
def language():
    return "pl"

def solve_for(unknown_name, equation):
    if language() == "en":
        return "Solve for $%s$ : %s" % (unknown_name, equation)
    if language() == "pl":
        return "Rozwiąż dla $%s$ : %s" % (unknown_name, equation)
    raise "unhandled language"
