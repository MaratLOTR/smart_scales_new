"""init

Revision ID: 3036d9dd0d45
Revises: 
Create Date: 2023-09-28 09:21:05.401889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3036d9dd0d45'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parameters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('muscle_mass', sa.Integer(), nullable=True),
    sa.Column('fat_mass', sa.Integer(), nullable=True),
    sa.Column('pulse', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('standards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('muscle_mass', sa.Integer(), nullable=True),
    sa.Column('fat_mass', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('standards_id', sa.Integer(), nullable=False),
    sa.Column('parameters_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parameters_id'], ['parameters.id'], ),
    sa.ForeignKeyConstraint(['standards_id'], ['standards.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('standards')
    op.drop_table('parameters')
    # ### end Alembic commands ###
