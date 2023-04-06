"""
Populates required initial data.
"""
from django.core.management import call_command
from django.db import transaction


def run():
    with transaction.atomic():
        populate_data()


def populate_data():
    call_command("loaddata", "core/initial_data/groups.json", verbosity=0)
    call_command("loaddata", "core/initial_data/initial.json", verbosity=0)


if __name__ == "main":
    run()
