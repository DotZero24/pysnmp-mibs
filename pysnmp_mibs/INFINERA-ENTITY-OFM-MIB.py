_c='ofmGroup'
_b='ofmAvailableTunableSuperChNumbers'
_a='ofmBwUsgWaterMarkGranularity'
_Z='ofmDefFlexLicModFormat'
_Y='ofmLicenseEnforced'
_X='ofmLicensedServicesDisabled'
_W='ofmBwBlicensed'
_V='ofmBwBused'
_U='ofmBwBmax'
_T='ofmBwQlicensed'
_S='ofmBwQused'
_R='ofmBwQmax'
_Q='ofmRecommendedGain'
_P='ofmOTNContainerRepresentation'
_O='ofmRxEdfaGain'
_N='ofmRxEdfaOutputPowerTarget'
_M='ofmMaxFruGain'
_L='ofmPicDspVer'
_K='ofmActvTimingSource'
_J='ofmProvEqptType'
_I='ofmMoId'
_H='unknown'
_G='entLPPhysicalIndex'
_F='ENTITY-MIB'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-OFM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEqptType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ofmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,40))
_OfmTable_Object=MibTable
ofmTable=_OfmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1))
if mibBuilder.loadTexts:ofmTable.setStatus(_A)
_OfmEntry_Object=MibTableRow
ofmEntry=_OfmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1))
ofmEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ofmEntry.setStatus(_A)
_OfmMoId_Type=DisplayString
_OfmMoId_Object=MibTableColumn
ofmMoId=_OfmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,1),_OfmMoId_Type())
ofmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmMoId.setStatus(_A)
_OfmProvEqptType_Type=InfnEqptType
_OfmProvEqptType_Object=MibTableColumn
ofmProvEqptType=_OfmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,2),_OfmProvEqptType_Type())
ofmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmProvEqptType.setStatus(_A)
class _OfmOTNContainerRepresentation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('otuKi',1),('otuAdapti',2)))
_OfmOTNContainerRepresentation_Type.__name__=_E
_OfmOTNContainerRepresentation_Object=MibTableColumn
ofmOTNContainerRepresentation=_OfmOTNContainerRepresentation_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,3),_OfmOTNContainerRepresentation_Type())
ofmOTNContainerRepresentation.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmOTNContainerRepresentation.setStatus(_A)
_OfmActvTimingSource_Type=DisplayString
_OfmActvTimingSource_Object=MibTableColumn
ofmActvTimingSource=_OfmActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,4),_OfmActvTimingSource_Type())
ofmActvTimingSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmActvTimingSource.setStatus(_A)
_OfmPicDspVer_Type=DisplayString
_OfmPicDspVer_Object=MibTableColumn
ofmPicDspVer=_OfmPicDspVer_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,5),_OfmPicDspVer_Type())
ofmPicDspVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmPicDspVer.setStatus(_A)
_OfmMaxFruGain_Type=FloatTenths
_OfmMaxFruGain_Object=MibTableColumn
ofmMaxFruGain=_OfmMaxFruGain_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,6),_OfmMaxFruGain_Type())
ofmMaxFruGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmMaxFruGain.setStatus(_A)
_OfmRecommendedGain_Type=FloatTenths
_OfmRecommendedGain_Object=MibTableColumn
ofmRecommendedGain=_OfmRecommendedGain_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,7),_OfmRecommendedGain_Type())
ofmRecommendedGain.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmRecommendedGain.setStatus(_A)
_OfmRxEdfaOutputPowerTarget_Type=FloatTenths
_OfmRxEdfaOutputPowerTarget_Object=MibTableColumn
ofmRxEdfaOutputPowerTarget=_OfmRxEdfaOutputPowerTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,8),_OfmRxEdfaOutputPowerTarget_Type())
ofmRxEdfaOutputPowerTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmRxEdfaOutputPowerTarget.setStatus(_A)
_OfmRxEdfaGain_Type=FloatTenths
_OfmRxEdfaGain_Object=MibTableColumn
ofmRxEdfaGain=_OfmRxEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,9),_OfmRxEdfaGain_Type())
ofmRxEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmRxEdfaGain.setStatus(_A)
_OfmBwQmax_Type=FloatTenths
_OfmBwQmax_Object=MibTableColumn
ofmBwQmax=_OfmBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,10),_OfmBwQmax_Type())
ofmBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwQmax.setStatus(_A)
_OfmBwQused_Type=FloatTenths
_OfmBwQused_Object=MibTableColumn
ofmBwQused=_OfmBwQused_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,11),_OfmBwQused_Type())
ofmBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwQused.setStatus(_A)
_OfmBwQlicensed_Type=FloatTenths
_OfmBwQlicensed_Object=MibTableColumn
ofmBwQlicensed=_OfmBwQlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,12),_OfmBwQlicensed_Type())
ofmBwQlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwQlicensed.setStatus(_A)
_OfmBwBmax_Type=FloatTenths
_OfmBwBmax_Object=MibTableColumn
ofmBwBmax=_OfmBwBmax_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,13),_OfmBwBmax_Type())
ofmBwBmax.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwBmax.setStatus(_A)
_OfmBwBused_Type=FloatTenths
_OfmBwBused_Object=MibTableColumn
ofmBwBused=_OfmBwBused_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,14),_OfmBwBused_Type())
ofmBwBused.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwBused.setStatus(_A)
_OfmBwBlicensed_Type=FloatTenths
_OfmBwBlicensed_Object=MibTableColumn
ofmBwBlicensed=_OfmBwBlicensed_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,15),_OfmBwBlicensed_Type())
ofmBwBlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwBlicensed.setStatus(_A)
_OfmLicensedServicesDisabled_Type=Integer32
_OfmLicensedServicesDisabled_Object=MibTableColumn
ofmLicensedServicesDisabled=_OfmLicensedServicesDisabled_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,16),_OfmLicensedServicesDisabled_Type())
ofmLicensedServicesDisabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmLicensedServicesDisabled.setStatus(_A)
class _OfmLicenseEnforced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('notEnforced',2),('enforced',3)))
_OfmLicenseEnforced_Type.__name__=_E
_OfmLicenseEnforced_Object=MibTableColumn
ofmLicenseEnforced=_OfmLicenseEnforced_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,17),_OfmLicenseEnforced_Type())
ofmLicenseEnforced.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmLicenseEnforced.setStatus(_A)
class _OfmDefFlexLicModFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('qpsk',2),('bpsk',3),('pm3qam',4)))
_OfmDefFlexLicModFormat_Type.__name__=_E
_OfmDefFlexLicModFormat_Object=MibTableColumn
ofmDefFlexLicModFormat=_OfmDefFlexLicModFormat_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,18),_OfmDefFlexLicModFormat_Type())
ofmDefFlexLicModFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmDefFlexLicModFormat.setStatus(_A)
_OfmBwUsgWaterMarkGranularity_Type=FloatTenths
_OfmBwUsgWaterMarkGranularity_Object=MibTableColumn
ofmBwUsgWaterMarkGranularity=_OfmBwUsgWaterMarkGranularity_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,19),_OfmBwUsgWaterMarkGranularity_Type())
ofmBwUsgWaterMarkGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:ofmBwUsgWaterMarkGranularity.setStatus(_A)
_OfmAvailableTunableSuperChNumbers_Type=DisplayString
_OfmAvailableTunableSuperChNumbers_Object=MibTableColumn
ofmAvailableTunableSuperChNumbers=_OfmAvailableTunableSuperChNumbers_Object((1,3,6,1,4,1,21296,2,2,2,1,40,1,1,20),_OfmAvailableTunableSuperChNumbers_Type())
ofmAvailableTunableSuperChNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:ofmAvailableTunableSuperChNumbers.setStatus(_A)
_OfmConformance_ObjectIdentity=ObjectIdentity
ofmConformance=_OfmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,40,3))
_OfmCompliances_ObjectIdentity=ObjectIdentity
ofmCompliances=_OfmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,40,3,1))
_OfmGroups_ObjectIdentity=ObjectIdentity
ofmGroups=_OfmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,40,3,2))
ofmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,40,3,2,1))
ofmGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ofmGroup.setStatus(_A)
ofmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,40,3,1,1))
ofmCompliance.setObjects((_B,_c))
if mibBuilder.loadTexts:ofmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ofmMIB':ofmMIB,'ofmTable':ofmTable,'ofmEntry':ofmEntry,_I:ofmMoId,_J:ofmProvEqptType,_P:ofmOTNContainerRepresentation,_K:ofmActvTimingSource,_L:ofmPicDspVer,_M:ofmMaxFruGain,_Q:ofmRecommendedGain,_N:ofmRxEdfaOutputPowerTarget,_O:ofmRxEdfaGain,_R:ofmBwQmax,_S:ofmBwQused,_T:ofmBwQlicensed,_U:ofmBwBmax,_V:ofmBwBused,_W:ofmBwBlicensed,_X:ofmLicensedServicesDisabled,_Y:ofmLicenseEnforced,_Z:ofmDefFlexLicModFormat,_a:ofmBwUsgWaterMarkGranularity,_b:ofmAvailableTunableSuperChNumbers,'ofmConformance':ofmConformance,'ofmCompliances':ofmCompliances,'ofmCompliance':ofmCompliance,'ofmGroups':ofmGroups,_c:ofmGroup})