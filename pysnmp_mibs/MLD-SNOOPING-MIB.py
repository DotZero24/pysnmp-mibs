_U='swMldSnpMutiGroupIpAddr'
_T='swMldSnpSourceIpAddr'
_S='swMldSnpVid'
_R='swMldSnoopingGroupSourceAddr'
_Q='swMldSnoopingGroupGroupAddr'
_P='swMldSnoopingGroupVid'
_O='swMldSnpRouterPortsVid'
_N='swMldSnoopingGroupInfoIpAddr'
_M='swMldSnoopingGroupInfoVid'
_L='enable'
_K='disable'
_J='swMldSnoopingCtrlVid'
_I='enabled'
_H='disabled'
_G='other'
_F='obsolete'
_E='MLD-SNOOPING-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swMldSnpMIB=ModuleIdentity((1,3,6,1,4,1,171,12,34))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwMldSnpCtrl_ObjectIdentity=ObjectIdentity
swMldSnpCtrl=_SwMldSnpCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,34,1))
class _SwMldSnoopingGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwMldSnoopingGlobalState_Type.__name__=_B
_SwMldSnoopingGlobalState_Object=MibScalar
swMldSnoopingGlobalState=_SwMldSnoopingGlobalState_Object((1,3,6,1,4,1,171,12,34,1,1),_SwMldSnoopingGlobalState_Type())
swMldSnoopingGlobalState.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingGlobalState.setStatus(_A)
class _SwMldSnoopingMcstRTOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwMldSnoopingMcstRTOnly_Type.__name__=_B
_SwMldSnoopingMcstRTOnly_Object=MibScalar
swMldSnoopingMcstRTOnly=_SwMldSnoopingMcstRTOnly_Object((1,3,6,1,4,1,171,12,34,1,2),_SwMldSnoopingMcstRTOnly_Type())
swMldSnoopingMcstRTOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingMcstRTOnly.setStatus(_A)
_SwMldSnpInfo_ObjectIdentity=ObjectIdentity
swMldSnpInfo=_SwMldSnpInfo_ObjectIdentity((1,3,6,1,4,1,171,12,34,2))
_SwMldSnpMgmt_ObjectIdentity=ObjectIdentity
swMldSnpMgmt=_SwMldSnpMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,34,3))
class _SwMldSnoopingMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnoopingMaxSupportedVlans_Type.__name__=_B
_SwMldSnoopingMaxSupportedVlans_Object=MibScalar
swMldSnoopingMaxSupportedVlans=_SwMldSnoopingMaxSupportedVlans_Object((1,3,6,1,4,1,171,12,34,3,1),_SwMldSnoopingMaxSupportedVlans_Type())
swMldSnoopingMaxSupportedVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingMaxSupportedVlans.setStatus(_A)
_SwMldSnoopingCtrlTable_Object=MibTable
swMldSnoopingCtrlTable=_SwMldSnoopingCtrlTable_Object((1,3,6,1,4,1,171,12,34,3,2))
if mibBuilder.loadTexts:swMldSnoopingCtrlTable.setStatus(_A)
_SwMldSnoopingCtrlEntry_Object=MibTableRow
swMldSnoopingCtrlEntry=_SwMldSnoopingCtrlEntry_Object((1,3,6,1,4,1,171,12,34,3,2,1))
swMldSnoopingCtrlEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:swMldSnoopingCtrlEntry.setStatus(_A)
class _SwMldSnoopingCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnoopingCtrlVid_Type.__name__=_B
_SwMldSnoopingCtrlVid_Object=MibTableColumn
swMldSnoopingCtrlVid=_SwMldSnoopingCtrlVid_Object((1,3,6,1,4,1,171,12,34,3,2,1,1),_SwMldSnoopingCtrlVid_Type())
swMldSnoopingCtrlVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingCtrlVid.setStatus(_A)
class _SwMldSnoopingQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwMldSnoopingQueryInterval_Type.__name__=_B
_SwMldSnoopingQueryInterval_Object=MibTableColumn
swMldSnoopingQueryInterval=_SwMldSnoopingQueryInterval_Object((1,3,6,1,4,1,171,12,34,3,2,1,2),_SwMldSnoopingQueryInterval_Type())
swMldSnoopingQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingQueryInterval.setStatus(_A)
class _SwMldSnoopingMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwMldSnoopingMaxResponseTime_Type.__name__=_B
_SwMldSnoopingMaxResponseTime_Object=MibTableColumn
swMldSnoopingMaxResponseTime=_SwMldSnoopingMaxResponseTime_Object((1,3,6,1,4,1,171,12,34,3,2,1,3),_SwMldSnoopingMaxResponseTime_Type())
swMldSnoopingMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingMaxResponseTime.setStatus(_A)
class _SwMldSnoopingRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwMldSnoopingRobustness_Type.__name__=_B
_SwMldSnoopingRobustness_Object=MibTableColumn
swMldSnoopingRobustness=_SwMldSnoopingRobustness_Object((1,3,6,1,4,1,171,12,34,3,2,1,4),_SwMldSnoopingRobustness_Type())
swMldSnoopingRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingRobustness.setStatus(_A)
class _SwMldSnoopingLastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwMldSnoopingLastMemberQueryInterval_Type.__name__=_B
_SwMldSnoopingLastMemberQueryInterval_Object=MibTableColumn
swMldSnoopingLastMemberQueryInterval=_SwMldSnoopingLastMemberQueryInterval_Object((1,3,6,1,4,1,171,12,34,3,2,1,5),_SwMldSnoopingLastMemberQueryInterval_Type())
swMldSnoopingLastMemberQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingLastMemberQueryInterval.setStatus(_A)
class _SwMldSnoopingHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwMldSnoopingHostTimeout_Type.__name__=_B
_SwMldSnoopingHostTimeout_Object=MibTableColumn
swMldSnoopingHostTimeout=_SwMldSnoopingHostTimeout_Object((1,3,6,1,4,1,171,12,34,3,2,1,6),_SwMldSnoopingHostTimeout_Type())
swMldSnoopingHostTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingHostTimeout.setStatus(_A)
class _SwMldSnoopingRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwMldSnoopingRouteTimeout_Type.__name__=_B
_SwMldSnoopingRouteTimeout_Object=MibTableColumn
swMldSnoopingRouteTimeout=_SwMldSnoopingRouteTimeout_Object((1,3,6,1,4,1,171,12,34,3,2,1,7),_SwMldSnoopingRouteTimeout_Type())
swMldSnoopingRouteTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingRouteTimeout.setStatus(_A)
class _SwMldSnoopingDoneTimer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwMldSnoopingDoneTimer_Type.__name__=_B
_SwMldSnoopingDoneTimer_Object=MibTableColumn
swMldSnoopingDoneTimer=_SwMldSnoopingDoneTimer_Object((1,3,6,1,4,1,171,12,34,3,2,1,8),_SwMldSnoopingDoneTimer_Type())
swMldSnoopingDoneTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingDoneTimer.setStatus(_A)
class _SwMldSnoopingQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwMldSnoopingQueryState_Type.__name__=_B
_SwMldSnoopingQueryState_Object=MibTableColumn
swMldSnoopingQueryState=_SwMldSnoopingQueryState_Object((1,3,6,1,4,1,171,12,34,3,2,1,9),_SwMldSnoopingQueryState_Type())
swMldSnoopingQueryState.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingQueryState.setStatus(_A)
class _SwMldSnoopingCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('querier',2),('non-querier',3)))
_SwMldSnoopingCurrentState_Type.__name__=_B
_SwMldSnoopingCurrentState_Object=MibTableColumn
swMldSnoopingCurrentState=_SwMldSnoopingCurrentState_Object((1,3,6,1,4,1,171,12,34,3,2,1,10),_SwMldSnoopingCurrentState_Type())
swMldSnoopingCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingCurrentState.setStatus(_A)
class _SwMldSnoopingCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_K,2),(_L,3)))
_SwMldSnoopingCtrlState_Type.__name__=_B
_SwMldSnoopingCtrlState_Object=MibTableColumn
swMldSnoopingCtrlState=_SwMldSnoopingCtrlState_Object((1,3,6,1,4,1,171,12,34,3,2,1,11),_SwMldSnoopingCtrlState_Type())
swMldSnoopingCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingCtrlState.setStatus(_A)
class _SwMldSnoopingFastDoneState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_K,2),(_L,3)))
_SwMldSnoopingFastDoneState_Type.__name__=_B
_SwMldSnoopingFastDoneState_Object=MibTableColumn
swMldSnoopingFastDoneState=_SwMldSnoopingFastDoneState_Object((1,3,6,1,4,1,171,12,34,3,2,1,12),_SwMldSnoopingFastDoneState_Type())
swMldSnoopingFastDoneState.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingFastDoneState.setStatus(_A)
class _SwMldSnoopingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version-1',1),('version-2',2)))
_SwMldSnoopingVersion_Type.__name__=_B
_SwMldSnoopingVersion_Object=MibTableColumn
swMldSnoopingVersion=_SwMldSnoopingVersion_Object((1,3,6,1,4,1,171,12,34,3,2,1,13),_SwMldSnoopingVersion_Type())
swMldSnoopingVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnoopingVersion.setStatus(_A)
_SwMldSnoopingGroupInfoTable_Object=MibTable
swMldSnoopingGroupInfoTable=_SwMldSnoopingGroupInfoTable_Object((1,3,6,1,4,1,171,12,34,3,3))
if mibBuilder.loadTexts:swMldSnoopingGroupInfoTable.setStatus(_F)
_SwMldSnoopingGroupInfoEntry_Object=MibTableRow
swMldSnoopingGroupInfoEntry=_SwMldSnoopingGroupInfoEntry_Object((1,3,6,1,4,1,171,12,34,3,3,1))
swMldSnoopingGroupInfoEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:swMldSnoopingGroupInfoEntry.setStatus(_F)
class _SwMldSnoopingGroupInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnoopingGroupInfoVid_Type.__name__=_B
_SwMldSnoopingGroupInfoVid_Object=MibTableColumn
swMldSnoopingGroupInfoVid=_SwMldSnoopingGroupInfoVid_Object((1,3,6,1,4,1,171,12,34,3,3,1,1),_SwMldSnoopingGroupInfoVid_Type())
swMldSnoopingGroupInfoVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupInfoVid.setStatus(_F)
_SwMldSnoopingGroupInfoIpAddr_Type=Ipv6Address
_SwMldSnoopingGroupInfoIpAddr_Object=MibTableColumn
swMldSnoopingGroupInfoIpAddr=_SwMldSnoopingGroupInfoIpAddr_Object((1,3,6,1,4,1,171,12,34,3,3,1,2),_SwMldSnoopingGroupInfoIpAddr_Type())
swMldSnoopingGroupInfoIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupInfoIpAddr.setStatus(_F)
_SwMldSnoopingGroupInfoMacAddr_Type=MacAddress
_SwMldSnoopingGroupInfoMacAddr_Object=MibTableColumn
swMldSnoopingGroupInfoMacAddr=_SwMldSnoopingGroupInfoMacAddr_Object((1,3,6,1,4,1,171,12,34,3,3,1,3),_SwMldSnoopingGroupInfoMacAddr_Type())
swMldSnoopingGroupInfoMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupInfoMacAddr.setStatus(_F)
_SwMldSnoopingGroupInfoPortMap_Type=PortList
_SwMldSnoopingGroupInfoPortMap_Object=MibTableColumn
swMldSnoopingGroupInfoPortMap=_SwMldSnoopingGroupInfoPortMap_Object((1,3,6,1,4,1,171,12,34,3,3,1,4),_SwMldSnoopingGroupInfoPortMap_Type())
swMldSnoopingGroupInfoPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupInfoPortMap.setStatus(_F)
class _SwMldSnoopingGroupInfoReportCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnoopingGroupInfoReportCount_Type.__name__=_B
_SwMldSnoopingGroupInfoReportCount_Object=MibTableColumn
swMldSnoopingGroupInfoReportCount=_SwMldSnoopingGroupInfoReportCount_Object((1,3,6,1,4,1,171,12,34,3,3,1,5),_SwMldSnoopingGroupInfoReportCount_Type())
swMldSnoopingGroupInfoReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupInfoReportCount.setStatus(_F)
_SwMldSnpRouterPortsTable_Object=MibTable
swMldSnpRouterPortsTable=_SwMldSnpRouterPortsTable_Object((1,3,6,1,4,1,171,12,34,3,4))
if mibBuilder.loadTexts:swMldSnpRouterPortsTable.setStatus(_A)
_SwMldSnpRouterPortsEntry_Object=MibTableRow
swMldSnpRouterPortsEntry=_SwMldSnpRouterPortsEntry_Object((1,3,6,1,4,1,171,12,34,3,4,1))
swMldSnpRouterPortsEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:swMldSnpRouterPortsEntry.setStatus(_A)
class _SwMldSnpRouterPortsVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnpRouterPortsVid_Type.__name__=_B
_SwMldSnpRouterPortsVid_Object=MibTableColumn
swMldSnpRouterPortsVid=_SwMldSnpRouterPortsVid_Object((1,3,6,1,4,1,171,12,34,3,4,1,1),_SwMldSnpRouterPortsVid_Type())
swMldSnpRouterPortsVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnpRouterPortsVid.setStatus(_A)
_SwMldSnpRouterStaticPortList_Type=PortList
_SwMldSnpRouterStaticPortList_Object=MibTableColumn
swMldSnpRouterStaticPortList=_SwMldSnpRouterStaticPortList_Object((1,3,6,1,4,1,171,12,34,3,4,1,2),_SwMldSnpRouterStaticPortList_Type())
swMldSnpRouterStaticPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnpRouterStaticPortList.setStatus(_A)
_SwMldSnpRouterDynamicPortList_Type=PortList
_SwMldSnpRouterDynamicPortList_Object=MibTableColumn
swMldSnpRouterDynamicPortList=_SwMldSnpRouterDynamicPortList_Object((1,3,6,1,4,1,171,12,34,3,4,1,3),_SwMldSnpRouterDynamicPortList_Type())
swMldSnpRouterDynamicPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnpRouterDynamicPortList.setStatus(_A)
_SwMldSnpRouterForbiddenPortList_Type=PortList
_SwMldSnpRouterForbiddenPortList_Object=MibTableColumn
swMldSnpRouterForbiddenPortList=_SwMldSnpRouterForbiddenPortList_Object((1,3,6,1,4,1,171,12,34,3,4,1,4),_SwMldSnpRouterForbiddenPortList_Type())
swMldSnpRouterForbiddenPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swMldSnpRouterForbiddenPortList.setStatus(_A)
_SwMldSnoopingGroupTable_Object=MibTable
swMldSnoopingGroupTable=_SwMldSnoopingGroupTable_Object((1,3,6,1,4,1,171,12,34,3,5))
if mibBuilder.loadTexts:swMldSnoopingGroupTable.setStatus(_A)
_SwMldSnoopingGroupEntry_Object=MibTableRow
swMldSnoopingGroupEntry=_SwMldSnoopingGroupEntry_Object((1,3,6,1,4,1,171,12,34,3,5,1))
swMldSnoopingGroupEntry.setIndexNames((0,_E,_P),(0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:swMldSnoopingGroupEntry.setStatus(_A)
class _SwMldSnoopingGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnoopingGroupVid_Type.__name__=_B
_SwMldSnoopingGroupVid_Object=MibTableColumn
swMldSnoopingGroupVid=_SwMldSnoopingGroupVid_Object((1,3,6,1,4,1,171,12,34,3,5,1,1),_SwMldSnoopingGroupVid_Type())
swMldSnoopingGroupVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupVid.setStatus(_A)
_SwMldSnoopingGroupGroupAddr_Type=Ipv6Address
_SwMldSnoopingGroupGroupAddr_Object=MibTableColumn
swMldSnoopingGroupGroupAddr=_SwMldSnoopingGroupGroupAddr_Object((1,3,6,1,4,1,171,12,34,3,5,1,2),_SwMldSnoopingGroupGroupAddr_Type())
swMldSnoopingGroupGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupGroupAddr.setStatus(_A)
_SwMldSnoopingGroupSourceAddr_Type=Ipv6Address
_SwMldSnoopingGroupSourceAddr_Object=MibTableColumn
swMldSnoopingGroupSourceAddr=_SwMldSnoopingGroupSourceAddr_Object((1,3,6,1,4,1,171,12,34,3,5,1,3),_SwMldSnoopingGroupSourceAddr_Type())
swMldSnoopingGroupSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupSourceAddr.setStatus(_A)
_SwMldSnoopingGroupIncludePortMap_Type=PortList
_SwMldSnoopingGroupIncludePortMap_Object=MibTableColumn
swMldSnoopingGroupIncludePortMap=_SwMldSnoopingGroupIncludePortMap_Object((1,3,6,1,4,1,171,12,34,3,5,1,4),_SwMldSnoopingGroupIncludePortMap_Type())
swMldSnoopingGroupIncludePortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupIncludePortMap.setStatus(_A)
_SwMldSnoopingGroupExcludePortMap_Type=PortList
_SwMldSnoopingGroupExcludePortMap_Object=MibTableColumn
swMldSnoopingGroupExcludePortMap=_SwMldSnoopingGroupExcludePortMap_Object((1,3,6,1,4,1,171,12,34,3,5,1,5),_SwMldSnoopingGroupExcludePortMap_Type())
swMldSnoopingGroupExcludePortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnoopingGroupExcludePortMap.setStatus(_A)
_SwMldSnpForwardingTable_Object=MibTable
swMldSnpForwardingTable=_SwMldSnpForwardingTable_Object((1,3,6,1,4,1,171,12,34,3,6))
if mibBuilder.loadTexts:swMldSnpForwardingTable.setStatus(_A)
_SwMldSnpForwardingEntry_Object=MibTableRow
swMldSnpForwardingEntry=_SwMldSnpForwardingEntry_Object((1,3,6,1,4,1,171,12,34,3,6,1))
swMldSnpForwardingEntry.setIndexNames((0,_E,_S),(0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:swMldSnpForwardingEntry.setStatus(_A)
class _SwMldSnpVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMldSnpVid_Type.__name__=_B
_SwMldSnpVid_Object=MibTableColumn
swMldSnpVid=_SwMldSnpVid_Object((1,3,6,1,4,1,171,12,34,3,6,1,1),_SwMldSnpVid_Type())
swMldSnpVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnpVid.setStatus(_A)
_SwMldSnpSourceIpAddr_Type=Ipv6Address
_SwMldSnpSourceIpAddr_Object=MibTableColumn
swMldSnpSourceIpAddr=_SwMldSnpSourceIpAddr_Object((1,3,6,1,4,1,171,12,34,3,6,1,2),_SwMldSnpSourceIpAddr_Type())
swMldSnpSourceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnpSourceIpAddr.setStatus(_A)
_SwMldSnpMutiGroupIpAddr_Type=Ipv6Address
_SwMldSnpMutiGroupIpAddr_Object=MibTableColumn
swMldSnpMutiGroupIpAddr=_SwMldSnpMutiGroupIpAddr_Object((1,3,6,1,4,1,171,12,34,3,6,1,3),_SwMldSnpMutiGroupIpAddr_Type())
swMldSnpMutiGroupIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnpMutiGroupIpAddr.setStatus(_A)
_SwMldSnpForwardingListenPort_Type=PortList
_SwMldSnpForwardingListenPort_Object=MibTableColumn
swMldSnpForwardingListenPort=_SwMldSnpForwardingListenPort_Object((1,3,6,1,4,1,171,12,34,3,6,1,4),_SwMldSnpForwardingListenPort_Type())
swMldSnpForwardingListenPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swMldSnpForwardingListenPort.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Ipv6Address':Ipv6Address,'PortList':PortList,'swMldSnpMIB':swMldSnpMIB,'swMldSnpCtrl':swMldSnpCtrl,'swMldSnoopingGlobalState':swMldSnoopingGlobalState,'swMldSnoopingMcstRTOnly':swMldSnoopingMcstRTOnly,'swMldSnpInfo':swMldSnpInfo,'swMldSnpMgmt':swMldSnpMgmt,'swMldSnoopingMaxSupportedVlans':swMldSnoopingMaxSupportedVlans,'swMldSnoopingCtrlTable':swMldSnoopingCtrlTable,'swMldSnoopingCtrlEntry':swMldSnoopingCtrlEntry,_J:swMldSnoopingCtrlVid,'swMldSnoopingQueryInterval':swMldSnoopingQueryInterval,'swMldSnoopingMaxResponseTime':swMldSnoopingMaxResponseTime,'swMldSnoopingRobustness':swMldSnoopingRobustness,'swMldSnoopingLastMemberQueryInterval':swMldSnoopingLastMemberQueryInterval,'swMldSnoopingHostTimeout':swMldSnoopingHostTimeout,'swMldSnoopingRouteTimeout':swMldSnoopingRouteTimeout,'swMldSnoopingDoneTimer':swMldSnoopingDoneTimer,'swMldSnoopingQueryState':swMldSnoopingQueryState,'swMldSnoopingCurrentState':swMldSnoopingCurrentState,'swMldSnoopingCtrlState':swMldSnoopingCtrlState,'swMldSnoopingFastDoneState':swMldSnoopingFastDoneState,'swMldSnoopingVersion':swMldSnoopingVersion,'swMldSnoopingGroupInfoTable':swMldSnoopingGroupInfoTable,'swMldSnoopingGroupInfoEntry':swMldSnoopingGroupInfoEntry,_M:swMldSnoopingGroupInfoVid,_N:swMldSnoopingGroupInfoIpAddr,'swMldSnoopingGroupInfoMacAddr':swMldSnoopingGroupInfoMacAddr,'swMldSnoopingGroupInfoPortMap':swMldSnoopingGroupInfoPortMap,'swMldSnoopingGroupInfoReportCount':swMldSnoopingGroupInfoReportCount,'swMldSnpRouterPortsTable':swMldSnpRouterPortsTable,'swMldSnpRouterPortsEntry':swMldSnpRouterPortsEntry,_O:swMldSnpRouterPortsVid,'swMldSnpRouterStaticPortList':swMldSnpRouterStaticPortList,'swMldSnpRouterDynamicPortList':swMldSnpRouterDynamicPortList,'swMldSnpRouterForbiddenPortList':swMldSnpRouterForbiddenPortList,'swMldSnoopingGroupTable':swMldSnoopingGroupTable,'swMldSnoopingGroupEntry':swMldSnoopingGroupEntry,_P:swMldSnoopingGroupVid,_Q:swMldSnoopingGroupGroupAddr,_R:swMldSnoopingGroupSourceAddr,'swMldSnoopingGroupIncludePortMap':swMldSnoopingGroupIncludePortMap,'swMldSnoopingGroupExcludePortMap':swMldSnoopingGroupExcludePortMap,'swMldSnpForwardingTable':swMldSnpForwardingTable,'swMldSnpForwardingEntry':swMldSnpForwardingEntry,_S:swMldSnpVid,_T:swMldSnpSourceIpAddr,_U:swMldSnpMutiGroupIpAddr,'swMldSnpForwardingListenPort':swMldSnpForwardingListenPort})