_K='lmmGroup'
_J='lmmAssociatedDegree'
_I='lmmProvSerialNumber'
_H='lmmProvEqptType'
_G='lmmMoId'
_F='read-write'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-LMM-MIB'
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
lmmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,41))
_LmmTable_Object=MibTable
lmmTable=_LmmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,41,1))
if mibBuilder.loadTexts:lmmTable.setStatus(_A)
_LmmEntry_Object=MibTableRow
lmmEntry=_LmmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,41,1,1))
lmmEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:lmmEntry.setStatus(_A)
_LmmMoId_Type=DisplayString
_LmmMoId_Object=MibTableColumn
lmmMoId=_LmmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,41,1,1,1),_LmmMoId_Type())
lmmMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:lmmMoId.setStatus(_A)
_LmmProvEqptType_Type=InfnEqptType
_LmmProvEqptType_Object=MibTableColumn
lmmProvEqptType=_LmmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,41,1,1,2),_LmmProvEqptType_Type())
lmmProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:lmmProvEqptType.setStatus(_A)
_LmmProvSerialNumber_Type=DisplayString
_LmmProvSerialNumber_Object=MibTableColumn
lmmProvSerialNumber=_LmmProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,41,1,1,3),_LmmProvSerialNumber_Type())
lmmProvSerialNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:lmmProvSerialNumber.setStatus(_A)
_LmmAssociatedDegree_Type=DisplayString
_LmmAssociatedDegree_Object=MibTableColumn
lmmAssociatedDegree=_LmmAssociatedDegree_Object((1,3,6,1,4,1,21296,2,2,2,1,41,1,1,4),_LmmAssociatedDegree_Type())
lmmAssociatedDegree.setMaxAccess(_F)
if mibBuilder.loadTexts:lmmAssociatedDegree.setStatus(_A)
_LmmConformance_ObjectIdentity=ObjectIdentity
lmmConformance=_LmmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,41,3))
_LmmCompliances_ObjectIdentity=ObjectIdentity
lmmCompliances=_LmmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,41,3,1))
_LmmGroups_ObjectIdentity=ObjectIdentity
lmmGroups=_LmmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,41,3,2))
lmmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,41,3,2,1))
lmmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:lmmGroup.setStatus(_A)
lmmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,41,3,1,1))
lmmCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:lmmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lmmMIB':lmmMIB,'lmmTable':lmmTable,'lmmEntry':lmmEntry,_G:lmmMoId,_H:lmmProvEqptType,_I:lmmProvSerialNumber,_J:lmmAssociatedDegree,'lmmConformance':lmmConformance,'lmmCompliances':lmmCompliances,'lmmCompliance':lmmCompliance,'lmmGroups':lmmGroups,_K:lmmGroup})