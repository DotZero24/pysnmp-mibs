_r='hmAgentOspfVirtIfEntry'
_q='hmAgentOspfIfEntry'
_p='hmAgentRip2IfConfEntry'
_o='hmVrrpDomainId'
_n='supervisorDown'
_m='noSupervisor'
_l='noError'
_k='hmVrrpExtVrid'
_j='hmVrrpExtIfIndex'
_i='hmVrrpTrackId'
_h='hmVrrpTrackVrid'
_g='hmVrrpTrackIfIndex'
_f='hmAgentOspfRouteRedistSource'
_e='externalType2'
_d='externalType1'
_c='hmAgentRip2InterfaceIfIndex'
_b='hmAgentRipRouteRedistSource'
_a='hmAgentSwitchIpRouteStaticNextHop'
_Z='hmAgentSwitchIpRouteStaticDestinationMask'
_Y='hmAgentSwitchIpRouteStaticDestination'
_X='hmAgentSwitchIpRoutePreferenceSource'
_W='hmAgentSwitchSecondaryIpAddress'
_V='hmAgentSwitchIpVlanId'
_U='hmAgentSwitchIpRouterDiscoveryIfIndex'
_T='hmAgentSwitchArpIpAddress'
_S='IpAddress'
_R='OctetString'
_Q='connected'
_P='hmAgentSwitchIpInterfaceIfIndex'
_O='static'
_N='not-applicable'
_M='false'
_L='true'
_K='TruthValue'
_J='Unsigned32'
_I='read-create'
_H='not-accessible'
_G='disable'
_F='enable'
_E='HIRSCHMANN-MMP4-ROUTING-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmPlatform4,=mibBuilder.importSymbols('HIRSCHMANN-MMP4-BASICL2-MIB','hmPlatform4')
ospfIfEntry,ospfVirtIfEntry=mibBuilder.importSymbols('OSPF-MIB','ospfIfEntry','ospfVirtIfEntry')
rip2IfConfEntry,=mibBuilder.importSymbols('RIPv2-MIB','rip2IfConfEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_S,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
hmPlatform4Routing=ModuleIdentity((1,3,6,1,4,1,248,15,2))
if mibBuilder.loadTexts:hmPlatform4Routing.setRevisions(('2005-08-18 12:00','2003-04-02 17:00'))
_HmAgentSwitchArpGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchArpGroup=_HmAgentSwitchArpGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,1))
class _HmAgentSwitchArpAgeoutTime_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,21600))
_HmAgentSwitchArpAgeoutTime_Type.__name__=_C
_HmAgentSwitchArpAgeoutTime_Object=MibScalar
hmAgentSwitchArpAgeoutTime=_HmAgentSwitchArpAgeoutTime_Object((1,3,6,1,4,1,248,15,2,1,1),_HmAgentSwitchArpAgeoutTime_Type())
hmAgentSwitchArpAgeoutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpAgeoutTime.setStatus(_A)
class _HmAgentSwitchArpResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HmAgentSwitchArpResponseTime_Type.__name__=_C
_HmAgentSwitchArpResponseTime_Object=MibScalar
hmAgentSwitchArpResponseTime=_HmAgentSwitchArpResponseTime_Object((1,3,6,1,4,1,248,15,2,1,2),_HmAgentSwitchArpResponseTime_Type())
hmAgentSwitchArpResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpResponseTime.setStatus(_A)
class _HmAgentSwitchArpMaxRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HmAgentSwitchArpMaxRetries_Type.__name__=_C
_HmAgentSwitchArpMaxRetries_Object=MibScalar
hmAgentSwitchArpMaxRetries=_HmAgentSwitchArpMaxRetries_Object((1,3,6,1,4,1,248,15,2,1,3),_HmAgentSwitchArpMaxRetries_Type())
hmAgentSwitchArpMaxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpMaxRetries.setStatus(_A)
_HmAgentSwitchArpCacheSize_Type=Integer32
_HmAgentSwitchArpCacheSize_Object=MibScalar
hmAgentSwitchArpCacheSize=_HmAgentSwitchArpCacheSize_Object((1,3,6,1,4,1,248,15,2,1,4),_HmAgentSwitchArpCacheSize_Type())
hmAgentSwitchArpCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpCacheSize.setStatus(_A)
class _HmAgentSwitchArpDynamicRenew_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchArpDynamicRenew_Type.__name__=_C
_HmAgentSwitchArpDynamicRenew_Object=MibScalar
hmAgentSwitchArpDynamicRenew=_HmAgentSwitchArpDynamicRenew_Object((1,3,6,1,4,1,248,15,2,1,5),_HmAgentSwitchArpDynamicRenew_Type())
hmAgentSwitchArpDynamicRenew.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpDynamicRenew.setStatus(_A)
_HmAgentSwitchArpTotalEntryCountCurrent_Type=Gauge32
_HmAgentSwitchArpTotalEntryCountCurrent_Object=MibScalar
hmAgentSwitchArpTotalEntryCountCurrent=_HmAgentSwitchArpTotalEntryCountCurrent_Object((1,3,6,1,4,1,248,15,2,1,6),_HmAgentSwitchArpTotalEntryCountCurrent_Type())
hmAgentSwitchArpTotalEntryCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpTotalEntryCountCurrent.setStatus(_A)
_HmAgentSwitchArpTotalEntryCountPeak_Type=Gauge32
_HmAgentSwitchArpTotalEntryCountPeak_Object=MibScalar
hmAgentSwitchArpTotalEntryCountPeak=_HmAgentSwitchArpTotalEntryCountPeak_Object((1,3,6,1,4,1,248,15,2,1,7),_HmAgentSwitchArpTotalEntryCountPeak_Type())
hmAgentSwitchArpTotalEntryCountPeak.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpTotalEntryCountPeak.setStatus(_A)
_HmAgentSwitchArpStaticEntryCountCurrent_Type=Gauge32
_HmAgentSwitchArpStaticEntryCountCurrent_Object=MibScalar
hmAgentSwitchArpStaticEntryCountCurrent=_HmAgentSwitchArpStaticEntryCountCurrent_Object((1,3,6,1,4,1,248,15,2,1,8),_HmAgentSwitchArpStaticEntryCountCurrent_Type())
hmAgentSwitchArpStaticEntryCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpStaticEntryCountCurrent.setStatus(_A)
_HmAgentSwitchArpStaticEntryCountMax_Type=Integer32
_HmAgentSwitchArpStaticEntryCountMax_Object=MibScalar
hmAgentSwitchArpStaticEntryCountMax=_HmAgentSwitchArpStaticEntryCountMax_Object((1,3,6,1,4,1,248,15,2,1,9),_HmAgentSwitchArpStaticEntryCountMax_Type())
hmAgentSwitchArpStaticEntryCountMax.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpStaticEntryCountMax.setStatus(_A)
_HmAgentSwitchArpTable_Object=MibTable
hmAgentSwitchArpTable=_HmAgentSwitchArpTable_Object((1,3,6,1,4,1,248,15,2,1,10))
if mibBuilder.loadTexts:hmAgentSwitchArpTable.setStatus(_A)
_HmAgentSwitchArpEntry_Object=MibTableRow
hmAgentSwitchArpEntry=_HmAgentSwitchArpEntry_Object((1,3,6,1,4,1,248,15,2,1,10,1))
hmAgentSwitchArpEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:hmAgentSwitchArpEntry.setStatus(_A)
_HmAgentSwitchArpAge_Type=TimeTicks
_HmAgentSwitchArpAge_Object=MibTableColumn
hmAgentSwitchArpAge=_HmAgentSwitchArpAge_Object((1,3,6,1,4,1,248,15,2,1,10,1,1),_HmAgentSwitchArpAge_Type())
hmAgentSwitchArpAge.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpAge.setStatus(_A)
_HmAgentSwitchArpIpAddress_Type=IpAddress
_HmAgentSwitchArpIpAddress_Object=MibTableColumn
hmAgentSwitchArpIpAddress=_HmAgentSwitchArpIpAddress_Object((1,3,6,1,4,1,248,15,2,1,10,1,2),_HmAgentSwitchArpIpAddress_Type())
hmAgentSwitchArpIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpIpAddress.setStatus(_A)
_HmAgentSwitchArpMacAddress_Type=MacAddress
_HmAgentSwitchArpMacAddress_Object=MibTableColumn
hmAgentSwitchArpMacAddress=_HmAgentSwitchArpMacAddress_Object((1,3,6,1,4,1,248,15,2,1,10,1,3),_HmAgentSwitchArpMacAddress_Type())
hmAgentSwitchArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentSwitchArpMacAddress.setStatus(_A)
_HmAgentSwitchArpInterface_Type=Integer32
_HmAgentSwitchArpInterface_Object=MibTableColumn
hmAgentSwitchArpInterface=_HmAgentSwitchArpInterface_Object((1,3,6,1,4,1,248,15,2,1,10,1,4),_HmAgentSwitchArpInterface_Type())
hmAgentSwitchArpInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpInterface.setStatus(_A)
class _HmAgentSwitchArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('gateway',2),(_O,3),('dynamic',4)))
_HmAgentSwitchArpType_Type.__name__=_C
_HmAgentSwitchArpType_Object=MibTableColumn
hmAgentSwitchArpType=_HmAgentSwitchArpType_Object((1,3,6,1,4,1,248,15,2,1,10,1,5),_HmAgentSwitchArpType_Type())
hmAgentSwitchArpType.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchArpType.setStatus(_A)
_HmAgentSwitchArpStatus_Type=RowStatus
_HmAgentSwitchArpStatus_Object=MibTableColumn
hmAgentSwitchArpStatus=_HmAgentSwitchArpStatus_Object((1,3,6,1,4,1,248,15,2,1,10,1,6),_HmAgentSwitchArpStatus_Type())
hmAgentSwitchArpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpStatus.setStatus(_A)
class _HmAgentSwitchArpSparseLearn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchArpSparseLearn_Type.__name__=_C
_HmAgentSwitchArpSparseLearn_Object=MibScalar
hmAgentSwitchArpSparseLearn=_HmAgentSwitchArpSparseLearn_Object((1,3,6,1,4,1,248,15,2,1,11),_HmAgentSwitchArpSparseLearn_Type())
hmAgentSwitchArpSparseLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchArpSparseLearn.setStatus(_A)
_HmAgentSwitchIpGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchIpGroup=_HmAgentSwitchIpGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,2))
class _HmAgentSwitchIpRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpRoutingMode_Type.__name__=_C
_HmAgentSwitchIpRoutingMode_Object=MibScalar
hmAgentSwitchIpRoutingMode=_HmAgentSwitchIpRoutingMode_Object((1,3,6,1,4,1,248,15,2,2,1),_HmAgentSwitchIpRoutingMode_Type())
hmAgentSwitchIpRoutingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRoutingMode.setStatus(_A)
class _HmAgentSwitchIpVRRPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpVRRPMode_Type.__name__=_C
_HmAgentSwitchIpVRRPMode_Object=MibScalar
hmAgentSwitchIpVRRPMode=_HmAgentSwitchIpVRRPMode_Object((1,3,6,1,4,1,248,15,2,2,2),_HmAgentSwitchIpVRRPMode_Type())
hmAgentSwitchIpVRRPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpVRRPMode.setStatus(_A)
_HmAgentSwitchIpInterfaceTable_Object=MibTable
hmAgentSwitchIpInterfaceTable=_HmAgentSwitchIpInterfaceTable_Object((1,3,6,1,4,1,248,15,2,2,3))
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceTable.setStatus(_A)
_HmAgentSwitchIpInterfaceEntry_Object=MibTableRow
hmAgentSwitchIpInterfaceEntry=_HmAgentSwitchIpInterfaceEntry_Object((1,3,6,1,4,1,248,15,2,2,3,1))
hmAgentSwitchIpInterfaceEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceEntry.setStatus(_A)
_HmAgentSwitchIpInterfaceIfIndex_Type=Integer32
_HmAgentSwitchIpInterfaceIfIndex_Object=MibTableColumn
hmAgentSwitchIpInterfaceIfIndex=_HmAgentSwitchIpInterfaceIfIndex_Object((1,3,6,1,4,1,248,15,2,2,3,1,1),_HmAgentSwitchIpInterfaceIfIndex_Type())
hmAgentSwitchIpInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceIfIndex.setStatus(_A)
_HmAgentSwitchIpInterfaceIpAddress_Type=IpAddress
_HmAgentSwitchIpInterfaceIpAddress_Object=MibTableColumn
hmAgentSwitchIpInterfaceIpAddress=_HmAgentSwitchIpInterfaceIpAddress_Object((1,3,6,1,4,1,248,15,2,2,3,1,2),_HmAgentSwitchIpInterfaceIpAddress_Type())
hmAgentSwitchIpInterfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceIpAddress.setStatus(_A)
_HmAgentSwitchIpInterfaceNetMask_Type=IpAddress
_HmAgentSwitchIpInterfaceNetMask_Object=MibTableColumn
hmAgentSwitchIpInterfaceNetMask=_HmAgentSwitchIpInterfaceNetMask_Object((1,3,6,1,4,1,248,15,2,2,3,1,3),_HmAgentSwitchIpInterfaceNetMask_Type())
hmAgentSwitchIpInterfaceNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceNetMask.setStatus(_A)
class _HmAgentSwitchIpInterfaceClearIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpInterfaceClearIp_Type.__name__=_C
_HmAgentSwitchIpInterfaceClearIp_Object=MibTableColumn
hmAgentSwitchIpInterfaceClearIp=_HmAgentSwitchIpInterfaceClearIp_Object((1,3,6,1,4,1,248,15,2,2,3,1,4),_HmAgentSwitchIpInterfaceClearIp_Type())
hmAgentSwitchIpInterfaceClearIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceClearIp.setStatus(_A)
class _HmAgentSwitchIpInterfaceRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpInterfaceRoutingMode_Type.__name__=_C
_HmAgentSwitchIpInterfaceRoutingMode_Object=MibTableColumn
hmAgentSwitchIpInterfaceRoutingMode=_HmAgentSwitchIpInterfaceRoutingMode_Object((1,3,6,1,4,1,248,15,2,2,3,1,5),_HmAgentSwitchIpInterfaceRoutingMode_Type())
hmAgentSwitchIpInterfaceRoutingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceRoutingMode.setStatus(_A)
class _HmAgentSwitchIpInterfaceProxyARPMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpInterfaceProxyARPMode_Type.__name__=_C
_HmAgentSwitchIpInterfaceProxyARPMode_Object=MibTableColumn
hmAgentSwitchIpInterfaceProxyARPMode=_HmAgentSwitchIpInterfaceProxyARPMode_Object((1,3,6,1,4,1,248,15,2,2,3,1,6),_HmAgentSwitchIpInterfaceProxyARPMode_Type())
hmAgentSwitchIpInterfaceProxyARPMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceProxyARPMode.setStatus(_A)
class _HmAgentSwitchIpInterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(68,9000))
_HmAgentSwitchIpInterfaceMtuValue_Type.__name__=_J
_HmAgentSwitchIpInterfaceMtuValue_Object=MibTableColumn
hmAgentSwitchIpInterfaceMtuValue=_HmAgentSwitchIpInterfaceMtuValue_Object((1,3,6,1,4,1,248,15,2,2,3,1,7),_HmAgentSwitchIpInterfaceMtuValue_Type())
hmAgentSwitchIpInterfaceMtuValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceMtuValue.setStatus(_A)
_HmAgentSwitchIpInterfaceSlotNum_Type=Integer32
_HmAgentSwitchIpInterfaceSlotNum_Object=MibTableColumn
hmAgentSwitchIpInterfaceSlotNum=_HmAgentSwitchIpInterfaceSlotNum_Object((1,3,6,1,4,1,248,15,2,2,3,1,8),_HmAgentSwitchIpInterfaceSlotNum_Type())
hmAgentSwitchIpInterfaceSlotNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceSlotNum.setStatus(_A)
_HmAgentSwitchIpInterfacePortNum_Type=Integer32
_HmAgentSwitchIpInterfacePortNum_Object=MibTableColumn
hmAgentSwitchIpInterfacePortNum=_HmAgentSwitchIpInterfacePortNum_Object((1,3,6,1,4,1,248,15,2,2,3,1,9),_HmAgentSwitchIpInterfacePortNum_Type())
hmAgentSwitchIpInterfacePortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfacePortNum.setStatus(_A)
class _HmAgentSwitchIpInterfaceNetdirectedBCMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpInterfaceNetdirectedBCMode_Type.__name__=_C
_HmAgentSwitchIpInterfaceNetdirectedBCMode_Object=MibTableColumn
hmAgentSwitchIpInterfaceNetdirectedBCMode=_HmAgentSwitchIpInterfaceNetdirectedBCMode_Object((1,3,6,1,4,1,248,15,2,2,3,1,10),_HmAgentSwitchIpInterfaceNetdirectedBCMode_Type())
hmAgentSwitchIpInterfaceNetdirectedBCMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpInterfaceNetdirectedBCMode.setStatus(_A)
_HmAgentSwitchIpRouterDiscoveryTable_Object=MibTable
hmAgentSwitchIpRouterDiscoveryTable=_HmAgentSwitchIpRouterDiscoveryTable_Object((1,3,6,1,4,1,248,15,2,2,4))
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryTable.setStatus(_A)
_HmAgentSwitchIpRouterDiscoveryEntry_Object=MibTableRow
hmAgentSwitchIpRouterDiscoveryEntry=_HmAgentSwitchIpRouterDiscoveryEntry_Object((1,3,6,1,4,1,248,15,2,2,4,1))
hmAgentSwitchIpRouterDiscoveryEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryEntry.setStatus(_A)
_HmAgentSwitchIpRouterDiscoveryIfIndex_Type=Integer32
_HmAgentSwitchIpRouterDiscoveryIfIndex_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryIfIndex=_HmAgentSwitchIpRouterDiscoveryIfIndex_Object((1,3,6,1,4,1,248,15,2,2,4,1,1),_HmAgentSwitchIpRouterDiscoveryIfIndex_Type())
hmAgentSwitchIpRouterDiscoveryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryIfIndex.setStatus(_A)
class _HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__=_C
_HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryAdvertiseMode=_HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Object((1,3,6,1,4,1,248,15,2,2,4,1,2),_HmAgentSwitchIpRouterDiscoveryAdvertiseMode_Type())
hmAgentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryAdvertiseMode.setStatus(_A)
class _HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__=_C
_HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval=_HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object((1,3,6,1,4,1,248,15,2,2,4,1,3),_HmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type())
hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus(_A)
class _HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__=_C
_HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval=_HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object((1,3,6,1,4,1,248,15,2,2,4,1,4),_HmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type())
hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus(_A)
class _HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__=_C
_HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime=_HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object((1,3,6,1,4,1,248,15,2,2,4,1,5),_HmAgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type())
hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus(_A)
class _HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):defaultValue=0
_HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__=_C
_HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryPreferenceLevel=_HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Object((1,3,6,1,4,1,248,15,2,2,4,1,6),_HmAgentSwitchIpRouterDiscoveryPreferenceLevel_Type())
hmAgentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryPreferenceLevel.setStatus(_A)
class _HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):defaultHexValue='E0000001'
_HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__=_S
_HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Object=MibTableColumn
hmAgentSwitchIpRouterDiscoveryAdvertisementAddress=_HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Object((1,3,6,1,4,1,248,15,2,2,4,1,7),_HmAgentSwitchIpRouterDiscoveryAdvertisementAddress_Type())
hmAgentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus(_A)
_HmAgentSwitchIpVlanTable_Object=MibTable
hmAgentSwitchIpVlanTable=_HmAgentSwitchIpVlanTable_Object((1,3,6,1,4,1,248,15,2,2,5))
if mibBuilder.loadTexts:hmAgentSwitchIpVlanTable.setStatus(_A)
_HmAgentSwitchIpVlanEntry_Object=MibTableRow
hmAgentSwitchIpVlanEntry=_HmAgentSwitchIpVlanEntry_Object((1,3,6,1,4,1,248,15,2,2,5,1))
hmAgentSwitchIpVlanEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:hmAgentSwitchIpVlanEntry.setStatus(_A)
_HmAgentSwitchIpVlanId_Type=Integer32
_HmAgentSwitchIpVlanId_Object=MibTableColumn
hmAgentSwitchIpVlanId=_HmAgentSwitchIpVlanId_Object((1,3,6,1,4,1,248,15,2,2,5,1,1),_HmAgentSwitchIpVlanId_Type())
hmAgentSwitchIpVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpVlanId.setStatus(_A)
_HmAgentSwitchIpVlanIfIndex_Type=Integer32
_HmAgentSwitchIpVlanIfIndex_Object=MibTableColumn
hmAgentSwitchIpVlanIfIndex=_HmAgentSwitchIpVlanIfIndex_Object((1,3,6,1,4,1,248,15,2,2,5,1,2),_HmAgentSwitchIpVlanIfIndex_Type())
hmAgentSwitchIpVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpVlanIfIndex.setStatus(_A)
_HmAgentSwitchIpVlanRoutingStatus_Type=RowStatus
_HmAgentSwitchIpVlanRoutingStatus_Object=MibTableColumn
hmAgentSwitchIpVlanRoutingStatus=_HmAgentSwitchIpVlanRoutingStatus_Object((1,3,6,1,4,1,248,15,2,2,5,1,3),_HmAgentSwitchIpVlanRoutingStatus_Type())
hmAgentSwitchIpVlanRoutingStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentSwitchIpVlanRoutingStatus.setStatus(_A)
_HmAgentSwitchSecondaryAddressTable_Object=MibTable
hmAgentSwitchSecondaryAddressTable=_HmAgentSwitchSecondaryAddressTable_Object((1,3,6,1,4,1,248,15,2,2,6))
if mibBuilder.loadTexts:hmAgentSwitchSecondaryAddressTable.setStatus(_A)
_HmAgentSwitchSecondaryAddressEntry_Object=MibTableRow
hmAgentSwitchSecondaryAddressEntry=_HmAgentSwitchSecondaryAddressEntry_Object((1,3,6,1,4,1,248,15,2,2,6,1))
hmAgentSwitchSecondaryAddressEntry.setIndexNames((0,_E,_P),(0,_E,_W))
if mibBuilder.loadTexts:hmAgentSwitchSecondaryAddressEntry.setStatus(_A)
_HmAgentSwitchSecondaryIpAddress_Type=IpAddress
_HmAgentSwitchSecondaryIpAddress_Object=MibTableColumn
hmAgentSwitchSecondaryIpAddress=_HmAgentSwitchSecondaryIpAddress_Object((1,3,6,1,4,1,248,15,2,2,6,1,1),_HmAgentSwitchSecondaryIpAddress_Type())
hmAgentSwitchSecondaryIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentSwitchSecondaryIpAddress.setStatus(_A)
_HmAgentSwitchSecondaryNetMask_Type=IpAddress
_HmAgentSwitchSecondaryNetMask_Object=MibTableColumn
hmAgentSwitchSecondaryNetMask=_HmAgentSwitchSecondaryNetMask_Object((1,3,6,1,4,1,248,15,2,2,6,1,2),_HmAgentSwitchSecondaryNetMask_Type())
hmAgentSwitchSecondaryNetMask.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentSwitchSecondaryNetMask.setStatus(_A)
_HmAgentSwitchSecondaryStatus_Type=RowStatus
_HmAgentSwitchSecondaryStatus_Object=MibTableColumn
hmAgentSwitchSecondaryStatus=_HmAgentSwitchSecondaryStatus_Object((1,3,6,1,4,1,248,15,2,2,6,1,3),_HmAgentSwitchSecondaryStatus_Type())
hmAgentSwitchSecondaryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentSwitchSecondaryStatus.setStatus(_A)
_HmAgentSwitchIpRoutePreferenceTable_Object=MibTable
hmAgentSwitchIpRoutePreferenceTable=_HmAgentSwitchIpRoutePreferenceTable_Object((1,3,6,1,4,1,248,15,2,2,7))
if mibBuilder.loadTexts:hmAgentSwitchIpRoutePreferenceTable.setStatus(_A)
_HmAgentSwitchIpRoutePreferenceEntry_Object=MibTableRow
hmAgentSwitchIpRoutePreferenceEntry=_HmAgentSwitchIpRoutePreferenceEntry_Object((1,3,6,1,4,1,248,15,2,2,7,1))
hmAgentSwitchIpRoutePreferenceEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:hmAgentSwitchIpRoutePreferenceEntry.setStatus(_A)
class _HmAgentSwitchIpRoutePreferenceSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,1),(_O,2),('ospf-intra',3),('ospf-inter',4),('ospf-ext-t1',5),('ospf-ext-t2',6),('rip',7)))
_HmAgentSwitchIpRoutePreferenceSource_Type.__name__=_C
_HmAgentSwitchIpRoutePreferenceSource_Object=MibTableColumn
hmAgentSwitchIpRoutePreferenceSource=_HmAgentSwitchIpRoutePreferenceSource_Object((1,3,6,1,4,1,248,15,2,2,7,1,1),_HmAgentSwitchIpRoutePreferenceSource_Type())
hmAgentSwitchIpRoutePreferenceSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpRoutePreferenceSource.setStatus(_A)
class _HmAgentSwitchIpRoutePreferenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmAgentSwitchIpRoutePreferenceValue_Type.__name__=_C
_HmAgentSwitchIpRoutePreferenceValue_Object=MibTableColumn
hmAgentSwitchIpRoutePreferenceValue=_HmAgentSwitchIpRoutePreferenceValue_Object((1,3,6,1,4,1,248,15,2,2,7,1,2),_HmAgentSwitchIpRoutePreferenceValue_Type())
hmAgentSwitchIpRoutePreferenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRoutePreferenceValue.setStatus(_A)
_HmAgentSwitchIpRouteStaticTable_Object=MibTable
hmAgentSwitchIpRouteStaticTable=_HmAgentSwitchIpRouteStaticTable_Object((1,3,6,1,4,1,248,15,2,2,8))
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticTable.setStatus(_A)
_HmAgentSwitchIpRouteStaticEntry_Object=MibTableRow
hmAgentSwitchIpRouteStaticEntry=_HmAgentSwitchIpRouteStaticEntry_Object((1,3,6,1,4,1,248,15,2,2,8,1))
hmAgentSwitchIpRouteStaticEntry.setIndexNames((0,_E,_Y),(0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticEntry.setStatus(_A)
_HmAgentSwitchIpRouteStaticDestination_Type=IpAddress
_HmAgentSwitchIpRouteStaticDestination_Object=MibTableColumn
hmAgentSwitchIpRouteStaticDestination=_HmAgentSwitchIpRouteStaticDestination_Object((1,3,6,1,4,1,248,15,2,2,8,1,1),_HmAgentSwitchIpRouteStaticDestination_Type())
hmAgentSwitchIpRouteStaticDestination.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticDestination.setStatus(_A)
_HmAgentSwitchIpRouteStaticDestinationMask_Type=IpAddress
_HmAgentSwitchIpRouteStaticDestinationMask_Object=MibTableColumn
hmAgentSwitchIpRouteStaticDestinationMask=_HmAgentSwitchIpRouteStaticDestinationMask_Object((1,3,6,1,4,1,248,15,2,2,8,1,2),_HmAgentSwitchIpRouteStaticDestinationMask_Type())
hmAgentSwitchIpRouteStaticDestinationMask.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticDestinationMask.setStatus(_A)
_HmAgentSwitchIpRouteStaticNextHop_Type=IpAddress
_HmAgentSwitchIpRouteStaticNextHop_Object=MibTableColumn
hmAgentSwitchIpRouteStaticNextHop=_HmAgentSwitchIpRouteStaticNextHop_Object((1,3,6,1,4,1,248,15,2,2,8,1,3),_HmAgentSwitchIpRouteStaticNextHop_Type())
hmAgentSwitchIpRouteStaticNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticNextHop.setStatus(_A)
class _HmAgentSwitchIpRouteStaticPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmAgentSwitchIpRouteStaticPreference_Type.__name__=_C
_HmAgentSwitchIpRouteStaticPreference_Object=MibTableColumn
hmAgentSwitchIpRouteStaticPreference=_HmAgentSwitchIpRouteStaticPreference_Object((1,3,6,1,4,1,248,15,2,2,8,1,4),_HmAgentSwitchIpRouteStaticPreference_Type())
hmAgentSwitchIpRouteStaticPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticPreference.setStatus(_A)
_HmAgentSwitchIpRouteStaticStatus_Type=RowStatus
_HmAgentSwitchIpRouteStaticStatus_Object=MibTableColumn
hmAgentSwitchIpRouteStaticStatus=_HmAgentSwitchIpRouteStaticStatus_Object((1,3,6,1,4,1,248,15,2,2,8,1,5),_HmAgentSwitchIpRouteStaticStatus_Type())
hmAgentSwitchIpRouteStaticStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticStatus.setStatus(_A)
class _HmAgentSwitchIpRouteStaticTrackId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmAgentSwitchIpRouteStaticTrackId_Type.__name__=_C
_HmAgentSwitchIpRouteStaticTrackId_Object=MibTableColumn
hmAgentSwitchIpRouteStaticTrackId=_HmAgentSwitchIpRouteStaticTrackId_Object((1,3,6,1,4,1,248,15,2,2,8,1,6),_HmAgentSwitchIpRouteStaticTrackId_Type())
hmAgentSwitchIpRouteStaticTrackId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpRouteStaticTrackId.setStatus(_A)
class _HmAgentSwitchIpVlanSingleMacMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSwitchIpVlanSingleMacMode_Type.__name__=_C
_HmAgentSwitchIpVlanSingleMacMode_Object=MibScalar
hmAgentSwitchIpVlanSingleMacMode=_HmAgentSwitchIpVlanSingleMacMode_Object((1,3,6,1,4,1,248,15,2,2,100),_HmAgentSwitchIpVlanSingleMacMode_Type())
hmAgentSwitchIpVlanSingleMacMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpVlanSingleMacMode.setStatus(_A)
_HmAgentSwitchIpTableSizesGroup_ObjectIdentity=ObjectIdentity
hmAgentSwitchIpTableSizesGroup=_HmAgentSwitchIpTableSizesGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,2,101))
class _HmAgentSwitchIpTableSizeArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,4096))
_HmAgentSwitchIpTableSizeArp_Type.__name__=_C
_HmAgentSwitchIpTableSizeArp_Object=MibScalar
hmAgentSwitchIpTableSizeArp=_HmAgentSwitchIpTableSizeArp_Object((1,3,6,1,4,1,248,15,2,2,101,1),_HmAgentSwitchIpTableSizeArp_Type())
hmAgentSwitchIpTableSizeArp.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpTableSizeArp.setStatus(_A)
class _HmAgentSwitchIpTableSizeUCRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,4096))
_HmAgentSwitchIpTableSizeUCRoutes_Type.__name__=_C
_HmAgentSwitchIpTableSizeUCRoutes_Object=MibScalar
hmAgentSwitchIpTableSizeUCRoutes=_HmAgentSwitchIpTableSizeUCRoutes_Object((1,3,6,1,4,1,248,15,2,2,101,2),_HmAgentSwitchIpTableSizeUCRoutes_Type())
hmAgentSwitchIpTableSizeUCRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpTableSizeUCRoutes.setStatus(_A)
class _HmAgentSwitchIpTableSizeMCRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_HmAgentSwitchIpTableSizeMCRoutes_Type.__name__=_C
_HmAgentSwitchIpTableSizeMCRoutes_Object=MibScalar
hmAgentSwitchIpTableSizeMCRoutes=_HmAgentSwitchIpTableSizeMCRoutes_Object((1,3,6,1,4,1,248,15,2,2,101,3),_HmAgentSwitchIpTableSizeMCRoutes_Type())
hmAgentSwitchIpTableSizeMCRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSwitchIpTableSizeMCRoutes.setStatus(_A)
class _HmAgentSwitchIpCurrentTableSizeArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,4096))
_HmAgentSwitchIpCurrentTableSizeArp_Type.__name__=_C
_HmAgentSwitchIpCurrentTableSizeArp_Object=MibScalar
hmAgentSwitchIpCurrentTableSizeArp=_HmAgentSwitchIpCurrentTableSizeArp_Object((1,3,6,1,4,1,248,15,2,2,101,4),_HmAgentSwitchIpCurrentTableSizeArp_Type())
hmAgentSwitchIpCurrentTableSizeArp.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpCurrentTableSizeArp.setStatus(_A)
class _HmAgentSwitchIpCurrentTableSizeUCRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,4096))
_HmAgentSwitchIpCurrentTableSizeUCRoutes_Type.__name__=_C
_HmAgentSwitchIpCurrentTableSizeUCRoutes_Object=MibScalar
hmAgentSwitchIpCurrentTableSizeUCRoutes=_HmAgentSwitchIpCurrentTableSizeUCRoutes_Object((1,3,6,1,4,1,248,15,2,2,101,5),_HmAgentSwitchIpCurrentTableSizeUCRoutes_Type())
hmAgentSwitchIpCurrentTableSizeUCRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpCurrentTableSizeUCRoutes.setStatus(_A)
class _HmAgentSwitchIpCurrentTableSizeMCRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_HmAgentSwitchIpCurrentTableSizeMCRoutes_Type.__name__=_C
_HmAgentSwitchIpCurrentTableSizeMCRoutes_Object=MibScalar
hmAgentSwitchIpCurrentTableSizeMCRoutes=_HmAgentSwitchIpCurrentTableSizeMCRoutes_Object((1,3,6,1,4,1,248,15,2,2,101,6),_HmAgentSwitchIpCurrentTableSizeMCRoutes_Type())
hmAgentSwitchIpCurrentTableSizeMCRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSwitchIpCurrentTableSizeMCRoutes.setStatus(_A)
_HmAgentRouterRipConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentRouterRipConfigGroup=_HmAgentRouterRipConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,3))
class _HmAgentRouterRipAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRouterRipAdminState_Type.__name__=_C
_HmAgentRouterRipAdminState_Object=MibScalar
hmAgentRouterRipAdminState=_HmAgentRouterRipAdminState_Object((1,3,6,1,4,1,248,15,2,3,1),_HmAgentRouterRipAdminState_Type())
hmAgentRouterRipAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipAdminState.setStatus(_A)
class _HmAgentRouterRipSplitHorizonMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('simple',2),('poisonReverse',3)))
_HmAgentRouterRipSplitHorizonMode_Type.__name__=_C
_HmAgentRouterRipSplitHorizonMode_Object=MibScalar
hmAgentRouterRipSplitHorizonMode=_HmAgentRouterRipSplitHorizonMode_Object((1,3,6,1,4,1,248,15,2,3,2),_HmAgentRouterRipSplitHorizonMode_Type())
hmAgentRouterRipSplitHorizonMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipSplitHorizonMode.setStatus(_A)
class _HmAgentRouterRipAutoSummaryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRouterRipAutoSummaryMode_Type.__name__=_C
_HmAgentRouterRipAutoSummaryMode_Object=MibScalar
hmAgentRouterRipAutoSummaryMode=_HmAgentRouterRipAutoSummaryMode_Object((1,3,6,1,4,1,248,15,2,3,3),_HmAgentRouterRipAutoSummaryMode_Type())
hmAgentRouterRipAutoSummaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipAutoSummaryMode.setStatus(_A)
class _HmAgentRouterRipHostRoutesAcceptMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRouterRipHostRoutesAcceptMode_Type.__name__=_C
_HmAgentRouterRipHostRoutesAcceptMode_Object=MibScalar
hmAgentRouterRipHostRoutesAcceptMode=_HmAgentRouterRipHostRoutesAcceptMode_Object((1,3,6,1,4,1,248,15,2,3,4),_HmAgentRouterRipHostRoutesAcceptMode_Type())
hmAgentRouterRipHostRoutesAcceptMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipHostRoutesAcceptMode.setStatus(_A)
class _HmAgentRouterRipDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HmAgentRouterRipDefaultMetric_Type.__name__=_C
_HmAgentRouterRipDefaultMetric_Object=MibScalar
hmAgentRouterRipDefaultMetric=_HmAgentRouterRipDefaultMetric_Object((1,3,6,1,4,1,248,15,2,3,5),_HmAgentRouterRipDefaultMetric_Type())
hmAgentRouterRipDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipDefaultMetric.setStatus(_A)
_HmAgentRouterRipDefaultMetricConfigured_Type=TruthValue
_HmAgentRouterRipDefaultMetricConfigured_Object=MibScalar
hmAgentRouterRipDefaultMetricConfigured=_HmAgentRouterRipDefaultMetricConfigured_Object((1,3,6,1,4,1,248,15,2,3,6),_HmAgentRouterRipDefaultMetricConfigured_Type())
hmAgentRouterRipDefaultMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipDefaultMetricConfigured.setStatus(_A)
class _HmAgentRouterRipDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_HmAgentRouterRipDefaultInfoOriginate_Type.__name__=_K
_HmAgentRouterRipDefaultInfoOriginate_Object=MibScalar
hmAgentRouterRipDefaultInfoOriginate=_HmAgentRouterRipDefaultInfoOriginate_Object((1,3,6,1,4,1,248,15,2,3,7),_HmAgentRouterRipDefaultInfoOriginate_Type())
hmAgentRouterRipDefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipDefaultInfoOriginate.setStatus(_A)
_HmAgentRipRouteRedistTable_Object=MibTable
hmAgentRipRouteRedistTable=_HmAgentRipRouteRedistTable_Object((1,3,6,1,4,1,248,15,2,3,8))
if mibBuilder.loadTexts:hmAgentRipRouteRedistTable.setStatus(_A)
_HmAgentRipRouteRedistEntry_Object=MibTableRow
hmAgentRipRouteRedistEntry=_HmAgentRipRouteRedistEntry_Object((1,3,6,1,4,1,248,15,2,3,8,1))
hmAgentRipRouteRedistEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:hmAgentRipRouteRedistEntry.setStatus(_A)
class _HmAgentRipRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_O,2),('ospf',3),('bgp',4)))
_HmAgentRipRouteRedistSource_Type.__name__=_C
_HmAgentRipRouteRedistSource_Object=MibTableColumn
hmAgentRipRouteRedistSource=_HmAgentRipRouteRedistSource_Object((1,3,6,1,4,1,248,15,2,3,8,1,1),_HmAgentRipRouteRedistSource_Type())
hmAgentRipRouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentRipRouteRedistSource.setStatus(_A)
class _HmAgentRipRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRipRouteRedistMode_Type.__name__=_C
_HmAgentRipRouteRedistMode_Object=MibTableColumn
hmAgentRipRouteRedistMode=_HmAgentRipRouteRedistMode_Object((1,3,6,1,4,1,248,15,2,3,8,1,2),_HmAgentRipRouteRedistMode_Type())
hmAgentRipRouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMode.setStatus(_A)
class _HmAgentRipRouteRedistMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HmAgentRipRouteRedistMetric_Type.__name__=_C
_HmAgentRipRouteRedistMetric_Object=MibTableColumn
hmAgentRipRouteRedistMetric=_HmAgentRipRouteRedistMetric_Object((1,3,6,1,4,1,248,15,2,3,8,1,3),_HmAgentRipRouteRedistMetric_Type())
hmAgentRipRouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMetric.setStatus(_A)
_HmAgentRipRouteRedistMetricConfigured_Type=TruthValue
_HmAgentRipRouteRedistMetricConfigured_Object=MibTableColumn
hmAgentRipRouteRedistMetricConfigured=_HmAgentRipRouteRedistMetricConfigured_Object((1,3,6,1,4,1,248,15,2,3,8,1,4),_HmAgentRipRouteRedistMetricConfigured_Type())
hmAgentRipRouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMetricConfigured.setStatus(_A)
class _HmAgentRipRouteRedistMatchInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_HmAgentRipRouteRedistMatchInternal_Type.__name__=_C
_HmAgentRipRouteRedistMatchInternal_Object=MibTableColumn
hmAgentRipRouteRedistMatchInternal=_HmAgentRipRouteRedistMatchInternal_Object((1,3,6,1,4,1,248,15,2,3,8,1,5),_HmAgentRipRouteRedistMatchInternal_Type())
hmAgentRipRouteRedistMatchInternal.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMatchInternal.setStatus(_A)
class _HmAgentRipRouteRedistMatchExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_HmAgentRipRouteRedistMatchExternal1_Type.__name__=_C
_HmAgentRipRouteRedistMatchExternal1_Object=MibTableColumn
hmAgentRipRouteRedistMatchExternal1=_HmAgentRipRouteRedistMatchExternal1_Object((1,3,6,1,4,1,248,15,2,3,8,1,6),_HmAgentRipRouteRedistMatchExternal1_Type())
hmAgentRipRouteRedistMatchExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMatchExternal1.setStatus(_A)
class _HmAgentRipRouteRedistMatchExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_HmAgentRipRouteRedistMatchExternal2_Type.__name__=_C
_HmAgentRipRouteRedistMatchExternal2_Object=MibTableColumn
hmAgentRipRouteRedistMatchExternal2=_HmAgentRipRouteRedistMatchExternal2_Object((1,3,6,1,4,1,248,15,2,3,8,1,7),_HmAgentRipRouteRedistMatchExternal2_Type())
hmAgentRipRouteRedistMatchExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMatchExternal2.setStatus(_A)
class _HmAgentRipRouteRedistMatchNSSAExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_HmAgentRipRouteRedistMatchNSSAExternal1_Type.__name__=_C
_HmAgentRipRouteRedistMatchNSSAExternal1_Object=MibTableColumn
hmAgentRipRouteRedistMatchNSSAExternal1=_HmAgentRipRouteRedistMatchNSSAExternal1_Object((1,3,6,1,4,1,248,15,2,3,8,1,8),_HmAgentRipRouteRedistMatchNSSAExternal1_Type())
hmAgentRipRouteRedistMatchNSSAExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMatchNSSAExternal1.setStatus(_A)
class _HmAgentRipRouteRedistMatchNSSAExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_HmAgentRipRouteRedistMatchNSSAExternal2_Type.__name__=_C
_HmAgentRipRouteRedistMatchNSSAExternal2_Object=MibTableColumn
hmAgentRipRouteRedistMatchNSSAExternal2=_HmAgentRipRouteRedistMatchNSSAExternal2_Object((1,3,6,1,4,1,248,15,2,3,8,1,9),_HmAgentRipRouteRedistMatchNSSAExternal2_Type())
hmAgentRipRouteRedistMatchNSSAExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistMatchNSSAExternal2.setStatus(_A)
class _HmAgentRipRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_HmAgentRipRouteRedistDistList_Type.__name__=_J
_HmAgentRipRouteRedistDistList_Object=MibTableColumn
hmAgentRipRouteRedistDistList=_HmAgentRipRouteRedistDistList_Object((1,3,6,1,4,1,248,15,2,3,8,1,10),_HmAgentRipRouteRedistDistList_Type())
hmAgentRipRouteRedistDistList.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistDistList.setStatus(_A)
_HmAgentRipRouteRedistDistListConfigured_Type=TruthValue
_HmAgentRipRouteRedistDistListConfigured_Object=MibTableColumn
hmAgentRipRouteRedistDistListConfigured=_HmAgentRipRouteRedistDistListConfigured_Object((1,3,6,1,4,1,248,15,2,3,8,1,11),_HmAgentRipRouteRedistDistListConfigured_Type())
hmAgentRipRouteRedistDistListConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRipRouteRedistDistListConfigured.setStatus(_A)
_HmAgentRip2IfConfTable_Object=MibTable
hmAgentRip2IfConfTable=_HmAgentRip2IfConfTable_Object((1,3,6,1,4,1,248,15,2,3,9))
if mibBuilder.loadTexts:hmAgentRip2IfConfTable.setStatus(_A)
_HmAgentRip2IfConfEntry_Object=MibTableRow
hmAgentRip2IfConfEntry=_HmAgentRip2IfConfEntry_Object((1,3,6,1,4,1,248,15,2,3,9,1))
if mibBuilder.loadTexts:hmAgentRip2IfConfEntry.setStatus(_A)
class _HmAgentRip2IfConfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmAgentRip2IfConfAuthKeyId_Type.__name__=_C
_HmAgentRip2IfConfAuthKeyId_Object=MibTableColumn
hmAgentRip2IfConfAuthKeyId=_HmAgentRip2IfConfAuthKeyId_Object((1,3,6,1,4,1,248,15,2,3,9,1,1),_HmAgentRip2IfConfAuthKeyId_Type())
hmAgentRip2IfConfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentRip2IfConfAuthKeyId.setStatus(_A)
_HmAgentRip2InterfaceTable_Object=MibTable
hmAgentRip2InterfaceTable=_HmAgentRip2InterfaceTable_Object((1,3,6,1,4,1,248,15,2,3,10))
if mibBuilder.loadTexts:hmAgentRip2InterfaceTable.setStatus(_A)
_HmAgentRip2InterfaceEntry_Object=MibTableRow
hmAgentRip2InterfaceEntry=_HmAgentRip2InterfaceEntry_Object((1,3,6,1,4,1,248,15,2,3,10,1))
hmAgentRip2InterfaceEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:hmAgentRip2InterfaceEntry.setStatus(_A)
_HmAgentRip2InterfaceIfIndex_Type=Integer32
_HmAgentRip2InterfaceIfIndex_Object=MibTableColumn
hmAgentRip2InterfaceIfIndex=_HmAgentRip2InterfaceIfIndex_Object((1,3,6,1,4,1,248,15,2,3,10,1,1),_HmAgentRip2InterfaceIfIndex_Type())
hmAgentRip2InterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentRip2InterfaceIfIndex.setStatus(_A)
class _HmAgentRip2InterfaceAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthentication',1),('simplePassword',2),('md5',3)))
_HmAgentRip2InterfaceAuthType_Type.__name__=_C
_HmAgentRip2InterfaceAuthType_Object=MibTableColumn
hmAgentRip2InterfaceAuthType=_HmAgentRip2InterfaceAuthType_Object((1,3,6,1,4,1,248,15,2,3,10,1,2),_HmAgentRip2InterfaceAuthType_Type())
hmAgentRip2InterfaceAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRip2InterfaceAuthType.setStatus(_A)
class _HmAgentRip2InterfaceAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HmAgentRip2InterfaceAuthKey_Type.__name__=_R
_HmAgentRip2InterfaceAuthKey_Object=MibTableColumn
hmAgentRip2InterfaceAuthKey=_HmAgentRip2InterfaceAuthKey_Object((1,3,6,1,4,1,248,15,2,3,10,1,3),_HmAgentRip2InterfaceAuthKey_Type())
hmAgentRip2InterfaceAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRip2InterfaceAuthKey.setStatus(_A)
class _HmAgentRip2InterfaceAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmAgentRip2InterfaceAuthKeyId_Type.__name__=_C
_HmAgentRip2InterfaceAuthKeyId_Object=MibTableColumn
hmAgentRip2InterfaceAuthKeyId=_HmAgentRip2InterfaceAuthKeyId_Object((1,3,6,1,4,1,248,15,2,3,10,1,4),_HmAgentRip2InterfaceAuthKeyId_Type())
hmAgentRip2InterfaceAuthKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRip2InterfaceAuthKeyId.setStatus(_A)
class _HmAgentRip2InterfaceSendVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('doNotSend',1),('ripVersion1',2),('rip1Compatible',3),('ripVersion2',4)))
_HmAgentRip2InterfaceSendVersion_Type.__name__=_C
_HmAgentRip2InterfaceSendVersion_Object=MibTableColumn
hmAgentRip2InterfaceSendVersion=_HmAgentRip2InterfaceSendVersion_Object((1,3,6,1,4,1,248,15,2,3,10,1,5),_HmAgentRip2InterfaceSendVersion_Type())
hmAgentRip2InterfaceSendVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRip2InterfaceSendVersion.setStatus(_A)
class _HmAgentRip2InterfaceReceiveVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rip1',1),('rip2',2),('rip1OrRip2',3),('doNotReceive',4)))
_HmAgentRip2InterfaceReceiveVersion_Type.__name__=_C
_HmAgentRip2InterfaceReceiveVersion_Object=MibTableColumn
hmAgentRip2InterfaceReceiveVersion=_HmAgentRip2InterfaceReceiveVersion_Object((1,3,6,1,4,1,248,15,2,3,10,1,6),_HmAgentRip2InterfaceReceiveVersion_Type())
hmAgentRip2InterfaceReceiveVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRip2InterfaceReceiveVersion.setStatus(_A)
class _HmAgentRip2InterfaceAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRip2InterfaceAdminState_Type.__name__=_C
_HmAgentRip2InterfaceAdminState_Object=MibTableColumn
hmAgentRip2InterfaceAdminState=_HmAgentRip2InterfaceAdminState_Object((1,3,6,1,4,1,248,15,2,3,10,1,7),_HmAgentRip2InterfaceAdminState_Type())
hmAgentRip2InterfaceAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRip2InterfaceAdminState.setStatus(_A)
_HmAgentRip2RcvBadPackets_Type=Counter32
_HmAgentRip2RcvBadPackets_Object=MibTableColumn
hmAgentRip2RcvBadPackets=_HmAgentRip2RcvBadPackets_Object((1,3,6,1,4,1,248,15,2,3,10,1,8),_HmAgentRip2RcvBadPackets_Type())
hmAgentRip2RcvBadPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentRip2RcvBadPackets.setStatus(_A)
_HmAgentRip2RcvBadRoutes_Type=Counter32
_HmAgentRip2RcvBadRoutes_Object=MibTableColumn
hmAgentRip2RcvBadRoutes=_HmAgentRip2RcvBadRoutes_Object((1,3,6,1,4,1,248,15,2,3,10,1,9),_HmAgentRip2RcvBadRoutes_Type())
hmAgentRip2RcvBadRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentRip2RcvBadRoutes.setStatus(_A)
_HmAgentRip2SentUpdates_Type=Counter32
_HmAgentRip2SentUpdates_Object=MibTableColumn
hmAgentRip2SentUpdates=_HmAgentRip2SentUpdates_Object((1,3,6,1,4,1,248,15,2,3,10,1,10),_HmAgentRip2SentUpdates_Type())
hmAgentRip2SentUpdates.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentRip2SentUpdates.setStatus(_A)
class _HmAgentRouterRipUpdateTimerInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HmAgentRouterRipUpdateTimerInterval_Type.__name__=_C
_HmAgentRouterRipUpdateTimerInterval_Object=MibScalar
hmAgentRouterRipUpdateTimerInterval=_HmAgentRouterRipUpdateTimerInterval_Object((1,3,6,1,4,1,248,15,2,3,50),_HmAgentRouterRipUpdateTimerInterval_Type())
hmAgentRouterRipUpdateTimerInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterRipUpdateTimerInterval.setStatus(_A)
_HmAgentRouterOspfConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentRouterOspfConfigGroup=_HmAgentRouterOspfConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,4))
class _HmAgentOspfDefaultMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_HmAgentOspfDefaultMetric_Type.__name__=_C
_HmAgentOspfDefaultMetric_Object=MibScalar
hmAgentOspfDefaultMetric=_HmAgentOspfDefaultMetric_Object((1,3,6,1,4,1,248,15,2,4,1),_HmAgentOspfDefaultMetric_Type())
hmAgentOspfDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultMetric.setStatus(_A)
_HmAgentOspfDefaultMetricConfigured_Type=TruthValue
_HmAgentOspfDefaultMetricConfigured_Object=MibScalar
hmAgentOspfDefaultMetricConfigured=_HmAgentOspfDefaultMetricConfigured_Object((1,3,6,1,4,1,248,15,2,4,2),_HmAgentOspfDefaultMetricConfigured_Type())
hmAgentOspfDefaultMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultMetricConfigured.setStatus(_A)
class _HmAgentOspfDefaultInfoOriginate_Type(TruthValue):defaultValue=2
_HmAgentOspfDefaultInfoOriginate_Type.__name__=_K
_HmAgentOspfDefaultInfoOriginate_Object=MibScalar
hmAgentOspfDefaultInfoOriginate=_HmAgentOspfDefaultInfoOriginate_Object((1,3,6,1,4,1,248,15,2,4,3),_HmAgentOspfDefaultInfoOriginate_Type())
hmAgentOspfDefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultInfoOriginate.setStatus(_A)
class _HmAgentOspfDefaultInfoOriginateAlways_Type(TruthValue):defaultValue=2
_HmAgentOspfDefaultInfoOriginateAlways_Type.__name__=_K
_HmAgentOspfDefaultInfoOriginateAlways_Object=MibScalar
hmAgentOspfDefaultInfoOriginateAlways=_HmAgentOspfDefaultInfoOriginateAlways_Object((1,3,6,1,4,1,248,15,2,4,4),_HmAgentOspfDefaultInfoOriginateAlways_Type())
hmAgentOspfDefaultInfoOriginateAlways.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultInfoOriginateAlways.setStatus(_A)
class _HmAgentOspfDefaultInfoOriginateMetric_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_HmAgentOspfDefaultInfoOriginateMetric_Type.__name__=_C
_HmAgentOspfDefaultInfoOriginateMetric_Object=MibScalar
hmAgentOspfDefaultInfoOriginateMetric=_HmAgentOspfDefaultInfoOriginateMetric_Object((1,3,6,1,4,1,248,15,2,4,5),_HmAgentOspfDefaultInfoOriginateMetric_Type())
hmAgentOspfDefaultInfoOriginateMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultInfoOriginateMetric.setStatus(_A)
_HmAgentOspfDefaultInfoOriginateMetricConfigured_Type=TruthValue
_HmAgentOspfDefaultInfoOriginateMetricConfigured_Object=MibScalar
hmAgentOspfDefaultInfoOriginateMetricConfigured=_HmAgentOspfDefaultInfoOriginateMetricConfigured_Object((1,3,6,1,4,1,248,15,2,4,6),_HmAgentOspfDefaultInfoOriginateMetricConfigured_Type())
hmAgentOspfDefaultInfoOriginateMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultInfoOriginateMetricConfigured.setStatus(_A)
class _HmAgentOspfDefaultInfoOriginateMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_HmAgentOspfDefaultInfoOriginateMetricType_Type.__name__=_C
_HmAgentOspfDefaultInfoOriginateMetricType_Object=MibScalar
hmAgentOspfDefaultInfoOriginateMetricType=_HmAgentOspfDefaultInfoOriginateMetricType_Object((1,3,6,1,4,1,248,15,2,4,7),_HmAgentOspfDefaultInfoOriginateMetricType_Type())
hmAgentOspfDefaultInfoOriginateMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfDefaultInfoOriginateMetricType.setStatus(_A)
_HmAgentOspfRouteRedistTable_Object=MibTable
hmAgentOspfRouteRedistTable=_HmAgentOspfRouteRedistTable_Object((1,3,6,1,4,1,248,15,2,4,8))
if mibBuilder.loadTexts:hmAgentOspfRouteRedistTable.setStatus(_A)
_HmAgentOspfRouteRedistEntry_Object=MibTableRow
hmAgentOspfRouteRedistEntry=_HmAgentOspfRouteRedistEntry_Object((1,3,6,1,4,1,248,15,2,4,8,1))
hmAgentOspfRouteRedistEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:hmAgentOspfRouteRedistEntry.setStatus(_A)
class _HmAgentOspfRouteRedistSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_O,2),('rip',3),('bgp',4)))
_HmAgentOspfRouteRedistSource_Type.__name__=_C
_HmAgentOspfRouteRedistSource_Object=MibTableColumn
hmAgentOspfRouteRedistSource=_HmAgentOspfRouteRedistSource_Object((1,3,6,1,4,1,248,15,2,4,8,1,1),_HmAgentOspfRouteRedistSource_Type())
hmAgentOspfRouteRedistSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistSource.setStatus(_A)
class _HmAgentOspfRouteRedistMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentOspfRouteRedistMode_Type.__name__=_C
_HmAgentOspfRouteRedistMode_Object=MibTableColumn
hmAgentOspfRouteRedistMode=_HmAgentOspfRouteRedistMode_Object((1,3,6,1,4,1,248,15,2,4,8,1,2),_HmAgentOspfRouteRedistMode_Type())
hmAgentOspfRouteRedistMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistMode.setStatus(_A)
class _HmAgentOspfRouteRedistMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_HmAgentOspfRouteRedistMetric_Type.__name__=_C
_HmAgentOspfRouteRedistMetric_Object=MibTableColumn
hmAgentOspfRouteRedistMetric=_HmAgentOspfRouteRedistMetric_Object((1,3,6,1,4,1,248,15,2,4,8,1,3),_HmAgentOspfRouteRedistMetric_Type())
hmAgentOspfRouteRedistMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistMetric.setStatus(_A)
_HmAgentOspfRouteRedistMetricConfigured_Type=TruthValue
_HmAgentOspfRouteRedistMetricConfigured_Object=MibTableColumn
hmAgentOspfRouteRedistMetricConfigured=_HmAgentOspfRouteRedistMetricConfigured_Object((1,3,6,1,4,1,248,15,2,4,8,1,4),_HmAgentOspfRouteRedistMetricConfigured_Type())
hmAgentOspfRouteRedistMetricConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistMetricConfigured.setStatus(_A)
class _HmAgentOspfRouteRedistMetricType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_HmAgentOspfRouteRedistMetricType_Type.__name__=_C
_HmAgentOspfRouteRedistMetricType_Object=MibTableColumn
hmAgentOspfRouteRedistMetricType=_HmAgentOspfRouteRedistMetricType_Object((1,3,6,1,4,1,248,15,2,4,8,1,5),_HmAgentOspfRouteRedistMetricType_Type())
hmAgentOspfRouteRedistMetricType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistMetricType.setStatus(_A)
class _HmAgentOspfRouteRedistTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HmAgentOspfRouteRedistTag_Type.__name__=_J
_HmAgentOspfRouteRedistTag_Object=MibTableColumn
hmAgentOspfRouteRedistTag=_HmAgentOspfRouteRedistTag_Object((1,3,6,1,4,1,248,15,2,4,8,1,6),_HmAgentOspfRouteRedistTag_Type())
hmAgentOspfRouteRedistTag.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistTag.setStatus(_A)
class _HmAgentOspfRouteRedistSubnets_Type(TruthValue):defaultValue=2
_HmAgentOspfRouteRedistSubnets_Type.__name__=_K
_HmAgentOspfRouteRedistSubnets_Object=MibTableColumn
hmAgentOspfRouteRedistSubnets=_HmAgentOspfRouteRedistSubnets_Object((1,3,6,1,4,1,248,15,2,4,8,1,7),_HmAgentOspfRouteRedistSubnets_Type())
hmAgentOspfRouteRedistSubnets.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistSubnets.setStatus(_A)
class _HmAgentOspfRouteRedistDistList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
_HmAgentOspfRouteRedistDistList_Type.__name__=_J
_HmAgentOspfRouteRedistDistList_Object=MibTableColumn
hmAgentOspfRouteRedistDistList=_HmAgentOspfRouteRedistDistList_Object((1,3,6,1,4,1,248,15,2,4,8,1,8),_HmAgentOspfRouteRedistDistList_Type())
hmAgentOspfRouteRedistDistList.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistDistList.setStatus(_A)
_HmAgentOspfRouteRedistDistListConfigured_Type=TruthValue
_HmAgentOspfRouteRedistDistListConfigured_Object=MibTableColumn
hmAgentOspfRouteRedistDistListConfigured=_HmAgentOspfRouteRedistDistListConfigured_Object((1,3,6,1,4,1,248,15,2,4,8,1,9),_HmAgentOspfRouteRedistDistListConfigured_Type())
hmAgentOspfRouteRedistDistListConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfRouteRedistDistListConfigured.setStatus(_A)
_HmAgentOspfIfTable_Object=MibTable
hmAgentOspfIfTable=_HmAgentOspfIfTable_Object((1,3,6,1,4,1,248,15,2,4,9))
if mibBuilder.loadTexts:hmAgentOspfIfTable.setStatus(_A)
_HmAgentOspfIfEntry_Object=MibTableRow
hmAgentOspfIfEntry=_HmAgentOspfIfEntry_Object((1,3,6,1,4,1,248,15,2,4,9,1))
if mibBuilder.loadTexts:hmAgentOspfIfEntry.setStatus(_A)
class _HmAgentOspfIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmAgentOspfIfAuthKeyId_Type.__name__=_C
_HmAgentOspfIfAuthKeyId_Object=MibTableColumn
hmAgentOspfIfAuthKeyId=_HmAgentOspfIfAuthKeyId_Object((1,3,6,1,4,1,248,15,2,4,9,1,1),_HmAgentOspfIfAuthKeyId_Type())
hmAgentOspfIfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentOspfIfAuthKeyId.setStatus(_A)
class _HmAgentOspfIfIpMtuIgnoreFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentOspfIfIpMtuIgnoreFlag_Type.__name__=_C
_HmAgentOspfIfIpMtuIgnoreFlag_Object=MibTableColumn
hmAgentOspfIfIpMtuIgnoreFlag=_HmAgentOspfIfIpMtuIgnoreFlag_Object((1,3,6,1,4,1,248,15,2,4,9,1,2),_HmAgentOspfIfIpMtuIgnoreFlag_Type())
hmAgentOspfIfIpMtuIgnoreFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentOspfIfIpMtuIgnoreFlag.setStatus(_A)
_HmAgentOspfVirtIfTable_Object=MibTable
hmAgentOspfVirtIfTable=_HmAgentOspfVirtIfTable_Object((1,3,6,1,4,1,248,15,2,4,10))
if mibBuilder.loadTexts:hmAgentOspfVirtIfTable.setStatus(_A)
_HmAgentOspfVirtIfEntry_Object=MibTableRow
hmAgentOspfVirtIfEntry=_HmAgentOspfVirtIfEntry_Object((1,3,6,1,4,1,248,15,2,4,10,1))
if mibBuilder.loadTexts:hmAgentOspfVirtIfEntry.setStatus(_A)
class _HmAgentOspfVirtIfAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmAgentOspfVirtIfAuthKeyId_Type.__name__=_C
_HmAgentOspfVirtIfAuthKeyId_Object=MibTableColumn
hmAgentOspfVirtIfAuthKeyId=_HmAgentOspfVirtIfAuthKeyId_Object((1,3,6,1,4,1,248,15,2,4,10,1,1),_HmAgentOspfVirtIfAuthKeyId_Type())
hmAgentOspfVirtIfAuthKeyId.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentOspfVirtIfAuthKeyId.setStatus(_A)
class _HmAgentRouterOspfRFC1583CompatibilityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRouterOspfRFC1583CompatibilityMode_Type.__name__=_C
_HmAgentRouterOspfRFC1583CompatibilityMode_Object=MibScalar
hmAgentRouterOspfRFC1583CompatibilityMode=_HmAgentRouterOspfRFC1583CompatibilityMode_Object((1,3,6,1,4,1,248,15,2,4,11),_HmAgentRouterOspfRFC1583CompatibilityMode_Type())
hmAgentRouterOspfRFC1583CompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterOspfRFC1583CompatibilityMode.setStatus(_A)
_HmAgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity=ObjectIdentity
hmAgentSnmpTrapFlagsConfigGroupLayer3=_HmAgentSnmpTrapFlagsConfigGroupLayer3_ObjectIdentity((1,3,6,1,4,1,248,15,2,5))
class _HmAgentSnmpVRRPNewMasterTrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSnmpVRRPNewMasterTrapFlag_Type.__name__=_C
_HmAgentSnmpVRRPNewMasterTrapFlag_Object=MibScalar
hmAgentSnmpVRRPNewMasterTrapFlag=_HmAgentSnmpVRRPNewMasterTrapFlag_Object((1,3,6,1,4,1,248,15,2,5,1),_HmAgentSnmpVRRPNewMasterTrapFlag_Type())
hmAgentSnmpVRRPNewMasterTrapFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSnmpVRRPNewMasterTrapFlag.setStatus(_A)
class _HmAgentSnmpVRRPAuthFailureTrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSnmpVRRPAuthFailureTrapFlag_Type.__name__=_C
_HmAgentSnmpVRRPAuthFailureTrapFlag_Object=MibScalar
hmAgentSnmpVRRPAuthFailureTrapFlag=_HmAgentSnmpVRRPAuthFailureTrapFlag_Object((1,3,6,1,4,1,248,15,2,5,2),_HmAgentSnmpVRRPAuthFailureTrapFlag_Type())
hmAgentSnmpVRRPAuthFailureTrapFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentSnmpVRRPAuthFailureTrapFlag.setStatus(_A)
_HmAgentECMPGroup_ObjectIdentity=ObjectIdentity
hmAgentECMPGroup=_HmAgentECMPGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,7))
class _HmAgentECMPOspfMaxPaths_Type(Integer32):defaultValue=4
_HmAgentECMPOspfMaxPaths_Type.__name__=_C
_HmAgentECMPOspfMaxPaths_Object=MibScalar
hmAgentECMPOspfMaxPaths=_HmAgentECMPOspfMaxPaths_Object((1,3,6,1,4,1,248,15,2,7,1),_HmAgentECMPOspfMaxPaths_Type())
hmAgentECMPOspfMaxPaths.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentECMPOspfMaxPaths.setStatus(_A)
_HmAgentRouterVrrpConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentRouterVrrpConfigGroup=_HmAgentRouterVrrpConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,8))
class _HmAgentRouterVrrpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentRouterVrrpAdminState_Type.__name__=_C
_HmAgentRouterVrrpAdminState_Object=MibScalar
hmAgentRouterVrrpAdminState=_HmAgentRouterVrrpAdminState_Object((1,3,6,1,4,1,248,15,2,8,1),_HmAgentRouterVrrpAdminState_Type())
hmAgentRouterVrrpAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hmAgentRouterVrrpAdminState.setStatus(_A)
_HmVrrpExtGroup_ObjectIdentity=ObjectIdentity
hmVrrpExtGroup=_HmVrrpExtGroup_ObjectIdentity((1,3,6,1,4,1,248,15,2,9))
_HmVrrpTrackingTable_Object=MibTable
hmVrrpTrackingTable=_HmVrrpTrackingTable_Object((1,3,6,1,4,1,248,15,2,9,1))
if mibBuilder.loadTexts:hmVrrpTrackingTable.setStatus(_A)
_HmVrrpTrackingEntry_Object=MibTableRow
hmVrrpTrackingEntry=_HmVrrpTrackingEntry_Object((1,3,6,1,4,1,248,15,2,9,1,1))
hmVrrpTrackingEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:hmVrrpTrackingEntry.setStatus(_A)
_HmVrrpTrackIfIndex_Type=Integer32
_HmVrrpTrackIfIndex_Object=MibTableColumn
hmVrrpTrackIfIndex=_HmVrrpTrackIfIndex_Object((1,3,6,1,4,1,248,15,2,9,1,1,1),_HmVrrpTrackIfIndex_Type())
hmVrrpTrackIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hmVrrpTrackIfIndex.setStatus(_A)
class _HmVrrpTrackVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmVrrpTrackVrid_Type.__name__=_C
_HmVrrpTrackVrid_Object=MibTableColumn
hmVrrpTrackVrid=_HmVrrpTrackVrid_Object((1,3,6,1,4,1,248,15,2,9,1,1,2),_HmVrrpTrackVrid_Type())
hmVrrpTrackVrid.setMaxAccess(_H)
if mibBuilder.loadTexts:hmVrrpTrackVrid.setStatus(_A)
_HmVrrpTrackId_Type=Integer32
_HmVrrpTrackId_Object=MibTableColumn
hmVrrpTrackId=_HmVrrpTrackId_Object((1,3,6,1,4,1,248,15,2,9,1,1,3),_HmVrrpTrackId_Type())
hmVrrpTrackId.setMaxAccess(_H)
if mibBuilder.loadTexts:hmVrrpTrackId.setStatus(_A)
class _HmVrrpTrackDecrement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,253))
_HmVrrpTrackDecrement_Type.__name__=_C
_HmVrrpTrackDecrement_Object=MibTableColumn
hmVrrpTrackDecrement=_HmVrrpTrackDecrement_Object((1,3,6,1,4,1,248,15,2,9,1,1,4),_HmVrrpTrackDecrement_Type())
hmVrrpTrackDecrement.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpTrackDecrement.setStatus(_A)
class _HmVrrpTrackOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HmVrrpTrackOperStatus_Type.__name__=_C
_HmVrrpTrackOperStatus_Object=MibTableColumn
hmVrrpTrackOperStatus=_HmVrrpTrackOperStatus_Object((1,3,6,1,4,1,248,15,2,9,1,1,5),_HmVrrpTrackOperStatus_Type())
hmVrrpTrackOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpTrackOperStatus.setStatus(_A)
_HmVrrpTrackRowStatus_Type=RowStatus
_HmVrrpTrackRowStatus_Object=MibTableColumn
hmVrrpTrackRowStatus=_HmVrrpTrackRowStatus_Object((1,3,6,1,4,1,248,15,2,9,1,1,6),_HmVrrpTrackRowStatus_Type())
hmVrrpTrackRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hmVrrpTrackRowStatus.setStatus(_A)
_HmVrrpExtTable_Object=MibTable
hmVrrpExtTable=_HmVrrpExtTable_Object((1,3,6,1,4,1,248,15,2,9,2))
if mibBuilder.loadTexts:hmVrrpExtTable.setStatus(_A)
_HmVrrpExtEntry_Object=MibTableRow
hmVrrpExtEntry=_HmVrrpExtEntry_Object((1,3,6,1,4,1,248,15,2,9,2,1))
hmVrrpExtEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:hmVrrpExtEntry.setStatus(_A)
_HmVrrpExtIfIndex_Type=Integer32
_HmVrrpExtIfIndex_Object=MibTableColumn
hmVrrpExtIfIndex=_HmVrrpExtIfIndex_Object((1,3,6,1,4,1,248,15,2,9,2,1,1),_HmVrrpExtIfIndex_Type())
hmVrrpExtIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hmVrrpExtIfIndex.setStatus(_A)
class _HmVrrpExtVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmVrrpExtVrid_Type.__name__=_C
_HmVrrpExtVrid_Object=MibTableColumn
hmVrrpExtVrid=_HmVrrpExtVrid_Object((1,3,6,1,4,1,248,15,2,9,2,1,2),_HmVrrpExtVrid_Type())
hmVrrpExtVrid.setMaxAccess(_H)
if mibBuilder.loadTexts:hmVrrpExtVrid.setStatus(_A)
class _HmVrrpExtDomainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_HmVrrpExtDomainId_Type.__name__=_C
_HmVrrpExtDomainId_Object=MibTableColumn
hmVrrpExtDomainId=_HmVrrpExtDomainId_Object((1,3,6,1,4,1,248,15,2,9,2,1,3),_HmVrrpExtDomainId_Type())
hmVrrpExtDomainId.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtDomainId.setStatus(_A)
class _HmVrrpExtDomainRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('member',2),('supervisor',3)))
_HmVrrpExtDomainRole_Type.__name__=_C
_HmVrrpExtDomainRole_Object=MibTableColumn
hmVrrpExtDomainRole=_HmVrrpExtDomainRole_Object((1,3,6,1,4,1,248,15,2,9,2,1,4),_HmVrrpExtDomainRole_Type())
hmVrrpExtDomainRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtDomainRole.setStatus(_A)
class _HmVrrpExtDomainStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_HmVrrpExtDomainStatus_Type.__name__=_C
_HmVrrpExtDomainStatus_Object=MibTableColumn
hmVrrpExtDomainStatus=_HmVrrpExtDomainStatus_Object((1,3,6,1,4,1,248,15,2,9,2,1,5),_HmVrrpExtDomainStatus_Type())
hmVrrpExtDomainStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpExtDomainStatus.setStatus(_A)
_HmVrrpExtAdvertAddress_Type=IpAddress
_HmVrrpExtAdvertAddress_Object=MibTableColumn
hmVrrpExtAdvertAddress=_HmVrrpExtAdvertAddress_Object((1,3,6,1,4,1,248,15,2,9,2,1,6),_HmVrrpExtAdvertAddress_Type())
hmVrrpExtAdvertAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtAdvertAddress.setStatus(_A)
class _HmVrrpExtAdvertTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,255000))
_HmVrrpExtAdvertTimer_Type.__name__=_C
_HmVrrpExtAdvertTimer_Object=MibTableColumn
hmVrrpExtAdvertTimer=_HmVrrpExtAdvertTimer_Object((1,3,6,1,4,1,248,15,2,9,2,1,7),_HmVrrpExtAdvertTimer_Type())
hmVrrpExtAdvertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtAdvertTimer.setStatus(_A)
if mibBuilder.loadTexts:hmVrrpExtAdvertTimer.setUnits('milliseconds')
class _HmVrrpExtOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmVrrpExtOperPriority_Type.__name__=_C
_HmVrrpExtOperPriority_Object=MibTableColumn
hmVrrpExtOperPriority=_HmVrrpExtOperPriority_Object((1,3,6,1,4,1,248,15,2,9,2,1,8),_HmVrrpExtOperPriority_Type())
hmVrrpExtOperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpExtOperPriority.setStatus(_A)
_HmVrrpExtNotifyAddress_Type=IpAddress
_HmVrrpExtNotifyAddress_Object=MibTableColumn
hmVrrpExtNotifyAddress=_HmVrrpExtNotifyAddress_Object((1,3,6,1,4,1,248,15,2,9,2,1,9),_HmVrrpExtNotifyAddress_Type())
hmVrrpExtNotifyAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtNotifyAddress.setStatus(_A)
class _HmVrrpExtNotifyLinkdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmVrrpExtNotifyLinkdown_Type.__name__=_C
_HmVrrpExtNotifyLinkdown_Object=MibTableColumn
hmVrrpExtNotifyLinkdown=_HmVrrpExtNotifyLinkdown_Object((1,3,6,1,4,1,248,15,2,9,2,1,10),_HmVrrpExtNotifyLinkdown_Type())
hmVrrpExtNotifyLinkdown.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtNotifyLinkdown.setStatus(_A)
class _HmVrrpExtPreemptionDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmVrrpExtPreemptionDelay_Type.__name__=_C
_HmVrrpExtPreemptionDelay_Object=MibTableColumn
hmVrrpExtPreemptionDelay=_HmVrrpExtPreemptionDelay_Object((1,3,6,1,4,1,248,15,2,9,2,1,11),_HmVrrpExtPreemptionDelay_Type())
hmVrrpExtPreemptionDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpExtPreemptionDelay.setStatus(_A)
_HmVrrpDomainTable_Object=MibTable
hmVrrpDomainTable=_HmVrrpDomainTable_Object((1,3,6,1,4,1,248,15,2,9,3))
if mibBuilder.loadTexts:hmVrrpDomainTable.setStatus(_A)
_HmVrrpDomainEntry_Object=MibTableRow
hmVrrpDomainEntry=_HmVrrpDomainEntry_Object((1,3,6,1,4,1,248,15,2,9,3,1))
hmVrrpDomainEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:hmVrrpDomainEntry.setStatus(_A)
class _HmVrrpDomainId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_HmVrrpDomainId_Type.__name__=_C
_HmVrrpDomainId_Object=MibTableColumn
hmVrrpDomainId=_HmVrrpDomainId_Object((1,3,6,1,4,1,248,15,2,9,3,1,1),_HmVrrpDomainId_Type())
hmVrrpDomainId.setMaxAccess(_H)
if mibBuilder.loadTexts:hmVrrpDomainId.setStatus(_A)
class _HmVrrpDomainMemberSendAdv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HmVrrpDomainMemberSendAdv_Type.__name__=_C
_HmVrrpDomainMemberSendAdv_Object=MibTableColumn
hmVrrpDomainMemberSendAdv=_HmVrrpDomainMemberSendAdv_Object((1,3,6,1,4,1,248,15,2,9,3,1,2),_HmVrrpDomainMemberSendAdv_Type())
hmVrrpDomainMemberSendAdv.setMaxAccess(_B)
if mibBuilder.loadTexts:hmVrrpDomainMemberSendAdv.setStatus(_A)
class _HmVrrpDomainStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_HmVrrpDomainStatus_Type.__name__=_C
_HmVrrpDomainStatus_Object=MibTableColumn
hmVrrpDomainStatus=_HmVrrpDomainStatus_Object((1,3,6,1,4,1,248,15,2,9,3,1,3),_HmVrrpDomainStatus_Type())
hmVrrpDomainStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpDomainStatus.setStatus(_A)
_HmVrrpDomainSupervisorIfIndex_Type=Integer32
_HmVrrpDomainSupervisorIfIndex_Object=MibTableColumn
hmVrrpDomainSupervisorIfIndex=_HmVrrpDomainSupervisorIfIndex_Object((1,3,6,1,4,1,248,15,2,9,3,1,4),_HmVrrpDomainSupervisorIfIndex_Type())
hmVrrpDomainSupervisorIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpDomainSupervisorIfIndex.setStatus(_A)
class _HmVrrpDomainSupervisorVrid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmVrrpDomainSupervisorVrid_Type.__name__=_C
_HmVrrpDomainSupervisorVrid_Object=MibTableColumn
hmVrrpDomainSupervisorVrid=_HmVrrpDomainSupervisorVrid_Object((1,3,6,1,4,1,248,15,2,9,3,1,5),_HmVrrpDomainSupervisorVrid_Type())
hmVrrpDomainSupervisorVrid.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpDomainSupervisorVrid.setStatus(_A)
class _HmVrrpDomainOperPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmVrrpDomainOperPriority_Type.__name__=_C
_HmVrrpDomainOperPriority_Object=MibTableColumn
hmVrrpDomainOperPriority=_HmVrrpDomainOperPriority_Object((1,3,6,1,4,1,248,15,2,9,3,1,6),_HmVrrpDomainOperPriority_Type())
hmVrrpDomainOperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpDomainOperPriority.setStatus(_A)
class _HmVrrpDomainSupervisorOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3),('unknown',4)))
_HmVrrpDomainSupervisorOperState_Type.__name__=_C
_HmVrrpDomainSupervisorOperState_Object=MibTableColumn
hmVrrpDomainSupervisorOperState=_HmVrrpDomainSupervisorOperState_Object((1,3,6,1,4,1,248,15,2,9,3,1,7),_HmVrrpDomainSupervisorOperState_Type())
hmVrrpDomainSupervisorOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmVrrpDomainSupervisorOperState.setStatus(_A)
rip2IfConfEntry.registerAugmentions((_E,_p))
hmAgentRip2IfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())
ospfIfEntry.registerAugmentions((_E,_q))
hmAgentOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions((_E,_r))
hmAgentOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'hmPlatform4Routing':hmPlatform4Routing,'hmAgentSwitchArpGroup':hmAgentSwitchArpGroup,'hmAgentSwitchArpAgeoutTime':hmAgentSwitchArpAgeoutTime,'hmAgentSwitchArpResponseTime':hmAgentSwitchArpResponseTime,'hmAgentSwitchArpMaxRetries':hmAgentSwitchArpMaxRetries,'hmAgentSwitchArpCacheSize':hmAgentSwitchArpCacheSize,'hmAgentSwitchArpDynamicRenew':hmAgentSwitchArpDynamicRenew,'hmAgentSwitchArpTotalEntryCountCurrent':hmAgentSwitchArpTotalEntryCountCurrent,'hmAgentSwitchArpTotalEntryCountPeak':hmAgentSwitchArpTotalEntryCountPeak,'hmAgentSwitchArpStaticEntryCountCurrent':hmAgentSwitchArpStaticEntryCountCurrent,'hmAgentSwitchArpStaticEntryCountMax':hmAgentSwitchArpStaticEntryCountMax,'hmAgentSwitchArpTable':hmAgentSwitchArpTable,'hmAgentSwitchArpEntry':hmAgentSwitchArpEntry,'hmAgentSwitchArpAge':hmAgentSwitchArpAge,_T:hmAgentSwitchArpIpAddress,'hmAgentSwitchArpMacAddress':hmAgentSwitchArpMacAddress,'hmAgentSwitchArpInterface':hmAgentSwitchArpInterface,'hmAgentSwitchArpType':hmAgentSwitchArpType,'hmAgentSwitchArpStatus':hmAgentSwitchArpStatus,'hmAgentSwitchArpSparseLearn':hmAgentSwitchArpSparseLearn,'hmAgentSwitchIpGroup':hmAgentSwitchIpGroup,'hmAgentSwitchIpRoutingMode':hmAgentSwitchIpRoutingMode,'hmAgentSwitchIpVRRPMode':hmAgentSwitchIpVRRPMode,'hmAgentSwitchIpInterfaceTable':hmAgentSwitchIpInterfaceTable,'hmAgentSwitchIpInterfaceEntry':hmAgentSwitchIpInterfaceEntry,_P:hmAgentSwitchIpInterfaceIfIndex,'hmAgentSwitchIpInterfaceIpAddress':hmAgentSwitchIpInterfaceIpAddress,'hmAgentSwitchIpInterfaceNetMask':hmAgentSwitchIpInterfaceNetMask,'hmAgentSwitchIpInterfaceClearIp':hmAgentSwitchIpInterfaceClearIp,'hmAgentSwitchIpInterfaceRoutingMode':hmAgentSwitchIpInterfaceRoutingMode,'hmAgentSwitchIpInterfaceProxyARPMode':hmAgentSwitchIpInterfaceProxyARPMode,'hmAgentSwitchIpInterfaceMtuValue':hmAgentSwitchIpInterfaceMtuValue,'hmAgentSwitchIpInterfaceSlotNum':hmAgentSwitchIpInterfaceSlotNum,'hmAgentSwitchIpInterfacePortNum':hmAgentSwitchIpInterfacePortNum,'hmAgentSwitchIpInterfaceNetdirectedBCMode':hmAgentSwitchIpInterfaceNetdirectedBCMode,'hmAgentSwitchIpRouterDiscoveryTable':hmAgentSwitchIpRouterDiscoveryTable,'hmAgentSwitchIpRouterDiscoveryEntry':hmAgentSwitchIpRouterDiscoveryEntry,_U:hmAgentSwitchIpRouterDiscoveryIfIndex,'hmAgentSwitchIpRouterDiscoveryAdvertiseMode':hmAgentSwitchIpRouterDiscoveryAdvertiseMode,'hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval':hmAgentSwitchIpRouterDiscoveryMaxAdvertisementInterval,'hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval':hmAgentSwitchIpRouterDiscoveryMinAdvertisementInterval,'hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime':hmAgentSwitchIpRouterDiscoveryAdvertisementLifetime,'hmAgentSwitchIpRouterDiscoveryPreferenceLevel':hmAgentSwitchIpRouterDiscoveryPreferenceLevel,'hmAgentSwitchIpRouterDiscoveryAdvertisementAddress':hmAgentSwitchIpRouterDiscoveryAdvertisementAddress,'hmAgentSwitchIpVlanTable':hmAgentSwitchIpVlanTable,'hmAgentSwitchIpVlanEntry':hmAgentSwitchIpVlanEntry,_V:hmAgentSwitchIpVlanId,'hmAgentSwitchIpVlanIfIndex':hmAgentSwitchIpVlanIfIndex,'hmAgentSwitchIpVlanRoutingStatus':hmAgentSwitchIpVlanRoutingStatus,'hmAgentSwitchSecondaryAddressTable':hmAgentSwitchSecondaryAddressTable,'hmAgentSwitchSecondaryAddressEntry':hmAgentSwitchSecondaryAddressEntry,_W:hmAgentSwitchSecondaryIpAddress,'hmAgentSwitchSecondaryNetMask':hmAgentSwitchSecondaryNetMask,'hmAgentSwitchSecondaryStatus':hmAgentSwitchSecondaryStatus,'hmAgentSwitchIpRoutePreferenceTable':hmAgentSwitchIpRoutePreferenceTable,'hmAgentSwitchIpRoutePreferenceEntry':hmAgentSwitchIpRoutePreferenceEntry,_X:hmAgentSwitchIpRoutePreferenceSource,'hmAgentSwitchIpRoutePreferenceValue':hmAgentSwitchIpRoutePreferenceValue,'hmAgentSwitchIpRouteStaticTable':hmAgentSwitchIpRouteStaticTable,'hmAgentSwitchIpRouteStaticEntry':hmAgentSwitchIpRouteStaticEntry,_Y:hmAgentSwitchIpRouteStaticDestination,_Z:hmAgentSwitchIpRouteStaticDestinationMask,_a:hmAgentSwitchIpRouteStaticNextHop,'hmAgentSwitchIpRouteStaticPreference':hmAgentSwitchIpRouteStaticPreference,'hmAgentSwitchIpRouteStaticStatus':hmAgentSwitchIpRouteStaticStatus,'hmAgentSwitchIpRouteStaticTrackId':hmAgentSwitchIpRouteStaticTrackId,'hmAgentSwitchIpVlanSingleMacMode':hmAgentSwitchIpVlanSingleMacMode,'hmAgentSwitchIpTableSizesGroup':hmAgentSwitchIpTableSizesGroup,'hmAgentSwitchIpTableSizeArp':hmAgentSwitchIpTableSizeArp,'hmAgentSwitchIpTableSizeUCRoutes':hmAgentSwitchIpTableSizeUCRoutes,'hmAgentSwitchIpTableSizeMCRoutes':hmAgentSwitchIpTableSizeMCRoutes,'hmAgentSwitchIpCurrentTableSizeArp':hmAgentSwitchIpCurrentTableSizeArp,'hmAgentSwitchIpCurrentTableSizeUCRoutes':hmAgentSwitchIpCurrentTableSizeUCRoutes,'hmAgentSwitchIpCurrentTableSizeMCRoutes':hmAgentSwitchIpCurrentTableSizeMCRoutes,'hmAgentRouterRipConfigGroup':hmAgentRouterRipConfigGroup,'hmAgentRouterRipAdminState':hmAgentRouterRipAdminState,'hmAgentRouterRipSplitHorizonMode':hmAgentRouterRipSplitHorizonMode,'hmAgentRouterRipAutoSummaryMode':hmAgentRouterRipAutoSummaryMode,'hmAgentRouterRipHostRoutesAcceptMode':hmAgentRouterRipHostRoutesAcceptMode,'hmAgentRouterRipDefaultMetric':hmAgentRouterRipDefaultMetric,'hmAgentRouterRipDefaultMetricConfigured':hmAgentRouterRipDefaultMetricConfigured,'hmAgentRouterRipDefaultInfoOriginate':hmAgentRouterRipDefaultInfoOriginate,'hmAgentRipRouteRedistTable':hmAgentRipRouteRedistTable,'hmAgentRipRouteRedistEntry':hmAgentRipRouteRedistEntry,_b:hmAgentRipRouteRedistSource,'hmAgentRipRouteRedistMode':hmAgentRipRouteRedistMode,'hmAgentRipRouteRedistMetric':hmAgentRipRouteRedistMetric,'hmAgentRipRouteRedistMetricConfigured':hmAgentRipRouteRedistMetricConfigured,'hmAgentRipRouteRedistMatchInternal':hmAgentRipRouteRedistMatchInternal,'hmAgentRipRouteRedistMatchExternal1':hmAgentRipRouteRedistMatchExternal1,'hmAgentRipRouteRedistMatchExternal2':hmAgentRipRouteRedistMatchExternal2,'hmAgentRipRouteRedistMatchNSSAExternal1':hmAgentRipRouteRedistMatchNSSAExternal1,'hmAgentRipRouteRedistMatchNSSAExternal2':hmAgentRipRouteRedistMatchNSSAExternal2,'hmAgentRipRouteRedistDistList':hmAgentRipRouteRedistDistList,'hmAgentRipRouteRedistDistListConfigured':hmAgentRipRouteRedistDistListConfigured,'hmAgentRip2IfConfTable':hmAgentRip2IfConfTable,_p:hmAgentRip2IfConfEntry,'hmAgentRip2IfConfAuthKeyId':hmAgentRip2IfConfAuthKeyId,'hmAgentRip2InterfaceTable':hmAgentRip2InterfaceTable,'hmAgentRip2InterfaceEntry':hmAgentRip2InterfaceEntry,_c:hmAgentRip2InterfaceIfIndex,'hmAgentRip2InterfaceAuthType':hmAgentRip2InterfaceAuthType,'hmAgentRip2InterfaceAuthKey':hmAgentRip2InterfaceAuthKey,'hmAgentRip2InterfaceAuthKeyId':hmAgentRip2InterfaceAuthKeyId,'hmAgentRip2InterfaceSendVersion':hmAgentRip2InterfaceSendVersion,'hmAgentRip2InterfaceReceiveVersion':hmAgentRip2InterfaceReceiveVersion,'hmAgentRip2InterfaceAdminState':hmAgentRip2InterfaceAdminState,'hmAgentRip2RcvBadPackets':hmAgentRip2RcvBadPackets,'hmAgentRip2RcvBadRoutes':hmAgentRip2RcvBadRoutes,'hmAgentRip2SentUpdates':hmAgentRip2SentUpdates,'hmAgentRouterRipUpdateTimerInterval':hmAgentRouterRipUpdateTimerInterval,'hmAgentRouterOspfConfigGroup':hmAgentRouterOspfConfigGroup,'hmAgentOspfDefaultMetric':hmAgentOspfDefaultMetric,'hmAgentOspfDefaultMetricConfigured':hmAgentOspfDefaultMetricConfigured,'hmAgentOspfDefaultInfoOriginate':hmAgentOspfDefaultInfoOriginate,'hmAgentOspfDefaultInfoOriginateAlways':hmAgentOspfDefaultInfoOriginateAlways,'hmAgentOspfDefaultInfoOriginateMetric':hmAgentOspfDefaultInfoOriginateMetric,'hmAgentOspfDefaultInfoOriginateMetricConfigured':hmAgentOspfDefaultInfoOriginateMetricConfigured,'hmAgentOspfDefaultInfoOriginateMetricType':hmAgentOspfDefaultInfoOriginateMetricType,'hmAgentOspfRouteRedistTable':hmAgentOspfRouteRedistTable,'hmAgentOspfRouteRedistEntry':hmAgentOspfRouteRedistEntry,_f:hmAgentOspfRouteRedistSource,'hmAgentOspfRouteRedistMode':hmAgentOspfRouteRedistMode,'hmAgentOspfRouteRedistMetric':hmAgentOspfRouteRedistMetric,'hmAgentOspfRouteRedistMetricConfigured':hmAgentOspfRouteRedistMetricConfigured,'hmAgentOspfRouteRedistMetricType':hmAgentOspfRouteRedistMetricType,'hmAgentOspfRouteRedistTag':hmAgentOspfRouteRedistTag,'hmAgentOspfRouteRedistSubnets':hmAgentOspfRouteRedistSubnets,'hmAgentOspfRouteRedistDistList':hmAgentOspfRouteRedistDistList,'hmAgentOspfRouteRedistDistListConfigured':hmAgentOspfRouteRedistDistListConfigured,'hmAgentOspfIfTable':hmAgentOspfIfTable,_q:hmAgentOspfIfEntry,'hmAgentOspfIfAuthKeyId':hmAgentOspfIfAuthKeyId,'hmAgentOspfIfIpMtuIgnoreFlag':hmAgentOspfIfIpMtuIgnoreFlag,'hmAgentOspfVirtIfTable':hmAgentOspfVirtIfTable,_r:hmAgentOspfVirtIfEntry,'hmAgentOspfVirtIfAuthKeyId':hmAgentOspfVirtIfAuthKeyId,'hmAgentRouterOspfRFC1583CompatibilityMode':hmAgentRouterOspfRFC1583CompatibilityMode,'hmAgentSnmpTrapFlagsConfigGroupLayer3':hmAgentSnmpTrapFlagsConfigGroupLayer3,'hmAgentSnmpVRRPNewMasterTrapFlag':hmAgentSnmpVRRPNewMasterTrapFlag,'hmAgentSnmpVRRPAuthFailureTrapFlag':hmAgentSnmpVRRPAuthFailureTrapFlag,'hmAgentECMPGroup':hmAgentECMPGroup,'hmAgentECMPOspfMaxPaths':hmAgentECMPOspfMaxPaths,'hmAgentRouterVrrpConfigGroup':hmAgentRouterVrrpConfigGroup,'hmAgentRouterVrrpAdminState':hmAgentRouterVrrpAdminState,'hmVrrpExtGroup':hmVrrpExtGroup,'hmVrrpTrackingTable':hmVrrpTrackingTable,'hmVrrpTrackingEntry':hmVrrpTrackingEntry,_g:hmVrrpTrackIfIndex,_h:hmVrrpTrackVrid,_i:hmVrrpTrackId,'hmVrrpTrackDecrement':hmVrrpTrackDecrement,'hmVrrpTrackOperStatus':hmVrrpTrackOperStatus,'hmVrrpTrackRowStatus':hmVrrpTrackRowStatus,'hmVrrpExtTable':hmVrrpExtTable,'hmVrrpExtEntry':hmVrrpExtEntry,_j:hmVrrpExtIfIndex,_k:hmVrrpExtVrid,'hmVrrpExtDomainId':hmVrrpExtDomainId,'hmVrrpExtDomainRole':hmVrrpExtDomainRole,'hmVrrpExtDomainStatus':hmVrrpExtDomainStatus,'hmVrrpExtAdvertAddress':hmVrrpExtAdvertAddress,'hmVrrpExtAdvertTimer':hmVrrpExtAdvertTimer,'hmVrrpExtOperPriority':hmVrrpExtOperPriority,'hmVrrpExtNotifyAddress':hmVrrpExtNotifyAddress,'hmVrrpExtNotifyLinkdown':hmVrrpExtNotifyLinkdown,'hmVrrpExtPreemptionDelay':hmVrrpExtPreemptionDelay,'hmVrrpDomainTable':hmVrrpDomainTable,'hmVrrpDomainEntry':hmVrrpDomainEntry,_o:hmVrrpDomainId,'hmVrrpDomainMemberSendAdv':hmVrrpDomainMemberSendAdv,'hmVrrpDomainStatus':hmVrrpDomainStatus,'hmVrrpDomainSupervisorIfIndex':hmVrrpDomainSupervisorIfIndex,'hmVrrpDomainSupervisorVrid':hmVrrpDomainSupervisorVrid,'hmVrrpDomainOperPriority':hmVrrpDomainOperPriority,'hmVrrpDomainSupervisorOperState':hmVrrpDomainSupervisorOperState})