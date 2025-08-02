_g='cpscNotificationGroupRev1'
_f='cpscNotificationGroup'
_e='cpscEventRev1'
_d='cpscEvent'
_c='cpscHistoryEndTime'
_b='cpscHistoryStartTime'
_a='cpscSuppressedPacket'
_Z='cpscNotificationThreshold'
_Y='cpscNotificationControl'
_X='cpscCurrentLevel'
_W='cpscAction'
_V='cpscLowerThreshold'
_U='cpscUpperThreshold'
_T='cpscHistoryIndex'
_S='cpscHistoryTrafficType'
_R='shutdown'
_Q='cpscHistoryGroup'
_P='cpscStatisticsGroup'
_O='cpscStatusGroup'
_N='cpscNotifConfigurationGroup'
_M='cpscConfigurationGroup'
_L='deprecated'
_K='0.01 Percentage'
_J='not-accessible'
_I='cpscTrafficType'
_H='cpscStatus'
_G='read-only'
_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='CISCO-PORT-STORM-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoPortStormControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,362))
if mibBuilder.loadTexts:ciscoPortStormControlMIB.setRevisions(('2007-10-19 00:00','2003-07-03 00:00'))
class CPortStormControlTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('broadcast',1),('multicast',2),('unicast',3),('all',4)))
class CPortStormControlActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('filter',1),(_R,2)))
class CPortStormControlStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('forwarding',2),('trafficTypeFiltered',3),('allTrafficFiltered',4),(_R,5)))
_CiscoPortStormControlMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoPortStormControlMIBNotifs=_CiscoPortStormControlMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,362,0))
_CpscNotificationsPrefix_ObjectIdentity=ObjectIdentity
cpscNotificationsPrefix=_CpscNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,362,0,1))
_CiscoPortStormControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPortStormControlMIBObjects=_CiscoPortStormControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,362,1))
_CpscConfigObjects_ObjectIdentity=ObjectIdentity
cpscConfigObjects=_CpscConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,362,1,1))
_CpscThresholdTable_Object=MibTable
cpscThresholdTable=_CpscThresholdTable_Object((1,3,6,1,4,1,9,9,362,1,1,1))
if mibBuilder.loadTexts:cpscThresholdTable.setStatus(_A)
_CpscThresholdEntry_Object=MibTableRow
cpscThresholdEntry=_CpscThresholdEntry_Object((1,3,6,1,4,1,9,9,362,1,1,1,1))
cpscThresholdEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:cpscThresholdEntry.setStatus(_A)
_CpscTrafficType_Type=CPortStormControlTrafficType
_CpscTrafficType_Object=MibTableColumn
cpscTrafficType=_CpscTrafficType_Object((1,3,6,1,4,1,9,9,362,1,1,1,1,1),_CpscTrafficType_Type())
cpscTrafficType.setMaxAccess(_J)
if mibBuilder.loadTexts:cpscTrafficType.setStatus(_A)
class _CpscUpperThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CpscUpperThreshold_Type.__name__=_C
_CpscUpperThreshold_Object=MibTableColumn
cpscUpperThreshold=_CpscUpperThreshold_Object((1,3,6,1,4,1,9,9,362,1,1,1,1,2),_CpscUpperThreshold_Type())
cpscUpperThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:cpscUpperThreshold.setStatus(_A)
if mibBuilder.loadTexts:cpscUpperThreshold.setUnits(_K)
class _CpscLowerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CpscLowerThreshold_Type.__name__=_C
_CpscLowerThreshold_Object=MibTableColumn
cpscLowerThreshold=_CpscLowerThreshold_Object((1,3,6,1,4,1,9,9,362,1,1,1,1,3),_CpscLowerThreshold_Type())
cpscLowerThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:cpscLowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:cpscLowerThreshold.setUnits(_K)
_CpscActionTable_Object=MibTable
cpscActionTable=_CpscActionTable_Object((1,3,6,1,4,1,9,9,362,1,1,2))
if mibBuilder.loadTexts:cpscActionTable.setStatus(_A)
_CpscActionEntry_Object=MibTableRow
cpscActionEntry=_CpscActionEntry_Object((1,3,6,1,4,1,9,9,362,1,1,2,1))
cpscActionEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpscActionEntry.setStatus(_A)
_CpscAction_Type=CPortStormControlActionType
_CpscAction_Object=MibTableColumn
cpscAction=_CpscAction_Object((1,3,6,1,4,1,9,9,362,1,1,2,1,1),_CpscAction_Type())
cpscAction.setMaxAccess(_F)
if mibBuilder.loadTexts:cpscAction.setStatus(_A)
class _CpscNotificationControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('stormOccurred',2),('stormCleared',3),('both',4)))
_CpscNotificationControl_Type.__name__=_C
_CpscNotificationControl_Object=MibTableColumn
cpscNotificationControl=_CpscNotificationControl_Object((1,3,6,1,4,1,9,9,362,1,1,2,1,2),_CpscNotificationControl_Type())
cpscNotificationControl.setMaxAccess(_F)
if mibBuilder.loadTexts:cpscNotificationControl.setStatus(_A)
class _CpscNotificationThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CpscNotificationThreshold_Type.__name__=_C
_CpscNotificationThreshold_Object=MibScalar
cpscNotificationThreshold=_CpscNotificationThreshold_Object((1,3,6,1,4,1,9,9,362,1,1,3),_CpscNotificationThreshold_Type())
cpscNotificationThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:cpscNotificationThreshold.setStatus(_A)
if mibBuilder.loadTexts:cpscNotificationThreshold.setUnits('Notifications per Minute')
_CpscStatusObjects_ObjectIdentity=ObjectIdentity
cpscStatusObjects=_CpscStatusObjects_ObjectIdentity((1,3,6,1,4,1,9,9,362,1,2))
_CpscStatusTable_Object=MibTable
cpscStatusTable=_CpscStatusTable_Object((1,3,6,1,4,1,9,9,362,1,2,1))
if mibBuilder.loadTexts:cpscStatusTable.setStatus(_A)
_CpscStatusEntry_Object=MibTableRow
cpscStatusEntry=_CpscStatusEntry_Object((1,3,6,1,4,1,9,9,362,1,2,1,1))
cpscStatusEntry.setIndexNames((0,_D,_E),(0,_B,_I))
if mibBuilder.loadTexts:cpscStatusEntry.setStatus(_A)
_CpscStatus_Type=CPortStormControlStatusType
_CpscStatus_Object=MibTableColumn
cpscStatus=_CpscStatus_Object((1,3,6,1,4,1,9,9,362,1,2,1,1,1),_CpscStatus_Type())
cpscStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cpscStatus.setStatus(_A)
class _CpscCurrentLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CpscCurrentLevel_Type.__name__=_C
_CpscCurrentLevel_Object=MibTableColumn
cpscCurrentLevel=_CpscCurrentLevel_Object((1,3,6,1,4,1,9,9,362,1,2,1,1,2),_CpscCurrentLevel_Type())
cpscCurrentLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:cpscCurrentLevel.setStatus(_A)
if mibBuilder.loadTexts:cpscCurrentLevel.setUnits(_K)
_CpscSuppressedPacket_Type=Counter64
_CpscSuppressedPacket_Object=MibTableColumn
cpscSuppressedPacket=_CpscSuppressedPacket_Object((1,3,6,1,4,1,9,9,362,1,2,1,1,3),_CpscSuppressedPacket_Type())
cpscSuppressedPacket.setMaxAccess(_G)
if mibBuilder.loadTexts:cpscSuppressedPacket.setStatus(_A)
_CpscHistoryTable_Object=MibTable
cpscHistoryTable=_CpscHistoryTable_Object((1,3,6,1,4,1,9,9,362,1,2,2))
if mibBuilder.loadTexts:cpscHistoryTable.setStatus(_A)
_CpscHistoryEntry_Object=MibTableRow
cpscHistoryEntry=_CpscHistoryEntry_Object((1,3,6,1,4,1,9,9,362,1,2,2,1))
cpscHistoryEntry.setIndexNames((0,_D,_E),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cpscHistoryEntry.setStatus(_A)
_CpscHistoryTrafficType_Type=CPortStormControlTrafficType
_CpscHistoryTrafficType_Object=MibTableColumn
cpscHistoryTrafficType=_CpscHistoryTrafficType_Object((1,3,6,1,4,1,9,9,362,1,2,2,1,1),_CpscHistoryTrafficType_Type())
cpscHistoryTrafficType.setMaxAccess(_J)
if mibBuilder.loadTexts:cpscHistoryTrafficType.setStatus(_A)
class _CpscHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CpscHistoryIndex_Type.__name__=_C
_CpscHistoryIndex_Object=MibTableColumn
cpscHistoryIndex=_CpscHistoryIndex_Object((1,3,6,1,4,1,9,9,362,1,2,2,1,2),_CpscHistoryIndex_Type())
cpscHistoryIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpscHistoryIndex.setStatus(_A)
_CpscHistoryStartTime_Type=TimeStamp
_CpscHistoryStartTime_Object=MibTableColumn
cpscHistoryStartTime=_CpscHistoryStartTime_Object((1,3,6,1,4,1,9,9,362,1,2,2,1,3),_CpscHistoryStartTime_Type())
cpscHistoryStartTime.setMaxAccess(_G)
if mibBuilder.loadTexts:cpscHistoryStartTime.setStatus(_A)
_CpscHistoryEndTime_Type=TimeStamp
_CpscHistoryEndTime_Object=MibTableColumn
cpscHistoryEndTime=_CpscHistoryEndTime_Object((1,3,6,1,4,1,9,9,362,1,2,2,1,4),_CpscHistoryEndTime_Type())
cpscHistoryEndTime.setMaxAccess(_G)
if mibBuilder.loadTexts:cpscHistoryEndTime.setStatus(_A)
_CiscoPortStormControlMIBConform_ObjectIdentity=ObjectIdentity
ciscoPortStormControlMIBConform=_CiscoPortStormControlMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,362,2))
_CiscoPortStormControlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPortStormControlMIBCompliances=_CiscoPortStormControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,362,2,1))
_CiscoPortStormControlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPortStormControlMIBGroups=_CiscoPortStormControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,362,2,2))
cpscConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,362,2,2,1))
cpscConfigurationGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cpscConfigurationGroup.setStatus(_A)
cpscStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,362,2,2,2))
cpscStatusGroup.setObjects(*((_B,_H),(_B,_X)))
if mibBuilder.loadTexts:cpscStatusGroup.setStatus(_A)
cpscNotifConfigurationGroup=ObjectGroup((1,3,6,1,4,1,9,9,362,2,2,4))
cpscNotifConfigurationGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:cpscNotifConfigurationGroup.setStatus(_A)
cpscStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,362,2,2,5))
cpscStatisticsGroup.setObjects((_B,_a))
if mibBuilder.loadTexts:cpscStatisticsGroup.setStatus(_A)
cpscHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,362,2,2,6))
cpscHistoryGroup.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cpscHistoryGroup.setStatus(_A)
cpscEvent=NotificationType((1,3,6,1,4,1,9,9,362,0,1,1))
cpscEvent.setObjects((_B,_H))
if mibBuilder.loadTexts:cpscEvent.setStatus(_L)
cpscEventRev1=NotificationType((1,3,6,1,4,1,9,9,362,0,2))
cpscEventRev1.setObjects((_B,_H))
if mibBuilder.loadTexts:cpscEventRev1.setStatus(_A)
cpscNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,362,2,2,3))
cpscNotificationGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:cpscNotificationGroup.setStatus(_L)
cpscNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,362,2,2,7))
cpscNotificationGroupRev1.setObjects((_B,_e))
if mibBuilder.loadTexts:cpscNotificationGroupRev1.setStatus(_A)
ciscoPortStormControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,362,2,1,1))
ciscoPortStormControlMIBCompliance.setObjects(*((_B,_M),(_B,_N),(_B,_f),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoPortStormControlMIBCompliance.setStatus(_L)
ciscoPortStormControlMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,362,2,1,2))
ciscoPortStormControlMIBComplianceRev1.setObjects(*((_B,_M),(_B,_N),(_B,_g),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoPortStormControlMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CPortStormControlTrafficType':CPortStormControlTrafficType,'CPortStormControlActionType':CPortStormControlActionType,'CPortStormControlStatusType':CPortStormControlStatusType,'ciscoPortStormControlMIB':ciscoPortStormControlMIB,'ciscoPortStormControlMIBNotifs':ciscoPortStormControlMIBNotifs,'cpscNotificationsPrefix':cpscNotificationsPrefix,_d:cpscEvent,_e:cpscEventRev1,'ciscoPortStormControlMIBObjects':ciscoPortStormControlMIBObjects,'cpscConfigObjects':cpscConfigObjects,'cpscThresholdTable':cpscThresholdTable,'cpscThresholdEntry':cpscThresholdEntry,_I:cpscTrafficType,_U:cpscUpperThreshold,_V:cpscLowerThreshold,'cpscActionTable':cpscActionTable,'cpscActionEntry':cpscActionEntry,_W:cpscAction,_Y:cpscNotificationControl,_Z:cpscNotificationThreshold,'cpscStatusObjects':cpscStatusObjects,'cpscStatusTable':cpscStatusTable,'cpscStatusEntry':cpscStatusEntry,_H:cpscStatus,_X:cpscCurrentLevel,_a:cpscSuppressedPacket,'cpscHistoryTable':cpscHistoryTable,'cpscHistoryEntry':cpscHistoryEntry,_S:cpscHistoryTrafficType,_T:cpscHistoryIndex,_b:cpscHistoryStartTime,_c:cpscHistoryEndTime,'ciscoPortStormControlMIBConform':ciscoPortStormControlMIBConform,'ciscoPortStormControlMIBCompliances':ciscoPortStormControlMIBCompliances,'ciscoPortStormControlMIBCompliance':ciscoPortStormControlMIBCompliance,'ciscoPortStormControlMIBComplianceRev1':ciscoPortStormControlMIBComplianceRev1,'ciscoPortStormControlMIBGroups':ciscoPortStormControlMIBGroups,_M:cpscConfigurationGroup,_O:cpscStatusGroup,_f:cpscNotificationGroup,_N:cpscNotifConfigurationGroup,_P:cpscStatisticsGroup,_Q:cpscHistoryGroup,_g:cpscNotificationGroupRev1})