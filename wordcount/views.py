from django.http import request
from django.shortcuts import render
import operator


def aboutme(request):
    return render(request, 'aboutme.html') 

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext'] 
    word_list = fulltext.split() 
    word_dictionary = {} 
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
#    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'worddictionary': sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)})