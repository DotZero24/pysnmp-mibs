_At='slcEventHost'
_As='slcRPMAction'
_Ar='slcDevRPMName'
_Aq='slcSDCardAction'
_Ap='slcDevPortErrorStatus'
_Ao='slcUSBType'
_An='slcUSBAction'
_Am='slcSystemInternalTemp'
_Al='slcPCCardType'
_Ak='slcPCCardAction'
_Aj='slcPCCardSlot'
_Ai='slcDevPortDeviceErrorStatus'
_Ah='slcDevPortCfgDevHighHumidity'
_Ag='slcDevPortCfgDevLowHumidity'
_Af='slcDevPortCfgDevHighTemp'
_Ae='slcDevPortCfgDevLowTemp'
_Ad='slcDevPortTimeFrame'
_Ac='slcDevPortStartByte'
_Ab='slcHostname'
_Aa='slcDevPortCfgEmailTextString'
_AZ='slcDevPortData'
_AY='slcPowerSupplyAction'
_AX='slcPowerSupplyId'
_AW='deviceRemoved'
_AV='deviceInserted'
_AU='slcConnIndex'
_AT='RPMOutletIndex'
_AS='tenths of Watts'
_AR='tenths of Volt-Amps'
_AQ='tenths of Amps'
_AP='RPMTowerIndex'
_AO='hundredths of seconds'
_AN='notmounted'
_AM='slcPCCardCfgIndex'
_AL='slcDevPortStateIndex'
_AK='cyclePower'
_AJ='lowerSlot'
_AI='upperSlot'
_AH='slcAuthGroupIndex'
_AG='slcAuthRemoteUserIndex'
_AF='slcAuthRADIUSServerIndex'
_AE='slcAuthLocalUserIndex'
_AD='slcServSiteIndex'
_AC='slcServHostListIndex'
_AB='slcServSLCNetIndex'
_AA='slcServNFSMountIndex'
_A9='tripledes'
_A8='slcNetRouteStaticIndex'
_A7='internalModem'
_A6='devicePort'
_A5='lowerPCCard'
_A4='upperPCCard'
_A3='slcNetFirewallMappingIndex'
_A2='slcNetFirewallRulesetIndex'
_A1='slcNetEthIfIndex'
_A0='slcDevPortCfgDevHumidity'
_z='slcDevPortCfgDevTemperature'
_y='tenths of a percent'
_x='slcDevUSBId'
_w='userDefined'
_v='adminDefined'
_u='read-write'
_t='noAction'
_s='cbcpClient'
_r='cbcpServer'
_q='dialinHostList'
_p='dialinAndDialondemand'
_o='dialondemand'
_n='Kilobytes'
_m='md5'
_l='aes'
_k='ethernet2'
_j='ethernet1'
_i='gprs'
_h='slcDevPortNumBytes'
_g='slcDevRPMId'
_f='gsmmodem'
_e='wireless'
_d='isdn'
_c='modem'
_b='storage'
_a='fixed'
_Z='usernumber'
_Y='text'
_X='ppp'
_W='dialback'
_V='dialin'
_U='dialout'
_T='rtscts'
_S='xonxoff'
_R='even'
_Q='odd'
_P='bytes'
_O='any'
_N='chap'
_M='pap'
_L='disabled'
_K='Celsius'
_J='slcDevPortId'
_I='obsolete'
_H='minutes'
_G='none'
_F='OctetString'
_E='seconds'
_D='LANTRONIX-SLC-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
products,=mibBuilder.importSymbols('LANTRONIX-MIB','products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
slc=ModuleIdentity((1,3,6,1,4,1,244,1,1))
if mibBuilder.loadTexts:slc.setRevisions(('2016-04-17 00:00','2015-02-24 00:00','2014-07-10 00:00','2013-12-06 00:00','2013-02-20 00:00','2010-04-07 00:00','2010-01-19 00:00','2009-12-09 00:00','2008-01-09 00:00','2007-06-25 00:00','2007-02-20 00:00','2007-02-07 00:00','2006-10-20 00:00','2006-07-14 00:00','2006-05-12 00:00','2006-02-13 00:00','2005-10-03 00:00','2005-06-09 00:00','2004-12-13 00:00'))
class EnabledState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('enabled',2)))
class AuthOrder(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
class SyslogLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('info',2),('warning',3),('error',4),('debug',5)))
class UserGroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('default',1),('power',2),('administrators',3),('custom',4)))
class UserRights(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class TimeoutDataDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('incomingNetwork',1),('outgoingNetwork',2),('bothDirections',3)))
class RPMTowerIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
class RPMOutletIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SlcEvents_ObjectIdentity=ObjectIdentity
slcEvents=_SlcEvents_ObjectIdentity((1,3,6,1,4,1,244,1,1,0))
_SlcNetwork_ObjectIdentity=ObjectIdentity
slcNetwork=_SlcNetwork_ObjectIdentity((1,3,6,1,4,1,244,1,1,1))
_SlcNetEth_ObjectIdentity=ObjectIdentity
slcNetEth=_SlcNetEth_ObjectIdentity((1,3,6,1,4,1,244,1,1,1,1))
class _SlcNetEthIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SlcNetEthIfNumber_Type.__name__=_C
_SlcNetEthIfNumber_Object=MibScalar
slcNetEthIfNumber=_SlcNetEthIfNumber_Object((1,3,6,1,4,1,244,1,1,1,1,1),_SlcNetEthIfNumber_Type())
slcNetEthIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfNumber.setStatus(_A)
_SlcNetEthIfTable_Object=MibTable
slcNetEthIfTable=_SlcNetEthIfTable_Object((1,3,6,1,4,1,244,1,1,1,1,2))
if mibBuilder.loadTexts:slcNetEthIfTable.setStatus(_A)
_SlcNetEthIfEntry_Object=MibTableRow
slcNetEthIfEntry=_SlcNetEthIfEntry_Object((1,3,6,1,4,1,244,1,1,1,1,2,1))
slcNetEthIfEntry.setIndexNames((0,_D,_A1))
if mibBuilder.loadTexts:slcNetEthIfEntry.setStatus(_A)
class _SlcNetEthIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SlcNetEthIfIndex_Type.__name__=_C
_SlcNetEthIfIndex_Object=MibTableColumn
slcNetEthIfIndex=_SlcNetEthIfIndex_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,1),_SlcNetEthIfIndex_Type())
slcNetEthIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfIndex.setStatus(_A)
class _SlcNetEthIfSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('dhcp',2),('bootp',3),('static',4)))
_SlcNetEthIfSource_Type.__name__=_C
_SlcNetEthIfSource_Object=MibTableColumn
slcNetEthIfSource=_SlcNetEthIfSource_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,2),_SlcNetEthIfSource_Type())
slcNetEthIfSource.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfSource.setStatus(_A)
class _SlcNetEthIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('autoNegotiate',1),('halfDuplex10mbit',2),('fullDuplex10mbit',3),('halfDuplex100mbit',4),('fullDuplex100mbit',5),('halfDuplex1000mbit',6),('fullDuplex1000mbit',7)))
_SlcNetEthIfMode_Type.__name__=_C
_SlcNetEthIfMode_Object=MibTableColumn
slcNetEthIfMode=_SlcNetEthIfMode_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,3),_SlcNetEthIfMode_Type())
slcNetEthIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfMode.setStatus(_A)
_SlcNetEthIfIPv6Addr_Type=Ipv6Address
_SlcNetEthIfIPv6Addr_Object=MibTableColumn
slcNetEthIfIPv6Addr=_SlcNetEthIfIPv6Addr_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,4),_SlcNetEthIfIPv6Addr_Type())
slcNetEthIfIPv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfIPv6Addr.setStatus(_A)
class _SlcNetEthIfIPv6PrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_SlcNetEthIfIPv6PrefixLength_Type.__name__=_C
_SlcNetEthIfIPv6PrefixLength_Object=MibTableColumn
slcNetEthIfIPv6PrefixLength=_SlcNetEthIfIPv6PrefixLength_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,5),_SlcNetEthIfIPv6PrefixLength_Type())
slcNetEthIfIPv6PrefixLength.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:slcNetEthIfIPv6PrefixLength.setStatus(_A)
_SlcNetEthIfMTU_Type=Integer32
_SlcNetEthIfMTU_Object=MibTableColumn
slcNetEthIfMTU=_SlcNetEthIfMTU_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,6),_SlcNetEthIfMTU_Type())
slcNetEthIfMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfMTU.setStatus(_A)
_SlcNetEthIfMacAddress_Type=MacAddress
_SlcNetEthIfMacAddress_Object=MibTableColumn
slcNetEthIfMacAddress=_SlcNetEthIfMacAddress_Object((1,3,6,1,4,1,244,1,1,1,1,2,1,7),_SlcNetEthIfMacAddress_Type())
slcNetEthIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIfMacAddress.setStatus(_A)
_SlcNetEthGateway_Type=IpAddress
_SlcNetEthGateway_Object=MibScalar
slcNetEthGateway=_SlcNetEthGateway_Object((1,3,6,1,4,1,244,1,1,1,1,3),_SlcNetEthGateway_Type())
slcNetEthGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthGateway.setStatus(_A)
class _SlcNetEthGatewayPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dhcp',1),('default',2),(_i,3)))
_SlcNetEthGatewayPrecedence_Type.__name__=_C
_SlcNetEthGatewayPrecedence_Object=MibScalar
slcNetEthGatewayPrecedence=_SlcNetEthGatewayPrecedence_Object((1,3,6,1,4,1,244,1,1,1,1,4),_SlcNetEthGatewayPrecedence_Type())
slcNetEthGatewayPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthGatewayPrecedence.setStatus(_A)
class _SlcNetEthKeepaliveStartProbes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99999))
_SlcNetEthKeepaliveStartProbes_Type.__name__=_C
_SlcNetEthKeepaliveStartProbes_Object=MibScalar
slcNetEthKeepaliveStartProbes=_SlcNetEthKeepaliveStartProbes_Object((1,3,6,1,4,1,244,1,1,1,1,5),_SlcNetEthKeepaliveStartProbes_Type())
slcNetEthKeepaliveStartProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthKeepaliveStartProbes.setStatus(_A)
class _SlcNetEthKeepaliveNumberOfProbes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SlcNetEthKeepaliveNumberOfProbes_Type.__name__=_C
_SlcNetEthKeepaliveNumberOfProbes_Object=MibScalar
slcNetEthKeepaliveNumberOfProbes=_SlcNetEthKeepaliveNumberOfProbes_Object((1,3,6,1,4,1,244,1,1,1,1,6),_SlcNetEthKeepaliveNumberOfProbes_Type())
slcNetEthKeepaliveNumberOfProbes.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthKeepaliveNumberOfProbes.setStatus(_A)
class _SlcNetEthKeepaliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_SlcNetEthKeepaliveInterval_Type.__name__=_C
_SlcNetEthKeepaliveInterval_Object=MibScalar
slcNetEthKeepaliveInterval=_SlcNetEthKeepaliveInterval_Object((1,3,6,1,4,1,244,1,1,1,1,7),_SlcNetEthKeepaliveInterval_Type())
slcNetEthKeepaliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthKeepaliveInterval.setStatus(_A)
_SlcNetEthIPForwarding_Type=EnabledState
_SlcNetEthIPForwarding_Object=MibScalar
slcNetEthIPForwarding=_SlcNetEthIPForwarding_Object((1,3,6,1,4,1,244,1,1,1,1,8),_SlcNetEthIPForwarding_Type())
slcNetEthIPForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIPForwarding.setStatus(_A)
_SlcNetEthDNS1_Type=IpAddress
_SlcNetEthDNS1_Object=MibScalar
slcNetEthDNS1=_SlcNetEthDNS1_Object((1,3,6,1,4,1,244,1,1,1,1,9),_SlcNetEthDNS1_Type())
slcNetEthDNS1.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDNS1.setStatus(_A)
_SlcNetEthDNS2_Type=IpAddress
_SlcNetEthDNS2_Object=MibScalar
slcNetEthDNS2=_SlcNetEthDNS2_Object((1,3,6,1,4,1,244,1,1,1,1,10),_SlcNetEthDNS2_Type())
slcNetEthDNS2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDNS2.setStatus(_A)
_SlcNetEthDNS3_Type=IpAddress
_SlcNetEthDNS3_Object=MibScalar
slcNetEthDNS3=_SlcNetEthDNS3_Object((1,3,6,1,4,1,244,1,1,1,1,11),_SlcNetEthDNS3_Type())
slcNetEthDNS3.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDNS3.setStatus(_A)
_SlcNetEthDomain_Type=OctetString
_SlcNetEthDomain_Object=MibScalar
slcNetEthDomain=_SlcNetEthDomain_Object((1,3,6,1,4,1,244,1,1,1,1,12),_SlcNetEthDomain_Type())
slcNetEthDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDomain.setStatus(_A)
_SlcNetEthAlternateGateway_Type=IpAddress
_SlcNetEthAlternateGateway_Object=MibScalar
slcNetEthAlternateGateway=_SlcNetEthAlternateGateway_Object((1,3,6,1,4,1,244,1,1,1,1,13),_SlcNetEthAlternateGateway_Type())
slcNetEthAlternateGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthAlternateGateway.setStatus(_A)
_SlcNetEthPingIPAddress_Type=IpAddress
_SlcNetEthPingIPAddress_Object=MibScalar
slcNetEthPingIPAddress=_SlcNetEthPingIPAddress_Object((1,3,6,1,4,1,244,1,1,1,1,14),_SlcNetEthPingIPAddress_Type())
slcNetEthPingIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthPingIPAddress.setStatus(_A)
class _SlcNetEthPingInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_SlcNetEthPingInterface_Type.__name__=_C
_SlcNetEthPingInterface_Object=MibScalar
slcNetEthPingInterface=_SlcNetEthPingInterface_Object((1,3,6,1,4,1,244,1,1,1,1,15),_SlcNetEthPingInterface_Type())
slcNetEthPingInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthPingInterface.setStatus(_A)
class _SlcNetEthPingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_SlcNetEthPingDelay_Type.__name__=_C
_SlcNetEthPingDelay_Object=MibScalar
slcNetEthPingDelay=_SlcNetEthPingDelay_Object((1,3,6,1,4,1,244,1,1,1,1,16),_SlcNetEthPingDelay_Type())
slcNetEthPingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthPingDelay.setStatus(_A)
if mibBuilder.loadTexts:slcNetEthPingDelay.setUnits(_E)
class _SlcNetEthPingFailed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_SlcNetEthPingFailed_Type.__name__=_C
_SlcNetEthPingFailed_Object=MibScalar
slcNetEthPingFailed=_SlcNetEthPingFailed_Object((1,3,6,1,4,1,244,1,1,1,1,17),_SlcNetEthPingFailed_Type())
slcNetEthPingFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthPingFailed.setStatus(_A)
class _SlcNetEthBonding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('activeBackup',2),('aggregation',3),('adaptiveLoadBalancing',4)))
_SlcNetEthBonding_Type.__name__=_C
_SlcNetEthBonding_Object=MibScalar
slcNetEthBonding=_SlcNetEthBonding_Object((1,3,6,1,4,1,244,1,1,1,1,18),_SlcNetEthBonding_Type())
slcNetEthBonding.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthBonding.setStatus(_A)
_SlcNetEthIPv6_Type=EnabledState
_SlcNetEthIPv6_Object=MibScalar
slcNetEthIPv6=_SlcNetEthIPv6_Object((1,3,6,1,4,1,244,1,1,1,1,19),_SlcNetEthIPv6_Type())
slcNetEthIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthIPv6.setStatus(_A)
_SlcNetEthGatewayIPv6_Type=Ipv6Address
_SlcNetEthGatewayIPv6_Object=MibScalar
slcNetEthGatewayIPv6=_SlcNetEthGatewayIPv6_Object((1,3,6,1,4,1,244,1,1,1,1,20),_SlcNetEthGatewayIPv6_Type())
slcNetEthGatewayIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthGatewayIPv6.setStatus(_A)
_SlcNetEthDNS1IPv6_Type=Ipv6Address
_SlcNetEthDNS1IPv6_Object=MibScalar
slcNetEthDNS1IPv6=_SlcNetEthDNS1IPv6_Object((1,3,6,1,4,1,244,1,1,1,1,21),_SlcNetEthDNS1IPv6_Type())
slcNetEthDNS1IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDNS1IPv6.setStatus(_A)
_SlcNetEthDNS2IPv6_Type=Ipv6Address
_SlcNetEthDNS2IPv6_Object=MibScalar
slcNetEthDNS2IPv6=_SlcNetEthDNS2IPv6_Object((1,3,6,1,4,1,244,1,1,1,1,22),_SlcNetEthDNS2IPv6_Type())
slcNetEthDNS2IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDNS2IPv6.setStatus(_A)
_SlcNetEthDNS3IPv6_Type=Ipv6Address
_SlcNetEthDNS3IPv6_Object=MibScalar
slcNetEthDNS3IPv6=_SlcNetEthDNS3IPv6_Object((1,3,6,1,4,1,244,1,1,1,1,23),_SlcNetEthDNS3IPv6_Type())
slcNetEthDNS3IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthDNS3IPv6.setStatus(_A)
_SlcNetEthPreferIPv4DNS_Type=EnabledState
_SlcNetEthPreferIPv4DNS_Object=MibScalar
slcNetEthPreferIPv4DNS=_SlcNetEthPreferIPv4DNS_Object((1,3,6,1,4,1,244,1,1,1,1,24),_SlcNetEthPreferIPv4DNS_Type())
slcNetEthPreferIPv4DNS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetEthPreferIPv4DNS.setStatus(_A)
_SlcNetFirewall_ObjectIdentity=ObjectIdentity
slcNetFirewall=_SlcNetFirewall_ObjectIdentity((1,3,6,1,4,1,244,1,1,1,2))
_SlcNetFirewallState_Type=EnabledState
_SlcNetFirewallState_Object=MibScalar
slcNetFirewallState=_SlcNetFirewallState_Object((1,3,6,1,4,1,244,1,1,1,2,1),_SlcNetFirewallState_Type())
slcNetFirewallState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallState.setStatus(_A)
class _SlcNetFirewallReject_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('return',1),('ignore',2)))
_SlcNetFirewallReject_Type.__name__=_C
_SlcNetFirewallReject_Object=MibScalar
slcNetFirewallReject=_SlcNetFirewallReject_Object((1,3,6,1,4,1,244,1,1,1,2,2),_SlcNetFirewallReject_Type())
slcNetFirewallReject.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallReject.setStatus(_I)
_SlcNetFirewallPing_Type=EnabledState
_SlcNetFirewallPing_Object=MibScalar
slcNetFirewallPing=_SlcNetFirewallPing_Object((1,3,6,1,4,1,244,1,1,1,2,3),_SlcNetFirewallPing_Type())
slcNetFirewallPing.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallPing.setStatus(_I)
_SlcNetFirewallSSH_Type=EnabledState
_SlcNetFirewallSSH_Object=MibScalar
slcNetFirewallSSH=_SlcNetFirewallSSH_Object((1,3,6,1,4,1,244,1,1,1,2,4),_SlcNetFirewallSSH_Type())
slcNetFirewallSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallSSH.setStatus(_I)
_SlcNetFirewallTelnet_Type=EnabledState
_SlcNetFirewallTelnet_Object=MibScalar
slcNetFirewallTelnet=_SlcNetFirewallTelnet_Object((1,3,6,1,4,1,244,1,1,1,2,5),_SlcNetFirewallTelnet_Type())
slcNetFirewallTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallTelnet.setStatus(_I)
_SlcNetFirewallHTTP_Type=EnabledState
_SlcNetFirewallHTTP_Object=MibScalar
slcNetFirewallHTTP=_SlcNetFirewallHTTP_Object((1,3,6,1,4,1,244,1,1,1,2,6),_SlcNetFirewallHTTP_Type())
slcNetFirewallHTTP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallHTTP.setStatus(_I)
_SlcNetFirewallHTTPS_Type=EnabledState
_SlcNetFirewallHTTPS_Object=MibScalar
slcNetFirewallHTTPS=_SlcNetFirewallHTTPS_Object((1,3,6,1,4,1,244,1,1,1,2,7),_SlcNetFirewallHTTPS_Type())
slcNetFirewallHTTPS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallHTTPS.setStatus(_I)
_SlcNetFirewallSMBCIFS_Type=EnabledState
_SlcNetFirewallSMBCIFS_Object=MibScalar
slcNetFirewallSMBCIFS=_SlcNetFirewallSMBCIFS_Object((1,3,6,1,4,1,244,1,1,1,2,8),_SlcNetFirewallSMBCIFS_Type())
slcNetFirewallSMBCIFS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallSMBCIFS.setStatus(_I)
class _SlcNetFirewallRulesetNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SlcNetFirewallRulesetNumber_Type.__name__=_C
_SlcNetFirewallRulesetNumber_Object=MibScalar
slcNetFirewallRulesetNumber=_SlcNetFirewallRulesetNumber_Object((1,3,6,1,4,1,244,1,1,1,2,9),_SlcNetFirewallRulesetNumber_Type())
slcNetFirewallRulesetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallRulesetNumber.setStatus(_A)
_SlcNetFirewallRulesetTable_Object=MibTable
slcNetFirewallRulesetTable=_SlcNetFirewallRulesetTable_Object((1,3,6,1,4,1,244,1,1,1,2,10))
if mibBuilder.loadTexts:slcNetFirewallRulesetTable.setStatus(_A)
_SlcNetFirewallRulesetEntry_Object=MibTableRow
slcNetFirewallRulesetEntry=_SlcNetFirewallRulesetEntry_Object((1,3,6,1,4,1,244,1,1,1,2,10,1))
slcNetFirewallRulesetEntry.setIndexNames((0,_D,_A2))
if mibBuilder.loadTexts:slcNetFirewallRulesetEntry.setStatus(_A)
class _SlcNetFirewallRulesetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SlcNetFirewallRulesetIndex_Type.__name__=_C
_SlcNetFirewallRulesetIndex_Object=MibTableColumn
slcNetFirewallRulesetIndex=_SlcNetFirewallRulesetIndex_Object((1,3,6,1,4,1,244,1,1,1,2,10,1,1),_SlcNetFirewallRulesetIndex_Type())
slcNetFirewallRulesetIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallRulesetIndex.setStatus(_A)
_SlcNetFirewallRulesetName_Type=OctetString
_SlcNetFirewallRulesetName_Object=MibTableColumn
slcNetFirewallRulesetName=_SlcNetFirewallRulesetName_Object((1,3,6,1,4,1,244,1,1,1,2,10,1,2),_SlcNetFirewallRulesetName_Type())
slcNetFirewallRulesetName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallRulesetName.setStatus(_A)
class _SlcNetFirewallRulesetNumRules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SlcNetFirewallRulesetNumRules_Type.__name__=_C
_SlcNetFirewallRulesetNumRules_Object=MibTableColumn
slcNetFirewallRulesetNumRules=_SlcNetFirewallRulesetNumRules_Object((1,3,6,1,4,1,244,1,1,1,2,10,1,3),_SlcNetFirewallRulesetNumRules_Type())
slcNetFirewallRulesetNumRules.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallRulesetNumRules.setStatus(_A)
_SlcNetFirewallRulesetRules_Type=OctetString
_SlcNetFirewallRulesetRules_Object=MibTableColumn
slcNetFirewallRulesetRules=_SlcNetFirewallRulesetRules_Object((1,3,6,1,4,1,244,1,1,1,2,10,1,4),_SlcNetFirewallRulesetRules_Type())
slcNetFirewallRulesetRules.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallRulesetRules.setStatus(_A)
_SlcNetFirewallMappingNumber_Type=Integer32
_SlcNetFirewallMappingNumber_Object=MibScalar
slcNetFirewallMappingNumber=_SlcNetFirewallMappingNumber_Object((1,3,6,1,4,1,244,1,1,1,2,11),_SlcNetFirewallMappingNumber_Type())
slcNetFirewallMappingNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallMappingNumber.setStatus(_A)
_SlcNetFirewallMappingTable_Object=MibTable
slcNetFirewallMappingTable=_SlcNetFirewallMappingTable_Object((1,3,6,1,4,1,244,1,1,1,2,12))
if mibBuilder.loadTexts:slcNetFirewallMappingTable.setStatus(_A)
_SlcNetFirewallMappingEntry_Object=MibTableRow
slcNetFirewallMappingEntry=_SlcNetFirewallMappingEntry_Object((1,3,6,1,4,1,244,1,1,1,2,12,1))
slcNetFirewallMappingEntry.setIndexNames((0,_D,_A3))
if mibBuilder.loadTexts:slcNetFirewallMappingEntry.setStatus(_A)
class _SlcNetFirewallMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SlcNetFirewallMappingIndex_Type.__name__=_C
_SlcNetFirewallMappingIndex_Object=MibTableColumn
slcNetFirewallMappingIndex=_SlcNetFirewallMappingIndex_Object((1,3,6,1,4,1,244,1,1,1,2,12,1,1),_SlcNetFirewallMappingIndex_Type())
slcNetFirewallMappingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallMappingIndex.setStatus(_A)
class _SlcNetFirewallMappingIfac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_j,1),(_k,2),(_A4,3),(_A5,4),(_A6,5),('usbPort',6),(_A7,7)))
_SlcNetFirewallMappingIfac_Type.__name__=_C
_SlcNetFirewallMappingIfac_Object=MibTableColumn
slcNetFirewallMappingIfac=_SlcNetFirewallMappingIfac_Object((1,3,6,1,4,1,244,1,1,1,2,12,1,2),_SlcNetFirewallMappingIfac_Type())
slcNetFirewallMappingIfac.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallMappingIfac.setStatus(_A)
class _SlcNetFirewallMappingIfacId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_SlcNetFirewallMappingIfacId_Type.__name__=_C
_SlcNetFirewallMappingIfacId_Object=MibTableColumn
slcNetFirewallMappingIfacId=_SlcNetFirewallMappingIfacId_Object((1,3,6,1,4,1,244,1,1,1,2,12,1,3),_SlcNetFirewallMappingIfacId_Type())
slcNetFirewallMappingIfacId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallMappingIfacId.setStatus(_A)
_SlcNetFirewallMappingRuleset_Type=OctetString
_SlcNetFirewallMappingRuleset_Object=MibTableColumn
slcNetFirewallMappingRuleset=_SlcNetFirewallMappingRuleset_Object((1,3,6,1,4,1,244,1,1,1,2,12,1,4),_SlcNetFirewallMappingRuleset_Type())
slcNetFirewallMappingRuleset.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetFirewallMappingRuleset.setStatus(_A)
_SlcNetRouting_ObjectIdentity=ObjectIdentity
slcNetRouting=_SlcNetRouting_ObjectIdentity((1,3,6,1,4,1,244,1,1,1,3))
_SlcNetRouteRIPState_Type=EnabledState
_SlcNetRouteRIPState_Object=MibScalar
slcNetRouteRIPState=_SlcNetRouteRIPState_Object((1,3,6,1,4,1,244,1,1,1,3,1),_SlcNetRouteRIPState_Type())
slcNetRouteRIPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteRIPState.setStatus(_A)
class _SlcNetRouteRIPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndTwo',3)))
_SlcNetRouteRIPVersion_Type.__name__=_C
_SlcNetRouteRIPVersion_Object=MibScalar
slcNetRouteRIPVersion=_SlcNetRouteRIPVersion_Object((1,3,6,1,4,1,244,1,1,1,3,2),_SlcNetRouteRIPVersion_Type())
slcNetRouteRIPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteRIPVersion.setStatus(_A)
_SlcNetRouteStaticState_Type=EnabledState
_SlcNetRouteStaticState_Object=MibScalar
slcNetRouteStaticState=_SlcNetRouteStaticState_Object((1,3,6,1,4,1,244,1,1,1,3,3),_SlcNetRouteStaticState_Type())
slcNetRouteStaticState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteStaticState.setStatus(_A)
class _SlcNetRouteStaticNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SlcNetRouteStaticNumber_Type.__name__=_C
_SlcNetRouteStaticNumber_Object=MibScalar
slcNetRouteStaticNumber=_SlcNetRouteStaticNumber_Object((1,3,6,1,4,1,244,1,1,1,3,4),_SlcNetRouteStaticNumber_Type())
slcNetRouteStaticNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteStaticNumber.setStatus(_A)
_SlcNetRouteStaticTable_Object=MibTable
slcNetRouteStaticTable=_SlcNetRouteStaticTable_Object((1,3,6,1,4,1,244,1,1,1,3,5))
if mibBuilder.loadTexts:slcNetRouteStaticTable.setStatus(_A)
_SlcNetRouteStaticEntry_Object=MibTableRow
slcNetRouteStaticEntry=_SlcNetRouteStaticEntry_Object((1,3,6,1,4,1,244,1,1,1,3,5,1))
slcNetRouteStaticEntry.setIndexNames((0,_D,_A8))
if mibBuilder.loadTexts:slcNetRouteStaticEntry.setStatus(_A)
class _SlcNetRouteStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_SlcNetRouteStaticIndex_Type.__name__=_C
_SlcNetRouteStaticIndex_Object=MibTableColumn
slcNetRouteStaticIndex=_SlcNetRouteStaticIndex_Object((1,3,6,1,4,1,244,1,1,1,3,5,1,1),_SlcNetRouteStaticIndex_Type())
slcNetRouteStaticIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteStaticIndex.setStatus(_A)
_SlcNetRouteStaticIP_Type=IpAddress
_SlcNetRouteStaticIP_Object=MibTableColumn
slcNetRouteStaticIP=_SlcNetRouteStaticIP_Object((1,3,6,1,4,1,244,1,1,1,3,5,1,2),_SlcNetRouteStaticIP_Type())
slcNetRouteStaticIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteStaticIP.setStatus(_A)
_SlcNetRouteStaticMask_Type=IpAddress
_SlcNetRouteStaticMask_Object=MibTableColumn
slcNetRouteStaticMask=_SlcNetRouteStaticMask_Object((1,3,6,1,4,1,244,1,1,1,3,5,1,3),_SlcNetRouteStaticMask_Type())
slcNetRouteStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteStaticMask.setStatus(_A)
_SlcNetRouteStaticGateway_Type=IpAddress
_SlcNetRouteStaticGateway_Object=MibTableColumn
slcNetRouteStaticGateway=_SlcNetRouteStaticGateway_Object((1,3,6,1,4,1,244,1,1,1,3,5,1,4),_SlcNetRouteStaticGateway_Type())
slcNetRouteStaticGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetRouteStaticGateway.setStatus(_A)
_SlcNetVPN_ObjectIdentity=ObjectIdentity
slcNetVPN=_SlcNetVPN_ObjectIdentity((1,3,6,1,4,1,244,1,1,1,4))
_SlcNetVPNTunnel_Type=EnabledState
_SlcNetVPNTunnel_Object=MibScalar
slcNetVPNTunnel=_SlcNetVPNTunnel_Object((1,3,6,1,4,1,244,1,1,1,4,1),_SlcNetVPNTunnel_Type())
slcNetVPNTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNTunnel.setStatus(_A)
_SlcNetVPNStatus_Type=OctetString
_SlcNetVPNStatus_Object=MibScalar
slcNetVPNStatus=_SlcNetVPNStatus_Object((1,3,6,1,4,1,244,1,1,1,4,2),_SlcNetVPNStatus_Type())
slcNetVPNStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNStatus.setStatus(_A)
class _SlcNetVPNName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlcNetVPNName_Type.__name__=_F
_SlcNetVPNName_Object=MibScalar
slcNetVPNName=_SlcNetVPNName_Object((1,3,6,1,4,1,244,1,1,1,4,3),_SlcNetVPNName_Type())
slcNetVPNName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNName.setStatus(_A)
class _SlcNetVPNEthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_SlcNetVPNEthPort_Type.__name__=_C
_SlcNetVPNEthPort_Object=MibScalar
slcNetVPNEthPort=_SlcNetVPNEthPort_Object((1,3,6,1,4,1,244,1,1,1,4,4),_SlcNetVPNEthPort_Type())
slcNetVPNEthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNEthPort.setStatus(_A)
_SlcNetVPNRemoteHost_Type=IpAddress
_SlcNetVPNRemoteHost_Object=MibScalar
slcNetVPNRemoteHost=_SlcNetVPNRemoteHost_Object((1,3,6,1,4,1,244,1,1,1,4,5),_SlcNetVPNRemoteHost_Type())
slcNetVPNRemoteHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNRemoteHost.setStatus(_A)
class _SlcNetVPNRemoteId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlcNetVPNRemoteId_Type.__name__=_F
_SlcNetVPNRemoteId_Object=MibScalar
slcNetVPNRemoteId=_SlcNetVPNRemoteId_Object((1,3,6,1,4,1,244,1,1,1,4,6),_SlcNetVPNRemoteId_Type())
slcNetVPNRemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNRemoteId.setStatus(_A)
_SlcNetVPNRemoteHop_Type=IpAddress
_SlcNetVPNRemoteHop_Object=MibScalar
slcNetVPNRemoteHop=_SlcNetVPNRemoteHop_Object((1,3,6,1,4,1,244,1,1,1,4,7),_SlcNetVPNRemoteHop_Type())
slcNetVPNRemoteHop.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNRemoteHop.setStatus(_A)
_SlcNetVPNRemoteSubnet_Type=OctetString
_SlcNetVPNRemoteSubnet_Object=MibScalar
slcNetVPNRemoteSubnet=_SlcNetVPNRemoteSubnet_Object((1,3,6,1,4,1,244,1,1,1,4,8),_SlcNetVPNRemoteSubnet_Type())
slcNetVPNRemoteSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNRemoteSubnet.setStatus(_A)
class _SlcNetVPNLocalId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlcNetVPNLocalId_Type.__name__=_F
_SlcNetVPNLocalId_Object=MibScalar
slcNetVPNLocalId=_SlcNetVPNLocalId_Object((1,3,6,1,4,1,244,1,1,1,4,9),_SlcNetVPNLocalId_Type())
slcNetVPNLocalId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNLocalId.setStatus(_A)
_SlcNetVPNLocalHop_Type=IpAddress
_SlcNetVPNLocalHop_Object=MibScalar
slcNetVPNLocalHop=_SlcNetVPNLocalHop_Object((1,3,6,1,4,1,244,1,1,1,4,10),_SlcNetVPNLocalHop_Type())
slcNetVPNLocalHop.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNLocalHop.setStatus(_A)
_SlcNetVPNLocalSubnet_Type=OctetString
_SlcNetVPNLocalSubnet_Object=MibScalar
slcNetVPNLocalSubnet=_SlcNetVPNLocalSubnet_Object((1,3,6,1,4,1,244,1,1,1,4,11),_SlcNetVPNLocalSubnet_Type())
slcNetVPNLocalSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNLocalSubnet.setStatus(_A)
class _SlcNetVPNIKENegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('main',1),('aggressive',2)))
_SlcNetVPNIKENegotiation_Type.__name__=_C
_SlcNetVPNIKENegotiation_Object=MibScalar
slcNetVPNIKENegotiation=_SlcNetVPNIKENegotiation_Object((1,3,6,1,4,1,244,1,1,1,4,12),_SlcNetVPNIKENegotiation_Type())
slcNetVPNIKENegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNIKENegotiation.setStatus(_A)
class _SlcNetVPNIKEEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_A9,2),(_l,3)))
_SlcNetVPNIKEEncryption_Type.__name__=_C
_SlcNetVPNIKEEncryption_Object=MibScalar
slcNetVPNIKEEncryption=_SlcNetVPNIKEEncryption_Object((1,3,6,1,4,1,244,1,1,1,4,13),_SlcNetVPNIKEEncryption_Type())
slcNetVPNIKEEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNIKEEncryption.setStatus(_A)
class _SlcNetVPNIKEAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('sha1',2),(_m,3)))
_SlcNetVPNIKEAuthentication_Type.__name__=_C
_SlcNetVPNIKEAuthentication_Object=MibScalar
slcNetVPNIKEAuthentication=_SlcNetVPNIKEAuthentication_Object((1,3,6,1,4,1,244,1,1,1,4,14),_SlcNetVPNIKEAuthentication_Type())
slcNetVPNIKEAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNIKEAuthentication.setStatus(_A)
class _SlcNetVPNIKEDHGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('dhg2',2),('dhg5',3)))
_SlcNetVPNIKEDHGroup_Type.__name__=_C
_SlcNetVPNIKEDHGroup_Object=MibScalar
slcNetVPNIKEDHGroup=_SlcNetVPNIKEDHGroup_Object((1,3,6,1,4,1,244,1,1,1,4,15),_SlcNetVPNIKEDHGroup_Type())
slcNetVPNIKEDHGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNIKEDHGroup.setStatus(_A)
class _SlcNetVPNESPEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_A9,2),(_l,3)))
_SlcNetVPNESPEncryption_Type.__name__=_C
_SlcNetVPNESPEncryption_Object=MibScalar
slcNetVPNESPEncryption=_SlcNetVPNESPEncryption_Object((1,3,6,1,4,1,244,1,1,1,4,16),_SlcNetVPNESPEncryption_Type())
slcNetVPNESPEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNESPEncryption.setStatus(_A)
class _SlcNetVPNESPAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('sha1',2),(_m,3)))
_SlcNetVPNESPAuthentication_Type.__name__=_C
_SlcNetVPNESPAuthentication_Object=MibScalar
slcNetVPNESPAuthentication=_SlcNetVPNESPAuthentication_Object((1,3,6,1,4,1,244,1,1,1,4,17),_SlcNetVPNESPAuthentication_Type())
slcNetVPNESPAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNESPAuthentication.setStatus(_A)
class _SlcNetVPNESPDHGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('dhg2',2),('dhg5',3)))
_SlcNetVPNESPDHGroup_Type.__name__=_C
_SlcNetVPNESPDHGroup_Object=MibScalar
slcNetVPNESPDHGroup=_SlcNetVPNESPDHGroup_Object((1,3,6,1,4,1,244,1,1,1,4,18),_SlcNetVPNESPDHGroup_Type())
slcNetVPNESPDHGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNESPDHGroup.setStatus(_A)
class _SlcNetVPNAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsaPublicKey',1),('preSharedKey',2)))
_SlcNetVPNAuthentication_Type.__name__=_C
_SlcNetVPNAuthentication_Object=MibScalar
slcNetVPNAuthentication=_SlcNetVPNAuthentication_Object((1,3,6,1,4,1,244,1,1,1,4,19),_SlcNetVPNAuthentication_Type())
slcNetVPNAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNAuthentication.setStatus(_A)
_SlcNetVPNPerfectForwardSecrecy_Type=EnabledState
_SlcNetVPNPerfectForwardSecrecy_Object=MibScalar
slcNetVPNPerfectForwardSecrecy=_SlcNetVPNPerfectForwardSecrecy_Object((1,3,6,1,4,1,244,1,1,1,4,20),_SlcNetVPNPerfectForwardSecrecy_Type())
slcNetVPNPerfectForwardSecrecy.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNPerfectForwardSecrecy.setStatus(_A)
_SlcNetVPNModeConfigClient_Type=EnabledState
_SlcNetVPNModeConfigClient_Object=MibScalar
slcNetVPNModeConfigClient=_SlcNetVPNModeConfigClient_Object((1,3,6,1,4,1,244,1,1,1,4,21),_SlcNetVPNModeConfigClient_Type())
slcNetVPNModeConfigClient.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNModeConfigClient.setStatus(_A)
_SlcNetVPNXAUTHClient_Type=EnabledState
_SlcNetVPNXAUTHClient_Object=MibScalar
slcNetVPNXAUTHClient=_SlcNetVPNXAUTHClient_Object((1,3,6,1,4,1,244,1,1,1,4,22),_SlcNetVPNXAUTHClient_Type())
slcNetVPNXAUTHClient.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNXAUTHClient.setStatus(_A)
_SlcNetVPNXAUTHClientLogin_Type=OctetString
_SlcNetVPNXAUTHClientLogin_Object=MibScalar
slcNetVPNXAUTHClientLogin=_SlcNetVPNXAUTHClientLogin_Object((1,3,6,1,4,1,244,1,1,1,4,23),_SlcNetVPNXAUTHClientLogin_Type())
slcNetVPNXAUTHClientLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetVPNXAUTHClientLogin.setStatus(_A)
_SlcNetSecurity_ObjectIdentity=ObjectIdentity
slcNetSecurity=_SlcNetSecurity_ObjectIdentity((1,3,6,1,4,1,244,1,1,1,5))
_SlcNetSecurityFIPSMode_Type=EnabledState
_SlcNetSecurityFIPSMode_Object=MibScalar
slcNetSecurityFIPSMode=_SlcNetSecurityFIPSMode_Object((1,3,6,1,4,1,244,1,1,1,5,1),_SlcNetSecurityFIPSMode_Type())
slcNetSecurityFIPSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcNetSecurityFIPSMode.setStatus(_A)
_SlcServices_ObjectIdentity=ObjectIdentity
slcServices=_SlcServices_ObjectIdentity((1,3,6,1,4,1,244,1,1,2))
_SlcServNTP_ObjectIdentity=ObjectIdentity
slcServNTP=_SlcServNTP_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,1))
_SlcServNTPState_Type=EnabledState
_SlcServNTPState_Object=MibScalar
slcServNTPState=_SlcServNTPState_Object((1,3,6,1,4,1,244,1,1,2,1,1),_SlcServNTPState_Type())
slcServNTPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPState.setStatus(_A)
class _SlcServNTPSynchronize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('broadcast',1),('poll',2)))
_SlcServNTPSynchronize_Type.__name__=_C
_SlcServNTPSynchronize_Object=MibScalar
slcServNTPSynchronize=_SlcServNTPSynchronize_Object((1,3,6,1,4,1,244,1,1,2,1,2),_SlcServNTPSynchronize_Type())
slcServNTPSynchronize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPSynchronize.setStatus(_A)
class _SlcServNTPPoll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('public',2)))
_SlcServNTPPoll_Type.__name__=_C
_SlcServNTPPoll_Object=MibScalar
slcServNTPPoll=_SlcServNTPPoll_Object((1,3,6,1,4,1,244,1,1,2,1,3),_SlcServNTPPoll_Type())
slcServNTPPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPPoll.setStatus(_A)
_SlcServNTPServer_Type=IpAddress
_SlcServNTPServer_Object=MibScalar
slcServNTPServer=_SlcServNTPServer_Object((1,3,6,1,4,1,244,1,1,2,1,4),_SlcServNTPServer_Type())
slcServNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPServer.setStatus(_A)
_SlcServNTPLocalServer2_Type=IpAddress
_SlcServNTPLocalServer2_Object=MibScalar
slcServNTPLocalServer2=_SlcServNTPLocalServer2_Object((1,3,6,1,4,1,244,1,1,2,1,5),_SlcServNTPLocalServer2_Type())
slcServNTPLocalServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPLocalServer2.setStatus(_A)
_SlcServNTPLocalServer3_Type=IpAddress
_SlcServNTPLocalServer3_Object=MibScalar
slcServNTPLocalServer3=_SlcServNTPLocalServer3_Object((1,3,6,1,4,1,244,1,1,2,1,6),_SlcServNTPLocalServer3_Type())
slcServNTPLocalServer3.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPLocalServer3.setStatus(_A)
_SlcServNTPServerIPv6_Type=Ipv6Address
_SlcServNTPServerIPv6_Object=MibScalar
slcServNTPServerIPv6=_SlcServNTPServerIPv6_Object((1,3,6,1,4,1,244,1,1,2,1,7),_SlcServNTPServerIPv6_Type())
slcServNTPServerIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPServerIPv6.setStatus(_A)
_SlcServNTPLocalServer2IPv6_Type=Ipv6Address
_SlcServNTPLocalServer2IPv6_Object=MibScalar
slcServNTPLocalServer2IPv6=_SlcServNTPLocalServer2IPv6_Object((1,3,6,1,4,1,244,1,1,2,1,8),_SlcServNTPLocalServer2IPv6_Type())
slcServNTPLocalServer2IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPLocalServer2IPv6.setStatus(_A)
_SlcServNTPLocalServer3IPv6_Type=Ipv6Address
_SlcServNTPLocalServer3IPv6_Object=MibScalar
slcServNTPLocalServer3IPv6=_SlcServNTPLocalServer3IPv6_Object((1,3,6,1,4,1,244,1,1,2,1,9),_SlcServNTPLocalServer3IPv6_Type())
slcServNTPLocalServer3IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNTPLocalServer3IPv6.setStatus(_A)
_SlcServSyslog_ObjectIdentity=ObjectIdentity
slcServSyslog=_SlcServSyslog_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,2))
_SlcServSysNetworkLevel_Type=SyslogLevel
_SlcServSysNetworkLevel_Object=MibScalar
slcServSysNetworkLevel=_SlcServSysNetworkLevel_Object((1,3,6,1,4,1,244,1,1,2,2,1),_SlcServSysNetworkLevel_Type())
slcServSysNetworkLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysNetworkLevel.setStatus(_A)
_SlcServSysServicesLevel_Type=SyslogLevel
_SlcServSysServicesLevel_Object=MibScalar
slcServSysServicesLevel=_SlcServSysServicesLevel_Object((1,3,6,1,4,1,244,1,1,2,2,2),_SlcServSysServicesLevel_Type())
slcServSysServicesLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysServicesLevel.setStatus(_A)
_SlcServSysAuthLevel_Type=SyslogLevel
_SlcServSysAuthLevel_Object=MibScalar
slcServSysAuthLevel=_SlcServSysAuthLevel_Object((1,3,6,1,4,1,244,1,1,2,2,3),_SlcServSysAuthLevel_Type())
slcServSysAuthLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysAuthLevel.setStatus(_A)
_SlcServSysDevPortLevel_Type=SyslogLevel
_SlcServSysDevPortLevel_Object=MibScalar
slcServSysDevPortLevel=_SlcServSysDevPortLevel_Object((1,3,6,1,4,1,244,1,1,2,2,4),_SlcServSysDevPortLevel_Type())
slcServSysDevPortLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysDevPortLevel.setStatus(_A)
_SlcServSysDiagLevel_Type=SyslogLevel
_SlcServSysDiagLevel_Object=MibScalar
slcServSysDiagLevel=_SlcServSysDiagLevel_Object((1,3,6,1,4,1,244,1,1,2,2,5),_SlcServSysDiagLevel_Type())
slcServSysDiagLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysDiagLevel.setStatus(_A)
_SlcServSysGeneralLevel_Type=SyslogLevel
_SlcServSysGeneralLevel_Object=MibScalar
slcServSysGeneralLevel=_SlcServSysGeneralLevel_Object((1,3,6,1,4,1,244,1,1,2,2,6),_SlcServSysGeneralLevel_Type())
slcServSysGeneralLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysGeneralLevel.setStatus(_A)
_SlcServSysRemoteServer_Type=IpAddress
_SlcServSysRemoteServer_Object=MibScalar
slcServSysRemoteServer=_SlcServSysRemoteServer_Object((1,3,6,1,4,1,244,1,1,2,2,7),_SlcServSysRemoteServer_Type())
slcServSysRemoteServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysRemoteServer.setStatus(_A)
_SlcServSysRemoteServer2_Type=IpAddress
_SlcServSysRemoteServer2_Object=MibScalar
slcServSysRemoteServer2=_SlcServSysRemoteServer2_Object((1,3,6,1,4,1,244,1,1,2,2,8),_SlcServSysRemoteServer2_Type())
slcServSysRemoteServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysRemoteServer2.setStatus(_A)
_SlcServSysRemoteServerIPv6_Type=Ipv6Address
_SlcServSysRemoteServerIPv6_Object=MibScalar
slcServSysRemoteServerIPv6=_SlcServSysRemoteServerIPv6_Object((1,3,6,1,4,1,244,1,1,2,2,9),_SlcServSysRemoteServerIPv6_Type())
slcServSysRemoteServerIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysRemoteServerIPv6.setStatus(_A)
_SlcServSysRemoteServer2IPv6_Type=Ipv6Address
_SlcServSysRemoteServer2IPv6_Object=MibScalar
slcServSysRemoteServer2IPv6=_SlcServSysRemoteServer2IPv6_Object((1,3,6,1,4,1,244,1,1,2,2,10),_SlcServSysRemoteServer2IPv6_Type())
slcServSysRemoteServer2IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysRemoteServer2IPv6.setStatus(_A)
class _SlcServSysRPMLogSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,40))
_SlcServSysRPMLogSize_Type.__name__=_C
_SlcServSysRPMLogSize_Object=MibScalar
slcServSysRPMLogSize=_SlcServSysRPMLogSize_Object((1,3,6,1,4,1,244,1,1,2,2,11),_SlcServSysRPMLogSize_Type())
slcServSysRPMLogSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysRPMLogSize.setStatus(_A)
if mibBuilder.loadTexts:slcServSysRPMLogSize.setUnits(_n)
class _SlcServSysOtherLogSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,40))
_SlcServSysOtherLogSize_Type.__name__=_C
_SlcServSysOtherLogSize_Object=MibScalar
slcServSysOtherLogSize=_SlcServSysOtherLogSize_Object((1,3,6,1,4,1,244,1,1,2,2,12),_SlcServSysOtherLogSize_Type())
slcServSysOtherLogSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSysOtherLogSize.setStatus(_A)
if mibBuilder.loadTexts:slcServSysOtherLogSize.setUnits(_n)
_SlcServAuditLog_ObjectIdentity=ObjectIdentity
slcServAuditLog=_SlcServAuditLog_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,3))
_SlcServAuditState_Type=EnabledState
_SlcServAuditState_Object=MibScalar
slcServAuditState=_SlcServAuditState_Object((1,3,6,1,4,1,244,1,1,2,3,1),_SlcServAuditState_Type())
slcServAuditState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServAuditState.setStatus(_A)
class _SlcServAuditSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,500))
_SlcServAuditSize_Type.__name__=_C
_SlcServAuditSize_Object=MibScalar
slcServAuditSize=_SlcServAuditSize_Object((1,3,6,1,4,1,244,1,1,2,3,2),_SlcServAuditSize_Type())
slcServAuditSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServAuditSize.setStatus(_A)
if mibBuilder.loadTexts:slcServAuditSize.setUnits(_n)
_SlcServAuditIncludeCLI_Type=EnabledState
_SlcServAuditIncludeCLI_Object=MibScalar
slcServAuditIncludeCLI=_SlcServAuditIncludeCLI_Object((1,3,6,1,4,1,244,1,1,2,3,3),_SlcServAuditIncludeCLI_Type())
slcServAuditIncludeCLI.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServAuditIncludeCLI.setStatus(_A)
_SlcServAuditInSystemLog_Type=EnabledState
_SlcServAuditInSystemLog_Object=MibScalar
slcServAuditInSystemLog=_SlcServAuditInSystemLog_Object((1,3,6,1,4,1,244,1,1,2,3,4),_SlcServAuditInSystemLog_Type())
slcServAuditInSystemLog.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServAuditInSystemLog.setStatus(_A)
_SlcServSSH_ObjectIdentity=ObjectIdentity
slcServSSH=_SlcServSSH_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,4))
_SlcServSSHState_Type=EnabledState
_SlcServSSHState_Object=MibScalar
slcServSSHState=_SlcServSSHState_Object((1,3,6,1,4,1,244,1,1,2,4,1),_SlcServSSHState_Type())
slcServSSHState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHState.setStatus(_A)
class _SlcServSSHTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcServSSHTimeout_Type.__name__=_C
_SlcServSSHTimeout_Object=MibScalar
slcServSSHTimeout=_SlcServSSHTimeout_Object((1,3,6,1,4,1,244,1,1,2,4,2),_SlcServSSHTimeout_Type())
slcServSSHTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcServSSHTimeout.setUnits(_H)
_SlcServSSHWebSSH_Type=EnabledState
_SlcServSSHWebSSH_Object=MibScalar
slcServSSHWebSSH=_SlcServSSHWebSSH_Object((1,3,6,1,4,1,244,1,1,2,4,3),_SlcServSSHWebSSH_Type())
slcServSSHWebSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHWebSSH.setStatus(_A)
class _SlcServSSHPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcServSSHPort_Type.__name__=_C
_SlcServSSHPort_Object=MibScalar
slcServSSHPort=_SlcServSSHPort_Object((1,3,6,1,4,1,244,1,1,2,4,4),_SlcServSSHPort_Type())
slcServSSHPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHPort.setStatus(_A)
_SlcServSSHV1Incoming_Type=EnabledState
_SlcServSSHV1Incoming_Object=MibScalar
slcServSSHV1Incoming=_SlcServSSHV1Incoming_Object((1,3,6,1,4,1,244,1,1,2,4,5),_SlcServSSHV1Incoming_Type())
slcServSSHV1Incoming.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHV1Incoming.setStatus(_A)
_SlcServSSHTimeoutDataDirection_Type=TimeoutDataDirection
_SlcServSSHTimeoutDataDirection_Object=MibScalar
slcServSSHTimeoutDataDirection=_SlcServSSHTimeoutDataDirection_Object((1,3,6,1,4,1,244,1,1,2,4,6),_SlcServSSHTimeoutDataDirection_Type())
slcServSSHTimeoutDataDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHTimeoutDataDirection.setStatus(_A)
_SlcServSSHDSAKeys_Type=EnabledState
_SlcServSSHDSAKeys_Object=MibScalar
slcServSSHDSAKeys=_SlcServSSHDSAKeys_Object((1,3,6,1,4,1,244,1,1,2,4,7),_SlcServSSHDSAKeys_Type())
slcServSSHDSAKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSSHDSAKeys.setStatus(_A)
_SlcServTelnet_ObjectIdentity=ObjectIdentity
slcServTelnet=_SlcServTelnet_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,5))
_SlcServTelnetState_Type=EnabledState
_SlcServTelnetState_Object=MibScalar
slcServTelnetState=_SlcServTelnetState_Object((1,3,6,1,4,1,244,1,1,2,5,1),_SlcServTelnetState_Type())
slcServTelnetState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServTelnetState.setStatus(_A)
class _SlcServTelnetTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcServTelnetTimeout_Type.__name__=_C
_SlcServTelnetTimeout_Object=MibScalar
slcServTelnetTimeout=_SlcServTelnetTimeout_Object((1,3,6,1,4,1,244,1,1,2,5,2),_SlcServTelnetTimeout_Type())
slcServTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServTelnetTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcServTelnetTimeout.setUnits(_H)
_SlcServTelnetWebTelnet_Type=EnabledState
_SlcServTelnetWebTelnet_Object=MibScalar
slcServTelnetWebTelnet=_SlcServTelnetWebTelnet_Object((1,3,6,1,4,1,244,1,1,2,5,3),_SlcServTelnetWebTelnet_Type())
slcServTelnetWebTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServTelnetWebTelnet.setStatus(_A)
_SlcServTelnetTelnetOut_Type=EnabledState
_SlcServTelnetTelnetOut_Object=MibScalar
slcServTelnetTelnetOut=_SlcServTelnetTelnetOut_Object((1,3,6,1,4,1,244,1,1,2,5,4),_SlcServTelnetTelnetOut_Type())
slcServTelnetTelnetOut.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServTelnetTelnetOut.setStatus(_A)
_SlcServTelnetTimeoutDataDirection_Type=TimeoutDataDirection
_SlcServTelnetTimeoutDataDirection_Object=MibScalar
slcServTelnetTimeoutDataDirection=_SlcServTelnetTimeoutDataDirection_Object((1,3,6,1,4,1,244,1,1,2,5,5),_SlcServTelnetTimeoutDataDirection_Type())
slcServTelnetTimeoutDataDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServTelnetTimeoutDataDirection.setStatus(_A)
_SlcServSNMP_ObjectIdentity=ObjectIdentity
slcServSNMP=_SlcServSNMP_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,6))
_SlcServSNMPState_Type=EnabledState
_SlcServSNMPState_Object=MibScalar
slcServSNMPState=_SlcServSNMPState_Object((1,3,6,1,4,1,244,1,1,2,6,1),_SlcServSNMPState_Type())
slcServSNMPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPState.setStatus(_A)
_SlcServSNMPTraps_Type=EnabledState
_SlcServSNMPTraps_Object=MibScalar
slcServSNMPTraps=_SlcServSNMPTraps_Object((1,3,6,1,4,1,244,1,1,2,6,2),_SlcServSNMPTraps_Type())
slcServSNMPTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPTraps.setStatus(_A)
_SlcServSNMPNMS_Type=IpAddress
_SlcServSNMPNMS_Object=MibScalar
slcServSNMPNMS=_SlcServSNMPNMS_Object((1,3,6,1,4,1,244,1,1,2,6,3),_SlcServSNMPNMS_Type())
slcServSNMPNMS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPNMS.setStatus(_A)
_SlcServSNMPLocation_Type=OctetString
_SlcServSNMPLocation_Object=MibScalar
slcServSNMPLocation=_SlcServSNMPLocation_Object((1,3,6,1,4,1,244,1,1,2,6,4),_SlcServSNMPLocation_Type())
slcServSNMPLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPLocation.setStatus(_A)
_SlcServSNMPContact_Type=OctetString
_SlcServSNMPContact_Object=MibScalar
slcServSNMPContact=_SlcServSNMPContact_Object((1,3,6,1,4,1,244,1,1,2,6,5),_SlcServSNMPContact_Type())
slcServSNMPContact.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPContact.setStatus(_A)
class _SlcServSNMPv3User_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcServSNMPv3User_Type.__name__=_F
_SlcServSNMPv3User_Object=MibScalar
slcServSNMPv3User=_SlcServSNMPv3User_Object((1,3,6,1,4,1,244,1,1,2,6,6),_SlcServSNMPv3User_Type())
slcServSNMPv3User.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPv3User.setStatus(_A)
_SlcServSNMPReadOnlyCommunity_Type=OctetString
_SlcServSNMPReadOnlyCommunity_Object=MibScalar
slcServSNMPReadOnlyCommunity=_SlcServSNMPReadOnlyCommunity_Object((1,3,6,1,4,1,244,1,1,2,6,7),_SlcServSNMPReadOnlyCommunity_Type())
slcServSNMPReadOnlyCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPReadOnlyCommunity.setStatus(_A)
_SlcServSNMPReadWriteCommunity_Type=OctetString
_SlcServSNMPReadWriteCommunity_Object=MibScalar
slcServSNMPReadWriteCommunity=_SlcServSNMPReadWriteCommunity_Object((1,3,6,1,4,1,244,1,1,2,6,8),_SlcServSNMPReadWriteCommunity_Type())
slcServSNMPReadWriteCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPReadWriteCommunity.setStatus(_A)
_SlcServSNMPTrapCommunity_Type=OctetString
_SlcServSNMPTrapCommunity_Object=MibScalar
slcServSNMPTrapCommunity=_SlcServSNMPTrapCommunity_Object((1,3,6,1,4,1,244,1,1,2,6,9),_SlcServSNMPTrapCommunity_Type())
slcServSNMPTrapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPTrapCommunity.setStatus(_A)
_SlcServSNMPAlarmDelay_Type=Integer32
_SlcServSNMPAlarmDelay_Object=MibScalar
slcServSNMPAlarmDelay=_SlcServSNMPAlarmDelay_Object((1,3,6,1,4,1,244,1,1,2,6,10),_SlcServSNMPAlarmDelay_Type())
slcServSNMPAlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPAlarmDelay.setStatus(_A)
class _SlcServSNMPv3ReadWriteUser_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcServSNMPv3ReadWriteUser_Type.__name__=_F
_SlcServSNMPv3ReadWriteUser_Object=MibScalar
slcServSNMPv3ReadWriteUser=_SlcServSNMPv3ReadWriteUser_Object((1,3,6,1,4,1,244,1,1,2,6,11),_SlcServSNMPv3ReadWriteUser_Type())
slcServSNMPv3ReadWriteUser.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPv3ReadWriteUser.setStatus(_A)
class _SlcServSNMPv3Security_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuthNoEncrypt',1),('authNoEncrypt',2),('authEncrypt',3)))
_SlcServSNMPv3Security_Type.__name__=_C
_SlcServSNMPv3Security_Object=MibScalar
slcServSNMPv3Security=_SlcServSNMPv3Security_Object((1,3,6,1,4,1,244,1,1,2,6,12),_SlcServSNMPv3Security_Type())
slcServSNMPv3Security.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPv3Security.setStatus(_A)
class _SlcServSNMPv3Authentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),('sha',2)))
_SlcServSNMPv3Authentication_Type.__name__=_C
_SlcServSNMPv3Authentication_Object=MibScalar
slcServSNMPv3Authentication=_SlcServSNMPv3Authentication_Object((1,3,6,1,4,1,244,1,1,2,6,13),_SlcServSNMPv3Authentication_Type())
slcServSNMPv3Authentication.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPv3Authentication.setStatus(_A)
class _SlcServSNMPv3Encryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('des',1),(_l,2)))
_SlcServSNMPv3Encryption_Type.__name__=_C
_SlcServSNMPv3Encryption_Object=MibScalar
slcServSNMPv3Encryption=_SlcServSNMPv3Encryption_Object((1,3,6,1,4,1,244,1,1,2,6,14),_SlcServSNMPv3Encryption_Type())
slcServSNMPv3Encryption.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPv3Encryption.setStatus(_A)
_SlcServSNMPv1v2_Type=EnabledState
_SlcServSNMPv1v2_Object=MibScalar
slcServSNMPv1v2=_SlcServSNMPv1v2_Object((1,3,6,1,4,1,244,1,1,2,6,15),_SlcServSNMPv1v2_Type())
slcServSNMPv1v2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPv1v2.setStatus(_A)
_SlcServSNMPNMS2_Type=IpAddress
_SlcServSNMPNMS2_Object=MibScalar
slcServSNMPNMS2=_SlcServSNMPNMS2_Object((1,3,6,1,4,1,244,1,1,2,6,16),_SlcServSNMPNMS2_Type())
slcServSNMPNMS2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPNMS2.setStatus(_A)
_SlcServSNMPNMSIPv6_Type=Ipv6Address
_SlcServSNMPNMSIPv6_Object=MibScalar
slcServSNMPNMSIPv6=_SlcServSNMPNMSIPv6_Object((1,3,6,1,4,1,244,1,1,2,6,17),_SlcServSNMPNMSIPv6_Type())
slcServSNMPNMSIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPNMSIPv6.setStatus(_A)
_SlcServSNMPNMS2IPv6_Type=Ipv6Address
_SlcServSNMPNMS2IPv6_Object=MibScalar
slcServSNMPNMS2IPv6=_SlcServSNMPNMS2IPv6_Object((1,3,6,1,4,1,244,1,1,2,6,18),_SlcServSNMPNMS2IPv6_Type())
slcServSNMPNMS2IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSNMPNMS2IPv6.setStatus(_A)
_SlcServSMTP_ObjectIdentity=ObjectIdentity
slcServSMTP=_SlcServSMTP_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,7))
_SlcServSMTPServer_Type=IpAddress
_SlcServSMTPServer_Object=MibScalar
slcServSMTPServer=_SlcServSMTPServer_Object((1,3,6,1,4,1,244,1,1,2,7,1),_SlcServSMTPServer_Type())
slcServSMTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSMTPServer.setStatus(_A)
_SlcServSMTPSender_Type=OctetString
_SlcServSMTPSender_Object=MibScalar
slcServSMTPSender=_SlcServSMTPSender_Object((1,3,6,1,4,1,244,1,1,2,7,2),_SlcServSMTPSender_Type())
slcServSMTPSender.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSMTPSender.setStatus(_A)
_SlcServNFS_ObjectIdentity=ObjectIdentity
slcServNFS=_SlcServNFS_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,8))
_SlcServNFSMountTable_Object=MibTable
slcServNFSMountTable=_SlcServNFSMountTable_Object((1,3,6,1,4,1,244,1,1,2,8,1))
if mibBuilder.loadTexts:slcServNFSMountTable.setStatus(_A)
_SlcServNFSMountEntry_Object=MibTableRow
slcServNFSMountEntry=_SlcServNFSMountEntry_Object((1,3,6,1,4,1,244,1,1,2,8,1,1))
slcServNFSMountEntry.setIndexNames((0,_D,_AA))
if mibBuilder.loadTexts:slcServNFSMountEntry.setStatus(_A)
class _SlcServNFSMountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SlcServNFSMountIndex_Type.__name__=_C
_SlcServNFSMountIndex_Object=MibTableColumn
slcServNFSMountIndex=_SlcServNFSMountIndex_Object((1,3,6,1,4,1,244,1,1,2,8,1,1,1),_SlcServNFSMountIndex_Type())
slcServNFSMountIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNFSMountIndex.setStatus(_A)
_SlcServNFSMountRemoteDir_Type=OctetString
_SlcServNFSMountRemoteDir_Object=MibTableColumn
slcServNFSMountRemoteDir=_SlcServNFSMountRemoteDir_Object((1,3,6,1,4,1,244,1,1,2,8,1,1,2),_SlcServNFSMountRemoteDir_Type())
slcServNFSMountRemoteDir.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNFSMountRemoteDir.setStatus(_A)
_SlcServNFSMountLocalDir_Type=OctetString
_SlcServNFSMountLocalDir_Object=MibTableColumn
slcServNFSMountLocalDir=_SlcServNFSMountLocalDir_Object((1,3,6,1,4,1,244,1,1,2,8,1,1,3),_SlcServNFSMountLocalDir_Type())
slcServNFSMountLocalDir.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNFSMountLocalDir.setStatus(_A)
_SlcServNFSMountReadWrite_Type=EnabledState
_SlcServNFSMountReadWrite_Object=MibTableColumn
slcServNFSMountReadWrite=_SlcServNFSMountReadWrite_Object((1,3,6,1,4,1,244,1,1,2,8,1,1,4),_SlcServNFSMountReadWrite_Type())
slcServNFSMountReadWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNFSMountReadWrite.setStatus(_A)
_SlcServNFSMountMount_Type=EnabledState
_SlcServNFSMountMount_Object=MibTableColumn
slcServNFSMountMount=_SlcServNFSMountMount_Object((1,3,6,1,4,1,244,1,1,2,8,1,1,5),_SlcServNFSMountMount_Type())
slcServNFSMountMount.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServNFSMountMount.setStatus(_A)
_SlcServCIFS_ObjectIdentity=ObjectIdentity
slcServCIFS=_SlcServCIFS_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,9))
_SlcServCIFSState_Type=EnabledState
_SlcServCIFSState_Object=MibScalar
slcServCIFSState=_SlcServCIFSState_Object((1,3,6,1,4,1,244,1,1,2,9,1),_SlcServCIFSState_Type())
slcServCIFSState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServCIFSState.setStatus(_A)
_SlcServCIFSEth1_Type=EnabledState
_SlcServCIFSEth1_Object=MibScalar
slcServCIFSEth1=_SlcServCIFSEth1_Object((1,3,6,1,4,1,244,1,1,2,9,2),_SlcServCIFSEth1_Type())
slcServCIFSEth1.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServCIFSEth1.setStatus(_A)
_SlcServCIFSEth2_Type=EnabledState
_SlcServCIFSEth2_Object=MibScalar
slcServCIFSEth2=_SlcServCIFSEth2_Object((1,3,6,1,4,1,244,1,1,2,9,3),_SlcServCIFSEth2_Type())
slcServCIFSEth2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServCIFSEth2.setStatus(_A)
class _SlcServCIFSWorkgroup_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SlcServCIFSWorkgroup_Type.__name__=_F
_SlcServCIFSWorkgroup_Object=MibScalar
slcServCIFSWorkgroup=_SlcServCIFSWorkgroup_Object((1,3,6,1,4,1,244,1,1,2,9,4),_SlcServCIFSWorkgroup_Type())
slcServCIFSWorkgroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServCIFSWorkgroup.setStatus(_A)
_SlcServSLCNetwork_ObjectIdentity=ObjectIdentity
slcServSLCNetwork=_SlcServSLCNetwork_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,10))
class _SlcServSLCNetSearch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('both',1),('subnet',2),('manual',3)))
_SlcServSLCNetSearch_Type.__name__=_C
_SlcServSLCNetSearch_Object=MibScalar
slcServSLCNetSearch=_SlcServSLCNetSearch_Object((1,3,6,1,4,1,244,1,1,2,10,1),_SlcServSLCNetSearch_Type())
slcServSLCNetSearch.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSLCNetSearch.setStatus(_A)
class _SlcServSLCNetNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_SlcServSLCNetNumber_Type.__name__=_C
_SlcServSLCNetNumber_Object=MibScalar
slcServSLCNetNumber=_SlcServSLCNetNumber_Object((1,3,6,1,4,1,244,1,1,2,10,2),_SlcServSLCNetNumber_Type())
slcServSLCNetNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSLCNetNumber.setStatus(_A)
_SlcServSLCNetTable_Object=MibTable
slcServSLCNetTable=_SlcServSLCNetTable_Object((1,3,6,1,4,1,244,1,1,2,10,3))
if mibBuilder.loadTexts:slcServSLCNetTable.setStatus(_A)
_SlcServSLCNetEntry_Object=MibTableRow
slcServSLCNetEntry=_SlcServSLCNetEntry_Object((1,3,6,1,4,1,244,1,1,2,10,3,1))
slcServSLCNetEntry.setIndexNames((0,_D,_AB))
if mibBuilder.loadTexts:slcServSLCNetEntry.setStatus(_A)
class _SlcServSLCNetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_SlcServSLCNetIndex_Type.__name__=_C
_SlcServSLCNetIndex_Object=MibTableColumn
slcServSLCNetIndex=_SlcServSLCNetIndex_Object((1,3,6,1,4,1,244,1,1,2,10,3,1,1),_SlcServSLCNetIndex_Type())
slcServSLCNetIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSLCNetIndex.setStatus(_A)
_SlcServSLCNetIP_Type=IpAddress
_SlcServSLCNetIP_Object=MibTableColumn
slcServSLCNetIP=_SlcServSLCNetIP_Object((1,3,6,1,4,1,244,1,1,2,10,3,1,2),_SlcServSLCNetIP_Type())
slcServSLCNetIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSLCNetIP.setStatus(_A)
_SlcServPhoneHome_ObjectIdentity=ObjectIdentity
slcServPhoneHome=_SlcServPhoneHome_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,11))
_SlcServPhoneHomeState_Type=EnabledState
_SlcServPhoneHomeState_Object=MibScalar
slcServPhoneHomeState=_SlcServPhoneHomeState_Object((1,3,6,1,4,1,244,1,1,2,11,1),_SlcServPhoneHomeState_Type())
slcServPhoneHomeState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServPhoneHomeState.setStatus(_A)
_SlcServPhoneHomeIP_Type=IpAddress
_SlcServPhoneHomeIP_Object=MibScalar
slcServPhoneHomeIP=_SlcServPhoneHomeIP_Object((1,3,6,1,4,1,244,1,1,2,11,2),_SlcServPhoneHomeIP_Type())
slcServPhoneHomeIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServPhoneHomeIP.setStatus(_A)
_SlcServHostList_ObjectIdentity=ObjectIdentity
slcServHostList=_SlcServHostList_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,12))
class _SlcServHostListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_SlcServHostListNumber_Type.__name__=_C
_SlcServHostListNumber_Object=MibScalar
slcServHostListNumber=_SlcServHostListNumber_Object((1,3,6,1,4,1,244,1,1,2,12,1),_SlcServHostListNumber_Type())
slcServHostListNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListNumber.setStatus(_A)
_SlcServHostListTable_Object=MibTable
slcServHostListTable=_SlcServHostListTable_Object((1,3,6,1,4,1,244,1,1,2,12,2))
if mibBuilder.loadTexts:slcServHostListTable.setStatus(_A)
_SlcServHostListEntry_Object=MibTableRow
slcServHostListEntry=_SlcServHostListEntry_Object((1,3,6,1,4,1,244,1,1,2,12,2,1))
slcServHostListEntry.setIndexNames((0,_D,_AC))
if mibBuilder.loadTexts:slcServHostListEntry.setStatus(_A)
class _SlcServHostListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SlcServHostListIndex_Type.__name__=_C
_SlcServHostListIndex_Object=MibTableColumn
slcServHostListIndex=_SlcServHostListIndex_Object((1,3,6,1,4,1,244,1,1,2,12,2,1,1),_SlcServHostListIndex_Type())
slcServHostListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListIndex.setStatus(_A)
_SlcServHostListName_Type=OctetString
_SlcServHostListName_Object=MibTableColumn
slcServHostListName=_SlcServHostListName_Object((1,3,6,1,4,1,244,1,1,2,12,2,1,2),_SlcServHostListName_Type())
slcServHostListName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListName.setStatus(_A)
_SlcServHostListRetryCount_Type=Integer32
_SlcServHostListRetryCount_Object=MibTableColumn
slcServHostListRetryCount=_SlcServHostListRetryCount_Object((1,3,6,1,4,1,244,1,1,2,12,2,1,3),_SlcServHostListRetryCount_Type())
slcServHostListRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListRetryCount.setStatus(_A)
_SlcServHostListAuth_Type=EnabledState
_SlcServHostListAuth_Object=MibTableColumn
slcServHostListAuth=_SlcServHostListAuth_Object((1,3,6,1,4,1,244,1,1,2,12,2,1,4),_SlcServHostListAuth_Type())
slcServHostListAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListAuth.setStatus(_A)
class _SlcServHostListNumHosts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SlcServHostListNumHosts_Type.__name__=_C
_SlcServHostListNumHosts_Object=MibTableColumn
slcServHostListNumHosts=_SlcServHostListNumHosts_Object((1,3,6,1,4,1,244,1,1,2,12,2,1,5),_SlcServHostListNumHosts_Type())
slcServHostListNumHosts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListNumHosts.setStatus(_A)
_SlcServHostListHosts_Type=OctetString
_SlcServHostListHosts_Object=MibTableColumn
slcServHostListHosts=_SlcServHostListHosts_Object((1,3,6,1,4,1,244,1,1,2,12,2,1,6),_SlcServHostListHosts_Type())
slcServHostListHosts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServHostListHosts.setStatus(_A)
_SlcServWebTerm_ObjectIdentity=ObjectIdentity
slcServWebTerm=_SlcServWebTerm_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,13))
class _SlcServWebTermDeployment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('javaWebStart',1),('applet',2)))
_SlcServWebTermDeployment_Type.__name__=_C
_SlcServWebTermDeployment_Object=MibScalar
slcServWebTermDeployment=_SlcServWebTermDeployment_Object((1,3,6,1,4,1,244,1,1,2,13,1),_SlcServWebTermDeployment_Type())
slcServWebTermDeployment.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServWebTermDeployment.setStatus(_A)
class _SlcServWebTermBufSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(24,5000))
_SlcServWebTermBufSize_Type.__name__=_C
_SlcServWebTermBufSize_Object=MibScalar
slcServWebTermBufSize=_SlcServWebTermBufSize_Object((1,3,6,1,4,1,244,1,1,2,13,2),_SlcServWebTermBufSize_Type())
slcServWebTermBufSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServWebTermBufSize.setStatus(_A)
_SlcServSite_ObjectIdentity=ObjectIdentity
slcServSite=_SlcServSite_ObjectIdentity((1,3,6,1,4,1,244,1,1,2,14))
class _SlcServSiteNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_SlcServSiteNumber_Type.__name__=_C
_SlcServSiteNumber_Object=MibScalar
slcServSiteNumber=_SlcServSiteNumber_Object((1,3,6,1,4,1,244,1,1,2,14,1),_SlcServSiteNumber_Type())
slcServSiteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteNumber.setStatus(_A)
_SlcServSiteTable_Object=MibTable
slcServSiteTable=_SlcServSiteTable_Object((1,3,6,1,4,1,244,1,1,2,14,2))
if mibBuilder.loadTexts:slcServSiteTable.setStatus(_A)
_SlcServSiteEntry_Object=MibTableRow
slcServSiteEntry=_SlcServSiteEntry_Object((1,3,6,1,4,1,244,1,1,2,14,2,1))
slcServSiteEntry.setIndexNames((0,_D,_AD))
if mibBuilder.loadTexts:slcServSiteEntry.setStatus(_A)
class _SlcServSiteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SlcServSiteIndex_Type.__name__=_C
_SlcServSiteIndex_Object=MibTableColumn
slcServSiteIndex=_SlcServSiteIndex_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,1),_SlcServSiteIndex_Type())
slcServSiteIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteIndex.setStatus(_A)
_SlcServSiteName_Type=OctetString
_SlcServSiteName_Object=MibTableColumn
slcServSiteName=_SlcServSiteName_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,2),_SlcServSiteName_Type())
slcServSiteName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteName.setStatus(_A)
class _SlcServSitePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_A6,2),(_A4,3),(_A5,4),('usbPort',5),(_A7,6)))
_SlcServSitePort_Type.__name__=_C
_SlcServSitePort_Object=MibTableColumn
slcServSitePort=_SlcServSitePort_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,3),_SlcServSitePort_Type())
slcServSitePort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSitePort.setStatus(_A)
class _SlcServSitePortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,48))
_SlcServSitePortId_Type.__name__=_C
_SlcServSitePortId_Object=MibTableColumn
slcServSitePortId=_SlcServSitePortId_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,4),_SlcServSitePortId_Type())
slcServSitePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSitePortId.setStatus(_A)
_SlcServSiteLoginHost_Type=OctetString
_SlcServSiteLoginHost_Object=MibTableColumn
slcServSiteLoginHost=_SlcServSiteLoginHost_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,5),_SlcServSiteLoginHost_Type())
slcServSiteLoginHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteLoginHost.setStatus(_A)
_SlcServSiteCHAPSecret_Type=OctetString
_SlcServSiteCHAPSecret_Object=MibTableColumn
slcServSiteCHAPSecret=_SlcServSiteCHAPSecret_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,6),_SlcServSiteCHAPSecret_Type())
slcServSiteCHAPSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteCHAPSecret.setStatus(_A)
class _SlcServSiteTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcServSiteTimeout_Type.__name__=_C
_SlcServSiteTimeout_Object=MibTableColumn
slcServSiteTimeout=_SlcServSiteTimeout_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,7),_SlcServSiteTimeout_Type())
slcServSiteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcServSiteTimeout.setUnits(_H)
_SlcServSiteLocalIP_Type=IpAddress
_SlcServSiteLocalIP_Object=MibTableColumn
slcServSiteLocalIP=_SlcServSiteLocalIP_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,8),_SlcServSiteLocalIP_Type())
slcServSiteLocalIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteLocalIP.setStatus(_A)
_SlcServSiteRemoteIP_Type=IpAddress
_SlcServSiteRemoteIP_Object=MibTableColumn
slcServSiteRemoteIP=_SlcServSiteRemoteIP_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,9),_SlcServSiteRemoteIP_Type())
slcServSiteRemoteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteRemoteIP.setStatus(_A)
_SlcServSiteStaticRouteIP_Type=IpAddress
_SlcServSiteStaticRouteIP_Object=MibTableColumn
slcServSiteStaticRouteIP=_SlcServSiteStaticRouteIP_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,10),_SlcServSiteStaticRouteIP_Type())
slcServSiteStaticRouteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteStaticRouteIP.setStatus(_A)
_SlcServSiteStaticRouteMask_Type=IpAddress
_SlcServSiteStaticRouteMask_Object=MibTableColumn
slcServSiteStaticRouteMask=_SlcServSiteStaticRouteMask_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,11),_SlcServSiteStaticRouteMask_Type())
slcServSiteStaticRouteMask.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteStaticRouteMask.setStatus(_A)
_SlcServSiteStaticRouteGateway_Type=IpAddress
_SlcServSiteStaticRouteGateway_Object=MibTableColumn
slcServSiteStaticRouteGateway=_SlcServSiteStaticRouteGateway_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,12),_SlcServSiteStaticRouteGateway_Type())
slcServSiteStaticRouteGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteStaticRouteGateway.setStatus(_A)
_SlcServSiteDialoutNum_Type=OctetString
_SlcServSiteDialoutNum_Object=MibTableColumn
slcServSiteDialoutNum=_SlcServSiteDialoutNum_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,13),_SlcServSiteDialoutNum_Type())
slcServSiteDialoutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteDialoutNum.setStatus(_A)
class _SlcServSiteDialoutLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcServSiteDialoutLogin_Type.__name__=_F
_SlcServSiteDialoutLogin_Object=MibTableColumn
slcServSiteDialoutLogin=_SlcServSiteDialoutLogin_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,14),_SlcServSiteDialoutLogin_Type())
slcServSiteDialoutLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteDialoutLogin.setStatus(_A)
_SlcServSiteDialback_Type=EnabledState
_SlcServSiteDialback_Object=MibTableColumn
slcServSiteDialback=_SlcServSiteDialback_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,15),_SlcServSiteDialback_Type())
slcServSiteDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteDialback.setStatus(_A)
_SlcServSiteDialbackNum_Type=OctetString
_SlcServSiteDialbackNum_Object=MibTableColumn
slcServSiteDialbackNum=_SlcServSiteDialbackNum_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,16),_SlcServSiteDialbackNum_Type())
slcServSiteDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteDialbackNum.setStatus(_A)
_SlcServSiteDialbackDelay_Type=Integer32
_SlcServSiteDialbackDelay_Object=MibTableColumn
slcServSiteDialbackDelay=_SlcServSiteDialbackDelay_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,17),_SlcServSiteDialbackDelay_Type())
slcServSiteDialbackDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteDialbackDelay.setStatus(_A)
if mibBuilder.loadTexts:slcServSiteDialbackDelay.setUnits(_E)
_SlcServSiteIdleTimeout_Type=Integer32
_SlcServSiteIdleTimeout_Object=MibTableColumn
slcServSiteIdleTimeout=_SlcServSiteIdleTimeout_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,18),_SlcServSiteIdleTimeout_Type())
slcServSiteIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcServSiteIdleTimeout.setUnits(_E)
_SlcServSiteRestartDelay_Type=Integer32
_SlcServSiteRestartDelay_Object=MibTableColumn
slcServSiteRestartDelay=_SlcServSiteRestartDelay_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,19),_SlcServSiteRestartDelay_Type())
slcServSiteRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:slcServSiteRestartDelay.setUnits(_E)
_SlcServSiteCBCPServerAllowNoCallback_Type=EnabledState
_SlcServSiteCBCPServerAllowNoCallback_Object=MibTableColumn
slcServSiteCBCPServerAllowNoCallback=_SlcServSiteCBCPServerAllowNoCallback_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,20),_SlcServSiteCBCPServerAllowNoCallback_Type())
slcServSiteCBCPServerAllowNoCallback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteCBCPServerAllowNoCallback.setStatus(_A)
_SlcServSiteNATState_Type=EnabledState
_SlcServSiteNATState_Object=MibTableColumn
slcServSiteNATState=_SlcServSiteNATState_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,21),_SlcServSiteNATState_Type())
slcServSiteNATState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteNATState.setStatus(_A)
_SlcServSiteDialbackRetries_Type=Integer32
_SlcServSiteDialbackRetries_Object=MibTableColumn
slcServSiteDialbackRetries=_SlcServSiteDialbackRetries_Object((1,3,6,1,4,1,244,1,1,2,14,2,1,22),_SlcServSiteDialbackRetries_Type())
slcServSiteDialbackRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:slcServSiteDialbackRetries.setStatus(_A)
_SlcAuth_ObjectIdentity=ObjectIdentity
slcAuth=_SlcAuth_ObjectIdentity((1,3,6,1,4,1,244,1,1,3))
_SlcAuthLocal_ObjectIdentity=ObjectIdentity
slcAuthLocal=_SlcAuthLocal_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,1))
class _SlcAuthLocalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_SlcAuthLocalNumber_Type.__name__=_C
_SlcAuthLocalNumber_Object=MibScalar
slcAuthLocalNumber=_SlcAuthLocalNumber_Object((1,3,6,1,4,1,244,1,1,3,1,1),_SlcAuthLocalNumber_Type())
slcAuthLocalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalNumber.setStatus(_A)
_SlcAuthLocalUsersTable_Object=MibTable
slcAuthLocalUsersTable=_SlcAuthLocalUsersTable_Object((1,3,6,1,4,1,244,1,1,3,1,2))
if mibBuilder.loadTexts:slcAuthLocalUsersTable.setStatus(_A)
_SlcAuthLocalUserEntry_Object=MibTableRow
slcAuthLocalUserEntry=_SlcAuthLocalUserEntry_Object((1,3,6,1,4,1,244,1,1,3,1,2,1))
slcAuthLocalUserEntry.setIndexNames((0,_D,_AE))
if mibBuilder.loadTexts:slcAuthLocalUserEntry.setStatus(_A)
class _SlcAuthLocalUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_SlcAuthLocalUserIndex_Type.__name__=_C
_SlcAuthLocalUserIndex_Object=MibTableColumn
slcAuthLocalUserIndex=_SlcAuthLocalUserIndex_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,1),_SlcAuthLocalUserIndex_Type())
slcAuthLocalUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserIndex.setStatus(_A)
class _SlcAuthLocalUserLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_SlcAuthLocalUserLogin_Type.__name__=_F
_SlcAuthLocalUserLogin_Object=MibTableColumn
slcAuthLocalUserLogin=_SlcAuthLocalUserLogin_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,2),_SlcAuthLocalUserLogin_Type())
slcAuthLocalUserLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserLogin.setStatus(_A)
_SlcAuthLocalUserUID_Type=Unsigned32
_SlcAuthLocalUserUID_Object=MibTableColumn
slcAuthLocalUserUID=_SlcAuthLocalUserUID_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,3),_SlcAuthLocalUserUID_Type())
slcAuthLocalUserUID.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserUID.setStatus(_A)
_SlcAuthLocalUserListenPorts_Type=OctetString
_SlcAuthLocalUserListenPorts_Object=MibTableColumn
slcAuthLocalUserListenPorts=_SlcAuthLocalUserListenPorts_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,4),_SlcAuthLocalUserListenPorts_Type())
slcAuthLocalUserListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserListenPorts.setStatus(_A)
_SlcAuthLocalUserDataPorts_Type=OctetString
_SlcAuthLocalUserDataPorts_Object=MibTableColumn
slcAuthLocalUserDataPorts=_SlcAuthLocalUserDataPorts_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,5),_SlcAuthLocalUserDataPorts_Type())
slcAuthLocalUserDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserDataPorts.setStatus(_A)
_SlcAuthLocalUserClearPorts_Type=OctetString
_SlcAuthLocalUserClearPorts_Object=MibTableColumn
slcAuthLocalUserClearPorts=_SlcAuthLocalUserClearPorts_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,6),_SlcAuthLocalUserClearPorts_Type())
slcAuthLocalUserClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserClearPorts.setStatus(_A)
_SlcAuthLocalUserEscapeSeq_Type=OctetString
_SlcAuthLocalUserEscapeSeq_Object=MibTableColumn
slcAuthLocalUserEscapeSeq=_SlcAuthLocalUserEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,7),_SlcAuthLocalUserEscapeSeq_Type())
slcAuthLocalUserEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserEscapeSeq.setStatus(_A)
_SlcAuthLocalUserBreakSeq_Type=OctetString
_SlcAuthLocalUserBreakSeq_Object=MibTableColumn
slcAuthLocalUserBreakSeq=_SlcAuthLocalUserBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,8),_SlcAuthLocalUserBreakSeq_Type())
slcAuthLocalUserBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserBreakSeq.setStatus(_A)
_SlcAuthLocalUserMenu_Type=OctetString
_SlcAuthLocalUserMenu_Object=MibTableColumn
slcAuthLocalUserMenu=_SlcAuthLocalUserMenu_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,9),_SlcAuthLocalUserMenu_Type())
slcAuthLocalUserMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserMenu.setStatus(_A)
_SlcAuthLocalUserDialback_Type=EnabledState
_SlcAuthLocalUserDialback_Object=MibTableColumn
slcAuthLocalUserDialback=_SlcAuthLocalUserDialback_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,10),_SlcAuthLocalUserDialback_Type())
slcAuthLocalUserDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserDialback.setStatus(_A)
_SlcAuthLocalUserDialbackNum_Type=OctetString
_SlcAuthLocalUserDialbackNum_Object=MibTableColumn
slcAuthLocalUserDialbackNum=_SlcAuthLocalUserDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,11),_SlcAuthLocalUserDialbackNum_Type())
slcAuthLocalUserDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserDialbackNum.setStatus(_A)
_SlcAuthLocalUserGroup_Type=UserGroup
_SlcAuthLocalUserGroup_Object=MibTableColumn
slcAuthLocalUserGroup=_SlcAuthLocalUserGroup_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,12),_SlcAuthLocalUserGroup_Type())
slcAuthLocalUserGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserGroup.setStatus(_A)
_SlcAuthLocalUserRights_Type=UserRights
_SlcAuthLocalUserRights_Object=MibTableColumn
slcAuthLocalUserRights=_SlcAuthLocalUserRights_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,13),_SlcAuthLocalUserRights_Type())
slcAuthLocalUserRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserRights.setStatus(_A)
_SlcAuthLocalUserPwdExpires_Type=EnabledState
_SlcAuthLocalUserPwdExpires_Object=MibTableColumn
slcAuthLocalUserPwdExpires=_SlcAuthLocalUserPwdExpires_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,14),_SlcAuthLocalUserPwdExpires_Type())
slcAuthLocalUserPwdExpires.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserPwdExpires.setStatus(_A)
_SlcAuthLocalUserChangePwd_Type=EnabledState
_SlcAuthLocalUserChangePwd_Object=MibTableColumn
slcAuthLocalUserChangePwd=_SlcAuthLocalUserChangePwd_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,15),_SlcAuthLocalUserChangePwd_Type())
slcAuthLocalUserChangePwd.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserChangePwd.setStatus(_A)
_SlcAuthLocalUserChangePwdNextLogin_Type=EnabledState
_SlcAuthLocalUserChangePwdNextLogin_Object=MibTableColumn
slcAuthLocalUserChangePwdNextLogin=_SlcAuthLocalUserChangePwdNextLogin_Object((1,3,6,1,4,1,244,1,1,3,1,2,1,16),_SlcAuthLocalUserChangePwdNextLogin_Type())
slcAuthLocalUserChangePwdNextLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUserChangePwdNextLogin.setStatus(_A)
_SlcAuthLocalState_Type=EnabledState
_SlcAuthLocalState_Object=MibScalar
slcAuthLocalState=_SlcAuthLocalState_Object((1,3,6,1,4,1,244,1,1,3,1,3),_SlcAuthLocalState_Type())
slcAuthLocalState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalState.setStatus(_A)
_SlcAuthLocalOrder_Type=AuthOrder
_SlcAuthLocalOrder_Object=MibScalar
slcAuthLocalOrder=_SlcAuthLocalOrder_Object((1,3,6,1,4,1,244,1,1,3,1,4),_SlcAuthLocalOrder_Type())
slcAuthLocalOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalOrder.setStatus(_A)
_SlcAuthLocalComplexPasswords_Type=EnabledState
_SlcAuthLocalComplexPasswords_Object=MibScalar
slcAuthLocalComplexPasswords=_SlcAuthLocalComplexPasswords_Object((1,3,6,1,4,1,244,1,1,3,1,5),_SlcAuthLocalComplexPasswords_Type())
slcAuthLocalComplexPasswords.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalComplexPasswords.setStatus(_A)
_SlcAuthLocalUseNextMethod_Type=EnabledState
_SlcAuthLocalUseNextMethod_Object=MibScalar
slcAuthLocalUseNextMethod=_SlcAuthLocalUseNextMethod_Object((1,3,6,1,4,1,244,1,1,3,1,6),_SlcAuthLocalUseNextMethod_Type())
slcAuthLocalUseNextMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalUseNextMethod.setStatus(_A)
_SlcAuthLocalAllowReuse_Type=EnabledState
_SlcAuthLocalAllowReuse_Object=MibScalar
slcAuthLocalAllowReuse=_SlcAuthLocalAllowReuse_Object((1,3,6,1,4,1,244,1,1,3,1,7),_SlcAuthLocalAllowReuse_Type())
slcAuthLocalAllowReuse.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalAllowReuse.setStatus(_A)
class _SlcAuthLocalReuseHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SlcAuthLocalReuseHistory_Type.__name__=_C
_SlcAuthLocalReuseHistory_Object=MibScalar
slcAuthLocalReuseHistory=_SlcAuthLocalReuseHistory_Object((1,3,6,1,4,1,244,1,1,3,1,8),_SlcAuthLocalReuseHistory_Type())
slcAuthLocalReuseHistory.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalReuseHistory.setStatus(_A)
class _SlcAuthLocalPasswordLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,365))
_SlcAuthLocalPasswordLifetime_Type.__name__=_C
_SlcAuthLocalPasswordLifetime_Object=MibScalar
slcAuthLocalPasswordLifetime=_SlcAuthLocalPasswordLifetime_Object((1,3,6,1,4,1,244,1,1,3,1,9),_SlcAuthLocalPasswordLifetime_Type())
slcAuthLocalPasswordLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalPasswordLifetime.setStatus(_A)
if mibBuilder.loadTexts:slcAuthLocalPasswordLifetime.setUnits('days')
class _SlcAuthLocalWarningPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_SlcAuthLocalWarningPeriod_Type.__name__=_C
_SlcAuthLocalWarningPeriod_Object=MibScalar
slcAuthLocalWarningPeriod=_SlcAuthLocalWarningPeriod_Object((1,3,6,1,4,1,244,1,1,3,1,10),_SlcAuthLocalWarningPeriod_Type())
slcAuthLocalWarningPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalWarningPeriod.setStatus(_A)
if mibBuilder.loadTexts:slcAuthLocalWarningPeriod.setUnits('days')
class _SlcAuthLocalMaxLoginAttempts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SlcAuthLocalMaxLoginAttempts_Type.__name__=_C
_SlcAuthLocalMaxLoginAttempts_Object=MibScalar
slcAuthLocalMaxLoginAttempts=_SlcAuthLocalMaxLoginAttempts_Object((1,3,6,1,4,1,244,1,1,3,1,11),_SlcAuthLocalMaxLoginAttempts_Type())
slcAuthLocalMaxLoginAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalMaxLoginAttempts.setStatus(_A)
class _SlcAuthLocalLockoutPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_SlcAuthLocalLockoutPeriod_Type.__name__=_C
_SlcAuthLocalLockoutPeriod_Object=MibScalar
slcAuthLocalLockoutPeriod=_SlcAuthLocalLockoutPeriod_Object((1,3,6,1,4,1,244,1,1,3,1,12),_SlcAuthLocalLockoutPeriod_Type())
slcAuthLocalLockoutPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalLockoutPeriod.setStatus(_A)
if mibBuilder.loadTexts:slcAuthLocalLockoutPeriod.setUnits(_H)
_SlcAuthLocalMultipleSysadminLogins_Type=EnabledState
_SlcAuthLocalMultipleSysadminLogins_Object=MibScalar
slcAuthLocalMultipleSysadminLogins=_SlcAuthLocalMultipleSysadminLogins_Object((1,3,6,1,4,1,244,1,1,3,1,13),_SlcAuthLocalMultipleSysadminLogins_Type())
slcAuthLocalMultipleSysadminLogins.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalMultipleSysadminLogins.setStatus(_A)
_SlcAuthLocalSysadminConsoleOnly_Type=EnabledState
_SlcAuthLocalSysadminConsoleOnly_Object=MibScalar
slcAuthLocalSysadminConsoleOnly=_SlcAuthLocalSysadminConsoleOnly_Object((1,3,6,1,4,1,244,1,1,3,1,14),_SlcAuthLocalSysadminConsoleOnly_Type())
slcAuthLocalSysadminConsoleOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLocalSysadminConsoleOnly.setStatus(_A)
_SlcAuthNIS_ObjectIdentity=ObjectIdentity
slcAuthNIS=_SlcAuthNIS_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,2))
_SlcAuthNISState_Type=EnabledState
_SlcAuthNISState_Object=MibScalar
slcAuthNISState=_SlcAuthNISState_Object((1,3,6,1,4,1,244,1,1,3,2,1),_SlcAuthNISState_Type())
slcAuthNISState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISState.setStatus(_A)
_SlcAuthNISOrder_Type=AuthOrder
_SlcAuthNISOrder_Object=MibScalar
slcAuthNISOrder=_SlcAuthNISOrder_Object((1,3,6,1,4,1,244,1,1,3,2,2),_SlcAuthNISOrder_Type())
slcAuthNISOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISOrder.setStatus(_A)
class _SlcAuthNISDomain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlcAuthNISDomain_Type.__name__=_F
_SlcAuthNISDomain_Object=MibScalar
slcAuthNISDomain=_SlcAuthNISDomain_Object((1,3,6,1,4,1,244,1,1,3,2,3),_SlcAuthNISDomain_Type())
slcAuthNISDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISDomain.setStatus(_A)
_SlcAuthNISBroadcast_Type=EnabledState
_SlcAuthNISBroadcast_Object=MibScalar
slcAuthNISBroadcast=_SlcAuthNISBroadcast_Object((1,3,6,1,4,1,244,1,1,3,2,4),_SlcAuthNISBroadcast_Type())
slcAuthNISBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISBroadcast.setStatus(_A)
_SlcAuthNISMaster_Type=IpAddress
_SlcAuthNISMaster_Object=MibScalar
slcAuthNISMaster=_SlcAuthNISMaster_Object((1,3,6,1,4,1,244,1,1,3,2,5),_SlcAuthNISMaster_Type())
slcAuthNISMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISMaster.setStatus(_A)
_SlcAuthNISSlave1_Type=IpAddress
_SlcAuthNISSlave1_Object=MibScalar
slcAuthNISSlave1=_SlcAuthNISSlave1_Object((1,3,6,1,4,1,244,1,1,3,2,6),_SlcAuthNISSlave1_Type())
slcAuthNISSlave1.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISSlave1.setStatus(_A)
_SlcAuthNISSlave2_Type=IpAddress
_SlcAuthNISSlave2_Object=MibScalar
slcAuthNISSlave2=_SlcAuthNISSlave2_Object((1,3,6,1,4,1,244,1,1,3,2,7),_SlcAuthNISSlave2_Type())
slcAuthNISSlave2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISSlave2.setStatus(_A)
_SlcAuthNISSlave3_Type=IpAddress
_SlcAuthNISSlave3_Object=MibScalar
slcAuthNISSlave3=_SlcAuthNISSlave3_Object((1,3,6,1,4,1,244,1,1,3,2,8),_SlcAuthNISSlave3_Type())
slcAuthNISSlave3.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISSlave3.setStatus(_A)
_SlcAuthNISGroup_Type=UserGroup
_SlcAuthNISGroup_Object=MibScalar
slcAuthNISGroup=_SlcAuthNISGroup_Object((1,3,6,1,4,1,244,1,1,3,2,9),_SlcAuthNISGroup_Type())
slcAuthNISGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISGroup.setStatus(_A)
_SlcAuthNISRights_Type=UserRights
_SlcAuthNISRights_Object=MibScalar
slcAuthNISRights=_SlcAuthNISRights_Object((1,3,6,1,4,1,244,1,1,3,2,10),_SlcAuthNISRights_Type())
slcAuthNISRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISRights.setStatus(_A)
_SlcAuthNISMenu_Type=OctetString
_SlcAuthNISMenu_Object=MibScalar
slcAuthNISMenu=_SlcAuthNISMenu_Object((1,3,6,1,4,1,244,1,1,3,2,11),_SlcAuthNISMenu_Type())
slcAuthNISMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISMenu.setStatus(_A)
_SlcAuthNISListenPorts_Type=OctetString
_SlcAuthNISListenPorts_Object=MibScalar
slcAuthNISListenPorts=_SlcAuthNISListenPorts_Object((1,3,6,1,4,1,244,1,1,3,2,12),_SlcAuthNISListenPorts_Type())
slcAuthNISListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISListenPorts.setStatus(_A)
_SlcAuthNISDataPorts_Type=OctetString
_SlcAuthNISDataPorts_Object=MibScalar
slcAuthNISDataPorts=_SlcAuthNISDataPorts_Object((1,3,6,1,4,1,244,1,1,3,2,13),_SlcAuthNISDataPorts_Type())
slcAuthNISDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISDataPorts.setStatus(_A)
_SlcAuthNISClearPorts_Type=OctetString
_SlcAuthNISClearPorts_Object=MibScalar
slcAuthNISClearPorts=_SlcAuthNISClearPorts_Object((1,3,6,1,4,1,244,1,1,3,2,14),_SlcAuthNISClearPorts_Type())
slcAuthNISClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISClearPorts.setStatus(_A)
_SlcAuthNISSlave4_Type=IpAddress
_SlcAuthNISSlave4_Object=MibScalar
slcAuthNISSlave4=_SlcAuthNISSlave4_Object((1,3,6,1,4,1,244,1,1,3,2,15),_SlcAuthNISSlave4_Type())
slcAuthNISSlave4.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISSlave4.setStatus(_A)
_SlcAuthNISSlave5_Type=IpAddress
_SlcAuthNISSlave5_Object=MibScalar
slcAuthNISSlave5=_SlcAuthNISSlave5_Object((1,3,6,1,4,1,244,1,1,3,2,16),_SlcAuthNISSlave5_Type())
slcAuthNISSlave5.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISSlave5.setStatus(_A)
_SlcAuthNISEscapeSeq_Type=OctetString
_SlcAuthNISEscapeSeq_Object=MibScalar
slcAuthNISEscapeSeq=_SlcAuthNISEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,2,17),_SlcAuthNISEscapeSeq_Type())
slcAuthNISEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISEscapeSeq.setStatus(_A)
_SlcAuthNISBreakSeq_Type=OctetString
_SlcAuthNISBreakSeq_Object=MibScalar
slcAuthNISBreakSeq=_SlcAuthNISBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,2,18),_SlcAuthNISBreakSeq_Type())
slcAuthNISBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISBreakSeq.setStatus(_A)
_SlcAuthNISDialback_Type=EnabledState
_SlcAuthNISDialback_Object=MibScalar
slcAuthNISDialback=_SlcAuthNISDialback_Object((1,3,6,1,4,1,244,1,1,3,2,19),_SlcAuthNISDialback_Type())
slcAuthNISDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISDialback.setStatus(_A)
_SlcAuthNISDialbackNum_Type=OctetString
_SlcAuthNISDialbackNum_Object=MibScalar
slcAuthNISDialbackNum=_SlcAuthNISDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,2,20),_SlcAuthNISDialbackNum_Type())
slcAuthNISDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthNISDialbackNum.setStatus(_A)
_SlcAuthLDAP_ObjectIdentity=ObjectIdentity
slcAuthLDAP=_SlcAuthLDAP_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,3))
_SlcAuthLDAPState_Type=EnabledState
_SlcAuthLDAPState_Object=MibScalar
slcAuthLDAPState=_SlcAuthLDAPState_Object((1,3,6,1,4,1,244,1,1,3,3,1),_SlcAuthLDAPState_Type())
slcAuthLDAPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPState.setStatus(_A)
_SlcAuthLDAPOrder_Type=AuthOrder
_SlcAuthLDAPOrder_Object=MibScalar
slcAuthLDAPOrder=_SlcAuthLDAPOrder_Object((1,3,6,1,4,1,244,1,1,3,3,2),_SlcAuthLDAPOrder_Type())
slcAuthLDAPOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPOrder.setStatus(_A)
_SlcAuthLDAPServer_Type=IpAddress
_SlcAuthLDAPServer_Object=MibScalar
slcAuthLDAPServer=_SlcAuthLDAPServer_Object((1,3,6,1,4,1,244,1,1,3,3,3),_SlcAuthLDAPServer_Type())
slcAuthLDAPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPServer.setStatus(_A)
class _SlcAuthLDAPBase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlcAuthLDAPBase_Type.__name__=_F
_SlcAuthLDAPBase_Object=MibScalar
slcAuthLDAPBase=_SlcAuthLDAPBase_Object((1,3,6,1,4,1,244,1,1,3,3,4),_SlcAuthLDAPBase_Type())
slcAuthLDAPBase.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPBase.setStatus(_A)
class _SlcAuthLDAPBindName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlcAuthLDAPBindName_Type.__name__=_F
_SlcAuthLDAPBindName_Object=MibScalar
slcAuthLDAPBindName=_SlcAuthLDAPBindName_Object((1,3,6,1,4,1,244,1,1,3,3,5),_SlcAuthLDAPBindName_Type())
slcAuthLDAPBindName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPBindName.setStatus(_A)
class _SlcAuthLDAPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcAuthLDAPPort_Type.__name__=_C
_SlcAuthLDAPPort_Object=MibScalar
slcAuthLDAPPort=_SlcAuthLDAPPort_Object((1,3,6,1,4,1,244,1,1,3,3,6),_SlcAuthLDAPPort_Type())
slcAuthLDAPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPPort.setStatus(_A)
_SlcAuthLDAPADSupport_Type=EnabledState
_SlcAuthLDAPADSupport_Object=MibScalar
slcAuthLDAPADSupport=_SlcAuthLDAPADSupport_Object((1,3,6,1,4,1,244,1,1,3,3,7),_SlcAuthLDAPADSupport_Type())
slcAuthLDAPADSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPADSupport.setStatus(_A)
_SlcAuthLDAPGroup_Type=UserGroup
_SlcAuthLDAPGroup_Object=MibScalar
slcAuthLDAPGroup=_SlcAuthLDAPGroup_Object((1,3,6,1,4,1,244,1,1,3,3,8),_SlcAuthLDAPGroup_Type())
slcAuthLDAPGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPGroup.setStatus(_A)
_SlcAuthLDAPRights_Type=UserRights
_SlcAuthLDAPRights_Object=MibScalar
slcAuthLDAPRights=_SlcAuthLDAPRights_Object((1,3,6,1,4,1,244,1,1,3,3,9),_SlcAuthLDAPRights_Type())
slcAuthLDAPRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPRights.setStatus(_A)
_SlcAuthLDAPMenu_Type=OctetString
_SlcAuthLDAPMenu_Object=MibScalar
slcAuthLDAPMenu=_SlcAuthLDAPMenu_Object((1,3,6,1,4,1,244,1,1,3,3,10),_SlcAuthLDAPMenu_Type())
slcAuthLDAPMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPMenu.setStatus(_A)
_SlcAuthLDAPListenPorts_Type=OctetString
_SlcAuthLDAPListenPorts_Object=MibScalar
slcAuthLDAPListenPorts=_SlcAuthLDAPListenPorts_Object((1,3,6,1,4,1,244,1,1,3,3,11),_SlcAuthLDAPListenPorts_Type())
slcAuthLDAPListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPListenPorts.setStatus(_A)
_SlcAuthLDAPDataPorts_Type=OctetString
_SlcAuthLDAPDataPorts_Object=MibScalar
slcAuthLDAPDataPorts=_SlcAuthLDAPDataPorts_Object((1,3,6,1,4,1,244,1,1,3,3,12),_SlcAuthLDAPDataPorts_Type())
slcAuthLDAPDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPDataPorts.setStatus(_A)
_SlcAuthLDAPClearPorts_Type=OctetString
_SlcAuthLDAPClearPorts_Object=MibScalar
slcAuthLDAPClearPorts=_SlcAuthLDAPClearPorts_Object((1,3,6,1,4,1,244,1,1,3,3,13),_SlcAuthLDAPClearPorts_Type())
slcAuthLDAPClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPClearPorts.setStatus(_A)
_SlcAuthLDAPEncrypt_Type=EnabledState
_SlcAuthLDAPEncrypt_Object=MibScalar
slcAuthLDAPEncrypt=_SlcAuthLDAPEncrypt_Object((1,3,6,1,4,1,244,1,1,3,3,14),_SlcAuthLDAPEncrypt_Type())
slcAuthLDAPEncrypt.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPEncrypt.setStatus(_A)
_SlcAuthLDAPEscapeSeq_Type=OctetString
_SlcAuthLDAPEscapeSeq_Object=MibScalar
slcAuthLDAPEscapeSeq=_SlcAuthLDAPEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,3,15),_SlcAuthLDAPEscapeSeq_Type())
slcAuthLDAPEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPEscapeSeq.setStatus(_A)
_SlcAuthLDAPBreakSeq_Type=OctetString
_SlcAuthLDAPBreakSeq_Object=MibScalar
slcAuthLDAPBreakSeq=_SlcAuthLDAPBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,3,16),_SlcAuthLDAPBreakSeq_Type())
slcAuthLDAPBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPBreakSeq.setStatus(_A)
_SlcAuthLDAPBindWithLogin_Type=EnabledState
_SlcAuthLDAPBindWithLogin_Object=MibScalar
slcAuthLDAPBindWithLogin=_SlcAuthLDAPBindWithLogin_Object((1,3,6,1,4,1,244,1,1,3,3,17),_SlcAuthLDAPBindWithLogin_Type())
slcAuthLDAPBindWithLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPBindWithLogin.setStatus(_A)
_SlcAuthLDAPUseLDAPSchema_Type=EnabledState
_SlcAuthLDAPUseLDAPSchema_Object=MibScalar
slcAuthLDAPUseLDAPSchema=_SlcAuthLDAPUseLDAPSchema_Object((1,3,6,1,4,1,244,1,1,3,3,18),_SlcAuthLDAPUseLDAPSchema_Type())
slcAuthLDAPUseLDAPSchema.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPUseLDAPSchema.setStatus(_A)
_SlcAuthLDAPDialback_Type=EnabledState
_SlcAuthLDAPDialback_Object=MibScalar
slcAuthLDAPDialback=_SlcAuthLDAPDialback_Object((1,3,6,1,4,1,244,1,1,3,3,19),_SlcAuthLDAPDialback_Type())
slcAuthLDAPDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPDialback.setStatus(_A)
_SlcAuthLDAPDialbackNum_Type=OctetString
_SlcAuthLDAPDialbackNum_Object=MibScalar
slcAuthLDAPDialbackNum=_SlcAuthLDAPDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,3,20),_SlcAuthLDAPDialbackNum_Type())
slcAuthLDAPDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPDialbackNum.setStatus(_A)
_SlcAuthLDAPUserFilter_Type=OctetString
_SlcAuthLDAPUserFilter_Object=MibScalar
slcAuthLDAPUserFilter=_SlcAuthLDAPUserFilter_Object((1,3,6,1,4,1,244,1,1,3,3,21),_SlcAuthLDAPUserFilter_Type())
slcAuthLDAPUserFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPUserFilter.setStatus(_A)
_SlcAuthLDAPGroupFilter_Type=OctetString
_SlcAuthLDAPGroupFilter_Object=MibScalar
slcAuthLDAPGroupFilter=_SlcAuthLDAPGroupFilter_Object((1,3,6,1,4,1,244,1,1,3,3,22),_SlcAuthLDAPGroupFilter_Type())
slcAuthLDAPGroupFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPGroupFilter.setStatus(_A)
_SlcAuthLDAPGroupMembershipAttr_Type=OctetString
_SlcAuthLDAPGroupMembershipAttr_Object=MibScalar
slcAuthLDAPGroupMembershipAttr=_SlcAuthLDAPGroupMembershipAttr_Object((1,3,6,1,4,1,244,1,1,3,3,23),_SlcAuthLDAPGroupMembershipAttr_Type())
slcAuthLDAPGroupMembershipAttr.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPGroupMembershipAttr.setStatus(_A)
_SlcAuthLDAPGroupMembershipDN_Type=EnabledState
_SlcAuthLDAPGroupMembershipDN_Object=MibScalar
slcAuthLDAPGroupMembershipDN=_SlcAuthLDAPGroupMembershipDN_Object((1,3,6,1,4,1,244,1,1,3,3,24),_SlcAuthLDAPGroupMembershipDN_Type())
slcAuthLDAPGroupMembershipDN.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPGroupMembershipDN.setStatus(_A)
_SlcAuthLDAPServer2_Type=IpAddress
_SlcAuthLDAPServer2_Object=MibScalar
slcAuthLDAPServer2=_SlcAuthLDAPServer2_Object((1,3,6,1,4,1,244,1,1,3,3,25),_SlcAuthLDAPServer2_Type())
slcAuthLDAPServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPServer2.setStatus(_A)
_SlcAuthLDAPServerIPv6_Type=Ipv6Address
_SlcAuthLDAPServerIPv6_Object=MibScalar
slcAuthLDAPServerIPv6=_SlcAuthLDAPServerIPv6_Object((1,3,6,1,4,1,244,1,1,3,3,26),_SlcAuthLDAPServerIPv6_Type())
slcAuthLDAPServerIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPServerIPv6.setStatus(_A)
_SlcAuthLDAPServer2IPv6_Type=Ipv6Address
_SlcAuthLDAPServer2IPv6_Object=MibScalar
slcAuthLDAPServer2IPv6=_SlcAuthLDAPServer2IPv6_Object((1,3,6,1,4,1,244,1,1,3,3,27),_SlcAuthLDAPServer2IPv6_Type())
slcAuthLDAPServer2IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthLDAPServer2IPv6.setStatus(_A)
_SlcAuthRADIUS_ObjectIdentity=ObjectIdentity
slcAuthRADIUS=_SlcAuthRADIUS_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,4))
_SlcAuthRADIUSState_Type=EnabledState
_SlcAuthRADIUSState_Object=MibScalar
slcAuthRADIUSState=_SlcAuthRADIUSState_Object((1,3,6,1,4,1,244,1,1,3,4,1),_SlcAuthRADIUSState_Type())
slcAuthRADIUSState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSState.setStatus(_A)
_SlcAuthRADIUSOrder_Type=AuthOrder
_SlcAuthRADIUSOrder_Object=MibScalar
slcAuthRADIUSOrder=_SlcAuthRADIUSOrder_Object((1,3,6,1,4,1,244,1,1,3,4,2),_SlcAuthRADIUSOrder_Type())
slcAuthRADIUSOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSOrder.setStatus(_A)
class _SlcAuthRADIUSTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcAuthRADIUSTimeout_Type.__name__=_C
_SlcAuthRADIUSTimeout_Object=MibScalar
slcAuthRADIUSTimeout=_SlcAuthRADIUSTimeout_Object((1,3,6,1,4,1,244,1,1,3,4,3),_SlcAuthRADIUSTimeout_Type())
slcAuthRADIUSTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcAuthRADIUSTimeout.setUnits(_E)
_SlcAuthRADIUSServerTable_Object=MibTable
slcAuthRADIUSServerTable=_SlcAuthRADIUSServerTable_Object((1,3,6,1,4,1,244,1,1,3,4,4))
if mibBuilder.loadTexts:slcAuthRADIUSServerTable.setStatus(_A)
_SlcAuthRADIUSServerEntry_Object=MibTableRow
slcAuthRADIUSServerEntry=_SlcAuthRADIUSServerEntry_Object((1,3,6,1,4,1,244,1,1,3,4,4,1))
slcAuthRADIUSServerEntry.setIndexNames((0,_D,_AF))
if mibBuilder.loadTexts:slcAuthRADIUSServerEntry.setStatus(_A)
class _SlcAuthRADIUSServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SlcAuthRADIUSServerIndex_Type.__name__=_C
_SlcAuthRADIUSServerIndex_Object=MibTableColumn
slcAuthRADIUSServerIndex=_SlcAuthRADIUSServerIndex_Object((1,3,6,1,4,1,244,1,1,3,4,4,1,1),_SlcAuthRADIUSServerIndex_Type())
slcAuthRADIUSServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSServerIndex.setStatus(_A)
_SlcAuthRADIUSServer_Type=IpAddress
_SlcAuthRADIUSServer_Object=MibTableColumn
slcAuthRADIUSServer=_SlcAuthRADIUSServer_Object((1,3,6,1,4,1,244,1,1,3,4,4,1,2),_SlcAuthRADIUSServer_Type())
slcAuthRADIUSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSServer.setStatus(_A)
class _SlcAuthRADIUSPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcAuthRADIUSPort_Type.__name__=_C
_SlcAuthRADIUSPort_Object=MibTableColumn
slcAuthRADIUSPort=_SlcAuthRADIUSPort_Object((1,3,6,1,4,1,244,1,1,3,4,4,1,3),_SlcAuthRADIUSPort_Type())
slcAuthRADIUSPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSPort.setStatus(_A)
_SlcAuthRADIUSServerIPv6_Type=Ipv6Address
_SlcAuthRADIUSServerIPv6_Object=MibTableColumn
slcAuthRADIUSServerIPv6=_SlcAuthRADIUSServerIPv6_Object((1,3,6,1,4,1,244,1,1,3,4,4,1,4),_SlcAuthRADIUSServerIPv6_Type())
slcAuthRADIUSServerIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSServerIPv6.setStatus(_A)
_SlcAuthRADIUSGroup_Type=UserGroup
_SlcAuthRADIUSGroup_Object=MibScalar
slcAuthRADIUSGroup=_SlcAuthRADIUSGroup_Object((1,3,6,1,4,1,244,1,1,3,4,5),_SlcAuthRADIUSGroup_Type())
slcAuthRADIUSGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSGroup.setStatus(_A)
_SlcAuthRADIUSRights_Type=UserRights
_SlcAuthRADIUSRights_Object=MibScalar
slcAuthRADIUSRights=_SlcAuthRADIUSRights_Object((1,3,6,1,4,1,244,1,1,3,4,6),_SlcAuthRADIUSRights_Type())
slcAuthRADIUSRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSRights.setStatus(_A)
_SlcAuthRADIUSMenu_Type=OctetString
_SlcAuthRADIUSMenu_Object=MibScalar
slcAuthRADIUSMenu=_SlcAuthRADIUSMenu_Object((1,3,6,1,4,1,244,1,1,3,4,7),_SlcAuthRADIUSMenu_Type())
slcAuthRADIUSMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSMenu.setStatus(_A)
_SlcAuthRADIUSListenPorts_Type=OctetString
_SlcAuthRADIUSListenPorts_Object=MibScalar
slcAuthRADIUSListenPorts=_SlcAuthRADIUSListenPorts_Object((1,3,6,1,4,1,244,1,1,3,4,8),_SlcAuthRADIUSListenPorts_Type())
slcAuthRADIUSListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSListenPorts.setStatus(_A)
_SlcAuthRADIUSDataPorts_Type=OctetString
_SlcAuthRADIUSDataPorts_Object=MibScalar
slcAuthRADIUSDataPorts=_SlcAuthRADIUSDataPorts_Object((1,3,6,1,4,1,244,1,1,3,4,9),_SlcAuthRADIUSDataPorts_Type())
slcAuthRADIUSDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSDataPorts.setStatus(_A)
_SlcAuthRADIUSClearPorts_Type=OctetString
_SlcAuthRADIUSClearPorts_Object=MibScalar
slcAuthRADIUSClearPorts=_SlcAuthRADIUSClearPorts_Object((1,3,6,1,4,1,244,1,1,3,4,10),_SlcAuthRADIUSClearPorts_Type())
slcAuthRADIUSClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSClearPorts.setStatus(_A)
_SlcAuthRADIUSEscapeSeq_Type=OctetString
_SlcAuthRADIUSEscapeSeq_Object=MibScalar
slcAuthRADIUSEscapeSeq=_SlcAuthRADIUSEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,4,11),_SlcAuthRADIUSEscapeSeq_Type())
slcAuthRADIUSEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSEscapeSeq.setStatus(_A)
_SlcAuthRADIUSBreakSeq_Type=OctetString
_SlcAuthRADIUSBreakSeq_Object=MibScalar
slcAuthRADIUSBreakSeq=_SlcAuthRADIUSBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,4,12),_SlcAuthRADIUSBreakSeq_Type())
slcAuthRADIUSBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSBreakSeq.setStatus(_A)
_SlcAuthRADIUSDialback_Type=EnabledState
_SlcAuthRADIUSDialback_Object=MibScalar
slcAuthRADIUSDialback=_SlcAuthRADIUSDialback_Object((1,3,6,1,4,1,244,1,1,3,4,13),_SlcAuthRADIUSDialback_Type())
slcAuthRADIUSDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSDialback.setStatus(_A)
_SlcAuthRADIUSDialbackNum_Type=OctetString
_SlcAuthRADIUSDialbackNum_Object=MibScalar
slcAuthRADIUSDialbackNum=_SlcAuthRADIUSDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,4,14),_SlcAuthRADIUSDialbackNum_Type())
slcAuthRADIUSDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSDialbackNum.setStatus(_A)
_SlcAuthRADIUSUseVSA_Type=EnabledState
_SlcAuthRADIUSUseVSA_Object=MibScalar
slcAuthRADIUSUseVSA=_SlcAuthRADIUSUseVSA_Object((1,3,6,1,4,1,244,1,1,3,4,15),_SlcAuthRADIUSUseVSA_Type())
slcAuthRADIUSUseVSA.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRADIUSUseVSA.setStatus(_A)
_SlcAuthKerberos_ObjectIdentity=ObjectIdentity
slcAuthKerberos=_SlcAuthKerberos_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,5))
_SlcAuthKerbState_Type=EnabledState
_SlcAuthKerbState_Object=MibScalar
slcAuthKerbState=_SlcAuthKerbState_Object((1,3,6,1,4,1,244,1,1,3,5,1),_SlcAuthKerbState_Type())
slcAuthKerbState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbState.setStatus(_A)
_SlcAuthKerbOrder_Type=AuthOrder
_SlcAuthKerbOrder_Object=MibScalar
slcAuthKerbOrder=_SlcAuthKerbOrder_Object((1,3,6,1,4,1,244,1,1,3,5,2),_SlcAuthKerbOrder_Type())
slcAuthKerbOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbOrder.setStatus(_A)
class _SlcAuthKerbRealm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SlcAuthKerbRealm_Type.__name__=_F
_SlcAuthKerbRealm_Object=MibScalar
slcAuthKerbRealm=_SlcAuthKerbRealm_Object((1,3,6,1,4,1,244,1,1,3,5,3),_SlcAuthKerbRealm_Type())
slcAuthKerbRealm.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbRealm.setStatus(_A)
class _SlcAuthKerbKDC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SlcAuthKerbKDC_Type.__name__=_F
_SlcAuthKerbKDC_Object=MibScalar
slcAuthKerbKDC=_SlcAuthKerbKDC_Object((1,3,6,1,4,1,244,1,1,3,5,4),_SlcAuthKerbKDC_Type())
slcAuthKerbKDC.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbKDC.setStatus(_A)
_SlcAuthKerbKDCIP_Type=IpAddress
_SlcAuthKerbKDCIP_Object=MibScalar
slcAuthKerbKDCIP=_SlcAuthKerbKDCIP_Object((1,3,6,1,4,1,244,1,1,3,5,5),_SlcAuthKerbKDCIP_Type())
slcAuthKerbKDCIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbKDCIP.setStatus(_A)
class _SlcAuthKerbKDCPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcAuthKerbKDCPort_Type.__name__=_C
_SlcAuthKerbKDCPort_Object=MibScalar
slcAuthKerbKDCPort=_SlcAuthKerbKDCPort_Object((1,3,6,1,4,1,244,1,1,3,5,6),_SlcAuthKerbKDCPort_Type())
slcAuthKerbKDCPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbKDCPort.setStatus(_A)
_SlcAuthKerbUseLDAP_Type=EnabledState
_SlcAuthKerbUseLDAP_Object=MibScalar
slcAuthKerbUseLDAP=_SlcAuthKerbUseLDAP_Object((1,3,6,1,4,1,244,1,1,3,5,7),_SlcAuthKerbUseLDAP_Type())
slcAuthKerbUseLDAP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbUseLDAP.setStatus(_A)
_SlcAuthKerbGroup_Type=UserGroup
_SlcAuthKerbGroup_Object=MibScalar
slcAuthKerbGroup=_SlcAuthKerbGroup_Object((1,3,6,1,4,1,244,1,1,3,5,8),_SlcAuthKerbGroup_Type())
slcAuthKerbGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbGroup.setStatus(_A)
_SlcAuthKerbRights_Type=UserRights
_SlcAuthKerbRights_Object=MibScalar
slcAuthKerbRights=_SlcAuthKerbRights_Object((1,3,6,1,4,1,244,1,1,3,5,9),_SlcAuthKerbRights_Type())
slcAuthKerbRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbRights.setStatus(_A)
_SlcAuthKerbMenu_Type=OctetString
_SlcAuthKerbMenu_Object=MibScalar
slcAuthKerbMenu=_SlcAuthKerbMenu_Object((1,3,6,1,4,1,244,1,1,3,5,10),_SlcAuthKerbMenu_Type())
slcAuthKerbMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbMenu.setStatus(_A)
_SlcAuthKerbListenPorts_Type=OctetString
_SlcAuthKerbListenPorts_Object=MibScalar
slcAuthKerbListenPorts=_SlcAuthKerbListenPorts_Object((1,3,6,1,4,1,244,1,1,3,5,11),_SlcAuthKerbListenPorts_Type())
slcAuthKerbListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbListenPorts.setStatus(_A)
_SlcAuthKerbDataPorts_Type=OctetString
_SlcAuthKerbDataPorts_Object=MibScalar
slcAuthKerbDataPorts=_SlcAuthKerbDataPorts_Object((1,3,6,1,4,1,244,1,1,3,5,12),_SlcAuthKerbDataPorts_Type())
slcAuthKerbDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbDataPorts.setStatus(_A)
_SlcAuthKerbClearPorts_Type=OctetString
_SlcAuthKerbClearPorts_Object=MibScalar
slcAuthKerbClearPorts=_SlcAuthKerbClearPorts_Object((1,3,6,1,4,1,244,1,1,3,5,13),_SlcAuthKerbClearPorts_Type())
slcAuthKerbClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbClearPorts.setStatus(_A)
_SlcAuthKerbEscapeSeq_Type=OctetString
_SlcAuthKerbEscapeSeq_Object=MibScalar
slcAuthKerbEscapeSeq=_SlcAuthKerbEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,5,14),_SlcAuthKerbEscapeSeq_Type())
slcAuthKerbEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbEscapeSeq.setStatus(_A)
_SlcAuthKerbBreakSeq_Type=OctetString
_SlcAuthKerbBreakSeq_Object=MibScalar
slcAuthKerbBreakSeq=_SlcAuthKerbBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,5,15),_SlcAuthKerbBreakSeq_Type())
slcAuthKerbBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbBreakSeq.setStatus(_A)
_SlcAuthKerbDialback_Type=EnabledState
_SlcAuthKerbDialback_Object=MibScalar
slcAuthKerbDialback=_SlcAuthKerbDialback_Object((1,3,6,1,4,1,244,1,1,3,5,16),_SlcAuthKerbDialback_Type())
slcAuthKerbDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbDialback.setStatus(_A)
_SlcAuthKerbDialbackNum_Type=OctetString
_SlcAuthKerbDialbackNum_Object=MibScalar
slcAuthKerbDialbackNum=_SlcAuthKerbDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,5,17),_SlcAuthKerbDialbackNum_Type())
slcAuthKerbDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbDialbackNum.setStatus(_A)
_SlcAuthKerbKDCIPv6_Type=Ipv6Address
_SlcAuthKerbKDCIPv6_Object=MibScalar
slcAuthKerbKDCIPv6=_SlcAuthKerbKDCIPv6_Object((1,3,6,1,4,1,244,1,1,3,5,18),_SlcAuthKerbKDCIPv6_Type())
slcAuthKerbKDCIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthKerbKDCIPv6.setStatus(_A)
_SlcAuthTACACS_ObjectIdentity=ObjectIdentity
slcAuthTACACS=_SlcAuthTACACS_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,6))
_SlcAuthTACACSState_Type=EnabledState
_SlcAuthTACACSState_Object=MibScalar
slcAuthTACACSState=_SlcAuthTACACSState_Object((1,3,6,1,4,1,244,1,1,3,6,1),_SlcAuthTACACSState_Type())
slcAuthTACACSState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSState.setStatus(_A)
_SlcAuthTACACSOrder_Type=AuthOrder
_SlcAuthTACACSOrder_Object=MibScalar
slcAuthTACACSOrder=_SlcAuthTACACSOrder_Object((1,3,6,1,4,1,244,1,1,3,6,2),_SlcAuthTACACSOrder_Type())
slcAuthTACACSOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSOrder.setStatus(_A)
_SlcAuthTACACSServer_Type=IpAddress
_SlcAuthTACACSServer_Object=MibScalar
slcAuthTACACSServer=_SlcAuthTACACSServer_Object((1,3,6,1,4,1,244,1,1,3,6,3),_SlcAuthTACACSServer_Type())
slcAuthTACACSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSServer.setStatus(_A)
_SlcAuthTACACSEncrypt_Type=EnabledState
_SlcAuthTACACSEncrypt_Object=MibScalar
slcAuthTACACSEncrypt=_SlcAuthTACACSEncrypt_Object((1,3,6,1,4,1,244,1,1,3,6,4),_SlcAuthTACACSEncrypt_Type())
slcAuthTACACSEncrypt.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSEncrypt.setStatus(_A)
_SlcAuthTACACSGroup_Type=UserGroup
_SlcAuthTACACSGroup_Object=MibScalar
slcAuthTACACSGroup=_SlcAuthTACACSGroup_Object((1,3,6,1,4,1,244,1,1,3,6,5),_SlcAuthTACACSGroup_Type())
slcAuthTACACSGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSGroup.setStatus(_A)
_SlcAuthTACACSRights_Type=UserRights
_SlcAuthTACACSRights_Object=MibScalar
slcAuthTACACSRights=_SlcAuthTACACSRights_Object((1,3,6,1,4,1,244,1,1,3,6,6),_SlcAuthTACACSRights_Type())
slcAuthTACACSRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSRights.setStatus(_A)
_SlcAuthTACACSMenu_Type=OctetString
_SlcAuthTACACSMenu_Object=MibScalar
slcAuthTACACSMenu=_SlcAuthTACACSMenu_Object((1,3,6,1,4,1,244,1,1,3,6,7),_SlcAuthTACACSMenu_Type())
slcAuthTACACSMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSMenu.setStatus(_A)
_SlcAuthTACACSListenPorts_Type=OctetString
_SlcAuthTACACSListenPorts_Object=MibScalar
slcAuthTACACSListenPorts=_SlcAuthTACACSListenPorts_Object((1,3,6,1,4,1,244,1,1,3,6,8),_SlcAuthTACACSListenPorts_Type())
slcAuthTACACSListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSListenPorts.setStatus(_A)
_SlcAuthTACACSDataPorts_Type=OctetString
_SlcAuthTACACSDataPorts_Object=MibScalar
slcAuthTACACSDataPorts=_SlcAuthTACACSDataPorts_Object((1,3,6,1,4,1,244,1,1,3,6,9),_SlcAuthTACACSDataPorts_Type())
slcAuthTACACSDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSDataPorts.setStatus(_A)
_SlcAuthTACACSClearPorts_Type=OctetString
_SlcAuthTACACSClearPorts_Object=MibScalar
slcAuthTACACSClearPorts=_SlcAuthTACACSClearPorts_Object((1,3,6,1,4,1,244,1,1,3,6,10),_SlcAuthTACACSClearPorts_Type())
slcAuthTACACSClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSClearPorts.setStatus(_A)
_SlcAuthTACACSServer2_Type=IpAddress
_SlcAuthTACACSServer2_Object=MibScalar
slcAuthTACACSServer2=_SlcAuthTACACSServer2_Object((1,3,6,1,4,1,244,1,1,3,6,11),_SlcAuthTACACSServer2_Type())
slcAuthTACACSServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSServer2.setStatus(_A)
_SlcAuthTACACSServer3_Type=IpAddress
_SlcAuthTACACSServer3_Object=MibScalar
slcAuthTACACSServer3=_SlcAuthTACACSServer3_Object((1,3,6,1,4,1,244,1,1,3,6,12),_SlcAuthTACACSServer3_Type())
slcAuthTACACSServer3.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSServer3.setStatus(_A)
_SlcAuthTACACSEscapeSeq_Type=OctetString
_SlcAuthTACACSEscapeSeq_Object=MibScalar
slcAuthTACACSEscapeSeq=_SlcAuthTACACSEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,6,13),_SlcAuthTACACSEscapeSeq_Type())
slcAuthTACACSEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSEscapeSeq.setStatus(_A)
_SlcAuthTACACSBreakSeq_Type=OctetString
_SlcAuthTACACSBreakSeq_Object=MibScalar
slcAuthTACACSBreakSeq=_SlcAuthTACACSBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,6,14),_SlcAuthTACACSBreakSeq_Type())
slcAuthTACACSBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSBreakSeq.setStatus(_A)
_SlcAuthTACACSDialback_Type=EnabledState
_SlcAuthTACACSDialback_Object=MibScalar
slcAuthTACACSDialback=_SlcAuthTACACSDialback_Object((1,3,6,1,4,1,244,1,1,3,6,15),_SlcAuthTACACSDialback_Type())
slcAuthTACACSDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSDialback.setStatus(_A)
_SlcAuthTACACSDialbackNum_Type=OctetString
_SlcAuthTACACSDialbackNum_Object=MibScalar
slcAuthTACACSDialbackNum=_SlcAuthTACACSDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,6,16),_SlcAuthTACACSDialbackNum_Type())
slcAuthTACACSDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSDialbackNum.setStatus(_A)
class _SlcAuthTACACSAuthService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pppPAP',1),('pppCHAP',2),('asciiLogin',3)))
_SlcAuthTACACSAuthService_Type.__name__=_C
_SlcAuthTACACSAuthService_Object=MibScalar
slcAuthTACACSAuthService=_SlcAuthTACACSAuthService_Object((1,3,6,1,4,1,244,1,1,3,6,17),_SlcAuthTACACSAuthService_Type())
slcAuthTACACSAuthService.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSAuthService.setStatus(_A)
_SlcAuthTACACSServerIPv6_Type=Ipv6Address
_SlcAuthTACACSServerIPv6_Object=MibScalar
slcAuthTACACSServerIPv6=_SlcAuthTACACSServerIPv6_Object((1,3,6,1,4,1,244,1,1,3,6,18),_SlcAuthTACACSServerIPv6_Type())
slcAuthTACACSServerIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSServerIPv6.setStatus(_A)
_SlcAuthTACACSServer2IPv6_Type=Ipv6Address
_SlcAuthTACACSServer2IPv6_Object=MibScalar
slcAuthTACACSServer2IPv6=_SlcAuthTACACSServer2IPv6_Object((1,3,6,1,4,1,244,1,1,3,6,19),_SlcAuthTACACSServer2IPv6_Type())
slcAuthTACACSServer2IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSServer2IPv6.setStatus(_A)
_SlcAuthTACACSServer3IPv6_Type=Ipv6Address
_SlcAuthTACACSServer3IPv6_Object=MibScalar
slcAuthTACACSServer3IPv6=_SlcAuthTACACSServer3IPv6_Object((1,3,6,1,4,1,244,1,1,3,6,20),_SlcAuthTACACSServer3IPv6_Type())
slcAuthTACACSServer3IPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthTACACSServer3IPv6.setStatus(_A)
_SlcAuthRemote_ObjectIdentity=ObjectIdentity
slcAuthRemote=_SlcAuthRemote_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,7))
class _SlcAuthRemoteNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_SlcAuthRemoteNumber_Type.__name__=_C
_SlcAuthRemoteNumber_Object=MibScalar
slcAuthRemoteNumber=_SlcAuthRemoteNumber_Object((1,3,6,1,4,1,244,1,1,3,7,1),_SlcAuthRemoteNumber_Type())
slcAuthRemoteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteNumber.setStatus(_A)
_SlcAuthRemoteUsersTable_Object=MibTable
slcAuthRemoteUsersTable=_SlcAuthRemoteUsersTable_Object((1,3,6,1,4,1,244,1,1,3,7,2))
if mibBuilder.loadTexts:slcAuthRemoteUsersTable.setStatus(_A)
_SlcAuthRemoteUserEntry_Object=MibTableRow
slcAuthRemoteUserEntry=_SlcAuthRemoteUserEntry_Object((1,3,6,1,4,1,244,1,1,3,7,2,1))
slcAuthRemoteUserEntry.setIndexNames((0,_D,_AG))
if mibBuilder.loadTexts:slcAuthRemoteUserEntry.setStatus(_A)
class _SlcAuthRemoteUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_SlcAuthRemoteUserIndex_Type.__name__=_C
_SlcAuthRemoteUserIndex_Object=MibTableColumn
slcAuthRemoteUserIndex=_SlcAuthRemoteUserIndex_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,1),_SlcAuthRemoteUserIndex_Type())
slcAuthRemoteUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserIndex.setStatus(_A)
class _SlcAuthRemoteUserLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SlcAuthRemoteUserLogin_Type.__name__=_F
_SlcAuthRemoteUserLogin_Object=MibTableColumn
slcAuthRemoteUserLogin=_SlcAuthRemoteUserLogin_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,2),_SlcAuthRemoteUserLogin_Type())
slcAuthRemoteUserLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserLogin.setStatus(_A)
_SlcAuthRemoteUserGroup_Type=UserGroup
_SlcAuthRemoteUserGroup_Object=MibTableColumn
slcAuthRemoteUserGroup=_SlcAuthRemoteUserGroup_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,3),_SlcAuthRemoteUserGroup_Type())
slcAuthRemoteUserGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserGroup.setStatus(_A)
_SlcAuthRemoteUserRights_Type=UserRights
_SlcAuthRemoteUserRights_Object=MibTableColumn
slcAuthRemoteUserRights=_SlcAuthRemoteUserRights_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,4),_SlcAuthRemoteUserRights_Type())
slcAuthRemoteUserRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserRights.setStatus(_A)
_SlcAuthRemoteUserListenPorts_Type=OctetString
_SlcAuthRemoteUserListenPorts_Object=MibTableColumn
slcAuthRemoteUserListenPorts=_SlcAuthRemoteUserListenPorts_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,5),_SlcAuthRemoteUserListenPorts_Type())
slcAuthRemoteUserListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserListenPorts.setStatus(_A)
_SlcAuthRemoteUserDataPorts_Type=OctetString
_SlcAuthRemoteUserDataPorts_Object=MibTableColumn
slcAuthRemoteUserDataPorts=_SlcAuthRemoteUserDataPorts_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,6),_SlcAuthRemoteUserDataPorts_Type())
slcAuthRemoteUserDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserDataPorts.setStatus(_A)
_SlcAuthRemoteUserClearPorts_Type=OctetString
_SlcAuthRemoteUserClearPorts_Object=MibTableColumn
slcAuthRemoteUserClearPorts=_SlcAuthRemoteUserClearPorts_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,7),_SlcAuthRemoteUserClearPorts_Type())
slcAuthRemoteUserClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserClearPorts.setStatus(_A)
_SlcAuthRemoteUserEscapeSeq_Type=OctetString
_SlcAuthRemoteUserEscapeSeq_Object=MibTableColumn
slcAuthRemoteUserEscapeSeq=_SlcAuthRemoteUserEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,8),_SlcAuthRemoteUserEscapeSeq_Type())
slcAuthRemoteUserEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserEscapeSeq.setStatus(_A)
_SlcAuthRemoteUserBreakSeq_Type=OctetString
_SlcAuthRemoteUserBreakSeq_Object=MibTableColumn
slcAuthRemoteUserBreakSeq=_SlcAuthRemoteUserBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,9),_SlcAuthRemoteUserBreakSeq_Type())
slcAuthRemoteUserBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserBreakSeq.setStatus(_A)
_SlcAuthRemoteUserMenu_Type=OctetString
_SlcAuthRemoteUserMenu_Object=MibTableColumn
slcAuthRemoteUserMenu=_SlcAuthRemoteUserMenu_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,10),_SlcAuthRemoteUserMenu_Type())
slcAuthRemoteUserMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserMenu.setStatus(_A)
_SlcAuthRemoteUserLocked_Type=EnabledState
_SlcAuthRemoteUserLocked_Object=MibTableColumn
slcAuthRemoteUserLocked=_SlcAuthRemoteUserLocked_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,11),_SlcAuthRemoteUserLocked_Type())
slcAuthRemoteUserLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserLocked.setStatus(_A)
_SlcAuthRemoteUserDialback_Type=EnabledState
_SlcAuthRemoteUserDialback_Object=MibTableColumn
slcAuthRemoteUserDialback=_SlcAuthRemoteUserDialback_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,12),_SlcAuthRemoteUserDialback_Type())
slcAuthRemoteUserDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserDialback.setStatus(_A)
_SlcAuthRemoteUserDialbackNum_Type=OctetString
_SlcAuthRemoteUserDialbackNum_Object=MibTableColumn
slcAuthRemoteUserDialbackNum=_SlcAuthRemoteUserDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,7,2,1,13),_SlcAuthRemoteUserDialbackNum_Type())
slcAuthRemoteUserDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteUserDialbackNum.setStatus(_A)
_SlcAuthRemoteAuthListOnly_Type=EnabledState
_SlcAuthRemoteAuthListOnly_Object=MibScalar
slcAuthRemoteAuthListOnly=_SlcAuthRemoteAuthListOnly_Object((1,3,6,1,4,1,244,1,1,3,7,3),_SlcAuthRemoteAuthListOnly_Type())
slcAuthRemoteAuthListOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthRemoteAuthListOnly.setStatus(_A)
_SlcAuthGroups_ObjectIdentity=ObjectIdentity
slcAuthGroups=_SlcAuthGroups_ObjectIdentity((1,3,6,1,4,1,244,1,1,3,8))
class _SlcAuthGroupsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_SlcAuthGroupsNumber_Type.__name__=_C
_SlcAuthGroupsNumber_Object=MibScalar
slcAuthGroupsNumber=_SlcAuthGroupsNumber_Object((1,3,6,1,4,1,244,1,1,3,8,1),_SlcAuthGroupsNumber_Type())
slcAuthGroupsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupsNumber.setStatus(_A)
_SlcAuthGroupsTable_Object=MibTable
slcAuthGroupsTable=_SlcAuthGroupsTable_Object((1,3,6,1,4,1,244,1,1,3,8,2))
if mibBuilder.loadTexts:slcAuthGroupsTable.setStatus(_A)
_SlcAuthGroupEntry_Object=MibTableRow
slcAuthGroupEntry=_SlcAuthGroupEntry_Object((1,3,6,1,4,1,244,1,1,3,8,2,1))
slcAuthGroupEntry.setIndexNames((0,_D,_AH))
if mibBuilder.loadTexts:slcAuthGroupEntry.setStatus(_A)
class _SlcAuthGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_SlcAuthGroupIndex_Type.__name__=_C
_SlcAuthGroupIndex_Object=MibTableColumn
slcAuthGroupIndex=_SlcAuthGroupIndex_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,1),_SlcAuthGroupIndex_Type())
slcAuthGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupIndex.setStatus(_A)
class _SlcAuthGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlcAuthGroupName_Type.__name__=_F
_SlcAuthGroupName_Object=MibTableColumn
slcAuthGroupName=_SlcAuthGroupName_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,2),_SlcAuthGroupName_Type())
slcAuthGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupName.setStatus(_A)
_SlcAuthGroupRights_Type=UserRights
_SlcAuthGroupRights_Object=MibTableColumn
slcAuthGroupRights=_SlcAuthGroupRights_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,3),_SlcAuthGroupRights_Type())
slcAuthGroupRights.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupRights.setStatus(_A)
_SlcAuthGroupListenPorts_Type=OctetString
_SlcAuthGroupListenPorts_Object=MibTableColumn
slcAuthGroupListenPorts=_SlcAuthGroupListenPorts_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,4),_SlcAuthGroupListenPorts_Type())
slcAuthGroupListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupListenPorts.setStatus(_A)
_SlcAuthGroupDataPorts_Type=OctetString
_SlcAuthGroupDataPorts_Object=MibTableColumn
slcAuthGroupDataPorts=_SlcAuthGroupDataPorts_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,5),_SlcAuthGroupDataPorts_Type())
slcAuthGroupDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupDataPorts.setStatus(_A)
_SlcAuthGroupClearPorts_Type=OctetString
_SlcAuthGroupClearPorts_Object=MibTableColumn
slcAuthGroupClearPorts=_SlcAuthGroupClearPorts_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,6),_SlcAuthGroupClearPorts_Type())
slcAuthGroupClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupClearPorts.setStatus(_A)
_SlcAuthGroupEscapeSeq_Type=OctetString
_SlcAuthGroupEscapeSeq_Object=MibTableColumn
slcAuthGroupEscapeSeq=_SlcAuthGroupEscapeSeq_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,7),_SlcAuthGroupEscapeSeq_Type())
slcAuthGroupEscapeSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupEscapeSeq.setStatus(_A)
_SlcAuthGroupBreakSeq_Type=OctetString
_SlcAuthGroupBreakSeq_Object=MibTableColumn
slcAuthGroupBreakSeq=_SlcAuthGroupBreakSeq_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,8),_SlcAuthGroupBreakSeq_Type())
slcAuthGroupBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupBreakSeq.setStatus(_A)
_SlcAuthGroupMenu_Type=OctetString
_SlcAuthGroupMenu_Object=MibTableColumn
slcAuthGroupMenu=_SlcAuthGroupMenu_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,9),_SlcAuthGroupMenu_Type())
slcAuthGroupMenu.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupMenu.setStatus(_A)
_SlcAuthGroupDialback_Type=EnabledState
_SlcAuthGroupDialback_Object=MibTableColumn
slcAuthGroupDialback=_SlcAuthGroupDialback_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,10),_SlcAuthGroupDialback_Type())
slcAuthGroupDialback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupDialback.setStatus(_A)
_SlcAuthGroupDialbackNum_Type=OctetString
_SlcAuthGroupDialbackNum_Object=MibTableColumn
slcAuthGroupDialbackNum=_SlcAuthGroupDialbackNum_Object((1,3,6,1,4,1,244,1,1,3,8,2,1,11),_SlcAuthGroupDialbackNum_Type())
slcAuthGroupDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcAuthGroupDialbackNum.setStatus(_A)
_SlcDevices_ObjectIdentity=ObjectIdentity
slcDevices=_SlcDevices_ObjectIdentity((1,3,6,1,4,1,244,1,1,4))
_SlcDevConsolePort_ObjectIdentity=ObjectIdentity
slcDevConsolePort=_SlcDevConsolePort_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,1))
class _SlcDevConBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,300),ValueRangeConstraint(600,600),ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200),ValueRangeConstraint(38400,38400),ValueRangeConstraint(57600,57600),ValueRangeConstraint(115200,115200))
_SlcDevConBaud_Type.__name__=_C
_SlcDevConBaud_Object=MibScalar
slcDevConBaud=_SlcDevConBaud_Object((1,3,6,1,4,1,244,1,1,4,1,1),_SlcDevConBaud_Type())
slcDevConBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConBaud.setStatus(_A)
class _SlcDevConDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,7),ValueRangeConstraint(8,8))
_SlcDevConDataBits_Type.__name__=_C
_SlcDevConDataBits_Object=MibScalar
slcDevConDataBits=_SlcDevConDataBits_Object((1,3,6,1,4,1,244,1,1,4,1,2),_SlcDevConDataBits_Type())
slcDevConDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConDataBits.setStatus(_A)
class _SlcDevConStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_SlcDevConStopBits_Type.__name__=_C
_SlcDevConStopBits_Object=MibScalar
slcDevConStopBits=_SlcDevConStopBits_Object((1,3,6,1,4,1,244,1,1,4,1,3),_SlcDevConStopBits_Type())
slcDevConStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConStopBits.setStatus(_A)
class _SlcDevConParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_R,3)))
_SlcDevConParity_Type.__name__=_C
_SlcDevConParity_Object=MibScalar
slcDevConParity=_SlcDevConParity_Object((1,3,6,1,4,1,244,1,1,4,1,4),_SlcDevConParity_Type())
slcDevConParity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConParity.setStatus(_A)
class _SlcDevConFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_S,2),(_T,3)))
_SlcDevConFlowControl_Type.__name__=_C
_SlcDevConFlowControl_Object=MibScalar
slcDevConFlowControl=_SlcDevConFlowControl_Object((1,3,6,1,4,1,244,1,1,4,1,5),_SlcDevConFlowControl_Type())
slcDevConFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConFlowControl.setStatus(_A)
class _SlcDevConTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcDevConTimeout_Type.__name__=_C
_SlcDevConTimeout_Object=MibScalar
slcDevConTimeout=_SlcDevConTimeout_Object((1,3,6,1,4,1,244,1,1,4,1,6),_SlcDevConTimeout_Type())
slcDevConTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevConTimeout.setUnits(_H)
_SlcDevConShowLines_Type=EnabledState
_SlcDevConShowLines_Object=MibScalar
slcDevConShowLines=_SlcDevConShowLines_Object((1,3,6,1,4,1,244,1,1,4,1,7),_SlcDevConShowLines_Type())
slcDevConShowLines.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConShowLines.setStatus(_A)
class _SlcDevConNumberShowLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SlcDevConNumberShowLines_Type.__name__=_C
_SlcDevConNumberShowLines_Object=MibScalar
slcDevConNumberShowLines=_SlcDevConNumberShowLines_Object((1,3,6,1,4,1,244,1,1,4,1,8),_SlcDevConNumberShowLines_Type())
slcDevConNumberShowLines.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConNumberShowLines.setStatus(_A)
_SlcDevConGroup_Type=OctetString
_SlcDevConGroup_Object=MibScalar
slcDevConGroup=_SlcDevConGroup_Object((1,3,6,1,4,1,244,1,1,4,1,9),_SlcDevConGroup_Type())
slcDevConGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevConGroup.setStatus(_A)
_SlcDevDevicePorts_ObjectIdentity=ObjectIdentity
slcDevDevicePorts=_SlcDevDevicePorts_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,2))
_SlcDevPortGlobal_ObjectIdentity=ObjectIdentity
slcDevPortGlobal=_SlcDevPortGlobal_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,2,1))
_SlcDevGlobalListenPorts_Type=OctetString
_SlcDevGlobalListenPorts_Object=MibScalar
slcDevGlobalListenPorts=_SlcDevGlobalListenPorts_Object((1,3,6,1,4,1,244,1,1,4,2,1,1),_SlcDevGlobalListenPorts_Type())
slcDevGlobalListenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalListenPorts.setStatus(_I)
_SlcDevGlobalDataPorts_Type=OctetString
_SlcDevGlobalDataPorts_Object=MibScalar
slcDevGlobalDataPorts=_SlcDevGlobalDataPorts_Object((1,3,6,1,4,1,244,1,1,4,2,1,2),_SlcDevGlobalDataPorts_Type())
slcDevGlobalDataPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalDataPorts.setStatus(_I)
_SlcDevGlobalClearPorts_Type=OctetString
_SlcDevGlobalClearPorts_Object=MibScalar
slcDevGlobalClearPorts=_SlcDevGlobalClearPorts_Object((1,3,6,1,4,1,244,1,1,4,2,1,3),_SlcDevGlobalClearPorts_Type())
slcDevGlobalClearPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalClearPorts.setStatus(_I)
class _SlcDevGlobalStartTelnetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcDevGlobalStartTelnetPort_Type.__name__=_C
_SlcDevGlobalStartTelnetPort_Object=MibScalar
slcDevGlobalStartTelnetPort=_SlcDevGlobalStartTelnetPort_Object((1,3,6,1,4,1,244,1,1,4,2,1,4),_SlcDevGlobalStartTelnetPort_Type())
slcDevGlobalStartTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalStartTelnetPort.setStatus(_A)
class _SlcDevGlobalStartSSHPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcDevGlobalStartSSHPort_Type.__name__=_C
_SlcDevGlobalStartSSHPort_Object=MibScalar
slcDevGlobalStartSSHPort=_SlcDevGlobalStartSSHPort_Object((1,3,6,1,4,1,244,1,1,4,2,1,5),_SlcDevGlobalStartSSHPort_Type())
slcDevGlobalStartSSHPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalStartSSHPort.setStatus(_A)
class _SlcDevGlobalStartTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SlcDevGlobalStartTCPPort_Type.__name__=_C
_SlcDevGlobalStartTCPPort_Object=MibScalar
slcDevGlobalStartTCPPort=_SlcDevGlobalStartTCPPort_Object((1,3,6,1,4,1,244,1,1,4,2,1,6),_SlcDevGlobalStartTCPPort_Type())
slcDevGlobalStartTCPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalStartTCPPort.setStatus(_A)
class _SlcDevGlobalMaxDirect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SlcDevGlobalMaxDirect_Type.__name__=_C
_SlcDevGlobalMaxDirect_Object=MibScalar
slcDevGlobalMaxDirect=_SlcDevGlobalMaxDirect_Object((1,3,6,1,4,1,244,1,1,4,2,1,7),_SlcDevGlobalMaxDirect_Type())
slcDevGlobalMaxDirect.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevGlobalMaxDirect.setStatus(_I)
_SlcDevPortConfig_ObjectIdentity=ObjectIdentity
slcDevPortConfig=_SlcDevPortConfig_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,2,2))
class _SlcDevPortCfgNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,8),ValueRangeConstraint(16,16),ValueRangeConstraint(24,24),ValueRangeConstraint(32,32),ValueRangeConstraint(40,40),ValueRangeConstraint(48,48))
_SlcDevPortCfgNumber_Type.__name__=_C
_SlcDevPortCfgNumber_Object=MibScalar
slcDevPortCfgNumber=_SlcDevPortCfgNumber_Object((1,3,6,1,4,1,244,1,1,4,2,2,1),_SlcDevPortCfgNumber_Type())
slcDevPortCfgNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNumber.setStatus(_A)
_SlcDevPortCfgTable_Object=MibTable
slcDevPortCfgTable=_SlcDevPortCfgTable_Object((1,3,6,1,4,1,244,1,1,4,2,2,2))
if mibBuilder.loadTexts:slcDevPortCfgTable.setStatus(_A)
_SlcDevPortCfgEntry_Object=MibTableRow
slcDevPortCfgEntry=_SlcDevPortCfgEntry_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1))
slcDevPortCfgEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:slcDevPortCfgEntry.setStatus(_A)
class _SlcDevPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_SlcDevPortId_Type.__name__=_C
_SlcDevPortId_Object=MibTableColumn
slcDevPortId=_SlcDevPortId_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,1),_SlcDevPortId_Type())
slcDevPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortId.setStatus(_A)
class _SlcDevPortCfgName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_SlcDevPortCfgName_Type.__name__=_F
_SlcDevPortCfgName_Object=MibTableColumn
slcDevPortCfgName=_SlcDevPortCfgName_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,2),_SlcDevPortCfgName_Type())
slcDevPortCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgName.setStatus(_A)
class _SlcDevPortCfgDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),('slp8',2),('slp16',3),('slp8Exp8',4),('slp8Exp16',5),('slp16Exp8',6),('slp16Exp16',7),('sensorsoft',8),('servertech',9),('rpm',10)))
_SlcDevPortCfgDevice_Type.__name__=_C
_SlcDevPortCfgDevice_Object=MibTableColumn
slcDevPortCfgDevice=_SlcDevPortCfgDevice_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,3),_SlcDevPortCfgDevice_Type())
slcDevPortCfgDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevice.setStatus(_A)
class _SlcDevPortCfgDevLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcDevPortCfgDevLogin_Type.__name__=_F
_SlcDevPortCfgDevLogin_Object=MibTableColumn
slcDevPortCfgDevLogin=_SlcDevPortCfgDevLogin_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,4),_SlcDevPortCfgDevLogin_Type())
slcDevPortCfgDevLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevLogin.setStatus(_A)
_SlcDevPortCfgBreakSeq_Type=OctetString
_SlcDevPortCfgBreakSeq_Object=MibTableColumn
slcDevPortCfgBreakSeq=_SlcDevPortCfgBreakSeq_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,5),_SlcDevPortCfgBreakSeq_Type())
slcDevPortCfgBreakSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgBreakSeq.setStatus(_A)
_SlcDevPortCfgTelnetState_Type=EnabledState
_SlcDevPortCfgTelnetState_Object=MibTableColumn
slcDevPortCfgTelnetState=_SlcDevPortCfgTelnetState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,6),_SlcDevPortCfgTelnetState_Type())
slcDevPortCfgTelnetState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTelnetState.setStatus(_A)
class _SlcDevPortCfgTelnetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcDevPortCfgTelnetPort_Type.__name__=_C
_SlcDevPortCfgTelnetPort_Object=MibTableColumn
slcDevPortCfgTelnetPort=_SlcDevPortCfgTelnetPort_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,7),_SlcDevPortCfgTelnetPort_Type())
slcDevPortCfgTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTelnetPort.setStatus(_A)
_SlcDevPortCfgTelnetAuth_Type=EnabledState
_SlcDevPortCfgTelnetAuth_Object=MibTableColumn
slcDevPortCfgTelnetAuth=_SlcDevPortCfgTelnetAuth_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,8),_SlcDevPortCfgTelnetAuth_Type())
slcDevPortCfgTelnetAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTelnetAuth.setStatus(_A)
_SlcDevPortCfgSSHState_Type=EnabledState
_SlcDevPortCfgSSHState_Object=MibTableColumn
slcDevPortCfgSSHState=_SlcDevPortCfgSSHState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,9),_SlcDevPortCfgSSHState_Type())
slcDevPortCfgSSHState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSSHState.setStatus(_A)
class _SlcDevPortCfgSSHPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcDevPortCfgSSHPort_Type.__name__=_C
_SlcDevPortCfgSSHPort_Object=MibTableColumn
slcDevPortCfgSSHPort=_SlcDevPortCfgSSHPort_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,10),_SlcDevPortCfgSSHPort_Type())
slcDevPortCfgSSHPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSSHPort.setStatus(_A)
_SlcDevPortCfgSSHAuth_Type=EnabledState
_SlcDevPortCfgSSHAuth_Object=MibTableColumn
slcDevPortCfgSSHAuth=_SlcDevPortCfgSSHAuth_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,11),_SlcDevPortCfgSSHAuth_Type())
slcDevPortCfgSSHAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSSHAuth.setStatus(_A)
_SlcDevPortCfgTCPState_Type=EnabledState
_SlcDevPortCfgTCPState_Object=MibTableColumn
slcDevPortCfgTCPState=_SlcDevPortCfgTCPState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,12),_SlcDevPortCfgTCPState_Type())
slcDevPortCfgTCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTCPState.setStatus(_A)
class _SlcDevPortCfgTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcDevPortCfgTCPPort_Type.__name__=_C
_SlcDevPortCfgTCPPort_Object=MibTableColumn
slcDevPortCfgTCPPort=_SlcDevPortCfgTCPPort_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,13),_SlcDevPortCfgTCPPort_Type())
slcDevPortCfgTCPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTCPPort.setStatus(_A)
_SlcDevPortCfgTCPAuth_Type=EnabledState
_SlcDevPortCfgTCPAuth_Object=MibTableColumn
slcDevPortCfgTCPAuth=_SlcDevPortCfgTCPAuth_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,14),_SlcDevPortCfgTCPAuth_Type())
slcDevPortCfgTCPAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTCPAuth.setStatus(_A)
_SlcDevPortCfgIP_Type=IpAddress
_SlcDevPortCfgIP_Object=MibTableColumn
slcDevPortCfgIP=_SlcDevPortCfgIP_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,15),_SlcDevPortCfgIP_Type())
slcDevPortCfgIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgIP.setStatus(_A)
class _SlcDevPortCfgBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,300),ValueRangeConstraint(600,600),ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200),ValueRangeConstraint(38400,38400),ValueRangeConstraint(57600,57600),ValueRangeConstraint(115200,115200))
_SlcDevPortCfgBaud_Type.__name__=_C
_SlcDevPortCfgBaud_Object=MibTableColumn
slcDevPortCfgBaud=_SlcDevPortCfgBaud_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,16),_SlcDevPortCfgBaud_Type())
slcDevPortCfgBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgBaud.setStatus(_A)
class _SlcDevPortCfgDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,7),ValueRangeConstraint(8,8))
_SlcDevPortCfgDataBits_Type.__name__=_C
_SlcDevPortCfgDataBits_Object=MibTableColumn
slcDevPortCfgDataBits=_SlcDevPortCfgDataBits_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,17),_SlcDevPortCfgDataBits_Type())
slcDevPortCfgDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDataBits.setStatus(_A)
class _SlcDevPortCfgStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_SlcDevPortCfgStopBits_Type.__name__=_C
_SlcDevPortCfgStopBits_Object=MibTableColumn
slcDevPortCfgStopBits=_SlcDevPortCfgStopBits_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,18),_SlcDevPortCfgStopBits_Type())
slcDevPortCfgStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgStopBits.setStatus(_A)
class _SlcDevPortCfgParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_R,3)))
_SlcDevPortCfgParity_Type.__name__=_C
_SlcDevPortCfgParity_Object=MibTableColumn
slcDevPortCfgParity=_SlcDevPortCfgParity_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,19),_SlcDevPortCfgParity_Type())
slcDevPortCfgParity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgParity.setStatus(_A)
class _SlcDevPortCfgFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_S,2),(_T,3)))
_SlcDevPortCfgFlowControl_Type.__name__=_C
_SlcDevPortCfgFlowControl_Object=MibTableColumn
slcDevPortCfgFlowControl=_SlcDevPortCfgFlowControl_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,20),_SlcDevPortCfgFlowControl_Type())
slcDevPortCfgFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgFlowControl.setStatus(_A)
_SlcDevPortCfgLogins_Type=EnabledState
_SlcDevPortCfgLogins_Object=MibTableColumn
slcDevPortCfgLogins=_SlcDevPortCfgLogins_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,21),_SlcDevPortCfgLogins_Type())
slcDevPortCfgLogins.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgLogins.setStatus(_A)
_SlcDevPortCfgConnectDSR_Type=EnabledState
_SlcDevPortCfgConnectDSR_Object=MibTableColumn
slcDevPortCfgConnectDSR=_SlcDevPortCfgConnectDSR_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,22),_SlcDevPortCfgConnectDSR_Type())
slcDevPortCfgConnectDSR.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgConnectDSR.setStatus(_A)
_SlcDevPortCfgDisconnectDSR_Type=EnabledState
_SlcDevPortCfgDisconnectDSR_Object=MibTableColumn
slcDevPortCfgDisconnectDSR=_SlcDevPortCfgDisconnectDSR_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,23),_SlcDevPortCfgDisconnectDSR_Type())
slcDevPortCfgDisconnectDSR.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDisconnectDSR.setStatus(_A)
class _SlcDevPortCfgModemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,1),(_U,2),(_V,3),(_W,4),(_o,5),(_p,6),(_q,7),(_r,8),(_s,9)))
_SlcDevPortCfgModemState_Type.__name__=_C
_SlcDevPortCfgModemState_Object=MibTableColumn
slcDevPortCfgModemState=_SlcDevPortCfgModemState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,24),_SlcDevPortCfgModemState_Type())
slcDevPortCfgModemState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgModemState.setStatus(_A)
class _SlcDevPortCfgModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_SlcDevPortCfgModemMode_Type.__name__=_C
_SlcDevPortCfgModemMode_Object=MibTableColumn
slcDevPortCfgModemMode=_SlcDevPortCfgModemMode_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,25),_SlcDevPortCfgModemMode_Type())
slcDevPortCfgModemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgModemMode.setStatus(_A)
_SlcDevPortCfgLocalIP_Type=IpAddress
_SlcDevPortCfgLocalIP_Object=MibTableColumn
slcDevPortCfgLocalIP=_SlcDevPortCfgLocalIP_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,26),_SlcDevPortCfgLocalIP_Type())
slcDevPortCfgLocalIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgLocalIP.setStatus(_A)
_SlcDevPortCfgRemoteIP_Type=IpAddress
_SlcDevPortCfgRemoteIP_Object=MibTableColumn
slcDevPortCfgRemoteIP=_SlcDevPortCfgRemoteIP_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,27),_SlcDevPortCfgRemoteIP_Type())
slcDevPortCfgRemoteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgRemoteIP.setStatus(_A)
class _SlcDevPortCfgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcDevPortCfgAuth_Type.__name__=_C
_SlcDevPortCfgAuth_Object=MibTableColumn
slcDevPortCfgAuth=_SlcDevPortCfgAuth_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,28),_SlcDevPortCfgAuth_Type())
slcDevPortCfgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgAuth.setStatus(_A)
_SlcDevPortCfgCHAPHost_Type=OctetString
_SlcDevPortCfgCHAPHost_Object=MibTableColumn
slcDevPortCfgCHAPHost=_SlcDevPortCfgCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,29),_SlcDevPortCfgCHAPHost_Type())
slcDevPortCfgCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgCHAPHost.setStatus(_A)
_SlcDevPortCfgInitScript_Type=OctetString
_SlcDevPortCfgInitScript_Object=MibTableColumn
slcDevPortCfgInitScript=_SlcDevPortCfgInitScript_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,30),_SlcDevPortCfgInitScript_Type())
slcDevPortCfgInitScript.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgInitScript.setStatus(_A)
class _SlcDevPortCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcDevPortCfgTimeout_Type.__name__=_C
_SlcDevPortCfgTimeout_Object=MibTableColumn
slcDevPortCfgTimeout=_SlcDevPortCfgTimeout_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,31),_SlcDevPortCfgTimeout_Type())
slcDevPortCfgTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgTimeout.setUnits(_H)
_SlcDevPortCfgDialoutNum_Type=OctetString
_SlcDevPortCfgDialoutNum_Object=MibTableColumn
slcDevPortCfgDialoutNum=_SlcDevPortCfgDialoutNum_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,32),_SlcDevPortCfgDialoutNum_Type())
slcDevPortCfgDialoutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDialoutNum.setStatus(_A)
class _SlcDevPortCfgDialoutLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcDevPortCfgDialoutLogin_Type.__name__=_F
_SlcDevPortCfgDialoutLogin_Object=MibTableColumn
slcDevPortCfgDialoutLogin=_SlcDevPortCfgDialoutLogin_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,33),_SlcDevPortCfgDialoutLogin_Type())
slcDevPortCfgDialoutLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDialoutLogin.setStatus(_A)
class _SlcDevPortCfgDialbackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_SlcDevPortCfgDialbackMode_Type.__name__=_C
_SlcDevPortCfgDialbackMode_Object=MibTableColumn
slcDevPortCfgDialbackMode=_SlcDevPortCfgDialbackMode_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,34),_SlcDevPortCfgDialbackMode_Type())
slcDevPortCfgDialbackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDialbackMode.setStatus(_A)
_SlcDevPortCfgDialbackNum_Type=OctetString
_SlcDevPortCfgDialbackNum_Object=MibTableColumn
slcDevPortCfgDialbackNum=_SlcDevPortCfgDialbackNum_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,35),_SlcDevPortCfgDialbackNum_Type())
slcDevPortCfgDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDialbackNum.setStatus(_A)
_SlcDevPortCfgNATState_Type=EnabledState
_SlcDevPortCfgNATState_Object=MibTableColumn
slcDevPortCfgNATState=_SlcDevPortCfgNATState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,36),_SlcDevPortCfgNATState_Type())
slcDevPortCfgNATState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNATState.setStatus(_A)
_SlcDevPortCfgLocalState_Type=EnabledState
_SlcDevPortCfgLocalState_Object=MibTableColumn
slcDevPortCfgLocalState=_SlcDevPortCfgLocalState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,37),_SlcDevPortCfgLocalState_Type())
slcDevPortCfgLocalState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgLocalState.setStatus(_A)
_SlcDevPortCfgNFSFileState_Type=EnabledState
_SlcDevPortCfgNFSFileState_Object=MibTableColumn
slcDevPortCfgNFSFileState=_SlcDevPortCfgNFSFileState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,38),_SlcDevPortCfgNFSFileState_Type())
slcDevPortCfgNFSFileState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNFSFileState.setStatus(_A)
_SlcDevPortCfgNFSDir_Type=OctetString
_SlcDevPortCfgNFSDir_Object=MibTableColumn
slcDevPortCfgNFSDir=_SlcDevPortCfgNFSDir_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,39),_SlcDevPortCfgNFSDir_Type())
slcDevPortCfgNFSDir.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNFSDir.setStatus(_A)
_SlcDevPortCfgNFSMaxFiles_Type=Integer32
_SlcDevPortCfgNFSMaxFiles_Object=MibTableColumn
slcDevPortCfgNFSMaxFiles=_SlcDevPortCfgNFSMaxFiles_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,40),_SlcDevPortCfgNFSMaxFiles_Type())
slcDevPortCfgNFSMaxFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNFSMaxFiles.setStatus(_A)
_SlcDevPortCfgNFSMaxSize_Type=Integer32
_SlcDevPortCfgNFSMaxSize_Object=MibTableColumn
slcDevPortCfgNFSMaxSize=_SlcDevPortCfgNFSMaxSize_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,41),_SlcDevPortCfgNFSMaxSize_Type())
slcDevPortCfgNFSMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNFSMaxSize.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgNFSMaxSize.setUnits(_P)
_SlcDevPortCfgEmailState_Type=EnabledState
_SlcDevPortCfgEmailState_Object=MibTableColumn
slcDevPortCfgEmailState=_SlcDevPortCfgEmailState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,42),_SlcDevPortCfgEmailState_Type())
slcDevPortCfgEmailState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailState.setStatus(_A)
class _SlcDevPortCfgEmailTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bytecnt',1),('textstring',2)))
_SlcDevPortCfgEmailTrigger_Type.__name__=_C
_SlcDevPortCfgEmailTrigger_Object=MibTableColumn
slcDevPortCfgEmailTrigger=_SlcDevPortCfgEmailTrigger_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,43),_SlcDevPortCfgEmailTrigger_Type())
slcDevPortCfgEmailTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailTrigger.setStatus(_A)
_SlcDevPortCfgEmailByteThresh_Type=Integer32
_SlcDevPortCfgEmailByteThresh_Object=MibTableColumn
slcDevPortCfgEmailByteThresh=_SlcDevPortCfgEmailByteThresh_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,44),_SlcDevPortCfgEmailByteThresh_Type())
slcDevPortCfgEmailByteThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailByteThresh.setStatus(_A)
_SlcDevPortCfgEmailDelay_Type=Integer32
_SlcDevPortCfgEmailDelay_Object=MibTableColumn
slcDevPortCfgEmailDelay=_SlcDevPortCfgEmailDelay_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,45),_SlcDevPortCfgEmailDelay_Type())
slcDevPortCfgEmailDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgEmailDelay.setUnits(_E)
_SlcDevPortCfgEmailRestartDelay_Type=Integer32
_SlcDevPortCfgEmailRestartDelay_Object=MibTableColumn
slcDevPortCfgEmailRestartDelay=_SlcDevPortCfgEmailRestartDelay_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,46),_SlcDevPortCfgEmailRestartDelay_Type())
slcDevPortCfgEmailRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgEmailRestartDelay.setUnits(_E)
_SlcDevPortCfgEmailTextString_Type=OctetString
_SlcDevPortCfgEmailTextString_Object=MibTableColumn
slcDevPortCfgEmailTextString=_SlcDevPortCfgEmailTextString_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,47),_SlcDevPortCfgEmailTextString_Type())
slcDevPortCfgEmailTextString.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailTextString.setStatus(_A)
_SlcDevPortCfgEmailTo_Type=OctetString
_SlcDevPortCfgEmailTo_Object=MibTableColumn
slcDevPortCfgEmailTo=_SlcDevPortCfgEmailTo_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,48),_SlcDevPortCfgEmailTo_Type())
slcDevPortCfgEmailTo.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailTo.setStatus(_A)
_SlcDevPortCfgEmailSubject_Type=OctetString
_SlcDevPortCfgEmailSubject_Object=MibTableColumn
slcDevPortCfgEmailSubject=_SlcDevPortCfgEmailSubject_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,49),_SlcDevPortCfgEmailSubject_Type())
slcDevPortCfgEmailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailSubject.setStatus(_A)
_SlcDevPortCfgPCCardState_Type=EnabledState
_SlcDevPortCfgPCCardState_Object=MibTableColumn
slcDevPortCfgPCCardState=_SlcDevPortCfgPCCardState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,50),_SlcDevPortCfgPCCardState_Type())
slcDevPortCfgPCCardState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPCCardState.setStatus(_A)
class _SlcDevPortCfgPCCardLogTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AI,1),(_AJ,2)))
_SlcDevPortCfgPCCardLogTo_Type.__name__=_C
_SlcDevPortCfgPCCardLogTo_Object=MibTableColumn
slcDevPortCfgPCCardLogTo=_SlcDevPortCfgPCCardLogTo_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,51),_SlcDevPortCfgPCCardLogTo_Type())
slcDevPortCfgPCCardLogTo.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPCCardLogTo.setStatus(_A)
_SlcDevPortCfgPCCardMaxFiles_Type=Integer32
_SlcDevPortCfgPCCardMaxFiles_Object=MibTableColumn
slcDevPortCfgPCCardMaxFiles=_SlcDevPortCfgPCCardMaxFiles_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,52),_SlcDevPortCfgPCCardMaxFiles_Type())
slcDevPortCfgPCCardMaxFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPCCardMaxFiles.setStatus(_A)
_SlcDevPortCfgPCCardMaxSize_Type=Integer32
_SlcDevPortCfgPCCardMaxSize_Object=MibTableColumn
slcDevPortCfgPCCardMaxSize=_SlcDevPortCfgPCCardMaxSize_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,53),_SlcDevPortCfgPCCardMaxSize_Type())
slcDevPortCfgPCCardMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPCCardMaxSize.setStatus(_A)
class _SlcDevPortCfgAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_t,1),('zeroPortCounters',2),('clearLocalLog',3),('terminateConnections',4)))
_SlcDevPortCfgAction_Type.__name__=_C
_SlcDevPortCfgAction_Object=MibTableColumn
slcDevPortCfgAction=_SlcDevPortCfgAction_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,54),_SlcDevPortCfgAction_Type())
slcDevPortCfgAction.setMaxAccess(_u)
if mibBuilder.loadTexts:slcDevPortCfgAction.setStatus(_A)
class _SlcDevPortCfgEmailSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('email',1),('snmptrap',2),('both',3)))
_SlcDevPortCfgEmailSend_Type.__name__=_C
_SlcDevPortCfgEmailSend_Object=MibTableColumn
slcDevPortCfgEmailSend=_SlcDevPortCfgEmailSend_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,55),_SlcDevPortCfgEmailSend_Type())
slcDevPortCfgEmailSend.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgEmailSend.setStatus(_A)
_SlcDevPortCfgBanner_Type=OctetString
_SlcDevPortCfgBanner_Object=MibTableColumn
slcDevPortCfgBanner=_SlcDevPortCfgBanner_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,56),_SlcDevPortCfgBanner_Type())
slcDevPortCfgBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgBanner.setStatus(_A)
_SlcDevPortCfgIdleTimeout_Type=Integer32
_SlcDevPortCfgIdleTimeout_Object=MibTableColumn
slcDevPortCfgIdleTimeout=_SlcDevPortCfgIdleTimeout_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,57),_SlcDevPortCfgIdleTimeout_Type())
slcDevPortCfgIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgIdleTimeout.setUnits(_E)
_SlcDevPortCfgRestartDelay_Type=Integer32
_SlcDevPortCfgRestartDelay_Object=MibTableColumn
slcDevPortCfgRestartDelay=_SlcDevPortCfgRestartDelay_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,58),_SlcDevPortCfgRestartDelay_Type())
slcDevPortCfgRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgRestartDelay.setUnits(_E)
_SlcDevPortCfgCallerIdLogging_Type=EnabledState
_SlcDevPortCfgCallerIdLogging_Object=MibTableColumn
slcDevPortCfgCallerIdLogging=_SlcDevPortCfgCallerIdLogging_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,59),_SlcDevPortCfgCallerIdLogging_Type())
slcDevPortCfgCallerIdLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgCallerIdLogging.setStatus(_A)
_SlcDevPortCfgCallerIdATCmd_Type=OctetString
_SlcDevPortCfgCallerIdATCmd_Object=MibTableColumn
slcDevPortCfgCallerIdATCmd=_SlcDevPortCfgCallerIdATCmd_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,60),_SlcDevPortCfgCallerIdATCmd_Type())
slcDevPortCfgCallerIdATCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgCallerIdATCmd.setStatus(_A)
class _SlcDevPortCfgDODAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcDevPortCfgDODAuth_Type.__name__=_C
_SlcDevPortCfgDODAuth_Object=MibTableColumn
slcDevPortCfgDODAuth=_SlcDevPortCfgDODAuth_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,61),_SlcDevPortCfgDODAuth_Type())
slcDevPortCfgDODAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDODAuth.setStatus(_A)
_SlcDevPortCfgDODCHAPHost_Type=OctetString
_SlcDevPortCfgDODCHAPHost_Object=MibTableColumn
slcDevPortCfgDODCHAPHost=_SlcDevPortCfgDODCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,62),_SlcDevPortCfgDODCHAPHost_Type())
slcDevPortCfgDODCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDODCHAPHost.setStatus(_A)
_SlcDevPortCfgSLMLoggingState_Type=EnabledState
_SlcDevPortCfgSLMLoggingState_Object=MibTableColumn
slcDevPortCfgSLMLoggingState=_SlcDevPortCfgSLMLoggingState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,63),_SlcDevPortCfgSLMLoggingState_Type())
slcDevPortCfgSLMLoggingState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSLMLoggingState.setStatus(_A)
_SlcDevPortCfgSLMNMS_Type=OctetString
_SlcDevPortCfgSLMNMS_Object=MibTableColumn
slcDevPortCfgSLMNMS=_SlcDevPortCfgSLMNMS_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,64),_SlcDevPortCfgSLMNMS_Type())
slcDevPortCfgSLMNMS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSLMNMS.setStatus(_A)
_SlcDevPortCfgSLMByteThresh_Type=Integer32
_SlcDevPortCfgSLMByteThresh_Object=MibTableColumn
slcDevPortCfgSLMByteThresh=_SlcDevPortCfgSLMByteThresh_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,65),_SlcDevPortCfgSLMByteThresh_Type())
slcDevPortCfgSLMByteThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSLMByteThresh.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgSLMByteThresh.setUnits(_P)
_SlcDevPortCfgSLMTimeFrame_Type=Integer32
_SlcDevPortCfgSLMTimeFrame_Object=MibTableColumn
slcDevPortCfgSLMTimeFrame=_SlcDevPortCfgSLMTimeFrame_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,66),_SlcDevPortCfgSLMTimeFrame_Type())
slcDevPortCfgSLMTimeFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSLMTimeFrame.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgSLMTimeFrame.setUnits(_E)
_SlcDevPortCfgWebColumns_Type=Integer32
_SlcDevPortCfgWebColumns_Object=MibTableColumn
slcDevPortCfgWebColumns=_SlcDevPortCfgWebColumns_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,67),_SlcDevPortCfgWebColumns_Type())
slcDevPortCfgWebColumns.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgWebColumns.setStatus(_A)
_SlcDevPortCfgWebRows_Type=Integer32
_SlcDevPortCfgWebRows_Object=MibTableColumn
slcDevPortCfgWebRows=_SlcDevPortCfgWebRows_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,68),_SlcDevPortCfgWebRows_Type())
slcDevPortCfgWebRows.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgWebRows.setStatus(_A)
_SlcDevPortCfgSyslogState_Type=EnabledState
_SlcDevPortCfgSyslogState_Object=MibTableColumn
slcDevPortCfgSyslogState=_SlcDevPortCfgSyslogState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,69),_SlcDevPortCfgSyslogState_Type())
slcDevPortCfgSyslogState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSyslogState.setStatus(_A)
_SlcDevPortCfgHostList_Type=OctetString
_SlcDevPortCfgHostList_Object=MibTableColumn
slcDevPortCfgHostList=_SlcDevPortCfgHostList_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,70),_SlcDevPortCfgHostList_Type())
slcDevPortCfgHostList.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgHostList.setStatus(_A)
_SlcDevPortCfgDevLowTemp_Type=Integer32
_SlcDevPortCfgDevLowTemp_Object=MibTableColumn
slcDevPortCfgDevLowTemp=_SlcDevPortCfgDevLowTemp_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,71),_SlcDevPortCfgDevLowTemp_Type())
slcDevPortCfgDevLowTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevLowTemp.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgDevLowTemp.setUnits(_K)
_SlcDevPortCfgDevHighTemp_Type=Integer32
_SlcDevPortCfgDevHighTemp_Object=MibTableColumn
slcDevPortCfgDevHighTemp=_SlcDevPortCfgDevHighTemp_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,72),_SlcDevPortCfgDevHighTemp_Type())
slcDevPortCfgDevHighTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevHighTemp.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgDevHighTemp.setUnits(_K)
_SlcDevPortCfgDevTemperature_Type=OctetString
_SlcDevPortCfgDevTemperature_Object=MibTableColumn
slcDevPortCfgDevTemperature=_SlcDevPortCfgDevTemperature_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,73),_SlcDevPortCfgDevTemperature_Type())
slcDevPortCfgDevTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevTemperature.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgDevTemperature.setUnits(_K)
_SlcDevPortCfgDevLowHumidity_Type=Integer32
_SlcDevPortCfgDevLowHumidity_Object=MibTableColumn
slcDevPortCfgDevLowHumidity=_SlcDevPortCfgDevLowHumidity_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,74),_SlcDevPortCfgDevLowHumidity_Type())
slcDevPortCfgDevLowHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevLowHumidity.setStatus(_A)
_SlcDevPortCfgDevHighHumidity_Type=Integer32
_SlcDevPortCfgDevHighHumidity_Object=MibTableColumn
slcDevPortCfgDevHighHumidity=_SlcDevPortCfgDevHighHumidity_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,75),_SlcDevPortCfgDevHighHumidity_Type())
slcDevPortCfgDevHighHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevHighHumidity.setStatus(_A)
_SlcDevPortCfgDevHumidity_Type=OctetString
_SlcDevPortCfgDevHumidity_Object=MibTableColumn
slcDevPortCfgDevHumidity=_SlcDevPortCfgDevHumidity_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,76),_SlcDevPortCfgDevHumidity_Type())
slcDevPortCfgDevHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevHumidity.setStatus(_A)
_SlcDevPortCfgDevTraps_Type=EnabledState
_SlcDevPortCfgDevTraps_Object=MibTableColumn
slcDevPortCfgDevTraps=_SlcDevPortCfgDevTraps_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,77),_SlcDevPortCfgDevTraps_Type())
slcDevPortCfgDevTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevTraps.setStatus(_A)
_SlcDevPortCfgShowLines_Type=EnabledState
_SlcDevPortCfgShowLines_Object=MibTableColumn
slcDevPortCfgShowLines=_SlcDevPortCfgShowLines_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,78),_SlcDevPortCfgShowLines_Type())
slcDevPortCfgShowLines.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgShowLines.setStatus(_A)
class _SlcDevPortCfgNumberShowLines_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_SlcDevPortCfgNumberShowLines_Type.__name__=_C
_SlcDevPortCfgNumberShowLines_Object=MibTableColumn
slcDevPortCfgNumberShowLines=_SlcDevPortCfgNumberShowLines_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,79),_SlcDevPortCfgNumberShowLines_Type())
slcDevPortCfgNumberShowLines.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNumberShowLines.setStatus(_A)
_SlcDevPortCfgViewPortLog_Type=EnabledState
_SlcDevPortCfgViewPortLog_Object=MibTableColumn
slcDevPortCfgViewPortLog=_SlcDevPortCfgViewPortLog_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,80),_SlcDevPortCfgViewPortLog_Type())
slcDevPortCfgViewPortLog.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgViewPortLog.setStatus(_A)
_SlcDevPortCfgPortLogSeq_Type=OctetString
_SlcDevPortCfgPortLogSeq_Object=MibTableColumn
slcDevPortCfgPortLogSeq=_SlcDevPortCfgPortLogSeq_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,81),_SlcDevPortCfgPortLogSeq_Type())
slcDevPortCfgPortLogSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPortLogSeq.setStatus(_A)
_SlcDevPortCfgMaxDirectConnects_Type=Integer32
_SlcDevPortCfgMaxDirectConnects_Object=MibTableColumn
slcDevPortCfgMaxDirectConnects=_SlcDevPortCfgMaxDirectConnects_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,82),_SlcDevPortCfgMaxDirectConnects_Type())
slcDevPortCfgMaxDirectConnects.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgMaxDirectConnects.setStatus(_A)
class _SlcDevPortCfgTelnetTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_SlcDevPortCfgTelnetTimeout_Type.__name__=_C
_SlcDevPortCfgTelnetTimeout_Object=MibTableColumn
slcDevPortCfgTelnetTimeout=_SlcDevPortCfgTelnetTimeout_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,83),_SlcDevPortCfgTelnetTimeout_Type())
slcDevPortCfgTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTelnetTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgTelnetTimeout.setUnits(_E)
class _SlcDevPortCfgSSHTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_SlcDevPortCfgSSHTimeout_Type.__name__=_C
_SlcDevPortCfgSSHTimeout_Object=MibTableColumn
slcDevPortCfgSSHTimeout=_SlcDevPortCfgSSHTimeout_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,84),_SlcDevPortCfgSSHTimeout_Type())
slcDevPortCfgSSHTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSSHTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgSSHTimeout.setUnits(_E)
class _SlcDevPortCfgTCPTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_SlcDevPortCfgTCPTimeout_Type.__name__=_C
_SlcDevPortCfgTCPTimeout_Object=MibTableColumn
slcDevPortCfgTCPTimeout=_SlcDevPortCfgTCPTimeout_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,85),_SlcDevPortCfgTCPTimeout_Type())
slcDevPortCfgTCPTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTCPTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgTCPTimeout.setUnits(_E)
class _SlcDevPortCfgCBCPClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_SlcDevPortCfgCBCPClientType_Type.__name__=_C
_SlcDevPortCfgCBCPClientType_Object=MibTableColumn
slcDevPortCfgCBCPClientType=_SlcDevPortCfgCBCPClientType_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,86),_SlcDevPortCfgCBCPClientType_Type())
slcDevPortCfgCBCPClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgCBCPClientType.setStatus(_A)
_SlcDevPortCfgCBCPServerAllowNoCallback_Type=EnabledState
_SlcDevPortCfgCBCPServerAllowNoCallback_Object=MibTableColumn
slcDevPortCfgCBCPServerAllowNoCallback=_SlcDevPortCfgCBCPServerAllowNoCallback_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,87),_SlcDevPortCfgCBCPServerAllowNoCallback_Type())
slcDevPortCfgCBCPServerAllowNoCallback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgCBCPServerAllowNoCallback.setStatus(_A)
_SlcDevPortCfgDialbackDelay_Type=Integer32
_SlcDevPortCfgDialbackDelay_Object=MibTableColumn
slcDevPortCfgDialbackDelay=_SlcDevPortCfgDialbackDelay_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,88),_SlcDevPortCfgDialbackDelay_Type())
slcDevPortCfgDialbackDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDialbackDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgDialbackDelay.setUnits(_E)
_SlcDevPortCfgUSBState_Type=EnabledState
_SlcDevPortCfgUSBState_Object=MibTableColumn
slcDevPortCfgUSBState=_SlcDevPortCfgUSBState_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,89),_SlcDevPortCfgUSBState_Type())
slcDevPortCfgUSBState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgUSBState.setStatus(_A)
_SlcDevPortCfgUSBLogTo_Type=Integer32
_SlcDevPortCfgUSBLogTo_Object=MibTableColumn
slcDevPortCfgUSBLogTo=_SlcDevPortCfgUSBLogTo_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,90),_SlcDevPortCfgUSBLogTo_Type())
slcDevPortCfgUSBLogTo.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgUSBLogTo.setStatus(_A)
_SlcDevPortCfgUSBMaxFiles_Type=Integer32
_SlcDevPortCfgUSBMaxFiles_Object=MibTableColumn
slcDevPortCfgUSBMaxFiles=_SlcDevPortCfgUSBMaxFiles_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,91),_SlcDevPortCfgUSBMaxFiles_Type())
slcDevPortCfgUSBMaxFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgUSBMaxFiles.setStatus(_A)
_SlcDevPortCfgUSBMaxSize_Type=Integer32
_SlcDevPortCfgUSBMaxSize_Object=MibTableColumn
slcDevPortCfgUSBMaxSize=_SlcDevPortCfgUSBMaxSize_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,92),_SlcDevPortCfgUSBMaxSize_Type())
slcDevPortCfgUSBMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgUSBMaxSize.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortCfgUSBMaxSize.setUnits(_P)
_SlcDevPortCfgCHAPAuthLocalUsers_Type=EnabledState
_SlcDevPortCfgCHAPAuthLocalUsers_Object=MibTableColumn
slcDevPortCfgCHAPAuthLocalUsers=_SlcDevPortCfgCHAPAuthLocalUsers_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,93),_SlcDevPortCfgCHAPAuthLocalUsers_Type())
slcDevPortCfgCHAPAuthLocalUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgCHAPAuthLocalUsers.setStatus(_A)
_SlcDevPortCfgUseSites_Type=EnabledState
_SlcDevPortCfgUseSites_Object=MibTableColumn
slcDevPortCfgUseSites=_SlcDevPortCfgUseSites_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,94),_SlcDevPortCfgUseSites_Type())
slcDevPortCfgUseSites.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgUseSites.setStatus(_A)
_SlcDevPortCfgDialbackRetries_Type=Integer32
_SlcDevPortCfgDialbackRetries_Object=MibTableColumn
slcDevPortCfgDialbackRetries=_SlcDevPortCfgDialbackRetries_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,95),_SlcDevPortCfgDialbackRetries_Type())
slcDevPortCfgDialbackRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDialbackRetries.setStatus(_A)
_SlcDevPortCfgGroup_Type=OctetString
_SlcDevPortCfgGroup_Object=MibTableColumn
slcDevPortCfgGroup=_SlcDevPortCfgGroup_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,96),_SlcDevPortCfgGroup_Type())
slcDevPortCfgGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgGroup.setStatus(_A)
_SlcDevPortCfgIPMask_Type=IpAddress
_SlcDevPortCfgIPMask_Object=MibTableColumn
slcDevPortCfgIPMask=_SlcDevPortCfgIPMask_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,97),_SlcDevPortCfgIPMask_Type())
slcDevPortCfgIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgIPMask.setStatus(_A)
_SlcDevPortCfgDevPrompt_Type=OctetString
_SlcDevPortCfgDevPrompt_Object=MibTableColumn
slcDevPortCfgDevPrompt=_SlcDevPortCfgDevPrompt_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,98),_SlcDevPortCfgDevPrompt_Type())
slcDevPortCfgDevPrompt.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevPrompt.setStatus(_A)
_SlcDevPortCfgDevNumOutlets_Type=Integer32
_SlcDevPortCfgDevNumOutlets_Object=MibTableColumn
slcDevPortCfgDevNumOutlets=_SlcDevPortCfgDevNumOutlets_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,99),_SlcDevPortCfgDevNumOutlets_Type())
slcDevPortCfgDevNumOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevNumOutlets.setStatus(_A)
_SlcDevPortCfgDevNumExpOutlets_Type=Integer32
_SlcDevPortCfgDevNumExpOutlets_Object=MibTableColumn
slcDevPortCfgDevNumExpOutlets=_SlcDevPortCfgDevNumExpOutlets_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,100),_SlcDevPortCfgDevNumExpOutlets_Type())
slcDevPortCfgDevNumExpOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgDevNumExpOutlets.setStatus(_A)
_SlcDevPortCfgReversePinout_Type=EnabledState
_SlcDevPortCfgReversePinout_Object=MibTableColumn
slcDevPortCfgReversePinout=_SlcDevPortCfgReversePinout_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,101),_SlcDevPortCfgReversePinout_Type())
slcDevPortCfgReversePinout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgReversePinout.setStatus(_A)
_SlcDevPortCfgUSBVBUS_Type=EnabledState
_SlcDevPortCfgUSBVBUS_Object=MibTableColumn
slcDevPortCfgUSBVBUS=_SlcDevPortCfgUSBVBUS_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,102),_SlcDevPortCfgUSBVBUS_Type())
slcDevPortCfgUSBVBUS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgUSBVBUS.setStatus(_A)
_SlcDevPortCfgAssertDTR_Type=EnabledState
_SlcDevPortCfgAssertDTR_Object=MibTableColumn
slcDevPortCfgAssertDTR=_SlcDevPortCfgAssertDTR_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,103),_SlcDevPortCfgAssertDTR_Type())
slcDevPortCfgAssertDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgAssertDTR.setStatus(_A)
class _SlcDevPortCfgPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rj45',1),('usb',2)))
_SlcDevPortCfgPortType_Type.__name__=_C
_SlcDevPortCfgPortType_Object=MibTableColumn
slcDevPortCfgPortType=_SlcDevPortCfgPortType_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,104),_SlcDevPortCfgPortType_Type())
slcDevPortCfgPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPortType.setStatus(_A)
_SlcDevPortCfgTelnetTimeoutDataDirection_Type=TimeoutDataDirection
_SlcDevPortCfgTelnetTimeoutDataDirection_Object=MibTableColumn
slcDevPortCfgTelnetTimeoutDataDirection=_SlcDevPortCfgTelnetTimeoutDataDirection_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,105),_SlcDevPortCfgTelnetTimeoutDataDirection_Type())
slcDevPortCfgTelnetTimeoutDataDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTelnetTimeoutDataDirection.setStatus(_A)
_SlcDevPortCfgSSHTimeoutDataDirection_Type=TimeoutDataDirection
_SlcDevPortCfgSSHTimeoutDataDirection_Object=MibTableColumn
slcDevPortCfgSSHTimeoutDataDirection=_SlcDevPortCfgSSHTimeoutDataDirection_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,106),_SlcDevPortCfgSSHTimeoutDataDirection_Type())
slcDevPortCfgSSHTimeoutDataDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSSHTimeoutDataDirection.setStatus(_A)
_SlcDevPortCfgTCPTimeoutDataDirection_Type=TimeoutDataDirection
_SlcDevPortCfgTCPTimeoutDataDirection_Object=MibTableColumn
slcDevPortCfgTCPTimeoutDataDirection=_SlcDevPortCfgTCPTimeoutDataDirection_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,107),_SlcDevPortCfgTCPTimeoutDataDirection_Type())
slcDevPortCfgTCPTimeoutDataDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTCPTimeoutDataDirection.setStatus(_A)
_SlcDevPortCfgIdleTimeoutMessage_Type=EnabledState
_SlcDevPortCfgIdleTimeoutMessage_Object=MibTableColumn
slcDevPortCfgIdleTimeoutMessage=_SlcDevPortCfgIdleTimeoutMessage_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,108),_SlcDevPortCfgIdleTimeoutMessage_Type())
slcDevPortCfgIdleTimeoutMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgIdleTimeoutMessage.setStatus(_A)
_SlcDevPortCfgNumberOfSessionsMessage_Type=EnabledState
_SlcDevPortCfgNumberOfSessionsMessage_Object=MibTableColumn
slcDevPortCfgNumberOfSessionsMessage=_SlcDevPortCfgNumberOfSessionsMessage_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,109),_SlcDevPortCfgNumberOfSessionsMessage_Type())
slcDevPortCfgNumberOfSessionsMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgNumberOfSessionsMessage.setStatus(_A)
_SlcDevPortCfgMinimizeLatency_Type=EnabledState
_SlcDevPortCfgMinimizeLatency_Object=MibTableColumn
slcDevPortCfgMinimizeLatency=_SlcDevPortCfgMinimizeLatency_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,110),_SlcDevPortCfgMinimizeLatency_Type())
slcDevPortCfgMinimizeLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgMinimizeLatency.setStatus(_A)
_SlcDevPortCfgTelnetSoftIAC_Type=EnabledState
_SlcDevPortCfgTelnetSoftIAC_Object=MibTableColumn
slcDevPortCfgTelnetSoftIAC=_SlcDevPortCfgTelnetSoftIAC_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,111),_SlcDevPortCfgTelnetSoftIAC_Type())
slcDevPortCfgTelnetSoftIAC.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTelnetSoftIAC.setStatus(_A)
_SlcDevPortCfgSendTermString_Type=EnabledState
_SlcDevPortCfgSendTermString_Object=MibTableColumn
slcDevPortCfgSendTermString=_SlcDevPortCfgSendTermString_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,112),_SlcDevPortCfgSendTermString_Type())
slcDevPortCfgSendTermString.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgSendTermString.setStatus(_A)
_SlcDevPortCfgTerminationString_Type=OctetString
_SlcDevPortCfgTerminationString_Object=MibTableColumn
slcDevPortCfgTerminationString=_SlcDevPortCfgTerminationString_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,113),_SlcDevPortCfgTerminationString_Type())
slcDevPortCfgTerminationString.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTerminationString.setStatus(_A)
_SlcDevPortCfgPowerManagementSeq_Type=OctetString
_SlcDevPortCfgPowerManagementSeq_Object=MibTableColumn
slcDevPortCfgPowerManagementSeq=_SlcDevPortCfgPowerManagementSeq_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,114),_SlcDevPortCfgPowerManagementSeq_Type())
slcDevPortCfgPowerManagementSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPowerManagementSeq.setStatus(_A)
_SlcDevPortCfgPowerSupplies_Type=OctetString
_SlcDevPortCfgPowerSupplies_Object=MibTableColumn
slcDevPortCfgPowerSupplies=_SlcDevPortCfgPowerSupplies_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,115),_SlcDevPortCfgPowerSupplies_Type())
slcDevPortCfgPowerSupplies.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgPowerSupplies.setStatus(_A)
_SlcDevPortCfgToggleDTR_Type=EnabledState
_SlcDevPortCfgToggleDTR_Object=MibTableColumn
slcDevPortCfgToggleDTR=_SlcDevPortCfgToggleDTR_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,116),_SlcDevPortCfgToggleDTR_Type())
slcDevPortCfgToggleDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgToggleDTR.setStatus(_A)
_SlcDevPortCfgTokenAction_Type=OctetString
_SlcDevPortCfgTokenAction_Object=MibTableColumn
slcDevPortCfgTokenAction=_SlcDevPortCfgTokenAction_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,117),_SlcDevPortCfgTokenAction_Type())
slcDevPortCfgTokenAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTokenAction.setStatus(_A)
_SlcDevPortCfgTokenSendString_Type=OctetString
_SlcDevPortCfgTokenSendString_Object=MibTableColumn
slcDevPortCfgTokenSendString=_SlcDevPortCfgTokenSendString_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,118),_SlcDevPortCfgTokenSendString_Type())
slcDevPortCfgTokenSendString.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTokenSendString.setStatus(_A)
_SlcDevPortCfgTokenPowerSupply_Type=OctetString
_SlcDevPortCfgTokenPowerSupply_Object=MibTableColumn
slcDevPortCfgTokenPowerSupply=_SlcDevPortCfgTokenPowerSupply_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,119),_SlcDevPortCfgTokenPowerSupply_Type())
slcDevPortCfgTokenPowerSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTokenPowerSupply.setStatus(_A)
class _SlcDevPortCfgTokenPowerAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('turnOff',1),('turnOn',2),(_AK,3)))
_SlcDevPortCfgTokenPowerAction_Type.__name__=_C
_SlcDevPortCfgTokenPowerAction_Object=MibTableColumn
slcDevPortCfgTokenPowerAction=_SlcDevPortCfgTokenPowerAction_Object((1,3,6,1,4,1,244,1,1,4,2,2,2,1,120),_SlcDevPortCfgTokenPowerAction_Type())
slcDevPortCfgTokenPowerAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortCfgTokenPowerAction.setStatus(_A)
_SlcDevPortState_ObjectIdentity=ObjectIdentity
slcDevPortState=_SlcDevPortState_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,2,3))
class _SlcDevPortStateNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,8),ValueRangeConstraint(16,16),ValueRangeConstraint(24,24),ValueRangeConstraint(32,32),ValueRangeConstraint(40,40),ValueRangeConstraint(48,48))
_SlcDevPortStateNumber_Type.__name__=_C
_SlcDevPortStateNumber_Object=MibScalar
slcDevPortStateNumber=_SlcDevPortStateNumber_Object((1,3,6,1,4,1,244,1,1,4,2,3,1),_SlcDevPortStateNumber_Type())
slcDevPortStateNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateNumber.setStatus(_A)
_SlcDevPortStateTable_Object=MibTable
slcDevPortStateTable=_SlcDevPortStateTable_Object((1,3,6,1,4,1,244,1,1,4,2,3,2))
if mibBuilder.loadTexts:slcDevPortStateTable.setStatus(_A)
_SlcDevPortStateEntry_Object=MibTableRow
slcDevPortStateEntry=_SlcDevPortStateEntry_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1))
slcDevPortStateEntry.setIndexNames((0,_D,_AL))
if mibBuilder.loadTexts:slcDevPortStateEntry.setStatus(_A)
class _SlcDevPortStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_SlcDevPortStateIndex_Type.__name__=_C
_SlcDevPortStateIndex_Object=MibTableColumn
slcDevPortStateIndex=_SlcDevPortStateIndex_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,1),_SlcDevPortStateIndex_Type())
slcDevPortStateIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateIndex.setStatus(_A)
_SlcDevPortStateBytesInput_Type=Integer32
_SlcDevPortStateBytesInput_Object=MibTableColumn
slcDevPortStateBytesInput=_SlcDevPortStateBytesInput_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,2),_SlcDevPortStateBytesInput_Type())
slcDevPortStateBytesInput.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateBytesInput.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortStateBytesInput.setUnits(_P)
_SlcDevPortStateBytesOutput_Type=Integer32
_SlcDevPortStateBytesOutput_Object=MibTableColumn
slcDevPortStateBytesOutput=_SlcDevPortStateBytesOutput_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,3),_SlcDevPortStateBytesOutput_Type())
slcDevPortStateBytesOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateBytesOutput.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortStateBytesOutput.setUnits(_P)
_SlcDevPortStateFramingErrors_Type=Integer32
_SlcDevPortStateFramingErrors_Object=MibTableColumn
slcDevPortStateFramingErrors=_SlcDevPortStateFramingErrors_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,4),_SlcDevPortStateFramingErrors_Type())
slcDevPortStateFramingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateFramingErrors.setStatus(_A)
_SlcDevPortStateParityErrors_Type=Integer32
_SlcDevPortStateParityErrors_Object=MibTableColumn
slcDevPortStateParityErrors=_SlcDevPortStateParityErrors_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,5),_SlcDevPortStateParityErrors_Type())
slcDevPortStateParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateParityErrors.setStatus(_A)
_SlcDevPortStateOverrunErrors_Type=Integer32
_SlcDevPortStateOverrunErrors_Object=MibTableColumn
slcDevPortStateOverrunErrors=_SlcDevPortStateOverrunErrors_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,6),_SlcDevPortStateOverrunErrors_Type())
slcDevPortStateOverrunErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateOverrunErrors.setStatus(_A)
_SlcDevPortStateFlowControlViolations_Type=Integer32
_SlcDevPortStateFlowControlViolations_Object=MibTableColumn
slcDevPortStateFlowControlViolations=_SlcDevPortStateFlowControlViolations_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,7),_SlcDevPortStateFlowControlViolations_Type())
slcDevPortStateFlowControlViolations.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateFlowControlViolations.setStatus(_A)
_SlcDevPortStateDSR_Type=EnabledState
_SlcDevPortStateDSR_Object=MibTableColumn
slcDevPortStateDSR=_SlcDevPortStateDSR_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,8),_SlcDevPortStateDSR_Type())
slcDevPortStateDSR.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateDSR.setStatus(_A)
_SlcDevPortStateDTR_Type=EnabledState
_SlcDevPortStateDTR_Object=MibTableColumn
slcDevPortStateDTR=_SlcDevPortStateDTR_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,9),_SlcDevPortStateDTR_Type())
slcDevPortStateDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateDTR.setStatus(_A)
_SlcDevPortStateCTS_Type=EnabledState
_SlcDevPortStateCTS_Object=MibTableColumn
slcDevPortStateCTS=_SlcDevPortStateCTS_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,10),_SlcDevPortStateCTS_Type())
slcDevPortStateCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateCTS.setStatus(_A)
_SlcDevPortStateRTS_Type=EnabledState
_SlcDevPortStateRTS_Object=MibTableColumn
slcDevPortStateRTS=_SlcDevPortStateRTS_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,11),_SlcDevPortStateRTS_Type())
slcDevPortStateRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateRTS.setStatus(_A)
_SlcDevPortStateCD_Type=EnabledState
_SlcDevPortStateCD_Object=MibTableColumn
slcDevPortStateCD=_SlcDevPortStateCD_Object((1,3,6,1,4,1,244,1,1,4,2,3,2,1,12),_SlcDevPortStateCD_Type())
slcDevPortStateCD.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStateCD.setStatus(_A)
_SlcDevPCCard_ObjectIdentity=ObjectIdentity
slcDevPCCard=_SlcDevPCCard_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,3))
_SlcPCCardCfgTable_Object=MibTable
slcPCCardCfgTable=_SlcPCCardCfgTable_Object((1,3,6,1,4,1,244,1,1,4,3,1))
if mibBuilder.loadTexts:slcPCCardCfgTable.setStatus(_A)
_SlcPCCardCfgEntry_Object=MibTableRow
slcPCCardCfgEntry=_SlcPCCardCfgEntry_Object((1,3,6,1,4,1,244,1,1,4,3,1,1))
slcPCCardCfgEntry.setIndexNames((0,_D,_AM))
if mibBuilder.loadTexts:slcPCCardCfgEntry.setStatus(_A)
class _SlcPCCardCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SlcPCCardCfgIndex_Type.__name__=_C
_SlcPCCardCfgIndex_Object=MibTableColumn
slcPCCardCfgIndex=_SlcPCCardCfgIndex_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,1),_SlcPCCardCfgIndex_Type())
slcPCCardCfgIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgIndex.setStatus(_A)
class _SlcPCCardCfgCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6)))
_SlcPCCardCfgCardType_Type.__name__=_C
_SlcPCCardCfgCardType_Object=MibTableColumn
slcPCCardCfgCardType=_SlcPCCardCfgCardType_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,2),_SlcPCCardCfgCardType_Type())
slcPCCardCfgCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCardType.setStatus(_A)
_SlcPCCardCfgCardId_Type=OctetString
_SlcPCCardCfgCardId_Object=MibTableColumn
slcPCCardCfgCardId=_SlcPCCardCfgCardId_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,3),_SlcPCCardCfgCardId_Type())
slcPCCardCfgCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCardId.setStatus(_A)
class _SlcPCCardCfgBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,300),ValueRangeConstraint(600,600),ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200),ValueRangeConstraint(38400,38400),ValueRangeConstraint(57600,57600),ValueRangeConstraint(115200,115200))
_SlcPCCardCfgBaud_Type.__name__=_C
_SlcPCCardCfgBaud_Object=MibTableColumn
slcPCCardCfgBaud=_SlcPCCardCfgBaud_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,4),_SlcPCCardCfgBaud_Type())
slcPCCardCfgBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgBaud.setStatus(_A)
class _SlcPCCardCfgDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,7),ValueRangeConstraint(8,8))
_SlcPCCardCfgDataBits_Type.__name__=_C
_SlcPCCardCfgDataBits_Object=MibTableColumn
slcPCCardCfgDataBits=_SlcPCCardCfgDataBits_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,5),_SlcPCCardCfgDataBits_Type())
slcPCCardCfgDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDataBits.setStatus(_A)
class _SlcPCCardCfgStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_SlcPCCardCfgStopBits_Type.__name__=_C
_SlcPCCardCfgStopBits_Object=MibTableColumn
slcPCCardCfgStopBits=_SlcPCCardCfgStopBits_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,6),_SlcPCCardCfgStopBits_Type())
slcPCCardCfgStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgStopBits.setStatus(_A)
class _SlcPCCardCfgParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_R,3)))
_SlcPCCardCfgParity_Type.__name__=_C
_SlcPCCardCfgParity_Object=MibTableColumn
slcPCCardCfgParity=_SlcPCCardCfgParity_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,7),_SlcPCCardCfgParity_Type())
slcPCCardCfgParity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgParity.setStatus(_A)
class _SlcPCCardCfgFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_S,2),(_T,3)))
_SlcPCCardCfgFlowControl_Type.__name__=_C
_SlcPCCardCfgFlowControl_Object=MibTableColumn
slcPCCardCfgFlowControl=_SlcPCCardCfgFlowControl_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,8),_SlcPCCardCfgFlowControl_Type())
slcPCCardCfgFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgFlowControl.setStatus(_A)
class _SlcPCCardCfgModemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,1),(_U,2),(_V,3),(_W,4),(_o,5),(_p,6),(_q,7),(_r,8),(_s,9)))
_SlcPCCardCfgModemState_Type.__name__=_C
_SlcPCCardCfgModemState_Object=MibTableColumn
slcPCCardCfgModemState=_SlcPCCardCfgModemState_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,9),_SlcPCCardCfgModemState_Type())
slcPCCardCfgModemState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgModemState.setStatus(_A)
class _SlcPCCardCfgModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_SlcPCCardCfgModemMode_Type.__name__=_C
_SlcPCCardCfgModemMode_Object=MibTableColumn
slcPCCardCfgModemMode=_SlcPCCardCfgModemMode_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,10),_SlcPCCardCfgModemMode_Type())
slcPCCardCfgModemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgModemMode.setStatus(_A)
_SlcPCCardCfgLocalIP_Type=IpAddress
_SlcPCCardCfgLocalIP_Object=MibTableColumn
slcPCCardCfgLocalIP=_SlcPCCardCfgLocalIP_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,11),_SlcPCCardCfgLocalIP_Type())
slcPCCardCfgLocalIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgLocalIP.setStatus(_A)
_SlcPCCardCfgRemoteIP_Type=IpAddress
_SlcPCCardCfgRemoteIP_Object=MibTableColumn
slcPCCardCfgRemoteIP=_SlcPCCardCfgRemoteIP_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,12),_SlcPCCardCfgRemoteIP_Type())
slcPCCardCfgRemoteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgRemoteIP.setStatus(_A)
class _SlcPCCardCfgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcPCCardCfgAuth_Type.__name__=_C
_SlcPCCardCfgAuth_Object=MibTableColumn
slcPCCardCfgAuth=_SlcPCCardCfgAuth_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,13),_SlcPCCardCfgAuth_Type())
slcPCCardCfgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgAuth.setStatus(_A)
_SlcPCCardCfgCHAPHost_Type=OctetString
_SlcPCCardCfgCHAPHost_Object=MibTableColumn
slcPCCardCfgCHAPHost=_SlcPCCardCfgCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,14),_SlcPCCardCfgCHAPHost_Type())
slcPCCardCfgCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCHAPHost.setStatus(_A)
_SlcPCCardCfgInitScript_Type=OctetString
_SlcPCCardCfgInitScript_Object=MibTableColumn
slcPCCardCfgInitScript=_SlcPCCardCfgInitScript_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,15),_SlcPCCardCfgInitScript_Type())
slcPCCardCfgInitScript.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgInitScript.setStatus(_A)
class _SlcPCCardCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcPCCardCfgTimeout_Type.__name__=_C
_SlcPCCardCfgTimeout_Object=MibTableColumn
slcPCCardCfgTimeout=_SlcPCCardCfgTimeout_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,16),_SlcPCCardCfgTimeout_Type())
slcPCCardCfgTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcPCCardCfgTimeout.setUnits(_H)
_SlcPCCardCfgDialoutNum_Type=OctetString
_SlcPCCardCfgDialoutNum_Object=MibTableColumn
slcPCCardCfgDialoutNum=_SlcPCCardCfgDialoutNum_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,17),_SlcPCCardCfgDialoutNum_Type())
slcPCCardCfgDialoutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDialoutNum.setStatus(_A)
class _SlcPCCardCfgDialoutLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcPCCardCfgDialoutLogin_Type.__name__=_F
_SlcPCCardCfgDialoutLogin_Object=MibTableColumn
slcPCCardCfgDialoutLogin=_SlcPCCardCfgDialoutLogin_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,18),_SlcPCCardCfgDialoutLogin_Type())
slcPCCardCfgDialoutLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDialoutLogin.setStatus(_A)
class _SlcPCCardCfgDialbackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_SlcPCCardCfgDialbackMode_Type.__name__=_C
_SlcPCCardCfgDialbackMode_Object=MibTableColumn
slcPCCardCfgDialbackMode=_SlcPCCardCfgDialbackMode_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,19),_SlcPCCardCfgDialbackMode_Type())
slcPCCardCfgDialbackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDialbackMode.setStatus(_A)
_SlcPCCardCfgDialbackNum_Type=OctetString
_SlcPCCardCfgDialbackNum_Object=MibTableColumn
slcPCCardCfgDialbackNum=_SlcPCCardCfgDialbackNum_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,20),_SlcPCCardCfgDialbackNum_Type())
slcPCCardCfgDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDialbackNum.setStatus(_A)
_SlcPCCardCfgNATState_Type=EnabledState
_SlcPCCardCfgNATState_Object=MibTableColumn
slcPCCardCfgNATState=_SlcPCCardCfgNATState_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,21),_SlcPCCardCfgNATState_Type())
slcPCCardCfgNATState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgNATState.setStatus(_A)
class _SlcPCCardCfgStorageFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AN,1),('ext2',2),('fat',3)))
_SlcPCCardCfgStorageFS_Type.__name__=_C
_SlcPCCardCfgStorageFS_Object=MibTableColumn
slcPCCardCfgStorageFS=_SlcPCCardCfgStorageFS_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,22),_SlcPCCardCfgStorageFS_Type())
slcPCCardCfgStorageFS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgStorageFS.setStatus(_A)
_SlcPCCardCfgISDNChannel_Type=Integer32
_SlcPCCardCfgISDNChannel_Object=MibTableColumn
slcPCCardCfgISDNChannel=_SlcPCCardCfgISDNChannel_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,23),_SlcPCCardCfgISDNChannel_Type())
slcPCCardCfgISDNChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgISDNChannel.setStatus(_A)
_SlcPCCardCfgISDNChannelNum_Type=OctetString
_SlcPCCardCfgISDNChannelNum_Object=MibTableColumn
slcPCCardCfgISDNChannelNum=_SlcPCCardCfgISDNChannelNum_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,24),_SlcPCCardCfgISDNChannelNum_Type())
slcPCCardCfgISDNChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgISDNChannelNum.setStatus(_A)
_SlcPCCardCfgTelnetState_Type=EnabledState
_SlcPCCardCfgTelnetState_Object=MibTableColumn
slcPCCardCfgTelnetState=_SlcPCCardCfgTelnetState_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,25),_SlcPCCardCfgTelnetState_Type())
slcPCCardCfgTelnetState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTelnetState.setStatus(_A)
class _SlcPCCardCfgTelnetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcPCCardCfgTelnetPort_Type.__name__=_C
_SlcPCCardCfgTelnetPort_Object=MibTableColumn
slcPCCardCfgTelnetPort=_SlcPCCardCfgTelnetPort_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,26),_SlcPCCardCfgTelnetPort_Type())
slcPCCardCfgTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTelnetPort.setStatus(_A)
_SlcPCCardCfgTelnetAuth_Type=EnabledState
_SlcPCCardCfgTelnetAuth_Object=MibTableColumn
slcPCCardCfgTelnetAuth=_SlcPCCardCfgTelnetAuth_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,27),_SlcPCCardCfgTelnetAuth_Type())
slcPCCardCfgTelnetAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTelnetAuth.setStatus(_A)
_SlcPCCardCfgSSHState_Type=EnabledState
_SlcPCCardCfgSSHState_Object=MibTableColumn
slcPCCardCfgSSHState=_SlcPCCardCfgSSHState_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,28),_SlcPCCardCfgSSHState_Type())
slcPCCardCfgSSHState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgSSHState.setStatus(_A)
class _SlcPCCardCfgSSHPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcPCCardCfgSSHPort_Type.__name__=_C
_SlcPCCardCfgSSHPort_Object=MibTableColumn
slcPCCardCfgSSHPort=_SlcPCCardCfgSSHPort_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,29),_SlcPCCardCfgSSHPort_Type())
slcPCCardCfgSSHPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgSSHPort.setStatus(_A)
_SlcPCCardCfgSSHAuth_Type=EnabledState
_SlcPCCardCfgSSHAuth_Object=MibTableColumn
slcPCCardCfgSSHAuth=_SlcPCCardCfgSSHAuth_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,30),_SlcPCCardCfgSSHAuth_Type())
slcPCCardCfgSSHAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgSSHAuth.setStatus(_A)
_SlcPCCardCfgTCPState_Type=EnabledState
_SlcPCCardCfgTCPState_Object=MibTableColumn
slcPCCardCfgTCPState=_SlcPCCardCfgTCPState_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,31),_SlcPCCardCfgTCPState_Type())
slcPCCardCfgTCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTCPState.setStatus(_A)
class _SlcPCCardCfgTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcPCCardCfgTCPPort_Type.__name__=_C
_SlcPCCardCfgTCPPort_Object=MibTableColumn
slcPCCardCfgTCPPort=_SlcPCCardCfgTCPPort_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,32),_SlcPCCardCfgTCPPort_Type())
slcPCCardCfgTCPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTCPPort.setStatus(_A)
_SlcPCCardCfgTCPAuth_Type=EnabledState
_SlcPCCardCfgTCPAuth_Object=MibTableColumn
slcPCCardCfgTCPAuth=_SlcPCCardCfgTCPAuth_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,33),_SlcPCCardCfgTCPAuth_Type())
slcPCCardCfgTCPAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgTCPAuth.setStatus(_A)
_SlcPCCardCfgGSMPIN_Type=OctetString
_SlcPCCardCfgGSMPIN_Object=MibTableColumn
slcPCCardCfgGSMPIN=_SlcPCCardCfgGSMPIN_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,34),_SlcPCCardCfgGSMPIN_Type())
slcPCCardCfgGSMPIN.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMPIN.setStatus(_A)
_SlcPCCardCfgGSMNetworkName_Type=OctetString
_SlcPCCardCfgGSMNetworkName_Object=MibTableColumn
slcPCCardCfgGSMNetworkName=_SlcPCCardCfgGSMNetworkName_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,35),_SlcPCCardCfgGSMNetworkName_Type())
slcPCCardCfgGSMNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMNetworkName.setStatus(_I)
_SlcPCCardCfgGSMPPPCompression_Type=EnabledState
_SlcPCCardCfgGSMPPPCompression_Object=MibTableColumn
slcPCCardCfgGSMPPPCompression=_SlcPCCardCfgGSMPPPCompression_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,36),_SlcPCCardCfgGSMPPPCompression_Type())
slcPCCardCfgGSMPPPCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMPPPCompression.setStatus(_A)
_SlcPCCardCfgGSMAutoAcquireDNS_Type=EnabledState
_SlcPCCardCfgGSMAutoAcquireDNS_Object=MibTableColumn
slcPCCardCfgGSMAutoAcquireDNS=_SlcPCCardCfgGSMAutoAcquireDNS_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,37),_SlcPCCardCfgGSMAutoAcquireDNS_Type())
slcPCCardCfgGSMAutoAcquireDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMAutoAcquireDNS.setStatus(_A)
class _SlcPCCardCfgGSMDialoutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),('gsm',2)))
_SlcPCCardCfgGSMDialoutMode_Type.__name__=_C
_SlcPCCardCfgGSMDialoutMode_Object=MibTableColumn
slcPCCardCfgGSMDialoutMode=_SlcPCCardCfgGSMDialoutMode_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,38),_SlcPCCardCfgGSMDialoutMode_Type())
slcPCCardCfgGSMDialoutMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMDialoutMode.setStatus(_A)
_SlcPCCardCfgGSMContextID_Type=OctetString
_SlcPCCardCfgGSMContextID_Object=MibTableColumn
slcPCCardCfgGSMContextID=_SlcPCCardCfgGSMContextID_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,39),_SlcPCCardCfgGSMContextID_Type())
slcPCCardCfgGSMContextID.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMContextID.setStatus(_A)
_SlcPCCardCfgGSMBearerService_Type=OctetString
_SlcPCCardCfgGSMBearerService_Object=MibTableColumn
slcPCCardCfgGSMBearerService=_SlcPCCardCfgGSMBearerService_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,40),_SlcPCCardCfgGSMBearerService_Type())
slcPCCardCfgGSMBearerService.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGSMBearerService.setStatus(_A)
_SlcPCCardCfgIdleTimeout_Type=Integer32
_SlcPCCardCfgIdleTimeout_Object=MibTableColumn
slcPCCardCfgIdleTimeout=_SlcPCCardCfgIdleTimeout_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,41),_SlcPCCardCfgIdleTimeout_Type())
slcPCCardCfgIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgIdleTimeout.setStatus(_A)
_SlcPCCardCfgRestartDelay_Type=Integer32
_SlcPCCardCfgRestartDelay_Object=MibTableColumn
slcPCCardCfgRestartDelay=_SlcPCCardCfgRestartDelay_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,42),_SlcPCCardCfgRestartDelay_Type())
slcPCCardCfgRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:slcPCCardCfgRestartDelay.setUnits(_E)
_SlcPCCardCfgCallerIdLogging_Type=EnabledState
_SlcPCCardCfgCallerIdLogging_Object=MibTableColumn
slcPCCardCfgCallerIdLogging=_SlcPCCardCfgCallerIdLogging_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,43),_SlcPCCardCfgCallerIdLogging_Type())
slcPCCardCfgCallerIdLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCallerIdLogging.setStatus(_A)
_SlcPCCardCfgCallerIdATCmd_Type=OctetString
_SlcPCCardCfgCallerIdATCmd_Object=MibTableColumn
slcPCCardCfgCallerIdATCmd=_SlcPCCardCfgCallerIdATCmd_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,44),_SlcPCCardCfgCallerIdATCmd_Type())
slcPCCardCfgCallerIdATCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCallerIdATCmd.setStatus(_A)
class _SlcPCCardCfgDODAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcPCCardCfgDODAuth_Type.__name__=_C
_SlcPCCardCfgDODAuth_Object=MibTableColumn
slcPCCardCfgDODAuth=_SlcPCCardCfgDODAuth_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,45),_SlcPCCardCfgDODAuth_Type())
slcPCCardCfgDODAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDODAuth.setStatus(_A)
_SlcPCCardCfgDODCHAPHost_Type=OctetString
_SlcPCCardCfgDODCHAPHost_Object=MibTableColumn
slcPCCardCfgDODCHAPHost=_SlcPCCardCfgDODCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,46),_SlcPCCardCfgDODCHAPHost_Type())
slcPCCardCfgDODCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDODCHAPHost.setStatus(_A)
_SlcPCCardCfgHostList_Type=OctetString
_SlcPCCardCfgHostList_Object=MibTableColumn
slcPCCardCfgHostList=_SlcPCCardCfgHostList_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,47),_SlcPCCardCfgHostList_Type())
slcPCCardCfgHostList.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgHostList.setStatus(_A)
class _SlcPCCardCfgCBCPClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_SlcPCCardCfgCBCPClientType_Type.__name__=_C
_SlcPCCardCfgCBCPClientType_Object=MibTableColumn
slcPCCardCfgCBCPClientType=_SlcPCCardCfgCBCPClientType_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,48),_SlcPCCardCfgCBCPClientType_Type())
slcPCCardCfgCBCPClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCBCPClientType.setStatus(_A)
_SlcPCCardCfgCBCPServerAllowNoCallback_Type=EnabledState
_SlcPCCardCfgCBCPServerAllowNoCallback_Object=MibTableColumn
slcPCCardCfgCBCPServerAllowNoCallback=_SlcPCCardCfgCBCPServerAllowNoCallback_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,49),_SlcPCCardCfgCBCPServerAllowNoCallback_Type())
slcPCCardCfgCBCPServerAllowNoCallback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCBCPServerAllowNoCallback.setStatus(_A)
_SlcPCCardCfgDialbackDelay_Type=Integer32
_SlcPCCardCfgDialbackDelay_Object=MibTableColumn
slcPCCardCfgDialbackDelay=_SlcPCCardCfgDialbackDelay_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,50),_SlcPCCardCfgDialbackDelay_Type())
slcPCCardCfgDialbackDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDialbackDelay.setStatus(_A)
if mibBuilder.loadTexts:slcPCCardCfgDialbackDelay.setUnits(_E)
_SlcPCCardCfgCHAPAuthLocalUsers_Type=EnabledState
_SlcPCCardCfgCHAPAuthLocalUsers_Object=MibTableColumn
slcPCCardCfgCHAPAuthLocalUsers=_SlcPCCardCfgCHAPAuthLocalUsers_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,51),_SlcPCCardCfgCHAPAuthLocalUsers_Type())
slcPCCardCfgCHAPAuthLocalUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgCHAPAuthLocalUsers.setStatus(_A)
_SlcPCCardCfgUseSites_Type=EnabledState
_SlcPCCardCfgUseSites_Object=MibTableColumn
slcPCCardCfgUseSites=_SlcPCCardCfgUseSites_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,52),_SlcPCCardCfgUseSites_Type())
slcPCCardCfgUseSites.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgUseSites.setStatus(_A)
_SlcPCCardCfgDialbackRetries_Type=Integer32
_SlcPCCardCfgDialbackRetries_Object=MibTableColumn
slcPCCardCfgDialbackRetries=_SlcPCCardCfgDialbackRetries_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,53),_SlcPCCardCfgDialbackRetries_Type())
slcPCCardCfgDialbackRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgDialbackRetries.setStatus(_A)
_SlcPCCardCfgGroup_Type=OctetString
_SlcPCCardCfgGroup_Object=MibTableColumn
slcPCCardCfgGroup=_SlcPCCardCfgGroup_Object((1,3,6,1,4,1,244,1,1,4,3,1,1,54),_SlcPCCardCfgGroup_Type())
slcPCCardCfgGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardCfgGroup.setStatus(_A)
_SlcDevPowerSupply_ObjectIdentity=ObjectIdentity
slcDevPowerSupply=_SlcDevPowerSupply_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,4))
class _SlcDevPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acOnePowerSupply',1),('acTwoPowerSupplies',2),('dcTwoPowerSupplies',3)))
_SlcDevPowerSupplyType_Type.__name__=_C
_SlcDevPowerSupplyType_Object=MibScalar
slcDevPowerSupplyType=_SlcDevPowerSupplyType_Object((1,3,6,1,4,1,244,1,1,4,4,1),_SlcDevPowerSupplyType_Type())
slcDevPowerSupplyType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPowerSupplyType.setStatus(_A)
class _SlcDevPowerSupplyA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_SlcDevPowerSupplyA_Type.__name__=_C
_SlcDevPowerSupplyA_Object=MibScalar
slcDevPowerSupplyA=_SlcDevPowerSupplyA_Object((1,3,6,1,4,1,244,1,1,4,4,2),_SlcDevPowerSupplyA_Type())
slcDevPowerSupplyA.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPowerSupplyA.setStatus(_A)
class _SlcDevPowerSupplyB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('notInstalled',3)))
_SlcDevPowerSupplyB_Type.__name__=_C
_SlcDevPowerSupplyB_Object=MibScalar
slcDevPowerSupplyB=_SlcDevPowerSupplyB_Object((1,3,6,1,4,1,244,1,1,4,4,3),_SlcDevPowerSupplyB_Type())
slcDevPowerSupplyB.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPowerSupplyB.setStatus(_A)
_SlcDevUSB_ObjectIdentity=ObjectIdentity
slcDevUSB=_SlcDevUSB_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,5))
_SlcDevUSBState_Type=EnabledState
_SlcDevUSBState_Object=MibScalar
slcDevUSBState=_SlcDevUSBState_Object((1,3,6,1,4,1,244,1,1,4,5,1),_SlcDevUSBState_Type())
slcDevUSBState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBState.setStatus(_A)
_SlcDevUSBCfgTable_Object=MibTable
slcDevUSBCfgTable=_SlcDevUSBCfgTable_Object((1,3,6,1,4,1,244,1,1,4,5,2))
if mibBuilder.loadTexts:slcDevUSBCfgTable.setStatus(_A)
_SlcDevUSBCfgEntry_Object=MibTableRow
slcDevUSBCfgEntry=_SlcDevUSBCfgEntry_Object((1,3,6,1,4,1,244,1,1,4,5,2,1))
slcDevUSBCfgEntry.setIndexNames((0,_D,_x))
if mibBuilder.loadTexts:slcDevUSBCfgEntry.setStatus(_A)
class _SlcDevUSBId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_SlcDevUSBId_Type.__name__=_C
_SlcDevUSBId_Object=MibTableColumn
slcDevUSBId=_SlcDevUSBId_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,1),_SlcDevUSBId_Type())
slcDevUSBId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBId.setStatus(_A)
class _SlcDevUSBCfgCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6)))
_SlcDevUSBCfgCardType_Type.__name__=_C
_SlcDevUSBCfgCardType_Object=MibTableColumn
slcDevUSBCfgCardType=_SlcDevUSBCfgCardType_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,2),_SlcDevUSBCfgCardType_Type())
slcDevUSBCfgCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCardType.setStatus(_A)
_SlcDevUSBCfgCardId_Type=OctetString
_SlcDevUSBCfgCardId_Object=MibTableColumn
slcDevUSBCfgCardId=_SlcDevUSBCfgCardId_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,3),_SlcDevUSBCfgCardId_Type())
slcDevUSBCfgCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCardId.setStatus(_A)
class _SlcDevUSBCfgStorageFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AN,1),('ext2',2),('fat',3)))
_SlcDevUSBCfgStorageFS_Type.__name__=_C
_SlcDevUSBCfgStorageFS_Object=MibTableColumn
slcDevUSBCfgStorageFS=_SlcDevUSBCfgStorageFS_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,4),_SlcDevUSBCfgStorageFS_Type())
slcDevUSBCfgStorageFS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgStorageFS.setStatus(_A)
class _SlcDevUSBCfgBaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,300),ValueRangeConstraint(600,600),ValueRangeConstraint(1200,1200),ValueRangeConstraint(2400,2400),ValueRangeConstraint(4800,4800),ValueRangeConstraint(9600,9600),ValueRangeConstraint(19200,19200),ValueRangeConstraint(38400,38400),ValueRangeConstraint(57600,57600),ValueRangeConstraint(115200,115200))
_SlcDevUSBCfgBaud_Type.__name__=_C
_SlcDevUSBCfgBaud_Object=MibTableColumn
slcDevUSBCfgBaud=_SlcDevUSBCfgBaud_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,5),_SlcDevUSBCfgBaud_Type())
slcDevUSBCfgBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgBaud.setStatus(_A)
class _SlcDevUSBCfgDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,7),ValueRangeConstraint(8,8))
_SlcDevUSBCfgDataBits_Type.__name__=_C
_SlcDevUSBCfgDataBits_Object=MibTableColumn
slcDevUSBCfgDataBits=_SlcDevUSBCfgDataBits_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,6),_SlcDevUSBCfgDataBits_Type())
slcDevUSBCfgDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDataBits.setStatus(_A)
class _SlcDevUSBCfgStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_SlcDevUSBCfgStopBits_Type.__name__=_C
_SlcDevUSBCfgStopBits_Object=MibTableColumn
slcDevUSBCfgStopBits=_SlcDevUSBCfgStopBits_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,7),_SlcDevUSBCfgStopBits_Type())
slcDevUSBCfgStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgStopBits.setStatus(_A)
class _SlcDevUSBCfgParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_Q,2),(_R,3)))
_SlcDevUSBCfgParity_Type.__name__=_C
_SlcDevUSBCfgParity_Object=MibTableColumn
slcDevUSBCfgParity=_SlcDevUSBCfgParity_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,8),_SlcDevUSBCfgParity_Type())
slcDevUSBCfgParity.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgParity.setStatus(_A)
class _SlcDevUSBCfgFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_S,2),(_T,3)))
_SlcDevUSBCfgFlowControl_Type.__name__=_C
_SlcDevUSBCfgFlowControl_Object=MibTableColumn
slcDevUSBCfgFlowControl=_SlcDevUSBCfgFlowControl_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,9),_SlcDevUSBCfgFlowControl_Type())
slcDevUSBCfgFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgFlowControl.setStatus(_A)
class _SlcDevUSBCfgModemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,1),(_U,2),(_V,3),(_W,4),(_o,5),(_p,6),(_q,7),(_r,8),(_s,9)))
_SlcDevUSBCfgModemState_Type.__name__=_C
_SlcDevUSBCfgModemState_Object=MibTableColumn
slcDevUSBCfgModemState=_SlcDevUSBCfgModemState_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,10),_SlcDevUSBCfgModemState_Type())
slcDevUSBCfgModemState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgModemState.setStatus(_A)
class _SlcDevUSBCfgModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_SlcDevUSBCfgModemMode_Type.__name__=_C
_SlcDevUSBCfgModemMode_Object=MibTableColumn
slcDevUSBCfgModemMode=_SlcDevUSBCfgModemMode_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,11),_SlcDevUSBCfgModemMode_Type())
slcDevUSBCfgModemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgModemMode.setStatus(_A)
_SlcDevUSBCfgLocalIP_Type=IpAddress
_SlcDevUSBCfgLocalIP_Object=MibTableColumn
slcDevUSBCfgLocalIP=_SlcDevUSBCfgLocalIP_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,12),_SlcDevUSBCfgLocalIP_Type())
slcDevUSBCfgLocalIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgLocalIP.setStatus(_A)
_SlcDevUSBCfgRemoteIP_Type=IpAddress
_SlcDevUSBCfgRemoteIP_Object=MibTableColumn
slcDevUSBCfgRemoteIP=_SlcDevUSBCfgRemoteIP_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,13),_SlcDevUSBCfgRemoteIP_Type())
slcDevUSBCfgRemoteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgRemoteIP.setStatus(_A)
class _SlcDevUSBCfgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcDevUSBCfgAuth_Type.__name__=_C
_SlcDevUSBCfgAuth_Object=MibTableColumn
slcDevUSBCfgAuth=_SlcDevUSBCfgAuth_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,14),_SlcDevUSBCfgAuth_Type())
slcDevUSBCfgAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgAuth.setStatus(_A)
_SlcDevUSBCfgCHAPHost_Type=OctetString
_SlcDevUSBCfgCHAPHost_Object=MibTableColumn
slcDevUSBCfgCHAPHost=_SlcDevUSBCfgCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,15),_SlcDevUSBCfgCHAPHost_Type())
slcDevUSBCfgCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCHAPHost.setStatus(_A)
class _SlcDevUSBCfgDODAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcDevUSBCfgDODAuth_Type.__name__=_C
_SlcDevUSBCfgDODAuth_Object=MibTableColumn
slcDevUSBCfgDODAuth=_SlcDevUSBCfgDODAuth_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,16),_SlcDevUSBCfgDODAuth_Type())
slcDevUSBCfgDODAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDODAuth.setStatus(_A)
_SlcDevUSBCfgDODCHAPHost_Type=OctetString
_SlcDevUSBCfgDODCHAPHost_Object=MibTableColumn
slcDevUSBCfgDODCHAPHost=_SlcDevUSBCfgDODCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,17),_SlcDevUSBCfgDODCHAPHost_Type())
slcDevUSBCfgDODCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDODCHAPHost.setStatus(_A)
_SlcDevUSBCfgInitScript_Type=OctetString
_SlcDevUSBCfgInitScript_Object=MibTableColumn
slcDevUSBCfgInitScript=_SlcDevUSBCfgInitScript_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,18),_SlcDevUSBCfgInitScript_Type())
slcDevUSBCfgInitScript.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgInitScript.setStatus(_A)
class _SlcDevUSBCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcDevUSBCfgTimeout_Type.__name__=_C
_SlcDevUSBCfgTimeout_Object=MibTableColumn
slcDevUSBCfgTimeout=_SlcDevUSBCfgTimeout_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,19),_SlcDevUSBCfgTimeout_Type())
slcDevUSBCfgTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevUSBCfgTimeout.setUnits(_H)
_SlcDevUSBCfgDialoutNum_Type=OctetString
_SlcDevUSBCfgDialoutNum_Object=MibTableColumn
slcDevUSBCfgDialoutNum=_SlcDevUSBCfgDialoutNum_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,20),_SlcDevUSBCfgDialoutNum_Type())
slcDevUSBCfgDialoutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialoutNum.setStatus(_A)
class _SlcDevUSBCfgDialoutLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcDevUSBCfgDialoutLogin_Type.__name__=_F
_SlcDevUSBCfgDialoutLogin_Object=MibTableColumn
slcDevUSBCfgDialoutLogin=_SlcDevUSBCfgDialoutLogin_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,21),_SlcDevUSBCfgDialoutLogin_Type())
slcDevUSBCfgDialoutLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialoutLogin.setStatus(_A)
class _SlcDevUSBCfgDialbackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_SlcDevUSBCfgDialbackMode_Type.__name__=_C
_SlcDevUSBCfgDialbackMode_Object=MibTableColumn
slcDevUSBCfgDialbackMode=_SlcDevUSBCfgDialbackMode_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,22),_SlcDevUSBCfgDialbackMode_Type())
slcDevUSBCfgDialbackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialbackMode.setStatus(_A)
_SlcDevUSBCfgDialbackNum_Type=OctetString
_SlcDevUSBCfgDialbackNum_Object=MibTableColumn
slcDevUSBCfgDialbackNum=_SlcDevUSBCfgDialbackNum_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,23),_SlcDevUSBCfgDialbackNum_Type())
slcDevUSBCfgDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialbackNum.setStatus(_A)
_SlcDevUSBCfgDialbackDelay_Type=Integer32
_SlcDevUSBCfgDialbackDelay_Object=MibTableColumn
slcDevUSBCfgDialbackDelay=_SlcDevUSBCfgDialbackDelay_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,24),_SlcDevUSBCfgDialbackDelay_Type())
slcDevUSBCfgDialbackDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialbackDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevUSBCfgDialbackDelay.setUnits(_E)
_SlcDevUSBCfgNATState_Type=EnabledState
_SlcDevUSBCfgNATState_Object=MibTableColumn
slcDevUSBCfgNATState=_SlcDevUSBCfgNATState_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,25),_SlcDevUSBCfgNATState_Type())
slcDevUSBCfgNATState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgNATState.setStatus(_A)
_SlcDevUSBCfgIdleTimeout_Type=Integer32
_SlcDevUSBCfgIdleTimeout_Object=MibTableColumn
slcDevUSBCfgIdleTimeout=_SlcDevUSBCfgIdleTimeout_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,26),_SlcDevUSBCfgIdleTimeout_Type())
slcDevUSBCfgIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevUSBCfgIdleTimeout.setUnits(_E)
_SlcDevUSBCfgRestartDelay_Type=Integer32
_SlcDevUSBCfgRestartDelay_Object=MibTableColumn
slcDevUSBCfgRestartDelay=_SlcDevUSBCfgRestartDelay_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,27),_SlcDevUSBCfgRestartDelay_Type())
slcDevUSBCfgRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevUSBCfgRestartDelay.setUnits(_E)
_SlcDevUSBCfgCallerIdLogging_Type=EnabledState
_SlcDevUSBCfgCallerIdLogging_Object=MibTableColumn
slcDevUSBCfgCallerIdLogging=_SlcDevUSBCfgCallerIdLogging_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,28),_SlcDevUSBCfgCallerIdLogging_Type())
slcDevUSBCfgCallerIdLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCallerIdLogging.setStatus(_A)
_SlcDevUSBCfgCallerIdATCmd_Type=OctetString
_SlcDevUSBCfgCallerIdATCmd_Object=MibTableColumn
slcDevUSBCfgCallerIdATCmd=_SlcDevUSBCfgCallerIdATCmd_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,29),_SlcDevUSBCfgCallerIdATCmd_Type())
slcDevUSBCfgCallerIdATCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCallerIdATCmd.setStatus(_A)
_SlcDevUSBCfgHostList_Type=OctetString
_SlcDevUSBCfgHostList_Object=MibTableColumn
slcDevUSBCfgHostList=_SlcDevUSBCfgHostList_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,30),_SlcDevUSBCfgHostList_Type())
slcDevUSBCfgHostList.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgHostList.setStatus(_A)
class _SlcDevUSBCfgCBCPClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_SlcDevUSBCfgCBCPClientType_Type.__name__=_C
_SlcDevUSBCfgCBCPClientType_Object=MibTableColumn
slcDevUSBCfgCBCPClientType=_SlcDevUSBCfgCBCPClientType_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,31),_SlcDevUSBCfgCBCPClientType_Type())
slcDevUSBCfgCBCPClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCBCPClientType.setStatus(_A)
_SlcDevUSBCfgCBCPServerAllowNoCallback_Type=EnabledState
_SlcDevUSBCfgCBCPServerAllowNoCallback_Object=MibTableColumn
slcDevUSBCfgCBCPServerAllowNoCallback=_SlcDevUSBCfgCBCPServerAllowNoCallback_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,32),_SlcDevUSBCfgCBCPServerAllowNoCallback_Type())
slcDevUSBCfgCBCPServerAllowNoCallback.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCBCPServerAllowNoCallback.setStatus(_A)
_SlcDevUSBCfgTelnetState_Type=EnabledState
_SlcDevUSBCfgTelnetState_Object=MibTableColumn
slcDevUSBCfgTelnetState=_SlcDevUSBCfgTelnetState_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,33),_SlcDevUSBCfgTelnetState_Type())
slcDevUSBCfgTelnetState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTelnetState.setStatus(_A)
class _SlcDevUSBCfgTelnetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcDevUSBCfgTelnetPort_Type.__name__=_C
_SlcDevUSBCfgTelnetPort_Object=MibTableColumn
slcDevUSBCfgTelnetPort=_SlcDevUSBCfgTelnetPort_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,34),_SlcDevUSBCfgTelnetPort_Type())
slcDevUSBCfgTelnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTelnetPort.setStatus(_A)
_SlcDevUSBCfgTelnetAuth_Type=EnabledState
_SlcDevUSBCfgTelnetAuth_Object=MibTableColumn
slcDevUSBCfgTelnetAuth=_SlcDevUSBCfgTelnetAuth_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,35),_SlcDevUSBCfgTelnetAuth_Type())
slcDevUSBCfgTelnetAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTelnetAuth.setStatus(_A)
_SlcDevUSBCfgSSHState_Type=EnabledState
_SlcDevUSBCfgSSHState_Object=MibTableColumn
slcDevUSBCfgSSHState=_SlcDevUSBCfgSSHState_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,36),_SlcDevUSBCfgSSHState_Type())
slcDevUSBCfgSSHState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgSSHState.setStatus(_A)
class _SlcDevUSBCfgSSHPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcDevUSBCfgSSHPort_Type.__name__=_C
_SlcDevUSBCfgSSHPort_Object=MibTableColumn
slcDevUSBCfgSSHPort=_SlcDevUSBCfgSSHPort_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,37),_SlcDevUSBCfgSSHPort_Type())
slcDevUSBCfgSSHPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgSSHPort.setStatus(_A)
_SlcDevUSBCfgSSHAuth_Type=EnabledState
_SlcDevUSBCfgSSHAuth_Object=MibTableColumn
slcDevUSBCfgSSHAuth=_SlcDevUSBCfgSSHAuth_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,38),_SlcDevUSBCfgSSHAuth_Type())
slcDevUSBCfgSSHAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgSSHAuth.setStatus(_A)
_SlcDevUSBCfgTCPState_Type=EnabledState
_SlcDevUSBCfgTCPState_Object=MibTableColumn
slcDevUSBCfgTCPState=_SlcDevUSBCfgTCPState_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,39),_SlcDevUSBCfgTCPState_Type())
slcDevUSBCfgTCPState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTCPState.setStatus(_A)
class _SlcDevUSBCfgTCPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SlcDevUSBCfgTCPPort_Type.__name__=_C
_SlcDevUSBCfgTCPPort_Object=MibTableColumn
slcDevUSBCfgTCPPort=_SlcDevUSBCfgTCPPort_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,40),_SlcDevUSBCfgTCPPort_Type())
slcDevUSBCfgTCPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTCPPort.setStatus(_A)
_SlcDevUSBCfgTCPAuth_Type=EnabledState
_SlcDevUSBCfgTCPAuth_Object=MibTableColumn
slcDevUSBCfgTCPAuth=_SlcDevUSBCfgTCPAuth_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,41),_SlcDevUSBCfgTCPAuth_Type())
slcDevUSBCfgTCPAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgTCPAuth.setStatus(_A)
_SlcDevUSBCfgGSMPIN_Type=OctetString
_SlcDevUSBCfgGSMPIN_Object=MibTableColumn
slcDevUSBCfgGSMPIN=_SlcDevUSBCfgGSMPIN_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,42),_SlcDevUSBCfgGSMPIN_Type())
slcDevUSBCfgGSMPIN.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGSMPIN.setStatus(_A)
_SlcDevUSBCfgGSMPPPCompression_Type=EnabledState
_SlcDevUSBCfgGSMPPPCompression_Object=MibTableColumn
slcDevUSBCfgGSMPPPCompression=_SlcDevUSBCfgGSMPPPCompression_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,43),_SlcDevUSBCfgGSMPPPCompression_Type())
slcDevUSBCfgGSMPPPCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGSMPPPCompression.setStatus(_A)
_SlcDevUSBCfgGSMAutoAcquireDNS_Type=EnabledState
_SlcDevUSBCfgGSMAutoAcquireDNS_Object=MibTableColumn
slcDevUSBCfgGSMAutoAcquireDNS=_SlcDevUSBCfgGSMAutoAcquireDNS_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,44),_SlcDevUSBCfgGSMAutoAcquireDNS_Type())
slcDevUSBCfgGSMAutoAcquireDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGSMAutoAcquireDNS.setStatus(_A)
class _SlcDevUSBCfgGSMDialoutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),('gsm',2)))
_SlcDevUSBCfgGSMDialoutMode_Type.__name__=_C
_SlcDevUSBCfgGSMDialoutMode_Object=MibTableColumn
slcDevUSBCfgGSMDialoutMode=_SlcDevUSBCfgGSMDialoutMode_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,45),_SlcDevUSBCfgGSMDialoutMode_Type())
slcDevUSBCfgGSMDialoutMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGSMDialoutMode.setStatus(_A)
_SlcDevUSBCfgGSMContextID_Type=OctetString
_SlcDevUSBCfgGSMContextID_Object=MibTableColumn
slcDevUSBCfgGSMContextID=_SlcDevUSBCfgGSMContextID_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,46),_SlcDevUSBCfgGSMContextID_Type())
slcDevUSBCfgGSMContextID.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGSMContextID.setStatus(_A)
_SlcDevUSBCfgGSMBearerService_Type=OctetString
_SlcDevUSBCfgGSMBearerService_Object=MibTableColumn
slcDevUSBCfgGSMBearerService=_SlcDevUSBCfgGSMBearerService_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,47),_SlcDevUSBCfgGSMBearerService_Type())
slcDevUSBCfgGSMBearerService.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGSMBearerService.setStatus(_A)
_SlcDevUSBCfgCHAPAuthLocalUsers_Type=EnabledState
_SlcDevUSBCfgCHAPAuthLocalUsers_Object=MibTableColumn
slcDevUSBCfgCHAPAuthLocalUsers=_SlcDevUSBCfgCHAPAuthLocalUsers_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,48),_SlcDevUSBCfgCHAPAuthLocalUsers_Type())
slcDevUSBCfgCHAPAuthLocalUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgCHAPAuthLocalUsers.setStatus(_A)
_SlcDevUSBCfgUseSites_Type=EnabledState
_SlcDevUSBCfgUseSites_Object=MibTableColumn
slcDevUSBCfgUseSites=_SlcDevUSBCfgUseSites_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,49),_SlcDevUSBCfgUseSites_Type())
slcDevUSBCfgUseSites.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgUseSites.setStatus(_A)
_SlcDevUSBCfgDialbackRetries_Type=Integer32
_SlcDevUSBCfgDialbackRetries_Object=MibTableColumn
slcDevUSBCfgDialbackRetries=_SlcDevUSBCfgDialbackRetries_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,50),_SlcDevUSBCfgDialbackRetries_Type())
slcDevUSBCfgDialbackRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialbackRetries.setStatus(_A)
class _SlcDevUSBCfgDialtoneCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_SlcDevUSBCfgDialtoneCheck_Type.__name__=_C
_SlcDevUSBCfgDialtoneCheck_Object=MibTableColumn
slcDevUSBCfgDialtoneCheck=_SlcDevUSBCfgDialtoneCheck_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,51),_SlcDevUSBCfgDialtoneCheck_Type())
slcDevUSBCfgDialtoneCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgDialtoneCheck.setStatus(_A)
if mibBuilder.loadTexts:slcDevUSBCfgDialtoneCheck.setUnits(_H)
_SlcDevUSBCfgGroup_Type=OctetString
_SlcDevUSBCfgGroup_Object=MibTableColumn
slcDevUSBCfgGroup=_SlcDevUSBCfgGroup_Object((1,3,6,1,4,1,244,1,1,4,5,2,1,52),_SlcDevUSBCfgGroup_Type())
slcDevUSBCfgGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevUSBCfgGroup.setStatus(_A)
_SlcDevIntModem_ObjectIdentity=ObjectIdentity
slcDevIntModem=_SlcDevIntModem_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,6))
class _SlcDevIntModemModemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_U,2),(_V,3),(_W,4)))
_SlcDevIntModemModemState_Type.__name__=_C
_SlcDevIntModemModemState_Object=MibScalar
slcDevIntModemModemState=_SlcDevIntModemModemState_Object((1,3,6,1,4,1,244,1,1,4,6,1),_SlcDevIntModemModemState_Type())
slcDevIntModemModemState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemModemState.setStatus(_A)
class _SlcDevIntModemModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_SlcDevIntModemModemMode_Type.__name__=_C
_SlcDevIntModemModemMode_Object=MibScalar
slcDevIntModemModemMode=_SlcDevIntModemModemMode_Object((1,3,6,1,4,1,244,1,1,4,6,2),_SlcDevIntModemModemMode_Type())
slcDevIntModemModemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemModemMode.setStatus(_A)
_SlcDevIntModemLocalIP_Type=IpAddress
_SlcDevIntModemLocalIP_Object=MibScalar
slcDevIntModemLocalIP=_SlcDevIntModemLocalIP_Object((1,3,6,1,4,1,244,1,1,4,6,3),_SlcDevIntModemLocalIP_Type())
slcDevIntModemLocalIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemLocalIP.setStatus(_A)
_SlcDevIntModemRemoteIP_Type=IpAddress
_SlcDevIntModemRemoteIP_Object=MibScalar
slcDevIntModemRemoteIP=_SlcDevIntModemRemoteIP_Object((1,3,6,1,4,1,244,1,1,4,6,4),_SlcDevIntModemRemoteIP_Type())
slcDevIntModemRemoteIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemRemoteIP.setStatus(_A)
class _SlcDevIntModemAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_SlcDevIntModemAuth_Type.__name__=_C
_SlcDevIntModemAuth_Object=MibScalar
slcDevIntModemAuth=_SlcDevIntModemAuth_Object((1,3,6,1,4,1,244,1,1,4,6,5),_SlcDevIntModemAuth_Type())
slcDevIntModemAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemAuth.setStatus(_A)
_SlcDevIntModemCHAPHost_Type=OctetString
_SlcDevIntModemCHAPHost_Object=MibScalar
slcDevIntModemCHAPHost=_SlcDevIntModemCHAPHost_Object((1,3,6,1,4,1,244,1,1,4,6,6),_SlcDevIntModemCHAPHost_Type())
slcDevIntModemCHAPHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemCHAPHost.setStatus(_A)
_SlcDevIntModemInitScript_Type=OctetString
_SlcDevIntModemInitScript_Object=MibScalar
slcDevIntModemInitScript=_SlcDevIntModemInitScript_Object((1,3,6,1,4,1,244,1,1,4,6,7),_SlcDevIntModemInitScript_Type())
slcDevIntModemInitScript.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemInitScript.setStatus(_A)
class _SlcDevIntModemTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlcDevIntModemTimeout_Type.__name__=_C
_SlcDevIntModemTimeout_Object=MibScalar
slcDevIntModemTimeout=_SlcDevIntModemTimeout_Object((1,3,6,1,4,1,244,1,1,4,6,8),_SlcDevIntModemTimeout_Type())
slcDevIntModemTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevIntModemTimeout.setUnits(_H)
_SlcDevIntModemDialoutNum_Type=OctetString
_SlcDevIntModemDialoutNum_Object=MibScalar
slcDevIntModemDialoutNum=_SlcDevIntModemDialoutNum_Object((1,3,6,1,4,1,244,1,1,4,6,9),_SlcDevIntModemDialoutNum_Type())
slcDevIntModemDialoutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialoutNum.setStatus(_A)
class _SlcDevIntModemDialoutLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcDevIntModemDialoutLogin_Type.__name__=_F
_SlcDevIntModemDialoutLogin_Object=MibScalar
slcDevIntModemDialoutLogin=_SlcDevIntModemDialoutLogin_Object((1,3,6,1,4,1,244,1,1,4,6,10),_SlcDevIntModemDialoutLogin_Type())
slcDevIntModemDialoutLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialoutLogin.setStatus(_A)
class _SlcDevIntModemDialbackMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_SlcDevIntModemDialbackMode_Type.__name__=_C
_SlcDevIntModemDialbackMode_Object=MibScalar
slcDevIntModemDialbackMode=_SlcDevIntModemDialbackMode_Object((1,3,6,1,4,1,244,1,1,4,6,11),_SlcDevIntModemDialbackMode_Type())
slcDevIntModemDialbackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialbackMode.setStatus(_A)
_SlcDevIntModemDialbackNum_Type=OctetString
_SlcDevIntModemDialbackNum_Object=MibScalar
slcDevIntModemDialbackNum=_SlcDevIntModemDialbackNum_Object((1,3,6,1,4,1,244,1,1,4,6,12),_SlcDevIntModemDialbackNum_Type())
slcDevIntModemDialbackNum.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialbackNum.setStatus(_A)
_SlcDevIntModemDialbackRetries_Type=Integer32
_SlcDevIntModemDialbackRetries_Object=MibScalar
slcDevIntModemDialbackRetries=_SlcDevIntModemDialbackRetries_Object((1,3,6,1,4,1,244,1,1,4,6,13),_SlcDevIntModemDialbackRetries_Type())
slcDevIntModemDialbackRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialbackRetries.setStatus(_A)
_SlcDevIntModemDialbackDelay_Type=Integer32
_SlcDevIntModemDialbackDelay_Object=MibScalar
slcDevIntModemDialbackDelay=_SlcDevIntModemDialbackDelay_Object((1,3,6,1,4,1,244,1,1,4,6,14),_SlcDevIntModemDialbackDelay_Type())
slcDevIntModemDialbackDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialbackDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevIntModemDialbackDelay.setUnits(_E)
_SlcDevIntModemCallerIdLogging_Type=EnabledState
_SlcDevIntModemCallerIdLogging_Object=MibScalar
slcDevIntModemCallerIdLogging=_SlcDevIntModemCallerIdLogging_Object((1,3,6,1,4,1,244,1,1,4,6,15),_SlcDevIntModemCallerIdLogging_Type())
slcDevIntModemCallerIdLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemCallerIdLogging.setStatus(_A)
_SlcDevIntModemCallerIdATCmd_Type=OctetString
_SlcDevIntModemCallerIdATCmd_Object=MibScalar
slcDevIntModemCallerIdATCmd=_SlcDevIntModemCallerIdATCmd_Object((1,3,6,1,4,1,244,1,1,4,6,16),_SlcDevIntModemCallerIdATCmd_Type())
slcDevIntModemCallerIdATCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemCallerIdATCmd.setStatus(_A)
_SlcDevIntModemUseSites_Type=EnabledState
_SlcDevIntModemUseSites_Object=MibScalar
slcDevIntModemUseSites=_SlcDevIntModemUseSites_Object((1,3,6,1,4,1,244,1,1,4,6,17),_SlcDevIntModemUseSites_Type())
slcDevIntModemUseSites.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemUseSites.setStatus(_A)
_SlcDevIntModemGroup_Type=OctetString
_SlcDevIntModemGroup_Object=MibScalar
slcDevIntModemGroup=_SlcDevIntModemGroup_Object((1,3,6,1,4,1,244,1,1,4,6,18),_SlcDevIntModemGroup_Type())
slcDevIntModemGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemGroup.setStatus(_A)
_SlcDevIntModemIdleTimeout_Type=Integer32
_SlcDevIntModemIdleTimeout_Object=MibScalar
slcDevIntModemIdleTimeout=_SlcDevIntModemIdleTimeout_Object((1,3,6,1,4,1,244,1,1,4,6,19),_SlcDevIntModemIdleTimeout_Type())
slcDevIntModemIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcDevIntModemIdleTimeout.setUnits(_E)
_SlcDevIntModemRestartDelay_Type=Integer32
_SlcDevIntModemRestartDelay_Object=MibScalar
slcDevIntModemRestartDelay=_SlcDevIntModemRestartDelay_Object((1,3,6,1,4,1,244,1,1,4,6,20),_SlcDevIntModemRestartDelay_Type())
slcDevIntModemRestartDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemRestartDelay.setStatus(_A)
if mibBuilder.loadTexts:slcDevIntModemRestartDelay.setUnits(_E)
_SlcDevIntModemNATState_Type=EnabledState
_SlcDevIntModemNATState_Object=MibScalar
slcDevIntModemNATState=_SlcDevIntModemNATState_Object((1,3,6,1,4,1,244,1,1,4,6,21),_SlcDevIntModemNATState_Type())
slcDevIntModemNATState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemNATState.setStatus(_A)
class _SlcDevIntModemDialtoneCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_SlcDevIntModemDialtoneCheck_Type.__name__=_C
_SlcDevIntModemDialtoneCheck_Object=MibScalar
slcDevIntModemDialtoneCheck=_SlcDevIntModemDialtoneCheck_Object((1,3,6,1,4,1,244,1,1,4,6,22),_SlcDevIntModemDialtoneCheck_Type())
slcDevIntModemDialtoneCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevIntModemDialtoneCheck.setStatus(_A)
if mibBuilder.loadTexts:slcDevIntModemDialtoneCheck.setUnits(_H)
_SlcDevRPM_ObjectIdentity=ObjectIdentity
slcDevRPM=_SlcDevRPM_ObjectIdentity((1,3,6,1,4,1,244,1,1,4,7))
_SlcDevRPMCfgTable_Object=MibTable
slcDevRPMCfgTable=_SlcDevRPMCfgTable_Object((1,3,6,1,4,1,244,1,1,4,7,1))
if mibBuilder.loadTexts:slcDevRPMCfgTable.setStatus(_A)
_SlcDevRPMCfgEntry_Object=MibTableRow
slcDevRPMCfgEntry=_SlcDevRPMCfgEntry_Object((1,3,6,1,4,1,244,1,1,4,7,1,1))
slcDevRPMCfgEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:slcDevRPMCfgEntry.setStatus(_A)
class _SlcDevRPMId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SlcDevRPMId_Type.__name__=_C
_SlcDevRPMId_Object=MibTableColumn
slcDevRPMId=_SlcDevRPMId_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,1),_SlcDevRPMId_Type())
slcDevRPMId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMId.setStatus(_A)
class _SlcDevRPMName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SlcDevRPMName_Type.__name__=_F
_SlcDevRPMName_Object=MibTableColumn
slcDevRPMName=_SlcDevRPMName_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,2),_SlcDevRPMName_Type())
slcDevRPMName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMName.setStatus(_A)
_SlcDevRPMVendorModel_Type=OctetString
_SlcDevRPMVendorModel_Object=MibTableColumn
slcDevRPMVendorModel=_SlcDevRPMVendorModel_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,3),_SlcDevRPMVendorModel_Type())
slcDevRPMVendorModel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMVendorModel.setStatus(_A)
class _SlcDevRPMManagedVia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serial',1),('network',2),('snmp',3),('usb',4)))
_SlcDevRPMManagedVia_Type.__name__=_C
_SlcDevRPMManagedVia_Object=MibTableColumn
slcDevRPMManagedVia=_SlcDevRPMManagedVia_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,4),_SlcDevRPMManagedVia_Type())
slcDevRPMManagedVia.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMManagedVia.setStatus(_A)
_SlcDevRPMIPAddress_Type=IpAddress
_SlcDevRPMIPAddress_Object=MibTableColumn
slcDevRPMIPAddress=_SlcDevRPMIPAddress_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,5),_SlcDevRPMIPAddress_Type())
slcDevRPMIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMIPAddress.setStatus(_A)
_SlcDevRPMPort_Type=Integer32
_SlcDevRPMPort_Object=MibTableColumn
slcDevRPMPort=_SlcDevRPMPort_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,6),_SlcDevRPMPort_Type())
slcDevRPMPort.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMPort.setStatus(_A)
_SlcDevRPMDriverOpts_Type=OctetString
_SlcDevRPMDriverOpts_Object=MibTableColumn
slcDevRPMDriverOpts=_SlcDevRPMDriverOpts_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,7),_SlcDevRPMDriverOpts_Type())
slcDevRPMDriverOpts.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMDriverOpts.setStatus(_A)
_SlcDevRPMStatus_Type=OctetString
_SlcDevRPMStatus_Object=MibTableColumn
slcDevRPMStatus=_SlcDevRPMStatus_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,8),_SlcDevRPMStatus_Type())
slcDevRPMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMStatus.setStatus(_A)
_SlcDevRPMFirmwareVersion_Type=OctetString
_SlcDevRPMFirmwareVersion_Object=MibTableColumn
slcDevRPMFirmwareVersion=_SlcDevRPMFirmwareVersion_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,9),_SlcDevRPMFirmwareVersion_Type())
slcDevRPMFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMFirmwareVersion.setStatus(_A)
_SlcDevRPMSerialNumber_Type=OctetString
_SlcDevRPMSerialNumber_Object=MibTableColumn
slcDevRPMSerialNumber=_SlcDevRPMSerialNumber_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,10),_SlcDevRPMSerialNumber_Type())
slcDevRPMSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMSerialNumber.setStatus(_A)
_SlcDevRPMMACAddress_Type=OctetString
_SlcDevRPMMACAddress_Object=MibTableColumn
slcDevRPMMACAddress=_SlcDevRPMMACAddress_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,11),_SlcDevRPMMACAddress_Type())
slcDevRPMMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMMACAddress.setStatus(_A)
class _SlcDevRPMNumOutlets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_SlcDevRPMNumOutlets_Type.__name__=_C
_SlcDevRPMNumOutlets_Object=MibTableColumn
slcDevRPMNumOutlets=_SlcDevRPMNumOutlets_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,12),_SlcDevRPMNumOutlets_Type())
slcDevRPMNumOutlets.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMNumOutlets.setStatus(_A)
class _SlcDevRPMOutletsOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,120))
_SlcDevRPMOutletsOn_Type.__name__=_C
_SlcDevRPMOutletsOn_Object=MibTableColumn
slcDevRPMOutletsOn=_SlcDevRPMOutletsOn_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,13),_SlcDevRPMOutletsOn_Type())
slcDevRPMOutletsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMOutletsOn.setStatus(_A)
class _SlcDevRPMSNMPReadComm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SlcDevRPMSNMPReadComm_Type.__name__=_F
_SlcDevRPMSNMPReadComm_Object=MibTableColumn
slcDevRPMSNMPReadComm=_SlcDevRPMSNMPReadComm_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,14),_SlcDevRPMSNMPReadComm_Type())
slcDevRPMSNMPReadComm.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMSNMPReadComm.setStatus(_A)
class _SlcDevRPMAdminLogin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SlcDevRPMAdminLogin_Type.__name__=_F
_SlcDevRPMAdminLogin_Object=MibTableColumn
slcDevRPMAdminLogin=_SlcDevRPMAdminLogin_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,15),_SlcDevRPMAdminLogin_Type())
slcDevRPMAdminLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMAdminLogin.setStatus(_A)
class _SlcDevRPMLogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_SlcDevRPMLogStatus_Type.__name__=_C
_SlcDevRPMLogStatus_Object=MibTableColumn
slcDevRPMLogStatus=_SlcDevRPMLogStatus_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,16),_SlcDevRPMLogStatus_Type())
slcDevRPMLogStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMLogStatus.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMLogStatus.setUnits(_H)
_SlcDevRPMCriticalSNMPTraps_Type=EnabledState
_SlcDevRPMCriticalSNMPTraps_Object=MibTableColumn
slcDevRPMCriticalSNMPTraps=_SlcDevRPMCriticalSNMPTraps_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,17),_SlcDevRPMCriticalSNMPTraps_Type())
slcDevRPMCriticalSNMPTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMCriticalSNMPTraps.setStatus(_A)
_SlcDevRPMCriticalEmails_Type=OctetString
_SlcDevRPMCriticalEmails_Object=MibTableColumn
slcDevRPMCriticalEmails=_SlcDevRPMCriticalEmails_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,18),_SlcDevRPMCriticalEmails_Type())
slcDevRPMCriticalEmails.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMCriticalEmails.setStatus(_A)
_SlcDevRPMProvidesSLCPower_Type=EnabledState
_SlcDevRPMProvidesSLCPower_Object=MibTableColumn
slcDevRPMProvidesSLCPower=_SlcDevRPMProvidesSLCPower_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,19),_SlcDevRPMProvidesSLCPower_Type())
slcDevRPMProvidesSLCPower.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMProvidesSLCPower.setStatus(_A)
class _SlcDevRPMOnLowBattery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('shutdownThisUPS',1),('shutdownAllUPS',2),('allowBatteryToFail',3),('shutdownSLCUPS',4)))
_SlcDevRPMOnLowBattery_Type.__name__=_C
_SlcDevRPMOnLowBattery_Object=MibTableColumn
slcDevRPMOnLowBattery=_SlcDevRPMOnLowBattery_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,20),_SlcDevRPMOnLowBattery_Type())
slcDevRPMOnLowBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMOnLowBattery.setStatus(_A)
class _SlcDevRPMShutdownOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_SlcDevRPMShutdownOrder_Type.__name__=_C
_SlcDevRPMShutdownOrder_Object=MibTableColumn
slcDevRPMShutdownOrder=_SlcDevRPMShutdownOrder_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,21),_SlcDevRPMShutdownOrder_Type())
slcDevRPMShutdownOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMShutdownOrder.setStatus(_A)
class _SlcDevRPMLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000))
_SlcDevRPMLoad_Type.__name__=_C
_SlcDevRPMLoad_Object=MibTableColumn
slcDevRPMLoad=_SlcDevRPMLoad_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,22),_SlcDevRPMLoad_Type())
slcDevRPMLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMLoad.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMLoad.setUnits(_y)
class _SlcDevRPMLoadOverThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000))
_SlcDevRPMLoadOverThreshold_Type.__name__=_C
_SlcDevRPMLoadOverThreshold_Object=MibTableColumn
slcDevRPMLoadOverThreshold=_SlcDevRPMLoadOverThreshold_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,23),_SlcDevRPMLoadOverThreshold_Type())
slcDevRPMLoadOverThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMLoadOverThreshold.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMLoadOverThreshold.setUnits(_y)
class _SlcDevRPMBatteryCharge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000))
_SlcDevRPMBatteryCharge_Type.__name__=_C
_SlcDevRPMBatteryCharge_Object=MibTableColumn
slcDevRPMBatteryCharge=_SlcDevRPMBatteryCharge_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,24),_SlcDevRPMBatteryCharge_Type())
slcDevRPMBatteryCharge.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMBatteryCharge.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMBatteryCharge.setUnits(_y)
_SlcDevRPMBatteryRuntime_Type=TimeTicks
_SlcDevRPMBatteryRuntime_Object=MibTableColumn
slcDevRPMBatteryRuntime=_SlcDevRPMBatteryRuntime_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,25),_SlcDevRPMBatteryRuntime_Type())
slcDevRPMBatteryRuntime.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMBatteryRuntime.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMBatteryRuntime.setUnits(_AO)
_SlcDevRPMBeeperStatus_Type=EnabledState
_SlcDevRPMBeeperStatus_Object=MibTableColumn
slcDevRPMBeeperStatus=_SlcDevRPMBeeperStatus_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,26),_SlcDevRPMBeeperStatus_Type())
slcDevRPMBeeperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMBeeperStatus.setStatus(_A)
_SlcDevRPMTemperature_Type=Integer32
_SlcDevRPMTemperature_Object=MibTableColumn
slcDevRPMTemperature=_SlcDevRPMTemperature_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,27),_SlcDevRPMTemperature_Type())
slcDevRPMTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMTemperature.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMTemperature.setUnits(_K)
_SlcDevRPMUptime_Type=TimeTicks
_SlcDevRPMUptime_Object=MibTableColumn
slcDevRPMUptime=_SlcDevRPMUptime_Object((1,3,6,1,4,1,244,1,1,4,7,1,1,28),_SlcDevRPMUptime_Type())
slcDevRPMUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMUptime.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMUptime.setUnits(_AO)
_SlcDevRPMStatusTable_Object=MibTable
slcDevRPMStatusTable=_SlcDevRPMStatusTable_Object((1,3,6,1,4,1,244,1,1,4,7,2))
if mibBuilder.loadTexts:slcDevRPMStatusTable.setStatus(_A)
_SlcDevRPMStatusEntry_Object=MibTableRow
slcDevRPMStatusEntry=_SlcDevRPMStatusEntry_Object((1,3,6,1,4,1,244,1,1,4,7,2,1))
slcDevRPMStatusEntry.setIndexNames((0,_D,_g),(0,_D,_AP))
if mibBuilder.loadTexts:slcDevRPMStatusEntry.setStatus(_A)
_SlcDevRPMCurrent_Type=Integer32
_SlcDevRPMCurrent_Object=MibTableColumn
slcDevRPMCurrent=_SlcDevRPMCurrent_Object((1,3,6,1,4,1,244,1,1,4,7,2,1,1),_SlcDevRPMCurrent_Type())
slcDevRPMCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMCurrent.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMCurrent.setUnits(_AQ)
_SlcDevRPMInputVoltage_Type=Integer32
_SlcDevRPMInputVoltage_Object=MibTableColumn
slcDevRPMInputVoltage=_SlcDevRPMInputVoltage_Object((1,3,6,1,4,1,244,1,1,4,7,2,1,2),_SlcDevRPMInputVoltage_Type())
slcDevRPMInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMInputVoltage.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMInputVoltage.setUnits('tenths of Volts')
_SlcDevRPMApparentPower_Type=Integer32
_SlcDevRPMApparentPower_Object=MibTableColumn
slcDevRPMApparentPower=_SlcDevRPMApparentPower_Object((1,3,6,1,4,1,244,1,1,4,7,2,1,3),_SlcDevRPMApparentPower_Type())
slcDevRPMApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMApparentPower.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMApparentPower.setUnits(_AR)
_SlcDevRPMNominalApparentPower_Type=Integer32
_SlcDevRPMNominalApparentPower_Object=MibTableColumn
slcDevRPMNominalApparentPower=_SlcDevRPMNominalApparentPower_Object((1,3,6,1,4,1,244,1,1,4,7,2,1,4),_SlcDevRPMNominalApparentPower_Type())
slcDevRPMNominalApparentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMNominalApparentPower.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMNominalApparentPower.setUnits(_AR)
_SlcDevRPMRealPower_Type=Integer32
_SlcDevRPMRealPower_Object=MibTableColumn
slcDevRPMRealPower=_SlcDevRPMRealPower_Object((1,3,6,1,4,1,244,1,1,4,7,2,1,5),_SlcDevRPMRealPower_Type())
slcDevRPMRealPower.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMRealPower.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMRealPower.setUnits(_AS)
_SlcDevRPMNominalRealPower_Type=Integer32
_SlcDevRPMNominalRealPower_Object=MibTableColumn
slcDevRPMNominalRealPower=_SlcDevRPMNominalRealPower_Object((1,3,6,1,4,1,244,1,1,4,7,2,1,6),_SlcDevRPMNominalRealPower_Type())
slcDevRPMNominalRealPower.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMNominalRealPower.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMNominalRealPower.setUnits(_AS)
_SlcDevRPMOutletTable_Object=MibTable
slcDevRPMOutletTable=_SlcDevRPMOutletTable_Object((1,3,6,1,4,1,244,1,1,4,7,3))
if mibBuilder.loadTexts:slcDevRPMOutletTable.setStatus(_A)
_SlcDevRPMOutletEntry_Object=MibTableRow
slcDevRPMOutletEntry=_SlcDevRPMOutletEntry_Object((1,3,6,1,4,1,244,1,1,4,7,3,1))
slcDevRPMOutletEntry.setIndexNames((0,_D,_g),(0,_D,_AT))
if mibBuilder.loadTexts:slcDevRPMOutletEntry.setStatus(_A)
_SlcDevRPMOutletName_Type=OctetString
_SlcDevRPMOutletName_Object=MibTableColumn
slcDevRPMOutletName=_SlcDevRPMOutletName_Object((1,3,6,1,4,1,244,1,1,4,7,3,1,1),_SlcDevRPMOutletName_Type())
slcDevRPMOutletName.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMOutletName.setStatus(_A)
class _SlcDevRPMOutletState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('off',2),('on',3)))
_SlcDevRPMOutletState_Type.__name__=_C
_SlcDevRPMOutletState_Object=MibTableColumn
slcDevRPMOutletState=_SlcDevRPMOutletState_Object((1,3,6,1,4,1,244,1,1,4,7,3,1,2),_SlcDevRPMOutletState_Type())
slcDevRPMOutletState.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMOutletState.setStatus(_A)
_SlcDevRPMOutletCurrent_Type=Integer32
_SlcDevRPMOutletCurrent_Object=MibTableColumn
slcDevRPMOutletCurrent=_SlcDevRPMOutletCurrent_Object((1,3,6,1,4,1,244,1,1,4,7,3,1,3),_SlcDevRPMOutletCurrent_Type())
slcDevRPMOutletCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevRPMOutletCurrent.setStatus(_A)
if mibBuilder.loadTexts:slcDevRPMOutletCurrent.setUnits(_AQ)
class _SlcDevRPMOutletAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_t,1),('turnOff',2),('turnOn',3),(_AK,4)))
_SlcDevRPMOutletAction_Type.__name__=_C
_SlcDevRPMOutletAction_Object=MibTableColumn
slcDevRPMOutletAction=_SlcDevRPMOutletAction_Object((1,3,6,1,4,1,244,1,1,4,7,3,1,4),_SlcDevRPMOutletAction_Type())
slcDevRPMOutletAction.setMaxAccess(_u)
if mibBuilder.loadTexts:slcDevRPMOutletAction.setStatus(_A)
_SlcConnections_ObjectIdentity=ObjectIdentity
slcConnections=_SlcConnections_ObjectIdentity((1,3,6,1,4,1,244,1,1,5))
_SlcConnNumber_Type=Integer32
_SlcConnNumber_Object=MibScalar
slcConnNumber=_SlcConnNumber_Object((1,3,6,1,4,1,244,1,1,5,1),_SlcConnNumber_Type())
slcConnNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnNumber.setStatus(_A)
_SlcConnTable_Object=MibTable
slcConnTable=_SlcConnTable_Object((1,3,6,1,4,1,244,1,1,5,2))
if mibBuilder.loadTexts:slcConnTable.setStatus(_A)
_SlcConnEntry_Object=MibTableRow
slcConnEntry=_SlcConnEntry_Object((1,3,6,1,4,1,244,1,1,5,2,1))
slcConnEntry.setIndexNames((0,_D,_AU))
if mibBuilder.loadTexts:slcConnEntry.setStatus(_A)
class _SlcConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_SlcConnIndex_Type.__name__=_C
_SlcConnIndex_Object=MibTableColumn
slcConnIndex=_SlcConnIndex_Object((1,3,6,1,4,1,244,1,1,5,2,1,1),_SlcConnIndex_Type())
slcConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnIndex.setStatus(_A)
_SlcConnEndPt1_Type=OctetString
_SlcConnEndPt1_Object=MibTableColumn
slcConnEndPt1=_SlcConnEndPt1_Object((1,3,6,1,4,1,244,1,1,5,2,1,2),_SlcConnEndPt1_Type())
slcConnEndPt1.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnEndPt1.setStatus(_A)
_SlcConnEndPt2_Type=OctetString
_SlcConnEndPt2_Object=MibTableColumn
slcConnEndPt2=_SlcConnEndPt2_Object((1,3,6,1,4,1,244,1,1,5,2,1,3),_SlcConnEndPt2_Type())
slcConnEndPt2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnEndPt2.setStatus(_A)
class _SlcConnFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bidirectional',1),('endpt1toendpt2',2),('endpt2toendpt1',3)))
_SlcConnFlow_Type.__name__=_C
_SlcConnFlow_Object=MibTableColumn
slcConnFlow=_SlcConnFlow_Object((1,3,6,1,4,1,244,1,1,5,2,1,4),_SlcConnFlow_Type())
slcConnFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnFlow.setStatus(_A)
class _SlcConnUser_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SlcConnUser_Type.__name__=_F
_SlcConnUser_Object=MibTableColumn
slcConnUser=_SlcConnUser_Object((1,3,6,1,4,1,244,1,1,5,2,1,5),_SlcConnUser_Type())
slcConnUser.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnUser.setStatus(_A)
_SlcConnDuration_Type=Integer32
_SlcConnDuration_Object=MibTableColumn
slcConnDuration=_SlcConnDuration_Object((1,3,6,1,4,1,244,1,1,5,2,1,6),_SlcConnDuration_Type())
slcConnDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnDuration.setStatus(_A)
if mibBuilder.loadTexts:slcConnDuration.setUnits(_E)
_SlcConnDurationStr_Type=OctetString
_SlcConnDurationStr_Object=MibTableColumn
slcConnDurationStr=_SlcConnDurationStr_Object((1,3,6,1,4,1,244,1,1,5,2,1,7),_SlcConnDurationStr_Type())
slcConnDurationStr.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnDurationStr.setStatus(_A)
_SlcConnIdle_Type=Integer32
_SlcConnIdle_Object=MibTableColumn
slcConnIdle=_SlcConnIdle_Object((1,3,6,1,4,1,244,1,1,5,2,1,8),_SlcConnIdle_Type())
slcConnIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnIdle.setStatus(_A)
if mibBuilder.loadTexts:slcConnIdle.setUnits(_E)
_SlcConnIdleStr_Type=OctetString
_SlcConnIdleStr_Object=MibTableColumn
slcConnIdleStr=_SlcConnIdleStr_Object((1,3,6,1,4,1,244,1,1,5,2,1,9),_SlcConnIdleStr_Type())
slcConnIdleStr.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnIdleStr.setStatus(_A)
_SlcConnSourceIP_Type=IpAddress
_SlcConnSourceIP_Object=MibTableColumn
slcConnSourceIP=_SlcConnSourceIP_Object((1,3,6,1,4,1,244,1,1,5,2,1,10),_SlcConnSourceIP_Type())
slcConnSourceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:slcConnSourceIP.setStatus(_A)
_SlcSystem_ObjectIdentity=ObjectIdentity
slcSystem=_SlcSystem_ObjectIdentity((1,3,6,1,4,1,244,1,1,6))
_SlcSystemModel_Type=OctetString
_SlcSystemModel_Object=MibScalar
slcSystemModel=_SlcSystemModel_Object((1,3,6,1,4,1,244,1,1,6,1),_SlcSystemModel_Type())
slcSystemModel.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemModel.setStatus(_A)
_SlcSystemSerialNo_Type=OctetString
_SlcSystemSerialNo_Object=MibScalar
slcSystemSerialNo=_SlcSystemSerialNo_Object((1,3,6,1,4,1,244,1,1,6,2),_SlcSystemSerialNo_Type())
slcSystemSerialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemSerialNo.setStatus(_A)
_SlcSystemFWRev_Type=OctetString
_SlcSystemFWRev_Object=MibScalar
slcSystemFWRev=_SlcSystemFWRev_Object((1,3,6,1,4,1,244,1,1,6,3),_SlcSystemFWRev_Type())
slcSystemFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemFWRev.setStatus(_A)
class _SlcSystemLoadVia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ftp',1),('tftp',2),('sftp',3),('slm',4),('https',5),('nfs',6),('pccard',7)))
_SlcSystemLoadVia_Type.__name__=_C
_SlcSystemLoadVia_Object=MibScalar
slcSystemLoadVia=_SlcSystemLoadVia_Object((1,3,6,1,4,1,244,1,1,6,4),_SlcSystemLoadVia_Type())
slcSystemLoadVia.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLoadVia.setStatus(_A)
_SlcSystemFTPServer_Type=IpAddress
_SlcSystemFTPServer_Object=MibScalar
slcSystemFTPServer=_SlcSystemFTPServer_Object((1,3,6,1,4,1,244,1,1,6,5),_SlcSystemFTPServer_Type())
slcSystemFTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemFTPServer.setStatus(_A)
_SlcSystemFTPPath_Type=OctetString
_SlcSystemFTPPath_Object=MibScalar
slcSystemFTPPath=_SlcSystemFTPPath_Object((1,3,6,1,4,1,244,1,1,6,6),_SlcSystemFTPPath_Type())
slcSystemFTPPath.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemFTPPath.setStatus(_A)
_SlcSystemKeypadLock_Type=EnabledState
_SlcSystemKeypadLock_Object=MibScalar
slcSystemKeypadLock=_SlcSystemKeypadLock_Object((1,3,6,1,4,1,244,1,1,6,7),_SlcSystemKeypadLock_Type())
slcSystemKeypadLock.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemKeypadLock.setStatus(_A)
_SlcSystemTimeZone_Type=OctetString
_SlcSystemTimeZone_Object=MibScalar
slcSystemTimeZone=_SlcSystemTimeZone_Object((1,3,6,1,4,1,244,1,1,6,8),_SlcSystemTimeZone_Type())
slcSystemTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemTimeZone.setStatus(_A)
_SlcSystemWelcomeBanner_Type=OctetString
_SlcSystemWelcomeBanner_Object=MibScalar
slcSystemWelcomeBanner=_SlcSystemWelcomeBanner_Object((1,3,6,1,4,1,244,1,1,6,9),_SlcSystemWelcomeBanner_Type())
slcSystemWelcomeBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWelcomeBanner.setStatus(_A)
_SlcSystemLoginBanner_Type=OctetString
_SlcSystemLoginBanner_Object=MibScalar
slcSystemLoginBanner=_SlcSystemLoginBanner_Object((1,3,6,1,4,1,244,1,1,6,10),_SlcSystemLoginBanner_Type())
slcSystemLoginBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLoginBanner.setStatus(_A)
_SlcSystemLogoutBanner_Type=OctetString
_SlcSystemLogoutBanner_Object=MibScalar
slcSystemLogoutBanner=_SlcSystemLogoutBanner_Object((1,3,6,1,4,1,244,1,1,6,11),_SlcSystemLogoutBanner_Type())
slcSystemLogoutBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLogoutBanner.setStatus(_A)
class _SlcSystemWebTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,120))
_SlcSystemWebTimeout_Type.__name__=_C
_SlcSystemWebTimeout_Object=MibScalar
slcSystemWebTimeout=_SlcSystemWebTimeout_Object((1,3,6,1,4,1,244,1,1,6,12),_SlcSystemWebTimeout_Type())
slcSystemWebTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebTimeout.setStatus(_A)
if mibBuilder.loadTexts:slcSystemWebTimeout.setUnits(_H)
_SlcSystemWebGadget_Type=EnabledState
_SlcSystemWebGadget_Object=MibScalar
slcSystemWebGadget=_SlcSystemWebGadget_Object((1,3,6,1,4,1,244,1,1,6,13),_SlcSystemWebGadget_Type())
slcSystemWebGadget.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebGadget.setStatus(_A)
class _SlcSystemAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),('rebootSLC',2),('shutdownSLC',3)))
_SlcSystemAction_Type.__name__=_C
_SlcSystemAction_Object=MibScalar
slcSystemAction=_SlcSystemAction_Object((1,3,6,1,4,1,244,1,1,6,14),_SlcSystemAction_Type())
slcSystemAction.setMaxAccess(_u)
if mibBuilder.loadTexts:slcSystemAction.setStatus(_A)
_SlcSystemSSHPreAuthBanner_Type=OctetString
_SlcSystemSSHPreAuthBanner_Object=MibScalar
slcSystemSSHPreAuthBanner=_SlcSystemSSHPreAuthBanner_Object((1,3,6,1,4,1,244,1,1,6,15),_SlcSystemSSHPreAuthBanner_Type())
slcSystemSSHPreAuthBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemSSHPreAuthBanner.setStatus(_A)
class _SlcSystemSiteRackRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SlcSystemSiteRackRow_Type.__name__=_C
_SlcSystemSiteRackRow_Object=MibScalar
slcSystemSiteRackRow=_SlcSystemSiteRackRow_Object((1,3,6,1,4,1,244,1,1,6,16),_SlcSystemSiteRackRow_Type())
slcSystemSiteRackRow.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemSiteRackRow.setStatus(_A)
class _SlcSystemSiteRackCluster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SlcSystemSiteRackCluster_Type.__name__=_C
_SlcSystemSiteRackCluster_Object=MibScalar
slcSystemSiteRackCluster=_SlcSystemSiteRackCluster_Object((1,3,6,1,4,1,244,1,1,6,17),_SlcSystemSiteRackCluster_Type())
slcSystemSiteRackCluster.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemSiteRackCluster.setStatus(_A)
class _SlcSystemSiteRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SlcSystemSiteRack_Type.__name__=_C
_SlcSystemSiteRack_Object=MibScalar
slcSystemSiteRack=_SlcSystemSiteRack_Object((1,3,6,1,4,1,244,1,1,6,18),_SlcSystemSiteRack_Type())
slcSystemSiteRack.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemSiteRack.setStatus(_A)
_SlcSystemLCDScreens_Type=OctetString
_SlcSystemLCDScreens_Object=MibScalar
slcSystemLCDScreens=_SlcSystemLCDScreens_Object((1,3,6,1,4,1,244,1,1,6,19),_SlcSystemLCDScreens_Type())
slcSystemLCDScreens.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLCDScreens.setStatus(_A)
_SlcSystemLCDUserStrLine1_Type=OctetString
_SlcSystemLCDUserStrLine1_Object=MibScalar
slcSystemLCDUserStrLine1=_SlcSystemLCDUserStrLine1_Object((1,3,6,1,4,1,244,1,1,6,20),_SlcSystemLCDUserStrLine1_Type())
slcSystemLCDUserStrLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLCDUserStrLine1.setStatus(_A)
_SlcSystemLCDUserStrLine2_Type=OctetString
_SlcSystemLCDUserStrLine2_Object=MibScalar
slcSystemLCDUserStrLine2=_SlcSystemLCDUserStrLine2_Object((1,3,6,1,4,1,244,1,1,6,21),_SlcSystemLCDUserStrLine2_Type())
slcSystemLCDUserStrLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLCDUserStrLine2.setStatus(_A)
_SlcSystemLCDScrolling_Type=EnabledState
_SlcSystemLCDScrolling_Object=MibScalar
slcSystemLCDScrolling=_SlcSystemLCDScrolling_Object((1,3,6,1,4,1,244,1,1,6,22),_SlcSystemLCDScrolling_Type())
slcSystemLCDScrolling.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLCDScrolling.setStatus(_A)
class _SlcSystemLCDScrollDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_SlcSystemLCDScrollDelay_Type.__name__=_C
_SlcSystemLCDScrollDelay_Object=MibScalar
slcSystemLCDScrollDelay=_SlcSystemLCDScrollDelay_Object((1,3,6,1,4,1,244,1,1,6,23),_SlcSystemLCDScrollDelay_Type())
slcSystemLCDScrollDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLCDScrollDelay.setStatus(_A)
if mibBuilder.loadTexts:slcSystemLCDScrollDelay.setUnits(_E)
class _SlcSystemLCDIdleDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_SlcSystemLCDIdleDelay_Type.__name__=_C
_SlcSystemLCDIdleDelay_Object=MibScalar
slcSystemLCDIdleDelay=_SlcSystemLCDIdleDelay_Object((1,3,6,1,4,1,244,1,1,6,24),_SlcSystemLCDIdleDelay_Type())
slcSystemLCDIdleDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemLCDIdleDelay.setStatus(_A)
if mibBuilder.loadTexts:slcSystemLCDIdleDelay.setUnits(_E)
_SlcSystemInternalTemp_Type=Integer32
_SlcSystemInternalTemp_Object=MibScalar
slcSystemInternalTemp=_SlcSystemInternalTemp_Object((1,3,6,1,4,1,244,1,1,6,25),_SlcSystemInternalTemp_Type())
slcSystemInternalTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemInternalTemp.setStatus(_A)
if mibBuilder.loadTexts:slcSystemInternalTemp.setUnits(_K)
class _SlcSystemWebProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tlsv1SSLv3',1),('tlsv1SSLv3SSLv2',2)))
_SlcSystemWebProtocol_Type.__name__=_C
_SlcSystemWebProtocol_Object=MibScalar
slcSystemWebProtocol=_SlcSystemWebProtocol_Object((1,3,6,1,4,1,244,1,1,6,26),_SlcSystemWebProtocol_Type())
slcSystemWebProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebProtocol.setStatus(_A)
class _SlcSystemWebCipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('highMedium',1),('highMediumLow',2)))
_SlcSystemWebCipher_Type.__name__=_C
_SlcSystemWebCipher_Object=MibScalar
slcSystemWebCipher=_SlcSystemWebCipher_Object((1,3,6,1,4,1,244,1,1,6,27),_SlcSystemWebCipher_Type())
slcSystemWebCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebCipher.setStatus(_A)
_SlcSystemModelString_Type=OctetString
_SlcSystemModelString_Object=MibScalar
slcSystemModelString=_SlcSystemModelString_Object((1,3,6,1,4,1,244,1,1,6,28),_SlcSystemModelString_Type())
slcSystemModelString.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemModelString.setStatus(_A)
_SlcSystemWebGroup_Type=OctetString
_SlcSystemWebGroup_Object=MibScalar
slcSystemWebGroup=_SlcSystemWebGroup_Object((1,3,6,1,4,1,244,1,1,6,29),_SlcSystemWebGroup_Type())
slcSystemWebGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebGroup.setStatus(_A)
_SlcSystemWebInterface_Type=OctetString
_SlcSystemWebInterface_Object=MibScalar
slcSystemWebInterface=_SlcSystemWebInterface_Object((1,3,6,1,4,1,244,1,1,6,30),_SlcSystemWebInterface_Type())
slcSystemWebInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebInterface.setStatus(_A)
_SlcSystemWebBanner_Type=OctetString
_SlcSystemWebBanner_Object=MibScalar
slcSystemWebBanner=_SlcSystemWebBanner_Object((1,3,6,1,4,1,244,1,1,6,31),_SlcSystemWebBanner_Type())
slcSystemWebBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebBanner.setStatus(_A)
_SlcSystemInternalTempLow_Type=Integer32
_SlcSystemInternalTempLow_Object=MibScalar
slcSystemInternalTempLow=_SlcSystemInternalTempLow_Object((1,3,6,1,4,1,244,1,1,6,32),_SlcSystemInternalTempLow_Type())
slcSystemInternalTempLow.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemInternalTempLow.setStatus(_A)
if mibBuilder.loadTexts:slcSystemInternalTempLow.setUnits(_K)
_SlcSystemInternalTempHigh_Type=Integer32
_SlcSystemInternalTempHigh_Object=MibScalar
slcSystemInternalTempHigh=_SlcSystemInternalTempHigh_Object((1,3,6,1,4,1,244,1,1,6,33),_SlcSystemInternalTempHigh_Type())
slcSystemInternalTempHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemInternalTempHigh.setStatus(_A)
if mibBuilder.loadTexts:slcSystemInternalTempHigh.setUnits(_K)
_SlcSystemCalibrateTemp_Type=Integer32
_SlcSystemCalibrateTemp_Object=MibScalar
slcSystemCalibrateTemp=_SlcSystemCalibrateTemp_Object((1,3,6,1,4,1,244,1,1,6,34),_SlcSystemCalibrateTemp_Type())
slcSystemCalibrateTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemCalibrateTemp.setStatus(_A)
if mibBuilder.loadTexts:slcSystemCalibrateTemp.setUnits(_K)
_SlcSystemWebServer_Type=EnabledState
_SlcSystemWebServer_Object=MibScalar
slcSystemWebServer=_SlcSystemWebServer_Object((1,3,6,1,4,1,244,1,1,6,35),_SlcSystemWebServer_Type())
slcSystemWebServer.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSystemWebServer.setStatus(_A)
_SlcEventObjects_ObjectIdentity=ObjectIdentity
slcEventObjects=_SlcEventObjects_ObjectIdentity((1,3,6,1,4,1,244,1,1,7))
class _SlcPowerSupplyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('powerSupplyA',1),('powerSupplyB',2),('primaryInlet',3),('secondaryInlet',4)))
_SlcPowerSupplyId_Type.__name__=_C
_SlcPowerSupplyId_Object=MibScalar
slcPowerSupplyId=_SlcPowerSupplyId_Object((1,3,6,1,4,1,244,1,1,7,1),_SlcPowerSupplyId_Type())
slcPowerSupplyId.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPowerSupplyId.setStatus(_A)
class _SlcPowerSupplyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerSupplyFailed',1),('powerSupplyRestored',2)))
_SlcPowerSupplyAction_Type.__name__=_C
_SlcPowerSupplyAction_Object=MibScalar
slcPowerSupplyAction=_SlcPowerSupplyAction_Object((1,3,6,1,4,1,244,1,1,7,2),_SlcPowerSupplyAction_Type())
slcPowerSupplyAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPowerSupplyAction.setStatus(_A)
_SlcDevPortNumBytes_Type=Integer32
_SlcDevPortNumBytes_Object=MibScalar
slcDevPortNumBytes=_SlcDevPortNumBytes_Object((1,3,6,1,4,1,244,1,1,7,3),_SlcDevPortNumBytes_Type())
slcDevPortNumBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortNumBytes.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortNumBytes.setUnits(_P)
_SlcDevPortData_Type=OctetString
_SlcDevPortData_Object=MibScalar
slcDevPortData=_SlcDevPortData_Object((1,3,6,1,4,1,244,1,1,7,4),_SlcDevPortData_Type())
slcDevPortData.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortData.setStatus(_A)
_SlcDevPortStartByte_Type=Integer32
_SlcDevPortStartByte_Object=MibScalar
slcDevPortStartByte=_SlcDevPortStartByte_Object((1,3,6,1,4,1,244,1,1,7,5),_SlcDevPortStartByte_Type())
slcDevPortStartByte.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortStartByte.setStatus(_A)
_SlcDevPortTimeFrame_Type=Integer32
_SlcDevPortTimeFrame_Object=MibScalar
slcDevPortTimeFrame=_SlcDevPortTimeFrame_Object((1,3,6,1,4,1,244,1,1,7,6),_SlcDevPortTimeFrame_Type())
slcDevPortTimeFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortTimeFrame.setStatus(_A)
if mibBuilder.loadTexts:slcDevPortTimeFrame.setUnits(_E)
class _SlcDevPortDeviceErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lowPower',1),('damageOrTamper',2)))
_SlcDevPortDeviceErrorStatus_Type.__name__=_C
_SlcDevPortDeviceErrorStatus_Object=MibScalar
slcDevPortDeviceErrorStatus=_SlcDevPortDeviceErrorStatus_Object((1,3,6,1,4,1,244,1,1,7,7),_SlcDevPortDeviceErrorStatus_Type())
slcDevPortDeviceErrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortDeviceErrorStatus.setStatus(_A)
_SlcHostname_Type=OctetString
_SlcHostname_Object=MibScalar
slcHostname=_SlcHostname_Object((1,3,6,1,4,1,244,1,1,7,8),_SlcHostname_Type())
slcHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:slcHostname.setStatus(_A)
class _SlcPCCardSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AI,1),(_AJ,2)))
_SlcPCCardSlot_Type.__name__=_C
_SlcPCCardSlot_Object=MibScalar
slcPCCardSlot=_SlcPCCardSlot_Object((1,3,6,1,4,1,244,1,1,7,9),_SlcPCCardSlot_Type())
slcPCCardSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardSlot.setStatus(_A)
class _SlcPCCardAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cardInserted',1),('cardRemoved',2)))
_SlcPCCardAction_Type.__name__=_C
_SlcPCCardAction_Object=MibScalar
slcPCCardAction=_SlcPCCardAction_Object((1,3,6,1,4,1,244,1,1,7,10),_SlcPCCardAction_Type())
slcPCCardAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardAction.setStatus(_A)
class _SlcPCCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6)))
_SlcPCCardType_Type.__name__=_C
_SlcPCCardType_Object=MibScalar
slcPCCardType=_SlcPCCardType_Object((1,3,6,1,4,1,244,1,1,7,11),_SlcPCCardType_Type())
slcPCCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcPCCardType.setStatus(_A)
class _SlcUSBAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AV,1),(_AW,2),('noModemDialTone',3)))
_SlcUSBAction_Type.__name__=_C
_SlcUSBAction_Object=MibScalar
slcUSBAction=_SlcUSBAction_Object((1,3,6,1,4,1,244,1,1,7,12),_SlcUSBAction_Type())
slcUSBAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcUSBAction.setStatus(_A)
class _SlcUSBType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6)))
_SlcUSBType_Type.__name__=_C
_SlcUSBType_Object=MibScalar
slcUSBType=_SlcUSBType_Object((1,3,6,1,4,1,244,1,1,7,13),_SlcUSBType_Type())
slcUSBType.setMaxAccess(_B)
if mibBuilder.loadTexts:slcUSBType.setStatus(_A)
class _SlcDevPortErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dataDrop',1),('invalidIOConfiguration',2),('errorIOModules',3)))
_SlcDevPortErrorStatus_Type.__name__=_C
_SlcDevPortErrorStatus_Object=MibScalar
slcDevPortErrorStatus=_SlcDevPortErrorStatus_Object((1,3,6,1,4,1,244,1,1,7,14),_SlcDevPortErrorStatus_Type())
slcDevPortErrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slcDevPortErrorStatus.setStatus(_A)
class _SlcSDCardAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AV,1),(_AW,2)))
_SlcSDCardAction_Type.__name__=_C
_SlcSDCardAction_Object=MibScalar
slcSDCardAction=_SlcSDCardAction_Object((1,3,6,1,4,1,244,1,1,7,15),_SlcSDCardAction_Type())
slcSDCardAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcSDCardAction.setStatus(_A)
_SlcRPMAction_Type=OctetString
_SlcRPMAction_Object=MibScalar
slcRPMAction=_SlcRPMAction_Object((1,3,6,1,4,1,244,1,1,7,16),_SlcRPMAction_Type())
slcRPMAction.setMaxAccess(_B)
if mibBuilder.loadTexts:slcRPMAction.setStatus(_A)
_SlcEventHost_Type=OctetString
_SlcEventHost_Object=MibScalar
slcEventHost=_SlcEventHost_Object((1,3,6,1,4,1,244,1,1,7,17),_SlcEventHost_Type())
slcEventHost.setMaxAccess(_B)
if mibBuilder.loadTexts:slcEventHost.setStatus(_A)
slcEventPowerSupply=NotificationType((1,3,6,1,4,1,244,1,1,0,1))
slcEventPowerSupply.setObjects(*((_D,_AX),(_D,_AY)))
if mibBuilder.loadTexts:slcEventPowerSupply.setStatus(_A)
slcEventSysadminPassword=NotificationType((1,3,6,1,4,1,244,1,1,0,2))
if mibBuilder.loadTexts:slcEventSysadminPassword.setStatus(_A)
slcEventSLCShutdown=NotificationType((1,3,6,1,4,1,244,1,1,0,3))
if mibBuilder.loadTexts:slcEventSLCShutdown.setStatus(_A)
slcEventDevicePortData=NotificationType((1,3,6,1,4,1,244,1,1,0,4))
slcEventDevicePortData.setObjects(*((_D,_J),(_D,_h),(_D,_AZ),(_D,_Aa),(_D,_Ab)))
if mibBuilder.loadTexts:slcEventDevicePortData.setStatus(_A)
slcEventDevicePortSLMData=NotificationType((1,3,6,1,4,1,244,1,1,0,5))
slcEventDevicePortSLMData.setObjects(*((_D,_J),(_D,_h),(_D,_Ac)))
if mibBuilder.loadTexts:slcEventDevicePortSLMData.setStatus(_A)
slcEventDevicePortSLMConfig=NotificationType((1,3,6,1,4,1,244,1,1,0,6))
slcEventDevicePortSLMConfig.setObjects(*((_D,_J),(_D,_h),(_D,_Ad)))
if mibBuilder.loadTexts:slcEventDevicePortSLMConfig.setStatus(_A)
slcEventDevicePortDeviceLowTemp=NotificationType((1,3,6,1,4,1,244,1,1,0,7))
slcEventDevicePortDeviceLowTemp.setObjects(*((_D,_J),(_D,_z),(_D,_Ae)))
if mibBuilder.loadTexts:slcEventDevicePortDeviceLowTemp.setStatus(_A)
slcEventDevicePortDeviceHighTemp=NotificationType((1,3,6,1,4,1,244,1,1,0,8))
slcEventDevicePortDeviceHighTemp.setObjects(*((_D,_J),(_D,_z),(_D,_Af)))
if mibBuilder.loadTexts:slcEventDevicePortDeviceHighTemp.setStatus(_A)
slcEventDevicePortDeviceLowHumidity=NotificationType((1,3,6,1,4,1,244,1,1,0,9))
slcEventDevicePortDeviceLowHumidity.setObjects(*((_D,_J),(_D,_A0),(_D,_Ag)))
if mibBuilder.loadTexts:slcEventDevicePortDeviceLowHumidity.setStatus(_A)
slcEventDevicePortDeviceHighHumidity=NotificationType((1,3,6,1,4,1,244,1,1,0,10))
slcEventDevicePortDeviceHighHumidity.setObjects(*((_D,_J),(_D,_A0),(_D,_Ah)))
if mibBuilder.loadTexts:slcEventDevicePortDeviceHighHumidity.setStatus(_A)
slcEventDevicePortDeviceError=NotificationType((1,3,6,1,4,1,244,1,1,0,11))
slcEventDevicePortDeviceError.setObjects(*((_D,_J),(_D,_Ai)))
if mibBuilder.loadTexts:slcEventDevicePortDeviceError.setStatus(_A)
slcEventPCCardAction=NotificationType((1,3,6,1,4,1,244,1,1,0,12))
slcEventPCCardAction.setObjects(*((_D,_Aj),(_D,_Ak),(_D,_Al)))
if mibBuilder.loadTexts:slcEventPCCardAction.setStatus(_A)
slcEventSLCInternalTemp=NotificationType((1,3,6,1,4,1,244,1,1,0,13))
slcEventSLCInternalTemp.setObjects((_D,_Am))
if mibBuilder.loadTexts:slcEventSLCInternalTemp.setStatus(_A)
slcEventUSBAction=NotificationType((1,3,6,1,4,1,244,1,1,0,14))
slcEventUSBAction.setObjects(*((_D,_x),(_D,_An),(_D,_Ao)))
if mibBuilder.loadTexts:slcEventUSBAction.setStatus(_A)
slcEventDevicePortError=NotificationType((1,3,6,1,4,1,244,1,1,0,15))
slcEventDevicePortError.setObjects(*((_D,_J),(_D,_Ap)))
if mibBuilder.loadTexts:slcEventDevicePortError.setStatus(_A)
slcEventSDCardAction=NotificationType((1,3,6,1,4,1,244,1,1,0,16))
slcEventSDCardAction.setObjects((_D,_Aq))
if mibBuilder.loadTexts:slcEventSDCardAction.setStatus(_A)
slcEventNoDialToneAlarm=NotificationType((1,3,6,1,4,1,244,1,1,0,17))
if mibBuilder.loadTexts:slcEventNoDialToneAlarm.setStatus(_A)
slcEventRPMAction=NotificationType((1,3,6,1,4,1,244,1,1,0,18))
slcEventRPMAction.setObjects(*((_D,_Ar),(_D,_As)))
if mibBuilder.loadTexts:slcEventRPMAction.setStatus(_A)
slcEventPingHostFails=NotificationType((1,3,6,1,4,1,244,1,1,0,19))
slcEventPingHostFails.setObjects((_D,_At))
if mibBuilder.loadTexts:slcEventPingHostFails.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'EnabledState':EnabledState,'AuthOrder':AuthOrder,'SyslogLevel':SyslogLevel,'UserGroup':UserGroup,'UserRights':UserRights,'TimeoutDataDirection':TimeoutDataDirection,_AP:RPMTowerIndex,_AT:RPMOutletIndex,'slc':slc,'slcEvents':slcEvents,'slcEventPowerSupply':slcEventPowerSupply,'slcEventSysadminPassword':slcEventSysadminPassword,'slcEventSLCShutdown':slcEventSLCShutdown,'slcEventDevicePortData':slcEventDevicePortData,'slcEventDevicePortSLMData':slcEventDevicePortSLMData,'slcEventDevicePortSLMConfig':slcEventDevicePortSLMConfig,'slcEventDevicePortDeviceLowTemp':slcEventDevicePortDeviceLowTemp,'slcEventDevicePortDeviceHighTemp':slcEventDevicePortDeviceHighTemp,'slcEventDevicePortDeviceLowHumidity':slcEventDevicePortDeviceLowHumidity,'slcEventDevicePortDeviceHighHumidity':slcEventDevicePortDeviceHighHumidity,'slcEventDevicePortDeviceError':slcEventDevicePortDeviceError,'slcEventPCCardAction':slcEventPCCardAction,'slcEventSLCInternalTemp':slcEventSLCInternalTemp,'slcEventUSBAction':slcEventUSBAction,'slcEventDevicePortError':slcEventDevicePortError,'slcEventSDCardAction':slcEventSDCardAction,'slcEventNoDialToneAlarm':slcEventNoDialToneAlarm,'slcEventRPMAction':slcEventRPMAction,'slcEventPingHostFails':slcEventPingHostFails,'slcNetwork':slcNetwork,'slcNetEth':slcNetEth,'slcNetEthIfNumber':slcNetEthIfNumber,'slcNetEthIfTable':slcNetEthIfTable,'slcNetEthIfEntry':slcNetEthIfEntry,_A1:slcNetEthIfIndex,'slcNetEthIfSource':slcNetEthIfSource,'slcNetEthIfMode':slcNetEthIfMode,'slcNetEthIfIPv6Addr':slcNetEthIfIPv6Addr,'slcNetEthIfIPv6PrefixLength':slcNetEthIfIPv6PrefixLength,'slcNetEthIfMTU':slcNetEthIfMTU,'slcNetEthIfMacAddress':slcNetEthIfMacAddress,'slcNetEthGateway':slcNetEthGateway,'slcNetEthGatewayPrecedence':slcNetEthGatewayPrecedence,'slcNetEthKeepaliveStartProbes':slcNetEthKeepaliveStartProbes,'slcNetEthKeepaliveNumberOfProbes':slcNetEthKeepaliveNumberOfProbes,'slcNetEthKeepaliveInterval':slcNetEthKeepaliveInterval,'slcNetEthIPForwarding':slcNetEthIPForwarding,'slcNetEthDNS1':slcNetEthDNS1,'slcNetEthDNS2':slcNetEthDNS2,'slcNetEthDNS3':slcNetEthDNS3,'slcNetEthDomain':slcNetEthDomain,'slcNetEthAlternateGateway':slcNetEthAlternateGateway,'slcNetEthPingIPAddress':slcNetEthPingIPAddress,'slcNetEthPingInterface':slcNetEthPingInterface,'slcNetEthPingDelay':slcNetEthPingDelay,'slcNetEthPingFailed':slcNetEthPingFailed,'slcNetEthBonding':slcNetEthBonding,'slcNetEthIPv6':slcNetEthIPv6,'slcNetEthGatewayIPv6':slcNetEthGatewayIPv6,'slcNetEthDNS1IPv6':slcNetEthDNS1IPv6,'slcNetEthDNS2IPv6':slcNetEthDNS2IPv6,'slcNetEthDNS3IPv6':slcNetEthDNS3IPv6,'slcNetEthPreferIPv4DNS':slcNetEthPreferIPv4DNS,'slcNetFirewall':slcNetFirewall,'slcNetFirewallState':slcNetFirewallState,'slcNetFirewallReject':slcNetFirewallReject,'slcNetFirewallPing':slcNetFirewallPing,'slcNetFirewallSSH':slcNetFirewallSSH,'slcNetFirewallTelnet':slcNetFirewallTelnet,'slcNetFirewallHTTP':slcNetFirewallHTTP,'slcNetFirewallHTTPS':slcNetFirewallHTTPS,'slcNetFirewallSMBCIFS':slcNetFirewallSMBCIFS,'slcNetFirewallRulesetNumber':slcNetFirewallRulesetNumber,'slcNetFirewallRulesetTable':slcNetFirewallRulesetTable,'slcNetFirewallRulesetEntry':slcNetFirewallRulesetEntry,_A2:slcNetFirewallRulesetIndex,'slcNetFirewallRulesetName':slcNetFirewallRulesetName,'slcNetFirewallRulesetNumRules':slcNetFirewallRulesetNumRules,'slcNetFirewallRulesetRules':slcNetFirewallRulesetRules,'slcNetFirewallMappingNumber':slcNetFirewallMappingNumber,'slcNetFirewallMappingTable':slcNetFirewallMappingTable,'slcNetFirewallMappingEntry':slcNetFirewallMappingEntry,_A3:slcNetFirewallMappingIndex,'slcNetFirewallMappingIfac':slcNetFirewallMappingIfac,'slcNetFirewallMappingIfacId':slcNetFirewallMappingIfacId,'slcNetFirewallMappingRuleset':slcNetFirewallMappingRuleset,'slcNetRouting':slcNetRouting,'slcNetRouteRIPState':slcNetRouteRIPState,'slcNetRouteRIPVersion':slcNetRouteRIPVersion,'slcNetRouteStaticState':slcNetRouteStaticState,'slcNetRouteStaticNumber':slcNetRouteStaticNumber,'slcNetRouteStaticTable':slcNetRouteStaticTable,'slcNetRouteStaticEntry':slcNetRouteStaticEntry,_A8:slcNetRouteStaticIndex,'slcNetRouteStaticIP':slcNetRouteStaticIP,'slcNetRouteStaticMask':slcNetRouteStaticMask,'slcNetRouteStaticGateway':slcNetRouteStaticGateway,'slcNetVPN':slcNetVPN,'slcNetVPNTunnel':slcNetVPNTunnel,'slcNetVPNStatus':slcNetVPNStatus,'slcNetVPNName':slcNetVPNName,'slcNetVPNEthPort':slcNetVPNEthPort,'slcNetVPNRemoteHost':slcNetVPNRemoteHost,'slcNetVPNRemoteId':slcNetVPNRemoteId,'slcNetVPNRemoteHop':slcNetVPNRemoteHop,'slcNetVPNRemoteSubnet':slcNetVPNRemoteSubnet,'slcNetVPNLocalId':slcNetVPNLocalId,'slcNetVPNLocalHop':slcNetVPNLocalHop,'slcNetVPNLocalSubnet':slcNetVPNLocalSubnet,'slcNetVPNIKENegotiation':slcNetVPNIKENegotiation,'slcNetVPNIKEEncryption':slcNetVPNIKEEncryption,'slcNetVPNIKEAuthentication':slcNetVPNIKEAuthentication,'slcNetVPNIKEDHGroup':slcNetVPNIKEDHGroup,'slcNetVPNESPEncryption':slcNetVPNESPEncryption,'slcNetVPNESPAuthentication':slcNetVPNESPAuthentication,'slcNetVPNESPDHGroup':slcNetVPNESPDHGroup,'slcNetVPNAuthentication':slcNetVPNAuthentication,'slcNetVPNPerfectForwardSecrecy':slcNetVPNPerfectForwardSecrecy,'slcNetVPNModeConfigClient':slcNetVPNModeConfigClient,'slcNetVPNXAUTHClient':slcNetVPNXAUTHClient,'slcNetVPNXAUTHClientLogin':slcNetVPNXAUTHClientLogin,'slcNetSecurity':slcNetSecurity,'slcNetSecurityFIPSMode':slcNetSecurityFIPSMode,'slcServices':slcServices,'slcServNTP':slcServNTP,'slcServNTPState':slcServNTPState,'slcServNTPSynchronize':slcServNTPSynchronize,'slcServNTPPoll':slcServNTPPoll,'slcServNTPServer':slcServNTPServer,'slcServNTPLocalServer2':slcServNTPLocalServer2,'slcServNTPLocalServer3':slcServNTPLocalServer3,'slcServNTPServerIPv6':slcServNTPServerIPv6,'slcServNTPLocalServer2IPv6':slcServNTPLocalServer2IPv6,'slcServNTPLocalServer3IPv6':slcServNTPLocalServer3IPv6,'slcServSyslog':slcServSyslog,'slcServSysNetworkLevel':slcServSysNetworkLevel,'slcServSysServicesLevel':slcServSysServicesLevel,'slcServSysAuthLevel':slcServSysAuthLevel,'slcServSysDevPortLevel':slcServSysDevPortLevel,'slcServSysDiagLevel':slcServSysDiagLevel,'slcServSysGeneralLevel':slcServSysGeneralLevel,'slcServSysRemoteServer':slcServSysRemoteServer,'slcServSysRemoteServer2':slcServSysRemoteServer2,'slcServSysRemoteServerIPv6':slcServSysRemoteServerIPv6,'slcServSysRemoteServer2IPv6':slcServSysRemoteServer2IPv6,'slcServSysRPMLogSize':slcServSysRPMLogSize,'slcServSysOtherLogSize':slcServSysOtherLogSize,'slcServAuditLog':slcServAuditLog,'slcServAuditState':slcServAuditState,'slcServAuditSize':slcServAuditSize,'slcServAuditIncludeCLI':slcServAuditIncludeCLI,'slcServAuditInSystemLog':slcServAuditInSystemLog,'slcServSSH':slcServSSH,'slcServSSHState':slcServSSHState,'slcServSSHTimeout':slcServSSHTimeout,'slcServSSHWebSSH':slcServSSHWebSSH,'slcServSSHPort':slcServSSHPort,'slcServSSHV1Incoming':slcServSSHV1Incoming,'slcServSSHTimeoutDataDirection':slcServSSHTimeoutDataDirection,'slcServSSHDSAKeys':slcServSSHDSAKeys,'slcServTelnet':slcServTelnet,'slcServTelnetState':slcServTelnetState,'slcServTelnetTimeout':slcServTelnetTimeout,'slcServTelnetWebTelnet':slcServTelnetWebTelnet,'slcServTelnetTelnetOut':slcServTelnetTelnetOut,'slcServTelnetTimeoutDataDirection':slcServTelnetTimeoutDataDirection,'slcServSNMP':slcServSNMP,'slcServSNMPState':slcServSNMPState,'slcServSNMPTraps':slcServSNMPTraps,'slcServSNMPNMS':slcServSNMPNMS,'slcServSNMPLocation':slcServSNMPLocation,'slcServSNMPContact':slcServSNMPContact,'slcServSNMPv3User':slcServSNMPv3User,'slcServSNMPReadOnlyCommunity':slcServSNMPReadOnlyCommunity,'slcServSNMPReadWriteCommunity':slcServSNMPReadWriteCommunity,'slcServSNMPTrapCommunity':slcServSNMPTrapCommunity,'slcServSNMPAlarmDelay':slcServSNMPAlarmDelay,'slcServSNMPv3ReadWriteUser':slcServSNMPv3ReadWriteUser,'slcServSNMPv3Security':slcServSNMPv3Security,'slcServSNMPv3Authentication':slcServSNMPv3Authentication,'slcServSNMPv3Encryption':slcServSNMPv3Encryption,'slcServSNMPv1v2':slcServSNMPv1v2,'slcServSNMPNMS2':slcServSNMPNMS2,'slcServSNMPNMSIPv6':slcServSNMPNMSIPv6,'slcServSNMPNMS2IPv6':slcServSNMPNMS2IPv6,'slcServSMTP':slcServSMTP,'slcServSMTPServer':slcServSMTPServer,'slcServSMTPSender':slcServSMTPSender,'slcServNFS':slcServNFS,'slcServNFSMountTable':slcServNFSMountTable,'slcServNFSMountEntry':slcServNFSMountEntry,_AA:slcServNFSMountIndex,'slcServNFSMountRemoteDir':slcServNFSMountRemoteDir,'slcServNFSMountLocalDir':slcServNFSMountLocalDir,'slcServNFSMountReadWrite':slcServNFSMountReadWrite,'slcServNFSMountMount':slcServNFSMountMount,'slcServCIFS':slcServCIFS,'slcServCIFSState':slcServCIFSState,'slcServCIFSEth1':slcServCIFSEth1,'slcServCIFSEth2':slcServCIFSEth2,'slcServCIFSWorkgroup':slcServCIFSWorkgroup,'slcServSLCNetwork':slcServSLCNetwork,'slcServSLCNetSearch':slcServSLCNetSearch,'slcServSLCNetNumber':slcServSLCNetNumber,'slcServSLCNetTable':slcServSLCNetTable,'slcServSLCNetEntry':slcServSLCNetEntry,_AB:slcServSLCNetIndex,'slcServSLCNetIP':slcServSLCNetIP,'slcServPhoneHome':slcServPhoneHome,'slcServPhoneHomeState':slcServPhoneHomeState,'slcServPhoneHomeIP':slcServPhoneHomeIP,'slcServHostList':slcServHostList,'slcServHostListNumber':slcServHostListNumber,'slcServHostListTable':slcServHostListTable,'slcServHostListEntry':slcServHostListEntry,_AC:slcServHostListIndex,'slcServHostListName':slcServHostListName,'slcServHostListRetryCount':slcServHostListRetryCount,'slcServHostListAuth':slcServHostListAuth,'slcServHostListNumHosts':slcServHostListNumHosts,'slcServHostListHosts':slcServHostListHosts,'slcServWebTerm':slcServWebTerm,'slcServWebTermDeployment':slcServWebTermDeployment,'slcServWebTermBufSize':slcServWebTermBufSize,'slcServSite':slcServSite,'slcServSiteNumber':slcServSiteNumber,'slcServSiteTable':slcServSiteTable,'slcServSiteEntry':slcServSiteEntry,_AD:slcServSiteIndex,'slcServSiteName':slcServSiteName,'slcServSitePort':slcServSitePort,'slcServSitePortId':slcServSitePortId,'slcServSiteLoginHost':slcServSiteLoginHost,'slcServSiteCHAPSecret':slcServSiteCHAPSecret,'slcServSiteTimeout':slcServSiteTimeout,'slcServSiteLocalIP':slcServSiteLocalIP,'slcServSiteRemoteIP':slcServSiteRemoteIP,'slcServSiteStaticRouteIP':slcServSiteStaticRouteIP,'slcServSiteStaticRouteMask':slcServSiteStaticRouteMask,'slcServSiteStaticRouteGateway':slcServSiteStaticRouteGateway,'slcServSiteDialoutNum':slcServSiteDialoutNum,'slcServSiteDialoutLogin':slcServSiteDialoutLogin,'slcServSiteDialback':slcServSiteDialback,'slcServSiteDialbackNum':slcServSiteDialbackNum,'slcServSiteDialbackDelay':slcServSiteDialbackDelay,'slcServSiteIdleTimeout':slcServSiteIdleTimeout,'slcServSiteRestartDelay':slcServSiteRestartDelay,'slcServSiteCBCPServerAllowNoCallback':slcServSiteCBCPServerAllowNoCallback,'slcServSiteNATState':slcServSiteNATState,'slcServSiteDialbackRetries':slcServSiteDialbackRetries,'slcAuth':slcAuth,'slcAuthLocal':slcAuthLocal,'slcAuthLocalNumber':slcAuthLocalNumber,'slcAuthLocalUsersTable':slcAuthLocalUsersTable,'slcAuthLocalUserEntry':slcAuthLocalUserEntry,_AE:slcAuthLocalUserIndex,'slcAuthLocalUserLogin':slcAuthLocalUserLogin,'slcAuthLocalUserUID':slcAuthLocalUserUID,'slcAuthLocalUserListenPorts':slcAuthLocalUserListenPorts,'slcAuthLocalUserDataPorts':slcAuthLocalUserDataPorts,'slcAuthLocalUserClearPorts':slcAuthLocalUserClearPorts,'slcAuthLocalUserEscapeSeq':slcAuthLocalUserEscapeSeq,'slcAuthLocalUserBreakSeq':slcAuthLocalUserBreakSeq,'slcAuthLocalUserMenu':slcAuthLocalUserMenu,'slcAuthLocalUserDialback':slcAuthLocalUserDialback,'slcAuthLocalUserDialbackNum':slcAuthLocalUserDialbackNum,'slcAuthLocalUserGroup':slcAuthLocalUserGroup,'slcAuthLocalUserRights':slcAuthLocalUserRights,'slcAuthLocalUserPwdExpires':slcAuthLocalUserPwdExpires,'slcAuthLocalUserChangePwd':slcAuthLocalUserChangePwd,'slcAuthLocalUserChangePwdNextLogin':slcAuthLocalUserChangePwdNextLogin,'slcAuthLocalState':slcAuthLocalState,'slcAuthLocalOrder':slcAuthLocalOrder,'slcAuthLocalComplexPasswords':slcAuthLocalComplexPasswords,'slcAuthLocalUseNextMethod':slcAuthLocalUseNextMethod,'slcAuthLocalAllowReuse':slcAuthLocalAllowReuse,'slcAuthLocalReuseHistory':slcAuthLocalReuseHistory,'slcAuthLocalPasswordLifetime':slcAuthLocalPasswordLifetime,'slcAuthLocalWarningPeriod':slcAuthLocalWarningPeriod,'slcAuthLocalMaxLoginAttempts':slcAuthLocalMaxLoginAttempts,'slcAuthLocalLockoutPeriod':slcAuthLocalLockoutPeriod,'slcAuthLocalMultipleSysadminLogins':slcAuthLocalMultipleSysadminLogins,'slcAuthLocalSysadminConsoleOnly':slcAuthLocalSysadminConsoleOnly,'slcAuthNIS':slcAuthNIS,'slcAuthNISState':slcAuthNISState,'slcAuthNISOrder':slcAuthNISOrder,'slcAuthNISDomain':slcAuthNISDomain,'slcAuthNISBroadcast':slcAuthNISBroadcast,'slcAuthNISMaster':slcAuthNISMaster,'slcAuthNISSlave1':slcAuthNISSlave1,'slcAuthNISSlave2':slcAuthNISSlave2,'slcAuthNISSlave3':slcAuthNISSlave3,'slcAuthNISGroup':slcAuthNISGroup,'slcAuthNISRights':slcAuthNISRights,'slcAuthNISMenu':slcAuthNISMenu,'slcAuthNISListenPorts':slcAuthNISListenPorts,'slcAuthNISDataPorts':slcAuthNISDataPorts,'slcAuthNISClearPorts':slcAuthNISClearPorts,'slcAuthNISSlave4':slcAuthNISSlave4,'slcAuthNISSlave5':slcAuthNISSlave5,'slcAuthNISEscapeSeq':slcAuthNISEscapeSeq,'slcAuthNISBreakSeq':slcAuthNISBreakSeq,'slcAuthNISDialback':slcAuthNISDialback,'slcAuthNISDialbackNum':slcAuthNISDialbackNum,'slcAuthLDAP':slcAuthLDAP,'slcAuthLDAPState':slcAuthLDAPState,'slcAuthLDAPOrder':slcAuthLDAPOrder,'slcAuthLDAPServer':slcAuthLDAPServer,'slcAuthLDAPBase':slcAuthLDAPBase,'slcAuthLDAPBindName':slcAuthLDAPBindName,'slcAuthLDAPPort':slcAuthLDAPPort,'slcAuthLDAPADSupport':slcAuthLDAPADSupport,'slcAuthLDAPGroup':slcAuthLDAPGroup,'slcAuthLDAPRights':slcAuthLDAPRights,'slcAuthLDAPMenu':slcAuthLDAPMenu,'slcAuthLDAPListenPorts':slcAuthLDAPListenPorts,'slcAuthLDAPDataPorts':slcAuthLDAPDataPorts,'slcAuthLDAPClearPorts':slcAuthLDAPClearPorts,'slcAuthLDAPEncrypt':slcAuthLDAPEncrypt,'slcAuthLDAPEscapeSeq':slcAuthLDAPEscapeSeq,'slcAuthLDAPBreakSeq':slcAuthLDAPBreakSeq,'slcAuthLDAPBindWithLogin':slcAuthLDAPBindWithLogin,'slcAuthLDAPUseLDAPSchema':slcAuthLDAPUseLDAPSchema,'slcAuthLDAPDialback':slcAuthLDAPDialback,'slcAuthLDAPDialbackNum':slcAuthLDAPDialbackNum,'slcAuthLDAPUserFilter':slcAuthLDAPUserFilter,'slcAuthLDAPGroupFilter':slcAuthLDAPGroupFilter,'slcAuthLDAPGroupMembershipAttr':slcAuthLDAPGroupMembershipAttr,'slcAuthLDAPGroupMembershipDN':slcAuthLDAPGroupMembershipDN,'slcAuthLDAPServer2':slcAuthLDAPServer2,'slcAuthLDAPServerIPv6':slcAuthLDAPServerIPv6,'slcAuthLDAPServer2IPv6':slcAuthLDAPServer2IPv6,'slcAuthRADIUS':slcAuthRADIUS,'slcAuthRADIUSState':slcAuthRADIUSState,'slcAuthRADIUSOrder':slcAuthRADIUSOrder,'slcAuthRADIUSTimeout':slcAuthRADIUSTimeout,'slcAuthRADIUSServerTable':slcAuthRADIUSServerTable,'slcAuthRADIUSServerEntry':slcAuthRADIUSServerEntry,_AF:slcAuthRADIUSServerIndex,'slcAuthRADIUSServer':slcAuthRADIUSServer,'slcAuthRADIUSPort':slcAuthRADIUSPort,'slcAuthRADIUSServerIPv6':slcAuthRADIUSServerIPv6,'slcAuthRADIUSGroup':slcAuthRADIUSGroup,'slcAuthRADIUSRights':slcAuthRADIUSRights,'slcAuthRADIUSMenu':slcAuthRADIUSMenu,'slcAuthRADIUSListenPorts':slcAuthRADIUSListenPorts,'slcAuthRADIUSDataPorts':slcAuthRADIUSDataPorts,'slcAuthRADIUSClearPorts':slcAuthRADIUSClearPorts,'slcAuthRADIUSEscapeSeq':slcAuthRADIUSEscapeSeq,'slcAuthRADIUSBreakSeq':slcAuthRADIUSBreakSeq,'slcAuthRADIUSDialback':slcAuthRADIUSDialback,'slcAuthRADIUSDialbackNum':slcAuthRADIUSDialbackNum,'slcAuthRADIUSUseVSA':slcAuthRADIUSUseVSA,'slcAuthKerberos':slcAuthKerberos,'slcAuthKerbState':slcAuthKerbState,'slcAuthKerbOrder':slcAuthKerbOrder,'slcAuthKerbRealm':slcAuthKerbRealm,'slcAuthKerbKDC':slcAuthKerbKDC,'slcAuthKerbKDCIP':slcAuthKerbKDCIP,'slcAuthKerbKDCPort':slcAuthKerbKDCPort,'slcAuthKerbUseLDAP':slcAuthKerbUseLDAP,'slcAuthKerbGroup':slcAuthKerbGroup,'slcAuthKerbRights':slcAuthKerbRights,'slcAuthKerbMenu':slcAuthKerbMenu,'slcAuthKerbListenPorts':slcAuthKerbListenPorts,'slcAuthKerbDataPorts':slcAuthKerbDataPorts,'slcAuthKerbClearPorts':slcAuthKerbClearPorts,'slcAuthKerbEscapeSeq':slcAuthKerbEscapeSeq,'slcAuthKerbBreakSeq':slcAuthKerbBreakSeq,'slcAuthKerbDialback':slcAuthKerbDialback,'slcAuthKerbDialbackNum':slcAuthKerbDialbackNum,'slcAuthKerbKDCIPv6':slcAuthKerbKDCIPv6,'slcAuthTACACS':slcAuthTACACS,'slcAuthTACACSState':slcAuthTACACSState,'slcAuthTACACSOrder':slcAuthTACACSOrder,'slcAuthTACACSServer':slcAuthTACACSServer,'slcAuthTACACSEncrypt':slcAuthTACACSEncrypt,'slcAuthTACACSGroup':slcAuthTACACSGroup,'slcAuthTACACSRights':slcAuthTACACSRights,'slcAuthTACACSMenu':slcAuthTACACSMenu,'slcAuthTACACSListenPorts':slcAuthTACACSListenPorts,'slcAuthTACACSDataPorts':slcAuthTACACSDataPorts,'slcAuthTACACSClearPorts':slcAuthTACACSClearPorts,'slcAuthTACACSServer2':slcAuthTACACSServer2,'slcAuthTACACSServer3':slcAuthTACACSServer3,'slcAuthTACACSEscapeSeq':slcAuthTACACSEscapeSeq,'slcAuthTACACSBreakSeq':slcAuthTACACSBreakSeq,'slcAuthTACACSDialback':slcAuthTACACSDialback,'slcAuthTACACSDialbackNum':slcAuthTACACSDialbackNum,'slcAuthTACACSAuthService':slcAuthTACACSAuthService,'slcAuthTACACSServerIPv6':slcAuthTACACSServerIPv6,'slcAuthTACACSServer2IPv6':slcAuthTACACSServer2IPv6,'slcAuthTACACSServer3IPv6':slcAuthTACACSServer3IPv6,'slcAuthRemote':slcAuthRemote,'slcAuthRemoteNumber':slcAuthRemoteNumber,'slcAuthRemoteUsersTable':slcAuthRemoteUsersTable,'slcAuthRemoteUserEntry':slcAuthRemoteUserEntry,_AG:slcAuthRemoteUserIndex,'slcAuthRemoteUserLogin':slcAuthRemoteUserLogin,'slcAuthRemoteUserGroup':slcAuthRemoteUserGroup,'slcAuthRemoteUserRights':slcAuthRemoteUserRights,'slcAuthRemoteUserListenPorts':slcAuthRemoteUserListenPorts,'slcAuthRemoteUserDataPorts':slcAuthRemoteUserDataPorts,'slcAuthRemoteUserClearPorts':slcAuthRemoteUserClearPorts,'slcAuthRemoteUserEscapeSeq':slcAuthRemoteUserEscapeSeq,'slcAuthRemoteUserBreakSeq':slcAuthRemoteUserBreakSeq,'slcAuthRemoteUserMenu':slcAuthRemoteUserMenu,'slcAuthRemoteUserLocked':slcAuthRemoteUserLocked,'slcAuthRemoteUserDialback':slcAuthRemoteUserDialback,'slcAuthRemoteUserDialbackNum':slcAuthRemoteUserDialbackNum,'slcAuthRemoteAuthListOnly':slcAuthRemoteAuthListOnly,'slcAuthGroups':slcAuthGroups,'slcAuthGroupsNumber':slcAuthGroupsNumber,'slcAuthGroupsTable':slcAuthGroupsTable,'slcAuthGroupEntry':slcAuthGroupEntry,_AH:slcAuthGroupIndex,'slcAuthGroupName':slcAuthGroupName,'slcAuthGroupRights':slcAuthGroupRights,'slcAuthGroupListenPorts':slcAuthGroupListenPorts,'slcAuthGroupDataPorts':slcAuthGroupDataPorts,'slcAuthGroupClearPorts':slcAuthGroupClearPorts,'slcAuthGroupEscapeSeq':slcAuthGroupEscapeSeq,'slcAuthGroupBreakSeq':slcAuthGroupBreakSeq,'slcAuthGroupMenu':slcAuthGroupMenu,'slcAuthGroupDialback':slcAuthGroupDialback,'slcAuthGroupDialbackNum':slcAuthGroupDialbackNum,'slcDevices':slcDevices,'slcDevConsolePort':slcDevConsolePort,'slcDevConBaud':slcDevConBaud,'slcDevConDataBits':slcDevConDataBits,'slcDevConStopBits':slcDevConStopBits,'slcDevConParity':slcDevConParity,'slcDevConFlowControl':slcDevConFlowControl,'slcDevConTimeout':slcDevConTimeout,'slcDevConShowLines':slcDevConShowLines,'slcDevConNumberShowLines':slcDevConNumberShowLines,'slcDevConGroup':slcDevConGroup,'slcDevDevicePorts':slcDevDevicePorts,'slcDevPortGlobal':slcDevPortGlobal,'slcDevGlobalListenPorts':slcDevGlobalListenPorts,'slcDevGlobalDataPorts':slcDevGlobalDataPorts,'slcDevGlobalClearPorts':slcDevGlobalClearPorts,'slcDevGlobalStartTelnetPort':slcDevGlobalStartTelnetPort,'slcDevGlobalStartSSHPort':slcDevGlobalStartSSHPort,'slcDevGlobalStartTCPPort':slcDevGlobalStartTCPPort,'slcDevGlobalMaxDirect':slcDevGlobalMaxDirect,'slcDevPortConfig':slcDevPortConfig,'slcDevPortCfgNumber':slcDevPortCfgNumber,'slcDevPortCfgTable':slcDevPortCfgTable,'slcDevPortCfgEntry':slcDevPortCfgEntry,_J:slcDevPortId,'slcDevPortCfgName':slcDevPortCfgName,'slcDevPortCfgDevice':slcDevPortCfgDevice,'slcDevPortCfgDevLogin':slcDevPortCfgDevLogin,'slcDevPortCfgBreakSeq':slcDevPortCfgBreakSeq,'slcDevPortCfgTelnetState':slcDevPortCfgTelnetState,'slcDevPortCfgTelnetPort':slcDevPortCfgTelnetPort,'slcDevPortCfgTelnetAuth':slcDevPortCfgTelnetAuth,'slcDevPortCfgSSHState':slcDevPortCfgSSHState,'slcDevPortCfgSSHPort':slcDevPortCfgSSHPort,'slcDevPortCfgSSHAuth':slcDevPortCfgSSHAuth,'slcDevPortCfgTCPState':slcDevPortCfgTCPState,'slcDevPortCfgTCPPort':slcDevPortCfgTCPPort,'slcDevPortCfgTCPAuth':slcDevPortCfgTCPAuth,'slcDevPortCfgIP':slcDevPortCfgIP,'slcDevPortCfgBaud':slcDevPortCfgBaud,'slcDevPortCfgDataBits':slcDevPortCfgDataBits,'slcDevPortCfgStopBits':slcDevPortCfgStopBits,'slcDevPortCfgParity':slcDevPortCfgParity,'slcDevPortCfgFlowControl':slcDevPortCfgFlowControl,'slcDevPortCfgLogins':slcDevPortCfgLogins,'slcDevPortCfgConnectDSR':slcDevPortCfgConnectDSR,'slcDevPortCfgDisconnectDSR':slcDevPortCfgDisconnectDSR,'slcDevPortCfgModemState':slcDevPortCfgModemState,'slcDevPortCfgModemMode':slcDevPortCfgModemMode,'slcDevPortCfgLocalIP':slcDevPortCfgLocalIP,'slcDevPortCfgRemoteIP':slcDevPortCfgRemoteIP,'slcDevPortCfgAuth':slcDevPortCfgAuth,'slcDevPortCfgCHAPHost':slcDevPortCfgCHAPHost,'slcDevPortCfgInitScript':slcDevPortCfgInitScript,'slcDevPortCfgTimeout':slcDevPortCfgTimeout,'slcDevPortCfgDialoutNum':slcDevPortCfgDialoutNum,'slcDevPortCfgDialoutLogin':slcDevPortCfgDialoutLogin,'slcDevPortCfgDialbackMode':slcDevPortCfgDialbackMode,'slcDevPortCfgDialbackNum':slcDevPortCfgDialbackNum,'slcDevPortCfgNATState':slcDevPortCfgNATState,'slcDevPortCfgLocalState':slcDevPortCfgLocalState,'slcDevPortCfgNFSFileState':slcDevPortCfgNFSFileState,'slcDevPortCfgNFSDir':slcDevPortCfgNFSDir,'slcDevPortCfgNFSMaxFiles':slcDevPortCfgNFSMaxFiles,'slcDevPortCfgNFSMaxSize':slcDevPortCfgNFSMaxSize,'slcDevPortCfgEmailState':slcDevPortCfgEmailState,'slcDevPortCfgEmailTrigger':slcDevPortCfgEmailTrigger,'slcDevPortCfgEmailByteThresh':slcDevPortCfgEmailByteThresh,'slcDevPortCfgEmailDelay':slcDevPortCfgEmailDelay,'slcDevPortCfgEmailRestartDelay':slcDevPortCfgEmailRestartDelay,_Aa:slcDevPortCfgEmailTextString,'slcDevPortCfgEmailTo':slcDevPortCfgEmailTo,'slcDevPortCfgEmailSubject':slcDevPortCfgEmailSubject,'slcDevPortCfgPCCardState':slcDevPortCfgPCCardState,'slcDevPortCfgPCCardLogTo':slcDevPortCfgPCCardLogTo,'slcDevPortCfgPCCardMaxFiles':slcDevPortCfgPCCardMaxFiles,'slcDevPortCfgPCCardMaxSize':slcDevPortCfgPCCardMaxSize,'slcDevPortCfgAction':slcDevPortCfgAction,'slcDevPortCfgEmailSend':slcDevPortCfgEmailSend,'slcDevPortCfgBanner':slcDevPortCfgBanner,'slcDevPortCfgIdleTimeout':slcDevPortCfgIdleTimeout,'slcDevPortCfgRestartDelay':slcDevPortCfgRestartDelay,'slcDevPortCfgCallerIdLogging':slcDevPortCfgCallerIdLogging,'slcDevPortCfgCallerIdATCmd':slcDevPortCfgCallerIdATCmd,'slcDevPortCfgDODAuth':slcDevPortCfgDODAuth,'slcDevPortCfgDODCHAPHost':slcDevPortCfgDODCHAPHost,'slcDevPortCfgSLMLoggingState':slcDevPortCfgSLMLoggingState,'slcDevPortCfgSLMNMS':slcDevPortCfgSLMNMS,'slcDevPortCfgSLMByteThresh':slcDevPortCfgSLMByteThresh,'slcDevPortCfgSLMTimeFrame':slcDevPortCfgSLMTimeFrame,'slcDevPortCfgWebColumns':slcDevPortCfgWebColumns,'slcDevPortCfgWebRows':slcDevPortCfgWebRows,'slcDevPortCfgSyslogState':slcDevPortCfgSyslogState,'slcDevPortCfgHostList':slcDevPortCfgHostList,_Ae:slcDevPortCfgDevLowTemp,_Af:slcDevPortCfgDevHighTemp,_z:slcDevPortCfgDevTemperature,_Ag:slcDevPortCfgDevLowHumidity,_Ah:slcDevPortCfgDevHighHumidity,_A0:slcDevPortCfgDevHumidity,'slcDevPortCfgDevTraps':slcDevPortCfgDevTraps,'slcDevPortCfgShowLines':slcDevPortCfgShowLines,'slcDevPortCfgNumberShowLines':slcDevPortCfgNumberShowLines,'slcDevPortCfgViewPortLog':slcDevPortCfgViewPortLog,'slcDevPortCfgPortLogSeq':slcDevPortCfgPortLogSeq,'slcDevPortCfgMaxDirectConnects':slcDevPortCfgMaxDirectConnects,'slcDevPortCfgTelnetTimeout':slcDevPortCfgTelnetTimeout,'slcDevPortCfgSSHTimeout':slcDevPortCfgSSHTimeout,'slcDevPortCfgTCPTimeout':slcDevPortCfgTCPTimeout,'slcDevPortCfgCBCPClientType':slcDevPortCfgCBCPClientType,'slcDevPortCfgCBCPServerAllowNoCallback':slcDevPortCfgCBCPServerAllowNoCallback,'slcDevPortCfgDialbackDelay':slcDevPortCfgDialbackDelay,'slcDevPortCfgUSBState':slcDevPortCfgUSBState,'slcDevPortCfgUSBLogTo':slcDevPortCfgUSBLogTo,'slcDevPortCfgUSBMaxFiles':slcDevPortCfgUSBMaxFiles,'slcDevPortCfgUSBMaxSize':slcDevPortCfgUSBMaxSize,'slcDevPortCfgCHAPAuthLocalUsers':slcDevPortCfgCHAPAuthLocalUsers,'slcDevPortCfgUseSites':slcDevPortCfgUseSites,'slcDevPortCfgDialbackRetries':slcDevPortCfgDialbackRetries,'slcDevPortCfgGroup':slcDevPortCfgGroup,'slcDevPortCfgIPMask':slcDevPortCfgIPMask,'slcDevPortCfgDevPrompt':slcDevPortCfgDevPrompt,'slcDevPortCfgDevNumOutlets':slcDevPortCfgDevNumOutlets,'slcDevPortCfgDevNumExpOutlets':slcDevPortCfgDevNumExpOutlets,'slcDevPortCfgReversePinout':slcDevPortCfgReversePinout,'slcDevPortCfgUSBVBUS':slcDevPortCfgUSBVBUS,'slcDevPortCfgAssertDTR':slcDevPortCfgAssertDTR,'slcDevPortCfgPortType':slcDevPortCfgPortType,'slcDevPortCfgTelnetTimeoutDataDirection':slcDevPortCfgTelnetTimeoutDataDirection,'slcDevPortCfgSSHTimeoutDataDirection':slcDevPortCfgSSHTimeoutDataDirection,'slcDevPortCfgTCPTimeoutDataDirection':slcDevPortCfgTCPTimeoutDataDirection,'slcDevPortCfgIdleTimeoutMessage':slcDevPortCfgIdleTimeoutMessage,'slcDevPortCfgNumberOfSessionsMessage':slcDevPortCfgNumberOfSessionsMessage,'slcDevPortCfgMinimizeLatency':slcDevPortCfgMinimizeLatency,'slcDevPortCfgTelnetSoftIAC':slcDevPortCfgTelnetSoftIAC,'slcDevPortCfgSendTermString':slcDevPortCfgSendTermString,'slcDevPortCfgTerminationString':slcDevPortCfgTerminationString,'slcDevPortCfgPowerManagementSeq':slcDevPortCfgPowerManagementSeq,'slcDevPortCfgPowerSupplies':slcDevPortCfgPowerSupplies,'slcDevPortCfgToggleDTR':slcDevPortCfgToggleDTR,'slcDevPortCfgTokenAction':slcDevPortCfgTokenAction,'slcDevPortCfgTokenSendString':slcDevPortCfgTokenSendString,'slcDevPortCfgTokenPowerSupply':slcDevPortCfgTokenPowerSupply,'slcDevPortCfgTokenPowerAction':slcDevPortCfgTokenPowerAction,'slcDevPortState':slcDevPortState,'slcDevPortStateNumber':slcDevPortStateNumber,'slcDevPortStateTable':slcDevPortStateTable,'slcDevPortStateEntry':slcDevPortStateEntry,_AL:slcDevPortStateIndex,'slcDevPortStateBytesInput':slcDevPortStateBytesInput,'slcDevPortStateBytesOutput':slcDevPortStateBytesOutput,'slcDevPortStateFramingErrors':slcDevPortStateFramingErrors,'slcDevPortStateParityErrors':slcDevPortStateParityErrors,'slcDevPortStateOverrunErrors':slcDevPortStateOverrunErrors,'slcDevPortStateFlowControlViolations':slcDevPortStateFlowControlViolations,'slcDevPortStateDSR':slcDevPortStateDSR,'slcDevPortStateDTR':slcDevPortStateDTR,'slcDevPortStateCTS':slcDevPortStateCTS,'slcDevPortStateRTS':slcDevPortStateRTS,'slcDevPortStateCD':slcDevPortStateCD,'slcDevPCCard':slcDevPCCard,'slcPCCardCfgTable':slcPCCardCfgTable,'slcPCCardCfgEntry':slcPCCardCfgEntry,_AM:slcPCCardCfgIndex,'slcPCCardCfgCardType':slcPCCardCfgCardType,'slcPCCardCfgCardId':slcPCCardCfgCardId,'slcPCCardCfgBaud':slcPCCardCfgBaud,'slcPCCardCfgDataBits':slcPCCardCfgDataBits,'slcPCCardCfgStopBits':slcPCCardCfgStopBits,'slcPCCardCfgParity':slcPCCardCfgParity,'slcPCCardCfgFlowControl':slcPCCardCfgFlowControl,'slcPCCardCfgModemState':slcPCCardCfgModemState,'slcPCCardCfgModemMode':slcPCCardCfgModemMode,'slcPCCardCfgLocalIP':slcPCCardCfgLocalIP,'slcPCCardCfgRemoteIP':slcPCCardCfgRemoteIP,'slcPCCardCfgAuth':slcPCCardCfgAuth,'slcPCCardCfgCHAPHost':slcPCCardCfgCHAPHost,'slcPCCardCfgInitScript':slcPCCardCfgInitScript,'slcPCCardCfgTimeout':slcPCCardCfgTimeout,'slcPCCardCfgDialoutNum':slcPCCardCfgDialoutNum,'slcPCCardCfgDialoutLogin':slcPCCardCfgDialoutLogin,'slcPCCardCfgDialbackMode':slcPCCardCfgDialbackMode,'slcPCCardCfgDialbackNum':slcPCCardCfgDialbackNum,'slcPCCardCfgNATState':slcPCCardCfgNATState,'slcPCCardCfgStorageFS':slcPCCardCfgStorageFS,'slcPCCardCfgISDNChannel':slcPCCardCfgISDNChannel,'slcPCCardCfgISDNChannelNum':slcPCCardCfgISDNChannelNum,'slcPCCardCfgTelnetState':slcPCCardCfgTelnetState,'slcPCCardCfgTelnetPort':slcPCCardCfgTelnetPort,'slcPCCardCfgTelnetAuth':slcPCCardCfgTelnetAuth,'slcPCCardCfgSSHState':slcPCCardCfgSSHState,'slcPCCardCfgSSHPort':slcPCCardCfgSSHPort,'slcPCCardCfgSSHAuth':slcPCCardCfgSSHAuth,'slcPCCardCfgTCPState':slcPCCardCfgTCPState,'slcPCCardCfgTCPPort':slcPCCardCfgTCPPort,'slcPCCardCfgTCPAuth':slcPCCardCfgTCPAuth,'slcPCCardCfgGSMPIN':slcPCCardCfgGSMPIN,'slcPCCardCfgGSMNetworkName':slcPCCardCfgGSMNetworkName,'slcPCCardCfgGSMPPPCompression':slcPCCardCfgGSMPPPCompression,'slcPCCardCfgGSMAutoAcquireDNS':slcPCCardCfgGSMAutoAcquireDNS,'slcPCCardCfgGSMDialoutMode':slcPCCardCfgGSMDialoutMode,'slcPCCardCfgGSMContextID':slcPCCardCfgGSMContextID,'slcPCCardCfgGSMBearerService':slcPCCardCfgGSMBearerService,'slcPCCardCfgIdleTimeout':slcPCCardCfgIdleTimeout,'slcPCCardCfgRestartDelay':slcPCCardCfgRestartDelay,'slcPCCardCfgCallerIdLogging':slcPCCardCfgCallerIdLogging,'slcPCCardCfgCallerIdATCmd':slcPCCardCfgCallerIdATCmd,'slcPCCardCfgDODAuth':slcPCCardCfgDODAuth,'slcPCCardCfgDODCHAPHost':slcPCCardCfgDODCHAPHost,'slcPCCardCfgHostList':slcPCCardCfgHostList,'slcPCCardCfgCBCPClientType':slcPCCardCfgCBCPClientType,'slcPCCardCfgCBCPServerAllowNoCallback':slcPCCardCfgCBCPServerAllowNoCallback,'slcPCCardCfgDialbackDelay':slcPCCardCfgDialbackDelay,'slcPCCardCfgCHAPAuthLocalUsers':slcPCCardCfgCHAPAuthLocalUsers,'slcPCCardCfgUseSites':slcPCCardCfgUseSites,'slcPCCardCfgDialbackRetries':slcPCCardCfgDialbackRetries,'slcPCCardCfgGroup':slcPCCardCfgGroup,'slcDevPowerSupply':slcDevPowerSupply,'slcDevPowerSupplyType':slcDevPowerSupplyType,'slcDevPowerSupplyA':slcDevPowerSupplyA,'slcDevPowerSupplyB':slcDevPowerSupplyB,'slcDevUSB':slcDevUSB,'slcDevUSBState':slcDevUSBState,'slcDevUSBCfgTable':slcDevUSBCfgTable,'slcDevUSBCfgEntry':slcDevUSBCfgEntry,_x:slcDevUSBId,'slcDevUSBCfgCardType':slcDevUSBCfgCardType,'slcDevUSBCfgCardId':slcDevUSBCfgCardId,'slcDevUSBCfgStorageFS':slcDevUSBCfgStorageFS,'slcDevUSBCfgBaud':slcDevUSBCfgBaud,'slcDevUSBCfgDataBits':slcDevUSBCfgDataBits,'slcDevUSBCfgStopBits':slcDevUSBCfgStopBits,'slcDevUSBCfgParity':slcDevUSBCfgParity,'slcDevUSBCfgFlowControl':slcDevUSBCfgFlowControl,'slcDevUSBCfgModemState':slcDevUSBCfgModemState,'slcDevUSBCfgModemMode':slcDevUSBCfgModemMode,'slcDevUSBCfgLocalIP':slcDevUSBCfgLocalIP,'slcDevUSBCfgRemoteIP':slcDevUSBCfgRemoteIP,'slcDevUSBCfgAuth':slcDevUSBCfgAuth,'slcDevUSBCfgCHAPHost':slcDevUSBCfgCHAPHost,'slcDevUSBCfgDODAuth':slcDevUSBCfgDODAuth,'slcDevUSBCfgDODCHAPHost':slcDevUSBCfgDODCHAPHost,'slcDevUSBCfgInitScript':slcDevUSBCfgInitScript,'slcDevUSBCfgTimeout':slcDevUSBCfgTimeout,'slcDevUSBCfgDialoutNum':slcDevUSBCfgDialoutNum,'slcDevUSBCfgDialoutLogin':slcDevUSBCfgDialoutLogin,'slcDevUSBCfgDialbackMode':slcDevUSBCfgDialbackMode,'slcDevUSBCfgDialbackNum':slcDevUSBCfgDialbackNum,'slcDevUSBCfgDialbackDelay':slcDevUSBCfgDialbackDelay,'slcDevUSBCfgNATState':slcDevUSBCfgNATState,'slcDevUSBCfgIdleTimeout':slcDevUSBCfgIdleTimeout,'slcDevUSBCfgRestartDelay':slcDevUSBCfgRestartDelay,'slcDevUSBCfgCallerIdLogging':slcDevUSBCfgCallerIdLogging,'slcDevUSBCfgCallerIdATCmd':slcDevUSBCfgCallerIdATCmd,'slcDevUSBCfgHostList':slcDevUSBCfgHostList,'slcDevUSBCfgCBCPClientType':slcDevUSBCfgCBCPClientType,'slcDevUSBCfgCBCPServerAllowNoCallback':slcDevUSBCfgCBCPServerAllowNoCallback,'slcDevUSBCfgTelnetState':slcDevUSBCfgTelnetState,'slcDevUSBCfgTelnetPort':slcDevUSBCfgTelnetPort,'slcDevUSBCfgTelnetAuth':slcDevUSBCfgTelnetAuth,'slcDevUSBCfgSSHState':slcDevUSBCfgSSHState,'slcDevUSBCfgSSHPort':slcDevUSBCfgSSHPort,'slcDevUSBCfgSSHAuth':slcDevUSBCfgSSHAuth,'slcDevUSBCfgTCPState':slcDevUSBCfgTCPState,'slcDevUSBCfgTCPPort':slcDevUSBCfgTCPPort,'slcDevUSBCfgTCPAuth':slcDevUSBCfgTCPAuth,'slcDevUSBCfgGSMPIN':slcDevUSBCfgGSMPIN,'slcDevUSBCfgGSMPPPCompression':slcDevUSBCfgGSMPPPCompression,'slcDevUSBCfgGSMAutoAcquireDNS':slcDevUSBCfgGSMAutoAcquireDNS,'slcDevUSBCfgGSMDialoutMode':slcDevUSBCfgGSMDialoutMode,'slcDevUSBCfgGSMContextID':slcDevUSBCfgGSMContextID,'slcDevUSBCfgGSMBearerService':slcDevUSBCfgGSMBearerService,'slcDevUSBCfgCHAPAuthLocalUsers':slcDevUSBCfgCHAPAuthLocalUsers,'slcDevUSBCfgUseSites':slcDevUSBCfgUseSites,'slcDevUSBCfgDialbackRetries':slcDevUSBCfgDialbackRetries,'slcDevUSBCfgDialtoneCheck':slcDevUSBCfgDialtoneCheck,'slcDevUSBCfgGroup':slcDevUSBCfgGroup,'slcDevIntModem':slcDevIntModem,'slcDevIntModemModemState':slcDevIntModemModemState,'slcDevIntModemModemMode':slcDevIntModemModemMode,'slcDevIntModemLocalIP':slcDevIntModemLocalIP,'slcDevIntModemRemoteIP':slcDevIntModemRemoteIP,'slcDevIntModemAuth':slcDevIntModemAuth,'slcDevIntModemCHAPHost':slcDevIntModemCHAPHost,'slcDevIntModemInitScript':slcDevIntModemInitScript,'slcDevIntModemTimeout':slcDevIntModemTimeout,'slcDevIntModemDialoutNum':slcDevIntModemDialoutNum,'slcDevIntModemDialoutLogin':slcDevIntModemDialoutLogin,'slcDevIntModemDialbackMode':slcDevIntModemDialbackMode,'slcDevIntModemDialbackNum':slcDevIntModemDialbackNum,'slcDevIntModemDialbackRetries':slcDevIntModemDialbackRetries,'slcDevIntModemDialbackDelay':slcDevIntModemDialbackDelay,'slcDevIntModemCallerIdLogging':slcDevIntModemCallerIdLogging,'slcDevIntModemCallerIdATCmd':slcDevIntModemCallerIdATCmd,'slcDevIntModemUseSites':slcDevIntModemUseSites,'slcDevIntModemGroup':slcDevIntModemGroup,'slcDevIntModemIdleTimeout':slcDevIntModemIdleTimeout,'slcDevIntModemRestartDelay':slcDevIntModemRestartDelay,'slcDevIntModemNATState':slcDevIntModemNATState,'slcDevIntModemDialtoneCheck':slcDevIntModemDialtoneCheck,'slcDevRPM':slcDevRPM,'slcDevRPMCfgTable':slcDevRPMCfgTable,'slcDevRPMCfgEntry':slcDevRPMCfgEntry,_g:slcDevRPMId,_Ar:slcDevRPMName,'slcDevRPMVendorModel':slcDevRPMVendorModel,'slcDevRPMManagedVia':slcDevRPMManagedVia,'slcDevRPMIPAddress':slcDevRPMIPAddress,'slcDevRPMPort':slcDevRPMPort,'slcDevRPMDriverOpts':slcDevRPMDriverOpts,'slcDevRPMStatus':slcDevRPMStatus,'slcDevRPMFirmwareVersion':slcDevRPMFirmwareVersion,'slcDevRPMSerialNumber':slcDevRPMSerialNumber,'slcDevRPMMACAddress':slcDevRPMMACAddress,'slcDevRPMNumOutlets':slcDevRPMNumOutlets,'slcDevRPMOutletsOn':slcDevRPMOutletsOn,'slcDevRPMSNMPReadComm':slcDevRPMSNMPReadComm,'slcDevRPMAdminLogin':slcDevRPMAdminLogin,'slcDevRPMLogStatus':slcDevRPMLogStatus,'slcDevRPMCriticalSNMPTraps':slcDevRPMCriticalSNMPTraps,'slcDevRPMCriticalEmails':slcDevRPMCriticalEmails,'slcDevRPMProvidesSLCPower':slcDevRPMProvidesSLCPower,'slcDevRPMOnLowBattery':slcDevRPMOnLowBattery,'slcDevRPMShutdownOrder':slcDevRPMShutdownOrder,'slcDevRPMLoad':slcDevRPMLoad,'slcDevRPMLoadOverThreshold':slcDevRPMLoadOverThreshold,'slcDevRPMBatteryCharge':slcDevRPMBatteryCharge,'slcDevRPMBatteryRuntime':slcDevRPMBatteryRuntime,'slcDevRPMBeeperStatus':slcDevRPMBeeperStatus,'slcDevRPMTemperature':slcDevRPMTemperature,'slcDevRPMUptime':slcDevRPMUptime,'slcDevRPMStatusTable':slcDevRPMStatusTable,'slcDevRPMStatusEntry':slcDevRPMStatusEntry,'slcDevRPMCurrent':slcDevRPMCurrent,'slcDevRPMInputVoltage':slcDevRPMInputVoltage,'slcDevRPMApparentPower':slcDevRPMApparentPower,'slcDevRPMNominalApparentPower':slcDevRPMNominalApparentPower,'slcDevRPMRealPower':slcDevRPMRealPower,'slcDevRPMNominalRealPower':slcDevRPMNominalRealPower,'slcDevRPMOutletTable':slcDevRPMOutletTable,'slcDevRPMOutletEntry':slcDevRPMOutletEntry,'slcDevRPMOutletName':slcDevRPMOutletName,'slcDevRPMOutletState':slcDevRPMOutletState,'slcDevRPMOutletCurrent':slcDevRPMOutletCurrent,'slcDevRPMOutletAction':slcDevRPMOutletAction,'slcConnections':slcConnections,'slcConnNumber':slcConnNumber,'slcConnTable':slcConnTable,'slcConnEntry':slcConnEntry,_AU:slcConnIndex,'slcConnEndPt1':slcConnEndPt1,'slcConnEndPt2':slcConnEndPt2,'slcConnFlow':slcConnFlow,'slcConnUser':slcConnUser,'slcConnDuration':slcConnDuration,'slcConnDurationStr':slcConnDurationStr,'slcConnIdle':slcConnIdle,'slcConnIdleStr':slcConnIdleStr,'slcConnSourceIP':slcConnSourceIP,'slcSystem':slcSystem,'slcSystemModel':slcSystemModel,'slcSystemSerialNo':slcSystemSerialNo,'slcSystemFWRev':slcSystemFWRev,'slcSystemLoadVia':slcSystemLoadVia,'slcSystemFTPServer':slcSystemFTPServer,'slcSystemFTPPath':slcSystemFTPPath,'slcSystemKeypadLock':slcSystemKeypadLock,'slcSystemTimeZone':slcSystemTimeZone,'slcSystemWelcomeBanner':slcSystemWelcomeBanner,'slcSystemLoginBanner':slcSystemLoginBanner,'slcSystemLogoutBanner':slcSystemLogoutBanner,'slcSystemWebTimeout':slcSystemWebTimeout,'slcSystemWebGadget':slcSystemWebGadget,'slcSystemAction':slcSystemAction,'slcSystemSSHPreAuthBanner':slcSystemSSHPreAuthBanner,'slcSystemSiteRackRow':slcSystemSiteRackRow,'slcSystemSiteRackCluster':slcSystemSiteRackCluster,'slcSystemSiteRack':slcSystemSiteRack,'slcSystemLCDScreens':slcSystemLCDScreens,'slcSystemLCDUserStrLine1':slcSystemLCDUserStrLine1,'slcSystemLCDUserStrLine2':slcSystemLCDUserStrLine2,'slcSystemLCDScrolling':slcSystemLCDScrolling,'slcSystemLCDScrollDelay':slcSystemLCDScrollDelay,'slcSystemLCDIdleDelay':slcSystemLCDIdleDelay,_Am:slcSystemInternalTemp,'slcSystemWebProtocol':slcSystemWebProtocol,'slcSystemWebCipher':slcSystemWebCipher,'slcSystemModelString':slcSystemModelString,'slcSystemWebGroup':slcSystemWebGroup,'slcSystemWebInterface':slcSystemWebInterface,'slcSystemWebBanner':slcSystemWebBanner,'slcSystemInternalTempLow':slcSystemInternalTempLow,'slcSystemInternalTempHigh':slcSystemInternalTempHigh,'slcSystemCalibrateTemp':slcSystemCalibrateTemp,'slcSystemWebServer':slcSystemWebServer,'slcEventObjects':slcEventObjects,_AX:slcPowerSupplyId,_AY:slcPowerSupplyAction,_h:slcDevPortNumBytes,_AZ:slcDevPortData,_Ac:slcDevPortStartByte,_Ad:slcDevPortTimeFrame,_Ai:slcDevPortDeviceErrorStatus,_Ab:slcHostname,_Aj:slcPCCardSlot,_Ak:slcPCCardAction,_Al:slcPCCardType,_An:slcUSBAction,_Ao:slcUSBType,_Ap:slcDevPortErrorStatus,_Aq:slcSDCardAction,_As:slcRPMAction,_At:slcEventHost})