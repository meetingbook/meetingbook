#!/usr/bin/env python
from cli.db import create_connection, create_slots_table, create_admininfo_table, create_bookinginfo_table
from cli.parser import createParser, correctness_commands


def main():
    parser = createParser()
    params = parser.parse_args()
    con = create_connection(params.path)
    create_slots_table(con)
    create_admininfo_table(con)
    create_bookinginfo_table(con)

    correctness_commands(params)


if __name__ == "__main__":
    # execute only if run as a script
    main()
