_R='hm2NetobjGeneralGroup'
_Q='hm2NetobjectsDataTableRowStatus'
_P='hm2NetobjectsDataTableData'
_O='hm2NetobjectsDataTableObjIndex'
_N='hm2NetobjectsDataTableEntriesCount'
_M='hm2NetobjectsRowStatus'
_L='hm2NetobjectsDataEntriesCount'
_K='hm2NetobjectsCount'
_J='hm2NetobjectsName'
_I='hm2NetobjectsDataTableIndex'
_H='not-accessible'
_G='hm2NetobjectsIndex'
_F='read-only'
_E='DisplayString'
_D='read-create'
_C='Integer32'
_B='HM2-NETOBJ-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
hm2NetobjMib=ModuleIdentity((1,3,6,1,4,1,248,11,60))
if mibBuilder.loadTexts:hm2NetobjMib.setRevisions(('2011-10-20 00:00','2011-07-01 00:00','2011-05-31 00:00'))
_Hm2NetobjNotifications_ObjectIdentity=ObjectIdentity
hm2NetobjNotifications=_Hm2NetobjNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,60,0))
_Hm2NetobjObjects_ObjectIdentity=ObjectIdentity
hm2NetobjObjects=_Hm2NetobjObjects_ObjectIdentity((1,3,6,1,4,1,248,11,60,1))
_Hm2NetobjectsObjects_ObjectIdentity=ObjectIdentity
hm2NetobjectsObjects=_Hm2NetobjectsObjects_ObjectIdentity((1,3,6,1,4,1,248,11,60,1,1))
class _Hm2NetobjectsCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Hm2NetobjectsCount_Type.__name__=_C
_Hm2NetobjectsCount_Object=MibScalar
hm2NetobjectsCount=_Hm2NetobjectsCount_Object((1,3,6,1,4,1,248,11,60,1,1,1),_Hm2NetobjectsCount_Type())
hm2NetobjectsCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2NetobjectsCount.setStatus(_A)
_Hm2NetobjectsDataTableEntriesCount_Type=Integer32
_Hm2NetobjectsDataTableEntriesCount_Object=MibScalar
hm2NetobjectsDataTableEntriesCount=_Hm2NetobjectsDataTableEntriesCount_Object((1,3,6,1,4,1,248,11,60,1,1,2),_Hm2NetobjectsDataTableEntriesCount_Type())
hm2NetobjectsDataTableEntriesCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2NetobjectsDataTableEntriesCount.setStatus(_A)
_Hm2NetobjectsTables_ObjectIdentity=ObjectIdentity
hm2NetobjectsTables=_Hm2NetobjectsTables_ObjectIdentity((1,3,6,1,4,1,248,11,60,1,2))
_Hm2NetobjectsTable_Object=MibTable
hm2NetobjectsTable=_Hm2NetobjectsTable_Object((1,3,6,1,4,1,248,11,60,1,2,1))
if mibBuilder.loadTexts:hm2NetobjectsTable.setStatus(_A)
_Hm2NetobjectsTableEntry_Object=MibTableRow
hm2NetobjectsTableEntry=_Hm2NetobjectsTableEntry_Object((1,3,6,1,4,1,248,11,60,1,2,1,1))
hm2NetobjectsTableEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hm2NetobjectsTableEntry.setStatus(_A)
class _Hm2NetobjectsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Hm2NetobjectsIndex_Type.__name__=_C
_Hm2NetobjectsIndex_Object=MibTableColumn
hm2NetobjectsIndex=_Hm2NetobjectsIndex_Object((1,3,6,1,4,1,248,11,60,1,2,1,1,1),_Hm2NetobjectsIndex_Type())
hm2NetobjectsIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2NetobjectsIndex.setStatus(_A)
class _Hm2NetobjectsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_Hm2NetobjectsName_Type.__name__=_E
_Hm2NetobjectsName_Object=MibTableColumn
hm2NetobjectsName=_Hm2NetobjectsName_Object((1,3,6,1,4,1,248,11,60,1,2,1,1,2),_Hm2NetobjectsName_Type())
hm2NetobjectsName.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NetobjectsName.setStatus(_A)
_Hm2NetobjectsDataEntriesCount_Type=Integer32
_Hm2NetobjectsDataEntriesCount_Object=MibTableColumn
hm2NetobjectsDataEntriesCount=_Hm2NetobjectsDataEntriesCount_Object((1,3,6,1,4,1,248,11,60,1,2,1,1,3),_Hm2NetobjectsDataEntriesCount_Type())
hm2NetobjectsDataEntriesCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2NetobjectsDataEntriesCount.setStatus(_A)
_Hm2NetobjectsRowStatus_Type=RowStatus
_Hm2NetobjectsRowStatus_Object=MibTableColumn
hm2NetobjectsRowStatus=_Hm2NetobjectsRowStatus_Object((1,3,6,1,4,1,248,11,60,1,2,1,1,4),_Hm2NetobjectsRowStatus_Type())
hm2NetobjectsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NetobjectsRowStatus.setStatus(_A)
_Hm2NetobjectsDataTable_Object=MibTable
hm2NetobjectsDataTable=_Hm2NetobjectsDataTable_Object((1,3,6,1,4,1,248,11,60,1,2,2))
if mibBuilder.loadTexts:hm2NetobjectsDataTable.setStatus(_A)
_Hm2NetobjectsDataTableEntry_Object=MibTableRow
hm2NetobjectsDataTableEntry=_Hm2NetobjectsDataTableEntry_Object((1,3,6,1,4,1,248,11,60,1,2,2,1))
hm2NetobjectsDataTableEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hm2NetobjectsDataTableEntry.setStatus(_A)
class _Hm2NetobjectsDataTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Hm2NetobjectsDataTableIndex_Type.__name__=_C
_Hm2NetobjectsDataTableIndex_Object=MibTableColumn
hm2NetobjectsDataTableIndex=_Hm2NetobjectsDataTableIndex_Object((1,3,6,1,4,1,248,11,60,1,2,2,1,1),_Hm2NetobjectsDataTableIndex_Type())
hm2NetobjectsDataTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2NetobjectsDataTableIndex.setStatus(_A)
class _Hm2NetobjectsDataTableObjIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_Hm2NetobjectsDataTableObjIndex_Type.__name__=_C
_Hm2NetobjectsDataTableObjIndex_Object=MibTableColumn
hm2NetobjectsDataTableObjIndex=_Hm2NetobjectsDataTableObjIndex_Object((1,3,6,1,4,1,248,11,60,1,2,2,1,2),_Hm2NetobjectsDataTableObjIndex_Type())
hm2NetobjectsDataTableObjIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NetobjectsDataTableObjIndex.setStatus(_A)
class _Hm2NetobjectsDataTableData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_Hm2NetobjectsDataTableData_Type.__name__=_E
_Hm2NetobjectsDataTableData_Object=MibTableColumn
hm2NetobjectsDataTableData=_Hm2NetobjectsDataTableData_Object((1,3,6,1,4,1,248,11,60,1,2,2,1,3),_Hm2NetobjectsDataTableData_Type())
hm2NetobjectsDataTableData.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NetobjectsDataTableData.setStatus(_A)
_Hm2NetobjectsDataTableRowStatus_Type=RowStatus
_Hm2NetobjectsDataTableRowStatus_Object=MibTableColumn
hm2NetobjectsDataTableRowStatus=_Hm2NetobjectsDataTableRowStatus_Object((1,3,6,1,4,1,248,11,60,1,2,2,1,4),_Hm2NetobjectsDataTableRowStatus_Type())
hm2NetobjectsDataTableRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NetobjectsDataTableRowStatus.setStatus(_A)
_Hm2NetobjConformance_ObjectIdentity=ObjectIdentity
hm2NetobjConformance=_Hm2NetobjConformance_ObjectIdentity((1,3,6,1,4,1,248,11,60,2))
_Hm2NetobjCompliances_ObjectIdentity=ObjectIdentity
hm2NetobjCompliances=_Hm2NetobjCompliances_ObjectIdentity((1,3,6,1,4,1,248,11,60,2,1))
_Hm2NetobjGroups_ObjectIdentity=ObjectIdentity
hm2NetobjGroups=_Hm2NetobjGroups_ObjectIdentity((1,3,6,1,4,1,248,11,60,2,2))
hm2NetobjGeneralGroup=ObjectGroup((1,3,6,1,4,1,248,11,60,2,2,1))
hm2NetobjGeneralGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hm2NetobjGeneralGroup.setStatus(_A)
hm2NetobjCompliance=ModuleCompliance((1,3,6,1,4,1,248,11,60,2,1,1))
hm2NetobjCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:hm2NetobjCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hm2NetobjMib':hm2NetobjMib,'hm2NetobjNotifications':hm2NetobjNotifications,'hm2NetobjObjects':hm2NetobjObjects,'hm2NetobjectsObjects':hm2NetobjectsObjects,_K:hm2NetobjectsCount,_N:hm2NetobjectsDataTableEntriesCount,'hm2NetobjectsTables':hm2NetobjectsTables,'hm2NetobjectsTable':hm2NetobjectsTable,'hm2NetobjectsTableEntry':hm2NetobjectsTableEntry,_G:hm2NetobjectsIndex,_J:hm2NetobjectsName,_L:hm2NetobjectsDataEntriesCount,_M:hm2NetobjectsRowStatus,'hm2NetobjectsDataTable':hm2NetobjectsDataTable,'hm2NetobjectsDataTableEntry':hm2NetobjectsDataTableEntry,_I:hm2NetobjectsDataTableIndex,_O:hm2NetobjectsDataTableObjIndex,_P:hm2NetobjectsDataTableData,_Q:hm2NetobjectsDataTableRowStatus,'hm2NetobjConformance':hm2NetobjConformance,'hm2NetobjCompliances':hm2NetobjCompliances,'hm2NetobjCompliance':hm2NetobjCompliance,'hm2NetobjGroups':hm2NetobjGroups,_R:hm2NetobjGeneralGroup})