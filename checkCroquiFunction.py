from PyQt4.QtSql import QSqlDatabase					
import os
name= "Rai"; 
report = open("d:/relatorio_{0}.txt".format(name),"w")
db = QSqlDatabase('QOCISPATIAL')
if db.isValid():
    # string
    db.setHostName('s324-prodabel.pbh')
    # string
    db.setDatabaseName('geodsv1')
    # string
    db.setUserName('tinorberto')
    # string
    db.setPassword('tiago123')
    # integer e.g. 5432
    db.setPort(1521);
    if db.open():
        for file in os.listdir("D:\CROQUIS_FAZENDA\croqui smf\pacote_croqui_interno_SMAAR\{0}".format(name)):
            if file.endswith(".dwg"):
                file = file.replace('.dwg','')
                print """select TRIBUTARIO.CHECK_IMOVEL_IPTU('{0}') from dual""".format(file)
                query = db.exec_("""select TRIBUTARIO.CHECK_IMOVEL_IPTU('{0}') from dual""".format(file))
                # iterate over the rows
                while query.next(): 
                    print "-------"
                    record = query.record()
                    print "Resultado "+str(record.value(0))
                    report.write("\n{0} - {1}".format(file, str(record.value(0))))
    report.close()