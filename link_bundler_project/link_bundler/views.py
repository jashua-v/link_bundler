from django.shortcuts import render, redirect, get_object_or_404
from .models import Bundle, Link
from .forms import BundleForm, LinkForm, PasswordForm

def create_bundle(request):
    if request.method == 'POST':
        bundle_form = BundleForm(request.POST)
        link_form = LinkForm(request.POST)

        if bundle_form.is_valid() and link_form.is_valid():
            bundle = bundle_form.save()

            link = link_form.save(commit=False)
            link.bundle = bundle
            link.save()

            return redirect('view_bundle', bundle_id=bundle.id)

    else:
        bundle_form = BundleForm()
        link_form = LinkForm()

    return render(request, 'create_bundle.html', {'bundle_form': bundle_form, 'link_form': link_form})

def view_bundle(request, bundle_id):
    bundle = get_object_or_404(Bundle, id=bundle_id)

    if bundle.password:
        if request.method == 'POST':
            password_form = PasswordForm(request.POST)
            if password_form.is_valid():
                entered_password = password_form.cleaned_data.get('password')
                if entered_password == bundle.password:
                    links = Link.objects.filter(bundle=bundle)
                else:
                    error_message = 'Incorrect password'
        else:
            password_form = PasswordForm()
            links = []
    else:
        links = Link.objects.filter(bundle=bundle)
        password_form = None

    return render(request, 'view_bundle.html', {'bundle': bundle, 'links': links, 'password_form': password_form})
