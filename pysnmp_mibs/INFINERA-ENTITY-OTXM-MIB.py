_I='otxmGroup'
_H='otxmRowStatus'
_G='otxmProvEqptType'
_F='otxmMoId'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-OTXM-MIB'
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
otxmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,32))
_OtxmTable_Object=MibTable
otxmTable=_OtxmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,32,1))
if mibBuilder.loadTexts:otxmTable.setStatus(_A)
_OtxmEntry_Object=MibTableRow
otxmEntry=_OtxmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,32,1,1))
otxmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:otxmEntry.setStatus(_A)
_OtxmMoId_Type=DisplayString
_OtxmMoId_Object=MibTableColumn
otxmMoId=_OtxmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,32,1,1,1),_OtxmMoId_Type())
otxmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:otxmMoId.setStatus(_A)
_OtxmProvEqptType_Type=InfnEqptType
_OtxmProvEqptType_Object=MibTableColumn
otxmProvEqptType=_OtxmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,32,1,1,2),_OtxmProvEqptType_Type())
otxmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:otxmProvEqptType.setStatus(_A)
_OtxmRowStatus_Type=RowStatus
_OtxmRowStatus_Object=MibTableColumn
otxmRowStatus=_OtxmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,32,1,1,3),_OtxmRowStatus_Type())
otxmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:otxmRowStatus.setStatus(_A)
_OtxmConformance_ObjectIdentity=ObjectIdentity
otxmConformance=_OtxmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,32,3))
_OtxmCompliances_ObjectIdentity=ObjectIdentity
otxmCompliances=_OtxmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,32,3,1))
_OtxmGroups_ObjectIdentity=ObjectIdentity
otxmGroups=_OtxmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,32,3,2))
otxmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,32,3,2,1))
otxmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:otxmGroup.setStatus(_A)
otxmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,32,3,1,1))
otxmCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:otxmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otxmMIB':otxmMIB,'otxmTable':otxmTable,'otxmEntry':otxmEntry,_F:otxmMoId,_G:otxmProvEqptType,_H:otxmRowStatus,'otxmConformance':otxmConformance,'otxmCompliances':otxmCompliances,'otxmCompliance':otxmCompliance,'otxmGroups':otxmGroups,_I:otxmGroup})