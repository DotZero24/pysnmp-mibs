_O='calibration'
_N='footfall'
_M='ruckusZDAPLBSAPGroupID'
_L='enable'
_K='admin-by-ap'
_J='admin-by-zd'
_I='not-accessible'
_H='ruckusZDAPConfigID'
_G='RUCKUS-ZD-AP-MIB'
_F='disable'
_E='read-only'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ruckusZDWLANModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusZDWLANModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ruckusZDAPMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,2,2,4))
_RuckusZDAPObjects_ObjectIdentity=ObjectIdentity
ruckusZDAPObjects=_RuckusZDAPObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,4,1))
_RuckusZDAPConfig_ObjectIdentity=ObjectIdentity
ruckusZDAPConfig=_RuckusZDAPConfig_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,4,1,1))
_RuckusZDAPConfigTable_Object=MibTable
ruckusZDAPConfigTable=_RuckusZDAPConfigTable_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1))
if mibBuilder.loadTexts:ruckusZDAPConfigTable.setStatus(_A)
_RuckusZDAPConfigEntry_Object=MibTableRow
ruckusZDAPConfigEntry=_RuckusZDAPConfigEntry_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1))
ruckusZDAPConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ruckusZDAPConfigEntry.setStatus(_A)
class _RuckusZDAPConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5000))
_RuckusZDAPConfigID_Type.__name__=_C
_RuckusZDAPConfigID_Object=MibTableColumn
ruckusZDAPConfigID=_RuckusZDAPConfigID_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,1),_RuckusZDAPConfigID_Type())
ruckusZDAPConfigID.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDAPConfigID.setStatus(_A)
_RuckusZDAPConfigMacAddress_Type=MacAddress
_RuckusZDAPConfigMacAddress_Object=MibTableColumn
ruckusZDAPConfigMacAddress=_RuckusZDAPConfigMacAddress_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,2),_RuckusZDAPConfigMacAddress_Type())
ruckusZDAPConfigMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPConfigMacAddress.setStatus(_A)
class _RuckusZDAPConfigAPModel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDAPConfigAPModel_Type.__name__=_D
_RuckusZDAPConfigAPModel_Object=MibTableColumn
ruckusZDAPConfigAPModel=_RuckusZDAPConfigAPModel_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,4),_RuckusZDAPConfigAPModel_Type())
ruckusZDAPConfigAPModel.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPConfigAPModel.setStatus(_A)
class _RuckusZDAPConfigDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDAPConfigDeviceName_Type.__name__=_D
_RuckusZDAPConfigDeviceName_Object=MibTableColumn
ruckusZDAPConfigDeviceName=_RuckusZDAPConfigDeviceName_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,5),_RuckusZDAPConfigDeviceName_Type())
ruckusZDAPConfigDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigDeviceName.setStatus(_A)
class _RuckusZDAPConfigDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RuckusZDAPConfigDescription_Type.__name__=_D
_RuckusZDAPConfigDescription_Object=MibTableColumn
ruckusZDAPConfigDescription=_RuckusZDAPConfigDescription_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,6),_RuckusZDAPConfigDescription_Type())
ruckusZDAPConfigDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigDescription.setStatus(_A)
class _RuckusZDAPConfigLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusZDAPConfigLocation_Type.__name__=_D
_RuckusZDAPConfigLocation_Object=MibTableColumn
ruckusZDAPConfigLocation=_RuckusZDAPConfigLocation_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,7),_RuckusZDAPConfigLocation_Type())
ruckusZDAPConfigLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigLocation.setStatus(_A)
class _RuckusZDAPConfigGpsLatitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RuckusZDAPConfigGpsLatitude_Type.__name__=_D
_RuckusZDAPConfigGpsLatitude_Object=MibTableColumn
ruckusZDAPConfigGpsLatitude=_RuckusZDAPConfigGpsLatitude_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,10),_RuckusZDAPConfigGpsLatitude_Type())
ruckusZDAPConfigGpsLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigGpsLatitude.setStatus(_A)
class _RuckusZDAPConfigGpsLongitude_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RuckusZDAPConfigGpsLongitude_Type.__name__=_D
_RuckusZDAPConfigGpsLongitude_Object=MibTableColumn
ruckusZDAPConfigGpsLongitude=_RuckusZDAPConfigGpsLongitude_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,11),_RuckusZDAPConfigGpsLongitude_Type())
ruckusZDAPConfigGpsLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigGpsLongitude.setStatus(_A)
class _RuckusZDAPConfigIPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('dualstack',3),('useparentsetting',4)))
_RuckusZDAPConfigIPVersion_Type.__name__=_C
_RuckusZDAPConfigIPVersion_Object=MibTableColumn
ruckusZDAPConfigIPVersion=_RuckusZDAPConfigIPVersion_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,14),_RuckusZDAPConfigIPVersion_Type())
ruckusZDAPConfigIPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIPVersion.setStatus(_A)
class _RuckusZDAPConfigIpAddressSettingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('admin-by-dhcp',2),(_K,3)))
_RuckusZDAPConfigIpAddressSettingMode_Type.__name__=_C
_RuckusZDAPConfigIpAddressSettingMode_Object=MibTableColumn
ruckusZDAPConfigIpAddressSettingMode=_RuckusZDAPConfigIpAddressSettingMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,15),_RuckusZDAPConfigIpAddressSettingMode_Type())
ruckusZDAPConfigIpAddressSettingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIpAddressSettingMode.setStatus(_A)
_RuckusZDAPConfigIpAddress_Type=IpAddress
_RuckusZDAPConfigIpAddress_Object=MibTableColumn
ruckusZDAPConfigIpAddress=_RuckusZDAPConfigIpAddress_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,16),_RuckusZDAPConfigIpAddress_Type())
ruckusZDAPConfigIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIpAddress.setStatus(_A)
_RuckusZDAPConfigIpAddressMask_Type=IpAddress
_RuckusZDAPConfigIpAddressMask_Object=MibTableColumn
ruckusZDAPConfigIpAddressMask=_RuckusZDAPConfigIpAddressMask_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,17),_RuckusZDAPConfigIpAddressMask_Type())
ruckusZDAPConfigIpAddressMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIpAddressMask.setStatus(_A)
_RuckusZDAPConfigGatewayIpAddress_Type=IpAddress
_RuckusZDAPConfigGatewayIpAddress_Object=MibTableColumn
ruckusZDAPConfigGatewayIpAddress=_RuckusZDAPConfigGatewayIpAddress_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,20),_RuckusZDAPConfigGatewayIpAddress_Type())
ruckusZDAPConfigGatewayIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigGatewayIpAddress.setStatus(_A)
class _RuckusZDAPConfigIpV6AddressSettingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('admin-by-autoconfig',2),(_K,3)))
_RuckusZDAPConfigIpV6AddressSettingMode_Type.__name__=_C
_RuckusZDAPConfigIpV6AddressSettingMode_Object=MibTableColumn
ruckusZDAPConfigIpV6AddressSettingMode=_RuckusZDAPConfigIpV6AddressSettingMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,21),_RuckusZDAPConfigIpV6AddressSettingMode_Type())
ruckusZDAPConfigIpV6AddressSettingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIpV6AddressSettingMode.setStatus(_A)
class _RuckusZDAPConfigIpV6Address_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDAPConfigIpV6Address_Type.__name__=_D
_RuckusZDAPConfigIpV6Address_Object=MibTableColumn
ruckusZDAPConfigIpV6Address=_RuckusZDAPConfigIpV6Address_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,22),_RuckusZDAPConfigIpV6Address_Type())
ruckusZDAPConfigIpV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIpV6Address.setStatus(_A)
class _RuckusZDAPConfigIpV6PrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,128))
_RuckusZDAPConfigIpV6PrefixLen_Type.__name__=_C
_RuckusZDAPConfigIpV6PrefixLen_Object=MibTableColumn
ruckusZDAPConfigIpV6PrefixLen=_RuckusZDAPConfigIpV6PrefixLen_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,23),_RuckusZDAPConfigIpV6PrefixLen_Type())
ruckusZDAPConfigIpV6PrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigIpV6PrefixLen.setStatus(_A)
class _RuckusZDAPConfigGatewayIpV6Address_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDAPConfigGatewayIpV6Address_Type.__name__=_D
_RuckusZDAPConfigGatewayIpV6Address_Object=MibTableColumn
ruckusZDAPConfigGatewayIpV6Address=_RuckusZDAPConfigGatewayIpV6Address_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,24),_RuckusZDAPConfigGatewayIpV6Address_Type())
ruckusZDAPConfigGatewayIpV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigGatewayIpV6Address.setStatus(_A)
_RuckusZDAPConfigPrimaryDnsIpAddress_Type=IpAddress
_RuckusZDAPConfigPrimaryDnsIpAddress_Object=MibTableColumn
ruckusZDAPConfigPrimaryDnsIpAddress=_RuckusZDAPConfigPrimaryDnsIpAddress_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,25),_RuckusZDAPConfigPrimaryDnsIpAddress_Type())
ruckusZDAPConfigPrimaryDnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigPrimaryDnsIpAddress.setStatus(_A)
_RuckusZDAPConfigSecondaryDnsIpAddress_Type=IpAddress
_RuckusZDAPConfigSecondaryDnsIpAddress_Object=MibTableColumn
ruckusZDAPConfigSecondaryDnsIpAddress=_RuckusZDAPConfigSecondaryDnsIpAddress_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,26),_RuckusZDAPConfigSecondaryDnsIpAddress_Type())
ruckusZDAPConfigSecondaryDnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigSecondaryDnsIpAddress.setStatus(_A)
class _RuckusZDAPConfigPrimaryDnsIpV6Address_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDAPConfigPrimaryDnsIpV6Address_Type.__name__=_D
_RuckusZDAPConfigPrimaryDnsIpV6Address_Object=MibTableColumn
ruckusZDAPConfigPrimaryDnsIpV6Address=_RuckusZDAPConfigPrimaryDnsIpV6Address_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,27),_RuckusZDAPConfigPrimaryDnsIpV6Address_Type())
ruckusZDAPConfigPrimaryDnsIpV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigPrimaryDnsIpV6Address.setStatus(_A)
class _RuckusZDAPConfigSecondaryDnsV6IpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusZDAPConfigSecondaryDnsV6IpAddress_Type.__name__=_D
_RuckusZDAPConfigSecondaryDnsV6IpAddress_Object=MibTableColumn
ruckusZDAPConfigSecondaryDnsV6IpAddress=_RuckusZDAPConfigSecondaryDnsV6IpAddress_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,28),_RuckusZDAPConfigSecondaryDnsV6IpAddress_Type())
ruckusZDAPConfigSecondaryDnsV6IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigSecondaryDnsV6IpAddress.setStatus(_A)
class _RuckusZDAPConfigRadioType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ieee80211bg',1),('ieee80211na',2),('ieee80211a',3),('ieee80211n',4),('ieee80211ng',5),('ieee80211ac',6)))
_RuckusZDAPConfigRadioType_Type.__name__=_C
_RuckusZDAPConfigRadioType_Object=MibTableColumn
ruckusZDAPConfigRadioType=_RuckusZDAPConfigRadioType_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,30),_RuckusZDAPConfigRadioType_Type())
ruckusZDAPConfigRadioType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioType.setStatus(_A)
class _RuckusZDAPConfigRadioChannel24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_RuckusZDAPConfigRadioChannel24_Type.__name__=_C
_RuckusZDAPConfigRadioChannel24_Object=MibTableColumn
ruckusZDAPConfigRadioChannel24=_RuckusZDAPConfigRadioChannel24_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,31),_RuckusZDAPConfigRadioChannel24_Type())
ruckusZDAPConfigRadioChannel24.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioChannel24.setStatus(_A)
class _RuckusZDAPConfigRadioTxPowerLevel24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_RuckusZDAPConfigRadioTxPowerLevel24_Type.__name__=_C
_RuckusZDAPConfigRadioTxPowerLevel24_Object=MibTableColumn
ruckusZDAPConfigRadioTxPowerLevel24=_RuckusZDAPConfigRadioTxPowerLevel24_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,32),_RuckusZDAPConfigRadioTxPowerLevel24_Type())
ruckusZDAPConfigRadioTxPowerLevel24.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioTxPowerLevel24.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioTxPowerLevel24.setUnits('dB')
class _RuckusZDAPConfigRadioWlanGroup24_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RuckusZDAPConfigRadioWlanGroup24_Type.__name__=_D
_RuckusZDAPConfigRadioWlanGroup24_Object=MibTableColumn
ruckusZDAPConfigRadioWlanGroup24=_RuckusZDAPConfigRadioWlanGroup24_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,33),_RuckusZDAPConfigRadioWlanGroup24_Type())
ruckusZDAPConfigRadioWlanGroup24.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioWlanGroup24.setStatus(_A)
class _RuckusZDAPConfigRadioEnableWlanService24_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_F,2)))
_RuckusZDAPConfigRadioEnableWlanService24_Type.__name__=_C
_RuckusZDAPConfigRadioEnableWlanService24_Object=MibTableColumn
ruckusZDAPConfigRadioEnableWlanService24=_RuckusZDAPConfigRadioEnableWlanService24_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,34),_RuckusZDAPConfigRadioEnableWlanService24_Type())
ruckusZDAPConfigRadioEnableWlanService24.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioEnableWlanService24.setStatus(_A)
class _RuckusZDAPConfigRadioChannel5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(36,165))
_RuckusZDAPConfigRadioChannel5_Type.__name__=_C
_RuckusZDAPConfigRadioChannel5_Object=MibTableColumn
ruckusZDAPConfigRadioChannel5=_RuckusZDAPConfigRadioChannel5_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,40),_RuckusZDAPConfigRadioChannel5_Type())
ruckusZDAPConfigRadioChannel5.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioChannel5.setStatus(_A)
class _RuckusZDAPConfigRadioTxPowerLevel5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_RuckusZDAPConfigRadioTxPowerLevel5_Type.__name__=_C
_RuckusZDAPConfigRadioTxPowerLevel5_Object=MibTableColumn
ruckusZDAPConfigRadioTxPowerLevel5=_RuckusZDAPConfigRadioTxPowerLevel5_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,41),_RuckusZDAPConfigRadioTxPowerLevel5_Type())
ruckusZDAPConfigRadioTxPowerLevel5.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioTxPowerLevel5.setStatus(_A)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioTxPowerLevel5.setUnits('dB')
class _RuckusZDAPConfigRadioWlanGroup5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RuckusZDAPConfigRadioWlanGroup5_Type.__name__=_D
_RuckusZDAPConfigRadioWlanGroup5_Object=MibTableColumn
ruckusZDAPConfigRadioWlanGroup5=_RuckusZDAPConfigRadioWlanGroup5_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,42),_RuckusZDAPConfigRadioWlanGroup5_Type())
ruckusZDAPConfigRadioWlanGroup5.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioWlanGroup5.setStatus(_A)
class _RuckusZDAPConfigRadioEnableWlanService5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_F,2)))
_RuckusZDAPConfigRadioEnableWlanService5_Type.__name__=_C
_RuckusZDAPConfigRadioEnableWlanService5_Object=MibTableColumn
ruckusZDAPConfigRadioEnableWlanService5=_RuckusZDAPConfigRadioEnableWlanService5_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,43),_RuckusZDAPConfigRadioEnableWlanService5_Type())
ruckusZDAPConfigRadioEnableWlanService5.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRadioEnableWlanService5.setStatus(_A)
class _RuckusZDAPConfigMeshConfigurationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('root-ap',2),('mesh-ap',3),('disabled',4)))
_RuckusZDAPConfigMeshConfigurationMode_Type.__name__=_C
_RuckusZDAPConfigMeshConfigurationMode_Object=MibTableColumn
ruckusZDAPConfigMeshConfigurationMode=_RuckusZDAPConfigMeshConfigurationMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,50),_RuckusZDAPConfigMeshConfigurationMode_Type())
ruckusZDAPConfigMeshConfigurationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigMeshConfigurationMode.setStatus(_A)
class _RuckusZDAPConfigUplinkSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('smart',1),('manual',2)))
_RuckusZDAPConfigUplinkSelectionMode_Type.__name__=_C
_RuckusZDAPConfigUplinkSelectionMode_Object=MibTableColumn
ruckusZDAPConfigUplinkSelectionMode=_RuckusZDAPConfigUplinkSelectionMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,51),_RuckusZDAPConfigUplinkSelectionMode_Type())
ruckusZDAPConfigUplinkSelectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigUplinkSelectionMode.setStatus(_A)
class _RuckusZDAPConfigApproveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('approved',1),('not-approved',2)))
_RuckusZDAPConfigApproveMode_Type.__name__=_C
_RuckusZDAPConfigApproveMode_Object=MibTableColumn
ruckusZDAPConfigApproveMode=_RuckusZDAPConfigApproveMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,52),_RuckusZDAPConfigApproveMode_Type())
ruckusZDAPConfigApproveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigApproveMode.setStatus(_A)
class _RuckusZDAPConfigManagementAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('associated',2)))
_RuckusZDAPConfigManagementAdmin_Type.__name__=_C
_RuckusZDAPConfigManagementAdmin_Object=MibTableColumn
ruckusZDAPConfigManagementAdmin=_RuckusZDAPConfigManagementAdmin_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,60),_RuckusZDAPConfigManagementAdmin_Type())
ruckusZDAPConfigManagementAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigManagementAdmin.setStatus(_A)
class _RuckusZDAPConfigRebootNow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_RuckusZDAPConfigRebootNow_Type.__name__=_C
_RuckusZDAPConfigRebootNow_Object=MibTableColumn
ruckusZDAPConfigRebootNow=_RuckusZDAPConfigRebootNow_Object((1,3,6,1,4,1,25053,1,2,2,4,1,1,1,1,64),_RuckusZDAPConfigRebootNow_Type())
ruckusZDAPConfigRebootNow.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusZDAPConfigRebootNow.setStatus(_A)
_RuckusZDAPLBSInfo_ObjectIdentity=ObjectIdentity
ruckusZDAPLBSInfo=_RuckusZDAPLBSInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,2,2,4,1,2))
_RuckusZDAPLBSVenueTable_Object=MibTable
ruckusZDAPLBSVenueTable=_RuckusZDAPLBSVenueTable_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1))
if mibBuilder.loadTexts:ruckusZDAPLBSVenueTable.setStatus(_A)
_RuckusZDAPLBSVenueEntry_Object=MibTableRow
ruckusZDAPLBSVenueEntry=_RuckusZDAPLBSVenueEntry_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1))
ruckusZDAPLBSVenueEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:ruckusZDAPLBSVenueEntry.setStatus(_A)
class _RuckusZDAPLBSAPGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RuckusZDAPLBSAPGroupID_Type.__name__=_C
_RuckusZDAPLBSAPGroupID_Object=MibTableColumn
ruckusZDAPLBSAPGroupID=_RuckusZDAPLBSAPGroupID_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1,1),_RuckusZDAPLBSAPGroupID_Type())
ruckusZDAPLBSAPGroupID.setMaxAccess(_I)
if mibBuilder.loadTexts:ruckusZDAPLBSAPGroupID.setStatus(_A)
class _RuckusZDAPLBSVenueName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RuckusZDAPLBSVenueName_Type.__name__=_D
_RuckusZDAPLBSVenueName_Object=MibTableColumn
ruckusZDAPLBSVenueName=_RuckusZDAPLBSVenueName_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1,2),_RuckusZDAPLBSVenueName_Type())
ruckusZDAPLBSVenueName.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPLBSVenueName.setStatus(_A)
class _RuckusZDAPLBSVenueAPGrpName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusZDAPLBSVenueAPGrpName_Type.__name__=_D
_RuckusZDAPLBSVenueAPGrpName_Object=MibTableColumn
ruckusZDAPLBSVenueAPGrpName=_RuckusZDAPLBSVenueAPGrpName_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1,3),_RuckusZDAPLBSVenueAPGrpName_Type())
ruckusZDAPLBSVenueAPGrpName.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPLBSVenueAPGrpName.setStatus(_A)
class _RuckusZDAPLBSVenueLSConnection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_RuckusZDAPLBSVenueLSConnection_Type.__name__=_C
_RuckusZDAPLBSVenueLSConnection_Object=MibTableColumn
ruckusZDAPLBSVenueLSConnection=_RuckusZDAPLBSVenueLSConnection_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1,4),_RuckusZDAPLBSVenueLSConnection_Type())
ruckusZDAPLBSVenueLSConnection.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPLBSVenueLSConnection.setStatus(_A)
class _RuckusZDAPLBSVenue24GMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_N,1),(_O,2)))
_RuckusZDAPLBSVenue24GMode_Type.__name__=_C
_RuckusZDAPLBSVenue24GMode_Object=MibTableColumn
ruckusZDAPLBSVenue24GMode=_RuckusZDAPLBSVenue24GMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1,5),_RuckusZDAPLBSVenue24GMode_Type())
ruckusZDAPLBSVenue24GMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPLBSVenue24GMode.setStatus(_A)
class _RuckusZDAPLBSVenue5GMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_N,1),(_O,2)))
_RuckusZDAPLBSVenue5GMode_Type.__name__=_C
_RuckusZDAPLBSVenue5GMode_Object=MibTableColumn
ruckusZDAPLBSVenue5GMode=_RuckusZDAPLBSVenue5GMode_Object((1,3,6,1,4,1,25053,1,2,2,4,1,2,1,1,6),_RuckusZDAPLBSVenue5GMode_Type())
ruckusZDAPLBSVenue5GMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusZDAPLBSVenue5GMode.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ruckusZDAPMIB':ruckusZDAPMIB,'ruckusZDAPObjects':ruckusZDAPObjects,'ruckusZDAPConfig':ruckusZDAPConfig,'ruckusZDAPConfigTable':ruckusZDAPConfigTable,'ruckusZDAPConfigEntry':ruckusZDAPConfigEntry,_H:ruckusZDAPConfigID,'ruckusZDAPConfigMacAddress':ruckusZDAPConfigMacAddress,'ruckusZDAPConfigAPModel':ruckusZDAPConfigAPModel,'ruckusZDAPConfigDeviceName':ruckusZDAPConfigDeviceName,'ruckusZDAPConfigDescription':ruckusZDAPConfigDescription,'ruckusZDAPConfigLocation':ruckusZDAPConfigLocation,'ruckusZDAPConfigGpsLatitude':ruckusZDAPConfigGpsLatitude,'ruckusZDAPConfigGpsLongitude':ruckusZDAPConfigGpsLongitude,'ruckusZDAPConfigIPVersion':ruckusZDAPConfigIPVersion,'ruckusZDAPConfigIpAddressSettingMode':ruckusZDAPConfigIpAddressSettingMode,'ruckusZDAPConfigIpAddress':ruckusZDAPConfigIpAddress,'ruckusZDAPConfigIpAddressMask':ruckusZDAPConfigIpAddressMask,'ruckusZDAPConfigGatewayIpAddress':ruckusZDAPConfigGatewayIpAddress,'ruckusZDAPConfigIpV6AddressSettingMode':ruckusZDAPConfigIpV6AddressSettingMode,'ruckusZDAPConfigIpV6Address':ruckusZDAPConfigIpV6Address,'ruckusZDAPConfigIpV6PrefixLen':ruckusZDAPConfigIpV6PrefixLen,'ruckusZDAPConfigGatewayIpV6Address':ruckusZDAPConfigGatewayIpV6Address,'ruckusZDAPConfigPrimaryDnsIpAddress':ruckusZDAPConfigPrimaryDnsIpAddress,'ruckusZDAPConfigSecondaryDnsIpAddress':ruckusZDAPConfigSecondaryDnsIpAddress,'ruckusZDAPConfigPrimaryDnsIpV6Address':ruckusZDAPConfigPrimaryDnsIpV6Address,'ruckusZDAPConfigSecondaryDnsV6IpAddress':ruckusZDAPConfigSecondaryDnsV6IpAddress,'ruckusZDAPConfigRadioType':ruckusZDAPConfigRadioType,'ruckusZDAPConfigRadioChannel24':ruckusZDAPConfigRadioChannel24,'ruckusZDAPConfigRadioTxPowerLevel24':ruckusZDAPConfigRadioTxPowerLevel24,'ruckusZDAPConfigRadioWlanGroup24':ruckusZDAPConfigRadioWlanGroup24,'ruckusZDAPConfigRadioEnableWlanService24':ruckusZDAPConfigRadioEnableWlanService24,'ruckusZDAPConfigRadioChannel5':ruckusZDAPConfigRadioChannel5,'ruckusZDAPConfigRadioTxPowerLevel5':ruckusZDAPConfigRadioTxPowerLevel5,'ruckusZDAPConfigRadioWlanGroup5':ruckusZDAPConfigRadioWlanGroup5,'ruckusZDAPConfigRadioEnableWlanService5':ruckusZDAPConfigRadioEnableWlanService5,'ruckusZDAPConfigMeshConfigurationMode':ruckusZDAPConfigMeshConfigurationMode,'ruckusZDAPConfigUplinkSelectionMode':ruckusZDAPConfigUplinkSelectionMode,'ruckusZDAPConfigApproveMode':ruckusZDAPConfigApproveMode,'ruckusZDAPConfigManagementAdmin':ruckusZDAPConfigManagementAdmin,'ruckusZDAPConfigRebootNow':ruckusZDAPConfigRebootNow,'ruckusZDAPLBSInfo':ruckusZDAPLBSInfo,'ruckusZDAPLBSVenueTable':ruckusZDAPLBSVenueTable,'ruckusZDAPLBSVenueEntry':ruckusZDAPLBSVenueEntry,_M:ruckusZDAPLBSAPGroupID,'ruckusZDAPLBSVenueName':ruckusZDAPLBSVenueName,'ruckusZDAPLBSVenueAPGrpName':ruckusZDAPLBSVenueAPGrpName,'ruckusZDAPLBSVenueLSConnection':ruckusZDAPLBSVenueLSConnection,'ruckusZDAPLBSVenue24GMode':ruckusZDAPLBSVenue24GMode,'ruckusZDAPLBSVenue5GMode':ruckusZDAPLBSVenue5GMode})