_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,lhnNsm=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG-MIB','lhnModules','lhnNsm')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lhnNsmMib=ModuleIdentity((1,3,6,1,4,1,9804,2,1,1))
if mibBuilder.loadTexts:lhnNsmMib.setRevisions(('2013-11-22 00:00','2013-06-25 00:00','2012-09-04 00:00','2011-06-21 00:00','2010-09-07 00:00','2010-07-19 00:00','2009-11-20 00:00','2009-03-10 00:00','2008-01-24 00:00'))
_LhnNsmDevices_ObjectIdentity=ObjectIdentity
lhnNsmDevices=_LhnNsmDevices_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1))
if mibBuilder.loadTexts:lhnNsmDevices.setStatus(_A)
_LhnNsmEvents_ObjectIdentity=ObjectIdentity
lhnNsmEvents=_LhnNsmEvents_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,0))
if mibBuilder.loadTexts:lhnNsmEvents.setStatus(_A)
_LhnNsmCommon_ObjectIdentity=ObjectIdentity
lhnNsmCommon=_LhnNsmCommon_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,1))
if mibBuilder.loadTexts:lhnNsmCommon.setStatus('obsolete')
_LhnNsmObjects_ObjectIdentity=ObjectIdentity
lhnNsmObjects=_LhnNsmObjects_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2))
if mibBuilder.loadTexts:lhnNsmObjects.setStatus(_A)
_LhnNsmInfo_ObjectIdentity=ObjectIdentity
lhnNsmInfo=_LhnNsmInfo_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,1))
if mibBuilder.loadTexts:lhnNsmInfo.setStatus(_A)
_LhnNsmNetwork_ObjectIdentity=ObjectIdentity
lhnNsmNetwork=_LhnNsmNetwork_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,2))
if mibBuilder.loadTexts:lhnNsmNetwork.setStatus(_A)
_LhnNsmDNS_ObjectIdentity=ObjectIdentity
lhnNsmDNS=_LhnNsmDNS_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,3))
if mibBuilder.loadTexts:lhnNsmDNS.setStatus(_A)
_LhnNsmStorage_ObjectIdentity=ObjectIdentity
lhnNsmStorage=_LhnNsmStorage_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,4))
if mibBuilder.loadTexts:lhnNsmStorage.setStatus(_A)
_LhnNsmNTP_ObjectIdentity=ObjectIdentity
lhnNsmNTP=_LhnNsmNTP_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,5))
if mibBuilder.loadTexts:lhnNsmNTP.setStatus(_A)
_LhnNsmSecurity_ObjectIdentity=ObjectIdentity
lhnNsmSecurity=_LhnNsmSecurity_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,11))
if mibBuilder.loadTexts:lhnNsmSecurity.setStatus(_A)
_LhnNsmClustering_ObjectIdentity=ObjectIdentity
lhnNsmClustering=_LhnNsmClustering_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,12))
if mibBuilder.loadTexts:lhnNsmClustering.setStatus(_A)
_LhnNsmOldNotification_ObjectIdentity=ObjectIdentity
lhnNsmOldNotification=_LhnNsmOldNotification_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,13))
if mibBuilder.loadTexts:lhnNsmOldNotification.setStatus(_A)
_LhnNsmNotification_ObjectIdentity=ObjectIdentity
lhnNsmNotification=_LhnNsmNotification_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,15))
if mibBuilder.loadTexts:lhnNsmNotification.setStatus(_A)
_LhnNsmStatus_ObjectIdentity=ObjectIdentity
lhnNsmStatus=_LhnNsmStatus_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,2,99))
if mibBuilder.loadTexts:lhnNsmStatus.setStatus(_A)
_LhnNsmOldEvents_ObjectIdentity=ObjectIdentity
lhnNsmOldEvents=_LhnNsmOldEvents_ObjectIdentity((1,3,6,1,4,1,9804,3,1,1,3))
if mibBuilder.loadTexts:lhnNsmOldEvents.setStatus(_A)
mibBuilder.exportSymbols('LEFTHAND-NETWORKS-NSM-MIB',**{'lhnNsmMib':lhnNsmMib,'lhnNsmDevices':lhnNsmDevices,'lhnNsmEvents':lhnNsmEvents,'lhnNsmCommon':lhnNsmCommon,'lhnNsmObjects':lhnNsmObjects,'lhnNsmInfo':lhnNsmInfo,'lhnNsmNetwork':lhnNsmNetwork,'lhnNsmDNS':lhnNsmDNS,'lhnNsmStorage':lhnNsmStorage,'lhnNsmNTP':lhnNsmNTP,'lhnNsmSecurity':lhnNsmSecurity,'lhnNsmClustering':lhnNsmClustering,'lhnNsmOldNotification':lhnNsmOldNotification,'lhnNsmNotification':lhnNsmNotification,'lhnNsmStatus':lhnNsmStatus,'lhnNsmOldEvents':lhnNsmOldEvents})