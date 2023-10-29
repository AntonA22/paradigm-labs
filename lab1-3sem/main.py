import math
import sys
class  roots:
    def __init__(self, A = 0.0, B = 0.0, C = 0.0):
        self.coef_A = A
        self.coef_B = B
        self.coef_C = C
        self.n_roots = 0
        self.roots = []
    def get_coef(self, index, line):
        try:
            i_coef = sys.argv[index]
            coef = float(i_coef)
            return coef
        except:
            print(line)
            while 1:
                try:
                    i_coef = float(input())
                    break
                except(ValueError, IndexError):
                    print("Введите корректное число для коэффициента.")
        return i_coef

    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def c_roots(self):
        if self.coef_A == 0:
            if self.coef_B == 0:
                if self.coef_C == 0:
                    print("Любое число")
                    return
                else:
                    print("Нет корней")
                    return
            else:
                xx = (-1) * self.coef_C / self.coef_B
                if xx < 0:
                    print("Нет корней")
                    return
                else:
                    roots = [math.sqrt(xx), (-1) * math.sqrt(xx)]
        else:
            D = self.coef_B ** 2 - 4 * self.coef_A * self.coef_C
            if D < 0:
                print("Нет корней")
                return
            else:
                x1 = ((-1) * self.coef_B - math.sqrt(D)) / (2 * self.coef_A)
                x2 = ((-1) * self.coef_B + math.sqrt(D)) / (2 * self.coef_A)
                if x1 >= 0:
                    self.roots.append(math.sqrt(x1))
                    self.roots.append(-math.sqrt(x1))
                if x2 >= 0:
                    self.roots.append(math.sqrt(x2))
                    self.roots.append(-math.sqrt(x2))
        if not self.roots:
            print("Нет корней")
            return
        unique_roots = list(set(self.roots))
        for root in unique_roots:
            print(root)


def main():
    r = roots()
    r.get_coefs()
    r.c_roots()
if __name__ == "__main__":
    main()
