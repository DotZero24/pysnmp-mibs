_Z='osSyslogNotificationsGroup'
_Y='osSyslogMandatoryGroup'
_X='osLogMsgAlarm'
_W='osLogLastSevUpTime'
_V='osLogLastSevMessage'
_U='osLogLastSevFacility'
_T='osLogMsgIgnored'
_S='osLogNotificationsSent'
_R='osLogDataClear'
_Q='osLogMaxSeverity'
_P='osLogNotificationsEnabled'
_O='osLogHistTableMaxLength'
_N='not-accessible'
_M='osLogHistIndex'
_L='SyslogSeverity'
_K='osLogHistUpTime'
_J='osLogHistMessage'
_I='osLogHistFacility'
_H='TruthValue'
_G='osLogHistSeverity'
_F='read-write'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='OS-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeStamp',_H)
osSyslog=ModuleIdentity((1,3,6,1,4,1,6926,2,32))
if mibBuilder.loadTexts:osSyslog.setRevisions(('2014-07-06 13:00',))
class SyslogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('info',7),('debug',8)))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaOptiSwitch_ObjectIdentity=ObjectIdentity
oaOptiSwitch=_OaOptiSwitch_ObjectIdentity((1,3,6,1,4,1,6926,2))
_OsSyslogNotifications_ObjectIdentity=ObjectIdentity
osSyslogNotifications=_OsSyslogNotifications_ObjectIdentity((1,3,6,1,4,1,6926,2,32,0))
_OsSyslogObjects_ObjectIdentity=ObjectIdentity
osSyslogObjects=_OsSyslogObjects_ObjectIdentity((1,3,6,1,4,1,6926,2,32,1))
_OsLogGen_ObjectIdentity=ObjectIdentity
osLogGen=_OsLogGen_ObjectIdentity((1,3,6,1,4,1,6926,2,32,1,1))
class _OsLogHistTableMaxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_OsLogHistTableMaxLength_Type.__name__=_E
_OsLogHistTableMaxLength_Object=MibScalar
osLogHistTableMaxLength=_OsLogHistTableMaxLength_Object((1,3,6,1,4,1,6926,2,32,1,1,1),_OsLogHistTableMaxLength_Type())
osLogHistTableMaxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:osLogHistTableMaxLength.setStatus(_A)
if mibBuilder.loadTexts:osLogHistTableMaxLength.setUnits('entries')
class _OsLogNotificationsEnabled_Type(TruthValue):defaultValue=2
_OsLogNotificationsEnabled_Type.__name__=_H
_OsLogNotificationsEnabled_Object=MibScalar
osLogNotificationsEnabled=_OsLogNotificationsEnabled_Object((1,3,6,1,4,1,6926,2,32,1,1,2),_OsLogNotificationsEnabled_Type())
osLogNotificationsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:osLogNotificationsEnabled.setStatus(_A)
class _OsLogMaxSeverity_Type(SyslogSeverity):defaultValue=7
_OsLogMaxSeverity_Type.__name__=_L
_OsLogMaxSeverity_Object=MibScalar
osLogMaxSeverity=_OsLogMaxSeverity_Object((1,3,6,1,4,1,6926,2,32,1,1,3),_OsLogMaxSeverity_Type())
osLogMaxSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:osLogMaxSeverity.setStatus(_A)
class _OsLogDataClear_Type(TruthValue):defaultValue=2
_OsLogDataClear_Type.__name__=_H
_OsLogDataClear_Object=MibScalar
osLogDataClear=_OsLogDataClear_Object((1,3,6,1,4,1,6926,2,32,1,1,4),_OsLogDataClear_Type())
osLogDataClear.setMaxAccess(_F)
if mibBuilder.loadTexts:osLogDataClear.setStatus(_A)
_OsLogNotificationsSent_Type=Counter32
_OsLogNotificationsSent_Object=MibScalar
osLogNotificationsSent=_OsLogNotificationsSent_Object((1,3,6,1,4,1,6926,2,32,1,1,7),_OsLogNotificationsSent_Type())
osLogNotificationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogNotificationsSent.setStatus(_A)
if mibBuilder.loadTexts:osLogNotificationsSent.setUnits('notifications')
_OsLogMsgIgnored_Type=Counter32
_OsLogMsgIgnored_Object=MibScalar
osLogMsgIgnored=_OsLogMsgIgnored_Object((1,3,6,1,4,1,6926,2,32,1,1,8),_OsLogMsgIgnored_Type())
osLogMsgIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogMsgIgnored.setStatus(_A)
if mibBuilder.loadTexts:osLogMsgIgnored.setUnits('messages')
_OsLogTables_ObjectIdentity=ObjectIdentity
osLogTables=_OsLogTables_ObjectIdentity((1,3,6,1,4,1,6926,2,32,1,2))
_OsLogHistoryTable_Object=MibTable
osLogHistoryTable=_OsLogHistoryTable_Object((1,3,6,1,4,1,6926,2,32,1,2,3))
if mibBuilder.loadTexts:osLogHistoryTable.setStatus(_A)
_OsLogHistoryEntry_Object=MibTableRow
osLogHistoryEntry=_OsLogHistoryEntry_Object((1,3,6,1,4,1,6926,2,32,1,2,3,1))
osLogHistoryEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:osLogHistoryEntry.setStatus(_A)
class _OsLogHistIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OsLogHistIndex_Type.__name__=_E
_OsLogHistIndex_Object=MibTableColumn
osLogHistIndex=_OsLogHistIndex_Object((1,3,6,1,4,1,6926,2,32,1,2,3,1,1),_OsLogHistIndex_Type())
osLogHistIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:osLogHistIndex.setStatus(_A)
class _OsLogHistFacility_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_OsLogHistFacility_Type.__name__=_D
_OsLogHistFacility_Object=MibTableColumn
osLogHistFacility=_OsLogHistFacility_Object((1,3,6,1,4,1,6926,2,32,1,2,3,1,2),_OsLogHistFacility_Type())
osLogHistFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogHistFacility.setStatus(_A)
_OsLogHistSeverity_Type=SyslogSeverity
_OsLogHistSeverity_Object=MibTableColumn
osLogHistSeverity=_OsLogHistSeverity_Object((1,3,6,1,4,1,6926,2,32,1,2,3,1,3),_OsLogHistSeverity_Type())
osLogHistSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogHistSeverity.setStatus(_A)
class _OsLogHistMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OsLogHistMessage_Type.__name__=_D
_OsLogHistMessage_Object=MibTableColumn
osLogHistMessage=_OsLogHistMessage_Object((1,3,6,1,4,1,6926,2,32,1,2,3,1,5),_OsLogHistMessage_Type())
osLogHistMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogHistMessage.setStatus(_A)
_OsLogHistUpTime_Type=TimeStamp
_OsLogHistUpTime_Object=MibTableColumn
osLogHistUpTime=_OsLogHistUpTime_Object((1,3,6,1,4,1,6926,2,32,1,2,3,1,6),_OsLogHistUpTime_Type())
osLogHistUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogHistUpTime.setStatus(_A)
_OsLogLastSevTable_Object=MibTable
osLogLastSevTable=_OsLogLastSevTable_Object((1,3,6,1,4,1,6926,2,32,1,2,5))
if mibBuilder.loadTexts:osLogLastSevTable.setStatus(_A)
_OsLogLastSevEntry_Object=MibTableRow
osLogLastSevEntry=_OsLogLastSevEntry_Object((1,3,6,1,4,1,6926,2,32,1,2,5,1))
osLogLastSevEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:osLogLastSevEntry.setStatus(_A)
class _OsLogLastSevIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OsLogLastSevIndex_Type.__name__=_E
_OsLogLastSevIndex_Object=MibTableColumn
osLogLastSevIndex=_OsLogLastSevIndex_Object((1,3,6,1,4,1,6926,2,32,1,2,5,1,1),_OsLogLastSevIndex_Type())
osLogLastSevIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:osLogLastSevIndex.setStatus(_A)
class _OsLogLastSevFacility_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_OsLogLastSevFacility_Type.__name__=_D
_OsLogLastSevFacility_Object=MibTableColumn
osLogLastSevFacility=_OsLogLastSevFacility_Object((1,3,6,1,4,1,6926,2,32,1,2,5,1,2),_OsLogLastSevFacility_Type())
osLogLastSevFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogLastSevFacility.setStatus(_A)
class _OsLogLastSevMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_OsLogLastSevMessage_Type.__name__=_D
_OsLogLastSevMessage_Object=MibTableColumn
osLogLastSevMessage=_OsLogLastSevMessage_Object((1,3,6,1,4,1,6926,2,32,1,2,5,1,5),_OsLogLastSevMessage_Type())
osLogLastSevMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogLastSevMessage.setStatus(_A)
_OsLogLastSevUpTime_Type=TimeStamp
_OsLogLastSevUpTime_Object=MibTableColumn
osLogLastSevUpTime=_OsLogLastSevUpTime_Object((1,3,6,1,4,1,6926,2,32,1,2,5,1,6),_OsLogLastSevUpTime_Type())
osLogLastSevUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:osLogLastSevUpTime.setStatus(_A)
_OsSyslogConformance_ObjectIdentity=ObjectIdentity
osSyslogConformance=_OsSyslogConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,32,100))
_OsLogCompliances_ObjectIdentity=ObjectIdentity
osLogCompliances=_OsLogCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,32,100,1))
_OsLogGroups_ObjectIdentity=ObjectIdentity
osLogGroups=_OsLogGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,32,100,2))
osSyslogMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,32,100,2,1))
osSyslogMandatoryGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_I),(_B,_G),(_B,_J),(_B,_K),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:osSyslogMandatoryGroup.setStatus(_A)
osLogMsgAlarm=NotificationType((1,3,6,1,4,1,6926,2,32,0,1))
osLogMsgAlarm.setObjects(*((_B,_I),(_B,_G),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:osLogMsgAlarm.setStatus(_A)
osSyslogNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6926,2,32,100,2,2))
osSyslogNotificationsGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:osSyslogNotificationsGroup.setStatus(_A)
osLogCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,32,100,1,1))
osLogCompliance.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:osLogCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:SyslogSeverity,'oaccess':oaccess,'oaOptiSwitch':oaOptiSwitch,'osSyslog':osSyslog,'osSyslogNotifications':osSyslogNotifications,_X:osLogMsgAlarm,'osSyslogObjects':osSyslogObjects,'osLogGen':osLogGen,_O:osLogHistTableMaxLength,_P:osLogNotificationsEnabled,_Q:osLogMaxSeverity,_R:osLogDataClear,_S:osLogNotificationsSent,_T:osLogMsgIgnored,'osLogTables':osLogTables,'osLogHistoryTable':osLogHistoryTable,'osLogHistoryEntry':osLogHistoryEntry,_M:osLogHistIndex,_I:osLogHistFacility,_G:osLogHistSeverity,_J:osLogHistMessage,_K:osLogHistUpTime,'osLogLastSevTable':osLogLastSevTable,'osLogLastSevEntry':osLogLastSevEntry,'osLogLastSevIndex':osLogLastSevIndex,_U:osLogLastSevFacility,_V:osLogLastSevMessage,_W:osLogLastSevUpTime,'osSyslogConformance':osSyslogConformance,'osLogCompliances':osLogCompliances,'osLogCompliance':osLogCompliance,'osLogGroups':osLogGroups,_Y:osSyslogMandatoryGroup,_Z:osSyslogNotificationsGroup})