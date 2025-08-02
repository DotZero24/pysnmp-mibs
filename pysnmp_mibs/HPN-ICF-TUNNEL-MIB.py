_T='hpnicfTunnelNvgreIfTunnNum'
_S='hpnicfTunnelEncapsMethod'
_R='hpnicfTunnelVxlanIfTunnNum'
_Q='hpnicfTunnelGreTunnNum'
_P='hpnicfTunnelEviLinkNum'
_O='hpnicfTunnelInetConfigTunnNum'
_N='hpnicfTunnelInetConfigSubSlot'
_M='hpnicfTunnelInetConfigSlot'
_L='TruthValue'
_K='Unsigned32'
_J='ifIndex'
_I='IF-MIB'
_H='hpnicfTunnelEviTunnNum'
_G='read-write'
_F='not-accessible'
_E='HPN-ICF-TUNNEL-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex','InterfaceIndexOrZero',_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
IPv6FlowLabelOrAny,=mibBuilder.importSymbols('IPV6-FLOW-LABEL-MIB','IPv6FlowLabelOrAny')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
hpnicfTunnel=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,53))
if mibBuilder.loadTexts:hpnicfTunnel.setRevisions(('2013-02-28 00:00',))
class HpnicfTunnelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54)));namedValues=NamedValues(*(('other',1),('direct',2),('gre',3),('minimal',4),('l2tp',5),('pptp',6),('l2f',7),('udp',8),('atmp',9),('msdp',10),('sixToFour',11),('sixOverFour',12),('isatap',13),('teredo',14),('tunnelModeReserve',35),('tunnelModeIPv4Gre',36),('tunnelModeIPv6Gre',37),('tunnelModeIPv4IPv4',38),('tunnelModeIPv4IPv6Config',39),('tunnelModeIPv4IPv6Auto',40),('tunnelModeIPv4IPv66to4',41),('tunnelModeIPv4IPv6Isatap',42),('tunnelModeIPv6IPv4',43),('tunnelModeIPv6IPv6',44),('tunnelModeIPv4UdpDVPN',45),('tunnelModeIPv4GreDVPN',46),('tunnelModeIPv6UdpDVPN',47),('tunnelModeIPv6GreDVPN',48),('tunnelModeCrLsp',49),('tunnelModeMax',50),('tunnelModeIPv4UdpVxlan',51),('tunnelModeIPv6UdpVxlan',52),('tunnelModeIPv4NVGRE',53),('tunnelModeIPv6NVGRE',54)))
_HpnicfTunnelMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfTunnelMIBObjects=_HpnicfTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,53,1))
_HpnicfTunnelTables_ObjectIdentity=ObjectIdentity
hpnicfTunnelTables=_HpnicfTunnelTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1))
_HpnicfTunnelIfTable_Object=MibTable
hpnicfTunnelIfTable=_HpnicfTunnelIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1))
if mibBuilder.loadTexts:hpnicfTunnelIfTable.setStatus(_A)
_HpnicfTunnelIfEntry_Object=MibTableRow
hpnicfTunnelIfEntry=_HpnicfTunnelIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1))
hpnicfTunnelIfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfTunnelIfEntry.setStatus(_A)
_HpnicfTunnelIfEncapsMethod_Type=HpnicfTunnelType
_HpnicfTunnelIfEncapsMethod_Object=MibTableColumn
hpnicfTunnelIfEncapsMethod=_HpnicfTunnelIfEncapsMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,3),_HpnicfTunnelIfEncapsMethod_Type())
hpnicfTunnelIfEncapsMethod.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelIfEncapsMethod.setStatus(_A)
class _HpnicfTunnelIfHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_HpnicfTunnelIfHopLimit_Type.__name__=_C
_HpnicfTunnelIfHopLimit_Object=MibTableColumn
hpnicfTunnelIfHopLimit=_HpnicfTunnelIfHopLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,4),_HpnicfTunnelIfHopLimit_Type())
hpnicfTunnelIfHopLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelIfHopLimit.setStatus(_A)
class _HpnicfTunnelIfSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipsec',2),('other',3)))
_HpnicfTunnelIfSecurity_Type.__name__=_C
_HpnicfTunnelIfSecurity_Object=MibTableColumn
hpnicfTunnelIfSecurity=_HpnicfTunnelIfSecurity_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,5),_HpnicfTunnelIfSecurity_Type())
hpnicfTunnelIfSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelIfSecurity.setStatus(_A)
class _HpnicfTunnelIfTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,63))
_HpnicfTunnelIfTOS_Type.__name__=_C
_HpnicfTunnelIfTOS_Object=MibTableColumn
hpnicfTunnelIfTOS=_HpnicfTunnelIfTOS_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,6),_HpnicfTunnelIfTOS_Type())
hpnicfTunnelIfTOS.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelIfTOS.setStatus(_A)
_HpnicfTunnelIfFlowLabel_Type=IPv6FlowLabelOrAny
_HpnicfTunnelIfFlowLabel_Object=MibTableColumn
hpnicfTunnelIfFlowLabel=_HpnicfTunnelIfFlowLabel_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,7),_HpnicfTunnelIfFlowLabel_Type())
hpnicfTunnelIfFlowLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelIfFlowLabel.setStatus(_A)
_HpnicfTunnelIfAddressType_Type=InetAddressType
_HpnicfTunnelIfAddressType_Object=MibTableColumn
hpnicfTunnelIfAddressType=_HpnicfTunnelIfAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,8),_HpnicfTunnelIfAddressType_Type())
hpnicfTunnelIfAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelIfAddressType.setStatus(_A)
_HpnicfTunnelIfLocalInetAddress_Type=InetAddress
_HpnicfTunnelIfLocalInetAddress_Object=MibTableColumn
hpnicfTunnelIfLocalInetAddress=_HpnicfTunnelIfLocalInetAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,9),_HpnicfTunnelIfLocalInetAddress_Type())
hpnicfTunnelIfLocalInetAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelIfLocalInetAddress.setStatus(_A)
_HpnicfTunnelIfRemoteInetAddress_Type=InetAddress
_HpnicfTunnelIfRemoteInetAddress_Object=MibTableColumn
hpnicfTunnelIfRemoteInetAddress=_HpnicfTunnelIfRemoteInetAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,10),_HpnicfTunnelIfRemoteInetAddress_Type())
hpnicfTunnelIfRemoteInetAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelIfRemoteInetAddress.setStatus(_A)
class _HpnicfTunnelIfEncapsLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_HpnicfTunnelIfEncapsLimit_Type.__name__=_C
_HpnicfTunnelIfEncapsLimit_Object=MibTableColumn
hpnicfTunnelIfEncapsLimit=_HpnicfTunnelIfEncapsLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,1,1,11),_HpnicfTunnelIfEncapsLimit_Type())
hpnicfTunnelIfEncapsLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelIfEncapsLimit.setStatus(_A)
_HpnicfTunnelInetConfigTable_Object=MibTable
hpnicfTunnelInetConfigTable=_HpnicfTunnelInetConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3))
if mibBuilder.loadTexts:hpnicfTunnelInetConfigTable.setStatus(_A)
_HpnicfTunnelInetConfigEntry_Object=MibTableRow
hpnicfTunnelInetConfigEntry=_HpnicfTunnelInetConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3,1))
hpnicfTunnelInetConfigEntry.setIndexNames((0,_E,_M),(0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:hpnicfTunnelInetConfigEntry.setStatus(_A)
class _HpnicfTunnelInetConfigSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfTunnelInetConfigSlot_Type.__name__=_C
_HpnicfTunnelInetConfigSlot_Object=MibTableColumn
hpnicfTunnelInetConfigSlot=_HpnicfTunnelInetConfigSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3,1,1),_HpnicfTunnelInetConfigSlot_Type())
hpnicfTunnelInetConfigSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelInetConfigSlot.setStatus(_A)
class _HpnicfTunnelInetConfigSubSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfTunnelInetConfigSubSlot_Type.__name__=_C
_HpnicfTunnelInetConfigSubSlot_Object=MibTableColumn
hpnicfTunnelInetConfigSubSlot=_HpnicfTunnelInetConfigSubSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3,1,2),_HpnicfTunnelInetConfigSubSlot_Type())
hpnicfTunnelInetConfigSubSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelInetConfigSubSlot.setStatus(_A)
class _HpnicfTunnelInetConfigTunnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfTunnelInetConfigTunnNum_Type.__name__=_C
_HpnicfTunnelInetConfigTunnNum_Object=MibTableColumn
hpnicfTunnelInetConfigTunnNum=_HpnicfTunnelInetConfigTunnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3,1,3),_HpnicfTunnelInetConfigTunnNum_Type())
hpnicfTunnelInetConfigTunnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelInetConfigTunnNum.setStatus(_A)
_HpnicfTunnelInetConfigIfIndex_Type=InterfaceIndexOrZero
_HpnicfTunnelInetConfigIfIndex_Object=MibTableColumn
hpnicfTunnelInetConfigIfIndex=_HpnicfTunnelInetConfigIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3,1,6),_HpnicfTunnelInetConfigIfIndex_Type())
hpnicfTunnelInetConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelInetConfigIfIndex.setStatus(_A)
_HpnicfTunnelInetConfigStatus_Type=RowStatus
_HpnicfTunnelInetConfigStatus_Object=MibTableColumn
hpnicfTunnelInetConfigStatus=_HpnicfTunnelInetConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,3,1,7),_HpnicfTunnelInetConfigStatus_Type())
hpnicfTunnelInetConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelInetConfigStatus.setStatus(_A)
_HpnicfTunnelEviTable_Object=MibTable
hpnicfTunnelEviTable=_HpnicfTunnelEviTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4))
if mibBuilder.loadTexts:hpnicfTunnelEviTable.setStatus(_A)
_HpnicfTunnelEviEntry_Object=MibTableRow
hpnicfTunnelEviEntry=_HpnicfTunnelEviEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1))
hpnicfTunnelEviEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hpnicfTunnelEviEntry.setStatus(_A)
class _HpnicfTunnelEviTunnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTunnelEviTunnNum_Type.__name__=_C
_HpnicfTunnelEviTunnNum_Object=MibTableColumn
hpnicfTunnelEviTunnNum=_HpnicfTunnelEviTunnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,1),_HpnicfTunnelEviTunnNum_Type())
hpnicfTunnelEviTunnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelEviTunnNum.setStatus(_A)
_HpnicfTunnelEviIfIndex_Type=InterfaceIndex
_HpnicfTunnelEviIfIndex_Object=MibTableColumn
hpnicfTunnelEviIfIndex=_HpnicfTunnelEviIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,2),_HpnicfTunnelEviIfIndex_Type())
hpnicfTunnelEviIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelEviIfIndex.setStatus(_A)
_HpnicfTunnelEviStatus_Type=RowStatus
_HpnicfTunnelEviStatus_Object=MibTableColumn
hpnicfTunnelEviStatus=_HpnicfTunnelEviStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,3),_HpnicfTunnelEviStatus_Type())
hpnicfTunnelEviStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelEviStatus.setStatus(_A)
_HpnicfTunnelEviAddressType_Type=InetAddressType
_HpnicfTunnelEviAddressType_Object=MibTableColumn
hpnicfTunnelEviAddressType=_HpnicfTunnelEviAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,4),_HpnicfTunnelEviAddressType_Type())
hpnicfTunnelEviAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelEviAddressType.setStatus(_A)
_HpnicfTunnelEviLocalAddr_Type=InetAddress
_HpnicfTunnelEviLocalAddr_Object=MibTableColumn
hpnicfTunnelEviLocalAddr=_HpnicfTunnelEviLocalAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,5),_HpnicfTunnelEviLocalAddr_Type())
hpnicfTunnelEviLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelEviLocalAddr.setStatus(_A)
class _HpnicfTunnelEviNetworkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_HpnicfTunnelEviNetworkID_Type.__name__=_C
_HpnicfTunnelEviNetworkID_Object=MibTableColumn
hpnicfTunnelEviNetworkID=_HpnicfTunnelEviNetworkID_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,6),_HpnicfTunnelEviNetworkID_Type())
hpnicfTunnelEviNetworkID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelEviNetworkID.setStatus(_A)
class _HpnicfTunnelEviKeepaliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HpnicfTunnelEviKeepaliveInterval_Type.__name__=_C
_HpnicfTunnelEviKeepaliveInterval_Object=MibTableColumn
hpnicfTunnelEviKeepaliveInterval=_HpnicfTunnelEviKeepaliveInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,7),_HpnicfTunnelEviKeepaliveInterval_Type())
hpnicfTunnelEviKeepaliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelEviKeepaliveInterval.setStatus(_A)
class _HpnicfTunnelEviKeepaliveTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfTunnelEviKeepaliveTimes_Type.__name__=_C
_HpnicfTunnelEviKeepaliveTimes_Object=MibTableColumn
hpnicfTunnelEviKeepaliveTimes=_HpnicfTunnelEviKeepaliveTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,4,1,8),_HpnicfTunnelEviKeepaliveTimes_Type())
hpnicfTunnelEviKeepaliveTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelEviKeepaliveTimes.setStatus(_A)
_HpnicfTunnelEviLinkTable_Object=MibTable
hpnicfTunnelEviLinkTable=_HpnicfTunnelEviLinkTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,5))
if mibBuilder.loadTexts:hpnicfTunnelEviLinkTable.setStatus(_A)
_HpnicfTunnelEviLinkEntry_Object=MibTableRow
hpnicfTunnelEviLinkEntry=_HpnicfTunnelEviLinkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,5,1))
hpnicfTunnelEviLinkEntry.setIndexNames((0,_E,_H),(0,_E,_P))
if mibBuilder.loadTexts:hpnicfTunnelEviLinkEntry.setStatus(_A)
class _HpnicfTunnelEviLinkNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTunnelEviLinkNum_Type.__name__=_C
_HpnicfTunnelEviLinkNum_Object=MibTableColumn
hpnicfTunnelEviLinkNum=_HpnicfTunnelEviLinkNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,5,1,1),_HpnicfTunnelEviLinkNum_Type())
hpnicfTunnelEviLinkNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelEviLinkNum.setStatus(_A)
_HpnicfTunnelEviLinkIfIndex_Type=InterfaceIndex
_HpnicfTunnelEviLinkIfIndex_Object=MibTableColumn
hpnicfTunnelEviLinkIfIndex=_HpnicfTunnelEviLinkIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,5,1,2),_HpnicfTunnelEviLinkIfIndex_Type())
hpnicfTunnelEviLinkIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelEviLinkIfIndex.setStatus(_A)
_HpnicfTunnelEviLinkAddressType_Type=InetAddressType
_HpnicfTunnelEviLinkAddressType_Object=MibTableColumn
hpnicfTunnelEviLinkAddressType=_HpnicfTunnelEviLinkAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,5,1,3),_HpnicfTunnelEviLinkAddressType_Type())
hpnicfTunnelEviLinkAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelEviLinkAddressType.setStatus(_A)
_HpnicfTunnelEviLinkRemoteAddr_Type=InetAddress
_HpnicfTunnelEviLinkRemoteAddr_Object=MibTableColumn
hpnicfTunnelEviLinkRemoteAddr=_HpnicfTunnelEviLinkRemoteAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,5,1,4),_HpnicfTunnelEviLinkRemoteAddr_Type())
hpnicfTunnelEviLinkRemoteAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelEviLinkRemoteAddr.setStatus(_A)
_HpnicfTunnelGreTable_Object=MibTable
hpnicfTunnelGreTable=_HpnicfTunnelGreTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6))
if mibBuilder.loadTexts:hpnicfTunnelGreTable.setStatus(_A)
_HpnicfTunnelGreEntry_Object=MibTableRow
hpnicfTunnelGreEntry=_HpnicfTunnelGreEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1))
hpnicfTunnelGreEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:hpnicfTunnelGreEntry.setStatus(_A)
class _HpnicfTunnelGreTunnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTunnelGreTunnNum_Type.__name__=_C
_HpnicfTunnelGreTunnNum_Object=MibTableColumn
hpnicfTunnelGreTunnNum=_HpnicfTunnelGreTunnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,1),_HpnicfTunnelGreTunnNum_Type())
hpnicfTunnelGreTunnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelGreTunnNum.setStatus(_A)
_HpnicfTunnelGreTunnIfIndex_Type=InterfaceIndex
_HpnicfTunnelGreTunnIfIndex_Object=MibTableColumn
hpnicfTunnelGreTunnIfIndex=_HpnicfTunnelGreTunnIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,2),_HpnicfTunnelGreTunnIfIndex_Type())
hpnicfTunnelGreTunnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelGreTunnIfIndex.setStatus(_A)
_HpnicfTunnelGreAddressType_Type=InetAddressType
_HpnicfTunnelGreAddressType_Object=MibTableColumn
hpnicfTunnelGreAddressType=_HpnicfTunnelGreAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,3),_HpnicfTunnelGreAddressType_Type())
hpnicfTunnelGreAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreAddressType.setStatus(_A)
_HpnicfTunnelGreLocalAddr_Type=InetAddress
_HpnicfTunnelGreLocalAddr_Object=MibTableColumn
hpnicfTunnelGreLocalAddr=_HpnicfTunnelGreLocalAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,4),_HpnicfTunnelGreLocalAddr_Type())
hpnicfTunnelGreLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreLocalAddr.setStatus(_A)
_HpnicfTunnelGreRemoteAddr_Type=InetAddress
_HpnicfTunnelGreRemoteAddr_Object=MibTableColumn
hpnicfTunnelGreRemoteAddr=_HpnicfTunnelGreRemoteAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,5),_HpnicfTunnelGreRemoteAddr_Type())
hpnicfTunnelGreRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreRemoteAddr.setStatus(_A)
class _HpnicfTunnelGreKeepaliveEnabled_Type(TruthValue):defaultValue=2
_HpnicfTunnelGreKeepaliveEnabled_Type.__name__=_L
_HpnicfTunnelGreKeepaliveEnabled_Object=MibTableColumn
hpnicfTunnelGreKeepaliveEnabled=_HpnicfTunnelGreKeepaliveEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,6),_HpnicfTunnelGreKeepaliveEnabled_Type())
hpnicfTunnelGreKeepaliveEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreKeepaliveEnabled.setStatus(_A)
class _HpnicfTunnelGreKeepaliveInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_HpnicfTunnelGreKeepaliveInterval_Type.__name__=_C
_HpnicfTunnelGreKeepaliveInterval_Object=MibTableColumn
hpnicfTunnelGreKeepaliveInterval=_HpnicfTunnelGreKeepaliveInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,7),_HpnicfTunnelGreKeepaliveInterval_Type())
hpnicfTunnelGreKeepaliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreKeepaliveInterval.setStatus(_A)
class _HpnicfTunnelGreKeepaliveTimes_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfTunnelGreKeepaliveTimes_Type.__name__=_C
_HpnicfTunnelGreKeepaliveTimes_Object=MibTableColumn
hpnicfTunnelGreKeepaliveTimes=_HpnicfTunnelGreKeepaliveTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,8),_HpnicfTunnelGreKeepaliveTimes_Type())
hpnicfTunnelGreKeepaliveTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreKeepaliveTimes.setStatus(_A)
class _HpnicfTunnelGreSlbgGroupNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfTunnelGreSlbgGroupNum_Type.__name__=_K
_HpnicfTunnelGreSlbgGroupNum_Object=MibTableColumn
hpnicfTunnelGreSlbgGroupNum=_HpnicfTunnelGreSlbgGroupNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,9),_HpnicfTunnelGreSlbgGroupNum_Type())
hpnicfTunnelGreSlbgGroupNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreSlbgGroupNum.setStatus(_A)
_HpnicfTunnelGreTunnStatus_Type=RowStatus
_HpnicfTunnelGreTunnStatus_Object=MibTableColumn
hpnicfTunnelGreTunnStatus=_HpnicfTunnelGreTunnStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,6,1,10),_HpnicfTunnelGreTunnStatus_Type())
hpnicfTunnelGreTunnStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelGreTunnStatus.setStatus(_A)
_HpnicfTunnelVxlanIfTable_Object=MibTable
hpnicfTunnelVxlanIfTable=_HpnicfTunnelVxlanIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7))
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfTable.setStatus(_A)
_HpnicfTunnelVxlanIfEntry_Object=MibTableRow
hpnicfTunnelVxlanIfEntry=_HpnicfTunnelVxlanIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1))
hpnicfTunnelVxlanIfEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfEntry.setStatus(_A)
class _HpnicfTunnelVxlanIfTunnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTunnelVxlanIfTunnNum_Type.__name__=_C
_HpnicfTunnelVxlanIfTunnNum_Object=MibTableColumn
hpnicfTunnelVxlanIfTunnNum=_HpnicfTunnelVxlanIfTunnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1,1),_HpnicfTunnelVxlanIfTunnNum_Type())
hpnicfTunnelVxlanIfTunnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfTunnNum.setStatus(_A)
_HpnicfTunnelVxlanTunnIfIndex_Type=InterfaceIndex
_HpnicfTunnelVxlanTunnIfIndex_Object=MibTableColumn
hpnicfTunnelVxlanTunnIfIndex=_HpnicfTunnelVxlanTunnIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1,2),_HpnicfTunnelVxlanTunnIfIndex_Type())
hpnicfTunnelVxlanTunnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelVxlanTunnIfIndex.setStatus(_A)
_HpnicfTunnelVxlanIfAddressType_Type=InetAddressType
_HpnicfTunnelVxlanIfAddressType_Object=MibTableColumn
hpnicfTunnelVxlanIfAddressType=_HpnicfTunnelVxlanIfAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1,3),_HpnicfTunnelVxlanIfAddressType_Type())
hpnicfTunnelVxlanIfAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfAddressType.setStatus(_A)
_HpnicfTunnelVxlanIfLocalAddr_Type=InetAddress
_HpnicfTunnelVxlanIfLocalAddr_Object=MibTableColumn
hpnicfTunnelVxlanIfLocalAddr=_HpnicfTunnelVxlanIfLocalAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1,4),_HpnicfTunnelVxlanIfLocalAddr_Type())
hpnicfTunnelVxlanIfLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfLocalAddr.setStatus(_A)
_HpnicfTunnelVxlanIfRemoteAddr_Type=InetAddress
_HpnicfTunnelVxlanIfRemoteAddr_Object=MibTableColumn
hpnicfTunnelVxlanIfRemoteAddr=_HpnicfTunnelVxlanIfRemoteAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1,5),_HpnicfTunnelVxlanIfRemoteAddr_Type())
hpnicfTunnelVxlanIfRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfRemoteAddr.setStatus(_A)
_HpnicfTunnelVxlanIfStatus_Type=RowStatus
_HpnicfTunnelVxlanIfStatus_Object=MibTableColumn
hpnicfTunnelVxlanIfStatus=_HpnicfTunnelVxlanIfStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,7,1,6),_HpnicfTunnelVxlanIfStatus_Type())
hpnicfTunnelVxlanIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelVxlanIfStatus.setStatus(_A)
_HpnicfTunnelVxlanConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfTunnelVxlanConfigGroup=_HpnicfTunnelVxlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,8))
class _HpnicfTunnelVxlanUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfTunnelVxlanUdpPort_Type.__name__=_C
_HpnicfTunnelVxlanUdpPort_Object=MibScalar
hpnicfTunnelVxlanUdpPort=_HpnicfTunnelVxlanUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,8,1),_HpnicfTunnelVxlanUdpPort_Type())
hpnicfTunnelVxlanUdpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelVxlanUdpPort.setStatus(_A)
_HpnicfTunnelVxlanDropWrongCksmPkt_Type=TruthValue
_HpnicfTunnelVxlanDropWrongCksmPkt_Object=MibScalar
hpnicfTunnelVxlanDropWrongCksmPkt=_HpnicfTunnelVxlanDropWrongCksmPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,8,2),_HpnicfTunnelVxlanDropWrongCksmPkt_Type())
hpnicfTunnelVxlanDropWrongCksmPkt.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelVxlanDropWrongCksmPkt.setStatus(_A)
_HpnicfTunnelVxlanDropVlanTagPkt_Type=TruthValue
_HpnicfTunnelVxlanDropVlanTagPkt_Object=MibScalar
hpnicfTunnelVxlanDropVlanTagPkt=_HpnicfTunnelVxlanDropVlanTagPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,8,3),_HpnicfTunnelVxlanDropVlanTagPkt_Type())
hpnicfTunnelVxlanDropVlanTagPkt.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfTunnelVxlanDropVlanTagPkt.setStatus(_A)
_HpnicfTunnelAvailableIDGroup_ObjectIdentity=ObjectIdentity
hpnicfTunnelAvailableIDGroup=_HpnicfTunnelAvailableIDGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,9))
class _HpnicfTunnelAvailableID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,2147483647))
_HpnicfTunnelAvailableID_Type.__name__=_C
_HpnicfTunnelAvailableID_Object=MibScalar
hpnicfTunnelAvailableID=_HpnicfTunnelAvailableID_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,9,1),_HpnicfTunnelAvailableID_Type())
hpnicfTunnelAvailableID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelAvailableID.setStatus(_A)
_HpnicfTunnelTotalNumTable_Object=MibTable
hpnicfTunnelTotalNumTable=_HpnicfTunnelTotalNumTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,10))
if mibBuilder.loadTexts:hpnicfTunnelTotalNumTable.setStatus(_A)
_HpnicfTunnelTotalNumEntry_Object=MibTableRow
hpnicfTunnelTotalNumEntry=_HpnicfTunnelTotalNumEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,10,1))
hpnicfTunnelTotalNumEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:hpnicfTunnelTotalNumEntry.setStatus(_A)
_HpnicfTunnelEncapsMethod_Type=HpnicfTunnelType
_HpnicfTunnelEncapsMethod_Object=MibTableColumn
hpnicfTunnelEncapsMethod=_HpnicfTunnelEncapsMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,10,1,1),_HpnicfTunnelEncapsMethod_Type())
hpnicfTunnelEncapsMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelEncapsMethod.setStatus(_A)
_HpnicfTunnelTotalNum_Type=Unsigned32
_HpnicfTunnelTotalNum_Object=MibTableColumn
hpnicfTunnelTotalNum=_HpnicfTunnelTotalNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,10,1,2),_HpnicfTunnelTotalNum_Type())
hpnicfTunnelTotalNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelTotalNum.setStatus(_A)
_HpnicfTunnelNvgreIfTable_Object=MibTable
hpnicfTunnelNvgreIfTable=_HpnicfTunnelNvgreIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11))
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfTable.setStatus(_A)
_HpnicfTunnelNvgreIfEntry_Object=MibTableRow
hpnicfTunnelNvgreIfEntry=_HpnicfTunnelNvgreIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1))
hpnicfTunnelNvgreIfEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfEntry.setStatus(_A)
class _HpnicfTunnelNvgreIfTunnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTunnelNvgreIfTunnNum_Type.__name__=_C
_HpnicfTunnelNvgreIfTunnNum_Object=MibTableColumn
hpnicfTunnelNvgreIfTunnNum=_HpnicfTunnelNvgreIfTunnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1,1),_HpnicfTunnelNvgreIfTunnNum_Type())
hpnicfTunnelNvgreIfTunnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfTunnNum.setStatus(_A)
_HpnicfTunnelNvgreTunnIfIndex_Type=InterfaceIndex
_HpnicfTunnelNvgreTunnIfIndex_Object=MibTableColumn
hpnicfTunnelNvgreTunnIfIndex=_HpnicfTunnelNvgreTunnIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1,2),_HpnicfTunnelNvgreTunnIfIndex_Type())
hpnicfTunnelNvgreTunnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfTunnelNvgreTunnIfIndex.setStatus(_A)
_HpnicfTunnelNvgreIfAddressType_Type=InetAddressType
_HpnicfTunnelNvgreIfAddressType_Object=MibTableColumn
hpnicfTunnelNvgreIfAddressType=_HpnicfTunnelNvgreIfAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1,3),_HpnicfTunnelNvgreIfAddressType_Type())
hpnicfTunnelNvgreIfAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfAddressType.setStatus(_A)
_HpnicfTunnelNvgreIfLocalAddr_Type=InetAddress
_HpnicfTunnelNvgreIfLocalAddr_Object=MibTableColumn
hpnicfTunnelNvgreIfLocalAddr=_HpnicfTunnelNvgreIfLocalAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1,4),_HpnicfTunnelNvgreIfLocalAddr_Type())
hpnicfTunnelNvgreIfLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfLocalAddr.setStatus(_A)
_HpnicfTunnelNvgreIfRemoteAddr_Type=InetAddress
_HpnicfTunnelNvgreIfRemoteAddr_Object=MibTableColumn
hpnicfTunnelNvgreIfRemoteAddr=_HpnicfTunnelNvgreIfRemoteAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1,5),_HpnicfTunnelNvgreIfRemoteAddr_Type())
hpnicfTunnelNvgreIfRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfRemoteAddr.setStatus(_A)
_HpnicfTunnelNvgreIfStatus_Type=RowStatus
_HpnicfTunnelNvgreIfStatus_Object=MibTableColumn
hpnicfTunnelNvgreIfStatus=_HpnicfTunnelNvgreIfStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,53,1,1,11,1,6),_HpnicfTunnelNvgreIfStatus_Type())
hpnicfTunnelNvgreIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTunnelNvgreIfStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'HpnicfTunnelType':HpnicfTunnelType,'hpnicfTunnel':hpnicfTunnel,'hpnicfTunnelMIBObjects':hpnicfTunnelMIBObjects,'hpnicfTunnelTables':hpnicfTunnelTables,'hpnicfTunnelIfTable':hpnicfTunnelIfTable,'hpnicfTunnelIfEntry':hpnicfTunnelIfEntry,'hpnicfTunnelIfEncapsMethod':hpnicfTunnelIfEncapsMethod,'hpnicfTunnelIfHopLimit':hpnicfTunnelIfHopLimit,'hpnicfTunnelIfSecurity':hpnicfTunnelIfSecurity,'hpnicfTunnelIfTOS':hpnicfTunnelIfTOS,'hpnicfTunnelIfFlowLabel':hpnicfTunnelIfFlowLabel,'hpnicfTunnelIfAddressType':hpnicfTunnelIfAddressType,'hpnicfTunnelIfLocalInetAddress':hpnicfTunnelIfLocalInetAddress,'hpnicfTunnelIfRemoteInetAddress':hpnicfTunnelIfRemoteInetAddress,'hpnicfTunnelIfEncapsLimit':hpnicfTunnelIfEncapsLimit,'hpnicfTunnelInetConfigTable':hpnicfTunnelInetConfigTable,'hpnicfTunnelInetConfigEntry':hpnicfTunnelInetConfigEntry,_M:hpnicfTunnelInetConfigSlot,_N:hpnicfTunnelInetConfigSubSlot,_O:hpnicfTunnelInetConfigTunnNum,'hpnicfTunnelInetConfigIfIndex':hpnicfTunnelInetConfigIfIndex,'hpnicfTunnelInetConfigStatus':hpnicfTunnelInetConfigStatus,'hpnicfTunnelEviTable':hpnicfTunnelEviTable,'hpnicfTunnelEviEntry':hpnicfTunnelEviEntry,_H:hpnicfTunnelEviTunnNum,'hpnicfTunnelEviIfIndex':hpnicfTunnelEviIfIndex,'hpnicfTunnelEviStatus':hpnicfTunnelEviStatus,'hpnicfTunnelEviAddressType':hpnicfTunnelEviAddressType,'hpnicfTunnelEviLocalAddr':hpnicfTunnelEviLocalAddr,'hpnicfTunnelEviNetworkID':hpnicfTunnelEviNetworkID,'hpnicfTunnelEviKeepaliveInterval':hpnicfTunnelEviKeepaliveInterval,'hpnicfTunnelEviKeepaliveTimes':hpnicfTunnelEviKeepaliveTimes,'hpnicfTunnelEviLinkTable':hpnicfTunnelEviLinkTable,'hpnicfTunnelEviLinkEntry':hpnicfTunnelEviLinkEntry,_P:hpnicfTunnelEviLinkNum,'hpnicfTunnelEviLinkIfIndex':hpnicfTunnelEviLinkIfIndex,'hpnicfTunnelEviLinkAddressType':hpnicfTunnelEviLinkAddressType,'hpnicfTunnelEviLinkRemoteAddr':hpnicfTunnelEviLinkRemoteAddr,'hpnicfTunnelGreTable':hpnicfTunnelGreTable,'hpnicfTunnelGreEntry':hpnicfTunnelGreEntry,_Q:hpnicfTunnelGreTunnNum,'hpnicfTunnelGreTunnIfIndex':hpnicfTunnelGreTunnIfIndex,'hpnicfTunnelGreAddressType':hpnicfTunnelGreAddressType,'hpnicfTunnelGreLocalAddr':hpnicfTunnelGreLocalAddr,'hpnicfTunnelGreRemoteAddr':hpnicfTunnelGreRemoteAddr,'hpnicfTunnelGreKeepaliveEnabled':hpnicfTunnelGreKeepaliveEnabled,'hpnicfTunnelGreKeepaliveInterval':hpnicfTunnelGreKeepaliveInterval,'hpnicfTunnelGreKeepaliveTimes':hpnicfTunnelGreKeepaliveTimes,'hpnicfTunnelGreSlbgGroupNum':hpnicfTunnelGreSlbgGroupNum,'hpnicfTunnelGreTunnStatus':hpnicfTunnelGreTunnStatus,'hpnicfTunnelVxlanIfTable':hpnicfTunnelVxlanIfTable,'hpnicfTunnelVxlanIfEntry':hpnicfTunnelVxlanIfEntry,_R:hpnicfTunnelVxlanIfTunnNum,'hpnicfTunnelVxlanTunnIfIndex':hpnicfTunnelVxlanTunnIfIndex,'hpnicfTunnelVxlanIfAddressType':hpnicfTunnelVxlanIfAddressType,'hpnicfTunnelVxlanIfLocalAddr':hpnicfTunnelVxlanIfLocalAddr,'hpnicfTunnelVxlanIfRemoteAddr':hpnicfTunnelVxlanIfRemoteAddr,'hpnicfTunnelVxlanIfStatus':hpnicfTunnelVxlanIfStatus,'hpnicfTunnelVxlanConfigGroup':hpnicfTunnelVxlanConfigGroup,'hpnicfTunnelVxlanUdpPort':hpnicfTunnelVxlanUdpPort,'hpnicfTunnelVxlanDropWrongCksmPkt':hpnicfTunnelVxlanDropWrongCksmPkt,'hpnicfTunnelVxlanDropVlanTagPkt':hpnicfTunnelVxlanDropVlanTagPkt,'hpnicfTunnelAvailableIDGroup':hpnicfTunnelAvailableIDGroup,'hpnicfTunnelAvailableID':hpnicfTunnelAvailableID,'hpnicfTunnelTotalNumTable':hpnicfTunnelTotalNumTable,'hpnicfTunnelTotalNumEntry':hpnicfTunnelTotalNumEntry,_S:hpnicfTunnelEncapsMethod,'hpnicfTunnelTotalNum':hpnicfTunnelTotalNum,'hpnicfTunnelNvgreIfTable':hpnicfTunnelNvgreIfTable,'hpnicfTunnelNvgreIfEntry':hpnicfTunnelNvgreIfEntry,_T:hpnicfTunnelNvgreIfTunnNum,'hpnicfTunnelNvgreTunnIfIndex':hpnicfTunnelNvgreTunnIfIndex,'hpnicfTunnelNvgreIfAddressType':hpnicfTunnelNvgreIfAddressType,'hpnicfTunnelNvgreIfLocalAddr':hpnicfTunnelNvgreIfLocalAddr,'hpnicfTunnelNvgreIfRemoteAddr':hpnicfTunnelNvgreIfRemoteAddr,'hpnicfTunnelNvgreIfStatus':hpnicfTunnelNvgreIfStatus})