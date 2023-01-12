from textblob import TextBlob


def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text

#
# def bubble_sort(list):
#     for i in range(len(list)):
#         for j in range(len(list)-i-1):
#             if list[j] > list[j + 1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j + 1] = temp
#     return list


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list