# Generated by Django 4.0.2 on 2022-03-11 11:42

import api.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('appointmentPlace', models.CharField(choices=[('p1', 'Place 1'), ('p2', 'Place 2')], default='p1', max_length=2)),
                ('appointmentDay', models.DateTimeField()),
                ('personOne', models.CharField(choices=[('p1', 'Person 1'), ('p2', 'Person 2')], default='p1', max_length=2)),
                ('personTwo', models.CharField(choices=[('p1', 'Person 1'), ('p2', 'Person 2')], default='p1', max_length=2)),
                ('volunteer', models.CharField(blank=True, default='', max_length=100)),
                ('durationTime', models.DurationField()),
                ('type', models.CharField(choices=[('t1', 'Type 1'), ('t2', 'Type 2')], default='t1', max_length=2)),
                ('report', models.TextField()),
            ],
            options={
                'ordering': ['appointmentDay'],
            },
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('surname', models.CharField(blank=True, default='', max_length=100)),
                ('yearsOld', models.IntegerField()),
                ('education', models.CharField(choices=[('e0', '--'), ('e1', 'Elementari'), ('e2', 'Medie'), ('e3', 'Superiori'), ('e4', 'Università')], default='e0', max_length=7)),
                ('job', models.CharField(choices=[('j0', '--'), ('j1', 'Occupato stabile'), ('j2', 'Occupato saltuario'), ('j3', 'Disoccupato'), ('j4', 'Inoccupato'), ('j5', 'Pensionato'), ('j6', 'Altra condizione')], default='j0', max_length=7)),
                ('relationship', models.CharField(choices=[('r0', '--'), ('r1', 'Coniuge'), ('r2', 'Ex coniuge'), ('r3', 'Fidanzato'), ('r4', 'Ex-fidanzato'), ('r5', 'Vicino'), ('r6', 'Figura paterna'), ('r7', 'Amico'), ('r8', 'Conoscente'), ('r9', 'Sconosciuto')], default='r0', max_length=7)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='path',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('status', models.CharField(choices=[('closed', 'Chiuso'), ('ongoing', 'In corso')], default='ongoing', max_length=7)),
                ('authors', djongo.models.fields.ArrayField(model_container=api.models.author)),
                ('appointments', djongo.models.fields.ArrayField(model_container=api.models.appointment)),
            ],
            options={
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='woman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('surname', models.CharField(blank=True, default='', max_length=100)),
                ('birthdate', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('citizenship', models.CharField(choices=[('IT', 'Italiana'), ('ST', 'Straniera')], default='IT', max_length=2)),
                ('path', djongo.models.fields.EmbeddedField(model_container=api.models.path)),
                ('report', models.TextField()),
            ],
            options={
                'ordering': ['birthdate'],
            },
        ),
    ]
