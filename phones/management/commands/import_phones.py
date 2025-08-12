import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
from datetime import datetime

class Command(BaseCommand):
    help = 'Импорт телефонов из CSV'

    def handle(self, *args, **kwargs):
        with open('phones.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    price=float(row['price']) if row['price'] else None,
                    image=row['image'],
                    release_date=datetime.strptime(row['release_date'], '%Y-%m-%d').date() if row['release_date'] else None,
                    lte_exists=row['lte_exists'].lower() == 'true',
                    slug=slugify(row['name'])
                )
                phone.save()
                self.stdout.write(f'Импортирован телефон: {row["name"]}')
        
        self.stdout.write(self.style.SUCCESS('Импорт завершен успешно!'))