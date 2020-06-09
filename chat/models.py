from channels.db import database_sync_to_async


async def connect(self):
    self.username = await database_sync_to_async(self.get_name)()


def get_name(User):
    return User.objects.all()[0].name
