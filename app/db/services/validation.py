import random

from sqlalchemy import and_

from app.db.models.client import ClientValidation, Client, ClientValidationFull
from app.db.schema import validation_table
from app.db.services.abstract import AbstractService
from app.internal.senders.email import EmailSender
from app.internal.time_manager import TimeManager


class ValidationService(AbstractService):

    pin_len = 4
    pin_ttl = 60000  # seconds
    email_validation = 1
    sms_validation = 2

    async def send_validation(self, client: Client):
        validation = ClientValidation(
            client_id=client.client_id,
            pin=self.generate_pin(),
            method=self.email_validation,
            date=TimeManager.get_ts()
        )

        await self.store_validation(validation)
        sender = EmailSender(client.email)
        sender.send({'subject': 'Validation code', 'content': f'Your validation pin: {validation.pin}'})

    async def check_validation(self, client: Client, client_pin: int):
        validation = await self.get_validation_by_client(client.client_id)
        return True if validation and validation.pin == client_pin else False

    def generate_pin(self):
        code = ''
        for i in range(self.pin_len):
            code += str(random.randint(0, 9))
        return code

    async def store_validation(self, validation: ClientValidation):
        validation_id = await self.execute(
            validation_table.insert().values({
                **validation.dict()
            }).returning(validation_table.c.validation_id)
        )
        return validation_id[0] if validation_id else False

    async def get_validation_by_client(self, client_id):
        row = await self.execute(
            validation_table.select().where(
                and_(
                    validation_table.c.client_id == client_id,
                    validation_table.c.date >= TimeManager.get_ts() - self.pin_ttl,
                )
            ).order_by(validation_table.c.date.desc())
        )
        return ClientValidationFull(**row) if row else False
