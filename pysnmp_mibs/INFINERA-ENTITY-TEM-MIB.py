_I='temGroup'
_H='temRowStatus'
_G='temProvEqptType'
_F='temMoId'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-TEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
temMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,6))
_TemTable_Object=MibTable
temTable=_TemTable_Object((1,3,6,1,4,1,21296,2,2,2,1,6,1))
if mibBuilder.loadTexts:temTable.setStatus(_A)
_TemEntry_Object=MibTableRow
temEntry=_TemEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,6,1,1))
temEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:temEntry.setStatus(_A)
_TemMoId_Type=DisplayString
_TemMoId_Object=MibTableColumn
temMoId=_TemMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,6,1,1,1),_TemMoId_Type())
temMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:temMoId.setStatus(_A)
_TemProvEqptType_Type=InfnEqptType
_TemProvEqptType_Object=MibTableColumn
temProvEqptType=_TemProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,6,1,1,2),_TemProvEqptType_Type())
temProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:temProvEqptType.setStatus(_A)
_TemRowStatus_Type=RowStatus
_TemRowStatus_Object=MibTableColumn
temRowStatus=_TemRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,6,1,1,3),_TemRowStatus_Type())
temRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:temRowStatus.setStatus(_A)
_TemConformance_ObjectIdentity=ObjectIdentity
temConformance=_TemConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,6,3))
_TemCompliances_ObjectIdentity=ObjectIdentity
temCompliances=_TemCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,6,3,1))
_TemGroups_ObjectIdentity=ObjectIdentity
temGroups=_TemGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,6,3,2))
temGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,6,3,2,1))
temGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:temGroup.setStatus(_A)
temCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,6,3,1,1))
temCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:temCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'temMIB':temMIB,'temTable':temTable,'temEntry':temEntry,_F:temMoId,_G:temProvEqptType,_H:temRowStatus,'temConformance':temConformance,'temCompliances':temCompliances,'temCompliance':temCompliance,'temGroups':temGroups,_I:temGroup})