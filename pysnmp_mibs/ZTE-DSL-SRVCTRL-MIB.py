_A3='zxDslExtIfAntiDosSourceMacAddr'
_A2='zxDslExtIfMaxMacLearn'
_A1='zxDslSupportedRateLimitScale'
_A0='zxDslSupportedProtocolType'
_z='zxDslProtocolRateLimitIndex'
_y='zxDslProtocolRateLimitScale'
_x='zxDslProtocolType'
_w='zxDslIpv6IpLockIpAddr'
_v='0.001dbm'
_u='zxDslServicePortId'
_t='zxDslMvidBrgPortId'
_s='zxDslCPvlanVid'
_r='zxDslVmacTranslateUserMac'
_q='zxDslVmacTranslateBrgPortId'
_p='zxDslVmacBrgPortId'
_o='zxDslMacAddressExtSeqId'
_n='zxDslMacFilterMacAddr'
_m='autoDuplex'
_l='speed1000M'
_k='speed100M'
_j='speed10M'
_i='autoSpeed'
_h='forceFlowControlDisable'
_g='autoFlowControlDisable'
_f='forceFlowControlEnable'
_e='autoFlowControlEnable'
_d='zxDslIpLockIpAddr'
_c='zxDslStaticMacVid'
_b='zxDslStaticMacAddr'
_a='zxDslMacLockVid'
_Z='zxDslMacLockMacAddr'
_Y='zxDslProtocolRateLimitValue'
_X='vlan'
_W='all'
_V='OctetString'
_U='pps'
_T='destroy'
_S='createAndWait'
_R='createAndGo'
_Q='notReady'
_P='notInService'
_O='active'
_N='Unsigned32'
_M='RowStatus'
_L='DisplayString'
_K='enable'
_J='disable'
_I='read-only'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='not-accessible'
_D='ZTE-DSL-SRVCTRL-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslLineAlarmConfProfileEntry,adslLineConfProfileEntry,adslLineConfProfileName=mibBuilder.importSymbols('ADSL-LINE-MIB','adslLineAlarmConfProfileEntry','adslLineConfProfileEntry','adslLineConfProfileName')
dot1dBasePort,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBasePort')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress',_M,'TextualConvention')
zxDslSrvctrlMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,7))
class RateLimitProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,20)));namedValues=NamedValues(*(('multicast',1),('broadcast',2),('unknownMulticast',3),('dlf',4),('dhcp',5),('igmp',6),('icmp',7),('dhcpv6',8),('icmpv6',9),('mld',10),('arp',11),(_W,20)))
class RateLimitScale(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,10,11,12)));namedValues=NamedValues(*(('global',1),('nni',2),('uni',3),('globalVlan',4),('globalPvc',5),(_X,10),('port',11),('pvc',12)))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslSrvctrlObjects_ObjectIdentity=ObjectIdentity
zxDslSrvctrlObjects=_ZxDslSrvctrlObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1))
_ZxDslMacLockTable_Object=MibTable
zxDslMacLockTable=_ZxDslMacLockTable_Object((1,3,6,1,4,1,3902,1004,7,1,1))
if mibBuilder.loadTexts:zxDslMacLockTable.setStatus(_A)
_ZxDslMacLockEntry_Object=MibTableRow
zxDslMacLockEntry=_ZxDslMacLockEntry_Object((1,3,6,1,4,1,3902,1004,7,1,1,1))
zxDslMacLockEntry.setIndexNames((0,_G,_H),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:zxDslMacLockEntry.setStatus(_A)
_ZxDslMacLockMacAddr_Type=MacAddress
_ZxDslMacLockMacAddr_Object=MibTableColumn
zxDslMacLockMacAddr=_ZxDslMacLockMacAddr_Object((1,3,6,1,4,1,3902,1004,7,1,1,1,1),_ZxDslMacLockMacAddr_Type())
zxDslMacLockMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslMacLockMacAddr.setStatus(_A)
class _ZxDslMacLockVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxDslMacLockVid_Type.__name__=_C
_ZxDslMacLockVid_Object=MibTableColumn
zxDslMacLockVid=_ZxDslMacLockVid_Object((1,3,6,1,4,1,3902,1004,7,1,1,1,2),_ZxDslMacLockVid_Type())
zxDslMacLockVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslMacLockVid.setStatus(_A)
class _ZxDslMacLockRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_ZxDslMacLockRowStatus_Type.__name__=_M
_ZxDslMacLockRowStatus_Object=MibTableColumn
zxDslMacLockRowStatus=_ZxDslMacLockRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,1,1,3),_ZxDslMacLockRowStatus_Type())
zxDslMacLockRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslMacLockRowStatus.setStatus(_A)
_ZxDslStaticMacTable_Object=MibTable
zxDslStaticMacTable=_ZxDslStaticMacTable_Object((1,3,6,1,4,1,3902,1004,7,1,2))
if mibBuilder.loadTexts:zxDslStaticMacTable.setStatus(_A)
_ZxDslStaticMacEntry_Object=MibTableRow
zxDslStaticMacEntry=_ZxDslStaticMacEntry_Object((1,3,6,1,4,1,3902,1004,7,1,2,1))
zxDslStaticMacEntry.setIndexNames((0,_G,_H),(0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:zxDslStaticMacEntry.setStatus(_A)
_ZxDslStaticMacAddr_Type=MacAddress
_ZxDslStaticMacAddr_Object=MibTableColumn
zxDslStaticMacAddr=_ZxDslStaticMacAddr_Object((1,3,6,1,4,1,3902,1004,7,1,2,1,1),_ZxDslStaticMacAddr_Type())
zxDslStaticMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslStaticMacAddr.setStatus(_A)
_ZxDslStaticMacVid_Type=Integer32
_ZxDslStaticMacVid_Object=MibTableColumn
zxDslStaticMacVid=_ZxDslStaticMacVid_Object((1,3,6,1,4,1,3902,1004,7,1,2,1,2),_ZxDslStaticMacVid_Type())
zxDslStaticMacVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslStaticMacVid.setStatus(_A)
_ZxDslStaticMacPvcId_Type=Integer32
_ZxDslStaticMacPvcId_Object=MibTableColumn
zxDslStaticMacPvcId=_ZxDslStaticMacPvcId_Object((1,3,6,1,4,1,3902,1004,7,1,2,1,3),_ZxDslStaticMacPvcId_Type())
zxDslStaticMacPvcId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslStaticMacPvcId.setStatus(_A)
class _ZxDslStaticMacTagflag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tag',1),('untag',2),(_W,3)))
_ZxDslStaticMacTagflag_Type.__name__=_C
_ZxDslStaticMacTagflag_Object=MibTableColumn
zxDslStaticMacTagflag=_ZxDslStaticMacTagflag_Object((1,3,6,1,4,1,3902,1004,7,1,2,1,4),_ZxDslStaticMacTagflag_Type())
zxDslStaticMacTagflag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslStaticMacTagflag.setStatus(_A)
class _ZxDslStaticMacRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_ZxDslStaticMacRowStatus_Type.__name__=_M
_ZxDslStaticMacRowStatus_Object=MibTableColumn
zxDslStaticMacRowStatus=_ZxDslStaticMacRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,2,1,5),_ZxDslStaticMacRowStatus_Type())
zxDslStaticMacRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslStaticMacRowStatus.setStatus(_A)
_ZxDslIpLockTable_Object=MibTable
zxDslIpLockTable=_ZxDslIpLockTable_Object((1,3,6,1,4,1,3902,1004,7,1,3))
if mibBuilder.loadTexts:zxDslIpLockTable.setStatus(_A)
_ZxDslIpLockEntry_Object=MibTableRow
zxDslIpLockEntry=_ZxDslIpLockEntry_Object((1,3,6,1,4,1,3902,1004,7,1,3,1))
zxDslIpLockEntry.setIndexNames((0,_G,_H),(0,_D,_d))
if mibBuilder.loadTexts:zxDslIpLockEntry.setStatus(_A)
_ZxDslIpLockIpAddr_Type=IpAddress
_ZxDslIpLockIpAddr_Object=MibTableColumn
zxDslIpLockIpAddr=_ZxDslIpLockIpAddr_Object((1,3,6,1,4,1,3902,1004,7,1,3,1,1),_ZxDslIpLockIpAddr_Type())
zxDslIpLockIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslIpLockIpAddr.setStatus(_A)
class _ZxDslIpLockRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_ZxDslIpLockRowStatus_Type.__name__=_M
_ZxDslIpLockRowStatus_Object=MibTableColumn
zxDslIpLockRowStatus=_ZxDslIpLockRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,3,1,2),_ZxDslIpLockRowStatus_Type())
zxDslIpLockRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslIpLockRowStatus.setStatus(_A)
_ZxDslExtIfTable_Object=MibTable
zxDslExtIfTable=_ZxDslExtIfTable_Object((1,3,6,1,4,1,3902,1004,7,1,4))
if mibBuilder.loadTexts:zxDslExtIfTable.setStatus(_A)
_ZxDslExtIfEntry_Object=MibTableRow
zxDslExtIfEntry=_ZxDslExtIfEntry_Object((1,3,6,1,4,1,3902,1004,7,1,4,1))
zxDslExtIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxDslExtIfEntry.setStatus(_A)
class _ZxDslExtIfFlowCtrlSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4)))
_ZxDslExtIfFlowCtrlSet_Type.__name__=_C
_ZxDslExtIfFlowCtrlSet_Object=MibTableColumn
zxDslExtIfFlowCtrlSet=_ZxDslExtIfFlowCtrlSet_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,1),_ZxDslExtIfFlowCtrlSet_Type())
zxDslExtIfFlowCtrlSet.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfFlowCtrlSet.setStatus(_A)
class _ZxDslExtIfFlowCtrlGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),(_f,2),(_g,3),(_h,4)))
_ZxDslExtIfFlowCtrlGet_Type.__name__=_C
_ZxDslExtIfFlowCtrlGet_Object=MibTableColumn
zxDslExtIfFlowCtrlGet=_ZxDslExtIfFlowCtrlGet_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,2),_ZxDslExtIfFlowCtrlGet_Type())
zxDslExtIfFlowCtrlGet.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslExtIfFlowCtrlGet.setStatus(_A)
class _ZxDslExtIfSpeedSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3),(_l,4)))
_ZxDslExtIfSpeedSet_Type.__name__=_C
_ZxDslExtIfSpeedSet_Object=MibTableColumn
zxDslExtIfSpeedSet=_ZxDslExtIfSpeedSet_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,3),_ZxDslExtIfSpeedSet_Type())
zxDslExtIfSpeedSet.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfSpeedSet.setStatus(_A)
class _ZxDslExtIfSpeedGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3),(_l,4)))
_ZxDslExtIfSpeedGet_Type.__name__=_C
_ZxDslExtIfSpeedGet_Object=MibTableColumn
zxDslExtIfSpeedGet=_ZxDslExtIfSpeedGet_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,4),_ZxDslExtIfSpeedGet_Type())
zxDslExtIfSpeedGet.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslExtIfSpeedGet.setStatus(_A)
class _ZxDslExtIfDuplexSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),('half',2),('full',3)))
_ZxDslExtIfDuplexSet_Type.__name__=_C
_ZxDslExtIfDuplexSet_Object=MibTableColumn
zxDslExtIfDuplexSet=_ZxDslExtIfDuplexSet_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,5),_ZxDslExtIfDuplexSet_Type())
zxDslExtIfDuplexSet.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfDuplexSet.setStatus(_A)
class _ZxDslExtIfDuplexGet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),('half',2),('full',3)))
_ZxDslExtIfDuplexGet_Type.__name__=_C
_ZxDslExtIfDuplexGet_Object=MibTableColumn
zxDslExtIfDuplexGet=_ZxDslExtIfDuplexGet_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,6),_ZxDslExtIfDuplexGet_Type())
zxDslExtIfDuplexGet.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslExtIfDuplexGet.setStatus(_A)
_ZxDslExtIfMaxMacLearn_Type=Integer32
_ZxDslExtIfMaxMacLearn_Object=MibTableColumn
zxDslExtIfMaxMacLearn=_ZxDslExtIfMaxMacLearn_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,7),_ZxDslExtIfMaxMacLearn_Type())
zxDslExtIfMaxMacLearn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfMaxMacLearn.setStatus(_A)
_ZxDslExtIfBroadcastRatelimit_Type=Unsigned32
_ZxDslExtIfBroadcastRatelimit_Object=MibTableColumn
zxDslExtIfBroadcastRatelimit=_ZxDslExtIfBroadcastRatelimit_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,8),_ZxDslExtIfBroadcastRatelimit_Type())
zxDslExtIfBroadcastRatelimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfBroadcastRatelimit.setStatus(_A)
_ZxDslExtIfMulticastRatelimit_Type=Unsigned32
_ZxDslExtIfMulticastRatelimit_Object=MibTableColumn
zxDslExtIfMulticastRatelimit=_ZxDslExtIfMulticastRatelimit_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,9),_ZxDslExtIfMulticastRatelimit_Type())
zxDslExtIfMulticastRatelimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfMulticastRatelimit.setStatus(_A)
_ZxDslExtIfDlfRatelimit_Type=Unsigned32
_ZxDslExtIfDlfRatelimit_Object=MibTableColumn
zxDslExtIfDlfRatelimit=_ZxDslExtIfDlfRatelimit_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,10),_ZxDslExtIfDlfRatelimit_Type())
zxDslExtIfDlfRatelimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfDlfRatelimit.setStatus(_A)
_ZxDslExtIfLinkErrors_Type=Unsigned32
_ZxDslExtIfLinkErrors_Object=MibTableColumn
zxDslExtIfLinkErrors=_ZxDslExtIfLinkErrors_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,11),_ZxDslExtIfLinkErrors_Type())
zxDslExtIfLinkErrors.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslExtIfLinkErrors.setStatus(_A)
class _ZxDslExtIfInterTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ZxDslExtIfInterTag_Type.__name__=_N
_ZxDslExtIfInterTag_Object=MibTableColumn
zxDslExtIfInterTag=_ZxDslExtIfInterTag_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,12),_ZxDslExtIfInterTag_Type())
zxDslExtIfInterTag.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfInterTag.setStatus(_A)
class _ZxDslExtIfBoardcastEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslExtIfBoardcastEnable_Type.__name__=_C
_ZxDslExtIfBoardcastEnable_Object=MibTableColumn
zxDslExtIfBoardcastEnable=_ZxDslExtIfBoardcastEnable_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,13),_ZxDslExtIfBoardcastEnable_Type())
zxDslExtIfBoardcastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfBoardcastEnable.setStatus(_A)
class _ZxDslExtIfMulticastEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslExtIfMulticastEnable_Type.__name__=_C
_ZxDslExtIfMulticastEnable_Object=MibTableColumn
zxDslExtIfMulticastEnable=_ZxDslExtIfMulticastEnable_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,14),_ZxDslExtIfMulticastEnable_Type())
zxDslExtIfMulticastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfMulticastEnable.setStatus(_A)
class _ZxDslExtIfDlfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslExtIfDlfEnable_Type.__name__=_C
_ZxDslExtIfDlfEnable_Object=MibTableColumn
zxDslExtIfDlfEnable=_ZxDslExtIfDlfEnable_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,15),_ZxDslExtIfDlfEnable_Type())
zxDslExtIfDlfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfDlfEnable.setStatus(_A)
_ZxDslExtIfDhcpRatelimit_Type=Unsigned32
_ZxDslExtIfDhcpRatelimit_Object=MibTableColumn
zxDslExtIfDhcpRatelimit=_ZxDslExtIfDhcpRatelimit_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,16),_ZxDslExtIfDhcpRatelimit_Type())
zxDslExtIfDhcpRatelimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfDhcpRatelimit.setStatus(_A)
if mibBuilder.loadTexts:zxDslExtIfDhcpRatelimit.setUnits(_U)
class _ZxDslExtIfUserInfoUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslExtIfUserInfoUserName_Type.__name__=_L
_ZxDslExtIfUserInfoUserName_Object=MibTableColumn
zxDslExtIfUserInfoUserName=_ZxDslExtIfUserInfoUserName_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,17),_ZxDslExtIfUserInfoUserName_Type())
zxDslExtIfUserInfoUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfUserInfoUserName.setStatus(_A)
class _ZxDslExtIfUserInfoUserAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxDslExtIfUserInfoUserAddress_Type.__name__=_L
_ZxDslExtIfUserInfoUserAddress_Object=MibTableColumn
zxDslExtIfUserInfoUserAddress=_ZxDslExtIfUserInfoUserAddress_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,18),_ZxDslExtIfUserInfoUserAddress_Type())
zxDslExtIfUserInfoUserAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfUserInfoUserAddress.setStatus(_A)
class _ZxDslExtIfUserInfoUserServiceConfigured_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslExtIfUserInfoUserServiceConfigured_Type.__name__=_L
_ZxDslExtIfUserInfoUserServiceConfigured_Object=MibTableColumn
zxDslExtIfUserInfoUserServiceConfigured=_ZxDslExtIfUserInfoUserServiceConfigured_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,19),_ZxDslExtIfUserInfoUserServiceConfigured_Type())
zxDslExtIfUserInfoUserServiceConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfUserInfoUserServiceConfigured.setStatus(_A)
class _ZxDslExtIfUserInfoUserOtherNode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZxDslExtIfUserInfoUserOtherNode_Type.__name__=_L
_ZxDslExtIfUserInfoUserOtherNode_Object=MibTableColumn
zxDslExtIfUserInfoUserOtherNode=_ZxDslExtIfUserInfoUserOtherNode_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,20),_ZxDslExtIfUserInfoUserOtherNode_Type())
zxDslExtIfUserInfoUserOtherNode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfUserInfoUserOtherNode.setStatus(_A)
class _ZxDslExtIfPoeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ZxDslExtIfPoeStatus_Type.__name__=_C
_ZxDslExtIfPoeStatus_Object=MibTableColumn
zxDslExtIfPoeStatus=_ZxDslExtIfPoeStatus_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,21),_ZxDslExtIfPoeStatus_Type())
zxDslExtIfPoeStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslExtIfPoeStatus.setStatus(_A)
class _ZxDslExtIfPoeEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslExtIfPoeEnable_Type.__name__=_C
_ZxDslExtIfPoeEnable_Object=MibTableColumn
zxDslExtIfPoeEnable=_ZxDslExtIfPoeEnable_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,22),_ZxDslExtIfPoeEnable_Type())
zxDslExtIfPoeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfPoeEnable.setStatus(_A)
class _ZxDslExtIfDhcpv6RateLimit_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_ZxDslExtIfDhcpv6RateLimit_Type.__name__=_N
_ZxDslExtIfDhcpv6RateLimit_Object=MibTableColumn
zxDslExtIfDhcpv6RateLimit=_ZxDslExtIfDhcpv6RateLimit_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,23),_ZxDslExtIfDhcpv6RateLimit_Type())
zxDslExtIfDhcpv6RateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfDhcpv6RateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxDslExtIfDhcpv6RateLimit.setUnits(_U)
class _ZxDslExtIfIcmpv6RateLimit_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_ZxDslExtIfIcmpv6RateLimit_Type.__name__=_N
_ZxDslExtIfIcmpv6RateLimit_Object=MibScalar
zxDslExtIfIcmpv6RateLimit=_ZxDslExtIfIcmpv6RateLimit_Object((1,3,6,1,4,1,3902,1004,7,1,4,1,24),_ZxDslExtIfIcmpv6RateLimit_Type())
zxDslExtIfIcmpv6RateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslExtIfIcmpv6RateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxDslExtIfIcmpv6RateLimit.setUnits(_U)
_ZxDslMacFilterTable_Object=MibTable
zxDslMacFilterTable=_ZxDslMacFilterTable_Object((1,3,6,1,4,1,3902,1004,7,1,5))
if mibBuilder.loadTexts:zxDslMacFilterTable.setStatus(_A)
_ZxDslMacFilterEntry_Object=MibTableRow
zxDslMacFilterEntry=_ZxDslMacFilterEntry_Object((1,3,6,1,4,1,3902,1004,7,1,5,1))
zxDslMacFilterEntry.setIndexNames((0,_G,_H),(0,_D,_n))
if mibBuilder.loadTexts:zxDslMacFilterEntry.setStatus(_A)
_ZxDslMacFilterMacAddr_Type=MacAddress
_ZxDslMacFilterMacAddr_Object=MibTableColumn
zxDslMacFilterMacAddr=_ZxDslMacFilterMacAddr_Object((1,3,6,1,4,1,3902,1004,7,1,5,1,1),_ZxDslMacFilterMacAddr_Type())
zxDslMacFilterMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslMacFilterMacAddr.setStatus(_A)
class _ZxDslMacFilterRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_ZxDslMacFilterRowStatus_Type.__name__=_M
_ZxDslMacFilterRowStatus_Object=MibTableColumn
zxDslMacFilterRowStatus=_ZxDslMacFilterRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,5,1,2),_ZxDslMacFilterRowStatus_Type())
zxDslMacFilterRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslMacFilterRowStatus.setStatus(_A)
_ZxDslMacCtrlObjects_ObjectIdentity=ObjectIdentity
zxDslMacCtrlObjects=_ZxDslMacCtrlObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9))
_ZxDslMacCtrlGlobalObjects_ObjectIdentity=ObjectIdentity
zxDslMacCtrlGlobalObjects=_ZxDslMacCtrlGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9,1))
class _ZxDslMacLearnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chip',1),('dslamSoftware',2)))
_ZxDslMacLearnType_Type.__name__=_C
_ZxDslMacLearnType_Object=MibScalar
zxDslMacLearnType=_ZxDslMacLearnType_Object((1,3,6,1,4,1,3902,1004,7,1,9,1,1),_ZxDslMacLearnType_Type())
zxDslMacLearnType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacLearnType.setStatus(_A)
class _ZxDslPredefMacForwardEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslPredefMacForwardEnable_Type.__name__=_C
_ZxDslPredefMacForwardEnable_Object=MibScalar
zxDslPredefMacForwardEnable=_ZxDslPredefMacForwardEnable_Object((1,3,6,1,4,1,3902,1004,7,1,9,1,2),_ZxDslPredefMacForwardEnable_Type())
zxDslPredefMacForwardEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPredefMacForwardEnable.setStatus(_A)
_ZxDslMacClear_ObjectIdentity=ObjectIdentity
zxDslMacClear=_ZxDslMacClear_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9,2))
class _ZxDslMacClearType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_W,1),('mac',2),('port',3),(_X,4),('vlanOfMac',5)))
_ZxDslMacClearType_Type.__name__=_C
_ZxDslMacClearType_Object=MibScalar
zxDslMacClearType=_ZxDslMacClearType_Object((1,3,6,1,4,1,3902,1004,7,1,9,2,1),_ZxDslMacClearType_Type())
zxDslMacClearType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacClearType.setStatus(_A)
class _ZxDslMacClearValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxDslMacClearValue_Type.__name__=_L
_ZxDslMacClearValue_Object=MibScalar
zxDslMacClearValue=_ZxDslMacClearValue_Object((1,3,6,1,4,1,3902,1004,7,1,9,2,2),_ZxDslMacClearValue_Type())
zxDslMacClearValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMacClearValue.setStatus(_A)
_ZxDslMacAddressObject_ObjectIdentity=ObjectIdentity
zxDslMacAddressObject=_ZxDslMacAddressObject_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9,3))
_ZxDslMacAddressTable_Object=MibTable
zxDslMacAddressTable=_ZxDslMacAddressTable_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,1))
if mibBuilder.loadTexts:zxDslMacAddressTable.setStatus(_A)
_ZxDslMacAddressEntry_Object=MibTableRow
zxDslMacAddressEntry=_ZxDslMacAddressEntry_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,1,1))
zxDslMacAddressEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxDslMacAddressEntry.setStatus(_A)
class _ZxDslMacAddressList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_ZxDslMacAddressList_Type.__name__=_V
_ZxDslMacAddressList_Object=MibTableColumn
zxDslMacAddressList=_ZxDslMacAddressList_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,1,1,1),_ZxDslMacAddressList_Type())
zxDslMacAddressList.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslMacAddressList.setStatus(_A)
_ZxDslMacAddressExtTable_Object=MibTable
zxDslMacAddressExtTable=_ZxDslMacAddressExtTable_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,2))
if mibBuilder.loadTexts:zxDslMacAddressExtTable.setStatus(_A)
_ZxDslMacAddressExtEntry_Object=MibTableRow
zxDslMacAddressExtEntry=_ZxDslMacAddressExtEntry_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,2,1))
zxDslMacAddressExtEntry.setIndexNames((0,_G,_H),(0,_D,_o))
if mibBuilder.loadTexts:zxDslMacAddressExtEntry.setStatus(_A)
_ZxDslMacAddressExtSeqId_Type=Unsigned32
_ZxDslMacAddressExtSeqId_Object=MibTableColumn
zxDslMacAddressExtSeqId=_ZxDslMacAddressExtSeqId_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,2,1,1),_ZxDslMacAddressExtSeqId_Type())
zxDslMacAddressExtSeqId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslMacAddressExtSeqId.setStatus(_A)
class _ZxDslMacAddressExtList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_ZxDslMacAddressExtList_Type.__name__=_V
_ZxDslMacAddressExtList_Object=MibTableColumn
zxDslMacAddressExtList=_ZxDslMacAddressExtList_Object((1,3,6,1,4,1,3902,1004,7,1,9,3,2,1,2),_ZxDslMacAddressExtList_Type())
zxDslMacAddressExtList.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslMacAddressExtList.setStatus(_A)
_ZxDslVmacObjects_ObjectIdentity=ObjectIdentity
zxDslVmacObjects=_ZxDslVmacObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9,4))
_ZxDslVmacGlobalObjects_ObjectIdentity=ObjectIdentity
zxDslVmacGlobalObjects=_ZxDslVmacGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9,4,1))
class _ZxDslVmacDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_ZxDslVmacDeviceId_Type.__name__=_C
_ZxDslVmacDeviceId_Object=MibScalar
zxDslVmacDeviceId=_ZxDslVmacDeviceId_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,1,1),_ZxDslVmacDeviceId_Type())
zxDslVmacDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslVmacDeviceId.setStatus(_A)
_ZxDslVmacSysMac_Type=MacAddress
_ZxDslVmacSysMac_Object=MibScalar
zxDslVmacSysMac=_ZxDslVmacSysMac_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,1,2),_ZxDslVmacSysMac_Type())
zxDslVmacSysMac.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslVmacSysMac.setStatus(_A)
_ZxDslVmacPortObject_ObjectIdentity=ObjectIdentity
zxDslVmacPortObject=_ZxDslVmacPortObject_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,9,4,2))
_ZxDslVmacBrgPortTable_Object=MibTable
zxDslVmacBrgPortTable=_ZxDslVmacBrgPortTable_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,1))
if mibBuilder.loadTexts:zxDslVmacBrgPortTable.setStatus(_A)
_ZxDslVmacBrgPortEntry_Object=MibTableRow
zxDslVmacBrgPortEntry=_ZxDslVmacBrgPortEntry_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,1,1))
zxDslVmacBrgPortEntry.setIndexNames((0,_G,_H),(0,_D,_p))
if mibBuilder.loadTexts:zxDslVmacBrgPortEntry.setStatus(_A)
_ZxDslVmacBrgPortId_Type=Integer32
_ZxDslVmacBrgPortId_Object=MibTableColumn
zxDslVmacBrgPortId=_ZxDslVmacBrgPortId_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,1,1,1),_ZxDslVmacBrgPortId_Type())
zxDslVmacBrgPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslVmacBrgPortId.setStatus(_A)
class _ZxDslVmacTranslateMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('nToOne',2),('oneToOneFromMacPool',3),('oneToOneFromMappingRule',4)))
_ZxDslVmacTranslateMode_Type.__name__=_C
_ZxDslVmacTranslateMode_Object=MibTableColumn
zxDslVmacTranslateMode=_ZxDslVmacTranslateMode_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,1,1,2),_ZxDslVmacTranslateMode_Type())
zxDslVmacTranslateMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslVmacTranslateMode.setStatus(_A)
class _ZxDslVmacTranslateLimit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ZxDslVmacTranslateLimit_Type.__name__=_C
_ZxDslVmacTranslateLimit_Object=MibTableColumn
zxDslVmacTranslateLimit=_ZxDslVmacTranslateLimit_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,1,1,3),_ZxDslVmacTranslateLimit_Type())
zxDslVmacTranslateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslVmacTranslateLimit.setStatus(_A)
_ZxDslVmacTranslateTable_Object=MibTable
zxDslVmacTranslateTable=_ZxDslVmacTranslateTable_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,2))
if mibBuilder.loadTexts:zxDslVmacTranslateTable.setStatus(_A)
_ZxDslVmacTranslateEntry_Object=MibTableRow
zxDslVmacTranslateEntry=_ZxDslVmacTranslateEntry_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,2,1))
zxDslVmacTranslateEntry.setIndexNames((0,_G,_H),(0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:zxDslVmacTranslateEntry.setStatus(_A)
_ZxDslVmacTranslateBrgPortId_Type=Integer32
_ZxDslVmacTranslateBrgPortId_Object=MibTableColumn
zxDslVmacTranslateBrgPortId=_ZxDslVmacTranslateBrgPortId_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,2,1,1),_ZxDslVmacTranslateBrgPortId_Type())
zxDslVmacTranslateBrgPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslVmacTranslateBrgPortId.setStatus(_A)
_ZxDslVmacTranslateUserMac_Type=MacAddress
_ZxDslVmacTranslateUserMac_Object=MibTableColumn
zxDslVmacTranslateUserMac=_ZxDslVmacTranslateUserMac_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,2,1,2),_ZxDslVmacTranslateUserMac_Type())
zxDslVmacTranslateUserMac.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslVmacTranslateUserMac.setStatus(_A)
_ZxDslVmacTranslateSysMac_Type=MacAddress
_ZxDslVmacTranslateSysMac_Object=MibTableColumn
zxDslVmacTranslateSysMac=_ZxDslVmacTranslateSysMac_Object((1,3,6,1,4,1,3902,1004,7,1,9,4,2,2,1,3),_ZxDslVmacTranslateSysMac_Type())
zxDslVmacTranslateSysMac.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslVmacTranslateSysMac.setStatus(_A)
_ZxDslPvlan_ObjectIdentity=ObjectIdentity
zxDslPvlan=_ZxDslPvlan_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,10))
_ZxDslUpLinkPortList_Type=PortList
_ZxDslUpLinkPortList_Object=MibScalar
zxDslUpLinkPortList=_ZxDslUpLinkPortList_Object((1,3,6,1,4,1,3902,1004,7,1,10,1),_ZxDslUpLinkPortList_Type())
zxDslUpLinkPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslUpLinkPortList.setStatus(_A)
class _ZxDslpvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslpvlanStatus_Type.__name__=_C
_ZxDslpvlanStatus_Object=MibScalar
zxDslpvlanStatus=_ZxDslpvlanStatus_Object((1,3,6,1,4,1,3902,1004,7,1,10,2),_ZxDslpvlanStatus_Type())
zxDslpvlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslpvlanStatus.setStatus(_A)
_ZxDslPvlanPortTable_Object=MibTable
zxDslPvlanPortTable=_ZxDslPvlanPortTable_Object((1,3,6,1,4,1,3902,1004,7,1,10,3))
if mibBuilder.loadTexts:zxDslPvlanPortTable.setStatus(_A)
_ZxDslPvlanPortEntry_Object=MibTableRow
zxDslPvlanPortEntry=_ZxDslPvlanPortEntry_Object((1,3,6,1,4,1,3902,1004,7,1,10,3,1))
zxDslPvlanPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxDslPvlanPortEntry.setStatus(_A)
_ZxDslPvlanPortInterList_Type=PortList
_ZxDslPvlanPortInterList_Object=MibTableColumn
zxDslPvlanPortInterList=_ZxDslPvlanPortInterList_Object((1,3,6,1,4,1,3902,1004,7,1,10,3,1,2),_ZxDslPvlanPortInterList_Type())
zxDslPvlanPortInterList.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPvlanPortInterList.setStatus(_A)
class _ZxDslPvlanPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslPvlanPortAction_Type.__name__=_C
_ZxDslPvlanPortAction_Object=MibTableColumn
zxDslPvlanPortAction=_ZxDslPvlanPortAction_Object((1,3,6,1,4,1,3902,1004,7,1,10,3,1,3),_ZxDslPvlanPortAction_Type())
zxDslPvlanPortAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPvlanPortAction.setStatus(_A)
_ZxDslCPvlanTable_Object=MibTable
zxDslCPvlanTable=_ZxDslCPvlanTable_Object((1,3,6,1,4,1,3902,1004,7,1,10,4))
if mibBuilder.loadTexts:zxDslCPvlanTable.setStatus(_A)
_ZxDslCPvlanEntry_Object=MibTableRow
zxDslCPvlanEntry=_ZxDslCPvlanEntry_Object((1,3,6,1,4,1,3902,1004,7,1,10,4,1))
zxDslCPvlanEntry.setIndexNames((0,_D,_s))
if mibBuilder.loadTexts:zxDslCPvlanEntry.setStatus(_A)
_ZxDslCPvlanVid_Type=Integer32
_ZxDslCPvlanVid_Object=MibTableColumn
zxDslCPvlanVid=_ZxDslCPvlanVid_Object((1,3,6,1,4,1,3902,1004,7,1,10,4,1,1),_ZxDslCPvlanVid_Type())
zxDslCPvlanVid.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslCPvlanVid.setStatus(_A)
class _ZxDslCPvlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslCPvlanStatus_Type.__name__=_C
_ZxDslCPvlanStatus_Object=MibTableColumn
zxDslCPvlanStatus=_ZxDslCPvlanStatus_Object((1,3,6,1,4,1,3902,1004,7,1,10,4,1,2),_ZxDslCPvlanStatus_Type())
zxDslCPvlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslCPvlanStatus.setStatus(_A)
_ZxDslSrvctrlGlobal_ObjectIdentity=ObjectIdentity
zxDslSrvctrlGlobal=_ZxDslSrvctrlGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,11))
_ZxDslBoardcastRateLimit_Type=Integer32
_ZxDslBoardcastRateLimit_Object=MibScalar
zxDslBoardcastRateLimit=_ZxDslBoardcastRateLimit_Object((1,3,6,1,4,1,3902,1004,7,1,11,1),_ZxDslBoardcastRateLimit_Type())
zxDslBoardcastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslBoardcastRateLimit.setStatus(_A)
_ZxDslMulticastRateLimit_Type=Integer32
_ZxDslMulticastRateLimit_Object=MibScalar
zxDslMulticastRateLimit=_ZxDslMulticastRateLimit_Object((1,3,6,1,4,1,3902,1004,7,1,11,2),_ZxDslMulticastRateLimit_Type())
zxDslMulticastRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMulticastRateLimit.setStatus(_A)
_ZxDslDlfRateLimit_Type=Integer32
_ZxDslDlfRateLimit_Object=MibScalar
zxDslDlfRateLimit=_ZxDslDlfRateLimit_Object((1,3,6,1,4,1,3902,1004,7,1,11,3),_ZxDslDlfRateLimit_Type())
zxDslDlfRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslDlfRateLimit.setStatus(_A)
class _ZxDslBoardcastEnalbed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslBoardcastEnalbed_Type.__name__=_C
_ZxDslBoardcastEnalbed_Object=MibScalar
zxDslBoardcastEnalbed=_ZxDslBoardcastEnalbed_Object((1,3,6,1,4,1,3902,1004,7,1,11,4),_ZxDslBoardcastEnalbed_Type())
zxDslBoardcastEnalbed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslBoardcastEnalbed.setStatus(_A)
class _ZxDslMulticastEnalbed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslMulticastEnalbed_Type.__name__=_C
_ZxDslMulticastEnalbed_Object=MibScalar
zxDslMulticastEnalbed=_ZxDslMulticastEnalbed_Object((1,3,6,1,4,1,3902,1004,7,1,11,5),_ZxDslMulticastEnalbed_Type())
zxDslMulticastEnalbed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslMulticastEnalbed.setStatus(_A)
class _ZxDslDlfEnalbed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslDlfEnalbed_Type.__name__=_C
_ZxDslDlfEnalbed_Object=MibScalar
zxDslDlfEnalbed=_ZxDslDlfEnalbed_Object((1,3,6,1,4,1,3902,1004,7,1,11,6),_ZxDslDlfEnalbed_Type())
zxDslDlfEnalbed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslDlfEnalbed.setStatus(_A)
class _ZxDslAntiMacSpoofEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslAntiMacSpoofEnable_Type.__name__=_C
_ZxDslAntiMacSpoofEnable_Object=MibScalar
zxDslAntiMacSpoofEnable=_ZxDslAntiMacSpoofEnable_Object((1,3,6,1,4,1,3902,1004,7,1,11,7),_ZxDslAntiMacSpoofEnable_Type())
zxDslAntiMacSpoofEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslAntiMacSpoofEnable.setStatus(_A)
class _ZxDslEthMgmtIfForwardToNetIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_ZxDslEthMgmtIfForwardToNetIf_Type.__name__=_C
_ZxDslEthMgmtIfForwardToNetIf_Object=MibScalar
zxDslEthMgmtIfForwardToNetIf=_ZxDslEthMgmtIfForwardToNetIf_Object((1,3,6,1,4,1,3902,1004,7,1,11,8),_ZxDslEthMgmtIfForwardToNetIf_Type())
zxDslEthMgmtIfForwardToNetIf.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEthMgmtIfForwardToNetIf.setStatus(_A)
_ZxDslEthMgmtIfForwardVlan_Type=Integer32
_ZxDslEthMgmtIfForwardVlan_Object=MibScalar
zxDslEthMgmtIfForwardVlan=_ZxDslEthMgmtIfForwardVlan_Object((1,3,6,1,4,1,3902,1004,7,1,11,9),_ZxDslEthMgmtIfForwardVlan_Type())
zxDslEthMgmtIfForwardVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslEthMgmtIfForwardVlan.setStatus(_A)
class _ZxDslVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('traditionalVlan',1),('translatingVlan',2),('nToOneVlan',3)))
_ZxDslVlanMode_Type.__name__=_C
_ZxDslVlanMode_Object=MibScalar
zxDslVlanMode=_ZxDslVlanMode_Object((1,3,6,1,4,1,3902,1004,7,1,11,10),_ZxDslVlanMode_Type())
zxDslVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslVlanMode.setStatus(_A)
_ZxDslSrvMulticast_ObjectIdentity=ObjectIdentity
zxDslSrvMulticast=_ZxDslSrvMulticast_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,12))
_ZxDslMvidTable_Object=MibTable
zxDslMvidTable=_ZxDslMvidTable_Object((1,3,6,1,4,1,3902,1004,7,1,12,1))
if mibBuilder.loadTexts:zxDslMvidTable.setStatus(_A)
_ZxDslMvidEntry_Object=MibTableRow
zxDslMvidEntry=_ZxDslMvidEntry_Object((1,3,6,1,4,1,3902,1004,7,1,12,1,1))
zxDslMvidEntry.setIndexNames((0,_G,_H),(0,_D,_t))
if mibBuilder.loadTexts:zxDslMvidEntry.setStatus(_A)
_ZxDslMvidBrgPortId_Type=Integer32
_ZxDslMvidBrgPortId_Object=MibTableColumn
zxDslMvidBrgPortId=_ZxDslMvidBrgPortId_Object((1,3,6,1,4,1,3902,1004,7,1,12,1,1,1),_ZxDslMvidBrgPortId_Type())
zxDslMvidBrgPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslMvidBrgPortId.setStatus(_A)
_ZxDslMvid_Type=Integer32
_ZxDslMvid_Object=MibTableColumn
zxDslMvid=_ZxDslMvid_Object((1,3,6,1,4,1,3902,1004,7,1,12,1,1,2),_ZxDslMvid_Type())
zxDslMvid.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslMvid.setStatus(_A)
_ZxDslMvidRowStatus_Type=RowStatus
_ZxDslMvidRowStatus_Object=MibTableColumn
zxDslMvidRowStatus=_ZxDslMvidRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,12,1,1,10),_ZxDslMvidRowStatus_Type())
zxDslMvidRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslMvidRowStatus.setStatus(_A)
_ZxDslServicePort_ObjectIdentity=ObjectIdentity
zxDslServicePort=_ZxDslServicePort_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,13))
_ZxDslServicePortTable_Object=MibTable
zxDslServicePortTable=_ZxDslServicePortTable_Object((1,3,6,1,4,1,3902,1004,7,1,13,1))
if mibBuilder.loadTexts:zxDslServicePortTable.setStatus(_A)
_ZxDslServicePortEntry_Object=MibTableRow
zxDslServicePortEntry=_ZxDslServicePortEntry_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1))
zxDslServicePortEntry.setIndexNames((0,_G,_H),(0,_D,_u))
if mibBuilder.loadTexts:zxDslServicePortEntry.setStatus(_A)
_ZxDslServicePortId_Type=Integer32
_ZxDslServicePortId_Object=MibTableColumn
zxDslServicePortId=_ZxDslServicePortId_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,1),_ZxDslServicePortId_Type())
zxDslServicePortId.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslServicePortId.setStatus(_A)
class _ZxDslServicePortDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslServicePortDesc_Type.__name__=_L
_ZxDslServicePortDesc_Object=MibTableColumn
zxDslServicePortDesc=_ZxDslServicePortDesc_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,2),_ZxDslServicePortDesc_Type())
zxDslServicePortDesc.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortDesc.setStatus(_A)
class _ZxDslServicePortServiceMode_Type(Bits):namedValues=NamedValues(*(('pvc',0),(_X,1),('priority',2),('encapType',3)))
_ZxDslServicePortServiceMode_Type.__name__='Bits'
_ZxDslServicePortServiceMode_Object=MibTableColumn
zxDslServicePortServiceMode=_ZxDslServicePortServiceMode_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,3),_ZxDslServicePortServiceMode_Type())
zxDslServicePortServiceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortServiceMode.setStatus(_A)
class _ZxDslServicePortPvc_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxDslServicePortPvc_Type.__name__=_C
_ZxDslServicePortPvc_Object=MibTableColumn
zxDslServicePortPvc=_ZxDslServicePortPvc_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,4),_ZxDslServicePortPvc_Type())
zxDslServicePortPvc.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortPvc.setStatus(_A)
class _ZxDslServicePortVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ZxDslServicePortVlan_Type.__name__=_C
_ZxDslServicePortVlan_Object=MibTableColumn
zxDslServicePortVlan=_ZxDslServicePortVlan_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,5),_ZxDslServicePortVlan_Type())
zxDslServicePortVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortVlan.setStatus(_A)
class _ZxDslServicePortPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxDslServicePortPriority_Type.__name__=_C
_ZxDslServicePortPriority_Object=MibTableColumn
zxDslServicePortPriority=_ZxDslServicePortPriority_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,6),_ZxDslServicePortPriority_Type())
zxDslServicePortPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortPriority.setStatus(_A)
class _ZxDslServicePortEthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pppoe',1),('arp',2),('ipoe',3),('ipoev6',4),('customized',5)))
_ZxDslServicePortEthType_Type.__name__=_C
_ZxDslServicePortEthType_Object=MibTableColumn
zxDslServicePortEthType=_ZxDslServicePortEthType_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,7),_ZxDslServicePortEthType_Type())
zxDslServicePortEthType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortEthType.setStatus(_A)
_ZxDslServicePortCustomizedEthType_Type=Integer32
_ZxDslServicePortCustomizedEthType_Object=MibTableColumn
zxDslServicePortCustomizedEthType=_ZxDslServicePortCustomizedEthType_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,8),_ZxDslServicePortCustomizedEthType_Type())
zxDslServicePortCustomizedEthType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortCustomizedEthType.setStatus(_A)
_ZxDslServicePortRowStatus_Type=RowStatus
_ZxDslServicePortRowStatus_Object=MibTableColumn
zxDslServicePortRowStatus=_ZxDslServicePortRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,13,1,1,50),_ZxDslServicePortRowStatus_Type())
zxDslServicePortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslServicePortRowStatus.setStatus(_A)
_ZxDslNni_ObjectIdentity=ObjectIdentity
zxDslNni=_ZxDslNni_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,14))
_ZxDslNniTable_Object=MibTable
zxDslNniTable=_ZxDslNniTable_Object((1,3,6,1,4,1,3902,1004,7,1,14,1))
if mibBuilder.loadTexts:zxDslNniTable.setStatus(_A)
_ZxDslNniEntry_Object=MibTableRow
zxDslNniEntry=_ZxDslNniEntry_Object((1,3,6,1,4,1,3902,1004,7,1,14,1,1))
zxDslNniEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zxDslNniEntry.setStatus(_A)
_ZxDslNniTxOpticalPower_Type=Integer32
_ZxDslNniTxOpticalPower_Object=MibTableColumn
zxDslNniTxOpticalPower=_ZxDslNniTxOpticalPower_Object((1,3,6,1,4,1,3902,1004,7,1,14,1,1,1),_ZxDslNniTxOpticalPower_Type())
zxDslNniTxOpticalPower.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslNniTxOpticalPower.setStatus(_A)
if mibBuilder.loadTexts:zxDslNniTxOpticalPower.setUnits(_v)
_ZxDslNniRxOpticalPower_Type=Integer32
_ZxDslNniRxOpticalPower_Object=MibTableColumn
zxDslNniRxOpticalPower=_ZxDslNniRxOpticalPower_Object((1,3,6,1,4,1,3902,1004,7,1,14,1,1,2),_ZxDslNniRxOpticalPower_Type())
zxDslNniRxOpticalPower.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslNniRxOpticalPower.setStatus(_A)
if mibBuilder.loadTexts:zxDslNniRxOpticalPower.setUnits(_v)
_ZxDslNniOpticalTxBiasCurrent_Type=Integer32
_ZxDslNniOpticalTxBiasCurrent_Object=MibTableColumn
zxDslNniOpticalTxBiasCurrent=_ZxDslNniOpticalTxBiasCurrent_Object((1,3,6,1,4,1,3902,1004,7,1,14,1,1,3),_ZxDslNniOpticalTxBiasCurrent_Type())
zxDslNniOpticalTxBiasCurrent.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslNniOpticalTxBiasCurrent.setStatus(_A)
if mibBuilder.loadTexts:zxDslNniOpticalTxBiasCurrent.setUnits('0.001uA')
_ZxDslNniOpticalVoltage_Type=Integer32
_ZxDslNniOpticalVoltage_Object=MibTableColumn
zxDslNniOpticalVoltage=_ZxDslNniOpticalVoltage_Object((1,3,6,1,4,1,3902,1004,7,1,14,1,1,4),_ZxDslNniOpticalVoltage_Type())
zxDslNniOpticalVoltage.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslNniOpticalVoltage.setStatus(_A)
if mibBuilder.loadTexts:zxDslNniOpticalVoltage.setUnits('0.001V')
_ZxDslNniOpticalTemperature_Type=Integer32
_ZxDslNniOpticalTemperature_Object=MibTableColumn
zxDslNniOpticalTemperature=_ZxDslNniOpticalTemperature_Object((1,3,6,1,4,1,3902,1004,7,1,14,1,1,5),_ZxDslNniOpticalTemperature_Type())
zxDslNniOpticalTemperature.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslNniOpticalTemperature.setStatus(_A)
if mibBuilder.loadTexts:zxDslNniOpticalTemperature.setUnits('0.001centigrade')
_ZxDslIpv6Objects_ObjectIdentity=ObjectIdentity
zxDslIpv6Objects=_ZxDslIpv6Objects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,15))
_ZxDslIpv6IpLockTable_Object=MibTable
zxDslIpv6IpLockTable=_ZxDslIpv6IpLockTable_Object((1,3,6,1,4,1,3902,1004,7,1,15,1))
if mibBuilder.loadTexts:zxDslIpv6IpLockTable.setStatus(_A)
_ZxDslIpv6IpLockEntry_Object=MibTableRow
zxDslIpv6IpLockEntry=_ZxDslIpv6IpLockEntry_Object((1,3,6,1,4,1,3902,1004,7,1,15,1,1))
zxDslIpv6IpLockEntry.setIndexNames((0,_G,_H),(0,_D,_w))
if mibBuilder.loadTexts:zxDslIpv6IpLockEntry.setStatus(_A)
_ZxDslIpv6IpLockIpAddr_Type=InetAddress
_ZxDslIpv6IpLockIpAddr_Object=MibTableColumn
zxDslIpv6IpLockIpAddr=_ZxDslIpv6IpLockIpAddr_Object((1,3,6,1,4,1,3902,1004,7,1,15,1,1,1),_ZxDslIpv6IpLockIpAddr_Type())
zxDslIpv6IpLockIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslIpv6IpLockIpAddr.setStatus(_A)
_ZxDslIpv6IpLockIpAddrPfxLen_Type=InetAddressPrefixLength
_ZxDslIpv6IpLockIpAddrPfxLen_Object=MibTableColumn
zxDslIpv6IpLockIpAddrPfxLen=_ZxDslIpv6IpLockIpAddrPfxLen_Object((1,3,6,1,4,1,3902,1004,7,1,15,1,1,2),_ZxDslIpv6IpLockIpAddrPfxLen_Type())
zxDslIpv6IpLockIpAddrPfxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslIpv6IpLockIpAddrPfxLen.setStatus(_A)
_ZxDslIpv6IpLockRowStatus_Type=RowStatus
_ZxDslIpv6IpLockRowStatus_Object=MibTableColumn
zxDslIpv6IpLockRowStatus=_ZxDslIpv6IpLockRowStatus_Object((1,3,6,1,4,1,3902,1004,7,1,15,1,1,10),_ZxDslIpv6IpLockRowStatus_Type())
zxDslIpv6IpLockRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslIpv6IpLockRowStatus.setStatus(_A)
_ZxDslPonLinkObjects_ObjectIdentity=ObjectIdentity
zxDslPonLinkObjects=_ZxDslPonLinkObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,16))
_ZxDslPonLinkGlobalObjects_ObjectIdentity=ObjectIdentity
zxDslPonLinkGlobalObjects=_ZxDslPonLinkGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,16,1))
_ZxDslPonLinkForceSwap_Type=Integer32
_ZxDslPonLinkForceSwap_Object=MibScalar
zxDslPonLinkForceSwap=_ZxDslPonLinkForceSwap_Object((1,3,6,1,4,1,3902,1004,7,1,16,1,1),_ZxDslPonLinkForceSwap_Type())
zxDslPonLinkForceSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslPonLinkForceSwap.setStatus(_A)
_ZxDslProtocolRateLimitObjects_ObjectIdentity=ObjectIdentity
zxDslProtocolRateLimitObjects=_ZxDslProtocolRateLimitObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,1,17))
_ZxDslProtocolRateLimitTable_Object=MibTable
zxDslProtocolRateLimitTable=_ZxDslProtocolRateLimitTable_Object((1,3,6,1,4,1,3902,1004,7,1,17,1))
if mibBuilder.loadTexts:zxDslProtocolRateLimitTable.setStatus(_A)
_ZxDslProtocolRateLimitEntry_Object=MibTableRow
zxDslProtocolRateLimitEntry=_ZxDslProtocolRateLimitEntry_Object((1,3,6,1,4,1,3902,1004,7,1,17,1,1))
zxDslProtocolRateLimitEntry.setIndexNames((0,_D,_x),(0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:zxDslProtocolRateLimitEntry.setStatus(_A)
_ZxDslProtocolType_Type=RateLimitProtocolType
_ZxDslProtocolType_Object=MibTableColumn
zxDslProtocolType=_ZxDslProtocolType_Object((1,3,6,1,4,1,3902,1004,7,1,17,1,1,1),_ZxDslProtocolType_Type())
zxDslProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslProtocolType.setStatus(_A)
_ZxDslProtocolRateLimitScale_Type=RateLimitScale
_ZxDslProtocolRateLimitScale_Object=MibTableColumn
zxDslProtocolRateLimitScale=_ZxDslProtocolRateLimitScale_Object((1,3,6,1,4,1,3902,1004,7,1,17,1,1,2),_ZxDslProtocolRateLimitScale_Type())
zxDslProtocolRateLimitScale.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslProtocolRateLimitScale.setStatus(_A)
_ZxDslProtocolRateLimitIndex_Type=Integer32
_ZxDslProtocolRateLimitIndex_Object=MibTableColumn
zxDslProtocolRateLimitIndex=_ZxDslProtocolRateLimitIndex_Object((1,3,6,1,4,1,3902,1004,7,1,17,1,1,3),_ZxDslProtocolRateLimitIndex_Type())
zxDslProtocolRateLimitIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslProtocolRateLimitIndex.setStatus(_A)
class _ZxDslProtocolRateLimitAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discard',1),('rateLimit',2),('rateUnlimit',3)))
_ZxDslProtocolRateLimitAction_Type.__name__=_C
_ZxDslProtocolRateLimitAction_Object=MibTableColumn
zxDslProtocolRateLimitAction=_ZxDslProtocolRateLimitAction_Object((1,3,6,1,4,1,3902,1004,7,1,17,1,1,4),_ZxDslProtocolRateLimitAction_Type())
zxDslProtocolRateLimitAction.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslProtocolRateLimitAction.setStatus(_A)
_ZxDslProtocolRateLimitValue_Type=Integer32
_ZxDslProtocolRateLimitValue_Object=MibTableColumn
zxDslProtocolRateLimitValue=_ZxDslProtocolRateLimitValue_Object((1,3,6,1,4,1,3902,1004,7,1,17,1,1,5),_ZxDslProtocolRateLimitValue_Type())
zxDslProtocolRateLimitValue.setMaxAccess(_F)
if mibBuilder.loadTexts:zxDslProtocolRateLimitValue.setStatus(_A)
_ZxDslSupportedRateLimitTable_Object=MibTable
zxDslSupportedRateLimitTable=_ZxDslSupportedRateLimitTable_Object((1,3,6,1,4,1,3902,1004,7,1,17,2))
if mibBuilder.loadTexts:zxDslSupportedRateLimitTable.setStatus(_A)
_ZxDslSupportedRateLimitEntry_Object=MibTableRow
zxDslSupportedRateLimitEntry=_ZxDslSupportedRateLimitEntry_Object((1,3,6,1,4,1,3902,1004,7,1,17,2,1))
zxDslSupportedRateLimitEntry.setIndexNames((0,_D,_A0),(0,_D,_A1))
if mibBuilder.loadTexts:zxDslSupportedRateLimitEntry.setStatus(_A)
_ZxDslSupportedProtocolType_Type=RateLimitProtocolType
_ZxDslSupportedProtocolType_Object=MibTableColumn
zxDslSupportedProtocolType=_ZxDslSupportedProtocolType_Object((1,3,6,1,4,1,3902,1004,7,1,17,2,1,1),_ZxDslSupportedProtocolType_Type())
zxDslSupportedProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslSupportedProtocolType.setStatus(_A)
_ZxDslSupportedRateLimitScale_Type=RateLimitScale
_ZxDslSupportedRateLimitScale_Object=MibTableColumn
zxDslSupportedRateLimitScale=_ZxDslSupportedRateLimitScale_Object((1,3,6,1,4,1,3902,1004,7,1,17,2,1,2),_ZxDslSupportedRateLimitScale_Type())
zxDslSupportedRateLimitScale.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslSupportedRateLimitScale.setStatus(_A)
class _ZxDslSupportedRateLimitUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('kbps',1),(_U,2)))
_ZxDslSupportedRateLimitUnits_Type.__name__=_C
_ZxDslSupportedRateLimitUnits_Object=MibTableColumn
zxDslSupportedRateLimitUnits=_ZxDslSupportedRateLimitUnits_Object((1,3,6,1,4,1,3902,1004,7,1,17,2,1,3),_ZxDslSupportedRateLimitUnits_Type())
zxDslSupportedRateLimitUnits.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslSupportedRateLimitUnits.setStatus(_A)
_ZxDslSrvctrlTrapObjects_ObjectIdentity=ObjectIdentity
zxDslSrvctrlTrapObjects=_ZxDslSrvctrlTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,2))
_ZxDslSrvctrlTrapBindVar_ObjectIdentity=ObjectIdentity
zxDslSrvctrlTrapBindVar=_ZxDslSrvctrlTrapBindVar_ObjectIdentity((1,3,6,1,4,1,3902,1004,7,3))
_ZxDslExtIfAntiDosSourceMacAddr_Type=MacAddress
_ZxDslExtIfAntiDosSourceMacAddr_Object=MibScalar
zxDslExtIfAntiDosSourceMacAddr=_ZxDslExtIfAntiDosSourceMacAddr_Object((1,3,6,1,4,1,3902,1004,7,3,1),_ZxDslExtIfAntiDosSourceMacAddr_Type())
zxDslExtIfAntiDosSourceMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:zxDslExtIfAntiDosSourceMacAddr.setStatus(_A)
zxDslExtIfMacLearnExceedLimit=NotificationType((1,3,6,1,4,1,3902,1004,7,2,1))
zxDslExtIfMacLearnExceedLimit.setObjects((_D,_A2))
if mibBuilder.loadTexts:zxDslExtIfMacLearnExceedLimit.setStatus(_A)
zxDslExtIfAntiDosFault=NotificationType((1,3,6,1,4,1,3902,1004,7,2,2))
zxDslExtIfAntiDosFault.setObjects(*((_G,_H),(_D,_A3)))
if mibBuilder.loadTexts:zxDslExtIfAntiDosFault.setStatus(_A)
zxDslExtIfAntiDosFaultCleared=NotificationType((1,3,6,1,4,1,3902,1004,7,2,3))
zxDslExtIfAntiDosFaultCleared.setObjects(*((_G,_H),(_D,'zxDslExtIfAttackedMacAddr')))
if mibBuilder.loadTexts:zxDslExtIfAntiDosFaultCleared.setStatus(_A)
zxDslRateOverThreshFault=NotificationType((1,3,6,1,4,1,3902,1004,7,2,4))
zxDslRateOverThreshFault.setObjects((_D,_Y))
if mibBuilder.loadTexts:zxDslRateOverThreshFault.setStatus(_A)
zxDslRateOverThreshFaultCleared=NotificationType((1,3,6,1,4,1,3902,1004,7,2,5))
zxDslRateOverThreshFaultCleared.setObjects((_D,_Y))
if mibBuilder.loadTexts:zxDslRateOverThreshFaultCleared.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RateLimitProtocolType':RateLimitProtocolType,'RateLimitScale':RateLimitScale,'zte':zte,'zxDsl':zxDsl,'zxDslSrvctrlMib':zxDslSrvctrlMib,'zxDslSrvctrlObjects':zxDslSrvctrlObjects,'zxDslMacLockTable':zxDslMacLockTable,'zxDslMacLockEntry':zxDslMacLockEntry,_Z:zxDslMacLockMacAddr,_a:zxDslMacLockVid,'zxDslMacLockRowStatus':zxDslMacLockRowStatus,'zxDslStaticMacTable':zxDslStaticMacTable,'zxDslStaticMacEntry':zxDslStaticMacEntry,_b:zxDslStaticMacAddr,_c:zxDslStaticMacVid,'zxDslStaticMacPvcId':zxDslStaticMacPvcId,'zxDslStaticMacTagflag':zxDslStaticMacTagflag,'zxDslStaticMacRowStatus':zxDslStaticMacRowStatus,'zxDslIpLockTable':zxDslIpLockTable,'zxDslIpLockEntry':zxDslIpLockEntry,_d:zxDslIpLockIpAddr,'zxDslIpLockRowStatus':zxDslIpLockRowStatus,'zxDslExtIfTable':zxDslExtIfTable,'zxDslExtIfEntry':zxDslExtIfEntry,'zxDslExtIfFlowCtrlSet':zxDslExtIfFlowCtrlSet,'zxDslExtIfFlowCtrlGet':zxDslExtIfFlowCtrlGet,'zxDslExtIfSpeedSet':zxDslExtIfSpeedSet,'zxDslExtIfSpeedGet':zxDslExtIfSpeedGet,'zxDslExtIfDuplexSet':zxDslExtIfDuplexSet,'zxDslExtIfDuplexGet':zxDslExtIfDuplexGet,_A2:zxDslExtIfMaxMacLearn,'zxDslExtIfBroadcastRatelimit':zxDslExtIfBroadcastRatelimit,'zxDslExtIfMulticastRatelimit':zxDslExtIfMulticastRatelimit,'zxDslExtIfDlfRatelimit':zxDslExtIfDlfRatelimit,'zxDslExtIfLinkErrors':zxDslExtIfLinkErrors,'zxDslExtIfInterTag':zxDslExtIfInterTag,'zxDslExtIfBoardcastEnable':zxDslExtIfBoardcastEnable,'zxDslExtIfMulticastEnable':zxDslExtIfMulticastEnable,'zxDslExtIfDlfEnable':zxDslExtIfDlfEnable,'zxDslExtIfDhcpRatelimit':zxDslExtIfDhcpRatelimit,'zxDslExtIfUserInfoUserName':zxDslExtIfUserInfoUserName,'zxDslExtIfUserInfoUserAddress':zxDslExtIfUserInfoUserAddress,'zxDslExtIfUserInfoUserServiceConfigured':zxDslExtIfUserInfoUserServiceConfigured,'zxDslExtIfUserInfoUserOtherNode':zxDslExtIfUserInfoUserOtherNode,'zxDslExtIfPoeStatus':zxDslExtIfPoeStatus,'zxDslExtIfPoeEnable':zxDslExtIfPoeEnable,'zxDslExtIfDhcpv6RateLimit':zxDslExtIfDhcpv6RateLimit,'zxDslExtIfIcmpv6RateLimit':zxDslExtIfIcmpv6RateLimit,'zxDslMacFilterTable':zxDslMacFilterTable,'zxDslMacFilterEntry':zxDslMacFilterEntry,_n:zxDslMacFilterMacAddr,'zxDslMacFilterRowStatus':zxDslMacFilterRowStatus,'zxDslMacCtrlObjects':zxDslMacCtrlObjects,'zxDslMacCtrlGlobalObjects':zxDslMacCtrlGlobalObjects,'zxDslMacLearnType':zxDslMacLearnType,'zxDslPredefMacForwardEnable':zxDslPredefMacForwardEnable,'zxDslMacClear':zxDslMacClear,'zxDslMacClearType':zxDslMacClearType,'zxDslMacClearValue':zxDslMacClearValue,'zxDslMacAddressObject':zxDslMacAddressObject,'zxDslMacAddressTable':zxDslMacAddressTable,'zxDslMacAddressEntry':zxDslMacAddressEntry,'zxDslMacAddressList':zxDslMacAddressList,'zxDslMacAddressExtTable':zxDslMacAddressExtTable,'zxDslMacAddressExtEntry':zxDslMacAddressExtEntry,_o:zxDslMacAddressExtSeqId,'zxDslMacAddressExtList':zxDslMacAddressExtList,'zxDslVmacObjects':zxDslVmacObjects,'zxDslVmacGlobalObjects':zxDslVmacGlobalObjects,'zxDslVmacDeviceId':zxDslVmacDeviceId,'zxDslVmacSysMac':zxDslVmacSysMac,'zxDslVmacPortObject':zxDslVmacPortObject,'zxDslVmacBrgPortTable':zxDslVmacBrgPortTable,'zxDslVmacBrgPortEntry':zxDslVmacBrgPortEntry,_p:zxDslVmacBrgPortId,'zxDslVmacTranslateMode':zxDslVmacTranslateMode,'zxDslVmacTranslateLimit':zxDslVmacTranslateLimit,'zxDslVmacTranslateTable':zxDslVmacTranslateTable,'zxDslVmacTranslateEntry':zxDslVmacTranslateEntry,_q:zxDslVmacTranslateBrgPortId,_r:zxDslVmacTranslateUserMac,'zxDslVmacTranslateSysMac':zxDslVmacTranslateSysMac,'zxDslPvlan':zxDslPvlan,'zxDslUpLinkPortList':zxDslUpLinkPortList,'zxDslpvlanStatus':zxDslpvlanStatus,'zxDslPvlanPortTable':zxDslPvlanPortTable,'zxDslPvlanPortEntry':zxDslPvlanPortEntry,'zxDslPvlanPortInterList':zxDslPvlanPortInterList,'zxDslPvlanPortAction':zxDslPvlanPortAction,'zxDslCPvlanTable':zxDslCPvlanTable,'zxDslCPvlanEntry':zxDslCPvlanEntry,_s:zxDslCPvlanVid,'zxDslCPvlanStatus':zxDslCPvlanStatus,'zxDslSrvctrlGlobal':zxDslSrvctrlGlobal,'zxDslBoardcastRateLimit':zxDslBoardcastRateLimit,'zxDslMulticastRateLimit':zxDslMulticastRateLimit,'zxDslDlfRateLimit':zxDslDlfRateLimit,'zxDslBoardcastEnalbed':zxDslBoardcastEnalbed,'zxDslMulticastEnalbed':zxDslMulticastEnalbed,'zxDslDlfEnalbed':zxDslDlfEnalbed,'zxDslAntiMacSpoofEnable':zxDslAntiMacSpoofEnable,'zxDslEthMgmtIfForwardToNetIf':zxDslEthMgmtIfForwardToNetIf,'zxDslEthMgmtIfForwardVlan':zxDslEthMgmtIfForwardVlan,'zxDslVlanMode':zxDslVlanMode,'zxDslSrvMulticast':zxDslSrvMulticast,'zxDslMvidTable':zxDslMvidTable,'zxDslMvidEntry':zxDslMvidEntry,_t:zxDslMvidBrgPortId,'zxDslMvid':zxDslMvid,'zxDslMvidRowStatus':zxDslMvidRowStatus,'zxDslServicePort':zxDslServicePort,'zxDslServicePortTable':zxDslServicePortTable,'zxDslServicePortEntry':zxDslServicePortEntry,_u:zxDslServicePortId,'zxDslServicePortDesc':zxDslServicePortDesc,'zxDslServicePortServiceMode':zxDslServicePortServiceMode,'zxDslServicePortPvc':zxDslServicePortPvc,'zxDslServicePortVlan':zxDslServicePortVlan,'zxDslServicePortPriority':zxDslServicePortPriority,'zxDslServicePortEthType':zxDslServicePortEthType,'zxDslServicePortCustomizedEthType':zxDslServicePortCustomizedEthType,'zxDslServicePortRowStatus':zxDslServicePortRowStatus,'zxDslNni':zxDslNni,'zxDslNniTable':zxDslNniTable,'zxDslNniEntry':zxDslNniEntry,'zxDslNniTxOpticalPower':zxDslNniTxOpticalPower,'zxDslNniRxOpticalPower':zxDslNniRxOpticalPower,'zxDslNniOpticalTxBiasCurrent':zxDslNniOpticalTxBiasCurrent,'zxDslNniOpticalVoltage':zxDslNniOpticalVoltage,'zxDslNniOpticalTemperature':zxDslNniOpticalTemperature,'zxDslIpv6Objects':zxDslIpv6Objects,'zxDslIpv6IpLockTable':zxDslIpv6IpLockTable,'zxDslIpv6IpLockEntry':zxDslIpv6IpLockEntry,_w:zxDslIpv6IpLockIpAddr,'zxDslIpv6IpLockIpAddrPfxLen':zxDslIpv6IpLockIpAddrPfxLen,'zxDslIpv6IpLockRowStatus':zxDslIpv6IpLockRowStatus,'zxDslPonLinkObjects':zxDslPonLinkObjects,'zxDslPonLinkGlobalObjects':zxDslPonLinkGlobalObjects,'zxDslPonLinkForceSwap':zxDslPonLinkForceSwap,'zxDslProtocolRateLimitObjects':zxDslProtocolRateLimitObjects,'zxDslProtocolRateLimitTable':zxDslProtocolRateLimitTable,'zxDslProtocolRateLimitEntry':zxDslProtocolRateLimitEntry,_x:zxDslProtocolType,_y:zxDslProtocolRateLimitScale,_z:zxDslProtocolRateLimitIndex,'zxDslProtocolRateLimitAction':zxDslProtocolRateLimitAction,_Y:zxDslProtocolRateLimitValue,'zxDslSupportedRateLimitTable':zxDslSupportedRateLimitTable,'zxDslSupportedRateLimitEntry':zxDslSupportedRateLimitEntry,_A0:zxDslSupportedProtocolType,_A1:zxDslSupportedRateLimitScale,'zxDslSupportedRateLimitUnits':zxDslSupportedRateLimitUnits,'zxDslSrvctrlTrapObjects':zxDslSrvctrlTrapObjects,'zxDslExtIfMacLearnExceedLimit':zxDslExtIfMacLearnExceedLimit,'zxDslExtIfAntiDosFault':zxDslExtIfAntiDosFault,'zxDslExtIfAntiDosFaultCleared':zxDslExtIfAntiDosFaultCleared,'zxDslRateOverThreshFault':zxDslRateOverThreshFault,'zxDslRateOverThreshFaultCleared':zxDslRateOverThreshFaultCleared,'zxDslSrvctrlTrapBindVar':zxDslSrvctrlTrapBindVar,_A3:zxDslExtIfAntiDosSourceMacAddr})