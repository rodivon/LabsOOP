# 9212
# C3=2, Тип текстових змінних -> String
# C17=15, Дія з рядком -> В заданому тексті замінити слова заданої довжини визначеним рядком

class Main:
    def __init__(self, sentence, number, word):
        self.number = number
        self.sentence = sentence
        self.word = word
        self.result = ''

    def main(self):
        s = self.sentence
        n = self.number
        w = self.word
        words = s.split(" ")
        print(words)
        for i in range(len(words)):
            if len(words[i]) == n:
                words[i] = w
        for j in range(len(words)):
            self.result += words[j] + " "
        return self.result

    def start(self):
        print(self.main())


se = input('Введіть текст :')
numb = input('Введіть число знаків :')
wor = input('Бажане слово:')
nio = Main(sentence=se, number=int(numb), word=wor)
nio.start()



