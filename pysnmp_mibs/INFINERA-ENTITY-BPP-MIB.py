_I='bppGroup'
_H='bppProvSerialNumber'
_G='bppProvEqptType'
_F='bppMoId'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-BPP-MIB'
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
bppMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,48))
_BppTable_Object=MibTable
bppTable=_BppTable_Object((1,3,6,1,4,1,21296,2,2,2,1,48,1))
if mibBuilder.loadTexts:bppTable.setStatus(_A)
_BppEntry_Object=MibTableRow
bppEntry=_BppEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,48,1,1))
bppEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bppEntry.setStatus(_A)
_BppMoId_Type=DisplayString
_BppMoId_Object=MibTableColumn
bppMoId=_BppMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,48,1,1,1),_BppMoId_Type())
bppMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:bppMoId.setStatus(_A)
_BppProvEqptType_Type=InfnEqptType
_BppProvEqptType_Object=MibTableColumn
bppProvEqptType=_BppProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,48,1,1,2),_BppProvEqptType_Type())
bppProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:bppProvEqptType.setStatus(_A)
_BppProvSerialNumber_Type=DisplayString
_BppProvSerialNumber_Object=MibTableColumn
bppProvSerialNumber=_BppProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,48,1,1,3),_BppProvSerialNumber_Type())
bppProvSerialNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:bppProvSerialNumber.setStatus(_A)
_BppConformance_ObjectIdentity=ObjectIdentity
bppConformance=_BppConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,48,3))
_BppCompliances_ObjectIdentity=ObjectIdentity
bppCompliances=_BppCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,48,3,1))
_BppGroups_ObjectIdentity=ObjectIdentity
bppGroups=_BppGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,48,3,2))
bppGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,48,3,2,1))
bppGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:bppGroup.setStatus(_A)
bppCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,48,3,1,1))
bppCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:bppCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bppMIB':bppMIB,'bppTable':bppTable,'bppEntry':bppEntry,_F:bppMoId,_G:bppProvEqptType,_H:bppProvSerialNumber,'bppConformance':bppConformance,'bppCompliances':bppCompliances,'bppCompliance':bppCompliance,'bppGroups':bppGroups,_I:bppGroup})