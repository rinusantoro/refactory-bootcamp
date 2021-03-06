"""empty message

Revision ID: fe15cde0cd05
Revises: 
Create Date: 2020-09-21 15:26:09.526037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe15cde0cd05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=230), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('prodis',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nama_prodi', sa.String(length=140), nullable=False),
    sa.Column('fakultas', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nama_prodi')
    )
    op.create_table('proposals',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('tgl_daftar', sa.Date(), nullable=False),
    sa.Column('nim', sa.String(length=10), nullable=False),
    sa.Column('nama_mhs', sa.String(length=100), nullable=False),
    sa.Column('jml_sks', sa.String(length=5), nullable=True),
    sa.Column('jml_ipk', sa.String(length=5), nullable=True),
    sa.Column('judul', sa.String(length=150), nullable=True),
    sa.Column('pembimbing', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('prodi_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['prodi_id'], ['prodis.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nim')
    )
    op.create_index(op.f('ix_proposals_email'), 'proposals', ['email'], unique=True)
    op.create_table('proposal_files',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('proposal_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proposal_files_created_at'), 'proposal_files', ['created_at'], unique=False)
    op.create_index(op.f('ix_proposal_files_updated_at'), 'proposal_files', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proposal_files_updated_at'), table_name='proposal_files')
    op.drop_index(op.f('ix_proposal_files_created_at'), table_name='proposal_files')
    op.drop_table('proposal_files')
    op.drop_index(op.f('ix_proposals_email'), table_name='proposals')
    op.drop_table('proposals')
    op.drop_table('prodis')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
