_d='ofxGroup'
_c='ofxBw3Qlicensed'
_b='ofxBw3Qused'
_a='ofxBw3Qmax'
_Z='ofxAvailableTunableSuperChNumbers'
_Y='ofxBwUsgWaterMarkGranularity'
_X='ofxDefFlexLicModFormat'
_W='ofxLicenseEnforced'
_V='ofxLicensedServicesDisabled'
_U='ofxBwBlicensed'
_T='ofxBwBused'
_S='ofxBwBmax'
_R='ofxBwQlicensed'
_Q='ofxBwQused'
_P='ofxBwQmax'
_O='ofxRecommendedGain'
_N='ofxOTNContainerRepresentation'
_M='ofxRxEdfaGain'
_L='ofxRxEdfaOutputPowerTarget'
_K='ofxMaxFruGain'
_J='ofxPicDspVer'
_I='ofxActvTimingSource'
_H='ofxProvEqptType'
_G='ofxMoId'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-ENTITY-OFX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEnforcementMode,InfnEqptType,InfnLicenseModulationType,InfnOtnOtuType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEnforcementMode','InfnEqptType','InfnLicenseModulationType','InfnOtnOtuType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ofxMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,34))
_OfxTable_Object=MibTable
ofxTable=_OfxTable_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1))
if mibBuilder.loadTexts:ofxTable.setStatus(_A)
_OfxEntry_Object=MibTableRow
ofxEntry=_OfxEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1))
ofxEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ofxEntry.setStatus(_A)
_OfxMoId_Type=DisplayString
_OfxMoId_Object=MibTableColumn
ofxMoId=_OfxMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,1),_OfxMoId_Type())
ofxMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxMoId.setStatus(_A)
_OfxProvEqptType_Type=InfnEqptType
_OfxProvEqptType_Object=MibTableColumn
ofxProvEqptType=_OfxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,2),_OfxProvEqptType_Type())
ofxProvEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxProvEqptType.setStatus(_A)
_OfxOTNContainerRepresentation_Type=InfnOtnOtuType
_OfxOTNContainerRepresentation_Object=MibTableColumn
ofxOTNContainerRepresentation=_OfxOTNContainerRepresentation_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,3),_OfxOTNContainerRepresentation_Type())
ofxOTNContainerRepresentation.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxOTNContainerRepresentation.setStatus(_A)
_OfxActvTimingSource_Type=DisplayString
_OfxActvTimingSource_Object=MibTableColumn
ofxActvTimingSource=_OfxActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,4),_OfxActvTimingSource_Type())
ofxActvTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxActvTimingSource.setStatus(_A)
_OfxPicDspVer_Type=DisplayString
_OfxPicDspVer_Object=MibTableColumn
ofxPicDspVer=_OfxPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,5),_OfxPicDspVer_Type())
ofxPicDspVer.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxPicDspVer.setStatus(_A)
_OfxMaxFruGain_Type=FloatTenths
_OfxMaxFruGain_Object=MibTableColumn
ofxMaxFruGain=_OfxMaxFruGain_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,6),_OfxMaxFruGain_Type())
ofxMaxFruGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxMaxFruGain.setStatus(_A)
_OfxRecommendedGain_Type=FloatTenths
_OfxRecommendedGain_Object=MibTableColumn
ofxRecommendedGain=_OfxRecommendedGain_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,7),_OfxRecommendedGain_Type())
ofxRecommendedGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxRecommendedGain.setStatus(_A)
_OfxRxEdfaOutputPowerTarget_Type=FloatTenths
_OfxRxEdfaOutputPowerTarget_Object=MibTableColumn
ofxRxEdfaOutputPowerTarget=_OfxRxEdfaOutputPowerTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,8),_OfxRxEdfaOutputPowerTarget_Type())
ofxRxEdfaOutputPowerTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxRxEdfaOutputPowerTarget.setStatus(_A)
_OfxRxEdfaGain_Type=FloatTenths
_OfxRxEdfaGain_Object=MibTableColumn
ofxRxEdfaGain=_OfxRxEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,9),_OfxRxEdfaGain_Type())
ofxRxEdfaGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxRxEdfaGain.setStatus(_A)
_OfxBwQmax_Type=FloatTenths
_OfxBwQmax_Object=MibTableColumn
ofxBwQmax=_OfxBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,10),_OfxBwQmax_Type())
ofxBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxBwQmax.setStatus(_A)
_OfxBwQused_Type=FloatTenths
_OfxBwQused_Object=MibTableColumn
ofxBwQused=_OfxBwQused_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,11),_OfxBwQused_Type())
ofxBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxBwQused.setStatus(_A)
_OfxBwQlicensed_Type=FloatTenths
_OfxBwQlicensed_Object=MibTableColumn
ofxBwQlicensed=_OfxBwQlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,12),_OfxBwQlicensed_Type())
ofxBwQlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxBwQlicensed.setStatus(_A)
_OfxBwBmax_Type=FloatTenths
_OfxBwBmax_Object=MibTableColumn
ofxBwBmax=_OfxBwBmax_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,13),_OfxBwBmax_Type())
ofxBwBmax.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxBwBmax.setStatus(_A)
_OfxBwBused_Type=FloatTenths
_OfxBwBused_Object=MibTableColumn
ofxBwBused=_OfxBwBused_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,14),_OfxBwBused_Type())
ofxBwBused.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxBwBused.setStatus(_A)
_OfxBwBlicensed_Type=FloatTenths
_OfxBwBlicensed_Object=MibTableColumn
ofxBwBlicensed=_OfxBwBlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,15),_OfxBwBlicensed_Type())
ofxBwBlicensed.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxBwBlicensed.setStatus(_A)
_OfxLicensedServicesDisabled_Type=Integer32
_OfxLicensedServicesDisabled_Object=MibTableColumn
ofxLicensedServicesDisabled=_OfxLicensedServicesDisabled_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,16),_OfxLicensedServicesDisabled_Type())
ofxLicensedServicesDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxLicensedServicesDisabled.setStatus(_A)
_OfxLicenseEnforced_Type=InfnEnforcementMode
_OfxLicenseEnforced_Object=MibTableColumn
ofxLicenseEnforced=_OfxLicenseEnforced_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,17),_OfxLicenseEnforced_Type())
ofxLicenseEnforced.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxLicenseEnforced.setStatus(_A)
_OfxDefFlexLicModFormat_Type=InfnLicenseModulationType
_OfxDefFlexLicModFormat_Object=MibTableColumn
ofxDefFlexLicModFormat=_OfxDefFlexLicModFormat_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,18),_OfxDefFlexLicModFormat_Type())
ofxDefFlexLicModFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxDefFlexLicModFormat.setStatus(_A)
_OfxBwUsgWaterMarkGranularity_Type=FloatTenths
_OfxBwUsgWaterMarkGranularity_Object=MibTableColumn
ofxBwUsgWaterMarkGranularity=_OfxBwUsgWaterMarkGranularity_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,19),_OfxBwUsgWaterMarkGranularity_Type())
ofxBwUsgWaterMarkGranularity.setMaxAccess(_D)
if mibBuilder.loadTexts:ofxBwUsgWaterMarkGranularity.setStatus(_A)
_OfxAvailableTunableSuperChNumbers_Type=DisplayString
_OfxAvailableTunableSuperChNumbers_Object=MibTableColumn
ofxAvailableTunableSuperChNumbers=_OfxAvailableTunableSuperChNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,20),_OfxAvailableTunableSuperChNumbers_Type())
ofxAvailableTunableSuperChNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxAvailableTunableSuperChNumbers.setStatus(_A)
_OfxBw3Qmax_Type=FloatTenths
_OfxBw3Qmax_Object=MibTableColumn
ofxBw3Qmax=_OfxBw3Qmax_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,21),_OfxBw3Qmax_Type())
ofxBw3Qmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxBw3Qmax.setStatus(_A)
_OfxBw3Qused_Type=FloatTenths
_OfxBw3Qused_Object=MibTableColumn
ofxBw3Qused=_OfxBw3Qused_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,22),_OfxBw3Qused_Type())
ofxBw3Qused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxBw3Qused.setStatus(_A)
_OfxBw3Qlicensed_Type=FloatTenths
_OfxBw3Qlicensed_Object=MibTableColumn
ofxBw3Qlicensed=_OfxBw3Qlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,34,1,1,23),_OfxBw3Qlicensed_Type())
ofxBw3Qlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:ofxBw3Qlicensed.setStatus(_A)
_OfxConformance_ObjectIdentity=ObjectIdentity
ofxConformance=_OfxConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,34,3))
_OfxCompliances_ObjectIdentity=ObjectIdentity
ofxCompliances=_OfxCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,34,3,1))
_OfxGroups_ObjectIdentity=ObjectIdentity
ofxGroups=_OfxGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,34,3,2))
ofxGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,34,3,2,1))
ofxGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ofxGroup.setStatus(_A)
ofxCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,34,3,1,1))
ofxCompliance.setObjects((_B,_d))
if mibBuilder.loadTexts:ofxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ofxMIB':ofxMIB,'ofxTable':ofxTable,'ofxEntry':ofxEntry,_G:ofxMoId,_H:ofxProvEqptType,_N:ofxOTNContainerRepresentation,_I:ofxActvTimingSource,_J:ofxPicDspVer,_K:ofxMaxFruGain,_O:ofxRecommendedGain,_L:ofxRxEdfaOutputPowerTarget,_M:ofxRxEdfaGain,_P:ofxBwQmax,_Q:ofxBwQused,_R:ofxBwQlicensed,_S:ofxBwBmax,_T:ofxBwBused,_U:ofxBwBlicensed,_V:ofxLicensedServicesDisabled,_W:ofxLicenseEnforced,_X:ofxDefFlexLicModFormat,_Y:ofxBwUsgWaterMarkGranularity,_Z:ofxAvailableTunableSuperChNumbers,_a:ofxBw3Qmax,_b:ofxBw3Qused,_c:ofxBw3Qlicensed,'ofxConformance':ofxConformance,'ofxCompliances':ofxCompliances,'ofxCompliance':ofxCompliance,'ofxGroups':ofxGroups,_d:ofxGroup})