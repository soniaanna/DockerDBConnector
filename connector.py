import ibm_db
import creds


def NetcoolConnect(reportingStartDateFinal, reportingEndDateFinal):
    conn = ibm_db.connect(f"DATABASE={creds.DB};HOSTNAME={creds.HOSTNAME};PORT={creds.PORT};PROTOCOL=TCPIP;UID"
                          f"={creds.UID};PWD={creds.PWD};", "", "")
    sql = "select * from DB2INST1.REPORTER_STATUS, DB2INST1.reporter_names  WHERE DB2INST1.REPORTER_STATUS.OWNERUID = DB2INST1.reporter_names.OWNERUID AND FIRSTOCCURRENCE > '%s' AND FIRSTOCCURRENCE < '%s' AND SEVERITY = '5'"%(reportingStartDateFinal, reportingEndDateFinal)
    stmt = ibm_db.exec_immediate(conn, sql)
    return(stmt)

print(NetcoolConnect('2019-07-10 17:04:11','2020-07-10 17:04:11'))
