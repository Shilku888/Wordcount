from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist =  fulltext.split()
    worddict ={}
    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            worddict[word] = 1
    sortedwords = sorted(worddict.items(),key=operator.itemgetter(1),reverse= True)
    c = len(wordlist)
    return render(request,'count.html',{'fulltext':fulltext,'count':c,'sortedwords':sortedwords})

about1 = "So you are in About Page"
def about(request):
    return render(request,'about.html',{'ab':about1})
