_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
products,=mibBuilder.importSymbols('AVAYAGEN-MIB','products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
avSMEPlatformProdMIB=ModuleIdentity((1,3,6,1,4,1,6889,1,48))
if mibBuilder.loadTexts:avSMEPlatformProdMIB.setRevisions(('2014-05-30 12:00','2014-04-03 12:00','2013-01-23 16:00','2012-11-29 12:00','2012-05-10 12:35','2012-04-09 10:25','2012-03-05 10:05','2011-12-16 13:30','2011-12-14 15:35','2011-12-07 14:10','2011-05-03 13:30','2011-03-30 09:22','2010-07-07 13:50','2010-07-06 13:45','2010-07-02 15:06'))
_SmepProdVariants_ObjectIdentity=ObjectIdentity
smepProdVariants=_SmepProdVariants_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1))
_SmepCfg1_ObjectIdentity=ObjectIdentity
smepCfg1=_SmepCfg1_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,1))
if mibBuilder.loadTexts:smepCfg1.setStatus(_A)
_SmepCfg2_ObjectIdentity=ObjectIdentity
smepCfg2=_SmepCfg2_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,2))
if mibBuilder.loadTexts:smepCfg2.setStatus(_A)
_SmepCfg3_ObjectIdentity=ObjectIdentity
smepCfg3=_SmepCfg3_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,3))
if mibBuilder.loadTexts:smepCfg3.setStatus(_A)
_SmepCfg4_ObjectIdentity=ObjectIdentity
smepCfg4=_SmepCfg4_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,4))
if mibBuilder.loadTexts:smepCfg4.setStatus(_A)
_SmepCfg5_ObjectIdentity=ObjectIdentity
smepCfg5=_SmepCfg5_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,5))
if mibBuilder.loadTexts:smepCfg5.setStatus(_A)
_SmepCfg6_ObjectIdentity=ObjectIdentity
smepCfg6=_SmepCfg6_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,6))
if mibBuilder.loadTexts:smepCfg6.setStatus(_A)
_SmepCfg7_ObjectIdentity=ObjectIdentity
smepCfg7=_SmepCfg7_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,7))
if mibBuilder.loadTexts:smepCfg7.setStatus(_A)
_SmepCfg8_ObjectIdentity=ObjectIdentity
smepCfg8=_SmepCfg8_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,8))
if mibBuilder.loadTexts:smepCfg8.setStatus(_A)
_SmepCfg9_ObjectIdentity=ObjectIdentity
smepCfg9=_SmepCfg9_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,9))
if mibBuilder.loadTexts:smepCfg9.setStatus(_A)
_SmepCfg10_ObjectIdentity=ObjectIdentity
smepCfg10=_SmepCfg10_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,10))
if mibBuilder.loadTexts:smepCfg10.setStatus(_A)
_SmepCfg11_ObjectIdentity=ObjectIdentity
smepCfg11=_SmepCfg11_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,11))
if mibBuilder.loadTexts:smepCfg11.setStatus(_A)
_SmepCfg12_ObjectIdentity=ObjectIdentity
smepCfg12=_SmepCfg12_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,12))
if mibBuilder.loadTexts:smepCfg12.setStatus(_A)
_SmepCfg13_ObjectIdentity=ObjectIdentity
smepCfg13=_SmepCfg13_ObjectIdentity((1,3,6,1,4,1,6889,1,48,1,13))
if mibBuilder.loadTexts:smepCfg13.setStatus(_A)
_SmepProdServices_ObjectIdentity=ObjectIdentity
smepProdServices=_SmepProdServices_ObjectIdentity((1,3,6,1,4,1,6889,1,48,2))
_SmepProdServiceOneXPortal_ObjectIdentity=ObjectIdentity
smepProdServiceOneXPortal=_SmepProdServiceOneXPortal_ObjectIdentity((1,3,6,1,4,1,6889,1,48,2,1))
if mibBuilder.loadTexts:smepProdServiceOneXPortal.setStatus(_A)
_SmepProdServiceVoicemailPro_ObjectIdentity=ObjectIdentity
smepProdServiceVoicemailPro=_SmepProdServiceVoicemailPro_ObjectIdentity((1,3,6,1,4,1,6889,1,48,2,2))
if mibBuilder.loadTexts:smepProdServiceVoicemailPro.setStatus(_A)
_SmepProdServiceContactRecorder_ObjectIdentity=ObjectIdentity
smepProdServiceContactRecorder=_SmepProdServiceContactRecorder_ObjectIdentity((1,3,6,1,4,1,6889,1,48,2,3))
if mibBuilder.loadTexts:smepProdServiceContactRecorder.setStatus(_A)
_SmepProdPorts_ObjectIdentity=ObjectIdentity
smepProdPorts=_SmepProdPorts_ObjectIdentity((1,3,6,1,4,1,6889,1,48,3))
_SmepProdPortLAN_ObjectIdentity=ObjectIdentity
smepProdPortLAN=_SmepProdPortLAN_ObjectIdentity((1,3,6,1,4,1,6889,1,48,3,1))
if mibBuilder.loadTexts:smepProdPortLAN.setStatus(_A)
_SmepProdDongleModules_ObjectIdentity=ObjectIdentity
smepProdDongleModules=_SmepProdDongleModules_ObjectIdentity((1,3,6,1,4,1,6889,1,48,4))
_SmepProdGenericDongle_ObjectIdentity=ObjectIdentity
smepProdGenericDongle=_SmepProdGenericDongle_ObjectIdentity((1,3,6,1,4,1,6889,1,48,4,1))
if mibBuilder.loadTexts:smepProdGenericDongle.setStatus(_A)
mibBuilder.exportSymbols('AV-SME-PLATFORM-PROD-MIB',**{'avSMEPlatformProdMIB':avSMEPlatformProdMIB,'smepProdVariants':smepProdVariants,'smepCfg1':smepCfg1,'smepCfg2':smepCfg2,'smepCfg3':smepCfg3,'smepCfg4':smepCfg4,'smepCfg5':smepCfg5,'smepCfg6':smepCfg6,'smepCfg7':smepCfg7,'smepCfg8':smepCfg8,'smepCfg9':smepCfg9,'smepCfg10':smepCfg10,'smepCfg11':smepCfg11,'smepCfg12':smepCfg12,'smepCfg13':smepCfg13,'smepProdServices':smepProdServices,'smepProdServiceOneXPortal':smepProdServiceOneXPortal,'smepProdServiceVoicemailPro':smepProdServiceVoicemailPro,'smepProdServiceContactRecorder':smepProdServiceContactRecorder,'smepProdPorts':smepProdPorts,'smepProdPortLAN':smepProdPortLAN,'smepProdDongleModules':smepProdDongleModules,'smepProdGenericDongle':smepProdGenericDongle})