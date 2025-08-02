_AW='cvDsx1ElecSigGroup'
_AV='cvDsx1AlarmLogGroup'
_AU='cvDsx1ConfGroupRev1'
_AT='cvDsx1ConfGroup'
_AS='vismDsx1ElectricalSignalEnable'
_AR='vismDsx1AlarmLogOperTimer'
_AQ='vismDsx1AlarmLogAdminTimer'
_AP='vismDsx1AlarmLogEnable'
_AO='vismDsx1V110Enable'
_AN='vismSlipCntDiscontinuityTime'
_AM='vismDsx1TotalRxFrameSlips'
_AL='vismDsx1TotalRxUncontrolledSlips'
_AK='vismDsx1TotalTxFrameSlips'
_AJ='vismDsx1TotalTxUncontrolledSlips'
_AI='dsx1RxFrameSlips'
_AH='dsx1RxUncontrolledSlips'
_AG='dsx1TxFrameSlips'
_AF='dsx1TxUncontrolledSlips'
_AE='vismBearerBusyCode'
_AD='vismCadenceTime'
_AC='vismEcanCnfNRN'
_AB='vismEcanToneDisable'
_AA='dsx1VismStatsGrpEntry'
_A9='milliseconds'
_A8='TimeStamp'
_A7='DisplayString'
_A6='cvDsx1ConfGroupSup1'
_A5='dsx1AlmClrButton'
_A4='rcvFECnt'
_A3='rcvRAICnt'
_A2='rcvOOFCnt'
_A1='rcvLOSCnt'
_A0='percentErrorFreeSecs'
_z='aISS'
_y='sEFS'
_x='cRCSES'
_w='cRCES'
_v='cRC'
_u='lSES'
_t='lES'
_s='lCV'
_r='Unsigned32'
_q='cvDsx1StatsGroup'
_p='cvDsx1AlmHistoryGroupRev1'
_o='cvDsx1AlmHistoryGroup'
_n='vismDsx1AdminStateControl'
_m='vismDsx1State'
_l='vismDsx1Sa8Byte'
_k='vismDsx1Sa7Byte'
_j='vismDsx1Sa6Byte'
_i='vismDsx1Sa5Byte'
_h='vismDsx1Sa4Byte'
_g='vismDsx1MidcallTcrit'
_f='vismDsx1MidcallTpart'
_e='vismDsx1RemoteRingback'
_d='vismDsx1OffHookAlertTO'
_c='vismDsx1StutterDialTO'
_b='vismDsx1DialTO'
_a='vismDsx1ReorderTO'
_Z='vismDsx1BusyTO'
_Y='vismDsx1RingBackTO'
_X='vismDsx1RingingTO'
_W='vismDsx1TonePlanVersion'
_V='vismDsx1TonePlanRegion'
_U='vismDsx1TxDigitOrder'
_T='vismDsx1CircuitIdentifier'
_S='vismTrunkConditionEnable'
_R='vismCcsChannels'
_Q='vismSignalingType'
_P='vismCompCnfVAD'
_O='vismEcanREC'
_N='vismEcanTail'
_M='vismEcanEnabled'
_L='almIntervalNumber'
_K='almlineNumber'
_J='cvDsx1ConfGroupRev2'
_I='vismLineNum'
_H='TruthValue'
_G='seconds'
_F='deprecated'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='CISCO-VISM-DSX1-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx1,=mibBuilder.importSymbols('BASIS-MIB','dsx1')
dsx1AlmGrp,=mibBuilder.importSymbols('CISCO-MGX82XX-DSX1-MIB','dsx1AlmGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_r,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_A7,'PhysAddress','TextualConvention',_A8,_H)
ciscoVismDsx1MIB=ModuleIdentity((1,3,6,1,4,1,351,150,79))
if mibBuilder.loadTexts:ciscoVismDsx1MIB.setRevisions(('2005-09-30 00:00','2005-01-20 00:00','2004-04-16 00:00','2004-03-09 00:00','2004-02-17 00:00','2004-02-15 00:00'))
_Dsx1AlmHistoryTable_Object=MibTable
dsx1AlmHistoryTable=_Dsx1AlmHistoryTable_Object((1,3,6,1,4,1,351,110,4,3,1,3,2))
if mibBuilder.loadTexts:dsx1AlmHistoryTable.setStatus(_B)
_Dsx1AlmHistoryEntry_Object=MibTableRow
dsx1AlmHistoryEntry=_Dsx1AlmHistoryEntry_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1))
dsx1AlmHistoryEntry.setIndexNames((0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:dsx1AlmHistoryEntry.setStatus(_B)
class _AlmlineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AlmlineNumber_Type.__name__=_C
_AlmlineNumber_Object=MibTableColumn
almlineNumber=_AlmlineNumber_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,1),_AlmlineNumber_Type())
almlineNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:almlineNumber.setStatus(_B)
class _AlmIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AlmIntervalNumber_Type.__name__=_C
_AlmIntervalNumber_Object=MibTableColumn
almIntervalNumber=_AlmIntervalNumber_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,2),_AlmIntervalNumber_Type())
almIntervalNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:almIntervalNumber.setStatus(_B)
_LCV_Type=Counter32
_LCV_Object=MibTableColumn
lCV=_LCV_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,3),_LCV_Type())
lCV.setMaxAccess(_E)
if mibBuilder.loadTexts:lCV.setStatus(_B)
_LES_Type=Counter32
_LES_Object=MibTableColumn
lES=_LES_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,4),_LES_Type())
lES.setMaxAccess(_E)
if mibBuilder.loadTexts:lES.setStatus(_B)
_LSES_Type=Counter32
_LSES_Object=MibTableColumn
lSES=_LSES_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,5),_LSES_Type())
lSES.setMaxAccess(_E)
if mibBuilder.loadTexts:lSES.setStatus(_B)
_CRC_Type=Counter32
_CRC_Object=MibTableColumn
cRC=_CRC_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,6),_CRC_Type())
cRC.setMaxAccess(_E)
if mibBuilder.loadTexts:cRC.setStatus(_B)
_CRCES_Type=Counter32
_CRCES_Object=MibTableColumn
cRCES=_CRCES_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,7),_CRCES_Type())
cRCES.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCES.setStatus(_B)
_CRCSES_Type=Counter32
_CRCSES_Object=MibTableColumn
cRCSES=_CRCSES_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,8),_CRCSES_Type())
cRCSES.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCSES.setStatus(_B)
_SEFS_Type=Counter32
_SEFS_Object=MibTableColumn
sEFS=_SEFS_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,9),_SEFS_Type())
sEFS.setMaxAccess(_E)
if mibBuilder.loadTexts:sEFS.setStatus(_B)
_AISS_Type=Counter32
_AISS_Object=MibTableColumn
aISS=_AISS_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,10),_AISS_Type())
aISS.setMaxAccess(_E)
if mibBuilder.loadTexts:aISS.setStatus(_B)
_UAS_Type=Counter32
_UAS_Object=MibTableColumn
uAS=_UAS_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,11),_UAS_Type())
uAS.setMaxAccess(_E)
if mibBuilder.loadTexts:uAS.setStatus(_B)
class _PercentErrorFreeSecs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PercentErrorFreeSecs_Type.__name__=_C
_PercentErrorFreeSecs_Object=MibTableColumn
percentErrorFreeSecs=_PercentErrorFreeSecs_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,12),_PercentErrorFreeSecs_Type())
percentErrorFreeSecs.setMaxAccess(_E)
if mibBuilder.loadTexts:percentErrorFreeSecs.setStatus(_B)
_RcvLOSCnt_Type=Counter32
_RcvLOSCnt_Object=MibTableColumn
rcvLOSCnt=_RcvLOSCnt_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,13),_RcvLOSCnt_Type())
rcvLOSCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvLOSCnt.setStatus(_B)
_RcvOOFCnt_Type=Counter32
_RcvOOFCnt_Object=MibTableColumn
rcvOOFCnt=_RcvOOFCnt_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,14),_RcvOOFCnt_Type())
rcvOOFCnt.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvOOFCnt.setStatus(_B)
_RcvRAICnt_Type=Counter32
_RcvRAICnt_Object=MibTableColumn
rcvRAICnt=_RcvRAICnt_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,15),_RcvRAICnt_Type())
rcvRAICnt.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvRAICnt.setStatus(_B)
_RcvFECnt_Type=Counter32
_RcvFECnt_Object=MibTableColumn
rcvFECnt=_RcvFECnt_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,16),_RcvFECnt_Type())
rcvFECnt.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvFECnt.setStatus(_B)
class _Dsx1AlmClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_Dsx1AlmClrButton_Type.__name__=_C
_Dsx1AlmClrButton_Object=MibTableColumn
dsx1AlmClrButton=_Dsx1AlmClrButton_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,17),_Dsx1AlmClrButton_Type())
dsx1AlmClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx1AlmClrButton.setStatus(_B)
_Dsx1TxUncontrolledSlips_Type=Counter32
_Dsx1TxUncontrolledSlips_Object=MibTableColumn
dsx1TxUncontrolledSlips=_Dsx1TxUncontrolledSlips_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,18),_Dsx1TxUncontrolledSlips_Type())
dsx1TxUncontrolledSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx1TxUncontrolledSlips.setStatus(_B)
_Dsx1RxUncontrolledSlips_Type=Counter32
_Dsx1RxUncontrolledSlips_Object=MibTableColumn
dsx1RxUncontrolledSlips=_Dsx1RxUncontrolledSlips_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,19),_Dsx1RxUncontrolledSlips_Type())
dsx1RxUncontrolledSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx1RxUncontrolledSlips.setStatus(_B)
_Dsx1TxFrameSlips_Type=Counter32
_Dsx1TxFrameSlips_Object=MibTableColumn
dsx1TxFrameSlips=_Dsx1TxFrameSlips_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,20),_Dsx1TxFrameSlips_Type())
dsx1TxFrameSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx1TxFrameSlips.setStatus(_B)
_Dsx1RxFrameSlips_Type=Counter32
_Dsx1RxFrameSlips_Object=MibTableColumn
dsx1RxFrameSlips=_Dsx1RxFrameSlips_Object((1,3,6,1,4,1,351,110,4,3,1,3,2,1,21),_Dsx1RxFrameSlips_Type())
dsx1RxFrameSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx1RxFrameSlips.setStatus(_B)
_Dsx1Vism_ObjectIdentity=ObjectIdentity
dsx1Vism=_Dsx1Vism_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,5))
_Dsx1VismCnfGrp_ObjectIdentity=ObjectIdentity
dsx1VismCnfGrp=_Dsx1VismCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,5,1))
_Dsx1VismCnfGrpTable_Object=MibTable
dsx1VismCnfGrpTable=_Dsx1VismCnfGrpTable_Object((1,3,6,1,4,1,351,110,4,3,5,1,1))
if mibBuilder.loadTexts:dsx1VismCnfGrpTable.setStatus(_B)
_Dsx1VismCnfGrpEntry_Object=MibTableRow
dsx1VismCnfGrpEntry=_Dsx1VismCnfGrpEntry_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1))
dsx1VismCnfGrpEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:dsx1VismCnfGrpEntry.setStatus(_B)
class _VismLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VismLineNum_Type.__name__=_C
_VismLineNum_Object=MibTableColumn
vismLineNum=_VismLineNum_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,1),_VismLineNum_Type())
vismLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLineNum.setStatus(_B)
class _VismEcanEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_VismEcanEnabled_Type.__name__=_C
_VismEcanEnabled_Object=MibTableColumn
vismEcanEnabled=_VismEcanEnabled_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,2),_VismEcanEnabled_Type())
vismEcanEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:vismEcanEnabled.setStatus(_B)
class _VismEcanToneDisable_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ignore',1),('g-164',2),('reserve',3),('g-165',4)))
_VismEcanToneDisable_Type.__name__=_C
_VismEcanToneDisable_Object=MibTableColumn
vismEcanToneDisable=_VismEcanToneDisable_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,3),_VismEcanToneDisable_Type())
vismEcanToneDisable.setMaxAccess(_E)
if mibBuilder.loadTexts:vismEcanToneDisable.setStatus(_F)
class _VismEcanCnfNRN_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reenableOnModemData',1),('reenableOnCallEnd',2)))
_VismEcanCnfNRN_Type.__name__=_C
_VismEcanCnfNRN_Object=MibTableColumn
vismEcanCnfNRN=_VismEcanCnfNRN_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,4),_VismEcanCnfNRN_Type())
vismEcanCnfNRN.setMaxAccess(_E)
if mibBuilder.loadTexts:vismEcanCnfNRN.setStatus(_F)
class _VismEcanTail_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(24,128))
_VismEcanTail_Type.__name__=_C
_VismEcanTail_Object=MibTableColumn
vismEcanTail=_VismEcanTail_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,5),_VismEcanTail_Type())
vismEcanTail.setMaxAccess(_D)
if mibBuilder.loadTexts:vismEcanTail.setStatus(_B)
if mibBuilder.loadTexts:vismEcanTail.setUnits(_A9)
class _VismEcanREC_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cancelOnly',1),('suppressResidual',2),('reserved',3),('comfortNoise',4)))
_VismEcanREC_Type.__name__=_C
_VismEcanREC_Object=MibTableColumn
vismEcanREC=_VismEcanREC_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,6),_VismEcanREC_Type())
vismEcanREC.setMaxAccess(_D)
if mibBuilder.loadTexts:vismEcanREC.setStatus(_B)
class _VismCompCnfVAD_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_VismCompCnfVAD_Type.__name__=_C
_VismCompCnfVAD_Object=MibTableColumn
vismCompCnfVAD=_VismCompCnfVAD_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,7),_VismCompCnfVAD_Type())
vismCompCnfVAD.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCompCnfVAD.setStatus(_B)
class _VismSignalingType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cas',1),('ccs',2),('none',3)))
_VismSignalingType_Type.__name__=_C
_VismSignalingType_Object=MibTableColumn
vismSignalingType=_VismSignalingType_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,8),_VismSignalingType_Type())
vismSignalingType.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSignalingType.setStatus(_B)
class _VismCcsChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismCcsChannels_Type.__name__=_C
_VismCcsChannels_Object=MibTableColumn
vismCcsChannels=_VismCcsChannels_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,9),_VismCcsChannels_Type())
vismCcsChannels.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCcsChannels.setStatus(_B)
class _VismCadenceTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,200))
_VismCadenceTime_Type.__name__=_C
_VismCadenceTime_Object=MibTableColumn
vismCadenceTime=_VismCadenceTime_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,10),_VismCadenceTime_Type())
vismCadenceTime.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCadenceTime.setStatus(_F)
if mibBuilder.loadTexts:vismCadenceTime.setUnits(_A9)
class _VismTrunkConditionEnable_Type(TruthValue):defaultValue=2
_VismTrunkConditionEnable_Type.__name__=_H
_VismTrunkConditionEnable_Object=MibTableColumn
vismTrunkConditionEnable=_VismTrunkConditionEnable_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,11),_VismTrunkConditionEnable_Type())
vismTrunkConditionEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:vismTrunkConditionEnable.setStatus(_B)
_VismDsx1CircuitIdentifier_Type=DisplayString
_VismDsx1CircuitIdentifier_Object=MibTableColumn
vismDsx1CircuitIdentifier=_VismDsx1CircuitIdentifier_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,12),_VismDsx1CircuitIdentifier_Type())
vismDsx1CircuitIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1CircuitIdentifier.setStatus(_B)
class _VismDsx1TxDigitOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aniThenDnis',1),('dnisThenAni',2)))
_VismDsx1TxDigitOrder_Type.__name__=_C
_VismDsx1TxDigitOrder_Object=MibTableColumn
vismDsx1TxDigitOrder=_VismDsx1TxDigitOrder_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,13),_VismDsx1TxDigitOrder_Type())
vismDsx1TxDigitOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1TxDigitOrder.setStatus(_B)
class _VismDsx1TonePlanRegion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismDsx1TonePlanRegion_Type.__name__=_A7
_VismDsx1TonePlanRegion_Object=MibTableColumn
vismDsx1TonePlanRegion=_VismDsx1TonePlanRegion_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,14),_VismDsx1TonePlanRegion_Type())
vismDsx1TonePlanRegion.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1TonePlanRegion.setStatus(_B)
class _VismDsx1TonePlanVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismDsx1TonePlanVersion_Type.__name__=_C
_VismDsx1TonePlanVersion_Object=MibTableColumn
vismDsx1TonePlanVersion=_VismDsx1TonePlanVersion_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,15),_VismDsx1TonePlanVersion_Type())
vismDsx1TonePlanVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1TonePlanVersion.setStatus(_B)
class _VismDsx1RingingTO_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1RingingTO_Type.__name__=_C
_VismDsx1RingingTO_Object=MibTableColumn
vismDsx1RingingTO=_VismDsx1RingingTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,16),_VismDsx1RingingTO_Type())
vismDsx1RingingTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1RingingTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1RingingTO.setUnits(_G)
class _VismDsx1RingBackTO_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1RingBackTO_Type.__name__=_C
_VismDsx1RingBackTO_Object=MibTableColumn
vismDsx1RingBackTO=_VismDsx1RingBackTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,17),_VismDsx1RingBackTO_Type())
vismDsx1RingBackTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1RingBackTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1RingBackTO.setUnits(_G)
class _VismDsx1BusyTO_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1BusyTO_Type.__name__=_C
_VismDsx1BusyTO_Object=MibTableColumn
vismDsx1BusyTO=_VismDsx1BusyTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,18),_VismDsx1BusyTO_Type())
vismDsx1BusyTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1BusyTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1BusyTO.setUnits(_G)
class _VismDsx1ReorderTO_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1ReorderTO_Type.__name__=_C
_VismDsx1ReorderTO_Object=MibTableColumn
vismDsx1ReorderTO=_VismDsx1ReorderTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,19),_VismDsx1ReorderTO_Type())
vismDsx1ReorderTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1ReorderTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1ReorderTO.setUnits(_G)
class _VismDsx1DialTO_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1DialTO_Type.__name__=_C
_VismDsx1DialTO_Object=MibTableColumn
vismDsx1DialTO=_VismDsx1DialTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,20),_VismDsx1DialTO_Type())
vismDsx1DialTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1DialTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1DialTO.setUnits(_G)
class _VismDsx1StutterDialTO_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1StutterDialTO_Type.__name__=_C
_VismDsx1StutterDialTO_Object=MibTableColumn
vismDsx1StutterDialTO=_VismDsx1StutterDialTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,21),_VismDsx1StutterDialTO_Type())
vismDsx1StutterDialTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1StutterDialTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1StutterDialTO.setUnits(_G)
class _VismDsx1OffHookAlertTO_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_VismDsx1OffHookAlertTO_Type.__name__=_C
_VismDsx1OffHookAlertTO_Object=MibTableColumn
vismDsx1OffHookAlertTO=_VismDsx1OffHookAlertTO_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,22),_VismDsx1OffHookAlertTO_Type())
vismDsx1OffHookAlertTO.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1OffHookAlertTO.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1OffHookAlertTO.setUnits(_G)
class _VismDsx1RemoteRingback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proxy',1),('inband',2)))
_VismDsx1RemoteRingback_Type.__name__=_C
_VismDsx1RemoteRingback_Object=MibTableColumn
vismDsx1RemoteRingback=_VismDsx1RemoteRingback_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,23),_VismDsx1RemoteRingback_Type())
vismDsx1RemoteRingback.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1RemoteRingback.setStatus(_B)
class _VismDsx1MidcallTpart_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_VismDsx1MidcallTpart_Type.__name__=_C
_VismDsx1MidcallTpart_Object=MibTableColumn
vismDsx1MidcallTpart=_VismDsx1MidcallTpart_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,24),_VismDsx1MidcallTpart_Type())
vismDsx1MidcallTpart.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1MidcallTpart.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1MidcallTpart.setUnits(_G)
class _VismDsx1MidcallTcrit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_VismDsx1MidcallTcrit_Type.__name__=_C
_VismDsx1MidcallTcrit_Object=MibTableColumn
vismDsx1MidcallTcrit=_VismDsx1MidcallTcrit_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,25),_VismDsx1MidcallTcrit_Type())
vismDsx1MidcallTcrit.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1MidcallTcrit.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1MidcallTcrit.setUnits(_G)
class _VismDsx1Sa4Byte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismDsx1Sa4Byte_Type.__name__=_C
_VismDsx1Sa4Byte_Object=MibTableColumn
vismDsx1Sa4Byte=_VismDsx1Sa4Byte_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,26),_VismDsx1Sa4Byte_Type())
vismDsx1Sa4Byte.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1Sa4Byte.setStatus(_B)
class _VismDsx1Sa5Byte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismDsx1Sa5Byte_Type.__name__=_C
_VismDsx1Sa5Byte_Object=MibTableColumn
vismDsx1Sa5Byte=_VismDsx1Sa5Byte_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,27),_VismDsx1Sa5Byte_Type())
vismDsx1Sa5Byte.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1Sa5Byte.setStatus(_B)
class _VismDsx1Sa6Byte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismDsx1Sa6Byte_Type.__name__=_C
_VismDsx1Sa6Byte_Object=MibTableColumn
vismDsx1Sa6Byte=_VismDsx1Sa6Byte_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,28),_VismDsx1Sa6Byte_Type())
vismDsx1Sa6Byte.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1Sa6Byte.setStatus(_B)
class _VismDsx1Sa7Byte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismDsx1Sa7Byte_Type.__name__=_C
_VismDsx1Sa7Byte_Object=MibTableColumn
vismDsx1Sa7Byte=_VismDsx1Sa7Byte_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,29),_VismDsx1Sa7Byte_Type())
vismDsx1Sa7Byte.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1Sa7Byte.setStatus(_B)
class _VismDsx1Sa8Byte_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismDsx1Sa8Byte_Type.__name__=_C
_VismDsx1Sa8Byte_Object=MibTableColumn
vismDsx1Sa8Byte=_VismDsx1Sa8Byte_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,30),_VismDsx1Sa8Byte_Type())
vismDsx1Sa8Byte.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1Sa8Byte.setStatus(_B)
class _VismDsx1State_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('invalid',1),('is',2),('oos',3),('poos',4),('coos',5),('inactive',6)))
_VismDsx1State_Type.__name__=_C
_VismDsx1State_Object=MibTableColumn
vismDsx1State=_VismDsx1State_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,31),_VismDsx1State_Type())
vismDsx1State.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDsx1State.setStatus(_B)
class _VismDsx1AdminStateControl_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inService',1),('forcefulOutOfService',2),('gracefulOutOfService',3),('inactive',4)))
_VismDsx1AdminStateControl_Type.__name__=_C
_VismDsx1AdminStateControl_Object=MibTableColumn
vismDsx1AdminStateControl=_VismDsx1AdminStateControl_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,32),_VismDsx1AdminStateControl_Type())
vismDsx1AdminStateControl.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1AdminStateControl.setStatus(_B)
class _VismBearerBusyCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismBearerBusyCode_Type.__name__=_C
_VismBearerBusyCode_Object=MibTableColumn
vismBearerBusyCode=_VismBearerBusyCode_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,33),_VismBearerBusyCode_Type())
vismBearerBusyCode.setMaxAccess(_D)
if mibBuilder.loadTexts:vismBearerBusyCode.setStatus(_B)
class _VismDsx1V110Enable_Type(TruthValue):defaultValue=2
_VismDsx1V110Enable_Type.__name__=_H
_VismDsx1V110Enable_Object=MibTableColumn
vismDsx1V110Enable=_VismDsx1V110Enable_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,34),_VismDsx1V110Enable_Type())
vismDsx1V110Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1V110Enable.setStatus(_B)
class _VismDsx1AlarmLogEnable_Type(TruthValue):defaultValue=2
_VismDsx1AlarmLogEnable_Type.__name__=_H
_VismDsx1AlarmLogEnable_Object=MibTableColumn
vismDsx1AlarmLogEnable=_VismDsx1AlarmLogEnable_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,35),_VismDsx1AlarmLogEnable_Type())
vismDsx1AlarmLogEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1AlarmLogEnable.setStatus(_B)
class _VismDsx1AlarmLogAdminTimer_Type(Unsigned32):defaultValue=7200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismDsx1AlarmLogAdminTimer_Type.__name__=_r
_VismDsx1AlarmLogAdminTimer_Object=MibTableColumn
vismDsx1AlarmLogAdminTimer=_VismDsx1AlarmLogAdminTimer_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,36),_VismDsx1AlarmLogAdminTimer_Type())
vismDsx1AlarmLogAdminTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1AlarmLogAdminTimer.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1AlarmLogAdminTimer.setUnits('minutes')
class _VismDsx1AlarmLogOperTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismDsx1AlarmLogOperTimer_Type.__name__=_r
_VismDsx1AlarmLogOperTimer_Object=MibTableColumn
vismDsx1AlarmLogOperTimer=_VismDsx1AlarmLogOperTimer_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,37),_VismDsx1AlarmLogOperTimer_Type())
vismDsx1AlarmLogOperTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDsx1AlarmLogOperTimer.setStatus(_B)
if mibBuilder.loadTexts:vismDsx1AlarmLogOperTimer.setUnits('minutes')
class _VismDsx1ElectricalSignalEnable_Type(TruthValue):defaultValue=1
_VismDsx1ElectricalSignalEnable_Type.__name__=_H
_VismDsx1ElectricalSignalEnable_Object=MibTableColumn
vismDsx1ElectricalSignalEnable=_VismDsx1ElectricalSignalEnable_Object((1,3,6,1,4,1,351,110,4,3,5,1,1,1,38),_VismDsx1ElectricalSignalEnable_Type())
vismDsx1ElectricalSignalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:vismDsx1ElectricalSignalEnable.setStatus(_B)
_Dsx1VismStatsGrp_ObjectIdentity=ObjectIdentity
dsx1VismStatsGrp=_Dsx1VismStatsGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,5,2))
_Dsx1VismStatsGrpTable_Object=MibTable
dsx1VismStatsGrpTable=_Dsx1VismStatsGrpTable_Object((1,3,6,1,4,1,351,110,4,3,5,2,1))
if mibBuilder.loadTexts:dsx1VismStatsGrpTable.setStatus(_B)
_Dsx1VismStatsGrpEntry_Object=MibTableRow
dsx1VismStatsGrpEntry=_Dsx1VismStatsGrpEntry_Object((1,3,6,1,4,1,351,110,4,3,5,2,1,1))
if mibBuilder.loadTexts:dsx1VismStatsGrpEntry.setStatus(_B)
_VismDsx1TotalTxUncontrolledSlips_Type=Counter32
_VismDsx1TotalTxUncontrolledSlips_Object=MibTableColumn
vismDsx1TotalTxUncontrolledSlips=_VismDsx1TotalTxUncontrolledSlips_Object((1,3,6,1,4,1,351,110,4,3,5,2,1,1,1),_VismDsx1TotalTxUncontrolledSlips_Type())
vismDsx1TotalTxUncontrolledSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDsx1TotalTxUncontrolledSlips.setStatus(_B)
_VismDsx1TotalTxFrameSlips_Type=Counter32
_VismDsx1TotalTxFrameSlips_Object=MibTableColumn
vismDsx1TotalTxFrameSlips=_VismDsx1TotalTxFrameSlips_Object((1,3,6,1,4,1,351,110,4,3,5,2,1,1,2),_VismDsx1TotalTxFrameSlips_Type())
vismDsx1TotalTxFrameSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDsx1TotalTxFrameSlips.setStatus(_B)
_VismDsx1TotalRxUncontrolledSlips_Type=Counter32
_VismDsx1TotalRxUncontrolledSlips_Object=MibTableColumn
vismDsx1TotalRxUncontrolledSlips=_VismDsx1TotalRxUncontrolledSlips_Object((1,3,6,1,4,1,351,110,4,3,5,2,1,1,3),_VismDsx1TotalRxUncontrolledSlips_Type())
vismDsx1TotalRxUncontrolledSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDsx1TotalRxUncontrolledSlips.setStatus(_B)
_VismDsx1TotalRxFrameSlips_Type=Counter32
_VismDsx1TotalRxFrameSlips_Object=MibTableColumn
vismDsx1TotalRxFrameSlips=_VismDsx1TotalRxFrameSlips_Object((1,3,6,1,4,1,351,110,4,3,5,2,1,1,4),_VismDsx1TotalRxFrameSlips_Type())
vismDsx1TotalRxFrameSlips.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDsx1TotalRxFrameSlips.setStatus(_B)
class _VismSlipCntDiscontinuityTime_Type(TimeStamp):defaultValue=0
_VismSlipCntDiscontinuityTime_Type.__name__=_A8
_VismSlipCntDiscontinuityTime_Object=MibTableColumn
vismSlipCntDiscontinuityTime=_VismSlipCntDiscontinuityTime_Object((1,3,6,1,4,1,351,110,4,3,5,2,1,1,5),_VismSlipCntDiscontinuityTime_Type())
vismSlipCntDiscontinuityTime.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSlipCntDiscontinuityTime.setStatus(_B)
_CvDsx1MIBConformance_ObjectIdentity=ObjectIdentity
cvDsx1MIBConformance=_CvDsx1MIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,79,2))
_CvDsx1MIBGroups_ObjectIdentity=ObjectIdentity
cvDsx1MIBGroups=_CvDsx1MIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,79,2,1))
_CvDsx1MIBCompliances_ObjectIdentity=ObjectIdentity
cvDsx1MIBCompliances=_CvDsx1MIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,79,2,2))
dsx1VismCnfGrpEntry.registerAugmentions((_A,_AA))
dsx1VismStatsGrpEntry.setIndexNames(*dsx1VismCnfGrpEntry.getIndexNames())
cvDsx1ConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,1))
cvDsx1ConfGroup.setObjects(*((_A,_I),(_A,_M),(_A,_AB),(_A,_AC),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_AD),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cvDsx1ConfGroup.setStatus(_F)
cvDsx1AlmHistoryGroup=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,2))
cvDsx1AlmHistoryGroup.setObjects(*((_A,_K),(_A,_L),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,'uAS'),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cvDsx1AlmHistoryGroup.setStatus(_F)
cvDsx1ConfGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,3))
cvDsx1ConfGroupRev1.setObjects(*((_A,_I),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cvDsx1ConfGroupRev1.setStatus(_F)
cvDsx1ConfGroupRev2=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,4))
cvDsx1ConfGroupRev2.setObjects(*((_A,_I),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_AE)))
if mibBuilder.loadTexts:cvDsx1ConfGroupRev2.setStatus(_B)
cvDsx1AlmHistoryGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,5))
cvDsx1AlmHistoryGroupRev1.setObjects(*((_A,_K),(_A,_L),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,'uAS'),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:cvDsx1AlmHistoryGroupRev1.setStatus(_B)
cvDsx1StatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,6))
cvDsx1StatsGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cvDsx1StatsGroup.setStatus(_B)
cvDsx1ConfGroupSup1=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,7))
cvDsx1ConfGroupSup1.setObjects((_A,_AO))
if mibBuilder.loadTexts:cvDsx1ConfGroupSup1.setStatus(_B)
cvDsx1AlarmLogGroup=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,8))
cvDsx1AlarmLogGroup.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:cvDsx1AlarmLogGroup.setStatus(_B)
cvDsx1ElecSigGroup=ObjectGroup((1,3,6,1,4,1,351,150,79,2,1,9))
cvDsx1ElecSigGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:cvDsx1ElecSigGroup.setStatus(_B)
cvDsx1Compliance=ModuleCompliance((1,3,6,1,4,1,351,150,79,2,2,1))
cvDsx1Compliance.setObjects(*((_A,_AT),(_A,_o)))
if mibBuilder.loadTexts:cvDsx1Compliance.setStatus(_F)
cvDsx1ComplianceRev1=ModuleCompliance((1,3,6,1,4,1,351,150,79,2,2,2))
cvDsx1ComplianceRev1.setObjects(*((_A,_AU),(_A,_o)))
if mibBuilder.loadTexts:cvDsx1ComplianceRev1.setStatus(_F)
cvDsx1ComplianceRev2=ModuleCompliance((1,3,6,1,4,1,351,150,79,2,2,3))
cvDsx1ComplianceRev2.setObjects(*((_A,_J),(_A,_o)))
if mibBuilder.loadTexts:cvDsx1ComplianceRev2.setStatus(_F)
cvDsx1ComplianceRev3=ModuleCompliance((1,3,6,1,4,1,351,150,79,2,2,4))
cvDsx1ComplianceRev3.setObjects(*((_A,_J),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cvDsx1ComplianceRev3.setStatus(_F)
cvDsx1ComplianceRev4=ModuleCompliance((1,3,6,1,4,1,351,150,79,2,2,5))
cvDsx1ComplianceRev4.setObjects(*((_A,_J),(_A,_p),(_A,_q),(_A,_A6)))
if mibBuilder.loadTexts:cvDsx1ComplianceRev4.setStatus(_F)
cvDsx1ComplianceRev5=ModuleCompliance((1,3,6,1,4,1,351,150,79,2,2,6))
cvDsx1ComplianceRev5.setObjects(*((_A,_J),(_A,_p),(_A,_q),(_A,_A6),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:cvDsx1ComplianceRev5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'dsx1AlmHistoryTable':dsx1AlmHistoryTable,'dsx1AlmHistoryEntry':dsx1AlmHistoryEntry,_K:almlineNumber,_L:almIntervalNumber,_s:lCV,_t:lES,_u:lSES,_v:cRC,_w:cRCES,_x:cRCSES,_y:sEFS,_z:aISS,'uAS':uAS,_A0:percentErrorFreeSecs,_A1:rcvLOSCnt,_A2:rcvOOFCnt,_A3:rcvRAICnt,_A4:rcvFECnt,_A5:dsx1AlmClrButton,_AF:dsx1TxUncontrolledSlips,_AH:dsx1RxUncontrolledSlips,_AG:dsx1TxFrameSlips,_AI:dsx1RxFrameSlips,'dsx1Vism':dsx1Vism,'dsx1VismCnfGrp':dsx1VismCnfGrp,'dsx1VismCnfGrpTable':dsx1VismCnfGrpTable,'dsx1VismCnfGrpEntry':dsx1VismCnfGrpEntry,_I:vismLineNum,_M:vismEcanEnabled,_AB:vismEcanToneDisable,_AC:vismEcanCnfNRN,_N:vismEcanTail,_O:vismEcanREC,_P:vismCompCnfVAD,_Q:vismSignalingType,_R:vismCcsChannels,_AD:vismCadenceTime,_S:vismTrunkConditionEnable,_T:vismDsx1CircuitIdentifier,_U:vismDsx1TxDigitOrder,_V:vismDsx1TonePlanRegion,_W:vismDsx1TonePlanVersion,_X:vismDsx1RingingTO,_Y:vismDsx1RingBackTO,_Z:vismDsx1BusyTO,_a:vismDsx1ReorderTO,_b:vismDsx1DialTO,_c:vismDsx1StutterDialTO,_d:vismDsx1OffHookAlertTO,_e:vismDsx1RemoteRingback,_f:vismDsx1MidcallTpart,_g:vismDsx1MidcallTcrit,_h:vismDsx1Sa4Byte,_i:vismDsx1Sa5Byte,_j:vismDsx1Sa6Byte,_k:vismDsx1Sa7Byte,_l:vismDsx1Sa8Byte,_m:vismDsx1State,_n:vismDsx1AdminStateControl,_AE:vismBearerBusyCode,_AO:vismDsx1V110Enable,_AP:vismDsx1AlarmLogEnable,_AQ:vismDsx1AlarmLogAdminTimer,_AR:vismDsx1AlarmLogOperTimer,_AS:vismDsx1ElectricalSignalEnable,'dsx1VismStatsGrp':dsx1VismStatsGrp,'dsx1VismStatsGrpTable':dsx1VismStatsGrpTable,_AA:dsx1VismStatsGrpEntry,_AJ:vismDsx1TotalTxUncontrolledSlips,_AK:vismDsx1TotalTxFrameSlips,_AL:vismDsx1TotalRxUncontrolledSlips,_AM:vismDsx1TotalRxFrameSlips,_AN:vismSlipCntDiscontinuityTime,'ciscoVismDsx1MIB':ciscoVismDsx1MIB,'cvDsx1MIBConformance':cvDsx1MIBConformance,'cvDsx1MIBGroups':cvDsx1MIBGroups,_AT:cvDsx1ConfGroup,_o:cvDsx1AlmHistoryGroup,_AU:cvDsx1ConfGroupRev1,_J:cvDsx1ConfGroupRev2,_p:cvDsx1AlmHistoryGroupRev1,_q:cvDsx1StatsGroup,_A6:cvDsx1ConfGroupSup1,_AV:cvDsx1AlarmLogGroup,_AW:cvDsx1ElecSigGroup,'cvDsx1MIBCompliances':cvDsx1MIBCompliances,'cvDsx1Compliance':cvDsx1Compliance,'cvDsx1ComplianceRev1':cvDsx1ComplianceRev1,'cvDsx1ComplianceRev2':cvDsx1ComplianceRev2,'cvDsx1ComplianceRev3':cvDsx1ComplianceRev3,'cvDsx1ComplianceRev4':cvDsx1ComplianceRev4,'cvDsx1ComplianceRev5':cvDsx1ComplianceRev5})