_Q='dhcpRelayVlanRelayServerIp'
_P='dhcpRelayVlanRelayServerVlanId'
_O='dhcpRelayServerPortChannelInterfaceIp'
_N='dhcpRelayServerRoutedPortInterfaceIp'
_M='dhcpRelayServerVlanInterfaceIp'
_L='dhcpRelayServerVlanId'
_K='read-create'
_J='enable'
_I='disable'
_H='ifIndex'
_G='IF-MIB'
_F='TPLINK-DHCPRELAY-MIB'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkDhcpRelayMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,39))
if mibBuilder.loadTexts:tplinkDhcpRelayMIB.setRevisions(('2012-12-17 11:21',))
_TplinkDhcpRelayMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDhcpRelayMIBObjects=_TplinkDhcpRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,39,1))
_DhcpRelayGlobalConfig_ObjectIdentity=ObjectIdentity
dhcpRelayGlobalConfig=_DhcpRelayGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,39,1,1))
class _DhcpRelayEnableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DhcpRelayEnableState_Type.__name__=_E
_DhcpRelayEnableState_Object=MibScalar
dhcpRelayEnableState=_DhcpRelayEnableState_Object((1,3,6,1,4,1,11863,6,39,1,1,1),_DhcpRelayEnableState_Type())
dhcpRelayEnableState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayEnableState.setStatus(_A)
_DhcpRelayHops_Type=Integer32
_DhcpRelayHops_Object=MibScalar
dhcpRelayHops=_DhcpRelayHops_Object((1,3,6,1,4,1,11863,6,39,1,1,2),_DhcpRelayHops_Type())
dhcpRelayHops.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayHops.setStatus(_A)
_DhcpRelayTimeThreshold_Type=Integer32
_DhcpRelayTimeThreshold_Object=MibScalar
dhcpRelayTimeThreshold=_DhcpRelayTimeThreshold_Object((1,3,6,1,4,1,11863,6,39,1,1,3),_DhcpRelayTimeThreshold_Type())
dhcpRelayTimeThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayTimeThreshold.setStatus(_A)
_DhcpRelayServerConfig_ObjectIdentity=ObjectIdentity
dhcpRelayServerConfig=_DhcpRelayServerConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,39,1,2))
_DhcpRelayServerVlanInterfaceTable_Object=MibTable
dhcpRelayServerVlanInterfaceTable=_DhcpRelayServerVlanInterfaceTable_Object((1,3,6,1,4,1,11863,6,39,1,2,1))
if mibBuilder.loadTexts:dhcpRelayServerVlanInterfaceTable.setStatus(_A)
_DhcpRelayServerVlanInterfaceEntry_Object=MibTableRow
dhcpRelayServerVlanInterfaceEntry=_DhcpRelayServerVlanInterfaceEntry_Object((1,3,6,1,4,1,11863,6,39,1,2,1,1))
dhcpRelayServerVlanInterfaceEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:dhcpRelayServerVlanInterfaceEntry.setStatus(_A)
_DhcpRelayServerVlanId_Type=Integer32
_DhcpRelayServerVlanId_Object=MibTableColumn
dhcpRelayServerVlanId=_DhcpRelayServerVlanId_Object((1,3,6,1,4,1,11863,6,39,1,2,1,1,1),_DhcpRelayServerVlanId_Type())
dhcpRelayServerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerVlanId.setStatus(_A)
_DhcpRelayServerVlanInterfaceIp_Type=IpAddress
_DhcpRelayServerVlanInterfaceIp_Object=MibTableColumn
dhcpRelayServerVlanInterfaceIp=_DhcpRelayServerVlanInterfaceIp_Object((1,3,6,1,4,1,11863,6,39,1,2,1,1,2),_DhcpRelayServerVlanInterfaceIp_Type())
dhcpRelayServerVlanInterfaceIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerVlanInterfaceIp.setStatus(_A)
_DhcpRelayServerVlanInterfaceStatus_Type=TPRowStatus
_DhcpRelayServerVlanInterfaceStatus_Object=MibTableColumn
dhcpRelayServerVlanInterfaceStatus=_DhcpRelayServerVlanInterfaceStatus_Object((1,3,6,1,4,1,11863,6,39,1,2,1,1,3),_DhcpRelayServerVlanInterfaceStatus_Type())
dhcpRelayServerVlanInterfaceStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpRelayServerVlanInterfaceStatus.setStatus(_A)
_DhcpRelayServerRoutedPortInterfaceTable_Object=MibTable
dhcpRelayServerRoutedPortInterfaceTable=_DhcpRelayServerRoutedPortInterfaceTable_Object((1,3,6,1,4,1,11863,6,39,1,2,3))
if mibBuilder.loadTexts:dhcpRelayServerRoutedPortInterfaceTable.setStatus(_A)
_DhcpRelayServerRoutedPortInterfaceEntry_Object=MibTableRow
dhcpRelayServerRoutedPortInterfaceEntry=_DhcpRelayServerRoutedPortInterfaceEntry_Object((1,3,6,1,4,1,11863,6,39,1,2,3,1))
dhcpRelayServerRoutedPortInterfaceEntry.setIndexNames((0,_G,_H),(0,_F,_N))
if mibBuilder.loadTexts:dhcpRelayServerRoutedPortInterfaceEntry.setStatus(_A)
class _DhcpRelayServerRoutedPortPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DhcpRelayServerRoutedPortPortId_Type.__name__=_D
_DhcpRelayServerRoutedPortPortId_Object=MibTableColumn
dhcpRelayServerRoutedPortPortId=_DhcpRelayServerRoutedPortPortId_Object((1,3,6,1,4,1,11863,6,39,1,2,3,1,1),_DhcpRelayServerRoutedPortPortId_Type())
dhcpRelayServerRoutedPortPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerRoutedPortPortId.setStatus(_A)
_DhcpRelayServerRoutedPortInterfaceIp_Type=IpAddress
_DhcpRelayServerRoutedPortInterfaceIp_Object=MibTableColumn
dhcpRelayServerRoutedPortInterfaceIp=_DhcpRelayServerRoutedPortInterfaceIp_Object((1,3,6,1,4,1,11863,6,39,1,2,3,1,2),_DhcpRelayServerRoutedPortInterfaceIp_Type())
dhcpRelayServerRoutedPortInterfaceIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerRoutedPortInterfaceIp.setStatus(_A)
_DhcpRelayServerRoutedPortInterfaceStatus_Type=TPRowStatus
_DhcpRelayServerRoutedPortInterfaceStatus_Object=MibTableColumn
dhcpRelayServerRoutedPortInterfaceStatus=_DhcpRelayServerRoutedPortInterfaceStatus_Object((1,3,6,1,4,1,11863,6,39,1,2,3,1,3),_DhcpRelayServerRoutedPortInterfaceStatus_Type())
dhcpRelayServerRoutedPortInterfaceStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpRelayServerRoutedPortInterfaceStatus.setStatus(_A)
_DhcpRelayServerPortChannelInterfaceTable_Object=MibTable
dhcpRelayServerPortChannelInterfaceTable=_DhcpRelayServerPortChannelInterfaceTable_Object((1,3,6,1,4,1,11863,6,39,1,2,4))
if mibBuilder.loadTexts:dhcpRelayServerPortChannelInterfaceTable.setStatus(_A)
_DhcpRelayServerPortChannelInterfaceEntry_Object=MibTableRow
dhcpRelayServerPortChannelInterfaceEntry=_DhcpRelayServerPortChannelInterfaceEntry_Object((1,3,6,1,4,1,11863,6,39,1,2,4,1))
dhcpRelayServerPortChannelInterfaceEntry.setIndexNames((0,_G,_H),(0,_F,_O))
if mibBuilder.loadTexts:dhcpRelayServerPortChannelInterfaceEntry.setStatus(_A)
_DhcpRelayServerPortChannelPortId_Type=Integer32
_DhcpRelayServerPortChannelPortId_Object=MibTableColumn
dhcpRelayServerPortChannelPortId=_DhcpRelayServerPortChannelPortId_Object((1,3,6,1,4,1,11863,6,39,1,2,4,1,1),_DhcpRelayServerPortChannelPortId_Type())
dhcpRelayServerPortChannelPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerPortChannelPortId.setStatus(_A)
_DhcpRelayServerPortChannelInterfaceIp_Type=IpAddress
_DhcpRelayServerPortChannelInterfaceIp_Object=MibTableColumn
dhcpRelayServerPortChannelInterfaceIp=_DhcpRelayServerPortChannelInterfaceIp_Object((1,3,6,1,4,1,11863,6,39,1,2,4,1,2),_DhcpRelayServerPortChannelInterfaceIp_Type())
dhcpRelayServerPortChannelInterfaceIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayServerPortChannelInterfaceIp.setStatus(_A)
_DhcpRelayServerPortChannelInterfaceStatus_Type=TPRowStatus
_DhcpRelayServerPortChannelInterfaceStatus_Object=MibTableColumn
dhcpRelayServerPortChannelInterfaceStatus=_DhcpRelayServerPortChannelInterfaceStatus_Object((1,3,6,1,4,1,11863,6,39,1,2,4,1,3),_DhcpRelayServerPortChannelInterfaceStatus_Type())
dhcpRelayServerPortChannelInterfaceStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpRelayServerPortChannelInterfaceStatus.setStatus(_A)
_DhcpRelayVlanRelayServerConfig_ObjectIdentity=ObjectIdentity
dhcpRelayVlanRelayServerConfig=_DhcpRelayVlanRelayServerConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,39,1,3))
_DhcpRelayVlanRelayDefaultRelayAgentInterface_ObjectIdentity=ObjectIdentity
dhcpRelayVlanRelayDefaultRelayAgentInterface=_DhcpRelayVlanRelayDefaultRelayAgentInterface_ObjectIdentity((1,3,6,1,4,1,11863,6,39,1,3,1))
class _DefaultRelayAgentInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_DefaultRelayAgentInterface_Type.__name__=_D
_DefaultRelayAgentInterface_Object=MibScalar
defaultRelayAgentInterface=_DefaultRelayAgentInterface_Object((1,3,6,1,4,1,11863,6,39,1,3,1,1),_DefaultRelayAgentInterface_Type())
defaultRelayAgentInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRelayAgentInterface.setStatus(_A)
_DefaultRelayAgentIp_Type=IpAddress
_DefaultRelayAgentIp_Object=MibScalar
defaultRelayAgentIp=_DefaultRelayAgentIp_Object((1,3,6,1,4,1,11863,6,39,1,3,1,2),_DefaultRelayAgentIp_Type())
defaultRelayAgentIp.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultRelayAgentIp.setStatus(_A)
_DhcpRelayVlanRelayServerTable_Object=MibTable
dhcpRelayVlanRelayServerTable=_DhcpRelayVlanRelayServerTable_Object((1,3,6,1,4,1,11863,6,39,1,3,2))
if mibBuilder.loadTexts:dhcpRelayVlanRelayServerTable.setStatus(_A)
_DhcpRelayVlanRelayServerEntry_Object=MibTableRow
dhcpRelayVlanRelayServerEntry=_DhcpRelayVlanRelayServerEntry_Object((1,3,6,1,4,1,11863,6,39,1,3,2,1))
dhcpRelayVlanRelayServerEntry.setIndexNames((0,_F,_P),(0,_F,_Q))
if mibBuilder.loadTexts:dhcpRelayVlanRelayServerEntry.setStatus(_A)
_DhcpRelayVlanRelayServerVlanId_Type=Integer32
_DhcpRelayVlanRelayServerVlanId_Object=MibTableColumn
dhcpRelayVlanRelayServerVlanId=_DhcpRelayVlanRelayServerVlanId_Object((1,3,6,1,4,1,11863,6,39,1,3,2,1,1),_DhcpRelayVlanRelayServerVlanId_Type())
dhcpRelayVlanRelayServerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayVlanRelayServerVlanId.setStatus(_A)
_DhcpRelayVlanRelayServerIp_Type=IpAddress
_DhcpRelayVlanRelayServerIp_Object=MibTableColumn
dhcpRelayVlanRelayServerIp=_DhcpRelayVlanRelayServerIp_Object((1,3,6,1,4,1,11863,6,39,1,3,2,1,2),_DhcpRelayVlanRelayServerIp_Type())
dhcpRelayVlanRelayServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayVlanRelayServerIp.setStatus(_A)
_DhcpRelayVlanRelayServerRowStatus_Type=TPRowStatus
_DhcpRelayVlanRelayServerRowStatus_Object=MibTableColumn
dhcpRelayVlanRelayServerRowStatus=_DhcpRelayVlanRelayServerRowStatus_Object((1,3,6,1,4,1,11863,6,39,1,3,2,1,3),_DhcpRelayVlanRelayServerRowStatus_Type())
dhcpRelayVlanRelayServerRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dhcpRelayVlanRelayServerRowStatus.setStatus(_A)
_DhcpRelayOption82Config_ObjectIdentity=ObjectIdentity
dhcpRelayOption82Config=_DhcpRelayOption82Config_ObjectIdentity((1,3,6,1,4,1,11863,6,39,1,4))
_DhcpRelayOption82ConfigTable_Object=MibTable
dhcpRelayOption82ConfigTable=_DhcpRelayOption82ConfigTable_Object((1,3,6,1,4,1,11863,6,39,1,4,1))
if mibBuilder.loadTexts:dhcpRelayOption82ConfigTable.setStatus(_A)
_DhcpRelayOption82ConfigEntry_Object=MibTableRow
dhcpRelayOption82ConfigEntry=_DhcpRelayOption82ConfigEntry_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1))
dhcpRelayOption82ConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dhcpRelayOption82ConfigEntry.setStatus(_A)
class _DhcpRelayOption82ConfigPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhcpRelayOption82ConfigPort_Type.__name__=_D
_DhcpRelayOption82ConfigPort_Object=MibTableColumn
dhcpRelayOption82ConfigPort=_DhcpRelayOption82ConfigPort_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,1),_DhcpRelayOption82ConfigPort_Type())
dhcpRelayOption82ConfigPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigPort.setStatus(_A)
class _DhcpRelayOption82ConfigSupportStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DhcpRelayOption82ConfigSupportStatus_Type.__name__=_E
_DhcpRelayOption82ConfigSupportStatus_Object=MibTableColumn
dhcpRelayOption82ConfigSupportStatus=_DhcpRelayOption82ConfigSupportStatus_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,2),_DhcpRelayOption82ConfigSupportStatus_Type())
dhcpRelayOption82ConfigSupportStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigSupportStatus.setStatus(_A)
class _DhcpRelayOption82ConfigOperationStrategy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('keep',0),('replace',1),('drop',2)))
_DhcpRelayOption82ConfigOperationStrategy_Type.__name__=_E
_DhcpRelayOption82ConfigOperationStrategy_Object=MibTableColumn
dhcpRelayOption82ConfigOperationStrategy=_DhcpRelayOption82ConfigOperationStrategy_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,3),_DhcpRelayOption82ConfigOperationStrategy_Type())
dhcpRelayOption82ConfigOperationStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigOperationStrategy.setStatus(_A)
class _DhcpRelayOption82ConfigFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('private',1)))
_DhcpRelayOption82ConfigFormat_Type.__name__=_E
_DhcpRelayOption82ConfigFormat_Object=MibTableColumn
dhcpRelayOption82ConfigFormat=_DhcpRelayOption82ConfigFormat_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,4),_DhcpRelayOption82ConfigFormat_Type())
dhcpRelayOption82ConfigFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigFormat.setStatus(_A)
class _DhcpRelayOption82ConfigCircuitCustomization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DhcpRelayOption82ConfigCircuitCustomization_Type.__name__=_E
_DhcpRelayOption82ConfigCircuitCustomization_Object=MibTableColumn
dhcpRelayOption82ConfigCircuitCustomization=_DhcpRelayOption82ConfigCircuitCustomization_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,5),_DhcpRelayOption82ConfigCircuitCustomization_Type())
dhcpRelayOption82ConfigCircuitCustomization.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigCircuitCustomization.setStatus(_A)
class _DhcpRelayOption82ConfigCircuitID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpRelayOption82ConfigCircuitID_Type.__name__=_D
_DhcpRelayOption82ConfigCircuitID_Object=MibTableColumn
dhcpRelayOption82ConfigCircuitID=_DhcpRelayOption82ConfigCircuitID_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,6),_DhcpRelayOption82ConfigCircuitID_Type())
dhcpRelayOption82ConfigCircuitID.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigCircuitID.setStatus(_A)
class _DhcpRelayOption82ConfigRemoteCustomization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_DhcpRelayOption82ConfigRemoteCustomization_Type.__name__=_E
_DhcpRelayOption82ConfigRemoteCustomization_Object=MibTableColumn
dhcpRelayOption82ConfigRemoteCustomization=_DhcpRelayOption82ConfigRemoteCustomization_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,7),_DhcpRelayOption82ConfigRemoteCustomization_Type())
dhcpRelayOption82ConfigRemoteCustomization.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigRemoteCustomization.setStatus(_A)
class _DhcpRelayOption82ConfigRemoteID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DhcpRelayOption82ConfigRemoteID_Type.__name__=_D
_DhcpRelayOption82ConfigRemoteID_Object=MibTableColumn
dhcpRelayOption82ConfigRemoteID=_DhcpRelayOption82ConfigRemoteID_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,8),_DhcpRelayOption82ConfigRemoteID_Type())
dhcpRelayOption82ConfigRemoteID.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigRemoteID.setStatus(_A)
class _DhcpRelayOption82ConfigLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DhcpRelayOption82ConfigLag_Type.__name__=_D
_DhcpRelayOption82ConfigLag_Object=MibTableColumn
dhcpRelayOption82ConfigLag=_DhcpRelayOption82ConfigLag_Object((1,3,6,1,4,1,11863,6,39,1,4,1,1,9),_DhcpRelayOption82ConfigLag_Type())
dhcpRelayOption82ConfigLag.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayOption82ConfigLag.setStatus(_A)
_TplinkDhcpRelayNotifications_ObjectIdentity=ObjectIdentity
tplinkDhcpRelayNotifications=_TplinkDhcpRelayNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,39,2))
mibBuilder.exportSymbols(_F,**{'tplinkDhcpRelayMIB':tplinkDhcpRelayMIB,'tplinkDhcpRelayMIBObjects':tplinkDhcpRelayMIBObjects,'dhcpRelayGlobalConfig':dhcpRelayGlobalConfig,'dhcpRelayEnableState':dhcpRelayEnableState,'dhcpRelayHops':dhcpRelayHops,'dhcpRelayTimeThreshold':dhcpRelayTimeThreshold,'dhcpRelayServerConfig':dhcpRelayServerConfig,'dhcpRelayServerVlanInterfaceTable':dhcpRelayServerVlanInterfaceTable,'dhcpRelayServerVlanInterfaceEntry':dhcpRelayServerVlanInterfaceEntry,_L:dhcpRelayServerVlanId,_M:dhcpRelayServerVlanInterfaceIp,'dhcpRelayServerVlanInterfaceStatus':dhcpRelayServerVlanInterfaceStatus,'dhcpRelayServerRoutedPortInterfaceTable':dhcpRelayServerRoutedPortInterfaceTable,'dhcpRelayServerRoutedPortInterfaceEntry':dhcpRelayServerRoutedPortInterfaceEntry,'dhcpRelayServerRoutedPortPortId':dhcpRelayServerRoutedPortPortId,_N:dhcpRelayServerRoutedPortInterfaceIp,'dhcpRelayServerRoutedPortInterfaceStatus':dhcpRelayServerRoutedPortInterfaceStatus,'dhcpRelayServerPortChannelInterfaceTable':dhcpRelayServerPortChannelInterfaceTable,'dhcpRelayServerPortChannelInterfaceEntry':dhcpRelayServerPortChannelInterfaceEntry,'dhcpRelayServerPortChannelPortId':dhcpRelayServerPortChannelPortId,_O:dhcpRelayServerPortChannelInterfaceIp,'dhcpRelayServerPortChannelInterfaceStatus':dhcpRelayServerPortChannelInterfaceStatus,'dhcpRelayVlanRelayServerConfig':dhcpRelayVlanRelayServerConfig,'dhcpRelayVlanRelayDefaultRelayAgentInterface':dhcpRelayVlanRelayDefaultRelayAgentInterface,'defaultRelayAgentInterface':defaultRelayAgentInterface,'defaultRelayAgentIp':defaultRelayAgentIp,'dhcpRelayVlanRelayServerTable':dhcpRelayVlanRelayServerTable,'dhcpRelayVlanRelayServerEntry':dhcpRelayVlanRelayServerEntry,_P:dhcpRelayVlanRelayServerVlanId,_Q:dhcpRelayVlanRelayServerIp,'dhcpRelayVlanRelayServerRowStatus':dhcpRelayVlanRelayServerRowStatus,'dhcpRelayOption82Config':dhcpRelayOption82Config,'dhcpRelayOption82ConfigTable':dhcpRelayOption82ConfigTable,'dhcpRelayOption82ConfigEntry':dhcpRelayOption82ConfigEntry,'dhcpRelayOption82ConfigPort':dhcpRelayOption82ConfigPort,'dhcpRelayOption82ConfigSupportStatus':dhcpRelayOption82ConfigSupportStatus,'dhcpRelayOption82ConfigOperationStrategy':dhcpRelayOption82ConfigOperationStrategy,'dhcpRelayOption82ConfigFormat':dhcpRelayOption82ConfigFormat,'dhcpRelayOption82ConfigCircuitCustomization':dhcpRelayOption82ConfigCircuitCustomization,'dhcpRelayOption82ConfigCircuitID':dhcpRelayOption82ConfigCircuitID,'dhcpRelayOption82ConfigRemoteCustomization':dhcpRelayOption82ConfigRemoteCustomization,'dhcpRelayOption82ConfigRemoteID':dhcpRelayOption82ConfigRemoteID,'dhcpRelayOption82ConfigLag':dhcpRelayOption82ConfigLag,'tplinkDhcpRelayNotifications':tplinkDhcpRelayNotifications})