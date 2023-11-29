from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . import models, forms
from django.views import generic
from django.urls import reverse


# не полная информация
# def person_list_view(request):
#     if request.method == "GET":
#         object_list = models.Person.objects.all()
#         return render(request, template_name='person_list.html', context={'object_list': object_list})
class PersonListView(generic.ListView):
    template_name = 'person_list.html'
    model = models.Person

    def get_queryset(self):
        return self.model.objects.all()


# def person_detail_view(request, id):
#     if request.method == 'GET':
#         person_id = get_object_or_404(models.Person, id=id)
#         return render(request, template_name='person_detail.html',
#                       context={'object': person_id})
#
class PersonDetailView(generic.DetailView):
    template_name = 'person_detail.html'

    def get_object(self, **kwargs):
        person_id = self.kwargs.get('id')
        return get_object_or_404(models.Person, id=person_id)

# Создание
class PersonCreateView(generic.CreateView):
    template_name = 'person_create.html'
    model = models.Person
    form_class = forms.PersonForm
    success_url = "/person_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PersonCreateView, self).form_valid(form=form)


# def person_create_view(request):
    #     method = request.method
#     if method == "POST":
#         form = forms.PersonForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('person_list'))
#             # return HttpResponse("Успешно добавлен в Базу Данных")
#     else:
#         form = forms.PersonForm()
#     return render(request, "person_create.html", {'form': form})

#####Удаление
class PhoneDeleteView(generic.DeleteView):
    template_name = "confirm_delete.html"
    success_url = "/person_list/"

    def get_object(self, **kwargs):
        person_id = self.kwargs.get("id")
        return get_object_or_404(models.Person, id=person_id)

# def person_delete_view(request, id):
#     person_id = get_object_or_404(models.Person, id=id)
#     person_id.delete()
#     return redirect(reverse('person_list'))

# Редактирование
class PersonUpdateView(generic.UpdateView):
    template_name = "person_update.html"
    form_class = forms.PersonForm
    success_url = "/person_list/"

    def get_object(self, **kwargs):
        person_id = self.kwargs.get("id")
        return get_object_or_404(models.Person, id=person_id)

    def form_valid(self, form):
        return super(PersonUpdateView, self).form_valid(form=form)


# def person_update_view(request, id):
#     person_id = get_object_or_404(models.Person, id=id)
#     if request.method == 'POST':
#         form = forms.PersonForm(instance=person_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('Данные успешно обновлены')
#             return redirect(reverse("person_list"))
#     else:
#         form = forms.PersonForm(instance=person_id)
#
#     context = {
#         'form': form,
#         'object': person_id
#     }
#     return render(request, 'person_update.html', context)

class SearchView(generic.ListView):
    template_name = "person_list.html"
    context_object_name = "person"
    paginate_by = 5

    def get_queryset(self):
        return models.Person.objects.filter(
            name__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context