_t='zxAnOtdrEnvApdTempLowThresh'
_s='zxAnOtdrRoutineTaskResultFile'
_r='zxAnOtdrRoutineTaskFailedReason'
_q='zxAnOtdrRoutineTaskOperStatus'
_p='zxAnOtdrRoutineTaskCurrStartTime'
_o='zxAnOtdrFtpServerId'
_n='zxAnOtdrFileFtpUploadFileName'
_m='stopped'
_l='zxAnOtdrIfPort'
_k='zxAnOtdrIfSlot'
_j='zxAnOtdrIfShelf'
_i='zxAnOtdrIfRack'
_h='zxAnOtdrTestParamPrfName'
_g='zxAnOtdrEnvApdTempHighThresh'
_f='zxAnOtdrEnvFanOperStatus'
_e='zxAnOtdrEnvFanStatus'
_d='zxAnOtdrCtrlCardTempLowThresh'
_c='zxAnOtdrCtrlCardTempHighThresh'
_b='zxAnOtdrRoutineTaskIfPort'
_a='zxAnOtdrRoutineTaskIfSlot'
_Z='zxAnOtdrRoutineTaskIfShelf'
_Y='zxAnOtdrRoutineTaskIfRack'
_X='zxAnOtdrRoutineTaskName'
_W='zxAnOtdrFastTestIfPort'
_V='zxAnOtdrFastTestIfSlot'
_U='zxAnOtdrFastTestIfShelf'
_T='zxAnOtdrFastTestIfRack'
_S='zxAnOtdrFastTestIfSn'
_R='InetAddressType'
_Q='otherErrors'
_P='noError'
_O='failed'
_N='success'
_M='inProgress'
_L='notStarted'
_K='zxAnOtdrEnvApdCurrentTemp'
_J='zxAnOtdrCtrlCardCurrentTemp'
_I='Centigrade'
_H='read-write'
_G='not-accessible'
_F='read-only'
_E='DisplayString'
_D='read-create'
_C='Integer32'
_B='ZTE-AN-OTDR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','RowStatus','TextualConvention')
zxAnOfd,=mibBuilder.importSymbols('ZTE-AN-OFD-SMI','zxAnOfd')
zxAnOtdrMib=ModuleIdentity((1,3,6,1,4,1,3902,1083,5))
if mibBuilder.loadTexts:zxAnOtdrMib.setRevisions(('2013-03-05 12:00',))
_ZxAnOtdrGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrGlobalObjects=_ZxAnOtdrGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,1))
_ZxAnOtdrCapacityGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrCapacityGlobalObjects=_ZxAnOtdrCapacityGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,1,1))
class _ZxAnOtdrWaveLengthList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnOtdrWaveLengthList_Type.__name__=_E
_ZxAnOtdrWaveLengthList_Object=MibScalar
zxAnOtdrWaveLengthList=_ZxAnOtdrWaveLengthList_Object((1,3,6,1,4,1,3902,1083,5,1,1,1),_ZxAnOtdrWaveLengthList_Type())
zxAnOtdrWaveLengthList.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrWaveLengthList.setStatus(_A)
class _ZxAnOtdrTestPulseWidthList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxAnOtdrTestPulseWidthList_Type.__name__=_E
_ZxAnOtdrTestPulseWidthList_Object=MibScalar
zxAnOtdrTestPulseWidthList=_ZxAnOtdrTestPulseWidthList_Object((1,3,6,1,4,1,3902,1083,5,1,1,2),_ZxAnOtdrTestPulseWidthList_Type())
zxAnOtdrTestPulseWidthList.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrTestPulseWidthList.setStatus(_A)
class _ZxAnOtdrTotalPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_ZxAnOtdrTotalPorts_Type.__name__=_C
_ZxAnOtdrTotalPorts_Object=MibScalar
zxAnOtdrTotalPorts=_ZxAnOtdrTotalPorts_Object((1,3,6,1,4,1,3902,1083,5,1,1,3),_ZxAnOtdrTotalPorts_Type())
zxAnOtdrTotalPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrTotalPorts.setStatus(_A)
_ZxAnOtdrEnvGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrEnvGlobalObjects=_ZxAnOtdrEnvGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,1,2))
_ZxAnOtdrEnvCtrlCardGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrEnvCtrlCardGlobalObjects=_ZxAnOtdrEnvCtrlCardGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,1,2,1))
_ZxAnOtdrCtrlCardCurrentTemp_Type=Integer32
_ZxAnOtdrCtrlCardCurrentTemp_Object=MibScalar
zxAnOtdrCtrlCardCurrentTemp=_ZxAnOtdrCtrlCardCurrentTemp_Object((1,3,6,1,4,1,3902,1083,5,1,2,1,1),_ZxAnOtdrCtrlCardCurrentTemp_Type())
zxAnOtdrCtrlCardCurrentTemp.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrCtrlCardCurrentTemp.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrCtrlCardCurrentTemp.setUnits(_I)
class _ZxAnOtdrCtrlCardTempHighThresh_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,95))
_ZxAnOtdrCtrlCardTempHighThresh_Type.__name__=_C
_ZxAnOtdrCtrlCardTempHighThresh_Object=MibScalar
zxAnOtdrCtrlCardTempHighThresh=_ZxAnOtdrCtrlCardTempHighThresh_Object((1,3,6,1,4,1,3902,1083,5,1,2,1,2),_ZxAnOtdrCtrlCardTempHighThresh_Type())
zxAnOtdrCtrlCardTempHighThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrCtrlCardTempHighThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrCtrlCardTempHighThresh.setUnits(_I)
class _ZxAnOtdrCtrlCardTempLowThresh_Type(Integer32):defaultValue=-45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-45,-25))
_ZxAnOtdrCtrlCardTempLowThresh_Type.__name__=_C
_ZxAnOtdrCtrlCardTempLowThresh_Object=MibScalar
zxAnOtdrCtrlCardTempLowThresh=_ZxAnOtdrCtrlCardTempLowThresh_Object((1,3,6,1,4,1,3902,1083,5,1,2,1,3),_ZxAnOtdrCtrlCardTempLowThresh_Type())
zxAnOtdrCtrlCardTempLowThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrCtrlCardTempLowThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrCtrlCardTempLowThresh.setUnits(_I)
_ZxAnOtdrEnvFanGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrEnvFanGlobalObjects=_ZxAnOtdrEnvFanGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,1,2,2))
class _ZxAnOtdrEnvFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('abnormal',2)))
_ZxAnOtdrEnvFanStatus_Type.__name__=_C
_ZxAnOtdrEnvFanStatus_Object=MibScalar
zxAnOtdrEnvFanStatus=_ZxAnOtdrEnvFanStatus_Object((1,3,6,1,4,1,3902,1083,5,1,2,2,1),_ZxAnOtdrEnvFanStatus_Type())
zxAnOtdrEnvFanStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrEnvFanStatus.setStatus(_A)
class _ZxAnOtdrEnvFanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ZxAnOtdrEnvFanOperStatus_Type.__name__=_C
_ZxAnOtdrEnvFanOperStatus_Object=MibScalar
zxAnOtdrEnvFanOperStatus=_ZxAnOtdrEnvFanOperStatus_Object((1,3,6,1,4,1,3902,1083,5,1,2,2,2),_ZxAnOtdrEnvFanOperStatus_Type())
zxAnOtdrEnvFanOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrEnvFanOperStatus.setStatus(_A)
_ZxAnOtdrEnvApdGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrEnvApdGlobalObjects=_ZxAnOtdrEnvApdGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,1,2,3))
_ZxAnOtdrEnvApdCurrentTemp_Type=Integer32
_ZxAnOtdrEnvApdCurrentTemp_Object=MibScalar
zxAnOtdrEnvApdCurrentTemp=_ZxAnOtdrEnvApdCurrentTemp_Object((1,3,6,1,4,1,3902,1083,5,1,2,3,1),_ZxAnOtdrEnvApdCurrentTemp_Type())
zxAnOtdrEnvApdCurrentTemp.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrEnvApdCurrentTemp.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrEnvApdCurrentTemp.setUnits(_I)
class _ZxAnOtdrEnvApdTempHighThresh_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,100))
_ZxAnOtdrEnvApdTempHighThresh_Type.__name__=_C
_ZxAnOtdrEnvApdTempHighThresh_Object=MibScalar
zxAnOtdrEnvApdTempHighThresh=_ZxAnOtdrEnvApdTempHighThresh_Object((1,3,6,1,4,1,3902,1083,5,1,2,3,2),_ZxAnOtdrEnvApdTempHighThresh_Type())
zxAnOtdrEnvApdTempHighThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrEnvApdTempHighThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrEnvApdTempHighThresh.setUnits(_I)
class _ZxAnOtdrEnvApdTempLowThresh_Type(Integer32):defaultValue=-20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-55,-20))
_ZxAnOtdrEnvApdTempLowThresh_Type.__name__=_C
_ZxAnOtdrEnvApdTempLowThresh_Object=MibScalar
zxAnOtdrEnvApdTempLowThresh=_ZxAnOtdrEnvApdTempLowThresh_Object((1,3,6,1,4,1,3902,1083,5,1,2,3,3),_ZxAnOtdrEnvApdTempLowThresh_Type())
zxAnOtdrEnvApdTempLowThresh.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrEnvApdTempLowThresh.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrEnvApdTempLowThresh.setUnits(_I)
_ZxAnOtdrObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrObjects=_ZxAnOtdrObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2))
_ZxAnOtdrIfObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrIfObjects=_ZxAnOtdrIfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,1))
_ZxAnOtdrTestParamPrfTable_Object=MibTable
zxAnOtdrTestParamPrfTable=_ZxAnOtdrTestParamPrfTable_Object((1,3,6,1,4,1,3902,1083,5,2,1,2))
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfTable.setStatus(_A)
_ZxAnOtdrTestParamPrfEntry_Object=MibTableRow
zxAnOtdrTestParamPrfEntry=_ZxAnOtdrTestParamPrfEntry_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1))
zxAnOtdrTestParamPrfEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfEntry.setStatus(_A)
class _ZxAnOtdrTestParamPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrTestParamPrfName_Type.__name__=_E
_ZxAnOtdrTestParamPrfName_Object=MibTableColumn
zxAnOtdrTestParamPrfName=_ZxAnOtdrTestParamPrfName_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,1),_ZxAnOtdrTestParamPrfName_Type())
zxAnOtdrTestParamPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfName.setStatus(_A)
class _ZxAnOtdrTestParamPrfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pulseMethod',1),('periodicSequenceMethod',2),('nonperiodicSequenceMethod',3)))
_ZxAnOtdrTestParamPrfMode_Type.__name__=_C
_ZxAnOtdrTestParamPrfMode_Object=MibTableColumn
zxAnOtdrTestParamPrfMode=_ZxAnOtdrTestParamPrfMode_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,2),_ZxAnOtdrTestParamPrfMode_Type())
zxAnOtdrTestParamPrfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfMode.setStatus(_A)
class _ZxAnOtdrTestParamPrfWaveLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1625,1650))
_ZxAnOtdrTestParamPrfWaveLength_Type.__name__=_C
_ZxAnOtdrTestParamPrfWaveLength_Object=MibTableColumn
zxAnOtdrTestParamPrfWaveLength=_ZxAnOtdrTestParamPrfWaveLength_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,3),_ZxAnOtdrTestParamPrfWaveLength_Type())
zxAnOtdrTestParamPrfWaveLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfWaveLength.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfWaveLength.setUnits('nm')
class _ZxAnOtdrTestParamPrfDistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_ZxAnOtdrTestParamPrfDistance_Type.__name__=_C
_ZxAnOtdrTestParamPrfDistance_Object=MibTableColumn
zxAnOtdrTestParamPrfDistance=_ZxAnOtdrTestParamPrfDistance_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,4),_ZxAnOtdrTestParamPrfDistance_Type())
zxAnOtdrTestParamPrfDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfDistance.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfDistance.setUnits('meter')
class _ZxAnOtdrTestParamPrfFiberIor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1400000,1500000))
_ZxAnOtdrTestParamPrfFiberIor_Type.__name__=_C
_ZxAnOtdrTestParamPrfFiberIor_Object=MibTableColumn
zxAnOtdrTestParamPrfFiberIor=_ZxAnOtdrTestParamPrfFiberIor_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,5),_ZxAnOtdrTestParamPrfFiberIor_Type())
zxAnOtdrTestParamPrfFiberIor.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfFiberIor.setStatus(_A)
class _ZxAnOtdrTestParamPrfPulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,20000))
_ZxAnOtdrTestParamPrfPulseWidth_Type.__name__=_C
_ZxAnOtdrTestParamPrfPulseWidth_Object=MibTableColumn
zxAnOtdrTestParamPrfPulseWidth=_ZxAnOtdrTestParamPrfPulseWidth_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,6),_ZxAnOtdrTestParamPrfPulseWidth_Type())
zxAnOtdrTestParamPrfPulseWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfPulseWidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfPulseWidth.setUnits('ns')
class _ZxAnOtdrTestParamPrfDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,3600))
_ZxAnOtdrTestParamPrfDuration_Type.__name__=_C
_ZxAnOtdrTestParamPrfDuration_Object=MibTableColumn
zxAnOtdrTestParamPrfDuration=_ZxAnOtdrTestParamPrfDuration_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,7),_ZxAnOtdrTestParamPrfDuration_Type())
zxAnOtdrTestParamPrfDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfDuration.setUnits('seconds')
class _ZxAnOtdrTestParamPrfSeqCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('complementaryCode',1),('pseudoRandomCode',2),('notConfigured',255)))
_ZxAnOtdrTestParamPrfSeqCode_Type.__name__=_C
_ZxAnOtdrTestParamPrfSeqCode_Object=MibTableColumn
zxAnOtdrTestParamPrfSeqCode=_ZxAnOtdrTestParamPrfSeqCode_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,8),_ZxAnOtdrTestParamPrfSeqCode_Type())
zxAnOtdrTestParamPrfSeqCode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfSeqCode.setStatus(_A)
class _ZxAnOtdrTestParamPrfSeqCodeLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,32000))
_ZxAnOtdrTestParamPrfSeqCodeLen_Type.__name__=_C
_ZxAnOtdrTestParamPrfSeqCodeLen_Object=MibTableColumn
zxAnOtdrTestParamPrfSeqCodeLen=_ZxAnOtdrTestParamPrfSeqCodeLen_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,9),_ZxAnOtdrTestParamPrfSeqCodeLen_Type())
zxAnOtdrTestParamPrfSeqCodeLen.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfSeqCodeLen.setStatus(_A)
class _ZxAnOtdrTestParamPrfCodeWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(50,60))
_ZxAnOtdrTestParamPrfCodeWidth_Type.__name__=_C
_ZxAnOtdrTestParamPrfCodeWidth_Object=MibTableColumn
zxAnOtdrTestParamPrfCodeWidth=_ZxAnOtdrTestParamPrfCodeWidth_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,10),_ZxAnOtdrTestParamPrfCodeWidth_Type())
zxAnOtdrTestParamPrfCodeWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfCodeWidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfCodeWidth.setUnits('ns')
class _ZxAnOtdrTestParamPrfTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,100))
_ZxAnOtdrTestParamPrfTimes_Type.__name__=_C
_ZxAnOtdrTestParamPrfTimes_Object=MibTableColumn
zxAnOtdrTestParamPrfTimes=_ZxAnOtdrTestParamPrfTimes_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,11),_ZxAnOtdrTestParamPrfTimes_Type())
zxAnOtdrTestParamPrfTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfTimes.setStatus(_A)
class _ZxAnOtdrTestParamPrfInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,100))
_ZxAnOtdrTestParamPrfInterval_Type.__name__=_C
_ZxAnOtdrTestParamPrfInterval_Object=MibTableColumn
zxAnOtdrTestParamPrfInterval=_ZxAnOtdrTestParamPrfInterval_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,12),_ZxAnOtdrTestParamPrfInterval_Type())
zxAnOtdrTestParamPrfInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfInterval.setUnits('us')
_ZxAnOtdrTestParamPrfRowStatus_Type=RowStatus
_ZxAnOtdrTestParamPrfRowStatus_Object=MibTableColumn
zxAnOtdrTestParamPrfRowStatus=_ZxAnOtdrTestParamPrfRowStatus_Object((1,3,6,1,4,1,3902,1083,5,2,1,2,1,50),_ZxAnOtdrTestParamPrfRowStatus_Type())
zxAnOtdrTestParamPrfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrTestParamPrfRowStatus.setStatus(_A)
_ZxAnOtdrIfTable_Object=MibTable
zxAnOtdrIfTable=_ZxAnOtdrIfTable_Object((1,3,6,1,4,1,3902,1083,5,2,1,3))
if mibBuilder.loadTexts:zxAnOtdrIfTable.setStatus(_A)
_ZxAnOtdrIfEntry_Object=MibTableRow
zxAnOtdrIfEntry=_ZxAnOtdrIfEntry_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1))
zxAnOtdrIfEntry.setIndexNames((0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:zxAnOtdrIfEntry.setStatus(_A)
_ZxAnOtdrIfRack_Type=Integer32
_ZxAnOtdrIfRack_Object=MibTableColumn
zxAnOtdrIfRack=_ZxAnOtdrIfRack_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,1),_ZxAnOtdrIfRack_Type())
zxAnOtdrIfRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrIfRack.setStatus(_A)
_ZxAnOtdrIfShelf_Type=Integer32
_ZxAnOtdrIfShelf_Object=MibTableColumn
zxAnOtdrIfShelf=_ZxAnOtdrIfShelf_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,2),_ZxAnOtdrIfShelf_Type())
zxAnOtdrIfShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrIfShelf.setStatus(_A)
_ZxAnOtdrIfSlot_Type=Integer32
_ZxAnOtdrIfSlot_Object=MibTableColumn
zxAnOtdrIfSlot=_ZxAnOtdrIfSlot_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,3),_ZxAnOtdrIfSlot_Type())
zxAnOtdrIfSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrIfSlot.setStatus(_A)
_ZxAnOtdrIfPort_Type=Integer32
_ZxAnOtdrIfPort_Object=MibTableColumn
zxAnOtdrIfPort=_ZxAnOtdrIfPort_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,4),_ZxAnOtdrIfPort_Type())
zxAnOtdrIfPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrIfPort.setStatus(_A)
class _ZxAnOtdrIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnOtdrIfAlias_Type.__name__=_E
_ZxAnOtdrIfAlias_Object=MibTableColumn
zxAnOtdrIfAlias=_ZxAnOtdrIfAlias_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,5),_ZxAnOtdrIfAlias_Type())
zxAnOtdrIfAlias.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrIfAlias.setStatus(_A)
class _ZxAnOtdrIfFastTestParamPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnOtdrIfFastTestParamPrf_Type.__name__=_E
_ZxAnOtdrIfFastTestParamPrf_Object=MibTableColumn
zxAnOtdrIfFastTestParamPrf=_ZxAnOtdrIfFastTestParamPrf_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,6),_ZxAnOtdrIfFastTestParamPrf_Type())
zxAnOtdrIfFastTestParamPrf.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrIfFastTestParamPrf.setStatus(_A)
class _ZxAnOtdrIfRoutineTestParamPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnOtdrIfRoutineTestParamPrf_Type.__name__=_E
_ZxAnOtdrIfRoutineTestParamPrf_Object=MibTableColumn
zxAnOtdrIfRoutineTestParamPrf=_ZxAnOtdrIfRoutineTestParamPrf_Object((1,3,6,1,4,1,3902,1083,5,2,1,3,1,7),_ZxAnOtdrIfRoutineTestParamPrf_Type())
zxAnOtdrIfRoutineTestParamPrf.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrIfRoutineTestParamPrf.setStatus(_A)
_ZxAnOtdrFastTestObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFastTestObjects=_ZxAnOtdrFastTestObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2))
_ZxAnOtdrFastTestConfObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFastTestConfObjects=_ZxAnOtdrFastTestConfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2,1))
_ZxAnOtdrFastTestActionObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFastTestActionObjects=_ZxAnOtdrFastTestActionObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2,1,1))
class _ZxAnOtdrFastTestSn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ZxAnOtdrFastTestSn_Type.__name__=_E
_ZxAnOtdrFastTestSn_Object=MibScalar
zxAnOtdrFastTestSn=_ZxAnOtdrFastTestSn_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,1,1),_ZxAnOtdrFastTestSn_Type())
zxAnOtdrFastTestSn.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFastTestSn.setStatus(_A)
class _ZxAnOtdrFastTestAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxAnOtdrFastTestAction_Type.__name__=_C
_ZxAnOtdrFastTestAction_Object=MibScalar
zxAnOtdrFastTestAction=_ZxAnOtdrFastTestAction_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,1,2),_ZxAnOtdrFastTestAction_Type())
zxAnOtdrFastTestAction.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFastTestAction.setStatus(_A)
_ZxAnOtdrFastTestIfTable_Object=MibTable
zxAnOtdrFastTestIfTable=_ZxAnOtdrFastTestIfTable_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2))
if mibBuilder.loadTexts:zxAnOtdrFastTestIfTable.setStatus(_A)
_ZxAnOtdrFastTestIfEntry_Object=MibTableRow
zxAnOtdrFastTestIfEntry=_ZxAnOtdrFastTestIfEntry_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1))
zxAnOtdrFastTestIfEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:zxAnOtdrFastTestIfEntry.setStatus(_A)
class _ZxAnOtdrFastTestIfSn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ZxAnOtdrFastTestIfSn_Type.__name__=_E
_ZxAnOtdrFastTestIfSn_Object=MibTableColumn
zxAnOtdrFastTestIfSn=_ZxAnOtdrFastTestIfSn_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1,1),_ZxAnOtdrFastTestIfSn_Type())
zxAnOtdrFastTestIfSn.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfSn.setStatus(_A)
_ZxAnOtdrFastTestIfRack_Type=Integer32
_ZxAnOtdrFastTestIfRack_Object=MibTableColumn
zxAnOtdrFastTestIfRack=_ZxAnOtdrFastTestIfRack_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1,2),_ZxAnOtdrFastTestIfRack_Type())
zxAnOtdrFastTestIfRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfRack.setStatus(_A)
_ZxAnOtdrFastTestIfShelf_Type=Integer32
_ZxAnOtdrFastTestIfShelf_Object=MibTableColumn
zxAnOtdrFastTestIfShelf=_ZxAnOtdrFastTestIfShelf_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1,3),_ZxAnOtdrFastTestIfShelf_Type())
zxAnOtdrFastTestIfShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfShelf.setStatus(_A)
_ZxAnOtdrFastTestIfSlot_Type=Integer32
_ZxAnOtdrFastTestIfSlot_Object=MibTableColumn
zxAnOtdrFastTestIfSlot=_ZxAnOtdrFastTestIfSlot_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1,4),_ZxAnOtdrFastTestIfSlot_Type())
zxAnOtdrFastTestIfSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfSlot.setStatus(_A)
_ZxAnOtdrFastTestIfPort_Type=Integer32
_ZxAnOtdrFastTestIfPort_Object=MibTableColumn
zxAnOtdrFastTestIfPort=_ZxAnOtdrFastTestIfPort_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1,5),_ZxAnOtdrFastTestIfPort_Type())
zxAnOtdrFastTestIfPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfPort.setStatus(_A)
_ZxAnOtdrFastTestIfRowStatus_Type=RowStatus
_ZxAnOtdrFastTestIfRowStatus_Object=MibTableColumn
zxAnOtdrFastTestIfRowStatus=_ZxAnOtdrFastTestIfRowStatus_Object((1,3,6,1,4,1,3902,1083,5,2,2,1,2,1,50),_ZxAnOtdrFastTestIfRowStatus_Type())
zxAnOtdrFastTestIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfRowStatus.setStatus(_A)
_ZxAnOtdrFastTestStatusObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFastTestStatusObjects=_ZxAnOtdrFastTestStatusObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2,2))
_ZxAnOtdrFastTestStatusGlbObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFastTestStatusGlbObjects=_ZxAnOtdrFastTestStatusGlbObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2,2,1))
class _ZxAnOtdrFastTestCurrentPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnOtdrFastTestCurrentPort_Type.__name__=_E
_ZxAnOtdrFastTestCurrentPort_Object=MibScalar
zxAnOtdrFastTestCurrentPort=_ZxAnOtdrFastTestCurrentPort_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,1,1),_ZxAnOtdrFastTestCurrentPort_Type())
zxAnOtdrFastTestCurrentPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFastTestCurrentPort.setStatus(_A)
class _ZxAnOtdrFastTestWaitTestPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnOtdrFastTestWaitTestPorts_Type.__name__=_C
_ZxAnOtdrFastTestWaitTestPorts_Object=MibScalar
zxAnOtdrFastTestWaitTestPorts=_ZxAnOtdrFastTestWaitTestPorts_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,1,2),_ZxAnOtdrFastTestWaitTestPorts_Type())
zxAnOtdrFastTestWaitTestPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFastTestWaitTestPorts.setStatus(_A)
_ZxAnOtdrFastTestIfStatusTable_Object=MibTable
zxAnOtdrFastTestIfStatusTable=_ZxAnOtdrFastTestIfStatusTable_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,2))
if mibBuilder.loadTexts:zxAnOtdrFastTestIfStatusTable.setStatus(_A)
_ZxAnOtdrFastTestIfStatusEntry_Object=MibTableRow
zxAnOtdrFastTestIfStatusEntry=_ZxAnOtdrFastTestIfStatusEntry_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,2,1))
zxAnOtdrFastTestIfStatusEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:zxAnOtdrFastTestIfStatusEntry.setStatus(_A)
class _ZxAnOtdrFastTestIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_m,5)))
_ZxAnOtdrFastTestIfStatus_Type.__name__=_C
_ZxAnOtdrFastTestIfStatus_Object=MibTableColumn
zxAnOtdrFastTestIfStatus=_ZxAnOtdrFastTestIfStatus_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,2,1,1),_ZxAnOtdrFastTestIfStatus_Type())
zxAnOtdrFastTestIfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfStatus.setStatus(_A)
class _ZxAnOtdrFastTestIfFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_P,1),(_Q,255)))
_ZxAnOtdrFastTestIfFailedReason_Type.__name__=_C
_ZxAnOtdrFastTestIfFailedReason_Object=MibTableColumn
zxAnOtdrFastTestIfFailedReason=_ZxAnOtdrFastTestIfFailedReason_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,2,1,2),_ZxAnOtdrFastTestIfFailedReason_Type())
zxAnOtdrFastTestIfFailedReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfFailedReason.setStatus(_A)
class _ZxAnOtdrFastTestIfResultFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnOtdrFastTestIfResultFile_Type.__name__=_E
_ZxAnOtdrFastTestIfResultFile_Object=MibTableColumn
zxAnOtdrFastTestIfResultFile=_ZxAnOtdrFastTestIfResultFile_Object((1,3,6,1,4,1,3902,1083,5,2,2,2,2,1,3),_ZxAnOtdrFastTestIfResultFile_Type())
zxAnOtdrFastTestIfResultFile.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFastTestIfResultFile.setStatus(_A)
_ZxAnOtdrFastTestFileFtpObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFastTestFileFtpObjects=_ZxAnOtdrFastTestFileFtpObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2,3))
_ZxAnOtdrFileFtpObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFileFtpObjects=_ZxAnOtdrFileFtpObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,2,3,1))
class _ZxAnOtdrFileFtpIpAddressType_Type(InetAddressType):defaultValue=1
_ZxAnOtdrFileFtpIpAddressType_Type.__name__=_R
_ZxAnOtdrFileFtpIpAddressType_Object=MibScalar
zxAnOtdrFileFtpIpAddressType=_ZxAnOtdrFileFtpIpAddressType_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,1),_ZxAnOtdrFileFtpIpAddressType_Type())
zxAnOtdrFileFtpIpAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpIpAddressType.setStatus(_A)
_ZxAnOtdrFileFtpIpAddress_Type=InetAddress
_ZxAnOtdrFileFtpIpAddress_Object=MibScalar
zxAnOtdrFileFtpIpAddress=_ZxAnOtdrFileFtpIpAddress_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,2),_ZxAnOtdrFileFtpIpAddress_Type())
zxAnOtdrFileFtpIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpIpAddress.setStatus(_A)
class _ZxAnOtdrFileFtpProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('sftp',2)))
_ZxAnOtdrFileFtpProtocolType_Type.__name__=_C
_ZxAnOtdrFileFtpProtocolType_Object=MibScalar
zxAnOtdrFileFtpProtocolType=_ZxAnOtdrFileFtpProtocolType_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,3),_ZxAnOtdrFileFtpProtocolType_Type())
zxAnOtdrFileFtpProtocolType.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpProtocolType.setStatus(_A)
class _ZxAnOtdrFileFtpUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFileFtpUserName_Type.__name__=_E
_ZxAnOtdrFileFtpUserName_Object=MibScalar
zxAnOtdrFileFtpUserName=_ZxAnOtdrFileFtpUserName_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,4),_ZxAnOtdrFileFtpUserName_Type())
zxAnOtdrFileFtpUserName.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpUserName.setStatus(_A)
class _ZxAnOtdrFileFtpUserPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFileFtpUserPwd_Type.__name__=_E
_ZxAnOtdrFileFtpUserPwd_Object=MibScalar
zxAnOtdrFileFtpUserPwd=_ZxAnOtdrFileFtpUserPwd_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,5),_ZxAnOtdrFileFtpUserPwd_Type())
zxAnOtdrFileFtpUserPwd.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpUserPwd.setStatus(_A)
class _ZxAnOtdrFileFtpPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ZxAnOtdrFileFtpPath_Type.__name__=_E
_ZxAnOtdrFileFtpPath_Object=MibScalar
zxAnOtdrFileFtpPath=_ZxAnOtdrFileFtpPath_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,6),_ZxAnOtdrFileFtpPath_Type())
zxAnOtdrFileFtpPath.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpPath.setStatus(_A)
class _ZxAnOtdrFileFtpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFileFtpFileName_Type.__name__=_E
_ZxAnOtdrFileFtpFileName_Object=MibScalar
zxAnOtdrFileFtpFileName=_ZxAnOtdrFileFtpFileName_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,1,7),_ZxAnOtdrFileFtpFileName_Type())
zxAnOtdrFileFtpFileName.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnOtdrFileFtpFileName.setStatus(_A)
_ZxAnOtdrFileFtpUploadStatusTable_Object=MibTable
zxAnOtdrFileFtpUploadStatusTable=_ZxAnOtdrFileFtpUploadStatusTable_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,2))
if mibBuilder.loadTexts:zxAnOtdrFileFtpUploadStatusTable.setStatus(_A)
_ZxAnOtdrFileFtpUploadStatusEntry_Object=MibTableRow
zxAnOtdrFileFtpUploadStatusEntry=_ZxAnOtdrFileFtpUploadStatusEntry_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,2,1))
zxAnOtdrFileFtpUploadStatusEntry.setIndexNames((0,_B,_n))
if mibBuilder.loadTexts:zxAnOtdrFileFtpUploadStatusEntry.setStatus(_A)
class _ZxAnOtdrFileFtpUploadFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFileFtpUploadFileName_Type.__name__=_E
_ZxAnOtdrFileFtpUploadFileName_Object=MibTableColumn
zxAnOtdrFileFtpUploadFileName=_ZxAnOtdrFileFtpUploadFileName_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,2,1,1),_ZxAnOtdrFileFtpUploadFileName_Type())
zxAnOtdrFileFtpUploadFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFileFtpUploadFileName.setStatus(_A)
class _ZxAnOtdrFileFtpUploadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_ZxAnOtdrFileFtpUploadStatus_Type.__name__=_C
_ZxAnOtdrFileFtpUploadStatus_Object=MibTableColumn
zxAnOtdrFileFtpUploadStatus=_ZxAnOtdrFileFtpUploadStatus_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,2,1,2),_ZxAnOtdrFileFtpUploadStatus_Type())
zxAnOtdrFileFtpUploadStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFileFtpUploadStatus.setStatus(_A)
class _ZxAnOtdrFileFtpUploadFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_P,1),('fileNotExists',2),('connectionFailed',3),(_Q,255)))
_ZxAnOtdrFileFtpUploadFailReason_Type.__name__=_C
_ZxAnOtdrFileFtpUploadFailReason_Object=MibTableColumn
zxAnOtdrFileFtpUploadFailReason=_ZxAnOtdrFileFtpUploadFailReason_Object((1,3,6,1,4,1,3902,1083,5,2,2,3,2,1,3),_ZxAnOtdrFileFtpUploadFailReason_Type())
zxAnOtdrFileFtpUploadFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrFileFtpUploadFailReason.setStatus(_A)
_ZxAnOtdrRoutineTestObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrRoutineTestObjects=_ZxAnOtdrRoutineTestObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,3))
_ZxAnOtdrRoutineTaskIfTable_Object=MibTable
zxAnOtdrRoutineTaskIfTable=_ZxAnOtdrRoutineTaskIfTable_Object((1,3,6,1,4,1,3902,1083,5,2,3,2))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfTable.setStatus(_A)
_ZxAnOtdrRoutineTaskIfEntry_Object=MibTableRow
zxAnOtdrRoutineTaskIfEntry=_ZxAnOtdrRoutineTaskIfEntry_Object((1,3,6,1,4,1,3902,1083,5,2,3,2,1))
zxAnOtdrRoutineTaskIfEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfEntry.setStatus(_A)
_ZxAnOtdrRoutineTaskIfRack_Type=Integer32
_ZxAnOtdrRoutineTaskIfRack_Object=MibTableColumn
zxAnOtdrRoutineTaskIfRack=_ZxAnOtdrRoutineTaskIfRack_Object((1,3,6,1,4,1,3902,1083,5,2,3,2,1,1),_ZxAnOtdrRoutineTaskIfRack_Type())
zxAnOtdrRoutineTaskIfRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfRack.setStatus(_A)
_ZxAnOtdrRoutineTaskIfShelf_Type=Integer32
_ZxAnOtdrRoutineTaskIfShelf_Object=MibTableColumn
zxAnOtdrRoutineTaskIfShelf=_ZxAnOtdrRoutineTaskIfShelf_Object((1,3,6,1,4,1,3902,1083,5,2,3,2,1,2),_ZxAnOtdrRoutineTaskIfShelf_Type())
zxAnOtdrRoutineTaskIfShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfShelf.setStatus(_A)
_ZxAnOtdrRoutineTaskIfSlot_Type=Integer32
_ZxAnOtdrRoutineTaskIfSlot_Object=MibTableColumn
zxAnOtdrRoutineTaskIfSlot=_ZxAnOtdrRoutineTaskIfSlot_Object((1,3,6,1,4,1,3902,1083,5,2,3,2,1,3),_ZxAnOtdrRoutineTaskIfSlot_Type())
zxAnOtdrRoutineTaskIfSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfSlot.setStatus(_A)
_ZxAnOtdrRoutineTaskIfPort_Type=Integer32
_ZxAnOtdrRoutineTaskIfPort_Object=MibTableColumn
zxAnOtdrRoutineTaskIfPort=_ZxAnOtdrRoutineTaskIfPort_Object((1,3,6,1,4,1,3902,1083,5,2,3,2,1,4),_ZxAnOtdrRoutineTaskIfPort_Type())
zxAnOtdrRoutineTaskIfPort.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfPort.setStatus(_A)
_ZxAnOtdrRoutineTaskIfRowStatus_Type=RowStatus
_ZxAnOtdrRoutineTaskIfRowStatus_Object=MibTableColumn
zxAnOtdrRoutineTaskIfRowStatus=_ZxAnOtdrRoutineTaskIfRowStatus_Object((1,3,6,1,4,1,3902,1083,5,2,3,2,1,50),_ZxAnOtdrRoutineTaskIfRowStatus_Type())
zxAnOtdrRoutineTaskIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfRowStatus.setStatus(_A)
_ZxAnOtdrRoutineTaskTable_Object=MibTable
zxAnOtdrRoutineTaskTable=_ZxAnOtdrRoutineTaskTable_Object((1,3,6,1,4,1,3902,1083,5,2,3,3))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskTable.setStatus(_A)
_ZxAnOtdrRoutineTaskEntry_Object=MibTableRow
zxAnOtdrRoutineTaskEntry=_ZxAnOtdrRoutineTaskEntry_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1))
zxAnOtdrRoutineTaskEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskEntry.setStatus(_A)
class _ZxAnOtdrRoutineTaskName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrRoutineTaskName_Type.__name__=_E
_ZxAnOtdrRoutineTaskName_Object=MibTableColumn
zxAnOtdrRoutineTaskName=_ZxAnOtdrRoutineTaskName_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,1),_ZxAnOtdrRoutineTaskName_Type())
zxAnOtdrRoutineTaskName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskName.setStatus(_A)
_ZxAnOtdrRoutineTaskStartTime_Type=DateAndTime
_ZxAnOtdrRoutineTaskStartTime_Object=MibTableColumn
zxAnOtdrRoutineTaskStartTime=_ZxAnOtdrRoutineTaskStartTime_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,2),_ZxAnOtdrRoutineTaskStartTime_Type())
zxAnOtdrRoutineTaskStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskStartTime.setStatus(_A)
class _ZxAnOtdrRoutineTaskInterval_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,525600))
_ZxAnOtdrRoutineTaskInterval_Type.__name__=_C
_ZxAnOtdrRoutineTaskInterval_Object=MibTableColumn
zxAnOtdrRoutineTaskInterval=_ZxAnOtdrRoutineTaskInterval_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,3),_ZxAnOtdrRoutineTaskInterval_Type())
zxAnOtdrRoutineTaskInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskInterval.setUnits('minutes')
class _ZxAnOtdrRoutineTaskActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activated',1),(_m,2)))
_ZxAnOtdrRoutineTaskActiveStatus_Type.__name__=_C
_ZxAnOtdrRoutineTaskActiveStatus_Object=MibTableColumn
zxAnOtdrRoutineTaskActiveStatus=_ZxAnOtdrRoutineTaskActiveStatus_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,4),_ZxAnOtdrRoutineTaskActiveStatus_Type())
zxAnOtdrRoutineTaskActiveStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskActiveStatus.setStatus(_A)
_ZxAnOtdrRoutineTaskCurrStartTime_Type=DateAndTime
_ZxAnOtdrRoutineTaskCurrStartTime_Object=MibTableColumn
zxAnOtdrRoutineTaskCurrStartTime=_ZxAnOtdrRoutineTaskCurrStartTime_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,5),_ZxAnOtdrRoutineTaskCurrStartTime_Type())
zxAnOtdrRoutineTaskCurrStartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskCurrStartTime.setStatus(_A)
class _ZxAnOtdrRoutineTaskOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_ZxAnOtdrRoutineTaskOperStatus_Type.__name__=_C
_ZxAnOtdrRoutineTaskOperStatus_Object=MibTableColumn
zxAnOtdrRoutineTaskOperStatus=_ZxAnOtdrRoutineTaskOperStatus_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,6),_ZxAnOtdrRoutineTaskOperStatus_Type())
zxAnOtdrRoutineTaskOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskOperStatus.setStatus(_A)
class _ZxAnOtdrRoutineTaskFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_P,1),(_Q,255)))
_ZxAnOtdrRoutineTaskFailedReason_Type.__name__=_C
_ZxAnOtdrRoutineTaskFailedReason_Object=MibTableColumn
zxAnOtdrRoutineTaskFailedReason=_ZxAnOtdrRoutineTaskFailedReason_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,7),_ZxAnOtdrRoutineTaskFailedReason_Type())
zxAnOtdrRoutineTaskFailedReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskFailedReason.setStatus(_A)
class _ZxAnOtdrRoutineTaskResultFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnOtdrRoutineTaskResultFile_Type.__name__=_E
_ZxAnOtdrRoutineTaskResultFile_Object=MibTableColumn
zxAnOtdrRoutineTaskResultFile=_ZxAnOtdrRoutineTaskResultFile_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,8),_ZxAnOtdrRoutineTaskResultFile_Type())
zxAnOtdrRoutineTaskResultFile.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskResultFile.setStatus(_A)
_ZxAnOtdrRoutineTaskRowStatus_Type=RowStatus
_ZxAnOtdrRoutineTaskRowStatus_Object=MibTableColumn
zxAnOtdrRoutineTaskRowStatus=_ZxAnOtdrRoutineTaskRowStatus_Object((1,3,6,1,4,1,3902,1083,5,2,3,3,1,50),_ZxAnOtdrRoutineTaskRowStatus_Type())
zxAnOtdrRoutineTaskRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskRowStatus.setStatus(_A)
_ZxAnOtdrRoutineTaskIfStatusTable_Object=MibTable
zxAnOtdrRoutineTaskIfStatusTable=_ZxAnOtdrRoutineTaskIfStatusTable_Object((1,3,6,1,4,1,3902,1083,5,2,3,4))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfStatusTable.setStatus(_A)
_ZxAnOtdrRoutineTaskIfStatusEntry_Object=MibTableRow
zxAnOtdrRoutineTaskIfStatusEntry=_ZxAnOtdrRoutineTaskIfStatusEntry_Object((1,3,6,1,4,1,3902,1083,5,2,3,4,1))
zxAnOtdrRoutineTaskIfStatusEntry.setIndexNames((0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfStatusEntry.setStatus(_A)
class _ZxAnOtdrRoutineTaskIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_ZxAnOtdrRoutineTaskIfStatus_Type.__name__=_C
_ZxAnOtdrRoutineTaskIfStatus_Object=MibTableColumn
zxAnOtdrRoutineTaskIfStatus=_ZxAnOtdrRoutineTaskIfStatus_Object((1,3,6,1,4,1,3902,1083,5,2,3,4,1,1),_ZxAnOtdrRoutineTaskIfStatus_Type())
zxAnOtdrRoutineTaskIfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfStatus.setStatus(_A)
class _ZxAnOtdrRoutineTaskIfFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,255)));namedValues=NamedValues(*((_P,1),(_Q,255)))
_ZxAnOtdrRoutineTaskIfFailReason_Type.__name__=_C
_ZxAnOtdrRoutineTaskIfFailReason_Object=MibTableColumn
zxAnOtdrRoutineTaskIfFailReason=_ZxAnOtdrRoutineTaskIfFailReason_Object((1,3,6,1,4,1,3902,1083,5,2,3,4,1,2),_ZxAnOtdrRoutineTaskIfFailReason_Type())
zxAnOtdrRoutineTaskIfFailReason.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskIfFailReason.setStatus(_A)
_ZxAnOtdrFtpServerObjects_ObjectIdentity=ObjectIdentity
zxAnOtdrFtpServerObjects=_ZxAnOtdrFtpServerObjects_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,2,4))
_ZxAnOtdrFtpServerTable_Object=MibTable
zxAnOtdrFtpServerTable=_ZxAnOtdrFtpServerTable_Object((1,3,6,1,4,1,3902,1083,5,2,4,2))
if mibBuilder.loadTexts:zxAnOtdrFtpServerTable.setStatus(_A)
_ZxAnOtdrFtpServerEntry_Object=MibTableRow
zxAnOtdrFtpServerEntry=_ZxAnOtdrFtpServerEntry_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1))
zxAnOtdrFtpServerEntry.setIndexNames((0,_B,_o))
if mibBuilder.loadTexts:zxAnOtdrFtpServerEntry.setStatus(_A)
class _ZxAnOtdrFtpServerId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFtpServerId_Type.__name__=_E
_ZxAnOtdrFtpServerId_Object=MibTableColumn
zxAnOtdrFtpServerId=_ZxAnOtdrFtpServerId_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,1),_ZxAnOtdrFtpServerId_Type())
zxAnOtdrFtpServerId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnOtdrFtpServerId.setStatus(_A)
class _ZxAnOtdrFtpServerIpAddressType_Type(InetAddressType):defaultValue=1
_ZxAnOtdrFtpServerIpAddressType_Type.__name__=_R
_ZxAnOtdrFtpServerIpAddressType_Object=MibTableColumn
zxAnOtdrFtpServerIpAddressType=_ZxAnOtdrFtpServerIpAddressType_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,2),_ZxAnOtdrFtpServerIpAddressType_Type())
zxAnOtdrFtpServerIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerIpAddressType.setStatus(_A)
_ZxAnOtdrFtpServerIpAddress_Type=InetAddress
_ZxAnOtdrFtpServerIpAddress_Object=MibTableColumn
zxAnOtdrFtpServerIpAddress=_ZxAnOtdrFtpServerIpAddress_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,3),_ZxAnOtdrFtpServerIpAddress_Type())
zxAnOtdrFtpServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerIpAddress.setStatus(_A)
class _ZxAnOtdrFtpServerProtocolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ftp',1),('sftp',2)))
_ZxAnOtdrFtpServerProtocolType_Type.__name__=_C
_ZxAnOtdrFtpServerProtocolType_Object=MibTableColumn
zxAnOtdrFtpServerProtocolType=_ZxAnOtdrFtpServerProtocolType_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,4),_ZxAnOtdrFtpServerProtocolType_Type())
zxAnOtdrFtpServerProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerProtocolType.setStatus(_A)
class _ZxAnOtdrFtpServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFtpServerUserName_Type.__name__=_E
_ZxAnOtdrFtpServerUserName_Object=MibTableColumn
zxAnOtdrFtpServerUserName=_ZxAnOtdrFtpServerUserName_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,5),_ZxAnOtdrFtpServerUserName_Type())
zxAnOtdrFtpServerUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerUserName.setStatus(_A)
class _ZxAnOtdrFtpServerUserPwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnOtdrFtpServerUserPwd_Type.__name__=_E
_ZxAnOtdrFtpServerUserPwd_Object=MibTableColumn
zxAnOtdrFtpServerUserPwd=_ZxAnOtdrFtpServerUserPwd_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,6),_ZxAnOtdrFtpServerUserPwd_Type())
zxAnOtdrFtpServerUserPwd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerUserPwd.setStatus(_A)
class _ZxAnOtdrFtpServerPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ZxAnOtdrFtpServerPath_Type.__name__=_E
_ZxAnOtdrFtpServerPath_Object=MibTableColumn
zxAnOtdrFtpServerPath=_ZxAnOtdrFtpServerPath_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,7),_ZxAnOtdrFtpServerPath_Type())
zxAnOtdrFtpServerPath.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerPath.setStatus(_A)
_ZxAnOtdrFtpServerRowStatus_Type=RowStatus
_ZxAnOtdrFtpServerRowStatus_Object=MibTableColumn
zxAnOtdrFtpServerRowStatus=_ZxAnOtdrFtpServerRowStatus_Object((1,3,6,1,4,1,3902,1083,5,2,4,2,1,50),_ZxAnOtdrFtpServerRowStatus_Type())
zxAnOtdrFtpServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnOtdrFtpServerRowStatus.setStatus(_A)
_ZxAnOtdrNotifications_ObjectIdentity=ObjectIdentity
zxAnOtdrNotifications=_ZxAnOtdrNotifications_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,3))
_ZxAnOtdrEnvTraps_ObjectIdentity=ObjectIdentity
zxAnOtdrEnvTraps=_ZxAnOtdrEnvTraps_ObjectIdentity((1,3,6,1,4,1,3902,1083,5,3,50))
zxAnOtdrRoutineTaskFinished=NotificationType((1,3,6,1,4,1,3902,1083,5,3,1))
zxAnOtdrRoutineTaskFinished.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:zxAnOtdrRoutineTaskFinished.setStatus(_A)
zxAnOtdrEnvCtrlCardHighTempAlm=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,1))
zxAnOtdrEnvCtrlCardHighTempAlm.setObjects(*((_B,_J),(_B,_c)))
if mibBuilder.loadTexts:zxAnOtdrEnvCtrlCardHighTempAlm.setStatus(_A)
zxAnOtdrEnvCtrlCardHighTempClr=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,2))
zxAnOtdrEnvCtrlCardHighTempClr.setObjects(*((_B,_J),(_B,_c)))
if mibBuilder.loadTexts:zxAnOtdrEnvCtrlCardHighTempClr.setStatus(_A)
zxAnOtdrEnvCtrlCardLowTempAlm=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,3))
zxAnOtdrEnvCtrlCardLowTempAlm.setObjects(*((_B,_J),(_B,_d)))
if mibBuilder.loadTexts:zxAnOtdrEnvCtrlCardLowTempAlm.setStatus(_A)
zxAnOtdrEnvCtrlCardLowTempClr=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,4))
zxAnOtdrEnvCtrlCardLowTempClr.setObjects(*((_B,_J),(_B,_d)))
if mibBuilder.loadTexts:zxAnOtdrEnvCtrlCardLowTempClr.setStatus(_A)
zxAnOtdrEnvFanFailureAlm=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,5))
zxAnOtdrEnvFanFailureAlm.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:zxAnOtdrEnvFanFailureAlm.setStatus(_A)
zxAnOtdrEnvFanFailureClr=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,6))
zxAnOtdrEnvFanFailureClr.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:zxAnOtdrEnvFanFailureClr.setStatus(_A)
zxAnOtdrEnvApdHighTempAlm=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,7))
zxAnOtdrEnvApdHighTempAlm.setObjects(*((_B,_K),(_B,_g)))
if mibBuilder.loadTexts:zxAnOtdrEnvApdHighTempAlm.setStatus(_A)
zxAnOtdrEnvApdHighTempClr=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,8))
zxAnOtdrEnvApdHighTempClr.setObjects(*((_B,_K),(_B,_g)))
if mibBuilder.loadTexts:zxAnOtdrEnvApdHighTempClr.setStatus(_A)
zxAnOtdrEnvApdLowTempAlm=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,9))
zxAnOtdrEnvApdLowTempAlm.setObjects(*((_B,_K),(_B,_t)))
if mibBuilder.loadTexts:zxAnOtdrEnvApdLowTempAlm.setStatus(_A)
zxAnOtdrEnvApdLowTempClr=NotificationType((1,3,6,1,4,1,3902,1083,5,3,50,10))
zxAnOtdrEnvApdLowTempClr.setObjects(*((_B,'zxAnOtdrApdCurrentTemperature'),(_B,_K)))
if mibBuilder.loadTexts:zxAnOtdrEnvApdLowTempClr.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnOtdrMib':zxAnOtdrMib,'zxAnOtdrGlobalObjects':zxAnOtdrGlobalObjects,'zxAnOtdrCapacityGlobalObjects':zxAnOtdrCapacityGlobalObjects,'zxAnOtdrWaveLengthList':zxAnOtdrWaveLengthList,'zxAnOtdrTestPulseWidthList':zxAnOtdrTestPulseWidthList,'zxAnOtdrTotalPorts':zxAnOtdrTotalPorts,'zxAnOtdrEnvGlobalObjects':zxAnOtdrEnvGlobalObjects,'zxAnOtdrEnvCtrlCardGlobalObjects':zxAnOtdrEnvCtrlCardGlobalObjects,_J:zxAnOtdrCtrlCardCurrentTemp,_c:zxAnOtdrCtrlCardTempHighThresh,_d:zxAnOtdrCtrlCardTempLowThresh,'zxAnOtdrEnvFanGlobalObjects':zxAnOtdrEnvFanGlobalObjects,_e:zxAnOtdrEnvFanStatus,_f:zxAnOtdrEnvFanOperStatus,'zxAnOtdrEnvApdGlobalObjects':zxAnOtdrEnvApdGlobalObjects,_K:zxAnOtdrEnvApdCurrentTemp,_g:zxAnOtdrEnvApdTempHighThresh,_t:zxAnOtdrEnvApdTempLowThresh,'zxAnOtdrObjects':zxAnOtdrObjects,'zxAnOtdrIfObjects':zxAnOtdrIfObjects,'zxAnOtdrTestParamPrfTable':zxAnOtdrTestParamPrfTable,'zxAnOtdrTestParamPrfEntry':zxAnOtdrTestParamPrfEntry,_h:zxAnOtdrTestParamPrfName,'zxAnOtdrTestParamPrfMode':zxAnOtdrTestParamPrfMode,'zxAnOtdrTestParamPrfWaveLength':zxAnOtdrTestParamPrfWaveLength,'zxAnOtdrTestParamPrfDistance':zxAnOtdrTestParamPrfDistance,'zxAnOtdrTestParamPrfFiberIor':zxAnOtdrTestParamPrfFiberIor,'zxAnOtdrTestParamPrfPulseWidth':zxAnOtdrTestParamPrfPulseWidth,'zxAnOtdrTestParamPrfDuration':zxAnOtdrTestParamPrfDuration,'zxAnOtdrTestParamPrfSeqCode':zxAnOtdrTestParamPrfSeqCode,'zxAnOtdrTestParamPrfSeqCodeLen':zxAnOtdrTestParamPrfSeqCodeLen,'zxAnOtdrTestParamPrfCodeWidth':zxAnOtdrTestParamPrfCodeWidth,'zxAnOtdrTestParamPrfTimes':zxAnOtdrTestParamPrfTimes,'zxAnOtdrTestParamPrfInterval':zxAnOtdrTestParamPrfInterval,'zxAnOtdrTestParamPrfRowStatus':zxAnOtdrTestParamPrfRowStatus,'zxAnOtdrIfTable':zxAnOtdrIfTable,'zxAnOtdrIfEntry':zxAnOtdrIfEntry,_i:zxAnOtdrIfRack,_j:zxAnOtdrIfShelf,_k:zxAnOtdrIfSlot,_l:zxAnOtdrIfPort,'zxAnOtdrIfAlias':zxAnOtdrIfAlias,'zxAnOtdrIfFastTestParamPrf':zxAnOtdrIfFastTestParamPrf,'zxAnOtdrIfRoutineTestParamPrf':zxAnOtdrIfRoutineTestParamPrf,'zxAnOtdrFastTestObjects':zxAnOtdrFastTestObjects,'zxAnOtdrFastTestConfObjects':zxAnOtdrFastTestConfObjects,'zxAnOtdrFastTestActionObjects':zxAnOtdrFastTestActionObjects,'zxAnOtdrFastTestSn':zxAnOtdrFastTestSn,'zxAnOtdrFastTestAction':zxAnOtdrFastTestAction,'zxAnOtdrFastTestIfTable':zxAnOtdrFastTestIfTable,'zxAnOtdrFastTestIfEntry':zxAnOtdrFastTestIfEntry,_S:zxAnOtdrFastTestIfSn,_T:zxAnOtdrFastTestIfRack,_U:zxAnOtdrFastTestIfShelf,_V:zxAnOtdrFastTestIfSlot,_W:zxAnOtdrFastTestIfPort,'zxAnOtdrFastTestIfRowStatus':zxAnOtdrFastTestIfRowStatus,'zxAnOtdrFastTestStatusObjects':zxAnOtdrFastTestStatusObjects,'zxAnOtdrFastTestStatusGlbObjects':zxAnOtdrFastTestStatusGlbObjects,'zxAnOtdrFastTestCurrentPort':zxAnOtdrFastTestCurrentPort,'zxAnOtdrFastTestWaitTestPorts':zxAnOtdrFastTestWaitTestPorts,'zxAnOtdrFastTestIfStatusTable':zxAnOtdrFastTestIfStatusTable,'zxAnOtdrFastTestIfStatusEntry':zxAnOtdrFastTestIfStatusEntry,'zxAnOtdrFastTestIfStatus':zxAnOtdrFastTestIfStatus,'zxAnOtdrFastTestIfFailedReason':zxAnOtdrFastTestIfFailedReason,'zxAnOtdrFastTestIfResultFile':zxAnOtdrFastTestIfResultFile,'zxAnOtdrFastTestFileFtpObjects':zxAnOtdrFastTestFileFtpObjects,'zxAnOtdrFileFtpObjects':zxAnOtdrFileFtpObjects,'zxAnOtdrFileFtpIpAddressType':zxAnOtdrFileFtpIpAddressType,'zxAnOtdrFileFtpIpAddress':zxAnOtdrFileFtpIpAddress,'zxAnOtdrFileFtpProtocolType':zxAnOtdrFileFtpProtocolType,'zxAnOtdrFileFtpUserName':zxAnOtdrFileFtpUserName,'zxAnOtdrFileFtpUserPwd':zxAnOtdrFileFtpUserPwd,'zxAnOtdrFileFtpPath':zxAnOtdrFileFtpPath,'zxAnOtdrFileFtpFileName':zxAnOtdrFileFtpFileName,'zxAnOtdrFileFtpUploadStatusTable':zxAnOtdrFileFtpUploadStatusTable,'zxAnOtdrFileFtpUploadStatusEntry':zxAnOtdrFileFtpUploadStatusEntry,_n:zxAnOtdrFileFtpUploadFileName,'zxAnOtdrFileFtpUploadStatus':zxAnOtdrFileFtpUploadStatus,'zxAnOtdrFileFtpUploadFailReason':zxAnOtdrFileFtpUploadFailReason,'zxAnOtdrRoutineTestObjects':zxAnOtdrRoutineTestObjects,'zxAnOtdrRoutineTaskIfTable':zxAnOtdrRoutineTaskIfTable,'zxAnOtdrRoutineTaskIfEntry':zxAnOtdrRoutineTaskIfEntry,_Y:zxAnOtdrRoutineTaskIfRack,_Z:zxAnOtdrRoutineTaskIfShelf,_a:zxAnOtdrRoutineTaskIfSlot,_b:zxAnOtdrRoutineTaskIfPort,'zxAnOtdrRoutineTaskIfRowStatus':zxAnOtdrRoutineTaskIfRowStatus,'zxAnOtdrRoutineTaskTable':zxAnOtdrRoutineTaskTable,'zxAnOtdrRoutineTaskEntry':zxAnOtdrRoutineTaskEntry,_X:zxAnOtdrRoutineTaskName,'zxAnOtdrRoutineTaskStartTime':zxAnOtdrRoutineTaskStartTime,'zxAnOtdrRoutineTaskInterval':zxAnOtdrRoutineTaskInterval,'zxAnOtdrRoutineTaskActiveStatus':zxAnOtdrRoutineTaskActiveStatus,_p:zxAnOtdrRoutineTaskCurrStartTime,_q:zxAnOtdrRoutineTaskOperStatus,_r:zxAnOtdrRoutineTaskFailedReason,_s:zxAnOtdrRoutineTaskResultFile,'zxAnOtdrRoutineTaskRowStatus':zxAnOtdrRoutineTaskRowStatus,'zxAnOtdrRoutineTaskIfStatusTable':zxAnOtdrRoutineTaskIfStatusTable,'zxAnOtdrRoutineTaskIfStatusEntry':zxAnOtdrRoutineTaskIfStatusEntry,'zxAnOtdrRoutineTaskIfStatus':zxAnOtdrRoutineTaskIfStatus,'zxAnOtdrRoutineTaskIfFailReason':zxAnOtdrRoutineTaskIfFailReason,'zxAnOtdrFtpServerObjects':zxAnOtdrFtpServerObjects,'zxAnOtdrFtpServerTable':zxAnOtdrFtpServerTable,'zxAnOtdrFtpServerEntry':zxAnOtdrFtpServerEntry,_o:zxAnOtdrFtpServerId,'zxAnOtdrFtpServerIpAddressType':zxAnOtdrFtpServerIpAddressType,'zxAnOtdrFtpServerIpAddress':zxAnOtdrFtpServerIpAddress,'zxAnOtdrFtpServerProtocolType':zxAnOtdrFtpServerProtocolType,'zxAnOtdrFtpServerUserName':zxAnOtdrFtpServerUserName,'zxAnOtdrFtpServerUserPwd':zxAnOtdrFtpServerUserPwd,'zxAnOtdrFtpServerPath':zxAnOtdrFtpServerPath,'zxAnOtdrFtpServerRowStatus':zxAnOtdrFtpServerRowStatus,'zxAnOtdrNotifications':zxAnOtdrNotifications,'zxAnOtdrRoutineTaskFinished':zxAnOtdrRoutineTaskFinished,'zxAnOtdrEnvTraps':zxAnOtdrEnvTraps,'zxAnOtdrEnvCtrlCardHighTempAlm':zxAnOtdrEnvCtrlCardHighTempAlm,'zxAnOtdrEnvCtrlCardHighTempClr':zxAnOtdrEnvCtrlCardHighTempClr,'zxAnOtdrEnvCtrlCardLowTempAlm':zxAnOtdrEnvCtrlCardLowTempAlm,'zxAnOtdrEnvCtrlCardLowTempClr':zxAnOtdrEnvCtrlCardLowTempClr,'zxAnOtdrEnvFanFailureAlm':zxAnOtdrEnvFanFailureAlm,'zxAnOtdrEnvFanFailureClr':zxAnOtdrEnvFanFailureClr,'zxAnOtdrEnvApdHighTempAlm':zxAnOtdrEnvApdHighTempAlm,'zxAnOtdrEnvApdHighTempClr':zxAnOtdrEnvApdHighTempClr,'zxAnOtdrEnvApdLowTempAlm':zxAnOtdrEnvApdLowTempAlm,'zxAnOtdrEnvApdLowTempClr':zxAnOtdrEnvApdLowTempClr})