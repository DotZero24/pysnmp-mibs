_h='tkAlarmNotifyGroup'
_g='tkAlarmTableGroup'
_f='powerChainAlarmUpdated'
_e='powerChainAlarmClosed'
_d='powerChainAlarmCleared'
_c='powerChainAlarmAcknowledged'
_b='powerChainCautionaryAlarm'
_a='powerChainCriticalAlarm'
_Z='powerChainAlarmEventClosed'
_Y='powerChainEvent'
_X='powerChainEventCleared'
_W='powerChainAlarmEventAcknowledged'
_V='powerChainCautionaryAlarmEvent'
_U='powerChainCriticalAlarmEvent'
_T='numAlarmsPresent'
_S='alarmTime'
_R='tkEventNotifyGroup'
_Q='tkEventGroup'
_P='alarmLevel'
_O='accessible-for-notify'
_N='read-only'
_M='Integer32'
_L='alarmValue'
_K='alarmDescription'
_J='alarmSequenceIndex'
_I='eventValue'
_H='eventDescription'
_G='eventSequenceIndex'
_F='eventID'
_E='alarmID'
_D='entPhysicalName'
_C='ENTITY-MIB'
_B='current'
_A='EATON-PXG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
powerChain,=mibBuilder.importSymbols('EATON-OIDS','powerChain')
entPhysicalName,=mibBuilder.importSymbols(_C,_D)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
pxgMIB=ModuleIdentity((1,3,6,1,4,1,534,8,1))
if mibBuilder.loadTexts:pxgMIB.setRevisions(('2008-01-30 00:00','2007-07-05 00:00','2007-04-10 00:00','2007-01-03 00:00','2006-10-13 00:00'))
_PxgNotifications_ObjectIdentity=ObjectIdentity
pxgNotifications=_PxgNotifications_ObjectIdentity((1,3,6,1,4,1,534,8,1,0))
_PxgMIBObjects_ObjectIdentity=ObjectIdentity
pxgMIBObjects=_PxgMIBObjects_ObjectIdentity((1,3,6,1,4,1,534,8,1,1))
_EventInfo_ObjectIdentity=ObjectIdentity
eventInfo=_EventInfo_ObjectIdentity((1,3,6,1,4,1,534,8,1,1,1))
class _EventID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EventID_Type.__name__=_M
_EventID_Object=MibScalar
eventID=_EventID_Object((1,3,6,1,4,1,534,8,1,1,1,1),_EventID_Type())
eventID.setMaxAccess(_O)
if mibBuilder.loadTexts:eventID.setStatus(_B)
class _EventSequenceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EventSequenceIndex_Type.__name__=_M
_EventSequenceIndex_Object=MibScalar
eventSequenceIndex=_EventSequenceIndex_Object((1,3,6,1,4,1,534,8,1,1,1,2),_EventSequenceIndex_Type())
eventSequenceIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:eventSequenceIndex.setStatus(_B)
_EventDescription_Type=SnmpAdminString
_EventDescription_Object=MibScalar
eventDescription=_EventDescription_Object((1,3,6,1,4,1,534,8,1,1,1,3),_EventDescription_Type())
eventDescription.setMaxAccess(_O)
if mibBuilder.loadTexts:eventDescription.setStatus(_B)
_EventValue_Type=SnmpAdminString
_EventValue_Object=MibScalar
eventValue=_EventValue_Object((1,3,6,1,4,1,534,8,1,1,1,4),_EventValue_Type())
eventValue.setMaxAccess(_O)
if mibBuilder.loadTexts:eventValue.setStatus(_B)
_Alarms_ObjectIdentity=ObjectIdentity
alarms=_Alarms_ObjectIdentity((1,3,6,1,4,1,534,8,1,1,2))
_NumAlarmsPresent_Type=Gauge32
_NumAlarmsPresent_Object=MibScalar
numAlarmsPresent=_NumAlarmsPresent_Object((1,3,6,1,4,1,534,8,1,1,2,1),_NumAlarmsPresent_Type())
numAlarmsPresent.setMaxAccess(_N)
if mibBuilder.loadTexts:numAlarmsPresent.setStatus(_B)
_ActiveAlarmsTable_Object=MibTable
activeAlarmsTable=_ActiveAlarmsTable_Object((1,3,6,1,4,1,534,8,1,1,2,2))
if mibBuilder.loadTexts:activeAlarmsTable.setStatus(_B)
_ActiveAlarmsEntry_Object=MibTableRow
activeAlarmsEntry=_ActiveAlarmsEntry_Object((1,3,6,1,4,1,534,8,1,1,2,2,1))
activeAlarmsEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:activeAlarmsEntry.setStatus(_B)
class _AlarmID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlarmID_Type.__name__=_M
_AlarmID_Object=MibTableColumn
alarmID=_AlarmID_Object((1,3,6,1,4,1,534,8,1,1,2,2,1,1),_AlarmID_Type())
alarmID.setMaxAccess(_O)
if mibBuilder.loadTexts:alarmID.setStatus(_B)
class _AlarmSequenceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlarmSequenceIndex_Type.__name__=_M
_AlarmSequenceIndex_Object=MibTableColumn
alarmSequenceIndex=_AlarmSequenceIndex_Object((1,3,6,1,4,1,534,8,1,1,2,2,1,2),_AlarmSequenceIndex_Type())
alarmSequenceIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:alarmSequenceIndex.setStatus(_B)
_AlarmDescription_Type=SnmpAdminString
_AlarmDescription_Object=MibTableColumn
alarmDescription=_AlarmDescription_Object((1,3,6,1,4,1,534,8,1,1,2,2,1,3),_AlarmDescription_Type())
alarmDescription.setMaxAccess(_N)
if mibBuilder.loadTexts:alarmDescription.setStatus(_B)
_AlarmValue_Type=SnmpAdminString
_AlarmValue_Object=MibTableColumn
alarmValue=_AlarmValue_Object((1,3,6,1,4,1,534,8,1,1,2,2,1,4),_AlarmValue_Type())
alarmValue.setMaxAccess(_N)
if mibBuilder.loadTexts:alarmValue.setStatus(_B)
class _AlarmLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('critical',1),('cautionary',2),('acknowledged',3),('active',4),('cleared',5),('closed',6),('unknown',7)))
_AlarmLevel_Type.__name__=_M
_AlarmLevel_Object=MibTableColumn
alarmLevel=_AlarmLevel_Object((1,3,6,1,4,1,534,8,1,1,2,2,1,5),_AlarmLevel_Type())
alarmLevel.setMaxAccess(_N)
if mibBuilder.loadTexts:alarmLevel.setStatus(_B)
_AlarmTime_Type=TimeStamp
_AlarmTime_Object=MibTableColumn
alarmTime=_AlarmTime_Object((1,3,6,1,4,1,534,8,1,1,2,2,1,6),_AlarmTime_Type())
alarmTime.setMaxAccess(_N)
if mibBuilder.loadTexts:alarmTime.setStatus(_B)
_PxgConformance_ObjectIdentity=ObjectIdentity
pxgConformance=_PxgConformance_ObjectIdentity((1,3,6,1,4,1,534,8,1,2))
tkEventGroup=ObjectGroup((1,3,6,1,4,1,534,8,1,2,1))
tkEventGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:tkEventGroup.setStatus(_B)
tkAlarmTableGroup=ObjectGroup((1,3,6,1,4,1,534,8,1,2,2))
tkAlarmTableGroup.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_P),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:tkAlarmTableGroup.setStatus(_B)
powerChainCriticalAlarmEvent=NotificationType((1,3,6,1,4,1,534,8,1,0,1))
powerChainCriticalAlarmEvent.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_C,_D)))
if mibBuilder.loadTexts:powerChainCriticalAlarmEvent.setStatus(_B)
powerChainCautionaryAlarmEvent=NotificationType((1,3,6,1,4,1,534,8,1,0,2))
powerChainCautionaryAlarmEvent.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_C,_D)))
if mibBuilder.loadTexts:powerChainCautionaryAlarmEvent.setStatus(_B)
powerChainAlarmEventAcknowledged=NotificationType((1,3,6,1,4,1,534,8,1,0,3))
powerChainAlarmEventAcknowledged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_C,_D)))
if mibBuilder.loadTexts:powerChainAlarmEventAcknowledged.setStatus(_B)
powerChainEventCleared=NotificationType((1,3,6,1,4,1,534,8,1,0,4))
powerChainEventCleared.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_C,_D)))
if mibBuilder.loadTexts:powerChainEventCleared.setStatus(_B)
powerChainEvent=NotificationType((1,3,6,1,4,1,534,8,1,0,5))
powerChainEvent.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_C,_D)))
if mibBuilder.loadTexts:powerChainEvent.setStatus(_B)
powerChainAlarmEventClosed=NotificationType((1,3,6,1,4,1,534,8,1,0,6))
powerChainAlarmEventClosed.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_C,_D)))
if mibBuilder.loadTexts:powerChainAlarmEventClosed.setStatus(_B)
powerChainCriticalAlarm=NotificationType((1,3,6,1,4,1,534,8,1,0,7))
powerChainCriticalAlarm.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_C,_D)))
if mibBuilder.loadTexts:powerChainCriticalAlarm.setStatus(_B)
powerChainCautionaryAlarm=NotificationType((1,3,6,1,4,1,534,8,1,0,8))
powerChainCautionaryAlarm.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_C,_D)))
if mibBuilder.loadTexts:powerChainCautionaryAlarm.setStatus(_B)
powerChainAlarmAcknowledged=NotificationType((1,3,6,1,4,1,534,8,1,0,9))
powerChainAlarmAcknowledged.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_C,_D)))
if mibBuilder.loadTexts:powerChainAlarmAcknowledged.setStatus(_B)
powerChainAlarmCleared=NotificationType((1,3,6,1,4,1,534,8,1,0,10))
powerChainAlarmCleared.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_C,_D)))
if mibBuilder.loadTexts:powerChainAlarmCleared.setStatus(_B)
powerChainAlarmClosed=NotificationType((1,3,6,1,4,1,534,8,1,0,11))
powerChainAlarmClosed.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_C,_D)))
if mibBuilder.loadTexts:powerChainAlarmClosed.setStatus(_B)
powerChainAlarmUpdated=NotificationType((1,3,6,1,4,1,534,8,1,0,12))
powerChainAlarmUpdated.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_P),(_C,_D)))
if mibBuilder.loadTexts:powerChainAlarmUpdated.setStatus(_B)
tkEventNotifyGroup=NotificationGroup((1,3,6,1,4,1,534,8,1,2,3))
tkEventNotifyGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:tkEventNotifyGroup.setStatus(_B)
tkAlarmNotifyGroup=NotificationGroup((1,3,6,1,4,1,534,8,1,2,4))
tkAlarmNotifyGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:tkAlarmNotifyGroup.setStatus(_B)
tkSimpleCompliance=ModuleCompliance((1,3,6,1,4,1,534,8,1,2,5))
tkSimpleCompliance.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:tkSimpleCompliance.setStatus(_B)
tkAlarmsTableCompliance=ModuleCompliance((1,3,6,1,4,1,534,8,1,2,6))
tkAlarmsTableCompliance.setObjects(*((_A,_Q),(_A,_g),(_A,_R),(_A,_h)))
if mibBuilder.loadTexts:tkAlarmsTableCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'pxgMIB':pxgMIB,'pxgNotifications':pxgNotifications,_U:powerChainCriticalAlarmEvent,_V:powerChainCautionaryAlarmEvent,_W:powerChainAlarmEventAcknowledged,_X:powerChainEventCleared,_Y:powerChainEvent,_Z:powerChainAlarmEventClosed,_a:powerChainCriticalAlarm,_b:powerChainCautionaryAlarm,_c:powerChainAlarmAcknowledged,_d:powerChainAlarmCleared,_e:powerChainAlarmClosed,_f:powerChainAlarmUpdated,'pxgMIBObjects':pxgMIBObjects,'eventInfo':eventInfo,_F:eventID,_G:eventSequenceIndex,_H:eventDescription,_I:eventValue,'alarms':alarms,_T:numAlarmsPresent,'activeAlarmsTable':activeAlarmsTable,'activeAlarmsEntry':activeAlarmsEntry,_E:alarmID,_J:alarmSequenceIndex,_K:alarmDescription,_L:alarmValue,_P:alarmLevel,_S:alarmTime,'pxgConformance':pxgConformance,_Q:tkEventGroup,_g:tkAlarmTableGroup,_R:tkEventNotifyGroup,_h:tkAlarmNotifyGroup,'tkSimpleCompliance':tkSimpleCompliance,'tkAlarmsTableCompliance':tkAlarmsTableCompliance})