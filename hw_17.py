
sentence = input("Your sentence: ")

def correct_sentence(text):
    fin = text[-1]
    if fin != ".":
        # text = "{text.capitalize()}.".format(text=text)  #alternative
        text = text.capitalize() + "."
        print(text)
    else:
        print(text.capitalize())

correct_sentence(sentence)