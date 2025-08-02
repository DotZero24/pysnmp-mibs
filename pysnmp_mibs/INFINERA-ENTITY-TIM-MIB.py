_S='timGroup'
_R='timPortMappingModeGroup4'
_Q='timPortMappingModeGroup3'
_P='timPortMappingModeGroup2'
_O='timPortMappingModeGroup1'
_N='timOperatingMode'
_M='timOperatingModeStatus'
_L='timRowStatus'
_K='timProvEqptType'
_J='timMoId'
_I='Integer32'
_H='InfnFPGAOperatingMode'
_G='entLPPhysicalIndex'
_F='ENTITY-MIB'
_E='read-create'
_D='read-write'
_C='InfnPortMappingMode'
_B='INFINERA-ENTITY-TIM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,InfnFPGAOperatingMode,InfnPortMappingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType',_H,_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
timMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,23))
_TimTable_Object=MibTable
timTable=_TimTable_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1))
if mibBuilder.loadTexts:timTable.setStatus(_A)
_TimEntry_Object=MibTableRow
timEntry=_TimEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1))
timEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:timEntry.setStatus(_A)
_TimMoId_Type=DisplayString
_TimMoId_Object=MibTableColumn
timMoId=_TimMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,1),_TimMoId_Type())
timMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:timMoId.setStatus(_A)
_TimProvEqptType_Type=InfnEqptType
_TimProvEqptType_Object=MibTableColumn
timProvEqptType=_TimProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,2),_TimProvEqptType_Type())
timProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:timProvEqptType.setStatus(_A)
_TimRowStatus_Type=RowStatus
_TimRowStatus_Object=MibTableColumn
timRowStatus=_TimRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,3),_TimRowStatus_Type())
timRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:timRowStatus.setStatus(_A)
class _TimOperatingModeStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('changeinprogress',2),('preProvisioned',3),('notDetermined',4)))
_TimOperatingModeStatus_Type.__name__=_I
_TimOperatingModeStatus_Object=MibTableColumn
timOperatingModeStatus=_TimOperatingModeStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,4),_TimOperatingModeStatus_Type())
timOperatingModeStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:timOperatingModeStatus.setStatus(_A)
class _TimOperatingMode_Type(InfnFPGAOperatingMode):defaultValue=4
_TimOperatingMode_Type.__name__=_H
_TimOperatingMode_Object=MibTableColumn
timOperatingMode=_TimOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,5),_TimOperatingMode_Type())
timOperatingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:timOperatingMode.setStatus(_A)
class _TimPortMappingModeGroup1_Type(InfnPortMappingMode):defaultValue=2
_TimPortMappingModeGroup1_Type.__name__=_C
_TimPortMappingModeGroup1_Object=MibTableColumn
timPortMappingModeGroup1=_TimPortMappingModeGroup1_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,6),_TimPortMappingModeGroup1_Type())
timPortMappingModeGroup1.setMaxAccess(_D)
if mibBuilder.loadTexts:timPortMappingModeGroup1.setStatus(_A)
class _TimPortMappingModeGroup2_Type(InfnPortMappingMode):defaultValue=2
_TimPortMappingModeGroup2_Type.__name__=_C
_TimPortMappingModeGroup2_Object=MibTableColumn
timPortMappingModeGroup2=_TimPortMappingModeGroup2_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,7),_TimPortMappingModeGroup2_Type())
timPortMappingModeGroup2.setMaxAccess(_D)
if mibBuilder.loadTexts:timPortMappingModeGroup2.setStatus(_A)
class _TimPortMappingModeGroup3_Type(InfnPortMappingMode):defaultValue=2
_TimPortMappingModeGroup3_Type.__name__=_C
_TimPortMappingModeGroup3_Object=MibTableColumn
timPortMappingModeGroup3=_TimPortMappingModeGroup3_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,8),_TimPortMappingModeGroup3_Type())
timPortMappingModeGroup3.setMaxAccess(_D)
if mibBuilder.loadTexts:timPortMappingModeGroup3.setStatus(_A)
class _TimPortMappingModeGroup4_Type(InfnPortMappingMode):defaultValue=2
_TimPortMappingModeGroup4_Type.__name__=_C
_TimPortMappingModeGroup4_Object=MibTableColumn
timPortMappingModeGroup4=_TimPortMappingModeGroup4_Object((1,3,6,1,4,1,21296,2,2,2,1,23,1,1,9),_TimPortMappingModeGroup4_Type())
timPortMappingModeGroup4.setMaxAccess(_D)
if mibBuilder.loadTexts:timPortMappingModeGroup4.setStatus(_A)
_TimConformance_ObjectIdentity=ObjectIdentity
timConformance=_TimConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,23,3))
_TimCompliances_ObjectIdentity=ObjectIdentity
timCompliances=_TimCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,23,3,1))
_TimGroups_ObjectIdentity=ObjectIdentity
timGroups=_TimGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,23,3,2))
timGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,23,3,2,1))
timGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:timGroup.setStatus(_A)
timCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,23,3,1,1))
timCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:timCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timMIB':timMIB,'timTable':timTable,'timEntry':timEntry,_J:timMoId,_K:timProvEqptType,_L:timRowStatus,_M:timOperatingModeStatus,_N:timOperatingMode,_O:timPortMappingModeGroup1,_P:timPortMappingModeGroup2,_Q:timPortMappingModeGroup3,_R:timPortMappingModeGroup4,'timConformance':timConformance,'timCompliances':timCompliances,'timCompliance':timCompliance,'timGroups':timGroups,_S:timGroup})