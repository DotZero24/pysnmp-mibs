_W='dcxMACSharedSecretId'
_V='dcxMACSpMgtActionIndex'
_U='dcxMACSpMgtTriggerNumber'
_T='dcxMACSpMgtTriggerIndex'
_S='dcxMACUpstreamFrequencyRegion'
_R='dcxMACUpstreamFrequencyIndex'
_Q='dcxMACUpstreamGroupId'
_P='disabled'
_O='read-only'
_N='OctetString'
_M='hertz'
_L='seconds'
_K='TimeInterval'
_J='TenthdBmV'
_I='ifIndex'
_H='IF-MIB'
_G='not-accessible'
_F='ARRIS-C3-MAC-MIB'
_E='Integer32'
_D='Unsigned32'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmtsC3,=mibBuilder.importSymbols('ARRIS-MIB','cmtsC3')
TenthdB,TenthdBmV=mibBuilder.importSymbols('DOCS-IF-MIB','TenthdB',_J)
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K,'TruthValue')
cmtsC3MACMIB=ModuleIdentity((1,3,6,1,4,1,4115,1,4,3,6))
if mibBuilder.loadTexts:cmtsC3MACMIB.setRevisions(('2004-11-21 00:00','2004-11-26 00:00','2004-12-03 00:00'))
class DocsisMacType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('docsis',1),('euroDocsis',2),('mixed',3),('custom',4)))
_DcxMACObjects_ObjectIdentity=ObjectIdentity
dcxMACObjects=_DcxMACObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,6,1))
_DcxMACCmtsMacTable_Object=MibTable
dcxMACCmtsMacTable=_DcxMACCmtsMacTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1))
if mibBuilder.loadTexts:dcxMACCmtsMacTable.setStatus(_A)
_DcxMACCmtsMacEntry_Object=MibTableRow
dcxMACCmtsMacEntry=_DcxMACCmtsMacEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1))
dcxMACCmtsMacEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dcxMACCmtsMacEntry.setStatus(_A)
_DcxMACCmtsMacMode_Type=DocsisMacType
_DcxMACCmtsMacMode_Object=MibTableColumn
dcxMACCmtsMacMode=_DcxMACCmtsMacMode_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,1),_DcxMACCmtsMacMode_Type())
dcxMACCmtsMacMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACCmtsMacMode.setStatus(_A)
class _DcxMACCableAdvanceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('dynamic',1)))
_DcxMACCableAdvanceType_Type.__name__=_E
_DcxMACCableAdvanceType_Object=MibTableColumn
dcxMACCableAdvanceType=_DcxMACCableAdvanceType_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,2),_DcxMACCableAdvanceType_Type())
dcxMACCableAdvanceType.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACCableAdvanceType.setStatus(_A)
class _DcxMACPlantLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,161))
_DcxMACPlantLength_Type.__name__=_D
_DcxMACPlantLength_Object=MibTableColumn
dcxMACPlantLength=_DcxMACPlantLength_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,3),_DcxMACPlantLength_Type())
dcxMACPlantLength.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACPlantLength.setStatus(_A)
if mibBuilder.loadTexts:dcxMACPlantLength.setUnits('kilometers')
class _DcxMACFlapAgingTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,864000))
_DcxMACFlapAgingTime_Type.__name__=_D
_DcxMACFlapAgingTime_Object=MibTableColumn
dcxMACFlapAgingTime=_DcxMACFlapAgingTime_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,4),_DcxMACFlapAgingTime_Type())
dcxMACFlapAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACFlapAgingTime.setStatus(_A)
if mibBuilder.loadTexts:dcxMACFlapAgingTime.setUnits(_L)
class _DcxMACFlapInsertTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DcxMACFlapInsertTime_Type.__name__=_D
_DcxMACFlapInsertTime_Object=MibTableColumn
dcxMACFlapInsertTime=_DcxMACFlapInsertTime_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,5),_DcxMACFlapInsertTime_Type())
dcxMACFlapInsertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACFlapInsertTime.setStatus(_A)
if mibBuilder.loadTexts:dcxMACFlapInsertTime.setUnits(_L)
class _DcxMACFlapMissThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_DcxMACFlapMissThresh_Type.__name__=_D
_DcxMACFlapMissThresh_Object=MibTableColumn
dcxMACFlapMissThresh=_DcxMACFlapMissThresh_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,6),_DcxMACFlapMissThresh_Type())
dcxMACFlapMissThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACFlapMissThresh.setStatus(_A)
if mibBuilder.loadTexts:dcxMACFlapMissThresh.setUnits('misses')
class _DcxMACFlapListSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6000))
_DcxMACFlapListSize_Type.__name__=_D
_DcxMACFlapListSize_Object=MibTableColumn
dcxMACFlapListSize=_DcxMACFlapListSize_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,8),_DcxMACFlapListSize_Type())
dcxMACFlapListSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACFlapListSize.setStatus(_A)
if mibBuilder.loadTexts:dcxMACFlapListSize.setUnits('entries')
class _DcxMACCmOfflineAgingTime_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,864000))
_DcxMACCmOfflineAgingTime_Type.__name__=_D
_DcxMACCmOfflineAgingTime_Object=MibTableColumn
dcxMACCmOfflineAgingTime=_DcxMACCmOfflineAgingTime_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,9),_DcxMACCmOfflineAgingTime_Type())
dcxMACCmOfflineAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACCmOfflineAgingTime.setStatus(_A)
if mibBuilder.loadTexts:dcxMACCmOfflineAgingTime.setUnits(_L)
class _DcxMACUccMaxFailedAttempts_Type(Unsigned32):defaultValue=2
_DcxMACUccMaxFailedAttempts_Type.__name__=_D
_DcxMACUccMaxFailedAttempts_Object=MibTableColumn
dcxMACUccMaxFailedAttempts=_DcxMACUccMaxFailedAttempts_Object((1,3,6,1,4,1,4115,1,4,3,6,1,1,1,10),_DcxMACUccMaxFailedAttempts_Type())
dcxMACUccMaxFailedAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUccMaxFailedAttempts.setStatus(_A)
_DcxMACDownstreamChannelTable_Object=MibTable
dcxMACDownstreamChannelTable=_DcxMACDownstreamChannelTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2))
if mibBuilder.loadTexts:dcxMACDownstreamChannelTable.setStatus(_A)
_DcxMACDownstreamChannelEntry_Object=MibTableRow
dcxMACDownstreamChannelEntry=_DcxMACDownstreamChannelEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1))
dcxMACDownstreamChannelEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dcxMACDownstreamChannelEntry.setStatus(_A)
_DcxMACDownChannelMacMode_Type=DocsisMacType
_DcxMACDownChannelMacMode_Object=MibTableColumn
dcxMACDownChannelMacMode=_DcxMACDownChannelMacMode_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1,1),_DcxMACDownChannelMacMode_Type())
dcxMACDownChannelMacMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACDownChannelMacMode.setStatus(_A)
class _DcxMACDownChannelUpconverter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_DcxMACDownChannelUpconverter_Type.__name__=_E
_DcxMACDownChannelUpconverter_Object=MibTableColumn
dcxMACDownChannelUpconverter=_DcxMACDownChannelUpconverter_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1,2),_DcxMACDownChannelUpconverter_Type())
dcxMACDownChannelUpconverter.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACDownChannelUpconverter.setStatus(_A)
class _DcxMACDownChannelIfFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10000000,60000000))
_DcxMACDownChannelIfFrequency_Type.__name__=_E
_DcxMACDownChannelIfFrequency_Object=MibTableColumn
dcxMACDownChannelIfFrequency=_DcxMACDownChannelIfFrequency_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1,3),_DcxMACDownChannelIfFrequency_Type())
dcxMACDownChannelIfFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACDownChannelIfFrequency.setStatus(_A)
if mibBuilder.loadTexts:dcxMACDownChannelIfFrequency.setUnits(_M)
class _DcxMACDownChannelWirelessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_DcxMACDownChannelWirelessMode_Type.__name__=_E
_DcxMACDownChannelWirelessMode_Object=MibTableColumn
dcxMACDownChannelWirelessMode=_DcxMACDownChannelWirelessMode_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1,4),_DcxMACDownChannelWirelessMode_Type())
dcxMACDownChannelWirelessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACDownChannelWirelessMode.setStatus(_A)
class _DcxMACDownChannelSymbolRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1250000,6952000))
_DcxMACDownChannelSymbolRate_Type.__name__=_E
_DcxMACDownChannelSymbolRate_Object=MibTableColumn
dcxMACDownChannelSymbolRate=_DcxMACDownChannelSymbolRate_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1,5),_DcxMACDownChannelSymbolRate_Type())
dcxMACDownChannelSymbolRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACDownChannelSymbolRate.setStatus(_A)
_DcxMACDownChannelAlpha_Type=Integer32
_DcxMACDownChannelAlpha_Object=MibTableColumn
dcxMACDownChannelAlpha=_DcxMACDownChannelAlpha_Object((1,3,6,1,4,1,4115,1,4,3,6,1,2,1,6),_DcxMACDownChannelAlpha_Type())
dcxMACDownChannelAlpha.setMaxAccess(_O)
if mibBuilder.loadTexts:dcxMACDownChannelAlpha.setStatus(_A)
if mibBuilder.loadTexts:dcxMACDownChannelAlpha.setUnits('percent')
_DcxMACUpstreamChannelTable_Object=MibTable
dcxMACUpstreamChannelTable=_DcxMACUpstreamChannelTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3))
if mibBuilder.loadTexts:dcxMACUpstreamChannelTable.setStatus(_A)
_DcxMACUpstreamChannelEntry_Object=MibTableRow
dcxMACUpstreamChannelEntry=_DcxMACUpstreamChannelEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1))
dcxMACUpstreamChannelEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dcxMACUpstreamChannelEntry.setStatus(_A)
_DcxMACUpChannelMacMode_Type=DocsisMacType
_DcxMACUpChannelMacMode_Object=MibTableColumn
dcxMACUpChannelMacMode=_DcxMACUpChannelMacMode_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,1),_DcxMACUpChannelMacMode_Type())
dcxMACUpChannelMacMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelMacMode.setStatus(_A)
_DcxMACUpChannelAmpAttenuation_Type=TenthdBmV
_DcxMACUpChannelAmpAttenuation_Object=MibTableColumn
dcxMACUpChannelAmpAttenuation=_DcxMACUpChannelAmpAttenuation_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,2),_DcxMACUpChannelAmpAttenuation_Type())
dcxMACUpChannelAmpAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelAmpAttenuation.setStatus(_A)
class _DcxMACUpChannelIngressCancellation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('tdmaOnly',2),('scdmaSec',3),('scdmaInc1',4),('scdmaInc2',5)))
_DcxMACUpChannelIngressCancellation_Type.__name__=_E
_DcxMACUpChannelIngressCancellation_Object=MibTableColumn
dcxMACUpChannelIngressCancellation=_DcxMACUpChannelIngressCancellation_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,3),_DcxMACUpChannelIngressCancellation_Type())
dcxMACUpChannelIngressCancellation.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelIngressCancellation.setStatus(_A)
_DcxMACUpChannelGroupId_Type=Unsigned32
_DcxMACUpChannelGroupId_Object=MibTableColumn
dcxMACUpChannelGroupId=_DcxMACUpChannelGroupId_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,4),_DcxMACUpChannelGroupId_Type())
dcxMACUpChannelGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelGroupId.setStatus(_A)
class _DcxMACUpChannelShortPollInterval_Type(TimeInterval):subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_DcxMACUpChannelShortPollInterval_Type.__name__=_K
_DcxMACUpChannelShortPollInterval_Object=MibTableColumn
dcxMACUpChannelShortPollInterval=_DcxMACUpChannelShortPollInterval_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,5),_DcxMACUpChannelShortPollInterval_Type())
dcxMACUpChannelShortPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelShortPollInterval.setStatus(_A)
class _DcxMACUpChannelPeriodicPollInterval_Type(TimeInterval):subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_DcxMACUpChannelPeriodicPollInterval_Type.__name__=_K
_DcxMACUpChannelPeriodicPollInterval_Object=MibTableColumn
dcxMACUpChannelPeriodicPollInterval=_DcxMACUpChannelPeriodicPollInterval_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,6),_DcxMACUpChannelPeriodicPollInterval_Type())
dcxMACUpChannelPeriodicPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelPeriodicPollInterval.setStatus(_A)
class _DcxMACUpChannelInputPowerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('automatic',2)))
_DcxMACUpChannelInputPowerMode_Type.__name__=_E
_DcxMACUpChannelInputPowerMode_Object=MibTableColumn
dcxMACUpChannelInputPowerMode=_DcxMACUpChannelInputPowerMode_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,7),_DcxMACUpChannelInputPowerMode_Type())
dcxMACUpChannelInputPowerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelInputPowerMode.setStatus(_A)
_DcxMACUpChannelPower_Type=TenthdBmV
_DcxMACUpChannelPower_Object=MibTableColumn
dcxMACUpChannelPower=_DcxMACUpChannelPower_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,8),_DcxMACUpChannelPower_Type())
dcxMACUpChannelPower.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelPower.setStatus(_A)
class _DcxMACUpChannelPlantLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,320))
_DcxMACUpChannelPlantLength_Type.__name__=_D
_DcxMACUpChannelPlantLength_Object=MibTableColumn
dcxMACUpChannelPlantLength=_DcxMACUpChannelPlantLength_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,9),_DcxMACUpChannelPlantLength_Type())
dcxMACUpChannelPlantLength.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelPlantLength.setStatus(_A)
class _DcxMACUpChannelMaxCmMapProcTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_DcxMACUpChannelMaxCmMapProcTime_Type.__name__=_D
_DcxMACUpChannelMaxCmMapProcTime_Object=MibTableColumn
dcxMACUpChannelMaxCmMapProcTime=_DcxMACUpChannelMaxCmMapProcTime_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,10),_DcxMACUpChannelMaxCmMapProcTime_Type())
dcxMACUpChannelMaxCmMapProcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelMaxCmMapProcTime.setStatus(_A)
_DcxMACUpChannelConcatenation_Type=TruthValue
_DcxMACUpChannelConcatenation_Object=MibTableColumn
dcxMACUpChannelConcatenation=_DcxMACUpChannelConcatenation_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,11),_DcxMACUpChannelConcatenation_Type())
dcxMACUpChannelConcatenation.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelConcatenation.setStatus(_A)
class _DcxMACUpChannelSpMgtTriggerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcxMACUpChannelSpMgtTriggerIndex_Type.__name__=_D
_DcxMACUpChannelSpMgtTriggerIndex_Object=MibTableColumn
dcxMACUpChannelSpMgtTriggerIndex=_DcxMACUpChannelSpMgtTriggerIndex_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,12),_DcxMACUpChannelSpMgtTriggerIndex_Type())
dcxMACUpChannelSpMgtTriggerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelSpMgtTriggerIndex.setStatus(_A)
class _DcxMACUpChannelLowPowerOffset_Type(TenthdBmV):defaultValue=-60;subtypeSpec=TenthdBmV.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,-10))
_DcxMACUpChannelLowPowerOffset_Type.__name__=_J
_DcxMACUpChannelLowPowerOffset_Object=MibTableColumn
dcxMACUpChannelLowPowerOffset=_DcxMACUpChannelLowPowerOffset_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,13),_DcxMACUpChannelLowPowerOffset_Type())
dcxMACUpChannelLowPowerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelLowPowerOffset.setStatus(_A)
class _DcxMACUpChannelHighPowerOffset_Type(TenthdBmV):defaultValue=60;subtypeSpec=TenthdBmV.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_DcxMACUpChannelHighPowerOffset_Type.__name__=_J
_DcxMACUpChannelHighPowerOffset_Object=MibTableColumn
dcxMACUpChannelHighPowerOffset=_DcxMACUpChannelHighPowerOffset_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,14),_DcxMACUpChannelHighPowerOffset_Type())
dcxMACUpChannelHighPowerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelHighPowerOffset.setStatus(_A)
class _DcxMACUpChannelLogSnrAveTimeconstant_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DcxMACUpChannelLogSnrAveTimeconstant_Type.__name__=_D
_DcxMACUpChannelLogSnrAveTimeconstant_Object=MibTableColumn
dcxMACUpChannelLogSnrAveTimeconstant=_DcxMACUpChannelLogSnrAveTimeconstant_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,15),_DcxMACUpChannelLogSnrAveTimeconstant_Type())
dcxMACUpChannelLogSnrAveTimeconstant.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelLogSnrAveTimeconstant.setStatus(_A)
class _DcxMACUpChannelImpulseMitigation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_P,2)))
_DcxMACUpChannelImpulseMitigation_Type.__name__=_E
_DcxMACUpChannelImpulseMitigation_Object=MibTableColumn
dcxMACUpChannelImpulseMitigation=_DcxMACUpChannelImpulseMitigation_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,16),_DcxMACUpChannelImpulseMitigation_Type())
dcxMACUpChannelImpulseMitigation.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelImpulseMitigation.setStatus(_A)
_DcxMACUpChannelRngPreambleGuardSymbols_Type=Unsigned32
_DcxMACUpChannelRngPreambleGuardSymbols_Object=MibTableColumn
dcxMACUpChannelRngPreambleGuardSymbols=_DcxMACUpChannelRngPreambleGuardSymbols_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,17),_DcxMACUpChannelRngPreambleGuardSymbols_Type())
dcxMACUpChannelRngPreambleGuardSymbols.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelRngPreambleGuardSymbols.setStatus(_A)
_DcxMACUpChannelNrngPreambleGuardSymbols_Type=Unsigned32
_DcxMACUpChannelNrngPreambleGuardSymbols_Object=MibTableColumn
dcxMACUpChannelNrngPreambleGuardSymbols=_DcxMACUpChannelNrngPreambleGuardSymbols_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,18),_DcxMACUpChannelNrngPreambleGuardSymbols_Type())
dcxMACUpChannelNrngPreambleGuardSymbols.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelNrngPreambleGuardSymbols.setStatus(_A)
class _DcxMACUpChannelExtendedFrequencyErrorDetect_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('initialRanging',1),('periodicRanging',2),('allRanging',3)))
_DcxMACUpChannelExtendedFrequencyErrorDetect_Type.__name__=_E
_DcxMACUpChannelExtendedFrequencyErrorDetect_Object=MibTableColumn
dcxMACUpChannelExtendedFrequencyErrorDetect=_DcxMACUpChannelExtendedFrequencyErrorDetect_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,19),_DcxMACUpChannelExtendedFrequencyErrorDetect_Type())
dcxMACUpChannelExtendedFrequencyErrorDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelExtendedFrequencyErrorDetect.setStatus(_A)
_DcxMACUpChannelLogC3SnrTimeconstant_Type=Unsigned32
_DcxMACUpChannelLogC3SnrTimeconstant_Object=MibTableColumn
dcxMACUpChannelLogC3SnrTimeconstant=_DcxMACUpChannelLogC3SnrTimeconstant_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,20),_DcxMACUpChannelLogC3SnrTimeconstant_Type())
dcxMACUpChannelLogC3SnrTimeconstant.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelLogC3SnrTimeconstant.setStatus(_A)
_DcxMACUpChannelSignalNoise_Type=TenthdB
_DcxMACUpChannelSignalNoise_Object=MibTableColumn
dcxMACUpChannelSignalNoise=_DcxMACUpChannelSignalNoise_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,21),_DcxMACUpChannelSignalNoise_Type())
dcxMACUpChannelSignalNoise.setMaxAccess(_O)
if mibBuilder.loadTexts:dcxMACUpChannelSignalNoise.setStatus(_A)
if mibBuilder.loadTexts:dcxMACUpChannelSignalNoise.setUnits('dB')
_DcxMACUpChannelSafeConfig_Type=TruthValue
_DcxMACUpChannelSafeConfig_Object=MibTableColumn
dcxMACUpChannelSafeConfig=_DcxMACUpChannelSafeConfig_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,22),_DcxMACUpChannelSafeConfig_Type())
dcxMACUpChannelSafeConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelSafeConfig.setStatus(_A)
class _DcxMACUpChannelInitialRangingDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,3000))
_DcxMACUpChannelInitialRangingDelay_Type.__name__=_D
_DcxMACUpChannelInitialRangingDelay_Object=MibTableColumn
dcxMACUpChannelInitialRangingDelay=_DcxMACUpChannelInitialRangingDelay_Object((1,3,6,1,4,1,4115,1,4,3,6,1,3,1,23),_DcxMACUpChannelInitialRangingDelay_Type())
dcxMACUpChannelInitialRangingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:dcxMACUpChannelInitialRangingDelay.setStatus(_A)
if mibBuilder.loadTexts:dcxMACUpChannelInitialRangingDelay.setUnits('microseconds')
_DcxMACUpstreamGroupTable_Object=MibTable
dcxMACUpstreamGroupTable=_DcxMACUpstreamGroupTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4))
if mibBuilder.loadTexts:dcxMACUpstreamGroupTable.setStatus(_A)
_DcxMACUpstreamGroupEntry_Object=MibTableRow
dcxMACUpstreamGroupEntry=_DcxMACUpstreamGroupEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1))
dcxMACUpstreamGroupEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:dcxMACUpstreamGroupEntry.setStatus(_A)
class _DcxMACUpstreamGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DcxMACUpstreamGroupId_Type.__name__=_D
_DcxMACUpstreamGroupId_Object=MibTableColumn
dcxMACUpstreamGroupId=_DcxMACUpstreamGroupId_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1,1),_DcxMACUpstreamGroupId_Type())
dcxMACUpstreamGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACUpstreamGroupId.setStatus(_A)
class _DcxMACUpstreamGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_DcxMACUpstreamGroupName_Type.__name__=_N
_DcxMACUpstreamGroupName_Object=MibTableColumn
dcxMACUpstreamGroupName=_DcxMACUpstreamGroupName_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1,2),_DcxMACUpstreamGroupName_Type())
dcxMACUpstreamGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamGroupName.setStatus(_A)
class _DcxMACUpstreamGroupLoadBalancing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('initialNumeric',2),('periodic',3)))
_DcxMACUpstreamGroupLoadBalancing_Type.__name__=_E
_DcxMACUpstreamGroupLoadBalancing_Object=MibTableColumn
dcxMACUpstreamGroupLoadBalancing=_DcxMACUpstreamGroupLoadBalancing_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1,3),_DcxMACUpstreamGroupLoadBalancing_Type())
dcxMACUpstreamGroupLoadBalancing.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamGroupLoadBalancing.setStatus(_A)
class _DcxMACUpstreamGroupFrequencyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcxMACUpstreamGroupFrequencyIndex_Type.__name__=_D
_DcxMACUpstreamGroupFrequencyIndex_Object=MibTableColumn
dcxMACUpstreamGroupFrequencyIndex=_DcxMACUpstreamGroupFrequencyIndex_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1,4),_DcxMACUpstreamGroupFrequencyIndex_Type())
dcxMACUpstreamGroupFrequencyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamGroupFrequencyIndex.setStatus(_A)
class _DcxMACUpstreamGroupSpMgtTriggerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcxMACUpstreamGroupSpMgtTriggerIndex_Type.__name__=_D
_DcxMACUpstreamGroupSpMgtTriggerIndex_Object=MibTableColumn
dcxMACUpstreamGroupSpMgtTriggerIndex=_DcxMACUpstreamGroupSpMgtTriggerIndex_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1,5),_DcxMACUpstreamGroupSpMgtTriggerIndex_Type())
dcxMACUpstreamGroupSpMgtTriggerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamGroupSpMgtTriggerIndex.setStatus(_A)
_DcxMACUpstreamGroupStatus_Type=RowStatus
_DcxMACUpstreamGroupStatus_Object=MibTableColumn
dcxMACUpstreamGroupStatus=_DcxMACUpstreamGroupStatus_Object((1,3,6,1,4,1,4115,1,4,3,6,1,4,1,6),_DcxMACUpstreamGroupStatus_Type())
dcxMACUpstreamGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamGroupStatus.setStatus(_A)
_DcxMACUpstreamFrequencyTable_Object=MibTable
dcxMACUpstreamFrequencyTable=_DcxMACUpstreamFrequencyTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5))
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyTable.setStatus(_A)
_DcxMACUpstreamFrequencyEntry_Object=MibTableRow
dcxMACUpstreamFrequencyEntry=_DcxMACUpstreamFrequencyEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5,1))
dcxMACUpstreamFrequencyEntry.setIndexNames((0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyEntry.setStatus(_A)
class _DcxMACUpstreamFrequencyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DcxMACUpstreamFrequencyIndex_Type.__name__=_D
_DcxMACUpstreamFrequencyIndex_Object=MibTableColumn
dcxMACUpstreamFrequencyIndex=_DcxMACUpstreamFrequencyIndex_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5,1,1),_DcxMACUpstreamFrequencyIndex_Type())
dcxMACUpstreamFrequencyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyIndex.setStatus(_A)
class _DcxMACUpstreamFrequencyRegion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DcxMACUpstreamFrequencyRegion_Type.__name__=_D
_DcxMACUpstreamFrequencyRegion_Object=MibTableColumn
dcxMACUpstreamFrequencyRegion=_DcxMACUpstreamFrequencyRegion_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5,1,2),_DcxMACUpstreamFrequencyRegion_Type())
dcxMACUpstreamFrequencyRegion.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyRegion.setStatus(_A)
_DcxMACUpstreamFrequencyStart_Type=Integer32
_DcxMACUpstreamFrequencyStart_Object=MibTableColumn
dcxMACUpstreamFrequencyStart=_DcxMACUpstreamFrequencyStart_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5,1,3),_DcxMACUpstreamFrequencyStart_Type())
dcxMACUpstreamFrequencyStart.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyStart.setStatus(_A)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyStart.setUnits(_M)
_DcxMACUpstreamFrequencyStop_Type=Integer32
_DcxMACUpstreamFrequencyStop_Object=MibTableColumn
dcxMACUpstreamFrequencyStop=_DcxMACUpstreamFrequencyStop_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5,1,4),_DcxMACUpstreamFrequencyStop_Type())
dcxMACUpstreamFrequencyStop.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyStop.setStatus(_A)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyStop.setUnits(_M)
_DcxMACUpstreamFrequencyStatus_Type=RowStatus
_DcxMACUpstreamFrequencyStatus_Object=MibTableColumn
dcxMACUpstreamFrequencyStatus=_DcxMACUpstreamFrequencyStatus_Object((1,3,6,1,4,1,4115,1,4,3,6,1,5,1,5),_DcxMACUpstreamFrequencyStatus_Type())
dcxMACUpstreamFrequencyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACUpstreamFrequencyStatus.setStatus(_A)
_DcxMACSpectralMgtObjects_ObjectIdentity=ObjectIdentity
dcxMACSpectralMgtObjects=_DcxMACSpectralMgtObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,4,3,6,1,6))
_DcxMACSpectralMgtTriggerTable_Object=MibTable
dcxMACSpectralMgtTriggerTable=_DcxMACSpectralMgtTriggerTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1))
if mibBuilder.loadTexts:dcxMACSpectralMgtTriggerTable.setStatus(_A)
_DcxMACSpectralMgtTriggerEntry_Object=MibTableRow
dcxMACSpectralMgtTriggerEntry=_DcxMACSpectralMgtTriggerEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1))
dcxMACSpectralMgtTriggerEntry.setIndexNames((0,_F,_T),(0,_F,_U))
if mibBuilder.loadTexts:dcxMACSpectralMgtTriggerEntry.setStatus(_A)
class _DcxMACSpMgtTriggerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DcxMACSpMgtTriggerIndex_Type.__name__=_D
_DcxMACSpMgtTriggerIndex_Object=MibTableColumn
dcxMACSpMgtTriggerIndex=_DcxMACSpMgtTriggerIndex_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,1),_DcxMACSpMgtTriggerIndex_Type())
dcxMACSpMgtTriggerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerIndex.setStatus(_A)
class _DcxMACSpMgtTriggerNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DcxMACSpMgtTriggerNumber_Type.__name__=_D
_DcxMACSpMgtTriggerNumber_Object=MibTableColumn
dcxMACSpMgtTriggerNumber=_DcxMACSpMgtTriggerNumber_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,2),_DcxMACSpMgtTriggerNumber_Type())
dcxMACSpMgtTriggerNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerNumber.setStatus(_A)
_DcxMACSpMgtTriggerType_Type=Integer32
_DcxMACSpMgtTriggerType_Object=MibTableColumn
dcxMACSpMgtTriggerType=_DcxMACSpMgtTriggerType_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,3),_DcxMACSpMgtTriggerType_Type())
dcxMACSpMgtTriggerType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerType.setStatus(_A)
class _DcxMACSpMgtTriggerAction_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DcxMACSpMgtTriggerAction_Type.__name__=_D
_DcxMACSpMgtTriggerAction_Object=MibTableColumn
dcxMACSpMgtTriggerAction=_DcxMACSpMgtTriggerAction_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,4),_DcxMACSpMgtTriggerAction_Type())
dcxMACSpMgtTriggerAction.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerAction.setStatus(_A)
_DcxMACSpMgtTriggerParam1_Type=Integer32
_DcxMACSpMgtTriggerParam1_Object=MibTableColumn
dcxMACSpMgtTriggerParam1=_DcxMACSpMgtTriggerParam1_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,5),_DcxMACSpMgtTriggerParam1_Type())
dcxMACSpMgtTriggerParam1.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam1.setStatus(_A)
_DcxMACSpMgtTriggerParam2_Type=Integer32
_DcxMACSpMgtTriggerParam2_Object=MibTableColumn
dcxMACSpMgtTriggerParam2=_DcxMACSpMgtTriggerParam2_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,6),_DcxMACSpMgtTriggerParam2_Type())
dcxMACSpMgtTriggerParam2.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam2.setStatus(_A)
_DcxMACSpMgtTriggerParam3_Type=Integer32
_DcxMACSpMgtTriggerParam3_Object=MibTableColumn
dcxMACSpMgtTriggerParam3=_DcxMACSpMgtTriggerParam3_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,7),_DcxMACSpMgtTriggerParam3_Type())
dcxMACSpMgtTriggerParam3.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam3.setStatus(_A)
_DcxMACSpMgtTriggerParam4_Type=Integer32
_DcxMACSpMgtTriggerParam4_Object=MibTableColumn
dcxMACSpMgtTriggerParam4=_DcxMACSpMgtTriggerParam4_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,8),_DcxMACSpMgtTriggerParam4_Type())
dcxMACSpMgtTriggerParam4.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam4.setStatus(_A)
_DcxMACSpMgtTriggerParam5_Type=Integer32
_DcxMACSpMgtTriggerParam5_Object=MibTableColumn
dcxMACSpMgtTriggerParam5=_DcxMACSpMgtTriggerParam5_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,9),_DcxMACSpMgtTriggerParam5_Type())
dcxMACSpMgtTriggerParam5.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam5.setStatus(_A)
_DcxMACSpMgtTriggerParam6_Type=Integer32
_DcxMACSpMgtTriggerParam6_Object=MibTableColumn
dcxMACSpMgtTriggerParam6=_DcxMACSpMgtTriggerParam6_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,10),_DcxMACSpMgtTriggerParam6_Type())
dcxMACSpMgtTriggerParam6.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam6.setStatus(_A)
_DcxMACSpMgtTriggerParam7_Type=Integer32
_DcxMACSpMgtTriggerParam7_Object=MibTableColumn
dcxMACSpMgtTriggerParam7=_DcxMACSpMgtTriggerParam7_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,11),_DcxMACSpMgtTriggerParam7_Type())
dcxMACSpMgtTriggerParam7.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam7.setStatus(_A)
_DcxMACSpMgtTriggerParam8_Type=Integer32
_DcxMACSpMgtTriggerParam8_Object=MibTableColumn
dcxMACSpMgtTriggerParam8=_DcxMACSpMgtTriggerParam8_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,12),_DcxMACSpMgtTriggerParam8_Type())
dcxMACSpMgtTriggerParam8.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerParam8.setStatus(_A)
_DcxMACSpMgtTriggerStatus_Type=RowStatus
_DcxMACSpMgtTriggerStatus_Object=MibTableColumn
dcxMACSpMgtTriggerStatus=_DcxMACSpMgtTriggerStatus_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,1,1,13),_DcxMACSpMgtTriggerStatus_Type())
dcxMACSpMgtTriggerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtTriggerStatus.setStatus(_A)
_DcxMACSpectralMgtActionTable_Object=MibTable
dcxMACSpectralMgtActionTable=_DcxMACSpectralMgtActionTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2))
if mibBuilder.loadTexts:dcxMACSpectralMgtActionTable.setStatus(_A)
_DcxMACSpectralMgtActionEntry_Object=MibTableRow
dcxMACSpectralMgtActionEntry=_DcxMACSpectralMgtActionEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1))
dcxMACSpectralMgtActionEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:dcxMACSpectralMgtActionEntry.setStatus(_A)
class _DcxMACSpMgtActionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DcxMACSpMgtActionIndex_Type.__name__=_D
_DcxMACSpMgtActionIndex_Object=MibTableColumn
dcxMACSpMgtActionIndex=_DcxMACSpMgtActionIndex_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,1),_DcxMACSpMgtActionIndex_Type())
dcxMACSpMgtActionIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACSpMgtActionIndex.setStatus(_A)
_DcxMACSpMgtActionType_Type=Integer32
_DcxMACSpMgtActionType_Object=MibTableColumn
dcxMACSpMgtActionType=_DcxMACSpMgtActionType_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,2),_DcxMACSpMgtActionType_Type())
dcxMACSpMgtActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionType.setStatus(_A)
_DcxMACSpMgtActionParam1_Type=Integer32
_DcxMACSpMgtActionParam1_Object=MibTableColumn
dcxMACSpMgtActionParam1=_DcxMACSpMgtActionParam1_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,3),_DcxMACSpMgtActionParam1_Type())
dcxMACSpMgtActionParam1.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam1.setStatus(_A)
_DcxMACSpMgtActionParam2_Type=Integer32
_DcxMACSpMgtActionParam2_Object=MibTableColumn
dcxMACSpMgtActionParam2=_DcxMACSpMgtActionParam2_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,4),_DcxMACSpMgtActionParam2_Type())
dcxMACSpMgtActionParam2.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam2.setStatus(_A)
_DcxMACSpMgtActionParam3_Type=Integer32
_DcxMACSpMgtActionParam3_Object=MibTableColumn
dcxMACSpMgtActionParam3=_DcxMACSpMgtActionParam3_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,5),_DcxMACSpMgtActionParam3_Type())
dcxMACSpMgtActionParam3.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam3.setStatus(_A)
_DcxMACSpMgtActionParam4_Type=Integer32
_DcxMACSpMgtActionParam4_Object=MibTableColumn
dcxMACSpMgtActionParam4=_DcxMACSpMgtActionParam4_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,6),_DcxMACSpMgtActionParam4_Type())
dcxMACSpMgtActionParam4.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam4.setStatus(_A)
_DcxMACSpMgtActionParam5_Type=Integer32
_DcxMACSpMgtActionParam5_Object=MibTableColumn
dcxMACSpMgtActionParam5=_DcxMACSpMgtActionParam5_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,7),_DcxMACSpMgtActionParam5_Type())
dcxMACSpMgtActionParam5.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam5.setStatus(_A)
_DcxMACSpMgtActionParam6_Type=Integer32
_DcxMACSpMgtActionParam6_Object=MibTableColumn
dcxMACSpMgtActionParam6=_DcxMACSpMgtActionParam6_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,8),_DcxMACSpMgtActionParam6_Type())
dcxMACSpMgtActionParam6.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam6.setStatus(_A)
_DcxMACSpMgtActionParam7_Type=Integer32
_DcxMACSpMgtActionParam7_Object=MibTableColumn
dcxMACSpMgtActionParam7=_DcxMACSpMgtActionParam7_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,9),_DcxMACSpMgtActionParam7_Type())
dcxMACSpMgtActionParam7.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam7.setStatus(_A)
_DcxMACSpMgtActionParam8_Type=Integer32
_DcxMACSpMgtActionParam8_Object=MibTableColumn
dcxMACSpMgtActionParam8=_DcxMACSpMgtActionParam8_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,10),_DcxMACSpMgtActionParam8_Type())
dcxMACSpMgtActionParam8.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionParam8.setStatus(_A)
_DcxMACSpMgtActionStatus_Type=RowStatus
_DcxMACSpMgtActionStatus_Object=MibTableColumn
dcxMACSpMgtActionStatus=_DcxMACSpMgtActionStatus_Object((1,3,6,1,4,1,4115,1,4,3,6,1,6,2,1,11),_DcxMACSpMgtActionStatus_Type())
dcxMACSpMgtActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSpMgtActionStatus.setStatus(_A)
_DcxMACSharedSecretTable_Object=MibTable
dcxMACSharedSecretTable=_DcxMACSharedSecretTable_Object((1,3,6,1,4,1,4115,1,4,3,6,1,7))
if mibBuilder.loadTexts:dcxMACSharedSecretTable.setStatus(_A)
_DcxMACSharedSecretEntry_Object=MibTableRow
dcxMACSharedSecretEntry=_DcxMACSharedSecretEntry_Object((1,3,6,1,4,1,4115,1,4,3,6,1,7,1))
dcxMACSharedSecretEntry.setIndexNames((0,_H,_I),(0,_F,_W))
if mibBuilder.loadTexts:dcxMACSharedSecretEntry.setStatus(_A)
class _DcxMACSharedSecretId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_DcxMACSharedSecretId_Type.__name__=_E
_DcxMACSharedSecretId_Object=MibTableColumn
dcxMACSharedSecretId=_DcxMACSharedSecretId_Object((1,3,6,1,4,1,4115,1,4,3,6,1,7,1,1),_DcxMACSharedSecretId_Type())
dcxMACSharedSecretId.setMaxAccess(_G)
if mibBuilder.loadTexts:dcxMACSharedSecretId.setStatus(_A)
_DcxMACSharedSecretStr_Type=DisplayString
_DcxMACSharedSecretStr_Object=MibTableColumn
dcxMACSharedSecretStr=_DcxMACSharedSecretStr_Object((1,3,6,1,4,1,4115,1,4,3,6,1,7,1,2),_DcxMACSharedSecretStr_Type())
dcxMACSharedSecretStr.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSharedSecretStr.setStatus(_A)
_DcxMACSharedSecretStatus_Type=RowStatus
_DcxMACSharedSecretStatus_Object=MibTableColumn
dcxMACSharedSecretStatus=_DcxMACSharedSecretStatus_Object((1,3,6,1,4,1,4115,1,4,3,6,1,7,1,3),_DcxMACSharedSecretStatus_Type())
dcxMACSharedSecretStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcxMACSharedSecretStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'DocsisMacType':DocsisMacType,'cmtsC3MACMIB':cmtsC3MACMIB,'dcxMACObjects':dcxMACObjects,'dcxMACCmtsMacTable':dcxMACCmtsMacTable,'dcxMACCmtsMacEntry':dcxMACCmtsMacEntry,'dcxMACCmtsMacMode':dcxMACCmtsMacMode,'dcxMACCableAdvanceType':dcxMACCableAdvanceType,'dcxMACPlantLength':dcxMACPlantLength,'dcxMACFlapAgingTime':dcxMACFlapAgingTime,'dcxMACFlapInsertTime':dcxMACFlapInsertTime,'dcxMACFlapMissThresh':dcxMACFlapMissThresh,'dcxMACFlapListSize':dcxMACFlapListSize,'dcxMACCmOfflineAgingTime':dcxMACCmOfflineAgingTime,'dcxMACUccMaxFailedAttempts':dcxMACUccMaxFailedAttempts,'dcxMACDownstreamChannelTable':dcxMACDownstreamChannelTable,'dcxMACDownstreamChannelEntry':dcxMACDownstreamChannelEntry,'dcxMACDownChannelMacMode':dcxMACDownChannelMacMode,'dcxMACDownChannelUpconverter':dcxMACDownChannelUpconverter,'dcxMACDownChannelIfFrequency':dcxMACDownChannelIfFrequency,'dcxMACDownChannelWirelessMode':dcxMACDownChannelWirelessMode,'dcxMACDownChannelSymbolRate':dcxMACDownChannelSymbolRate,'dcxMACDownChannelAlpha':dcxMACDownChannelAlpha,'dcxMACUpstreamChannelTable':dcxMACUpstreamChannelTable,'dcxMACUpstreamChannelEntry':dcxMACUpstreamChannelEntry,'dcxMACUpChannelMacMode':dcxMACUpChannelMacMode,'dcxMACUpChannelAmpAttenuation':dcxMACUpChannelAmpAttenuation,'dcxMACUpChannelIngressCancellation':dcxMACUpChannelIngressCancellation,'dcxMACUpChannelGroupId':dcxMACUpChannelGroupId,'dcxMACUpChannelShortPollInterval':dcxMACUpChannelShortPollInterval,'dcxMACUpChannelPeriodicPollInterval':dcxMACUpChannelPeriodicPollInterval,'dcxMACUpChannelInputPowerMode':dcxMACUpChannelInputPowerMode,'dcxMACUpChannelPower':dcxMACUpChannelPower,'dcxMACUpChannelPlantLength':dcxMACUpChannelPlantLength,'dcxMACUpChannelMaxCmMapProcTime':dcxMACUpChannelMaxCmMapProcTime,'dcxMACUpChannelConcatenation':dcxMACUpChannelConcatenation,'dcxMACUpChannelSpMgtTriggerIndex':dcxMACUpChannelSpMgtTriggerIndex,'dcxMACUpChannelLowPowerOffset':dcxMACUpChannelLowPowerOffset,'dcxMACUpChannelHighPowerOffset':dcxMACUpChannelHighPowerOffset,'dcxMACUpChannelLogSnrAveTimeconstant':dcxMACUpChannelLogSnrAveTimeconstant,'dcxMACUpChannelImpulseMitigation':dcxMACUpChannelImpulseMitigation,'dcxMACUpChannelRngPreambleGuardSymbols':dcxMACUpChannelRngPreambleGuardSymbols,'dcxMACUpChannelNrngPreambleGuardSymbols':dcxMACUpChannelNrngPreambleGuardSymbols,'dcxMACUpChannelExtendedFrequencyErrorDetect':dcxMACUpChannelExtendedFrequencyErrorDetect,'dcxMACUpChannelLogC3SnrTimeconstant':dcxMACUpChannelLogC3SnrTimeconstant,'dcxMACUpChannelSignalNoise':dcxMACUpChannelSignalNoise,'dcxMACUpChannelSafeConfig':dcxMACUpChannelSafeConfig,'dcxMACUpChannelInitialRangingDelay':dcxMACUpChannelInitialRangingDelay,'dcxMACUpstreamGroupTable':dcxMACUpstreamGroupTable,'dcxMACUpstreamGroupEntry':dcxMACUpstreamGroupEntry,_Q:dcxMACUpstreamGroupId,'dcxMACUpstreamGroupName':dcxMACUpstreamGroupName,'dcxMACUpstreamGroupLoadBalancing':dcxMACUpstreamGroupLoadBalancing,'dcxMACUpstreamGroupFrequencyIndex':dcxMACUpstreamGroupFrequencyIndex,'dcxMACUpstreamGroupSpMgtTriggerIndex':dcxMACUpstreamGroupSpMgtTriggerIndex,'dcxMACUpstreamGroupStatus':dcxMACUpstreamGroupStatus,'dcxMACUpstreamFrequencyTable':dcxMACUpstreamFrequencyTable,'dcxMACUpstreamFrequencyEntry':dcxMACUpstreamFrequencyEntry,_R:dcxMACUpstreamFrequencyIndex,_S:dcxMACUpstreamFrequencyRegion,'dcxMACUpstreamFrequencyStart':dcxMACUpstreamFrequencyStart,'dcxMACUpstreamFrequencyStop':dcxMACUpstreamFrequencyStop,'dcxMACUpstreamFrequencyStatus':dcxMACUpstreamFrequencyStatus,'dcxMACSpectralMgtObjects':dcxMACSpectralMgtObjects,'dcxMACSpectralMgtTriggerTable':dcxMACSpectralMgtTriggerTable,'dcxMACSpectralMgtTriggerEntry':dcxMACSpectralMgtTriggerEntry,_T:dcxMACSpMgtTriggerIndex,_U:dcxMACSpMgtTriggerNumber,'dcxMACSpMgtTriggerType':dcxMACSpMgtTriggerType,'dcxMACSpMgtTriggerAction':dcxMACSpMgtTriggerAction,'dcxMACSpMgtTriggerParam1':dcxMACSpMgtTriggerParam1,'dcxMACSpMgtTriggerParam2':dcxMACSpMgtTriggerParam2,'dcxMACSpMgtTriggerParam3':dcxMACSpMgtTriggerParam3,'dcxMACSpMgtTriggerParam4':dcxMACSpMgtTriggerParam4,'dcxMACSpMgtTriggerParam5':dcxMACSpMgtTriggerParam5,'dcxMACSpMgtTriggerParam6':dcxMACSpMgtTriggerParam6,'dcxMACSpMgtTriggerParam7':dcxMACSpMgtTriggerParam7,'dcxMACSpMgtTriggerParam8':dcxMACSpMgtTriggerParam8,'dcxMACSpMgtTriggerStatus':dcxMACSpMgtTriggerStatus,'dcxMACSpectralMgtActionTable':dcxMACSpectralMgtActionTable,'dcxMACSpectralMgtActionEntry':dcxMACSpectralMgtActionEntry,_V:dcxMACSpMgtActionIndex,'dcxMACSpMgtActionType':dcxMACSpMgtActionType,'dcxMACSpMgtActionParam1':dcxMACSpMgtActionParam1,'dcxMACSpMgtActionParam2':dcxMACSpMgtActionParam2,'dcxMACSpMgtActionParam3':dcxMACSpMgtActionParam3,'dcxMACSpMgtActionParam4':dcxMACSpMgtActionParam4,'dcxMACSpMgtActionParam5':dcxMACSpMgtActionParam5,'dcxMACSpMgtActionParam6':dcxMACSpMgtActionParam6,'dcxMACSpMgtActionParam7':dcxMACSpMgtActionParam7,'dcxMACSpMgtActionParam8':dcxMACSpMgtActionParam8,'dcxMACSpMgtActionStatus':dcxMACSpMgtActionStatus,'dcxMACSharedSecretTable':dcxMACSharedSecretTable,'dcxMACSharedSecretEntry':dcxMACSharedSecretEntry,_W:dcxMACSharedSecretId,'dcxMACSharedSecretStr':dcxMACSharedSecretStr,'dcxMACSharedSecretStatus':dcxMACSharedSecretStatus})