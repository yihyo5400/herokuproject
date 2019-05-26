from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request, 'index.html')

def about (request):
    return render (request, 'about.html')

def result (request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    li = list(text)
    letter = []

    for i in li:
        if i != ' ':
            letter.append(i) #letter에 i 항목을 추가해라

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    return render (request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items(), 'letters' : len(letter)})