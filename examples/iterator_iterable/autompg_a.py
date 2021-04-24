class AutoMPG:
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg


class AutoMPGData:
    def __init__(self):
        self.data = []

    def _load_data(self):
        autompg1 = AutoMPG("ford", "clunker", 1960, 2)
        autompg2 = AutoMPG("bmw", "salesy", 2020, 10)
        self.data.append(autompg1)
        self.data.append(autompg2)
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration()
        return self.data[self.index]


def main():
    for auto in AutoMPGData():
        print(str(auto), auto.make, auto.model, auto.year, auto.mpg)


if __name__ == "__main__":
    main()
