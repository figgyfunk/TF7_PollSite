from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Question, Choice, Arch
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
import json



def index(request):

    return render(request, 'poll/index.html', {'question_list': Question.objects.all()})


def vote(request):
    all_checked = True
    choices = []

    for question in Question.objects.all():
        try:
            selected_choice = question.choice_set.get(pk=request.POST[question.question_text])
            if question.question_text == "Which Personality Type Do You Match Up With?":
                a = Arch.objects.get(name__startswith=selected_choice.choice_text)
            elif question.question_text == "What Month Were You Born In?":
                if selected_choice.choice_text == "January":
                    a.jan += 1
                elif selected_choice.choice_text == "February":
                    a.feb += 1
                elif selected_choice.choice_text == "March":
                    a.mar += 1
                elif selected_choice.choice_text == "April":
                    a.apr += 1
                elif selected_choice.choice_text == "May":
                    a.may += 1
                elif selected_choice.choice_text == "June":
                    a.jun += 1
                elif selected_choice.choice_text == "July":
                    a.jul += 1
                elif selected_choice.choice_text == "August":
                    a.aug += 1
                elif selected_choice.choice_text == "September":
                    a.sep += 1
                elif selected_choice.choice_text == "October":
                    a.oct += 1
                elif selected_choice.choice_text == "November":
                    a.nov += 1
                elif selected_choice.choice_text == "December":
                    a.dec += 1
            else:
                if selected_choice.choice_text == "Marketing":
                    a.mark += 1
                elif selected_choice.choice_text == "Account":
                    a.acc += 1
                elif selected_choice.choice_text == "Executive":
                    a.exec += 1
                elif selected_choice.choice_text == "Design":
                    a.des += 1
                else:
                    a.pro += 1

        except (KeyError, Choice.DoesNotExist):
            all_checked = False
        else:
            selected_choice.votes += 1
            choices.append(selected_choice)
    if all_checked:
        a.save()
        for c in choices:
            c.save()
        return HttpResponseRedirect('/results/')
    else:
        return render(request, 'poll/index.html', {'question_list': Question.objects.all()})

def results(request):
    personalities = {}
    question = Question.objects.get(pk=1)
    for choice in question.choice_set.all():
        personalities[choice.choice_text] = choice.votes
    json.dumps(personalities)

    months = {}
    for arch in Arch.objects.all():
        months[arch.name] = [arch.jan, arch.feb, arch.mar, arch.apr, arch.may, arch.jun, arch.jul, arch.aug, arch.sep, arch.oct, arch.nov, arch.dec]

    json.dumps(months)

    context = {
        'personalities' : personalities,
        'months' : months,
    }
    return render(request, 'poll/results.html', context)
