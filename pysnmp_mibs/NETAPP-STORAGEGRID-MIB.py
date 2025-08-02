_c='activeCriticalAlert'
_b='activeMajorAlert'
_a='activeMinorAlert'
_Z='currentCriticalAlarm'
_Y='currentMajorAlarm'
_X='currentMinorAlarm'
_W='currentNoticeAlarm'
_V='currentNormalAlarm'
_U='activeAlertCount'
_T='currentAlarmCount'
_S='DisplayString'
_R='Integer32'
_Q='OctetString'
_P='activeAlertStartTime'
_O='activeAlertSeverity'
_N='activeAlertInstance'
_M='activeAlertName'
_L='activeAlertId'
_K='currentAlarmTriggerValue'
_J='currentAlarmTriggerTime'
_I='currentAlarmSeverity'
_H='currentAlarmNodeName'
_G='currentAlarmAttrIndex'
_F='currentAlarmAttrCode'
_E='currentAlarmSourceId'
_D='current'
_C='read-only'
_B='deprecated'
_A='NETAPP-STORAGEGRID-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_S,'PhysAddress','TextualConvention')
storagegrid=ModuleIdentity((1,3,6,1,4,1,789,28669))
if mibBuilder.loadTexts:storagegrid.setRevisions(('2020-09-09 15:00','2018-03-21 17:25'))
class AlarmSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('notice',2),('minor',3),('major',4),('critical',5)))
_Netapp_ObjectIdentity=ObjectIdentity
netapp=_Netapp_ObjectIdentity((1,3,6,1,4,1,789))
_SgNotifications_ObjectIdentity=ObjectIdentity
sgNotifications=_SgNotifications_ObjectIdentity((1,3,6,1,4,1,789,28669,0))
_SgObjects_ObjectIdentity=ObjectIdentity
sgObjects=_SgObjects_ObjectIdentity((1,3,6,1,4,1,789,28669,1))
_CurrentAlarmTable_Object=MibTable
currentAlarmTable=_CurrentAlarmTable_Object((1,3,6,1,4,1,789,28669,1,1))
if mibBuilder.loadTexts:currentAlarmTable.setStatus(_B)
_CurrentAlarmEntry_Object=MibTableRow
currentAlarmEntry=_CurrentAlarmEntry_Object((1,3,6,1,4,1,789,28669,1,1,1))
currentAlarmEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:currentAlarmEntry.setStatus(_B)
class _CurrentAlarmSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CurrentAlarmSourceId_Type.__name__=_Q
_CurrentAlarmSourceId_Object=MibTableColumn
currentAlarmSourceId=_CurrentAlarmSourceId_Object((1,3,6,1,4,1,789,28669,1,1,1,1),_CurrentAlarmSourceId_Type())
currentAlarmSourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmSourceId.setStatus(_B)
class _CurrentAlarmAttrCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CurrentAlarmAttrCode_Type.__name__=_S
_CurrentAlarmAttrCode_Object=MibTableColumn
currentAlarmAttrCode=_CurrentAlarmAttrCode_Object((1,3,6,1,4,1,789,28669,1,1,1,2),_CurrentAlarmAttrCode_Type())
currentAlarmAttrCode.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmAttrCode.setStatus(_B)
class _CurrentAlarmAttrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CurrentAlarmAttrIndex_Type.__name__=_R
_CurrentAlarmAttrIndex_Object=MibTableColumn
currentAlarmAttrIndex=_CurrentAlarmAttrIndex_Object((1,3,6,1,4,1,789,28669,1,1,1,3),_CurrentAlarmAttrIndex_Type())
currentAlarmAttrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmAttrIndex.setStatus(_B)
class _CurrentAlarmNodeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CurrentAlarmNodeName_Type.__name__=_Q
_CurrentAlarmNodeName_Object=MibTableColumn
currentAlarmNodeName=_CurrentAlarmNodeName_Object((1,3,6,1,4,1,789,28669,1,1,1,4),_CurrentAlarmNodeName_Type())
currentAlarmNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmNodeName.setStatus(_B)
_CurrentAlarmSeverity_Type=AlarmSeverity
_CurrentAlarmSeverity_Object=MibTableColumn
currentAlarmSeverity=_CurrentAlarmSeverity_Object((1,3,6,1,4,1,789,28669,1,1,1,5),_CurrentAlarmSeverity_Type())
currentAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmSeverity.setStatus(_B)
_CurrentAlarmTriggerValue_Type=DisplayString
_CurrentAlarmTriggerValue_Object=MibTableColumn
currentAlarmTriggerValue=_CurrentAlarmTriggerValue_Object((1,3,6,1,4,1,789,28669,1,1,1,6),_CurrentAlarmTriggerValue_Type())
currentAlarmTriggerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmTriggerValue.setStatus(_B)
_CurrentAlarmTriggerTime_Type=DateAndTime
_CurrentAlarmTriggerTime_Object=MibTableColumn
currentAlarmTriggerTime=_CurrentAlarmTriggerTime_Object((1,3,6,1,4,1,789,28669,1,1,1,7),_CurrentAlarmTriggerTime_Type())
currentAlarmTriggerTime.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmTriggerTime.setStatus(_B)
_CurrentAlarmCount_Type=Integer32
_CurrentAlarmCount_Object=MibScalar
currentAlarmCount=_CurrentAlarmCount_Object((1,3,6,1,4,1,789,28669,1,2),_CurrentAlarmCount_Type())
currentAlarmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:currentAlarmCount.setStatus(_B)
_ActiveAlertCount_Type=Integer32
_ActiveAlertCount_Object=MibScalar
activeAlertCount=_ActiveAlertCount_Object((1,3,6,1,4,1,789,28669,1,3),_ActiveAlertCount_Type())
activeAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlertCount.setStatus(_D)
_ActiveAlertTable_Object=MibTable
activeAlertTable=_ActiveAlertTable_Object((1,3,6,1,4,1,789,28669,1,4))
if mibBuilder.loadTexts:activeAlertTable.setStatus(_D)
_ActiveAlertEntry_Object=MibTableRow
activeAlertEntry=_ActiveAlertEntry_Object((1,3,6,1,4,1,789,28669,1,4,1))
activeAlertEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:activeAlertEntry.setStatus(_D)
class _ActiveAlertId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ActiveAlertId_Type.__name__=_Q
_ActiveAlertId_Object=MibTableColumn
activeAlertId=_ActiveAlertId_Object((1,3,6,1,4,1,789,28669,1,4,1,1),_ActiveAlertId_Type())
activeAlertId.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlertId.setStatus(_D)
_ActiveAlertName_Type=OctetString
_ActiveAlertName_Object=MibTableColumn
activeAlertName=_ActiveAlertName_Object((1,3,6,1,4,1,789,28669,1,4,1,2),_ActiveAlertName_Type())
activeAlertName.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlertName.setStatus(_D)
_ActiveAlertInstance_Type=OctetString
_ActiveAlertInstance_Object=MibTableColumn
activeAlertInstance=_ActiveAlertInstance_Object((1,3,6,1,4,1,789,28669,1,4,1,3),_ActiveAlertInstance_Type())
activeAlertInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlertInstance.setStatus(_D)
_ActiveAlertSeverity_Type=OctetString
_ActiveAlertSeverity_Object=MibTableColumn
activeAlertSeverity=_ActiveAlertSeverity_Object((1,3,6,1,4,1,789,28669,1,4,1,4),_ActiveAlertSeverity_Type())
activeAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlertSeverity.setStatus(_D)
_ActiveAlertStartTime_Type=DateAndTime
_ActiveAlertStartTime_Object=MibTableColumn
activeAlertStartTime=_ActiveAlertStartTime_Object((1,3,6,1,4,1,789,28669,1,4,1,5),_ActiveAlertStartTime_Type())
activeAlertStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlertStartTime.setStatus(_D)
_SgGroups_ObjectIdentity=ObjectIdentity
sgGroups=_SgGroups_ObjectIdentity((1,3,6,1,4,1,789,28669,2))
currentAlarmGroup=ObjectGroup((1,3,6,1,4,1,789,28669,2,1))
currentAlarmGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_T)))
if mibBuilder.loadTexts:currentAlarmGroup.setStatus(_B)
activeAlertGroup=ObjectGroup((1,3,6,1,4,1,789,28669,2,3))
activeAlertGroup.setObjects(*((_A,_U),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:activeAlertGroup.setStatus(_D)
currentNormalAlarm=NotificationType((1,3,6,1,4,1,789,28669,0,1))
currentNormalAlarm.setObjects(*((_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:currentNormalAlarm.setStatus(_B)
currentNoticeAlarm=NotificationType((1,3,6,1,4,1,789,28669,0,2))
currentNoticeAlarm.setObjects(*((_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:currentNoticeAlarm.setStatus(_B)
currentMinorAlarm=NotificationType((1,3,6,1,4,1,789,28669,0,3))
currentMinorAlarm.setObjects(*((_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:currentMinorAlarm.setStatus(_B)
currentMajorAlarm=NotificationType((1,3,6,1,4,1,789,28669,0,4))
currentMajorAlarm.setObjects(*((_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:currentMajorAlarm.setStatus(_B)
currentCriticalAlarm=NotificationType((1,3,6,1,4,1,789,28669,0,5))
currentCriticalAlarm.setObjects(*((_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_K),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:currentCriticalAlarm.setStatus(_B)
activeMinorAlert=NotificationType((1,3,6,1,4,1,789,28669,0,6))
activeMinorAlert.setObjects(*((_A,_P),(_A,_N),(_A,_L),(_A,_O),(_A,_M)))
if mibBuilder.loadTexts:activeMinorAlert.setStatus(_D)
activeMajorAlert=NotificationType((1,3,6,1,4,1,789,28669,0,7))
activeMajorAlert.setObjects(*((_A,_P),(_A,_N),(_A,_L),(_A,_O),(_A,_M)))
if mibBuilder.loadTexts:activeMajorAlert.setStatus(_D)
activeCriticalAlert=NotificationType((1,3,6,1,4,1,789,28669,0,8))
activeCriticalAlert.setObjects(*((_A,_P),(_A,_N),(_A,_L),(_A,_O),(_A,_M)))
if mibBuilder.loadTexts:activeCriticalAlert.setStatus(_D)
currentAlarmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,789,28669,2,2))
currentAlarmNotificationsGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:currentAlarmNotificationsGroup.setStatus(_B)
activeAlertNotificationsGroup=NotificationGroup((1,3,6,1,4,1,789,28669,2,4))
activeAlertNotificationsGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:activeAlertNotificationsGroup.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'AlarmSeverity':AlarmSeverity,'netapp':netapp,'storagegrid':storagegrid,'sgNotifications':sgNotifications,_V:currentNormalAlarm,_W:currentNoticeAlarm,_X:currentMinorAlarm,_Y:currentMajorAlarm,_Z:currentCriticalAlarm,_a:activeMinorAlert,_b:activeMajorAlert,_c:activeCriticalAlert,'sgObjects':sgObjects,'currentAlarmTable':currentAlarmTable,'currentAlarmEntry':currentAlarmEntry,_E:currentAlarmSourceId,_F:currentAlarmAttrCode,_G:currentAlarmAttrIndex,_H:currentAlarmNodeName,_I:currentAlarmSeverity,_K:currentAlarmTriggerValue,_J:currentAlarmTriggerTime,_T:currentAlarmCount,_U:activeAlertCount,'activeAlertTable':activeAlertTable,'activeAlertEntry':activeAlertEntry,_L:activeAlertId,_M:activeAlertName,_N:activeAlertInstance,_O:activeAlertSeverity,_P:activeAlertStartTime,'sgGroups':sgGroups,'currentAlarmGroup':currentAlarmGroup,'currentAlarmNotificationsGroup':currentAlarmNotificationsGroup,'activeAlertGroup':activeAlertGroup,'activeAlertNotificationsGroup':activeAlertNotificationsGroup})