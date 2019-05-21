from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.forms import modelformset_factory
from django.forms import modelform_factory

# Create your views here.
import ast

from .models import Question, RK, RKResult

"""class QuestionCreateView(CreateView):
    model = QuestionsTest
    template_name = "new_question.html"
    fields = ['body', 'answers', 'answer_true']

    def form_valid(self, form):
        obj = form.save(commit=False)
        #obj.author = self.request.user
        #obj.date = timezone.now()

        obj.save()

        return super().form_valid(form)"""


class RKListView(ListView):
    model = RK
    template_name = 'rk_list.html'

    #def get_context_data(self, *args, **kwargs):
    #    all_rks = self.model.objects.all()
    #    context = super(RKListView, self).get_context_data(*args, **kwargs)
    #    context['rk_res'] = RKResult.objects.filter(rk__in=all_rks.id)
    #
        #return context

    def get_queryset(self):
        return self.model.objects.order_by('-date_start')


class RKCreateView(CreateView):
    model = RK
    template_name = 'rk_new.html'
    fields = ['name', 'disciple', 'date_start', 'date_stop']

    def form_valid(self, form):

        obj = form.save(commit=False)
        obj.save()

        return super().form_valid(form)


def add_questions(request, rk_id):
    rk = RK.objects.get(pk=rk_id)
    QuestionsFormset = modelformset_factory(Question, fields=('name', 'body', 'answer_true'))

    if request.method == "POST":

        formset = QuestionsFormset(request.POST, queryset=Question.objects.filter(rk__id=rk.id))
        if formset.is_valid():
            instances = formset.save(commit=False)

            for instance in instances:
                instance.rk_id = rk.id
                instance.save()

            return redirect('question_new', rk_id = rk.id)

    formset = QuestionsFormset(queryset=Question.objects.filter(rk__id=rk.id))

    return render(request, "new_question.html", {'formset': formset})


def rk_solving(request, rk_id):
    rk = RK.objects.get(pk=rk_id)
    questions = rk.question_set.all()

    true_answers = [val.answer_true for val in questions]
    #print(f"True answers: {true_answers}")

    QuestionsForm = modelform_factory(Question, fields=('answer_true',))

    if request.method == "POST":

        form = QuestionsForm(request.POST)

        if form.is_valid():
            instances = form.save(commit=False)

            student = request.user
            #QueryDict: {'csrfmiddlewaretoken': ['41T0Y1sJINbkLF8HWgUFzpFQAeXN68bOZC1LZs2PXUpEVlKzrKkuGSwO7hYeOx63'], 'answer_true': ['A', 'C']}
            #print(request.POST)
            student_answers = str(request.POST).split(': ')[-1][:-2]
            answers = list(ast.literal_eval(student_answers))
            #print(f"Student answers: {answers}")

            res = 0

            for answer, answ_tr in zip(answers, true_answers):
                #print("It 1: ", answer, answ_tr)
                if answer == answ_tr:
                    res += 1

            result = f"{round(res*100/len(true_answers), 3)} %"
            #print(f"{round(res/len(true_answers))*100} %")
            #instances.save()
            obj = RKResult.objects.create(
                student=student,
                rk=rk,
                result=result,
                answers=f"{answers}"
            )

            #print(list(zip(questions, answer)))
            #context={'questions_answers': list(zip(questions, answer))}

            return redirect('rk_result', obj.id)

    form = QuestionsForm()

    return render(request, "rk_solving.html", {'rk': rk, 'questions': questions, 'form': form})

#class RKResultView(DetailView):
#    model = RKResult
#    template_name = "rk_result.html"


def RKResultDetail(request, **kwargs):
    obj = RKResult.objects.get(pk=kwargs.get("pk"))
    rk_questions = obj.rk.question_set.all()
    rk_true_answers = [el.answer_true for el in rk_questions]
    rk_questions = [el.body for el in rk_questions]
    rk_answers = list(ast.literal_eval(obj.answers))
    #rk_true_answers = list(ast.literal_eval(obj.question_set.all()))


    context = {'rk': obj, 'questions_answers': list(zip(rk_questions, rk_answers, rk_true_answers))}

    return render(request, "rk_result.html", context=context)


def RKResultsList(request, rk_id):
    rks = RKResult.objects.filter(rk=rk_id)

    context = {'rks': rks}

    return render(request, "rk_results_list.html", context=context)



"""class RKResultsListView(ListView):
    model = RKResult
    template_name = "rk_results_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RKResultsListView, self).get_context_data(*args, **kwargs)
        context['rks'] = self.model.objects.filter(pk=rk_id)

        return context

    def get_queryset(self):
        return self.model.objects.order_by('-date')"""
