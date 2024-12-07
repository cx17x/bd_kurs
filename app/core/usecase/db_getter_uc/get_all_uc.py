import dataclasses
from typing import List, Dict

from app.core.i_for_uc.i_db_getter import BaseDBGetter


@dataclasses.dataclass
class GetAllRecordsDTO:
    table_name: str


class GetAllRecordsUC:
    def __init__(self, db_gateway: BaseDBGetter):
        self.db_gateway = db_gateway

    async def execute(self, dto: GetAllRecordsDTO) -> List[Dict]:
        """Execute the use case to get all records from a table."""
        records = await self.db_gateway.get_all(table_name=dto.table_name)
        return records
