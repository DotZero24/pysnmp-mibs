_e='hpEntityNotificationsGroup'
_d='hpEntityGeneralGroup'
_c='hpEntityMappingGroup'
_b='hpEntityLogicalGroup'
_a='hpEntityPhysicalGroup'
_Z='hpEntConfigChange'
_Y='hpEntLastChangeTime'
_X='hpEntAliasMappingIdentifier'
_W='hpEntLogicalTDomain'
_V='hpEntLogicalTAddress'
_U='hpEntLogicalCommunity'
_T='hpEntLogicalType'
_S='hpEntLogicalDescr'
_R='hpEntPhysicalName'
_Q='hpEntPhysicalParentRelPos'
_P='hpEntPhysicalClass'
_O='hpEntPhysicalContainedIn'
_N='hpEntPhysicalVendorType'
_M='hpEntPhysicalDescr'
_L='hpEntAliasLogicalIndexOrZero'
_K='current'
_J='OctetString'
_I='hpEntPhysicalChildIndex'
_H='hpEntLPPhysicalIndex'
_G='hpEntLogicalIndex'
_F='not-accessible'
_E='hpEntPhysicalIndex'
_D='Integer32'
_C='read-only'
_B='HP-ENTITY-MIB'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
icf,=mibBuilder.importSymbols('HP-ICF-OID','icf')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,RowPointer,TAddress,TDomain,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowPointer','TAddress','TDomain','TextualConvention','TimeStamp')
hpEntityMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,9))
if mibBuilder.loadTexts:hpEntityMIB.setRevisions(('2000-11-03 06:36','1997-03-06 03:26','1996-09-06 21:35'))
class PhysicalIndex(TextualConvention,Integer32):status=_K;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class PhysicalClass(TextualConvention,Integer32):status=_K;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('unknown',2),('chassis',3),('backplane',4),('container',5),('powerSupply',6),('fan',7),('sensor',8),('module',9),('port',10)))
_HpEntityMIBObjects_ObjectIdentity=ObjectIdentity
hpEntityMIBObjects=_HpEntityMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,1))
_HpEntityPhysical_ObjectIdentity=ObjectIdentity
hpEntityPhysical=_HpEntityPhysical_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,1,1))
_HpEntPhysicalTable_Object=MibTable
hpEntPhysicalTable=_HpEntPhysicalTable_Object((1,3,6,1,4,1,11,2,14,9,1,1,1))
if mibBuilder.loadTexts:hpEntPhysicalTable.setStatus(_A)
_HpEntPhysicalEntry_Object=MibTableRow
hpEntPhysicalEntry=_HpEntPhysicalEntry_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1))
hpEntPhysicalEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpEntPhysicalEntry.setStatus(_A)
_HpEntPhysicalIndex_Type=PhysicalIndex
_HpEntPhysicalIndex_Object=MibTableColumn
hpEntPhysicalIndex=_HpEntPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,1),_HpEntPhysicalIndex_Type())
hpEntPhysicalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEntPhysicalIndex.setStatus(_A)
_HpEntPhysicalDescr_Type=DisplayString
_HpEntPhysicalDescr_Object=MibTableColumn
hpEntPhysicalDescr=_HpEntPhysicalDescr_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,2),_HpEntPhysicalDescr_Type())
hpEntPhysicalDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalDescr.setStatus(_A)
_HpEntPhysicalVendorType_Type=AutonomousType
_HpEntPhysicalVendorType_Object=MibTableColumn
hpEntPhysicalVendorType=_HpEntPhysicalVendorType_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,3),_HpEntPhysicalVendorType_Type())
hpEntPhysicalVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalVendorType.setStatus(_A)
class _HpEntPhysicalContainedIn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpEntPhysicalContainedIn_Type.__name__=_D
_HpEntPhysicalContainedIn_Object=MibTableColumn
hpEntPhysicalContainedIn=_HpEntPhysicalContainedIn_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,4),_HpEntPhysicalContainedIn_Type())
hpEntPhysicalContainedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalContainedIn.setStatus(_A)
_HpEntPhysicalClass_Type=PhysicalClass
_HpEntPhysicalClass_Object=MibTableColumn
hpEntPhysicalClass=_HpEntPhysicalClass_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,5),_HpEntPhysicalClass_Type())
hpEntPhysicalClass.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalClass.setStatus(_A)
class _HpEntPhysicalParentRelPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_HpEntPhysicalParentRelPos_Type.__name__=_D
_HpEntPhysicalParentRelPos_Object=MibTableColumn
hpEntPhysicalParentRelPos=_HpEntPhysicalParentRelPos_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,6),_HpEntPhysicalParentRelPos_Type())
hpEntPhysicalParentRelPos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalParentRelPos.setStatus(_A)
_HpEntPhysicalName_Type=DisplayString
_HpEntPhysicalName_Object=MibTableColumn
hpEntPhysicalName=_HpEntPhysicalName_Object((1,3,6,1,4,1,11,2,14,9,1,1,1,1,7),_HpEntPhysicalName_Type())
hpEntPhysicalName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalName.setStatus(_A)
_HpEntityLogical_ObjectIdentity=ObjectIdentity
hpEntityLogical=_HpEntityLogical_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,1,2))
_HpEntLogicalTable_Object=MibTable
hpEntLogicalTable=_HpEntLogicalTable_Object((1,3,6,1,4,1,11,2,14,9,1,2,1))
if mibBuilder.loadTexts:hpEntLogicalTable.setStatus(_A)
_HpEntLogicalEntry_Object=MibTableRow
hpEntLogicalEntry=_HpEntLogicalEntry_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1))
hpEntLogicalEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpEntLogicalEntry.setStatus(_A)
class _HpEntLogicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpEntLogicalIndex_Type.__name__=_D
_HpEntLogicalIndex_Object=MibTableColumn
hpEntLogicalIndex=_HpEntLogicalIndex_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1,1),_HpEntLogicalIndex_Type())
hpEntLogicalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEntLogicalIndex.setStatus(_A)
_HpEntLogicalDescr_Type=DisplayString
_HpEntLogicalDescr_Object=MibTableColumn
hpEntLogicalDescr=_HpEntLogicalDescr_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1,2),_HpEntLogicalDescr_Type())
hpEntLogicalDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLogicalDescr.setStatus(_A)
_HpEntLogicalType_Type=AutonomousType
_HpEntLogicalType_Object=MibTableColumn
hpEntLogicalType=_HpEntLogicalType_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1,3),_HpEntLogicalType_Type())
hpEntLogicalType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLogicalType.setStatus(_A)
class _HpEntLogicalCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpEntLogicalCommunity_Type.__name__=_J
_HpEntLogicalCommunity_Object=MibTableColumn
hpEntLogicalCommunity=_HpEntLogicalCommunity_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1,4),_HpEntLogicalCommunity_Type())
hpEntLogicalCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLogicalCommunity.setStatus(_A)
_HpEntLogicalTAddress_Type=TAddress
_HpEntLogicalTAddress_Object=MibTableColumn
hpEntLogicalTAddress=_HpEntLogicalTAddress_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1,5),_HpEntLogicalTAddress_Type())
hpEntLogicalTAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLogicalTAddress.setStatus(_A)
_HpEntLogicalTDomain_Type=TDomain
_HpEntLogicalTDomain_Object=MibTableColumn
hpEntLogicalTDomain=_HpEntLogicalTDomain_Object((1,3,6,1,4,1,11,2,14,9,1,2,1,1,6),_HpEntLogicalTDomain_Type())
hpEntLogicalTDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLogicalTDomain.setStatus(_A)
_HpEntityMapping_ObjectIdentity=ObjectIdentity
hpEntityMapping=_HpEntityMapping_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,1,3))
_HpEntLPMappingTable_Object=MibTable
hpEntLPMappingTable=_HpEntLPMappingTable_Object((1,3,6,1,4,1,11,2,14,9,1,3,1))
if mibBuilder.loadTexts:hpEntLPMappingTable.setStatus(_A)
_HpEntLPMappingEntry_Object=MibTableRow
hpEntLPMappingEntry=_HpEntLPMappingEntry_Object((1,3,6,1,4,1,11,2,14,9,1,3,1,1))
hpEntLPMappingEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpEntLPMappingEntry.setStatus(_A)
_HpEntLPPhysicalIndex_Type=PhysicalIndex
_HpEntLPPhysicalIndex_Object=MibTableColumn
hpEntLPPhysicalIndex=_HpEntLPPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,9,1,3,1,1,1),_HpEntLPPhysicalIndex_Type())
hpEntLPPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLPPhysicalIndex.setStatus(_A)
_HpEntAliasMappingTable_Object=MibTable
hpEntAliasMappingTable=_HpEntAliasMappingTable_Object((1,3,6,1,4,1,11,2,14,9,1,3,2))
if mibBuilder.loadTexts:hpEntAliasMappingTable.setStatus(_A)
_HpEntAliasMappingEntry_Object=MibTableRow
hpEntAliasMappingEntry=_HpEntAliasMappingEntry_Object((1,3,6,1,4,1,11,2,14,9,1,3,2,1))
hpEntAliasMappingEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:hpEntAliasMappingEntry.setStatus(_A)
class _HpEntAliasLogicalIndexOrZero_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpEntAliasLogicalIndexOrZero_Type.__name__=_D
_HpEntAliasLogicalIndexOrZero_Object=MibTableColumn
hpEntAliasLogicalIndexOrZero=_HpEntAliasLogicalIndexOrZero_Object((1,3,6,1,4,1,11,2,14,9,1,3,2,1,1),_HpEntAliasLogicalIndexOrZero_Type())
hpEntAliasLogicalIndexOrZero.setMaxAccess(_F)
if mibBuilder.loadTexts:hpEntAliasLogicalIndexOrZero.setStatus(_A)
_HpEntAliasMappingIdentifier_Type=RowPointer
_HpEntAliasMappingIdentifier_Object=MibTableColumn
hpEntAliasMappingIdentifier=_HpEntAliasMappingIdentifier_Object((1,3,6,1,4,1,11,2,14,9,1,3,2,1,2),_HpEntAliasMappingIdentifier_Type())
hpEntAliasMappingIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntAliasMappingIdentifier.setStatus(_A)
_HpEntPhysicalContainsTable_Object=MibTable
hpEntPhysicalContainsTable=_HpEntPhysicalContainsTable_Object((1,3,6,1,4,1,11,2,14,9,1,3,3))
if mibBuilder.loadTexts:hpEntPhysicalContainsTable.setStatus(_A)
_HpEntPhysicalContainsEntry_Object=MibTableRow
hpEntPhysicalContainsEntry=_HpEntPhysicalContainsEntry_Object((1,3,6,1,4,1,11,2,14,9,1,3,3,1))
hpEntPhysicalContainsEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:hpEntPhysicalContainsEntry.setStatus(_A)
_HpEntPhysicalChildIndex_Type=PhysicalIndex
_HpEntPhysicalChildIndex_Object=MibTableColumn
hpEntPhysicalChildIndex=_HpEntPhysicalChildIndex_Object((1,3,6,1,4,1,11,2,14,9,1,3,3,1,1),_HpEntPhysicalChildIndex_Type())
hpEntPhysicalChildIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntPhysicalChildIndex.setStatus(_A)
_HpEntityGeneral_ObjectIdentity=ObjectIdentity
hpEntityGeneral=_HpEntityGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,1,4))
_HpEntLastChangeTime_Type=TimeStamp
_HpEntLastChangeTime_Object=MibScalar
hpEntLastChangeTime=_HpEntLastChangeTime_Object((1,3,6,1,4,1,11,2,14,9,1,4,1),_HpEntLastChangeTime_Type())
hpEntLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpEntLastChangeTime.setStatus(_A)
_HpEntityMIBTraps_ObjectIdentity=ObjectIdentity
hpEntityMIBTraps=_HpEntityMIBTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,2))
_HpEntityMIBTrapPrefix_ObjectIdentity=ObjectIdentity
hpEntityMIBTrapPrefix=_HpEntityMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,2,0))
_HpEntityConformance_ObjectIdentity=ObjectIdentity
hpEntityConformance=_HpEntityConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,3))
_HpEntityCompliances_ObjectIdentity=ObjectIdentity
hpEntityCompliances=_HpEntityCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,3,1))
_HpEntityGroups_ObjectIdentity=ObjectIdentity
hpEntityGroups=_HpEntityGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,9,3,2))
hpEntityPhysicalGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,9,3,2,1))
hpEntityPhysicalGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpEntityPhysicalGroup.setStatus(_A)
hpEntityLogicalGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,9,3,2,2))
hpEntityLogicalGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpEntityLogicalGroup.setStatus(_A)
hpEntityMappingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,9,3,2,3))
hpEntityMappingGroup.setObjects(*((_B,_H),(_B,_X),(_B,_I)))
if mibBuilder.loadTexts:hpEntityMappingGroup.setStatus(_A)
hpEntityGeneralGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,9,3,2,4))
hpEntityGeneralGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:hpEntityGeneralGroup.setStatus(_A)
hpEntConfigChange=NotificationType((1,3,6,1,4,1,11,2,14,9,2,0,1))
if mibBuilder.loadTexts:hpEntConfigChange.setStatus(_A)
hpEntityNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,9,3,2,5))
hpEntityNotificationsGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:hpEntityNotificationsGroup.setStatus(_A)
hpEntityCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,9,3,1,1))
hpEntityCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:hpEntityCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PhysicalIndex':PhysicalIndex,'PhysicalClass':PhysicalClass,'hpEntityMIB':hpEntityMIB,'hpEntityMIBObjects':hpEntityMIBObjects,'hpEntityPhysical':hpEntityPhysical,'hpEntPhysicalTable':hpEntPhysicalTable,'hpEntPhysicalEntry':hpEntPhysicalEntry,_E:hpEntPhysicalIndex,_M:hpEntPhysicalDescr,_N:hpEntPhysicalVendorType,_O:hpEntPhysicalContainedIn,_P:hpEntPhysicalClass,_Q:hpEntPhysicalParentRelPos,_R:hpEntPhysicalName,'hpEntityLogical':hpEntityLogical,'hpEntLogicalTable':hpEntLogicalTable,'hpEntLogicalEntry':hpEntLogicalEntry,_G:hpEntLogicalIndex,_S:hpEntLogicalDescr,_T:hpEntLogicalType,_U:hpEntLogicalCommunity,_V:hpEntLogicalTAddress,_W:hpEntLogicalTDomain,'hpEntityMapping':hpEntityMapping,'hpEntLPMappingTable':hpEntLPMappingTable,'hpEntLPMappingEntry':hpEntLPMappingEntry,_H:hpEntLPPhysicalIndex,'hpEntAliasMappingTable':hpEntAliasMappingTable,'hpEntAliasMappingEntry':hpEntAliasMappingEntry,_L:hpEntAliasLogicalIndexOrZero,_X:hpEntAliasMappingIdentifier,'hpEntPhysicalContainsTable':hpEntPhysicalContainsTable,'hpEntPhysicalContainsEntry':hpEntPhysicalContainsEntry,_I:hpEntPhysicalChildIndex,'hpEntityGeneral':hpEntityGeneral,_Y:hpEntLastChangeTime,'hpEntityMIBTraps':hpEntityMIBTraps,'hpEntityMIBTrapPrefix':hpEntityMIBTrapPrefix,_Z:hpEntConfigChange,'hpEntityConformance':hpEntityConformance,'hpEntityCompliances':hpEntityCompliances,'hpEntityCompliance':hpEntityCompliance,'hpEntityGroups':hpEntityGroups,_a:hpEntityPhysicalGroup,_b:hpEntityLogicalGroup,_c:hpEntityMappingGroup,_d:hpEntityGeneralGroup,_e:hpEntityNotificationsGroup})