# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from first_app.models import Program, Student

import os

clicked = 1

program_values = Program.objects.all()


def index(request):
    fruits = ['apple', 'banana', 'kiwi', 'guava', 'mango']
    my_dict = {"fruits_list": fruits}
    return render(request, 'index.html', my_dict)


def help(request):
    return render(request, "help.html")


def process_form(request):
    username = request.GET.get('user')
    password = request.GET.get('pwd')
    print(username, password)
    return render(request, 'form.html')


def get_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            s_name = form.cleaned_data['name']
            s_roll = form.cleaned_data['roll']
            s_year = form.cleaned_data['year']
            s_degree = form.cleaned_data['degree']
            s_branch = form.cleaned_data['branch']
            return HttpResponseRedirect('/student/')

            p = Program.objects.get(title=s_degree, branch=s_branch)

            if p != None:
                s = Student(roll_number=s_roll,
                            name=s_name,
                            year=s_year)

    else:
        form = StudentForm()
        return render(request, 'studentForm.html', {'form': form})


def code_eval(request):
    if request.method == "POST":

        pycode = request.POST['code']

        print(repr(pycode))

        wDir = "/home/advait/Documents"

        os.system(f"rm -r {wDir}/code.py")
        os.system(f'touch {wDir}/code.py')
        os.system(f'echo {pycode} > {wDir}/code.py')
        os.system(f'cat {wDir}/code.py')

        return render(request, 'codeOutput.html')

    else:
        return render(request, 'codeEval.html')


def crud(request):
    my_dict = {
        "program_rows": program_values
    }
    return render(request, 'crud.html', my_dict)
