
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def analyze(request):
    text=request.POST.get('text','defalut')
    textpunc=request.POST.get('puncheck','off')
    uppercase=request.POST.get('uppercase', 'off')
    newline=request.POST.get('newline','off')
    extraspace=request.POST.get('extraspace','off')
    punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    
    if textpunc == 'on':
        analyzed =" "
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        param = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        text = analyzed
    
    if (uppercase == 'on'):
            analyzed =" "
            for char in text:
                analyzed = analyzed + char.upper()
            param = {'purpose':'Upper Case','analyzed_text':analyzed}
            text = analyzed    
    
    if(newline == 'on'):
        analyzed =" "
        for char in text:
              if char !='\n' and char !='\r':
                   analyzed = analyzed + char
        param = {'purpose':'New Line','analyzed_text':analyzed}
        text = analyzed

    if(extraspace == 'on'):
        analyzed =" "
        for index, char in enumerate(text):
              if index + 1 < len (text) and not (text[index] == " " and text[index+1] == " "):
                   analyzed = analyzed + char
        param = {'purpose':'Remove Extra Space','analyzed_text': analyzed}
    else:
         if(textpunc!='on' and uppercase!='on' and  newline!='on' and  extraspace!='on'):
              return HttpResponse("Error !!! Select the text analyzer options")
    return render(request,'analyze2.html',param)
              
