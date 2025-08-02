_L='acPMAtmCellDiscardedInterval'
_K='acPMAtmCellDiscardedInterface'
_J='acPMAtmCellRxInterval'
_I='acPMAtmCellRxInterface'
_H='acPMAtmCellTxInterval'
_G='acPMAtmCellTxInterface'
_F='not-accessible'
_E='read-write'
_D='AC-PM-ATM-MIB'
_C='read-only'
_B='Integer32'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
acPMAtm=ModuleIdentity((1,3,6,1,4,1,5003,10,12))
if mibBuilder.loadTexts:acPMAtm.setRevisions(('2010-06-04 15:28',))
_AudioCodes_ObjectIdentity=ObjectIdentity
audioCodes=_AudioCodes_ObjectIdentity((1,3,6,1,4,1,5003))
_AcRegistrations_ObjectIdentity=ObjectIdentity
acRegistrations=_AcRegistrations_ObjectIdentity((1,3,6,1,4,1,5003,7))
_AcGeneric_ObjectIdentity=ObjectIdentity
acGeneric=_AcGeneric_ObjectIdentity((1,3,6,1,4,1,5003,8))
_AcProducts_ObjectIdentity=ObjectIdentity
acProducts=_AcProducts_ObjectIdentity((1,3,6,1,4,1,5003,9))
_AcPerformance_ObjectIdentity=ObjectIdentity
acPerformance=_AcPerformance_ObjectIdentity((1,3,6,1,4,1,5003,10))
_AcPMAtmConfiguration_ObjectIdentity=ObjectIdentity
acPMAtmConfiguration=_AcPMAtmConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,10,12,1))
class _AcPMAtmConfigurationPeriodLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,894780))
_AcPMAtmConfigurationPeriodLength_Type.__name__=_B
_AcPMAtmConfigurationPeriodLength_Object=MibScalar
acPMAtmConfigurationPeriodLength=_AcPMAtmConfigurationPeriodLength_Object((1,3,6,1,4,1,5003,10,12,1,1),_AcPMAtmConfigurationPeriodLength_Type())
acPMAtmConfigurationPeriodLength.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAtmConfigurationPeriodLength.setStatus(_A)
class _AcPMAtmConfigurationResetTotalCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('resetCountersDone',1),('resetTotalCounters',2)))
_AcPMAtmConfigurationResetTotalCounters_Type.__name__=_B
_AcPMAtmConfigurationResetTotalCounters_Object=MibScalar
acPMAtmConfigurationResetTotalCounters=_AcPMAtmConfigurationResetTotalCounters_Object((1,3,6,1,4,1,5003,10,12,1,2),_AcPMAtmConfigurationResetTotalCounters_Type())
acPMAtmConfigurationResetTotalCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAtmConfigurationResetTotalCounters.setStatus(_A)
_AcPMAtmCellAttributes_ObjectIdentity=ObjectIdentity
acPMAtmCellAttributes=_AcPMAtmCellAttributes_ObjectIdentity((1,3,6,1,4,1,5003,10,12,1,31))
class _AcPMAtmCellAttributesTxHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_AcPMAtmCellAttributesTxHighThreshold_Type.__name__=_B
_AcPMAtmCellAttributesTxHighThreshold_Object=MibScalar
acPMAtmCellAttributesTxHighThreshold=_AcPMAtmCellAttributesTxHighThreshold_Object((1,3,6,1,4,1,5003,10,12,1,31,1),_AcPMAtmCellAttributesTxHighThreshold_Type())
acPMAtmCellAttributesTxHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAtmCellAttributesTxHighThreshold.setStatus(_A)
class _AcPMAtmCellAttributesTxLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_AcPMAtmCellAttributesTxLowThreshold_Type.__name__=_B
_AcPMAtmCellAttributesTxLowThreshold_Object=MibScalar
acPMAtmCellAttributesTxLowThreshold=_AcPMAtmCellAttributesTxLowThreshold_Object((1,3,6,1,4,1,5003,10,12,1,31,2),_AcPMAtmCellAttributesTxLowThreshold_Type())
acPMAtmCellAttributesTxLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAtmCellAttributesTxLowThreshold.setStatus(_A)
class _AcPMAtmCellAttributesRxHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_AcPMAtmCellAttributesRxHighThreshold_Type.__name__=_B
_AcPMAtmCellAttributesRxHighThreshold_Object=MibScalar
acPMAtmCellAttributesRxHighThreshold=_AcPMAtmCellAttributesRxHighThreshold_Object((1,3,6,1,4,1,5003,10,12,1,31,3),_AcPMAtmCellAttributesRxHighThreshold_Type())
acPMAtmCellAttributesRxHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAtmCellAttributesRxHighThreshold.setStatus(_A)
class _AcPMAtmCellAttributesRxLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_AcPMAtmCellAttributesRxLowThreshold_Type.__name__=_B
_AcPMAtmCellAttributesRxLowThreshold_Object=MibScalar
acPMAtmCellAttributesRxLowThreshold=_AcPMAtmCellAttributesRxLowThreshold_Object((1,3,6,1,4,1,5003,10,12,1,31,4),_AcPMAtmCellAttributesRxLowThreshold_Type())
acPMAtmCellAttributesRxLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAtmCellAttributesRxLowThreshold.setStatus(_A)
_AcPMAtmData_ObjectIdentity=ObjectIdentity
acPMAtmData=_AcPMAtmData_ObjectIdentity((1,3,6,1,4,1,5003,10,12,2))
class _AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Type.__name__=_B
_AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Object=MibScalar
acPMAtmDataAcPMAtmTimeFromStartOfInterval=_AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Object((1,3,6,1,4,1,5003,10,12,2,1),_AcPMAtmDataAcPMAtmTimeFromStartOfInterval_Type())
acPMAtmDataAcPMAtmTimeFromStartOfInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmDataAcPMAtmTimeFromStartOfInterval.setStatus(_A)
_AcPMAtmCellTxTable_Object=MibTable
acPMAtmCellTxTable=_AcPMAtmCellTxTable_Object((1,3,6,1,4,1,5003,10,12,2,21))
if mibBuilder.loadTexts:acPMAtmCellTxTable.setStatus(_A)
_AcPMAtmCellTxEntry_Object=MibTableRow
acPMAtmCellTxEntry=_AcPMAtmCellTxEntry_Object((1,3,6,1,4,1,5003,10,12,2,21,1))
acPMAtmCellTxEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:acPMAtmCellTxEntry.setStatus(_A)
class _AcPMAtmCellTxInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMAtmCellTxInterface_Type.__name__=_B
_AcPMAtmCellTxInterface_Object=MibTableColumn
acPMAtmCellTxInterface=_AcPMAtmCellTxInterface_Object((1,3,6,1,4,1,5003,10,12,2,21,1,1),_AcPMAtmCellTxInterface_Type())
acPMAtmCellTxInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:acPMAtmCellTxInterface.setStatus(_A)
class _AcPMAtmCellTxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMAtmCellTxInterval_Type.__name__=_B
_AcPMAtmCellTxInterval_Object=MibTableColumn
acPMAtmCellTxInterval=_AcPMAtmCellTxInterval_Object((1,3,6,1,4,1,5003,10,12,2,21,1,2),_AcPMAtmCellTxInterval_Type())
acPMAtmCellTxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:acPMAtmCellTxInterval.setStatus(_A)
class _AcPMAtmCellTxAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellTxAverage_Type.__name__=_B
_AcPMAtmCellTxAverage_Object=MibTableColumn
acPMAtmCellTxAverage=_AcPMAtmCellTxAverage_Object((1,3,6,1,4,1,5003,10,12,2,21,1,3),_AcPMAtmCellTxAverage_Type())
acPMAtmCellTxAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxAverage.setStatus(_A)
class _AcPMAtmCellTxMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellTxMax_Type.__name__=_B
_AcPMAtmCellTxMax_Object=MibTableColumn
acPMAtmCellTxMax=_AcPMAtmCellTxMax_Object((1,3,6,1,4,1,5003,10,12,2,21,1,4),_AcPMAtmCellTxMax_Type())
acPMAtmCellTxMax.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxMax.setStatus(_A)
class _AcPMAtmCellTxMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellTxMin_Type.__name__=_B
_AcPMAtmCellTxMin_Object=MibTableColumn
acPMAtmCellTxMin=_AcPMAtmCellTxMin_Object((1,3,6,1,4,1,5003,10,12,2,21,1,5),_AcPMAtmCellTxMin_Type())
acPMAtmCellTxMin.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxMin.setStatus(_A)
_AcPMAtmCellTxVolume_Type=Counter32
_AcPMAtmCellTxVolume_Object=MibTableColumn
acPMAtmCellTxVolume=_AcPMAtmCellTxVolume_Object((1,3,6,1,4,1,5003,10,12,2,21,1,6),_AcPMAtmCellTxVolume_Type())
acPMAtmCellTxVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxVolume.setStatus(_A)
class _AcPMAtmCellTxTimeBelowLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMAtmCellTxTimeBelowLowThreshold_Type.__name__=_B
_AcPMAtmCellTxTimeBelowLowThreshold_Object=MibTableColumn
acPMAtmCellTxTimeBelowLowThreshold=_AcPMAtmCellTxTimeBelowLowThreshold_Object((1,3,6,1,4,1,5003,10,12,2,21,1,7),_AcPMAtmCellTxTimeBelowLowThreshold_Type())
acPMAtmCellTxTimeBelowLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxTimeBelowLowThreshold.setStatus(_A)
class _AcPMAtmCellTxTimeBetweenThresholds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMAtmCellTxTimeBetweenThresholds_Type.__name__=_B
_AcPMAtmCellTxTimeBetweenThresholds_Object=MibTableColumn
acPMAtmCellTxTimeBetweenThresholds=_AcPMAtmCellTxTimeBetweenThresholds_Object((1,3,6,1,4,1,5003,10,12,2,21,1,8),_AcPMAtmCellTxTimeBetweenThresholds_Type())
acPMAtmCellTxTimeBetweenThresholds.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxTimeBetweenThresholds.setStatus(_A)
class _AcPMAtmCellTxTimeAboveHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMAtmCellTxTimeAboveHighThreshold_Type.__name__=_B
_AcPMAtmCellTxTimeAboveHighThreshold_Object=MibTableColumn
acPMAtmCellTxTimeAboveHighThreshold=_AcPMAtmCellTxTimeAboveHighThreshold_Object((1,3,6,1,4,1,5003,10,12,2,21,1,9),_AcPMAtmCellTxTimeAboveHighThreshold_Type())
acPMAtmCellTxTimeAboveHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxTimeAboveHighThreshold.setStatus(_A)
class _AcPMAtmCellTxFullDayAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellTxFullDayAverage_Type.__name__=_B
_AcPMAtmCellTxFullDayAverage_Object=MibTableColumn
acPMAtmCellTxFullDayAverage=_AcPMAtmCellTxFullDayAverage_Object((1,3,6,1,4,1,5003,10,12,2,21,1,10),_AcPMAtmCellTxFullDayAverage_Type())
acPMAtmCellTxFullDayAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellTxFullDayAverage.setStatus(_A)
_AcPMAtmCellRxTable_Object=MibTable
acPMAtmCellRxTable=_AcPMAtmCellRxTable_Object((1,3,6,1,4,1,5003,10,12,2,22))
if mibBuilder.loadTexts:acPMAtmCellRxTable.setStatus(_A)
_AcPMAtmCellRxEntry_Object=MibTableRow
acPMAtmCellRxEntry=_AcPMAtmCellRxEntry_Object((1,3,6,1,4,1,5003,10,12,2,22,1))
acPMAtmCellRxEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:acPMAtmCellRxEntry.setStatus(_A)
class _AcPMAtmCellRxInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMAtmCellRxInterface_Type.__name__=_B
_AcPMAtmCellRxInterface_Object=MibTableColumn
acPMAtmCellRxInterface=_AcPMAtmCellRxInterface_Object((1,3,6,1,4,1,5003,10,12,2,22,1,1),_AcPMAtmCellRxInterface_Type())
acPMAtmCellRxInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:acPMAtmCellRxInterface.setStatus(_A)
class _AcPMAtmCellRxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMAtmCellRxInterval_Type.__name__=_B
_AcPMAtmCellRxInterval_Object=MibTableColumn
acPMAtmCellRxInterval=_AcPMAtmCellRxInterval_Object((1,3,6,1,4,1,5003,10,12,2,22,1,2),_AcPMAtmCellRxInterval_Type())
acPMAtmCellRxInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:acPMAtmCellRxInterval.setStatus(_A)
class _AcPMAtmCellRxAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellRxAverage_Type.__name__=_B
_AcPMAtmCellRxAverage_Object=MibTableColumn
acPMAtmCellRxAverage=_AcPMAtmCellRxAverage_Object((1,3,6,1,4,1,5003,10,12,2,22,1,3),_AcPMAtmCellRxAverage_Type())
acPMAtmCellRxAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxAverage.setStatus(_A)
class _AcPMAtmCellRxMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellRxMax_Type.__name__=_B
_AcPMAtmCellRxMax_Object=MibTableColumn
acPMAtmCellRxMax=_AcPMAtmCellRxMax_Object((1,3,6,1,4,1,5003,10,12,2,22,1,4),_AcPMAtmCellRxMax_Type())
acPMAtmCellRxMax.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxMax.setStatus(_A)
class _AcPMAtmCellRxMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellRxMin_Type.__name__=_B
_AcPMAtmCellRxMin_Object=MibTableColumn
acPMAtmCellRxMin=_AcPMAtmCellRxMin_Object((1,3,6,1,4,1,5003,10,12,2,22,1,5),_AcPMAtmCellRxMin_Type())
acPMAtmCellRxMin.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxMin.setStatus(_A)
_AcPMAtmCellRxVolume_Type=Counter32
_AcPMAtmCellRxVolume_Object=MibTableColumn
acPMAtmCellRxVolume=_AcPMAtmCellRxVolume_Object((1,3,6,1,4,1,5003,10,12,2,22,1,6),_AcPMAtmCellRxVolume_Type())
acPMAtmCellRxVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxVolume.setStatus(_A)
class _AcPMAtmCellRxTimeBelowLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMAtmCellRxTimeBelowLowThreshold_Type.__name__=_B
_AcPMAtmCellRxTimeBelowLowThreshold_Object=MibTableColumn
acPMAtmCellRxTimeBelowLowThreshold=_AcPMAtmCellRxTimeBelowLowThreshold_Object((1,3,6,1,4,1,5003,10,12,2,22,1,7),_AcPMAtmCellRxTimeBelowLowThreshold_Type())
acPMAtmCellRxTimeBelowLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxTimeBelowLowThreshold.setStatus(_A)
class _AcPMAtmCellRxTimeBetweenThresholds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMAtmCellRxTimeBetweenThresholds_Type.__name__=_B
_AcPMAtmCellRxTimeBetweenThresholds_Object=MibTableColumn
acPMAtmCellRxTimeBetweenThresholds=_AcPMAtmCellRxTimeBetweenThresholds_Object((1,3,6,1,4,1,5003,10,12,2,22,1,8),_AcPMAtmCellRxTimeBetweenThresholds_Type())
acPMAtmCellRxTimeBetweenThresholds.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxTimeBetweenThresholds.setStatus(_A)
class _AcPMAtmCellRxTimeAboveHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMAtmCellRxTimeAboveHighThreshold_Type.__name__=_B
_AcPMAtmCellRxTimeAboveHighThreshold_Object=MibTableColumn
acPMAtmCellRxTimeAboveHighThreshold=_AcPMAtmCellRxTimeAboveHighThreshold_Object((1,3,6,1,4,1,5003,10,12,2,22,1,9),_AcPMAtmCellRxTimeAboveHighThreshold_Type())
acPMAtmCellRxTimeAboveHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxTimeAboveHighThreshold.setStatus(_A)
class _AcPMAtmCellRxFullDayAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMAtmCellRxFullDayAverage_Type.__name__=_B
_AcPMAtmCellRxFullDayAverage_Object=MibTableColumn
acPMAtmCellRxFullDayAverage=_AcPMAtmCellRxFullDayAverage_Object((1,3,6,1,4,1,5003,10,12,2,22,1,10),_AcPMAtmCellRxFullDayAverage_Type())
acPMAtmCellRxFullDayAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellRxFullDayAverage.setStatus(_A)
_AcPMAtmCellDiscardedTable_Object=MibTable
acPMAtmCellDiscardedTable=_AcPMAtmCellDiscardedTable_Object((1,3,6,1,4,1,5003,10,12,2,23))
if mibBuilder.loadTexts:acPMAtmCellDiscardedTable.setStatus(_A)
_AcPMAtmCellDiscardedEntry_Object=MibTableRow
acPMAtmCellDiscardedEntry=_AcPMAtmCellDiscardedEntry_Object((1,3,6,1,4,1,5003,10,12,2,23,1))
acPMAtmCellDiscardedEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:acPMAtmCellDiscardedEntry.setStatus(_A)
class _AcPMAtmCellDiscardedInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMAtmCellDiscardedInterface_Type.__name__=_B
_AcPMAtmCellDiscardedInterface_Object=MibTableColumn
acPMAtmCellDiscardedInterface=_AcPMAtmCellDiscardedInterface_Object((1,3,6,1,4,1,5003,10,12,2,23,1,1),_AcPMAtmCellDiscardedInterface_Type())
acPMAtmCellDiscardedInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:acPMAtmCellDiscardedInterface.setStatus(_A)
class _AcPMAtmCellDiscardedInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMAtmCellDiscardedInterval_Type.__name__=_B
_AcPMAtmCellDiscardedInterval_Object=MibTableColumn
acPMAtmCellDiscardedInterval=_AcPMAtmCellDiscardedInterval_Object((1,3,6,1,4,1,5003,10,12,2,23,1,2),_AcPMAtmCellDiscardedInterval_Type())
acPMAtmCellDiscardedInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:acPMAtmCellDiscardedInterval.setStatus(_A)
_AcPMAtmCellDiscardedVal_Type=Gauge32
_AcPMAtmCellDiscardedVal_Object=MibTableColumn
acPMAtmCellDiscardedVal=_AcPMAtmCellDiscardedVal_Object((1,3,6,1,4,1,5003,10,12,2,23,1,3),_AcPMAtmCellDiscardedVal_Type())
acPMAtmCellDiscardedVal.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAtmCellDiscardedVal.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'audioCodes':audioCodes,'acRegistrations':acRegistrations,'acGeneric':acGeneric,'acProducts':acProducts,'acPerformance':acPerformance,'acPMAtm':acPMAtm,'acPMAtmConfiguration':acPMAtmConfiguration,'acPMAtmConfigurationPeriodLength':acPMAtmConfigurationPeriodLength,'acPMAtmConfigurationResetTotalCounters':acPMAtmConfigurationResetTotalCounters,'acPMAtmCellAttributes':acPMAtmCellAttributes,'acPMAtmCellAttributesTxHighThreshold':acPMAtmCellAttributesTxHighThreshold,'acPMAtmCellAttributesTxLowThreshold':acPMAtmCellAttributesTxLowThreshold,'acPMAtmCellAttributesRxHighThreshold':acPMAtmCellAttributesRxHighThreshold,'acPMAtmCellAttributesRxLowThreshold':acPMAtmCellAttributesRxLowThreshold,'acPMAtmData':acPMAtmData,'acPMAtmDataAcPMAtmTimeFromStartOfInterval':acPMAtmDataAcPMAtmTimeFromStartOfInterval,'acPMAtmCellTxTable':acPMAtmCellTxTable,'acPMAtmCellTxEntry':acPMAtmCellTxEntry,_G:acPMAtmCellTxInterface,_H:acPMAtmCellTxInterval,'acPMAtmCellTxAverage':acPMAtmCellTxAverage,'acPMAtmCellTxMax':acPMAtmCellTxMax,'acPMAtmCellTxMin':acPMAtmCellTxMin,'acPMAtmCellTxVolume':acPMAtmCellTxVolume,'acPMAtmCellTxTimeBelowLowThreshold':acPMAtmCellTxTimeBelowLowThreshold,'acPMAtmCellTxTimeBetweenThresholds':acPMAtmCellTxTimeBetweenThresholds,'acPMAtmCellTxTimeAboveHighThreshold':acPMAtmCellTxTimeAboveHighThreshold,'acPMAtmCellTxFullDayAverage':acPMAtmCellTxFullDayAverage,'acPMAtmCellRxTable':acPMAtmCellRxTable,'acPMAtmCellRxEntry':acPMAtmCellRxEntry,_I:acPMAtmCellRxInterface,_J:acPMAtmCellRxInterval,'acPMAtmCellRxAverage':acPMAtmCellRxAverage,'acPMAtmCellRxMax':acPMAtmCellRxMax,'acPMAtmCellRxMin':acPMAtmCellRxMin,'acPMAtmCellRxVolume':acPMAtmCellRxVolume,'acPMAtmCellRxTimeBelowLowThreshold':acPMAtmCellRxTimeBelowLowThreshold,'acPMAtmCellRxTimeBetweenThresholds':acPMAtmCellRxTimeBetweenThresholds,'acPMAtmCellRxTimeAboveHighThreshold':acPMAtmCellRxTimeAboveHighThreshold,'acPMAtmCellRxFullDayAverage':acPMAtmCellRxFullDayAverage,'acPMAtmCellDiscardedTable':acPMAtmCellDiscardedTable,'acPMAtmCellDiscardedEntry':acPMAtmCellDiscardedEntry,_K:acPMAtmCellDiscardedInterface,_L:acPMAtmCellDiscardedInterval,'acPMAtmCellDiscardedVal':acPMAtmCellDiscardedVal})