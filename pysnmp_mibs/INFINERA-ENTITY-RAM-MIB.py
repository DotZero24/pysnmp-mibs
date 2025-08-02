_O='ramGroup'
_N='ramPilotLaserDisable'
_M='ramTargetGainOffset'
_L='ramRowStatus'
_K='ramPointLossOffset'
_J='ramMaxNumberOfChannels'
_I='ramGainCorrection'
_H='ramProvEqptType'
_G='ramMoId'
_F='read-write'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-create'
_B='INFINERA-ENTITY-RAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEqptType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ramMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,12))
_RamTable_Object=MibTable
ramTable=_RamTable_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1))
if mibBuilder.loadTexts:ramTable.setStatus(_A)
_RamEntry_Object=MibTableRow
ramEntry=_RamEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1))
ramEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ramEntry.setStatus(_A)
_RamMoId_Type=DisplayString
_RamMoId_Object=MibTableColumn
ramMoId=_RamMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,1),_RamMoId_Type())
ramMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:ramMoId.setStatus(_A)
_RamProvEqptType_Type=InfnEqptType
_RamProvEqptType_Object=MibTableColumn
ramProvEqptType=_RamProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,2),_RamProvEqptType_Type())
ramProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:ramProvEqptType.setStatus(_A)
_RamGainCorrection_Type=FloatTenths
_RamGainCorrection_Object=MibTableColumn
ramGainCorrection=_RamGainCorrection_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,3),_RamGainCorrection_Type())
ramGainCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:ramGainCorrection.setStatus(_A)
_RamMaxNumberOfChannels_Type=Unsigned32
_RamMaxNumberOfChannels_Object=MibTableColumn
ramMaxNumberOfChannels=_RamMaxNumberOfChannels_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,4),_RamMaxNumberOfChannels_Type())
ramMaxNumberOfChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:ramMaxNumberOfChannels.setStatus(_A)
_RamPointLossOffset_Type=FloatTenths
_RamPointLossOffset_Object=MibTableColumn
ramPointLossOffset=_RamPointLossOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,5),_RamPointLossOffset_Type())
ramPointLossOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:ramPointLossOffset.setStatus(_A)
_RamRowStatus_Type=RowStatus
_RamRowStatus_Object=MibTableColumn
ramRowStatus=_RamRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,6),_RamRowStatus_Type())
ramRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ramRowStatus.setStatus(_A)
_RamTargetGainOffset_Type=FloatTenths
_RamTargetGainOffset_Object=MibTableColumn
ramTargetGainOffset=_RamTargetGainOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,7),_RamTargetGainOffset_Type())
ramTargetGainOffset.setMaxAccess(_F)
if mibBuilder.loadTexts:ramTargetGainOffset.setStatus(_A)
_RamPilotLaserDisable_Type=TruthValue
_RamPilotLaserDisable_Object=MibTableColumn
ramPilotLaserDisable=_RamPilotLaserDisable_Object((1,3,6,1,4,1,21296,2,2,2,1,12,1,1,8),_RamPilotLaserDisable_Type())
ramPilotLaserDisable.setMaxAccess(_F)
if mibBuilder.loadTexts:ramPilotLaserDisable.setStatus(_A)
_RamConformance_ObjectIdentity=ObjectIdentity
ramConformance=_RamConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,12,3))
_RamCompliances_ObjectIdentity=ObjectIdentity
ramCompliances=_RamCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,12,3,1))
_RamGroups_ObjectIdentity=ObjectIdentity
ramGroups=_RamGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,12,3,2))
ramGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,12,3,2,1))
ramGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ramGroup.setStatus(_A)
ramCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,12,3,1,1))
ramCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ramCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ramMIB':ramMIB,'ramTable':ramTable,'ramEntry':ramEntry,_G:ramMoId,_H:ramProvEqptType,_I:ramGainCorrection,_J:ramMaxNumberOfChannels,_K:ramPointLossOffset,_L:ramRowStatus,_M:ramTargetGainOffset,_N:ramPilotLaserDisable,'ramConformance':ramConformance,'ramCompliances':ramCompliances,'ramCompliance':ramCompliance,'ramGroups':ramGroups,_O:ramGroup})