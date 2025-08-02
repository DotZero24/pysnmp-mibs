_o='cdlLocationPreferWeightGroup'
_n='cdlGeoLocationGroup'
_m='cdlCustomLocationGroup'
_l='cdlLocationPreferWeightValue'
_k='cdlGeoStorageType'
_j='cdlGeoStatus'
_i='cdlGeoResolution'
_h='cdlGeoAltitudeResolution'
_g='cdlGeoAltitudeType'
_f='cdlGeoAltitude'
_e='cdlGeoLongitudeResolution'
_d='cdlGeoLongitude'
_c='cdlGeoLatitudeResolution'
_b='cdlGeoLatitude'
_a='cdlCustomLocationStorageType'
_Z='cdlCustomLocationStatus'
_Y='cdlCustomLocationValue'
_X='cdlCivicAddrLocationStorageType'
_W='cdlCivicAddrLocationStatus'
_V='cdlCivicAddrLocationValue'
_U='cdlKey'
_T='cdlLocationTargetIdentifier'
_S='cdlLocationTargetType'
_R='cdlLocationCountryCode'
_Q='cdlLocationSubTypeCapability'
_P='cdlLocationPreferWeightType'
_O='cdlCustomLocationName'
_N='cdlCivicAddrLocationType'
_M='OctetString'
_L='cdlCivicAddrLocationGroup'
_K='cdlLocationGroup'
_J='read-only'
_I='read-write'
_H='StorageType'
_G='not-accessible'
_F='cdlLocationIndex'
_E='Integer32'
_D='SnmpAdminString'
_C='read-create'
_B='CISCO-DEVICE-LOCATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCode,=mibBuilder.importSymbols('CISCO-TC','CountryCode')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention')
ciscoDeviceLocationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,732))
if mibBuilder.loadTexts:ciscoDeviceLocationMIB.setRevisions(('2010-10-28 00:00','2010-04-26 00:00'))
_CdlMIBNotifications_ObjectIdentity=ObjectIdentity
cdlMIBNotifications=_CdlMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,732,0))
_CdlMIBObjects_ObjectIdentity=ObjectIdentity
cdlMIBObjects=_CdlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,732,1))
_CdlMIBScalars_ObjectIdentity=ObjectIdentity
cdlMIBScalars=_CdlMIBScalars_ObjectIdentity((1,3,6,1,4,1,9,9,732,1,1))
class _CdlKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CdlKey_Type.__name__=_D
_CdlKey_Object=MibScalar
cdlKey=_CdlKey_Object((1,3,6,1,4,1,9,9,732,1,1,1),_CdlKey_Type())
cdlKey.setMaxAccess(_I)
if mibBuilder.loadTexts:cdlKey.setStatus(_A)
_CdlLocationTable_Object=MibTable
cdlLocationTable=_CdlLocationTable_Object((1,3,6,1,4,1,9,9,732,1,2))
if mibBuilder.loadTexts:cdlLocationTable.setStatus(_A)
_CdlLocationEntry_Object=MibTableRow
cdlLocationEntry=_CdlLocationEntry_Object((1,3,6,1,4,1,9,9,732,1,2,1))
cdlLocationEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cdlLocationEntry.setStatus(_A)
_CdlLocationIndex_Type=Unsigned32
_CdlLocationIndex_Object=MibTableColumn
cdlLocationIndex=_CdlLocationIndex_Object((1,3,6,1,4,1,9,9,732,1,2,1,1),_CdlLocationIndex_Type())
cdlLocationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cdlLocationIndex.setStatus(_A)
class _CdlLocationSubTypeCapability_Type(Bits):namedValues=NamedValues(*(('noSubtypesConfigured',0),('geoLocation',1),('civic',2),('elin',3),('custom',4)))
_CdlLocationSubTypeCapability_Type.__name__='Bits'
_CdlLocationSubTypeCapability_Object=MibTableColumn
cdlLocationSubTypeCapability=_CdlLocationSubTypeCapability_Object((1,3,6,1,4,1,9,9,732,1,2,1,2),_CdlLocationSubTypeCapability_Type())
cdlLocationSubTypeCapability.setMaxAccess(_J)
if mibBuilder.loadTexts:cdlLocationSubTypeCapability.setStatus(_A)
_CdlLocationCountryCode_Type=CountryCode
_CdlLocationCountryCode_Object=MibTableColumn
cdlLocationCountryCode=_CdlLocationCountryCode_Object((1,3,6,1,4,1,9,9,732,1,2,1,3),_CdlLocationCountryCode_Type())
cdlLocationCountryCode.setMaxAccess(_I)
if mibBuilder.loadTexts:cdlLocationCountryCode.setStatus(_A)
class _CdlLocationTargetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('interface',1),('ipv4Addr',2)))
_CdlLocationTargetType_Type.__name__=_E
_CdlLocationTargetType_Object=MibTableColumn
cdlLocationTargetType=_CdlLocationTargetType_Object((1,3,6,1,4,1,9,9,732,1,2,1,4),_CdlLocationTargetType_Type())
cdlLocationTargetType.setMaxAccess(_J)
if mibBuilder.loadTexts:cdlLocationTargetType.setStatus(_A)
class _CdlLocationTargetIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CdlLocationTargetIdentifier_Type.__name__=_M
_CdlLocationTargetIdentifier_Object=MibTableColumn
cdlLocationTargetIdentifier=_CdlLocationTargetIdentifier_Object((1,3,6,1,4,1,9,9,732,1,2,1,5),_CdlLocationTargetIdentifier_Type())
cdlLocationTargetIdentifier.setMaxAccess(_J)
if mibBuilder.loadTexts:cdlLocationTargetIdentifier.setStatus(_A)
_CdlCivicAddrLocationTable_Object=MibTable
cdlCivicAddrLocationTable=_CdlCivicAddrLocationTable_Object((1,3,6,1,4,1,9,9,732,1,3))
if mibBuilder.loadTexts:cdlCivicAddrLocationTable.setStatus(_A)
_CdlCivicAddrLocationEntry_Object=MibTableRow
cdlCivicAddrLocationEntry=_CdlCivicAddrLocationEntry_Object((1,3,6,1,4,1,9,9,732,1,3,1))
cdlCivicAddrLocationEntry.setIndexNames((0,_B,_F),(0,_B,_N))
if mibBuilder.loadTexts:cdlCivicAddrLocationEntry.setStatus(_A)
class _CdlCivicAddrLocationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)));namedValues=NamedValues(*(('state',1),('county',2),('city',3),('cityDivision',4),('neighborhood',5),('streetGroup',6),('leadingStreetDirection',16),('trailingStreetDirection',17),('streetSuffix',18),('house',19),('streetNumber',20),('landmark',21),('additionalLoc',22),('name',23),('zipcode',24),('building',25),('unit',26),('floor',27),('room',28),('place',29),('postalCommunityName',30),('postOffiiceBox',31),('additionalCode',32),('seat',33),('primaryRoad',34),('roadSection',35),('roadBranch',36),('roadSubBranch',37),('streetNamePreMod',38),('streetNamePostMod',39)))
_CdlCivicAddrLocationType_Type.__name__=_E
_CdlCivicAddrLocationType_Object=MibTableColumn
cdlCivicAddrLocationType=_CdlCivicAddrLocationType_Object((1,3,6,1,4,1,9,9,732,1,3,1,1),_CdlCivicAddrLocationType_Type())
cdlCivicAddrLocationType.setMaxAccess(_G)
if mibBuilder.loadTexts:cdlCivicAddrLocationType.setStatus(_A)
_CdlCivicAddrLocationValue_Type=SnmpAdminString
_CdlCivicAddrLocationValue_Object=MibTableColumn
cdlCivicAddrLocationValue=_CdlCivicAddrLocationValue_Object((1,3,6,1,4,1,9,9,732,1,3,1,2),_CdlCivicAddrLocationValue_Type())
cdlCivicAddrLocationValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlCivicAddrLocationValue.setStatus(_A)
_CdlCivicAddrLocationStorageType_Type=StorageType
_CdlCivicAddrLocationStorageType_Object=MibTableColumn
cdlCivicAddrLocationStorageType=_CdlCivicAddrLocationStorageType_Object((1,3,6,1,4,1,9,9,732,1,3,1,3),_CdlCivicAddrLocationStorageType_Type())
cdlCivicAddrLocationStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlCivicAddrLocationStorageType.setStatus(_A)
_CdlCivicAddrLocationStatus_Type=RowStatus
_CdlCivicAddrLocationStatus_Object=MibTableColumn
cdlCivicAddrLocationStatus=_CdlCivicAddrLocationStatus_Object((1,3,6,1,4,1,9,9,732,1,3,1,4),_CdlCivicAddrLocationStatus_Type())
cdlCivicAddrLocationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlCivicAddrLocationStatus.setStatus(_A)
_CdlCustomLocationTable_Object=MibTable
cdlCustomLocationTable=_CdlCustomLocationTable_Object((1,3,6,1,4,1,9,9,732,1,4))
if mibBuilder.loadTexts:cdlCustomLocationTable.setStatus(_A)
_CdlCustomLocationEntry_Object=MibTableRow
cdlCustomLocationEntry=_CdlCustomLocationEntry_Object((1,3,6,1,4,1,9,9,732,1,4,1))
cdlCustomLocationEntry.setIndexNames((0,_B,_F),(1,_B,_O))
if mibBuilder.loadTexts:cdlCustomLocationEntry.setStatus(_A)
class _CdlCustomLocationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CdlCustomLocationName_Type.__name__=_D
_CdlCustomLocationName_Object=MibTableColumn
cdlCustomLocationName=_CdlCustomLocationName_Object((1,3,6,1,4,1,9,9,732,1,4,1,1),_CdlCustomLocationName_Type())
cdlCustomLocationName.setMaxAccess(_G)
if mibBuilder.loadTexts:cdlCustomLocationName.setStatus(_A)
class _CdlCustomLocationValue_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CdlCustomLocationValue_Type.__name__=_D
_CdlCustomLocationValue_Object=MibTableColumn
cdlCustomLocationValue=_CdlCustomLocationValue_Object((1,3,6,1,4,1,9,9,732,1,4,1,2),_CdlCustomLocationValue_Type())
cdlCustomLocationValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlCustomLocationValue.setStatus(_A)
class _CdlCustomLocationStorageType_Type(StorageType):defaultValue=3
_CdlCustomLocationStorageType_Type.__name__=_H
_CdlCustomLocationStorageType_Object=MibTableColumn
cdlCustomLocationStorageType=_CdlCustomLocationStorageType_Object((1,3,6,1,4,1,9,9,732,1,4,1,3),_CdlCustomLocationStorageType_Type())
cdlCustomLocationStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlCustomLocationStorageType.setStatus(_A)
_CdlCustomLocationStatus_Type=RowStatus
_CdlCustomLocationStatus_Object=MibTableColumn
cdlCustomLocationStatus=_CdlCustomLocationStatus_Object((1,3,6,1,4,1,9,9,732,1,4,1,4),_CdlCustomLocationStatus_Type())
cdlCustomLocationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlCustomLocationStatus.setStatus(_A)
_CdlGeoLocationTable_Object=MibTable
cdlGeoLocationTable=_CdlGeoLocationTable_Object((1,3,6,1,4,1,9,9,732,1,5))
if mibBuilder.loadTexts:cdlGeoLocationTable.setStatus(_A)
_CdlGeoLocationEntry_Object=MibTableRow
cdlGeoLocationEntry=_CdlGeoLocationEntry_Object((1,3,6,1,4,1,9,9,732,1,5,1))
cdlGeoLocationEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cdlGeoLocationEntry.setStatus(_A)
class _CdlGeoLatitude_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CdlGeoLatitude_Type.__name__=_D
_CdlGeoLatitude_Object=MibTableColumn
cdlGeoLatitude=_CdlGeoLatitude_Object((1,3,6,1,4,1,9,9,732,1,5,1,1),_CdlGeoLatitude_Type())
cdlGeoLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoLatitude.setStatus(_A)
class _CdlGeoLatitudeResolution_Type(SnmpAdminString):defaultValue=OctetString('')
_CdlGeoLatitudeResolution_Type.__name__=_D
_CdlGeoLatitudeResolution_Object=MibTableColumn
cdlGeoLatitudeResolution=_CdlGeoLatitudeResolution_Object((1,3,6,1,4,1,9,9,732,1,5,1,2),_CdlGeoLatitudeResolution_Type())
cdlGeoLatitudeResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoLatitudeResolution.setStatus(_A)
class _CdlGeoLongitude_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CdlGeoLongitude_Type.__name__=_D
_CdlGeoLongitude_Object=MibTableColumn
cdlGeoLongitude=_CdlGeoLongitude_Object((1,3,6,1,4,1,9,9,732,1,5,1,3),_CdlGeoLongitude_Type())
cdlGeoLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoLongitude.setStatus(_A)
class _CdlGeoLongitudeResolution_Type(SnmpAdminString):defaultValue=OctetString('')
_CdlGeoLongitudeResolution_Type.__name__=_D
_CdlGeoLongitudeResolution_Object=MibTableColumn
cdlGeoLongitudeResolution=_CdlGeoLongitudeResolution_Object((1,3,6,1,4,1,9,9,732,1,5,1,4),_CdlGeoLongitudeResolution_Type())
cdlGeoLongitudeResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoLongitudeResolution.setStatus(_A)
class _CdlGeoAltitude_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CdlGeoAltitude_Type.__name__=_D
_CdlGeoAltitude_Object=MibTableColumn
cdlGeoAltitude=_CdlGeoAltitude_Object((1,3,6,1,4,1,9,9,732,1,5,1,5),_CdlGeoAltitude_Type())
cdlGeoAltitude.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoAltitude.setStatus(_A)
class _CdlGeoAltitudeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('meters',1),('floors',2)))
_CdlGeoAltitudeType_Type.__name__=_E
_CdlGeoAltitudeType_Object=MibTableColumn
cdlGeoAltitudeType=_CdlGeoAltitudeType_Object((1,3,6,1,4,1,9,9,732,1,5,1,6),_CdlGeoAltitudeType_Type())
cdlGeoAltitudeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoAltitudeType.setStatus(_A)
class _CdlGeoAltitudeResolution_Type(SnmpAdminString):defaultValue=OctetString('10')
_CdlGeoAltitudeResolution_Type.__name__=_D
_CdlGeoAltitudeResolution_Object=MibTableColumn
cdlGeoAltitudeResolution=_CdlGeoAltitudeResolution_Object((1,3,6,1,4,1,9,9,732,1,5,1,7),_CdlGeoAltitudeResolution_Type())
cdlGeoAltitudeResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoAltitudeResolution.setStatus(_A)
class _CdlGeoResolution_Type(SnmpAdminString):defaultValue=OctetString('10')
_CdlGeoResolution_Type.__name__=_D
_CdlGeoResolution_Object=MibTableColumn
cdlGeoResolution=_CdlGeoResolution_Object((1,3,6,1,4,1,9,9,732,1,5,1,8),_CdlGeoResolution_Type())
cdlGeoResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoResolution.setStatus(_A)
class _CdlGeoStorageType_Type(StorageType):defaultValue=3
_CdlGeoStorageType_Type.__name__=_H
_CdlGeoStorageType_Object=MibTableColumn
cdlGeoStorageType=_CdlGeoStorageType_Object((1,3,6,1,4,1,9,9,732,1,5,1,9),_CdlGeoStorageType_Type())
cdlGeoStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoStorageType.setStatus(_A)
_CdlGeoStatus_Type=RowStatus
_CdlGeoStatus_Object=MibTableColumn
cdlGeoStatus=_CdlGeoStatus_Object((1,3,6,1,4,1,9,9,732,1,5,1,10),_CdlGeoStatus_Type())
cdlGeoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdlGeoStatus.setStatus(_A)
_CdlLocationPreferWeightTable_Object=MibTable
cdlLocationPreferWeightTable=_CdlLocationPreferWeightTable_Object((1,3,6,1,4,1,9,9,732,1,6))
if mibBuilder.loadTexts:cdlLocationPreferWeightTable.setStatus(_A)
_CdlLocationPreferWeightEntry_Object=MibTableRow
cdlLocationPreferWeightEntry=_CdlLocationPreferWeightEntry_Object((1,3,6,1,4,1,9,9,732,1,6,1))
cdlLocationPreferWeightEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cdlLocationPreferWeightEntry.setStatus(_A)
class _CdlLocationPreferWeightType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('locp',2),('dhcp',3),('lldp',4),('cdp',5)))
_CdlLocationPreferWeightType_Type.__name__=_E
_CdlLocationPreferWeightType_Object=MibTableColumn
cdlLocationPreferWeightType=_CdlLocationPreferWeightType_Object((1,3,6,1,4,1,9,9,732,1,6,1,1),_CdlLocationPreferWeightType_Type())
cdlLocationPreferWeightType.setMaxAccess(_G)
if mibBuilder.loadTexts:cdlLocationPreferWeightType.setStatus(_A)
_CdlLocationPreferWeightValue_Type=Unsigned32
_CdlLocationPreferWeightValue_Object=MibTableColumn
cdlLocationPreferWeightValue=_CdlLocationPreferWeightValue_Object((1,3,6,1,4,1,9,9,732,1,6,1,2),_CdlLocationPreferWeightValue_Type())
cdlLocationPreferWeightValue.setMaxAccess(_I)
if mibBuilder.loadTexts:cdlLocationPreferWeightValue.setStatus(_A)
_CdlMIBConform_ObjectIdentity=ObjectIdentity
cdlMIBConform=_CdlMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,732,2))
_CdlMIBCompliances_ObjectIdentity=ObjectIdentity
cdlMIBCompliances=_CdlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,732,2,1))
_CdlMIBGroups_ObjectIdentity=ObjectIdentity
cdlMIBGroups=_CdlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,732,2,2))
cdlLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,732,2,2,1))
cdlLocationGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cdlLocationGroup.setStatus(_A)
cdlCivicAddrLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,732,2,2,2))
cdlCivicAddrLocationGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cdlCivicAddrLocationGroup.setStatus(_A)
cdlCustomLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,732,2,2,3))
cdlCustomLocationGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cdlCustomLocationGroup.setStatus(_A)
cdlGeoLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,732,2,2,4))
cdlGeoLocationGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cdlGeoLocationGroup.setStatus(_A)
cdlLocationPreferWeightGroup=ObjectGroup((1,3,6,1,4,1,9,9,732,2,2,5))
cdlLocationPreferWeightGroup.setObjects((_B,_l))
if mibBuilder.loadTexts:cdlLocationPreferWeightGroup.setStatus(_A)
cdlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,732,2,1,1))
cdlMIBCompliance.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cdlMIBCompliance.setStatus('deprecated')
cdlMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,732,2,1,2))
cdlMIBComplianceRev1.setObjects(*((_B,_K),(_B,_L),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:cdlMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDeviceLocationMIB':ciscoDeviceLocationMIB,'cdlMIBNotifications':cdlMIBNotifications,'cdlMIBObjects':cdlMIBObjects,'cdlMIBScalars':cdlMIBScalars,_U:cdlKey,'cdlLocationTable':cdlLocationTable,'cdlLocationEntry':cdlLocationEntry,_F:cdlLocationIndex,_Q:cdlLocationSubTypeCapability,_R:cdlLocationCountryCode,_S:cdlLocationTargetType,_T:cdlLocationTargetIdentifier,'cdlCivicAddrLocationTable':cdlCivicAddrLocationTable,'cdlCivicAddrLocationEntry':cdlCivicAddrLocationEntry,_N:cdlCivicAddrLocationType,_V:cdlCivicAddrLocationValue,_X:cdlCivicAddrLocationStorageType,_W:cdlCivicAddrLocationStatus,'cdlCustomLocationTable':cdlCustomLocationTable,'cdlCustomLocationEntry':cdlCustomLocationEntry,_O:cdlCustomLocationName,_Y:cdlCustomLocationValue,_a:cdlCustomLocationStorageType,_Z:cdlCustomLocationStatus,'cdlGeoLocationTable':cdlGeoLocationTable,'cdlGeoLocationEntry':cdlGeoLocationEntry,_b:cdlGeoLatitude,_c:cdlGeoLatitudeResolution,_d:cdlGeoLongitude,_e:cdlGeoLongitudeResolution,_f:cdlGeoAltitude,_g:cdlGeoAltitudeType,_h:cdlGeoAltitudeResolution,_i:cdlGeoResolution,_k:cdlGeoStorageType,_j:cdlGeoStatus,'cdlLocationPreferWeightTable':cdlLocationPreferWeightTable,'cdlLocationPreferWeightEntry':cdlLocationPreferWeightEntry,_P:cdlLocationPreferWeightType,_l:cdlLocationPreferWeightValue,'cdlMIBConform':cdlMIBConform,'cdlMIBCompliances':cdlMIBCompliances,'cdlMIBCompliance':cdlMIBCompliance,'cdlMIBComplianceRev1':cdlMIBComplianceRev1,'cdlMIBGroups':cdlMIBGroups,_K:cdlLocationGroup,_L:cdlCivicAddrLocationGroup,_m:cdlCustomLocationGroup,_n:cdlGeoLocationGroup,_o:cdlLocationPreferWeightGroup})