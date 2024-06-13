from django.shortcuts import render
from django.http import HttpResponse

def input_view(request):
    if request.method == 'POST':
        user_input1 = int(request.POST.get('user_input1'))
        user_input2 = int(request.POST.get('user_input2'))
        return HttpResponse("Addition of two numbbers : %d"%(user_input1+user_input2))
    return render(request, 'inputapp/input_form.html')
# Create your views here.
