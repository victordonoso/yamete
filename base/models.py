from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

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
        return self.name

    def generate_org_code(self):
        org_code = self.org_name.capitalize()[0:3] + self.org_owner.first_name.capitalize()[0:2] + self.org_owner.last_name.capitalize()[0:2] + self.org_created_date.strftime("%y%m%d")
        return org_code

    def get_absolute_url(self):
        return reverse("Org_detail", kwargs={"pk": self.pk})

class OrgMembers(models.Model):
    
        parent_org = models.ForeignKey(Organization, related_name='parent_org', on_delete=models.CASCADE)
        org_member = models.ForeignKey(User, related_name='org_members', on_delete=models.CASCADE)
        member_join_date = models.DateTimeField(auto_now_add=True)
    
        class Meta:
            verbose_name = _("Org Members")
            verbose_name_plural = _("Org Members")
    
        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return reverse("OrgMembers_detail", kwargs={"pk": self.pk})
