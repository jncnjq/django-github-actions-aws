from django.http import HttpResponse

def home(request):
   text = """<h1>Mind blowing super mega everyhomepage!</h1>"""
   return HttpResponse(text)