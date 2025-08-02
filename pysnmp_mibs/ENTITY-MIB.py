_z='entityPhysicalCRGroup'
_y='entityLogicalGroup'
_x='entConfigChange'
_w='entPhysicalUUID'
_v='entPhysicalUris'
_u='entPhysicalMfgDate'
_t='entLogicalContextName'
_s='entLogicalContextEngineID'
_r='entPhysicalIsFRU'
_q='entPhysicalAssetID'
_p='entPhysicalAlias'
_o='entPhysicalModelName'
_n='entPhysicalMfgName'
_m='entPhysicalSerialNum'
_l='entPhysicalSoftwareRev'
_k='entPhysicalFirmwareRev'
_j='entPhysicalHardwareRev'
_i='entLastChangeTime'
_h='entAliasMappingIdentifier'
_g='entLogicalCommunity'
_f='entPhysicalParentRelPos'
_e='entPhysicalContainedIn'
_d='entPhysicalVendorType'
_c='entPhysicalDescr'
_b='entAliasLogicalIndexOrZero'
_a='OctetString'
_Z='entityPhysical4Group'
_Y='entityPhysical3Group'
_X='entLogicalTDomain'
_W='entLogicalTAddress'
_V='entLogicalType'
_U='entLogicalDescr'
_T='entPhysicalName'
_S='entPhysicalClass'
_R='entPhysicalChildIndex'
_Q='entLPPhysicalIndex'
_P='entLogicalIndex'
_O='not-accessible'
_N='entityLogical2Group'
_M='entityPhysical2Group'
_L='read-write'
_K='entPhysicalIndex'
_J='Integer32'
_I='SnmpAdminString'
_H='entityNotificationsGroup'
_G='entityGeneralGroup'
_F='entityMappingGroup'
_E='entityPhysicalGroup'
_D='deprecated'
_C='read-only'
_B='current'
_A='ENTITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAPhysicalClass,=mibBuilder.importSymbols('IANA-ENTITY-MIB','IANAPhysicalClass')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DateAndTime,DisplayString,PhysAddress,RowPointer,TAddress,TDomain,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime','DisplayString','PhysAddress','RowPointer','TAddress','TDomain','TextualConvention','TimeStamp','TruthValue')
UUIDorZero,=mibBuilder.importSymbols('UUID-TC-MIB','UUIDorZero')
entityMIB=ModuleIdentity((1,3,6,1,2,1,47))
if mibBuilder.loadTexts:entityMIB.setRevisions(('2013-04-05 00:00','2005-08-10 00:00','1999-12-07 00:00','1996-10-31 00:00'))
class PhysicalIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class PhysicalIndexOrZero(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class SnmpEngineIdOrNone(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class PhysicalClass(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('unknown',2),('chassis',3),('backplane',4),('container',5),('powerSupply',6),('fan',7),('sensor',8),('module',9),('port',10),('stack',11),('cpu',12)))
_EntityMIBObjects_ObjectIdentity=ObjectIdentity
entityMIBObjects=_EntityMIBObjects_ObjectIdentity((1,3,6,1,2,1,47,1))
_EntityPhysical_ObjectIdentity=ObjectIdentity
entityPhysical=_EntityPhysical_ObjectIdentity((1,3,6,1,2,1,47,1,1))
_EntPhysicalTable_Object=MibTable
entPhysicalTable=_EntPhysicalTable_Object((1,3,6,1,2,1,47,1,1,1))
if mibBuilder.loadTexts:entPhysicalTable.setStatus(_B)
_EntPhysicalEntry_Object=MibTableRow
entPhysicalEntry=_EntPhysicalEntry_Object((1,3,6,1,2,1,47,1,1,1,1))
entPhysicalEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:entPhysicalEntry.setStatus(_B)
_EntPhysicalIndex_Type=PhysicalIndex
_EntPhysicalIndex_Object=MibTableColumn
entPhysicalIndex=_EntPhysicalIndex_Object((1,3,6,1,2,1,47,1,1,1,1,1),_EntPhysicalIndex_Type())
entPhysicalIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:entPhysicalIndex.setStatus(_B)
_EntPhysicalDescr_Type=SnmpAdminString
_EntPhysicalDescr_Object=MibTableColumn
entPhysicalDescr=_EntPhysicalDescr_Object((1,3,6,1,2,1,47,1,1,1,1,2),_EntPhysicalDescr_Type())
entPhysicalDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalDescr.setStatus(_B)
_EntPhysicalVendorType_Type=AutonomousType
_EntPhysicalVendorType_Object=MibTableColumn
entPhysicalVendorType=_EntPhysicalVendorType_Object((1,3,6,1,2,1,47,1,1,1,1,3),_EntPhysicalVendorType_Type())
entPhysicalVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalVendorType.setStatus(_B)
_EntPhysicalContainedIn_Type=PhysicalIndexOrZero
_EntPhysicalContainedIn_Object=MibTableColumn
entPhysicalContainedIn=_EntPhysicalContainedIn_Object((1,3,6,1,2,1,47,1,1,1,1,4),_EntPhysicalContainedIn_Type())
entPhysicalContainedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalContainedIn.setStatus(_B)
_EntPhysicalClass_Type=IANAPhysicalClass
_EntPhysicalClass_Object=MibTableColumn
entPhysicalClass=_EntPhysicalClass_Object((1,3,6,1,2,1,47,1,1,1,1,5),_EntPhysicalClass_Type())
entPhysicalClass.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalClass.setStatus(_B)
class _EntPhysicalParentRelPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_EntPhysicalParentRelPos_Type.__name__=_J
_EntPhysicalParentRelPos_Object=MibTableColumn
entPhysicalParentRelPos=_EntPhysicalParentRelPos_Object((1,3,6,1,2,1,47,1,1,1,1,6),_EntPhysicalParentRelPos_Type())
entPhysicalParentRelPos.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalParentRelPos.setStatus(_B)
_EntPhysicalName_Type=SnmpAdminString
_EntPhysicalName_Object=MibTableColumn
entPhysicalName=_EntPhysicalName_Object((1,3,6,1,2,1,47,1,1,1,1,7),_EntPhysicalName_Type())
entPhysicalName.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalName.setStatus(_B)
_EntPhysicalHardwareRev_Type=SnmpAdminString
_EntPhysicalHardwareRev_Object=MibTableColumn
entPhysicalHardwareRev=_EntPhysicalHardwareRev_Object((1,3,6,1,2,1,47,1,1,1,1,8),_EntPhysicalHardwareRev_Type())
entPhysicalHardwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalHardwareRev.setStatus(_B)
_EntPhysicalFirmwareRev_Type=SnmpAdminString
_EntPhysicalFirmwareRev_Object=MibTableColumn
entPhysicalFirmwareRev=_EntPhysicalFirmwareRev_Object((1,3,6,1,2,1,47,1,1,1,1,9),_EntPhysicalFirmwareRev_Type())
entPhysicalFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalFirmwareRev.setStatus(_B)
_EntPhysicalSoftwareRev_Type=SnmpAdminString
_EntPhysicalSoftwareRev_Object=MibTableColumn
entPhysicalSoftwareRev=_EntPhysicalSoftwareRev_Object((1,3,6,1,2,1,47,1,1,1,1,10),_EntPhysicalSoftwareRev_Type())
entPhysicalSoftwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalSoftwareRev.setStatus(_B)
class _EntPhysicalSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EntPhysicalSerialNum_Type.__name__=_I
_EntPhysicalSerialNum_Object=MibTableColumn
entPhysicalSerialNum=_EntPhysicalSerialNum_Object((1,3,6,1,2,1,47,1,1,1,1,11),_EntPhysicalSerialNum_Type())
entPhysicalSerialNum.setMaxAccess(_L)
if mibBuilder.loadTexts:entPhysicalSerialNum.setStatus(_B)
_EntPhysicalMfgName_Type=SnmpAdminString
_EntPhysicalMfgName_Object=MibTableColumn
entPhysicalMfgName=_EntPhysicalMfgName_Object((1,3,6,1,2,1,47,1,1,1,1,12),_EntPhysicalMfgName_Type())
entPhysicalMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalMfgName.setStatus(_B)
_EntPhysicalModelName_Type=SnmpAdminString
_EntPhysicalModelName_Object=MibTableColumn
entPhysicalModelName=_EntPhysicalModelName_Object((1,3,6,1,2,1,47,1,1,1,1,13),_EntPhysicalModelName_Type())
entPhysicalModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalModelName.setStatus(_B)
class _EntPhysicalAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EntPhysicalAlias_Type.__name__=_I
_EntPhysicalAlias_Object=MibTableColumn
entPhysicalAlias=_EntPhysicalAlias_Object((1,3,6,1,2,1,47,1,1,1,1,14),_EntPhysicalAlias_Type())
entPhysicalAlias.setMaxAccess(_L)
if mibBuilder.loadTexts:entPhysicalAlias.setStatus(_B)
class _EntPhysicalAssetID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EntPhysicalAssetID_Type.__name__=_I
_EntPhysicalAssetID_Object=MibTableColumn
entPhysicalAssetID=_EntPhysicalAssetID_Object((1,3,6,1,2,1,47,1,1,1,1,15),_EntPhysicalAssetID_Type())
entPhysicalAssetID.setMaxAccess(_L)
if mibBuilder.loadTexts:entPhysicalAssetID.setStatus(_B)
_EntPhysicalIsFRU_Type=TruthValue
_EntPhysicalIsFRU_Object=MibTableColumn
entPhysicalIsFRU=_EntPhysicalIsFRU_Object((1,3,6,1,2,1,47,1,1,1,1,16),_EntPhysicalIsFRU_Type())
entPhysicalIsFRU.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalIsFRU.setStatus(_B)
_EntPhysicalMfgDate_Type=DateAndTime
_EntPhysicalMfgDate_Object=MibTableColumn
entPhysicalMfgDate=_EntPhysicalMfgDate_Object((1,3,6,1,2,1,47,1,1,1,1,17),_EntPhysicalMfgDate_Type())
entPhysicalMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalMfgDate.setStatus(_B)
_EntPhysicalUris_Type=OctetString
_EntPhysicalUris_Object=MibTableColumn
entPhysicalUris=_EntPhysicalUris_Object((1,3,6,1,2,1,47,1,1,1,1,18),_EntPhysicalUris_Type())
entPhysicalUris.setMaxAccess(_L)
if mibBuilder.loadTexts:entPhysicalUris.setStatus(_B)
_EntPhysicalUUID_Type=UUIDorZero
_EntPhysicalUUID_Object=MibTableColumn
entPhysicalUUID=_EntPhysicalUUID_Object((1,3,6,1,2,1,47,1,1,1,1,19),_EntPhysicalUUID_Type())
entPhysicalUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalUUID.setStatus(_B)
_EntityLogical_ObjectIdentity=ObjectIdentity
entityLogical=_EntityLogical_ObjectIdentity((1,3,6,1,2,1,47,1,2))
_EntLogicalTable_Object=MibTable
entLogicalTable=_EntLogicalTable_Object((1,3,6,1,2,1,47,1,2,1))
if mibBuilder.loadTexts:entLogicalTable.setStatus(_B)
_EntLogicalEntry_Object=MibTableRow
entLogicalEntry=_EntLogicalEntry_Object((1,3,6,1,2,1,47,1,2,1,1))
entLogicalEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:entLogicalEntry.setStatus(_B)
class _EntLogicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EntLogicalIndex_Type.__name__=_J
_EntLogicalIndex_Object=MibTableColumn
entLogicalIndex=_EntLogicalIndex_Object((1,3,6,1,2,1,47,1,2,1,1,1),_EntLogicalIndex_Type())
entLogicalIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:entLogicalIndex.setStatus(_B)
_EntLogicalDescr_Type=SnmpAdminString
_EntLogicalDescr_Object=MibTableColumn
entLogicalDescr=_EntLogicalDescr_Object((1,3,6,1,2,1,47,1,2,1,1,2),_EntLogicalDescr_Type())
entLogicalDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalDescr.setStatus(_B)
_EntLogicalType_Type=AutonomousType
_EntLogicalType_Object=MibTableColumn
entLogicalType=_EntLogicalType_Object((1,3,6,1,2,1,47,1,2,1,1,3),_EntLogicalType_Type())
entLogicalType.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalType.setStatus(_B)
class _EntLogicalCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EntLogicalCommunity_Type.__name__=_a
_EntLogicalCommunity_Object=MibTableColumn
entLogicalCommunity=_EntLogicalCommunity_Object((1,3,6,1,2,1,47,1,2,1,1,4),_EntLogicalCommunity_Type())
entLogicalCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalCommunity.setStatus(_D)
_EntLogicalTAddress_Type=TAddress
_EntLogicalTAddress_Object=MibTableColumn
entLogicalTAddress=_EntLogicalTAddress_Object((1,3,6,1,2,1,47,1,2,1,1,5),_EntLogicalTAddress_Type())
entLogicalTAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalTAddress.setStatus(_B)
_EntLogicalTDomain_Type=TDomain
_EntLogicalTDomain_Object=MibTableColumn
entLogicalTDomain=_EntLogicalTDomain_Object((1,3,6,1,2,1,47,1,2,1,1,6),_EntLogicalTDomain_Type())
entLogicalTDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalTDomain.setStatus(_B)
_EntLogicalContextEngineID_Type=SnmpEngineIdOrNone
_EntLogicalContextEngineID_Object=MibTableColumn
entLogicalContextEngineID=_EntLogicalContextEngineID_Object((1,3,6,1,2,1,47,1,2,1,1,7),_EntLogicalContextEngineID_Type())
entLogicalContextEngineID.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalContextEngineID.setStatus(_B)
_EntLogicalContextName_Type=SnmpAdminString
_EntLogicalContextName_Object=MibTableColumn
entLogicalContextName=_EntLogicalContextName_Object((1,3,6,1,2,1,47,1,2,1,1,8),_EntLogicalContextName_Type())
entLogicalContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:entLogicalContextName.setStatus(_B)
_EntityMapping_ObjectIdentity=ObjectIdentity
entityMapping=_EntityMapping_ObjectIdentity((1,3,6,1,2,1,47,1,3))
_EntLPMappingTable_Object=MibTable
entLPMappingTable=_EntLPMappingTable_Object((1,3,6,1,2,1,47,1,3,1))
if mibBuilder.loadTexts:entLPMappingTable.setStatus(_B)
_EntLPMappingEntry_Object=MibTableRow
entLPMappingEntry=_EntLPMappingEntry_Object((1,3,6,1,2,1,47,1,3,1,1))
entLPMappingEntry.setIndexNames((0,_A,_P),(0,_A,_Q))
if mibBuilder.loadTexts:entLPMappingEntry.setStatus(_B)
_EntLPPhysicalIndex_Type=PhysicalIndex
_EntLPPhysicalIndex_Object=MibTableColumn
entLPPhysicalIndex=_EntLPPhysicalIndex_Object((1,3,6,1,2,1,47,1,3,1,1,1),_EntLPPhysicalIndex_Type())
entLPPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:entLPPhysicalIndex.setStatus(_B)
_EntAliasMappingTable_Object=MibTable
entAliasMappingTable=_EntAliasMappingTable_Object((1,3,6,1,2,1,47,1,3,2))
if mibBuilder.loadTexts:entAliasMappingTable.setStatus(_B)
_EntAliasMappingEntry_Object=MibTableRow
entAliasMappingEntry=_EntAliasMappingEntry_Object((1,3,6,1,2,1,47,1,3,2,1))
entAliasMappingEntry.setIndexNames((0,_A,_K),(0,_A,_b))
if mibBuilder.loadTexts:entAliasMappingEntry.setStatus(_B)
class _EntAliasLogicalIndexOrZero_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EntAliasLogicalIndexOrZero_Type.__name__=_J
_EntAliasLogicalIndexOrZero_Object=MibTableColumn
entAliasLogicalIndexOrZero=_EntAliasLogicalIndexOrZero_Object((1,3,6,1,2,1,47,1,3,2,1,1),_EntAliasLogicalIndexOrZero_Type())
entAliasLogicalIndexOrZero.setMaxAccess(_O)
if mibBuilder.loadTexts:entAliasLogicalIndexOrZero.setStatus(_B)
_EntAliasMappingIdentifier_Type=RowPointer
_EntAliasMappingIdentifier_Object=MibTableColumn
entAliasMappingIdentifier=_EntAliasMappingIdentifier_Object((1,3,6,1,2,1,47,1,3,2,1,2),_EntAliasMappingIdentifier_Type())
entAliasMappingIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:entAliasMappingIdentifier.setStatus(_B)
_EntPhysicalContainsTable_Object=MibTable
entPhysicalContainsTable=_EntPhysicalContainsTable_Object((1,3,6,1,2,1,47,1,3,3))
if mibBuilder.loadTexts:entPhysicalContainsTable.setStatus(_B)
_EntPhysicalContainsEntry_Object=MibTableRow
entPhysicalContainsEntry=_EntPhysicalContainsEntry_Object((1,3,6,1,2,1,47,1,3,3,1))
entPhysicalContainsEntry.setIndexNames((0,_A,_K),(0,_A,_R))
if mibBuilder.loadTexts:entPhysicalContainsEntry.setStatus(_B)
_EntPhysicalChildIndex_Type=PhysicalIndex
_EntPhysicalChildIndex_Object=MibTableColumn
entPhysicalChildIndex=_EntPhysicalChildIndex_Object((1,3,6,1,2,1,47,1,3,3,1,1),_EntPhysicalChildIndex_Type())
entPhysicalChildIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:entPhysicalChildIndex.setStatus(_B)
_EntityGeneral_ObjectIdentity=ObjectIdentity
entityGeneral=_EntityGeneral_ObjectIdentity((1,3,6,1,2,1,47,1,4))
_EntLastChangeTime_Type=TimeStamp
_EntLastChangeTime_Object=MibScalar
entLastChangeTime=_EntLastChangeTime_Object((1,3,6,1,2,1,47,1,4,1),_EntLastChangeTime_Type())
entLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:entLastChangeTime.setStatus(_B)
_EntityMIBTraps_ObjectIdentity=ObjectIdentity
entityMIBTraps=_EntityMIBTraps_ObjectIdentity((1,3,6,1,2,1,47,2))
_EntityMIBTrapPrefix_ObjectIdentity=ObjectIdentity
entityMIBTrapPrefix=_EntityMIBTrapPrefix_ObjectIdentity((1,3,6,1,2,1,47,2,0))
_EntityConformance_ObjectIdentity=ObjectIdentity
entityConformance=_EntityConformance_ObjectIdentity((1,3,6,1,2,1,47,3))
_EntityCompliances_ObjectIdentity=ObjectIdentity
entityCompliances=_EntityCompliances_ObjectIdentity((1,3,6,1,2,1,47,3,1))
_EntityGroups_ObjectIdentity=ObjectIdentity
entityGroups=_EntityGroups_ObjectIdentity((1,3,6,1,2,1,47,3,2))
entityPhysicalGroup=ObjectGroup((1,3,6,1,2,1,47,3,2,1))
entityPhysicalGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_S),(_A,_f),(_A,_T)))
if mibBuilder.loadTexts:entityPhysicalGroup.setStatus(_B)
entityLogicalGroup=ObjectGroup((1,3,6,1,2,1,47,3,2,2))
entityLogicalGroup.setObjects(*((_A,_U),(_A,_V),(_A,_g),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:entityLogicalGroup.setStatus(_D)
entityMappingGroup=ObjectGroup((1,3,6,1,2,1,47,3,2,3))
entityMappingGroup.setObjects(*((_A,_Q),(_A,_h),(_A,_R)))
if mibBuilder.loadTexts:entityMappingGroup.setStatus(_B)
entityGeneralGroup=ObjectGroup((1,3,6,1,2,1,47,3,2,4))
entityGeneralGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:entityGeneralGroup.setStatus(_B)
entityPhysical2Group=ObjectGroup((1,3,6,1,2,1,47,3,2,6))
entityPhysical2Group.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:entityPhysical2Group.setStatus(_B)
entityLogical2Group=ObjectGroup((1,3,6,1,2,1,47,3,2,7))
entityLogical2Group.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:entityLogical2Group.setStatus(_B)
entityPhysical3Group=ObjectGroup((1,3,6,1,2,1,47,3,2,8))
entityPhysical3Group.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:entityPhysical3Group.setStatus(_B)
entityPhysical4Group=ObjectGroup((1,3,6,1,2,1,47,3,2,9))
entityPhysical4Group.setObjects((_A,_w))
if mibBuilder.loadTexts:entityPhysical4Group.setStatus(_B)
entityPhysicalCRGroup=ObjectGroup((1,3,6,1,2,1,47,3,2,10))
entityPhysicalCRGroup.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:entityPhysicalCRGroup.setStatus(_B)
entConfigChange=NotificationType((1,3,6,1,2,1,47,2,0,1))
if mibBuilder.loadTexts:entConfigChange.setStatus(_B)
entityNotificationsGroup=NotificationGroup((1,3,6,1,2,1,47,3,2,5))
entityNotificationsGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:entityNotificationsGroup.setStatus(_B)
entityCompliance=ModuleCompliance((1,3,6,1,2,1,47,3,1,1))
entityCompliance.setObjects(*((_A,_E),(_A,_y),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:entityCompliance.setStatus(_D)
entity2Compliance=ModuleCompliance((1,3,6,1,2,1,47,3,1,2))
entity2Compliance.setObjects(*((_A,_E),(_A,_M),(_A,_G),(_A,_H),(_A,_N),(_A,_F)))
if mibBuilder.loadTexts:entity2Compliance.setStatus(_D)
entity3Compliance=ModuleCompliance((1,3,6,1,2,1,47,3,1,3))
entity3Compliance.setObjects(*((_A,_E),(_A,_M),(_A,_Y),(_A,_G),(_A,_H),(_A,_N),(_A,_F)))
if mibBuilder.loadTexts:entity3Compliance.setStatus(_D)
entity4Compliance=ModuleCompliance((1,3,6,1,2,1,47,3,1,4))
entity4Compliance.setObjects(*((_A,_E),(_A,_M),(_A,_Y),(_A,_G),(_A,_H),(_A,_Z),(_A,_N),(_A,_F)))
if mibBuilder.loadTexts:entity4Compliance.setStatus(_B)
entity4CRCompliance=ModuleCompliance((1,3,6,1,2,1,47,3,1,5))
entity4CRCompliance.setObjects(*((_A,_z),(_A,_Z)))
if mibBuilder.loadTexts:entity4CRCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PhysicalIndex':PhysicalIndex,'PhysicalIndexOrZero':PhysicalIndexOrZero,'SnmpEngineIdOrNone':SnmpEngineIdOrNone,'PhysicalClass':PhysicalClass,'entityMIB':entityMIB,'entityMIBObjects':entityMIBObjects,'entityPhysical':entityPhysical,'entPhysicalTable':entPhysicalTable,'entPhysicalEntry':entPhysicalEntry,_K:entPhysicalIndex,_c:entPhysicalDescr,_d:entPhysicalVendorType,_e:entPhysicalContainedIn,_S:entPhysicalClass,_f:entPhysicalParentRelPos,_T:entPhysicalName,_j:entPhysicalHardwareRev,_k:entPhysicalFirmwareRev,_l:entPhysicalSoftwareRev,_m:entPhysicalSerialNum,_n:entPhysicalMfgName,_o:entPhysicalModelName,_p:entPhysicalAlias,_q:entPhysicalAssetID,_r:entPhysicalIsFRU,_u:entPhysicalMfgDate,_v:entPhysicalUris,_w:entPhysicalUUID,'entityLogical':entityLogical,'entLogicalTable':entLogicalTable,'entLogicalEntry':entLogicalEntry,_P:entLogicalIndex,_U:entLogicalDescr,_V:entLogicalType,_g:entLogicalCommunity,_W:entLogicalTAddress,_X:entLogicalTDomain,_s:entLogicalContextEngineID,_t:entLogicalContextName,'entityMapping':entityMapping,'entLPMappingTable':entLPMappingTable,'entLPMappingEntry':entLPMappingEntry,_Q:entLPPhysicalIndex,'entAliasMappingTable':entAliasMappingTable,'entAliasMappingEntry':entAliasMappingEntry,_b:entAliasLogicalIndexOrZero,_h:entAliasMappingIdentifier,'entPhysicalContainsTable':entPhysicalContainsTable,'entPhysicalContainsEntry':entPhysicalContainsEntry,_R:entPhysicalChildIndex,'entityGeneral':entityGeneral,_i:entLastChangeTime,'entityMIBTraps':entityMIBTraps,'entityMIBTrapPrefix':entityMIBTrapPrefix,_x:entConfigChange,'entityConformance':entityConformance,'entityCompliances':entityCompliances,'entityCompliance':entityCompliance,'entity2Compliance':entity2Compliance,'entity3Compliance':entity3Compliance,'entity4Compliance':entity4Compliance,'entity4CRCompliance':entity4CRCompliance,'entityGroups':entityGroups,_E:entityPhysicalGroup,_y:entityLogicalGroup,_F:entityMappingGroup,_G:entityGeneralGroup,_H:entityNotificationsGroup,_M:entityPhysical2Group,_N:entityLogical2Group,_Y:entityPhysical3Group,_Z:entityPhysical4Group,_z:entityPhysicalCRGroup})