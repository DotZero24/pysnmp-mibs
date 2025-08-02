_R='zxDslDhcpv6SnoopingBindIp'
_Q='zxDslDhcpv6SnoopingBindMac'
_P='zxDslDhcpClientDomainName'
_O='zxDslDhcpL3IfIndex'
_N='zxDslDhcpPvcNo'
_M='not-accessible'
_L='zxDslDhcpSnoopingBindMac'
_K='DisplayString'
_J='ifIndex'
_I='IF-MIB'
_H='disable'
_G='enable'
_F='ZTE-DSL-DHCP-MIB'
_E='read-create'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
InetAddress,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','RowStatus','TextualConvention')
zxDslDhcpMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,28))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxDslDhcpSnoopingTable_Object=MibTable
zxDslDhcpSnoopingTable=_ZxDslDhcpSnoopingTable_Object((1,3,6,1,4,1,3902,1004,28,1))
if mibBuilder.loadTexts:zxDslDhcpSnoopingTable.setStatus(_A)
_ZxDslDhcpSnoopingEntry_Object=MibTableRow
zxDslDhcpSnoopingEntry=_ZxDslDhcpSnoopingEntry_Object((1,3,6,1,4,1,3902,1004,28,1,1))
zxDslDhcpSnoopingEntry.setIndexNames((0,_I,_J),(0,_F,_L))
if mibBuilder.loadTexts:zxDslDhcpSnoopingEntry.setStatus(_A)
_ZxDslDhcpSnoopingBindMac_Type=MacAddress
_ZxDslDhcpSnoopingBindMac_Object=MibTableColumn
zxDslDhcpSnoopingBindMac=_ZxDslDhcpSnoopingBindMac_Object((1,3,6,1,4,1,3902,1004,28,1,1,1),_ZxDslDhcpSnoopingBindMac_Type())
zxDslDhcpSnoopingBindMac.setMaxAccess(_M)
if mibBuilder.loadTexts:zxDslDhcpSnoopingBindMac.setStatus(_A)
_ZxDslDhcpSnoopingPvcNo_Type=Integer32
_ZxDslDhcpSnoopingPvcNo_Object=MibTableColumn
zxDslDhcpSnoopingPvcNo=_ZxDslDhcpSnoopingPvcNo_Object((1,3,6,1,4,1,3902,1004,28,1,1,2),_ZxDslDhcpSnoopingPvcNo_Type())
zxDslDhcpSnoopingPvcNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpSnoopingPvcNo.setStatus(_A)
_ZxDslDhcpSnoopingBindIp_Type=IpAddress
_ZxDslDhcpSnoopingBindIp_Object=MibTableColumn
zxDslDhcpSnoopingBindIp=_ZxDslDhcpSnoopingBindIp_Object((1,3,6,1,4,1,3902,1004,28,1,1,3),_ZxDslDhcpSnoopingBindIp_Type())
zxDslDhcpSnoopingBindIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpSnoopingBindIp.setStatus(_A)
_ZxDslDhcpSnoopingBindIpLeaseTime_Type=Integer32
_ZxDslDhcpSnoopingBindIpLeaseTime_Object=MibTableColumn
zxDslDhcpSnoopingBindIpLeaseTime=_ZxDslDhcpSnoopingBindIpLeaseTime_Object((1,3,6,1,4,1,3902,1004,28,1,1,4),_ZxDslDhcpSnoopingBindIpLeaseTime_Type())
zxDslDhcpSnoopingBindIpLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpSnoopingBindIpLeaseTime.setStatus(_A)
_ZxDslDhcpSnoopingBindVlan_Type=Integer32
_ZxDslDhcpSnoopingBindVlan_Object=MibTableColumn
zxDslDhcpSnoopingBindVlan=_ZxDslDhcpSnoopingBindVlan_Object((1,3,6,1,4,1,3902,1004,28,1,1,5),_ZxDslDhcpSnoopingBindVlan_Type())
zxDslDhcpSnoopingBindVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpSnoopingBindVlan.setStatus(_A)
class _ZxDslDhcpSnoopingIpSourceGuard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpSnoopingIpSourceGuard_Type.__name__=_B
_ZxDslDhcpSnoopingIpSourceGuard_Object=MibTableColumn
zxDslDhcpSnoopingIpSourceGuard=_ZxDslDhcpSnoopingIpSourceGuard_Object((1,3,6,1,4,1,3902,1004,28,1,1,6),_ZxDslDhcpSnoopingIpSourceGuard_Type())
zxDslDhcpSnoopingIpSourceGuard.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpSnoopingIpSourceGuard.setStatus(_A)
_ZxDslDhcpPvcIfTable_Object=MibTable
zxDslDhcpPvcIfTable=_ZxDslDhcpPvcIfTable_Object((1,3,6,1,4,1,3902,1004,28,2))
if mibBuilder.loadTexts:zxDslDhcpPvcIfTable.setStatus(_A)
_ZxDslDhcpPvcIfEntry_Object=MibTableRow
zxDslDhcpPvcIfEntry=_ZxDslDhcpPvcIfEntry_Object((1,3,6,1,4,1,3902,1004,28,2,1))
zxDslDhcpPvcIfEntry.setIndexNames((0,_I,_J),(0,_F,_N))
if mibBuilder.loadTexts:zxDslDhcpPvcIfEntry.setStatus(_A)
_ZxDslDhcpPvcNo_Type=Integer32
_ZxDslDhcpPvcNo_Object=MibTableColumn
zxDslDhcpPvcNo=_ZxDslDhcpPvcNo_Object((1,3,6,1,4,1,3902,1004,28,2,1,1),_ZxDslDhcpPvcNo_Type())
zxDslDhcpPvcNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpPvcNo.setStatus(_A)
class _ZxDslDhcpPvcIfIpSourceGuardEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpPvcIfIpSourceGuardEnable_Type.__name__=_B
_ZxDslDhcpPvcIfIpSourceGuardEnable_Object=MibTableColumn
zxDslDhcpPvcIfIpSourceGuardEnable=_ZxDslDhcpPvcIfIpSourceGuardEnable_Object((1,3,6,1,4,1,3902,1004,28,2,1,2),_ZxDslDhcpPvcIfIpSourceGuardEnable_Type())
zxDslDhcpPvcIfIpSourceGuardEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpPvcIfIpSourceGuardEnable.setStatus(_A)
class _ZxDslDhcpPvcIfShortLeaseEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpPvcIfShortLeaseEnable_Type.__name__=_B
_ZxDslDhcpPvcIfShortLeaseEnable_Object=MibTableColumn
zxDslDhcpPvcIfShortLeaseEnable=_ZxDslDhcpPvcIfShortLeaseEnable_Object((1,3,6,1,4,1,3902,1004,28,2,1,3),_ZxDslDhcpPvcIfShortLeaseEnable_Type())
zxDslDhcpPvcIfShortLeaseEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpPvcIfShortLeaseEnable.setStatus(_A)
class _ZxDslDhcpv6PvcIfIpSourceGuardEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpv6PvcIfIpSourceGuardEnable_Type.__name__=_B
_ZxDslDhcpv6PvcIfIpSourceGuardEnable_Object=MibTableColumn
zxDslDhcpv6PvcIfIpSourceGuardEnable=_ZxDslDhcpv6PvcIfIpSourceGuardEnable_Object((1,3,6,1,4,1,3902,1004,28,2,1,4),_ZxDslDhcpv6PvcIfIpSourceGuardEnable_Type())
zxDslDhcpv6PvcIfIpSourceGuardEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpv6PvcIfIpSourceGuardEnable.setStatus(_A)
_ZxDslDhcpIfTable_Object=MibTable
zxDslDhcpIfTable=_ZxDslDhcpIfTable_Object((1,3,6,1,4,1,3902,1004,28,3))
if mibBuilder.loadTexts:zxDslDhcpIfTable.setStatus(_A)
_ZxDslDhcpIfEntry_Object=MibTableRow
zxDslDhcpIfEntry=_ZxDslDhcpIfEntry_Object((1,3,6,1,4,1,3902,1004,28,3,1))
zxDslDhcpIfEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zxDslDhcpIfEntry.setStatus(_A)
class _ZxDslDhcpIfDhcpSnoopingEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpIfDhcpSnoopingEnable_Type.__name__=_B
_ZxDslDhcpIfDhcpSnoopingEnable_Object=MibTableColumn
zxDslDhcpIfDhcpSnoopingEnable=_ZxDslDhcpIfDhcpSnoopingEnable_Object((1,3,6,1,4,1,3902,1004,28,3,1,1),_ZxDslDhcpIfDhcpSnoopingEnable_Type())
zxDslDhcpIfDhcpSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpIfDhcpSnoopingEnable.setStatus(_A)
class _ZxDslDhcpIfDhcpSnoopingLimit_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ZxDslDhcpIfDhcpSnoopingLimit_Type.__name__=_B
_ZxDslDhcpIfDhcpSnoopingLimit_Object=MibTableColumn
zxDslDhcpIfDhcpSnoopingLimit=_ZxDslDhcpIfDhcpSnoopingLimit_Object((1,3,6,1,4,1,3902,1004,28,3,1,2),_ZxDslDhcpIfDhcpSnoopingLimit_Type())
zxDslDhcpIfDhcpSnoopingLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpIfDhcpSnoopingLimit.setStatus(_A)
class _ZxDslDhcpv6IfDhcpSnoopingEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpv6IfDhcpSnoopingEnable_Type.__name__=_B
_ZxDslDhcpv6IfDhcpSnoopingEnable_Object=MibTableColumn
zxDslDhcpv6IfDhcpSnoopingEnable=_ZxDslDhcpv6IfDhcpSnoopingEnable_Object((1,3,6,1,4,1,3902,1004,28,3,1,3),_ZxDslDhcpv6IfDhcpSnoopingEnable_Type())
zxDslDhcpv6IfDhcpSnoopingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpv6IfDhcpSnoopingEnable.setStatus(_A)
class _ZxDslDhcpv6IfDhcpSnoopingLimit_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ZxDslDhcpv6IfDhcpSnoopingLimit_Type.__name__=_B
_ZxDslDhcpv6IfDhcpSnoopingLimit_Object=MibTableColumn
zxDslDhcpv6IfDhcpSnoopingLimit=_ZxDslDhcpv6IfDhcpSnoopingLimit_Object((1,3,6,1,4,1,3902,1004,28,3,1,4),_ZxDslDhcpv6IfDhcpSnoopingLimit_Type())
zxDslDhcpv6IfDhcpSnoopingLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpv6IfDhcpSnoopingLimit.setStatus(_A)
_ZxDslDhcpL3IfTable_Object=MibTable
zxDslDhcpL3IfTable=_ZxDslDhcpL3IfTable_Object((1,3,6,1,4,1,3902,1004,28,4))
if mibBuilder.loadTexts:zxDslDhcpL3IfTable.setStatus(_A)
_ZxDslDhcpL3IfEntry_Object=MibTableRow
zxDslDhcpL3IfEntry=_ZxDslDhcpL3IfEntry_Object((1,3,6,1,4,1,3902,1004,28,4,1))
zxDslDhcpL3IfEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:zxDslDhcpL3IfEntry.setStatus(_A)
_ZxDslDhcpL3IfIndex_Type=Integer32
_ZxDslDhcpL3IfIndex_Object=MibTableColumn
zxDslDhcpL3IfIndex=_ZxDslDhcpL3IfIndex_Object((1,3,6,1,4,1,3902,1004,28,4,1,1),_ZxDslDhcpL3IfIndex_Type())
zxDslDhcpL3IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpL3IfIndex.setStatus(_A)
_ZxDslDhcpL3IfIpAddress_Type=IpAddress
_ZxDslDhcpL3IfIpAddress_Object=MibTableColumn
zxDslDhcpL3IfIpAddress=_ZxDslDhcpL3IfIpAddress_Object((1,3,6,1,4,1,3902,1004,28,4,1,2),_ZxDslDhcpL3IfIpAddress_Type())
zxDslDhcpL3IfIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpL3IfIpAddress.setStatus(_A)
_ZxDslDhcpL3IfIpMask_Type=IpAddress
_ZxDslDhcpL3IfIpMask_Object=MibTableColumn
zxDslDhcpL3IfIpMask=_ZxDslDhcpL3IfIpMask_Object((1,3,6,1,4,1,3902,1004,28,4,1,3),_ZxDslDhcpL3IfIpMask_Type())
zxDslDhcpL3IfIpMask.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpL3IfIpMask.setStatus(_A)
_ZxDslDhcpL3IfDhcpServerIp_Type=IpAddress
_ZxDslDhcpL3IfDhcpServerIp_Object=MibTableColumn
zxDslDhcpL3IfDhcpServerIp=_ZxDslDhcpL3IfDhcpServerIp_Object((1,3,6,1,4,1,3902,1004,28,4,1,4),_ZxDslDhcpL3IfDhcpServerIp_Type())
zxDslDhcpL3IfDhcpServerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpL3IfDhcpServerIp.setStatus(_A)
_ZxDslDhcpL3IfRowstatus_Type=RowStatus
_ZxDslDhcpL3IfRowstatus_Object=MibTableColumn
zxDslDhcpL3IfRowstatus=_ZxDslDhcpL3IfRowstatus_Object((1,3,6,1,4,1,3902,1004,28,4,1,5),_ZxDslDhcpL3IfRowstatus_Type())
zxDslDhcpL3IfRowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpL3IfRowstatus.setStatus(_A)
_ZxDslDhcpClientDomainTable_Object=MibTable
zxDslDhcpClientDomainTable=_ZxDslDhcpClientDomainTable_Object((1,3,6,1,4,1,3902,1004,28,5))
if mibBuilder.loadTexts:zxDslDhcpClientDomainTable.setStatus(_A)
_ZxDslDhcpClientDomainEntry_Object=MibTableRow
zxDslDhcpClientDomainEntry=_ZxDslDhcpClientDomainEntry_Object((1,3,6,1,4,1,3902,1004,28,5,1))
zxDslDhcpClientDomainEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:zxDslDhcpClientDomainEntry.setStatus(_A)
class _ZxDslDhcpClientDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxDslDhcpClientDomainName_Type.__name__=_K
_ZxDslDhcpClientDomainName_Object=MibTableColumn
zxDslDhcpClientDomainName=_ZxDslDhcpClientDomainName_Object((1,3,6,1,4,1,3902,1004,28,5,1,1),_ZxDslDhcpClientDomainName_Type())
zxDslDhcpClientDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpClientDomainName.setStatus(_A)
_ZxDslDhcpServerIp_Type=IpAddress
_ZxDslDhcpServerIp_Object=MibTableColumn
zxDslDhcpServerIp=_ZxDslDhcpServerIp_Object((1,3,6,1,4,1,3902,1004,28,5,1,2),_ZxDslDhcpServerIp_Type())
zxDslDhcpServerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpServerIp.setStatus(_A)
_ZxDslDhcpClientDomainRowstatus_Type=RowStatus
_ZxDslDhcpClientDomainRowstatus_Object=MibTableColumn
zxDslDhcpClientDomainRowstatus=_ZxDslDhcpClientDomainRowstatus_Object((1,3,6,1,4,1,3902,1004,28,5,1,3),_ZxDslDhcpClientDomainRowstatus_Type())
zxDslDhcpClientDomainRowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxDslDhcpClientDomainRowstatus.setStatus(_A)
_ZxDslDhcpGlobal_ObjectIdentity=ObjectIdentity
zxDslDhcpGlobal=_ZxDslDhcpGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1004,28,6))
class _ZxDslDhcpProxyShortLease_Type(Integer32):defaultValue=7200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_ZxDslDhcpProxyShortLease_Type.__name__=_B
_ZxDslDhcpProxyShortLease_Object=MibScalar
zxDslDhcpProxyShortLease=_ZxDslDhcpProxyShortLease_Object((1,3,6,1,4,1,3902,1004,28,6,1),_ZxDslDhcpProxyShortLease_Type())
zxDslDhcpProxyShortLease.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslDhcpProxyShortLease.setStatus(_A)
if mibBuilder.loadTexts:zxDslDhcpProxyShortLease.setUnits('seconds')
_ZxDslDhcpv6_ObjectIdentity=ObjectIdentity
zxDslDhcpv6=_ZxDslDhcpv6_ObjectIdentity((1,3,6,1,4,1,3902,1004,28,7))
_ZxDslDhcpv6SnoopingTable_Object=MibTable
zxDslDhcpv6SnoopingTable=_ZxDslDhcpv6SnoopingTable_Object((1,3,6,1,4,1,3902,1004,28,7,1))
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingTable.setStatus(_A)
_ZxDslDhcpv6SnoopingEntry_Object=MibTableRow
zxDslDhcpv6SnoopingEntry=_ZxDslDhcpv6SnoopingEntry_Object((1,3,6,1,4,1,3902,1004,28,7,1,1))
zxDslDhcpv6SnoopingEntry.setIndexNames((0,_I,_J),(0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingEntry.setStatus(_A)
_ZxDslDhcpv6SnoopingBindMac_Type=MacAddress
_ZxDslDhcpv6SnoopingBindMac_Object=MibTableColumn
zxDslDhcpv6SnoopingBindMac=_ZxDslDhcpv6SnoopingBindMac_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,1),_ZxDslDhcpv6SnoopingBindMac_Type())
zxDslDhcpv6SnoopingBindMac.setMaxAccess(_M)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingBindMac.setStatus(_A)
_ZxDslDhcpv6SnoopingBindIp_Type=InetAddress
_ZxDslDhcpv6SnoopingBindIp_Object=MibTableColumn
zxDslDhcpv6SnoopingBindIp=_ZxDslDhcpv6SnoopingBindIp_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,2),_ZxDslDhcpv6SnoopingBindIp_Type())
zxDslDhcpv6SnoopingBindIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingBindIp.setStatus(_A)
_ZxDslDhcpv6SnoopingPvcNo_Type=Integer32
_ZxDslDhcpv6SnoopingPvcNo_Object=MibTableColumn
zxDslDhcpv6SnoopingPvcNo=_ZxDslDhcpv6SnoopingPvcNo_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,3),_ZxDslDhcpv6SnoopingPvcNo_Type())
zxDslDhcpv6SnoopingPvcNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingPvcNo.setStatus(_A)
_ZxDslDhcpv6SnoopingBindIpLeaseTime_Type=Integer32
_ZxDslDhcpv6SnoopingBindIpLeaseTime_Object=MibTableColumn
zxDslDhcpv6SnoopingBindIpLeaseTime=_ZxDslDhcpv6SnoopingBindIpLeaseTime_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,4),_ZxDslDhcpv6SnoopingBindIpLeaseTime_Type())
zxDslDhcpv6SnoopingBindIpLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingBindIpLeaseTime.setStatus(_A)
_ZxDslDhcpv6SnoopingBindVlan_Type=Integer32
_ZxDslDhcpv6SnoopingBindVlan_Object=MibTableColumn
zxDslDhcpv6SnoopingBindVlan=_ZxDslDhcpv6SnoopingBindVlan_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,5),_ZxDslDhcpv6SnoopingBindVlan_Type())
zxDslDhcpv6SnoopingBindVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingBindVlan.setStatus(_A)
class _ZxDslDhcpv6SnoopingIpSourceGuard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ZxDslDhcpv6SnoopingIpSourceGuard_Type.__name__=_B
_ZxDslDhcpv6SnoopingIpSourceGuard_Object=MibTableColumn
zxDslDhcpv6SnoopingIpSourceGuard=_ZxDslDhcpv6SnoopingIpSourceGuard_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,6),_ZxDslDhcpv6SnoopingIpSourceGuard_Type())
zxDslDhcpv6SnoopingIpSourceGuard.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingIpSourceGuard.setStatus(_A)
_ZxDslDhcpv6SnoopingBindIpPrefixLength_Type=InetAddressPrefixLength
_ZxDslDhcpv6SnoopingBindIpPrefixLength_Object=MibTableColumn
zxDslDhcpv6SnoopingBindIpPrefixLength=_ZxDslDhcpv6SnoopingBindIpPrefixLength_Object((1,3,6,1,4,1,3902,1004,28,7,1,1,7),_ZxDslDhcpv6SnoopingBindIpPrefixLength_Type())
zxDslDhcpv6SnoopingBindIpPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:zxDslDhcpv6SnoopingBindIpPrefixLength.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zte':zte,'zxDsl':zxDsl,'zxDslDhcpMib':zxDslDhcpMib,'zxDslDhcpSnoopingTable':zxDslDhcpSnoopingTable,'zxDslDhcpSnoopingEntry':zxDslDhcpSnoopingEntry,_L:zxDslDhcpSnoopingBindMac,'zxDslDhcpSnoopingPvcNo':zxDslDhcpSnoopingPvcNo,'zxDslDhcpSnoopingBindIp':zxDslDhcpSnoopingBindIp,'zxDslDhcpSnoopingBindIpLeaseTime':zxDslDhcpSnoopingBindIpLeaseTime,'zxDslDhcpSnoopingBindVlan':zxDslDhcpSnoopingBindVlan,'zxDslDhcpSnoopingIpSourceGuard':zxDslDhcpSnoopingIpSourceGuard,'zxDslDhcpPvcIfTable':zxDslDhcpPvcIfTable,'zxDslDhcpPvcIfEntry':zxDslDhcpPvcIfEntry,_N:zxDslDhcpPvcNo,'zxDslDhcpPvcIfIpSourceGuardEnable':zxDslDhcpPvcIfIpSourceGuardEnable,'zxDslDhcpPvcIfShortLeaseEnable':zxDslDhcpPvcIfShortLeaseEnable,'zxDslDhcpv6PvcIfIpSourceGuardEnable':zxDslDhcpv6PvcIfIpSourceGuardEnable,'zxDslDhcpIfTable':zxDslDhcpIfTable,'zxDslDhcpIfEntry':zxDslDhcpIfEntry,'zxDslDhcpIfDhcpSnoopingEnable':zxDslDhcpIfDhcpSnoopingEnable,'zxDslDhcpIfDhcpSnoopingLimit':zxDslDhcpIfDhcpSnoopingLimit,'zxDslDhcpv6IfDhcpSnoopingEnable':zxDslDhcpv6IfDhcpSnoopingEnable,'zxDslDhcpv6IfDhcpSnoopingLimit':zxDslDhcpv6IfDhcpSnoopingLimit,'zxDslDhcpL3IfTable':zxDslDhcpL3IfTable,'zxDslDhcpL3IfEntry':zxDslDhcpL3IfEntry,_O:zxDslDhcpL3IfIndex,'zxDslDhcpL3IfIpAddress':zxDslDhcpL3IfIpAddress,'zxDslDhcpL3IfIpMask':zxDslDhcpL3IfIpMask,'zxDslDhcpL3IfDhcpServerIp':zxDslDhcpL3IfDhcpServerIp,'zxDslDhcpL3IfRowstatus':zxDslDhcpL3IfRowstatus,'zxDslDhcpClientDomainTable':zxDslDhcpClientDomainTable,'zxDslDhcpClientDomainEntry':zxDslDhcpClientDomainEntry,_P:zxDslDhcpClientDomainName,'zxDslDhcpServerIp':zxDslDhcpServerIp,'zxDslDhcpClientDomainRowstatus':zxDslDhcpClientDomainRowstatus,'zxDslDhcpGlobal':zxDslDhcpGlobal,'zxDslDhcpProxyShortLease':zxDslDhcpProxyShortLease,'zxDslDhcpv6':zxDslDhcpv6,'zxDslDhcpv6SnoopingTable':zxDslDhcpv6SnoopingTable,'zxDslDhcpv6SnoopingEntry':zxDslDhcpv6SnoopingEntry,_Q:zxDslDhcpv6SnoopingBindMac,_R:zxDslDhcpv6SnoopingBindIp,'zxDslDhcpv6SnoopingPvcNo':zxDslDhcpv6SnoopingPvcNo,'zxDslDhcpv6SnoopingBindIpLeaseTime':zxDslDhcpv6SnoopingBindIpLeaseTime,'zxDslDhcpv6SnoopingBindVlan':zxDslDhcpv6SnoopingBindVlan,'zxDslDhcpv6SnoopingIpSourceGuard':zxDslDhcpv6SnoopingIpSourceGuard,'zxDslDhcpv6SnoopingBindIpPrefixLength':zxDslDhcpv6SnoopingBindIpPrefixLength})