_z='hwSecStatExtModuleLicenseNum'
_y='hwSecStatExtModuleName'
_x='hwSecStatExtVcpuUseage'
_w='hwSecStatExtVcpuID'
_v='hwSecStatExtL2tpSessionNum'
_u='hwSecStatExtL2tpTunnelNum'
_t='hwSecStatHrpPacketsSend'
_s='hwSecStatL2tpUserTotalNum'
_r='hwSecStatIpsecPacketsDorp'
_q='hwSecStatIpsecPacketsOut'
_p='hwSecStatIpsecPacketsIn'
_o='hwSecStatIkeNum'
_n='hwSecStatExtIpv6ServerMapTotalNum'
_m='hwSecStatExtIpv6SessionNum'
_l='hwSecStatExtArplistTotalNum'
_k='hwSecStatExt802dot1xUserOnlineNum'
_j='hwSecStatExtWifiUserOnlineNum'
_i='hwSecStatExtServerMapDynamicNum'
_h='hwSecStatExtServerMapTotalNum'
_g='hwSecStatExtIpMonitorListNum'
_f='hwSecStatExtNatServerNum'
_e='hwSecStatExtBlackListNum'
_d='hwSecStatExtMacAddrListNum'
_c='hwSecStatExtSessionNum'
_b='hwSecStatExtIpv6BgpNum'
_a='hwSecStatExtIpv6IsisNum'
_Z='hwSecStatExtIpv6RipNum'
_Y='hwSecStatExtIpv6OspfNum'
_X='hwSecStatExtIpv6StaticRouteNum'
_W='hwSecStatExtBgpNum'
_V='hwSecStatExtIsisNum'
_U='hwSecStatExtRipNum'
_T='hwSecStatExtOspfNum'
_S='hwSecStatExtStaticRouteNum'
_R='hwSecStatExtAcl6RuleNum'
_Q='hwSecStatExtMacAclRuleNum'
_P='hwSecStatExtAdvanceAclRuleNum'
_O='hwSecStatExtBasicAclRuleNum'
_N='hwSecStatExtAcl6GroupNum'
_M='hwSecStatExtMacAclGroupNum'
_L='hwSecStatExtAdvanceAclGroupNum'
_K='hwSecStatExtBasicAclGroupNum'
_J='hwSecStatExtModuleIndex'
_I='hwSecStatExtVcpuIndex'
_H='hwSecStatExtL2tpCpuIndex'
_G='hwSecStatExtL2tpSlotIndex'
_F='OctetString'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='HUAWEI-SECURITY-STATEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hwSecStatExtMib=ModuleIdentity((1,3,6,1,4,1,2011,6,122,38))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwSecStatExtMibObjects_ObjectIdentity=ObjectIdentity
hwSecStatExtMibObjects=_HwSecStatExtMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,1))
_HwSecStatExtAcl_ObjectIdentity=ObjectIdentity
hwSecStatExtAcl=_HwSecStatExtAcl_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,1,1))
class _HwSecStatExtBasicAclGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtBasicAclGroupNum_Type.__name__=_C
_HwSecStatExtBasicAclGroupNum_Object=MibScalar
hwSecStatExtBasicAclGroupNum=_HwSecStatExtBasicAclGroupNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,1),_HwSecStatExtBasicAclGroupNum_Type())
hwSecStatExtBasicAclGroupNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtBasicAclGroupNum.setStatus(_A)
class _HwSecStatExtAdvanceAclGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtAdvanceAclGroupNum_Type.__name__=_C
_HwSecStatExtAdvanceAclGroupNum_Object=MibScalar
hwSecStatExtAdvanceAclGroupNum=_HwSecStatExtAdvanceAclGroupNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,2),_HwSecStatExtAdvanceAclGroupNum_Type())
hwSecStatExtAdvanceAclGroupNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtAdvanceAclGroupNum.setStatus(_A)
class _HwSecStatExtMacAclGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtMacAclGroupNum_Type.__name__=_C
_HwSecStatExtMacAclGroupNum_Object=MibScalar
hwSecStatExtMacAclGroupNum=_HwSecStatExtMacAclGroupNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,3),_HwSecStatExtMacAclGroupNum_Type())
hwSecStatExtMacAclGroupNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtMacAclGroupNum.setStatus(_A)
class _HwSecStatExtAcl6GroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtAcl6GroupNum_Type.__name__=_C
_HwSecStatExtAcl6GroupNum_Object=MibScalar
hwSecStatExtAcl6GroupNum=_HwSecStatExtAcl6GroupNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,4),_HwSecStatExtAcl6GroupNum_Type())
hwSecStatExtAcl6GroupNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtAcl6GroupNum.setStatus(_A)
class _HwSecStatExtBasicAclRuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtBasicAclRuleNum_Type.__name__=_C
_HwSecStatExtBasicAclRuleNum_Object=MibScalar
hwSecStatExtBasicAclRuleNum=_HwSecStatExtBasicAclRuleNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,5),_HwSecStatExtBasicAclRuleNum_Type())
hwSecStatExtBasicAclRuleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtBasicAclRuleNum.setStatus(_A)
class _HwSecStatExtAdvanceAclRuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtAdvanceAclRuleNum_Type.__name__=_C
_HwSecStatExtAdvanceAclRuleNum_Object=MibScalar
hwSecStatExtAdvanceAclRuleNum=_HwSecStatExtAdvanceAclRuleNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,6),_HwSecStatExtAdvanceAclRuleNum_Type())
hwSecStatExtAdvanceAclRuleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtAdvanceAclRuleNum.setStatus(_A)
class _HwSecStatExtMacAclRuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtMacAclRuleNum_Type.__name__=_C
_HwSecStatExtMacAclRuleNum_Object=MibScalar
hwSecStatExtMacAclRuleNum=_HwSecStatExtMacAclRuleNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,7),_HwSecStatExtMacAclRuleNum_Type())
hwSecStatExtMacAclRuleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtMacAclRuleNum.setStatus(_A)
class _HwSecStatExtAcl6RuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtAcl6RuleNum_Type.__name__=_C
_HwSecStatExtAcl6RuleNum_Object=MibScalar
hwSecStatExtAcl6RuleNum=_HwSecStatExtAcl6RuleNum_Object((1,3,6,1,4,1,2011,6,122,38,1,1,8),_HwSecStatExtAcl6RuleNum_Type())
hwSecStatExtAcl6RuleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtAcl6RuleNum.setStatus(_A)
_HwSecStatExtRoute_ObjectIdentity=ObjectIdentity
hwSecStatExtRoute=_HwSecStatExtRoute_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,1,2))
class _HwSecStatExtStaticRouteNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtStaticRouteNum_Type.__name__=_C
_HwSecStatExtStaticRouteNum_Object=MibScalar
hwSecStatExtStaticRouteNum=_HwSecStatExtStaticRouteNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,1),_HwSecStatExtStaticRouteNum_Type())
hwSecStatExtStaticRouteNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtStaticRouteNum.setStatus(_A)
class _HwSecStatExtOspfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtOspfNum_Type.__name__=_C
_HwSecStatExtOspfNum_Object=MibScalar
hwSecStatExtOspfNum=_HwSecStatExtOspfNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,2),_HwSecStatExtOspfNum_Type())
hwSecStatExtOspfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtOspfNum.setStatus(_A)
class _HwSecStatExtRipNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtRipNum_Type.__name__=_C
_HwSecStatExtRipNum_Object=MibScalar
hwSecStatExtRipNum=_HwSecStatExtRipNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,3),_HwSecStatExtRipNum_Type())
hwSecStatExtRipNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtRipNum.setStatus(_A)
class _HwSecStatExtIsisNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtIsisNum_Type.__name__=_C
_HwSecStatExtIsisNum_Object=MibScalar
hwSecStatExtIsisNum=_HwSecStatExtIsisNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,4),_HwSecStatExtIsisNum_Type())
hwSecStatExtIsisNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIsisNum.setStatus(_A)
class _HwSecStatExtBgpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtBgpNum_Type.__name__=_C
_HwSecStatExtBgpNum_Object=MibScalar
hwSecStatExtBgpNum=_HwSecStatExtBgpNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,5),_HwSecStatExtBgpNum_Type())
hwSecStatExtBgpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtBgpNum.setStatus(_A)
class _HwSecStatExtIpv6StaticRouteNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtIpv6StaticRouteNum_Type.__name__=_C
_HwSecStatExtIpv6StaticRouteNum_Object=MibScalar
hwSecStatExtIpv6StaticRouteNum=_HwSecStatExtIpv6StaticRouteNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,6),_HwSecStatExtIpv6StaticRouteNum_Type())
hwSecStatExtIpv6StaticRouteNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6StaticRouteNum.setStatus(_A)
class _HwSecStatExtIpv6OspfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtIpv6OspfNum_Type.__name__=_C
_HwSecStatExtIpv6OspfNum_Object=MibScalar
hwSecStatExtIpv6OspfNum=_HwSecStatExtIpv6OspfNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,7),_HwSecStatExtIpv6OspfNum_Type())
hwSecStatExtIpv6OspfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6OspfNum.setStatus(_A)
class _HwSecStatExtIpv6RipNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtIpv6RipNum_Type.__name__=_C
_HwSecStatExtIpv6RipNum_Object=MibScalar
hwSecStatExtIpv6RipNum=_HwSecStatExtIpv6RipNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,8),_HwSecStatExtIpv6RipNum_Type())
hwSecStatExtIpv6RipNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6RipNum.setStatus(_A)
class _HwSecStatExtIpv6IsisNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtIpv6IsisNum_Type.__name__=_C
_HwSecStatExtIpv6IsisNum_Object=MibScalar
hwSecStatExtIpv6IsisNum=_HwSecStatExtIpv6IsisNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,9),_HwSecStatExtIpv6IsisNum_Type())
hwSecStatExtIpv6IsisNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6IsisNum.setStatus(_A)
class _HwSecStatExtIpv6BgpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwSecStatExtIpv6BgpNum_Type.__name__=_C
_HwSecStatExtIpv6BgpNum_Object=MibScalar
hwSecStatExtIpv6BgpNum=_HwSecStatExtIpv6BgpNum_Object((1,3,6,1,4,1,2011,6,122,38,1,2,10),_HwSecStatExtIpv6BgpNum_Type())
hwSecStatExtIpv6BgpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6BgpNum.setStatus(_A)
_HwSecStatExtSession_ObjectIdentity=ObjectIdentity
hwSecStatExtSession=_HwSecStatExtSession_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,1,3))
class _HwSecStatExtSessionNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtSessionNum_Type.__name__=_C
_HwSecStatExtSessionNum_Object=MibScalar
hwSecStatExtSessionNum=_HwSecStatExtSessionNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,1),_HwSecStatExtSessionNum_Type())
hwSecStatExtSessionNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtSessionNum.setStatus(_A)
class _HwSecStatExtMacAddrListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtMacAddrListNum_Type.__name__=_C
_HwSecStatExtMacAddrListNum_Object=MibScalar
hwSecStatExtMacAddrListNum=_HwSecStatExtMacAddrListNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,2),_HwSecStatExtMacAddrListNum_Type())
hwSecStatExtMacAddrListNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtMacAddrListNum.setStatus(_A)
class _HwSecStatExtBlackListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtBlackListNum_Type.__name__=_C
_HwSecStatExtBlackListNum_Object=MibScalar
hwSecStatExtBlackListNum=_HwSecStatExtBlackListNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,3),_HwSecStatExtBlackListNum_Type())
hwSecStatExtBlackListNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtBlackListNum.setStatus(_A)
class _HwSecStatExtNatServerNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtNatServerNum_Type.__name__=_C
_HwSecStatExtNatServerNum_Object=MibScalar
hwSecStatExtNatServerNum=_HwSecStatExtNatServerNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,4),_HwSecStatExtNatServerNum_Type())
hwSecStatExtNatServerNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtNatServerNum.setStatus(_A)
class _HwSecStatExtIpMonitorListNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtIpMonitorListNum_Type.__name__=_C
_HwSecStatExtIpMonitorListNum_Object=MibScalar
hwSecStatExtIpMonitorListNum=_HwSecStatExtIpMonitorListNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,5),_HwSecStatExtIpMonitorListNum_Type())
hwSecStatExtIpMonitorListNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpMonitorListNum.setStatus(_A)
class _HwSecStatExtServerMapTotalNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtServerMapTotalNum_Type.__name__=_C
_HwSecStatExtServerMapTotalNum_Object=MibScalar
hwSecStatExtServerMapTotalNum=_HwSecStatExtServerMapTotalNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,6),_HwSecStatExtServerMapTotalNum_Type())
hwSecStatExtServerMapTotalNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtServerMapTotalNum.setStatus(_A)
class _HwSecStatExtServerMapDynamicNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtServerMapDynamicNum_Type.__name__=_C
_HwSecStatExtServerMapDynamicNum_Object=MibScalar
hwSecStatExtServerMapDynamicNum=_HwSecStatExtServerMapDynamicNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,7),_HwSecStatExtServerMapDynamicNum_Type())
hwSecStatExtServerMapDynamicNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtServerMapDynamicNum.setStatus(_A)
class _HwSecStatExtWifiUserOnlineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtWifiUserOnlineNum_Type.__name__=_C
_HwSecStatExtWifiUserOnlineNum_Object=MibScalar
hwSecStatExtWifiUserOnlineNum=_HwSecStatExtWifiUserOnlineNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,8),_HwSecStatExtWifiUserOnlineNum_Type())
hwSecStatExtWifiUserOnlineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtWifiUserOnlineNum.setStatus(_A)
class _HwSecStatExt802dot1xUserOnlineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExt802dot1xUserOnlineNum_Type.__name__=_C
_HwSecStatExt802dot1xUserOnlineNum_Object=MibScalar
hwSecStatExt802dot1xUserOnlineNum=_HwSecStatExt802dot1xUserOnlineNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,9),_HwSecStatExt802dot1xUserOnlineNum_Type())
hwSecStatExt802dot1xUserOnlineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExt802dot1xUserOnlineNum.setStatus(_A)
class _HwSecStatExtArplistTotalNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtArplistTotalNum_Type.__name__=_C
_HwSecStatExtArplistTotalNum_Object=MibScalar
hwSecStatExtArplistTotalNum=_HwSecStatExtArplistTotalNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,10),_HwSecStatExtArplistTotalNum_Type())
hwSecStatExtArplistTotalNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtArplistTotalNum.setStatus(_A)
class _HwSecStatExtFiblistTotoleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtFiblistTotoleNum_Type.__name__=_C
_HwSecStatExtFiblistTotoleNum_Object=MibScalar
hwSecStatExtFiblistTotoleNum=_HwSecStatExtFiblistTotoleNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,11),_HwSecStatExtFiblistTotoleNum_Type())
hwSecStatExtFiblistTotoleNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtFiblistTotoleNum.setStatus(_A)
class _HwSecStatExtIpv6SessionNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtIpv6SessionNum_Type.__name__=_C
_HwSecStatExtIpv6SessionNum_Object=MibScalar
hwSecStatExtIpv6SessionNum=_HwSecStatExtIpv6SessionNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,12),_HwSecStatExtIpv6SessionNum_Type())
hwSecStatExtIpv6SessionNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6SessionNum.setStatus(_A)
class _HwSecStatExtIpv6ServerMapTotalNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtIpv6ServerMapTotalNum_Type.__name__=_C
_HwSecStatExtIpv6ServerMapTotalNum_Object=MibScalar
hwSecStatExtIpv6ServerMapTotalNum=_HwSecStatExtIpv6ServerMapTotalNum_Object((1,3,6,1,4,1,2011,6,122,38,1,3,13),_HwSecStatExtIpv6ServerMapTotalNum_Type())
hwSecStatExtIpv6ServerMapTotalNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtIpv6ServerMapTotalNum.setStatus(_A)
_HwSecStatExtTotalNum_ObjectIdentity=ObjectIdentity
hwSecStatExtTotalNum=_HwSecStatExtTotalNum_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,1,4))
class _HwSecStatIkeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatIkeNum_Type.__name__=_C
_HwSecStatIkeNum_Object=MibScalar
hwSecStatIkeNum=_HwSecStatIkeNum_Object((1,3,6,1,4,1,2011,6,122,38,1,4,1),_HwSecStatIkeNum_Type())
hwSecStatIkeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatIkeNum.setStatus(_A)
_HwSecStatIpsecPacketsIn_Type=Counter64
_HwSecStatIpsecPacketsIn_Object=MibScalar
hwSecStatIpsecPacketsIn=_HwSecStatIpsecPacketsIn_Object((1,3,6,1,4,1,2011,6,122,38,1,4,2),_HwSecStatIpsecPacketsIn_Type())
hwSecStatIpsecPacketsIn.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatIpsecPacketsIn.setStatus(_A)
_HwSecStatIpsecPacketsOut_Type=Counter64
_HwSecStatIpsecPacketsOut_Object=MibScalar
hwSecStatIpsecPacketsOut=_HwSecStatIpsecPacketsOut_Object((1,3,6,1,4,1,2011,6,122,38,1,4,3),_HwSecStatIpsecPacketsOut_Type())
hwSecStatIpsecPacketsOut.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatIpsecPacketsOut.setStatus(_A)
_HwSecStatIpsecPacketsDorp_Type=Counter64
_HwSecStatIpsecPacketsDorp_Object=MibScalar
hwSecStatIpsecPacketsDorp=_HwSecStatIpsecPacketsDorp_Object((1,3,6,1,4,1,2011,6,122,38,1,4,4),_HwSecStatIpsecPacketsDorp_Type())
hwSecStatIpsecPacketsDorp.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatIpsecPacketsDorp.setStatus(_A)
class _HwSecStatL2tpUserTotalNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatL2tpUserTotalNum_Type.__name__=_C
_HwSecStatL2tpUserTotalNum_Object=MibScalar
hwSecStatL2tpUserTotalNum=_HwSecStatL2tpUserTotalNum_Object((1,3,6,1,4,1,2011,6,122,38,1,4,5),_HwSecStatL2tpUserTotalNum_Type())
hwSecStatL2tpUserTotalNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatL2tpUserTotalNum.setStatus(_A)
class _HwSecStatHrpPacketsSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatHrpPacketsSend_Type.__name__=_C
_HwSecStatHrpPacketsSend_Object=MibScalar
hwSecStatHrpPacketsSend=_HwSecStatHrpPacketsSend_Object((1,3,6,1,4,1,2011,6,122,38,1,4,6),_HwSecStatHrpPacketsSend_Type())
hwSecStatHrpPacketsSend.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatHrpPacketsSend.setStatus(_A)
_HwSecStatExtL2tpTable_Object=MibTable
hwSecStatExtL2tpTable=_HwSecStatExtL2tpTable_Object((1,3,6,1,4,1,2011,6,122,38,1,5))
if mibBuilder.loadTexts:hwSecStatExtL2tpTable.setStatus(_A)
_HwSecStatExtL2tpEntry_Object=MibTableRow
hwSecStatExtL2tpEntry=_HwSecStatExtL2tpEntry_Object((1,3,6,1,4,1,2011,6,122,38,1,5,1))
hwSecStatExtL2tpEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hwSecStatExtL2tpEntry.setStatus(_A)
class _HwSecStatExtL2tpSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwSecStatExtL2tpSlotIndex_Type.__name__=_C
_HwSecStatExtL2tpSlotIndex_Object=MibTableColumn
hwSecStatExtL2tpSlotIndex=_HwSecStatExtL2tpSlotIndex_Object((1,3,6,1,4,1,2011,6,122,38,1,5,1,1),_HwSecStatExtL2tpSlotIndex_Type())
hwSecStatExtL2tpSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwSecStatExtL2tpSlotIndex.setStatus(_A)
class _HwSecStatExtL2tpCpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HwSecStatExtL2tpCpuIndex_Type.__name__=_C
_HwSecStatExtL2tpCpuIndex_Object=MibTableColumn
hwSecStatExtL2tpCpuIndex=_HwSecStatExtL2tpCpuIndex_Object((1,3,6,1,4,1,2011,6,122,38,1,5,1,2),_HwSecStatExtL2tpCpuIndex_Type())
hwSecStatExtL2tpCpuIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwSecStatExtL2tpCpuIndex.setStatus(_A)
class _HwSecStatExtL2tpTunnelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtL2tpTunnelNum_Type.__name__=_C
_HwSecStatExtL2tpTunnelNum_Object=MibTableColumn
hwSecStatExtL2tpTunnelNum=_HwSecStatExtL2tpTunnelNum_Object((1,3,6,1,4,1,2011,6,122,38,1,5,1,3),_HwSecStatExtL2tpTunnelNum_Type())
hwSecStatExtL2tpTunnelNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtL2tpTunnelNum.setStatus(_A)
class _HwSecStatExtL2tpSessionNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtL2tpSessionNum_Type.__name__=_C
_HwSecStatExtL2tpSessionNum_Object=MibTableColumn
hwSecStatExtL2tpSessionNum=_HwSecStatExtL2tpSessionNum_Object((1,3,6,1,4,1,2011,6,122,38,1,5,1,4),_HwSecStatExtL2tpSessionNum_Type())
hwSecStatExtL2tpSessionNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtL2tpSessionNum.setStatus(_A)
_HwSecStatExtVcpuTable_Object=MibTable
hwSecStatExtVcpuTable=_HwSecStatExtVcpuTable_Object((1,3,6,1,4,1,2011,6,122,38,1,6))
if mibBuilder.loadTexts:hwSecStatExtVcpuTable.setStatus(_A)
_HwSecStatExtVcpuEntry_Object=MibTableRow
hwSecStatExtVcpuEntry=_HwSecStatExtVcpuEntry_Object((1,3,6,1,4,1,2011,6,122,38,1,6,1))
hwSecStatExtVcpuEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwSecStatExtVcpuEntry.setStatus(_A)
class _HwSecStatExtVcpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HwSecStatExtVcpuIndex_Type.__name__=_C
_HwSecStatExtVcpuIndex_Object=MibTableColumn
hwSecStatExtVcpuIndex=_HwSecStatExtVcpuIndex_Object((1,3,6,1,4,1,2011,6,122,38,1,6,1,1),_HwSecStatExtVcpuIndex_Type())
hwSecStatExtVcpuIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwSecStatExtVcpuIndex.setStatus(_A)
class _HwSecStatExtVcpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_HwSecStatExtVcpuID_Type.__name__=_C
_HwSecStatExtVcpuID_Object=MibTableColumn
hwSecStatExtVcpuID=_HwSecStatExtVcpuID_Object((1,3,6,1,4,1,2011,6,122,38,1,6,1,2),_HwSecStatExtVcpuID_Type())
hwSecStatExtVcpuID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtVcpuID.setStatus(_A)
class _HwSecStatExtVcpuUseage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtVcpuUseage_Type.__name__=_C
_HwSecStatExtVcpuUseage_Object=MibTableColumn
hwSecStatExtVcpuUseage=_HwSecStatExtVcpuUseage_Object((1,3,6,1,4,1,2011,6,122,38,1,6,1,3),_HwSecStatExtVcpuUseage_Type())
hwSecStatExtVcpuUseage.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtVcpuUseage.setStatus(_A)
_HwSecStatExtLicenseTable_Object=MibTable
hwSecStatExtLicenseTable=_HwSecStatExtLicenseTable_Object((1,3,6,1,4,1,2011,6,122,38,1,7))
if mibBuilder.loadTexts:hwSecStatExtLicenseTable.setStatus(_A)
_HwSecStatExtLicenseEntry_Object=MibTableRow
hwSecStatExtLicenseEntry=_HwSecStatExtLicenseEntry_Object((1,3,6,1,4,1,2011,6,122,38,1,7,1))
hwSecStatExtLicenseEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwSecStatExtLicenseEntry.setStatus(_A)
class _HwSecStatExtModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HwSecStatExtModuleIndex_Type.__name__=_C
_HwSecStatExtModuleIndex_Object=MibTableColumn
hwSecStatExtModuleIndex=_HwSecStatExtModuleIndex_Object((1,3,6,1,4,1,2011,6,122,38,1,7,1,1),_HwSecStatExtModuleIndex_Type())
hwSecStatExtModuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwSecStatExtModuleIndex.setStatus(_A)
class _HwSecStatExtModuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwSecStatExtModuleName_Type.__name__=_F
_HwSecStatExtModuleName_Object=MibTableColumn
hwSecStatExtModuleName=_HwSecStatExtModuleName_Object((1,3,6,1,4,1,2011,6,122,38,1,7,1,2),_HwSecStatExtModuleName_Type())
hwSecStatExtModuleName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtModuleName.setStatus(_A)
class _HwSecStatExtModuleLicenseNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HwSecStatExtModuleLicenseNum_Type.__name__=_C
_HwSecStatExtModuleLicenseNum_Object=MibTableColumn
hwSecStatExtModuleLicenseNum=_HwSecStatExtModuleLicenseNum_Object((1,3,6,1,4,1,2011,6,122,38,1,7,1,3),_HwSecStatExtModuleLicenseNum_Type())
hwSecStatExtModuleLicenseNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSecStatExtModuleLicenseNum.setStatus(_A)
_HwSecStatExtConformance_ObjectIdentity=ObjectIdentity
hwSecStatExtConformance=_HwSecStatExtConformance_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,2))
_HwSecStatExtCompliance_ObjectIdentity=ObjectIdentity
hwSecStatExtCompliance=_HwSecStatExtCompliance_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,2,1))
_HwSecStatExtMibGroups_ObjectIdentity=ObjectIdentity
hwSecStatExtMibGroups=_HwSecStatExtMibGroups_ObjectIdentity((1,3,6,1,4,1,2011,6,122,38,2,2))
hwSecStatExtAclGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,1))
hwSecStatExtAclGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hwSecStatExtAclGroup.setStatus(_A)
hwSecStatExtRouteGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,2))
hwSecStatExtRouteGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:hwSecStatExtRouteGroup.setStatus(_A)
hwSecStatExtSessionGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,3))
hwSecStatExtSessionGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:hwSecStatExtSessionGroup.setStatus(_A)
hwSecStatExtIPsecGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,4))
hwSecStatExtIPsecGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:hwSecStatExtIPsecGroup.setStatus(_A)
hwSecStatExtL2tpGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,5))
hwSecStatExtL2tpGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:hwSecStatExtL2tpGroup.setStatus(_A)
hwSecStatExtVcpuGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,6))
hwSecStatExtVcpuGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:hwSecStatExtVcpuGroup.setStatus(_A)
hwSecStatExtLicenseGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,38,2,2,7))
hwSecStatExtLicenseGroup.setObjects(*((_B,_y),(_B,_z)))
if mibBuilder.loadTexts:hwSecStatExtLicenseGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwSecStatExtMib':hwSecStatExtMib,'hwSecStatExtMibObjects':hwSecStatExtMibObjects,'hwSecStatExtAcl':hwSecStatExtAcl,_K:hwSecStatExtBasicAclGroupNum,_L:hwSecStatExtAdvanceAclGroupNum,_M:hwSecStatExtMacAclGroupNum,_N:hwSecStatExtAcl6GroupNum,_O:hwSecStatExtBasicAclRuleNum,_P:hwSecStatExtAdvanceAclRuleNum,_Q:hwSecStatExtMacAclRuleNum,_R:hwSecStatExtAcl6RuleNum,'hwSecStatExtRoute':hwSecStatExtRoute,_S:hwSecStatExtStaticRouteNum,_T:hwSecStatExtOspfNum,_U:hwSecStatExtRipNum,_V:hwSecStatExtIsisNum,_W:hwSecStatExtBgpNum,_X:hwSecStatExtIpv6StaticRouteNum,_Y:hwSecStatExtIpv6OspfNum,_Z:hwSecStatExtIpv6RipNum,_a:hwSecStatExtIpv6IsisNum,_b:hwSecStatExtIpv6BgpNum,'hwSecStatExtSession':hwSecStatExtSession,_c:hwSecStatExtSessionNum,_d:hwSecStatExtMacAddrListNum,_e:hwSecStatExtBlackListNum,_f:hwSecStatExtNatServerNum,_g:hwSecStatExtIpMonitorListNum,_h:hwSecStatExtServerMapTotalNum,_i:hwSecStatExtServerMapDynamicNum,_j:hwSecStatExtWifiUserOnlineNum,_k:hwSecStatExt802dot1xUserOnlineNum,_l:hwSecStatExtArplistTotalNum,'hwSecStatExtFiblistTotoleNum':hwSecStatExtFiblistTotoleNum,_m:hwSecStatExtIpv6SessionNum,_n:hwSecStatExtIpv6ServerMapTotalNum,'hwSecStatExtTotalNum':hwSecStatExtTotalNum,_o:hwSecStatIkeNum,_p:hwSecStatIpsecPacketsIn,_q:hwSecStatIpsecPacketsOut,_r:hwSecStatIpsecPacketsDorp,_s:hwSecStatL2tpUserTotalNum,_t:hwSecStatHrpPacketsSend,'hwSecStatExtL2tpTable':hwSecStatExtL2tpTable,'hwSecStatExtL2tpEntry':hwSecStatExtL2tpEntry,_G:hwSecStatExtL2tpSlotIndex,_H:hwSecStatExtL2tpCpuIndex,_u:hwSecStatExtL2tpTunnelNum,_v:hwSecStatExtL2tpSessionNum,'hwSecStatExtVcpuTable':hwSecStatExtVcpuTable,'hwSecStatExtVcpuEntry':hwSecStatExtVcpuEntry,_I:hwSecStatExtVcpuIndex,_w:hwSecStatExtVcpuID,_x:hwSecStatExtVcpuUseage,'hwSecStatExtLicenseTable':hwSecStatExtLicenseTable,'hwSecStatExtLicenseEntry':hwSecStatExtLicenseEntry,_J:hwSecStatExtModuleIndex,_y:hwSecStatExtModuleName,_z:hwSecStatExtModuleLicenseNum,'hwSecStatExtConformance':hwSecStatExtConformance,'hwSecStatExtCompliance':hwSecStatExtCompliance,'hwSecStatExtMibGroups':hwSecStatExtMibGroups,'hwSecStatExtAclGroup':hwSecStatExtAclGroup,'hwSecStatExtRouteGroup':hwSecStatExtRouteGroup,'hwSecStatExtSessionGroup':hwSecStatExtSessionGroup,'hwSecStatExtIPsecGroup':hwSecStatExtIPsecGroup,'hwSecStatExtL2tpGroup':hwSecStatExtL2tpGroup,'hwSecStatExtVcpuGroup':hwSecStatExtVcpuGroup,'hwSecStatExtLicenseGroup':hwSecStatExtLicenseGroup})