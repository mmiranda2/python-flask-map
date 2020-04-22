"""empty message

Revision ID: d842c1c1f7b9
Revises: f12de8a0ea26
Create Date: 2019-12-25 13:45:35.540125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd842c1c1f7b9'
down_revision = 'f12de8a0ea26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('GeoJSONs', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('GeoJSONs', sa.Column('uuid', sa.String(length=255), nullable=True))
    op.add_column('Users', sa.Column('session_token', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('GeoJSONs', 'name')
    op.drop_column('GeoJSONs', 'uuid')
    op.drop_column('Users', 'session_token')
    # ### end Alembic commands ###