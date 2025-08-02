_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qlogicModules,qlogicProducts=mibBuilder.importSymbols('QLOGIC-SMI','qlogicModules','qlogicProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qlogicProductsMIB=ModuleIdentity((1,3,6,1,4,1,3873,2,1))
if mibBuilder.loadTexts:qlogicProductsMIB.setRevisions(('2013-03-29 00:00','2009-09-29 00:00','2009-03-03 00:00','2009-02-17 00:00','2006-10-11 00:00','2006-10-06 00:00','2005-08-23 00:00'))
_SanBox6140_ObjectIdentity=ObjectIdentity
sanBox6140=_SanBox6140_ObjectIdentity((1,3,6,1,4,1,3873,1,1))
if mibBuilder.loadTexts:sanBox6140.setStatus(_A)
_EvaISCSI_ObjectIdentity=ObjectIdentity
evaISCSI=_EvaISCSI_ObjectIdentity((1,3,6,1,4,1,3873,1,2))
if mibBuilder.loadTexts:evaISCSI.setStatus(_A)
_Reserved3_ObjectIdentity=ObjectIdentity
reserved3=_Reserved3_ObjectIdentity((1,3,6,1,4,1,3873,1,3))
_Mpx100_ObjectIdentity=ObjectIdentity
mpx100=_Mpx100_ObjectIdentity((1,3,6,1,4,1,3873,1,4))
if mibBuilder.loadTexts:mpx100.setStatus(_A)
_ISR6140_ObjectIdentity=ObjectIdentity
iSR6140=_ISR6140_ObjectIdentity((1,3,6,1,4,1,3873,1,5))
if mibBuilder.loadTexts:iSR6140.setStatus(_A)
_ISR6142_ObjectIdentity=ObjectIdentity
iSR6142=_ISR6142_ObjectIdentity((1,3,6,1,4,1,3873,1,6))
if mibBuilder.loadTexts:iSR6142.setStatus(_A)
_Mpx110_ObjectIdentity=ObjectIdentity
mpx110=_Mpx110_ObjectIdentity((1,3,6,1,4,1,3873,1,7))
if mibBuilder.loadTexts:mpx110.setStatus(_A)
_Reserved8_ObjectIdentity=ObjectIdentity
reserved8=_Reserved8_ObjectIdentity((1,3,6,1,4,1,3873,1,8))
_SanBox5802_ObjectIdentity=ObjectIdentity
sanBox5802=_SanBox5802_ObjectIdentity((1,3,6,1,4,1,3873,1,9))
if mibBuilder.loadTexts:sanBox5802.setStatus(_A)
_Reserved10_ObjectIdentity=ObjectIdentity
reserved10=_Reserved10_ObjectIdentity((1,3,6,1,4,1,3873,1,10))
_HpStorageWorks820FcSwitch_ObjectIdentity=ObjectIdentity
hpStorageWorks820FcSwitch=_HpStorageWorks820FcSwitch_ObjectIdentity((1,3,6,1,4,1,3873,1,11))
if mibBuilder.loadTexts:hpStorageWorks820FcSwitch.setStatus(_A)
_Reserved12_ObjectIdentity=ObjectIdentity
reserved12=_Reserved12_ObjectIdentity((1,3,6,1,4,1,3873,1,12))
_Reserved13_ObjectIdentity=ObjectIdentity
reserved13=_Reserved13_ObjectIdentity((1,3,6,1,4,1,3873,1,13))
_SanBox5800_ObjectIdentity=ObjectIdentity
sanBox5800=_SanBox5800_ObjectIdentity((1,3,6,1,4,1,3873,1,14))
if mibBuilder.loadTexts:sanBox5800.setStatus(_A)
_Reserved15_ObjectIdentity=ObjectIdentity
reserved15=_Reserved15_ObjectIdentity((1,3,6,1,4,1,3873,1,15))
_Reserved16_ObjectIdentity=ObjectIdentity
reserved16=_Reserved16_ObjectIdentity((1,3,6,1,4,1,3873,1,16))
_ISR6200_ObjectIdentity=ObjectIdentity
iSR6200=_ISR6200_ObjectIdentity((1,3,6,1,4,1,3873,1,17))
if mibBuilder.loadTexts:iSR6200.setStatus(_A)
_Mpx200_ObjectIdentity=ObjectIdentity
mpx200=_Mpx200_ObjectIdentity((1,3,6,1,4,1,3873,1,18))
if mibBuilder.loadTexts:mpx200.setStatus(_A)
_Mez50_ObjectIdentity=ObjectIdentity
mez50=_Mez50_ObjectIdentity((1,3,6,1,4,1,3873,1,19))
if mibBuilder.loadTexts:mez50.setStatus(_A)
_SanBox3810_ObjectIdentity=ObjectIdentity
sanBox3810=_SanBox3810_ObjectIdentity((1,3,6,1,4,1,3873,1,20))
if mibBuilder.loadTexts:sanBox3810.setStatus(_A)
_Reserved21_ObjectIdentity=ObjectIdentity
reserved21=_Reserved21_ObjectIdentity((1,3,6,1,4,1,3873,1,21))
_Reserved22_ObjectIdentity=ObjectIdentity
reserved22=_Reserved22_ObjectIdentity((1,3,6,1,4,1,3873,1,22))
_Reserved23_ObjectIdentity=ObjectIdentity
reserved23=_Reserved23_ObjectIdentity((1,3,6,1,4,1,3873,1,23))
_HpStorageWorksSN6000SingleFcSwitch_ObjectIdentity=ObjectIdentity
hpStorageWorksSN6000SingleFcSwitch=_HpStorageWorksSN6000SingleFcSwitch_ObjectIdentity((1,3,6,1,4,1,3873,1,24))
if mibBuilder.loadTexts:hpStorageWorksSN6000SingleFcSwitch.setStatus(_A)
_HpStorageWorksSN6000DualFcSwitch_ObjectIdentity=ObjectIdentity
hpStorageWorksSN6000DualFcSwitch=_HpStorageWorksSN6000DualFcSwitch_ObjectIdentity((1,3,6,1,4,1,3873,1,25))
if mibBuilder.loadTexts:hpStorageWorksSN6000DualFcSwitch.setStatus(_A)
_Reserved26_ObjectIdentity=ObjectIdentity
reserved26=_Reserved26_ObjectIdentity((1,3,6,1,4,1,3873,1,26))
_Reserved27_ObjectIdentity=ObjectIdentity
reserved27=_Reserved27_ObjectIdentity((1,3,6,1,4,1,3873,1,27))
_Reserved28_ObjectIdentity=ObjectIdentity
reserved28=_Reserved28_ObjectIdentity((1,3,6,1,4,1,3873,1,28))
_Reserved29_ObjectIdentity=ObjectIdentity
reserved29=_Reserved29_ObjectIdentity((1,3,6,1,4,1,3873,1,29))
_Reserved30_ObjectIdentity=ObjectIdentity
reserved30=_Reserved30_ObjectIdentity((1,3,6,1,4,1,3873,1,30))
_Reserved31_ObjectIdentity=ObjectIdentity
reserved31=_Reserved31_ObjectIdentity((1,3,6,1,4,1,3873,1,31))
_Reserved32_ObjectIdentity=ObjectIdentity
reserved32=_Reserved32_ObjectIdentity((1,3,6,1,4,1,3873,1,32))
_Reserved33_ObjectIdentity=ObjectIdentity
reserved33=_Reserved33_ObjectIdentity((1,3,6,1,4,1,3873,1,33))
_Sns2120_ObjectIdentity=ObjectIdentity
sns2120=_Sns2120_ObjectIdentity((1,3,6,1,4,1,3873,1,34))
if mibBuilder.loadTexts:sns2120.setStatus(_A)
_Reserved35_ObjectIdentity=ObjectIdentity
reserved35=_Reserved35_ObjectIdentity((1,3,6,1,4,1,3873,1,35))
_Reserved36_ObjectIdentity=ObjectIdentity
reserved36=_Reserved36_ObjectIdentity((1,3,6,1,4,1,3873,1,36))
_Reserved37_ObjectIdentity=ObjectIdentity
reserved37=_Reserved37_ObjectIdentity((1,3,6,1,4,1,3873,1,37))
_Reserved38_ObjectIdentity=ObjectIdentity
reserved38=_Reserved38_ObjectIdentity((1,3,6,1,4,1,3873,1,38))
_Reserved39_ObjectIdentity=ObjectIdentity
reserved39=_Reserved39_ObjectIdentity((1,3,6,1,4,1,3873,1,39))
_Reserved40_ObjectIdentity=ObjectIdentity
reserved40=_Reserved40_ObjectIdentity((1,3,6,1,4,1,3873,1,40))
_Reserved41_ObjectIdentity=ObjectIdentity
reserved41=_Reserved41_ObjectIdentity((1,3,6,1,4,1,3873,1,41))
_Reserved42_ObjectIdentity=ObjectIdentity
reserved42=_Reserved42_ObjectIdentity((1,3,6,1,4,1,3873,1,42))
_Reserved43_ObjectIdentity=ObjectIdentity
reserved43=_Reserved43_ObjectIdentity((1,3,6,1,4,1,3873,1,43))
mibBuilder.exportSymbols('QLOGIC-PRODUCTS-MIB',**{'sanBox6140':sanBox6140,'evaISCSI':evaISCSI,'reserved3':reserved3,'mpx100':mpx100,'iSR6140':iSR6140,'iSR6142':iSR6142,'mpx110':mpx110,'reserved8':reserved8,'sanBox5802':sanBox5802,'reserved10':reserved10,'hpStorageWorks820FcSwitch':hpStorageWorks820FcSwitch,'reserved12':reserved12,'reserved13':reserved13,'sanBox5800':sanBox5800,'reserved15':reserved15,'reserved16':reserved16,'iSR6200':iSR6200,'mpx200':mpx200,'mez50':mez50,'sanBox3810':sanBox3810,'reserved21':reserved21,'reserved22':reserved22,'reserved23':reserved23,'hpStorageWorksSN6000SingleFcSwitch':hpStorageWorksSN6000SingleFcSwitch,'hpStorageWorksSN6000DualFcSwitch':hpStorageWorksSN6000DualFcSwitch,'reserved26':reserved26,'reserved27':reserved27,'reserved28':reserved28,'reserved29':reserved29,'reserved30':reserved30,'reserved31':reserved31,'reserved32':reserved32,'reserved33':reserved33,'sns2120':sns2120,'reserved35':reserved35,'reserved36':reserved36,'reserved37':reserved37,'reserved38':reserved38,'reserved39':reserved39,'reserved40':reserved40,'reserved41':reserved41,'reserved42':reserved42,'reserved43':reserved43,'qlogicProductsMIB':qlogicProductsMIB})