#!usr/bin/python
from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Database setup
engine = create_engine('sqlite:///lib/db/bank_account.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @classmethod
    def create_user(cls, username):
        user = cls(name=username)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_user_by_id(cls, user_id):
        return session.query(cls).filter_by(id=user_id).first()

    @classmethod
    def get_all_users(cls):
        return session.query(cls).all()

    @classmethod
    def update_user(cls, user_id, new_name):
        user = cls.get_user_by_id(user_id)
        if user:
            user.name = new_name
            session.commit()
            return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        user = cls.get_user_by_id(user_id)
        if user:
            session.delete(user)
            session.commit()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Float, default=0.0)
    user = relationship('User')

    @classmethod
    def create_account(cls, user_id, initial_balance=0.0):
        account = cls(user_id=user_id, balance=initial_balance)
        session.add(account)
        session.commit()
        return account

    @classmethod
    def get_account_by_id(cls, account_id):
        return session.query(cls).filter_by(id=account_id).first()

    @classmethod
    def update_account_balance(cls, account_id, new_balance):
        account = cls.get_account_by_id(account_id)
        if account:
            account.balance = new_balance
            session.commit()
            return account
        return None

    @classmethod
    def delete_account(cls, account_id):
        account = cls.get_account_by_id(account_id)
        if account:
            session.delete(account)
            session.commit()

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Float)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    account = relationship('Account')

    @classmethod
    def create_transaction(cls, account_id, amount, transaction_date=None):
        if transaction_date is None:
            transaction_date = datetime.utcnow()
        transaction = cls(account_id=account_id, amount=amount, transaction_date=transaction_date)
        session.add(transaction)
        session.commit()
        return transaction

    @classmethod
    def get_transaction_by_id(cls, transaction_id):
        return session.query(cls).filter_by(id=transaction_id).first()

    @classmethod
    def get_transactions_by_account_id(cls, account_id):
        return session.query(cls).filter_by(account_id=account_id).all()

    @classmethod
    def delete_transaction(cls, transaction_id):
        transaction = cls.get_transaction_by_id(transaction_id)
        if transaction:
            session.delete(transaction)
            session.commit()
