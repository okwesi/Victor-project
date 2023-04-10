from django.shortcuts import render, redirect
from .models import Person
from django import forms
import csv
from django.http import HttpResponse

class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=(('male', 'Male'), ('female', 'Female')),
        initial='male',  # set 'male' as the default value
        widget=forms.Select(attrs={'class': 'form-control'})  # add class for styling
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Person
        fields = ('name', 'location', 'gender', 'age')


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = PersonForm()
    return render(request, 'create_person.html', {'form': form})

def person_list(request):
    persons = Person.objects.order_by('gender')  # Sort by gender
    return render(request, 'person_list.html', {'persons': persons})


def person_list_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="person_list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Location', 'Gender', 'Age'])
    persons = Person.objects.all()
    for person in persons:
        writer.writerow([person.name, person.location, person.gender, person.age])

    return response

def success_page(request):
    return render(request, 'success.html')


def person_delete(request, pk):
    """View to delete a person object"""
    if request.method == 'POST':
        person = Person.objects.get(id=pk)
        person.delete()
    return redirect('/list')