_c='cgprsL2rlyStatsGroup'
_b='cgprsL2rlyConfigGroup'
_a='cgprsL2rlyPeerUnitType'
_Z='cgprsL2rlyDroppedPktsCount'
_Y='cgprsL2rlyDroppedPktsTimeFrame'
_X='cgprsL2rlyTotalPacketsDropped'
_W='cgprsL2rlyInputQLen'
_V='cgprsL2rlyFlowControlTriggerCount'
_U='cgprsL2rlyInterfaceRowStatus'
_T='cgprsL2rlyUnitJoinNotificationEnable'
_S='cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable'
_R='cgprsL2rlyDroppedPktsMonTime'
_Q='cgprsL2rlyFlowControlFlag'
_P='cgprsL2rlyEchoTimer'
_O='cgprsL2rlyUnitType'
_N='cgprsL2rlyPeerUid'
_M='not-accessible'
_L='telecomUnit'
_K='datacomUnit'
_J='packets'
_I='cgprsL2rlyInterfaceId'
_H='seconds'
_G='TruthValue'
_F='cgprsL2rlyUid'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-GPRS-L2RLY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
ciscoGprsL2rlyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9993))
_CiscoGprsL2rlyObjects_ObjectIdentity=ObjectIdentity
ciscoGprsL2rlyObjects=_CiscoGprsL2rlyObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9993,1))
_CiscoGprsL2rlyConfig_ObjectIdentity=ObjectIdentity
ciscoGprsL2rlyConfig=_CiscoGprsL2rlyConfig_ObjectIdentity((1,3,6,1,4,1,9,9,9993,1,1))
class _CgprsL2rlyUid_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CgprsL2rlyUid_Type.__name__=_C
_CgprsL2rlyUid_Object=MibScalar
cgprsL2rlyUid=_CgprsL2rlyUid_Object((1,3,6,1,4,1,9,9,9993,1,1,1),_CgprsL2rlyUid_Type())
cgprsL2rlyUid.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyUid.setStatus(_A)
class _CgprsL2rlyUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CgprsL2rlyUnitType_Type.__name__=_C
_CgprsL2rlyUnitType_Object=MibScalar
cgprsL2rlyUnitType=_CgprsL2rlyUnitType_Object((1,3,6,1,4,1,9,9,9993,1,1,2),_CgprsL2rlyUnitType_Type())
cgprsL2rlyUnitType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyUnitType.setStatus(_A)
class _CgprsL2rlyEchoTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CgprsL2rlyEchoTimer_Type.__name__=_C
_CgprsL2rlyEchoTimer_Object=MibScalar
cgprsL2rlyEchoTimer=_CgprsL2rlyEchoTimer_Object((1,3,6,1,4,1,9,9,9993,1,1,3),_CgprsL2rlyEchoTimer_Type())
cgprsL2rlyEchoTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyEchoTimer.setStatus(_A)
if mibBuilder.loadTexts:cgprsL2rlyEchoTimer.setUnits(_H)
_CgprsL2rlyFlowControlFlag_Type=TruthValue
_CgprsL2rlyFlowControlFlag_Object=MibScalar
cgprsL2rlyFlowControlFlag=_CgprsL2rlyFlowControlFlag_Object((1,3,6,1,4,1,9,9,9993,1,1,4),_CgprsL2rlyFlowControlFlag_Type())
cgprsL2rlyFlowControlFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyFlowControlFlag.setStatus(_A)
class _CgprsL2rlyDroppedPktsMonTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CgprsL2rlyDroppedPktsMonTime_Type.__name__=_C
_CgprsL2rlyDroppedPktsMonTime_Object=MibScalar
cgprsL2rlyDroppedPktsMonTime=_CgprsL2rlyDroppedPktsMonTime_Object((1,3,6,1,4,1,9,9,9993,1,1,5),_CgprsL2rlyDroppedPktsMonTime_Type())
cgprsL2rlyDroppedPktsMonTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyDroppedPktsMonTime.setStatus(_A)
if mibBuilder.loadTexts:cgprsL2rlyDroppedPktsMonTime.setUnits(_H)
class _CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Type(TruthValue):defaultValue=1
_CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Type.__name__=_G
_CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Object=MibScalar
cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable=_CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Object((1,3,6,1,4,1,9,9,9993,1,1,6),_CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Type())
cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable.setStatus(_A)
class _CgprsL2rlyUnitJoinNotificationEnable_Type(TruthValue):defaultValue=1
_CgprsL2rlyUnitJoinNotificationEnable_Type.__name__=_G
_CgprsL2rlyUnitJoinNotificationEnable_Object=MibScalar
cgprsL2rlyUnitJoinNotificationEnable=_CgprsL2rlyUnitJoinNotificationEnable_Object((1,3,6,1,4,1,9,9,9993,1,1,7),_CgprsL2rlyUnitJoinNotificationEnable_Type())
cgprsL2rlyUnitJoinNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cgprsL2rlyUnitJoinNotificationEnable.setStatus(_A)
_CgprsL2rlyInterfaceTable_Object=MibTable
cgprsL2rlyInterfaceTable=_CgprsL2rlyInterfaceTable_Object((1,3,6,1,4,1,9,9,9993,1,1,8))
if mibBuilder.loadTexts:cgprsL2rlyInterfaceTable.setStatus(_A)
_CgprsL2rlyInterfaceEntry_Object=MibTableRow
cgprsL2rlyInterfaceEntry=_CgprsL2rlyInterfaceEntry_Object((1,3,6,1,4,1,9,9,9993,1,1,8,1))
cgprsL2rlyInterfaceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cgprsL2rlyInterfaceEntry.setStatus(_A)
_CgprsL2rlyInterfaceId_Type=InterfaceIndex
_CgprsL2rlyInterfaceId_Object=MibTableColumn
cgprsL2rlyInterfaceId=_CgprsL2rlyInterfaceId_Object((1,3,6,1,4,1,9,9,9993,1,1,8,1,1),_CgprsL2rlyInterfaceId_Type())
cgprsL2rlyInterfaceId.setMaxAccess(_M)
if mibBuilder.loadTexts:cgprsL2rlyInterfaceId.setStatus(_A)
_CgprsL2rlyInterfaceRowStatus_Type=RowStatus
_CgprsL2rlyInterfaceRowStatus_Object=MibTableColumn
cgprsL2rlyInterfaceRowStatus=_CgprsL2rlyInterfaceRowStatus_Object((1,3,6,1,4,1,9,9,9993,1,1,8,1,2),_CgprsL2rlyInterfaceRowStatus_Type())
cgprsL2rlyInterfaceRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:cgprsL2rlyInterfaceRowStatus.setStatus(_A)
_CiscoGprsL2rlyStats_ObjectIdentity=ObjectIdentity
ciscoGprsL2rlyStats=_CiscoGprsL2rlyStats_ObjectIdentity((1,3,6,1,4,1,9,9,9993,1,2))
_CgprsL2rlyFlowControlTriggerCount_Type=Counter32
_CgprsL2rlyFlowControlTriggerCount_Object=MibScalar
cgprsL2rlyFlowControlTriggerCount=_CgprsL2rlyFlowControlTriggerCount_Object((1,3,6,1,4,1,9,9,9993,1,2,1),_CgprsL2rlyFlowControlTriggerCount_Type())
cgprsL2rlyFlowControlTriggerCount.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsL2rlyFlowControlTriggerCount.setStatus(_A)
_CgprsL2rlyInputQLen_Type=Counter32
_CgprsL2rlyInputQLen_Object=MibScalar
cgprsL2rlyInputQLen=_CgprsL2rlyInputQLen_Object((1,3,6,1,4,1,9,9,9993,1,2,2),_CgprsL2rlyInputQLen_Type())
cgprsL2rlyInputQLen.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsL2rlyInputQLen.setStatus(_A)
if mibBuilder.loadTexts:cgprsL2rlyInputQLen.setUnits(_J)
_CgprsL2rlyTotalPacketsDropped_Type=Counter32
_CgprsL2rlyTotalPacketsDropped_Object=MibScalar
cgprsL2rlyTotalPacketsDropped=_CgprsL2rlyTotalPacketsDropped_Object((1,3,6,1,4,1,9,9,9993,1,2,3),_CgprsL2rlyTotalPacketsDropped_Type())
cgprsL2rlyTotalPacketsDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsL2rlyTotalPacketsDropped.setStatus(_A)
if mibBuilder.loadTexts:cgprsL2rlyTotalPacketsDropped.setUnits(_J)
class _CgprsL2rlyDroppedPktsTimeFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CgprsL2rlyDroppedPktsTimeFrame_Type.__name__=_C
_CgprsL2rlyDroppedPktsTimeFrame_Object=MibScalar
cgprsL2rlyDroppedPktsTimeFrame=_CgprsL2rlyDroppedPktsTimeFrame_Object((1,3,6,1,4,1,9,9,9993,1,2,4),_CgprsL2rlyDroppedPktsTimeFrame_Type())
cgprsL2rlyDroppedPktsTimeFrame.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsL2rlyDroppedPktsTimeFrame.setStatus(_A)
if mibBuilder.loadTexts:cgprsL2rlyDroppedPktsTimeFrame.setUnits(_H)
_CgprsL2rlyDroppedPktsCount_Type=Counter32
_CgprsL2rlyDroppedPktsCount_Object=MibScalar
cgprsL2rlyDroppedPktsCount=_CgprsL2rlyDroppedPktsCount_Object((1,3,6,1,4,1,9,9,9993,1,2,5),_CgprsL2rlyDroppedPktsCount_Type())
cgprsL2rlyDroppedPktsCount.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsL2rlyDroppedPktsCount.setStatus(_A)
if mibBuilder.loadTexts:cgprsL2rlyDroppedPktsCount.setUnits(_J)
_CgprsL2rlyPeerTable_Object=MibTable
cgprsL2rlyPeerTable=_CgprsL2rlyPeerTable_Object((1,3,6,1,4,1,9,9,9993,1,2,6))
if mibBuilder.loadTexts:cgprsL2rlyPeerTable.setStatus(_A)
_CgprsL2rlyPeerEntry_Object=MibTableRow
cgprsL2rlyPeerEntry=_CgprsL2rlyPeerEntry_Object((1,3,6,1,4,1,9,9,9993,1,2,6,1))
cgprsL2rlyPeerEntry.setIndexNames((0,_B,_N),(0,_B,_I))
if mibBuilder.loadTexts:cgprsL2rlyPeerEntry.setStatus(_A)
class _CgprsL2rlyPeerUid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CgprsL2rlyPeerUid_Type.__name__=_C
_CgprsL2rlyPeerUid_Object=MibTableColumn
cgprsL2rlyPeerUid=_CgprsL2rlyPeerUid_Object((1,3,6,1,4,1,9,9,9993,1,2,6,1,1),_CgprsL2rlyPeerUid_Type())
cgprsL2rlyPeerUid.setMaxAccess(_M)
if mibBuilder.loadTexts:cgprsL2rlyPeerUid.setStatus(_A)
class _CgprsL2rlyPeerUnitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CgprsL2rlyPeerUnitType_Type.__name__=_C
_CgprsL2rlyPeerUnitType_Object=MibTableColumn
cgprsL2rlyPeerUnitType=_CgprsL2rlyPeerUnitType_Object((1,3,6,1,4,1,9,9,9993,1,2,6,1,2),_CgprsL2rlyPeerUnitType_Type())
cgprsL2rlyPeerUnitType.setMaxAccess(_E)
if mibBuilder.loadTexts:cgprsL2rlyPeerUnitType.setStatus(_A)
_CiscoGprsL2rlyNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoGprsL2rlyNotificationPrefix=_CiscoGprsL2rlyNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,9993,2))
_CiscoGprsL2rlyNotifications_ObjectIdentity=ObjectIdentity
ciscoGprsL2rlyNotifications=_CiscoGprsL2rlyNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,9993,2,0))
_CiscoGprsL2rlyConformances_ObjectIdentity=ObjectIdentity
ciscoGprsL2rlyConformances=_CiscoGprsL2rlyConformances_ObjectIdentity((1,3,6,1,4,1,9,9,9993,3))
_CgprsL2rlyCompliances_ObjectIdentity=ObjectIdentity
cgprsL2rlyCompliances=_CgprsL2rlyCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9993,3,1))
_CgprsL2rlyGroups_ObjectIdentity=ObjectIdentity
cgprsL2rlyGroups=_CgprsL2rlyGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9993,3,2))
cgprsL2rlyConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,9993,3,2,1))
cgprsL2rlyConfigGroup.setObjects(*((_B,_F),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cgprsL2rlyConfigGroup.setStatus(_A)
cgprsL2rlyStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,9993,3,2,2))
cgprsL2rlyStatsGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cgprsL2rlyStatsGroup.setStatus(_A)
cgprsL2rlyUnitJoinNotification=NotificationType((1,3,6,1,4,1,9,9,9993,2,0,1))
cgprsL2rlyUnitJoinNotification.setObjects((_B,_F))
if mibBuilder.loadTexts:cgprsL2rlyUnitJoinNotification.setStatus(_A)
cgprsL2rlyNoRespToKeepAliveMsgNotification=NotificationType((1,3,6,1,4,1,9,9,9993,2,0,2))
cgprsL2rlyNoRespToKeepAliveMsgNotification.setObjects((_B,_F))
if mibBuilder.loadTexts:cgprsL2rlyNoRespToKeepAliveMsgNotification.setStatus(_A)
cgprsL2rlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,9993,3,1,1))
cgprsL2rlyCompliance.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cgprsL2rlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoGprsL2rlyMIB':ciscoGprsL2rlyMIB,'ciscoGprsL2rlyObjects':ciscoGprsL2rlyObjects,'ciscoGprsL2rlyConfig':ciscoGprsL2rlyConfig,_F:cgprsL2rlyUid,_O:cgprsL2rlyUnitType,_P:cgprsL2rlyEchoTimer,_Q:cgprsL2rlyFlowControlFlag,_R:cgprsL2rlyDroppedPktsMonTime,_S:cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable,_T:cgprsL2rlyUnitJoinNotificationEnable,'cgprsL2rlyInterfaceTable':cgprsL2rlyInterfaceTable,'cgprsL2rlyInterfaceEntry':cgprsL2rlyInterfaceEntry,_I:cgprsL2rlyInterfaceId,_U:cgprsL2rlyInterfaceRowStatus,'ciscoGprsL2rlyStats':ciscoGprsL2rlyStats,_V:cgprsL2rlyFlowControlTriggerCount,_W:cgprsL2rlyInputQLen,_X:cgprsL2rlyTotalPacketsDropped,_Y:cgprsL2rlyDroppedPktsTimeFrame,_Z:cgprsL2rlyDroppedPktsCount,'cgprsL2rlyPeerTable':cgprsL2rlyPeerTable,'cgprsL2rlyPeerEntry':cgprsL2rlyPeerEntry,_N:cgprsL2rlyPeerUid,_a:cgprsL2rlyPeerUnitType,'ciscoGprsL2rlyNotificationPrefix':ciscoGprsL2rlyNotificationPrefix,'ciscoGprsL2rlyNotifications':ciscoGprsL2rlyNotifications,'cgprsL2rlyUnitJoinNotification':cgprsL2rlyUnitJoinNotification,'cgprsL2rlyNoRespToKeepAliveMsgNotification':cgprsL2rlyNoRespToKeepAliveMsgNotification,'ciscoGprsL2rlyConformances':ciscoGprsL2rlyConformances,'cgprsL2rlyCompliances':cgprsL2rlyCompliances,'cgprsL2rlyCompliance':cgprsL2rlyCompliance,'cgprsL2rlyGroups':cgprsL2rlyGroups,_b:cgprsL2rlyConfigGroup,_c:cgprsL2rlyStatsGroup})