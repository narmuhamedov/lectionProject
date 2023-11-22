from django.shortcuts import get_object_or_404
from . import models, forms
from django.views import generic


# не полная информация
class PersonListView(generic.ListView):
    template_name = 'person_list.html'
    queryset = models.Person.objects.all()

    def get_queryset(self):
        return self.queryset

class PersonDetailView(generic.DetailView):
    template_name = 'person_detail.html'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Person, id=person_id)

#Создание
class PersonCreateView(generic.CreateView):
    template_name = 'person_create.html'
    queryset = models.Person.objects.all()
    form_class = forms.PersonForm
    success_url = "/person_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PersonCreateView, self).form_valid(form=form)