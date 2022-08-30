from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse

class Events(models.Model):
    event_title = models.CharField(_("Title"), max_length=50)
    event_description = models.TextField(_("Description"), null=True, blank=True)
    event_date = models.DateField(_("Date"))
    slug = models.SlugField(_("Slug"), max_length=50, unique=True, blank=True)
    event_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return str(self.pk) + " - " + self.event_title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.pk) + "-" + self.event_title)
        super(Events, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})
    
class Matches(models.Model):

    parent_event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="matches")
    match_description = models.TextField(_("Description"), null=True, blank=True)
    match_date = models.DateField(_("Date"))
    match_team_0 = models.CharField(_("Team 0"), max_length=50)
    match_team_1 = models.CharField(_("Team 1"), max_length=50)
    match_team_0_score = models.IntegerField(_("Team 0 Score"), null=True, blank=True)
    match_team_1_score = models.IntegerField(_("Team 1 Score"), null=True, blank=True)
    slug = models.SlugField(_("Slug"), max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = _("Matches")
        verbose_name_plural = _("Matchess")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            pre_slug = f"{self.id} {self.match_team_0} vs {self.match_team_1}"
            self.slug = slugify(pre_slug)
        super(Matches, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id) + " - " + self.match_team_0 + " vs " + self.match_team_1

    def get_absolute_url(self):
        return reverse("match_detail", kwargs={"slug": self.slug})

