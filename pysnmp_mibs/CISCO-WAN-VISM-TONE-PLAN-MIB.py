_A1='vismSequentialToneDetectGroup'
_A0='vismConfigToneDetectTableGroup'
_z='vismTonePlanTableGroup'
_y='vismTonePlanControlGroup'
_x='seqToneFrequency10'
_w='seqToneFrequency9'
_v='seqToneFrequency8'
_u='seqToneFrequency7'
_t='seqToneFrequency6'
_s='seqToneFrequency5'
_r='seqToneFrequency4'
_q='seqToneFrequency3'
_p='seqToneFrequency2'
_o='seqToneFrequency1'
_n='seqTonePowerLevelFloor'
_m='seqTonePowerLevelCeiling'
_l='seqToneFreqDeviation'
_k='seqToneGapDurationDeviation'
_j='seqToneMaximumGapDuration'
_i='seqToneDurationDeviation'
_h='seqToneGapBetweenEachTone'
_g='seqToneDurationOfEachTone'
_f='seqToneEventID'
_e='seqToneNumOfFrequencies'
_d='vismFreqOffCadence'
_c='vismFreqOnCadence'
_b='vismFrequency2'
_a='vismFrequency1'
_Z='vismFreqNumOfCadenceMatch'
_Y='vismMaxOffCadence'
_X='vismMinOnCadence'
_W='vismFreqMaxDelay'
_V='vismFreqPowerTwist'
_U='vismFreqMinPower'
_T='vismFreqMaxPower'
_S='vismFreqMaxDeviation'
_R='vismConfigToneDetectRowStatus'
_Q='vismEventCode'
_P='tonePlanFileName'
_O='tonePlanVersionNumber'
_N='tonePlanRegionName'
_M='tonePlanProvisionFlag'
_L='tonePlanEntryStatus'
_K='tonePlanCurrentSize'
_J='tonePlanIndex'
_I='vismConfigToneDetectNum'
_H='read-only'
_G='DisplayString'
_F='milliseconds'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-VISM-TONE-PLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
vismTonePlanGrpMIB=ModuleIdentity((1,3,6,1,4,1,351,150,24))
if mibBuilder.loadTexts:vismTonePlanGrpMIB.setRevisions(('2003-12-17 00:00','2003-04-23 00:00','2002-07-19 00:00','2001-12-26 00:00','2001-08-05 00:00','2001-04-03 00:00'))
_VismTonePlanGrpMIBObjects_ObjectIdentity=ObjectIdentity
vismTonePlanGrpMIBObjects=_VismTonePlanGrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,24,1))
_VismTonePlan_ObjectIdentity=ObjectIdentity
vismTonePlan=_VismTonePlan_ObjectIdentity((1,3,6,1,4,1,351,150,24,1,1))
_VismTonePlanControlGrp_ObjectIdentity=ObjectIdentity
vismTonePlanControlGrp=_VismTonePlanControlGrp_ObjectIdentity((1,3,6,1,4,1,351,150,24,1,1,1))
_TonePlanCurrentSize_Type=Integer32
_TonePlanCurrentSize_Object=MibScalar
tonePlanCurrentSize=_TonePlanCurrentSize_Object((1,3,6,1,4,1,351,150,24,1,1,1,1),_TonePlanCurrentSize_Type())
tonePlanCurrentSize.setMaxAccess(_H)
if mibBuilder.loadTexts:tonePlanCurrentSize.setStatus(_A)
_VismTonePlanTableGrp_ObjectIdentity=ObjectIdentity
vismTonePlanTableGrp=_VismTonePlanTableGrp_ObjectIdentity((1,3,6,1,4,1,351,150,24,1,1,2))
_VismTonePlanTable_Object=MibTable
vismTonePlanTable=_VismTonePlanTable_Object((1,3,6,1,4,1,351,150,24,1,1,2,1))
if mibBuilder.loadTexts:vismTonePlanTable.setStatus(_A)
_VismTonePlanEntry_Object=MibTableRow
vismTonePlanEntry=_VismTonePlanEntry_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1))
vismTonePlanEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:vismTonePlanEntry.setStatus(_A)
class _TonePlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TonePlanIndex_Type.__name__=_C
_TonePlanIndex_Object=MibTableColumn
tonePlanIndex=_TonePlanIndex_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1,1),_TonePlanIndex_Type())
tonePlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tonePlanIndex.setStatus(_A)
class _TonePlanEntryStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unused',1),('configured',2),('reloading',3),('lostFile',4)))
_TonePlanEntryStatus_Type.__name__=_C
_TonePlanEntryStatus_Object=MibTableColumn
tonePlanEntryStatus=_TonePlanEntryStatus_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1,2),_TonePlanEntryStatus_Type())
tonePlanEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tonePlanEntryStatus.setStatus(_A)
class _TonePlanProvisionFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('builtIn',1),('provisionable',2)))
_TonePlanProvisionFlag_Type.__name__=_C
_TonePlanProvisionFlag_Object=MibTableColumn
tonePlanProvisionFlag=_TonePlanProvisionFlag_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1,3),_TonePlanProvisionFlag_Type())
tonePlanProvisionFlag.setMaxAccess(_H)
if mibBuilder.loadTexts:tonePlanProvisionFlag.setStatus(_A)
class _TonePlanRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_TonePlanRegionName_Type.__name__=_G
_TonePlanRegionName_Object=MibTableColumn
tonePlanRegionName=_TonePlanRegionName_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1,4),_TonePlanRegionName_Type())
tonePlanRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:tonePlanRegionName.setStatus(_A)
class _TonePlanVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TonePlanVersionNumber_Type.__name__=_C
_TonePlanVersionNumber_Object=MibTableColumn
tonePlanVersionNumber=_TonePlanVersionNumber_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1,5),_TonePlanVersionNumber_Type())
tonePlanVersionNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:tonePlanVersionNumber.setStatus(_A)
class _TonePlanFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TonePlanFileName_Type.__name__=_G
_TonePlanFileName_Object=MibTableColumn
tonePlanFileName=_TonePlanFileName_Object((1,3,6,1,4,1,351,150,24,1,1,2,1,1,6),_TonePlanFileName_Type())
tonePlanFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:tonePlanFileName.setStatus(_A)
_VismConfigToneDetectGrp_ObjectIdentity=ObjectIdentity
vismConfigToneDetectGrp=_VismConfigToneDetectGrp_ObjectIdentity((1,3,6,1,4,1,351,150,24,1,1,3))
_VismConfigToneDetectTable_Object=MibTable
vismConfigToneDetectTable=_VismConfigToneDetectTable_Object((1,3,6,1,4,1,351,150,24,1,1,3,1))
if mibBuilder.loadTexts:vismConfigToneDetectTable.setStatus(_A)
_VismConfigToneDetectEntry_Object=MibTableRow
vismConfigToneDetectEntry=_VismConfigToneDetectEntry_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1))
vismConfigToneDetectEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:vismConfigToneDetectEntry.setStatus(_A)
class _VismConfigToneDetectNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VismConfigToneDetectNum_Type.__name__=_C
_VismConfigToneDetectNum_Object=MibTableColumn
vismConfigToneDetectNum=_VismConfigToneDetectNum_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,1),_VismConfigToneDetectNum_Type())
vismConfigToneDetectNum.setMaxAccess(_H)
if mibBuilder.loadTexts:vismConfigToneDetectNum.setStatus(_A)
class _VismEventCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismEventCode_Type.__name__=_C
_VismEventCode_Object=MibTableColumn
vismEventCode=_VismEventCode_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,2),_VismEventCode_Type())
vismEventCode.setMaxAccess(_E)
if mibBuilder.loadTexts:vismEventCode.setStatus(_A)
_VismConfigToneDetectRowStatus_Type=RowStatus
_VismConfigToneDetectRowStatus_Object=MibTableColumn
vismConfigToneDetectRowStatus=_VismConfigToneDetectRowStatus_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,3),_VismConfigToneDetectRowStatus_Type())
vismConfigToneDetectRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismConfigToneDetectRowStatus.setStatus(_A)
class _VismFreqMaxDeviation_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,125))
_VismFreqMaxDeviation_Type.__name__=_C
_VismFreqMaxDeviation_Object=MibTableColumn
vismFreqMaxDeviation=_VismFreqMaxDeviation_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,4),_VismFreqMaxDeviation_Type())
vismFreqMaxDeviation.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqMaxDeviation.setStatus(_A)
if mibBuilder.loadTexts:vismFreqMaxDeviation.setUnits('Hz')
class _VismFreqMaxPower_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_VismFreqMaxPower_Type.__name__=_C
_VismFreqMaxPower_Object=MibTableColumn
vismFreqMaxPower=_VismFreqMaxPower_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,5),_VismFreqMaxPower_Type())
vismFreqMaxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqMaxPower.setStatus(_A)
if mibBuilder.loadTexts:vismFreqMaxPower.setUnits('dB')
class _VismFreqMinPower_Type(Integer32):defaultValue=35;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,35))
_VismFreqMinPower_Type.__name__=_C
_VismFreqMinPower_Object=MibTableColumn
vismFreqMinPower=_VismFreqMinPower_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,6),_VismFreqMinPower_Type())
vismFreqMinPower.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqMinPower.setStatus(_A)
if mibBuilder.loadTexts:vismFreqMinPower.setUnits('dB')
class _VismFreqPowerTwist_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_VismFreqPowerTwist_Type.__name__=_C
_VismFreqPowerTwist_Object=MibTableColumn
vismFreqPowerTwist=_VismFreqPowerTwist_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,7),_VismFreqPowerTwist_Type())
vismFreqPowerTwist.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqPowerTwist.setStatus(_A)
if mibBuilder.loadTexts:vismFreqPowerTwist.setUnits('dB')
class _VismFreqMaxDelay_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismFreqMaxDelay_Type.__name__=_C
_VismFreqMaxDelay_Object=MibTableColumn
vismFreqMaxDelay=_VismFreqMaxDelay_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,8),_VismFreqMaxDelay_Type())
vismFreqMaxDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqMaxDelay.setStatus(_A)
if mibBuilder.loadTexts:vismFreqMaxDelay.setUnits(_F)
class _VismMinOnCadence_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_VismMinOnCadence_Type.__name__=_C
_VismMinOnCadence_Object=MibTableColumn
vismMinOnCadence=_VismMinOnCadence_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,9),_VismMinOnCadence_Type())
vismMinOnCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:vismMinOnCadence.setStatus(_A)
if mibBuilder.loadTexts:vismMinOnCadence.setUnits(_F)
class _VismMaxOffCadence_Type(Integer32):defaultValue=450;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5000))
_VismMaxOffCadence_Type.__name__=_C
_VismMaxOffCadence_Object=MibTableColumn
vismMaxOffCadence=_VismMaxOffCadence_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,10),_VismMaxOffCadence_Type())
vismMaxOffCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:vismMaxOffCadence.setStatus(_A)
class _VismFreqNumOfCadenceMatch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_VismFreqNumOfCadenceMatch_Type.__name__=_C
_VismFreqNumOfCadenceMatch_Object=MibTableColumn
vismFreqNumOfCadenceMatch=_VismFreqNumOfCadenceMatch_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,11),_VismFreqNumOfCadenceMatch_Type())
vismFreqNumOfCadenceMatch.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqNumOfCadenceMatch.setStatus(_A)
class _VismFrequency1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_VismFrequency1_Type.__name__=_C
_VismFrequency1_Object=MibTableColumn
vismFrequency1=_VismFrequency1_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,12),_VismFrequency1_Type())
vismFrequency1.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFrequency1.setStatus(_A)
if mibBuilder.loadTexts:vismFrequency1.setUnits('Hz')
class _VismFrequency2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3800))
_VismFrequency2_Type.__name__=_C
_VismFrequency2_Object=MibTableColumn
vismFrequency2=_VismFrequency2_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,13),_VismFrequency2_Type())
vismFrequency2.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFrequency2.setStatus(_A)
if mibBuilder.loadTexts:vismFrequency2.setUnits('Hz')
class _VismFreqOnCadence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5000))
_VismFreqOnCadence_Type.__name__=_C
_VismFreqOnCadence_Object=MibTableColumn
vismFreqOnCadence=_VismFreqOnCadence_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,14),_VismFreqOnCadence_Type())
vismFreqOnCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqOnCadence.setStatus(_A)
if mibBuilder.loadTexts:vismFreqOnCadence.setUnits(_F)
class _VismFreqOffCadence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5000))
_VismFreqOffCadence_Type.__name__=_C
_VismFreqOffCadence_Object=MibTableColumn
vismFreqOffCadence=_VismFreqOffCadence_Object((1,3,6,1,4,1,351,150,24,1,1,3,1,1,15),_VismFreqOffCadence_Type())
vismFreqOffCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFreqOffCadence.setStatus(_A)
if mibBuilder.loadTexts:vismFreqOffCadence.setUnits(_F)
_VismSequentialToneDetectGrp_ObjectIdentity=ObjectIdentity
vismSequentialToneDetectGrp=_VismSequentialToneDetectGrp_ObjectIdentity((1,3,6,1,4,1,351,150,24,1,1,4))
class _SeqToneNumOfFrequencies_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SeqToneNumOfFrequencies_Type.__name__=_C
_SeqToneNumOfFrequencies_Object=MibScalar
seqToneNumOfFrequencies=_SeqToneNumOfFrequencies_Object((1,3,6,1,4,1,351,150,24,1,1,4,1),_SeqToneNumOfFrequencies_Type())
seqToneNumOfFrequencies.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneNumOfFrequencies.setStatus(_A)
class _SeqToneEventID_Type(Integer32):defaultValue=74;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SeqToneEventID_Type.__name__=_C
_SeqToneEventID_Object=MibScalar
seqToneEventID=_SeqToneEventID_Object((1,3,6,1,4,1,351,150,24,1,1,4,2),_SeqToneEventID_Type())
seqToneEventID.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneEventID.setStatus(_A)
class _SeqToneDurationOfEachTone_Type(Integer32):defaultValue=33;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_SeqToneDurationOfEachTone_Type.__name__=_C
_SeqToneDurationOfEachTone_Object=MibScalar
seqToneDurationOfEachTone=_SeqToneDurationOfEachTone_Object((1,3,6,1,4,1,351,150,24,1,1,4,3),_SeqToneDurationOfEachTone_Type())
seqToneDurationOfEachTone.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneDurationOfEachTone.setStatus(_A)
class _SeqToneGapBetweenEachTone_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_SeqToneGapBetweenEachTone_Type.__name__=_C
_SeqToneGapBetweenEachTone_Object=MibScalar
seqToneGapBetweenEachTone=_SeqToneGapBetweenEachTone_Object((1,3,6,1,4,1,351,150,24,1,1,4,4),_SeqToneGapBetweenEachTone_Type())
seqToneGapBetweenEachTone.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneGapBetweenEachTone.setStatus(_A)
class _SeqToneDurationDeviation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SeqToneDurationDeviation_Type.__name__=_C
_SeqToneDurationDeviation_Object=MibScalar
seqToneDurationDeviation=_SeqToneDurationDeviation_Object((1,3,6,1,4,1,351,150,24,1,1,4,5),_SeqToneDurationDeviation_Type())
seqToneDurationDeviation.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneDurationDeviation.setStatus(_A)
class _SeqToneMaximumGapDuration_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SeqToneMaximumGapDuration_Type.__name__=_C
_SeqToneMaximumGapDuration_Object=MibScalar
seqToneMaximumGapDuration=_SeqToneMaximumGapDuration_Object((1,3,6,1,4,1,351,150,24,1,1,4,6),_SeqToneMaximumGapDuration_Type())
seqToneMaximumGapDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneMaximumGapDuration.setStatus(_A)
class _SeqToneGapDurationDeviation_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SeqToneGapDurationDeviation_Type.__name__=_C
_SeqToneGapDurationDeviation_Object=MibScalar
seqToneGapDurationDeviation=_SeqToneGapDurationDeviation_Object((1,3,6,1,4,1,351,150,24,1,1,4,7),_SeqToneGapDurationDeviation_Type())
seqToneGapDurationDeviation.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneGapDurationDeviation.setStatus(_A)
class _SeqToneFreqDeviation_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_SeqToneFreqDeviation_Type.__name__=_C
_SeqToneFreqDeviation_Object=MibScalar
seqToneFreqDeviation=_SeqToneFreqDeviation_Object((1,3,6,1,4,1,351,150,24,1,1,4,8),_SeqToneFreqDeviation_Type())
seqToneFreqDeviation.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFreqDeviation.setStatus(_A)
class _SeqTonePowerLevelCeiling_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_SeqTonePowerLevelCeiling_Type.__name__=_C
_SeqTonePowerLevelCeiling_Object=MibScalar
seqTonePowerLevelCeiling=_SeqTonePowerLevelCeiling_Object((1,3,6,1,4,1,351,150,24,1,1,4,9),_SeqTonePowerLevelCeiling_Type())
seqTonePowerLevelCeiling.setMaxAccess(_D)
if mibBuilder.loadTexts:seqTonePowerLevelCeiling.setStatus(_A)
class _SeqTonePowerLevelFloor_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,40))
_SeqTonePowerLevelFloor_Type.__name__=_C
_SeqTonePowerLevelFloor_Object=MibScalar
seqTonePowerLevelFloor=_SeqTonePowerLevelFloor_Object((1,3,6,1,4,1,351,150,24,1,1,4,10),_SeqTonePowerLevelFloor_Type())
seqTonePowerLevelFloor.setMaxAccess(_D)
if mibBuilder.loadTexts:seqTonePowerLevelFloor.setStatus(_A)
class _SeqToneFrequency1_Type(Integer32):defaultValue=950;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency1_Type.__name__=_C
_SeqToneFrequency1_Object=MibScalar
seqToneFrequency1=_SeqToneFrequency1_Object((1,3,6,1,4,1,351,150,24,1,1,4,11),_SeqToneFrequency1_Type())
seqToneFrequency1.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency1.setStatus(_A)
class _SeqToneFrequency2_Type(Integer32):defaultValue=1400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency2_Type.__name__=_C
_SeqToneFrequency2_Object=MibScalar
seqToneFrequency2=_SeqToneFrequency2_Object((1,3,6,1,4,1,351,150,24,1,1,4,12),_SeqToneFrequency2_Type())
seqToneFrequency2.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency2.setStatus(_A)
class _SeqToneFrequency3_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency3_Type.__name__=_C
_SeqToneFrequency3_Object=MibScalar
seqToneFrequency3=_SeqToneFrequency3_Object((1,3,6,1,4,1,351,150,24,1,1,4,13),_SeqToneFrequency3_Type())
seqToneFrequency3.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency3.setStatus(_A)
class _SeqToneFrequency4_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency4_Type.__name__=_C
_SeqToneFrequency4_Object=MibScalar
seqToneFrequency4=_SeqToneFrequency4_Object((1,3,6,1,4,1,351,150,24,1,1,4,14),_SeqToneFrequency4_Type())
seqToneFrequency4.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency4.setStatus(_A)
class _SeqToneFrequency5_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency5_Type.__name__=_C
_SeqToneFrequency5_Object=MibScalar
seqToneFrequency5=_SeqToneFrequency5_Object((1,3,6,1,4,1,351,150,24,1,1,4,15),_SeqToneFrequency5_Type())
seqToneFrequency5.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency5.setStatus(_A)
class _SeqToneFrequency6_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency6_Type.__name__=_C
_SeqToneFrequency6_Object=MibScalar
seqToneFrequency6=_SeqToneFrequency6_Object((1,3,6,1,4,1,351,150,24,1,1,4,16),_SeqToneFrequency6_Type())
seqToneFrequency6.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency6.setStatus(_A)
class _SeqToneFrequency7_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency7_Type.__name__=_C
_SeqToneFrequency7_Object=MibScalar
seqToneFrequency7=_SeqToneFrequency7_Object((1,3,6,1,4,1,351,150,24,1,1,4,17),_SeqToneFrequency7_Type())
seqToneFrequency7.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency7.setStatus(_A)
class _SeqToneFrequency8_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency8_Type.__name__=_C
_SeqToneFrequency8_Object=MibScalar
seqToneFrequency8=_SeqToneFrequency8_Object((1,3,6,1,4,1,351,150,24,1,1,4,18),_SeqToneFrequency8_Type())
seqToneFrequency8.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency8.setStatus(_A)
class _SeqToneFrequency9_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency9_Type.__name__=_C
_SeqToneFrequency9_Object=MibScalar
seqToneFrequency9=_SeqToneFrequency9_Object((1,3,6,1,4,1,351,150,24,1,1,4,19),_SeqToneFrequency9_Type())
seqToneFrequency9.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency9.setStatus(_A)
class _SeqToneFrequency10_Type(Integer32):defaultValue=280;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(280,3800))
_SeqToneFrequency10_Type.__name__=_C
_SeqToneFrequency10_Object=MibScalar
seqToneFrequency10=_SeqToneFrequency10_Object((1,3,6,1,4,1,351,150,24,1,1,4,20),_SeqToneFrequency10_Type())
seqToneFrequency10.setMaxAccess(_D)
if mibBuilder.loadTexts:seqToneFrequency10.setStatus(_A)
_VismToneNotificationPrefix_ObjectIdentity=ObjectIdentity
vismToneNotificationPrefix=_VismToneNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,24,2))
_VismToneNotifications_ObjectIdentity=ObjectIdentity
vismToneNotifications=_VismToneNotifications_ObjectIdentity((1,3,6,1,4,1,351,150,24,2,0))
_VismTonePlanMIBConformance_ObjectIdentity=ObjectIdentity
vismTonePlanMIBConformance=_VismTonePlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,24,3))
_VismTonePlanMIBCompliances_ObjectIdentity=ObjectIdentity
vismTonePlanMIBCompliances=_VismTonePlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,24,3,1))
_VismTonePlanMIBGroups_ObjectIdentity=ObjectIdentity
vismTonePlanMIBGroups=_VismTonePlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,24,3,2))
vismTonePlanControlGroup=ObjectGroup((1,3,6,1,4,1,351,150,24,3,2,1))
vismTonePlanControlGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:vismTonePlanControlGroup.setStatus(_A)
vismTonePlanTableGroup=ObjectGroup((1,3,6,1,4,1,351,150,24,3,2,2))
vismTonePlanTableGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:vismTonePlanTableGroup.setStatus(_A)
vismConfigToneDetectTableGroup=ObjectGroup((1,3,6,1,4,1,351,150,24,3,2,3))
vismConfigToneDetectTableGroup.setObjects(*((_B,_I),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:vismConfigToneDetectTableGroup.setStatus(_A)
vismSequentialToneDetectGroup=ObjectGroup((1,3,6,1,4,1,351,150,24,3,2,4))
vismSequentialToneDetectGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:vismSequentialToneDetectGroup.setStatus(_A)
vismTonePlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,24,3,1,1))
vismTonePlanMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:vismTonePlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismTonePlanGrpMIB':vismTonePlanGrpMIB,'vismTonePlanGrpMIBObjects':vismTonePlanGrpMIBObjects,'vismTonePlan':vismTonePlan,'vismTonePlanControlGrp':vismTonePlanControlGrp,_K:tonePlanCurrentSize,'vismTonePlanTableGrp':vismTonePlanTableGrp,'vismTonePlanTable':vismTonePlanTable,'vismTonePlanEntry':vismTonePlanEntry,_J:tonePlanIndex,_L:tonePlanEntryStatus,_M:tonePlanProvisionFlag,_N:tonePlanRegionName,_O:tonePlanVersionNumber,_P:tonePlanFileName,'vismConfigToneDetectGrp':vismConfigToneDetectGrp,'vismConfigToneDetectTable':vismConfigToneDetectTable,'vismConfigToneDetectEntry':vismConfigToneDetectEntry,_I:vismConfigToneDetectNum,_Q:vismEventCode,_R:vismConfigToneDetectRowStatus,_S:vismFreqMaxDeviation,_T:vismFreqMaxPower,_U:vismFreqMinPower,_V:vismFreqPowerTwist,_W:vismFreqMaxDelay,_X:vismMinOnCadence,_Y:vismMaxOffCadence,_Z:vismFreqNumOfCadenceMatch,_a:vismFrequency1,_b:vismFrequency2,_c:vismFreqOnCadence,_d:vismFreqOffCadence,'vismSequentialToneDetectGrp':vismSequentialToneDetectGrp,_e:seqToneNumOfFrequencies,_f:seqToneEventID,_g:seqToneDurationOfEachTone,_h:seqToneGapBetweenEachTone,_i:seqToneDurationDeviation,_j:seqToneMaximumGapDuration,_k:seqToneGapDurationDeviation,_l:seqToneFreqDeviation,_m:seqTonePowerLevelCeiling,_n:seqTonePowerLevelFloor,_o:seqToneFrequency1,_p:seqToneFrequency2,_q:seqToneFrequency3,_r:seqToneFrequency4,_s:seqToneFrequency5,_t:seqToneFrequency6,_u:seqToneFrequency7,_v:seqToneFrequency8,_w:seqToneFrequency9,_x:seqToneFrequency10,'vismToneNotificationPrefix':vismToneNotificationPrefix,'vismToneNotifications':vismToneNotifications,'vismTonePlanMIBConformance':vismTonePlanMIBConformance,'vismTonePlanMIBCompliances':vismTonePlanMIBCompliances,'vismTonePlanMIBCompliance':vismTonePlanMIBCompliance,'vismTonePlanMIBGroups':vismTonePlanMIBGroups,_y:vismTonePlanControlGroup,_z:vismTonePlanTableGroup,_A0:vismConfigToneDetectTableGroup,_A1:vismSequentialToneDetectGroup})