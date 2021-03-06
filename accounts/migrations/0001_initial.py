# Generated by Django 3.0.1 on 2020-08-29 19:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cid', models.IntegerField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='Example2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InfoSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchedtitle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250, unique=True)),
                ('date', models.DateField(default=datetime.date(2020, 8, 30))),
                ('minsal', models.IntegerField(blank=True, default=0)),
                ('maxsal', models.IntegerField(blank=True, default=0)),
                ('jobtitle', models.TextField(max_length=100)),
                ('companyname', models.CharField(max_length=500)),
                ('minexp', models.IntegerField(default=0, max_length=10)),
                ('maxexp', models.IntegerField(default=0, max_length=10)),
                ('location', models.CharField(blank=True, max_length=300)),
                ('jobdescription', models.TextField(max_length=500)),
                ('originaljoburl', models.URLField(blank=True)),
                ('jobportal', models.CharField(blank=True, max_length=20)),
                ('skills', models.CharField(blank=True, max_length=1000)),
                ('jobtype', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phoneno', models.CharField(blank=True, max_length=30)),
                ('linkedinprofileurl', models.CharField(blank=True, max_length=30)),
                ('usertitle', models.CharField(max_length=30)),
                ('skills', models.TextField(max_length=100)),
                ('extrainfo', models.TextField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=42)),
                ('projecttitle1', models.CharField(blank=True, max_length=30)),
                ('projectdescription1', models.TextField(blank=True, max_length=200)),
                ('projectyoc1', models.CharField(blank=True, max_length=30)),
                ('projecttitle2', models.CharField(blank=True, max_length=30)),
                ('projectdescription2', models.TextField(blank=True, max_length=200)),
                ('projectyoc2', models.CharField(blank=True, max_length=30)),
                ('projecttitle3', models.CharField(blank=True, max_length=30)),
                ('projectdescription3', models.TextField(blank=True, max_length=200)),
                ('projectyoc3', models.CharField(blank=True, max_length=30)),
                ('companyname1', models.CharField(blank=True, max_length=30)),
                ('designation1', models.CharField(blank=True, max_length=30)),
                ('companyyow1', models.CharField(blank=True, max_length=30)),
                ('companyname2', models.CharField(blank=True, max_length=30)),
                ('designation2', models.CharField(blank=True, max_length=30)),
                ('companyyow2', models.CharField(blank=True, max_length=30)),
                ('companyname3', models.CharField(blank=True, max_length=30)),
                ('designation3', models.CharField(blank=True, max_length=30)),
                ('companyyow3', models.CharField(blank=True, max_length=30)),
                ('institute1', models.CharField(blank=True, max_length=30)),
                ('degree1', models.CharField(blank=True, max_length=30)),
                ('stream1', models.CharField(blank=True, max_length=30)),
                ('studyforyears1', models.CharField(blank=True, max_length=30)),
                ('grade1', models.CharField(blank=True, max_length=30)),
                ('institute2', models.CharField(blank=True, max_length=30)),
                ('degree2', models.CharField(blank=True, max_length=30)),
                ('stream2', models.CharField(blank=True, max_length=30)),
                ('studyforyears2', models.CharField(blank=True, max_length=30)),
                ('grade2', models.CharField(blank=True, max_length=30)),
                ('institute3', models.CharField(blank=True, max_length=30)),
                ('degree3', models.CharField(blank=True, max_length=30)),
                ('stream3', models.CharField(blank=True, max_length=30)),
                ('studyforyears3', models.CharField(blank=True, max_length=30)),
                ('grade3', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobtitle', models.CharField(blank=True, max_length=100)),
                ('Sortby', models.CharField(choices=[('DATE', 'DATE'), ('SALARY', 'SALARY'), ('EXPERIENCE', 'EXPERIENCE')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sid', models.IntegerField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchedtitle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('savedjobs', models.TextField(max_length=50)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('skills', models.TextField(blank=True, default=' ', max_length=200)),
                ('additionalinfo', models.TextField(blank=True, default=' ', max_length=100)),
                ('city', models.CharField(default=' ', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
