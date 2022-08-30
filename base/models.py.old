import datetime
import os
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
def get_image_path(instance, filename):
    return 'images/{0}/{1}_{2}'.format(instance.id, filename, datetime.date.today().strftime("%y%m%d"))


class Organization(models.Model):

    org_name = models.CharField(verbose_name =_('Name'), max_length=150)
    org_description = models.TextField(blank=True, null=True)
    org_created_date = models.DateTimeField(auto_now_add=True)
    org_updated_date = models.DateTimeField(auto_now=True)
    org_owner = models.ForeignKey(User, related_name='organizations', on_delete=models.CASCADE)
    org_code = models.CharField(max_length=150)

    class Meta:
        verbose_name = _("org")
        verbose_name_plural = _("Orgs")

    def __str__(self):
        return self.org_name

    def generate_org_code(self):
        org_code = self.org_name.capitalize()[0:3] + self.org_owner.first_name.capitalize()[0:2] + self.org_owner.last_name.capitalize()[0:2] + self.org_created_date.strftime("%y%m%d")
        return org_code

    def get_absolute_url(self):
        return reverse("Org_detail", kwargs={"pk": self.pk})

class OrgMembers(models.Model):
    
    parent_org = models.ForeignKey(Organization, related_name='parent_org', on_delete=models.CASCADE)
    org_member = models.ForeignKey(User, related_name='org_members', on_delete=models.CASCADE)
    member_profile_pic = models.FileField(upload_to=get_image_path, blank=True)
    member_join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Org Members")
        verbose_name_plural = _("Org Members")

    def __str__(self):
        return self.parent_org.org_name + " - " + self.org_member.username

    def get_absolute_url(self):
        return reverse("OrgMembers_detail", kwargs={"pk": self.pk})


class TeamsInformation(models.Model):
    
    team_name = models.CharField(verbose_name =_('Name'), max_length=150)
    team_description = models.TextField(blank=True, null=True)
    team_created_date = models.DateTimeField(auto_now_add=True)
    team_updated_date = models.DateTimeField(auto_now=True)
    team_owner = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)
    team_code = models.CharField(max_length=150)
    team_logo = models.ImageField(upload_to='team_logo', blank=True, null=True)
    team_org = models.ForeignKey(Organization, related_name='teams', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.team_name

    def generate_team_code(self):
        team_code = self.team_name.capitalize()[0:3] + self.team_owner.first_name.capitalize()[0:2] + self.team_owner.last_name.capitalize()[0:2] + self.team_created_date.strftime("%y%m%d")
        return team_code
    
    def save(self, *args, **kwargs):
        self.team_code = self.generate_team_code()
        super(TeamsInformation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})

class TeamRoles(models.Model):

    role_name = models.CharField(verbose_name =_('Name'), max_length=150)
    role_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Team Roles")
        verbose_name_plural = _("Team Roles")

    def __str__(self):
        return self.role_name

    def get_absolute_url(self):
        return reverse("TeamRoles_detail", kwargs={"pk": self.pk})

class TeamMembers(models.Model):
        
    parent_team = models.ForeignKey(TeamsInformation, related_name='parent_team', on_delete=models.CASCADE)
    team_member = models.ForeignKey(User, related_name='team_members', on_delete=models.CASCADE)
    member_bio = models.TextField(blank=True, null=True)
    member_profile_pic = models.ImageField(upload_to='team_member_profile_pic', blank=True, null=True)
    member_role = models.ForeignKey(TeamRoles, related_name='team_member_roles', on_delete=models.SET_NULL, null=True)
    member_join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Team Members")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("TeamMembers_detail", kwargs={"pk": self.pk})


