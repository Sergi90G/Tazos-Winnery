"""added photo pass

Revision ID: 06f60d766425
Revises: ebb877a5b917
Create Date: 2023-09-17 22:35:46.639200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06f60d766425'
down_revision = 'ebb877a5b917'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_path', sa.String(length=255), nullable=True))
        batch_op.drop_column('profile_image_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_image_url', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('profile_path')

    # ### end Alembic commands ###