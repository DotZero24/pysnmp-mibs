_H='otdmGroup'
_G='otdmProvEqptType'
_F='otdmMoId'
_E='read-write'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-OTDM-MIB'
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
otdmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,46))
_OtdmTable_Object=MibTable
otdmTable=_OtdmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,46,1))
if mibBuilder.loadTexts:otdmTable.setStatus(_A)
_OtdmEntry_Object=MibTableRow
otdmEntry=_OtdmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,46,1,1))
otdmEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:otdmEntry.setStatus(_A)
_OtdmMoId_Type=DisplayString
_OtdmMoId_Object=MibTableColumn
otdmMoId=_OtdmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,46,1,1,1),_OtdmMoId_Type())
otdmMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:otdmMoId.setStatus(_A)
_OtdmProvEqptType_Type=InfnEqptType
_OtdmProvEqptType_Object=MibTableColumn
otdmProvEqptType=_OtdmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,46,1,1,2),_OtdmProvEqptType_Type())
otdmProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:otdmProvEqptType.setStatus(_A)
_OtdmConformance_ObjectIdentity=ObjectIdentity
otdmConformance=_OtdmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,46,3))
_OtdmCompliances_ObjectIdentity=ObjectIdentity
otdmCompliances=_OtdmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,46,3,1))
_OtdmGroups_ObjectIdentity=ObjectIdentity
otdmGroups=_OtdmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,46,3,2))
otdmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,46,3,2,1))
otdmGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:otdmGroup.setStatus(_A)
otdmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,46,3,1,1))
otdmCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:otdmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otdmMIB':otdmMIB,'otdmTable':otdmTable,'otdmEntry':otdmEntry,_F:otdmMoId,_G:otdmProvEqptType,'otdmConformance':otdmConformance,'otdmCompliances':otdmCompliances,'otdmCompliance':otdmCompliance,'otdmGroups':otdmGroups,_H:otdmGroup})