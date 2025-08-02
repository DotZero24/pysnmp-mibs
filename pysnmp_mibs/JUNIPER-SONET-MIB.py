_J='Integer32'
_I='ifIndex'
_H='jnxSonetLastAlarmDate'
_G='jnxSonetCurrentAlarms'
_F='jnxSonetLastAlarmId'
_E='ifDescr'
_D='IF-MIB'
_C='read-only'
_B='JUNIPER-SONET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_E,_I)
jnxMibs,jnxSonetNotifications=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs','jnxSonetNotifications')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
jnxSonet=ModuleIdentity((1,3,6,1,4,1,2636,3,20))
if mibBuilder.loadTexts:jnxSonet.setRevisions(('2002-12-12 00:00','2002-08-08 00:00'))
class JnxSonetAlarmId(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('sonetLolAlarm',0),('sonetPllAlarm',1),('sonetLofAlarm',2),('sonetLosAlarm',3),('sonetSefAlarm',4),('sonetLaisAlarm',5),('sonetPaisAlarm',6),('sonetLopAlarm',7),('sonetBerrSdAlarm',8),('sonetBerrSfAlarm',9),('sonetLrdiAlarm',10),('sonetPrdiAlarm',11),('sonetReiAlarm',12),('sonetUneqAlarm',13),('sonetPmisAlarm',14),('sonetLocAlarm',15),('sonetVaisAlarm',16),('sonetVlopAlarm',17),('sonetVrdiAlarm',18),('sonetVuneqAlarm',19),('sonetVmisAlarm',20),('sonetVlocAlarm',21),('sdhLolAlarm',22),('sdhPllAlarm',23),('sdhLofAlarm',24),('sdhLosAlarm',25),('sdhOofAlarm',26),('sdhMsAisAlarm',27),('sdhHpAisAlarm',28),('sdhLopAlarm',29),('sdhBerrSdAlarm',30),('sdhBerrSfAlarm',31),('sdhMsFerfAlarm',32),('sdhHpFerfAlarm',33),('sdhMsFebeAlarm',34),('sdhHpUneqAlarm',35),('sdhHpMisAlarm',36),('sdhLocAlarm',37)))
_JnxSonetAlarms_ObjectIdentity=ObjectIdentity
jnxSonetAlarms=_JnxSonetAlarms_ObjectIdentity((1,3,6,1,4,1,2636,3,20,1))
_JnxSonetAlarmTable_Object=MibTable
jnxSonetAlarmTable=_JnxSonetAlarmTable_Object((1,3,6,1,4,1,2636,3,20,1,1))
if mibBuilder.loadTexts:jnxSonetAlarmTable.setStatus(_A)
_JnxSonetAlarmEntry_Object=MibTableRow
jnxSonetAlarmEntry=_JnxSonetAlarmEntry_Object((1,3,6,1,4,1,2636,3,20,1,1,1))
jnxSonetAlarmEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:jnxSonetAlarmEntry.setStatus(_A)
_JnxSonetCurrentAlarms_Type=JnxSonetAlarmId
_JnxSonetCurrentAlarms_Object=MibTableColumn
jnxSonetCurrentAlarms=_JnxSonetCurrentAlarms_Object((1,3,6,1,4,1,2636,3,20,1,1,1,1),_JnxSonetCurrentAlarms_Type())
jnxSonetCurrentAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSonetCurrentAlarms.setStatus(_A)
_JnxSonetLastAlarmId_Type=JnxSonetAlarmId
_JnxSonetLastAlarmId_Object=MibTableColumn
jnxSonetLastAlarmId=_JnxSonetLastAlarmId_Object((1,3,6,1,4,1,2636,3,20,1,1,1,2),_JnxSonetLastAlarmId_Type())
jnxSonetLastAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSonetLastAlarmId.setStatus(_A)
_JnxSonetLastAlarmTime_Type=TimeTicks
_JnxSonetLastAlarmTime_Object=MibTableColumn
jnxSonetLastAlarmTime=_JnxSonetLastAlarmTime_Object((1,3,6,1,4,1,2636,3,20,1,1,1,3),_JnxSonetLastAlarmTime_Type())
jnxSonetLastAlarmTime.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSonetLastAlarmTime.setStatus(_A)
_JnxSonetLastAlarmDate_Type=DateAndTime
_JnxSonetLastAlarmDate_Object=MibTableColumn
jnxSonetLastAlarmDate=_JnxSonetLastAlarmDate_Object((1,3,6,1,4,1,2636,3,20,1,1,1,4),_JnxSonetLastAlarmDate_Type())
jnxSonetLastAlarmDate.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSonetLastAlarmDate.setStatus(_A)
class _JnxSonetLastAlarmEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('set',2),('cleared',3)))
_JnxSonetLastAlarmEvent_Type.__name__=_J
_JnxSonetLastAlarmEvent_Object=MibTableColumn
jnxSonetLastAlarmEvent=_JnxSonetLastAlarmEvent_Object((1,3,6,1,4,1,2636,3,20,1,1,1,5),_JnxSonetLastAlarmEvent_Type())
jnxSonetLastAlarmEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:jnxSonetLastAlarmEvent.setStatus(_A)
_JnxSonetNotificationPrefix_ObjectIdentity=ObjectIdentity
jnxSonetNotificationPrefix=_JnxSonetNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2636,4,6,0))
jnxSonetAlarmSet=NotificationType((1,3,6,1,4,1,2636,4,6,0,1))
jnxSonetAlarmSet.setObjects(*((_D,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:jnxSonetAlarmSet.setStatus(_A)
jnxSonetAlarmCleared=NotificationType((1,3,6,1,4,1,2636,4,6,0,2))
jnxSonetAlarmCleared.setObjects(*((_D,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:jnxSonetAlarmCleared.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JnxSonetAlarmId':JnxSonetAlarmId,'jnxSonet':jnxSonet,'jnxSonetAlarms':jnxSonetAlarms,'jnxSonetAlarmTable':jnxSonetAlarmTable,'jnxSonetAlarmEntry':jnxSonetAlarmEntry,_G:jnxSonetCurrentAlarms,_F:jnxSonetLastAlarmId,'jnxSonetLastAlarmTime':jnxSonetLastAlarmTime,_H:jnxSonetLastAlarmDate,'jnxSonetLastAlarmEvent':jnxSonetLastAlarmEvent,'jnxSonetNotificationPrefix':jnxSonetNotificationPrefix,'jnxSonetAlarmSet':jnxSonetAlarmSet,'jnxSonetAlarmCleared':jnxSonetAlarmCleared})