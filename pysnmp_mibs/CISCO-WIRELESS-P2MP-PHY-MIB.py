_AV='p2mpRadioAntennaGroup'
_AU='p2mpRadioHeGroup'
_AT='p2mpRadioSuGroup'
_AS='p2mpCommonTestGroup'
_AR='p2mpCommonRfGroup'
_AQ='p2mpCommonRadioGroup'
_AP='p2mpAntennaPolarization'
_AO='p2mpAntennaGain'
_AN='p2mpAntennaDescr'
_AM='p2mpAntennaType'
_AL='p2mpAntennaYDim'
_AK='p2mpAntennaXDim'
_AJ='p2mpRfResource'
_AI='p2mpHeTrapEnable'
_AH='p2mpHeIfOutFreq'
_AG='p2mpHeIfInpFreq'
_AF='p2mpHeAlcNumMiniSlots'
_AE='p2mpHeAlcInterval'
_AD='p2mpHeAlcEnable'
_AC='p2mpSuMeasuredPower'
_AB='p2mpSuCenterFrequency'
_AA='p2mpSuTxMuteDuration'
_A9='p2mpSuTxMuteEnable'
_A8='p2mpLocalLoopbackChannel'
_A7='p2mpLocalLoopbackAntenna'
_A6='p2mpLocalLoopbackMode'
_A5='p2mpDuplexerBurnDate'
_A4='p2mpDuplexerTxInsertionLoss'
_A3='p2mpDuplexerReceivePassband'
_A2='p2mpDuplexerHiPassbandMaxFreq'
_A1='p2mpDuplexerHiPassbandMinFreq'
_A0='p2mpDuplexerLoPassbandMaxFreq'
_z='p2mpDuplexerLoPassbandMinFreq'
_y='p2mpDuplexerRF'
_x='p2mpRfLoopbackSupported'
_w='p2mpMaxTxPower'
_v='p2mpMinTxPower'
_u='p2mpRxFreqRangeMax'
_t='p2mpRxFreqRangeMin'
_s='p2mpTxFreqRangeMax'
_r='p2mpTxFreqRangeMin'
_q='p2mpRfOpMode'
_p='p2mpLedState'
_o='p2mpLedType'
_n='p2mpCommonTrapEnable'
_m='p2mpClockRefExt'
_l='p2mpDenyService'
_k='p2mpCableLossDiversity'
_j='p2mpCableLoss'
_i='p2mpDiversityAntennaPresent'
_h='p2mpSelfTest'
_g='p2mpSuPowerScanIndex'
_f='p2mpLedIndex'
_e='Inches'
_d='p2mpAntennaIndex'
_c='p2mpDuplexerIndex'
_b='p2mpRfIndex'
_a='entPhysicalIndex'
_Z='ENTITY-MIB'
_Y='p2mpHeIfRefOscState'
_X='p2mpHeIfRxOscState'
_W='p2mpHeIfTxOscState'
_V='p2mpRfStatus'
_U='p2mpRfSupplyVoltageState'
_T='p2mpRfTemperature'
_S='p2mpRfRxOscState'
_R='p2mpRfTxOscState'
_Q='p2mpLastPhyFailureReason'
_P='p2mpLastPhyFailureType'
_O='dBm'
_N='TruthValue'
_M='p2mpRfType'
_L='MHz'
_K='DisplayString'
_J='not-accessible'
_I='KHz'
_H='ifIndex'
_G='IF-MIB'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='CISCO-WIRELESS-P2MP-PHY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned32,=mibBuilder.importSymbols('CISCO-TC',_F)
CwrOscState,CwrRfFreqRange,CwrRfType=mibBuilder.importSymbols('CISCO-WIRELESS-TC-MIB','CwrOscState','CwrRfFreqRange','CwrRfType')
entPhysicalIndex,=mibBuilder.importSymbols(_Z,_a)
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention',_N)
ciscoWirelessPhyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,170))
if mibBuilder.loadTexts:ciscoWirelessPhyMIB.setRevisions(('2000-10-22 19:10','2000-10-04 19:10','2000-07-21 19:10'))
_P2mpRadioObjects_ObjectIdentity=ObjectIdentity
p2mpRadioObjects=_P2mpRadioObjects_ObjectIdentity((1,3,6,1,4,1,9,9,170,1))
_P2mpRadioBaseObjects_ObjectIdentity=ObjectIdentity
p2mpRadioBaseObjects=_P2mpRadioBaseObjects_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,1))
_P2mpPhyConfigGroup_ObjectIdentity=ObjectIdentity
p2mpPhyConfigGroup=_P2mpPhyConfigGroup_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,1,1))
_P2mpRadioPhyTable_Object=MibTable
p2mpRadioPhyTable=_P2mpRadioPhyTable_Object((1,3,6,1,4,1,9,9,170,1,1,1,1))
if mibBuilder.loadTexts:p2mpRadioPhyTable.setStatus(_A)
_P2mpRadioPhyEntry_Object=MibTableRow
p2mpRadioPhyEntry=_P2mpRadioPhyEntry_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1))
p2mpRadioPhyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:p2mpRadioPhyEntry.setStatus(_A)
_P2mpSelfTest_Type=TruthValue
_P2mpSelfTest_Object=MibTableColumn
p2mpSelfTest=_P2mpSelfTest_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,1),_P2mpSelfTest_Type())
p2mpSelfTest.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpSelfTest.setStatus(_A)
_P2mpDiversityAntennaPresent_Type=TruthValue
_P2mpDiversityAntennaPresent_Object=MibTableColumn
p2mpDiversityAntennaPresent=_P2mpDiversityAntennaPresent_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,2),_P2mpDiversityAntennaPresent_Type())
p2mpDiversityAntennaPresent.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpDiversityAntennaPresent.setStatus(_A)
class _P2mpCableLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_P2mpCableLoss_Type.__name__=_F
_P2mpCableLoss_Object=MibTableColumn
p2mpCableLoss=_P2mpCableLoss_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,3),_P2mpCableLoss_Type())
p2mpCableLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpCableLoss.setStatus(_A)
if mibBuilder.loadTexts:p2mpCableLoss.setUnits('dB')
class _P2mpCableLossDiversity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_P2mpCableLossDiversity_Type.__name__=_F
_P2mpCableLossDiversity_Object=MibTableColumn
p2mpCableLossDiversity=_P2mpCableLossDiversity_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,4),_P2mpCableLossDiversity_Type())
p2mpCableLossDiversity.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpCableLossDiversity.setStatus(_A)
if mibBuilder.loadTexts:p2mpCableLossDiversity.setUnits('dB')
_P2mpDenyService_Type=TruthValue
_P2mpDenyService_Object=MibTableColumn
p2mpDenyService=_P2mpDenyService_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,5),_P2mpDenyService_Type())
p2mpDenyService.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDenyService.setStatus(_A)
_P2mpClockRefExt_Type=TruthValue
_P2mpClockRefExt_Object=MibTableColumn
p2mpClockRefExt=_P2mpClockRefExt_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,6),_P2mpClockRefExt_Type())
p2mpClockRefExt.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpClockRefExt.setStatus(_A)
class _P2mpCommonTrapEnable_Type(TruthValue):defaultValue=1
_P2mpCommonTrapEnable_Type.__name__=_N
_P2mpCommonTrapEnable_Object=MibTableColumn
p2mpCommonTrapEnable=_P2mpCommonTrapEnable_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,7),_P2mpCommonTrapEnable_Type())
p2mpCommonTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpCommonTrapEnable.setStatus(_A)
class _P2mpLastPhyFailureType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('p2mpHwConfigUnsupported',2),('p2mpHwConfigMismatch',3),('p2mpHwInitFailure',4),('p2mpHostIfCommLinkError',5),('p2mpAutoCableCompFailure',6)))
_P2mpLastPhyFailureType_Type.__name__=_E
_P2mpLastPhyFailureType_Object=MibTableColumn
p2mpLastPhyFailureType=_P2mpLastPhyFailureType_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,8),_P2mpLastPhyFailureType_Type())
p2mpLastPhyFailureType.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpLastPhyFailureType.setStatus(_A)
class _P2mpLastPhyFailureReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_P2mpLastPhyFailureReason_Type.__name__=_K
_P2mpLastPhyFailureReason_Object=MibTableColumn
p2mpLastPhyFailureReason=_P2mpLastPhyFailureReason_Object((1,3,6,1,4,1,9,9,170,1,1,1,1,1,9),_P2mpLastPhyFailureReason_Type())
p2mpLastPhyFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpLastPhyFailureReason.setStatus(_A)
_P2mpFreqResourceGroup_ObjectIdentity=ObjectIdentity
p2mpFreqResourceGroup=_P2mpFreqResourceGroup_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,1,2))
_P2mpRfTable_Object=MibTable
p2mpRfTable=_P2mpRfTable_Object((1,3,6,1,4,1,9,9,170,1,1,2,1))
if mibBuilder.loadTexts:p2mpRfTable.setStatus(_A)
_P2mpRfEntry_Object=MibTableRow
p2mpRfEntry=_P2mpRfEntry_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1))
p2mpRfEntry.setIndexNames((0,_G,_H),(0,_B,_b))
if mibBuilder.loadTexts:p2mpRfEntry.setStatus(_A)
class _P2mpRfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_P2mpRfIndex_Type.__name__=_E
_P2mpRfIndex_Object=MibTableColumn
p2mpRfIndex=_P2mpRfIndex_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,1),_P2mpRfIndex_Type())
p2mpRfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpRfIndex.setStatus(_A)
_P2mpRfType_Type=CwrRfType
_P2mpRfType_Object=MibTableColumn
p2mpRfType=_P2mpRfType_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,2),_P2mpRfType_Type())
p2mpRfType.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfType.setStatus(_A)
class _P2mpRfOpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('receiveOnly',1),('transmitOnly',2),('transmitAndReceive',3)))
_P2mpRfOpMode_Type.__name__=_E
_P2mpRfOpMode_Object=MibTableColumn
p2mpRfOpMode=_P2mpRfOpMode_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,3),_P2mpRfOpMode_Type())
p2mpRfOpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfOpMode.setStatus(_A)
_P2mpTxFreqRangeMin_Type=CwrRfFreqRange
_P2mpTxFreqRangeMin_Object=MibTableColumn
p2mpTxFreqRangeMin=_P2mpTxFreqRangeMin_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,4),_P2mpTxFreqRangeMin_Type())
p2mpTxFreqRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpTxFreqRangeMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpTxFreqRangeMin.setUnits(_I)
_P2mpTxFreqRangeMax_Type=CwrRfFreqRange
_P2mpTxFreqRangeMax_Object=MibTableColumn
p2mpTxFreqRangeMax=_P2mpTxFreqRangeMax_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,5),_P2mpTxFreqRangeMax_Type())
p2mpTxFreqRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpTxFreqRangeMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpTxFreqRangeMax.setUnits(_I)
_P2mpRxFreqRangeMin_Type=CwrRfFreqRange
_P2mpRxFreqRangeMin_Object=MibTableColumn
p2mpRxFreqRangeMin=_P2mpRxFreqRangeMin_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,6),_P2mpRxFreqRangeMin_Type())
p2mpRxFreqRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRxFreqRangeMin.setStatus(_A)
if mibBuilder.loadTexts:p2mpRxFreqRangeMin.setUnits(_I)
_P2mpRxFreqRangeMax_Type=CwrRfFreqRange
_P2mpRxFreqRangeMax_Object=MibTableColumn
p2mpRxFreqRangeMax=_P2mpRxFreqRangeMax_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,7),_P2mpRxFreqRangeMax_Type())
p2mpRxFreqRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRxFreqRangeMax.setStatus(_A)
if mibBuilder.loadTexts:p2mpRxFreqRangeMax.setUnits(_I)
class _P2mpMinTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,50))
_P2mpMinTxPower_Type.__name__=_E
_P2mpMinTxPower_Object=MibTableColumn
p2mpMinTxPower=_P2mpMinTxPower_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,8),_P2mpMinTxPower_Type())
p2mpMinTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpMinTxPower.setStatus(_A)
if mibBuilder.loadTexts:p2mpMinTxPower.setUnits(_O)
class _P2mpMaxTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-80,50))
_P2mpMaxTxPower_Type.__name__=_E
_P2mpMaxTxPower_Object=MibTableColumn
p2mpMaxTxPower=_P2mpMaxTxPower_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,9),_P2mpMaxTxPower_Type())
p2mpMaxTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpMaxTxPower.setStatus(_A)
if mibBuilder.loadTexts:p2mpMaxTxPower.setUnits(_O)
class _P2mpRfTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-40,100))
_P2mpRfTemperature_Type.__name__=_E
_P2mpRfTemperature_Object=MibTableColumn
p2mpRfTemperature=_P2mpRfTemperature_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,10),_P2mpRfTemperature_Type())
p2mpRfTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfTemperature.setStatus(_A)
if mibBuilder.loadTexts:p2mpRfTemperature.setUnits('Degrees Centigrade')
_P2mpRfTxOscState_Type=CwrOscState
_P2mpRfTxOscState_Object=MibTableColumn
p2mpRfTxOscState=_P2mpRfTxOscState_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,11),_P2mpRfTxOscState_Type())
p2mpRfTxOscState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfTxOscState.setStatus(_A)
_P2mpRfRxOscState_Type=CwrOscState
_P2mpRfRxOscState_Object=MibTableColumn
p2mpRfRxOscState=_P2mpRfRxOscState_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,12),_P2mpRfRxOscState_Type())
p2mpRfRxOscState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfRxOscState.setStatus(_A)
class _P2mpRfSupplyVoltageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('withinSpecification',1),('outsideSpecification',2)))
_P2mpRfSupplyVoltageState_Type.__name__=_E
_P2mpRfSupplyVoltageState_Object=MibTableColumn
p2mpRfSupplyVoltageState=_P2mpRfSupplyVoltageState_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,13),_P2mpRfSupplyVoltageState_Type())
p2mpRfSupplyVoltageState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfSupplyVoltageState.setStatus(_A)
class _P2mpRfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_P2mpRfStatus_Type.__name__=_E
_P2mpRfStatus_Object=MibTableColumn
p2mpRfStatus=_P2mpRfStatus_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,14),_P2mpRfStatus_Type())
p2mpRfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfStatus.setStatus(_A)
_P2mpRfLoopbackSupported_Type=TruthValue
_P2mpRfLoopbackSupported_Object=MibTableColumn
p2mpRfLoopbackSupported=_P2mpRfLoopbackSupported_Object((1,3,6,1,4,1,9,9,170,1,1,2,1,1,15),_P2mpRfLoopbackSupported_Type())
p2mpRfLoopbackSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfLoopbackSupported.setStatus(_A)
_P2mpDuplexerTable_Object=MibTable
p2mpDuplexerTable=_P2mpDuplexerTable_Object((1,3,6,1,4,1,9,9,170,1,1,2,2))
if mibBuilder.loadTexts:p2mpDuplexerTable.setStatus(_A)
_P2mpDuplexerEntry_Object=MibTableRow
p2mpDuplexerEntry=_P2mpDuplexerEntry_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1))
p2mpDuplexerEntry.setIndexNames((0,_G,_H),(0,_B,_c))
if mibBuilder.loadTexts:p2mpDuplexerEntry.setStatus(_A)
class _P2mpDuplexerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_P2mpDuplexerIndex_Type.__name__=_E
_P2mpDuplexerIndex_Object=MibTableColumn
p2mpDuplexerIndex=_P2mpDuplexerIndex_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,1),_P2mpDuplexerIndex_Type())
p2mpDuplexerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpDuplexerIndex.setStatus(_A)
_P2mpDuplexerRF_Type=CwrRfType
_P2mpDuplexerRF_Object=MibTableColumn
p2mpDuplexerRF=_P2mpDuplexerRF_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,2),_P2mpDuplexerRF_Type())
p2mpDuplexerRF.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerRF.setStatus(_A)
_P2mpDuplexerLoPassbandMinFreq_Type=CwrRfFreqRange
_P2mpDuplexerLoPassbandMinFreq_Object=MibTableColumn
p2mpDuplexerLoPassbandMinFreq=_P2mpDuplexerLoPassbandMinFreq_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,3),_P2mpDuplexerLoPassbandMinFreq_Type())
p2mpDuplexerLoPassbandMinFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerLoPassbandMinFreq.setStatus(_A)
if mibBuilder.loadTexts:p2mpDuplexerLoPassbandMinFreq.setUnits(_L)
_P2mpDuplexerLoPassbandMaxFreq_Type=CwrRfFreqRange
_P2mpDuplexerLoPassbandMaxFreq_Object=MibTableColumn
p2mpDuplexerLoPassbandMaxFreq=_P2mpDuplexerLoPassbandMaxFreq_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,4),_P2mpDuplexerLoPassbandMaxFreq_Type())
p2mpDuplexerLoPassbandMaxFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerLoPassbandMaxFreq.setStatus(_A)
if mibBuilder.loadTexts:p2mpDuplexerLoPassbandMaxFreq.setUnits(_L)
_P2mpDuplexerHiPassbandMinFreq_Type=CwrRfFreqRange
_P2mpDuplexerHiPassbandMinFreq_Object=MibTableColumn
p2mpDuplexerHiPassbandMinFreq=_P2mpDuplexerHiPassbandMinFreq_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,5),_P2mpDuplexerHiPassbandMinFreq_Type())
p2mpDuplexerHiPassbandMinFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerHiPassbandMinFreq.setStatus(_A)
if mibBuilder.loadTexts:p2mpDuplexerHiPassbandMinFreq.setUnits(_L)
_P2mpDuplexerHiPassbandMaxFreq_Type=CwrRfFreqRange
_P2mpDuplexerHiPassbandMaxFreq_Object=MibTableColumn
p2mpDuplexerHiPassbandMaxFreq=_P2mpDuplexerHiPassbandMaxFreq_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,6),_P2mpDuplexerHiPassbandMaxFreq_Type())
p2mpDuplexerHiPassbandMaxFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerHiPassbandMaxFreq.setStatus(_A)
if mibBuilder.loadTexts:p2mpDuplexerHiPassbandMaxFreq.setUnits(_L)
class _P2mpDuplexerReceivePassband_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loPassband',1),('hiPassband',2)))
_P2mpDuplexerReceivePassband_Type.__name__=_E
_P2mpDuplexerReceivePassband_Object=MibTableColumn
p2mpDuplexerReceivePassband=_P2mpDuplexerReceivePassband_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,7),_P2mpDuplexerReceivePassband_Type())
p2mpDuplexerReceivePassband.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerReceivePassband.setStatus(_A)
_P2mpDuplexerTxInsertionLoss_Type=Integer32
_P2mpDuplexerTxInsertionLoss_Object=MibTableColumn
p2mpDuplexerTxInsertionLoss=_P2mpDuplexerTxInsertionLoss_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,8),_P2mpDuplexerTxInsertionLoss_Type())
p2mpDuplexerTxInsertionLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerTxInsertionLoss.setStatus(_A)
if mibBuilder.loadTexts:p2mpDuplexerTxInsertionLoss.setUnits('dB')
_P2mpDuplexerBurnDate_Type=DisplayString
_P2mpDuplexerBurnDate_Object=MibTableColumn
p2mpDuplexerBurnDate=_P2mpDuplexerBurnDate_Object((1,3,6,1,4,1,9,9,170,1,1,2,2,1,9),_P2mpDuplexerBurnDate_Type())
p2mpDuplexerBurnDate.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpDuplexerBurnDate.setStatus(_A)
_P2mpAntennaTable_Object=MibTable
p2mpAntennaTable=_P2mpAntennaTable_Object((1,3,6,1,4,1,9,9,170,1,1,2,3))
if mibBuilder.loadTexts:p2mpAntennaTable.setStatus(_A)
_P2mpAntennaEntry_Object=MibTableRow
p2mpAntennaEntry=_P2mpAntennaEntry_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1))
p2mpAntennaEntry.setIndexNames((0,_G,_H),(0,_B,_d))
if mibBuilder.loadTexts:p2mpAntennaEntry.setStatus(_A)
_P2mpAntennaIndex_Type=Unsigned32
_P2mpAntennaIndex_Object=MibTableColumn
p2mpAntennaIndex=_P2mpAntennaIndex_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,1),_P2mpAntennaIndex_Type())
p2mpAntennaIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpAntennaIndex.setStatus(_A)
_P2mpRfResource_Type=CwrRfType
_P2mpRfResource_Object=MibTableColumn
p2mpRfResource=_P2mpRfResource_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,2),_P2mpRfResource_Type())
p2mpRfResource.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpRfResource.setStatus(_A)
class _P2mpAntennaXDim_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_P2mpAntennaXDim_Type.__name__=_F
_P2mpAntennaXDim_Object=MibTableColumn
p2mpAntennaXDim=_P2mpAntennaXDim_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,3),_P2mpAntennaXDim_Type())
p2mpAntennaXDim.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpAntennaXDim.setStatus(_A)
if mibBuilder.loadTexts:p2mpAntennaXDim.setUnits(_e)
class _P2mpAntennaYDim_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_P2mpAntennaYDim_Type.__name__=_F
_P2mpAntennaYDim_Object=MibTableColumn
p2mpAntennaYDim=_P2mpAntennaYDim_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,4),_P2mpAntennaYDim_Type())
p2mpAntennaYDim.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpAntennaYDim.setStatus(_A)
if mibBuilder.loadTexts:p2mpAntennaYDim.setUnits(_e)
class _P2mpAntennaType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_P2mpAntennaType_Type.__name__=_K
_P2mpAntennaType_Object=MibTableColumn
p2mpAntennaType=_P2mpAntennaType_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,5),_P2mpAntennaType_Type())
p2mpAntennaType.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpAntennaType.setStatus(_A)
class _P2mpAntennaDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_P2mpAntennaDescr_Type.__name__=_K
_P2mpAntennaDescr_Object=MibTableColumn
p2mpAntennaDescr=_P2mpAntennaDescr_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,6),_P2mpAntennaDescr_Type())
p2mpAntennaDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpAntennaDescr.setStatus(_A)
class _P2mpAntennaGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_P2mpAntennaGain_Type.__name__=_F
_P2mpAntennaGain_Object=MibTableColumn
p2mpAntennaGain=_P2mpAntennaGain_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,7),_P2mpAntennaGain_Type())
p2mpAntennaGain.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpAntennaGain.setStatus(_A)
if mibBuilder.loadTexts:p2mpAntennaGain.setUnits('dBi : decibel Isotropic')
class _P2mpAntennaPolarization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vertical',1),('horizontal',2)))
_P2mpAntennaPolarization_Type.__name__=_E
_P2mpAntennaPolarization_Object=MibTableColumn
p2mpAntennaPolarization=_P2mpAntennaPolarization_Object((1,3,6,1,4,1,9,9,170,1,1,2,3,1,8),_P2mpAntennaPolarization_Type())
p2mpAntennaPolarization.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpAntennaPolarization.setStatus(_A)
_P2mpRadioTestGroup_ObjectIdentity=ObjectIdentity
p2mpRadioTestGroup=_P2mpRadioTestGroup_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,1,3))
_P2mpLoopbackTable_Object=MibTable
p2mpLoopbackTable=_P2mpLoopbackTable_Object((1,3,6,1,4,1,9,9,170,1,1,3,1))
if mibBuilder.loadTexts:p2mpLoopbackTable.setStatus(_A)
_P2mpLoopbackEntry_Object=MibTableRow
p2mpLoopbackEntry=_P2mpLoopbackEntry_Object((1,3,6,1,4,1,9,9,170,1,1,3,1,1))
p2mpLoopbackEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:p2mpLoopbackEntry.setStatus(_A)
class _P2mpLocalLoopbackMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLoopback',1),('fir',2),('if',3),('rf',4)))
_P2mpLocalLoopbackMode_Type.__name__=_E
_P2mpLocalLoopbackMode_Object=MibTableColumn
p2mpLocalLoopbackMode=_P2mpLocalLoopbackMode_Object((1,3,6,1,4,1,9,9,170,1,1,3,1,1,1),_P2mpLocalLoopbackMode_Type())
p2mpLocalLoopbackMode.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpLocalLoopbackMode.setStatus(_A)
_P2mpLocalLoopbackAntenna_Type=CwrRfType
_P2mpLocalLoopbackAntenna_Object=MibTableColumn
p2mpLocalLoopbackAntenna=_P2mpLocalLoopbackAntenna_Object((1,3,6,1,4,1,9,9,170,1,1,3,1,1,2),_P2mpLocalLoopbackAntenna_Type())
p2mpLocalLoopbackAntenna.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpLocalLoopbackAntenna.setStatus(_A)
class _P2mpLocalLoopbackChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_P2mpLocalLoopbackChannel_Type.__name__=_F
_P2mpLocalLoopbackChannel_Object=MibTableColumn
p2mpLocalLoopbackChannel=_P2mpLocalLoopbackChannel_Object((1,3,6,1,4,1,9,9,170,1,1,3,1,1,3),_P2mpLocalLoopbackChannel_Type())
p2mpLocalLoopbackChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpLocalLoopbackChannel.setStatus(_A)
_P2mpLedGroup_ObjectIdentity=ObjectIdentity
p2mpLedGroup=_P2mpLedGroup_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,1,4))
_P2mpLedTable_Object=MibTable
p2mpLedTable=_P2mpLedTable_Object((1,3,6,1,4,1,9,9,170,1,1,4,1))
if mibBuilder.loadTexts:p2mpLedTable.setStatus(_A)
_P2mpLedEntry_Object=MibTableRow
p2mpLedEntry=_P2mpLedEntry_Object((1,3,6,1,4,1,9,9,170,1,1,4,1,1))
p2mpLedEntry.setIndexNames((0,_Z,_a),(0,_B,_f))
if mibBuilder.loadTexts:p2mpLedEntry.setStatus(_A)
class _P2mpLedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_P2mpLedIndex_Type.__name__=_E
_P2mpLedIndex_Object=MibTableColumn
p2mpLedIndex=_P2mpLedIndex_Object((1,3,6,1,4,1,9,9,170,1,1,4,1,1,1),_P2mpLedIndex_Type())
p2mpLedIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpLedIndex.setStatus(_A)
class _P2mpLedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('interfaceEnable',0),('majorAlarm',1),('minorAlarm',2),('outOfService',3),('carrier',4),('transmitData',5),('receiveData',6)))
_P2mpLedType_Type.__name__=_E
_P2mpLedType_Object=MibTableColumn
p2mpLedType=_P2mpLedType_Object((1,3,6,1,4,1,9,9,170,1,1,4,1,1,2),_P2mpLedType_Type())
p2mpLedType.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpLedType.setStatus(_A)
class _P2mpLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('green',1),('yellow',2)))
_P2mpLedState_Type.__name__=_E
_P2mpLedState_Object=MibTableColumn
p2mpLedState=_P2mpLedState_Object((1,3,6,1,4,1,9,9,170,1,1,4,1,1,3),_P2mpLedState_Type())
p2mpLedState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpLedState.setStatus(_A)
_P2mpRadioSuObjects_ObjectIdentity=ObjectIdentity
p2mpRadioSuObjects=_P2mpRadioSuObjects_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,2))
_P2mpSuRadioPhyTable_Object=MibTable
p2mpSuRadioPhyTable=_P2mpSuRadioPhyTable_Object((1,3,6,1,4,1,9,9,170,1,2,1))
if mibBuilder.loadTexts:p2mpSuRadioPhyTable.setStatus(_A)
_P2mpSuRadioPhyEntry_Object=MibTableRow
p2mpSuRadioPhyEntry=_P2mpSuRadioPhyEntry_Object((1,3,6,1,4,1,9,9,170,1,2,1,1))
p2mpSuRadioPhyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:p2mpSuRadioPhyEntry.setStatus(_A)
_P2mpSuTxMuteEnable_Type=TruthValue
_P2mpSuTxMuteEnable_Object=MibTableColumn
p2mpSuTxMuteEnable=_P2mpSuTxMuteEnable_Object((1,3,6,1,4,1,9,9,170,1,2,1,1,1),_P2mpSuTxMuteEnable_Type())
p2mpSuTxMuteEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuTxMuteEnable.setStatus(_A)
class _P2mpSuTxMuteDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_P2mpSuTxMuteDuration_Type.__name__=_F
_P2mpSuTxMuteDuration_Object=MibTableColumn
p2mpSuTxMuteDuration=_P2mpSuTxMuteDuration_Object((1,3,6,1,4,1,9,9,170,1,2,1,1,2),_P2mpSuTxMuteDuration_Type())
p2mpSuTxMuteDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpSuTxMuteDuration.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuTxMuteDuration.setUnits('minutes')
_P2mpSuPowerScanTable_Object=MibTable
p2mpSuPowerScanTable=_P2mpSuPowerScanTable_Object((1,3,6,1,4,1,9,9,170,1,2,2))
if mibBuilder.loadTexts:p2mpSuPowerScanTable.setStatus(_A)
_P2mpSuPowerScanEntry_Object=MibTableRow
p2mpSuPowerScanEntry=_P2mpSuPowerScanEntry_Object((1,3,6,1,4,1,9,9,170,1,2,2,1))
p2mpSuPowerScanEntry.setIndexNames((0,_G,_H),(0,_B,_g))
if mibBuilder.loadTexts:p2mpSuPowerScanEntry.setStatus(_A)
class _P2mpSuPowerScanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_P2mpSuPowerScanIndex_Type.__name__=_E
_P2mpSuPowerScanIndex_Object=MibTableColumn
p2mpSuPowerScanIndex=_P2mpSuPowerScanIndex_Object((1,3,6,1,4,1,9,9,170,1,2,2,1,1),_P2mpSuPowerScanIndex_Type())
p2mpSuPowerScanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:p2mpSuPowerScanIndex.setStatus(_A)
_P2mpSuCenterFrequency_Type=CwrRfFreqRange
_P2mpSuCenterFrequency_Object=MibTableColumn
p2mpSuCenterFrequency=_P2mpSuCenterFrequency_Object((1,3,6,1,4,1,9,9,170,1,2,2,1,2),_P2mpSuCenterFrequency_Type())
p2mpSuCenterFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuCenterFrequency.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuCenterFrequency.setUnits(_I)
class _P2mpSuMeasuredPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,50))
_P2mpSuMeasuredPower_Type.__name__=_E
_P2mpSuMeasuredPower_Object=MibTableColumn
p2mpSuMeasuredPower=_P2mpSuMeasuredPower_Object((1,3,6,1,4,1,9,9,170,1,2,2,1,3),_P2mpSuMeasuredPower_Type())
p2mpSuMeasuredPower.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpSuMeasuredPower.setStatus(_A)
if mibBuilder.loadTexts:p2mpSuMeasuredPower.setUnits(_O)
_P2mpRadioHeObjects_ObjectIdentity=ObjectIdentity
p2mpRadioHeObjects=_P2mpRadioHeObjects_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,3))
_P2mpHeAlcTable_Object=MibTable
p2mpHeAlcTable=_P2mpHeAlcTable_Object((1,3,6,1,4,1,9,9,170,1,3,1))
if mibBuilder.loadTexts:p2mpHeAlcTable.setStatus(_A)
_P2mpHeAlcEntry_Object=MibTableRow
p2mpHeAlcEntry=_P2mpHeAlcEntry_Object((1,3,6,1,4,1,9,9,170,1,3,1,1))
p2mpHeAlcEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:p2mpHeAlcEntry.setStatus(_A)
_P2mpHeAlcEnable_Type=TruthValue
_P2mpHeAlcEnable_Object=MibTableColumn
p2mpHeAlcEnable=_P2mpHeAlcEnable_Object((1,3,6,1,4,1,9,9,170,1,3,1,1,1),_P2mpHeAlcEnable_Type())
p2mpHeAlcEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpHeAlcEnable.setStatus(_A)
class _P2mpHeAlcInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,1024))
_P2mpHeAlcInterval_Type.__name__=_F
_P2mpHeAlcInterval_Object=MibTableColumn
p2mpHeAlcInterval=_P2mpHeAlcInterval_Object((1,3,6,1,4,1,9,9,170,1,3,1,1,2),_P2mpHeAlcInterval_Type())
p2mpHeAlcInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpHeAlcInterval.setStatus(_A)
if mibBuilder.loadTexts:p2mpHeAlcInterval.setUnits('milliseconds')
class _P2mpHeAlcNumMiniSlots_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_P2mpHeAlcNumMiniSlots_Type.__name__=_F
_P2mpHeAlcNumMiniSlots_Object=MibTableColumn
p2mpHeAlcNumMiniSlots=_P2mpHeAlcNumMiniSlots_Object((1,3,6,1,4,1,9,9,170,1,3,1,1,3),_P2mpHeAlcNumMiniSlots_Type())
p2mpHeAlcNumMiniSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpHeAlcNumMiniSlots.setStatus(_A)
_P2mpHeIntFreqTable_Object=MibTable
p2mpHeIntFreqTable=_P2mpHeIntFreqTable_Object((1,3,6,1,4,1,9,9,170,1,3,2))
if mibBuilder.loadTexts:p2mpHeIntFreqTable.setStatus(_A)
_P2mpHeIntFreqEntry_Object=MibTableRow
p2mpHeIntFreqEntry=_P2mpHeIntFreqEntry_Object((1,3,6,1,4,1,9,9,170,1,3,2,1))
p2mpHeIntFreqEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:p2mpHeIntFreqEntry.setStatus(_A)
_P2mpHeIfTxOscState_Type=CwrOscState
_P2mpHeIfTxOscState_Object=MibTableColumn
p2mpHeIfTxOscState=_P2mpHeIfTxOscState_Object((1,3,6,1,4,1,9,9,170,1,3,2,1,1),_P2mpHeIfTxOscState_Type())
p2mpHeIfTxOscState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHeIfTxOscState.setStatus(_A)
_P2mpHeIfRxOscState_Type=CwrOscState
_P2mpHeIfRxOscState_Object=MibTableColumn
p2mpHeIfRxOscState=_P2mpHeIfRxOscState_Object((1,3,6,1,4,1,9,9,170,1,3,2,1,2),_P2mpHeIfRxOscState_Type())
p2mpHeIfRxOscState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHeIfRxOscState.setStatus(_A)
_P2mpHeIfRefOscState_Type=CwrOscState
_P2mpHeIfRefOscState_Object=MibTableColumn
p2mpHeIfRefOscState=_P2mpHeIfRefOscState_Object((1,3,6,1,4,1,9,9,170,1,3,2,1,3),_P2mpHeIfRefOscState_Type())
p2mpHeIfRefOscState.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHeIfRefOscState.setStatus(_A)
class _P2mpHeIfInpFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,500000))
_P2mpHeIfInpFreq_Type.__name__=_F
_P2mpHeIfInpFreq_Object=MibTableColumn
p2mpHeIfInpFreq=_P2mpHeIfInpFreq_Object((1,3,6,1,4,1,9,9,170,1,3,2,1,4),_P2mpHeIfInpFreq_Type())
p2mpHeIfInpFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHeIfInpFreq.setStatus(_A)
if mibBuilder.loadTexts:p2mpHeIfInpFreq.setUnits(_I)
class _P2mpHeIfOutFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,500000))
_P2mpHeIfOutFreq_Type.__name__=_F
_P2mpHeIfOutFreq_Object=MibTableColumn
p2mpHeIfOutFreq=_P2mpHeIfOutFreq_Object((1,3,6,1,4,1,9,9,170,1,3,2,1,5),_P2mpHeIfOutFreq_Type())
p2mpHeIfOutFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:p2mpHeIfOutFreq.setStatus(_A)
if mibBuilder.loadTexts:p2mpHeIfOutFreq.setUnits(_I)
class _P2mpHeTrapEnable_Type(TruthValue):defaultValue=1
_P2mpHeTrapEnable_Type.__name__=_N
_P2mpHeTrapEnable_Object=MibTableColumn
p2mpHeTrapEnable=_P2mpHeTrapEnable_Object((1,3,6,1,4,1,9,9,170,1,3,2,1,6),_P2mpHeTrapEnable_Type())
p2mpHeTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:p2mpHeTrapEnable.setStatus(_A)
_P2mpRadioPhyConformance_ObjectIdentity=ObjectIdentity
p2mpRadioPhyConformance=_P2mpRadioPhyConformance_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,4))
_P2mpRadioPhyCompliances_ObjectIdentity=ObjectIdentity
p2mpRadioPhyCompliances=_P2mpRadioPhyCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,4,1))
_P2mpRadioPhyGroups_ObjectIdentity=ObjectIdentity
p2mpRadioPhyGroups=_P2mpRadioPhyGroups_ObjectIdentity((1,3,6,1,4,1,9,9,170,1,4,2))
_P2mpPhyMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
p2mpPhyMIBNotificationPrefix=_P2mpPhyMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,170,2))
_P2mpPhyMIBNotification_ObjectIdentity=ObjectIdentity
p2mpPhyMIBNotification=_P2mpPhyMIBNotification_ObjectIdentity((1,3,6,1,4,1,9,9,170,2,0))
p2mpCommonRadioGroup=ObjectGroup((1,3,6,1,4,1,9,9,170,1,4,2,1))
p2mpCommonRadioGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_P),(_B,_Q),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:p2mpCommonRadioGroup.setStatus(_A)
p2mpCommonRfGroup=ObjectGroup((1,3,6,1,4,1,9,9,170,1,4,2,2))
p2mpCommonRfGroup.setObjects(*((_B,_M),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:p2mpCommonRfGroup.setStatus(_A)
p2mpCommonTestGroup=ObjectGroup((1,3,6,1,4,1,9,9,170,1,4,2,3))
p2mpCommonTestGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:p2mpCommonTestGroup.setStatus(_A)
p2mpRadioSuGroup=ObjectGroup((1,3,6,1,4,1,9,9,170,1,4,2,5))
p2mpRadioSuGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:p2mpRadioSuGroup.setStatus(_A)
p2mpRadioHeGroup=ObjectGroup((1,3,6,1,4,1,9,9,170,1,4,2,6))
p2mpRadioHeGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_W),(_B,_X),(_B,_Y),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:p2mpRadioHeGroup.setStatus(_A)
p2mpRadioAntennaGroup=ObjectGroup((1,3,6,1,4,1,9,9,170,1,4,2,8))
p2mpRadioAntennaGroup.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:p2mpRadioAntennaGroup.setStatus(_A)
p2mpRadioPhyFailNotification=NotificationType((1,3,6,1,4,1,9,9,170,2,0,1))
p2mpRadioPhyFailNotification.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:p2mpRadioPhyFailNotification.setStatus(_A)
p2mpTrapRfSupplyVoltage=NotificationType((1,3,6,1,4,1,9,9,170,2,0,2))
p2mpTrapRfSupplyVoltage.setObjects((_B,_U))
if mibBuilder.loadTexts:p2mpTrapRfSupplyVoltage.setStatus(_A)
p2mpTrapRfRxOsc=NotificationType((1,3,6,1,4,1,9,9,170,2,0,3))
p2mpTrapRfRxOsc.setObjects((_B,_S))
if mibBuilder.loadTexts:p2mpTrapRfRxOsc.setStatus(_A)
p2mpTrapRfTxOsc=NotificationType((1,3,6,1,4,1,9,9,170,2,0,4))
p2mpTrapRfTxOsc.setObjects((_B,_R))
if mibBuilder.loadTexts:p2mpTrapRfTxOsc.setStatus(_A)
p2mpTrapRfTemp=NotificationType((1,3,6,1,4,1,9,9,170,2,0,5))
p2mpTrapRfTemp.setObjects((_B,_T))
if mibBuilder.loadTexts:p2mpTrapRfTemp.setStatus(_A)
p2mpTrapRfCommLinkError=NotificationType((1,3,6,1,4,1,9,9,170,2,0,6))
p2mpTrapRfCommLinkError.setObjects((_B,_M))
if mibBuilder.loadTexts:p2mpTrapRfCommLinkError.setStatus(_A)
p2mpTrapTxPower=NotificationType((1,3,6,1,4,1,9,9,170,2,0,7))
p2mpTrapTxPower.setObjects((_B,_M))
if mibBuilder.loadTexts:p2mpTrapTxPower.setStatus(_A)
p2mpTrapRfStatusChange=NotificationType((1,3,6,1,4,1,9,9,170,2,0,8))
p2mpTrapRfStatusChange.setObjects((_B,_V))
if mibBuilder.loadTexts:p2mpTrapRfStatusChange.setStatus(_A)
p2mpTrapHeIfRxOsc=NotificationType((1,3,6,1,4,1,9,9,170,2,0,9))
p2mpTrapHeIfRxOsc.setObjects((_B,_X))
if mibBuilder.loadTexts:p2mpTrapHeIfRxOsc.setStatus(_A)
p2mpTrapHeIfTxOsc=NotificationType((1,3,6,1,4,1,9,9,170,2,0,10))
p2mpTrapHeIfTxOsc.setObjects((_B,_W))
if mibBuilder.loadTexts:p2mpTrapHeIfTxOsc.setStatus(_A)
p2mpTrapHeIfExtRefOsc=NotificationType((1,3,6,1,4,1,9,9,170,2,0,11))
p2mpTrapHeIfExtRefOsc.setObjects((_B,_Y))
if mibBuilder.loadTexts:p2mpTrapHeIfExtRefOsc.setStatus(_A)
p2mpRadioPhyCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,170,1,4,1,1))
p2mpRadioPhyCompliance.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:p2mpRadioPhyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWirelessPhyMIB':ciscoWirelessPhyMIB,'p2mpRadioObjects':p2mpRadioObjects,'p2mpRadioBaseObjects':p2mpRadioBaseObjects,'p2mpPhyConfigGroup':p2mpPhyConfigGroup,'p2mpRadioPhyTable':p2mpRadioPhyTable,'p2mpRadioPhyEntry':p2mpRadioPhyEntry,_h:p2mpSelfTest,_i:p2mpDiversityAntennaPresent,_j:p2mpCableLoss,_k:p2mpCableLossDiversity,_l:p2mpDenyService,_m:p2mpClockRefExt,_n:p2mpCommonTrapEnable,_P:p2mpLastPhyFailureType,_Q:p2mpLastPhyFailureReason,'p2mpFreqResourceGroup':p2mpFreqResourceGroup,'p2mpRfTable':p2mpRfTable,'p2mpRfEntry':p2mpRfEntry,_b:p2mpRfIndex,_M:p2mpRfType,_q:p2mpRfOpMode,_r:p2mpTxFreqRangeMin,_s:p2mpTxFreqRangeMax,_t:p2mpRxFreqRangeMin,_u:p2mpRxFreqRangeMax,_v:p2mpMinTxPower,_w:p2mpMaxTxPower,_T:p2mpRfTemperature,_R:p2mpRfTxOscState,_S:p2mpRfRxOscState,_U:p2mpRfSupplyVoltageState,_V:p2mpRfStatus,_x:p2mpRfLoopbackSupported,'p2mpDuplexerTable':p2mpDuplexerTable,'p2mpDuplexerEntry':p2mpDuplexerEntry,_c:p2mpDuplexerIndex,_y:p2mpDuplexerRF,_z:p2mpDuplexerLoPassbandMinFreq,_A0:p2mpDuplexerLoPassbandMaxFreq,_A1:p2mpDuplexerHiPassbandMinFreq,_A2:p2mpDuplexerHiPassbandMaxFreq,_A3:p2mpDuplexerReceivePassband,_A4:p2mpDuplexerTxInsertionLoss,_A5:p2mpDuplexerBurnDate,'p2mpAntennaTable':p2mpAntennaTable,'p2mpAntennaEntry':p2mpAntennaEntry,_d:p2mpAntennaIndex,_AJ:p2mpRfResource,_AK:p2mpAntennaXDim,_AL:p2mpAntennaYDim,_AM:p2mpAntennaType,_AN:p2mpAntennaDescr,_AO:p2mpAntennaGain,_AP:p2mpAntennaPolarization,'p2mpRadioTestGroup':p2mpRadioTestGroup,'p2mpLoopbackTable':p2mpLoopbackTable,'p2mpLoopbackEntry':p2mpLoopbackEntry,_A6:p2mpLocalLoopbackMode,_A7:p2mpLocalLoopbackAntenna,_A8:p2mpLocalLoopbackChannel,'p2mpLedGroup':p2mpLedGroup,'p2mpLedTable':p2mpLedTable,'p2mpLedEntry':p2mpLedEntry,_f:p2mpLedIndex,_o:p2mpLedType,_p:p2mpLedState,'p2mpRadioSuObjects':p2mpRadioSuObjects,'p2mpSuRadioPhyTable':p2mpSuRadioPhyTable,'p2mpSuRadioPhyEntry':p2mpSuRadioPhyEntry,_A9:p2mpSuTxMuteEnable,_AA:p2mpSuTxMuteDuration,'p2mpSuPowerScanTable':p2mpSuPowerScanTable,'p2mpSuPowerScanEntry':p2mpSuPowerScanEntry,_g:p2mpSuPowerScanIndex,_AB:p2mpSuCenterFrequency,_AC:p2mpSuMeasuredPower,'p2mpRadioHeObjects':p2mpRadioHeObjects,'p2mpHeAlcTable':p2mpHeAlcTable,'p2mpHeAlcEntry':p2mpHeAlcEntry,_AD:p2mpHeAlcEnable,_AE:p2mpHeAlcInterval,_AF:p2mpHeAlcNumMiniSlots,'p2mpHeIntFreqTable':p2mpHeIntFreqTable,'p2mpHeIntFreqEntry':p2mpHeIntFreqEntry,_W:p2mpHeIfTxOscState,_X:p2mpHeIfRxOscState,_Y:p2mpHeIfRefOscState,_AG:p2mpHeIfInpFreq,_AH:p2mpHeIfOutFreq,_AI:p2mpHeTrapEnable,'p2mpRadioPhyConformance':p2mpRadioPhyConformance,'p2mpRadioPhyCompliances':p2mpRadioPhyCompliances,'p2mpRadioPhyCompliance':p2mpRadioPhyCompliance,'p2mpRadioPhyGroups':p2mpRadioPhyGroups,_AQ:p2mpCommonRadioGroup,_AR:p2mpCommonRfGroup,_AS:p2mpCommonTestGroup,_AT:p2mpRadioSuGroup,_AU:p2mpRadioHeGroup,_AV:p2mpRadioAntennaGroup,'p2mpPhyMIBNotificationPrefix':p2mpPhyMIBNotificationPrefix,'p2mpPhyMIBNotification':p2mpPhyMIBNotification,'p2mpRadioPhyFailNotification':p2mpRadioPhyFailNotification,'p2mpTrapRfSupplyVoltage':p2mpTrapRfSupplyVoltage,'p2mpTrapRfRxOsc':p2mpTrapRfRxOsc,'p2mpTrapRfTxOsc':p2mpTrapRfTxOsc,'p2mpTrapRfTemp':p2mpTrapRfTemp,'p2mpTrapRfCommLinkError':p2mpTrapRfCommLinkError,'p2mpTrapTxPower':p2mpTrapTxPower,'p2mpTrapRfStatusChange':p2mpTrapRfStatusChange,'p2mpTrapHeIfRxOsc':p2mpTrapHeIfRxOsc,'p2mpTrapHeIfTxOsc':p2mpTrapHeIfTxOsc,'p2mpTrapHeIfExtRefOsc':p2mpTrapHeIfExtRefOsc})