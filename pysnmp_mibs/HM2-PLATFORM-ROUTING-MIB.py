_AP='hm2AgentOspfNbrEntry'
_AO='hm2AgentOspfIfMetricEntry'
_AN='hm2AgentOspfAreaNSSAEntry'
_AM='hm2AgentOspfVirtIfEntry'
_AL='hm2AgentOspfIfEntry'
_AK='hm2AgentRip2IfConfEntry'
_AJ='hm2AgentDynamicNeighbourAddress'
_AI='hm2AgentDynamicNeighbourAddressType'
_AH='hm2AgentStaticNeighbourAddress'
_AG='hm2AgentStaticNeighbourAddressType'
_AF='hm2AgentVrrpDomainId'
_AE='supervisorDown'
_AD='noSupervisor'
_AC='hm2AgentVrrpExtVrid'
_AB='hm2AgentVrrpExtIfIndex'
_AA='hm2AgentVrrpTrackId'
_A9='hm2AgentVrrpTrackVrid'
_A8='hm2AgentVrrpTrackIfIndex'
_A7='hm2AgentOspfRouteMask'
_A6='hm2AgentOspfRouteNet'
_A5='hm2AgentEcmpNextHopCount'
_A4='hm2AgentOspfSpfIndex'
_A3='hm2AgentOspfQueueIndex'
_A2='hm2AgentSwitchInternalVlanId'
_A1='hm2AgentSwitchIpHelperAddress'
_A0='hm2AgentSwitchIpHelperUdpPort'
_z='hm2AgentOspfAsLsdbRouterId'
_y='hm2AgentOspfAsLsdbLsid'
_x='hm2AgentOspfAsLsdbType'
_w='hm2AgentOspfLocalLsdbRouterId'
_v='hm2AgentOspfLocalLsdbLsid'
_u='hm2AgentOspfLocalLsdbType'
_t='hm2AgentOspfLocalLsdbAddressLessIf'
_s='hm2AgentOspfLocalLsdbIpAddress'
_r='hm2AgentOspfAreaOpaqueLsdbRouterId'
_q='hm2AgentOspfAreaOpaqueLsdbLsid'
_p='hm2AgentOspfAreaOpaqueLsdbType'
_o='hm2AgentOspfAreaOpaqueLsdbAreaId'
_n='hm2AgentOspfRouteRedistSource'
_m='externalType2'
_l='externalType1'
_k='connected'
_j='hm2AgentRipRouteRedistSource'
_i='hm2AgentSwitchIntfIpHelperIpAddress'
_h='hm2AgentSwitchIntfIpHelperUdpPort'
_g='hm2AgentSwitchSecondaryIpAddress'
_f='hm2AgentSwitchIpVlanId'
_e='hm2AgentSwitchIpRouterDiscoveryIfIndex'
_d='hm2AgentSwitchIntfArpIfIndex'
_c='hm2AgentSwitchIntfArpIpAddress'
_b='vrrpOperVrId'
_a='VRRP-MIB'
_Z='VlanId'
_Y='PhysAddress'
_X='ifIndex'
_W='IF-MIB'
_V='seconds'
_U='hm2AgentSwitchIpInterfaceIfIndex'
_T='static'
_S='IpAddress'
_R='InetAddress'
_Q='OctetString'
_P='not-applicable'
_O='false'
_N='true'
_M='none'
_L='obsolete'
_K='milli-seconds'
_J='TruthValue'
_I='Unsigned32'
_H='read-create'
_G='not-accessible'
_F='HmEnabledStatus'
_E='HM2-PLATFORM-ROUTING-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2PlatformMibs=mibBuilder.importSymbols('HM2-TC-MIB',_F,'hm2PlatformMibs')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_W,'InterfaceIndex','InterfaceIndexOrZero',_X)
InetAddress,InetAddressIPv4,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,'InetAddressIPv4','InetAddressType')
RouterID,ospfAreaEntry,ospfIfEntry,ospfIfMetricEntry,ospfNbrEntry,ospfVirtIfEntry=mibBuilder.importSymbols('OSPF-MIB','RouterID','ospfAreaEntry','ospfIfEntry','ospfIfMetricEntry','ospfNbrEntry','ospfVirtIfEntry')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_Z)
rip2IfConfEntry,=mibBuilder.importSymbols('RIPv2-MIB','rip2IfConfEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_S,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_Y,'RowStatus','TextualConvention',_J)
vrrpOperVrId,=mibBuilder.importSymbols(_a,_b)
hm2PlatformRouting=ModuleIdentity((1,3,6,1,4,1,248,12,2))
if mibBuilder.loadTexts:hm2PlatformRouting.setRevisions(('2011-09-08 00:00',))
_Hm2AgentSwitchArpGroup_ObjectIdentity=ObjectIdentity
hm2AgentSwitchArpGroup=_Hm2AgentSwitchArpGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,1))
class _Hm2AgentSwitchArpAgeoutTime_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,21600))
_Hm2AgentSwitchArpAgeoutTime_Type.__name__=_D
_Hm2AgentSwitchArpAgeoutTime_Object=MibScalar
hm2AgentSwitchArpAgeoutTime=_Hm2AgentSwitchArpAgeoutTime_Object((1,3,6,1,4,1,248,12,2,1,1),_Hm2AgentSwitchArpAgeoutTime_Type())
hm2AgentSwitchArpAgeoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpAgeoutTime.setStatus(_A)
class _Hm2AgentSwitchArpResponseTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Hm2AgentSwitchArpResponseTime_Type.__name__=_D
_Hm2AgentSwitchArpResponseTime_Object=MibScalar
hm2AgentSwitchArpResponseTime=_Hm2AgentSwitchArpResponseTime_Object((1,3,6,1,4,1,248,12,2,1,2),_Hm2AgentSwitchArpResponseTime_Type())
hm2AgentSwitchArpResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpResponseTime.setStatus(_A)
class _Hm2AgentSwitchArpMaxRetries_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Hm2AgentSwitchArpMaxRetries_Type.__name__=_D
_Hm2AgentSwitchArpMaxRetries_Object=MibScalar
hm2AgentSwitchArpMaxRetries=_Hm2AgentSwitchArpMaxRetries_Object((1,3,6,1,4,1,248,12,2,1,3),_Hm2AgentSwitchArpMaxRetries_Type())
hm2AgentSwitchArpMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpMaxRetries.setStatus(_A)
_Hm2AgentSwitchArpCacheSize_Type=Integer32
_Hm2AgentSwitchArpCacheSize_Object=MibScalar
hm2AgentSwitchArpCacheSize=_Hm2AgentSwitchArpCacheSize_Object((1,3,6,1,4,1,248,12,2,1,4),_Hm2AgentSwitchArpCacheSize_Type())
hm2AgentSwitchArpCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpCacheSize.setStatus(_A)
class _Hm2AgentSwitchArpDynamicRenew_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchArpDynamicRenew_Type.__name__=_F
_Hm2AgentSwitchArpDynamicRenew_Object=MibScalar
hm2AgentSwitchArpDynamicRenew=_Hm2AgentSwitchArpDynamicRenew_Object((1,3,6,1,4,1,248,12,2,1,5),_Hm2AgentSwitchArpDynamicRenew_Type())
hm2AgentSwitchArpDynamicRenew.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpDynamicRenew.setStatus(_A)
_Hm2AgentSwitchArpTotalEntryCountCurrent_Type=Gauge32
_Hm2AgentSwitchArpTotalEntryCountCurrent_Object=MibScalar
hm2AgentSwitchArpTotalEntryCountCurrent=_Hm2AgentSwitchArpTotalEntryCountCurrent_Object((1,3,6,1,4,1,248,12,2,1,6),_Hm2AgentSwitchArpTotalEntryCountCurrent_Type())
hm2AgentSwitchArpTotalEntryCountCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchArpTotalEntryCountCurrent.setStatus(_A)
_Hm2AgentSwitchArpTotalEntryCountPeak_Type=Gauge32
_Hm2AgentSwitchArpTotalEntryCountPeak_Object=MibScalar
hm2AgentSwitchArpTotalEntryCountPeak=_Hm2AgentSwitchArpTotalEntryCountPeak_Object((1,3,6,1,4,1,248,12,2,1,7),_Hm2AgentSwitchArpTotalEntryCountPeak_Type())
hm2AgentSwitchArpTotalEntryCountPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchArpTotalEntryCountPeak.setStatus(_A)
_Hm2AgentSwitchArpStaticEntryCountCurrent_Type=Gauge32
_Hm2AgentSwitchArpStaticEntryCountCurrent_Object=MibScalar
hm2AgentSwitchArpStaticEntryCountCurrent=_Hm2AgentSwitchArpStaticEntryCountCurrent_Object((1,3,6,1,4,1,248,12,2,1,8),_Hm2AgentSwitchArpStaticEntryCountCurrent_Type())
hm2AgentSwitchArpStaticEntryCountCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchArpStaticEntryCountCurrent.setStatus(_A)
_Hm2AgentSwitchArpStaticEntryCountMax_Type=Integer32
_Hm2AgentSwitchArpStaticEntryCountMax_Object=MibScalar
hm2AgentSwitchArpStaticEntryCountMax=_Hm2AgentSwitchArpStaticEntryCountMax_Object((1,3,6,1,4,1,248,12,2,1,9),_Hm2AgentSwitchArpStaticEntryCountMax_Type())
hm2AgentSwitchArpStaticEntryCountMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchArpStaticEntryCountMax.setStatus(_A)
_Hm2AgentSwitchLocalProxyArpTable_Object=MibTable
hm2AgentSwitchLocalProxyArpTable=_Hm2AgentSwitchLocalProxyArpTable_Object((1,3,6,1,4,1,248,12,2,1,11))
if mibBuilder.loadTexts:hm2AgentSwitchLocalProxyArpTable.setStatus(_A)
_Hm2AgentSwitchLocalProxyArpEntry_Object=MibTableRow
hm2AgentSwitchLocalProxyArpEntry=_Hm2AgentSwitchLocalProxyArpEntry_Object((1,3,6,1,4,1,248,12,2,1,11,1))
hm2AgentSwitchLocalProxyArpEntry.setIndexNames((0,_W,_X))
if mibBuilder.loadTexts:hm2AgentSwitchLocalProxyArpEntry.setStatus(_A)
class _Hm2AgentSwitchLocalProxyArpMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchLocalProxyArpMode_Type.__name__=_F
_Hm2AgentSwitchLocalProxyArpMode_Object=MibTableColumn
hm2AgentSwitchLocalProxyArpMode=_Hm2AgentSwitchLocalProxyArpMode_Object((1,3,6,1,4,1,248,12,2,1,11,1,1),_Hm2AgentSwitchLocalProxyArpMode_Type())
hm2AgentSwitchLocalProxyArpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchLocalProxyArpMode.setStatus(_A)
_Hm2AgentSwitchIntfArpTable_Object=MibTable
hm2AgentSwitchIntfArpTable=_Hm2AgentSwitchIntfArpTable_Object((1,3,6,1,4,1,248,12,2,1,12))
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpTable.setStatus(_A)
_Hm2AgentSwitchIntfArpEntry_Object=MibTableRow
hm2AgentSwitchIntfArpEntry=_Hm2AgentSwitchIntfArpEntry_Object((1,3,6,1,4,1,248,12,2,1,12,1))
hm2AgentSwitchIntfArpEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpEntry.setStatus(_A)
_Hm2AgentSwitchIntfArpIpAddress_Type=IpAddress
_Hm2AgentSwitchIntfArpIpAddress_Object=MibTableColumn
hm2AgentSwitchIntfArpIpAddress=_Hm2AgentSwitchIntfArpIpAddress_Object((1,3,6,1,4,1,248,12,2,1,12,1,1),_Hm2AgentSwitchIntfArpIpAddress_Type())
hm2AgentSwitchIntfArpIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpIpAddress.setStatus(_A)
_Hm2AgentSwitchIntfArpIfIndex_Type=InterfaceIndex
_Hm2AgentSwitchIntfArpIfIndex_Object=MibTableColumn
hm2AgentSwitchIntfArpIfIndex=_Hm2AgentSwitchIntfArpIfIndex_Object((1,3,6,1,4,1,248,12,2,1,12,1,2),_Hm2AgentSwitchIntfArpIfIndex_Type())
hm2AgentSwitchIntfArpIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpIfIndex.setStatus(_A)
_Hm2AgentSwitchIntfArpAge_Type=TimeTicks
_Hm2AgentSwitchIntfArpAge_Object=MibTableColumn
hm2AgentSwitchIntfArpAge=_Hm2AgentSwitchIntfArpAge_Object((1,3,6,1,4,1,248,12,2,1,12,1,3),_Hm2AgentSwitchIntfArpAge_Type())
hm2AgentSwitchIntfArpAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpAge.setStatus(_A)
_Hm2AgentSwitchIntfArpMacAddress_Type=PhysAddress
_Hm2AgentSwitchIntfArpMacAddress_Object=MibTableColumn
hm2AgentSwitchIntfArpMacAddress=_Hm2AgentSwitchIntfArpMacAddress_Object((1,3,6,1,4,1,248,12,2,1,12,1,4),_Hm2AgentSwitchIntfArpMacAddress_Type())
hm2AgentSwitchIntfArpMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpMacAddress.setStatus(_A)
class _Hm2AgentSwitchIntfArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('gateway',2),(_T,3),('dynamic',4)))
_Hm2AgentSwitchIntfArpType_Type.__name__=_D
_Hm2AgentSwitchIntfArpType_Object=MibTableColumn
hm2AgentSwitchIntfArpType=_Hm2AgentSwitchIntfArpType_Object((1,3,6,1,4,1,248,12,2,1,12,1,5),_Hm2AgentSwitchIntfArpType_Type())
hm2AgentSwitchIntfArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpType.setStatus(_A)
_Hm2AgentSwitchIntfArpStatus_Type=RowStatus
_Hm2AgentSwitchIntfArpStatus_Object=MibTableColumn
hm2AgentSwitchIntfArpStatus=_Hm2AgentSwitchIntfArpStatus_Object((1,3,6,1,4,1,248,12,2,1,12,1,6),_Hm2AgentSwitchIntfArpStatus_Type())
hm2AgentSwitchIntfArpStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchIntfArpStatus.setStatus(_A)
class _Hm2AgentSwitchArpSparseLearn_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentSwitchArpSparseLearn_Type.__name__=_F
_Hm2AgentSwitchArpSparseLearn_Object=MibScalar
hm2AgentSwitchArpSparseLearn=_Hm2AgentSwitchArpSparseLearn_Object((1,3,6,1,4,1,248,12,2,1,100),_Hm2AgentSwitchArpSparseLearn_Type())
hm2AgentSwitchArpSparseLearn.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpSparseLearn.setStatus(_A)
class _Hm2AgentSwitchArpCacheClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('flushARP',2),('flushARPWithGateway',3)))
_Hm2AgentSwitchArpCacheClear_Type.__name__=_D
_Hm2AgentSwitchArpCacheClear_Object=MibScalar
hm2AgentSwitchArpCacheClear=_Hm2AgentSwitchArpCacheClear_Object((1,3,6,1,4,1,248,12,2,1,101),_Hm2AgentSwitchArpCacheClear_Type())
hm2AgentSwitchArpCacheClear.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchArpCacheClear.setStatus(_A)
class _Hm2AgentSwitchProxyArpMaxResponseDelay_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1000))
_Hm2AgentSwitchProxyArpMaxResponseDelay_Type.__name__=_D
_Hm2AgentSwitchProxyArpMaxResponseDelay_Object=MibScalar
hm2AgentSwitchProxyArpMaxResponseDelay=_Hm2AgentSwitchProxyArpMaxResponseDelay_Object((1,3,6,1,4,1,248,12,2,1,248),_Hm2AgentSwitchProxyArpMaxResponseDelay_Type())
hm2AgentSwitchProxyArpMaxResponseDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchProxyArpMaxResponseDelay.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentSwitchProxyArpMaxResponseDelay.setUnits(_K)
_Hm2AgentSwitchIpGroup_ObjectIdentity=ObjectIdentity
hm2AgentSwitchIpGroup=_Hm2AgentSwitchIpGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,2))
class _Hm2AgentSwitchIpRoutingMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchIpRoutingMode_Type.__name__=_F
_Hm2AgentSwitchIpRoutingMode_Object=MibScalar
hm2AgentSwitchIpRoutingMode=_Hm2AgentSwitchIpRoutingMode_Object((1,3,6,1,4,1,248,12,2,2,1),_Hm2AgentSwitchIpRoutingMode_Type())
hm2AgentSwitchIpRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRoutingMode.setStatus(_A)
_Hm2AgentSwitchIpDefaultGateway_Type=IpAddress
_Hm2AgentSwitchIpDefaultGateway_Object=MibScalar
hm2AgentSwitchIpDefaultGateway=_Hm2AgentSwitchIpDefaultGateway_Object((1,3,6,1,4,1,248,12,2,2,2),_Hm2AgentSwitchIpDefaultGateway_Type())
hm2AgentSwitchIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpDefaultGateway.setStatus(_A)
_Hm2AgentSwitchIpInterfaceTable_Object=MibTable
hm2AgentSwitchIpInterfaceTable=_Hm2AgentSwitchIpInterfaceTable_Object((1,3,6,1,4,1,248,12,2,2,3))
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceTable.setStatus(_A)
_Hm2AgentSwitchIpInterfaceEntry_Object=MibTableRow
hm2AgentSwitchIpInterfaceEntry=_Hm2AgentSwitchIpInterfaceEntry_Object((1,3,6,1,4,1,248,12,2,2,3,1))
hm2AgentSwitchIpInterfaceEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceEntry.setStatus(_A)
_Hm2AgentSwitchIpInterfaceIfIndex_Type=InterfaceIndex
_Hm2AgentSwitchIpInterfaceIfIndex_Object=MibTableColumn
hm2AgentSwitchIpInterfaceIfIndex=_Hm2AgentSwitchIpInterfaceIfIndex_Object((1,3,6,1,4,1,248,12,2,2,3,1,1),_Hm2AgentSwitchIpInterfaceIfIndex_Type())
hm2AgentSwitchIpInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceIfIndex.setStatus(_A)
class _Hm2AgentSwitchIPAddressConfigMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('manual',1),('dhcp',2)))
_Hm2AgentSwitchIPAddressConfigMethod_Type.__name__=_D
_Hm2AgentSwitchIPAddressConfigMethod_Object=MibTableColumn
hm2AgentSwitchIPAddressConfigMethod=_Hm2AgentSwitchIPAddressConfigMethod_Object((1,3,6,1,4,1,248,12,2,2,3,1,2),_Hm2AgentSwitchIPAddressConfigMethod_Type())
hm2AgentSwitchIPAddressConfigMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIPAddressConfigMethod.setStatus(_A)
_Hm2AgentSwitchIpInterfaceIpAddress_Type=IpAddress
_Hm2AgentSwitchIpInterfaceIpAddress_Object=MibTableColumn
hm2AgentSwitchIpInterfaceIpAddress=_Hm2AgentSwitchIpInterfaceIpAddress_Object((1,3,6,1,4,1,248,12,2,2,3,1,3),_Hm2AgentSwitchIpInterfaceIpAddress_Type())
hm2AgentSwitchIpInterfaceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceIpAddress.setStatus(_A)
_Hm2AgentSwitchIpInterfaceNetMask_Type=IpAddress
_Hm2AgentSwitchIpInterfaceNetMask_Object=MibTableColumn
hm2AgentSwitchIpInterfaceNetMask=_Hm2AgentSwitchIpInterfaceNetMask_Object((1,3,6,1,4,1,248,12,2,2,3,1,4),_Hm2AgentSwitchIpInterfaceNetMask_Type())
hm2AgentSwitchIpInterfaceNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceNetMask.setStatus(_A)
_Hm2AgentSwitchIpInterfaceClearIp_Type=HmEnabledStatus
_Hm2AgentSwitchIpInterfaceClearIp_Object=MibTableColumn
hm2AgentSwitchIpInterfaceClearIp=_Hm2AgentSwitchIpInterfaceClearIp_Object((1,3,6,1,4,1,248,12,2,2,3,1,5),_Hm2AgentSwitchIpInterfaceClearIp_Type())
hm2AgentSwitchIpInterfaceClearIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceClearIp.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceRoutingMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchIpInterfaceRoutingMode_Type.__name__=_F
_Hm2AgentSwitchIpInterfaceRoutingMode_Object=MibTableColumn
hm2AgentSwitchIpInterfaceRoutingMode=_Hm2AgentSwitchIpInterfaceRoutingMode_Object((1,3,6,1,4,1,248,12,2,2,3,1,6),_Hm2AgentSwitchIpInterfaceRoutingMode_Type())
hm2AgentSwitchIpInterfaceRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceRoutingMode.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceProxyARPMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchIpInterfaceProxyARPMode_Type.__name__=_F
_Hm2AgentSwitchIpInterfaceProxyARPMode_Object=MibTableColumn
hm2AgentSwitchIpInterfaceProxyARPMode=_Hm2AgentSwitchIpInterfaceProxyARPMode_Object((1,3,6,1,4,1,248,12,2,2,3,1,7),_Hm2AgentSwitchIpInterfaceProxyARPMode_Type())
hm2AgentSwitchIpInterfaceProxyARPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceProxyARPMode.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(68,12266))
_Hm2AgentSwitchIpInterfaceMtuValue_Type.__name__=_I
_Hm2AgentSwitchIpInterfaceMtuValue_Object=MibTableColumn
hm2AgentSwitchIpInterfaceMtuValue=_Hm2AgentSwitchIpInterfaceMtuValue_Object((1,3,6,1,4,1,248,12,2,2,3,1,8),_Hm2AgentSwitchIpInterfaceMtuValue_Type())
hm2AgentSwitchIpInterfaceMtuValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceMtuValue.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_Hm2AgentSwitchIpInterfaceBandwidth_Type.__name__=_I
_Hm2AgentSwitchIpInterfaceBandwidth_Object=MibTableColumn
hm2AgentSwitchIpInterfaceBandwidth=_Hm2AgentSwitchIpInterfaceBandwidth_Object((1,3,6,1,4,1,248,12,2,2,3,1,9),_Hm2AgentSwitchIpInterfaceBandwidth_Type())
hm2AgentSwitchIpInterfaceBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceBandwidth.setStatus(_A)
_Hm2AgentSwitchIpInterfaceUnnumberedIfIndex_Type=InterfaceIndexOrZero
_Hm2AgentSwitchIpInterfaceUnnumberedIfIndex_Object=MibTableColumn
hm2AgentSwitchIpInterfaceUnnumberedIfIndex=_Hm2AgentSwitchIpInterfaceUnnumberedIfIndex_Object((1,3,6,1,4,1,248,12,2,2,3,1,10),_Hm2AgentSwitchIpInterfaceUnnumberedIfIndex_Type())
hm2AgentSwitchIpInterfaceUnnumberedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceUnnumberedIfIndex.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceIcmpUnreachables_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentSwitchIpInterfaceIcmpUnreachables_Type.__name__=_F
_Hm2AgentSwitchIpInterfaceIcmpUnreachables_Object=MibTableColumn
hm2AgentSwitchIpInterfaceIcmpUnreachables=_Hm2AgentSwitchIpInterfaceIcmpUnreachables_Object((1,3,6,1,4,1,248,12,2,2,3,1,11),_Hm2AgentSwitchIpInterfaceIcmpUnreachables_Type())
hm2AgentSwitchIpInterfaceIcmpUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceIcmpUnreachables.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceIcmpRedirects_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentSwitchIpInterfaceIcmpRedirects_Type.__name__=_F
_Hm2AgentSwitchIpInterfaceIcmpRedirects_Object=MibTableColumn
hm2AgentSwitchIpInterfaceIcmpRedirects=_Hm2AgentSwitchIpInterfaceIcmpRedirects_Object((1,3,6,1,4,1,248,12,2,2,3,1,12),_Hm2AgentSwitchIpInterfaceIcmpRedirects_Type())
hm2AgentSwitchIpInterfaceIcmpRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceIcmpRedirects.setStatus(_A)
class _Hm2AgentSwitchDhcpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('renew',1),('release',2),(_M,3)))
_Hm2AgentSwitchDhcpOperation_Type.__name__=_D
_Hm2AgentSwitchDhcpOperation_Object=MibTableColumn
hm2AgentSwitchDhcpOperation=_Hm2AgentSwitchDhcpOperation_Object((1,3,6,1,4,1,248,12,2,2,3,1,13),_Hm2AgentSwitchDhcpOperation_Type())
hm2AgentSwitchDhcpOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchDhcpOperation.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceSuppressed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsuppressed',0),('suppressed',1)))
_Hm2AgentSwitchIpInterfaceSuppressed_Type.__name__=_D
_Hm2AgentSwitchIpInterfaceSuppressed_Object=MibTableColumn
hm2AgentSwitchIpInterfaceSuppressed=_Hm2AgentSwitchIpInterfaceSuppressed_Object((1,3,6,1,4,1,248,12,2,2,3,1,14),_Hm2AgentSwitchIpInterfaceSuppressed_Type())
hm2AgentSwitchIpInterfaceSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceSuppressed.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceNumberOfFlaps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Hm2AgentSwitchIpInterfaceNumberOfFlaps_Type.__name__=_I
_Hm2AgentSwitchIpInterfaceNumberOfFlaps_Object=MibTableColumn
hm2AgentSwitchIpInterfaceNumberOfFlaps=_Hm2AgentSwitchIpInterfaceNumberOfFlaps_Object((1,3,6,1,4,1,248,12,2,2,3,1,15),_Hm2AgentSwitchIpInterfaceNumberOfFlaps_Type())
hm2AgentSwitchIpInterfaceNumberOfFlaps.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceNumberOfFlaps.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceCurrentPenalty_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_Hm2AgentSwitchIpInterfaceCurrentPenalty_Type.__name__=_I
_Hm2AgentSwitchIpInterfaceCurrentPenalty_Object=MibTableColumn
hm2AgentSwitchIpInterfaceCurrentPenalty=_Hm2AgentSwitchIpInterfaceCurrentPenalty_Object((1,3,6,1,4,1,248,12,2,2,3,1,16),_Hm2AgentSwitchIpInterfaceCurrentPenalty_Type())
hm2AgentSwitchIpInterfaceCurrentPenalty.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceCurrentPenalty.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceReUseTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentSwitchIpInterfaceReUseTime_Type.__name__=_I
_Hm2AgentSwitchIpInterfaceReUseTime_Object=MibTableColumn
hm2AgentSwitchIpInterfaceReUseTime=_Hm2AgentSwitchIpInterfaceReUseTime_Object((1,3,6,1,4,1,248,12,2,2,3,1,17),_Hm2AgentSwitchIpInterfaceReUseTime_Type())
hm2AgentSwitchIpInterfaceReUseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceReUseTime.setStatus(_A)
class _Hm2AgentSwitchIpInterfaceNetdirectedBCMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchIpInterfaceNetdirectedBCMode_Type.__name__=_F
_Hm2AgentSwitchIpInterfaceNetdirectedBCMode_Object=MibTableColumn
hm2AgentSwitchIpInterfaceNetdirectedBCMode=_Hm2AgentSwitchIpInterfaceNetdirectedBCMode_Object((1,3,6,1,4,1,248,12,2,2,3,1,248),_Hm2AgentSwitchIpInterfaceNetdirectedBCMode_Type())
hm2AgentSwitchIpInterfaceNetdirectedBCMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpInterfaceNetdirectedBCMode.setStatus(_A)
_Hm2AgentSwitchIpRouterDiscoveryTable_Object=MibTable
hm2AgentSwitchIpRouterDiscoveryTable=_Hm2AgentSwitchIpRouterDiscoveryTable_Object((1,3,6,1,4,1,248,12,2,2,4))
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryTable.setStatus(_A)
_Hm2AgentSwitchIpRouterDiscoveryEntry_Object=MibTableRow
hm2AgentSwitchIpRouterDiscoveryEntry=_Hm2AgentSwitchIpRouterDiscoveryEntry_Object((1,3,6,1,4,1,248,12,2,2,4,1))
hm2AgentSwitchIpRouterDiscoveryEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryEntry.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2AgentSwitchIpRouterDiscoveryIfIndex_Type.__name__=_D
_Hm2AgentSwitchIpRouterDiscoveryIfIndex_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryIfIndex=_Hm2AgentSwitchIpRouterDiscoveryIfIndex_Object((1,3,6,1,4,1,248,12,2,2,4,1,1),_Hm2AgentSwitchIpRouterDiscoveryIfIndex_Type())
hm2AgentSwitchIpRouterDiscoveryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryIfIndex.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__=_F
_Hm2AgentSwitchIpRouterDiscoveryAdvertiseMode_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryAdvertiseMode=_Hm2AgentSwitchIpRouterDiscoveryAdvertiseMode_Object((1,3,6,1,4,1,248,12,2,2,4,1,2),_Hm2AgentSwitchIpRouterDiscoveryAdvertiseMode_Type())
hm2AgentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryAdvertiseMode.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_Hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__=_D
_Hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval=_Hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object((1,3,6,1,4,1,248,12,2,2,4,1,3),_Hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type())
hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_Hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__=_D
_Hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval=_Hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object((1,3,6,1,4,1,248,12,2,2,4,1,4),_Hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type())
hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_Hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__=_D
_Hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime=_Hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object((1,3,6,1,4,1,248,12,2,2,4,1,5),_Hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type())
hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):defaultValue=0
_Hm2AgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__=_D
_Hm2AgentSwitchIpRouterDiscoveryPreferenceLevel_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryPreferenceLevel=_Hm2AgentSwitchIpRouterDiscoveryPreferenceLevel_Object((1,3,6,1,4,1,248,12,2,2,4,1,6),_Hm2AgentSwitchIpRouterDiscoveryPreferenceLevel_Type())
hm2AgentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryPreferenceLevel.setStatus(_A)
class _Hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):defaultHexValue='E0000001'
_Hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__=_S
_Hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object=MibTableColumn
hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress=_Hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object((1,3,6,1,4,1,248,12,2,2,4,1,7),_Hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type())
hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus(_A)
_Hm2AgentSwitchIpVlanTable_Object=MibTable
hm2AgentSwitchIpVlanTable=_Hm2AgentSwitchIpVlanTable_Object((1,3,6,1,4,1,248,12,2,2,5))
if mibBuilder.loadTexts:hm2AgentSwitchIpVlanTable.setStatus(_A)
_Hm2AgentSwitchIpVlanEntry_Object=MibTableRow
hm2AgentSwitchIpVlanEntry=_Hm2AgentSwitchIpVlanEntry_Object((1,3,6,1,4,1,248,12,2,2,5,1))
hm2AgentSwitchIpVlanEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:hm2AgentSwitchIpVlanEntry.setStatus(_A)
_Hm2AgentSwitchIpVlanId_Type=VlanId
_Hm2AgentSwitchIpVlanId_Object=MibTableColumn
hm2AgentSwitchIpVlanId=_Hm2AgentSwitchIpVlanId_Object((1,3,6,1,4,1,248,12,2,2,5,1,1),_Hm2AgentSwitchIpVlanId_Type())
hm2AgentSwitchIpVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpVlanId.setStatus(_A)
_Hm2AgentSwitchIpVlanIfIndex_Type=InterfaceIndex
_Hm2AgentSwitchIpVlanIfIndex_Object=MibTableColumn
hm2AgentSwitchIpVlanIfIndex=_Hm2AgentSwitchIpVlanIfIndex_Object((1,3,6,1,4,1,248,12,2,2,5,1,2),_Hm2AgentSwitchIpVlanIfIndex_Type())
hm2AgentSwitchIpVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpVlanIfIndex.setStatus(_A)
_Hm2AgentSwitchIpVlanRoutingStatus_Type=RowStatus
_Hm2AgentSwitchIpVlanRoutingStatus_Object=MibTableColumn
hm2AgentSwitchIpVlanRoutingStatus=_Hm2AgentSwitchIpVlanRoutingStatus_Object((1,3,6,1,4,1,248,12,2,2,5,1,3),_Hm2AgentSwitchIpVlanRoutingStatus_Type())
hm2AgentSwitchIpVlanRoutingStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchIpVlanRoutingStatus.setStatus(_A)
_Hm2AgentSwitchSecondaryAddressTable_Object=MibTable
hm2AgentSwitchSecondaryAddressTable=_Hm2AgentSwitchSecondaryAddressTable_Object((1,3,6,1,4,1,248,12,2,2,6))
if mibBuilder.loadTexts:hm2AgentSwitchSecondaryAddressTable.setStatus(_A)
_Hm2AgentSwitchSecondaryAddressEntry_Object=MibTableRow
hm2AgentSwitchSecondaryAddressEntry=_Hm2AgentSwitchSecondaryAddressEntry_Object((1,3,6,1,4,1,248,12,2,2,6,1))
hm2AgentSwitchSecondaryAddressEntry.setIndexNames((0,_E,_U),(0,_E,_g))
if mibBuilder.loadTexts:hm2AgentSwitchSecondaryAddressEntry.setStatus(_A)
_Hm2AgentSwitchSecondaryIpAddress_Type=IpAddress
_Hm2AgentSwitchSecondaryIpAddress_Object=MibTableColumn
hm2AgentSwitchSecondaryIpAddress=_Hm2AgentSwitchSecondaryIpAddress_Object((1,3,6,1,4,1,248,12,2,2,6,1,1),_Hm2AgentSwitchSecondaryIpAddress_Type())
hm2AgentSwitchSecondaryIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentSwitchSecondaryIpAddress.setStatus(_A)
_Hm2AgentSwitchSecondaryNetMask_Type=IpAddress
_Hm2AgentSwitchSecondaryNetMask_Object=MibTableColumn
hm2AgentSwitchSecondaryNetMask=_Hm2AgentSwitchSecondaryNetMask_Object((1,3,6,1,4,1,248,12,2,2,6,1,2),_Hm2AgentSwitchSecondaryNetMask_Type())
hm2AgentSwitchSecondaryNetMask.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchSecondaryNetMask.setStatus(_A)
_Hm2AgentSwitchSecondaryStatus_Type=RowStatus
_Hm2AgentSwitchSecondaryStatus_Object=MibTableColumn
hm2AgentSwitchSecondaryStatus=_Hm2AgentSwitchSecondaryStatus_Object((1,3,6,1,4,1,248,12,2,2,6,1,3),_Hm2AgentSwitchSecondaryStatus_Type())
hm2AgentSwitchSecondaryStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchSecondaryStatus.setStatus(_A)
_Hm2AgentSwitchIpIcmpControlGroup_ObjectIdentity=ObjectIdentity
hm2AgentSwitchIpIcmpControlGroup=_Hm2AgentSwitchIpIcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,2,8))
class _Hm2AgentSwitchIpIcmpEchoReplyMode_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentSwitchIpIcmpEchoReplyMode_Type.__name__=_F
_Hm2AgentSwitchIpIcmpEchoReplyMode_Object=MibScalar
hm2AgentSwitchIpIcmpEchoReplyMode=_Hm2AgentSwitchIpIcmpEchoReplyMode_Object((1,3,6,1,4,1,248,12,2,2,8,1),_Hm2AgentSwitchIpIcmpEchoReplyMode_Type())
hm2AgentSwitchIpIcmpEchoReplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpIcmpEchoReplyMode.setStatus(_A)
class _Hm2AgentSwitchIpIcmpRedirectsMode_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentSwitchIpIcmpRedirectsMode_Type.__name__=_F
_Hm2AgentSwitchIpIcmpRedirectsMode_Object=MibScalar
hm2AgentSwitchIpIcmpRedirectsMode=_Hm2AgentSwitchIpIcmpRedirectsMode_Object((1,3,6,1,4,1,248,12,2,2,8,2),_Hm2AgentSwitchIpIcmpRedirectsMode_Type())
hm2AgentSwitchIpIcmpRedirectsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpIcmpRedirectsMode.setStatus(_A)
class _Hm2AgentSwitchIpIcmpRateLimitInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Hm2AgentSwitchIpIcmpRateLimitInterval_Type.__name__=_D
_Hm2AgentSwitchIpIcmpRateLimitInterval_Object=MibScalar
hm2AgentSwitchIpIcmpRateLimitInterval=_Hm2AgentSwitchIpIcmpRateLimitInterval_Object((1,3,6,1,4,1,248,12,2,2,8,3),_Hm2AgentSwitchIpIcmpRateLimitInterval_Type())
hm2AgentSwitchIpIcmpRateLimitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpIcmpRateLimitInterval.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentSwitchIpIcmpRateLimitInterval.setUnits(_K)
class _Hm2AgentSwitchIpIcmpRateLimitBurstSize_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_Hm2AgentSwitchIpIcmpRateLimitBurstSize_Type.__name__=_D
_Hm2AgentSwitchIpIcmpRateLimitBurstSize_Object=MibScalar
hm2AgentSwitchIpIcmpRateLimitBurstSize=_Hm2AgentSwitchIpIcmpRateLimitBurstSize_Object((1,3,6,1,4,1,248,12,2,2,8,4),_Hm2AgentSwitchIpIcmpRateLimitBurstSize_Type())
hm2AgentSwitchIpIcmpRateLimitBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpIcmpRateLimitBurstSize.setStatus(_A)
_Hm2AgentSwitchIntfIpHelperAddressTable_Object=MibTable
hm2AgentSwitchIntfIpHelperAddressTable=_Hm2AgentSwitchIntfIpHelperAddressTable_Object((1,3,6,1,4,1,248,12,2,2,10))
if mibBuilder.loadTexts:hm2AgentSwitchIntfIpHelperAddressTable.setStatus(_A)
_Hm2AgentSwitchIntfIpHelperAddressEntry_Object=MibTableRow
hm2AgentSwitchIntfIpHelperAddressEntry=_Hm2AgentSwitchIntfIpHelperAddressEntry_Object((1,3,6,1,4,1,248,12,2,2,10,1))
hm2AgentSwitchIntfIpHelperAddressEntry.setIndexNames((0,_E,_U),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:hm2AgentSwitchIntfIpHelperAddressEntry.setStatus(_A)
class _Hm2AgentSwitchIntfIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentSwitchIntfIpHelperUdpPort_Type.__name__=_I
_Hm2AgentSwitchIntfIpHelperUdpPort_Object=MibTableColumn
hm2AgentSwitchIntfIpHelperUdpPort=_Hm2AgentSwitchIntfIpHelperUdpPort_Object((1,3,6,1,4,1,248,12,2,2,10,1,1),_Hm2AgentSwitchIntfIpHelperUdpPort_Type())
hm2AgentSwitchIntfIpHelperUdpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentSwitchIntfIpHelperUdpPort.setStatus(_A)
_Hm2AgentSwitchIntfIpHelperIpAddress_Type=IpAddress
_Hm2AgentSwitchIntfIpHelperIpAddress_Object=MibTableColumn
hm2AgentSwitchIntfIpHelperIpAddress=_Hm2AgentSwitchIntfIpHelperIpAddress_Object((1,3,6,1,4,1,248,12,2,2,10,1,2),_Hm2AgentSwitchIntfIpHelperIpAddress_Type())
hm2AgentSwitchIntfIpHelperIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentSwitchIntfIpHelperIpAddress.setStatus(_A)
_Hm2AgentSwitchIntfIpHelperHitCount_Type=Unsigned32
_Hm2AgentSwitchIntfIpHelperHitCount_Object=MibTableColumn
hm2AgentSwitchIntfIpHelperHitCount=_Hm2AgentSwitchIntfIpHelperHitCount_Object((1,3,6,1,4,1,248,12,2,2,10,1,4),_Hm2AgentSwitchIntfIpHelperHitCount_Type())
hm2AgentSwitchIntfIpHelperHitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIntfIpHelperHitCount.setStatus(_A)
_Hm2AgentSwitchIntfIpHelperStatus_Type=RowStatus
_Hm2AgentSwitchIntfIpHelperStatus_Object=MibTableColumn
hm2AgentSwitchIntfIpHelperStatus=_Hm2AgentSwitchIntfIpHelperStatus_Object((1,3,6,1,4,1,248,12,2,2,10,1,5),_Hm2AgentSwitchIntfIpHelperStatus_Type())
hm2AgentSwitchIntfIpHelperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchIntfIpHelperStatus.setStatus(_A)
class _Hm2AgentSwitchClearIpDefaultGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_Hm2AgentSwitchClearIpDefaultGateway_Type.__name__=_D
_Hm2AgentSwitchClearIpDefaultGateway_Object=MibScalar
hm2AgentSwitchClearIpDefaultGateway=_Hm2AgentSwitchClearIpDefaultGateway_Object((1,3,6,1,4,1,248,12,2,2,11),_Hm2AgentSwitchClearIpDefaultGateway_Type())
hm2AgentSwitchClearIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchClearIpDefaultGateway.setStatus(_A)
_Hm2AgentSwitchIpFirstActiveAddressType_Type=InetAddressType
_Hm2AgentSwitchIpFirstActiveAddressType_Object=MibScalar
hm2AgentSwitchIpFirstActiveAddressType=_Hm2AgentSwitchIpFirstActiveAddressType_Object((1,3,6,1,4,1,248,12,2,2,248),_Hm2AgentSwitchIpFirstActiveAddressType_Type())
hm2AgentSwitchIpFirstActiveAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpFirstActiveAddressType.setStatus(_A)
class _Hm2AgentSwitchIpFirstActiveAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_Hm2AgentSwitchIpFirstActiveAddress_Type.__name__=_R
_Hm2AgentSwitchIpFirstActiveAddress_Object=MibScalar
hm2AgentSwitchIpFirstActiveAddress=_Hm2AgentSwitchIpFirstActiveAddress_Object((1,3,6,1,4,1,248,12,2,2,249),_Hm2AgentSwitchIpFirstActiveAddress_Type())
hm2AgentSwitchIpFirstActiveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpFirstActiveAddress.setStatus(_A)
class _Hm2AgentSwitchIpStaticDefaultPref_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentSwitchIpStaticDefaultPref_Type.__name__=_D
_Hm2AgentSwitchIpStaticDefaultPref_Object=MibScalar
hm2AgentSwitchIpStaticDefaultPref=_Hm2AgentSwitchIpStaticDefaultPref_Object((1,3,6,1,4,1,248,12,2,2,250),_Hm2AgentSwitchIpStaticDefaultPref_Type())
hm2AgentSwitchIpStaticDefaultPref.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpStaticDefaultPref.setStatus(_A)
_Hm2AgentSwitchIpRouteCount_Type=Unsigned32
_Hm2AgentSwitchIpRouteCount_Object=MibScalar
hm2AgentSwitchIpRouteCount=_Hm2AgentSwitchIpRouteCount_Object((1,3,6,1,4,1,248,12,2,2,251),_Hm2AgentSwitchIpRouteCount_Type())
hm2AgentSwitchIpRouteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpRouteCount.setStatus(_A)
_Hm2AgentSwitchIpBestRouteCount_Type=Unsigned32
_Hm2AgentSwitchIpBestRouteCount_Object=MibScalar
hm2AgentSwitchIpBestRouteCount=_Hm2AgentSwitchIpBestRouteCount_Object((1,3,6,1,4,1,248,12,2,2,252),_Hm2AgentSwitchIpBestRouteCount_Type())
hm2AgentSwitchIpBestRouteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpBestRouteCount.setStatus(_A)
class _Hm2AgentSwitchIpSourceRoutingMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSwitchIpSourceRoutingMode_Type.__name__=_F
_Hm2AgentSwitchIpSourceRoutingMode_Object=MibScalar
hm2AgentSwitchIpSourceRoutingMode=_Hm2AgentSwitchIpSourceRoutingMode_Object((1,3,6,1,4,1,248,12,2,2,253),_Hm2AgentSwitchIpSourceRoutingMode_Type())
hm2AgentSwitchIpSourceRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpSourceRoutingMode.setStatus(_A)
_Hm2AgentRouterRipConfigGroup_ObjectIdentity=ObjectIdentity
hm2AgentRouterRipConfigGroup=_Hm2AgentRouterRipConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,3))
class _Hm2AgentRouterRipAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentRouterRipAdminState_Type.__name__=_F
_Hm2AgentRouterRipAdminState_Object=MibScalar
hm2AgentRouterRipAdminState=_Hm2AgentRouterRipAdminState_Object((1,3,6,1,4,1,248,12,2,3,1),_Hm2AgentRouterRipAdminState_Type())
hm2AgentRouterRipAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipAdminState.setStatus(_A)
class _Hm2AgentRouterRipSplitHorizonMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('simple',2),('poisonReverse',3)))
_Hm2AgentRouterRipSplitHorizonMode_Type.__name__=_D
_Hm2AgentRouterRipSplitHorizonMode_Object=MibScalar
hm2AgentRouterRipSplitHorizonMode=_Hm2AgentRouterRipSplitHorizonMode_Object((1,3,6,1,4,1,248,12,2,3,2),_Hm2AgentRouterRipSplitHorizonMode_Type())
hm2AgentRouterRipSplitHorizonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipSplitHorizonMode.setStatus(_A)
class _Hm2AgentRouterRipAutoSummaryMode_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentRouterRipAutoSummaryMode_Type.__name__=_F
_Hm2AgentRouterRipAutoSummaryMode_Object=MibScalar
hm2AgentRouterRipAutoSummaryMode=_Hm2AgentRouterRipAutoSummaryMode_Object((1,3,6,1,4,1,248,12,2,3,3),_Hm2AgentRouterRipAutoSummaryMode_Type())
hm2AgentRouterRipAutoSummaryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipAutoSummaryMode.setStatus(_A)
class _Hm2AgentRouterRipHostRoutesAcceptMode_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentRouterRipHostRoutesAcceptMode_Type.__name__=_F
_Hm2AgentRouterRipHostRoutesAcceptMode_Object=MibScalar
hm2AgentRouterRipHostRoutesAcceptMode=_Hm2AgentRouterRipHostRoutesAcceptMode_Object((1,3,6,1,4,1,248,12,2,3,4),_Hm2AgentRouterRipHostRoutesAcceptMode_Type())
hm2AgentRouterRipHostRoutesAcceptMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipHostRoutesAcceptMode.setStatus(_A)
class _Hm2AgentRouterRipDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_Hm2AgentRouterRipDefaultMetric_Type.__name__=_D
_Hm2AgentRouterRipDefaultMetric_Object=MibScalar
hm2AgentRouterRipDefaultMetric=_Hm2AgentRouterRipDefaultMetric_Object((1,3,6,1,4,1,248,12,2,3,5),_Hm2AgentRouterRipDefaultMetric_Type())
hm2AgentRouterRipDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipDefaultMetric.setStatus(_A)
class _Hm2AgentRouterRipDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_Hm2AgentRouterRipDefaultMetricConfigured_Type.__name__=_J
_Hm2AgentRouterRipDefaultMetricConfigured_Object=MibScalar
hm2AgentRouterRipDefaultMetricConfigured=_Hm2AgentRouterRipDefaultMetricConfigured_Object((1,3,6,1,4,1,248,12,2,3,6),_Hm2AgentRouterRipDefaultMetricConfigured_Type())
hm2AgentRouterRipDefaultMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipDefaultMetricConfigured.setStatus(_A)
class _Hm2AgentRouterRipDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_Hm2AgentRouterRipDefaultInfoOriginate_Type.__name__=_J
_Hm2AgentRouterRipDefaultInfoOriginate_Object=MibScalar
hm2AgentRouterRipDefaultInfoOriginate=_Hm2AgentRouterRipDefaultInfoOriginate_Object((1,3,6,1,4,1,248,12,2,3,7),_Hm2AgentRouterRipDefaultInfoOriginate_Type())
hm2AgentRouterRipDefaultInfoOriginate.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipDefaultInfoOriginate.setStatus(_A)
_Hm2AgentRipRouteRedistTable_Object=MibTable
hm2AgentRipRouteRedistTable=_Hm2AgentRipRouteRedistTable_Object((1,3,6,1,4,1,248,12,2,3,8))
if mibBuilder.loadTexts:hm2AgentRipRouteRedistTable.setStatus(_A)
_Hm2AgentRipRouteRedistEntry_Object=MibTableRow
hm2AgentRipRouteRedistEntry=_Hm2AgentRipRouteRedistEntry_Object((1,3,6,1,4,1,248,12,2,3,8,1))
hm2AgentRipRouteRedistEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:hm2AgentRipRouteRedistEntry.setStatus(_A)
class _Hm2AgentRipRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_k,1),(_T,2),('ospf',3),('bgp',4)))
_Hm2AgentRipRouteRedistSource_Type.__name__=_D
_Hm2AgentRipRouteRedistSource_Object=MibTableColumn
hm2AgentRipRouteRedistSource=_Hm2AgentRipRouteRedistSource_Object((1,3,6,1,4,1,248,12,2,3,8,1,1),_Hm2AgentRipRouteRedistSource_Type())
hm2AgentRipRouteRedistSource.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistSource.setStatus(_A)
class _Hm2AgentRipRouteRedistMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentRipRouteRedistMode_Type.__name__=_F
_Hm2AgentRipRouteRedistMode_Object=MibTableColumn
hm2AgentRipRouteRedistMode=_Hm2AgentRipRouteRedistMode_Object((1,3,6,1,4,1,248,12,2,3,8,1,2),_Hm2AgentRipRouteRedistMode_Type())
hm2AgentRipRouteRedistMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMode.setStatus(_A)
class _Hm2AgentRipRouteRedistMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_Hm2AgentRipRouteRedistMetric_Type.__name__=_D
_Hm2AgentRipRouteRedistMetric_Object=MibTableColumn
hm2AgentRipRouteRedistMetric=_Hm2AgentRipRouteRedistMetric_Object((1,3,6,1,4,1,248,12,2,3,8,1,3),_Hm2AgentRipRouteRedistMetric_Type())
hm2AgentRipRouteRedistMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMetric.setStatus(_A)
class _Hm2AgentRipRouteRedistMetricConfigured_Type(TruthValue):defaultValue=2
_Hm2AgentRipRouteRedistMetricConfigured_Type.__name__=_J
_Hm2AgentRipRouteRedistMetricConfigured_Object=MibTableColumn
hm2AgentRipRouteRedistMetricConfigured=_Hm2AgentRipRouteRedistMetricConfigured_Object((1,3,6,1,4,1,248,12,2,3,8,1,4),_Hm2AgentRipRouteRedistMetricConfigured_Type())
hm2AgentRipRouteRedistMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMetricConfigured.setStatus(_A)
class _Hm2AgentRipRouteRedistMatchInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_Hm2AgentRipRouteRedistMatchInternal_Type.__name__=_D
_Hm2AgentRipRouteRedistMatchInternal_Object=MibTableColumn
hm2AgentRipRouteRedistMatchInternal=_Hm2AgentRipRouteRedistMatchInternal_Object((1,3,6,1,4,1,248,12,2,3,8,1,5),_Hm2AgentRipRouteRedistMatchInternal_Type())
hm2AgentRipRouteRedistMatchInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMatchInternal.setStatus(_A)
class _Hm2AgentRipRouteRedistMatchExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_Hm2AgentRipRouteRedistMatchExternal1_Type.__name__=_D
_Hm2AgentRipRouteRedistMatchExternal1_Object=MibTableColumn
hm2AgentRipRouteRedistMatchExternal1=_Hm2AgentRipRouteRedistMatchExternal1_Object((1,3,6,1,4,1,248,12,2,3,8,1,6),_Hm2AgentRipRouteRedistMatchExternal1_Type())
hm2AgentRipRouteRedistMatchExternal1.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMatchExternal1.setStatus(_A)
class _Hm2AgentRipRouteRedistMatchExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_Hm2AgentRipRouteRedistMatchExternal2_Type.__name__=_D
_Hm2AgentRipRouteRedistMatchExternal2_Object=MibTableColumn
hm2AgentRipRouteRedistMatchExternal2=_Hm2AgentRipRouteRedistMatchExternal2_Object((1,3,6,1,4,1,248,12,2,3,8,1,7),_Hm2AgentRipRouteRedistMatchExternal2_Type())
hm2AgentRipRouteRedistMatchExternal2.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMatchExternal2.setStatus(_A)
class _Hm2AgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_Hm2AgentRipRouteRedistMatchNSSAExternal1_Type.__name__=_D
_Hm2AgentRipRouteRedistMatchNSSAExternal1_Object=MibTableColumn
hm2AgentRipRouteRedistMatchNSSAExternal1=_Hm2AgentRipRouteRedistMatchNSSAExternal1_Object((1,3,6,1,4,1,248,12,2,3,8,1,8),_Hm2AgentRipRouteRedistMatchNSSAExternal1_Type())
hm2AgentRipRouteRedistMatchNSSAExternal1.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMatchNSSAExternal1.setStatus(_A)
class _Hm2AgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_Hm2AgentRipRouteRedistMatchNSSAExternal2_Type.__name__=_D
_Hm2AgentRipRouteRedistMatchNSSAExternal2_Object=MibTableColumn
hm2AgentRipRouteRedistMatchNSSAExternal2=_Hm2AgentRipRouteRedistMatchNSSAExternal2_Object((1,3,6,1,4,1,248,12,2,3,8,1,9),_Hm2AgentRipRouteRedistMatchNSSAExternal2_Type())
hm2AgentRipRouteRedistMatchNSSAExternal2.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistMatchNSSAExternal2.setStatus(_A)
class _Hm2AgentRipRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1000,1099))
_Hm2AgentRipRouteRedistDistList_Type.__name__=_I
_Hm2AgentRipRouteRedistDistList_Object=MibTableColumn
hm2AgentRipRouteRedistDistList=_Hm2AgentRipRouteRedistDistList_Object((1,3,6,1,4,1,248,12,2,3,8,1,10),_Hm2AgentRipRouteRedistDistList_Type())
hm2AgentRipRouteRedistDistList.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistDistList.setStatus(_A)
_Hm2AgentRipRouteRedistDistListConfigured_Type=TruthValue
_Hm2AgentRipRouteRedistDistListConfigured_Object=MibTableColumn
hm2AgentRipRouteRedistDistListConfigured=_Hm2AgentRipRouteRedistDistListConfigured_Object((1,3,6,1,4,1,248,12,2,3,8,1,11),_Hm2AgentRipRouteRedistDistListConfigured_Type())
hm2AgentRipRouteRedistDistListConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRipRouteRedistDistListConfigured.setStatus(_A)
_Hm2AgentRip2IfConfTable_Object=MibTable
hm2AgentRip2IfConfTable=_Hm2AgentRip2IfConfTable_Object((1,3,6,1,4,1,248,12,2,3,9))
if mibBuilder.loadTexts:hm2AgentRip2IfConfTable.setStatus(_A)
_Hm2AgentRip2IfConfEntry_Object=MibTableRow
hm2AgentRip2IfConfEntry=_Hm2AgentRip2IfConfEntry_Object((1,3,6,1,4,1,248,12,2,3,9,1))
if mibBuilder.loadTexts:hm2AgentRip2IfConfEntry.setStatus(_A)
class _Hm2AgentRip2IfConfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentRip2IfConfAuthKeyId_Type.__name__=_D
_Hm2AgentRip2IfConfAuthKeyId_Object=MibTableColumn
hm2AgentRip2IfConfAuthKeyId=_Hm2AgentRip2IfConfAuthKeyId_Object((1,3,6,1,4,1,248,12,2,3,9,1,1),_Hm2AgentRip2IfConfAuthKeyId_Type())
hm2AgentRip2IfConfAuthKeyId.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentRip2IfConfAuthKeyId.setStatus(_A)
class _Hm2AgentRouterRipRoutePref_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentRouterRipRoutePref_Type.__name__=_D
_Hm2AgentRouterRipRoutePref_Object=MibScalar
hm2AgentRouterRipRoutePref=_Hm2AgentRouterRipRoutePref_Object((1,3,6,1,4,1,248,12,2,3,10),_Hm2AgentRouterRipRoutePref_Type())
hm2AgentRouterRipRoutePref.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipRoutePref.setStatus(_A)
class _Hm2AgentRouterRipUpdateTimerInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Hm2AgentRouterRipUpdateTimerInterval_Type.__name__=_D
_Hm2AgentRouterRipUpdateTimerInterval_Object=MibScalar
hm2AgentRouterRipUpdateTimerInterval=_Hm2AgentRouterRipUpdateTimerInterval_Object((1,3,6,1,4,1,248,12,2,3,248),_Hm2AgentRouterRipUpdateTimerInterval_Type())
hm2AgentRouterRipUpdateTimerInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterRipUpdateTimerInterval.setStatus(_A)
_Hm2AgentRouterOspfConfigGroup_ObjectIdentity=ObjectIdentity
hm2AgentRouterOspfConfigGroup=_Hm2AgentRouterOspfConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,4))
class _Hm2AgentOspfDefaultMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_Hm2AgentOspfDefaultMetric_Type.__name__=_D
_Hm2AgentOspfDefaultMetric_Object=MibScalar
hm2AgentOspfDefaultMetric=_Hm2AgentOspfDefaultMetric_Object((1,3,6,1,4,1,248,12,2,4,1),_Hm2AgentOspfDefaultMetric_Type())
hm2AgentOspfDefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultMetric.setStatus(_A)
class _Hm2AgentOspfDefaultMetricConfigured_Type(TruthValue):defaultValue=2
_Hm2AgentOspfDefaultMetricConfigured_Type.__name__=_J
_Hm2AgentOspfDefaultMetricConfigured_Object=MibScalar
hm2AgentOspfDefaultMetricConfigured=_Hm2AgentOspfDefaultMetricConfigured_Object((1,3,6,1,4,1,248,12,2,4,2),_Hm2AgentOspfDefaultMetricConfigured_Type())
hm2AgentOspfDefaultMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultMetricConfigured.setStatus(_A)
class _Hm2AgentOspfDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_Hm2AgentOspfDefaultInfoOriginate_Type.__name__=_J
_Hm2AgentOspfDefaultInfoOriginate_Object=MibScalar
hm2AgentOspfDefaultInfoOriginate=_Hm2AgentOspfDefaultInfoOriginate_Object((1,3,6,1,4,1,248,12,2,4,3),_Hm2AgentOspfDefaultInfoOriginate_Type())
hm2AgentOspfDefaultInfoOriginate.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultInfoOriginate.setStatus(_A)
class _Hm2AgentOspfDefaultInfoOriginateAlways_Type(TruthValue):defaultValue=2
_Hm2AgentOspfDefaultInfoOriginateAlways_Type.__name__=_J
_Hm2AgentOspfDefaultInfoOriginateAlways_Object=MibScalar
hm2AgentOspfDefaultInfoOriginateAlways=_Hm2AgentOspfDefaultInfoOriginateAlways_Object((1,3,6,1,4,1,248,12,2,4,4),_Hm2AgentOspfDefaultInfoOriginateAlways_Type())
hm2AgentOspfDefaultInfoOriginateAlways.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultInfoOriginateAlways.setStatus(_A)
class _Hm2AgentOspfDefaultInfoOriginateMetric_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16777214))
_Hm2AgentOspfDefaultInfoOriginateMetric_Type.__name__=_D
_Hm2AgentOspfDefaultInfoOriginateMetric_Object=MibScalar
hm2AgentOspfDefaultInfoOriginateMetric=_Hm2AgentOspfDefaultInfoOriginateMetric_Object((1,3,6,1,4,1,248,12,2,4,5),_Hm2AgentOspfDefaultInfoOriginateMetric_Type())
hm2AgentOspfDefaultInfoOriginateMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultInfoOriginateMetric.setStatus(_A)
_Hm2AgentOspfDefaultInfoOriginateMetricConfigured_Type=TruthValue
_Hm2AgentOspfDefaultInfoOriginateMetricConfigured_Object=MibScalar
hm2AgentOspfDefaultInfoOriginateMetricConfigured=_Hm2AgentOspfDefaultInfoOriginateMetricConfigured_Object((1,3,6,1,4,1,248,12,2,4,6),_Hm2AgentOspfDefaultInfoOriginateMetricConfigured_Type())
hm2AgentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultInfoOriginateMetricConfigured.setStatus(_A)
class _Hm2AgentOspfDefaultInfoOriginateMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_Hm2AgentOspfDefaultInfoOriginateMetricType_Type.__name__=_D
_Hm2AgentOspfDefaultInfoOriginateMetricType_Object=MibScalar
hm2AgentOspfDefaultInfoOriginateMetricType=_Hm2AgentOspfDefaultInfoOriginateMetricType_Object((1,3,6,1,4,1,248,12,2,4,7),_Hm2AgentOspfDefaultInfoOriginateMetricType_Type())
hm2AgentOspfDefaultInfoOriginateMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultInfoOriginateMetricType.setStatus(_A)
_Hm2AgentOspfRouteRedistTable_Object=MibTable
hm2AgentOspfRouteRedistTable=_Hm2AgentOspfRouteRedistTable_Object((1,3,6,1,4,1,248,12,2,4,8))
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistTable.setStatus(_A)
_Hm2AgentOspfRouteRedistEntry_Object=MibTableRow
hm2AgentOspfRouteRedistEntry=_Hm2AgentOspfRouteRedistEntry_Object((1,3,6,1,4,1,248,12,2,4,8,1))
hm2AgentOspfRouteRedistEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistEntry.setStatus(_A)
class _Hm2AgentOspfRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_k,1),(_T,2),('rip',3),('bgp',4)))
_Hm2AgentOspfRouteRedistSource_Type.__name__=_D
_Hm2AgentOspfRouteRedistSource_Object=MibTableColumn
hm2AgentOspfRouteRedistSource=_Hm2AgentOspfRouteRedistSource_Object((1,3,6,1,4,1,248,12,2,4,8,1,1),_Hm2AgentOspfRouteRedistSource_Type())
hm2AgentOspfRouteRedistSource.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistSource.setStatus(_A)
class _Hm2AgentOspfRouteRedistMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentOspfRouteRedistMode_Type.__name__=_F
_Hm2AgentOspfRouteRedistMode_Object=MibTableColumn
hm2AgentOspfRouteRedistMode=_Hm2AgentOspfRouteRedistMode_Object((1,3,6,1,4,1,248,12,2,4,8,1,2),_Hm2AgentOspfRouteRedistMode_Type())
hm2AgentOspfRouteRedistMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistMode.setStatus(_A)
class _Hm2AgentOspfRouteRedistMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_Hm2AgentOspfRouteRedistMetric_Type.__name__=_D
_Hm2AgentOspfRouteRedistMetric_Object=MibTableColumn
hm2AgentOspfRouteRedistMetric=_Hm2AgentOspfRouteRedistMetric_Object((1,3,6,1,4,1,248,12,2,4,8,1,3),_Hm2AgentOspfRouteRedistMetric_Type())
hm2AgentOspfRouteRedistMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistMetric.setStatus(_A)
_Hm2AgentOspfRouteRedistMetricConfigured_Type=TruthValue
_Hm2AgentOspfRouteRedistMetricConfigured_Object=MibTableColumn
hm2AgentOspfRouteRedistMetricConfigured=_Hm2AgentOspfRouteRedistMetricConfigured_Object((1,3,6,1,4,1,248,12,2,4,8,1,4),_Hm2AgentOspfRouteRedistMetricConfigured_Type())
hm2AgentOspfRouteRedistMetricConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistMetricConfigured.setStatus(_A)
class _Hm2AgentOspfRouteRedistMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_Hm2AgentOspfRouteRedistMetricType_Type.__name__=_D
_Hm2AgentOspfRouteRedistMetricType_Object=MibTableColumn
hm2AgentOspfRouteRedistMetricType=_Hm2AgentOspfRouteRedistMetricType_Object((1,3,6,1,4,1,248,12,2,4,8,1,5),_Hm2AgentOspfRouteRedistMetricType_Type())
hm2AgentOspfRouteRedistMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistMetricType.setStatus(_A)
_Hm2AgentOspfRouteRedistTag_Type=Unsigned32
_Hm2AgentOspfRouteRedistTag_Object=MibTableColumn
hm2AgentOspfRouteRedistTag=_Hm2AgentOspfRouteRedistTag_Object((1,3,6,1,4,1,248,12,2,4,8,1,6),_Hm2AgentOspfRouteRedistTag_Type())
hm2AgentOspfRouteRedistTag.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistTag.setStatus(_A)
class _Hm2AgentOspfRouteRedistSubnets_Type(TruthValue):defaultValue=1
_Hm2AgentOspfRouteRedistSubnets_Type.__name__=_J
_Hm2AgentOspfRouteRedistSubnets_Object=MibTableColumn
hm2AgentOspfRouteRedistSubnets=_Hm2AgentOspfRouteRedistSubnets_Object((1,3,6,1,4,1,248,12,2,4,8,1,7),_Hm2AgentOspfRouteRedistSubnets_Type())
hm2AgentOspfRouteRedistSubnets.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistSubnets.setStatus(_A)
class _Hm2AgentOspfRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10000))
_Hm2AgentOspfRouteRedistDistList_Type.__name__=_I
_Hm2AgentOspfRouteRedistDistList_Object=MibTableColumn
hm2AgentOspfRouteRedistDistList=_Hm2AgentOspfRouteRedistDistList_Object((1,3,6,1,4,1,248,12,2,4,8,1,8),_Hm2AgentOspfRouteRedistDistList_Type())
hm2AgentOspfRouteRedistDistList.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistDistList.setStatus(_A)
_Hm2AgentOspfRouteRedistDistListConfigured_Type=TruthValue
_Hm2AgentOspfRouteRedistDistListConfigured_Object=MibTableColumn
hm2AgentOspfRouteRedistDistListConfigured=_Hm2AgentOspfRouteRedistDistListConfigured_Object((1,3,6,1,4,1,248,12,2,4,8,1,9),_Hm2AgentOspfRouteRedistDistListConfigured_Type())
hm2AgentOspfRouteRedistDistListConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRouteRedistDistListConfigured.setStatus(_A)
_Hm2AgentOspfIfTable_Object=MibTable
hm2AgentOspfIfTable=_Hm2AgentOspfIfTable_Object((1,3,6,1,4,1,248,12,2,4,9))
if mibBuilder.loadTexts:hm2AgentOspfIfTable.setStatus(_A)
_Hm2AgentOspfIfEntry_Object=MibTableRow
hm2AgentOspfIfEntry=_Hm2AgentOspfIfEntry_Object((1,3,6,1,4,1,248,12,2,4,9,1))
if mibBuilder.loadTexts:hm2AgentOspfIfEntry.setStatus(_A)
class _Hm2AgentOspfIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentOspfIfAuthKeyId_Type.__name__=_D
_Hm2AgentOspfIfAuthKeyId_Object=MibTableColumn
hm2AgentOspfIfAuthKeyId=_Hm2AgentOspfIfAuthKeyId_Object((1,3,6,1,4,1,248,12,2,4,9,1,1),_Hm2AgentOspfIfAuthKeyId_Type())
hm2AgentOspfIfAuthKeyId.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentOspfIfAuthKeyId.setStatus(_A)
_Hm2AgentOspfIfIpMtuIgnoreFlag_Type=HmEnabledStatus
_Hm2AgentOspfIfIpMtuIgnoreFlag_Object=MibTableColumn
hm2AgentOspfIfIpMtuIgnoreFlag=_Hm2AgentOspfIfIpMtuIgnoreFlag_Object((1,3,6,1,4,1,248,12,2,4,9,1,2),_Hm2AgentOspfIfIpMtuIgnoreFlag_Type())
hm2AgentOspfIfIpMtuIgnoreFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfIfIpMtuIgnoreFlag.setStatus(_A)
class _Hm2AgentOspfIfPassiveMode_Type(TruthValue):defaultValue=2
_Hm2AgentOspfIfPassiveMode_Type.__name__=_J
_Hm2AgentOspfIfPassiveMode_Object=MibTableColumn
hm2AgentOspfIfPassiveMode=_Hm2AgentOspfIfPassiveMode_Object((1,3,6,1,4,1,248,12,2,4,9,1,3),_Hm2AgentOspfIfPassiveMode_Type())
hm2AgentOspfIfPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfIfPassiveMode.setStatus(_A)
_Hm2AgentOspfIfAdvertiseSecondaries_Type=HmEnabledStatus
_Hm2AgentOspfIfAdvertiseSecondaries_Object=MibTableColumn
hm2AgentOspfIfAdvertiseSecondaries=_Hm2AgentOspfIfAdvertiseSecondaries_Object((1,3,6,1,4,1,248,12,2,4,9,1,4),_Hm2AgentOspfIfAdvertiseSecondaries_Type())
hm2AgentOspfIfAdvertiseSecondaries.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfIfAdvertiseSecondaries.setStatus(_A)
class _Hm2AgentOspfIfFastHelloMode_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentOspfIfFastHelloMode_Type.__name__=_F
_Hm2AgentOspfIfFastHelloMode_Object=MibTableColumn
hm2AgentOspfIfFastHelloMode=_Hm2AgentOspfIfFastHelloMode_Object((1,3,6,1,4,1,248,12,2,4,9,1,248),_Hm2AgentOspfIfFastHelloMode_Type())
hm2AgentOspfIfFastHelloMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfIfFastHelloMode.setStatus(_A)
_Hm2AgentOspfVirtIfTable_Object=MibTable
hm2AgentOspfVirtIfTable=_Hm2AgentOspfVirtIfTable_Object((1,3,6,1,4,1,248,12,2,4,10))
if mibBuilder.loadTexts:hm2AgentOspfVirtIfTable.setStatus(_A)
_Hm2AgentOspfVirtIfEntry_Object=MibTableRow
hm2AgentOspfVirtIfEntry=_Hm2AgentOspfVirtIfEntry_Object((1,3,6,1,4,1,248,12,2,4,10,1))
if mibBuilder.loadTexts:hm2AgentOspfVirtIfEntry.setStatus(_A)
class _Hm2AgentOspfVirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentOspfVirtIfAuthKeyId_Type.__name__=_D
_Hm2AgentOspfVirtIfAuthKeyId_Object=MibTableColumn
hm2AgentOspfVirtIfAuthKeyId=_Hm2AgentOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,248,12,2,4,10,1,1),_Hm2AgentOspfVirtIfAuthKeyId_Type())
hm2AgentOspfVirtIfAuthKeyId.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentOspfVirtIfAuthKeyId.setStatus(_A)
class _Hm2AgentRouterOspfRFC1583CompatibilityMode_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentRouterOspfRFC1583CompatibilityMode_Type.__name__=_F
_Hm2AgentRouterOspfRFC1583CompatibilityMode_Object=MibScalar
hm2AgentRouterOspfRFC1583CompatibilityMode=_Hm2AgentRouterOspfRFC1583CompatibilityMode_Object((1,3,6,1,4,1,248,12,2,4,11),_Hm2AgentRouterOspfRFC1583CompatibilityMode_Type())
hm2AgentRouterOspfRFC1583CompatibilityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterOspfRFC1583CompatibilityMode.setStatus(_A)
class _Hm2AgentOspfSpfDelayTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentOspfSpfDelayTime_Type.__name__=_D
_Hm2AgentOspfSpfDelayTime_Object=MibScalar
hm2AgentOspfSpfDelayTime=_Hm2AgentOspfSpfDelayTime_Object((1,3,6,1,4,1,248,12,2,4,12),_Hm2AgentOspfSpfDelayTime_Type())
hm2AgentOspfSpfDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfSpfDelayTime.setStatus(_A)
class _Hm2AgentOspfSpfHoldTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentOspfSpfHoldTime_Type.__name__=_D
_Hm2AgentOspfSpfHoldTime_Object=MibScalar
hm2AgentOspfSpfHoldTime=_Hm2AgentOspfSpfHoldTime_Object((1,3,6,1,4,1,248,12,2,4,13),_Hm2AgentOspfSpfHoldTime_Type())
hm2AgentOspfSpfHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfSpfHoldTime.setStatus(_A)
class _Hm2AgentOspfAutoCostRefBw_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967))
_Hm2AgentOspfAutoCostRefBw_Type.__name__=_I
_Hm2AgentOspfAutoCostRefBw_Object=MibScalar
hm2AgentOspfAutoCostRefBw=_Hm2AgentOspfAutoCostRefBw_Object((1,3,6,1,4,1,248,12,2,4,14),_Hm2AgentOspfAutoCostRefBw_Type())
hm2AgentOspfAutoCostRefBw.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfAutoCostRefBw.setStatus(_A)
_Hm2AgentOspfOpaqueLsaSupport_Type=TruthValue
_Hm2AgentOspfOpaqueLsaSupport_Object=MibScalar
hm2AgentOspfOpaqueLsaSupport=_Hm2AgentOspfOpaqueLsaSupport_Object((1,3,6,1,4,1,248,12,2,4,15),_Hm2AgentOspfOpaqueLsaSupport_Type())
hm2AgentOspfOpaqueLsaSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfOpaqueLsaSupport.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbTable_Object=MibTable
hm2AgentOspfAreaOpaqueLsdbTable=_Hm2AgentOspfAreaOpaqueLsdbTable_Object((1,3,6,1,4,1,248,12,2,4,16))
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbTable.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbEntry_Object=MibTableRow
hm2AgentOspfAreaOpaqueLsdbEntry=_Hm2AgentOspfAreaOpaqueLsdbEntry_Object((1,3,6,1,4,1,248,12,2,4,16,1))
hm2AgentOspfAreaOpaqueLsdbEntry.setIndexNames((0,_E,_o),(0,_E,_p),(0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbEntry.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbAreaId_Type=IpAddress
_Hm2AgentOspfAreaOpaqueLsdbAreaId_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbAreaId=_Hm2AgentOspfAreaOpaqueLsdbAreaId_Object((1,3,6,1,4,1,248,12,2,4,16,1,1),_Hm2AgentOspfAreaOpaqueLsdbAreaId_Type())
hm2AgentOspfAreaOpaqueLsdbAreaId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbAreaId.setStatus(_A)
class _Hm2AgentOspfAreaOpaqueLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(10));namedValues=NamedValues(('areaOpaqueLink',10))
_Hm2AgentOspfAreaOpaqueLsdbType_Type.__name__=_D
_Hm2AgentOspfAreaOpaqueLsdbType_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbType=_Hm2AgentOspfAreaOpaqueLsdbType_Object((1,3,6,1,4,1,248,12,2,4,16,1,2),_Hm2AgentOspfAreaOpaqueLsdbType_Type())
hm2AgentOspfAreaOpaqueLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbType.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbLsid_Type=IpAddress
_Hm2AgentOspfAreaOpaqueLsdbLsid_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbLsid=_Hm2AgentOspfAreaOpaqueLsdbLsid_Object((1,3,6,1,4,1,248,12,2,4,16,1,3),_Hm2AgentOspfAreaOpaqueLsdbLsid_Type())
hm2AgentOspfAreaOpaqueLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbLsid.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbRouterId_Type=RouterID
_Hm2AgentOspfAreaOpaqueLsdbRouterId_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbRouterId=_Hm2AgentOspfAreaOpaqueLsdbRouterId_Object((1,3,6,1,4,1,248,12,2,4,16,1,4),_Hm2AgentOspfAreaOpaqueLsdbRouterId_Type())
hm2AgentOspfAreaOpaqueLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbRouterId.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbSequence_Type=Integer32
_Hm2AgentOspfAreaOpaqueLsdbSequence_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbSequence=_Hm2AgentOspfAreaOpaqueLsdbSequence_Object((1,3,6,1,4,1,248,12,2,4,16,1,5),_Hm2AgentOspfAreaOpaqueLsdbSequence_Type())
hm2AgentOspfAreaOpaqueLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbSequence.setStatus(_A)
_Hm2AgentOspfAreaOpaqueLsdbAge_Type=Integer32
_Hm2AgentOspfAreaOpaqueLsdbAge_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbAge=_Hm2AgentOspfAreaOpaqueLsdbAge_Object((1,3,6,1,4,1,248,12,2,4,16,1,6),_Hm2AgentOspfAreaOpaqueLsdbAge_Type())
hm2AgentOspfAreaOpaqueLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbAge.setUnits(_V)
_Hm2AgentOspfAreaOpaqueLsdbChecksum_Type=Integer32
_Hm2AgentOspfAreaOpaqueLsdbChecksum_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbChecksum=_Hm2AgentOspfAreaOpaqueLsdbChecksum_Object((1,3,6,1,4,1,248,12,2,4,16,1,7),_Hm2AgentOspfAreaOpaqueLsdbChecksum_Type())
hm2AgentOspfAreaOpaqueLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbChecksum.setStatus(_A)
class _Hm2AgentOspfAreaOpaqueLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_Hm2AgentOspfAreaOpaqueLsdbAdvertisement_Type.__name__=_Q
_Hm2AgentOspfAreaOpaqueLsdbAdvertisement_Object=MibTableColumn
hm2AgentOspfAreaOpaqueLsdbAdvertisement=_Hm2AgentOspfAreaOpaqueLsdbAdvertisement_Object((1,3,6,1,4,1,248,12,2,4,16,1,8),_Hm2AgentOspfAreaOpaqueLsdbAdvertisement_Type())
hm2AgentOspfAreaOpaqueLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAreaOpaqueLsdbAdvertisement.setStatus(_A)
_Hm2AgentOspfLocalLsdbTable_Object=MibTable
hm2AgentOspfLocalLsdbTable=_Hm2AgentOspfLocalLsdbTable_Object((1,3,6,1,4,1,248,12,2,4,17))
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbTable.setStatus(_A)
_Hm2AgentOspfLocalLsdbEntry_Object=MibTableRow
hm2AgentOspfLocalLsdbEntry=_Hm2AgentOspfLocalLsdbEntry_Object((1,3,6,1,4,1,248,12,2,4,17,1))
hm2AgentOspfLocalLsdbEntry.setIndexNames((0,_E,_s),(0,_E,_t),(0,_E,_u),(0,_E,_v),(0,_E,_w))
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbEntry.setStatus(_A)
_Hm2AgentOspfLocalLsdbIpAddress_Type=IpAddress
_Hm2AgentOspfLocalLsdbIpAddress_Object=MibTableColumn
hm2AgentOspfLocalLsdbIpAddress=_Hm2AgentOspfLocalLsdbIpAddress_Object((1,3,6,1,4,1,248,12,2,4,17,1,1),_Hm2AgentOspfLocalLsdbIpAddress_Type())
hm2AgentOspfLocalLsdbIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbIpAddress.setStatus(_A)
_Hm2AgentOspfLocalLsdbAddressLessIf_Type=InterfaceIndexOrZero
_Hm2AgentOspfLocalLsdbAddressLessIf_Object=MibTableColumn
hm2AgentOspfLocalLsdbAddressLessIf=_Hm2AgentOspfLocalLsdbAddressLessIf_Object((1,3,6,1,4,1,248,12,2,4,17,1,2),_Hm2AgentOspfLocalLsdbAddressLessIf_Type())
hm2AgentOspfLocalLsdbAddressLessIf.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbAddressLessIf.setStatus(_A)
class _Hm2AgentOspfLocalLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(9));namedValues=NamedValues(('localOpaqueLink',9))
_Hm2AgentOspfLocalLsdbType_Type.__name__=_D
_Hm2AgentOspfLocalLsdbType_Object=MibTableColumn
hm2AgentOspfLocalLsdbType=_Hm2AgentOspfLocalLsdbType_Object((1,3,6,1,4,1,248,12,2,4,17,1,3),_Hm2AgentOspfLocalLsdbType_Type())
hm2AgentOspfLocalLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbType.setStatus(_A)
_Hm2AgentOspfLocalLsdbLsid_Type=IpAddress
_Hm2AgentOspfLocalLsdbLsid_Object=MibTableColumn
hm2AgentOspfLocalLsdbLsid=_Hm2AgentOspfLocalLsdbLsid_Object((1,3,6,1,4,1,248,12,2,4,17,1,4),_Hm2AgentOspfLocalLsdbLsid_Type())
hm2AgentOspfLocalLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbLsid.setStatus(_A)
_Hm2AgentOspfLocalLsdbRouterId_Type=RouterID
_Hm2AgentOspfLocalLsdbRouterId_Object=MibTableColumn
hm2AgentOspfLocalLsdbRouterId=_Hm2AgentOspfLocalLsdbRouterId_Object((1,3,6,1,4,1,248,12,2,4,17,1,5),_Hm2AgentOspfLocalLsdbRouterId_Type())
hm2AgentOspfLocalLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbRouterId.setStatus(_A)
_Hm2AgentOspfLocalLsdbSequence_Type=Integer32
_Hm2AgentOspfLocalLsdbSequence_Object=MibTableColumn
hm2AgentOspfLocalLsdbSequence=_Hm2AgentOspfLocalLsdbSequence_Object((1,3,6,1,4,1,248,12,2,4,17,1,6),_Hm2AgentOspfLocalLsdbSequence_Type())
hm2AgentOspfLocalLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbSequence.setStatus(_A)
_Hm2AgentOspfLocalLsdbAge_Type=Integer32
_Hm2AgentOspfLocalLsdbAge_Object=MibTableColumn
hm2AgentOspfLocalLsdbAge=_Hm2AgentOspfLocalLsdbAge_Object((1,3,6,1,4,1,248,12,2,4,17,1,7),_Hm2AgentOspfLocalLsdbAge_Type())
hm2AgentOspfLocalLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbAge.setUnits(_V)
_Hm2AgentOspfLocalLsdbChecksum_Type=Integer32
_Hm2AgentOspfLocalLsdbChecksum_Object=MibTableColumn
hm2AgentOspfLocalLsdbChecksum=_Hm2AgentOspfLocalLsdbChecksum_Object((1,3,6,1,4,1,248,12,2,4,17,1,8),_Hm2AgentOspfLocalLsdbChecksum_Type())
hm2AgentOspfLocalLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbChecksum.setStatus(_A)
class _Hm2AgentOspfLocalLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_Hm2AgentOspfLocalLsdbAdvertisement_Type.__name__=_Q
_Hm2AgentOspfLocalLsdbAdvertisement_Object=MibTableColumn
hm2AgentOspfLocalLsdbAdvertisement=_Hm2AgentOspfLocalLsdbAdvertisement_Object((1,3,6,1,4,1,248,12,2,4,17,1,9),_Hm2AgentOspfLocalLsdbAdvertisement_Type())
hm2AgentOspfLocalLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLocalLsdbAdvertisement.setStatus(_A)
_Hm2AgentOspfAsLsdbTable_Object=MibTable
hm2AgentOspfAsLsdbTable=_Hm2AgentOspfAsLsdbTable_Object((1,3,6,1,4,1,248,12,2,4,18))
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbTable.setStatus(_A)
_Hm2AgentOspfAsLsdbEntry_Object=MibTableRow
hm2AgentOspfAsLsdbEntry=_Hm2AgentOspfAsLsdbEntry_Object((1,3,6,1,4,1,248,12,2,4,18,1))
hm2AgentOspfAsLsdbEntry.setIndexNames((0,_E,_x),(0,_E,_y),(0,_E,_z))
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbEntry.setStatus(_A)
class _Hm2AgentOspfAsLsdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(11));namedValues=NamedValues(('asOpaqueLink',11))
_Hm2AgentOspfAsLsdbType_Type.__name__=_D
_Hm2AgentOspfAsLsdbType_Object=MibTableColumn
hm2AgentOspfAsLsdbType=_Hm2AgentOspfAsLsdbType_Object((1,3,6,1,4,1,248,12,2,4,18,1,1),_Hm2AgentOspfAsLsdbType_Type())
hm2AgentOspfAsLsdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbType.setStatus(_A)
_Hm2AgentOspfAsLsdbLsid_Type=IpAddress
_Hm2AgentOspfAsLsdbLsid_Object=MibTableColumn
hm2AgentOspfAsLsdbLsid=_Hm2AgentOspfAsLsdbLsid_Object((1,3,6,1,4,1,248,12,2,4,18,1,2),_Hm2AgentOspfAsLsdbLsid_Type())
hm2AgentOspfAsLsdbLsid.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbLsid.setStatus(_A)
_Hm2AgentOspfAsLsdbRouterId_Type=RouterID
_Hm2AgentOspfAsLsdbRouterId_Object=MibTableColumn
hm2AgentOspfAsLsdbRouterId=_Hm2AgentOspfAsLsdbRouterId_Object((1,3,6,1,4,1,248,12,2,4,18,1,3),_Hm2AgentOspfAsLsdbRouterId_Type())
hm2AgentOspfAsLsdbRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbRouterId.setStatus(_A)
_Hm2AgentOspfAsLsdbSequence_Type=Integer32
_Hm2AgentOspfAsLsdbSequence_Object=MibTableColumn
hm2AgentOspfAsLsdbSequence=_Hm2AgentOspfAsLsdbSequence_Object((1,3,6,1,4,1,248,12,2,4,18,1,4),_Hm2AgentOspfAsLsdbSequence_Type())
hm2AgentOspfAsLsdbSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbSequence.setStatus(_A)
_Hm2AgentOspfAsLsdbAge_Type=Integer32
_Hm2AgentOspfAsLsdbAge_Object=MibTableColumn
hm2AgentOspfAsLsdbAge=_Hm2AgentOspfAsLsdbAge_Object((1,3,6,1,4,1,248,12,2,4,18,1,5),_Hm2AgentOspfAsLsdbAge_Type())
hm2AgentOspfAsLsdbAge.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbAge.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbAge.setUnits(_V)
_Hm2AgentOspfAsLsdbChecksum_Type=Integer32
_Hm2AgentOspfAsLsdbChecksum_Object=MibTableColumn
hm2AgentOspfAsLsdbChecksum=_Hm2AgentOspfAsLsdbChecksum_Object((1,3,6,1,4,1,248,12,2,4,18,1,6),_Hm2AgentOspfAsLsdbChecksum_Type())
hm2AgentOspfAsLsdbChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbChecksum.setStatus(_A)
class _Hm2AgentOspfAsLsdbAdvertisement_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_Hm2AgentOspfAsLsdbAdvertisement_Type.__name__=_Q
_Hm2AgentOspfAsLsdbAdvertisement_Object=MibTableColumn
hm2AgentOspfAsLsdbAdvertisement=_Hm2AgentOspfAsLsdbAdvertisement_Object((1,3,6,1,4,1,248,12,2,4,18,1,7),_Hm2AgentOspfAsLsdbAdvertisement_Type())
hm2AgentOspfAsLsdbAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfAsLsdbAdvertisement.setStatus(_A)
class _Hm2AgentOspfDefaultPassiveMode_Type(TruthValue):defaultValue=2
_Hm2AgentOspfDefaultPassiveMode_Type.__name__=_J
_Hm2AgentOspfDefaultPassiveMode_Object=MibScalar
hm2AgentOspfDefaultPassiveMode=_Hm2AgentOspfDefaultPassiveMode_Object((1,3,6,1,4,1,248,12,2,4,19),_Hm2AgentOspfDefaultPassiveMode_Type())
hm2AgentOspfDefaultPassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfDefaultPassiveMode.setStatus(_A)
class _Hm2AgentOspfRoutePrefIntraArea_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentOspfRoutePrefIntraArea_Type.__name__=_D
_Hm2AgentOspfRoutePrefIntraArea_Object=MibScalar
hm2AgentOspfRoutePrefIntraArea=_Hm2AgentOspfRoutePrefIntraArea_Object((1,3,6,1,4,1,248,12,2,4,20),_Hm2AgentOspfRoutePrefIntraArea_Type())
hm2AgentOspfRoutePrefIntraArea.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRoutePrefIntraArea.setStatus(_A)
class _Hm2AgentOspfRoutePrefInterArea_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentOspfRoutePrefInterArea_Type.__name__=_D
_Hm2AgentOspfRoutePrefInterArea_Object=MibScalar
hm2AgentOspfRoutePrefInterArea=_Hm2AgentOspfRoutePrefInterArea_Object((1,3,6,1,4,1,248,12,2,4,21),_Hm2AgentOspfRoutePrefInterArea_Type())
hm2AgentOspfRoutePrefInterArea.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRoutePrefInterArea.setStatus(_A)
class _Hm2AgentOspfRoutePrefExternal_Type(Integer32):defaultValue=110;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentOspfRoutePrefExternal_Type.__name__=_D
_Hm2AgentOspfRoutePrefExternal_Object=MibScalar
hm2AgentOspfRoutePrefExternal=_Hm2AgentOspfRoutePrefExternal_Object((1,3,6,1,4,1,248,12,2,4,22),_Hm2AgentOspfRoutePrefExternal_Type())
hm2AgentOspfRoutePrefExternal.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfRoutePrefExternal.setStatus(_A)
_Hm2AgentOspfAreaNSSATable_Object=MibTable
hm2AgentOspfAreaNSSATable=_Hm2AgentOspfAreaNSSATable_Object((1,3,6,1,4,1,248,12,2,4,248))
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSATable.setStatus(_A)
_Hm2AgentOspfAreaNSSAEntry_Object=MibTableRow
hm2AgentOspfAreaNSSAEntry=_Hm2AgentOspfAreaNSSAEntry_Object((1,3,6,1,4,1,248,12,2,4,248,1))
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSAEntry.setStatus(_A)
class _Hm2AgentOspfAreaNSSAImportSummaries_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentOspfAreaNSSAImportSummaries_Type.__name__=_F
_Hm2AgentOspfAreaNSSAImportSummaries_Object=MibTableColumn
hm2AgentOspfAreaNSSAImportSummaries=_Hm2AgentOspfAreaNSSAImportSummaries_Object((1,3,6,1,4,1,248,12,2,4,248,1,1),_Hm2AgentOspfAreaNSSAImportSummaries_Type())
hm2AgentOspfAreaNSSAImportSummaries.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSAImportSummaries.setStatus(_A)
class _Hm2AgentOspfAreaNSSARedistribute_Type(HmEnabledStatus):defaultValue=1
_Hm2AgentOspfAreaNSSARedistribute_Type.__name__=_F
_Hm2AgentOspfAreaNSSARedistribute_Object=MibTableColumn
hm2AgentOspfAreaNSSARedistribute=_Hm2AgentOspfAreaNSSARedistribute_Object((1,3,6,1,4,1,248,12,2,4,248,1,2),_Hm2AgentOspfAreaNSSARedistribute_Type())
hm2AgentOspfAreaNSSARedistribute.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSARedistribute.setStatus(_A)
class _Hm2AgentOspfAreaNSSADefaultInfoOriginate_Type(TruthValue):defaultValue=2
_Hm2AgentOspfAreaNSSADefaultInfoOriginate_Type.__name__=_J
_Hm2AgentOspfAreaNSSADefaultInfoOriginate_Object=MibTableColumn
hm2AgentOspfAreaNSSADefaultInfoOriginate=_Hm2AgentOspfAreaNSSADefaultInfoOriginate_Object((1,3,6,1,4,1,248,12,2,4,248,1,3),_Hm2AgentOspfAreaNSSADefaultInfoOriginate_Type())
hm2AgentOspfAreaNSSADefaultInfoOriginate.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSADefaultInfoOriginate.setStatus(_A)
class _Hm2AgentOspfAreaNSSADefaultMetric_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_Hm2AgentOspfAreaNSSADefaultMetric_Type.__name__=_D
_Hm2AgentOspfAreaNSSADefaultMetric_Object=MibTableColumn
hm2AgentOspfAreaNSSADefaultMetric=_Hm2AgentOspfAreaNSSADefaultMetric_Object((1,3,6,1,4,1,248,12,2,4,248,1,4),_Hm2AgentOspfAreaNSSADefaultMetric_Type())
hm2AgentOspfAreaNSSADefaultMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSADefaultMetric.setStatus(_A)
class _Hm2AgentOspfAreaNSSADefaultMetricType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ospfMetric',1),('comparable',2),('nonComparable',3)))
_Hm2AgentOspfAreaNSSADefaultMetricType_Type.__name__=_D
_Hm2AgentOspfAreaNSSADefaultMetricType_Object=MibTableColumn
hm2AgentOspfAreaNSSADefaultMetricType=_Hm2AgentOspfAreaNSSADefaultMetricType_Object((1,3,6,1,4,1,248,12,2,4,248,1,5),_Hm2AgentOspfAreaNSSADefaultMetricType_Type())
hm2AgentOspfAreaNSSADefaultMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentOspfAreaNSSADefaultMetricType.setStatus(_A)
_Hm2AgentOspfIfMetricTable_Object=MibTable
hm2AgentOspfIfMetricTable=_Hm2AgentOspfIfMetricTable_Object((1,3,6,1,4,1,248,12,2,4,249))
if mibBuilder.loadTexts:hm2AgentOspfIfMetricTable.setStatus(_A)
_Hm2AgentOspfIfMetricEntry_Object=MibTableRow
hm2AgentOspfIfMetricEntry=_Hm2AgentOspfIfMetricEntry_Object((1,3,6,1,4,1,248,12,2,4,249,1))
if mibBuilder.loadTexts:hm2AgentOspfIfMetricEntry.setStatus(_A)
class _Hm2AgentOspfIfMetricCalculatedCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentOspfIfMetricCalculatedCost_Type.__name__=_D
_Hm2AgentOspfIfMetricCalculatedCost_Object=MibTableColumn
hm2AgentOspfIfMetricCalculatedCost=_Hm2AgentOspfIfMetricCalculatedCost_Object((1,3,6,1,4,1,248,12,2,4,249,1,1),_Hm2AgentOspfIfMetricCalculatedCost_Type())
hm2AgentOspfIfMetricCalculatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfIfMetricCalculatedCost.setStatus(_A)
_Hm2AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity=ObjectIdentity
hm2AgentSnmpTrapFlagsConfigGroupLayer3=_Hm2AgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity((1,3,6,1,4,1,248,12,2,5))
class _Hm2AgentSnmpVRRPNewMasterTrapFlag_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSnmpVRRPNewMasterTrapFlag_Type.__name__=_F
_Hm2AgentSnmpVRRPNewMasterTrapFlag_Object=MibScalar
hm2AgentSnmpVRRPNewMasterTrapFlag=_Hm2AgentSnmpVRRPNewMasterTrapFlag_Object((1,3,6,1,4,1,248,12,2,5,1),_Hm2AgentSnmpVRRPNewMasterTrapFlag_Type())
hm2AgentSnmpVRRPNewMasterTrapFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSnmpVRRPNewMasterTrapFlag.setStatus(_A)
class _Hm2AgentSnmpVRRPAuthFailureTrapFlag_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentSnmpVRRPAuthFailureTrapFlag_Type.__name__=_F
_Hm2AgentSnmpVRRPAuthFailureTrapFlag_Object=MibScalar
hm2AgentSnmpVRRPAuthFailureTrapFlag=_Hm2AgentSnmpVRRPAuthFailureTrapFlag_Object((1,3,6,1,4,1,248,12,2,5,2),_Hm2AgentSnmpVRRPAuthFailureTrapFlag_Type())
hm2AgentSnmpVRRPAuthFailureTrapFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSnmpVRRPAuthFailureTrapFlag.setStatus(_A)
_Hm2AgentBootpDhcpRelayGroup_ObjectIdentity=ObjectIdentity
hm2AgentBootpDhcpRelayGroup=_Hm2AgentBootpDhcpRelayGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,6))
class _Hm2AgentBootpDhcpRelayMaxHopCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Hm2AgentBootpDhcpRelayMaxHopCount_Type.__name__=_D
_Hm2AgentBootpDhcpRelayMaxHopCount_Object=MibScalar
hm2AgentBootpDhcpRelayMaxHopCount=_Hm2AgentBootpDhcpRelayMaxHopCount_Object((1,3,6,1,4,1,248,12,2,6,1),_Hm2AgentBootpDhcpRelayMaxHopCount_Type())
hm2AgentBootpDhcpRelayMaxHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentBootpDhcpRelayMaxHopCount.setStatus(_A)
class _Hm2AgentBootpDhcpRelayMinWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2AgentBootpDhcpRelayMinWaitTime_Type.__name__=_D
_Hm2AgentBootpDhcpRelayMinWaitTime_Object=MibScalar
hm2AgentBootpDhcpRelayMinWaitTime=_Hm2AgentBootpDhcpRelayMinWaitTime_Object((1,3,6,1,4,1,248,12,2,6,4),_Hm2AgentBootpDhcpRelayMinWaitTime_Type())
hm2AgentBootpDhcpRelayMinWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentBootpDhcpRelayMinWaitTime.setStatus(_A)
_Hm2AgentBootpDhcpRelayCircuitIdOptionMode_Type=HmEnabledStatus
_Hm2AgentBootpDhcpRelayCircuitIdOptionMode_Object=MibScalar
hm2AgentBootpDhcpRelayCircuitIdOptionMode=_Hm2AgentBootpDhcpRelayCircuitIdOptionMode_Object((1,3,6,1,4,1,248,12,2,6,5),_Hm2AgentBootpDhcpRelayCircuitIdOptionMode_Type())
hm2AgentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentBootpDhcpRelayCircuitIdOptionMode.setStatus(_A)
_Hm2AgentECMPGroup_ObjectIdentity=ObjectIdentity
hm2AgentECMPGroup=_Hm2AgentECMPGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,7))
_Hm2AgentECMPOspfMaxPaths_Type=Integer32
_Hm2AgentECMPOspfMaxPaths_Object=MibScalar
hm2AgentECMPOspfMaxPaths=_Hm2AgentECMPOspfMaxPaths_Object((1,3,6,1,4,1,248,12,2,7,1),_Hm2AgentECMPOspfMaxPaths_Type())
hm2AgentECMPOspfMaxPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentECMPOspfMaxPaths.setStatus(_A)
_Hm2AgentRouterVrrpConfigGroup_ObjectIdentity=ObjectIdentity
hm2AgentRouterVrrpConfigGroup=_Hm2AgentRouterVrrpConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,8))
_Hm2AgentRouterVrrpAdminState_Type=HmEnabledStatus
_Hm2AgentRouterVrrpAdminState_Object=MibScalar
hm2AgentRouterVrrpAdminState=_Hm2AgentRouterVrrpAdminState_Object((1,3,6,1,4,1,248,12,2,8,1),_Hm2AgentRouterVrrpAdminState_Type())
hm2AgentRouterVrrpAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentRouterVrrpAdminState.setStatus(_A)
_Hm2AgentVrrpOperations_ObjectIdentity=ObjectIdentity
hm2AgentVrrpOperations=_Hm2AgentVrrpOperations_ObjectIdentity((1,3,6,1,4,1,248,12,2,9))
_Hm2AgentRouterVrrpOperTable_Object=MibTable
hm2AgentRouterVrrpOperTable=_Hm2AgentRouterVrrpOperTable_Object((1,3,6,1,4,1,248,12,2,9,1))
if mibBuilder.loadTexts:hm2AgentRouterVrrpOperTable.setStatus(_L)
_Hm2AgentRouterVrrpOperEntry_Object=MibTableRow
hm2AgentRouterVrrpOperEntry=_Hm2AgentRouterVrrpOperEntry_Object((1,3,6,1,4,1,248,12,2,9,1,1))
hm2AgentRouterVrrpOperEntry.setIndexNames((0,_W,_X),(0,_a,_b))
if mibBuilder.loadTexts:hm2AgentRouterVrrpOperEntry.setStatus(_L)
class _Hm2AgentRouterVrrpOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentRouterVrrpOperPriority_Type.__name__=_D
_Hm2AgentRouterVrrpOperPriority_Object=MibTableColumn
hm2AgentRouterVrrpOperPriority=_Hm2AgentRouterVrrpOperPriority_Object((1,3,6,1,4,1,248,12,2,9,1,1,1),_Hm2AgentRouterVrrpOperPriority_Type())
hm2AgentRouterVrrpOperPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRouterVrrpOperPriority.setStatus(_L)
class _Hm2AgentRouterVrrpNumberOfFastInst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_Hm2AgentRouterVrrpNumberOfFastInst_Type.__name__=_D
_Hm2AgentRouterVrrpNumberOfFastInst_Object=MibScalar
hm2AgentRouterVrrpNumberOfFastInst=_Hm2AgentRouterVrrpNumberOfFastInst_Object((1,3,6,1,4,1,248,12,2,9,248),_Hm2AgentRouterVrrpNumberOfFastInst_Type())
hm2AgentRouterVrrpNumberOfFastInst.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRouterVrrpNumberOfFastInst.setStatus(_A)
_Hm2AgentIpHelperGroup_ObjectIdentity=ObjectIdentity
hm2AgentIpHelperGroup=_Hm2AgentIpHelperGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,11))
_Hm2AgentIpHelperAdminMode_Type=HmEnabledStatus
_Hm2AgentIpHelperAdminMode_Object=MibScalar
hm2AgentIpHelperAdminMode=_Hm2AgentIpHelperAdminMode_Object((1,3,6,1,4,1,248,12,2,11,1),_Hm2AgentIpHelperAdminMode_Type())
hm2AgentIpHelperAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentIpHelperAdminMode.setStatus(_A)
_Hm2AgentDhcpClientMsgsReceived_Type=Counter32
_Hm2AgentDhcpClientMsgsReceived_Object=MibScalar
hm2AgentDhcpClientMsgsReceived=_Hm2AgentDhcpClientMsgsReceived_Object((1,3,6,1,4,1,248,12,2,11,2),_Hm2AgentDhcpClientMsgsReceived_Type())
hm2AgentDhcpClientMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDhcpClientMsgsReceived.setStatus(_A)
_Hm2AgentDhcpClientMsgsRelayed_Type=Counter32
_Hm2AgentDhcpClientMsgsRelayed_Object=MibScalar
hm2AgentDhcpClientMsgsRelayed=_Hm2AgentDhcpClientMsgsRelayed_Object((1,3,6,1,4,1,248,12,2,11,3),_Hm2AgentDhcpClientMsgsRelayed_Type())
hm2AgentDhcpClientMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDhcpClientMsgsRelayed.setStatus(_A)
_Hm2AgentDhcpServerMsgsReceived_Type=Counter32
_Hm2AgentDhcpServerMsgsReceived_Object=MibScalar
hm2AgentDhcpServerMsgsReceived=_Hm2AgentDhcpServerMsgsReceived_Object((1,3,6,1,4,1,248,12,2,11,4),_Hm2AgentDhcpServerMsgsReceived_Type())
hm2AgentDhcpServerMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDhcpServerMsgsReceived.setStatus(_A)
_Hm2AgentDhcpServerMsgsRelayed_Type=Counter32
_Hm2AgentDhcpServerMsgsRelayed_Object=MibScalar
hm2AgentDhcpServerMsgsRelayed=_Hm2AgentDhcpServerMsgsRelayed_Object((1,3,6,1,4,1,248,12,2,11,5),_Hm2AgentDhcpServerMsgsRelayed_Type())
hm2AgentDhcpServerMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDhcpServerMsgsRelayed.setStatus(_A)
_Hm2AgentUdpClientMsgsReceived_Type=Counter32
_Hm2AgentUdpClientMsgsReceived_Object=MibScalar
hm2AgentUdpClientMsgsReceived=_Hm2AgentUdpClientMsgsReceived_Object((1,3,6,1,4,1,248,12,2,11,6),_Hm2AgentUdpClientMsgsReceived_Type())
hm2AgentUdpClientMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUdpClientMsgsReceived.setStatus(_A)
_Hm2AgentUdpClientMsgsRelayed_Type=Counter32
_Hm2AgentUdpClientMsgsRelayed_Object=MibScalar
hm2AgentUdpClientMsgsRelayed=_Hm2AgentUdpClientMsgsRelayed_Object((1,3,6,1,4,1,248,12,2,11,7),_Hm2AgentUdpClientMsgsRelayed_Type())
hm2AgentUdpClientMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUdpClientMsgsRelayed.setStatus(_A)
_Hm2AgentSwitchIpHelperAddressTable_Object=MibTable
hm2AgentSwitchIpHelperAddressTable=_Hm2AgentSwitchIpHelperAddressTable_Object((1,3,6,1,4,1,248,12,2,11,8))
if mibBuilder.loadTexts:hm2AgentSwitchIpHelperAddressTable.setStatus(_A)
_Hm2AgentSwitchIpHelperAddressEntry_Object=MibTableRow
hm2AgentSwitchIpHelperAddressEntry=_Hm2AgentSwitchIpHelperAddressEntry_Object((1,3,6,1,4,1,248,12,2,11,8,1))
hm2AgentSwitchIpHelperAddressEntry.setIndexNames((0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:hm2AgentSwitchIpHelperAddressEntry.setStatus(_A)
class _Hm2AgentSwitchIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentSwitchIpHelperUdpPort_Type.__name__=_I
_Hm2AgentSwitchIpHelperUdpPort_Object=MibTableColumn
hm2AgentSwitchIpHelperUdpPort=_Hm2AgentSwitchIpHelperUdpPort_Object((1,3,6,1,4,1,248,12,2,11,8,1,1),_Hm2AgentSwitchIpHelperUdpPort_Type())
hm2AgentSwitchIpHelperUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpHelperUdpPort.setStatus(_A)
_Hm2AgentSwitchIpHelperAddress_Type=IpAddress
_Hm2AgentSwitchIpHelperAddress_Object=MibTableColumn
hm2AgentSwitchIpHelperAddress=_Hm2AgentSwitchIpHelperAddress_Object((1,3,6,1,4,1,248,12,2,11,8,1,2),_Hm2AgentSwitchIpHelperAddress_Type())
hm2AgentSwitchIpHelperAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentSwitchIpHelperAddress.setStatus(_A)
_Hm2AgentSwitchIpHelperHitCount_Type=Unsigned32
_Hm2AgentSwitchIpHelperHitCount_Object=MibTableColumn
hm2AgentSwitchIpHelperHitCount=_Hm2AgentSwitchIpHelperHitCount_Object((1,3,6,1,4,1,248,12,2,11,8,1,3),_Hm2AgentSwitchIpHelperHitCount_Type())
hm2AgentSwitchIpHelperHitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchIpHelperHitCount.setStatus(_A)
_Hm2AgentSwitchIpHelperStatus_Type=RowStatus
_Hm2AgentSwitchIpHelperStatus_Object=MibTableColumn
hm2AgentSwitchIpHelperStatus=_Hm2AgentSwitchIpHelperStatus_Object((1,3,6,1,4,1,248,12,2,11,8,1,4),_Hm2AgentSwitchIpHelperStatus_Type())
hm2AgentSwitchIpHelperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentSwitchIpHelperStatus.setStatus(_A)
_Hm2AgentUdpClientMsgsTtlExpired_Type=Counter32
_Hm2AgentUdpClientMsgsTtlExpired_Object=MibScalar
hm2AgentUdpClientMsgsTtlExpired=_Hm2AgentUdpClientMsgsTtlExpired_Object((1,3,6,1,4,1,248,12,2,11,9),_Hm2AgentUdpClientMsgsTtlExpired_Type())
hm2AgentUdpClientMsgsTtlExpired.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUdpClientMsgsTtlExpired.setStatus(_A)
_Hm2AgentUdpClientMsgsDiscarded_Type=Counter32
_Hm2AgentUdpClientMsgsDiscarded_Object=MibScalar
hm2AgentUdpClientMsgsDiscarded=_Hm2AgentUdpClientMsgsDiscarded_Object((1,3,6,1,4,1,248,12,2,11,10),_Hm2AgentUdpClientMsgsDiscarded_Type())
hm2AgentUdpClientMsgsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUdpClientMsgsDiscarded.setStatus(_A)
_Hm2AgentInternalVlanGroup_ObjectIdentity=ObjectIdentity
hm2AgentInternalVlanGroup=_Hm2AgentInternalVlanGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,12))
class _Hm2AgentInternalVlanBase_Type(VlanId):defaultValue=4093
_Hm2AgentInternalVlanBase_Type.__name__=_Z
_Hm2AgentInternalVlanBase_Object=MibScalar
hm2AgentInternalVlanBase=_Hm2AgentInternalVlanBase_Object((1,3,6,1,4,1,248,12,2,12,1),_Hm2AgentInternalVlanBase_Type())
hm2AgentInternalVlanBase.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentInternalVlanBase.setStatus(_A)
class _Hm2AgentInternalVlanPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascending',0),('descending',1)))
_Hm2AgentInternalVlanPolicy_Type.__name__=_D
_Hm2AgentInternalVlanPolicy_Object=MibScalar
hm2AgentInternalVlanPolicy=_Hm2AgentInternalVlanPolicy_Object((1,3,6,1,4,1,248,12,2,12,2),_Hm2AgentInternalVlanPolicy_Type())
hm2AgentInternalVlanPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentInternalVlanPolicy.setStatus(_A)
_Hm2AgentSwitchInternalVlanTable_Object=MibTable
hm2AgentSwitchInternalVlanTable=_Hm2AgentSwitchInternalVlanTable_Object((1,3,6,1,4,1,248,12,2,12,3))
if mibBuilder.loadTexts:hm2AgentSwitchInternalVlanTable.setStatus(_A)
_Hm2AgentSwitchInternalVlanEntry_Object=MibTableRow
hm2AgentSwitchInternalVlanEntry=_Hm2AgentSwitchInternalVlanEntry_Object((1,3,6,1,4,1,248,12,2,12,3,1))
hm2AgentSwitchInternalVlanEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:hm2AgentSwitchInternalVlanEntry.setStatus(_A)
_Hm2AgentSwitchInternalVlanId_Type=VlanId
_Hm2AgentSwitchInternalVlanId_Object=MibTableColumn
hm2AgentSwitchInternalVlanId=_Hm2AgentSwitchInternalVlanId_Object((1,3,6,1,4,1,248,12,2,12,3,1,1),_Hm2AgentSwitchInternalVlanId_Type())
hm2AgentSwitchInternalVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentSwitchInternalVlanId.setStatus(_A)
_Hm2AgentSwitchInternalVlanIfIndex_Type=InterfaceIndex
_Hm2AgentSwitchInternalVlanIfIndex_Object=MibTableColumn
hm2AgentSwitchInternalVlanIfIndex=_Hm2AgentSwitchInternalVlanIfIndex_Object((1,3,6,1,4,1,248,12,2,12,3,1,2),_Hm2AgentSwitchInternalVlanIfIndex_Type())
hm2AgentSwitchInternalVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentSwitchInternalVlanIfIndex.setStatus(_A)
_Hm2AgentOspfQueueGroup_ObjectIdentity=ObjectIdentity
hm2AgentOspfQueueGroup=_Hm2AgentOspfQueueGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,13))
_Hm2AgentOspfQueueTable_Object=MibTable
hm2AgentOspfQueueTable=_Hm2AgentOspfQueueTable_Object((1,3,6,1,4,1,248,12,2,13,1))
if mibBuilder.loadTexts:hm2AgentOspfQueueTable.setStatus(_A)
_Hm2AgentOspfQueueEntry_Object=MibTableRow
hm2AgentOspfQueueEntry=_Hm2AgentOspfQueueEntry_Object((1,3,6,1,4,1,248,12,2,13,1,1))
hm2AgentOspfQueueEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:hm2AgentOspfQueueEntry.setStatus(_A)
_Hm2AgentOspfQueueIndex_Type=Unsigned32
_Hm2AgentOspfQueueIndex_Object=MibTableColumn
hm2AgentOspfQueueIndex=_Hm2AgentOspfQueueIndex_Object((1,3,6,1,4,1,248,12,2,13,1,1,1),_Hm2AgentOspfQueueIndex_Type())
hm2AgentOspfQueueIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentOspfQueueIndex.setStatus(_A)
_Hm2AgentOspfQueueName_Type=DisplayString
_Hm2AgentOspfQueueName_Object=MibTableColumn
hm2AgentOspfQueueName=_Hm2AgentOspfQueueName_Object((1,3,6,1,4,1,248,12,2,13,1,1,2),_Hm2AgentOspfQueueName_Type())
hm2AgentOspfQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfQueueName.setStatus(_A)
_Hm2AgentOspfQueueLength_Type=Gauge32
_Hm2AgentOspfQueueLength_Object=MibTableColumn
hm2AgentOspfQueueLength=_Hm2AgentOspfQueueLength_Object((1,3,6,1,4,1,248,12,2,13,1,1,3),_Hm2AgentOspfQueueLength_Type())
hm2AgentOspfQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfQueueLength.setStatus(_A)
_Hm2AgentOspfQueueHigh_Type=Gauge32
_Hm2AgentOspfQueueHigh_Object=MibTableColumn
hm2AgentOspfQueueHigh=_Hm2AgentOspfQueueHigh_Object((1,3,6,1,4,1,248,12,2,13,1,1,4),_Hm2AgentOspfQueueHigh_Type())
hm2AgentOspfQueueHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfQueueHigh.setStatus(_A)
_Hm2AgentOspfQueueDrops_Type=Counter32
_Hm2AgentOspfQueueDrops_Object=MibTableColumn
hm2AgentOspfQueueDrops=_Hm2AgentOspfQueueDrops_Object((1,3,6,1,4,1,248,12,2,13,1,1,5),_Hm2AgentOspfQueueDrops_Type())
hm2AgentOspfQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfQueueDrops.setStatus(_A)
_Hm2AgentOspfQueueLimit_Type=Unsigned32
_Hm2AgentOspfQueueLimit_Object=MibTableColumn
hm2AgentOspfQueueLimit=_Hm2AgentOspfQueueLimit_Object((1,3,6,1,4,1,248,12,2,13,1,1,6),_Hm2AgentOspfQueueLimit_Type())
hm2AgentOspfQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfQueueLimit.setStatus(_A)
_Hm2AgentOspfPacketStatsGroup_ObjectIdentity=ObjectIdentity
hm2AgentOspfPacketStatsGroup=_Hm2AgentOspfPacketStatsGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,14))
_Hm2AgentOspfCountersCleared_Type=Unsigned32
_Hm2AgentOspfCountersCleared_Object=MibScalar
hm2AgentOspfCountersCleared=_Hm2AgentOspfCountersCleared_Object((1,3,6,1,4,1,248,12,2,14,1),_Hm2AgentOspfCountersCleared_Type())
hm2AgentOspfCountersCleared.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfCountersCleared.setStatus(_A)
_Hm2AgentOspfLsaRetxCount_Type=Counter32
_Hm2AgentOspfLsaRetxCount_Object=MibScalar
hm2AgentOspfLsaRetxCount=_Hm2AgentOspfLsaRetxCount_Object((1,3,6,1,4,1,248,12,2,14,2),_Hm2AgentOspfLsaRetxCount_Type())
hm2AgentOspfLsaRetxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsaRetxCount.setStatus(_A)
_Hm2AgentOspfHellosRx_Type=Counter32
_Hm2AgentOspfHellosRx_Object=MibScalar
hm2AgentOspfHellosRx=_Hm2AgentOspfHellosRx_Object((1,3,6,1,4,1,248,12,2,14,3),_Hm2AgentOspfHellosRx_Type())
hm2AgentOspfHellosRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfHellosRx.setStatus(_A)
_Hm2AgentOspfHellosTx_Type=Counter32
_Hm2AgentOspfHellosTx_Object=MibScalar
hm2AgentOspfHellosTx=_Hm2AgentOspfHellosTx_Object((1,3,6,1,4,1,248,12,2,14,4),_Hm2AgentOspfHellosTx_Type())
hm2AgentOspfHellosTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfHellosTx.setStatus(_A)
_Hm2AgentOspfDdRx_Type=Counter32
_Hm2AgentOspfDdRx_Object=MibScalar
hm2AgentOspfDdRx=_Hm2AgentOspfDdRx_Object((1,3,6,1,4,1,248,12,2,14,5),_Hm2AgentOspfDdRx_Type())
hm2AgentOspfDdRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfDdRx.setStatus(_A)
_Hm2AgentOspfDdTx_Type=Counter32
_Hm2AgentOspfDdTx_Object=MibScalar
hm2AgentOspfDdTx=_Hm2AgentOspfDdTx_Object((1,3,6,1,4,1,248,12,2,14,6),_Hm2AgentOspfDdTx_Type())
hm2AgentOspfDdTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfDdTx.setStatus(_A)
_Hm2AgentOspfLsReqRx_Type=Counter32
_Hm2AgentOspfLsReqRx_Object=MibScalar
hm2AgentOspfLsReqRx=_Hm2AgentOspfLsReqRx_Object((1,3,6,1,4,1,248,12,2,14,7),_Hm2AgentOspfLsReqRx_Type())
hm2AgentOspfLsReqRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsReqRx.setStatus(_A)
_Hm2AgentOspfLsReqTx_Type=Counter32
_Hm2AgentOspfLsReqTx_Object=MibScalar
hm2AgentOspfLsReqTx=_Hm2AgentOspfLsReqTx_Object((1,3,6,1,4,1,248,12,2,14,8),_Hm2AgentOspfLsReqTx_Type())
hm2AgentOspfLsReqTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsReqTx.setStatus(_A)
_Hm2AgentOspfLsUpdatesRx_Type=Counter32
_Hm2AgentOspfLsUpdatesRx_Object=MibScalar
hm2AgentOspfLsUpdatesRx=_Hm2AgentOspfLsUpdatesRx_Object((1,3,6,1,4,1,248,12,2,14,9),_Hm2AgentOspfLsUpdatesRx_Type())
hm2AgentOspfLsUpdatesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsUpdatesRx.setStatus(_A)
_Hm2AgentOspfLsUpdatesTx_Type=Counter32
_Hm2AgentOspfLsUpdatesTx_Object=MibScalar
hm2AgentOspfLsUpdatesTx=_Hm2AgentOspfLsUpdatesTx_Object((1,3,6,1,4,1,248,12,2,14,10),_Hm2AgentOspfLsUpdatesTx_Type())
hm2AgentOspfLsUpdatesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsUpdatesTx.setStatus(_A)
_Hm2AgentOspfLsAckRx_Type=Counter32
_Hm2AgentOspfLsAckRx_Object=MibScalar
hm2AgentOspfLsAckRx=_Hm2AgentOspfLsAckRx_Object((1,3,6,1,4,1,248,12,2,14,11),_Hm2AgentOspfLsAckRx_Type())
hm2AgentOspfLsAckRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsAckRx.setStatus(_A)
_Hm2AgentOspfLsAckTx_Type=Counter32
_Hm2AgentOspfLsAckTx_Object=MibScalar
hm2AgentOspfLsAckTx=_Hm2AgentOspfLsAckTx_Object((1,3,6,1,4,1,248,12,2,14,12),_Hm2AgentOspfLsAckTx_Type())
hm2AgentOspfLsAckTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsAckTx.setStatus(_A)
_Hm2AgentOspfLsUpdatesRxMax_Type=Gauge32
_Hm2AgentOspfLsUpdatesRxMax_Object=MibScalar
hm2AgentOspfLsUpdatesRxMax=_Hm2AgentOspfLsUpdatesRxMax_Object((1,3,6,1,4,1,248,12,2,14,13),_Hm2AgentOspfLsUpdatesRxMax_Type())
hm2AgentOspfLsUpdatesRxMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsUpdatesRxMax.setStatus(_A)
_Hm2AgentOspfLsUpdatesTxMax_Type=Gauge32
_Hm2AgentOspfLsUpdatesTxMax_Object=MibScalar
hm2AgentOspfLsUpdatesTxMax=_Hm2AgentOspfLsUpdatesTxMax_Object((1,3,6,1,4,1,248,12,2,14,14),_Hm2AgentOspfLsUpdatesTxMax_Type())
hm2AgentOspfLsUpdatesTxMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfLsUpdatesTxMax.setStatus(_A)
_Hm2AgentOspfType1LsasRx_Type=Counter32
_Hm2AgentOspfType1LsasRx_Object=MibScalar
hm2AgentOspfType1LsasRx=_Hm2AgentOspfType1LsasRx_Object((1,3,6,1,4,1,248,12,2,14,15),_Hm2AgentOspfType1LsasRx_Type())
hm2AgentOspfType1LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType1LsasRx.setStatus(_A)
_Hm2AgentOspfType2LsasRx_Type=Counter32
_Hm2AgentOspfType2LsasRx_Object=MibScalar
hm2AgentOspfType2LsasRx=_Hm2AgentOspfType2LsasRx_Object((1,3,6,1,4,1,248,12,2,14,16),_Hm2AgentOspfType2LsasRx_Type())
hm2AgentOspfType2LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType2LsasRx.setStatus(_A)
_Hm2AgentOspfType3LsasRx_Type=Counter32
_Hm2AgentOspfType3LsasRx_Object=MibScalar
hm2AgentOspfType3LsasRx=_Hm2AgentOspfType3LsasRx_Object((1,3,6,1,4,1,248,12,2,14,17),_Hm2AgentOspfType3LsasRx_Type())
hm2AgentOspfType3LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType3LsasRx.setStatus(_A)
_Hm2AgentOspfType4LsasRx_Type=Counter32
_Hm2AgentOspfType4LsasRx_Object=MibScalar
hm2AgentOspfType4LsasRx=_Hm2AgentOspfType4LsasRx_Object((1,3,6,1,4,1,248,12,2,14,18),_Hm2AgentOspfType4LsasRx_Type())
hm2AgentOspfType4LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType4LsasRx.setStatus(_A)
_Hm2AgentOspfType5LsasRx_Type=Counter32
_Hm2AgentOspfType5LsasRx_Object=MibScalar
hm2AgentOspfType5LsasRx=_Hm2AgentOspfType5LsasRx_Object((1,3,6,1,4,1,248,12,2,14,19),_Hm2AgentOspfType5LsasRx_Type())
hm2AgentOspfType5LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType5LsasRx.setStatus(_A)
_Hm2AgentOspfType7LsasRx_Type=Counter32
_Hm2AgentOspfType7LsasRx_Object=MibScalar
hm2AgentOspfType7LsasRx=_Hm2AgentOspfType7LsasRx_Object((1,3,6,1,4,1,248,12,2,14,20),_Hm2AgentOspfType7LsasRx_Type())
hm2AgentOspfType7LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType7LsasRx.setStatus(_A)
_Hm2AgentOspfType9LsasRx_Type=Counter32
_Hm2AgentOspfType9LsasRx_Object=MibScalar
hm2AgentOspfType9LsasRx=_Hm2AgentOspfType9LsasRx_Object((1,3,6,1,4,1,248,12,2,14,21),_Hm2AgentOspfType9LsasRx_Type())
hm2AgentOspfType9LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType9LsasRx.setStatus(_A)
_Hm2AgentOspfType10LsasRx_Type=Counter32
_Hm2AgentOspfType10LsasRx_Object=MibScalar
hm2AgentOspfType10LsasRx=_Hm2AgentOspfType10LsasRx_Object((1,3,6,1,4,1,248,12,2,14,22),_Hm2AgentOspfType10LsasRx_Type())
hm2AgentOspfType10LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType10LsasRx.setStatus(_A)
_Hm2AgentOspfType11LsasRx_Type=Counter32
_Hm2AgentOspfType11LsasRx_Object=MibScalar
hm2AgentOspfType11LsasRx=_Hm2AgentOspfType11LsasRx_Object((1,3,6,1,4,1,248,12,2,14,23),_Hm2AgentOspfType11LsasRx_Type())
hm2AgentOspfType11LsasRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfType11LsasRx.setStatus(_A)
_Hm2AgentOspfSpfStatsTable_Object=MibTable
hm2AgentOspfSpfStatsTable=_Hm2AgentOspfSpfStatsTable_Object((1,3,6,1,4,1,248,12,2,15))
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsTable.setStatus(_A)
_Hm2AgentOspfSpfStatsEntry_Object=MibTableRow
hm2AgentOspfSpfStatsEntry=_Hm2AgentOspfSpfStatsEntry_Object((1,3,6,1,4,1,248,12,2,15,1))
hm2AgentOspfSpfStatsEntry.setIndexNames((0,_E,_A4))
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsEntry.setStatus(_A)
_Hm2AgentOspfSpfIndex_Type=Unsigned32
_Hm2AgentOspfSpfIndex_Object=MibTableColumn
hm2AgentOspfSpfIndex=_Hm2AgentOspfSpfIndex_Object((1,3,6,1,4,1,248,12,2,15,1,1),_Hm2AgentOspfSpfIndex_Type())
hm2AgentOspfSpfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentOspfSpfIndex.setStatus(_A)
_Hm2AgentOspfSpfStatsDeltaT_Type=Unsigned32
_Hm2AgentOspfSpfStatsDeltaT_Object=MibTableColumn
hm2AgentOspfSpfStatsDeltaT=_Hm2AgentOspfSpfStatsDeltaT_Object((1,3,6,1,4,1,248,12,2,15,1,2),_Hm2AgentOspfSpfStatsDeltaT_Type())
hm2AgentOspfSpfStatsDeltaT.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsDeltaT.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsDeltaT.setUnits(_V)
_Hm2AgentOspfSpfStatsIntra_Type=Unsigned32
_Hm2AgentOspfSpfStatsIntra_Object=MibTableColumn
hm2AgentOspfSpfStatsIntra=_Hm2AgentOspfSpfStatsIntra_Object((1,3,6,1,4,1,248,12,2,15,1,3),_Hm2AgentOspfSpfStatsIntra_Type())
hm2AgentOspfSpfStatsIntra.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsIntra.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsIntra.setUnits(_K)
_Hm2AgentOspfSpfStatsSumm_Type=Unsigned32
_Hm2AgentOspfSpfStatsSumm_Object=MibTableColumn
hm2AgentOspfSpfStatsSumm=_Hm2AgentOspfSpfStatsSumm_Object((1,3,6,1,4,1,248,12,2,15,1,4),_Hm2AgentOspfSpfStatsSumm_Type())
hm2AgentOspfSpfStatsSumm.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsSumm.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsSumm.setUnits(_K)
_Hm2AgentOspfSpfStatsExt_Type=Unsigned32
_Hm2AgentOspfSpfStatsExt_Object=MibTableColumn
hm2AgentOspfSpfStatsExt=_Hm2AgentOspfSpfStatsExt_Object((1,3,6,1,4,1,248,12,2,15,1,5),_Hm2AgentOspfSpfStatsExt_Type())
hm2AgentOspfSpfStatsExt.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsExt.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsExt.setUnits(_K)
_Hm2AgentOspfSpfStatsSpfTotal_Type=Unsigned32
_Hm2AgentOspfSpfStatsSpfTotal_Object=MibTableColumn
hm2AgentOspfSpfStatsSpfTotal=_Hm2AgentOspfSpfStatsSpfTotal_Object((1,3,6,1,4,1,248,12,2,15,1,6),_Hm2AgentOspfSpfStatsSpfTotal_Type())
hm2AgentOspfSpfStatsSpfTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsSpfTotal.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsSpfTotal.setUnits(_K)
_Hm2AgentOspfSpfStatsRibUpdate_Type=Unsigned32
_Hm2AgentOspfSpfStatsRibUpdate_Object=MibTableColumn
hm2AgentOspfSpfStatsRibUpdate=_Hm2AgentOspfSpfStatsRibUpdate_Object((1,3,6,1,4,1,248,12,2,15,1,7),_Hm2AgentOspfSpfStatsRibUpdate_Type())
hm2AgentOspfSpfStatsRibUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsRibUpdate.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsRibUpdate.setUnits(_K)
_Hm2AgentOspfSpfStatsReason_Type=DisplayString
_Hm2AgentOspfSpfStatsReason_Object=MibTableColumn
hm2AgentOspfSpfStatsReason=_Hm2AgentOspfSpfStatsReason_Object((1,3,6,1,4,1,248,12,2,15,1,8),_Hm2AgentOspfSpfStatsReason_Type())
hm2AgentOspfSpfStatsReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfSpfStatsReason.setStatus(_A)
_Hm2AgentRoutingHeapGroup_ObjectIdentity=ObjectIdentity
hm2AgentRoutingHeapGroup=_Hm2AgentRoutingHeapGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,16))
_Hm2AgentRoutingHeapSize_Type=Unsigned32
_Hm2AgentRoutingHeapSize_Object=MibScalar
hm2AgentRoutingHeapSize=_Hm2AgentRoutingHeapSize_Object((1,3,6,1,4,1,248,12,2,16,1),_Hm2AgentRoutingHeapSize_Type())
hm2AgentRoutingHeapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRoutingHeapSize.setStatus(_A)
_Hm2AgentRoutingHeapInUse_Type=Gauge32
_Hm2AgentRoutingHeapInUse_Object=MibScalar
hm2AgentRoutingHeapInUse=_Hm2AgentRoutingHeapInUse_Object((1,3,6,1,4,1,248,12,2,16,2),_Hm2AgentRoutingHeapInUse_Type())
hm2AgentRoutingHeapInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRoutingHeapInUse.setStatus(_A)
_Hm2AgentRoutingHeapHigh_Type=Gauge32
_Hm2AgentRoutingHeapHigh_Object=MibScalar
hm2AgentRoutingHeapHigh=_Hm2AgentRoutingHeapHigh_Object((1,3,6,1,4,1,248,12,2,16,3),_Hm2AgentRoutingHeapHigh_Type())
hm2AgentRoutingHeapHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRoutingHeapHigh.setStatus(_A)
_Hm2AgentRoutingTableSummaryGroup_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTableSummaryGroup=_Hm2AgentRoutingTableSummaryGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,17))
_Hm2AgentConnectedRoutes_Type=Gauge32
_Hm2AgentConnectedRoutes_Object=MibScalar
hm2AgentConnectedRoutes=_Hm2AgentConnectedRoutes_Object((1,3,6,1,4,1,248,12,2,17,1),_Hm2AgentConnectedRoutes_Type())
hm2AgentConnectedRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentConnectedRoutes.setStatus(_A)
_Hm2AgentStaticRoutes_Type=Gauge32
_Hm2AgentStaticRoutes_Object=MibScalar
hm2AgentStaticRoutes=_Hm2AgentStaticRoutes_Object((1,3,6,1,4,1,248,12,2,17,2),_Hm2AgentStaticRoutes_Type())
hm2AgentStaticRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStaticRoutes.setStatus(_A)
_Hm2AgentRipRoutes_Type=Gauge32
_Hm2AgentRipRoutes_Object=MibScalar
hm2AgentRipRoutes=_Hm2AgentRipRoutes_Object((1,3,6,1,4,1,248,12,2,17,3),_Hm2AgentRipRoutes_Type())
hm2AgentRipRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRipRoutes.setStatus(_A)
_Hm2AgentOspfRoutes_Type=Gauge32
_Hm2AgentOspfRoutes_Object=MibScalar
hm2AgentOspfRoutes=_Hm2AgentOspfRoutes_Object((1,3,6,1,4,1,248,12,2,17,4),_Hm2AgentOspfRoutes_Type())
hm2AgentOspfRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfRoutes.setStatus(_A)
_Hm2AgentOspfIntraRoutes_Type=Gauge32
_Hm2AgentOspfIntraRoutes_Object=MibScalar
hm2AgentOspfIntraRoutes=_Hm2AgentOspfIntraRoutes_Object((1,3,6,1,4,1,248,12,2,17,5),_Hm2AgentOspfIntraRoutes_Type())
hm2AgentOspfIntraRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfIntraRoutes.setStatus(_A)
_Hm2AgentOspfInterRoutes_Type=Gauge32
_Hm2AgentOspfInterRoutes_Object=MibScalar
hm2AgentOspfInterRoutes=_Hm2AgentOspfInterRoutes_Object((1,3,6,1,4,1,248,12,2,17,6),_Hm2AgentOspfInterRoutes_Type())
hm2AgentOspfInterRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfInterRoutes.setStatus(_A)
_Hm2AgentOspfExt1Routes_Type=Gauge32
_Hm2AgentOspfExt1Routes_Object=MibScalar
hm2AgentOspfExt1Routes=_Hm2AgentOspfExt1Routes_Object((1,3,6,1,4,1,248,12,2,17,7),_Hm2AgentOspfExt1Routes_Type())
hm2AgentOspfExt1Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfExt1Routes.setStatus(_A)
_Hm2AgentOspfExt2Routes_Type=Gauge32
_Hm2AgentOspfExt2Routes_Object=MibScalar
hm2AgentOspfExt2Routes=_Hm2AgentOspfExt2Routes_Object((1,3,6,1,4,1,248,12,2,17,8),_Hm2AgentOspfExt2Routes_Type())
hm2AgentOspfExt2Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfExt2Routes.setStatus(_A)
_Hm2AgentBgpRoutes_Type=Gauge32
_Hm2AgentBgpRoutes_Object=MibScalar
hm2AgentBgpRoutes=_Hm2AgentBgpRoutes_Object((1,3,6,1,4,1,248,12,2,17,9),_Hm2AgentBgpRoutes_Type())
hm2AgentBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentBgpRoutes.setStatus(_A)
_Hm2AgentEbgpRoutes_Type=Gauge32
_Hm2AgentEbgpRoutes_Object=MibScalar
hm2AgentEbgpRoutes=_Hm2AgentEbgpRoutes_Object((1,3,6,1,4,1,248,12,2,17,10),_Hm2AgentEbgpRoutes_Type())
hm2AgentEbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentEbgpRoutes.setStatus(_A)
_Hm2AgentIbgpRoutes_Type=Gauge32
_Hm2AgentIbgpRoutes_Object=MibScalar
hm2AgentIbgpRoutes=_Hm2AgentIbgpRoutes_Object((1,3,6,1,4,1,248,12,2,17,11),_Hm2AgentIbgpRoutes_Type())
hm2AgentIbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentIbgpRoutes.setStatus(_A)
_Hm2AgentLocalBgpRoutes_Type=Gauge32
_Hm2AgentLocalBgpRoutes_Object=MibScalar
hm2AgentLocalBgpRoutes=_Hm2AgentLocalBgpRoutes_Object((1,3,6,1,4,1,248,12,2,17,12),_Hm2AgentLocalBgpRoutes_Type())
hm2AgentLocalBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentLocalBgpRoutes.setStatus(_A)
_Hm2AgentRejectRoutes_Type=Gauge32
_Hm2AgentRejectRoutes_Object=MibScalar
hm2AgentRejectRoutes=_Hm2AgentRejectRoutes_Object((1,3,6,1,4,1,248,12,2,17,13),_Hm2AgentRejectRoutes_Type())
hm2AgentRejectRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRejectRoutes.setStatus(_A)
_Hm2AgentTotalRoutes_Type=Gauge32
_Hm2AgentTotalRoutes_Object=MibScalar
hm2AgentTotalRoutes=_Hm2AgentTotalRoutes_Object((1,3,6,1,4,1,248,12,2,17,14),_Hm2AgentTotalRoutes_Type())
hm2AgentTotalRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTotalRoutes.setStatus(_A)
_Hm2AgentBestRoutes_Type=Gauge32
_Hm2AgentBestRoutes_Object=MibScalar
hm2AgentBestRoutes=_Hm2AgentBestRoutes_Object((1,3,6,1,4,1,248,12,2,17,15),_Hm2AgentBestRoutes_Type())
hm2AgentBestRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentBestRoutes.setStatus(_A)
_Hm2AgentBestRoutesHigh_Type=Gauge32
_Hm2AgentBestRoutesHigh_Object=MibScalar
hm2AgentBestRoutesHigh=_Hm2AgentBestRoutesHigh_Object((1,3,6,1,4,1,248,12,2,17,16),_Hm2AgentBestRoutesHigh_Type())
hm2AgentBestRoutesHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentBestRoutesHigh.setStatus(_A)
_Hm2AgentAlternateRoutes_Type=Gauge32
_Hm2AgentAlternateRoutes_Object=MibScalar
hm2AgentAlternateRoutes=_Hm2AgentAlternateRoutes_Object((1,3,6,1,4,1,248,12,2,17,17),_Hm2AgentAlternateRoutes_Type())
hm2AgentAlternateRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentAlternateRoutes.setStatus(_A)
_Hm2AgentRouteAdds_Type=Counter32
_Hm2AgentRouteAdds_Object=MibScalar
hm2AgentRouteAdds=_Hm2AgentRouteAdds_Object((1,3,6,1,4,1,248,12,2,17,18),_Hm2AgentRouteAdds_Type())
hm2AgentRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRouteAdds.setStatus(_A)
_Hm2AgentRouteModifies_Type=Counter32
_Hm2AgentRouteModifies_Object=MibScalar
hm2AgentRouteModifies=_Hm2AgentRouteModifies_Object((1,3,6,1,4,1,248,12,2,17,19),_Hm2AgentRouteModifies_Type())
hm2AgentRouteModifies.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRouteModifies.setStatus(_A)
_Hm2AgentRouteDeletes_Type=Counter32
_Hm2AgentRouteDeletes_Object=MibScalar
hm2AgentRouteDeletes=_Hm2AgentRouteDeletes_Object((1,3,6,1,4,1,248,12,2,17,20),_Hm2AgentRouteDeletes_Type())
hm2AgentRouteDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentRouteDeletes.setStatus(_A)
_Hm2AgentUnresolvedRouteAdds_Type=Counter32
_Hm2AgentUnresolvedRouteAdds_Object=MibScalar
hm2AgentUnresolvedRouteAdds=_Hm2AgentUnresolvedRouteAdds_Object((1,3,6,1,4,1,248,12,2,17,21),_Hm2AgentUnresolvedRouteAdds_Type())
hm2AgentUnresolvedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUnresolvedRouteAdds.setStatus(_A)
_Hm2AgentInvalidRouteAdds_Type=Counter32
_Hm2AgentInvalidRouteAdds_Object=MibScalar
hm2AgentInvalidRouteAdds=_Hm2AgentInvalidRouteAdds_Object((1,3,6,1,4,1,248,12,2,17,22),_Hm2AgentInvalidRouteAdds_Type())
hm2AgentInvalidRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentInvalidRouteAdds.setStatus(_A)
_Hm2AgentFailedRouteAdds_Type=Counter32
_Hm2AgentFailedRouteAdds_Object=MibScalar
hm2AgentFailedRouteAdds=_Hm2AgentFailedRouteAdds_Object((1,3,6,1,4,1,248,12,2,17,23),_Hm2AgentFailedRouteAdds_Type())
hm2AgentFailedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentFailedRouteAdds.setStatus(_A)
_Hm2AgentReservedLocals_Type=Gauge32
_Hm2AgentReservedLocals_Object=MibScalar
hm2AgentReservedLocals=_Hm2AgentReservedLocals_Object((1,3,6,1,4,1,248,12,2,17,24),_Hm2AgentReservedLocals_Type())
hm2AgentReservedLocals.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentReservedLocals.setStatus(_A)
_Hm2AgentUniqueNextHops_Type=Gauge32
_Hm2AgentUniqueNextHops_Object=MibScalar
hm2AgentUniqueNextHops=_Hm2AgentUniqueNextHops_Object((1,3,6,1,4,1,248,12,2,17,25),_Hm2AgentUniqueNextHops_Type())
hm2AgentUniqueNextHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUniqueNextHops.setStatus(_A)
_Hm2AgentUniqueNextHopsHigh_Type=Gauge32
_Hm2AgentUniqueNextHopsHigh_Object=MibScalar
hm2AgentUniqueNextHopsHigh=_Hm2AgentUniqueNextHopsHigh_Object((1,3,6,1,4,1,248,12,2,17,26),_Hm2AgentUniqueNextHopsHigh_Type())
hm2AgentUniqueNextHopsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentUniqueNextHopsHigh.setStatus(_A)
_Hm2AgentNextHopGroups_Type=Gauge32
_Hm2AgentNextHopGroups_Object=MibScalar
hm2AgentNextHopGroups=_Hm2AgentNextHopGroups_Object((1,3,6,1,4,1,248,12,2,17,27),_Hm2AgentNextHopGroups_Type())
hm2AgentNextHopGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentNextHopGroups.setStatus(_A)
_Hm2AgentNextHopGroupsHigh_Type=Gauge32
_Hm2AgentNextHopGroupsHigh_Object=MibScalar
hm2AgentNextHopGroupsHigh=_Hm2AgentNextHopGroupsHigh_Object((1,3,6,1,4,1,248,12,2,17,28),_Hm2AgentNextHopGroupsHigh_Type())
hm2AgentNextHopGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentNextHopGroupsHigh.setStatus(_A)
_Hm2AgentEcmpGroups_Type=Gauge32
_Hm2AgentEcmpGroups_Object=MibScalar
hm2AgentEcmpGroups=_Hm2AgentEcmpGroups_Object((1,3,6,1,4,1,248,12,2,17,29),_Hm2AgentEcmpGroups_Type())
hm2AgentEcmpGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentEcmpGroups.setStatus(_A)
_Hm2AgentEcmpGroupsHigh_Type=Gauge32
_Hm2AgentEcmpGroupsHigh_Object=MibScalar
hm2AgentEcmpGroupsHigh=_Hm2AgentEcmpGroupsHigh_Object((1,3,6,1,4,1,248,12,2,17,30),_Hm2AgentEcmpGroupsHigh_Type())
hm2AgentEcmpGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentEcmpGroupsHigh.setStatus(_A)
_Hm2AgentEcmpRoutes_Type=Gauge32
_Hm2AgentEcmpRoutes_Object=MibScalar
hm2AgentEcmpRoutes=_Hm2AgentEcmpRoutes_Object((1,3,6,1,4,1,248,12,2,17,31),_Hm2AgentEcmpRoutes_Type())
hm2AgentEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentEcmpRoutes.setStatus(_A)
_Hm2AgentTruncEcmpRoutes_Type=Gauge32
_Hm2AgentTruncEcmpRoutes_Object=MibScalar
hm2AgentTruncEcmpRoutes=_Hm2AgentTruncEcmpRoutes_Object((1,3,6,1,4,1,248,12,2,17,32),_Hm2AgentTruncEcmpRoutes_Type())
hm2AgentTruncEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentTruncEcmpRoutes.setStatus(_A)
_Hm2AgentEcmpRetries_Type=Counter32
_Hm2AgentEcmpRetries_Object=MibScalar
hm2AgentEcmpRetries=_Hm2AgentEcmpRetries_Object((1,3,6,1,4,1,248,12,2,17,33),_Hm2AgentEcmpRetries_Type())
hm2AgentEcmpRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentEcmpRetries.setStatus(_A)
_Hm2AgentEcmpCountTable_Object=MibTable
hm2AgentEcmpCountTable=_Hm2AgentEcmpCountTable_Object((1,3,6,1,4,1,248,12,2,18))
if mibBuilder.loadTexts:hm2AgentEcmpCountTable.setStatus(_A)
_Hm2AgentEcmpCountEntry_Object=MibTableRow
hm2AgentEcmpCountEntry=_Hm2AgentEcmpCountEntry_Object((1,3,6,1,4,1,248,12,2,18,1))
hm2AgentEcmpCountEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:hm2AgentEcmpCountEntry.setStatus(_A)
class _Hm2AgentEcmpNextHopCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Hm2AgentEcmpNextHopCount_Type.__name__=_I
_Hm2AgentEcmpNextHopCount_Object=MibTableColumn
hm2AgentEcmpNextHopCount=_Hm2AgentEcmpNextHopCount_Object((1,3,6,1,4,1,248,12,2,18,1,1),_Hm2AgentEcmpNextHopCount_Type())
hm2AgentEcmpNextHopCount.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentEcmpNextHopCount.setStatus(_A)
_Hm2AgentEcmpRouteCount_Type=Gauge32
_Hm2AgentEcmpRouteCount_Object=MibTableColumn
hm2AgentEcmpRouteCount=_Hm2AgentEcmpRouteCount_Object((1,3,6,1,4,1,248,12,2,18,1,2),_Hm2AgentEcmpRouteCount_Type())
hm2AgentEcmpRouteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentEcmpRouteCount.setStatus(_A)
_Hm2AgentOspfStubRouterGroup_ObjectIdentity=ObjectIdentity
hm2AgentOspfStubRouterGroup=_Hm2AgentOspfStubRouterGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,19))
class _Hm2AgentOspfStubRouterAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNotAdvertise',1),('advertise',2)))
_Hm2AgentOspfStubRouterAdvertisement_Type.__name__=_D
_Hm2AgentOspfStubRouterAdvertisement_Object=MibScalar
hm2AgentOspfStubRouterAdvertisement=_Hm2AgentOspfStubRouterAdvertisement_Object((1,3,6,1,4,1,248,12,2,19,1),_Hm2AgentOspfStubRouterAdvertisement_Type())
hm2AgentOspfStubRouterAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfStubRouterAdvertisement.setStatus(_A)
class _Hm2AgentOspfStubRouterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('configured',0),('startup',1),('resource-limitation',2)))
_Hm2AgentOspfStubRouterReason_Type.__name__=_D
_Hm2AgentOspfStubRouterReason_Object=MibScalar
hm2AgentOspfStubRouterReason=_Hm2AgentOspfStubRouterReason_Object((1,3,6,1,4,1,248,12,2,19,2),_Hm2AgentOspfStubRouterReason_Type())
hm2AgentOspfStubRouterReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfStubRouterReason.setStatus(_A)
_Hm2AgentOspfStubRouterStartupTimeRemaining_Type=Unsigned32
_Hm2AgentOspfStubRouterStartupTimeRemaining_Object=MibScalar
hm2AgentOspfStubRouterStartupTimeRemaining=_Hm2AgentOspfStubRouterStartupTimeRemaining_Object((1,3,6,1,4,1,248,12,2,19,3),_Hm2AgentOspfStubRouterStartupTimeRemaining_Type())
hm2AgentOspfStubRouterStartupTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfStubRouterStartupTimeRemaining.setStatus(_A)
_Hm2AgentOspfStubRouterDuration_Type=Unsigned32
_Hm2AgentOspfStubRouterDuration_Object=MibScalar
hm2AgentOspfStubRouterDuration=_Hm2AgentOspfStubRouterDuration_Object((1,3,6,1,4,1,248,12,2,19,4),_Hm2AgentOspfStubRouterDuration_Type())
hm2AgentOspfStubRouterDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfStubRouterDuration.setStatus(_A)
_Hm2AgentOspfNbrTable_Object=MibTable
hm2AgentOspfNbrTable=_Hm2AgentOspfNbrTable_Object((1,3,6,1,4,1,248,12,2,249))
if mibBuilder.loadTexts:hm2AgentOspfNbrTable.setStatus(_A)
_Hm2AgentOspfNbrEntry_Object=MibTableRow
hm2AgentOspfNbrEntry=_Hm2AgentOspfNbrEntry_Object((1,3,6,1,4,1,248,12,2,249,1))
if mibBuilder.loadTexts:hm2AgentOspfNbrEntry.setStatus(_A)
_Hm2AgentOspfNbrDeadTime_Type=TimeTicks
_Hm2AgentOspfNbrDeadTime_Object=MibTableColumn
hm2AgentOspfNbrDeadTime=_Hm2AgentOspfNbrDeadTime_Object((1,3,6,1,4,1,248,12,2,249,1,1),_Hm2AgentOspfNbrDeadTime_Type())
hm2AgentOspfNbrDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfNbrDeadTime.setStatus(_A)
_Hm2AgentOspfRouteTable_Object=MibTable
hm2AgentOspfRouteTable=_Hm2AgentOspfRouteTable_Object((1,3,6,1,4,1,248,12,2,250))
if mibBuilder.loadTexts:hm2AgentOspfRouteTable.setStatus(_A)
_Hm2AgentOspfRouteEntry_Object=MibTableRow
hm2AgentOspfRouteEntry=_Hm2AgentOspfRouteEntry_Object((1,3,6,1,4,1,248,12,2,250,1))
hm2AgentOspfRouteEntry.setIndexNames((0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:hm2AgentOspfRouteEntry.setStatus(_A)
_Hm2AgentOspfRouteNet_Type=InetAddressIPv4
_Hm2AgentOspfRouteNet_Object=MibTableColumn
hm2AgentOspfRouteNet=_Hm2AgentOspfRouteNet_Object((1,3,6,1,4,1,248,12,2,250,1,1),_Hm2AgentOspfRouteNet_Type())
hm2AgentOspfRouteNet.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentOspfRouteNet.setStatus(_A)
_Hm2AgentOspfRouteMask_Type=InetAddressIPv4
_Hm2AgentOspfRouteMask_Object=MibTableColumn
hm2AgentOspfRouteMask=_Hm2AgentOspfRouteMask_Object((1,3,6,1,4,1,248,12,2,250,1,2),_Hm2AgentOspfRouteMask_Type())
hm2AgentOspfRouteMask.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentOspfRouteMask.setStatus(_A)
_Hm2AgentOspfRouteCost_Type=Integer32
_Hm2AgentOspfRouteCost_Object=MibTableColumn
hm2AgentOspfRouteCost=_Hm2AgentOspfRouteCost_Object((1,3,6,1,4,1,248,12,2,250,1,3),_Hm2AgentOspfRouteCost_Type())
hm2AgentOspfRouteCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfRouteCost.setStatus(_A)
class _Hm2AgentOspfRouteProtoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('intra',1),('inter',2),('ext-type1',3),('ext-type2',4),('nssa-type1',5),('nssa-type2',6)))
_Hm2AgentOspfRouteProtoType_Type.__name__=_D
_Hm2AgentOspfRouteProtoType_Object=MibTableColumn
hm2AgentOspfRouteProtoType=_Hm2AgentOspfRouteProtoType_Object((1,3,6,1,4,1,248,12,2,250,1,4),_Hm2AgentOspfRouteProtoType_Type())
hm2AgentOspfRouteProtoType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentOspfRouteProtoType.setStatus(_A)
_Hm2AgentVrrpExtGroup_ObjectIdentity=ObjectIdentity
hm2AgentVrrpExtGroup=_Hm2AgentVrrpExtGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,260))
_Hm2AgentVrrpTrackingTable_Object=MibTable
hm2AgentVrrpTrackingTable=_Hm2AgentVrrpTrackingTable_Object((1,3,6,1,4,1,248,12,2,260,1))
if mibBuilder.loadTexts:hm2AgentVrrpTrackingTable.setStatus(_A)
_Hm2AgentVrrpTrackingEntry_Object=MibTableRow
hm2AgentVrrpTrackingEntry=_Hm2AgentVrrpTrackingEntry_Object((1,3,6,1,4,1,248,12,2,260,1,1))
hm2AgentVrrpTrackingEntry.setIndexNames((0,_E,_A8),(0,_E,_A9),(1,_E,_AA))
if mibBuilder.loadTexts:hm2AgentVrrpTrackingEntry.setStatus(_A)
_Hm2AgentVrrpTrackIfIndex_Type=Integer32
_Hm2AgentVrrpTrackIfIndex_Object=MibTableColumn
hm2AgentVrrpTrackIfIndex=_Hm2AgentVrrpTrackIfIndex_Object((1,3,6,1,4,1,248,12,2,260,1,1,1),_Hm2AgentVrrpTrackIfIndex_Type())
hm2AgentVrrpTrackIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentVrrpTrackIfIndex.setStatus(_A)
class _Hm2AgentVrrpTrackVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentVrrpTrackVrid_Type.__name__=_D
_Hm2AgentVrrpTrackVrid_Object=MibTableColumn
hm2AgentVrrpTrackVrid=_Hm2AgentVrrpTrackVrid_Object((1,3,6,1,4,1,248,12,2,260,1,1,2),_Hm2AgentVrrpTrackVrid_Type())
hm2AgentVrrpTrackVrid.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentVrrpTrackVrid.setStatus(_A)
_Hm2AgentVrrpTrackId_Type=SnmpAdminString
_Hm2AgentVrrpTrackId_Object=MibTableColumn
hm2AgentVrrpTrackId=_Hm2AgentVrrpTrackId_Object((1,3,6,1,4,1,248,12,2,260,1,1,3),_Hm2AgentVrrpTrackId_Type())
hm2AgentVrrpTrackId.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentVrrpTrackId.setStatus(_A)
class _Hm2AgentVrrpTrackDecrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,253))
_Hm2AgentVrrpTrackDecrement_Type.__name__=_D
_Hm2AgentVrrpTrackDecrement_Object=MibTableColumn
hm2AgentVrrpTrackDecrement=_Hm2AgentVrrpTrackDecrement_Object((1,3,6,1,4,1,248,12,2,260,1,1,4),_Hm2AgentVrrpTrackDecrement_Type())
hm2AgentVrrpTrackDecrement.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpTrackDecrement.setStatus(_A)
class _Hm2AgentVrrpTrackOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('notReady',3)))
_Hm2AgentVrrpTrackOperStatus_Type.__name__=_D
_Hm2AgentVrrpTrackOperStatus_Object=MibTableColumn
hm2AgentVrrpTrackOperStatus=_Hm2AgentVrrpTrackOperStatus_Object((1,3,6,1,4,1,248,12,2,260,1,1,5),_Hm2AgentVrrpTrackOperStatus_Type())
hm2AgentVrrpTrackOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpTrackOperStatus.setStatus(_A)
_Hm2AgentVrrpTrackRowStatus_Type=RowStatus
_Hm2AgentVrrpTrackRowStatus_Object=MibTableColumn
hm2AgentVrrpTrackRowStatus=_Hm2AgentVrrpTrackRowStatus_Object((1,3,6,1,4,1,248,12,2,260,1,1,6),_Hm2AgentVrrpTrackRowStatus_Type())
hm2AgentVrrpTrackRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentVrrpTrackRowStatus.setStatus(_A)
_Hm2AgentVrrpExtTable_Object=MibTable
hm2AgentVrrpExtTable=_Hm2AgentVrrpExtTable_Object((1,3,6,1,4,1,248,12,2,260,2))
if mibBuilder.loadTexts:hm2AgentVrrpExtTable.setStatus(_A)
_Hm2AgentVrrpExtEntry_Object=MibTableRow
hm2AgentVrrpExtEntry=_Hm2AgentVrrpExtEntry_Object((1,3,6,1,4,1,248,12,2,260,2,1))
hm2AgentVrrpExtEntry.setIndexNames((0,_E,_AB),(0,_E,_AC))
if mibBuilder.loadTexts:hm2AgentVrrpExtEntry.setStatus(_A)
_Hm2AgentVrrpExtIfIndex_Type=Integer32
_Hm2AgentVrrpExtIfIndex_Object=MibTableColumn
hm2AgentVrrpExtIfIndex=_Hm2AgentVrrpExtIfIndex_Object((1,3,6,1,4,1,248,12,2,260,2,1,1),_Hm2AgentVrrpExtIfIndex_Type())
hm2AgentVrrpExtIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentVrrpExtIfIndex.setStatus(_A)
class _Hm2AgentVrrpExtVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hm2AgentVrrpExtVrid_Type.__name__=_D
_Hm2AgentVrrpExtVrid_Object=MibTableColumn
hm2AgentVrrpExtVrid=_Hm2AgentVrrpExtVrid_Object((1,3,6,1,4,1,248,12,2,260,2,1,2),_Hm2AgentVrrpExtVrid_Type())
hm2AgentVrrpExtVrid.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentVrrpExtVrid.setStatus(_A)
class _Hm2AgentVrrpExtDomainId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Hm2AgentVrrpExtDomainId_Type.__name__=_D
_Hm2AgentVrrpExtDomainId_Object=MibTableColumn
hm2AgentVrrpExtDomainId=_Hm2AgentVrrpExtDomainId_Object((1,3,6,1,4,1,248,12,2,260,2,1,3),_Hm2AgentVrrpExtDomainId_Type())
hm2AgentVrrpExtDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtDomainId.setStatus(_A)
class _Hm2AgentVrrpExtDomainRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('member',2),('supervisor',3)))
_Hm2AgentVrrpExtDomainRole_Type.__name__=_D
_Hm2AgentVrrpExtDomainRole_Object=MibTableColumn
hm2AgentVrrpExtDomainRole=_Hm2AgentVrrpExtDomainRole_Object((1,3,6,1,4,1,248,12,2,260,2,1,4),_Hm2AgentVrrpExtDomainRole_Type())
hm2AgentVrrpExtDomainRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtDomainRole.setStatus(_A)
class _Hm2AgentVrrpExtDomainStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noError',1),(_AD,2),(_AE,3)))
_Hm2AgentVrrpExtDomainStatus_Type.__name__=_D
_Hm2AgentVrrpExtDomainStatus_Object=MibTableColumn
hm2AgentVrrpExtDomainStatus=_Hm2AgentVrrpExtDomainStatus_Object((1,3,6,1,4,1,248,12,2,260,2,1,5),_Hm2AgentVrrpExtDomainStatus_Type())
hm2AgentVrrpExtDomainStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpExtDomainStatus.setStatus(_A)
class _Hm2AgentVrrpExtAdvertAddress_Type(IpAddress):defaultHexValue='E0000012'
_Hm2AgentVrrpExtAdvertAddress_Type.__name__=_S
_Hm2AgentVrrpExtAdvertAddress_Object=MibTableColumn
hm2AgentVrrpExtAdvertAddress=_Hm2AgentVrrpExtAdvertAddress_Object((1,3,6,1,4,1,248,12,2,260,2,1,6),_Hm2AgentVrrpExtAdvertAddress_Type())
hm2AgentVrrpExtAdvertAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtAdvertAddress.setStatus(_A)
class _Hm2AgentVrrpExtAdvertTimer_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,255000))
_Hm2AgentVrrpExtAdvertTimer_Type.__name__=_D
_Hm2AgentVrrpExtAdvertTimer_Object=MibTableColumn
hm2AgentVrrpExtAdvertTimer=_Hm2AgentVrrpExtAdvertTimer_Object((1,3,6,1,4,1,248,12,2,260,2,1,7),_Hm2AgentVrrpExtAdvertTimer_Type())
hm2AgentVrrpExtAdvertTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtAdvertTimer.setStatus(_A)
if mibBuilder.loadTexts:hm2AgentVrrpExtAdvertTimer.setUnits(_K)
class _Hm2AgentVrrpExtCfgPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_Hm2AgentVrrpExtCfgPriority_Type.__name__=_D
_Hm2AgentVrrpExtCfgPriority_Object=MibTableColumn
hm2AgentVrrpExtCfgPriority=_Hm2AgentVrrpExtCfgPriority_Object((1,3,6,1,4,1,248,12,2,260,2,1,8),_Hm2AgentVrrpExtCfgPriority_Type())
hm2AgentVrrpExtCfgPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtCfgPriority.setStatus(_A)
class _Hm2AgentVrrpExtNotifyAddress_Type(IpAddress):defaultHexValue='00000000'
_Hm2AgentVrrpExtNotifyAddress_Type.__name__=_S
_Hm2AgentVrrpExtNotifyAddress_Object=MibTableColumn
hm2AgentVrrpExtNotifyAddress=_Hm2AgentVrrpExtNotifyAddress_Object((1,3,6,1,4,1,248,12,2,260,2,1,9),_Hm2AgentVrrpExtNotifyAddress_Type())
hm2AgentVrrpExtNotifyAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtNotifyAddress.setStatus(_A)
class _Hm2AgentVrrpExtNotifyLinkdown_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentVrrpExtNotifyLinkdown_Type.__name__=_F
_Hm2AgentVrrpExtNotifyLinkdown_Object=MibTableColumn
hm2AgentVrrpExtNotifyLinkdown=_Hm2AgentVrrpExtNotifyLinkdown_Object((1,3,6,1,4,1,248,12,2,260,2,1,10),_Hm2AgentVrrpExtNotifyLinkdown_Type())
hm2AgentVrrpExtNotifyLinkdown.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtNotifyLinkdown.setStatus(_A)
class _Hm2AgentVrrpExtPreemptionDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2AgentVrrpExtPreemptionDelay_Type.__name__=_D
_Hm2AgentVrrpExtPreemptionDelay_Object=MibTableColumn
hm2AgentVrrpExtPreemptionDelay=_Hm2AgentVrrpExtPreemptionDelay_Object((1,3,6,1,4,1,248,12,2,260,2,1,11),_Hm2AgentVrrpExtPreemptionDelay_Type())
hm2AgentVrrpExtPreemptionDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtPreemptionDelay.setStatus(_A)
_Hm2AgentVrrpPrimaryVirtualAddress_Type=IpAddress
_Hm2AgentVrrpPrimaryVirtualAddress_Object=MibTableColumn
hm2AgentVrrpPrimaryVirtualAddress=_Hm2AgentVrrpPrimaryVirtualAddress_Object((1,3,6,1,4,1,248,12,2,260,2,1,12),_Hm2AgentVrrpPrimaryVirtualAddress_Type())
hm2AgentVrrpPrimaryVirtualAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpPrimaryVirtualAddress.setStatus(_A)
class _Hm2AgentVrrpExtMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('config',2),('ttdp',3)))
_Hm2AgentVrrpExtMethod_Type.__name__=_D
_Hm2AgentVrrpExtMethod_Object=MibTableColumn
hm2AgentVrrpExtMethod=_Hm2AgentVrrpExtMethod_Object((1,3,6,1,4,1,248,12,2,260,2,1,13),_Hm2AgentVrrpExtMethod_Type())
hm2AgentVrrpExtMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtMethod.setStatus(_A)
class _Hm2AgentVrrpExtProxyarp_Type(TruthValue):defaultValue=2
_Hm2AgentVrrpExtProxyarp_Type.__name__=_J
_Hm2AgentVrrpExtProxyarp_Object=MibTableColumn
hm2AgentVrrpExtProxyarp=_Hm2AgentVrrpExtProxyarp_Object((1,3,6,1,4,1,248,12,2,260,2,1,14),_Hm2AgentVrrpExtProxyarp_Type())
hm2AgentVrrpExtProxyarp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpExtProxyarp.setStatus(_A)
_Hm2AgentVrrpDomainTable_Object=MibTable
hm2AgentVrrpDomainTable=_Hm2AgentVrrpDomainTable_Object((1,3,6,1,4,1,248,12,2,260,3))
if mibBuilder.loadTexts:hm2AgentVrrpDomainTable.setStatus(_A)
_Hm2AgentVrrpDomainEntry_Object=MibTableRow
hm2AgentVrrpDomainEntry=_Hm2AgentVrrpDomainEntry_Object((1,3,6,1,4,1,248,12,2,260,3,1))
hm2AgentVrrpDomainEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:hm2AgentVrrpDomainEntry.setStatus(_A)
class _Hm2AgentVrrpDomainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_Hm2AgentVrrpDomainId_Type.__name__=_D
_Hm2AgentVrrpDomainId_Object=MibTableColumn
hm2AgentVrrpDomainId=_Hm2AgentVrrpDomainId_Object((1,3,6,1,4,1,248,12,2,260,3,1,1),_Hm2AgentVrrpDomainId_Type())
hm2AgentVrrpDomainId.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentVrrpDomainId.setStatus(_A)
class _Hm2AgentVrrpDomainMemberSendAdv_Type(HmEnabledStatus):defaultValue=2
_Hm2AgentVrrpDomainMemberSendAdv_Type.__name__=_F
_Hm2AgentVrrpDomainMemberSendAdv_Object=MibTableColumn
hm2AgentVrrpDomainMemberSendAdv=_Hm2AgentVrrpDomainMemberSendAdv_Object((1,3,6,1,4,1,248,12,2,260,3,1,2),_Hm2AgentVrrpDomainMemberSendAdv_Type())
hm2AgentVrrpDomainMemberSendAdv.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentVrrpDomainMemberSendAdv.setStatus(_A)
class _Hm2AgentVrrpDomainStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noError',1),(_AD,2),(_AE,3)))
_Hm2AgentVrrpDomainStatus_Type.__name__=_D
_Hm2AgentVrrpDomainStatus_Object=MibTableColumn
hm2AgentVrrpDomainStatus=_Hm2AgentVrrpDomainStatus_Object((1,3,6,1,4,1,248,12,2,260,3,1,3),_Hm2AgentVrrpDomainStatus_Type())
hm2AgentVrrpDomainStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpDomainStatus.setStatus(_A)
_Hm2AgentVrrpDomainSupervisorIfIndex_Type=Integer32
_Hm2AgentVrrpDomainSupervisorIfIndex_Object=MibTableColumn
hm2AgentVrrpDomainSupervisorIfIndex=_Hm2AgentVrrpDomainSupervisorIfIndex_Object((1,3,6,1,4,1,248,12,2,260,3,1,4),_Hm2AgentVrrpDomainSupervisorIfIndex_Type())
hm2AgentVrrpDomainSupervisorIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpDomainSupervisorIfIndex.setStatus(_A)
class _Hm2AgentVrrpDomainSupervisorVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentVrrpDomainSupervisorVrid_Type.__name__=_D
_Hm2AgentVrrpDomainSupervisorVrid_Object=MibTableColumn
hm2AgentVrrpDomainSupervisorVrid=_Hm2AgentVrrpDomainSupervisorVrid_Object((1,3,6,1,4,1,248,12,2,260,3,1,5),_Hm2AgentVrrpDomainSupervisorVrid_Type())
hm2AgentVrrpDomainSupervisorVrid.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpDomainSupervisorVrid.setStatus(_A)
class _Hm2AgentVrrpDomainOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2AgentVrrpDomainOperPriority_Type.__name__=_D
_Hm2AgentVrrpDomainOperPriority_Object=MibTableColumn
hm2AgentVrrpDomainOperPriority=_Hm2AgentVrrpDomainOperPriority_Object((1,3,6,1,4,1,248,12,2,260,3,1,6),_Hm2AgentVrrpDomainOperPriority_Type())
hm2AgentVrrpDomainOperPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpDomainOperPriority.setStatus(_A)
class _Hm2AgentVrrpDomainSupervisorOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3),('unknown',4)))
_Hm2AgentVrrpDomainSupervisorOperState_Type.__name__=_D
_Hm2AgentVrrpDomainSupervisorOperState_Object=MibTableColumn
hm2AgentVrrpDomainSupervisorOperState=_Hm2AgentVrrpDomainSupervisorOperState_Object((1,3,6,1,4,1,248,12,2,260,3,1,7),_Hm2AgentVrrpDomainSupervisorOperState_Type())
hm2AgentVrrpDomainSupervisorOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentVrrpDomainSupervisorOperState.setStatus(_A)
_Hm2AgentNeighbourGroup_ObjectIdentity=ObjectIdentity
hm2AgentNeighbourGroup=_Hm2AgentNeighbourGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,270))
_Hm2AgentStaticNeighbourTable_Object=MibTable
hm2AgentStaticNeighbourTable=_Hm2AgentStaticNeighbourTable_Object((1,3,6,1,4,1,248,12,2,270,10))
if mibBuilder.loadTexts:hm2AgentStaticNeighbourTable.setStatus(_A)
_Hm2AgentStaticNeighbourEntry_Object=MibTableRow
hm2AgentStaticNeighbourEntry=_Hm2AgentStaticNeighbourEntry_Object((1,3,6,1,4,1,248,12,2,270,10,1))
hm2AgentStaticNeighbourEntry.setIndexNames((0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:hm2AgentStaticNeighbourEntry.setStatus(_A)
_Hm2AgentStaticNeighbourAddressType_Type=InetAddressType
_Hm2AgentStaticNeighbourAddressType_Object=MibTableColumn
hm2AgentStaticNeighbourAddressType=_Hm2AgentStaticNeighbourAddressType_Object((1,3,6,1,4,1,248,12,2,270,10,1,1),_Hm2AgentStaticNeighbourAddressType_Type())
hm2AgentStaticNeighbourAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentStaticNeighbourAddressType.setStatus(_A)
class _Hm2AgentStaticNeighbourAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_Hm2AgentStaticNeighbourAddress_Type.__name__=_R
_Hm2AgentStaticNeighbourAddress_Object=MibTableColumn
hm2AgentStaticNeighbourAddress=_Hm2AgentStaticNeighbourAddress_Object((1,3,6,1,4,1,248,12,2,270,10,1,2),_Hm2AgentStaticNeighbourAddress_Type())
hm2AgentStaticNeighbourAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentStaticNeighbourAddress.setStatus(_A)
class _Hm2AgentStaticNeighbourPhysAddress_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_Hm2AgentStaticNeighbourPhysAddress_Type.__name__=_Y
_Hm2AgentStaticNeighbourPhysAddress_Object=MibTableColumn
hm2AgentStaticNeighbourPhysAddress=_Hm2AgentStaticNeighbourPhysAddress_Object((1,3,6,1,4,1,248,12,2,270,10,1,3),_Hm2AgentStaticNeighbourPhysAddress_Type())
hm2AgentStaticNeighbourPhysAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentStaticNeighbourPhysAddress.setStatus(_A)
_Hm2AgentStaticNeighbourIfIndex_Type=InterfaceIndexOrZero
_Hm2AgentStaticNeighbourIfIndex_Object=MibTableColumn
hm2AgentStaticNeighbourIfIndex=_Hm2AgentStaticNeighbourIfIndex_Object((1,3,6,1,4,1,248,12,2,270,10,1,4),_Hm2AgentStaticNeighbourIfIndex_Type())
hm2AgentStaticNeighbourIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentStaticNeighbourIfIndex.setStatus(_A)
_Hm2AgentStaticNeighbourRowStatus_Type=RowStatus
_Hm2AgentStaticNeighbourRowStatus_Object=MibTableColumn
hm2AgentStaticNeighbourRowStatus=_Hm2AgentStaticNeighbourRowStatus_Object((1,3,6,1,4,1,248,12,2,270,10,1,5),_Hm2AgentStaticNeighbourRowStatus_Type())
hm2AgentStaticNeighbourRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentStaticNeighbourRowStatus.setStatus(_A)
_Hm2AgentDynamicNeighbourTable_Object=MibTable
hm2AgentDynamicNeighbourTable=_Hm2AgentDynamicNeighbourTable_Object((1,3,6,1,4,1,248,12,2,270,11))
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourTable.setStatus(_A)
_Hm2AgentDynamicNeighbourEntry_Object=MibTableRow
hm2AgentDynamicNeighbourEntry=_Hm2AgentDynamicNeighbourEntry_Object((1,3,6,1,4,1,248,12,2,270,11,1))
hm2AgentDynamicNeighbourEntry.setIndexNames((0,_E,_AI),(0,_E,_AJ))
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourEntry.setStatus(_A)
_Hm2AgentDynamicNeighbourAddressType_Type=InetAddressType
_Hm2AgentDynamicNeighbourAddressType_Object=MibTableColumn
hm2AgentDynamicNeighbourAddressType=_Hm2AgentDynamicNeighbourAddressType_Object((1,3,6,1,4,1,248,12,2,270,11,1,1),_Hm2AgentDynamicNeighbourAddressType_Type())
hm2AgentDynamicNeighbourAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourAddressType.setStatus(_A)
class _Hm2AgentDynamicNeighbourAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_Hm2AgentDynamicNeighbourAddress_Type.__name__=_R
_Hm2AgentDynamicNeighbourAddress_Object=MibTableColumn
hm2AgentDynamicNeighbourAddress=_Hm2AgentDynamicNeighbourAddress_Object((1,3,6,1,4,1,248,12,2,270,11,1,2),_Hm2AgentDynamicNeighbourAddress_Type())
hm2AgentDynamicNeighbourAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourAddress.setStatus(_A)
class _Hm2AgentDynamicNeighbourPhysAddress_Type(PhysAddress):subtypeSpec=PhysAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_Hm2AgentDynamicNeighbourPhysAddress_Type.__name__=_Y
_Hm2AgentDynamicNeighbourPhysAddress_Object=MibTableColumn
hm2AgentDynamicNeighbourPhysAddress=_Hm2AgentDynamicNeighbourPhysAddress_Object((1,3,6,1,4,1,248,12,2,270,11,1,3),_Hm2AgentDynamicNeighbourPhysAddress_Type())
hm2AgentDynamicNeighbourPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourPhysAddress.setStatus(_A)
_Hm2AgentDynamicNeighbourIfIndex_Type=InterfaceIndexOrZero
_Hm2AgentDynamicNeighbourIfIndex_Object=MibTableColumn
hm2AgentDynamicNeighbourIfIndex=_Hm2AgentDynamicNeighbourIfIndex_Object((1,3,6,1,4,1,248,12,2,270,11,1,4),_Hm2AgentDynamicNeighbourIfIndex_Type())
hm2AgentDynamicNeighbourIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourIfIndex.setStatus(_A)
class _Hm2AgentDynamicNeighbourAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('delete',2),(_T,3)))
_Hm2AgentDynamicNeighbourAction_Type.__name__=_D
_Hm2AgentDynamicNeighbourAction_Object=MibTableColumn
hm2AgentDynamicNeighbourAction=_Hm2AgentDynamicNeighbourAction_Object((1,3,6,1,4,1,248,12,2,270,11,1,5),_Hm2AgentDynamicNeighbourAction_Type())
hm2AgentDynamicNeighbourAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentDynamicNeighbourAction.setStatus(_A)
_Hm2AgentRoutingSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2AgentRoutingSNMPExtensionGroup=_Hm2AgentRoutingSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,12,2,280))
_Hm2AgentIpHelperTableFullErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentIpHelperTableFullErrorReturn=_Hm2AgentIpHelperTableFullErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,1))
if mibBuilder.loadTexts:hm2AgentIpHelperTableFullErrorReturn.setStatus(_A)
_Hm2AgentIpHelperInvalidServerAddrErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentIpHelperInvalidServerAddrErrorReturn=_Hm2AgentIpHelperInvalidServerAddrErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,2))
if mibBuilder.loadTexts:hm2AgentIpHelperInvalidServerAddrErrorReturn.setStatus(_A)
_Hm2AgentRouterOspfDependenciesNotMet_ObjectIdentity=ObjectIdentity
hm2AgentRouterOspfDependenciesNotMet=_Hm2AgentRouterOspfDependenciesNotMet_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,3))
if mibBuilder.loadTexts:hm2AgentRouterOspfDependenciesNotMet.setStatus(_A)
_Hm2AgentRouterOspfRangeTableFullErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentRouterOspfRangeTableFullErrorReturn=_Hm2AgentRouterOspfRangeTableFullErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,4))
if mibBuilder.loadTexts:hm2AgentRouterOspfRangeTableFullErrorReturn.setStatus(_A)
_Hm2AgentRouterOspfVirtNbrTableFullErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentRouterOspfVirtNbrTableFullErrorReturn=_Hm2AgentRouterOspfVirtNbrTableFullErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,5))
if mibBuilder.loadTexts:hm2AgentRouterOspfVirtNbrTableFullErrorReturn.setStatus(_A)
_Hm2AgentRouterRIPDependenciesNotMet_ObjectIdentity=ObjectIdentity
hm2AgentRouterRIPDependenciesNotMet=_Hm2AgentRouterRIPDependenciesNotMet_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,8))
if mibBuilder.loadTexts:hm2AgentRouterRIPDependenciesNotMet.setStatus(_A)
_Hm2AgentIpHelperInvalidUdpPortErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentIpHelperInvalidUdpPortErrorReturn=_Hm2AgentIpHelperInvalidUdpPortErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,9))
if mibBuilder.loadTexts:hm2AgentIpHelperInvalidUdpPortErrorReturn.setStatus(_A)
_Hm2AgentStaticNeighbourTableFullErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentStaticNeighbourTableFullErrorReturn=_Hm2AgentStaticNeighbourTableFullErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,10))
if mibBuilder.loadTexts:hm2AgentStaticNeighbourTableFullErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrNoPrimaryErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrNoPrimaryErrorReturn=_Hm2AgentSecondaryAddrNoPrimaryErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,11))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrNoPrimaryErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrDifferentPrimaryErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrDifferentPrimaryErrorReturn=_Hm2AgentSecondaryAddrDifferentPrimaryErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,12))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrDifferentPrimaryErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrWrongIpClassErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrWrongIpClassErrorReturn=_Hm2AgentSecondaryAddrWrongIpClassErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,13))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrWrongIpClassErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrWrongSubnetErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrWrongSubnetErrorReturn=_Hm2AgentSecondaryAddrWrongSubnetErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,14))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrWrongSubnetErrorReturn.setStatus(_L)
_Hm2AgentSecondaryAddrMaxIntfEntriesErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrMaxIntfEntriesErrorReturn=_Hm2AgentSecondaryAddrMaxIntfEntriesErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,15))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrMaxIntfEntriesErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrMaxSystemEntriesErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrMaxSystemEntriesErrorReturn=_Hm2AgentSecondaryAddrMaxSystemEntriesErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,16))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrMaxSystemEntriesErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrStaticRouteErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrStaticRouteErrorReturn=_Hm2AgentSecondaryAddrStaticRouteErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,17))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrStaticRouteErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrStaticARPErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrStaticARPErrorReturn=_Hm2AgentSecondaryAddrStaticARPErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,18))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrStaticARPErrorReturn.setStatus(_A)
_Hm2AgentSecondaryAddrAbsentEntryErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSecondaryAddrAbsentEntryErrorReturn=_Hm2AgentSecondaryAddrAbsentEntryErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,19))
if mibBuilder.loadTexts:hm2AgentSecondaryAddrAbsentEntryErrorReturn.setStatus(_A)
_Hm2AgentPrimaryAddrWrongIpClassErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrWrongIpClassErrorReturn=_Hm2AgentPrimaryAddrWrongIpClassErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,20))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrWrongIpClassErrorReturn.setStatus(_A)
_Hm2AgentPrimaryAddrConflictErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrConflictErrorReturn=_Hm2AgentPrimaryAddrConflictErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,21))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrConflictErrorReturn.setStatus(_L)
_Hm2AgentPrimaryAddrStaticRouteErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrStaticRouteErrorReturn=_Hm2AgentPrimaryAddrStaticRouteErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,22))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrStaticRouteErrorReturn.setStatus(_A)
_Hm2AgentPrimaryAddrStaticARPErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrStaticARPErrorReturn=_Hm2AgentPrimaryAddrStaticARPErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,23))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrStaticARPErrorReturn.setStatus(_A)
_Hm2AgentPrimaryAddrExistingSecondaryErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrExistingSecondaryErrorReturn=_Hm2AgentPrimaryAddrExistingSecondaryErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,24))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrExistingSecondaryErrorReturn.setStatus(_A)
_Hm2AgentPrimaryAddrNetworkConflictErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrNetworkConflictErrorReturn=_Hm2AgentPrimaryAddrNetworkConflictErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,25))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrNetworkConflictErrorReturn.setStatus(_L)
_Hm2AgentPrimaryAddrRoutingTableFullErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentPrimaryAddrRoutingTableFullErrorReturn=_Hm2AgentPrimaryAddrRoutingTableFullErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,26))
if mibBuilder.loadTexts:hm2AgentPrimaryAddrRoutingTableFullErrorReturn.setStatus(_A)
_Hm2AgentDstAddrHostBitSetErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentDstAddrHostBitSetErrorReturn=_Hm2AgentDstAddrHostBitSetErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,27))
if mibBuilder.loadTexts:hm2AgentDstAddrHostBitSetErrorReturn.setStatus(_A)
_Hm2AgentSamePrefRouteErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSamePrefRouteErrorReturn=_Hm2AgentSamePrefRouteErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,28))
if mibBuilder.loadTexts:hm2AgentSamePrefRouteErrorReturn.setStatus(_A)
_Hm2AgentVrrpAssoIpAddrRowStatusInconsistentAddress_ObjectIdentity=ObjectIdentity
hm2AgentVrrpAssoIpAddrRowStatusInconsistentAddress=_Hm2AgentVrrpAssoIpAddrRowStatusInconsistentAddress_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,29))
if mibBuilder.loadTexts:hm2AgentVrrpAssoIpAddrRowStatusInconsistentAddress.setStatus(_A)
_Hm2AgentVrrpAssoIpAddrRowStatusInvalidAddress_ObjectIdentity=ObjectIdentity
hm2AgentVrrpAssoIpAddrRowStatusInvalidAddress=_Hm2AgentVrrpAssoIpAddrRowStatusInvalidAddress_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,30))
if mibBuilder.loadTexts:hm2AgentVrrpAssoIpAddrRowStatusInvalidAddress.setStatus(_A)
_Hm2AgentVrrpAssoIpAddrRowStatusUnknownVRID_ObjectIdentity=ObjectIdentity
hm2AgentVrrpAssoIpAddrRowStatusUnknownVRID=_Hm2AgentVrrpAssoIpAddrRowStatusUnknownVRID_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,31))
if mibBuilder.loadTexts:hm2AgentVrrpAssoIpAddrRowStatusUnknownVRID.setStatus(_A)
_Hm2AgentSwitchIpRouterDiscMinMaxAdvtIntErrorRtrn_ObjectIdentity=ObjectIdentity
hm2AgentSwitchIpRouterDiscMinMaxAdvtIntErrorRtrn=_Hm2AgentSwitchIpRouterDiscMinMaxAdvtIntErrorRtrn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,32))
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscMinMaxAdvtIntErrorRtrn.setStatus(_A)
_Hm2AgentSwitchIpRouterDiscLifeTimeMaxAdvIntErrorRtrn_ObjectIdentity=ObjectIdentity
hm2AgentSwitchIpRouterDiscLifeTimeMaxAdvIntErrorRtrn=_Hm2AgentSwitchIpRouterDiscLifeTimeMaxAdvIntErrorRtrn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,33))
if mibBuilder.loadTexts:hm2AgentSwitchIpRouterDiscLifeTimeMaxAdvIntErrorRtrn.setStatus(_A)
_Hm2AgentSwitchIpIcmpRateLimitExceedingRatioErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentSwitchIpIcmpRateLimitExceedingRatioErrorReturn=_Hm2AgentSwitchIpIcmpRateLimitExceedingRatioErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,34))
if mibBuilder.loadTexts:hm2AgentSwitchIpIcmpRateLimitExceedingRatioErrorReturn.setStatus(_A)
_Hm2AgentRouterOspfMaxAreaErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentRouterOspfMaxAreaErrorReturn=_Hm2AgentRouterOspfMaxAreaErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,35))
if mibBuilder.loadTexts:hm2AgentRouterOspfMaxAreaErrorReturn.setStatus(_A)
_Hm2AgentospfRouterIdChange_ObjectIdentity=ObjectIdentity
hm2AgentospfRouterIdChange=_Hm2AgentospfRouterIdChange_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,36))
if mibBuilder.loadTexts:hm2AgentospfRouterIdChange.setStatus(_A)
_Hm2AgentOspfRedistDistList_ObjectIdentity=ObjectIdentity
hm2AgentOspfRedistDistList=_Hm2AgentOspfRedistDistList_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,37))
if mibBuilder.loadTexts:hm2AgentOspfRedistDistList.setStatus(_A)
_Hm2AgentOspfDefaultAreaDeleteErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentOspfDefaultAreaDeleteErrorReturn=_Hm2AgentOspfDefaultAreaDeleteErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,38))
if mibBuilder.loadTexts:hm2AgentOspfDefaultAreaDeleteErrorReturn.setStatus(_A)
_Hm2AgentLocalArpDeleteErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentLocalArpDeleteErrorReturn=_Hm2AgentLocalArpDeleteErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,39))
if mibBuilder.loadTexts:hm2AgentLocalArpDeleteErrorReturn.setStatus(_A)
_Hm2AgentDynamicVlanRoutingErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentDynamicVlanRoutingErrorReturn=_Hm2AgentDynamicVlanRoutingErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,40))
if mibBuilder.loadTexts:hm2AgentDynamicVlanRoutingErrorReturn.setStatus(_A)
_Hm2AgentVlanUnawareRoutingErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentVlanUnawareRoutingErrorReturn=_Hm2AgentVlanUnawareRoutingErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,41))
if mibBuilder.loadTexts:hm2AgentVlanUnawareRoutingErrorReturn.setStatus(_A)
_Hm2AgentRoutingInvalidNetworkAddress_ObjectIdentity=ObjectIdentity
hm2AgentRoutingInvalidNetworkAddress=_Hm2AgentRoutingInvalidNetworkAddress_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,42))
if mibBuilder.loadTexts:hm2AgentRoutingInvalidNetworkAddress.setStatus(_A)
_Hm2AgentRoutingTypeInvalidValue_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTypeInvalidValue=_Hm2AgentRoutingTypeInvalidValue_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,43))
if mibBuilder.loadTexts:hm2AgentRoutingTypeInvalidValue.setStatus(_A)
_Hm2AgentRoutingLocalRoutePreference_ObjectIdentity=ObjectIdentity
hm2AgentRoutingLocalRoutePreference=_Hm2AgentRoutingLocalRoutePreference_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,44))
if mibBuilder.loadTexts:hm2AgentRoutingLocalRoutePreference.setStatus(_A)
_Hm2AgentRoutingMetricInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingMetricInvalid=_Hm2AgentRoutingMetricInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,45))
if mibBuilder.loadTexts:hm2AgentRoutingMetricInvalid.setStatus(_A)
_Hm2AgentRoutingMetricNotSupported_ObjectIdentity=ObjectIdentity
hm2AgentRoutingMetricNotSupported=_Hm2AgentRoutingMetricNotSupported_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,46))
if mibBuilder.loadTexts:hm2AgentRoutingMetricNotSupported.setStatus(_A)
_Hm2AgentRoutingNexthopAtLocalInterface_ObjectIdentity=ObjectIdentity
hm2AgentRoutingNexthopAtLocalInterface=_Hm2AgentRoutingNexthopAtLocalInterface_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,47))
if mibBuilder.loadTexts:hm2AgentRoutingNexthopAtLocalInterface.setStatus(_A)
_Hm2AgentRoutingNexthopInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingNexthopInvalid=_Hm2AgentRoutingNexthopInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,48))
if mibBuilder.loadTexts:hm2AgentRoutingNexthopInvalid.setStatus(_A)
_Hm2AgentRoutingMaxEntryCountReached_ObjectIdentity=ObjectIdentity
hm2AgentRoutingMaxEntryCountReached=_Hm2AgentRoutingMaxEntryCountReached_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,49))
if mibBuilder.loadTexts:hm2AgentRoutingMaxEntryCountReached.setStatus(_A)
_Hm2AgentRoutingNoPreferenceUpdate_ObjectIdentity=ObjectIdentity
hm2AgentRoutingNoPreferenceUpdate=_Hm2AgentRoutingNoPreferenceUpdate_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,50))
if mibBuilder.loadTexts:hm2AgentRoutingNoPreferenceUpdate.setStatus(_A)
_Hm2AgentRoutingPortInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingPortInvalid=_Hm2AgentRoutingPortInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,51))
if mibBuilder.loadTexts:hm2AgentRoutingPortInvalid.setStatus(_A)
_Hm2AgentRoutingStaticRoutePreference_ObjectIdentity=ObjectIdentity
hm2AgentRoutingStaticRoutePreference=_Hm2AgentRoutingStaticRoutePreference_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,52))
if mibBuilder.loadTexts:hm2AgentRoutingStaticRoutePreference.setStatus(_A)
_Hm2AgentRoutingSameNetworkAddrErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentRoutingSameNetworkAddrErrorReturn=_Hm2AgentRoutingSameNetworkAddrErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,53))
if mibBuilder.loadTexts:hm2AgentRoutingSameNetworkAddrErrorReturn.setStatus(_A)
_Hm2AgentRoutingTypeInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTypeInvalid=_Hm2AgentRoutingTypeInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,54))
if mibBuilder.loadTexts:hm2AgentRoutingTypeInvalid.setStatus(_A)
_Hm2AgentRoutingMacAddressInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingMacAddressInvalid=_Hm2AgentRoutingMacAddressInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,55))
if mibBuilder.loadTexts:hm2AgentRoutingMacAddressInvalid.setStatus(_A)
_Hm2AgentRoutingIPAddressExist_ObjectIdentity=ObjectIdentity
hm2AgentRoutingIPAddressExist=_Hm2AgentRoutingIPAddressExist_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,56))
if mibBuilder.loadTexts:hm2AgentRoutingIPAddressExist.setStatus(_A)
_Hm2AgentRoutingPingPortInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingPingPortInvalid=_Hm2AgentRoutingPingPortInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,57))
if mibBuilder.loadTexts:hm2AgentRoutingPingPortInvalid.setStatus(_A)
_Hm2AgentRoutingIntervalTimeInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingIntervalTimeInvalid=_Hm2AgentRoutingIntervalTimeInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,58))
if mibBuilder.loadTexts:hm2AgentRoutingIntervalTimeInvalid.setStatus(_A)
_Hm2AgentRoutingPingLoseTimeInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingPingLoseTimeInvalid=_Hm2AgentRoutingPingLoseTimeInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,59))
if mibBuilder.loadTexts:hm2AgentRoutingPingLoseTimeInvalid.setStatus(_A)
_Hm2AgentRoutingPingReceiveTimeInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingPingReceiveTimeInvalid=_Hm2AgentRoutingPingReceiveTimeInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,60))
if mibBuilder.loadTexts:hm2AgentRoutingPingReceiveTimeInvalid.setStatus(_A)
_Hm2AgentRoutingPingTimeoutInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingPingTimeoutInvalid=_Hm2AgentRoutingPingTimeoutInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,61))
if mibBuilder.loadTexts:hm2AgentRoutingPingTimeoutInvalid.setStatus(_A)
_Hm2AgentRoutingPingTTLInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingPingTTLInvalid=_Hm2AgentRoutingPingTTLInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,62))
if mibBuilder.loadTexts:hm2AgentRoutingPingTTLInvalid.setStatus(_A)
_Hm2AgentRoutingLogicalOperandInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingLogicalOperandInvalid=_Hm2AgentRoutingLogicalOperandInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,63))
if mibBuilder.loadTexts:hm2AgentRoutingLogicalOperandInvalid.setStatus(_A)
_Hm2AgentRoutingOperatorInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingOperatorInvalid=_Hm2AgentRoutingOperatorInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,64))
if mibBuilder.loadTexts:hm2AgentRoutingOperatorInvalid.setStatus(_A)
_Hm2AgentRoutingLinkDelayInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingLinkDelayInvalid=_Hm2AgentRoutingLinkDelayInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,65))
if mibBuilder.loadTexts:hm2AgentRoutingLinkDelayInvalid.setStatus(_A)
_Hm2AgentRoutingL3RelayFunctionInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingL3RelayFunctionInvalid=_Hm2AgentRoutingL3RelayFunctionInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,66))
if mibBuilder.loadTexts:hm2AgentRoutingL3RelayFunctionInvalid.setStatus(_A)
_Hm2AgentRoutingBootpDhcpHopsInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingBootpDhcpHopsInvalid=_Hm2AgentRoutingBootpDhcpHopsInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,67))
if mibBuilder.loadTexts:hm2AgentRoutingBootpDhcpHopsInvalid.setStatus(_A)
_Hm2AgentRoutingBootpDhcpWaitTimeInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingBootpDhcpWaitTimeInvalid=_Hm2AgentRoutingBootpDhcpWaitTimeInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,68))
if mibBuilder.loadTexts:hm2AgentRoutingBootpDhcpWaitTimeInvalid.setStatus(_A)
_Hm2AgentRoutingCircuitIDInvalid_ObjectIdentity=ObjectIdentity
hm2AgentRoutingCircuitIDInvalid=_Hm2AgentRoutingCircuitIDInvalid_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,69))
if mibBuilder.loadTexts:hm2AgentRoutingCircuitIDInvalid.setStatus(_A)
_Hm2AgentRoutingTrackTypeEnableError_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTrackTypeEnableError=_Hm2AgentRoutingTrackTypeEnableError_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,70))
if mibBuilder.loadTexts:hm2AgentRoutingTrackTypeEnableError.setStatus(_A)
_Hm2AgentRoutingTrackingEnableErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTrackingEnableErrorReturn=_Hm2AgentRoutingTrackingEnableErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,71))
if mibBuilder.loadTexts:hm2AgentRoutingTrackingEnableErrorReturn.setStatus(_A)
_Hm2AgentRoutingTrackingDisableErrorReturn_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTrackingDisableErrorReturn=_Hm2AgentRoutingTrackingDisableErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,72))
if mibBuilder.loadTexts:hm2AgentRoutingTrackingDisableErrorReturn.setStatus(_A)
_Hm2AgentRoutingTrackTypeDisableError_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTrackTypeDisableError=_Hm2AgentRoutingTrackTypeDisableError_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,73))
if mibBuilder.loadTexts:hm2AgentRoutingTrackTypeDisableError.setStatus(_A)
_Hm2AgentRoutingTrackIDCreateError_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTrackIDCreateError=_Hm2AgentRoutingTrackIDCreateError_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,74))
if mibBuilder.loadTexts:hm2AgentRoutingTrackIDCreateError.setStatus(_A)
_Hm2AgentRoutingTrackTypeCreateError_ObjectIdentity=ObjectIdentity
hm2AgentRoutingTrackTypeCreateError=_Hm2AgentRoutingTrackTypeCreateError_ObjectIdentity((1,3,6,1,4,1,248,12,2,280,75))
if mibBuilder.loadTexts:hm2AgentRoutingTrackTypeCreateError.setStatus(_A)
rip2IfConfEntry.registerAugmentions((_E,_AK))
hm2AgentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_E,_AL))
hm2AgentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_E,_AM))
hm2AgentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfAreaEntry.registerAugmentions((_E,_AN))
hm2AgentOspfAreaNSSAEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfMetricEntry.registerAugmentions((_E,_AO))
hm2AgentOspfIfMetricEntry.setIndexNames(*ospfIfMetricEntry.getIndexNames())
ospfNbrEntry.registerAugmentions((_E,_AP))
hm2AgentOspfNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'hm2PlatformRouting':hm2PlatformRouting,'hm2AgentSwitchArpGroup':hm2AgentSwitchArpGroup,'hm2AgentSwitchArpAgeoutTime':hm2AgentSwitchArpAgeoutTime,'hm2AgentSwitchArpResponseTime':hm2AgentSwitchArpResponseTime,'hm2AgentSwitchArpMaxRetries':hm2AgentSwitchArpMaxRetries,'hm2AgentSwitchArpCacheSize':hm2AgentSwitchArpCacheSize,'hm2AgentSwitchArpDynamicRenew':hm2AgentSwitchArpDynamicRenew,'hm2AgentSwitchArpTotalEntryCountCurrent':hm2AgentSwitchArpTotalEntryCountCurrent,'hm2AgentSwitchArpTotalEntryCountPeak':hm2AgentSwitchArpTotalEntryCountPeak,'hm2AgentSwitchArpStaticEntryCountCurrent':hm2AgentSwitchArpStaticEntryCountCurrent,'hm2AgentSwitchArpStaticEntryCountMax':hm2AgentSwitchArpStaticEntryCountMax,'hm2AgentSwitchLocalProxyArpTable':hm2AgentSwitchLocalProxyArpTable,'hm2AgentSwitchLocalProxyArpEntry':hm2AgentSwitchLocalProxyArpEntry,'hm2AgentSwitchLocalProxyArpMode':hm2AgentSwitchLocalProxyArpMode,'hm2AgentSwitchIntfArpTable':hm2AgentSwitchIntfArpTable,'hm2AgentSwitchIntfArpEntry':hm2AgentSwitchIntfArpEntry,_c:hm2AgentSwitchIntfArpIpAddress,_d:hm2AgentSwitchIntfArpIfIndex,'hm2AgentSwitchIntfArpAge':hm2AgentSwitchIntfArpAge,'hm2AgentSwitchIntfArpMacAddress':hm2AgentSwitchIntfArpMacAddress,'hm2AgentSwitchIntfArpType':hm2AgentSwitchIntfArpType,'hm2AgentSwitchIntfArpStatus':hm2AgentSwitchIntfArpStatus,'hm2AgentSwitchArpSparseLearn':hm2AgentSwitchArpSparseLearn,'hm2AgentSwitchArpCacheClear':hm2AgentSwitchArpCacheClear,'hm2AgentSwitchProxyArpMaxResponseDelay':hm2AgentSwitchProxyArpMaxResponseDelay,'hm2AgentSwitchIpGroup':hm2AgentSwitchIpGroup,'hm2AgentSwitchIpRoutingMode':hm2AgentSwitchIpRoutingMode,'hm2AgentSwitchIpDefaultGateway':hm2AgentSwitchIpDefaultGateway,'hm2AgentSwitchIpInterfaceTable':hm2AgentSwitchIpInterfaceTable,'hm2AgentSwitchIpInterfaceEntry':hm2AgentSwitchIpInterfaceEntry,_U:hm2AgentSwitchIpInterfaceIfIndex,'hm2AgentSwitchIPAddressConfigMethod':hm2AgentSwitchIPAddressConfigMethod,'hm2AgentSwitchIpInterfaceIpAddress':hm2AgentSwitchIpInterfaceIpAddress,'hm2AgentSwitchIpInterfaceNetMask':hm2AgentSwitchIpInterfaceNetMask,'hm2AgentSwitchIpInterfaceClearIp':hm2AgentSwitchIpInterfaceClearIp,'hm2AgentSwitchIpInterfaceRoutingMode':hm2AgentSwitchIpInterfaceRoutingMode,'hm2AgentSwitchIpInterfaceProxyARPMode':hm2AgentSwitchIpInterfaceProxyARPMode,'hm2AgentSwitchIpInterfaceMtuValue':hm2AgentSwitchIpInterfaceMtuValue,'hm2AgentSwitchIpInterfaceBandwidth':hm2AgentSwitchIpInterfaceBandwidth,'hm2AgentSwitchIpInterfaceUnnumberedIfIndex':hm2AgentSwitchIpInterfaceUnnumberedIfIndex,'hm2AgentSwitchIpInterfaceIcmpUnreachables':hm2AgentSwitchIpInterfaceIcmpUnreachables,'hm2AgentSwitchIpInterfaceIcmpRedirects':hm2AgentSwitchIpInterfaceIcmpRedirects,'hm2AgentSwitchDhcpOperation':hm2AgentSwitchDhcpOperation,'hm2AgentSwitchIpInterfaceSuppressed':hm2AgentSwitchIpInterfaceSuppressed,'hm2AgentSwitchIpInterfaceNumberOfFlaps':hm2AgentSwitchIpInterfaceNumberOfFlaps,'hm2AgentSwitchIpInterfaceCurrentPenalty':hm2AgentSwitchIpInterfaceCurrentPenalty,'hm2AgentSwitchIpInterfaceReUseTime':hm2AgentSwitchIpInterfaceReUseTime,'hm2AgentSwitchIpInterfaceNetdirectedBCMode':hm2AgentSwitchIpInterfaceNetdirectedBCMode,'hm2AgentSwitchIpRouterDiscoveryTable':hm2AgentSwitchIpRouterDiscoveryTable,'hm2AgentSwitchIpRouterDiscoveryEntry':hm2AgentSwitchIpRouterDiscoveryEntry,_e:hm2AgentSwitchIpRouterDiscoveryIfIndex,'hm2AgentSwitchIpRouterDiscoveryAdvertiseMode':hm2AgentSwitchIpRouterDiscoveryAdvertiseMode,'hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval':hm2AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval,'hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval':hm2AgentSwitchIpRouterDiscoveryMinAdvertisementInterval,'hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime':hm2AgentSwitchIpRouterDiscoveryAdvertisementLifetime,'hm2AgentSwitchIpRouterDiscoveryPreferenceLevel':hm2AgentSwitchIpRouterDiscoveryPreferenceLevel,'hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress':hm2AgentSwitchIpRouterDiscoveryAdvertisementAddress,'hm2AgentSwitchIpVlanTable':hm2AgentSwitchIpVlanTable,'hm2AgentSwitchIpVlanEntry':hm2AgentSwitchIpVlanEntry,_f:hm2AgentSwitchIpVlanId,'hm2AgentSwitchIpVlanIfIndex':hm2AgentSwitchIpVlanIfIndex,'hm2AgentSwitchIpVlanRoutingStatus':hm2AgentSwitchIpVlanRoutingStatus,'hm2AgentSwitchSecondaryAddressTable':hm2AgentSwitchSecondaryAddressTable,'hm2AgentSwitchSecondaryAddressEntry':hm2AgentSwitchSecondaryAddressEntry,_g:hm2AgentSwitchSecondaryIpAddress,'hm2AgentSwitchSecondaryNetMask':hm2AgentSwitchSecondaryNetMask,'hm2AgentSwitchSecondaryStatus':hm2AgentSwitchSecondaryStatus,'hm2AgentSwitchIpIcmpControlGroup':hm2AgentSwitchIpIcmpControlGroup,'hm2AgentSwitchIpIcmpEchoReplyMode':hm2AgentSwitchIpIcmpEchoReplyMode,'hm2AgentSwitchIpIcmpRedirectsMode':hm2AgentSwitchIpIcmpRedirectsMode,'hm2AgentSwitchIpIcmpRateLimitInterval':hm2AgentSwitchIpIcmpRateLimitInterval,'hm2AgentSwitchIpIcmpRateLimitBurstSize':hm2AgentSwitchIpIcmpRateLimitBurstSize,'hm2AgentSwitchIntfIpHelperAddressTable':hm2AgentSwitchIntfIpHelperAddressTable,'hm2AgentSwitchIntfIpHelperAddressEntry':hm2AgentSwitchIntfIpHelperAddressEntry,_h:hm2AgentSwitchIntfIpHelperUdpPort,_i:hm2AgentSwitchIntfIpHelperIpAddress,'hm2AgentSwitchIntfIpHelperHitCount':hm2AgentSwitchIntfIpHelperHitCount,'hm2AgentSwitchIntfIpHelperStatus':hm2AgentSwitchIntfIpHelperStatus,'hm2AgentSwitchClearIpDefaultGateway':hm2AgentSwitchClearIpDefaultGateway,'hm2AgentSwitchIpFirstActiveAddressType':hm2AgentSwitchIpFirstActiveAddressType,'hm2AgentSwitchIpFirstActiveAddress':hm2AgentSwitchIpFirstActiveAddress,'hm2AgentSwitchIpStaticDefaultPref':hm2AgentSwitchIpStaticDefaultPref,'hm2AgentSwitchIpRouteCount':hm2AgentSwitchIpRouteCount,'hm2AgentSwitchIpBestRouteCount':hm2AgentSwitchIpBestRouteCount,'hm2AgentSwitchIpSourceRoutingMode':hm2AgentSwitchIpSourceRoutingMode,'hm2AgentRouterRipConfigGroup':hm2AgentRouterRipConfigGroup,'hm2AgentRouterRipAdminState':hm2AgentRouterRipAdminState,'hm2AgentRouterRipSplitHorizonMode':hm2AgentRouterRipSplitHorizonMode,'hm2AgentRouterRipAutoSummaryMode':hm2AgentRouterRipAutoSummaryMode,'hm2AgentRouterRipHostRoutesAcceptMode':hm2AgentRouterRipHostRoutesAcceptMode,'hm2AgentRouterRipDefaultMetric':hm2AgentRouterRipDefaultMetric,'hm2AgentRouterRipDefaultMetricConfigured':hm2AgentRouterRipDefaultMetricConfigured,'hm2AgentRouterRipDefaultInfoOriginate':hm2AgentRouterRipDefaultInfoOriginate,'hm2AgentRipRouteRedistTable':hm2AgentRipRouteRedistTable,'hm2AgentRipRouteRedistEntry':hm2AgentRipRouteRedistEntry,_j:hm2AgentRipRouteRedistSource,'hm2AgentRipRouteRedistMode':hm2AgentRipRouteRedistMode,'hm2AgentRipRouteRedistMetric':hm2AgentRipRouteRedistMetric,'hm2AgentRipRouteRedistMetricConfigured':hm2AgentRipRouteRedistMetricConfigured,'hm2AgentRipRouteRedistMatchInternal':hm2AgentRipRouteRedistMatchInternal,'hm2AgentRipRouteRedistMatchExternal1':hm2AgentRipRouteRedistMatchExternal1,'hm2AgentRipRouteRedistMatchExternal2':hm2AgentRipRouteRedistMatchExternal2,'hm2AgentRipRouteRedistMatchNSSAExternal1':hm2AgentRipRouteRedistMatchNSSAExternal1,'hm2AgentRipRouteRedistMatchNSSAExternal2':hm2AgentRipRouteRedistMatchNSSAExternal2,'hm2AgentRipRouteRedistDistList':hm2AgentRipRouteRedistDistList,'hm2AgentRipRouteRedistDistListConfigured':hm2AgentRipRouteRedistDistListConfigured,'hm2AgentRip2IfConfTable':hm2AgentRip2IfConfTable,_AK:hm2AgentRip2IfConfEntry,'hm2AgentRip2IfConfAuthKeyId':hm2AgentRip2IfConfAuthKeyId,'hm2AgentRouterRipRoutePref':hm2AgentRouterRipRoutePref,'hm2AgentRouterRipUpdateTimerInterval':hm2AgentRouterRipUpdateTimerInterval,'hm2AgentRouterOspfConfigGroup':hm2AgentRouterOspfConfigGroup,'hm2AgentOspfDefaultMetric':hm2AgentOspfDefaultMetric,'hm2AgentOspfDefaultMetricConfigured':hm2AgentOspfDefaultMetricConfigured,'hm2AgentOspfDefaultInfoOriginate':hm2AgentOspfDefaultInfoOriginate,'hm2AgentOspfDefaultInfoOriginateAlways':hm2AgentOspfDefaultInfoOriginateAlways,'hm2AgentOspfDefaultInfoOriginateMetric':hm2AgentOspfDefaultInfoOriginateMetric,'hm2AgentOspfDefaultInfoOriginateMetricConfigured':hm2AgentOspfDefaultInfoOriginateMetricConfigured,'hm2AgentOspfDefaultInfoOriginateMetricType':hm2AgentOspfDefaultInfoOriginateMetricType,'hm2AgentOspfRouteRedistTable':hm2AgentOspfRouteRedistTable,'hm2AgentOspfRouteRedistEntry':hm2AgentOspfRouteRedistEntry,_n:hm2AgentOspfRouteRedistSource,'hm2AgentOspfRouteRedistMode':hm2AgentOspfRouteRedistMode,'hm2AgentOspfRouteRedistMetric':hm2AgentOspfRouteRedistMetric,'hm2AgentOspfRouteRedistMetricConfigured':hm2AgentOspfRouteRedistMetricConfigured,'hm2AgentOspfRouteRedistMetricType':hm2AgentOspfRouteRedistMetricType,'hm2AgentOspfRouteRedistTag':hm2AgentOspfRouteRedistTag,'hm2AgentOspfRouteRedistSubnets':hm2AgentOspfRouteRedistSubnets,'hm2AgentOspfRouteRedistDistList':hm2AgentOspfRouteRedistDistList,'hm2AgentOspfRouteRedistDistListConfigured':hm2AgentOspfRouteRedistDistListConfigured,'hm2AgentOspfIfTable':hm2AgentOspfIfTable,_AL:hm2AgentOspfIfEntry,'hm2AgentOspfIfAuthKeyId':hm2AgentOspfIfAuthKeyId,'hm2AgentOspfIfIpMtuIgnoreFlag':hm2AgentOspfIfIpMtuIgnoreFlag,'hm2AgentOspfIfPassiveMode':hm2AgentOspfIfPassiveMode,'hm2AgentOspfIfAdvertiseSecondaries':hm2AgentOspfIfAdvertiseSecondaries,'hm2AgentOspfIfFastHelloMode':hm2AgentOspfIfFastHelloMode,'hm2AgentOspfVirtIfTable':hm2AgentOspfVirtIfTable,_AM:hm2AgentOspfVirtIfEntry,'hm2AgentOspfVirtIfAuthKeyId':hm2AgentOspfVirtIfAuthKeyId,'hm2AgentRouterOspfRFC1583CompatibilityMode':hm2AgentRouterOspfRFC1583CompatibilityMode,'hm2AgentOspfSpfDelayTime':hm2AgentOspfSpfDelayTime,'hm2AgentOspfSpfHoldTime':hm2AgentOspfSpfHoldTime,'hm2AgentOspfAutoCostRefBw':hm2AgentOspfAutoCostRefBw,'hm2AgentOspfOpaqueLsaSupport':hm2AgentOspfOpaqueLsaSupport,'hm2AgentOspfAreaOpaqueLsdbTable':hm2AgentOspfAreaOpaqueLsdbTable,'hm2AgentOspfAreaOpaqueLsdbEntry':hm2AgentOspfAreaOpaqueLsdbEntry,_o:hm2AgentOspfAreaOpaqueLsdbAreaId,_p:hm2AgentOspfAreaOpaqueLsdbType,_q:hm2AgentOspfAreaOpaqueLsdbLsid,_r:hm2AgentOspfAreaOpaqueLsdbRouterId,'hm2AgentOspfAreaOpaqueLsdbSequence':hm2AgentOspfAreaOpaqueLsdbSequence,'hm2AgentOspfAreaOpaqueLsdbAge':hm2AgentOspfAreaOpaqueLsdbAge,'hm2AgentOspfAreaOpaqueLsdbChecksum':hm2AgentOspfAreaOpaqueLsdbChecksum,'hm2AgentOspfAreaOpaqueLsdbAdvertisement':hm2AgentOspfAreaOpaqueLsdbAdvertisement,'hm2AgentOspfLocalLsdbTable':hm2AgentOspfLocalLsdbTable,'hm2AgentOspfLocalLsdbEntry':hm2AgentOspfLocalLsdbEntry,_s:hm2AgentOspfLocalLsdbIpAddress,_t:hm2AgentOspfLocalLsdbAddressLessIf,_u:hm2AgentOspfLocalLsdbType,_v:hm2AgentOspfLocalLsdbLsid,_w:hm2AgentOspfLocalLsdbRouterId,'hm2AgentOspfLocalLsdbSequence':hm2AgentOspfLocalLsdbSequence,'hm2AgentOspfLocalLsdbAge':hm2AgentOspfLocalLsdbAge,'hm2AgentOspfLocalLsdbChecksum':hm2AgentOspfLocalLsdbChecksum,'hm2AgentOspfLocalLsdbAdvertisement':hm2AgentOspfLocalLsdbAdvertisement,'hm2AgentOspfAsLsdbTable':hm2AgentOspfAsLsdbTable,'hm2AgentOspfAsLsdbEntry':hm2AgentOspfAsLsdbEntry,_x:hm2AgentOspfAsLsdbType,_y:hm2AgentOspfAsLsdbLsid,_z:hm2AgentOspfAsLsdbRouterId,'hm2AgentOspfAsLsdbSequence':hm2AgentOspfAsLsdbSequence,'hm2AgentOspfAsLsdbAge':hm2AgentOspfAsLsdbAge,'hm2AgentOspfAsLsdbChecksum':hm2AgentOspfAsLsdbChecksum,'hm2AgentOspfAsLsdbAdvertisement':hm2AgentOspfAsLsdbAdvertisement,'hm2AgentOspfDefaultPassiveMode':hm2AgentOspfDefaultPassiveMode,'hm2AgentOspfRoutePrefIntraArea':hm2AgentOspfRoutePrefIntraArea,'hm2AgentOspfRoutePrefInterArea':hm2AgentOspfRoutePrefInterArea,'hm2AgentOspfRoutePrefExternal':hm2AgentOspfRoutePrefExternal,'hm2AgentOspfAreaNSSATable':hm2AgentOspfAreaNSSATable,_AN:hm2AgentOspfAreaNSSAEntry,'hm2AgentOspfAreaNSSAImportSummaries':hm2AgentOspfAreaNSSAImportSummaries,'hm2AgentOspfAreaNSSARedistribute':hm2AgentOspfAreaNSSARedistribute,'hm2AgentOspfAreaNSSADefaultInfoOriginate':hm2AgentOspfAreaNSSADefaultInfoOriginate,'hm2AgentOspfAreaNSSADefaultMetric':hm2AgentOspfAreaNSSADefaultMetric,'hm2AgentOspfAreaNSSADefaultMetricType':hm2AgentOspfAreaNSSADefaultMetricType,'hm2AgentOspfIfMetricTable':hm2AgentOspfIfMetricTable,_AO:hm2AgentOspfIfMetricEntry,'hm2AgentOspfIfMetricCalculatedCost':hm2AgentOspfIfMetricCalculatedCost,'hm2AgentSnmpTrapFlagsConfigGroupLayer3':hm2AgentSnmpTrapFlagsConfigGroupLayer3,'hm2AgentSnmpVRRPNewMasterTrapFlag':hm2AgentSnmpVRRPNewMasterTrapFlag,'hm2AgentSnmpVRRPAuthFailureTrapFlag':hm2AgentSnmpVRRPAuthFailureTrapFlag,'hm2AgentBootpDhcpRelayGroup':hm2AgentBootpDhcpRelayGroup,'hm2AgentBootpDhcpRelayMaxHopCount':hm2AgentBootpDhcpRelayMaxHopCount,'hm2AgentBootpDhcpRelayMinWaitTime':hm2AgentBootpDhcpRelayMinWaitTime,'hm2AgentBootpDhcpRelayCircuitIdOptionMode':hm2AgentBootpDhcpRelayCircuitIdOptionMode,'hm2AgentECMPGroup':hm2AgentECMPGroup,'hm2AgentECMPOspfMaxPaths':hm2AgentECMPOspfMaxPaths,'hm2AgentRouterVrrpConfigGroup':hm2AgentRouterVrrpConfigGroup,'hm2AgentRouterVrrpAdminState':hm2AgentRouterVrrpAdminState,'hm2AgentVrrpOperations':hm2AgentVrrpOperations,'hm2AgentRouterVrrpOperTable':hm2AgentRouterVrrpOperTable,'hm2AgentRouterVrrpOperEntry':hm2AgentRouterVrrpOperEntry,'hm2AgentRouterVrrpOperPriority':hm2AgentRouterVrrpOperPriority,'hm2AgentRouterVrrpNumberOfFastInst':hm2AgentRouterVrrpNumberOfFastInst,'hm2AgentIpHelperGroup':hm2AgentIpHelperGroup,'hm2AgentIpHelperAdminMode':hm2AgentIpHelperAdminMode,'hm2AgentDhcpClientMsgsReceived':hm2AgentDhcpClientMsgsReceived,'hm2AgentDhcpClientMsgsRelayed':hm2AgentDhcpClientMsgsRelayed,'hm2AgentDhcpServerMsgsReceived':hm2AgentDhcpServerMsgsReceived,'hm2AgentDhcpServerMsgsRelayed':hm2AgentDhcpServerMsgsRelayed,'hm2AgentUdpClientMsgsReceived':hm2AgentUdpClientMsgsReceived,'hm2AgentUdpClientMsgsRelayed':hm2AgentUdpClientMsgsRelayed,'hm2AgentSwitchIpHelperAddressTable':hm2AgentSwitchIpHelperAddressTable,'hm2AgentSwitchIpHelperAddressEntry':hm2AgentSwitchIpHelperAddressEntry,_A0:hm2AgentSwitchIpHelperUdpPort,_A1:hm2AgentSwitchIpHelperAddress,'hm2AgentSwitchIpHelperHitCount':hm2AgentSwitchIpHelperHitCount,'hm2AgentSwitchIpHelperStatus':hm2AgentSwitchIpHelperStatus,'hm2AgentUdpClientMsgsTtlExpired':hm2AgentUdpClientMsgsTtlExpired,'hm2AgentUdpClientMsgsDiscarded':hm2AgentUdpClientMsgsDiscarded,'hm2AgentInternalVlanGroup':hm2AgentInternalVlanGroup,'hm2AgentInternalVlanBase':hm2AgentInternalVlanBase,'hm2AgentInternalVlanPolicy':hm2AgentInternalVlanPolicy,'hm2AgentSwitchInternalVlanTable':hm2AgentSwitchInternalVlanTable,'hm2AgentSwitchInternalVlanEntry':hm2AgentSwitchInternalVlanEntry,_A2:hm2AgentSwitchInternalVlanId,'hm2AgentSwitchInternalVlanIfIndex':hm2AgentSwitchInternalVlanIfIndex,'hm2AgentOspfQueueGroup':hm2AgentOspfQueueGroup,'hm2AgentOspfQueueTable':hm2AgentOspfQueueTable,'hm2AgentOspfQueueEntry':hm2AgentOspfQueueEntry,_A3:hm2AgentOspfQueueIndex,'hm2AgentOspfQueueName':hm2AgentOspfQueueName,'hm2AgentOspfQueueLength':hm2AgentOspfQueueLength,'hm2AgentOspfQueueHigh':hm2AgentOspfQueueHigh,'hm2AgentOspfQueueDrops':hm2AgentOspfQueueDrops,'hm2AgentOspfQueueLimit':hm2AgentOspfQueueLimit,'hm2AgentOspfPacketStatsGroup':hm2AgentOspfPacketStatsGroup,'hm2AgentOspfCountersCleared':hm2AgentOspfCountersCleared,'hm2AgentOspfLsaRetxCount':hm2AgentOspfLsaRetxCount,'hm2AgentOspfHellosRx':hm2AgentOspfHellosRx,'hm2AgentOspfHellosTx':hm2AgentOspfHellosTx,'hm2AgentOspfDdRx':hm2AgentOspfDdRx,'hm2AgentOspfDdTx':hm2AgentOspfDdTx,'hm2AgentOspfLsReqRx':hm2AgentOspfLsReqRx,'hm2AgentOspfLsReqTx':hm2AgentOspfLsReqTx,'hm2AgentOspfLsUpdatesRx':hm2AgentOspfLsUpdatesRx,'hm2AgentOspfLsUpdatesTx':hm2AgentOspfLsUpdatesTx,'hm2AgentOspfLsAckRx':hm2AgentOspfLsAckRx,'hm2AgentOspfLsAckTx':hm2AgentOspfLsAckTx,'hm2AgentOspfLsUpdatesRxMax':hm2AgentOspfLsUpdatesRxMax,'hm2AgentOspfLsUpdatesTxMax':hm2AgentOspfLsUpdatesTxMax,'hm2AgentOspfType1LsasRx':hm2AgentOspfType1LsasRx,'hm2AgentOspfType2LsasRx':hm2AgentOspfType2LsasRx,'hm2AgentOspfType3LsasRx':hm2AgentOspfType3LsasRx,'hm2AgentOspfType4LsasRx':hm2AgentOspfType4LsasRx,'hm2AgentOspfType5LsasRx':hm2AgentOspfType5LsasRx,'hm2AgentOspfType7LsasRx':hm2AgentOspfType7LsasRx,'hm2AgentOspfType9LsasRx':hm2AgentOspfType9LsasRx,'hm2AgentOspfType10LsasRx':hm2AgentOspfType10LsasRx,'hm2AgentOspfType11LsasRx':hm2AgentOspfType11LsasRx,'hm2AgentOspfSpfStatsTable':hm2AgentOspfSpfStatsTable,'hm2AgentOspfSpfStatsEntry':hm2AgentOspfSpfStatsEntry,_A4:hm2AgentOspfSpfIndex,'hm2AgentOspfSpfStatsDeltaT':hm2AgentOspfSpfStatsDeltaT,'hm2AgentOspfSpfStatsIntra':hm2AgentOspfSpfStatsIntra,'hm2AgentOspfSpfStatsSumm':hm2AgentOspfSpfStatsSumm,'hm2AgentOspfSpfStatsExt':hm2AgentOspfSpfStatsExt,'hm2AgentOspfSpfStatsSpfTotal':hm2AgentOspfSpfStatsSpfTotal,'hm2AgentOspfSpfStatsRibUpdate':hm2AgentOspfSpfStatsRibUpdate,'hm2AgentOspfSpfStatsReason':hm2AgentOspfSpfStatsReason,'hm2AgentRoutingHeapGroup':hm2AgentRoutingHeapGroup,'hm2AgentRoutingHeapSize':hm2AgentRoutingHeapSize,'hm2AgentRoutingHeapInUse':hm2AgentRoutingHeapInUse,'hm2AgentRoutingHeapHigh':hm2AgentRoutingHeapHigh,'hm2AgentRoutingTableSummaryGroup':hm2AgentRoutingTableSummaryGroup,'hm2AgentConnectedRoutes':hm2AgentConnectedRoutes,'hm2AgentStaticRoutes':hm2AgentStaticRoutes,'hm2AgentRipRoutes':hm2AgentRipRoutes,'hm2AgentOspfRoutes':hm2AgentOspfRoutes,'hm2AgentOspfIntraRoutes':hm2AgentOspfIntraRoutes,'hm2AgentOspfInterRoutes':hm2AgentOspfInterRoutes,'hm2AgentOspfExt1Routes':hm2AgentOspfExt1Routes,'hm2AgentOspfExt2Routes':hm2AgentOspfExt2Routes,'hm2AgentBgpRoutes':hm2AgentBgpRoutes,'hm2AgentEbgpRoutes':hm2AgentEbgpRoutes,'hm2AgentIbgpRoutes':hm2AgentIbgpRoutes,'hm2AgentLocalBgpRoutes':hm2AgentLocalBgpRoutes,'hm2AgentRejectRoutes':hm2AgentRejectRoutes,'hm2AgentTotalRoutes':hm2AgentTotalRoutes,'hm2AgentBestRoutes':hm2AgentBestRoutes,'hm2AgentBestRoutesHigh':hm2AgentBestRoutesHigh,'hm2AgentAlternateRoutes':hm2AgentAlternateRoutes,'hm2AgentRouteAdds':hm2AgentRouteAdds,'hm2AgentRouteModifies':hm2AgentRouteModifies,'hm2AgentRouteDeletes':hm2AgentRouteDeletes,'hm2AgentUnresolvedRouteAdds':hm2AgentUnresolvedRouteAdds,'hm2AgentInvalidRouteAdds':hm2AgentInvalidRouteAdds,'hm2AgentFailedRouteAdds':hm2AgentFailedRouteAdds,'hm2AgentReservedLocals':hm2AgentReservedLocals,'hm2AgentUniqueNextHops':hm2AgentUniqueNextHops,'hm2AgentUniqueNextHopsHigh':hm2AgentUniqueNextHopsHigh,'hm2AgentNextHopGroups':hm2AgentNextHopGroups,'hm2AgentNextHopGroupsHigh':hm2AgentNextHopGroupsHigh,'hm2AgentEcmpGroups':hm2AgentEcmpGroups,'hm2AgentEcmpGroupsHigh':hm2AgentEcmpGroupsHigh,'hm2AgentEcmpRoutes':hm2AgentEcmpRoutes,'hm2AgentTruncEcmpRoutes':hm2AgentTruncEcmpRoutes,'hm2AgentEcmpRetries':hm2AgentEcmpRetries,'hm2AgentEcmpCountTable':hm2AgentEcmpCountTable,'hm2AgentEcmpCountEntry':hm2AgentEcmpCountEntry,_A5:hm2AgentEcmpNextHopCount,'hm2AgentEcmpRouteCount':hm2AgentEcmpRouteCount,'hm2AgentOspfStubRouterGroup':hm2AgentOspfStubRouterGroup,'hm2AgentOspfStubRouterAdvertisement':hm2AgentOspfStubRouterAdvertisement,'hm2AgentOspfStubRouterReason':hm2AgentOspfStubRouterReason,'hm2AgentOspfStubRouterStartupTimeRemaining':hm2AgentOspfStubRouterStartupTimeRemaining,'hm2AgentOspfStubRouterDuration':hm2AgentOspfStubRouterDuration,'hm2AgentOspfNbrTable':hm2AgentOspfNbrTable,_AP:hm2AgentOspfNbrEntry,'hm2AgentOspfNbrDeadTime':hm2AgentOspfNbrDeadTime,'hm2AgentOspfRouteTable':hm2AgentOspfRouteTable,'hm2AgentOspfRouteEntry':hm2AgentOspfRouteEntry,_A6:hm2AgentOspfRouteNet,_A7:hm2AgentOspfRouteMask,'hm2AgentOspfRouteCost':hm2AgentOspfRouteCost,'hm2AgentOspfRouteProtoType':hm2AgentOspfRouteProtoType,'hm2AgentVrrpExtGroup':hm2AgentVrrpExtGroup,'hm2AgentVrrpTrackingTable':hm2AgentVrrpTrackingTable,'hm2AgentVrrpTrackingEntry':hm2AgentVrrpTrackingEntry,_A8:hm2AgentVrrpTrackIfIndex,_A9:hm2AgentVrrpTrackVrid,_AA:hm2AgentVrrpTrackId,'hm2AgentVrrpTrackDecrement':hm2AgentVrrpTrackDecrement,'hm2AgentVrrpTrackOperStatus':hm2AgentVrrpTrackOperStatus,'hm2AgentVrrpTrackRowStatus':hm2AgentVrrpTrackRowStatus,'hm2AgentVrrpExtTable':hm2AgentVrrpExtTable,'hm2AgentVrrpExtEntry':hm2AgentVrrpExtEntry,_AB:hm2AgentVrrpExtIfIndex,_AC:hm2AgentVrrpExtVrid,'hm2AgentVrrpExtDomainId':hm2AgentVrrpExtDomainId,'hm2AgentVrrpExtDomainRole':hm2AgentVrrpExtDomainRole,'hm2AgentVrrpExtDomainStatus':hm2AgentVrrpExtDomainStatus,'hm2AgentVrrpExtAdvertAddress':hm2AgentVrrpExtAdvertAddress,'hm2AgentVrrpExtAdvertTimer':hm2AgentVrrpExtAdvertTimer,'hm2AgentVrrpExtCfgPriority':hm2AgentVrrpExtCfgPriority,'hm2AgentVrrpExtNotifyAddress':hm2AgentVrrpExtNotifyAddress,'hm2AgentVrrpExtNotifyLinkdown':hm2AgentVrrpExtNotifyLinkdown,'hm2AgentVrrpExtPreemptionDelay':hm2AgentVrrpExtPreemptionDelay,'hm2AgentVrrpPrimaryVirtualAddress':hm2AgentVrrpPrimaryVirtualAddress,'hm2AgentVrrpExtMethod':hm2AgentVrrpExtMethod,'hm2AgentVrrpExtProxyarp':hm2AgentVrrpExtProxyarp,'hm2AgentVrrpDomainTable':hm2AgentVrrpDomainTable,'hm2AgentVrrpDomainEntry':hm2AgentVrrpDomainEntry,_AF:hm2AgentVrrpDomainId,'hm2AgentVrrpDomainMemberSendAdv':hm2AgentVrrpDomainMemberSendAdv,'hm2AgentVrrpDomainStatus':hm2AgentVrrpDomainStatus,'hm2AgentVrrpDomainSupervisorIfIndex':hm2AgentVrrpDomainSupervisorIfIndex,'hm2AgentVrrpDomainSupervisorVrid':hm2AgentVrrpDomainSupervisorVrid,'hm2AgentVrrpDomainOperPriority':hm2AgentVrrpDomainOperPriority,'hm2AgentVrrpDomainSupervisorOperState':hm2AgentVrrpDomainSupervisorOperState,'hm2AgentNeighbourGroup':hm2AgentNeighbourGroup,'hm2AgentStaticNeighbourTable':hm2AgentStaticNeighbourTable,'hm2AgentStaticNeighbourEntry':hm2AgentStaticNeighbourEntry,_AG:hm2AgentStaticNeighbourAddressType,_AH:hm2AgentStaticNeighbourAddress,'hm2AgentStaticNeighbourPhysAddress':hm2AgentStaticNeighbourPhysAddress,'hm2AgentStaticNeighbourIfIndex':hm2AgentStaticNeighbourIfIndex,'hm2AgentStaticNeighbourRowStatus':hm2AgentStaticNeighbourRowStatus,'hm2AgentDynamicNeighbourTable':hm2AgentDynamicNeighbourTable,'hm2AgentDynamicNeighbourEntry':hm2AgentDynamicNeighbourEntry,_AI:hm2AgentDynamicNeighbourAddressType,_AJ:hm2AgentDynamicNeighbourAddress,'hm2AgentDynamicNeighbourPhysAddress':hm2AgentDynamicNeighbourPhysAddress,'hm2AgentDynamicNeighbourIfIndex':hm2AgentDynamicNeighbourIfIndex,'hm2AgentDynamicNeighbourAction':hm2AgentDynamicNeighbourAction,'hm2AgentRoutingSNMPExtensionGroup':hm2AgentRoutingSNMPExtensionGroup,'hm2AgentIpHelperTableFullErrorReturn':hm2AgentIpHelperTableFullErrorReturn,'hm2AgentIpHelperInvalidServerAddrErrorReturn':hm2AgentIpHelperInvalidServerAddrErrorReturn,'hm2AgentRouterOspfDependenciesNotMet':hm2AgentRouterOspfDependenciesNotMet,'hm2AgentRouterOspfRangeTableFullErrorReturn':hm2AgentRouterOspfRangeTableFullErrorReturn,'hm2AgentRouterOspfVirtNbrTableFullErrorReturn':hm2AgentRouterOspfVirtNbrTableFullErrorReturn,'hm2AgentRouterRIPDependenciesNotMet':hm2AgentRouterRIPDependenciesNotMet,'hm2AgentIpHelperInvalidUdpPortErrorReturn':hm2AgentIpHelperInvalidUdpPortErrorReturn,'hm2AgentStaticNeighbourTableFullErrorReturn':hm2AgentStaticNeighbourTableFullErrorReturn,'hm2AgentSecondaryAddrNoPrimaryErrorReturn':hm2AgentSecondaryAddrNoPrimaryErrorReturn,'hm2AgentSecondaryAddrDifferentPrimaryErrorReturn':hm2AgentSecondaryAddrDifferentPrimaryErrorReturn,'hm2AgentSecondaryAddrWrongIpClassErrorReturn':hm2AgentSecondaryAddrWrongIpClassErrorReturn,'hm2AgentSecondaryAddrWrongSubnetErrorReturn':hm2AgentSecondaryAddrWrongSubnetErrorReturn,'hm2AgentSecondaryAddrMaxIntfEntriesErrorReturn':hm2AgentSecondaryAddrMaxIntfEntriesErrorReturn,'hm2AgentSecondaryAddrMaxSystemEntriesErrorReturn':hm2AgentSecondaryAddrMaxSystemEntriesErrorReturn,'hm2AgentSecondaryAddrStaticRouteErrorReturn':hm2AgentSecondaryAddrStaticRouteErrorReturn,'hm2AgentSecondaryAddrStaticARPErrorReturn':hm2AgentSecondaryAddrStaticARPErrorReturn,'hm2AgentSecondaryAddrAbsentEntryErrorReturn':hm2AgentSecondaryAddrAbsentEntryErrorReturn,'hm2AgentPrimaryAddrWrongIpClassErrorReturn':hm2AgentPrimaryAddrWrongIpClassErrorReturn,'hm2AgentPrimaryAddrConflictErrorReturn':hm2AgentPrimaryAddrConflictErrorReturn,'hm2AgentPrimaryAddrStaticRouteErrorReturn':hm2AgentPrimaryAddrStaticRouteErrorReturn,'hm2AgentPrimaryAddrStaticARPErrorReturn':hm2AgentPrimaryAddrStaticARPErrorReturn,'hm2AgentPrimaryAddrExistingSecondaryErrorReturn':hm2AgentPrimaryAddrExistingSecondaryErrorReturn,'hm2AgentPrimaryAddrNetworkConflictErrorReturn':hm2AgentPrimaryAddrNetworkConflictErrorReturn,'hm2AgentPrimaryAddrRoutingTableFullErrorReturn':hm2AgentPrimaryAddrRoutingTableFullErrorReturn,'hm2AgentDstAddrHostBitSetErrorReturn':hm2AgentDstAddrHostBitSetErrorReturn,'hm2AgentSamePrefRouteErrorReturn':hm2AgentSamePrefRouteErrorReturn,'hm2AgentVrrpAssoIpAddrRowStatusInconsistentAddress':hm2AgentVrrpAssoIpAddrRowStatusInconsistentAddress,'hm2AgentVrrpAssoIpAddrRowStatusInvalidAddress':hm2AgentVrrpAssoIpAddrRowStatusInvalidAddress,'hm2AgentVrrpAssoIpAddrRowStatusUnknownVRID':hm2AgentVrrpAssoIpAddrRowStatusUnknownVRID,'hm2AgentSwitchIpRouterDiscMinMaxAdvtIntErrorRtrn':hm2AgentSwitchIpRouterDiscMinMaxAdvtIntErrorRtrn,'hm2AgentSwitchIpRouterDiscLifeTimeMaxAdvIntErrorRtrn':hm2AgentSwitchIpRouterDiscLifeTimeMaxAdvIntErrorRtrn,'hm2AgentSwitchIpIcmpRateLimitExceedingRatioErrorReturn':hm2AgentSwitchIpIcmpRateLimitExceedingRatioErrorReturn,'hm2AgentRouterOspfMaxAreaErrorReturn':hm2AgentRouterOspfMaxAreaErrorReturn,'hm2AgentospfRouterIdChange':hm2AgentospfRouterIdChange,'hm2AgentOspfRedistDistList':hm2AgentOspfRedistDistList,'hm2AgentOspfDefaultAreaDeleteErrorReturn':hm2AgentOspfDefaultAreaDeleteErrorReturn,'hm2AgentLocalArpDeleteErrorReturn':hm2AgentLocalArpDeleteErrorReturn,'hm2AgentDynamicVlanRoutingErrorReturn':hm2AgentDynamicVlanRoutingErrorReturn,'hm2AgentVlanUnawareRoutingErrorReturn':hm2AgentVlanUnawareRoutingErrorReturn,'hm2AgentRoutingInvalidNetworkAddress':hm2AgentRoutingInvalidNetworkAddress,'hm2AgentRoutingTypeInvalidValue':hm2AgentRoutingTypeInvalidValue,'hm2AgentRoutingLocalRoutePreference':hm2AgentRoutingLocalRoutePreference,'hm2AgentRoutingMetricInvalid':hm2AgentRoutingMetricInvalid,'hm2AgentRoutingMetricNotSupported':hm2AgentRoutingMetricNotSupported,'hm2AgentRoutingNexthopAtLocalInterface':hm2AgentRoutingNexthopAtLocalInterface,'hm2AgentRoutingNexthopInvalid':hm2AgentRoutingNexthopInvalid,'hm2AgentRoutingMaxEntryCountReached':hm2AgentRoutingMaxEntryCountReached,'hm2AgentRoutingNoPreferenceUpdate':hm2AgentRoutingNoPreferenceUpdate,'hm2AgentRoutingPortInvalid':hm2AgentRoutingPortInvalid,'hm2AgentRoutingStaticRoutePreference':hm2AgentRoutingStaticRoutePreference,'hm2AgentRoutingSameNetworkAddrErrorReturn':hm2AgentRoutingSameNetworkAddrErrorReturn,'hm2AgentRoutingTypeInvalid':hm2AgentRoutingTypeInvalid,'hm2AgentRoutingMacAddressInvalid':hm2AgentRoutingMacAddressInvalid,'hm2AgentRoutingIPAddressExist':hm2AgentRoutingIPAddressExist,'hm2AgentRoutingPingPortInvalid':hm2AgentRoutingPingPortInvalid,'hm2AgentRoutingIntervalTimeInvalid':hm2AgentRoutingIntervalTimeInvalid,'hm2AgentRoutingPingLoseTimeInvalid':hm2AgentRoutingPingLoseTimeInvalid,'hm2AgentRoutingPingReceiveTimeInvalid':hm2AgentRoutingPingReceiveTimeInvalid,'hm2AgentRoutingPingTimeoutInvalid':hm2AgentRoutingPingTimeoutInvalid,'hm2AgentRoutingPingTTLInvalid':hm2AgentRoutingPingTTLInvalid,'hm2AgentRoutingLogicalOperandInvalid':hm2AgentRoutingLogicalOperandInvalid,'hm2AgentRoutingOperatorInvalid':hm2AgentRoutingOperatorInvalid,'hm2AgentRoutingLinkDelayInvalid':hm2AgentRoutingLinkDelayInvalid,'hm2AgentRoutingL3RelayFunctionInvalid':hm2AgentRoutingL3RelayFunctionInvalid,'hm2AgentRoutingBootpDhcpHopsInvalid':hm2AgentRoutingBootpDhcpHopsInvalid,'hm2AgentRoutingBootpDhcpWaitTimeInvalid':hm2AgentRoutingBootpDhcpWaitTimeInvalid,'hm2AgentRoutingCircuitIDInvalid':hm2AgentRoutingCircuitIDInvalid,'hm2AgentRoutingTrackTypeEnableError':hm2AgentRoutingTrackTypeEnableError,'hm2AgentRoutingTrackingEnableErrorReturn':hm2AgentRoutingTrackingEnableErrorReturn,'hm2AgentRoutingTrackingDisableErrorReturn':hm2AgentRoutingTrackingDisableErrorReturn,'hm2AgentRoutingTrackTypeDisableError':hm2AgentRoutingTrackTypeDisableError,'hm2AgentRoutingTrackIDCreateError':hm2AgentRoutingTrackIDCreateError,'hm2AgentRoutingTrackTypeCreateError':hm2AgentRoutingTrackTypeCreateError})