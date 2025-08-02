_U='ofixGroup'
_T='ofixAvailableTunableSuperChNumbers'
_S='ofixBwUsgWaterMarkGranularity'
_R='ofixBwBused'
_Q='ofixBwBmax'
_P='ofixBwQused'
_O='ofixBwQmax'
_N='ofixRecommendedGain'
_M='ofixOTNContainerRepresentation'
_L='ofixRxEdfaGain'
_K='ofixRxEdfaOutputPowerTarget'
_J='ofixMaxFruGain'
_I='ofixPicDspVer'
_H='ofixProvEqptType'
_G='ofixMoId'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-OFIX-MIB'
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
ofixMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,45))
_OfixTable_Object=MibTable
ofixTable=_OfixTable_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1))
if mibBuilder.loadTexts:ofixTable.setStatus(_A)
_OfixEntry_Object=MibTableRow
ofixEntry=_OfixEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1))
ofixEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ofixEntry.setStatus(_A)
_OfixMoId_Type=DisplayString
_OfixMoId_Object=MibTableColumn
ofixMoId=_OfixMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,1),_OfixMoId_Type())
ofixMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixMoId.setStatus(_A)
_OfixProvEqptType_Type=InfnEqptType
_OfixProvEqptType_Object=MibTableColumn
ofixProvEqptType=_OfixProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,2),_OfixProvEqptType_Type())
ofixProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixProvEqptType.setStatus(_A)
_OfixOTNContainerRepresentation_Type=InfnOtnOtuType
_OfixOTNContainerRepresentation_Object=MibTableColumn
ofixOTNContainerRepresentation=_OfixOTNContainerRepresentation_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,3),_OfixOTNContainerRepresentation_Type())
ofixOTNContainerRepresentation.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixOTNContainerRepresentation.setStatus(_A)
_OfixPicDspVer_Type=DisplayString
_OfixPicDspVer_Object=MibTableColumn
ofixPicDspVer=_OfixPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,4),_OfixPicDspVer_Type())
ofixPicDspVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ofixPicDspVer.setStatus(_A)
_OfixMaxFruGain_Type=FloatTenths
_OfixMaxFruGain_Object=MibTableColumn
ofixMaxFruGain=_OfixMaxFruGain_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,5),_OfixMaxFruGain_Type())
ofixMaxFruGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofixMaxFruGain.setStatus(_A)
_OfixRecommendedGain_Type=FloatTenths
_OfixRecommendedGain_Object=MibTableColumn
ofixRecommendedGain=_OfixRecommendedGain_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,6),_OfixRecommendedGain_Type())
ofixRecommendedGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofixRecommendedGain.setStatus(_A)
_OfixRxEdfaOutputPowerTarget_Type=FloatTenths
_OfixRxEdfaOutputPowerTarget_Object=MibTableColumn
ofixRxEdfaOutputPowerTarget=_OfixRxEdfaOutputPowerTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,7),_OfixRxEdfaOutputPowerTarget_Type())
ofixRxEdfaOutputPowerTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:ofixRxEdfaOutputPowerTarget.setStatus(_A)
_OfixRxEdfaGain_Type=FloatTenths
_OfixRxEdfaGain_Object=MibTableColumn
ofixRxEdfaGain=_OfixRxEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,8),_OfixRxEdfaGain_Type())
ofixRxEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixRxEdfaGain.setStatus(_A)
_OfixBwQmax_Type=FloatTenths
_OfixBwQmax_Object=MibTableColumn
ofixBwQmax=_OfixBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,9),_OfixBwQmax_Type())
ofixBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixBwQmax.setStatus(_A)
_OfixBwQused_Type=FloatTenths
_OfixBwQused_Object=MibTableColumn
ofixBwQused=_OfixBwQused_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,10),_OfixBwQused_Type())
ofixBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixBwQused.setStatus(_A)
_OfixBwBmax_Type=FloatTenths
_OfixBwBmax_Object=MibTableColumn
ofixBwBmax=_OfixBwBmax_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,11),_OfixBwBmax_Type())
ofixBwBmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixBwBmax.setStatus(_A)
_OfixBwBused_Type=FloatTenths
_OfixBwBused_Object=MibTableColumn
ofixBwBused=_OfixBwBused_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,12),_OfixBwBused_Type())
ofixBwBused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixBwBused.setStatus(_A)
_OfixBwUsgWaterMarkGranularity_Type=FloatTenths
_OfixBwUsgWaterMarkGranularity_Object=MibTableColumn
ofixBwUsgWaterMarkGranularity=_OfixBwUsgWaterMarkGranularity_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,13),_OfixBwUsgWaterMarkGranularity_Type())
ofixBwUsgWaterMarkGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:ofixBwUsgWaterMarkGranularity.setStatus(_A)
_OfixAvailableTunableSuperChNumbers_Type=DisplayString
_OfixAvailableTunableSuperChNumbers_Object=MibTableColumn
ofixAvailableTunableSuperChNumbers=_OfixAvailableTunableSuperChNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,45,1,1,14),_OfixAvailableTunableSuperChNumbers_Type())
ofixAvailableTunableSuperChNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:ofixAvailableTunableSuperChNumbers.setStatus(_A)
_OfixConformance_ObjectIdentity=ObjectIdentity
ofixConformance=_OfixConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,45,3))
_OfixCompliances_ObjectIdentity=ObjectIdentity
ofixCompliances=_OfixCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,45,3,1))
_OfixGroups_ObjectIdentity=ObjectIdentity
ofixGroups=_OfixGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,45,3,2))
ofixGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,45,3,2,1))
ofixGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ofixGroup.setStatus(_A)
ofixCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,45,3,1,1))
ofixCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:ofixCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ofixMIB':ofixMIB,'ofixTable':ofixTable,'ofixEntry':ofixEntry,_G:ofixMoId,_H:ofixProvEqptType,_M:ofixOTNContainerRepresentation,_I:ofixPicDspVer,_J:ofixMaxFruGain,_N:ofixRecommendedGain,_K:ofixRxEdfaOutputPowerTarget,_L:ofixRxEdfaGain,_O:ofixBwQmax,_P:ofixBwQused,_Q:ofixBwBmax,_R:ofixBwBused,_S:ofixBwUsgWaterMarkGranularity,_T:ofixAvailableTunableSuperChNumbers,'ofixConformance':ofixConformance,'ofixCompliances':ofixCompliances,'ofixCompliance':ofixCompliance,'ofixGroups':ofixGroups,_U:ofixGroup})