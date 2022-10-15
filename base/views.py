from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.




class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields ='__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
        template_name = 'logout.html'

        def get_success_url(self):
            return reverse_lazy('login')


class RegisterPage(FormView):
    form_class = UserCreationForm
    template_name = 'register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

        def get(self, *args, **kwargs):
                if self.request.user.is_authenticated:
                    return redirect('login')
                return super(RegisterPage,self).get(*args, **kwargs)


# DISPLAY CONTACT QUERY
class HomeView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #SEARCH QUERY
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['contacts'] = context ['contacts'].filter(full_name__startswith=search_input)
            context['search_input'] = search_input

        return context


#DISPLAY CONTACT DETAIL QUERY
class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'profile.html'


#CREATE CONTACT QUERY
class CreateContact(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'add_contact.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateContact, self).form_valid(form)
        form.save()


#EDIT CONTACT QUERY
class UpdateContact(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


#DELETE CONTACT QUERY
class DeleteContact(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = reverse_lazy('home')