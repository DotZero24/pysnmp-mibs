_c='raisecomIgmpFilterIpProfileRangeIndex'
_b='raisecomIgmpFilterIpProfileIndex'
_a='raisecomIgmpFilterPortVlanVlanIndex'
_Z='raisecomIgmpFilterPortVlanPortIndex'
_Y='replace'
_X='raisecomIgmpFilterPortIndex'
_W='raisecomIgmpFilterProfileIndex'
_V='raisecomIgmpVlanCopyGroup'
_U='raisecomIgmpVlanCopyGroupIpType'
_T='raisecomIgmpMvrGroup'
_S='raisecomIgmpMvrGroupIpType'
_R='raisecomIgmpPortStatisticsPortNum'
_Q='raisecomIgmpMemberMVlan'
_P='raisecomIgmpMemberGroup'
_O='raisecomIgmpMemberGroupIpType'
_N='raisecomIgmpMemberUserVlan'
_M='raisecomIgmpMemberPort'
_L='raisecomIgmpMrouterVlan'
_K='raisecomIgmpMrouterPort'
_J='raisecomIgmpImmediateLeavePort'
_I='InetAddressType'
_H='EnableVar'
_G='not-accessible'
_F='read-write'
_E='RAISECOM-IGMPL2-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_I)
VlanId,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','VlanIndex')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,PortList,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_H,'PortList','Vlanset')
raisecomIgmpL2=ModuleIdentity((1,3,6,1,4,1,8886,1,28))
_RaisecomIgmpL2Notifications_ObjectIdentity=ObjectIdentity
raisecomIgmpL2Notifications=_RaisecomIgmpL2Notifications_ObjectIdentity((1,3,6,1,4,1,8886,1,28,1))
_RaisecomIgmpL2Objects_ObjectIdentity=ObjectIdentity
raisecomIgmpL2Objects=_RaisecomIgmpL2Objects_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2))
_RaisecomIgmpBase_ObjectIdentity=ObjectIdentity
raisecomIgmpBase=_RaisecomIgmpBase_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,1))
_RaisecomIgmpBaseScalar_ObjectIdentity=ObjectIdentity
raisecomIgmpBaseScalar=_RaisecomIgmpBaseScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,1,1))
class _RaisecomIgmpAging_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_RaisecomIgmpAging_Type.__name__=_D
_RaisecomIgmpAging_Object=MibScalar
raisecomIgmpAging=_RaisecomIgmpAging_Object((1,3,6,1,4,1,8886,1,28,2,1,1,1),_RaisecomIgmpAging_Type())
raisecomIgmpAging.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpAging.setStatus(_A)
_RaisecomIgmpRingPortList_Type=PortList
_RaisecomIgmpRingPortList_Object=MibScalar
raisecomIgmpRingPortList=_RaisecomIgmpRingPortList_Object((1,3,6,1,4,1,8886,1,28,2,1,1,2),_RaisecomIgmpRingPortList_Type())
raisecomIgmpRingPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpRingPortList.setStatus(_A)
_RaisecomIgmpImmediateLeaveTable_Object=MibTable
raisecomIgmpImmediateLeaveTable=_RaisecomIgmpImmediateLeaveTable_Object((1,3,6,1,4,1,8886,1,28,2,1,2))
if mibBuilder.loadTexts:raisecomIgmpImmediateLeaveTable.setStatus(_A)
_RaisecomIgmpImmediateLeaveEntry_Object=MibTableRow
raisecomIgmpImmediateLeaveEntry=_RaisecomIgmpImmediateLeaveEntry_Object((1,3,6,1,4,1,8886,1,28,2,1,2,1))
raisecomIgmpImmediateLeaveEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:raisecomIgmpImmediateLeaveEntry.setStatus(_A)
_RaisecomIgmpImmediateLeavePort_Type=Integer32
_RaisecomIgmpImmediateLeavePort_Object=MibTableColumn
raisecomIgmpImmediateLeavePort=_RaisecomIgmpImmediateLeavePort_Object((1,3,6,1,4,1,8886,1,28,2,1,2,1,1),_RaisecomIgmpImmediateLeavePort_Type())
raisecomIgmpImmediateLeavePort.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpImmediateLeavePort.setStatus(_A)
_RaisecomIgmpImmediateLeaveType_Type=Integer32
_RaisecomIgmpImmediateLeaveType_Object=MibTableColumn
raisecomIgmpImmediateLeaveType=_RaisecomIgmpImmediateLeaveType_Object((1,3,6,1,4,1,8886,1,28,2,1,2,1,2),_RaisecomIgmpImmediateLeaveType_Type())
raisecomIgmpImmediateLeaveType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpImmediateLeaveType.setStatus(_A)
_RaisecomIgmpImmediateLeaveVlanList_Type=Vlanset
_RaisecomIgmpImmediateLeaveVlanList_Object=MibTableColumn
raisecomIgmpImmediateLeaveVlanList=_RaisecomIgmpImmediateLeaveVlanList_Object((1,3,6,1,4,1,8886,1,28,2,1,2,1,3),_RaisecomIgmpImmediateLeaveVlanList_Type())
raisecomIgmpImmediateLeaveVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpImmediateLeaveVlanList.setStatus(_A)
_RaisecomIgmpImmediateLeaveRowStatus_Type=RowStatus
_RaisecomIgmpImmediateLeaveRowStatus_Object=MibTableColumn
raisecomIgmpImmediateLeaveRowStatus=_RaisecomIgmpImmediateLeaveRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,1,2,1,4),_RaisecomIgmpImmediateLeaveRowStatus_Type())
raisecomIgmpImmediateLeaveRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpImmediateLeaveRowStatus.setStatus(_A)
_RaisecomIgmpMrouterTable_Object=MibTable
raisecomIgmpMrouterTable=_RaisecomIgmpMrouterTable_Object((1,3,6,1,4,1,8886,1,28,2,1,3))
if mibBuilder.loadTexts:raisecomIgmpMrouterTable.setStatus(_A)
_RaisecomIgmpMrouterEntry_Object=MibTableRow
raisecomIgmpMrouterEntry=_RaisecomIgmpMrouterEntry_Object((1,3,6,1,4,1,8886,1,28,2,1,3,1))
raisecomIgmpMrouterEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:raisecomIgmpMrouterEntry.setStatus(_A)
_RaisecomIgmpMrouterPort_Type=Integer32
_RaisecomIgmpMrouterPort_Object=MibTableColumn
raisecomIgmpMrouterPort=_RaisecomIgmpMrouterPort_Object((1,3,6,1,4,1,8886,1,28,2,1,3,1,1),_RaisecomIgmpMrouterPort_Type())
raisecomIgmpMrouterPort.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMrouterPort.setStatus(_A)
_RaisecomIgmpMrouterVlan_Type=VlanIndex
_RaisecomIgmpMrouterVlan_Object=MibTableColumn
raisecomIgmpMrouterVlan=_RaisecomIgmpMrouterVlan_Object((1,3,6,1,4,1,8886,1,28,2,1,3,1,2),_RaisecomIgmpMrouterVlan_Type())
raisecomIgmpMrouterVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMrouterVlan.setStatus(_A)
class _RaisecomIgmpMrouterLiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_RaisecomIgmpMrouterLiveTime_Type.__name__=_D
_RaisecomIgmpMrouterLiveTime_Object=MibTableColumn
raisecomIgmpMrouterLiveTime=_RaisecomIgmpMrouterLiveTime_Object((1,3,6,1,4,1,8886,1,28,2,1,3,1,3),_RaisecomIgmpMrouterLiveTime_Type())
raisecomIgmpMrouterLiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpMrouterLiveTime.setStatus(_A)
_RaisecomIgmpMrouterMRStatus_Type=Integer32
_RaisecomIgmpMrouterMRStatus_Object=MibTableColumn
raisecomIgmpMrouterMRStatus=_RaisecomIgmpMrouterMRStatus_Object((1,3,6,1,4,1,8886,1,28,2,1,3,1,4),_RaisecomIgmpMrouterMRStatus_Type())
raisecomIgmpMrouterMRStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpMrouterMRStatus.setStatus(_A)
_RaisecomIgmpMrouterRowStatus_Type=RowStatus
_RaisecomIgmpMrouterRowStatus_Object=MibTableColumn
raisecomIgmpMrouterRowStatus=_RaisecomIgmpMrouterRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,1,3,1,5),_RaisecomIgmpMrouterRowStatus_Type())
raisecomIgmpMrouterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpMrouterRowStatus.setStatus(_A)
_RaisecomIgmpMemberTable_Object=MibTable
raisecomIgmpMemberTable=_RaisecomIgmpMemberTable_Object((1,3,6,1,4,1,8886,1,28,2,1,4))
if mibBuilder.loadTexts:raisecomIgmpMemberTable.setStatus(_A)
_RaisecomIgmpMemberEntry_Object=MibTableRow
raisecomIgmpMemberEntry=_RaisecomIgmpMemberEntry_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1))
raisecomIgmpMemberEntry.setIndexNames((0,_E,_M),(0,_E,_N),(0,_E,_O),(0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:raisecomIgmpMemberEntry.setStatus(_A)
_RaisecomIgmpMemberPort_Type=Integer32
_RaisecomIgmpMemberPort_Object=MibTableColumn
raisecomIgmpMemberPort=_RaisecomIgmpMemberPort_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,1),_RaisecomIgmpMemberPort_Type())
raisecomIgmpMemberPort.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMemberPort.setStatus(_A)
_RaisecomIgmpMemberUserVlan_Type=VlanIndex
_RaisecomIgmpMemberUserVlan_Object=MibTableColumn
raisecomIgmpMemberUserVlan=_RaisecomIgmpMemberUserVlan_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,2),_RaisecomIgmpMemberUserVlan_Type())
raisecomIgmpMemberUserVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMemberUserVlan.setStatus(_A)
_RaisecomIgmpMemberGroupIpType_Type=InetAddressType
_RaisecomIgmpMemberGroupIpType_Object=MibTableColumn
raisecomIgmpMemberGroupIpType=_RaisecomIgmpMemberGroupIpType_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,3),_RaisecomIgmpMemberGroupIpType_Type())
raisecomIgmpMemberGroupIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMemberGroupIpType.setStatus(_A)
_RaisecomIgmpMemberGroup_Type=InetAddress
_RaisecomIgmpMemberGroup_Object=MibTableColumn
raisecomIgmpMemberGroup=_RaisecomIgmpMemberGroup_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,4),_RaisecomIgmpMemberGroup_Type())
raisecomIgmpMemberGroup.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMemberGroup.setStatus(_A)
_RaisecomIgmpMemberMVlan_Type=Integer32
_RaisecomIgmpMemberMVlan_Object=MibTableColumn
raisecomIgmpMemberMVlan=_RaisecomIgmpMemberMVlan_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,5),_RaisecomIgmpMemberMVlan_Type())
raisecomIgmpMemberMVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMemberMVlan.setStatus(_A)
class _RaisecomIgmpMemberLiveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_RaisecomIgmpMemberLiveTime_Type.__name__=_D
_RaisecomIgmpMemberLiveTime_Object=MibTableColumn
raisecomIgmpMemberLiveTime=_RaisecomIgmpMemberLiveTime_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,6),_RaisecomIgmpMemberLiveTime_Type())
raisecomIgmpMemberLiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpMemberLiveTime.setStatus(_A)
_RaisecomIgmpMemberSource_Type=Integer32
_RaisecomIgmpMemberSource_Object=MibTableColumn
raisecomIgmpMemberSource=_RaisecomIgmpMemberSource_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,7),_RaisecomIgmpMemberSource_Type())
raisecomIgmpMemberSource.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpMemberSource.setStatus(_A)
_RaisecomIgmpMemberRowStatus_Type=RowStatus
_RaisecomIgmpMemberRowStatus_Object=MibTableColumn
raisecomIgmpMemberRowStatus=_RaisecomIgmpMemberRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,1,4,1,8),_RaisecomIgmpMemberRowStatus_Type())
raisecomIgmpMemberRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpMemberRowStatus.setStatus(_A)
_RaisecomIgmpPortStatisticsTable_Object=MibTable
raisecomIgmpPortStatisticsTable=_RaisecomIgmpPortStatisticsTable_Object((1,3,6,1,4,1,8886,1,28,2,1,5))
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsTable.setStatus(_A)
_RaisecomIgmpPortStatisticsEntry_Object=MibTableRow
raisecomIgmpPortStatisticsEntry=_RaisecomIgmpPortStatisticsEntry_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1))
raisecomIgmpPortStatisticsEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsEntry.setStatus(_A)
_RaisecomIgmpPortStatisticsPortNum_Type=Integer32
_RaisecomIgmpPortStatisticsPortNum_Object=MibTableColumn
raisecomIgmpPortStatisticsPortNum=_RaisecomIgmpPortStatisticsPortNum_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,1),_RaisecomIgmpPortStatisticsPortNum_Type())
raisecomIgmpPortStatisticsPortNum.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsPortNum.setStatus(_A)
class _RaisecomIgmpPortStatisticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('read',0),('clear',1)))
_RaisecomIgmpPortStatisticsClear_Type.__name__=_D
_RaisecomIgmpPortStatisticsClear_Object=MibTableColumn
raisecomIgmpPortStatisticsClear=_RaisecomIgmpPortStatisticsClear_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,2),_RaisecomIgmpPortStatisticsClear_Type())
raisecomIgmpPortStatisticsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsClear.setStatus(_A)
_RaisecomIgmpPortStatisticsRecvQuery_Type=Counter32
_RaisecomIgmpPortStatisticsRecvQuery_Object=MibTableColumn
raisecomIgmpPortStatisticsRecvQuery=_RaisecomIgmpPortStatisticsRecvQuery_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,3),_RaisecomIgmpPortStatisticsRecvQuery_Type())
raisecomIgmpPortStatisticsRecvQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsRecvQuery.setStatus(_A)
_RaisecomIgmpPortStatisticsRecvReport_Type=Counter32
_RaisecomIgmpPortStatisticsRecvReport_Object=MibTableColumn
raisecomIgmpPortStatisticsRecvReport=_RaisecomIgmpPortStatisticsRecvReport_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,4),_RaisecomIgmpPortStatisticsRecvReport_Type())
raisecomIgmpPortStatisticsRecvReport.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsRecvReport.setStatus(_A)
_RaisecomIgmpPortStatisticsRecvLeave_Type=Counter32
_RaisecomIgmpPortStatisticsRecvLeave_Object=MibTableColumn
raisecomIgmpPortStatisticsRecvLeave=_RaisecomIgmpPortStatisticsRecvLeave_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,5),_RaisecomIgmpPortStatisticsRecvLeave_Type())
raisecomIgmpPortStatisticsRecvLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsRecvLeave.setStatus(_A)
_RaisecomIgmpPortStatisticsFilterDropQuery_Type=Counter32
_RaisecomIgmpPortStatisticsFilterDropQuery_Object=MibTableColumn
raisecomIgmpPortStatisticsFilterDropQuery=_RaisecomIgmpPortStatisticsFilterDropQuery_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,6),_RaisecomIgmpPortStatisticsFilterDropQuery_Type())
raisecomIgmpPortStatisticsFilterDropQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsFilterDropQuery.setStatus(_A)
_RaisecomIgmpPortStatisticsFilterDropReport_Type=Counter32
_RaisecomIgmpPortStatisticsFilterDropReport_Object=MibTableColumn
raisecomIgmpPortStatisticsFilterDropReport=_RaisecomIgmpPortStatisticsFilterDropReport_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,7),_RaisecomIgmpPortStatisticsFilterDropReport_Type())
raisecomIgmpPortStatisticsFilterDropReport.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsFilterDropReport.setStatus(_A)
_RaisecomIgmpPortStatisticsFilterDropLeave_Type=Counter32
_RaisecomIgmpPortStatisticsFilterDropLeave_Object=MibTableColumn
raisecomIgmpPortStatisticsFilterDropLeave=_RaisecomIgmpPortStatisticsFilterDropLeave_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,8),_RaisecomIgmpPortStatisticsFilterDropLeave_Type())
raisecomIgmpPortStatisticsFilterDropLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsFilterDropLeave.setStatus(_A)
_RaisecomIgmpPortStatisticsSnoopDealQuery_Type=Counter32
_RaisecomIgmpPortStatisticsSnoopDealQuery_Object=MibTableColumn
raisecomIgmpPortStatisticsSnoopDealQuery=_RaisecomIgmpPortStatisticsSnoopDealQuery_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,9),_RaisecomIgmpPortStatisticsSnoopDealQuery_Type())
raisecomIgmpPortStatisticsSnoopDealQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsSnoopDealQuery.setStatus(_A)
_RaisecomIgmpPortStatisticsSnoopDealReport_Type=Counter32
_RaisecomIgmpPortStatisticsSnoopDealReport_Object=MibTableColumn
raisecomIgmpPortStatisticsSnoopDealReport=_RaisecomIgmpPortStatisticsSnoopDealReport_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,10),_RaisecomIgmpPortStatisticsSnoopDealReport_Type())
raisecomIgmpPortStatisticsSnoopDealReport.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsSnoopDealReport.setStatus(_A)
_RaisecomIgmpPortStatisticsSnoopDealLeave_Type=Counter32
_RaisecomIgmpPortStatisticsSnoopDealLeave_Object=MibTableColumn
raisecomIgmpPortStatisticsSnoopDealLeave=_RaisecomIgmpPortStatisticsSnoopDealLeave_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,11),_RaisecomIgmpPortStatisticsSnoopDealLeave_Type())
raisecomIgmpPortStatisticsSnoopDealLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsSnoopDealLeave.setStatus(_A)
_RaisecomIgmpPortStatisticsMvrDealQuery_Type=Counter32
_RaisecomIgmpPortStatisticsMvrDealQuery_Object=MibTableColumn
raisecomIgmpPortStatisticsMvrDealQuery=_RaisecomIgmpPortStatisticsMvrDealQuery_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,12),_RaisecomIgmpPortStatisticsMvrDealQuery_Type())
raisecomIgmpPortStatisticsMvrDealQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsMvrDealQuery.setStatus(_A)
_RaisecomIgmpPortStatisticsMvrDealReport_Type=Counter32
_RaisecomIgmpPortStatisticsMvrDealReport_Object=MibTableColumn
raisecomIgmpPortStatisticsMvrDealReport=_RaisecomIgmpPortStatisticsMvrDealReport_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,13),_RaisecomIgmpPortStatisticsMvrDealReport_Type())
raisecomIgmpPortStatisticsMvrDealReport.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsMvrDealReport.setStatus(_A)
_RaisecomIgmpPortStatisticsMvrDealLeave_Type=Counter32
_RaisecomIgmpPortStatisticsMvrDealLeave_Object=MibTableColumn
raisecomIgmpPortStatisticsMvrDealLeave=_RaisecomIgmpPortStatisticsMvrDealLeave_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,14),_RaisecomIgmpPortStatisticsMvrDealLeave_Type())
raisecomIgmpPortStatisticsMvrDealLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsMvrDealLeave.setStatus(_A)
_RaisecomIgmpPortStatisticsVlanCPDealQuery_Type=Counter32
_RaisecomIgmpPortStatisticsVlanCPDealQuery_Object=MibTableColumn
raisecomIgmpPortStatisticsVlanCPDealQuery=_RaisecomIgmpPortStatisticsVlanCPDealQuery_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,15),_RaisecomIgmpPortStatisticsVlanCPDealQuery_Type())
raisecomIgmpPortStatisticsVlanCPDealQuery.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsVlanCPDealQuery.setStatus(_A)
_RaisecomIgmpPortStatisticsVlanCPDealReport_Type=Counter32
_RaisecomIgmpPortStatisticsVlanCPDealReport_Object=MibTableColumn
raisecomIgmpPortStatisticsVlanCPDealReport=_RaisecomIgmpPortStatisticsVlanCPDealReport_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,16),_RaisecomIgmpPortStatisticsVlanCPDealReport_Type())
raisecomIgmpPortStatisticsVlanCPDealReport.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsVlanCPDealReport.setStatus(_A)
_RaisecomIgmpPortStatisticsVlanCPDealLeave_Type=Counter32
_RaisecomIgmpPortStatisticsVlanCPDealLeave_Object=MibTableColumn
raisecomIgmpPortStatisticsVlanCPDealLeave=_RaisecomIgmpPortStatisticsVlanCPDealLeave_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,17),_RaisecomIgmpPortStatisticsVlanCPDealLeave_Type())
raisecomIgmpPortStatisticsVlanCPDealLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsVlanCPDealLeave.setStatus(_A)
_RaisecomIgmpPortStatisticsReplaceCount_Type=Counter32
_RaisecomIgmpPortStatisticsReplaceCount_Object=MibTableColumn
raisecomIgmpPortStatisticsReplaceCount=_RaisecomIgmpPortStatisticsReplaceCount_Object((1,3,6,1,4,1,8886,1,28,2,1,5,1,18),_RaisecomIgmpPortStatisticsReplaceCount_Type())
raisecomIgmpPortStatisticsReplaceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpPortStatisticsReplaceCount.setStatus(_A)
_RaisecomIgmpSnooping_ObjectIdentity=ObjectIdentity
raisecomIgmpSnooping=_RaisecomIgmpSnooping_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,2))
_RaisecomIgmpSnoopingScalar_ObjectIdentity=ObjectIdentity
raisecomIgmpSnoopingScalar=_RaisecomIgmpSnoopingScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,2,1))
class _RaisecomIgmpSnoopingEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpSnoopingEnable_Type.__name__=_H
_RaisecomIgmpSnoopingEnable_Object=MibScalar
raisecomIgmpSnoopingEnable=_RaisecomIgmpSnoopingEnable_Object((1,3,6,1,4,1,8886,1,28,2,2,1,1),_RaisecomIgmpSnoopingEnable_Type())
raisecomIgmpSnoopingEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpSnoopingEnable.setStatus(_A)
_RaisecomIgmpSnoopingEnableVlanList_Type=Vlanset
_RaisecomIgmpSnoopingEnableVlanList_Object=MibScalar
raisecomIgmpSnoopingEnableVlanList=_RaisecomIgmpSnoopingEnableVlanList_Object((1,3,6,1,4,1,8886,1,28,2,2,1,2),_RaisecomIgmpSnoopingEnableVlanList_Type())
raisecomIgmpSnoopingEnableVlanList.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpSnoopingEnableVlanList.setStatus(_A)
class _RaisecomIgmpAuthRadiusEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpAuthRadiusEnable_Type.__name__=_H
_RaisecomIgmpAuthRadiusEnable_Object=MibScalar
raisecomIgmpAuthRadiusEnable=_RaisecomIgmpAuthRadiusEnable_Object((1,3,6,1,4,1,8886,1,28,2,2,1,3),_RaisecomIgmpAuthRadiusEnable_Type())
raisecomIgmpAuthRadiusEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpAuthRadiusEnable.setStatus(_A)
_RaisecomIgmpAuthRadiusPortEnable_Type=PortList
_RaisecomIgmpAuthRadiusPortEnable_Object=MibScalar
raisecomIgmpAuthRadiusPortEnable=_RaisecomIgmpAuthRadiusPortEnable_Object((1,3,6,1,4,1,8886,1,28,2,2,1,4),_RaisecomIgmpAuthRadiusPortEnable_Type())
raisecomIgmpAuthRadiusPortEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpAuthRadiusPortEnable.setStatus(_A)
_RaisecomIgmpMvr_ObjectIdentity=ObjectIdentity
raisecomIgmpMvr=_RaisecomIgmpMvr_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,3))
_RaisecomIgmpMvrScalar_ObjectIdentity=ObjectIdentity
raisecomIgmpMvrScalar=_RaisecomIgmpMvrScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,3,1))
class _RaisecomIgmpMvrEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpMvrEnable_Type.__name__=_H
_RaisecomIgmpMvrEnable_Object=MibScalar
raisecomIgmpMvrEnable=_RaisecomIgmpMvrEnable_Object((1,3,6,1,4,1,8886,1,28,2,3,1,1),_RaisecomIgmpMvrEnable_Type())
raisecomIgmpMvrEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpMvrEnable.setStatus(_A)
_RaisecomIgmpMvrEnablePortList_Type=PortList
_RaisecomIgmpMvrEnablePortList_Object=MibScalar
raisecomIgmpMvrEnablePortList=_RaisecomIgmpMvrEnablePortList_Object((1,3,6,1,4,1,8886,1,28,2,3,1,2),_RaisecomIgmpMvrEnablePortList_Type())
raisecomIgmpMvrEnablePortList.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpMvrEnablePortList.setStatus(_A)
_RaisecomIgmpMvrMVlanGroupTable_Object=MibTable
raisecomIgmpMvrMVlanGroupTable=_RaisecomIgmpMvrMVlanGroupTable_Object((1,3,6,1,4,1,8886,1,28,2,3,2))
if mibBuilder.loadTexts:raisecomIgmpMvrMVlanGroupTable.setStatus(_A)
_RaisecomIgmpMvrMVlanGroupEntry_Object=MibTableRow
raisecomIgmpMvrMVlanGroupEntry=_RaisecomIgmpMvrMVlanGroupEntry_Object((1,3,6,1,4,1,8886,1,28,2,3,2,1))
raisecomIgmpMvrMVlanGroupEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:raisecomIgmpMvrMVlanGroupEntry.setStatus(_A)
_RaisecomIgmpMvrGroupIpType_Type=InetAddressType
_RaisecomIgmpMvrGroupIpType_Object=MibTableColumn
raisecomIgmpMvrGroupIpType=_RaisecomIgmpMvrGroupIpType_Object((1,3,6,1,4,1,8886,1,28,2,3,2,1,1),_RaisecomIgmpMvrGroupIpType_Type())
raisecomIgmpMvrGroupIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMvrGroupIpType.setStatus(_A)
_RaisecomIgmpMvrGroup_Type=InetAddress
_RaisecomIgmpMvrGroup_Object=MibTableColumn
raisecomIgmpMvrGroup=_RaisecomIgmpMvrGroup_Object((1,3,6,1,4,1,8886,1,28,2,3,2,1,2),_RaisecomIgmpMvrGroup_Type())
raisecomIgmpMvrGroup.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpMvrGroup.setStatus(_A)
_RaisecomIgmpMvrMVlan_Type=VlanId
_RaisecomIgmpMvrMVlan_Object=MibTableColumn
raisecomIgmpMvrMVlan=_RaisecomIgmpMvrMVlan_Object((1,3,6,1,4,1,8886,1,28,2,3,2,1,3),_RaisecomIgmpMvrMVlan_Type())
raisecomIgmpMvrMVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpMvrMVlan.setStatus(_A)
_RaisecomIgmpMvrGroupRowStatus_Type=RowStatus
_RaisecomIgmpMvrGroupRowStatus_Object=MibTableColumn
raisecomIgmpMvrGroupRowStatus=_RaisecomIgmpMvrGroupRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,3,2,1,4),_RaisecomIgmpMvrGroupRowStatus_Type())
raisecomIgmpMvrGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpMvrGroupRowStatus.setStatus(_A)
_RaisecomIgmpVlanCopy_ObjectIdentity=ObjectIdentity
raisecomIgmpVlanCopy=_RaisecomIgmpVlanCopy_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,4))
_RaisecomIgmpVlanCopyScalar_ObjectIdentity=ObjectIdentity
raisecomIgmpVlanCopyScalar=_RaisecomIgmpVlanCopyScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,4,1))
class _RaisecomIgmpVlanCopyEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpVlanCopyEnable_Type.__name__=_H
_RaisecomIgmpVlanCopyEnable_Object=MibScalar
raisecomIgmpVlanCopyEnable=_RaisecomIgmpVlanCopyEnable_Object((1,3,6,1,4,1,8886,1,28,2,4,1,1),_RaisecomIgmpVlanCopyEnable_Type())
raisecomIgmpVlanCopyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyEnable.setStatus(_A)
_RaisecomIgmpVlanCopyEnablePortList_Type=PortList
_RaisecomIgmpVlanCopyEnablePortList_Object=MibScalar
raisecomIgmpVlanCopyEnablePortList=_RaisecomIgmpVlanCopyEnablePortList_Object((1,3,6,1,4,1,8886,1,28,2,4,1,2),_RaisecomIgmpVlanCopyEnablePortList_Type())
raisecomIgmpVlanCopyEnablePortList.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyEnablePortList.setStatus(_A)
_RaisecomIgmpVlanCopyVlanGroupTable_Object=MibTable
raisecomIgmpVlanCopyVlanGroupTable=_RaisecomIgmpVlanCopyVlanGroupTable_Object((1,3,6,1,4,1,8886,1,28,2,4,2))
if mibBuilder.loadTexts:raisecomIgmpVlanCopyVlanGroupTable.setStatus(_A)
_RaisecomIgmpVlanCopyVlanGroupEntry_Object=MibTableRow
raisecomIgmpVlanCopyVlanGroupEntry=_RaisecomIgmpVlanCopyVlanGroupEntry_Object((1,3,6,1,4,1,8886,1,28,2,4,2,1))
raisecomIgmpVlanCopyVlanGroupEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:raisecomIgmpVlanCopyVlanGroupEntry.setStatus(_A)
_RaisecomIgmpVlanCopyGroupIpType_Type=InetAddressType
_RaisecomIgmpVlanCopyGroupIpType_Object=MibTableColumn
raisecomIgmpVlanCopyGroupIpType=_RaisecomIgmpVlanCopyGroupIpType_Object((1,3,6,1,4,1,8886,1,28,2,4,2,1,1),_RaisecomIgmpVlanCopyGroupIpType_Type())
raisecomIgmpVlanCopyGroupIpType.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyGroupIpType.setStatus(_A)
_RaisecomIgmpVlanCopyGroup_Type=InetAddress
_RaisecomIgmpVlanCopyGroup_Object=MibTableColumn
raisecomIgmpVlanCopyGroup=_RaisecomIgmpVlanCopyGroup_Object((1,3,6,1,4,1,8886,1,28,2,4,2,1,2),_RaisecomIgmpVlanCopyGroup_Type())
raisecomIgmpVlanCopyGroup.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyGroup.setStatus(_A)
_RaisecomIgmpVlanCopyMcastVlan_Type=VlanId
_RaisecomIgmpVlanCopyMcastVlan_Object=MibTableColumn
raisecomIgmpVlanCopyMcastVlan=_RaisecomIgmpVlanCopyMcastVlan_Object((1,3,6,1,4,1,8886,1,28,2,4,2,1,3),_RaisecomIgmpVlanCopyMcastVlan_Type())
raisecomIgmpVlanCopyMcastVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyMcastVlan.setStatus(_A)
_RaisecomIgmpVlanCopyGroupRowStatus_Type=RowStatus
_RaisecomIgmpVlanCopyGroupRowStatus_Object=MibTableColumn
raisecomIgmpVlanCopyGroupRowStatus=_RaisecomIgmpVlanCopyGroupRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,4,2,1,4),_RaisecomIgmpVlanCopyGroupRowStatus_Type())
raisecomIgmpVlanCopyGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyGroupRowStatus.setStatus(_A)
_RaisecomIgmpProxy_ObjectIdentity=ObjectIdentity
raisecomIgmpProxy=_RaisecomIgmpProxy_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,5))
_RaisecomIgmpProxyScalar_ObjectIdentity=ObjectIdentity
raisecomIgmpProxyScalar=_RaisecomIgmpProxyScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,5,1))
class _RaisecomIgmpProxyEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpProxyEnable_Type.__name__=_H
_RaisecomIgmpProxyEnable_Object=MibScalar
raisecomIgmpProxyEnable=_RaisecomIgmpProxyEnable_Object((1,3,6,1,4,1,8886,1,28,2,5,1,1),_RaisecomIgmpProxyEnable_Type())
raisecomIgmpProxyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxyEnable.setStatus(_A)
class _RaisecomIgmpProxySuppressionEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpProxySuppressionEnable_Type.__name__=_H
_RaisecomIgmpProxySuppressionEnable_Object=MibScalar
raisecomIgmpProxySuppressionEnable=_RaisecomIgmpProxySuppressionEnable_Object((1,3,6,1,4,1,8886,1,28,2,5,1,2),_RaisecomIgmpProxySuppressionEnable_Type())
raisecomIgmpProxySuppressionEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxySuppressionEnable.setStatus(_A)
class _RaisecomIgmpProxyQuerierEnable_Type(EnableVar):defaultValue=2
_RaisecomIgmpProxyQuerierEnable_Type.__name__=_H
_RaisecomIgmpProxyQuerierEnable_Object=MibScalar
raisecomIgmpProxyQuerierEnable=_RaisecomIgmpProxyQuerierEnable_Object((1,3,6,1,4,1,8886,1,28,2,5,1,3),_RaisecomIgmpProxyQuerierEnable_Type())
raisecomIgmpProxyQuerierEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxyQuerierEnable.setStatus(_A)
class _RaisecomIgmpProxySourceIpType_Type(InetAddressType):defaultValue=1
_RaisecomIgmpProxySourceIpType_Type.__name__=_I
_RaisecomIgmpProxySourceIpType_Object=MibScalar
raisecomIgmpProxySourceIpType=_RaisecomIgmpProxySourceIpType_Object((1,3,6,1,4,1,8886,1,28,2,5,1,4),_RaisecomIgmpProxySourceIpType_Type())
raisecomIgmpProxySourceIpType.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxySourceIpType.setStatus(_A)
_RaisecomIgmpProxySourceIpAddress_Type=InetAddress
_RaisecomIgmpProxySourceIpAddress_Object=MibScalar
raisecomIgmpProxySourceIpAddress=_RaisecomIgmpProxySourceIpAddress_Object((1,3,6,1,4,1,8886,1,28,2,5,1,5),_RaisecomIgmpProxySourceIpAddress_Type())
raisecomIgmpProxySourceIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxySourceIpAddress.setStatus(_A)
class _RaisecomIgmpProxyQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_RaisecomIgmpProxyQueryInterval_Type.__name__=_D
_RaisecomIgmpProxyQueryInterval_Object=MibScalar
raisecomIgmpProxyQueryInterval=_RaisecomIgmpProxyQueryInterval_Object((1,3,6,1,4,1,8886,1,28,2,5,1,6),_RaisecomIgmpProxyQueryInterval_Type())
raisecomIgmpProxyQueryInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxyQueryInterval.setStatus(_A)
class _RaisecomIgmpProxyQueryMaxReponseInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_RaisecomIgmpProxyQueryMaxReponseInterval_Type.__name__=_D
_RaisecomIgmpProxyQueryMaxReponseInterval_Object=MibScalar
raisecomIgmpProxyQueryMaxReponseInterval=_RaisecomIgmpProxyQueryMaxReponseInterval_Object((1,3,6,1,4,1,8886,1,28,2,5,1,7),_RaisecomIgmpProxyQueryMaxReponseInterval_Type())
raisecomIgmpProxyQueryMaxReponseInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxyQueryMaxReponseInterval.setStatus(_A)
class _RaisecomIgmpProxyQueryLastMemberInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_RaisecomIgmpProxyQueryLastMemberInterval_Type.__name__=_D
_RaisecomIgmpProxyQueryLastMemberInterval_Object=MibScalar
raisecomIgmpProxyQueryLastMemberInterval=_RaisecomIgmpProxyQueryLastMemberInterval_Object((1,3,6,1,4,1,8886,1,28,2,5,1,8),_RaisecomIgmpProxyQueryLastMemberInterval_Type())
raisecomIgmpProxyQueryLastMemberInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpProxyQueryLastMemberInterval.setStatus(_A)
_RaisecomIgmpFilter_ObjectIdentity=ObjectIdentity
raisecomIgmpFilter=_RaisecomIgmpFilter_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,6))
_RaisecomIgmpFilterScalar_ObjectIdentity=ObjectIdentity
raisecomIgmpFilterScalar=_RaisecomIgmpFilterScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,28,2,6,1))
class _RaisecomIgmpFilterEnableFilter_Type(EnableVar):defaultValue=2
_RaisecomIgmpFilterEnableFilter_Type.__name__=_H
_RaisecomIgmpFilterEnableFilter_Object=MibScalar
raisecomIgmpFilterEnableFilter=_RaisecomIgmpFilterEnableFilter_Object((1,3,6,1,4,1,8886,1,28,2,6,1,1),_RaisecomIgmpFilterEnableFilter_Type())
raisecomIgmpFilterEnableFilter.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpFilterEnableFilter.setStatus(_A)
class _RaisecomIgmpFilterMaxProfileNum_Type(Integer32):defaultValue=100
_RaisecomIgmpFilterMaxProfileNum_Type.__name__=_D
_RaisecomIgmpFilterMaxProfileNum_Object=MibScalar
raisecomIgmpFilterMaxProfileNum=_RaisecomIgmpFilterMaxProfileNum_Object((1,3,6,1,4,1,8886,1,28,2,6,1,2),_RaisecomIgmpFilterMaxProfileNum_Type())
raisecomIgmpFilterMaxProfileNum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpFilterMaxProfileNum.setStatus(_A)
class _RaisecomIgmpFilterCurrentProfileNum_Type(Integer32):defaultValue=0
_RaisecomIgmpFilterCurrentProfileNum_Type.__name__=_D
_RaisecomIgmpFilterCurrentProfileNum_Object=MibScalar
raisecomIgmpFilterCurrentProfileNum=_RaisecomIgmpFilterCurrentProfileNum_Object((1,3,6,1,4,1,8886,1,28,2,6,1,3),_RaisecomIgmpFilterCurrentProfileNum_Type())
raisecomIgmpFilterCurrentProfileNum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpFilterCurrentProfileNum.setStatus(_A)
_RaisecomIgmpFilterProfileTable_Object=MibTable
raisecomIgmpFilterProfileTable=_RaisecomIgmpFilterProfileTable_Object((1,3,6,1,4,1,8886,1,28,2,6,2))
if mibBuilder.loadTexts:raisecomIgmpFilterProfileTable.setStatus(_A)
_RaisecomIgmpFilterProfileEntry_Object=MibTableRow
raisecomIgmpFilterProfileEntry=_RaisecomIgmpFilterProfileEntry_Object((1,3,6,1,4,1,8886,1,28,2,6,2,1))
raisecomIgmpFilterProfileEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:raisecomIgmpFilterProfileEntry.setStatus(_A)
class _RaisecomIgmpFilterProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomIgmpFilterProfileIndex_Type.__name__=_D
_RaisecomIgmpFilterProfileIndex_Object=MibTableColumn
raisecomIgmpFilterProfileIndex=_RaisecomIgmpFilterProfileIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,2,1,1),_RaisecomIgmpFilterProfileIndex_Type())
raisecomIgmpFilterProfileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpFilterProfileIndex.setStatus(_A)
class _RaisecomIgmpFilterProfileAct_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_RaisecomIgmpFilterProfileAct_Type.__name__=_D
_RaisecomIgmpFilterProfileAct_Object=MibTableColumn
raisecomIgmpFilterProfileAct=_RaisecomIgmpFilterProfileAct_Object((1,3,6,1,4,1,8886,1,28,2,6,2,1,2),_RaisecomIgmpFilterProfileAct_Type())
raisecomIgmpFilterProfileAct.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterProfileAct.setStatus(_A)
_RaisecomIgmpFilterProfileRowStatus_Type=RowStatus
_RaisecomIgmpFilterProfileRowStatus_Object=MibTableColumn
raisecomIgmpFilterProfileRowStatus=_RaisecomIgmpFilterProfileRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,6,2,1,3),_RaisecomIgmpFilterProfileRowStatus_Type())
raisecomIgmpFilterProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterProfileRowStatus.setStatus(_A)
_RaisecomIgmpFilterPortTable_Object=MibTable
raisecomIgmpFilterPortTable=_RaisecomIgmpFilterPortTable_Object((1,3,6,1,4,1,8886,1,28,2,6,3))
if mibBuilder.loadTexts:raisecomIgmpFilterPortTable.setStatus(_A)
_RaisecomIgmpFilterPortEntry_Object=MibTableRow
raisecomIgmpFilterPortEntry=_RaisecomIgmpFilterPortEntry_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1))
raisecomIgmpFilterPortEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:raisecomIgmpFilterPortEntry.setStatus(_A)
_RaisecomIgmpFilterPortIndex_Type=Integer32
_RaisecomIgmpFilterPortIndex_Object=MibTableColumn
raisecomIgmpFilterPortIndex=_RaisecomIgmpFilterPortIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1,1),_RaisecomIgmpFilterPortIndex_Type())
raisecomIgmpFilterPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpFilterPortIndex.setStatus(_A)
class _RaisecomIgmpFilterPortProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomIgmpFilterPortProfileIndex_Type.__name__=_D
_RaisecomIgmpFilterPortProfileIndex_Object=MibTableColumn
raisecomIgmpFilterPortProfileIndex=_RaisecomIgmpFilterPortProfileIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1,2),_RaisecomIgmpFilterPortProfileIndex_Type())
raisecomIgmpFilterPortProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortProfileIndex.setStatus(_A)
class _RaisecomIgmpFilterPortMaxGroups_Type(Integer32):defaultValue=0
_RaisecomIgmpFilterPortMaxGroups_Type.__name__=_D
_RaisecomIgmpFilterPortMaxGroups_Object=MibTableColumn
raisecomIgmpFilterPortMaxGroups=_RaisecomIgmpFilterPortMaxGroups_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1,3),_RaisecomIgmpFilterPortMaxGroups_Type())
raisecomIgmpFilterPortMaxGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortMaxGroups.setStatus(_A)
_RaisecomIgmpFilterPortCurrentGroups_Type=Integer32
_RaisecomIgmpFilterPortCurrentGroups_Object=MibTableColumn
raisecomIgmpFilterPortCurrentGroups=_RaisecomIgmpFilterPortCurrentGroups_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1,4),_RaisecomIgmpFilterPortCurrentGroups_Type())
raisecomIgmpFilterPortCurrentGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpFilterPortCurrentGroups.setStatus(_A)
class _RaisecomIgmpFilterPortMaxGroupsAct_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),(_Y,2)))
_RaisecomIgmpFilterPortMaxGroupsAct_Type.__name__=_D
_RaisecomIgmpFilterPortMaxGroupsAct_Object=MibTableColumn
raisecomIgmpFilterPortMaxGroupsAct=_RaisecomIgmpFilterPortMaxGroupsAct_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1,5),_RaisecomIgmpFilterPortMaxGroupsAct_Type())
raisecomIgmpFilterPortMaxGroupsAct.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortMaxGroupsAct.setStatus(_A)
_RaisecomIgmpFilterPortRowStatus_Type=RowStatus
_RaisecomIgmpFilterPortRowStatus_Object=MibTableColumn
raisecomIgmpFilterPortRowStatus=_RaisecomIgmpFilterPortRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,6,3,1,6),_RaisecomIgmpFilterPortRowStatus_Type())
raisecomIgmpFilterPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortRowStatus.setStatus(_A)
_RaisecomIgmpFilterPortVlanTable_Object=MibTable
raisecomIgmpFilterPortVlanTable=_RaisecomIgmpFilterPortVlanTable_Object((1,3,6,1,4,1,8886,1,28,2,6,4))
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanTable.setStatus(_A)
_RaisecomIgmpFilterPortVlanEntry_Object=MibTableRow
raisecomIgmpFilterPortVlanEntry=_RaisecomIgmpFilterPortVlanEntry_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1))
raisecomIgmpFilterPortVlanEntry.setIndexNames((0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanEntry.setStatus(_A)
_RaisecomIgmpFilterPortVlanPortIndex_Type=Integer32
_RaisecomIgmpFilterPortVlanPortIndex_Object=MibTableColumn
raisecomIgmpFilterPortVlanPortIndex=_RaisecomIgmpFilterPortVlanPortIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,1),_RaisecomIgmpFilterPortVlanPortIndex_Type())
raisecomIgmpFilterPortVlanPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanPortIndex.setStatus(_A)
_RaisecomIgmpFilterPortVlanVlanIndex_Type=VlanIndex
_RaisecomIgmpFilterPortVlanVlanIndex_Object=MibTableColumn
raisecomIgmpFilterPortVlanVlanIndex=_RaisecomIgmpFilterPortVlanVlanIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,2),_RaisecomIgmpFilterPortVlanVlanIndex_Type())
raisecomIgmpFilterPortVlanVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanVlanIndex.setStatus(_A)
class _RaisecomIgmpFilterPortVlanProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomIgmpFilterPortVlanProfileIndex_Type.__name__=_D
_RaisecomIgmpFilterPortVlanProfileIndex_Object=MibTableColumn
raisecomIgmpFilterPortVlanProfileIndex=_RaisecomIgmpFilterPortVlanProfileIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,3),_RaisecomIgmpFilterPortVlanProfileIndex_Type())
raisecomIgmpFilterPortVlanProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanProfileIndex.setStatus(_A)
class _RaisecomIgmpFilterPortVlanMaxGroups_Type(Integer32):defaultValue=0
_RaisecomIgmpFilterPortVlanMaxGroups_Type.__name__=_D
_RaisecomIgmpFilterPortVlanMaxGroups_Object=MibTableColumn
raisecomIgmpFilterPortVlanMaxGroups=_RaisecomIgmpFilterPortVlanMaxGroups_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,4),_RaisecomIgmpFilterPortVlanMaxGroups_Type())
raisecomIgmpFilterPortVlanMaxGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanMaxGroups.setStatus(_A)
_RaisecomIgmpFilterPortVlanCurrentGroups_Type=Integer32
_RaisecomIgmpFilterPortVlanCurrentGroups_Object=MibTableColumn
raisecomIgmpFilterPortVlanCurrentGroups=_RaisecomIgmpFilterPortVlanCurrentGroups_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,5),_RaisecomIgmpFilterPortVlanCurrentGroups_Type())
raisecomIgmpFilterPortVlanCurrentGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanCurrentGroups.setStatus(_A)
class _RaisecomIgmpFilterPortVlanMaxGroupsAct_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),(_Y,2)))
_RaisecomIgmpFilterPortVlanMaxGroupsAct_Type.__name__=_D
_RaisecomIgmpFilterPortVlanMaxGroupsAct_Object=MibTableColumn
raisecomIgmpFilterPortVlanMaxGroupsAct=_RaisecomIgmpFilterPortVlanMaxGroupsAct_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,6),_RaisecomIgmpFilterPortVlanMaxGroupsAct_Type())
raisecomIgmpFilterPortVlanMaxGroupsAct.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanMaxGroupsAct.setStatus(_A)
_RaisecomIgmpFilterPortVlanRowStatus_Type=RowStatus
_RaisecomIgmpFilterPortVlanRowStatus_Object=MibTableColumn
raisecomIgmpFilterPortVlanRowStatus=_RaisecomIgmpFilterPortVlanRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,6,4,1,7),_RaisecomIgmpFilterPortVlanRowStatus_Type())
raisecomIgmpFilterPortVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterPortVlanRowStatus.setStatus(_A)
_RaisecomIgmpFilterIpProfileTable_Object=MibTable
raisecomIgmpFilterIpProfileTable=_RaisecomIgmpFilterIpProfileTable_Object((1,3,6,1,4,1,8886,1,28,2,6,5))
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileTable.setStatus(_A)
_RaisecomIgmpFilterIpProfileEntry_Object=MibTableRow
raisecomIgmpFilterIpProfileEntry=_RaisecomIgmpFilterIpProfileEntry_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1))
raisecomIgmpFilterIpProfileEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileEntry.setStatus(_A)
class _RaisecomIgmpFilterIpProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomIgmpFilterIpProfileIndex_Type.__name__=_D
_RaisecomIgmpFilterIpProfileIndex_Object=MibTableColumn
raisecomIgmpFilterIpProfileIndex=_RaisecomIgmpFilterIpProfileIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1,1),_RaisecomIgmpFilterIpProfileIndex_Type())
raisecomIgmpFilterIpProfileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileIndex.setStatus(_A)
class _RaisecomIgmpFilterIpProfileRangeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RaisecomIgmpFilterIpProfileRangeIndex_Type.__name__=_D
_RaisecomIgmpFilterIpProfileRangeIndex_Object=MibTableColumn
raisecomIgmpFilterIpProfileRangeIndex=_RaisecomIgmpFilterIpProfileRangeIndex_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1,2),_RaisecomIgmpFilterIpProfileRangeIndex_Type())
raisecomIgmpFilterIpProfileRangeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileRangeIndex.setStatus(_A)
_RaisecomIgmpFilterIpProfileStartAddress_Type=InetAddress
_RaisecomIgmpFilterIpProfileStartAddress_Object=MibTableColumn
raisecomIgmpFilterIpProfileStartAddress=_RaisecomIgmpFilterIpProfileStartAddress_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1,3),_RaisecomIgmpFilterIpProfileStartAddress_Type())
raisecomIgmpFilterIpProfileStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileStartAddress.setStatus(_A)
_RaisecomIgmpFilterIpProfileEndAddress_Type=InetAddress
_RaisecomIgmpFilterIpProfileEndAddress_Object=MibTableColumn
raisecomIgmpFilterIpProfileEndAddress=_RaisecomIgmpFilterIpProfileEndAddress_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1,4),_RaisecomIgmpFilterIpProfileEndAddress_Type())
raisecomIgmpFilterIpProfileEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileEndAddress.setStatus(_A)
_RaisecomIgmpFilterIpProfileIpType_Type=InetAddressType
_RaisecomIgmpFilterIpProfileIpType_Object=MibTableColumn
raisecomIgmpFilterIpProfileIpType=_RaisecomIgmpFilterIpProfileIpType_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1,5),_RaisecomIgmpFilterIpProfileIpType_Type())
raisecomIgmpFilterIpProfileIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileIpType.setStatus(_A)
_RaisecomIgmpFilterIpProfileRowStatus_Type=RowStatus
_RaisecomIgmpFilterIpProfileRowStatus_Object=MibTableColumn
raisecomIgmpFilterIpProfileRowStatus=_RaisecomIgmpFilterIpProfileRowStatus_Object((1,3,6,1,4,1,8886,1,28,2,6,5,1,6),_RaisecomIgmpFilterIpProfileRowStatus_Type())
raisecomIgmpFilterIpProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIgmpFilterIpProfileRowStatus.setStatus(_A)
_RaisecomIgmpL2Conformance_ObjectIdentity=ObjectIdentity
raisecomIgmpL2Conformance=_RaisecomIgmpL2Conformance_ObjectIdentity((1,3,6,1,4,1,8886,1,28,3))
mibBuilder.exportSymbols(_E,**{'raisecomIgmpL2':raisecomIgmpL2,'raisecomIgmpL2Notifications':raisecomIgmpL2Notifications,'raisecomIgmpL2Objects':raisecomIgmpL2Objects,'raisecomIgmpBase':raisecomIgmpBase,'raisecomIgmpBaseScalar':raisecomIgmpBaseScalar,'raisecomIgmpAging':raisecomIgmpAging,'raisecomIgmpRingPortList':raisecomIgmpRingPortList,'raisecomIgmpImmediateLeaveTable':raisecomIgmpImmediateLeaveTable,'raisecomIgmpImmediateLeaveEntry':raisecomIgmpImmediateLeaveEntry,_J:raisecomIgmpImmediateLeavePort,'raisecomIgmpImmediateLeaveType':raisecomIgmpImmediateLeaveType,'raisecomIgmpImmediateLeaveVlanList':raisecomIgmpImmediateLeaveVlanList,'raisecomIgmpImmediateLeaveRowStatus':raisecomIgmpImmediateLeaveRowStatus,'raisecomIgmpMrouterTable':raisecomIgmpMrouterTable,'raisecomIgmpMrouterEntry':raisecomIgmpMrouterEntry,_K:raisecomIgmpMrouterPort,_L:raisecomIgmpMrouterVlan,'raisecomIgmpMrouterLiveTime':raisecomIgmpMrouterLiveTime,'raisecomIgmpMrouterMRStatus':raisecomIgmpMrouterMRStatus,'raisecomIgmpMrouterRowStatus':raisecomIgmpMrouterRowStatus,'raisecomIgmpMemberTable':raisecomIgmpMemberTable,'raisecomIgmpMemberEntry':raisecomIgmpMemberEntry,_M:raisecomIgmpMemberPort,_N:raisecomIgmpMemberUserVlan,_O:raisecomIgmpMemberGroupIpType,_P:raisecomIgmpMemberGroup,_Q:raisecomIgmpMemberMVlan,'raisecomIgmpMemberLiveTime':raisecomIgmpMemberLiveTime,'raisecomIgmpMemberSource':raisecomIgmpMemberSource,'raisecomIgmpMemberRowStatus':raisecomIgmpMemberRowStatus,'raisecomIgmpPortStatisticsTable':raisecomIgmpPortStatisticsTable,'raisecomIgmpPortStatisticsEntry':raisecomIgmpPortStatisticsEntry,_R:raisecomIgmpPortStatisticsPortNum,'raisecomIgmpPortStatisticsClear':raisecomIgmpPortStatisticsClear,'raisecomIgmpPortStatisticsRecvQuery':raisecomIgmpPortStatisticsRecvQuery,'raisecomIgmpPortStatisticsRecvReport':raisecomIgmpPortStatisticsRecvReport,'raisecomIgmpPortStatisticsRecvLeave':raisecomIgmpPortStatisticsRecvLeave,'raisecomIgmpPortStatisticsFilterDropQuery':raisecomIgmpPortStatisticsFilterDropQuery,'raisecomIgmpPortStatisticsFilterDropReport':raisecomIgmpPortStatisticsFilterDropReport,'raisecomIgmpPortStatisticsFilterDropLeave':raisecomIgmpPortStatisticsFilterDropLeave,'raisecomIgmpPortStatisticsSnoopDealQuery':raisecomIgmpPortStatisticsSnoopDealQuery,'raisecomIgmpPortStatisticsSnoopDealReport':raisecomIgmpPortStatisticsSnoopDealReport,'raisecomIgmpPortStatisticsSnoopDealLeave':raisecomIgmpPortStatisticsSnoopDealLeave,'raisecomIgmpPortStatisticsMvrDealQuery':raisecomIgmpPortStatisticsMvrDealQuery,'raisecomIgmpPortStatisticsMvrDealReport':raisecomIgmpPortStatisticsMvrDealReport,'raisecomIgmpPortStatisticsMvrDealLeave':raisecomIgmpPortStatisticsMvrDealLeave,'raisecomIgmpPortStatisticsVlanCPDealQuery':raisecomIgmpPortStatisticsVlanCPDealQuery,'raisecomIgmpPortStatisticsVlanCPDealReport':raisecomIgmpPortStatisticsVlanCPDealReport,'raisecomIgmpPortStatisticsVlanCPDealLeave':raisecomIgmpPortStatisticsVlanCPDealLeave,'raisecomIgmpPortStatisticsReplaceCount':raisecomIgmpPortStatisticsReplaceCount,'raisecomIgmpSnooping':raisecomIgmpSnooping,'raisecomIgmpSnoopingScalar':raisecomIgmpSnoopingScalar,'raisecomIgmpSnoopingEnable':raisecomIgmpSnoopingEnable,'raisecomIgmpSnoopingEnableVlanList':raisecomIgmpSnoopingEnableVlanList,'raisecomIgmpAuthRadiusEnable':raisecomIgmpAuthRadiusEnable,'raisecomIgmpAuthRadiusPortEnable':raisecomIgmpAuthRadiusPortEnable,'raisecomIgmpMvr':raisecomIgmpMvr,'raisecomIgmpMvrScalar':raisecomIgmpMvrScalar,'raisecomIgmpMvrEnable':raisecomIgmpMvrEnable,'raisecomIgmpMvrEnablePortList':raisecomIgmpMvrEnablePortList,'raisecomIgmpMvrMVlanGroupTable':raisecomIgmpMvrMVlanGroupTable,'raisecomIgmpMvrMVlanGroupEntry':raisecomIgmpMvrMVlanGroupEntry,_S:raisecomIgmpMvrGroupIpType,_T:raisecomIgmpMvrGroup,'raisecomIgmpMvrMVlan':raisecomIgmpMvrMVlan,'raisecomIgmpMvrGroupRowStatus':raisecomIgmpMvrGroupRowStatus,'raisecomIgmpVlanCopy':raisecomIgmpVlanCopy,'raisecomIgmpVlanCopyScalar':raisecomIgmpVlanCopyScalar,'raisecomIgmpVlanCopyEnable':raisecomIgmpVlanCopyEnable,'raisecomIgmpVlanCopyEnablePortList':raisecomIgmpVlanCopyEnablePortList,'raisecomIgmpVlanCopyVlanGroupTable':raisecomIgmpVlanCopyVlanGroupTable,'raisecomIgmpVlanCopyVlanGroupEntry':raisecomIgmpVlanCopyVlanGroupEntry,_U:raisecomIgmpVlanCopyGroupIpType,_V:raisecomIgmpVlanCopyGroup,'raisecomIgmpVlanCopyMcastVlan':raisecomIgmpVlanCopyMcastVlan,'raisecomIgmpVlanCopyGroupRowStatus':raisecomIgmpVlanCopyGroupRowStatus,'raisecomIgmpProxy':raisecomIgmpProxy,'raisecomIgmpProxyScalar':raisecomIgmpProxyScalar,'raisecomIgmpProxyEnable':raisecomIgmpProxyEnable,'raisecomIgmpProxySuppressionEnable':raisecomIgmpProxySuppressionEnable,'raisecomIgmpProxyQuerierEnable':raisecomIgmpProxyQuerierEnable,'raisecomIgmpProxySourceIpType':raisecomIgmpProxySourceIpType,'raisecomIgmpProxySourceIpAddress':raisecomIgmpProxySourceIpAddress,'raisecomIgmpProxyQueryInterval':raisecomIgmpProxyQueryInterval,'raisecomIgmpProxyQueryMaxReponseInterval':raisecomIgmpProxyQueryMaxReponseInterval,'raisecomIgmpProxyQueryLastMemberInterval':raisecomIgmpProxyQueryLastMemberInterval,'raisecomIgmpFilter':raisecomIgmpFilter,'raisecomIgmpFilterScalar':raisecomIgmpFilterScalar,'raisecomIgmpFilterEnableFilter':raisecomIgmpFilterEnableFilter,'raisecomIgmpFilterMaxProfileNum':raisecomIgmpFilterMaxProfileNum,'raisecomIgmpFilterCurrentProfileNum':raisecomIgmpFilterCurrentProfileNum,'raisecomIgmpFilterProfileTable':raisecomIgmpFilterProfileTable,'raisecomIgmpFilterProfileEntry':raisecomIgmpFilterProfileEntry,_W:raisecomIgmpFilterProfileIndex,'raisecomIgmpFilterProfileAct':raisecomIgmpFilterProfileAct,'raisecomIgmpFilterProfileRowStatus':raisecomIgmpFilterProfileRowStatus,'raisecomIgmpFilterPortTable':raisecomIgmpFilterPortTable,'raisecomIgmpFilterPortEntry':raisecomIgmpFilterPortEntry,_X:raisecomIgmpFilterPortIndex,'raisecomIgmpFilterPortProfileIndex':raisecomIgmpFilterPortProfileIndex,'raisecomIgmpFilterPortMaxGroups':raisecomIgmpFilterPortMaxGroups,'raisecomIgmpFilterPortCurrentGroups':raisecomIgmpFilterPortCurrentGroups,'raisecomIgmpFilterPortMaxGroupsAct':raisecomIgmpFilterPortMaxGroupsAct,'raisecomIgmpFilterPortRowStatus':raisecomIgmpFilterPortRowStatus,'raisecomIgmpFilterPortVlanTable':raisecomIgmpFilterPortVlanTable,'raisecomIgmpFilterPortVlanEntry':raisecomIgmpFilterPortVlanEntry,_Z:raisecomIgmpFilterPortVlanPortIndex,_a:raisecomIgmpFilterPortVlanVlanIndex,'raisecomIgmpFilterPortVlanProfileIndex':raisecomIgmpFilterPortVlanProfileIndex,'raisecomIgmpFilterPortVlanMaxGroups':raisecomIgmpFilterPortVlanMaxGroups,'raisecomIgmpFilterPortVlanCurrentGroups':raisecomIgmpFilterPortVlanCurrentGroups,'raisecomIgmpFilterPortVlanMaxGroupsAct':raisecomIgmpFilterPortVlanMaxGroupsAct,'raisecomIgmpFilterPortVlanRowStatus':raisecomIgmpFilterPortVlanRowStatus,'raisecomIgmpFilterIpProfileTable':raisecomIgmpFilterIpProfileTable,'raisecomIgmpFilterIpProfileEntry':raisecomIgmpFilterIpProfileEntry,_b:raisecomIgmpFilterIpProfileIndex,_c:raisecomIgmpFilterIpProfileRangeIndex,'raisecomIgmpFilterIpProfileStartAddress':raisecomIgmpFilterIpProfileStartAddress,'raisecomIgmpFilterIpProfileEndAddress':raisecomIgmpFilterIpProfileEndAddress,'raisecomIgmpFilterIpProfileIpType':raisecomIgmpFilterIpProfileIpType,'raisecomIgmpFilterIpProfileRowStatus':raisecomIgmpFilterIpProfileRowStatus,'raisecomIgmpL2Conformance':raisecomIgmpL2Conformance})