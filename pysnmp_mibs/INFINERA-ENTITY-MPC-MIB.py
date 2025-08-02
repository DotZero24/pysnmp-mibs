_J='mpcGroup'
_I='mpcConnectedPassiveEqptList'
_H='mpcLabel'
_G='mpcProvSerialNumber'
_F='mpcProvEqptType'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='INFINERA-ENTITY-MPC-MIB'
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
mpcMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,50))
_MpcTable_Object=MibTable
mpcTable=_MpcTable_Object((1,3,6,1,4,1,21296,2,2,2,1,50,1))
if mibBuilder.loadTexts:mpcTable.setStatus(_A)
_MpcEntry_Object=MibTableRow
mpcEntry=_MpcEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,50,1,1))
mpcEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mpcEntry.setStatus(_A)
_MpcProvEqptType_Type=InfnEqptType
_MpcProvEqptType_Object=MibTableColumn
mpcProvEqptType=_MpcProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,50,1,1,1),_MpcProvEqptType_Type())
mpcProvEqptType.setMaxAccess('read-create')
if mibBuilder.loadTexts:mpcProvEqptType.setStatus(_A)
_MpcProvSerialNumber_Type=DisplayString
_MpcProvSerialNumber_Object=MibTableColumn
mpcProvSerialNumber=_MpcProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,1,50,1,1,2),_MpcProvSerialNumber_Type())
mpcProvSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mpcProvSerialNumber.setStatus(_A)
_MpcLabel_Type=DisplayString
_MpcLabel_Object=MibTableColumn
mpcLabel=_MpcLabel_Object((1,3,6,1,4,1,21296,2,2,2,1,50,1,1,3),_MpcLabel_Type())
mpcLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:mpcLabel.setStatus(_A)
_MpcConnectedPassiveEqptList_Type=DisplayString
_MpcConnectedPassiveEqptList_Object=MibTableColumn
mpcConnectedPassiveEqptList=_MpcConnectedPassiveEqptList_Object((1,3,6,1,4,1,21296,2,2,2,1,50,1,1,4),_MpcConnectedPassiveEqptList_Type())
mpcConnectedPassiveEqptList.setMaxAccess(_C)
if mibBuilder.loadTexts:mpcConnectedPassiveEqptList.setStatus(_A)
_MpcConformance_ObjectIdentity=ObjectIdentity
mpcConformance=_MpcConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,50,3))
_MpcCompliances_ObjectIdentity=ObjectIdentity
mpcCompliances=_MpcCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,50,3,1))
_MpcGroups_ObjectIdentity=ObjectIdentity
mpcGroups=_MpcGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,50,3,2))
mpcGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,50,3,2,1))
mpcGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mpcGroup.setStatus(_A)
mpcCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,50,3,1,1))
mpcCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:mpcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mpcMIB':mpcMIB,'mpcTable':mpcTable,'mpcEntry':mpcEntry,_F:mpcProvEqptType,_G:mpcProvSerialNumber,_H:mpcLabel,_I:mpcConnectedPassiveEqptList,'mpcConformance':mpcConformance,'mpcCompliances':mpcCompliances,'mpcCompliance':mpcCompliance,'mpcGroups':mpcGroups,_J:mpcGroup})