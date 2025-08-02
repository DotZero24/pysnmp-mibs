_N='passiveGroup'
_M='passiveNumLinePorts'
_L='passiveNumSystemPorts'
_K='passiveProvSerialNumber'
_J='passiveLabel'
_I='passiveProvEqptType'
_H='passiveMoId'
_G='read-only'
_F='read-write'
_E='read-create'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-PASSIVE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
commonEquipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonEquipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
passiveMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,9,2))
if mibBuilder.loadTexts:passiveMIB.setRevisions(('2017-01-08 00:00',))
_PassiveTable_Object=MibTable
passiveTable=_PassiveTable_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1))
if mibBuilder.loadTexts:passiveTable.setStatus(_A)
_PassiveEntry_Object=MibTableRow
passiveEntry=_PassiveEntry_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1))
passiveEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:passiveEntry.setStatus(_A)
_PassiveMoId_Type=DisplayString
_PassiveMoId_Object=MibTableColumn
passiveMoId=_PassiveMoId_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1,1),_PassiveMoId_Type())
passiveMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:passiveMoId.setStatus(_A)
_PassiveProvEqptType_Type=InfnEqptType
_PassiveProvEqptType_Object=MibTableColumn
passiveProvEqptType=_PassiveProvEqptType_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1,2),_PassiveProvEqptType_Type())
passiveProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:passiveProvEqptType.setStatus(_A)
_PassiveLabel_Type=DisplayString
_PassiveLabel_Object=MibTableColumn
passiveLabel=_PassiveLabel_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1,3),_PassiveLabel_Type())
passiveLabel.setMaxAccess(_F)
if mibBuilder.loadTexts:passiveLabel.setStatus(_A)
_PassiveProvSerialNumber_Type=DisplayString
_PassiveProvSerialNumber_Object=MibTableColumn
passiveProvSerialNumber=_PassiveProvSerialNumber_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1,4),_PassiveProvSerialNumber_Type())
passiveProvSerialNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:passiveProvSerialNumber.setStatus(_A)
_PassiveNumSystemPorts_Type=Integer32
_PassiveNumSystemPorts_Object=MibTableColumn
passiveNumSystemPorts=_PassiveNumSystemPorts_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1,5),_PassiveNumSystemPorts_Type())
passiveNumSystemPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:passiveNumSystemPorts.setStatus(_A)
_PassiveNumLinePorts_Type=Integer32
_PassiveNumLinePorts_Object=MibTableColumn
passiveNumLinePorts=_PassiveNumLinePorts_Object((1,3,6,1,4,1,21296,2,2,1,9,2,1,1,6),_PassiveNumLinePorts_Type())
passiveNumLinePorts.setMaxAccess(_G)
if mibBuilder.loadTexts:passiveNumLinePorts.setStatus(_A)
_PassiveConformance_ObjectIdentity=ObjectIdentity
passiveConformance=_PassiveConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9,2,3))
_PassiveCompliances_ObjectIdentity=ObjectIdentity
passiveCompliances=_PassiveCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9,2,3,1))
_PassiveGroups_ObjectIdentity=ObjectIdentity
passiveGroups=_PassiveGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9,2,3,2))
passiveGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,9,2,3,2,1))
passiveGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:passiveGroup.setStatus(_A)
passiveCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,9,2,3,1,1))
passiveCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:passiveCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'passiveMIB':passiveMIB,'passiveTable':passiveTable,'passiveEntry':passiveEntry,_H:passiveMoId,_I:passiveProvEqptType,_J:passiveLabel,_K:passiveProvSerialNumber,_L:passiveNumSystemPorts,_M:passiveNumLinePorts,'passiveConformance':passiveConformance,'passiveCompliances':passiveCompliances,'passiveCompliance':passiveCompliance,'passiveGroups':passiveGroups,_N:passiveGroup})