# 1. Написать функцию num_translate(), 
# переводящую числительные от 0 до 10 
# c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def num_translate(num):
    num_dict  = {
        "one":"один",
        "two":"два",
        "tree":"три",
        "four":"четыре",
        "five":"пять",
        "six":"шесть",
        "seven":"семь",
        "eight":"восемь",
        "nine":"девять",
        "ten":"десять"}
    if num[0].islower():
        return num_dict.get(num)
    elif num[0]:
        num = num.lower()
        return num_dict[num].capitalize()

print(num_translate('Ten'))