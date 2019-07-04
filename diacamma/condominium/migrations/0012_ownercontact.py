# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-11 18:51
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.translation import ugettext_lazy as _
import django.db.models.deletion
from django.conf import settings

from lucterios.framework.tools import set_locale_lang
from lucterios.CORE.models import PrintModel


def initial_values(*_args):
    from diacamma.condominium.models import OwnerLink
    set_locale_lang(settings.LANGUAGE_CODE)
    link1, created = OwnerLink.objects.get_or_create(id=1)
    if created:
        link1.name = _('lodger')
        link1.save()
    link2, created = OwnerLink.objects.get_or_create(id=2)
    if created:
        link2.name = _('rental agency')
        link2.save()
    link3, created = OwnerLink.objects.get_or_create(id=3)
    if created:
        link3.name = _('emergency')
        link3.save()
    link4, created = OwnerLink.objects.get_or_create(id=4)
    if created:
        link4.name = _('security agency')
        link4.save()


def printer_model(*_args):
    set_locale_lang(settings.LANGUAGE_CODE)
    PrintModel().load_model("diacamma.condominium", "Owner_0002", is_default=True)


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_length_field'),
        ('payoff', '0006_depositslip_status'),
        ('condominium', '0011_sizeofpartition'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.AbstractContact', verbose_name='contact')),
            ],
            options={
                'verbose_name_plural': 'owner contacts',
                'verbose_name': 'owner contact',
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='OwnerLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'owner links',
                'verbose_name': 'owner link',
                'default_permissions': [],
            },
        ),
        migrations.AddField(
            model_name='ownercontact',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='condominium.OwnerLink', verbose_name='owner link'),
        ),
        migrations.AddField(
            model_name='ownercontact',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominium.Owner', verbose_name='owner'),
        ),
        migrations.CreateModel(
            name='OwnerEntryLineAccount',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('accounting.entrylineaccount',),
        ),
        migrations.RunPython(initial_values),
        migrations.RunPython(printer_model),
    ]
