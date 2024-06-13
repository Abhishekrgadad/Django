from django.shortcuts import render
from django.http import HttpResponse

def input_view(request):
    if request.method == 'POST':
        user_input1 = int(request.POST.get('user_input1'))
        user_input2 = int(request.POST.get('user_input2'))
        value1 = user_input1 + user_input2
        value2 = user_input1 - user_input2
        value3 = user_input1 * user_input2
        value4 = user_input1 / user_input2

        str1 = "Addition of two numbers %d and %d is %d " % (user_input1, user_input2, value1)
        str2 = "Difference of two numbers %d and %d is %d " % (user_input1, user_input2, value2)
        str3 = "Multiplication of two numbers %d and %d is %d" % (user_input1, user_input2, value3)
        str4 = "Division of two numbers %d and %d is %.2f " % (user_input1, user_input2, value4)
        str = str1 + "<br>" + str2 + "<br>" + str3 + "<br>" + str4
        return HttpResponse(str)
    return render(request, 'airthmetapp/index.html')