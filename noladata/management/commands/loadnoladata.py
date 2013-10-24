from importlib import import_module
import traceback

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = 'dataset_name'
    help = 'Loads NOLA data (addresses, buildings, parcels, ...)'

    datasets = {
        'addresses': 'noladata.addresses',
        'buildings': 'noladata.buildings',
        'nora': 'noladata.nora',
        'parcels': 'noladata.parcels',
    }

    def handle(self, dataset_name, *args, **options):
        try:
            load_module = import_module('%s.load' % self.datasets[dataset_name])
            load_module.load()
        except KeyError:
            traceback.print_exc()
            raise CommandError('Could not find dataset %s' % dataset_name)
        except Exception:
            traceback.print_exc()
            raise CommandError('There was a problem loading data')
