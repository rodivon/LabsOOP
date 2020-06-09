import re

sentence_counter = 1
word_counter = 1
char_counter = 1


class Text:
    text = ''
    def __init__(self, text, num, word):
        self.sentences = list()
        self.num = num
        self.word = word
        split_regex = re.compile(r'[.|!|?|…|\v]|\n')
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
        for s in sentences:
            self.sentences.append(s)
            Sentences(self.sentences[-1])
        print('Всі речення тексту: ', self.sentences)

    def main(self):
        n = self.num
        w = self.word
        self.result = ''
        for q in self.sentences:
            words = q.split(" ")
            for i in range(len(words)):
                if len(words[i]) == n:
                    words[i] = w
            for j in range(len(words)):
                self.result += words[j] + " "
        return self.result



class Sentences:
    def __init__(self, sentences):
        global sentence_counter
        self.words = list()
        split_regex = re.compile(r'[' '| : | ( | )| , |-]')
        words = filter(lambda t: t, [t.strip() for t in split_regex.split(sentences)])
        for s in words:
            self.words.append(s)
            Words(self.words[-1])
        print('Речення ', sentence_counter, self.words)
        sentence_counter += 1


class Words:

    def __init__(self, words):
        global sentence_counter, word_counter
        self.chars = list()
        for q in words:
            Text.text = Text.text + q
            self.chars.append(q)
            Chars(self.chars[-1])
        print('Слово ', word_counter, 'Речення ', sentence_counter, self.chars)
        word_counter += 1



class Chars:
    def __init__(self, chars):
        global sentence_counter, word_counter, char_counter
        self.chars2 = list()
        for z in chars:
            self.chars2.append(z)
        print('Символ ', char_counter, 'Слова ', word_counter, 'Речення ', sentence_counter, self.chars2)
        char_counter += 1



se = input('Введіть текст :')
numb = input('Введіть число знаків :')
wor = input('Бажане слово:')

nio = Text(text=se, num=int(numb), word=wor)
print('Готовий результат: ', nio.main())
