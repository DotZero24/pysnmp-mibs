_V='zyIgmpSnoopingClientIpAddress'
_U='zyIgmpSnoopingClientGroupIpAddress'
_T='zyIgmpSnoopingClientPort'
_S='zyIgmpSnoopingClientVid'
_R='zyIgmpSnoopingGroupIpAddress'
_Q='zyIgmpSnoopingGroupVid'
_P='zyIgmpSnoopingGroupCountVlanVid'
_O='zyIgmpSnoopingCountVlanVid'
_N='zyIgmpSnoopingCountIndex'
_M='zyIgmpSnoopingInfoVlanVid'
_L='zyIgmpSnoopingRecordGroup'
_K='zyIgmpSnoopingRecordPort'
_J='zyIgmpSnoopingRecordVid'
_I='zyIgmpSnoopingVlanVid'
_H='dot1dBasePort'
_G='BRIDGE-MIB'
_F='Integer32'
_E='not-accessible'
_D='ZYXEL-IGMP-SNOOPING-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_G,_H)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIgmpSnooping=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,31))
_ZyxelIgmpSnoopingSetup_ObjectIdentity=ObjectIdentity
zyxelIgmpSnoopingSetup=_ZyxelIgmpSnoopingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,31,1))
_ZyIgmpSnoopingState_Type=EnabledStatus
_ZyIgmpSnoopingState_Object=MibScalar
zyIgmpSnoopingState=_ZyIgmpSnoopingState_Object((1,3,6,1,4,1,890,1,15,3,31,1,1),_ZyIgmpSnoopingState_Type())
zyIgmpSnoopingState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingState.setStatus(_A)
_ZyIgmpSnoopingGroupHostTimeout_Type=Integer32
_ZyIgmpSnoopingGroupHostTimeout_Object=MibScalar
zyIgmpSnoopingGroupHostTimeout=_ZyIgmpSnoopingGroupHostTimeout_Object((1,3,6,1,4,1,890,1,15,3,31,1,2),_ZyIgmpSnoopingGroupHostTimeout_Type())
zyIgmpSnoopingGroupHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupHostTimeout.setStatus(_A)
_ZyIgmpSnooping8021pPriority_Type=Integer32
_ZyIgmpSnooping8021pPriority_Object=MibScalar
zyIgmpSnooping8021pPriority=_ZyIgmpSnooping8021pPriority_Object((1,3,6,1,4,1,890,1,15,3,31,1,3),_ZyIgmpSnooping8021pPriority_Type())
zyIgmpSnooping8021pPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnooping8021pPriority.setStatus(_A)
class _ZyIgmpSnoopingVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('fixed',2)))
_ZyIgmpSnoopingVlanMode_Type.__name__=_F
_ZyIgmpSnoopingVlanMode_Object=MibScalar
zyIgmpSnoopingVlanMode=_ZyIgmpSnoopingVlanMode_Object((1,3,6,1,4,1,890,1,15,3,31,1,4),_ZyIgmpSnoopingVlanMode_Type())
zyIgmpSnoopingVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingVlanMode.setStatus(_A)
_ZyIgmpSnoopingMaxNumberOfVlans_Type=Integer32
_ZyIgmpSnoopingMaxNumberOfVlans_Object=MibScalar
zyIgmpSnoopingMaxNumberOfVlans=_ZyIgmpSnoopingMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,31,1,5),_ZyIgmpSnoopingMaxNumberOfVlans_Type())
zyIgmpSnoopingMaxNumberOfVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingMaxNumberOfVlans.setStatus(_A)
_ZyxelIgmpSnoopingVlanTable_Object=MibTable
zyxelIgmpSnoopingVlanTable=_ZyxelIgmpSnoopingVlanTable_Object((1,3,6,1,4,1,890,1,15,3,31,1,6))
if mibBuilder.loadTexts:zyxelIgmpSnoopingVlanTable.setStatus(_A)
_ZyxelIgmpSnoopingVlanEntry_Object=MibTableRow
zyxelIgmpSnoopingVlanEntry=_ZyxelIgmpSnoopingVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,31,1,6,1))
zyxelIgmpSnoopingVlanEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:zyxelIgmpSnoopingVlanEntry.setStatus(_A)
_ZyIgmpSnoopingVlanVid_Type=Integer32
_ZyIgmpSnoopingVlanVid_Object=MibTableColumn
zyIgmpSnoopingVlanVid=_ZyIgmpSnoopingVlanVid_Object((1,3,6,1,4,1,890,1,15,3,31,1,6,1,1),_ZyIgmpSnoopingVlanVid_Type())
zyIgmpSnoopingVlanVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingVlanVid.setStatus(_A)
_ZyIgmpSnoopingVlanName_Type=DisplayString
_ZyIgmpSnoopingVlanName_Object=MibTableColumn
zyIgmpSnoopingVlanName=_ZyIgmpSnoopingVlanName_Object((1,3,6,1,4,1,890,1,15,3,31,1,6,1,2),_ZyIgmpSnoopingVlanName_Type())
zyIgmpSnoopingVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingVlanName.setStatus(_A)
_ZyIgmpSnoopingVlanRowStatus_Type=RowStatus
_ZyIgmpSnoopingVlanRowStatus_Object=MibTableColumn
zyIgmpSnoopingVlanRowStatus=_ZyIgmpSnoopingVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,31,1,6,1,3),_ZyIgmpSnoopingVlanRowStatus_Type())
zyIgmpSnoopingVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyIgmpSnoopingVlanRowStatus.setStatus(_A)
_ZyIgmpSnoopingQuerierModeState_Type=EnabledStatus
_ZyIgmpSnoopingQuerierModeState_Object=MibScalar
zyIgmpSnoopingQuerierModeState=_ZyIgmpSnoopingQuerierModeState_Object((1,3,6,1,4,1,890,1,15,3,31,1,7),_ZyIgmpSnoopingQuerierModeState_Type())
zyIgmpSnoopingQuerierModeState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingQuerierModeState.setStatus(_A)
_ZyIgmpSnoopingReportProxyState_Type=EnabledStatus
_ZyIgmpSnoopingReportProxyState_Object=MibScalar
zyIgmpSnoopingReportProxyState=_ZyIgmpSnoopingReportProxyState_Object((1,3,6,1,4,1,890,1,15,3,31,1,8),_ZyIgmpSnoopingReportProxyState_Type())
zyIgmpSnoopingReportProxyState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingReportProxyState.setStatus(_A)
_ZyxelIgmpSnoopingPortTable_Object=MibTable
zyxelIgmpSnoopingPortTable=_ZyxelIgmpSnoopingPortTable_Object((1,3,6,1,4,1,890,1,15,3,31,1,9))
if mibBuilder.loadTexts:zyxelIgmpSnoopingPortTable.setStatus(_A)
_ZyxelIgmpSnoopingPortEntry_Object=MibTableRow
zyxelIgmpSnoopingPortEntry=_ZyxelIgmpSnoopingPortEntry_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1))
zyxelIgmpSnoopingPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelIgmpSnoopingPortEntry.setStatus(_A)
_ZyIgmpSnoopingPortMaxGroupLimitedState_Type=EnabledStatus
_ZyIgmpSnoopingPortMaxGroupLimitedState_Object=MibTableColumn
zyIgmpSnoopingPortMaxGroupLimitedState=_ZyIgmpSnoopingPortMaxGroupLimitedState_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,1),_ZyIgmpSnoopingPortMaxGroupLimitedState_Type())
zyIgmpSnoopingPortMaxGroupLimitedState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortMaxGroupLimitedState.setStatus(_A)
_ZyIgmpSnoopingPortMaxOfGroups_Type=Integer32
_ZyIgmpSnoopingPortMaxOfGroups_Object=MibTableColumn
zyIgmpSnoopingPortMaxOfGroups=_ZyIgmpSnoopingPortMaxOfGroups_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,2),_ZyIgmpSnoopingPortMaxOfGroups_Type())
zyIgmpSnoopingPortMaxOfGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortMaxOfGroups.setStatus(_A)
class _ZyIgmpSnoopingPortQuerierMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('fixed',2),('edge',3)))
_ZyIgmpSnoopingPortQuerierMode_Type.__name__=_F
_ZyIgmpSnoopingPortQuerierMode_Object=MibTableColumn
zyIgmpSnoopingPortQuerierMode=_ZyIgmpSnoopingPortQuerierMode_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,3),_ZyIgmpSnoopingPortQuerierMode_Type())
zyIgmpSnoopingPortQuerierMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortQuerierMode.setStatus(_A)
class _ZyIgmpSnoopingPortThrottlingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('replace',2)))
_ZyIgmpSnoopingPortThrottlingAction_Type.__name__=_F
_ZyIgmpSnoopingPortThrottlingAction_Object=MibTableColumn
zyIgmpSnoopingPortThrottlingAction=_ZyIgmpSnoopingPortThrottlingAction_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,4),_ZyIgmpSnoopingPortThrottlingAction_Type())
zyIgmpSnoopingPortThrottlingAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortThrottlingAction.setStatus(_A)
class _ZyIgmpSnoopingPortLeaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('immediate',1),('fast',2)))
_ZyIgmpSnoopingPortLeaveMode_Type.__name__=_F
_ZyIgmpSnoopingPortLeaveMode_Object=MibTableColumn
zyIgmpSnoopingPortLeaveMode=_ZyIgmpSnoopingPortLeaveMode_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,5),_ZyIgmpSnoopingPortLeaveMode_Type())
zyIgmpSnoopingPortLeaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortLeaveMode.setStatus(_A)
_ZyIgmpSnoopingPortLeaveTimeout_Type=Integer32
_ZyIgmpSnoopingPortLeaveTimeout_Object=MibTableColumn
zyIgmpSnoopingPortLeaveTimeout=_ZyIgmpSnoopingPortLeaveTimeout_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,6),_ZyIgmpSnoopingPortLeaveTimeout_Type())
zyIgmpSnoopingPortLeaveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortLeaveTimeout.setStatus(_A)
_ZyIgmpSnoopingPortFastLeaveTimeout_Type=Integer32
_ZyIgmpSnoopingPortFastLeaveTimeout_Object=MibTableColumn
zyIgmpSnoopingPortFastLeaveTimeout=_ZyIgmpSnoopingPortFastLeaveTimeout_Object((1,3,6,1,4,1,890,1,15,3,31,1,9,1,7),_ZyIgmpSnoopingPortFastLeaveTimeout_Type())
zyIgmpSnoopingPortFastLeaveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingPortFastLeaveTimeout.setStatus(_A)
class _ZyIgmpSnoopingQuerierVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('igmpV2',2),('igmpV3',3)))
_ZyIgmpSnoopingQuerierVersion_Type.__name__=_F
_ZyIgmpSnoopingQuerierVersion_Object=MibScalar
zyIgmpSnoopingQuerierVersion=_ZyIgmpSnoopingQuerierVersion_Object((1,3,6,1,4,1,890,1,15,3,31,1,11),_ZyIgmpSnoopingQuerierVersion_Type())
zyIgmpSnoopingQuerierVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingQuerierVersion.setStatus(_A)
_ZyIgmpSnoopingSmartForward_Type=EnabledStatus
_ZyIgmpSnoopingSmartForward_Object=MibScalar
zyIgmpSnoopingSmartForward=_ZyIgmpSnoopingSmartForward_Object((1,3,6,1,4,1,890,1,15,3,31,1,12),_ZyIgmpSnoopingSmartForward_Type())
zyIgmpSnoopingSmartForward.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingSmartForward.setStatus(_A)
_ZyxelIgmpSnoopingStatus_ObjectIdentity=ObjectIdentity
zyxelIgmpSnoopingStatus=_ZyxelIgmpSnoopingStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,31,2))
_ZyxelIgmpSnoopingRecordTable_Object=MibTable
zyxelIgmpSnoopingRecordTable=_ZyxelIgmpSnoopingRecordTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,1))
if mibBuilder.loadTexts:zyxelIgmpSnoopingRecordTable.setStatus(_A)
_ZyxelIgmpSnoopingRecordEntry_Object=MibTableRow
zyxelIgmpSnoopingRecordEntry=_ZyxelIgmpSnoopingRecordEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1))
zyxelIgmpSnoopingRecordEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:zyxelIgmpSnoopingRecordEntry.setStatus(_A)
_ZyIgmpSnoopingRecordIndex_Type=Integer32
_ZyIgmpSnoopingRecordIndex_Object=MibTableColumn
zyIgmpSnoopingRecordIndex=_ZyIgmpSnoopingRecordIndex_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1,1),_ZyIgmpSnoopingRecordIndex_Type())
zyIgmpSnoopingRecordIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingRecordIndex.setStatus(_A)
_ZyIgmpSnoopingRecordVid_Type=Integer32
_ZyIgmpSnoopingRecordVid_Object=MibTableColumn
zyIgmpSnoopingRecordVid=_ZyIgmpSnoopingRecordVid_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1,2),_ZyIgmpSnoopingRecordVid_Type())
zyIgmpSnoopingRecordVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingRecordVid.setStatus(_A)
_ZyIgmpSnoopingRecordPort_Type=Integer32
_ZyIgmpSnoopingRecordPort_Object=MibTableColumn
zyIgmpSnoopingRecordPort=_ZyIgmpSnoopingRecordPort_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1,3),_ZyIgmpSnoopingRecordPort_Type())
zyIgmpSnoopingRecordPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingRecordPort.setStatus(_A)
_ZyIgmpSnoopingRecordGroup_Type=IpAddress
_ZyIgmpSnoopingRecordGroup_Object=MibTableColumn
zyIgmpSnoopingRecordGroup=_ZyIgmpSnoopingRecordGroup_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1,4),_ZyIgmpSnoopingRecordGroup_Type())
zyIgmpSnoopingRecordGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingRecordGroup.setStatus(_A)
_ZyIgmpSnoopingRecordTimeout_Type=Integer32
_ZyIgmpSnoopingRecordTimeout_Object=MibTableColumn
zyIgmpSnoopingRecordTimeout=_ZyIgmpSnoopingRecordTimeout_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1,5),_ZyIgmpSnoopingRecordTimeout_Type())
zyIgmpSnoopingRecordTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingRecordTimeout.setStatus(_A)
_ZyIgmpSnoopingRecordUpTime_Type=Integer32
_ZyIgmpSnoopingRecordUpTime_Object=MibTableColumn
zyIgmpSnoopingRecordUpTime=_ZyIgmpSnoopingRecordUpTime_Object((1,3,6,1,4,1,890,1,15,3,31,2,1,1,6),_ZyIgmpSnoopingRecordUpTime_Type())
zyIgmpSnoopingRecordUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingRecordUpTime.setStatus(_A)
_ZyxelIgmpSnoopingInfoVlanTable_Object=MibTable
zyxelIgmpSnoopingInfoVlanTable=_ZyxelIgmpSnoopingInfoVlanTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,2))
if mibBuilder.loadTexts:zyxelIgmpSnoopingInfoVlanTable.setStatus(_A)
_ZyxelIgmpSnoopingInfoVlanEntry_Object=MibTableRow
zyxelIgmpSnoopingInfoVlanEntry=_ZyxelIgmpSnoopingInfoVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,2,1))
zyxelIgmpSnoopingInfoVlanEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:zyxelIgmpSnoopingInfoVlanEntry.setStatus(_A)
_ZyIgmpSnoopingInfoVlanVid_Type=Integer32
_ZyIgmpSnoopingInfoVlanVid_Object=MibTableColumn
zyIgmpSnoopingInfoVlanVid=_ZyIgmpSnoopingInfoVlanVid_Object((1,3,6,1,4,1,890,1,15,3,31,2,2,1,1),_ZyIgmpSnoopingInfoVlanVid_Type())
zyIgmpSnoopingInfoVlanVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingInfoVlanVid.setStatus(_A)
class _ZyIgmpSnoopingInfoVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('mvr',2),('static',3)))
_ZyIgmpSnoopingInfoVlanType_Type.__name__=_F
_ZyIgmpSnoopingInfoVlanType_Object=MibTableColumn
zyIgmpSnoopingInfoVlanType=_ZyIgmpSnoopingInfoVlanType_Object((1,3,6,1,4,1,890,1,15,3,31,2,2,1,2),_ZyIgmpSnoopingInfoVlanType_Type())
zyIgmpSnoopingInfoVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingInfoVlanType.setStatus(_A)
_ZyIgmpSnoopingInfoVlanQueryPorts_Type=PortList
_ZyIgmpSnoopingInfoVlanQueryPorts_Object=MibTableColumn
zyIgmpSnoopingInfoVlanQueryPorts=_ZyIgmpSnoopingInfoVlanQueryPorts_Object((1,3,6,1,4,1,890,1,15,3,31,2,2,1,3),_ZyIgmpSnoopingInfoVlanQueryPorts_Type())
zyIgmpSnoopingInfoVlanQueryPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingInfoVlanQueryPorts.setStatus(_A)
_ZyxelIgmpSnoopingCountTable_Object=MibTable
zyxelIgmpSnoopingCountTable=_ZyxelIgmpSnoopingCountTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,3))
if mibBuilder.loadTexts:zyxelIgmpSnoopingCountTable.setStatus(_A)
_ZyxelIgmpSnoopingCountEntry_Object=MibTableRow
zyxelIgmpSnoopingCountEntry=_ZyxelIgmpSnoopingCountEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1))
zyxelIgmpSnoopingCountEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:zyxelIgmpSnoopingCountEntry.setStatus(_A)
_ZyIgmpSnoopingCountIndex_Type=Integer32
_ZyIgmpSnoopingCountIndex_Object=MibTableColumn
zyIgmpSnoopingCountIndex=_ZyIgmpSnoopingCountIndex_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,1),_ZyIgmpSnoopingCountIndex_Type())
zyIgmpSnoopingCountIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingCountIndex.setStatus(_A)
_ZyIgmpSnoopingCountV2QueryRx_Type=Integer32
_ZyIgmpSnoopingCountV2QueryRx_Object=MibTableColumn
zyIgmpSnoopingCountV2QueryRx=_ZyIgmpSnoopingCountV2QueryRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,2),_ZyIgmpSnoopingCountV2QueryRx_Type())
zyIgmpSnoopingCountV2QueryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2QueryRx.setStatus(_A)
_ZyIgmpSnoopingCountV2ReportRx_Type=Integer32
_ZyIgmpSnoopingCountV2ReportRx_Object=MibTableColumn
zyIgmpSnoopingCountV2ReportRx=_ZyIgmpSnoopingCountV2ReportRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,3),_ZyIgmpSnoopingCountV2ReportRx_Type())
zyIgmpSnoopingCountV2ReportRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2ReportRx.setStatus(_A)
_ZyIgmpSnoopingCountV2LeaveRx_Type=Integer32
_ZyIgmpSnoopingCountV2LeaveRx_Object=MibTableColumn
zyIgmpSnoopingCountV2LeaveRx=_ZyIgmpSnoopingCountV2LeaveRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,4),_ZyIgmpSnoopingCountV2LeaveRx_Type())
zyIgmpSnoopingCountV2LeaveRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2LeaveRx.setStatus(_A)
_ZyIgmpSnoopingCountV2QueryRxDrop_Type=Integer32
_ZyIgmpSnoopingCountV2QueryRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountV2QueryRxDrop=_ZyIgmpSnoopingCountV2QueryRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,5),_ZyIgmpSnoopingCountV2QueryRxDrop_Type())
zyIgmpSnoopingCountV2QueryRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2QueryRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountV2ReportRxDrop_Type=Integer32
_ZyIgmpSnoopingCountV2ReportRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountV2ReportRxDrop=_ZyIgmpSnoopingCountV2ReportRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,6),_ZyIgmpSnoopingCountV2ReportRxDrop_Type())
zyIgmpSnoopingCountV2ReportRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2ReportRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountV2LeaveRxDrop_Type=Integer32
_ZyIgmpSnoopingCountV2LeaveRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountV2LeaveRxDrop=_ZyIgmpSnoopingCountV2LeaveRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,7),_ZyIgmpSnoopingCountV2LeaveRxDrop_Type())
zyIgmpSnoopingCountV2LeaveRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2LeaveRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountV2QueryTx_Type=Integer32
_ZyIgmpSnoopingCountV2QueryTx_Object=MibTableColumn
zyIgmpSnoopingCountV2QueryTx=_ZyIgmpSnoopingCountV2QueryTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,8),_ZyIgmpSnoopingCountV2QueryTx_Type())
zyIgmpSnoopingCountV2QueryTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2QueryTx.setStatus(_A)
_ZyIgmpSnoopingCountV2ReportTx_Type=Integer32
_ZyIgmpSnoopingCountV2ReportTx_Object=MibTableColumn
zyIgmpSnoopingCountV2ReportTx=_ZyIgmpSnoopingCountV2ReportTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,9),_ZyIgmpSnoopingCountV2ReportTx_Type())
zyIgmpSnoopingCountV2ReportTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2ReportTx.setStatus(_A)
_ZyIgmpSnoopingCountV2LeaveTx_Type=Integer32
_ZyIgmpSnoopingCountV2LeaveTx_Object=MibTableColumn
zyIgmpSnoopingCountV2LeaveTx=_ZyIgmpSnoopingCountV2LeaveTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,10),_ZyIgmpSnoopingCountV2LeaveTx_Type())
zyIgmpSnoopingCountV2LeaveTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV2LeaveTx.setStatus(_A)
_ZyIgmpSnoopingCountV3QueryRx_Type=Integer32
_ZyIgmpSnoopingCountV3QueryRx_Object=MibTableColumn
zyIgmpSnoopingCountV3QueryRx=_ZyIgmpSnoopingCountV3QueryRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,11),_ZyIgmpSnoopingCountV3QueryRx_Type())
zyIgmpSnoopingCountV3QueryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV3QueryRx.setStatus(_A)
_ZyIgmpSnoopingCountV3ReportRx_Type=Integer32
_ZyIgmpSnoopingCountV3ReportRx_Object=MibTableColumn
zyIgmpSnoopingCountV3ReportRx=_ZyIgmpSnoopingCountV3ReportRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,12),_ZyIgmpSnoopingCountV3ReportRx_Type())
zyIgmpSnoopingCountV3ReportRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV3ReportRx.setStatus(_A)
_ZyIgmpSnoopingCountV3QueryRxDrop_Type=Integer32
_ZyIgmpSnoopingCountV3QueryRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountV3QueryRxDrop=_ZyIgmpSnoopingCountV3QueryRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,13),_ZyIgmpSnoopingCountV3QueryRxDrop_Type())
zyIgmpSnoopingCountV3QueryRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV3QueryRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountV3ReportRxDrop_Type=Integer32
_ZyIgmpSnoopingCountV3ReportRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountV3ReportRxDrop=_ZyIgmpSnoopingCountV3ReportRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,14),_ZyIgmpSnoopingCountV3ReportRxDrop_Type())
zyIgmpSnoopingCountV3ReportRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV3ReportRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountV3QueryTx_Type=Integer32
_ZyIgmpSnoopingCountV3QueryTx_Object=MibTableColumn
zyIgmpSnoopingCountV3QueryTx=_ZyIgmpSnoopingCountV3QueryTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,15),_ZyIgmpSnoopingCountV3QueryTx_Type())
zyIgmpSnoopingCountV3QueryTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV3QueryTx.setStatus(_A)
_ZyIgmpSnoopingCountV3ReportTx_Type=Integer32
_ZyIgmpSnoopingCountV3ReportTx_Object=MibTableColumn
zyIgmpSnoopingCountV3ReportTx=_ZyIgmpSnoopingCountV3ReportTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,3,1,16),_ZyIgmpSnoopingCountV3ReportTx_Type())
zyIgmpSnoopingCountV3ReportTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountV3ReportTx.setStatus(_A)
_ZyxelIgmpSnoopingCountVlanTable_Object=MibTable
zyxelIgmpSnoopingCountVlanTable=_ZyxelIgmpSnoopingCountVlanTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,4))
if mibBuilder.loadTexts:zyxelIgmpSnoopingCountVlanTable.setStatus(_A)
_ZyxelIgmpSnoopingCountVlanEntry_Object=MibTableRow
zyxelIgmpSnoopingCountVlanEntry=_ZyxelIgmpSnoopingCountVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1))
zyxelIgmpSnoopingCountVlanEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:zyxelIgmpSnoopingCountVlanEntry.setStatus(_A)
_ZyIgmpSnoopingCountVlanVid_Type=Integer32
_ZyIgmpSnoopingCountVlanVid_Object=MibTableColumn
zyIgmpSnoopingCountVlanVid=_ZyIgmpSnoopingCountVlanVid_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,1),_ZyIgmpSnoopingCountVlanVid_Type())
zyIgmpSnoopingCountVlanVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanVid.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2QueryRx_Type=Integer32
_ZyIgmpSnoopingCountVlanV2QueryRx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2QueryRx=_ZyIgmpSnoopingCountVlanV2QueryRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,2),_ZyIgmpSnoopingCountVlanV2QueryRx_Type())
zyIgmpSnoopingCountVlanV2QueryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2QueryRx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2ReportRx_Type=Integer32
_ZyIgmpSnoopingCountVlanV2ReportRx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2ReportRx=_ZyIgmpSnoopingCountVlanV2ReportRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,3),_ZyIgmpSnoopingCountVlanV2ReportRx_Type())
zyIgmpSnoopingCountVlanV2ReportRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2ReportRx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2LeaveRx_Type=Integer32
_ZyIgmpSnoopingCountVlanV2LeaveRx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2LeaveRx=_ZyIgmpSnoopingCountVlanV2LeaveRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,4),_ZyIgmpSnoopingCountVlanV2LeaveRx_Type())
zyIgmpSnoopingCountVlanV2LeaveRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2LeaveRx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2QueryRxDrop_Type=Integer32
_ZyIgmpSnoopingCountVlanV2QueryRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2QueryRxDrop=_ZyIgmpSnoopingCountVlanV2QueryRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,5),_ZyIgmpSnoopingCountVlanV2QueryRxDrop_Type())
zyIgmpSnoopingCountVlanV2QueryRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2QueryRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2ReportRxDrop_Type=Integer32
_ZyIgmpSnoopingCountVlanV2ReportRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2ReportRxDrop=_ZyIgmpSnoopingCountVlanV2ReportRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,6),_ZyIgmpSnoopingCountVlanV2ReportRxDrop_Type())
zyIgmpSnoopingCountVlanV2ReportRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2ReportRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Type=Integer32
_ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2LeaveRxDrop=_ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,7),_ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Type())
zyIgmpSnoopingCountVlanV2LeaveRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2LeaveRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2QueryTx_Type=Integer32
_ZyIgmpSnoopingCountVlanV2QueryTx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2QueryTx=_ZyIgmpSnoopingCountVlanV2QueryTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,8),_ZyIgmpSnoopingCountVlanV2QueryTx_Type())
zyIgmpSnoopingCountVlanV2QueryTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2QueryTx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2ReportTx_Type=Integer32
_ZyIgmpSnoopingCountVlanV2ReportTx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2ReportTx=_ZyIgmpSnoopingCountVlanV2ReportTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,9),_ZyIgmpSnoopingCountVlanV2ReportTx_Type())
zyIgmpSnoopingCountVlanV2ReportTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2ReportTx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV2LeaveTx_Type=Integer32
_ZyIgmpSnoopingCountVlanV2LeaveTx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV2LeaveTx=_ZyIgmpSnoopingCountVlanV2LeaveTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,10),_ZyIgmpSnoopingCountVlanV2LeaveTx_Type())
zyIgmpSnoopingCountVlanV2LeaveTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV2LeaveTx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV3QueryRx_Type=Integer32
_ZyIgmpSnoopingCountVlanV3QueryRx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV3QueryRx=_ZyIgmpSnoopingCountVlanV3QueryRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,11),_ZyIgmpSnoopingCountVlanV3QueryRx_Type())
zyIgmpSnoopingCountVlanV3QueryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV3QueryRx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV3ReportRx_Type=Integer32
_ZyIgmpSnoopingCountVlanV3ReportRx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV3ReportRx=_ZyIgmpSnoopingCountVlanV3ReportRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,12),_ZyIgmpSnoopingCountVlanV3ReportRx_Type())
zyIgmpSnoopingCountVlanV3ReportRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV3ReportRx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV3QueryRxDrop_Type=Integer32
_ZyIgmpSnoopingCountVlanV3QueryRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountVlanV3QueryRxDrop=_ZyIgmpSnoopingCountVlanV3QueryRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,13),_ZyIgmpSnoopingCountVlanV3QueryRxDrop_Type())
zyIgmpSnoopingCountVlanV3QueryRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV3QueryRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountVlanV3ReportRxDrop_Type=Integer32
_ZyIgmpSnoopingCountVlanV3ReportRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountVlanV3ReportRxDrop=_ZyIgmpSnoopingCountVlanV3ReportRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,14),_ZyIgmpSnoopingCountVlanV3ReportRxDrop_Type())
zyIgmpSnoopingCountVlanV3ReportRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV3ReportRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountVlanV3QueryTx_Type=Integer32
_ZyIgmpSnoopingCountVlanV3QueryTx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV3QueryTx=_ZyIgmpSnoopingCountVlanV3QueryTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,15),_ZyIgmpSnoopingCountVlanV3QueryTx_Type())
zyIgmpSnoopingCountVlanV3QueryTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV3QueryTx.setStatus(_A)
_ZyIgmpSnoopingCountVlanV3ReportTx_Type=Integer32
_ZyIgmpSnoopingCountVlanV3ReportTx_Object=MibTableColumn
zyIgmpSnoopingCountVlanV3ReportTx=_ZyIgmpSnoopingCountVlanV3ReportTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,4,1,16),_ZyIgmpSnoopingCountVlanV3ReportTx_Type())
zyIgmpSnoopingCountVlanV3ReportTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountVlanV3ReportTx.setStatus(_A)
_ZyxelIgmpSnoopingCountPortTable_Object=MibTable
zyxelIgmpSnoopingCountPortTable=_ZyxelIgmpSnoopingCountPortTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,5))
if mibBuilder.loadTexts:zyxelIgmpSnoopingCountPortTable.setStatus(_A)
_ZyxelIgmpSnoopingCountPortEntry_Object=MibTableRow
zyxelIgmpSnoopingCountPortEntry=_ZyxelIgmpSnoopingCountPortEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1))
zyxelIgmpSnoopingCountPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelIgmpSnoopingCountPortEntry.setStatus(_A)
_ZyIgmpSnoopingCountPortV2QueryRx_Type=Integer32
_ZyIgmpSnoopingCountPortV2QueryRx_Object=MibTableColumn
zyIgmpSnoopingCountPortV2QueryRx=_ZyIgmpSnoopingCountPortV2QueryRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,1),_ZyIgmpSnoopingCountPortV2QueryRx_Type())
zyIgmpSnoopingCountPortV2QueryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2QueryRx.setStatus(_A)
_ZyIgmpSnoopingCountPortV2ReportRx_Type=Integer32
_ZyIgmpSnoopingCountPortV2ReportRx_Object=MibTableColumn
zyIgmpSnoopingCountPortV2ReportRx=_ZyIgmpSnoopingCountPortV2ReportRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,2),_ZyIgmpSnoopingCountPortV2ReportRx_Type())
zyIgmpSnoopingCountPortV2ReportRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2ReportRx.setStatus(_A)
_ZyIgmpSnoopingCountPortV2LeaveRx_Type=Integer32
_ZyIgmpSnoopingCountPortV2LeaveRx_Object=MibTableColumn
zyIgmpSnoopingCountPortV2LeaveRx=_ZyIgmpSnoopingCountPortV2LeaveRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,3),_ZyIgmpSnoopingCountPortV2LeaveRx_Type())
zyIgmpSnoopingCountPortV2LeaveRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2LeaveRx.setStatus(_A)
_ZyIgmpSnoopingCountPortV2ReportRxDrop_Type=Integer32
_ZyIgmpSnoopingCountPortV2ReportRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountPortV2ReportRxDrop=_ZyIgmpSnoopingCountPortV2ReportRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,4),_ZyIgmpSnoopingCountPortV2ReportRxDrop_Type())
zyIgmpSnoopingCountPortV2ReportRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2ReportRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountPortV2LeaveRxDrop_Type=Integer32
_ZyIgmpSnoopingCountPortV2LeaveRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountPortV2LeaveRxDrop=_ZyIgmpSnoopingCountPortV2LeaveRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,5),_ZyIgmpSnoopingCountPortV2LeaveRxDrop_Type())
zyIgmpSnoopingCountPortV2LeaveRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2LeaveRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountPortV2ReportTx_Type=Integer32
_ZyIgmpSnoopingCountPortV2ReportTx_Object=MibTableColumn
zyIgmpSnoopingCountPortV2ReportTx=_ZyIgmpSnoopingCountPortV2ReportTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,6),_ZyIgmpSnoopingCountPortV2ReportTx_Type())
zyIgmpSnoopingCountPortV2ReportTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2ReportTx.setStatus(_A)
_ZyIgmpSnoopingCountPortV2LeaveTx_Type=Integer32
_ZyIgmpSnoopingCountPortV2LeaveTx_Object=MibTableColumn
zyIgmpSnoopingCountPortV2LeaveTx=_ZyIgmpSnoopingCountPortV2LeaveTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,7),_ZyIgmpSnoopingCountPortV2LeaveTx_Type())
zyIgmpSnoopingCountPortV2LeaveTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV2LeaveTx.setStatus(_A)
_ZyIgmpSnoopingCountPortV3QueryRx_Type=Integer32
_ZyIgmpSnoopingCountPortV3QueryRx_Object=MibTableColumn
zyIgmpSnoopingCountPortV3QueryRx=_ZyIgmpSnoopingCountPortV3QueryRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,8),_ZyIgmpSnoopingCountPortV3QueryRx_Type())
zyIgmpSnoopingCountPortV3QueryRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV3QueryRx.setStatus(_A)
_ZyIgmpSnoopingCountPortV3ReportRx_Type=Integer32
_ZyIgmpSnoopingCountPortV3ReportRx_Object=MibTableColumn
zyIgmpSnoopingCountPortV3ReportRx=_ZyIgmpSnoopingCountPortV3ReportRx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,9),_ZyIgmpSnoopingCountPortV3ReportRx_Type())
zyIgmpSnoopingCountPortV3ReportRx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV3ReportRx.setStatus(_A)
_ZyIgmpSnoopingCountPortV3ReportRxDrop_Type=Integer32
_ZyIgmpSnoopingCountPortV3ReportRxDrop_Object=MibTableColumn
zyIgmpSnoopingCountPortV3ReportRxDrop=_ZyIgmpSnoopingCountPortV3ReportRxDrop_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,10),_ZyIgmpSnoopingCountPortV3ReportRxDrop_Type())
zyIgmpSnoopingCountPortV3ReportRxDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV3ReportRxDrop.setStatus(_A)
_ZyIgmpSnoopingCountPortV3ReportTx_Type=Integer32
_ZyIgmpSnoopingCountPortV3ReportTx_Object=MibTableColumn
zyIgmpSnoopingCountPortV3ReportTx=_ZyIgmpSnoopingCountPortV3ReportTx_Object((1,3,6,1,4,1,890,1,15,3,31,2,5,1,11),_ZyIgmpSnoopingCountPortV3ReportTx_Type())
zyIgmpSnoopingCountPortV3ReportTx.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingCountPortV3ReportTx.setStatus(_A)
_ZyxelIgmpSnoopingGroupCountStatus_ObjectIdentity=ObjectIdentity
zyxelIgmpSnoopingGroupCountStatus=_ZyxelIgmpSnoopingGroupCountStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,31,2,6))
_ZyIgmpSnoopingGroupCountNumber_Type=Integer32
_ZyIgmpSnoopingGroupCountNumber_Object=MibScalar
zyIgmpSnoopingGroupCountNumber=_ZyIgmpSnoopingGroupCountNumber_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,1),_ZyIgmpSnoopingGroupCountNumber_Type())
zyIgmpSnoopingGroupCountNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupCountNumber.setStatus(_A)
_ZyxelIgmpSnoopingGroupCountVlanTable_Object=MibTable
zyxelIgmpSnoopingGroupCountVlanTable=_ZyxelIgmpSnoopingGroupCountVlanTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,2))
if mibBuilder.loadTexts:zyxelIgmpSnoopingGroupCountVlanTable.setStatus(_A)
_ZyxelIgmpSnoopingGroupCountVlanEntry_Object=MibTableRow
zyxelIgmpSnoopingGroupCountVlanEntry=_ZyxelIgmpSnoopingGroupCountVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,2,1))
zyxelIgmpSnoopingGroupCountVlanEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:zyxelIgmpSnoopingGroupCountVlanEntry.setStatus(_A)
_ZyIgmpSnoopingGroupCountVlanVid_Type=Integer32
_ZyIgmpSnoopingGroupCountVlanVid_Object=MibTableColumn
zyIgmpSnoopingGroupCountVlanVid=_ZyIgmpSnoopingGroupCountVlanVid_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,2,1,1),_ZyIgmpSnoopingGroupCountVlanVid_Type())
zyIgmpSnoopingGroupCountVlanVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupCountVlanVid.setStatus(_A)
_ZyIgmpSnoopingGroupCountVlanNumber_Type=Integer32
_ZyIgmpSnoopingGroupCountVlanNumber_Object=MibTableColumn
zyIgmpSnoopingGroupCountVlanNumber=_ZyIgmpSnoopingGroupCountVlanNumber_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,2,1,2),_ZyIgmpSnoopingGroupCountVlanNumber_Type())
zyIgmpSnoopingGroupCountVlanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupCountVlanNumber.setStatus(_A)
_ZyxelIgmpSnoopingGroupCountPortTable_Object=MibTable
zyxelIgmpSnoopingGroupCountPortTable=_ZyxelIgmpSnoopingGroupCountPortTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,3))
if mibBuilder.loadTexts:zyxelIgmpSnoopingGroupCountPortTable.setStatus(_A)
_ZyxelIgmpSnoopingGroupCountPortEntry_Object=MibTableRow
zyxelIgmpSnoopingGroupCountPortEntry=_ZyxelIgmpSnoopingGroupCountPortEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,3,1))
zyxelIgmpSnoopingGroupCountPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelIgmpSnoopingGroupCountPortEntry.setStatus(_A)
_ZyIgmpSnoopingGroupCountPortNumber_Type=Integer32
_ZyIgmpSnoopingGroupCountPortNumber_Object=MibTableColumn
zyIgmpSnoopingGroupCountPortNumber=_ZyIgmpSnoopingGroupCountPortNumber_Object((1,3,6,1,4,1,890,1,15,3,31,2,6,3,1,1),_ZyIgmpSnoopingGroupCountPortNumber_Type())
zyIgmpSnoopingGroupCountPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupCountPortNumber.setStatus(_A)
_ZyxelIgmpSnoopingGroupStatus_ObjectIdentity=ObjectIdentity
zyxelIgmpSnoopingGroupStatus=_ZyxelIgmpSnoopingGroupStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,31,2,7))
_ZyxelIgmpSnoopingGroupTable_Object=MibTable
zyxelIgmpSnoopingGroupTable=_ZyxelIgmpSnoopingGroupTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,7,1))
if mibBuilder.loadTexts:zyxelIgmpSnoopingGroupTable.setStatus(_A)
_ZyxelIgmpSnoopingGroupEntry_Object=MibTableRow
zyxelIgmpSnoopingGroupEntry=_ZyxelIgmpSnoopingGroupEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,7,1,1))
zyxelIgmpSnoopingGroupEntry.setIndexNames((0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:zyxelIgmpSnoopingGroupEntry.setStatus(_A)
_ZyIgmpSnoopingGroupVid_Type=Integer32
_ZyIgmpSnoopingGroupVid_Object=MibTableColumn
zyIgmpSnoopingGroupVid=_ZyIgmpSnoopingGroupVid_Object((1,3,6,1,4,1,890,1,15,3,31,2,7,1,1,1),_ZyIgmpSnoopingGroupVid_Type())
zyIgmpSnoopingGroupVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupVid.setStatus(_A)
_ZyIgmpSnoopingGroupIpAddress_Type=IpAddress
_ZyIgmpSnoopingGroupIpAddress_Object=MibTableColumn
zyIgmpSnoopingGroupIpAddress=_ZyIgmpSnoopingGroupIpAddress_Object((1,3,6,1,4,1,890,1,15,3,31,2,7,1,1,2),_ZyIgmpSnoopingGroupIpAddress_Type())
zyIgmpSnoopingGroupIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupIpAddress.setStatus(_A)
_ZyIgmpSnoopingGroupPortCount_Type=Integer32
_ZyIgmpSnoopingGroupPortCount_Object=MibTableColumn
zyIgmpSnoopingGroupPortCount=_ZyIgmpSnoopingGroupPortCount_Object((1,3,6,1,4,1,890,1,15,3,31,2,7,1,1,3),_ZyIgmpSnoopingGroupPortCount_Type())
zyIgmpSnoopingGroupPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupPortCount.setStatus(_A)
_ZyIgmpSnoopingGroupPorts_Type=PortList
_ZyIgmpSnoopingGroupPorts_Object=MibTableColumn
zyIgmpSnoopingGroupPorts=_ZyIgmpSnoopingGroupPorts_Object((1,3,6,1,4,1,890,1,15,3,31,2,7,1,1,4),_ZyIgmpSnoopingGroupPorts_Type())
zyIgmpSnoopingGroupPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingGroupPorts.setStatus(_A)
_ZyxelIgmpSnoopingClientTable_Object=MibTable
zyxelIgmpSnoopingClientTable=_ZyxelIgmpSnoopingClientTable_Object((1,3,6,1,4,1,890,1,15,3,31,2,8))
if mibBuilder.loadTexts:zyxelIgmpSnoopingClientTable.setStatus(_A)
_ZyxelIgmpSnoopingClientEntry_Object=MibTableRow
zyxelIgmpSnoopingClientEntry=_ZyxelIgmpSnoopingClientEntry_Object((1,3,6,1,4,1,890,1,15,3,31,2,8,1))
zyxelIgmpSnoopingClientEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:zyxelIgmpSnoopingClientEntry.setStatus(_A)
_ZyIgmpSnoopingClientVid_Type=Integer32
_ZyIgmpSnoopingClientVid_Object=MibTableColumn
zyIgmpSnoopingClientVid=_ZyIgmpSnoopingClientVid_Object((1,3,6,1,4,1,890,1,15,3,31,2,8,1,1),_ZyIgmpSnoopingClientVid_Type())
zyIgmpSnoopingClientVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingClientVid.setStatus(_A)
_ZyIgmpSnoopingClientPort_Type=Integer32
_ZyIgmpSnoopingClientPort_Object=MibTableColumn
zyIgmpSnoopingClientPort=_ZyIgmpSnoopingClientPort_Object((1,3,6,1,4,1,890,1,15,3,31,2,8,1,2),_ZyIgmpSnoopingClientPort_Type())
zyIgmpSnoopingClientPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingClientPort.setStatus(_A)
_ZyIgmpSnoopingClientGroupIpAddress_Type=IpAddress
_ZyIgmpSnoopingClientGroupIpAddress_Object=MibTableColumn
zyIgmpSnoopingClientGroupIpAddress=_ZyIgmpSnoopingClientGroupIpAddress_Object((1,3,6,1,4,1,890,1,15,3,31,2,8,1,3),_ZyIgmpSnoopingClientGroupIpAddress_Type())
zyIgmpSnoopingClientGroupIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingClientGroupIpAddress.setStatus(_A)
_ZyIgmpSnoopingClientIpAddress_Type=IpAddress
_ZyIgmpSnoopingClientIpAddress_Object=MibTableColumn
zyIgmpSnoopingClientIpAddress=_ZyIgmpSnoopingClientIpAddress_Object((1,3,6,1,4,1,890,1,15,3,31,2,8,1,4),_ZyIgmpSnoopingClientIpAddress_Type())
zyIgmpSnoopingClientIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIgmpSnoopingClientIpAddress.setStatus(_A)
_ZyIgmpSnoopingClientUpTime_Type=Integer32
_ZyIgmpSnoopingClientUpTime_Object=MibTableColumn
zyIgmpSnoopingClientUpTime=_ZyIgmpSnoopingClientUpTime_Object((1,3,6,1,4,1,890,1,15,3,31,2,8,1,5),_ZyIgmpSnoopingClientUpTime_Type())
zyIgmpSnoopingClientUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyIgmpSnoopingClientUpTime.setStatus(_A)
_ZyIgmpSnoopingStatisticsClear_Type=EnabledStatus
_ZyIgmpSnoopingStatisticsClear_Object=MibScalar
zyIgmpSnoopingStatisticsClear=_ZyIgmpSnoopingStatisticsClear_Object((1,3,6,1,4,1,890,1,15,3,31,2,9),_ZyIgmpSnoopingStatisticsClear_Type())
zyIgmpSnoopingStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingStatisticsClear.setStatus(_A)
_ZyIgmpSnoopingStatisticsClearSystem_Type=EnabledStatus
_ZyIgmpSnoopingStatisticsClearSystem_Object=MibScalar
zyIgmpSnoopingStatisticsClearSystem=_ZyIgmpSnoopingStatisticsClearSystem_Object((1,3,6,1,4,1,890,1,15,3,31,2,10),_ZyIgmpSnoopingStatisticsClearSystem_Type())
zyIgmpSnoopingStatisticsClearSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingStatisticsClearSystem.setStatus(_A)
_ZyIgmpSnoopingStatisticsClearPort_Type=EnabledStatus
_ZyIgmpSnoopingStatisticsClearPort_Object=MibScalar
zyIgmpSnoopingStatisticsClearPort=_ZyIgmpSnoopingStatisticsClearPort_Object((1,3,6,1,4,1,890,1,15,3,31,2,11),_ZyIgmpSnoopingStatisticsClearPort_Type())
zyIgmpSnoopingStatisticsClearPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingStatisticsClearPort.setStatus(_A)
_ZyIgmpSnoopingStatisticsClearVlan_Type=EnabledStatus
_ZyIgmpSnoopingStatisticsClearVlan_Object=MibScalar
zyIgmpSnoopingStatisticsClearVlan=_ZyIgmpSnoopingStatisticsClearVlan_Object((1,3,6,1,4,1,890,1,15,3,31,2,12),_ZyIgmpSnoopingStatisticsClearVlan_Type())
zyIgmpSnoopingStatisticsClearVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIgmpSnoopingStatisticsClearVlan.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelIgmpSnooping':zyxelIgmpSnooping,'zyxelIgmpSnoopingSetup':zyxelIgmpSnoopingSetup,'zyIgmpSnoopingState':zyIgmpSnoopingState,'zyIgmpSnoopingGroupHostTimeout':zyIgmpSnoopingGroupHostTimeout,'zyIgmpSnooping8021pPriority':zyIgmpSnooping8021pPriority,'zyIgmpSnoopingVlanMode':zyIgmpSnoopingVlanMode,'zyIgmpSnoopingMaxNumberOfVlans':zyIgmpSnoopingMaxNumberOfVlans,'zyxelIgmpSnoopingVlanTable':zyxelIgmpSnoopingVlanTable,'zyxelIgmpSnoopingVlanEntry':zyxelIgmpSnoopingVlanEntry,_I:zyIgmpSnoopingVlanVid,'zyIgmpSnoopingVlanName':zyIgmpSnoopingVlanName,'zyIgmpSnoopingVlanRowStatus':zyIgmpSnoopingVlanRowStatus,'zyIgmpSnoopingQuerierModeState':zyIgmpSnoopingQuerierModeState,'zyIgmpSnoopingReportProxyState':zyIgmpSnoopingReportProxyState,'zyxelIgmpSnoopingPortTable':zyxelIgmpSnoopingPortTable,'zyxelIgmpSnoopingPortEntry':zyxelIgmpSnoopingPortEntry,'zyIgmpSnoopingPortMaxGroupLimitedState':zyIgmpSnoopingPortMaxGroupLimitedState,'zyIgmpSnoopingPortMaxOfGroups':zyIgmpSnoopingPortMaxOfGroups,'zyIgmpSnoopingPortQuerierMode':zyIgmpSnoopingPortQuerierMode,'zyIgmpSnoopingPortThrottlingAction':zyIgmpSnoopingPortThrottlingAction,'zyIgmpSnoopingPortLeaveMode':zyIgmpSnoopingPortLeaveMode,'zyIgmpSnoopingPortLeaveTimeout':zyIgmpSnoopingPortLeaveTimeout,'zyIgmpSnoopingPortFastLeaveTimeout':zyIgmpSnoopingPortFastLeaveTimeout,'zyIgmpSnoopingQuerierVersion':zyIgmpSnoopingQuerierVersion,'zyIgmpSnoopingSmartForward':zyIgmpSnoopingSmartForward,'zyxelIgmpSnoopingStatus':zyxelIgmpSnoopingStatus,'zyxelIgmpSnoopingRecordTable':zyxelIgmpSnoopingRecordTable,'zyxelIgmpSnoopingRecordEntry':zyxelIgmpSnoopingRecordEntry,'zyIgmpSnoopingRecordIndex':zyIgmpSnoopingRecordIndex,_J:zyIgmpSnoopingRecordVid,_K:zyIgmpSnoopingRecordPort,_L:zyIgmpSnoopingRecordGroup,'zyIgmpSnoopingRecordTimeout':zyIgmpSnoopingRecordTimeout,'zyIgmpSnoopingRecordUpTime':zyIgmpSnoopingRecordUpTime,'zyxelIgmpSnoopingInfoVlanTable':zyxelIgmpSnoopingInfoVlanTable,'zyxelIgmpSnoopingInfoVlanEntry':zyxelIgmpSnoopingInfoVlanEntry,_M:zyIgmpSnoopingInfoVlanVid,'zyIgmpSnoopingInfoVlanType':zyIgmpSnoopingInfoVlanType,'zyIgmpSnoopingInfoVlanQueryPorts':zyIgmpSnoopingInfoVlanQueryPorts,'zyxelIgmpSnoopingCountTable':zyxelIgmpSnoopingCountTable,'zyxelIgmpSnoopingCountEntry':zyxelIgmpSnoopingCountEntry,_N:zyIgmpSnoopingCountIndex,'zyIgmpSnoopingCountV2QueryRx':zyIgmpSnoopingCountV2QueryRx,'zyIgmpSnoopingCountV2ReportRx':zyIgmpSnoopingCountV2ReportRx,'zyIgmpSnoopingCountV2LeaveRx':zyIgmpSnoopingCountV2LeaveRx,'zyIgmpSnoopingCountV2QueryRxDrop':zyIgmpSnoopingCountV2QueryRxDrop,'zyIgmpSnoopingCountV2ReportRxDrop':zyIgmpSnoopingCountV2ReportRxDrop,'zyIgmpSnoopingCountV2LeaveRxDrop':zyIgmpSnoopingCountV2LeaveRxDrop,'zyIgmpSnoopingCountV2QueryTx':zyIgmpSnoopingCountV2QueryTx,'zyIgmpSnoopingCountV2ReportTx':zyIgmpSnoopingCountV2ReportTx,'zyIgmpSnoopingCountV2LeaveTx':zyIgmpSnoopingCountV2LeaveTx,'zyIgmpSnoopingCountV3QueryRx':zyIgmpSnoopingCountV3QueryRx,'zyIgmpSnoopingCountV3ReportRx':zyIgmpSnoopingCountV3ReportRx,'zyIgmpSnoopingCountV3QueryRxDrop':zyIgmpSnoopingCountV3QueryRxDrop,'zyIgmpSnoopingCountV3ReportRxDrop':zyIgmpSnoopingCountV3ReportRxDrop,'zyIgmpSnoopingCountV3QueryTx':zyIgmpSnoopingCountV3QueryTx,'zyIgmpSnoopingCountV3ReportTx':zyIgmpSnoopingCountV3ReportTx,'zyxelIgmpSnoopingCountVlanTable':zyxelIgmpSnoopingCountVlanTable,'zyxelIgmpSnoopingCountVlanEntry':zyxelIgmpSnoopingCountVlanEntry,_O:zyIgmpSnoopingCountVlanVid,'zyIgmpSnoopingCountVlanV2QueryRx':zyIgmpSnoopingCountVlanV2QueryRx,'zyIgmpSnoopingCountVlanV2ReportRx':zyIgmpSnoopingCountVlanV2ReportRx,'zyIgmpSnoopingCountVlanV2LeaveRx':zyIgmpSnoopingCountVlanV2LeaveRx,'zyIgmpSnoopingCountVlanV2QueryRxDrop':zyIgmpSnoopingCountVlanV2QueryRxDrop,'zyIgmpSnoopingCountVlanV2ReportRxDrop':zyIgmpSnoopingCountVlanV2ReportRxDrop,'zyIgmpSnoopingCountVlanV2LeaveRxDrop':zyIgmpSnoopingCountVlanV2LeaveRxDrop,'zyIgmpSnoopingCountVlanV2QueryTx':zyIgmpSnoopingCountVlanV2QueryTx,'zyIgmpSnoopingCountVlanV2ReportTx':zyIgmpSnoopingCountVlanV2ReportTx,'zyIgmpSnoopingCountVlanV2LeaveTx':zyIgmpSnoopingCountVlanV2LeaveTx,'zyIgmpSnoopingCountVlanV3QueryRx':zyIgmpSnoopingCountVlanV3QueryRx,'zyIgmpSnoopingCountVlanV3ReportRx':zyIgmpSnoopingCountVlanV3ReportRx,'zyIgmpSnoopingCountVlanV3QueryRxDrop':zyIgmpSnoopingCountVlanV3QueryRxDrop,'zyIgmpSnoopingCountVlanV3ReportRxDrop':zyIgmpSnoopingCountVlanV3ReportRxDrop,'zyIgmpSnoopingCountVlanV3QueryTx':zyIgmpSnoopingCountVlanV3QueryTx,'zyIgmpSnoopingCountVlanV3ReportTx':zyIgmpSnoopingCountVlanV3ReportTx,'zyxelIgmpSnoopingCountPortTable':zyxelIgmpSnoopingCountPortTable,'zyxelIgmpSnoopingCountPortEntry':zyxelIgmpSnoopingCountPortEntry,'zyIgmpSnoopingCountPortV2QueryRx':zyIgmpSnoopingCountPortV2QueryRx,'zyIgmpSnoopingCountPortV2ReportRx':zyIgmpSnoopingCountPortV2ReportRx,'zyIgmpSnoopingCountPortV2LeaveRx':zyIgmpSnoopingCountPortV2LeaveRx,'zyIgmpSnoopingCountPortV2ReportRxDrop':zyIgmpSnoopingCountPortV2ReportRxDrop,'zyIgmpSnoopingCountPortV2LeaveRxDrop':zyIgmpSnoopingCountPortV2LeaveRxDrop,'zyIgmpSnoopingCountPortV2ReportTx':zyIgmpSnoopingCountPortV2ReportTx,'zyIgmpSnoopingCountPortV2LeaveTx':zyIgmpSnoopingCountPortV2LeaveTx,'zyIgmpSnoopingCountPortV3QueryRx':zyIgmpSnoopingCountPortV3QueryRx,'zyIgmpSnoopingCountPortV3ReportRx':zyIgmpSnoopingCountPortV3ReportRx,'zyIgmpSnoopingCountPortV3ReportRxDrop':zyIgmpSnoopingCountPortV3ReportRxDrop,'zyIgmpSnoopingCountPortV3ReportTx':zyIgmpSnoopingCountPortV3ReportTx,'zyxelIgmpSnoopingGroupCountStatus':zyxelIgmpSnoopingGroupCountStatus,'zyIgmpSnoopingGroupCountNumber':zyIgmpSnoopingGroupCountNumber,'zyxelIgmpSnoopingGroupCountVlanTable':zyxelIgmpSnoopingGroupCountVlanTable,'zyxelIgmpSnoopingGroupCountVlanEntry':zyxelIgmpSnoopingGroupCountVlanEntry,_P:zyIgmpSnoopingGroupCountVlanVid,'zyIgmpSnoopingGroupCountVlanNumber':zyIgmpSnoopingGroupCountVlanNumber,'zyxelIgmpSnoopingGroupCountPortTable':zyxelIgmpSnoopingGroupCountPortTable,'zyxelIgmpSnoopingGroupCountPortEntry':zyxelIgmpSnoopingGroupCountPortEntry,'zyIgmpSnoopingGroupCountPortNumber':zyIgmpSnoopingGroupCountPortNumber,'zyxelIgmpSnoopingGroupStatus':zyxelIgmpSnoopingGroupStatus,'zyxelIgmpSnoopingGroupTable':zyxelIgmpSnoopingGroupTable,'zyxelIgmpSnoopingGroupEntry':zyxelIgmpSnoopingGroupEntry,_Q:zyIgmpSnoopingGroupVid,_R:zyIgmpSnoopingGroupIpAddress,'zyIgmpSnoopingGroupPortCount':zyIgmpSnoopingGroupPortCount,'zyIgmpSnoopingGroupPorts':zyIgmpSnoopingGroupPorts,'zyxelIgmpSnoopingClientTable':zyxelIgmpSnoopingClientTable,'zyxelIgmpSnoopingClientEntry':zyxelIgmpSnoopingClientEntry,_S:zyIgmpSnoopingClientVid,_T:zyIgmpSnoopingClientPort,_U:zyIgmpSnoopingClientGroupIpAddress,_V:zyIgmpSnoopingClientIpAddress,'zyIgmpSnoopingClientUpTime':zyIgmpSnoopingClientUpTime,'zyIgmpSnoopingStatisticsClear':zyIgmpSnoopingStatisticsClear,'zyIgmpSnoopingStatisticsClearSystem':zyIgmpSnoopingStatisticsClearSystem,'zyIgmpSnoopingStatisticsClearPort':zyIgmpSnoopingStatisticsClearPort,'zyIgmpSnoopingStatisticsClearVlan':zyIgmpSnoopingStatisticsClearVlan})