from django.shortcuts import render
from .forms import SupporterForm

def supporter_form(request):
    if request.method == 'POST':
        form = SupporterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  # Extract the name from the form
            form.save()
            # Redirect to a success page or do something else
            return render(request, 'success.html', {'name': name})
    else:
        form = SupporterForm()
    return render(request, 'user_form.html', {'form': form})
