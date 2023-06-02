"""Add timestamps to users table

Revision ID: 1ddb4cc256d8
Revises: 6df5a76814a3
Create Date: 2023-06-02 19:52:33.166636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ddb4cc256d8'
down_revision = '6df5a76814a3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('modified_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(DATE(\'now\'))'), nullable=False))
    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('(DATE(\'now\'))'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'modified_at')
    # ### end Alembic commands ###