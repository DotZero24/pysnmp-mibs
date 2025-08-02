_k='receivedPoeControlPortIndex'
_j='critical'
_i='pdPseLocal'
_h='pdLocalBackup'
_g='pdPsePrimary'
_f='receivedPoeInfosPortIndex'
_e='receivedInventoryInfosPortIndex'
_d='receivedPoliciesPortIndex'
_c='receivedCivicLocationsPortIndex'
_b='receivedCoordinatesPortIndex'
_a='station'
_Z='docsis'
_Y='telephone'
_X='router'
_W='bridge'
_V='repeater'
_U='interfaceName'
_T='networkAddress'
_S='macAddress'
_R='portComponent'
_Q='interfaceAlias'
_P='receivedOverviewPortIndex'
_O='localCivicLocationIndex'
_N='localCoordinatesIndex'
_M='configIndex'
_L='Bits'
_K='true'
_J='false'
_I='enabled'
_H='disabled'
_G='unknown'
_F='not-accessible'
_E='G6-LLDP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Lldp_ObjectIdentity=ObjectIdentity
lldp=_Lldp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,43))
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,43,1))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1))
configEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_ConfigIndex_Type.__name__=_C
_ConfigIndex_Object=MibTableColumn
configIndex=_ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,1),_ConfigIndex_Type())
configIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:configIndex.setStatus(_A)
class _ConfigEnableLldp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigEnableLldp_Type.__name__=_C
_ConfigEnableLldp_Object=MibTableColumn
configEnableLldp=_ConfigEnableLldp_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,2),_ConfigEnableLldp_Type())
configEnableLldp.setMaxAccess(_D)
if mibBuilder.loadTexts:configEnableLldp.setStatus(_A)
class _ConfigEnableCdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigEnableCdp_Type.__name__=_C
_ConfigEnableCdp_Object=MibTableColumn
configEnableCdp=_ConfigEnableCdp_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,3),_ConfigEnableCdp_Type())
configEnableCdp.setMaxAccess(_D)
if mibBuilder.loadTexts:configEnableCdp.setStatus(_A)
_ConfigLldpEnabledPorts_Type=Integer32
_ConfigLldpEnabledPorts_Object=MibTableColumn
configLldpEnabledPorts=_ConfigLldpEnabledPorts_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,4),_ConfigLldpEnabledPorts_Type())
configLldpEnabledPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:configLldpEnabledPorts.setStatus(_A)
class _ConfigReceiveOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigReceiveOnly_Type.__name__=_C
_ConfigReceiveOnly_Object=MibTableColumn
configReceiveOnly=_ConfigReceiveOnly_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,5),_ConfigReceiveOnly_Type())
configReceiveOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:configReceiveOnly.setStatus(_A)
class _ConfigForwardToLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigForwardToLink_Type.__name__=_C
_ConfigForwardToLink_Object=MibTableColumn
configForwardToLink=_ConfigForwardToLink_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,6),_ConfigForwardToLink_Type())
configForwardToLink.setMaxAccess(_D)
if mibBuilder.loadTexts:configForwardToLink.setStatus(_A)
class _ConfigAdvertizedMedClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('disableMed',0),('genericEndpoint',1),('mediaEndpoint',2),('communicationEndpoint',3),('networkDevice',4)))
_ConfigAdvertizedMedClass_Type.__name__=_C
_ConfigAdvertizedMedClass_Object=MibTableColumn
configAdvertizedMedClass=_ConfigAdvertizedMedClass_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,7),_ConfigAdvertizedMedClass_Type())
configAdvertizedMedClass.setMaxAccess(_D)
if mibBuilder.loadTexts:configAdvertizedMedClass.setStatus(_A)
class _ConfigDisableMedInventory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigDisableMedInventory_Type.__name__=_C
_ConfigDisableMedInventory_Object=MibTableColumn
configDisableMedInventory=_ConfigDisableMedInventory_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,8),_ConfigDisableMedInventory_Type())
configDisableMedInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:configDisableMedInventory.setStatus(_A)
class _ConfigDisableVoiceVlanTlv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigDisableVoiceVlanTlv_Type.__name__=_C
_ConfigDisableVoiceVlanTlv_Object=MibTableColumn
configDisableVoiceVlanTlv=_ConfigDisableVoiceVlanTlv_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,9),_ConfigDisableVoiceVlanTlv_Type())
configDisableVoiceVlanTlv.setMaxAccess(_D)
if mibBuilder.loadTexts:configDisableVoiceVlanTlv.setStatus(_A)
class _ConfigCdpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('v1AndV2',0),('v1',1),('v2',2)))
_ConfigCdpVersion_Type.__name__=_C
_ConfigCdpVersion_Object=MibTableColumn
configCdpVersion=_ConfigCdpVersion_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,10),_ConfigCdpVersion_Type())
configCdpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:configCdpVersion.setStatus(_A)
class _ConfigVoiceVlanPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigVoiceVlanPrio_Type.__name__=_C
_ConfigVoiceVlanPrio_Object=MibTableColumn
configVoiceVlanPrio=_ConfigVoiceVlanPrio_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,11),_ConfigVoiceVlanPrio_Type())
configVoiceVlanPrio.setMaxAccess(_D)
if mibBuilder.loadTexts:configVoiceVlanPrio.setStatus(_A)
class _ConfigVoiceVlanSignalPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigVoiceVlanSignalPrio_Type.__name__=_C
_ConfigVoiceVlanSignalPrio_Object=MibTableColumn
configVoiceVlanSignalPrio=_ConfigVoiceVlanSignalPrio_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,12),_ConfigVoiceVlanSignalPrio_Type())
configVoiceVlanSignalPrio.setMaxAccess(_D)
if mibBuilder.loadTexts:configVoiceVlanSignalPrio.setStatus(_A)
class _ConfigVoiceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigVoiceDscp_Type.__name__=_C
_ConfigVoiceDscp_Object=MibTableColumn
configVoiceDscp=_ConfigVoiceDscp_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,13),_ConfigVoiceDscp_Type())
configVoiceDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:configVoiceDscp.setStatus(_A)
class _ConfigSignalingDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigSignalingDscp_Type.__name__=_C
_ConfigSignalingDscp_Object=MibTableColumn
configSignalingDscp=_ConfigSignalingDscp_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,14),_ConfigSignalingDscp_Type())
configSignalingDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:configSignalingDscp.setStatus(_A)
class _ConfigTimeToLive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigTimeToLive_Type.__name__=_C
_ConfigTimeToLive_Object=MibTableColumn
configTimeToLive=_ConfigTimeToLive_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,15),_ConfigTimeToLive_Type())
configTimeToLive.setMaxAccess(_D)
if mibBuilder.loadTexts:configTimeToLive.setStatus(_A)
class _ConfigTxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigTxDelay_Type.__name__=_C
_ConfigTxDelay_Object=MibTableColumn
configTxDelay=_ConfigTxDelay_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,16),_ConfigTxDelay_Type())
configTxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:configTxDelay.setStatus(_A)
class _ConfigMsgTxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigMsgTxInterval_Type.__name__=_C
_ConfigMsgTxInterval_Object=MibTableColumn
configMsgTxInterval=_ConfigMsgTxInterval_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,17),_ConfigMsgTxInterval_Type())
configMsgTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:configMsgTxInterval.setStatus(_A)
class _ConfigForceLldpTransmission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigForceLldpTransmission_Type.__name__=_C
_ConfigForceLldpTransmission_Object=MibTableColumn
configForceLldpTransmission=_ConfigForceLldpTransmission_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,18),_ConfigForceLldpTransmission_Type())
configForceLldpTransmission.setMaxAccess(_D)
if mibBuilder.loadTexts:configForceLldpTransmission.setStatus(_A)
class _ConfigLldpResponsePreferred_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ConfigLldpResponsePreferred_Type.__name__=_C
_ConfigLldpResponsePreferred_Object=MibTableColumn
configLldpResponsePreferred=_ConfigLldpResponsePreferred_Object((1,3,6,1,4,1,3181,10,6,2,43,1,1,19),_ConfigLldpResponsePreferred_Type())
configLldpResponsePreferred.setMaxAccess(_D)
if mibBuilder.loadTexts:configLldpResponsePreferred.setStatus(_A)
_LocalCoordinatesTable_Object=MibTable
localCoordinatesTable=_LocalCoordinatesTable_Object((1,3,6,1,4,1,3181,10,6,2,43,2))
if mibBuilder.loadTexts:localCoordinatesTable.setStatus(_A)
_LocalCoordinatesEntry_Object=MibTableRow
localCoordinatesEntry=_LocalCoordinatesEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1))
localCoordinatesEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:localCoordinatesEntry.setStatus(_A)
class _LocalCoordinatesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_LocalCoordinatesIndex_Type.__name__=_C
_LocalCoordinatesIndex_Object=MibTableColumn
localCoordinatesIndex=_LocalCoordinatesIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,1),_LocalCoordinatesIndex_Type())
localCoordinatesIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:localCoordinatesIndex.setStatus(_A)
_LocalCoordinatesLatitude_Type=DisplayString
_LocalCoordinatesLatitude_Object=MibTableColumn
localCoordinatesLatitude=_LocalCoordinatesLatitude_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,2),_LocalCoordinatesLatitude_Type())
localCoordinatesLatitude.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesLatitude.setStatus(_A)
class _LocalCoordinatesLatResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LocalCoordinatesLatResolution_Type.__name__=_C
_LocalCoordinatesLatResolution_Object=MibTableColumn
localCoordinatesLatResolution=_LocalCoordinatesLatResolution_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,3),_LocalCoordinatesLatResolution_Type())
localCoordinatesLatResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesLatResolution.setStatus(_A)
_LocalCoordinatesLongitude_Type=DisplayString
_LocalCoordinatesLongitude_Object=MibTableColumn
localCoordinatesLongitude=_LocalCoordinatesLongitude_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,4),_LocalCoordinatesLongitude_Type())
localCoordinatesLongitude.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesLongitude.setStatus(_A)
class _LocalCoordinatesLongResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LocalCoordinatesLongResolution_Type.__name__=_C
_LocalCoordinatesLongResolution_Object=MibTableColumn
localCoordinatesLongResolution=_LocalCoordinatesLongResolution_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,5),_LocalCoordinatesLongResolution_Type())
localCoordinatesLongResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesLongResolution.setStatus(_A)
_LocalCoordinatesAltitude_Type=DisplayString
_LocalCoordinatesAltitude_Object=MibTableColumn
localCoordinatesAltitude=_LocalCoordinatesAltitude_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,6),_LocalCoordinatesAltitude_Type())
localCoordinatesAltitude.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesAltitude.setStatus(_A)
class _LocalCoordinatesAltResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LocalCoordinatesAltResolution_Type.__name__=_C
_LocalCoordinatesAltResolution_Object=MibTableColumn
localCoordinatesAltResolution=_LocalCoordinatesAltResolution_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,7),_LocalCoordinatesAltResolution_Type())
localCoordinatesAltResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesAltResolution.setStatus(_A)
class _LocalCoordinatesAltType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('meter',0),('floor',1)))
_LocalCoordinatesAltType_Type.__name__=_C
_LocalCoordinatesAltType_Object=MibTableColumn
localCoordinatesAltType=_LocalCoordinatesAltType_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,8),_LocalCoordinatesAltType_Type())
localCoordinatesAltType.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesAltType.setStatus(_A)
_LocalCoordinatesDatum_Type=DisplayString
_LocalCoordinatesDatum_Object=MibTableColumn
localCoordinatesDatum=_LocalCoordinatesDatum_Object((1,3,6,1,4,1,3181,10,6,2,43,2,1,9),_LocalCoordinatesDatum_Type())
localCoordinatesDatum.setMaxAccess(_D)
if mibBuilder.loadTexts:localCoordinatesDatum.setStatus(_A)
_LocalCivicLocationTable_Object=MibTable
localCivicLocationTable=_LocalCivicLocationTable_Object((1,3,6,1,4,1,3181,10,6,2,43,3))
if mibBuilder.loadTexts:localCivicLocationTable.setStatus(_A)
_LocalCivicLocationEntry_Object=MibTableRow
localCivicLocationEntry=_LocalCivicLocationEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1))
localCivicLocationEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:localCivicLocationEntry.setStatus(_A)
class _LocalCivicLocationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_LocalCivicLocationIndex_Type.__name__=_C
_LocalCivicLocationIndex_Object=MibTableColumn
localCivicLocationIndex=_LocalCivicLocationIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,1),_LocalCivicLocationIndex_Type())
localCivicLocationIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:localCivicLocationIndex.setStatus(_A)
_LocalCivicLocationCountryCode_Type=DisplayString
_LocalCivicLocationCountryCode_Object=MibTableColumn
localCivicLocationCountryCode=_LocalCivicLocationCountryCode_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,2),_LocalCivicLocationCountryCode_Type())
localCivicLocationCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationCountryCode.setStatus(_A)
_LocalCivicLocationLanguage_Type=DisplayString
_LocalCivicLocationLanguage_Object=MibTableColumn
localCivicLocationLanguage=_LocalCivicLocationLanguage_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,3),_LocalCivicLocationLanguage_Type())
localCivicLocationLanguage.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationLanguage.setStatus(_A)
_LocalCivicLocationNationalSubdivision_Type=DisplayString
_LocalCivicLocationNationalSubdivision_Object=MibTableColumn
localCivicLocationNationalSubdivision=_LocalCivicLocationNationalSubdivision_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,4),_LocalCivicLocationNationalSubdivision_Type())
localCivicLocationNationalSubdivision.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationNationalSubdivision.setStatus(_A)
_LocalCivicLocationCounty_Type=DisplayString
_LocalCivicLocationCounty_Object=MibTableColumn
localCivicLocationCounty=_LocalCivicLocationCounty_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,5),_LocalCivicLocationCounty_Type())
localCivicLocationCounty.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationCounty.setStatus(_A)
_LocalCivicLocationTown_Type=DisplayString
_LocalCivicLocationTown_Object=MibTableColumn
localCivicLocationTown=_LocalCivicLocationTown_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,6),_LocalCivicLocationTown_Type())
localCivicLocationTown.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationTown.setStatus(_A)
_LocalCivicLocationDistrict_Type=DisplayString
_LocalCivicLocationDistrict_Object=MibTableColumn
localCivicLocationDistrict=_LocalCivicLocationDistrict_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,7),_LocalCivicLocationDistrict_Type())
localCivicLocationDistrict.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationDistrict.setStatus(_A)
_LocalCivicLocationBlock_Type=DisplayString
_LocalCivicLocationBlock_Object=MibTableColumn
localCivicLocationBlock=_LocalCivicLocationBlock_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,8),_LocalCivicLocationBlock_Type())
localCivicLocationBlock.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationBlock.setStatus(_A)
_LocalCivicLocationStreet_Type=DisplayString
_LocalCivicLocationStreet_Object=MibTableColumn
localCivicLocationStreet=_LocalCivicLocationStreet_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,9),_LocalCivicLocationStreet_Type())
localCivicLocationStreet.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationStreet.setStatus(_A)
_LocalCivicLocationLeadingStreetDirection_Type=DisplayString
_LocalCivicLocationLeadingStreetDirection_Object=MibTableColumn
localCivicLocationLeadingStreetDirection=_LocalCivicLocationLeadingStreetDirection_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,10),_LocalCivicLocationLeadingStreetDirection_Type())
localCivicLocationLeadingStreetDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationLeadingStreetDirection.setStatus(_A)
_LocalCivicLocationTrailingStreetSuffix_Type=DisplayString
_LocalCivicLocationTrailingStreetSuffix_Object=MibTableColumn
localCivicLocationTrailingStreetSuffix=_LocalCivicLocationTrailingStreetSuffix_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,11),_LocalCivicLocationTrailingStreetSuffix_Type())
localCivicLocationTrailingStreetSuffix.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationTrailingStreetSuffix.setStatus(_A)
_LocalCivicLocationStreetSuffix_Type=DisplayString
_LocalCivicLocationStreetSuffix_Object=MibTableColumn
localCivicLocationStreetSuffix=_LocalCivicLocationStreetSuffix_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,12),_LocalCivicLocationStreetSuffix_Type())
localCivicLocationStreetSuffix.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationStreetSuffix.setStatus(_A)
_LocalCivicLocationHouseNumber_Type=DisplayString
_LocalCivicLocationHouseNumber_Object=MibTableColumn
localCivicLocationHouseNumber=_LocalCivicLocationHouseNumber_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,13),_LocalCivicLocationHouseNumber_Type())
localCivicLocationHouseNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationHouseNumber.setStatus(_A)
_LocalCivicLocationHouseNumberSuffix_Type=DisplayString
_LocalCivicLocationHouseNumberSuffix_Object=MibTableColumn
localCivicLocationHouseNumberSuffix=_LocalCivicLocationHouseNumberSuffix_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,14),_LocalCivicLocationHouseNumberSuffix_Type())
localCivicLocationHouseNumberSuffix.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationHouseNumberSuffix.setStatus(_A)
_LocalCivicLocationLandmark_Type=DisplayString
_LocalCivicLocationLandmark_Object=MibTableColumn
localCivicLocationLandmark=_LocalCivicLocationLandmark_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,15),_LocalCivicLocationLandmark_Type())
localCivicLocationLandmark.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationLandmark.setStatus(_A)
_LocalCivicLocationAdditionalInfo_Type=DisplayString
_LocalCivicLocationAdditionalInfo_Object=MibTableColumn
localCivicLocationAdditionalInfo=_LocalCivicLocationAdditionalInfo_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,16),_LocalCivicLocationAdditionalInfo_Type())
localCivicLocationAdditionalInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationAdditionalInfo.setStatus(_A)
_LocalCivicLocationName_Type=DisplayString
_LocalCivicLocationName_Object=MibTableColumn
localCivicLocationName=_LocalCivicLocationName_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,17),_LocalCivicLocationName_Type())
localCivicLocationName.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationName.setStatus(_A)
_LocalCivicLocationZipCode_Type=DisplayString
_LocalCivicLocationZipCode_Object=MibTableColumn
localCivicLocationZipCode=_LocalCivicLocationZipCode_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,18),_LocalCivicLocationZipCode_Type())
localCivicLocationZipCode.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationZipCode.setStatus(_A)
_LocalCivicLocationBuilding_Type=DisplayString
_LocalCivicLocationBuilding_Object=MibTableColumn
localCivicLocationBuilding=_LocalCivicLocationBuilding_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,19),_LocalCivicLocationBuilding_Type())
localCivicLocationBuilding.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationBuilding.setStatus(_A)
_LocalCivicLocationUnit_Type=DisplayString
_LocalCivicLocationUnit_Object=MibTableColumn
localCivicLocationUnit=_LocalCivicLocationUnit_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,20),_LocalCivicLocationUnit_Type())
localCivicLocationUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationUnit.setStatus(_A)
_LocalCivicLocationFloor_Type=DisplayString
_LocalCivicLocationFloor_Object=MibTableColumn
localCivicLocationFloor=_LocalCivicLocationFloor_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,21),_LocalCivicLocationFloor_Type())
localCivicLocationFloor.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationFloor.setStatus(_A)
_LocalCivicLocationRoom_Type=DisplayString
_LocalCivicLocationRoom_Object=MibTableColumn
localCivicLocationRoom=_LocalCivicLocationRoom_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,22),_LocalCivicLocationRoom_Type())
localCivicLocationRoom.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationRoom.setStatus(_A)
_LocalCivicLocationPlaceType_Type=DisplayString
_LocalCivicLocationPlaceType_Object=MibTableColumn
localCivicLocationPlaceType=_LocalCivicLocationPlaceType_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,23),_LocalCivicLocationPlaceType_Type())
localCivicLocationPlaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationPlaceType.setStatus(_A)
_LocalCivicLocationScript_Type=DisplayString
_LocalCivicLocationScript_Object=MibTableColumn
localCivicLocationScript=_LocalCivicLocationScript_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,24),_LocalCivicLocationScript_Type())
localCivicLocationScript.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationScript.setStatus(_A)
_LocalCivicLocationElinNumber_Type=DisplayString
_LocalCivicLocationElinNumber_Object=MibTableColumn
localCivicLocationElinNumber=_LocalCivicLocationElinNumber_Object((1,3,6,1,4,1,3181,10,6,2,43,3,1,25),_LocalCivicLocationElinNumber_Type())
localCivicLocationElinNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:localCivicLocationElinNumber.setStatus(_A)
_ReceivedOverviewTable_Object=MibTable
receivedOverviewTable=_ReceivedOverviewTable_Object((1,3,6,1,4,1,3181,10,6,2,43,100))
if mibBuilder.loadTexts:receivedOverviewTable.setStatus(_A)
_ReceivedOverviewEntry_Object=MibTableRow
receivedOverviewEntry=_ReceivedOverviewEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1))
receivedOverviewEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:receivedOverviewEntry.setStatus(_A)
class _ReceivedOverviewPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedOverviewPortIndex_Type.__name__=_C
_ReceivedOverviewPortIndex_Object=MibTableColumn
receivedOverviewPortIndex=_ReceivedOverviewPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,1),_ReceivedOverviewPortIndex_Type())
receivedOverviewPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedOverviewPortIndex.setStatus(_A)
_ReceivedOverviewSysName_Type=DisplayString
_ReceivedOverviewSysName_Object=MibTableColumn
receivedOverviewSysName=_ReceivedOverviewSysName_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,2),_ReceivedOverviewSysName_Type())
receivedOverviewSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewSysName.setStatus(_A)
_ReceivedOverviewSysDesc_Type=DisplayString
_ReceivedOverviewSysDesc_Object=MibTableColumn
receivedOverviewSysDesc=_ReceivedOverviewSysDesc_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,3),_ReceivedOverviewSysDesc_Type())
receivedOverviewSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewSysDesc.setStatus(_A)
class _ReceivedOverviewChassisIdSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),('chassisComponent',1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6),('local',7)))
_ReceivedOverviewChassisIdSubtype_Type.__name__=_C
_ReceivedOverviewChassisIdSubtype_Object=MibTableColumn
receivedOverviewChassisIdSubtype=_ReceivedOverviewChassisIdSubtype_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,4),_ReceivedOverviewChassisIdSubtype_Type())
receivedOverviewChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewChassisIdSubtype.setStatus(_A)
_ReceivedOverviewChassisId_Type=DisplayString
_ReceivedOverviewChassisId_Object=MibTableColumn
receivedOverviewChassisId=_ReceivedOverviewChassisId_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,5),_ReceivedOverviewChassisId_Type())
receivedOverviewChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewChassisId.setStatus(_A)
_ReceivedOverviewMgmtIp_Type=DisplayString
_ReceivedOverviewMgmtIp_Object=MibTableColumn
receivedOverviewMgmtIp=_ReceivedOverviewMgmtIp_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,6),_ReceivedOverviewMgmtIp_Type())
receivedOverviewMgmtIp.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewMgmtIp.setStatus(_A)
_ReceivedOverviewMgmtOid_Type=DisplayString
_ReceivedOverviewMgmtOid_Object=MibTableColumn
receivedOverviewMgmtOid=_ReceivedOverviewMgmtOid_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,7),_ReceivedOverviewMgmtOid_Type())
receivedOverviewMgmtOid.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewMgmtOid.setStatus(_A)
class _ReceivedOverviewCapabilities_Type(Bits):namedValues=NamedValues(*(('other',0),(_V,1),(_W,2),('wlan',3),(_X,4),(_Y,5),(_Z,6),(_a,7)))
_ReceivedOverviewCapabilities_Type.__name__=_L
_ReceivedOverviewCapabilities_Object=MibTableColumn
receivedOverviewCapabilities=_ReceivedOverviewCapabilities_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,8),_ReceivedOverviewCapabilities_Type())
receivedOverviewCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewCapabilities.setStatus(_A)
class _ReceivedOverviewCapabilitiesEnabled_Type(Bits):namedValues=NamedValues(*(('other',0),(_V,1),(_W,2),('wlan',3),(_X,4),(_Y,5),(_Z,6),(_a,7)))
_ReceivedOverviewCapabilitiesEnabled_Type.__name__=_L
_ReceivedOverviewCapabilitiesEnabled_Object=MibTableColumn
receivedOverviewCapabilitiesEnabled=_ReceivedOverviewCapabilitiesEnabled_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,9),_ReceivedOverviewCapabilitiesEnabled_Type())
receivedOverviewCapabilitiesEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewCapabilitiesEnabled.setStatus(_A)
class _ReceivedOverviewMedCapabilities_Type(Bits):namedValues=NamedValues(*(('capability',0),('policy',1),('location',2),('mdiPse',3),('mdiPd',4),('inventory',5)))
_ReceivedOverviewMedCapabilities_Type.__name__=_L
_ReceivedOverviewMedCapabilities_Object=MibTableColumn
receivedOverviewMedCapabilities=_ReceivedOverviewMedCapabilities_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,10),_ReceivedOverviewMedCapabilities_Type())
receivedOverviewMedCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewMedCapabilities.setStatus(_A)
class _ReceivedOverviewPortIdSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),('agentCircuitId',6),('local',7)))
_ReceivedOverviewPortIdSubtype_Type.__name__=_C
_ReceivedOverviewPortIdSubtype_Object=MibTableColumn
receivedOverviewPortIdSubtype=_ReceivedOverviewPortIdSubtype_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,11),_ReceivedOverviewPortIdSubtype_Type())
receivedOverviewPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewPortIdSubtype.setStatus(_A)
_ReceivedOverviewPortIdentification_Type=DisplayString
_ReceivedOverviewPortIdentification_Object=MibTableColumn
receivedOverviewPortIdentification=_ReceivedOverviewPortIdentification_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,12),_ReceivedOverviewPortIdentification_Type())
receivedOverviewPortIdentification.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewPortIdentification.setStatus(_A)
_ReceivedOverviewPortDescription_Type=DisplayString
_ReceivedOverviewPortDescription_Object=MibTableColumn
receivedOverviewPortDescription=_ReceivedOverviewPortDescription_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,13),_ReceivedOverviewPortDescription_Type())
receivedOverviewPortDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewPortDescription.setStatus(_A)
class _ReceivedOverviewPortVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ReceivedOverviewPortVlan_Type.__name__=_C
_ReceivedOverviewPortVlan_Object=MibTableColumn
receivedOverviewPortVlan=_ReceivedOverviewPortVlan_Object((1,3,6,1,4,1,3181,10,6,2,43,100,1,14),_ReceivedOverviewPortVlan_Type())
receivedOverviewPortVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedOverviewPortVlan.setStatus(_A)
_ReceivedCoordinatesTable_Object=MibTable
receivedCoordinatesTable=_ReceivedCoordinatesTable_Object((1,3,6,1,4,1,3181,10,6,2,43,101))
if mibBuilder.loadTexts:receivedCoordinatesTable.setStatus(_A)
_ReceivedCoordinatesEntry_Object=MibTableRow
receivedCoordinatesEntry=_ReceivedCoordinatesEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1))
receivedCoordinatesEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:receivedCoordinatesEntry.setStatus(_A)
class _ReceivedCoordinatesPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedCoordinatesPortIndex_Type.__name__=_C
_ReceivedCoordinatesPortIndex_Object=MibTableColumn
receivedCoordinatesPortIndex=_ReceivedCoordinatesPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,1),_ReceivedCoordinatesPortIndex_Type())
receivedCoordinatesPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedCoordinatesPortIndex.setStatus(_A)
_ReceivedCoordinatesLatitude_Type=DisplayString
_ReceivedCoordinatesLatitude_Object=MibTableColumn
receivedCoordinatesLatitude=_ReceivedCoordinatesLatitude_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,2),_ReceivedCoordinatesLatitude_Type())
receivedCoordinatesLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesLatitude.setStatus(_A)
class _ReceivedCoordinatesLatResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedCoordinatesLatResolution_Type.__name__=_C
_ReceivedCoordinatesLatResolution_Object=MibTableColumn
receivedCoordinatesLatResolution=_ReceivedCoordinatesLatResolution_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,3),_ReceivedCoordinatesLatResolution_Type())
receivedCoordinatesLatResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesLatResolution.setStatus(_A)
_ReceivedCoordinatesLongitude_Type=DisplayString
_ReceivedCoordinatesLongitude_Object=MibTableColumn
receivedCoordinatesLongitude=_ReceivedCoordinatesLongitude_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,4),_ReceivedCoordinatesLongitude_Type())
receivedCoordinatesLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesLongitude.setStatus(_A)
class _ReceivedCoordinatesLongResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedCoordinatesLongResolution_Type.__name__=_C
_ReceivedCoordinatesLongResolution_Object=MibTableColumn
receivedCoordinatesLongResolution=_ReceivedCoordinatesLongResolution_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,5),_ReceivedCoordinatesLongResolution_Type())
receivedCoordinatesLongResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesLongResolution.setStatus(_A)
_ReceivedCoordinatesAltitude_Type=DisplayString
_ReceivedCoordinatesAltitude_Object=MibTableColumn
receivedCoordinatesAltitude=_ReceivedCoordinatesAltitude_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,6),_ReceivedCoordinatesAltitude_Type())
receivedCoordinatesAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesAltitude.setStatus(_A)
class _ReceivedCoordinatesAltResolution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedCoordinatesAltResolution_Type.__name__=_C
_ReceivedCoordinatesAltResolution_Object=MibTableColumn
receivedCoordinatesAltResolution=_ReceivedCoordinatesAltResolution_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,7),_ReceivedCoordinatesAltResolution_Type())
receivedCoordinatesAltResolution.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesAltResolution.setStatus(_A)
class _ReceivedCoordinatesAltUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('meter',0),('floor',1)))
_ReceivedCoordinatesAltUnit_Type.__name__=_C
_ReceivedCoordinatesAltUnit_Object=MibTableColumn
receivedCoordinatesAltUnit=_ReceivedCoordinatesAltUnit_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,8),_ReceivedCoordinatesAltUnit_Type())
receivedCoordinatesAltUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesAltUnit.setStatus(_A)
_ReceivedCoordinatesDatum_Type=DisplayString
_ReceivedCoordinatesDatum_Object=MibTableColumn
receivedCoordinatesDatum=_ReceivedCoordinatesDatum_Object((1,3,6,1,4,1,3181,10,6,2,43,101,1,9),_ReceivedCoordinatesDatum_Type())
receivedCoordinatesDatum.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCoordinatesDatum.setStatus(_A)
_ReceivedCivicLocationsTable_Object=MibTable
receivedCivicLocationsTable=_ReceivedCivicLocationsTable_Object((1,3,6,1,4,1,3181,10,6,2,43,102))
if mibBuilder.loadTexts:receivedCivicLocationsTable.setStatus(_A)
_ReceivedCivicLocationsEntry_Object=MibTableRow
receivedCivicLocationsEntry=_ReceivedCivicLocationsEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1))
receivedCivicLocationsEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:receivedCivicLocationsEntry.setStatus(_A)
class _ReceivedCivicLocationsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedCivicLocationsPortIndex_Type.__name__=_C
_ReceivedCivicLocationsPortIndex_Object=MibTableColumn
receivedCivicLocationsPortIndex=_ReceivedCivicLocationsPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,1),_ReceivedCivicLocationsPortIndex_Type())
receivedCivicLocationsPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedCivicLocationsPortIndex.setStatus(_A)
_ReceivedCivicLocationsCountryCode_Type=DisplayString
_ReceivedCivicLocationsCountryCode_Object=MibTableColumn
receivedCivicLocationsCountryCode=_ReceivedCivicLocationsCountryCode_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,2),_ReceivedCivicLocationsCountryCode_Type())
receivedCivicLocationsCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsCountryCode.setStatus(_A)
_ReceivedCivicLocationsLanguage_Type=DisplayString
_ReceivedCivicLocationsLanguage_Object=MibTableColumn
receivedCivicLocationsLanguage=_ReceivedCivicLocationsLanguage_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,3),_ReceivedCivicLocationsLanguage_Type())
receivedCivicLocationsLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsLanguage.setStatus(_A)
_ReceivedCivicLocationsNationalSubdivision_Type=DisplayString
_ReceivedCivicLocationsNationalSubdivision_Object=MibTableColumn
receivedCivicLocationsNationalSubdivision=_ReceivedCivicLocationsNationalSubdivision_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,4),_ReceivedCivicLocationsNationalSubdivision_Type())
receivedCivicLocationsNationalSubdivision.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsNationalSubdivision.setStatus(_A)
_ReceivedCivicLocationsCounty_Type=DisplayString
_ReceivedCivicLocationsCounty_Object=MibTableColumn
receivedCivicLocationsCounty=_ReceivedCivicLocationsCounty_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,5),_ReceivedCivicLocationsCounty_Type())
receivedCivicLocationsCounty.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsCounty.setStatus(_A)
_ReceivedCivicLocationsTown_Type=DisplayString
_ReceivedCivicLocationsTown_Object=MibTableColumn
receivedCivicLocationsTown=_ReceivedCivicLocationsTown_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,6),_ReceivedCivicLocationsTown_Type())
receivedCivicLocationsTown.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsTown.setStatus(_A)
_ReceivedCivicLocationsDistrict_Type=DisplayString
_ReceivedCivicLocationsDistrict_Object=MibTableColumn
receivedCivicLocationsDistrict=_ReceivedCivicLocationsDistrict_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,7),_ReceivedCivicLocationsDistrict_Type())
receivedCivicLocationsDistrict.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsDistrict.setStatus(_A)
_ReceivedCivicLocationsBlock_Type=DisplayString
_ReceivedCivicLocationsBlock_Object=MibTableColumn
receivedCivicLocationsBlock=_ReceivedCivicLocationsBlock_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,8),_ReceivedCivicLocationsBlock_Type())
receivedCivicLocationsBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsBlock.setStatus(_A)
_ReceivedCivicLocationsStreet_Type=DisplayString
_ReceivedCivicLocationsStreet_Object=MibTableColumn
receivedCivicLocationsStreet=_ReceivedCivicLocationsStreet_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,9),_ReceivedCivicLocationsStreet_Type())
receivedCivicLocationsStreet.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsStreet.setStatus(_A)
_ReceivedCivicLocationsLeadingStreetDirection_Type=DisplayString
_ReceivedCivicLocationsLeadingStreetDirection_Object=MibTableColumn
receivedCivicLocationsLeadingStreetDirection=_ReceivedCivicLocationsLeadingStreetDirection_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,10),_ReceivedCivicLocationsLeadingStreetDirection_Type())
receivedCivicLocationsLeadingStreetDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsLeadingStreetDirection.setStatus(_A)
_ReceivedCivicLocationsTrailingStreetSuffix_Type=DisplayString
_ReceivedCivicLocationsTrailingStreetSuffix_Object=MibTableColumn
receivedCivicLocationsTrailingStreetSuffix=_ReceivedCivicLocationsTrailingStreetSuffix_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,11),_ReceivedCivicLocationsTrailingStreetSuffix_Type())
receivedCivicLocationsTrailingStreetSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsTrailingStreetSuffix.setStatus(_A)
_ReceivedCivicLocationsStreetSuffix_Type=DisplayString
_ReceivedCivicLocationsStreetSuffix_Object=MibTableColumn
receivedCivicLocationsStreetSuffix=_ReceivedCivicLocationsStreetSuffix_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,12),_ReceivedCivicLocationsStreetSuffix_Type())
receivedCivicLocationsStreetSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsStreetSuffix.setStatus(_A)
_ReceivedCivicLocationsHouseNumber_Type=DisplayString
_ReceivedCivicLocationsHouseNumber_Object=MibTableColumn
receivedCivicLocationsHouseNumber=_ReceivedCivicLocationsHouseNumber_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,13),_ReceivedCivicLocationsHouseNumber_Type())
receivedCivicLocationsHouseNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsHouseNumber.setStatus(_A)
_ReceivedCivicLocationsHouseNumberSuffix_Type=DisplayString
_ReceivedCivicLocationsHouseNumberSuffix_Object=MibTableColumn
receivedCivicLocationsHouseNumberSuffix=_ReceivedCivicLocationsHouseNumberSuffix_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,14),_ReceivedCivicLocationsHouseNumberSuffix_Type())
receivedCivicLocationsHouseNumberSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsHouseNumberSuffix.setStatus(_A)
_ReceivedCivicLocationsLandmark_Type=DisplayString
_ReceivedCivicLocationsLandmark_Object=MibTableColumn
receivedCivicLocationsLandmark=_ReceivedCivicLocationsLandmark_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,15),_ReceivedCivicLocationsLandmark_Type())
receivedCivicLocationsLandmark.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsLandmark.setStatus(_A)
_ReceivedCivicLocationsAdditionalInfo_Type=DisplayString
_ReceivedCivicLocationsAdditionalInfo_Object=MibTableColumn
receivedCivicLocationsAdditionalInfo=_ReceivedCivicLocationsAdditionalInfo_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,16),_ReceivedCivicLocationsAdditionalInfo_Type())
receivedCivicLocationsAdditionalInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsAdditionalInfo.setStatus(_A)
_ReceivedCivicLocationsName_Type=DisplayString
_ReceivedCivicLocationsName_Object=MibTableColumn
receivedCivicLocationsName=_ReceivedCivicLocationsName_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,17),_ReceivedCivicLocationsName_Type())
receivedCivicLocationsName.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsName.setStatus(_A)
_ReceivedCivicLocationsZipCode_Type=DisplayString
_ReceivedCivicLocationsZipCode_Object=MibTableColumn
receivedCivicLocationsZipCode=_ReceivedCivicLocationsZipCode_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,18),_ReceivedCivicLocationsZipCode_Type())
receivedCivicLocationsZipCode.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsZipCode.setStatus(_A)
_ReceivedCivicLocationsBuilding_Type=DisplayString
_ReceivedCivicLocationsBuilding_Object=MibTableColumn
receivedCivicLocationsBuilding=_ReceivedCivicLocationsBuilding_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,19),_ReceivedCivicLocationsBuilding_Type())
receivedCivicLocationsBuilding.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsBuilding.setStatus(_A)
_ReceivedCivicLocationsUnit_Type=DisplayString
_ReceivedCivicLocationsUnit_Object=MibTableColumn
receivedCivicLocationsUnit=_ReceivedCivicLocationsUnit_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,20),_ReceivedCivicLocationsUnit_Type())
receivedCivicLocationsUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsUnit.setStatus(_A)
_ReceivedCivicLocationsFloor_Type=DisplayString
_ReceivedCivicLocationsFloor_Object=MibTableColumn
receivedCivicLocationsFloor=_ReceivedCivicLocationsFloor_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,21),_ReceivedCivicLocationsFloor_Type())
receivedCivicLocationsFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsFloor.setStatus(_A)
_ReceivedCivicLocationsRoom_Type=DisplayString
_ReceivedCivicLocationsRoom_Object=MibTableColumn
receivedCivicLocationsRoom=_ReceivedCivicLocationsRoom_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,22),_ReceivedCivicLocationsRoom_Type())
receivedCivicLocationsRoom.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsRoom.setStatus(_A)
_ReceivedCivicLocationsPlaceType_Type=DisplayString
_ReceivedCivicLocationsPlaceType_Object=MibTableColumn
receivedCivicLocationsPlaceType=_ReceivedCivicLocationsPlaceType_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,23),_ReceivedCivicLocationsPlaceType_Type())
receivedCivicLocationsPlaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsPlaceType.setStatus(_A)
_ReceivedCivicLocationsScript_Type=DisplayString
_ReceivedCivicLocationsScript_Object=MibTableColumn
receivedCivicLocationsScript=_ReceivedCivicLocationsScript_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,24),_ReceivedCivicLocationsScript_Type())
receivedCivicLocationsScript.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsScript.setStatus(_A)
_ReceivedCivicLocationsElinNumber_Type=DisplayString
_ReceivedCivicLocationsElinNumber_Object=MibTableColumn
receivedCivicLocationsElinNumber=_ReceivedCivicLocationsElinNumber_Object((1,3,6,1,4,1,3181,10,6,2,43,102,1,25),_ReceivedCivicLocationsElinNumber_Type())
receivedCivicLocationsElinNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedCivicLocationsElinNumber.setStatus(_A)
_ReceivedPoliciesTable_Object=MibTable
receivedPoliciesTable=_ReceivedPoliciesTable_Object((1,3,6,1,4,1,3181,10,6,2,43,103))
if mibBuilder.loadTexts:receivedPoliciesTable.setStatus(_A)
_ReceivedPoliciesEntry_Object=MibTableRow
receivedPoliciesEntry=_ReceivedPoliciesEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1))
receivedPoliciesEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:receivedPoliciesEntry.setStatus(_A)
class _ReceivedPoliciesPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedPoliciesPortIndex_Type.__name__=_C
_ReceivedPoliciesPortIndex_Object=MibTableColumn
receivedPoliciesPortIndex=_ReceivedPoliciesPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,1),_ReceivedPoliciesPortIndex_Type())
receivedPoliciesPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedPoliciesPortIndex.setStatus(_A)
class _ReceivedPoliciesApplicationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),('voice',1),('voiceSignaling',2),('guestVoice',3),('guestVoiceSignaling',4),('softphoneVoice',5),('videoConferencing',6),('streamingVideo',7),('videoSignaling',8)))
_ReceivedPoliciesApplicationType_Type.__name__=_C
_ReceivedPoliciesApplicationType_Object=MibTableColumn
receivedPoliciesApplicationType=_ReceivedPoliciesApplicationType_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,2),_ReceivedPoliciesApplicationType_Type())
receivedPoliciesApplicationType.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoliciesApplicationType.setStatus(_A)
class _ReceivedPoliciesPolicyDefined_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ReceivedPoliciesPolicyDefined_Type.__name__=_C
_ReceivedPoliciesPolicyDefined_Object=MibTableColumn
receivedPoliciesPolicyDefined=_ReceivedPoliciesPolicyDefined_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,3),_ReceivedPoliciesPolicyDefined_Type())
receivedPoliciesPolicyDefined.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoliciesPolicyDefined.setStatus(_A)
class _ReceivedPoliciesTaggedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ReceivedPoliciesTaggedVlan_Type.__name__=_C
_ReceivedPoliciesTaggedVlan_Object=MibTableColumn
receivedPoliciesTaggedVlan=_ReceivedPoliciesTaggedVlan_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,4),_ReceivedPoliciesTaggedVlan_Type())
receivedPoliciesTaggedVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoliciesTaggedVlan.setStatus(_A)
_ReceivedPoliciesVlanId_Type=Unsigned32
_ReceivedPoliciesVlanId_Object=MibTableColumn
receivedPoliciesVlanId=_ReceivedPoliciesVlanId_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,5),_ReceivedPoliciesVlanId_Type())
receivedPoliciesVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoliciesVlanId.setStatus(_A)
class _ReceivedPoliciesLayer2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,0),('background',1),('spare',2),('bestEffort',3),('excellentEffort',4),('controlledLoad',5),('video',6),('voice',7),('networkControl',8)))
_ReceivedPoliciesLayer2Priority_Type.__name__=_C
_ReceivedPoliciesLayer2Priority_Object=MibTableColumn
receivedPoliciesLayer2Priority=_ReceivedPoliciesLayer2Priority_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,6),_ReceivedPoliciesLayer2Priority_Type())
receivedPoliciesLayer2Priority.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoliciesLayer2Priority.setStatus(_A)
class _ReceivedPoliciesDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedPoliciesDscp_Type.__name__=_C
_ReceivedPoliciesDscp_Object=MibTableColumn
receivedPoliciesDscp=_ReceivedPoliciesDscp_Object((1,3,6,1,4,1,3181,10,6,2,43,103,1,7),_ReceivedPoliciesDscp_Type())
receivedPoliciesDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoliciesDscp.setStatus(_A)
_ReceivedInventoryInfosTable_Object=MibTable
receivedInventoryInfosTable=_ReceivedInventoryInfosTable_Object((1,3,6,1,4,1,3181,10,6,2,43,104))
if mibBuilder.loadTexts:receivedInventoryInfosTable.setStatus(_A)
_ReceivedInventoryInfosEntry_Object=MibTableRow
receivedInventoryInfosEntry=_ReceivedInventoryInfosEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1))
receivedInventoryInfosEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:receivedInventoryInfosEntry.setStatus(_A)
class _ReceivedInventoryInfosPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedInventoryInfosPortIndex_Type.__name__=_C
_ReceivedInventoryInfosPortIndex_Object=MibTableColumn
receivedInventoryInfosPortIndex=_ReceivedInventoryInfosPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,1),_ReceivedInventoryInfosPortIndex_Type())
receivedInventoryInfosPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedInventoryInfosPortIndex.setStatus(_A)
_ReceivedInventoryInfosHardwareRevision_Type=DisplayString
_ReceivedInventoryInfosHardwareRevision_Object=MibTableColumn
receivedInventoryInfosHardwareRevision=_ReceivedInventoryInfosHardwareRevision_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,2),_ReceivedInventoryInfosHardwareRevision_Type())
receivedInventoryInfosHardwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosHardwareRevision.setStatus(_A)
_ReceivedInventoryInfosFirmwareRevision_Type=DisplayString
_ReceivedInventoryInfosFirmwareRevision_Object=MibTableColumn
receivedInventoryInfosFirmwareRevision=_ReceivedInventoryInfosFirmwareRevision_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,3),_ReceivedInventoryInfosFirmwareRevision_Type())
receivedInventoryInfosFirmwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosFirmwareRevision.setStatus(_A)
_ReceivedInventoryInfosSoftwareRevision_Type=DisplayString
_ReceivedInventoryInfosSoftwareRevision_Object=MibTableColumn
receivedInventoryInfosSoftwareRevision=_ReceivedInventoryInfosSoftwareRevision_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,4),_ReceivedInventoryInfosSoftwareRevision_Type())
receivedInventoryInfosSoftwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosSoftwareRevision.setStatus(_A)
_ReceivedInventoryInfosSerialNumber_Type=DisplayString
_ReceivedInventoryInfosSerialNumber_Object=MibTableColumn
receivedInventoryInfosSerialNumber=_ReceivedInventoryInfosSerialNumber_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,5),_ReceivedInventoryInfosSerialNumber_Type())
receivedInventoryInfosSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosSerialNumber.setStatus(_A)
_ReceivedInventoryInfosManufacturer_Type=DisplayString
_ReceivedInventoryInfosManufacturer_Object=MibTableColumn
receivedInventoryInfosManufacturer=_ReceivedInventoryInfosManufacturer_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,6),_ReceivedInventoryInfosManufacturer_Type())
receivedInventoryInfosManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosManufacturer.setStatus(_A)
_ReceivedInventoryInfosModelName_Type=DisplayString
_ReceivedInventoryInfosModelName_Object=MibTableColumn
receivedInventoryInfosModelName=_ReceivedInventoryInfosModelName_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,7),_ReceivedInventoryInfosModelName_Type())
receivedInventoryInfosModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosModelName.setStatus(_A)
_ReceivedInventoryInfosAssetId_Type=DisplayString
_ReceivedInventoryInfosAssetId_Object=MibTableColumn
receivedInventoryInfosAssetId=_ReceivedInventoryInfosAssetId_Object((1,3,6,1,4,1,3181,10,6,2,43,104,1,8),_ReceivedInventoryInfosAssetId_Type())
receivedInventoryInfosAssetId.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedInventoryInfosAssetId.setStatus(_A)
_ReceivedPoeInfosTable_Object=MibTable
receivedPoeInfosTable=_ReceivedPoeInfosTable_Object((1,3,6,1,4,1,3181,10,6,2,43,105))
if mibBuilder.loadTexts:receivedPoeInfosTable.setStatus(_A)
_ReceivedPoeInfosEntry_Object=MibTableRow
receivedPoeInfosEntry=_ReceivedPoeInfosEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,105,1))
receivedPoeInfosEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:receivedPoeInfosEntry.setStatus(_A)
class _ReceivedPoeInfosPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedPoeInfosPortIndex_Type.__name__=_C
_ReceivedPoeInfosPortIndex_Object=MibTableColumn
receivedPoeInfosPortIndex=_ReceivedPoeInfosPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,105,1,1),_ReceivedPoeInfosPortIndex_Type())
receivedPoeInfosPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedPoeInfosPortIndex.setStatus(_A)
class _ReceivedPoeInfosType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('pse',1),('pd',2),('noPoe',3)))
_ReceivedPoeInfosType_Type.__name__=_C
_ReceivedPoeInfosType_Object=MibTableColumn
receivedPoeInfosType=_ReceivedPoeInfosType_Object((1,3,6,1,4,1,3181,10,6,2,43,105,1,2),_ReceivedPoeInfosType_Type())
receivedPoeInfosType.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeInfosType.setStatus(_A)
class _ReceivedPoeInfosSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_g,1),(_h,2),(_i,3)))
_ReceivedPoeInfosSource_Type.__name__=_C
_ReceivedPoeInfosSource_Object=MibTableColumn
receivedPoeInfosSource=_ReceivedPoeInfosSource_Object((1,3,6,1,4,1,3181,10,6,2,43,105,1,3),_ReceivedPoeInfosSource_Type())
receivedPoeInfosSource.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeInfosSource.setStatus(_A)
class _ReceivedPoeInfosPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_j,1),('high',2),('low',3)))
_ReceivedPoeInfosPriority_Type.__name__=_C
_ReceivedPoeInfosPriority_Object=MibTableColumn
receivedPoeInfosPriority=_ReceivedPoeInfosPriority_Object((1,3,6,1,4,1,3181,10,6,2,43,105,1,4),_ReceivedPoeInfosPriority_Type())
receivedPoeInfosPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeInfosPriority.setStatus(_A)
_ReceivedPoeInfosValue_Type=Unsigned32
_ReceivedPoeInfosValue_Object=MibTableColumn
receivedPoeInfosValue=_ReceivedPoeInfosValue_Object((1,3,6,1,4,1,3181,10,6,2,43,105,1,5),_ReceivedPoeInfosValue_Type())
receivedPoeInfosValue.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeInfosValue.setStatus(_A)
_ReceivedPoeControlTable_Object=MibTable
receivedPoeControlTable=_ReceivedPoeControlTable_Object((1,3,6,1,4,1,3181,10,6,2,43,106))
if mibBuilder.loadTexts:receivedPoeControlTable.setStatus(_A)
_ReceivedPoeControlEntry_Object=MibTableRow
receivedPoeControlEntry=_ReceivedPoeControlEntry_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1))
receivedPoeControlEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:receivedPoeControlEntry.setStatus(_A)
class _ReceivedPoeControlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ReceivedPoeControlPortIndex_Type.__name__=_C
_ReceivedPoeControlPortIndex_Object=MibTableColumn
receivedPoeControlPortIndex=_ReceivedPoeControlPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,1),_ReceivedPoeControlPortIndex_Type())
receivedPoeControlPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:receivedPoeControlPortIndex.setStatus(_A)
class _ReceivedPoeControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('pse',1),('pd',2),('noPoe',3)))
_ReceivedPoeControlType_Type.__name__=_C
_ReceivedPoeControlType_Object=MibTableColumn
receivedPoeControlType=_ReceivedPoeControlType_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,2),_ReceivedPoeControlType_Type())
receivedPoeControlType.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlType.setStatus(_A)
class _ReceivedPoeControlPoePowerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ReceivedPoeControlPoePowerSupported_Type.__name__=_C
_ReceivedPoeControlPoePowerSupported_Object=MibTableColumn
receivedPoeControlPoePowerSupported=_ReceivedPoeControlPoePowerSupported_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,3),_ReceivedPoeControlPoePowerSupported_Type())
receivedPoeControlPoePowerSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPoePowerSupported.setStatus(_A)
class _ReceivedPoeControlPoePowerEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ReceivedPoeControlPoePowerEnabled_Type.__name__=_C
_ReceivedPoeControlPoePowerEnabled_Object=MibTableColumn
receivedPoeControlPoePowerEnabled=_ReceivedPoeControlPoePowerEnabled_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,4),_ReceivedPoeControlPoePowerEnabled_Type())
receivedPoeControlPoePowerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPoePowerEnabled.setStatus(_A)
class _ReceivedPoeControlPairControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_ReceivedPoeControlPairControl_Type.__name__=_C
_ReceivedPoeControlPairControl_Object=MibTableColumn
receivedPoeControlPairControl=_ReceivedPoeControlPairControl_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,5),_ReceivedPoeControlPairControl_Type())
receivedPoeControlPairControl.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPairControl.setStatus(_A)
class _ReceivedPoeControlPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('signal',1),('spare',2)))
_ReceivedPoeControlPowerPairs_Type.__name__=_C
_ReceivedPoeControlPowerPairs_Object=MibTableColumn
receivedPoeControlPowerPairs=_ReceivedPoeControlPowerPairs_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,6),_ReceivedPoeControlPowerPairs_Type())
receivedPoeControlPowerPairs.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPowerPairs.setStatus(_A)
class _ReceivedPoeControlPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noClass',0),('class0',1),('class1',2),('class2',3),('class3',4),('class4',5)))
_ReceivedPoeControlPowerClass_Type.__name__=_C
_ReceivedPoeControlPowerClass_Object=MibTableColumn
receivedPoeControlPowerClass=_ReceivedPoeControlPowerClass_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,7),_ReceivedPoeControlPowerClass_Type())
receivedPoeControlPowerClass.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPowerClass.setStatus(_A)
class _ReceivedPoeControlDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedPoeControlDeviceType_Type.__name__=_C
_ReceivedPoeControlDeviceType_Object=MibTableColumn
receivedPoeControlDeviceType=_ReceivedPoeControlDeviceType_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,8),_ReceivedPoeControlDeviceType_Type())
receivedPoeControlDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlDeviceType.setStatus(_A)
class _ReceivedPoeControlSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_g,1),(_h,2),(_i,3)))
_ReceivedPoeControlSource_Type.__name__=_C
_ReceivedPoeControlSource_Object=MibTableColumn
receivedPoeControlSource=_ReceivedPoeControlSource_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,9),_ReceivedPoeControlSource_Type())
receivedPoeControlSource.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlSource.setStatus(_A)
class _ReceivedPoeControlPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_j,1),('high',2),('low',3)))
_ReceivedPoeControlPriority_Type.__name__=_C
_ReceivedPoeControlPriority_Object=MibTableColumn
receivedPoeControlPriority=_ReceivedPoeControlPriority_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,10),_ReceivedPoeControlPriority_Type())
receivedPoeControlPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPriority.setStatus(_A)
class _ReceivedPoeControlPdRequestedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedPoeControlPdRequestedPower_Type.__name__=_C
_ReceivedPoeControlPdRequestedPower_Object=MibTableColumn
receivedPoeControlPdRequestedPower=_ReceivedPoeControlPdRequestedPower_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,11),_ReceivedPoeControlPdRequestedPower_Type())
receivedPoeControlPdRequestedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPdRequestedPower.setStatus(_A)
class _ReceivedPoeControlPseAllocatedPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ReceivedPoeControlPseAllocatedPower_Type.__name__=_C
_ReceivedPoeControlPseAllocatedPower_Object=MibTableColumn
receivedPoeControlPseAllocatedPower=_ReceivedPoeControlPseAllocatedPower_Object((1,3,6,1,4,1,3181,10,6,2,43,106,1,12),_ReceivedPoeControlPseAllocatedPower_Type())
receivedPoeControlPseAllocatedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPoeControlPseAllocatedPower.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'protocol':protocol,'lldp':lldp,'configTable':configTable,'configEntry':configEntry,_M:configIndex,'configEnableLldp':configEnableLldp,'configEnableCdp':configEnableCdp,'configLldpEnabledPorts':configLldpEnabledPorts,'configReceiveOnly':configReceiveOnly,'configForwardToLink':configForwardToLink,'configAdvertizedMedClass':configAdvertizedMedClass,'configDisableMedInventory':configDisableMedInventory,'configDisableVoiceVlanTlv':configDisableVoiceVlanTlv,'configCdpVersion':configCdpVersion,'configVoiceVlanPrio':configVoiceVlanPrio,'configVoiceVlanSignalPrio':configVoiceVlanSignalPrio,'configVoiceDscp':configVoiceDscp,'configSignalingDscp':configSignalingDscp,'configTimeToLive':configTimeToLive,'configTxDelay':configTxDelay,'configMsgTxInterval':configMsgTxInterval,'configForceLldpTransmission':configForceLldpTransmission,'configLldpResponsePreferred':configLldpResponsePreferred,'localCoordinatesTable':localCoordinatesTable,'localCoordinatesEntry':localCoordinatesEntry,_N:localCoordinatesIndex,'localCoordinatesLatitude':localCoordinatesLatitude,'localCoordinatesLatResolution':localCoordinatesLatResolution,'localCoordinatesLongitude':localCoordinatesLongitude,'localCoordinatesLongResolution':localCoordinatesLongResolution,'localCoordinatesAltitude':localCoordinatesAltitude,'localCoordinatesAltResolution':localCoordinatesAltResolution,'localCoordinatesAltType':localCoordinatesAltType,'localCoordinatesDatum':localCoordinatesDatum,'localCivicLocationTable':localCivicLocationTable,'localCivicLocationEntry':localCivicLocationEntry,_O:localCivicLocationIndex,'localCivicLocationCountryCode':localCivicLocationCountryCode,'localCivicLocationLanguage':localCivicLocationLanguage,'localCivicLocationNationalSubdivision':localCivicLocationNationalSubdivision,'localCivicLocationCounty':localCivicLocationCounty,'localCivicLocationTown':localCivicLocationTown,'localCivicLocationDistrict':localCivicLocationDistrict,'localCivicLocationBlock':localCivicLocationBlock,'localCivicLocationStreet':localCivicLocationStreet,'localCivicLocationLeadingStreetDirection':localCivicLocationLeadingStreetDirection,'localCivicLocationTrailingStreetSuffix':localCivicLocationTrailingStreetSuffix,'localCivicLocationStreetSuffix':localCivicLocationStreetSuffix,'localCivicLocationHouseNumber':localCivicLocationHouseNumber,'localCivicLocationHouseNumberSuffix':localCivicLocationHouseNumberSuffix,'localCivicLocationLandmark':localCivicLocationLandmark,'localCivicLocationAdditionalInfo':localCivicLocationAdditionalInfo,'localCivicLocationName':localCivicLocationName,'localCivicLocationZipCode':localCivicLocationZipCode,'localCivicLocationBuilding':localCivicLocationBuilding,'localCivicLocationUnit':localCivicLocationUnit,'localCivicLocationFloor':localCivicLocationFloor,'localCivicLocationRoom':localCivicLocationRoom,'localCivicLocationPlaceType':localCivicLocationPlaceType,'localCivicLocationScript':localCivicLocationScript,'localCivicLocationElinNumber':localCivicLocationElinNumber,'receivedOverviewTable':receivedOverviewTable,'receivedOverviewEntry':receivedOverviewEntry,_P:receivedOverviewPortIndex,'receivedOverviewSysName':receivedOverviewSysName,'receivedOverviewSysDesc':receivedOverviewSysDesc,'receivedOverviewChassisIdSubtype':receivedOverviewChassisIdSubtype,'receivedOverviewChassisId':receivedOverviewChassisId,'receivedOverviewMgmtIp':receivedOverviewMgmtIp,'receivedOverviewMgmtOid':receivedOverviewMgmtOid,'receivedOverviewCapabilities':receivedOverviewCapabilities,'receivedOverviewCapabilitiesEnabled':receivedOverviewCapabilitiesEnabled,'receivedOverviewMedCapabilities':receivedOverviewMedCapabilities,'receivedOverviewPortIdSubtype':receivedOverviewPortIdSubtype,'receivedOverviewPortIdentification':receivedOverviewPortIdentification,'receivedOverviewPortDescription':receivedOverviewPortDescription,'receivedOverviewPortVlan':receivedOverviewPortVlan,'receivedCoordinatesTable':receivedCoordinatesTable,'receivedCoordinatesEntry':receivedCoordinatesEntry,_b:receivedCoordinatesPortIndex,'receivedCoordinatesLatitude':receivedCoordinatesLatitude,'receivedCoordinatesLatResolution':receivedCoordinatesLatResolution,'receivedCoordinatesLongitude':receivedCoordinatesLongitude,'receivedCoordinatesLongResolution':receivedCoordinatesLongResolution,'receivedCoordinatesAltitude':receivedCoordinatesAltitude,'receivedCoordinatesAltResolution':receivedCoordinatesAltResolution,'receivedCoordinatesAltUnit':receivedCoordinatesAltUnit,'receivedCoordinatesDatum':receivedCoordinatesDatum,'receivedCivicLocationsTable':receivedCivicLocationsTable,'receivedCivicLocationsEntry':receivedCivicLocationsEntry,_c:receivedCivicLocationsPortIndex,'receivedCivicLocationsCountryCode':receivedCivicLocationsCountryCode,'receivedCivicLocationsLanguage':receivedCivicLocationsLanguage,'receivedCivicLocationsNationalSubdivision':receivedCivicLocationsNationalSubdivision,'receivedCivicLocationsCounty':receivedCivicLocationsCounty,'receivedCivicLocationsTown':receivedCivicLocationsTown,'receivedCivicLocationsDistrict':receivedCivicLocationsDistrict,'receivedCivicLocationsBlock':receivedCivicLocationsBlock,'receivedCivicLocationsStreet':receivedCivicLocationsStreet,'receivedCivicLocationsLeadingStreetDirection':receivedCivicLocationsLeadingStreetDirection,'receivedCivicLocationsTrailingStreetSuffix':receivedCivicLocationsTrailingStreetSuffix,'receivedCivicLocationsStreetSuffix':receivedCivicLocationsStreetSuffix,'receivedCivicLocationsHouseNumber':receivedCivicLocationsHouseNumber,'receivedCivicLocationsHouseNumberSuffix':receivedCivicLocationsHouseNumberSuffix,'receivedCivicLocationsLandmark':receivedCivicLocationsLandmark,'receivedCivicLocationsAdditionalInfo':receivedCivicLocationsAdditionalInfo,'receivedCivicLocationsName':receivedCivicLocationsName,'receivedCivicLocationsZipCode':receivedCivicLocationsZipCode,'receivedCivicLocationsBuilding':receivedCivicLocationsBuilding,'receivedCivicLocationsUnit':receivedCivicLocationsUnit,'receivedCivicLocationsFloor':receivedCivicLocationsFloor,'receivedCivicLocationsRoom':receivedCivicLocationsRoom,'receivedCivicLocationsPlaceType':receivedCivicLocationsPlaceType,'receivedCivicLocationsScript':receivedCivicLocationsScript,'receivedCivicLocationsElinNumber':receivedCivicLocationsElinNumber,'receivedPoliciesTable':receivedPoliciesTable,'receivedPoliciesEntry':receivedPoliciesEntry,_d:receivedPoliciesPortIndex,'receivedPoliciesApplicationType':receivedPoliciesApplicationType,'receivedPoliciesPolicyDefined':receivedPoliciesPolicyDefined,'receivedPoliciesTaggedVlan':receivedPoliciesTaggedVlan,'receivedPoliciesVlanId':receivedPoliciesVlanId,'receivedPoliciesLayer2Priority':receivedPoliciesLayer2Priority,'receivedPoliciesDscp':receivedPoliciesDscp,'receivedInventoryInfosTable':receivedInventoryInfosTable,'receivedInventoryInfosEntry':receivedInventoryInfosEntry,_e:receivedInventoryInfosPortIndex,'receivedInventoryInfosHardwareRevision':receivedInventoryInfosHardwareRevision,'receivedInventoryInfosFirmwareRevision':receivedInventoryInfosFirmwareRevision,'receivedInventoryInfosSoftwareRevision':receivedInventoryInfosSoftwareRevision,'receivedInventoryInfosSerialNumber':receivedInventoryInfosSerialNumber,'receivedInventoryInfosManufacturer':receivedInventoryInfosManufacturer,'receivedInventoryInfosModelName':receivedInventoryInfosModelName,'receivedInventoryInfosAssetId':receivedInventoryInfosAssetId,'receivedPoeInfosTable':receivedPoeInfosTable,'receivedPoeInfosEntry':receivedPoeInfosEntry,_f:receivedPoeInfosPortIndex,'receivedPoeInfosType':receivedPoeInfosType,'receivedPoeInfosSource':receivedPoeInfosSource,'receivedPoeInfosPriority':receivedPoeInfosPriority,'receivedPoeInfosValue':receivedPoeInfosValue,'receivedPoeControlTable':receivedPoeControlTable,'receivedPoeControlEntry':receivedPoeControlEntry,_k:receivedPoeControlPortIndex,'receivedPoeControlType':receivedPoeControlType,'receivedPoeControlPoePowerSupported':receivedPoeControlPoePowerSupported,'receivedPoeControlPoePowerEnabled':receivedPoeControlPoePowerEnabled,'receivedPoeControlPairControl':receivedPoeControlPairControl,'receivedPoeControlPowerPairs':receivedPoeControlPowerPairs,'receivedPoeControlPowerClass':receivedPoeControlPowerClass,'receivedPoeControlDeviceType':receivedPoeControlDeviceType,'receivedPoeControlSource':receivedPoeControlSource,'receivedPoeControlPriority':receivedPoeControlPriority,'receivedPoeControlPdRequestedPower':receivedPoeControlPdRequestedPower,'receivedPoeControlPseAllocatedPower':receivedPoeControlPseAllocatedPower})