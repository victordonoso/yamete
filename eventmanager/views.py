from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from models import Events, Matches
# Create your views here.

@login_required
class EventCreateView(CreateView):
    model = Events
    template_name = "event_manager/event_create.html"

    fields = [
        "event_title",
        "event_description",
        "event_date",
        "event_creator",
    ]

    def form_valid(self, form):
        form.instance.event_creator = self.request.user
        return super().form_valid(form)

@login_required
class EventListView(ListView):
    model = Events
    template_name = "event_manager/event_list.html"

    def get_queryset(self):
        return Events.objects.filter(event_creator=self.request.user)

@login_required
class EventDetailView(DetailView):
    model = Events
    template_name = "event_manager/event_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = Matches.objects.filter(parent_event=self.object)
        context["matches"] = matches
        return context
    

@login_required
class EventUpdateView(UpdateView):
    model = Events
    template_name = "event_manager/event_update.html"

    fields = [
        "event_title",
        "event_description",
        "event_date",
    ]

@login_required
class EventDeleteView(DeleteView):
    model = Events
    template_name = "event_manager/event_delete.html"

    def get_success_url(self):
        return reverse("event_list")

@login_required
class MatchCreateView(CreateView):
    model = Matches
    template_name = "event_manager/match_create.html"

    fields = [
        "parent_event",
        "match_description",
        "match_date",
        "match_team_0",
        "match_team_1",
        "match_team_0_score",
        "match_team_1_score",
    ]

    def _init_(self, *args, **kwargs):
        super(MatchCreateView, self)._init_(*args, **kwargs)
        try:
            self.fields["parent_event"].queryset = Events.objects.filter(event_creator=self.request.user)
        except:
            pass
    
    def form_valid(self, form):
        form.instance.match_creator = self.request.user
        return super().form_valid(form)

@login_required
class MatchListView(ListView):
    model = Matches
    template_name = "event_manager/match_list.html"

    def get_queryset(self):
        try:
            matches = Matches.objects.filter(parent_event__event_creator=self.request.user)
        except:
            matches = []
        return matches

@login_required
class MatchDetailView(DetailView):
    model = Matches
    template_name = "event_manager/match_detail.html"


@login_required
class MatchUpdateView(UpdateView):
    model = Matches
    template_name = "event_manager/match_update.html"

    fields = [
        "parent_event",
        "match_description",
        "match_date",
        "match_team_0",
        "match_team_1",
        "match_team_0_score",
        "match_team_1_score",
    ]

    def _init_(self, *args, **kwargs):
        super(MatchUpdateView, self)._init_(*args, **kwargs)
        try:
            self.fields["parent_event"].queryset = Events.objects.filter(event_creator=self.request.user)
        except:
            pass

@login_required
class MatchDeleteView(DeleteView):
    model = Matches
    template_name = "event_manager/match_delete.html"

    def get_success_url(self):
        return reverse("match_list")

def match_overlay(request, slug):
    match = get_object_or_404(Matches, slug=slug)
    context = {
        "match": match,
    }
    return render(request, "event_manager/match_overlay.html", context)

