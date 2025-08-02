_N='ipv6ParaConfigCfgIfIndex'
_M='read-create'
_L='ipv6ParaConfigAddress'
_K='ipv6ParaConfigSourceType'
_J='ipv6ParaConfigAddrType'
_I='ipv6ParaConfigIfIndex'
_H='OctetString'
_G='enable'
_F='disable'
_E='read-write'
_D='TPLINK-IPV6ADDR-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkIpv6AddrMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,50))
if mibBuilder.loadTexts:tplinkIpv6AddrMIB.setRevisions(('2012-12-13 09:30',))
_TplinkIpv6AddrMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpv6AddrMIBObjects=_TplinkIpv6AddrMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,50,1))
_Ipv6ParaConfigAddrTable_Object=MibTable
ipv6ParaConfigAddrTable=_Ipv6ParaConfigAddrTable_Object((1,3,6,1,4,1,11863,6,50,1,1))
if mibBuilder.loadTexts:ipv6ParaConfigAddrTable.setStatus(_A)
_Ipv6ParaConfigAddrEntry_Object=MibTableRow
ipv6ParaConfigAddrEntry=_Ipv6ParaConfigAddrEntry_Object((1,3,6,1,4,1,11863,6,50,1,1,1))
ipv6ParaConfigAddrEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:ipv6ParaConfigAddrEntry.setStatus(_A)
_Ipv6ParaConfigIfIndex_Type=Integer32
_Ipv6ParaConfigIfIndex_Object=MibTableColumn
ipv6ParaConfigIfIndex=_Ipv6ParaConfigIfIndex_Object((1,3,6,1,4,1,11863,6,50,1,1,1,1),_Ipv6ParaConfigIfIndex_Type())
ipv6ParaConfigIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigIfIndex.setStatus(_A)
_Ipv6ParaConfigIfDescription_Type=DisplayString
_Ipv6ParaConfigIfDescription_Object=MibTableColumn
ipv6ParaConfigIfDescription=_Ipv6ParaConfigIfDescription_Object((1,3,6,1,4,1,11863,6,50,1,1,1,2),_Ipv6ParaConfigIfDescription_Type())
ipv6ParaConfigIfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigIfDescription.setStatus(_A)
_Ipv6ParaConfigAddrType_Type=InetAddressType
_Ipv6ParaConfigAddrType_Object=MibTableColumn
ipv6ParaConfigAddrType=_Ipv6ParaConfigAddrType_Object((1,3,6,1,4,1,11863,6,50,1,1,1,3),_Ipv6ParaConfigAddrType_Type())
ipv6ParaConfigAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigAddrType.setStatus(_A)
_Ipv6ParaConfigAddress_Type=InetAddress
_Ipv6ParaConfigAddress_Object=MibTableColumn
ipv6ParaConfigAddress=_Ipv6ParaConfigAddress_Object((1,3,6,1,4,1,11863,6,50,1,1,1,4),_Ipv6ParaConfigAddress_Type())
ipv6ParaConfigAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigAddress.setStatus(_A)
class _Ipv6ParaConfigPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_Ipv6ParaConfigPrefixLength_Type.__name__=_B
_Ipv6ParaConfigPrefixLength_Object=MibTableColumn
ipv6ParaConfigPrefixLength=_Ipv6ParaConfigPrefixLength_Object((1,3,6,1,4,1,11863,6,50,1,1,1,5),_Ipv6ParaConfigPrefixLength_Type())
ipv6ParaConfigPrefixLength.setMaxAccess(_M)
if mibBuilder.loadTexts:ipv6ParaConfigPrefixLength.setStatus(_A)
class _Ipv6ParaConfigSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('assignedIp',1),('assignedEUI64Ip',2),('assignedLinklocalIp',3),('autoIp',4),('dhcpv6',5),('negotiate',6)))
_Ipv6ParaConfigSourceType_Type.__name__=_B
_Ipv6ParaConfigSourceType_Object=MibTableColumn
ipv6ParaConfigSourceType=_Ipv6ParaConfigSourceType_Object((1,3,6,1,4,1,11863,6,50,1,1,1,6),_Ipv6ParaConfigSourceType_Type())
ipv6ParaConfigSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigSourceType.setStatus(_A)
_Ipv6ParaConfigRowStatus_Type=RowStatus
_Ipv6ParaConfigRowStatus_Object=MibTableColumn
ipv6ParaConfigRowStatus=_Ipv6ParaConfigRowStatus_Object((1,3,6,1,4,1,11863,6,50,1,1,1,7),_Ipv6ParaConfigRowStatus_Type())
ipv6ParaConfigRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:ipv6ParaConfigRowStatus.setStatus(_A)
_Ipv6ParaConfigCfgTable_Object=MibTable
ipv6ParaConfigCfgTable=_Ipv6ParaConfigCfgTable_Object((1,3,6,1,4,1,11863,6,50,1,2))
if mibBuilder.loadTexts:ipv6ParaConfigCfgTable.setStatus(_A)
_Ipv6ParaConfigCfgEntry_Object=MibTableRow
ipv6ParaConfigCfgEntry=_Ipv6ParaConfigCfgEntry_Object((1,3,6,1,4,1,11863,6,50,1,2,1))
ipv6ParaConfigCfgEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:ipv6ParaConfigCfgEntry.setStatus(_A)
_Ipv6ParaConfigCfgIfIndex_Type=Integer32
_Ipv6ParaConfigCfgIfIndex_Object=MibTableColumn
ipv6ParaConfigCfgIfIndex=_Ipv6ParaConfigCfgIfIndex_Object((1,3,6,1,4,1,11863,6,50,1,2,1,1),_Ipv6ParaConfigCfgIfIndex_Type())
ipv6ParaConfigCfgIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigCfgIfIndex.setStatus(_A)
_Ipv6ParaConfigCfgIfDescription_Type=DisplayString
_Ipv6ParaConfigCfgIfDescription_Object=MibTableColumn
ipv6ParaConfigCfgIfDescription=_Ipv6ParaConfigCfgIfDescription_Object((1,3,6,1,4,1,11863,6,50,1,2,1,2),_Ipv6ParaConfigCfgIfDescription_Type())
ipv6ParaConfigCfgIfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ipv6ParaConfigCfgIfDescription.setStatus(_A)
class _Ipv6ParaConfigAutoLinkLocalEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Ipv6ParaConfigAutoLinkLocalEnable_Type.__name__=_B
_Ipv6ParaConfigAutoLinkLocalEnable_Object=MibTableColumn
ipv6ParaConfigAutoLinkLocalEnable=_Ipv6ParaConfigAutoLinkLocalEnable_Object((1,3,6,1,4,1,11863,6,50,1,2,1,3),_Ipv6ParaConfigAutoLinkLocalEnable_Type())
ipv6ParaConfigAutoLinkLocalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6ParaConfigAutoLinkLocalEnable.setStatus(_A)
class _Ipv6ParaConfigDhcpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Ipv6ParaConfigDhcpEnable_Type.__name__=_B
_Ipv6ParaConfigDhcpEnable_Object=MibTableColumn
ipv6ParaConfigDhcpEnable=_Ipv6ParaConfigDhcpEnable_Object((1,3,6,1,4,1,11863,6,50,1,2,1,4),_Ipv6ParaConfigDhcpEnable_Type())
ipv6ParaConfigDhcpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6ParaConfigDhcpEnable.setStatus(_A)
class _Ipv6ParaConfigNegotiateEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Ipv6ParaConfigNegotiateEnable_Type.__name__=_B
_Ipv6ParaConfigNegotiateEnable_Object=MibTableColumn
ipv6ParaConfigNegotiateEnable=_Ipv6ParaConfigNegotiateEnable_Object((1,3,6,1,4,1,11863,6,50,1,2,1,5),_Ipv6ParaConfigNegotiateEnable_Type())
ipv6ParaConfigNegotiateEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6ParaConfigNegotiateEnable.setStatus(_A)
class _Ipv6ParaConfigIPv6Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Ipv6ParaConfigIPv6Enable_Type.__name__=_B
_Ipv6ParaConfigIPv6Enable_Object=MibTableColumn
ipv6ParaConfigIPv6Enable=_Ipv6ParaConfigIPv6Enable_Object((1,3,6,1,4,1,11863,6,50,1,2,1,6),_Ipv6ParaConfigIPv6Enable_Type())
ipv6ParaConfigIPv6Enable.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6ParaConfigIPv6Enable.setStatus(_A)
_Ipv6GatewayConfig_ObjectIdentity=ObjectIdentity
ipv6GatewayConfig=_Ipv6GatewayConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,50,1,3))
class _Ipv6Gateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(46,46));fixedLength=46
_Ipv6Gateway_Type.__name__=_H
_Ipv6Gateway_Object=MibScalar
ipv6Gateway=_Ipv6Gateway_Object((1,3,6,1,4,1,11863,6,50,1,3,1),_Ipv6Gateway_Type())
ipv6Gateway.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6Gateway.setStatus(_A)
_TplinkIpv6RoutingConfig_ObjectIdentity=ObjectIdentity
tplinkIpv6RoutingConfig=_TplinkIpv6RoutingConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,50,2))
class _TpIpv6Routing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIpv6Routing_Type.__name__=_B
_TpIpv6Routing_Object=MibScalar
tpIpv6Routing=_TpIpv6Routing_Object((1,3,6,1,4,1,11863,6,50,2,1),_TpIpv6Routing_Type())
tpIpv6Routing.setMaxAccess(_E)
if mibBuilder.loadTexts:tpIpv6Routing.setStatus(_A)
_TplinkIpv6AddrNotifications_ObjectIdentity=ObjectIdentity
tplinkIpv6AddrNotifications=_TplinkIpv6AddrNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,50,3))
mibBuilder.exportSymbols(_D,**{'tplinkIpv6AddrMIB':tplinkIpv6AddrMIB,'tplinkIpv6AddrMIBObjects':tplinkIpv6AddrMIBObjects,'ipv6ParaConfigAddrTable':ipv6ParaConfigAddrTable,'ipv6ParaConfigAddrEntry':ipv6ParaConfigAddrEntry,_I:ipv6ParaConfigIfIndex,'ipv6ParaConfigIfDescription':ipv6ParaConfigIfDescription,_J:ipv6ParaConfigAddrType,_L:ipv6ParaConfigAddress,'ipv6ParaConfigPrefixLength':ipv6ParaConfigPrefixLength,_K:ipv6ParaConfigSourceType,'ipv6ParaConfigRowStatus':ipv6ParaConfigRowStatus,'ipv6ParaConfigCfgTable':ipv6ParaConfigCfgTable,'ipv6ParaConfigCfgEntry':ipv6ParaConfigCfgEntry,_N:ipv6ParaConfigCfgIfIndex,'ipv6ParaConfigCfgIfDescription':ipv6ParaConfigCfgIfDescription,'ipv6ParaConfigAutoLinkLocalEnable':ipv6ParaConfigAutoLinkLocalEnable,'ipv6ParaConfigDhcpEnable':ipv6ParaConfigDhcpEnable,'ipv6ParaConfigNegotiateEnable':ipv6ParaConfigNegotiateEnable,'ipv6ParaConfigIPv6Enable':ipv6ParaConfigIPv6Enable,'ipv6GatewayConfig':ipv6GatewayConfig,'ipv6Gateway':ipv6Gateway,'tplinkIpv6RoutingConfig':tplinkIpv6RoutingConfig,'tpIpv6Routing':tpIpv6Routing,'tplinkIpv6AddrNotifications':tplinkIpv6AddrNotifications})