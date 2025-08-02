_I='rbpGroup'
_H='rbpProvSerialNumber'
_G='rbpProvEqptType'
_F='rbpMoId'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-RBP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rbpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,49))
_RbpTable_Object=MibTable
rbpTable=_RbpTable_Object((1,3,6,1,4,1,21296,2,2,2,1,49,1))
if mibBuilder.loadTexts:rbpTable.setStatus(_A)
_RbpEntry_Object=MibTableRow
rbpEntry=_RbpEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,49,1,1))
rbpEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rbpEntry.setStatus(_A)
_RbpMoId_Type=DisplayString
_RbpMoId_Object=MibTableColumn
rbpMoId=_RbpMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,49,1,1,1),_RbpMoId_Type())
rbpMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:rbpMoId.setStatus(_A)
_RbpProvEqptType_Type=InfnEqptType
_RbpProvEqptType_Object=MibTableColumn
rbpProvEqptType=_RbpProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,49,1,1,2),_RbpProvEqptType_Type())
rbpProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:rbpProvEqptType.setStatus(_A)
_RbpProvSerialNumber_Type=DisplayString
_RbpProvSerialNumber_Object=MibTableColumn
rbpProvSerialNumber=_RbpProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,49,1,1,3),_RbpProvSerialNumber_Type())
rbpProvSerialNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:rbpProvSerialNumber.setStatus(_A)
_RbpConformance_ObjectIdentity=ObjectIdentity
rbpConformance=_RbpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,49,3))
_RbpCompliances_ObjectIdentity=ObjectIdentity
rbpCompliances=_RbpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,49,3,1))
_RbpGroups_ObjectIdentity=ObjectIdentity
rbpGroups=_RbpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,49,3,2))
rbpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,49,3,2,1))
rbpGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:rbpGroup.setStatus(_A)
rbpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,49,3,1,1))
rbpCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:rbpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbpMIB':rbpMIB,'rbpTable':rbpTable,'rbpEntry':rbpEntry,_F:rbpMoId,_G:rbpProvEqptType,_H:rbpProvSerialNumber,'rbpConformance':rbpConformance,'rbpCompliances':rbpCompliances,'rbpCompliance':rbpCompliance,'rbpGroups':rbpGroups,_I:rbpGroup})