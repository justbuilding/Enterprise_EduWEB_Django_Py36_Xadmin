from django.shortcuts import render

# Create your views here.


def get_form(request):
    # 注意form.html内置有重名，需改为其他如message_form.html
    return render(request, 'message_form.html')
