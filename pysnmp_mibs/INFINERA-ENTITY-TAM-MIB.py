_I='tamGroup'
_H='tamRowStatus'
_G='tamProvEqptType'
_F='tamMoId'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-TAM-MIB'
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
tamMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,7))
_TamTable_Object=MibTable
tamTable=_TamTable_Object((1,3,6,1,4,1,21296,2,2,2,1,7,1))
if mibBuilder.loadTexts:tamTable.setStatus(_A)
_TamEntry_Object=MibTableRow
tamEntry=_TamEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,7,1,1))
tamEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tamEntry.setStatus(_A)
_TamMoId_Type=DisplayString
_TamMoId_Object=MibTableColumn
tamMoId=_TamMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,7,1,1,1),_TamMoId_Type())
tamMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:tamMoId.setStatus(_A)
_TamProvEqptType_Type=InfnEqptType
_TamProvEqptType_Object=MibTableColumn
tamProvEqptType=_TamProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,7,1,1,2),_TamProvEqptType_Type())
tamProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:tamProvEqptType.setStatus(_A)
_TamRowStatus_Type=RowStatus
_TamRowStatus_Object=MibTableColumn
tamRowStatus=_TamRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,7,1,1,3),_TamRowStatus_Type())
tamRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tamRowStatus.setStatus(_A)
_TamConformance_ObjectIdentity=ObjectIdentity
tamConformance=_TamConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,7,3))
_TamCompliances_ObjectIdentity=ObjectIdentity
tamCompliances=_TamCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,7,3,1))
_TamGroups_ObjectIdentity=ObjectIdentity
tamGroups=_TamGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,7,3,2))
tamGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,7,3,2,1))
tamGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:tamGroup.setStatus(_A)
tamCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,7,3,1,1))
tamCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:tamCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tamMIB':tamMIB,'tamTable':tamTable,'tamEntry':tamEntry,_F:tamMoId,_G:tamProvEqptType,_H:tamRowStatus,'tamConformance':tamConformance,'tamCompliances':tamCompliances,'tamCompliance':tamCompliance,'tamGroups':tamGroups,_I:tamGroup})