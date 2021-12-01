#Este código convierte un número entero a número romano
#Juvenal Rafael Mercado Cano
#A01730700

class Romanos:
    numeroRomano = ''

    def intRomanos(self, num: int) -> str:
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        symbols = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        for value, symbol in zip(values, symbols):
            num = self.convertirLetras(num, value, symbol)

        return self.numeroRomano
        
    def convertirLetras(self, num: int, value: int, symbol: str) -> int:
        out = num // value
        self.numeroRomano += symbol * out
        return num - (out * value)

if __name__ == '__main__':
    r = Romanos()

    n = 0
    n = int(input())
    print(r.intRomanos(n))
  