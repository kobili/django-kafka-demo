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
        while self.running:
            # TODO: Consume kafka events here
            print("running...")
        
        # TODO: Perform shutdown events here; cleanup kafka client; commit kafka consumer offsets
        print("done!")

    def terminate(self, signum, frame):
        print(f"received signal: {signum}")
        self.running = False

