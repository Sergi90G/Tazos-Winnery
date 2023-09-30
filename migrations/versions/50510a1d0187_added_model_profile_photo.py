"""added model profile-photo

Revision ID: 50510a1d0187
Revises: 06f60d766425
Create Date: 2023-09-20 11:47:56.965992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50510a1d0187'
down_revision = '06f60d766425'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_photo', sa.String(length=255), nullable=True))
        batch_op.drop_column('profile_path')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_path', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('profile_photo')

    # ### end Alembic commands ###