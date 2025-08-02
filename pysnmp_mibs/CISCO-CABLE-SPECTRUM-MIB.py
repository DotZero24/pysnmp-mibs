_BI='ccsUpInFiberNodeGroup'
_BH='ccsUpInSpecGroupGroup'
_BG='ccsSpecGroupFreqGroup'
_BF='ccsUpSpecMgmtGroupRev4'
_BE='ccsUpSpecMgmtGroupRev3'
_BD='ccsUpSpecMgmtGroupRev2'
_BC='ccsUpSpecMgmtGroupRev1'
_BB='ccsSpecMgmtNotification'
_BA='ccsHoppingNotification'
_B9='ccsFiberNodeUpstreamRowStatus'
_B8='ccsFiberNodeUpstreamStorage'
_B7='ccsSpecGroupUpstreamRowStatus'
_B6='ccsSpecGroupUpstreamStorage'
_B5='ccsUpSpecMgmtSharedSpectrum'
_B4='ccsUpSpecMgmtSpecGroup'
_B3='ccsSpecGroupRowStatus'
_B2='ccsSpecGroupStorage'
_B1='ccsSpecGroupFreqUpper'
_B0='ccsSpecGroupFreqLower'
_A_='ccsSpecGroupFreqType'
_Az='ccsCmFlapRowStatus'
_Ay='ccsCmFlapLastResetTime'
_Ax='ccsCmFlapResetNow'
_Aw='ccsCmFlapTotalNum'
_Av='ccsCmFlapPowerAdjustmentNum'
_Au='ccsCmFlapCrcErrorNum'
_At='ccsCmFlapMissNum'
_As='ccsCmFlapHitNum'
_Ar='ccsCmFlapInsertionFailNum'
_Aq='ccsCmFlapCreateTime'
_Ap='ccsCmFlapLastFlapTime'
_Ao='ccsFlapLastClearTime'
_An='ccsFlapClearAll'
_Am='ccsFlapResetAll'
_Al='ccsFlapMissThreshold'
_Ak='ccsFlapPowerAdjustThreshold'
_Aj='ccsFlapLastResetTime'
_Ai='ccsFlapResetNow'
_Ah='ccsFlapTotalNum'
_Ag='ccsFlapPowerAdjustmentNum'
_Af='ccsFlapCrcErrorNum'
_Ae='ccsFlapMissNum'
_Ad='ccsFlapHitNum'
_Ac='ccsFlapInsertionFailNum'
_Ab='ccsUpSpecMgmtSnrPollPeriod'
_Aa='ccsSNRRequestStatus'
_AZ='ccsSNRRequestOperState'
_AY='ccsSNRRequestOperation'
_AX='ccsSNRRequestStoppedTime'
_AW='ccsSNRRequestStartTime'
_AV='ccsSNRRequestSNR'
_AU='ccsSNRRequestMacAddr'
_AT='ccsSpectrumDataPower'
_AS='ccsSpectrumRequestStatus'
_AR='ccsSpectrumRequestOperState'
_AQ='ccsSpectrumRequestOperation'
_AP='ccsSpectrumRequestStoppedTime'
_AO='ccsSpectrumRequestStartTime'
_AN='ccsSpectrumRequestResolution'
_AM='ccsSpectrumRequestLowFreq'
_AL='ccsSpectrumRequestUpperFreq'
_AK='ccsSpectrumRequestMacAddr'
_AJ='ccsSpectrumRequestIfIndex'
_AI='ccsFlapTotal'
_AH='ccsFlapPowerAdjustments'
_AG='ccsFlapCrcErrors'
_AF='ccsFlapMisses'
_AE='ccsFlapHits'
_AD='ccsFlapInsertionFails'
_AC='ccsSpecGroupFreqIndex'
_AB='ccsFiberNodeUpstreamIfIndex'
_AA='ccsFiberNodeNumber'
_A9='ccsSpecGroupUpstreamIfIndex'
_A8='ccsSNRRequestIndex'
_A7='ccsCmFlapMacAddr'
_A6='ccsCmFlapUpstreamIfIndex'
_A5='ccsCmFlapDownstreamIfIndex'
_A4='ccsFlapMacAddr'
_A3='MacAddress'
_A2='ccsNotificationGroupRev1'
_A1='ccsNotificationGroup'
_A0='ccsFlapGroupRev1'
_z='ccsUpSpecMgmtGroup'
_y='ccsFlapGroup'
_x='ccsUpSpecMgmtHopPeriod'
_w='ccsUpSpecMgmtMissedMaintMsgThres'
_v='ccsUpSpecMgmtCNR'
_u='ccsUpSpecMgmtCnrThres2'
_t='ccsUpSpecMgmtCnrThres1'
_s='ccsFlapRowStatus'
_r='ccsFlapCreateTime'
_q='ccsFlapLastFlapTime'
_p='ccsFlapDownstreamIfIndex'
_o='ccsFlapUpstreamIfIndex'
_n='ccsSpecGroupNumber'
_m='ccsSpectrumDataFreq'
_l='CCSRequestOperation'
_k='CCSFrequency'
_j='ccsSpectrumRequestIndex'
_i='others'
_h='ccsFlapGroupRev2'
_g='ccsUpSpecMgmtCriteria'
_f='ccsUpSpecMgmtUpperBoundFreq'
_e='ccsUpSpecMgmtFecCorrectThres2'
_d='ccsFlapInsertionTime'
_c='ccsFlapAging'
_b='ccsFlapListCurrentSize'
_a='ccsFlapListMaxSize'
_Z='ccsUpSpecMgmtHopCondition'
_Y='ccsUpSpecMgmtSNR'
_X='ccsUpSpecMgmtFecUnCorrectThres2'
_W='ccsUpSpecMgmtFecUnCorrectThres1'
_V='ccsUpSpecMgmtFecCorrectThres1'
_U='ccsUpSpecMgmtSnrThres2'
_T='ccsUpSpecMgmtSnrThres1'
_S='ccsUpSpecMgmtHopPriority'
_R='ccsSpectrumGroup'
_Q='dB'
_P='ccsUpSpecMgmtToModProfile'
_O='ccsUpSpecMgmtFromModProfile'
_N='ccsUpSpecMgmtToBandWidth'
_M='ccsUpSpecMgmtFromBandWidth'
_L='ccsUpSpecMgmtToCenterFreq'
_K='ccsUpSpecMgmtFromCenterFreq'
_J='KHz'
_I='not-accessible'
_H='Unsigned32'
_G='read-create'
_F='read-write'
_E='Integer32'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-CABLE-SPECTRUM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString',_A3,'PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp','TruthValue')
ciscoCableSpectrumMIB=ModuleIdentity((1,3,6,1,4,1,9,9,114))
if mibBuilder.loadTexts:ciscoCableSpectrumMIB.setRevisions(('2011-04-08 00:00','2006-10-10 00:00','2004-09-05 00:00','2004-07-14 00:00','2004-03-02 00:00','2003-06-18 00:00','2002-06-10 00:00','2001-02-01 00:00','2000-08-18 00:00','2000-04-24 00:00'))
class CCSFrequency(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,85000))
class CCSMeasuredFrequency(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4000,85000))
class CCSRequestOperation(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('start',1),('abort',2)))
class CCSRequestOperState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('idle',0),('pending',1),('running',2),('noError',3),('aborted',4),('notOnLine',5),('invalidMac',6),('timeOut',7),('fftBusy',8),('fftFailed',9),(_i,10)))
_CiscoCableSpectrumMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCableSpectrumMIBObjects=_CiscoCableSpectrumMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,114,1))
_CcsFlapObjects_ObjectIdentity=ObjectIdentity
ccsFlapObjects=_CcsFlapObjects_ObjectIdentity((1,3,6,1,4,1,9,9,114,1,1))
class _CcsFlapListMaxSize_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_CcsFlapListMaxSize_Type.__name__=_E
_CcsFlapListMaxSize_Object=MibScalar
ccsFlapListMaxSize=_CcsFlapListMaxSize_Object((1,3,6,1,4,1,9,9,114,1,1,1),_CcsFlapListMaxSize_Type())
ccsFlapListMaxSize.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapListMaxSize.setStatus(_B)
if mibBuilder.loadTexts:ccsFlapListMaxSize.setUnits('modems')
class _CcsFlapListCurrentSize_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CcsFlapListCurrentSize_Type.__name__='Gauge32'
_CcsFlapListCurrentSize_Object=MibScalar
ccsFlapListCurrentSize=_CcsFlapListCurrentSize_Object((1,3,6,1,4,1,9,9,114,1,1,2),_CcsFlapListCurrentSize_Type())
ccsFlapListCurrentSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapListCurrentSize.setStatus(_B)
if mibBuilder.loadTexts:ccsFlapListCurrentSize.setUnits('modems')
class _CcsFlapAging_Type(Integer32):defaultValue=10080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CcsFlapAging_Type.__name__=_E
_CcsFlapAging_Object=MibScalar
ccsFlapAging=_CcsFlapAging_Object((1,3,6,1,4,1,9,9,114,1,1,3),_CcsFlapAging_Type())
ccsFlapAging.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapAging.setStatus(_B)
if mibBuilder.loadTexts:ccsFlapAging.setUnits('minutes')
class _CcsFlapInsertionTime_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_CcsFlapInsertionTime_Type.__name__=_E
_CcsFlapInsertionTime_Object=MibScalar
ccsFlapInsertionTime=_CcsFlapInsertionTime_Object((1,3,6,1,4,1,9,9,114,1,1,4),_CcsFlapInsertionTime_Type())
ccsFlapInsertionTime.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapInsertionTime.setStatus(_B)
if mibBuilder.loadTexts:ccsFlapInsertionTime.setUnits('seconds')
_CcsFlapTable_Object=MibTable
ccsFlapTable=_CcsFlapTable_Object((1,3,6,1,4,1,9,9,114,1,1,5))
if mibBuilder.loadTexts:ccsFlapTable.setStatus(_D)
_CcsFlapEntry_Object=MibTableRow
ccsFlapEntry=_CcsFlapEntry_Object((1,3,6,1,4,1,9,9,114,1,1,5,1))
ccsFlapEntry.setIndexNames((0,_A,_A4))
if mibBuilder.loadTexts:ccsFlapEntry.setStatus(_D)
_CcsFlapMacAddr_Type=MacAddress
_CcsFlapMacAddr_Object=MibTableColumn
ccsFlapMacAddr=_CcsFlapMacAddr_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,1),_CcsFlapMacAddr_Type())
ccsFlapMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsFlapMacAddr.setStatus(_D)
_CcsFlapUpstreamIfIndex_Type=InterfaceIndex
_CcsFlapUpstreamIfIndex_Object=MibTableColumn
ccsFlapUpstreamIfIndex=_CcsFlapUpstreamIfIndex_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,2),_CcsFlapUpstreamIfIndex_Type())
ccsFlapUpstreamIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapUpstreamIfIndex.setStatus(_D)
_CcsFlapDownstreamIfIndex_Type=InterfaceIndex
_CcsFlapDownstreamIfIndex_Object=MibTableColumn
ccsFlapDownstreamIfIndex=_CcsFlapDownstreamIfIndex_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,3),_CcsFlapDownstreamIfIndex_Type())
ccsFlapDownstreamIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapDownstreamIfIndex.setStatus(_D)
_CcsFlapInsertionFails_Type=Counter32
_CcsFlapInsertionFails_Object=MibTableColumn
ccsFlapInsertionFails=_CcsFlapInsertionFails_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,4),_CcsFlapInsertionFails_Type())
ccsFlapInsertionFails.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapInsertionFails.setStatus(_D)
_CcsFlapHits_Type=Counter32
_CcsFlapHits_Object=MibTableColumn
ccsFlapHits=_CcsFlapHits_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,5),_CcsFlapHits_Type())
ccsFlapHits.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapHits.setStatus(_D)
_CcsFlapMisses_Type=Counter32
_CcsFlapMisses_Object=MibTableColumn
ccsFlapMisses=_CcsFlapMisses_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,6),_CcsFlapMisses_Type())
ccsFlapMisses.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapMisses.setStatus(_D)
_CcsFlapCrcErrors_Type=Counter32
_CcsFlapCrcErrors_Object=MibTableColumn
ccsFlapCrcErrors=_CcsFlapCrcErrors_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,7),_CcsFlapCrcErrors_Type())
ccsFlapCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapCrcErrors.setStatus(_D)
_CcsFlapPowerAdjustments_Type=Counter32
_CcsFlapPowerAdjustments_Object=MibTableColumn
ccsFlapPowerAdjustments=_CcsFlapPowerAdjustments_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,8),_CcsFlapPowerAdjustments_Type())
ccsFlapPowerAdjustments.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapPowerAdjustments.setStatus(_D)
_CcsFlapTotal_Type=Counter32
_CcsFlapTotal_Object=MibTableColumn
ccsFlapTotal=_CcsFlapTotal_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,9),_CcsFlapTotal_Type())
ccsFlapTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapTotal.setStatus(_D)
_CcsFlapLastFlapTime_Type=DateAndTime
_CcsFlapLastFlapTime_Object=MibTableColumn
ccsFlapLastFlapTime=_CcsFlapLastFlapTime_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,10),_CcsFlapLastFlapTime_Type())
ccsFlapLastFlapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapLastFlapTime.setStatus(_D)
_CcsFlapCreateTime_Type=DateAndTime
_CcsFlapCreateTime_Object=MibTableColumn
ccsFlapCreateTime=_CcsFlapCreateTime_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,11),_CcsFlapCreateTime_Type())
ccsFlapCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapCreateTime.setStatus(_D)
_CcsFlapRowStatus_Type=RowStatus
_CcsFlapRowStatus_Object=MibTableColumn
ccsFlapRowStatus=_CcsFlapRowStatus_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,12),_CcsFlapRowStatus_Type())
ccsFlapRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapRowStatus.setStatus(_D)
_CcsFlapInsertionFailNum_Type=Unsigned32
_CcsFlapInsertionFailNum_Object=MibTableColumn
ccsFlapInsertionFailNum=_CcsFlapInsertionFailNum_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,13),_CcsFlapInsertionFailNum_Type())
ccsFlapInsertionFailNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapInsertionFailNum.setStatus(_D)
_CcsFlapHitNum_Type=Unsigned32
_CcsFlapHitNum_Object=MibTableColumn
ccsFlapHitNum=_CcsFlapHitNum_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,14),_CcsFlapHitNum_Type())
ccsFlapHitNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapHitNum.setStatus(_D)
_CcsFlapMissNum_Type=Unsigned32
_CcsFlapMissNum_Object=MibTableColumn
ccsFlapMissNum=_CcsFlapMissNum_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,15),_CcsFlapMissNum_Type())
ccsFlapMissNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapMissNum.setStatus(_D)
_CcsFlapCrcErrorNum_Type=Unsigned32
_CcsFlapCrcErrorNum_Object=MibTableColumn
ccsFlapCrcErrorNum=_CcsFlapCrcErrorNum_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,16),_CcsFlapCrcErrorNum_Type())
ccsFlapCrcErrorNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapCrcErrorNum.setStatus(_D)
_CcsFlapPowerAdjustmentNum_Type=Unsigned32
_CcsFlapPowerAdjustmentNum_Object=MibTableColumn
ccsFlapPowerAdjustmentNum=_CcsFlapPowerAdjustmentNum_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,17),_CcsFlapPowerAdjustmentNum_Type())
ccsFlapPowerAdjustmentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapPowerAdjustmentNum.setStatus(_D)
_CcsFlapTotalNum_Type=Unsigned32
_CcsFlapTotalNum_Object=MibTableColumn
ccsFlapTotalNum=_CcsFlapTotalNum_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,18),_CcsFlapTotalNum_Type())
ccsFlapTotalNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapTotalNum.setStatus(_D)
_CcsFlapResetNow_Type=TruthValue
_CcsFlapResetNow_Object=MibTableColumn
ccsFlapResetNow=_CcsFlapResetNow_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,19),_CcsFlapResetNow_Type())
ccsFlapResetNow.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapResetNow.setStatus(_D)
_CcsFlapLastResetTime_Type=DateAndTime
_CcsFlapLastResetTime_Object=MibTableColumn
ccsFlapLastResetTime=_CcsFlapLastResetTime_Object((1,3,6,1,4,1,9,9,114,1,1,5,1,20),_CcsFlapLastResetTime_Type())
ccsFlapLastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapLastResetTime.setStatus(_D)
class _CcsFlapPowerAdjustThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CcsFlapPowerAdjustThreshold_Type.__name__=_E
_CcsFlapPowerAdjustThreshold_Object=MibScalar
ccsFlapPowerAdjustThreshold=_CcsFlapPowerAdjustThreshold_Object((1,3,6,1,4,1,9,9,114,1,1,6),_CcsFlapPowerAdjustThreshold_Type())
ccsFlapPowerAdjustThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapPowerAdjustThreshold.setStatus(_D)
if mibBuilder.loadTexts:ccsFlapPowerAdjustThreshold.setUnits('db')
class _CcsFlapMissThreshold_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_CcsFlapMissThreshold_Type.__name__=_H
_CcsFlapMissThreshold_Object=MibScalar
ccsFlapMissThreshold=_CcsFlapMissThreshold_Object((1,3,6,1,4,1,9,9,114,1,1,7),_CcsFlapMissThreshold_Type())
ccsFlapMissThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapMissThreshold.setStatus(_D)
_CcsFlapResetAll_Type=TruthValue
_CcsFlapResetAll_Object=MibScalar
ccsFlapResetAll=_CcsFlapResetAll_Object((1,3,6,1,4,1,9,9,114,1,1,8),_CcsFlapResetAll_Type())
ccsFlapResetAll.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapResetAll.setStatus(_D)
_CcsFlapClearAll_Type=TruthValue
_CcsFlapClearAll_Object=MibScalar
ccsFlapClearAll=_CcsFlapClearAll_Object((1,3,6,1,4,1,9,9,114,1,1,9),_CcsFlapClearAll_Type())
ccsFlapClearAll.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsFlapClearAll.setStatus(_D)
_CcsFlapLastClearTime_Type=DateAndTime
_CcsFlapLastClearTime_Object=MibScalar
ccsFlapLastClearTime=_CcsFlapLastClearTime_Object((1,3,6,1,4,1,9,9,114,1,1,10),_CcsFlapLastClearTime_Type())
ccsFlapLastClearTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsFlapLastClearTime.setStatus(_D)
_CcsCmFlapTable_Object=MibTable
ccsCmFlapTable=_CcsCmFlapTable_Object((1,3,6,1,4,1,9,9,114,1,1,11))
if mibBuilder.loadTexts:ccsCmFlapTable.setStatus(_B)
_CcsCmFlapEntry_Object=MibTableRow
ccsCmFlapEntry=_CcsCmFlapEntry_Object((1,3,6,1,4,1,9,9,114,1,1,11,1))
ccsCmFlapEntry.setIndexNames((0,_A,_A5),(0,_A,_A6),(0,_A,_A7))
if mibBuilder.loadTexts:ccsCmFlapEntry.setStatus(_B)
_CcsCmFlapDownstreamIfIndex_Type=InterfaceIndex
_CcsCmFlapDownstreamIfIndex_Object=MibTableColumn
ccsCmFlapDownstreamIfIndex=_CcsCmFlapDownstreamIfIndex_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,1),_CcsCmFlapDownstreamIfIndex_Type())
ccsCmFlapDownstreamIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsCmFlapDownstreamIfIndex.setStatus(_B)
_CcsCmFlapUpstreamIfIndex_Type=InterfaceIndex
_CcsCmFlapUpstreamIfIndex_Object=MibTableColumn
ccsCmFlapUpstreamIfIndex=_CcsCmFlapUpstreamIfIndex_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,2),_CcsCmFlapUpstreamIfIndex_Type())
ccsCmFlapUpstreamIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsCmFlapUpstreamIfIndex.setStatus(_B)
_CcsCmFlapMacAddr_Type=MacAddress
_CcsCmFlapMacAddr_Object=MibTableColumn
ccsCmFlapMacAddr=_CcsCmFlapMacAddr_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,3),_CcsCmFlapMacAddr_Type())
ccsCmFlapMacAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsCmFlapMacAddr.setStatus(_B)
_CcsCmFlapLastFlapTime_Type=DateAndTime
_CcsCmFlapLastFlapTime_Object=MibTableColumn
ccsCmFlapLastFlapTime=_CcsCmFlapLastFlapTime_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,4),_CcsCmFlapLastFlapTime_Type())
ccsCmFlapLastFlapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapLastFlapTime.setStatus(_B)
_CcsCmFlapCreateTime_Type=DateAndTime
_CcsCmFlapCreateTime_Object=MibTableColumn
ccsCmFlapCreateTime=_CcsCmFlapCreateTime_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,5),_CcsCmFlapCreateTime_Type())
ccsCmFlapCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapCreateTime.setStatus(_B)
_CcsCmFlapInsertionFailNum_Type=Unsigned32
_CcsCmFlapInsertionFailNum_Object=MibTableColumn
ccsCmFlapInsertionFailNum=_CcsCmFlapInsertionFailNum_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,6),_CcsCmFlapInsertionFailNum_Type())
ccsCmFlapInsertionFailNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapInsertionFailNum.setStatus(_B)
_CcsCmFlapHitNum_Type=Unsigned32
_CcsCmFlapHitNum_Object=MibTableColumn
ccsCmFlapHitNum=_CcsCmFlapHitNum_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,7),_CcsCmFlapHitNum_Type())
ccsCmFlapHitNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapHitNum.setStatus(_B)
_CcsCmFlapMissNum_Type=Unsigned32
_CcsCmFlapMissNum_Object=MibTableColumn
ccsCmFlapMissNum=_CcsCmFlapMissNum_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,8),_CcsCmFlapMissNum_Type())
ccsCmFlapMissNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapMissNum.setStatus(_B)
_CcsCmFlapCrcErrorNum_Type=Unsigned32
_CcsCmFlapCrcErrorNum_Object=MibTableColumn
ccsCmFlapCrcErrorNum=_CcsCmFlapCrcErrorNum_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,9),_CcsCmFlapCrcErrorNum_Type())
ccsCmFlapCrcErrorNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapCrcErrorNum.setStatus(_B)
_CcsCmFlapPowerAdjustmentNum_Type=Unsigned32
_CcsCmFlapPowerAdjustmentNum_Object=MibTableColumn
ccsCmFlapPowerAdjustmentNum=_CcsCmFlapPowerAdjustmentNum_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,10),_CcsCmFlapPowerAdjustmentNum_Type())
ccsCmFlapPowerAdjustmentNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapPowerAdjustmentNum.setStatus(_B)
_CcsCmFlapTotalNum_Type=Unsigned32
_CcsCmFlapTotalNum_Object=MibTableColumn
ccsCmFlapTotalNum=_CcsCmFlapTotalNum_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,11),_CcsCmFlapTotalNum_Type())
ccsCmFlapTotalNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapTotalNum.setStatus(_B)
_CcsCmFlapResetNow_Type=TruthValue
_CcsCmFlapResetNow_Object=MibTableColumn
ccsCmFlapResetNow=_CcsCmFlapResetNow_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,12),_CcsCmFlapResetNow_Type())
ccsCmFlapResetNow.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsCmFlapResetNow.setStatus(_B)
_CcsCmFlapLastResetTime_Type=DateAndTime
_CcsCmFlapLastResetTime_Object=MibTableColumn
ccsCmFlapLastResetTime=_CcsCmFlapLastResetTime_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,13),_CcsCmFlapLastResetTime_Type())
ccsCmFlapLastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsCmFlapLastResetTime.setStatus(_B)
_CcsCmFlapRowStatus_Type=RowStatus
_CcsCmFlapRowStatus_Object=MibTableColumn
ccsCmFlapRowStatus=_CcsCmFlapRowStatus_Object((1,3,6,1,4,1,9,9,114,1,1,11,1,14),_CcsCmFlapRowStatus_Type())
ccsCmFlapRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsCmFlapRowStatus.setStatus(_B)
_CcsSpectrumObjects_ObjectIdentity=ObjectIdentity
ccsSpectrumObjects=_CcsSpectrumObjects_ObjectIdentity((1,3,6,1,4,1,9,9,114,1,2))
_CcsSpectrumRequestTable_Object=MibTable
ccsSpectrumRequestTable=_CcsSpectrumRequestTable_Object((1,3,6,1,4,1,9,9,114,1,2,1))
if mibBuilder.loadTexts:ccsSpectrumRequestTable.setStatus(_B)
_CcsSpectrumRequestEntry_Object=MibTableRow
ccsSpectrumRequestEntry=_CcsSpectrumRequestEntry_Object((1,3,6,1,4,1,9,9,114,1,2,1,1))
ccsSpectrumRequestEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:ccsSpectrumRequestEntry.setStatus(_B)
class _CcsSpectrumRequestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcsSpectrumRequestIndex_Type.__name__=_E
_CcsSpectrumRequestIndex_Object=MibTableColumn
ccsSpectrumRequestIndex=_CcsSpectrumRequestIndex_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,1),_CcsSpectrumRequestIndex_Type())
ccsSpectrumRequestIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsSpectrumRequestIndex.setStatus(_B)
_CcsSpectrumRequestIfIndex_Type=InterfaceIndexOrZero
_CcsSpectrumRequestIfIndex_Object=MibTableColumn
ccsSpectrumRequestIfIndex=_CcsSpectrumRequestIfIndex_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,2),_CcsSpectrumRequestIfIndex_Type())
ccsSpectrumRequestIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestIfIndex.setStatus(_B)
class _CcsSpectrumRequestMacAddr_Type(MacAddress):defaultHexValue='000000000000'
_CcsSpectrumRequestMacAddr_Type.__name__=_A3
_CcsSpectrumRequestMacAddr_Object=MibTableColumn
ccsSpectrumRequestMacAddr=_CcsSpectrumRequestMacAddr_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,3),_CcsSpectrumRequestMacAddr_Type())
ccsSpectrumRequestMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestMacAddr.setStatus(_B)
class _CcsSpectrumRequestLowFreq_Type(CCSFrequency):defaultValue=5000
_CcsSpectrumRequestLowFreq_Type.__name__=_k
_CcsSpectrumRequestLowFreq_Object=MibTableColumn
ccsSpectrumRequestLowFreq=_CcsSpectrumRequestLowFreq_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,4),_CcsSpectrumRequestLowFreq_Type())
ccsSpectrumRequestLowFreq.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestLowFreq.setStatus(_B)
if mibBuilder.loadTexts:ccsSpectrumRequestLowFreq.setUnits(_J)
class _CcsSpectrumRequestUpperFreq_Type(CCSFrequency):defaultValue=42000
_CcsSpectrumRequestUpperFreq_Type.__name__=_k
_CcsSpectrumRequestUpperFreq_Object=MibTableColumn
ccsSpectrumRequestUpperFreq=_CcsSpectrumRequestUpperFreq_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,5),_CcsSpectrumRequestUpperFreq_Type())
ccsSpectrumRequestUpperFreq.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestUpperFreq.setStatus(_B)
if mibBuilder.loadTexts:ccsSpectrumRequestUpperFreq.setUnits(_J)
class _CcsSpectrumRequestResolution_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,37000))
_CcsSpectrumRequestResolution_Type.__name__=_E
_CcsSpectrumRequestResolution_Object=MibTableColumn
ccsSpectrumRequestResolution=_CcsSpectrumRequestResolution_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,6),_CcsSpectrumRequestResolution_Type())
ccsSpectrumRequestResolution.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestResolution.setStatus(_B)
if mibBuilder.loadTexts:ccsSpectrumRequestResolution.setUnits(_J)
class _CcsSpectrumRequestOperation_Type(CCSRequestOperation):defaultValue=0
_CcsSpectrumRequestOperation_Type.__name__=_l
_CcsSpectrumRequestOperation_Object=MibTableColumn
ccsSpectrumRequestOperation=_CcsSpectrumRequestOperation_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,7),_CcsSpectrumRequestOperation_Type())
ccsSpectrumRequestOperation.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestOperation.setStatus(_B)
_CcsSpectrumRequestOperState_Type=CCSRequestOperState
_CcsSpectrumRequestOperState_Object=MibTableColumn
ccsSpectrumRequestOperState=_CcsSpectrumRequestOperState_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,8),_CcsSpectrumRequestOperState_Type())
ccsSpectrumRequestOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSpectrumRequestOperState.setStatus(_B)
_CcsSpectrumRequestStartTime_Type=TimeStamp
_CcsSpectrumRequestStartTime_Object=MibTableColumn
ccsSpectrumRequestStartTime=_CcsSpectrumRequestStartTime_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,9),_CcsSpectrumRequestStartTime_Type())
ccsSpectrumRequestStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSpectrumRequestStartTime.setStatus(_B)
_CcsSpectrumRequestStoppedTime_Type=TimeStamp
_CcsSpectrumRequestStoppedTime_Object=MibTableColumn
ccsSpectrumRequestStoppedTime=_CcsSpectrumRequestStoppedTime_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,10),_CcsSpectrumRequestStoppedTime_Type())
ccsSpectrumRequestStoppedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSpectrumRequestStoppedTime.setStatus(_B)
_CcsSpectrumRequestStatus_Type=RowStatus
_CcsSpectrumRequestStatus_Object=MibTableColumn
ccsSpectrumRequestStatus=_CcsSpectrumRequestStatus_Object((1,3,6,1,4,1,9,9,114,1,2,1,1,11),_CcsSpectrumRequestStatus_Type())
ccsSpectrumRequestStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpectrumRequestStatus.setStatus(_B)
_CcsSpectrumDataTable_Object=MibTable
ccsSpectrumDataTable=_CcsSpectrumDataTable_Object((1,3,6,1,4,1,9,9,114,1,2,2))
if mibBuilder.loadTexts:ccsSpectrumDataTable.setStatus(_B)
_CcsSpectrumDataEntry_Object=MibTableRow
ccsSpectrumDataEntry=_CcsSpectrumDataEntry_Object((1,3,6,1,4,1,9,9,114,1,2,2,1))
ccsSpectrumDataEntry.setIndexNames((0,_A,_j),(0,_A,_m))
if mibBuilder.loadTexts:ccsSpectrumDataEntry.setStatus(_B)
_CcsSpectrumDataFreq_Type=CCSMeasuredFrequency
_CcsSpectrumDataFreq_Object=MibTableColumn
ccsSpectrumDataFreq=_CcsSpectrumDataFreq_Object((1,3,6,1,4,1,9,9,114,1,2,2,1,1),_CcsSpectrumDataFreq_Type())
ccsSpectrumDataFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSpectrumDataFreq.setStatus(_B)
if mibBuilder.loadTexts:ccsSpectrumDataFreq.setUnits(_J)
class _CcsSpectrumDataPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,50))
_CcsSpectrumDataPower_Type.__name__=_E
_CcsSpectrumDataPower_Object=MibTableColumn
ccsSpectrumDataPower=_CcsSpectrumDataPower_Object((1,3,6,1,4,1,9,9,114,1,2,2,1,2),_CcsSpectrumDataPower_Type())
ccsSpectrumDataPower.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSpectrumDataPower.setStatus(_B)
if mibBuilder.loadTexts:ccsSpectrumDataPower.setUnits('dBmV')
_CcsSNRRequestTable_Object=MibTable
ccsSNRRequestTable=_CcsSNRRequestTable_Object((1,3,6,1,4,1,9,9,114,1,2,3))
if mibBuilder.loadTexts:ccsSNRRequestTable.setStatus(_B)
_CcsSNRRequestEntry_Object=MibTableRow
ccsSNRRequestEntry=_CcsSNRRequestEntry_Object((1,3,6,1,4,1,9,9,114,1,2,3,1))
ccsSNRRequestEntry.setIndexNames((0,_A,_A8))
if mibBuilder.loadTexts:ccsSNRRequestEntry.setStatus(_B)
class _CcsSNRRequestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcsSNRRequestIndex_Type.__name__=_E
_CcsSNRRequestIndex_Object=MibTableColumn
ccsSNRRequestIndex=_CcsSNRRequestIndex_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,1),_CcsSNRRequestIndex_Type())
ccsSNRRequestIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsSNRRequestIndex.setStatus(_B)
_CcsSNRRequestMacAddr_Type=MacAddress
_CcsSNRRequestMacAddr_Object=MibTableColumn
ccsSNRRequestMacAddr=_CcsSNRRequestMacAddr_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,2),_CcsSNRRequestMacAddr_Type())
ccsSNRRequestMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSNRRequestMacAddr.setStatus(_B)
class _CcsSNRRequestSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_CcsSNRRequestSNR_Type.__name__=_E
_CcsSNRRequestSNR_Object=MibTableColumn
ccsSNRRequestSNR=_CcsSNRRequestSNR_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,3),_CcsSNRRequestSNR_Type())
ccsSNRRequestSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSNRRequestSNR.setStatus(_B)
if mibBuilder.loadTexts:ccsSNRRequestSNR.setUnits(_Q)
class _CcsSNRRequestOperation_Type(CCSRequestOperation):defaultValue=0
_CcsSNRRequestOperation_Type.__name__=_l
_CcsSNRRequestOperation_Object=MibTableColumn
ccsSNRRequestOperation=_CcsSNRRequestOperation_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,4),_CcsSNRRequestOperation_Type())
ccsSNRRequestOperation.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSNRRequestOperation.setStatus(_B)
_CcsSNRRequestOperState_Type=CCSRequestOperState
_CcsSNRRequestOperState_Object=MibTableColumn
ccsSNRRequestOperState=_CcsSNRRequestOperState_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,5),_CcsSNRRequestOperState_Type())
ccsSNRRequestOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSNRRequestOperState.setStatus(_B)
_CcsSNRRequestStartTime_Type=TimeStamp
_CcsSNRRequestStartTime_Object=MibTableColumn
ccsSNRRequestStartTime=_CcsSNRRequestStartTime_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,6),_CcsSNRRequestStartTime_Type())
ccsSNRRequestStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSNRRequestStartTime.setStatus(_B)
_CcsSNRRequestStoppedTime_Type=TimeStamp
_CcsSNRRequestStoppedTime_Object=MibTableColumn
ccsSNRRequestStoppedTime=_CcsSNRRequestStoppedTime_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,7),_CcsSNRRequestStoppedTime_Type())
ccsSNRRequestStoppedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsSNRRequestStoppedTime.setStatus(_B)
_CcsSNRRequestStatus_Type=RowStatus
_CcsSNRRequestStatus_Object=MibTableColumn
ccsSNRRequestStatus=_CcsSNRRequestStatus_Object((1,3,6,1,4,1,9,9,114,1,2,3,1,8),_CcsSNRRequestStatus_Type())
ccsSNRRequestStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSNRRequestStatus.setStatus(_B)
_CcsUpInSpecGroupTable_Object=MibTable
ccsUpInSpecGroupTable=_CcsUpInSpecGroupTable_Object((1,3,6,1,4,1,9,9,114,1,2,4))
if mibBuilder.loadTexts:ccsUpInSpecGroupTable.setStatus(_B)
_CcsUpInSpecGroupEntry_Object=MibTableRow
ccsUpInSpecGroupEntry=_CcsUpInSpecGroupEntry_Object((1,3,6,1,4,1,9,9,114,1,2,4,1))
ccsUpInSpecGroupEntry.setIndexNames((0,_A,_n),(0,_A,_A9))
if mibBuilder.loadTexts:ccsUpInSpecGroupEntry.setStatus(_B)
class _CcsSpecGroupNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CcsSpecGroupNumber_Type.__name__=_H
_CcsSpecGroupNumber_Object=MibTableColumn
ccsSpecGroupNumber=_CcsSpecGroupNumber_Object((1,3,6,1,4,1,9,9,114,1,2,4,1,1),_CcsSpecGroupNumber_Type())
ccsSpecGroupNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsSpecGroupNumber.setStatus(_B)
_CcsSpecGroupUpstreamIfIndex_Type=InterfaceIndex
_CcsSpecGroupUpstreamIfIndex_Object=MibTableColumn
ccsSpecGroupUpstreamIfIndex=_CcsSpecGroupUpstreamIfIndex_Object((1,3,6,1,4,1,9,9,114,1,2,4,1,2),_CcsSpecGroupUpstreamIfIndex_Type())
ccsSpecGroupUpstreamIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsSpecGroupUpstreamIfIndex.setStatus(_B)
_CcsSpecGroupUpstreamStorage_Type=StorageType
_CcsSpecGroupUpstreamStorage_Object=MibTableColumn
ccsSpecGroupUpstreamStorage=_CcsSpecGroupUpstreamStorage_Object((1,3,6,1,4,1,9,9,114,1,2,4,1,3),_CcsSpecGroupUpstreamStorage_Type())
ccsSpecGroupUpstreamStorage.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupUpstreamStorage.setStatus(_B)
_CcsSpecGroupUpstreamRowStatus_Type=RowStatus
_CcsSpecGroupUpstreamRowStatus_Object=MibTableColumn
ccsSpecGroupUpstreamRowStatus=_CcsSpecGroupUpstreamRowStatus_Object((1,3,6,1,4,1,9,9,114,1,2,4,1,4),_CcsSpecGroupUpstreamRowStatus_Type())
ccsSpecGroupUpstreamRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupUpstreamRowStatus.setStatus(_B)
_CcsUpInFiberNodeTable_Object=MibTable
ccsUpInFiberNodeTable=_CcsUpInFiberNodeTable_Object((1,3,6,1,4,1,9,9,114,1,2,5))
if mibBuilder.loadTexts:ccsUpInFiberNodeTable.setStatus(_B)
_CcsUpInFiberNodeEntry_Object=MibTableRow
ccsUpInFiberNodeEntry=_CcsUpInFiberNodeEntry_Object((1,3,6,1,4,1,9,9,114,1,2,5,1))
ccsUpInFiberNodeEntry.setIndexNames((0,_A,_AA),(0,_A,_AB))
if mibBuilder.loadTexts:ccsUpInFiberNodeEntry.setStatus(_B)
class _CcsFiberNodeNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CcsFiberNodeNumber_Type.__name__=_H
_CcsFiberNodeNumber_Object=MibTableColumn
ccsFiberNodeNumber=_CcsFiberNodeNumber_Object((1,3,6,1,4,1,9,9,114,1,2,5,1,1),_CcsFiberNodeNumber_Type())
ccsFiberNodeNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsFiberNodeNumber.setStatus(_B)
_CcsFiberNodeUpstreamIfIndex_Type=InterfaceIndex
_CcsFiberNodeUpstreamIfIndex_Object=MibTableColumn
ccsFiberNodeUpstreamIfIndex=_CcsFiberNodeUpstreamIfIndex_Object((1,3,6,1,4,1,9,9,114,1,2,5,1,2),_CcsFiberNodeUpstreamIfIndex_Type())
ccsFiberNodeUpstreamIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsFiberNodeUpstreamIfIndex.setStatus(_B)
_CcsFiberNodeUpstreamStorage_Type=StorageType
_CcsFiberNodeUpstreamStorage_Object=MibTableColumn
ccsFiberNodeUpstreamStorage=_CcsFiberNodeUpstreamStorage_Object((1,3,6,1,4,1,9,9,114,1,2,5,1,3),_CcsFiberNodeUpstreamStorage_Type())
ccsFiberNodeUpstreamStorage.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsFiberNodeUpstreamStorage.setStatus(_B)
_CcsFiberNodeUpstreamRowStatus_Type=RowStatus
_CcsFiberNodeUpstreamRowStatus_Object=MibTableColumn
ccsFiberNodeUpstreamRowStatus=_CcsFiberNodeUpstreamRowStatus_Object((1,3,6,1,4,1,9,9,114,1,2,5,1,4),_CcsFiberNodeUpstreamRowStatus_Type())
ccsFiberNodeUpstreamRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsFiberNodeUpstreamRowStatus.setStatus(_B)
_CcsConfigObjects_ObjectIdentity=ObjectIdentity
ccsConfigObjects=_CcsConfigObjects_ObjectIdentity((1,3,6,1,4,1,9,9,114,1,3))
_CcsUpSpecMgmtTable_Object=MibTable
ccsUpSpecMgmtTable=_CcsUpSpecMgmtTable_Object((1,3,6,1,4,1,9,9,114,1,3,1))
if mibBuilder.loadTexts:ccsUpSpecMgmtTable.setStatus(_B)
_CcsUpSpecMgmtEntry_Object=MibTableRow
ccsUpSpecMgmtEntry=_CcsUpSpecMgmtEntry_Object((1,3,6,1,4,1,9,9,114,1,3,1,1))
ccsUpSpecMgmtEntry.setIndexNames((0,'IF-MIB','ifIndex'))
if mibBuilder.loadTexts:ccsUpSpecMgmtEntry.setStatus(_B)
class _CcsUpSpecMgmtHopPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('frqModChannel',0),('frqChannelMod',1),('modFrqChannel',2),('modChannelFrq',3),('channelFrqMod',4),('channelModFrq',5)))
_CcsUpSpecMgmtHopPriority_Type.__name__=_E
_CcsUpSpecMgmtHopPriority_Object=MibTableColumn
ccsUpSpecMgmtHopPriority=_CcsUpSpecMgmtHopPriority_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,1),_CcsUpSpecMgmtHopPriority_Type())
ccsUpSpecMgmtHopPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtHopPriority.setStatus(_B)
class _CcsUpSpecMgmtSnrThres1_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,35))
_CcsUpSpecMgmtSnrThres1_Type.__name__=_E
_CcsUpSpecMgmtSnrThres1_Object=MibTableColumn
ccsUpSpecMgmtSnrThres1=_CcsUpSpecMgmtSnrThres1_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,2),_CcsUpSpecMgmtSnrThres1_Type())
ccsUpSpecMgmtSnrThres1.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtSnrThres1.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtSnrThres1.setUnits(_Q)
class _CcsUpSpecMgmtSnrThres2_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,35))
_CcsUpSpecMgmtSnrThres2_Type.__name__=_E
_CcsUpSpecMgmtSnrThres2_Object=MibTableColumn
ccsUpSpecMgmtSnrThres2=_CcsUpSpecMgmtSnrThres2_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,3),_CcsUpSpecMgmtSnrThres2_Type())
ccsUpSpecMgmtSnrThres2.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtSnrThres2.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtSnrThres2.setUnits(_Q)
class _CcsUpSpecMgmtFecCorrectThres1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,30))
_CcsUpSpecMgmtFecCorrectThres1_Type.__name__=_E
_CcsUpSpecMgmtFecCorrectThres1_Object=MibTableColumn
ccsUpSpecMgmtFecCorrectThres1=_CcsUpSpecMgmtFecCorrectThres1_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,4),_CcsUpSpecMgmtFecCorrectThres1_Type())
ccsUpSpecMgmtFecCorrectThres1.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtFecCorrectThres1.setStatus(_B)
class _CcsUpSpecMgmtFecCorrectThres2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CcsUpSpecMgmtFecCorrectThres2_Type.__name__=_E
_CcsUpSpecMgmtFecCorrectThres2_Object=MibTableColumn
ccsUpSpecMgmtFecCorrectThres2=_CcsUpSpecMgmtFecCorrectThres2_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,5),_CcsUpSpecMgmtFecCorrectThres2_Type())
ccsUpSpecMgmtFecCorrectThres2.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtFecCorrectThres2.setStatus(_D)
class _CcsUpSpecMgmtFecUnCorrectThres1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,30))
_CcsUpSpecMgmtFecUnCorrectThres1_Type.__name__=_E
_CcsUpSpecMgmtFecUnCorrectThres1_Object=MibTableColumn
ccsUpSpecMgmtFecUnCorrectThres1=_CcsUpSpecMgmtFecUnCorrectThres1_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,6),_CcsUpSpecMgmtFecUnCorrectThres1_Type())
ccsUpSpecMgmtFecUnCorrectThres1.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtFecUnCorrectThres1.setStatus(_B)
class _CcsUpSpecMgmtFecUnCorrectThres2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,30))
_CcsUpSpecMgmtFecUnCorrectThres2_Type.__name__=_E
_CcsUpSpecMgmtFecUnCorrectThres2_Object=MibTableColumn
ccsUpSpecMgmtFecUnCorrectThres2=_CcsUpSpecMgmtFecUnCorrectThres2_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,7),_CcsUpSpecMgmtFecUnCorrectThres2_Type())
ccsUpSpecMgmtFecUnCorrectThres2.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtFecUnCorrectThres2.setStatus(_B)
class _CcsUpSpecMgmtSnrPollPeriod_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,25000))
_CcsUpSpecMgmtSnrPollPeriod_Type.__name__=_E
_CcsUpSpecMgmtSnrPollPeriod_Object=MibTableColumn
ccsUpSpecMgmtSnrPollPeriod=_CcsUpSpecMgmtSnrPollPeriod_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,8),_CcsUpSpecMgmtSnrPollPeriod_Type())
ccsUpSpecMgmtSnrPollPeriod.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtSnrPollPeriod.setStatus(_D)
if mibBuilder.loadTexts:ccsUpSpecMgmtSnrPollPeriod.setUnits('msec')
class _CcsUpSpecMgmtHopCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('snr',0),('stationMaintainenceMiss',1),(_i,2)))
_CcsUpSpecMgmtHopCondition_Type.__name__=_E
_CcsUpSpecMgmtHopCondition_Object=MibTableColumn
ccsUpSpecMgmtHopCondition=_CcsUpSpecMgmtHopCondition_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,9),_CcsUpSpecMgmtHopCondition_Type())
ccsUpSpecMgmtHopCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtHopCondition.setStatus(_D)
class _CcsUpSpecMgmtFromCenterFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,65000))
_CcsUpSpecMgmtFromCenterFreq_Type.__name__=_H
_CcsUpSpecMgmtFromCenterFreq_Object=MibTableColumn
ccsUpSpecMgmtFromCenterFreq=_CcsUpSpecMgmtFromCenterFreq_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,10),_CcsUpSpecMgmtFromCenterFreq_Type())
ccsUpSpecMgmtFromCenterFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtFromCenterFreq.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtFromCenterFreq.setUnits(_J)
class _CcsUpSpecMgmtToCenterFreq_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,65000))
_CcsUpSpecMgmtToCenterFreq_Type.__name__=_H
_CcsUpSpecMgmtToCenterFreq_Object=MibTableColumn
ccsUpSpecMgmtToCenterFreq=_CcsUpSpecMgmtToCenterFreq_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,11),_CcsUpSpecMgmtToCenterFreq_Type())
ccsUpSpecMgmtToCenterFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtToCenterFreq.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtToCenterFreq.setUnits(_J)
class _CcsUpSpecMgmtFromBandWidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,200),ValueRangeConstraint(400,400),ValueRangeConstraint(800,800),ValueRangeConstraint(1600,1600),ValueRangeConstraint(3200,3200),ValueRangeConstraint(6400,6400))
_CcsUpSpecMgmtFromBandWidth_Type.__name__=_H
_CcsUpSpecMgmtFromBandWidth_Object=MibTableColumn
ccsUpSpecMgmtFromBandWidth=_CcsUpSpecMgmtFromBandWidth_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,12),_CcsUpSpecMgmtFromBandWidth_Type())
ccsUpSpecMgmtFromBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtFromBandWidth.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtFromBandWidth.setUnits(_J)
class _CcsUpSpecMgmtToBandWidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,200),ValueRangeConstraint(400,400),ValueRangeConstraint(800,800),ValueRangeConstraint(1600,1600),ValueRangeConstraint(3200,3200),ValueRangeConstraint(6400,6400))
_CcsUpSpecMgmtToBandWidth_Type.__name__=_H
_CcsUpSpecMgmtToBandWidth_Object=MibTableColumn
ccsUpSpecMgmtToBandWidth=_CcsUpSpecMgmtToBandWidth_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,13),_CcsUpSpecMgmtToBandWidth_Type())
ccsUpSpecMgmtToBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtToBandWidth.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtToBandWidth.setUnits(_J)
class _CcsUpSpecMgmtFromModProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcsUpSpecMgmtFromModProfile_Type.__name__=_E
_CcsUpSpecMgmtFromModProfile_Object=MibTableColumn
ccsUpSpecMgmtFromModProfile=_CcsUpSpecMgmtFromModProfile_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,14),_CcsUpSpecMgmtFromModProfile_Type())
ccsUpSpecMgmtFromModProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtFromModProfile.setStatus(_B)
class _CcsUpSpecMgmtToModProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CcsUpSpecMgmtToModProfile_Type.__name__=_E
_CcsUpSpecMgmtToModProfile_Object=MibTableColumn
ccsUpSpecMgmtToModProfile=_CcsUpSpecMgmtToModProfile_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,15),_CcsUpSpecMgmtToModProfile_Type())
ccsUpSpecMgmtToModProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtToModProfile.setStatus(_B)
class _CcsUpSpecMgmtSNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_CcsUpSpecMgmtSNR_Type.__name__=_E
_CcsUpSpecMgmtSNR_Object=MibTableColumn
ccsUpSpecMgmtSNR=_CcsUpSpecMgmtSNR_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,16),_CcsUpSpecMgmtSNR_Type())
ccsUpSpecMgmtSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtSNR.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtSNR.setUnits(_Q)
_CcsUpSpecMgmtUpperBoundFreq_Type=CCSFrequency
_CcsUpSpecMgmtUpperBoundFreq_Object=MibTableColumn
ccsUpSpecMgmtUpperBoundFreq=_CcsUpSpecMgmtUpperBoundFreq_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,17),_CcsUpSpecMgmtUpperBoundFreq_Type())
ccsUpSpecMgmtUpperBoundFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtUpperBoundFreq.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtUpperBoundFreq.setUnits(_J)
class _CcsUpSpecMgmtCnrThres1_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,35))
_CcsUpSpecMgmtCnrThres1_Type.__name__=_E
_CcsUpSpecMgmtCnrThres1_Object=MibTableColumn
ccsUpSpecMgmtCnrThres1=_CcsUpSpecMgmtCnrThres1_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,18),_CcsUpSpecMgmtCnrThres1_Type())
ccsUpSpecMgmtCnrThres1.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtCnrThres1.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtCnrThres1.setUnits(_Q)
class _CcsUpSpecMgmtCnrThres2_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,35))
_CcsUpSpecMgmtCnrThres2_Type.__name__=_E
_CcsUpSpecMgmtCnrThres2_Object=MibTableColumn
ccsUpSpecMgmtCnrThres2=_CcsUpSpecMgmtCnrThres2_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,19),_CcsUpSpecMgmtCnrThres2_Type())
ccsUpSpecMgmtCnrThres2.setMaxAccess(_F)
if mibBuilder.loadTexts:ccsUpSpecMgmtCnrThres2.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtCnrThres2.setUnits(_Q)
class _CcsUpSpecMgmtCNR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_CcsUpSpecMgmtCNR_Type.__name__=_E
_CcsUpSpecMgmtCNR_Object=MibTableColumn
ccsUpSpecMgmtCNR=_CcsUpSpecMgmtCNR_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,20),_CcsUpSpecMgmtCNR_Type())
ccsUpSpecMgmtCNR.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtCNR.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtCNR.setUnits(_Q)
class _CcsUpSpecMgmtMissedMaintMsgThres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CcsUpSpecMgmtMissedMaintMsgThres_Type.__name__=_E
_CcsUpSpecMgmtMissedMaintMsgThres_Object=MibTableColumn
ccsUpSpecMgmtMissedMaintMsgThres=_CcsUpSpecMgmtMissedMaintMsgThres_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,21),_CcsUpSpecMgmtMissedMaintMsgThres_Type())
ccsUpSpecMgmtMissedMaintMsgThres.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtMissedMaintMsgThres.setStatus(_B)
class _CcsUpSpecMgmtHopPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,3600))
_CcsUpSpecMgmtHopPeriod_Type.__name__=_E
_CcsUpSpecMgmtHopPeriod_Object=MibTableColumn
ccsUpSpecMgmtHopPeriod=_CcsUpSpecMgmtHopPeriod_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,22),_CcsUpSpecMgmtHopPeriod_Type())
ccsUpSpecMgmtHopPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtHopPeriod.setStatus(_B)
if mibBuilder.loadTexts:ccsUpSpecMgmtHopPeriod.setUnits('seconds')
class _CcsUpSpecMgmtCriteria_Type(Bits):namedValues=NamedValues(*(('snrBelowThres',0),('cnrBelowThres',1),('corrFecAboveThres',2),('uncorrFecAboveThres',3),('snrAboveThres',4),('cnrAboveThres',5),('corrFecBelowThres',6),('uncorrFecBelowThres',7),('noActiveModem',8),('uncorrFecAboveSecondThres',9),(_i,10)))
_CcsUpSpecMgmtCriteria_Type.__name__='Bits'
_CcsUpSpecMgmtCriteria_Object=MibTableColumn
ccsUpSpecMgmtCriteria=_CcsUpSpecMgmtCriteria_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,23),_CcsUpSpecMgmtCriteria_Type())
ccsUpSpecMgmtCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtCriteria.setStatus(_B)
class _CcsUpSpecMgmtSpecGroup_Type(Unsigned32):defaultValue=0
_CcsUpSpecMgmtSpecGroup_Type.__name__=_H
_CcsUpSpecMgmtSpecGroup_Object=MibTableColumn
ccsUpSpecMgmtSpecGroup=_CcsUpSpecMgmtSpecGroup_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,24),_CcsUpSpecMgmtSpecGroup_Type())
ccsUpSpecMgmtSpecGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtSpecGroup.setStatus(_B)
class _CcsUpSpecMgmtSharedSpectrum_Type(Unsigned32):defaultValue=0
_CcsUpSpecMgmtSharedSpectrum_Type.__name__=_H
_CcsUpSpecMgmtSharedSpectrum_Object=MibTableColumn
ccsUpSpecMgmtSharedSpectrum=_CcsUpSpecMgmtSharedSpectrum_Object((1,3,6,1,4,1,9,9,114,1,3,1,1,25),_CcsUpSpecMgmtSharedSpectrum_Type())
ccsUpSpecMgmtSharedSpectrum.setMaxAccess(_C)
if mibBuilder.loadTexts:ccsUpSpecMgmtSharedSpectrum.setStatus(_B)
_CcsSpecGroupFreqTable_Object=MibTable
ccsSpecGroupFreqTable=_CcsSpecGroupFreqTable_Object((1,3,6,1,4,1,9,9,114,1,3,2))
if mibBuilder.loadTexts:ccsSpecGroupFreqTable.setStatus(_B)
_CcsSpecGroupFreqEntry_Object=MibTableRow
ccsSpecGroupFreqEntry=_CcsSpecGroupFreqEntry_Object((1,3,6,1,4,1,9,9,114,1,3,2,1))
ccsSpecGroupFreqEntry.setIndexNames((0,_A,_n),(0,_A,_AC))
if mibBuilder.loadTexts:ccsSpecGroupFreqEntry.setStatus(_B)
class _CcsSpecGroupFreqIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CcsSpecGroupFreqIndex_Type.__name__=_H
_CcsSpecGroupFreqIndex_Object=MibTableColumn
ccsSpecGroupFreqIndex=_CcsSpecGroupFreqIndex_Object((1,3,6,1,4,1,9,9,114,1,3,2,1,1),_CcsSpecGroupFreqIndex_Type())
ccsSpecGroupFreqIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccsSpecGroupFreqIndex.setStatus(_B)
class _CcsSpecGroupFreqType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('centerFreq',1),('bandFreq',2)))
_CcsSpecGroupFreqType_Type.__name__=_E
_CcsSpecGroupFreqType_Object=MibTableColumn
ccsSpecGroupFreqType=_CcsSpecGroupFreqType_Object((1,3,6,1,4,1,9,9,114,1,3,2,1,2),_CcsSpecGroupFreqType_Type())
ccsSpecGroupFreqType.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupFreqType.setStatus(_B)
class _CcsSpecGroupFreqLower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CcsSpecGroupFreqLower_Type.__name__=_E
_CcsSpecGroupFreqLower_Object=MibTableColumn
ccsSpecGroupFreqLower=_CcsSpecGroupFreqLower_Object((1,3,6,1,4,1,9,9,114,1,3,2,1,3),_CcsSpecGroupFreqLower_Type())
ccsSpecGroupFreqLower.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupFreqLower.setStatus(_B)
if mibBuilder.loadTexts:ccsSpecGroupFreqLower.setUnits('Hz')
class _CcsSpecGroupFreqUpper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_CcsSpecGroupFreqUpper_Type.__name__=_E
_CcsSpecGroupFreqUpper_Object=MibTableColumn
ccsSpecGroupFreqUpper=_CcsSpecGroupFreqUpper_Object((1,3,6,1,4,1,9,9,114,1,3,2,1,4),_CcsSpecGroupFreqUpper_Type())
ccsSpecGroupFreqUpper.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupFreqUpper.setStatus(_B)
if mibBuilder.loadTexts:ccsSpecGroupFreqUpper.setUnits('Hz')
_CcsSpecGroupStorage_Type=StorageType
_CcsSpecGroupStorage_Object=MibTableColumn
ccsSpecGroupStorage=_CcsSpecGroupStorage_Object((1,3,6,1,4,1,9,9,114,1,3,2,1,5),_CcsSpecGroupStorage_Type())
ccsSpecGroupStorage.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupStorage.setStatus(_B)
_CcsSpecGroupRowStatus_Type=RowStatus
_CcsSpecGroupRowStatus_Object=MibTableColumn
ccsSpecGroupRowStatus=_CcsSpecGroupRowStatus_Object((1,3,6,1,4,1,9,9,114,1,3,2,1,6),_CcsSpecGroupRowStatus_Type())
ccsSpecGroupRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ccsSpecGroupRowStatus.setStatus(_B)
_CiscoCableSpectrumMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoCableSpectrumMIBNotificationPrefix=_CiscoCableSpectrumMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,114,2))
_CcsMIBNotifications_ObjectIdentity=ObjectIdentity
ccsMIBNotifications=_CcsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,114,2,0))
_CiscoCableSpectrumMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCableSpectrumMIBConformance=_CiscoCableSpectrumMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,114,3))
_CiscoCableSpectrumMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCableSpectrumMIBCompliances=_CiscoCableSpectrumMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,114,3,1))
_CiscoCableSpectrumMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCableSpectrumMIBGroups=_CiscoCableSpectrumMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,114,3,2))
ccsFlapGroup=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,1))
ccsFlapGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_o),(_A,_p),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ccsFlapGroup.setStatus(_D)
ccsSpectrumGroup=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,2))
ccsSpectrumGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_m),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:ccsSpectrumGroup.setStatus(_B)
ccsUpSpecMgmtGroup=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,3))
ccsUpSpecMgmtGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_e),(_A,_W),(_A,_X),(_A,_Ab),(_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y)))
if mibBuilder.loadTexts:ccsUpSpecMgmtGroup.setStatus(_D)
ccsFlapGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,5))
ccsFlapGroupRev1.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:ccsFlapGroupRev1.setStatus(_D)
ccsUpSpecMgmtGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,6))
ccsUpSpecMgmtGroupRev1.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_e),(_A,_W),(_A,_X),(_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y)))
if mibBuilder.loadTexts:ccsUpSpecMgmtGroupRev1.setStatus(_D)
ccsFlapGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,7))
ccsFlapGroupRev2.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:ccsFlapGroupRev2.setStatus(_B)
ccsUpSpecMgmtGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,8))
ccsUpSpecMgmtGroupRev2.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_e),(_A,_W),(_A,_X),(_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y),(_A,_f)))
if mibBuilder.loadTexts:ccsUpSpecMgmtGroupRev2.setStatus(_D)
ccsUpSpecMgmtGroupRev3=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,10))
ccsUpSpecMgmtGroupRev3.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y),(_A,_f),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_g)))
if mibBuilder.loadTexts:ccsUpSpecMgmtGroupRev3.setStatus(_D)
ccsSpecGroupFreqGroup=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,11))
ccsSpecGroupFreqGroup.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3)))
if mibBuilder.loadTexts:ccsSpecGroupFreqGroup.setStatus(_B)
ccsUpSpecMgmtGroupRev4=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,12))
ccsUpSpecMgmtGroupRev4.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y),(_A,_f),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_g),(_A,_B4),(_A,_B5)))
if mibBuilder.loadTexts:ccsUpSpecMgmtGroupRev4.setStatus(_B)
ccsUpInSpecGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,13))
ccsUpInSpecGroupGroup.setObjects(*((_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:ccsUpInSpecGroupGroup.setStatus(_B)
ccsUpInFiberNodeGroup=ObjectGroup((1,3,6,1,4,1,9,9,114,3,2,14))
ccsUpInFiberNodeGroup.setObjects(*((_A,_B8),(_A,_B9)))
if mibBuilder.loadTexts:ccsUpInFiberNodeGroup.setStatus(_B)
ccsHoppingNotification=NotificationType((1,3,6,1,4,1,9,9,114,2,0,1))
ccsHoppingNotification.setObjects(*((_A,_Z),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ccsHoppingNotification.setStatus(_D)
ccsSpecMgmtNotification=NotificationType((1,3,6,1,4,1,9,9,114,2,0,2))
ccsSpecMgmtNotification.setObjects(*((_A,_g),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ccsSpecMgmtNotification.setStatus(_B)
ccsNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,114,3,2,4))
ccsNotificationGroup.setObjects((_A,_BA))
if mibBuilder.loadTexts:ccsNotificationGroup.setStatus(_D)
ccsNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,114,3,2,9))
ccsNotificationGroupRev1.setObjects((_A,_BB))
if mibBuilder.loadTexts:ccsNotificationGroupRev1.setStatus(_B)
ccsCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,1))
ccsCompliance.setObjects((_A,_y))
if mibBuilder.loadTexts:ccsCompliance.setStatus('obsolete')
ccsCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,2))
ccsCompliance2.setObjects(*((_A,_y),(_A,_R),(_A,_z)))
if mibBuilder.loadTexts:ccsCompliance2.setStatus(_D)
ccsCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,3))
ccsCompliance3.setObjects(*((_A,_A0),(_A,_R),(_A,_z)))
if mibBuilder.loadTexts:ccsCompliance3.setStatus(_D)
ccsCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,4))
ccsCompliance4.setObjects(*((_A,_A0),(_A,_R),(_A,_A1),(_A,_BC)))
if mibBuilder.loadTexts:ccsCompliance4.setStatus(_D)
ccsCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,5))
ccsCompliance5.setObjects(*((_A,_h),(_A,_R),(_A,_A1),(_A,_BD)))
if mibBuilder.loadTexts:ccsCompliance5.setStatus(_D)
ccsCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,6))
ccsCompliance6.setObjects(*((_A,_h),(_A,_R),(_A,_A2),(_A,_BE)))
if mibBuilder.loadTexts:ccsCompliance6.setStatus(_D)
ccsCompliance7=ModuleCompliance((1,3,6,1,4,1,9,9,114,3,1,7))
ccsCompliance7.setObjects(*((_A,_h),(_A,_R),(_A,_A2),(_A,_BF),(_A,_BG),(_A,_BH),(_A,_BI)))
if mibBuilder.loadTexts:ccsCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_k:CCSFrequency,'CCSMeasuredFrequency':CCSMeasuredFrequency,_l:CCSRequestOperation,'CCSRequestOperState':CCSRequestOperState,'ciscoCableSpectrumMIB':ciscoCableSpectrumMIB,'ciscoCableSpectrumMIBObjects':ciscoCableSpectrumMIBObjects,'ccsFlapObjects':ccsFlapObjects,_a:ccsFlapListMaxSize,_b:ccsFlapListCurrentSize,_c:ccsFlapAging,_d:ccsFlapInsertionTime,'ccsFlapTable':ccsFlapTable,'ccsFlapEntry':ccsFlapEntry,_A4:ccsFlapMacAddr,_o:ccsFlapUpstreamIfIndex,_p:ccsFlapDownstreamIfIndex,_AD:ccsFlapInsertionFails,_AE:ccsFlapHits,_AF:ccsFlapMisses,_AG:ccsFlapCrcErrors,_AH:ccsFlapPowerAdjustments,_AI:ccsFlapTotal,_q:ccsFlapLastFlapTime,_r:ccsFlapCreateTime,_s:ccsFlapRowStatus,_Ac:ccsFlapInsertionFailNum,_Ad:ccsFlapHitNum,_Ae:ccsFlapMissNum,_Af:ccsFlapCrcErrorNum,_Ag:ccsFlapPowerAdjustmentNum,_Ah:ccsFlapTotalNum,_Ai:ccsFlapResetNow,_Aj:ccsFlapLastResetTime,_Ak:ccsFlapPowerAdjustThreshold,_Al:ccsFlapMissThreshold,_Am:ccsFlapResetAll,_An:ccsFlapClearAll,_Ao:ccsFlapLastClearTime,'ccsCmFlapTable':ccsCmFlapTable,'ccsCmFlapEntry':ccsCmFlapEntry,_A5:ccsCmFlapDownstreamIfIndex,_A6:ccsCmFlapUpstreamIfIndex,_A7:ccsCmFlapMacAddr,_Ap:ccsCmFlapLastFlapTime,_Aq:ccsCmFlapCreateTime,_Ar:ccsCmFlapInsertionFailNum,_As:ccsCmFlapHitNum,_At:ccsCmFlapMissNum,_Au:ccsCmFlapCrcErrorNum,_Av:ccsCmFlapPowerAdjustmentNum,_Aw:ccsCmFlapTotalNum,_Ax:ccsCmFlapResetNow,_Ay:ccsCmFlapLastResetTime,_Az:ccsCmFlapRowStatus,'ccsSpectrumObjects':ccsSpectrumObjects,'ccsSpectrumRequestTable':ccsSpectrumRequestTable,'ccsSpectrumRequestEntry':ccsSpectrumRequestEntry,_j:ccsSpectrumRequestIndex,_AJ:ccsSpectrumRequestIfIndex,_AK:ccsSpectrumRequestMacAddr,_AM:ccsSpectrumRequestLowFreq,_AL:ccsSpectrumRequestUpperFreq,_AN:ccsSpectrumRequestResolution,_AQ:ccsSpectrumRequestOperation,_AR:ccsSpectrumRequestOperState,_AO:ccsSpectrumRequestStartTime,_AP:ccsSpectrumRequestStoppedTime,_AS:ccsSpectrumRequestStatus,'ccsSpectrumDataTable':ccsSpectrumDataTable,'ccsSpectrumDataEntry':ccsSpectrumDataEntry,_m:ccsSpectrumDataFreq,_AT:ccsSpectrumDataPower,'ccsSNRRequestTable':ccsSNRRequestTable,'ccsSNRRequestEntry':ccsSNRRequestEntry,_A8:ccsSNRRequestIndex,_AU:ccsSNRRequestMacAddr,_AV:ccsSNRRequestSNR,_AY:ccsSNRRequestOperation,_AZ:ccsSNRRequestOperState,_AW:ccsSNRRequestStartTime,_AX:ccsSNRRequestStoppedTime,_Aa:ccsSNRRequestStatus,'ccsUpInSpecGroupTable':ccsUpInSpecGroupTable,'ccsUpInSpecGroupEntry':ccsUpInSpecGroupEntry,_n:ccsSpecGroupNumber,_A9:ccsSpecGroupUpstreamIfIndex,_B6:ccsSpecGroupUpstreamStorage,_B7:ccsSpecGroupUpstreamRowStatus,'ccsUpInFiberNodeTable':ccsUpInFiberNodeTable,'ccsUpInFiberNodeEntry':ccsUpInFiberNodeEntry,_AA:ccsFiberNodeNumber,_AB:ccsFiberNodeUpstreamIfIndex,_B8:ccsFiberNodeUpstreamStorage,_B9:ccsFiberNodeUpstreamRowStatus,'ccsConfigObjects':ccsConfigObjects,'ccsUpSpecMgmtTable':ccsUpSpecMgmtTable,'ccsUpSpecMgmtEntry':ccsUpSpecMgmtEntry,_S:ccsUpSpecMgmtHopPriority,_T:ccsUpSpecMgmtSnrThres1,_U:ccsUpSpecMgmtSnrThres2,_V:ccsUpSpecMgmtFecCorrectThres1,_e:ccsUpSpecMgmtFecCorrectThres2,_W:ccsUpSpecMgmtFecUnCorrectThres1,_X:ccsUpSpecMgmtFecUnCorrectThres2,_Ab:ccsUpSpecMgmtSnrPollPeriod,_Z:ccsUpSpecMgmtHopCondition,_K:ccsUpSpecMgmtFromCenterFreq,_L:ccsUpSpecMgmtToCenterFreq,_M:ccsUpSpecMgmtFromBandWidth,_N:ccsUpSpecMgmtToBandWidth,_O:ccsUpSpecMgmtFromModProfile,_P:ccsUpSpecMgmtToModProfile,_Y:ccsUpSpecMgmtSNR,_f:ccsUpSpecMgmtUpperBoundFreq,_t:ccsUpSpecMgmtCnrThres1,_u:ccsUpSpecMgmtCnrThres2,_v:ccsUpSpecMgmtCNR,_w:ccsUpSpecMgmtMissedMaintMsgThres,_x:ccsUpSpecMgmtHopPeriod,_g:ccsUpSpecMgmtCriteria,_B4:ccsUpSpecMgmtSpecGroup,_B5:ccsUpSpecMgmtSharedSpectrum,'ccsSpecGroupFreqTable':ccsSpecGroupFreqTable,'ccsSpecGroupFreqEntry':ccsSpecGroupFreqEntry,_AC:ccsSpecGroupFreqIndex,_A_:ccsSpecGroupFreqType,_B0:ccsSpecGroupFreqLower,_B1:ccsSpecGroupFreqUpper,_B2:ccsSpecGroupStorage,_B3:ccsSpecGroupRowStatus,'ciscoCableSpectrumMIBNotificationPrefix':ciscoCableSpectrumMIBNotificationPrefix,'ccsMIBNotifications':ccsMIBNotifications,_BA:ccsHoppingNotification,_BB:ccsSpecMgmtNotification,'ciscoCableSpectrumMIBConformance':ciscoCableSpectrumMIBConformance,'ciscoCableSpectrumMIBCompliances':ciscoCableSpectrumMIBCompliances,'ccsCompliance':ccsCompliance,'ccsCompliance2':ccsCompliance2,'ccsCompliance3':ccsCompliance3,'ccsCompliance4':ccsCompliance4,'ccsCompliance5':ccsCompliance5,'ccsCompliance6':ccsCompliance6,'ccsCompliance7':ccsCompliance7,'ciscoCableSpectrumMIBGroups':ciscoCableSpectrumMIBGroups,_y:ccsFlapGroup,_R:ccsSpectrumGroup,_z:ccsUpSpecMgmtGroup,_A1:ccsNotificationGroup,_A0:ccsFlapGroupRev1,_BC:ccsUpSpecMgmtGroupRev1,_h:ccsFlapGroupRev2,_BD:ccsUpSpecMgmtGroupRev2,_A2:ccsNotificationGroupRev1,_BE:ccsUpSpecMgmtGroupRev3,_BG:ccsSpecGroupFreqGroup,_BF:ccsUpSpecMgmtGroupRev4,_BH:ccsUpInSpecGroupGroup,_BI:ccsUpInFiberNodeGroup})