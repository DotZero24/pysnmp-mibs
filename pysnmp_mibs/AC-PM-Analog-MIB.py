_G='acPMOffHookChannelsInterval'
_F='AC-PM-Analog-MIB'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acBoardMibs,acGeneric,acPerformance,acProducts,acRegistrations,audioCodes=mibBuilder.importSymbols('AUDIOCODES-TYPES-MIB','acBoardMibs','acGeneric','acPerformance','acProducts','acRegistrations','audioCodes')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TAddress','TextualConvention')
acPMAnalog=ModuleIdentity((1,3,6,1,4,1,5003,10,9))
_AcPMAnalogConfiguration_ObjectIdentity=ObjectIdentity
acPMAnalogConfiguration=_AcPMAnalogConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,10,9,1))
class _AcPMAnalogConfigurationPeriodLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,894780))
_AcPMAnalogConfigurationPeriodLength_Type.__name__=_D
_AcPMAnalogConfigurationPeriodLength_Object=MibScalar
acPMAnalogConfigurationPeriodLength=_AcPMAnalogConfigurationPeriodLength_Object((1,3,6,1,4,1,5003,10,9,1,1),_AcPMAnalogConfigurationPeriodLength_Type())
acPMAnalogConfigurationPeriodLength.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAnalogConfigurationPeriodLength.setStatus(_A)
class _AcPMAnalogConfigurationResetTotalCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('resetCountersDone',1),('resetTotalCounters',2)))
_AcPMAnalogConfigurationResetTotalCounters_Type.__name__=_B
_AcPMAnalogConfigurationResetTotalCounters_Object=MibScalar
acPMAnalogConfigurationResetTotalCounters=_AcPMAnalogConfigurationResetTotalCounters_Object((1,3,6,1,4,1,5003,10,9,1,2),_AcPMAnalogConfigurationResetTotalCounters_Type())
acPMAnalogConfigurationResetTotalCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAnalogConfigurationResetTotalCounters.setStatus(_A)
_AcPMAnalogUtilsAttributes_ObjectIdentity=ObjectIdentity
acPMAnalogUtilsAttributes=_AcPMAnalogUtilsAttributes_ObjectIdentity((1,3,6,1,4,1,5003,10,9,1,31))
class _AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Type.__name__=_D
_AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Object=MibScalar
acPMAnalogUtilsAttributesOffHookChannelsHighThreshold=_AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Object((1,3,6,1,4,1,5003,10,9,1,31,1),_AcPMAnalogUtilsAttributesOffHookChannelsHighThreshold_Type())
acPMAnalogUtilsAttributesOffHookChannelsHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAnalogUtilsAttributesOffHookChannelsHighThreshold.setStatus(_A)
class _AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Type.__name__=_D
_AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Object=MibScalar
acPMAnalogUtilsAttributesOffHookChannelsLowThreshold=_AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Object((1,3,6,1,4,1,5003,10,9,1,31,2),_AcPMAnalogUtilsAttributesOffHookChannelsLowThreshold_Type())
acPMAnalogUtilsAttributesOffHookChannelsLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acPMAnalogUtilsAttributesOffHookChannelsLowThreshold.setStatus(_A)
_AcPMAnalogData_ObjectIdentity=ObjectIdentity
acPMAnalogData=_AcPMAnalogData_ObjectIdentity((1,3,6,1,4,1,5003,10,9,2))
class _AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Type.__name__=_D
_AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Object=MibScalar
acPMAnalogDataAcPMAnalogTimeFromStartOfInterval=_AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Object((1,3,6,1,4,1,5003,10,9,2,1),_AcPMAnalogDataAcPMAnalogTimeFromStartOfInterval_Type())
acPMAnalogDataAcPMAnalogTimeFromStartOfInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMAnalogDataAcPMAnalogTimeFromStartOfInterval.setStatus(_A)
_AcPMAnalogUtils_ObjectIdentity=ObjectIdentity
acPMAnalogUtils=_AcPMAnalogUtils_ObjectIdentity((1,3,6,1,4,1,5003,10,9,2,31))
_AcPMOffHookChannelsTable_Object=MibTable
acPMOffHookChannelsTable=_AcPMOffHookChannelsTable_Object((1,3,6,1,4,1,5003,10,9,2,31,21))
if mibBuilder.loadTexts:acPMOffHookChannelsTable.setStatus(_A)
_AcPMOffHookChannelsEntry_Object=MibTableRow
acPMOffHookChannelsEntry=_AcPMOffHookChannelsEntry_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1))
acPMOffHookChannelsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:acPMOffHookChannelsEntry.setStatus(_A)
class _AcPMOffHookChannelsInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcPMOffHookChannelsInterval_Type.__name__=_D
_AcPMOffHookChannelsInterval_Object=MibTableColumn
acPMOffHookChannelsInterval=_AcPMOffHookChannelsInterval_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,1),_AcPMOffHookChannelsInterval_Type())
acPMOffHookChannelsInterval.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:acPMOffHookChannelsInterval.setStatus(_A)
_AcPMOffHookChannelsVal_Type=Gauge32
_AcPMOffHookChannelsVal_Object=MibTableColumn
acPMOffHookChannelsVal=_AcPMOffHookChannelsVal_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,2),_AcPMOffHookChannelsVal_Type())
acPMOffHookChannelsVal.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsVal.setStatus(_A)
class _AcPMOffHookChannelsAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMOffHookChannelsAverage_Type.__name__=_B
_AcPMOffHookChannelsAverage_Object=MibTableColumn
acPMOffHookChannelsAverage=_AcPMOffHookChannelsAverage_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,3),_AcPMOffHookChannelsAverage_Type())
acPMOffHookChannelsAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsAverage.setStatus(_A)
class _AcPMOffHookChannelsMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMOffHookChannelsMax_Type.__name__=_B
_AcPMOffHookChannelsMax_Object=MibTableColumn
acPMOffHookChannelsMax=_AcPMOffHookChannelsMax_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,4),_AcPMOffHookChannelsMax_Type())
acPMOffHookChannelsMax.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsMax.setStatus(_A)
class _AcPMOffHookChannelsMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMOffHookChannelsMin_Type.__name__=_B
_AcPMOffHookChannelsMin_Object=MibTableColumn
acPMOffHookChannelsMin=_AcPMOffHookChannelsMin_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,5),_AcPMOffHookChannelsMin_Type())
acPMOffHookChannelsMin.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsMin.setStatus(_A)
class _AcPMOffHookChannelsVolume_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMOffHookChannelsVolume_Type.__name__=_B
_AcPMOffHookChannelsVolume_Object=MibTableColumn
acPMOffHookChannelsVolume=_AcPMOffHookChannelsVolume_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,6),_AcPMOffHookChannelsVolume_Type())
acPMOffHookChannelsVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsVolume.setStatus(_A)
class _AcPMOffHookChannelsTimeBelowLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMOffHookChannelsTimeBelowLowThreshold_Type.__name__=_B
_AcPMOffHookChannelsTimeBelowLowThreshold_Object=MibTableColumn
acPMOffHookChannelsTimeBelowLowThreshold=_AcPMOffHookChannelsTimeBelowLowThreshold_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,7),_AcPMOffHookChannelsTimeBelowLowThreshold_Type())
acPMOffHookChannelsTimeBelowLowThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsTimeBelowLowThreshold.setStatus(_A)
class _AcPMOffHookChannelsTimeBetweenThresholds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMOffHookChannelsTimeBetweenThresholds_Type.__name__=_B
_AcPMOffHookChannelsTimeBetweenThresholds_Object=MibTableColumn
acPMOffHookChannelsTimeBetweenThresholds=_AcPMOffHookChannelsTimeBetweenThresholds_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,8),_AcPMOffHookChannelsTimeBetweenThresholds_Type())
acPMOffHookChannelsTimeBetweenThresholds.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsTimeBetweenThresholds.setStatus(_A)
class _AcPMOffHookChannelsTimeAboveHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_AcPMOffHookChannelsTimeAboveHighThreshold_Type.__name__=_B
_AcPMOffHookChannelsTimeAboveHighThreshold_Object=MibTableColumn
acPMOffHookChannelsTimeAboveHighThreshold=_AcPMOffHookChannelsTimeAboveHighThreshold_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,9),_AcPMOffHookChannelsTimeAboveHighThreshold_Type())
acPMOffHookChannelsTimeAboveHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsTimeAboveHighThreshold.setStatus(_A)
class _AcPMOffHookChannelsFullDayAverage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcPMOffHookChannelsFullDayAverage_Type.__name__=_B
_AcPMOffHookChannelsFullDayAverage_Object=MibTableColumn
acPMOffHookChannelsFullDayAverage=_AcPMOffHookChannelsFullDayAverage_Object((1,3,6,1,4,1,5003,10,9,2,31,21,1,10),_AcPMOffHookChannelsFullDayAverage_Type())
acPMOffHookChannelsFullDayAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:acPMOffHookChannelsFullDayAverage.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'acPMAnalog':acPMAnalog,'acPMAnalogConfiguration':acPMAnalogConfiguration,'acPMAnalogConfigurationPeriodLength':acPMAnalogConfigurationPeriodLength,'acPMAnalogConfigurationResetTotalCounters':acPMAnalogConfigurationResetTotalCounters,'acPMAnalogUtilsAttributes':acPMAnalogUtilsAttributes,'acPMAnalogUtilsAttributesOffHookChannelsHighThreshold':acPMAnalogUtilsAttributesOffHookChannelsHighThreshold,'acPMAnalogUtilsAttributesOffHookChannelsLowThreshold':acPMAnalogUtilsAttributesOffHookChannelsLowThreshold,'acPMAnalogData':acPMAnalogData,'acPMAnalogDataAcPMAnalogTimeFromStartOfInterval':acPMAnalogDataAcPMAnalogTimeFromStartOfInterval,'acPMAnalogUtils':acPMAnalogUtils,'acPMOffHookChannelsTable':acPMOffHookChannelsTable,'acPMOffHookChannelsEntry':acPMOffHookChannelsEntry,_G:acPMOffHookChannelsInterval,'acPMOffHookChannelsVal':acPMOffHookChannelsVal,'acPMOffHookChannelsAverage':acPMOffHookChannelsAverage,'acPMOffHookChannelsMax':acPMOffHookChannelsMax,'acPMOffHookChannelsMin':acPMOffHookChannelsMin,'acPMOffHookChannelsVolume':acPMOffHookChannelsVolume,'acPMOffHookChannelsTimeBelowLowThreshold':acPMOffHookChannelsTimeBelowLowThreshold,'acPMOffHookChannelsTimeBetweenThresholds':acPMOffHookChannelsTimeBetweenThresholds,'acPMOffHookChannelsTimeAboveHighThreshold':acPMOffHookChannelsTimeAboveHighThreshold,'acPMOffHookChannelsFullDayAverage':acPMOffHookChannelsFullDayAverage})