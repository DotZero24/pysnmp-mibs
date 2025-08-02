_P='swIGMPSnpDataDrivenLearningGrpGrpAddr'
_O='swMLDSnpFwdGrpAddr'
_N='swMLDSnpFwdSrcAddr'
_M='swIGMPSnpGrpGrpAddr'
_L='swIGMPSnpGrpSrcAddr'
_K='swIGMPSnpFwdGrpAddr'
_J='swIGMPSnpFwdSrcAddr'
_I='swMLDSnoopingVlanID'
_H='disabled'
_G='enabled'
_F='swIGMPSnoopingVlanID'
_E='read-write'
_D='MCAST-SNOOPING-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swMcastSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,171,12,73))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwMcastSnoopingCtrl_ObjectIdentity=ObjectIdentity
swMcastSnoopingCtrl=_SwMcastSnoopingCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,73,1))
class _SwIGMPSnoopingGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwIGMPSnoopingGlobalState_Type.__name__=_C
_SwIGMPSnoopingGlobalState_Object=MibScalar
swIGMPSnoopingGlobalState=_SwIGMPSnoopingGlobalState_Object((1,3,6,1,4,1,171,12,73,1,1),_SwIGMPSnoopingGlobalState_Type())
swIGMPSnoopingGlobalState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnoopingGlobalState.setStatus(_A)
class _SwIGMPSnoopingMaxDataDrivenLearningCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwIGMPSnoopingMaxDataDrivenLearningCount_Type.__name__=_C
_SwIGMPSnoopingMaxDataDrivenLearningCount_Object=MibScalar
swIGMPSnoopingMaxDataDrivenLearningCount=_SwIGMPSnoopingMaxDataDrivenLearningCount_Object((1,3,6,1,4,1,171,12,73,1,3),_SwIGMPSnoopingMaxDataDrivenLearningCount_Type())
swIGMPSnoopingMaxDataDrivenLearningCount.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnoopingMaxDataDrivenLearningCount.setStatus(_A)
_SwMcastSnoopingInfo_ObjectIdentity=ObjectIdentity
swMcastSnoopingInfo=_SwMcastSnoopingInfo_ObjectIdentity((1,3,6,1,4,1,171,12,73,2))
_SwIGMPSnoopingInfo_ObjectIdentity=ObjectIdentity
swIGMPSnoopingInfo=_SwIGMPSnoopingInfo_ObjectIdentity((1,3,6,1,4,1,171,12,73,2,1))
_SwIGMPSnoopingForwardingTable_Object=MibTable
swIGMPSnoopingForwardingTable=_SwIGMPSnoopingForwardingTable_Object((1,3,6,1,4,1,171,12,73,2,1,1))
if mibBuilder.loadTexts:swIGMPSnoopingForwardingTable.setStatus(_A)
_SwIGMPSnoopingForwardingEntry_Object=MibTableRow
swIGMPSnoopingForwardingEntry=_SwIGMPSnoopingForwardingEntry_Object((1,3,6,1,4,1,171,12,73,2,1,1,1))
swIGMPSnoopingForwardingEntry.setIndexNames((0,_D,_F),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:swIGMPSnoopingForwardingEntry.setStatus(_A)
class _SwIGMPSnoopingVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwIGMPSnoopingVlanID_Type.__name__=_C
_SwIGMPSnoopingVlanID_Object=MibTableColumn
swIGMPSnoopingVlanID=_SwIGMPSnoopingVlanID_Object((1,3,6,1,4,1,171,12,73,2,1,1,1,1),_SwIGMPSnoopingVlanID_Type())
swIGMPSnoopingVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnoopingVlanID.setStatus(_A)
_SwIGMPSnpFwdSrcAddr_Type=IpAddress
_SwIGMPSnpFwdSrcAddr_Object=MibTableColumn
swIGMPSnpFwdSrcAddr=_SwIGMPSnpFwdSrcAddr_Object((1,3,6,1,4,1,171,12,73,2,1,1,1,2),_SwIGMPSnpFwdSrcAddr_Type())
swIGMPSnpFwdSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpFwdSrcAddr.setStatus(_A)
_SwIGMPSnpFwdGrpAddr_Type=IpAddress
_SwIGMPSnpFwdGrpAddr_Object=MibTableColumn
swIGMPSnpFwdGrpAddr=_SwIGMPSnpFwdGrpAddr_Object((1,3,6,1,4,1,171,12,73,2,1,1,1,3),_SwIGMPSnpFwdGrpAddr_Type())
swIGMPSnpFwdGrpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpFwdGrpAddr.setStatus(_A)
_SwIGMPSnpFwdMemberPorts_Type=PortList
_SwIGMPSnpFwdMemberPorts_Object=MibTableColumn
swIGMPSnpFwdMemberPorts=_SwIGMPSnpFwdMemberPorts_Object((1,3,6,1,4,1,171,12,73,2,1,1,1,4),_SwIGMPSnpFwdMemberPorts_Type())
swIGMPSnpFwdMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpFwdMemberPorts.setStatus(_A)
_SwIGMPSnoopingGroupTable_Object=MibTable
swIGMPSnoopingGroupTable=_SwIGMPSnoopingGroupTable_Object((1,3,6,1,4,1,171,12,73,2,1,2))
if mibBuilder.loadTexts:swIGMPSnoopingGroupTable.setStatus(_A)
_SwIGMPSnoopingGroupEntry_Object=MibTableRow
swIGMPSnoopingGroupEntry=_SwIGMPSnoopingGroupEntry_Object((1,3,6,1,4,1,171,12,73,2,1,2,1))
swIGMPSnoopingGroupEntry.setIndexNames((0,_D,_F),(0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swIGMPSnoopingGroupEntry.setStatus(_A)
_SwIGMPSnpGrpSrcAddr_Type=IpAddress
_SwIGMPSnpGrpSrcAddr_Object=MibTableColumn
swIGMPSnpGrpSrcAddr=_SwIGMPSnpGrpSrcAddr_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,1),_SwIGMPSnpGrpSrcAddr_Type())
swIGMPSnpGrpSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpSrcAddr.setStatus(_A)
_SwIGMPSnpGrpGrpAddr_Type=IpAddress
_SwIGMPSnpGrpGrpAddr_Object=MibTableColumn
swIGMPSnpGrpGrpAddr=_SwIGMPSnpGrpGrpAddr_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,2),_SwIGMPSnpGrpGrpAddr_Type())
swIGMPSnpGrpGrpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpGrpAddr.setStatus(_A)
_SwIGMPSnpGrpIncludeMemberPorts_Type=PortList
_SwIGMPSnpGrpIncludeMemberPorts_Object=MibTableColumn
swIGMPSnpGrpIncludeMemberPorts=_SwIGMPSnpGrpIncludeMemberPorts_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,3),_SwIGMPSnpGrpIncludeMemberPorts_Type())
swIGMPSnpGrpIncludeMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpIncludeMemberPorts.setStatus(_A)
_SwIGMPSnpGrpExcludeMemberPorts_Type=PortList
_SwIGMPSnpGrpExcludeMemberPorts_Object=MibTableColumn
swIGMPSnpGrpExcludeMemberPorts=_SwIGMPSnpGrpExcludeMemberPorts_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,4),_SwIGMPSnpGrpExcludeMemberPorts_Type())
swIGMPSnpGrpExcludeMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpExcludeMemberPorts.setStatus(_A)
_SwIGMPSnpGrpRouterPorts_Type=PortList
_SwIGMPSnpGrpRouterPorts_Object=MibTableColumn
swIGMPSnpGrpRouterPorts=_SwIGMPSnpGrpRouterPorts_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,5),_SwIGMPSnpGrpRouterPorts_Type())
swIGMPSnpGrpRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpRouterPorts.setStatus(_A)
_SwIGMPSnpGrpUpTime_Type=Integer32
_SwIGMPSnpGrpUpTime_Object=MibTableColumn
swIGMPSnpGrpUpTime=_SwIGMPSnpGrpUpTime_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,6),_SwIGMPSnpGrpUpTime_Type())
swIGMPSnpGrpUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpUpTime.setStatus(_A)
_SwIGMPSnpGrpExpiryTime_Type=Integer32
_SwIGMPSnpGrpExpiryTime_Object=MibTableColumn
swIGMPSnpGrpExpiryTime=_SwIGMPSnpGrpExpiryTime_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,7),_SwIGMPSnpGrpExpiryTime_Type())
swIGMPSnpGrpExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpExpiryTime.setStatus(_A)
_SwIGMPSnpGrpReportCount_Type=Integer32
_SwIGMPSnpGrpReportCount_Object=MibTableColumn
swIGMPSnpGrpReportCount=_SwIGMPSnpGrpReportCount_Object((1,3,6,1,4,1,171,12,73,2,1,2,1,8),_SwIGMPSnpGrpReportCount_Type())
swIGMPSnpGrpReportCount.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpGrpReportCount.setStatus(_A)
_SwMLDSnoopingInfo_ObjectIdentity=ObjectIdentity
swMLDSnoopingInfo=_SwMLDSnoopingInfo_ObjectIdentity((1,3,6,1,4,1,171,12,73,2,2))
_SwMLDSnoopingForwardingTable_Object=MibTable
swMLDSnoopingForwardingTable=_SwMLDSnoopingForwardingTable_Object((1,3,6,1,4,1,171,12,73,2,2,1))
if mibBuilder.loadTexts:swMLDSnoopingForwardingTable.setStatus(_A)
_SwMLDSnoopingForwardingEntry_Object=MibTableRow
swMLDSnoopingForwardingEntry=_SwMLDSnoopingForwardingEntry_Object((1,3,6,1,4,1,171,12,73,2,2,1,1))
swMLDSnoopingForwardingEntry.setIndexNames((0,_D,_I),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:swMLDSnoopingForwardingEntry.setStatus(_A)
class _SwMLDSnoopingVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwMLDSnoopingVlanID_Type.__name__=_C
_SwMLDSnoopingVlanID_Object=MibTableColumn
swMLDSnoopingVlanID=_SwMLDSnoopingVlanID_Object((1,3,6,1,4,1,171,12,73,2,2,1,1,1),_SwMLDSnoopingVlanID_Type())
swMLDSnoopingVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:swMLDSnoopingVlanID.setStatus(_A)
_SwMLDSnpFwdSrcAddr_Type=Ipv6Address
_SwMLDSnpFwdSrcAddr_Object=MibTableColumn
swMLDSnpFwdSrcAddr=_SwMLDSnpFwdSrcAddr_Object((1,3,6,1,4,1,171,12,73,2,2,1,1,2),_SwMLDSnpFwdSrcAddr_Type())
swMLDSnpFwdSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swMLDSnpFwdSrcAddr.setStatus(_A)
_SwMLDSnpFwdGrpAddr_Type=Ipv6Address
_SwMLDSnpFwdGrpAddr_Object=MibTableColumn
swMLDSnpFwdGrpAddr=_SwMLDSnpFwdGrpAddr_Object((1,3,6,1,4,1,171,12,73,2,2,1,1,3),_SwMLDSnpFwdGrpAddr_Type())
swMLDSnpFwdGrpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swMLDSnpFwdGrpAddr.setStatus(_A)
_SwMLDSnpFwdMemberPorts_Type=PortList
_SwMLDSnpFwdMemberPorts_Object=MibTableColumn
swMLDSnpFwdMemberPorts=_SwMLDSnpFwdMemberPorts_Object((1,3,6,1,4,1,171,12,73,2,2,1,1,4),_SwMLDSnpFwdMemberPorts_Type())
swMLDSnpFwdMemberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swMLDSnpFwdMemberPorts.setStatus(_A)
_SwMLDSnoopingVlanStatisticCounterTable_Object=MibTable
swMLDSnoopingVlanStatisticCounterTable=_SwMLDSnoopingVlanStatisticCounterTable_Object((1,3,6,1,4,1,171,12,73,2,2,3))
if mibBuilder.loadTexts:swMLDSnoopingVlanStatisticCounterTable.setStatus(_A)
_SwMLDSnoopingVlanStatisticCounterEntry_Object=MibTableRow
swMLDSnoopingVlanStatisticCounterEntry=_SwMLDSnoopingVlanStatisticCounterEntry_Object((1,3,6,1,4,1,171,12,73,2,2,3,1))
swMLDSnoopingVlanStatisticCounterEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:swMLDSnoopingVlanStatisticCounterEntry.setStatus(_A)
_SwMLDSnpVlanCounterTotalRxQuery_Type=Counter32
_SwMLDSnpVlanCounterTotalRxQuery_Object=MibTableColumn
swMLDSnpVlanCounterTotalRxQuery=_SwMLDSnpVlanCounterTotalRxQuery_Object((1,3,6,1,4,1,171,12,73,2,2,3,1,20),_SwMLDSnpVlanCounterTotalRxQuery_Type())
swMLDSnpVlanCounterTotalRxQuery.setMaxAccess(_B)
if mibBuilder.loadTexts:swMLDSnpVlanCounterTotalRxQuery.setStatus(_A)
_SwMcastSnoopingMgmt_ObjectIdentity=ObjectIdentity
swMcastSnoopingMgmt=_SwMcastSnoopingMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,73,3))
_SwIGMPSnoopingMgmt_ObjectIdentity=ObjectIdentity
swIGMPSnoopingMgmt=_SwIGMPSnoopingMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,73,3,1))
_SwIGMPSnoopingCtrlTable_Object=MibTable
swIGMPSnoopingCtrlTable=_SwIGMPSnoopingCtrlTable_Object((1,3,6,1,4,1,171,12,73,3,1,1))
if mibBuilder.loadTexts:swIGMPSnoopingCtrlTable.setStatus(_A)
_SwIGMPSnoopingCtrlEntry_Object=MibTableRow
swIGMPSnoopingCtrlEntry=_SwIGMPSnoopingCtrlEntry_Object((1,3,6,1,4,1,171,12,73,3,1,1,1))
swIGMPSnoopingCtrlEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:swIGMPSnoopingCtrlEntry.setStatus(_A)
class _SwIGMPSnpCtrlQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwIGMPSnpCtrlQueryInterval_Type.__name__=_C
_SwIGMPSnpCtrlQueryInterval_Object=MibTableColumn
swIGMPSnpCtrlQueryInterval=_SwIGMPSnpCtrlQueryInterval_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,5),_SwIGMPSnpCtrlQueryInterval_Type())
swIGMPSnpCtrlQueryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlQueryInterval.setStatus(_A)
class _SwIGMPSnpCtrlMaxResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwIGMPSnpCtrlMaxResponseTime_Type.__name__=_C
_SwIGMPSnpCtrlMaxResponseTime_Object=MibTableColumn
swIGMPSnpCtrlMaxResponseTime=_SwIGMPSnpCtrlMaxResponseTime_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,10),_SwIGMPSnpCtrlMaxResponseTime_Type())
swIGMPSnpCtrlMaxResponseTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlMaxResponseTime.setStatus(_A)
class _SwIGMPSnpCtrlRobustnessValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwIGMPSnpCtrlRobustnessValue_Type.__name__=_C
_SwIGMPSnpCtrlRobustnessValue_Object=MibTableColumn
swIGMPSnpCtrlRobustnessValue=_SwIGMPSnpCtrlRobustnessValue_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,15),_SwIGMPSnpCtrlRobustnessValue_Type())
swIGMPSnpCtrlRobustnessValue.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlRobustnessValue.setStatus(_A)
class _SwIGMPSnpCtrlLastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwIGMPSnpCtrlLastMemberQueryInterval_Type.__name__=_C
_SwIGMPSnpCtrlLastMemberQueryInterval_Object=MibTableColumn
swIGMPSnpCtrlLastMemberQueryInterval=_SwIGMPSnpCtrlLastMemberQueryInterval_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,20),_SwIGMPSnpCtrlLastMemberQueryInterval_Type())
swIGMPSnpCtrlLastMemberQueryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlLastMemberQueryInterval.setStatus(_A)
class _SwIGMPSnpCtrlQuerierState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwIGMPSnpCtrlQuerierState_Type.__name__=_C
_SwIGMPSnpCtrlQuerierState_Object=MibTableColumn
swIGMPSnpCtrlQuerierState=_SwIGMPSnpCtrlQuerierState_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,25),_SwIGMPSnpCtrlQuerierState_Type())
swIGMPSnpCtrlQuerierState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlQuerierState.setStatus(_A)
class _SwIGMPSnpCtrlQuerierRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('querier',1),('non-querier',2)))
_SwIGMPSnpCtrlQuerierRole_Type.__name__=_C
_SwIGMPSnpCtrlQuerierRole_Object=MibTableColumn
swIGMPSnpCtrlQuerierRole=_SwIGMPSnpCtrlQuerierRole_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,30),_SwIGMPSnpCtrlQuerierRole_Type())
swIGMPSnpCtrlQuerierRole.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpCtrlQuerierRole.setStatus(_A)
_SwIGMPSnpCtrlQuerierIP_Type=IpAddress
_SwIGMPSnpCtrlQuerierIP_Object=MibTableColumn
swIGMPSnpCtrlQuerierIP=_SwIGMPSnpCtrlQuerierIP_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,35),_SwIGMPSnpCtrlQuerierIP_Type())
swIGMPSnpCtrlQuerierIP.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpCtrlQuerierIP.setStatus(_A)
class _SwIGMPSnpCtrlQuerierExpiryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwIGMPSnpCtrlQuerierExpiryTime_Type.__name__=_C
_SwIGMPSnpCtrlQuerierExpiryTime_Object=MibTableColumn
swIGMPSnpCtrlQuerierExpiryTime=_SwIGMPSnpCtrlQuerierExpiryTime_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,40),_SwIGMPSnpCtrlQuerierExpiryTime_Type())
swIGMPSnpCtrlQuerierExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpCtrlQuerierExpiryTime.setStatus(_A)
class _SwIGMPSnpCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwIGMPSnpCtrlState_Type.__name__=_C
_SwIGMPSnpCtrlState_Object=MibTableColumn
swIGMPSnpCtrlState=_SwIGMPSnpCtrlState_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,45),_SwIGMPSnpCtrlState_Type())
swIGMPSnpCtrlState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlState.setStatus(_A)
class _SwIGMPSnpCtrlFastLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwIGMPSnpCtrlFastLeaveState_Type.__name__=_C
_SwIGMPSnpCtrlFastLeaveState_Object=MibTableColumn
swIGMPSnpCtrlFastLeaveState=_SwIGMPSnpCtrlFastLeaveState_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,50),_SwIGMPSnpCtrlFastLeaveState_Type())
swIGMPSnpCtrlFastLeaveState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlFastLeaveState.setStatus(_A)
class _SwIGMPSnpCtrlVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version-1',1),('version-2',2),('version-3',3)))
_SwIGMPSnpCtrlVersion_Type.__name__=_C
_SwIGMPSnpCtrlVersion_Object=MibTableColumn
swIGMPSnpCtrlVersion=_SwIGMPSnpCtrlVersion_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,60),_SwIGMPSnpCtrlVersion_Type())
swIGMPSnpCtrlVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlVersion.setStatus(_A)
class _SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Type.__name__=_C
_SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Object=MibTableColumn
swIGMPSnpCtrlDataDrivenLearningAgedOutState=_SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Object((1,3,6,1,4,1,171,12,73,3,1,1,1,70),_SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Type())
swIGMPSnpCtrlDataDrivenLearningAgedOutState.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpCtrlDataDrivenLearningAgedOutState.setStatus(_A)
_SwIGMPSnoopingDataDrivenLearningGroupTable_Object=MibTable
swIGMPSnoopingDataDrivenLearningGroupTable=_SwIGMPSnoopingDataDrivenLearningGroupTable_Object((1,3,6,1,4,1,171,12,73,3,1,3))
if mibBuilder.loadTexts:swIGMPSnoopingDataDrivenLearningGroupTable.setStatus(_A)
_SwIGMPSnoopingDataDrivenLearningGroupEntry_Object=MibTableRow
swIGMPSnoopingDataDrivenLearningGroupEntry=_SwIGMPSnoopingDataDrivenLearningGroupEntry_Object((1,3,6,1,4,1,171,12,73,3,1,3,1))
swIGMPSnoopingDataDrivenLearningGroupEntry.setIndexNames((0,_D,_F),(0,_D,_P))
if mibBuilder.loadTexts:swIGMPSnoopingDataDrivenLearningGroupEntry.setStatus(_A)
_SwIGMPSnpDataDrivenLearningGrpGrpAddr_Type=IpAddress
_SwIGMPSnpDataDrivenLearningGrpGrpAddr_Object=MibTableColumn
swIGMPSnpDataDrivenLearningGrpGrpAddr=_SwIGMPSnpDataDrivenLearningGrpGrpAddr_Object((1,3,6,1,4,1,171,12,73,3,1,3,1,1),_SwIGMPSnpDataDrivenLearningGrpGrpAddr_Type())
swIGMPSnpDataDrivenLearningGrpGrpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpDataDrivenLearningGrpGrpAddr.setStatus(_A)
_SwIGMPSnpDataDrivenLearningGrpRouterPorts_Type=PortList
_SwIGMPSnpDataDrivenLearningGrpRouterPorts_Object=MibTableColumn
swIGMPSnpDataDrivenLearningGrpRouterPorts=_SwIGMPSnpDataDrivenLearningGrpRouterPorts_Object((1,3,6,1,4,1,171,12,73,3,1,3,1,2),_SwIGMPSnpDataDrivenLearningGrpRouterPorts_Type())
swIGMPSnpDataDrivenLearningGrpRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpDataDrivenLearningGrpRouterPorts.setStatus(_A)
_SwIGMPSnpDataDrivenLearningGrpUpTime_Type=Integer32
_SwIGMPSnpDataDrivenLearningGrpUpTime_Object=MibTableColumn
swIGMPSnpDataDrivenLearningGrpUpTime=_SwIGMPSnpDataDrivenLearningGrpUpTime_Object((1,3,6,1,4,1,171,12,73,3,1,3,1,3),_SwIGMPSnpDataDrivenLearningGrpUpTime_Type())
swIGMPSnpDataDrivenLearningGrpUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpDataDrivenLearningGrpUpTime.setStatus(_A)
_SwIGMPSnpDataDrivenLearningGrpExpiryTime_Type=Integer32
_SwIGMPSnpDataDrivenLearningGrpExpiryTime_Object=MibTableColumn
swIGMPSnpDataDrivenLearningGrpExpiryTime=_SwIGMPSnpDataDrivenLearningGrpExpiryTime_Object((1,3,6,1,4,1,171,12,73,3,1,3,1,4),_SwIGMPSnpDataDrivenLearningGrpExpiryTime_Type())
swIGMPSnpDataDrivenLearningGrpExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpDataDrivenLearningGrpExpiryTime.setStatus(_A)
class _SwIGMPSnpDataDrivenLearningGrpClearGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('clear',2)))
_SwIGMPSnpDataDrivenLearningGrpClearGrp_Type.__name__=_C
_SwIGMPSnpDataDrivenLearningGrpClearGrp_Object=MibTableColumn
swIGMPSnpDataDrivenLearningGrpClearGrp=_SwIGMPSnpDataDrivenLearningGrpClearGrp_Object((1,3,6,1,4,1,171,12,73,3,1,3,1,100),_SwIGMPSnpDataDrivenLearningGrpClearGrp_Type())
swIGMPSnpDataDrivenLearningGrpClearGrp.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpDataDrivenLearningGrpClearGrp.setStatus(_A)
_SwIGMPSnoopingRouterPortTable_Object=MibTable
swIGMPSnoopingRouterPortTable=_SwIGMPSnoopingRouterPortTable_Object((1,3,6,1,4,1,171,12,73,3,1,4))
if mibBuilder.loadTexts:swIGMPSnoopingRouterPortTable.setStatus(_A)
_SwIGMPSnoopingRouterPortEntry_Object=MibTableRow
swIGMPSnoopingRouterPortEntry=_SwIGMPSnoopingRouterPortEntry_Object((1,3,6,1,4,1,171,12,73,3,1,4,1))
swIGMPSnoopingRouterPortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:swIGMPSnoopingRouterPortEntry.setStatus(_A)
_SwIGMPSnpStaticRouterPorts_Type=PortList
_SwIGMPSnpStaticRouterPorts_Object=MibTableColumn
swIGMPSnpStaticRouterPorts=_SwIGMPSnpStaticRouterPorts_Object((1,3,6,1,4,1,171,12,73,3,1,4,1,5),_SwIGMPSnpStaticRouterPorts_Type())
swIGMPSnpStaticRouterPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpStaticRouterPorts.setStatus(_A)
_SwIGMPSnpDynamicRouterPorts_Type=PortList
_SwIGMPSnpDynamicRouterPorts_Object=MibTableColumn
swIGMPSnpDynamicRouterPorts=_SwIGMPSnpDynamicRouterPorts_Object((1,3,6,1,4,1,171,12,73,3,1,4,1,10),_SwIGMPSnpDynamicRouterPorts_Type())
swIGMPSnpDynamicRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swIGMPSnpDynamicRouterPorts.setStatus(_A)
_SwIGMPSnpForbiddenRouterPorts_Type=PortList
_SwIGMPSnpForbiddenRouterPorts_Object=MibTableColumn
swIGMPSnpForbiddenRouterPorts=_SwIGMPSnpForbiddenRouterPorts_Object((1,3,6,1,4,1,171,12,73,3,1,4,1,15),_SwIGMPSnpForbiddenRouterPorts_Type())
swIGMPSnpForbiddenRouterPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:swIGMPSnpForbiddenRouterPorts.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'Ipv6Address':Ipv6Address,'PortList':PortList,'swMcastSnoopingMIB':swMcastSnoopingMIB,'swMcastSnoopingCtrl':swMcastSnoopingCtrl,'swIGMPSnoopingGlobalState':swIGMPSnoopingGlobalState,'swIGMPSnoopingMaxDataDrivenLearningCount':swIGMPSnoopingMaxDataDrivenLearningCount,'swMcastSnoopingInfo':swMcastSnoopingInfo,'swIGMPSnoopingInfo':swIGMPSnoopingInfo,'swIGMPSnoopingForwardingTable':swIGMPSnoopingForwardingTable,'swIGMPSnoopingForwardingEntry':swIGMPSnoopingForwardingEntry,_F:swIGMPSnoopingVlanID,_J:swIGMPSnpFwdSrcAddr,_K:swIGMPSnpFwdGrpAddr,'swIGMPSnpFwdMemberPorts':swIGMPSnpFwdMemberPorts,'swIGMPSnoopingGroupTable':swIGMPSnoopingGroupTable,'swIGMPSnoopingGroupEntry':swIGMPSnoopingGroupEntry,_L:swIGMPSnpGrpSrcAddr,_M:swIGMPSnpGrpGrpAddr,'swIGMPSnpGrpIncludeMemberPorts':swIGMPSnpGrpIncludeMemberPorts,'swIGMPSnpGrpExcludeMemberPorts':swIGMPSnpGrpExcludeMemberPorts,'swIGMPSnpGrpRouterPorts':swIGMPSnpGrpRouterPorts,'swIGMPSnpGrpUpTime':swIGMPSnpGrpUpTime,'swIGMPSnpGrpExpiryTime':swIGMPSnpGrpExpiryTime,'swIGMPSnpGrpReportCount':swIGMPSnpGrpReportCount,'swMLDSnoopingInfo':swMLDSnoopingInfo,'swMLDSnoopingForwardingTable':swMLDSnoopingForwardingTable,'swMLDSnoopingForwardingEntry':swMLDSnoopingForwardingEntry,_I:swMLDSnoopingVlanID,_N:swMLDSnpFwdSrcAddr,_O:swMLDSnpFwdGrpAddr,'swMLDSnpFwdMemberPorts':swMLDSnpFwdMemberPorts,'swMLDSnoopingVlanStatisticCounterTable':swMLDSnoopingVlanStatisticCounterTable,'swMLDSnoopingVlanStatisticCounterEntry':swMLDSnoopingVlanStatisticCounterEntry,'swMLDSnpVlanCounterTotalRxQuery':swMLDSnpVlanCounterTotalRxQuery,'swMcastSnoopingMgmt':swMcastSnoopingMgmt,'swIGMPSnoopingMgmt':swIGMPSnoopingMgmt,'swIGMPSnoopingCtrlTable':swIGMPSnoopingCtrlTable,'swIGMPSnoopingCtrlEntry':swIGMPSnoopingCtrlEntry,'swIGMPSnpCtrlQueryInterval':swIGMPSnpCtrlQueryInterval,'swIGMPSnpCtrlMaxResponseTime':swIGMPSnpCtrlMaxResponseTime,'swIGMPSnpCtrlRobustnessValue':swIGMPSnpCtrlRobustnessValue,'swIGMPSnpCtrlLastMemberQueryInterval':swIGMPSnpCtrlLastMemberQueryInterval,'swIGMPSnpCtrlQuerierState':swIGMPSnpCtrlQuerierState,'swIGMPSnpCtrlQuerierRole':swIGMPSnpCtrlQuerierRole,'swIGMPSnpCtrlQuerierIP':swIGMPSnpCtrlQuerierIP,'swIGMPSnpCtrlQuerierExpiryTime':swIGMPSnpCtrlQuerierExpiryTime,'swIGMPSnpCtrlState':swIGMPSnpCtrlState,'swIGMPSnpCtrlFastLeaveState':swIGMPSnpCtrlFastLeaveState,'swIGMPSnpCtrlVersion':swIGMPSnpCtrlVersion,'swIGMPSnpCtrlDataDrivenLearningAgedOutState':swIGMPSnpCtrlDataDrivenLearningAgedOutState,'swIGMPSnoopingDataDrivenLearningGroupTable':swIGMPSnoopingDataDrivenLearningGroupTable,'swIGMPSnoopingDataDrivenLearningGroupEntry':swIGMPSnoopingDataDrivenLearningGroupEntry,_P:swIGMPSnpDataDrivenLearningGrpGrpAddr,'swIGMPSnpDataDrivenLearningGrpRouterPorts':swIGMPSnpDataDrivenLearningGrpRouterPorts,'swIGMPSnpDataDrivenLearningGrpUpTime':swIGMPSnpDataDrivenLearningGrpUpTime,'swIGMPSnpDataDrivenLearningGrpExpiryTime':swIGMPSnpDataDrivenLearningGrpExpiryTime,'swIGMPSnpDataDrivenLearningGrpClearGrp':swIGMPSnpDataDrivenLearningGrpClearGrp,'swIGMPSnoopingRouterPortTable':swIGMPSnoopingRouterPortTable,'swIGMPSnoopingRouterPortEntry':swIGMPSnoopingRouterPortEntry,'swIGMPSnpStaticRouterPorts':swIGMPSnpStaticRouterPorts,'swIGMPSnpDynamicRouterPorts':swIGMPSnpDynamicRouterPorts,'swIGMPSnpForbiddenRouterPorts':swIGMPSnpForbiddenRouterPorts})