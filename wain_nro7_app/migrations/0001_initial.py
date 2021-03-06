# Generated by Django 3.0 on 2019-12-27 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('xcoordinate', models.FloatField()),
                ('ycoordinate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lock', models.BooleanField(default=False)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trivia', to='wain_nro7_app.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='riddle', to='wain_nro7_app.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('trivia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='wain_nro7_app.Trivia')),
            ],
        ),
        migrations.CreateModel(
            name='Difference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('diffs', models.PositiveIntegerField()),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='difference', to='wain_nro7_app.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xcoordinate', models.FloatField()),
                ('ycoordinate', models.FloatField()),
                ('difference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='wain_nro7_app.Difference')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('right', models.BooleanField(default=False)),
                ('score', models.FloatField()),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='wain_nro7_app.Question')),
            ],
        ),
    ]
