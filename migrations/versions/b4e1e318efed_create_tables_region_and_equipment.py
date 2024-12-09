"""create tables Region and Equipment

Revision ID: b4e1e318efed
Revises: 
Create Date: 2024-12-08 22:02:04.574188
"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b4e1e318efed'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE IF NOT EXISTS Region (
            plot_code INT PRIMARY KEY,
            soil_type VARCHAR(50),
            plot_description TEXT,
            harvest_code INT
        );
    """)
    op.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            employee_code INT PRIMARY KEY,
            full_name VARCHAR(255) NOT NULL,
            position VARCHAR(50) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            plot_code INT,
            FOREIGN KEY (plot_code) REFERENCES Region(plot_code)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS Equipment (
            equipment_code INT PRIMARY KEY,
            equipment_type VARCHAR(50),
            condition VARCHAR(50),
            employee_code INT,
            region_code INT,
            FOREIGN KEY (employee_code) REFERENCES Employee(employee_code),
            FOREIGN KEY (region_code) REFERENCES Region(plot_code)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS Harvest (
            harvest_code INT PRIMARY KEY,
            harvest_type VARCHAR(50) NOT NULL,
            quantity INT NOT NULL
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            order_number INT PRIMARY KEY,
            status VARCHAR(50) NOT NULL,
            order_date DATE NOT NULL,
            employee_code INT,
            FOREIGN KEY (employee_code) REFERENCES Employee(employee_code)
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            role VARCHAR(20) NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS Employee;")
    op.execute("DROP TABLE IF EXISTS Orders;")
    op.execute("DROP TABLE IF EXISTS Harvest;")
    op.execute("DROP TABLE IF EXISTS Equipment;")
    op.execute("DROP TABLE IF EXISTS Region;")
