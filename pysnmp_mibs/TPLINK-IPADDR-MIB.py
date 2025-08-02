_Y='tpPortChannelName'
_X='tpRoutedPortName'
_W='tpLoopbackInterfaceName'
_V='tpVlanInterfaceName'
_U='read-write'
_T='tpPortChannelSecondary'
_S='tpPortChannelIp'
_R='tpPortChannelId'
_Q='tpRoutedPortSecondary'
_P='tpRoutedPortIp'
_O='tpLoopbackInterfaceSecondary'
_N='tpLoopbackInterfaceIp'
_M='tpLoopbackInterfaceId'
_L='tpVlanInterfaceSecondary'
_K='tpVlanInterfaceIp'
_J='tpVlanInterfaceVlanId'
_I='manual'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='read-only'
_C='TPLINK-IPADDR-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkIpAddrMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,6))
if mibBuilder.loadTexts:tplinkIpAddrMIB.setRevisions(('2012-12-13 09:30',))
class TpInterfaceMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),(_I,1),('dhcp',2),('bootp',3)))
class TpInterfaceMode2(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),(_I,1)))
class TpPortLinkMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bridge',0),('route',1)))
_TplinkIpAddrMIBObjects_ObjectIdentity=ObjectIdentity
tplinkIpAddrMIBObjects=_TplinkIpAddrMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,6,1))
_TpInterfaceConfig_ObjectIdentity=ObjectIdentity
tpInterfaceConfig=_TpInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,6,1,1))
_TpVlanInterfaceTable_Object=MibTable
tpVlanInterfaceTable=_TpVlanInterfaceTable_Object((1,3,6,1,4,1,11863,6,6,1,1,1))
if mibBuilder.loadTexts:tpVlanInterfaceTable.setStatus(_A)
_TpVlanInterfaceConfigEntry_Object=MibTableRow
tpVlanInterfaceConfigEntry=_TpVlanInterfaceConfigEntry_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1))
tpVlanInterfaceConfigEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:tpVlanInterfaceConfigEntry.setStatus(_A)
_TpVlanInterfaceVlanId_Type=Integer32
_TpVlanInterfaceVlanId_Object=MibTableColumn
tpVlanInterfaceVlanId=_TpVlanInterfaceVlanId_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,1),_TpVlanInterfaceVlanId_Type())
tpVlanInterfaceVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpVlanInterfaceVlanId.setStatus(_A)
_TpVlanInterfaceSecondary_Type=Integer32
_TpVlanInterfaceSecondary_Object=MibTableColumn
tpVlanInterfaceSecondary=_TpVlanInterfaceSecondary_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,2),_TpVlanInterfaceSecondary_Type())
tpVlanInterfaceSecondary.setMaxAccess(_D)
if mibBuilder.loadTexts:tpVlanInterfaceSecondary.setStatus(_A)
_TpVlanInterfaceMode_Type=TpInterfaceMode
_TpVlanInterfaceMode_Object=MibTableColumn
tpVlanInterfaceMode=_TpVlanInterfaceMode_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,3),_TpVlanInterfaceMode_Type())
tpVlanInterfaceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVlanInterfaceMode.setStatus(_A)
_TpVlanInterfaceIp_Type=IpAddress
_TpVlanInterfaceIp_Object=MibTableColumn
tpVlanInterfaceIp=_TpVlanInterfaceIp_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,4),_TpVlanInterfaceIp_Type())
tpVlanInterfaceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpVlanInterfaceIp.setStatus(_A)
_TpVlanInterfaceMsk_Type=IpAddress
_TpVlanInterfaceMsk_Object=MibTableColumn
tpVlanInterfaceMsk=_TpVlanInterfaceMsk_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,5),_TpVlanInterfaceMsk_Type())
tpVlanInterfaceMsk.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVlanInterfaceMsk.setStatus(_A)
class _TpVlanInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TpVlanInterfaceName_Type.__name__=_E
_TpVlanInterfaceName_Object=MibTableColumn
tpVlanInterfaceName=_TpVlanInterfaceName_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,6),_TpVlanInterfaceName_Type())
tpVlanInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVlanInterfaceName.setStatus(_A)
class _TpVlanInterfaceDhcpOption12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TpVlanInterfaceDhcpOption12_Type.__name__=_E
_TpVlanInterfaceDhcpOption12_Object=MibTableColumn
tpVlanInterfaceDhcpOption12=_TpVlanInterfaceDhcpOption12_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,7),_TpVlanInterfaceDhcpOption12_Type())
tpVlanInterfaceDhcpOption12.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVlanInterfaceDhcpOption12.setStatus(_A)
_TpVlanInterfaceStatus_Type=TPRowStatus
_TpVlanInterfaceStatus_Object=MibTableColumn
tpVlanInterfaceStatus=_TpVlanInterfaceStatus_Object((1,3,6,1,4,1,11863,6,6,1,1,1,1,8),_TpVlanInterfaceStatus_Type())
tpVlanInterfaceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpVlanInterfaceStatus.setStatus(_A)
_TpLoopbackInterfaceTable_Object=MibTable
tpLoopbackInterfaceTable=_TpLoopbackInterfaceTable_Object((1,3,6,1,4,1,11863,6,6,1,1,2))
if mibBuilder.loadTexts:tpLoopbackInterfaceTable.setStatus(_A)
_TpLoopbackInterfaceConfigEntry_Object=MibTableRow
tpLoopbackInterfaceConfigEntry=_TpLoopbackInterfaceConfigEntry_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1))
tpLoopbackInterfaceConfigEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:tpLoopbackInterfaceConfigEntry.setStatus(_A)
_TpLoopbackInterfaceId_Type=Integer32
_TpLoopbackInterfaceId_Object=MibTableColumn
tpLoopbackInterfaceId=_TpLoopbackInterfaceId_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,1),_TpLoopbackInterfaceId_Type())
tpLoopbackInterfaceId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLoopbackInterfaceId.setStatus(_A)
_TpLoopbackInterfaceSecondary_Type=Integer32
_TpLoopbackInterfaceSecondary_Object=MibTableColumn
tpLoopbackInterfaceSecondary=_TpLoopbackInterfaceSecondary_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,2),_TpLoopbackInterfaceSecondary_Type())
tpLoopbackInterfaceSecondary.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLoopbackInterfaceSecondary.setStatus(_A)
_TpLoopbackInterfaceMode_Type=TpInterfaceMode2
_TpLoopbackInterfaceMode_Object=MibTableColumn
tpLoopbackInterfaceMode=_TpLoopbackInterfaceMode_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,3),_TpLoopbackInterfaceMode_Type())
tpLoopbackInterfaceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLoopbackInterfaceMode.setStatus(_A)
_TpLoopbackInterfaceIp_Type=IpAddress
_TpLoopbackInterfaceIp_Object=MibTableColumn
tpLoopbackInterfaceIp=_TpLoopbackInterfaceIp_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,4),_TpLoopbackInterfaceIp_Type())
tpLoopbackInterfaceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpLoopbackInterfaceIp.setStatus(_A)
_TpLoopbackInterfaceMsk_Type=IpAddress
_TpLoopbackInterfaceMsk_Object=MibTableColumn
tpLoopbackInterfaceMsk=_TpLoopbackInterfaceMsk_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,5),_TpLoopbackInterfaceMsk_Type())
tpLoopbackInterfaceMsk.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLoopbackInterfaceMsk.setStatus(_A)
class _TpLoopbackInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TpLoopbackInterfaceName_Type.__name__=_E
_TpLoopbackInterfaceName_Object=MibTableColumn
tpLoopbackInterfaceName=_TpLoopbackInterfaceName_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,6),_TpLoopbackInterfaceName_Type())
tpLoopbackInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLoopbackInterfaceName.setStatus(_A)
class _TpLoopbackInterfaceDhcpOption12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TpLoopbackInterfaceDhcpOption12_Type.__name__=_E
_TpLoopbackInterfaceDhcpOption12_Object=MibTableColumn
tpLoopbackInterfaceDhcpOption12=_TpLoopbackInterfaceDhcpOption12_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,7),_TpLoopbackInterfaceDhcpOption12_Type())
tpLoopbackInterfaceDhcpOption12.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLoopbackInterfaceDhcpOption12.setStatus(_A)
_TpLoopbackInterfaceStatus_Type=TPRowStatus
_TpLoopbackInterfaceStatus_Object=MibTableColumn
tpLoopbackInterfaceStatus=_TpLoopbackInterfaceStatus_Object((1,3,6,1,4,1,11863,6,6,1,1,2,1,8),_TpLoopbackInterfaceStatus_Type())
tpLoopbackInterfaceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpLoopbackInterfaceStatus.setStatus(_A)
_TpRoutedPortTable_Object=MibTable
tpRoutedPortTable=_TpRoutedPortTable_Object((1,3,6,1,4,1,11863,6,6,1,1,3))
if mibBuilder.loadTexts:tpRoutedPortTable.setStatus(_A)
_TpRoutedPortConfigEntry_Object=MibTableRow
tpRoutedPortConfigEntry=_TpRoutedPortConfigEntry_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1))
tpRoutedPortConfigEntry.setIndexNames((0,_F,_G),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:tpRoutedPortConfigEntry.setStatus(_A)
class _TpRoutedPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TpRoutedPortId_Type.__name__=_E
_TpRoutedPortId_Object=MibTableColumn
tpRoutedPortId=_TpRoutedPortId_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,1),_TpRoutedPortId_Type())
tpRoutedPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpRoutedPortId.setStatus(_A)
_TpRoutedPortSecondary_Type=Integer32
_TpRoutedPortSecondary_Object=MibTableColumn
tpRoutedPortSecondary=_TpRoutedPortSecondary_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,2),_TpRoutedPortSecondary_Type())
tpRoutedPortSecondary.setMaxAccess(_D)
if mibBuilder.loadTexts:tpRoutedPortSecondary.setStatus(_A)
_TpRoutedPortMode_Type=TpInterfaceMode
_TpRoutedPortMode_Object=MibTableColumn
tpRoutedPortMode=_TpRoutedPortMode_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,3),_TpRoutedPortMode_Type())
tpRoutedPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRoutedPortMode.setStatus(_A)
_TpRoutedPortIp_Type=IpAddress
_TpRoutedPortIp_Object=MibTableColumn
tpRoutedPortIp=_TpRoutedPortIp_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,4),_TpRoutedPortIp_Type())
tpRoutedPortIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpRoutedPortIp.setStatus(_A)
_TpRoutedPortMsk_Type=IpAddress
_TpRoutedPortMsk_Object=MibTableColumn
tpRoutedPortMsk=_TpRoutedPortMsk_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,5),_TpRoutedPortMsk_Type())
tpRoutedPortMsk.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRoutedPortMsk.setStatus(_A)
class _TpRoutedPortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TpRoutedPortName_Type.__name__=_E
_TpRoutedPortName_Object=MibTableColumn
tpRoutedPortName=_TpRoutedPortName_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,6),_TpRoutedPortName_Type())
tpRoutedPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRoutedPortName.setStatus(_A)
class _TpRoutedPortDhcpOption12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TpRoutedPortDhcpOption12_Type.__name__=_E
_TpRoutedPortDhcpOption12_Object=MibTableColumn
tpRoutedPortDhcpOption12=_TpRoutedPortDhcpOption12_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,7),_TpRoutedPortDhcpOption12_Type())
tpRoutedPortDhcpOption12.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRoutedPortDhcpOption12.setStatus(_A)
_TpRoutedPortStatus_Type=TPRowStatus
_TpRoutedPortStatus_Object=MibTableColumn
tpRoutedPortStatus=_TpRoutedPortStatus_Object((1,3,6,1,4,1,11863,6,6,1,1,3,1,8),_TpRoutedPortStatus_Type())
tpRoutedPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpRoutedPortStatus.setStatus(_A)
_TpPortChannelTable_Object=MibTable
tpPortChannelTable=_TpPortChannelTable_Object((1,3,6,1,4,1,11863,6,6,1,1,4))
if mibBuilder.loadTexts:tpPortChannelTable.setStatus(_A)
_TpPortChannelConfigEntry_Object=MibTableRow
tpPortChannelConfigEntry=_TpPortChannelConfigEntry_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1))
tpPortChannelConfigEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:tpPortChannelConfigEntry.setStatus(_A)
_TpPortChannelId_Type=Integer32
_TpPortChannelId_Object=MibTableColumn
tpPortChannelId=_TpPortChannelId_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,1),_TpPortChannelId_Type())
tpPortChannelId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPortChannelId.setStatus(_A)
_TpPortChannelSecondary_Type=Integer32
_TpPortChannelSecondary_Object=MibTableColumn
tpPortChannelSecondary=_TpPortChannelSecondary_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,2),_TpPortChannelSecondary_Type())
tpPortChannelSecondary.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPortChannelSecondary.setStatus(_A)
_TpPortChannelMode_Type=TpInterfaceMode
_TpPortChannelMode_Object=MibTableColumn
tpPortChannelMode=_TpPortChannelMode_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,3),_TpPortChannelMode_Type())
tpPortChannelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortChannelMode.setStatus(_A)
_TpPortChannelIp_Type=IpAddress
_TpPortChannelIp_Object=MibTableColumn
tpPortChannelIp=_TpPortChannelIp_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,4),_TpPortChannelIp_Type())
tpPortChannelIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPortChannelIp.setStatus(_A)
_TpPortChannelMsk_Type=IpAddress
_TpPortChannelMsk_Object=MibTableColumn
tpPortChannelMsk=_TpPortChannelMsk_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,5),_TpPortChannelMsk_Type())
tpPortChannelMsk.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortChannelMsk.setStatus(_A)
class _TpPortChannelName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TpPortChannelName_Type.__name__=_E
_TpPortChannelName_Object=MibTableColumn
tpPortChannelName=_TpPortChannelName_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,6),_TpPortChannelName_Type())
tpPortChannelName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortChannelName.setStatus(_A)
class _TpPortChannelDhcpOption12_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TpPortChannelDhcpOption12_Type.__name__=_E
_TpPortChannelDhcpOption12_Object=MibTableColumn
tpPortChannelDhcpOption12=_TpPortChannelDhcpOption12_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,7),_TpPortChannelDhcpOption12_Type())
tpPortChannelDhcpOption12.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortChannelDhcpOption12.setStatus(_A)
_TpPortChannelStatus_Type=TPRowStatus
_TpPortChannelStatus_Object=MibTableColumn
tpPortChannelStatus=_TpPortChannelStatus_Object((1,3,6,1,4,1,11863,6,6,1,1,4,1,8),_TpPortChannelStatus_Type())
tpPortChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortChannelStatus.setStatus(_A)
_TpInterfaceGatewayConfig_ObjectIdentity=ObjectIdentity
tpInterfaceGatewayConfig=_TpInterfaceGatewayConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,6,1,1,5))
_TpInterfaceGateway_Type=IpAddress
_TpInterfaceGateway_Object=MibScalar
tpInterfaceGateway=_TpInterfaceGateway_Object((1,3,6,1,4,1,11863,6,6,1,1,5,1),_TpInterfaceGateway_Type())
tpInterfaceGateway.setMaxAccess(_U)
if mibBuilder.loadTexts:tpInterfaceGateway.setStatus(_A)
_TplinkIpRoutingConfig_ObjectIdentity=ObjectIdentity
tplinkIpRoutingConfig=_TplinkIpRoutingConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,6,2))
class _TpIpRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_TpIpRouting_Type.__name__=_H
_TpIpRouting_Object=MibScalar
tpIpRouting=_TpIpRouting_Object((1,3,6,1,4,1,11863,6,6,2,1),_TpIpRouting_Type())
tpIpRouting.setMaxAccess(_U)
if mibBuilder.loadTexts:tpIpRouting.setStatus(_A)
_TplinkIpAddrNotifications_ObjectIdentity=ObjectIdentity
tplinkIpAddrNotifications=_TplinkIpAddrNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,6,3))
vlanInterfaceIpChange=NotificationType((1,3,6,1,4,1,11863,6,6,3,1))
vlanInterfaceIpChange.setObjects((_C,_V))
if mibBuilder.loadTexts:vlanInterfaceIpChange.setStatus(_A)
loopbackInterfaceIpChange=NotificationType((1,3,6,1,4,1,11863,6,6,3,2))
loopbackInterfaceIpChange.setObjects((_C,_W))
if mibBuilder.loadTexts:loopbackInterfaceIpChange.setStatus(_A)
routedPortIpChange=NotificationType((1,3,6,1,4,1,11863,6,6,3,3))
routedPortIpChange.setObjects((_C,_X))
if mibBuilder.loadTexts:routedPortIpChange.setStatus(_A)
portChannelIpChange=NotificationType((1,3,6,1,4,1,11863,6,6,3,4))
portChannelIpChange.setObjects((_C,_Y))
if mibBuilder.loadTexts:portChannelIpChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'TpInterfaceMode':TpInterfaceMode,'TpInterfaceMode2':TpInterfaceMode2,'TpPortLinkMode':TpPortLinkMode,'tplinkIpAddrMIB':tplinkIpAddrMIB,'tplinkIpAddrMIBObjects':tplinkIpAddrMIBObjects,'tpInterfaceConfig':tpInterfaceConfig,'tpVlanInterfaceTable':tpVlanInterfaceTable,'tpVlanInterfaceConfigEntry':tpVlanInterfaceConfigEntry,_J:tpVlanInterfaceVlanId,_L:tpVlanInterfaceSecondary,'tpVlanInterfaceMode':tpVlanInterfaceMode,_K:tpVlanInterfaceIp,'tpVlanInterfaceMsk':tpVlanInterfaceMsk,_V:tpVlanInterfaceName,'tpVlanInterfaceDhcpOption12':tpVlanInterfaceDhcpOption12,'tpVlanInterfaceStatus':tpVlanInterfaceStatus,'tpLoopbackInterfaceTable':tpLoopbackInterfaceTable,'tpLoopbackInterfaceConfigEntry':tpLoopbackInterfaceConfigEntry,_M:tpLoopbackInterfaceId,_O:tpLoopbackInterfaceSecondary,'tpLoopbackInterfaceMode':tpLoopbackInterfaceMode,_N:tpLoopbackInterfaceIp,'tpLoopbackInterfaceMsk':tpLoopbackInterfaceMsk,_W:tpLoopbackInterfaceName,'tpLoopbackInterfaceDhcpOption12':tpLoopbackInterfaceDhcpOption12,'tpLoopbackInterfaceStatus':tpLoopbackInterfaceStatus,'tpRoutedPortTable':tpRoutedPortTable,'tpRoutedPortConfigEntry':tpRoutedPortConfigEntry,'tpRoutedPortId':tpRoutedPortId,_Q:tpRoutedPortSecondary,'tpRoutedPortMode':tpRoutedPortMode,_P:tpRoutedPortIp,'tpRoutedPortMsk':tpRoutedPortMsk,_X:tpRoutedPortName,'tpRoutedPortDhcpOption12':tpRoutedPortDhcpOption12,'tpRoutedPortStatus':tpRoutedPortStatus,'tpPortChannelTable':tpPortChannelTable,'tpPortChannelConfigEntry':tpPortChannelConfigEntry,_R:tpPortChannelId,_T:tpPortChannelSecondary,'tpPortChannelMode':tpPortChannelMode,_S:tpPortChannelIp,'tpPortChannelMsk':tpPortChannelMsk,_Y:tpPortChannelName,'tpPortChannelDhcpOption12':tpPortChannelDhcpOption12,'tpPortChannelStatus':tpPortChannelStatus,'tpInterfaceGatewayConfig':tpInterfaceGatewayConfig,'tpInterfaceGateway':tpInterfaceGateway,'tplinkIpRoutingConfig':tplinkIpRoutingConfig,'tpIpRouting':tpIpRouting,'tplinkIpAddrNotifications':tplinkIpAddrNotifications,'vlanInterfaceIpChange':vlanInterfaceIpChange,'loopbackInterfaceIpChange':loopbackInterfaceIpChange,'routedPortIpChange':routedPortIpChange,'portChannelIpChange':portChannelIpChange})