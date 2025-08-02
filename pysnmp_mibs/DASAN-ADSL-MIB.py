_An='dsAdslLineAlarmExtnAturThresh1DayFecsL'
_Am='dsAdslAturPerfDataExtnCurr1DayFecsL'
_Al='dsAdslLineAlarmExtnAturThresh1DayUasL'
_Ak='dsAdslAturPerfDataExtnCurr1DayUasL'
_Aj='dsAdslLineAlarmExtnAturThresh1DaySesL'
_Ai='dsAdslAturPerfDataExtnCurr1DaySesL'
_Ah='dsAdslLineAlarmExtnAturThresh1DayESs'
_Ag='dsAdslLineAlarmExtnAturThresh1DayLprs'
_Af='dsAdslLineAlarmExtnAturThresh1DayLoss'
_Ae='dsAdslLineAlarmExtnAturThresh1DayLofs'
_Ad='dsAdslLineAlarmExtnAturThresh15MinFecsL'
_Ac='dsAdslAturPerfDataExtnCurr15MinFecsL'
_Ab='dsAdslLineAlarmExtnAturThresh15MinUasL'
_Aa='dsAdslAturPerfDataExtnCurr15MinUasL'
_AZ='dsAdslLineAlarmExtnAturThresh15MinSesL'
_AY='dsAdslAturPerfDataExtnCurr15MinSesL'
_AX='dsAdslLineAlarmExtnAtucThresh1DayFecsL'
_AW='dsAdslAtucPerfDataExtnCurr1DayFecsL'
_AV='dsAdslLineAlarmExtnAtucThresh1DayUasL'
_AU='dsAdslAtucPerfDataExtnCurr1DayUasL'
_AT='dsAdslLineAlarmExtnAtucThresh1DaySesL'
_AS='dsAdslAtucPerfDataExtnCurr1DaySesL'
_AR='dsAdslLineAlarmExtnAtucThresh1DayESs'
_AQ='dsAdslLineAlarmExtnAtucThresh1DayLprs'
_AP='dsAdslLineAlarmExtnAtucThresh1DayLols'
_AO='dsAdslLineAlarmExtnAtucThresh1DayLoss'
_AN='dsAdslLineAlarmExtnAtucThresh1DayLofs'
_AM='dsAdslLineAlarmExtnAtucThresh15MinFecsL'
_AL='dsAdslAtucPerfDataExtnCurr15MinFecsL'
_AK='dsAdslLineAlarmExtnAtucThresh15MinUasL'
_AJ='dsAdslAtucPerfDataExtnCurr15MinUasL'
_AI='dsAdslLineAlarmExtnAtucThresh15MinSesL'
_AH='dsAdslAtucPerfDataExtnCurr15MinSesL'
_AG='dsAdslLineAlarmExtnAtucThresh15MinFailFastR'
_AF='dsAdslAtucPerfDataExtnCurr15MinFailedFastR'
_AE='dsAdslAtucPhysExtnPMState'
_AD='dsAdslAtucPhysExtnOpState'
_AC='dsAdslLineConfProfileExtnTable50'
_AB='not-accessible'
_AA='lossOfCellDelineation'
_A9='noCellDelineation'
_A8='noAtmDefect'
_A7='cabMsk2Rfi'
_A6='flatMskRfi'
_A5='gspanPlus'
_A4='adsl2PlusAuto'
_A3='adsl2Auto'
_A2='adsl2Plus'
_A1='multimode'
_A0='q9921tcmIsdnSymmetric'
_z='q9922tcmIsdnOverlapped'
_y='q9922tcmIsdnNonOverlapped'
_x='q9922potsOverlapped'
_w='q9922potsNonOverlapeed'
_v='q9921tcmIsdnOverlapped'
_u='q9921tcmIsdnNonOverlapped'
_t='q9921isdnOverlapped'
_s='q9921GspanPlusPotsNonOverlapped'
_r='q9921GspanPlusPotsOverlapped'
_q='q9923Adsl2PotsOverlapped'
_p='q9923Adsl2PotsNonOverlapped'
_o='q9925Adsl2PlusPotsOverlapped'
_n='q9925Adsl2PlusPotsNonOverlapped'
_m='q9923Readsl2PotsNonOverlapped'
_l='q9923Readsl2PotsOverlapped'
_k='adslPlusPotsOverlapped'
_j='q9921TcmIsdnSymmetric'
_i='q9922TcmIsdnOverlapped'
_h='q9922TcmIsdnNonOverlapped'
_g='q9922PotsOverlapped'
_f='q9922PotsNonOverlapped'
_e='q9921TcmIsdnOverlapped'
_d='q9921TcmIsdnNonOverlapped'
_c='q9921IsdnOverlapped'
_b='adslLineConfProfileName'
_a='adslLineAlarmConfProfileName'
_Z='adslAturChanIntervalNumber'
_Y='adslAtucIntervalNumber'
_X='adslAtucChanIntervalNumber'
_W='dsAdslLineConfProfileExtnTable25'
_V='dsAdslLineConfProfileExtnTable12'
_U='dsAdslLineConfProfileExtnTable6'
_T='dsAdslLineConfProfileExtnTable3'
_S='dsAdslLineConfProfileExtnTable1'
_R='adslPlusPotsNonOverlapped'
_Q='adsl'
_P='q9921IsdnNonOverlapped'
_O='q9921PotsOverlapped'
_N='q9921PotsNonOverlapped'
_M='etsi'
_L='ansit1413'
_K='Bits'
_J='ADSL-LINE-MIB'
_I='disable'
_H='OctetString'
_G='ifIndex'
_F='IF-MIB'
_E='DASAN-ADSL-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslAtucChanIntervalNumber,adslAtucIntervalNumber,adslAturChanIntervalNumber,adslLineAlarmConfProfileName,adslLineConfProfileName=mibBuilder.importSymbols(_J,_X,_Y,_Z,_a,_b)
dasanMgmt,=mibBuilder.importSymbols('DASAN-SMI','dasanMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
dasanAdslMIB=ModuleIdentity((1,3,6,1,4,1,6296,9,5))
_DasanAdslLineMIB_ObjectIdentity=ObjectIdentity
dasanAdslLineMIB=_DasanAdslLineMIB_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1))
_DasanAdslMIBObjects_ObjectIdentity=ObjectIdentity
dasanAdslMIBObjects=_DasanAdslMIBObjects_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1,1))
_DsDslSystemParamGroup_ObjectIdentity=ObjectIdentity
dsDslSystemParamGroup=_DsDslSystemParamGroup_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1,1,1))
class _DsDslSystemDslType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('sdsl',2),('shdsl',3)))
_DsDslSystemDslType_Type.__name__=_C
_DsDslSystemDslType_Object=MibScalar
dsDslSystemDslType=_DsDslSystemDslType_Object((1,3,6,1,4,1,6296,9,5,1,1,1,1),_DsDslSystemDslType_Type())
dsDslSystemDslType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsDslSystemDslType.setStatus(_A)
class _DsDslSystemLineCodingType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('dmt',2),('cap',3),('qam',4)))
_DsDslSystemLineCodingType_Type.__name__=_C
_DsDslSystemLineCodingType_Object=MibScalar
dsDslSystemLineCodingType=_DsDslSystemLineCodingType_Object((1,3,6,1,4,1,6296,9,5,1,1,1,2),_DsDslSystemLineCodingType_Type())
dsDslSystemLineCodingType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsDslSystemLineCodingType.setStatus(_A)
class _DsDslSystemLineTxCfg_Type(Bits):defaultHexValue='0c';namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4),(_c,5),(_d,6),(_e,7),(_f,8),(_g,9),(_h,10),(_i,11),(_j,12)))
_DsDslSystemLineTxCfg_Type.__name__=_K
_DsDslSystemLineTxCfg_Object=MibScalar
dsDslSystemLineTxCfg=_DsDslSystemLineTxCfg_Object((1,3,6,1,4,1,6296,9,5,1,1,1,3),_DsDslSystemLineTxCfg_Type())
dsDslSystemLineTxCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:dsDslSystemLineTxCfg.setStatus(_A)
_DsAdslCapabilityGroup_ObjectIdentity=ObjectIdentity
dsAdslCapabilityGroup=_DsAdslCapabilityGroup_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1,1,2))
class _DsAdslCapabilityLineTxCap_Type(Bits):namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4),(_c,5),(_d,6),(_e,7),(_f,8),(_g,9),(_h,10),(_i,11),(_j,12),(_R,13),(_k,18),(_l,22),(_m,23),(_n,26),(_o,27),(_p,28),(_q,29),(_r,30),(_s,31)))
_DsAdslCapabilityLineTxCap_Type.__name__=_K
_DsAdslCapabilityLineTxCap_Object=MibScalar
dsAdslCapabilityLineTxCap=_DsAdslCapabilityLineTxCap_Object((1,3,6,1,4,1,6296,9,5,1,1,2,1),_DsAdslCapabilityLineTxCap_Type())
dsAdslCapabilityLineTxCap.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslCapabilityLineTxCap.setStatus(_A)
_DsAdslLineExtnTable_Object=MibTable
dsAdslLineExtnTable=_DsAdslLineExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,3))
if mibBuilder.loadTexts:dsAdslLineExtnTable.setStatus(_A)
_DsAdslLineExtnEntry_Object=MibTableRow
dsAdslLineExtnEntry=_DsAdslLineExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1))
dsAdslLineExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslLineExtnEntry.setStatus(_A)
class _DsAdslLineExtnAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,6,7,10,26,27,30,32,33,34,35,36,37,38,101,102,4134)));namedValues=NamedValues(*(('startup',0),('spectrumReverb',5),('analogLb',6),('digitalLb',7),('atmLp',10),('spectrumMedley',26),('spectrumPilot',27),('spectrumCMtpr',30),('spectrumRMtpr',32),('hybridLossTest',33),('rcvLinearityTest',34),('rcvFilterTest',35),('rcvPowerPerBinTest',36),('idleNoisePerBinTest',37),('totalIdleNoiseTest',38),('shutdown',101),('wakeup',102),('selt',4134)))
_DsAdslLineExtnAction_Type.__name__=_C
_DsAdslLineExtnAction_Object=MibTableColumn
dsAdslLineExtnAction=_DsAdslLineExtnAction_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,1),_DsAdslLineExtnAction_Type())
dsAdslLineExtnAction.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineExtnAction.setStatus(_A)
class _DsAdslLineExtnUtopiaL2RxAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DsAdslLineExtnUtopiaL2RxAddr_Type.__name__=_C
_DsAdslLineExtnUtopiaL2RxAddr_Object=MibTableColumn
dsAdslLineExtnUtopiaL2RxAddr=_DsAdslLineExtnUtopiaL2RxAddr_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,2),_DsAdslLineExtnUtopiaL2RxAddr_Type())
dsAdslLineExtnUtopiaL2RxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineExtnUtopiaL2RxAddr.setStatus(_A)
class _DsAdslLineExtnUtopiaL2TxAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DsAdslLineExtnUtopiaL2TxAddr_Type.__name__=_C
_DsAdslLineExtnUtopiaL2TxAddr_Object=MibTableColumn
dsAdslLineExtnUtopiaL2TxAddr=_DsAdslLineExtnUtopiaL2TxAddr_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,3),_DsAdslLineExtnUtopiaL2TxAddr_Type())
dsAdslLineExtnUtopiaL2TxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineExtnUtopiaL2TxAddr.setStatus(_A)
class _DsAdslLineExtnTransAtucCap_Type(Bits):namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4),(_t,5),(_u,6),(_v,7),(_w,8),(_x,9),(_y,10),(_z,11),(_A0,12),(_R,13),(_k,18),(_l,22),(_m,23),('vdslOverlapped',24),('vdslNonOverlapped',25),(_n,26),(_o,27),(_p,28),(_q,29),(_r,30),(_s,31)))
_DsAdslLineExtnTransAtucCap_Type.__name__=_K
_DsAdslLineExtnTransAtucCap_Object=MibTableColumn
dsAdslLineExtnTransAtucCap=_DsAdslLineExtnTransAtucCap_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,4),_DsAdslLineExtnTransAtucCap_Type())
dsAdslLineExtnTransAtucCap.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineExtnTransAtucCap.setStatus(_A)
class _DsAdslLineExtnTransAtucActual_Type(Bits):namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4),(_t,5),(_u,6),(_v,7),(_w,8),(_x,9),(_y,10),(_z,11),(_A0,12),(_R,13)))
_DsAdslLineExtnTransAtucActual_Type.__name__=_K
_DsAdslLineExtnTransAtucActual_Object=MibTableColumn
dsAdslLineExtnTransAtucActual=_DsAdslLineExtnTransAtucActual_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,5),_DsAdslLineExtnTransAtucActual_Type())
dsAdslLineExtnTransAtucActual.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineExtnTransAtucActual.setStatus(_A)
class _DsAdslLineExtnClockType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*(('oscillator',0),('crystal',4)))
_DsAdslLineExtnClockType_Type.__name__=_C
_DsAdslLineExtnClockType_Object=MibTableColumn
dsAdslLineExtnClockType=_DsAdslLineExtnClockType_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,6),_DsAdslLineExtnClockType_Type())
dsAdslLineExtnClockType.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineExtnClockType.setStatus(_A)
class _DsAdslLineExtnLineDmtTrellis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trellisOn',1),('trellisOff',2)))
_DsAdslLineExtnLineDmtTrellis_Type.__name__=_C
_DsAdslLineExtnLineDmtTrellis_Object=MibTableColumn
dsAdslLineExtnLineDmtTrellis=_DsAdslLineExtnLineDmtTrellis_Object((1,3,6,1,4,1,6296,9,5,1,1,3,1,7),_DsAdslLineExtnLineDmtTrellis_Type())
dsAdslLineExtnLineDmtTrellis.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineExtnLineDmtTrellis.setStatus(_A)
_DsAdslAtucPhysExtnTable_Object=MibTable
dsAdslAtucPhysExtnTable=_DsAdslAtucPhysExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,4))
if mibBuilder.loadTexts:dsAdslAtucPhysExtnTable.setStatus(_A)
_DsAdslAtucPhysExtnEntry_Object=MibTableRow
dsAdslAtucPhysExtnEntry=_DsAdslAtucPhysExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1))
dsAdslAtucPhysExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAtucPhysExtnEntry.setStatus(_A)
class _DsAdslAtucPhysExtnOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,8,16,24,26,27,46,128,131,132,133,139,140)));namedValues=NamedValues(*(('idle',0),('data',1),('bootupLoad',8),('handshake',16),('training',24),('framerSync',26),('fastRetrainInProg',27),('discovery',46),('llTest',128),('dlTest',131),('txTest',132),('atmLpTest',133),('deltTraining',139),('delt',140)))
_DsAdslAtucPhysExtnOpState_Type.__name__=_C
_DsAdslAtucPhysExtnOpState_Object=MibTableColumn
dsAdslAtucPhysExtnOpState=_DsAdslAtucPhysExtnOpState_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,1),_DsAdslAtucPhysExtnOpState_Type())
dsAdslAtucPhysExtnOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnOpState.setStatus(_A)
class _DsAdslAtucPhysExtnActualStd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,9,26,27,28,29,30,48,64)));namedValues=NamedValues(*(('t1413',0),('gLite',1),('gDmt',2),('alctl14',3),(_A1,4),('adi',5),('alctl',6),('t1413auto',9),('adsl2',26),(_A2,27),('reAdsl2',28),(_A3,29),(_A4,30),('adslPlus',48),(_A5,64)))
_DsAdslAtucPhysExtnActualStd_Type.__name__=_C
_DsAdslAtucPhysExtnActualStd_Object=MibTableColumn
dsAdslAtucPhysExtnActualStd=_DsAdslAtucPhysExtnActualStd_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,2),_DsAdslAtucPhysExtnActualStd_Type())
dsAdslAtucPhysExtnActualStd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnActualStd.setStatus(_A)
_DsAdslAtucPhysExtnBertError_Type=Integer32
_DsAdslAtucPhysExtnBertError_Object=MibTableColumn
dsAdslAtucPhysExtnBertError=_DsAdslAtucPhysExtnBertError_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,3),_DsAdslAtucPhysExtnBertError_Type())
dsAdslAtucPhysExtnBertError.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnBertError.setStatus(_A)
_DsAdslAtucPhysExtnTxAtmCellCounter_Type=Counter32
_DsAdslAtucPhysExtnTxAtmCellCounter_Object=MibTableColumn
dsAdslAtucPhysExtnTxAtmCellCounter=_DsAdslAtucPhysExtnTxAtmCellCounter_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,4),_DsAdslAtucPhysExtnTxAtmCellCounter_Type())
dsAdslAtucPhysExtnTxAtmCellCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnTxAtmCellCounter.setStatus(_A)
_DsAdslAtucPhysExtnRxAtmCellCounter_Type=Integer32
_DsAdslAtucPhysExtnRxAtmCellCounter_Object=MibTableColumn
dsAdslAtucPhysExtnRxAtmCellCounter=_DsAdslAtucPhysExtnRxAtmCellCounter_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,5),_DsAdslAtucPhysExtnRxAtmCellCounter_Type())
dsAdslAtucPhysExtnRxAtmCellCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnRxAtmCellCounter.setStatus(_A)
_DsAdslAtucPhysExtnStartProgress_Type=Integer32
_DsAdslAtucPhysExtnStartProgress_Object=MibTableColumn
dsAdslAtucPhysExtnStartProgress=_DsAdslAtucPhysExtnStartProgress_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,6),_DsAdslAtucPhysExtnStartProgress_Type())
dsAdslAtucPhysExtnStartProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnStartProgress.setStatus(_A)
_DsAdslAtucPhysExtnIdleBertError_Type=Integer32
_DsAdslAtucPhysExtnIdleBertError_Object=MibTableColumn
dsAdslAtucPhysExtnIdleBertError=_DsAdslAtucPhysExtnIdleBertError_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,7),_DsAdslAtucPhysExtnIdleBertError_Type())
dsAdslAtucPhysExtnIdleBertError.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnIdleBertError.setStatus(_A)
_DsAdslAtucPhysExtnIdleBertCells_Type=Integer32
_DsAdslAtucPhysExtnIdleBertCells_Object=MibTableColumn
dsAdslAtucPhysExtnIdleBertCells=_DsAdslAtucPhysExtnIdleBertCells_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,8),_DsAdslAtucPhysExtnIdleBertCells_Type())
dsAdslAtucPhysExtnIdleBertCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnIdleBertCells.setStatus(_A)
class _DsAdslAtucPhysExtnBertSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,128)));namedValues=NamedValues(*(('bertOutOfSync',0),('bertInSync',128)))
_DsAdslAtucPhysExtnBertSync_Type.__name__=_C
_DsAdslAtucPhysExtnBertSync_Object=MibTableColumn
dsAdslAtucPhysExtnBertSync=_DsAdslAtucPhysExtnBertSync_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,9),_DsAdslAtucPhysExtnBertSync_Type())
dsAdslAtucPhysExtnBertSync.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnBertSync.setStatus(_A)
class _DsAdslAtucPhysExtnParametricTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),('fail',1),('dspIfFail',2)))
_DsAdslAtucPhysExtnParametricTestResult_Type.__name__=_C
_DsAdslAtucPhysExtnParametricTestResult_Object=MibTableColumn
dsAdslAtucPhysExtnParametricTestResult=_DsAdslAtucPhysExtnParametricTestResult_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,10),_DsAdslAtucPhysExtnParametricTestResult_Type())
dsAdslAtucPhysExtnParametricTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnParametricTestResult.setStatus(_A)
class _DsAdslAtucPhysExtnDataBoostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,32768)));namedValues=NamedValues(*(('disabled',0),('enabled',32768)))
_DsAdslAtucPhysExtnDataBoostStatus_Type.__name__=_C
_DsAdslAtucPhysExtnDataBoostStatus_Object=MibTableColumn
dsAdslAtucPhysExtnDataBoostStatus=_DsAdslAtucPhysExtnDataBoostStatus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,21),_DsAdslAtucPhysExtnDataBoostStatus_Type())
dsAdslAtucPhysExtnDataBoostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDataBoostStatus.setStatus(_A)
class _DsAdslAtucPhysExtnTestArray_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAtucPhysExtnTestArray_Type.__name__=_H
_DsAdslAtucPhysExtnTestArray_Object=MibTableColumn
dsAdslAtucPhysExtnTestArray=_DsAdslAtucPhysExtnTestArray_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,22),_DsAdslAtucPhysExtnTestArray_Type())
dsAdslAtucPhysExtnTestArray.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnTestArray.setStatus(_A)
_DsAdslAtucPhysExtnChanPerfCD_Type=Integer32
_DsAdslAtucPhysExtnChanPerfCD_Object=MibTableColumn
dsAdslAtucPhysExtnChanPerfCD=_DsAdslAtucPhysExtnChanPerfCD_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,23),_DsAdslAtucPhysExtnChanPerfCD_Type())
dsAdslAtucPhysExtnChanPerfCD.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnChanPerfCD.setStatus(_A)
_DsAdslAtucPhysExtnChanPerfBE_Type=Integer32
_DsAdslAtucPhysExtnChanPerfBE_Object=MibTableColumn
dsAdslAtucPhysExtnChanPerfBE=_DsAdslAtucPhysExtnChanPerfBE_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,24),_DsAdslAtucPhysExtnChanPerfBE_Type())
dsAdslAtucPhysExtnChanPerfBE.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnChanPerfBE.setStatus(_A)
_DsAdslAtucPhysExtnDeltHLINSCus_Type=Integer32
_DsAdslAtucPhysExtnDeltHLINSCus_Object=MibTableColumn
dsAdslAtucPhysExtnDeltHLINSCus=_DsAdslAtucPhysExtnDeltHLINSCus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,25),_DsAdslAtucPhysExtnDeltHLINSCus_Type())
dsAdslAtucPhysExtnDeltHLINSCus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltHLINSCus.setStatus(_A)
class _DsAdslAtucPhysExtnDeltHLINpsus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAtucPhysExtnDeltHLINpsus_Type.__name__=_H
_DsAdslAtucPhysExtnDeltHLINpsus_Object=MibTableColumn
dsAdslAtucPhysExtnDeltHLINpsus=_DsAdslAtucPhysExtnDeltHLINpsus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,26),_DsAdslAtucPhysExtnDeltHLINpsus_Type())
dsAdslAtucPhysExtnDeltHLINpsus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltHLINpsus.setStatus(_A)
_DsAdslAtucPhysExtnDeltHLOGMTus_Type=Integer32
_DsAdslAtucPhysExtnDeltHLOGMTus_Object=MibTableColumn
dsAdslAtucPhysExtnDeltHLOGMTus=_DsAdslAtucPhysExtnDeltHLOGMTus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,27),_DsAdslAtucPhysExtnDeltHLOGMTus_Type())
dsAdslAtucPhysExtnDeltHLOGMTus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltHLOGMTus.setStatus(_A)
class _DsAdslAtucPhysExtnDeltHLOGpsus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAtucPhysExtnDeltHLOGpsus_Type.__name__=_H
_DsAdslAtucPhysExtnDeltHLOGpsus_Object=MibTableColumn
dsAdslAtucPhysExtnDeltHLOGpsus=_DsAdslAtucPhysExtnDeltHLOGpsus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,28),_DsAdslAtucPhysExtnDeltHLOGpsus_Type())
dsAdslAtucPhysExtnDeltHLOGpsus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltHLOGpsus.setStatus(_A)
_DsAdslAtucPhysExtnDeltQLNMTus_Type=Integer32
_DsAdslAtucPhysExtnDeltQLNMTus_Object=MibTableColumn
dsAdslAtucPhysExtnDeltQLNMTus=_DsAdslAtucPhysExtnDeltQLNMTus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,29),_DsAdslAtucPhysExtnDeltQLNMTus_Type())
dsAdslAtucPhysExtnDeltQLNMTus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltQLNMTus.setStatus(_A)
class _DsAdslAtucPhysExtnDeltQLNpsus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAtucPhysExtnDeltQLNpsus_Type.__name__=_H
_DsAdslAtucPhysExtnDeltQLNpsus_Object=MibTableColumn
dsAdslAtucPhysExtnDeltQLNpsus=_DsAdslAtucPhysExtnDeltQLNpsus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,30),_DsAdslAtucPhysExtnDeltQLNpsus_Type())
dsAdslAtucPhysExtnDeltQLNpsus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltQLNpsus.setStatus(_A)
class _DsAdslAtucPhysExtnDeltLastTxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)));namedValues=NamedValues(*(('dmtatucg9941',0),('dmtatucquiet1',1),('dmtatuccomb1',2),('dmtatucquiet2',3),('dmtatuccomb2',4),('dmtatucicomb1',5),('dmtatuclineprob',6),('dmtatucquiet3',7),('dmtatuccomb3',8),('dmtatucicomb2',9),('dmtatucmsgfmt',10),('dmtatucmsgpcb',11),('dmtatucquiet4',12),('dmtatucreverb1',13),('dmtatuctref1',14),('dmtatucreverb2',15),('dmtatucect',16),('dmtatucreverb3',17),('dmtatuctref2',18),('dmtatucreverb4',19),('dmtatucsegue1',20),('dmtatucmsg1',21),('dmtatucreverb5',22),('dmtatucsegue2',23),('dmtatucmedley',24),('dmtatucexchmarker',25),('dmtatucmsg2',26),('dmtatucreverb6',27),('dmtatucsegue3',28),('dmtatucparams',29),('dmtatucreverb7',30),('dmtatucsegue4',31),('dmtatucshowtime',32)))
_DsAdslAtucPhysExtnDeltLastTxState_Type.__name__=_C
_DsAdslAtucPhysExtnDeltLastTxState_Object=MibTableColumn
dsAdslAtucPhysExtnDeltLastTxState=_DsAdslAtucPhysExtnDeltLastTxState_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,31),_DsAdslAtucPhysExtnDeltLastTxState_Type())
dsAdslAtucPhysExtnDeltLastTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnDeltLastTxState.setStatus(_A)
class _DsAdslAtucPhysExtnPMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,141)));namedValues=NamedValues(*(('idleop',0),('dataop',1),('l2op',141)))
_DsAdslAtucPhysExtnPMState_Type.__name__=_C
_DsAdslAtucPhysExtnPMState_Object=MibTableColumn
dsAdslAtucPhysExtnPMState=_DsAdslAtucPhysExtnPMState_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,32),_DsAdslAtucPhysExtnPMState_Type())
dsAdslAtucPhysExtnPMState.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnPMState.setStatus(_A)
_DsAdslAtucPhysExtnChanPerfCU_Type=Integer32
_DsAdslAtucPhysExtnChanPerfCU_Object=MibTableColumn
dsAdslAtucPhysExtnChanPerfCU=_DsAdslAtucPhysExtnChanPerfCU_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,33),_DsAdslAtucPhysExtnChanPerfCU_Type())
dsAdslAtucPhysExtnChanPerfCU.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnChanPerfCU.setStatus(_A)
class _DsAdslAtucPhysExtnExtendedPsdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,32768)));namedValues=NamedValues(*(('standard',0),('jj100',1),('extended',32768)))
_DsAdslAtucPhysExtnExtendedPsdStatus_Type.__name__=_C
_DsAdslAtucPhysExtnExtendedPsdStatus_Object=MibTableColumn
dsAdslAtucPhysExtnExtendedPsdStatus=_DsAdslAtucPhysExtnExtendedPsdStatus_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,34),_DsAdslAtucPhysExtnExtendedPsdStatus_Type())
dsAdslAtucPhysExtnExtendedPsdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnExtendedPsdStatus.setStatus(_A)
_DsAdslAtucPhysExtnChipVersion_Type=Integer32
_DsAdslAtucPhysExtnChipVersion_Object=MibTableColumn
dsAdslAtucPhysExtnChipVersion=_DsAdslAtucPhysExtnChipVersion_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,35),_DsAdslAtucPhysExtnChipVersion_Type())
dsAdslAtucPhysExtnChipVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnChipVersion.setStatus(_A)
_DsAdslAtucPhysExtnPilotTone_Type=Integer32
_DsAdslAtucPhysExtnPilotTone_Object=MibTableColumn
dsAdslAtucPhysExtnPilotTone=_DsAdslAtucPhysExtnPilotTone_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,36),_DsAdslAtucPhysExtnPilotTone_Type())
dsAdslAtucPhysExtnPilotTone.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnPilotTone.setStatus(_A)
_DsAdslAtucMSGds_Type=Gauge32
_DsAdslAtucMSGds_Object=MibTableColumn
dsAdslAtucMSGds=_DsAdslAtucMSGds_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,37),_DsAdslAtucMSGds_Type())
dsAdslAtucMSGds.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucMSGds.setStatus(_A)
class _DsAdslAtucPhysExtnPsdMaskMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,32768,32771,32772,49152)));namedValues=NamedValues(*((_Q,0),('hsadslM1',3),('hsadslM2',4),('msk2Rfi',32768),(_A6,32771),(_A7,32772),('coMsk2Rfi0',49152)))
_DsAdslAtucPhysExtnPsdMaskMode_Type.__name__=_C
_DsAdslAtucPhysExtnPsdMaskMode_Object=MibTableColumn
dsAdslAtucPhysExtnPsdMaskMode=_DsAdslAtucPhysExtnPsdMaskMode_Object((1,3,6,1,4,1,6296,9,5,1,1,4,1,38),_DsAdslAtucPhysExtnPsdMaskMode_Type())
dsAdslAtucPhysExtnPsdMaskMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPhysExtnPsdMaskMode.setStatus(_A)
_DsAdslAturPhysExtnTable_Object=MibTable
dsAdslAturPhysExtnTable=_DsAdslAturPhysExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,5))
if mibBuilder.loadTexts:dsAdslAturPhysExtnTable.setStatus(_A)
_DsAdslAturPhysExtnEntry_Object=MibTableRow
dsAdslAturPhysExtnEntry=_DsAdslAturPhysExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1))
dsAdslAturPhysExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAturPhysExtnEntry.setStatus(_A)
class _DsAdslAturPhysExtnConfig_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DsAdslAturPhysExtnConfig_Type.__name__=_H
_DsAdslAturPhysExtnConfig_Object=MibTableColumn
dsAdslAturPhysExtnConfig=_DsAdslAturPhysExtnConfig_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,1),_DsAdslAturPhysExtnConfig_Type())
dsAdslAturPhysExtnConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnConfig.setStatus(_A)
_DsAdslAturPhysExtnChanPerfCD_Type=Integer32
_DsAdslAturPhysExtnChanPerfCD_Object=MibTableColumn
dsAdslAturPhysExtnChanPerfCD=_DsAdslAturPhysExtnChanPerfCD_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,2),_DsAdslAturPhysExtnChanPerfCD_Type())
dsAdslAturPhysExtnChanPerfCD.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnChanPerfCD.setStatus(_A)
_DsAdslAturPhysExtnChanPerfCU_Type=Integer32
_DsAdslAturPhysExtnChanPerfCU_Object=MibTableColumn
dsAdslAturPhysExtnChanPerfCU=_DsAdslAturPhysExtnChanPerfCU_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,3),_DsAdslAturPhysExtnChanPerfCU_Type())
dsAdslAturPhysExtnChanPerfCU.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnChanPerfCU.setStatus(_A)
_DsAdslAturPhysExtnChanPerfBE_Type=Integer32
_DsAdslAturPhysExtnChanPerfBE_Object=MibTableColumn
dsAdslAturPhysExtnChanPerfBE=_DsAdslAturPhysExtnChanPerfBE_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,4),_DsAdslAturPhysExtnChanPerfBE_Type())
dsAdslAturPhysExtnChanPerfBE.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnChanPerfBE.setStatus(_A)
_DsAdslAturPhysExtnDeltHLINSCds_Type=Integer32
_DsAdslAturPhysExtnDeltHLINSCds_Object=MibTableColumn
dsAdslAturPhysExtnDeltHLINSCds=_DsAdslAturPhysExtnDeltHLINSCds_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,5),_DsAdslAturPhysExtnDeltHLINSCds_Type())
dsAdslAturPhysExtnDeltHLINSCds.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltHLINSCds.setStatus(_A)
class _DsAdslAturPhysExtnDeltHLINpsds_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAturPhysExtnDeltHLINpsds_Type.__name__=_H
_DsAdslAturPhysExtnDeltHLINpsds_Object=MibTableColumn
dsAdslAturPhysExtnDeltHLINpsds=_DsAdslAturPhysExtnDeltHLINpsds_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,6),_DsAdslAturPhysExtnDeltHLINpsds_Type())
dsAdslAturPhysExtnDeltHLINpsds.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltHLINpsds.setStatus(_A)
_DsAdslAturPhysExtnDeltHLOGMTds_Type=Integer32
_DsAdslAturPhysExtnDeltHLOGMTds_Object=MibTableColumn
dsAdslAturPhysExtnDeltHLOGMTds=_DsAdslAturPhysExtnDeltHLOGMTds_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,7),_DsAdslAturPhysExtnDeltHLOGMTds_Type())
dsAdslAturPhysExtnDeltHLOGMTds.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltHLOGMTds.setStatus(_A)
class _DsAdslAturPhysExtnDeltHLOGpsus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAturPhysExtnDeltHLOGpsus_Type.__name__=_H
_DsAdslAturPhysExtnDeltHLOGpsus_Object=MibTableColumn
dsAdslAturPhysExtnDeltHLOGpsus=_DsAdslAturPhysExtnDeltHLOGpsus_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,8),_DsAdslAturPhysExtnDeltHLOGpsus_Type())
dsAdslAturPhysExtnDeltHLOGpsus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltHLOGpsus.setStatus(_A)
_DsAdslAturPhysExtnDeltQLNMTds_Type=Integer32
_DsAdslAturPhysExtnDeltQLNMTds_Object=MibTableColumn
dsAdslAturPhysExtnDeltQLNMTds=_DsAdslAturPhysExtnDeltQLNMTds_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,9),_DsAdslAturPhysExtnDeltQLNMTds_Type())
dsAdslAturPhysExtnDeltQLNMTds.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltQLNMTds.setStatus(_A)
class _DsAdslAturPhysExtnDeltQLNpsds_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,42))
_DsAdslAturPhysExtnDeltQLNpsds_Type.__name__=_H
_DsAdslAturPhysExtnDeltQLNpsds_Object=MibTableColumn
dsAdslAturPhysExtnDeltQLNpsds=_DsAdslAturPhysExtnDeltQLNpsds_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,10),_DsAdslAturPhysExtnDeltQLNpsds_Type())
dsAdslAturPhysExtnDeltQLNpsds.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltQLNpsds.setStatus(_A)
class _DsAdslAturPhysExtnDeltLastTxState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('dmtaturg9941',0),('dmtaturquiet1',1),('dmtaturcomb1',2),('dmtaturquiet2',3),('dmtaturcomb2',4),('dmtaturicomb1',5),('dmtaturlineprob',6),('dmtaturquiet3',7),('dmtaturcomb3',8),('dmtaturicomb2',9),('dmtaturmsgfmt',10),('dmtaturmsgpcb',11),('dmtaturreverb1',12),('dmtaturquiet4',13),('dmtaturreverb2',14),('dmtaturquiet5',15),('dmtaturreverb3',16),('dmtaturect',17),('dmtaturreverb4',18),('dmtatursegue1',19),('dmtaturreverb5',20),('dmtatursegue2',21),('dmtaturmsg1',22),('dmtaturmedley',23),('dmtaturexchmarker',24),('dmtaturmsg2',25),('dmtaturreverb6',26),('dmtatursegue3',27),('dmtaturparams',28),('dmtaturreverb7',29),('dmtatursegue4',30),('dmtaturshowtime',31)))
_DsAdslAturPhysExtnDeltLastTxState_Type.__name__=_C
_DsAdslAturPhysExtnDeltLastTxState_Object=MibTableColumn
dsAdslAturPhysExtnDeltLastTxState=_DsAdslAturPhysExtnDeltLastTxState_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,11),_DsAdslAturPhysExtnDeltLastTxState_Type())
dsAdslAturPhysExtnDeltLastTxState.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPhysExtnDeltLastTxState.setStatus(_A)
_DsAdslAturMSGus_Type=Gauge32
_DsAdslAturMSGus_Object=MibTableColumn
dsAdslAturMSGus=_DsAdslAturMSGus_Object((1,3,6,1,4,1,6296,9,5,1,1,5,1,12),_DsAdslAturMSGus_Type())
dsAdslAturMSGus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturMSGus.setStatus(_A)
_DsAdslAtucChanExtnTable_Object=MibTable
dsAdslAtucChanExtnTable=_DsAdslAtucChanExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,6))
if mibBuilder.loadTexts:dsAdslAtucChanExtnTable.setStatus(_A)
_DsAdslAtucChanExtnEntry_Object=MibTableRow
dsAdslAtucChanExtnEntry=_DsAdslAtucChanExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,6,1))
dsAdslAtucChanExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAtucChanExtnEntry.setStatus(_A)
class _DsAdslAtucChanExtnCurrAtmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_A8,0),(_A9,1),(_AA,2)))
_DsAdslAtucChanExtnCurrAtmStatus_Type.__name__=_C
_DsAdslAtucChanExtnCurrAtmStatus_Object=MibTableColumn
dsAdslAtucChanExtnCurrAtmStatus=_DsAdslAtucChanExtnCurrAtmStatus_Object((1,3,6,1,4,1,6296,9,5,1,1,6,1,1),_DsAdslAtucChanExtnCurrAtmStatus_Type())
dsAdslAtucChanExtnCurrAtmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanExtnCurrAtmStatus.setStatus(_A)
_DsAdslAtucChanExtnRsSymbols_Type=Integer32
_DsAdslAtucChanExtnRsSymbols_Object=MibTableColumn
dsAdslAtucChanExtnRsSymbols=_DsAdslAtucChanExtnRsSymbols_Object((1,3,6,1,4,1,6296,9,5,1,1,6,1,2),_DsAdslAtucChanExtnRsSymbols_Type())
dsAdslAtucChanExtnRsSymbols.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanExtnRsSymbols.setStatus(_A)
_DsAdslAtucChanExtnRsDepth_Type=Integer32
_DsAdslAtucChanExtnRsDepth_Object=MibTableColumn
dsAdslAtucChanExtnRsDepth=_DsAdslAtucChanExtnRsDepth_Object((1,3,6,1,4,1,6296,9,5,1,1,6,1,3),_DsAdslAtucChanExtnRsDepth_Type())
dsAdslAtucChanExtnRsDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanExtnRsDepth.setStatus(_A)
_DsAdslAtucChanExtnRsRedundancy_Type=Integer32
_DsAdslAtucChanExtnRsRedundancy_Object=MibTableColumn
dsAdslAtucChanExtnRsRedundancy=_DsAdslAtucChanExtnRsRedundancy_Object((1,3,6,1,4,1,6296,9,5,1,1,6,1,4),_DsAdslAtucChanExtnRsRedundancy_Type())
dsAdslAtucChanExtnRsRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanExtnRsRedundancy.setStatus(_A)
_DsAdslAturChanExtnTable_Object=MibTable
dsAdslAturChanExtnTable=_DsAdslAturChanExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,7))
if mibBuilder.loadTexts:dsAdslAturChanExtnTable.setStatus(_A)
_DsAdslAturChanExtnEntry_Object=MibTableRow
dsAdslAturChanExtnEntry=_DsAdslAturChanExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,7,1))
dsAdslAturChanExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAturChanExtnEntry.setStatus(_A)
class _DsAdslAturChanExtnCurrAtmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_A8,0),(_A9,1),(_AA,2)))
_DsAdslAturChanExtnCurrAtmStatus_Type.__name__=_C
_DsAdslAturChanExtnCurrAtmStatus_Object=MibTableColumn
dsAdslAturChanExtnCurrAtmStatus=_DsAdslAturChanExtnCurrAtmStatus_Object((1,3,6,1,4,1,6296,9,5,1,1,7,1,1),_DsAdslAturChanExtnCurrAtmStatus_Type())
dsAdslAturChanExtnCurrAtmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanExtnCurrAtmStatus.setStatus(_A)
_DsAdslAturChanExtnRsSymbols_Type=Unsigned32
_DsAdslAturChanExtnRsSymbols_Object=MibTableColumn
dsAdslAturChanExtnRsSymbols=_DsAdslAturChanExtnRsSymbols_Object((1,3,6,1,4,1,6296,9,5,1,1,7,1,2),_DsAdslAturChanExtnRsSymbols_Type())
dsAdslAturChanExtnRsSymbols.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanExtnRsSymbols.setStatus(_A)
_DsAdslAturChanExtnRsDepth_Type=Unsigned32
_DsAdslAturChanExtnRsDepth_Object=MibTableColumn
dsAdslAturChanExtnRsDepth=_DsAdslAturChanExtnRsDepth_Object((1,3,6,1,4,1,6296,9,5,1,1,7,1,3),_DsAdslAturChanExtnRsDepth_Type())
dsAdslAturChanExtnRsDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanExtnRsDepth.setStatus(_A)
_DsAdslAturChanExtnRsRedundancy_Type=Unsigned32
_DsAdslAturChanExtnRsRedundancy_Object=MibTableColumn
dsAdslAturChanExtnRsRedundancy=_DsAdslAturChanExtnRsRedundancy_Object((1,3,6,1,4,1,6296,9,5,1,1,7,1,4),_DsAdslAturChanExtnRsRedundancy_Type())
dsAdslAturChanExtnRsRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanExtnRsRedundancy.setStatus(_A)
_DsAdslAtucPerfDataExtnTable_Object=MibTable
dsAdslAtucPerfDataExtnTable=_DsAdslAtucPerfDataExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,8))
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnTable.setStatus(_A)
_DsAdslAtucPerfDataExtnEntry_Object=MibTableRow
dsAdslAtucPerfDataExtnEntry=_DsAdslAtucPerfDataExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1))
dsAdslAtucPerfDataExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnEntry.setStatus(_A)
_DsAdslAtucPerfDataExtnStatFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnStatFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnStatFastR=_DsAdslAtucPerfDataExtnStatFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,1),_DsAdslAtucPerfDataExtnStatFastR_Type())
dsAdslAtucPerfDataExtnStatFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnStatFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnStatFailedFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnStatFailedFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnStatFailedFastR=_DsAdslAtucPerfDataExtnStatFailedFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,2),_DsAdslAtucPerfDataExtnStatFailedFastR_Type())
dsAdslAtucPerfDataExtnStatFailedFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnStatFailedFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnStatSesL_Type=Gauge32
_DsAdslAtucPerfDataExtnStatSesL_Object=MibTableColumn
dsAdslAtucPerfDataExtnStatSesL=_DsAdslAtucPerfDataExtnStatSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,3),_DsAdslAtucPerfDataExtnStatSesL_Type())
dsAdslAtucPerfDataExtnStatSesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnStatSesL.setStatus(_A)
_DsAdslAtucPerfDataExtnStatUasL_Type=Gauge32
_DsAdslAtucPerfDataExtnStatUasL_Object=MibTableColumn
dsAdslAtucPerfDataExtnStatUasL=_DsAdslAtucPerfDataExtnStatUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,4),_DsAdslAtucPerfDataExtnStatUasL_Type())
dsAdslAtucPerfDataExtnStatUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnStatUasL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr15MinFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr15MinFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinFastR=_DsAdslAtucPerfDataExtnCurr15MinFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,5),_DsAdslAtucPerfDataExtnCurr15MinFastR_Type())
dsAdslAtucPerfDataExtnCurr15MinFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr15MinFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinFailedFastR=_DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,6),_DsAdslAtucPerfDataExtnCurr15MinFailedFastR_Type())
dsAdslAtucPerfDataExtnCurr15MinFailedFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr15MinFailedFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr15MinSesL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr15MinSesL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinSesL=_DsAdslAtucPerfDataExtnCurr15MinSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,7),_DsAdslAtucPerfDataExtnCurr15MinSesL_Type())
dsAdslAtucPerfDataExtnCurr15MinSesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr15MinSesL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr15MinUasL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr15MinUasL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinUasL=_DsAdslAtucPerfDataExtnCurr15MinUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,8),_DsAdslAtucPerfDataExtnCurr15MinUasL_Type())
dsAdslAtucPerfDataExtnCurr15MinUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr15MinUasL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr1DayFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr1DayFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayFastR=_DsAdslAtucPerfDataExtnCurr1DayFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,9),_DsAdslAtucPerfDataExtnCurr1DayFastR_Type())
dsAdslAtucPerfDataExtnCurr1DayFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr1DayFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayFailedFastR=_DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,10),_DsAdslAtucPerfDataExtnCurr1DayFailedFastR_Type())
dsAdslAtucPerfDataExtnCurr1DayFailedFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr1DayFailedFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr1DaySesL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr1DaySesL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr1DaySesL=_DsAdslAtucPerfDataExtnCurr1DaySesL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,11),_DsAdslAtucPerfDataExtnCurr1DaySesL_Type())
dsAdslAtucPerfDataExtnCurr1DaySesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr1DaySesL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr1DayUasL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr1DayUasL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayUasL=_DsAdslAtucPerfDataExtnCurr1DayUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,12),_DsAdslAtucPerfDataExtnCurr1DayUasL_Type())
dsAdslAtucPerfDataExtnCurr1DayUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr1DayUasL.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DayFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DayFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayFastR=_DsAdslAtucPerfDataExtnPrev1DayFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,13),_DsAdslAtucPerfDataExtnPrev1DayFastR_Type())
dsAdslAtucPerfDataExtnPrev1DayFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DayFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayFailedFastR=_DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,14),_DsAdslAtucPerfDataExtnPrev1DayFailedFastR_Type())
dsAdslAtucPerfDataExtnPrev1DayFailedFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DayFailedFastR.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DaySesL_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DaySesL_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DaySesL=_DsAdslAtucPerfDataExtnPrev1DaySesL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,15),_DsAdslAtucPerfDataExtnPrev1DaySesL_Type())
dsAdslAtucPerfDataExtnPrev1DaySesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DaySesL.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DayUasL_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DayUasL_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayUasL=_DsAdslAtucPerfDataExtnPrev1DayUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,16),_DsAdslAtucPerfDataExtnPrev1DayUasL_Type())
dsAdslAtucPerfDataExtnPrev1DayUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DayUasL.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayTimeElapsed=_DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,17),_DsAdslAtucPerfDataExtnPrev1DayTimeElapsed_Type())
dsAdslAtucPerfDataExtnPrev1DayTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DayTimeElapsed.setStatus(_A)
_DsAdslAtucPerfDataExtnStatFecsL_Type=Gauge32
_DsAdslAtucPerfDataExtnStatFecsL_Object=MibTableColumn
dsAdslAtucPerfDataExtnStatFecsL=_DsAdslAtucPerfDataExtnStatFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,18),_DsAdslAtucPerfDataExtnStatFecsL_Type())
dsAdslAtucPerfDataExtnStatFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnStatFecsL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr15MinFecsL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr15MinFecsL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinFecsL=_DsAdslAtucPerfDataExtnCurr15MinFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,19),_DsAdslAtucPerfDataExtnCurr15MinFecsL_Type())
dsAdslAtucPerfDataExtnCurr15MinFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr15MinFecsL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr1DayFecsL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr1DayFecsL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayFecsL=_DsAdslAtucPerfDataExtnCurr1DayFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,20),_DsAdslAtucPerfDataExtnCurr1DayFecsL_Type())
dsAdslAtucPerfDataExtnCurr1DayFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr1DayFecsL.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DayFecsL_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DayFecsL_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayFecsL=_DsAdslAtucPerfDataExtnPrev1DayFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,21),_DsAdslAtucPerfDataExtnPrev1DayFecsL_Type())
dsAdslAtucPerfDataExtnPrev1DayFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DayFecsL.setStatus(_A)
_DsAdslAtucPerfDataExtnStatLossL_Type=Gauge32
_DsAdslAtucPerfDataExtnStatLossL_Object=MibTableColumn
dsAdslAtucPerfDataExtnStatLossL=_DsAdslAtucPerfDataExtnStatLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,22),_DsAdslAtucPerfDataExtnStatLossL_Type())
dsAdslAtucPerfDataExtnStatLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnStatLossL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr15MinLossL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr15MinLossL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr15MinLossL=_DsAdslAtucPerfDataExtnCurr15MinLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,23),_DsAdslAtucPerfDataExtnCurr15MinLossL_Type())
dsAdslAtucPerfDataExtnCurr15MinLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr15MinLossL.setStatus(_A)
_DsAdslAtucPerfDataExtnCurr1DayLossL_Type=Gauge32
_DsAdslAtucPerfDataExtnCurr1DayLossL_Object=MibTableColumn
dsAdslAtucPerfDataExtnCurr1DayLossL=_DsAdslAtucPerfDataExtnCurr1DayLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,24),_DsAdslAtucPerfDataExtnCurr1DayLossL_Type())
dsAdslAtucPerfDataExtnCurr1DayLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnCurr1DayLossL.setStatus(_A)
_DsAdslAtucPerfDataExtnPrev1DayLossL_Type=Gauge32
_DsAdslAtucPerfDataExtnPrev1DayLossL_Object=MibTableColumn
dsAdslAtucPerfDataExtnPrev1DayLossL=_DsAdslAtucPerfDataExtnPrev1DayLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,8,1,25),_DsAdslAtucPerfDataExtnPrev1DayLossL_Type())
dsAdslAtucPerfDataExtnPrev1DayLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucPerfDataExtnPrev1DayLossL.setStatus(_A)
_DsAdslAturPerfDataExtnTable_Object=MibTable
dsAdslAturPerfDataExtnTable=_DsAdslAturPerfDataExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,9))
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnTable.setStatus(_A)
_DsAdslAturPerfDataExtnEntry_Object=MibTableRow
dsAdslAturPerfDataExtnEntry=_DsAdslAturPerfDataExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1))
dsAdslAturPerfDataExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnEntry.setStatus(_A)
_DsAdslAturPerfDataExtnStatSesL_Type=Counter32
_DsAdslAturPerfDataExtnStatSesL_Object=MibTableColumn
dsAdslAturPerfDataExtnStatSesL=_DsAdslAturPerfDataExtnStatSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,1),_DsAdslAturPerfDataExtnStatSesL_Type())
dsAdslAturPerfDataExtnStatSesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnStatSesL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr15MinSesL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr15MinSesL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr15MinSesL=_DsAdslAturPerfDataExtnCurr15MinSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,2),_DsAdslAturPerfDataExtnCurr15MinSesL_Type())
dsAdslAturPerfDataExtnCurr15MinSesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr15MinSesL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr1DaySesL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr1DaySesL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr1DaySesL=_DsAdslAturPerfDataExtnCurr1DaySesL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,3),_DsAdslAturPerfDataExtnCurr1DaySesL_Type())
dsAdslAturPerfDataExtnCurr1DaySesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr1DaySesL.setStatus(_A)
_DsAdslAturPerfDataExtnPrev1DaySesL_Type=Gauge32
_DsAdslAturPerfDataExtnPrev1DaySesL_Object=MibTableColumn
dsAdslAturPerfDataExtnPrev1DaySesL=_DsAdslAturPerfDataExtnPrev1DaySesL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,4),_DsAdslAturPerfDataExtnPrev1DaySesL_Type())
dsAdslAturPerfDataExtnPrev1DaySesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnPrev1DaySesL.setStatus(_A)
_DsAdslAturPerfDataExtnStatUasL_Type=Counter32
_DsAdslAturPerfDataExtnStatUasL_Object=MibTableColumn
dsAdslAturPerfDataExtnStatUasL=_DsAdslAturPerfDataExtnStatUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,5),_DsAdslAturPerfDataExtnStatUasL_Type())
dsAdslAturPerfDataExtnStatUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnStatUasL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr15MinUasL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr15MinUasL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr15MinUasL=_DsAdslAturPerfDataExtnCurr15MinUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,6),_DsAdslAturPerfDataExtnCurr15MinUasL_Type())
dsAdslAturPerfDataExtnCurr15MinUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr15MinUasL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr1DayUasL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr1DayUasL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr1DayUasL=_DsAdslAturPerfDataExtnCurr1DayUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,7),_DsAdslAturPerfDataExtnCurr1DayUasL_Type())
dsAdslAturPerfDataExtnCurr1DayUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr1DayUasL.setStatus(_A)
_DsAdslAturPerfDataExtnPrev1DayUasL_Type=Gauge32
_DsAdslAturPerfDataExtnPrev1DayUasL_Object=MibTableColumn
dsAdslAturPerfDataExtnPrev1DayUasL=_DsAdslAturPerfDataExtnPrev1DayUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,8),_DsAdslAturPerfDataExtnPrev1DayUasL_Type())
dsAdslAturPerfDataExtnPrev1DayUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnPrev1DayUasL.setStatus(_A)
_DsAdslAturPerfDataExtnStatFecsL_Type=Counter32
_DsAdslAturPerfDataExtnStatFecsL_Object=MibTableColumn
dsAdslAturPerfDataExtnStatFecsL=_DsAdslAturPerfDataExtnStatFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,9),_DsAdslAturPerfDataExtnStatFecsL_Type())
dsAdslAturPerfDataExtnStatFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnStatFecsL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr15MinFecsL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr15MinFecsL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr15MinFecsL=_DsAdslAturPerfDataExtnCurr15MinFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,10),_DsAdslAturPerfDataExtnCurr15MinFecsL_Type())
dsAdslAturPerfDataExtnCurr15MinFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr15MinFecsL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr1DayFecsL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr1DayFecsL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr1DayFecsL=_DsAdslAturPerfDataExtnCurr1DayFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,11),_DsAdslAturPerfDataExtnCurr1DayFecsL_Type())
dsAdslAturPerfDataExtnCurr1DayFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr1DayFecsL.setStatus(_A)
_DsAdslAturPerfDataExtnPrev1DayFecsL_Type=Gauge32
_DsAdslAturPerfDataExtnPrev1DayFecsL_Object=MibTableColumn
dsAdslAturPerfDataExtnPrev1DayFecsL=_DsAdslAturPerfDataExtnPrev1DayFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,12),_DsAdslAturPerfDataExtnPrev1DayFecsL_Type())
dsAdslAturPerfDataExtnPrev1DayFecsL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnPrev1DayFecsL.setStatus(_A)
_DsAdslAturPerfDataExtnStatLossL_Type=Counter32
_DsAdslAturPerfDataExtnStatLossL_Object=MibTableColumn
dsAdslAturPerfDataExtnStatLossL=_DsAdslAturPerfDataExtnStatLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,13),_DsAdslAturPerfDataExtnStatLossL_Type())
dsAdslAturPerfDataExtnStatLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnStatLossL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr15MinLossL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr15MinLossL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr15MinLossL=_DsAdslAturPerfDataExtnCurr15MinLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,14),_DsAdslAturPerfDataExtnCurr15MinLossL_Type())
dsAdslAturPerfDataExtnCurr15MinLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr15MinLossL.setStatus(_A)
_DsAdslAturPerfDataExtnCurr1DayLossL_Type=Gauge32
_DsAdslAturPerfDataExtnCurr1DayLossL_Object=MibTableColumn
dsAdslAturPerfDataExtnCurr1DayLossL=_DsAdslAturPerfDataExtnCurr1DayLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,15),_DsAdslAturPerfDataExtnCurr1DayLossL_Type())
dsAdslAturPerfDataExtnCurr1DayLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnCurr1DayLossL.setStatus(_A)
_DsAdslAturPerfDataExtnPrev1DayLossL_Type=Gauge32
_DsAdslAturPerfDataExtnPrev1DayLossL_Object=MibTableColumn
dsAdslAturPerfDataExtnPrev1DayLossL=_DsAdslAturPerfDataExtnPrev1DayLossL_Object((1,3,6,1,4,1,6296,9,5,1,1,9,1,16),_DsAdslAturPerfDataExtnPrev1DayLossL_Type())
dsAdslAturPerfDataExtnPrev1DayLossL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturPerfDataExtnPrev1DayLossL.setStatus(_A)
_DsAdslAtucIntervalExtnTable_Object=MibTable
dsAdslAtucIntervalExtnTable=_DsAdslAtucIntervalExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,10))
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnTable.setStatus(_A)
_DsAdslAtucIntervalExtnEntry_Object=MibTableRow
dsAdslAtucIntervalExtnEntry=_DsAdslAtucIntervalExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,10,1))
dsAdslAtucIntervalExtnEntry.setIndexNames((0,_F,_G),(0,_J,_Y))
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnEntry.setStatus(_A)
_DsAdslAtucIntervalExtnFastR_Type=Gauge32
_DsAdslAtucIntervalExtnFastR_Object=MibTableColumn
dsAdslAtucIntervalExtnFastR=_DsAdslAtucIntervalExtnFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,10,1,1),_DsAdslAtucIntervalExtnFastR_Type())
dsAdslAtucIntervalExtnFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnFastR.setStatus(_A)
_DsAdslAtucIntervalExtnFailedFastR_Type=Gauge32
_DsAdslAtucIntervalExtnFailedFastR_Object=MibTableColumn
dsAdslAtucIntervalExtnFailedFastR=_DsAdslAtucIntervalExtnFailedFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,10,1,2),_DsAdslAtucIntervalExtnFailedFastR_Type())
dsAdslAtucIntervalExtnFailedFastR.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnFailedFastR.setStatus(_A)
_DsAdslAtucIntervalExtnSesL_Type=Gauge32
_DsAdslAtucIntervalExtnSesL_Object=MibTableColumn
dsAdslAtucIntervalExtnSesL=_DsAdslAtucIntervalExtnSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,10,1,3),_DsAdslAtucIntervalExtnSesL_Type())
dsAdslAtucIntervalExtnSesL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnSesL.setStatus(_A)
_DsAdslAtucIntervalExtnUasL_Type=Gauge32
_DsAdslAtucIntervalExtnUasL_Object=MibTableColumn
dsAdslAtucIntervalExtnUasL=_DsAdslAtucIntervalExtnUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,10,1,4),_DsAdslAtucIntervalExtnUasL_Type())
dsAdslAtucIntervalExtnUasL.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnUasL.setStatus(_A)
_DsAdslAtucIntervalExtnTimeElapsed_Type=Gauge32
_DsAdslAtucIntervalExtnTimeElapsed_Object=MibTableColumn
dsAdslAtucIntervalExtnTimeElapsed=_DsAdslAtucIntervalExtnTimeElapsed_Object((1,3,6,1,4,1,6296,9,5,1,1,10,1,5),_DsAdslAtucIntervalExtnTimeElapsed_Type())
dsAdslAtucIntervalExtnTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucIntervalExtnTimeElapsed.setStatus(_A)
_DsAdslAtucChanPerfDataExtnTable_Object=MibTable
dsAdslAtucChanPerfDataExtnTable=_DsAdslAtucChanPerfDataExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,12))
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnTable.setStatus(_A)
_DsAdslAtucChanPerfDataExtnEntry_Object=MibTableRow
dsAdslAtucChanPerfDataExtnEntry=_DsAdslAtucChanPerfDataExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1))
dsAdslAtucChanPerfDataExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnEntry.setStatus(_A)
_DsAdslAtucChanPerfDataExtnTimeElapsed_Type=Gauge32
_DsAdslAtucChanPerfDataExtnTimeElapsed_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnTimeElapsed=_DsAdslAtucChanPerfDataExtnTimeElapsed_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,1),_DsAdslAtucChanPerfDataExtnTimeElapsed_Type())
dsAdslAtucChanPerfDataExtnTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnTimeElapsed.setStatus(_A)
_DsAdslAtucChanPerfDataExtnNcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnNcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnNcd=_DsAdslAtucChanPerfDataExtnNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,2),_DsAdslAtucChanPerfDataExtnNcd_Type())
dsAdslAtucChanPerfDataExtnNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnNcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnOcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnOcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnOcd=_DsAdslAtucChanPerfDataExtnOcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,3),_DsAdslAtucChanPerfDataExtnOcd_Type())
dsAdslAtucChanPerfDataExtnOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnOcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnHec_Type=Gauge32
_DsAdslAtucChanPerfDataExtnHec_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnHec=_DsAdslAtucChanPerfDataExtnHec_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,4),_DsAdslAtucChanPerfDataExtnHec_Type())
dsAdslAtucChanPerfDataExtnHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnHec.setStatus(_A)
_DsAdslAtucChanPerfDataExtnCurr15MinNcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnCurr15MinNcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnCurr15MinNcd=_DsAdslAtucChanPerfDataExtnCurr15MinNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,5),_DsAdslAtucChanPerfDataExtnCurr15MinNcd_Type())
dsAdslAtucChanPerfDataExtnCurr15MinNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnCurr15MinNcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnCurr15MinOcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnCurr15MinOcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnCurr15MinOcd=_DsAdslAtucChanPerfDataExtnCurr15MinOcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,6),_DsAdslAtucChanPerfDataExtnCurr15MinOcd_Type())
dsAdslAtucChanPerfDataExtnCurr15MinOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnCurr15MinOcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnCurr15MinHec_Type=Gauge32
_DsAdslAtucChanPerfDataExtnCurr15MinHec_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnCurr15MinHec=_DsAdslAtucChanPerfDataExtnCurr15MinHec_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,7),_DsAdslAtucChanPerfDataExtnCurr15MinHec_Type())
dsAdslAtucChanPerfDataExtnCurr15MinHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnCurr15MinHec.setStatus(_A)
_DsAdslAtucChanPerfDataExtnCurr1DayNcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnCurr1DayNcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnCurr1DayNcd=_DsAdslAtucChanPerfDataExtnCurr1DayNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,8),_DsAdslAtucChanPerfDataExtnCurr1DayNcd_Type())
dsAdslAtucChanPerfDataExtnCurr1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnCurr1DayNcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnCurr1DayOcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnCurr1DayOcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnCurr1DayOcd=_DsAdslAtucChanPerfDataExtnCurr1DayOcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,9),_DsAdslAtucChanPerfDataExtnCurr1DayOcd_Type())
dsAdslAtucChanPerfDataExtnCurr1DayOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnCurr1DayOcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnCurr1DayHec_Type=Gauge32
_DsAdslAtucChanPerfDataExtnCurr1DayHec_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnCurr1DayHec=_DsAdslAtucChanPerfDataExtnCurr1DayHec_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,10),_DsAdslAtucChanPerfDataExtnCurr1DayHec_Type())
dsAdslAtucChanPerfDataExtnCurr1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnCurr1DayHec.setStatus(_A)
_DsAdslAtucChanPerfDataExtnPrev1DayNcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnPrev1DayNcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnPrev1DayNcd=_DsAdslAtucChanPerfDataExtnPrev1DayNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,11),_DsAdslAtucChanPerfDataExtnPrev1DayNcd_Type())
dsAdslAtucChanPerfDataExtnPrev1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnPrev1DayNcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnPrev1DayOcd_Type=Gauge32
_DsAdslAtucChanPerfDataExtnPrev1DayOcd_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnPrev1DayOcd=_DsAdslAtucChanPerfDataExtnPrev1DayOcd_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,12),_DsAdslAtucChanPerfDataExtnPrev1DayOcd_Type())
dsAdslAtucChanPerfDataExtnPrev1DayOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnPrev1DayOcd.setStatus(_A)
_DsAdslAtucChanPerfDataExtnPrev1DayHec_Type=Gauge32
_DsAdslAtucChanPerfDataExtnPrev1DayHec_Object=MibTableColumn
dsAdslAtucChanPerfDataExtnPrev1DayHec=_DsAdslAtucChanPerfDataExtnPrev1DayHec_Object((1,3,6,1,4,1,6296,9,5,1,1,12,1,13),_DsAdslAtucChanPerfDataExtnPrev1DayHec_Type())
dsAdslAtucChanPerfDataExtnPrev1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanPerfDataExtnPrev1DayHec.setStatus(_A)
_DsAdslAturChanPerfDataExtnTable_Object=MibTable
dsAdslAturChanPerfDataExtnTable=_DsAdslAturChanPerfDataExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,13))
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnTable.setStatus(_A)
_DsAdslAturChanPerfDataExtnEntry_Object=MibTableRow
dsAdslAturChanPerfDataExtnEntry=_DsAdslAturChanPerfDataExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1))
dsAdslAturChanPerfDataExtnEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnEntry.setStatus(_A)
_DsAdslAturChanPerfDataExtnNcd_Type=Gauge32
_DsAdslAturChanPerfDataExtnNcd_Object=MibTableColumn
dsAdslAturChanPerfDataExtnNcd=_DsAdslAturChanPerfDataExtnNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,1),_DsAdslAturChanPerfDataExtnNcd_Type())
dsAdslAturChanPerfDataExtnNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnNcd.setStatus(_A)
_DsAdslAturChanPerfDataExtnHec_Type=Gauge32
_DsAdslAturChanPerfDataExtnHec_Object=MibTableColumn
dsAdslAturChanPerfDataExtnHec=_DsAdslAturChanPerfDataExtnHec_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,2),_DsAdslAturChanPerfDataExtnHec_Type())
dsAdslAturChanPerfDataExtnHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnHec.setStatus(_A)
_DsAdslAturChanPerfDataExtnCurr15MinNcd_Type=Gauge32
_DsAdslAturChanPerfDataExtnCurr15MinNcd_Object=MibTableColumn
dsAdslAturChanPerfDataExtnCurr15MinNcd=_DsAdslAturChanPerfDataExtnCurr15MinNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,3),_DsAdslAturChanPerfDataExtnCurr15MinNcd_Type())
dsAdslAturChanPerfDataExtnCurr15MinNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnCurr15MinNcd.setStatus(_A)
_DsAdslAturChanPerfDataExtnCurr15MinHec_Type=Gauge32
_DsAdslAturChanPerfDataExtnCurr15MinHec_Object=MibTableColumn
dsAdslAturChanPerfDataExtnCurr15MinHec=_DsAdslAturChanPerfDataExtnCurr15MinHec_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,4),_DsAdslAturChanPerfDataExtnCurr15MinHec_Type())
dsAdslAturChanPerfDataExtnCurr15MinHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnCurr15MinHec.setStatus(_A)
_DsAdslAturChanPerfDataExtnCurr1DayNcd_Type=Gauge32
_DsAdslAturChanPerfDataExtnCurr1DayNcd_Object=MibTableColumn
dsAdslAturChanPerfDataExtnCurr1DayNcd=_DsAdslAturChanPerfDataExtnCurr1DayNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,5),_DsAdslAturChanPerfDataExtnCurr1DayNcd_Type())
dsAdslAturChanPerfDataExtnCurr1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnCurr1DayNcd.setStatus(_A)
_DsAdslAturChanPerfDataExtnCurr1DayHec_Type=Gauge32
_DsAdslAturChanPerfDataExtnCurr1DayHec_Object=MibTableColumn
dsAdslAturChanPerfDataExtnCurr1DayHec=_DsAdslAturChanPerfDataExtnCurr1DayHec_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,6),_DsAdslAturChanPerfDataExtnCurr1DayHec_Type())
dsAdslAturChanPerfDataExtnCurr1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnCurr1DayHec.setStatus(_A)
_DsAdslAturChanPerfDataExtnPrev1DayNcd_Type=Gauge32
_DsAdslAturChanPerfDataExtnPrev1DayNcd_Object=MibTableColumn
dsAdslAturChanPerfDataExtnPrev1DayNcd=_DsAdslAturChanPerfDataExtnPrev1DayNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,7),_DsAdslAturChanPerfDataExtnPrev1DayNcd_Type())
dsAdslAturChanPerfDataExtnPrev1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnPrev1DayNcd.setStatus(_A)
_DsAdslAturChanPerfDataExtnPrev1DayHec_Type=Gauge32
_DsAdslAturChanPerfDataExtnPrev1DayHec_Object=MibTableColumn
dsAdslAturChanPerfDataExtnPrev1DayHec=_DsAdslAturChanPerfDataExtnPrev1DayHec_Object((1,3,6,1,4,1,6296,9,5,1,1,13,1,8),_DsAdslAturChanPerfDataExtnPrev1DayHec_Type())
dsAdslAturChanPerfDataExtnPrev1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanPerfDataExtnPrev1DayHec.setStatus(_A)
_DsAdslAtucChanIntervalExtnTable_Object=MibTable
dsAdslAtucChanIntervalExtnTable=_DsAdslAtucChanIntervalExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,14))
if mibBuilder.loadTexts:dsAdslAtucChanIntervalExtnTable.setStatus(_A)
_DsAdslAtucChanIntervalExtnEntry_Object=MibTableRow
dsAdslAtucChanIntervalExtnEntry=_DsAdslAtucChanIntervalExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,14,1))
dsAdslAtucChanIntervalExtnEntry.setIndexNames((0,_F,_G),(0,_J,_X))
if mibBuilder.loadTexts:dsAdslAtucChanIntervalExtnEntry.setStatus(_A)
_DsAdslAtucChanIntervalExtnTimeElapsed_Type=Counter32
_DsAdslAtucChanIntervalExtnTimeElapsed_Object=MibTableColumn
dsAdslAtucChanIntervalExtnTimeElapsed=_DsAdslAtucChanIntervalExtnTimeElapsed_Object((1,3,6,1,4,1,6296,9,5,1,1,14,1,1),_DsAdslAtucChanIntervalExtnTimeElapsed_Type())
dsAdslAtucChanIntervalExtnTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanIntervalExtnTimeElapsed.setStatus(_A)
_DsAdslAtucChanIntervalExtnNcd_Type=Counter32
_DsAdslAtucChanIntervalExtnNcd_Object=MibTableColumn
dsAdslAtucChanIntervalExtnNcd=_DsAdslAtucChanIntervalExtnNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,14,1,2),_DsAdslAtucChanIntervalExtnNcd_Type())
dsAdslAtucChanIntervalExtnNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanIntervalExtnNcd.setStatus(_A)
_DsAdslAtucChanIntervalExtnOcd_Type=Counter32
_DsAdslAtucChanIntervalExtnOcd_Object=MibTableColumn
dsAdslAtucChanIntervalExtnOcd=_DsAdslAtucChanIntervalExtnOcd_Object((1,3,6,1,4,1,6296,9,5,1,1,14,1,3),_DsAdslAtucChanIntervalExtnOcd_Type())
dsAdslAtucChanIntervalExtnOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanIntervalExtnOcd.setStatus(_A)
_DsAdslAtucChanIntervalExtnHec_Type=Counter32
_DsAdslAtucChanIntervalExtnHec_Object=MibTableColumn
dsAdslAtucChanIntervalExtnHec=_DsAdslAtucChanIntervalExtnHec_Object((1,3,6,1,4,1,6296,9,5,1,1,14,1,4),_DsAdslAtucChanIntervalExtnHec_Type())
dsAdslAtucChanIntervalExtnHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAtucChanIntervalExtnHec.setStatus(_A)
_DsAdslAturChanIntervalExtnTable_Object=MibTable
dsAdslAturChanIntervalExtnTable=_DsAdslAturChanIntervalExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,15))
if mibBuilder.loadTexts:dsAdslAturChanIntervalExtnTable.setStatus(_A)
_DsAdslAturChanIntervalExtnEntry_Object=MibTableRow
dsAdslAturChanIntervalExtnEntry=_DsAdslAturChanIntervalExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,15,1))
dsAdslAturChanIntervalExtnEntry.setIndexNames((0,_F,_G),(0,_J,_Z))
if mibBuilder.loadTexts:dsAdslAturChanIntervalExtnEntry.setStatus(_A)
_DsAdslAturChanIntervalExtnNcd_Type=Gauge32
_DsAdslAturChanIntervalExtnNcd_Object=MibTableColumn
dsAdslAturChanIntervalExtnNcd=_DsAdslAturChanIntervalExtnNcd_Object((1,3,6,1,4,1,6296,9,5,1,1,15,1,1),_DsAdslAturChanIntervalExtnNcd_Type())
dsAdslAturChanIntervalExtnNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanIntervalExtnNcd.setStatus(_A)
_DsAdslAturChanIntervalExtnHec_Type=Gauge32
_DsAdslAturChanIntervalExtnHec_Object=MibTableColumn
dsAdslAturChanIntervalExtnHec=_DsAdslAturChanIntervalExtnHec_Object((1,3,6,1,4,1,6296,9,5,1,1,15,1,2),_DsAdslAturChanIntervalExtnHec_Type())
dsAdslAturChanIntervalExtnHec.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslAturChanIntervalExtnHec.setStatus(_A)
_DsAdslLineConfProfileExtnTable_Object=MibTable
dsAdslLineConfProfileExtnTable=_DsAdslLineConfProfileExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,16))
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnTable.setStatus(_A)
_DsAdslLineConfProfileExtnEntry_Object=MibTableRow
dsAdslLineConfProfileExtnEntry=_DsAdslLineConfProfileExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1))
dsAdslLineConfProfileExtnEntry.setIndexNames((0,_J,_b))
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnEntry.setStatus(_A)
class _DsAdslLineConfProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DsAdslLineConfProfileName_Type.__name__=_H
_DsAdslLineConfProfileName_Object=MibTableColumn
dsAdslLineConfProfileName=_DsAdslLineConfProfileName_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,1),_DsAdslLineConfProfileName_Type())
dsAdslLineConfProfileName.setMaxAccess(_AB)
if mibBuilder.loadTexts:dsAdslLineConfProfileName.setStatus(_A)
class _DsAdslLineConfProfileExtnRsIntCorrectionUp_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,15)));namedValues=NamedValues(*(('dsAdslLineConfProfileExtnTable125us',3),('dsAdslLineConfProfileExtnTable250us',4),('dsAdslLineConfProfileExtnTable500us',5),('dsAdslLineConfProfileExtnTable1ms',6),('dsAdslLineConfProfileExtnTable2ms',7),('dsAdslLineConfProfileExtnTable4ms',8),(_I,15)))
_DsAdslLineConfProfileExtnRsIntCorrectionUp_Type.__name__=_C
_DsAdslLineConfProfileExtnRsIntCorrectionUp_Object=MibTableColumn
dsAdslLineConfProfileExtnRsIntCorrectionUp=_DsAdslLineConfProfileExtnRsIntCorrectionUp_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,3),_DsAdslLineConfProfileExtnRsIntCorrectionUp_Type())
dsAdslLineConfProfileExtnRsIntCorrectionUp.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnRsIntCorrectionUp.setStatus(_A)
class _DsAdslLineConfProfileExtnLineType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('noChannel',1),('fastOnly',2),('interleavedOnly',3),('fastOrInterleaved',4),('fastAndInterleaved',5)))
_DsAdslLineConfProfileExtnLineType_Type.__name__=_C
_DsAdslLineConfProfileExtnLineType_Object=MibTableColumn
dsAdslLineConfProfileExtnLineType=_DsAdslLineConfProfileExtnLineType_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,4),_DsAdslLineConfProfileExtnLineType_Type())
dsAdslLineConfProfileExtnLineType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnLineType.setStatus(_A)
class _DsAdslLineConfProfileExtnTxEndBin_Type(Integer32):defaultValue=511;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,511))
_DsAdslLineConfProfileExtnTxEndBin_Type.__name__=_C
_DsAdslLineConfProfileExtnTxEndBin_Object=MibTableColumn
dsAdslLineConfProfileExtnTxEndBin=_DsAdslLineConfProfileExtnTxEndBin_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,5),_DsAdslLineConfProfileExtnTxEndBin_Type())
dsAdslLineConfProfileExtnTxEndBin.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnTxEndBin.setStatus(_A)
class _DsAdslLineConfProfileExtnTxStartBin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,511))
_DsAdslLineConfProfileExtnTxStartBin_Type.__name__=_C
_DsAdslLineConfProfileExtnTxStartBin_Object=MibTableColumn
dsAdslLineConfProfileExtnTxStartBin=_DsAdslLineConfProfileExtnTxStartBin_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,6),_DsAdslLineConfProfileExtnTxStartBin_Type())
dsAdslLineConfProfileExtnTxStartBin.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnTxStartBin.setStatus(_A)
class _DsAdslLineConfProfileExtnRxStartBin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,511))
_DsAdslLineConfProfileExtnRxStartBin_Type.__name__=_C
_DsAdslLineConfProfileExtnRxStartBin_Object=MibTableColumn
dsAdslLineConfProfileExtnRxStartBin=_DsAdslLineConfProfileExtnRxStartBin_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,8),_DsAdslLineConfProfileExtnRxStartBin_Type())
dsAdslLineConfProfileExtnRxStartBin.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnRxStartBin.setStatus(_A)
class _DsAdslLineConfProfileExtnRxEndBin_Type(Integer32):defaultValue=511;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,511))
_DsAdslLineConfProfileExtnRxEndBin_Type.__name__=_C
_DsAdslLineConfProfileExtnRxEndBin_Object=MibTableColumn
dsAdslLineConfProfileExtnRxEndBin=_DsAdslLineConfProfileExtnRxEndBin_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,9),_DsAdslLineConfProfileExtnRxEndBin_Type())
dsAdslLineConfProfileExtnRxEndBin.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnRxEndBin.setStatus(_A)
class _DsAdslLineConfProfileExtnRxBinAdjust_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_I,0))
_DsAdslLineConfProfileExtnRxBinAdjust_Type.__name__=_C
_DsAdslLineConfProfileExtnRxBinAdjust_Object=MibTableColumn
dsAdslLineConfProfileExtnRxBinAdjust=_DsAdslLineConfProfileExtnRxBinAdjust_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,10),_DsAdslLineConfProfileExtnRxBinAdjust_Type())
dsAdslLineConfProfileExtnRxBinAdjust.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnRxBinAdjust.setStatus(_A)
class _DsAdslLineConfProfileExtnStandard_Type(Integer32):defaultValue=27;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,9,26,27,28,29,30,48,49)));namedValues=NamedValues(*(('t1413',0),('gLite',1),('gDmt',2),('alctl14',3),(_A1,4),('adi',5),('alctl',6),('t1413Auto',9),('adsl2',26),(_A2,27),('readsl2',28),(_A3,29),(_A4,30),('adslPlus',48),(_A5,49)))
_DsAdslLineConfProfileExtnStandard_Type.__name__=_C
_DsAdslLineConfProfileExtnStandard_Object=MibTableColumn
dsAdslLineConfProfileExtnStandard=_DsAdslLineConfProfileExtnStandard_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,13),_DsAdslLineConfProfileExtnStandard_Type())
dsAdslLineConfProfileExtnStandard.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnStandard.setStatus(_A)
class _DsAdslLineConfProfileExtnTxPowerAttenuation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,32781,32782,32783,32784,32785,32786,32787,32788,32789,32790,32791,32792,32793,32794,32795,32796,32797,32798,32799,32800,32801,32802,32803,32804,32805,32806,32807,32808)));namedValues=NamedValues(*(('dsAdslLineConfProfileExtnTable0',0),(_S,1),('dsAdslLineConfProfileExtnTable2',2),(_T,3),('dsAdslLineConfProfileExtnTable4',4),('dsAdslLineConfProfileExtnTable5',5),(_U,6),('dsAdslLineConfProfileExtnTable7',7),('dsAdslLineConfProfileExtnTable8',8),('dsAdslLineConfProfileExtnTable9',9),('dsAdslLineConfProfileExtnTable10',10),('dsAdslLineConfProfileExtnTable11',11),(_V,12),('point1',13),('point2',14),('point3',15),('point4',16),('point5',17),('point6',18),('point7',19),('point8',20),('point9',21),('dsAdslLineConfProfileExtnTable13',32781),('dsAdslLineConfProfileExtnTable14',32782),('dsAdslLineConfProfileExtnTable15',32783),('dsAdslLineConfProfileExtnTable16',32784),('dsAdslLineConfProfileExtnTable17',32785),('dsAdslLineConfProfileExtnTable18',32786),('dsAdslLineConfProfileExtnTable19',32787),('dsAdslLineConfProfileExtnTable20',32788),('dsAdslLineConfProfileExtnTable21',32789),('dsAdslLineConfProfileExtnTable22',32790),('dsAdslLineConfProfileExtnTable23',32791),('dsAdslLineConfProfileExtnTable24',32792),(_W,32793),('dsAdslLineConfProfileExtnTable26',32794),('dsAdslLineConfProfileExtnTable27',32795),('dsAdslLineConfProfileExtnTable28',32796),('dsAdslLineConfProfileExtnTable29',32797),('dsAdslLineConfProfileExtnTable30',32798),('dsAdslLineConfProfileExtnTable31',32799),('dsAdslLineConfProfileExtnTable32',32800),('dsAdslLineConfProfileExtnTable33',32801),('dsAdslLineConfProfileExtnTable34',32802),('dsAdslLineConfProfileExtnTable35',32803),('dsAdslLineConfProfileExtnTable36',32804),('dsAdslLineConfProfileExtnTable37',32805),('dsAdslLineConfProfileExtnTable38',32806),('dsAdslLineConfProfileExtnTable39',32807),('dsAdslLineConfProfileExtnTable40',32808)))
_DsAdslLineConfProfileExtnTxPowerAttenuation_Type.__name__=_C
_DsAdslLineConfProfileExtnTxPowerAttenuation_Object=MibTableColumn
dsAdslLineConfProfileExtnTxPowerAttenuation=_DsAdslLineConfProfileExtnTxPowerAttenuation_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,15),_DsAdslLineConfProfileExtnTxPowerAttenuation_Type())
dsAdslLineConfProfileExtnTxPowerAttenuation.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnTxPowerAttenuation.setStatus(_A)
class _DsAdslLineConfProfileExtnRsFastOvrhdDown_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,15)));namedValues=NamedValues(*((_AC,1),(_W,2),(_V,3),(_U,4),(_T,5),(_S,7),(_I,15)))
_DsAdslLineConfProfileExtnRsFastOvrhdDown_Type.__name__=_C
_DsAdslLineConfProfileExtnRsFastOvrhdDown_Object=MibTableColumn
dsAdslLineConfProfileExtnRsFastOvrhdDown=_DsAdslLineConfProfileExtnRsFastOvrhdDown_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,17),_DsAdslLineConfProfileExtnRsFastOvrhdDown_Type())
dsAdslLineConfProfileExtnRsFastOvrhdDown.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnRsFastOvrhdDown.setStatus(_A)
class _DsAdslLineConfProfileExtnIntCorrectionDown_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,15)));namedValues=NamedValues(*(('dsAdslLineConfProfileExtnTable125Us',3),('dsAdslLineConfProfileExtnTable250Us',4),('dsAdslLineConfProfileExtnTable500Us',5),('dsAdslLineConfProfileExtnTable1Ms',6),('dsAdslLineConfProfileExtnTable2Ms',7),('dsAdslLineConfProfileExtnTable4Ms',8),(_I,15)))
_DsAdslLineConfProfileExtnIntCorrectionDown_Type.__name__=_C
_DsAdslLineConfProfileExtnIntCorrectionDown_Object=MibTableColumn
dsAdslLineConfProfileExtnIntCorrectionDown=_DsAdslLineConfProfileExtnIntCorrectionDown_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,18),_DsAdslLineConfProfileExtnIntCorrectionDown_Type())
dsAdslLineConfProfileExtnIntCorrectionDown.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnIntCorrectionDown.setStatus(_A)
class _DsAdslLineConfProfileExtnRsFastOvrhdUp_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,15)));namedValues=NamedValues(*((_AC,1),(_W,2),(_V,3),(_U,4),(_T,5),(_S,7),(_I,15)))
_DsAdslLineConfProfileExtnRsFastOvrhdUp_Type.__name__=_C
_DsAdslLineConfProfileExtnRsFastOvrhdUp_Object=MibTableColumn
dsAdslLineConfProfileExtnRsFastOvrhdUp=_DsAdslLineConfProfileExtnRsFastOvrhdUp_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,19),_DsAdslLineConfProfileExtnRsFastOvrhdUp_Type())
dsAdslLineConfProfileExtnRsFastOvrhdUp.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnRsFastOvrhdUp.setStatus(_A)
class _DsAdslLineConfProfileExtnAnnexType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5)));namedValues=NamedValues(*(('annexA',0),('annexB',1),('highSpeed',2),('annexADSL2',5)))
_DsAdslLineConfProfileExtnAnnexType_Type.__name__=_C
_DsAdslLineConfProfileExtnAnnexType_Object=MibTableColumn
dsAdslLineConfProfileExtnAnnexType=_DsAdslLineConfProfileExtnAnnexType_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,26),_DsAdslLineConfProfileExtnAnnexType_Type())
dsAdslLineConfProfileExtnAnnexType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnAnnexType.setStatus(_A)
class _DsAdslLineConfProfileExtnMaxDCo_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4096,8192)));namedValues=NamedValues(*(('dsAdslLineConfProfileExtnTable64',0),('dsAdslLineConfProfileExtnTable128',4096),('dsAdslLineConfProfileExtnTable256',8192)))
_DsAdslLineConfProfileExtnMaxDCo_Type.__name__=_C
_DsAdslLineConfProfileExtnMaxDCo_Object=MibTableColumn
dsAdslLineConfProfileExtnMaxDCo=_DsAdslLineConfProfileExtnMaxDCo_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,30),_DsAdslLineConfProfileExtnMaxDCo_Type())
dsAdslLineConfProfileExtnMaxDCo.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnMaxDCo.setStatus(_A)
class _DsAdslLineConfProfileExtnAdvertisedCapabilities_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,16)));namedValues=NamedValues(*((_I,0),('annexa',1),('annexb',2),('adslplus',16)))
_DsAdslLineConfProfileExtnAdvertisedCapabilities_Type.__name__=_C
_DsAdslLineConfProfileExtnAdvertisedCapabilities_Object=MibTableColumn
dsAdslLineConfProfileExtnAdvertisedCapabilities=_DsAdslLineConfProfileExtnAdvertisedCapabilities_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,32),_DsAdslLineConfProfileExtnAdvertisedCapabilities_Type())
dsAdslLineConfProfileExtnAdvertisedCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnAdvertisedCapabilities.setStatus(_A)
class _DsAdslLineConfProfileExtnPsdMaskType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,259,275,291,32768,32771,32772,49152)));namedValues=NamedValues(*((_Q,0),('hsadslM1',3),('hsadslM2',4),('adls2NonovlpFlat',259),('adsl2NonovlpM1',275),('adls2NonovlpM2',291),('msk2Rfi',32768),(_A6,32771),(_A7,32772),('coMsk2Rfio',49152)))
_DsAdslLineConfProfileExtnPsdMaskType_Type.__name__=_C
_DsAdslLineConfProfileExtnPsdMaskType_Object=MibTableColumn
dsAdslLineConfProfileExtnPsdMaskType=_DsAdslLineConfProfileExtnPsdMaskType_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,33),_DsAdslLineConfProfileExtnPsdMaskType_Type())
dsAdslLineConfProfileExtnPsdMaskType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPsdMaskType.setStatus(_A)
class _DsAdslLineConfProfileExtnLineDmtConfMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ecMode',1),('fdmMode',2)))
_DsAdslLineConfProfileExtnLineDmtConfMode_Type.__name__=_C
_DsAdslLineConfProfileExtnLineDmtConfMode_Object=MibTableColumn
dsAdslLineConfProfileExtnLineDmtConfMode=_DsAdslLineConfProfileExtnLineDmtConfMode_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,34),_DsAdslLineConfProfileExtnLineDmtConfMode_Type())
dsAdslLineConfProfileExtnLineDmtConfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnLineDmtConfMode.setStatus(_A)
class _DsAdslLineConfProfileExtnUpstreamPSD_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,32768)));namedValues=NamedValues(*(('standard',0),('jj100',1),('extended',32768)))
_DsAdslLineConfProfileExtnUpstreamPSD_Type.__name__=_C
_DsAdslLineConfProfileExtnUpstreamPSD_Object=MibTableColumn
dsAdslLineConfProfileExtnUpstreamPSD=_DsAdslLineConfProfileExtnUpstreamPSD_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,41),_DsAdslLineConfProfileExtnUpstreamPSD_Type())
dsAdslLineConfProfileExtnUpstreamPSD.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnUpstreamPSD.setStatus(_A)
class _DsAdslLineConfProfileExtnPMMode_Type(Bits):namedValues=NamedValues(*(('pmstatel3enable',0),('pmstatel2enable',1)))
_DsAdslLineConfProfileExtnPMMode_Type.__name__=_K
_DsAdslLineConfProfileExtnPMMode_Object=MibTableColumn
dsAdslLineConfProfileExtnPMMode=_DsAdslLineConfProfileExtnPMMode_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,42),_DsAdslLineConfProfileExtnPMMode_Type())
dsAdslLineConfProfileExtnPMMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPMMode.setStatus(_A)
class _DsAdslLineConfProfileExtnPML0Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DsAdslLineConfProfileExtnPML0Time_Type.__name__=_C
_DsAdslLineConfProfileExtnPML0Time_Object=MibTableColumn
dsAdslLineConfProfileExtnPML0Time=_DsAdslLineConfProfileExtnPML0Time_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,43),_DsAdslLineConfProfileExtnPML0Time_Type())
dsAdslLineConfProfileExtnPML0Time.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML0Time.setStatus(_A)
class _DsAdslLineConfProfileExtnPML2Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DsAdslLineConfProfileExtnPML2Time_Type.__name__=_C
_DsAdslLineConfProfileExtnPML2Time_Object=MibTableColumn
dsAdslLineConfProfileExtnPML2Time=_DsAdslLineConfProfileExtnPML2Time_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,44),_DsAdslLineConfProfileExtnPML2Time_Type())
dsAdslLineConfProfileExtnPML2Time.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML2Time.setStatus(_A)
class _DsAdslLineConfProfileExtnPML2ATPR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_DsAdslLineConfProfileExtnPML2ATPR_Type.__name__=_C
_DsAdslLineConfProfileExtnPML2ATPR_Object=MibTableColumn
dsAdslLineConfProfileExtnPML2ATPR=_DsAdslLineConfProfileExtnPML2ATPR_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,45),_DsAdslLineConfProfileExtnPML2ATPR_Type())
dsAdslLineConfProfileExtnPML2ATPR.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML2ATPR.setStatus(_A)
class _DsAdslLineConfProfileExtnPML2Rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256000,1024000))
_DsAdslLineConfProfileExtnPML2Rate_Type.__name__=_C
_DsAdslLineConfProfileExtnPML2Rate_Object=MibTableColumn
dsAdslLineConfProfileExtnPML2Rate=_DsAdslLineConfProfileExtnPML2Rate_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,46),_DsAdslLineConfProfileExtnPML2Rate_Type())
dsAdslLineConfProfileExtnPML2Rate.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML2Rate.setStatus(_A)
class _DsAdslLineConfProfileExtnAtucConfMinINP_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_DsAdslLineConfProfileExtnAtucConfMinINP_Type.__name__=_C
_DsAdslLineConfProfileExtnAtucConfMinINP_Object=MibTableColumn
dsAdslLineConfProfileExtnAtucConfMinINP=_DsAdslLineConfProfileExtnAtucConfMinINP_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,63),_DsAdslLineConfProfileExtnAtucConfMinINP_Type())
dsAdslLineConfProfileExtnAtucConfMinINP.setMaxAccess(_B)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnAtucConfMinINP.setStatus(_A)
class _DsAdslLineConfProfileExtnPML2EntryThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256000,1024000))
_DsAdslLineConfProfileExtnPML2EntryThresholdRate_Type.__name__=_C
_DsAdslLineConfProfileExtnPML2EntryThresholdRate_Object=MibTableColumn
dsAdslLineConfProfileExtnPML2EntryThresholdRate=_DsAdslLineConfProfileExtnPML2EntryThresholdRate_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,64),_DsAdslLineConfProfileExtnPML2EntryThresholdRate_Type())
dsAdslLineConfProfileExtnPML2EntryThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML2EntryThresholdRate.setStatus(_A)
class _DsAdslLineConfProfileExtnPML2ExitThresholdRate_Type(Integer32):defaultValue=512000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256000,1024000))
_DsAdslLineConfProfileExtnPML2ExitThresholdRate_Type.__name__=_C
_DsAdslLineConfProfileExtnPML2ExitThresholdRate_Object=MibTableColumn
dsAdslLineConfProfileExtnPML2ExitThresholdRate=_DsAdslLineConfProfileExtnPML2ExitThresholdRate_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,65),_DsAdslLineConfProfileExtnPML2ExitThresholdRate_Type())
dsAdslLineConfProfileExtnPML2ExitThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML2ExitThresholdRate.setStatus(_A)
class _DsAdslLineConfProfileExtnPML2EntryRateMinTime_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(900,65535))
_DsAdslLineConfProfileExtnPML2EntryRateMinTime_Type.__name__=_C
_DsAdslLineConfProfileExtnPML2EntryRateMinTime_Object=MibTableColumn
dsAdslLineConfProfileExtnPML2EntryRateMinTime=_DsAdslLineConfProfileExtnPML2EntryRateMinTime_Object((1,3,6,1,4,1,6296,9,5,1,1,16,1,66),_DsAdslLineConfProfileExtnPML2EntryRateMinTime_Type())
dsAdslLineConfProfileExtnPML2EntryRateMinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineConfProfileExtnPML2EntryRateMinTime.setStatus(_A)
_DsAdslLineAlarmConfProfileExtnTable_Object=MibTable
dsAdslLineAlarmConfProfileExtnTable=_DsAdslLineAlarmConfProfileExtnTable_Object((1,3,6,1,4,1,6296,9,5,1,1,17))
if mibBuilder.loadTexts:dsAdslLineAlarmConfProfileExtnTable.setStatus(_A)
_DsAdslLineAlarmConfProfileExtnEntry_Object=MibTableRow
dsAdslLineAlarmConfProfileExtnEntry=_DsAdslLineAlarmConfProfileExtnEntry_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1))
dsAdslLineAlarmConfProfileExtnEntry.setIndexNames((0,_J,_a))
if mibBuilder.loadTexts:dsAdslLineAlarmConfProfileExtnEntry.setStatus(_A)
class _DsAdslLineAlarmConfProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DsAdslLineAlarmConfProfileName_Type.__name__=_H
_DsAdslLineAlarmConfProfileName_Object=MibTableColumn
dsAdslLineAlarmConfProfileName=_DsAdslLineAlarmConfProfileName_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,1),_DsAdslLineAlarmConfProfileName_Type())
dsAdslLineAlarmConfProfileName.setMaxAccess(_AB)
if mibBuilder.loadTexts:dsAdslLineAlarmConfProfileName.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinFailFastR=_DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,2),_DsAdslLineAlarmExtnAtucThresh15MinFailFastR_Type())
dsAdslLineAlarmExtnAtucThresh15MinFailFastR.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh15MinFailFastR.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh15MinSesL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAtucThresh15MinSesL_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh15MinSesL_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinSesL=_DsAdslLineAlarmExtnAtucThresh15MinSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,3),_DsAdslLineAlarmExtnAtucThresh15MinSesL_Type())
dsAdslLineAlarmExtnAtucThresh15MinSesL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh15MinSesL.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh15MinUasL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAtucThresh15MinUasL_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh15MinUasL_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinUasL=_DsAdslLineAlarmExtnAtucThresh15MinUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,4),_DsAdslLineAlarmExtnAtucThresh15MinUasL_Type())
dsAdslLineAlarmExtnAtucThresh15MinUasL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh15MinUasL.setStatus(_A)
class _DsAdslLineAlarmExtnAtucOpStateTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('enable',1)))
_DsAdslLineAlarmExtnAtucOpStateTrapEnable_Type.__name__=_C
_DsAdslLineAlarmExtnAtucOpStateTrapEnable_Object=MibTableColumn
dsAdslLineAlarmExtnAtucOpStateTrapEnable=_DsAdslLineAlarmExtnAtucOpStateTrapEnable_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,5),_DsAdslLineAlarmExtnAtucOpStateTrapEnable_Type())
dsAdslLineAlarmExtnAtucOpStateTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucOpStateTrapEnable.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh15MinFecsL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAtucThresh15MinFecsL_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh15MinFecsL_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh15MinFecsL=_DsAdslLineAlarmExtnAtucThresh15MinFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,6),_DsAdslLineAlarmExtnAtucThresh15MinFecsL_Type())
dsAdslLineAlarmExtnAtucThresh15MinFecsL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh15MinFecsL.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayLofs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayLofs_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayLofs_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLofs=_DsAdslLineAlarmExtnAtucThresh1DayLofs_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,7),_DsAdslLineAlarmExtnAtucThresh1DayLofs_Type())
dsAdslLineAlarmExtnAtucThresh1DayLofs.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayLofs.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayLoss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayLoss_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayLoss_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLoss=_DsAdslLineAlarmExtnAtucThresh1DayLoss_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,8),_DsAdslLineAlarmExtnAtucThresh1DayLoss_Type())
dsAdslLineAlarmExtnAtucThresh1DayLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayLoss.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayLols_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayLols_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayLols_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLols=_DsAdslLineAlarmExtnAtucThresh1DayLols_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,9),_DsAdslLineAlarmExtnAtucThresh1DayLols_Type())
dsAdslLineAlarmExtnAtucThresh1DayLols.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayLols.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayLprs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayLprs_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayLprs_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayLprs=_DsAdslLineAlarmExtnAtucThresh1DayLprs_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,10),_DsAdslLineAlarmExtnAtucThresh1DayLprs_Type())
dsAdslLineAlarmExtnAtucThresh1DayLprs.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayLprs.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayESs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayESs_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayESs_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayESs=_DsAdslLineAlarmExtnAtucThresh1DayESs_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,11),_DsAdslLineAlarmExtnAtucThresh1DayESs_Type())
dsAdslLineAlarmExtnAtucThresh1DayESs.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayESs.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DaySesL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DaySesL_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DaySesL_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DaySesL=_DsAdslLineAlarmExtnAtucThresh1DaySesL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,12),_DsAdslLineAlarmExtnAtucThresh1DaySesL_Type())
dsAdslLineAlarmExtnAtucThresh1DaySesL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DaySesL.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayUasL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayUasL_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayUasL_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayUasL=_DsAdslLineAlarmExtnAtucThresh1DayUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,13),_DsAdslLineAlarmExtnAtucThresh1DayUasL_Type())
dsAdslLineAlarmExtnAtucThresh1DayUasL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayUasL.setStatus(_A)
class _DsAdslLineAlarmExtnAtucThresh1DayFecsL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAtucThresh1DayFecsL_Type.__name__=_C
_DsAdslLineAlarmExtnAtucThresh1DayFecsL_Object=MibTableColumn
dsAdslLineAlarmExtnAtucThresh1DayFecsL=_DsAdslLineAlarmExtnAtucThresh1DayFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,14),_DsAdslLineAlarmExtnAtucThresh1DayFecsL_Type())
dsAdslLineAlarmExtnAtucThresh1DayFecsL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucThresh1DayFecsL.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh15MinFecsL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAturThresh15MinFecsL_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh15MinFecsL_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh15MinFecsL=_DsAdslLineAlarmExtnAturThresh15MinFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,15),_DsAdslLineAlarmExtnAturThresh15MinFecsL_Type())
dsAdslLineAlarmExtnAturThresh15MinFecsL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh15MinFecsL.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DayLofs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DayLofs_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DayLofs_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayLofs=_DsAdslLineAlarmExtnAturThresh1DayLofs_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,16),_DsAdslLineAlarmExtnAturThresh1DayLofs_Type())
dsAdslLineAlarmExtnAturThresh1DayLofs.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DayLofs.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DayLoss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DayLoss_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DayLoss_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayLoss=_DsAdslLineAlarmExtnAturThresh1DayLoss_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,17),_DsAdslLineAlarmExtnAturThresh1DayLoss_Type())
dsAdslLineAlarmExtnAturThresh1DayLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DayLoss.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DayLprs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DayLprs_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DayLprs_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayLprs=_DsAdslLineAlarmExtnAturThresh1DayLprs_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,18),_DsAdslLineAlarmExtnAturThresh1DayLprs_Type())
dsAdslLineAlarmExtnAturThresh1DayLprs.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DayLprs.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DayESs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DayESs_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DayESs_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayESs=_DsAdslLineAlarmExtnAturThresh1DayESs_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,19),_DsAdslLineAlarmExtnAturThresh1DayESs_Type())
dsAdslLineAlarmExtnAturThresh1DayESs.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DayESs.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DaySesL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DaySesL_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DaySesL_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DaySesL=_DsAdslLineAlarmExtnAturThresh1DaySesL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,20),_DsAdslLineAlarmExtnAturThresh1DaySesL_Type())
dsAdslLineAlarmExtnAturThresh1DaySesL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DaySesL.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DayUasL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DayUasL_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DayUasL_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayUasL=_DsAdslLineAlarmExtnAturThresh1DayUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,21),_DsAdslLineAlarmExtnAturThresh1DayUasL_Type())
dsAdslLineAlarmExtnAturThresh1DayUasL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DayUasL.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh1DayFecsL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DsAdslLineAlarmExtnAturThresh1DayFecsL_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh1DayFecsL_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh1DayFecsL=_DsAdslLineAlarmExtnAturThresh1DayFecsL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,22),_DsAdslLineAlarmExtnAturThresh1DayFecsL_Type())
dsAdslLineAlarmExtnAturThresh1DayFecsL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh1DayFecsL.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh15MinSesL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAturThresh15MinSesL_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh15MinSesL_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh15MinSesL=_DsAdslLineAlarmExtnAturThresh15MinSesL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,23),_DsAdslLineAlarmExtnAturThresh15MinSesL_Type())
dsAdslLineAlarmExtnAturThresh15MinSesL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh15MinSesL.setStatus(_A)
class _DsAdslLineAlarmExtnAturThresh15MinUasL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DsAdslLineAlarmExtnAturThresh15MinUasL_Type.__name__=_C
_DsAdslLineAlarmExtnAturThresh15MinUasL_Object=MibTableColumn
dsAdslLineAlarmExtnAturThresh15MinUasL=_DsAdslLineAlarmExtnAturThresh15MinUasL_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,24),_DsAdslLineAlarmExtnAturThresh15MinUasL_Type())
dsAdslLineAlarmExtnAturThresh15MinUasL.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAturThresh15MinUasL.setStatus(_A)
class _DsAdslLineAlarmExtnAtucPmStateTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('enable',1)))
_DsAdslLineAlarmExtnAtucPmStateTrapEnable_Type.__name__=_C
_DsAdslLineAlarmExtnAtucPmStateTrapEnable_Object=MibTableColumn
dsAdslLineAlarmExtnAtucPmStateTrapEnable=_DsAdslLineAlarmExtnAtucPmStateTrapEnable_Object((1,3,6,1,4,1,6296,9,5,1,1,17,1,25),_DsAdslLineAlarmExtnAtucPmStateTrapEnable_Type())
dsAdslLineAlarmExtnAtucPmStateTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dsAdslLineAlarmExtnAtucPmStateTrapEnable.setStatus(_A)
_DsAdslTrap_ObjectIdentity=ObjectIdentity
dsAdslTrap=_DsAdslTrap_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1,2))
_DsAdslAtucTraps_ObjectIdentity=ObjectIdentity
dsAdslAtucTraps=_DsAdslAtucTraps_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1,2,1))
_DsAdslAturTraps_ObjectIdentity=ObjectIdentity
dsAdslAturTraps=_DsAdslAturTraps_ObjectIdentity((1,3,6,1,4,1,6296,9,5,1,2,2))
dsAdslAtucOpStateChangeTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,1))
dsAdslAtucOpStateChangeTrap.setObjects((_E,_AD))
if mibBuilder.loadTexts:dsAdslAtucOpStateChangeTrap.setStatus(_A)
dsAdslAtucPmStateChangeTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,2))
dsAdslAtucPmStateChangeTrap.setObjects((_E,_AE))
if mibBuilder.loadTexts:dsAdslAtucPmStateChangeTrap.setStatus(_A)
dsAdslAtucPerfFailedFastRThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,3))
dsAdslAtucPerfFailedFastRThreshTrap.setObjects(*((_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:dsAdslAtucPerfFailedFastRThreshTrap.setStatus(_A)
dsAdslAtucPerfSesLThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,4))
dsAdslAtucPerfSesLThreshTrap.setObjects(*((_E,_AH),(_E,_AI)))
if mibBuilder.loadTexts:dsAdslAtucPerfSesLThreshTrap.setStatus(_A)
dsAdslAtucPerfUasLThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,5))
dsAdslAtucPerfUasLThreshTrap.setObjects(*((_E,_AJ),(_E,_AK)))
if mibBuilder.loadTexts:dsAdslAtucPerfUasLThreshTrap.setStatus(_A)
dsAdslAtucPerfFecsLThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,6))
dsAdslAtucPerfFecsLThreshTrap.setObjects(*((_E,_AL),(_E,_AM)))
if mibBuilder.loadTexts:dsAdslAtucPerfFecsLThreshTrap.setStatus(_A)
dsAdslAtucPerfLofsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,7))
dsAdslAtucPerfLofsThresh1DayTrap.setObjects(*((_E,'adslAtucPerfCurr1DayLofs'),(_E,_AN)))
if mibBuilder.loadTexts:dsAdslAtucPerfLofsThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfLossThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,8))
dsAdslAtucPerfLossThresh1DayTrap.setObjects(*((_E,'adslAtucPerfCurr1DayLoss'),(_E,_AO)))
if mibBuilder.loadTexts:dsAdslAtucPerfLossThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfLolsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,9))
dsAdslAtucPerfLolsThresh1DayTrap.setObjects(*((_E,'adslAtucPerfCurr1DayLols'),(_E,_AP)))
if mibBuilder.loadTexts:dsAdslAtucPerfLolsThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfLprsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,10))
dsAdslAtucPerfLprsThresh1DayTrap.setObjects(*((_E,'adslAtucPerfCurr1DayLprs'),(_E,_AQ)))
if mibBuilder.loadTexts:dsAdslAtucPerfLprsThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfESsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,11))
dsAdslAtucPerfESsThresh1DayTrap.setObjects(*((_E,'adslAtucPerfCurr1DayESs'),(_E,_AR)))
if mibBuilder.loadTexts:dsAdslAtucPerfESsThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfSesLThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,12))
dsAdslAtucPerfSesLThresh1DayTrap.setObjects(*((_E,_AS),(_E,_AT)))
if mibBuilder.loadTexts:dsAdslAtucPerfSesLThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfUasLThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,13))
dsAdslAtucPerfUasLThresh1DayTrap.setObjects(*((_E,_AU),(_E,_AV)))
if mibBuilder.loadTexts:dsAdslAtucPerfUasLThresh1DayTrap.setStatus(_A)
dsAdslAtucPerfFecsLThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,1,14))
dsAdslAtucPerfFecsLThresh1DayTrap.setObjects(*((_E,_AW),(_E,_AX)))
if mibBuilder.loadTexts:dsAdslAtucPerfFecsLThresh1DayTrap.setStatus(_A)
dsAdslAturSesLThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,1))
dsAdslAturSesLThreshTrap.setObjects(*((_E,_AY),(_E,_AZ)))
if mibBuilder.loadTexts:dsAdslAturSesLThreshTrap.setStatus(_A)
dsAdslAturUasLThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,2))
dsAdslAturUasLThreshTrap.setObjects(*((_E,_Aa),(_E,_Ab)))
if mibBuilder.loadTexts:dsAdslAturUasLThreshTrap.setStatus(_A)
dsAdslAturPerfFecsLThreshTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,3))
dsAdslAturPerfFecsLThreshTrap.setObjects(*((_E,_Ac),(_E,_Ad)))
if mibBuilder.loadTexts:dsAdslAturPerfFecsLThreshTrap.setStatus(_A)
dsAdslAturPerfLofsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,4))
dsAdslAturPerfLofsThresh1DayTrap.setObjects(*((_E,'adslAturPerfCurr1DayLofs'),(_E,_Ae)))
if mibBuilder.loadTexts:dsAdslAturPerfLofsThresh1DayTrap.setStatus(_A)
dsAdslAturPerfLossThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,5))
dsAdslAturPerfLossThresh1DayTrap.setObjects(*((_E,'adslAturPerfCurr1DayLoss'),(_E,_Af)))
if mibBuilder.loadTexts:dsAdslAturPerfLossThresh1DayTrap.setStatus(_A)
dsAdslAturPerfLprsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,6))
dsAdslAturPerfLprsThresh1DayTrap.setObjects(*((_E,'adslAturPerfCurr1DayLprs'),(_E,_Ag)))
if mibBuilder.loadTexts:dsAdslAturPerfLprsThresh1DayTrap.setStatus(_A)
dsAdslAturPerfESsThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,7))
dsAdslAturPerfESsThresh1DayTrap.setObjects(*((_E,'adslAturPerfCurr1DayESs'),(_E,_Ah)))
if mibBuilder.loadTexts:dsAdslAturPerfESsThresh1DayTrap.setStatus(_A)
dsAdslAturPerfSesLThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,8))
dsAdslAturPerfSesLThresh1DayTrap.setObjects(*((_E,_Ai),(_E,_Aj)))
if mibBuilder.loadTexts:dsAdslAturPerfSesLThresh1DayTrap.setStatus(_A)
dsAdslAturPerfUasLThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,9))
dsAdslAturPerfUasLThresh1DayTrap.setObjects(*((_E,_Ak),(_E,_Al)))
if mibBuilder.loadTexts:dsAdslAturPerfUasLThresh1DayTrap.setStatus(_A)
dsAdslAturPerfFecsLThresh1DayTrap=NotificationType((1,3,6,1,4,1,6296,9,5,1,2,2,10))
dsAdslAturPerfFecsLThresh1DayTrap.setObjects(*((_E,_Am),(_E,_An)))
if mibBuilder.loadTexts:dsAdslAturPerfFecsLThresh1DayTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dasanAdslMIB':dasanAdslMIB,'dasanAdslLineMIB':dasanAdslLineMIB,'dasanAdslMIBObjects':dasanAdslMIBObjects,'dsDslSystemParamGroup':dsDslSystemParamGroup,'dsDslSystemDslType':dsDslSystemDslType,'dsDslSystemLineCodingType':dsDslSystemLineCodingType,'dsDslSystemLineTxCfg':dsDslSystemLineTxCfg,'dsAdslCapabilityGroup':dsAdslCapabilityGroup,'dsAdslCapabilityLineTxCap':dsAdslCapabilityLineTxCap,'dsAdslLineExtnTable':dsAdslLineExtnTable,'dsAdslLineExtnEntry':dsAdslLineExtnEntry,'dsAdslLineExtnAction':dsAdslLineExtnAction,'dsAdslLineExtnUtopiaL2RxAddr':dsAdslLineExtnUtopiaL2RxAddr,'dsAdslLineExtnUtopiaL2TxAddr':dsAdslLineExtnUtopiaL2TxAddr,'dsAdslLineExtnTransAtucCap':dsAdslLineExtnTransAtucCap,'dsAdslLineExtnTransAtucActual':dsAdslLineExtnTransAtucActual,'dsAdslLineExtnClockType':dsAdslLineExtnClockType,'dsAdslLineExtnLineDmtTrellis':dsAdslLineExtnLineDmtTrellis,'dsAdslAtucPhysExtnTable':dsAdslAtucPhysExtnTable,'dsAdslAtucPhysExtnEntry':dsAdslAtucPhysExtnEntry,_AD:dsAdslAtucPhysExtnOpState,'dsAdslAtucPhysExtnActualStd':dsAdslAtucPhysExtnActualStd,'dsAdslAtucPhysExtnBertError':dsAdslAtucPhysExtnBertError,'dsAdslAtucPhysExtnTxAtmCellCounter':dsAdslAtucPhysExtnTxAtmCellCounter,'dsAdslAtucPhysExtnRxAtmCellCounter':dsAdslAtucPhysExtnRxAtmCellCounter,'dsAdslAtucPhysExtnStartProgress':dsAdslAtucPhysExtnStartProgress,'dsAdslAtucPhysExtnIdleBertError':dsAdslAtucPhysExtnIdleBertError,'dsAdslAtucPhysExtnIdleBertCells':dsAdslAtucPhysExtnIdleBertCells,'dsAdslAtucPhysExtnBertSync':dsAdslAtucPhysExtnBertSync,'dsAdslAtucPhysExtnParametricTestResult':dsAdslAtucPhysExtnParametricTestResult,'dsAdslAtucPhysExtnDataBoostStatus':dsAdslAtucPhysExtnDataBoostStatus,'dsAdslAtucPhysExtnTestArray':dsAdslAtucPhysExtnTestArray,'dsAdslAtucPhysExtnChanPerfCD':dsAdslAtucPhysExtnChanPerfCD,'dsAdslAtucPhysExtnChanPerfBE':dsAdslAtucPhysExtnChanPerfBE,'dsAdslAtucPhysExtnDeltHLINSCus':dsAdslAtucPhysExtnDeltHLINSCus,'dsAdslAtucPhysExtnDeltHLINpsus':dsAdslAtucPhysExtnDeltHLINpsus,'dsAdslAtucPhysExtnDeltHLOGMTus':dsAdslAtucPhysExtnDeltHLOGMTus,'dsAdslAtucPhysExtnDeltHLOGpsus':dsAdslAtucPhysExtnDeltHLOGpsus,'dsAdslAtucPhysExtnDeltQLNMTus':dsAdslAtucPhysExtnDeltQLNMTus,'dsAdslAtucPhysExtnDeltQLNpsus':dsAdslAtucPhysExtnDeltQLNpsus,'dsAdslAtucPhysExtnDeltLastTxState':dsAdslAtucPhysExtnDeltLastTxState,_AE:dsAdslAtucPhysExtnPMState,'dsAdslAtucPhysExtnChanPerfCU':dsAdslAtucPhysExtnChanPerfCU,'dsAdslAtucPhysExtnExtendedPsdStatus':dsAdslAtucPhysExtnExtendedPsdStatus,'dsAdslAtucPhysExtnChipVersion':dsAdslAtucPhysExtnChipVersion,'dsAdslAtucPhysExtnPilotTone':dsAdslAtucPhysExtnPilotTone,'dsAdslAtucMSGds':dsAdslAtucMSGds,'dsAdslAtucPhysExtnPsdMaskMode':dsAdslAtucPhysExtnPsdMaskMode,'dsAdslAturPhysExtnTable':dsAdslAturPhysExtnTable,'dsAdslAturPhysExtnEntry':dsAdslAturPhysExtnEntry,'dsAdslAturPhysExtnConfig':dsAdslAturPhysExtnConfig,'dsAdslAturPhysExtnChanPerfCD':dsAdslAturPhysExtnChanPerfCD,'dsAdslAturPhysExtnChanPerfCU':dsAdslAturPhysExtnChanPerfCU,'dsAdslAturPhysExtnChanPerfBE':dsAdslAturPhysExtnChanPerfBE,'dsAdslAturPhysExtnDeltHLINSCds':dsAdslAturPhysExtnDeltHLINSCds,'dsAdslAturPhysExtnDeltHLINpsds':dsAdslAturPhysExtnDeltHLINpsds,'dsAdslAturPhysExtnDeltHLOGMTds':dsAdslAturPhysExtnDeltHLOGMTds,'dsAdslAturPhysExtnDeltHLOGpsus':dsAdslAturPhysExtnDeltHLOGpsus,'dsAdslAturPhysExtnDeltQLNMTds':dsAdslAturPhysExtnDeltQLNMTds,'dsAdslAturPhysExtnDeltQLNpsds':dsAdslAturPhysExtnDeltQLNpsds,'dsAdslAturPhysExtnDeltLastTxState':dsAdslAturPhysExtnDeltLastTxState,'dsAdslAturMSGus':dsAdslAturMSGus,'dsAdslAtucChanExtnTable':dsAdslAtucChanExtnTable,'dsAdslAtucChanExtnEntry':dsAdslAtucChanExtnEntry,'dsAdslAtucChanExtnCurrAtmStatus':dsAdslAtucChanExtnCurrAtmStatus,'dsAdslAtucChanExtnRsSymbols':dsAdslAtucChanExtnRsSymbols,'dsAdslAtucChanExtnRsDepth':dsAdslAtucChanExtnRsDepth,'dsAdslAtucChanExtnRsRedundancy':dsAdslAtucChanExtnRsRedundancy,'dsAdslAturChanExtnTable':dsAdslAturChanExtnTable,'dsAdslAturChanExtnEntry':dsAdslAturChanExtnEntry,'dsAdslAturChanExtnCurrAtmStatus':dsAdslAturChanExtnCurrAtmStatus,'dsAdslAturChanExtnRsSymbols':dsAdslAturChanExtnRsSymbols,'dsAdslAturChanExtnRsDepth':dsAdslAturChanExtnRsDepth,'dsAdslAturChanExtnRsRedundancy':dsAdslAturChanExtnRsRedundancy,'dsAdslAtucPerfDataExtnTable':dsAdslAtucPerfDataExtnTable,'dsAdslAtucPerfDataExtnEntry':dsAdslAtucPerfDataExtnEntry,'dsAdslAtucPerfDataExtnStatFastR':dsAdslAtucPerfDataExtnStatFastR,'dsAdslAtucPerfDataExtnStatFailedFastR':dsAdslAtucPerfDataExtnStatFailedFastR,'dsAdslAtucPerfDataExtnStatSesL':dsAdslAtucPerfDataExtnStatSesL,'dsAdslAtucPerfDataExtnStatUasL':dsAdslAtucPerfDataExtnStatUasL,'dsAdslAtucPerfDataExtnCurr15MinFastR':dsAdslAtucPerfDataExtnCurr15MinFastR,_AF:dsAdslAtucPerfDataExtnCurr15MinFailedFastR,_AH:dsAdslAtucPerfDataExtnCurr15MinSesL,_AJ:dsAdslAtucPerfDataExtnCurr15MinUasL,'dsAdslAtucPerfDataExtnCurr1DayFastR':dsAdslAtucPerfDataExtnCurr1DayFastR,'dsAdslAtucPerfDataExtnCurr1DayFailedFastR':dsAdslAtucPerfDataExtnCurr1DayFailedFastR,_AS:dsAdslAtucPerfDataExtnCurr1DaySesL,_AU:dsAdslAtucPerfDataExtnCurr1DayUasL,'dsAdslAtucPerfDataExtnPrev1DayFastR':dsAdslAtucPerfDataExtnPrev1DayFastR,'dsAdslAtucPerfDataExtnPrev1DayFailedFastR':dsAdslAtucPerfDataExtnPrev1DayFailedFastR,'dsAdslAtucPerfDataExtnPrev1DaySesL':dsAdslAtucPerfDataExtnPrev1DaySesL,'dsAdslAtucPerfDataExtnPrev1DayUasL':dsAdslAtucPerfDataExtnPrev1DayUasL,'dsAdslAtucPerfDataExtnPrev1DayTimeElapsed':dsAdslAtucPerfDataExtnPrev1DayTimeElapsed,'dsAdslAtucPerfDataExtnStatFecsL':dsAdslAtucPerfDataExtnStatFecsL,_AL:dsAdslAtucPerfDataExtnCurr15MinFecsL,_AW:dsAdslAtucPerfDataExtnCurr1DayFecsL,'dsAdslAtucPerfDataExtnPrev1DayFecsL':dsAdslAtucPerfDataExtnPrev1DayFecsL,'dsAdslAtucPerfDataExtnStatLossL':dsAdslAtucPerfDataExtnStatLossL,'dsAdslAtucPerfDataExtnCurr15MinLossL':dsAdslAtucPerfDataExtnCurr15MinLossL,'dsAdslAtucPerfDataExtnCurr1DayLossL':dsAdslAtucPerfDataExtnCurr1DayLossL,'dsAdslAtucPerfDataExtnPrev1DayLossL':dsAdslAtucPerfDataExtnPrev1DayLossL,'dsAdslAturPerfDataExtnTable':dsAdslAturPerfDataExtnTable,'dsAdslAturPerfDataExtnEntry':dsAdslAturPerfDataExtnEntry,'dsAdslAturPerfDataExtnStatSesL':dsAdslAturPerfDataExtnStatSesL,_AY:dsAdslAturPerfDataExtnCurr15MinSesL,_Ai:dsAdslAturPerfDataExtnCurr1DaySesL,'dsAdslAturPerfDataExtnPrev1DaySesL':dsAdslAturPerfDataExtnPrev1DaySesL,'dsAdslAturPerfDataExtnStatUasL':dsAdslAturPerfDataExtnStatUasL,_Aa:dsAdslAturPerfDataExtnCurr15MinUasL,_Ak:dsAdslAturPerfDataExtnCurr1DayUasL,'dsAdslAturPerfDataExtnPrev1DayUasL':dsAdslAturPerfDataExtnPrev1DayUasL,'dsAdslAturPerfDataExtnStatFecsL':dsAdslAturPerfDataExtnStatFecsL,_Ac:dsAdslAturPerfDataExtnCurr15MinFecsL,_Am:dsAdslAturPerfDataExtnCurr1DayFecsL,'dsAdslAturPerfDataExtnPrev1DayFecsL':dsAdslAturPerfDataExtnPrev1DayFecsL,'dsAdslAturPerfDataExtnStatLossL':dsAdslAturPerfDataExtnStatLossL,'dsAdslAturPerfDataExtnCurr15MinLossL':dsAdslAturPerfDataExtnCurr15MinLossL,'dsAdslAturPerfDataExtnCurr1DayLossL':dsAdslAturPerfDataExtnCurr1DayLossL,'dsAdslAturPerfDataExtnPrev1DayLossL':dsAdslAturPerfDataExtnPrev1DayLossL,'dsAdslAtucIntervalExtnTable':dsAdslAtucIntervalExtnTable,'dsAdslAtucIntervalExtnEntry':dsAdslAtucIntervalExtnEntry,'dsAdslAtucIntervalExtnFastR':dsAdslAtucIntervalExtnFastR,'dsAdslAtucIntervalExtnFailedFastR':dsAdslAtucIntervalExtnFailedFastR,'dsAdslAtucIntervalExtnSesL':dsAdslAtucIntervalExtnSesL,'dsAdslAtucIntervalExtnUasL':dsAdslAtucIntervalExtnUasL,'dsAdslAtucIntervalExtnTimeElapsed':dsAdslAtucIntervalExtnTimeElapsed,'dsAdslAtucChanPerfDataExtnTable':dsAdslAtucChanPerfDataExtnTable,'dsAdslAtucChanPerfDataExtnEntry':dsAdslAtucChanPerfDataExtnEntry,'dsAdslAtucChanPerfDataExtnTimeElapsed':dsAdslAtucChanPerfDataExtnTimeElapsed,'dsAdslAtucChanPerfDataExtnNcd':dsAdslAtucChanPerfDataExtnNcd,'dsAdslAtucChanPerfDataExtnOcd':dsAdslAtucChanPerfDataExtnOcd,'dsAdslAtucChanPerfDataExtnHec':dsAdslAtucChanPerfDataExtnHec,'dsAdslAtucChanPerfDataExtnCurr15MinNcd':dsAdslAtucChanPerfDataExtnCurr15MinNcd,'dsAdslAtucChanPerfDataExtnCurr15MinOcd':dsAdslAtucChanPerfDataExtnCurr15MinOcd,'dsAdslAtucChanPerfDataExtnCurr15MinHec':dsAdslAtucChanPerfDataExtnCurr15MinHec,'dsAdslAtucChanPerfDataExtnCurr1DayNcd':dsAdslAtucChanPerfDataExtnCurr1DayNcd,'dsAdslAtucChanPerfDataExtnCurr1DayOcd':dsAdslAtucChanPerfDataExtnCurr1DayOcd,'dsAdslAtucChanPerfDataExtnCurr1DayHec':dsAdslAtucChanPerfDataExtnCurr1DayHec,'dsAdslAtucChanPerfDataExtnPrev1DayNcd':dsAdslAtucChanPerfDataExtnPrev1DayNcd,'dsAdslAtucChanPerfDataExtnPrev1DayOcd':dsAdslAtucChanPerfDataExtnPrev1DayOcd,'dsAdslAtucChanPerfDataExtnPrev1DayHec':dsAdslAtucChanPerfDataExtnPrev1DayHec,'dsAdslAturChanPerfDataExtnTable':dsAdslAturChanPerfDataExtnTable,'dsAdslAturChanPerfDataExtnEntry':dsAdslAturChanPerfDataExtnEntry,'dsAdslAturChanPerfDataExtnNcd':dsAdslAturChanPerfDataExtnNcd,'dsAdslAturChanPerfDataExtnHec':dsAdslAturChanPerfDataExtnHec,'dsAdslAturChanPerfDataExtnCurr15MinNcd':dsAdslAturChanPerfDataExtnCurr15MinNcd,'dsAdslAturChanPerfDataExtnCurr15MinHec':dsAdslAturChanPerfDataExtnCurr15MinHec,'dsAdslAturChanPerfDataExtnCurr1DayNcd':dsAdslAturChanPerfDataExtnCurr1DayNcd,'dsAdslAturChanPerfDataExtnCurr1DayHec':dsAdslAturChanPerfDataExtnCurr1DayHec,'dsAdslAturChanPerfDataExtnPrev1DayNcd':dsAdslAturChanPerfDataExtnPrev1DayNcd,'dsAdslAturChanPerfDataExtnPrev1DayHec':dsAdslAturChanPerfDataExtnPrev1DayHec,'dsAdslAtucChanIntervalExtnTable':dsAdslAtucChanIntervalExtnTable,'dsAdslAtucChanIntervalExtnEntry':dsAdslAtucChanIntervalExtnEntry,'dsAdslAtucChanIntervalExtnTimeElapsed':dsAdslAtucChanIntervalExtnTimeElapsed,'dsAdslAtucChanIntervalExtnNcd':dsAdslAtucChanIntervalExtnNcd,'dsAdslAtucChanIntervalExtnOcd':dsAdslAtucChanIntervalExtnOcd,'dsAdslAtucChanIntervalExtnHec':dsAdslAtucChanIntervalExtnHec,'dsAdslAturChanIntervalExtnTable':dsAdslAturChanIntervalExtnTable,'dsAdslAturChanIntervalExtnEntry':dsAdslAturChanIntervalExtnEntry,'dsAdslAturChanIntervalExtnNcd':dsAdslAturChanIntervalExtnNcd,'dsAdslAturChanIntervalExtnHec':dsAdslAturChanIntervalExtnHec,'dsAdslLineConfProfileExtnTable':dsAdslLineConfProfileExtnTable,'dsAdslLineConfProfileExtnEntry':dsAdslLineConfProfileExtnEntry,'dsAdslLineConfProfileName':dsAdslLineConfProfileName,'dsAdslLineConfProfileExtnRsIntCorrectionUp':dsAdslLineConfProfileExtnRsIntCorrectionUp,'dsAdslLineConfProfileExtnLineType':dsAdslLineConfProfileExtnLineType,'dsAdslLineConfProfileExtnTxEndBin':dsAdslLineConfProfileExtnTxEndBin,'dsAdslLineConfProfileExtnTxStartBin':dsAdslLineConfProfileExtnTxStartBin,'dsAdslLineConfProfileExtnRxStartBin':dsAdslLineConfProfileExtnRxStartBin,'dsAdslLineConfProfileExtnRxEndBin':dsAdslLineConfProfileExtnRxEndBin,'dsAdslLineConfProfileExtnRxBinAdjust':dsAdslLineConfProfileExtnRxBinAdjust,'dsAdslLineConfProfileExtnStandard':dsAdslLineConfProfileExtnStandard,'dsAdslLineConfProfileExtnTxPowerAttenuation':dsAdslLineConfProfileExtnTxPowerAttenuation,'dsAdslLineConfProfileExtnRsFastOvrhdDown':dsAdslLineConfProfileExtnRsFastOvrhdDown,'dsAdslLineConfProfileExtnIntCorrectionDown':dsAdslLineConfProfileExtnIntCorrectionDown,'dsAdslLineConfProfileExtnRsFastOvrhdUp':dsAdslLineConfProfileExtnRsFastOvrhdUp,'dsAdslLineConfProfileExtnAnnexType':dsAdslLineConfProfileExtnAnnexType,'dsAdslLineConfProfileExtnMaxDCo':dsAdslLineConfProfileExtnMaxDCo,'dsAdslLineConfProfileExtnAdvertisedCapabilities':dsAdslLineConfProfileExtnAdvertisedCapabilities,'dsAdslLineConfProfileExtnPsdMaskType':dsAdslLineConfProfileExtnPsdMaskType,'dsAdslLineConfProfileExtnLineDmtConfMode':dsAdslLineConfProfileExtnLineDmtConfMode,'dsAdslLineConfProfileExtnUpstreamPSD':dsAdslLineConfProfileExtnUpstreamPSD,'dsAdslLineConfProfileExtnPMMode':dsAdslLineConfProfileExtnPMMode,'dsAdslLineConfProfileExtnPML0Time':dsAdslLineConfProfileExtnPML0Time,'dsAdslLineConfProfileExtnPML2Time':dsAdslLineConfProfileExtnPML2Time,'dsAdslLineConfProfileExtnPML2ATPR':dsAdslLineConfProfileExtnPML2ATPR,'dsAdslLineConfProfileExtnPML2Rate':dsAdslLineConfProfileExtnPML2Rate,'dsAdslLineConfProfileExtnAtucConfMinINP':dsAdslLineConfProfileExtnAtucConfMinINP,'dsAdslLineConfProfileExtnPML2EntryThresholdRate':dsAdslLineConfProfileExtnPML2EntryThresholdRate,'dsAdslLineConfProfileExtnPML2ExitThresholdRate':dsAdslLineConfProfileExtnPML2ExitThresholdRate,'dsAdslLineConfProfileExtnPML2EntryRateMinTime':dsAdslLineConfProfileExtnPML2EntryRateMinTime,'dsAdslLineAlarmConfProfileExtnTable':dsAdslLineAlarmConfProfileExtnTable,'dsAdslLineAlarmConfProfileExtnEntry':dsAdslLineAlarmConfProfileExtnEntry,'dsAdslLineAlarmConfProfileName':dsAdslLineAlarmConfProfileName,_AG:dsAdslLineAlarmExtnAtucThresh15MinFailFastR,_AI:dsAdslLineAlarmExtnAtucThresh15MinSesL,_AK:dsAdslLineAlarmExtnAtucThresh15MinUasL,'dsAdslLineAlarmExtnAtucOpStateTrapEnable':dsAdslLineAlarmExtnAtucOpStateTrapEnable,_AM:dsAdslLineAlarmExtnAtucThresh15MinFecsL,_AN:dsAdslLineAlarmExtnAtucThresh1DayLofs,_AO:dsAdslLineAlarmExtnAtucThresh1DayLoss,_AP:dsAdslLineAlarmExtnAtucThresh1DayLols,_AQ:dsAdslLineAlarmExtnAtucThresh1DayLprs,_AR:dsAdslLineAlarmExtnAtucThresh1DayESs,_AT:dsAdslLineAlarmExtnAtucThresh1DaySesL,_AV:dsAdslLineAlarmExtnAtucThresh1DayUasL,_AX:dsAdslLineAlarmExtnAtucThresh1DayFecsL,_Ad:dsAdslLineAlarmExtnAturThresh15MinFecsL,_Ae:dsAdslLineAlarmExtnAturThresh1DayLofs,_Af:dsAdslLineAlarmExtnAturThresh1DayLoss,_Ag:dsAdslLineAlarmExtnAturThresh1DayLprs,_Ah:dsAdslLineAlarmExtnAturThresh1DayESs,_Aj:dsAdslLineAlarmExtnAturThresh1DaySesL,_Al:dsAdslLineAlarmExtnAturThresh1DayUasL,_An:dsAdslLineAlarmExtnAturThresh1DayFecsL,_AZ:dsAdslLineAlarmExtnAturThresh15MinSesL,_Ab:dsAdslLineAlarmExtnAturThresh15MinUasL,'dsAdslLineAlarmExtnAtucPmStateTrapEnable':dsAdslLineAlarmExtnAtucPmStateTrapEnable,'dsAdslTrap':dsAdslTrap,'dsAdslAtucTraps':dsAdslAtucTraps,'dsAdslAtucOpStateChangeTrap':dsAdslAtucOpStateChangeTrap,'dsAdslAtucPmStateChangeTrap':dsAdslAtucPmStateChangeTrap,'dsAdslAtucPerfFailedFastRThreshTrap':dsAdslAtucPerfFailedFastRThreshTrap,'dsAdslAtucPerfSesLThreshTrap':dsAdslAtucPerfSesLThreshTrap,'dsAdslAtucPerfUasLThreshTrap':dsAdslAtucPerfUasLThreshTrap,'dsAdslAtucPerfFecsLThreshTrap':dsAdslAtucPerfFecsLThreshTrap,'dsAdslAtucPerfLofsThresh1DayTrap':dsAdslAtucPerfLofsThresh1DayTrap,'dsAdslAtucPerfLossThresh1DayTrap':dsAdslAtucPerfLossThresh1DayTrap,'dsAdslAtucPerfLolsThresh1DayTrap':dsAdslAtucPerfLolsThresh1DayTrap,'dsAdslAtucPerfLprsThresh1DayTrap':dsAdslAtucPerfLprsThresh1DayTrap,'dsAdslAtucPerfESsThresh1DayTrap':dsAdslAtucPerfESsThresh1DayTrap,'dsAdslAtucPerfSesLThresh1DayTrap':dsAdslAtucPerfSesLThresh1DayTrap,'dsAdslAtucPerfUasLThresh1DayTrap':dsAdslAtucPerfUasLThresh1DayTrap,'dsAdslAtucPerfFecsLThresh1DayTrap':dsAdslAtucPerfFecsLThresh1DayTrap,'dsAdslAturTraps':dsAdslAturTraps,'dsAdslAturSesLThreshTrap':dsAdslAturSesLThreshTrap,'dsAdslAturUasLThreshTrap':dsAdslAturUasLThreshTrap,'dsAdslAturPerfFecsLThreshTrap':dsAdslAturPerfFecsLThreshTrap,'dsAdslAturPerfLofsThresh1DayTrap':dsAdslAturPerfLofsThresh1DayTrap,'dsAdslAturPerfLossThresh1DayTrap':dsAdslAturPerfLossThresh1DayTrap,'dsAdslAturPerfLprsThresh1DayTrap':dsAdslAturPerfLprsThresh1DayTrap,'dsAdslAturPerfESsThresh1DayTrap':dsAdslAturPerfESsThresh1DayTrap,'dsAdslAturPerfSesLThresh1DayTrap':dsAdslAturPerfSesLThresh1DayTrap,'dsAdslAturPerfUasLThresh1DayTrap':dsAdslAturPerfUasLThresh1DayTrap,'dsAdslAturPerfFecsLThresh1DayTrap':dsAdslAturPerfFecsLThresh1DayTrap})