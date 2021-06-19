class Estenes:
    def estenes(self, data):
        def prime_number(data, i):
            if i >= len(data): return data
            d = data[i]
            data = [x for x in data if (x == d or x % d != 0)]
            i += 1
            return prime_number(data, i)
        return prime_number(data, 0)

data = [i for i in range(2, 100)]
estenes = Estenes()
print(estenes.estenes(data))