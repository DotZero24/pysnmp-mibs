_At='ciscoWirelessHotspotConfigGroup3'
_As='ciscoWirelessHotspotConfigGroup1'
_Ar='cLHotspotEAPAuthRowStatus'
_Aq='cLHotspotAdviceChargeNAIRealmRowStatus'
_Ap='cLHotspotAdviceChargePlanInfoCurrency'
_Ao='cLHotspotAdviceChargePlanInfoLanguage'
_An='cLHotspotAdviceChargePlanInfoRowStatus'
_Am='cLHotspotAdviceChargeRowStatus'
_Al='cLHotspotTermsConditionsUrlFilter'
_Ak='cLHotspotTermsConditionsTime'
_Aj='cLHotspotTermsConditionsDate'
_Ai='cLHotspotTermsConditionsFilename'
_Ah='cLHotspotIconRowStatus'
_Ag='cLHotspotIconHeight'
_Af='cLHotspotIconWidth'
_Ae='cLHotspotIconLanguage'
_Ad='cLHotspotIconType'
_Ac='cLHotspotIconPath'
_Ab='cLHotspotRealmEAPAuthRowStatus'
_Aa='cLHotspotRealmEAPAuthTunneledEAPCredentialType'
_AZ='cLHotspotRealmEAPAuthCredentialType'
_AY='cLHotspotRealmEAPAuthNonInnerAuthEAPType'
_AX='cLHotspotRealmEAPAuthInnerAuthEAPType'
_AW='cLHotspotEAPAuthType'
_AV='cLHotspotAdviceChargeNAIRealmName'
_AU='cLHotspotAdviceChargePlanInfoPath'
_AT='cLHotspotAdviceChargePlanInfoFilename'
_AS='cLHotspotNetworkAuthType'
_AR='cLHotspotVenueNameLanguage'
_AQ='cLHotspotIconFileName'
_AP='cLHotspotOperatingClassId'
_AO='cLHotspotOsuProviderIconFileName'
_AN='cLHotspotOsuProviderFriendlyNameLanguage'
_AM='soapXmlSpp'
_AL='cLHotspotOperatorNameLanguage'
_AK='cLHotspotConnectionCapabilityPort'
_AJ='cLHotspotConnectionCapabilityProtocol'
_AI='usernamePassword'
_AH='certificate'
_AG='cLHotspotRealmEAPAuthMethod'
_AF='cLHotspot3gppCountryCode'
_AE='cLHotspot3gppNetworkCode'
_AD='cLHotspotDomainName'
_AC='cLHotspotRoamingOI'
_AB='notAvailable'
_AA='TruthValue'
_A9='ciscoWirelessHotspotConfigGroup2'
_A8='cLHotspotNetworkAuthRowStatus'
_A7='cLHotspotNetworkAuthUrl'
_A6='cLHotspotVenueNameRowStatus'
_A5='cLHotspotVenueNameUrl'
_A4='cLHotspotVenueNameDescription'
_A3='cLHotspotOperatingClassRowStatus'
_A2='cLHotspotOsuProviderIconRowStatus'
_A1='cLHotspotOsuProviderFriendlyNameRowStatus'
_A0='cLHotspotOsuProviderFriendlyNameDescription'
_z='cLHotspotOsuProviderFriendlyName'
_y='cLHotspotOsuProviderRowStatus'
_x='cLHotspotOsuProviderSecondaryMethod'
_w='cLHotspotOsuProviderPrimaryMethod'
_v='cLHotspotOsuProviderNai'
_u='cLHotspotOsuProviderServerUri'
_t='cLHotspotOperatorNameRowStatus'
_s='cLHotspotOperatorName'
_r='cLHotspotConnectionCapabilityRowStatus'
_q='cLHotspotConnectionCapabilityStatus'
_p='cLHotspotRealmEAPRowStatus'
_o='cLHotspotRealmRowStatus'
_n='cLHotspot3gppRowStatus'
_m='cLHotspotDomainNameRowStatus'
_l='cLHotspotRoamingOIRowStatus'
_k='cLHotspotRoamingOIIsBeacon'
_j='cLHotspotAnqpServerRowStatus'
_i='cLHotspotWanLoadMeasDuration'
_h='cLHotspotWanUplinkLoad'
_g='cLHotspotWanDownlinkLoad'
_f='cLHotspotWanUplinkSpeed'
_e='cLHotspotWanDownlinkSpeed'
_d='cLHotspotWanIsAtCapacity'
_c='cLHotspotWanLinkStatus'
_b='cLHotspotAnqpOsuSsid'
_a='cLHotspotAnqpServerIpv6AddressType'
_Z='cLHotspotAnqpServerIpv4AddressType'
_Y='cLHotspotAnqpDomainIdEnabled'
_X='cLHotspotAnqpDomainId'
_W='cLHotspotAnqpFragmentationThreshold'
_V='cLHotspotGasRequestTimeout'
_U='cLHotspotAnqpServerHessid'
_T='cLHotspotAnqpServerVenueType'
_S='cLHotspotAnqpServerNetworkType'
_R='cLHotspotAnqpServerInternetEnabled'
_Q='cLHotspotAnqpServerDescription'
_P='none'
_O='cLHotspotAdviceChargeType'
_N='cLHotspotOsuProviderName'
_M='reserved'
_L='cLHotspotRealmEAPMethod'
_K='OctetString'
_J='cLHotspotRealmName'
_I='deprecated'
_H='Unsigned32'
_G='Integer32'
_F='cLHotspotAnqpServerName'
_E='not-accessible'
_D='SnmpAdminString'
_C='read-create'
_B='current'
_A='CISCO-WIRELESS-HOTSPOT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_AA)
ciscoWirelessHotspotMIB=ModuleIdentity((1,3,6,1,4,1,9,9,863))
if mibBuilder.loadTexts:ciscoWirelessHotspotMIB.setRevisions(('2020-06-18 00:00','2019-06-20 00:00'))
_CiscoWirelessHotspotMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWirelessHotspotMIBNotifs=_CiscoWirelessHotspotMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,863,0))
_CiscoWirelessHotspotMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWirelessHotspotMIBObjects=_CiscoWirelessHotspotMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,863,1))
_CiscoWirelessHotspotConfig_ObjectIdentity=ObjectIdentity
ciscoWirelessHotspotConfig=_CiscoWirelessHotspotConfig_ObjectIdentity((1,3,6,1,4,1,9,9,863,1,1))
_CLHotspotAnqpServerConfigTable_Object=MibTable
cLHotspotAnqpServerConfigTable=_CLHotspotAnqpServerConfigTable_Object((1,3,6,1,4,1,9,9,863,1,1,1))
if mibBuilder.loadTexts:cLHotspotAnqpServerConfigTable.setStatus(_B)
_CLHotspotAnqpServerConfigEntry_Object=MibTableRow
cLHotspotAnqpServerConfigEntry=_CLHotspotAnqpServerConfigEntry_Object((1,3,6,1,4,1,9,9,863,1,1,1,1))
cLHotspotAnqpServerConfigEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cLHotspotAnqpServerConfigEntry.setStatus(_B)
class _CLHotspotAnqpServerName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotAnqpServerName_Type.__name__=_D
_CLHotspotAnqpServerName_Object=MibTableColumn
cLHotspotAnqpServerName=_CLHotspotAnqpServerName_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,1),_CLHotspotAnqpServerName_Type())
cLHotspotAnqpServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotAnqpServerName.setStatus(_B)
_CLHotspotAnqpServerRowStatus_Type=RowStatus
_CLHotspotAnqpServerRowStatus_Object=MibTableColumn
cLHotspotAnqpServerRowStatus=_CLHotspotAnqpServerRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,2),_CLHotspotAnqpServerRowStatus_Type())
cLHotspotAnqpServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerRowStatus.setStatus(_B)
_CLHotspotAnqpServerDescription_Type=SnmpAdminString
_CLHotspotAnqpServerDescription_Object=MibTableColumn
cLHotspotAnqpServerDescription=_CLHotspotAnqpServerDescription_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,3),_CLHotspotAnqpServerDescription_Type())
cLHotspotAnqpServerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerDescription.setStatus(_B)
_CLHotspotAnqpServerInternetEnabled_Type=TruthValue
_CLHotspotAnqpServerInternetEnabled_Object=MibTableColumn
cLHotspotAnqpServerInternetEnabled=_CLHotspotAnqpServerInternetEnabled_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,4),_CLHotspotAnqpServerInternetEnabled_Type())
cLHotspotAnqpServerInternetEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerInternetEnabled.setStatus(_B)
class _CLHotspotAnqpServerNetworkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('private',1),('guestPrivate',2),('chargeablePublic',3),('freePublic',4),('personalDevice',5),('emergency',6),('test',7),('wildcard',8)))
_CLHotspotAnqpServerNetworkType_Type.__name__=_G
_CLHotspotAnqpServerNetworkType_Object=MibTableColumn
cLHotspotAnqpServerNetworkType=_CLHotspotAnqpServerNetworkType_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,5),_CLHotspotAnqpServerNetworkType_Type())
cLHotspotAnqpServerNetworkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerNetworkType.setStatus(_B)
class _CLHotspotAnqpServerVenueType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66)));namedValues=NamedValues(*(('unspecifiedUnspecified',1),('assemblyUnspecified',2),('assemblyArena',3),('assemblyStadium',4),('assemblyPassengerTerminal',5),('assemblyAmphitheater',6),('assemblyAmusementPark',7),('assemblyPlaceOfWorship',8),('assemblyConventionCenter',9),('assemblyLibrary',10),('assemblyMuseum',11),('assemblyRestaurant',12),('assemblyTheater',13),('assemblyBar',14),('assemblyCoffeeShop',15),('assemblyZoo',16),('assemblyEmergencyCoordCenter',17),('businessUnspecified',18),('businessDoctor',19),('businessBank',20),('businessFireStation',21),('businessPoliceStation',22),('businessPostOffice',23),('businessProfessionalOffice',24),('businessRdFacility',25),('businessAttorney',26),('educationalUnspecifiedEducational',27),('educationalPrimarySchool',28),('educationalSecondarySchool',29),('educationaluniversity',30),('industrialUnspecified',31),('industrialFactory',32),('institutionalUnspecified',33),('institutionalHospital',34),('institutionalLongTermCareFacility',35),('institutionalAlcoholDrugRehabCenter',36),('institutionalGroupHome',37),('institutionalJail',38),('mercantileUnspecified',39),('mercantileRetailStore',40),('mercantileGroceryMarket',41),('mercantileAutomotiveServiceStation',42),('mercantileShoppingMall',43),('mercantileGasStation',44),('residentialUnspecified',45),('residentialPrivate',46),('residentialHotel',47),('residentialDormitory',48),('residentialBoardingHouse',49),('storageUnspecified',50),('utilityUnspecified',51),('vehicularUnspecified',52),('vehicularAutomobileTruck',53),('vehicularAirplane',54),('vehicularBus',55),('vehicularFerry',56),('vehicularBoat',57),('vehicularTrain',58),('vehicularMotorbike',59),('outdoorUnspecified',60),('outdoorMuniMesh',61),('outdoorCityPark',62),('outdoorRestArea',63),('outdoorTrafficControl',64),('outdoorBusStop',65),('outdoorKiosk',66)))
_CLHotspotAnqpServerVenueType_Type.__name__=_G
_CLHotspotAnqpServerVenueType_Object=MibTableColumn
cLHotspotAnqpServerVenueType=_CLHotspotAnqpServerVenueType_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,6),_CLHotspotAnqpServerVenueType_Type())
cLHotspotAnqpServerVenueType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerVenueType.setStatus(_B)
_CLHotspotAnqpServerHessid_Type=MacAddress
_CLHotspotAnqpServerHessid_Object=MibTableColumn
cLHotspotAnqpServerHessid=_CLHotspotAnqpServerHessid_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,7),_CLHotspotAnqpServerHessid_Type())
cLHotspotAnqpServerHessid.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerHessid.setStatus(_B)
class _CLHotspotGasRequestTimeout_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_CLHotspotGasRequestTimeout_Type.__name__=_H
_CLHotspotGasRequestTimeout_Object=MibTableColumn
cLHotspotGasRequestTimeout=_CLHotspotGasRequestTimeout_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,8),_CLHotspotGasRequestTimeout_Type())
cLHotspotGasRequestTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotGasRequestTimeout.setStatus(_B)
if mibBuilder.loadTexts:cLHotspotGasRequestTimeout.setUnits('milliseconds')
class _CLHotspotAnqpFragmentationThreshold_Type(Unsigned32):defaultValue=1294;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1294))
_CLHotspotAnqpFragmentationThreshold_Type.__name__=_H
_CLHotspotAnqpFragmentationThreshold_Object=MibTableColumn
cLHotspotAnqpFragmentationThreshold=_CLHotspotAnqpFragmentationThreshold_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,9),_CLHotspotAnqpFragmentationThreshold_Type())
cLHotspotAnqpFragmentationThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpFragmentationThreshold.setStatus(_B)
if mibBuilder.loadTexts:cLHotspotAnqpFragmentationThreshold.setUnits('bytes')
class _CLHotspotAnqpDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CLHotspotAnqpDomainId_Type.__name__=_H
_CLHotspotAnqpDomainId_Object=MibTableColumn
cLHotspotAnqpDomainId=_CLHotspotAnqpDomainId_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,10),_CLHotspotAnqpDomainId_Type())
cLHotspotAnqpDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpDomainId.setStatus(_B)
_CLHotspotAnqpDomainIdEnabled_Type=TruthValue
_CLHotspotAnqpDomainIdEnabled_Object=MibTableColumn
cLHotspotAnqpDomainIdEnabled=_CLHotspotAnqpDomainIdEnabled_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,11),_CLHotspotAnqpDomainIdEnabled_Type())
cLHotspotAnqpDomainIdEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpDomainIdEnabled.setStatus(_B)
class _CLHotspotAnqpServerIpv4AddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_AB,1),('public',2),('portRestricted',3),('singleNatedPrivate',4),('doubleNatedPrivate',5),('portRestrictedSingleNatedPrivate',6),('portRestrictedDoubleNatedPrivate',7),('notKnown',8)))
_CLHotspotAnqpServerIpv4AddressType_Type.__name__=_G
_CLHotspotAnqpServerIpv4AddressType_Object=MibTableColumn
cLHotspotAnqpServerIpv4AddressType=_CLHotspotAnqpServerIpv4AddressType_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,12),_CLHotspotAnqpServerIpv4AddressType_Type())
cLHotspotAnqpServerIpv4AddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerIpv4AddressType.setStatus(_B)
class _CLHotspotAnqpServerIpv6AddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AB,1),('available',2),('notKnown',3)))
_CLHotspotAnqpServerIpv6AddressType_Type.__name__=_G
_CLHotspotAnqpServerIpv6AddressType_Object=MibTableColumn
cLHotspotAnqpServerIpv6AddressType=_CLHotspotAnqpServerIpv6AddressType_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,13),_CLHotspotAnqpServerIpv6AddressType_Type())
cLHotspotAnqpServerIpv6AddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpServerIpv6AddressType.setStatus(_B)
class _CLHotspotAnqpOsuSsid_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CLHotspotAnqpOsuSsid_Type.__name__=_D
_CLHotspotAnqpOsuSsid_Object=MibTableColumn
cLHotspotAnqpOsuSsid=_CLHotspotAnqpOsuSsid_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,14),_CLHotspotAnqpOsuSsid_Type())
cLHotspotAnqpOsuSsid.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAnqpOsuSsid.setStatus(_B)
class _CLHotspotWanLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notConfigured',0),('up',1),('down',2),('testState',3)))
_CLHotspotWanLinkStatus_Type.__name__=_G
_CLHotspotWanLinkStatus_Object=MibTableColumn
cLHotspotWanLinkStatus=_CLHotspotWanLinkStatus_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,15),_CLHotspotWanLinkStatus_Type())
cLHotspotWanLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanLinkStatus.setStatus(_B)
_CLHotspotWanIsAtCapacity_Type=TruthValue
_CLHotspotWanIsAtCapacity_Object=MibTableColumn
cLHotspotWanIsAtCapacity=_CLHotspotWanIsAtCapacity_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,16),_CLHotspotWanIsAtCapacity_Type())
cLHotspotWanIsAtCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanIsAtCapacity.setStatus(_B)
_CLHotspotWanDownlinkSpeed_Type=Unsigned32
_CLHotspotWanDownlinkSpeed_Object=MibTableColumn
cLHotspotWanDownlinkSpeed=_CLHotspotWanDownlinkSpeed_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,17),_CLHotspotWanDownlinkSpeed_Type())
cLHotspotWanDownlinkSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanDownlinkSpeed.setStatus(_B)
_CLHotspotWanUplinkSpeed_Type=Unsigned32
_CLHotspotWanUplinkSpeed_Object=MibTableColumn
cLHotspotWanUplinkSpeed=_CLHotspotWanUplinkSpeed_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,18),_CLHotspotWanUplinkSpeed_Type())
cLHotspotWanUplinkSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanUplinkSpeed.setStatus(_B)
class _CLHotspotWanDownlinkLoad_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CLHotspotWanDownlinkLoad_Type.__name__=_H
_CLHotspotWanDownlinkLoad_Object=MibTableColumn
cLHotspotWanDownlinkLoad=_CLHotspotWanDownlinkLoad_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,19),_CLHotspotWanDownlinkLoad_Type())
cLHotspotWanDownlinkLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanDownlinkLoad.setStatus(_B)
class _CLHotspotWanUplinkLoad_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CLHotspotWanUplinkLoad_Type.__name__=_H
_CLHotspotWanUplinkLoad_Object=MibTableColumn
cLHotspotWanUplinkLoad=_CLHotspotWanUplinkLoad_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,20),_CLHotspotWanUplinkLoad_Type())
cLHotspotWanUplinkLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanUplinkLoad.setStatus(_B)
class _CLHotspotWanLoadMeasDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CLHotspotWanLoadMeasDuration_Type.__name__=_H
_CLHotspotWanLoadMeasDuration_Object=MibTableColumn
cLHotspotWanLoadMeasDuration=_CLHotspotWanLoadMeasDuration_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,21),_CLHotspotWanLoadMeasDuration_Type())
cLHotspotWanLoadMeasDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotWanLoadMeasDuration.setStatus(_B)
if mibBuilder.loadTexts:cLHotspotWanLoadMeasDuration.setUnits('tenths of seconds')
class _CLHotspotTermsConditionsFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,220))
_CLHotspotTermsConditionsFilename_Type.__name__=_D
_CLHotspotTermsConditionsFilename_Object=MibTableColumn
cLHotspotTermsConditionsFilename=_CLHotspotTermsConditionsFilename_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,22),_CLHotspotTermsConditionsFilename_Type())
cLHotspotTermsConditionsFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotTermsConditionsFilename.setStatus(_B)
class _CLHotspotTermsConditionsDate_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CLHotspotTermsConditionsDate_Type.__name__=_D
_CLHotspotTermsConditionsDate_Object=MibTableColumn
cLHotspotTermsConditionsDate=_CLHotspotTermsConditionsDate_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,23),_CLHotspotTermsConditionsDate_Type())
cLHotspotTermsConditionsDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotTermsConditionsDate.setStatus(_B)
class _CLHotspotTermsConditionsTime_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CLHotspotTermsConditionsTime_Type.__name__=_D
_CLHotspotTermsConditionsTime_Object=MibTableColumn
cLHotspotTermsConditionsTime=_CLHotspotTermsConditionsTime_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,24),_CLHotspotTermsConditionsTime_Type())
cLHotspotTermsConditionsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotTermsConditionsTime.setStatus(_B)
class _CLHotspotTermsConditionsUrlFilter_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CLHotspotTermsConditionsUrlFilter_Type.__name__=_D
_CLHotspotTermsConditionsUrlFilter_Object=MibTableColumn
cLHotspotTermsConditionsUrlFilter=_CLHotspotTermsConditionsUrlFilter_Object((1,3,6,1,4,1,9,9,863,1,1,1,1,25),_CLHotspotTermsConditionsUrlFilter_Type())
cLHotspotTermsConditionsUrlFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotTermsConditionsUrlFilter.setStatus(_B)
_CLHotspotRoamingOITable_Object=MibTable
cLHotspotRoamingOITable=_CLHotspotRoamingOITable_Object((1,3,6,1,4,1,9,9,863,1,1,2))
if mibBuilder.loadTexts:cLHotspotRoamingOITable.setStatus(_B)
_CLHotspotRoamingOIEntry_Object=MibTableRow
cLHotspotRoamingOIEntry=_CLHotspotRoamingOIEntry_Object((1,3,6,1,4,1,9,9,863,1,1,2,1))
cLHotspotRoamingOIEntry.setIndexNames((0,_A,_F),(0,_A,_AC))
if mibBuilder.loadTexts:cLHotspotRoamingOIEntry.setStatus(_B)
class _CLHotspotRoamingOI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6),ValueSizeConstraint(10,10))
_CLHotspotRoamingOI_Type.__name__=_K
_CLHotspotRoamingOI_Object=MibTableColumn
cLHotspotRoamingOI=_CLHotspotRoamingOI_Object((1,3,6,1,4,1,9,9,863,1,1,2,1,1),_CLHotspotRoamingOI_Type())
cLHotspotRoamingOI.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotRoamingOI.setStatus(_B)
_CLHotspotRoamingOIRowStatus_Type=RowStatus
_CLHotspotRoamingOIRowStatus_Object=MibTableColumn
cLHotspotRoamingOIRowStatus=_CLHotspotRoamingOIRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,2,1,2),_CLHotspotRoamingOIRowStatus_Type())
cLHotspotRoamingOIRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRoamingOIRowStatus.setStatus(_B)
class _CLHotspotRoamingOIIsBeacon_Type(TruthValue):defaultValue=2
_CLHotspotRoamingOIIsBeacon_Type.__name__=_AA
_CLHotspotRoamingOIIsBeacon_Object=MibTableColumn
cLHotspotRoamingOIIsBeacon=_CLHotspotRoamingOIIsBeacon_Object((1,3,6,1,4,1,9,9,863,1,1,2,1,3),_CLHotspotRoamingOIIsBeacon_Type())
cLHotspotRoamingOIIsBeacon.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRoamingOIIsBeacon.setStatus(_B)
_CLHotspotDomainNameTable_Object=MibTable
cLHotspotDomainNameTable=_CLHotspotDomainNameTable_Object((1,3,6,1,4,1,9,9,863,1,1,3))
if mibBuilder.loadTexts:cLHotspotDomainNameTable.setStatus(_B)
_CLHotspotDomainNameEntry_Object=MibTableRow
cLHotspotDomainNameEntry=_CLHotspotDomainNameEntry_Object((1,3,6,1,4,1,9,9,863,1,1,3,1))
cLHotspotDomainNameEntry.setIndexNames((0,_A,_F),(0,_A,_AD))
if mibBuilder.loadTexts:cLHotspotDomainNameEntry.setStatus(_B)
class _CLHotspotDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotDomainName_Type.__name__=_D
_CLHotspotDomainName_Object=MibTableColumn
cLHotspotDomainName=_CLHotspotDomainName_Object((1,3,6,1,4,1,9,9,863,1,1,3,1,1),_CLHotspotDomainName_Type())
cLHotspotDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotDomainName.setStatus(_B)
_CLHotspotDomainNameRowStatus_Type=RowStatus
_CLHotspotDomainNameRowStatus_Object=MibTableColumn
cLHotspotDomainNameRowStatus=_CLHotspotDomainNameRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,3,1,2),_CLHotspotDomainNameRowStatus_Type())
cLHotspotDomainNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotDomainNameRowStatus.setStatus(_B)
_CLHotspot3gppTable_Object=MibTable
cLHotspot3gppTable=_CLHotspot3gppTable_Object((1,3,6,1,4,1,9,9,863,1,1,4))
if mibBuilder.loadTexts:cLHotspot3gppTable.setStatus(_B)
_CLHotspot3gppEntry_Object=MibTableRow
cLHotspot3gppEntry=_CLHotspot3gppEntry_Object((1,3,6,1,4,1,9,9,863,1,1,4,1))
cLHotspot3gppEntry.setIndexNames((0,_A,_F),(0,_A,_AE),(0,_A,_AF))
if mibBuilder.loadTexts:cLHotspot3gppEntry.setStatus(_B)
class _CLHotspot3gppNetworkCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2),ValueSizeConstraint(3,3))
_CLHotspot3gppNetworkCode_Type.__name__=_K
_CLHotspot3gppNetworkCode_Object=MibTableColumn
cLHotspot3gppNetworkCode=_CLHotspot3gppNetworkCode_Object((1,3,6,1,4,1,9,9,863,1,1,4,1,1),_CLHotspot3gppNetworkCode_Type())
cLHotspot3gppNetworkCode.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspot3gppNetworkCode.setStatus(_B)
class _CLHotspot3gppCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_CLHotspot3gppCountryCode_Type.__name__=_K
_CLHotspot3gppCountryCode_Object=MibTableColumn
cLHotspot3gppCountryCode=_CLHotspot3gppCountryCode_Object((1,3,6,1,4,1,9,9,863,1,1,4,1,2),_CLHotspot3gppCountryCode_Type())
cLHotspot3gppCountryCode.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspot3gppCountryCode.setStatus(_B)
_CLHotspot3gppRowStatus_Type=RowStatus
_CLHotspot3gppRowStatus_Object=MibTableColumn
cLHotspot3gppRowStatus=_CLHotspot3gppRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,4,1,3),_CLHotspot3gppRowStatus_Type())
cLHotspot3gppRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspot3gppRowStatus.setStatus(_B)
_CLHotspotRealmTable_Object=MibTable
cLHotspotRealmTable=_CLHotspotRealmTable_Object((1,3,6,1,4,1,9,9,863,1,1,5))
if mibBuilder.loadTexts:cLHotspotRealmTable.setStatus(_B)
_CLHotspotRealmEntry_Object=MibTableRow
cLHotspotRealmEntry=_CLHotspotRealmEntry_Object((1,3,6,1,4,1,9,9,863,1,1,5,1))
cLHotspotRealmEntry.setIndexNames((0,_A,_F),(0,_A,_J))
if mibBuilder.loadTexts:cLHotspotRealmEntry.setStatus(_B)
class _CLHotspotRealmName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotRealmName_Type.__name__=_D
_CLHotspotRealmName_Object=MibTableColumn
cLHotspotRealmName=_CLHotspotRealmName_Object((1,3,6,1,4,1,9,9,863,1,1,5,1,1),_CLHotspotRealmName_Type())
cLHotspotRealmName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotRealmName.setStatus(_B)
_CLHotspotRealmRowStatus_Type=RowStatus
_CLHotspotRealmRowStatus_Object=MibTableColumn
cLHotspotRealmRowStatus=_CLHotspotRealmRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,5,1,2),_CLHotspotRealmRowStatus_Type())
cLHotspotRealmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmRowStatus.setStatus(_B)
_CLHotspotRealmEAPTable_Object=MibTable
cLHotspotRealmEAPTable=_CLHotspotRealmEAPTable_Object((1,3,6,1,4,1,9,9,863,1,1,6))
if mibBuilder.loadTexts:cLHotspotRealmEAPTable.setStatus(_B)
_CLHotspotRealmEAPEntry_Object=MibTableRow
cLHotspotRealmEAPEntry=_CLHotspotRealmEAPEntry_Object((1,3,6,1,4,1,9,9,863,1,1,6,1))
cLHotspotRealmEAPEntry.setIndexNames((0,_A,_F),(0,_A,_J),(0,_A,_L))
if mibBuilder.loadTexts:cLHotspotRealmEAPEntry.setStatus(_B)
class _CLHotspotRealmEAPMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('eapTLS',1),('eapLEAP',2),('eapSIM',3),('eapTTLS',4),('eapAKA',5),('eapPEAP',6),('eapFAST',7)))
_CLHotspotRealmEAPMethod_Type.__name__=_G
_CLHotspotRealmEAPMethod_Object=MibTableColumn
cLHotspotRealmEAPMethod=_CLHotspotRealmEAPMethod_Object((1,3,6,1,4,1,9,9,863,1,1,6,1,1),_CLHotspotRealmEAPMethod_Type())
cLHotspotRealmEAPMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotRealmEAPMethod.setStatus(_B)
_CLHotspotRealmEAPRowStatus_Type=RowStatus
_CLHotspotRealmEAPRowStatus_Object=MibTableColumn
cLHotspotRealmEAPRowStatus=_CLHotspotRealmEAPRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,6,1,2),_CLHotspotRealmEAPRowStatus_Type())
cLHotspotRealmEAPRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmEAPRowStatus.setStatus(_B)
_CLHotspotRealmEAPAuthTable_Object=MibTable
cLHotspotRealmEAPAuthTable=_CLHotspotRealmEAPAuthTable_Object((1,3,6,1,4,1,9,9,863,1,1,7))
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthTable.setStatus(_I)
_CLHotspotRealmEAPAuthEntry_Object=MibTableRow
cLHotspotRealmEAPAuthEntry=_CLHotspotRealmEAPAuthEntry_Object((1,3,6,1,4,1,9,9,863,1,1,7,1))
cLHotspotRealmEAPAuthEntry.setIndexNames((0,_A,_F),(0,_A,_J),(0,_A,_L),(0,_A,_AG))
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthEntry.setStatus(_I)
class _CLHotspotRealmEAPAuthMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('innerAuthNonEap',1),('innerAuthEap',2),('credential',3),('tunneledEapCredential',4)))
_CLHotspotRealmEAPAuthMethod_Type.__name__=_G
_CLHotspotRealmEAPAuthMethod_Object=MibTableColumn
cLHotspotRealmEAPAuthMethod=_CLHotspotRealmEAPAuthMethod_Object((1,3,6,1,4,1,9,9,863,1,1,7,1,1),_CLHotspotRealmEAPAuthMethod_Type())
cLHotspotRealmEAPAuthMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthMethod.setStatus(_I)
_CLHotspotRealmEAPAuthRowStatus_Type=RowStatus
_CLHotspotRealmEAPAuthRowStatus_Object=MibTableColumn
cLHotspotRealmEAPAuthRowStatus=_CLHotspotRealmEAPAuthRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,7,1,2),_CLHotspotRealmEAPAuthRowStatus_Type())
cLHotspotRealmEAPAuthRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthRowStatus.setStatus(_I)
class _CLHotspotRealmEAPAuthInnerAuthEAPType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('eapTLS',2),('eapLEAP',3),('eapSIM',4),('eapTTLS',5),('eapAKA',6),('eapPEAP',7),('eapFAST',8)))
_CLHotspotRealmEAPAuthInnerAuthEAPType_Type.__name__=_G
_CLHotspotRealmEAPAuthInnerAuthEAPType_Object=MibTableColumn
cLHotspotRealmEAPAuthInnerAuthEAPType=_CLHotspotRealmEAPAuthInnerAuthEAPType_Object((1,3,6,1,4,1,9,9,863,1,1,7,1,3),_CLHotspotRealmEAPAuthInnerAuthEAPType_Type())
cLHotspotRealmEAPAuthInnerAuthEAPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthInnerAuthEAPType.setStatus(_I)
class _CLHotspotRealmEAPAuthNonInnerAuthEAPType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),('pap',2),('chap',3),('mschap',4),('mschapV2',5)))
_CLHotspotRealmEAPAuthNonInnerAuthEAPType_Type.__name__=_G
_CLHotspotRealmEAPAuthNonInnerAuthEAPType_Object=MibTableColumn
cLHotspotRealmEAPAuthNonInnerAuthEAPType=_CLHotspotRealmEAPAuthNonInnerAuthEAPType_Object((1,3,6,1,4,1,9,9,863,1,1,7,1,4),_CLHotspotRealmEAPAuthNonInnerAuthEAPType_Type())
cLHotspotRealmEAPAuthNonInnerAuthEAPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthNonInnerAuthEAPType.setStatus(_I)
class _CLHotspotRealmEAPAuthCredentialType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_M,1),('sim',2),('usim',3),('nfc',4),('hwToken',5),('softoken',6),(_AH,7),(_AI,8),(_P,9)))
_CLHotspotRealmEAPAuthCredentialType_Type.__name__=_G
_CLHotspotRealmEAPAuthCredentialType_Object=MibTableColumn
cLHotspotRealmEAPAuthCredentialType=_CLHotspotRealmEAPAuthCredentialType_Object((1,3,6,1,4,1,9,9,863,1,1,7,1,5),_CLHotspotRealmEAPAuthCredentialType_Type())
cLHotspotRealmEAPAuthCredentialType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthCredentialType.setStatus(_I)
class _CLHotspotRealmEAPAuthTunneledEAPCredentialType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_M,1),('sim',2),('usim',3),('nfc',4),('hwToken',5),('softoken',6),(_AH,7),(_AI,8),('anonymous',9)))
_CLHotspotRealmEAPAuthTunneledEAPCredentialType_Type.__name__=_G
_CLHotspotRealmEAPAuthTunneledEAPCredentialType_Object=MibTableColumn
cLHotspotRealmEAPAuthTunneledEAPCredentialType=_CLHotspotRealmEAPAuthTunneledEAPCredentialType_Object((1,3,6,1,4,1,9,9,863,1,1,7,1,6),_CLHotspotRealmEAPAuthTunneledEAPCredentialType_Type())
cLHotspotRealmEAPAuthTunneledEAPCredentialType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotRealmEAPAuthTunneledEAPCredentialType.setStatus(_I)
_CLHotspotConnectionCapabilityTable_Object=MibTable
cLHotspotConnectionCapabilityTable=_CLHotspotConnectionCapabilityTable_Object((1,3,6,1,4,1,9,9,863,1,1,8))
if mibBuilder.loadTexts:cLHotspotConnectionCapabilityTable.setStatus(_B)
_CLHotspotConnectionCapabilityEntry_Object=MibTableRow
cLHotspotConnectionCapabilityEntry=_CLHotspotConnectionCapabilityEntry_Object((1,3,6,1,4,1,9,9,863,1,1,8,1))
cLHotspotConnectionCapabilityEntry.setIndexNames((0,_A,_F),(0,_A,_AJ),(0,_A,_AK))
if mibBuilder.loadTexts:cLHotspotConnectionCapabilityEntry.setStatus(_B)
class _CLHotspotConnectionCapabilityProtocol_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CLHotspotConnectionCapabilityProtocol_Type.__name__=_H
_CLHotspotConnectionCapabilityProtocol_Object=MibTableColumn
cLHotspotConnectionCapabilityProtocol=_CLHotspotConnectionCapabilityProtocol_Object((1,3,6,1,4,1,9,9,863,1,1,8,1,1),_CLHotspotConnectionCapabilityProtocol_Type())
cLHotspotConnectionCapabilityProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotConnectionCapabilityProtocol.setStatus(_B)
class _CLHotspotConnectionCapabilityPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CLHotspotConnectionCapabilityPort_Type.__name__=_H
_CLHotspotConnectionCapabilityPort_Object=MibTableColumn
cLHotspotConnectionCapabilityPort=_CLHotspotConnectionCapabilityPort_Object((1,3,6,1,4,1,9,9,863,1,1,8,1,2),_CLHotspotConnectionCapabilityPort_Type())
cLHotspotConnectionCapabilityPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotConnectionCapabilityPort.setStatus(_B)
_CLHotspotConnectionCapabilityRowStatus_Type=RowStatus
_CLHotspotConnectionCapabilityRowStatus_Object=MibTableColumn
cLHotspotConnectionCapabilityRowStatus=_CLHotspotConnectionCapabilityRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,8,1,3),_CLHotspotConnectionCapabilityRowStatus_Type())
cLHotspotConnectionCapabilityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotConnectionCapabilityRowStatus.setStatus(_B)
class _CLHotspotConnectionCapabilityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('closed',1),('open',2),('unknown',3)))
_CLHotspotConnectionCapabilityStatus_Type.__name__=_G
_CLHotspotConnectionCapabilityStatus_Object=MibTableColumn
cLHotspotConnectionCapabilityStatus=_CLHotspotConnectionCapabilityStatus_Object((1,3,6,1,4,1,9,9,863,1,1,8,1,4),_CLHotspotConnectionCapabilityStatus_Type())
cLHotspotConnectionCapabilityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotConnectionCapabilityStatus.setStatus(_B)
_CLHotspotOperatorNameTable_Object=MibTable
cLHotspotOperatorNameTable=_CLHotspotOperatorNameTable_Object((1,3,6,1,4,1,9,9,863,1,1,9))
if mibBuilder.loadTexts:cLHotspotOperatorNameTable.setStatus(_B)
_CLHotspotOperatorNameEntry_Object=MibTableRow
cLHotspotOperatorNameEntry=_CLHotspotOperatorNameEntry_Object((1,3,6,1,4,1,9,9,863,1,1,9,1))
cLHotspotOperatorNameEntry.setIndexNames((0,_A,_F),(0,_A,_AL))
if mibBuilder.loadTexts:cLHotspotOperatorNameEntry.setStatus(_B)
class _CLHotspotOperatorNameLanguage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,3))
_CLHotspotOperatorNameLanguage_Type.__name__=_D
_CLHotspotOperatorNameLanguage_Object=MibTableColumn
cLHotspotOperatorNameLanguage=_CLHotspotOperatorNameLanguage_Object((1,3,6,1,4,1,9,9,863,1,1,9,1,1),_CLHotspotOperatorNameLanguage_Type())
cLHotspotOperatorNameLanguage.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotOperatorNameLanguage.setStatus(_B)
_CLHotspotOperatorNameRowStatus_Type=RowStatus
_CLHotspotOperatorNameRowStatus_Object=MibTableColumn
cLHotspotOperatorNameRowStatus=_CLHotspotOperatorNameRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,9,1,2),_CLHotspotOperatorNameRowStatus_Type())
cLHotspotOperatorNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOperatorNameRowStatus.setStatus(_B)
class _CLHotspotOperatorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,252))
_CLHotspotOperatorName_Type.__name__=_D
_CLHotspotOperatorName_Object=MibTableColumn
cLHotspotOperatorName=_CLHotspotOperatorName_Object((1,3,6,1,4,1,9,9,863,1,1,9,1,3),_CLHotspotOperatorName_Type())
cLHotspotOperatorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOperatorName.setStatus(_B)
_CLHotspotOsuProviderTable_Object=MibTable
cLHotspotOsuProviderTable=_CLHotspotOsuProviderTable_Object((1,3,6,1,4,1,9,9,863,1,1,10))
if mibBuilder.loadTexts:cLHotspotOsuProviderTable.setStatus(_B)
_CLHotspotOsuProviderEntry_Object=MibTableRow
cLHotspotOsuProviderEntry=_CLHotspotOsuProviderEntry_Object((1,3,6,1,4,1,9,9,863,1,1,10,1))
cLHotspotOsuProviderEntry.setIndexNames((0,_A,_F),(0,_A,_N))
if mibBuilder.loadTexts:cLHotspotOsuProviderEntry.setStatus(_B)
class _CLHotspotOsuProviderName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotOsuProviderName_Type.__name__=_D
_CLHotspotOsuProviderName_Object=MibTableColumn
cLHotspotOsuProviderName=_CLHotspotOsuProviderName_Object((1,3,6,1,4,1,9,9,863,1,1,10,1,1),_CLHotspotOsuProviderName_Type())
cLHotspotOsuProviderName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotOsuProviderName.setStatus(_B)
_CLHotspotOsuProviderRowStatus_Type=RowStatus
_CLHotspotOsuProviderRowStatus_Object=MibTableColumn
cLHotspotOsuProviderRowStatus=_CLHotspotOsuProviderRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,10,1,2),_CLHotspotOsuProviderRowStatus_Type())
cLHotspotOsuProviderRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderRowStatus.setStatus(_B)
_CLHotspotOsuProviderServerUri_Type=SnmpAdminString
_CLHotspotOsuProviderServerUri_Object=MibTableColumn
cLHotspotOsuProviderServerUri=_CLHotspotOsuProviderServerUri_Object((1,3,6,1,4,1,9,9,863,1,1,10,1,3),_CLHotspotOsuProviderServerUri_Type())
cLHotspotOsuProviderServerUri.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderServerUri.setStatus(_B)
_CLHotspotOsuProviderNai_Type=SnmpAdminString
_CLHotspotOsuProviderNai_Object=MibTableColumn
cLHotspotOsuProviderNai=_CLHotspotOsuProviderNai_Object((1,3,6,1,4,1,9,9,863,1,1,10,1,4),_CLHotspotOsuProviderNai_Type())
cLHotspotOsuProviderNai.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderNai.setStatus(_B)
class _CLHotspotOsuProviderPrimaryMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('omaDm',2),(_AM,3)))
_CLHotspotOsuProviderPrimaryMethod_Type.__name__=_G
_CLHotspotOsuProviderPrimaryMethod_Object=MibTableColumn
cLHotspotOsuProviderPrimaryMethod=_CLHotspotOsuProviderPrimaryMethod_Object((1,3,6,1,4,1,9,9,863,1,1,10,1,5),_CLHotspotOsuProviderPrimaryMethod_Type())
cLHotspotOsuProviderPrimaryMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderPrimaryMethod.setStatus(_B)
class _CLHotspotOsuProviderSecondaryMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('omaDm',2),(_AM,3)))
_CLHotspotOsuProviderSecondaryMethod_Type.__name__=_G
_CLHotspotOsuProviderSecondaryMethod_Object=MibTableColumn
cLHotspotOsuProviderSecondaryMethod=_CLHotspotOsuProviderSecondaryMethod_Object((1,3,6,1,4,1,9,9,863,1,1,10,1,6),_CLHotspotOsuProviderSecondaryMethod_Type())
cLHotspotOsuProviderSecondaryMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderSecondaryMethod.setStatus(_B)
_CLHotspotOsuProviderFriendlyNameTable_Object=MibTable
cLHotspotOsuProviderFriendlyNameTable=_CLHotspotOsuProviderFriendlyNameTable_Object((1,3,6,1,4,1,9,9,863,1,1,11))
if mibBuilder.loadTexts:cLHotspotOsuProviderFriendlyNameTable.setStatus(_B)
_CLHotspotOsuProviderFriendlyNameEntry_Object=MibTableRow
cLHotspotOsuProviderFriendlyNameEntry=_CLHotspotOsuProviderFriendlyNameEntry_Object((1,3,6,1,4,1,9,9,863,1,1,11,1))
cLHotspotOsuProviderFriendlyNameEntry.setIndexNames((0,_A,_F),(0,_A,_N),(0,_A,_AN))
if mibBuilder.loadTexts:cLHotspotOsuProviderFriendlyNameEntry.setStatus(_B)
class _CLHotspotOsuProviderFriendlyNameLanguage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,3))
_CLHotspotOsuProviderFriendlyNameLanguage_Type.__name__=_D
_CLHotspotOsuProviderFriendlyNameLanguage_Object=MibTableColumn
cLHotspotOsuProviderFriendlyNameLanguage=_CLHotspotOsuProviderFriendlyNameLanguage_Object((1,3,6,1,4,1,9,9,863,1,1,11,1,1),_CLHotspotOsuProviderFriendlyNameLanguage_Type())
cLHotspotOsuProviderFriendlyNameLanguage.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotOsuProviderFriendlyNameLanguage.setStatus(_B)
_CLHotspotOsuProviderFriendlyNameRowStatus_Type=RowStatus
_CLHotspotOsuProviderFriendlyNameRowStatus_Object=MibTableColumn
cLHotspotOsuProviderFriendlyNameRowStatus=_CLHotspotOsuProviderFriendlyNameRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,11,1,2),_CLHotspotOsuProviderFriendlyNameRowStatus_Type())
cLHotspotOsuProviderFriendlyNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderFriendlyNameRowStatus.setStatus(_B)
class _CLHotspotOsuProviderFriendlyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotOsuProviderFriendlyName_Type.__name__=_D
_CLHotspotOsuProviderFriendlyName_Object=MibTableColumn
cLHotspotOsuProviderFriendlyName=_CLHotspotOsuProviderFriendlyName_Object((1,3,6,1,4,1,9,9,863,1,1,11,1,3),_CLHotspotOsuProviderFriendlyName_Type())
cLHotspotOsuProviderFriendlyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderFriendlyName.setStatus(_B)
_CLHotspotOsuProviderFriendlyNameDescription_Type=SnmpAdminString
_CLHotspotOsuProviderFriendlyNameDescription_Object=MibTableColumn
cLHotspotOsuProviderFriendlyNameDescription=_CLHotspotOsuProviderFriendlyNameDescription_Object((1,3,6,1,4,1,9,9,863,1,1,11,1,4),_CLHotspotOsuProviderFriendlyNameDescription_Type())
cLHotspotOsuProviderFriendlyNameDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderFriendlyNameDescription.setStatus(_B)
_CLHotspotOsuProviderIconTable_Object=MibTable
cLHotspotOsuProviderIconTable=_CLHotspotOsuProviderIconTable_Object((1,3,6,1,4,1,9,9,863,1,1,12))
if mibBuilder.loadTexts:cLHotspotOsuProviderIconTable.setStatus(_B)
_CLHotspotOsuProviderIconEntry_Object=MibTableRow
cLHotspotOsuProviderIconEntry=_CLHotspotOsuProviderIconEntry_Object((1,3,6,1,4,1,9,9,863,1,1,12,1))
cLHotspotOsuProviderIconEntry.setIndexNames((0,_A,_F),(0,_A,_N),(0,_A,_AO))
if mibBuilder.loadTexts:cLHotspotOsuProviderIconEntry.setStatus(_B)
class _CLHotspotOsuProviderIconFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotOsuProviderIconFileName_Type.__name__=_D
_CLHotspotOsuProviderIconFileName_Object=MibTableColumn
cLHotspotOsuProviderIconFileName=_CLHotspotOsuProviderIconFileName_Object((1,3,6,1,4,1,9,9,863,1,1,12,1,1),_CLHotspotOsuProviderIconFileName_Type())
cLHotspotOsuProviderIconFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotOsuProviderIconFileName.setStatus(_B)
_CLHotspotOsuProviderIconRowStatus_Type=RowStatus
_CLHotspotOsuProviderIconRowStatus_Object=MibTableColumn
cLHotspotOsuProviderIconRowStatus=_CLHotspotOsuProviderIconRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,12,1,2),_CLHotspotOsuProviderIconRowStatus_Type())
cLHotspotOsuProviderIconRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOsuProviderIconRowStatus.setStatus(_B)
_CLHotspotOperatingClassTable_Object=MibTable
cLHotspotOperatingClassTable=_CLHotspotOperatingClassTable_Object((1,3,6,1,4,1,9,9,863,1,1,13))
if mibBuilder.loadTexts:cLHotspotOperatingClassTable.setStatus(_B)
_CLHotspotOperatingClassEntry_Object=MibTableRow
cLHotspotOperatingClassEntry=_CLHotspotOperatingClassEntry_Object((1,3,6,1,4,1,9,9,863,1,1,13,1))
cLHotspotOperatingClassEntry.setIndexNames((0,_A,_F),(0,_A,_AP))
if mibBuilder.loadTexts:cLHotspotOperatingClassEntry.setStatus(_B)
class _CLHotspotOperatingClassId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CLHotspotOperatingClassId_Type.__name__=_H
_CLHotspotOperatingClassId_Object=MibTableColumn
cLHotspotOperatingClassId=_CLHotspotOperatingClassId_Object((1,3,6,1,4,1,9,9,863,1,1,13,1,1),_CLHotspotOperatingClassId_Type())
cLHotspotOperatingClassId.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotOperatingClassId.setStatus(_B)
_CLHotspotOperatingClassRowStatus_Type=RowStatus
_CLHotspotOperatingClassRowStatus_Object=MibTableColumn
cLHotspotOperatingClassRowStatus=_CLHotspotOperatingClassRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,13,1,2),_CLHotspotOperatingClassRowStatus_Type())
cLHotspotOperatingClassRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotOperatingClassRowStatus.setStatus(_B)
_CLHotspotIconTable_Object=MibTable
cLHotspotIconTable=_CLHotspotIconTable_Object((1,3,6,1,4,1,9,9,863,1,1,14))
if mibBuilder.loadTexts:cLHotspotIconTable.setStatus(_B)
_CLHotspotIconEntry_Object=MibTableRow
cLHotspotIconEntry=_CLHotspotIconEntry_Object((1,3,6,1,4,1,9,9,863,1,1,14,1))
cLHotspotIconEntry.setIndexNames((0,_A,_AQ))
if mibBuilder.loadTexts:cLHotspotIconEntry.setStatus(_B)
class _CLHotspotIconFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotIconFileName_Type.__name__=_D
_CLHotspotIconFileName_Object=MibTableColumn
cLHotspotIconFileName=_CLHotspotIconFileName_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,1),_CLHotspotIconFileName_Type())
cLHotspotIconFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotIconFileName.setStatus(_B)
_CLHotspotIconRowStatus_Type=RowStatus
_CLHotspotIconRowStatus_Object=MibTableColumn
cLHotspotIconRowStatus=_CLHotspotIconRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,2),_CLHotspotIconRowStatus_Type())
cLHotspotIconRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotIconRowStatus.setStatus(_B)
class _CLHotspotIconPath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5),ValueSizeConstraint(9,9))
_CLHotspotIconPath_Type.__name__=_D
_CLHotspotIconPath_Object=MibTableColumn
cLHotspotIconPath=_CLHotspotIconPath_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,3),_CLHotspotIconPath_Type())
cLHotspotIconPath.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotIconPath.setStatus(_B)
class _CLHotspotIconType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLHotspotIconType_Type.__name__=_D
_CLHotspotIconType_Object=MibTableColumn
cLHotspotIconType=_CLHotspotIconType_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,4),_CLHotspotIconType_Type())
cLHotspotIconType.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotIconType.setStatus(_B)
class _CLHotspotIconLanguage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,3))
_CLHotspotIconLanguage_Type.__name__=_D
_CLHotspotIconLanguage_Object=MibTableColumn
cLHotspotIconLanguage=_CLHotspotIconLanguage_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,5),_CLHotspotIconLanguage_Type())
cLHotspotIconLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotIconLanguage.setStatus(_B)
class _CLHotspotIconWidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CLHotspotIconWidth_Type.__name__=_H
_CLHotspotIconWidth_Object=MibTableColumn
cLHotspotIconWidth=_CLHotspotIconWidth_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,6),_CLHotspotIconWidth_Type())
cLHotspotIconWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotIconWidth.setStatus(_B)
class _CLHotspotIconHeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CLHotspotIconHeight_Type.__name__=_H
_CLHotspotIconHeight_Object=MibTableColumn
cLHotspotIconHeight=_CLHotspotIconHeight_Object((1,3,6,1,4,1,9,9,863,1,1,14,1,7),_CLHotspotIconHeight_Type())
cLHotspotIconHeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotIconHeight.setStatus(_B)
_CLHotspotVenueNameTable_Object=MibTable
cLHotspotVenueNameTable=_CLHotspotVenueNameTable_Object((1,3,6,1,4,1,9,9,863,1,1,15))
if mibBuilder.loadTexts:cLHotspotVenueNameTable.setStatus(_B)
_CLHotspotVenueNameEntry_Object=MibTableRow
cLHotspotVenueNameEntry=_CLHotspotVenueNameEntry_Object((1,3,6,1,4,1,9,9,863,1,1,15,1))
cLHotspotVenueNameEntry.setIndexNames((0,_A,_F),(0,_A,_AR))
if mibBuilder.loadTexts:cLHotspotVenueNameEntry.setStatus(_B)
class _CLHotspotVenueNameLanguage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,3))
_CLHotspotVenueNameLanguage_Type.__name__=_D
_CLHotspotVenueNameLanguage_Object=MibTableColumn
cLHotspotVenueNameLanguage=_CLHotspotVenueNameLanguage_Object((1,3,6,1,4,1,9,9,863,1,1,15,1,1),_CLHotspotVenueNameLanguage_Type())
cLHotspotVenueNameLanguage.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotVenueNameLanguage.setStatus(_B)
_CLHotspotVenueNameRowStatus_Type=RowStatus
_CLHotspotVenueNameRowStatus_Object=MibTableColumn
cLHotspotVenueNameRowStatus=_CLHotspotVenueNameRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,15,1,2),_CLHotspotVenueNameRowStatus_Type())
cLHotspotVenueNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotVenueNameRowStatus.setStatus(_B)
class _CLHotspotVenueNameDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,252))
_CLHotspotVenueNameDescription_Type.__name__=_D
_CLHotspotVenueNameDescription_Object=MibTableColumn
cLHotspotVenueNameDescription=_CLHotspotVenueNameDescription_Object((1,3,6,1,4,1,9,9,863,1,1,15,1,3),_CLHotspotVenueNameDescription_Type())
cLHotspotVenueNameDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotVenueNameDescription.setStatus(_B)
_CLHotspotVenueNameUrl_Type=SnmpAdminString
_CLHotspotVenueNameUrl_Object=MibTableColumn
cLHotspotVenueNameUrl=_CLHotspotVenueNameUrl_Object((1,3,6,1,4,1,9,9,863,1,1,15,1,4),_CLHotspotVenueNameUrl_Type())
cLHotspotVenueNameUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotVenueNameUrl.setStatus(_B)
_CLHotspotNetworkAuthTable_Object=MibTable
cLHotspotNetworkAuthTable=_CLHotspotNetworkAuthTable_Object((1,3,6,1,4,1,9,9,863,1,1,16))
if mibBuilder.loadTexts:cLHotspotNetworkAuthTable.setStatus(_B)
_CLHotspotNetworkAuthEntry_Object=MibTableRow
cLHotspotNetworkAuthEntry=_CLHotspotNetworkAuthEntry_Object((1,3,6,1,4,1,9,9,863,1,1,16,1))
cLHotspotNetworkAuthEntry.setIndexNames((0,_A,_F),(0,_A,_AS))
if mibBuilder.loadTexts:cLHotspotNetworkAuthEntry.setStatus(_B)
class _CLHotspotNetworkAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('termsAndConditions',1),('onlineEnrollment',2),('httpHttpsRedirect',3),('dnsRedirect',4)))
_CLHotspotNetworkAuthType_Type.__name__=_G
_CLHotspotNetworkAuthType_Object=MibTableColumn
cLHotspotNetworkAuthType=_CLHotspotNetworkAuthType_Object((1,3,6,1,4,1,9,9,863,1,1,16,1,1),_CLHotspotNetworkAuthType_Type())
cLHotspotNetworkAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotNetworkAuthType.setStatus(_B)
_CLHotspotNetworkAuthRowStatus_Type=RowStatus
_CLHotspotNetworkAuthRowStatus_Object=MibTableColumn
cLHotspotNetworkAuthRowStatus=_CLHotspotNetworkAuthRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,16,1,2),_CLHotspotNetworkAuthRowStatus_Type())
cLHotspotNetworkAuthRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotNetworkAuthRowStatus.setStatus(_B)
_CLHotspotNetworkAuthUrl_Type=SnmpAdminString
_CLHotspotNetworkAuthUrl_Object=MibTableColumn
cLHotspotNetworkAuthUrl=_CLHotspotNetworkAuthUrl_Object((1,3,6,1,4,1,9,9,863,1,1,16,1,3),_CLHotspotNetworkAuthUrl_Type())
cLHotspotNetworkAuthUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotNetworkAuthUrl.setStatus(_B)
_CLHotspotAdviceChargeTable_Object=MibTable
cLHotspotAdviceChargeTable=_CLHotspotAdviceChargeTable_Object((1,3,6,1,4,1,9,9,863,1,1,17))
if mibBuilder.loadTexts:cLHotspotAdviceChargeTable.setStatus(_B)
_CLHotspotAdviceChargeEntry_Object=MibTableRow
cLHotspotAdviceChargeEntry=_CLHotspotAdviceChargeEntry_Object((1,3,6,1,4,1,9,9,863,1,1,17,1))
cLHotspotAdviceChargeEntry.setIndexNames((0,_A,_F),(0,_A,_O))
if mibBuilder.loadTexts:cLHotspotAdviceChargeEntry.setStatus(_B)
class _CLHotspotAdviceChargeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('time',1),('data',2),('timeAndData',3),('unlimited',4)))
_CLHotspotAdviceChargeType_Type.__name__=_G
_CLHotspotAdviceChargeType_Object=MibTableColumn
cLHotspotAdviceChargeType=_CLHotspotAdviceChargeType_Object((1,3,6,1,4,1,9,9,863,1,1,17,1,1),_CLHotspotAdviceChargeType_Type())
cLHotspotAdviceChargeType.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotAdviceChargeType.setStatus(_B)
_CLHotspotAdviceChargeRowStatus_Type=RowStatus
_CLHotspotAdviceChargeRowStatus_Object=MibTableColumn
cLHotspotAdviceChargeRowStatus=_CLHotspotAdviceChargeRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,17,1,2),_CLHotspotAdviceChargeRowStatus_Type())
cLHotspotAdviceChargeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAdviceChargeRowStatus.setStatus(_B)
_CLHotspotAdviceChargePlanInfoTable_Object=MibTable
cLHotspotAdviceChargePlanInfoTable=_CLHotspotAdviceChargePlanInfoTable_Object((1,3,6,1,4,1,9,9,863,1,1,18))
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoTable.setStatus(_B)
_CLHotspotAdviceChargePlanInfoEntry_Object=MibTableRow
cLHotspotAdviceChargePlanInfoEntry=_CLHotspotAdviceChargePlanInfoEntry_Object((1,3,6,1,4,1,9,9,863,1,1,18,1))
cLHotspotAdviceChargePlanInfoEntry.setIndexNames((0,_A,_F),(0,_A,_O),(0,_A,_AT),(0,_A,_AU))
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoEntry.setStatus(_B)
class _CLHotspotAdviceChargePlanInfoFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,220))
_CLHotspotAdviceChargePlanInfoFilename_Type.__name__=_D
_CLHotspotAdviceChargePlanInfoFilename_Object=MibTableColumn
cLHotspotAdviceChargePlanInfoFilename=_CLHotspotAdviceChargePlanInfoFilename_Object((1,3,6,1,4,1,9,9,863,1,1,18,1,1),_CLHotspotAdviceChargePlanInfoFilename_Type())
cLHotspotAdviceChargePlanInfoFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoFilename.setStatus(_B)
class _CLHotspotAdviceChargePlanInfoPath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,231))
_CLHotspotAdviceChargePlanInfoPath_Type.__name__=_D
_CLHotspotAdviceChargePlanInfoPath_Object=MibTableColumn
cLHotspotAdviceChargePlanInfoPath=_CLHotspotAdviceChargePlanInfoPath_Object((1,3,6,1,4,1,9,9,863,1,1,18,1,2),_CLHotspotAdviceChargePlanInfoPath_Type())
cLHotspotAdviceChargePlanInfoPath.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoPath.setStatus(_B)
_CLHotspotAdviceChargePlanInfoRowStatus_Type=RowStatus
_CLHotspotAdviceChargePlanInfoRowStatus_Object=MibTableColumn
cLHotspotAdviceChargePlanInfoRowStatus=_CLHotspotAdviceChargePlanInfoRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,18,1,3),_CLHotspotAdviceChargePlanInfoRowStatus_Type())
cLHotspotAdviceChargePlanInfoRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoRowStatus.setStatus(_B)
class _CLHotspotAdviceChargePlanInfoLanguage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_CLHotspotAdviceChargePlanInfoLanguage_Type.__name__=_D
_CLHotspotAdviceChargePlanInfoLanguage_Object=MibTableColumn
cLHotspotAdviceChargePlanInfoLanguage=_CLHotspotAdviceChargePlanInfoLanguage_Object((1,3,6,1,4,1,9,9,863,1,1,18,1,4),_CLHotspotAdviceChargePlanInfoLanguage_Type())
cLHotspotAdviceChargePlanInfoLanguage.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoLanguage.setStatus(_B)
class _CLHotspotAdviceChargePlanInfoCurrency_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_CLHotspotAdviceChargePlanInfoCurrency_Type.__name__=_D
_CLHotspotAdviceChargePlanInfoCurrency_Object=MibTableColumn
cLHotspotAdviceChargePlanInfoCurrency=_CLHotspotAdviceChargePlanInfoCurrency_Object((1,3,6,1,4,1,9,9,863,1,1,18,1,5),_CLHotspotAdviceChargePlanInfoCurrency_Type())
cLHotspotAdviceChargePlanInfoCurrency.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAdviceChargePlanInfoCurrency.setStatus(_B)
_CLHotspotAdviceChargeNAIRealmTable_Object=MibTable
cLHotspotAdviceChargeNAIRealmTable=_CLHotspotAdviceChargeNAIRealmTable_Object((1,3,6,1,4,1,9,9,863,1,1,19))
if mibBuilder.loadTexts:cLHotspotAdviceChargeNAIRealmTable.setStatus(_B)
_CLHotspotAdviceChargeNAIRealmEntry_Object=MibTableRow
cLHotspotAdviceChargeNAIRealmEntry=_CLHotspotAdviceChargeNAIRealmEntry_Object((1,3,6,1,4,1,9,9,863,1,1,19,1))
cLHotspotAdviceChargeNAIRealmEntry.setIndexNames((0,_A,_F),(0,_A,_O),(0,_A,_AV))
if mibBuilder.loadTexts:cLHotspotAdviceChargeNAIRealmEntry.setStatus(_B)
class _CLHotspotAdviceChargeNAIRealmName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,220))
_CLHotspotAdviceChargeNAIRealmName_Type.__name__=_D
_CLHotspotAdviceChargeNAIRealmName_Object=MibTableColumn
cLHotspotAdviceChargeNAIRealmName=_CLHotspotAdviceChargeNAIRealmName_Object((1,3,6,1,4,1,9,9,863,1,1,19,1,1),_CLHotspotAdviceChargeNAIRealmName_Type())
cLHotspotAdviceChargeNAIRealmName.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotAdviceChargeNAIRealmName.setStatus(_B)
_CLHotspotAdviceChargeNAIRealmRowStatus_Type=RowStatus
_CLHotspotAdviceChargeNAIRealmRowStatus_Object=MibTableColumn
cLHotspotAdviceChargeNAIRealmRowStatus=_CLHotspotAdviceChargeNAIRealmRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,19,1,2),_CLHotspotAdviceChargeNAIRealmRowStatus_Type())
cLHotspotAdviceChargeNAIRealmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotAdviceChargeNAIRealmRowStatus.setStatus(_B)
_CLHotspotEAPAuthTable_Object=MibTable
cLHotspotEAPAuthTable=_CLHotspotEAPAuthTable_Object((1,3,6,1,4,1,9,9,863,1,1,20))
if mibBuilder.loadTexts:cLHotspotEAPAuthTable.setStatus(_B)
_CLHotspotEAPAuthEntry_Object=MibTableRow
cLHotspotEAPAuthEntry=_CLHotspotEAPAuthEntry_Object((1,3,6,1,4,1,9,9,863,1,1,20,1))
cLHotspotEAPAuthEntry.setIndexNames((0,_A,_F),(0,_A,_J),(0,_A,_L),(0,_A,_AW))
if mibBuilder.loadTexts:cLHotspotEAPAuthEntry.setStatus(_B)
class _CLHotspotEAPAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*(('innerAuthPap',1),('innerAuthChap',2),('innerAuthMschap',3),('innerAuthMschapv2',4),('innerAuthEapTls',5),('innerAuthEapLeap',6),('innerAuthEapSim',7),('innerAuthEapTtls',8),('innerAuthEapAka',9),('innerAuthEapPeap',10),('innerAuthEapFast',11),('credentialSim',12),('credentialUsim',13),('credentialNfc',14),('credentialHwToken',15),('credentialSoftoken',16),('credentialCertificate',17),('credentialUsernamePassword',18),('credentialNone',19),('tunneledEapCredentialSim',20),('tunneledEapCredentialUsim',21),('tunneledEapCredentialNfc',22),('tunneledEapCredentialHwToken',23),('tunneledEapCredentialSoftoken',24),('tunneledEapCredentialCertificate',25),('tunneledEapCredentialUsernamePassword',26),('tunneledEapCredentialAnonymous',27)))
_CLHotspotEAPAuthType_Type.__name__=_G
_CLHotspotEAPAuthType_Object=MibTableColumn
cLHotspotEAPAuthType=_CLHotspotEAPAuthType_Object((1,3,6,1,4,1,9,9,863,1,1,20,1,1),_CLHotspotEAPAuthType_Type())
cLHotspotEAPAuthType.setMaxAccess(_E)
if mibBuilder.loadTexts:cLHotspotEAPAuthType.setStatus(_B)
_CLHotspotEAPAuthRowStatus_Type=RowStatus
_CLHotspotEAPAuthRowStatus_Object=MibTableColumn
cLHotspotEAPAuthRowStatus=_CLHotspotEAPAuthRowStatus_Object((1,3,6,1,4,1,9,9,863,1,1,20,1,2),_CLHotspotEAPAuthRowStatus_Type())
cLHotspotEAPAuthRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLHotspotEAPAuthRowStatus.setStatus(_B)
_CiscoWirelessHotspotMIBConform_ObjectIdentity=ObjectIdentity
ciscoWirelessHotspotMIBConform=_CiscoWirelessHotspotMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,863,2))
_CiscoWirelessHotspotCompliances_ObjectIdentity=ObjectIdentity
ciscoWirelessHotspotCompliances=_CiscoWirelessHotspotCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,863,2,1))
_CiscoWirelessHotspotGroups_ObjectIdentity=ObjectIdentity
ciscoWirelessHotspotGroups=_CiscoWirelessHotspotGroups_ObjectIdentity((1,3,6,1,4,1,9,9,863,2,2))
ciscoWirelessHotspotConfigGroup1=ObjectGroup((1,3,6,1,4,1,9,9,863,2,2,1))
ciscoWirelessHotspotConfigGroup1.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciscoWirelessHotspotConfigGroup1.setStatus(_I)
ciscoWirelessHotspotConfigGroup2=ObjectGroup((1,3,6,1,4,1,9,9,863,2,2,2))
ciscoWirelessHotspotConfigGroup2.setObjects(*((_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoWirelessHotspotConfigGroup2.setStatus(_B)
ciscoWirelessHotspotConfigGroup3=ObjectGroup((1,3,6,1,4,1,9,9,863,2,2,3))
ciscoWirelessHotspotConfigGroup3.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:ciscoWirelessHotspotConfigGroup3.setStatus(_B)
ciscoWirelessHotspotCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,863,2,1,1))
ciscoWirelessHotspotCompliance.setObjects(*((_A,_As),(_A,_A9)))
if mibBuilder.loadTexts:ciscoWirelessHotspotCompliance.setStatus(_I)
ciscoWirelessHotspotComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,863,2,1,2))
ciscoWirelessHotspotComplianceRev1.setObjects(*((_A,_A9),(_A,_At)))
if mibBuilder.loadTexts:ciscoWirelessHotspotComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWirelessHotspotMIB':ciscoWirelessHotspotMIB,'ciscoWirelessHotspotMIBNotifs':ciscoWirelessHotspotMIBNotifs,'ciscoWirelessHotspotMIBObjects':ciscoWirelessHotspotMIBObjects,'ciscoWirelessHotspotConfig':ciscoWirelessHotspotConfig,'cLHotspotAnqpServerConfigTable':cLHotspotAnqpServerConfigTable,'cLHotspotAnqpServerConfigEntry':cLHotspotAnqpServerConfigEntry,_F:cLHotspotAnqpServerName,_j:cLHotspotAnqpServerRowStatus,_Q:cLHotspotAnqpServerDescription,_R:cLHotspotAnqpServerInternetEnabled,_S:cLHotspotAnqpServerNetworkType,_T:cLHotspotAnqpServerVenueType,_U:cLHotspotAnqpServerHessid,_V:cLHotspotGasRequestTimeout,_W:cLHotspotAnqpFragmentationThreshold,_X:cLHotspotAnqpDomainId,_Y:cLHotspotAnqpDomainIdEnabled,_Z:cLHotspotAnqpServerIpv4AddressType,_a:cLHotspotAnqpServerIpv6AddressType,_b:cLHotspotAnqpOsuSsid,_c:cLHotspotWanLinkStatus,_d:cLHotspotWanIsAtCapacity,_e:cLHotspotWanDownlinkSpeed,_f:cLHotspotWanUplinkSpeed,_g:cLHotspotWanDownlinkLoad,_h:cLHotspotWanUplinkLoad,_i:cLHotspotWanLoadMeasDuration,_Ai:cLHotspotTermsConditionsFilename,_Aj:cLHotspotTermsConditionsDate,_Ak:cLHotspotTermsConditionsTime,_Al:cLHotspotTermsConditionsUrlFilter,'cLHotspotRoamingOITable':cLHotspotRoamingOITable,'cLHotspotRoamingOIEntry':cLHotspotRoamingOIEntry,_AC:cLHotspotRoamingOI,_l:cLHotspotRoamingOIRowStatus,_k:cLHotspotRoamingOIIsBeacon,'cLHotspotDomainNameTable':cLHotspotDomainNameTable,'cLHotspotDomainNameEntry':cLHotspotDomainNameEntry,_AD:cLHotspotDomainName,_m:cLHotspotDomainNameRowStatus,'cLHotspot3gppTable':cLHotspot3gppTable,'cLHotspot3gppEntry':cLHotspot3gppEntry,_AE:cLHotspot3gppNetworkCode,_AF:cLHotspot3gppCountryCode,_n:cLHotspot3gppRowStatus,'cLHotspotRealmTable':cLHotspotRealmTable,'cLHotspotRealmEntry':cLHotspotRealmEntry,_J:cLHotspotRealmName,_o:cLHotspotRealmRowStatus,'cLHotspotRealmEAPTable':cLHotspotRealmEAPTable,'cLHotspotRealmEAPEntry':cLHotspotRealmEAPEntry,_L:cLHotspotRealmEAPMethod,_p:cLHotspotRealmEAPRowStatus,'cLHotspotRealmEAPAuthTable':cLHotspotRealmEAPAuthTable,'cLHotspotRealmEAPAuthEntry':cLHotspotRealmEAPAuthEntry,_AG:cLHotspotRealmEAPAuthMethod,_Ab:cLHotspotRealmEAPAuthRowStatus,_AX:cLHotspotRealmEAPAuthInnerAuthEAPType,_AY:cLHotspotRealmEAPAuthNonInnerAuthEAPType,_AZ:cLHotspotRealmEAPAuthCredentialType,_Aa:cLHotspotRealmEAPAuthTunneledEAPCredentialType,'cLHotspotConnectionCapabilityTable':cLHotspotConnectionCapabilityTable,'cLHotspotConnectionCapabilityEntry':cLHotspotConnectionCapabilityEntry,_AJ:cLHotspotConnectionCapabilityProtocol,_AK:cLHotspotConnectionCapabilityPort,_r:cLHotspotConnectionCapabilityRowStatus,_q:cLHotspotConnectionCapabilityStatus,'cLHotspotOperatorNameTable':cLHotspotOperatorNameTable,'cLHotspotOperatorNameEntry':cLHotspotOperatorNameEntry,_AL:cLHotspotOperatorNameLanguage,_t:cLHotspotOperatorNameRowStatus,_s:cLHotspotOperatorName,'cLHotspotOsuProviderTable':cLHotspotOsuProviderTable,'cLHotspotOsuProviderEntry':cLHotspotOsuProviderEntry,_N:cLHotspotOsuProviderName,_y:cLHotspotOsuProviderRowStatus,_u:cLHotspotOsuProviderServerUri,_v:cLHotspotOsuProviderNai,_w:cLHotspotOsuProviderPrimaryMethod,_x:cLHotspotOsuProviderSecondaryMethod,'cLHotspotOsuProviderFriendlyNameTable':cLHotspotOsuProviderFriendlyNameTable,'cLHotspotOsuProviderFriendlyNameEntry':cLHotspotOsuProviderFriendlyNameEntry,_AN:cLHotspotOsuProviderFriendlyNameLanguage,_A1:cLHotspotOsuProviderFriendlyNameRowStatus,_z:cLHotspotOsuProviderFriendlyName,_A0:cLHotspotOsuProviderFriendlyNameDescription,'cLHotspotOsuProviderIconTable':cLHotspotOsuProviderIconTable,'cLHotspotOsuProviderIconEntry':cLHotspotOsuProviderIconEntry,_AO:cLHotspotOsuProviderIconFileName,_A2:cLHotspotOsuProviderIconRowStatus,'cLHotspotOperatingClassTable':cLHotspotOperatingClassTable,'cLHotspotOperatingClassEntry':cLHotspotOperatingClassEntry,_AP:cLHotspotOperatingClassId,_A3:cLHotspotOperatingClassRowStatus,'cLHotspotIconTable':cLHotspotIconTable,'cLHotspotIconEntry':cLHotspotIconEntry,_AQ:cLHotspotIconFileName,_Ah:cLHotspotIconRowStatus,_Ac:cLHotspotIconPath,_Ad:cLHotspotIconType,_Ae:cLHotspotIconLanguage,_Af:cLHotspotIconWidth,_Ag:cLHotspotIconHeight,'cLHotspotVenueNameTable':cLHotspotVenueNameTable,'cLHotspotVenueNameEntry':cLHotspotVenueNameEntry,_AR:cLHotspotVenueNameLanguage,_A6:cLHotspotVenueNameRowStatus,_A4:cLHotspotVenueNameDescription,_A5:cLHotspotVenueNameUrl,'cLHotspotNetworkAuthTable':cLHotspotNetworkAuthTable,'cLHotspotNetworkAuthEntry':cLHotspotNetworkAuthEntry,_AS:cLHotspotNetworkAuthType,_A8:cLHotspotNetworkAuthRowStatus,_A7:cLHotspotNetworkAuthUrl,'cLHotspotAdviceChargeTable':cLHotspotAdviceChargeTable,'cLHotspotAdviceChargeEntry':cLHotspotAdviceChargeEntry,_O:cLHotspotAdviceChargeType,_Am:cLHotspotAdviceChargeRowStatus,'cLHotspotAdviceChargePlanInfoTable':cLHotspotAdviceChargePlanInfoTable,'cLHotspotAdviceChargePlanInfoEntry':cLHotspotAdviceChargePlanInfoEntry,_AT:cLHotspotAdviceChargePlanInfoFilename,_AU:cLHotspotAdviceChargePlanInfoPath,_An:cLHotspotAdviceChargePlanInfoRowStatus,_Ao:cLHotspotAdviceChargePlanInfoLanguage,_Ap:cLHotspotAdviceChargePlanInfoCurrency,'cLHotspotAdviceChargeNAIRealmTable':cLHotspotAdviceChargeNAIRealmTable,'cLHotspotAdviceChargeNAIRealmEntry':cLHotspotAdviceChargeNAIRealmEntry,_AV:cLHotspotAdviceChargeNAIRealmName,_Aq:cLHotspotAdviceChargeNAIRealmRowStatus,'cLHotspotEAPAuthTable':cLHotspotEAPAuthTable,'cLHotspotEAPAuthEntry':cLHotspotEAPAuthEntry,_AW:cLHotspotEAPAuthType,_Ar:cLHotspotEAPAuthRowStatus,'ciscoWirelessHotspotMIBConform':ciscoWirelessHotspotMIBConform,'ciscoWirelessHotspotCompliances':ciscoWirelessHotspotCompliances,'ciscoWirelessHotspotCompliance':ciscoWirelessHotspotCompliance,'ciscoWirelessHotspotComplianceRev1':ciscoWirelessHotspotComplianceRev1,'ciscoWirelessHotspotGroups':ciscoWirelessHotspotGroups,_As:ciscoWirelessHotspotConfigGroup1,_A9:ciscoWirelessHotspotConfigGroup2,_At:ciscoWirelessHotspotConfigGroup3})