#!usr/bin/python

from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Database setup
# Create an SQLite engine and bind it to a session
engine = create_engine('sqlite:///lib/db/bank_account.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for the models
Base = declarative_base()

# Create all tables in the engine
Base.metadata.create_all(engine)

# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Class method to create a new user
    @classmethod
    def create_user(cls, username):
        user = cls(name=username)
        session.add(user)
        session.commit()
        return user

    # Class method to get a user by ID
    @classmethod
    def get_user_by_id(cls, user_id):
        return session.query(cls).filter_by(id=user_id).first()

    # Class method to get all users
    @classmethod
    def get_all_users(cls):
        return session.query(cls).all()

    # Class method to update a user's name
    @classmethod
    def update_user(cls, user_id, new_name):
        user = cls.get_user_by_id(user_id)
        if user:
            user.name = new_name
            session.commit()
            return user
        return None

    # Class method to delete a user by ID
    @classmethod
    def delete_user(cls, user_id):
        user = cls.get_user_by_id(user_id)
        if user:
            session.delete(user)
            session.commit()

# Define the Account model
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Float, default=0.0)
    user = relationship('User')

    # Class method to create a new account
    @classmethod
    def create_account(cls, user_id, initial_balance=0.0):
        account = cls(user_id=user_id, balance=initial_balance)
        session.add(account)
        session.commit()
        return account

    # Class method to get an account by ID
    @classmethod
    def get_account_by_id(cls, account_id):
        return session.query(cls).filter_by(id=account_id).first()

    # Class method to update an account's balance
    @classmethod
    def update_account_balance(cls, account_id, new_balance):
        account = cls.get_account_by_id(account_id)
        if account:
            account.balance = new_balance
            session.commit()
            return account
        return None

    # Class method to delete an account by ID
    @classmethod
    def delete_account(cls, account_id):
        account = cls.get_account_by_id(account_id)
        if account:
            session.delete(account)
            session.commit()

# Define the Transaction model
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Float)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    account = relationship('Account')

    # Class method to create a new transaction
    @classmethod
    def create_transaction(cls, account_id, amount, transaction_date=None):
        if transaction_date is None:
            transaction_date = datetime.utcnow()
        transaction = cls(account_id=account_id, amount=amount, transaction_date=transaction_date)
        session.add(transaction)
        session.commit()
        return transaction

    # Class method to get a transaction by ID
    @classmethod
    def get_transaction_by_id(cls, transaction_id):
        return session.query(cls).filter_by(id=transaction_id).first()

    # Class method to get all transactions for a specific account ID
    @classmethod
    def get_transactions_by_account_id(cls, account_id):
        return session.query(cls).filter_by(account_id=account_id).all()

    # Class method to delete a transaction by ID
    @classmethod
    def delete_transaction(cls, transaction_id):
        transaction = cls.get_transaction_by_id(transaction_id)
        if transaction:
            session.delete(transaction)
            session.commit()
