import dataclasses

from app.core.i_for_uc.i_db_getter import BaseDBGetter


@dataclasses.dataclass
class DeleteRecordByIdDTO:
    table_name: str
    id_column: str
    record_id: int


class DeleteRecordByIdUC:
    def __init__(self, db_gateway: BaseDBGetter):
        self.db_gateway = db_gateway

    async def execute(self, dto: DeleteRecordByIdDTO) -> None:
        """Execute the use case to delete a record by ID."""
        await self.db_gateway.delete_by_id(
            table_name=dto.table_name,
            id_column=dto.id_column,
            record_id=dto.record_id
        )
