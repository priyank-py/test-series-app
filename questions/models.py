from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class QuestionPaper(models.Model):

    subject = models.CharField(_("Subject"), max_length=50)
    created_on = models.DateField(_("Created on"), auto_now=False, auto_now_add=False, default=timezone.now)
    max_marks = models.IntegerField(_("Maximum Marks"), blank=True, null=True)
    duration = models.DecimalField(_("Duration (in minutes)"), max_digits=3, decimal_places=2, blank=True, null=True)
    rule = models.TextField(_("Rules"), blank=True, null=True)

    class Meta:
        verbose_name = _("QuestionPaper")
        verbose_name_plural = _("QuestionPapers")

    def __str__(self):
        return self.subject

    # def get_absolute_url(self):
    #     return reverse("QuestionPaper_detail", kwargs={"pk": self.pk})


class Question(models.Model):
    paper = models.ForeignKey(QuestionPaper, verbose_name=_("Question Paper"), related_name="questions",on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField(_("Question"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.paper.subject

    # def get_absolute_url(self):
    #     return reverse("Question_detail", kwargs={"pk": self.pk})

class Option(models.Model):
    CHOICES = (
        (True, 'correct'),
        (False, 'incorrect')
    )
    
    question = models.ForeignKey(Question, verbose_name=_("Question"), related_name="options", on_delete=models.CASCADE, blank=True, null=True)
    option = models.CharField(_("Option"), max_length=50)
    correct = models.BooleanField(_("Is correct"), choices=CHOICES)
    

    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")

    def __str__(self):
        return self.option

    # def get_absolute_url(self):
    #     return reverse("Option_detail", kwargs={"pk": self.pk})



class QuestionImage(models.Model):
    subject = models.CharField(_("Subject"), max_length=50)
    question = models.FileField(_("Upload Question"), upload_to=None, max_length=100)
    created_on = models.DateField(_("Created on"), auto_now=False, auto_now_add=False, default=timezone.now)
    max_marks = models.IntegerField(_("Maximum Marks"), blank=True, null=True)
    duration = models.DecimalField(_("Duration (in minutes)"), max_digits=3, decimal_places=2, blank=True, null=True)
    rule = models.TextField(_("Rules"), blank=True, null=True)
    

    class Meta:
        verbose_name = _("QuestionImage")
        verbose_name_plural = _("QuestionImages")

    def __str__(self):
        return self.subject

    # def get_absolute_url(self):
    #     return reverse("QuestionImage_detail", kwargs={"pk": self.pk})
