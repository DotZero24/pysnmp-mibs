_J='aosCoreConditionObjectGroup'
_I='aosCoreConditionTimestamp'
_H='aosCoreConditionDescr'
_G='aosCoreConditionEntity'
_F='aosCoreConditionEntityTranslation'
_E='aosCoreConditionType'
_D='aosCoreConditionIndex'
_C='read-only'
_B='AOS-CORE-CONDITION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aosCommon,=mibBuilder.importSymbols('ADVA-MIB','aosCommon')
ConditionDescr,ConditionEntityTranslation,ConditionType=mibBuilder.importSymbols('AOS-CORE-ALARM-MIB','ConditionDescr','ConditionEntityTranslation','ConditionType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
aosCoreConditionMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,20,1,2))
if mibBuilder.loadTexts:aosCoreConditionMIB.setRevisions(('2015-10-23 00:00',))
_ConditionObjects_ObjectIdentity=ObjectIdentity
conditionObjects=_ConditionObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,2,1))
_AosCoreConditionTable_Object=MibTable
aosCoreConditionTable=_AosCoreConditionTable_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1))
if mibBuilder.loadTexts:aosCoreConditionTable.setStatus(_A)
_AosCoreConditionEntry_Object=MibTableRow
aosCoreConditionEntry=_AosCoreConditionEntry_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1))
aosCoreConditionEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:aosCoreConditionEntry.setStatus(_A)
_AosCoreConditionIndex_Type=Integer32
_AosCoreConditionIndex_Object=MibTableColumn
aosCoreConditionIndex=_AosCoreConditionIndex_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1,1),_AosCoreConditionIndex_Type())
aosCoreConditionIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:aosCoreConditionIndex.setStatus(_A)
_AosCoreConditionType_Type=ConditionType
_AosCoreConditionType_Object=MibTableColumn
aosCoreConditionType=_AosCoreConditionType_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1,2),_AosCoreConditionType_Type())
aosCoreConditionType.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreConditionType.setStatus(_A)
_AosCoreConditionEntityTranslation_Type=ConditionEntityTranslation
_AosCoreConditionEntityTranslation_Object=MibTableColumn
aosCoreConditionEntityTranslation=_AosCoreConditionEntityTranslation_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1,3),_AosCoreConditionEntityTranslation_Type())
aosCoreConditionEntityTranslation.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreConditionEntityTranslation.setStatus(_A)
_AosCoreConditionEntity_Type=RowPointer
_AosCoreConditionEntity_Object=MibTableColumn
aosCoreConditionEntity=_AosCoreConditionEntity_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1,4),_AosCoreConditionEntity_Type())
aosCoreConditionEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreConditionEntity.setStatus(_A)
_AosCoreConditionDescr_Type=ConditionDescr
_AosCoreConditionDescr_Object=MibTableColumn
aosCoreConditionDescr=_AosCoreConditionDescr_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1,5),_AosCoreConditionDescr_Type())
aosCoreConditionDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreConditionDescr.setStatus(_A)
_AosCoreConditionTimestamp_Type=DisplayString
_AosCoreConditionTimestamp_Object=MibTableColumn
aosCoreConditionTimestamp=_AosCoreConditionTimestamp_Object((1,3,6,1,4,1,2544,1,20,1,2,1,1,1,6),_AosCoreConditionTimestamp_Type())
aosCoreConditionTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:aosCoreConditionTimestamp.setStatus(_A)
_ConditionConformance_ObjectIdentity=ObjectIdentity
conditionConformance=_ConditionConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,2,2))
_AosCoreConditionCompliances_ObjectIdentity=ObjectIdentity
aosCoreConditionCompliances=_AosCoreConditionCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,2,2,1))
_AosCoreConditionGroups_ObjectIdentity=ObjectIdentity
aosCoreConditionGroups=_AosCoreConditionGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,20,1,2,2,2))
aosCoreConditionObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,20,1,2,2,2,1))
aosCoreConditionObjectGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:aosCoreConditionObjectGroup.setStatus(_A)
aosCoreConditionCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,20,1,2,2,1,1))
aosCoreConditionCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:aosCoreConditionCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aosCoreConditionMIB':aosCoreConditionMIB,'conditionObjects':conditionObjects,'aosCoreConditionTable':aosCoreConditionTable,'aosCoreConditionEntry':aosCoreConditionEntry,_D:aosCoreConditionIndex,_E:aosCoreConditionType,_F:aosCoreConditionEntityTranslation,_G:aosCoreConditionEntity,_H:aosCoreConditionDescr,_I:aosCoreConditionTimestamp,'conditionConformance':conditionConformance,'aosCoreConditionCompliances':aosCoreConditionCompliances,'aosCoreConditionCompliance':aosCoreConditionCompliance,'aosCoreConditionGroups':aosCoreConditionGroups,_J:aosCoreConditionObjectGroup})