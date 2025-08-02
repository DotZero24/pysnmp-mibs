_c='agentEcmpNextHopCount'
_b='agentSwitchInternalVlanId'
_a='agentSwitchIpHelperUdpPort'
_Z='agentSwitchIpHelperAddress'
_Y='agentSwitchIntfIpHelperIpAddress'
_X='agentSwitchIntfIpHelperUdpPort'
_W='agentSwitchHelperIpAddress'
_V='agentSwitchSecondaryIpAddress'
_U='agentSwitchIpVlanId'
_T='agentSwitchIpRouterDiscoveryIfIndex'
_S='agentSwitchIntfArpIfIndex'
_R='agentSwitchIntfArpIpAddress'
_Q='dynamic'
_P='static'
_O='gateway'
_N='agentSwitchArpIpAddress'
_M='IpAddress'
_L='agentSwitchIpInterfaceIfIndex'
_K='not-accessible'
_J='Unsigned32'
_I='read-create'
_H='disable'
_G='enable'
_F='NG700-ROUTING-MIB'
_E='obsolete'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
ng700smartswitch,=mibBuilder.importSymbols('NG700-REF-MIB','ng700smartswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_M,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathRouting=ModuleIdentity((1,3,6,1,4,1,4526,11,2))
if mibBuilder.loadTexts:fastPathRouting.setRevisions(('2011-01-26 00:00','2007-05-23 00:00','2003-11-21 00:00','2003-04-02 17:00'))
class SpfTimerRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchArpGroup_ObjectIdentity=ObjectIdentity
agentSwitchArpGroup=_AgentSwitchArpGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,1))
class _AgentSwitchArpAgeoutTime_Type(Integer32):defaultValue=1200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,21600))
_AgentSwitchArpAgeoutTime_Type.__name__=_D
_AgentSwitchArpAgeoutTime_Object=MibScalar
agentSwitchArpAgeoutTime=_AgentSwitchArpAgeoutTime_Object((1,3,6,1,4,1,4526,11,2,1,1),_AgentSwitchArpAgeoutTime_Type())
agentSwitchArpAgeoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpAgeoutTime.setStatus(_A)
class _AgentSwitchArpResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgentSwitchArpResponseTime_Type.__name__=_D
_AgentSwitchArpResponseTime_Object=MibScalar
agentSwitchArpResponseTime=_AgentSwitchArpResponseTime_Object((1,3,6,1,4,1,4526,11,2,1,2),_AgentSwitchArpResponseTime_Type())
agentSwitchArpResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpResponseTime.setStatus(_A)
class _AgentSwitchArpMaxRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AgentSwitchArpMaxRetries_Type.__name__=_D
_AgentSwitchArpMaxRetries_Object=MibScalar
agentSwitchArpMaxRetries=_AgentSwitchArpMaxRetries_Object((1,3,6,1,4,1,4526,11,2,1,3),_AgentSwitchArpMaxRetries_Type())
agentSwitchArpMaxRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpMaxRetries.setStatus(_A)
_AgentSwitchArpCacheSize_Type=Integer32
_AgentSwitchArpCacheSize_Object=MibScalar
agentSwitchArpCacheSize=_AgentSwitchArpCacheSize_Object((1,3,6,1,4,1,4526,11,2,1,4),_AgentSwitchArpCacheSize_Type())
agentSwitchArpCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpCacheSize.setStatus(_A)
class _AgentSwitchArpDynamicRenew_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchArpDynamicRenew_Type.__name__=_D
_AgentSwitchArpDynamicRenew_Object=MibScalar
agentSwitchArpDynamicRenew=_AgentSwitchArpDynamicRenew_Object((1,3,6,1,4,1,4526,11,2,1,5),_AgentSwitchArpDynamicRenew_Type())
agentSwitchArpDynamicRenew.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpDynamicRenew.setStatus(_A)
_AgentSwitchArpTotalEntryCountCurrent_Type=Gauge32
_AgentSwitchArpTotalEntryCountCurrent_Object=MibScalar
agentSwitchArpTotalEntryCountCurrent=_AgentSwitchArpTotalEntryCountCurrent_Object((1,3,6,1,4,1,4526,11,2,1,6),_AgentSwitchArpTotalEntryCountCurrent_Type())
agentSwitchArpTotalEntryCountCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpTotalEntryCountCurrent.setStatus(_A)
_AgentSwitchArpTotalEntryCountPeak_Type=Gauge32
_AgentSwitchArpTotalEntryCountPeak_Object=MibScalar
agentSwitchArpTotalEntryCountPeak=_AgentSwitchArpTotalEntryCountPeak_Object((1,3,6,1,4,1,4526,11,2,1,7),_AgentSwitchArpTotalEntryCountPeak_Type())
agentSwitchArpTotalEntryCountPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpTotalEntryCountPeak.setStatus(_A)
_AgentSwitchArpStaticEntryCountCurrent_Type=Gauge32
_AgentSwitchArpStaticEntryCountCurrent_Object=MibScalar
agentSwitchArpStaticEntryCountCurrent=_AgentSwitchArpStaticEntryCountCurrent_Object((1,3,6,1,4,1,4526,11,2,1,8),_AgentSwitchArpStaticEntryCountCurrent_Type())
agentSwitchArpStaticEntryCountCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpStaticEntryCountCurrent.setStatus(_A)
_AgentSwitchArpStaticEntryCountMax_Type=Integer32
_AgentSwitchArpStaticEntryCountMax_Object=MibScalar
agentSwitchArpStaticEntryCountMax=_AgentSwitchArpStaticEntryCountMax_Object((1,3,6,1,4,1,4526,11,2,1,9),_AgentSwitchArpStaticEntryCountMax_Type())
agentSwitchArpStaticEntryCountMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpStaticEntryCountMax.setStatus(_A)
_AgentSwitchArpTable_Object=MibTable
agentSwitchArpTable=_AgentSwitchArpTable_Object((1,3,6,1,4,1,4526,11,2,1,10))
if mibBuilder.loadTexts:agentSwitchArpTable.setStatus(_E)
_AgentSwitchArpEntry_Object=MibTableRow
agentSwitchArpEntry=_AgentSwitchArpEntry_Object((1,3,6,1,4,1,4526,11,2,1,10,1))
agentSwitchArpEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:agentSwitchArpEntry.setStatus(_E)
_AgentSwitchArpAge_Type=TimeTicks
_AgentSwitchArpAge_Object=MibTableColumn
agentSwitchArpAge=_AgentSwitchArpAge_Object((1,3,6,1,4,1,4526,11,2,1,10,1,1),_AgentSwitchArpAge_Type())
agentSwitchArpAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpAge.setStatus(_E)
_AgentSwitchArpIpAddress_Type=IpAddress
_AgentSwitchArpIpAddress_Object=MibTableColumn
agentSwitchArpIpAddress=_AgentSwitchArpIpAddress_Object((1,3,6,1,4,1,4526,11,2,1,10,1,2),_AgentSwitchArpIpAddress_Type())
agentSwitchArpIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpIpAddress.setStatus(_E)
_AgentSwitchArpMacAddress_Type=PhysAddress
_AgentSwitchArpMacAddress_Object=MibTableColumn
agentSwitchArpMacAddress=_AgentSwitchArpMacAddress_Object((1,3,6,1,4,1,4526,11,2,1,10,1,3),_AgentSwitchArpMacAddress_Type())
agentSwitchArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchArpMacAddress.setStatus(_E)
_AgentSwitchArpInterface_Type=Integer32
_AgentSwitchArpInterface_Object=MibTableColumn
agentSwitchArpInterface=_AgentSwitchArpInterface_Object((1,3,6,1,4,1,4526,11,2,1,10,1,4),_AgentSwitchArpInterface_Type())
agentSwitchArpInterface.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchArpInterface.setStatus(_E)
class _AgentSwitchArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_O,2),(_P,3),(_Q,4)))
_AgentSwitchArpType_Type.__name__=_D
_AgentSwitchArpType_Object=MibTableColumn
agentSwitchArpType=_AgentSwitchArpType_Object((1,3,6,1,4,1,4526,11,2,1,10,1,5),_AgentSwitchArpType_Type())
agentSwitchArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchArpType.setStatus(_E)
_AgentSwitchArpStatus_Type=RowStatus
_AgentSwitchArpStatus_Object=MibTableColumn
agentSwitchArpStatus=_AgentSwitchArpStatus_Object((1,3,6,1,4,1,4526,11,2,1,10,1,6),_AgentSwitchArpStatus_Type())
agentSwitchArpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchArpStatus.setStatus(_E)
_AgentSwitchIntfArpTable_Object=MibTable
agentSwitchIntfArpTable=_AgentSwitchIntfArpTable_Object((1,3,6,1,4,1,4526,11,2,1,12))
if mibBuilder.loadTexts:agentSwitchIntfArpTable.setStatus(_A)
_AgentSwitchIntfArpEntry_Object=MibTableRow
agentSwitchIntfArpEntry=_AgentSwitchIntfArpEntry_Object((1,3,6,1,4,1,4526,11,2,1,12,1))
agentSwitchIntfArpEntry.setIndexNames((0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:agentSwitchIntfArpEntry.setStatus(_A)
_AgentSwitchIntfArpIpAddress_Type=IpAddress
_AgentSwitchIntfArpIpAddress_Object=MibTableColumn
agentSwitchIntfArpIpAddress=_AgentSwitchIntfArpIpAddress_Object((1,3,6,1,4,1,4526,11,2,1,12,1,1),_AgentSwitchIntfArpIpAddress_Type())
agentSwitchIntfArpIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchIntfArpIpAddress.setStatus(_A)
_AgentSwitchIntfArpIfIndex_Type=InterfaceIndex
_AgentSwitchIntfArpIfIndex_Object=MibTableColumn
agentSwitchIntfArpIfIndex=_AgentSwitchIntfArpIfIndex_Object((1,3,6,1,4,1,4526,11,2,1,12,1,2),_AgentSwitchIntfArpIfIndex_Type())
agentSwitchIntfArpIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchIntfArpIfIndex.setStatus(_A)
_AgentSwitchIntfArpAge_Type=TimeTicks
_AgentSwitchIntfArpAge_Object=MibTableColumn
agentSwitchIntfArpAge=_AgentSwitchIntfArpAge_Object((1,3,6,1,4,1,4526,11,2,1,12,1,3),_AgentSwitchIntfArpAge_Type())
agentSwitchIntfArpAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfArpAge.setStatus(_A)
_AgentSwitchIntfArpMacAddress_Type=PhysAddress
_AgentSwitchIntfArpMacAddress_Object=MibTableColumn
agentSwitchIntfArpMacAddress=_AgentSwitchIntfArpMacAddress_Object((1,3,6,1,4,1,4526,11,2,1,12,1,4),_AgentSwitchIntfArpMacAddress_Type())
agentSwitchIntfArpMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfArpMacAddress.setStatus(_A)
class _AgentSwitchIntfArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_O,2),(_P,3),(_Q,4)))
_AgentSwitchIntfArpType_Type.__name__=_D
_AgentSwitchIntfArpType_Object=MibTableColumn
agentSwitchIntfArpType=_AgentSwitchIntfArpType_Object((1,3,6,1,4,1,4526,11,2,1,12,1,5),_AgentSwitchIntfArpType_Type())
agentSwitchIntfArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfArpType.setStatus(_A)
_AgentSwitchIntfArpStatus_Type=RowStatus
_AgentSwitchIntfArpStatus_Object=MibTableColumn
agentSwitchIntfArpStatus=_AgentSwitchIntfArpStatus_Object((1,3,6,1,4,1,4526,11,2,1,12,1,6),_AgentSwitchIntfArpStatus_Type())
agentSwitchIntfArpStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfArpStatus.setStatus(_A)
_AgentSwitchIpGroup_ObjectIdentity=ObjectIdentity
agentSwitchIpGroup=_AgentSwitchIpGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,2))
class _AgentSwitchIpRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpRoutingMode_Type.__name__=_D
_AgentSwitchIpRoutingMode_Object=MibScalar
agentSwitchIpRoutingMode=_AgentSwitchIpRoutingMode_Object((1,3,6,1,4,1,4526,11,2,2,1),_AgentSwitchIpRoutingMode_Type())
agentSwitchIpRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRoutingMode.setStatus(_A)
_AgentSwitchIpDefaultGateway_Type=IpAddress
_AgentSwitchIpDefaultGateway_Object=MibScalar
agentSwitchIpDefaultGateway=_AgentSwitchIpDefaultGateway_Object((1,3,6,1,4,1,4526,11,2,2,2),_AgentSwitchIpDefaultGateway_Type())
agentSwitchIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpDefaultGateway.setStatus(_A)
_AgentSwitchIpInterfaceTable_Object=MibTable
agentSwitchIpInterfaceTable=_AgentSwitchIpInterfaceTable_Object((1,3,6,1,4,1,4526,11,2,2,3))
if mibBuilder.loadTexts:agentSwitchIpInterfaceTable.setStatus(_A)
_AgentSwitchIpInterfaceEntry_Object=MibTableRow
agentSwitchIpInterfaceEntry=_AgentSwitchIpInterfaceEntry_Object((1,3,6,1,4,1,4526,11,2,2,3,1))
agentSwitchIpInterfaceEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:agentSwitchIpInterfaceEntry.setStatus(_A)
class _AgentSwitchIpInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpInterfaceIfIndex_Type.__name__=_D
_AgentSwitchIpInterfaceIfIndex_Object=MibTableColumn
agentSwitchIpInterfaceIfIndex=_AgentSwitchIpInterfaceIfIndex_Object((1,3,6,1,4,1,4526,11,2,2,3,1,1),_AgentSwitchIpInterfaceIfIndex_Type())
agentSwitchIpInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIfIndex.setStatus(_A)
class _AgentSwitchIPAddressConfigMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('manual',1),('dhcp',2)))
_AgentSwitchIPAddressConfigMethod_Type.__name__=_D
_AgentSwitchIPAddressConfigMethod_Object=MibTableColumn
agentSwitchIPAddressConfigMethod=_AgentSwitchIPAddressConfigMethod_Object((1,3,6,1,4,1,4526,11,2,2,3,1,2),_AgentSwitchIPAddressConfigMethod_Type())
agentSwitchIPAddressConfigMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIPAddressConfigMethod.setStatus(_A)
_AgentSwitchIpInterfaceIpAddress_Type=IpAddress
_AgentSwitchIpInterfaceIpAddress_Object=MibTableColumn
agentSwitchIpInterfaceIpAddress=_AgentSwitchIpInterfaceIpAddress_Object((1,3,6,1,4,1,4526,11,2,2,3,1,3),_AgentSwitchIpInterfaceIpAddress_Type())
agentSwitchIpInterfaceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIpAddress.setStatus(_A)
_AgentSwitchIpInterfaceNetMask_Type=IpAddress
_AgentSwitchIpInterfaceNetMask_Object=MibTableColumn
agentSwitchIpInterfaceNetMask=_AgentSwitchIpInterfaceNetMask_Object((1,3,6,1,4,1,4526,11,2,2,3,1,4),_AgentSwitchIpInterfaceNetMask_Type())
agentSwitchIpInterfaceNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceNetMask.setStatus(_A)
class _AgentSwitchIpInterfaceClearIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceClearIp_Type.__name__=_D
_AgentSwitchIpInterfaceClearIp_Object=MibTableColumn
agentSwitchIpInterfaceClearIp=_AgentSwitchIpInterfaceClearIp_Object((1,3,6,1,4,1,4526,11,2,2,3,1,5),_AgentSwitchIpInterfaceClearIp_Type())
agentSwitchIpInterfaceClearIp.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceClearIp.setStatus(_A)
class _AgentSwitchIpInterfaceRoutingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceRoutingMode_Type.__name__=_D
_AgentSwitchIpInterfaceRoutingMode_Object=MibTableColumn
agentSwitchIpInterfaceRoutingMode=_AgentSwitchIpInterfaceRoutingMode_Object((1,3,6,1,4,1,4526,11,2,2,3,1,6),_AgentSwitchIpInterfaceRoutingMode_Type())
agentSwitchIpInterfaceRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceRoutingMode.setStatus(_A)
class _AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(68,9198))
_AgentSwitchIpInterfaceMtuValue_Type.__name__=_J
_AgentSwitchIpInterfaceMtuValue_Object=MibTableColumn
agentSwitchIpInterfaceMtuValue=_AgentSwitchIpInterfaceMtuValue_Object((1,3,6,1,4,1,4526,11,2,2,3,1,8),_AgentSwitchIpInterfaceMtuValue_Type())
agentSwitchIpInterfaceMtuValue.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceMtuValue.setStatus(_A)
class _AgentSwitchIpInterfaceBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,10000000))
_AgentSwitchIpInterfaceBandwidth_Type.__name__=_J
_AgentSwitchIpInterfaceBandwidth_Object=MibTableColumn
agentSwitchIpInterfaceBandwidth=_AgentSwitchIpInterfaceBandwidth_Object((1,3,6,1,4,1,4526,11,2,2,3,1,9),_AgentSwitchIpInterfaceBandwidth_Type())
agentSwitchIpInterfaceBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceBandwidth.setStatus(_A)
_AgentSwitchIpInterfaceUnnumberedIfIndex_Type=InterfaceIndexOrZero
_AgentSwitchIpInterfaceUnnumberedIfIndex_Object=MibTableColumn
agentSwitchIpInterfaceUnnumberedIfIndex=_AgentSwitchIpInterfaceUnnumberedIfIndex_Object((1,3,6,1,4,1,4526,11,2,2,3,1,10),_AgentSwitchIpInterfaceUnnumberedIfIndex_Type())
agentSwitchIpInterfaceUnnumberedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceUnnumberedIfIndex.setStatus(_A)
class _AgentSwitchIpInterfaceIcmpUnreachables_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceIcmpUnreachables_Type.__name__=_D
_AgentSwitchIpInterfaceIcmpUnreachables_Object=MibTableColumn
agentSwitchIpInterfaceIcmpUnreachables=_AgentSwitchIpInterfaceIcmpUnreachables_Object((1,3,6,1,4,1,4526,11,2,2,3,1,11),_AgentSwitchIpInterfaceIcmpUnreachables_Type())
agentSwitchIpInterfaceIcmpUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIcmpUnreachables.setStatus(_A)
class _AgentSwitchIpInterfaceIcmpRedirects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpInterfaceIcmpRedirects_Type.__name__=_D
_AgentSwitchIpInterfaceIcmpRedirects_Object=MibTableColumn
agentSwitchIpInterfaceIcmpRedirects=_AgentSwitchIpInterfaceIcmpRedirects_Object((1,3,6,1,4,1,4526,11,2,2,3,1,12),_AgentSwitchIpInterfaceIcmpRedirects_Type())
agentSwitchIpInterfaceIcmpRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpInterfaceIcmpRedirects.setStatus(_A)
class _AgentSwitchDhcpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('renew',1),('release',2),('none',3)))
_AgentSwitchDhcpOperation_Type.__name__=_D
_AgentSwitchDhcpOperation_Object=MibTableColumn
agentSwitchDhcpOperation=_AgentSwitchDhcpOperation_Object((1,3,6,1,4,1,4526,11,2,2,3,1,13),_AgentSwitchDhcpOperation_Type())
agentSwitchDhcpOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchDhcpOperation.setStatus(_A)
class _AgentSwitchIpInterfaceSuppressed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsuppressed',0),('suppressed',1)))
_AgentSwitchIpInterfaceSuppressed_Type.__name__=_D
_AgentSwitchIpInterfaceSuppressed_Object=MibTableColumn
agentSwitchIpInterfaceSuppressed=_AgentSwitchIpInterfaceSuppressed_Object((1,3,6,1,4,1,4526,11,2,2,3,1,14),_AgentSwitchIpInterfaceSuppressed_Type())
agentSwitchIpInterfaceSuppressed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceSuppressed.setStatus(_A)
class _AgentSwitchIpInterfaceNumberOfFlaps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AgentSwitchIpInterfaceNumberOfFlaps_Type.__name__=_J
_AgentSwitchIpInterfaceNumberOfFlaps_Object=MibTableColumn
agentSwitchIpInterfaceNumberOfFlaps=_AgentSwitchIpInterfaceNumberOfFlaps_Object((1,3,6,1,4,1,4526,11,2,2,3,1,15),_AgentSwitchIpInterfaceNumberOfFlaps_Type())
agentSwitchIpInterfaceNumberOfFlaps.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceNumberOfFlaps.setStatus(_A)
class _AgentSwitchIpInterfaceCurrentPenalty_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AgentSwitchIpInterfaceCurrentPenalty_Type.__name__=_J
_AgentSwitchIpInterfaceCurrentPenalty_Object=MibTableColumn
agentSwitchIpInterfaceCurrentPenalty=_AgentSwitchIpInterfaceCurrentPenalty_Object((1,3,6,1,4,1,4526,11,2,2,3,1,16),_AgentSwitchIpInterfaceCurrentPenalty_Type())
agentSwitchIpInterfaceCurrentPenalty.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceCurrentPenalty.setStatus(_A)
class _AgentSwitchIpInterfaceReUseTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentSwitchIpInterfaceReUseTime_Type.__name__=_J
_AgentSwitchIpInterfaceReUseTime_Object=MibTableColumn
agentSwitchIpInterfaceReUseTime=_AgentSwitchIpInterfaceReUseTime_Object((1,3,6,1,4,1,4526,11,2,2,3,1,17),_AgentSwitchIpInterfaceReUseTime_Type())
agentSwitchIpInterfaceReUseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpInterfaceReUseTime.setStatus(_A)
_AgentSwitchIpRouterDiscoveryTable_Object=MibTable
agentSwitchIpRouterDiscoveryTable=_AgentSwitchIpRouterDiscoveryTable_Object((1,3,6,1,4,1,4526,11,2,2,4))
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryTable.setStatus(_A)
_AgentSwitchIpRouterDiscoveryEntry_Object=MibTableRow
agentSwitchIpRouterDiscoveryEntry=_AgentSwitchIpRouterDiscoveryEntry_Object((1,3,6,1,4,1,4526,11,2,2,4,1))
agentSwitchIpRouterDiscoveryEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryEntry.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpRouterDiscoveryIfIndex_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryIfIndex_Object=MibTableColumn
agentSwitchIpRouterDiscoveryIfIndex=_AgentSwitchIpRouterDiscoveryIfIndex_Object((1,3,6,1,4,1,4526,11,2,2,4,1,1),_AgentSwitchIpRouterDiscoveryIfIndex_Type())
agentSwitchIpRouterDiscoveryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryIfIndex.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertiseMode=_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object((1,3,6,1,4,1,4526,11,2,2,4,1,2),_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type())
agentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertiseMode.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1800))
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object=MibTableColumn
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval=_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object((1,3,6,1,4,1,4526,11,2,2,4,1,3),_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type())
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,1800))
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object=MibTableColumn
agentSwitchIpRouterDiscoveryMinAdvertisementInterval=_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object((1,3,6,1,4,1,4526,11,2,2,4,1,4),_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type())
agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,9000))
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementLifetime=_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object((1,3,6,1,4,1,4526,11,2,2,4,1,5),_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type())
agentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):defaultValue=0
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__=_D
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object=MibTableColumn
agentSwitchIpRouterDiscoveryPreferenceLevel=_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object((1,3,6,1,4,1,4526,11,2,2,4,1,6),_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type())
agentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryPreferenceLevel.setStatus(_A)
class _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):defaultHexValue='E0000001'
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__=_M
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object=MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementAddress=_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object((1,3,6,1,4,1,4526,11,2,2,4,1,7),_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type())
agentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus(_A)
_AgentSwitchIpVlanTable_Object=MibTable
agentSwitchIpVlanTable=_AgentSwitchIpVlanTable_Object((1,3,6,1,4,1,4526,11,2,2,5))
if mibBuilder.loadTexts:agentSwitchIpVlanTable.setStatus(_A)
_AgentSwitchIpVlanEntry_Object=MibTableRow
agentSwitchIpVlanEntry=_AgentSwitchIpVlanEntry_Object((1,3,6,1,4,1,4526,11,2,2,5,1))
agentSwitchIpVlanEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:agentSwitchIpVlanEntry.setStatus(_A)
class _AgentSwitchIpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpVlanId_Type.__name__=_D
_AgentSwitchIpVlanId_Object=MibTableColumn
agentSwitchIpVlanId=_AgentSwitchIpVlanId_Object((1,3,6,1,4,1,4526,11,2,2,5,1,1),_AgentSwitchIpVlanId_Type())
agentSwitchIpVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpVlanId.setStatus(_A)
_AgentSwitchIpVlanIfIndex_Type=Integer32
_AgentSwitchIpVlanIfIndex_Object=MibTableColumn
agentSwitchIpVlanIfIndex=_AgentSwitchIpVlanIfIndex_Object((1,3,6,1,4,1,4526,11,2,2,5,1,2),_AgentSwitchIpVlanIfIndex_Type())
agentSwitchIpVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpVlanIfIndex.setStatus(_A)
_AgentSwitchIpVlanRoutingStatus_Type=RowStatus
_AgentSwitchIpVlanRoutingStatus_Object=MibTableColumn
agentSwitchIpVlanRoutingStatus=_AgentSwitchIpVlanRoutingStatus_Object((1,3,6,1,4,1,4526,11,2,2,5,1,3),_AgentSwitchIpVlanRoutingStatus_Type())
agentSwitchIpVlanRoutingStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIpVlanRoutingStatus.setStatus(_A)
_AgentSwitchSecondaryAddressTable_Object=MibTable
agentSwitchSecondaryAddressTable=_AgentSwitchSecondaryAddressTable_Object((1,3,6,1,4,1,4526,11,2,2,6))
if mibBuilder.loadTexts:agentSwitchSecondaryAddressTable.setStatus(_A)
_AgentSwitchSecondaryAddressEntry_Object=MibTableRow
agentSwitchSecondaryAddressEntry=_AgentSwitchSecondaryAddressEntry_Object((1,3,6,1,4,1,4526,11,2,2,6,1))
agentSwitchSecondaryAddressEntry.setIndexNames((0,_F,_L),(0,_F,_V))
if mibBuilder.loadTexts:agentSwitchSecondaryAddressEntry.setStatus(_A)
_AgentSwitchSecondaryIpAddress_Type=IpAddress
_AgentSwitchSecondaryIpAddress_Object=MibTableColumn
agentSwitchSecondaryIpAddress=_AgentSwitchSecondaryIpAddress_Object((1,3,6,1,4,1,4526,11,2,2,6,1,1),_AgentSwitchSecondaryIpAddress_Type())
agentSwitchSecondaryIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchSecondaryIpAddress.setStatus(_A)
_AgentSwitchSecondaryNetMask_Type=IpAddress
_AgentSwitchSecondaryNetMask_Object=MibTableColumn
agentSwitchSecondaryNetMask=_AgentSwitchSecondaryNetMask_Object((1,3,6,1,4,1,4526,11,2,2,6,1,2),_AgentSwitchSecondaryNetMask_Type())
agentSwitchSecondaryNetMask.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchSecondaryNetMask.setStatus(_A)
_AgentSwitchSecondaryStatus_Type=RowStatus
_AgentSwitchSecondaryStatus_Object=MibTableColumn
agentSwitchSecondaryStatus=_AgentSwitchSecondaryStatus_Object((1,3,6,1,4,1,4526,11,2,2,6,1,3),_AgentSwitchSecondaryStatus_Type())
agentSwitchSecondaryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchSecondaryStatus.setStatus(_A)
_AgentSwitchHelperAddressTable_Object=MibTable
agentSwitchHelperAddressTable=_AgentSwitchHelperAddressTable_Object((1,3,6,1,4,1,4526,11,2,2,7))
if mibBuilder.loadTexts:agentSwitchHelperAddressTable.setStatus(_E)
_AgentSwitchHelperAddressEntry_Object=MibTableRow
agentSwitchHelperAddressEntry=_AgentSwitchHelperAddressEntry_Object((1,3,6,1,4,1,4526,11,2,2,7,1))
agentSwitchHelperAddressEntry.setIndexNames((0,_F,_L),(0,_F,_W))
if mibBuilder.loadTexts:agentSwitchHelperAddressEntry.setStatus(_E)
_AgentSwitchHelperIpAddress_Type=IpAddress
_AgentSwitchHelperIpAddress_Object=MibTableColumn
agentSwitchHelperIpAddress=_AgentSwitchHelperIpAddress_Object((1,3,6,1,4,1,4526,11,2,2,7,1,1),_AgentSwitchHelperIpAddress_Type())
agentSwitchHelperIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchHelperIpAddress.setStatus(_E)
_AgentSwitchHelperStatus_Type=RowStatus
_AgentSwitchHelperStatus_Object=MibTableColumn
agentSwitchHelperStatus=_AgentSwitchHelperStatus_Object((1,3,6,1,4,1,4526,11,2,2,7,1,2),_AgentSwitchHelperStatus_Type())
agentSwitchHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchHelperStatus.setStatus(_E)
_AgentSwitchIpIcmpControlGroup_ObjectIdentity=ObjectIdentity
agentSwitchIpIcmpControlGroup=_AgentSwitchIpIcmpControlGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,2,8))
class _AgentSwitchIpIcmpEchoReplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpIcmpEchoReplyMode_Type.__name__=_D
_AgentSwitchIpIcmpEchoReplyMode_Object=MibScalar
agentSwitchIpIcmpEchoReplyMode=_AgentSwitchIpIcmpEchoReplyMode_Object((1,3,6,1,4,1,4526,11,2,2,8,1),_AgentSwitchIpIcmpEchoReplyMode_Type())
agentSwitchIpIcmpEchoReplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpEchoReplyMode.setStatus(_A)
class _AgentSwitchIpIcmpRedirectsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchIpIcmpRedirectsMode_Type.__name__=_D
_AgentSwitchIpIcmpRedirectsMode_Object=MibScalar
agentSwitchIpIcmpRedirectsMode=_AgentSwitchIpIcmpRedirectsMode_Object((1,3,6,1,4,1,4526,11,2,2,8,2),_AgentSwitchIpIcmpRedirectsMode_Type())
agentSwitchIpIcmpRedirectsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpRedirectsMode.setStatus(_A)
class _AgentSwitchIpIcmpRateLimitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchIpIcmpRateLimitInterval_Type.__name__=_D
_AgentSwitchIpIcmpRateLimitInterval_Object=MibScalar
agentSwitchIpIcmpRateLimitInterval=_AgentSwitchIpIcmpRateLimitInterval_Object((1,3,6,1,4,1,4526,11,2,2,8,3),_AgentSwitchIpIcmpRateLimitInterval_Type())
agentSwitchIpIcmpRateLimitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpRateLimitInterval.setStatus(_A)
class _AgentSwitchIpIcmpRateLimitBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AgentSwitchIpIcmpRateLimitBurstSize_Type.__name__=_D
_AgentSwitchIpIcmpRateLimitBurstSize_Object=MibScalar
agentSwitchIpIcmpRateLimitBurstSize=_AgentSwitchIpIcmpRateLimitBurstSize_Object((1,3,6,1,4,1,4526,11,2,2,8,4),_AgentSwitchIpIcmpRateLimitBurstSize_Type())
agentSwitchIpIcmpRateLimitBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpIcmpRateLimitBurstSize.setStatus(_A)
_AgentSwitchIntfIpHelperAddressTable_Object=MibTable
agentSwitchIntfIpHelperAddressTable=_AgentSwitchIntfIpHelperAddressTable_Object((1,3,6,1,4,1,4526,11,2,2,10))
if mibBuilder.loadTexts:agentSwitchIntfIpHelperAddressTable.setStatus(_A)
_AgentSwitchIntfIpHelperAddressEntry_Object=MibTableRow
agentSwitchIntfIpHelperAddressEntry=_AgentSwitchIntfIpHelperAddressEntry_Object((1,3,6,1,4,1,4526,11,2,2,10,1))
agentSwitchIntfIpHelperAddressEntry.setIndexNames((0,_F,_L),(0,_F,_X),(0,_F,_Y))
if mibBuilder.loadTexts:agentSwitchIntfIpHelperAddressEntry.setStatus(_A)
_AgentSwitchIntfIpHelperIpAddress_Type=IpAddress
_AgentSwitchIntfIpHelperIpAddress_Object=MibTableColumn
agentSwitchIntfIpHelperIpAddress=_AgentSwitchIntfIpHelperIpAddress_Object((1,3,6,1,4,1,4526,11,2,2,10,1,1),_AgentSwitchIntfIpHelperIpAddress_Type())
agentSwitchIntfIpHelperIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperIpAddress.setStatus(_A)
class _AgentSwitchIntfIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchIntfIpHelperUdpPort_Type.__name__=_J
_AgentSwitchIntfIpHelperUdpPort_Object=MibTableColumn
agentSwitchIntfIpHelperUdpPort=_AgentSwitchIntfIpHelperUdpPort_Object((1,3,6,1,4,1,4526,11,2,2,10,1,2),_AgentSwitchIntfIpHelperUdpPort_Type())
agentSwitchIntfIpHelperUdpPort.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperUdpPort.setStatus(_A)
_AgentSwitchIntfIpHelperDiscard_Type=TruthValue
_AgentSwitchIntfIpHelperDiscard_Object=MibTableColumn
agentSwitchIntfIpHelperDiscard=_AgentSwitchIntfIpHelperDiscard_Object((1,3,6,1,4,1,4526,11,2,2,10,1,3),_AgentSwitchIntfIpHelperDiscard_Type())
agentSwitchIntfIpHelperDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperDiscard.setStatus(_E)
_AgentSwitchIntfIpHelperHitCount_Type=Unsigned32
_AgentSwitchIntfIpHelperHitCount_Object=MibTableColumn
agentSwitchIntfIpHelperHitCount=_AgentSwitchIntfIpHelperHitCount_Object((1,3,6,1,4,1,4526,11,2,2,10,1,4),_AgentSwitchIntfIpHelperHitCount_Type())
agentSwitchIntfIpHelperHitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperHitCount.setStatus(_A)
_AgentSwitchIntfIpHelperStatus_Type=RowStatus
_AgentSwitchIntfIpHelperStatus_Object=MibTableColumn
agentSwitchIntfIpHelperStatus=_AgentSwitchIntfIpHelperStatus_Object((1,3,6,1,4,1,4526,11,2,2,10,1,5),_AgentSwitchIntfIpHelperStatus_Type())
agentSwitchIntfIpHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIntfIpHelperStatus.setStatus(_A)
class _AgentSwitchClearIpDefaultGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentSwitchClearIpDefaultGateway_Type.__name__=_D
_AgentSwitchClearIpDefaultGateway_Object=MibScalar
agentSwitchClearIpDefaultGateway=_AgentSwitchClearIpDefaultGateway_Object((1,3,6,1,4,1,4526,11,2,2,11),_AgentSwitchClearIpDefaultGateway_Type())
agentSwitchClearIpDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchClearIpDefaultGateway.setStatus(_A)
_AgentBootpDhcpRelayGroup_ObjectIdentity=ObjectIdentity
agentBootpDhcpRelayGroup=_AgentBootpDhcpRelayGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,6))
class _AgentBootpDhcpRelayMaxHopCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AgentBootpDhcpRelayMaxHopCount_Type.__name__=_D
_AgentBootpDhcpRelayMaxHopCount_Object=MibScalar
agentBootpDhcpRelayMaxHopCount=_AgentBootpDhcpRelayMaxHopCount_Object((1,3,6,1,4,1,4526,11,2,6,1),_AgentBootpDhcpRelayMaxHopCount_Type())
agentBootpDhcpRelayMaxHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayMaxHopCount.setStatus(_A)
_AgentBootpDhcpRelayForwardingIp_Type=IpAddress
_AgentBootpDhcpRelayForwardingIp_Object=MibScalar
agentBootpDhcpRelayForwardingIp=_AgentBootpDhcpRelayForwardingIp_Object((1,3,6,1,4,1,4526,11,2,6,2),_AgentBootpDhcpRelayForwardingIp_Type())
agentBootpDhcpRelayForwardingIp.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayForwardingIp.setStatus(_E)
class _AgentBootpDhcpRelayForwardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentBootpDhcpRelayForwardMode_Type.__name__=_D
_AgentBootpDhcpRelayForwardMode_Object=MibScalar
agentBootpDhcpRelayForwardMode=_AgentBootpDhcpRelayForwardMode_Object((1,3,6,1,4,1,4526,11,2,6,3),_AgentBootpDhcpRelayForwardMode_Type())
agentBootpDhcpRelayForwardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayForwardMode.setStatus(_E)
class _AgentBootpDhcpRelayMinWaitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentBootpDhcpRelayMinWaitTime_Type.__name__=_D
_AgentBootpDhcpRelayMinWaitTime_Object=MibScalar
agentBootpDhcpRelayMinWaitTime=_AgentBootpDhcpRelayMinWaitTime_Object((1,3,6,1,4,1,4526,11,2,6,4),_AgentBootpDhcpRelayMinWaitTime_Type())
agentBootpDhcpRelayMinWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayMinWaitTime.setStatus(_A)
class _AgentBootpDhcpRelayCircuitIdOptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentBootpDhcpRelayCircuitIdOptionMode_Type.__name__=_D
_AgentBootpDhcpRelayCircuitIdOptionMode_Object=MibScalar
agentBootpDhcpRelayCircuitIdOptionMode=_AgentBootpDhcpRelayCircuitIdOptionMode_Object((1,3,6,1,4,1,4526,11,2,6,5),_AgentBootpDhcpRelayCircuitIdOptionMode_Type())
agentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBootpDhcpRelayCircuitIdOptionMode.setStatus(_A)
_AgentBootpDhcpRelayNumOfRequestsReceived_Type=Integer32
_AgentBootpDhcpRelayNumOfRequestsReceived_Object=MibScalar
agentBootpDhcpRelayNumOfRequestsReceived=_AgentBootpDhcpRelayNumOfRequestsReceived_Object((1,3,6,1,4,1,4526,11,2,6,6),_AgentBootpDhcpRelayNumOfRequestsReceived_Type())
agentBootpDhcpRelayNumOfRequestsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfRequestsReceived.setStatus(_E)
_AgentBootpDhcpRelayNumOfRequestsForwarded_Type=Integer32
_AgentBootpDhcpRelayNumOfRequestsForwarded_Object=MibScalar
agentBootpDhcpRelayNumOfRequestsForwarded=_AgentBootpDhcpRelayNumOfRequestsForwarded_Object((1,3,6,1,4,1,4526,11,2,6,7),_AgentBootpDhcpRelayNumOfRequestsForwarded_Type())
agentBootpDhcpRelayNumOfRequestsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfRequestsForwarded.setStatus(_E)
_AgentBootpDhcpRelayNumOfDiscards_Type=Integer32
_AgentBootpDhcpRelayNumOfDiscards_Object=MibScalar
agentBootpDhcpRelayNumOfDiscards=_AgentBootpDhcpRelayNumOfDiscards_Object((1,3,6,1,4,1,4526,11,2,6,8),_AgentBootpDhcpRelayNumOfDiscards_Type())
agentBootpDhcpRelayNumOfDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBootpDhcpRelayNumOfDiscards.setStatus(_E)
_AgentIpHelperGroup_ObjectIdentity=ObjectIdentity
agentIpHelperGroup=_AgentIpHelperGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,11))
class _AgentIpHelperAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentIpHelperAdminMode_Type.__name__=_D
_AgentIpHelperAdminMode_Object=MibScalar
agentIpHelperAdminMode=_AgentIpHelperAdminMode_Object((1,3,6,1,4,1,4526,11,2,11,1),_AgentIpHelperAdminMode_Type())
agentIpHelperAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpHelperAdminMode.setStatus(_A)
_AgentDhcpClientMsgsReceived_Type=Counter32
_AgentDhcpClientMsgsReceived_Object=MibScalar
agentDhcpClientMsgsReceived=_AgentDhcpClientMsgsReceived_Object((1,3,6,1,4,1,4526,11,2,11,2),_AgentDhcpClientMsgsReceived_Type())
agentDhcpClientMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpClientMsgsReceived.setStatus(_A)
_AgentDhcpClientMsgsRelayed_Type=Counter32
_AgentDhcpClientMsgsRelayed_Object=MibScalar
agentDhcpClientMsgsRelayed=_AgentDhcpClientMsgsRelayed_Object((1,3,6,1,4,1,4526,11,2,11,3),_AgentDhcpClientMsgsRelayed_Type())
agentDhcpClientMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpClientMsgsRelayed.setStatus(_A)
_AgentDhcpServerMsgsReceived_Type=Counter32
_AgentDhcpServerMsgsReceived_Object=MibScalar
agentDhcpServerMsgsReceived=_AgentDhcpServerMsgsReceived_Object((1,3,6,1,4,1,4526,11,2,11,4),_AgentDhcpServerMsgsReceived_Type())
agentDhcpServerMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerMsgsReceived.setStatus(_A)
_AgentDhcpServerMsgsRelayed_Type=Counter32
_AgentDhcpServerMsgsRelayed_Object=MibScalar
agentDhcpServerMsgsRelayed=_AgentDhcpServerMsgsRelayed_Object((1,3,6,1,4,1,4526,11,2,11,5),_AgentDhcpServerMsgsRelayed_Type())
agentDhcpServerMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerMsgsRelayed.setStatus(_A)
_AgentUdpClientMsgsReceived_Type=Counter32
_AgentUdpClientMsgsReceived_Object=MibScalar
agentUdpClientMsgsReceived=_AgentUdpClientMsgsReceived_Object((1,3,6,1,4,1,4526,11,2,11,6),_AgentUdpClientMsgsReceived_Type())
agentUdpClientMsgsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsReceived.setStatus(_A)
_AgentUdpClientMsgsRelayed_Type=Counter32
_AgentUdpClientMsgsRelayed_Object=MibScalar
agentUdpClientMsgsRelayed=_AgentUdpClientMsgsRelayed_Object((1,3,6,1,4,1,4526,11,2,11,7),_AgentUdpClientMsgsRelayed_Type())
agentUdpClientMsgsRelayed.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsRelayed.setStatus(_A)
_AgentSwitchIpHelperAddressTable_Object=MibTable
agentSwitchIpHelperAddressTable=_AgentSwitchIpHelperAddressTable_Object((1,3,6,1,4,1,4526,11,2,11,8))
if mibBuilder.loadTexts:agentSwitchIpHelperAddressTable.setStatus(_A)
_AgentSwitchIpHelperAddressEntry_Object=MibTableRow
agentSwitchIpHelperAddressEntry=_AgentSwitchIpHelperAddressEntry_Object((1,3,6,1,4,1,4526,11,2,11,8,1))
agentSwitchIpHelperAddressEntry.setIndexNames((0,_F,_Z),(0,_F,_a))
if mibBuilder.loadTexts:agentSwitchIpHelperAddressEntry.setStatus(_A)
_AgentSwitchIpHelperAddress_Type=IpAddress
_AgentSwitchIpHelperAddress_Object=MibTableColumn
agentSwitchIpHelperAddress=_AgentSwitchIpHelperAddress_Object((1,3,6,1,4,1,4526,11,2,11,8,1,1),_AgentSwitchIpHelperAddress_Type())
agentSwitchIpHelperAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpHelperAddress.setStatus(_A)
class _AgentSwitchIpHelperUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentSwitchIpHelperUdpPort_Type.__name__=_J
_AgentSwitchIpHelperUdpPort_Object=MibTableColumn
agentSwitchIpHelperUdpPort=_AgentSwitchIpHelperUdpPort_Object((1,3,6,1,4,1,4526,11,2,11,8,1,2),_AgentSwitchIpHelperUdpPort_Type())
agentSwitchIpHelperUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSwitchIpHelperUdpPort.setStatus(_A)
_AgentSwitchIpHelperHitCount_Type=Unsigned32
_AgentSwitchIpHelperHitCount_Object=MibTableColumn
agentSwitchIpHelperHitCount=_AgentSwitchIpHelperHitCount_Object((1,3,6,1,4,1,4526,11,2,11,8,1,3),_AgentSwitchIpHelperHitCount_Type())
agentSwitchIpHelperHitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchIpHelperHitCount.setStatus(_A)
_AgentSwitchIpHelperStatus_Type=RowStatus
_AgentSwitchIpHelperStatus_Object=MibTableColumn
agentSwitchIpHelperStatus=_AgentSwitchIpHelperStatus_Object((1,3,6,1,4,1,4526,11,2,11,8,1,4),_AgentSwitchIpHelperStatus_Type())
agentSwitchIpHelperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentSwitchIpHelperStatus.setStatus(_A)
_AgentUdpClientMsgsTtlExpired_Type=Counter32
_AgentUdpClientMsgsTtlExpired_Object=MibScalar
agentUdpClientMsgsTtlExpired=_AgentUdpClientMsgsTtlExpired_Object((1,3,6,1,4,1,4526,11,2,11,9),_AgentUdpClientMsgsTtlExpired_Type())
agentUdpClientMsgsTtlExpired.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsTtlExpired.setStatus(_A)
_AgentUdpClientMsgsDiscarded_Type=Counter32
_AgentUdpClientMsgsDiscarded_Object=MibScalar
agentUdpClientMsgsDiscarded=_AgentUdpClientMsgsDiscarded_Object((1,3,6,1,4,1,4526,11,2,11,10),_AgentUdpClientMsgsDiscarded_Type())
agentUdpClientMsgsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUdpClientMsgsDiscarded.setStatus(_A)
_AgentInternalVlanGroup_ObjectIdentity=ObjectIdentity
agentInternalVlanGroup=_AgentInternalVlanGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,12))
class _AgentInternalVlanBase_Type(Integer32):defaultValue=4093
_AgentInternalVlanBase_Type.__name__=_D
_AgentInternalVlanBase_Object=MibScalar
agentInternalVlanBase=_AgentInternalVlanBase_Object((1,3,6,1,4,1,4526,11,2,12,1),_AgentInternalVlanBase_Type())
agentInternalVlanBase.setMaxAccess(_C)
if mibBuilder.loadTexts:agentInternalVlanBase.setStatus(_A)
class _AgentInternalVlanPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ascending',0),('descending',1)))
_AgentInternalVlanPolicy_Type.__name__=_D
_AgentInternalVlanPolicy_Object=MibScalar
agentInternalVlanPolicy=_AgentInternalVlanPolicy_Object((1,3,6,1,4,1,4526,11,2,12,2),_AgentInternalVlanPolicy_Type())
agentInternalVlanPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:agentInternalVlanPolicy.setStatus(_A)
_AgentSwitchInternalVlanTable_Object=MibTable
agentSwitchInternalVlanTable=_AgentSwitchInternalVlanTable_Object((1,3,6,1,4,1,4526,11,2,12,3))
if mibBuilder.loadTexts:agentSwitchInternalVlanTable.setStatus(_A)
_AgentSwitchInternalVlanEntry_Object=MibTableRow
agentSwitchInternalVlanEntry=_AgentSwitchInternalVlanEntry_Object((1,3,6,1,4,1,4526,11,2,12,3,1))
agentSwitchInternalVlanEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:agentSwitchInternalVlanEntry.setStatus(_A)
class _AgentSwitchInternalVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentSwitchInternalVlanId_Type.__name__=_D
_AgentSwitchInternalVlanId_Object=MibTableColumn
agentSwitchInternalVlanId=_AgentSwitchInternalVlanId_Object((1,3,6,1,4,1,4526,11,2,12,3,1,1),_AgentSwitchInternalVlanId_Type())
agentSwitchInternalVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:agentSwitchInternalVlanId.setStatus(_A)
_AgentSwitchInternalVlanIfIndex_Type=Integer32
_AgentSwitchInternalVlanIfIndex_Object=MibTableColumn
agentSwitchInternalVlanIfIndex=_AgentSwitchInternalVlanIfIndex_Object((1,3,6,1,4,1,4526,11,2,12,3,1,2),_AgentSwitchInternalVlanIfIndex_Type())
agentSwitchInternalVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentSwitchInternalVlanIfIndex.setStatus(_A)
_AgentRoutingHeapGroup_ObjectIdentity=ObjectIdentity
agentRoutingHeapGroup=_AgentRoutingHeapGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,16))
_AgentRoutingHeapSize_Type=Unsigned32
_AgentRoutingHeapSize_Object=MibScalar
agentRoutingHeapSize=_AgentRoutingHeapSize_Object((1,3,6,1,4,1,4526,11,2,16,1),_AgentRoutingHeapSize_Type())
agentRoutingHeapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRoutingHeapSize.setStatus(_A)
_AgentRoutingHeapInUse_Type=Gauge32
_AgentRoutingHeapInUse_Object=MibScalar
agentRoutingHeapInUse=_AgentRoutingHeapInUse_Object((1,3,6,1,4,1,4526,11,2,16,2),_AgentRoutingHeapInUse_Type())
agentRoutingHeapInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRoutingHeapInUse.setStatus(_A)
_AgentRoutingHeapHigh_Type=Gauge32
_AgentRoutingHeapHigh_Object=MibScalar
agentRoutingHeapHigh=_AgentRoutingHeapHigh_Object((1,3,6,1,4,1,4526,11,2,16,3),_AgentRoutingHeapHigh_Type())
agentRoutingHeapHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRoutingHeapHigh.setStatus(_A)
_AgentRoutingTableSummaryGroup_ObjectIdentity=ObjectIdentity
agentRoutingTableSummaryGroup=_AgentRoutingTableSummaryGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,2,17))
_AgentConnectedRoutes_Type=Gauge32
_AgentConnectedRoutes_Object=MibScalar
agentConnectedRoutes=_AgentConnectedRoutes_Object((1,3,6,1,4,1,4526,11,2,17,1),_AgentConnectedRoutes_Type())
agentConnectedRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentConnectedRoutes.setStatus(_A)
_AgentStaticRoutes_Type=Gauge32
_AgentStaticRoutes_Object=MibScalar
agentStaticRoutes=_AgentStaticRoutes_Object((1,3,6,1,4,1,4526,11,2,17,2),_AgentStaticRoutes_Type())
agentStaticRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStaticRoutes.setStatus(_A)
_AgentRipRoutes_Type=Gauge32
_AgentRipRoutes_Object=MibScalar
agentRipRoutes=_AgentRipRoutes_Object((1,3,6,1,4,1,4526,11,2,17,3),_AgentRipRoutes_Type())
agentRipRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRipRoutes.setStatus(_A)
_AgentOspfRoutes_Type=Gauge32
_AgentOspfRoutes_Object=MibScalar
agentOspfRoutes=_AgentOspfRoutes_Object((1,3,6,1,4,1,4526,11,2,17,4),_AgentOspfRoutes_Type())
agentOspfRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfRoutes.setStatus(_A)
_AgentOspfIntraRoutes_Type=Gauge32
_AgentOspfIntraRoutes_Object=MibScalar
agentOspfIntraRoutes=_AgentOspfIntraRoutes_Object((1,3,6,1,4,1,4526,11,2,17,5),_AgentOspfIntraRoutes_Type())
agentOspfIntraRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfIntraRoutes.setStatus(_A)
_AgentOspfInterRoutes_Type=Gauge32
_AgentOspfInterRoutes_Object=MibScalar
agentOspfInterRoutes=_AgentOspfInterRoutes_Object((1,3,6,1,4,1,4526,11,2,17,6),_AgentOspfInterRoutes_Type())
agentOspfInterRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfInterRoutes.setStatus(_A)
_AgentOspfExt1Routes_Type=Gauge32
_AgentOspfExt1Routes_Object=MibScalar
agentOspfExt1Routes=_AgentOspfExt1Routes_Object((1,3,6,1,4,1,4526,11,2,17,7),_AgentOspfExt1Routes_Type())
agentOspfExt1Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfExt1Routes.setStatus(_A)
_AgentOspfExt2Routes_Type=Gauge32
_AgentOspfExt2Routes_Object=MibScalar
agentOspfExt2Routes=_AgentOspfExt2Routes_Object((1,3,6,1,4,1,4526,11,2,17,8),_AgentOspfExt2Routes_Type())
agentOspfExt2Routes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentOspfExt2Routes.setStatus(_A)
_AgentBgpRoutes_Type=Gauge32
_AgentBgpRoutes_Object=MibScalar
agentBgpRoutes=_AgentBgpRoutes_Object((1,3,6,1,4,1,4526,11,2,17,9),_AgentBgpRoutes_Type())
agentBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBgpRoutes.setStatus(_A)
_AgentEbgpRoutes_Type=Gauge32
_AgentEbgpRoutes_Object=MibScalar
agentEbgpRoutes=_AgentEbgpRoutes_Object((1,3,6,1,4,1,4526,11,2,17,10),_AgentEbgpRoutes_Type())
agentEbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEbgpRoutes.setStatus(_A)
_AgentIbgpRoutes_Type=Gauge32
_AgentIbgpRoutes_Object=MibScalar
agentIbgpRoutes=_AgentIbgpRoutes_Object((1,3,6,1,4,1,4526,11,2,17,11),_AgentIbgpRoutes_Type())
agentIbgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentIbgpRoutes.setStatus(_A)
_AgentLocalBgpRoutes_Type=Gauge32
_AgentLocalBgpRoutes_Object=MibScalar
agentLocalBgpRoutes=_AgentLocalBgpRoutes_Object((1,3,6,1,4,1,4526,11,2,17,12),_AgentLocalBgpRoutes_Type())
agentLocalBgpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentLocalBgpRoutes.setStatus(_A)
_AgentRejectRoutes_Type=Gauge32
_AgentRejectRoutes_Object=MibScalar
agentRejectRoutes=_AgentRejectRoutes_Object((1,3,6,1,4,1,4526,11,2,17,13),_AgentRejectRoutes_Type())
agentRejectRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRejectRoutes.setStatus(_A)
_AgentTotalRoutes_Type=Gauge32
_AgentTotalRoutes_Object=MibScalar
agentTotalRoutes=_AgentTotalRoutes_Object((1,3,6,1,4,1,4526,11,2,17,14),_AgentTotalRoutes_Type())
agentTotalRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTotalRoutes.setStatus(_A)
_AgentBestRoutes_Type=Gauge32
_AgentBestRoutes_Object=MibScalar
agentBestRoutes=_AgentBestRoutes_Object((1,3,6,1,4,1,4526,11,2,17,15),_AgentBestRoutes_Type())
agentBestRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBestRoutes.setStatus(_A)
_AgentBestRoutesHigh_Type=Gauge32
_AgentBestRoutesHigh_Object=MibScalar
agentBestRoutesHigh=_AgentBestRoutesHigh_Object((1,3,6,1,4,1,4526,11,2,17,16),_AgentBestRoutesHigh_Type())
agentBestRoutesHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentBestRoutesHigh.setStatus(_A)
_AgentAlternateRoutes_Type=Gauge32
_AgentAlternateRoutes_Object=MibScalar
agentAlternateRoutes=_AgentAlternateRoutes_Object((1,3,6,1,4,1,4526,11,2,17,17),_AgentAlternateRoutes_Type())
agentAlternateRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAlternateRoutes.setStatus(_A)
_AgentRouteAdds_Type=Counter32
_AgentRouteAdds_Object=MibScalar
agentRouteAdds=_AgentRouteAdds_Object((1,3,6,1,4,1,4526,11,2,17,18),_AgentRouteAdds_Type())
agentRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouteAdds.setStatus(_A)
_AgentRouteModifies_Type=Counter32
_AgentRouteModifies_Object=MibScalar
agentRouteModifies=_AgentRouteModifies_Object((1,3,6,1,4,1,4526,11,2,17,19),_AgentRouteModifies_Type())
agentRouteModifies.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouteModifies.setStatus(_A)
_AgentRouteDeletes_Type=Counter32
_AgentRouteDeletes_Object=MibScalar
agentRouteDeletes=_AgentRouteDeletes_Object((1,3,6,1,4,1,4526,11,2,17,20),_AgentRouteDeletes_Type())
agentRouteDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentRouteDeletes.setStatus(_A)
_AgentUnresolvedRouteAdds_Type=Counter32
_AgentUnresolvedRouteAdds_Object=MibScalar
agentUnresolvedRouteAdds=_AgentUnresolvedRouteAdds_Object((1,3,6,1,4,1,4526,11,2,17,21),_AgentUnresolvedRouteAdds_Type())
agentUnresolvedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUnresolvedRouteAdds.setStatus(_A)
_AgentInvalidRouteAdds_Type=Counter32
_AgentInvalidRouteAdds_Object=MibScalar
agentInvalidRouteAdds=_AgentInvalidRouteAdds_Object((1,3,6,1,4,1,4526,11,2,17,22),_AgentInvalidRouteAdds_Type())
agentInvalidRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentInvalidRouteAdds.setStatus(_A)
_AgentFailedRouteAdds_Type=Counter32
_AgentFailedRouteAdds_Object=MibScalar
agentFailedRouteAdds=_AgentFailedRouteAdds_Object((1,3,6,1,4,1,4526,11,2,17,23),_AgentFailedRouteAdds_Type())
agentFailedRouteAdds.setMaxAccess(_B)
if mibBuilder.loadTexts:agentFailedRouteAdds.setStatus(_A)
_AgentReservedLocals_Type=Gauge32
_AgentReservedLocals_Object=MibScalar
agentReservedLocals=_AgentReservedLocals_Object((1,3,6,1,4,1,4526,11,2,17,24),_AgentReservedLocals_Type())
agentReservedLocals.setMaxAccess(_B)
if mibBuilder.loadTexts:agentReservedLocals.setStatus(_A)
_AgentUniqueNextHops_Type=Gauge32
_AgentUniqueNextHops_Object=MibScalar
agentUniqueNextHops=_AgentUniqueNextHops_Object((1,3,6,1,4,1,4526,11,2,17,25),_AgentUniqueNextHops_Type())
agentUniqueNextHops.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUniqueNextHops.setStatus(_A)
_AgentUniqueNextHopsHigh_Type=Gauge32
_AgentUniqueNextHopsHigh_Object=MibScalar
agentUniqueNextHopsHigh=_AgentUniqueNextHopsHigh_Object((1,3,6,1,4,1,4526,11,2,17,26),_AgentUniqueNextHopsHigh_Type())
agentUniqueNextHopsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentUniqueNextHopsHigh.setStatus(_A)
_AgentNextHopGroups_Type=Gauge32
_AgentNextHopGroups_Object=MibScalar
agentNextHopGroups=_AgentNextHopGroups_Object((1,3,6,1,4,1,4526,11,2,17,27),_AgentNextHopGroups_Type())
agentNextHopGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNextHopGroups.setStatus(_A)
_AgentNextHopGroupsHigh_Type=Gauge32
_AgentNextHopGroupsHigh_Object=MibScalar
agentNextHopGroupsHigh=_AgentNextHopGroupsHigh_Object((1,3,6,1,4,1,4526,11,2,17,28),_AgentNextHopGroupsHigh_Type())
agentNextHopGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNextHopGroupsHigh.setStatus(_A)
_AgentEcmpGroups_Type=Gauge32
_AgentEcmpGroups_Object=MibScalar
agentEcmpGroups=_AgentEcmpGroups_Object((1,3,6,1,4,1,4526,11,2,17,29),_AgentEcmpGroups_Type())
agentEcmpGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpGroups.setStatus(_A)
_AgentEcmpGroupsHigh_Type=Gauge32
_AgentEcmpGroupsHigh_Object=MibScalar
agentEcmpGroupsHigh=_AgentEcmpGroupsHigh_Object((1,3,6,1,4,1,4526,11,2,17,30),_AgentEcmpGroupsHigh_Type())
agentEcmpGroupsHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpGroupsHigh.setStatus(_A)
_AgentEcmpRoutes_Type=Gauge32
_AgentEcmpRoutes_Object=MibScalar
agentEcmpRoutes=_AgentEcmpRoutes_Object((1,3,6,1,4,1,4526,11,2,17,31),_AgentEcmpRoutes_Type())
agentEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpRoutes.setStatus(_A)
_AgentTruncEcmpRoutes_Type=Gauge32
_AgentTruncEcmpRoutes_Object=MibScalar
agentTruncEcmpRoutes=_AgentTruncEcmpRoutes_Object((1,3,6,1,4,1,4526,11,2,17,32),_AgentTruncEcmpRoutes_Type())
agentTruncEcmpRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:agentTruncEcmpRoutes.setStatus(_A)
_AgentEcmpRetries_Type=Counter32
_AgentEcmpRetries_Object=MibScalar
agentEcmpRetries=_AgentEcmpRetries_Object((1,3,6,1,4,1,4526,11,2,17,33),_AgentEcmpRetries_Type())
agentEcmpRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpRetries.setStatus(_A)
_AgentEcmpCountTable_Object=MibTable
agentEcmpCountTable=_AgentEcmpCountTable_Object((1,3,6,1,4,1,4526,11,2,18))
if mibBuilder.loadTexts:agentEcmpCountTable.setStatus(_A)
_AgentEcmpCountEntry_Object=MibTableRow
agentEcmpCountEntry=_AgentEcmpCountEntry_Object((1,3,6,1,4,1,4526,11,2,18,1))
agentEcmpCountEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:agentEcmpCountEntry.setStatus(_A)
class _AgentEcmpNextHopCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentEcmpNextHopCount_Type.__name__=_J
_AgentEcmpNextHopCount_Object=MibTableColumn
agentEcmpNextHopCount=_AgentEcmpNextHopCount_Object((1,3,6,1,4,1,4526,11,2,18,1,1),_AgentEcmpNextHopCount_Type())
agentEcmpNextHopCount.setMaxAccess(_K)
if mibBuilder.loadTexts:agentEcmpNextHopCount.setStatus(_A)
_AgentEcmpRouteCount_Type=Gauge32
_AgentEcmpRouteCount_Object=MibTableColumn
agentEcmpRouteCount=_AgentEcmpRouteCount_Object((1,3,6,1,4,1,4526,11,2,18,1,2),_AgentEcmpRouteCount_Type())
agentEcmpRouteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEcmpRouteCount.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'SpfTimerRange':SpfTimerRange,'fastPathRouting':fastPathRouting,'agentSwitchArpGroup':agentSwitchArpGroup,'agentSwitchArpAgeoutTime':agentSwitchArpAgeoutTime,'agentSwitchArpResponseTime':agentSwitchArpResponseTime,'agentSwitchArpMaxRetries':agentSwitchArpMaxRetries,'agentSwitchArpCacheSize':agentSwitchArpCacheSize,'agentSwitchArpDynamicRenew':agentSwitchArpDynamicRenew,'agentSwitchArpTotalEntryCountCurrent':agentSwitchArpTotalEntryCountCurrent,'agentSwitchArpTotalEntryCountPeak':agentSwitchArpTotalEntryCountPeak,'agentSwitchArpStaticEntryCountCurrent':agentSwitchArpStaticEntryCountCurrent,'agentSwitchArpStaticEntryCountMax':agentSwitchArpStaticEntryCountMax,'agentSwitchArpTable':agentSwitchArpTable,'agentSwitchArpEntry':agentSwitchArpEntry,'agentSwitchArpAge':agentSwitchArpAge,_N:agentSwitchArpIpAddress,'agentSwitchArpMacAddress':agentSwitchArpMacAddress,'agentSwitchArpInterface':agentSwitchArpInterface,'agentSwitchArpType':agentSwitchArpType,'agentSwitchArpStatus':agentSwitchArpStatus,'agentSwitchIntfArpTable':agentSwitchIntfArpTable,'agentSwitchIntfArpEntry':agentSwitchIntfArpEntry,_R:agentSwitchIntfArpIpAddress,_S:agentSwitchIntfArpIfIndex,'agentSwitchIntfArpAge':agentSwitchIntfArpAge,'agentSwitchIntfArpMacAddress':agentSwitchIntfArpMacAddress,'agentSwitchIntfArpType':agentSwitchIntfArpType,'agentSwitchIntfArpStatus':agentSwitchIntfArpStatus,'agentSwitchIpGroup':agentSwitchIpGroup,'agentSwitchIpRoutingMode':agentSwitchIpRoutingMode,'agentSwitchIpDefaultGateway':agentSwitchIpDefaultGateway,'agentSwitchIpInterfaceTable':agentSwitchIpInterfaceTable,'agentSwitchIpInterfaceEntry':agentSwitchIpInterfaceEntry,_L:agentSwitchIpInterfaceIfIndex,'agentSwitchIPAddressConfigMethod':agentSwitchIPAddressConfigMethod,'agentSwitchIpInterfaceIpAddress':agentSwitchIpInterfaceIpAddress,'agentSwitchIpInterfaceNetMask':agentSwitchIpInterfaceNetMask,'agentSwitchIpInterfaceClearIp':agentSwitchIpInterfaceClearIp,'agentSwitchIpInterfaceRoutingMode':agentSwitchIpInterfaceRoutingMode,'agentSwitchIpInterfaceMtuValue':agentSwitchIpInterfaceMtuValue,'agentSwitchIpInterfaceBandwidth':agentSwitchIpInterfaceBandwidth,'agentSwitchIpInterfaceUnnumberedIfIndex':agentSwitchIpInterfaceUnnumberedIfIndex,'agentSwitchIpInterfaceIcmpUnreachables':agentSwitchIpInterfaceIcmpUnreachables,'agentSwitchIpInterfaceIcmpRedirects':agentSwitchIpInterfaceIcmpRedirects,'agentSwitchDhcpOperation':agentSwitchDhcpOperation,'agentSwitchIpInterfaceSuppressed':agentSwitchIpInterfaceSuppressed,'agentSwitchIpInterfaceNumberOfFlaps':agentSwitchIpInterfaceNumberOfFlaps,'agentSwitchIpInterfaceCurrentPenalty':agentSwitchIpInterfaceCurrentPenalty,'agentSwitchIpInterfaceReUseTime':agentSwitchIpInterfaceReUseTime,'agentSwitchIpRouterDiscoveryTable':agentSwitchIpRouterDiscoveryTable,'agentSwitchIpRouterDiscoveryEntry':agentSwitchIpRouterDiscoveryEntry,_T:agentSwitchIpRouterDiscoveryIfIndex,'agentSwitchIpRouterDiscoveryAdvertiseMode':agentSwitchIpRouterDiscoveryAdvertiseMode,'agentSwitchIpRouterDiscoveryMaxAdvertisementInterval':agentSwitchIpRouterDiscoveryMaxAdvertisementInterval,'agentSwitchIpRouterDiscoveryMinAdvertisementInterval':agentSwitchIpRouterDiscoveryMinAdvertisementInterval,'agentSwitchIpRouterDiscoveryAdvertisementLifetime':agentSwitchIpRouterDiscoveryAdvertisementLifetime,'agentSwitchIpRouterDiscoveryPreferenceLevel':agentSwitchIpRouterDiscoveryPreferenceLevel,'agentSwitchIpRouterDiscoveryAdvertisementAddress':agentSwitchIpRouterDiscoveryAdvertisementAddress,'agentSwitchIpVlanTable':agentSwitchIpVlanTable,'agentSwitchIpVlanEntry':agentSwitchIpVlanEntry,_U:agentSwitchIpVlanId,'agentSwitchIpVlanIfIndex':agentSwitchIpVlanIfIndex,'agentSwitchIpVlanRoutingStatus':agentSwitchIpVlanRoutingStatus,'agentSwitchSecondaryAddressTable':agentSwitchSecondaryAddressTable,'agentSwitchSecondaryAddressEntry':agentSwitchSecondaryAddressEntry,_V:agentSwitchSecondaryIpAddress,'agentSwitchSecondaryNetMask':agentSwitchSecondaryNetMask,'agentSwitchSecondaryStatus':agentSwitchSecondaryStatus,'agentSwitchHelperAddressTable':agentSwitchHelperAddressTable,'agentSwitchHelperAddressEntry':agentSwitchHelperAddressEntry,_W:agentSwitchHelperIpAddress,'agentSwitchHelperStatus':agentSwitchHelperStatus,'agentSwitchIpIcmpControlGroup':agentSwitchIpIcmpControlGroup,'agentSwitchIpIcmpEchoReplyMode':agentSwitchIpIcmpEchoReplyMode,'agentSwitchIpIcmpRedirectsMode':agentSwitchIpIcmpRedirectsMode,'agentSwitchIpIcmpRateLimitInterval':agentSwitchIpIcmpRateLimitInterval,'agentSwitchIpIcmpRateLimitBurstSize':agentSwitchIpIcmpRateLimitBurstSize,'agentSwitchIntfIpHelperAddressTable':agentSwitchIntfIpHelperAddressTable,'agentSwitchIntfIpHelperAddressEntry':agentSwitchIntfIpHelperAddressEntry,_Y:agentSwitchIntfIpHelperIpAddress,_X:agentSwitchIntfIpHelperUdpPort,'agentSwitchIntfIpHelperDiscard':agentSwitchIntfIpHelperDiscard,'agentSwitchIntfIpHelperHitCount':agentSwitchIntfIpHelperHitCount,'agentSwitchIntfIpHelperStatus':agentSwitchIntfIpHelperStatus,'agentSwitchClearIpDefaultGateway':agentSwitchClearIpDefaultGateway,'agentBootpDhcpRelayGroup':agentBootpDhcpRelayGroup,'agentBootpDhcpRelayMaxHopCount':agentBootpDhcpRelayMaxHopCount,'agentBootpDhcpRelayForwardingIp':agentBootpDhcpRelayForwardingIp,'agentBootpDhcpRelayForwardMode':agentBootpDhcpRelayForwardMode,'agentBootpDhcpRelayMinWaitTime':agentBootpDhcpRelayMinWaitTime,'agentBootpDhcpRelayCircuitIdOptionMode':agentBootpDhcpRelayCircuitIdOptionMode,'agentBootpDhcpRelayNumOfRequestsReceived':agentBootpDhcpRelayNumOfRequestsReceived,'agentBootpDhcpRelayNumOfRequestsForwarded':agentBootpDhcpRelayNumOfRequestsForwarded,'agentBootpDhcpRelayNumOfDiscards':agentBootpDhcpRelayNumOfDiscards,'agentIpHelperGroup':agentIpHelperGroup,'agentIpHelperAdminMode':agentIpHelperAdminMode,'agentDhcpClientMsgsReceived':agentDhcpClientMsgsReceived,'agentDhcpClientMsgsRelayed':agentDhcpClientMsgsRelayed,'agentDhcpServerMsgsReceived':agentDhcpServerMsgsReceived,'agentDhcpServerMsgsRelayed':agentDhcpServerMsgsRelayed,'agentUdpClientMsgsReceived':agentUdpClientMsgsReceived,'agentUdpClientMsgsRelayed':agentUdpClientMsgsRelayed,'agentSwitchIpHelperAddressTable':agentSwitchIpHelperAddressTable,'agentSwitchIpHelperAddressEntry':agentSwitchIpHelperAddressEntry,_Z:agentSwitchIpHelperAddress,_a:agentSwitchIpHelperUdpPort,'agentSwitchIpHelperHitCount':agentSwitchIpHelperHitCount,'agentSwitchIpHelperStatus':agentSwitchIpHelperStatus,'agentUdpClientMsgsTtlExpired':agentUdpClientMsgsTtlExpired,'agentUdpClientMsgsDiscarded':agentUdpClientMsgsDiscarded,'agentInternalVlanGroup':agentInternalVlanGroup,'agentInternalVlanBase':agentInternalVlanBase,'agentInternalVlanPolicy':agentInternalVlanPolicy,'agentSwitchInternalVlanTable':agentSwitchInternalVlanTable,'agentSwitchInternalVlanEntry':agentSwitchInternalVlanEntry,_b:agentSwitchInternalVlanId,'agentSwitchInternalVlanIfIndex':agentSwitchInternalVlanIfIndex,'agentRoutingHeapGroup':agentRoutingHeapGroup,'agentRoutingHeapSize':agentRoutingHeapSize,'agentRoutingHeapInUse':agentRoutingHeapInUse,'agentRoutingHeapHigh':agentRoutingHeapHigh,'agentRoutingTableSummaryGroup':agentRoutingTableSummaryGroup,'agentConnectedRoutes':agentConnectedRoutes,'agentStaticRoutes':agentStaticRoutes,'agentRipRoutes':agentRipRoutes,'agentOspfRoutes':agentOspfRoutes,'agentOspfIntraRoutes':agentOspfIntraRoutes,'agentOspfInterRoutes':agentOspfInterRoutes,'agentOspfExt1Routes':agentOspfExt1Routes,'agentOspfExt2Routes':agentOspfExt2Routes,'agentBgpRoutes':agentBgpRoutes,'agentEbgpRoutes':agentEbgpRoutes,'agentIbgpRoutes':agentIbgpRoutes,'agentLocalBgpRoutes':agentLocalBgpRoutes,'agentRejectRoutes':agentRejectRoutes,'agentTotalRoutes':agentTotalRoutes,'agentBestRoutes':agentBestRoutes,'agentBestRoutesHigh':agentBestRoutesHigh,'agentAlternateRoutes':agentAlternateRoutes,'agentRouteAdds':agentRouteAdds,'agentRouteModifies':agentRouteModifies,'agentRouteDeletes':agentRouteDeletes,'agentUnresolvedRouteAdds':agentUnresolvedRouteAdds,'agentInvalidRouteAdds':agentInvalidRouteAdds,'agentFailedRouteAdds':agentFailedRouteAdds,'agentReservedLocals':agentReservedLocals,'agentUniqueNextHops':agentUniqueNextHops,'agentUniqueNextHopsHigh':agentUniqueNextHopsHigh,'agentNextHopGroups':agentNextHopGroups,'agentNextHopGroupsHigh':agentNextHopGroupsHigh,'agentEcmpGroups':agentEcmpGroups,'agentEcmpGroupsHigh':agentEcmpGroupsHigh,'agentEcmpRoutes':agentEcmpRoutes,'agentTruncEcmpRoutes':agentTruncEcmpRoutes,'agentEcmpRetries':agentEcmpRetries,'agentEcmpCountTable':agentEcmpCountTable,'agentEcmpCountEntry':agentEcmpCountEntry,_c:agentEcmpNextHopCount,'agentEcmpRouteCount':agentEcmpRouteCount})