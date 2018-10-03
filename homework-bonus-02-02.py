from operator import attrgetter


class Term:

    def __init__(self, ncoef, nexp):
        self.c = ncoef
        self.e = nexp

    def __eq__(self, other):
        return self.e == other.e and self.c == other.c

    def __mul__(self, other):
        return Term(self.c*other.c, self.e*other.e)


class Ploynomial:

    def __init__(self, item):
        self.item = item

    def __add__(self, other):
        for i in other.item:
            tmp = self.get(i.e)
            if tmp is None:
                self.item.append(i)
            else:
                tmp.c += i.c

        self.item.sort(key=attrgetter('e'), reverse=True)
        return Ploynomial(self.item)

    def __mul__(self, other):
        ans = Ploynomial([])
        for i in self.item:
            for j in other.item:
                ans.addATerm(i*j)
        return Ploynomial(ans.item)

    def __str__(self):
        temp = ""
        for item in self.item:
            if item.e == 1:
                temp += (str(item.c) + "x+")
            elif item.e:
                temp += (str(item.c) + "x^" + str(item.e) + "+")
            else:
                temp += str(item.c)
        temp = temp.rstrip("+")
        return temp

    def get(self, e):
        for item in self.item:
            if item.e == e:
                return item
            if item.e < e:
                return None
        return None

    def addATerm(self, newTerm):
        tmp = self.get(newTerm.e)
        if tmp is not None:
            tmp.c += newTerm.c
        else:
            self.item.append(newTerm)
            self.item.sort(key=attrgetter('e'), reverse=True)

    def removeATerm(self, Term):
        for index, item in enumerate(self.item):
            if item == Term:
                del self.item[index]

    def printPolynomial(self):
        print(self)


a = Ploynomial([Term(8, 8), Term(8, 1)])
b = Ploynomial([Term(8, 8), Term(8, 2)])
c = Ploynomial([Term(8, 5), Term(8, 3)])
print(a*b+c)
T = a*b+c
T.removeATerm(Term(64, 2))
T.printPolynomial()