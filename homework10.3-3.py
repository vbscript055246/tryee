from operator import attrgetter


class Term:

    def __init__(self, ncoef, nexp):
        self.c = ncoef
        self.e = nexp


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


a = Ploynomial([Term(8, 8), Term(8, 1)])
b = Ploynomial([Term(8, 8), Term(8, 2)])
c = Ploynomial([Term(8, 5), Term(8, 3)])
print(a+b+c)