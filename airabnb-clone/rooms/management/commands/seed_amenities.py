from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that i love you?"
    #     )

    def handle(self, *args, **options):
        amenities = [
            "TV",
            "Oven",
            "Shower",
            "Toilet",
            "WIfi",
            "Sofa",
            "bed",
            "Restaurant",
            "Shopping Mall",
            "Bathtub",
            "Book",
            "Cup",
            "Orange juice",
            "Wine",
            "Beer",
            "Air conditioner",
            "Water",
            "Brush",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
