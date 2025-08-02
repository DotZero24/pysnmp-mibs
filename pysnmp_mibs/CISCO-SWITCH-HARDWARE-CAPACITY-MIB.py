_As='cshcForwardingResourceGroup'
_Ar='cshcProtocolFibTcamWidthTypeGroup'
_Aq='cshcForwardingResourceValue'
_Ap='cshcForwardingResourceDescr'
_Ao='cshcProtocolFibTcamWidthType'
_An='cshcMetResourceMcastGrp'
_Am='cshcMetResourceTotal'
_Al='cshcMetResourceUsed'
_Ak='cshcMetResourceDescr'
_Aj='cshcModRxTopDropIfIndexList'
_Ai='cshcModTxTopDropIfIndexList'
_Ah='cshcQosResourceTotal'
_Ag='cshcQosResourceUsed'
_Af='cshcAdjacencyResourceTotal'
_Ae='cshcAdjacencyResourceUsed'
_Ad='cshcAdjacencyResourceDescr'
_Ac='cshcProtocolFibTcamLogicalTotal'
_Ab='cshcProtocolFibTcamLogicalUsed'
_Aa='cshcMacLinesFull'
_AZ='cshcMacLines'
_AY='cshcMacUcast'
_AX='cshcMacMcast'
_AW='cshcNetflowResourceUsageFail'
_AV='cshcNetflowResourceUsageFree'
_AU='cshcNetflowResourceUsageUsed'
_AT='cshcNetflowResourceUsageUtil'
_AS='cshcNetflowResourceUsageDescr'
_AR='cshc288bitsFibTcamTotal'
_AQ='cshc288bitsFibTcamUsed'
_AP='cshcNetflowFlowMaskFeature'
_AO='cshcNetflowFlowMaskType'
_AN='cshcIcamUtilization'
_AM='cshcIcamFailed'
_AL='cshcIcamCreated'
_AK='cshcCPURateLimiterReserved'
_AJ='cshcCPURateLimiterUsed'
_AI='cshcCPURateLimiterTotal'
_AH='cshcIntlChnlTxDroppedPackets'
_AG='cshcIntlChnlTxTotalPackets'
_AF='cshcIntlChnlTxPacketRate'
_AE='cshcIntlChnlRxDroppedPackets'
_AD='cshcIntlChnlRxTotalPackets'
_AC='cshcIntlChnlRxPacketRate'
_AB='cshcInterfaceReceiveBufferSize'
_AA='cshcInterfaceTransmitBufferSize'
_A9='cshcModRxTopDropPort'
_A8='cshcModTxTopDropPort'
_A7='cshcModRxTotalDroppedPackets'
_A6='cshcModTxTotalDroppedPackets'
_A5='cshcForwardingLoadPktPeakTime'
_A4='cshcForwardingLoadPktPeakRate'
_A3='cshcForwardingLoadPktRate'
_A2='cshcAdjacencyTotal'
_A1='cshcAdjacencyUsed'
_A0='cshcProtocolFibTcamTotal'
_z='cshcProtocolFibTcamUsed'
_y='cshc144bitsFibTcamTotal'
_x='cshc144bitsFibTcamUsed'
_w='cshc72bitsFibTcamTotal'
_v='cshc72bitsFibTcamUsed'
_u='cshcVpnCamTotal'
_t='cshcVpnCamUsed'
_s='cshcMacTotal'
_r='cshcMacUsed'
_q='cshcMacCollisions'
_p='cshcQosResourceType'
_o='cshcNetflowResourceUsageIndex'
_n='cshcNetflowFlowMaskIndex'
_m='cshcNetflowFlowMaskAddrType'
_l='cshcCPURateLimiterNetworkLayer'
_k='packets per second'
_j='cshcIntlChnlType'
_i='cshcForwardingResourceIndex'
_h='cshcMetResourceIndex'
_g='cshcAdjacencyResourceIndex'
_f='cshcProtocolFibTcamProtocol'
_e='ifIndex'
_d='IF-MIB'
_c='cshcMetResourceUsageGroup'
_b='cshcModTopDropIfIndexListGroup'
_a='cshcQosResourceUsageGroup'
_Z='cshcAdjacencyResourceUsageGroup'
_Y='cshcProtocolFibTcamUsageExtGroup'
_X='cshcMacUsageExtGroup'
_W='cshcNetflowFlowResourceUsageGroup'
_V='deprecated'
_U='Unsigned32'
_T='cshcFibTcamUsageExtGroup'
_S='cshcNetflowFlowMaskResourceGroup'
_R='cshcIcamResourcesGroup'
_Q='cshcCPURateLimiterResourcesGroup'
_P='cshcInternalChannelGroup'
_O='cshcInterfaceBufferGroup'
_N='cshcModuleInterfaceDropsGroup'
_M='cshcForwardingLoadGroup'
_L='cshcAdjacencyUsageGroup'
_K='cshcProtocolFibTcamUsageGroup'
_J='cshcFibTcamUsageGroup'
_I='cshcVpnCamUsageGroup'
_H='cshcMacUsageGroup'
_G='Integer32'
_F='not-accessible'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='current'
_A='CISCO-SWITCH-HARDWARE-CAPACITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Percent')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoInterfaceIndexList,=mibBuilder.importSymbols('CISCO-TC','CiscoInterfaceIndexList')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_d,'InterfaceIndexOrZero',_e)
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_U,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ciscoSwitchHardwareCapacityMIB=ModuleIdentity((1,3,6,1,4,1,9,9,663))
if mibBuilder.loadTexts:ciscoSwitchHardwareCapacityMIB.setRevisions(('2016-08-17 00:00','2014-09-16 00:00','2014-01-24 00:00','2013-05-08 00:00','2010-11-22 00:00','2008-07-02 00:00'))
class CshcInternalChannelType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eobc',1),('ibc',2)))
_CiscoSwitchHardwareCapacityMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSwitchHardwareCapacityMIBNotifs=_CiscoSwitchHardwareCapacityMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,663,0))
_CiscoSwitchHardwareCapacityMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchHardwareCapacityMIBObjects=_CiscoSwitchHardwareCapacityMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,663,1))
_CshcForwarding_ObjectIdentity=ObjectIdentity
cshcForwarding=_CshcForwarding_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,1))
_CshcL2Forwarding_ObjectIdentity=ObjectIdentity
cshcL2Forwarding=_CshcL2Forwarding_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,1,1))
_CshcMacUsageTable_Object=MibTable
cshcMacUsageTable=_CshcMacUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,1,1))
if mibBuilder.loadTexts:cshcMacUsageTable.setStatus(_B)
_CshcMacUsageEntry_Object=MibTableRow
cshcMacUsageEntry=_CshcMacUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1))
cshcMacUsageEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcMacUsageEntry.setStatus(_B)
_CshcMacCollisions_Type=Counter32
_CshcMacCollisions_Object=MibTableColumn
cshcMacCollisions=_CshcMacCollisions_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,1),_CshcMacCollisions_Type())
cshcMacCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacCollisions.setStatus(_B)
_CshcMacUsed_Type=Unsigned32
_CshcMacUsed_Object=MibTableColumn
cshcMacUsed=_CshcMacUsed_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,2),_CshcMacUsed_Type())
cshcMacUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacUsed.setStatus(_B)
_CshcMacTotal_Type=Unsigned32
_CshcMacTotal_Object=MibTableColumn
cshcMacTotal=_CshcMacTotal_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,3),_CshcMacTotal_Type())
cshcMacTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacTotal.setStatus(_B)
_CshcMacMcast_Type=Unsigned32
_CshcMacMcast_Object=MibTableColumn
cshcMacMcast=_CshcMacMcast_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,4),_CshcMacMcast_Type())
cshcMacMcast.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacMcast.setStatus(_B)
_CshcMacUcast_Type=Unsigned32
_CshcMacUcast_Object=MibTableColumn
cshcMacUcast=_CshcMacUcast_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,5),_CshcMacUcast_Type())
cshcMacUcast.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacUcast.setStatus(_B)
_CshcMacLines_Type=Unsigned32
_CshcMacLines_Object=MibTableColumn
cshcMacLines=_CshcMacLines_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,6),_CshcMacLines_Type())
cshcMacLines.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacLines.setStatus(_B)
_CshcMacLinesFull_Type=Unsigned32
_CshcMacLinesFull_Object=MibTableColumn
cshcMacLinesFull=_CshcMacLinesFull_Object((1,3,6,1,4,1,9,9,663,1,1,1,1,1,7),_CshcMacLinesFull_Type())
cshcMacLinesFull.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMacLinesFull.setStatus(_B)
_CshcVpnCamUsageTable_Object=MibTable
cshcVpnCamUsageTable=_CshcVpnCamUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,1,2))
if mibBuilder.loadTexts:cshcVpnCamUsageTable.setStatus(_B)
_CshcVpnCamUsageEntry_Object=MibTableRow
cshcVpnCamUsageEntry=_CshcVpnCamUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,1,2,1))
cshcVpnCamUsageEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcVpnCamUsageEntry.setStatus(_B)
_CshcVpnCamUsed_Type=Unsigned32
_CshcVpnCamUsed_Object=MibTableColumn
cshcVpnCamUsed=_CshcVpnCamUsed_Object((1,3,6,1,4,1,9,9,663,1,1,1,2,1,1),_CshcVpnCamUsed_Type())
cshcVpnCamUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcVpnCamUsed.setStatus(_B)
_CshcVpnCamTotal_Type=Unsigned32
_CshcVpnCamTotal_Object=MibTableColumn
cshcVpnCamTotal=_CshcVpnCamTotal_Object((1,3,6,1,4,1,9,9,663,1,1,1,2,1,2),_CshcVpnCamTotal_Type())
cshcVpnCamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcVpnCamTotal.setStatus(_B)
_CshcL3Forwarding_ObjectIdentity=ObjectIdentity
cshcL3Forwarding=_CshcL3Forwarding_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,1,2))
_CshcFibTcamUsageTable_Object=MibTable
cshcFibTcamUsageTable=_CshcFibTcamUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,1))
if mibBuilder.loadTexts:cshcFibTcamUsageTable.setStatus(_B)
_CshcFibTcamUsageEntry_Object=MibTableRow
cshcFibTcamUsageEntry=_CshcFibTcamUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1))
cshcFibTcamUsageEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcFibTcamUsageEntry.setStatus(_B)
_Cshc72bitsFibTcamUsed_Type=Unsigned32
_Cshc72bitsFibTcamUsed_Object=MibTableColumn
cshc72bitsFibTcamUsed=_Cshc72bitsFibTcamUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1,1),_Cshc72bitsFibTcamUsed_Type())
cshc72bitsFibTcamUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshc72bitsFibTcamUsed.setStatus(_B)
_Cshc72bitsFibTcamTotal_Type=Unsigned32
_Cshc72bitsFibTcamTotal_Object=MibTableColumn
cshc72bitsFibTcamTotal=_Cshc72bitsFibTcamTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1,2),_Cshc72bitsFibTcamTotal_Type())
cshc72bitsFibTcamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshc72bitsFibTcamTotal.setStatus(_B)
_Cshc144bitsFibTcamUsed_Type=Unsigned32
_Cshc144bitsFibTcamUsed_Object=MibTableColumn
cshc144bitsFibTcamUsed=_Cshc144bitsFibTcamUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1,3),_Cshc144bitsFibTcamUsed_Type())
cshc144bitsFibTcamUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshc144bitsFibTcamUsed.setStatus(_B)
_Cshc144bitsFibTcamTotal_Type=Unsigned32
_Cshc144bitsFibTcamTotal_Object=MibTableColumn
cshc144bitsFibTcamTotal=_Cshc144bitsFibTcamTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1,4),_Cshc144bitsFibTcamTotal_Type())
cshc144bitsFibTcamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshc144bitsFibTcamTotal.setStatus(_B)
_Cshc288bitsFibTcamUsed_Type=Unsigned32
_Cshc288bitsFibTcamUsed_Object=MibTableColumn
cshc288bitsFibTcamUsed=_Cshc288bitsFibTcamUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1,5),_Cshc288bitsFibTcamUsed_Type())
cshc288bitsFibTcamUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshc288bitsFibTcamUsed.setStatus(_B)
_Cshc288bitsFibTcamTotal_Type=Unsigned32
_Cshc288bitsFibTcamTotal_Object=MibTableColumn
cshc288bitsFibTcamTotal=_Cshc288bitsFibTcamTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,1,1,6),_Cshc288bitsFibTcamTotal_Type())
cshc288bitsFibTcamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshc288bitsFibTcamTotal.setStatus(_B)
_CshcProtocolFibTcamUsageTable_Object=MibTable
cshcProtocolFibTcamUsageTable=_CshcProtocolFibTcamUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,2))
if mibBuilder.loadTexts:cshcProtocolFibTcamUsageTable.setStatus(_B)
_CshcProtocolFibTcamUsageEntry_Object=MibTableRow
cshcProtocolFibTcamUsageEntry=_CshcProtocolFibTcamUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1))
cshcProtocolFibTcamUsageEntry.setIndexNames((0,_D,_E),(0,_A,_f))
if mibBuilder.loadTexts:cshcProtocolFibTcamUsageEntry.setStatus(_B)
class _CshcProtocolFibTcamProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('ipv4',1),('mpls',2),('eom',3),('ipv6',4),('ipv4Multicast',5),('ipv6Multicast',6),('l2VpnPeer',7),('l2VpnIpv4Multicast',8),('l2VpnIpv6Multicast',9),('fcoe',10),('mplsVpn',11),('fcMpls',12),('ipv6LocalLink',13),('allProtocols',14)))
_CshcProtocolFibTcamProtocol_Type.__name__=_G
_CshcProtocolFibTcamProtocol_Object=MibTableColumn
cshcProtocolFibTcamProtocol=_CshcProtocolFibTcamProtocol_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1,1),_CshcProtocolFibTcamProtocol_Type())
cshcProtocolFibTcamProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcProtocolFibTcamProtocol.setStatus(_B)
_CshcProtocolFibTcamUsed_Type=Unsigned32
_CshcProtocolFibTcamUsed_Object=MibTableColumn
cshcProtocolFibTcamUsed=_CshcProtocolFibTcamUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1,2),_CshcProtocolFibTcamUsed_Type())
cshcProtocolFibTcamUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcProtocolFibTcamUsed.setStatus(_B)
_CshcProtocolFibTcamTotal_Type=Unsigned32
_CshcProtocolFibTcamTotal_Object=MibTableColumn
cshcProtocolFibTcamTotal=_CshcProtocolFibTcamTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1,3),_CshcProtocolFibTcamTotal_Type())
cshcProtocolFibTcamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcProtocolFibTcamTotal.setStatus(_B)
_CshcProtocolFibTcamLogicalUsed_Type=Unsigned32
_CshcProtocolFibTcamLogicalUsed_Object=MibTableColumn
cshcProtocolFibTcamLogicalUsed=_CshcProtocolFibTcamLogicalUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1,4),_CshcProtocolFibTcamLogicalUsed_Type())
cshcProtocolFibTcamLogicalUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcProtocolFibTcamLogicalUsed.setStatus(_B)
_CshcProtocolFibTcamLogicalTotal_Type=Unsigned32
_CshcProtocolFibTcamLogicalTotal_Object=MibTableColumn
cshcProtocolFibTcamLogicalTotal=_CshcProtocolFibTcamLogicalTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1,5),_CshcProtocolFibTcamLogicalTotal_Type())
cshcProtocolFibTcamLogicalTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcProtocolFibTcamLogicalTotal.setStatus(_B)
class _CshcProtocolFibTcamWidthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('singleWidth',1),('doubleWidth',2),('quadWidth',3)))
_CshcProtocolFibTcamWidthType_Type.__name__=_G
_CshcProtocolFibTcamWidthType_Object=MibTableColumn
cshcProtocolFibTcamWidthType=_CshcProtocolFibTcamWidthType_Object((1,3,6,1,4,1,9,9,663,1,1,2,2,1,6),_CshcProtocolFibTcamWidthType_Type())
cshcProtocolFibTcamWidthType.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcProtocolFibTcamWidthType.setStatus(_B)
_CshcAdjacencyUsageTable_Object=MibTable
cshcAdjacencyUsageTable=_CshcAdjacencyUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,3))
if mibBuilder.loadTexts:cshcAdjacencyUsageTable.setStatus(_B)
_CshcAdjacencyUsageEntry_Object=MibTableRow
cshcAdjacencyUsageEntry=_CshcAdjacencyUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,3,1))
cshcAdjacencyUsageEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcAdjacencyUsageEntry.setStatus(_B)
_CshcAdjacencyUsed_Type=Unsigned32
_CshcAdjacencyUsed_Object=MibTableColumn
cshcAdjacencyUsed=_CshcAdjacencyUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,3,1,1),_CshcAdjacencyUsed_Type())
cshcAdjacencyUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcAdjacencyUsed.setStatus(_B)
_CshcAdjacencyTotal_Type=Unsigned32
_CshcAdjacencyTotal_Object=MibTableColumn
cshcAdjacencyTotal=_CshcAdjacencyTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,3,1,2),_CshcAdjacencyTotal_Type())
cshcAdjacencyTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcAdjacencyTotal.setStatus(_B)
_CshcForwardingLoadTable_Object=MibTable
cshcForwardingLoadTable=_CshcForwardingLoadTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,4))
if mibBuilder.loadTexts:cshcForwardingLoadTable.setStatus(_B)
_CshcForwardingLoadEntry_Object=MibTableRow
cshcForwardingLoadEntry=_CshcForwardingLoadEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,4,1))
cshcForwardingLoadEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcForwardingLoadEntry.setStatus(_B)
_CshcForwardingLoadPktRate_Type=CounterBasedGauge64
_CshcForwardingLoadPktRate_Object=MibTableColumn
cshcForwardingLoadPktRate=_CshcForwardingLoadPktRate_Object((1,3,6,1,4,1,9,9,663,1,1,2,4,1,1),_CshcForwardingLoadPktRate_Type())
cshcForwardingLoadPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcForwardingLoadPktRate.setStatus(_B)
if mibBuilder.loadTexts:cshcForwardingLoadPktRate.setUnits('pps')
_CshcForwardingLoadPktPeakRate_Type=CounterBasedGauge64
_CshcForwardingLoadPktPeakRate_Object=MibTableColumn
cshcForwardingLoadPktPeakRate=_CshcForwardingLoadPktPeakRate_Object((1,3,6,1,4,1,9,9,663,1,1,2,4,1,2),_CshcForwardingLoadPktPeakRate_Type())
cshcForwardingLoadPktPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcForwardingLoadPktPeakRate.setStatus(_B)
if mibBuilder.loadTexts:cshcForwardingLoadPktPeakRate.setUnits('pps')
_CshcForwardingLoadPktPeakTime_Type=DateAndTime
_CshcForwardingLoadPktPeakTime_Object=MibTableColumn
cshcForwardingLoadPktPeakTime=_CshcForwardingLoadPktPeakTime_Object((1,3,6,1,4,1,9,9,663,1,1,2,4,1,3),_CshcForwardingLoadPktPeakTime_Type())
cshcForwardingLoadPktPeakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcForwardingLoadPktPeakTime.setStatus(_B)
_CshcAdjacencyResourceUsageTable_Object=MibTable
cshcAdjacencyResourceUsageTable=_CshcAdjacencyResourceUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,5))
if mibBuilder.loadTexts:cshcAdjacencyResourceUsageTable.setStatus(_B)
_CshcAdjacencyResourceUsageEntry_Object=MibTableRow
cshcAdjacencyResourceUsageEntry=_CshcAdjacencyResourceUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,5,1))
cshcAdjacencyResourceUsageEntry.setIndexNames((0,_D,_E),(0,_A,_g))
if mibBuilder.loadTexts:cshcAdjacencyResourceUsageEntry.setStatus(_B)
_CshcAdjacencyResourceIndex_Type=Unsigned32
_CshcAdjacencyResourceIndex_Object=MibTableColumn
cshcAdjacencyResourceIndex=_CshcAdjacencyResourceIndex_Object((1,3,6,1,4,1,9,9,663,1,1,2,5,1,1),_CshcAdjacencyResourceIndex_Type())
cshcAdjacencyResourceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcAdjacencyResourceIndex.setStatus(_B)
_CshcAdjacencyResourceDescr_Type=SnmpAdminString
_CshcAdjacencyResourceDescr_Object=MibTableColumn
cshcAdjacencyResourceDescr=_CshcAdjacencyResourceDescr_Object((1,3,6,1,4,1,9,9,663,1,1,2,5,1,2),_CshcAdjacencyResourceDescr_Type())
cshcAdjacencyResourceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcAdjacencyResourceDescr.setStatus(_B)
_CshcAdjacencyResourceUsed_Type=Unsigned32
_CshcAdjacencyResourceUsed_Object=MibTableColumn
cshcAdjacencyResourceUsed=_CshcAdjacencyResourceUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,5,1,3),_CshcAdjacencyResourceUsed_Type())
cshcAdjacencyResourceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcAdjacencyResourceUsed.setStatus(_B)
_CshcAdjacencyResourceTotal_Type=Unsigned32
_CshcAdjacencyResourceTotal_Object=MibTableColumn
cshcAdjacencyResourceTotal=_CshcAdjacencyResourceTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,5,1,4),_CshcAdjacencyResourceTotal_Type())
cshcAdjacencyResourceTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcAdjacencyResourceTotal.setStatus(_B)
_CshcMetResourceUsageTable_Object=MibTable
cshcMetResourceUsageTable=_CshcMetResourceUsageTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,6))
if mibBuilder.loadTexts:cshcMetResourceUsageTable.setStatus(_B)
_CshcMetResourceUsageEntry_Object=MibTableRow
cshcMetResourceUsageEntry=_CshcMetResourceUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,6,1))
cshcMetResourceUsageEntry.setIndexNames((0,_D,_E),(0,_A,_h))
if mibBuilder.loadTexts:cshcMetResourceUsageEntry.setStatus(_B)
_CshcMetResourceIndex_Type=Unsigned32
_CshcMetResourceIndex_Object=MibTableColumn
cshcMetResourceIndex=_CshcMetResourceIndex_Object((1,3,6,1,4,1,9,9,663,1,1,2,6,1,1),_CshcMetResourceIndex_Type())
cshcMetResourceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcMetResourceIndex.setStatus(_B)
_CshcMetResourceDescr_Type=SnmpAdminString
_CshcMetResourceDescr_Object=MibTableColumn
cshcMetResourceDescr=_CshcMetResourceDescr_Object((1,3,6,1,4,1,9,9,663,1,1,2,6,1,2),_CshcMetResourceDescr_Type())
cshcMetResourceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMetResourceDescr.setStatus(_B)
_CshcMetResourceUsed_Type=Gauge32
_CshcMetResourceUsed_Object=MibTableColumn
cshcMetResourceUsed=_CshcMetResourceUsed_Object((1,3,6,1,4,1,9,9,663,1,1,2,6,1,3),_CshcMetResourceUsed_Type())
cshcMetResourceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMetResourceUsed.setStatus(_B)
_CshcMetResourceTotal_Type=Gauge32
_CshcMetResourceTotal_Object=MibTableColumn
cshcMetResourceTotal=_CshcMetResourceTotal_Object((1,3,6,1,4,1,9,9,663,1,1,2,6,1,4),_CshcMetResourceTotal_Type())
cshcMetResourceTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMetResourceTotal.setStatus(_B)
class _CshcMetResourceMcastGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CshcMetResourceMcastGrp_Type.__name__=_G
_CshcMetResourceMcastGrp_Object=MibTableColumn
cshcMetResourceMcastGrp=_CshcMetResourceMcastGrp_Object((1,3,6,1,4,1,9,9,663,1,1,2,6,1,5),_CshcMetResourceMcastGrp_Type())
cshcMetResourceMcastGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcMetResourceMcastGrp.setStatus(_B)
_CshcForwardingResourceTable_Object=MibTable
cshcForwardingResourceTable=_CshcForwardingResourceTable_Object((1,3,6,1,4,1,9,9,663,1,1,2,7))
if mibBuilder.loadTexts:cshcForwardingResourceTable.setStatus(_B)
_CshcForwardingResourceEntry_Object=MibTableRow
cshcForwardingResourceEntry=_CshcForwardingResourceEntry_Object((1,3,6,1,4,1,9,9,663,1,1,2,7,1))
cshcForwardingResourceEntry.setIndexNames((0,_D,_E),(0,_A,_i))
if mibBuilder.loadTexts:cshcForwardingResourceEntry.setStatus(_B)
class _CshcForwardingResourceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CshcForwardingResourceIndex_Type.__name__=_U
_CshcForwardingResourceIndex_Object=MibTableColumn
cshcForwardingResourceIndex=_CshcForwardingResourceIndex_Object((1,3,6,1,4,1,9,9,663,1,1,2,7,1,1),_CshcForwardingResourceIndex_Type())
cshcForwardingResourceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcForwardingResourceIndex.setStatus(_B)
_CshcForwardingResourceDescr_Type=SnmpAdminString
_CshcForwardingResourceDescr_Object=MibTableColumn
cshcForwardingResourceDescr=_CshcForwardingResourceDescr_Object((1,3,6,1,4,1,9,9,663,1,1,2,7,1,2),_CshcForwardingResourceDescr_Type())
cshcForwardingResourceDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcForwardingResourceDescr.setStatus(_B)
_CshcForwardingResourceValue_Type=Unsigned32
_CshcForwardingResourceValue_Object=MibTableColumn
cshcForwardingResourceValue=_CshcForwardingResourceValue_Object((1,3,6,1,4,1,9,9,663,1,1,2,7,1,3),_CshcForwardingResourceValue_Type())
cshcForwardingResourceValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcForwardingResourceValue.setStatus(_B)
_CshcInterface_ObjectIdentity=ObjectIdentity
cshcInterface=_CshcInterface_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,2))
_CshcModuleInterfaceDropsTable_Object=MibTable
cshcModuleInterfaceDropsTable=_CshcModuleInterfaceDropsTable_Object((1,3,6,1,4,1,9,9,663,1,2,1))
if mibBuilder.loadTexts:cshcModuleInterfaceDropsTable.setStatus(_B)
_CshcModuleInterfaceDropsEntry_Object=MibTableRow
cshcModuleInterfaceDropsEntry=_CshcModuleInterfaceDropsEntry_Object((1,3,6,1,4,1,9,9,663,1,2,1,1))
cshcModuleInterfaceDropsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcModuleInterfaceDropsEntry.setStatus(_B)
_CshcModTxTotalDroppedPackets_Type=Counter64
_CshcModTxTotalDroppedPackets_Object=MibTableColumn
cshcModTxTotalDroppedPackets=_CshcModTxTotalDroppedPackets_Object((1,3,6,1,4,1,9,9,663,1,2,1,1,1),_CshcModTxTotalDroppedPackets_Type())
cshcModTxTotalDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcModTxTotalDroppedPackets.setStatus(_B)
_CshcModRxTotalDroppedPackets_Type=Counter64
_CshcModRxTotalDroppedPackets_Object=MibTableColumn
cshcModRxTotalDroppedPackets=_CshcModRxTotalDroppedPackets_Object((1,3,6,1,4,1,9,9,663,1,2,1,1,2),_CshcModRxTotalDroppedPackets_Type())
cshcModRxTotalDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcModRxTotalDroppedPackets.setStatus(_B)
_CshcModTxTopDropPort_Type=InterfaceIndexOrZero
_CshcModTxTopDropPort_Object=MibTableColumn
cshcModTxTopDropPort=_CshcModTxTopDropPort_Object((1,3,6,1,4,1,9,9,663,1,2,1,1,3),_CshcModTxTopDropPort_Type())
cshcModTxTopDropPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcModTxTopDropPort.setStatus(_B)
_CshcModRxTopDropPort_Type=InterfaceIndexOrZero
_CshcModRxTopDropPort_Object=MibTableColumn
cshcModRxTopDropPort=_CshcModRxTopDropPort_Object((1,3,6,1,4,1,9,9,663,1,2,1,1,4),_CshcModRxTopDropPort_Type())
cshcModRxTopDropPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcModRxTopDropPort.setStatus(_B)
_CshcModTxTopDropIfIndexList_Type=CiscoInterfaceIndexList
_CshcModTxTopDropIfIndexList_Object=MibTableColumn
cshcModTxTopDropIfIndexList=_CshcModTxTopDropIfIndexList_Object((1,3,6,1,4,1,9,9,663,1,2,1,1,5),_CshcModTxTopDropIfIndexList_Type())
cshcModTxTopDropIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcModTxTopDropIfIndexList.setStatus(_B)
_CshcModRxTopDropIfIndexList_Type=CiscoInterfaceIndexList
_CshcModRxTopDropIfIndexList_Object=MibTableColumn
cshcModRxTopDropIfIndexList=_CshcModRxTopDropIfIndexList_Object((1,3,6,1,4,1,9,9,663,1,2,1,1,6),_CshcModRxTopDropIfIndexList_Type())
cshcModRxTopDropIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcModRxTopDropIfIndexList.setStatus(_B)
_CshcInterfaceBufferTable_Object=MibTable
cshcInterfaceBufferTable=_CshcInterfaceBufferTable_Object((1,3,6,1,4,1,9,9,663,1,2,2))
if mibBuilder.loadTexts:cshcInterfaceBufferTable.setStatus(_B)
_CshcInterfaceBufferEntry_Object=MibTableRow
cshcInterfaceBufferEntry=_CshcInterfaceBufferEntry_Object((1,3,6,1,4,1,9,9,663,1,2,2,1))
cshcInterfaceBufferEntry.setIndexNames((0,_d,_e))
if mibBuilder.loadTexts:cshcInterfaceBufferEntry.setStatus(_B)
_CshcInterfaceTransmitBufferSize_Type=Unsigned32
_CshcInterfaceTransmitBufferSize_Object=MibTableColumn
cshcInterfaceTransmitBufferSize=_CshcInterfaceTransmitBufferSize_Object((1,3,6,1,4,1,9,9,663,1,2,2,1,1),_CshcInterfaceTransmitBufferSize_Type())
cshcInterfaceTransmitBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcInterfaceTransmitBufferSize.setStatus(_B)
if mibBuilder.loadTexts:cshcInterfaceTransmitBufferSize.setUnits('bytes')
_CshcInterfaceReceiveBufferSize_Type=Unsigned32
_CshcInterfaceReceiveBufferSize_Object=MibTableColumn
cshcInterfaceReceiveBufferSize=_CshcInterfaceReceiveBufferSize_Object((1,3,6,1,4,1,9,9,663,1,2,2,1,2),_CshcInterfaceReceiveBufferSize_Type())
cshcInterfaceReceiveBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcInterfaceReceiveBufferSize.setStatus(_B)
if mibBuilder.loadTexts:cshcInterfaceReceiveBufferSize.setUnits('bytes')
_CshcInternalChannelTable_Object=MibTable
cshcInternalChannelTable=_CshcInternalChannelTable_Object((1,3,6,1,4,1,9,9,663,1,2,3))
if mibBuilder.loadTexts:cshcInternalChannelTable.setStatus(_B)
_CshcInternalChannelEntry_Object=MibTableRow
cshcInternalChannelEntry=_CshcInternalChannelEntry_Object((1,3,6,1,4,1,9,9,663,1,2,3,1))
cshcInternalChannelEntry.setIndexNames((0,_D,_E),(0,_A,_j))
if mibBuilder.loadTexts:cshcInternalChannelEntry.setStatus(_B)
_CshcIntlChnlType_Type=CshcInternalChannelType
_CshcIntlChnlType_Object=MibTableColumn
cshcIntlChnlType=_CshcIntlChnlType_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,1),_CshcIntlChnlType_Type())
cshcIntlChnlType.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcIntlChnlType.setStatus(_B)
_CshcIntlChnlRxPacketRate_Type=CounterBasedGauge64
_CshcIntlChnlRxPacketRate_Object=MibTableColumn
cshcIntlChnlRxPacketRate=_CshcIntlChnlRxPacketRate_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,2),_CshcIntlChnlRxPacketRate_Type())
cshcIntlChnlRxPacketRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIntlChnlRxPacketRate.setStatus(_B)
if mibBuilder.loadTexts:cshcIntlChnlRxPacketRate.setUnits(_k)
_CshcIntlChnlRxTotalPackets_Type=Counter64
_CshcIntlChnlRxTotalPackets_Object=MibTableColumn
cshcIntlChnlRxTotalPackets=_CshcIntlChnlRxTotalPackets_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,3),_CshcIntlChnlRxTotalPackets_Type())
cshcIntlChnlRxTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIntlChnlRxTotalPackets.setStatus(_B)
_CshcIntlChnlRxDroppedPackets_Type=Counter64
_CshcIntlChnlRxDroppedPackets_Object=MibTableColumn
cshcIntlChnlRxDroppedPackets=_CshcIntlChnlRxDroppedPackets_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,4),_CshcIntlChnlRxDroppedPackets_Type())
cshcIntlChnlRxDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIntlChnlRxDroppedPackets.setStatus(_B)
_CshcIntlChnlTxPacketRate_Type=CounterBasedGauge64
_CshcIntlChnlTxPacketRate_Object=MibTableColumn
cshcIntlChnlTxPacketRate=_CshcIntlChnlTxPacketRate_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,5),_CshcIntlChnlTxPacketRate_Type())
cshcIntlChnlTxPacketRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIntlChnlTxPacketRate.setStatus(_B)
if mibBuilder.loadTexts:cshcIntlChnlTxPacketRate.setUnits(_k)
_CshcIntlChnlTxTotalPackets_Type=Counter64
_CshcIntlChnlTxTotalPackets_Object=MibTableColumn
cshcIntlChnlTxTotalPackets=_CshcIntlChnlTxTotalPackets_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,6),_CshcIntlChnlTxTotalPackets_Type())
cshcIntlChnlTxTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIntlChnlTxTotalPackets.setStatus(_B)
_CshcIntlChnlTxDroppedPackets_Type=Counter64
_CshcIntlChnlTxDroppedPackets_Object=MibTableColumn
cshcIntlChnlTxDroppedPackets=_CshcIntlChnlTxDroppedPackets_Object((1,3,6,1,4,1,9,9,663,1,2,3,1,7),_CshcIntlChnlTxDroppedPackets_Type())
cshcIntlChnlTxDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIntlChnlTxDroppedPackets.setStatus(_B)
_CshcCPURateLimiterResources_ObjectIdentity=ObjectIdentity
cshcCPURateLimiterResources=_CshcCPURateLimiterResources_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,3))
_CshcCPURateLimiterResourcesTable_Object=MibTable
cshcCPURateLimiterResourcesTable=_CshcCPURateLimiterResourcesTable_Object((1,3,6,1,4,1,9,9,663,1,3,1))
if mibBuilder.loadTexts:cshcCPURateLimiterResourcesTable.setStatus(_B)
_CshcCPURateLimiterResourcesEntry_Object=MibTableRow
cshcCPURateLimiterResourcesEntry=_CshcCPURateLimiterResourcesEntry_Object((1,3,6,1,4,1,9,9,663,1,3,1,1))
cshcCPURateLimiterResourcesEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:cshcCPURateLimiterResourcesEntry.setStatus(_B)
class _CshcCPURateLimiterNetworkLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('layer2',1),('layer3',2),('layer2Input',3),('layer2Output',4)))
_CshcCPURateLimiterNetworkLayer_Type.__name__=_G
_CshcCPURateLimiterNetworkLayer_Object=MibTableColumn
cshcCPURateLimiterNetworkLayer=_CshcCPURateLimiterNetworkLayer_Object((1,3,6,1,4,1,9,9,663,1,3,1,1,1),_CshcCPURateLimiterNetworkLayer_Type())
cshcCPURateLimiterNetworkLayer.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcCPURateLimiterNetworkLayer.setStatus(_B)
_CshcCPURateLimiterTotal_Type=Unsigned32
_CshcCPURateLimiterTotal_Object=MibTableColumn
cshcCPURateLimiterTotal=_CshcCPURateLimiterTotal_Object((1,3,6,1,4,1,9,9,663,1,3,1,1,2),_CshcCPURateLimiterTotal_Type())
cshcCPURateLimiterTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcCPURateLimiterTotal.setStatus(_B)
_CshcCPURateLimiterUsed_Type=Unsigned32
_CshcCPURateLimiterUsed_Object=MibTableColumn
cshcCPURateLimiterUsed=_CshcCPURateLimiterUsed_Object((1,3,6,1,4,1,9,9,663,1,3,1,1,3),_CshcCPURateLimiterUsed_Type())
cshcCPURateLimiterUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcCPURateLimiterUsed.setStatus(_B)
_CshcCPURateLimiterReserved_Type=Unsigned32
_CshcCPURateLimiterReserved_Object=MibTableColumn
cshcCPURateLimiterReserved=_CshcCPURateLimiterReserved_Object((1,3,6,1,4,1,9,9,663,1,3,1,1,4),_CshcCPURateLimiterReserved_Type())
cshcCPURateLimiterReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcCPURateLimiterReserved.setStatus(_B)
_CshcIcamResources_ObjectIdentity=ObjectIdentity
cshcIcamResources=_CshcIcamResources_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,4))
_CshcIcamUtilizationTable_Object=MibTable
cshcIcamUtilizationTable=_CshcIcamUtilizationTable_Object((1,3,6,1,4,1,9,9,663,1,4,1))
if mibBuilder.loadTexts:cshcIcamUtilizationTable.setStatus(_B)
_CshcIcamUtilizationEntry_Object=MibTableRow
cshcIcamUtilizationEntry=_CshcIcamUtilizationEntry_Object((1,3,6,1,4,1,9,9,663,1,4,1,1))
cshcIcamUtilizationEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cshcIcamUtilizationEntry.setStatus(_B)
_CshcIcamCreated_Type=Unsigned32
_CshcIcamCreated_Object=MibTableColumn
cshcIcamCreated=_CshcIcamCreated_Object((1,3,6,1,4,1,9,9,663,1,4,1,1,1),_CshcIcamCreated_Type())
cshcIcamCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIcamCreated.setStatus(_B)
_CshcIcamFailed_Type=Unsigned32
_CshcIcamFailed_Object=MibTableColumn
cshcIcamFailed=_CshcIcamFailed_Object((1,3,6,1,4,1,9,9,663,1,4,1,1,2),_CshcIcamFailed_Type())
cshcIcamFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIcamFailed.setStatus(_B)
_CshcIcamUtilization_Type=Percent
_CshcIcamUtilization_Object=MibTableColumn
cshcIcamUtilization=_CshcIcamUtilization_Object((1,3,6,1,4,1,9,9,663,1,4,1,1,3),_CshcIcamUtilization_Type())
cshcIcamUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcIcamUtilization.setStatus(_B)
_CshcNetflowFlowMaskResources_ObjectIdentity=ObjectIdentity
cshcNetflowFlowMaskResources=_CshcNetflowFlowMaskResources_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,5))
_CshcNetflowFlowMaskTable_Object=MibTable
cshcNetflowFlowMaskTable=_CshcNetflowFlowMaskTable_Object((1,3,6,1,4,1,9,9,663,1,5,1))
if mibBuilder.loadTexts:cshcNetflowFlowMaskTable.setStatus(_B)
_CshcNetflowFlowMaskEntry_Object=MibTableRow
cshcNetflowFlowMaskEntry=_CshcNetflowFlowMaskEntry_Object((1,3,6,1,4,1,9,9,663,1,5,1,1))
cshcNetflowFlowMaskEntry.setIndexNames((0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:cshcNetflowFlowMaskEntry.setStatus(_B)
_CshcNetflowFlowMaskAddrType_Type=InetAddressType
_CshcNetflowFlowMaskAddrType_Object=MibTableColumn
cshcNetflowFlowMaskAddrType=_CshcNetflowFlowMaskAddrType_Object((1,3,6,1,4,1,9,9,663,1,5,1,1,1),_CshcNetflowFlowMaskAddrType_Type())
cshcNetflowFlowMaskAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcNetflowFlowMaskAddrType.setStatus(_B)
_CshcNetflowFlowMaskIndex_Type=Unsigned32
_CshcNetflowFlowMaskIndex_Object=MibTableColumn
cshcNetflowFlowMaskIndex=_CshcNetflowFlowMaskIndex_Object((1,3,6,1,4,1,9,9,663,1,5,1,1,2),_CshcNetflowFlowMaskIndex_Type())
cshcNetflowFlowMaskIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcNetflowFlowMaskIndex.setStatus(_B)
class _CshcNetflowFlowMaskType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37)));namedValues=NamedValues(*(('null',1),('srcOnly',2),('destOnly',3),('srcDest',4),('interfaceSrcDest',5),('fullFlow',6),('interfaceFullFlow',7),('interfaceFullFlowOrFullFlow',8),('atleastInterfaceSrcDest',9),('atleastFullFlow',10),('atleastInterfaceFullFlow',11),('atleastSrc',12),('atleastDst',13),('atleastSrcDst',14),('shortest',15),('lessThanFullFlow',16),('exceptFullFlow',17),('exceptInterfaceFullFlow',18),('interfaceDest',19),('atleastInterfaceDest',20),('interfaceSrc',21),('atleastInterfaceSrc',22),('srcOnlyCR',23),('dstOnlyCR',24),('fullFlowCR',25),('interfaceFullFlowCR',26),('max',27),('conflict',28),('err',29),('unused',30),('fullFlow1',31),('fullFlow2',32),('fullFlow3',33),('vlanFullFlow1',34),('vlanFullFlow2',35),('vlanFullFlow3',36),('reserved',37)))
_CshcNetflowFlowMaskType_Type.__name__=_G
_CshcNetflowFlowMaskType_Object=MibTableColumn
cshcNetflowFlowMaskType=_CshcNetflowFlowMaskType_Object((1,3,6,1,4,1,9,9,663,1,5,1,1,3),_CshcNetflowFlowMaskType_Type())
cshcNetflowFlowMaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowFlowMaskType.setStatus(_B)
class _CshcNetflowFlowMaskFeature_Type(Bits):namedValues=NamedValues(*(('null',0),('ipAcgIngress',1),('ipAcgEgress',2),('natIngress',3),('natEngress',4),('natInside',5),('pbr',6),('cryptoIngress',7),('cryptoEgress',8),('qos',9),('idsIngress',10),('tcpIntrcptEgress',11),('guardian',12),('ipv6AcgIngress',13),('ipv6AcgEgress',14),('mcastAcgIngress',15),('mcastAcgEgress',16),('mcastStub',17),('mcastUrd',18),('ipDsIngress',19),('ipDsEgress',20),('ipVaclIngress',21),('ipVaclEgress',22),('macVaclIngress',23),('macVaclEgress',24),('inspIngress',25),('inspEgress',26),('authProxy',27),('rpf',28),('wccpIngress',29),('wccpEgress',30),('inspDummyIngress',31),('inspDummyEgress',32),('nbarIngress',33),('nbarEgress',34),('ipv6Rpf',35),('ipv6GlobalDefault',36),('dai',37),('ipPaclIngress',38),('macPaclIngress',39),('mplsIcmpBridge',40),('ipSlb',41),('ipv4Default',42),('ipv6Default',43),('mplsDefault',44),('erSpanTermination',45),('ipv6Mcast',46),('ipDsL3Ingress',47),('ipDsL3Egress',48),('cryptoRedirectIngress',49),('otherDefault',50),('ipRecir',51),('iPAdmissionL3Eou',52),('iPAdmissionL2Eou',53),('iPAdmissionL2EouArp',54),('ipAdmissionL2Http',55),('ipAdmissionL2HttpArp',56),('ipv4L3IntfNde',57),('ipv4L2IntfNde',58),('ipSguardIngress',59),('pvtHostsIngress',60),('vrfNatIngress',61),('tcpAdjustMssIngress',62),('tcpAdjustMssEgress',63),('eomIw',64),('eomIw2',65),('ipv4VrfNdeEgress',66),('l1Egress',67),('l1Ingress',68),('l1GlobalEgress',69),('l1GlobalIngress',70),('ipDot1xAcl',71),('ipDot1xAclArp',72),('dot1ad',73),('ipSpanPcap',74),('ipv6CryptoRedirectIngress',75),('svcAcclrtIngress',76),('ipv6SvcAcclrtIngress',77),('nfAggregation',78),('nfSampling',79),('ipv6Guardian',80),('ipv6Qos',81),('none',82)))
_CshcNetflowFlowMaskFeature_Type.__name__='Bits'
_CshcNetflowFlowMaskFeature_Object=MibTableColumn
cshcNetflowFlowMaskFeature=_CshcNetflowFlowMaskFeature_Object((1,3,6,1,4,1,9,9,663,1,5,1,1,4),_CshcNetflowFlowMaskFeature_Type())
cshcNetflowFlowMaskFeature.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowFlowMaskFeature.setStatus(_B)
_CshcNetflowResourceUsage_ObjectIdentity=ObjectIdentity
cshcNetflowResourceUsage=_CshcNetflowResourceUsage_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,6))
_CshcNetflowResourceUsageTable_Object=MibTable
cshcNetflowResourceUsageTable=_CshcNetflowResourceUsageTable_Object((1,3,6,1,4,1,9,9,663,1,6,1))
if mibBuilder.loadTexts:cshcNetflowResourceUsageTable.setStatus(_B)
_CshcNetflowResourceUsageEntry_Object=MibTableRow
cshcNetflowResourceUsageEntry=_CshcNetflowResourceUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,6,1,1))
cshcNetflowResourceUsageEntry.setIndexNames((0,_D,_E),(0,_A,_o))
if mibBuilder.loadTexts:cshcNetflowResourceUsageEntry.setStatus(_B)
class _CshcNetflowResourceUsageIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CshcNetflowResourceUsageIndex_Type.__name__=_U
_CshcNetflowResourceUsageIndex_Object=MibTableColumn
cshcNetflowResourceUsageIndex=_CshcNetflowResourceUsageIndex_Object((1,3,6,1,4,1,9,9,663,1,6,1,1,1),_CshcNetflowResourceUsageIndex_Type())
cshcNetflowResourceUsageIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcNetflowResourceUsageIndex.setStatus(_B)
_CshcNetflowResourceUsageDescr_Type=SnmpAdminString
_CshcNetflowResourceUsageDescr_Object=MibTableColumn
cshcNetflowResourceUsageDescr=_CshcNetflowResourceUsageDescr_Object((1,3,6,1,4,1,9,9,663,1,6,1,1,2),_CshcNetflowResourceUsageDescr_Type())
cshcNetflowResourceUsageDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowResourceUsageDescr.setStatus(_B)
_CshcNetflowResourceUsageUtil_Type=Percent
_CshcNetflowResourceUsageUtil_Object=MibTableColumn
cshcNetflowResourceUsageUtil=_CshcNetflowResourceUsageUtil_Object((1,3,6,1,4,1,9,9,663,1,6,1,1,3),_CshcNetflowResourceUsageUtil_Type())
cshcNetflowResourceUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowResourceUsageUtil.setStatus(_B)
_CshcNetflowResourceUsageUsed_Type=Gauge32
_CshcNetflowResourceUsageUsed_Object=MibTableColumn
cshcNetflowResourceUsageUsed=_CshcNetflowResourceUsageUsed_Object((1,3,6,1,4,1,9,9,663,1,6,1,1,4),_CshcNetflowResourceUsageUsed_Type())
cshcNetflowResourceUsageUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowResourceUsageUsed.setStatus(_B)
_CshcNetflowResourceUsageFree_Type=Gauge32
_CshcNetflowResourceUsageFree_Object=MibTableColumn
cshcNetflowResourceUsageFree=_CshcNetflowResourceUsageFree_Object((1,3,6,1,4,1,9,9,663,1,6,1,1,5),_CshcNetflowResourceUsageFree_Type())
cshcNetflowResourceUsageFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowResourceUsageFree.setStatus(_B)
class _CshcNetflowResourceUsageFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_CshcNetflowResourceUsageFail_Type.__name__=_G
_CshcNetflowResourceUsageFail_Object=MibTableColumn
cshcNetflowResourceUsageFail=_CshcNetflowResourceUsageFail_Object((1,3,6,1,4,1,9,9,663,1,6,1,1,6),_CshcNetflowResourceUsageFail_Type())
cshcNetflowResourceUsageFail.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcNetflowResourceUsageFail.setStatus(_B)
_CshcQosResourceUsage_ObjectIdentity=ObjectIdentity
cshcQosResourceUsage=_CshcQosResourceUsage_ObjectIdentity((1,3,6,1,4,1,9,9,663,1,7))
_CshcQosResourceUsageTable_Object=MibTable
cshcQosResourceUsageTable=_CshcQosResourceUsageTable_Object((1,3,6,1,4,1,9,9,663,1,7,1))
if mibBuilder.loadTexts:cshcQosResourceUsageTable.setStatus(_B)
_CshcQosResourceUsageEntry_Object=MibTableRow
cshcQosResourceUsageEntry=_CshcQosResourceUsageEntry_Object((1,3,6,1,4,1,9,9,663,1,7,1,1))
cshcQosResourceUsageEntry.setIndexNames((0,_D,_E),(0,_A,_p))
if mibBuilder.loadTexts:cshcQosResourceUsageEntry.setStatus(_B)
class _CshcQosResourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aggregatePolicers',1),('distributedPolicers',2),('policerProfiles',3)))
_CshcQosResourceType_Type.__name__=_G
_CshcQosResourceType_Object=MibTableColumn
cshcQosResourceType=_CshcQosResourceType_Object((1,3,6,1,4,1,9,9,663,1,7,1,1,1),_CshcQosResourceType_Type())
cshcQosResourceType.setMaxAccess(_F)
if mibBuilder.loadTexts:cshcQosResourceType.setStatus(_B)
_CshcQosResourceUsed_Type=Unsigned32
_CshcQosResourceUsed_Object=MibTableColumn
cshcQosResourceUsed=_CshcQosResourceUsed_Object((1,3,6,1,4,1,9,9,663,1,7,1,1,2),_CshcQosResourceUsed_Type())
cshcQosResourceUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcQosResourceUsed.setStatus(_B)
_CshcQosResourceTotal_Type=Unsigned32
_CshcQosResourceTotal_Object=MibTableColumn
cshcQosResourceTotal=_CshcQosResourceTotal_Object((1,3,6,1,4,1,9,9,663,1,7,1,1,3),_CshcQosResourceTotal_Type())
cshcQosResourceTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cshcQosResourceTotal.setStatus(_B)
_CiscoSwitchHardwareCapacityMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSwitchHardwareCapacityMIBConformance=_CiscoSwitchHardwareCapacityMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,663,2))
_CiscoSwitchHardwareCapacityMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSwitchHardwareCapacityMIBCompliances=_CiscoSwitchHardwareCapacityMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,663,2,1))
_CiscoSwitchHardwareCapacityMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSwitchHardwareCapacityMIBGroups=_CiscoSwitchHardwareCapacityMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,663,2,2))
cshcMacUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,1))
cshcMacUsageGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:cshcMacUsageGroup.setStatus(_B)
cshcVpnCamUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,2))
cshcVpnCamUsageGroup.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cshcVpnCamUsageGroup.setStatus(_B)
cshcFibTcamUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,3))
cshcFibTcamUsageGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:cshcFibTcamUsageGroup.setStatus(_B)
cshcProtocolFibTcamUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,4))
cshcProtocolFibTcamUsageGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:cshcProtocolFibTcamUsageGroup.setStatus(_B)
cshcAdjacencyUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,5))
cshcAdjacencyUsageGroup.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:cshcAdjacencyUsageGroup.setStatus(_B)
cshcForwardingLoadGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,6))
cshcForwardingLoadGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cshcForwardingLoadGroup.setStatus(_B)
cshcModuleInterfaceDropsGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,7))
cshcModuleInterfaceDropsGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cshcModuleInterfaceDropsGroup.setStatus(_B)
cshcInterfaceBufferGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,8))
cshcInterfaceBufferGroup.setObjects(*((_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:cshcInterfaceBufferGroup.setStatus(_B)
cshcInternalChannelGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,9))
cshcInternalChannelGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:cshcInternalChannelGroup.setStatus(_B)
cshcCPURateLimiterResourcesGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,10))
cshcCPURateLimiterResourcesGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:cshcCPURateLimiterResourcesGroup.setStatus(_B)
cshcIcamResourcesGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,11))
cshcIcamResourcesGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cshcIcamResourcesGroup.setStatus(_B)
cshcNetflowFlowMaskResourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,12))
cshcNetflowFlowMaskResourceGroup.setObjects(*((_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:cshcNetflowFlowMaskResourceGroup.setStatus(_B)
cshcFibTcamUsageExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,13))
cshcFibTcamUsageExtGroup.setObjects(*((_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:cshcFibTcamUsageExtGroup.setStatus(_B)
cshcNetflowFlowResourceUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,14))
cshcNetflowFlowResourceUsageGroup.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:cshcNetflowFlowResourceUsageGroup.setStatus(_B)
cshcMacUsageExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,15))
cshcMacUsageExtGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:cshcMacUsageExtGroup.setStatus(_B)
cshcProtocolFibTcamUsageExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,16))
cshcProtocolFibTcamUsageExtGroup.setObjects(*((_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:cshcProtocolFibTcamUsageExtGroup.setStatus(_B)
cshcAdjacencyResourceUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,17))
cshcAdjacencyResourceUsageGroup.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:cshcAdjacencyResourceUsageGroup.setStatus(_B)
cshcQosResourceUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,18))
cshcQosResourceUsageGroup.setObjects(*((_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:cshcQosResourceUsageGroup.setStatus(_B)
cshcModTopDropIfIndexListGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,19))
cshcModTopDropIfIndexListGroup.setObjects(*((_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:cshcModTopDropIfIndexListGroup.setStatus(_B)
cshcMetResourceUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,20))
cshcMetResourceUsageGroup.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An)))
if mibBuilder.loadTexts:cshcMetResourceUsageGroup.setStatus(_B)
cshcProtocolFibTcamWidthTypeGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,21))
cshcProtocolFibTcamWidthTypeGroup.setObjects((_A,_Ao))
if mibBuilder.loadTexts:cshcProtocolFibTcamWidthTypeGroup.setStatus(_B)
cshcForwardingResourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,663,2,2,22))
cshcForwardingResourceGroup.setObjects(*((_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:cshcForwardingResourceGroup.setStatus(_B)
ciscoSwitchHardwareCapacityMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,663,2,1,1))
ciscoSwitchHardwareCapacityMIBCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoSwitchHardwareCapacityMIBCompliance.setStatus(_V)
ciscoSwitchHardwareCapacityMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,663,2,1,2))
ciscoSwitchHardwareCapacityMIBCompliance1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoSwitchHardwareCapacityMIBCompliance1.setStatus(_V)
ciscoSwitchHardwareCapacityMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,663,2,1,3))
ciscoSwitchHardwareCapacityMIBCompliance2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoSwitchHardwareCapacityMIBCompliance2.setStatus(_V)
ciscoSwitchHardwareCapacityMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,663,2,1,4))
ciscoSwitchHardwareCapacityMIBCompliance3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:ciscoSwitchHardwareCapacityMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CshcInternalChannelType':CshcInternalChannelType,'ciscoSwitchHardwareCapacityMIB':ciscoSwitchHardwareCapacityMIB,'ciscoSwitchHardwareCapacityMIBNotifs':ciscoSwitchHardwareCapacityMIBNotifs,'ciscoSwitchHardwareCapacityMIBObjects':ciscoSwitchHardwareCapacityMIBObjects,'cshcForwarding':cshcForwarding,'cshcL2Forwarding':cshcL2Forwarding,'cshcMacUsageTable':cshcMacUsageTable,'cshcMacUsageEntry':cshcMacUsageEntry,_q:cshcMacCollisions,_r:cshcMacUsed,_s:cshcMacTotal,_AX:cshcMacMcast,_AY:cshcMacUcast,_AZ:cshcMacLines,_Aa:cshcMacLinesFull,'cshcVpnCamUsageTable':cshcVpnCamUsageTable,'cshcVpnCamUsageEntry':cshcVpnCamUsageEntry,_t:cshcVpnCamUsed,_u:cshcVpnCamTotal,'cshcL3Forwarding':cshcL3Forwarding,'cshcFibTcamUsageTable':cshcFibTcamUsageTable,'cshcFibTcamUsageEntry':cshcFibTcamUsageEntry,_v:cshc72bitsFibTcamUsed,_w:cshc72bitsFibTcamTotal,_x:cshc144bitsFibTcamUsed,_y:cshc144bitsFibTcamTotal,_AQ:cshc288bitsFibTcamUsed,_AR:cshc288bitsFibTcamTotal,'cshcProtocolFibTcamUsageTable':cshcProtocolFibTcamUsageTable,'cshcProtocolFibTcamUsageEntry':cshcProtocolFibTcamUsageEntry,_f:cshcProtocolFibTcamProtocol,_z:cshcProtocolFibTcamUsed,_A0:cshcProtocolFibTcamTotal,_Ab:cshcProtocolFibTcamLogicalUsed,_Ac:cshcProtocolFibTcamLogicalTotal,_Ao:cshcProtocolFibTcamWidthType,'cshcAdjacencyUsageTable':cshcAdjacencyUsageTable,'cshcAdjacencyUsageEntry':cshcAdjacencyUsageEntry,_A1:cshcAdjacencyUsed,_A2:cshcAdjacencyTotal,'cshcForwardingLoadTable':cshcForwardingLoadTable,'cshcForwardingLoadEntry':cshcForwardingLoadEntry,_A3:cshcForwardingLoadPktRate,_A4:cshcForwardingLoadPktPeakRate,_A5:cshcForwardingLoadPktPeakTime,'cshcAdjacencyResourceUsageTable':cshcAdjacencyResourceUsageTable,'cshcAdjacencyResourceUsageEntry':cshcAdjacencyResourceUsageEntry,_g:cshcAdjacencyResourceIndex,_Ad:cshcAdjacencyResourceDescr,_Ae:cshcAdjacencyResourceUsed,_Af:cshcAdjacencyResourceTotal,'cshcMetResourceUsageTable':cshcMetResourceUsageTable,'cshcMetResourceUsageEntry':cshcMetResourceUsageEntry,_h:cshcMetResourceIndex,_Ak:cshcMetResourceDescr,_Al:cshcMetResourceUsed,_Am:cshcMetResourceTotal,_An:cshcMetResourceMcastGrp,'cshcForwardingResourceTable':cshcForwardingResourceTable,'cshcForwardingResourceEntry':cshcForwardingResourceEntry,_i:cshcForwardingResourceIndex,_Ap:cshcForwardingResourceDescr,_Aq:cshcForwardingResourceValue,'cshcInterface':cshcInterface,'cshcModuleInterfaceDropsTable':cshcModuleInterfaceDropsTable,'cshcModuleInterfaceDropsEntry':cshcModuleInterfaceDropsEntry,_A6:cshcModTxTotalDroppedPackets,_A7:cshcModRxTotalDroppedPackets,_A8:cshcModTxTopDropPort,_A9:cshcModRxTopDropPort,_Ai:cshcModTxTopDropIfIndexList,_Aj:cshcModRxTopDropIfIndexList,'cshcInterfaceBufferTable':cshcInterfaceBufferTable,'cshcInterfaceBufferEntry':cshcInterfaceBufferEntry,_AA:cshcInterfaceTransmitBufferSize,_AB:cshcInterfaceReceiveBufferSize,'cshcInternalChannelTable':cshcInternalChannelTable,'cshcInternalChannelEntry':cshcInternalChannelEntry,_j:cshcIntlChnlType,_AC:cshcIntlChnlRxPacketRate,_AD:cshcIntlChnlRxTotalPackets,_AE:cshcIntlChnlRxDroppedPackets,_AF:cshcIntlChnlTxPacketRate,_AG:cshcIntlChnlTxTotalPackets,_AH:cshcIntlChnlTxDroppedPackets,'cshcCPURateLimiterResources':cshcCPURateLimiterResources,'cshcCPURateLimiterResourcesTable':cshcCPURateLimiterResourcesTable,'cshcCPURateLimiterResourcesEntry':cshcCPURateLimiterResourcesEntry,_l:cshcCPURateLimiterNetworkLayer,_AI:cshcCPURateLimiterTotal,_AJ:cshcCPURateLimiterUsed,_AK:cshcCPURateLimiterReserved,'cshcIcamResources':cshcIcamResources,'cshcIcamUtilizationTable':cshcIcamUtilizationTable,'cshcIcamUtilizationEntry':cshcIcamUtilizationEntry,_AL:cshcIcamCreated,_AM:cshcIcamFailed,_AN:cshcIcamUtilization,'cshcNetflowFlowMaskResources':cshcNetflowFlowMaskResources,'cshcNetflowFlowMaskTable':cshcNetflowFlowMaskTable,'cshcNetflowFlowMaskEntry':cshcNetflowFlowMaskEntry,_m:cshcNetflowFlowMaskAddrType,_n:cshcNetflowFlowMaskIndex,_AO:cshcNetflowFlowMaskType,_AP:cshcNetflowFlowMaskFeature,'cshcNetflowResourceUsage':cshcNetflowResourceUsage,'cshcNetflowResourceUsageTable':cshcNetflowResourceUsageTable,'cshcNetflowResourceUsageEntry':cshcNetflowResourceUsageEntry,_o:cshcNetflowResourceUsageIndex,_AS:cshcNetflowResourceUsageDescr,_AT:cshcNetflowResourceUsageUtil,_AU:cshcNetflowResourceUsageUsed,_AV:cshcNetflowResourceUsageFree,_AW:cshcNetflowResourceUsageFail,'cshcQosResourceUsage':cshcQosResourceUsage,'cshcQosResourceUsageTable':cshcQosResourceUsageTable,'cshcQosResourceUsageEntry':cshcQosResourceUsageEntry,_p:cshcQosResourceType,_Ag:cshcQosResourceUsed,_Ah:cshcQosResourceTotal,'ciscoSwitchHardwareCapacityMIBConformance':ciscoSwitchHardwareCapacityMIBConformance,'ciscoSwitchHardwareCapacityMIBCompliances':ciscoSwitchHardwareCapacityMIBCompliances,'ciscoSwitchHardwareCapacityMIBCompliance':ciscoSwitchHardwareCapacityMIBCompliance,'ciscoSwitchHardwareCapacityMIBCompliance1':ciscoSwitchHardwareCapacityMIBCompliance1,'ciscoSwitchHardwareCapacityMIBCompliance2':ciscoSwitchHardwareCapacityMIBCompliance2,'ciscoSwitchHardwareCapacityMIBCompliance3':ciscoSwitchHardwareCapacityMIBCompliance3,'ciscoSwitchHardwareCapacityMIBGroups':ciscoSwitchHardwareCapacityMIBGroups,_H:cshcMacUsageGroup,_I:cshcVpnCamUsageGroup,_J:cshcFibTcamUsageGroup,_K:cshcProtocolFibTcamUsageGroup,_L:cshcAdjacencyUsageGroup,_M:cshcForwardingLoadGroup,_N:cshcModuleInterfaceDropsGroup,_O:cshcInterfaceBufferGroup,_P:cshcInternalChannelGroup,_Q:cshcCPURateLimiterResourcesGroup,_R:cshcIcamResourcesGroup,_S:cshcNetflowFlowMaskResourceGroup,_T:cshcFibTcamUsageExtGroup,_W:cshcNetflowFlowResourceUsageGroup,_X:cshcMacUsageExtGroup,_Y:cshcProtocolFibTcamUsageExtGroup,_Z:cshcAdjacencyResourceUsageGroup,_a:cshcQosResourceUsageGroup,_b:cshcModTopDropIfIndexListGroup,_c:cshcMetResourceUsageGroup,_Ar:cshcProtocolFibTcamWidthTypeGroup,_As:cshcForwardingResourceGroup})