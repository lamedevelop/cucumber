import random

from app.db.models.client import ClientValidation
from app.db.schema import validation_table
from app.db.services.abstract import AbstractService


class ValidationService(AbstractService):

    code = ''
    pin_len = 6
    pin_ttl = 60  # seconds
    validation_method = 0

    def send_validation(self): pass

    def check_validation(self): pass

    def generate_pin(self):
        for i in range(self.pin_len):
            self.code += str(random.randint(0, 9))

    # def store_pin(self, validator: ClientValidation):
    #     validation_id = await self.execute(
    #         validation_table.insert().values({
    #             'client_id': validator.client_id,
    #             'method': self.validation_method
    #
    #         }).returning(validation_table.c.validation_id)
    #     )
