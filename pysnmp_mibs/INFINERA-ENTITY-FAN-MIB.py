_H='fanGroup'
_G='fanProvEqptType'
_F='fanMoId'
_E='read-only'
_D='entLPPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-FAN-MIB'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fanMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,14))
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,21296,2,2,2,1,14,1))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,14,1,1))
fanEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fanEntry.setStatus(_A)
_FanMoId_Type=DisplayString
_FanMoId_Object=MibTableColumn
fanMoId=_FanMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,14,1,1,1),_FanMoId_Type())
fanMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:fanMoId.setStatus(_A)
_FanProvEqptType_Type=InfnEqptType
_FanProvEqptType_Object=MibTableColumn
fanProvEqptType=_FanProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,14,1,1,2),_FanProvEqptType_Type())
fanProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:fanProvEqptType.setStatus(_A)
_FanConformance_ObjectIdentity=ObjectIdentity
fanConformance=_FanConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,14,3))
_FanCompliances_ObjectIdentity=ObjectIdentity
fanCompliances=_FanCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,14,3,1))
_FanGroups_ObjectIdentity=ObjectIdentity
fanGroups=_FanGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,14,3,2))
fanGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,14,3,2,1))
fanGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:fanGroup.setStatus(_A)
fanCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,14,3,1,1))
fanCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:fanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fanMIB':fanMIB,'fanTable':fanTable,'fanEntry':fanEntry,_F:fanMoId,_G:fanProvEqptType,'fanConformance':fanConformance,'fanCompliances':fanCompliances,'fanCompliance':fanCompliance,'fanGroups':fanGroups,_H:fanGroup})