from base.models import Organization
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth.models import User


class Events(models.Model):

    event_name = models.CharField(verbose_name=_("Event Name"),max_length=150)
    event_creator = models.ForeignKey(User, verbose_name=_("Creator"), on_delete=models.CASCADE)
    event_created_date = models.DateTimeField(verbose_name=_("Created Date"),auto_now_add=True)
    event_org = models.ForeignKey(Organization, related_name='events', on_delete=models.CASCADE)
    event_description = models.TextField(verbose_name=_("Description"),blank=True, null=True)
    event_slug = models.SlugField(verbose_name=_("Slug"),max_length=150, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Events")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("Events", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.event_slug = self.event_org.org_name.capitalize()[0:3]+'-'+self.event_name.lower().replace(" ", "-")[0:30]
        super(Events, self).save(*args, **kwargs)

class EventStatuses(models.Model):
    
    event_status = models.CharField(verbose_name=_("Event Status"),max_length=150)
    event_status_description = models.TextField(verbose_name=_("Event Status Description"),blank=True, null=True)

    class Meta:
        verbose_name = _("Event Statuses")
        verbose_name_plural = _("Event Statuses")

    def __str__(self):
        return self.event_status

    def get_absolute_url(self):
        return reverse("EventStatuses", kwargs={"pk": self.pk})

class EventTypes(models.Model):

    event_type_name = models.CharField(verbose_name=_("Event Type Name"), max_length=150)
    event_type_description = models.TextField(verbose_name=_("Event Type Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Event Type")
        verbose_name_plural = _("Event Types")

    def __str__(self):
        return self.event_type_name

    def get_absolute_url(self):
        return reverse("EventTypes", kwargs={"pk": self.pk})

class EventRoles(models.Model):

    event_role_name = models.CharField(verbose_name=_("Event Role Name"), max_length=150)
    event_role_description = models.TextField(verbose_name=_("Event Role Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Event Role")
        verbose_name_plural = _("Event Roles")

    def __str__(self):
        return self.event_role_name

    def get_absolute_url(self):
        return reverse("EventRoles", kwargs={"pk": self.pk})

class EventParticipants(models.Model):

    parent_event = models.ForeignKey(Events, verbose_name=_("Event"), related_name='event_participants', on_delete=models.CASCADE)
    participant = models.ForeignKey(User, verbose_name=_("Participant"), on_delete=models.CASCADE) # Add a filter to limit choices to only those that are members of the parent org
    participant_role = models.ForeignKey(EventRoles, verbose_name=_("Participant Role"), related_name='event_participants', on_delete=models.CASCADE)
    participant_is_active = models.BooleanField(verbose_name=_("Participant Is Active"), default=True)

    class Meta:
        verbose_name = _("Event Participant")
        verbose_name_plural = _("Event Participants")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EventParticipants_detail", kwargs={"pk": self.pk})

class EventDivisions(models.Model):

    parent_event = models.ForeignKey(Events, verbose_name=_("Event"), related_name='event_divisions', on_delete=models.CASCADE)
    division_name = models.CharField(verbose_name=_("Division Name"), max_length=150)
    division_description = models.TextField(verbose_name=_("Division Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Event Division")
        verbose_name_plural = _("Event Divisions")

    def __str__(self):
        return self.parent_event.event_name + ' - ' + self.division_name

    def get_absolute_url(self):
        return reverse("EventDivisions_detail", kwargs={"pk": self.pk})



class EventDetails(models.Model):

    parent_event = models.ForeignKey(Events, verbose_name=_("Event"), related_name='event_details', on_delete=models.CASCADE)
    event_manager = models.ForeignKey(User, verbose_name=_("Event Manager"), on_delete=models.CASCADE) # Add a filter to limit choices to only those that are members of the parent org
    event_start_date = models.DateField(verbose_name=_("Event Date"))
    event_finish_date = models.DateField(verbose_name=_("Event Finish Date"))
    event_real_start_date = models.DateField(verbose_name=_("Event Real Start Date"), blank=True, null=True)
    event_real_finish_date = models.DateField(verbose_name=_("Event Real Finish Date"), blank=True, null=True)
    event_location = models.CharField(verbose_name=_("Event Location"), max_length=150)
    event_description = models.TextField(verbose_name=_("Event Description"), blank=True, null=True)
    event_type = models.ForeignKey(EventTypes, verbose_name=_("Event Type"), related_name='event_details', on_delete=models.CASCADE)
    event_status = models.ForeignKey(EventStatuses, verbose_name=_("Event Status"), related_name='event_details', on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Event Details")
        verbose_name_plural = _("Event Details")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EventDetails_detail", kwargs={"pk": self.pk})
