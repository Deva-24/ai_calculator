import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from calculator import Calculator, History, Base

# Setup the database for testing
@pytest.fixture(scope="module")
def db_session():
    engine = create_engine('postgresql://username:password@localhost:5432/testdb')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()

# Test saving operations to history
def test_save_history(db_session):
    calc = Calculator(db_session)
    calc.add(5, 10)
    calc.subtract(10, 5)

    history = db_session.query(History).all()
    assert len(history) == 2, "Expected 2 history entries, but got {len(history)}"

# Test clearing history
def test_clear_history(db_session):
    calc = Calculator(db_session)
    calc.add(5, 10)
    calc.clear_history()

    history = db_session.query(History).all()
    assert len(history) == 0, "Expected 0 history entries, but got {len(history)}"

# Test undo operation
def test_undo(db_session):
    calc = Calculator(db_session)
    calc.add(5, 10)
    calc.subtract(10, 5)
    calc.undo()

    history = db_session.query(History).all()
    assert len(history) == 1, "Expected 1 history entry, but got {len(history)}"

# Test redo operation
def test_redo(db_session):
    calc = Calculator(db_session)
    calc.add(5, 10)
    calc.subtract(10, 5)
    calc.undo()
    calc.redo()

    history = db_session.query(History).all()
    assert len(history) == 2, "Expected 2 history entries, but got {len(history)}"
