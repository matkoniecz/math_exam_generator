# encoding: utf-8
from examgen import worksheet, make_quotient_rule_prob

# make an exam with a filename and title
myexam = worksheet("zadania", "Zadania", savetex=True)


myexam.add_section("Simple linear equations", 40, "",
                   "Równania do rozwiązania, wykonaj sprawdzenie poprawności rozwiązania. Wynik niekoniecznie jest liczbą całkowitą.")

"""
# add some problem sections 
myexam.add_section("Simple linear equations", 70, "",
                   "Równania do rozwiązania, wykonaj sprawdzenie poprawności rozwiązania. Wynik niekoniecznie jest liczbą całkowitą.")

myexam.add_section("Linear equations", 6, "",
                   "Równania do rozwiązania, wykonaj sprawdzenie poprawności rozwiązania. Wynik niekoniecznie jest liczbą całkowitą.")
"""

# generate the exam and solutions pdf
myexam.write()