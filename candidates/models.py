from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Candidate(models.Model):

    PROFESSIONS = (
        ('student', 'Student'),
        ('private', 'Private Sector'),
        ('government', 'Government Sector'),
        ('freelance', 'Freelance'),
        ('unemployed', 'Unemployed')
    )

    user = models.OneToOneField(User, verbose_name=_("candidate_user"), on_delete=models.CASCADE)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False, blank=True, null=True)
    status = models.CharField(_("Profession Status"), max_length=50, choices=PROFESSIONS, blank=True, null=True)
    highest_qualification = models.CharField(_("Highest Qualification"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidates")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Candidate_detail", kwargs={"pk": self.pk})

