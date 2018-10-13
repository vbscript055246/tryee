class Ploynomial:

    def __init__(self, item):
        self.Term = item.copy()

    def __add__(self, other):
        ans = Ploynomial(self.Term)
        for (e, c) in other.Term.items():
            if ans.Term.get(e) is not None:
                ans.Term[e] += c
            else:
                ans.Term[e] = c
        ans.flush()
        return ans

    def __str__(self):
        temp = ""
        for e in sorted(self.Term.keys(), reverse=True):
            if e == 1:
                temp += (str(self.Term[e]) + "x+")
            elif e:
                temp += (str(self.Term[e]) + "x^" + str(e) + "+")
            else:
                temp += str(self.Term[e])
        temp = temp.rstrip("+")
        return temp

    def flush(self):
        for e in self.Term.copy():
            if self.Term[e] == 0:
                self.Term.pop(e)


a = Ploynomial({8: 8, 1: 8})
b = Ploynomial({8: -8, 2: 8})
c = Ploynomial({5: 8, 3: 8})
print(a+b+c)
print(a)
