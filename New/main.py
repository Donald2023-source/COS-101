from tkinter import Label
hausa_dict = {
    "come": 'zo',
    "go" : "Je",
    "sit": "Zauna",
    "eat": "ci"
}

def search(word):
    if word in hausa_dict
        result.set(hausa_dict[word])
        print(hausa_dict[word])
    else:
        result.set('Not Found')
        print("Not found")

search_btn = Button(window, text="Search", command = lambda, search(entry_text.get()))
search_btn.pack()

result = stringVar()
result_label = Label()