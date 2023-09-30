from sqlalchemy import select

from infrastructure.database.models.slots import WorkingHour
from infrastructure.database.repo.base import BaseRepo


class SlotRepo(BaseRepo):
    async def get_working_hours(self, location_id: int):
        query = select(WorkingHour).where(WorkingHour.location_id == location_id)
        return (await self.session.scalars(query)).all()
