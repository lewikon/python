class MinMaxWordFinder:

    def __init__(self) -> None:
        self.some_list =[]

    def add_sentence(self, text: str):
        for word in text.split():
            self.some_list.append(word)

    def shortest_words(self):
        return [x for x in self.some_list if len(x) == min(map(len, self.some_list))]

    def longest_words(self):
        return [x for x in self.some_list if len(x) == max(map(len, self.some_list))]

finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence("def asdf qwert")
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))