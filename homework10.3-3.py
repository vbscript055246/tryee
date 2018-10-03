class Term:

    def __init__(self, ncoef, nexp):
        self.c = ncoef
        self.e = nexp


class Ploynomial:

    def __init__(self, item):
        self.item = item

    def __add__(self, other):
        for i in other.item:
            if self.item.get(i.e) == None:
                self.item[i.e] = i.c
            else:
                self.item[i.e].c += i.c

    def __str__(self):
        temp = ""
        for item in self.item:
            if item.e:
                temp += (str(item.c) + "x^" + str(item.e) + "+")
            else:
                temp += str(item.c)
        temp = temp.rstrip("+")
        return temp

print(Ploynomial([Term(8, 8), Term(8, 0)]))