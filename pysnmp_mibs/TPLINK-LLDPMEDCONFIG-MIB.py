_M='lldpMedNeighborMediaPolicyIndex'
_L='lldpMedNeighborPortIndex'
_K='lldpMedNeighborPortIndexId'
_J='TPLINK-LLDPMEDCONFIG-MIB'
_I='enable'
_H='disable'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkLldpMIBObjects,=mibBuilder.importSymbols('TPLINK-LLDP-MIB','tplinkLldpMIBObjects')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
lldpMedNeighborInfo=ModuleIdentity((1,3,6,1,4,1,11863,6,35,1,4,5))
if mibBuilder.loadTexts:lldpMedNeighborInfo.setRevisions(('2011-09-27 00:00',))
_LldpMed_ObjectIdentity=ObjectIdentity
lldpMed=_LldpMed_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,4))
_LldpMedGlobalConfig_ObjectIdentity=ObjectIdentity
lldpMedGlobalConfig=_LldpMedGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,4,1))
class _LldpMedGlobalConfigFastStartRepeatCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpMedGlobalConfigFastStartRepeatCount_Type.__name__=_E
_LldpMedGlobalConfigFastStartRepeatCount_Object=MibScalar
lldpMedGlobalConfigFastStartRepeatCount=_LldpMedGlobalConfigFastStartRepeatCount_Object((1,3,6,1,4,1,11863,6,35,1,4,1,1),_LldpMedGlobalConfigFastStartRepeatCount_Type())
lldpMedGlobalConfigFastStartRepeatCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedGlobalConfigFastStartRepeatCount.setStatus(_A)
_LldpMedPortConfigTable_Object=MibTable
lldpMedPortConfigTable=_LldpMedPortConfigTable_Object((1,3,6,1,4,1,11863,6,35,1,4,2))
if mibBuilder.loadTexts:lldpMedPortConfigTable.setStatus(_A)
_LldpMedPortConfigEntry_Object=MibTableRow
lldpMedPortConfigEntry=_LldpMedPortConfigEntry_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1))
lldpMedPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:lldpMedPortConfigEntry.setStatus(_A)
class _LldpMedConfigPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpMedConfigPortId_Type.__name__=_B
_LldpMedConfigPortId_Object=MibTableColumn
lldpMedConfigPortId=_LldpMedConfigPortId_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1,1),_LldpMedConfigPortId_Type())
lldpMedConfigPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedConfigPortId.setStatus(_A)
class _LldpMedConfigPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LldpMedConfigPortStatus_Type.__name__=_E
_LldpMedConfigPortStatus_Object=MibTableColumn
lldpMedConfigPortStatus=_LldpMedConfigPortStatus_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1,2),_LldpMedConfigPortStatus_Type())
lldpMedConfigPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortStatus.setStatus(_A)
class _LldpMedConfigPortTlvNetworkPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LldpMedConfigPortTlvNetworkPolicy_Type.__name__=_E
_LldpMedConfigPortTlvNetworkPolicy_Object=MibTableColumn
lldpMedConfigPortTlvNetworkPolicy=_LldpMedConfigPortTlvNetworkPolicy_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1,3),_LldpMedConfigPortTlvNetworkPolicy_Type())
lldpMedConfigPortTlvNetworkPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortTlvNetworkPolicy.setStatus(_A)
class _LldpMedConfigPortTlvLocationId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LldpMedConfigPortTlvLocationId_Type.__name__=_E
_LldpMedConfigPortTlvLocationId_Object=MibTableColumn
lldpMedConfigPortTlvLocationId=_LldpMedConfigPortTlvLocationId_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1,4),_LldpMedConfigPortTlvLocationId_Type())
lldpMedConfigPortTlvLocationId.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortTlvLocationId.setStatus(_A)
class _LldpMedConfigPortTlvExtendedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LldpMedConfigPortTlvExtendedPower_Type.__name__=_E
_LldpMedConfigPortTlvExtendedPower_Object=MibTableColumn
lldpMedConfigPortTlvExtendedPower=_LldpMedConfigPortTlvExtendedPower_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1,5),_LldpMedConfigPortTlvExtendedPower_Type())
lldpMedConfigPortTlvExtendedPower.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortTlvExtendedPower.setStatus(_A)
class _LldpMedConfigPortTlvInventory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LldpMedConfigPortTlvInventory_Type.__name__=_E
_LldpMedConfigPortTlvInventory_Object=MibTableColumn
lldpMedConfigPortTlvInventory=_LldpMedConfigPortTlvInventory_Object((1,3,6,1,4,1,11863,6,35,1,4,2,1,6),_LldpMedConfigPortTlvInventory_Type())
lldpMedConfigPortTlvInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortTlvInventory.setStatus(_A)
_LldpMedPortConfigTlvLocationTable_Object=MibTable
lldpMedPortConfigTlvLocationTable=_LldpMedPortConfigTlvLocationTable_Object((1,3,6,1,4,1,11863,6,35,1,4,3))
if mibBuilder.loadTexts:lldpMedPortConfigTlvLocationTable.setStatus(_A)
_LldpMedPortConfigTlvLocationEntry_Object=MibTableRow
lldpMedPortConfigTlvLocationEntry=_LldpMedPortConfigTlvLocationEntry_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1))
lldpMedPortConfigTlvLocationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:lldpMedPortConfigTlvLocationEntry.setStatus(_A)
class _LldpMedConfigLocationPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpMedConfigLocationPortId_Type.__name__=_B
_LldpMedConfigLocationPortId_Object=MibTableColumn
lldpMedConfigLocationPortId=_LldpMedConfigLocationPortId_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,1),_LldpMedConfigLocationPortId_Type())
lldpMedConfigLocationPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedConfigLocationPortId.setStatus(_A)
class _LldpMedConfigPortLocationEmergencyNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,25))
_LldpMedConfigPortLocationEmergencyNumber_Type.__name__=_B
_LldpMedConfigPortLocationEmergencyNumber_Object=MibTableColumn
lldpMedConfigPortLocationEmergencyNumber=_LldpMedConfigPortLocationEmergencyNumber_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,2),_LldpMedConfigPortLocationEmergencyNumber_Type())
lldpMedConfigPortLocationEmergencyNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationEmergencyNumber.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressWhat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dhcp-server',0),('switch',1),('lldp-med-endpoint',2)))
_LldpMedConfigPortLocationCivicAddressWhat_Type.__name__=_E
_LldpMedConfigPortLocationCivicAddressWhat_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressWhat=_LldpMedConfigPortLocationCivicAddressWhat_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,3),_LldpMedConfigPortLocationCivicAddressWhat_Type())
lldpMedConfigPortLocationCivicAddressWhat.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressWhat.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_LldpMedConfigPortLocationCivicAddressCountryCode_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressCountryCode_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressCountryCode=_LldpMedConfigPortLocationCivicAddressCountryCode_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,4),_LldpMedConfigPortLocationCivicAddressCountryCode_Type())
lldpMedConfigPortLocationCivicAddressCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressCountryCode.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressLanguage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressLanguage_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressLanguage_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressLanguage=_LldpMedConfigPortLocationCivicAddressLanguage_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,5),_LldpMedConfigPortLocationCivicAddressLanguage_Type())
lldpMedConfigPortLocationCivicAddressLanguage.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressLanguage.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressProvince_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressProvince_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressProvince_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressProvince=_LldpMedConfigPortLocationCivicAddressProvince_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,6),_LldpMedConfigPortLocationCivicAddressProvince_Type())
lldpMedConfigPortLocationCivicAddressProvince.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressProvince.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressCounty_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressCounty_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressCounty_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressCounty=_LldpMedConfigPortLocationCivicAddressCounty_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,7),_LldpMedConfigPortLocationCivicAddressCounty_Type())
lldpMedConfigPortLocationCivicAddressCounty.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressCounty.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressCity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressCity_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressCity_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressCity=_LldpMedConfigPortLocationCivicAddressCity_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,8),_LldpMedConfigPortLocationCivicAddressCity_Type())
lldpMedConfigPortLocationCivicAddressCity.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressCity.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressStreet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressStreet_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressStreet_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressStreet=_LldpMedConfigPortLocationCivicAddressStreet_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,9),_LldpMedConfigPortLocationCivicAddressStreet_Type())
lldpMedConfigPortLocationCivicAddressStreet.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressStreet.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressHouseNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressHouseNumber_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressHouseNumber_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressHouseNumber=_LldpMedConfigPortLocationCivicAddressHouseNumber_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,10),_LldpMedConfigPortLocationCivicAddressHouseNumber_Type())
lldpMedConfigPortLocationCivicAddressHouseNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressHouseNumber.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressName_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressName_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressName=_LldpMedConfigPortLocationCivicAddressName_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,11),_LldpMedConfigPortLocationCivicAddressName_Type())
lldpMedConfigPortLocationCivicAddressName.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressName.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressPostalZipCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressPostalZipCode_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressPostalZipCode_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressPostalZipCode=_LldpMedConfigPortLocationCivicAddressPostalZipCode_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,12),_LldpMedConfigPortLocationCivicAddressPostalZipCode_Type())
lldpMedConfigPortLocationCivicAddressPostalZipCode.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressPostalZipCode.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressRoomNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressRoomNumber_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressRoomNumber_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressRoomNumber=_LldpMedConfigPortLocationCivicAddressRoomNumber_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,13),_LldpMedConfigPortLocationCivicAddressRoomNumber_Type())
lldpMedConfigPortLocationCivicAddressRoomNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressRoomNumber.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressPostOfficeBox_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressPostOfficeBox_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressPostOfficeBox_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressPostOfficeBox=_LldpMedConfigPortLocationCivicAddressPostOfficeBox_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,14),_LldpMedConfigPortLocationCivicAddressPostOfficeBox_Type())
lldpMedConfigPortLocationCivicAddressPostOfficeBox.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressPostOfficeBox.setStatus(_A)
class _LldpMedConfigPortLocationCivicAddressAdditional_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpMedConfigPortLocationCivicAddressAdditional_Type.__name__=_B
_LldpMedConfigPortLocationCivicAddressAdditional_Object=MibTableColumn
lldpMedConfigPortLocationCivicAddressAdditional=_LldpMedConfigPortLocationCivicAddressAdditional_Object((1,3,6,1,4,1,11863,6,35,1,4,3,1,15),_LldpMedConfigPortLocationCivicAddressAdditional_Type())
lldpMedConfigPortLocationCivicAddressAdditional.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpMedConfigPortLocationCivicAddressAdditional.setStatus(_A)
_LldpMedLocalInfoTable_Object=MibTable
lldpMedLocalInfoTable=_LldpMedLocalInfoTable_Object((1,3,6,1,4,1,11863,6,35,1,4,4))
if mibBuilder.loadTexts:lldpMedLocalInfoTable.setStatus(_A)
_LldpMedLocalInfoEntry_Object=MibTableRow
lldpMedLocalInfoEntry=_LldpMedLocalInfoEntry_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1))
lldpMedLocalInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:lldpMedLocalInfoEntry.setStatus(_A)
class _LldpMedLocalPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpMedLocalPortId_Type.__name__=_B
_LldpMedLocalPortId_Object=MibTableColumn
lldpMedLocalPortId=_LldpMedLocalPortId_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,1),_LldpMedLocalPortId_Type())
lldpMedLocalPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalPortId.setStatus(_A)
class _LldpMEDLocalCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_LldpMEDLocalCapabilities_Type.__name__=_B
_LldpMEDLocalCapabilities_Object=MibTableColumn
lldpMEDLocalCapabilities=_LldpMEDLocalCapabilities_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,2),_LldpMEDLocalCapabilities_Type())
lldpMEDLocalCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMEDLocalCapabilities.setStatus(_A)
class _LldpMedLocalDeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalDeviceType_Type.__name__=_B
_LldpMedLocalDeviceType_Object=MibTableColumn
lldpMedLocalDeviceType=_LldpMedLocalDeviceType_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,3),_LldpMedLocalDeviceType_Type())
lldpMedLocalDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalDeviceType.setStatus(_A)
class _LldpMedLocalApplicationType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalApplicationType_Type.__name__=_B
_LldpMedLocalApplicationType_Object=MibTableColumn
lldpMedLocalApplicationType=_LldpMedLocalApplicationType_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,4),_LldpMedLocalApplicationType_Type())
lldpMedLocalApplicationType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalApplicationType.setStatus(_A)
class _LldpMedLocalUnknownPolicy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_LldpMedLocalUnknownPolicy_Type.__name__=_B
_LldpMedLocalUnknownPolicy_Object=MibTableColumn
lldpMedLocalUnknownPolicy=_LldpMedLocalUnknownPolicy_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,5),_LldpMedLocalUnknownPolicy_Type())
lldpMedLocalUnknownPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalUnknownPolicy.setStatus(_A)
class _LldpMedLocalAppTagged_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_LldpMedLocalAppTagged_Type.__name__=_B
_LldpMedLocalAppTagged_Object=MibTableColumn
lldpMedLocalAppTagged=_LldpMedLocalAppTagged_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,6),_LldpMedLocalAppTagged_Type())
lldpMedLocalAppTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalAppTagged.setStatus(_A)
_LldpMedLocalAppVLANID_Type=Integer32
_LldpMedLocalAppVLANID_Object=MibTableColumn
lldpMedLocalAppVLANID=_LldpMedLocalAppVLANID_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,7),_LldpMedLocalAppVLANID_Type())
lldpMedLocalAppVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalAppVLANID.setStatus(_A)
_LldpMedLocalAppLayer2Priority_Type=Integer32
_LldpMedLocalAppLayer2Priority_Object=MibTableColumn
lldpMedLocalAppLayer2Priority=_LldpMedLocalAppLayer2Priority_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,8),_LldpMedLocalAppLayer2Priority_Type())
lldpMedLocalAppLayer2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalAppLayer2Priority.setStatus(_A)
_LldpMedLocalAppDSCP_Type=Integer32
_LldpMedLocalAppDSCP_Object=MibTableColumn
lldpMedLocalAppDSCP=_LldpMedLocalAppDSCP_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,9),_LldpMedLocalAppDSCP_Type())
lldpMedLocalAppDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalAppDSCP.setStatus(_A)
class _LldpMedLocalLocationDataFormat_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalLocationDataFormat_Type.__name__=_B
_LldpMedLocalLocationDataFormat_Object=MibTableColumn
lldpMedLocalLocationDataFormat=_LldpMedLocalLocationDataFormat_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,10),_LldpMedLocalLocationDataFormat_Type())
lldpMedLocalLocationDataFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalLocationDataFormat.setStatus(_A)
class _LldpMedLocalLocationID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_LldpMedLocalLocationID_Type.__name__=_B
_LldpMedLocalLocationID_Object=MibTableColumn
lldpMedLocalLocationID=_LldpMedLocalLocationID_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,11),_LldpMedLocalLocationID_Type())
lldpMedLocalLocationID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalLocationID.setStatus(_A)
class _LldpMedLocalPowerType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalPowerType_Type.__name__=_B
_LldpMedLocalPowerType_Object=MibTableColumn
lldpMedLocalPowerType=_LldpMedLocalPowerType_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,12),_LldpMedLocalPowerType_Type())
lldpMedLocalPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalPowerType.setStatus(_A)
class _LldpMedLocalPowerSource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalPowerSource_Type.__name__=_B
_LldpMedLocalPowerSource_Object=MibTableColumn
lldpMedLocalPowerSource=_LldpMedLocalPowerSource_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,13),_LldpMedLocalPowerSource_Type())
lldpMedLocalPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalPowerSource.setStatus(_A)
class _LldpMedLocalPowerPriority_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalPowerPriority_Type.__name__=_B
_LldpMedLocalPowerPriority_Object=MibTableColumn
lldpMedLocalPowerPriority=_LldpMedLocalPowerPriority_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,14),_LldpMedLocalPowerPriority_Type())
lldpMedLocalPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalPowerPriority.setStatus(_A)
class _LldpMedLocalPowerValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedLocalPowerValue_Type.__name__=_B
_LldpMedLocalPowerValue_Object=MibTableColumn
lldpMedLocalPowerValue=_LldpMedLocalPowerValue_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,15),_LldpMedLocalPowerValue_Type())
lldpMedLocalPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalPowerValue.setStatus(_A)
class _LldpMedLocalInventoryHardwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventoryHardwareRevision_Type.__name__=_B
_LldpMedLocalInventoryHardwareRevision_Object=MibTableColumn
lldpMedLocalInventoryHardwareRevision=_LldpMedLocalInventoryHardwareRevision_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,16),_LldpMedLocalInventoryHardwareRevision_Type())
lldpMedLocalInventoryHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventoryHardwareRevision.setStatus(_A)
class _LldpMedLocalInventoryFirmwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventoryFirmwareRevision_Type.__name__=_B
_LldpMedLocalInventoryFirmwareRevision_Object=MibTableColumn
lldpMedLocalInventoryFirmwareRevision=_LldpMedLocalInventoryFirmwareRevision_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,17),_LldpMedLocalInventoryFirmwareRevision_Type())
lldpMedLocalInventoryFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventoryFirmwareRevision.setStatus(_A)
class _LldpMedLocalInventorySoftwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventorySoftwareRevision_Type.__name__=_B
_LldpMedLocalInventorySoftwareRevision_Object=MibTableColumn
lldpMedLocalInventorySoftwareRevision=_LldpMedLocalInventorySoftwareRevision_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,18),_LldpMedLocalInventorySoftwareRevision_Type())
lldpMedLocalInventorySoftwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventorySoftwareRevision.setStatus(_A)
class _LldpMedLocalInventorySerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventorySerialNumber_Type.__name__=_B
_LldpMedLocalInventorySerialNumber_Object=MibTableColumn
lldpMedLocalInventorySerialNumber=_LldpMedLocalInventorySerialNumber_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,19),_LldpMedLocalInventorySerialNumber_Type())
lldpMedLocalInventorySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventorySerialNumber.setStatus(_A)
class _LldpMedLocalInventoryManufacturerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventoryManufacturerName_Type.__name__=_B
_LldpMedLocalInventoryManufacturerName_Object=MibTableColumn
lldpMedLocalInventoryManufacturerName=_LldpMedLocalInventoryManufacturerName_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,20),_LldpMedLocalInventoryManufacturerName_Type())
lldpMedLocalInventoryManufacturerName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventoryManufacturerName.setStatus(_A)
class _LldpMedLocalInventoryModelName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventoryModelName_Type.__name__=_B
_LldpMedLocalInventoryModelName_Object=MibTableColumn
lldpMedLocalInventoryModelName=_LldpMedLocalInventoryModelName_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,21),_LldpMedLocalInventoryModelName_Type())
lldpMedLocalInventoryModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventoryModelName.setStatus(_A)
class _LldpMedLocalInventoryAssetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedLocalInventoryAssetID_Type.__name__=_B
_LldpMedLocalInventoryAssetID_Object=MibTableColumn
lldpMedLocalInventoryAssetID=_LldpMedLocalInventoryAssetID_Object((1,3,6,1,4,1,11863,6,35,1,4,4,1,22),_LldpMedLocalInventoryAssetID_Type())
lldpMedLocalInventoryAssetID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedLocalInventoryAssetID.setStatus(_A)
_LldpMedNeighborInfoTable_Object=MibTable
lldpMedNeighborInfoTable=_LldpMedNeighborInfoTable_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1))
if mibBuilder.loadTexts:lldpMedNeighborInfoTable.setStatus(_A)
_LldpMedNeighborInfoEntry_Object=MibTableRow
lldpMedNeighborInfoEntry=_LldpMedNeighborInfoEntry_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1))
lldpMedNeighborInfoEntry.setIndexNames((0,_F,_G),(0,_J,_K))
if mibBuilder.loadTexts:lldpMedNeighborInfoEntry.setStatus(_A)
class _LldpMedNeighborPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpMedNeighborPortId_Type.__name__=_B
_LldpMedNeighborPortId_Object=MibTableColumn
lldpMedNeighborPortId=_LldpMedNeighborPortId_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,1),_LldpMedNeighborPortId_Type())
lldpMedNeighborPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPortId.setStatus(_A)
_LldpMedNeighborPortIndexId_Type=Integer32
_LldpMedNeighborPortIndexId_Object=MibTableColumn
lldpMedNeighborPortIndexId=_LldpMedNeighborPortIndexId_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,2),_LldpMedNeighborPortIndexId_Type())
lldpMedNeighborPortIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPortIndexId.setStatus(_A)
class _LldpMEDNeighborCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_LldpMEDNeighborCapabilities_Type.__name__=_B
_LldpMEDNeighborCapabilities_Object=MibTableColumn
lldpMEDNeighborCapabilities=_LldpMEDNeighborCapabilities_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,3),_LldpMEDNeighborCapabilities_Type())
lldpMEDNeighborCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMEDNeighborCapabilities.setStatus(_A)
class _LldpMedNeighborDeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborDeviceType_Type.__name__=_B
_LldpMedNeighborDeviceType_Object=MibTableColumn
lldpMedNeighborDeviceType=_LldpMedNeighborDeviceType_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,4),_LldpMedNeighborDeviceType_Type())
lldpMedNeighborDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborDeviceType.setStatus(_A)
class _LldpMedNeighborLocationDataFormat_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborLocationDataFormat_Type.__name__=_B
_LldpMedNeighborLocationDataFormat_Object=MibTableColumn
lldpMedNeighborLocationDataFormat=_LldpMedNeighborLocationDataFormat_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,5),_LldpMedNeighborLocationDataFormat_Type())
lldpMedNeighborLocationDataFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborLocationDataFormat.setStatus(_A)
class _LldpMedNeighborLocationID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_LldpMedNeighborLocationID_Type.__name__=_B
_LldpMedNeighborLocationID_Object=MibTableColumn
lldpMedNeighborLocationID=_LldpMedNeighborLocationID_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,6),_LldpMedNeighborLocationID_Type())
lldpMedNeighborLocationID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborLocationID.setStatus(_A)
class _LldpMedNeighborPowerType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborPowerType_Type.__name__=_B
_LldpMedNeighborPowerType_Object=MibTableColumn
lldpMedNeighborPowerType=_LldpMedNeighborPowerType_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,7),_LldpMedNeighborPowerType_Type())
lldpMedNeighborPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPowerType.setStatus(_A)
class _LldpMedNeighborPowerSource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborPowerSource_Type.__name__=_B
_LldpMedNeighborPowerSource_Object=MibTableColumn
lldpMedNeighborPowerSource=_LldpMedNeighborPowerSource_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,8),_LldpMedNeighborPowerSource_Type())
lldpMedNeighborPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPowerSource.setStatus(_A)
class _LldpMedNeighborPowerPriority_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborPowerPriority_Type.__name__=_B
_LldpMedNeighborPowerPriority_Object=MibTableColumn
lldpMedNeighborPowerPriority=_LldpMedNeighborPowerPriority_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,9),_LldpMedNeighborPowerPriority_Type())
lldpMedNeighborPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPowerPriority.setStatus(_A)
class _LldpMedNeighborPowerValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborPowerValue_Type.__name__=_B
_LldpMedNeighborPowerValue_Object=MibTableColumn
lldpMedNeighborPowerValue=_LldpMedNeighborPowerValue_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,10),_LldpMedNeighborPowerValue_Type())
lldpMedNeighborPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPowerValue.setStatus(_A)
class _LldpMedNeighborInventoryHardwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventoryHardwareRevision_Type.__name__=_B
_LldpMedNeighborInventoryHardwareRevision_Object=MibTableColumn
lldpMedNeighborInventoryHardwareRevision=_LldpMedNeighborInventoryHardwareRevision_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,11),_LldpMedNeighborInventoryHardwareRevision_Type())
lldpMedNeighborInventoryHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventoryHardwareRevision.setStatus(_A)
class _LldpMedNeighborInventoryFirmwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventoryFirmwareRevision_Type.__name__=_B
_LldpMedNeighborInventoryFirmwareRevision_Object=MibTableColumn
lldpMedNeighborInventoryFirmwareRevision=_LldpMedNeighborInventoryFirmwareRevision_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,12),_LldpMedNeighborInventoryFirmwareRevision_Type())
lldpMedNeighborInventoryFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventoryFirmwareRevision.setStatus(_A)
class _LldpMedNeighborInventorySoftwareRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventorySoftwareRevision_Type.__name__=_B
_LldpMedNeighborInventorySoftwareRevision_Object=MibTableColumn
lldpMedNeighborInventorySoftwareRevision=_LldpMedNeighborInventorySoftwareRevision_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,13),_LldpMedNeighborInventorySoftwareRevision_Type())
lldpMedNeighborInventorySoftwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventorySoftwareRevision.setStatus(_A)
class _LldpMedNeighborInventorySerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventorySerialNumber_Type.__name__=_B
_LldpMedNeighborInventorySerialNumber_Object=MibTableColumn
lldpMedNeighborInventorySerialNumber=_LldpMedNeighborInventorySerialNumber_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,14),_LldpMedNeighborInventorySerialNumber_Type())
lldpMedNeighborInventorySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventorySerialNumber.setStatus(_A)
class _LldpMedNeighborInventoryManufacturerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventoryManufacturerName_Type.__name__=_B
_LldpMedNeighborInventoryManufacturerName_Object=MibTableColumn
lldpMedNeighborInventoryManufacturerName=_LldpMedNeighborInventoryManufacturerName_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,15),_LldpMedNeighborInventoryManufacturerName_Type())
lldpMedNeighborInventoryManufacturerName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventoryManufacturerName.setStatus(_A)
class _LldpMedNeighborInventoryModelName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventoryModelName_Type.__name__=_B
_LldpMedNeighborInventoryModelName_Object=MibTableColumn
lldpMedNeighborInventoryModelName=_LldpMedNeighborInventoryModelName_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,16),_LldpMedNeighborInventoryModelName_Type())
lldpMedNeighborInventoryModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventoryModelName.setStatus(_A)
class _LldpMedNeighborInventoryAssetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpMedNeighborInventoryAssetID_Type.__name__=_B
_LldpMedNeighborInventoryAssetID_Object=MibTableColumn
lldpMedNeighborInventoryAssetID=_LldpMedNeighborInventoryAssetID_Object((1,3,6,1,4,1,11863,6,35,1,4,5,1,1,17),_LldpMedNeighborInventoryAssetID_Type())
lldpMedNeighborInventoryAssetID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborInventoryAssetID.setStatus(_A)
_LldpMedNeighborMediaPolicyInfoTable_Object=MibTable
lldpMedNeighborMediaPolicyInfoTable=_LldpMedNeighborMediaPolicyInfoTable_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2))
if mibBuilder.loadTexts:lldpMedNeighborMediaPolicyInfoTable.setStatus(_A)
_LldpMedNeighborMediaPolicyInfoEntry_Object=MibTableRow
lldpMedNeighborMediaPolicyInfoEntry=_LldpMedNeighborMediaPolicyInfoEntry_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1))
lldpMedNeighborMediaPolicyInfoEntry.setIndexNames((0,_F,_G),(0,_J,_L),(0,_J,_M))
if mibBuilder.loadTexts:lldpMedNeighborMediaPolicyInfoEntry.setStatus(_A)
class _LldpMedNeighborPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpMedNeighborPort_Type.__name__=_B
_LldpMedNeighborPort_Object=MibTableColumn
lldpMedNeighborPort=_LldpMedNeighborPort_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,1),_LldpMedNeighborPort_Type())
lldpMedNeighborPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPort.setStatus(_A)
_LldpMedNeighborPortIndex_Type=Integer32
_LldpMedNeighborPortIndex_Object=MibTableColumn
lldpMedNeighborPortIndex=_LldpMedNeighborPortIndex_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,2),_LldpMedNeighborPortIndex_Type())
lldpMedNeighborPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborPortIndex.setStatus(_A)
_LldpMedNeighborMediaPolicyIndex_Type=Integer32
_LldpMedNeighborMediaPolicyIndex_Object=MibTableColumn
lldpMedNeighborMediaPolicyIndex=_LldpMedNeighborMediaPolicyIndex_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,3),_LldpMedNeighborMediaPolicyIndex_Type())
lldpMedNeighborMediaPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborMediaPolicyIndex.setStatus(_A)
class _LldpMedNeighborApplicationType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_LldpMedNeighborApplicationType_Type.__name__=_B
_LldpMedNeighborApplicationType_Object=MibTableColumn
lldpMedNeighborApplicationType=_LldpMedNeighborApplicationType_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,4),_LldpMedNeighborApplicationType_Type())
lldpMedNeighborApplicationType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborApplicationType.setStatus(_A)
class _LldpMedNeighborUnknownPolicy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_LldpMedNeighborUnknownPolicy_Type.__name__=_B
_LldpMedNeighborUnknownPolicy_Object=MibTableColumn
lldpMedNeighborUnknownPolicy=_LldpMedNeighborUnknownPolicy_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,5),_LldpMedNeighborUnknownPolicy_Type())
lldpMedNeighborUnknownPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborUnknownPolicy.setStatus(_A)
class _LldpMedNeighborAppTagged_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_LldpMedNeighborAppTagged_Type.__name__=_B
_LldpMedNeighborAppTagged_Object=MibTableColumn
lldpMedNeighborAppTagged=_LldpMedNeighborAppTagged_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,6),_LldpMedNeighborAppTagged_Type())
lldpMedNeighborAppTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborAppTagged.setStatus(_A)
_LldpMedNeighborAppVLANID_Type=Integer32
_LldpMedNeighborAppVLANID_Object=MibTableColumn
lldpMedNeighborAppVLANID=_LldpMedNeighborAppVLANID_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,7),_LldpMedNeighborAppVLANID_Type())
lldpMedNeighborAppVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborAppVLANID.setStatus(_A)
_LldpMedNeighborAppLayer2Priority_Type=Integer32
_LldpMedNeighborAppLayer2Priority_Object=MibTableColumn
lldpMedNeighborAppLayer2Priority=_LldpMedNeighborAppLayer2Priority_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,8),_LldpMedNeighborAppLayer2Priority_Type())
lldpMedNeighborAppLayer2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborAppLayer2Priority.setStatus(_A)
_LldpMedNeighborAppDSCP_Type=Integer32
_LldpMedNeighborAppDSCP_Object=MibTableColumn
lldpMedNeighborAppDSCP=_LldpMedNeighborAppDSCP_Object((1,3,6,1,4,1,11863,6,35,1,4,5,2,1,9),_LldpMedNeighborAppDSCP_Type())
lldpMedNeighborAppDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpMedNeighborAppDSCP.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'lldpMed':lldpMed,'lldpMedGlobalConfig':lldpMedGlobalConfig,'lldpMedGlobalConfigFastStartRepeatCount':lldpMedGlobalConfigFastStartRepeatCount,'lldpMedPortConfigTable':lldpMedPortConfigTable,'lldpMedPortConfigEntry':lldpMedPortConfigEntry,'lldpMedConfigPortId':lldpMedConfigPortId,'lldpMedConfigPortStatus':lldpMedConfigPortStatus,'lldpMedConfigPortTlvNetworkPolicy':lldpMedConfigPortTlvNetworkPolicy,'lldpMedConfigPortTlvLocationId':lldpMedConfigPortTlvLocationId,'lldpMedConfigPortTlvExtendedPower':lldpMedConfigPortTlvExtendedPower,'lldpMedConfigPortTlvInventory':lldpMedConfigPortTlvInventory,'lldpMedPortConfigTlvLocationTable':lldpMedPortConfigTlvLocationTable,'lldpMedPortConfigTlvLocationEntry':lldpMedPortConfigTlvLocationEntry,'lldpMedConfigLocationPortId':lldpMedConfigLocationPortId,'lldpMedConfigPortLocationEmergencyNumber':lldpMedConfigPortLocationEmergencyNumber,'lldpMedConfigPortLocationCivicAddressWhat':lldpMedConfigPortLocationCivicAddressWhat,'lldpMedConfigPortLocationCivicAddressCountryCode':lldpMedConfigPortLocationCivicAddressCountryCode,'lldpMedConfigPortLocationCivicAddressLanguage':lldpMedConfigPortLocationCivicAddressLanguage,'lldpMedConfigPortLocationCivicAddressProvince':lldpMedConfigPortLocationCivicAddressProvince,'lldpMedConfigPortLocationCivicAddressCounty':lldpMedConfigPortLocationCivicAddressCounty,'lldpMedConfigPortLocationCivicAddressCity':lldpMedConfigPortLocationCivicAddressCity,'lldpMedConfigPortLocationCivicAddressStreet':lldpMedConfigPortLocationCivicAddressStreet,'lldpMedConfigPortLocationCivicAddressHouseNumber':lldpMedConfigPortLocationCivicAddressHouseNumber,'lldpMedConfigPortLocationCivicAddressName':lldpMedConfigPortLocationCivicAddressName,'lldpMedConfigPortLocationCivicAddressPostalZipCode':lldpMedConfigPortLocationCivicAddressPostalZipCode,'lldpMedConfigPortLocationCivicAddressRoomNumber':lldpMedConfigPortLocationCivicAddressRoomNumber,'lldpMedConfigPortLocationCivicAddressPostOfficeBox':lldpMedConfigPortLocationCivicAddressPostOfficeBox,'lldpMedConfigPortLocationCivicAddressAdditional':lldpMedConfigPortLocationCivicAddressAdditional,'lldpMedLocalInfoTable':lldpMedLocalInfoTable,'lldpMedLocalInfoEntry':lldpMedLocalInfoEntry,'lldpMedLocalPortId':lldpMedLocalPortId,'lldpMEDLocalCapabilities':lldpMEDLocalCapabilities,'lldpMedLocalDeviceType':lldpMedLocalDeviceType,'lldpMedLocalApplicationType':lldpMedLocalApplicationType,'lldpMedLocalUnknownPolicy':lldpMedLocalUnknownPolicy,'lldpMedLocalAppTagged':lldpMedLocalAppTagged,'lldpMedLocalAppVLANID':lldpMedLocalAppVLANID,'lldpMedLocalAppLayer2Priority':lldpMedLocalAppLayer2Priority,'lldpMedLocalAppDSCP':lldpMedLocalAppDSCP,'lldpMedLocalLocationDataFormat':lldpMedLocalLocationDataFormat,'lldpMedLocalLocationID':lldpMedLocalLocationID,'lldpMedLocalPowerType':lldpMedLocalPowerType,'lldpMedLocalPowerSource':lldpMedLocalPowerSource,'lldpMedLocalPowerPriority':lldpMedLocalPowerPriority,'lldpMedLocalPowerValue':lldpMedLocalPowerValue,'lldpMedLocalInventoryHardwareRevision':lldpMedLocalInventoryHardwareRevision,'lldpMedLocalInventoryFirmwareRevision':lldpMedLocalInventoryFirmwareRevision,'lldpMedLocalInventorySoftwareRevision':lldpMedLocalInventorySoftwareRevision,'lldpMedLocalInventorySerialNumber':lldpMedLocalInventorySerialNumber,'lldpMedLocalInventoryManufacturerName':lldpMedLocalInventoryManufacturerName,'lldpMedLocalInventoryModelName':lldpMedLocalInventoryModelName,'lldpMedLocalInventoryAssetID':lldpMedLocalInventoryAssetID,'lldpMedNeighborInfo':lldpMedNeighborInfo,'lldpMedNeighborInfoTable':lldpMedNeighborInfoTable,'lldpMedNeighborInfoEntry':lldpMedNeighborInfoEntry,'lldpMedNeighborPortId':lldpMedNeighborPortId,_K:lldpMedNeighborPortIndexId,'lldpMEDNeighborCapabilities':lldpMEDNeighborCapabilities,'lldpMedNeighborDeviceType':lldpMedNeighborDeviceType,'lldpMedNeighborLocationDataFormat':lldpMedNeighborLocationDataFormat,'lldpMedNeighborLocationID':lldpMedNeighborLocationID,'lldpMedNeighborPowerType':lldpMedNeighborPowerType,'lldpMedNeighborPowerSource':lldpMedNeighborPowerSource,'lldpMedNeighborPowerPriority':lldpMedNeighborPowerPriority,'lldpMedNeighborPowerValue':lldpMedNeighborPowerValue,'lldpMedNeighborInventoryHardwareRevision':lldpMedNeighborInventoryHardwareRevision,'lldpMedNeighborInventoryFirmwareRevision':lldpMedNeighborInventoryFirmwareRevision,'lldpMedNeighborInventorySoftwareRevision':lldpMedNeighborInventorySoftwareRevision,'lldpMedNeighborInventorySerialNumber':lldpMedNeighborInventorySerialNumber,'lldpMedNeighborInventoryManufacturerName':lldpMedNeighborInventoryManufacturerName,'lldpMedNeighborInventoryModelName':lldpMedNeighborInventoryModelName,'lldpMedNeighborInventoryAssetID':lldpMedNeighborInventoryAssetID,'lldpMedNeighborMediaPolicyInfoTable':lldpMedNeighborMediaPolicyInfoTable,'lldpMedNeighborMediaPolicyInfoEntry':lldpMedNeighborMediaPolicyInfoEntry,'lldpMedNeighborPort':lldpMedNeighborPort,_L:lldpMedNeighborPortIndex,_M:lldpMedNeighborMediaPolicyIndex,'lldpMedNeighborApplicationType':lldpMedNeighborApplicationType,'lldpMedNeighborUnknownPolicy':lldpMedNeighborUnknownPolicy,'lldpMedNeighborAppTagged':lldpMedNeighborAppTagged,'lldpMedNeighborAppVLANID':lldpMedNeighborAppVLANID,'lldpMedNeighborAppLayer2Priority':lldpMedNeighborAppLayer2Priority,'lldpMedNeighborAppDSCP':lldpMedNeighborAppDSCP})