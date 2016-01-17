import time
from bynge import app


class AudioFileProcessor:

    def __init__(self, uuid):
        self.uuid = uuid
        app.logger.info('processing task started')

    def process(self):
        app.logger.info(self.uuid)
        time.sleep(10)

    def store(self):
        print(self.uuid)

    def normalize(self):
        print(self.uuid)

    def recode(self):
        print(self.uuid)

    def read_tag(self):
        print(self.uuid)

    def write_tag(self):
        print(self.uuid)

    def get_data_hash(self):
        print(self.uuid)

    def is_duplicate(self):
        print(self.uuid)

    def __del__(self):
        app.logger.info('processing task finished')