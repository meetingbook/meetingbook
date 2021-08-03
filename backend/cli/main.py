#!/Usr/bin/env python
import comand_line_parser as par
import db


parser = par.createParser()
params = parser.parse_args()
con = db.create_connection(params.path)
db.create_slots_table(con)
db.create_admininfo_table(con)
db.create_bookinginfo_table(con)

par.correctness_commands(params)
