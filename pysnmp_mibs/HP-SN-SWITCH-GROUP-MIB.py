_AV='snFdpCachedAddrDeviceAddrEntryIndex'
_AU='snFdpCachedAddrDeviceIndex'
_AT='snFdpCachedAddrIfIndex'
_AS='appletalk'
_AR='snFdpCacheDeviceIndex'
_AQ='snFdpCacheIfIndex'
_AP='snFdpInterfaceIfIndex'
_AO='snSflowCollectorIndex'
_AN='snNetFlowIfIndex'
_AM='snNetFlowAggregationIndex'
_AL='snNetFlowCollectorIndex'
_AK='snQosBindIndex'
_AJ='snQosProfileIndex'
_AI='snTacacsServerIp'
_AH='accounting-only'
_AG='authorization-only'
_AF='authentication-only'
_AE='snRadiusServerIp'
_AD='snNTPServerIp'
_AC='snMacFilterPortAccessPortIndex'
_AB='snMacFilterIndex'
_AA='snDhcpGatewayListId'
_A9='snMSTrunkPortIndex'
_A8='snTrunkIndex'
_A7='snPortStpPortNum'
_A6='snPortStpVLanId'
_A5='snFdbStationIndex'
_A4='snIfIndexLookupIfIndex'
_A3='snInterfaceLookupInterfaceId'
_A2='m1000BaseTX'
_A1='snSwPortInfoPortNum'
_A0='snVLanByPortCfgVLanId'
_z='snVLanByPortMemberPortId'
_y='snVLanByPortMemberVLanId'
_x='snVLanByATCableIndex'
_w='snVLanByATCableVLanId'
_v='notApplicable'
_u='snVLanByIpxNetFrameType'
_t='snVLanByIpxNetNetworkNum'
_s='snVLanByIpxNetVLanId'
_r='snVLanByIpSubnetSubnetMask'
_q='snVLanByIpSubnetIpAddress'
_p='snVLanByIpSubnetVLanId'
_o='snVLanByProtocolIndex'
_n='snVLanByProtocolVLanId'
_m='ieee8021d'
_l='decLb100'
_k='sourceroute-only'
_j='transparent-only'
_i='activated'
_h='notActivated'
_g='snVLanByPortVLanIndex'
_f='negFullAuto'
_e='PhysAddress'
_d='invalid'
_c='ipx'
_b='default'
_a='unknown'
_Z='level7'
_Y='level6'
_X='level3'
_W='level2'
_V='level1'
_U='true'
_T='false'
_S='level5'
_R='level4'
_Q='level0'
_P='not-accessible'
_O='modify'
_N='DisplayString'
_M='create'
_L='delete'
_K='valid'
_J='other'
_I='OctetString'
_H='enabled'
_G='disabled'
_F='HP-SN-SWITCH-GROUP-MIB'
_E='deprecated'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('HP-SN-ROOT-MIB','snSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,_e,'TextualConvention')
class DisplayString(OctetString):0
class PhysAddress(OctetString):0
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(Integer32):0
class PortMask(Integer32):0
class InterfaceId(ObjectIdentifier):0
_SnSwInfo_ObjectIdentity=ObjectIdentity
snSwInfo=_SnSwInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1))
class _SnSwGroupOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noVLan',1),('vlanByPort',2)))
_SnSwGroupOperMode_Type.__name__=_C
_SnSwGroupOperMode_Object=MibScalar
snSwGroupOperMode=_SnSwGroupOperMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,1),_SnSwGroupOperMode_Type())
snSwGroupOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGroupOperMode.setStatus(_A)
class _SnSwGroupIpL3SwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwGroupIpL3SwMode_Type.__name__=_C
_SnSwGroupIpL3SwMode_Object=MibScalar
snSwGroupIpL3SwMode=_SnSwGroupIpL3SwMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,2),_SnSwGroupIpL3SwMode_Type())
snSwGroupIpL3SwMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGroupIpL3SwMode.setStatus(_A)
class _SnSwGroupIpMcastMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwGroupIpMcastMode_Type.__name__=_C
_SnSwGroupIpMcastMode_Object=MibScalar
snSwGroupIpMcastMode=_SnSwGroupIpMcastMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,3),_SnSwGroupIpMcastMode_Type())
snSwGroupIpMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGroupIpMcastMode.setStatus(_A)
class _SnSwGroupDefaultCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),('nonDefault',2)))
_SnSwGroupDefaultCfgMode_Type.__name__=_C
_SnSwGroupDefaultCfgMode_Object=MibScalar
snSwGroupDefaultCfgMode=_SnSwGroupDefaultCfgMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,4),_SnSwGroupDefaultCfgMode_Type())
snSwGroupDefaultCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGroupDefaultCfgMode.setStatus(_A)
_SnSwGroupSwitchAgeTime_Type=Integer32
_SnSwGroupSwitchAgeTime_Object=MibScalar
snSwGroupSwitchAgeTime=_SnSwGroupSwitchAgeTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,5),_SnSwGroupSwitchAgeTime_Type())
snSwGroupSwitchAgeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGroupSwitchAgeTime.setStatus(_A)
_SnVLanGroupVlanCurEntry_Type=Integer32
_SnVLanGroupVlanCurEntry_Object=MibScalar
snVLanGroupVlanCurEntry=_SnVLanGroupVlanCurEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,6),_SnVLanGroupVlanCurEntry_Type())
snVLanGroupVlanCurEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanGroupVlanCurEntry.setStatus(_A)
_SnVLanGroupSetAllVLan_Type=Integer32
_SnVLanGroupSetAllVLan_Object=MibScalar
snVLanGroupSetAllVLan=_SnVLanGroupSetAllVLan_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,7),_SnVLanGroupSetAllVLan_Type())
snVLanGroupSetAllVLan.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanGroupSetAllVLan.setStatus(_A)
_SnSwPortSetAll_Type=Integer32
_SnSwPortSetAll_Object=MibScalar
snSwPortSetAll=_SnSwPortSetAll_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,8),_SnSwPortSetAll_Type())
snSwPortSetAll.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortSetAll.setStatus(_A)
_SnFdbTableCurEntry_Type=Integer32
_SnFdbTableCurEntry_Object=MibScalar
snFdbTableCurEntry=_SnFdbTableCurEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,9),_SnFdbTableCurEntry_Type())
snFdbTableCurEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdbTableCurEntry.setStatus(_A)
class _SnFdbTableStationFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('error',2),('flush',3),('flushing',4)))
_SnFdbTableStationFlush_Type.__name__=_C
_SnFdbTableStationFlush_Object=MibScalar
snFdbTableStationFlush=_SnFdbTableStationFlush_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,10),_SnFdbTableStationFlush_Type())
snFdbTableStationFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbTableStationFlush.setStatus(_A)
_SnPortStpSetAll_Type=Integer32
_SnPortStpSetAll_Object=MibScalar
snPortStpSetAll=_SnPortStpSetAll_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,11),_SnPortStpSetAll_Type())
snPortStpSetAll.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortStpSetAll.setStatus(_A)
_SnSwProbePortNum_Type=Integer32
_SnSwProbePortNum_Object=MibScalar
snSwProbePortNum=_SnSwProbePortNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,12),_SnSwProbePortNum_Type())
snSwProbePortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwProbePortNum.setStatus(_A)
class _SnSw8021qTagMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSw8021qTagMode_Type.__name__=_C
_SnSw8021qTagMode_Object=MibScalar
snSw8021qTagMode=_SnSw8021qTagMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,13),_SnSw8021qTagMode_Type())
snSw8021qTagMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSw8021qTagMode.setStatus(_A)
class _SnSwGlobalStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwGlobalStpMode_Type.__name__=_C
_SnSwGlobalStpMode_Object=MibScalar
snSwGlobalStpMode=_SnSwGlobalStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,14),_SnSwGlobalStpMode_Type())
snSwGlobalStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGlobalStpMode.setStatus(_A)
class _SnSwIpMcastQuerierMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('querier',1),('nonQuerier',2)))
_SnSwIpMcastQuerierMode_Type.__name__=_C
_SnSwIpMcastQuerierMode_Object=MibScalar
snSwIpMcastQuerierMode=_SnSwIpMcastQuerierMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,15),_SnSwIpMcastQuerierMode_Type())
snSwIpMcastQuerierMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwIpMcastQuerierMode.setStatus(_A)
_SnSwViolatorPortNumber_Type=Integer32
_SnSwViolatorPortNumber_Object=MibScalar
snSwViolatorPortNumber=_SnSwViolatorPortNumber_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,17),_SnSwViolatorPortNumber_Type())
snSwViolatorPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwViolatorPortNumber.setStatus(_A)
_SnSwViolatorMacAddress_Type=MacAddress
_SnSwViolatorMacAddress_Object=MibScalar
snSwViolatorMacAddress=_SnSwViolatorMacAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,18),_SnSwViolatorMacAddress_Type())
snSwViolatorMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwViolatorMacAddress.setStatus(_A)
_SnVLanGroupVlanMaxEntry_Type=Integer32
_SnVLanGroupVlanMaxEntry_Object=MibScalar
snVLanGroupVlanMaxEntry=_SnVLanGroupVlanMaxEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,19),_SnVLanGroupVlanMaxEntry_Type())
snVLanGroupVlanMaxEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanGroupVlanMaxEntry.setStatus(_A)
_SnSwEosBufferSize_Type=Integer32
_SnSwEosBufferSize_Object=MibScalar
snSwEosBufferSize=_SnSwEosBufferSize_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,20),_SnSwEosBufferSize_Type())
snSwEosBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwEosBufferSize.setStatus(_A)
_SnVLanByPortEntrySize_Type=Integer32
_SnVLanByPortEntrySize_Object=MibScalar
snVLanByPortEntrySize=_SnVLanByPortEntrySize_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,21),_SnVLanByPortEntrySize_Type())
snVLanByPortEntrySize.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortEntrySize.setStatus(_A)
_SnSwPortEntrySize_Type=Integer32
_SnSwPortEntrySize_Object=MibScalar
snSwPortEntrySize=_SnSwPortEntrySize_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,22),_SnSwPortEntrySize_Type())
snSwPortEntrySize.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortEntrySize.setStatus(_A)
_SnFdbStationEntrySize_Type=Integer32
_SnFdbStationEntrySize_Object=MibScalar
snFdbStationEntrySize=_SnFdbStationEntrySize_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,23),_SnFdbStationEntrySize_Type())
snFdbStationEntrySize.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdbStationEntrySize.setStatus(_A)
_SnPortStpEntrySize_Type=Integer32
_SnPortStpEntrySize_Object=MibScalar
snPortStpEntrySize=_SnPortStpEntrySize_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,24),_SnPortStpEntrySize_Type())
snPortStpEntrySize.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpEntrySize.setStatus(_A)
class _SnSwEnableBridgeNewRootTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwEnableBridgeNewRootTrap_Type.__name__=_C
_SnSwEnableBridgeNewRootTrap_Object=MibScalar
snSwEnableBridgeNewRootTrap=_SnSwEnableBridgeNewRootTrap_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,25),_SnSwEnableBridgeNewRootTrap_Type())
snSwEnableBridgeNewRootTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwEnableBridgeNewRootTrap.setStatus(_A)
class _SnSwEnableBridgeTopoChangeTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwEnableBridgeTopoChangeTrap_Type.__name__=_C
_SnSwEnableBridgeTopoChangeTrap_Object=MibScalar
snSwEnableBridgeTopoChangeTrap=_SnSwEnableBridgeTopoChangeTrap_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,26),_SnSwEnableBridgeTopoChangeTrap_Type())
snSwEnableBridgeTopoChangeTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwEnableBridgeTopoChangeTrap.setStatus(_A)
class _SnSwEnableLockedAddrViolationTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwEnableLockedAddrViolationTrap_Type.__name__=_C
_SnSwEnableLockedAddrViolationTrap_Object=MibScalar
snSwEnableLockedAddrViolationTrap=_SnSwEnableLockedAddrViolationTrap_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,27),_SnSwEnableLockedAddrViolationTrap_Type())
snSwEnableLockedAddrViolationTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwEnableLockedAddrViolationTrap.setStatus(_A)
class _SnSwIpxL3SwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwIpxL3SwMode_Type.__name__=_C
_SnSwIpxL3SwMode_Object=MibScalar
snSwIpxL3SwMode=_SnSwIpxL3SwMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,28),_SnSwIpxL3SwMode_Type())
snSwIpxL3SwMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwIpxL3SwMode.setStatus(_A)
_SnVLanByIpSubnetMaxSubnets_Type=Integer32
_SnVLanByIpSubnetMaxSubnets_Object=MibScalar
snVLanByIpSubnetMaxSubnets=_SnVLanByIpSubnetMaxSubnets_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,29),_SnVLanByIpSubnetMaxSubnets_Type())
snVLanByIpSubnetMaxSubnets.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetMaxSubnets.setStatus(_A)
_SnVLanByIpxNetMaxNetworks_Type=Integer32
_SnVLanByIpxNetMaxNetworks_Object=MibScalar
snVLanByIpxNetMaxNetworks=_SnVLanByIpxNetMaxNetworks_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,30),_SnVLanByIpxNetMaxNetworks_Type())
snVLanByIpxNetMaxNetworks.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetMaxNetworks.setStatus(_A)
class _SnSwProtocolVLanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwProtocolVLanMode_Type.__name__=_C
_SnSwProtocolVLanMode_Object=MibScalar
snSwProtocolVLanMode=_SnSwProtocolVLanMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,31),_SnSwProtocolVLanMode_Type())
snSwProtocolVLanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwProtocolVLanMode.setStatus(_A)
class _SnMacStationVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnMacStationVLanId_Type.__name__=_C
_SnMacStationVLanId_Object=MibScalar
snMacStationVLanId=_SnMacStationVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,32),_SnMacStationVLanId_Type())
snMacStationVLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacStationVLanId.setStatus(_A)
class _SnSwClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('clear',1)))
_SnSwClearCounters_Type.__name__=_C
_SnSwClearCounters_Object=MibScalar
snSwClearCounters=_SnSwClearCounters_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,33),_SnSwClearCounters_Type())
snSwClearCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwClearCounters.setStatus(_A)
class _SnSw8021qTagType_Type(Integer32):defaultValue=33024
_SnSw8021qTagType_Type.__name__=_C
_SnSw8021qTagType_Object=MibScalar
snSw8021qTagType=_SnSw8021qTagType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,34),_SnSw8021qTagType_Type())
snSw8021qTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:snSw8021qTagType.setStatus(_A)
class _SnSwBroadcastLimit_Type(Integer32):defaultValue=0
_SnSwBroadcastLimit_Type.__name__=_C
_SnSwBroadcastLimit_Object=MibScalar
snSwBroadcastLimit=_SnSwBroadcastLimit_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,35),_SnSwBroadcastLimit_Type())
snSwBroadcastLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwBroadcastLimit.setStatus(_A)
_SnSwMaxMacFilterPerSystem_Type=Integer32
_SnSwMaxMacFilterPerSystem_Object=MibScalar
snSwMaxMacFilterPerSystem=_SnSwMaxMacFilterPerSystem_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,36),_SnSwMaxMacFilterPerSystem_Type())
snSwMaxMacFilterPerSystem.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwMaxMacFilterPerSystem.setStatus(_A)
_SnSwMaxMacFilterPerPort_Type=Integer32
_SnSwMaxMacFilterPerPort_Object=MibScalar
snSwMaxMacFilterPerPort=_SnSwMaxMacFilterPerPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,37),_SnSwMaxMacFilterPerPort_Type())
snSwMaxMacFilterPerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwMaxMacFilterPerPort.setStatus(_A)
class _SnSwDefaultVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnSwDefaultVLanId_Type.__name__=_C
_SnSwDefaultVLanId_Object=MibScalar
snSwDefaultVLanId=_SnSwDefaultVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,38),_SnSwDefaultVLanId_Type())
snSwDefaultVLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwDefaultVLanId.setStatus(_A)
class _SnSwGlobalAutoNegotiate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_f,2),(_J,3)))
_SnSwGlobalAutoNegotiate_Type.__name__=_C
_SnSwGlobalAutoNegotiate_Object=MibScalar
snSwGlobalAutoNegotiate=_SnSwGlobalAutoNegotiate_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,39),_SnSwGlobalAutoNegotiate_Type())
snSwGlobalAutoNegotiate.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwGlobalAutoNegotiate.setStatus(_A)
class _SnSwQosMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('strict',0),('weighted',1)))
_SnSwQosMechanism_Type.__name__=_C
_SnSwQosMechanism_Object=MibScalar
snSwQosMechanism=_SnSwQosMechanism_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,40),_SnSwQosMechanism_Type())
snSwQosMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwQosMechanism.setStatus(_A)
class _SnSwSingleStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwSingleStpMode_Type.__name__=_C
_SnSwSingleStpMode_Object=MibScalar
snSwSingleStpMode=_SnSwSingleStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,41),_SnSwSingleStpMode_Type())
snSwSingleStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwSingleStpMode.setStatus(_A)
class _SnSwFastStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwFastStpMode_Type.__name__=_C
_SnSwFastStpMode_Object=MibScalar
snSwFastStpMode=_SnSwFastStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,1,42),_SnSwFastStpMode_Type())
snSwFastStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwFastStpMode.setStatus(_A)
_SnVLanInfo_ObjectIdentity=ObjectIdentity
snVLanInfo=_SnVLanInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2))
_SnVLanByPortTable_Object=MibTable
snVLanByPortTable=_SnVLanByPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1))
if mibBuilder.loadTexts:snVLanByPortTable.setStatus(_E)
_SnVLanByPortEntry_Object=MibTableRow
snVLanByPortEntry=_SnVLanByPortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1))
snVLanByPortEntry.setIndexNames((0,_F,_g))
if mibBuilder.loadTexts:snVLanByPortEntry.setStatus(_E)
class _SnVLanByPortVLanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByPortVLanIndex_Type.__name__=_C
_SnVLanByPortVLanIndex_Object=MibTableColumn
snVLanByPortVLanIndex=_SnVLanByPortVLanIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,1),_SnVLanByPortVLanIndex_Type())
snVLanByPortVLanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortVLanIndex.setStatus(_E)
class _SnVLanByPortVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByPortVLanId_Type.__name__=_C
_SnVLanByPortVLanId_Object=MibTableColumn
snVLanByPortVLanId=_SnVLanByPortVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,2),_SnVLanByPortVLanId_Type())
snVLanByPortVLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortVLanId.setStatus(_E)
_SnVLanByPortPortMask_Type=PortMask
_SnVLanByPortPortMask_Object=MibTableColumn
snVLanByPortPortMask=_SnVLanByPortPortMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,3),_SnVLanByPortPortMask_Type())
snVLanByPortPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortPortMask.setStatus(_E)
class _SnVLanByPortQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,0),(_V,1),(_W,2),(_X,3),(_R,4),(_S,5),(_Y,6),(_Z,7)))
_SnVLanByPortQos_Type.__name__=_C
_SnVLanByPortQos_Object=MibTableColumn
snVLanByPortQos=_SnVLanByPortQos_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,4),_SnVLanByPortQos_Type())
snVLanByPortQos.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortQos.setStatus(_E)
class _SnVLanByPortStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnVLanByPortStpMode_Type.__name__=_C
_SnVLanByPortStpMode_Object=MibTableColumn
snVLanByPortStpMode=_SnVLanByPortStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,5),_SnVLanByPortStpMode_Type())
snVLanByPortStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortStpMode.setStatus(_E)
class _SnVLanByPortStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnVLanByPortStpPriority_Type.__name__=_C
_SnVLanByPortStpPriority_Object=MibTableColumn
snVLanByPortStpPriority=_SnVLanByPortStpPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,6),_SnVLanByPortStpPriority_Type())
snVLanByPortStpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortStpPriority.setStatus(_E)
class _SnVLanByPortStpGroupMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_SnVLanByPortStpGroupMaxAge_Type.__name__=_C
_SnVLanByPortStpGroupMaxAge_Object=MibTableColumn
snVLanByPortStpGroupMaxAge=_SnVLanByPortStpGroupMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,7),_SnVLanByPortStpGroupMaxAge_Type())
snVLanByPortStpGroupMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortStpGroupMaxAge.setStatus(_E)
class _SnVLanByPortStpGroupHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SnVLanByPortStpGroupHelloTime_Type.__name__=_C
_SnVLanByPortStpGroupHelloTime_Object=MibTableColumn
snVLanByPortStpGroupHelloTime=_SnVLanByPortStpGroupHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,8),_SnVLanByPortStpGroupHelloTime_Type())
snVLanByPortStpGroupHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortStpGroupHelloTime.setStatus(_E)
class _SnVLanByPortStpGroupForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_SnVLanByPortStpGroupForwardDelay_Type.__name__=_C
_SnVLanByPortStpGroupForwardDelay_Object=MibTableColumn
snVLanByPortStpGroupForwardDelay=_SnVLanByPortStpGroupForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,9),_SnVLanByPortStpGroupForwardDelay_Type())
snVLanByPortStpGroupForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortStpGroupForwardDelay.setStatus(_E)
class _SnVLanByPortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnVLanByPortRowStatus_Type.__name__=_C
_SnVLanByPortRowStatus_Object=MibTableColumn
snVLanByPortRowStatus=_SnVLanByPortRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,10),_SnVLanByPortRowStatus_Type())
snVLanByPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortRowStatus.setStatus(_E)
class _SnVLanByPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_SnVLanByPortOperState_Type.__name__=_C
_SnVLanByPortOperState_Object=MibTableColumn
snVLanByPortOperState=_SnVLanByPortOperState_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,11),_SnVLanByPortOperState_Type())
snVLanByPortOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortOperState.setStatus(_E)
_SnVLanByPortBaseNumPorts_Type=Integer32
_SnVLanByPortBaseNumPorts_Object=MibTableColumn
snVLanByPortBaseNumPorts=_SnVLanByPortBaseNumPorts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,12),_SnVLanByPortBaseNumPorts_Type())
snVLanByPortBaseNumPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortBaseNumPorts.setStatus(_E)
class _SnVLanByPortBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_j,2),(_k,3),('srt',4)))
_SnVLanByPortBaseType_Type.__name__=_C
_SnVLanByPortBaseType_Object=MibTableColumn
snVLanByPortBaseType=_SnVLanByPortBaseType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,13),_SnVLanByPortBaseType_Type())
snVLanByPortBaseType.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortBaseType.setStatus(_E)
class _SnVLanByPortStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_l,2),(_m,3)))
_SnVLanByPortStpProtocolSpecification_Type.__name__=_C
_SnVLanByPortStpProtocolSpecification_Object=MibTableColumn
snVLanByPortStpProtocolSpecification=_SnVLanByPortStpProtocolSpecification_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,14),_SnVLanByPortStpProtocolSpecification_Type())
snVLanByPortStpProtocolSpecification.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpProtocolSpecification.setStatus(_E)
_SnVLanByPortStpMaxAge_Type=Timeout
_SnVLanByPortStpMaxAge_Object=MibTableColumn
snVLanByPortStpMaxAge=_SnVLanByPortStpMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,15),_SnVLanByPortStpMaxAge_Type())
snVLanByPortStpMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpMaxAge.setStatus(_E)
_SnVLanByPortStpHelloTime_Type=Timeout
_SnVLanByPortStpHelloTime_Object=MibTableColumn
snVLanByPortStpHelloTime=_SnVLanByPortStpHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,16),_SnVLanByPortStpHelloTime_Type())
snVLanByPortStpHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpHelloTime.setStatus(_E)
_SnVLanByPortStpHoldTime_Type=Integer32
_SnVLanByPortStpHoldTime_Object=MibTableColumn
snVLanByPortStpHoldTime=_SnVLanByPortStpHoldTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,17),_SnVLanByPortStpHoldTime_Type())
snVLanByPortStpHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpHoldTime.setStatus(_E)
_SnVLanByPortStpForwardDelay_Type=Timeout
_SnVLanByPortStpForwardDelay_Object=MibTableColumn
snVLanByPortStpForwardDelay=_SnVLanByPortStpForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,18),_SnVLanByPortStpForwardDelay_Type())
snVLanByPortStpForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpForwardDelay.setStatus(_E)
_SnVLanByPortStpTimeSinceTopologyChange_Type=TimeTicks
_SnVLanByPortStpTimeSinceTopologyChange_Object=MibTableColumn
snVLanByPortStpTimeSinceTopologyChange=_SnVLanByPortStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,19),_SnVLanByPortStpTimeSinceTopologyChange_Type())
snVLanByPortStpTimeSinceTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpTimeSinceTopologyChange.setStatus(_E)
_SnVLanByPortStpTopChanges_Type=Counter32
_SnVLanByPortStpTopChanges_Object=MibTableColumn
snVLanByPortStpTopChanges=_SnVLanByPortStpTopChanges_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,20),_SnVLanByPortStpTopChanges_Type())
snVLanByPortStpTopChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpTopChanges.setStatus(_E)
_SnVLanByPortStpRootCost_Type=Integer32
_SnVLanByPortStpRootCost_Object=MibTableColumn
snVLanByPortStpRootCost=_SnVLanByPortStpRootCost_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,21),_SnVLanByPortStpRootCost_Type())
snVLanByPortStpRootCost.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpRootCost.setStatus(_E)
_SnVLanByPortStpRootPort_Type=Integer32
_SnVLanByPortStpRootPort_Object=MibTableColumn
snVLanByPortStpRootPort=_SnVLanByPortStpRootPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,22),_SnVLanByPortStpRootPort_Type())
snVLanByPortStpRootPort.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpRootPort.setStatus(_E)
_SnVLanByPortStpDesignatedRoot_Type=BridgeId
_SnVLanByPortStpDesignatedRoot_Object=MibTableColumn
snVLanByPortStpDesignatedRoot=_SnVLanByPortStpDesignatedRoot_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,23),_SnVLanByPortStpDesignatedRoot_Type())
snVLanByPortStpDesignatedRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortStpDesignatedRoot.setStatus(_E)
_SnVLanByPortBaseBridgeAddress_Type=MacAddress
_SnVLanByPortBaseBridgeAddress_Object=MibTableColumn
snVLanByPortBaseBridgeAddress=_SnVLanByPortBaseBridgeAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,24),_SnVLanByPortBaseBridgeAddress_Type())
snVLanByPortBaseBridgeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortBaseBridgeAddress.setStatus(_E)
class _SnVLanByPortVLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnVLanByPortVLanName_Type.__name__=_N
_SnVLanByPortVLanName_Object=MibTableColumn
snVLanByPortVLanName=_SnVLanByPortVLanName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,25),_SnVLanByPortVLanName_Type())
snVLanByPortVLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortVLanName.setStatus(_E)
class _SnVLanByPortRouterIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SnVLanByPortRouterIntf_Type.__name__=_C
_SnVLanByPortRouterIntf_Object=MibTableColumn
snVLanByPortRouterIntf=_SnVLanByPortRouterIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,26),_SnVLanByPortRouterIntf_Type())
snVLanByPortRouterIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortRouterIntf.setStatus(_E)
class _SnVLanByPortChassisPortMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByPortChassisPortMask_Type.__name__=_I
_SnVLanByPortChassisPortMask_Object=MibTableColumn
snVLanByPortChassisPortMask=_SnVLanByPortChassisPortMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,27),_SnVLanByPortChassisPortMask_Type())
snVLanByPortChassisPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortChassisPortMask.setStatus(_E)
_SnVLanByPortPortList_Type=OctetString
_SnVLanByPortPortList_Object=MibTableColumn
snVLanByPortPortList=_SnVLanByPortPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,1,1,28),_SnVLanByPortPortList_Type())
snVLanByPortPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortPortList.setStatus(_E)
_SnVLanByProtocolTable_Object=MibTable
snVLanByProtocolTable=_SnVLanByProtocolTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2))
if mibBuilder.loadTexts:snVLanByProtocolTable.setStatus(_A)
_SnVLanByProtocolEntry_Object=MibTableRow
snVLanByProtocolEntry=_SnVLanByProtocolEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1))
snVLanByProtocolEntry.setIndexNames((0,_F,_n),(0,_F,_o))
if mibBuilder.loadTexts:snVLanByProtocolEntry.setStatus(_A)
class _SnVLanByProtocolVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByProtocolVLanId_Type.__name__=_C
_SnVLanByProtocolVLanId_Object=MibTableColumn
snVLanByProtocolVLanId=_SnVLanByProtocolVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,1),_SnVLanByProtocolVLanId_Type())
snVLanByProtocolVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByProtocolVLanId.setStatus(_A)
class _SnVLanByProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ip',1),(_c,2),('appleTalk',3),('decNet',4),('netBios',5),('others',6),('ipv6',7)))
_SnVLanByProtocolIndex_Type.__name__=_C
_SnVLanByProtocolIndex_Object=MibTableColumn
snVLanByProtocolIndex=_SnVLanByProtocolIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,2),_SnVLanByProtocolIndex_Type())
snVLanByProtocolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByProtocolIndex.setStatus(_A)
class _SnVLanByProtocolDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnVLanByProtocolDynamic_Type.__name__=_C
_SnVLanByProtocolDynamic_Object=MibTableColumn
snVLanByProtocolDynamic=_SnVLanByProtocolDynamic_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,3),_SnVLanByProtocolDynamic_Type())
snVLanByProtocolDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolDynamic.setStatus(_A)
_SnVLanByProtocolStaticMask_Type=PortMask
_SnVLanByProtocolStaticMask_Object=MibTableColumn
snVLanByProtocolStaticMask=_SnVLanByProtocolStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,4),_SnVLanByProtocolStaticMask_Type())
snVLanByProtocolStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolStaticMask.setStatus(_E)
_SnVLanByProtocolExcludeMask_Type=PortMask
_SnVLanByProtocolExcludeMask_Object=MibTableColumn
snVLanByProtocolExcludeMask=_SnVLanByProtocolExcludeMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,5),_SnVLanByProtocolExcludeMask_Type())
snVLanByProtocolExcludeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolExcludeMask.setStatus(_E)
class _SnVLanByProtocolRouterIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SnVLanByProtocolRouterIntf_Type.__name__=_C
_SnVLanByProtocolRouterIntf_Object=MibTableColumn
snVLanByProtocolRouterIntf=_SnVLanByProtocolRouterIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,6),_SnVLanByProtocolRouterIntf_Type())
snVLanByProtocolRouterIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolRouterIntf.setStatus(_A)
class _SnVLanByProtocolRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnVLanByProtocolRowStatus_Type.__name__=_C
_SnVLanByProtocolRowStatus_Object=MibTableColumn
snVLanByProtocolRowStatus=_SnVLanByProtocolRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,7),_SnVLanByProtocolRowStatus_Type())
snVLanByProtocolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolRowStatus.setStatus(_A)
_SnVLanByProtocolDynamicMask_Type=PortMask
_SnVLanByProtocolDynamicMask_Object=MibTableColumn
snVLanByProtocolDynamicMask=_SnVLanByProtocolDynamicMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,8),_SnVLanByProtocolDynamicMask_Type())
snVLanByProtocolDynamicMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByProtocolDynamicMask.setStatus(_E)
class _SnVLanByProtocolChassisStaticMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByProtocolChassisStaticMask_Type.__name__=_I
_SnVLanByProtocolChassisStaticMask_Object=MibTableColumn
snVLanByProtocolChassisStaticMask=_SnVLanByProtocolChassisStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,9),_SnVLanByProtocolChassisStaticMask_Type())
snVLanByProtocolChassisStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolChassisStaticMask.setStatus(_E)
class _SnVLanByProtocolChassisExcludeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByProtocolChassisExcludeMask_Type.__name__=_I
_SnVLanByProtocolChassisExcludeMask_Object=MibTableColumn
snVLanByProtocolChassisExcludeMask=_SnVLanByProtocolChassisExcludeMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,10),_SnVLanByProtocolChassisExcludeMask_Type())
snVLanByProtocolChassisExcludeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolChassisExcludeMask.setStatus(_E)
class _SnVLanByProtocolChassisDynamicMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByProtocolChassisDynamicMask_Type.__name__=_I
_SnVLanByProtocolChassisDynamicMask_Object=MibTableColumn
snVLanByProtocolChassisDynamicMask=_SnVLanByProtocolChassisDynamicMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,11),_SnVLanByProtocolChassisDynamicMask_Type())
snVLanByProtocolChassisDynamicMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByProtocolChassisDynamicMask.setStatus(_E)
class _SnVLanByProtocolVLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnVLanByProtocolVLanName_Type.__name__=_N
_SnVLanByProtocolVLanName_Object=MibTableColumn
snVLanByProtocolVLanName=_SnVLanByProtocolVLanName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,12),_SnVLanByProtocolVLanName_Type())
snVLanByProtocolVLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolVLanName.setStatus(_A)
_SnVLanByProtocolStaticPortList_Type=OctetString
_SnVLanByProtocolStaticPortList_Object=MibTableColumn
snVLanByProtocolStaticPortList=_SnVLanByProtocolStaticPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,13),_SnVLanByProtocolStaticPortList_Type())
snVLanByProtocolStaticPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolStaticPortList.setStatus(_A)
_SnVLanByProtocolExcludePortList_Type=OctetString
_SnVLanByProtocolExcludePortList_Object=MibTableColumn
snVLanByProtocolExcludePortList=_SnVLanByProtocolExcludePortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,14),_SnVLanByProtocolExcludePortList_Type())
snVLanByProtocolExcludePortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByProtocolExcludePortList.setStatus(_A)
_SnVLanByProtocolDynamicPortList_Type=OctetString
_SnVLanByProtocolDynamicPortList_Object=MibTableColumn
snVLanByProtocolDynamicPortList=_SnVLanByProtocolDynamicPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,2,1,15),_SnVLanByProtocolDynamicPortList_Type())
snVLanByProtocolDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByProtocolDynamicPortList.setStatus(_A)
_SnVLanByIpSubnetTable_Object=MibTable
snVLanByIpSubnetTable=_SnVLanByIpSubnetTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3))
if mibBuilder.loadTexts:snVLanByIpSubnetTable.setStatus(_A)
_SnVLanByIpSubnetEntry_Object=MibTableRow
snVLanByIpSubnetEntry=_SnVLanByIpSubnetEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1))
snVLanByIpSubnetEntry.setIndexNames((0,_F,_p),(0,_F,_q),(0,_F,_r))
if mibBuilder.loadTexts:snVLanByIpSubnetEntry.setStatus(_A)
class _SnVLanByIpSubnetVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByIpSubnetVLanId_Type.__name__=_C
_SnVLanByIpSubnetVLanId_Object=MibTableColumn
snVLanByIpSubnetVLanId=_SnVLanByIpSubnetVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,1),_SnVLanByIpSubnetVLanId_Type())
snVLanByIpSubnetVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetVLanId.setStatus(_A)
_SnVLanByIpSubnetIpAddress_Type=IpAddress
_SnVLanByIpSubnetIpAddress_Object=MibTableColumn
snVLanByIpSubnetIpAddress=_SnVLanByIpSubnetIpAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,2),_SnVLanByIpSubnetIpAddress_Type())
snVLanByIpSubnetIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetIpAddress.setStatus(_A)
_SnVLanByIpSubnetSubnetMask_Type=IpAddress
_SnVLanByIpSubnetSubnetMask_Object=MibTableColumn
snVLanByIpSubnetSubnetMask=_SnVLanByIpSubnetSubnetMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,3),_SnVLanByIpSubnetSubnetMask_Type())
snVLanByIpSubnetSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetSubnetMask.setStatus(_A)
class _SnVLanByIpSubnetDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnVLanByIpSubnetDynamic_Type.__name__=_C
_SnVLanByIpSubnetDynamic_Object=MibTableColumn
snVLanByIpSubnetDynamic=_SnVLanByIpSubnetDynamic_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,4),_SnVLanByIpSubnetDynamic_Type())
snVLanByIpSubnetDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetDynamic.setStatus(_A)
_SnVLanByIpSubnetStaticMask_Type=PortMask
_SnVLanByIpSubnetStaticMask_Object=MibTableColumn
snVLanByIpSubnetStaticMask=_SnVLanByIpSubnetStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,5),_SnVLanByIpSubnetStaticMask_Type())
snVLanByIpSubnetStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetStaticMask.setStatus(_E)
_SnVLanByIpSubnetExcludeMask_Type=PortMask
_SnVLanByIpSubnetExcludeMask_Object=MibTableColumn
snVLanByIpSubnetExcludeMask=_SnVLanByIpSubnetExcludeMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,6),_SnVLanByIpSubnetExcludeMask_Type())
snVLanByIpSubnetExcludeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetExcludeMask.setStatus(_E)
class _SnVLanByIpSubnetRouterIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SnVLanByIpSubnetRouterIntf_Type.__name__=_C
_SnVLanByIpSubnetRouterIntf_Object=MibTableColumn
snVLanByIpSubnetRouterIntf=_SnVLanByIpSubnetRouterIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,7),_SnVLanByIpSubnetRouterIntf_Type())
snVLanByIpSubnetRouterIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetRouterIntf.setStatus(_A)
class _SnVLanByIpSubnetRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnVLanByIpSubnetRowStatus_Type.__name__=_C
_SnVLanByIpSubnetRowStatus_Object=MibTableColumn
snVLanByIpSubnetRowStatus=_SnVLanByIpSubnetRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,8),_SnVLanByIpSubnetRowStatus_Type())
snVLanByIpSubnetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetRowStatus.setStatus(_A)
_SnVLanByIpSubnetDynamicMask_Type=PortMask
_SnVLanByIpSubnetDynamicMask_Object=MibTableColumn
snVLanByIpSubnetDynamicMask=_SnVLanByIpSubnetDynamicMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,9),_SnVLanByIpSubnetDynamicMask_Type())
snVLanByIpSubnetDynamicMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetDynamicMask.setStatus(_E)
class _SnVLanByIpSubnetChassisStaticMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByIpSubnetChassisStaticMask_Type.__name__=_I
_SnVLanByIpSubnetChassisStaticMask_Object=MibTableColumn
snVLanByIpSubnetChassisStaticMask=_SnVLanByIpSubnetChassisStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,10),_SnVLanByIpSubnetChassisStaticMask_Type())
snVLanByIpSubnetChassisStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetChassisStaticMask.setStatus(_E)
class _SnVLanByIpSubnetChassisExcludeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByIpSubnetChassisExcludeMask_Type.__name__=_I
_SnVLanByIpSubnetChassisExcludeMask_Object=MibTableColumn
snVLanByIpSubnetChassisExcludeMask=_SnVLanByIpSubnetChassisExcludeMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,11),_SnVLanByIpSubnetChassisExcludeMask_Type())
snVLanByIpSubnetChassisExcludeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetChassisExcludeMask.setStatus(_E)
class _SnVLanByIpSubnetChassisDynamicMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByIpSubnetChassisDynamicMask_Type.__name__=_I
_SnVLanByIpSubnetChassisDynamicMask_Object=MibTableColumn
snVLanByIpSubnetChassisDynamicMask=_SnVLanByIpSubnetChassisDynamicMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,12),_SnVLanByIpSubnetChassisDynamicMask_Type())
snVLanByIpSubnetChassisDynamicMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetChassisDynamicMask.setStatus(_E)
class _SnVLanByIpSubnetVLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnVLanByIpSubnetVLanName_Type.__name__=_N
_SnVLanByIpSubnetVLanName_Object=MibTableColumn
snVLanByIpSubnetVLanName=_SnVLanByIpSubnetVLanName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,13),_SnVLanByIpSubnetVLanName_Type())
snVLanByIpSubnetVLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetVLanName.setStatus(_A)
_SnVLanByIpSubnetStaticPortList_Type=OctetString
_SnVLanByIpSubnetStaticPortList_Object=MibTableColumn
snVLanByIpSubnetStaticPortList=_SnVLanByIpSubnetStaticPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,14),_SnVLanByIpSubnetStaticPortList_Type())
snVLanByIpSubnetStaticPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetStaticPortList.setStatus(_A)
_SnVLanByIpSubnetExcludePortList_Type=OctetString
_SnVLanByIpSubnetExcludePortList_Object=MibTableColumn
snVLanByIpSubnetExcludePortList=_SnVLanByIpSubnetExcludePortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,15),_SnVLanByIpSubnetExcludePortList_Type())
snVLanByIpSubnetExcludePortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpSubnetExcludePortList.setStatus(_A)
_SnVLanByIpSubnetDynamicPortList_Type=OctetString
_SnVLanByIpSubnetDynamicPortList_Object=MibTableColumn
snVLanByIpSubnetDynamicPortList=_SnVLanByIpSubnetDynamicPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,3,1,16),_SnVLanByIpSubnetDynamicPortList_Type())
snVLanByIpSubnetDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpSubnetDynamicPortList.setStatus(_A)
_SnVLanByIpxNetTable_Object=MibTable
snVLanByIpxNetTable=_SnVLanByIpxNetTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4))
if mibBuilder.loadTexts:snVLanByIpxNetTable.setStatus(_A)
_SnVLanByIpxNetEntry_Object=MibTableRow
snVLanByIpxNetEntry=_SnVLanByIpxNetEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1))
snVLanByIpxNetEntry.setIndexNames((0,_F,_s),(0,_F,_t),(0,_F,_u))
if mibBuilder.loadTexts:snVLanByIpxNetEntry.setStatus(_A)
class _SnVLanByIpxNetVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByIpxNetVLanId_Type.__name__=_C
_SnVLanByIpxNetVLanId_Object=MibTableColumn
snVLanByIpxNetVLanId=_SnVLanByIpxNetVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,1),_SnVLanByIpxNetVLanId_Type())
snVLanByIpxNetVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetVLanId.setStatus(_A)
class _SnVLanByIpxNetNetworkNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SnVLanByIpxNetNetworkNum_Type.__name__=_I
_SnVLanByIpxNetNetworkNum_Object=MibTableColumn
snVLanByIpxNetNetworkNum=_SnVLanByIpxNetNetworkNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,2),_SnVLanByIpxNetNetworkNum_Type())
snVLanByIpxNetNetworkNum.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetNetworkNum.setStatus(_A)
class _SnVLanByIpxNetFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_v,0),('ipxEthernet8022',1),('ipxEthernet8023',2),('ipxEthernetII',3),('ipxEthernetSnap',4)))
_SnVLanByIpxNetFrameType_Type.__name__=_C
_SnVLanByIpxNetFrameType_Object=MibTableColumn
snVLanByIpxNetFrameType=_SnVLanByIpxNetFrameType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,3),_SnVLanByIpxNetFrameType_Type())
snVLanByIpxNetFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetFrameType.setStatus(_A)
class _SnVLanByIpxNetDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnVLanByIpxNetDynamic_Type.__name__=_C
_SnVLanByIpxNetDynamic_Object=MibTableColumn
snVLanByIpxNetDynamic=_SnVLanByIpxNetDynamic_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,4),_SnVLanByIpxNetDynamic_Type())
snVLanByIpxNetDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetDynamic.setStatus(_A)
_SnVLanByIpxNetStaticMask_Type=PortMask
_SnVLanByIpxNetStaticMask_Object=MibTableColumn
snVLanByIpxNetStaticMask=_SnVLanByIpxNetStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,5),_SnVLanByIpxNetStaticMask_Type())
snVLanByIpxNetStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetStaticMask.setStatus(_E)
_SnVLanByIpxNetExcludeMask_Type=PortMask
_SnVLanByIpxNetExcludeMask_Object=MibTableColumn
snVLanByIpxNetExcludeMask=_SnVLanByIpxNetExcludeMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,6),_SnVLanByIpxNetExcludeMask_Type())
snVLanByIpxNetExcludeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetExcludeMask.setStatus(_E)
class _SnVLanByIpxNetRouterIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SnVLanByIpxNetRouterIntf_Type.__name__=_C
_SnVLanByIpxNetRouterIntf_Object=MibTableColumn
snVLanByIpxNetRouterIntf=_SnVLanByIpxNetRouterIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,7),_SnVLanByIpxNetRouterIntf_Type())
snVLanByIpxNetRouterIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetRouterIntf.setStatus(_A)
class _SnVLanByIpxNetRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnVLanByIpxNetRowStatus_Type.__name__=_C
_SnVLanByIpxNetRowStatus_Object=MibTableColumn
snVLanByIpxNetRowStatus=_SnVLanByIpxNetRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,8),_SnVLanByIpxNetRowStatus_Type())
snVLanByIpxNetRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetRowStatus.setStatus(_A)
_SnVLanByIpxNetDynamicMask_Type=PortMask
_SnVLanByIpxNetDynamicMask_Object=MibTableColumn
snVLanByIpxNetDynamicMask=_SnVLanByIpxNetDynamicMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,9),_SnVLanByIpxNetDynamicMask_Type())
snVLanByIpxNetDynamicMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetDynamicMask.setStatus(_E)
class _SnVLanByIpxNetChassisStaticMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByIpxNetChassisStaticMask_Type.__name__=_I
_SnVLanByIpxNetChassisStaticMask_Object=MibTableColumn
snVLanByIpxNetChassisStaticMask=_SnVLanByIpxNetChassisStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,10),_SnVLanByIpxNetChassisStaticMask_Type())
snVLanByIpxNetChassisStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetChassisStaticMask.setStatus(_E)
class _SnVLanByIpxNetChassisExcludeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByIpxNetChassisExcludeMask_Type.__name__=_I
_SnVLanByIpxNetChassisExcludeMask_Object=MibTableColumn
snVLanByIpxNetChassisExcludeMask=_SnVLanByIpxNetChassisExcludeMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,11),_SnVLanByIpxNetChassisExcludeMask_Type())
snVLanByIpxNetChassisExcludeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetChassisExcludeMask.setStatus(_E)
class _SnVLanByIpxNetChassisDynamicMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByIpxNetChassisDynamicMask_Type.__name__=_I
_SnVLanByIpxNetChassisDynamicMask_Object=MibTableColumn
snVLanByIpxNetChassisDynamicMask=_SnVLanByIpxNetChassisDynamicMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,12),_SnVLanByIpxNetChassisDynamicMask_Type())
snVLanByIpxNetChassisDynamicMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetChassisDynamicMask.setStatus(_E)
class _SnVLanByIpxNetVLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnVLanByIpxNetVLanName_Type.__name__=_N
_SnVLanByIpxNetVLanName_Object=MibTableColumn
snVLanByIpxNetVLanName=_SnVLanByIpxNetVLanName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,13),_SnVLanByIpxNetVLanName_Type())
snVLanByIpxNetVLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetVLanName.setStatus(_A)
_SnVLanByIpxNetStaticPortList_Type=OctetString
_SnVLanByIpxNetStaticPortList_Object=MibTableColumn
snVLanByIpxNetStaticPortList=_SnVLanByIpxNetStaticPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,14),_SnVLanByIpxNetStaticPortList_Type())
snVLanByIpxNetStaticPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetStaticPortList.setStatus(_A)
_SnVLanByIpxNetExcludePortList_Type=OctetString
_SnVLanByIpxNetExcludePortList_Object=MibTableColumn
snVLanByIpxNetExcludePortList=_SnVLanByIpxNetExcludePortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,15),_SnVLanByIpxNetExcludePortList_Type())
snVLanByIpxNetExcludePortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByIpxNetExcludePortList.setStatus(_A)
_SnVLanByIpxNetDynamicPortList_Type=OctetString
_SnVLanByIpxNetDynamicPortList_Object=MibTableColumn
snVLanByIpxNetDynamicPortList=_SnVLanByIpxNetDynamicPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,4,1,16),_SnVLanByIpxNetDynamicPortList_Type())
snVLanByIpxNetDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByIpxNetDynamicPortList.setStatus(_A)
_SnVLanByATCableTable_Object=MibTable
snVLanByATCableTable=_SnVLanByATCableTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5))
if mibBuilder.loadTexts:snVLanByATCableTable.setStatus(_A)
_SnVLanByATCableEntry_Object=MibTableRow
snVLanByATCableEntry=_SnVLanByATCableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1))
snVLanByATCableEntry.setIndexNames((0,_F,_w),(0,_F,_x))
if mibBuilder.loadTexts:snVLanByATCableEntry.setStatus(_A)
class _SnVLanByATCableVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByATCableVLanId_Type.__name__=_C
_SnVLanByATCableVLanId_Object=MibTableColumn
snVLanByATCableVLanId=_SnVLanByATCableVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,1),_SnVLanByATCableVLanId_Type())
snVLanByATCableVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByATCableVLanId.setStatus(_A)
_SnVLanByATCableIndex_Type=Integer32
_SnVLanByATCableIndex_Object=MibTableColumn
snVLanByATCableIndex=_SnVLanByATCableIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,2),_SnVLanByATCableIndex_Type())
snVLanByATCableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByATCableIndex.setStatus(_A)
class _SnVLanByATCableRouterIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_SnVLanByATCableRouterIntf_Type.__name__=_C
_SnVLanByATCableRouterIntf_Object=MibTableColumn
snVLanByATCableRouterIntf=_SnVLanByATCableRouterIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,3),_SnVLanByATCableRouterIntf_Type())
snVLanByATCableRouterIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByATCableRouterIntf.setStatus(_A)
class _SnVLanByATCableRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnVLanByATCableRowStatus_Type.__name__=_C
_SnVLanByATCableRowStatus_Object=MibTableColumn
snVLanByATCableRowStatus=_SnVLanByATCableRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,4),_SnVLanByATCableRowStatus_Type())
snVLanByATCableRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByATCableRowStatus.setStatus(_A)
class _SnVLanByATCableChassisStaticMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_SnVLanByATCableChassisStaticMask_Type.__name__=_I
_SnVLanByATCableChassisStaticMask_Object=MibTableColumn
snVLanByATCableChassisStaticMask=_SnVLanByATCableChassisStaticMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,5),_SnVLanByATCableChassisStaticMask_Type())
snVLanByATCableChassisStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByATCableChassisStaticMask.setStatus(_E)
class _SnVLanByATCableVLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnVLanByATCableVLanName_Type.__name__=_N
_SnVLanByATCableVLanName_Object=MibTableColumn
snVLanByATCableVLanName=_SnVLanByATCableVLanName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,6),_SnVLanByATCableVLanName_Type())
snVLanByATCableVLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByATCableVLanName.setStatus(_A)
_SnVLanByATCableStaticPortList_Type=OctetString
_SnVLanByATCableStaticPortList_Object=MibTableColumn
snVLanByATCableStaticPortList=_SnVLanByATCableStaticPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,5,1,7),_SnVLanByATCableStaticPortList_Type())
snVLanByATCableStaticPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByATCableStaticPortList.setStatus(_A)
_SnVLanByPortMemberTable_Object=MibTable
snVLanByPortMemberTable=_SnVLanByPortMemberTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,6))
if mibBuilder.loadTexts:snVLanByPortMemberTable.setStatus(_A)
_SnVLanByPortMemberEntry_Object=MibTableRow
snVLanByPortMemberEntry=_SnVLanByPortMemberEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,6,1))
snVLanByPortMemberEntry.setIndexNames((0,_F,_y),(0,_F,_z))
if mibBuilder.loadTexts:snVLanByPortMemberEntry.setStatus(_A)
class _SnVLanByPortMemberVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByPortMemberVLanId_Type.__name__=_C
_SnVLanByPortMemberVLanId_Object=MibTableColumn
snVLanByPortMemberVLanId=_SnVLanByPortMemberVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,6,1,1),_SnVLanByPortMemberVLanId_Type())
snVLanByPortMemberVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortMemberVLanId.setStatus(_A)
_SnVLanByPortMemberPortId_Type=Integer32
_SnVLanByPortMemberPortId_Object=MibTableColumn
snVLanByPortMemberPortId=_SnVLanByPortMemberPortId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,6,1,2),_SnVLanByPortMemberPortId_Type())
snVLanByPortMemberPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortMemberPortId.setStatus(_A)
class _SnVLanByPortMemberRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnVLanByPortMemberRowStatus_Type.__name__=_C
_SnVLanByPortMemberRowStatus_Object=MibTableColumn
snVLanByPortMemberRowStatus=_SnVLanByPortMemberRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,6,1,3),_SnVLanByPortMemberRowStatus_Type())
snVLanByPortMemberRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortMemberRowStatus.setStatus(_A)
_SnVLanByPortCfgTable_Object=MibTable
snVLanByPortCfgTable=_SnVLanByPortCfgTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7))
if mibBuilder.loadTexts:snVLanByPortCfgTable.setStatus(_A)
_SnVLanByPortCfgEntry_Object=MibTableRow
snVLanByPortCfgEntry=_SnVLanByPortCfgEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1))
snVLanByPortCfgEntry.setIndexNames((0,_F,_A0))
if mibBuilder.loadTexts:snVLanByPortCfgEntry.setStatus(_A)
class _SnVLanByPortCfgVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SnVLanByPortCfgVLanId_Type.__name__=_C
_SnVLanByPortCfgVLanId_Object=MibTableColumn
snVLanByPortCfgVLanId=_SnVLanByPortCfgVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,1),_SnVLanByPortCfgVLanId_Type())
snVLanByPortCfgVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgVLanId.setStatus(_A)
class _SnVLanByPortCfgQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,0),(_V,1),(_W,2),(_X,3),(_R,4),(_S,5),(_Y,6),(_Z,7)))
_SnVLanByPortCfgQos_Type.__name__=_C
_SnVLanByPortCfgQos_Object=MibTableColumn
snVLanByPortCfgQos=_SnVLanByPortCfgQos_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,2),_SnVLanByPortCfgQos_Type())
snVLanByPortCfgQos.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgQos.setStatus(_A)
class _SnVLanByPortCfgStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnVLanByPortCfgStpMode_Type.__name__=_C
_SnVLanByPortCfgStpMode_Object=MibTableColumn
snVLanByPortCfgStpMode=_SnVLanByPortCfgStpMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,3),_SnVLanByPortCfgStpMode_Type())
snVLanByPortCfgStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgStpMode.setStatus(_A)
class _SnVLanByPortCfgStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnVLanByPortCfgStpPriority_Type.__name__=_C
_SnVLanByPortCfgStpPriority_Object=MibTableColumn
snVLanByPortCfgStpPriority=_SnVLanByPortCfgStpPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,4),_SnVLanByPortCfgStpPriority_Type())
snVLanByPortCfgStpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgStpPriority.setStatus(_A)
class _SnVLanByPortCfgStpGroupMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_SnVLanByPortCfgStpGroupMaxAge_Type.__name__=_C
_SnVLanByPortCfgStpGroupMaxAge_Object=MibTableColumn
snVLanByPortCfgStpGroupMaxAge=_SnVLanByPortCfgStpGroupMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,5),_SnVLanByPortCfgStpGroupMaxAge_Type())
snVLanByPortCfgStpGroupMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgStpGroupMaxAge.setStatus(_A)
class _SnVLanByPortCfgStpGroupHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SnVLanByPortCfgStpGroupHelloTime_Type.__name__=_C
_SnVLanByPortCfgStpGroupHelloTime_Object=MibTableColumn
snVLanByPortCfgStpGroupHelloTime=_SnVLanByPortCfgStpGroupHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,6),_SnVLanByPortCfgStpGroupHelloTime_Type())
snVLanByPortCfgStpGroupHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgStpGroupHelloTime.setStatus(_A)
class _SnVLanByPortCfgStpGroupForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_SnVLanByPortCfgStpGroupForwardDelay_Type.__name__=_C
_SnVLanByPortCfgStpGroupForwardDelay_Object=MibTableColumn
snVLanByPortCfgStpGroupForwardDelay=_SnVLanByPortCfgStpGroupForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,7),_SnVLanByPortCfgStpGroupForwardDelay_Type())
snVLanByPortCfgStpGroupForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgStpGroupForwardDelay.setStatus(_A)
_SnVLanByPortCfgBaseNumPorts_Type=Integer32
_SnVLanByPortCfgBaseNumPorts_Object=MibTableColumn
snVLanByPortCfgBaseNumPorts=_SnVLanByPortCfgBaseNumPorts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,8),_SnVLanByPortCfgBaseNumPorts_Type())
snVLanByPortCfgBaseNumPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgBaseNumPorts.setStatus(_A)
class _SnVLanByPortCfgBaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_j,2),(_k,3),('srt',4)))
_SnVLanByPortCfgBaseType_Type.__name__=_C
_SnVLanByPortCfgBaseType_Object=MibTableColumn
snVLanByPortCfgBaseType=_SnVLanByPortCfgBaseType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,9),_SnVLanByPortCfgBaseType_Type())
snVLanByPortCfgBaseType.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgBaseType.setStatus(_A)
class _SnVLanByPortCfgStpProtocolSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_l,2),(_m,3)))
_SnVLanByPortCfgStpProtocolSpecification_Type.__name__=_C
_SnVLanByPortCfgStpProtocolSpecification_Object=MibTableColumn
snVLanByPortCfgStpProtocolSpecification=_SnVLanByPortCfgStpProtocolSpecification_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,10),_SnVLanByPortCfgStpProtocolSpecification_Type())
snVLanByPortCfgStpProtocolSpecification.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpProtocolSpecification.setStatus(_A)
_SnVLanByPortCfgStpMaxAge_Type=Timeout
_SnVLanByPortCfgStpMaxAge_Object=MibTableColumn
snVLanByPortCfgStpMaxAge=_SnVLanByPortCfgStpMaxAge_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,11),_SnVLanByPortCfgStpMaxAge_Type())
snVLanByPortCfgStpMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpMaxAge.setStatus(_A)
_SnVLanByPortCfgStpHelloTime_Type=Timeout
_SnVLanByPortCfgStpHelloTime_Object=MibTableColumn
snVLanByPortCfgStpHelloTime=_SnVLanByPortCfgStpHelloTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,12),_SnVLanByPortCfgStpHelloTime_Type())
snVLanByPortCfgStpHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpHelloTime.setStatus(_A)
_SnVLanByPortCfgStpHoldTime_Type=Integer32
_SnVLanByPortCfgStpHoldTime_Object=MibTableColumn
snVLanByPortCfgStpHoldTime=_SnVLanByPortCfgStpHoldTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,13),_SnVLanByPortCfgStpHoldTime_Type())
snVLanByPortCfgStpHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpHoldTime.setStatus(_A)
_SnVLanByPortCfgStpForwardDelay_Type=Timeout
_SnVLanByPortCfgStpForwardDelay_Object=MibTableColumn
snVLanByPortCfgStpForwardDelay=_SnVLanByPortCfgStpForwardDelay_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,14),_SnVLanByPortCfgStpForwardDelay_Type())
snVLanByPortCfgStpForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpForwardDelay.setStatus(_A)
_SnVLanByPortCfgStpTimeSinceTopologyChange_Type=TimeTicks
_SnVLanByPortCfgStpTimeSinceTopologyChange_Object=MibTableColumn
snVLanByPortCfgStpTimeSinceTopologyChange=_SnVLanByPortCfgStpTimeSinceTopologyChange_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,15),_SnVLanByPortCfgStpTimeSinceTopologyChange_Type())
snVLanByPortCfgStpTimeSinceTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpTimeSinceTopologyChange.setStatus(_A)
_SnVLanByPortCfgStpTopChanges_Type=Counter32
_SnVLanByPortCfgStpTopChanges_Object=MibTableColumn
snVLanByPortCfgStpTopChanges=_SnVLanByPortCfgStpTopChanges_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,16),_SnVLanByPortCfgStpTopChanges_Type())
snVLanByPortCfgStpTopChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpTopChanges.setStatus(_A)
_SnVLanByPortCfgStpRootCost_Type=Integer32
_SnVLanByPortCfgStpRootCost_Object=MibTableColumn
snVLanByPortCfgStpRootCost=_SnVLanByPortCfgStpRootCost_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,17),_SnVLanByPortCfgStpRootCost_Type())
snVLanByPortCfgStpRootCost.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpRootCost.setStatus(_A)
_SnVLanByPortCfgStpRootPort_Type=Integer32
_SnVLanByPortCfgStpRootPort_Object=MibTableColumn
snVLanByPortCfgStpRootPort=_SnVLanByPortCfgStpRootPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,18),_SnVLanByPortCfgStpRootPort_Type())
snVLanByPortCfgStpRootPort.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpRootPort.setStatus(_A)
_SnVLanByPortCfgStpDesignatedRoot_Type=BridgeId
_SnVLanByPortCfgStpDesignatedRoot_Object=MibTableColumn
snVLanByPortCfgStpDesignatedRoot=_SnVLanByPortCfgStpDesignatedRoot_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,19),_SnVLanByPortCfgStpDesignatedRoot_Type())
snVLanByPortCfgStpDesignatedRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgStpDesignatedRoot.setStatus(_A)
_SnVLanByPortCfgBaseBridgeAddress_Type=MacAddress
_SnVLanByPortCfgBaseBridgeAddress_Object=MibTableColumn
snVLanByPortCfgBaseBridgeAddress=_SnVLanByPortCfgBaseBridgeAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,20),_SnVLanByPortCfgBaseBridgeAddress_Type())
snVLanByPortCfgBaseBridgeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snVLanByPortCfgBaseBridgeAddress.setStatus(_A)
class _SnVLanByPortCfgVLanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnVLanByPortCfgVLanName_Type.__name__=_N
_SnVLanByPortCfgVLanName_Object=MibTableColumn
snVLanByPortCfgVLanName=_SnVLanByPortCfgVLanName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,21),_SnVLanByPortCfgVLanName_Type())
snVLanByPortCfgVLanName.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgVLanName.setStatus(_A)
_SnVLanByPortCfgRouterIntf_Type=Integer32
_SnVLanByPortCfgRouterIntf_Object=MibTableColumn
snVLanByPortCfgRouterIntf=_SnVLanByPortCfgRouterIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,22),_SnVLanByPortCfgRouterIntf_Type())
snVLanByPortCfgRouterIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgRouterIntf.setStatus(_A)
class _SnVLanByPortCfgRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_SnVLanByPortCfgRowStatus_Type.__name__=_C
_SnVLanByPortCfgRowStatus_Object=MibTableColumn
snVLanByPortCfgRowStatus=_SnVLanByPortCfgRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,2,7,1,23),_SnVLanByPortCfgRowStatus_Type())
snVLanByPortCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snVLanByPortCfgRowStatus.setStatus(_A)
_SnSwPortInfo_ObjectIdentity=ObjectIdentity
snSwPortInfo=_SnSwPortInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3))
_SnSwPortInfoTable_Object=MibTable
snSwPortInfoTable=_SnSwPortInfoTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1))
if mibBuilder.loadTexts:snSwPortInfoTable.setStatus(_A)
_SnSwPortInfoEntry_Object=MibTableRow
snSwPortInfoEntry=_SnSwPortInfoEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1))
snSwPortInfoEntry.setIndexNames((0,_F,_A1))
if mibBuilder.loadTexts:snSwPortInfoEntry.setStatus(_A)
_SnSwPortInfoPortNum_Type=Integer32
_SnSwPortInfoPortNum_Object=MibTableColumn
snSwPortInfoPortNum=_SnSwPortInfoPortNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,1),_SnSwPortInfoPortNum_Type())
snSwPortInfoPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInfoPortNum.setStatus(_A)
class _SnSwPortInfoMonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('input',1),('output',2),('both',3)))
_SnSwPortInfoMonitorMode_Type.__name__=_C
_SnSwPortInfoMonitorMode_Object=MibTableColumn
snSwPortInfoMonitorMode=_SnSwPortInfoMonitorMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,2),_SnSwPortInfoMonitorMode_Type())
snSwPortInfoMonitorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoMonitorMode.setStatus(_A)
class _SnSwPortInfoTagMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tagged',1),('untagged',2),('auto',3),(_G,4)))
_SnSwPortInfoTagMode_Type.__name__=_C
_SnSwPortInfoTagMode_Object=MibTableColumn
snSwPortInfoTagMode=_SnSwPortInfoTagMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,3),_SnSwPortInfoTagMode_Type())
snSwPortInfoTagMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoTagMode.setStatus(_A)
class _SnSwPortInfoChnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('halfDuplex',1),('fullDuplex',2)))
_SnSwPortInfoChnMode_Type.__name__=_C
_SnSwPortInfoChnMode_Object=MibTableColumn
snSwPortInfoChnMode=_SnSwPortInfoChnMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,4),_SnSwPortInfoChnMode_Type())
snSwPortInfoChnMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoChnMode.setStatus(_A)
class _SnSwPortInfoSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),('sAutoSense',1),('s10M',2),('s100M',3),('s1G',4),('s45M',5),('s155M',6),('s10G',7)))
_SnSwPortInfoSpeed_Type.__name__=_C
_SnSwPortInfoSpeed_Object=MibTableColumn
snSwPortInfoSpeed=_SnSwPortInfoSpeed_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,5),_SnSwPortInfoSpeed_Type())
snSwPortInfoSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoSpeed.setStatus(_A)
class _SnSwPortInfoMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_J,1),('m100BaseTX',2),('m100BaseFX',3),('m1000BaseFX',4),('mT3',5),('m155ATM',6),(_A2,7),('m622ATM',8),('m155POS',9),('m622POS',10),('m2488POS',11),('m10000BaseFX',12)))
_SnSwPortInfoMediaType_Type.__name__=_C
_SnSwPortInfoMediaType_Object=MibTableColumn
snSwPortInfoMediaType=_SnSwPortInfoMediaType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,6),_SnSwPortInfoMediaType_Type())
snSwPortInfoMediaType.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInfoMediaType.setStatus(_A)
class _SnSwPortInfoConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('copper',2),('fiber',3)))
_SnSwPortInfoConnectorType_Type.__name__=_C
_SnSwPortInfoConnectorType_Object=MibTableColumn
snSwPortInfoConnectorType=_SnSwPortInfoConnectorType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,7),_SnSwPortInfoConnectorType_Type())
snSwPortInfoConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInfoConnectorType.setStatus(_A)
class _SnSwPortInfoAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_SnSwPortInfoAdminStatus_Type.__name__=_C
_SnSwPortInfoAdminStatus_Object=MibTableColumn
snSwPortInfoAdminStatus=_SnSwPortInfoAdminStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,8),_SnSwPortInfoAdminStatus_Type())
snSwPortInfoAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoAdminStatus.setStatus(_A)
class _SnSwPortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_SnSwPortInfoLinkStatus_Type.__name__=_C
_SnSwPortInfoLinkStatus_Object=MibTableColumn
snSwPortInfoLinkStatus=_SnSwPortInfoLinkStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,9),_SnSwPortInfoLinkStatus_Type())
snSwPortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInfoLinkStatus.setStatus(_A)
class _SnSwPortInfoPortQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,0),(_V,1),(_W,2),(_X,3),(_R,4),(_S,5),(_Y,6),(_Z,7)))
_SnSwPortInfoPortQos_Type.__name__=_C
_SnSwPortInfoPortQos_Object=MibTableColumn
snSwPortInfoPortQos=_SnSwPortInfoPortQos_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,10),_SnSwPortInfoPortQos_Type())
snSwPortInfoPortQos.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoPortQos.setStatus(_A)
_SnSwPortInfoPhysAddress_Type=PhysAddress
_SnSwPortInfoPhysAddress_Object=MibTableColumn
snSwPortInfoPhysAddress=_SnSwPortInfoPhysAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,11),_SnSwPortInfoPhysAddress_Type())
snSwPortInfoPhysAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInfoPhysAddress.setStatus(_A)
_SnSwPortStatsInFrames_Type=Counter32
_SnSwPortStatsInFrames_Object=MibTableColumn
snSwPortStatsInFrames=_SnSwPortStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,12),_SnSwPortStatsInFrames_Type())
snSwPortStatsInFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInFrames.setStatus(_A)
_SnSwPortStatsOutFrames_Type=Counter32
_SnSwPortStatsOutFrames_Object=MibTableColumn
snSwPortStatsOutFrames=_SnSwPortStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,13),_SnSwPortStatsOutFrames_Type())
snSwPortStatsOutFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutFrames.setStatus(_A)
_SnSwPortStatsAlignErrors_Type=Counter32
_SnSwPortStatsAlignErrors_Object=MibTableColumn
snSwPortStatsAlignErrors=_SnSwPortStatsAlignErrors_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,14),_SnSwPortStatsAlignErrors_Type())
snSwPortStatsAlignErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsAlignErrors.setStatus(_A)
_SnSwPortStatsFCSErrors_Type=Counter32
_SnSwPortStatsFCSErrors_Object=MibTableColumn
snSwPortStatsFCSErrors=_SnSwPortStatsFCSErrors_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,15),_SnSwPortStatsFCSErrors_Type())
snSwPortStatsFCSErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsFCSErrors.setStatus(_A)
_SnSwPortStatsMultiColliFrames_Type=Counter32
_SnSwPortStatsMultiColliFrames_Object=MibTableColumn
snSwPortStatsMultiColliFrames=_SnSwPortStatsMultiColliFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,16),_SnSwPortStatsMultiColliFrames_Type())
snSwPortStatsMultiColliFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsMultiColliFrames.setStatus(_A)
_SnSwPortStatsFrameTooLongs_Type=Counter32
_SnSwPortStatsFrameTooLongs_Object=MibTableColumn
snSwPortStatsFrameTooLongs=_SnSwPortStatsFrameTooLongs_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,17),_SnSwPortStatsFrameTooLongs_Type())
snSwPortStatsFrameTooLongs.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsFrameTooLongs.setStatus(_A)
_SnSwPortStatsTxColliFrames_Type=Counter32
_SnSwPortStatsTxColliFrames_Object=MibTableColumn
snSwPortStatsTxColliFrames=_SnSwPortStatsTxColliFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,18),_SnSwPortStatsTxColliFrames_Type())
snSwPortStatsTxColliFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsTxColliFrames.setStatus(_A)
_SnSwPortStatsRxColliFrames_Type=Counter32
_SnSwPortStatsRxColliFrames_Object=MibTableColumn
snSwPortStatsRxColliFrames=_SnSwPortStatsRxColliFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,19),_SnSwPortStatsRxColliFrames_Type())
snSwPortStatsRxColliFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsRxColliFrames.setStatus(_A)
_SnSwPortStatsFrameTooShorts_Type=Counter32
_SnSwPortStatsFrameTooShorts_Object=MibTableColumn
snSwPortStatsFrameTooShorts=_SnSwPortStatsFrameTooShorts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,20),_SnSwPortStatsFrameTooShorts_Type())
snSwPortStatsFrameTooShorts.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsFrameTooShorts.setStatus(_A)
class _SnSwPortLockAddressCount_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_SnSwPortLockAddressCount_Type.__name__=_C
_SnSwPortLockAddressCount_Object=MibTableColumn
snSwPortLockAddressCount=_SnSwPortLockAddressCount_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,21),_SnSwPortLockAddressCount_Type())
snSwPortLockAddressCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortLockAddressCount.setStatus(_A)
class _SnSwPortStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwPortStpPortEnable_Type.__name__=_C
_SnSwPortStpPortEnable_Object=MibTableColumn
snSwPortStpPortEnable=_SnSwPortStpPortEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,22),_SnSwPortStpPortEnable_Type())
snSwPortStpPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortStpPortEnable.setStatus(_A)
class _SnSwPortDhcpGateListId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_SnSwPortDhcpGateListId_Type.__name__=_C
_SnSwPortDhcpGateListId_Object=MibTableColumn
snSwPortDhcpGateListId=_SnSwPortDhcpGateListId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,23),_SnSwPortDhcpGateListId_Type())
snSwPortDhcpGateListId.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortDhcpGateListId.setStatus(_A)
class _SnSwPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SnSwPortName_Type.__name__=_N
_SnSwPortName_Object=MibTableColumn
snSwPortName=_SnSwPortName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,24),_SnSwPortName_Type())
snSwPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortName.setStatus(_A)
_SnSwPortStatsInBcastFrames_Type=Counter32
_SnSwPortStatsInBcastFrames_Object=MibTableColumn
snSwPortStatsInBcastFrames=_SnSwPortStatsInBcastFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,25),_SnSwPortStatsInBcastFrames_Type())
snSwPortStatsInBcastFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInBcastFrames.setStatus(_A)
_SnSwPortStatsOutBcastFrames_Type=Counter32
_SnSwPortStatsOutBcastFrames_Object=MibTableColumn
snSwPortStatsOutBcastFrames=_SnSwPortStatsOutBcastFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,26),_SnSwPortStatsOutBcastFrames_Type())
snSwPortStatsOutBcastFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutBcastFrames.setStatus(_A)
_SnSwPortStatsInMcastFrames_Type=Counter32
_SnSwPortStatsInMcastFrames_Object=MibTableColumn
snSwPortStatsInMcastFrames=_SnSwPortStatsInMcastFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,27),_SnSwPortStatsInMcastFrames_Type())
snSwPortStatsInMcastFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInMcastFrames.setStatus(_A)
_SnSwPortStatsOutMcastFrames_Type=Counter32
_SnSwPortStatsOutMcastFrames_Object=MibTableColumn
snSwPortStatsOutMcastFrames=_SnSwPortStatsOutMcastFrames_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,28),_SnSwPortStatsOutMcastFrames_Type())
snSwPortStatsOutMcastFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutMcastFrames.setStatus(_A)
_SnSwPortStatsInDiscard_Type=Counter32
_SnSwPortStatsInDiscard_Object=MibTableColumn
snSwPortStatsInDiscard=_SnSwPortStatsInDiscard_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,29),_SnSwPortStatsInDiscard_Type())
snSwPortStatsInDiscard.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInDiscard.setStatus(_A)
_SnSwPortStatsOutDiscard_Type=Counter32
_SnSwPortStatsOutDiscard_Object=MibTableColumn
snSwPortStatsOutDiscard=_SnSwPortStatsOutDiscard_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,30),_SnSwPortStatsOutDiscard_Type())
snSwPortStatsOutDiscard.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutDiscard.setStatus(_A)
_SnSwPortStatsMacStations_Type=Integer32
_SnSwPortStatsMacStations_Object=MibTableColumn
snSwPortStatsMacStations=_SnSwPortStatsMacStations_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,31),_SnSwPortStatsMacStations_Type())
snSwPortStatsMacStations.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsMacStations.setStatus(_A)
_SnSwPortCacheGroupId_Type=Integer32
_SnSwPortCacheGroupId_Object=MibTableColumn
snSwPortCacheGroupId=_SnSwPortCacheGroupId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,32),_SnSwPortCacheGroupId_Type())
snSwPortCacheGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortCacheGroupId.setStatus(_A)
_SnSwPortTransGroupId_Type=Integer32
_SnSwPortTransGroupId_Object=MibTableColumn
snSwPortTransGroupId=_SnSwPortTransGroupId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,33),_SnSwPortTransGroupId_Type())
snSwPortTransGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortTransGroupId.setStatus(_A)
class _SnSwPortInfoAutoNegotiate_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_H,1),(_f,2),('global',3),(_J,4)))
_SnSwPortInfoAutoNegotiate_Type.__name__=_C
_SnSwPortInfoAutoNegotiate_Object=MibTableColumn
snSwPortInfoAutoNegotiate=_SnSwPortInfoAutoNegotiate_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,34),_SnSwPortInfoAutoNegotiate_Type())
snSwPortInfoAutoNegotiate.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoAutoNegotiate.setStatus(_A)
class _SnSwPortInfoFlowControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwPortInfoFlowControl_Type.__name__=_C
_SnSwPortInfoFlowControl_Object=MibTableColumn
snSwPortInfoFlowControl=_SnSwPortInfoFlowControl_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,35),_SnSwPortInfoFlowControl_Type())
snSwPortInfoFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortInfoFlowControl.setStatus(_A)
class _SnSwPortInfoGigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*(('m1000BaseSX',0),('m1000BaseLX',1),('m1000BaseLH',2),('m1000BaseLHA',3),('m1000BaseLHB',4),(_A2,5),('m10000BaseSR',6),('m10000BaseLR',7),('m10000BaseER',8),(_v,255)))
_SnSwPortInfoGigType_Type.__name__=_C
_SnSwPortInfoGigType_Object=MibTableColumn
snSwPortInfoGigType=_SnSwPortInfoGigType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,36),_SnSwPortInfoGigType_Type())
snSwPortInfoGigType.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInfoGigType.setStatus(_A)
_SnSwPortStatsLinkChange_Type=Counter32
_SnSwPortStatsLinkChange_Object=MibTableColumn
snSwPortStatsLinkChange=_SnSwPortStatsLinkChange_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,37),_SnSwPortStatsLinkChange_Type())
snSwPortStatsLinkChange.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsLinkChange.setStatus(_A)
_SnSwPortIfIndex_Type=Integer32
_SnSwPortIfIndex_Object=MibTableColumn
snSwPortIfIndex=_SnSwPortIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,38),_SnSwPortIfIndex_Type())
snSwPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortIfIndex.setStatus(_A)
_SnSwPortDescr_Type=DisplayString
_SnSwPortDescr_Object=MibTableColumn
snSwPortDescr=_SnSwPortDescr_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,39),_SnSwPortDescr_Type())
snSwPortDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortDescr.setStatus(_A)
class _SnSwPortInOctets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SnSwPortInOctets_Type.__name__=_I
_SnSwPortInOctets_Object=MibTableColumn
snSwPortInOctets=_SnSwPortInOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,40),_SnSwPortInOctets_Type())
snSwPortInOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortInOctets.setStatus(_A)
class _SnSwPortOutOctets_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SnSwPortOutOctets_Type.__name__=_I
_SnSwPortOutOctets_Object=MibTableColumn
snSwPortOutOctets=_SnSwPortOutOctets_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,41),_SnSwPortOutOctets_Type())
snSwPortOutOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortOutOctets.setStatus(_A)
_SnSwPortStatsInBitsPerSec_Type=Gauge32
_SnSwPortStatsInBitsPerSec_Object=MibTableColumn
snSwPortStatsInBitsPerSec=_SnSwPortStatsInBitsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,42),_SnSwPortStatsInBitsPerSec_Type())
snSwPortStatsInBitsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInBitsPerSec.setStatus(_A)
_SnSwPortStatsOutBitsPerSec_Type=Gauge32
_SnSwPortStatsOutBitsPerSec_Object=MibTableColumn
snSwPortStatsOutBitsPerSec=_SnSwPortStatsOutBitsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,43),_SnSwPortStatsOutBitsPerSec_Type())
snSwPortStatsOutBitsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutBitsPerSec.setStatus(_A)
_SnSwPortStatsInPktsPerSec_Type=Gauge32
_SnSwPortStatsInPktsPerSec_Object=MibTableColumn
snSwPortStatsInPktsPerSec=_SnSwPortStatsInPktsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,44),_SnSwPortStatsInPktsPerSec_Type())
snSwPortStatsInPktsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInPktsPerSec.setStatus(_A)
_SnSwPortStatsOutPktsPerSec_Type=Gauge32
_SnSwPortStatsOutPktsPerSec_Object=MibTableColumn
snSwPortStatsOutPktsPerSec=_SnSwPortStatsOutPktsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,45),_SnSwPortStatsOutPktsPerSec_Type())
snSwPortStatsOutPktsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutPktsPerSec.setStatus(_A)
class _SnSwPortStatsInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SnSwPortStatsInUtilization_Type.__name__=_C
_SnSwPortStatsInUtilization_Object=MibTableColumn
snSwPortStatsInUtilization=_SnSwPortStatsInUtilization_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,46),_SnSwPortStatsInUtilization_Type())
snSwPortStatsInUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInUtilization.setStatus(_A)
class _SnSwPortStatsOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_SnSwPortStatsOutUtilization_Type.__name__=_C
_SnSwPortStatsOutUtilization_Object=MibTableColumn
snSwPortStatsOutUtilization=_SnSwPortStatsOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,47),_SnSwPortStatsOutUtilization_Type())
snSwPortStatsOutUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutUtilization.setStatus(_A)
class _SnSwPortFastSpanPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwPortFastSpanPortEnable_Type.__name__=_C
_SnSwPortFastSpanPortEnable_Object=MibTableColumn
snSwPortFastSpanPortEnable=_SnSwPortFastSpanPortEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,48),_SnSwPortFastSpanPortEnable_Type())
snSwPortFastSpanPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortFastSpanPortEnable.setStatus(_A)
class _SnSwPortFastSpanUplinkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwPortFastSpanUplinkEnable_Type.__name__=_C
_SnSwPortFastSpanUplinkEnable_Object=MibTableColumn
snSwPortFastSpanUplinkEnable=_SnSwPortFastSpanUplinkEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,49),_SnSwPortFastSpanUplinkEnable_Type())
snSwPortFastSpanUplinkEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortFastSpanUplinkEnable.setStatus(_A)
class _SnSwPortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SnSwPortVlanId_Type.__name__=_C
_SnSwPortVlanId_Object=MibTableColumn
snSwPortVlanId=_SnSwPortVlanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,50),_SnSwPortVlanId_Type())
snSwPortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortVlanId.setStatus(_A)
class _SnSwPortRouteOnly_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwPortRouteOnly_Type.__name__=_C
_SnSwPortRouteOnly_Object=MibTableColumn
snSwPortRouteOnly=_SnSwPortRouteOnly_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,51),_SnSwPortRouteOnly_Type())
snSwPortRouteOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortRouteOnly.setStatus(_A)
class _SnSwPortPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_SnSwPortPresent_Type.__name__=_C
_SnSwPortPresent_Object=MibTableColumn
snSwPortPresent=_SnSwPortPresent_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,52),_SnSwPortPresent_Type())
snSwPortPresent.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortPresent.setStatus(_A)
class _SnSwPortGBICStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('gbic',1),('miniGBIC',2),('empty',3),(_J,4)))
_SnSwPortGBICStatus_Type.__name__=_C
_SnSwPortGBICStatus_Object=MibTableColumn
snSwPortGBICStatus=_SnSwPortGBICStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,53),_SnSwPortGBICStatus_Type())
snSwPortGBICStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortGBICStatus.setStatus(_A)
_SnSwPortStatsInKiloBitsPerSec_Type=Unsigned32
_SnSwPortStatsInKiloBitsPerSec_Object=MibTableColumn
snSwPortStatsInKiloBitsPerSec=_SnSwPortStatsInKiloBitsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,54),_SnSwPortStatsInKiloBitsPerSec_Type())
snSwPortStatsInKiloBitsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsInKiloBitsPerSec.setStatus(_A)
_SnSwPortStatsOutKiloBitsPerSec_Type=Unsigned32
_SnSwPortStatsOutKiloBitsPerSec_Object=MibTableColumn
snSwPortStatsOutKiloBitsPerSec=_SnSwPortStatsOutKiloBitsPerSec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,55),_SnSwPortStatsOutKiloBitsPerSec_Type())
snSwPortStatsOutKiloBitsPerSec.setMaxAccess(_D)
if mibBuilder.loadTexts:snSwPortStatsOutKiloBitsPerSec.setStatus(_A)
class _SnSwPortLoadInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,300))
_SnSwPortLoadInterval_Type.__name__=_C
_SnSwPortLoadInterval_Object=MibTableColumn
snSwPortLoadInterval=_SnSwPortLoadInterval_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,56),_SnSwPortLoadInterval_Type())
snSwPortLoadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortLoadInterval.setStatus(_A)
class _SnSwPortTagType_Type(Integer32):defaultValue=33024
_SnSwPortTagType_Type.__name__=_C
_SnSwPortTagType_Object=MibTableColumn
snSwPortTagType=_SnSwPortTagType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,1,1,57),_SnSwPortTagType_Type())
snSwPortTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwPortTagType.setStatus(_A)
_SnInterfaceId_ObjectIdentity=ObjectIdentity
snInterfaceId=_SnInterfaceId_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,2))
_SnInterfaceLookupTable_Object=MibTable
snInterfaceLookupTable=_SnInterfaceLookupTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,3))
if mibBuilder.loadTexts:snInterfaceLookupTable.setStatus(_A)
_SnInterfaceLookupEntry_Object=MibTableRow
snInterfaceLookupEntry=_SnInterfaceLookupEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,3,1))
snInterfaceLookupEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:snInterfaceLookupEntry.setStatus(_A)
_SnInterfaceLookupInterfaceId_Type=InterfaceId
_SnInterfaceLookupInterfaceId_Object=MibTableColumn
snInterfaceLookupInterfaceId=_SnInterfaceLookupInterfaceId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,3,1,1),_SnInterfaceLookupInterfaceId_Type())
snInterfaceLookupInterfaceId.setMaxAccess(_D)
if mibBuilder.loadTexts:snInterfaceLookupInterfaceId.setStatus(_A)
_SnInterfaceLookupIfIndex_Type=Integer32
_SnInterfaceLookupIfIndex_Object=MibTableColumn
snInterfaceLookupIfIndex=_SnInterfaceLookupIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,3,1,2),_SnInterfaceLookupIfIndex_Type())
snInterfaceLookupIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snInterfaceLookupIfIndex.setStatus(_A)
_SnIfIndexLookupTable_Object=MibTable
snIfIndexLookupTable=_SnIfIndexLookupTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,4))
if mibBuilder.loadTexts:snIfIndexLookupTable.setStatus(_A)
_SnIfIndexLookupEntry_Object=MibTableRow
snIfIndexLookupEntry=_SnIfIndexLookupEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,4,1))
snIfIndexLookupEntry.setIndexNames((0,_F,_A4))
if mibBuilder.loadTexts:snIfIndexLookupEntry.setStatus(_A)
_SnIfIndexLookupIfIndex_Type=Integer32
_SnIfIndexLookupIfIndex_Object=MibTableColumn
snIfIndexLookupIfIndex=_SnIfIndexLookupIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,4,1,1),_SnIfIndexLookupIfIndex_Type())
snIfIndexLookupIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snIfIndexLookupIfIndex.setStatus(_A)
_SnIfIndexLookupInterfaceId_Type=InterfaceId
_SnIfIndexLookupInterfaceId_Object=MibTableColumn
snIfIndexLookupInterfaceId=_SnIfIndexLookupInterfaceId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,3,4,1,2),_SnIfIndexLookupInterfaceId_Type())
snIfIndexLookupInterfaceId.setMaxAccess(_D)
if mibBuilder.loadTexts:snIfIndexLookupInterfaceId.setStatus(_A)
_SnFdbInfo_ObjectIdentity=ObjectIdentity
snFdbInfo=_SnFdbInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4))
_SnFdbTable_Object=MibTable
snFdbTable=_SnFdbTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1))
if mibBuilder.loadTexts:snFdbTable.setStatus(_A)
_SnFdbEntry_Object=MibTableRow
snFdbEntry=_SnFdbEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1))
snFdbEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:snFdbEntry.setStatus(_A)
class _SnFdbStationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_SnFdbStationIndex_Type.__name__=_C
_SnFdbStationIndex_Object=MibTableColumn
snFdbStationIndex=_SnFdbStationIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,1),_SnFdbStationIndex_Type())
snFdbStationIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdbStationIndex.setStatus(_A)
_SnFdbStationAddr_Type=PhysAddress
_SnFdbStationAddr_Object=MibTableColumn
snFdbStationAddr=_SnFdbStationAddr_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,2),_SnFdbStationAddr_Type())
snFdbStationAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbStationAddr.setStatus(_A)
_SnFdbStationPort_Type=Integer32
_SnFdbStationPort_Object=MibTableColumn
snFdbStationPort=_SnFdbStationPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,3),_SnFdbStationPort_Type())
snFdbStationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbStationPort.setStatus(_A)
class _SnFdbVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnFdbVLanId_Type.__name__=_C
_SnFdbVLanId_Object=MibTableColumn
snFdbVLanId=_SnFdbVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,4),_SnFdbVLanId_Type())
snFdbVLanId.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbVLanId.setStatus(_A)
class _SnFdbStationQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Q,0),(_V,1),(_W,2),(_X,3),(_R,4),(_S,5),(_Y,6),(_Z,7)))
_SnFdbStationQos_Type.__name__=_C
_SnFdbStationQos_Object=MibTableColumn
snFdbStationQos=_SnFdbStationQos_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,5),_SnFdbStationQos_Type())
snFdbStationQos.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbStationQos.setStatus(_A)
class _SnFdbStationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notSupported',0),('host',1),('router',2)))
_SnFdbStationType_Type.__name__=_C
_SnFdbStationType_Object=MibTableColumn
snFdbStationType=_SnFdbStationType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,6),_SnFdbStationType_Type())
snFdbStationType.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbStationType.setStatus(_A)
class _SnFdbRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnFdbRowStatus_Type.__name__=_C
_SnFdbRowStatus_Object=MibTableColumn
snFdbRowStatus=_SnFdbRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,4,1,1,7),_SnFdbRowStatus_Type())
snFdbRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdbRowStatus.setStatus(_A)
_SnPortStpInfo_ObjectIdentity=ObjectIdentity
snPortStpInfo=_SnPortStpInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5))
_SnPortStpTable_Object=MibTable
snPortStpTable=_SnPortStpTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1))
if mibBuilder.loadTexts:snPortStpTable.setStatus(_A)
_SnPortStpEntry_Object=MibTableRow
snPortStpEntry=_SnPortStpEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1))
snPortStpEntry.setIndexNames((0,_F,_A6),(0,_F,_A7))
if mibBuilder.loadTexts:snPortStpEntry.setStatus(_A)
class _SnPortStpVLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnPortStpVLanId_Type.__name__=_C
_SnPortStpVLanId_Object=MibTableColumn
snPortStpVLanId=_SnPortStpVLanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,1),_SnPortStpVLanId_Type())
snPortStpVLanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpVLanId.setStatus(_A)
_SnPortStpPortNum_Type=Integer32
_SnPortStpPortNum_Object=MibTableColumn
snPortStpPortNum=_SnPortStpPortNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,2),_SnPortStpPortNum_Type())
snPortStpPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpPortNum.setStatus(_A)
class _SnPortStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,255))
_SnPortStpPortPriority_Type.__name__=_C
_SnPortStpPortPriority_Object=MibTableColumn
snPortStpPortPriority=_SnPortStpPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,3),_SnPortStpPortPriority_Type())
snPortStpPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortStpPortPriority.setStatus(_A)
class _SnPortStpPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnPortStpPathCost_Type.__name__=_C
_SnPortStpPathCost_Object=MibTableColumn
snPortStpPathCost=_SnPortStpPathCost_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,4),_SnPortStpPathCost_Type())
snPortStpPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:snPortStpPathCost.setStatus(_A)
class _SnPortStpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_h,0),(_i,1)))
_SnPortStpOperState_Type.__name__=_C
_SnPortStpOperState_Object=MibTableColumn
snPortStpOperState=_SnPortStpOperState_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,5),_SnPortStpOperState_Type())
snPortStpOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpOperState.setStatus(_A)
class _SnPortStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SnPortStpPortEnable_Type.__name__=_C
_SnPortStpPortEnable_Object=MibTableColumn
snPortStpPortEnable=_SnPortStpPortEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,6),_SnPortStpPortEnable_Type())
snPortStpPortEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:snPortStpPortEnable.setStatus(_A)
_SnPortStpPortForwardTransitions_Type=Counter32
_SnPortStpPortForwardTransitions_Object=MibTableColumn
snPortStpPortForwardTransitions=_SnPortStpPortForwardTransitions_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,7),_SnPortStpPortForwardTransitions_Type())
snPortStpPortForwardTransitions.setMaxAccess(_P)
if mibBuilder.loadTexts:snPortStpPortForwardTransitions.setStatus(_A)
class _SnPortStpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_SnPortStpPortState_Type.__name__=_C
_SnPortStpPortState_Object=MibTableColumn
snPortStpPortState=_SnPortStpPortState_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,8),_SnPortStpPortState_Type())
snPortStpPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpPortState.setStatus(_A)
_SnPortStpPortDesignatedCost_Type=Integer32
_SnPortStpPortDesignatedCost_Object=MibTableColumn
snPortStpPortDesignatedCost=_SnPortStpPortDesignatedCost_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,9),_SnPortStpPortDesignatedCost_Type())
snPortStpPortDesignatedCost.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpPortDesignatedCost.setStatus(_A)
_SnPortStpPortDesignatedRoot_Type=BridgeId
_SnPortStpPortDesignatedRoot_Object=MibTableColumn
snPortStpPortDesignatedRoot=_SnPortStpPortDesignatedRoot_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,10),_SnPortStpPortDesignatedRoot_Type())
snPortStpPortDesignatedRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpPortDesignatedRoot.setStatus(_A)
_SnPortStpPortDesignatedBridge_Type=BridgeId
_SnPortStpPortDesignatedBridge_Object=MibTableColumn
snPortStpPortDesignatedBridge=_SnPortStpPortDesignatedBridge_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,11),_SnPortStpPortDesignatedBridge_Type())
snPortStpPortDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpPortDesignatedBridge.setStatus(_A)
class _SnPortStpPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SnPortStpPortDesignatedPort_Type.__name__=_I
_SnPortStpPortDesignatedPort_Object=MibTableColumn
snPortStpPortDesignatedPort=_SnPortStpPortDesignatedPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,5,1,1,12),_SnPortStpPortDesignatedPort_Type())
snPortStpPortDesignatedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:snPortStpPortDesignatedPort.setStatus(_A)
_SnTrunkInfo_ObjectIdentity=ObjectIdentity
snTrunkInfo=_SnTrunkInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6))
_SnTrunkTable_Object=MibTable
snTrunkTable=_SnTrunkTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,1))
if mibBuilder.loadTexts:snTrunkTable.setStatus(_A)
_SnTrunkEntry_Object=MibTableRow
snTrunkEntry=_SnTrunkEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,1,1))
snTrunkEntry.setIndexNames((0,_F,_A8))
if mibBuilder.loadTexts:snTrunkEntry.setStatus(_A)
class _SnTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SnTrunkIndex_Type.__name__=_C
_SnTrunkIndex_Object=MibTableColumn
snTrunkIndex=_SnTrunkIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,1,1,1),_SnTrunkIndex_Type())
snTrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snTrunkIndex.setStatus(_A)
_SnTrunkPortMask_Type=PortMask
_SnTrunkPortMask_Object=MibTableColumn
snTrunkPortMask=_SnTrunkPortMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,1,1,2),_SnTrunkPortMask_Type())
snTrunkPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snTrunkPortMask.setStatus(_A)
class _SnTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switch',1),('server',2)))
_SnTrunkType_Type.__name__=_C
_SnTrunkType_Object=MibTableColumn
snTrunkType=_SnTrunkType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,1,1,3),_SnTrunkType_Type())
snTrunkType.setMaxAccess(_B)
if mibBuilder.loadTexts:snTrunkType.setStatus(_A)
_SnMSTrunkTable_Object=MibTable
snMSTrunkTable=_SnMSTrunkTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,2))
if mibBuilder.loadTexts:snMSTrunkTable.setStatus(_A)
_SnMSTrunkEntry_Object=MibTableRow
snMSTrunkEntry=_SnMSTrunkEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,2,1))
snMSTrunkEntry.setIndexNames((0,_F,_A9))
if mibBuilder.loadTexts:snMSTrunkEntry.setStatus(_A)
_SnMSTrunkPortIndex_Type=Integer32
_SnMSTrunkPortIndex_Object=MibTableColumn
snMSTrunkPortIndex=_SnMSTrunkPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,2,1,1),_SnMSTrunkPortIndex_Type())
snMSTrunkPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snMSTrunkPortIndex.setStatus(_A)
_SnMSTrunkPortList_Type=OctetString
_SnMSTrunkPortList_Object=MibTableColumn
snMSTrunkPortList=_SnMSTrunkPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,2,1,2),_SnMSTrunkPortList_Type())
snMSTrunkPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:snMSTrunkPortList.setStatus(_A)
class _SnMSTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switch',1),('server',2)))
_SnMSTrunkType_Type.__name__=_C
_SnMSTrunkType_Object=MibTableColumn
snMSTrunkType=_SnMSTrunkType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,2,1,3),_SnMSTrunkType_Type())
snMSTrunkType.setMaxAccess(_B)
if mibBuilder.loadTexts:snMSTrunkType.setStatus(_A)
class _SnMSTrunkRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_d,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnMSTrunkRowStatus_Type.__name__=_C
_SnMSTrunkRowStatus_Object=MibTableColumn
snMSTrunkRowStatus=_SnMSTrunkRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,6,2,1,4),_SnMSTrunkRowStatus_Type())
snMSTrunkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snMSTrunkRowStatus.setStatus(_A)
_SnSwSummary_ObjectIdentity=ObjectIdentity
snSwSummary=_SnSwSummary_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,7))
class _SnSwSummaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnSwSummaryMode_Type.__name__=_C
_SnSwSummaryMode_Object=MibScalar
snSwSummaryMode=_SnSwSummaryMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,7,1),_SnSwSummaryMode_Type())
snSwSummaryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:snSwSummaryMode.setStatus(_A)
_SnDhcpGatewayListInfo_ObjectIdentity=ObjectIdentity
snDhcpGatewayListInfo=_SnDhcpGatewayListInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,8))
_SnDhcpGatewayListTable_Object=MibTable
snDhcpGatewayListTable=_SnDhcpGatewayListTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,8,1))
if mibBuilder.loadTexts:snDhcpGatewayListTable.setStatus(_A)
_SnDhcpGatewayListEntry_Object=MibTableRow
snDhcpGatewayListEntry=_SnDhcpGatewayListEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,8,1,1))
snDhcpGatewayListEntry.setIndexNames((0,_F,_AA))
if mibBuilder.loadTexts:snDhcpGatewayListEntry.setStatus(_A)
class _SnDhcpGatewayListId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SnDhcpGatewayListId_Type.__name__=_C
_SnDhcpGatewayListId_Object=MibTableColumn
snDhcpGatewayListId=_SnDhcpGatewayListId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,8,1,1,1),_SnDhcpGatewayListId_Type())
snDhcpGatewayListId.setMaxAccess(_D)
if mibBuilder.loadTexts:snDhcpGatewayListId.setStatus(_A)
class _SnDhcpGatewayListAddrList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,32))
_SnDhcpGatewayListAddrList_Type.__name__=_I
_SnDhcpGatewayListAddrList_Object=MibTableColumn
snDhcpGatewayListAddrList=_SnDhcpGatewayListAddrList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,8,1,1,2),_SnDhcpGatewayListAddrList_Type())
snDhcpGatewayListAddrList.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpGatewayListAddrList.setStatus(_A)
class _SnDhcpGatewayListRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnDhcpGatewayListRowStatus_Type.__name__=_C
_SnDhcpGatewayListRowStatus_Object=MibTableColumn
snDhcpGatewayListRowStatus=_SnDhcpGatewayListRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,8,1,1,3),_SnDhcpGatewayListRowStatus_Type())
snDhcpGatewayListRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snDhcpGatewayListRowStatus.setStatus(_A)
_SnDnsInfo_ObjectIdentity=ObjectIdentity
snDnsInfo=_SnDnsInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,9))
class _SnDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SnDnsDomainName_Type.__name__=_N
_SnDnsDomainName_Object=MibScalar
snDnsDomainName=_SnDnsDomainName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,9,1),_SnDnsDomainName_Type())
snDnsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:snDnsDomainName.setStatus(_A)
class _SnDnsGatewayIpAddrList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SnDnsGatewayIpAddrList_Type.__name__=_I
_SnDnsGatewayIpAddrList_Object=MibScalar
snDnsGatewayIpAddrList=_SnDnsGatewayIpAddrList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,9,2),_SnDnsGatewayIpAddrList_Type())
snDnsGatewayIpAddrList.setMaxAccess(_B)
if mibBuilder.loadTexts:snDnsGatewayIpAddrList.setStatus(_A)
_SnMacFilter_ObjectIdentity=ObjectIdentity
snMacFilter=_SnMacFilter_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10))
_SnMacFilterTable_Object=MibTable
snMacFilterTable=_SnMacFilterTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1))
if mibBuilder.loadTexts:snMacFilterTable.setStatus(_A)
_SnMacFilterEntry_Object=MibTableRow
snMacFilterEntry=_SnMacFilterEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1))
snMacFilterEntry.setIndexNames((0,_F,_AB))
if mibBuilder.loadTexts:snMacFilterEntry.setStatus(_A)
_SnMacFilterIndex_Type=Integer32
_SnMacFilterIndex_Object=MibTableColumn
snMacFilterIndex=_SnMacFilterIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,1),_SnMacFilterIndex_Type())
snMacFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacFilterIndex.setStatus(_A)
class _SnMacFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
_SnMacFilterAction_Type.__name__=_C
_SnMacFilterAction_Object=MibTableColumn
snMacFilterAction=_SnMacFilterAction_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,2),_SnMacFilterAction_Type())
snMacFilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterAction.setStatus(_A)
_SnMacFilterSourceMac_Type=MacAddress
_SnMacFilterSourceMac_Object=MibTableColumn
snMacFilterSourceMac=_SnMacFilterSourceMac_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,3),_SnMacFilterSourceMac_Type())
snMacFilterSourceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterSourceMac.setStatus(_A)
_SnMacFilterSourceMask_Type=MacAddress
_SnMacFilterSourceMask_Object=MibTableColumn
snMacFilterSourceMask=_SnMacFilterSourceMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,4),_SnMacFilterSourceMask_Type())
snMacFilterSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterSourceMask.setStatus(_A)
_SnMacFilterDestMac_Type=MacAddress
_SnMacFilterDestMac_Object=MibTableColumn
snMacFilterDestMac=_SnMacFilterDestMac_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,5),_SnMacFilterDestMac_Type())
snMacFilterDestMac.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterDestMac.setStatus(_A)
_SnMacFilterDestMask_Type=MacAddress
_SnMacFilterDestMask_Object=MibTableColumn
snMacFilterDestMask=_SnMacFilterDestMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,6),_SnMacFilterDestMask_Type())
snMacFilterDestMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterDestMask.setStatus(_A)
class _SnMacFilterOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('equal',0),('notEqual',1),('less',2),('greater',3)))
_SnMacFilterOperator_Type.__name__=_C
_SnMacFilterOperator_Object=MibTableColumn
snMacFilterOperator=_SnMacFilterOperator_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,7),_SnMacFilterOperator_Type())
snMacFilterOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterOperator.setStatus(_A)
class _SnMacFilterFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notUsed',0),('ethernet',1),('llc',2),('snap',3)))
_SnMacFilterFrameType_Type.__name__=_C
_SnMacFilterFrameType_Object=MibTableColumn
snMacFilterFrameType=_SnMacFilterFrameType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,8),_SnMacFilterFrameType_Type())
snMacFilterFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterFrameType.setStatus(_A)
class _SnMacFilterFrameTypeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnMacFilterFrameTypeNum_Type.__name__=_C
_SnMacFilterFrameTypeNum_Object=MibTableColumn
snMacFilterFrameTypeNum=_SnMacFilterFrameTypeNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,9),_SnMacFilterFrameTypeNum_Type())
snMacFilterFrameTypeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterFrameTypeNum.setStatus(_A)
class _SnMacFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_d,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnMacFilterRowStatus_Type.__name__=_C
_SnMacFilterRowStatus_Object=MibTableColumn
snMacFilterRowStatus=_SnMacFilterRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,1,1,10),_SnMacFilterRowStatus_Type())
snMacFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterRowStatus.setStatus(_A)
_SnMacFilterPortAccessTable_Object=MibTable
snMacFilterPortAccessTable=_SnMacFilterPortAccessTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,2))
if mibBuilder.loadTexts:snMacFilterPortAccessTable.setStatus(_A)
_SnMacFilterPortAccessEntry_Object=MibTableRow
snMacFilterPortAccessEntry=_SnMacFilterPortAccessEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,2,1))
snMacFilterPortAccessEntry.setIndexNames((0,_F,_AC))
if mibBuilder.loadTexts:snMacFilterPortAccessEntry.setStatus(_A)
class _SnMacFilterPortAccessPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3900))
_SnMacFilterPortAccessPortIndex_Type.__name__=_C
_SnMacFilterPortAccessPortIndex_Object=MibTableColumn
snMacFilterPortAccessPortIndex=_SnMacFilterPortAccessPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,2,1,1),_SnMacFilterPortAccessPortIndex_Type())
snMacFilterPortAccessPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacFilterPortAccessPortIndex.setStatus(_A)
_SnMacFilterPortAccessFilters_Type=OctetString
_SnMacFilterPortAccessFilters_Object=MibTableColumn
snMacFilterPortAccessFilters=_SnMacFilterPortAccessFilters_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,2,1,2),_SnMacFilterPortAccessFilters_Type())
snMacFilterPortAccessFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterPortAccessFilters.setStatus(_A)
class _SnMacFilterPortAccessRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_d,1),(_K,2),(_L,3),(_M,4)))
_SnMacFilterPortAccessRowStatus_Type.__name__=_C
_SnMacFilterPortAccessRowStatus_Object=MibTableColumn
snMacFilterPortAccessRowStatus=_SnMacFilterPortAccessRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,10,2,1,3),_SnMacFilterPortAccessRowStatus_Type())
snMacFilterPortAccessRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snMacFilterPortAccessRowStatus.setStatus(_A)
_SnNTP_ObjectIdentity=ObjectIdentity
snNTP=_SnNTP_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11))
_SnNTPGeneral_ObjectIdentity=ObjectIdentity
snNTPGeneral=_SnNTPGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,1))
class _SnNTPPollInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnNTPPollInterval_Type.__name__=_C
_SnNTPPollInterval_Object=MibScalar
snNTPPollInterval=_SnNTPPollInterval_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,1,1),_SnNTPPollInterval_Type())
snNTPPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPPollInterval.setStatus(_A)
class _SnNTPTimeZone_Type(Integer32):defaultValue=23;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)));namedValues=NamedValues(*(('alaska',0),('aleutian',1),('arizona',2),('central',3),('eastIndiana',4),('eastern',5),('hawaii',6),('michigan',7),('mountain',8),('pacific',9),('samoa',10),('gmtPlus12',11),('gmtPlus11',12),('gmtPlus10',13),('gmtPlus9',14),('gmtPlus8',15),('gmtPlus7',16),('gmtPlus6',17),('gmtPlus5',18),('gmtPlus4',19),('gmtPlus3',20),('gmtPlus2',21),('gmtPlus1',22),('gmt',23),('gmtMinus1',24),('gmtMinus2',25),('gmtMinus3',26),('gmtMinus4',27),('gmtMinus5',28),('gmtMinus6',29),('gmtMinus7',30),('gmtMinus8',31),('gmtMinus9',32),('gmtMinus10',33),('gmtMinus11',34),('gmtMinus12',35)))
_SnNTPTimeZone_Type.__name__=_C
_SnNTPTimeZone_Object=MibScalar
snNTPTimeZone=_SnNTPTimeZone_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,1,2),_SnNTPTimeZone_Type())
snNTPTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPTimeZone.setStatus(_A)
class _SnNTPSummerTimeEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnNTPSummerTimeEnable_Type.__name__=_C
_SnNTPSummerTimeEnable_Object=MibScalar
snNTPSummerTimeEnable=_SnNTPSummerTimeEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,1,3),_SnNTPSummerTimeEnable_Type())
snNTPSummerTimeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPSummerTimeEnable.setStatus(_A)
class _SnNTPSystemClock_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_SnNTPSystemClock_Type.__name__=_I
_SnNTPSystemClock_Object=MibScalar
snNTPSystemClock=_SnNTPSystemClock_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,1,4),_SnNTPSystemClock_Type())
snNTPSystemClock.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPSystemClock.setStatus(_A)
class _SnNTPSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('synchronize',2)))
_SnNTPSync_Type.__name__=_C
_SnNTPSync_Object=MibScalar
snNTPSync=_SnNTPSync_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,1,5),_SnNTPSync_Type())
snNTPSync.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPSync.setStatus(_A)
_SnNTPServerTable_Object=MibTable
snNTPServerTable=_SnNTPServerTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,2))
if mibBuilder.loadTexts:snNTPServerTable.setStatus(_A)
_SnNTPServerEntry_Object=MibTableRow
snNTPServerEntry=_SnNTPServerEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,2,1))
snNTPServerEntry.setIndexNames((0,_F,_AD))
if mibBuilder.loadTexts:snNTPServerEntry.setStatus(_A)
_SnNTPServerIp_Type=IpAddress
_SnNTPServerIp_Object=MibTableColumn
snNTPServerIp=_SnNTPServerIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,2,1,1),_SnNTPServerIp_Type())
snNTPServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:snNTPServerIp.setStatus(_A)
class _SnNTPServerVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SnNTPServerVersion_Type.__name__=_C
_SnNTPServerVersion_Object=MibTableColumn
snNTPServerVersion=_SnNTPServerVersion_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,2,1,2),_SnNTPServerVersion_Type())
snNTPServerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPServerVersion.setStatus(_A)
class _SnNTPServerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnNTPServerRowStatus_Type.__name__=_C
_SnNTPServerRowStatus_Object=MibTableColumn
snNTPServerRowStatus=_SnNTPServerRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,11,2,1,3),_SnNTPServerRowStatus_Type())
snNTPServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snNTPServerRowStatus.setStatus(_A)
_SnRadius_ObjectIdentity=ObjectIdentity
snRadius=_SnRadius_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12))
_SnRadiusGeneral_ObjectIdentity=ObjectIdentity
snRadiusGeneral=_SnRadiusGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1))
class _SnRadiusSNMPAccess_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnRadiusSNMPAccess_Type.__name__=_C
_SnRadiusSNMPAccess_Object=MibScalar
snRadiusSNMPAccess=_SnRadiusSNMPAccess_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,1),_SnRadiusSNMPAccess_Type())
snRadiusSNMPAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:snRadiusSNMPAccess.setStatus(_A)
class _SnRadiusEnableTelnetAuth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnRadiusEnableTelnetAuth_Type.__name__=_C
_SnRadiusEnableTelnetAuth_Object=MibScalar
snRadiusEnableTelnetAuth=_SnRadiusEnableTelnetAuth_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,2),_SnRadiusEnableTelnetAuth_Type())
snRadiusEnableTelnetAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusEnableTelnetAuth.setStatus(_A)
class _SnRadiusRetransmit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_SnRadiusRetransmit_Type.__name__=_C
_SnRadiusRetransmit_Object=MibScalar
snRadiusRetransmit=_SnRadiusRetransmit_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,3),_SnRadiusRetransmit_Type())
snRadiusRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusRetransmit.setStatus(_A)
class _SnRadiusTimeOut_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_SnRadiusTimeOut_Type.__name__=_C
_SnRadiusTimeOut_Object=MibScalar
snRadiusTimeOut=_SnRadiusTimeOut_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,4),_SnRadiusTimeOut_Type())
snRadiusTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusTimeOut.setStatus(_A)
class _SnRadiusDeadTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SnRadiusDeadTime_Type.__name__=_C
_SnRadiusDeadTime_Object=MibScalar
snRadiusDeadTime=_SnRadiusDeadTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,5),_SnRadiusDeadTime_Type())
snRadiusDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusDeadTime.setStatus(_A)
class _SnRadiusKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnRadiusKey_Type.__name__=_N
_SnRadiusKey_Object=MibScalar
snRadiusKey=_SnRadiusKey_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,6),_SnRadiusKey_Type())
snRadiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusKey.setStatus(_A)
class _SnRadiusLoginMethod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_SnRadiusLoginMethod_Type.__name__=_I
_SnRadiusLoginMethod_Object=MibScalar
snRadiusLoginMethod=_SnRadiusLoginMethod_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,7),_SnRadiusLoginMethod_Type())
snRadiusLoginMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusLoginMethod.setStatus(_A)
class _SnRadiusEnableMethod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_SnRadiusEnableMethod_Type.__name__=_I
_SnRadiusEnableMethod_Object=MibScalar
snRadiusEnableMethod=_SnRadiusEnableMethod_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,8),_SnRadiusEnableMethod_Type())
snRadiusEnableMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusEnableMethod.setStatus(_A)
class _SnRadiusWebServerMethod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_SnRadiusWebServerMethod_Type.__name__=_I
_SnRadiusWebServerMethod_Object=MibScalar
snRadiusWebServerMethod=_SnRadiusWebServerMethod_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,9),_SnRadiusWebServerMethod_Type())
snRadiusWebServerMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusWebServerMethod.setStatus(_A)
class _SnRadiusSNMPServerMethod_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_SnRadiusSNMPServerMethod_Type.__name__=_I
_SnRadiusSNMPServerMethod_Object=MibScalar
snRadiusSNMPServerMethod=_SnRadiusSNMPServerMethod_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,1,10),_SnRadiusSNMPServerMethod_Type())
snRadiusSNMPServerMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusSNMPServerMethod.setStatus(_A)
_SnRadiusServerTable_Object=MibTable
snRadiusServerTable=_SnRadiusServerTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2))
if mibBuilder.loadTexts:snRadiusServerTable.setStatus(_A)
_SnRadiusServerEntry_Object=MibTableRow
snRadiusServerEntry=_SnRadiusServerEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1))
snRadiusServerEntry.setIndexNames((0,_F,_AE))
if mibBuilder.loadTexts:snRadiusServerEntry.setStatus(_A)
_SnRadiusServerIp_Type=IpAddress
_SnRadiusServerIp_Object=MibTableColumn
snRadiusServerIp=_SnRadiusServerIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1,1),_SnRadiusServerIp_Type())
snRadiusServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:snRadiusServerIp.setStatus(_A)
class _SnRadiusServerAuthPort_Type(Integer32):defaultValue=1645
_SnRadiusServerAuthPort_Type.__name__=_C
_SnRadiusServerAuthPort_Object=MibTableColumn
snRadiusServerAuthPort=_SnRadiusServerAuthPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1,2),_SnRadiusServerAuthPort_Type())
snRadiusServerAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusServerAuthPort.setStatus(_A)
class _SnRadiusServerAcctPort_Type(Integer32):defaultValue=1646
_SnRadiusServerAcctPort_Type.__name__=_C
_SnRadiusServerAcctPort_Object=MibTableColumn
snRadiusServerAcctPort=_SnRadiusServerAcctPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1,3),_SnRadiusServerAcctPort_Type())
snRadiusServerAcctPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusServerAcctPort.setStatus(_A)
class _SnRadiusServerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnRadiusServerRowStatus_Type.__name__=_C
_SnRadiusServerRowStatus_Object=MibTableColumn
snRadiusServerRowStatus=_SnRadiusServerRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1,4),_SnRadiusServerRowStatus_Type())
snRadiusServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusServerRowStatus.setStatus(_A)
class _SnRadiusServerRowKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnRadiusServerRowKey_Type.__name__=_N
_SnRadiusServerRowKey_Object=MibTableColumn
snRadiusServerRowKey=_SnRadiusServerRowKey_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1,5),_SnRadiusServerRowKey_Type())
snRadiusServerRowKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusServerRowKey.setStatus(_A)
class _SnRadiusServerUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_AF,2),(_AG,3),(_AH,4)))
_SnRadiusServerUsage_Type.__name__=_C
_SnRadiusServerUsage_Object=MibTableColumn
snRadiusServerUsage=_SnRadiusServerUsage_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,12,2,1,6),_SnRadiusServerUsage_Type())
snRadiusServerUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:snRadiusServerUsage.setStatus(_A)
_SnTacacs_ObjectIdentity=ObjectIdentity
snTacacs=_SnTacacs_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13))
_SnTacacsGeneral_ObjectIdentity=ObjectIdentity
snTacacsGeneral=_SnTacacsGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,1))
class _SnTacacsRetransmit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_SnTacacsRetransmit_Type.__name__=_C
_SnTacacsRetransmit_Object=MibScalar
snTacacsRetransmit=_SnTacacsRetransmit_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,1,1),_SnTacacsRetransmit_Type())
snTacacsRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsRetransmit.setStatus(_A)
class _SnTacacsTimeOut_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_SnTacacsTimeOut_Type.__name__=_C
_SnTacacsTimeOut_Object=MibScalar
snTacacsTimeOut=_SnTacacsTimeOut_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,1,2),_SnTacacsTimeOut_Type())
snTacacsTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsTimeOut.setStatus(_A)
class _SnTacacsDeadTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SnTacacsDeadTime_Type.__name__=_C
_SnTacacsDeadTime_Object=MibScalar
snTacacsDeadTime=_SnTacacsDeadTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,1,3),_SnTacacsDeadTime_Type())
snTacacsDeadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsDeadTime.setStatus(_A)
class _SnTacacsKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnTacacsKey_Type.__name__=_N
_SnTacacsKey_Object=MibScalar
snTacacsKey=_SnTacacsKey_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,1,4),_SnTacacsKey_Type())
snTacacsKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsKey.setStatus(_A)
class _SnTacacsSNMPAccess_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnTacacsSNMPAccess_Type.__name__=_C
_SnTacacsSNMPAccess_Object=MibScalar
snTacacsSNMPAccess=_SnTacacsSNMPAccess_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,1,5),_SnTacacsSNMPAccess_Type())
snTacacsSNMPAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:snTacacsSNMPAccess.setStatus(_A)
_SnTacacsServerTable_Object=MibTable
snTacacsServerTable=_SnTacacsServerTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2))
if mibBuilder.loadTexts:snTacacsServerTable.setStatus(_A)
_SnTacacsServerEntry_Object=MibTableRow
snTacacsServerEntry=_SnTacacsServerEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2,1))
snTacacsServerEntry.setIndexNames((0,_F,_AI))
if mibBuilder.loadTexts:snTacacsServerEntry.setStatus(_A)
_SnTacacsServerIp_Type=IpAddress
_SnTacacsServerIp_Object=MibTableColumn
snTacacsServerIp=_SnTacacsServerIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2,1,1),_SnTacacsServerIp_Type())
snTacacsServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:snTacacsServerIp.setStatus(_A)
class _SnTacacsServerAuthPort_Type(Integer32):defaultValue=49
_SnTacacsServerAuthPort_Type.__name__=_C
_SnTacacsServerAuthPort_Object=MibTableColumn
snTacacsServerAuthPort=_SnTacacsServerAuthPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2,1,2),_SnTacacsServerAuthPort_Type())
snTacacsServerAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsServerAuthPort.setStatus(_A)
class _SnTacacsServerRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnTacacsServerRowStatus_Type.__name__=_C
_SnTacacsServerRowStatus_Object=MibTableColumn
snTacacsServerRowStatus=_SnTacacsServerRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2,1,3),_SnTacacsServerRowStatus_Type())
snTacacsServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsServerRowStatus.setStatus(_A)
class _SnTacacsServerRowKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnTacacsServerRowKey_Type.__name__=_N
_SnTacacsServerRowKey_Object=MibTableColumn
snTacacsServerRowKey=_SnTacacsServerRowKey_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2,1,4),_SnTacacsServerRowKey_Type())
snTacacsServerRowKey.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsServerRowKey.setStatus(_A)
class _SnTacacsServerUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_AF,2),(_AG,3),(_AH,4)))
_SnTacacsServerUsage_Type.__name__=_C
_SnTacacsServerUsage_Object=MibTableColumn
snTacacsServerUsage=_SnTacacsServerUsage_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,13,2,1,5),_SnTacacsServerUsage_Type())
snTacacsServerUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:snTacacsServerUsage.setStatus(_A)
_SnQos_ObjectIdentity=ObjectIdentity
snQos=_SnQos_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14))
_SnQosProfileTable_Object=MibTable
snQosProfileTable=_SnQosProfileTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,1))
if mibBuilder.loadTexts:snQosProfileTable.setStatus(_A)
_SnQosProfileEntry_Object=MibTableRow
snQosProfileEntry=_SnQosProfileEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,1,1))
snQosProfileEntry.setIndexNames((0,_F,_AJ))
if mibBuilder.loadTexts:snQosProfileEntry.setStatus(_A)
class _SnQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SnQosProfileIndex_Type.__name__=_C
_SnQosProfileIndex_Object=MibTableColumn
snQosProfileIndex=_SnQosProfileIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,1,1,1),_SnQosProfileIndex_Type())
snQosProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snQosProfileIndex.setStatus(_A)
class _SnQosProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnQosProfileName_Type.__name__=_N
_SnQosProfileName_Object=MibTableColumn
snQosProfileName=_SnQosProfileName_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,1,1,2),_SnQosProfileName_Type())
snQosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:snQosProfileName.setStatus(_A)
class _SnQosProfileRequestedBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SnQosProfileRequestedBandwidth_Type.__name__=_C
_SnQosProfileRequestedBandwidth_Object=MibTableColumn
snQosProfileRequestedBandwidth=_SnQosProfileRequestedBandwidth_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,1,1,3),_SnQosProfileRequestedBandwidth_Type())
snQosProfileRequestedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:snQosProfileRequestedBandwidth.setStatus(_A)
class _SnQosProfileCalculatedBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SnQosProfileCalculatedBandwidth_Type.__name__=_C
_SnQosProfileCalculatedBandwidth_Object=MibTableColumn
snQosProfileCalculatedBandwidth=_SnQosProfileCalculatedBandwidth_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,1,1,4),_SnQosProfileCalculatedBandwidth_Type())
snQosProfileCalculatedBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:snQosProfileCalculatedBandwidth.setStatus(_A)
_SnQosBindTable_Object=MibTable
snQosBindTable=_SnQosBindTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,2))
if mibBuilder.loadTexts:snQosBindTable.setStatus(_A)
_SnQosBindEntry_Object=MibTableRow
snQosBindEntry=_SnQosBindEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,2,1))
snQosBindEntry.setIndexNames((0,_F,_AK))
if mibBuilder.loadTexts:snQosBindEntry.setStatus(_A)
class _SnQosBindIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SnQosBindIndex_Type.__name__=_C
_SnQosBindIndex_Object=MibTableColumn
snQosBindIndex=_SnQosBindIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,2,1,1),_SnQosBindIndex_Type())
snQosBindIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snQosBindIndex.setStatus(_A)
_SnQosBindPriority_Type=Integer32
_SnQosBindPriority_Object=MibTableColumn
snQosBindPriority=_SnQosBindPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,2,1,2),_SnQosBindPriority_Type())
snQosBindPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snQosBindPriority.setStatus(_A)
class _SnQosBindProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SnQosBindProfileIndex_Type.__name__=_C
_SnQosBindProfileIndex_Object=MibTableColumn
snQosBindProfileIndex=_SnQosBindProfileIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,14,2,1,3),_SnQosBindProfileIndex_Type())
snQosBindProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snQosBindProfileIndex.setStatus(_A)
_SnAAA_ObjectIdentity=ObjectIdentity
snAAA=_SnAAA_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15))
_SnAuthentication_ObjectIdentity=ObjectIdentity
snAuthentication=_SnAuthentication_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,1))
_SnAuthorization_ObjectIdentity=ObjectIdentity
snAuthorization=_SnAuthorization_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,2))
class _SnAuthorizationCommandMethods_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SnAuthorizationCommandMethods_Type.__name__=_I
_SnAuthorizationCommandMethods_Object=MibScalar
snAuthorizationCommandMethods=_SnAuthorizationCommandMethods_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,2,1),_SnAuthorizationCommandMethods_Type())
snAuthorizationCommandMethods.setMaxAccess(_B)
if mibBuilder.loadTexts:snAuthorizationCommandMethods.setStatus(_A)
class _SnAuthorizationCommandLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,5)));namedValues=NamedValues(*((_Q,0),(_R,4),(_S,5)))
_SnAuthorizationCommandLevel_Type.__name__=_C
_SnAuthorizationCommandLevel_Object=MibScalar
snAuthorizationCommandLevel=_SnAuthorizationCommandLevel_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,2,2),_SnAuthorizationCommandLevel_Type())
snAuthorizationCommandLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:snAuthorizationCommandLevel.setStatus(_A)
class _SnAuthorizationExec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SnAuthorizationExec_Type.__name__=_I
_SnAuthorizationExec_Object=MibScalar
snAuthorizationExec=_SnAuthorizationExec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,2,3),_SnAuthorizationExec_Type())
snAuthorizationExec.setMaxAccess(_B)
if mibBuilder.loadTexts:snAuthorizationExec.setStatus(_A)
_SnAccounting_ObjectIdentity=ObjectIdentity
snAccounting=_SnAccounting_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,3))
class _SnAccountingCommandMethods_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SnAccountingCommandMethods_Type.__name__=_I
_SnAccountingCommandMethods_Object=MibScalar
snAccountingCommandMethods=_SnAccountingCommandMethods_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,3,1),_SnAccountingCommandMethods_Type())
snAccountingCommandMethods.setMaxAccess(_B)
if mibBuilder.loadTexts:snAccountingCommandMethods.setStatus(_A)
class _SnAccountingCommandLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,5)));namedValues=NamedValues(*((_Q,0),(_R,4),(_S,5)))
_SnAccountingCommandLevel_Type.__name__=_C
_SnAccountingCommandLevel_Object=MibScalar
snAccountingCommandLevel=_SnAccountingCommandLevel_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,3,2),_SnAccountingCommandLevel_Type())
snAccountingCommandLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:snAccountingCommandLevel.setStatus(_A)
class _SnAccountingExec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SnAccountingExec_Type.__name__=_I
_SnAccountingExec_Object=MibScalar
snAccountingExec=_SnAccountingExec_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,3,3),_SnAccountingExec_Type())
snAccountingExec.setMaxAccess(_B)
if mibBuilder.loadTexts:snAccountingExec.setStatus(_A)
class _SnAccountingSystem_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SnAccountingSystem_Type.__name__=_I
_SnAccountingSystem_Object=MibScalar
snAccountingSystem=_SnAccountingSystem_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,15,3,4),_SnAccountingSystem_Type())
snAccountingSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:snAccountingSystem.setStatus(_A)
_SnCAR_ObjectIdentity=ObjectIdentity
snCAR=_SnCAR_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,16))
_SnVLanCAR_ObjectIdentity=ObjectIdentity
snVLanCAR=_SnVLanCAR_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,17))
_SnNetFlow_ObjectIdentity=ObjectIdentity
snNetFlow=_SnNetFlow_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18))
_SnNetFlowGlb_ObjectIdentity=ObjectIdentity
snNetFlowGlb=_SnNetFlowGlb_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,1))
class _SnNetFlowGblEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnNetFlowGblEnable_Type.__name__=_C
_SnNetFlowGblEnable_Object=MibScalar
snNetFlowGblEnable=_SnNetFlowGblEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,1,1),_SnNetFlowGblEnable_Type())
snNetFlowGblEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowGblEnable.setStatus(_A)
class _SnNetFlowGblVersion_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('version1',1),('version5',5)))
_SnNetFlowGblVersion_Type.__name__=_C
_SnNetFlowGblVersion_Object=MibScalar
snNetFlowGblVersion=_SnNetFlowGblVersion_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,1,2),_SnNetFlowGblVersion_Type())
snNetFlowGblVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowGblVersion.setStatus(_A)
class _SnNetFlowGblProtocolDisable_Type(Integer32):defaultValue=0
_SnNetFlowGblProtocolDisable_Type.__name__=_C
_SnNetFlowGblProtocolDisable_Object=MibScalar
snNetFlowGblProtocolDisable=_SnNetFlowGblProtocolDisable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,1,3),_SnNetFlowGblProtocolDisable_Type())
snNetFlowGblProtocolDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowGblProtocolDisable.setStatus(_A)
class _SnNetFlowGblActiveTimeout_Type(Integer32):defaultValue=60
_SnNetFlowGblActiveTimeout_Type.__name__=_C
_SnNetFlowGblActiveTimeout_Object=MibScalar
snNetFlowGblActiveTimeout=_SnNetFlowGblActiveTimeout_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,1,4),_SnNetFlowGblActiveTimeout_Type())
snNetFlowGblActiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowGblActiveTimeout.setStatus(_A)
class _SnNetFlowGblInactiveTimeout_Type(Integer32):defaultValue=60
_SnNetFlowGblInactiveTimeout_Type.__name__=_C
_SnNetFlowGblInactiveTimeout_Object=MibScalar
snNetFlowGblInactiveTimeout=_SnNetFlowGblInactiveTimeout_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,1,5),_SnNetFlowGblInactiveTimeout_Type())
snNetFlowGblInactiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowGblInactiveTimeout.setStatus(_A)
_SnNetFlowCollectorTable_Object=MibTable
snNetFlowCollectorTable=_SnNetFlowCollectorTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2))
if mibBuilder.loadTexts:snNetFlowCollectorTable.setStatus(_A)
_SnNetFlowCollectorEntry_Object=MibTableRow
snNetFlowCollectorEntry=_SnNetFlowCollectorEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2,1))
snNetFlowCollectorEntry.setIndexNames((0,_F,_AL))
if mibBuilder.loadTexts:snNetFlowCollectorEntry.setStatus(_A)
class _SnNetFlowCollectorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SnNetFlowCollectorIndex_Type.__name__=_C
_SnNetFlowCollectorIndex_Object=MibTableColumn
snNetFlowCollectorIndex=_SnNetFlowCollectorIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2,1,1),_SnNetFlowCollectorIndex_Type())
snNetFlowCollectorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snNetFlowCollectorIndex.setStatus(_A)
_SnNetFlowCollectorIp_Type=IpAddress
_SnNetFlowCollectorIp_Object=MibTableColumn
snNetFlowCollectorIp=_SnNetFlowCollectorIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2,1,2),_SnNetFlowCollectorIp_Type())
snNetFlowCollectorIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowCollectorIp.setStatus(_A)
_SnNetFlowCollectorUdpPort_Type=Integer32
_SnNetFlowCollectorUdpPort_Object=MibTableColumn
snNetFlowCollectorUdpPort=_SnNetFlowCollectorUdpPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2,1,3),_SnNetFlowCollectorUdpPort_Type())
snNetFlowCollectorUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowCollectorUdpPort.setStatus(_A)
_SnNetFlowCollectorSourceInterface_Type=Integer32
_SnNetFlowCollectorSourceInterface_Object=MibTableColumn
snNetFlowCollectorSourceInterface=_SnNetFlowCollectorSourceInterface_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2,1,4),_SnNetFlowCollectorSourceInterface_Type())
snNetFlowCollectorSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowCollectorSourceInterface.setStatus(_A)
class _SnNetFlowCollectorRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnNetFlowCollectorRowStatus_Type.__name__=_C
_SnNetFlowCollectorRowStatus_Object=MibTableColumn
snNetFlowCollectorRowStatus=_SnNetFlowCollectorRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,2,1,5),_SnNetFlowCollectorRowStatus_Type())
snNetFlowCollectorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowCollectorRowStatus.setStatus(_A)
_SnNetFlowAggregationTable_Object=MibTable
snNetFlowAggregationTable=_SnNetFlowAggregationTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3))
if mibBuilder.loadTexts:snNetFlowAggregationTable.setStatus(_A)
_SnNetFlowAggregationEntry_Object=MibTableRow
snNetFlowAggregationEntry=_SnNetFlowAggregationEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1))
snNetFlowAggregationEntry.setIndexNames((0,_F,_AM))
if mibBuilder.loadTexts:snNetFlowAggregationEntry.setStatus(_A)
class _SnNetFlowAggregationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('as',1),('protocolPort',2),('destPrefix',3),('sourcePrefix',4),('prefix',5)))
_SnNetFlowAggregationIndex_Type.__name__=_C
_SnNetFlowAggregationIndex_Object=MibTableColumn
snNetFlowAggregationIndex=_SnNetFlowAggregationIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,1),_SnNetFlowAggregationIndex_Type())
snNetFlowAggregationIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snNetFlowAggregationIndex.setStatus(_A)
_SnNetFlowAggregationIp_Type=IpAddress
_SnNetFlowAggregationIp_Object=MibTableColumn
snNetFlowAggregationIp=_SnNetFlowAggregationIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,2),_SnNetFlowAggregationIp_Type())
snNetFlowAggregationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationIp.setStatus(_A)
_SnNetFlowAggregationUdpPort_Type=Integer32
_SnNetFlowAggregationUdpPort_Object=MibTableColumn
snNetFlowAggregationUdpPort=_SnNetFlowAggregationUdpPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,3),_SnNetFlowAggregationUdpPort_Type())
snNetFlowAggregationUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationUdpPort.setStatus(_A)
_SnNetFlowAggregationSourceInterface_Type=Integer32
_SnNetFlowAggregationSourceInterface_Object=MibTableColumn
snNetFlowAggregationSourceInterface=_SnNetFlowAggregationSourceInterface_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,4),_SnNetFlowAggregationSourceInterface_Type())
snNetFlowAggregationSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationSourceInterface.setStatus(_A)
_SnNetFlowAggregationNumberOfCacheEntries_Type=Integer32
_SnNetFlowAggregationNumberOfCacheEntries_Object=MibTableColumn
snNetFlowAggregationNumberOfCacheEntries=_SnNetFlowAggregationNumberOfCacheEntries_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,5),_SnNetFlowAggregationNumberOfCacheEntries_Type())
snNetFlowAggregationNumberOfCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationNumberOfCacheEntries.setStatus(_A)
_SnNetFlowAggregationActiveTimeout_Type=Integer32
_SnNetFlowAggregationActiveTimeout_Object=MibTableColumn
snNetFlowAggregationActiveTimeout=_SnNetFlowAggregationActiveTimeout_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,6),_SnNetFlowAggregationActiveTimeout_Type())
snNetFlowAggregationActiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationActiveTimeout.setStatus(_A)
_SnNetFlowAggregationInactiveTimeout_Type=Integer32
_SnNetFlowAggregationInactiveTimeout_Object=MibTableColumn
snNetFlowAggregationInactiveTimeout=_SnNetFlowAggregationInactiveTimeout_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,7),_SnNetFlowAggregationInactiveTimeout_Type())
snNetFlowAggregationInactiveTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationInactiveTimeout.setStatus(_A)
class _SnNetFlowAggregationEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnNetFlowAggregationEnable_Type.__name__=_C
_SnNetFlowAggregationEnable_Object=MibTableColumn
snNetFlowAggregationEnable=_SnNetFlowAggregationEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,8),_SnNetFlowAggregationEnable_Type())
snNetFlowAggregationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationEnable.setStatus(_A)
class _SnNetFlowAggregationRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4)))
_SnNetFlowAggregationRowStatus_Type.__name__=_C
_SnNetFlowAggregationRowStatus_Object=MibTableColumn
snNetFlowAggregationRowStatus=_SnNetFlowAggregationRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,3,1,9),_SnNetFlowAggregationRowStatus_Type())
snNetFlowAggregationRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowAggregationRowStatus.setStatus(_A)
_SnNetFlowIfTable_Object=MibTable
snNetFlowIfTable=_SnNetFlowIfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,4))
if mibBuilder.loadTexts:snNetFlowIfTable.setStatus(_A)
_SnNetFlowIfEntry_Object=MibTableRow
snNetFlowIfEntry=_SnNetFlowIfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,4,1))
snNetFlowIfEntry.setIndexNames((0,_F,_AN))
if mibBuilder.loadTexts:snNetFlowIfEntry.setStatus(_A)
class _SnNetFlowIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_SnNetFlowIfIndex_Type.__name__=_C
_SnNetFlowIfIndex_Object=MibTableColumn
snNetFlowIfIndex=_SnNetFlowIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,4,1,1),_SnNetFlowIfIndex_Type())
snNetFlowIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snNetFlowIfIndex.setStatus(_A)
class _SnNetFlowIfFlowSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnNetFlowIfFlowSwitching_Type.__name__=_C
_SnNetFlowIfFlowSwitching_Object=MibTableColumn
snNetFlowIfFlowSwitching=_SnNetFlowIfFlowSwitching_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,18,4,1,2),_SnNetFlowIfFlowSwitching_Type())
snNetFlowIfFlowSwitching.setMaxAccess(_B)
if mibBuilder.loadTexts:snNetFlowIfFlowSwitching.setStatus(_A)
_SnSFlow_ObjectIdentity=ObjectIdentity
snSFlow=_SnSFlow_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19))
_SnSFlowGlb_ObjectIdentity=ObjectIdentity
snSFlowGlb=_SnSFlowGlb_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,1))
_SnSflowCollectorTable_Object=MibTable
snSflowCollectorTable=_SnSflowCollectorTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,2))
if mibBuilder.loadTexts:snSflowCollectorTable.setStatus(_A)
_SnSflowCollectorEntry_Object=MibTableRow
snSflowCollectorEntry=_SnSflowCollectorEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,2,1))
snSflowCollectorEntry.setIndexNames((0,_F,_AO))
if mibBuilder.loadTexts:snSflowCollectorEntry.setStatus(_A)
_SnSflowCollectorIndex_Type=Integer32
_SnSflowCollectorIndex_Object=MibTableColumn
snSflowCollectorIndex=_SnSflowCollectorIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,2,1,1),_SnSflowCollectorIndex_Type())
snSflowCollectorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snSflowCollectorIndex.setStatus(_A)
_SnSflowCollectorIP_Type=IpAddress
_SnSflowCollectorIP_Object=MibTableColumn
snSflowCollectorIP=_SnSflowCollectorIP_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,2,1,2),_SnSflowCollectorIP_Type())
snSflowCollectorIP.setMaxAccess(_B)
if mibBuilder.loadTexts:snSflowCollectorIP.setStatus(_A)
_SnSflowCollectorUDPPort_Type=Integer32
_SnSflowCollectorUDPPort_Object=MibTableColumn
snSflowCollectorUDPPort=_SnSflowCollectorUDPPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,2,1,3),_SnSflowCollectorUDPPort_Type())
snSflowCollectorUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snSflowCollectorUDPPort.setStatus(_A)
class _SnSflowCollectorRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noSuch',0),(_J,1),(_K,2),(_L,3),(_M,4),(_O,5)))
_SnSflowCollectorRowStatus_Type.__name__=_C
_SnSflowCollectorRowStatus_Object=MibTableColumn
snSflowCollectorRowStatus=_SnSflowCollectorRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,19,2,1,4),_SnSflowCollectorRowStatus_Type())
snSflowCollectorRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snSflowCollectorRowStatus.setStatus(_A)
_SnFDP_ObjectIdentity=ObjectIdentity
snFDP=_SnFDP_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20))
_SnFdpMIBObjects_ObjectIdentity=ObjectIdentity
snFdpMIBObjects=_SnFdpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1))
_SnFdpInterface_ObjectIdentity=ObjectIdentity
snFdpInterface=_SnFdpInterface_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,1))
_SnFdpInterfaceTable_Object=MibTable
snFdpInterfaceTable=_SnFdpInterfaceTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,1,1))
if mibBuilder.loadTexts:snFdpInterfaceTable.setStatus(_A)
_SnFdpInterfaceEntry_Object=MibTableRow
snFdpInterfaceEntry=_SnFdpInterfaceEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,1,1,1))
snFdpInterfaceEntry.setIndexNames((0,_F,_AP))
if mibBuilder.loadTexts:snFdpInterfaceEntry.setStatus(_A)
_SnFdpInterfaceIfIndex_Type=Integer32
_SnFdpInterfaceIfIndex_Object=MibTableColumn
snFdpInterfaceIfIndex=_SnFdpInterfaceIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,1,1,1,1),_SnFdpInterfaceIfIndex_Type())
snFdpInterfaceIfIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:snFdpInterfaceIfIndex.setStatus(_A)
class _SnFdpInterfaceFdpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_SnFdpInterfaceFdpEnable_Type.__name__=_C
_SnFdpInterfaceFdpEnable_Object=MibTableColumn
snFdpInterfaceFdpEnable=_SnFdpInterfaceFdpEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,1,1,1,2),_SnFdpInterfaceFdpEnable_Type())
snFdpInterfaceFdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdpInterfaceFdpEnable.setStatus(_A)
class _SnFdpInterfaceCdpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_SnFdpInterfaceCdpEnable_Type.__name__=_C
_SnFdpInterfaceCdpEnable_Object=MibTableColumn
snFdpInterfaceCdpEnable=_SnFdpInterfaceCdpEnable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,1,1,1,3),_SnFdpInterfaceCdpEnable_Type())
snFdpInterfaceCdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdpInterfaceCdpEnable.setStatus(_A)
_SnFdpCache_ObjectIdentity=ObjectIdentity
snFdpCache=_SnFdpCache_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2))
_SnFdpCacheTable_Object=MibTable
snFdpCacheTable=_SnFdpCacheTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1))
if mibBuilder.loadTexts:snFdpCacheTable.setStatus(_A)
_SnFdpCacheEntry_Object=MibTableRow
snFdpCacheEntry=_SnFdpCacheEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1))
snFdpCacheEntry.setIndexNames((0,_F,_AQ),(0,_F,_AR))
if mibBuilder.loadTexts:snFdpCacheEntry.setStatus(_A)
_SnFdpCacheIfIndex_Type=Integer32
_SnFdpCacheIfIndex_Object=MibTableColumn
snFdpCacheIfIndex=_SnFdpCacheIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,1),_SnFdpCacheIfIndex_Type())
snFdpCacheIfIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:snFdpCacheIfIndex.setStatus(_A)
_SnFdpCacheDeviceIndex_Type=Integer32
_SnFdpCacheDeviceIndex_Object=MibTableColumn
snFdpCacheDeviceIndex=_SnFdpCacheDeviceIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,2),_SnFdpCacheDeviceIndex_Type())
snFdpCacheDeviceIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:snFdpCacheDeviceIndex.setStatus(_A)
_SnFdpCacheDeviceId_Type=DisplayString
_SnFdpCacheDeviceId_Object=MibTableColumn
snFdpCacheDeviceId=_SnFdpCacheDeviceId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,3),_SnFdpCacheDeviceId_Type())
snFdpCacheDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheDeviceId.setStatus(_A)
class _SnFdpCacheAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip',1),(_c,2),(_AS,3)))
_SnFdpCacheAddressType_Type.__name__=_C
_SnFdpCacheAddressType_Object=MibTableColumn
snFdpCacheAddressType=_SnFdpCacheAddressType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,4),_SnFdpCacheAddressType_Type())
snFdpCacheAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheAddressType.setStatus(_A)
_SnFdpCacheAddress_Type=OctetString
_SnFdpCacheAddress_Object=MibTableColumn
snFdpCacheAddress=_SnFdpCacheAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,5),_SnFdpCacheAddress_Type())
snFdpCacheAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheAddress.setStatus(_A)
_SnFdpCacheVersion_Type=DisplayString
_SnFdpCacheVersion_Object=MibTableColumn
snFdpCacheVersion=_SnFdpCacheVersion_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,6),_SnFdpCacheVersion_Type())
snFdpCacheVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheVersion.setStatus(_A)
_SnFdpCacheDevicePort_Type=DisplayString
_SnFdpCacheDevicePort_Object=MibTableColumn
snFdpCacheDevicePort=_SnFdpCacheDevicePort_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,7),_SnFdpCacheDevicePort_Type())
snFdpCacheDevicePort.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheDevicePort.setStatus(_A)
_SnFdpCachePlatform_Type=DisplayString
_SnFdpCachePlatform_Object=MibTableColumn
snFdpCachePlatform=_SnFdpCachePlatform_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,8),_SnFdpCachePlatform_Type())
snFdpCachePlatform.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCachePlatform.setStatus(_A)
_SnFdpCacheCapabilities_Type=DisplayString
_SnFdpCacheCapabilities_Object=MibTableColumn
snFdpCacheCapabilities=_SnFdpCacheCapabilities_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,9),_SnFdpCacheCapabilities_Type())
snFdpCacheCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheCapabilities.setStatus(_A)
class _SnFdpCacheVendorId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fdp',1),('cdp',2)))
_SnFdpCacheVendorId_Type.__name__=_C
_SnFdpCacheVendorId_Object=MibTableColumn
snFdpCacheVendorId=_SnFdpCacheVendorId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,10),_SnFdpCacheVendorId_Type())
snFdpCacheVendorId.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheVendorId.setStatus(_A)
class _SnFdpCacheIsAggregateVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_SnFdpCacheIsAggregateVlan_Type.__name__=_C
_SnFdpCacheIsAggregateVlan_Object=MibTableColumn
snFdpCacheIsAggregateVlan=_SnFdpCacheIsAggregateVlan_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,11),_SnFdpCacheIsAggregateVlan_Type())
snFdpCacheIsAggregateVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheIsAggregateVlan.setStatus(_A)
_SnFdpCacheTagType_Type=Integer32
_SnFdpCacheTagType_Object=MibTableColumn
snFdpCacheTagType=_SnFdpCacheTagType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,12),_SnFdpCacheTagType_Type())
snFdpCacheTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheTagType.setStatus(_A)
_SnFdpCachePortVlanMask_Type=OctetString
_SnFdpCachePortVlanMask_Object=MibTableColumn
snFdpCachePortVlanMask=_SnFdpCachePortVlanMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,13),_SnFdpCachePortVlanMask_Type())
snFdpCachePortVlanMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCachePortVlanMask.setStatus(_A)
class _SnFdpCachePortTagMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('untagged',1),('tagged',2),('dual',3)))
_SnFdpCachePortTagMode_Type.__name__=_C
_SnFdpCachePortTagMode_Object=MibTableColumn
snFdpCachePortTagMode=_SnFdpCachePortTagMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,14),_SnFdpCachePortTagMode_Type())
snFdpCachePortTagMode.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCachePortTagMode.setStatus(_A)
_SnFdpCacheDefaultTrafficeVlanIdForDualMode_Type=Integer32
_SnFdpCacheDefaultTrafficeVlanIdForDualMode_Object=MibTableColumn
snFdpCacheDefaultTrafficeVlanIdForDualMode=_SnFdpCacheDefaultTrafficeVlanIdForDualMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,2,1,1,15),_SnFdpCacheDefaultTrafficeVlanIdForDualMode_Type())
snFdpCacheDefaultTrafficeVlanIdForDualMode.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCacheDefaultTrafficeVlanIdForDualMode.setStatus(_A)
_SnFdpGlobal_ObjectIdentity=ObjectIdentity
snFdpGlobal=_SnFdpGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,3))
class _SnFdpGlobalRun_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_SnFdpGlobalRun_Type.__name__=_C
_SnFdpGlobalRun_Object=MibScalar
snFdpGlobalRun=_SnFdpGlobalRun_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,3,1),_SnFdpGlobalRun_Type())
snFdpGlobalRun.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdpGlobalRun.setStatus(_A)
class _SnFdpGlobalMessageInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,900))
_SnFdpGlobalMessageInterval_Type.__name__=_C
_SnFdpGlobalMessageInterval_Object=MibScalar
snFdpGlobalMessageInterval=_SnFdpGlobalMessageInterval_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,3,2),_SnFdpGlobalMessageInterval_Type())
snFdpGlobalMessageInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdpGlobalMessageInterval.setStatus(_A)
class _SnFdpGlobalHoldTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_SnFdpGlobalHoldTime_Type.__name__=_C
_SnFdpGlobalHoldTime_Object=MibScalar
snFdpGlobalHoldTime=_SnFdpGlobalHoldTime_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,3,3),_SnFdpGlobalHoldTime_Type())
snFdpGlobalHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdpGlobalHoldTime.setStatus(_A)
class _SnFdpGlobalCdpRun_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_SnFdpGlobalCdpRun_Type.__name__=_C
_SnFdpGlobalCdpRun_Object=MibScalar
snFdpGlobalCdpRun=_SnFdpGlobalCdpRun_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,3,4),_SnFdpGlobalCdpRun_Type())
snFdpGlobalCdpRun.setMaxAccess(_B)
if mibBuilder.loadTexts:snFdpGlobalCdpRun.setStatus(_A)
_SnFdpCachedAddr_ObjectIdentity=ObjectIdentity
snFdpCachedAddr=_SnFdpCachedAddr_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4))
_SnFdpCachedAddressTable_Object=MibTable
snFdpCachedAddressTable=_SnFdpCachedAddressTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1))
if mibBuilder.loadTexts:snFdpCachedAddressTable.setStatus(_A)
_SnFdpCachedAddressEntry_Object=MibTableRow
snFdpCachedAddressEntry=_SnFdpCachedAddressEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1,1))
snFdpCachedAddressEntry.setIndexNames((0,_F,_AT),(0,_F,_AU),(0,_F,_AV))
if mibBuilder.loadTexts:snFdpCachedAddressEntry.setStatus(_A)
_SnFdpCachedAddrIfIndex_Type=Integer32
_SnFdpCachedAddrIfIndex_Object=MibTableColumn
snFdpCachedAddrIfIndex=_SnFdpCachedAddrIfIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1,1,1),_SnFdpCachedAddrIfIndex_Type())
snFdpCachedAddrIfIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:snFdpCachedAddrIfIndex.setStatus(_A)
_SnFdpCachedAddrDeviceIndex_Type=Integer32
_SnFdpCachedAddrDeviceIndex_Object=MibTableColumn
snFdpCachedAddrDeviceIndex=_SnFdpCachedAddrDeviceIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1,1,2),_SnFdpCachedAddrDeviceIndex_Type())
snFdpCachedAddrDeviceIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:snFdpCachedAddrDeviceIndex.setStatus(_A)
_SnFdpCachedAddrDeviceAddrEntryIndex_Type=Integer32
_SnFdpCachedAddrDeviceAddrEntryIndex_Object=MibTableColumn
snFdpCachedAddrDeviceAddrEntryIndex=_SnFdpCachedAddrDeviceAddrEntryIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1,1,3),_SnFdpCachedAddrDeviceAddrEntryIndex_Type())
snFdpCachedAddrDeviceAddrEntryIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:snFdpCachedAddrDeviceAddrEntryIndex.setStatus(_A)
class _SnFdpCachedAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip',1),(_c,2),(_AS,3)))
_SnFdpCachedAddrType_Type.__name__=_C
_SnFdpCachedAddrType_Object=MibTableColumn
snFdpCachedAddrType=_SnFdpCachedAddrType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1,1,4),_SnFdpCachedAddrType_Type())
snFdpCachedAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCachedAddrType.setStatus(_A)
_SnFdpCachedAddrValue_Type=OctetString
_SnFdpCachedAddrValue_Object=MibTableColumn
snFdpCachedAddrValue=_SnFdpCachedAddrValue_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,20,1,4,1,1,5),_SnFdpCachedAddrValue_Type())
snFdpCachedAddrValue.setMaxAccess(_D)
if mibBuilder.loadTexts:snFdpCachedAddrValue.setStatus(_A)
_SnVsrp_ObjectIdentity=ObjectIdentity
snVsrp=_SnVsrp_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21))
mibBuilder.exportSymbols(_F,**{_N:DisplayString,_e:PhysAddress,'MacAddress':MacAddress,'BridgeId':BridgeId,'Timeout':Timeout,'PortMask':PortMask,'InterfaceId':InterfaceId,'snSwInfo':snSwInfo,'snSwGroupOperMode':snSwGroupOperMode,'snSwGroupIpL3SwMode':snSwGroupIpL3SwMode,'snSwGroupIpMcastMode':snSwGroupIpMcastMode,'snSwGroupDefaultCfgMode':snSwGroupDefaultCfgMode,'snSwGroupSwitchAgeTime':snSwGroupSwitchAgeTime,'snVLanGroupVlanCurEntry':snVLanGroupVlanCurEntry,'snVLanGroupSetAllVLan':snVLanGroupSetAllVLan,'snSwPortSetAll':snSwPortSetAll,'snFdbTableCurEntry':snFdbTableCurEntry,'snFdbTableStationFlush':snFdbTableStationFlush,'snPortStpSetAll':snPortStpSetAll,'snSwProbePortNum':snSwProbePortNum,'snSw8021qTagMode':snSw8021qTagMode,'snSwGlobalStpMode':snSwGlobalStpMode,'snSwIpMcastQuerierMode':snSwIpMcastQuerierMode,'snSwViolatorPortNumber':snSwViolatorPortNumber,'snSwViolatorMacAddress':snSwViolatorMacAddress,'snVLanGroupVlanMaxEntry':snVLanGroupVlanMaxEntry,'snSwEosBufferSize':snSwEosBufferSize,'snVLanByPortEntrySize':snVLanByPortEntrySize,'snSwPortEntrySize':snSwPortEntrySize,'snFdbStationEntrySize':snFdbStationEntrySize,'snPortStpEntrySize':snPortStpEntrySize,'snSwEnableBridgeNewRootTrap':snSwEnableBridgeNewRootTrap,'snSwEnableBridgeTopoChangeTrap':snSwEnableBridgeTopoChangeTrap,'snSwEnableLockedAddrViolationTrap':snSwEnableLockedAddrViolationTrap,'snSwIpxL3SwMode':snSwIpxL3SwMode,'snVLanByIpSubnetMaxSubnets':snVLanByIpSubnetMaxSubnets,'snVLanByIpxNetMaxNetworks':snVLanByIpxNetMaxNetworks,'snSwProtocolVLanMode':snSwProtocolVLanMode,'snMacStationVLanId':snMacStationVLanId,'snSwClearCounters':snSwClearCounters,'snSw8021qTagType':snSw8021qTagType,'snSwBroadcastLimit':snSwBroadcastLimit,'snSwMaxMacFilterPerSystem':snSwMaxMacFilterPerSystem,'snSwMaxMacFilterPerPort':snSwMaxMacFilterPerPort,'snSwDefaultVLanId':snSwDefaultVLanId,'snSwGlobalAutoNegotiate':snSwGlobalAutoNegotiate,'snSwQosMechanism':snSwQosMechanism,'snSwSingleStpMode':snSwSingleStpMode,'snSwFastStpMode':snSwFastStpMode,'snVLanInfo':snVLanInfo,'snVLanByPortTable':snVLanByPortTable,'snVLanByPortEntry':snVLanByPortEntry,_g:snVLanByPortVLanIndex,'snVLanByPortVLanId':snVLanByPortVLanId,'snVLanByPortPortMask':snVLanByPortPortMask,'snVLanByPortQos':snVLanByPortQos,'snVLanByPortStpMode':snVLanByPortStpMode,'snVLanByPortStpPriority':snVLanByPortStpPriority,'snVLanByPortStpGroupMaxAge':snVLanByPortStpGroupMaxAge,'snVLanByPortStpGroupHelloTime':snVLanByPortStpGroupHelloTime,'snVLanByPortStpGroupForwardDelay':snVLanByPortStpGroupForwardDelay,'snVLanByPortRowStatus':snVLanByPortRowStatus,'snVLanByPortOperState':snVLanByPortOperState,'snVLanByPortBaseNumPorts':snVLanByPortBaseNumPorts,'snVLanByPortBaseType':snVLanByPortBaseType,'snVLanByPortStpProtocolSpecification':snVLanByPortStpProtocolSpecification,'snVLanByPortStpMaxAge':snVLanByPortStpMaxAge,'snVLanByPortStpHelloTime':snVLanByPortStpHelloTime,'snVLanByPortStpHoldTime':snVLanByPortStpHoldTime,'snVLanByPortStpForwardDelay':snVLanByPortStpForwardDelay,'snVLanByPortStpTimeSinceTopologyChange':snVLanByPortStpTimeSinceTopologyChange,'snVLanByPortStpTopChanges':snVLanByPortStpTopChanges,'snVLanByPortStpRootCost':snVLanByPortStpRootCost,'snVLanByPortStpRootPort':snVLanByPortStpRootPort,'snVLanByPortStpDesignatedRoot':snVLanByPortStpDesignatedRoot,'snVLanByPortBaseBridgeAddress':snVLanByPortBaseBridgeAddress,'snVLanByPortVLanName':snVLanByPortVLanName,'snVLanByPortRouterIntf':snVLanByPortRouterIntf,'snVLanByPortChassisPortMask':snVLanByPortChassisPortMask,'snVLanByPortPortList':snVLanByPortPortList,'snVLanByProtocolTable':snVLanByProtocolTable,'snVLanByProtocolEntry':snVLanByProtocolEntry,_n:snVLanByProtocolVLanId,_o:snVLanByProtocolIndex,'snVLanByProtocolDynamic':snVLanByProtocolDynamic,'snVLanByProtocolStaticMask':snVLanByProtocolStaticMask,'snVLanByProtocolExcludeMask':snVLanByProtocolExcludeMask,'snVLanByProtocolRouterIntf':snVLanByProtocolRouterIntf,'snVLanByProtocolRowStatus':snVLanByProtocolRowStatus,'snVLanByProtocolDynamicMask':snVLanByProtocolDynamicMask,'snVLanByProtocolChassisStaticMask':snVLanByProtocolChassisStaticMask,'snVLanByProtocolChassisExcludeMask':snVLanByProtocolChassisExcludeMask,'snVLanByProtocolChassisDynamicMask':snVLanByProtocolChassisDynamicMask,'snVLanByProtocolVLanName':snVLanByProtocolVLanName,'snVLanByProtocolStaticPortList':snVLanByProtocolStaticPortList,'snVLanByProtocolExcludePortList':snVLanByProtocolExcludePortList,'snVLanByProtocolDynamicPortList':snVLanByProtocolDynamicPortList,'snVLanByIpSubnetTable':snVLanByIpSubnetTable,'snVLanByIpSubnetEntry':snVLanByIpSubnetEntry,_p:snVLanByIpSubnetVLanId,_q:snVLanByIpSubnetIpAddress,_r:snVLanByIpSubnetSubnetMask,'snVLanByIpSubnetDynamic':snVLanByIpSubnetDynamic,'snVLanByIpSubnetStaticMask':snVLanByIpSubnetStaticMask,'snVLanByIpSubnetExcludeMask':snVLanByIpSubnetExcludeMask,'snVLanByIpSubnetRouterIntf':snVLanByIpSubnetRouterIntf,'snVLanByIpSubnetRowStatus':snVLanByIpSubnetRowStatus,'snVLanByIpSubnetDynamicMask':snVLanByIpSubnetDynamicMask,'snVLanByIpSubnetChassisStaticMask':snVLanByIpSubnetChassisStaticMask,'snVLanByIpSubnetChassisExcludeMask':snVLanByIpSubnetChassisExcludeMask,'snVLanByIpSubnetChassisDynamicMask':snVLanByIpSubnetChassisDynamicMask,'snVLanByIpSubnetVLanName':snVLanByIpSubnetVLanName,'snVLanByIpSubnetStaticPortList':snVLanByIpSubnetStaticPortList,'snVLanByIpSubnetExcludePortList':snVLanByIpSubnetExcludePortList,'snVLanByIpSubnetDynamicPortList':snVLanByIpSubnetDynamicPortList,'snVLanByIpxNetTable':snVLanByIpxNetTable,'snVLanByIpxNetEntry':snVLanByIpxNetEntry,_s:snVLanByIpxNetVLanId,_t:snVLanByIpxNetNetworkNum,_u:snVLanByIpxNetFrameType,'snVLanByIpxNetDynamic':snVLanByIpxNetDynamic,'snVLanByIpxNetStaticMask':snVLanByIpxNetStaticMask,'snVLanByIpxNetExcludeMask':snVLanByIpxNetExcludeMask,'snVLanByIpxNetRouterIntf':snVLanByIpxNetRouterIntf,'snVLanByIpxNetRowStatus':snVLanByIpxNetRowStatus,'snVLanByIpxNetDynamicMask':snVLanByIpxNetDynamicMask,'snVLanByIpxNetChassisStaticMask':snVLanByIpxNetChassisStaticMask,'snVLanByIpxNetChassisExcludeMask':snVLanByIpxNetChassisExcludeMask,'snVLanByIpxNetChassisDynamicMask':snVLanByIpxNetChassisDynamicMask,'snVLanByIpxNetVLanName':snVLanByIpxNetVLanName,'snVLanByIpxNetStaticPortList':snVLanByIpxNetStaticPortList,'snVLanByIpxNetExcludePortList':snVLanByIpxNetExcludePortList,'snVLanByIpxNetDynamicPortList':snVLanByIpxNetDynamicPortList,'snVLanByATCableTable':snVLanByATCableTable,'snVLanByATCableEntry':snVLanByATCableEntry,_w:snVLanByATCableVLanId,_x:snVLanByATCableIndex,'snVLanByATCableRouterIntf':snVLanByATCableRouterIntf,'snVLanByATCableRowStatus':snVLanByATCableRowStatus,'snVLanByATCableChassisStaticMask':snVLanByATCableChassisStaticMask,'snVLanByATCableVLanName':snVLanByATCableVLanName,'snVLanByATCableStaticPortList':snVLanByATCableStaticPortList,'snVLanByPortMemberTable':snVLanByPortMemberTable,'snVLanByPortMemberEntry':snVLanByPortMemberEntry,_y:snVLanByPortMemberVLanId,_z:snVLanByPortMemberPortId,'snVLanByPortMemberRowStatus':snVLanByPortMemberRowStatus,'snVLanByPortCfgTable':snVLanByPortCfgTable,'snVLanByPortCfgEntry':snVLanByPortCfgEntry,_A0:snVLanByPortCfgVLanId,'snVLanByPortCfgQos':snVLanByPortCfgQos,'snVLanByPortCfgStpMode':snVLanByPortCfgStpMode,'snVLanByPortCfgStpPriority':snVLanByPortCfgStpPriority,'snVLanByPortCfgStpGroupMaxAge':snVLanByPortCfgStpGroupMaxAge,'snVLanByPortCfgStpGroupHelloTime':snVLanByPortCfgStpGroupHelloTime,'snVLanByPortCfgStpGroupForwardDelay':snVLanByPortCfgStpGroupForwardDelay,'snVLanByPortCfgBaseNumPorts':snVLanByPortCfgBaseNumPorts,'snVLanByPortCfgBaseType':snVLanByPortCfgBaseType,'snVLanByPortCfgStpProtocolSpecification':snVLanByPortCfgStpProtocolSpecification,'snVLanByPortCfgStpMaxAge':snVLanByPortCfgStpMaxAge,'snVLanByPortCfgStpHelloTime':snVLanByPortCfgStpHelloTime,'snVLanByPortCfgStpHoldTime':snVLanByPortCfgStpHoldTime,'snVLanByPortCfgStpForwardDelay':snVLanByPortCfgStpForwardDelay,'snVLanByPortCfgStpTimeSinceTopologyChange':snVLanByPortCfgStpTimeSinceTopologyChange,'snVLanByPortCfgStpTopChanges':snVLanByPortCfgStpTopChanges,'snVLanByPortCfgStpRootCost':snVLanByPortCfgStpRootCost,'snVLanByPortCfgStpRootPort':snVLanByPortCfgStpRootPort,'snVLanByPortCfgStpDesignatedRoot':snVLanByPortCfgStpDesignatedRoot,'snVLanByPortCfgBaseBridgeAddress':snVLanByPortCfgBaseBridgeAddress,'snVLanByPortCfgVLanName':snVLanByPortCfgVLanName,'snVLanByPortCfgRouterIntf':snVLanByPortCfgRouterIntf,'snVLanByPortCfgRowStatus':snVLanByPortCfgRowStatus,'snSwPortInfo':snSwPortInfo,'snSwPortInfoTable':snSwPortInfoTable,'snSwPortInfoEntry':snSwPortInfoEntry,_A1:snSwPortInfoPortNum,'snSwPortInfoMonitorMode':snSwPortInfoMonitorMode,'snSwPortInfoTagMode':snSwPortInfoTagMode,'snSwPortInfoChnMode':snSwPortInfoChnMode,'snSwPortInfoSpeed':snSwPortInfoSpeed,'snSwPortInfoMediaType':snSwPortInfoMediaType,'snSwPortInfoConnectorType':snSwPortInfoConnectorType,'snSwPortInfoAdminStatus':snSwPortInfoAdminStatus,'snSwPortInfoLinkStatus':snSwPortInfoLinkStatus,'snSwPortInfoPortQos':snSwPortInfoPortQos,'snSwPortInfoPhysAddress':snSwPortInfoPhysAddress,'snSwPortStatsInFrames':snSwPortStatsInFrames,'snSwPortStatsOutFrames':snSwPortStatsOutFrames,'snSwPortStatsAlignErrors':snSwPortStatsAlignErrors,'snSwPortStatsFCSErrors':snSwPortStatsFCSErrors,'snSwPortStatsMultiColliFrames':snSwPortStatsMultiColliFrames,'snSwPortStatsFrameTooLongs':snSwPortStatsFrameTooLongs,'snSwPortStatsTxColliFrames':snSwPortStatsTxColliFrames,'snSwPortStatsRxColliFrames':snSwPortStatsRxColliFrames,'snSwPortStatsFrameTooShorts':snSwPortStatsFrameTooShorts,'snSwPortLockAddressCount':snSwPortLockAddressCount,'snSwPortStpPortEnable':snSwPortStpPortEnable,'snSwPortDhcpGateListId':snSwPortDhcpGateListId,'snSwPortName':snSwPortName,'snSwPortStatsInBcastFrames':snSwPortStatsInBcastFrames,'snSwPortStatsOutBcastFrames':snSwPortStatsOutBcastFrames,'snSwPortStatsInMcastFrames':snSwPortStatsInMcastFrames,'snSwPortStatsOutMcastFrames':snSwPortStatsOutMcastFrames,'snSwPortStatsInDiscard':snSwPortStatsInDiscard,'snSwPortStatsOutDiscard':snSwPortStatsOutDiscard,'snSwPortStatsMacStations':snSwPortStatsMacStations,'snSwPortCacheGroupId':snSwPortCacheGroupId,'snSwPortTransGroupId':snSwPortTransGroupId,'snSwPortInfoAutoNegotiate':snSwPortInfoAutoNegotiate,'snSwPortInfoFlowControl':snSwPortInfoFlowControl,'snSwPortInfoGigType':snSwPortInfoGigType,'snSwPortStatsLinkChange':snSwPortStatsLinkChange,'snSwPortIfIndex':snSwPortIfIndex,'snSwPortDescr':snSwPortDescr,'snSwPortInOctets':snSwPortInOctets,'snSwPortOutOctets':snSwPortOutOctets,'snSwPortStatsInBitsPerSec':snSwPortStatsInBitsPerSec,'snSwPortStatsOutBitsPerSec':snSwPortStatsOutBitsPerSec,'snSwPortStatsInPktsPerSec':snSwPortStatsInPktsPerSec,'snSwPortStatsOutPktsPerSec':snSwPortStatsOutPktsPerSec,'snSwPortStatsInUtilization':snSwPortStatsInUtilization,'snSwPortStatsOutUtilization':snSwPortStatsOutUtilization,'snSwPortFastSpanPortEnable':snSwPortFastSpanPortEnable,'snSwPortFastSpanUplinkEnable':snSwPortFastSpanUplinkEnable,'snSwPortVlanId':snSwPortVlanId,'snSwPortRouteOnly':snSwPortRouteOnly,'snSwPortPresent':snSwPortPresent,'snSwPortGBICStatus':snSwPortGBICStatus,'snSwPortStatsInKiloBitsPerSec':snSwPortStatsInKiloBitsPerSec,'snSwPortStatsOutKiloBitsPerSec':snSwPortStatsOutKiloBitsPerSec,'snSwPortLoadInterval':snSwPortLoadInterval,'snSwPortTagType':snSwPortTagType,'snInterfaceId':snInterfaceId,'snInterfaceLookupTable':snInterfaceLookupTable,'snInterfaceLookupEntry':snInterfaceLookupEntry,_A3:snInterfaceLookupInterfaceId,'snInterfaceLookupIfIndex':snInterfaceLookupIfIndex,'snIfIndexLookupTable':snIfIndexLookupTable,'snIfIndexLookupEntry':snIfIndexLookupEntry,_A4:snIfIndexLookupIfIndex,'snIfIndexLookupInterfaceId':snIfIndexLookupInterfaceId,'snFdbInfo':snFdbInfo,'snFdbTable':snFdbTable,'snFdbEntry':snFdbEntry,_A5:snFdbStationIndex,'snFdbStationAddr':snFdbStationAddr,'snFdbStationPort':snFdbStationPort,'snFdbVLanId':snFdbVLanId,'snFdbStationQos':snFdbStationQos,'snFdbStationType':snFdbStationType,'snFdbRowStatus':snFdbRowStatus,'snPortStpInfo':snPortStpInfo,'snPortStpTable':snPortStpTable,'snPortStpEntry':snPortStpEntry,_A6:snPortStpVLanId,_A7:snPortStpPortNum,'snPortStpPortPriority':snPortStpPortPriority,'snPortStpPathCost':snPortStpPathCost,'snPortStpOperState':snPortStpOperState,'snPortStpPortEnable':snPortStpPortEnable,'snPortStpPortForwardTransitions':snPortStpPortForwardTransitions,'snPortStpPortState':snPortStpPortState,'snPortStpPortDesignatedCost':snPortStpPortDesignatedCost,'snPortStpPortDesignatedRoot':snPortStpPortDesignatedRoot,'snPortStpPortDesignatedBridge':snPortStpPortDesignatedBridge,'snPortStpPortDesignatedPort':snPortStpPortDesignatedPort,'snTrunkInfo':snTrunkInfo,'snTrunkTable':snTrunkTable,'snTrunkEntry':snTrunkEntry,_A8:snTrunkIndex,'snTrunkPortMask':snTrunkPortMask,'snTrunkType':snTrunkType,'snMSTrunkTable':snMSTrunkTable,'snMSTrunkEntry':snMSTrunkEntry,_A9:snMSTrunkPortIndex,'snMSTrunkPortList':snMSTrunkPortList,'snMSTrunkType':snMSTrunkType,'snMSTrunkRowStatus':snMSTrunkRowStatus,'snSwSummary':snSwSummary,'snSwSummaryMode':snSwSummaryMode,'snDhcpGatewayListInfo':snDhcpGatewayListInfo,'snDhcpGatewayListTable':snDhcpGatewayListTable,'snDhcpGatewayListEntry':snDhcpGatewayListEntry,_AA:snDhcpGatewayListId,'snDhcpGatewayListAddrList':snDhcpGatewayListAddrList,'snDhcpGatewayListRowStatus':snDhcpGatewayListRowStatus,'snDnsInfo':snDnsInfo,'snDnsDomainName':snDnsDomainName,'snDnsGatewayIpAddrList':snDnsGatewayIpAddrList,'snMacFilter':snMacFilter,'snMacFilterTable':snMacFilterTable,'snMacFilterEntry':snMacFilterEntry,_AB:snMacFilterIndex,'snMacFilterAction':snMacFilterAction,'snMacFilterSourceMac':snMacFilterSourceMac,'snMacFilterSourceMask':snMacFilterSourceMask,'snMacFilterDestMac':snMacFilterDestMac,'snMacFilterDestMask':snMacFilterDestMask,'snMacFilterOperator':snMacFilterOperator,'snMacFilterFrameType':snMacFilterFrameType,'snMacFilterFrameTypeNum':snMacFilterFrameTypeNum,'snMacFilterRowStatus':snMacFilterRowStatus,'snMacFilterPortAccessTable':snMacFilterPortAccessTable,'snMacFilterPortAccessEntry':snMacFilterPortAccessEntry,_AC:snMacFilterPortAccessPortIndex,'snMacFilterPortAccessFilters':snMacFilterPortAccessFilters,'snMacFilterPortAccessRowStatus':snMacFilterPortAccessRowStatus,'snNTP':snNTP,'snNTPGeneral':snNTPGeneral,'snNTPPollInterval':snNTPPollInterval,'snNTPTimeZone':snNTPTimeZone,'snNTPSummerTimeEnable':snNTPSummerTimeEnable,'snNTPSystemClock':snNTPSystemClock,'snNTPSync':snNTPSync,'snNTPServerTable':snNTPServerTable,'snNTPServerEntry':snNTPServerEntry,_AD:snNTPServerIp,'snNTPServerVersion':snNTPServerVersion,'snNTPServerRowStatus':snNTPServerRowStatus,'snRadius':snRadius,'snRadiusGeneral':snRadiusGeneral,'snRadiusSNMPAccess':snRadiusSNMPAccess,'snRadiusEnableTelnetAuth':snRadiusEnableTelnetAuth,'snRadiusRetransmit':snRadiusRetransmit,'snRadiusTimeOut':snRadiusTimeOut,'snRadiusDeadTime':snRadiusDeadTime,'snRadiusKey':snRadiusKey,'snRadiusLoginMethod':snRadiusLoginMethod,'snRadiusEnableMethod':snRadiusEnableMethod,'snRadiusWebServerMethod':snRadiusWebServerMethod,'snRadiusSNMPServerMethod':snRadiusSNMPServerMethod,'snRadiusServerTable':snRadiusServerTable,'snRadiusServerEntry':snRadiusServerEntry,_AE:snRadiusServerIp,'snRadiusServerAuthPort':snRadiusServerAuthPort,'snRadiusServerAcctPort':snRadiusServerAcctPort,'snRadiusServerRowStatus':snRadiusServerRowStatus,'snRadiusServerRowKey':snRadiusServerRowKey,'snRadiusServerUsage':snRadiusServerUsage,'snTacacs':snTacacs,'snTacacsGeneral':snTacacsGeneral,'snTacacsRetransmit':snTacacsRetransmit,'snTacacsTimeOut':snTacacsTimeOut,'snTacacsDeadTime':snTacacsDeadTime,'snTacacsKey':snTacacsKey,'snTacacsSNMPAccess':snTacacsSNMPAccess,'snTacacsServerTable':snTacacsServerTable,'snTacacsServerEntry':snTacacsServerEntry,_AI:snTacacsServerIp,'snTacacsServerAuthPort':snTacacsServerAuthPort,'snTacacsServerRowStatus':snTacacsServerRowStatus,'snTacacsServerRowKey':snTacacsServerRowKey,'snTacacsServerUsage':snTacacsServerUsage,'snQos':snQos,'snQosProfileTable':snQosProfileTable,'snQosProfileEntry':snQosProfileEntry,_AJ:snQosProfileIndex,'snQosProfileName':snQosProfileName,'snQosProfileRequestedBandwidth':snQosProfileRequestedBandwidth,'snQosProfileCalculatedBandwidth':snQosProfileCalculatedBandwidth,'snQosBindTable':snQosBindTable,'snQosBindEntry':snQosBindEntry,_AK:snQosBindIndex,'snQosBindPriority':snQosBindPriority,'snQosBindProfileIndex':snQosBindProfileIndex,'snAAA':snAAA,'snAuthentication':snAuthentication,'snAuthorization':snAuthorization,'snAuthorizationCommandMethods':snAuthorizationCommandMethods,'snAuthorizationCommandLevel':snAuthorizationCommandLevel,'snAuthorizationExec':snAuthorizationExec,'snAccounting':snAccounting,'snAccountingCommandMethods':snAccountingCommandMethods,'snAccountingCommandLevel':snAccountingCommandLevel,'snAccountingExec':snAccountingExec,'snAccountingSystem':snAccountingSystem,'snCAR':snCAR,'snVLanCAR':snVLanCAR,'snNetFlow':snNetFlow,'snNetFlowGlb':snNetFlowGlb,'snNetFlowGblEnable':snNetFlowGblEnable,'snNetFlowGblVersion':snNetFlowGblVersion,'snNetFlowGblProtocolDisable':snNetFlowGblProtocolDisable,'snNetFlowGblActiveTimeout':snNetFlowGblActiveTimeout,'snNetFlowGblInactiveTimeout':snNetFlowGblInactiveTimeout,'snNetFlowCollectorTable':snNetFlowCollectorTable,'snNetFlowCollectorEntry':snNetFlowCollectorEntry,_AL:snNetFlowCollectorIndex,'snNetFlowCollectorIp':snNetFlowCollectorIp,'snNetFlowCollectorUdpPort':snNetFlowCollectorUdpPort,'snNetFlowCollectorSourceInterface':snNetFlowCollectorSourceInterface,'snNetFlowCollectorRowStatus':snNetFlowCollectorRowStatus,'snNetFlowAggregationTable':snNetFlowAggregationTable,'snNetFlowAggregationEntry':snNetFlowAggregationEntry,_AM:snNetFlowAggregationIndex,'snNetFlowAggregationIp':snNetFlowAggregationIp,'snNetFlowAggregationUdpPort':snNetFlowAggregationUdpPort,'snNetFlowAggregationSourceInterface':snNetFlowAggregationSourceInterface,'snNetFlowAggregationNumberOfCacheEntries':snNetFlowAggregationNumberOfCacheEntries,'snNetFlowAggregationActiveTimeout':snNetFlowAggregationActiveTimeout,'snNetFlowAggregationInactiveTimeout':snNetFlowAggregationInactiveTimeout,'snNetFlowAggregationEnable':snNetFlowAggregationEnable,'snNetFlowAggregationRowStatus':snNetFlowAggregationRowStatus,'snNetFlowIfTable':snNetFlowIfTable,'snNetFlowIfEntry':snNetFlowIfEntry,_AN:snNetFlowIfIndex,'snNetFlowIfFlowSwitching':snNetFlowIfFlowSwitching,'snSFlow':snSFlow,'snSFlowGlb':snSFlowGlb,'snSflowCollectorTable':snSflowCollectorTable,'snSflowCollectorEntry':snSflowCollectorEntry,_AO:snSflowCollectorIndex,'snSflowCollectorIP':snSflowCollectorIP,'snSflowCollectorUDPPort':snSflowCollectorUDPPort,'snSflowCollectorRowStatus':snSflowCollectorRowStatus,'snFDP':snFDP,'snFdpMIBObjects':snFdpMIBObjects,'snFdpInterface':snFdpInterface,'snFdpInterfaceTable':snFdpInterfaceTable,'snFdpInterfaceEntry':snFdpInterfaceEntry,_AP:snFdpInterfaceIfIndex,'snFdpInterfaceFdpEnable':snFdpInterfaceFdpEnable,'snFdpInterfaceCdpEnable':snFdpInterfaceCdpEnable,'snFdpCache':snFdpCache,'snFdpCacheTable':snFdpCacheTable,'snFdpCacheEntry':snFdpCacheEntry,_AQ:snFdpCacheIfIndex,_AR:snFdpCacheDeviceIndex,'snFdpCacheDeviceId':snFdpCacheDeviceId,'snFdpCacheAddressType':snFdpCacheAddressType,'snFdpCacheAddress':snFdpCacheAddress,'snFdpCacheVersion':snFdpCacheVersion,'snFdpCacheDevicePort':snFdpCacheDevicePort,'snFdpCachePlatform':snFdpCachePlatform,'snFdpCacheCapabilities':snFdpCacheCapabilities,'snFdpCacheVendorId':snFdpCacheVendorId,'snFdpCacheIsAggregateVlan':snFdpCacheIsAggregateVlan,'snFdpCacheTagType':snFdpCacheTagType,'snFdpCachePortVlanMask':snFdpCachePortVlanMask,'snFdpCachePortTagMode':snFdpCachePortTagMode,'snFdpCacheDefaultTrafficeVlanIdForDualMode':snFdpCacheDefaultTrafficeVlanIdForDualMode,'snFdpGlobal':snFdpGlobal,'snFdpGlobalRun':snFdpGlobalRun,'snFdpGlobalMessageInterval':snFdpGlobalMessageInterval,'snFdpGlobalHoldTime':snFdpGlobalHoldTime,'snFdpGlobalCdpRun':snFdpGlobalCdpRun,'snFdpCachedAddr':snFdpCachedAddr,'snFdpCachedAddressTable':snFdpCachedAddressTable,'snFdpCachedAddressEntry':snFdpCachedAddressEntry,_AT:snFdpCachedAddrIfIndex,_AU:snFdpCachedAddrDeviceIndex,_AV:snFdpCachedAddrDeviceAddrEntryIndex,'snFdpCachedAddrType':snFdpCachedAddrType,'snFdpCachedAddrValue':snFdpCachedAddrValue,'snVsrp':snVsrp})