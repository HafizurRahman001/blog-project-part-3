from django.shortcuts import render,redirect
from categories_app.forms import CategoryForm

# Create your views here.
def add_categories(request):
    if request.method == 'POST':
        add_category_form = CategoryForm(request.POST)
        if add_category_form.is_valid():
            add_category_form.save()
            return redirect('add_categories')
    else:
        add_category_form = CategoryForm()
    return render(request,'add_category.html', {'form':add_category_form})