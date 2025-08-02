_g='cfgMERRulesTableIndex'
_f='cfgInputPowerBaseLineChannelIndex'
_e='qam1024'
_d='qam512'
_c='qam256'
_b='qam128'
_a='analog'
_Z='cfgChannelInclusionIndex'
_Y='cfgChannelExclusionIndex'
_X='dmonUserFreqProvIndex'
_W='second'
_V='dmonParkModeReceiverID'
_U='eight-mhz'
_T='six-mhz'
_S='re-start'
_R='fast-scan'
_Q='manual'
_P='TimeInterval'
_O='DisplayString'
_N='trillionth'
_M='enabled'
_L='disabled'
_K='TenthdB'
_J='dBmV'
_I='TenthdBmV'
_H='hertz'
_G='DMON-COMMON-MIB'
_F='Unsigned32'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModulationType,dmonMib=mibBuilder.importSymbols('DMON-MIB','ModulationType','dmonMib')
TenthdB,TenthdBmV=mibBuilder.importSymbols('DOCS-IF-MIB',_K,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_O,'PhysAddress','RowStatus','StorageType','TextualConvention',_P,'TruthValue')
dmonCommonGroup=ModuleIdentity((1,3,6,1,4,1,5802,999999,2))
class _DmonGpsPosition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DmonGpsPosition_Type.__name__=_O
_DmonGpsPosition_Object=MibScalar
dmonGpsPosition=_DmonGpsPosition_Object((1,3,6,1,4,1,5802,999999,2,1),_DmonGpsPosition_Type())
dmonGpsPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonGpsPosition.setStatus(_A)
_DmonOperation_ObjectIdentity=ObjectIdentity
dmonOperation=_DmonOperation_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,2))
class _DmonOperationMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('auto',0),(_Q,1),(_R,2),(_S,3)))
_DmonOperationMode_Type.__name__=_C
_DmonOperationMode_Object=MibScalar
dmonOperationMode=_DmonOperationMode_Object((1,3,6,1,4,1,5802,999999,2,2,1),_DmonOperationMode_Type())
dmonOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonOperationMode.setStatus(_A)
class _DmonOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('auto',0),(_Q,1),(_R,2),(_S,3),('baseline',4)))
_DmonOperationStatus_Type.__name__=_C
_DmonOperationStatus_Object=MibScalar
dmonOperationStatus=_DmonOperationStatus_Object((1,3,6,1,4,1,5802,999999,2,2,2),_DmonOperationStatus_Type())
dmonOperationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dmonOperationStatus.setStatus(_A)
class _DmonOperationAutoScanTask_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('physcan',1),('mpegscan',2),('bothscan',3)))
_DmonOperationAutoScanTask_Type.__name__=_C
_DmonOperationAutoScanTask_Object=MibScalar
dmonOperationAutoScanTask=_DmonOperationAutoScanTask_Object((1,3,6,1,4,1,5802,999999,2,2,3),_DmonOperationAutoScanTask_Type())
dmonOperationAutoScanTask.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonOperationAutoScanTask.setStatus(_A)
_DmonVideoModeTable_ObjectIdentity=ObjectIdentity
dmonVideoModeTable=_DmonVideoModeTable_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,4))
class _DmonVideoModeChannelBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_DmonVideoModeChannelBandwidth_Type.__name__=_C
_DmonVideoModeChannelBandwidth_Object=MibScalar
dmonVideoModeChannelBandwidth=_DmonVideoModeChannelBandwidth_Object((1,3,6,1,4,1,5802,999999,2,4,1),_DmonVideoModeChannelBandwidth_Type())
dmonVideoModeChannelBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonVideoModeChannelBandwidth.setStatus(_A)
_DmonParkModeControlTable_Object=MibTable
dmonParkModeControlTable=_DmonParkModeControlTable_Object((1,3,6,1,4,1,5802,999999,2,5))
if mibBuilder.loadTexts:dmonParkModeControlTable.setStatus(_A)
_DmonParkModeControlEntry_Object=MibTableRow
dmonParkModeControlEntry=_DmonParkModeControlEntry_Object((1,3,6,1,4,1,5802,999999,2,5,1))
dmonParkModeControlEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:dmonParkModeControlEntry.setStatus(_A)
_DmonParkModeReceiverID_Type=Integer32
_DmonParkModeReceiverID_Object=MibTableColumn
dmonParkModeReceiverID=_DmonParkModeReceiverID_Object((1,3,6,1,4,1,5802,999999,2,5,1,1),_DmonParkModeReceiverID_Type())
dmonParkModeReceiverID.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeReceiverID.setStatus(_A)
class _DmonParkModeReceiverStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('isScanning',0),('isParked-Infinite',1),('isParked-Timed',2),('isUsedByDOCSIS',3),('other',4)))
_DmonParkModeReceiverStatus_Type.__name__=_C
_DmonParkModeReceiverStatus_Object=MibTableColumn
dmonParkModeReceiverStatus=_DmonParkModeReceiverStatus_Object((1,3,6,1,4,1,5802,999999,2,5,1,2),_DmonParkModeReceiverStatus_Type())
dmonParkModeReceiverStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dmonParkModeReceiverStatus.setStatus(_A)
class _DmonParkModeReceiverParkingFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_DmonParkModeReceiverParkingFrequency_Type.__name__=_C
_DmonParkModeReceiverParkingFrequency_Object=MibTableColumn
dmonParkModeReceiverParkingFrequency=_DmonParkModeReceiverParkingFrequency_Object((1,3,6,1,4,1,5802,999999,2,5,1,3),_DmonParkModeReceiverParkingFrequency_Type())
dmonParkModeReceiverParkingFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeReceiverParkingFrequency.setStatus(_A)
if mibBuilder.loadTexts:dmonParkModeReceiverParkingFrequency.setUnits(_H)
class _DmonParkModeReceiverSymbolRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_DmonParkModeReceiverSymbolRate_Type.__name__=_C
_DmonParkModeReceiverSymbolRate_Object=MibTableColumn
dmonParkModeReceiverSymbolRate=_DmonParkModeReceiverSymbolRate_Object((1,3,6,1,4,1,5802,999999,2,5,1,4),_DmonParkModeReceiverSymbolRate_Type())
dmonParkModeReceiverSymbolRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeReceiverSymbolRate.setStatus(_A)
_DmonParkModeReceiverQamType_Type=ModulationType
_DmonParkModeReceiverQamType_Object=MibTableColumn
dmonParkModeReceiverQamType=_DmonParkModeReceiverQamType_Object((1,3,6,1,4,1,5802,999999,2,5,1,5),_DmonParkModeReceiverQamType_Type())
dmonParkModeReceiverQamType.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeReceiverQamType.setStatus(_A)
class _DmonParkModeReceiverInverseMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_DmonParkModeReceiverInverseMode_Type.__name__=_C
_DmonParkModeReceiverInverseMode_Object=MibTableColumn
dmonParkModeReceiverInverseMode=_DmonParkModeReceiverInverseMode_Object((1,3,6,1,4,1,5802,999999,2,5,1,6),_DmonParkModeReceiverInverseMode_Type())
dmonParkModeReceiverInverseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeReceiverInverseMode.setStatus(_A)
class _DmonParkModeDwellTime_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_DmonParkModeDwellTime_Type.__name__=_C
_DmonParkModeDwellTime_Object=MibTableColumn
dmonParkModeDwellTime=_DmonParkModeDwellTime_Object((1,3,6,1,4,1,5802,999999,2,5,1,7),_DmonParkModeDwellTime_Type())
dmonParkModeDwellTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeDwellTime.setStatus(_A)
if mibBuilder.loadTexts:dmonParkModeDwellTime.setUnits(_W)
class _DmonParkModeReceiverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('scanningMode',0),('parkingMode',1),('notAvailable',2)))
_DmonParkModeReceiverControl_Type.__name__=_C
_DmonParkModeReceiverControl_Object=MibTableColumn
dmonParkModeReceiverControl=_DmonParkModeReceiverControl_Object((1,3,6,1,4,1,5802,999999,2,5,1,8),_DmonParkModeReceiverControl_Type())
dmonParkModeReceiverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonParkModeReceiverControl.setStatus(_A)
class _DmonLocalAccess_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_DmonLocalAccess_Type.__name__=_C
_DmonLocalAccess_Object=MibScalar
dmonLocalAccess=_DmonLocalAccess_Object((1,3,6,1,4,1,5802,999999,2,6),_DmonLocalAccess_Type())
dmonLocalAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonLocalAccess.setStatus(_A)
class _DmonDwellingTIme_Type(TimeInterval):defaultValue=10
_DmonDwellingTIme_Type.__name__=_P
_DmonDwellingTIme_Object=MibScalar
dmonDwellingTIme=_DmonDwellingTIme_Object((1,3,6,1,4,1,5802,999999,2,7),_DmonDwellingTIme_Type())
dmonDwellingTIme.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonDwellingTIme.setStatus(_A)
if mibBuilder.loadTexts:dmonDwellingTIme.setUnits(_W)
class _DmonLanguageCharset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('utf8',0),('gbk',1),('gb18030',2),('big5',3),('iso-8859-15',4),('ascii',5)))
_DmonLanguageCharset_Type.__name__=_C
_DmonLanguageCharset_Object=MibScalar
dmonLanguageCharset=_DmonLanguageCharset_Object((1,3,6,1,4,1,5802,999999,2,8),_DmonLanguageCharset_Type())
dmonLanguageCharset.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonLanguageCharset.setStatus(_A)
class _DmonChannelPlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('eia542',0),('fixed-inc',1),('userdefined',2)))
_DmonChannelPlan_Type.__name__=_C
_DmonChannelPlan_Object=MibScalar
dmonChannelPlan=_DmonChannelPlan_Object((1,3,6,1,4,1,5802,999999,2,9),_DmonChannelPlan_Type())
dmonChannelPlan.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonChannelPlan.setStatus(_A)
_DmonFixedIncTable_ObjectIdentity=ObjectIdentity
dmonFixedIncTable=_DmonFixedIncTable_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,10))
class _DmonFixedIncStartFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(57000000,999000000))
_DmonFixedIncStartFreq_Type.__name__=_F
_DmonFixedIncStartFreq_Object=MibScalar
dmonFixedIncStartFreq=_DmonFixedIncStartFreq_Object((1,3,6,1,4,1,5802,999999,2,10,1),_DmonFixedIncStartFreq_Type())
dmonFixedIncStartFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonFixedIncStartFreq.setStatus(_A)
class _DmonFixedIncFreqStep_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000000,54000000))
_DmonFixedIncFreqStep_Type.__name__=_F
_DmonFixedIncFreqStep_Object=MibScalar
dmonFixedIncFreqStep=_DmonFixedIncFreqStep_Object((1,3,6,1,4,1,5802,999999,2,10,2),_DmonFixedIncFreqStep_Type())
dmonFixedIncFreqStep.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonFixedIncFreqStep.setStatus(_A)
class _DmonFixedIncEndFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(57000000,999000000))
_DmonFixedIncEndFreq_Type.__name__=_F
_DmonFixedIncEndFreq_Object=MibScalar
dmonFixedIncEndFreq=_DmonFixedIncEndFreq_Object((1,3,6,1,4,1,5802,999999,2,10,3),_DmonFixedIncEndFreq_Type())
dmonFixedIncEndFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonFixedIncEndFreq.setStatus(_A)
class _DmonFixedIncSymbolRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999000000))
_DmonFixedIncSymbolRate_Type.__name__=_F
_DmonFixedIncSymbolRate_Object=MibScalar
dmonFixedIncSymbolRate=_DmonFixedIncSymbolRate_Object((1,3,6,1,4,1,5802,999999,2,10,4),_DmonFixedIncSymbolRate_Type())
dmonFixedIncSymbolRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonFixedIncSymbolRate.setStatus(_A)
class _DmonFixedIncInverseMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_DmonFixedIncInverseMode_Type.__name__=_C
_DmonFixedIncInverseMode_Object=MibScalar
dmonFixedIncInverseMode=_DmonFixedIncInverseMode_Object((1,3,6,1,4,1,5802,999999,2,10,5),_DmonFixedIncInverseMode_Type())
dmonFixedIncInverseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonFixedIncInverseMode.setStatus(_A)
_DmonFixedIncQamType_Type=ModulationType
_DmonFixedIncQamType_Object=MibScalar
dmonFixedIncQamType=_DmonFixedIncQamType_Object((1,3,6,1,4,1,5802,999999,2,10,6),_DmonFixedIncQamType_Type())
dmonFixedIncQamType.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonFixedIncQamType.setStatus(_A)
_DmonUserFreqTable_Object=MibTable
dmonUserFreqTable=_DmonUserFreqTable_Object((1,3,6,1,4,1,5802,999999,2,11))
if mibBuilder.loadTexts:dmonUserFreqTable.setStatus(_A)
_DmonUserFreqEntry_Object=MibTableRow
dmonUserFreqEntry=_DmonUserFreqEntry_Object((1,3,6,1,4,1,5802,999999,2,11,1))
dmonUserFreqEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:dmonUserFreqEntry.setStatus(_A)
class _DmonUserFreqProvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DmonUserFreqProvIndex_Type.__name__=_C
_DmonUserFreqProvIndex_Object=MibTableColumn
dmonUserFreqProvIndex=_DmonUserFreqProvIndex_Object((1,3,6,1,4,1,5802,999999,2,11,1,1),_DmonUserFreqProvIndex_Type())
dmonUserFreqProvIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dmonUserFreqProvIndex.setStatus(_A)
_DmonUserFreqProvStatus_Type=RowStatus
_DmonUserFreqProvStatus_Object=MibTableColumn
dmonUserFreqProvStatus=_DmonUserFreqProvStatus_Object((1,3,6,1,4,1,5802,999999,2,11,1,2),_DmonUserFreqProvStatus_Type())
dmonUserFreqProvStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dmonUserFreqProvStatus.setStatus(_A)
class _DmonUserFreqProvFrequency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(57000000,999000000))
_DmonUserFreqProvFrequency_Type.__name__=_F
_DmonUserFreqProvFrequency_Object=MibTableColumn
dmonUserFreqProvFrequency=_DmonUserFreqProvFrequency_Object((1,3,6,1,4,1,5802,999999,2,11,1,3),_DmonUserFreqProvFrequency_Type())
dmonUserFreqProvFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonUserFreqProvFrequency.setStatus(_A)
_DmonUserFreqProvModulation_Type=ModulationType
_DmonUserFreqProvModulation_Object=MibTableColumn
dmonUserFreqProvModulation=_DmonUserFreqProvModulation_Object((1,3,6,1,4,1,5802,999999,2,11,1,4),_DmonUserFreqProvModulation_Type())
dmonUserFreqProvModulation.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonUserFreqProvModulation.setStatus(_A)
class _DmonUserFreqProvSymbolRate_Type(Unsigned32):defaultValue=0
_DmonUserFreqProvSymbolRate_Type.__name__=_F
_DmonUserFreqProvSymbolRate_Object=MibTableColumn
dmonUserFreqProvSymbolRate=_DmonUserFreqProvSymbolRate_Object((1,3,6,1,4,1,5802,999999,2,11,1,5),_DmonUserFreqProvSymbolRate_Type())
dmonUserFreqProvSymbolRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonUserFreqProvSymbolRate.setStatus(_A)
class _DmonUserFreqProvInversion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_DmonUserFreqProvInversion_Type.__name__=_C
_DmonUserFreqProvInversion_Object=MibTableColumn
dmonUserFreqProvInversion=_DmonUserFreqProvInversion_Object((1,3,6,1,4,1,5802,999999,2,11,1,6),_DmonUserFreqProvInversion_Type())
dmonUserFreqProvInversion.setMaxAccess(_B)
if mibBuilder.loadTexts:dmonUserFreqProvInversion.setStatus(_A)
_CfgChannelMap_ObjectIdentity=ObjectIdentity
cfgChannelMap=_CfgChannelMap_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,18))
class _CfgChannelMapSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dsg',0),('auto-discovery',1),('provisioning',2)))
_CfgChannelMapSource_Type.__name__=_C
_CfgChannelMapSource_Object=MibScalar
cfgChannelMapSource=_CfgChannelMapSource_Object((1,3,6,1,4,1,5802,999999,2,18,1),_CfgChannelMapSource_Type())
cfgChannelMapSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgChannelMapSource.setStatus(_A)
_CfgChannelExclusionTable_Object=MibTable
cfgChannelExclusionTable=_CfgChannelExclusionTable_Object((1,3,6,1,4,1,5802,999999,2,18,2))
if mibBuilder.loadTexts:cfgChannelExclusionTable.setStatus(_A)
_CfgChannelExclusionEntry_Object=MibTableRow
cfgChannelExclusionEntry=_CfgChannelExclusionEntry_Object((1,3,6,1,4,1,5802,999999,2,18,2,1))
cfgChannelExclusionEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:cfgChannelExclusionEntry.setStatus(_A)
_CfgChannelExclusionIndex_Type=Integer32
_CfgChannelExclusionIndex_Object=MibTableColumn
cfgChannelExclusionIndex=_CfgChannelExclusionIndex_Object((1,3,6,1,4,1,5802,999999,2,18,2,1,1),_CfgChannelExclusionIndex_Type())
cfgChannelExclusionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgChannelExclusionIndex.setStatus(_A)
_CfgChannelExclusionStatus_Type=RowStatus
_CfgChannelExclusionStatus_Object=MibTableColumn
cfgChannelExclusionStatus=_CfgChannelExclusionStatus_Object((1,3,6,1,4,1,5802,999999,2,18,2,1,2),_CfgChannelExclusionStatus_Type())
cfgChannelExclusionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelExclusionStatus.setStatus(_A)
class _CfgChannelExclusionStartFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CfgChannelExclusionStartFrequency_Type.__name__=_C
_CfgChannelExclusionStartFrequency_Object=MibTableColumn
cfgChannelExclusionStartFrequency=_CfgChannelExclusionStartFrequency_Object((1,3,6,1,4,1,5802,999999,2,18,2,1,3),_CfgChannelExclusionStartFrequency_Type())
cfgChannelExclusionStartFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelExclusionStartFrequency.setStatus(_A)
if mibBuilder.loadTexts:cfgChannelExclusionStartFrequency.setUnits(_H)
class _CfgChannelExclusionStopFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CfgChannelExclusionStopFrequency_Type.__name__=_C
_CfgChannelExclusionStopFrequency_Object=MibTableColumn
cfgChannelExclusionStopFrequency=_CfgChannelExclusionStopFrequency_Object((1,3,6,1,4,1,5802,999999,2,18,2,1,4),_CfgChannelExclusionStopFrequency_Type())
cfgChannelExclusionStopFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelExclusionStopFrequency.setStatus(_A)
if mibBuilder.loadTexts:cfgChannelExclusionStopFrequency.setUnits(_H)
_CfgChannelInclusionTable_Object=MibTable
cfgChannelInclusionTable=_CfgChannelInclusionTable_Object((1,3,6,1,4,1,5802,999999,2,18,3))
if mibBuilder.loadTexts:cfgChannelInclusionTable.setStatus(_A)
_CfgChannelInclusionEntry_Object=MibTableRow
cfgChannelInclusionEntry=_CfgChannelInclusionEntry_Object((1,3,6,1,4,1,5802,999999,2,18,3,1))
cfgChannelInclusionEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:cfgChannelInclusionEntry.setStatus(_A)
_CfgChannelInclusionIndex_Type=Integer32
_CfgChannelInclusionIndex_Object=MibTableColumn
cfgChannelInclusionIndex=_CfgChannelInclusionIndex_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,1),_CfgChannelInclusionIndex_Type())
cfgChannelInclusionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgChannelInclusionIndex.setStatus(_A)
_CfgChannelInclusionStatus_Type=RowStatus
_CfgChannelInclusionStatus_Object=MibTableColumn
cfgChannelInclusionStatus=_CfgChannelInclusionStatus_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,2),_CfgChannelInclusionStatus_Type())
cfgChannelInclusionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelInclusionStatus.setStatus(_A)
class _CfgChannelInclusionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('linear-qam',0),('docsis',1),('sdv',2),('vod',3),(_a,4),('oob',5)))
_CfgChannelInclusionType_Type.__name__=_C
_CfgChannelInclusionType_Object=MibTableColumn
cfgChannelInclusionType=_CfgChannelInclusionType_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,3),_CfgChannelInclusionType_Type())
cfgChannelInclusionType.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelInclusionType.setStatus(_A)
class _CfgChannelInclusionModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),('qam64',1),(_b,2),(_c,3),(_d,4),(_e,5)))
_CfgChannelInclusionModulation_Type.__name__=_C
_CfgChannelInclusionModulation_Object=MibTableColumn
cfgChannelInclusionModulation=_CfgChannelInclusionModulation_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,4),_CfgChannelInclusionModulation_Type())
cfgChannelInclusionModulation.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelInclusionModulation.setStatus(_A)
class _CfgChannelInclusionBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_CfgChannelInclusionBandwidth_Type.__name__=_C
_CfgChannelInclusionBandwidth_Object=MibTableColumn
cfgChannelInclusionBandwidth=_CfgChannelInclusionBandwidth_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,5),_CfgChannelInclusionBandwidth_Type())
cfgChannelInclusionBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelInclusionBandwidth.setStatus(_A)
class _CfgChannelInclusionStartFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CfgChannelInclusionStartFrequency_Type.__name__=_C
_CfgChannelInclusionStartFrequency_Object=MibTableColumn
cfgChannelInclusionStartFrequency=_CfgChannelInclusionStartFrequency_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,6),_CfgChannelInclusionStartFrequency_Type())
cfgChannelInclusionStartFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelInclusionStartFrequency.setStatus(_A)
if mibBuilder.loadTexts:cfgChannelInclusionStartFrequency.setUnits(_H)
class _CfgChannelInclusionStopFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CfgChannelInclusionStopFrequency_Type.__name__=_C
_CfgChannelInclusionStopFrequency_Object=MibTableColumn
cfgChannelInclusionStopFrequency=_CfgChannelInclusionStopFrequency_Object((1,3,6,1,4,1,5802,999999,2,18,3,1,7),_CfgChannelInclusionStopFrequency_Type())
cfgChannelInclusionStopFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:cfgChannelInclusionStopFrequency.setStatus(_A)
if mibBuilder.loadTexts:cfgChannelInclusionStopFrequency.setUnits(_H)
_CfgPropertyProvisionning_ObjectIdentity=ObjectIdentity
cfgPropertyProvisionning=_CfgPropertyProvisionning_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,19))
_CfgPropertyProvisionningRunNow_Type=TruthValue
_CfgPropertyProvisionningRunNow_Object=MibScalar
cfgPropertyProvisionningRunNow=_CfgPropertyProvisionningRunNow_Object((1,3,6,1,4,1,5802,999999,2,19,1),_CfgPropertyProvisionningRunNow_Type())
cfgPropertyProvisionningRunNow.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPropertyProvisionningRunNow.setStatus(_A)
_CfgInputPowerBaselineResultTable_Object=MibTable
cfgInputPowerBaselineResultTable=_CfgInputPowerBaselineResultTable_Object((1,3,6,1,4,1,5802,999999,2,19,2))
if mibBuilder.loadTexts:cfgInputPowerBaselineResultTable.setStatus(_A)
_CfgInputPowerBaselineResultEntry_Object=MibTableRow
cfgInputPowerBaselineResultEntry=_CfgInputPowerBaselineResultEntry_Object((1,3,6,1,4,1,5802,999999,2,19,2,1))
cfgInputPowerBaselineResultEntry.setIndexNames((0,_G,_f))
if mibBuilder.loadTexts:cfgInputPowerBaselineResultEntry.setStatus(_A)
class _CfgInputPowerBaseLineChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CfgInputPowerBaseLineChannelIndex_Type.__name__=_C
_CfgInputPowerBaseLineChannelIndex_Object=MibTableColumn
cfgInputPowerBaseLineChannelIndex=_CfgInputPowerBaseLineChannelIndex_Object((1,3,6,1,4,1,5802,999999,2,19,2,1,1),_CfgInputPowerBaseLineChannelIndex_Type())
cfgInputPowerBaseLineChannelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelIndex.setStatus(_A)
class _CfgInputPowerBaseLineChannelFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CfgInputPowerBaseLineChannelFrequency_Type.__name__=_C
_CfgInputPowerBaseLineChannelFrequency_Object=MibTableColumn
cfgInputPowerBaseLineChannelFrequency=_CfgInputPowerBaseLineChannelFrequency_Object((1,3,6,1,4,1,5802,999999,2,19,2,1,2),_CfgInputPowerBaseLineChannelFrequency_Type())
cfgInputPowerBaseLineChannelFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelFrequency.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelFrequency.setUnits(_H)
_CfgInputPowerBaseLineChannelPower_Type=TenthdBmV
_CfgInputPowerBaseLineChannelPower_Object=MibTableColumn
cfgInputPowerBaseLineChannelPower=_CfgInputPowerBaseLineChannelPower_Object((1,3,6,1,4,1,5802,999999,2,19,2,1,3),_CfgInputPowerBaseLineChannelPower_Type())
cfgInputPowerBaseLineChannelPower.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelPower.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelPower.setUnits(_J)
_CfgInputPowerBaseLineChannelMER_Type=TenthdB
_CfgInputPowerBaseLineChannelMER_Object=MibTableColumn
cfgInputPowerBaseLineChannelMER=_CfgInputPowerBaseLineChannelMER_Object((1,3,6,1,4,1,5802,999999,2,19,2,1,4),_CfgInputPowerBaseLineChannelMER_Type())
cfgInputPowerBaseLineChannelMER.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelMER.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelMER.setUnits(_K)
class _CfgInputPowerBaseLineChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('success',1),('error',2)))
_CfgInputPowerBaseLineChannelStatus_Type.__name__=_C
_CfgInputPowerBaseLineChannelStatus_Object=MibTableColumn
cfgInputPowerBaseLineChannelStatus=_CfgInputPowerBaseLineChannelStatus_Object((1,3,6,1,4,1,5802,999999,2,19,2,1,5),_CfgInputPowerBaseLineChannelStatus_Type())
cfgInputPowerBaseLineChannelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgInputPowerBaseLineChannelStatus.setStatus(_A)
_CfgInputPowerRules_ObjectIdentity=ObjectIdentity
cfgInputPowerRules=_CfgInputPowerRules_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,19,3))
class _CfgInputPowerRuleHIHI_Type(TenthdBmV):defaultValue=6
_CfgInputPowerRuleHIHI_Type.__name__=_I
_CfgInputPowerRuleHIHI_Object=MibScalar
cfgInputPowerRuleHIHI=_CfgInputPowerRuleHIHI_Object((1,3,6,1,4,1,5802,999999,2,19,3,1),_CfgInputPowerRuleHIHI_Type())
cfgInputPowerRuleHIHI.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgInputPowerRuleHIHI.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerRuleHIHI.setUnits(_J)
class _CfgInputPowerRuleHI_Type(TenthdBmV):defaultValue=3
_CfgInputPowerRuleHI_Type.__name__=_I
_CfgInputPowerRuleHI_Object=MibScalar
cfgInputPowerRuleHI=_CfgInputPowerRuleHI_Object((1,3,6,1,4,1,5802,999999,2,19,3,2),_CfgInputPowerRuleHI_Type())
cfgInputPowerRuleHI.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgInputPowerRuleHI.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerRuleHI.setUnits(_J)
class _CfgInputPowerRuleLO_Type(TenthdBmV):defaultValue=-3
_CfgInputPowerRuleLO_Type.__name__=_I
_CfgInputPowerRuleLO_Object=MibScalar
cfgInputPowerRuleLO=_CfgInputPowerRuleLO_Object((1,3,6,1,4,1,5802,999999,2,19,3,3),_CfgInputPowerRuleLO_Type())
cfgInputPowerRuleLO.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgInputPowerRuleLO.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerRuleLO.setUnits(_J)
class _CfgInputPowerRuleLOLO_Type(TenthdBmV):defaultValue=-6
_CfgInputPowerRuleLOLO_Type.__name__=_I
_CfgInputPowerRuleLOLO_Object=MibScalar
cfgInputPowerRuleLOLO=_CfgInputPowerRuleLOLO_Object((1,3,6,1,4,1,5802,999999,2,19,3,4),_CfgInputPowerRuleLOLO_Type())
cfgInputPowerRuleLOLO.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgInputPowerRuleLOLO.setStatus(_A)
if mibBuilder.loadTexts:cfgInputPowerRuleLOLO.setUnits(_J)
_CfgBERRules_ObjectIdentity=ObjectIdentity
cfgBERRules=_CfgBERRules_ObjectIdentity((1,3,6,1,4,1,5802,999999,2,19,4))
_CfgPreFECBERRulesHIHI_Type=Integer32
_CfgPreFECBERRulesHIHI_Object=MibScalar
cfgPreFECBERRulesHIHI=_CfgPreFECBERRulesHIHI_Object((1,3,6,1,4,1,5802,999999,2,19,4,2),_CfgPreFECBERRulesHIHI_Type())
cfgPreFECBERRulesHIHI.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPreFECBERRulesHIHI.setStatus(_A)
if mibBuilder.loadTexts:cfgPreFECBERRulesHIHI.setUnits(_N)
_CfgPreFECBERRulesHI_Type=Integer32
_CfgPreFECBERRulesHI_Object=MibScalar
cfgPreFECBERRulesHI=_CfgPreFECBERRulesHI_Object((1,3,6,1,4,1,5802,999999,2,19,4,3),_CfgPreFECBERRulesHI_Type())
cfgPreFECBERRulesHI.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPreFECBERRulesHI.setStatus(_A)
if mibBuilder.loadTexts:cfgPreFECBERRulesHI.setUnits(_N)
_CfgPostFECBERRulesHIHI_Type=Integer32
_CfgPostFECBERRulesHIHI_Object=MibScalar
cfgPostFECBERRulesHIHI=_CfgPostFECBERRulesHIHI_Object((1,3,6,1,4,1,5802,999999,2,19,4,4),_CfgPostFECBERRulesHIHI_Type())
cfgPostFECBERRulesHIHI.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPostFECBERRulesHIHI.setStatus(_A)
if mibBuilder.loadTexts:cfgPostFECBERRulesHIHI.setUnits(_N)
_CfgPostFECBERRulesHI_Type=Integer32
_CfgPostFECBERRulesHI_Object=MibScalar
cfgPostFECBERRulesHI=_CfgPostFECBERRulesHI_Object((1,3,6,1,4,1,5802,999999,2,19,4,5),_CfgPostFECBERRulesHI_Type())
cfgPostFECBERRulesHI.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPostFECBERRulesHI.setStatus(_A)
if mibBuilder.loadTexts:cfgPostFECBERRulesHI.setUnits(_N)
_CfgMERRulesTable_Object=MibTable
cfgMERRulesTable=_CfgMERRulesTable_Object((1,3,6,1,4,1,5802,999999,2,19,5))
if mibBuilder.loadTexts:cfgMERRulesTable.setStatus(_A)
_CfgMERRulesEntry_Object=MibTableRow
cfgMERRulesEntry=_CfgMERRulesEntry_Object((1,3,6,1,4,1,5802,999999,2,19,5,1))
cfgMERRulesEntry.setIndexNames((0,_G,_g))
if mibBuilder.loadTexts:cfgMERRulesEntry.setStatus(_A)
class _CfgMERRulesTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('qam64',1),(_b,2),(_c,3),(_d,4),(_e,5)))
_CfgMERRulesTableIndex_Type.__name__=_C
_CfgMERRulesTableIndex_Object=MibTableColumn
cfgMERRulesTableIndex=_CfgMERRulesTableIndex_Object((1,3,6,1,4,1,5802,999999,2,19,5,1,1),_CfgMERRulesTableIndex_Type())
cfgMERRulesTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cfgMERRulesTableIndex.setStatus(_A)
class _CfgMERRulesLO_Type(TenthdB):defaultValue=-3
_CfgMERRulesLO_Type.__name__=_K
_CfgMERRulesLO_Object=MibTableColumn
cfgMERRulesLO=_CfgMERRulesLO_Object((1,3,6,1,4,1,5802,999999,2,19,5,1,2),_CfgMERRulesLO_Type())
cfgMERRulesLO.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgMERRulesLO.setStatus(_A)
if mibBuilder.loadTexts:cfgMERRulesLO.setUnits('dB')
class _CfgMERRulesLOLO_Type(TenthdB):defaultValue=-6
_CfgMERRulesLOLO_Type.__name__=_K
_CfgMERRulesLOLO_Object=MibTableColumn
cfgMERRulesLOLO=_CfgMERRulesLOLO_Object((1,3,6,1,4,1,5802,999999,2,19,5,1,3),_CfgMERRulesLOLO_Type())
cfgMERRulesLOLO.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgMERRulesLOLO.setStatus(_A)
if mibBuilder.loadTexts:cfgMERRulesLOLO.setUnits('dB')
mibBuilder.exportSymbols(_G,**{'dmonCommonGroup':dmonCommonGroup,'dmonGpsPosition':dmonGpsPosition,'dmonOperation':dmonOperation,'dmonOperationMode':dmonOperationMode,'dmonOperationStatus':dmonOperationStatus,'dmonOperationAutoScanTask':dmonOperationAutoScanTask,'dmonVideoModeTable':dmonVideoModeTable,'dmonVideoModeChannelBandwidth':dmonVideoModeChannelBandwidth,'dmonParkModeControlTable':dmonParkModeControlTable,'dmonParkModeControlEntry':dmonParkModeControlEntry,_V:dmonParkModeReceiverID,'dmonParkModeReceiverStatus':dmonParkModeReceiverStatus,'dmonParkModeReceiverParkingFrequency':dmonParkModeReceiverParkingFrequency,'dmonParkModeReceiverSymbolRate':dmonParkModeReceiverSymbolRate,'dmonParkModeReceiverQamType':dmonParkModeReceiverQamType,'dmonParkModeReceiverInverseMode':dmonParkModeReceiverInverseMode,'dmonParkModeDwellTime':dmonParkModeDwellTime,'dmonParkModeReceiverControl':dmonParkModeReceiverControl,'dmonLocalAccess':dmonLocalAccess,'dmonDwellingTIme':dmonDwellingTIme,'dmonLanguageCharset':dmonLanguageCharset,'dmonChannelPlan':dmonChannelPlan,'dmonFixedIncTable':dmonFixedIncTable,'dmonFixedIncStartFreq':dmonFixedIncStartFreq,'dmonFixedIncFreqStep':dmonFixedIncFreqStep,'dmonFixedIncEndFreq':dmonFixedIncEndFreq,'dmonFixedIncSymbolRate':dmonFixedIncSymbolRate,'dmonFixedIncInverseMode':dmonFixedIncInverseMode,'dmonFixedIncQamType':dmonFixedIncQamType,'dmonUserFreqTable':dmonUserFreqTable,'dmonUserFreqEntry':dmonUserFreqEntry,_X:dmonUserFreqProvIndex,'dmonUserFreqProvStatus':dmonUserFreqProvStatus,'dmonUserFreqProvFrequency':dmonUserFreqProvFrequency,'dmonUserFreqProvModulation':dmonUserFreqProvModulation,'dmonUserFreqProvSymbolRate':dmonUserFreqProvSymbolRate,'dmonUserFreqProvInversion':dmonUserFreqProvInversion,'cfgChannelMap':cfgChannelMap,'cfgChannelMapSource':cfgChannelMapSource,'cfgChannelExclusionTable':cfgChannelExclusionTable,'cfgChannelExclusionEntry':cfgChannelExclusionEntry,_Y:cfgChannelExclusionIndex,'cfgChannelExclusionStatus':cfgChannelExclusionStatus,'cfgChannelExclusionStartFrequency':cfgChannelExclusionStartFrequency,'cfgChannelExclusionStopFrequency':cfgChannelExclusionStopFrequency,'cfgChannelInclusionTable':cfgChannelInclusionTable,'cfgChannelInclusionEntry':cfgChannelInclusionEntry,_Z:cfgChannelInclusionIndex,'cfgChannelInclusionStatus':cfgChannelInclusionStatus,'cfgChannelInclusionType':cfgChannelInclusionType,'cfgChannelInclusionModulation':cfgChannelInclusionModulation,'cfgChannelInclusionBandwidth':cfgChannelInclusionBandwidth,'cfgChannelInclusionStartFrequency':cfgChannelInclusionStartFrequency,'cfgChannelInclusionStopFrequency':cfgChannelInclusionStopFrequency,'cfgPropertyProvisionning':cfgPropertyProvisionning,'cfgPropertyProvisionningRunNow':cfgPropertyProvisionningRunNow,'cfgInputPowerBaselineResultTable':cfgInputPowerBaselineResultTable,'cfgInputPowerBaselineResultEntry':cfgInputPowerBaselineResultEntry,_f:cfgInputPowerBaseLineChannelIndex,'cfgInputPowerBaseLineChannelFrequency':cfgInputPowerBaseLineChannelFrequency,'cfgInputPowerBaseLineChannelPower':cfgInputPowerBaseLineChannelPower,'cfgInputPowerBaseLineChannelMER':cfgInputPowerBaseLineChannelMER,'cfgInputPowerBaseLineChannelStatus':cfgInputPowerBaseLineChannelStatus,'cfgInputPowerRules':cfgInputPowerRules,'cfgInputPowerRuleHIHI':cfgInputPowerRuleHIHI,'cfgInputPowerRuleHI':cfgInputPowerRuleHI,'cfgInputPowerRuleLO':cfgInputPowerRuleLO,'cfgInputPowerRuleLOLO':cfgInputPowerRuleLOLO,'cfgBERRules':cfgBERRules,'cfgPreFECBERRulesHIHI':cfgPreFECBERRulesHIHI,'cfgPreFECBERRulesHI':cfgPreFECBERRulesHI,'cfgPostFECBERRulesHIHI':cfgPostFECBERRulesHIHI,'cfgPostFECBERRulesHI':cfgPostFECBERRulesHI,'cfgMERRulesTable':cfgMERRulesTable,'cfgMERRulesEntry':cfgMERRulesEntry,_g:cfgMERRulesTableIndex,'cfgMERRulesLO':cfgMERRulesLO,'cfgMERRulesLOLO':cfgMERRulesLOLO})