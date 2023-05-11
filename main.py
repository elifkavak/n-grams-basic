import re
from tkinter import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
#nltk.download("punkt")
#nltk.download('stopwords')

pencere = Tk(className='N-grams')
pencere.geometry("500x500")

def n_gram():
    name =entry.get()
    name = name.lower()
    name = re.sub(r'[^a-zA-Z0-9\s]', ' ', name)
    stop_words = set(stopwords.words('english'))
    token = word_tokenize(name)
    filtered = []
    for w in token:
        if w not in stop_words:
            filtered.append(w)
    s = entry2.get()
    s = int(s)
    n_grams = list(ngrams(filtered, s))
    print(n_grams)
    return n_grams

label=Label(pencere)
label.config(text="Paragraph : ",font=("Arial",10))
label.place(x=10,y=70)

entry=Entry(pencere, width=60)
entry.place(height="60")
entry.place(x=100,y=70)

label=Label(pencere)
label.config(text="Enter n values: ",font=("Arial",10))
label.place(x=10,y=140)

entry2=Entry(pencere, width=30)
entry2.place(x=100,y=140)

buton=Button(pencere)
buton.config(text="Entire",bg="black",fg="white",command=n_gram)
buton.place(x=20,y=210)

mainloop()