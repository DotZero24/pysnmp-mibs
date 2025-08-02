_x='hpicfVirtualNetworkNotificationsGroup'
_w='hpicfVirtualNetworkNotifyScalarsGroup'
_v='hpicfVXLANTunnelScalarGroup'
_u='hpicfVXLANTunnelStatsGroup'
_t='hpicfVirtualNetworkScalarGroup'
_s='hpicfVirtualNetworkGroup'
_r='hpicfVirtualNetworkIcmpErrorRcvd'
_q='hpicfMTUDropNotifyEnable'
_p='hpicfVXLANTunnelUDPPort'
_o='hpicfVXLANTunnelEnable'
_n='hpicfVXLANTunnelGlobalStatsClear'
_m='hpicfVXLANTunnelGlobalStatsDropCount'
_l='hpicfVXLANTunnelStatsTxMTUViolation'
_k='hpicfTotalVXLANTunnels'
_j='hpicfMaxVXLANTunnels'
_i='hpicfVXLANTunnelStatsClear'
_h='hpicfVXLANTunnelStatsTxPackets'
_g='hpicfVXLANTunnelStatsRxPackets'
_f='hpicfVXLANTunnelIfNextHopPortName'
_e='hpicfVXLANTunnelIfNextHopInterface'
_d='hpicfVXLANTunnelIfNextHopIp'
_c='hpicfVXLANTunnelIfNextHopIpType'
_b='hpicfVXLANTunnelIfDownReason'
_a='hpicfTotalVirtualNetworks'
_Z='hpicfMaxVirtualNetworks'
_Y='hpicfVirtualNetworkRowStatus'
_X='hpicfVirtualNetworkVLANID'
_W='hpicfVirtualNetworkName'
_V='hpicfVXLANTunnelIfEntry'
_U='hpicfVirtualNetworkID'
_T='tunnelIfRemoteInetAddress'
_S='tunnelIfLocalInetAddress'
_R='tunnelIfAddressType'
_Q='TruthValue'
_P='hpicfMTUDropInIfIndex'
_O='hpicfMTUDropVTEPDest'
_N='hpicfMTUDropVTEPDstAddrType'
_M='hpicfMTUDropVTEPSource'
_L='hpicfMTUDropVTEPSrcAddrType'
_K='hpicfMTUDropRouterMTU'
_J='hpicfMTUDropRouterAddr'
_I='hpicfMTUDropRouterAddrType'
_H='read-create'
_G='TUNNEL-MIB'
_F='read-write'
_E='Integer32'
_D='accessible-for-notify'
_C='read-only'
_B='current'
_A='HP-ICF-VIRTUAL-NETWORK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_Q)
tunnelIfAddressType,tunnelIfEntry,tunnelIfLocalInetAddress,tunnelIfRemoteInetAddress=mibBuilder.importSymbols(_G,_R,'tunnelIfEntry',_S,_T)
hpicfVirtualNetwork=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107))
if mibBuilder.loadTexts:hpicfVirtualNetwork.setRevisions(('2014-03-19 00:00',))
_HpicfVirtualNetworkNotifications_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkNotifications=_HpicfVirtualNetworkNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,0))
_HpicfVirtualNetworkObjects_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkObjects=_HpicfVirtualNetworkObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,1))
_HpicfVirtualNetworkScalars_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkScalars=_HpicfVirtualNetworkScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,1,1))
_HpicfMaxVirtualNetworks_Type=Unsigned32
_HpicfMaxVirtualNetworks_Object=MibScalar
hpicfMaxVirtualNetworks=_HpicfMaxVirtualNetworks_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,1,1),_HpicfMaxVirtualNetworks_Type())
hpicfMaxVirtualNetworks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMaxVirtualNetworks.setStatus(_B)
_HpicfTotalVirtualNetworks_Type=Unsigned32
_HpicfTotalVirtualNetworks_Object=MibScalar
hpicfTotalVirtualNetworks=_HpicfTotalVirtualNetworks_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,1,2),_HpicfTotalVirtualNetworks_Type())
hpicfTotalVirtualNetworks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTotalVirtualNetworks.setStatus(_B)
_HpicfVirtualNetworkTable_Object=MibTable
hpicfVirtualNetworkTable=_HpicfVirtualNetworkTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,2))
if mibBuilder.loadTexts:hpicfVirtualNetworkTable.setStatus(_B)
_HpicfVirtualNetworkEntry_Object=MibTableRow
hpicfVirtualNetworkEntry=_HpicfVirtualNetworkEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,2,1))
hpicfVirtualNetworkEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:hpicfVirtualNetworkEntry.setStatus(_B)
class _HpicfVirtualNetworkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777215))
_HpicfVirtualNetworkID_Type.__name__=_E
_HpicfVirtualNetworkID_Object=MibTableColumn
hpicfVirtualNetworkID=_HpicfVirtualNetworkID_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,2,1,1),_HpicfVirtualNetworkID_Type())
hpicfVirtualNetworkID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfVirtualNetworkID.setStatus(_B)
_HpicfVirtualNetworkName_Type=SnmpAdminString
_HpicfVirtualNetworkName_Object=MibTableColumn
hpicfVirtualNetworkName=_HpicfVirtualNetworkName_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,2,1,2),_HpicfVirtualNetworkName_Type())
hpicfVirtualNetworkName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVirtualNetworkName.setStatus(_B)
_HpicfVirtualNetworkVLANID_Type=VlanIndex
_HpicfVirtualNetworkVLANID_Object=MibTableColumn
hpicfVirtualNetworkVLANID=_HpicfVirtualNetworkVLANID_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,2,1,3),_HpicfVirtualNetworkVLANID_Type())
hpicfVirtualNetworkVLANID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVirtualNetworkVLANID.setStatus(_B)
_HpicfVirtualNetworkRowStatus_Type=RowStatus
_HpicfVirtualNetworkRowStatus_Object=MibTableColumn
hpicfVirtualNetworkRowStatus=_HpicfVirtualNetworkRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,2,1,4),_HpicfVirtualNetworkRowStatus_Type())
hpicfVirtualNetworkRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfVirtualNetworkRowStatus.setStatus(_B)
_HpicfVirtualNetworkNotifyScalars_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkNotifyScalars=_HpicfVirtualNetworkNotifyScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3))
_HpicfMTUDropRouterAddrType_Type=InetAddressType
_HpicfMTUDropRouterAddrType_Object=MibScalar
hpicfMTUDropRouterAddrType=_HpicfMTUDropRouterAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,1),_HpicfMTUDropRouterAddrType_Type())
hpicfMTUDropRouterAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropRouterAddrType.setStatus(_B)
_HpicfMTUDropRouterAddr_Type=InetAddress
_HpicfMTUDropRouterAddr_Object=MibScalar
hpicfMTUDropRouterAddr=_HpicfMTUDropRouterAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,2),_HpicfMTUDropRouterAddr_Type())
hpicfMTUDropRouterAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropRouterAddr.setStatus(_B)
_HpicfMTUDropRouterMTU_Type=Integer32
_HpicfMTUDropRouterMTU_Object=MibScalar
hpicfMTUDropRouterMTU=_HpicfMTUDropRouterMTU_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,3),_HpicfMTUDropRouterMTU_Type())
hpicfMTUDropRouterMTU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropRouterMTU.setStatus(_B)
_HpicfMTUDropVTEPSrcAddrType_Type=InetAddressType
_HpicfMTUDropVTEPSrcAddrType_Object=MibScalar
hpicfMTUDropVTEPSrcAddrType=_HpicfMTUDropVTEPSrcAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,4),_HpicfMTUDropVTEPSrcAddrType_Type())
hpicfMTUDropVTEPSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropVTEPSrcAddrType.setStatus(_B)
_HpicfMTUDropVTEPSource_Type=InetAddress
_HpicfMTUDropVTEPSource_Object=MibScalar
hpicfMTUDropVTEPSource=_HpicfMTUDropVTEPSource_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,5),_HpicfMTUDropVTEPSource_Type())
hpicfMTUDropVTEPSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropVTEPSource.setStatus(_B)
_HpicfMTUDropVTEPDstAddrType_Type=InetAddressType
_HpicfMTUDropVTEPDstAddrType_Object=MibScalar
hpicfMTUDropVTEPDstAddrType=_HpicfMTUDropVTEPDstAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,6),_HpicfMTUDropVTEPDstAddrType_Type())
hpicfMTUDropVTEPDstAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropVTEPDstAddrType.setStatus(_B)
_HpicfMTUDropVTEPDest_Type=InetAddress
_HpicfMTUDropVTEPDest_Object=MibScalar
hpicfMTUDropVTEPDest=_HpicfMTUDropVTEPDest_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,7),_HpicfMTUDropVTEPDest_Type())
hpicfMTUDropVTEPDest.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropVTEPDest.setStatus(_B)
_HpicfMTUDropInIfIndex_Type=InterfaceIndex
_HpicfMTUDropInIfIndex_Object=MibScalar
hpicfMTUDropInIfIndex=_HpicfMTUDropInIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,8),_HpicfMTUDropInIfIndex_Type())
hpicfMTUDropInIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfMTUDropInIfIndex.setStatus(_B)
class _HpicfMTUDropNotifyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfMTUDropNotifyEnable_Type.__name__=_E
_HpicfMTUDropNotifyEnable_Object=MibScalar
hpicfMTUDropNotifyEnable=_HpicfMTUDropNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,1,3,9),_HpicfMTUDropNotifyEnable_Type())
hpicfMTUDropNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfMTUDropNotifyEnable.setStatus(_B)
_HpicfTunnelObjects_ObjectIdentity=ObjectIdentity
hpicfTunnelObjects=_HpicfTunnelObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,2))
_HpicfVXLANTunnelObjects_ObjectIdentity=ObjectIdentity
hpicfVXLANTunnelObjects=_HpicfVXLANTunnelObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1))
_HpicfVXLANTunnelConfigObjects_ObjectIdentity=ObjectIdentity
hpicfVXLANTunnelConfigObjects=_HpicfVXLANTunnelConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1))
_HpicfVXLANTunnelIfTable_Object=MibTable
hpicfVXLANTunnelIfTable=_HpicfVXLANTunnelIfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1))
if mibBuilder.loadTexts:hpicfVXLANTunnelIfTable.setStatus(_B)
_HpicfVXLANTunnelIfEntry_Object=MibTableRow
hpicfVXLANTunnelIfEntry=_HpicfVXLANTunnelIfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1))
if mibBuilder.loadTexts:hpicfVXLANTunnelIfEntry.setStatus(_B)
class _HpicfVXLANTunnelIfDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('ifAdminDown',1),('tepNotReachable',2),('resourceUnavailable',3)))
_HpicfVXLANTunnelIfDownReason_Type.__name__=_E
_HpicfVXLANTunnelIfDownReason_Object=MibTableColumn
hpicfVXLANTunnelIfDownReason=_HpicfVXLANTunnelIfDownReason_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,1),_HpicfVXLANTunnelIfDownReason_Type())
hpicfVXLANTunnelIfDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelIfDownReason.setStatus(_B)
_HpicfVXLANTunnelIfNextHopIpType_Type=InetAddressType
_HpicfVXLANTunnelIfNextHopIpType_Object=MibTableColumn
hpicfVXLANTunnelIfNextHopIpType=_HpicfVXLANTunnelIfNextHopIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,2),_HpicfVXLANTunnelIfNextHopIpType_Type())
hpicfVXLANTunnelIfNextHopIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelIfNextHopIpType.setStatus(_B)
_HpicfVXLANTunnelIfNextHopIp_Type=InetAddress
_HpicfVXLANTunnelIfNextHopIp_Object=MibTableColumn
hpicfVXLANTunnelIfNextHopIp=_HpicfVXLANTunnelIfNextHopIp_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,3),_HpicfVXLANTunnelIfNextHopIp_Type())
hpicfVXLANTunnelIfNextHopIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelIfNextHopIp.setStatus(_B)
_HpicfVXLANTunnelIfNextHopInterface_Type=DisplayString
_HpicfVXLANTunnelIfNextHopInterface_Object=MibTableColumn
hpicfVXLANTunnelIfNextHopInterface=_HpicfVXLANTunnelIfNextHopInterface_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,4),_HpicfVXLANTunnelIfNextHopInterface_Type())
hpicfVXLANTunnelIfNextHopInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelIfNextHopInterface.setStatus(_B)
_HpicfVXLANTunnelIfNextHopPortName_Type=DisplayString
_HpicfVXLANTunnelIfNextHopPortName_Object=MibTableColumn
hpicfVXLANTunnelIfNextHopPortName=_HpicfVXLANTunnelIfNextHopPortName_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,5),_HpicfVXLANTunnelIfNextHopPortName_Type())
hpicfVXLANTunnelIfNextHopPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelIfNextHopPortName.setStatus(_B)
_HpicfVXLANTunnelStatsRxPackets_Type=Counter64
_HpicfVXLANTunnelStatsRxPackets_Object=MibTableColumn
hpicfVXLANTunnelStatsRxPackets=_HpicfVXLANTunnelStatsRxPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,6),_HpicfVXLANTunnelStatsRxPackets_Type())
hpicfVXLANTunnelStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelStatsRxPackets.setStatus(_B)
_HpicfVXLANTunnelStatsTxPackets_Type=Counter32
_HpicfVXLANTunnelStatsTxPackets_Object=MibTableColumn
hpicfVXLANTunnelStatsTxPackets=_HpicfVXLANTunnelStatsTxPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,7),_HpicfVXLANTunnelStatsTxPackets_Type())
hpicfVXLANTunnelStatsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelStatsTxPackets.setStatus(_B)
_HpicfVXLANTunnelStatsClear_Type=TruthValue
_HpicfVXLANTunnelStatsClear_Object=MibTableColumn
hpicfVXLANTunnelStatsClear=_HpicfVXLANTunnelStatsClear_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,1,1,1,9),_HpicfVXLANTunnelStatsClear_Type())
hpicfVXLANTunnelStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVXLANTunnelStatsClear.setStatus(_B)
_HpicfVXLANTunnelScalars_ObjectIdentity=ObjectIdentity
hpicfVXLANTunnelScalars=_HpicfVXLANTunnelScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2))
_HpicfMaxVXLANTunnels_Type=Unsigned32
_HpicfMaxVXLANTunnels_Object=MibScalar
hpicfMaxVXLANTunnels=_HpicfMaxVXLANTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,1),_HpicfMaxVXLANTunnels_Type())
hpicfMaxVXLANTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfMaxVXLANTunnels.setStatus(_B)
_HpicfTotalVXLANTunnels_Type=Unsigned32
_HpicfTotalVXLANTunnels_Object=MibScalar
hpicfTotalVXLANTunnels=_HpicfTotalVXLANTunnels_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,2),_HpicfTotalVXLANTunnels_Type())
hpicfTotalVXLANTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfTotalVXLANTunnels.setStatus(_B)
_HpicfVXLANTunnelStatsTxMTUViolation_Type=Counter32
_HpicfVXLANTunnelStatsTxMTUViolation_Object=MibScalar
hpicfVXLANTunnelStatsTxMTUViolation=_HpicfVXLANTunnelStatsTxMTUViolation_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,3),_HpicfVXLANTunnelStatsTxMTUViolation_Type())
hpicfVXLANTunnelStatsTxMTUViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelStatsTxMTUViolation.setStatus(_B)
_HpicfVXLANTunnelGlobalStatsDropCount_Type=Counter64
_HpicfVXLANTunnelGlobalStatsDropCount_Object=MibScalar
hpicfVXLANTunnelGlobalStatsDropCount=_HpicfVXLANTunnelGlobalStatsDropCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,4),_HpicfVXLANTunnelGlobalStatsDropCount_Type())
hpicfVXLANTunnelGlobalStatsDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfVXLANTunnelGlobalStatsDropCount.setStatus(_B)
_HpicfVXLANTunnelGlobalStatsClear_Type=TruthValue
_HpicfVXLANTunnelGlobalStatsClear_Object=MibScalar
hpicfVXLANTunnelGlobalStatsClear=_HpicfVXLANTunnelGlobalStatsClear_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,5),_HpicfVXLANTunnelGlobalStatsClear_Type())
hpicfVXLANTunnelGlobalStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVXLANTunnelGlobalStatsClear.setStatus(_B)
class _HpicfVXLANTunnelEnable_Type(TruthValue):defaultValue=2
_HpicfVXLANTunnelEnable_Type.__name__=_Q
_HpicfVXLANTunnelEnable_Object=MibScalar
hpicfVXLANTunnelEnable=_HpicfVXLANTunnelEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,6),_HpicfVXLANTunnelEnable_Type())
hpicfVXLANTunnelEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVXLANTunnelEnable.setStatus(_B)
class _HpicfVXLANTunnelUDPPort_Type(Integer32):defaultValue=4789;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfVXLANTunnelUDPPort_Type.__name__=_E
_HpicfVXLANTunnelUDPPort_Object=MibScalar
hpicfVXLANTunnelUDPPort=_HpicfVXLANTunnelUDPPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,107,2,1,2,7),_HpicfVXLANTunnelUDPPort_Type())
hpicfVXLANTunnelUDPPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfVXLANTunnelUDPPort.setStatus(_B)
_HpicfVirtualNetworkConformance_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkConformance=_HpicfVirtualNetworkConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,3))
_HpicfVirtualNetworkCompliances_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkCompliances=_HpicfVirtualNetworkCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,3,1))
_HpicfVirtualNetworkGroups_ObjectIdentity=ObjectIdentity
hpicfVirtualNetworkGroups=_HpicfVirtualNetworkGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2))
tunnelIfEntry.registerAugmentions((_A,_V))
hpicfVXLANTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
hpicfVirtualNetworkGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2,1))
hpicfVirtualNetworkGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hpicfVirtualNetworkGroup.setStatus(_B)
hpicfVirtualNetworkScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2,2))
hpicfVirtualNetworkScalarGroup.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpicfVirtualNetworkScalarGroup.setStatus(_B)
hpicfVXLANTunnelStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2,3))
hpicfVXLANTunnelStatsGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:hpicfVXLANTunnelStatsGroup.setStatus(_B)
hpicfVXLANTunnelScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2,4))
hpicfVXLANTunnelScalarGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:hpicfVXLANTunnelScalarGroup.setStatus(_B)
hpicfVirtualNetworkNotifyScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2,5))
hpicfVirtualNetworkNotifyScalarsGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_q)))
if mibBuilder.loadTexts:hpicfVirtualNetworkNotifyScalarsGroup.setStatus(_B)
hpicfVirtualNetworkIcmpErrorRcvd=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,107,0,1))
hpicfVirtualNetworkIcmpErrorRcvd.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_G,_R),(_G,_S),(_G,_T)))
if mibBuilder.loadTexts:hpicfVirtualNetworkIcmpErrorRcvd.setStatus(_B)
hpicfVirtualNetworkNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,107,3,2,6))
hpicfVirtualNetworkNotificationsGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:hpicfVirtualNetworkNotificationsGroup.setStatus(_B)
hpicfVirtualNetworkCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,107,3,1,1))
hpicfVirtualNetworkCompliance.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:hpicfVirtualNetworkCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfVirtualNetwork':hpicfVirtualNetwork,'hpicfVirtualNetworkNotifications':hpicfVirtualNetworkNotifications,_r:hpicfVirtualNetworkIcmpErrorRcvd,'hpicfVirtualNetworkObjects':hpicfVirtualNetworkObjects,'hpicfVirtualNetworkScalars':hpicfVirtualNetworkScalars,_Z:hpicfMaxVirtualNetworks,_a:hpicfTotalVirtualNetworks,'hpicfVirtualNetworkTable':hpicfVirtualNetworkTable,'hpicfVirtualNetworkEntry':hpicfVirtualNetworkEntry,_U:hpicfVirtualNetworkID,_W:hpicfVirtualNetworkName,_X:hpicfVirtualNetworkVLANID,_Y:hpicfVirtualNetworkRowStatus,'hpicfVirtualNetworkNotifyScalars':hpicfVirtualNetworkNotifyScalars,_I:hpicfMTUDropRouterAddrType,_J:hpicfMTUDropRouterAddr,_K:hpicfMTUDropRouterMTU,_L:hpicfMTUDropVTEPSrcAddrType,_M:hpicfMTUDropVTEPSource,_N:hpicfMTUDropVTEPDstAddrType,_O:hpicfMTUDropVTEPDest,_P:hpicfMTUDropInIfIndex,_q:hpicfMTUDropNotifyEnable,'hpicfTunnelObjects':hpicfTunnelObjects,'hpicfVXLANTunnelObjects':hpicfVXLANTunnelObjects,'hpicfVXLANTunnelConfigObjects':hpicfVXLANTunnelConfigObjects,'hpicfVXLANTunnelIfTable':hpicfVXLANTunnelIfTable,_V:hpicfVXLANTunnelIfEntry,_b:hpicfVXLANTunnelIfDownReason,_c:hpicfVXLANTunnelIfNextHopIpType,_d:hpicfVXLANTunnelIfNextHopIp,_e:hpicfVXLANTunnelIfNextHopInterface,_f:hpicfVXLANTunnelIfNextHopPortName,_g:hpicfVXLANTunnelStatsRxPackets,_h:hpicfVXLANTunnelStatsTxPackets,_i:hpicfVXLANTunnelStatsClear,'hpicfVXLANTunnelScalars':hpicfVXLANTunnelScalars,_j:hpicfMaxVXLANTunnels,_k:hpicfTotalVXLANTunnels,_l:hpicfVXLANTunnelStatsTxMTUViolation,_m:hpicfVXLANTunnelGlobalStatsDropCount,_n:hpicfVXLANTunnelGlobalStatsClear,_o:hpicfVXLANTunnelEnable,_p:hpicfVXLANTunnelUDPPort,'hpicfVirtualNetworkConformance':hpicfVirtualNetworkConformance,'hpicfVirtualNetworkCompliances':hpicfVirtualNetworkCompliances,'hpicfVirtualNetworkCompliance':hpicfVirtualNetworkCompliance,'hpicfVirtualNetworkGroups':hpicfVirtualNetworkGroups,_s:hpicfVirtualNetworkGroup,_t:hpicfVirtualNetworkScalarGroup,_u:hpicfVXLANTunnelStatsGroup,_v:hpicfVXLANTunnelScalarGroup,_w:hpicfVirtualNetworkNotifyScalarsGroup,_x:hpicfVirtualNetworkNotificationsGroup})