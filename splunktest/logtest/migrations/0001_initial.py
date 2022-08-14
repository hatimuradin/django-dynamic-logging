# Generated by Django 4.1 on 2022-08-14 05:18

from django.db import migrations, models
import django_enum_choices.choice_builders
import django_enum_choices.fields
import logtest.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LoggerSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("enable", models.BooleanField(default=True, verbose_name="Enable")),
                (
                    "handler",
                    django_enum_choices.fields.EnumChoiceField(
                        choice_builder=django_enum_choices.choice_builders.value_value,
                        choices=[("CONSOLE", "CONSOLE"), ("SPLUNK", "SPLUNK")],
                        default=logtest.models.HandlerTypes["CONSOLE"],
                        enum_class=logtest.models.HandlerTypes,
                        max_length=7,
                        verbose_name="TradeType",
                    ),
                ),
            ],
        ),
    ]