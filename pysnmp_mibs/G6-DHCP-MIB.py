_a='snoopingTableIndex'
_Z='snoopingStatisticsPortIndex'
_Y='arpInspectionPortConfigPortIndex'
_X='pppoePortConfigPortIndex'
_W='pppoeConfigIndex'
_V='trusted'
_U='untrusted'
_T='snoopingPortConfigPortIndex'
_S='relayPortConfigPortIndex'
_R='ipSlotPortVlan'
_Q='slotPortId'
_P='snmpPortId'
_O='userDefined'
_N='sysName'
_M='macAddress'
_L='hostname'
_K='relayConfigIndex'
_J='OctetString'
_I='portAlias'
_H='not-accessible'
_G='G6-DHCP-MIB'
_F='read-only'
_E='enabled'
_D='disabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Dhcp_ObjectIdentity=ObjectIdentity
dhcp=_Dhcp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,49))
class _DhcpEnableDhcpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpEnableDhcpRelay_Type.__name__=_B
_DhcpEnableDhcpRelay_Object=MibScalar
dhcpEnableDhcpRelay=_DhcpEnableDhcpRelay_Object((1,3,6,1,4,1,3181,10,6,2,49,1),_DhcpEnableDhcpRelay_Type())
dhcpEnableDhcpRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpEnableDhcpRelay.setStatus(_A)
class _DhcpEnableDhcpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpEnableDhcpSnooping_Type.__name__=_B
_DhcpEnableDhcpSnooping_Object=MibScalar
dhcpEnableDhcpSnooping=_DhcpEnableDhcpSnooping_Object((1,3,6,1,4,1,3181,10,6,2,49,2),_DhcpEnableDhcpSnooping_Type())
dhcpEnableDhcpSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpEnableDhcpSnooping.setStatus(_A)
class _DhcpEnablePppoeSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpEnablePppoeSnooping_Type.__name__=_B
_DhcpEnablePppoeSnooping_Object=MibScalar
dhcpEnablePppoeSnooping=_DhcpEnablePppoeSnooping_Object((1,3,6,1,4,1,3181,10,6,2,49,3),_DhcpEnablePppoeSnooping_Type())
dhcpEnablePppoeSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpEnablePppoeSnooping.setStatus(_A)
class _DhcpEnableArpInspection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DhcpEnableArpInspection_Type.__name__=_B
_DhcpEnableArpInspection_Object=MibScalar
dhcpEnableArpInspection=_DhcpEnableArpInspection_Object((1,3,6,1,4,1,3181,10,6,2,49,4),_DhcpEnableArpInspection_Type())
dhcpEnableArpInspection.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpEnableArpInspection.setStatus(_A)
_DhcpUnblockPort_Type=DisplayString
_DhcpUnblockPort_Object=MibScalar
dhcpUnblockPort=_DhcpUnblockPort_Object((1,3,6,1,4,1,3181,10,6,2,49,5),_DhcpUnblockPort_Type())
dhcpUnblockPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpUnblockPort.setStatus(_A)
_DhcpClearSnoopingTable_Type=DisplayString
_DhcpClearSnoopingTable_Object=MibScalar
dhcpClearSnoopingTable=_DhcpClearSnoopingTable_Object((1,3,6,1,4,1,3181,10,6,2,49,6),_DhcpClearSnoopingTable_Type())
dhcpClearSnoopingTable.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpClearSnoopingTable.setStatus(_A)
_RelayConfigTable_Object=MibTable
relayConfigTable=_RelayConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,49,7))
if mibBuilder.loadTexts:relayConfigTable.setStatus(_A)
_RelayConfigEntry_Object=MibTableRow
relayConfigEntry=_RelayConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,7,1))
relayConfigEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:relayConfigEntry.setStatus(_A)
class _RelayConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_RelayConfigIndex_Type.__name__=_B
_RelayConfigIndex_Object=MibTableColumn
relayConfigIndex=_RelayConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,7,1,1),_RelayConfigIndex_Type())
relayConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:relayConfigIndex.setStatus(_A)
_RelayConfigDhcpServerAddress_Type=DisplayString
_RelayConfigDhcpServerAddress_Object=MibTableColumn
relayConfigDhcpServerAddress=_RelayConfigDhcpServerAddress_Object((1,3,6,1,4,1,3181,10,6,2,49,7,1,2),_RelayConfigDhcpServerAddress_Type())
relayConfigDhcpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:relayConfigDhcpServerAddress.setStatus(_A)
class _RelayConfigRemoteIdSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_I,4)))
_RelayConfigRemoteIdSource_Type.__name__=_B
_RelayConfigRemoteIdSource_Object=MibTableColumn
relayConfigRemoteIdSource=_RelayConfigRemoteIdSource_Object((1,3,6,1,4,1,3181,10,6,2,49,7,1,3),_RelayConfigRemoteIdSource_Type())
relayConfigRemoteIdSource.setMaxAccess(_C)
if mibBuilder.loadTexts:relayConfigRemoteIdSource.setStatus(_A)
_RelayConfigCustomRemoteId_Type=DisplayString
_RelayConfigCustomRemoteId_Object=MibTableColumn
relayConfigCustomRemoteId=_RelayConfigCustomRemoteId_Object((1,3,6,1,4,1,3181,10,6,2,49,7,1,4),_RelayConfigCustomRemoteId_Type())
relayConfigCustomRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:relayConfigCustomRemoteId.setStatus(_A)
class _RelayConfigCircuitIdSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),(_Q,1),(_I,2),(_R,3)))
_RelayConfigCircuitIdSource_Type.__name__=_B
_RelayConfigCircuitIdSource_Object=MibTableColumn
relayConfigCircuitIdSource=_RelayConfigCircuitIdSource_Object((1,3,6,1,4,1,3181,10,6,2,49,7,1,5),_RelayConfigCircuitIdSource_Type())
relayConfigCircuitIdSource.setMaxAccess(_C)
if mibBuilder.loadTexts:relayConfigCircuitIdSource.setStatus(_A)
_RelayPortConfigTable_Object=MibTable
relayPortConfigTable=_RelayPortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,49,8))
if mibBuilder.loadTexts:relayPortConfigTable.setStatus(_A)
_RelayPortConfigEntry_Object=MibTableRow
relayPortConfigEntry=_RelayPortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,8,1))
relayPortConfigEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:relayPortConfigEntry.setStatus(_A)
class _RelayPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_RelayPortConfigPortIndex_Type.__name__=_B
_RelayPortConfigPortIndex_Object=MibTableColumn
relayPortConfigPortIndex=_RelayPortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,8,1,1),_RelayPortConfigPortIndex_Type())
relayPortConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:relayPortConfigPortIndex.setStatus(_A)
class _RelayPortConfigEnableDhcpRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RelayPortConfigEnableDhcpRelay_Type.__name__=_B
_RelayPortConfigEnableDhcpRelay_Object=MibTableColumn
relayPortConfigEnableDhcpRelay=_RelayPortConfigEnableDhcpRelay_Object((1,3,6,1,4,1,3181,10,6,2,49,8,1,2),_RelayPortConfigEnableDhcpRelay_Type())
relayPortConfigEnableDhcpRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:relayPortConfigEnableDhcpRelay.setStatus(_A)
class _RelayPortConfigEnableOption82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RelayPortConfigEnableOption82_Type.__name__=_B
_RelayPortConfigEnableOption82_Object=MibTableColumn
relayPortConfigEnableOption82=_RelayPortConfigEnableOption82_Object((1,3,6,1,4,1,3181,10,6,2,49,8,1,3),_RelayPortConfigEnableOption82_Type())
relayPortConfigEnableOption82.setMaxAccess(_C)
if mibBuilder.loadTexts:relayPortConfigEnableOption82.setStatus(_A)
_SnoopingPortConfigTable_Object=MibTable
snoopingPortConfigTable=_SnoopingPortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,49,9))
if mibBuilder.loadTexts:snoopingPortConfigTable.setStatus(_A)
_SnoopingPortConfigEntry_Object=MibTableRow
snoopingPortConfigEntry=_SnoopingPortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1))
snoopingPortConfigEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:snoopingPortConfigEntry.setStatus(_A)
class _SnoopingPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_SnoopingPortConfigPortIndex_Type.__name__=_B
_SnoopingPortConfigPortIndex_Object=MibTableColumn
snoopingPortConfigPortIndex=_SnoopingPortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,1),_SnoopingPortConfigPortIndex_Type())
snoopingPortConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snoopingPortConfigPortIndex.setStatus(_A)
class _SnoopingPortConfigEnableDhcpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SnoopingPortConfigEnableDhcpSnooping_Type.__name__=_B
_SnoopingPortConfigEnableDhcpSnooping_Object=MibTableColumn
snoopingPortConfigEnableDhcpSnooping=_SnoopingPortConfigEnableDhcpSnooping_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,2),_SnoopingPortConfigEnableDhcpSnooping_Type())
snoopingPortConfigEnableDhcpSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigEnableDhcpSnooping.setStatus(_A)
class _SnoopingPortConfigDhcpFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),('dropAndEvent',1),('blockAndEvent',2)))
_SnoopingPortConfigDhcpFiltering_Type.__name__=_B
_SnoopingPortConfigDhcpFiltering_Object=MibTableColumn
snoopingPortConfigDhcpFiltering=_SnoopingPortConfigDhcpFiltering_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,3),_SnoopingPortConfigDhcpFiltering_Type())
snoopingPortConfigDhcpFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigDhcpFiltering.setStatus(_A)
class _SnoopingPortConfigSnoopingTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),(_U,1),(_V,2)))
_SnoopingPortConfigSnoopingTrust_Type.__name__=_B
_SnoopingPortConfigSnoopingTrust_Object=MibTableColumn
snoopingPortConfigSnoopingTrust=_SnoopingPortConfigSnoopingTrust_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,4),_SnoopingPortConfigSnoopingTrust_Type())
snoopingPortConfigSnoopingTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigSnoopingTrust.setStatus(_A)
class _SnoopingPortConfigAcceptIngressOption82_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SnoopingPortConfigAcceptIngressOption82_Type.__name__=_B
_SnoopingPortConfigAcceptIngressOption82_Object=MibTableColumn
snoopingPortConfigAcceptIngressOption82=_SnoopingPortConfigAcceptIngressOption82_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,5),_SnoopingPortConfigAcceptIngressOption82_Type())
snoopingPortConfigAcceptIngressOption82.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigAcceptIngressOption82.setStatus(_A)
class _SnoopingPortConfigMacAddressVerification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SnoopingPortConfigMacAddressVerification_Type.__name__=_B
_SnoopingPortConfigMacAddressVerification_Object=MibTableColumn
snoopingPortConfigMacAddressVerification=_SnoopingPortConfigMacAddressVerification_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,6),_SnoopingPortConfigMacAddressVerification_Type())
snoopingPortConfigMacAddressVerification.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigMacAddressVerification.setStatus(_A)
class _SnoopingPortConfigDhcpRateLimiting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnoopingPortConfigDhcpRateLimiting_Type.__name__=_B
_SnoopingPortConfigDhcpRateLimiting_Object=MibTableColumn
snoopingPortConfigDhcpRateLimiting=_SnoopingPortConfigDhcpRateLimiting_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,7),_SnoopingPortConfigDhcpRateLimiting_Type())
snoopingPortConfigDhcpRateLimiting.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigDhcpRateLimiting.setStatus(_A)
_SnoopingPortConfigClearSnoopingStatistics_Type=DisplayString
_SnoopingPortConfigClearSnoopingStatistics_Object=MibTableColumn
snoopingPortConfigClearSnoopingStatistics=_SnoopingPortConfigClearSnoopingStatistics_Object((1,3,6,1,4,1,3181,10,6,2,49,9,1,8),_SnoopingPortConfigClearSnoopingStatistics_Type())
snoopingPortConfigClearSnoopingStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:snoopingPortConfigClearSnoopingStatistics.setStatus(_A)
_PppoeConfigTable_Object=MibTable
pppoeConfigTable=_PppoeConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,49,10))
if mibBuilder.loadTexts:pppoeConfigTable.setStatus(_A)
_PppoeConfigEntry_Object=MibTableRow
pppoeConfigEntry=_PppoeConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,10,1))
pppoeConfigEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:pppoeConfigEntry.setStatus(_A)
class _PppoeConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_PppoeConfigIndex_Type.__name__=_B
_PppoeConfigIndex_Object=MibTableColumn
pppoeConfigIndex=_PppoeConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,10,1,1),_PppoeConfigIndex_Type())
pppoeConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:pppoeConfigIndex.setStatus(_A)
_PppoeConfigVendorId_Type=Unsigned32
_PppoeConfigVendorId_Object=MibTableColumn
pppoeConfigVendorId=_PppoeConfigVendorId_Object((1,3,6,1,4,1,3181,10,6,2,49,10,1,2),_PppoeConfigVendorId_Type())
pppoeConfigVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeConfigVendorId.setStatus(_A)
class _PppoeConfigRemoteIdSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_I,4)))
_PppoeConfigRemoteIdSource_Type.__name__=_B
_PppoeConfigRemoteIdSource_Object=MibTableColumn
pppoeConfigRemoteIdSource=_PppoeConfigRemoteIdSource_Object((1,3,6,1,4,1,3181,10,6,2,49,10,1,3),_PppoeConfigRemoteIdSource_Type())
pppoeConfigRemoteIdSource.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeConfigRemoteIdSource.setStatus(_A)
_PppoeConfigCustomRemoteId_Type=DisplayString
_PppoeConfigCustomRemoteId_Object=MibTableColumn
pppoeConfigCustomRemoteId=_PppoeConfigCustomRemoteId_Object((1,3,6,1,4,1,3181,10,6,2,49,10,1,4),_PppoeConfigCustomRemoteId_Type())
pppoeConfigCustomRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeConfigCustomRemoteId.setStatus(_A)
class _PppoeConfigCircuitIdSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),(_Q,1),(_I,2),(_R,3)))
_PppoeConfigCircuitIdSource_Type.__name__=_B
_PppoeConfigCircuitIdSource_Object=MibTableColumn
pppoeConfigCircuitIdSource=_PppoeConfigCircuitIdSource_Object((1,3,6,1,4,1,3181,10,6,2,49,10,1,5),_PppoeConfigCircuitIdSource_Type())
pppoeConfigCircuitIdSource.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoeConfigCircuitIdSource.setStatus(_A)
_PppoePortConfigTable_Object=MibTable
pppoePortConfigTable=_PppoePortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,49,11))
if mibBuilder.loadTexts:pppoePortConfigTable.setStatus(_A)
_PppoePortConfigEntry_Object=MibTableRow
pppoePortConfigEntry=_PppoePortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,11,1))
pppoePortConfigEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:pppoePortConfigEntry.setStatus(_A)
class _PppoePortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PppoePortConfigPortIndex_Type.__name__=_B
_PppoePortConfigPortIndex_Object=MibTableColumn
pppoePortConfigPortIndex=_PppoePortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,11,1,1),_PppoePortConfigPortIndex_Type())
pppoePortConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:pppoePortConfigPortIndex.setStatus(_A)
class _PppoePortConfigEnablePppoeSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PppoePortConfigEnablePppoeSnooping_Type.__name__=_B
_PppoePortConfigEnablePppoeSnooping_Object=MibTableColumn
pppoePortConfigEnablePppoeSnooping=_PppoePortConfigEnablePppoeSnooping_Object((1,3,6,1,4,1,3181,10,6,2,49,11,1,2),_PppoePortConfigEnablePppoeSnooping_Type())
pppoePortConfigEnablePppoeSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:pppoePortConfigEnablePppoeSnooping.setStatus(_A)
_ArpInspectionPortConfigTable_Object=MibTable
arpInspectionPortConfigTable=_ArpInspectionPortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,49,12))
if mibBuilder.loadTexts:arpInspectionPortConfigTable.setStatus(_A)
_ArpInspectionPortConfigEntry_Object=MibTableRow
arpInspectionPortConfigEntry=_ArpInspectionPortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1))
arpInspectionPortConfigEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:arpInspectionPortConfigEntry.setStatus(_A)
class _ArpInspectionPortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ArpInspectionPortConfigPortIndex_Type.__name__=_B
_ArpInspectionPortConfigPortIndex_Object=MibTableColumn
arpInspectionPortConfigPortIndex=_ArpInspectionPortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,1),_ArpInspectionPortConfigPortIndex_Type())
arpInspectionPortConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:arpInspectionPortConfigPortIndex.setStatus(_A)
class _ArpInspectionPortConfigEnableArpInspection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ArpInspectionPortConfigEnableArpInspection_Type.__name__=_B
_ArpInspectionPortConfigEnableArpInspection_Object=MibTableColumn
arpInspectionPortConfigEnableArpInspection=_ArpInspectionPortConfigEnableArpInspection_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,2),_ArpInspectionPortConfigEnableArpInspection_Type())
arpInspectionPortConfigEnableArpInspection.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigEnableArpInspection.setStatus(_A)
class _ArpInspectionPortConfigArpRateLimiting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArpInspectionPortConfigArpRateLimiting_Type.__name__=_B
_ArpInspectionPortConfigArpRateLimiting_Object=MibTableColumn
arpInspectionPortConfigArpRateLimiting=_ArpInspectionPortConfigArpRateLimiting_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,3),_ArpInspectionPortConfigArpRateLimiting_Type())
arpInspectionPortConfigArpRateLimiting.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigArpRateLimiting.setStatus(_A)
class _ArpInspectionPortConfigInspectionDatabase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('dhcp',1),('arpAcl',2),('both',3)))
_ArpInspectionPortConfigInspectionDatabase_Type.__name__=_B
_ArpInspectionPortConfigInspectionDatabase_Object=MibTableColumn
arpInspectionPortConfigInspectionDatabase=_ArpInspectionPortConfigInspectionDatabase_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,4),_ArpInspectionPortConfigInspectionDatabase_Type())
arpInspectionPortConfigInspectionDatabase.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigInspectionDatabase.setStatus(_A)
_ArpInspectionPortConfigArpAclName_Type=DisplayString
_ArpInspectionPortConfigArpAclName_Object=MibTableColumn
arpInspectionPortConfigArpAclName=_ArpInspectionPortConfigArpAclName_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,5),_ArpInspectionPortConfigArpAclName_Type())
arpInspectionPortConfigArpAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigArpAclName.setStatus(_A)
class _ArpInspectionPortConfigAclDefaultLogic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
_ArpInspectionPortConfigAclDefaultLogic_Type.__name__=_B
_ArpInspectionPortConfigAclDefaultLogic_Object=MibTableColumn
arpInspectionPortConfigAclDefaultLogic=_ArpInspectionPortConfigAclDefaultLogic_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,6),_ArpInspectionPortConfigAclDefaultLogic_Type())
arpInspectionPortConfigAclDefaultLogic.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigAclDefaultLogic.setStatus(_A)
class _ArpInspectionPortConfigSourceMacValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ArpInspectionPortConfigSourceMacValidation_Type.__name__=_B
_ArpInspectionPortConfigSourceMacValidation_Object=MibTableColumn
arpInspectionPortConfigSourceMacValidation=_ArpInspectionPortConfigSourceMacValidation_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,7),_ArpInspectionPortConfigSourceMacValidation_Type())
arpInspectionPortConfigSourceMacValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigSourceMacValidation.setStatus(_A)
class _ArpInspectionPortConfigDestMacValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ArpInspectionPortConfigDestMacValidation_Type.__name__=_B
_ArpInspectionPortConfigDestMacValidation_Object=MibTableColumn
arpInspectionPortConfigDestMacValidation=_ArpInspectionPortConfigDestMacValidation_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,8),_ArpInspectionPortConfigDestMacValidation_Type())
arpInspectionPortConfigDestMacValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigDestMacValidation.setStatus(_A)
class _ArpInspectionPortConfigIpRangeValidation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ArpInspectionPortConfigIpRangeValidation_Type.__name__=_B
_ArpInspectionPortConfigIpRangeValidation_Object=MibTableColumn
arpInspectionPortConfigIpRangeValidation=_ArpInspectionPortConfigIpRangeValidation_Object((1,3,6,1,4,1,3181,10,6,2,49,12,1,9),_ArpInspectionPortConfigIpRangeValidation_Type())
arpInspectionPortConfigIpRangeValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:arpInspectionPortConfigIpRangeValidation.setStatus(_A)
_SnoopingStatisticsTable_Object=MibTable
snoopingStatisticsTable=_SnoopingStatisticsTable_Object((1,3,6,1,4,1,3181,10,6,2,49,100))
if mibBuilder.loadTexts:snoopingStatisticsTable.setStatus(_A)
_SnoopingStatisticsEntry_Object=MibTableRow
snoopingStatisticsEntry=_SnoopingStatisticsEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,100,1))
snoopingStatisticsEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:snoopingStatisticsEntry.setStatus(_A)
class _SnoopingStatisticsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_SnoopingStatisticsPortIndex_Type.__name__=_B
_SnoopingStatisticsPortIndex_Object=MibTableColumn
snoopingStatisticsPortIndex=_SnoopingStatisticsPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,100,1,1),_SnoopingStatisticsPortIndex_Type())
snoopingStatisticsPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snoopingStatisticsPortIndex.setStatus(_A)
class _SnoopingStatisticsTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undecided',0),(_U,1),(_V,2)))
_SnoopingStatisticsTrustMode_Type.__name__=_B
_SnoopingStatisticsTrustMode_Object=MibTableColumn
snoopingStatisticsTrustMode=_SnoopingStatisticsTrustMode_Object((1,3,6,1,4,1,3181,10,6,2,49,100,1,2),_SnoopingStatisticsTrustMode_Type())
snoopingStatisticsTrustMode.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingStatisticsTrustMode.setStatus(_A)
_SnoopingStatisticsNumberOfDhcpProcessed_Type=Unsigned32
_SnoopingStatisticsNumberOfDhcpProcessed_Object=MibTableColumn
snoopingStatisticsNumberOfDhcpProcessed=_SnoopingStatisticsNumberOfDhcpProcessed_Object((1,3,6,1,4,1,3181,10,6,2,49,100,1,3),_SnoopingStatisticsNumberOfDhcpProcessed_Type())
snoopingStatisticsNumberOfDhcpProcessed.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingStatisticsNumberOfDhcpProcessed.setStatus(_A)
_SnoopingStatisticsNumberOfDhcpDropped_Type=Unsigned32
_SnoopingStatisticsNumberOfDhcpDropped_Object=MibTableColumn
snoopingStatisticsNumberOfDhcpDropped=_SnoopingStatisticsNumberOfDhcpDropped_Object((1,3,6,1,4,1,3181,10,6,2,49,100,1,4),_SnoopingStatisticsNumberOfDhcpDropped_Type())
snoopingStatisticsNumberOfDhcpDropped.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingStatisticsNumberOfDhcpDropped.setStatus(_A)
class _SnoopingStatisticsLastDropReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('ok',0),('illegalDhcpServer',1),('dhcpServerSpoofed',2),('illegalRelayAgent',3),('bindingMismatch',4),('flooding',5)))
_SnoopingStatisticsLastDropReason_Type.__name__=_B
_SnoopingStatisticsLastDropReason_Object=MibTableColumn
snoopingStatisticsLastDropReason=_SnoopingStatisticsLastDropReason_Object((1,3,6,1,4,1,3181,10,6,2,49,100,1,5),_SnoopingStatisticsLastDropReason_Type())
snoopingStatisticsLastDropReason.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingStatisticsLastDropReason.setStatus(_A)
_SnoopingTableTable_Object=MibTable
snoopingTableTable=_SnoopingTableTable_Object((1,3,6,1,4,1,3181,10,6,2,49,101))
if mibBuilder.loadTexts:snoopingTableTable.setStatus(_A)
_SnoopingTableEntry_Object=MibTableRow
snoopingTableEntry=_SnoopingTableEntry_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1))
snoopingTableEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:snoopingTableEntry.setStatus(_A)
class _SnoopingTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnoopingTableIndex_Type.__name__=_B
_SnoopingTableIndex_Object=MibTableColumn
snoopingTableIndex=_SnoopingTableIndex_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,1),_SnoopingTableIndex_Type())
snoopingTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:snoopingTableIndex.setStatus(_A)
_SnoopingTableMac_Type=MacAddress
_SnoopingTableMac_Object=MibTableColumn
snoopingTableMac=_SnoopingTableMac_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,2),_SnoopingTableMac_Type())
snoopingTableMac.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTableMac.setStatus(_A)
class _SnoopingTableIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnoopingTableIp_Type.__name__=_J
_SnoopingTableIp_Object=MibTableColumn
snoopingTableIp=_SnoopingTableIp_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,3),_SnoopingTableIp_Type())
snoopingTableIp.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTableIp.setStatus(_A)
class _SnoopingTablePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnoopingTablePort_Type.__name__=_B
_SnoopingTablePort_Object=MibTableColumn
snoopingTablePort=_SnoopingTablePort_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,4),_SnoopingTablePort_Type())
snoopingTablePort.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTablePort.setStatus(_A)
class _SnoopingTableVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnoopingTableVlan_Type.__name__=_B
_SnoopingTableVlan_Object=MibTableColumn
snoopingTableVlan=_SnoopingTableVlan_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,5),_SnoopingTableVlan_Type())
snoopingTableVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTableVlan.setStatus(_A)
_SnoopingTableLastUpdated_Type=DisplayString
_SnoopingTableLastUpdated_Object=MibTableColumn
snoopingTableLastUpdated=_SnoopingTableLastUpdated_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,6),_SnoopingTableLastUpdated_Type())
snoopingTableLastUpdated.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTableLastUpdated.setStatus(_A)
_SnoopingTableLastUpdatedEpoch_Type=Unsigned32
_SnoopingTableLastUpdatedEpoch_Object=MibTableColumn
snoopingTableLastUpdatedEpoch=_SnoopingTableLastUpdatedEpoch_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,7),_SnoopingTableLastUpdatedEpoch_Type())
snoopingTableLastUpdatedEpoch.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTableLastUpdatedEpoch.setStatus(_A)
_SnoopingTableLeaseTime_Type=Counter32
_SnoopingTableLeaseTime_Object=MibTableColumn
snoopingTableLeaseTime=_SnoopingTableLeaseTime_Object((1,3,6,1,4,1,3181,10,6,2,49,101,1,8),_SnoopingTableLeaseTime_Type())
snoopingTableLeaseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:snoopingTableLeaseTime.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'protocol':protocol,'dhcp':dhcp,'dhcpEnableDhcpRelay':dhcpEnableDhcpRelay,'dhcpEnableDhcpSnooping':dhcpEnableDhcpSnooping,'dhcpEnablePppoeSnooping':dhcpEnablePppoeSnooping,'dhcpEnableArpInspection':dhcpEnableArpInspection,'dhcpUnblockPort':dhcpUnblockPort,'dhcpClearSnoopingTable':dhcpClearSnoopingTable,'relayConfigTable':relayConfigTable,'relayConfigEntry':relayConfigEntry,_K:relayConfigIndex,'relayConfigDhcpServerAddress':relayConfigDhcpServerAddress,'relayConfigRemoteIdSource':relayConfigRemoteIdSource,'relayConfigCustomRemoteId':relayConfigCustomRemoteId,'relayConfigCircuitIdSource':relayConfigCircuitIdSource,'relayPortConfigTable':relayPortConfigTable,'relayPortConfigEntry':relayPortConfigEntry,_S:relayPortConfigPortIndex,'relayPortConfigEnableDhcpRelay':relayPortConfigEnableDhcpRelay,'relayPortConfigEnableOption82':relayPortConfigEnableOption82,'snoopingPortConfigTable':snoopingPortConfigTable,'snoopingPortConfigEntry':snoopingPortConfigEntry,_T:snoopingPortConfigPortIndex,'snoopingPortConfigEnableDhcpSnooping':snoopingPortConfigEnableDhcpSnooping,'snoopingPortConfigDhcpFiltering':snoopingPortConfigDhcpFiltering,'snoopingPortConfigSnoopingTrust':snoopingPortConfigSnoopingTrust,'snoopingPortConfigAcceptIngressOption82':snoopingPortConfigAcceptIngressOption82,'snoopingPortConfigMacAddressVerification':snoopingPortConfigMacAddressVerification,'snoopingPortConfigDhcpRateLimiting':snoopingPortConfigDhcpRateLimiting,'snoopingPortConfigClearSnoopingStatistics':snoopingPortConfigClearSnoopingStatistics,'pppoeConfigTable':pppoeConfigTable,'pppoeConfigEntry':pppoeConfigEntry,_W:pppoeConfigIndex,'pppoeConfigVendorId':pppoeConfigVendorId,'pppoeConfigRemoteIdSource':pppoeConfigRemoteIdSource,'pppoeConfigCustomRemoteId':pppoeConfigCustomRemoteId,'pppoeConfigCircuitIdSource':pppoeConfigCircuitIdSource,'pppoePortConfigTable':pppoePortConfigTable,'pppoePortConfigEntry':pppoePortConfigEntry,_X:pppoePortConfigPortIndex,'pppoePortConfigEnablePppoeSnooping':pppoePortConfigEnablePppoeSnooping,'arpInspectionPortConfigTable':arpInspectionPortConfigTable,'arpInspectionPortConfigEntry':arpInspectionPortConfigEntry,_Y:arpInspectionPortConfigPortIndex,'arpInspectionPortConfigEnableArpInspection':arpInspectionPortConfigEnableArpInspection,'arpInspectionPortConfigArpRateLimiting':arpInspectionPortConfigArpRateLimiting,'arpInspectionPortConfigInspectionDatabase':arpInspectionPortConfigInspectionDatabase,'arpInspectionPortConfigArpAclName':arpInspectionPortConfigArpAclName,'arpInspectionPortConfigAclDefaultLogic':arpInspectionPortConfigAclDefaultLogic,'arpInspectionPortConfigSourceMacValidation':arpInspectionPortConfigSourceMacValidation,'arpInspectionPortConfigDestMacValidation':arpInspectionPortConfigDestMacValidation,'arpInspectionPortConfigIpRangeValidation':arpInspectionPortConfigIpRangeValidation,'snoopingStatisticsTable':snoopingStatisticsTable,'snoopingStatisticsEntry':snoopingStatisticsEntry,_Z:snoopingStatisticsPortIndex,'snoopingStatisticsTrustMode':snoopingStatisticsTrustMode,'snoopingStatisticsNumberOfDhcpProcessed':snoopingStatisticsNumberOfDhcpProcessed,'snoopingStatisticsNumberOfDhcpDropped':snoopingStatisticsNumberOfDhcpDropped,'snoopingStatisticsLastDropReason':snoopingStatisticsLastDropReason,'snoopingTableTable':snoopingTableTable,'snoopingTableEntry':snoopingTableEntry,_a:snoopingTableIndex,'snoopingTableMac':snoopingTableMac,'snoopingTableIp':snoopingTableIp,'snoopingTablePort':snoopingTablePort,'snoopingTableVlan':snoopingTableVlan,'snoopingTableLastUpdated':snoopingTableLastUpdated,'snoopingTableLastUpdatedEpoch':snoopingTableLastUpdatedEpoch,'snoopingTableLeaseTime':snoopingTableLeaseTime})