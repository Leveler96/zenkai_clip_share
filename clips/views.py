from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Clip
from .forms import ClipCreateForm


# Create your views here.
def clip_list(request):
    clips = Clip.objects.all().order_by('date_uploaded')
    context = {
        'clips': clips
    }
    return render(request, 'clips/clip_list.html', context)

# class based view for uploading clips
class ClipCreateView(LoginRequiredMixin, CreateView):
    model = Clip
    form_class = ClipCreateForm
    template_name = 'clips/clip_create.html'
    success_url = reverse_lazy('clip-list')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)