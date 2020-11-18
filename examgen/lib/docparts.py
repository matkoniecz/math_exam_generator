def doc_parts(title="", author=""):
    start="""
    \documentclass{article}
    \usepackage{amsfonts}""" + magic_incantation_to_allow_polish_letters() + """
    \usepackage{amsmath,multicol,eso-pic}
    \\begin{document}
    """

    if title:
        start = start + "\\title{%s} \n \date{\\vspace{-5ex}} \n \maketitle" % title

    end="""
    \end{document}
    """
    return start, end

def exam_parts(title="", author=""):
    start="""
    \\documentclass{exam}
    \\usepackage{amsfonts}""" + magic_incantation_to_allow_polish_letters() + """
    \\usepackage{amsmath,multicol,eso-pic}
    \\noprintanswers
    \\addpoints 
    \\qformat{\\textbf{Question \\\\ \\thequestion}\\quad(\\thepoints)\\hfill}
    \\usepackage{color}
    \\definecolor{SolutionColor}{rgb}{0.8,0.9,1} 
    \\shadedsolutions 
    \\renewcommand{\\solutiontitle}{\\noindent\\textbf{Solution:}\\par\\noindent}

    \\begin{document}
    \\AddToShipoutPicture{
        \\AtTextUpperLeft{
        \\makebox(400,45)[lt]{ 
          \\footnotesize
          \\begin{tabular}{r@{\\,}l}
            Name:  & \\rule{0.5\\linewidth}{\\linethickness} \\\\[.5cm]
            Date:  & \\rule{0.5\\linewidth}{\\linethickness} \\\\
          \end{tabular}
    }}}
    \\begin{minipage}{.8\\textwidth}
    This exam includes \\numquestions\\ questions. The total number of points is \\numpoints.
    \\end{minipage}
    \\begin{questions}
    """

    end = """\end{questions}
    \end{document}
    """
    return start, end

def magic_incantation_to_allow_polish_letters():
    # as UTF8 is not supported by default a special incantation is needed
    # https://tex.stackexchange.com/questions/268824/ways-to-input-special-characters-polish-alphabet#268854
    return """
    \\usepackage[T1]{fontenc}
    \\usepackage[polish]{babel}
    \\usepackage[utf8]{inputenc}"""

def section_parts(title, instr="", cols = 2):
    if cols >= 2:
        section_start="""
        \\section{%s}
        %s
        \\begin{multicols}{%s}
        \\begin{enumerate}
        """ % (title, instr, str(cols))

        section_end="""
        \\end{enumerate}
        \\end{multicols}
        """
    else:
        section_start = """
        \\section{%s}
        %s
        \\begin{enumerate}
        """ % (title, instr)
        section_end = """
        \\end{enumerate}
        """
    return section_start, section_end


def problem(instructions, problem, solution, points=1):
    code = """
    \\question[%s]
        %s
        %s
    \\begin{solution} 
        %s
    \\end{solution}
    """ % (str(points), instructions, problem, solution)
    return code

if __name__ == "__main__":
    print problem("test", "fasd", "asdfasd", 10)





