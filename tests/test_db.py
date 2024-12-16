import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from calculator import Base, History, Calculator

# Setup and teardown of the database
@pytest.fixture(scope="module")
def db_session():
    engine = create_engine('postgresql://username:password@localhost:5432/testdb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()

# Test the database connection
def test_database_connection(db_session):
    assert db_session is not None, "Database session is None"

# Test if the History table exists
def test_history_table_exists(db_session):
    result = db_session.query(History).all()
    assert result is not None, "History table does not exist"

# Test saving a record to the history table
def test_save_history_to_db(db_session):
    calc = Calculator(db_session)
    calc.add(5, 10)

    history = db_session.query(History).all()
    assert len(history) > 0, "No history records found in the database"
