_A3='bgpPathAttrCommIndex'
_A2='bgpIpPreNumber'
_A1='bgpIpPreMatch'
_A0='BgpAsSize'
_z='BgpCommunityAction'
_y='bgpNetworkPrefixLen'
_x='bgpNetworkPrefixAddr'
_w='bgpNetworkAddrType'
_v='bgpNetworkSafi'
_u='bgpNetworkAfiType'
_t='bgpAdjRibOutPrefixLen'
_s='bgpAdjRibOutPrefix'
_r='bgpAdjRibOutSafi'
_q='bgpAdjRibOutAfiType'
_p='bgpRibManagerIndex'
_o='InetAddressType'
_n='InetAddressPrefixLength'
_m='InetAddress'
_l='bgpPolicyBindNumber'
_k='bgpPolicyBindType'
_j='bgpPolicyBindDirection'
_i='BgpPermitOrDeny'
_h='bgpNlriPrefixLen'
_g='bgpNlriPerfixAddress'
_f='bgpNlriSafi'
_e='bgpNlriAfiType'
_d='off'
_c='TruthValue'
_b='DisplayString'
_a='bgpPeerDescr'
_Z='bgpRouteMapNumber'
_Y='bgpRouteMapIndex'
_X='bgpPeerAfiSafiSafi'
_W='bgpPeerAfiSafiAfiType'
_V='Unsigned32'
_U='SnmpAdminString'
_T='rtrConfigRoutingName'
_S='RAD-SubRtr-MIB'
_R='alarmEventReason'
_Q='alarmEventLogSourceName'
_P='alarmEventLogSeverity'
_O='alarmEventLogDescription'
_N='alarmEventLogDateAndTime'
_M='alarmEventLogAlarmOrEventId'
_L='seconds'
_K='OctetString'
_J='read-write'
_I='bgpPeerRemoteAddr'
_H='bgpPeerRemoteAddrType'
_G='Integer32'
_F='RAD-GEN-MIB'
_E='not-accessible'
_D='read-only'
_C='read-create'
_B='RAD-RadBgp-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_m,_n,_o,'InetPortNumber')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason,radSysRtrEvents=mibBuilder.importSymbols(_F,_M,_N,_O,_P,_Q,_R,'radSysRtrEvents')
RtrSafi,radRouter,rtrConfigRoutingName=mibBuilder.importSymbols(_S,'RtrSafi','radRouter',_T)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_U)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_b,'PhysAddress','RowStatus','TextualConvention',_c)
rtrBgp=ModuleIdentity((1,3,6,1,4,1,164,11,4))
class BgpAutonomousSystemNumber(TextualConvention,Unsigned32):status=_A
class BgpIdentifier(TextualConvention,OctetString):status=_A;displayHint='4x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class BgpPeerStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
class BgpCapabilities(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('reserved0',0),('mpIpv4Unicast',1),('mpIpv4Multicast',2),('mpIpv4Vpn',3),('reserved4',4),('mpIpv6Unicast',5),('mpIpv6Multicast',6),('mpIpv6Vpn',7),('reserved8',8),('routeRefresh',9),('gracefulRestart',10),('routeRefreshCisco',11),('outboundRouteFilter',12),('outboundRouteFilterCisco',13),('fourOctetAs',14)))
class BgpPermitOrDeny(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
class BgpSafi(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,128)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('both',3),('mplsBgpVpn',128)))
class BgpCommunity(TextualConvention,OctetString):status=_A;displayHint='4x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class BgpCommunityAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('removeAll',1),('removeSpecific',2),('setSpecific',3),('removeAllAndSet',4)))
class BgpIpMatchType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nlriAddr',1),('sourceAddr',2),('nextHopAddr',3)))
class BgpAsSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoOctet',1),('fourOctet',2)))
_BgpRibManagerTable_Object=MibTable
bgpRibManagerTable=_BgpRibManagerTable_Object((1,3,6,1,4,1,164,11,4,1))
if mibBuilder.loadTexts:bgpRibManagerTable.setStatus(_A)
_BgpRibManagerEntry_Object=MibTableRow
bgpRibManagerEntry=_BgpRibManagerEntry_Object((1,3,6,1,4,1,164,11,4,1,1))
bgpRibManagerEntry.setIndexNames((0,_B,_p))
if mibBuilder.loadTexts:bgpRibManagerEntry.setStatus(_A)
_BgpRibManagerIndex_Type=Unsigned32
_BgpRibManagerIndex_Object=MibTableColumn
bgpRibManagerIndex=_BgpRibManagerIndex_Object((1,3,6,1,4,1,164,11,4,1,1,1),_BgpRibManagerIndex_Type())
bgpRibManagerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpRibManagerIndex.setStatus(_A)
_BgpRibManagerRowStatus_Type=RowStatus
_BgpRibManagerRowStatus_Object=MibTableColumn
bgpRibManagerRowStatus=_BgpRibManagerRowStatus_Object((1,3,6,1,4,1,164,11,4,1,1,2),_BgpRibManagerRowStatus_Type())
bgpRibManagerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRibManagerRowStatus.setStatus(_A)
_BgpRibManagerLocalAs_Type=BgpAutonomousSystemNumber
_BgpRibManagerLocalAs_Object=MibTableColumn
bgpRibManagerLocalAs=_BgpRibManagerLocalAs_Object((1,3,6,1,4,1,164,11,4,1,1,3),_BgpRibManagerLocalAs_Type())
bgpRibManagerLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRibManagerLocalAs.setStatus(_A)
_BgpRibManagerLocalIdentifier_Type=BgpIdentifier
_BgpRibManagerLocalIdentifier_Object=MibTableColumn
bgpRibManagerLocalIdentifier=_BgpRibManagerLocalIdentifier_Object((1,3,6,1,4,1,164,11,4,1,1,4),_BgpRibManagerLocalIdentifier_Type())
bgpRibManagerLocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRibManagerLocalIdentifier.setStatus(_A)
_BgpPeerTable_Object=MibTable
bgpPeerTable=_BgpPeerTable_Object((1,3,6,1,4,1,164,11,4,2))
if mibBuilder.loadTexts:bgpPeerTable.setStatus(_A)
_BgpPeerEntry_Object=MibTableRow
bgpPeerEntry=_BgpPeerEntry_Object((1,3,6,1,4,1,164,11,4,2,1))
bgpPeerEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:bgpPeerEntry.setStatus(_A)
_BgpPeerRemoteAddrType_Type=InetAddressType
_BgpPeerRemoteAddrType_Object=MibTableColumn
bgpPeerRemoteAddrType=_BgpPeerRemoteAddrType_Object((1,3,6,1,4,1,164,11,4,2,1,1),_BgpPeerRemoteAddrType_Type())
bgpPeerRemoteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPeerRemoteAddrType.setStatus(_A)
_BgpPeerRemoteAddr_Type=InetAddress
_BgpPeerRemoteAddr_Object=MibTableColumn
bgpPeerRemoteAddr=_BgpPeerRemoteAddr_Object((1,3,6,1,4,1,164,11,4,2,1,2),_BgpPeerRemoteAddr_Type())
bgpPeerRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPeerRemoteAddr.setStatus(_A)
_BgpPeerFsmState_Type=BgpPeerStates
_BgpPeerFsmState_Object=MibTableColumn
bgpPeerFsmState=_BgpPeerFsmState_Object((1,3,6,1,4,1,164,11,4,2,1,3),_BgpPeerFsmState_Type())
bgpPeerFsmState.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerFsmState.setStatus(_A)
_BgpPeerRowStatus_Type=RowStatus
_BgpPeerRowStatus_Object=MibTableColumn
bgpPeerRowStatus=_BgpPeerRowStatus_Object((1,3,6,1,4,1,164,11,4,2,1,4),_BgpPeerRowStatus_Type())
bgpPeerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerRowStatus.setStatus(_A)
_BgpPeerLocalAddrType_Type=InetAddressType
_BgpPeerLocalAddrType_Object=MibTableColumn
bgpPeerLocalAddrType=_BgpPeerLocalAddrType_Object((1,3,6,1,4,1,164,11,4,2,1,5),_BgpPeerLocalAddrType_Type())
bgpPeerLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerLocalAddrType.setStatus(_A)
_BgpPeerLocalAddr_Type=InetAddress
_BgpPeerLocalAddr_Object=MibTableColumn
bgpPeerLocalAddr=_BgpPeerLocalAddr_Object((1,3,6,1,4,1,164,11,4,2,1,6),_BgpPeerLocalAddr_Type())
bgpPeerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerLocalAddr.setStatus(_A)
_BgpPeerRemoteAs_Type=BgpAutonomousSystemNumber
_BgpPeerRemoteAs_Object=MibTableColumn
bgpPeerRemoteAs=_BgpPeerRemoteAs_Object((1,3,6,1,4,1,164,11,4,2,1,7),_BgpPeerRemoteAs_Type())
bgpPeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerRemoteAs.setStatus(_A)
class _BgpPeerLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_BgpPeerLastError_Type.__name__=_K
_BgpPeerLastError_Object=MibTableColumn
bgpPeerLastError=_BgpPeerLastError_Object((1,3,6,1,4,1,164,11,4,2,1,8),_BgpPeerLastError_Type())
bgpPeerLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerLastError.setStatus(_A)
_BgpPeerFsmEstablishedTime_Type=Gauge32
_BgpPeerFsmEstablishedTime_Object=MibTableColumn
bgpPeerFsmEstablishedTime=_BgpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,164,11,4,2,1,9),_BgpPeerFsmEstablishedTime_Type())
bgpPeerFsmEstablishedTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerFsmEstablishedTime.setStatus(_A)
if mibBuilder.loadTexts:bgpPeerFsmEstablishedTime.setUnits(_L)
_BgpPeerHoldTimeConfig_Type=Unsigned32
_BgpPeerHoldTimeConfig_Object=MibTableColumn
bgpPeerHoldTimeConfig=_BgpPeerHoldTimeConfig_Object((1,3,6,1,4,1,164,11,4,2,1,10),_BgpPeerHoldTimeConfig_Type())
bgpPeerHoldTimeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerHoldTimeConfig.setStatus(_A)
if mibBuilder.loadTexts:bgpPeerHoldTimeConfig.setUnits(_L)
_BgpPeerKeepAliveConfig_Type=Unsigned32
_BgpPeerKeepAliveConfig_Object=MibTableColumn
bgpPeerKeepAliveConfig=_BgpPeerKeepAliveConfig_Object((1,3,6,1,4,1,164,11,4,2,1,11),_BgpPeerKeepAliveConfig_Type())
bgpPeerKeepAliveConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerKeepAliveConfig.setStatus(_A)
if mibBuilder.loadTexts:bgpPeerKeepAliveConfig.setUnits(_L)
_BgpPeerHoldTime_Type=Integer32
_BgpPeerHoldTime_Object=MibTableColumn
bgpPeerHoldTime=_BgpPeerHoldTime_Object((1,3,6,1,4,1,164,11,4,2,1,12),_BgpPeerHoldTime_Type())
bgpPeerHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerHoldTime.setStatus(_A)
if mibBuilder.loadTexts:bgpPeerHoldTime.setUnits(_L)
_BgpPeerKeepAlive_Type=Integer32
_BgpPeerKeepAlive_Object=MibTableColumn
bgpPeerKeepAlive=_BgpPeerKeepAlive_Object((1,3,6,1,4,1,164,11,4,2,1,13),_BgpPeerKeepAlive_Type())
bgpPeerKeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:bgpPeerKeepAlive.setUnits(_L)
_BgpPeerConfigMaxPrefix_Type=Integer32
_BgpPeerConfigMaxPrefix_Object=MibTableColumn
bgpPeerConfigMaxPrefix=_BgpPeerConfigMaxPrefix_Object((1,3,6,1,4,1,164,11,4,2,1,14),_BgpPeerConfigMaxPrefix_Type())
bgpPeerConfigMaxPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerConfigMaxPrefix.setStatus(_A)
class _BgpPeerPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_BgpPeerPassword_Type.__name__=_K
_BgpPeerPassword_Object=MibTableColumn
bgpPeerPassword=_BgpPeerPassword_Object((1,3,6,1,4,1,164,11,4,2,1,15),_BgpPeerPassword_Type())
bgpPeerPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerPassword.setStatus(_A)
_BgpPeerCapabilitySent_Type=BgpCapabilities
_BgpPeerCapabilitySent_Object=MibTableColumn
bgpPeerCapabilitySent=_BgpPeerCapabilitySent_Object((1,3,6,1,4,1,164,11,4,2,1,16),_BgpPeerCapabilitySent_Type())
bgpPeerCapabilitySent.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerCapabilitySent.setStatus(_A)
_BgpPeerCapabilityRcv_Type=BgpCapabilities
_BgpPeerCapabilityRcv_Object=MibTableColumn
bgpPeerCapabilityRcv=_BgpPeerCapabilityRcv_Object((1,3,6,1,4,1,164,11,4,2,1,17),_BgpPeerCapabilityRcv_Type())
bgpPeerCapabilityRcv.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerCapabilityRcv.setStatus(_A)
_BgpPeerCapabilityNegotiated_Type=BgpCapabilities
_BgpPeerCapabilityNegotiated_Object=MibTableColumn
bgpPeerCapabilityNegotiated=_BgpPeerCapabilityNegotiated_Object((1,3,6,1,4,1,164,11,4,2,1,18),_BgpPeerCapabilityNegotiated_Type())
bgpPeerCapabilityNegotiated.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerCapabilityNegotiated.setStatus(_A)
_BgpPeerSelectedLocalAddr_Type=InetAddress
_BgpPeerSelectedLocalAddr_Object=MibTableColumn
bgpPeerSelectedLocalAddr=_BgpPeerSelectedLocalAddr_Object((1,3,6,1,4,1,164,11,4,2,1,19),_BgpPeerSelectedLocalAddr_Type())
bgpPeerSelectedLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerSelectedLocalAddr.setStatus(_A)
_BgpPeerSelectedLocalPort_Type=InetPortNumber
_BgpPeerSelectedLocalPort_Object=MibTableColumn
bgpPeerSelectedLocalPort=_BgpPeerSelectedLocalPort_Object((1,3,6,1,4,1,164,11,4,2,1,20),_BgpPeerSelectedLocalPort_Type())
bgpPeerSelectedLocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerSelectedLocalPort.setStatus(_A)
_BgpPeerSelectedRemotePort_Type=InetPortNumber
_BgpPeerSelectedRemotePort_Object=MibTableColumn
bgpPeerSelectedRemotePort=_BgpPeerSelectedRemotePort_Object((1,3,6,1,4,1,164,11,4,2,1,21),_BgpPeerSelectedRemotePort_Type())
bgpPeerSelectedRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPeerSelectedRemotePort.setStatus(_A)
class _BgpPeerClearCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_d,2),('on',3),('soft',4)))
_BgpPeerClearCmd_Type.__name__=_G
_BgpPeerClearCmd_Object=MibTableColumn
bgpPeerClearCmd=_BgpPeerClearCmd_Object((1,3,6,1,4,1,164,11,4,2,1,22),_BgpPeerClearCmd_Type())
bgpPeerClearCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerClearCmd.setStatus(_A)
_BgpPeerDescr_Type=SnmpAdminString
_BgpPeerDescr_Object=MibTableColumn
bgpPeerDescr=_BgpPeerDescr_Object((1,3,6,1,4,1,164,11,4,2,1,23),_BgpPeerDescr_Type())
bgpPeerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerDescr.setStatus(_A)
_BgpPeerAfiSafiTable_Object=MibTable
bgpPeerAfiSafiTable=_BgpPeerAfiSafiTable_Object((1,3,6,1,4,1,164,11,4,3))
if mibBuilder.loadTexts:bgpPeerAfiSafiTable.setStatus(_A)
_BgpPeerAfiSafiEntry_Object=MibTableRow
bgpPeerAfiSafiEntry=_BgpPeerAfiSafiEntry_Object((1,3,6,1,4,1,164,11,4,3,1))
bgpPeerAfiSafiEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:bgpPeerAfiSafiEntry.setStatus(_A)
_BgpPeerAfiSafiAfiType_Type=InetAddressType
_BgpPeerAfiSafiAfiType_Object=MibTableColumn
bgpPeerAfiSafiAfiType=_BgpPeerAfiSafiAfiType_Object((1,3,6,1,4,1,164,11,4,3,1,1),_BgpPeerAfiSafiAfiType_Type())
bgpPeerAfiSafiAfiType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPeerAfiSafiAfiType.setStatus(_A)
_BgpPeerAfiSafiSafi_Type=RtrSafi
_BgpPeerAfiSafiSafi_Object=MibTableColumn
bgpPeerAfiSafiSafi=_BgpPeerAfiSafiSafi_Object((1,3,6,1,4,1,164,11,4,3,1,2),_BgpPeerAfiSafiSafi_Type())
bgpPeerAfiSafiSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPeerAfiSafiSafi.setStatus(_A)
class _BgpPeerAfiSafiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_BgpPeerAfiSafiStatus_Type.__name__=_G
_BgpPeerAfiSafiStatus_Object=MibTableColumn
bgpPeerAfiSafiStatus=_BgpPeerAfiSafiStatus_Object((1,3,6,1,4,1,164,11,4,3,1,3),_BgpPeerAfiSafiStatus_Type())
bgpPeerAfiSafiStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpPeerAfiSafiStatus.setStatus(_A)
_BgpNlriTable_Object=MibTable
bgpNlriTable=_BgpNlriTable_Object((1,3,6,1,4,1,164,11,4,4))
if mibBuilder.loadTexts:bgpNlriTable.setStatus(_A)
_BgpNlriEntry_Object=MibTableRow
bgpNlriEntry=_BgpNlriEntry_Object((1,3,6,1,4,1,164,11,4,4,1))
bgpNlriEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:bgpNlriEntry.setStatus(_A)
_BgpNlriAfiType_Type=InetAddressType
_BgpNlriAfiType_Object=MibTableColumn
bgpNlriAfiType=_BgpNlriAfiType_Object((1,3,6,1,4,1,164,11,4,4,1,1),_BgpNlriAfiType_Type())
bgpNlriAfiType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNlriAfiType.setStatus(_A)
_BgpNlriSafi_Type=RtrSafi
_BgpNlriSafi_Object=MibTableColumn
bgpNlriSafi=_BgpNlriSafi_Object((1,3,6,1,4,1,164,11,4,4,1,2),_BgpNlriSafi_Type())
bgpNlriSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNlriSafi.setStatus(_A)
_BgpNlriPerfixAddress_Type=InetAddress
_BgpNlriPerfixAddress_Object=MibTableColumn
bgpNlriPerfixAddress=_BgpNlriPerfixAddress_Object((1,3,6,1,4,1,164,11,4,4,1,3),_BgpNlriPerfixAddress_Type())
bgpNlriPerfixAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNlriPerfixAddress.setStatus(_A)
_BgpNlriPrefixLen_Type=InetAddressPrefixLength
_BgpNlriPrefixLen_Object=MibTableColumn
bgpNlriPrefixLen=_BgpNlriPrefixLen_Object((1,3,6,1,4,1,164,11,4,4,1,4),_BgpNlriPrefixLen_Type())
bgpNlriPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNlriPrefixLen.setStatus(_A)
class _BgpNlriASPathStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BgpNlriASPathStr_Type.__name__=_K
_BgpNlriASPathStr_Object=MibTableColumn
bgpNlriASPathStr=_BgpNlriASPathStr_Object((1,3,6,1,4,1,164,11,4,4,1,5),_BgpNlriASPathStr_Type())
bgpNlriASPathStr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriASPathStr.setStatus(_A)
_BgpNlriNextHop_Type=InetAddress
_BgpNlriNextHop_Object=MibTableColumn
bgpNlriNextHop=_BgpNlriNextHop_Object((1,3,6,1,4,1,164,11,4,4,1,6),_BgpNlriNextHop_Type())
bgpNlriNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriNextHop.setStatus(_A)
_BgpNlriAsSize_Type=BgpAsSize
_BgpNlriAsSize_Object=MibTableColumn
bgpNlriAsSize=_BgpNlriAsSize_Object((1,3,6,1,4,1,164,11,4,4,1,7),_BgpNlriAsSize_Type())
bgpNlriAsSize.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriAsSize.setStatus(_A)
_BgpNlriPathAttrMultiExitDisc_Type=Unsigned32
_BgpNlriPathAttrMultiExitDisc_Object=MibTableColumn
bgpNlriPathAttrMultiExitDisc=_BgpNlriPathAttrMultiExitDisc_Object((1,3,6,1,4,1,164,11,4,4,1,8),_BgpNlriPathAttrMultiExitDisc_Type())
bgpNlriPathAttrMultiExitDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriPathAttrMultiExitDisc.setStatus(_A)
_BgpNlriPathAttrLocalPref_Type=Unsigned32
_BgpNlriPathAttrLocalPref_Object=MibTableColumn
bgpNlriPathAttrLocalPref=_BgpNlriPathAttrLocalPref_Object((1,3,6,1,4,1,164,11,4,4,1,9),_BgpNlriPathAttrLocalPref_Type())
bgpNlriPathAttrLocalPref.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriPathAttrLocalPref.setStatus(_A)
_BgpNlriBest_Type=TruthValue
_BgpNlriBest_Object=MibTableColumn
bgpNlriBest=_BgpNlriBest_Object((1,3,6,1,4,1,164,11,4,4,1,10),_BgpNlriBest_Type())
bgpNlriBest.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriBest.setStatus(_A)
_BgpNlriPathAttrMEDPrsnt_Type=TruthValue
_BgpNlriPathAttrMEDPrsnt_Object=MibTableColumn
bgpNlriPathAttrMEDPrsnt=_BgpNlriPathAttrMEDPrsnt_Object((1,3,6,1,4,1,164,11,4,4,1,11),_BgpNlriPathAttrMEDPrsnt_Type())
bgpNlriPathAttrMEDPrsnt.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpNlriPathAttrMEDPrsnt.setStatus(_A)
_BgpAdjRibOutTable_Object=MibTable
bgpAdjRibOutTable=_BgpAdjRibOutTable_Object((1,3,6,1,4,1,164,11,4,5))
if mibBuilder.loadTexts:bgpAdjRibOutTable.setStatus(_A)
_BgpAdjRibOutEntry_Object=MibTableRow
bgpAdjRibOutEntry=_BgpAdjRibOutEntry_Object((1,3,6,1,4,1,164,11,4,5,1))
bgpAdjRibOutEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_q),(0,_B,_r),(0,_B,_s),(0,_B,_t))
if mibBuilder.loadTexts:bgpAdjRibOutEntry.setStatus(_A)
_BgpAdjRibOutAfiType_Type=InetAddressType
_BgpAdjRibOutAfiType_Object=MibTableColumn
bgpAdjRibOutAfiType=_BgpAdjRibOutAfiType_Object((1,3,6,1,4,1,164,11,4,5,1,1),_BgpAdjRibOutAfiType_Type())
bgpAdjRibOutAfiType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpAdjRibOutAfiType.setStatus(_A)
_BgpAdjRibOutSafi_Type=RtrSafi
_BgpAdjRibOutSafi_Object=MibTableColumn
bgpAdjRibOutSafi=_BgpAdjRibOutSafi_Object((1,3,6,1,4,1,164,11,4,5,1,2),_BgpAdjRibOutSafi_Type())
bgpAdjRibOutSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpAdjRibOutSafi.setStatus(_A)
_BgpAdjRibOutPrefix_Type=InetAddress
_BgpAdjRibOutPrefix_Object=MibTableColumn
bgpAdjRibOutPrefix=_BgpAdjRibOutPrefix_Object((1,3,6,1,4,1,164,11,4,5,1,3),_BgpAdjRibOutPrefix_Type())
bgpAdjRibOutPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpAdjRibOutPrefix.setStatus(_A)
_BgpAdjRibOutPrefixLen_Type=InetAddressPrefixLength
_BgpAdjRibOutPrefixLen_Object=MibTableColumn
bgpAdjRibOutPrefixLen=_BgpAdjRibOutPrefixLen_Object((1,3,6,1,4,1,164,11,4,5,1,4),_BgpAdjRibOutPrefixLen_Type())
bgpAdjRibOutPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpAdjRibOutPrefixLen.setStatus(_A)
class _BgpAdjRibOutAdvertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertised',1),('suppressed',2),('pendingWithdrawal',3),('withdrawn',4)))
_BgpAdjRibOutAdvertStatus_Type.__name__=_G
_BgpAdjRibOutAdvertStatus_Object=MibTableColumn
bgpAdjRibOutAdvertStatus=_BgpAdjRibOutAdvertStatus_Object((1,3,6,1,4,1,164,11,4,5,1,5),_BgpAdjRibOutAdvertStatus_Type())
bgpAdjRibOutAdvertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutAdvertStatus.setStatus(_A)
class _BgpAdjRibOutASPathStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BgpAdjRibOutASPathStr_Type.__name__=_K
_BgpAdjRibOutASPathStr_Object=MibTableColumn
bgpAdjRibOutASPathStr=_BgpAdjRibOutASPathStr_Object((1,3,6,1,4,1,164,11,4,5,1,6),_BgpAdjRibOutASPathStr_Type())
bgpAdjRibOutASPathStr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutASPathStr.setStatus(_A)
_BgpAdjRibOutNextHop_Type=InetAddress
_BgpAdjRibOutNextHop_Object=MibTableColumn
bgpAdjRibOutNextHop=_BgpAdjRibOutNextHop_Object((1,3,6,1,4,1,164,11,4,5,1,7),_BgpAdjRibOutNextHop_Type())
bgpAdjRibOutNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutNextHop.setStatus(_A)
_BgpAdjRibOutAsSize_Type=BgpAsSize
_BgpAdjRibOutAsSize_Object=MibTableColumn
bgpAdjRibOutAsSize=_BgpAdjRibOutAsSize_Object((1,3,6,1,4,1,164,11,4,5,1,8),_BgpAdjRibOutAsSize_Type())
bgpAdjRibOutAsSize.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutAsSize.setStatus(_A)
_BgpAdjRibOutMultiExitDisc_Type=Unsigned32
_BgpAdjRibOutMultiExitDisc_Object=MibTableColumn
bgpAdjRibOutMultiExitDisc=_BgpAdjRibOutMultiExitDisc_Object((1,3,6,1,4,1,164,11,4,5,1,9),_BgpAdjRibOutMultiExitDisc_Type())
bgpAdjRibOutMultiExitDisc.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutMultiExitDisc.setStatus(_A)
_BgpAdjRibOutLocalPref_Type=Unsigned32
_BgpAdjRibOutLocalPref_Object=MibTableColumn
bgpAdjRibOutLocalPref=_BgpAdjRibOutLocalPref_Object((1,3,6,1,4,1,164,11,4,5,1,10),_BgpAdjRibOutLocalPref_Type())
bgpAdjRibOutLocalPref.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutLocalPref.setStatus(_A)
_BgpAdjRibOutMEDPrsnt_Type=TruthValue
_BgpAdjRibOutMEDPrsnt_Object=MibTableColumn
bgpAdjRibOutMEDPrsnt=_BgpAdjRibOutMEDPrsnt_Object((1,3,6,1,4,1,164,11,4,5,1,11),_BgpAdjRibOutMEDPrsnt_Type())
bgpAdjRibOutMEDPrsnt.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpAdjRibOutMEDPrsnt.setStatus(_A)
_BgpNetworkTable_Object=MibTable
bgpNetworkTable=_BgpNetworkTable_Object((1,3,6,1,4,1,164,11,4,6))
if mibBuilder.loadTexts:bgpNetworkTable.setStatus(_A)
_BgpNetworkEntry_Object=MibTableRow
bgpNetworkEntry=_BgpNetworkEntry_Object((1,3,6,1,4,1,164,11,4,6,1))
bgpNetworkEntry.setIndexNames((0,_B,_u),(0,_B,_v),(0,_B,_w),(0,_B,_x),(0,_B,_y))
if mibBuilder.loadTexts:bgpNetworkEntry.setStatus(_A)
_BgpNetworkAfiType_Type=InetAddressType
_BgpNetworkAfiType_Object=MibTableColumn
bgpNetworkAfiType=_BgpNetworkAfiType_Object((1,3,6,1,4,1,164,11,4,6,1,1),_BgpNetworkAfiType_Type())
bgpNetworkAfiType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNetworkAfiType.setStatus(_A)
_BgpNetworkSafi_Type=RtrSafi
_BgpNetworkSafi_Object=MibTableColumn
bgpNetworkSafi=_BgpNetworkSafi_Object((1,3,6,1,4,1,164,11,4,6,1,2),_BgpNetworkSafi_Type())
bgpNetworkSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNetworkSafi.setStatus(_A)
_BgpNetworkAddrType_Type=InetAddressType
_BgpNetworkAddrType_Object=MibTableColumn
bgpNetworkAddrType=_BgpNetworkAddrType_Object((1,3,6,1,4,1,164,11,4,6,1,3),_BgpNetworkAddrType_Type())
bgpNetworkAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNetworkAddrType.setStatus(_A)
_BgpNetworkPrefixAddr_Type=InetAddress
_BgpNetworkPrefixAddr_Object=MibTableColumn
bgpNetworkPrefixAddr=_BgpNetworkPrefixAddr_Object((1,3,6,1,4,1,164,11,4,6,1,4),_BgpNetworkPrefixAddr_Type())
bgpNetworkPrefixAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNetworkPrefixAddr.setStatus(_A)
class _BgpNetworkPrefixLen_Type(Integer32):defaultValue=0
_BgpNetworkPrefixLen_Type.__name__=_G
_BgpNetworkPrefixLen_Object=MibTableColumn
bgpNetworkPrefixLen=_BgpNetworkPrefixLen_Object((1,3,6,1,4,1,164,11,4,6,1,5),_BgpNetworkPrefixLen_Type())
bgpNetworkPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpNetworkPrefixLen.setStatus(_A)
_BgpNetworkRowStatus_Type=RowStatus
_BgpNetworkRowStatus_Object=MibTableColumn
bgpNetworkRowStatus=_BgpNetworkRowStatus_Object((1,3,6,1,4,1,164,11,4,6,1,6),_BgpNetworkRowStatus_Type())
bgpNetworkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpNetworkRowStatus.setStatus(_A)
_BgpRouteMapTable_Object=MibTable
bgpRouteMapTable=_BgpRouteMapTable_Object((1,3,6,1,4,1,164,11,4,7))
if mibBuilder.loadTexts:bgpRouteMapTable.setStatus(_A)
_BgpRouteMapEntry_Object=MibTableRow
bgpRouteMapEntry=_BgpRouteMapEntry_Object((1,3,6,1,4,1,164,11,4,7,1))
bgpRouteMapEntry.setIndexNames((0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:bgpRouteMapEntry.setStatus(_A)
class _BgpRouteMapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4278190079))
_BgpRouteMapIndex_Type.__name__=_V
_BgpRouteMapIndex_Object=MibTableColumn
bgpRouteMapIndex=_BgpRouteMapIndex_Object((1,3,6,1,4,1,164,11,4,7,1,1),_BgpRouteMapIndex_Type())
bgpRouteMapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpRouteMapIndex.setStatus(_A)
_BgpRouteMapNumber_Type=Unsigned32
_BgpRouteMapNumber_Object=MibTableColumn
bgpRouteMapNumber=_BgpRouteMapNumber_Object((1,3,6,1,4,1,164,11,4,7,1,2),_BgpRouteMapNumber_Type())
bgpRouteMapNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpRouteMapNumber.setStatus(_A)
class _BgpRouteMapType_Type(BgpPermitOrDeny):defaultValue=1
_BgpRouteMapType_Type.__name__=_i
_BgpRouteMapType_Object=MibTableColumn
bgpRouteMapType=_BgpRouteMapType_Object((1,3,6,1,4,1,164,11,4,7,1,3),_BgpRouteMapType_Type())
bgpRouteMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpRouteMapType.setStatus(_A)
class _BgpRouteMapMaComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BgpRouteMapMaComm_Type.__name__=_b
_BgpRouteMapMaComm_Object=MibTableColumn
bgpRouteMapMaComm=_BgpRouteMapMaComm_Object((1,3,6,1,4,1,164,11,4,7,1,4),_BgpRouteMapMaComm_Type())
bgpRouteMapMaComm.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapMaComm.setStatus(_A)
class _BgpRouteMapSeComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BgpRouteMapSeComm_Type.__name__=_b
_BgpRouteMapSeComm_Object=MibTableColumn
bgpRouteMapSeComm=_BgpRouteMapSeComm_Object((1,3,6,1,4,1,164,11,4,7,1,5),_BgpRouteMapSeComm_Type())
bgpRouteMapSeComm.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeComm.setStatus(_A)
class _BgpRouteMapSeCommAct_Type(BgpCommunityAction):defaultValue=0
_BgpRouteMapSeCommAct_Type.__name__=_z
_BgpRouteMapSeCommAct_Object=MibTableColumn
bgpRouteMapSeCommAct=_BgpRouteMapSeCommAct_Object((1,3,6,1,4,1,164,11,4,7,1,6),_BgpRouteMapSeCommAct_Type())
bgpRouteMapSeCommAct.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeCommAct.setStatus(_A)
class _BgpRouteMapSeLocPref_Type(Integer32):defaultValue=0
_BgpRouteMapSeLocPref_Type.__name__=_G
_BgpRouteMapSeLocPref_Object=MibTableColumn
bgpRouteMapSeLocPref=_BgpRouteMapSeLocPref_Object((1,3,6,1,4,1,164,11,4,7,1,7),_BgpRouteMapSeLocPref_Type())
bgpRouteMapSeLocPref.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeLocPref.setStatus(_A)
class _BgpRouteMapSeLocPrefDef_Type(TruthValue):defaultValue=2
_BgpRouteMapSeLocPrefDef_Type.__name__=_c
_BgpRouteMapSeLocPrefDef_Object=MibTableColumn
bgpRouteMapSeLocPrefDef=_BgpRouteMapSeLocPrefDef_Object((1,3,6,1,4,1,164,11,4,7,1,8),_BgpRouteMapSeLocPrefDef_Type())
bgpRouteMapSeLocPrefDef.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeLocPrefDef.setStatus(_A)
class _BgpRouteMapSeMed_Type(Unsigned32):defaultValue=0
_BgpRouteMapSeMed_Type.__name__=_V
_BgpRouteMapSeMed_Object=MibTableColumn
bgpRouteMapSeMed=_BgpRouteMapSeMed_Object((1,3,6,1,4,1,164,11,4,7,1,9),_BgpRouteMapSeMed_Type())
bgpRouteMapSeMed.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeMed.setStatus(_A)
class _BgpRouteMapSeMedDef_Type(TruthValue):defaultValue=2
_BgpRouteMapSeMedDef_Type.__name__=_c
_BgpRouteMapSeMedDef_Object=MibTableColumn
bgpRouteMapSeMedDef=_BgpRouteMapSeMedDef_Object((1,3,6,1,4,1,164,11,4,7,1,10),_BgpRouteMapSeMedDef_Type())
bgpRouteMapSeMedDef.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeMedDef.setStatus(_A)
class _BgpRouteMapSeAsPrependCount_Type(Unsigned32):defaultValue=0
_BgpRouteMapSeAsPrependCount_Type.__name__=_V
_BgpRouteMapSeAsPrependCount_Object=MibTableColumn
bgpRouteMapSeAsPrependCount=_BgpRouteMapSeAsPrependCount_Object((1,3,6,1,4,1,164,11,4,7,1,11),_BgpRouteMapSeAsPrependCount_Type())
bgpRouteMapSeAsPrependCount.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeAsPrependCount.setStatus(_A)
class _BgpRouteMapSeAsPrependSize_Type(BgpAsSize):defaultValue=1
_BgpRouteMapSeAsPrependSize_Type.__name__=_A0
_BgpRouteMapSeAsPrependSize_Object=MibTableColumn
bgpRouteMapSeAsPrependSize=_BgpRouteMapSeAsPrependSize_Object((1,3,6,1,4,1,164,11,4,7,1,12),_BgpRouteMapSeAsPrependSize_Type())
bgpRouteMapSeAsPrependSize.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeAsPrependSize.setStatus(_A)
class _BgpRouteMapSeAsPrependAsVals_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BgpRouteMapSeAsPrependAsVals_Type.__name__=_K
_BgpRouteMapSeAsPrependAsVals_Object=MibTableColumn
bgpRouteMapSeAsPrependAsVals=_BgpRouteMapSeAsPrependAsVals_Object((1,3,6,1,4,1,164,11,4,7,1,13),_BgpRouteMapSeAsPrependAsVals_Type())
bgpRouteMapSeAsPrependAsVals.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapSeAsPrependAsVals.setStatus(_A)
class _BgpRouteMapMaPrefixListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_BgpRouteMapMaPrefixListName_Type.__name__=_U
_BgpRouteMapMaPrefixListName_Object=MibTableColumn
bgpRouteMapMaPrefixListName=_BgpRouteMapMaPrefixListName_Object((1,3,6,1,4,1,164,11,4,7,1,14),_BgpRouteMapMaPrefixListName_Type())
bgpRouteMapMaPrefixListName.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapMaPrefixListName.setStatus(_A)
class _BgpRouteMapMaAsExp_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_BgpRouteMapMaAsExp_Type.__name__=_U
_BgpRouteMapMaAsExp_Object=MibTableColumn
bgpRouteMapMaAsExp=_BgpRouteMapMaAsExp_Object((1,3,6,1,4,1,164,11,4,7,1,15),_BgpRouteMapMaAsExp_Type())
bgpRouteMapMaAsExp.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpRouteMapMaAsExp.setStatus(_A)
_BgpIpPreTable_Object=MibTable
bgpIpPreTable=_BgpIpPreTable_Object((1,3,6,1,4,1,164,11,4,8))
if mibBuilder.loadTexts:bgpIpPreTable.setStatus(_A)
_BgpIpPreEntry_Object=MibTableRow
bgpIpPreEntry=_BgpIpPreEntry_Object((1,3,6,1,4,1,164,11,4,8,1))
bgpIpPreEntry.setIndexNames((0,_B,_Y),(0,_B,_Z),(0,_B,_A1),(0,_B,_A2))
if mibBuilder.loadTexts:bgpIpPreEntry.setStatus(_A)
_BgpIpPreMatch_Type=BgpIpMatchType
_BgpIpPreMatch_Object=MibTableColumn
bgpIpPreMatch=_BgpIpPreMatch_Object((1,3,6,1,4,1,164,11,4,8,1,1),_BgpIpPreMatch_Type())
bgpIpPreMatch.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpIpPreMatch.setStatus(_A)
_BgpIpPreNumber_Type=Unsigned32
_BgpIpPreNumber_Object=MibTableColumn
bgpIpPreNumber=_BgpIpPreNumber_Object((1,3,6,1,4,1,164,11,4,8,1,2),_BgpIpPreNumber_Type())
bgpIpPreNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpIpPreNumber.setStatus(_A)
class _BgpIpPreAfi_Type(InetAddressType):defaultValue=1
_BgpIpPreAfi_Type.__name__=_o
_BgpIpPreAfi_Object=MibTableColumn
bgpIpPreAfi=_BgpIpPreAfi_Object((1,3,6,1,4,1,164,11,4,8,1,3),_BgpIpPreAfi_Type())
bgpIpPreAfi.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreAfi.setStatus(_A)
class _BgpIpPreSafi_Type(BgpSafi):defaultValue=1
_BgpIpPreSafi_Type.__name__='BgpSafi'
_BgpIpPreSafi_Object=MibTableColumn
bgpIpPreSafi=_BgpIpPreSafi_Object((1,3,6,1,4,1,164,11,4,8,1,4),_BgpIpPreSafi_Type())
bgpIpPreSafi.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreSafi.setStatus(_A)
class _BgpIpPreAddr_Type(InetAddress):defaultHexValue='00';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BgpIpPreAddr_Type.__name__=_m
_BgpIpPreAddr_Object=MibTableColumn
bgpIpPreAddr=_BgpIpPreAddr_Object((1,3,6,1,4,1,164,11,4,8,1,5),_BgpIpPreAddr_Type())
bgpIpPreAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreAddr.setStatus(_A)
class _BgpIpPreLen_Type(InetAddressPrefixLength):defaultValue=0
_BgpIpPreLen_Type.__name__=_n
_BgpIpPreLen_Object=MibTableColumn
bgpIpPreLen=_BgpIpPreLen_Object((1,3,6,1,4,1,164,11,4,8,1,6),_BgpIpPreLen_Type())
bgpIpPreLen.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreLen.setStatus(_A)
class _BgpIpPreGe_Type(Integer32):defaultValue=0
_BgpIpPreGe_Type.__name__=_G
_BgpIpPreGe_Object=MibTableColumn
bgpIpPreGe=_BgpIpPreGe_Object((1,3,6,1,4,1,164,11,4,8,1,7),_BgpIpPreGe_Type())
bgpIpPreGe.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreGe.setStatus(_A)
class _BgpIpPreLe_Type(Integer32):defaultValue=0
_BgpIpPreLe_Type.__name__=_G
_BgpIpPreLe_Object=MibTableColumn
bgpIpPreLe=_BgpIpPreLe_Object((1,3,6,1,4,1,164,11,4,8,1,8),_BgpIpPreLe_Type())
bgpIpPreLe.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreLe.setStatus(_A)
class _BgpIpPreType_Type(BgpPermitOrDeny):defaultValue=1
_BgpIpPreType_Type.__name__=_i
_BgpIpPreType_Object=MibTableColumn
bgpIpPreType=_BgpIpPreType_Object((1,3,6,1,4,1,164,11,4,8,1,9),_BgpIpPreType_Type())
bgpIpPreType.setMaxAccess(_J)
if mibBuilder.loadTexts:bgpIpPreType.setStatus(_A)
_BgpPolicyBindTable_Object=MibTable
bgpPolicyBindTable=_BgpPolicyBindTable_Object((1,3,6,1,4,1,164,11,4,9))
if mibBuilder.loadTexts:bgpPolicyBindTable.setStatus(_A)
_BgpPolicyBindEntry_Object=MibTableRow
bgpPolicyBindEntry=_BgpPolicyBindEntry_Object((1,3,6,1,4,1,164,11,4,9,1))
bgpPolicyBindEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_W),(0,_B,_X),(0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:bgpPolicyBindEntry.setStatus(_A)
class _BgpPolicyBindDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('inbound',2),('outbound',3)))
_BgpPolicyBindDirection_Type.__name__=_G
_BgpPolicyBindDirection_Object=MibTableColumn
bgpPolicyBindDirection=_BgpPolicyBindDirection_Object((1,3,6,1,4,1,164,11,4,9,1,1),_BgpPolicyBindDirection_Type())
bgpPolicyBindDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPolicyBindDirection.setStatus(_A)
class _BgpPolicyBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('bgpPrefixListIpv4',2),('bgpPrefixListIpv6',3),('bgpRouteMap',4)))
_BgpPolicyBindType_Type.__name__=_G
_BgpPolicyBindType_Object=MibTableColumn
bgpPolicyBindType=_BgpPolicyBindType_Object((1,3,6,1,4,1,164,11,4,9,1,2),_BgpPolicyBindType_Type())
bgpPolicyBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPolicyBindType.setStatus(_A)
_BgpPolicyBindNumber_Type=Integer32
_BgpPolicyBindNumber_Object=MibTableColumn
bgpPolicyBindNumber=_BgpPolicyBindNumber_Object((1,3,6,1,4,1,164,11,4,9,1,3),_BgpPolicyBindNumber_Type())
bgpPolicyBindNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPolicyBindNumber.setStatus(_A)
class _BgpPolicyBindName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,252))
_BgpPolicyBindName_Type.__name__=_U
_BgpPolicyBindName_Object=MibTableColumn
bgpPolicyBindName=_BgpPolicyBindName_Object((1,3,6,1,4,1,164,11,4,9,1,4),_BgpPolicyBindName_Type())
bgpPolicyBindName.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPolicyBindName.setStatus(_A)
class _BgpPolicyBindClearStatisticsCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('on',2)))
_BgpPolicyBindClearStatisticsCmd_Type.__name__=_G
_BgpPolicyBindClearStatisticsCmd_Object=MibTableColumn
bgpPolicyBindClearStatisticsCmd=_BgpPolicyBindClearStatisticsCmd_Object((1,3,6,1,4,1,164,11,4,9,1,5),_BgpPolicyBindClearStatisticsCmd_Type())
bgpPolicyBindClearStatisticsCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPolicyBindClearStatisticsCmd.setStatus(_A)
_BgpPolicyBindRowStatus_Type=RowStatus
_BgpPolicyBindRowStatus_Object=MibTableColumn
bgpPolicyBindRowStatus=_BgpPolicyBindRowStatus_Object((1,3,6,1,4,1,164,11,4,9,1,6),_BgpPolicyBindRowStatus_Type())
bgpPolicyBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPolicyBindRowStatus.setStatus(_A)
_BgpPolicyRuleStatsTable_Object=MibTable
bgpPolicyRuleStatsTable=_BgpPolicyRuleStatsTable_Object((1,3,6,1,4,1,164,11,4,10))
if mibBuilder.loadTexts:bgpPolicyRuleStatsTable.setStatus(_A)
_BgpPolicyRuleStatsEntry_Object=MibTableRow
bgpPolicyRuleStatsEntry=_BgpPolicyRuleStatsEntry_Object((1,3,6,1,4,1,164,11,4,10,1))
bgpPolicyRuleStatsEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_W),(0,_B,_X),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:bgpPolicyRuleStatsEntry.setStatus(_A)
_BgpPolicyRuleStatsMatches_Type=Gauge32
_BgpPolicyRuleStatsMatches_Object=MibTableColumn
bgpPolicyRuleStatsMatches=_BgpPolicyRuleStatsMatches_Object((1,3,6,1,4,1,164,11,4,10,1,1),_BgpPolicyRuleStatsMatches_Type())
bgpPolicyRuleStatsMatches.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPolicyRuleStatsMatches.setStatus(_A)
class _BgpPolicyRuleStatsClearCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),('on',2),('softClear',3)))
_BgpPolicyRuleStatsClearCmd_Type.__name__=_G
_BgpPolicyRuleStatsClearCmd_Object=MibTableColumn
bgpPolicyRuleStatsClearCmd=_BgpPolicyRuleStatsClearCmd_Object((1,3,6,1,4,1,164,11,4,10,1,2),_BgpPolicyRuleStatsClearCmd_Type())
bgpPolicyRuleStatsClearCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPolicyRuleStatsClearCmd.setStatus(_A)
_BgpPathAttrExtensions_ObjectIdentity=ObjectIdentity
bgpPathAttrExtensions=_BgpPathAttrExtensions_ObjectIdentity((1,3,6,1,4,1,164,11,4,11))
_BgpPathAttrCommTable_Object=MibTable
bgpPathAttrCommTable=_BgpPathAttrCommTable_Object((1,3,6,1,4,1,164,11,4,11,1))
if mibBuilder.loadTexts:bgpPathAttrCommTable.setStatus(_A)
_BgpPathAttrCommEntry_Object=MibTableRow
bgpPathAttrCommEntry=_BgpPathAttrCommEntry_Object((1,3,6,1,4,1,164,11,4,11,1,1))
bgpPathAttrCommEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h),(0,_B,_A3))
if mibBuilder.loadTexts:bgpPathAttrCommEntry.setStatus(_A)
_BgpPathAttrCommIndex_Type=Unsigned32
_BgpPathAttrCommIndex_Object=MibTableColumn
bgpPathAttrCommIndex=_BgpPathAttrCommIndex_Object((1,3,6,1,4,1,164,11,4,11,1,1,1),_BgpPathAttrCommIndex_Type())
bgpPathAttrCommIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bgpPathAttrCommIndex.setStatus(_A)
_BgpPathAttrCommValue_Type=BgpCommunity
_BgpPathAttrCommValue_Object=MibTableColumn
bgpPathAttrCommValue=_BgpPathAttrCommValue_Object((1,3,6,1,4,1,164,11,4,11,1,1,2),_BgpPathAttrCommValue_Type())
bgpPathAttrCommValue.setMaxAccess(_D)
if mibBuilder.loadTexts:bgpPathAttrCommValue.setStatus(_A)
bgpSessionFailure=NotificationType((1,3,6,1,4,1,164,6,1,11,0,3))
bgpSessionFailure.setObjects(*((_F,_Q),(_F,_M),(_F,_O),(_F,_P),(_F,_N),(_F,_R),(_B,_a),(_S,_T)))
if mibBuilder.loadTexts:bgpSessionFailure.setStatus(_A)
bgpTcpSessionAuthFailure=NotificationType((1,3,6,1,4,1,164,6,1,11,0,4))
bgpTcpSessionAuthFailure.setObjects(*((_F,_Q),(_F,_M),(_F,_O),(_F,_P),(_F,_N),(_F,_R),(_B,_a),(_S,_T)))
if mibBuilder.loadTexts:bgpTcpSessionAuthFailure.setStatus(_A)
bgpSessionPrefixOverflow=NotificationType((1,3,6,1,4,1,164,6,1,11,0,5))
bgpSessionPrefixOverflow.setObjects(*((_F,_Q),(_F,_M),(_F,_O),(_F,_P),(_F,_N),(_F,_R),(_B,_a),(_S,_T)))
if mibBuilder.loadTexts:bgpSessionPrefixOverflow.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BgpAutonomousSystemNumber':BgpAutonomousSystemNumber,'BgpIdentifier':BgpIdentifier,'BgpPeerStates':BgpPeerStates,'BgpCapabilities':BgpCapabilities,_i:BgpPermitOrDeny,'BgpSafi':BgpSafi,'BgpCommunity':BgpCommunity,_z:BgpCommunityAction,'BgpIpMatchType':BgpIpMatchType,_A0:BgpAsSize,'bgpSessionFailure':bgpSessionFailure,'bgpTcpSessionAuthFailure':bgpTcpSessionAuthFailure,'bgpSessionPrefixOverflow':bgpSessionPrefixOverflow,'rtrBgp':rtrBgp,'bgpRibManagerTable':bgpRibManagerTable,'bgpRibManagerEntry':bgpRibManagerEntry,_p:bgpRibManagerIndex,'bgpRibManagerRowStatus':bgpRibManagerRowStatus,'bgpRibManagerLocalAs':bgpRibManagerLocalAs,'bgpRibManagerLocalIdentifier':bgpRibManagerLocalIdentifier,'bgpPeerTable':bgpPeerTable,'bgpPeerEntry':bgpPeerEntry,_H:bgpPeerRemoteAddrType,_I:bgpPeerRemoteAddr,'bgpPeerFsmState':bgpPeerFsmState,'bgpPeerRowStatus':bgpPeerRowStatus,'bgpPeerLocalAddrType':bgpPeerLocalAddrType,'bgpPeerLocalAddr':bgpPeerLocalAddr,'bgpPeerRemoteAs':bgpPeerRemoteAs,'bgpPeerLastError':bgpPeerLastError,'bgpPeerFsmEstablishedTime':bgpPeerFsmEstablishedTime,'bgpPeerHoldTimeConfig':bgpPeerHoldTimeConfig,'bgpPeerKeepAliveConfig':bgpPeerKeepAliveConfig,'bgpPeerHoldTime':bgpPeerHoldTime,'bgpPeerKeepAlive':bgpPeerKeepAlive,'bgpPeerConfigMaxPrefix':bgpPeerConfigMaxPrefix,'bgpPeerPassword':bgpPeerPassword,'bgpPeerCapabilitySent':bgpPeerCapabilitySent,'bgpPeerCapabilityRcv':bgpPeerCapabilityRcv,'bgpPeerCapabilityNegotiated':bgpPeerCapabilityNegotiated,'bgpPeerSelectedLocalAddr':bgpPeerSelectedLocalAddr,'bgpPeerSelectedLocalPort':bgpPeerSelectedLocalPort,'bgpPeerSelectedRemotePort':bgpPeerSelectedRemotePort,'bgpPeerClearCmd':bgpPeerClearCmd,_a:bgpPeerDescr,'bgpPeerAfiSafiTable':bgpPeerAfiSafiTable,'bgpPeerAfiSafiEntry':bgpPeerAfiSafiEntry,_W:bgpPeerAfiSafiAfiType,_X:bgpPeerAfiSafiSafi,'bgpPeerAfiSafiStatus':bgpPeerAfiSafiStatus,'bgpNlriTable':bgpNlriTable,'bgpNlriEntry':bgpNlriEntry,_e:bgpNlriAfiType,_f:bgpNlriSafi,_g:bgpNlriPerfixAddress,_h:bgpNlriPrefixLen,'bgpNlriASPathStr':bgpNlriASPathStr,'bgpNlriNextHop':bgpNlriNextHop,'bgpNlriAsSize':bgpNlriAsSize,'bgpNlriPathAttrMultiExitDisc':bgpNlriPathAttrMultiExitDisc,'bgpNlriPathAttrLocalPref':bgpNlriPathAttrLocalPref,'bgpNlriBest':bgpNlriBest,'bgpNlriPathAttrMEDPrsnt':bgpNlriPathAttrMEDPrsnt,'bgpAdjRibOutTable':bgpAdjRibOutTable,'bgpAdjRibOutEntry':bgpAdjRibOutEntry,_q:bgpAdjRibOutAfiType,_r:bgpAdjRibOutSafi,_s:bgpAdjRibOutPrefix,_t:bgpAdjRibOutPrefixLen,'bgpAdjRibOutAdvertStatus':bgpAdjRibOutAdvertStatus,'bgpAdjRibOutASPathStr':bgpAdjRibOutASPathStr,'bgpAdjRibOutNextHop':bgpAdjRibOutNextHop,'bgpAdjRibOutAsSize':bgpAdjRibOutAsSize,'bgpAdjRibOutMultiExitDisc':bgpAdjRibOutMultiExitDisc,'bgpAdjRibOutLocalPref':bgpAdjRibOutLocalPref,'bgpAdjRibOutMEDPrsnt':bgpAdjRibOutMEDPrsnt,'bgpNetworkTable':bgpNetworkTable,'bgpNetworkEntry':bgpNetworkEntry,_u:bgpNetworkAfiType,_v:bgpNetworkSafi,_w:bgpNetworkAddrType,_x:bgpNetworkPrefixAddr,_y:bgpNetworkPrefixLen,'bgpNetworkRowStatus':bgpNetworkRowStatus,'bgpRouteMapTable':bgpRouteMapTable,'bgpRouteMapEntry':bgpRouteMapEntry,_Y:bgpRouteMapIndex,_Z:bgpRouteMapNumber,'bgpRouteMapType':bgpRouteMapType,'bgpRouteMapMaComm':bgpRouteMapMaComm,'bgpRouteMapSeComm':bgpRouteMapSeComm,'bgpRouteMapSeCommAct':bgpRouteMapSeCommAct,'bgpRouteMapSeLocPref':bgpRouteMapSeLocPref,'bgpRouteMapSeLocPrefDef':bgpRouteMapSeLocPrefDef,'bgpRouteMapSeMed':bgpRouteMapSeMed,'bgpRouteMapSeMedDef':bgpRouteMapSeMedDef,'bgpRouteMapSeAsPrependCount':bgpRouteMapSeAsPrependCount,'bgpRouteMapSeAsPrependSize':bgpRouteMapSeAsPrependSize,'bgpRouteMapSeAsPrependAsVals':bgpRouteMapSeAsPrependAsVals,'bgpRouteMapMaPrefixListName':bgpRouteMapMaPrefixListName,'bgpRouteMapMaAsExp':bgpRouteMapMaAsExp,'bgpIpPreTable':bgpIpPreTable,'bgpIpPreEntry':bgpIpPreEntry,_A1:bgpIpPreMatch,_A2:bgpIpPreNumber,'bgpIpPreAfi':bgpIpPreAfi,'bgpIpPreSafi':bgpIpPreSafi,'bgpIpPreAddr':bgpIpPreAddr,'bgpIpPreLen':bgpIpPreLen,'bgpIpPreGe':bgpIpPreGe,'bgpIpPreLe':bgpIpPreLe,'bgpIpPreType':bgpIpPreType,'bgpPolicyBindTable':bgpPolicyBindTable,'bgpPolicyBindEntry':bgpPolicyBindEntry,_j:bgpPolicyBindDirection,_k:bgpPolicyBindType,_l:bgpPolicyBindNumber,'bgpPolicyBindName':bgpPolicyBindName,'bgpPolicyBindClearStatisticsCmd':bgpPolicyBindClearStatisticsCmd,'bgpPolicyBindRowStatus':bgpPolicyBindRowStatus,'bgpPolicyRuleStatsTable':bgpPolicyRuleStatsTable,'bgpPolicyRuleStatsEntry':bgpPolicyRuleStatsEntry,'bgpPolicyRuleStatsMatches':bgpPolicyRuleStatsMatches,'bgpPolicyRuleStatsClearCmd':bgpPolicyRuleStatsClearCmd,'bgpPathAttrExtensions':bgpPathAttrExtensions,'bgpPathAttrCommTable':bgpPathAttrCommTable,'bgpPathAttrCommEntry':bgpPathAttrCommEntry,_A3:bgpPathAttrCommIndex,'bgpPathAttrCommValue':bgpPathAttrCommValue})