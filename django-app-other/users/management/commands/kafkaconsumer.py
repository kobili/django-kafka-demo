import signal

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Initializes and starts a long running Kafka consumer to sync user data from an external source"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        signal.signal(signal.SIGINT, self.terminate)
        signal.signal(signal.SIGTERM, self.terminate)

        self.running = True

    def handle(self, *args, **options):
        # TODO: Consume kafka events here
        while self.running:
            print("running...")

    def terminate(self, signum, frame):
        # TODO: Perform shutdown events here; cleanup kafka client; commit kafka consumer offsets
        self.running = False
        print("done!")

