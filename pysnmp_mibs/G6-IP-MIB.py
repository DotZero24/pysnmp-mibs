_N='v6StatusIndex'
_M='v4StatusIndex'
_L='v6AddressIndex'
_K='v6ConfigIndex'
_J='v4ConfigIndex'
_I='enabled'
_H='disabled'
_G='not-accessible'
_F='G6-IP-MIB'
_E='read-only'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Ip_ObjectIdentity=ObjectIdentity
ip=_Ip_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,22))
_IpPingTest_Type=DisplayString
_IpPingTest_Object=MibScalar
ipPingTest=_IpPingTest_Object((1,3,6,1,4,1,3181,10,6,1,22,1),_IpPingTest_Type())
ipPingTest.setMaxAccess(_B)
if mibBuilder.loadTexts:ipPingTest.setStatus(_A)
_IpTraceRoute_Type=DisplayString
_IpTraceRoute_Object=MibScalar
ipTraceRoute=_IpTraceRoute_Object((1,3,6,1,4,1,3181,10,6,1,22,2),_IpTraceRoute_Type())
ipTraceRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:ipTraceRoute.setStatus(_A)
_IpDnsLookup_Type=DisplayString
_IpDnsLookup_Object=MibScalar
ipDnsLookup=_IpDnsLookup_Object((1,3,6,1,4,1,3181,10,6,1,22,3),_IpDnsLookup_Type())
ipDnsLookup.setMaxAccess(_B)
if mibBuilder.loadTexts:ipDnsLookup.setStatus(_A)
_IpArpTable_Type=DisplayString
_IpArpTable_Object=MibScalar
ipArpTable=_IpArpTable_Object((1,3,6,1,4,1,3181,10,6,1,22,4),_IpArpTable_Type())
ipArpTable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipArpTable.setStatus(_A)
_IpHostname_Type=DisplayString
_IpHostname_Object=MibScalar
ipHostname=_IpHostname_Object((1,3,6,1,4,1,3181,10,6,1,22,5),_IpHostname_Type())
ipHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:ipHostname.setStatus(_A)
class _IpLocalMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpLocalMtu_Type.__name__=_D
_IpLocalMtu_Object=MibScalar
ipLocalMtu=_IpLocalMtu_Object((1,3,6,1,4,1,3181,10,6,1,22,6),_IpLocalMtu_Type())
ipLocalMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:ipLocalMtu.setStatus(_A)
_V4ConfigTable_Object=MibTable
v4ConfigTable=_V4ConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,22,7))
if mibBuilder.loadTexts:v4ConfigTable.setStatus(_A)
_V4ConfigEntry_Object=MibTableRow
v4ConfigEntry=_V4ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1))
v4ConfigEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:v4ConfigEntry.setStatus(_A)
class _V4ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_V4ConfigIndex_Type.__name__=_D
_V4ConfigIndex_Object=MibTableColumn
v4ConfigIndex=_V4ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,1),_V4ConfigIndex_Type())
v4ConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:v4ConfigIndex.setStatus(_A)
class _V4ConfigDhcpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('useDhcp',1),('dhcpWithScript',2)))
_V4ConfigDhcpMode_Type.__name__=_D
_V4ConfigDhcpMode_Object=MibTableColumn
v4ConfigDhcpMode=_V4ConfigDhcpMode_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,2),_V4ConfigDhcpMode_Type())
v4ConfigDhcpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigDhcpMode.setStatus(_A)
class _V4ConfigStaticDeviceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4ConfigStaticDeviceIp_Type.__name__=_C
_V4ConfigStaticDeviceIp_Object=MibTableColumn
v4ConfigStaticDeviceIp=_V4ConfigStaticDeviceIp_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,3),_V4ConfigStaticDeviceIp_Type())
v4ConfigStaticDeviceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigStaticDeviceIp.setStatus(_A)
class _V4ConfigStaticSubnetMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4ConfigStaticSubnetMask_Type.__name__=_C
_V4ConfigStaticSubnetMask_Object=MibTableColumn
v4ConfigStaticSubnetMask=_V4ConfigStaticSubnetMask_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,4),_V4ConfigStaticSubnetMask_Type())
v4ConfigStaticSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigStaticSubnetMask.setStatus(_A)
class _V4ConfigStaticGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4ConfigStaticGateway_Type.__name__=_C
_V4ConfigStaticGateway_Object=MibTableColumn
v4ConfigStaticGateway=_V4ConfigStaticGateway_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,5),_V4ConfigStaticGateway_Type())
v4ConfigStaticGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigStaticGateway.setStatus(_A)
class _V4ConfigStaticDnsServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4ConfigStaticDnsServer_Type.__name__=_C
_V4ConfigStaticDnsServer_Object=MibTableColumn
v4ConfigStaticDnsServer=_V4ConfigStaticDnsServer_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,6),_V4ConfigStaticDnsServer_Type())
v4ConfigStaticDnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigStaticDnsServer.setStatus(_A)
class _V4ConfigSecondaryDeviceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4ConfigSecondaryDeviceIp_Type.__name__=_C
_V4ConfigSecondaryDeviceIp_Object=MibTableColumn
v4ConfigSecondaryDeviceIp=_V4ConfigSecondaryDeviceIp_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,7),_V4ConfigSecondaryDeviceIp_Type())
v4ConfigSecondaryDeviceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigSecondaryDeviceIp.setStatus(_A)
class _V4ConfigSecondarySubnetMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4ConfigSecondarySubnetMask_Type.__name__=_C
_V4ConfigSecondarySubnetMask_Object=MibTableColumn
v4ConfigSecondarySubnetMask=_V4ConfigSecondarySubnetMask_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,8),_V4ConfigSecondarySubnetMask_Type())
v4ConfigSecondarySubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigSecondarySubnetMask.setStatus(_A)
class _V4ConfigDefaultAddressSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('primary',0),('secondary',1)))
_V4ConfigDefaultAddressSelection_Type.__name__=_D
_V4ConfigDefaultAddressSelection_Object=MibTableColumn
v4ConfigDefaultAddressSelection=_V4ConfigDefaultAddressSelection_Object((1,3,6,1,4,1,3181,10,6,1,22,7,1,9),_V4ConfigDefaultAddressSelection_Type())
v4ConfigDefaultAddressSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:v4ConfigDefaultAddressSelection.setStatus(_A)
_V6ConfigTable_Object=MibTable
v6ConfigTable=_V6ConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,22,8))
if mibBuilder.loadTexts:v6ConfigTable.setStatus(_A)
_V6ConfigEntry_Object=MibTableRow
v6ConfigEntry=_V6ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,22,8,1))
v6ConfigEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:v6ConfigEntry.setStatus(_A)
class _V6ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_V6ConfigIndex_Type.__name__=_D
_V6ConfigIndex_Object=MibTableColumn
v6ConfigIndex=_V6ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,22,8,1,1),_V6ConfigIndex_Type())
v6ConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:v6ConfigIndex.setStatus(_A)
class _V6ConfigEnableIpv6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_V6ConfigEnableIpv6_Type.__name__=_D
_V6ConfigEnableIpv6_Object=MibTableColumn
v6ConfigEnableIpv6=_V6ConfigEnableIpv6_Object((1,3,6,1,4,1,3181,10,6,1,22,8,1,2),_V6ConfigEnableIpv6_Type())
v6ConfigEnableIpv6.setMaxAccess(_B)
if mibBuilder.loadTexts:v6ConfigEnableIpv6.setStatus(_A)
class _V6ConfigEnableIcmpAutoAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_V6ConfigEnableIcmpAutoAddress_Type.__name__=_D
_V6ConfigEnableIcmpAutoAddress_Object=MibTableColumn
v6ConfigEnableIcmpAutoAddress=_V6ConfigEnableIcmpAutoAddress_Object((1,3,6,1,4,1,3181,10,6,1,22,8,1,3),_V6ConfigEnableIcmpAutoAddress_Type())
v6ConfigEnableIcmpAutoAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:v6ConfigEnableIcmpAutoAddress.setStatus(_A)
class _V6ConfigEnableDhcpAutoAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_V6ConfigEnableDhcpAutoAddress_Type.__name__=_D
_V6ConfigEnableDhcpAutoAddress_Object=MibTableColumn
v6ConfigEnableDhcpAutoAddress=_V6ConfigEnableDhcpAutoAddress_Object((1,3,6,1,4,1,3181,10,6,1,22,8,1,4),_V6ConfigEnableDhcpAutoAddress_Type())
v6ConfigEnableDhcpAutoAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:v6ConfigEnableDhcpAutoAddress.setStatus(_A)
_V6AddressTable_Object=MibTable
v6AddressTable=_V6AddressTable_Object((1,3,6,1,4,1,3181,10,6,1,22,9))
if mibBuilder.loadTexts:v6AddressTable.setStatus(_A)
_V6AddressEntry_Object=MibTableRow
v6AddressEntry=_V6AddressEntry_Object((1,3,6,1,4,1,3181,10,6,1,22,9,1))
v6AddressEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:v6AddressEntry.setStatus(_A)
class _V6AddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_V6AddressIndex_Type.__name__=_D
_V6AddressIndex_Object=MibTableColumn
v6AddressIndex=_V6AddressIndex_Object((1,3,6,1,4,1,3181,10,6,1,22,9,1,1),_V6AddressIndex_Type())
v6AddressIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:v6AddressIndex.setStatus(_A)
_V6AddressIp_Type=DisplayString
_V6AddressIp_Object=MibTableColumn
v6AddressIp=_V6AddressIp_Object((1,3,6,1,4,1,3181,10,6,1,22,9,1,2),_V6AddressIp_Type())
v6AddressIp.setMaxAccess(_B)
if mibBuilder.loadTexts:v6AddressIp.setStatus(_A)
_V4StatusTable_Object=MibTable
v4StatusTable=_V4StatusTable_Object((1,3,6,1,4,1,3181,10,6,1,22,100))
if mibBuilder.loadTexts:v4StatusTable.setStatus(_A)
_V4StatusEntry_Object=MibTableRow
v4StatusEntry=_V4StatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1))
v4StatusEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:v4StatusEntry.setStatus(_A)
class _V4StatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_V4StatusIndex_Type.__name__=_D
_V4StatusIndex_Object=MibTableColumn
v4StatusIndex=_V4StatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,1),_V4StatusIndex_Type())
v4StatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:v4StatusIndex.setStatus(_A)
class _V4StatusDynamicDeviceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicDeviceIp_Type.__name__=_C
_V4StatusDynamicDeviceIp_Object=MibTableColumn
v4StatusDynamicDeviceIp=_V4StatusDynamicDeviceIp_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,2),_V4StatusDynamicDeviceIp_Type())
v4StatusDynamicDeviceIp.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicDeviceIp.setStatus(_A)
class _V4StatusDynamicSubnetMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicSubnetMask_Type.__name__=_C
_V4StatusDynamicSubnetMask_Object=MibTableColumn
v4StatusDynamicSubnetMask=_V4StatusDynamicSubnetMask_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,3),_V4StatusDynamicSubnetMask_Type())
v4StatusDynamicSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicSubnetMask.setStatus(_A)
class _V4StatusDynamicGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicGateway_Type.__name__=_C
_V4StatusDynamicGateway_Object=MibTableColumn
v4StatusDynamicGateway=_V4StatusDynamicGateway_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,4),_V4StatusDynamicGateway_Type())
v4StatusDynamicGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicGateway.setStatus(_A)
class _V4StatusDynamicDnsServer1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicDnsServer1_Type.__name__=_C
_V4StatusDynamicDnsServer1_Object=MibTableColumn
v4StatusDynamicDnsServer1=_V4StatusDynamicDnsServer1_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,5),_V4StatusDynamicDnsServer1_Type())
v4StatusDynamicDnsServer1.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicDnsServer1.setStatus(_A)
class _V4StatusDynamicDnsServer2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicDnsServer2_Type.__name__=_C
_V4StatusDynamicDnsServer2_Object=MibTableColumn
v4StatusDynamicDnsServer2=_V4StatusDynamicDnsServer2_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,6),_V4StatusDynamicDnsServer2_Type())
v4StatusDynamicDnsServer2.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicDnsServer2.setStatus(_A)
class _V4StatusDynamicDnsServer3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicDnsServer3_Type.__name__=_C
_V4StatusDynamicDnsServer3_Object=MibTableColumn
v4StatusDynamicDnsServer3=_V4StatusDynamicDnsServer3_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,7),_V4StatusDynamicDnsServer3_Type())
v4StatusDynamicDnsServer3.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicDnsServer3.setStatus(_A)
class _V4StatusDynamicDnsServer4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusDynamicDnsServer4_Type.__name__=_C
_V4StatusDynamicDnsServer4_Object=MibTableColumn
v4StatusDynamicDnsServer4=_V4StatusDynamicDnsServer4_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,8),_V4StatusDynamicDnsServer4_Type())
v4StatusDynamicDnsServer4.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusDynamicDnsServer4.setStatus(_A)
class _V4StatusOutgoingDeviceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V4StatusOutgoingDeviceIp_Type.__name__=_C
_V4StatusOutgoingDeviceIp_Object=MibTableColumn
v4StatusOutgoingDeviceIp=_V4StatusOutgoingDeviceIp_Object((1,3,6,1,4,1,3181,10,6,1,22,100,1,9),_V4StatusOutgoingDeviceIp_Type())
v4StatusOutgoingDeviceIp.setMaxAccess(_E)
if mibBuilder.loadTexts:v4StatusOutgoingDeviceIp.setStatus(_A)
_V6StatusTable_Object=MibTable
v6StatusTable=_V6StatusTable_Object((1,3,6,1,4,1,3181,10,6,1,22,101))
if mibBuilder.loadTexts:v6StatusTable.setStatus(_A)
_V6StatusEntry_Object=MibTableRow
v6StatusEntry=_V6StatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,22,101,1))
v6StatusEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:v6StatusEntry.setStatus(_A)
class _V6StatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_V6StatusIndex_Type.__name__=_D
_V6StatusIndex_Object=MibTableColumn
v6StatusIndex=_V6StatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,22,101,1,1),_V6StatusIndex_Type())
v6StatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:v6StatusIndex.setStatus(_A)
class _V6StatusIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_V6StatusIp_Type.__name__=_C
_V6StatusIp_Object=MibTableColumn
v6StatusIp=_V6StatusIp_Object((1,3,6,1,4,1,3181,10,6,1,22,101,1,2),_V6StatusIp_Type())
v6StatusIp.setMaxAccess(_E)
if mibBuilder.loadTexts:v6StatusIp.setStatus(_A)
class _V6StatusScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('link',0),('site',1),('global',2),('other',3)))
_V6StatusScope_Type.__name__=_D
_V6StatusScope_Object=MibTableColumn
v6StatusScope=_V6StatusScope_Object((1,3,6,1,4,1,3181,10,6,1,22,101,1,3),_V6StatusScope_Type())
v6StatusScope.setMaxAccess(_E)
if mibBuilder.loadTexts:v6StatusScope.setStatus(_A)
class _V6StatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('stateless',0),('stateful',1),('both',2),('other',3)))
_V6StatusState_Type.__name__=_D
_V6StatusState_Object=MibTableColumn
v6StatusState=_V6StatusState_Object((1,3,6,1,4,1,3181,10,6,1,22,101,1,4),_V6StatusState_Type())
v6StatusState.setMaxAccess(_E)
if mibBuilder.loadTexts:v6StatusState.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'device':device,'ip':ip,'ipPingTest':ipPingTest,'ipTraceRoute':ipTraceRoute,'ipDnsLookup':ipDnsLookup,'ipArpTable':ipArpTable,'ipHostname':ipHostname,'ipLocalMtu':ipLocalMtu,'v4ConfigTable':v4ConfigTable,'v4ConfigEntry':v4ConfigEntry,_J:v4ConfigIndex,'v4ConfigDhcpMode':v4ConfigDhcpMode,'v4ConfigStaticDeviceIp':v4ConfigStaticDeviceIp,'v4ConfigStaticSubnetMask':v4ConfigStaticSubnetMask,'v4ConfigStaticGateway':v4ConfigStaticGateway,'v4ConfigStaticDnsServer':v4ConfigStaticDnsServer,'v4ConfigSecondaryDeviceIp':v4ConfigSecondaryDeviceIp,'v4ConfigSecondarySubnetMask':v4ConfigSecondarySubnetMask,'v4ConfigDefaultAddressSelection':v4ConfigDefaultAddressSelection,'v6ConfigTable':v6ConfigTable,'v6ConfigEntry':v6ConfigEntry,_K:v6ConfigIndex,'v6ConfigEnableIpv6':v6ConfigEnableIpv6,'v6ConfigEnableIcmpAutoAddress':v6ConfigEnableIcmpAutoAddress,'v6ConfigEnableDhcpAutoAddress':v6ConfigEnableDhcpAutoAddress,'v6AddressTable':v6AddressTable,'v6AddressEntry':v6AddressEntry,_L:v6AddressIndex,'v6AddressIp':v6AddressIp,'v4StatusTable':v4StatusTable,'v4StatusEntry':v4StatusEntry,_M:v4StatusIndex,'v4StatusDynamicDeviceIp':v4StatusDynamicDeviceIp,'v4StatusDynamicSubnetMask':v4StatusDynamicSubnetMask,'v4StatusDynamicGateway':v4StatusDynamicGateway,'v4StatusDynamicDnsServer1':v4StatusDynamicDnsServer1,'v4StatusDynamicDnsServer2':v4StatusDynamicDnsServer2,'v4StatusDynamicDnsServer3':v4StatusDynamicDnsServer3,'v4StatusDynamicDnsServer4':v4StatusDynamicDnsServer4,'v4StatusOutgoingDeviceIp':v4StatusOutgoingDeviceIp,'v6StatusTable':v6StatusTable,'v6StatusEntry':v6StatusEntry,_N:v6StatusIndex,'v6StatusIp':v6StatusIp,'v6StatusScope':v6StatusScope,'v6StatusState':v6StatusState})