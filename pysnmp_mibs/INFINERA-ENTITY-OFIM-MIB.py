_U='ofimGroup'
_T='ofimAvailableTunableSuperChNumbers'
_S='ofimBwUsgWaterMarkGranularity'
_R='ofimBwBused'
_Q='ofimBwBmax'
_P='ofimBwQused'
_O='ofimBwQmax'
_N='ofimRecommendedGain'
_M='ofimOTNContainerRepresentation'
_L='ofimRxEdfaGain'
_K='ofimRxEdfaOutputPowerTarget'
_J='ofimMaxFruGain'
_I='ofimPicDspVer'
_H='ofimProvEqptType'
_G='ofimMoId'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-OFIM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEnforcementMode,InfnEqptType,InfnOtnOtuType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEnforcementMode','InfnEqptType','InfnOtnOtuType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ofimMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,44))
_OfimTable_Object=MibTable
ofimTable=_OfimTable_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1))
if mibBuilder.loadTexts:ofimTable.setStatus(_A)
_OfimEntry_Object=MibTableRow
ofimEntry=_OfimEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1))
ofimEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ofimEntry.setStatus(_A)
_OfimMoId_Type=DisplayString
_OfimMoId_Object=MibTableColumn
ofimMoId=_OfimMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,1),_OfimMoId_Type())
ofimMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimMoId.setStatus(_A)
_OfimProvEqptType_Type=InfnEqptType
_OfimProvEqptType_Object=MibTableColumn
ofimProvEqptType=_OfimProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,2),_OfimProvEqptType_Type())
ofimProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimProvEqptType.setStatus(_A)
_OfimOTNContainerRepresentation_Type=InfnOtnOtuType
_OfimOTNContainerRepresentation_Object=MibTableColumn
ofimOTNContainerRepresentation=_OfimOTNContainerRepresentation_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,3),_OfimOTNContainerRepresentation_Type())
ofimOTNContainerRepresentation.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimOTNContainerRepresentation.setStatus(_A)
_OfimPicDspVer_Type=DisplayString
_OfimPicDspVer_Object=MibTableColumn
ofimPicDspVer=_OfimPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,4),_OfimPicDspVer_Type())
ofimPicDspVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ofimPicDspVer.setStatus(_A)
_OfimMaxFruGain_Type=FloatTenths
_OfimMaxFruGain_Object=MibTableColumn
ofimMaxFruGain=_OfimMaxFruGain_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,5),_OfimMaxFruGain_Type())
ofimMaxFruGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofimMaxFruGain.setStatus(_A)
_OfimRecommendedGain_Type=FloatTenths
_OfimRecommendedGain_Object=MibTableColumn
ofimRecommendedGain=_OfimRecommendedGain_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,6),_OfimRecommendedGain_Type())
ofimRecommendedGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofimRecommendedGain.setStatus(_A)
_OfimRxEdfaOutputPowerTarget_Type=FloatTenths
_OfimRxEdfaOutputPowerTarget_Object=MibTableColumn
ofimRxEdfaOutputPowerTarget=_OfimRxEdfaOutputPowerTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,7),_OfimRxEdfaOutputPowerTarget_Type())
ofimRxEdfaOutputPowerTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:ofimRxEdfaOutputPowerTarget.setStatus(_A)
_OfimRxEdfaGain_Type=FloatTenths
_OfimRxEdfaGain_Object=MibTableColumn
ofimRxEdfaGain=_OfimRxEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,8),_OfimRxEdfaGain_Type())
ofimRxEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimRxEdfaGain.setStatus(_A)
_OfimBwQmax_Type=FloatTenths
_OfimBwQmax_Object=MibTableColumn
ofimBwQmax=_OfimBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,9),_OfimBwQmax_Type())
ofimBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimBwQmax.setStatus(_A)
_OfimBwQused_Type=FloatTenths
_OfimBwQused_Object=MibTableColumn
ofimBwQused=_OfimBwQused_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,10),_OfimBwQused_Type())
ofimBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimBwQused.setStatus(_A)
_OfimBwBmax_Type=FloatTenths
_OfimBwBmax_Object=MibTableColumn
ofimBwBmax=_OfimBwBmax_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,11),_OfimBwBmax_Type())
ofimBwBmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimBwBmax.setStatus(_A)
_OfimBwBused_Type=FloatTenths
_OfimBwBused_Object=MibTableColumn
ofimBwBused=_OfimBwBused_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,12),_OfimBwBused_Type())
ofimBwBused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimBwBused.setStatus(_A)
_OfimBwUsgWaterMarkGranularity_Type=FloatTenths
_OfimBwUsgWaterMarkGranularity_Object=MibTableColumn
ofimBwUsgWaterMarkGranularity=_OfimBwUsgWaterMarkGranularity_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,13),_OfimBwUsgWaterMarkGranularity_Type())
ofimBwUsgWaterMarkGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:ofimBwUsgWaterMarkGranularity.setStatus(_A)
_OfimAvailableTunableSuperChNumbers_Type=DisplayString
_OfimAvailableTunableSuperChNumbers_Object=MibTableColumn
ofimAvailableTunableSuperChNumbers=_OfimAvailableTunableSuperChNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,44,1,1,14),_OfimAvailableTunableSuperChNumbers_Type())
ofimAvailableTunableSuperChNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:ofimAvailableTunableSuperChNumbers.setStatus(_A)
_OfimConformance_ObjectIdentity=ObjectIdentity
ofimConformance=_OfimConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,44,3))
_OfimCompliances_ObjectIdentity=ObjectIdentity
ofimCompliances=_OfimCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,44,3,1))
_OfimGroups_ObjectIdentity=ObjectIdentity
ofimGroups=_OfimGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,44,3,2))
ofimGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,44,3,2,1))
ofimGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ofimGroup.setStatus(_A)
ofimCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,44,3,1,1))
ofimCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:ofimCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ofimMIB':ofimMIB,'ofimTable':ofimTable,'ofimEntry':ofimEntry,_G:ofimMoId,_H:ofimProvEqptType,_M:ofimOTNContainerRepresentation,_I:ofimPicDspVer,_J:ofimMaxFruGain,_N:ofimRecommendedGain,_K:ofimRxEdfaOutputPowerTarget,_L:ofimRxEdfaGain,_O:ofimBwQmax,_P:ofimBwQused,_Q:ofimBwBmax,_R:ofimBwBused,_S:ofimBwUsgWaterMarkGranularity,_T:ofimAvailableTunableSuperChNumbers,'ofimConformance':ofimConformance,'ofimCompliances':ofimCompliances,'ofimCompliance':ofimCompliance,'ofimGroups':ofimGroups,_U:ofimGroup})