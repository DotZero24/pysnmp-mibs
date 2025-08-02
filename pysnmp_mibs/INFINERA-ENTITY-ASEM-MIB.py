_H='asemGroup'
_G='asemProvEqptType'
_F='asemMoId'
_E='read-write'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-ASEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
asemMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,56))
_AsemTable_Object=MibTable
asemTable=_AsemTable_Object((1,3,6,1,4,1,21296,2,2,2,1,56,1))
if mibBuilder.loadTexts:asemTable.setStatus(_A)
_AsemEntry_Object=MibTableRow
asemEntry=_AsemEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,56,1,1))
asemEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:asemEntry.setStatus(_A)
_AsemMoId_Type=DisplayString
_AsemMoId_Object=MibTableColumn
asemMoId=_AsemMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,56,1,1,1),_AsemMoId_Type())
asemMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:asemMoId.setStatus(_A)
_AsemProvEqptType_Type=InfnEqptType
_AsemProvEqptType_Object=MibTableColumn
asemProvEqptType=_AsemProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,56,1,1,2),_AsemProvEqptType_Type())
asemProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:asemProvEqptType.setStatus(_A)
_AsemConformance_ObjectIdentity=ObjectIdentity
asemConformance=_AsemConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,56,3))
_AsemCompliances_ObjectIdentity=ObjectIdentity
asemCompliances=_AsemCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,56,3,1))
_AsemGroups_ObjectIdentity=ObjectIdentity
asemGroups=_AsemGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,56,3,2))
asemGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,56,3,2,1))
asemGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:asemGroup.setStatus(_A)
asemCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,56,3,1,1))
asemCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:asemCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'asemMIB':asemMIB,'asemTable':asemTable,'asemEntry':asemEntry,_F:asemMoId,_G:asemProvEqptType,'asemConformance':asemConformance,'asemCompliances':asemCompliances,'asemCompliance':asemCompliance,'asemGroups':asemGroups,_H:asemGroup})