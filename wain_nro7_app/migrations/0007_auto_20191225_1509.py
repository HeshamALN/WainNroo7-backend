# Generated by Django 3.0 on 2019-12-25 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wain_nro7_app', '0006_riddle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('right', models.BooleanField(default=False)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='trivia',
        ),
        migrations.AddField(
            model_name='trivia',
            name='lock',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='questions',
            name='trivia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='wain_nro7_app.Trivia'),
        ),
        migrations.AddField(
            model_name='answers',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='wain_nro7_app.Questions'),
        ),
    ]
