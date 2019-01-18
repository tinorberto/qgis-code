from PyQt4.QtSql import QSqlDatabase					
import os

t = [['ADE','ID_ADE'],
['AEIS','ID_AEIS'],
['AREA_ABRANGENCIA_SAUDE','ID_AAS'],
['AREA_RISCO_GEOLOGICO','ID_ARG'],
['BAIRRO_CARTORIAL','ID_BAC'],
['BAIRRO_POPULAR','ID'],
['EQUIP_SAUDE','ID_EQ_SAUDE'],
['ILUM_PUBLICA','ID_BASE_IP'],
['JURISDICAO_ESCOLAR_EF','ID_JUREF'],
['JURISDICAO_ESCOLAR_EI','ID_JUREF'],
['JURISDICAO_ESCOLAR_EI_CRECHE','ID_JURCR'],
['LOCAL_ENTREGA_VOLUNTARIA','ID_LEV'],
['MEIO_FIO','ID_BASE_MF'],
['OPERACAO_URBANA','ID_OPU'],
['PRACA','ID_PRC'],
['REDE_ELETRICA','ID_BASE_RE'],
['REDE_TELEFONICA','ID_BASE_RT'],
['REGIONAL','ID'],
['TERRITORIO_CRAS','ID_TER_CRAS'],
['UNID_CONSERV_AMBIENTAL','ID_UCA'],
['UNID_RECEB_PEQN_VOLUME','ID_URPV'],
['VILA_FAVELA','ID_VF']]


db = QSqlDatabase('QOCISPATIAL')
if db.isValid():
    # string
    db.setHostName('s340-prodabel')
    # string
    db.setDatabaseName('geocprd')
    # string
    db.setUserName('le_geoc')
    # string
    db.setPassword('Usrcale_geoc_prd')
    # integer e.g. 5432
    db.setPort(1521);


db.open()


for data in t:

    print """select {0} , count({0}) from  idepbh.{1}  group by {0} having count ({0}) > 1""".format( data[1], data[0])
    query = db.exec_( """select {0} , count({0}) from  idepbh.{1}  group by {0} having count ({0}) > 1""".format( data[1], data[0]))
    #query = db.exec_( """ Select 1 as n  from dual""")
#    print query.isValid()

    # iterate over the rows
    while query.next(): 
        print data[1]+"----"+ data[0]
        record = query.record()
        print "Resultado "+str(record.value(0))
    
