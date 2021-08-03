import sqlite3
from sqlite3.dbapi2 import Connection

ADMIN_INFO_QUERY = """
        CREATE TABLE IF NOT EXISTS AdminInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """

BOOKING_INFO_QUERY = """
        CREATE TABLE IF NOT EXISTS BookingInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        topic TEXT 
    );
    """

CREATE_SLOTS_QUERY = """
        CREATE TABLE IF NOT EXISTS Slots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_interval TEXT NOT NULL UNIQUE,
        booking_id INTEGER,
        FOREIGN KEY(booking_id) REFERENCES BookingInfo(id)
    );
    """


def create_connection(path_to_db=":memory:") -> Connection:
    """
    Creates a connection to the database path.
    By default returns a connection to memory.
    """
    return sqlite3.connect(path_to_db)


def create_table(connection: Connection, query: str) -> None:
    connection.execute(query)
    connection.commit()


def create_admininfo_table(connection: Connection) -> None:
    """
    Creates AdminInfo(id, email, password) table using specified connection.
    """

    create_table(connection, ADMIN_INFO_QUERY)


def create_bookinginfo_table(connection: Connection) -> None:
    """
    Creates BookingInfo(id, name, email, topic) table using specified connection.
    """

    create_table(connection, BOOKING_INFO_QUERY)


def create_slots_table(connection: Connection) -> None:
    """
    Creates Slots(id, start_interval, booking_id) table using specified connection and
    add foreign key for BookingInfo id.
    By default guest's info is null or is taken from BookingInfo.
    """

    create_table(connection, CREATE_SLOTS_QUERY)
