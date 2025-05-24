#I have created this file -Krati
from  django.http  import HttpResponse
#   return HttpResponse("hello Krati ")

#def about(request):
    #return HttpResponse('''<h1>exhello Krati</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Code with Harry</a>''')

#def fun(request):
   #file=open('textutils/fun.txt','r')
    #content=file.read()
    #file.close()
   # return HttpResponse(content,content_type = 'text/plain')
from django.shortcuts import render

def ex1(request):
    s = ''' Navigation Bar <br> </h2>
        <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
        <a href="https://www.facebook.com/"> Facebook </a> <br>
        <a href="https://www.flipkart.com/"> Flipkart </a> <br>
        <a href="https://www.hindustantimes.com/"> News </a> <br>
        <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)

def index(request):
    return render(request,'index2.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text','default')

    #Check Checkbox values
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #check which checkbox is ON
    if removepunc == "on" or fullcaps == "on" or newlineremover == "on" or extraspaceremover == "on":
        if(removepunc=="on"):
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed=""
            for char in djtext:
                if char not in punctuations:
                    analyzed= analyzed+char
            params={'purpose':'Remove Punctuations','analyzed_text': analyzed}
            djtext=analyzed
            #return render(request,'analyze2.html',params)



        if(fullcaps=='on'):
            analyzed=''
            for char in djtext:
                analyzed= analyzed+ char.upper()
            params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
            # Analyze the text
            djtext = analyzed
            #return render(request, 'analyze2.html', params)

        if(newlineremover=='on'):
            analyzed = ''
            for char in djtext:
                if char !="\n" and char!="\r":
                    analyzed = analyzed + char
            params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
            # Analyze the text
            djtext = analyzed
            #return render(request, 'analyze2.html', params)


        if(extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

            # Analyze the text
            djtext = analyzed
            #return render(request, 'analyze2.html', params)


    else:
        return HttpResponse("Error")

    return render(request, 'analyze2.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")