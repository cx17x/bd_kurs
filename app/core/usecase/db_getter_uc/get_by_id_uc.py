import dataclasses
from typing import Optional, Dict

from app.core.i_for_uc.i_db_getter import BaseDBGetter


@dataclasses.dataclass
class GetRecordByIdDTO:
    table_name: str
    id_column: str
    record_id: int


class GetRecordByIdUC:
    def __init__(self, db_gateway: BaseDBGetter):
        self.db_gateway = db_gateway

    async def execute(self, dto: GetRecordByIdDTO) -> Optional[Dict]:
        """Execute the use case to get a record by ID."""
        record = await self.db_gateway.get_by_id(
            table_name=dto.table_name,
            id_column=dto.id_column,
            record_id=dto.record_id
        )
        return record
