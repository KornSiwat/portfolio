from django.shortcuts import render
from portfolioApp.forms import ContactMessageForm


def indexView(request):
    context = {'form': ContactMessageForm}

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'portfolioApp/index.html', context)
