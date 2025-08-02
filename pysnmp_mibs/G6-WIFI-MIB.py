_P='ipV4StatusIndex'
_O='statusIndex'
_N='permit'
_M='firewallRulesIndex'
_L='firewallConfigIndex'
_K='interfaceIndex'
_J='accessPointIndex'
_I='read-only'
_H='not-accessible'
_G='G6-WIFI-MIB'
_F='enabled'
_E='disabled'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Wifi_ObjectIdentity=ObjectIdentity
wifi=_Wifi_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,98))
class _WifiEnableWifi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WifiEnableWifi_Type.__name__=_C
_WifiEnableWifi_Object=MibScalar
wifiEnableWifi=_WifiEnableWifi_Object((1,3,6,1,4,1,3181,10,6,1,98,1),_WifiEnableWifi_Type())
wifiEnableWifi.setMaxAccess(_B)
if mibBuilder.loadTexts:wifiEnableWifi.setStatus(_A)
_AccessPointTable_Object=MibTable
accessPointTable=_AccessPointTable_Object((1,3,6,1,4,1,3181,10,6,1,98,2))
if mibBuilder.loadTexts:accessPointTable.setStatus(_A)
_AccessPointEntry_Object=MibTableRow
accessPointEntry=_AccessPointEntry_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1))
accessPointEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:accessPointEntry.setStatus(_A)
class _AccessPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_AccessPointIndex_Type.__name__=_C
_AccessPointIndex_Object=MibTableColumn
accessPointIndex=_AccessPointIndex_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,1),_AccessPointIndex_Type())
accessPointIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:accessPointIndex.setStatus(_A)
_AccessPointHostname_Type=DisplayString
_AccessPointHostname_Object=MibTableColumn
accessPointHostname=_AccessPointHostname_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,2),_AccessPointHostname_Type())
accessPointHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:accessPointHostname.setStatus(_A)
class _AccessPointDeviceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AccessPointDeviceIp_Type.__name__=_D
_AccessPointDeviceIp_Object=MibTableColumn
accessPointDeviceIp=_AccessPointDeviceIp_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,3),_AccessPointDeviceIp_Type())
accessPointDeviceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:accessPointDeviceIp.setStatus(_A)
class _AccessPointSubnetMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AccessPointSubnetMask_Type.__name__=_D
_AccessPointSubnetMask_Object=MibTableColumn
accessPointSubnetMask=_AccessPointSubnetMask_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,4),_AccessPointSubnetMask_Type())
accessPointSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:accessPointSubnetMask.setStatus(_A)
class _AccessPointGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AccessPointGateway_Type.__name__=_D
_AccessPointGateway_Object=MibTableColumn
accessPointGateway=_AccessPointGateway_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,5),_AccessPointGateway_Type())
accessPointGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:accessPointGateway.setStatus(_A)
_AccessPointUpdateFirmware_Type=DisplayString
_AccessPointUpdateFirmware_Object=MibTableColumn
accessPointUpdateFirmware=_AccessPointUpdateFirmware_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,6),_AccessPointUpdateFirmware_Type())
accessPointUpdateFirmware.setMaxAccess(_B)
if mibBuilder.loadTexts:accessPointUpdateFirmware.setStatus(_A)
_AccessPointReboot_Type=DisplayString
_AccessPointReboot_Object=MibTableColumn
accessPointReboot=_AccessPointReboot_Object((1,3,6,1,4,1,3181,10,6,1,98,2,1,7),_AccessPointReboot_Type())
accessPointReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:accessPointReboot.setStatus(_A)
_InterfaceTable_Object=MibTable
interfaceTable=_InterfaceTable_Object((1,3,6,1,4,1,3181,10,6,1,98,3))
if mibBuilder.loadTexts:interfaceTable.setStatus(_A)
_InterfaceEntry_Object=MibTableRow
interfaceEntry=_InterfaceEntry_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1))
interfaceEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:interfaceEntry.setStatus(_A)
class _InterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_InterfaceIndex_Type.__name__=_C
_InterfaceIndex_Object=MibTableColumn
interfaceIndex=_InterfaceIndex_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,1),_InterfaceIndex_Type())
interfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:interfaceIndex.setStatus(_A)
_InterfaceCountryCode_Type=DisplayString
_InterfaceCountryCode_Object=MibTableColumn
interfaceCountryCode=_InterfaceCountryCode_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,2),_InterfaceCountryCode_Type())
interfaceCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceCountryCode.setStatus(_A)
_InterfaceSsid_Type=DisplayString
_InterfaceSsid_Object=MibTableColumn
interfaceSsid=_InterfaceSsid_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,3),_InterfaceSsid_Type())
interfaceSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceSsid.setStatus(_A)
_InterfaceEnterPresharedKey_Type=DisplayString
_InterfaceEnterPresharedKey_Object=MibTableColumn
interfaceEnterPresharedKey=_InterfaceEnterPresharedKey_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,4),_InterfaceEnterPresharedKey_Type())
interfaceEnterPresharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceEnterPresharedKey.setStatus(_A)
_InterfaceEncryptedPresharedKey_Type=DisplayString
_InterfaceEncryptedPresharedKey_Object=MibTableColumn
interfaceEncryptedPresharedKey=_InterfaceEncryptedPresharedKey_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,5),_InterfaceEncryptedPresharedKey_Type())
interfaceEncryptedPresharedKey.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceEncryptedPresharedKey.setStatus(_A)
class _InterfaceExposeSsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hidden',0),('visible',1)))
_InterfaceExposeSsid_Type.__name__=_C
_InterfaceExposeSsid_Object=MibTableColumn
interfaceExposeSsid=_InterfaceExposeSsid_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,6),_InterfaceExposeSsid_Type())
interfaceExposeSsid.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceExposeSsid.setStatus(_A)
class _InterfaceEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('wep',1),('wpaPsk',2),('wpaPsk2',3)))
_InterfaceEncryption_Type.__name__=_C
_InterfaceEncryption_Object=MibTableColumn
interfaceEncryption=_InterfaceEncryption_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,7),_InterfaceEncryption_Type())
interfaceEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceEncryption.setStatus(_A)
class _InterfaceDhcpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_InterfaceDhcpServer_Type.__name__=_C
_InterfaceDhcpServer_Object=MibTableColumn
interfaceDhcpServer=_InterfaceDhcpServer_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,8),_InterfaceDhcpServer_Type())
interfaceDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceDhcpServer.setStatus(_A)
class _InterfaceDhcpStartAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_InterfaceDhcpStartAddress_Type.__name__=_D
_InterfaceDhcpStartAddress_Object=MibTableColumn
interfaceDhcpStartAddress=_InterfaceDhcpStartAddress_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,9),_InterfaceDhcpStartAddress_Type())
interfaceDhcpStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceDhcpStartAddress.setStatus(_A)
class _InterfaceDhcpNumberOfAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_InterfaceDhcpNumberOfAddresses_Type.__name__=_C
_InterfaceDhcpNumberOfAddresses_Object=MibTableColumn
interfaceDhcpNumberOfAddresses=_InterfaceDhcpNumberOfAddresses_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,10),_InterfaceDhcpNumberOfAddresses_Type())
interfaceDhcpNumberOfAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceDhcpNumberOfAddresses.setStatus(_A)
_InterfaceChannelNumber_Type=Unsigned32
_InterfaceChannelNumber_Object=MibTableColumn
interfaceChannelNumber=_InterfaceChannelNumber_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,11),_InterfaceChannelNumber_Type())
interfaceChannelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceChannelNumber.setStatus(_A)
class _InterfaceChannelWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ht20',1),('ht40p',2),('ht40n',3)))
_InterfaceChannelWidth_Type.__name__=_C
_InterfaceChannelWidth_Object=MibTableColumn
interfaceChannelWidth=_InterfaceChannelWidth_Object((1,3,6,1,4,1,3181,10,6,1,98,3,1,12),_InterfaceChannelWidth_Type())
interfaceChannelWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceChannelWidth.setStatus(_A)
_FirewallConfigTable_Object=MibTable
firewallConfigTable=_FirewallConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,98,4))
if mibBuilder.loadTexts:firewallConfigTable.setStatus(_A)
_FirewallConfigEntry_Object=MibTableRow
firewallConfigEntry=_FirewallConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1))
firewallConfigEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:firewallConfigEntry.setStatus(_A)
class _FirewallConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_FirewallConfigIndex_Type.__name__=_C
_FirewallConfigIndex_Object=MibTableColumn
firewallConfigIndex=_FirewallConfigIndex_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,1),_FirewallConfigIndex_Type())
firewallConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:firewallConfigIndex.setStatus(_A)
class _FirewallConfigEnableIngressFirewall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FirewallConfigEnableIngressFirewall_Type.__name__=_C
_FirewallConfigEnableIngressFirewall_Object=MibTableColumn
firewallConfigEnableIngressFirewall=_FirewallConfigEnableIngressFirewall_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,2),_FirewallConfigEnableIngressFirewall_Type())
firewallConfigEnableIngressFirewall.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallConfigEnableIngressFirewall.setStatus(_A)
class _FirewallConfigEnableEgressFirewall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FirewallConfigEnableEgressFirewall_Type.__name__=_C
_FirewallConfigEnableEgressFirewall_Object=MibTableColumn
firewallConfigEnableEgressFirewall=_FirewallConfigEnableEgressFirewall_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,3),_FirewallConfigEnableEgressFirewall_Type())
firewallConfigEnableEgressFirewall.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallConfigEnableEgressFirewall.setStatus(_A)
class _FirewallConfigDropInvalidPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FirewallConfigDropInvalidPackets_Type.__name__=_C
_FirewallConfigDropInvalidPackets_Object=MibTableColumn
firewallConfigDropInvalidPackets=_FirewallConfigDropInvalidPackets_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,4),_FirewallConfigDropInvalidPackets_Type())
firewallConfigDropInvalidPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallConfigDropInvalidPackets.setStatus(_A)
class _FirewallConfigSynRateLimiting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FirewallConfigSynRateLimiting_Type.__name__=_C
_FirewallConfigSynRateLimiting_Object=MibTableColumn
firewallConfigSynRateLimiting=_FirewallConfigSynRateLimiting_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,5),_FirewallConfigSynRateLimiting_Type())
firewallConfigSynRateLimiting.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallConfigSynRateLimiting.setStatus(_A)
class _FirewallConfigUseSynCookies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FirewallConfigUseSynCookies_Type.__name__=_C
_FirewallConfigUseSynCookies_Object=MibTableColumn
firewallConfigUseSynCookies=_FirewallConfigUseSynCookies_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,6),_FirewallConfigUseSynCookies_Type())
firewallConfigUseSynCookies.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallConfigUseSynCookies.setStatus(_A)
class _FirewallConfigTcpWindowScaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_FirewallConfigTcpWindowScaling_Type.__name__=_C
_FirewallConfigTcpWindowScaling_Object=MibTableColumn
firewallConfigTcpWindowScaling=_FirewallConfigTcpWindowScaling_Object((1,3,6,1,4,1,3181,10,6,1,98,4,1,7),_FirewallConfigTcpWindowScaling_Type())
firewallConfigTcpWindowScaling.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallConfigTcpWindowScaling.setStatus(_A)
_FirewallRulesTable_Object=MibTable
firewallRulesTable=_FirewallRulesTable_Object((1,3,6,1,4,1,3181,10,6,1,98,5))
if mibBuilder.loadTexts:firewallRulesTable.setStatus(_A)
_FirewallRulesEntry_Object=MibTableRow
firewallRulesEntry=_FirewallRulesEntry_Object((1,3,6,1,4,1,3181,10,6,1,98,5,1))
firewallRulesEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:firewallRulesEntry.setStatus(_A)
class _FirewallRulesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_FirewallRulesIndex_Type.__name__=_C
_FirewallRulesIndex_Object=MibTableColumn
firewallRulesIndex=_FirewallRulesIndex_Object((1,3,6,1,4,1,3181,10,6,1,98,5,1,1),_FirewallRulesIndex_Type())
firewallRulesIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:firewallRulesIndex.setStatus(_A)
_FirewallRulesIncomingAclList_Type=DisplayString
_FirewallRulesIncomingAclList_Object=MibTableColumn
firewallRulesIncomingAclList=_FirewallRulesIncomingAclList_Object((1,3,6,1,4,1,3181,10,6,1,98,5,1,2),_FirewallRulesIncomingAclList_Type())
firewallRulesIncomingAclList.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallRulesIncomingAclList.setStatus(_A)
class _FirewallRulesIncomingAclDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),(_N,1)))
_FirewallRulesIncomingAclDefault_Type.__name__=_C
_FirewallRulesIncomingAclDefault_Object=MibTableColumn
firewallRulesIncomingAclDefault=_FirewallRulesIncomingAclDefault_Object((1,3,6,1,4,1,3181,10,6,1,98,5,1,3),_FirewallRulesIncomingAclDefault_Type())
firewallRulesIncomingAclDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallRulesIncomingAclDefault.setStatus(_A)
_FirewallRulesOutgoingAclList_Type=DisplayString
_FirewallRulesOutgoingAclList_Object=MibTableColumn
firewallRulesOutgoingAclList=_FirewallRulesOutgoingAclList_Object((1,3,6,1,4,1,3181,10,6,1,98,5,1,4),_FirewallRulesOutgoingAclList_Type())
firewallRulesOutgoingAclList.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallRulesOutgoingAclList.setStatus(_A)
class _FirewallRulesOutgoingAclDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),(_N,1)))
_FirewallRulesOutgoingAclDefault_Type.__name__=_C
_FirewallRulesOutgoingAclDefault_Object=MibTableColumn
firewallRulesOutgoingAclDefault=_FirewallRulesOutgoingAclDefault_Object((1,3,6,1,4,1,3181,10,6,1,98,5,1,5),_FirewallRulesOutgoingAclDefault_Type())
firewallRulesOutgoingAclDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:firewallRulesOutgoingAclDefault.setStatus(_A)
_StatusTable_Object=MibTable
statusTable=_StatusTable_Object((1,3,6,1,4,1,3181,10,6,1,98,100))
if mibBuilder.loadTexts:statusTable.setStatus(_A)
_StatusEntry_Object=MibTableRow
statusEntry=_StatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,98,100,1))
statusEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:statusEntry.setStatus(_A)
class _StatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_StatusIndex_Type.__name__=_C
_StatusIndex_Object=MibTableColumn
statusIndex=_StatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,98,100,1,1),_StatusIndex_Type())
statusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:statusIndex.setStatus(_A)
class _StatusOverallStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notPresent',0),(_E,1),('fault',2),('operational',3)))
_StatusOverallStatus_Type.__name__=_C
_StatusOverallStatus_Object=MibTableColumn
statusOverallStatus=_StatusOverallStatus_Object((1,3,6,1,4,1,3181,10,6,1,98,100,1,2),_StatusOverallStatus_Type())
statusOverallStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:statusOverallStatus.setStatus(_A)
_StatusNumberOfConnections_Type=Unsigned32
_StatusNumberOfConnections_Object=MibTableColumn
statusNumberOfConnections=_StatusNumberOfConnections_Object((1,3,6,1,4,1,3181,10,6,1,98,100,1,3),_StatusNumberOfConnections_Type())
statusNumberOfConnections.setMaxAccess(_I)
if mibBuilder.loadTexts:statusNumberOfConnections.setStatus(_A)
_IpV4StatusTable_Object=MibTable
ipV4StatusTable=_IpV4StatusTable_Object((1,3,6,1,4,1,3181,10,6,1,98,101))
if mibBuilder.loadTexts:ipV4StatusTable.setStatus(_A)
_IpV4StatusEntry_Object=MibTableRow
ipV4StatusEntry=_IpV4StatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,98,101,1))
ipV4StatusEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:ipV4StatusEntry.setStatus(_A)
class _IpV4StatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_IpV4StatusIndex_Type.__name__=_C
_IpV4StatusIndex_Object=MibTableColumn
ipV4StatusIndex=_IpV4StatusIndex_Object((1,3,6,1,4,1,3181,10,6,1,98,101,1,1),_IpV4StatusIndex_Type())
ipV4StatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipV4StatusIndex.setStatus(_A)
class _IpV4StatusDynamicDeviceIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IpV4StatusDynamicDeviceIp_Type.__name__=_D
_IpV4StatusDynamicDeviceIp_Object=MibTableColumn
ipV4StatusDynamicDeviceIp=_IpV4StatusDynamicDeviceIp_Object((1,3,6,1,4,1,3181,10,6,1,98,101,1,2),_IpV4StatusDynamicDeviceIp_Type())
ipV4StatusDynamicDeviceIp.setMaxAccess(_I)
if mibBuilder.loadTexts:ipV4StatusDynamicDeviceIp.setStatus(_A)
class _IpV4StatusDynamicSubnetMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IpV4StatusDynamicSubnetMask_Type.__name__=_D
_IpV4StatusDynamicSubnetMask_Object=MibTableColumn
ipV4StatusDynamicSubnetMask=_IpV4StatusDynamicSubnetMask_Object((1,3,6,1,4,1,3181,10,6,1,98,101,1,3),_IpV4StatusDynamicSubnetMask_Type())
ipV4StatusDynamicSubnetMask.setMaxAccess(_I)
if mibBuilder.loadTexts:ipV4StatusDynamicSubnetMask.setStatus(_A)
class _IpV4StatusDynamicGateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IpV4StatusDynamicGateway_Type.__name__=_D
_IpV4StatusDynamicGateway_Object=MibTableColumn
ipV4StatusDynamicGateway=_IpV4StatusDynamicGateway_Object((1,3,6,1,4,1,3181,10,6,1,98,101,1,4),_IpV4StatusDynamicGateway_Type())
ipV4StatusDynamicGateway.setMaxAccess(_I)
if mibBuilder.loadTexts:ipV4StatusDynamicGateway.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'device':device,'wifi':wifi,'wifiEnableWifi':wifiEnableWifi,'accessPointTable':accessPointTable,'accessPointEntry':accessPointEntry,_J:accessPointIndex,'accessPointHostname':accessPointHostname,'accessPointDeviceIp':accessPointDeviceIp,'accessPointSubnetMask':accessPointSubnetMask,'accessPointGateway':accessPointGateway,'accessPointUpdateFirmware':accessPointUpdateFirmware,'accessPointReboot':accessPointReboot,'interfaceTable':interfaceTable,'interfaceEntry':interfaceEntry,_K:interfaceIndex,'interfaceCountryCode':interfaceCountryCode,'interfaceSsid':interfaceSsid,'interfaceEnterPresharedKey':interfaceEnterPresharedKey,'interfaceEncryptedPresharedKey':interfaceEncryptedPresharedKey,'interfaceExposeSsid':interfaceExposeSsid,'interfaceEncryption':interfaceEncryption,'interfaceDhcpServer':interfaceDhcpServer,'interfaceDhcpStartAddress':interfaceDhcpStartAddress,'interfaceDhcpNumberOfAddresses':interfaceDhcpNumberOfAddresses,'interfaceChannelNumber':interfaceChannelNumber,'interfaceChannelWidth':interfaceChannelWidth,'firewallConfigTable':firewallConfigTable,'firewallConfigEntry':firewallConfigEntry,_L:firewallConfigIndex,'firewallConfigEnableIngressFirewall':firewallConfigEnableIngressFirewall,'firewallConfigEnableEgressFirewall':firewallConfigEnableEgressFirewall,'firewallConfigDropInvalidPackets':firewallConfigDropInvalidPackets,'firewallConfigSynRateLimiting':firewallConfigSynRateLimiting,'firewallConfigUseSynCookies':firewallConfigUseSynCookies,'firewallConfigTcpWindowScaling':firewallConfigTcpWindowScaling,'firewallRulesTable':firewallRulesTable,'firewallRulesEntry':firewallRulesEntry,_M:firewallRulesIndex,'firewallRulesIncomingAclList':firewallRulesIncomingAclList,'firewallRulesIncomingAclDefault':firewallRulesIncomingAclDefault,'firewallRulesOutgoingAclList':firewallRulesOutgoingAclList,'firewallRulesOutgoingAclDefault':firewallRulesOutgoingAclDefault,'statusTable':statusTable,'statusEntry':statusEntry,_O:statusIndex,'statusOverallStatus':statusOverallStatus,'statusNumberOfConnections':statusNumberOfConnections,'ipV4StatusTable':ipV4StatusTable,'ipV4StatusEntry':ipV4StatusEntry,_P:ipV4StatusIndex,'ipV4StatusDynamicDeviceIp':ipV4StatusDynamicDeviceIp,'ipV4StatusDynamicSubnetMask':ipV4StatusDynamicSubnetMask,'ipV4StatusDynamicGateway':ipV4StatusDynamicGateway})