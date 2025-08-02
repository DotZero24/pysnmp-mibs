_S='swMLDProxyUpstreamIndex'
_R='read-create'
_Q='swIGMPProxyUpstreamIndex'
_P='swMLDProxyGroupSrcAddr'
_O='swMLDProxyGroupDesAddr'
_N='inactive'
_M='active'
_L='swIGMPProxyGroupSrcAddr'
_K='swIGMPProxyGroupDesAddr'
_J='disabled'
_I='enabled'
_H='swMLDProxyDownstreamVlanID'
_G='swIGMPProxyDownstreamVlanID'
_F='read-only'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='MCAST-PROXY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
PortList,VlanId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swMcastProxyMIB=ModuleIdentity((1,3,6,1,4,1,171,12,80))
_SwMcastProxyCtrl_ObjectIdentity=ObjectIdentity
swMcastProxyCtrl=_SwMcastProxyCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,80,1))
class _SwIGMPProxyGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SwIGMPProxyGlobalState_Type.__name__=_E
_SwIGMPProxyGlobalState_Object=MibScalar
swIGMPProxyGlobalState=_SwIGMPProxyGlobalState_Object((1,3,6,1,4,1,171,12,80,1,1),_SwIGMPProxyGlobalState_Type())
swIGMPProxyGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPProxyGlobalState.setStatus(_A)
class _SwMLDProxyGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_SwMLDProxyGlobalState_Type.__name__=_E
_SwMLDProxyGlobalState_Object=MibScalar
swMLDProxyGlobalState=_SwMLDProxyGlobalState_Object((1,3,6,1,4,1,171,12,80,1,2),_SwMLDProxyGlobalState_Type())
swMLDProxyGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMLDProxyGlobalState.setStatus(_A)
_SwMcastProxyInfo_ObjectIdentity=ObjectIdentity
swMcastProxyInfo=_SwMcastProxyInfo_ObjectIdentity((1,3,6,1,4,1,171,12,80,2))
_SwIGMPProxyInfo_ObjectIdentity=ObjectIdentity
swIGMPProxyInfo=_SwIGMPProxyInfo_ObjectIdentity((1,3,6,1,4,1,171,12,80,2,1))
_SwIGMPProxyGroupTable_Object=MibTable
swIGMPProxyGroupTable=_SwIGMPProxyGroupTable_Object((1,3,6,1,4,1,171,12,80,2,1,1))
if mibBuilder.loadTexts:swIGMPProxyGroupTable.setStatus(_A)
_SwIGMPProxyGroupEntry_Object=MibTableRow
swIGMPProxyGroupEntry=_SwIGMPProxyGroupEntry_Object((1,3,6,1,4,1,171,12,80,2,1,1,1))
swIGMPProxyGroupEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:swIGMPProxyGroupEntry.setStatus(_A)
_SwIGMPProxyGroupDesAddr_Type=IpAddress
_SwIGMPProxyGroupDesAddr_Object=MibTableColumn
swIGMPProxyGroupDesAddr=_SwIGMPProxyGroupDesAddr_Object((1,3,6,1,4,1,171,12,80,2,1,1,1,1),_SwIGMPProxyGroupDesAddr_Type())
swIGMPProxyGroupDesAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPProxyGroupDesAddr.setStatus(_A)
_SwIGMPProxyGroupSrcAddr_Type=IpAddress
_SwIGMPProxyGroupSrcAddr_Object=MibTableColumn
swIGMPProxyGroupSrcAddr=_SwIGMPProxyGroupSrcAddr_Object((1,3,6,1,4,1,171,12,80,2,1,1,1,2),_SwIGMPProxyGroupSrcAddr_Type())
swIGMPProxyGroupSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPProxyGroupSrcAddr.setStatus(_A)
_SwIGMPProxyDownstreamVlanID_Type=VlanId
_SwIGMPProxyDownstreamVlanID_Object=MibTableColumn
swIGMPProxyDownstreamVlanID=_SwIGMPProxyDownstreamVlanID_Object((1,3,6,1,4,1,171,12,80,2,1,1,1,3),_SwIGMPProxyDownstreamVlanID_Type())
swIGMPProxyDownstreamVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPProxyDownstreamVlanID.setStatus(_A)
_SwIGMPProxyDownstreamVlanMemberPorts_Type=PortList
_SwIGMPProxyDownstreamVlanMemberPorts_Object=MibTableColumn
swIGMPProxyDownstreamVlanMemberPorts=_SwIGMPProxyDownstreamVlanMemberPorts_Object((1,3,6,1,4,1,171,12,80,2,1,1,1,4),_SwIGMPProxyDownstreamVlanMemberPorts_Type())
swIGMPProxyDownstreamVlanMemberPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:swIGMPProxyDownstreamVlanMemberPorts.setStatus(_A)
class _SwIGMPProxyGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwIGMPProxyGroupStatus_Type.__name__=_E
_SwIGMPProxyGroupStatus_Object=MibTableColumn
swIGMPProxyGroupStatus=_SwIGMPProxyGroupStatus_Object((1,3,6,1,4,1,171,12,80,2,1,1,1,5),_SwIGMPProxyGroupStatus_Type())
swIGMPProxyGroupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:swIGMPProxyGroupStatus.setStatus(_A)
_SwMLDProxyInfo_ObjectIdentity=ObjectIdentity
swMLDProxyInfo=_SwMLDProxyInfo_ObjectIdentity((1,3,6,1,4,1,171,12,80,2,2))
_SwMLDProxyGroupTable_Object=MibTable
swMLDProxyGroupTable=_SwMLDProxyGroupTable_Object((1,3,6,1,4,1,171,12,80,2,2,1))
if mibBuilder.loadTexts:swMLDProxyGroupTable.setStatus(_A)
_SwMLDProxyGroupEntry_Object=MibTableRow
swMLDProxyGroupEntry=_SwMLDProxyGroupEntry_Object((1,3,6,1,4,1,171,12,80,2,2,1,1))
swMLDProxyGroupEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_H))
if mibBuilder.loadTexts:swMLDProxyGroupEntry.setStatus(_A)
_SwMLDProxyGroupDesAddr_Type=Ipv6Address
_SwMLDProxyGroupDesAddr_Object=MibTableColumn
swMLDProxyGroupDesAddr=_SwMLDProxyGroupDesAddr_Object((1,3,6,1,4,1,171,12,80,2,2,1,1,1),_SwMLDProxyGroupDesAddr_Type())
swMLDProxyGroupDesAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swMLDProxyGroupDesAddr.setStatus(_A)
_SwMLDProxyGroupSrcAddr_Type=Ipv6Address
_SwMLDProxyGroupSrcAddr_Object=MibTableColumn
swMLDProxyGroupSrcAddr=_SwMLDProxyGroupSrcAddr_Object((1,3,6,1,4,1,171,12,80,2,2,1,1,2),_SwMLDProxyGroupSrcAddr_Type())
swMLDProxyGroupSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swMLDProxyGroupSrcAddr.setStatus(_A)
_SwMLDProxyDownstreamVlanID_Type=VlanId
_SwMLDProxyDownstreamVlanID_Object=MibTableColumn
swMLDProxyDownstreamVlanID=_SwMLDProxyDownstreamVlanID_Object((1,3,6,1,4,1,171,12,80,2,2,1,1,3),_SwMLDProxyDownstreamVlanID_Type())
swMLDProxyDownstreamVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:swMLDProxyDownstreamVlanID.setStatus(_A)
_SwMLDProxyDownstreamVlanMemberPorts_Type=PortList
_SwMLDProxyDownstreamVlanMemberPorts_Object=MibTableColumn
swMLDProxyDownstreamVlanMemberPorts=_SwMLDProxyDownstreamVlanMemberPorts_Object((1,3,6,1,4,1,171,12,80,2,2,1,1,4),_SwMLDProxyDownstreamVlanMemberPorts_Type())
swMLDProxyDownstreamVlanMemberPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:swMLDProxyDownstreamVlanMemberPorts.setStatus(_A)
class _SwMLDProxyGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SwMLDProxyGroupStatus_Type.__name__=_E
_SwMLDProxyGroupStatus_Object=MibTableColumn
swMLDProxyGroupStatus=_SwMLDProxyGroupStatus_Object((1,3,6,1,4,1,171,12,80,2,2,1,1,5),_SwMLDProxyGroupStatus_Type())
swMLDProxyGroupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:swMLDProxyGroupStatus.setStatus(_A)
_SwMcastProxyMgmt_ObjectIdentity=ObjectIdentity
swMcastProxyMgmt=_SwMcastProxyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,80,3))
_SwIGMPProxyMgmt_ObjectIdentity=ObjectIdentity
swIGMPProxyMgmt=_SwIGMPProxyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,80,3,1))
_SwIGMPProxyUpstreamInterfaceTable_Object=MibTable
swIGMPProxyUpstreamInterfaceTable=_SwIGMPProxyUpstreamInterfaceTable_Object((1,3,6,1,4,1,171,12,80,3,1,1))
if mibBuilder.loadTexts:swIGMPProxyUpstreamInterfaceTable.setStatus(_A)
_SwIGMPProxyUpstreamInterfaceEntry_Object=MibTableRow
swIGMPProxyUpstreamInterfaceEntry=_SwIGMPProxyUpstreamInterfaceEntry_Object((1,3,6,1,4,1,171,12,80,3,1,1,1))
swIGMPProxyUpstreamInterfaceEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:swIGMPProxyUpstreamInterfaceEntry.setStatus(_A)
_SwIGMPProxyUpstreamIndex_Type=Integer32
_SwIGMPProxyUpstreamIndex_Object=MibTableColumn
swIGMPProxyUpstreamIndex=_SwIGMPProxyUpstreamIndex_Object((1,3,6,1,4,1,171,12,80,3,1,1,1,1),_SwIGMPProxyUpstreamIndex_Type())
swIGMPProxyUpstreamIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swIGMPProxyUpstreamIndex.setStatus(_A)
_SwIGMPProxyUpstreamVlanID_Type=VlanId
_SwIGMPProxyUpstreamVlanID_Object=MibTableColumn
swIGMPProxyUpstreamVlanID=_SwIGMPProxyUpstreamVlanID_Object((1,3,6,1,4,1,171,12,80,3,1,1,1,2),_SwIGMPProxyUpstreamVlanID_Type())
swIGMPProxyUpstreamVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPProxyUpstreamVlanID.setStatus(_A)
_SwIGMPProxyUpstreamDynamicRouterPorts_Type=PortList
_SwIGMPProxyUpstreamDynamicRouterPorts_Object=MibTableColumn
swIGMPProxyUpstreamDynamicRouterPorts=_SwIGMPProxyUpstreamDynamicRouterPorts_Object((1,3,6,1,4,1,171,12,80,3,1,1,1,3),_SwIGMPProxyUpstreamDynamicRouterPorts_Type())
swIGMPProxyUpstreamDynamicRouterPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:swIGMPProxyUpstreamDynamicRouterPorts.setStatus(_A)
_SwIGMPProxyUpstreamStaticRouterPorts_Type=PortList
_SwIGMPProxyUpstreamStaticRouterPorts_Object=MibTableColumn
swIGMPProxyUpstreamStaticRouterPorts=_SwIGMPProxyUpstreamStaticRouterPorts_Object((1,3,6,1,4,1,171,12,80,3,1,1,1,4),_SwIGMPProxyUpstreamStaticRouterPorts_Type())
swIGMPProxyUpstreamStaticRouterPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPProxyUpstreamStaticRouterPorts.setStatus(_A)
class _SwIGMPProxyUpstreamUnsolicitedReportInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_SwIGMPProxyUpstreamUnsolicitedReportInterval_Type.__name__=_E
_SwIGMPProxyUpstreamUnsolicitedReportInterval_Object=MibTableColumn
swIGMPProxyUpstreamUnsolicitedReportInterval=_SwIGMPProxyUpstreamUnsolicitedReportInterval_Object((1,3,6,1,4,1,171,12,80,3,1,1,1,5),_SwIGMPProxyUpstreamUnsolicitedReportInterval_Type())
swIGMPProxyUpstreamUnsolicitedReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPProxyUpstreamUnsolicitedReportInterval.setStatus(_A)
_SwIGMPProxyUpstreamSourceIP_Type=IpAddress
_SwIGMPProxyUpstreamSourceIP_Object=MibTableColumn
swIGMPProxyUpstreamSourceIP=_SwIGMPProxyUpstreamSourceIP_Object((1,3,6,1,4,1,171,12,80,3,1,1,1,6),_SwIGMPProxyUpstreamSourceIP_Type())
swIGMPProxyUpstreamSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPProxyUpstreamSourceIP.setStatus(_A)
_SwIGMPProxyDownstreamInterfaceTable_Object=MibTable
swIGMPProxyDownstreamInterfaceTable=_SwIGMPProxyDownstreamInterfaceTable_Object((1,3,6,1,4,1,171,12,80,3,1,2))
if mibBuilder.loadTexts:swIGMPProxyDownstreamInterfaceTable.setStatus(_A)
_SwIGMPProxyDownstreamInterfaceEntry_Object=MibTableRow
swIGMPProxyDownstreamInterfaceEntry=_SwIGMPProxyDownstreamInterfaceEntry_Object((1,3,6,1,4,1,171,12,80,3,1,2,1))
swIGMPProxyDownstreamInterfaceEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:swIGMPProxyDownstreamInterfaceEntry.setStatus(_A)
_SwIGMPProxyDownstreamRowStatus_Type=RowStatus
_SwIGMPProxyDownstreamRowStatus_Object=MibTableColumn
swIGMPProxyDownstreamRowStatus=_SwIGMPProxyDownstreamRowStatus_Object((1,3,6,1,4,1,171,12,80,3,1,2,1,1),_SwIGMPProxyDownstreamRowStatus_Type())
swIGMPProxyDownstreamRowStatus.setMaxAccess(_R)
if mibBuilder.loadTexts:swIGMPProxyDownstreamRowStatus.setStatus(_A)
_SwMLDProxyMgmt_ObjectIdentity=ObjectIdentity
swMLDProxyMgmt=_SwMLDProxyMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,80,3,2))
_SwMLDProxyUpstreamInterfaceTable_Object=MibTable
swMLDProxyUpstreamInterfaceTable=_SwMLDProxyUpstreamInterfaceTable_Object((1,3,6,1,4,1,171,12,80,3,2,1))
if mibBuilder.loadTexts:swMLDProxyUpstreamInterfaceTable.setStatus(_A)
_SwMLDProxyUpstreamInterfaceEntry_Object=MibTableRow
swMLDProxyUpstreamInterfaceEntry=_SwMLDProxyUpstreamInterfaceEntry_Object((1,3,6,1,4,1,171,12,80,3,2,1,1))
swMLDProxyUpstreamInterfaceEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:swMLDProxyUpstreamInterfaceEntry.setStatus(_A)
_SwMLDProxyUpstreamIndex_Type=Integer32
_SwMLDProxyUpstreamIndex_Object=MibTableColumn
swMLDProxyUpstreamIndex=_SwMLDProxyUpstreamIndex_Object((1,3,6,1,4,1,171,12,80,3,2,1,1,1),_SwMLDProxyUpstreamIndex_Type())
swMLDProxyUpstreamIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swMLDProxyUpstreamIndex.setStatus(_A)
_SwMLDProxyUpstreamVlanID_Type=VlanId
_SwMLDProxyUpstreamVlanID_Object=MibTableColumn
swMLDProxyUpstreamVlanID=_SwMLDProxyUpstreamVlanID_Object((1,3,6,1,4,1,171,12,80,3,2,1,1,2),_SwMLDProxyUpstreamVlanID_Type())
swMLDProxyUpstreamVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:swMLDProxyUpstreamVlanID.setStatus(_A)
_SwMLDProxyUpstreamDynamicRouterPorts_Type=PortList
_SwMLDProxyUpstreamDynamicRouterPorts_Object=MibTableColumn
swMLDProxyUpstreamDynamicRouterPorts=_SwMLDProxyUpstreamDynamicRouterPorts_Object((1,3,6,1,4,1,171,12,80,3,2,1,1,3),_SwMLDProxyUpstreamDynamicRouterPorts_Type())
swMLDProxyUpstreamDynamicRouterPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:swMLDProxyUpstreamDynamicRouterPorts.setStatus(_A)
_SwMLDProxyUpstreamStaticRouterPorts_Type=PortList
_SwMLDProxyUpstreamStaticRouterPorts_Object=MibTableColumn
swMLDProxyUpstreamStaticRouterPorts=_SwMLDProxyUpstreamStaticRouterPorts_Object((1,3,6,1,4,1,171,12,80,3,2,1,1,4),_SwMLDProxyUpstreamStaticRouterPorts_Type())
swMLDProxyUpstreamStaticRouterPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swMLDProxyUpstreamStaticRouterPorts.setStatus(_A)
class _SwMLDProxyUpstreamUnsolicitedReportInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_SwMLDProxyUpstreamUnsolicitedReportInterval_Type.__name__=_E
_SwMLDProxyUpstreamUnsolicitedReportInterval_Object=MibTableColumn
swMLDProxyUpstreamUnsolicitedReportInterval=_SwMLDProxyUpstreamUnsolicitedReportInterval_Object((1,3,6,1,4,1,171,12,80,3,2,1,1,5),_SwMLDProxyUpstreamUnsolicitedReportInterval_Type())
swMLDProxyUpstreamUnsolicitedReportInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swMLDProxyUpstreamUnsolicitedReportInterval.setStatus(_A)
_SwMLDProxyUpstreamSourceIP_Type=Ipv6Address
_SwMLDProxyUpstreamSourceIP_Object=MibTableColumn
swMLDProxyUpstreamSourceIP=_SwMLDProxyUpstreamSourceIP_Object((1,3,6,1,4,1,171,12,80,3,2,1,1,6),_SwMLDProxyUpstreamSourceIP_Type())
swMLDProxyUpstreamSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swMLDProxyUpstreamSourceIP.setStatus(_A)
_SwMLDProxyDownstreamInterfaceTable_Object=MibTable
swMLDProxyDownstreamInterfaceTable=_SwMLDProxyDownstreamInterfaceTable_Object((1,3,6,1,4,1,171,12,80,3,2,2))
if mibBuilder.loadTexts:swMLDProxyDownstreamInterfaceTable.setStatus(_A)
_SwMLDProxyDownstreamInterfaceEntry_Object=MibTableRow
swMLDProxyDownstreamInterfaceEntry=_SwMLDProxyDownstreamInterfaceEntry_Object((1,3,6,1,4,1,171,12,80,3,2,2,1))
swMLDProxyDownstreamInterfaceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:swMLDProxyDownstreamInterfaceEntry.setStatus(_A)
_SwMLDProxyDownstreamRowStatus_Type=RowStatus
_SwMLDProxyDownstreamRowStatus_Object=MibTableColumn
swMLDProxyDownstreamRowStatus=_SwMLDProxyDownstreamRowStatus_Object((1,3,6,1,4,1,171,12,80,3,2,2,1,1),_SwMLDProxyDownstreamRowStatus_Type())
swMLDProxyDownstreamRowStatus.setMaxAccess(_R)
if mibBuilder.loadTexts:swMLDProxyDownstreamRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'swMcastProxyMIB':swMcastProxyMIB,'swMcastProxyCtrl':swMcastProxyCtrl,'swIGMPProxyGlobalState':swIGMPProxyGlobalState,'swMLDProxyGlobalState':swMLDProxyGlobalState,'swMcastProxyInfo':swMcastProxyInfo,'swIGMPProxyInfo':swIGMPProxyInfo,'swIGMPProxyGroupTable':swIGMPProxyGroupTable,'swIGMPProxyGroupEntry':swIGMPProxyGroupEntry,_K:swIGMPProxyGroupDesAddr,_L:swIGMPProxyGroupSrcAddr,_G:swIGMPProxyDownstreamVlanID,'swIGMPProxyDownstreamVlanMemberPorts':swIGMPProxyDownstreamVlanMemberPorts,'swIGMPProxyGroupStatus':swIGMPProxyGroupStatus,'swMLDProxyInfo':swMLDProxyInfo,'swMLDProxyGroupTable':swMLDProxyGroupTable,'swMLDProxyGroupEntry':swMLDProxyGroupEntry,_O:swMLDProxyGroupDesAddr,_P:swMLDProxyGroupSrcAddr,_H:swMLDProxyDownstreamVlanID,'swMLDProxyDownstreamVlanMemberPorts':swMLDProxyDownstreamVlanMemberPorts,'swMLDProxyGroupStatus':swMLDProxyGroupStatus,'swMcastProxyMgmt':swMcastProxyMgmt,'swIGMPProxyMgmt':swIGMPProxyMgmt,'swIGMPProxyUpstreamInterfaceTable':swIGMPProxyUpstreamInterfaceTable,'swIGMPProxyUpstreamInterfaceEntry':swIGMPProxyUpstreamInterfaceEntry,_Q:swIGMPProxyUpstreamIndex,'swIGMPProxyUpstreamVlanID':swIGMPProxyUpstreamVlanID,'swIGMPProxyUpstreamDynamicRouterPorts':swIGMPProxyUpstreamDynamicRouterPorts,'swIGMPProxyUpstreamStaticRouterPorts':swIGMPProxyUpstreamStaticRouterPorts,'swIGMPProxyUpstreamUnsolicitedReportInterval':swIGMPProxyUpstreamUnsolicitedReportInterval,'swIGMPProxyUpstreamSourceIP':swIGMPProxyUpstreamSourceIP,'swIGMPProxyDownstreamInterfaceTable':swIGMPProxyDownstreamInterfaceTable,'swIGMPProxyDownstreamInterfaceEntry':swIGMPProxyDownstreamInterfaceEntry,'swIGMPProxyDownstreamRowStatus':swIGMPProxyDownstreamRowStatus,'swMLDProxyMgmt':swMLDProxyMgmt,'swMLDProxyUpstreamInterfaceTable':swMLDProxyUpstreamInterfaceTable,'swMLDProxyUpstreamInterfaceEntry':swMLDProxyUpstreamInterfaceEntry,_S:swMLDProxyUpstreamIndex,'swMLDProxyUpstreamVlanID':swMLDProxyUpstreamVlanID,'swMLDProxyUpstreamDynamicRouterPorts':swMLDProxyUpstreamDynamicRouterPorts,'swMLDProxyUpstreamStaticRouterPorts':swMLDProxyUpstreamStaticRouterPorts,'swMLDProxyUpstreamUnsolicitedReportInterval':swMLDProxyUpstreamUnsolicitedReportInterval,'swMLDProxyUpstreamSourceIP':swMLDProxyUpstreamSourceIP,'swMLDProxyDownstreamInterfaceTable':swMLDProxyDownstreamInterfaceTable,'swMLDProxyDownstreamInterfaceEntry':swMLDProxyDownstreamInterfaceEntry,'swMLDProxyDownstreamRowStatus':swMLDProxyDownstreamRowStatus})