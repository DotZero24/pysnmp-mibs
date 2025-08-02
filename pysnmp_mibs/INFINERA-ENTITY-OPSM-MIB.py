_I='opsmGroup'
_H='opsmNodeId'
_G='opsmProvEqptType'
_F='opsmMoId'
_E='read-write'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-OPSM-MIB'
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
opsmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,43))
_OpsmTable_Object=MibTable
opsmTable=_OpsmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,43,1))
if mibBuilder.loadTexts:opsmTable.setStatus(_A)
_OpsmEntry_Object=MibTableRow
opsmEntry=_OpsmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,43,1,1))
opsmEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:opsmEntry.setStatus(_A)
_OpsmMoId_Type=DisplayString
_OpsmMoId_Object=MibTableColumn
opsmMoId=_OpsmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,43,1,1,1),_OpsmMoId_Type())
opsmMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:opsmMoId.setStatus(_A)
_OpsmProvEqptType_Type=InfnEqptType
_OpsmProvEqptType_Object=MibTableColumn
opsmProvEqptType=_OpsmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,43,1,1,2),_OpsmProvEqptType_Type())
opsmProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:opsmProvEqptType.setStatus(_A)
_OpsmNodeId_Type=DisplayString
_OpsmNodeId_Object=MibTableColumn
opsmNodeId=_OpsmNodeId_Object((1,3,6,1,4,1,21296,2,2,2,1,43,1,1,3),_OpsmNodeId_Type())
opsmNodeId.setMaxAccess('read-only')
if mibBuilder.loadTexts:opsmNodeId.setStatus(_A)
_OpsmConformance_ObjectIdentity=ObjectIdentity
opsmConformance=_OpsmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,43,3))
_OpsmCompliances_ObjectIdentity=ObjectIdentity
opsmCompliances=_OpsmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,43,3,1))
_OpsmGroups_ObjectIdentity=ObjectIdentity
opsmGroups=_OpsmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,43,3,2))
opsmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,43,3,2,1))
opsmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:opsmGroup.setStatus(_A)
opsmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,43,3,1,1))
opsmCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:opsmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'opsmMIB':opsmMIB,'opsmTable':opsmTable,'opsmEntry':opsmEntry,_F:opsmMoId,_G:opsmProvEqptType,_H:opsmNodeId,'opsmConformance':opsmConformance,'opsmCompliances':opsmCompliances,'opsmCompliance':opsmCompliance,'opsmGroups':opsmGroups,_I:opsmGroup})