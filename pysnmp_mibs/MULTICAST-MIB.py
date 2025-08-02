_v='agentIpStaticMRouteSrcNetMask'
_u='agentIpStaticMRouteSrcIpAddr'
_t='agentIpStaticMRouteSrcAddressType'
_s='agentMulticastStaticRouteSourceIP'
_r='agentMulticastAdminBoundaryGroupMask'
_q='agentMulticastAdminBoundaryGroupAddress'
_p='agentMulticastAdminBoundaryIndex'
_o='agentMulticastIPv6PIMDMInterfaceIndex'
_n='agentMulticastIPv6PIMSMCandRPGroupPrefixLength'
_m='agentMulticastIPv6PIMSMCandRPGroupAddress'
_l='agentMulticastIPv6PIMSMCandRPAddress'
_k='agentMulticastIPv6PIMSMInterfaceIndex'
_j='agentMulticastIPv6PIMSMSSMGroupMask'
_i='agentMulticastIPv6PIMSMSSMGroupAddress'
_h='agentMulticastIPv6PIMSMCBSRInterfaceIndex'
_g='agentMulticastIPv6PIMSMStaticRPGroupIpPrefix'
_f='agentMulticastIPv6PIMSMStaticRPGroupIpAddr'
_e='agentMulticastIPv6PIMSMStaticRPIpAddr'
_d='agentMulticastMLDProxyInterfaceIfIndex'
_c='agentMulticastMLDInterfaceIfIndex'
_b='agentMulticastDVMRPInterfaceIfIndex'
_a='agentMulticastPIMDMInterfaceIndex'
_Z='agentMulticastPIMSMCandRPGroupPrefixLength'
_Y='agentMulticastPIMSMCandRPGroupAddress'
_X='agentMulticastPIMSMCandRPAddress'
_W='agentMulticastPIMSMInterfaceIndex'
_V='agentMulticastPIMSMSSMGroupMask'
_U='agentMulticastPIMSMSSMGroupAddress'
_T='agentMulticastPIMSMCBSRInterfaceIndex'
_S='agentMulticastPIMSMStaticRPGroupIpMask'
_R='agentMulticastPIMSMStaticRPGroupIpAddr'
_Q='agentMulticastPIMSMStaticRPIpAddr'
_P='agentMulticastIGMPProxyInterfaceIfIndex'
_O='agentMulticastIGMPInterfaceIfIndex'
_N='destory'
_M='create'
_L='active'
_K='read-only'
_J='not-accessible'
_I='Unsigned32'
_H='disable'
_G='enable'
_F='current'
_E='read-create'
_D='MULTICAST-MIB'
_C='read-write'
_B='Integer32'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
quanta,switch=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','quanta','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
multicast=ModuleIdentity((1,3,6,1,4,1,7244,2,4))
if mibBuilder.loadTexts:multicast.setRevisions(('2011-08-31 00:00',))
_AgentMulticastIGMPConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastIGMPConfigGroup=_AgentMulticastIGMPConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,1))
class _AgentMulticastIGMPAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIGMPAdminMode_Type.__name__=_B
_AgentMulticastIGMPAdminMode_Object=MibScalar
agentMulticastIGMPAdminMode=_AgentMulticastIGMPAdminMode_Object((1,3,6,1,4,1,7244,2,4,1,1),_AgentMulticastIGMPAdminMode_Type())
agentMulticastIGMPAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIGMPAdminMode.setStatus(_F)
_AgentMulticastIGMPInterfaceTable_Object=MibTable
agentMulticastIGMPInterfaceTable=_AgentMulticastIGMPInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,1,2))
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceTable.setStatus(_A)
_AgentMulticastIGMPInterfaceEntry_Object=MibTableRow
agentMulticastIGMPInterfaceEntry=_AgentMulticastIGMPInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,1,2,1))
agentMulticastIGMPInterfaceEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceEntry.setStatus(_A)
class _AgentMulticastIGMPInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastIGMPInterfaceIfIndex_Type.__name__=_B
_AgentMulticastIGMPInterfaceIfIndex_Object=MibTableColumn
agentMulticastIGMPInterfaceIfIndex=_AgentMulticastIGMPInterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,4,1,2,1,1),_AgentMulticastIGMPInterfaceIfIndex_Type())
agentMulticastIGMPInterfaceIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceIfIndex.setStatus(_A)
class _AgentMulticastIGMPInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIGMPInterfaceAdminMode_Type.__name__=_B
_AgentMulticastIGMPInterfaceAdminMode_Object=MibTableColumn
agentMulticastIGMPInterfaceAdminMode=_AgentMulticastIGMPInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,1,2,1,2),_AgentMulticastIGMPInterfaceAdminMode_Type())
agentMulticastIGMPInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceAdminMode.setStatus(_A)
_AgentMulticastIGMPProxyInterfaceTable_Object=MibTable
agentMulticastIGMPProxyInterfaceTable=_AgentMulticastIGMPProxyInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,1,3))
if mibBuilder.loadTexts:agentMulticastIGMPProxyInterfaceTable.setStatus(_A)
_AgentMulticastIGMPProxyInterfaceEntry_Object=MibTableRow
agentMulticastIGMPProxyInterfaceEntry=_AgentMulticastIGMPProxyInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,1,3,1))
agentMulticastIGMPProxyInterfaceEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:agentMulticastIGMPProxyInterfaceEntry.setStatus(_A)
class _AgentMulticastIGMPProxyInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastIGMPProxyInterfaceIfIndex_Type.__name__=_B
_AgentMulticastIGMPProxyInterfaceIfIndex_Object=MibTableColumn
agentMulticastIGMPProxyInterfaceIfIndex=_AgentMulticastIGMPProxyInterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,4,1,3,1,1),_AgentMulticastIGMPProxyInterfaceIfIndex_Type())
agentMulticastIGMPProxyInterfaceIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastIGMPProxyInterfaceIfIndex.setStatus(_A)
class _AgentMulticastIGMPProxyInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIGMPProxyInterfaceAdminMode_Type.__name__=_B
_AgentMulticastIGMPProxyInterfaceAdminMode_Object=MibTableColumn
agentMulticastIGMPProxyInterfaceAdminMode=_AgentMulticastIGMPProxyInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,1,3,1,2),_AgentMulticastIGMPProxyInterfaceAdminMode_Type())
agentMulticastIGMPProxyInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIGMPProxyInterfaceAdminMode.setStatus(_A)
class _AgentMulticastIGMPProxyInterfaceInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,260))
_AgentMulticastIGMPProxyInterfaceInterval_Type.__name__=_B
_AgentMulticastIGMPProxyInterfaceInterval_Object=MibTableColumn
agentMulticastIGMPProxyInterfaceInterval=_AgentMulticastIGMPProxyInterfaceInterval_Object((1,3,6,1,4,1,7244,2,4,1,3,1,3),_AgentMulticastIGMPProxyInterfaceInterval_Type())
agentMulticastIGMPProxyInterfaceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIGMPProxyInterfaceInterval.setStatus(_A)
_AgentMulticastPIMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastPIMConfigGroup=_AgentMulticastPIMConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,2))
class _AgentMulticastPIMConfigMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('sparse',1),('dense',2)))
_AgentMulticastPIMConfigMode_Type.__name__=_B
_AgentMulticastPIMConfigMode_Object=MibScalar
agentMulticastPIMConfigMode=_AgentMulticastPIMConfigMode_Object((1,3,6,1,4,1,7244,2,4,2,1),_AgentMulticastPIMConfigMode_Type())
agentMulticastPIMConfigMode.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastPIMConfigMode.setStatus(_A)
_AgentMulticastPIMSMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastPIMSMConfigGroup=_AgentMulticastPIMSMConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,3))
class _AgentMulticastPIMSMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastPIMSMAdminMode_Type.__name__=_B
_AgentMulticastPIMSMAdminMode_Object=MibScalar
agentMulticastPIMSMAdminMode=_AgentMulticastPIMSMAdminMode_Object((1,3,6,1,4,1,7244,2,4,3,1),_AgentMulticastPIMSMAdminMode_Type())
agentMulticastPIMSMAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMAdminMode.setStatus(_F)
class _AgentMulticastPIMSMDataThresholdRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AgentMulticastPIMSMDataThresholdRate_Type.__name__=_B
_AgentMulticastPIMSMDataThresholdRate_Object=MibScalar
agentMulticastPIMSMDataThresholdRate=_AgentMulticastPIMSMDataThresholdRate_Object((1,3,6,1,4,1,7244,2,4,3,2),_AgentMulticastPIMSMDataThresholdRate_Type())
agentMulticastPIMSMDataThresholdRate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMDataThresholdRate.setStatus(_A)
_AgentMulticastPIMSMStaticRPTable_Object=MibTable
agentMulticastPIMSMStaticRPTable=_AgentMulticastPIMSMStaticRPTable_Object((1,3,6,1,4,1,7244,2,4,3,4))
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPTable.setStatus(_A)
_AgentMulticastPIMSMStaticRPEntry_Object=MibTableRow
agentMulticastPIMSMStaticRPEntry=_AgentMulticastPIMSMStaticRPEntry_Object((1,3,6,1,4,1,7244,2,4,3,4,1))
agentMulticastPIMSMStaticRPEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPEntry.setStatus(_A)
_AgentMulticastPIMSMStaticRPIpAddr_Type=IpAddress
_AgentMulticastPIMSMStaticRPIpAddr_Object=MibTableColumn
agentMulticastPIMSMStaticRPIpAddr=_AgentMulticastPIMSMStaticRPIpAddr_Object((1,3,6,1,4,1,7244,2,4,3,4,1,1),_AgentMulticastPIMSMStaticRPIpAddr_Type())
agentMulticastPIMSMStaticRPIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPIpAddr.setStatus(_A)
_AgentMulticastPIMSMStaticRPGroupIpAddr_Type=IpAddress
_AgentMulticastPIMSMStaticRPGroupIpAddr_Object=MibTableColumn
agentMulticastPIMSMStaticRPGroupIpAddr=_AgentMulticastPIMSMStaticRPGroupIpAddr_Object((1,3,6,1,4,1,7244,2,4,3,4,1,2),_AgentMulticastPIMSMStaticRPGroupIpAddr_Type())
agentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPGroupIpAddr.setStatus(_A)
_AgentMulticastPIMSMStaticRPGroupIpMask_Type=IpAddress
_AgentMulticastPIMSMStaticRPGroupIpMask_Object=MibTableColumn
agentMulticastPIMSMStaticRPGroupIpMask=_AgentMulticastPIMSMStaticRPGroupIpMask_Object((1,3,6,1,4,1,7244,2,4,3,4,1,3),_AgentMulticastPIMSMStaticRPGroupIpMask_Type())
agentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPGroupIpMask.setStatus(_A)
_AgentMulticastPIMSMStaticRPStatus_Type=RowStatus
_AgentMulticastPIMSMStaticRPStatus_Object=MibTableColumn
agentMulticastPIMSMStaticRPStatus=_AgentMulticastPIMSMStaticRPStatus_Object((1,3,6,1,4,1,7244,2,4,3,4,1,4),_AgentMulticastPIMSMStaticRPStatus_Type())
agentMulticastPIMSMStaticRPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPStatus.setStatus(_A)
_AgentMulticastPIMSMCBSRInterfaceTable_Object=MibTable
agentMulticastPIMSMCBSRInterfaceTable=_AgentMulticastPIMSMCBSRInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,3,5))
if mibBuilder.loadTexts:agentMulticastPIMSMCBSRInterfaceTable.setStatus(_A)
_AgentMulticastPIMSMCBSRInterfaceEntry_Object=MibTableRow
agentMulticastPIMSMCBSRInterfaceEntry=_AgentMulticastPIMSMCBSRInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,3,5,1))
agentMulticastPIMSMCBSRInterfaceEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:agentMulticastPIMSMCBSRInterfaceEntry.setStatus(_A)
_AgentMulticastPIMSMCBSRInterfaceIndex_Type=Unsigned32
_AgentMulticastPIMSMCBSRInterfaceIndex_Object=MibTableColumn
agentMulticastPIMSMCBSRInterfaceIndex=_AgentMulticastPIMSMCBSRInterfaceIndex_Object((1,3,6,1,4,1,7244,2,4,3,5,1,1),_AgentMulticastPIMSMCBSRInterfaceIndex_Type())
agentMulticastPIMSMCBSRInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastPIMSMCBSRInterfaceIndex.setStatus(_A)
class _AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Type.__name__=_I
_AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Object=MibTableColumn
agentMulticastPIMSMCBSRInterfaceHashMaskLength=_AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Object((1,3,6,1,4,1,7244,2,4,3,5,1,2),_AgentMulticastPIMSMCBSRInterfaceHashMaskLength_Type())
agentMulticastPIMSMCBSRInterfaceHashMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMCBSRInterfaceHashMaskLength.setStatus(_A)
class _AgentMulticastPIMSMCBSRInterfacePriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_AgentMulticastPIMSMCBSRInterfacePriority_Type.__name__=_B
_AgentMulticastPIMSMCBSRInterfacePriority_Object=MibTableColumn
agentMulticastPIMSMCBSRInterfacePriority=_AgentMulticastPIMSMCBSRInterfacePriority_Object((1,3,6,1,4,1,7244,2,4,3,5,1,3),_AgentMulticastPIMSMCBSRInterfacePriority_Type())
agentMulticastPIMSMCBSRInterfacePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMCBSRInterfacePriority.setStatus(_A)
_AgentMulticastPIMSMSSMTable_Object=MibTable
agentMulticastPIMSMSSMTable=_AgentMulticastPIMSMSSMTable_Object((1,3,6,1,4,1,7244,2,4,3,6))
if mibBuilder.loadTexts:agentMulticastPIMSMSSMTable.setStatus(_A)
_AgentMulticastPIMSMSSMEntry_Object=MibTableRow
agentMulticastPIMSMSSMEntry=_AgentMulticastPIMSMSSMEntry_Object((1,3,6,1,4,1,7244,2,4,3,6,1))
agentMulticastPIMSMSSMEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:agentMulticastPIMSMSSMEntry.setStatus(_A)
_AgentMulticastPIMSMSSMGroupAddress_Type=IpAddress
_AgentMulticastPIMSMSSMGroupAddress_Object=MibTableColumn
agentMulticastPIMSMSSMGroupAddress=_AgentMulticastPIMSMSSMGroupAddress_Object((1,3,6,1,4,1,7244,2,4,3,6,1,1),_AgentMulticastPIMSMSSMGroupAddress_Type())
agentMulticastPIMSMSSMGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMSSMGroupAddress.setStatus(_A)
class _AgentMulticastPIMSMSSMGroupMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentMulticastPIMSMSSMGroupMask_Type.__name__=_I
_AgentMulticastPIMSMSSMGroupMask_Object=MibTableColumn
agentMulticastPIMSMSSMGroupMask=_AgentMulticastPIMSMSSMGroupMask_Object((1,3,6,1,4,1,7244,2,4,3,6,1,2),_AgentMulticastPIMSMSSMGroupMask_Type())
agentMulticastPIMSMSSMGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMSSMGroupMask.setStatus(_A)
class _AgentMulticastPIMSMSSMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_L,1),(_M,4),(_N,6)))
_AgentMulticastPIMSMSSMStatus_Type.__name__=_B
_AgentMulticastPIMSMSSMStatus_Object=MibTableColumn
agentMulticastPIMSMSSMStatus=_AgentMulticastPIMSMSSMStatus_Object((1,3,6,1,4,1,7244,2,4,3,6,1,3),_AgentMulticastPIMSMSSMStatus_Type())
agentMulticastPIMSMSSMStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMSSMStatus.setStatus(_A)
_AgentMulticastPIMSMInterfaceTable_Object=MibTable
agentMulticastPIMSMInterfaceTable=_AgentMulticastPIMSMInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,3,7))
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceTable.setStatus(_A)
_AgentMulticastPIMSMInterfaceEntry_Object=MibTableRow
agentMulticastPIMSMInterfaceEntry=_AgentMulticastPIMSMInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,3,7,1))
agentMulticastPIMSMInterfaceEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceEntry.setStatus(_A)
_AgentMulticastPIMSMInterfaceIndex_Type=Unsigned32
_AgentMulticastPIMSMInterfaceIndex_Object=MibTableColumn
agentMulticastPIMSMInterfaceIndex=_AgentMulticastPIMSMInterfaceIndex_Object((1,3,6,1,4,1,7244,2,4,3,7,1,1),_AgentMulticastPIMSMInterfaceIndex_Type())
agentMulticastPIMSMInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceIndex.setStatus(_A)
class _AgentMulticastPIMSMInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastPIMSMInterfaceAdminMode_Type.__name__=_B
_AgentMulticastPIMSMInterfaceAdminMode_Object=MibTableColumn
agentMulticastPIMSMInterfaceAdminMode=_AgentMulticastPIMSMInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,3,7,1,2),_AgentMulticastPIMSMInterfaceAdminMode_Type())
agentMulticastPIMSMInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceAdminMode.setStatus(_F)
class _AgentMulticastPIMSMInterfaceHelloInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_AgentMulticastPIMSMInterfaceHelloInterval_Type.__name__=_I
_AgentMulticastPIMSMInterfaceHelloInterval_Object=MibTableColumn
agentMulticastPIMSMInterfaceHelloInterval=_AgentMulticastPIMSMInterfaceHelloInterval_Object((1,3,6,1,4,1,7244,2,4,3,7,1,3),_AgentMulticastPIMSMInterfaceHelloInterval_Type())
agentMulticastPIMSMInterfaceHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceHelloInterval.setStatus(_A)
class _AgentMulticastPIMSMInterfaceJoinPruneInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_AgentMulticastPIMSMInterfaceJoinPruneInterval_Type.__name__=_I
_AgentMulticastPIMSMInterfaceJoinPruneInterval_Object=MibTableColumn
agentMulticastPIMSMInterfaceJoinPruneInterval=_AgentMulticastPIMSMInterfaceJoinPruneInterval_Object((1,3,6,1,4,1,7244,2,4,3,7,1,4),_AgentMulticastPIMSMInterfaceJoinPruneInterval_Type())
agentMulticastPIMSMInterfaceJoinPruneInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceJoinPruneInterval.setStatus(_A)
class _AgentMulticastPIMSMInterfaceBsrBorder_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastPIMSMInterfaceBsrBorder_Type.__name__=_B
_AgentMulticastPIMSMInterfaceBsrBorder_Object=MibTableColumn
agentMulticastPIMSMInterfaceBsrBorder=_AgentMulticastPIMSMInterfaceBsrBorder_Object((1,3,6,1,4,1,7244,2,4,3,7,1,5),_AgentMulticastPIMSMInterfaceBsrBorder_Type())
agentMulticastPIMSMInterfaceBsrBorder.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceBsrBorder.setStatus(_F)
class _AgentMulticastPIMSMInterfaceDrPriority_Type(Unsigned32):defaultValue=1
_AgentMulticastPIMSMInterfaceDrPriority_Type.__name__=_I
_AgentMulticastPIMSMInterfaceDrPriority_Object=MibTableColumn
agentMulticastPIMSMInterfaceDrPriority=_AgentMulticastPIMSMInterfaceDrPriority_Object((1,3,6,1,4,1,7244,2,4,3,7,1,6),_AgentMulticastPIMSMInterfaceDrPriority_Type())
agentMulticastPIMSMInterfaceDrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceDrPriority.setStatus(_A)
class _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type.__name__=_I
_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object=MibTableColumn
agentMulticastPIMSMInterfaceCBSRHashMaskLength=_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object((1,3,6,1,4,1,7244,2,4,3,7,1,7),_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type())
agentMulticastPIMSMInterfaceCBSRHashMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus(_A)
class _AgentMulticastPIMSMInterfaceCRPPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_AgentMulticastPIMSMInterfaceCRPPreference_Type.__name__=_B
_AgentMulticastPIMSMInterfaceCRPPreference_Object=MibTableColumn
agentMulticastPIMSMInterfaceCRPPreference=_AgentMulticastPIMSMInterfaceCRPPreference_Object((1,3,6,1,4,1,7244,2,4,3,7,1,8),_AgentMulticastPIMSMInterfaceCRPPreference_Type())
agentMulticastPIMSMInterfaceCRPPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceCRPPreference.setStatus(_A)
_AgentMulticastPIMSMCandRPTable_Object=MibTable
agentMulticastPIMSMCandRPTable=_AgentMulticastPIMSMCandRPTable_Object((1,3,6,1,4,1,7244,2,4,3,8))
if mibBuilder.loadTexts:agentMulticastPIMSMCandRPTable.setStatus(_A)
_AgentMulticastPIMSMCandRPEntry_Object=MibTableRow
agentMulticastPIMSMCandRPEntry=_AgentMulticastPIMSMCandRPEntry_Object((1,3,6,1,4,1,7244,2,4,3,8,1))
agentMulticastPIMSMCandRPEntry.setIndexNames((0,_D,_X),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:agentMulticastPIMSMCandRPEntry.setStatus(_A)
_AgentMulticastPIMSMCandRPAddress_Type=IpAddress
_AgentMulticastPIMSMCandRPAddress_Object=MibTableColumn
agentMulticastPIMSMCandRPAddress=_AgentMulticastPIMSMCandRPAddress_Object((1,3,6,1,4,1,7244,2,4,3,8,1,1),_AgentMulticastPIMSMCandRPAddress_Type())
agentMulticastPIMSMCandRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMCandRPAddress.setStatus(_A)
_AgentMulticastPIMSMCandRPGroupAddress_Type=IpAddress
_AgentMulticastPIMSMCandRPGroupAddress_Object=MibTableColumn
agentMulticastPIMSMCandRPGroupAddress=_AgentMulticastPIMSMCandRPGroupAddress_Object((1,3,6,1,4,1,7244,2,4,3,8,1,2),_AgentMulticastPIMSMCandRPGroupAddress_Type())
agentMulticastPIMSMCandRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMCandRPGroupAddress.setStatus(_A)
class _AgentMulticastPIMSMCandRPGroupPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentMulticastPIMSMCandRPGroupPrefixLength_Type.__name__=_I
_AgentMulticastPIMSMCandRPGroupPrefixLength_Object=MibTableColumn
agentMulticastPIMSMCandRPGroupPrefixLength=_AgentMulticastPIMSMCandRPGroupPrefixLength_Object((1,3,6,1,4,1,7244,2,4,3,8,1,3),_AgentMulticastPIMSMCandRPGroupPrefixLength_Type())
agentMulticastPIMSMCandRPGroupPrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMCandRPGroupPrefixLength.setStatus(_A)
class _AgentMulticastPIMSMCandRPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_L,1),(_M,4),(_N,6)))
_AgentMulticastPIMSMCandRPStatus_Type.__name__=_B
_AgentMulticastPIMSMCandRPStatus_Object=MibTableColumn
agentMulticastPIMSMCandRPStatus=_AgentMulticastPIMSMCandRPStatus_Object((1,3,6,1,4,1,7244,2,4,3,8,1,4),_AgentMulticastPIMSMCandRPStatus_Type())
agentMulticastPIMSMCandRPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastPIMSMCandRPStatus.setStatus(_A)
_AgentMulticastPIMDMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastPIMDMConfigGroup=_AgentMulticastPIMDMConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,4))
class _AgentMulticastPIMDMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastPIMDMAdminMode_Type.__name__=_B
_AgentMulticastPIMDMAdminMode_Object=MibScalar
agentMulticastPIMDMAdminMode=_AgentMulticastPIMDMAdminMode_Object((1,3,6,1,4,1,7244,2,4,4,1),_AgentMulticastPIMDMAdminMode_Type())
agentMulticastPIMDMAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMDMAdminMode.setStatus(_F)
_AgentMulticastPIMDMInterfaceTable_Object=MibTable
agentMulticastPIMDMInterfaceTable=_AgentMulticastPIMDMInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,4,2))
if mibBuilder.loadTexts:agentMulticastPIMDMInterfaceTable.setStatus(_A)
_AgentMulticastPIMDMInterfaceEntry_Object=MibTableRow
agentMulticastPIMDMInterfaceEntry=_AgentMulticastPIMDMInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,4,2,1))
agentMulticastPIMDMInterfaceEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:agentMulticastPIMDMInterfaceEntry.setStatus(_A)
_AgentMulticastPIMDMInterfaceIndex_Type=Unsigned32
_AgentMulticastPIMDMInterfaceIndex_Object=MibTableColumn
agentMulticastPIMDMInterfaceIndex=_AgentMulticastPIMDMInterfaceIndex_Object((1,3,6,1,4,1,7244,2,4,4,2,1,1),_AgentMulticastPIMDMInterfaceIndex_Type())
agentMulticastPIMDMInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastPIMDMInterfaceIndex.setStatus(_A)
class _AgentMulticastPIMDMInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastPIMDMInterfaceMode_Type.__name__=_B
_AgentMulticastPIMDMInterfaceMode_Object=MibTableColumn
agentMulticastPIMDMInterfaceMode=_AgentMulticastPIMDMInterfaceMode_Object((1,3,6,1,4,1,7244,2,4,4,2,1,2),_AgentMulticastPIMDMInterfaceMode_Type())
agentMulticastPIMDMInterfaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMDMInterfaceMode.setStatus(_A)
class _AgentMulticastPIMDMInterfaceHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_AgentMulticastPIMDMInterfaceHelloInterval_Type.__name__=_B
_AgentMulticastPIMDMInterfaceHelloInterval_Object=MibTableColumn
agentMulticastPIMDMInterfaceHelloInterval=_AgentMulticastPIMDMInterfaceHelloInterval_Object((1,3,6,1,4,1,7244,2,4,4,2,1,3),_AgentMulticastPIMDMInterfaceHelloInterval_Type())
agentMulticastPIMDMInterfaceHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastPIMDMInterfaceHelloInterval.setStatus(_A)
_AgentMulticastRoutingConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastRoutingConfigGroup=_AgentMulticastRoutingConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,5))
class _AgentMulticastRoutingAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastRoutingAdminMode_Type.__name__=_B
_AgentMulticastRoutingAdminMode_Object=MibScalar
agentMulticastRoutingAdminMode=_AgentMulticastRoutingAdminMode_Object((1,3,6,1,4,1,7244,2,4,5,1),_AgentMulticastRoutingAdminMode_Type())
agentMulticastRoutingAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastRoutingAdminMode.setStatus(_A)
_AgentMulticastDVMRPConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastDVMRPConfigGroup=_AgentMulticastDVMRPConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,6))
class _AgentMulticastDVMRPAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastDVMRPAdminMode_Type.__name__=_B
_AgentMulticastDVMRPAdminMode_Object=MibScalar
agentMulticastDVMRPAdminMode=_AgentMulticastDVMRPAdminMode_Object((1,3,6,1,4,1,7244,2,4,6,1),_AgentMulticastDVMRPAdminMode_Type())
agentMulticastDVMRPAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastDVMRPAdminMode.setStatus(_F)
_AgentMulticastDVMRPInterfaceTable_Object=MibTable
agentMulticastDVMRPInterfaceTable=_AgentMulticastDVMRPInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,6,2))
if mibBuilder.loadTexts:agentMulticastDVMRPInterfaceTable.setStatus(_A)
_AgentMulticastDVMRPInterfaceEntry_Object=MibTableRow
agentMulticastDVMRPInterfaceEntry=_AgentMulticastDVMRPInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,6,2,1))
agentMulticastDVMRPInterfaceEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:agentMulticastDVMRPInterfaceEntry.setStatus(_A)
class _AgentMulticastDVMRPInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastDVMRPInterfaceIfIndex_Type.__name__=_B
_AgentMulticastDVMRPInterfaceIfIndex_Object=MibTableColumn
agentMulticastDVMRPInterfaceIfIndex=_AgentMulticastDVMRPInterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,4,6,2,1,1),_AgentMulticastDVMRPInterfaceIfIndex_Type())
agentMulticastDVMRPInterfaceIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastDVMRPInterfaceIfIndex.setStatus(_A)
class _AgentMulticastDVMRPInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastDVMRPInterfaceAdminMode_Type.__name__=_B
_AgentMulticastDVMRPInterfaceAdminMode_Object=MibTableColumn
agentMulticastDVMRPInterfaceAdminMode=_AgentMulticastDVMRPInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,6,2,1,2),_AgentMulticastDVMRPInterfaceAdminMode_Type())
agentMulticastDVMRPInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastDVMRPInterfaceAdminMode.setStatus(_A)
class _AgentMulticastDVMRPInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AgentMulticastDVMRPInterfaceMetric_Type.__name__=_B
_AgentMulticastDVMRPInterfaceMetric_Object=MibTableColumn
agentMulticastDVMRPInterfaceMetric=_AgentMulticastDVMRPInterfaceMetric_Object((1,3,6,1,4,1,7244,2,4,6,2,1,3),_AgentMulticastDVMRPInterfaceMetric_Type())
agentMulticastDVMRPInterfaceMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastDVMRPInterfaceMetric.setStatus(_A)
_AgentMulticastDVMRPInterfaceGenerationId_Type=Integer32
_AgentMulticastDVMRPInterfaceGenerationId_Object=MibTableColumn
agentMulticastDVMRPInterfaceGenerationId=_AgentMulticastDVMRPInterfaceGenerationId_Object((1,3,6,1,4,1,7244,2,4,6,2,1,4),_AgentMulticastDVMRPInterfaceGenerationId_Type())
agentMulticastDVMRPInterfaceGenerationId.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastDVMRPInterfaceGenerationId.setStatus(_A)
_AgentMulticastMLDConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastMLDConfigGroup=_AgentMulticastMLDConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,8))
class _AgentMulticastMLDAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastMLDAdminMode_Type.__name__=_B
_AgentMulticastMLDAdminMode_Object=MibScalar
agentMulticastMLDAdminMode=_AgentMulticastMLDAdminMode_Object((1,3,6,1,4,1,7244,2,4,8,1),_AgentMulticastMLDAdminMode_Type())
agentMulticastMLDAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastMLDAdminMode.setStatus(_F)
_AgentMulticastMLDInterfaceTable_Object=MibTable
agentMulticastMLDInterfaceTable=_AgentMulticastMLDInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,8,2))
if mibBuilder.loadTexts:agentMulticastMLDInterfaceTable.setStatus(_A)
_AgentMulticastMLDInterfaceEntry_Object=MibTableRow
agentMulticastMLDInterfaceEntry=_AgentMulticastMLDInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,8,2,1))
agentMulticastMLDInterfaceEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:agentMulticastMLDInterfaceEntry.setStatus(_A)
class _AgentMulticastMLDInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastMLDInterfaceIfIndex_Type.__name__=_B
_AgentMulticastMLDInterfaceIfIndex_Object=MibTableColumn
agentMulticastMLDInterfaceIfIndex=_AgentMulticastMLDInterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,4,8,2,1,1),_AgentMulticastMLDInterfaceIfIndex_Type())
agentMulticastMLDInterfaceIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastMLDInterfaceIfIndex.setStatus(_A)
class _AgentMulticastMLDInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastMLDInterfaceAdminMode_Type.__name__=_B
_AgentMulticastMLDInterfaceAdminMode_Object=MibTableColumn
agentMulticastMLDInterfaceAdminMode=_AgentMulticastMLDInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,8,2,1,2),_AgentMulticastMLDInterfaceAdminMode_Type())
agentMulticastMLDInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastMLDInterfaceAdminMode.setStatus(_A)
_AgentMulticastMLDProxyInterfaceTable_Object=MibTable
agentMulticastMLDProxyInterfaceTable=_AgentMulticastMLDProxyInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,8,3))
if mibBuilder.loadTexts:agentMulticastMLDProxyInterfaceTable.setStatus(_A)
_AgentMulticastMLDProxyInterfaceEntry_Object=MibTableRow
agentMulticastMLDProxyInterfaceEntry=_AgentMulticastMLDProxyInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,8,3,1))
agentMulticastMLDProxyInterfaceEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:agentMulticastMLDProxyInterfaceEntry.setStatus(_A)
class _AgentMulticastMLDProxyInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastMLDProxyInterfaceIfIndex_Type.__name__=_B
_AgentMulticastMLDProxyInterfaceIfIndex_Object=MibTableColumn
agentMulticastMLDProxyInterfaceIfIndex=_AgentMulticastMLDProxyInterfaceIfIndex_Object((1,3,6,1,4,1,7244,2,4,8,3,1,1),_AgentMulticastMLDProxyInterfaceIfIndex_Type())
agentMulticastMLDProxyInterfaceIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentMulticastMLDProxyInterfaceIfIndex.setStatus(_A)
class _AgentMulticastMLDProxyInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastMLDProxyInterfaceAdminMode_Type.__name__=_B
_AgentMulticastMLDProxyInterfaceAdminMode_Object=MibTableColumn
agentMulticastMLDProxyInterfaceAdminMode=_AgentMulticastMLDProxyInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,8,3,1,2),_AgentMulticastMLDProxyInterfaceAdminMode_Type())
agentMulticastMLDProxyInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastMLDProxyInterfaceAdminMode.setStatus(_A)
class _AgentMulticastMLDProxyInterfaceInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,260))
_AgentMulticastMLDProxyInterfaceInterval_Type.__name__=_B
_AgentMulticastMLDProxyInterfaceInterval_Object=MibTableColumn
agentMulticastMLDProxyInterfaceInterval=_AgentMulticastMLDProxyInterfaceInterval_Object((1,3,6,1,4,1,7244,2,4,8,3,1,3),_AgentMulticastMLDProxyInterfaceInterval_Type())
agentMulticastMLDProxyInterfaceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastMLDProxyInterfaceInterval.setStatus(_A)
_AgentMulticastIPv6PIMSMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastIPv6PIMSMConfigGroup=_AgentMulticastIPv6PIMSMConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,9))
class _AgentMulticastIPv6PIMSMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIPv6PIMSMAdminMode_Type.__name__=_B
_AgentMulticastIPv6PIMSMAdminMode_Object=MibScalar
agentMulticastIPv6PIMSMAdminMode=_AgentMulticastIPv6PIMSMAdminMode_Object((1,3,6,1,4,1,7244,2,4,9,1),_AgentMulticastIPv6PIMSMAdminMode_Type())
agentMulticastIPv6PIMSMAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMAdminMode.setStatus(_F)
class _AgentMulticastIPv6PIMSMDataThresholdRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AgentMulticastIPv6PIMSMDataThresholdRate_Type.__name__=_B
_AgentMulticastIPv6PIMSMDataThresholdRate_Object=MibScalar
agentMulticastIPv6PIMSMDataThresholdRate=_AgentMulticastIPv6PIMSMDataThresholdRate_Object((1,3,6,1,4,1,7244,2,4,9,2),_AgentMulticastIPv6PIMSMDataThresholdRate_Type())
agentMulticastIPv6PIMSMDataThresholdRate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMDataThresholdRate.setStatus(_A)
_AgentMulticastIPv6PIMSMStaticRPTable_Object=MibTable
agentMulticastIPv6PIMSMStaticRPTable=_AgentMulticastIPv6PIMSMStaticRPTable_Object((1,3,6,1,4,1,7244,2,4,9,4))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMStaticRPTable.setStatus(_A)
_AgentMulticastIPv6PIMSMStaticRPEntry_Object=MibTableRow
agentMulticastIPv6PIMSMStaticRPEntry=_AgentMulticastIPv6PIMSMStaticRPEntry_Object((1,3,6,1,4,1,7244,2,4,9,4,1))
agentMulticastIPv6PIMSMStaticRPEntry.setIndexNames((0,_D,_e),(0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMStaticRPEntry.setStatus(_A)
_AgentMulticastIPv6PIMSMStaticRPIpAddr_Type=Ipv6Address
_AgentMulticastIPv6PIMSMStaticRPIpAddr_Object=MibTableColumn
agentMulticastIPv6PIMSMStaticRPIpAddr=_AgentMulticastIPv6PIMSMStaticRPIpAddr_Object((1,3,6,1,4,1,7244,2,4,9,4,1,1),_AgentMulticastIPv6PIMSMStaticRPIpAddr_Type())
agentMulticastIPv6PIMSMStaticRPIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMStaticRPIpAddr.setStatus(_A)
_AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Type=Ipv6Address
_AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Object=MibTableColumn
agentMulticastIPv6PIMSMStaticRPGroupIpAddr=_AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Object((1,3,6,1,4,1,7244,2,4,9,4,1,2),_AgentMulticastIPv6PIMSMStaticRPGroupIpAddr_Type())
agentMulticastIPv6PIMSMStaticRPGroupIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMStaticRPGroupIpAddr.setStatus(_A)
class _AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Type.__name__=_B
_AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Object=MibTableColumn
agentMulticastIPv6PIMSMStaticRPGroupIpPrefix=_AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Object((1,3,6,1,4,1,7244,2,4,9,4,1,3),_AgentMulticastIPv6PIMSMStaticRPGroupIpPrefix_Type())
agentMulticastIPv6PIMSMStaticRPGroupIpPrefix.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMStaticRPGroupIpPrefix.setStatus(_A)
_AgentMulticastIPv6PIMSMStaticRPStatus_Type=RowStatus
_AgentMulticastIPv6PIMSMStaticRPStatus_Object=MibTableColumn
agentMulticastIPv6PIMSMStaticRPStatus=_AgentMulticastIPv6PIMSMStaticRPStatus_Object((1,3,6,1,4,1,7244,2,4,9,4,1,4),_AgentMulticastIPv6PIMSMStaticRPStatus_Type())
agentMulticastIPv6PIMSMStaticRPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMStaticRPStatus.setStatus(_A)
_AgentMulticastIPv6PIMSMCBSRInterfaceTable_Object=MibTable
agentMulticastIPv6PIMSMCBSRInterfaceTable=_AgentMulticastIPv6PIMSMCBSRInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,9,5))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCBSRInterfaceTable.setStatus(_A)
_AgentMulticastIPv6PIMSMCBSRInterfaceEntry_Object=MibTableRow
agentMulticastIPv6PIMSMCBSRInterfaceEntry=_AgentMulticastIPv6PIMSMCBSRInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,9,5,1))
agentMulticastIPv6PIMSMCBSRInterfaceEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCBSRInterfaceEntry.setStatus(_A)
_AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Type=Unsigned32
_AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Object=MibTableColumn
agentMulticastIPv6PIMSMCBSRInterfaceIndex=_AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Object((1,3,6,1,4,1,7244,2,4,9,5,1,1),_AgentMulticastIPv6PIMSMCBSRInterfaceIndex_Type())
agentMulticastIPv6PIMSMCBSRInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCBSRInterfaceIndex.setStatus(_A)
class _AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Type.__name__=_I
_AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Object=MibTableColumn
agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength=_AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Object((1,3,6,1,4,1,7244,2,4,9,5,1,2),_AgentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength_Type())
agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength.setStatus(_A)
class _AgentMulticastIPv6PIMSMCBSRInterfacePriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_AgentMulticastIPv6PIMSMCBSRInterfacePriority_Type.__name__=_B
_AgentMulticastIPv6PIMSMCBSRInterfacePriority_Object=MibTableColumn
agentMulticastIPv6PIMSMCBSRInterfacePriority=_AgentMulticastIPv6PIMSMCBSRInterfacePriority_Object((1,3,6,1,4,1,7244,2,4,9,5,1,3),_AgentMulticastIPv6PIMSMCBSRInterfacePriority_Type())
agentMulticastIPv6PIMSMCBSRInterfacePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCBSRInterfacePriority.setStatus(_A)
_AgentMulticastIPv6PIMSMSSMTable_Object=MibTable
agentMulticastIPv6PIMSMSSMTable=_AgentMulticastIPv6PIMSMSSMTable_Object((1,3,6,1,4,1,7244,2,4,9,6))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMSSMTable.setStatus(_A)
_AgentMulticastIPv6PIMSMSSMEntry_Object=MibTableRow
agentMulticastIPv6PIMSMSSMEntry=_AgentMulticastIPv6PIMSMSSMEntry_Object((1,3,6,1,4,1,7244,2,4,9,6,1))
agentMulticastIPv6PIMSMSSMEntry.setIndexNames((0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMSSMEntry.setStatus(_A)
_AgentMulticastIPv6PIMSMSSMGroupAddress_Type=Ipv6Address
_AgentMulticastIPv6PIMSMSSMGroupAddress_Object=MibTableColumn
agentMulticastIPv6PIMSMSSMGroupAddress=_AgentMulticastIPv6PIMSMSSMGroupAddress_Object((1,3,6,1,4,1,7244,2,4,9,6,1,1),_AgentMulticastIPv6PIMSMSSMGroupAddress_Type())
agentMulticastIPv6PIMSMSSMGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMSSMGroupAddress.setStatus(_A)
class _AgentMulticastIPv6PIMSMSSMGroupMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentMulticastIPv6PIMSMSSMGroupMask_Type.__name__=_I
_AgentMulticastIPv6PIMSMSSMGroupMask_Object=MibTableColumn
agentMulticastIPv6PIMSMSSMGroupMask=_AgentMulticastIPv6PIMSMSSMGroupMask_Object((1,3,6,1,4,1,7244,2,4,9,6,1,2),_AgentMulticastIPv6PIMSMSSMGroupMask_Type())
agentMulticastIPv6PIMSMSSMGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMSSMGroupMask.setStatus(_A)
class _AgentMulticastIPv6PIMSMSSMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_L,1),(_M,4),(_N,6)))
_AgentMulticastIPv6PIMSMSSMStatus_Type.__name__=_B
_AgentMulticastIPv6PIMSMSSMStatus_Object=MibTableColumn
agentMulticastIPv6PIMSMSSMStatus=_AgentMulticastIPv6PIMSMSSMStatus_Object((1,3,6,1,4,1,7244,2,4,9,6,1,3),_AgentMulticastIPv6PIMSMSSMStatus_Type())
agentMulticastIPv6PIMSMSSMStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMSSMStatus.setStatus(_A)
_AgentMulticastIPv6PIMSMInterfaceTable_Object=MibTable
agentMulticastIPv6PIMSMInterfaceTable=_AgentMulticastIPv6PIMSMInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,9,7))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceTable.setStatus(_A)
_AgentMulticastIPv6PIMSMInterfaceEntry_Object=MibTableRow
agentMulticastIPv6PIMSMInterfaceEntry=_AgentMulticastIPv6PIMSMInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,9,7,1))
agentMulticastIPv6PIMSMInterfaceEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceEntry.setStatus(_A)
_AgentMulticastIPv6PIMSMInterfaceIndex_Type=Unsigned32
_AgentMulticastIPv6PIMSMInterfaceIndex_Object=MibTableColumn
agentMulticastIPv6PIMSMInterfaceIndex=_AgentMulticastIPv6PIMSMInterfaceIndex_Object((1,3,6,1,4,1,7244,2,4,9,7,1,1),_AgentMulticastIPv6PIMSMInterfaceIndex_Type())
agentMulticastIPv6PIMSMInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceIndex.setStatus(_A)
class _AgentMulticastIPv6PIMSMInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIPv6PIMSMInterfaceAdminMode_Type.__name__=_B
_AgentMulticastIPv6PIMSMInterfaceAdminMode_Object=MibTableColumn
agentMulticastIPv6PIMSMInterfaceAdminMode=_AgentMulticastIPv6PIMSMInterfaceAdminMode_Object((1,3,6,1,4,1,7244,2,4,9,7,1,2),_AgentMulticastIPv6PIMSMInterfaceAdminMode_Type())
agentMulticastIPv6PIMSMInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceAdminMode.setStatus(_F)
class _AgentMulticastIPv6PIMSMInterfaceHelloInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_AgentMulticastIPv6PIMSMInterfaceHelloInterval_Type.__name__=_I
_AgentMulticastIPv6PIMSMInterfaceHelloInterval_Object=MibTableColumn
agentMulticastIPv6PIMSMInterfaceHelloInterval=_AgentMulticastIPv6PIMSMInterfaceHelloInterval_Object((1,3,6,1,4,1,7244,2,4,9,7,1,3),_AgentMulticastIPv6PIMSMInterfaceHelloInterval_Type())
agentMulticastIPv6PIMSMInterfaceHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceHelloInterval.setStatus(_A)
class _AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Type.__name__=_I
_AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Object=MibTableColumn
agentMulticastIPv6PIMSMInterfaceJoinPruneInterval=_AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Object((1,3,6,1,4,1,7244,2,4,9,7,1,4),_AgentMulticastIPv6PIMSMInterfaceJoinPruneInterval_Type())
agentMulticastIPv6PIMSMInterfaceJoinPruneInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceJoinPruneInterval.setStatus(_A)
class _AgentMulticastIPv6PIMSMInterfaceBsrBorder_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIPv6PIMSMInterfaceBsrBorder_Type.__name__=_B
_AgentMulticastIPv6PIMSMInterfaceBsrBorder_Object=MibTableColumn
agentMulticastIPv6PIMSMInterfaceBsrBorder=_AgentMulticastIPv6PIMSMInterfaceBsrBorder_Object((1,3,6,1,4,1,7244,2,4,9,7,1,5),_AgentMulticastIPv6PIMSMInterfaceBsrBorder_Type())
agentMulticastIPv6PIMSMInterfaceBsrBorder.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceBsrBorder.setStatus(_F)
class _AgentMulticastIPv6PIMSMInterfaceDrPriority_Type(Unsigned32):defaultValue=1
_AgentMulticastIPv6PIMSMInterfaceDrPriority_Type.__name__=_I
_AgentMulticastIPv6PIMSMInterfaceDrPriority_Object=MibTableColumn
agentMulticastIPv6PIMSMInterfaceDrPriority=_AgentMulticastIPv6PIMSMInterfaceDrPriority_Object((1,3,6,1,4,1,7244,2,4,9,7,1,6),_AgentMulticastIPv6PIMSMInterfaceDrPriority_Type())
agentMulticastIPv6PIMSMInterfaceDrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMInterfaceDrPriority.setStatus(_A)
_AgentMulticastIPv6PIMSMCandRPTable_Object=MibTable
agentMulticastIPv6PIMSMCandRPTable=_AgentMulticastIPv6PIMSMCandRPTable_Object((1,3,6,1,4,1,7244,2,4,9,8))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCandRPTable.setStatus(_A)
_AgentMulticastIPv6PIMSMCandRPEntry_Object=MibTableRow
agentMulticastIPv6PIMSMCandRPEntry=_AgentMulticastIPv6PIMSMCandRPEntry_Object((1,3,6,1,4,1,7244,2,4,9,8,1))
agentMulticastIPv6PIMSMCandRPEntry.setIndexNames((0,_D,_l),(0,_D,_m),(0,_D,_n))
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCandRPEntry.setStatus(_A)
_AgentMulticastIPv6PIMSMCandRPAddress_Type=Ipv6Address
_AgentMulticastIPv6PIMSMCandRPAddress_Object=MibTableColumn
agentMulticastIPv6PIMSMCandRPAddress=_AgentMulticastIPv6PIMSMCandRPAddress_Object((1,3,6,1,4,1,7244,2,4,9,8,1,1),_AgentMulticastIPv6PIMSMCandRPAddress_Type())
agentMulticastIPv6PIMSMCandRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCandRPAddress.setStatus(_A)
_AgentMulticastIPv6PIMSMCandRPGroupAddress_Type=Ipv6Address
_AgentMulticastIPv6PIMSMCandRPGroupAddress_Object=MibTableColumn
agentMulticastIPv6PIMSMCandRPGroupAddress=_AgentMulticastIPv6PIMSMCandRPGroupAddress_Object((1,3,6,1,4,1,7244,2,4,9,8,1,2),_AgentMulticastIPv6PIMSMCandRPGroupAddress_Type())
agentMulticastIPv6PIMSMCandRPGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCandRPGroupAddress.setStatus(_A)
class _AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Type.__name__=_I
_AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Object=MibTableColumn
agentMulticastIPv6PIMSMCandRPGroupPrefixLength=_AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Object((1,3,6,1,4,1,7244,2,4,9,8,1,3),_AgentMulticastIPv6PIMSMCandRPGroupPrefixLength_Type())
agentMulticastIPv6PIMSMCandRPGroupPrefixLength.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCandRPGroupPrefixLength.setStatus(_A)
class _AgentMulticastIPv6PIMSMCandRPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_L,1),(_M,4),(_N,6)))
_AgentMulticastIPv6PIMSMCandRPStatus_Type.__name__=_B
_AgentMulticastIPv6PIMSMCandRPStatus_Object=MibTableColumn
agentMulticastIPv6PIMSMCandRPStatus=_AgentMulticastIPv6PIMSMCandRPStatus_Object((1,3,6,1,4,1,7244,2,4,9,8,1,4),_AgentMulticastIPv6PIMSMCandRPStatus_Type())
agentMulticastIPv6PIMSMCandRPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastIPv6PIMSMCandRPStatus.setStatus(_A)
_AgentMulticastIPv6PIMDMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastIPv6PIMDMConfigGroup=_AgentMulticastIPv6PIMDMConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,10))
class _AgentMulticastIPv6PIMDMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIPv6PIMDMAdminMode_Type.__name__=_B
_AgentMulticastIPv6PIMDMAdminMode_Object=MibScalar
agentMulticastIPv6PIMDMAdminMode=_AgentMulticastIPv6PIMDMAdminMode_Object((1,3,6,1,4,1,7244,2,4,10,1),_AgentMulticastIPv6PIMDMAdminMode_Type())
agentMulticastIPv6PIMDMAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMDMAdminMode.setStatus(_F)
_AgentMulticastIPv6PIMDMInterfaceTable_Object=MibTable
agentMulticastIPv6PIMDMInterfaceTable=_AgentMulticastIPv6PIMDMInterfaceTable_Object((1,3,6,1,4,1,7244,2,4,10,2))
if mibBuilder.loadTexts:agentMulticastIPv6PIMDMInterfaceTable.setStatus(_A)
_AgentMulticastIPv6PIMDMInterfaceEntry_Object=MibTableRow
agentMulticastIPv6PIMDMInterfaceEntry=_AgentMulticastIPv6PIMDMInterfaceEntry_Object((1,3,6,1,4,1,7244,2,4,10,2,1))
agentMulticastIPv6PIMDMInterfaceEntry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:agentMulticastIPv6PIMDMInterfaceEntry.setStatus(_A)
_AgentMulticastIPv6PIMDMInterfaceIndex_Type=Unsigned32
_AgentMulticastIPv6PIMDMInterfaceIndex_Object=MibTableColumn
agentMulticastIPv6PIMDMInterfaceIndex=_AgentMulticastIPv6PIMDMInterfaceIndex_Object((1,3,6,1,4,1,7244,2,4,10,2,1,1),_AgentMulticastIPv6PIMDMInterfaceIndex_Type())
agentMulticastIPv6PIMDMInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:agentMulticastIPv6PIMDMInterfaceIndex.setStatus(_A)
class _AgentMulticastIPv6PIMDMInterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentMulticastIPv6PIMDMInterfaceMode_Type.__name__=_B
_AgentMulticastIPv6PIMDMInterfaceMode_Object=MibTableColumn
agentMulticastIPv6PIMDMInterfaceMode=_AgentMulticastIPv6PIMDMInterfaceMode_Object((1,3,6,1,4,1,7244,2,4,10,2,1,2),_AgentMulticastIPv6PIMDMInterfaceMode_Type())
agentMulticastIPv6PIMDMInterfaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMDMInterfaceMode.setStatus(_A)
class _AgentMulticastIPv6PIMDMInterfaceHelloInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18000))
_AgentMulticastIPv6PIMDMInterfaceHelloInterval_Type.__name__=_B
_AgentMulticastIPv6PIMDMInterfaceHelloInterval_Object=MibTableColumn
agentMulticastIPv6PIMDMInterfaceHelloInterval=_AgentMulticastIPv6PIMDMInterfaceHelloInterval_Object((1,3,6,1,4,1,7244,2,4,10,2,1,3),_AgentMulticastIPv6PIMDMInterfaceHelloInterval_Type())
agentMulticastIPv6PIMDMInterfaceHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentMulticastIPv6PIMDMInterfaceHelloInterval.setStatus(_A)
_AgentMulticastAdminBoundaryConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastAdminBoundaryConfigGroup=_AgentMulticastAdminBoundaryConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,11))
_AgentMulticastAdminBoundaryTable_Object=MibTable
agentMulticastAdminBoundaryTable=_AgentMulticastAdminBoundaryTable_Object((1,3,6,1,4,1,7244,2,4,11,1))
if mibBuilder.loadTexts:agentMulticastAdminBoundaryTable.setStatus(_A)
_AgentMulticastAdminBoundaryEntry_Object=MibTableRow
agentMulticastAdminBoundaryEntry=_AgentMulticastAdminBoundaryEntry_Object((1,3,6,1,4,1,7244,2,4,11,1,1))
agentMulticastAdminBoundaryEntry.setIndexNames((0,_D,_p),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:agentMulticastAdminBoundaryEntry.setStatus(_A)
_AgentMulticastAdminBoundaryIndex_Type=Unsigned32
_AgentMulticastAdminBoundaryIndex_Object=MibTableColumn
agentMulticastAdminBoundaryIndex=_AgentMulticastAdminBoundaryIndex_Object((1,3,6,1,4,1,7244,2,4,11,1,1,1),_AgentMulticastAdminBoundaryIndex_Type())
agentMulticastAdminBoundaryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastAdminBoundaryIndex.setStatus(_A)
_AgentMulticastAdminBoundaryGroupAddress_Type=IpAddress
_AgentMulticastAdminBoundaryGroupAddress_Object=MibTableColumn
agentMulticastAdminBoundaryGroupAddress=_AgentMulticastAdminBoundaryGroupAddress_Object((1,3,6,1,4,1,7244,2,4,11,1,1,2),_AgentMulticastAdminBoundaryGroupAddress_Type())
agentMulticastAdminBoundaryGroupAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastAdminBoundaryGroupAddress.setStatus(_A)
_AgentMulticastAdminBoundaryGroupMask_Type=IpAddress
_AgentMulticastAdminBoundaryGroupMask_Object=MibTableColumn
agentMulticastAdminBoundaryGroupMask=_AgentMulticastAdminBoundaryGroupMask_Object((1,3,6,1,4,1,7244,2,4,11,1,1,3),_AgentMulticastAdminBoundaryGroupMask_Type())
agentMulticastAdminBoundaryGroupMask.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastAdminBoundaryGroupMask.setStatus(_A)
class _AgentMulticastAdminBoundaryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_L,1),(_M,4),(_N,6)))
_AgentMulticastAdminBoundaryStatus_Type.__name__=_B
_AgentMulticastAdminBoundaryStatus_Object=MibTableColumn
agentMulticastAdminBoundaryStatus=_AgentMulticastAdminBoundaryStatus_Object((1,3,6,1,4,1,7244,2,4,11,1,1,4),_AgentMulticastAdminBoundaryStatus_Type())
agentMulticastAdminBoundaryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastAdminBoundaryStatus.setStatus(_A)
_AgentMulticastStaticRouteConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastStaticRouteConfigGroup=_AgentMulticastStaticRouteConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,4,12))
_AgentMulticastStaticRouteTable_Object=MibTable
agentMulticastStaticRouteTable=_AgentMulticastStaticRouteTable_Object((1,3,6,1,4,1,7244,2,4,12,1))
if mibBuilder.loadTexts:agentMulticastStaticRouteTable.setStatus(_A)
_AgentMulticastStaticRouteEntry_Object=MibTableRow
agentMulticastStaticRouteEntry=_AgentMulticastStaticRouteEntry_Object((1,3,6,1,4,1,7244,2,4,12,1,1))
agentMulticastStaticRouteEntry.setIndexNames((0,_D,_s))
if mibBuilder.loadTexts:agentMulticastStaticRouteEntry.setStatus(_A)
_AgentMulticastStaticRouteSourceIP_Type=IpAddress
_AgentMulticastStaticRouteSourceIP_Object=MibTableColumn
agentMulticastStaticRouteSourceIP=_AgentMulticastStaticRouteSourceIP_Object((1,3,6,1,4,1,7244,2,4,12,1,1,1),_AgentMulticastStaticRouteSourceIP_Type())
agentMulticastStaticRouteSourceIP.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastStaticRouteSourceIP.setStatus(_A)
_AgentMulticastStaticRouteSourceMask_Type=IpAddress
_AgentMulticastStaticRouteSourceMask_Object=MibTableColumn
agentMulticastStaticRouteSourceMask=_AgentMulticastStaticRouteSourceMask_Object((1,3,6,1,4,1,7244,2,4,12,1,1,2),_AgentMulticastStaticRouteSourceMask_Type())
agentMulticastStaticRouteSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastStaticRouteSourceMask.setStatus(_A)
_AgentMulticastStaticRouteRPFNeighbor_Type=IpAddress
_AgentMulticastStaticRouteRPFNeighbor_Object=MibTableColumn
agentMulticastStaticRouteRPFNeighbor=_AgentMulticastStaticRouteRPFNeighbor_Object((1,3,6,1,4,1,7244,2,4,12,1,1,3),_AgentMulticastStaticRouteRPFNeighbor_Type())
agentMulticastStaticRouteRPFNeighbor.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastStaticRouteRPFNeighbor.setStatus(_A)
class _AgentMulticastStaticRouteMetric_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentMulticastStaticRouteMetric_Type.__name__=_I
_AgentMulticastStaticRouteMetric_Object=MibTableColumn
agentMulticastStaticRouteMetric=_AgentMulticastStaticRouteMetric_Object((1,3,6,1,4,1,7244,2,4,12,1,1,4),_AgentMulticastStaticRouteMetric_Type())
agentMulticastStaticRouteMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastStaticRouteMetric.setStatus(_A)
_AgentMulticastStaticRouteInterface_Type=Unsigned32
_AgentMulticastStaticRouteInterface_Object=MibTableColumn
agentMulticastStaticRouteInterface=_AgentMulticastStaticRouteInterface_Object((1,3,6,1,4,1,7244,2,4,12,1,1,5),_AgentMulticastStaticRouteInterface_Type())
agentMulticastStaticRouteInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastStaticRouteInterface.setStatus(_A)
class _AgentMulticastStaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_L,1),(_M,4),(_N,6)))
_AgentMulticastStaticRouteStatus_Type.__name__=_B
_AgentMulticastStaticRouteStatus_Object=MibTableColumn
agentMulticastStaticRouteStatus=_AgentMulticastStaticRouteStatus_Object((1,3,6,1,4,1,7244,2,4,12,1,1,6),_AgentMulticastStaticRouteStatus_Type())
agentMulticastStaticRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentMulticastStaticRouteStatus.setStatus(_A)
_AgentIpStaticMRouteTable_Object=MibTable
agentIpStaticMRouteTable=_AgentIpStaticMRouteTable_Object((1,3,6,1,4,1,7244,2,4,13))
if mibBuilder.loadTexts:agentIpStaticMRouteTable.setStatus(_F)
_AgentIpStaticMRouteEntry_Object=MibTableRow
agentIpStaticMRouteEntry=_AgentIpStaticMRouteEntry_Object((1,3,6,1,4,1,7244,2,4,13,1))
agentIpStaticMRouteEntry.setIndexNames((0,_D,_t),(0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:agentIpStaticMRouteEntry.setStatus(_F)
_AgentIpStaticMRouteSrcAddressType_Type=InetAddressType
_AgentIpStaticMRouteSrcAddressType_Object=MibTableColumn
agentIpStaticMRouteSrcAddressType=_AgentIpStaticMRouteSrcAddressType_Object((1,3,6,1,4,1,7244,2,4,13,1,1),_AgentIpStaticMRouteSrcAddressType_Type())
agentIpStaticMRouteSrcAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpStaticMRouteSrcAddressType.setStatus(_F)
_AgentIpStaticMRouteSrcIpAddr_Type=InetAddress
_AgentIpStaticMRouteSrcIpAddr_Object=MibTableColumn
agentIpStaticMRouteSrcIpAddr=_AgentIpStaticMRouteSrcIpAddr_Object((1,3,6,1,4,1,7244,2,4,13,1,2),_AgentIpStaticMRouteSrcIpAddr_Type())
agentIpStaticMRouteSrcIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpStaticMRouteSrcIpAddr.setStatus(_F)
class _AgentIpStaticMRouteSrcNetMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AgentIpStaticMRouteSrcNetMask_Type.__name__=_B
_AgentIpStaticMRouteSrcNetMask_Object=MibTableColumn
agentIpStaticMRouteSrcNetMask=_AgentIpStaticMRouteSrcNetMask_Object((1,3,6,1,4,1,7244,2,4,13,1,3),_AgentIpStaticMRouteSrcNetMask_Type())
agentIpStaticMRouteSrcNetMask.setMaxAccess(_J)
if mibBuilder.loadTexts:agentIpStaticMRouteSrcNetMask.setStatus(_F)
_AgentIpStaticMRouteRpfIpAddr_Type=InetAddress
_AgentIpStaticMRouteRpfIpAddr_Object=MibTableColumn
agentIpStaticMRouteRpfIpAddr=_AgentIpStaticMRouteRpfIpAddr_Object((1,3,6,1,4,1,7244,2,4,13,1,4),_AgentIpStaticMRouteRpfIpAddr_Type())
agentIpStaticMRouteRpfIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpStaticMRouteRpfIpAddr.setStatus(_F)
_AgentIpStaticMRouteIfIndex_Type=InterfaceIndex
_AgentIpStaticMRouteIfIndex_Object=MibTableColumn
agentIpStaticMRouteIfIndex=_AgentIpStaticMRouteIfIndex_Object((1,3,6,1,4,1,7244,2,4,13,1,5),_AgentIpStaticMRouteIfIndex_Type())
agentIpStaticMRouteIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpStaticMRouteIfIndex.setStatus(_F)
class _AgentIpStaticMRoutePreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentIpStaticMRoutePreference_Type.__name__=_B
_AgentIpStaticMRoutePreference_Object=MibTableColumn
agentIpStaticMRoutePreference=_AgentIpStaticMRoutePreference_Object((1,3,6,1,4,1,7244,2,4,13,1,6),_AgentIpStaticMRoutePreference_Type())
agentIpStaticMRoutePreference.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpStaticMRoutePreference.setStatus(_F)
_AgentIpStaticMRouteStatus_Type=RowStatus
_AgentIpStaticMRouteStatus_Object=MibTableColumn
agentIpStaticMRouteStatus=_AgentIpStaticMRouteStatus_Object((1,3,6,1,4,1,7244,2,4,13,1,7),_AgentIpStaticMRouteStatus_Type())
agentIpStaticMRouteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:agentIpStaticMRouteStatus.setStatus(_F)
mibBuilder.exportSymbols(_D,**{'multicast':multicast,'agentMulticastIGMPConfigGroup':agentMulticastIGMPConfigGroup,'agentMulticastIGMPAdminMode':agentMulticastIGMPAdminMode,'agentMulticastIGMPInterfaceTable':agentMulticastIGMPInterfaceTable,'agentMulticastIGMPInterfaceEntry':agentMulticastIGMPInterfaceEntry,_O:agentMulticastIGMPInterfaceIfIndex,'agentMulticastIGMPInterfaceAdminMode':agentMulticastIGMPInterfaceAdminMode,'agentMulticastIGMPProxyInterfaceTable':agentMulticastIGMPProxyInterfaceTable,'agentMulticastIGMPProxyInterfaceEntry':agentMulticastIGMPProxyInterfaceEntry,_P:agentMulticastIGMPProxyInterfaceIfIndex,'agentMulticastIGMPProxyInterfaceAdminMode':agentMulticastIGMPProxyInterfaceAdminMode,'agentMulticastIGMPProxyInterfaceInterval':agentMulticastIGMPProxyInterfaceInterval,'agentMulticastPIMConfigGroup':agentMulticastPIMConfigGroup,'agentMulticastPIMConfigMode':agentMulticastPIMConfigMode,'agentMulticastPIMSMConfigGroup':agentMulticastPIMSMConfigGroup,'agentMulticastPIMSMAdminMode':agentMulticastPIMSMAdminMode,'agentMulticastPIMSMDataThresholdRate':agentMulticastPIMSMDataThresholdRate,'agentMulticastPIMSMStaticRPTable':agentMulticastPIMSMStaticRPTable,'agentMulticastPIMSMStaticRPEntry':agentMulticastPIMSMStaticRPEntry,_Q:agentMulticastPIMSMStaticRPIpAddr,_R:agentMulticastPIMSMStaticRPGroupIpAddr,_S:agentMulticastPIMSMStaticRPGroupIpMask,'agentMulticastPIMSMStaticRPStatus':agentMulticastPIMSMStaticRPStatus,'agentMulticastPIMSMCBSRInterfaceTable':agentMulticastPIMSMCBSRInterfaceTable,'agentMulticastPIMSMCBSRInterfaceEntry':agentMulticastPIMSMCBSRInterfaceEntry,_T:agentMulticastPIMSMCBSRInterfaceIndex,'agentMulticastPIMSMCBSRInterfaceHashMaskLength':agentMulticastPIMSMCBSRInterfaceHashMaskLength,'agentMulticastPIMSMCBSRInterfacePriority':agentMulticastPIMSMCBSRInterfacePriority,'agentMulticastPIMSMSSMTable':agentMulticastPIMSMSSMTable,'agentMulticastPIMSMSSMEntry':agentMulticastPIMSMSSMEntry,_U:agentMulticastPIMSMSSMGroupAddress,_V:agentMulticastPIMSMSSMGroupMask,'agentMulticastPIMSMSSMStatus':agentMulticastPIMSMSSMStatus,'agentMulticastPIMSMInterfaceTable':agentMulticastPIMSMInterfaceTable,'agentMulticastPIMSMInterfaceEntry':agentMulticastPIMSMInterfaceEntry,_W:agentMulticastPIMSMInterfaceIndex,'agentMulticastPIMSMInterfaceAdminMode':agentMulticastPIMSMInterfaceAdminMode,'agentMulticastPIMSMInterfaceHelloInterval':agentMulticastPIMSMInterfaceHelloInterval,'agentMulticastPIMSMInterfaceJoinPruneInterval':agentMulticastPIMSMInterfaceJoinPruneInterval,'agentMulticastPIMSMInterfaceBsrBorder':agentMulticastPIMSMInterfaceBsrBorder,'agentMulticastPIMSMInterfaceDrPriority':agentMulticastPIMSMInterfaceDrPriority,'agentMulticastPIMSMInterfaceCBSRHashMaskLength':agentMulticastPIMSMInterfaceCBSRHashMaskLength,'agentMulticastPIMSMInterfaceCRPPreference':agentMulticastPIMSMInterfaceCRPPreference,'agentMulticastPIMSMCandRPTable':agentMulticastPIMSMCandRPTable,'agentMulticastPIMSMCandRPEntry':agentMulticastPIMSMCandRPEntry,_X:agentMulticastPIMSMCandRPAddress,_Y:agentMulticastPIMSMCandRPGroupAddress,_Z:agentMulticastPIMSMCandRPGroupPrefixLength,'agentMulticastPIMSMCandRPStatus':agentMulticastPIMSMCandRPStatus,'agentMulticastPIMDMConfigGroup':agentMulticastPIMDMConfigGroup,'agentMulticastPIMDMAdminMode':agentMulticastPIMDMAdminMode,'agentMulticastPIMDMInterfaceTable':agentMulticastPIMDMInterfaceTable,'agentMulticastPIMDMInterfaceEntry':agentMulticastPIMDMInterfaceEntry,_a:agentMulticastPIMDMInterfaceIndex,'agentMulticastPIMDMInterfaceMode':agentMulticastPIMDMInterfaceMode,'agentMulticastPIMDMInterfaceHelloInterval':agentMulticastPIMDMInterfaceHelloInterval,'agentMulticastRoutingConfigGroup':agentMulticastRoutingConfigGroup,'agentMulticastRoutingAdminMode':agentMulticastRoutingAdminMode,'agentMulticastDVMRPConfigGroup':agentMulticastDVMRPConfigGroup,'agentMulticastDVMRPAdminMode':agentMulticastDVMRPAdminMode,'agentMulticastDVMRPInterfaceTable':agentMulticastDVMRPInterfaceTable,'agentMulticastDVMRPInterfaceEntry':agentMulticastDVMRPInterfaceEntry,_b:agentMulticastDVMRPInterfaceIfIndex,'agentMulticastDVMRPInterfaceAdminMode':agentMulticastDVMRPInterfaceAdminMode,'agentMulticastDVMRPInterfaceMetric':agentMulticastDVMRPInterfaceMetric,'agentMulticastDVMRPInterfaceGenerationId':agentMulticastDVMRPInterfaceGenerationId,'agentMulticastMLDConfigGroup':agentMulticastMLDConfigGroup,'agentMulticastMLDAdminMode':agentMulticastMLDAdminMode,'agentMulticastMLDInterfaceTable':agentMulticastMLDInterfaceTable,'agentMulticastMLDInterfaceEntry':agentMulticastMLDInterfaceEntry,_c:agentMulticastMLDInterfaceIfIndex,'agentMulticastMLDInterfaceAdminMode':agentMulticastMLDInterfaceAdminMode,'agentMulticastMLDProxyInterfaceTable':agentMulticastMLDProxyInterfaceTable,'agentMulticastMLDProxyInterfaceEntry':agentMulticastMLDProxyInterfaceEntry,_d:agentMulticastMLDProxyInterfaceIfIndex,'agentMulticastMLDProxyInterfaceAdminMode':agentMulticastMLDProxyInterfaceAdminMode,'agentMulticastMLDProxyInterfaceInterval':agentMulticastMLDProxyInterfaceInterval,'agentMulticastIPv6PIMSMConfigGroup':agentMulticastIPv6PIMSMConfigGroup,'agentMulticastIPv6PIMSMAdminMode':agentMulticastIPv6PIMSMAdminMode,'agentMulticastIPv6PIMSMDataThresholdRate':agentMulticastIPv6PIMSMDataThresholdRate,'agentMulticastIPv6PIMSMStaticRPTable':agentMulticastIPv6PIMSMStaticRPTable,'agentMulticastIPv6PIMSMStaticRPEntry':agentMulticastIPv6PIMSMStaticRPEntry,_e:agentMulticastIPv6PIMSMStaticRPIpAddr,_f:agentMulticastIPv6PIMSMStaticRPGroupIpAddr,_g:agentMulticastIPv6PIMSMStaticRPGroupIpPrefix,'agentMulticastIPv6PIMSMStaticRPStatus':agentMulticastIPv6PIMSMStaticRPStatus,'agentMulticastIPv6PIMSMCBSRInterfaceTable':agentMulticastIPv6PIMSMCBSRInterfaceTable,'agentMulticastIPv6PIMSMCBSRInterfaceEntry':agentMulticastIPv6PIMSMCBSRInterfaceEntry,_h:agentMulticastIPv6PIMSMCBSRInterfaceIndex,'agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength':agentMulticastIPv6PIMSMCBSRInterfaceHashMaskLength,'agentMulticastIPv6PIMSMCBSRInterfacePriority':agentMulticastIPv6PIMSMCBSRInterfacePriority,'agentMulticastIPv6PIMSMSSMTable':agentMulticastIPv6PIMSMSSMTable,'agentMulticastIPv6PIMSMSSMEntry':agentMulticastIPv6PIMSMSSMEntry,_i:agentMulticastIPv6PIMSMSSMGroupAddress,_j:agentMulticastIPv6PIMSMSSMGroupMask,'agentMulticastIPv6PIMSMSSMStatus':agentMulticastIPv6PIMSMSSMStatus,'agentMulticastIPv6PIMSMInterfaceTable':agentMulticastIPv6PIMSMInterfaceTable,'agentMulticastIPv6PIMSMInterfaceEntry':agentMulticastIPv6PIMSMInterfaceEntry,_k:agentMulticastIPv6PIMSMInterfaceIndex,'agentMulticastIPv6PIMSMInterfaceAdminMode':agentMulticastIPv6PIMSMInterfaceAdminMode,'agentMulticastIPv6PIMSMInterfaceHelloInterval':agentMulticastIPv6PIMSMInterfaceHelloInterval,'agentMulticastIPv6PIMSMInterfaceJoinPruneInterval':agentMulticastIPv6PIMSMInterfaceJoinPruneInterval,'agentMulticastIPv6PIMSMInterfaceBsrBorder':agentMulticastIPv6PIMSMInterfaceBsrBorder,'agentMulticastIPv6PIMSMInterfaceDrPriority':agentMulticastIPv6PIMSMInterfaceDrPriority,'agentMulticastIPv6PIMSMCandRPTable':agentMulticastIPv6PIMSMCandRPTable,'agentMulticastIPv6PIMSMCandRPEntry':agentMulticastIPv6PIMSMCandRPEntry,_l:agentMulticastIPv6PIMSMCandRPAddress,_m:agentMulticastIPv6PIMSMCandRPGroupAddress,_n:agentMulticastIPv6PIMSMCandRPGroupPrefixLength,'agentMulticastIPv6PIMSMCandRPStatus':agentMulticastIPv6PIMSMCandRPStatus,'agentMulticastIPv6PIMDMConfigGroup':agentMulticastIPv6PIMDMConfigGroup,'agentMulticastIPv6PIMDMAdminMode':agentMulticastIPv6PIMDMAdminMode,'agentMulticastIPv6PIMDMInterfaceTable':agentMulticastIPv6PIMDMInterfaceTable,'agentMulticastIPv6PIMDMInterfaceEntry':agentMulticastIPv6PIMDMInterfaceEntry,_o:agentMulticastIPv6PIMDMInterfaceIndex,'agentMulticastIPv6PIMDMInterfaceMode':agentMulticastIPv6PIMDMInterfaceMode,'agentMulticastIPv6PIMDMInterfaceHelloInterval':agentMulticastIPv6PIMDMInterfaceHelloInterval,'agentMulticastAdminBoundaryConfigGroup':agentMulticastAdminBoundaryConfigGroup,'agentMulticastAdminBoundaryTable':agentMulticastAdminBoundaryTable,'agentMulticastAdminBoundaryEntry':agentMulticastAdminBoundaryEntry,_p:agentMulticastAdminBoundaryIndex,_q:agentMulticastAdminBoundaryGroupAddress,_r:agentMulticastAdminBoundaryGroupMask,'agentMulticastAdminBoundaryStatus':agentMulticastAdminBoundaryStatus,'agentMulticastStaticRouteConfigGroup':agentMulticastStaticRouteConfigGroup,'agentMulticastStaticRouteTable':agentMulticastStaticRouteTable,'agentMulticastStaticRouteEntry':agentMulticastStaticRouteEntry,_s:agentMulticastStaticRouteSourceIP,'agentMulticastStaticRouteSourceMask':agentMulticastStaticRouteSourceMask,'agentMulticastStaticRouteRPFNeighbor':agentMulticastStaticRouteRPFNeighbor,'agentMulticastStaticRouteMetric':agentMulticastStaticRouteMetric,'agentMulticastStaticRouteInterface':agentMulticastStaticRouteInterface,'agentMulticastStaticRouteStatus':agentMulticastStaticRouteStatus,'agentIpStaticMRouteTable':agentIpStaticMRouteTable,'agentIpStaticMRouteEntry':agentIpStaticMRouteEntry,_t:agentIpStaticMRouteSrcAddressType,_u:agentIpStaticMRouteSrcIpAddr,_v:agentIpStaticMRouteSrcNetMask,'agentIpStaticMRouteRpfIpAddr':agentIpStaticMRouteRpfIpAddr,'agentIpStaticMRouteIfIndex':agentIpStaticMRouteIfIndex,'agentIpStaticMRoutePreference':agentIpStaticMRoutePreference,'agentIpStaticMRouteStatus':agentIpStaticMRouteStatus})