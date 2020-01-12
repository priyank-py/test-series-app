# Generated by Django 3.0.2 on 2020-01-11 19:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('question', models.FileField(upload_to=None, verbose_name='Upload Question')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('max_marks', models.IntegerField(blank=True, null=True, verbose_name='Maximum Marks')),
                ('duration', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Duration (in minutes)')),
                ('rule', models.TextField(blank=True, null=True, verbose_name='Rules')),
            ],
            options={
                'verbose_name': 'QuestionImage',
                'verbose_name_plural': 'QuestionImages',
            },
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('created_on', models.DateField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('max_marks', models.IntegerField(blank=True, null=True, verbose_name='Maximum Marks')),
                ('duration', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='Duration (in minutes)')),
                ('rule', models.TextField(blank=True, null=True, verbose_name='Rules')),
            ],
            options={
                'verbose_name': 'QuestionPaper',
                'verbose_name_plural': 'QuestionPapers',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
                ('paper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.QuestionPaper', verbose_name='Question Paper')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=50, verbose_name='Option')),
                ('correct', models.BooleanField(choices=[(True, 'correct'), (False, 'incorrect')], verbose_name='Is correct')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
    ]
