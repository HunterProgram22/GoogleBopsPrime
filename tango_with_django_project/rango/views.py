from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its content.
    # Note the key boldmessage is the same as {{ boldmessage }} in template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'aboutme': """My name is Justin Kudela and this is one of my
                    first forays into building a website""",
                    'abouthunter': """My son's name is Hunter and he is a pretty 
                    awsome kid!"""}
    return render(request, 'rango/about.html', context=context_dict)

