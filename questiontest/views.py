from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.forms import modelformset_factory

# Create your views here.
from .models import Question, RK

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


    def form_valid(self, form):
        #doc = self.request.body.decode('utf-8').split("&")[-1].split('=')[-1]
        obj = form.save(commit=False)
        obj.author = self.request.user
        #obj.document = self.request.FILES
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
