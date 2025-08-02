_P='ruckusZDClientIsolationWhiteListRuleID'
_O='ruckusZDHotspotID'
_N='ruckusZDClientIsolationWhiteListID'
_M='ruckusZDWLANGroupID'
_L='ruckusZDWLANID'
_K='TruthValue'
_J='not-accessible'
_I='read-create'
_H='enable'
_G='OctetString'
_F='disable'
_E='RUCKUS-ZD-WLAN-CONFIG-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusZDWLANModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusZDWLANModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
ruckusZDWLANConfigMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,2,2,2))
_RuckusZDWLANConfigObjects_ObjectIdentity=ObjectIdentity
ruckusZDWLANConfigObjects=_RuckusZDWLANConfigObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,2,1))
_RuckusZDWLANConfig_ObjectIdentity=ObjectIdentity
ruckusZDWLANConfig=_RuckusZDWLANConfig_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,2,1,1))
_RuckusZDWLANConfigTable_Object=MibTable
ruckusZDWLANConfigTable=_RuckusZDWLANConfigTable_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1))
if mibBuilder.loadTexts:ruckusZDWLANConfigTable.setStatus(_A)
_RuckusZDWLANConfigEntry_Object=MibTableRow
ruckusZDWLANConfigEntry=_RuckusZDWLANConfigEntry_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1))
ruckusZDWLANConfigEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:ruckusZDWLANConfigEntry.setStatus(_A)
class _RuckusZDWLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_RuckusZDWLANID_Type.__name__=_C
_RuckusZDWLANID_Object=MibTableColumn
ruckusZDWLANID=_RuckusZDWLANID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,1),_RuckusZDWLANID_Type())
ruckusZDWLANID.setMaxAccess(_J)
if mibBuilder.loadTexts:ruckusZDWLANID.setStatus(_A)
class _RuckusZDWLANConfigSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RuckusZDWLANConfigSSID_Type.__name__=_G
_RuckusZDWLANConfigSSID_Object=MibTableColumn
ruckusZDWLANConfigSSID=_RuckusZDWLANConfigSSID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,2),_RuckusZDWLANConfigSSID_Type())
ruckusZDWLANConfigSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigSSID.setStatus(_A)
class _RuckusZDWLANConfigDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDWLANConfigDescription_Type.__name__=_D
_RuckusZDWLANConfigDescription_Object=MibTableColumn
ruckusZDWLANConfigDescription=_RuckusZDWLANConfigDescription_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,3),_RuckusZDWLANConfigDescription_Type())
ruckusZDWLANConfigDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigDescription.setStatus(_A)
class _RuckusZDWLANConfigName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RuckusZDWLANConfigName_Type.__name__=_G
_RuckusZDWLANConfigName_Object=MibTableColumn
ruckusZDWLANConfigName=_RuckusZDWLANConfigName_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,4),_RuckusZDWLANConfigName_Type())
ruckusZDWLANConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigName.setStatus(_A)
class _RuckusZDWLANConfigWLANServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standardUsage',1),('guestAccess',2),('hotSpotService',3)))
_RuckusZDWLANConfigWLANServiceType_Type.__name__=_C
_RuckusZDWLANConfigWLANServiceType_Object=MibTableColumn
ruckusZDWLANConfigWLANServiceType=_RuckusZDWLANConfigWLANServiceType_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,8),_RuckusZDWLANConfigWLANServiceType_Type())
ruckusZDWLANConfigWLANServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWLANServiceType.setStatus(_A)
class _RuckusZDWLANConfigAuthentication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('open',1),('shared',2),('eap',3),('mac-address',4),('eap-mac-mix',5)))
_RuckusZDWLANConfigAuthentication_Type.__name__=_C
_RuckusZDWLANConfigAuthentication_Object=MibTableColumn
ruckusZDWLANConfigAuthentication=_RuckusZDWLANConfigAuthentication_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,10),_RuckusZDWLANConfigAuthentication_Type())
ruckusZDWLANConfigAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigAuthentication.setStatus(_A)
class _RuckusZDWLANConfigEncryption_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('wpa',1),('wpa2',2),('wpa-Mixed',3),('wep-64',4),('wep-128',5),('none-enc',6)))
_RuckusZDWLANConfigEncryption_Type.__name__=_C
_RuckusZDWLANConfigEncryption_Object=MibTableColumn
ruckusZDWLANConfigEncryption=_RuckusZDWLANConfigEncryption_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,12),_RuckusZDWLANConfigEncryption_Type())
ruckusZDWLANConfigEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigEncryption.setStatus(_A)
class _RuckusZDWLANConfigWEPKeyIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RuckusZDWLANConfigWEPKeyIndex_Type.__name__=_C
_RuckusZDWLANConfigWEPKeyIndex_Object=MibTableColumn
ruckusZDWLANConfigWEPKeyIndex=_RuckusZDWLANConfigWEPKeyIndex_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,15),_RuckusZDWLANConfigWEPKeyIndex_Type())
ruckusZDWLANConfigWEPKeyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWEPKeyIndex.setStatus(_A)
class _RuckusZDWLANConfigWEPKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10),ValueSizeConstraint(26,26))
_RuckusZDWLANConfigWEPKey_Type.__name__=_G
_RuckusZDWLANConfigWEPKey_Object=MibTableColumn
ruckusZDWLANConfigWEPKey=_RuckusZDWLANConfigWEPKey_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,16),_RuckusZDWLANConfigWEPKey_Type())
ruckusZDWLANConfigWEPKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWEPKey.setStatus(_A)
class _RuckusZDWLANConfigWPACipherType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('tkip',1),('aes',2),('auto',3)))
_RuckusZDWLANConfigWPACipherType_Type.__name__=_C
_RuckusZDWLANConfigWPACipherType_Object=MibTableColumn
ruckusZDWLANConfigWPACipherType=_RuckusZDWLANConfigWPACipherType_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,20),_RuckusZDWLANConfigWPACipherType_Type())
ruckusZDWLANConfigWPACipherType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWPACipherType.setStatus(_A)
class _RuckusZDWLANConfigWPAKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,63),ValueSizeConstraint(64,64))
_RuckusZDWLANConfigWPAKey_Type.__name__=_G
_RuckusZDWLANConfigWPAKey_Object=MibTableColumn
ruckusZDWLANConfigWPAKey=_RuckusZDWLANConfigWPAKey_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,21),_RuckusZDWLANConfigWPAKey_Type())
ruckusZDWLANConfigWPAKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWPAKey.setStatus(_A)
_RuckusZDWLANConfigAuthenticationServerID_Type=Integer32
_RuckusZDWLANConfigAuthenticationServerID_Object=MibTableColumn
ruckusZDWLANConfigAuthenticationServerID=_RuckusZDWLANConfigAuthenticationServerID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,25),_RuckusZDWLANConfigAuthenticationServerID_Type())
ruckusZDWLANConfigAuthenticationServerID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigAuthenticationServerID.setStatus(_A)
class _RuckusZDWLANConfigWirelessClientIsolation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfigWirelessClientIsolation_Type.__name__=_C
_RuckusZDWLANConfigWirelessClientIsolation_Object=MibTableColumn
ruckusZDWLANConfigWirelessClientIsolation=_RuckusZDWLANConfigWirelessClientIsolation_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,28),_RuckusZDWLANConfigWirelessClientIsolation_Type())
ruckusZDWLANConfigWirelessClientIsolation.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWirelessClientIsolation.setStatus(_A)
class _RuckusZDWLANConfigWirelessWhiteListID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RuckusZDWLANConfigWirelessWhiteListID_Type.__name__=_C
_RuckusZDWLANConfigWirelessWhiteListID_Object=MibTableColumn
ruckusZDWLANConfigWirelessWhiteListID=_RuckusZDWLANConfigWirelessWhiteListID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,29),_RuckusZDWLANConfigWirelessWhiteListID_Type())
ruckusZDWLANConfigWirelessWhiteListID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWirelessWhiteListID.setStatus(_A)
class _RuckusZDWLANConfigZeroITActivation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfigZeroITActivation_Type.__name__=_C
_RuckusZDWLANConfigZeroITActivation_Object=MibTableColumn
ruckusZDWLANConfigZeroITActivation=_RuckusZDWLANConfigZeroITActivation_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,30),_RuckusZDWLANConfigZeroITActivation_Type())
ruckusZDWLANConfigZeroITActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigZeroITActivation.setStatus(_A)
class _RuckusZDWLANConfigWLANHotspotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_RuckusZDWLANConfigWLANHotspotID_Type.__name__=_C
_RuckusZDWLANConfigWLANHotspotID_Object=MibTableColumn
ruckusZDWLANConfigWLANHotspotID=_RuckusZDWLANConfigWLANHotspotID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,31),_RuckusZDWLANConfigWLANHotspotID_Type())
ruckusZDWLANConfigWLANHotspotID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWLANHotspotID.setStatus(_A)
class _RuckusZDWLANConfigWLANServicePriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_RuckusZDWLANConfigWLANServicePriority_Type.__name__=_C
_RuckusZDWLANConfigWLANServicePriority_Object=MibTableColumn
ruckusZDWLANConfigWLANServicePriority=_RuckusZDWLANConfigWLANServicePriority_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,32),_RuckusZDWLANConfigWLANServicePriority_Type())
ruckusZDWLANConfigWLANServicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWLANServicePriority.setStatus(_A)
class _RuckusZDWLANConfigAccountingServerID_Type(Integer32):defaultValue=0
_RuckusZDWLANConfigAccountingServerID_Type.__name__=_C
_RuckusZDWLANConfigAccountingServerID_Object=MibTableColumn
ruckusZDWLANConfigAccountingServerID=_RuckusZDWLANConfigAccountingServerID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,35),_RuckusZDWLANConfigAccountingServerID_Type())
ruckusZDWLANConfigAccountingServerID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigAccountingServerID.setStatus(_A)
class _RuckusZDWLANConfigAccountingUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_RuckusZDWLANConfigAccountingUpdateInterval_Type.__name__=_C
_RuckusZDWLANConfigAccountingUpdateInterval_Object=MibTableColumn
ruckusZDWLANConfigAccountingUpdateInterval=_RuckusZDWLANConfigAccountingUpdateInterval_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,36),_RuckusZDWLANConfigAccountingUpdateInterval_Type())
ruckusZDWLANConfigAccountingUpdateInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigAccountingUpdateInterval.setStatus(_A)
class _RuckusZDWLANConfigUplinkRate_Type(OctetString):defaultValue=OctetString(_F);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_RuckusZDWLANConfigUplinkRate_Type.__name__=_G
_RuckusZDWLANConfigUplinkRate_Object=MibTableColumn
ruckusZDWLANConfigUplinkRate=_RuckusZDWLANConfigUplinkRate_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,40),_RuckusZDWLANConfigUplinkRate_Type())
ruckusZDWLANConfigUplinkRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigUplinkRate.setStatus(_A)
class _RuckusZDWLANConfigDownlinkRate_Type(OctetString):defaultValue=OctetString(_F);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_RuckusZDWLANConfigDownlinkRate_Type.__name__=_G
_RuckusZDWLANConfigDownlinkRate_Object=MibTableColumn
ruckusZDWLANConfigDownlinkRate=_RuckusZDWLANConfigDownlinkRate_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,41),_RuckusZDWLANConfigDownlinkRate_Type())
ruckusZDWLANConfigDownlinkRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigDownlinkRate.setStatus(_A)
class _RuckusZDWLANConfigIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfigIGMPSnooping_Type.__name__=_C
_RuckusZDWLANConfigIGMPSnooping_Object=MibTableColumn
ruckusZDWLANConfigIGMPSnooping=_RuckusZDWLANConfigIGMPSnooping_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,42),_RuckusZDWLANConfigIGMPSnooping_Type())
ruckusZDWLANConfigIGMPSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigIGMPSnooping.setStatus(_A)
class _RuckusZDWLANConfigVlanID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusZDWLANConfigVlanID_Type.__name__=_C
_RuckusZDWLANConfigVlanID_Object=MibTableColumn
ruckusZDWLANConfigVlanID=_RuckusZDWLANConfigVlanID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,45),_RuckusZDWLANConfigVlanID_Type())
ruckusZDWLANConfigVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigVlanID.setStatus(_A)
class _RuckusZDWLANConfigDynamicVLAN_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfigDynamicVLAN_Type.__name__=_C
_RuckusZDWLANConfigDynamicVLAN_Object=MibTableColumn
ruckusZDWLANConfigDynamicVLAN=_RuckusZDWLANConfigDynamicVLAN_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,46),_RuckusZDWLANConfigDynamicVLAN_Type())
ruckusZDWLANConfigDynamicVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigDynamicVLAN.setStatus(_A)
class _RuckusZDWLANConfig802dot11d_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfig802dot11d_Type.__name__=_C
_RuckusZDWLANConfig802dot11d_Object=MibTableColumn
ruckusZDWLANConfig802dot11d=_RuckusZDWLANConfig802dot11d_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,47),_RuckusZDWLANConfig802dot11d_Type())
ruckusZDWLANConfig802dot11d.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfig802dot11d.setStatus(_A)
class _RuckusZDWLANConfigOfdmonly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfigOfdmonly_Type.__name__=_C
_RuckusZDWLANConfigOfdmonly_Object=MibTableColumn
ruckusZDWLANConfigOfdmonly=_RuckusZDWLANConfigOfdmonly_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,48),_RuckusZDWLANConfigOfdmonly_Type())
ruckusZDWLANConfigOfdmonly.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigOfdmonly.setStatus(_A)
class _RuckusZDWLANConfigBSSMinrate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_RuckusZDWLANConfigBSSMinrate_Type.__name__=_G
_RuckusZDWLANConfigBSSMinrate_Object=MibTableColumn
ruckusZDWLANConfigBSSMinrate=_RuckusZDWLANConfigBSSMinrate_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,49),_RuckusZDWLANConfigBSSMinrate_Type())
ruckusZDWLANConfigBSSMinrate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigBSSMinrate.setStatus(_A)
class _RuckusZDWLANConfigHideSSID_Type(TruthValue):defaultValue=2
_RuckusZDWLANConfigHideSSID_Type.__name__=_K
_RuckusZDWLANConfigHideSSID_Object=MibTableColumn
ruckusZDWLANConfigHideSSID=_RuckusZDWLANConfigHideSSID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,50),_RuckusZDWLANConfigHideSSID_Type())
ruckusZDWLANConfigHideSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigHideSSID.setStatus(_A)
class _RuckusZDWLANConfigTunnelMode_Type(TruthValue):defaultValue=2
_RuckusZDWLANConfigTunnelMode_Type.__name__=_K
_RuckusZDWLANConfigTunnelMode_Object=MibTableColumn
ruckusZDWLANConfigTunnelMode=_RuckusZDWLANConfigTunnelMode_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,52),_RuckusZDWLANConfigTunnelMode_Type())
ruckusZDWLANConfigTunnelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigTunnelMode.setStatus(_A)
class _RuckusZDWLANConfigBackgroundScanning_Type(TruthValue):defaultValue=2
_RuckusZDWLANConfigBackgroundScanning_Type.__name__=_K
_RuckusZDWLANConfigBackgroundScanning_Object=MibTableColumn
ruckusZDWLANConfigBackgroundScanning=_RuckusZDWLANConfigBackgroundScanning_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,53),_RuckusZDWLANConfigBackgroundScanning_Type())
ruckusZDWLANConfigBackgroundScanning.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigBackgroundScanning.setStatus(_A)
class _RuckusZDWLANConfigMaxClients_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RuckusZDWLANConfigMaxClients_Type.__name__=_C
_RuckusZDWLANConfigMaxClients_Object=MibTableColumn
ruckusZDWLANConfigMaxClients=_RuckusZDWLANConfigMaxClients_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,55),_RuckusZDWLANConfigMaxClients_Type())
ruckusZDWLANConfigMaxClients.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigMaxClients.setStatus(_A)
class _RuckusZDWLANConfigWebAuthentication_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_RuckusZDWLANConfigWebAuthentication_Type.__name__=_C
_RuckusZDWLANConfigWebAuthentication_Object=MibTableColumn
ruckusZDWLANConfigWebAuthentication=_RuckusZDWLANConfigWebAuthentication_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,60),_RuckusZDWLANConfigWebAuthentication_Type())
ruckusZDWLANConfigWebAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANConfigWebAuthentication.setStatus(_A)
_RuckusZDWLANConfigRowStatus_Type=RowStatus
_RuckusZDWLANConfigRowStatus_Object=MibTableColumn
ruckusZDWLANConfigRowStatus=_RuckusZDWLANConfigRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,1,1,63),_RuckusZDWLANConfigRowStatus_Type())
ruckusZDWLANConfigRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDWLANConfigRowStatus.setStatus(_A)
_RuckusZDWLANGroupConfigTable_Object=MibTable
ruckusZDWLANGroupConfigTable=_RuckusZDWLANGroupConfigTable_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2))
if mibBuilder.loadTexts:ruckusZDWLANGroupConfigTable.setStatus(_A)
_RuckusZDWLANGroupConfigEntry_Object=MibTableRow
ruckusZDWLANGroupConfigEntry=_RuckusZDWLANGroupConfigEntry_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2,1))
ruckusZDWLANGroupConfigEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:ruckusZDWLANGroupConfigEntry.setStatus(_A)
class _RuckusZDWLANGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_RuckusZDWLANGroupID_Type.__name__=_C
_RuckusZDWLANGroupID_Object=MibTableColumn
ruckusZDWLANGroupID=_RuckusZDWLANGroupID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2,1,1),_RuckusZDWLANGroupID_Type())
ruckusZDWLANGroupID.setMaxAccess(_J)
if mibBuilder.loadTexts:ruckusZDWLANGroupID.setStatus(_A)
class _RuckusZDWLANGroupConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDWLANGroupConfigName_Type.__name__=_D
_RuckusZDWLANGroupConfigName_Object=MibTableColumn
ruckusZDWLANGroupConfigName=_RuckusZDWLANGroupConfigName_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2,1,5),_RuckusZDWLANGroupConfigName_Type())
ruckusZDWLANGroupConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANGroupConfigName.setStatus(_A)
class _RuckusZDWLANGroupConfigDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDWLANGroupConfigDescription_Type.__name__=_D
_RuckusZDWLANGroupConfigDescription_Object=MibTableColumn
ruckusZDWLANGroupConfigDescription=_RuckusZDWLANGroupConfigDescription_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2,1,6),_RuckusZDWLANGroupConfigDescription_Type())
ruckusZDWLANGroupConfigDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANGroupConfigDescription.setStatus(_A)
_RuckusZDWLANGroupVlanOverrideStatus_Type=TruthValue
_RuckusZDWLANGroupVlanOverrideStatus_Object=MibTableColumn
ruckusZDWLANGroupVlanOverrideStatus=_RuckusZDWLANGroupVlanOverrideStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2,1,8),_RuckusZDWLANGroupVlanOverrideStatus_Type())
ruckusZDWLANGroupVlanOverrideStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:ruckusZDWLANGroupVlanOverrideStatus.setStatus(_A)
_RuckusZDWLANGroupConfigRowStatus_Type=RowStatus
_RuckusZDWLANGroupConfigRowStatus_Object=MibTableColumn
ruckusZDWLANGroupConfigRowStatus=_RuckusZDWLANGroupConfigRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,2,1,15),_RuckusZDWLANGroupConfigRowStatus_Type())
ruckusZDWLANGroupConfigRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDWLANGroupConfigRowStatus.setStatus(_A)
_RuckusZDWLANGroupCfgAttrTable_Object=MibTable
ruckusZDWLANGroupCfgAttrTable=_RuckusZDWLANGroupCfgAttrTable_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,3))
if mibBuilder.loadTexts:ruckusZDWLANGroupCfgAttrTable.setStatus(_A)
_RuckusZDWLANGroupCfgAttrEntry_Object=MibTableRow
ruckusZDWLANGroupCfgAttrEntry=_RuckusZDWLANGroupCfgAttrEntry_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,3,1))
ruckusZDWLANGroupCfgAttrEntry.setIndexNames((0,_E,_M),(0,_E,_L))
if mibBuilder.loadTexts:ruckusZDWLANGroupCfgAttrEntry.setStatus(_A)
class _RuckusZDWLANGroupCfgAttrOverrideType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nochange',1),('tag',2)))
_RuckusZDWLANGroupCfgAttrOverrideType_Type.__name__=_C
_RuckusZDWLANGroupCfgAttrOverrideType_Object=MibTableColumn
ruckusZDWLANGroupCfgAttrOverrideType=_RuckusZDWLANGroupCfgAttrOverrideType_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,3,1,3),_RuckusZDWLANGroupCfgAttrOverrideType_Type())
ruckusZDWLANGroupCfgAttrOverrideType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANGroupCfgAttrOverrideType.setStatus(_A)
class _RuckusZDWLANGroupCfgAttrWGVlanTag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusZDWLANGroupCfgAttrWGVlanTag_Type.__name__=_C
_RuckusZDWLANGroupCfgAttrWGVlanTag_Object=MibTableColumn
ruckusZDWLANGroupCfgAttrWGVlanTag=_RuckusZDWLANGroupCfgAttrWGVlanTag_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,3,1,4),_RuckusZDWLANGroupCfgAttrWGVlanTag_Type())
ruckusZDWLANGroupCfgAttrWGVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDWLANGroupCfgAttrWGVlanTag.setStatus(_A)
_RuckusZDWLANGroupCfgAttrRowStatus_Type=RowStatus
_RuckusZDWLANGroupCfgAttrRowStatus_Object=MibTableColumn
ruckusZDWLANGroupCfgAttrRowStatus=_RuckusZDWLANGroupCfgAttrRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,3,1,10),_RuckusZDWLANGroupCfgAttrRowStatus_Type())
ruckusZDWLANGroupCfgAttrRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDWLANGroupCfgAttrRowStatus.setStatus(_A)
_RuckusZDHotspotConfigTable_Object=MibTable
ruckusZDHotspotConfigTable=_RuckusZDHotspotConfigTable_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8))
if mibBuilder.loadTexts:ruckusZDHotspotConfigTable.setStatus(_A)
_RuckusZDHotspotConfigEntry_Object=MibTableRow
ruckusZDHotspotConfigEntry=_RuckusZDHotspotConfigEntry_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1))
ruckusZDHotspotConfigEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:ruckusZDHotspotConfigEntry.setStatus(_A)
class _RuckusZDHotspotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_RuckusZDHotspotID_Type.__name__=_C
_RuckusZDHotspotID_Object=MibTableColumn
ruckusZDHotspotID=_RuckusZDHotspotID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1,1),_RuckusZDHotspotID_Type())
ruckusZDHotspotID.setMaxAccess(_J)
if mibBuilder.loadTexts:ruckusZDHotspotID.setStatus(_A)
class _RuckusZDHotspotName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDHotspotName_Type.__name__=_D
_RuckusZDHotspotName_Object=MibTableColumn
ruckusZDHotspotName=_RuckusZDHotspotName_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1,2),_RuckusZDHotspotName_Type())
ruckusZDHotspotName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDHotspotName.setStatus(_A)
class _RuckusZDHotspotRedirectLoginPage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RuckusZDHotspotRedirectLoginPage_Type.__name__=_D
_RuckusZDHotspotRedirectLoginPage_Object=MibTableColumn
ruckusZDHotspotRedirectLoginPage=_RuckusZDHotspotRedirectLoginPage_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1,3),_RuckusZDHotspotRedirectLoginPage_Type())
ruckusZDHotspotRedirectLoginPage.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDHotspotRedirectLoginPage.setStatus(_A)
class _RuckusZDHotspotRedirectStartURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RuckusZDHotspotRedirectStartURL_Type.__name__=_D
_RuckusZDHotspotRedirectStartURL_Object=MibTableColumn
ruckusZDHotspotRedirectStartURL=_RuckusZDHotspotRedirectStartURL_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1,4),_RuckusZDHotspotRedirectStartURL_Type())
ruckusZDHotspotRedirectStartURL.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDHotspotRedirectStartURL.setStatus(_A)
class _RuckusZDHotspotRedirectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user',1),('url',2)))
_RuckusZDHotspotRedirectType_Type.__name__=_C
_RuckusZDHotspotRedirectType_Object=MibTableColumn
ruckusZDHotspotRedirectType=_RuckusZDHotspotRedirectType_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1,6),_RuckusZDHotspotRedirectType_Type())
ruckusZDHotspotRedirectType.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDHotspotRedirectType.setStatus(_A)
_RuckusZDHotspotRowStatus_Type=RowStatus
_RuckusZDHotspotRowStatus_Object=MibTableColumn
ruckusZDHotspotRowStatus=_RuckusZDHotspotRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,8,1,15),_RuckusZDHotspotRowStatus_Type())
ruckusZDHotspotRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDHotspotRowStatus.setStatus(_A)
_RuckusZDClientIsolationWhiteListTable_Object=MibTable
ruckusZDClientIsolationWhiteListTable=_RuckusZDClientIsolationWhiteListTable_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,15))
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListTable.setStatus(_A)
_RuckusZDClientIsolationWhiteListEntry_Object=MibTableRow
ruckusZDClientIsolationWhiteListEntry=_RuckusZDClientIsolationWhiteListEntry_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,15,1))
ruckusZDClientIsolationWhiteListEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListEntry.setStatus(_A)
class _RuckusZDClientIsolationWhiteListID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RuckusZDClientIsolationWhiteListID_Type.__name__=_C
_RuckusZDClientIsolationWhiteListID_Object=MibTableColumn
ruckusZDClientIsolationWhiteListID=_RuckusZDClientIsolationWhiteListID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,15,1,1),_RuckusZDClientIsolationWhiteListID_Type())
ruckusZDClientIsolationWhiteListID.setMaxAccess(_J)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListID.setStatus(_A)
class _RuckusZDClientIsolationWhiteListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDClientIsolationWhiteListName_Type.__name__=_D
_RuckusZDClientIsolationWhiteListName_Object=MibTableColumn
ruckusZDClientIsolationWhiteListName=_RuckusZDClientIsolationWhiteListName_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,15,1,5),_RuckusZDClientIsolationWhiteListName_Type())
ruckusZDClientIsolationWhiteListName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListName.setStatus(_A)
class _RuckusZDClientIsolationWhiteListDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDClientIsolationWhiteListDescription_Type.__name__=_D
_RuckusZDClientIsolationWhiteListDescription_Object=MibTableColumn
ruckusZDClientIsolationWhiteListDescription=_RuckusZDClientIsolationWhiteListDescription_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,15,1,6),_RuckusZDClientIsolationWhiteListDescription_Type())
ruckusZDClientIsolationWhiteListDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListDescription.setStatus(_A)
_RuckusZDClientIsolationWhiteListRowStatus_Type=RowStatus
_RuckusZDClientIsolationWhiteListRowStatus_Object=MibTableColumn
ruckusZDClientIsolationWhiteListRowStatus=_RuckusZDClientIsolationWhiteListRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,15,1,15),_RuckusZDClientIsolationWhiteListRowStatus_Type())
ruckusZDClientIsolationWhiteListRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRowStatus.setStatus(_A)
_RuckusZDClientIsolationWhiteListRuleTable_Object=MibTable
ruckusZDClientIsolationWhiteListRuleTable=_RuckusZDClientIsolationWhiteListRuleTable_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16))
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleTable.setStatus(_A)
_RuckusZDClientIsolationWhiteListRuleEntry_Object=MibTableRow
ruckusZDClientIsolationWhiteListRuleEntry=_RuckusZDClientIsolationWhiteListRuleEntry_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16,1))
ruckusZDClientIsolationWhiteListRuleEntry.setIndexNames((0,_E,_N),(0,_E,_P))
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleEntry.setStatus(_A)
class _RuckusZDClientIsolationWhiteListRuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RuckusZDClientIsolationWhiteListRuleID_Type.__name__=_C
_RuckusZDClientIsolationWhiteListRuleID_Object=MibTableColumn
ruckusZDClientIsolationWhiteListRuleID=_RuckusZDClientIsolationWhiteListRuleID_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16,1,1),_RuckusZDClientIsolationWhiteListRuleID_Type())
ruckusZDClientIsolationWhiteListRuleID.setMaxAccess(_J)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleID.setStatus(_A)
class _RuckusZDClientIsolationWhiteListRuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDClientIsolationWhiteListRuleDescription_Type.__name__=_D
_RuckusZDClientIsolationWhiteListRuleDescription_Object=MibTableColumn
ruckusZDClientIsolationWhiteListRuleDescription=_RuckusZDClientIsolationWhiteListRuleDescription_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16,1,3),_RuckusZDClientIsolationWhiteListRuleDescription_Type())
ruckusZDClientIsolationWhiteListRuleDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleDescription.setStatus(_A)
class _RuckusZDClientIsolationWhiteListRuleMac_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_RuckusZDClientIsolationWhiteListRuleMac_Type.__name__=_D
_RuckusZDClientIsolationWhiteListRuleMac_Object=MibTableColumn
ruckusZDClientIsolationWhiteListRuleMac=_RuckusZDClientIsolationWhiteListRuleMac_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16,1,5),_RuckusZDClientIsolationWhiteListRuleMac_Type())
ruckusZDClientIsolationWhiteListRuleMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleMac.setStatus(_A)
class _RuckusZDClientIsolationWhiteListRuleDesAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,46))
_RuckusZDClientIsolationWhiteListRuleDesAddr_Type.__name__=_D
_RuckusZDClientIsolationWhiteListRuleDesAddr_Object=MibTableColumn
ruckusZDClientIsolationWhiteListRuleDesAddr=_RuckusZDClientIsolationWhiteListRuleDesAddr_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16,1,6),_RuckusZDClientIsolationWhiteListRuleDesAddr_Type())
ruckusZDClientIsolationWhiteListRuleDesAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleDesAddr.setStatus(_A)
_RuckusZDClientIsolationWhiteListRuleRowStatus_Type=RowStatus
_RuckusZDClientIsolationWhiteListRuleRowStatus_Object=MibTableColumn
ruckusZDClientIsolationWhiteListRuleRowStatus=_RuckusZDClientIsolationWhiteListRuleRowStatus_Object((1,3,6,1,4,1,25053,1,2,2,2,1,1,16,1,10),_RuckusZDClientIsolationWhiteListRuleRowStatus_Type())
ruckusZDClientIsolationWhiteListRuleRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDClientIsolationWhiteListRuleRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ruckusZDWLANConfigMIB':ruckusZDWLANConfigMIB,'ruckusZDWLANConfigObjects':ruckusZDWLANConfigObjects,'ruckusZDWLANConfig':ruckusZDWLANConfig,'ruckusZDWLANConfigTable':ruckusZDWLANConfigTable,'ruckusZDWLANConfigEntry':ruckusZDWLANConfigEntry,_L:ruckusZDWLANID,'ruckusZDWLANConfigSSID':ruckusZDWLANConfigSSID,'ruckusZDWLANConfigDescription':ruckusZDWLANConfigDescription,'ruckusZDWLANConfigName':ruckusZDWLANConfigName,'ruckusZDWLANConfigWLANServiceType':ruckusZDWLANConfigWLANServiceType,'ruckusZDWLANConfigAuthentication':ruckusZDWLANConfigAuthentication,'ruckusZDWLANConfigEncryption':ruckusZDWLANConfigEncryption,'ruckusZDWLANConfigWEPKeyIndex':ruckusZDWLANConfigWEPKeyIndex,'ruckusZDWLANConfigWEPKey':ruckusZDWLANConfigWEPKey,'ruckusZDWLANConfigWPACipherType':ruckusZDWLANConfigWPACipherType,'ruckusZDWLANConfigWPAKey':ruckusZDWLANConfigWPAKey,'ruckusZDWLANConfigAuthenticationServerID':ruckusZDWLANConfigAuthenticationServerID,'ruckusZDWLANConfigWirelessClientIsolation':ruckusZDWLANConfigWirelessClientIsolation,'ruckusZDWLANConfigWirelessWhiteListID':ruckusZDWLANConfigWirelessWhiteListID,'ruckusZDWLANConfigZeroITActivation':ruckusZDWLANConfigZeroITActivation,'ruckusZDWLANConfigWLANHotspotID':ruckusZDWLANConfigWLANHotspotID,'ruckusZDWLANConfigWLANServicePriority':ruckusZDWLANConfigWLANServicePriority,'ruckusZDWLANConfigAccountingServerID':ruckusZDWLANConfigAccountingServerID,'ruckusZDWLANConfigAccountingUpdateInterval':ruckusZDWLANConfigAccountingUpdateInterval,'ruckusZDWLANConfigUplinkRate':ruckusZDWLANConfigUplinkRate,'ruckusZDWLANConfigDownlinkRate':ruckusZDWLANConfigDownlinkRate,'ruckusZDWLANConfigIGMPSnooping':ruckusZDWLANConfigIGMPSnooping,'ruckusZDWLANConfigVlanID':ruckusZDWLANConfigVlanID,'ruckusZDWLANConfigDynamicVLAN':ruckusZDWLANConfigDynamicVLAN,'ruckusZDWLANConfig802dot11d':ruckusZDWLANConfig802dot11d,'ruckusZDWLANConfigOfdmonly':ruckusZDWLANConfigOfdmonly,'ruckusZDWLANConfigBSSMinrate':ruckusZDWLANConfigBSSMinrate,'ruckusZDWLANConfigHideSSID':ruckusZDWLANConfigHideSSID,'ruckusZDWLANConfigTunnelMode':ruckusZDWLANConfigTunnelMode,'ruckusZDWLANConfigBackgroundScanning':ruckusZDWLANConfigBackgroundScanning,'ruckusZDWLANConfigMaxClients':ruckusZDWLANConfigMaxClients,'ruckusZDWLANConfigWebAuthentication':ruckusZDWLANConfigWebAuthentication,'ruckusZDWLANConfigRowStatus':ruckusZDWLANConfigRowStatus,'ruckusZDWLANGroupConfigTable':ruckusZDWLANGroupConfigTable,'ruckusZDWLANGroupConfigEntry':ruckusZDWLANGroupConfigEntry,_M:ruckusZDWLANGroupID,'ruckusZDWLANGroupConfigName':ruckusZDWLANGroupConfigName,'ruckusZDWLANGroupConfigDescription':ruckusZDWLANGroupConfigDescription,'ruckusZDWLANGroupVlanOverrideStatus':ruckusZDWLANGroupVlanOverrideStatus,'ruckusZDWLANGroupConfigRowStatus':ruckusZDWLANGroupConfigRowStatus,'ruckusZDWLANGroupCfgAttrTable':ruckusZDWLANGroupCfgAttrTable,'ruckusZDWLANGroupCfgAttrEntry':ruckusZDWLANGroupCfgAttrEntry,'ruckusZDWLANGroupCfgAttrOverrideType':ruckusZDWLANGroupCfgAttrOverrideType,'ruckusZDWLANGroupCfgAttrWGVlanTag':ruckusZDWLANGroupCfgAttrWGVlanTag,'ruckusZDWLANGroupCfgAttrRowStatus':ruckusZDWLANGroupCfgAttrRowStatus,'ruckusZDHotspotConfigTable':ruckusZDHotspotConfigTable,'ruckusZDHotspotConfigEntry':ruckusZDHotspotConfigEntry,_O:ruckusZDHotspotID,'ruckusZDHotspotName':ruckusZDHotspotName,'ruckusZDHotspotRedirectLoginPage':ruckusZDHotspotRedirectLoginPage,'ruckusZDHotspotRedirectStartURL':ruckusZDHotspotRedirectStartURL,'ruckusZDHotspotRedirectType':ruckusZDHotspotRedirectType,'ruckusZDHotspotRowStatus':ruckusZDHotspotRowStatus,'ruckusZDClientIsolationWhiteListTable':ruckusZDClientIsolationWhiteListTable,'ruckusZDClientIsolationWhiteListEntry':ruckusZDClientIsolationWhiteListEntry,_N:ruckusZDClientIsolationWhiteListID,'ruckusZDClientIsolationWhiteListName':ruckusZDClientIsolationWhiteListName,'ruckusZDClientIsolationWhiteListDescription':ruckusZDClientIsolationWhiteListDescription,'ruckusZDClientIsolationWhiteListRowStatus':ruckusZDClientIsolationWhiteListRowStatus,'ruckusZDClientIsolationWhiteListRuleTable':ruckusZDClientIsolationWhiteListRuleTable,'ruckusZDClientIsolationWhiteListRuleEntry':ruckusZDClientIsolationWhiteListRuleEntry,_P:ruckusZDClientIsolationWhiteListRuleID,'ruckusZDClientIsolationWhiteListRuleDescription':ruckusZDClientIsolationWhiteListRuleDescription,'ruckusZDClientIsolationWhiteListRuleMac':ruckusZDClientIsolationWhiteListRuleMac,'ruckusZDClientIsolationWhiteListRuleDesAddr':ruckusZDClientIsolationWhiteListRuleDesAddr,'ruckusZDClientIsolationWhiteListRuleRowStatus':ruckusZDClientIsolationWhiteListRuleRowStatus})