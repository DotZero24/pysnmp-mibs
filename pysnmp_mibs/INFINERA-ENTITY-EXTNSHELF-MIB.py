_I='extnShelfGroup'
_H='extnShelfProvSerialNumber'
_G='extnShelfProvEqptType'
_F='extnShelfMoId'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-EXTNSHELF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
extnShelfMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,53))
_ExtnShelfTable_Object=MibTable
extnShelfTable=_ExtnShelfTable_Object((1,3,6,1,4,1,21296,2,2,2,1,53,1))
if mibBuilder.loadTexts:extnShelfTable.setStatus(_A)
_ExtnShelfEntry_Object=MibTableRow
extnShelfEntry=_ExtnShelfEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,53,1,1))
extnShelfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extnShelfEntry.setStatus(_A)
_ExtnShelfMoId_Type=DisplayString
_ExtnShelfMoId_Object=MibTableColumn
extnShelfMoId=_ExtnShelfMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,53,1,1,1),_ExtnShelfMoId_Type())
extnShelfMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:extnShelfMoId.setStatus(_A)
_ExtnShelfProvEqptType_Type=InfnEqptType
_ExtnShelfProvEqptType_Object=MibTableColumn
extnShelfProvEqptType=_ExtnShelfProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,53,1,1,2),_ExtnShelfProvEqptType_Type())
extnShelfProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:extnShelfProvEqptType.setStatus(_A)
_ExtnShelfProvSerialNumber_Type=DisplayString
_ExtnShelfProvSerialNumber_Object=MibTableColumn
extnShelfProvSerialNumber=_ExtnShelfProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,53,1,1,3),_ExtnShelfProvSerialNumber_Type())
extnShelfProvSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:extnShelfProvSerialNumber.setStatus(_A)
_ExtnShelfConformance_ObjectIdentity=ObjectIdentity
extnShelfConformance=_ExtnShelfConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,53,3))
_ExtnShelfCompliances_ObjectIdentity=ObjectIdentity
extnShelfCompliances=_ExtnShelfCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,53,3,1))
_ExtnShelfGroups_ObjectIdentity=ObjectIdentity
extnShelfGroups=_ExtnShelfGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,53,3,2))
extnShelfGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,53,3,2,1))
extnShelfGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:extnShelfGroup.setStatus(_A)
extnShelfCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,53,3,1,1))
extnShelfCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:extnShelfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extnShelfMIB':extnShelfMIB,'extnShelfTable':extnShelfTable,'extnShelfEntry':extnShelfEntry,_F:extnShelfMoId,_G:extnShelfProvEqptType,_H:extnShelfProvSerialNumber,'extnShelfConformance':extnShelfConformance,'extnShelfCompliances':extnShelfCompliances,'extnShelfCompliance':extnShelfCompliance,'extnShelfGroups':extnShelfGroups,_I:extnShelfGroup})