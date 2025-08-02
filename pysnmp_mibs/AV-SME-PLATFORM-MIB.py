_W='smepGenAppNotificationsGroup'
_V='smepGenEntGenNotificationsGroup'
_U='smepGenNotificationObjectsGroup'
_T='smepGenAppEvent'
_S='smepGenAuthFailureEvent'
_R='smepGenLinkUpEvent'
_Q='smepGenLinkDownEvent'
_P='smepGenWarmStartEvent'
_O='smepGenColdStartEvent'
_N='SnmpAdminString'
_M='smepGTEventAppEvent'
_L='smepGTEventAppEntity'
_K='Integer32'
_J='ifIndex'
_I='IF-MIB'
_H='accessible-for-notify'
_G='sysDescr'
_F='SNMPv2-MIB'
_E='smepGTEventDateTime'
_D='smepGTEventDevID'
_C='smepGTEventStdSeverity'
_B='current'
_A='AV-SME-PLATFORM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mibs,=mibBuilder.importSymbols('AVAYAGEN-MIB','mibs')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysDescr,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
avSMEPlatformMIB=ModuleIdentity((1,3,6,1,4,1,6889,2,48))
if mibBuilder.loadTexts:avSMEPlatformMIB.setRevisions(('2013-01-11 14:05','2010-07-06 13:47','2010-07-02 14:37'))
_SmepGeneric_ObjectIdentity=ObjectIdentity
smepGeneric=_SmepGeneric_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1))
_SmepGenMibs_ObjectIdentity=ObjectIdentity
smepGenMibs=_SmepGenMibs_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,1))
_SmepGenTraps_ObjectIdentity=ObjectIdentity
smepGenTraps=_SmepGenTraps_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,2))
_SmepGTEvents_ObjectIdentity=ObjectIdentity
smepGTEvents=_SmepGTEvents_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,2,0))
_SmepGTObjects_ObjectIdentity=ObjectIdentity
smepGTObjects=_SmepGTObjects_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,2,1))
_SmepGTEventStdSeverity_Type=ItuPerceivedSeverity
_SmepGTEventStdSeverity_Object=MibScalar
smepGTEventStdSeverity=_SmepGTEventStdSeverity_Object((1,3,6,1,4,1,6889,2,48,1,2,1,1),_SmepGTEventStdSeverity_Type())
smepGTEventStdSeverity.setMaxAccess(_H)
if mibBuilder.loadTexts:smepGTEventStdSeverity.setStatus(_B)
_SmepGTEventDateTime_Type=DateAndTime
_SmepGTEventDateTime_Object=MibScalar
smepGTEventDateTime=_SmepGTEventDateTime_Object((1,3,6,1,4,1,6889,2,48,1,2,1,2),_SmepGTEventDateTime_Type())
smepGTEventDateTime.setMaxAccess(_H)
if mibBuilder.loadTexts:smepGTEventDateTime.setStatus(_B)
class _SmepGTEventDevID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_SmepGTEventDevID_Type.__name__=_N
_SmepGTEventDevID_Object=MibScalar
smepGTEventDevID=_SmepGTEventDevID_Object((1,3,6,1,4,1,6889,2,48,1,2,1,3),_SmepGTEventDevID_Type())
smepGTEventDevID.setMaxAccess(_H)
if mibBuilder.loadTexts:smepGTEventDevID.setStatus(_B)
class _SmepGTEventAppEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('voiceMailPro',1),('onex',2),('ipOffice',3),('jade',4),('webmanagement',5)))
_SmepGTEventAppEntity_Type.__name__=_K
_SmepGTEventAppEntity_Object=MibScalar
smepGTEventAppEntity=_SmepGTEventAppEntity_Object((1,3,6,1,4,1,6889,2,48,1,2,1,4),_SmepGTEventAppEntity_Type())
smepGTEventAppEntity.setMaxAccess(_H)
if mibBuilder.loadTexts:smepGTEventAppEntity.setStatus(_B)
class _SmepGTEventAppEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('crash',1))
_SmepGTEventAppEvent_Type.__name__=_K
_SmepGTEventAppEvent_Object=MibScalar
smepGTEventAppEvent=_SmepGTEventAppEvent_Object((1,3,6,1,4,1,6889,2,48,1,2,1,5),_SmepGTEventAppEvent_Type())
smepGTEventAppEvent.setMaxAccess(_H)
if mibBuilder.loadTexts:smepGTEventAppEvent.setStatus(_B)
_SmepGenConformance_ObjectIdentity=ObjectIdentity
smepGenConformance=_SmepGenConformance_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,3))
_SmepGenCompliances_ObjectIdentity=ObjectIdentity
smepGenCompliances=_SmepGenCompliances_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,3,1))
_SmepGenGroups_ObjectIdentity=ObjectIdentity
smepGenGroups=_SmepGenGroups_ObjectIdentity((1,3,6,1,4,1,6889,2,48,1,3,2))
smepGenNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6889,2,48,1,3,2,1))
smepGenNotificationObjectsGroup.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:smepGenNotificationObjectsGroup.setStatus(_B)
smepGenColdStartEvent=NotificationType((1,3,6,1,4,1,6889,2,48,1,2,0,1))
smepGenColdStartEvent.setObjects(*((_A,_C),(_A,_E),(_A,_D),(_F,_G)))
if mibBuilder.loadTexts:smepGenColdStartEvent.setStatus(_B)
smepGenWarmStartEvent=NotificationType((1,3,6,1,4,1,6889,2,48,1,2,0,2))
smepGenWarmStartEvent.setObjects(*((_A,_C),(_A,_E),(_A,_D),(_F,_G)))
if mibBuilder.loadTexts:smepGenWarmStartEvent.setStatus(_B)
smepGenLinkDownEvent=NotificationType((1,3,6,1,4,1,6889,2,48,1,2,0,3))
smepGenLinkDownEvent.setObjects(*((_A,_C),(_A,_E),(_A,_D),(_F,_G),(_I,_J)))
if mibBuilder.loadTexts:smepGenLinkDownEvent.setStatus(_B)
smepGenLinkUpEvent=NotificationType((1,3,6,1,4,1,6889,2,48,1,2,0,4))
smepGenLinkUpEvent.setObjects(*((_A,_C),(_A,_E),(_A,_D),(_F,_G),(_I,_J)))
if mibBuilder.loadTexts:smepGenLinkUpEvent.setStatus(_B)
smepGenAuthFailureEvent=NotificationType((1,3,6,1,4,1,6889,2,48,1,2,0,5))
smepGenAuthFailureEvent.setObjects(*((_A,_C),(_A,_E),(_A,_D),(_F,_G)))
if mibBuilder.loadTexts:smepGenAuthFailureEvent.setStatus(_B)
smepGenAppEvent=NotificationType((1,3,6,1,4,1,6889,2,48,1,2,0,6))
smepGenAppEvent.setObjects(*((_A,_C),(_A,_E),(_A,_D),(_F,_G),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:smepGenAppEvent.setStatus(_B)
smepGenEntGenNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,48,1,3,2,2))
smepGenEntGenNotificationsGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:smepGenEntGenNotificationsGroup.setStatus(_B)
smepGenAppNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6889,2,48,1,3,2,3))
smepGenAppNotificationsGroup.setObjects((_A,_T))
if mibBuilder.loadTexts:smepGenAppNotificationsGroup.setStatus(_B)
smepGenCompliance=ModuleCompliance((1,3,6,1,4,1,6889,2,48,1,3,1,1))
smepGenCompliance.setObjects(*((_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:smepGenCompliance.setStatus('deprecated')
mibBuilder.exportSymbols(_A,**{'avSMEPlatformMIB':avSMEPlatformMIB,'smepGeneric':smepGeneric,'smepGenMibs':smepGenMibs,'smepGenTraps':smepGenTraps,'smepGTEvents':smepGTEvents,_O:smepGenColdStartEvent,_P:smepGenWarmStartEvent,_Q:smepGenLinkDownEvent,_R:smepGenLinkUpEvent,_S:smepGenAuthFailureEvent,_T:smepGenAppEvent,'smepGTObjects':smepGTObjects,_C:smepGTEventStdSeverity,_E:smepGTEventDateTime,_D:smepGTEventDevID,_L:smepGTEventAppEntity,_M:smepGTEventAppEvent,'smepGenConformance':smepGenConformance,'smepGenCompliances':smepGenCompliances,'smepGenCompliance':smepGenCompliance,'smepGenGroups':smepGenGroups,_U:smepGenNotificationObjectsGroup,_V:smepGenEntGenNotificationsGroup,_W:smepGenAppNotificationsGroup})