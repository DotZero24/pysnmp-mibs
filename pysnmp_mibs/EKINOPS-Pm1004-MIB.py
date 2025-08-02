_Ap='pm1004PerfLinePast24CntIndex'
_Ao='pm1004PerfLineCurrent24CntIndex'
_An='pm1004PerfLinePast15CntIndex'
_Am='pm1004PerfLineCurrent15CntIndex'
_Al='pm1004Almj0AlarmIndex'
_Ak='pm1004PerfUpPast24CntIndex'
_Aj='pm1004PerfUpCurrent24CntIndex'
_Ai='pm1004PerfUpPast15CntIndex'
_Ah='pm1004PerfUpCurrent15CntIndex'
_Ag='pm1004CfgOtxtlhcapabilitiesIndex'
_Af='pm1004CfgOtxtlhIndex'
_Ae='pm1004CfgLabellineIndex'
_Ad='pm1004CfgLabelclientIndex'
_Ac='pm1004CfgEmptyIndex'
_Ab='pm1004CfgXfpIndex'
_Aa='pm1004CfgClientStartupIndex'
_AZ='pm1004CfgClientcaiscsfIndex'
_AY='pm1004RinvLineIndex'
_AX='pm1004RinvSfpIndex'
_AW='pm1004CtrllinePowerLaserIndex'
_AV='pm1004CtrllinePhotodiodeValueIndex'
_AU='pm1004CtrllinePhotodiodeModeIndex'
_AT='pm1004CtrllineTunableChannelIndex'
_AS='pm1004CtrlxfpXfiLoopIndex'
_AR='pm1004CtrlxfpLineLoopIndex'
_AQ='pm1004CtrlxfpOnoffIndex'
_AP='pm1004CtrllineResetCount24LineIndex'
_AO='pm1004CtrllineResetCount15LineIndex'
_AN='pm1004CtrllineOosModeIndex'
_AM='pm1004CtrlfecDisableIndex'
_AL='pm1004CtrlprotocolIndex'
_AK='pm1004CtrlresetCount24PortIndex'
_AJ='pm1004CtrlresetCount15PortIndex'
_AI='pm1004CtrlclientAccessTermLoopIndex'
_AH='pm1004CtrlcaisDwInsIndex'
_AG='pm1004CtrlcsfUpInsIndex'
_AF='pm1004CtrlsfpOffCtrlIndex'
_AE='pm1004CtrlsfpOnCtrlIndex'
_AD='pm1004CtrlportOosModeIndex'
_AC='pm1004CtrlaccessLoopIndex'
_AB='pm1004CntdfrmPrimLineErrCntIndex'
_AA='pm1004CntdfrmTimCntIndex'
_A9='pm1004CntdfrmB1ErrCntIndex'
_A8='pm1004CntdwTimCntIndex'
_A7='pm1004CntdwCbipCntIndex'
_A6='pm1004CntupCvErrCntIndex'
_A5='pm1004CntupTimCntIndex'
_A4='pm1004CntupRdErrCntIndex'
_A3='pm1004CntupRaInsCntIndex'
_A2='pm1004CntupRaRemCntIndex'
_A1='pm1004Mesrotx1LaserWvlengthIndex'
_A0='pm1004Mesrotx1FreqDeviationIndex'
_z='pm1004Mesrotx1LaserTemperatureIndex'
_y='pm1004Mesrotx1AgingIndex'
_x='pm1004Mesrxfp1LxAux2MeasIndex'
_w='pm1004Mesrxfp1LxAux1MeasIndex'
_v='pm1004Mesrxfp1LiRxPowerMeasIndex'
_u='pm1004Mesrxfp1LoTxPowerMeasIndex'
_t='pm1004Mesrxfp1LoBiasCurrentMeasIndex'
_s='pm1004Mesrxfp1ReservedIndex'
_r='pm1004Mesrxfp1LxModTempMeasIndex'
_q='pm1004MesrrxpwrMeasIndex'
_p='pm1004MesrtxpwrMeasIndex'
_o='pm1004MesrbiasMeasIndex'
_n='pm1004MesrvoltMeasIndex'
_m='pm1004MesrtempMeasIndex'
_l='pm1004AlmlineXfp1AlarmsIndex'
_k='pm1004AlmlineSyncAlarmsIndex'
_j='pm1004AlmdfrmAlmIndex'
_i='pm1004AlmsynthAlmLineIndex'
_h='pm1004AlmlineOtx1TlhAlarmsIndex'
_g='pm1004AlmlineXfp1SupplyAlarmIndex'
_f='pm1004AlmlineXfp1AlarmIndex'
_e='pm1004AlmdfrmBerIndex'
_d='pm1004AlmlineOtx1TlhWarningsIndex'
_c='pm1004AlmlineXfp1WarningsIndex'
_b='pm1004AlmaccessioSdhAlarmIndex'
_a='pm1004AlmmapperDeAlmIndex'
_Z='pm1004AlmaccessioAlmIndex'
_Y='pm1004AlmsynthAlmPortIndex'
_X='pm1004AlmsfpAlmDdmIndex'
_W='pm1004Almk1K2ClientIndex'
_V='pm1004AlmsfpWarnDdmIndex'
_U='pm1004AlmDefFuseA'
_T='pm1004AlmDefFuseB'
_S='pm1004AlmHwFailAccPortn'
_R='pm1004AlmFailAccPortn'
_Q='pm1004AlmSfpDdmAlmPortn'
_P='pm1004AlmSfpDdmWarningPortn'
_O='pm1004AlmLineHwFailPortn'
_N='pm1004AlmLineFailPortn'
_M='pm1004AlmLineDdmAlmPortn'
_L='pm1004AlmLineDdmWarningPortn'
_K='DisplayString'
_J='pm1004trapPortNumber'
_I='pm1004trapLineNumber'
_H='pm1004trapBoardNumber'
_G='deprecated'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='EKINOPS-Pm1004-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
modulePm1004=ModuleIdentity((1,3,6,1,4,1,20044,18))
if mibBuilder.loadTexts:modulePm1004.setRevisions(('2006-11-10 00:00','2007-02-21 00:00','2007-06-27 00:00','2007-09-27 00:00','2007-11-14 00:00','2008-07-01 00:00','2009-03-16 00:00','2009-04-07 00:00','2009-04-09 00:00','2009-05-15 00:00','2010-01-28 00:00','2010-02-18 00:00','2010-03-18 00:00','2010-11-09 00:00','2012-07-03 00:00','2013-04-02 00:00','2014-03-27 00:00','2014-12-22 00:00','2016-05-19 00:00','2016-06-02 00:00'))
class Pm1004OtxMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('otx80mode',1),('otx60mode',2),('otxadjustmode',4)))
class Pm1004OtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pm1004AdjustValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('otxadjustvalue0',0),('otxadjustvalue1',1),('otxadjustvalue2',2),('otxadjustvalue3',3),('otxadjustvalue4',4),('otxadjustvalue5',5),('otxadjustvalue6',6),('otxadjustvalue7',7),('otxadjustvalue8',8),('otxadjustvalue9',9),('otxadjustvalue10',10)))
class Pm1004OtxChannel(TextualConvention,Integer32):status=_A
_Pm1004alarms_ObjectIdentity=ObjectIdentity
pm1004alarms=_Pm1004alarms_ObjectIdentity((1,3,6,1,4,1,20044,18,2))
_Pm1004AlmOther_ObjectIdentity=ObjectIdentity
pm1004AlmOther=_Pm1004AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1))
_Pm1004AlmOtherNurg_ObjectIdentity=ObjectIdentity
pm1004AlmOtherNurg=_Pm1004AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,1))
_Pm1004AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm1004AlmsynthAlm2=_Pm1004AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,1,2))
_Pm1004AlmConfTableSave_Type=EkiOnOff
_Pm1004AlmConfTableSave_Object=MibScalar
pm1004AlmConfTableSave=_Pm1004AlmConfTableSave_Object((1,3,6,1,4,1,20044,18,2,1,1,2,1),_Pm1004AlmConfTableSave_Type())
pm1004AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmConfTableSave.setStatus(_A)
_Pm1004AlmInvUpload_Type=EkiOnOff
_Pm1004AlmInvUpload_Object=MibScalar
pm1004AlmInvUpload=_Pm1004AlmInvUpload_Object((1,3,6,1,4,1,20044,18,2,1,1,2,2),_Pm1004AlmInvUpload_Type())
pm1004AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmInvUpload.setStatus(_A)
_Pm1004AlmConfTableLoad_Type=EkiOnOff
_Pm1004AlmConfTableLoad_Object=MibScalar
pm1004AlmConfTableLoad=_Pm1004AlmConfTableLoad_Object((1,3,6,1,4,1,20044,18,2,1,1,2,3),_Pm1004AlmConfTableLoad_Type())
pm1004AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmConfTableLoad.setStatus(_A)
_Pm1004AlmCorrelatOff_Type=EkiOnOff
_Pm1004AlmCorrelatOff_Object=MibScalar
pm1004AlmCorrelatOff=_Pm1004AlmCorrelatOff_Object((1,3,6,1,4,1,20044,18,2,1,1,2,4),_Pm1004AlmCorrelatOff_Type())
pm1004AlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmCorrelatOff.setStatus(_A)
_Pm1004AlmMaintenanceOn_Type=EkiOnOff
_Pm1004AlmMaintenanceOn_Object=MibScalar
pm1004AlmMaintenanceOn=_Pm1004AlmMaintenanceOn_Object((1,3,6,1,4,1,20044,18,2,1,1,2,5),_Pm1004AlmMaintenanceOn_Type())
pm1004AlmMaintenanceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmMaintenanceOn.setStatus(_A)
_Pm1004AlmOtherUrg_ObjectIdentity=ObjectIdentity
pm1004AlmOtherUrg=_Pm1004AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,2))
_Pm1004AlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pm1004AlmmodInitFailLevel2=_Pm1004AlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,2,194))
_Pm1004AlmLedFail_Type=EkiOnOff
_Pm1004AlmLedFail_Object=MibScalar
pm1004AlmLedFail=_Pm1004AlmLedFail_Object((1,3,6,1,4,1,20044,18,2,1,2,194,1),_Pm1004AlmLedFail_Type())
pm1004AlmLedFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLedFail.setStatus(_A)
_Pm1004AlmNextColdBootForced_Type=EkiOnOff
_Pm1004AlmNextColdBootForced_Object=MibScalar
pm1004AlmNextColdBootForced=_Pm1004AlmNextColdBootForced_Object((1,3,6,1,4,1,20044,18,2,1,2,194,2),_Pm1004AlmNextColdBootForced_Type())
pm1004AlmNextColdBootForced.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmNextColdBootForced.setStatus(_A)
_Pm1004AlmBootUndone_Type=EkiOnOff
_Pm1004AlmBootUndone_Object=MibScalar
pm1004AlmBootUndone=_Pm1004AlmBootUndone_Object((1,3,6,1,4,1,20044,18,2,1,2,194,3),_Pm1004AlmBootUndone_Type())
pm1004AlmBootUndone.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmBootUndone.setStatus(_A)
_Pm1004AlmResetHwInitFail_Type=EkiOnOff
_Pm1004AlmResetHwInitFail_Object=MibScalar
pm1004AlmResetHwInitFail=_Pm1004AlmResetHwInitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,194,4),_Pm1004AlmResetHwInitFail_Type())
pm1004AlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmResetHwInitFail.setStatus(_A)
_Pm1004AlmSwInitFail_Type=EkiOnOff
_Pm1004AlmSwInitFail_Object=MibScalar
pm1004AlmSwInitFail=_Pm1004AlmSwInitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,194,5),_Pm1004AlmSwInitFail_Type())
pm1004AlmSwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmSwInitFail.setStatus(_A)
_Pm1004AlmmodInitFailLevel3_ObjectIdentity=ObjectIdentity
pm1004AlmmodInitFailLevel3=_Pm1004AlmmodInitFailLevel3_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,2,195))
_Pm1004AlmGwIdentFail_Type=EkiOnOff
_Pm1004AlmGwIdentFail_Object=MibScalar
pm1004AlmGwIdentFail=_Pm1004AlmGwIdentFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,1),_Pm1004AlmGwIdentFail_Type())
pm1004AlmGwIdentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmGwIdentFail.setStatus(_A)
_Pm1004AlmObmTypeReadFail_Type=EkiOnOff
_Pm1004AlmObmTypeReadFail_Object=MibScalar
pm1004AlmObmTypeReadFail=_Pm1004AlmObmTypeReadFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,2),_Pm1004AlmObmTypeReadFail_Type())
pm1004AlmObmTypeReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmObmTypeReadFail.setStatus(_A)
_Pm1004AlmInitModuleFail_Type=EkiOnOff
_Pm1004AlmInitModuleFail_Object=MibScalar
pm1004AlmInitModuleFail=_Pm1004AlmInitModuleFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,3),_Pm1004AlmInitModuleFail_Type())
pm1004AlmInitModuleFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmInitModuleFail.setStatus(_A)
_Pm1004AlmXfp1InitFail_Type=EkiOnOff
_Pm1004AlmXfp1InitFail_Object=MibScalar
pm1004AlmXfp1InitFail=_Pm1004AlmXfp1InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,5),_Pm1004AlmXfp1InitFail_Type())
pm1004AlmXfp1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmXfp1InitFail.setStatus(_A)
_Pm1004AlmXfp2InitFail_Type=EkiOnOff
_Pm1004AlmXfp2InitFail_Object=MibScalar
pm1004AlmXfp2InitFail=_Pm1004AlmXfp2InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,6),_Pm1004AlmXfp2InitFail_Type())
pm1004AlmXfp2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmXfp2InitFail.setStatus(_A)
_Pm1004AlmLine1InitFail_Type=EkiOnOff
_Pm1004AlmLine1InitFail_Object=MibScalar
pm1004AlmLine1InitFail=_Pm1004AlmLine1InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,7),_Pm1004AlmLine1InitFail_Type())
pm1004AlmLine1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLine1InitFail.setStatus(_A)
_Pm1004AlmLine2InitFail_Type=EkiOnOff
_Pm1004AlmLine2InitFail_Object=MibScalar
pm1004AlmLine2InitFail=_Pm1004AlmLine2InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,8),_Pm1004AlmLine2InitFail_Type())
pm1004AlmLine2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLine2InitFail.setStatus(_A)
_Pm1004AlmClient1InitFail_Type=EkiOnOff
_Pm1004AlmClient1InitFail_Object=MibScalar
pm1004AlmClient1InitFail=_Pm1004AlmClient1InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,9),_Pm1004AlmClient1InitFail_Type())
pm1004AlmClient1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClient1InitFail.setStatus(_A)
_Pm1004AlmClient2InitFail_Type=EkiOnOff
_Pm1004AlmClient2InitFail_Object=MibScalar
pm1004AlmClient2InitFail=_Pm1004AlmClient2InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,10),_Pm1004AlmClient2InitFail_Type())
pm1004AlmClient2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClient2InitFail.setStatus(_A)
_Pm1004AlmClient3InitFail_Type=EkiOnOff
_Pm1004AlmClient3InitFail_Object=MibScalar
pm1004AlmClient3InitFail=_Pm1004AlmClient3InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,11),_Pm1004AlmClient3InitFail_Type())
pm1004AlmClient3InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClient3InitFail.setStatus(_A)
_Pm1004AlmClient4InitFail_Type=EkiOnOff
_Pm1004AlmClient4InitFail_Object=MibScalar
pm1004AlmClient4InitFail=_Pm1004AlmClient4InitFail_Object((1,3,6,1,4,1,20044,18,2,1,2,195,12),_Pm1004AlmClient4InitFail_Type())
pm1004AlmClient4InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClient4InitFail.setStatus(_A)
_Pm1004AlmOtherCrit_ObjectIdentity=ObjectIdentity
pm1004AlmOtherCrit=_Pm1004AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,3))
_Pm1004AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm1004AlmsynthAlm0=_Pm1004AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,18,2,1,3,0))
_Pm1004AlmModGlobFail_Type=EkiOnOff
_Pm1004AlmModGlobFail_Object=MibScalar
pm1004AlmModGlobFail=_Pm1004AlmModGlobFail_Object((1,3,6,1,4,1,20044,18,2,1,3,0,9),_Pm1004AlmModGlobFail_Type())
pm1004AlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmModGlobFail.setStatus(_A)
_Pm1004AlmDefFuseA_Type=EkiOnOff
_Pm1004AlmDefFuseA_Object=MibScalar
pm1004AlmDefFuseA=_Pm1004AlmDefFuseA_Object((1,3,6,1,4,1,20044,18,2,1,3,0,15),_Pm1004AlmDefFuseA_Type())
pm1004AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDefFuseA.setStatus(_A)
_Pm1004AlmDefFuseB_Type=EkiOnOff
_Pm1004AlmDefFuseB_Object=MibScalar
pm1004AlmDefFuseB=_Pm1004AlmDefFuseB_Object((1,3,6,1,4,1,20044,18,2,1,3,0,16),_Pm1004AlmDefFuseB_Type())
pm1004AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDefFuseB.setStatus(_A)
_Pm1004AlmClient_ObjectIdentity=ObjectIdentity
pm1004AlmClient=_Pm1004AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,18,2,2))
_Pm1004AlmClientNurg_ObjectIdentity=ObjectIdentity
pm1004AlmClientNurg=_Pm1004AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,18,2,2,1))
_Pm1004AlmsfpWarnDdmTable_Object=MibTable
pm1004AlmsfpWarnDdmTable=_Pm1004AlmsfpWarnDdmTable_Object((1,3,6,1,4,1,20044,18,2,2,1,48))
if mibBuilder.loadTexts:pm1004AlmsfpWarnDdmTable.setStatus(_A)
_Pm1004AlmsfpWarnDdmEntry_Object=MibTableRow
pm1004AlmsfpWarnDdmEntry=_Pm1004AlmsfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1))
pm1004AlmsfpWarnDdmEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pm1004AlmsfpWarnDdmEntry.setStatus(_A)
class _Pm1004AlmsfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmsfpWarnDdmIndex_Type.__name__=_D
_Pm1004AlmsfpWarnDdmIndex_Object=MibTableColumn
pm1004AlmsfpWarnDdmIndex=_Pm1004AlmsfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,1),_Pm1004AlmsfpWarnDdmIndex_Type())
pm1004AlmsfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmsfpWarnDdmIndex.setStatus(_A)
_Pm1004AlmTxPwLowWngPortn_Type=EkiOnOff
_Pm1004AlmTxPwLowWngPortn_Object=MibTableColumn
pm1004AlmTxPwLowWngPortn=_Pm1004AlmTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,2),_Pm1004AlmTxPwLowWngPortn_Type())
pm1004AlmTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPwLowWngPortn.setStatus(_A)
_Pm1004AlmTxPwrHighWngPortn_Type=EkiOnOff
_Pm1004AlmTxPwrHighWngPortn_Object=MibTableColumn
pm1004AlmTxPwrHighWngPortn=_Pm1004AlmTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,3),_Pm1004AlmTxPwrHighWngPortn_Type())
pm1004AlmTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPwrHighWngPortn.setStatus(_A)
_Pm1004AlmTxBiasLowWngPortn_Type=EkiOnOff
_Pm1004AlmTxBiasLowWngPortn_Object=MibTableColumn
pm1004AlmTxBiasLowWngPortn=_Pm1004AlmTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,4),_Pm1004AlmTxBiasLowWngPortn_Type())
pm1004AlmTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasLowWngPortn.setStatus(_A)
_Pm1004AlmTxBiasHighWngPortn_Type=EkiOnOff
_Pm1004AlmTxBiasHighWngPortn_Object=MibTableColumn
pm1004AlmTxBiasHighWngPortn=_Pm1004AlmTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,5),_Pm1004AlmTxBiasHighWngPortn_Type())
pm1004AlmTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasHighWngPortn.setStatus(_A)
_Pm1004AlmVccLowWngPortn_Type=EkiOnOff
_Pm1004AlmVccLowWngPortn_Object=MibTableColumn
pm1004AlmVccLowWngPortn=_Pm1004AlmVccLowWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,6),_Pm1004AlmVccLowWngPortn_Type())
pm1004AlmVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVccLowWngPortn.setStatus(_A)
_Pm1004AlmVccHighWngPortn_Type=EkiOnOff
_Pm1004AlmVccHighWngPortn_Object=MibTableColumn
pm1004AlmVccHighWngPortn=_Pm1004AlmVccHighWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,7),_Pm1004AlmVccHighWngPortn_Type())
pm1004AlmVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVccHighWngPortn.setStatus(_A)
_Pm1004AlmTempLowWngPortn_Type=EkiOnOff
_Pm1004AlmTempLowWngPortn_Object=MibTableColumn
pm1004AlmTempLowWngPortn=_Pm1004AlmTempLowWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,8),_Pm1004AlmTempLowWngPortn_Type())
pm1004AlmTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempLowWngPortn.setStatus(_A)
_Pm1004AlmTempHighWngPortn_Type=EkiOnOff
_Pm1004AlmTempHighWngPortn_Object=MibTableColumn
pm1004AlmTempHighWngPortn=_Pm1004AlmTempHighWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,9),_Pm1004AlmTempHighWngPortn_Type())
pm1004AlmTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempHighWngPortn.setStatus(_A)
_Pm1004AlmRxPwrLowWngPortn_Type=EkiOnOff
_Pm1004AlmRxPwrLowWngPortn_Object=MibTableColumn
pm1004AlmRxPwrLowWngPortn=_Pm1004AlmRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,16),_Pm1004AlmRxPwrLowWngPortn_Type())
pm1004AlmRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPwrLowWngPortn.setStatus(_A)
_Pm1004AlmRxPwrHighWngPortn_Type=EkiOnOff
_Pm1004AlmRxPwrHighWngPortn_Object=MibTableColumn
pm1004AlmRxPwrHighWngPortn=_Pm1004AlmRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,48,1,17),_Pm1004AlmRxPwrHighWngPortn_Type())
pm1004AlmRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPwrHighWngPortn.setStatus(_A)
_Pm1004Almk1K2ClientTable_Object=MibTable
pm1004Almk1K2ClientTable=_Pm1004Almk1K2ClientTable_Object((1,3,6,1,4,1,20044,18,2,2,1,96))
if mibBuilder.loadTexts:pm1004Almk1K2ClientTable.setStatus(_A)
_Pm1004Almk1K2ClientEntry_Object=MibTableRow
pm1004Almk1K2ClientEntry=_Pm1004Almk1K2ClientEntry_Object((1,3,6,1,4,1,20044,18,2,2,1,96,1))
pm1004Almk1K2ClientEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm1004Almk1K2ClientEntry.setStatus(_A)
class _Pm1004Almk1K2ClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Almk1K2ClientIndex_Type.__name__=_D
_Pm1004Almk1K2ClientIndex_Object=MibTableColumn
pm1004Almk1K2ClientIndex=_Pm1004Almk1K2ClientIndex_Object((1,3,6,1,4,1,20044,18,2,2,1,96,1,1),_Pm1004Almk1K2ClientIndex_Type())
pm1004Almk1K2ClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Almk1K2ClientIndex.setStatus(_A)
class _Pm1004Almk1K2ClientPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Almk1K2ClientPortn_Type.__name__=_D
_Pm1004Almk1K2ClientPortn_Object=MibTableColumn
pm1004Almk1K2ClientPortn=_Pm1004Almk1K2ClientPortn_Object((1,3,6,1,4,1,20044,18,2,2,1,96,1,2),_Pm1004Almk1K2ClientPortn_Type())
pm1004Almk1K2ClientPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Almk1K2ClientPortn.setStatus(_A)
_Pm1004AlmClientUrg_ObjectIdentity=ObjectIdentity
pm1004AlmClientUrg=_Pm1004AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,18,2,2,2))
_Pm1004AlmsfpAlmDdmTable_Object=MibTable
pm1004AlmsfpAlmDdmTable=_Pm1004AlmsfpAlmDdmTable_Object((1,3,6,1,4,1,20044,18,2,2,2,32))
if mibBuilder.loadTexts:pm1004AlmsfpAlmDdmTable.setStatus(_A)
_Pm1004AlmsfpAlmDdmEntry_Object=MibTableRow
pm1004AlmsfpAlmDdmEntry=_Pm1004AlmsfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1))
pm1004AlmsfpAlmDdmEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm1004AlmsfpAlmDdmEntry.setStatus(_A)
class _Pm1004AlmsfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmsfpAlmDdmIndex_Type.__name__=_D
_Pm1004AlmsfpAlmDdmIndex_Object=MibTableColumn
pm1004AlmsfpAlmDdmIndex=_Pm1004AlmsfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,1),_Pm1004AlmsfpAlmDdmIndex_Type())
pm1004AlmsfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmsfpAlmDdmIndex.setStatus(_A)
_Pm1004AlmTxPwrLowAlaPortn_Type=EkiOnOff
_Pm1004AlmTxPwrLowAlaPortn_Object=MibTableColumn
pm1004AlmTxPwrLowAlaPortn=_Pm1004AlmTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,2),_Pm1004AlmTxPwrLowAlaPortn_Type())
pm1004AlmTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPwrLowAlaPortn.setStatus(_A)
_Pm1004AlmTxPwrHighAlaPortn_Type=EkiOnOff
_Pm1004AlmTxPwrHighAlaPortn_Object=MibTableColumn
pm1004AlmTxPwrHighAlaPortn=_Pm1004AlmTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,3),_Pm1004AlmTxPwrHighAlaPortn_Type())
pm1004AlmTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPwrHighAlaPortn.setStatus(_A)
_Pm1004AlmTxBiasLowAlaPortn_Type=EkiOnOff
_Pm1004AlmTxBiasLowAlaPortn_Object=MibTableColumn
pm1004AlmTxBiasLowAlaPortn=_Pm1004AlmTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,4),_Pm1004AlmTxBiasLowAlaPortn_Type())
pm1004AlmTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasLowAlaPortn.setStatus(_A)
_Pm1004AlmTxBiasHighAlaPortn_Type=EkiOnOff
_Pm1004AlmTxBiasHighAlaPortn_Object=MibTableColumn
pm1004AlmTxBiasHighAlaPortn=_Pm1004AlmTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,5),_Pm1004AlmTxBiasHighAlaPortn_Type())
pm1004AlmTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasHighAlaPortn.setStatus(_A)
_Pm1004AlmVccLowAlaPortn_Type=EkiOnOff
_Pm1004AlmVccLowAlaPortn_Object=MibTableColumn
pm1004AlmVccLowAlaPortn=_Pm1004AlmVccLowAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,6),_Pm1004AlmVccLowAlaPortn_Type())
pm1004AlmVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVccLowAlaPortn.setStatus(_A)
_Pm1004AlmVccHighAlaPortn_Type=EkiOnOff
_Pm1004AlmVccHighAlaPortn_Object=MibTableColumn
pm1004AlmVccHighAlaPortn=_Pm1004AlmVccHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,7),_Pm1004AlmVccHighAlaPortn_Type())
pm1004AlmVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVccHighAlaPortn.setStatus(_A)
_Pm1004AlmTempLowAlaPortn_Type=EkiOnOff
_Pm1004AlmTempLowAlaPortn_Object=MibTableColumn
pm1004AlmTempLowAlaPortn=_Pm1004AlmTempLowAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,8),_Pm1004AlmTempLowAlaPortn_Type())
pm1004AlmTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempLowAlaPortn.setStatus(_A)
_Pm1004AlmTempHighAlaPortn_Type=EkiOnOff
_Pm1004AlmTempHighAlaPortn_Object=MibTableColumn
pm1004AlmTempHighAlaPortn=_Pm1004AlmTempHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,9),_Pm1004AlmTempHighAlaPortn_Type())
pm1004AlmTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempHighAlaPortn.setStatus(_A)
_Pm1004AlmRxPwrLowAlaPortn_Type=EkiOnOff
_Pm1004AlmRxPwrLowAlaPortn_Object=MibTableColumn
pm1004AlmRxPwrLowAlaPortn=_Pm1004AlmRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,16),_Pm1004AlmRxPwrLowAlaPortn_Type())
pm1004AlmRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPwrLowAlaPortn.setStatus(_A)
_Pm1004AlmRxPwrHighAlaPortn_Type=EkiOnOff
_Pm1004AlmRxPwrHighAlaPortn_Object=MibTableColumn
pm1004AlmRxPwrHighAlaPortn=_Pm1004AlmRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,2,2,32,1,17),_Pm1004AlmRxPwrHighAlaPortn_Type())
pm1004AlmRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPwrHighAlaPortn.setStatus(_A)
_Pm1004AlmClientCrit_ObjectIdentity=ObjectIdentity
pm1004AlmClientCrit=_Pm1004AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,18,2,2,3))
_Pm1004AlmsynthAlmPortTable_Object=MibTable
pm1004AlmsynthAlmPortTable=_Pm1004AlmsynthAlmPortTable_Object((1,3,6,1,4,1,20044,18,2,2,3,8))
if mibBuilder.loadTexts:pm1004AlmsynthAlmPortTable.setStatus(_A)
_Pm1004AlmsynthAlmPortEntry_Object=MibTableRow
pm1004AlmsynthAlmPortEntry=_Pm1004AlmsynthAlmPortEntry_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1))
pm1004AlmsynthAlmPortEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm1004AlmsynthAlmPortEntry.setStatus(_A)
class _Pm1004AlmsynthAlmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmsynthAlmPortIndex_Type.__name__=_D
_Pm1004AlmsynthAlmPortIndex_Object=MibTableColumn
pm1004AlmsynthAlmPortIndex=_Pm1004AlmsynthAlmPortIndex_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,1),_Pm1004AlmsynthAlmPortIndex_Type())
pm1004AlmsynthAlmPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmsynthAlmPortIndex.setStatus(_A)
_Pm1004AlmSfpAbsentPortn_Type=EkiOnOff
_Pm1004AlmSfpAbsentPortn_Object=MibTableColumn
pm1004AlmSfpAbsentPortn=_Pm1004AlmSfpAbsentPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,2),_Pm1004AlmSfpAbsentPortn_Type())
pm1004AlmSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmSfpAbsentPortn.setStatus(_A)
_Pm1004AlmDdmAbsentPortn_Type=EkiOnOff
_Pm1004AlmDdmAbsentPortn_Object=MibTableColumn
pm1004AlmDdmAbsentPortn=_Pm1004AlmDdmAbsentPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,3),_Pm1004AlmDdmAbsentPortn_Type())
pm1004AlmDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDdmAbsentPortn.setStatus(_A)
_Pm1004AlmHwFailAccPortn_Type=EkiOnOff
_Pm1004AlmHwFailAccPortn_Object=MibTableColumn
pm1004AlmHwFailAccPortn=_Pm1004AlmHwFailAccPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,5),_Pm1004AlmHwFailAccPortn_Type())
pm1004AlmHwFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmHwFailAccPortn.setStatus(_A)
_Pm1004AlmDwLsdPortn_Type=EkiOnOff
_Pm1004AlmDwLsdPortn_Object=MibTableColumn
pm1004AlmDwLsdPortn=_Pm1004AlmDwLsdPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,6),_Pm1004AlmDwLsdPortn_Type())
pm1004AlmDwLsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwLsdPortn.setStatus(_A)
_Pm1004AlmClientLocalOosPortn_Type=EkiOnOff
_Pm1004AlmClientLocalOosPortn_Object=MibTableColumn
pm1004AlmClientLocalOosPortn=_Pm1004AlmClientLocalOosPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,7),_Pm1004AlmClientLocalOosPortn_Type())
pm1004AlmClientLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClientLocalOosPortn.setStatus(_A)
_Pm1004AlmClientRemoteOosPortn_Type=EkiOnOff
_Pm1004AlmClientRemoteOosPortn_Object=MibTableColumn
pm1004AlmClientRemoteOosPortn=_Pm1004AlmClientRemoteOosPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,8),_Pm1004AlmClientRemoteOosPortn_Type())
pm1004AlmClientRemoteOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClientRemoteOosPortn.setStatus(_A)
_Pm1004AlmDwCaisPortn_Type=EkiOnOff
_Pm1004AlmDwCaisPortn_Object=MibTableColumn
pm1004AlmDwCaisPortn=_Pm1004AlmDwCaisPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,9),_Pm1004AlmDwCaisPortn_Type())
pm1004AlmDwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwCaisPortn.setStatus(_A)
_Pm1004AlmSfpDdmWarningPortn_Type=EkiOnOff
_Pm1004AlmSfpDdmWarningPortn_Object=MibTableColumn
pm1004AlmSfpDdmWarningPortn=_Pm1004AlmSfpDdmWarningPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,10),_Pm1004AlmSfpDdmWarningPortn_Type())
pm1004AlmSfpDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmSfpDdmWarningPortn.setStatus(_A)
_Pm1004AlmSfpDdmAlmPortn_Type=EkiOnOff
_Pm1004AlmSfpDdmAlmPortn_Object=MibTableColumn
pm1004AlmSfpDdmAlmPortn=_Pm1004AlmSfpDdmAlmPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,11),_Pm1004AlmSfpDdmAlmPortn_Type())
pm1004AlmSfpDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmSfpDdmAlmPortn.setStatus(_A)
_Pm1004AlmFailAccPortn_Type=EkiOnOff
_Pm1004AlmFailAccPortn_Object=MibTableColumn
pm1004AlmFailAccPortn=_Pm1004AlmFailAccPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,13),_Pm1004AlmFailAccPortn_Type())
pm1004AlmFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmFailAccPortn.setStatus(_A)
_Pm1004AlmUpCsfPortn_Type=EkiOnOff
_Pm1004AlmUpCsfPortn_Object=MibTableColumn
pm1004AlmUpCsfPortn=_Pm1004AlmUpCsfPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,8,1,17),_Pm1004AlmUpCsfPortn_Type())
pm1004AlmUpCsfPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmUpCsfPortn.setStatus(_A)
_Pm1004AlmaccessioAlmTable_Object=MibTable
pm1004AlmaccessioAlmTable=_Pm1004AlmaccessioAlmTable_Object((1,3,6,1,4,1,20044,18,2,2,3,16))
if mibBuilder.loadTexts:pm1004AlmaccessioAlmTable.setStatus(_A)
_Pm1004AlmaccessioAlmEntry_Object=MibTableRow
pm1004AlmaccessioAlmEntry=_Pm1004AlmaccessioAlmEntry_Object((1,3,6,1,4,1,20044,18,2,2,3,16,1))
pm1004AlmaccessioAlmEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm1004AlmaccessioAlmEntry.setStatus(_A)
class _Pm1004AlmaccessioAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmaccessioAlmIndex_Type.__name__=_D
_Pm1004AlmaccessioAlmIndex_Object=MibTableColumn
pm1004AlmaccessioAlmIndex=_Pm1004AlmaccessioAlmIndex_Object((1,3,6,1,4,1,20044,18,2,2,3,16,1,1),_Pm1004AlmaccessioAlmIndex_Type())
pm1004AlmaccessioAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmaccessioAlmIndex.setStatus(_A)
_Pm1004AlmDwLasFailPortn_Type=EkiOnOff
_Pm1004AlmDwLasFailPortn_Object=MibTableColumn
pm1004AlmDwLasFailPortn=_Pm1004AlmDwLasFailPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,16,1,2),_Pm1004AlmDwLasFailPortn_Type())
pm1004AlmDwLasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwLasFailPortn.setStatus(_A)
_Pm1004AlmUpLosPortn_Type=EkiOnOff
_Pm1004AlmUpLosPortn_Object=MibTableColumn
pm1004AlmUpLosPortn=_Pm1004AlmUpLosPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,16,1,5),_Pm1004AlmUpLosPortn_Type())
pm1004AlmUpLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmUpLosPortn.setStatus(_A)
_Pm1004AlmmapperDeAlmTable_Object=MibTable
pm1004AlmmapperDeAlmTable=_Pm1004AlmmapperDeAlmTable_Object((1,3,6,1,4,1,20044,18,2,2,3,72))
if mibBuilder.loadTexts:pm1004AlmmapperDeAlmTable.setStatus(_A)
_Pm1004AlmmapperDeAlmEntry_Object=MibTableRow
pm1004AlmmapperDeAlmEntry=_Pm1004AlmmapperDeAlmEntry_Object((1,3,6,1,4,1,20044,18,2,2,3,72,1))
pm1004AlmmapperDeAlmEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm1004AlmmapperDeAlmEntry.setStatus(_A)
class _Pm1004AlmmapperDeAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmmapperDeAlmIndex_Type.__name__=_D
_Pm1004AlmmapperDeAlmIndex_Object=MibTableColumn
pm1004AlmmapperDeAlmIndex=_Pm1004AlmmapperDeAlmIndex_Object((1,3,6,1,4,1,20044,18,2,2,3,72,1,1),_Pm1004AlmmapperDeAlmIndex_Type())
pm1004AlmmapperDeAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmmapperDeAlmIndex.setStatus(_A)
_Pm1004AlmUpAccOosPortn_Type=EkiOnOff
_Pm1004AlmUpAccOosPortn_Object=MibTableColumn
pm1004AlmUpAccOosPortn=_Pm1004AlmUpAccOosPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,72,1,2),_Pm1004AlmUpAccOosPortn_Type())
pm1004AlmUpAccOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmUpAccOosPortn.setStatus(_A)
_Pm1004AlmUpBufferOvlPortn_Type=EkiOnOff
_Pm1004AlmUpBufferOvlPortn_Object=MibTableColumn
pm1004AlmUpBufferOvlPortn=_Pm1004AlmUpBufferOvlPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,72,1,11),_Pm1004AlmUpBufferOvlPortn_Type())
pm1004AlmUpBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmUpBufferOvlPortn.setStatus(_A)
_Pm1004AlmDwCsfDetPortn_Type=EkiOnOff
_Pm1004AlmDwCsfDetPortn_Object=MibTableColumn
pm1004AlmDwCsfDetPortn=_Pm1004AlmDwCsfDetPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,72,1,12),_Pm1004AlmDwCsfDetPortn_Type())
pm1004AlmDwCsfDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwCsfDetPortn.setStatus(_A)
_Pm1004AlmDwBufferOvlPortn_Type=EkiOnOff
_Pm1004AlmDwBufferOvlPortn_Object=MibTableColumn
pm1004AlmDwBufferOvlPortn=_Pm1004AlmDwBufferOvlPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,72,1,15),_Pm1004AlmDwBufferOvlPortn_Type())
pm1004AlmDwBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwBufferOvlPortn.setStatus(_A)
_Pm1004AlmaccessioSdhAlarmTable_Object=MibTable
pm1004AlmaccessioSdhAlarmTable=_Pm1004AlmaccessioSdhAlarmTable_Object((1,3,6,1,4,1,20044,18,2,2,3,104))
if mibBuilder.loadTexts:pm1004AlmaccessioSdhAlarmTable.setStatus(_A)
_Pm1004AlmaccessioSdhAlarmEntry_Object=MibTableRow
pm1004AlmaccessioSdhAlarmEntry=_Pm1004AlmaccessioSdhAlarmEntry_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1))
pm1004AlmaccessioSdhAlarmEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm1004AlmaccessioSdhAlarmEntry.setStatus(_A)
class _Pm1004AlmaccessioSdhAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmaccessioSdhAlarmIndex_Type.__name__=_D
_Pm1004AlmaccessioSdhAlarmIndex_Object=MibTableColumn
pm1004AlmaccessioSdhAlarmIndex=_Pm1004AlmaccessioSdhAlarmIndex_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,1),_Pm1004AlmaccessioSdhAlarmIndex_Type())
pm1004AlmaccessioSdhAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmaccessioSdhAlarmIndex.setStatus(_A)
_Pm1004AlmFifoErrPortn_Type=EkiOnOff
_Pm1004AlmFifoErrPortn_Object=MibTableColumn
pm1004AlmFifoErrPortn=_Pm1004AlmFifoErrPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,3),_Pm1004AlmFifoErrPortn_Type())
pm1004AlmFifoErrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmFifoErrPortn.setStatus(_A)
_Pm1004AlmRxLossOfLockPortn_Type=EkiOnOff
_Pm1004AlmRxLossOfLockPortn_Object=MibTableColumn
pm1004AlmRxLossOfLockPortn=_Pm1004AlmRxLossOfLockPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,4),_Pm1004AlmRxLossOfLockPortn_Type())
pm1004AlmRxLossOfLockPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxLossOfLockPortn.setStatus(_A)
_Pm1004AlmTxLossOfLockPortn_Type=EkiOnOff
_Pm1004AlmTxLossOfLockPortn_Object=MibTableColumn
pm1004AlmTxLossOfLockPortn=_Pm1004AlmTxLossOfLockPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,5),_Pm1004AlmTxLossOfLockPortn_Type())
pm1004AlmTxLossOfLockPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxLossOfLockPortn.setStatus(_A)
_Pm1004AlmClientAisDetPortn_Type=EkiOnOff
_Pm1004AlmClientAisDetPortn_Object=MibTableColumn
pm1004AlmClientAisDetPortn=_Pm1004AlmClientAisDetPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,6),_Pm1004AlmClientAisDetPortn_Type())
pm1004AlmClientAisDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClientAisDetPortn.setStatus(_A)
_Pm1004AlmClientRdiDetPortn_Type=EkiOnOff
_Pm1004AlmClientRdiDetPortn_Object=MibTableColumn
pm1004AlmClientRdiDetPortn=_Pm1004AlmClientRdiDetPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,7),_Pm1004AlmClientRdiDetPortn_Type())
pm1004AlmClientRdiDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClientRdiDetPortn.setStatus(_A)
_Pm1004AlmClientOofPortn_Type=EkiOnOff
_Pm1004AlmClientOofPortn_Object=MibTableColumn
pm1004AlmClientOofPortn=_Pm1004AlmClientOofPortn_Object((1,3,6,1,4,1,20044,18,2,2,3,104,1,8),_Pm1004AlmClientOofPortn_Type())
pm1004AlmClientOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmClientOofPortn.setStatus(_A)
_Pm1004AlmLine_ObjectIdentity=ObjectIdentity
pm1004AlmLine=_Pm1004AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,18,2,3))
_Pm1004AlmLineNurg_ObjectIdentity=ObjectIdentity
pm1004AlmLineNurg=_Pm1004AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,18,2,3,1))
_Pm1004AlmlineXfp1WarningsTable_Object=MibTable
pm1004AlmlineXfp1WarningsTable=_Pm1004AlmlineXfp1WarningsTable_Object((1,3,6,1,4,1,20044,18,2,3,1,209))
if mibBuilder.loadTexts:pm1004AlmlineXfp1WarningsTable.setStatus(_A)
_Pm1004AlmlineXfp1WarningsEntry_Object=MibTableRow
pm1004AlmlineXfp1WarningsEntry=_Pm1004AlmlineXfp1WarningsEntry_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1))
pm1004AlmlineXfp1WarningsEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm1004AlmlineXfp1WarningsEntry.setStatus(_A)
class _Pm1004AlmlineXfp1WarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineXfp1WarningsIndex_Type.__name__=_D
_Pm1004AlmlineXfp1WarningsIndex_Object=MibTableColumn
pm1004AlmlineXfp1WarningsIndex=_Pm1004AlmlineXfp1WarningsIndex_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,1),_Pm1004AlmlineXfp1WarningsIndex_Type())
pm1004AlmlineXfp1WarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineXfp1WarningsIndex.setStatus(_A)
_Pm1004AlmTxPowerLowWarningPortn_Type=EkiOnOff
_Pm1004AlmTxPowerLowWarningPortn_Object=MibTableColumn
pm1004AlmTxPowerLowWarningPortn=_Pm1004AlmTxPowerLowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,2),_Pm1004AlmTxPowerLowWarningPortn_Type())
pm1004AlmTxPowerLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPowerLowWarningPortn.setStatus(_A)
_Pm1004AlmTxPowerHighWarningPortn_Type=EkiOnOff
_Pm1004AlmTxPowerHighWarningPortn_Object=MibTableColumn
pm1004AlmTxPowerHighWarningPortn=_Pm1004AlmTxPowerHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,3),_Pm1004AlmTxPowerHighWarningPortn_Type())
pm1004AlmTxPowerHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPowerHighWarningPortn.setStatus(_A)
_Pm1004AlmTxBiasLowWarningPortn_Type=EkiOnOff
_Pm1004AlmTxBiasLowWarningPortn_Object=MibTableColumn
pm1004AlmTxBiasLowWarningPortn=_Pm1004AlmTxBiasLowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,4),_Pm1004AlmTxBiasLowWarningPortn_Type())
pm1004AlmTxBiasLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasLowWarningPortn.setStatus(_A)
_Pm1004AlmTxBiasHighWarningPortn_Type=EkiOnOff
_Pm1004AlmTxBiasHighWarningPortn_Object=MibTableColumn
pm1004AlmTxBiasHighWarningPortn=_Pm1004AlmTxBiasHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,5),_Pm1004AlmTxBiasHighWarningPortn_Type())
pm1004AlmTxBiasHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasHighWarningPortn.setStatus(_A)
_Pm1004AlmTempLowWarningPortn_Type=EkiOnOff
_Pm1004AlmTempLowWarningPortn_Object=MibTableColumn
pm1004AlmTempLowWarningPortn=_Pm1004AlmTempLowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,8),_Pm1004AlmTempLowWarningPortn_Type())
pm1004AlmTempLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempLowWarningPortn.setStatus(_A)
_Pm1004AlmTempHighWarningPortn_Type=EkiOnOff
_Pm1004AlmTempHighWarningPortn_Object=MibTableColumn
pm1004AlmTempHighWarningPortn=_Pm1004AlmTempHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,9),_Pm1004AlmTempHighWarningPortn_Type())
pm1004AlmTempHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempHighWarningPortn.setStatus(_A)
_Pm1004AlmRxPowerLowWarningPortn_Type=EkiOnOff
_Pm1004AlmRxPowerLowWarningPortn_Object=MibTableColumn
pm1004AlmRxPowerLowWarningPortn=_Pm1004AlmRxPowerLowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,16),_Pm1004AlmRxPowerLowWarningPortn_Type())
pm1004AlmRxPowerLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPowerLowWarningPortn.setStatus(_A)
_Pm1004AlmRxPowerHighWarningPortn_Type=EkiOnOff
_Pm1004AlmRxPowerHighWarningPortn_Object=MibTableColumn
pm1004AlmRxPowerHighWarningPortn=_Pm1004AlmRxPowerHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,209,1,17),_Pm1004AlmRxPowerHighWarningPortn_Type())
pm1004AlmRxPowerHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPowerHighWarningPortn.setStatus(_A)
_Pm1004AlmlineOtx1TlhWarningsTable_Object=MibTable
pm1004AlmlineOtx1TlhWarningsTable=_Pm1004AlmlineOtx1TlhWarningsTable_Object((1,3,6,1,4,1,20044,18,2,3,1,225))
if mibBuilder.loadTexts:pm1004AlmlineOtx1TlhWarningsTable.setStatus(_A)
_Pm1004AlmlineOtx1TlhWarningsEntry_Object=MibTableRow
pm1004AlmlineOtx1TlhWarningsEntry=_Pm1004AlmlineOtx1TlhWarningsEntry_Object((1,3,6,1,4,1,20044,18,2,3,1,225,1))
pm1004AlmlineOtx1TlhWarningsEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm1004AlmlineOtx1TlhWarningsEntry.setStatus(_A)
class _Pm1004AlmlineOtx1TlhWarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineOtx1TlhWarningsIndex_Type.__name__=_D
_Pm1004AlmlineOtx1TlhWarningsIndex_Object=MibTableColumn
pm1004AlmlineOtx1TlhWarningsIndex=_Pm1004AlmlineOtx1TlhWarningsIndex_Object((1,3,6,1,4,1,20044,18,2,3,1,225,1,1),_Pm1004AlmlineOtx1TlhWarningsIndex_Type())
pm1004AlmlineOtx1TlhWarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineOtx1TlhWarningsIndex.setStatus(_A)
_Pm1004AlmLineModulatorAgingHighWarningPortn_Type=EkiOnOff
_Pm1004AlmLineModulatorAgingHighWarningPortn_Object=MibTableColumn
pm1004AlmLineModulatorAgingHighWarningPortn=_Pm1004AlmLineModulatorAgingHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,225,1,6),_Pm1004AlmLineModulatorAgingHighWarningPortn_Type())
pm1004AlmLineModulatorAgingHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineModulatorAgingHighWarningPortn.setStatus(_A)
_Pm1004AlmLineAgingHighWarningPortn_Type=EkiOnOff
_Pm1004AlmLineAgingHighWarningPortn_Object=MibTableColumn
pm1004AlmLineAgingHighWarningPortn=_Pm1004AlmLineAgingHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,225,1,7),_Pm1004AlmLineAgingHighWarningPortn_Type())
pm1004AlmLineAgingHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineAgingHighWarningPortn.setStatus(_A)
_Pm1004AlmLineFreqDevHighWarningPortn_Type=EkiOnOff
_Pm1004AlmLineFreqDevHighWarningPortn_Object=MibTableColumn
pm1004AlmLineFreqDevHighWarningPortn=_Pm1004AlmLineFreqDevHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,225,1,13),_Pm1004AlmLineFreqDevHighWarningPortn_Type())
pm1004AlmLineFreqDevHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineFreqDevHighWarningPortn.setStatus(_A)
_Pm1004AlmLineLaserTempHighWarningPortn_Type=EkiOnOff
_Pm1004AlmLineLaserTempHighWarningPortn_Object=MibTableColumn
pm1004AlmLineLaserTempHighWarningPortn=_Pm1004AlmLineLaserTempHighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,1,225,1,15),_Pm1004AlmLineLaserTempHighWarningPortn_Type())
pm1004AlmLineLaserTempHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineLaserTempHighWarningPortn.setStatus(_A)
_Pm1004AlmLineUrg_ObjectIdentity=ObjectIdentity
pm1004AlmLineUrg=_Pm1004AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,18,2,3,2))
_Pm1004AlmdfrmBerTable_Object=MibTable
pm1004AlmdfrmBerTable=_Pm1004AlmdfrmBerTable_Object((1,3,6,1,4,1,20044,18,2,3,2,129))
if mibBuilder.loadTexts:pm1004AlmdfrmBerTable.setStatus(_A)
_Pm1004AlmdfrmBerEntry_Object=MibTableRow
pm1004AlmdfrmBerEntry=_Pm1004AlmdfrmBerEntry_Object((1,3,6,1,4,1,20044,18,2,3,2,129,1))
pm1004AlmdfrmBerEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm1004AlmdfrmBerEntry.setStatus(_A)
class _Pm1004AlmdfrmBerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmdfrmBerIndex_Type.__name__=_D
_Pm1004AlmdfrmBerIndex_Object=MibTableColumn
pm1004AlmdfrmBerIndex=_Pm1004AlmdfrmBerIndex_Object((1,3,6,1,4,1,20044,18,2,3,2,129,1,1),_Pm1004AlmdfrmBerIndex_Type())
pm1004AlmdfrmBerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmdfrmBerIndex.setStatus(_A)
_Pm1004AlmLineSignalDegradePortn_Type=EkiOnOff
_Pm1004AlmLineSignalDegradePortn_Object=MibTableColumn
pm1004AlmLineSignalDegradePortn=_Pm1004AlmLineSignalDegradePortn_Object((1,3,6,1,4,1,20044,18,2,3,2,129,1,2),_Pm1004AlmLineSignalDegradePortn_Type())
pm1004AlmLineSignalDegradePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineSignalDegradePortn.setStatus(_A)
_Pm1004AlmLineSignalFailPortn_Type=EkiOnOff
_Pm1004AlmLineSignalFailPortn_Object=MibTableColumn
pm1004AlmLineSignalFailPortn=_Pm1004AlmLineSignalFailPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,129,1,3),_Pm1004AlmLineSignalFailPortn_Type())
pm1004AlmLineSignalFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineSignalFailPortn.setStatus(_A)
_Pm1004AlmLineDegradePortn_Type=EkiOnOff
_Pm1004AlmLineDegradePortn_Object=MibTableColumn
pm1004AlmLineDegradePortn=_Pm1004AlmLineDegradePortn_Object((1,3,6,1,4,1,20044,18,2,3,2,129,1,6),_Pm1004AlmLineDegradePortn_Type())
pm1004AlmLineDegradePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineDegradePortn.setStatus(_A)
_Pm1004AlmlineXfp1AlarmTable_Object=MibTable
pm1004AlmlineXfp1AlarmTable=_Pm1004AlmlineXfp1AlarmTable_Object((1,3,6,1,4,1,20044,18,2,3,2,208))
if mibBuilder.loadTexts:pm1004AlmlineXfp1AlarmTable.setStatus(_A)
_Pm1004AlmlineXfp1AlarmEntry_Object=MibTableRow
pm1004AlmlineXfp1AlarmEntry=_Pm1004AlmlineXfp1AlarmEntry_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1))
pm1004AlmlineXfp1AlarmEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm1004AlmlineXfp1AlarmEntry.setStatus(_A)
class _Pm1004AlmlineXfp1AlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineXfp1AlarmIndex_Type.__name__=_D
_Pm1004AlmlineXfp1AlarmIndex_Object=MibTableColumn
pm1004AlmlineXfp1AlarmIndex=_Pm1004AlmlineXfp1AlarmIndex_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,1),_Pm1004AlmlineXfp1AlarmIndex_Type())
pm1004AlmlineXfp1AlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineXfp1AlarmIndex.setStatus(_A)
_Pm1004AlmTxPowerLowAlarmPortn_Type=EkiOnOff
_Pm1004AlmTxPowerLowAlarmPortn_Object=MibTableColumn
pm1004AlmTxPowerLowAlarmPortn=_Pm1004AlmTxPowerLowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,2),_Pm1004AlmTxPowerLowAlarmPortn_Type())
pm1004AlmTxPowerLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPowerLowAlarmPortn.setStatus(_A)
_Pm1004AlmTxPowerHighAlarmPortn_Type=EkiOnOff
_Pm1004AlmTxPowerHighAlarmPortn_Object=MibTableColumn
pm1004AlmTxPowerHighAlarmPortn=_Pm1004AlmTxPowerHighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,3),_Pm1004AlmTxPowerHighAlarmPortn_Type())
pm1004AlmTxPowerHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxPowerHighAlarmPortn.setStatus(_A)
_Pm1004AlmTxBiasLowAlarmPortn_Type=EkiOnOff
_Pm1004AlmTxBiasLowAlarmPortn_Object=MibTableColumn
pm1004AlmTxBiasLowAlarmPortn=_Pm1004AlmTxBiasLowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,4),_Pm1004AlmTxBiasLowAlarmPortn_Type())
pm1004AlmTxBiasLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasLowAlarmPortn.setStatus(_A)
_Pm1004AlmTxBiasHighAlarmPortn_Type=EkiOnOff
_Pm1004AlmTxBiasHighAlarmPortn_Object=MibTableColumn
pm1004AlmTxBiasHighAlarmPortn=_Pm1004AlmTxBiasHighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,5),_Pm1004AlmTxBiasHighAlarmPortn_Type())
pm1004AlmTxBiasHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxBiasHighAlarmPortn.setStatus(_A)
_Pm1004AlmTempLowAlarmPortn_Type=EkiOnOff
_Pm1004AlmTempLowAlarmPortn_Object=MibTableColumn
pm1004AlmTempLowAlarmPortn=_Pm1004AlmTempLowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,8),_Pm1004AlmTempLowAlarmPortn_Type())
pm1004AlmTempLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempLowAlarmPortn.setStatus(_A)
_Pm1004AlmTempHighAlarmPortn_Type=EkiOnOff
_Pm1004AlmTempHighAlarmPortn_Object=MibTableColumn
pm1004AlmTempHighAlarmPortn=_Pm1004AlmTempHighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,9),_Pm1004AlmTempHighAlarmPortn_Type())
pm1004AlmTempHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTempHighAlarmPortn.setStatus(_A)
_Pm1004AlmRxPowerLowAlarmPortn_Type=EkiOnOff
_Pm1004AlmRxPowerLowAlarmPortn_Object=MibTableColumn
pm1004AlmRxPowerLowAlarmPortn=_Pm1004AlmRxPowerLowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,16),_Pm1004AlmRxPowerLowAlarmPortn_Type())
pm1004AlmRxPowerLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPowerLowAlarmPortn.setStatus(_A)
_Pm1004AlmRxPowerHighAlarmPortn_Type=EkiOnOff
_Pm1004AlmRxPowerHighAlarmPortn_Object=MibTableColumn
pm1004AlmRxPowerHighAlarmPortn=_Pm1004AlmRxPowerHighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,208,1,17),_Pm1004AlmRxPowerHighAlarmPortn_Type())
pm1004AlmRxPowerHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxPowerHighAlarmPortn.setStatus(_A)
_Pm1004AlmlineXfp1SupplyAlarmTable_Object=MibTable
pm1004AlmlineXfp1SupplyAlarmTable=_Pm1004AlmlineXfp1SupplyAlarmTable_Object((1,3,6,1,4,1,20044,18,2,3,2,212))
if mibBuilder.loadTexts:pm1004AlmlineXfp1SupplyAlarmTable.setStatus(_A)
_Pm1004AlmlineXfp1SupplyAlarmEntry_Object=MibTableRow
pm1004AlmlineXfp1SupplyAlarmEntry=_Pm1004AlmlineXfp1SupplyAlarmEntry_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1))
pm1004AlmlineXfp1SupplyAlarmEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm1004AlmlineXfp1SupplyAlarmEntry.setStatus(_A)
class _Pm1004AlmlineXfp1SupplyAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineXfp1SupplyAlarmIndex_Type.__name__=_D
_Pm1004AlmlineXfp1SupplyAlarmIndex_Object=MibTableColumn
pm1004AlmlineXfp1SupplyAlarmIndex=_Pm1004AlmlineXfp1SupplyAlarmIndex_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,1),_Pm1004AlmlineXfp1SupplyAlarmIndex_Type())
pm1004AlmlineXfp1SupplyAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineXfp1SupplyAlarmIndex.setStatus(_A)
_Pm1004AlmVee5LowAlarmPortn_Type=EkiOnOff
_Pm1004AlmVee5LowAlarmPortn_Object=MibTableColumn
pm1004AlmVee5LowAlarmPortn=_Pm1004AlmVee5LowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,2),_Pm1004AlmVee5LowAlarmPortn_Type())
pm1004AlmVee5LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVee5LowAlarmPortn.setStatus(_A)
_Pm1004AlmVee5HighAlarmPortn_Type=EkiOnOff
_Pm1004AlmVee5HighAlarmPortn_Object=MibTableColumn
pm1004AlmVee5HighAlarmPortn=_Pm1004AlmVee5HighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,3),_Pm1004AlmVee5HighAlarmPortn_Type())
pm1004AlmVee5HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVee5HighAlarmPortn.setStatus(_A)
_Pm1004AlmVcc2LowAlarmPortn_Type=EkiOnOff
_Pm1004AlmVcc2LowAlarmPortn_Object=MibTableColumn
pm1004AlmVcc2LowAlarmPortn=_Pm1004AlmVcc2LowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,4),_Pm1004AlmVcc2LowAlarmPortn_Type())
pm1004AlmVcc2LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc2LowAlarmPortn.setStatus(_A)
_Pm1004AlmVcc2HighAlarmPortn_Type=EkiOnOff
_Pm1004AlmVcc2HighAlarmPortn_Object=MibTableColumn
pm1004AlmVcc2HighAlarmPortn=_Pm1004AlmVcc2HighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,5),_Pm1004AlmVcc2HighAlarmPortn_Type())
pm1004AlmVcc2HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc2HighAlarmPortn.setStatus(_A)
_Pm1004AlmVcc3LowAlarmPortn_Type=EkiOnOff
_Pm1004AlmVcc3LowAlarmPortn_Object=MibTableColumn
pm1004AlmVcc3LowAlarmPortn=_Pm1004AlmVcc3LowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,6),_Pm1004AlmVcc3LowAlarmPortn_Type())
pm1004AlmVcc3LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc3LowAlarmPortn.setStatus(_A)
_Pm1004AlmVcc3HighAlarmPortn_Type=EkiOnOff
_Pm1004AlmVcc3HighAlarmPortn_Object=MibTableColumn
pm1004AlmVcc3HighAlarmPortn=_Pm1004AlmVcc3HighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,7),_Pm1004AlmVcc3HighAlarmPortn_Type())
pm1004AlmVcc3HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc3HighAlarmPortn.setStatus(_A)
_Pm1004AlmVcc5LowAlarmPortn_Type=EkiOnOff
_Pm1004AlmVcc5LowAlarmPortn_Object=MibTableColumn
pm1004AlmVcc5LowAlarmPortn=_Pm1004AlmVcc5LowAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,8),_Pm1004AlmVcc5LowAlarmPortn_Type())
pm1004AlmVcc5LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc5LowAlarmPortn.setStatus(_A)
_Pm1004AlmVcc5HighAlarmPortn_Type=EkiOnOff
_Pm1004AlmVcc5HighAlarmPortn_Object=MibTableColumn
pm1004AlmVcc5HighAlarmPortn=_Pm1004AlmVcc5HighAlarmPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,9),_Pm1004AlmVcc5HighAlarmPortn_Type())
pm1004AlmVcc5HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc5HighAlarmPortn.setStatus(_A)
_Pm1004AlmVee5LowWarningPortn_Type=EkiOnOff
_Pm1004AlmVee5LowWarningPortn_Object=MibTableColumn
pm1004AlmVee5LowWarningPortn=_Pm1004AlmVee5LowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,10),_Pm1004AlmVee5LowWarningPortn_Type())
pm1004AlmVee5LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVee5LowWarningPortn.setStatus(_A)
_Pm1004AlmVee5HighWarningPortn_Type=EkiOnOff
_Pm1004AlmVee5HighWarningPortn_Object=MibTableColumn
pm1004AlmVee5HighWarningPortn=_Pm1004AlmVee5HighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,11),_Pm1004AlmVee5HighWarningPortn_Type())
pm1004AlmVee5HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVee5HighWarningPortn.setStatus(_A)
_Pm1004AlmVcc2LowWarningPortn_Type=EkiOnOff
_Pm1004AlmVcc2LowWarningPortn_Object=MibTableColumn
pm1004AlmVcc2LowWarningPortn=_Pm1004AlmVcc2LowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,12),_Pm1004AlmVcc2LowWarningPortn_Type())
pm1004AlmVcc2LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc2LowWarningPortn.setStatus(_A)
_Pm1004AlmVcc2HighWarningPortn_Type=EkiOnOff
_Pm1004AlmVcc2HighWarningPortn_Object=MibTableColumn
pm1004AlmVcc2HighWarningPortn=_Pm1004AlmVcc2HighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,13),_Pm1004AlmVcc2HighWarningPortn_Type())
pm1004AlmVcc2HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc2HighWarningPortn.setStatus(_A)
_Pm1004AlmVcc3LowWarningPortn_Type=EkiOnOff
_Pm1004AlmVcc3LowWarningPortn_Object=MibTableColumn
pm1004AlmVcc3LowWarningPortn=_Pm1004AlmVcc3LowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,14),_Pm1004AlmVcc3LowWarningPortn_Type())
pm1004AlmVcc3LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc3LowWarningPortn.setStatus(_A)
_Pm1004AlmVcc3HighWarningPortn_Type=EkiOnOff
_Pm1004AlmVcc3HighWarningPortn_Object=MibTableColumn
pm1004AlmVcc3HighWarningPortn=_Pm1004AlmVcc3HighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,15),_Pm1004AlmVcc3HighWarningPortn_Type())
pm1004AlmVcc3HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc3HighWarningPortn.setStatus(_A)
_Pm1004AlmVcc5LowWarningPortn_Type=EkiOnOff
_Pm1004AlmVcc5LowWarningPortn_Object=MibTableColumn
pm1004AlmVcc5LowWarningPortn=_Pm1004AlmVcc5LowWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,16),_Pm1004AlmVcc5LowWarningPortn_Type())
pm1004AlmVcc5LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc5LowWarningPortn.setStatus(_A)
_Pm1004AlmVcc5HighWarningPortn_Type=EkiOnOff
_Pm1004AlmVcc5HighWarningPortn_Object=MibTableColumn
pm1004AlmVcc5HighWarningPortn=_Pm1004AlmVcc5HighWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,212,1,17),_Pm1004AlmVcc5HighWarningPortn_Type())
pm1004AlmVcc5HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmVcc5HighWarningPortn.setStatus(_A)
_Pm1004AlmlineOtx1TlhAlarmsTable_Object=MibTable
pm1004AlmlineOtx1TlhAlarmsTable=_Pm1004AlmlineOtx1TlhAlarmsTable_Object((1,3,6,1,4,1,20044,18,2,3,2,224))
if mibBuilder.loadTexts:pm1004AlmlineOtx1TlhAlarmsTable.setStatus(_A)
_Pm1004AlmlineOtx1TlhAlarmsEntry_Object=MibTableRow
pm1004AlmlineOtx1TlhAlarmsEntry=_Pm1004AlmlineOtx1TlhAlarmsEntry_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1))
pm1004AlmlineOtx1TlhAlarmsEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm1004AlmlineOtx1TlhAlarmsEntry.setStatus(_A)
class _Pm1004AlmlineOtx1TlhAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineOtx1TlhAlarmsIndex_Type.__name__=_D
_Pm1004AlmlineOtx1TlhAlarmsIndex_Object=MibTableColumn
pm1004AlmlineOtx1TlhAlarmsIndex=_Pm1004AlmlineOtx1TlhAlarmsIndex_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1,1),_Pm1004AlmlineOtx1TlhAlarmsIndex_Type())
pm1004AlmlineOtx1TlhAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineOtx1TlhAlarmsIndex.setStatus(_A)
_Pm1004AlmLineModulatorAgingHighAlaPortn_Type=EkiOnOff
_Pm1004AlmLineModulatorAgingHighAlaPortn_Object=MibTableColumn
pm1004AlmLineModulatorAgingHighAlaPortn=_Pm1004AlmLineModulatorAgingHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1,6),_Pm1004AlmLineModulatorAgingHighAlaPortn_Type())
pm1004AlmLineModulatorAgingHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineModulatorAgingHighAlaPortn.setStatus(_A)
_Pm1004AlmLineAgingHighAlaPortn_Type=EkiOnOff
_Pm1004AlmLineAgingHighAlaPortn_Object=MibTableColumn
pm1004AlmLineAgingHighAlaPortn=_Pm1004AlmLineAgingHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1,7),_Pm1004AlmLineAgingHighAlaPortn_Type())
pm1004AlmLineAgingHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineAgingHighAlaPortn.setStatus(_A)
_Pm1004AlmLineCdrNotReadyPortn_Type=EkiOnOff
_Pm1004AlmLineCdrNotReadyPortn_Object=MibTableColumn
pm1004AlmLineCdrNotReadyPortn=_Pm1004AlmLineCdrNotReadyPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1,10),_Pm1004AlmLineCdrNotReadyPortn_Type())
pm1004AlmLineCdrNotReadyPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineCdrNotReadyPortn.setStatus(_A)
_Pm1004AlmLineFreqDevHighAlaPortn_Type=EkiOnOff
_Pm1004AlmLineFreqDevHighAlaPortn_Object=MibTableColumn
pm1004AlmLineFreqDevHighAlaPortn=_Pm1004AlmLineFreqDevHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1,13),_Pm1004AlmLineFreqDevHighAlaPortn_Type())
pm1004AlmLineFreqDevHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineFreqDevHighAlaPortn.setStatus(_A)
_Pm1004AlmLineLaserTempHighAlaPortn_Type=EkiOnOff
_Pm1004AlmLineLaserTempHighAlaPortn_Object=MibTableColumn
pm1004AlmLineLaserTempHighAlaPortn=_Pm1004AlmLineLaserTempHighAlaPortn_Object((1,3,6,1,4,1,20044,18,2,3,2,224,1,15),_Pm1004AlmLineLaserTempHighAlaPortn_Type())
pm1004AlmLineLaserTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineLaserTempHighAlaPortn.setStatus(_A)
_Pm1004AlmLineCrit_ObjectIdentity=ObjectIdentity
pm1004AlmLineCrit=_Pm1004AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,18,2,3,3))
_Pm1004AlmsynthAlmLineTable_Object=MibTable
pm1004AlmsynthAlmLineTable=_Pm1004AlmsynthAlmLineTable_Object((1,3,6,1,4,1,20044,18,2,3,3,7))
if mibBuilder.loadTexts:pm1004AlmsynthAlmLineTable.setStatus(_A)
_Pm1004AlmsynthAlmLineEntry_Object=MibTableRow
pm1004AlmsynthAlmLineEntry=_Pm1004AlmsynthAlmLineEntry_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1))
pm1004AlmsynthAlmLineEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm1004AlmsynthAlmLineEntry.setStatus(_A)
class _Pm1004AlmsynthAlmLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmsynthAlmLineIndex_Type.__name__=_D
_Pm1004AlmsynthAlmLineIndex_Object=MibTableColumn
pm1004AlmsynthAlmLineIndex=_Pm1004AlmsynthAlmLineIndex_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,1),_Pm1004AlmsynthAlmLineIndex_Type())
pm1004AlmsynthAlmLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmsynthAlmLineIndex.setStatus(_A)
_Pm1004AlmXfpAbsentPortn_Type=EkiOnOff
_Pm1004AlmXfpAbsentPortn_Object=MibTableColumn
pm1004AlmXfpAbsentPortn=_Pm1004AlmXfpAbsentPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,2),_Pm1004AlmXfpAbsentPortn_Type())
pm1004AlmXfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmXfpAbsentPortn.setStatus(_A)
_Pm1004AlmXfpInitNotComplPortn_Type=EkiOnOff
_Pm1004AlmXfpInitNotComplPortn_Object=MibTableColumn
pm1004AlmXfpInitNotComplPortn=_Pm1004AlmXfpInitNotComplPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,3),_Pm1004AlmXfpInitNotComplPortn_Type())
pm1004AlmXfpInitNotComplPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmXfpInitNotComplPortn.setStatus(_A)
_Pm1004AlmLineHwFailPortn_Type=EkiOnOff
_Pm1004AlmLineHwFailPortn_Object=MibTableColumn
pm1004AlmLineHwFailPortn=_Pm1004AlmLineHwFailPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,5),_Pm1004AlmLineHwFailPortn_Type())
pm1004AlmLineHwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineHwFailPortn.setStatus(_A)
_Pm1004AlmXfpTxOffPortn_Type=EkiOnOff
_Pm1004AlmXfpTxOffPortn_Object=MibTableColumn
pm1004AlmXfpTxOffPortn=_Pm1004AlmXfpTxOffPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,6),_Pm1004AlmXfpTxOffPortn_Type())
pm1004AlmXfpTxOffPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmXfpTxOffPortn.setStatus(_A)
_Pm1004AlmLineLocalOosPortn_Type=EkiOnOff
_Pm1004AlmLineLocalOosPortn_Object=MibTableColumn
pm1004AlmLineLocalOosPortn=_Pm1004AlmLineLocalOosPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,7),_Pm1004AlmLineLocalOosPortn_Type())
pm1004AlmLineLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineLocalOosPortn.setStatus(_A)
_Pm1004AlmUpRdiInsPortn_Type=EkiOnOff
_Pm1004AlmUpRdiInsPortn_Object=MibTableColumn
pm1004AlmUpRdiInsPortn=_Pm1004AlmUpRdiInsPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,9),_Pm1004AlmUpRdiInsPortn_Type())
pm1004AlmUpRdiInsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmUpRdiInsPortn.setStatus(_A)
_Pm1004AlmLineDdmWarningPortn_Type=EkiOnOff
_Pm1004AlmLineDdmWarningPortn_Object=MibTableColumn
pm1004AlmLineDdmWarningPortn=_Pm1004AlmLineDdmWarningPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,10),_Pm1004AlmLineDdmWarningPortn_Type())
pm1004AlmLineDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineDdmWarningPortn.setStatus(_A)
_Pm1004AlmLineDdmAlmPortn_Type=EkiOnOff
_Pm1004AlmLineDdmAlmPortn_Object=MibTableColumn
pm1004AlmLineDdmAlmPortn=_Pm1004AlmLineDdmAlmPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,11),_Pm1004AlmLineDdmAlmPortn_Type())
pm1004AlmLineDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineDdmAlmPortn.setStatus(_A)
_Pm1004AlmLineFailPortn_Type=EkiOnOff
_Pm1004AlmLineFailPortn_Object=MibTableColumn
pm1004AlmLineFailPortn=_Pm1004AlmLineFailPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,13),_Pm1004AlmLineFailPortn_Type())
pm1004AlmLineFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineFailPortn.setStatus(_A)
_Pm1004AlmLineActivePortn_Type=EkiOnOff
_Pm1004AlmLineActivePortn_Object=MibTableColumn
pm1004AlmLineActivePortn=_Pm1004AlmLineActivePortn_Object((1,3,6,1,4,1,20044,18,2,3,3,7,1,17),_Pm1004AlmLineActivePortn_Type())
pm1004AlmLineActivePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmLineActivePortn.setStatus(_A)
_Pm1004AlmdfrmAlmTable_Object=MibTable
pm1004AlmdfrmAlmTable=_Pm1004AlmdfrmAlmTable_Object((1,3,6,1,4,1,20044,18,2,3,3,128))
if mibBuilder.loadTexts:pm1004AlmdfrmAlmTable.setStatus(_A)
_Pm1004AlmdfrmAlmEntry_Object=MibTableRow
pm1004AlmdfrmAlmEntry=_Pm1004AlmdfrmAlmEntry_Object((1,3,6,1,4,1,20044,18,2,3,3,128,1))
pm1004AlmdfrmAlmEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm1004AlmdfrmAlmEntry.setStatus(_A)
class _Pm1004AlmdfrmAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmdfrmAlmIndex_Type.__name__=_D
_Pm1004AlmdfrmAlmIndex_Object=MibTableColumn
pm1004AlmdfrmAlmIndex=_Pm1004AlmdfrmAlmIndex_Object((1,3,6,1,4,1,20044,18,2,3,3,128,1,1),_Pm1004AlmdfrmAlmIndex_Type())
pm1004AlmdfrmAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmdfrmAlmIndex.setStatus(_A)
_Pm1004AlmDwAisDetPortn_Type=EkiOnOff
_Pm1004AlmDwAisDetPortn_Object=MibTableColumn
pm1004AlmDwAisDetPortn=_Pm1004AlmDwAisDetPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,128,1,2),_Pm1004AlmDwAisDetPortn_Type())
pm1004AlmDwAisDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwAisDetPortn.setStatus(_A)
_Pm1004AlmDwRdiDetPortn_Type=EkiOnOff
_Pm1004AlmDwRdiDetPortn_Object=MibTableColumn
pm1004AlmDwRdiDetPortn=_Pm1004AlmDwRdiDetPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,128,1,3),_Pm1004AlmDwRdiDetPortn_Type())
pm1004AlmDwRdiDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwRdiDetPortn.setStatus(_A)
_Pm1004AlmDwOofPortn_Type=EkiOnOff
_Pm1004AlmDwOofPortn_Object=MibTableColumn
pm1004AlmDwOofPortn=_Pm1004AlmDwOofPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,128,1,4),_Pm1004AlmDwOofPortn_Type())
pm1004AlmDwOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwOofPortn.setStatus(_A)
_Pm1004AlmDwLofPortn_Type=EkiOnOff
_Pm1004AlmDwLofPortn_Object=MibTableColumn
pm1004AlmDwLofPortn=_Pm1004AlmDwLofPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,128,1,5),_Pm1004AlmDwLofPortn_Type())
pm1004AlmDwLofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwLofPortn.setStatus(_A)
_Pm1004AlmlineSyncAlarmsTable_Object=MibTable
pm1004AlmlineSyncAlarmsTable=_Pm1004AlmlineSyncAlarmsTable_Object((1,3,6,1,4,1,20044,18,2,3,3,133))
if mibBuilder.loadTexts:pm1004AlmlineSyncAlarmsTable.setStatus(_A)
_Pm1004AlmlineSyncAlarmsEntry_Object=MibTableRow
pm1004AlmlineSyncAlarmsEntry=_Pm1004AlmlineSyncAlarmsEntry_Object((1,3,6,1,4,1,20044,18,2,3,3,133,1))
pm1004AlmlineSyncAlarmsEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm1004AlmlineSyncAlarmsEntry.setStatus(_A)
class _Pm1004AlmlineSyncAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineSyncAlarmsIndex_Type.__name__=_D
_Pm1004AlmlineSyncAlarmsIndex_Object=MibTableColumn
pm1004AlmlineSyncAlarmsIndex=_Pm1004AlmlineSyncAlarmsIndex_Object((1,3,6,1,4,1,20044,18,2,3,3,133,1,1),_Pm1004AlmlineSyncAlarmsIndex_Type())
pm1004AlmlineSyncAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineSyncAlarmsIndex.setStatus(_A)
_Pm1004AlmDwLockerrPortn_Type=EkiOnOff
_Pm1004AlmDwLockerrPortn_Object=MibTableColumn
pm1004AlmDwLockerrPortn=_Pm1004AlmDwLockerrPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,133,1,13),_Pm1004AlmDwLockerrPortn_Type())
pm1004AlmDwLockerrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwLockerrPortn.setStatus(_A)
_Pm1004AlmUpLockerrPortn_Type=EkiOnOff
_Pm1004AlmUpLockerrPortn_Object=MibTableColumn
pm1004AlmUpLockerrPortn=_Pm1004AlmUpLockerrPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,133,1,14),_Pm1004AlmUpLockerrPortn_Type())
pm1004AlmUpLockerrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmUpLockerrPortn.setStatus(_A)
_Pm1004AlmDwLosPortn_Type=EkiOnOff
_Pm1004AlmDwLosPortn_Object=MibTableColumn
pm1004AlmDwLosPortn=_Pm1004AlmDwLosPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,133,1,17),_Pm1004AlmDwLosPortn_Type())
pm1004AlmDwLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmDwLosPortn.setStatus(_A)
_Pm1004AlmlineXfp1AlarmsTable_Object=MibTable
pm1004AlmlineXfp1AlarmsTable=_Pm1004AlmlineXfp1AlarmsTable_Object((1,3,6,1,4,1,20044,18,2,3,3,211))
if mibBuilder.loadTexts:pm1004AlmlineXfp1AlarmsTable.setStatus(_A)
_Pm1004AlmlineXfp1AlarmsEntry_Object=MibTableRow
pm1004AlmlineXfp1AlarmsEntry=_Pm1004AlmlineXfp1AlarmsEntry_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1))
pm1004AlmlineXfp1AlarmsEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm1004AlmlineXfp1AlarmsEntry.setStatus(_A)
class _Pm1004AlmlineXfp1AlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004AlmlineXfp1AlarmsIndex_Type.__name__=_D
_Pm1004AlmlineXfp1AlarmsIndex_Object=MibTableColumn
pm1004AlmlineXfp1AlarmsIndex=_Pm1004AlmlineXfp1AlarmsIndex_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,1),_Pm1004AlmlineXfp1AlarmsIndex_Type())
pm1004AlmlineXfp1AlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmlineXfp1AlarmsIndex.setStatus(_A)
_Pm1004AlmModNrPortn_Type=EkiOnOff
_Pm1004AlmModNrPortn_Object=MibTableColumn
pm1004AlmModNrPortn=_Pm1004AlmModNrPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,3),_Pm1004AlmModNrPortn_Type())
pm1004AlmModNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmModNrPortn.setStatus(_A)
_Pm1004AlmRxCdrNotLockedPortn_Type=EkiOnOff
_Pm1004AlmRxCdrNotLockedPortn_Object=MibTableColumn
pm1004AlmRxCdrNotLockedPortn=_Pm1004AlmRxCdrNotLockedPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,4),_Pm1004AlmRxCdrNotLockedPortn_Type())
pm1004AlmRxCdrNotLockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxCdrNotLockedPortn.setStatus(_A)
_Pm1004AlmRxNrPortn_Type=EkiOnOff
_Pm1004AlmRxNrPortn_Object=MibTableColumn
pm1004AlmRxNrPortn=_Pm1004AlmRxNrPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,6),_Pm1004AlmRxNrPortn_Type())
pm1004AlmRxNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmRxNrPortn.setStatus(_A)
_Pm1004AlmTxCdrNotLockedPortn_Type=EkiOnOff
_Pm1004AlmTxCdrNotLockedPortn_Object=MibTableColumn
pm1004AlmTxCdrNotLockedPortn=_Pm1004AlmTxCdrNotLockedPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,7),_Pm1004AlmTxCdrNotLockedPortn_Type())
pm1004AlmTxCdrNotLockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxCdrNotLockedPortn.setStatus(_A)
_Pm1004AlmTxFaultPortn_Type=EkiOnOff
_Pm1004AlmTxFaultPortn_Object=MibTableColumn
pm1004AlmTxFaultPortn=_Pm1004AlmTxFaultPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,8),_Pm1004AlmTxFaultPortn_Type())
pm1004AlmTxFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxFaultPortn.setStatus(_A)
_Pm1004AlmTxNrPortn_Type=EkiOnOff
_Pm1004AlmTxNrPortn_Object=MibTableColumn
pm1004AlmTxNrPortn=_Pm1004AlmTxNrPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,9),_Pm1004AlmTxNrPortn_Type())
pm1004AlmTxNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTxNrPortn.setStatus(_A)
_Pm1004AlmChannelNotAcquiredPortn_Type=EkiOnOff
_Pm1004AlmChannelNotAcquiredPortn_Object=MibTableColumn
pm1004AlmChannelNotAcquiredPortn=_Pm1004AlmChannelNotAcquiredPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,11),_Pm1004AlmChannelNotAcquiredPortn_Type())
pm1004AlmChannelNotAcquiredPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmChannelNotAcquiredPortn.setStatus(_A)
_Pm1004AlmWavelengthUnlockedPortn_Type=EkiOnOff
_Pm1004AlmWavelengthUnlockedPortn_Object=MibTableColumn
pm1004AlmWavelengthUnlockedPortn=_Pm1004AlmWavelengthUnlockedPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,15),_Pm1004AlmWavelengthUnlockedPortn_Type())
pm1004AlmWavelengthUnlockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmWavelengthUnlockedPortn.setStatus(_A)
_Pm1004AlmTecFaultPortn_Type=EkiOnOff
_Pm1004AlmTecFaultPortn_Object=MibTableColumn
pm1004AlmTecFaultPortn=_Pm1004AlmTecFaultPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,16),_Pm1004AlmTecFaultPortn_Type())
pm1004AlmTecFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmTecFaultPortn.setStatus(_A)
_Pm1004AlmApdSupplyFaultPortn_Type=EkiOnOff
_Pm1004AlmApdSupplyFaultPortn_Object=MibTableColumn
pm1004AlmApdSupplyFaultPortn=_Pm1004AlmApdSupplyFaultPortn_Object((1,3,6,1,4,1,20044,18,2,3,3,211,1,17),_Pm1004AlmApdSupplyFaultPortn_Type())
pm1004AlmApdSupplyFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmApdSupplyFaultPortn.setStatus(_A)
_Pm1004measures_ObjectIdentity=ObjectIdentity
pm1004measures=_Pm1004measures_ObjectIdentity((1,3,6,1,4,1,20044,18,3))
_Pm1004MesrOther_ObjectIdentity=ObjectIdentity
pm1004MesrOther=_Pm1004MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,18,3,1))
_Pm1004Mesrsynth0_Type=EkiMeasureType
_Pm1004Mesrsynth0_Object=MibScalar
pm1004Mesrsynth0=_Pm1004Mesrsynth0_Object((1,3,6,1,4,1,20044,18,3,1,0),_Pm1004Mesrsynth0_Type())
pm1004Mesrsynth0.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrsynth0.setStatus(_G)
_Pm1004Mesrsynth1_Type=EkiMeasureType
_Pm1004Mesrsynth1_Object=MibScalar
pm1004Mesrsynth1=_Pm1004Mesrsynth1_Object((1,3,6,1,4,1,20044,18,3,1,1),_Pm1004Mesrsynth1_Type())
pm1004Mesrsynth1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrsynth1.setStatus(_G)
_Pm1004MesrClient_ObjectIdentity=ObjectIdentity
pm1004MesrClient=_Pm1004MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,18,3,2))
_Pm1004MesrtempMeasTable_Object=MibTable
pm1004MesrtempMeasTable=_Pm1004MesrtempMeasTable_Object((1,3,6,1,4,1,20044,18,3,2,16))
if mibBuilder.loadTexts:pm1004MesrtempMeasTable.setStatus(_A)
_Pm1004MesrtempMeasEntry_Object=MibTableRow
pm1004MesrtempMeasEntry=_Pm1004MesrtempMeasEntry_Object((1,3,6,1,4,1,20044,18,3,2,16,1))
pm1004MesrtempMeasEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm1004MesrtempMeasEntry.setStatus(_A)
class _Pm1004MesrtempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004MesrtempMeasIndex_Type.__name__=_D
_Pm1004MesrtempMeasIndex_Object=MibTableColumn
pm1004MesrtempMeasIndex=_Pm1004MesrtempMeasIndex_Object((1,3,6,1,4,1,20044,18,3,2,16,1,1),_Pm1004MesrtempMeasIndex_Type())
pm1004MesrtempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrtempMeasIndex.setStatus(_A)
class _Pm1004MesrtempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004MesrtempMeasPortn_Type.__name__=_D
_Pm1004MesrtempMeasPortn_Object=MibTableColumn
pm1004MesrtempMeasPortn=_Pm1004MesrtempMeasPortn_Object((1,3,6,1,4,1,20044,18,3,2,16,1,2),_Pm1004MesrtempMeasPortn_Type())
pm1004MesrtempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrtempMeasPortn.setStatus(_A)
_Pm1004MesrvoltMeasTable_Object=MibTable
pm1004MesrvoltMeasTable=_Pm1004MesrvoltMeasTable_Object((1,3,6,1,4,1,20044,18,3,2,24))
if mibBuilder.loadTexts:pm1004MesrvoltMeasTable.setStatus(_A)
_Pm1004MesrvoltMeasEntry_Object=MibTableRow
pm1004MesrvoltMeasEntry=_Pm1004MesrvoltMeasEntry_Object((1,3,6,1,4,1,20044,18,3,2,24,1))
pm1004MesrvoltMeasEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm1004MesrvoltMeasEntry.setStatus(_A)
class _Pm1004MesrvoltMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004MesrvoltMeasIndex_Type.__name__=_D
_Pm1004MesrvoltMeasIndex_Object=MibTableColumn
pm1004MesrvoltMeasIndex=_Pm1004MesrvoltMeasIndex_Object((1,3,6,1,4,1,20044,18,3,2,24,1,1),_Pm1004MesrvoltMeasIndex_Type())
pm1004MesrvoltMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrvoltMeasIndex.setStatus(_A)
class _Pm1004MesrvoltMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004MesrvoltMeasPortn_Type.__name__=_D
_Pm1004MesrvoltMeasPortn_Object=MibTableColumn
pm1004MesrvoltMeasPortn=_Pm1004MesrvoltMeasPortn_Object((1,3,6,1,4,1,20044,18,3,2,24,1,2),_Pm1004MesrvoltMeasPortn_Type())
pm1004MesrvoltMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrvoltMeasPortn.setStatus(_A)
_Pm1004MesrbiasMeasTable_Object=MibTable
pm1004MesrbiasMeasTable=_Pm1004MesrbiasMeasTable_Object((1,3,6,1,4,1,20044,18,3,2,32))
if mibBuilder.loadTexts:pm1004MesrbiasMeasTable.setStatus(_A)
_Pm1004MesrbiasMeasEntry_Object=MibTableRow
pm1004MesrbiasMeasEntry=_Pm1004MesrbiasMeasEntry_Object((1,3,6,1,4,1,20044,18,3,2,32,1))
pm1004MesrbiasMeasEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm1004MesrbiasMeasEntry.setStatus(_A)
class _Pm1004MesrbiasMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004MesrbiasMeasIndex_Type.__name__=_D
_Pm1004MesrbiasMeasIndex_Object=MibTableColumn
pm1004MesrbiasMeasIndex=_Pm1004MesrbiasMeasIndex_Object((1,3,6,1,4,1,20044,18,3,2,32,1,1),_Pm1004MesrbiasMeasIndex_Type())
pm1004MesrbiasMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrbiasMeasIndex.setStatus(_A)
class _Pm1004MesrbiasMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004MesrbiasMeasPortn_Type.__name__=_D
_Pm1004MesrbiasMeasPortn_Object=MibTableColumn
pm1004MesrbiasMeasPortn=_Pm1004MesrbiasMeasPortn_Object((1,3,6,1,4,1,20044,18,3,2,32,1,2),_Pm1004MesrbiasMeasPortn_Type())
pm1004MesrbiasMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrbiasMeasPortn.setStatus(_A)
_Pm1004MesrtxpwrMeasTable_Object=MibTable
pm1004MesrtxpwrMeasTable=_Pm1004MesrtxpwrMeasTable_Object((1,3,6,1,4,1,20044,18,3,2,40))
if mibBuilder.loadTexts:pm1004MesrtxpwrMeasTable.setStatus(_A)
_Pm1004MesrtxpwrMeasEntry_Object=MibTableRow
pm1004MesrtxpwrMeasEntry=_Pm1004MesrtxpwrMeasEntry_Object((1,3,6,1,4,1,20044,18,3,2,40,1))
pm1004MesrtxpwrMeasEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm1004MesrtxpwrMeasEntry.setStatus(_A)
class _Pm1004MesrtxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004MesrtxpwrMeasIndex_Type.__name__=_D
_Pm1004MesrtxpwrMeasIndex_Object=MibTableColumn
pm1004MesrtxpwrMeasIndex=_Pm1004MesrtxpwrMeasIndex_Object((1,3,6,1,4,1,20044,18,3,2,40,1,1),_Pm1004MesrtxpwrMeasIndex_Type())
pm1004MesrtxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrtxpwrMeasIndex.setStatus(_A)
class _Pm1004MesrtxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004MesrtxpwrMeasPortn_Type.__name__=_D
_Pm1004MesrtxpwrMeasPortn_Object=MibTableColumn
pm1004MesrtxpwrMeasPortn=_Pm1004MesrtxpwrMeasPortn_Object((1,3,6,1,4,1,20044,18,3,2,40,1,2),_Pm1004MesrtxpwrMeasPortn_Type())
pm1004MesrtxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrtxpwrMeasPortn.setStatus(_A)
_Pm1004MesrrxpwrMeasTable_Object=MibTable
pm1004MesrrxpwrMeasTable=_Pm1004MesrrxpwrMeasTable_Object((1,3,6,1,4,1,20044,18,3,2,48))
if mibBuilder.loadTexts:pm1004MesrrxpwrMeasTable.setStatus(_A)
_Pm1004MesrrxpwrMeasEntry_Object=MibTableRow
pm1004MesrrxpwrMeasEntry=_Pm1004MesrrxpwrMeasEntry_Object((1,3,6,1,4,1,20044,18,3,2,48,1))
pm1004MesrrxpwrMeasEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm1004MesrrxpwrMeasEntry.setStatus(_A)
class _Pm1004MesrrxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004MesrrxpwrMeasIndex_Type.__name__=_D
_Pm1004MesrrxpwrMeasIndex_Object=MibTableColumn
pm1004MesrrxpwrMeasIndex=_Pm1004MesrrxpwrMeasIndex_Object((1,3,6,1,4,1,20044,18,3,2,48,1,1),_Pm1004MesrrxpwrMeasIndex_Type())
pm1004MesrrxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrrxpwrMeasIndex.setStatus(_A)
class _Pm1004MesrrxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004MesrrxpwrMeasPortn_Type.__name__=_D
_Pm1004MesrrxpwrMeasPortn_Object=MibTableColumn
pm1004MesrrxpwrMeasPortn=_Pm1004MesrrxpwrMeasPortn_Object((1,3,6,1,4,1,20044,18,3,2,48,1,2),_Pm1004MesrrxpwrMeasPortn_Type())
pm1004MesrrxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004MesrrxpwrMeasPortn.setStatus(_A)
_Pm1004MesrLine_ObjectIdentity=ObjectIdentity
pm1004MesrLine=_Pm1004MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,18,3,3))
_Pm1004Mesrxfp1LxModTempMeasTable_Object=MibTable
pm1004Mesrxfp1LxModTempMeasTable=_Pm1004Mesrxfp1LxModTempMeasTable_Object((1,3,6,1,4,1,20044,18,3,3,208))
if mibBuilder.loadTexts:pm1004Mesrxfp1LxModTempMeasTable.setStatus(_A)
_Pm1004Mesrxfp1LxModTempMeasEntry_Object=MibTableRow
pm1004Mesrxfp1LxModTempMeasEntry=_Pm1004Mesrxfp1LxModTempMeasEntry_Object((1,3,6,1,4,1,20044,18,3,3,208,1))
pm1004Mesrxfp1LxModTempMeasEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm1004Mesrxfp1LxModTempMeasEntry.setStatus(_A)
class _Pm1004Mesrxfp1LxModTempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1LxModTempMeasIndex_Type.__name__=_D
_Pm1004Mesrxfp1LxModTempMeasIndex_Object=MibTableColumn
pm1004Mesrxfp1LxModTempMeasIndex=_Pm1004Mesrxfp1LxModTempMeasIndex_Object((1,3,6,1,4,1,20044,18,3,3,208,1,1),_Pm1004Mesrxfp1LxModTempMeasIndex_Type())
pm1004Mesrxfp1LxModTempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LxModTempMeasIndex.setStatus(_A)
class _Pm1004Mesrxfp1LxModTempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1LxModTempMeasPortn_Type.__name__=_D
_Pm1004Mesrxfp1LxModTempMeasPortn_Object=MibTableColumn
pm1004Mesrxfp1LxModTempMeasPortn=_Pm1004Mesrxfp1LxModTempMeasPortn_Object((1,3,6,1,4,1,20044,18,3,3,208,1,2),_Pm1004Mesrxfp1LxModTempMeasPortn_Type())
pm1004Mesrxfp1LxModTempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LxModTempMeasPortn.setStatus(_A)
_Pm1004Mesrxfp1ReservedTable_Object=MibTable
pm1004Mesrxfp1ReservedTable=_Pm1004Mesrxfp1ReservedTable_Object((1,3,6,1,4,1,20044,18,3,3,209))
if mibBuilder.loadTexts:pm1004Mesrxfp1ReservedTable.setStatus(_G)
_Pm1004Mesrxfp1ReservedEntry_Object=MibTableRow
pm1004Mesrxfp1ReservedEntry=_Pm1004Mesrxfp1ReservedEntry_Object((1,3,6,1,4,1,20044,18,3,3,209,1))
pm1004Mesrxfp1ReservedEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm1004Mesrxfp1ReservedEntry.setStatus(_G)
class _Pm1004Mesrxfp1ReservedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1ReservedIndex_Type.__name__=_D
_Pm1004Mesrxfp1ReservedIndex_Object=MibTableColumn
pm1004Mesrxfp1ReservedIndex=_Pm1004Mesrxfp1ReservedIndex_Object((1,3,6,1,4,1,20044,18,3,3,209,1,1),_Pm1004Mesrxfp1ReservedIndex_Type())
pm1004Mesrxfp1ReservedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1ReservedIndex.setStatus(_G)
class _Pm1004Mesrxfp1ReservedPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1ReservedPortn_Type.__name__=_D
_Pm1004Mesrxfp1ReservedPortn_Object=MibTableColumn
pm1004Mesrxfp1ReservedPortn=_Pm1004Mesrxfp1ReservedPortn_Object((1,3,6,1,4,1,20044,18,3,3,209,1,2),_Pm1004Mesrxfp1ReservedPortn_Type())
pm1004Mesrxfp1ReservedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1ReservedPortn.setStatus(_G)
_Pm1004Mesrxfp1LoBiasCurrentMeasTable_Object=MibTable
pm1004Mesrxfp1LoBiasCurrentMeasTable=_Pm1004Mesrxfp1LoBiasCurrentMeasTable_Object((1,3,6,1,4,1,20044,18,3,3,210))
if mibBuilder.loadTexts:pm1004Mesrxfp1LoBiasCurrentMeasTable.setStatus(_A)
_Pm1004Mesrxfp1LoBiasCurrentMeasEntry_Object=MibTableRow
pm1004Mesrxfp1LoBiasCurrentMeasEntry=_Pm1004Mesrxfp1LoBiasCurrentMeasEntry_Object((1,3,6,1,4,1,20044,18,3,3,210,1))
pm1004Mesrxfp1LoBiasCurrentMeasEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm1004Mesrxfp1LoBiasCurrentMeasEntry.setStatus(_A)
class _Pm1004Mesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1LoBiasCurrentMeasIndex_Type.__name__=_D
_Pm1004Mesrxfp1LoBiasCurrentMeasIndex_Object=MibTableColumn
pm1004Mesrxfp1LoBiasCurrentMeasIndex=_Pm1004Mesrxfp1LoBiasCurrentMeasIndex_Object((1,3,6,1,4,1,20044,18,3,3,210,1,1),_Pm1004Mesrxfp1LoBiasCurrentMeasIndex_Type())
pm1004Mesrxfp1LoBiasCurrentMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LoBiasCurrentMeasIndex.setStatus(_A)
class _Pm1004Mesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1LoBiasCurrentMeasPortn_Type.__name__=_D
_Pm1004Mesrxfp1LoBiasCurrentMeasPortn_Object=MibTableColumn
pm1004Mesrxfp1LoBiasCurrentMeasPortn=_Pm1004Mesrxfp1LoBiasCurrentMeasPortn_Object((1,3,6,1,4,1,20044,18,3,3,210,1,2),_Pm1004Mesrxfp1LoBiasCurrentMeasPortn_Type())
pm1004Mesrxfp1LoBiasCurrentMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LoBiasCurrentMeasPortn.setStatus(_A)
_Pm1004Mesrxfp1LoTxPowerMeasTable_Object=MibTable
pm1004Mesrxfp1LoTxPowerMeasTable=_Pm1004Mesrxfp1LoTxPowerMeasTable_Object((1,3,6,1,4,1,20044,18,3,3,211))
if mibBuilder.loadTexts:pm1004Mesrxfp1LoTxPowerMeasTable.setStatus(_A)
_Pm1004Mesrxfp1LoTxPowerMeasEntry_Object=MibTableRow
pm1004Mesrxfp1LoTxPowerMeasEntry=_Pm1004Mesrxfp1LoTxPowerMeasEntry_Object((1,3,6,1,4,1,20044,18,3,3,211,1))
pm1004Mesrxfp1LoTxPowerMeasEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm1004Mesrxfp1LoTxPowerMeasEntry.setStatus(_A)
class _Pm1004Mesrxfp1LoTxPowerMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1LoTxPowerMeasIndex_Type.__name__=_D
_Pm1004Mesrxfp1LoTxPowerMeasIndex_Object=MibTableColumn
pm1004Mesrxfp1LoTxPowerMeasIndex=_Pm1004Mesrxfp1LoTxPowerMeasIndex_Object((1,3,6,1,4,1,20044,18,3,3,211,1,1),_Pm1004Mesrxfp1LoTxPowerMeasIndex_Type())
pm1004Mesrxfp1LoTxPowerMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LoTxPowerMeasIndex.setStatus(_A)
class _Pm1004Mesrxfp1LoTxPowerMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1LoTxPowerMeasPortn_Type.__name__=_D
_Pm1004Mesrxfp1LoTxPowerMeasPortn_Object=MibTableColumn
pm1004Mesrxfp1LoTxPowerMeasPortn=_Pm1004Mesrxfp1LoTxPowerMeasPortn_Object((1,3,6,1,4,1,20044,18,3,3,211,1,2),_Pm1004Mesrxfp1LoTxPowerMeasPortn_Type())
pm1004Mesrxfp1LoTxPowerMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LoTxPowerMeasPortn.setStatus(_A)
_Pm1004Mesrxfp1LiRxPowerMeasTable_Object=MibTable
pm1004Mesrxfp1LiRxPowerMeasTable=_Pm1004Mesrxfp1LiRxPowerMeasTable_Object((1,3,6,1,4,1,20044,18,3,3,212))
if mibBuilder.loadTexts:pm1004Mesrxfp1LiRxPowerMeasTable.setStatus(_A)
_Pm1004Mesrxfp1LiRxPowerMeasEntry_Object=MibTableRow
pm1004Mesrxfp1LiRxPowerMeasEntry=_Pm1004Mesrxfp1LiRxPowerMeasEntry_Object((1,3,6,1,4,1,20044,18,3,3,212,1))
pm1004Mesrxfp1LiRxPowerMeasEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm1004Mesrxfp1LiRxPowerMeasEntry.setStatus(_A)
class _Pm1004Mesrxfp1LiRxPowerMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1LiRxPowerMeasIndex_Type.__name__=_D
_Pm1004Mesrxfp1LiRxPowerMeasIndex_Object=MibTableColumn
pm1004Mesrxfp1LiRxPowerMeasIndex=_Pm1004Mesrxfp1LiRxPowerMeasIndex_Object((1,3,6,1,4,1,20044,18,3,3,212,1,1),_Pm1004Mesrxfp1LiRxPowerMeasIndex_Type())
pm1004Mesrxfp1LiRxPowerMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LiRxPowerMeasIndex.setStatus(_A)
class _Pm1004Mesrxfp1LiRxPowerMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1LiRxPowerMeasPortn_Type.__name__=_D
_Pm1004Mesrxfp1LiRxPowerMeasPortn_Object=MibTableColumn
pm1004Mesrxfp1LiRxPowerMeasPortn=_Pm1004Mesrxfp1LiRxPowerMeasPortn_Object((1,3,6,1,4,1,20044,18,3,3,212,1,2),_Pm1004Mesrxfp1LiRxPowerMeasPortn_Type())
pm1004Mesrxfp1LiRxPowerMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LiRxPowerMeasPortn.setStatus(_A)
_Pm1004Mesrxfp1LxAux1MeasTable_Object=MibTable
pm1004Mesrxfp1LxAux1MeasTable=_Pm1004Mesrxfp1LxAux1MeasTable_Object((1,3,6,1,4,1,20044,18,3,3,213))
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux1MeasTable.setStatus(_G)
_Pm1004Mesrxfp1LxAux1MeasEntry_Object=MibTableRow
pm1004Mesrxfp1LxAux1MeasEntry=_Pm1004Mesrxfp1LxAux1MeasEntry_Object((1,3,6,1,4,1,20044,18,3,3,213,1))
pm1004Mesrxfp1LxAux1MeasEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux1MeasEntry.setStatus(_G)
class _Pm1004Mesrxfp1LxAux1MeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1LxAux1MeasIndex_Type.__name__=_D
_Pm1004Mesrxfp1LxAux1MeasIndex_Object=MibTableColumn
pm1004Mesrxfp1LxAux1MeasIndex=_Pm1004Mesrxfp1LxAux1MeasIndex_Object((1,3,6,1,4,1,20044,18,3,3,213,1,1),_Pm1004Mesrxfp1LxAux1MeasIndex_Type())
pm1004Mesrxfp1LxAux1MeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux1MeasIndex.setStatus(_G)
class _Pm1004Mesrxfp1LxAux1MeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1LxAux1MeasPortn_Type.__name__=_D
_Pm1004Mesrxfp1LxAux1MeasPortn_Object=MibTableColumn
pm1004Mesrxfp1LxAux1MeasPortn=_Pm1004Mesrxfp1LxAux1MeasPortn_Object((1,3,6,1,4,1,20044,18,3,3,213,1,2),_Pm1004Mesrxfp1LxAux1MeasPortn_Type())
pm1004Mesrxfp1LxAux1MeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux1MeasPortn.setStatus(_G)
_Pm1004Mesrxfp1LxAux2MeasTable_Object=MibTable
pm1004Mesrxfp1LxAux2MeasTable=_Pm1004Mesrxfp1LxAux2MeasTable_Object((1,3,6,1,4,1,20044,18,3,3,214))
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux2MeasTable.setStatus(_G)
_Pm1004Mesrxfp1LxAux2MeasEntry_Object=MibTableRow
pm1004Mesrxfp1LxAux2MeasEntry=_Pm1004Mesrxfp1LxAux2MeasEntry_Object((1,3,6,1,4,1,20044,18,3,3,214,1))
pm1004Mesrxfp1LxAux2MeasEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux2MeasEntry.setStatus(_G)
class _Pm1004Mesrxfp1LxAux2MeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrxfp1LxAux2MeasIndex_Type.__name__=_D
_Pm1004Mesrxfp1LxAux2MeasIndex_Object=MibTableColumn
pm1004Mesrxfp1LxAux2MeasIndex=_Pm1004Mesrxfp1LxAux2MeasIndex_Object((1,3,6,1,4,1,20044,18,3,3,214,1,1),_Pm1004Mesrxfp1LxAux2MeasIndex_Type())
pm1004Mesrxfp1LxAux2MeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux2MeasIndex.setStatus(_G)
class _Pm1004Mesrxfp1LxAux2MeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrxfp1LxAux2MeasPortn_Type.__name__=_D
_Pm1004Mesrxfp1LxAux2MeasPortn_Object=MibTableColumn
pm1004Mesrxfp1LxAux2MeasPortn=_Pm1004Mesrxfp1LxAux2MeasPortn_Object((1,3,6,1,4,1,20044,18,3,3,214,1,2),_Pm1004Mesrxfp1LxAux2MeasPortn_Type())
pm1004Mesrxfp1LxAux2MeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrxfp1LxAux2MeasPortn.setStatus(_G)
_Pm1004Mesrotx1AgingTable_Object=MibTable
pm1004Mesrotx1AgingTable=_Pm1004Mesrotx1AgingTable_Object((1,3,6,1,4,1,20044,18,3,3,224))
if mibBuilder.loadTexts:pm1004Mesrotx1AgingTable.setStatus(_A)
_Pm1004Mesrotx1AgingEntry_Object=MibTableRow
pm1004Mesrotx1AgingEntry=_Pm1004Mesrotx1AgingEntry_Object((1,3,6,1,4,1,20044,18,3,3,224,1))
pm1004Mesrotx1AgingEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm1004Mesrotx1AgingEntry.setStatus(_A)
class _Pm1004Mesrotx1AgingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrotx1AgingIndex_Type.__name__=_D
_Pm1004Mesrotx1AgingIndex_Object=MibTableColumn
pm1004Mesrotx1AgingIndex=_Pm1004Mesrotx1AgingIndex_Object((1,3,6,1,4,1,20044,18,3,3,224,1,1),_Pm1004Mesrotx1AgingIndex_Type())
pm1004Mesrotx1AgingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1AgingIndex.setStatus(_A)
class _Pm1004Mesrotx1AgingPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrotx1AgingPortn_Type.__name__=_D
_Pm1004Mesrotx1AgingPortn_Object=MibTableColumn
pm1004Mesrotx1AgingPortn=_Pm1004Mesrotx1AgingPortn_Object((1,3,6,1,4,1,20044,18,3,3,224,1,2),_Pm1004Mesrotx1AgingPortn_Type())
pm1004Mesrotx1AgingPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1AgingPortn.setStatus(_A)
_Pm1004Mesrotx1LaserTemperatureTable_Object=MibTable
pm1004Mesrotx1LaserTemperatureTable=_Pm1004Mesrotx1LaserTemperatureTable_Object((1,3,6,1,4,1,20044,18,3,3,225))
if mibBuilder.loadTexts:pm1004Mesrotx1LaserTemperatureTable.setStatus(_G)
_Pm1004Mesrotx1LaserTemperatureEntry_Object=MibTableRow
pm1004Mesrotx1LaserTemperatureEntry=_Pm1004Mesrotx1LaserTemperatureEntry_Object((1,3,6,1,4,1,20044,18,3,3,225,1))
pm1004Mesrotx1LaserTemperatureEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm1004Mesrotx1LaserTemperatureEntry.setStatus(_G)
class _Pm1004Mesrotx1LaserTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrotx1LaserTemperatureIndex_Type.__name__=_D
_Pm1004Mesrotx1LaserTemperatureIndex_Object=MibTableColumn
pm1004Mesrotx1LaserTemperatureIndex=_Pm1004Mesrotx1LaserTemperatureIndex_Object((1,3,6,1,4,1,20044,18,3,3,225,1,1),_Pm1004Mesrotx1LaserTemperatureIndex_Type())
pm1004Mesrotx1LaserTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1LaserTemperatureIndex.setStatus(_G)
class _Pm1004Mesrotx1LaserTemperaturePortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrotx1LaserTemperaturePortn_Type.__name__=_D
_Pm1004Mesrotx1LaserTemperaturePortn_Object=MibTableColumn
pm1004Mesrotx1LaserTemperaturePortn=_Pm1004Mesrotx1LaserTemperaturePortn_Object((1,3,6,1,4,1,20044,18,3,3,225,1,2),_Pm1004Mesrotx1LaserTemperaturePortn_Type())
pm1004Mesrotx1LaserTemperaturePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1LaserTemperaturePortn.setStatus(_G)
_Pm1004Mesrotx1FreqDeviationTable_Object=MibTable
pm1004Mesrotx1FreqDeviationTable=_Pm1004Mesrotx1FreqDeviationTable_Object((1,3,6,1,4,1,20044,18,3,3,226))
if mibBuilder.loadTexts:pm1004Mesrotx1FreqDeviationTable.setStatus(_A)
_Pm1004Mesrotx1FreqDeviationEntry_Object=MibTableRow
pm1004Mesrotx1FreqDeviationEntry=_Pm1004Mesrotx1FreqDeviationEntry_Object((1,3,6,1,4,1,20044,18,3,3,226,1))
pm1004Mesrotx1FreqDeviationEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm1004Mesrotx1FreqDeviationEntry.setStatus(_A)
class _Pm1004Mesrotx1FreqDeviationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrotx1FreqDeviationIndex_Type.__name__=_D
_Pm1004Mesrotx1FreqDeviationIndex_Object=MibTableColumn
pm1004Mesrotx1FreqDeviationIndex=_Pm1004Mesrotx1FreqDeviationIndex_Object((1,3,6,1,4,1,20044,18,3,3,226,1,1),_Pm1004Mesrotx1FreqDeviationIndex_Type())
pm1004Mesrotx1FreqDeviationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1FreqDeviationIndex.setStatus(_A)
class _Pm1004Mesrotx1FreqDeviationPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrotx1FreqDeviationPortn_Type.__name__=_D
_Pm1004Mesrotx1FreqDeviationPortn_Object=MibTableColumn
pm1004Mesrotx1FreqDeviationPortn=_Pm1004Mesrotx1FreqDeviationPortn_Object((1,3,6,1,4,1,20044,18,3,3,226,1,2),_Pm1004Mesrotx1FreqDeviationPortn_Type())
pm1004Mesrotx1FreqDeviationPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1FreqDeviationPortn.setStatus(_A)
_Pm1004Mesrotx1LaserWvlengthTable_Object=MibTable
pm1004Mesrotx1LaserWvlengthTable=_Pm1004Mesrotx1LaserWvlengthTable_Object((1,3,6,1,4,1,20044,18,3,3,227))
if mibBuilder.loadTexts:pm1004Mesrotx1LaserWvlengthTable.setStatus(_A)
_Pm1004Mesrotx1LaserWvlengthEntry_Object=MibTableRow
pm1004Mesrotx1LaserWvlengthEntry=_Pm1004Mesrotx1LaserWvlengthEntry_Object((1,3,6,1,4,1,20044,18,3,3,227,1))
pm1004Mesrotx1LaserWvlengthEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm1004Mesrotx1LaserWvlengthEntry.setStatus(_A)
class _Pm1004Mesrotx1LaserWvlengthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Mesrotx1LaserWvlengthIndex_Type.__name__=_D
_Pm1004Mesrotx1LaserWvlengthIndex_Object=MibTableColumn
pm1004Mesrotx1LaserWvlengthIndex=_Pm1004Mesrotx1LaserWvlengthIndex_Object((1,3,6,1,4,1,20044,18,3,3,227,1,1),_Pm1004Mesrotx1LaserWvlengthIndex_Type())
pm1004Mesrotx1LaserWvlengthIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1LaserWvlengthIndex.setStatus(_A)
class _Pm1004Mesrotx1LaserWvlengthPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004Mesrotx1LaserWvlengthPortn_Type.__name__=_D
_Pm1004Mesrotx1LaserWvlengthPortn_Object=MibTableColumn
pm1004Mesrotx1LaserWvlengthPortn=_Pm1004Mesrotx1LaserWvlengthPortn_Object((1,3,6,1,4,1,20044,18,3,3,227,1,2),_Pm1004Mesrotx1LaserWvlengthPortn_Type())
pm1004Mesrotx1LaserWvlengthPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Mesrotx1LaserWvlengthPortn.setStatus(_A)
_Pm1004counters_ObjectIdentity=ObjectIdentity
pm1004counters=_Pm1004counters_ObjectIdentity((1,3,6,1,4,1,20044,18,4))
_Pm1004CntOther_ObjectIdentity=ObjectIdentity
pm1004CntOther=_Pm1004CntOther_ObjectIdentity((1,3,6,1,4,1,20044,18,4,1))
_Pm1004CntClient_ObjectIdentity=ObjectIdentity
pm1004CntClient=_Pm1004CntClient_ObjectIdentity((1,3,6,1,4,1,20044,18,4,2))
_Pm1004CntupRaRemCntTable_Object=MibTable
pm1004CntupRaRemCntTable=_Pm1004CntupRaRemCntTable_Object((1,3,6,1,4,1,20044,18,4,2,16))
if mibBuilder.loadTexts:pm1004CntupRaRemCntTable.setStatus(_A)
_Pm1004CntupRaRemCntEntry_Object=MibTableRow
pm1004CntupRaRemCntEntry=_Pm1004CntupRaRemCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,16,1))
pm1004CntupRaRemCntEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm1004CntupRaRemCntEntry.setStatus(_A)
class _Pm1004CntupRaRemCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntupRaRemCntIndex_Type.__name__=_D
_Pm1004CntupRaRemCntIndex_Object=MibTableColumn
pm1004CntupRaRemCntIndex=_Pm1004CntupRaRemCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,16,1,1),_Pm1004CntupRaRemCntIndex_Type())
pm1004CntupRaRemCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaRemCntIndex.setStatus(_A)
_Pm1004CntupRaRemCntValuePortn_Type=Counter32
_Pm1004CntupRaRemCntValuePortn_Object=MibTableColumn
pm1004CntupRaRemCntValuePortn=_Pm1004CntupRaRemCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,16,1,2),_Pm1004CntupRaRemCntValuePortn_Type())
pm1004CntupRaRemCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaRemCntValuePortn.setStatus(_A)
_Pm1004CntupRaRemCntErrorPortn_Type=EkiOnOff
_Pm1004CntupRaRemCntErrorPortn_Object=MibTableColumn
pm1004CntupRaRemCntErrorPortn=_Pm1004CntupRaRemCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,16,1,3),_Pm1004CntupRaRemCntErrorPortn_Type())
pm1004CntupRaRemCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaRemCntErrorPortn.setStatus(_A)
_Pm1004CntupRaRemCntOverloadPortn_Type=EkiOnOff
_Pm1004CntupRaRemCntOverloadPortn_Object=MibTableColumn
pm1004CntupRaRemCntOverloadPortn=_Pm1004CntupRaRemCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,16,1,4),_Pm1004CntupRaRemCntOverloadPortn_Type())
pm1004CntupRaRemCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaRemCntOverloadPortn.setStatus(_A)
_Pm1004CntupRaInsCntTable_Object=MibTable
pm1004CntupRaInsCntTable=_Pm1004CntupRaInsCntTable_Object((1,3,6,1,4,1,20044,18,4,2,24))
if mibBuilder.loadTexts:pm1004CntupRaInsCntTable.setStatus(_A)
_Pm1004CntupRaInsCntEntry_Object=MibTableRow
pm1004CntupRaInsCntEntry=_Pm1004CntupRaInsCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,24,1))
pm1004CntupRaInsCntEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm1004CntupRaInsCntEntry.setStatus(_A)
class _Pm1004CntupRaInsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntupRaInsCntIndex_Type.__name__=_D
_Pm1004CntupRaInsCntIndex_Object=MibTableColumn
pm1004CntupRaInsCntIndex=_Pm1004CntupRaInsCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,24,1,1),_Pm1004CntupRaInsCntIndex_Type())
pm1004CntupRaInsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaInsCntIndex.setStatus(_A)
_Pm1004CntupRaInsCntValuePortn_Type=Counter32
_Pm1004CntupRaInsCntValuePortn_Object=MibTableColumn
pm1004CntupRaInsCntValuePortn=_Pm1004CntupRaInsCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,24,1,2),_Pm1004CntupRaInsCntValuePortn_Type())
pm1004CntupRaInsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaInsCntValuePortn.setStatus(_A)
_Pm1004CntupRaInsCntErrorPortn_Type=EkiOnOff
_Pm1004CntupRaInsCntErrorPortn_Object=MibTableColumn
pm1004CntupRaInsCntErrorPortn=_Pm1004CntupRaInsCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,24,1,3),_Pm1004CntupRaInsCntErrorPortn_Type())
pm1004CntupRaInsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaInsCntErrorPortn.setStatus(_A)
_Pm1004CntupRaInsCntOverloadPortn_Type=EkiOnOff
_Pm1004CntupRaInsCntOverloadPortn_Object=MibTableColumn
pm1004CntupRaInsCntOverloadPortn=_Pm1004CntupRaInsCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,24,1,4),_Pm1004CntupRaInsCntOverloadPortn_Type())
pm1004CntupRaInsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRaInsCntOverloadPortn.setStatus(_A)
_Pm1004CntupRdErrCntTable_Object=MibTable
pm1004CntupRdErrCntTable=_Pm1004CntupRdErrCntTable_Object((1,3,6,1,4,1,20044,18,4,2,32))
if mibBuilder.loadTexts:pm1004CntupRdErrCntTable.setStatus(_A)
_Pm1004CntupRdErrCntEntry_Object=MibTableRow
pm1004CntupRdErrCntEntry=_Pm1004CntupRdErrCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,32,1))
pm1004CntupRdErrCntEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pm1004CntupRdErrCntEntry.setStatus(_A)
class _Pm1004CntupRdErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntupRdErrCntIndex_Type.__name__=_D
_Pm1004CntupRdErrCntIndex_Object=MibTableColumn
pm1004CntupRdErrCntIndex=_Pm1004CntupRdErrCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,32,1,1),_Pm1004CntupRdErrCntIndex_Type())
pm1004CntupRdErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRdErrCntIndex.setStatus(_A)
_Pm1004CntupRdErrCntValuePortn_Type=Counter32
_Pm1004CntupRdErrCntValuePortn_Object=MibTableColumn
pm1004CntupRdErrCntValuePortn=_Pm1004CntupRdErrCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,32,1,2),_Pm1004CntupRdErrCntValuePortn_Type())
pm1004CntupRdErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRdErrCntValuePortn.setStatus(_A)
_Pm1004CntupRdErrCntErrorPortn_Type=EkiOnOff
_Pm1004CntupRdErrCntErrorPortn_Object=MibTableColumn
pm1004CntupRdErrCntErrorPortn=_Pm1004CntupRdErrCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,32,1,3),_Pm1004CntupRdErrCntErrorPortn_Type())
pm1004CntupRdErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRdErrCntErrorPortn.setStatus(_A)
_Pm1004CntupRdErrCntOverloadPortn_Type=EkiOnOff
_Pm1004CntupRdErrCntOverloadPortn_Object=MibTableColumn
pm1004CntupRdErrCntOverloadPortn=_Pm1004CntupRdErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,32,1,4),_Pm1004CntupRdErrCntOverloadPortn_Type())
pm1004CntupRdErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupRdErrCntOverloadPortn.setStatus(_A)
_Pm1004CntupTimCntTable_Object=MibTable
pm1004CntupTimCntTable=_Pm1004CntupTimCntTable_Object((1,3,6,1,4,1,20044,18,4,2,40))
if mibBuilder.loadTexts:pm1004CntupTimCntTable.setStatus(_A)
_Pm1004CntupTimCntEntry_Object=MibTableRow
pm1004CntupTimCntEntry=_Pm1004CntupTimCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,40,1))
pm1004CntupTimCntEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pm1004CntupTimCntEntry.setStatus(_A)
class _Pm1004CntupTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntupTimCntIndex_Type.__name__=_D
_Pm1004CntupTimCntIndex_Object=MibTableColumn
pm1004CntupTimCntIndex=_Pm1004CntupTimCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,40,1,1),_Pm1004CntupTimCntIndex_Type())
pm1004CntupTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupTimCntIndex.setStatus(_A)
_Pm1004CntupTimCntValuePortn_Type=Counter32
_Pm1004CntupTimCntValuePortn_Object=MibTableColumn
pm1004CntupTimCntValuePortn=_Pm1004CntupTimCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,40,1,2),_Pm1004CntupTimCntValuePortn_Type())
pm1004CntupTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupTimCntValuePortn.setStatus(_A)
_Pm1004CntupTimCntErrorPortn_Type=EkiOnOff
_Pm1004CntupTimCntErrorPortn_Object=MibTableColumn
pm1004CntupTimCntErrorPortn=_Pm1004CntupTimCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,40,1,3),_Pm1004CntupTimCntErrorPortn_Type())
pm1004CntupTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupTimCntErrorPortn.setStatus(_A)
_Pm1004CntupTimCntOverloadPortn_Type=EkiOnOff
_Pm1004CntupTimCntOverloadPortn_Object=MibTableColumn
pm1004CntupTimCntOverloadPortn=_Pm1004CntupTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,40,1,4),_Pm1004CntupTimCntOverloadPortn_Type())
pm1004CntupTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupTimCntOverloadPortn.setStatus(_A)
_Pm1004CntupCvErrCntTable_Object=MibTable
pm1004CntupCvErrCntTable=_Pm1004CntupCvErrCntTable_Object((1,3,6,1,4,1,20044,18,4,2,48))
if mibBuilder.loadTexts:pm1004CntupCvErrCntTable.setStatus(_A)
_Pm1004CntupCvErrCntEntry_Object=MibTableRow
pm1004CntupCvErrCntEntry=_Pm1004CntupCvErrCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,48,1))
pm1004CntupCvErrCntEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pm1004CntupCvErrCntEntry.setStatus(_A)
class _Pm1004CntupCvErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntupCvErrCntIndex_Type.__name__=_D
_Pm1004CntupCvErrCntIndex_Object=MibTableColumn
pm1004CntupCvErrCntIndex=_Pm1004CntupCvErrCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,48,1,1),_Pm1004CntupCvErrCntIndex_Type())
pm1004CntupCvErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupCvErrCntIndex.setStatus(_A)
_Pm1004CntupCvErrCntValuePortn_Type=Counter32
_Pm1004CntupCvErrCntValuePortn_Object=MibTableColumn
pm1004CntupCvErrCntValuePortn=_Pm1004CntupCvErrCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,48,1,2),_Pm1004CntupCvErrCntValuePortn_Type())
pm1004CntupCvErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupCvErrCntValuePortn.setStatus(_A)
_Pm1004CntupCvErrCntErrorPortn_Type=EkiOnOff
_Pm1004CntupCvErrCntErrorPortn_Object=MibTableColumn
pm1004CntupCvErrCntErrorPortn=_Pm1004CntupCvErrCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,48,1,3),_Pm1004CntupCvErrCntErrorPortn_Type())
pm1004CntupCvErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupCvErrCntErrorPortn.setStatus(_A)
_Pm1004CntupCvErrCntOverloadPortn_Type=EkiOnOff
_Pm1004CntupCvErrCntOverloadPortn_Object=MibTableColumn
pm1004CntupCvErrCntOverloadPortn=_Pm1004CntupCvErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,48,1,4),_Pm1004CntupCvErrCntOverloadPortn_Type())
pm1004CntupCvErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntupCvErrCntOverloadPortn.setStatus(_A)
_Pm1004CntdwCbipCntTable_Object=MibTable
pm1004CntdwCbipCntTable=_Pm1004CntdwCbipCntTable_Object((1,3,6,1,4,1,20044,18,4,2,64))
if mibBuilder.loadTexts:pm1004CntdwCbipCntTable.setStatus(_A)
_Pm1004CntdwCbipCntEntry_Object=MibTableRow
pm1004CntdwCbipCntEntry=_Pm1004CntdwCbipCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,64,1))
pm1004CntdwCbipCntEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pm1004CntdwCbipCntEntry.setStatus(_A)
class _Pm1004CntdwCbipCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntdwCbipCntIndex_Type.__name__=_D
_Pm1004CntdwCbipCntIndex_Object=MibTableColumn
pm1004CntdwCbipCntIndex=_Pm1004CntdwCbipCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,64,1,1),_Pm1004CntdwCbipCntIndex_Type())
pm1004CntdwCbipCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwCbipCntIndex.setStatus(_A)
_Pm1004CntdwCbipCntValuePortn_Type=Counter32
_Pm1004CntdwCbipCntValuePortn_Object=MibTableColumn
pm1004CntdwCbipCntValuePortn=_Pm1004CntdwCbipCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,64,1,2),_Pm1004CntdwCbipCntValuePortn_Type())
pm1004CntdwCbipCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwCbipCntValuePortn.setStatus(_A)
_Pm1004CntdwCbipCntErrorPortn_Type=EkiOnOff
_Pm1004CntdwCbipCntErrorPortn_Object=MibTableColumn
pm1004CntdwCbipCntErrorPortn=_Pm1004CntdwCbipCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,64,1,3),_Pm1004CntdwCbipCntErrorPortn_Type())
pm1004CntdwCbipCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwCbipCntErrorPortn.setStatus(_A)
_Pm1004CntdwCbipCntOverloadPortn_Type=EkiOnOff
_Pm1004CntdwCbipCntOverloadPortn_Object=MibTableColumn
pm1004CntdwCbipCntOverloadPortn=_Pm1004CntdwCbipCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,64,1,4),_Pm1004CntdwCbipCntOverloadPortn_Type())
pm1004CntdwCbipCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwCbipCntOverloadPortn.setStatus(_A)
_Pm1004CntdwTimCntTable_Object=MibTable
pm1004CntdwTimCntTable=_Pm1004CntdwTimCntTable_Object((1,3,6,1,4,1,20044,18,4,2,72))
if mibBuilder.loadTexts:pm1004CntdwTimCntTable.setStatus(_A)
_Pm1004CntdwTimCntEntry_Object=MibTableRow
pm1004CntdwTimCntEntry=_Pm1004CntdwTimCntEntry_Object((1,3,6,1,4,1,20044,18,4,2,72,1))
pm1004CntdwTimCntEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pm1004CntdwTimCntEntry.setStatus(_A)
class _Pm1004CntdwTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntdwTimCntIndex_Type.__name__=_D
_Pm1004CntdwTimCntIndex_Object=MibTableColumn
pm1004CntdwTimCntIndex=_Pm1004CntdwTimCntIndex_Object((1,3,6,1,4,1,20044,18,4,2,72,1,1),_Pm1004CntdwTimCntIndex_Type())
pm1004CntdwTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwTimCntIndex.setStatus(_A)
_Pm1004CntdwTimCntValuePortn_Type=Counter32
_Pm1004CntdwTimCntValuePortn_Object=MibTableColumn
pm1004CntdwTimCntValuePortn=_Pm1004CntdwTimCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,2,72,1,2),_Pm1004CntdwTimCntValuePortn_Type())
pm1004CntdwTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwTimCntValuePortn.setStatus(_A)
_Pm1004CntdwTimCntErrorPortn_Type=EkiOnOff
_Pm1004CntdwTimCntErrorPortn_Object=MibTableColumn
pm1004CntdwTimCntErrorPortn=_Pm1004CntdwTimCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,2,72,1,3),_Pm1004CntdwTimCntErrorPortn_Type())
pm1004CntdwTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwTimCntErrorPortn.setStatus(_A)
_Pm1004CntdwTimCntOverloadPortn_Type=EkiOnOff
_Pm1004CntdwTimCntOverloadPortn_Object=MibTableColumn
pm1004CntdwTimCntOverloadPortn=_Pm1004CntdwTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,2,72,1,4),_Pm1004CntdwTimCntOverloadPortn_Type())
pm1004CntdwTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdwTimCntOverloadPortn.setStatus(_A)
_Pm1004CntLine_ObjectIdentity=ObjectIdentity
pm1004CntLine=_Pm1004CntLine_ObjectIdentity((1,3,6,1,4,1,20044,18,4,3))
_Pm1004CntdfrmB1ErrCntTable_Object=MibTable
pm1004CntdfrmB1ErrCntTable=_Pm1004CntdfrmB1ErrCntTable_Object((1,3,6,1,4,1,20044,18,4,3,152))
if mibBuilder.loadTexts:pm1004CntdfrmB1ErrCntTable.setStatus(_A)
_Pm1004CntdfrmB1ErrCntEntry_Object=MibTableRow
pm1004CntdfrmB1ErrCntEntry=_Pm1004CntdfrmB1ErrCntEntry_Object((1,3,6,1,4,1,20044,18,4,3,152,1))
pm1004CntdfrmB1ErrCntEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pm1004CntdfrmB1ErrCntEntry.setStatus(_A)
class _Pm1004CntdfrmB1ErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntdfrmB1ErrCntIndex_Type.__name__=_D
_Pm1004CntdfrmB1ErrCntIndex_Object=MibTableColumn
pm1004CntdfrmB1ErrCntIndex=_Pm1004CntdfrmB1ErrCntIndex_Object((1,3,6,1,4,1,20044,18,4,3,152,1,1),_Pm1004CntdfrmB1ErrCntIndex_Type())
pm1004CntdfrmB1ErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmB1ErrCntIndex.setStatus(_A)
_Pm1004CntdfrmB1ErrCntValuePortn_Type=Counter32
_Pm1004CntdfrmB1ErrCntValuePortn_Object=MibTableColumn
pm1004CntdfrmB1ErrCntValuePortn=_Pm1004CntdfrmB1ErrCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,3,152,1,2),_Pm1004CntdfrmB1ErrCntValuePortn_Type())
pm1004CntdfrmB1ErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmB1ErrCntValuePortn.setStatus(_A)
_Pm1004CntdfrmB1ErrCntErrorPortn_Type=EkiOnOff
_Pm1004CntdfrmB1ErrCntErrorPortn_Object=MibTableColumn
pm1004CntdfrmB1ErrCntErrorPortn=_Pm1004CntdfrmB1ErrCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,3,152,1,3),_Pm1004CntdfrmB1ErrCntErrorPortn_Type())
pm1004CntdfrmB1ErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmB1ErrCntErrorPortn.setStatus(_A)
_Pm1004CntdfrmB1ErrCntOverloadPortn_Type=EkiOnOff
_Pm1004CntdfrmB1ErrCntOverloadPortn_Object=MibTableColumn
pm1004CntdfrmB1ErrCntOverloadPortn=_Pm1004CntdfrmB1ErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,3,152,1,4),_Pm1004CntdfrmB1ErrCntOverloadPortn_Type())
pm1004CntdfrmB1ErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmB1ErrCntOverloadPortn.setStatus(_A)
_Pm1004CntdfrmTimCntTable_Object=MibTable
pm1004CntdfrmTimCntTable=_Pm1004CntdfrmTimCntTable_Object((1,3,6,1,4,1,20044,18,4,3,153))
if mibBuilder.loadTexts:pm1004CntdfrmTimCntTable.setStatus(_A)
_Pm1004CntdfrmTimCntEntry_Object=MibTableRow
pm1004CntdfrmTimCntEntry=_Pm1004CntdfrmTimCntEntry_Object((1,3,6,1,4,1,20044,18,4,3,153,1))
pm1004CntdfrmTimCntEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pm1004CntdfrmTimCntEntry.setStatus(_A)
class _Pm1004CntdfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntdfrmTimCntIndex_Type.__name__=_D
_Pm1004CntdfrmTimCntIndex_Object=MibTableColumn
pm1004CntdfrmTimCntIndex=_Pm1004CntdfrmTimCntIndex_Object((1,3,6,1,4,1,20044,18,4,3,153,1,1),_Pm1004CntdfrmTimCntIndex_Type())
pm1004CntdfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmTimCntIndex.setStatus(_A)
_Pm1004CntdfrmTimCntValuePortn_Type=Counter32
_Pm1004CntdfrmTimCntValuePortn_Object=MibTableColumn
pm1004CntdfrmTimCntValuePortn=_Pm1004CntdfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,3,153,1,2),_Pm1004CntdfrmTimCntValuePortn_Type())
pm1004CntdfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmTimCntValuePortn.setStatus(_A)
_Pm1004CntdfrmTimCntErrorPortn_Type=EkiOnOff
_Pm1004CntdfrmTimCntErrorPortn_Object=MibTableColumn
pm1004CntdfrmTimCntErrorPortn=_Pm1004CntdfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,3,153,1,3),_Pm1004CntdfrmTimCntErrorPortn_Type())
pm1004CntdfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmTimCntErrorPortn.setStatus(_A)
_Pm1004CntdfrmTimCntOverloadPortn_Type=EkiOnOff
_Pm1004CntdfrmTimCntOverloadPortn_Object=MibTableColumn
pm1004CntdfrmTimCntOverloadPortn=_Pm1004CntdfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,3,153,1,4),_Pm1004CntdfrmTimCntOverloadPortn_Type())
pm1004CntdfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmTimCntOverloadPortn.setStatus(_A)
_Pm1004CntdfrmPrimLineErrCntTable_Object=MibTable
pm1004CntdfrmPrimLineErrCntTable=_Pm1004CntdfrmPrimLineErrCntTable_Object((1,3,6,1,4,1,20044,18,4,3,154))
if mibBuilder.loadTexts:pm1004CntdfrmPrimLineErrCntTable.setStatus(_A)
_Pm1004CntdfrmPrimLineErrCntEntry_Object=MibTableRow
pm1004CntdfrmPrimLineErrCntEntry=_Pm1004CntdfrmPrimLineErrCntEntry_Object((1,3,6,1,4,1,20044,18,4,3,154,1))
pm1004CntdfrmPrimLineErrCntEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pm1004CntdfrmPrimLineErrCntEntry.setStatus(_A)
class _Pm1004CntdfrmPrimLineErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CntdfrmPrimLineErrCntIndex_Type.__name__=_D
_Pm1004CntdfrmPrimLineErrCntIndex_Object=MibTableColumn
pm1004CntdfrmPrimLineErrCntIndex=_Pm1004CntdfrmPrimLineErrCntIndex_Object((1,3,6,1,4,1,20044,18,4,3,154,1,1),_Pm1004CntdfrmPrimLineErrCntIndex_Type())
pm1004CntdfrmPrimLineErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmPrimLineErrCntIndex.setStatus(_A)
_Pm1004CntdfrmPrimLineErrCntValuePortn_Type=Counter32
_Pm1004CntdfrmPrimLineErrCntValuePortn_Object=MibTableColumn
pm1004CntdfrmPrimLineErrCntValuePortn=_Pm1004CntdfrmPrimLineErrCntValuePortn_Object((1,3,6,1,4,1,20044,18,4,3,154,1,2),_Pm1004CntdfrmPrimLineErrCntValuePortn_Type())
pm1004CntdfrmPrimLineErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmPrimLineErrCntValuePortn.setStatus(_A)
_Pm1004CntdfrmPrimLineErrCntErrorPortn_Type=EkiOnOff
_Pm1004CntdfrmPrimLineErrCntErrorPortn_Object=MibTableColumn
pm1004CntdfrmPrimLineErrCntErrorPortn=_Pm1004CntdfrmPrimLineErrCntErrorPortn_Object((1,3,6,1,4,1,20044,18,4,3,154,1,3),_Pm1004CntdfrmPrimLineErrCntErrorPortn_Type())
pm1004CntdfrmPrimLineErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmPrimLineErrCntErrorPortn.setStatus(_A)
_Pm1004CntdfrmPrimLineErrCntOverloadPortn_Type=EkiOnOff
_Pm1004CntdfrmPrimLineErrCntOverloadPortn_Object=MibTableColumn
pm1004CntdfrmPrimLineErrCntOverloadPortn=_Pm1004CntdfrmPrimLineErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,18,4,3,154,1,4),_Pm1004CntdfrmPrimLineErrCntOverloadPortn_Type())
pm1004CntdfrmPrimLineErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CntdfrmPrimLineErrCntOverloadPortn.setStatus(_A)
_Pm1004CntCountersReset_Type=EkiOnOff
_Pm1004CntCountersReset_Object=MibScalar
pm1004CntCountersReset=_Pm1004CntCountersReset_Object((1,3,6,1,4,1,20044,18,4,259),_Pm1004CntCountersReset_Type())
pm1004CntCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CntCountersReset.setStatus(_A)
_Pm1004CntCountersStop_Type=EkiOnOff
_Pm1004CntCountersStop_Object=MibScalar
pm1004CntCountersStop=_Pm1004CntCountersStop_Object((1,3,6,1,4,1,20044,18,4,260),_Pm1004CntCountersStop_Type())
pm1004CntCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CntCountersStop.setStatus(_A)
_Pm1004controlsWrite_ObjectIdentity=ObjectIdentity
pm1004controlsWrite=_Pm1004controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,18,6))
_Pm1004CtrlOther_ObjectIdentity=ObjectIdentity
pm1004CtrlOther=_Pm1004CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1))
_Pm1004CtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pm1004CtrlconfMgnt1=_Pm1004CtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,1))
_Pm1004CtrlConf1Load1_Type=EkiOnOff
_Pm1004CtrlConf1Load1_Object=MibScalar
pm1004CtrlConf1Load1=_Pm1004CtrlConf1Load1_Object((1,3,6,1,4,1,20044,18,6,1,1,1),_Pm1004CtrlConf1Load1_Type())
pm1004CtrlConf1Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlConf1Load1.setStatus(_A)
_Pm1004CtrlConf2Load1_Type=EkiOnOff
_Pm1004CtrlConf2Load1_Object=MibScalar
pm1004CtrlConf2Load1=_Pm1004CtrlConf2Load1_Object((1,3,6,1,4,1,20044,18,6,1,1,2),_Pm1004CtrlConf2Load1_Type())
pm1004CtrlConf2Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlConf2Load1.setStatus(_A)
_Pm1004CtrlConf2Flash1_Type=EkiOnOff
_Pm1004CtrlConf2Flash1_Object=MibScalar
pm1004CtrlConf2Flash1=_Pm1004CtrlConf2Flash1_Object((1,3,6,1,4,1,20044,18,6,1,1,10),_Pm1004CtrlConf2Flash1_Type())
pm1004CtrlConf2Flash1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlConf2Flash1.setStatus(_A)
_Pm1004CtrlConf2Clear1_Type=EkiOnOff
_Pm1004CtrlConf2Clear1_Object=MibScalar
pm1004CtrlConf2Clear1=_Pm1004CtrlConf2Clear1_Object((1,3,6,1,4,1,20044,18,6,1,1,14),_Pm1004CtrlConf2Clear1_Type())
pm1004CtrlConf2Clear1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlConf2Clear1.setStatus(_A)
_Pm1004Ctrlsynth4_ObjectIdentity=ObjectIdentity
pm1004Ctrlsynth4=_Pm1004Ctrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,4))
_Pm1004CtrlCorrelatOn_Type=EkiOnOff
_Pm1004CtrlCorrelatOn_Object=MibScalar
pm1004CtrlCorrelatOn=_Pm1004CtrlCorrelatOn_Object((1,3,6,1,4,1,20044,18,6,1,4,1),_Pm1004CtrlCorrelatOn_Type())
pm1004CtrlCorrelatOn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlCorrelatOn.setStatus(_A)
_Pm1004CtrlCorrelatOff_Type=EkiOnOff
_Pm1004CtrlCorrelatOff_Object=MibScalar
pm1004CtrlCorrelatOff=_Pm1004CtrlCorrelatOff_Object((1,3,6,1,4,1,20044,18,6,1,4,2),_Pm1004CtrlCorrelatOff_Type())
pm1004CtrlCorrelatOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlCorrelatOff.setStatus(_A)
_Pm1004CtrlswMgnt_ObjectIdentity=ObjectIdentity
pm1004CtrlswMgnt=_Pm1004CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,5))
_Pm1004CtrlColdReset_Type=EkiOnOff
_Pm1004CtrlColdReset_Object=MibScalar
pm1004CtrlColdReset=_Pm1004CtrlColdReset_Object((1,3,6,1,4,1,20044,18,6,1,5,2),_Pm1004CtrlColdReset_Type())
pm1004CtrlColdReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlColdReset.setStatus(_A)
_Pm1004CtrlWarmReset_Type=EkiOnOff
_Pm1004CtrlWarmReset_Object=MibScalar
pm1004CtrlWarmReset=_Pm1004CtrlWarmReset_Object((1,3,6,1,4,1,20044,18,6,1,5,3),_Pm1004CtrlWarmReset_Type())
pm1004CtrlWarmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlWarmReset.setStatus(_A)
_Pm1004CtrlLoadSwBank1_Type=EkiOnOff
_Pm1004CtrlLoadSwBank1_Object=MibScalar
pm1004CtrlLoadSwBank1=_Pm1004CtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,18,6,1,5,5),_Pm1004CtrlLoadSwBank1_Type())
pm1004CtrlLoadSwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLoadSwBank1.setStatus(_A)
_Pm1004CtrlLoadSwBank2_Type=EkiOnOff
_Pm1004CtrlLoadSwBank2_Object=MibScalar
pm1004CtrlLoadSwBank2=_Pm1004CtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,18,6,1,5,6),_Pm1004CtrlLoadSwBank2_Type())
pm1004CtrlLoadSwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLoadSwBank2.setStatus(_A)
_Pm1004CtrlgwMgnt_ObjectIdentity=ObjectIdentity
pm1004CtrlgwMgnt=_Pm1004CtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,6))
_Pm1004CtrlCurrentGwReset_Type=EkiOnOff
_Pm1004CtrlCurrentGwReset_Object=MibScalar
pm1004CtrlCurrentGwReset=_Pm1004CtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,18,6,1,6,1),_Pm1004CtrlCurrentGwReset_Type())
pm1004CtrlCurrentGwReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlCurrentGwReset.setStatus(_A)
_Pm1004CtrlLoadGwBank1_Type=EkiOnOff
_Pm1004CtrlLoadGwBank1_Object=MibScalar
pm1004CtrlLoadGwBank1=_Pm1004CtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,18,6,1,6,5),_Pm1004CtrlLoadGwBank1_Type())
pm1004CtrlLoadGwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLoadGwBank1.setStatus(_A)
_Pm1004CtrlLoadGwBank2_Type=EkiOnOff
_Pm1004CtrlLoadGwBank2_Object=MibScalar
pm1004CtrlLoadGwBank2=_Pm1004CtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,18,6,1,6,6),_Pm1004CtrlLoadGwBank2_Type())
pm1004CtrlLoadGwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLoadGwBank2.setStatus(_A)
_Pm1004CtrlLoadGwBank3_Type=EkiOnOff
_Pm1004CtrlLoadGwBank3_Object=MibScalar
pm1004CtrlLoadGwBank3=_Pm1004CtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,18,6,1,6,7),_Pm1004CtrlLoadGwBank3_Type())
pm1004CtrlLoadGwBank3.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLoadGwBank3.setStatus(_A)
_Pm1004CtrlLoadGwBank4_Type=EkiOnOff
_Pm1004CtrlLoadGwBank4_Object=MibScalar
pm1004CtrlLoadGwBank4=_Pm1004CtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,18,6,1,6,8),_Pm1004CtrlLoadGwBank4_Type())
pm1004CtrlLoadGwBank4.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLoadGwBank4.setStatus(_A)
_Pm1004CtrlledTest_ObjectIdentity=ObjectIdentity
pm1004CtrlledTest=_Pm1004CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,192))
_Pm1004CtrlGreenLed_Type=EkiOnOff
_Pm1004CtrlGreenLed_Object=MibScalar
pm1004CtrlGreenLed=_Pm1004CtrlGreenLed_Object((1,3,6,1,4,1,20044,18,6,1,192,1),_Pm1004CtrlGreenLed_Type())
pm1004CtrlGreenLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlGreenLed.setStatus(_A)
_Pm1004CtrlRedLed_Type=EkiOnOff
_Pm1004CtrlRedLed_Object=MibScalar
pm1004CtrlRedLed=_Pm1004CtrlRedLed_Object((1,3,6,1,4,1,20044,18,6,1,192,2),_Pm1004CtrlRedLed_Type())
pm1004CtrlRedLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlRedLed.setStatus(_A)
_Pm1004CtrlLedOff_Type=EkiOnOff
_Pm1004CtrlLedOff_Object=MibScalar
pm1004CtrlLedOff=_Pm1004CtrlLedOff_Object((1,3,6,1,4,1,20044,18,6,1,192,3),_Pm1004CtrlLedOff_Type())
pm1004CtrlLedOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLedOff.setStatus(_A)
_Pm1004CtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm1004CtrlmoduleOosMode=_Pm1004CtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,193))
_Pm1004CtrlModuleOosMode_Type=EkiOnOff
_Pm1004CtrlModuleOosMode_Object=MibScalar
pm1004CtrlModuleOosMode=_Pm1004CtrlModuleOosMode_Object((1,3,6,1,4,1,20044,18,6,1,193,1),_Pm1004CtrlModuleOosMode_Type())
pm1004CtrlModuleOosMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlModuleOosMode.setStatus(_A)
_Pm1004CtrlmaintenanceMode_ObjectIdentity=ObjectIdentity
pm1004CtrlmaintenanceMode=_Pm1004CtrlmaintenanceMode_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,197))
_Pm1004CtrlMaintenanceMode_Type=EkiOnOff
_Pm1004CtrlMaintenanceMode_Object=MibScalar
pm1004CtrlMaintenanceMode=_Pm1004CtrlMaintenanceMode_Object((1,3,6,1,4,1,20044,18,6,1,197,1),_Pm1004CtrlMaintenanceMode_Type())
pm1004CtrlMaintenanceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlMaintenanceMode.setStatus(_A)
_Pm1004CtrldccEnable_ObjectIdentity=ObjectIdentity
pm1004CtrldccEnable=_Pm1004CtrldccEnable_ObjectIdentity((1,3,6,1,4,1,20044,18,6,1,198))
_Pm1004CtrlDccEnable_Type=EkiOnOff
_Pm1004CtrlDccEnable_Object=MibScalar
pm1004CtrlDccEnable=_Pm1004CtrlDccEnable_Object((1,3,6,1,4,1,20044,18,6,1,198,1),_Pm1004CtrlDccEnable_Type())
pm1004CtrlDccEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlDccEnable.setStatus(_A)
_Pm1004CtrlClient_ObjectIdentity=ObjectIdentity
pm1004CtrlClient=_Pm1004CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,18,6,2))
_Pm1004CtrlaccessLoopTable_Object=MibTable
pm1004CtrlaccessLoopTable=_Pm1004CtrlaccessLoopTable_Object((1,3,6,1,4,1,20044,18,6,2,16))
if mibBuilder.loadTexts:pm1004CtrlaccessLoopTable.setStatus(_A)
_Pm1004CtrlaccessLoopEntry_Object=MibTableRow
pm1004CtrlaccessLoopEntry=_Pm1004CtrlaccessLoopEntry_Object((1,3,6,1,4,1,20044,18,6,2,16,1))
pm1004CtrlaccessLoopEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pm1004CtrlaccessLoopEntry.setStatus(_A)
class _Pm1004CtrlaccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlaccessLoopIndex_Type.__name__=_D
_Pm1004CtrlaccessLoopIndex_Object=MibTableColumn
pm1004CtrlaccessLoopIndex=_Pm1004CtrlaccessLoopIndex_Object((1,3,6,1,4,1,20044,18,6,2,16,1,1),_Pm1004CtrlaccessLoopIndex_Type())
pm1004CtrlaccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlaccessLoopIndex.setStatus(_A)
_Pm1004CtrlaccessLoopPortn_Type=EkiState
_Pm1004CtrlaccessLoopPortn_Object=MibTableColumn
pm1004CtrlaccessLoopPortn=_Pm1004CtrlaccessLoopPortn_Object((1,3,6,1,4,1,20044,18,6,2,16,1,2),_Pm1004CtrlaccessLoopPortn_Type())
pm1004CtrlaccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlaccessLoopPortn.setStatus(_A)
_Pm1004CtrlportOosModeTable_Object=MibTable
pm1004CtrlportOosModeTable=_Pm1004CtrlportOosModeTable_Object((1,3,6,1,4,1,20044,18,6,2,18))
if mibBuilder.loadTexts:pm1004CtrlportOosModeTable.setStatus(_A)
_Pm1004CtrlportOosModeEntry_Object=MibTableRow
pm1004CtrlportOosModeEntry=_Pm1004CtrlportOosModeEntry_Object((1,3,6,1,4,1,20044,18,6,2,18,1))
pm1004CtrlportOosModeEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pm1004CtrlportOosModeEntry.setStatus(_A)
class _Pm1004CtrlportOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlportOosModeIndex_Type.__name__=_D
_Pm1004CtrlportOosModeIndex_Object=MibTableColumn
pm1004CtrlportOosModeIndex=_Pm1004CtrlportOosModeIndex_Object((1,3,6,1,4,1,20044,18,6,2,18,1,1),_Pm1004CtrlportOosModeIndex_Type())
pm1004CtrlportOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlportOosModeIndex.setStatus(_A)
_Pm1004CtrlportOosModePortn_Type=EkiState
_Pm1004CtrlportOosModePortn_Object=MibTableColumn
pm1004CtrlportOosModePortn=_Pm1004CtrlportOosModePortn_Object((1,3,6,1,4,1,20044,18,6,2,18,1,2),_Pm1004CtrlportOosModePortn_Type())
pm1004CtrlportOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlportOosModePortn.setStatus(_A)
_Pm1004CtrlsfpOnCtrlTable_Object=MibTable
pm1004CtrlsfpOnCtrlTable=_Pm1004CtrlsfpOnCtrlTable_Object((1,3,6,1,4,1,20044,18,6,2,19))
if mibBuilder.loadTexts:pm1004CtrlsfpOnCtrlTable.setStatus(_A)
_Pm1004CtrlsfpOnCtrlEntry_Object=MibTableRow
pm1004CtrlsfpOnCtrlEntry=_Pm1004CtrlsfpOnCtrlEntry_Object((1,3,6,1,4,1,20044,18,6,2,19,1))
pm1004CtrlsfpOnCtrlEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pm1004CtrlsfpOnCtrlEntry.setStatus(_A)
class _Pm1004CtrlsfpOnCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlsfpOnCtrlIndex_Type.__name__=_D
_Pm1004CtrlsfpOnCtrlIndex_Object=MibTableColumn
pm1004CtrlsfpOnCtrlIndex=_Pm1004CtrlsfpOnCtrlIndex_Object((1,3,6,1,4,1,20044,18,6,2,19,1,1),_Pm1004CtrlsfpOnCtrlIndex_Type())
pm1004CtrlsfpOnCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlsfpOnCtrlIndex.setStatus(_A)
_Pm1004CtrlsfpOnCtrlPortn_Type=EkiState
_Pm1004CtrlsfpOnCtrlPortn_Object=MibTableColumn
pm1004CtrlsfpOnCtrlPortn=_Pm1004CtrlsfpOnCtrlPortn_Object((1,3,6,1,4,1,20044,18,6,2,19,1,2),_Pm1004CtrlsfpOnCtrlPortn_Type())
pm1004CtrlsfpOnCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlsfpOnCtrlPortn.setStatus(_A)
_Pm1004CtrlsfpOffCtrlTable_Object=MibTable
pm1004CtrlsfpOffCtrlTable=_Pm1004CtrlsfpOffCtrlTable_Object((1,3,6,1,4,1,20044,18,6,2,20))
if mibBuilder.loadTexts:pm1004CtrlsfpOffCtrlTable.setStatus(_A)
_Pm1004CtrlsfpOffCtrlEntry_Object=MibTableRow
pm1004CtrlsfpOffCtrlEntry=_Pm1004CtrlsfpOffCtrlEntry_Object((1,3,6,1,4,1,20044,18,6,2,20,1))
pm1004CtrlsfpOffCtrlEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pm1004CtrlsfpOffCtrlEntry.setStatus(_A)
class _Pm1004CtrlsfpOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlsfpOffCtrlIndex_Type.__name__=_D
_Pm1004CtrlsfpOffCtrlIndex_Object=MibTableColumn
pm1004CtrlsfpOffCtrlIndex=_Pm1004CtrlsfpOffCtrlIndex_Object((1,3,6,1,4,1,20044,18,6,2,20,1,1),_Pm1004CtrlsfpOffCtrlIndex_Type())
pm1004CtrlsfpOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlsfpOffCtrlIndex.setStatus(_A)
_Pm1004CtrlsfpOffCtrlPortn_Type=EkiState
_Pm1004CtrlsfpOffCtrlPortn_Object=MibTableColumn
pm1004CtrlsfpOffCtrlPortn=_Pm1004CtrlsfpOffCtrlPortn_Object((1,3,6,1,4,1,20044,18,6,2,20,1,2),_Pm1004CtrlsfpOffCtrlPortn_Type())
pm1004CtrlsfpOffCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlsfpOffCtrlPortn.setStatus(_A)
_Pm1004CtrlcsfUpInsTable_Object=MibTable
pm1004CtrlcsfUpInsTable=_Pm1004CtrlcsfUpInsTable_Object((1,3,6,1,4,1,20044,18,6,2,21))
if mibBuilder.loadTexts:pm1004CtrlcsfUpInsTable.setStatus(_A)
_Pm1004CtrlcsfUpInsEntry_Object=MibTableRow
pm1004CtrlcsfUpInsEntry=_Pm1004CtrlcsfUpInsEntry_Object((1,3,6,1,4,1,20044,18,6,2,21,1))
pm1004CtrlcsfUpInsEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pm1004CtrlcsfUpInsEntry.setStatus(_A)
class _Pm1004CtrlcsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlcsfUpInsIndex_Type.__name__=_D
_Pm1004CtrlcsfUpInsIndex_Object=MibTableColumn
pm1004CtrlcsfUpInsIndex=_Pm1004CtrlcsfUpInsIndex_Object((1,3,6,1,4,1,20044,18,6,2,21,1,1),_Pm1004CtrlcsfUpInsIndex_Type())
pm1004CtrlcsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlcsfUpInsIndex.setStatus(_A)
_Pm1004CtrlcsfUpInsPortn_Type=EkiState
_Pm1004CtrlcsfUpInsPortn_Object=MibTableColumn
pm1004CtrlcsfUpInsPortn=_Pm1004CtrlcsfUpInsPortn_Object((1,3,6,1,4,1,20044,18,6,2,21,1,2),_Pm1004CtrlcsfUpInsPortn_Type())
pm1004CtrlcsfUpInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlcsfUpInsPortn.setStatus(_A)
_Pm1004CtrlcaisDwInsTable_Object=MibTable
pm1004CtrlcaisDwInsTable=_Pm1004CtrlcaisDwInsTable_Object((1,3,6,1,4,1,20044,18,6,2,22))
if mibBuilder.loadTexts:pm1004CtrlcaisDwInsTable.setStatus(_A)
_Pm1004CtrlcaisDwInsEntry_Object=MibTableRow
pm1004CtrlcaisDwInsEntry=_Pm1004CtrlcaisDwInsEntry_Object((1,3,6,1,4,1,20044,18,6,2,22,1))
pm1004CtrlcaisDwInsEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pm1004CtrlcaisDwInsEntry.setStatus(_A)
class _Pm1004CtrlcaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlcaisDwInsIndex_Type.__name__=_D
_Pm1004CtrlcaisDwInsIndex_Object=MibTableColumn
pm1004CtrlcaisDwInsIndex=_Pm1004CtrlcaisDwInsIndex_Object((1,3,6,1,4,1,20044,18,6,2,22,1,1),_Pm1004CtrlcaisDwInsIndex_Type())
pm1004CtrlcaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlcaisDwInsIndex.setStatus(_A)
_Pm1004CtrlcaisDwInsPortn_Type=EkiState
_Pm1004CtrlcaisDwInsPortn_Object=MibTableColumn
pm1004CtrlcaisDwInsPortn=_Pm1004CtrlcaisDwInsPortn_Object((1,3,6,1,4,1,20044,18,6,2,22,1,2),_Pm1004CtrlcaisDwInsPortn_Type())
pm1004CtrlcaisDwInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlcaisDwInsPortn.setStatus(_A)
_Pm1004CtrlclientAccessTermLoopTable_Object=MibTable
pm1004CtrlclientAccessTermLoopTable=_Pm1004CtrlclientAccessTermLoopTable_Object((1,3,6,1,4,1,20044,18,6,2,26))
if mibBuilder.loadTexts:pm1004CtrlclientAccessTermLoopTable.setStatus(_A)
_Pm1004CtrlclientAccessTermLoopEntry_Object=MibTableRow
pm1004CtrlclientAccessTermLoopEntry=_Pm1004CtrlclientAccessTermLoopEntry_Object((1,3,6,1,4,1,20044,18,6,2,26,1))
pm1004CtrlclientAccessTermLoopEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pm1004CtrlclientAccessTermLoopEntry.setStatus(_A)
class _Pm1004CtrlclientAccessTermLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlclientAccessTermLoopIndex_Type.__name__=_D
_Pm1004CtrlclientAccessTermLoopIndex_Object=MibTableColumn
pm1004CtrlclientAccessTermLoopIndex=_Pm1004CtrlclientAccessTermLoopIndex_Object((1,3,6,1,4,1,20044,18,6,2,26,1,1),_Pm1004CtrlclientAccessTermLoopIndex_Type())
pm1004CtrlclientAccessTermLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlclientAccessTermLoopIndex.setStatus(_A)
_Pm1004CtrlclientAccessTermLoopPortn_Type=EkiState
_Pm1004CtrlclientAccessTermLoopPortn_Object=MibTableColumn
pm1004CtrlclientAccessTermLoopPortn=_Pm1004CtrlclientAccessTermLoopPortn_Object((1,3,6,1,4,1,20044,18,6,2,26,1,2),_Pm1004CtrlclientAccessTermLoopPortn_Type())
pm1004CtrlclientAccessTermLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlclientAccessTermLoopPortn.setStatus(_A)
_Pm1004CtrlresetCount15PortTable_Object=MibTable
pm1004CtrlresetCount15PortTable=_Pm1004CtrlresetCount15PortTable_Object((1,3,6,1,4,1,20044,18,6,2,35))
if mibBuilder.loadTexts:pm1004CtrlresetCount15PortTable.setStatus(_A)
_Pm1004CtrlresetCount15PortEntry_Object=MibTableRow
pm1004CtrlresetCount15PortEntry=_Pm1004CtrlresetCount15PortEntry_Object((1,3,6,1,4,1,20044,18,6,2,35,1))
pm1004CtrlresetCount15PortEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pm1004CtrlresetCount15PortEntry.setStatus(_A)
class _Pm1004CtrlresetCount15PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlresetCount15PortIndex_Type.__name__=_D
_Pm1004CtrlresetCount15PortIndex_Object=MibTableColumn
pm1004CtrlresetCount15PortIndex=_Pm1004CtrlresetCount15PortIndex_Object((1,3,6,1,4,1,20044,18,6,2,35,1,1),_Pm1004CtrlresetCount15PortIndex_Type())
pm1004CtrlresetCount15PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlresetCount15PortIndex.setStatus(_A)
_Pm1004CtrlclientResetAllPerfCount15Portn_Type=EkiState
_Pm1004CtrlclientResetAllPerfCount15Portn_Object=MibTableColumn
pm1004CtrlclientResetAllPerfCount15Portn=_Pm1004CtrlclientResetAllPerfCount15Portn_Object((1,3,6,1,4,1,20044,18,6,2,35,1,2),_Pm1004CtrlclientResetAllPerfCount15Portn_Type())
pm1004CtrlclientResetAllPerfCount15Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlclientResetAllPerfCount15Portn.setStatus(_A)
_Pm1004CtrlresetCount24PortTable_Object=MibTable
pm1004CtrlresetCount24PortTable=_Pm1004CtrlresetCount24PortTable_Object((1,3,6,1,4,1,20044,18,6,2,36))
if mibBuilder.loadTexts:pm1004CtrlresetCount24PortTable.setStatus(_A)
_Pm1004CtrlresetCount24PortEntry_Object=MibTableRow
pm1004CtrlresetCount24PortEntry=_Pm1004CtrlresetCount24PortEntry_Object((1,3,6,1,4,1,20044,18,6,2,36,1))
pm1004CtrlresetCount24PortEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pm1004CtrlresetCount24PortEntry.setStatus(_A)
class _Pm1004CtrlresetCount24PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlresetCount24PortIndex_Type.__name__=_D
_Pm1004CtrlresetCount24PortIndex_Object=MibTableColumn
pm1004CtrlresetCount24PortIndex=_Pm1004CtrlresetCount24PortIndex_Object((1,3,6,1,4,1,20044,18,6,2,36,1,1),_Pm1004CtrlresetCount24PortIndex_Type())
pm1004CtrlresetCount24PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlresetCount24PortIndex.setStatus(_A)
_Pm1004CtrlclientResetAllPerfCount24Portn_Type=EkiState
_Pm1004CtrlclientResetAllPerfCount24Portn_Object=MibTableColumn
pm1004CtrlclientResetAllPerfCount24Portn=_Pm1004CtrlclientResetAllPerfCount24Portn_Object((1,3,6,1,4,1,20044,18,6,2,36,1,2),_Pm1004CtrlclientResetAllPerfCount24Portn_Type())
pm1004CtrlclientResetAllPerfCount24Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlclientResetAllPerfCount24Portn.setStatus(_A)
_Pm1004CtrlprotocolTable_Object=MibTable
pm1004CtrlprotocolTable=_Pm1004CtrlprotocolTable_Object((1,3,6,1,4,1,20044,18,6,2,51))
if mibBuilder.loadTexts:pm1004CtrlprotocolTable.setStatus(_A)
_Pm1004CtrlprotocolEntry_Object=MibTableRow
pm1004CtrlprotocolEntry=_Pm1004CtrlprotocolEntry_Object((1,3,6,1,4,1,20044,18,6,2,51,1))
pm1004CtrlprotocolEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pm1004CtrlprotocolEntry.setStatus(_A)
class _Pm1004CtrlprotocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlprotocolIndex_Type.__name__=_D
_Pm1004CtrlprotocolIndex_Object=MibTableColumn
pm1004CtrlprotocolIndex=_Pm1004CtrlprotocolIndex_Object((1,3,6,1,4,1,20044,18,6,2,51,1,1),_Pm1004CtrlprotocolIndex_Type())
pm1004CtrlprotocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlprotocolIndex.setStatus(_A)
_Pm1004CtrlprotocolPortn_Type=EkiProtocol
_Pm1004CtrlprotocolPortn_Object=MibTableColumn
pm1004CtrlprotocolPortn=_Pm1004CtrlprotocolPortn_Object((1,3,6,1,4,1,20044,18,6,2,51,1,2),_Pm1004CtrlprotocolPortn_Type())
pm1004CtrlprotocolPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlprotocolPortn.setStatus(_A)
_Pm1004CtrlLine_ObjectIdentity=ObjectIdentity
pm1004CtrlLine=_Pm1004CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,18,6,3))
_Pm1004CtrlcommAccessLoop_ObjectIdentity=ObjectIdentity
pm1004CtrlcommAccessLoop=_Pm1004CtrlcommAccessLoop_ObjectIdentity((1,3,6,1,4,1,20044,18,6,3,64))
_Pm1004CtrlCommAccessloop_Type=EkiOnOff
_Pm1004CtrlCommAccessloop_Object=MibScalar
pm1004CtrlCommAccessloop=_Pm1004CtrlCommAccessloop_Object((1,3,6,1,4,1,20044,18,6,3,64,1),_Pm1004CtrlCommAccessloop_Type())
pm1004CtrlCommAccessloop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlCommAccessloop.setStatus(_G)
_Pm1004CtrllineLoop_ObjectIdentity=ObjectIdentity
pm1004CtrllineLoop=_Pm1004CtrllineLoop_ObjectIdentity((1,3,6,1,4,1,20044,18,6,3,66))
_Pm1004CtrlLineLoop_Type=EkiOnOff
_Pm1004CtrlLineLoop_Object=MibScalar
pm1004CtrlLineLoop=_Pm1004CtrlLineLoop_Object((1,3,6,1,4,1,20044,18,6,3,66,1),_Pm1004CtrlLineLoop_Type())
pm1004CtrlLineLoop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLineLoop.setStatus(_G)
_Pm1004CtrlmsAis_ObjectIdentity=ObjectIdentity
pm1004CtrlmsAis=_Pm1004CtrlmsAis_ObjectIdentity((1,3,6,1,4,1,20044,18,6,3,67))
_Pm1004CtrlMsAis_Type=EkiOnOff
_Pm1004CtrlMsAis_Object=MibScalar
pm1004CtrlMsAis=_Pm1004CtrlMsAis_Object((1,3,6,1,4,1,20044,18,6,3,67,1),_Pm1004CtrlMsAis_Type())
pm1004CtrlMsAis.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlMsAis.setStatus(_A)
_Pm1004CtrlfecDisableTable_Object=MibTable
pm1004CtrlfecDisableTable=_Pm1004CtrlfecDisableTable_Object((1,3,6,1,4,1,20044,18,6,3,69))
if mibBuilder.loadTexts:pm1004CtrlfecDisableTable.setStatus(_A)
_Pm1004CtrlfecDisableEntry_Object=MibTableRow
pm1004CtrlfecDisableEntry=_Pm1004CtrlfecDisableEntry_Object((1,3,6,1,4,1,20044,18,6,3,69,1))
pm1004CtrlfecDisableEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pm1004CtrlfecDisableEntry.setStatus(_A)
class _Pm1004CtrlfecDisableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlfecDisableIndex_Type.__name__=_D
_Pm1004CtrlfecDisableIndex_Object=MibTableColumn
pm1004CtrlfecDisableIndex=_Pm1004CtrlfecDisableIndex_Object((1,3,6,1,4,1,20044,18,6,3,69,1,1),_Pm1004CtrlfecDisableIndex_Type())
pm1004CtrlfecDisableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlfecDisableIndex.setStatus(_A)
_Pm1004CtrlfecDisablePortn_Type=EkiState
_Pm1004CtrlfecDisablePortn_Object=MibTableColumn
pm1004CtrlfecDisablePortn=_Pm1004CtrlfecDisablePortn_Object((1,3,6,1,4,1,20044,18,6,3,69,1,2),_Pm1004CtrlfecDisablePortn_Type())
pm1004CtrlfecDisablePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlfecDisablePortn.setStatus(_A)
_Pm1004CtrlProtMgnt_ObjectIdentity=ObjectIdentity
pm1004CtrlProtMgnt=_Pm1004CtrlProtMgnt_ObjectIdentity((1,3,6,1,4,1,20044,18,6,3,73))
class _Pm1004CtrlLineNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pm1004CtrlLineNumber_Type.__name__=_F
_Pm1004CtrlLineNumber_Object=MibScalar
pm1004CtrlLineNumber=_Pm1004CtrlLineNumber_Object((1,3,6,1,4,1,20044,18,6,3,73,1),_Pm1004CtrlLineNumber_Type())
pm1004CtrlLineNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlLineNumber.setStatus(_A)
_Pm1004CtrlProtMode_Type=EkiMode
_Pm1004CtrlProtMode_Object=MibScalar
pm1004CtrlProtMode=_Pm1004CtrlProtMode_Object((1,3,6,1,4,1,20044,18,6,3,73,2),_Pm1004CtrlProtMode_Type())
pm1004CtrlProtMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlProtMode.setStatus(_A)
_Pm1004CtrllineOosModeTable_Object=MibTable
pm1004CtrllineOosModeTable=_Pm1004CtrllineOosModeTable_Object((1,3,6,1,4,1,20044,18,6,3,74))
if mibBuilder.loadTexts:pm1004CtrllineOosModeTable.setStatus(_A)
_Pm1004CtrllineOosModeEntry_Object=MibTableRow
pm1004CtrllineOosModeEntry=_Pm1004CtrllineOosModeEntry_Object((1,3,6,1,4,1,20044,18,6,3,74,1))
pm1004CtrllineOosModeEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pm1004CtrllineOosModeEntry.setStatus(_A)
class _Pm1004CtrllineOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllineOosModeIndex_Type.__name__=_D
_Pm1004CtrllineOosModeIndex_Object=MibTableColumn
pm1004CtrllineOosModeIndex=_Pm1004CtrllineOosModeIndex_Object((1,3,6,1,4,1,20044,18,6,3,74,1,1),_Pm1004CtrllineOosModeIndex_Type())
pm1004CtrllineOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllineOosModeIndex.setStatus(_A)
_Pm1004CtrllineOosModePortn_Type=EkiState
_Pm1004CtrllineOosModePortn_Object=MibTableColumn
pm1004CtrllineOosModePortn=_Pm1004CtrllineOosModePortn_Object((1,3,6,1,4,1,20044,18,6,3,74,1,2),_Pm1004CtrllineOosModePortn_Type())
pm1004CtrllineOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrllineOosModePortn.setStatus(_A)
_Pm1004CtrllineResetCount15LineTable_Object=MibTable
pm1004CtrllineResetCount15LineTable=_Pm1004CtrllineResetCount15LineTable_Object((1,3,6,1,4,1,20044,18,6,3,86))
if mibBuilder.loadTexts:pm1004CtrllineResetCount15LineTable.setStatus(_A)
_Pm1004CtrllineResetCount15LineEntry_Object=MibTableRow
pm1004CtrllineResetCount15LineEntry=_Pm1004CtrllineResetCount15LineEntry_Object((1,3,6,1,4,1,20044,18,6,3,86,1))
pm1004CtrllineResetCount15LineEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:pm1004CtrllineResetCount15LineEntry.setStatus(_A)
class _Pm1004CtrllineResetCount15LineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllineResetCount15LineIndex_Type.__name__=_D
_Pm1004CtrllineResetCount15LineIndex_Object=MibTableColumn
pm1004CtrllineResetCount15LineIndex=_Pm1004CtrllineResetCount15LineIndex_Object((1,3,6,1,4,1,20044,18,6,3,86,1,1),_Pm1004CtrllineResetCount15LineIndex_Type())
pm1004CtrllineResetCount15LineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllineResetCount15LineIndex.setStatus(_A)
_Pm1004CtrlresetAllPerfCount15Portn_Type=EkiState
_Pm1004CtrlresetAllPerfCount15Portn_Object=MibTableColumn
pm1004CtrlresetAllPerfCount15Portn=_Pm1004CtrlresetAllPerfCount15Portn_Object((1,3,6,1,4,1,20044,18,6,3,86,1,2),_Pm1004CtrlresetAllPerfCount15Portn_Type())
pm1004CtrlresetAllPerfCount15Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlresetAllPerfCount15Portn.setStatus(_A)
_Pm1004CtrllineResetCount24LineTable_Object=MibTable
pm1004CtrllineResetCount24LineTable=_Pm1004CtrllineResetCount24LineTable_Object((1,3,6,1,4,1,20044,18,6,3,87))
if mibBuilder.loadTexts:pm1004CtrllineResetCount24LineTable.setStatus(_A)
_Pm1004CtrllineResetCount24LineEntry_Object=MibTableRow
pm1004CtrllineResetCount24LineEntry=_Pm1004CtrllineResetCount24LineEntry_Object((1,3,6,1,4,1,20044,18,6,3,87,1))
pm1004CtrllineResetCount24LineEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:pm1004CtrllineResetCount24LineEntry.setStatus(_A)
class _Pm1004CtrllineResetCount24LineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllineResetCount24LineIndex_Type.__name__=_D
_Pm1004CtrllineResetCount24LineIndex_Object=MibTableColumn
pm1004CtrllineResetCount24LineIndex=_Pm1004CtrllineResetCount24LineIndex_Object((1,3,6,1,4,1,20044,18,6,3,87,1,1),_Pm1004CtrllineResetCount24LineIndex_Type())
pm1004CtrllineResetCount24LineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllineResetCount24LineIndex.setStatus(_A)
_Pm1004CtrlresetAllPerfCount24Portn_Type=EkiState
_Pm1004CtrlresetAllPerfCount24Portn_Object=MibTableColumn
pm1004CtrlresetAllPerfCount24Portn=_Pm1004CtrlresetAllPerfCount24Portn_Object((1,3,6,1,4,1,20044,18,6,3,87,1,2),_Pm1004CtrlresetAllPerfCount24Portn_Type())
pm1004CtrlresetAllPerfCount24Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlresetAllPerfCount24Portn.setStatus(_A)
_Pm1004CtrlxfpOnoffTable_Object=MibTable
pm1004CtrlxfpOnoffTable=_Pm1004CtrlxfpOnoffTable_Object((1,3,6,1,4,1,20044,18,6,3,208))
if mibBuilder.loadTexts:pm1004CtrlxfpOnoffTable.setStatus(_A)
_Pm1004CtrlxfpOnoffEntry_Object=MibTableRow
pm1004CtrlxfpOnoffEntry=_Pm1004CtrlxfpOnoffEntry_Object((1,3,6,1,4,1,20044,18,6,3,208,1))
pm1004CtrlxfpOnoffEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:pm1004CtrlxfpOnoffEntry.setStatus(_A)
class _Pm1004CtrlxfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlxfpOnoffIndex_Type.__name__=_D
_Pm1004CtrlxfpOnoffIndex_Object=MibTableColumn
pm1004CtrlxfpOnoffIndex=_Pm1004CtrlxfpOnoffIndex_Object((1,3,6,1,4,1,20044,18,6,3,208,1,1),_Pm1004CtrlxfpOnoffIndex_Type())
pm1004CtrlxfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlxfpOnoffIndex.setStatus(_A)
_Pm1004CtrlxfpOnoffPortn_Type=EkiState
_Pm1004CtrlxfpOnoffPortn_Object=MibTableColumn
pm1004CtrlxfpOnoffPortn=_Pm1004CtrlxfpOnoffPortn_Object((1,3,6,1,4,1,20044,18,6,3,208,1,2),_Pm1004CtrlxfpOnoffPortn_Type())
pm1004CtrlxfpOnoffPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlxfpOnoffPortn.setStatus(_A)
_Pm1004CtrlxfpLineLoopTable_Object=MibTable
pm1004CtrlxfpLineLoopTable=_Pm1004CtrlxfpLineLoopTable_Object((1,3,6,1,4,1,20044,18,6,3,209))
if mibBuilder.loadTexts:pm1004CtrlxfpLineLoopTable.setStatus(_A)
_Pm1004CtrlxfpLineLoopEntry_Object=MibTableRow
pm1004CtrlxfpLineLoopEntry=_Pm1004CtrlxfpLineLoopEntry_Object((1,3,6,1,4,1,20044,18,6,3,209,1))
pm1004CtrlxfpLineLoopEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:pm1004CtrlxfpLineLoopEntry.setStatus(_A)
class _Pm1004CtrlxfpLineLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlxfpLineLoopIndex_Type.__name__=_D
_Pm1004CtrlxfpLineLoopIndex_Object=MibTableColumn
pm1004CtrlxfpLineLoopIndex=_Pm1004CtrlxfpLineLoopIndex_Object((1,3,6,1,4,1,20044,18,6,3,209,1,1),_Pm1004CtrlxfpLineLoopIndex_Type())
pm1004CtrlxfpLineLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlxfpLineLoopIndex.setStatus(_A)
_Pm1004CtrlxfpLineLoopPortn_Type=EkiState
_Pm1004CtrlxfpLineLoopPortn_Object=MibTableColumn
pm1004CtrlxfpLineLoopPortn=_Pm1004CtrlxfpLineLoopPortn_Object((1,3,6,1,4,1,20044,18,6,3,209,1,2),_Pm1004CtrlxfpLineLoopPortn_Type())
pm1004CtrlxfpLineLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlxfpLineLoopPortn.setStatus(_A)
_Pm1004CtrlxfpXfiLoopTable_Object=MibTable
pm1004CtrlxfpXfiLoopTable=_Pm1004CtrlxfpXfiLoopTable_Object((1,3,6,1,4,1,20044,18,6,3,210))
if mibBuilder.loadTexts:pm1004CtrlxfpXfiLoopTable.setStatus(_A)
_Pm1004CtrlxfpXfiLoopEntry_Object=MibTableRow
pm1004CtrlxfpXfiLoopEntry=_Pm1004CtrlxfpXfiLoopEntry_Object((1,3,6,1,4,1,20044,18,6,3,210,1))
pm1004CtrlxfpXfiLoopEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:pm1004CtrlxfpXfiLoopEntry.setStatus(_A)
class _Pm1004CtrlxfpXfiLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrlxfpXfiLoopIndex_Type.__name__=_D
_Pm1004CtrlxfpXfiLoopIndex_Object=MibTableColumn
pm1004CtrlxfpXfiLoopIndex=_Pm1004CtrlxfpXfiLoopIndex_Object((1,3,6,1,4,1,20044,18,6,3,210,1,1),_Pm1004CtrlxfpXfiLoopIndex_Type())
pm1004CtrlxfpXfiLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrlxfpXfiLoopIndex.setStatus(_A)
_Pm1004CtrlxfpXfiLoopPortn_Type=EkiState
_Pm1004CtrlxfpXfiLoopPortn_Object=MibTableColumn
pm1004CtrlxfpXfiLoopPortn=_Pm1004CtrlxfpXfiLoopPortn_Object((1,3,6,1,4,1,20044,18,6,3,210,1,2),_Pm1004CtrlxfpXfiLoopPortn_Type())
pm1004CtrlxfpXfiLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlxfpXfiLoopPortn.setStatus(_A)
_Pm1004CtrllineTunableChannelTable_Object=MibTable
pm1004CtrllineTunableChannelTable=_Pm1004CtrllineTunableChannelTable_Object((1,3,6,1,4,1,20044,18,6,3,212))
if mibBuilder.loadTexts:pm1004CtrllineTunableChannelTable.setStatus(_A)
_Pm1004CtrllineTunableChannelEntry_Object=MibTableRow
pm1004CtrllineTunableChannelEntry=_Pm1004CtrllineTunableChannelEntry_Object((1,3,6,1,4,1,20044,18,6,3,212,1))
pm1004CtrllineTunableChannelEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:pm1004CtrllineTunableChannelEntry.setStatus(_A)
class _Pm1004CtrllineTunableChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllineTunableChannelIndex_Type.__name__=_D
_Pm1004CtrllineTunableChannelIndex_Object=MibTableColumn
pm1004CtrllineTunableChannelIndex=_Pm1004CtrllineTunableChannelIndex_Object((1,3,6,1,4,1,20044,18,6,3,212,1,1),_Pm1004CtrllineTunableChannelIndex_Type())
pm1004CtrllineTunableChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllineTunableChannelIndex.setStatus(_A)
_Pm1004CtrllineTunableChannelPortn_Type=Pm1004OtxChannel
_Pm1004CtrllineTunableChannelPortn_Object=MibTableColumn
pm1004CtrllineTunableChannelPortn=_Pm1004CtrllineTunableChannelPortn_Object((1,3,6,1,4,1,20044,18,6,3,212,1,2),_Pm1004CtrllineTunableChannelPortn_Type())
pm1004CtrllineTunableChannelPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrllineTunableChannelPortn.setStatus(_A)
_Pm1004CtrllinePhotodiodeModeTable_Object=MibTable
pm1004CtrllinePhotodiodeModeTable=_Pm1004CtrllinePhotodiodeModeTable_Object((1,3,6,1,4,1,20044,18,6,3,213))
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeModeTable.setStatus(_A)
_Pm1004CtrllinePhotodiodeModeEntry_Object=MibTableRow
pm1004CtrllinePhotodiodeModeEntry=_Pm1004CtrllinePhotodiodeModeEntry_Object((1,3,6,1,4,1,20044,18,6,3,213,1))
pm1004CtrllinePhotodiodeModeEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeModeEntry.setStatus(_A)
class _Pm1004CtrllinePhotodiodeModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllinePhotodiodeModeIndex_Type.__name__=_D
_Pm1004CtrllinePhotodiodeModeIndex_Object=MibTableColumn
pm1004CtrllinePhotodiodeModeIndex=_Pm1004CtrllinePhotodiodeModeIndex_Object((1,3,6,1,4,1,20044,18,6,3,213,1,1),_Pm1004CtrllinePhotodiodeModeIndex_Type())
pm1004CtrllinePhotodiodeModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeModeIndex.setStatus(_A)
_Pm1004CtrllinePhotodiodeModePortn_Type=Pm1004OtxMode
_Pm1004CtrllinePhotodiodeModePortn_Object=MibTableColumn
pm1004CtrllinePhotodiodeModePortn=_Pm1004CtrllinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,18,6,3,213,1,2),_Pm1004CtrllinePhotodiodeModePortn_Type())
pm1004CtrllinePhotodiodeModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeModePortn.setStatus(_A)
_Pm1004CtrllinePhotodiodeValueTable_Object=MibTable
pm1004CtrllinePhotodiodeValueTable=_Pm1004CtrllinePhotodiodeValueTable_Object((1,3,6,1,4,1,20044,18,6,3,214))
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeValueTable.setStatus(_A)
_Pm1004CtrllinePhotodiodeValueEntry_Object=MibTableRow
pm1004CtrllinePhotodiodeValueEntry=_Pm1004CtrllinePhotodiodeValueEntry_Object((1,3,6,1,4,1,20044,18,6,3,214,1))
pm1004CtrllinePhotodiodeValueEntry.setIndexNames((0,_C,_AV))
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeValueEntry.setStatus(_A)
class _Pm1004CtrllinePhotodiodeValueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllinePhotodiodeValueIndex_Type.__name__=_D
_Pm1004CtrllinePhotodiodeValueIndex_Object=MibTableColumn
pm1004CtrllinePhotodiodeValueIndex=_Pm1004CtrllinePhotodiodeValueIndex_Object((1,3,6,1,4,1,20044,18,6,3,214,1,1),_Pm1004CtrllinePhotodiodeValueIndex_Type())
pm1004CtrllinePhotodiodeValueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeValueIndex.setStatus(_A)
_Pm1004CtrllinePhotodiodeValuePortn_Type=Pm1004AdjustValue
_Pm1004CtrllinePhotodiodeValuePortn_Object=MibTableColumn
pm1004CtrllinePhotodiodeValuePortn=_Pm1004CtrllinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,18,6,3,214,1,2),_Pm1004CtrllinePhotodiodeValuePortn_Type())
pm1004CtrllinePhotodiodeValuePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrllinePhotodiodeValuePortn.setStatus(_A)
_Pm1004CtrllinePowerLaserTable_Object=MibTable
pm1004CtrllinePowerLaserTable=_Pm1004CtrllinePowerLaserTable_Object((1,3,6,1,4,1,20044,18,6,3,215))
if mibBuilder.loadTexts:pm1004CtrllinePowerLaserTable.setStatus(_A)
_Pm1004CtrllinePowerLaserEntry_Object=MibTableRow
pm1004CtrllinePowerLaserEntry=_Pm1004CtrllinePowerLaserEntry_Object((1,3,6,1,4,1,20044,18,6,3,215,1))
pm1004CtrllinePowerLaserEntry.setIndexNames((0,_C,_AW))
if mibBuilder.loadTexts:pm1004CtrllinePowerLaserEntry.setStatus(_A)
class _Pm1004CtrllinePowerLaserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CtrllinePowerLaserIndex_Type.__name__=_D
_Pm1004CtrllinePowerLaserIndex_Object=MibTableColumn
pm1004CtrllinePowerLaserIndex=_Pm1004CtrllinePowerLaserIndex_Object((1,3,6,1,4,1,20044,18,6,3,215,1,1),_Pm1004CtrllinePowerLaserIndex_Type())
pm1004CtrllinePowerLaserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CtrllinePowerLaserIndex.setStatus(_A)
class _Pm1004CtrllinePowerLaserPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1004CtrllinePowerLaserPortn_Type.__name__=_D
_Pm1004CtrllinePowerLaserPortn_Object=MibTableColumn
pm1004CtrllinePowerLaserPortn=_Pm1004CtrllinePowerLaserPortn_Object((1,3,6,1,4,1,20044,18,6,3,215,1,2),_Pm1004CtrllinePowerLaserPortn_Type())
pm1004CtrllinePowerLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrllinePowerLaserPortn.setStatus(_A)
_Pm1004CtrlotxVlhReset_ObjectIdentity=ObjectIdentity
pm1004CtrlotxVlhReset=_Pm1004CtrlotxVlhReset_ObjectIdentity((1,3,6,1,4,1,20044,18,6,3,216))
_Pm1004CtrlOtxVlhReset_Type=EkiOnOff
_Pm1004CtrlOtxVlhReset_Object=MibScalar
pm1004CtrlOtxVlhReset=_Pm1004CtrlOtxVlhReset_Object((1,3,6,1,4,1,20044,18,6,3,216,1),_Pm1004CtrlOtxVlhReset_Type())
pm1004CtrlOtxVlhReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CtrlOtxVlhReset.setStatus(_A)
_Pm1004ri_ObjectIdentity=ObjectIdentity
pm1004ri=_Pm1004ri_ObjectIdentity((1,3,6,1,4,1,20044,18,7))
_Pm1004riTable_ObjectIdentity=ObjectIdentity
pm1004riTable=_Pm1004riTable_ObjectIdentity((1,3,6,1,4,1,20044,18,7,1))
_Pm1004RinvSfpTable_Object=MibTable
pm1004RinvSfpTable=_Pm1004RinvSfpTable_Object((1,3,6,1,4,1,20044,18,7,1,1))
if mibBuilder.loadTexts:pm1004RinvSfpTable.setStatus(_A)
_Pm1004RinvSfpEntry_Object=MibTableRow
pm1004RinvSfpEntry=_Pm1004RinvSfpEntry_Object((1,3,6,1,4,1,20044,18,7,1,1,1))
pm1004RinvSfpEntry.setIndexNames((0,_C,_AX))
if mibBuilder.loadTexts:pm1004RinvSfpEntry.setStatus(_A)
class _Pm1004RinvSfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1004RinvSfpIndex_Type.__name__=_D
_Pm1004RinvSfpIndex_Object=MibTableColumn
pm1004RinvSfpIndex=_Pm1004RinvSfpIndex_Object((1,3,6,1,4,1,20044,18,7,1,1,1,1),_Pm1004RinvSfpIndex_Type())
pm1004RinvSfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvSfpIndex.setStatus(_A)
_Pm1004Rinvsfp_Type=DisplayString
_Pm1004Rinvsfp_Object=MibTableColumn
pm1004Rinvsfp=_Pm1004Rinvsfp_Object((1,3,6,1,4,1,20044,18,7,1,1,1,2),_Pm1004Rinvsfp_Type())
pm1004Rinvsfp.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Rinvsfp.setStatus(_A)
_Pm1004RinvLineTable_Object=MibTable
pm1004RinvLineTable=_Pm1004RinvLineTable_Object((1,3,6,1,4,1,20044,18,7,1,2))
if mibBuilder.loadTexts:pm1004RinvLineTable.setStatus(_A)
_Pm1004RinvLineEntry_Object=MibTableRow
pm1004RinvLineEntry=_Pm1004RinvLineEntry_Object((1,3,6,1,4,1,20044,18,7,1,2,1))
pm1004RinvLineEntry.setIndexNames((0,_C,_AY))
if mibBuilder.loadTexts:pm1004RinvLineEntry.setStatus(_A)
class _Pm1004RinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1004RinvLineIndex_Type.__name__=_D
_Pm1004RinvLineIndex_Object=MibTableColumn
pm1004RinvLineIndex=_Pm1004RinvLineIndex_Object((1,3,6,1,4,1,20044,18,7,1,2,1,1),_Pm1004RinvLineIndex_Type())
pm1004RinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvLineIndex.setStatus(_A)
_Pm1004RinvxfpLine_Type=DisplayString
_Pm1004RinvxfpLine_Object=MibTableColumn
pm1004RinvxfpLine=_Pm1004RinvxfpLine_Object((1,3,6,1,4,1,20044,18,7,1,2,1,2),_Pm1004RinvxfpLine_Type())
pm1004RinvxfpLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvxfpLine.setStatus(_A)
_Pm1004RinvReloadInventory_Type=EkiOnOff
_Pm1004RinvReloadInventory_Object=MibScalar
pm1004RinvReloadInventory=_Pm1004RinvReloadInventory_Object((1,3,6,1,4,1,20044,18,7,2),_Pm1004RinvReloadInventory_Type())
pm1004RinvReloadInventory.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004RinvReloadInventory.setStatus(_A)
_Pm1004RinvHwPlatform_Type=DisplayString
_Pm1004RinvHwPlatform_Object=MibScalar
pm1004RinvHwPlatform=_Pm1004RinvHwPlatform_Object((1,3,6,1,4,1,20044,18,7,3),_Pm1004RinvHwPlatform_Type())
pm1004RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvHwPlatform.setStatus(_A)
_Pm1004RinvModulePlatform_Type=DisplayString
_Pm1004RinvModulePlatform_Object=MibScalar
pm1004RinvModulePlatform=_Pm1004RinvModulePlatform_Object((1,3,6,1,4,1,20044,18,7,4),_Pm1004RinvModulePlatform_Type())
pm1004RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvModulePlatform.setStatus(_A)
_Pm1004RinvSwPlatform_Type=DisplayString
_Pm1004RinvSwPlatform_Object=MibScalar
pm1004RinvSwPlatform=_Pm1004RinvSwPlatform_Object((1,3,6,1,4,1,20044,18,7,5),_Pm1004RinvSwPlatform_Type())
pm1004RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvSwPlatform.setStatus(_A)
_Pm1004RinvGwPlatform_Type=DisplayString
_Pm1004RinvGwPlatform_Object=MibScalar
pm1004RinvGwPlatform=_Pm1004RinvGwPlatform_Object((1,3,6,1,4,1,20044,18,7,6),_Pm1004RinvGwPlatform_Type())
pm1004RinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004RinvGwPlatform.setStatus(_A)
_Pm1004download_ObjectIdentity=ObjectIdentity
pm1004download=_Pm1004download_ObjectIdentity((1,3,6,1,4,1,20044,18,8))
_Pm1004DwlOther_ObjectIdentity=ObjectIdentity
pm1004DwlOther=_Pm1004DwlOther_ObjectIdentity((1,3,6,1,4,1,20044,18,8,1))
_Pm1004DwlrestartProcess_ObjectIdentity=ObjectIdentity
pm1004DwlrestartProcess=_Pm1004DwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,18,8,1,0))
_Pm1004DwlWarmRestartProcessed_Type=EkiOnOff
_Pm1004DwlWarmRestartProcessed_Object=MibScalar
pm1004DwlWarmRestartProcessed=_Pm1004DwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,18,8,1,0,1),_Pm1004DwlWarmRestartProcessed_Type())
pm1004DwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlWarmRestartProcessed.setStatus(_A)
_Pm1004DwlColdRestartProcessed_Type=EkiOnOff
_Pm1004DwlColdRestartProcessed_Object=MibScalar
pm1004DwlColdRestartProcessed=_Pm1004DwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,18,8,1,0,2),_Pm1004DwlColdRestartProcessed_Type())
pm1004DwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlColdRestartProcessed.setStatus(_A)
_Pm1004DwlswBanksUsed_ObjectIdentity=ObjectIdentity
pm1004DwlswBanksUsed=_Pm1004DwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,18,8,1,1))
_Pm1004DwlSwBank1Used_Type=EkiOnOff
_Pm1004DwlSwBank1Used_Object=MibScalar
pm1004DwlSwBank1Used=_Pm1004DwlSwBank1Used_Object((1,3,6,1,4,1,20044,18,8,1,1,1),_Pm1004DwlSwBank1Used_Type())
pm1004DwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlSwBank1Used.setStatus(_A)
_Pm1004DwlSwBank2Used_Type=EkiOnOff
_Pm1004DwlSwBank2Used_Object=MibScalar
pm1004DwlSwBank2Used=_Pm1004DwlSwBank2Used_Object((1,3,6,1,4,1,20044,18,8,1,1,2),_Pm1004DwlSwBank2Used_Type())
pm1004DwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlSwBank2Used.setStatus(_A)
_Pm1004DwlSwBank1Notempty_Type=EkiOnOff
_Pm1004DwlSwBank1Notempty_Object=MibScalar
pm1004DwlSwBank1Notempty=_Pm1004DwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,18,8,1,1,5),_Pm1004DwlSwBank1Notempty_Type())
pm1004DwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlSwBank1Notempty.setStatus(_A)
_Pm1004DwlSwBank2Notempty_Type=EkiOnOff
_Pm1004DwlSwBank2Notempty_Object=MibScalar
pm1004DwlSwBank2Notempty=_Pm1004DwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,18,8,1,1,6),_Pm1004DwlSwBank2Notempty_Type())
pm1004DwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlSwBank2Notempty.setStatus(_A)
_Pm1004DwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pm1004DwlgwBanksUsed=_Pm1004DwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,18,8,1,2))
_Pm1004DwlGwBank1Used_Type=EkiOnOff
_Pm1004DwlGwBank1Used_Object=MibScalar
pm1004DwlGwBank1Used=_Pm1004DwlGwBank1Used_Object((1,3,6,1,4,1,20044,18,8,1,2,1),_Pm1004DwlGwBank1Used_Type())
pm1004DwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank1Used.setStatus(_A)
_Pm1004DwlGwBank2Used_Type=EkiOnOff
_Pm1004DwlGwBank2Used_Object=MibScalar
pm1004DwlGwBank2Used=_Pm1004DwlGwBank2Used_Object((1,3,6,1,4,1,20044,18,8,1,2,2),_Pm1004DwlGwBank2Used_Type())
pm1004DwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank2Used.setStatus(_A)
_Pm1004DwlGwBank3Used_Type=EkiOnOff
_Pm1004DwlGwBank3Used_Object=MibScalar
pm1004DwlGwBank3Used=_Pm1004DwlGwBank3Used_Object((1,3,6,1,4,1,20044,18,8,1,2,3),_Pm1004DwlGwBank3Used_Type())
pm1004DwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank3Used.setStatus(_A)
_Pm1004DwlGwBank4Used_Type=EkiOnOff
_Pm1004DwlGwBank4Used_Object=MibScalar
pm1004DwlGwBank4Used=_Pm1004DwlGwBank4Used_Object((1,3,6,1,4,1,20044,18,8,1,2,4),_Pm1004DwlGwBank4Used_Type())
pm1004DwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank4Used.setStatus(_A)
_Pm1004DwlGwBank1Notempty_Type=EkiOnOff
_Pm1004DwlGwBank1Notempty_Object=MibScalar
pm1004DwlGwBank1Notempty=_Pm1004DwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,18,8,1,2,5),_Pm1004DwlGwBank1Notempty_Type())
pm1004DwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank1Notempty.setStatus(_A)
_Pm1004DwlGwBank2Notempty_Type=EkiOnOff
_Pm1004DwlGwBank2Notempty_Object=MibScalar
pm1004DwlGwBank2Notempty=_Pm1004DwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,18,8,1,2,6),_Pm1004DwlGwBank2Notempty_Type())
pm1004DwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank2Notempty.setStatus(_A)
_Pm1004DwlGwBank3Notempty_Type=EkiOnOff
_Pm1004DwlGwBank3Notempty_Object=MibScalar
pm1004DwlGwBank3Notempty=_Pm1004DwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,18,8,1,2,7),_Pm1004DwlGwBank3Notempty_Type())
pm1004DwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank3Notempty.setStatus(_A)
_Pm1004DwlGwBank4Notempty_Type=EkiOnOff
_Pm1004DwlGwBank4Notempty_Object=MibScalar
pm1004DwlGwBank4Notempty=_Pm1004DwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,18,8,1,2,8),_Pm1004DwlGwBank4Notempty_Type())
pm1004DwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004DwlGwBank4Notempty.setStatus(_A)
_Pm1004DwlClient_ObjectIdentity=ObjectIdentity
pm1004DwlClient=_Pm1004DwlClient_ObjectIdentity((1,3,6,1,4,1,20044,18,8,2))
_Pm1004DwlLine_ObjectIdentity=ObjectIdentity
pm1004DwlLine=_Pm1004DwlLine_ObjectIdentity((1,3,6,1,4,1,20044,18,8,3))
_Pm1004Config_ObjectIdentity=ObjectIdentity
pm1004Config=_Pm1004Config_ObjectIdentity((1,3,6,1,4,1,20044,18,9))
_Pm1004CfgAccessCAisCsf_ObjectIdentity=ObjectIdentity
pm1004CfgAccessCAisCsf=_Pm1004CfgAccessCAisCsf_ObjectIdentity((1,3,6,1,4,1,20044,18,9,1))
_Pm1004CfgClientcaiscsfTable_Object=MibTable
pm1004CfgClientcaiscsfTable=_Pm1004CfgClientcaiscsfTable_Object((1,3,6,1,4,1,20044,18,9,1,1))
if mibBuilder.loadTexts:pm1004CfgClientcaiscsfTable.setStatus(_A)
_Pm1004CfgClientcaiscsfEntry_Object=MibTableRow
pm1004CfgClientcaiscsfEntry=_Pm1004CfgClientcaiscsfEntry_Object((1,3,6,1,4,1,20044,18,9,1,1,1))
pm1004CfgClientcaiscsfEntry.setIndexNames((0,_C,_AZ))
if mibBuilder.loadTexts:pm1004CfgClientcaiscsfEntry.setStatus(_A)
class _Pm1004CfgClientcaiscsfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgClientcaiscsfIndex_Type.__name__=_D
_Pm1004CfgClientcaiscsfIndex_Object=MibTableColumn
pm1004CfgClientcaiscsfIndex=_Pm1004CfgClientcaiscsfIndex_Object((1,3,6,1,4,1,20044,18,9,1,1,1,1),_Pm1004CfgClientcaiscsfIndex_Type())
pm1004CfgClientcaiscsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgClientcaiscsfIndex.setStatus(_A)
class _Pm1004CfgCAisModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgCAisModePortn_Type.__name__=_F
_Pm1004CfgCAisModePortn_Object=MibTableColumn
pm1004CfgCAisModePortn=_Pm1004CfgCAisModePortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,3),_Pm1004CfgCAisModePortn_Type())
pm1004CfgCAisModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgCAisModePortn.setStatus(_A)
class _Pm1004CfgUpAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgUpAccessioAlmPortn_Type.__name__=_F
_Pm1004CfgUpAccessioAlmPortn_Object=MibTableColumn
pm1004CfgUpAccessioAlmPortn=_Pm1004CfgUpAccessioAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,9),_Pm1004CfgUpAccessioAlmPortn_Type())
pm1004CfgUpAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgUpAccessioAlmPortn.setStatus(_A)
class _Pm1004CfgUpMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgUpMapperDeAlmPortn_Type.__name__=_F
_Pm1004CfgUpMapperDeAlmPortn_Object=MibTableColumn
pm1004CfgUpMapperDeAlmPortn=_Pm1004CfgUpMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,10),_Pm1004CfgUpMapperDeAlmPortn_Type())
pm1004CfgUpMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgUpMapperDeAlmPortn.setStatus(_A)
class _Pm1004CfgUpAccessioSdhAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgUpAccessioSdhAlmPortn_Type.__name__=_F
_Pm1004CfgUpAccessioSdhAlmPortn_Object=MibTableColumn
pm1004CfgUpAccessioSdhAlmPortn=_Pm1004CfgUpAccessioSdhAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,11),_Pm1004CfgUpAccessioSdhAlmPortn_Type())
pm1004CfgUpAccessioSdhAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgUpAccessioSdhAlmPortn.setStatus(_A)
class _Pm1004CfgDownAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgDownAccessioAlmPortn_Type.__name__=_F
_Pm1004CfgDownAccessioAlmPortn_Object=MibTableColumn
pm1004CfgDownAccessioAlmPortn=_Pm1004CfgDownAccessioAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,17),_Pm1004CfgDownAccessioAlmPortn_Type())
pm1004CfgDownAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgDownAccessioAlmPortn.setStatus(_A)
class _Pm1004CfgDownMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgDownMapperDeAlmPortn_Type.__name__=_F
_Pm1004CfgDownMapperDeAlmPortn_Object=MibTableColumn
pm1004CfgDownMapperDeAlmPortn=_Pm1004CfgDownMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,18),_Pm1004CfgDownMapperDeAlmPortn_Type())
pm1004CfgDownMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgDownMapperDeAlmPortn.setStatus(_A)
class _Pm1004CfgDownDfrmAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgDownDfrmAlmPortn_Type.__name__=_F
_Pm1004CfgDownDfrmAlmPortn_Object=MibTableColumn
pm1004CfgDownDfrmAlmPortn=_Pm1004CfgDownDfrmAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,19),_Pm1004CfgDownDfrmAlmPortn_Type())
pm1004CfgDownDfrmAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgDownDfrmAlmPortn.setStatus(_A)
class _Pm1004CfgDownLineSyncAlarmsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgDownLineSyncAlarmsPortn_Type.__name__=_F
_Pm1004CfgDownLineSyncAlarmsPortn_Object=MibTableColumn
pm1004CfgDownLineSyncAlarmsPortn=_Pm1004CfgDownLineSyncAlarmsPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,20),_Pm1004CfgDownLineSyncAlarmsPortn_Type())
pm1004CfgDownLineSyncAlarmsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgDownLineSyncAlarmsPortn.setStatus(_G)
class _Pm1004CfgDownAccessioSdhAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgDownAccessioSdhAlmPortn_Type.__name__=_F
_Pm1004CfgDownAccessioSdhAlmPortn_Object=MibTableColumn
pm1004CfgDownAccessioSdhAlmPortn=_Pm1004CfgDownAccessioSdhAlmPortn_Object((1,3,6,1,4,1,20044,18,9,1,1,1,21),_Pm1004CfgDownAccessioSdhAlmPortn_Type())
pm1004CfgDownAccessioSdhAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgDownAccessioSdhAlmPortn.setStatus(_A)
_Pm1004CfgStartup_ObjectIdentity=ObjectIdentity
pm1004CfgStartup=_Pm1004CfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,18,9,2))
_Pm1004CfgClientStartupTable_Object=MibTable
pm1004CfgClientStartupTable=_Pm1004CfgClientStartupTable_Object((1,3,6,1,4,1,20044,18,9,2,1))
if mibBuilder.loadTexts:pm1004CfgClientStartupTable.setStatus(_A)
_Pm1004CfgClientStartupEntry_Object=MibTableRow
pm1004CfgClientStartupEntry=_Pm1004CfgClientStartupEntry_Object((1,3,6,1,4,1,20044,18,9,2,1,1))
pm1004CfgClientStartupEntry.setIndexNames((0,_C,_Aa))
if mibBuilder.loadTexts:pm1004CfgClientStartupEntry.setStatus(_A)
class _Pm1004CfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgClientStartupIndex_Type.__name__=_D
_Pm1004CfgClientStartupIndex_Object=MibTableColumn
pm1004CfgClientStartupIndex=_Pm1004CfgClientStartupIndex_Object((1,3,6,1,4,1,20044,18,9,2,1,1,1),_Pm1004CfgClientStartupIndex_Type())
pm1004CfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgClientStartupIndex.setStatus(_A)
class _Pm1004CfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgSystConfPortPortn_Type.__name__=_F
_Pm1004CfgSystConfPortPortn_Object=MibTableColumn
pm1004CfgSystConfPortPortn=_Pm1004CfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,18,9,2,1,1,3),_Pm1004CfgSystConfPortPortn_Type())
pm1004CfgSystConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgSystConfPortPortn.setStatus(_A)
class _Pm1004CfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgNetConfPortPortn_Type.__name__=_F
_Pm1004CfgNetConfPortPortn_Object=MibTableColumn
pm1004CfgNetConfPortPortn=_Pm1004CfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,18,9,2,1,1,4),_Pm1004CfgNetConfPortPortn_Type())
pm1004CfgNetConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgNetConfPortPortn.setStatus(_A)
_Pm1004tablelineStartup_ObjectIdentity=ObjectIdentity
pm1004tablelineStartup=_Pm1004tablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,18,9,2,2))
class _Pm1004CfgsystConfLine1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgsystConfLine1_Type.__name__=_F
_Pm1004CfgsystConfLine1_Object=MibScalar
pm1004CfgsystConfLine1=_Pm1004CfgsystConfLine1_Object((1,3,6,1,4,1,20044,18,9,2,2,2),_Pm1004CfgsystConfLine1_Type())
pm1004CfgsystConfLine1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgsystConfLine1.setStatus(_A)
class _Pm1004CfglineOptions1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfglineOptions1_Type.__name__=_F
_Pm1004CfglineOptions1_Object=MibScalar
pm1004CfglineOptions1=_Pm1004CfglineOptions1_Object((1,3,6,1,4,1,20044,18,9,2,2,5),_Pm1004CfglineOptions1_Type())
pm1004CfglineOptions1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfglineOptions1.setStatus(_A)
class _Pm1004CfgsystConfLine2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgsystConfLine2_Type.__name__=_F
_Pm1004CfgsystConfLine2_Object=MibScalar
pm1004CfgsystConfLine2=_Pm1004CfgsystConfLine2_Object((1,3,6,1,4,1,20044,18,9,2,2,6),_Pm1004CfgsystConfLine2_Type())
pm1004CfgsystConfLine2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgsystConfLine2.setStatus(_A)
class _Pm1004CfglineSelection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfglineSelection_Type.__name__=_F
_Pm1004CfglineSelection_Object=MibScalar
pm1004CfglineSelection=_Pm1004CfglineSelection_Object((1,3,6,1,4,1,20044,18,9,2,2,7),_Pm1004CfglineSelection_Type())
pm1004CfglineSelection.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfglineSelection.setStatus(_A)
_Pm1004CfgXfpTable_Object=MibTable
pm1004CfgXfpTable=_Pm1004CfgXfpTable_Object((1,3,6,1,4,1,20044,18,9,2,3))
if mibBuilder.loadTexts:pm1004CfgXfpTable.setStatus(_A)
_Pm1004CfgXfpEntry_Object=MibTableRow
pm1004CfgXfpEntry=_Pm1004CfgXfpEntry_Object((1,3,6,1,4,1,20044,18,9,2,3,1))
pm1004CfgXfpEntry.setIndexNames((0,_C,_Ab))
if mibBuilder.loadTexts:pm1004CfgXfpEntry.setStatus(_A)
class _Pm1004CfgXfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgXfpIndex_Type.__name__=_D
_Pm1004CfgXfpIndex_Object=MibTableColumn
pm1004CfgXfpIndex=_Pm1004CfgXfpIndex_Object((1,3,6,1,4,1,20044,18,9,2,3,1,1),_Pm1004CfgXfpIndex_Type())
pm1004CfgXfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgXfpIndex.setStatus(_A)
class _Pm1004CfgSystConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgSystConfXfpPortn_Type.__name__=_F
_Pm1004CfgSystConfXfpPortn_Object=MibTableColumn
pm1004CfgSystConfXfpPortn=_Pm1004CfgSystConfXfpPortn_Object((1,3,6,1,4,1,20044,18,9,2,3,1,3),_Pm1004CfgSystConfXfpPortn_Type())
pm1004CfgSystConfXfpPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgSystConfXfpPortn.setStatus(_A)
class _Pm1004CfgDataRateConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgDataRateConfXfpPortn_Type.__name__=_F
_Pm1004CfgDataRateConfXfpPortn_Object=MibTableColumn
pm1004CfgDataRateConfXfpPortn=_Pm1004CfgDataRateConfXfpPortn_Object((1,3,6,1,4,1,20044,18,9,2,3,1,4),_Pm1004CfgDataRateConfXfpPortn_Type())
pm1004CfgDataRateConfXfpPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgDataRateConfXfpPortn.setStatus(_G)
_Pm1004CfgModPerfConfig_ObjectIdentity=ObjectIdentity
pm1004CfgModPerfConfig=_Pm1004CfgModPerfConfig_ObjectIdentity((1,3,6,1,4,1,20044,18,9,3))
_Pm1004tablemodPerfConfig_ObjectIdentity=ObjectIdentity
pm1004tablemodPerfConfig=_Pm1004tablemodPerfConfig_ObjectIdentity((1,3,6,1,4,1,20044,18,9,3,1))
class _Pm1004CfgperfMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgperfMode_Type.__name__=_F
_Pm1004CfgperfMode_Object=MibScalar
pm1004CfgperfMode=_Pm1004CfgperfMode_Object((1,3,6,1,4,1,20044,18,9,3,1,2),_Pm1004CfgperfMode_Type())
pm1004CfgperfMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgperfMode.setStatus(_A)
_Pm1004CfgJ0Client_ObjectIdentity=ObjectIdentity
pm1004CfgJ0Client=_Pm1004CfgJ0Client_ObjectIdentity((1,3,6,1,4,1,20044,18,9,4))
_Pm1004CfgEmptyTable_Object=MibTable
pm1004CfgEmptyTable=_Pm1004CfgEmptyTable_Object((1,3,6,1,4,1,20044,18,9,4,1))
if mibBuilder.loadTexts:pm1004CfgEmptyTable.setStatus(_A)
_Pm1004CfgEmptyEntry_Object=MibTableRow
pm1004CfgEmptyEntry=_Pm1004CfgEmptyEntry_Object((1,3,6,1,4,1,20044,18,9,4,1,1))
pm1004CfgEmptyEntry.setIndexNames((0,_C,_Ac))
if mibBuilder.loadTexts:pm1004CfgEmptyEntry.setStatus(_A)
class _Pm1004CfgEmptyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgEmptyIndex_Type.__name__=_D
_Pm1004CfgEmptyIndex_Object=MibTableColumn
pm1004CfgEmptyIndex=_Pm1004CfgEmptyIndex_Object((1,3,6,1,4,1,20044,18,9,4,1,1,1),_Pm1004CfgEmptyIndex_Type())
pm1004CfgEmptyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgEmptyIndex.setStatus(_A)
class _Pm1004CfgClientExpectJ0SetupPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgClientExpectJ0SetupPortn_Type.__name__=_F
_Pm1004CfgClientExpectJ0SetupPortn_Object=MibTableColumn
pm1004CfgClientExpectJ0SetupPortn=_Pm1004CfgClientExpectJ0SetupPortn_Object((1,3,6,1,4,1,20044,18,9,4,1,1,3),_Pm1004CfgClientExpectJ0SetupPortn_Type())
pm1004CfgClientExpectJ0SetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgClientExpectJ0SetupPortn.setStatus(_A)
_Pm1004CfgLabels_ObjectIdentity=ObjectIdentity
pm1004CfgLabels=_Pm1004CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,18,9,5))
_Pm1004CfgLabelclientTable_Object=MibTable
pm1004CfgLabelclientTable=_Pm1004CfgLabelclientTable_Object((1,3,6,1,4,1,20044,18,9,5,1))
if mibBuilder.loadTexts:pm1004CfgLabelclientTable.setStatus(_A)
_Pm1004CfgLabelclientEntry_Object=MibTableRow
pm1004CfgLabelclientEntry=_Pm1004CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,18,9,5,1,1))
pm1004CfgLabelclientEntry.setIndexNames((0,_C,_Ad))
if mibBuilder.loadTexts:pm1004CfgLabelclientEntry.setStatus(_A)
class _Pm1004CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgLabelclientIndex_Type.__name__=_D
_Pm1004CfgLabelclientIndex_Object=MibTableColumn
pm1004CfgLabelclientIndex=_Pm1004CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,18,9,5,1,1,1),_Pm1004CfgLabelclientIndex_Type())
pm1004CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgLabelclientIndex.setStatus(_A)
class _Pm1004CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1004CfgLabelclientPortn_Type.__name__=_K
_Pm1004CfgLabelclientPortn_Object=MibTableColumn
pm1004CfgLabelclientPortn=_Pm1004CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,18,9,5,1,1,3),_Pm1004CfgLabelclientPortn_Type())
pm1004CfgLabelclientPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLabelclientPortn.setStatus(_A)
_Pm1004CfgLabellineTable_Object=MibTable
pm1004CfgLabellineTable=_Pm1004CfgLabellineTable_Object((1,3,6,1,4,1,20044,18,9,5,2))
if mibBuilder.loadTexts:pm1004CfgLabellineTable.setStatus(_A)
_Pm1004CfgLabellineEntry_Object=MibTableRow
pm1004CfgLabellineEntry=_Pm1004CfgLabellineEntry_Object((1,3,6,1,4,1,20044,18,9,5,2,1))
pm1004CfgLabellineEntry.setIndexNames((0,_C,_Ae))
if mibBuilder.loadTexts:pm1004CfgLabellineEntry.setStatus(_A)
class _Pm1004CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgLabellineIndex_Type.__name__=_D
_Pm1004CfgLabellineIndex_Object=MibTableColumn
pm1004CfgLabellineIndex=_Pm1004CfgLabellineIndex_Object((1,3,6,1,4,1,20044,18,9,5,2,1,1),_Pm1004CfgLabellineIndex_Type())
pm1004CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgLabellineIndex.setStatus(_A)
class _Pm1004CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1004CfgLabellinePortn_Type.__name__=_K
_Pm1004CfgLabellinePortn_Object=MibTableColumn
pm1004CfgLabellinePortn=_Pm1004CfgLabellinePortn_Object((1,3,6,1,4,1,20044,18,9,5,2,1,3),_Pm1004CfgLabellinePortn_Type())
pm1004CfgLabellinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLabellinePortn.setStatus(_A)
_Pm1004CfgStartuptlh_ObjectIdentity=ObjectIdentity
pm1004CfgStartuptlh=_Pm1004CfgStartuptlh_ObjectIdentity((1,3,6,1,4,1,20044,18,9,6))
_Pm1004CfgOtxtlhTable_Object=MibTable
pm1004CfgOtxtlhTable=_Pm1004CfgOtxtlhTable_Object((1,3,6,1,4,1,20044,18,9,6,1))
if mibBuilder.loadTexts:pm1004CfgOtxtlhTable.setStatus(_A)
_Pm1004CfgOtxtlhEntry_Object=MibTableRow
pm1004CfgOtxtlhEntry=_Pm1004CfgOtxtlhEntry_Object((1,3,6,1,4,1,20044,18,9,6,1,1))
pm1004CfgOtxtlhEntry.setIndexNames((0,_C,_Af))
if mibBuilder.loadTexts:pm1004CfgOtxtlhEntry.setStatus(_A)
class _Pm1004CfgOtxtlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgOtxtlhIndex_Type.__name__=_D
_Pm1004CfgOtxtlhIndex_Object=MibTableColumn
pm1004CfgOtxtlhIndex=_Pm1004CfgOtxtlhIndex_Object((1,3,6,1,4,1,20044,18,9,6,1,1,1),_Pm1004CfgOtxtlhIndex_Type())
pm1004CfgOtxtlhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgOtxtlhIndex.setStatus(_A)
class _Pm1004CfgNuPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgNuPortn_Type.__name__=_F
_Pm1004CfgNuPortn_Object=MibTableColumn
pm1004CfgNuPortn=_Pm1004CfgNuPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,3),_Pm1004CfgNuPortn_Type())
pm1004CfgNuPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgNuPortn.setStatus(_G)
class _Pm1004CfgLineDitherRatePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLineDitherRatePortn_Type.__name__=_F
_Pm1004CfgLineDitherRatePortn_Object=MibTableColumn
pm1004CfgLineDitherRatePortn=_Pm1004CfgLineDitherRatePortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,4),_Pm1004CfgLineDitherRatePortn_Type())
pm1004CfgLineDitherRatePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLineDitherRatePortn.setStatus(_A)
class _Pm1004CfgLineDitherFhzPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLineDitherFhzPortn_Type.__name__=_F
_Pm1004CfgLineDitherFhzPortn_Object=MibTableColumn
pm1004CfgLineDitherFhzPortn=_Pm1004CfgLineDitherFhzPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,5),_Pm1004CfgLineDitherFhzPortn_Type())
pm1004CfgLineDitherFhzPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLineDitherFhzPortn.setStatus(_A)
class _Pm1004CfgLinePwrLaserPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLinePwrLaserPortn_Type.__name__=_F
_Pm1004CfgLinePwrLaserPortn_Object=MibTableColumn
pm1004CfgLinePwrLaserPortn=_Pm1004CfgLinePwrLaserPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,6),_Pm1004CfgLinePwrLaserPortn_Type())
pm1004CfgLinePwrLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLinePwrLaserPortn.setStatus(_A)
class _Pm1004CfgLineFCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLineFCurrentPortn_Type.__name__=_F
_Pm1004CfgLineFCurrentPortn_Object=MibTableColumn
pm1004CfgLineFCurrentPortn=_Pm1004CfgLineFCurrentPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,7),_Pm1004CfgLineFCurrentPortn_Type())
pm1004CfgLineFCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLineFCurrentPortn.setStatus(_A)
class _Pm1004CfgLineGridCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLineGridCurrentPortn_Type.__name__=_F
_Pm1004CfgLineGridCurrentPortn_Object=MibTableColumn
pm1004CfgLineGridCurrentPortn=_Pm1004CfgLineGridCurrentPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,8),_Pm1004CfgLineGridCurrentPortn_Type())
pm1004CfgLineGridCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLineGridCurrentPortn.setStatus(_A)
class _Pm1004CfgFPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgFPortn_Type.__name__=_F
_Pm1004CfgFPortn_Object=MibTableColumn
pm1004CfgFPortn=_Pm1004CfgFPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,9),_Pm1004CfgFPortn_Type())
pm1004CfgFPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgFPortn.setStatus(_A)
class _Pm1004CfgReservedPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgReservedPortn_Type.__name__=_F
_Pm1004CfgReservedPortn_Object=MibTableColumn
pm1004CfgReservedPortn=_Pm1004CfgReservedPortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,10),_Pm1004CfgReservedPortn_Type())
pm1004CfgReservedPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgReservedPortn.setStatus(_G)
class _Pm1004CfgLinePhotodiodeModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLinePhotodiodeModePortn_Type.__name__=_F
_Pm1004CfgLinePhotodiodeModePortn_Object=MibTableColumn
pm1004CfgLinePhotodiodeModePortn=_Pm1004CfgLinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,11),_Pm1004CfgLinePhotodiodeModePortn_Type())
pm1004CfgLinePhotodiodeModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLinePhotodiodeModePortn.setStatus(_A)
class _Pm1004CfgLinePhotodiodeValuePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLinePhotodiodeValuePortn_Type.__name__=_F
_Pm1004CfgLinePhotodiodeValuePortn_Object=MibTableColumn
pm1004CfgLinePhotodiodeValuePortn=_Pm1004CfgLinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,18,9,6,1,1,12),_Pm1004CfgLinePhotodiodeValuePortn_Type())
pm1004CfgLinePhotodiodeValuePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgLinePhotodiodeValuePortn.setStatus(_A)
_Pm1004CfgStartuptablefive_ObjectIdentity=ObjectIdentity
pm1004CfgStartuptablefive=_Pm1004CfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,18,9,7))
_Pm1004CfgOtxtlhcapabilitiesTable_Object=MibTable
pm1004CfgOtxtlhcapabilitiesTable=_Pm1004CfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,18,9,7,1))
if mibBuilder.loadTexts:pm1004CfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pm1004CfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pm1004CfgOtxtlhcapabilitiesEntry=_Pm1004CfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,18,9,7,1,1))
pm1004CfgOtxtlhcapabilitiesEntry.setIndexNames((0,_C,_Ag))
if mibBuilder.loadTexts:pm1004CfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pm1004CfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004CfgOtxtlhcapabilitiesIndex_Type.__name__=_D
_Pm1004CfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pm1004CfgOtxtlhcapabilitiesIndex=_Pm1004CfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,18,9,7,1,1,1),_Pm1004CfgOtxtlhcapabilitiesIndex_Type())
pm1004CfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pm1004CfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgComponentTypePortn_Type.__name__=_F
_Pm1004CfgComponentTypePortn_Object=MibTableColumn
pm1004CfgComponentTypePortn=_Pm1004CfgComponentTypePortn_Object((1,3,6,1,4,1,20044,18,9,7,1,1,3),_Pm1004CfgComponentTypePortn_Type())
pm1004CfgComponentTypePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgComponentTypePortn.setStatus(_A)
class _Pm1004CfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgMiscellaneousPortn_Type.__name__=_F
_Pm1004CfgMiscellaneousPortn_Object=MibTableColumn
pm1004CfgMiscellaneousPortn=_Pm1004CfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,18,9,7,1,1,4),_Pm1004CfgMiscellaneousPortn_Type())
pm1004CfgMiscellaneousPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgMiscellaneousPortn.setStatus(_A)
class _Pm1004CfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgFirstChannelPortn_Type.__name__=_F
_Pm1004CfgFirstChannelPortn_Object=MibTableColumn
pm1004CfgFirstChannelPortn=_Pm1004CfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,18,9,7,1,1,5),_Pm1004CfgFirstChannelPortn_Type())
pm1004CfgFirstChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgFirstChannelPortn.setStatus(_A)
class _Pm1004CfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgLastChannelPortn_Type.__name__=_F
_Pm1004CfgLastChannelPortn_Object=MibTableColumn
pm1004CfgLastChannelPortn=_Pm1004CfgLastChannelPortn_Object((1,3,6,1,4,1,20044,18,9,7,1,1,6),_Pm1004CfgLastChannelPortn_Type())
pm1004CfgLastChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgLastChannelPortn.setStatus(_A)
class _Pm1004CfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1004CfgGridPortn_Type.__name__=_F
_Pm1004CfgGridPortn_Object=MibTableColumn
pm1004CfgGridPortn=_Pm1004CfgGridPortn_Object((1,3,6,1,4,1,20044,18,9,7,1,1,7),_Pm1004CfgGridPortn_Type())
pm1004CfgGridPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004CfgGridPortn.setStatus(_A)
_Pm1004CfgWriteConfiguration_Type=EkiOnOff
_Pm1004CfgWriteConfiguration_Object=MibScalar
pm1004CfgWriteConfiguration=_Pm1004CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,18,9,257),_Pm1004CfgWriteConfiguration_Type())
pm1004CfgWriteConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004CfgWriteConfiguration.setStatus(_A)
_Pm1004traps_ObjectIdentity=ObjectIdentity
pm1004traps=_Pm1004traps_ObjectIdentity((1,3,6,1,4,1,20044,18,10))
class _Pm1004trapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1004trapPortNumber_Type.__name__=_D
_Pm1004trapPortNumber_Object=MibScalar
pm1004trapPortNumber=_Pm1004trapPortNumber_Object((1,3,6,1,4,1,20044,18,10,2),_Pm1004trapPortNumber_Type())
pm1004trapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004trapPortNumber.setStatus(_A)
class _Pm1004trapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1004trapLineNumber_Type.__name__=_D
_Pm1004trapLineNumber_Object=MibScalar
pm1004trapLineNumber=_Pm1004trapLineNumber_Object((1,3,6,1,4,1,20044,18,10,3),_Pm1004trapLineNumber_Type())
pm1004trapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004trapLineNumber.setStatus(_A)
class _Pm1004trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1004trapBoardNumber_Type.__name__=_D
_Pm1004trapBoardNumber_Object=MibScalar
pm1004trapBoardNumber=_Pm1004trapBoardNumber_Object((1,3,6,1,4,1,20044,18,10,4),_Pm1004trapBoardNumber_Type())
pm1004trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004trapBoardNumber.setStatus(_A)
_Pm1004Monitoring_ObjectIdentity=ObjectIdentity
pm1004Monitoring=_Pm1004Monitoring_ObjectIdentity((1,3,6,1,4,1,20044,18,11))
_Pm1004MonOther_ObjectIdentity=ObjectIdentity
pm1004MonOther=_Pm1004MonOther_ObjectIdentity((1,3,6,1,4,1,20044,18,11,1))
_Pm1004MonSync_ObjectIdentity=ObjectIdentity
pm1004MonSync=_Pm1004MonSync_ObjectIdentity((1,3,6,1,4,1,20044,18,11,1,1))
_Pm1004PerfEnable_Type=EkiOnOff
_Pm1004PerfEnable_Object=MibScalar
pm1004PerfEnable=_Pm1004PerfEnable_Object((1,3,6,1,4,1,20044,18,11,1,1,257),_Pm1004PerfEnable_Type())
pm1004PerfEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004PerfEnable.setStatus(_A)
_Pm1004PerfSyncSource_Type=EkiSynchroMode
_Pm1004PerfSyncSource_Object=MibScalar
pm1004PerfSyncSource=_Pm1004PerfSyncSource_Object((1,3,6,1,4,1,20044,18,11,1,1,258),_Pm1004PerfSyncSource_Type())
pm1004PerfSyncSource.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004PerfSyncSource.setStatus(_A)
_Pm1004Perf15minSync_Type=EkiOnOff
_Pm1004Perf15minSync_Object=MibScalar
pm1004Perf15minSync=_Pm1004Perf15minSync_Object((1,3,6,1,4,1,20044,18,11,1,1,259),_Pm1004Perf15minSync_Type())
pm1004Perf15minSync.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004Perf15minSync.setStatus(_A)
_Pm1004Perf24hSync_Type=EkiOnOff
_Pm1004Perf24hSync_Object=MibScalar
pm1004Perf24hSync=_Pm1004Perf24hSync_Object((1,3,6,1,4,1,20044,18,11,1,1,260),_Pm1004Perf24hSync_Type())
pm1004Perf24hSync.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004Perf24hSync.setStatus(_A)
_Pm1004MonTimeStamp_ObjectIdentity=ObjectIdentity
pm1004MonTimeStamp=_Pm1004MonTimeStamp_ObjectIdentity((1,3,6,1,4,1,20044,18,11,1,2))
_Pm1004PerfCurrent15MinElapsedTime_Type=Counter32
_Pm1004PerfCurrent15MinElapsedTime_Object=MibScalar
pm1004PerfCurrent15MinElapsedTime=_Pm1004PerfCurrent15MinElapsedTime_Object((1,3,6,1,4,1,20044,18,11,1,2,5),_Pm1004PerfCurrent15MinElapsedTime_Type())
pm1004PerfCurrent15MinElapsedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004PerfCurrent15MinElapsedTime.setStatus(_A)
_Pm1004PerfCurrent24HoursElapsedTime_Type=Counter32
_Pm1004PerfCurrent24HoursElapsedTime_Object=MibScalar
pm1004PerfCurrent24HoursElapsedTime=_Pm1004PerfCurrent24HoursElapsedTime_Object((1,3,6,1,4,1,20044,18,11,1,2,6),_Pm1004PerfCurrent24HoursElapsedTime_Type())
pm1004PerfCurrent24HoursElapsedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004PerfCurrent24HoursElapsedTime.setStatus(_A)
_Pm1004PerfPast15MinElapsedTime_Type=Counter32
_Pm1004PerfPast15MinElapsedTime_Object=MibScalar
pm1004PerfPast15MinElapsedTime=_Pm1004PerfPast15MinElapsedTime_Object((1,3,6,1,4,1,20044,18,11,1,2,7),_Pm1004PerfPast15MinElapsedTime_Type())
pm1004PerfPast15MinElapsedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004PerfPast15MinElapsedTime.setStatus(_A)
_Pm1004PerfPast24HoursElapsedTime_Type=Counter32
_Pm1004PerfPast24HoursElapsedTime_Object=MibScalar
pm1004PerfPast24HoursElapsedTime=_Pm1004PerfPast24HoursElapsedTime_Object((1,3,6,1,4,1,20044,18,11,1,2,8),_Pm1004PerfPast24HoursElapsedTime_Type())
pm1004PerfPast24HoursElapsedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1004PerfPast24HoursElapsedTime.setStatus(_A)
_Pm1004MonClient_ObjectIdentity=ObjectIdentity
pm1004MonClient=_Pm1004MonClient_ObjectIdentity((1,3,6,1,4,1,20044,18,11,2))
_Pm1004MonClientPerformance_ObjectIdentity=ObjectIdentity
pm1004MonClientPerformance=_Pm1004MonClientPerformance_ObjectIdentity((1,3,6,1,4,1,20044,18,11,2,1))
_Pm1004PerfUpCurrent15CntTable_Object=MibTable
pm1004PerfUpCurrent15CntTable=_Pm1004PerfUpCurrent15CntTable_Object((1,3,6,1,4,1,20044,18,11,2,1,16))
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntTable.setStatus(_A)
_Pm1004PerfUpCurrent15CntEntry_Object=MibTableRow
pm1004PerfUpCurrent15CntEntry=_Pm1004PerfUpCurrent15CntEntry_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1))
pm1004PerfUpCurrent15CntEntry.setIndexNames((0,_C,_Ah))
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntEntry.setStatus(_A)
class _Pm1004PerfUpCurrent15CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfUpCurrent15CntIndex_Type.__name__=_D
_Pm1004PerfUpCurrent15CntIndex_Object=MibTableColumn
pm1004PerfUpCurrent15CntIndex=_Pm1004PerfUpCurrent15CntIndex_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,1),_Pm1004PerfUpCurrent15CntIndex_Type())
pm1004PerfUpCurrent15CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntIndex.setStatus(_A)
_Pm1004PerfUpCurrent15CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent15CntInvCvPortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntInvCvPortn=_Pm1004PerfUpCurrent15CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,2),_Pm1004PerfUpCurrent15CntInvCvPortn_Type())
pm1004PerfUpCurrent15CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntInvCvPortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntCvValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent15CntCvValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntCvValuePortn=_Pm1004PerfUpCurrent15CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,3),_Pm1004PerfUpCurrent15CntCvValuePortn_Type())
pm1004PerfUpCurrent15CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntCvValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent15CntInvEsPortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntInvEsPortn=_Pm1004PerfUpCurrent15CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,4),_Pm1004PerfUpCurrent15CntInvEsPortn_Type())
pm1004PerfUpCurrent15CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntInvEsPortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntEsValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent15CntEsValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntEsValuePortn=_Pm1004PerfUpCurrent15CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,5),_Pm1004PerfUpCurrent15CntEsValuePortn_Type())
pm1004PerfUpCurrent15CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntEsValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent15CntInvSesPortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntInvSesPortn=_Pm1004PerfUpCurrent15CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,6),_Pm1004PerfUpCurrent15CntInvSesPortn_Type())
pm1004PerfUpCurrent15CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntInvSesPortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntSesValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent15CntSesValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntSesValuePortn=_Pm1004PerfUpCurrent15CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,7),_Pm1004PerfUpCurrent15CntSesValuePortn_Type())
pm1004PerfUpCurrent15CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntSesValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent15CntInvSefsPortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntInvSefsPortn=_Pm1004PerfUpCurrent15CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,8),_Pm1004PerfUpCurrent15CntInvSefsPortn_Type())
pm1004PerfUpCurrent15CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntInvSefsPortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent15CntSefsValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntSefsValuePortn=_Pm1004PerfUpCurrent15CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,9),_Pm1004PerfUpCurrent15CntSefsValuePortn_Type())
pm1004PerfUpCurrent15CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntSefsValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent15CntInvUasPortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntInvUasPortn=_Pm1004PerfUpCurrent15CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,10),_Pm1004PerfUpCurrent15CntInvUasPortn_Type())
pm1004PerfUpCurrent15CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntInvUasPortn.setStatus(_A)
_Pm1004PerfUpCurrent15CntUasValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent15CntUasValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent15CntUasValuePortn=_Pm1004PerfUpCurrent15CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,16,1,11),_Pm1004PerfUpCurrent15CntUasValuePortn_Type())
pm1004PerfUpCurrent15CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent15CntUasValuePortn.setStatus(_A)
_Pm1004PerfUpPast15CntTable_Object=MibTable
pm1004PerfUpPast15CntTable=_Pm1004PerfUpPast15CntTable_Object((1,3,6,1,4,1,20044,18,11,2,1,24))
if mibBuilder.loadTexts:pm1004PerfUpPast15CntTable.setStatus(_A)
_Pm1004PerfUpPast15CntEntry_Object=MibTableRow
pm1004PerfUpPast15CntEntry=_Pm1004PerfUpPast15CntEntry_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1))
pm1004PerfUpPast15CntEntry.setIndexNames((0,_C,_Ai))
if mibBuilder.loadTexts:pm1004PerfUpPast15CntEntry.setStatus(_A)
class _Pm1004PerfUpPast15CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfUpPast15CntIndex_Type.__name__=_D
_Pm1004PerfUpPast15CntIndex_Object=MibTableColumn
pm1004PerfUpPast15CntIndex=_Pm1004PerfUpPast15CntIndex_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,1),_Pm1004PerfUpPast15CntIndex_Type())
pm1004PerfUpPast15CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntIndex.setStatus(_A)
_Pm1004PerfUpPast15CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfUpPast15CntInvCvPortn_Object=MibTableColumn
pm1004PerfUpPast15CntInvCvPortn=_Pm1004PerfUpPast15CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,2),_Pm1004PerfUpPast15CntInvCvPortn_Type())
pm1004PerfUpPast15CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntInvCvPortn.setStatus(_A)
_Pm1004PerfUpPast15CntCvValuePortn_Type=Unsigned32
_Pm1004PerfUpPast15CntCvValuePortn_Object=MibTableColumn
pm1004PerfUpPast15CntCvValuePortn=_Pm1004PerfUpPast15CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,3),_Pm1004PerfUpPast15CntCvValuePortn_Type())
pm1004PerfUpPast15CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntCvValuePortn.setStatus(_A)
_Pm1004PerfUpPast15CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfUpPast15CntInvEsPortn_Object=MibTableColumn
pm1004PerfUpPast15CntInvEsPortn=_Pm1004PerfUpPast15CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,4),_Pm1004PerfUpPast15CntInvEsPortn_Type())
pm1004PerfUpPast15CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntInvEsPortn.setStatus(_A)
_Pm1004PerfUpPast15CntEsValuePortn_Type=Unsigned32
_Pm1004PerfUpPast15CntEsValuePortn_Object=MibTableColumn
pm1004PerfUpPast15CntEsValuePortn=_Pm1004PerfUpPast15CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,5),_Pm1004PerfUpPast15CntEsValuePortn_Type())
pm1004PerfUpPast15CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntEsValuePortn.setStatus(_A)
_Pm1004PerfUpPast15CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfUpPast15CntInvSesPortn_Object=MibTableColumn
pm1004PerfUpPast15CntInvSesPortn=_Pm1004PerfUpPast15CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,6),_Pm1004PerfUpPast15CntInvSesPortn_Type())
pm1004PerfUpPast15CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntInvSesPortn.setStatus(_A)
_Pm1004PerfUpPast15CntSesValuePortn_Type=Unsigned32
_Pm1004PerfUpPast15CntSesValuePortn_Object=MibTableColumn
pm1004PerfUpPast15CntSesValuePortn=_Pm1004PerfUpPast15CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,7),_Pm1004PerfUpPast15CntSesValuePortn_Type())
pm1004PerfUpPast15CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntSesValuePortn.setStatus(_A)
_Pm1004PerfUpPast15CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfUpPast15CntInvSefsPortn_Object=MibTableColumn
pm1004PerfUpPast15CntInvSefsPortn=_Pm1004PerfUpPast15CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,8),_Pm1004PerfUpPast15CntInvSefsPortn_Type())
pm1004PerfUpPast15CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntInvSefsPortn.setStatus(_A)
_Pm1004PerfUpPast15CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfUpPast15CntSefsValuePortn_Object=MibTableColumn
pm1004PerfUpPast15CntSefsValuePortn=_Pm1004PerfUpPast15CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,9),_Pm1004PerfUpPast15CntSefsValuePortn_Type())
pm1004PerfUpPast15CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntSefsValuePortn.setStatus(_A)
_Pm1004PerfUpPast15CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfUpPast15CntInvUasPortn_Object=MibTableColumn
pm1004PerfUpPast15CntInvUasPortn=_Pm1004PerfUpPast15CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,10),_Pm1004PerfUpPast15CntInvUasPortn_Type())
pm1004PerfUpPast15CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntInvUasPortn.setStatus(_A)
_Pm1004PerfUpPast15CntUasValuePortn_Type=Unsigned32
_Pm1004PerfUpPast15CntUasValuePortn_Object=MibTableColumn
pm1004PerfUpPast15CntUasValuePortn=_Pm1004PerfUpPast15CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,24,1,11),_Pm1004PerfUpPast15CntUasValuePortn_Type())
pm1004PerfUpPast15CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast15CntUasValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntTable_Object=MibTable
pm1004PerfUpCurrent24CntTable=_Pm1004PerfUpCurrent24CntTable_Object((1,3,6,1,4,1,20044,18,11,2,1,32))
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntTable.setStatus(_A)
_Pm1004PerfUpCurrent24CntEntry_Object=MibTableRow
pm1004PerfUpCurrent24CntEntry=_Pm1004PerfUpCurrent24CntEntry_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1))
pm1004PerfUpCurrent24CntEntry.setIndexNames((0,_C,_Aj))
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntEntry.setStatus(_A)
class _Pm1004PerfUpCurrent24CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfUpCurrent24CntIndex_Type.__name__=_D
_Pm1004PerfUpCurrent24CntIndex_Object=MibTableColumn
pm1004PerfUpCurrent24CntIndex=_Pm1004PerfUpCurrent24CntIndex_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,1),_Pm1004PerfUpCurrent24CntIndex_Type())
pm1004PerfUpCurrent24CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntIndex.setStatus(_A)
_Pm1004PerfUpCurrent24CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent24CntInvCvPortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntInvCvPortn=_Pm1004PerfUpCurrent24CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,2),_Pm1004PerfUpCurrent24CntInvCvPortn_Type())
pm1004PerfUpCurrent24CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntInvCvPortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntCvValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent24CntCvValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntCvValuePortn=_Pm1004PerfUpCurrent24CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,3),_Pm1004PerfUpCurrent24CntCvValuePortn_Type())
pm1004PerfUpCurrent24CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntCvValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent24CntInvEsPortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntInvEsPortn=_Pm1004PerfUpCurrent24CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,4),_Pm1004PerfUpCurrent24CntInvEsPortn_Type())
pm1004PerfUpCurrent24CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntInvEsPortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntEsValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent24CntEsValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntEsValuePortn=_Pm1004PerfUpCurrent24CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,5),_Pm1004PerfUpCurrent24CntEsValuePortn_Type())
pm1004PerfUpCurrent24CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntEsValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent24CntInvSesPortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntInvSesPortn=_Pm1004PerfUpCurrent24CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,6),_Pm1004PerfUpCurrent24CntInvSesPortn_Type())
pm1004PerfUpCurrent24CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntInvSesPortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntSesValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent24CntSesValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntSesValuePortn=_Pm1004PerfUpCurrent24CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,7),_Pm1004PerfUpCurrent24CntSesValuePortn_Type())
pm1004PerfUpCurrent24CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntSesValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent24CntInvSefsPortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntInvSefsPortn=_Pm1004PerfUpCurrent24CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,8),_Pm1004PerfUpCurrent24CntInvSefsPortn_Type())
pm1004PerfUpCurrent24CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntInvSefsPortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent24CntSefsValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntSefsValuePortn=_Pm1004PerfUpCurrent24CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,9),_Pm1004PerfUpCurrent24CntSefsValuePortn_Type())
pm1004PerfUpCurrent24CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntSefsValuePortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfUpCurrent24CntInvUasPortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntInvUasPortn=_Pm1004PerfUpCurrent24CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,10),_Pm1004PerfUpCurrent24CntInvUasPortn_Type())
pm1004PerfUpCurrent24CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntInvUasPortn.setStatus(_A)
_Pm1004PerfUpCurrent24CntUasValuePortn_Type=Unsigned32
_Pm1004PerfUpCurrent24CntUasValuePortn_Object=MibTableColumn
pm1004PerfUpCurrent24CntUasValuePortn=_Pm1004PerfUpCurrent24CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,32,1,11),_Pm1004PerfUpCurrent24CntUasValuePortn_Type())
pm1004PerfUpCurrent24CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpCurrent24CntUasValuePortn.setStatus(_A)
_Pm1004PerfUpPast24CntTable_Object=MibTable
pm1004PerfUpPast24CntTable=_Pm1004PerfUpPast24CntTable_Object((1,3,6,1,4,1,20044,18,11,2,1,40))
if mibBuilder.loadTexts:pm1004PerfUpPast24CntTable.setStatus(_A)
_Pm1004PerfUpPast24CntEntry_Object=MibTableRow
pm1004PerfUpPast24CntEntry=_Pm1004PerfUpPast24CntEntry_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1))
pm1004PerfUpPast24CntEntry.setIndexNames((0,_C,_Ak))
if mibBuilder.loadTexts:pm1004PerfUpPast24CntEntry.setStatus(_A)
class _Pm1004PerfUpPast24CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfUpPast24CntIndex_Type.__name__=_D
_Pm1004PerfUpPast24CntIndex_Object=MibTableColumn
pm1004PerfUpPast24CntIndex=_Pm1004PerfUpPast24CntIndex_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,1),_Pm1004PerfUpPast24CntIndex_Type())
pm1004PerfUpPast24CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntIndex.setStatus(_A)
_Pm1004PerfUpPast24CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfUpPast24CntInvCvPortn_Object=MibTableColumn
pm1004PerfUpPast24CntInvCvPortn=_Pm1004PerfUpPast24CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,2),_Pm1004PerfUpPast24CntInvCvPortn_Type())
pm1004PerfUpPast24CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntInvCvPortn.setStatus(_A)
_Pm1004PerfUpPast24CntCvValuePortn_Type=Unsigned32
_Pm1004PerfUpPast24CntCvValuePortn_Object=MibTableColumn
pm1004PerfUpPast24CntCvValuePortn=_Pm1004PerfUpPast24CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,3),_Pm1004PerfUpPast24CntCvValuePortn_Type())
pm1004PerfUpPast24CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntCvValuePortn.setStatus(_A)
_Pm1004PerfUpPast24CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfUpPast24CntInvEsPortn_Object=MibTableColumn
pm1004PerfUpPast24CntInvEsPortn=_Pm1004PerfUpPast24CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,4),_Pm1004PerfUpPast24CntInvEsPortn_Type())
pm1004PerfUpPast24CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntInvEsPortn.setStatus(_A)
_Pm1004PerfUpPast24CntEsValuePortn_Type=Unsigned32
_Pm1004PerfUpPast24CntEsValuePortn_Object=MibTableColumn
pm1004PerfUpPast24CntEsValuePortn=_Pm1004PerfUpPast24CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,5),_Pm1004PerfUpPast24CntEsValuePortn_Type())
pm1004PerfUpPast24CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntEsValuePortn.setStatus(_A)
_Pm1004PerfUpPast24CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfUpPast24CntInvSesPortn_Object=MibTableColumn
pm1004PerfUpPast24CntInvSesPortn=_Pm1004PerfUpPast24CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,6),_Pm1004PerfUpPast24CntInvSesPortn_Type())
pm1004PerfUpPast24CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntInvSesPortn.setStatus(_A)
_Pm1004PerfUpPast24CntSesValuePortn_Type=Unsigned32
_Pm1004PerfUpPast24CntSesValuePortn_Object=MibTableColumn
pm1004PerfUpPast24CntSesValuePortn=_Pm1004PerfUpPast24CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,7),_Pm1004PerfUpPast24CntSesValuePortn_Type())
pm1004PerfUpPast24CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntSesValuePortn.setStatus(_A)
_Pm1004PerfUpPast24CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfUpPast24CntInvSefsPortn_Object=MibTableColumn
pm1004PerfUpPast24CntInvSefsPortn=_Pm1004PerfUpPast24CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,8),_Pm1004PerfUpPast24CntInvSefsPortn_Type())
pm1004PerfUpPast24CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntInvSefsPortn.setStatus(_A)
_Pm1004PerfUpPast24CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfUpPast24CntSefsValuePortn_Object=MibTableColumn
pm1004PerfUpPast24CntSefsValuePortn=_Pm1004PerfUpPast24CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,9),_Pm1004PerfUpPast24CntSefsValuePortn_Type())
pm1004PerfUpPast24CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntSefsValuePortn.setStatus(_A)
_Pm1004PerfUpPast24CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfUpPast24CntInvUasPortn_Object=MibTableColumn
pm1004PerfUpPast24CntInvUasPortn=_Pm1004PerfUpPast24CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,10),_Pm1004PerfUpPast24CntInvUasPortn_Type())
pm1004PerfUpPast24CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntInvUasPortn.setStatus(_A)
_Pm1004PerfUpPast24CntUasValuePortn_Type=Unsigned32
_Pm1004PerfUpPast24CntUasValuePortn_Object=MibTableColumn
pm1004PerfUpPast24CntUasValuePortn=_Pm1004PerfUpPast24CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,2,1,40,1,11),_Pm1004PerfUpPast24CntUasValuePortn_Type())
pm1004PerfUpPast24CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfUpPast24CntUasValuePortn.setStatus(_A)
_Pm1004MonClientTraceIdentifier_ObjectIdentity=ObjectIdentity
pm1004MonClientTraceIdentifier=_Pm1004MonClientTraceIdentifier_ObjectIdentity((1,3,6,1,4,1,20044,18,11,2,2))
_Pm1004Almj0AlarmTable_Object=MibTable
pm1004Almj0AlarmTable=_Pm1004Almj0AlarmTable_Object((1,3,6,1,4,1,20044,18,11,2,2,2112))
if mibBuilder.loadTexts:pm1004Almj0AlarmTable.setStatus(_A)
_Pm1004Almj0AlarmEntry_Object=MibTableRow
pm1004Almj0AlarmEntry=_Pm1004Almj0AlarmEntry_Object((1,3,6,1,4,1,20044,18,11,2,2,2112,1))
pm1004Almj0AlarmEntry.setIndexNames((0,_C,_Al))
if mibBuilder.loadTexts:pm1004Almj0AlarmEntry.setStatus(_A)
class _Pm1004Almj0AlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004Almj0AlarmIndex_Type.__name__=_D
_Pm1004Almj0AlarmIndex_Object=MibTableColumn
pm1004Almj0AlarmIndex=_Pm1004Almj0AlarmIndex_Object((1,3,6,1,4,1,20044,18,11,2,2,2112,1,1),_Pm1004Almj0AlarmIndex_Type())
pm1004Almj0AlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004Almj0AlarmIndex.setStatus(_A)
_Pm1004AlmJ0TimAlarmPortn_Type=EkiOnOff
_Pm1004AlmJ0TimAlarmPortn_Object=MibTableColumn
pm1004AlmJ0TimAlarmPortn=_Pm1004AlmJ0TimAlarmPortn_Object((1,3,6,1,4,1,20044,18,11,2,2,2112,1,2),_Pm1004AlmJ0TimAlarmPortn_Type())
pm1004AlmJ0TimAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmJ0TimAlarmPortn.setStatus(_A)
_Pm1004AlmJ0TiiAlarmPortn_Type=EkiOnOff
_Pm1004AlmJ0TiiAlarmPortn_Object=MibTableColumn
pm1004AlmJ0TiiAlarmPortn=_Pm1004AlmJ0TiiAlarmPortn_Object((1,3,6,1,4,1,20044,18,11,2,2,2112,1,3),_Pm1004AlmJ0TiiAlarmPortn_Type())
pm1004AlmJ0TiiAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmJ0TiiAlarmPortn.setStatus(_A)
_Pm1004AlmCrc7ErrorPortn_Type=EkiOnOff
_Pm1004AlmCrc7ErrorPortn_Object=MibTableColumn
pm1004AlmCrc7ErrorPortn=_Pm1004AlmCrc7ErrorPortn_Object((1,3,6,1,4,1,20044,18,11,2,2,2112,1,4),_Pm1004AlmCrc7ErrorPortn_Type())
pm1004AlmCrc7ErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004AlmCrc7ErrorPortn.setStatus(_A)
_Pm1004MonLine_ObjectIdentity=ObjectIdentity
pm1004MonLine=_Pm1004MonLine_ObjectIdentity((1,3,6,1,4,1,20044,18,11,3))
_Pm1004MonLinePerformance_ObjectIdentity=ObjectIdentity
pm1004MonLinePerformance=_Pm1004MonLinePerformance_ObjectIdentity((1,3,6,1,4,1,20044,18,11,3,1))
_Pm1004PerfLineCurrent15CntTable_Object=MibTable
pm1004PerfLineCurrent15CntTable=_Pm1004PerfLineCurrent15CntTable_Object((1,3,6,1,4,1,20044,18,11,3,1,128))
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntTable.setStatus(_A)
_Pm1004PerfLineCurrent15CntEntry_Object=MibTableRow
pm1004PerfLineCurrent15CntEntry=_Pm1004PerfLineCurrent15CntEntry_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1))
pm1004PerfLineCurrent15CntEntry.setIndexNames((0,_C,_Am))
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntEntry.setStatus(_A)
class _Pm1004PerfLineCurrent15CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfLineCurrent15CntIndex_Type.__name__=_D
_Pm1004PerfLineCurrent15CntIndex_Object=MibTableColumn
pm1004PerfLineCurrent15CntIndex=_Pm1004PerfLineCurrent15CntIndex_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,1),_Pm1004PerfLineCurrent15CntIndex_Type())
pm1004PerfLineCurrent15CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntIndex.setStatus(_A)
_Pm1004PerfLineCurrent15CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent15CntInvCvPortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntInvCvPortn=_Pm1004PerfLineCurrent15CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,2),_Pm1004PerfLineCurrent15CntInvCvPortn_Type())
pm1004PerfLineCurrent15CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntInvCvPortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntCvValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent15CntCvValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntCvValuePortn=_Pm1004PerfLineCurrent15CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,3),_Pm1004PerfLineCurrent15CntCvValuePortn_Type())
pm1004PerfLineCurrent15CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntCvValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent15CntInvEsPortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntInvEsPortn=_Pm1004PerfLineCurrent15CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,4),_Pm1004PerfLineCurrent15CntInvEsPortn_Type())
pm1004PerfLineCurrent15CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntInvEsPortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntEsValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent15CntEsValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntEsValuePortn=_Pm1004PerfLineCurrent15CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,5),_Pm1004PerfLineCurrent15CntEsValuePortn_Type())
pm1004PerfLineCurrent15CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntEsValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent15CntInvSesPortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntInvSesPortn=_Pm1004PerfLineCurrent15CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,6),_Pm1004PerfLineCurrent15CntInvSesPortn_Type())
pm1004PerfLineCurrent15CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntInvSesPortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntSesValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent15CntSesValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntSesValuePortn=_Pm1004PerfLineCurrent15CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,7),_Pm1004PerfLineCurrent15CntSesValuePortn_Type())
pm1004PerfLineCurrent15CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntSesValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent15CntInvSefsPortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntInvSefsPortn=_Pm1004PerfLineCurrent15CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,8),_Pm1004PerfLineCurrent15CntInvSefsPortn_Type())
pm1004PerfLineCurrent15CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntInvSefsPortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent15CntSefsValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntSefsValuePortn=_Pm1004PerfLineCurrent15CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,9),_Pm1004PerfLineCurrent15CntSefsValuePortn_Type())
pm1004PerfLineCurrent15CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntSefsValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent15CntInvUasPortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntInvUasPortn=_Pm1004PerfLineCurrent15CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,10),_Pm1004PerfLineCurrent15CntInvUasPortn_Type())
pm1004PerfLineCurrent15CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntInvUasPortn.setStatus(_A)
_Pm1004PerfLineCurrent15CntUasValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent15CntUasValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent15CntUasValuePortn=_Pm1004PerfLineCurrent15CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,128,1,11),_Pm1004PerfLineCurrent15CntUasValuePortn_Type())
pm1004PerfLineCurrent15CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent15CntUasValuePortn.setStatus(_A)
_Pm1004PerfLinePast15CntTable_Object=MibTable
pm1004PerfLinePast15CntTable=_Pm1004PerfLinePast15CntTable_Object((1,3,6,1,4,1,20044,18,11,3,1,129))
if mibBuilder.loadTexts:pm1004PerfLinePast15CntTable.setStatus(_A)
_Pm1004PerfLinePast15CntEntry_Object=MibTableRow
pm1004PerfLinePast15CntEntry=_Pm1004PerfLinePast15CntEntry_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1))
pm1004PerfLinePast15CntEntry.setIndexNames((0,_C,_An))
if mibBuilder.loadTexts:pm1004PerfLinePast15CntEntry.setStatus(_A)
class _Pm1004PerfLinePast15CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfLinePast15CntIndex_Type.__name__=_D
_Pm1004PerfLinePast15CntIndex_Object=MibTableColumn
pm1004PerfLinePast15CntIndex=_Pm1004PerfLinePast15CntIndex_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,1),_Pm1004PerfLinePast15CntIndex_Type())
pm1004PerfLinePast15CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntIndex.setStatus(_A)
_Pm1004PerfLinePast15CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfLinePast15CntInvCvPortn_Object=MibTableColumn
pm1004PerfLinePast15CntInvCvPortn=_Pm1004PerfLinePast15CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,2),_Pm1004PerfLinePast15CntInvCvPortn_Type())
pm1004PerfLinePast15CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntInvCvPortn.setStatus(_A)
_Pm1004PerfLinePast15CntCvValuePortn_Type=Unsigned32
_Pm1004PerfLinePast15CntCvValuePortn_Object=MibTableColumn
pm1004PerfLinePast15CntCvValuePortn=_Pm1004PerfLinePast15CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,3),_Pm1004PerfLinePast15CntCvValuePortn_Type())
pm1004PerfLinePast15CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntCvValuePortn.setStatus(_A)
_Pm1004PerfLinePast15CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfLinePast15CntInvEsPortn_Object=MibTableColumn
pm1004PerfLinePast15CntInvEsPortn=_Pm1004PerfLinePast15CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,4),_Pm1004PerfLinePast15CntInvEsPortn_Type())
pm1004PerfLinePast15CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntInvEsPortn.setStatus(_A)
_Pm1004PerfLinePast15CntEsValuePortn_Type=Unsigned32
_Pm1004PerfLinePast15CntEsValuePortn_Object=MibTableColumn
pm1004PerfLinePast15CntEsValuePortn=_Pm1004PerfLinePast15CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,5),_Pm1004PerfLinePast15CntEsValuePortn_Type())
pm1004PerfLinePast15CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntEsValuePortn.setStatus(_A)
_Pm1004PerfLinePast15CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfLinePast15CntInvSesPortn_Object=MibTableColumn
pm1004PerfLinePast15CntInvSesPortn=_Pm1004PerfLinePast15CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,6),_Pm1004PerfLinePast15CntInvSesPortn_Type())
pm1004PerfLinePast15CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntInvSesPortn.setStatus(_A)
_Pm1004PerfLinePast15CntSesValuePortn_Type=Unsigned32
_Pm1004PerfLinePast15CntSesValuePortn_Object=MibTableColumn
pm1004PerfLinePast15CntSesValuePortn=_Pm1004PerfLinePast15CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,7),_Pm1004PerfLinePast15CntSesValuePortn_Type())
pm1004PerfLinePast15CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntSesValuePortn.setStatus(_A)
_Pm1004PerfLinePast15CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfLinePast15CntInvSefsPortn_Object=MibTableColumn
pm1004PerfLinePast15CntInvSefsPortn=_Pm1004PerfLinePast15CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,8),_Pm1004PerfLinePast15CntInvSefsPortn_Type())
pm1004PerfLinePast15CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntInvSefsPortn.setStatus(_A)
_Pm1004PerfLinePast15CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfLinePast15CntSefsValuePortn_Object=MibTableColumn
pm1004PerfLinePast15CntSefsValuePortn=_Pm1004PerfLinePast15CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,9),_Pm1004PerfLinePast15CntSefsValuePortn_Type())
pm1004PerfLinePast15CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntSefsValuePortn.setStatus(_A)
_Pm1004PerfLinePast15CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfLinePast15CntInvUasPortn_Object=MibTableColumn
pm1004PerfLinePast15CntInvUasPortn=_Pm1004PerfLinePast15CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,10),_Pm1004PerfLinePast15CntInvUasPortn_Type())
pm1004PerfLinePast15CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntInvUasPortn.setStatus(_A)
_Pm1004PerfLinePast15CntUasValuePortn_Type=Unsigned32
_Pm1004PerfLinePast15CntUasValuePortn_Object=MibTableColumn
pm1004PerfLinePast15CntUasValuePortn=_Pm1004PerfLinePast15CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,129,1,11),_Pm1004PerfLinePast15CntUasValuePortn_Type())
pm1004PerfLinePast15CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast15CntUasValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntTable_Object=MibTable
pm1004PerfLineCurrent24CntTable=_Pm1004PerfLineCurrent24CntTable_Object((1,3,6,1,4,1,20044,18,11,3,1,130))
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntTable.setStatus(_A)
_Pm1004PerfLineCurrent24CntEntry_Object=MibTableRow
pm1004PerfLineCurrent24CntEntry=_Pm1004PerfLineCurrent24CntEntry_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1))
pm1004PerfLineCurrent24CntEntry.setIndexNames((0,_C,_Ao))
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntEntry.setStatus(_A)
class _Pm1004PerfLineCurrent24CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfLineCurrent24CntIndex_Type.__name__=_D
_Pm1004PerfLineCurrent24CntIndex_Object=MibTableColumn
pm1004PerfLineCurrent24CntIndex=_Pm1004PerfLineCurrent24CntIndex_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,1),_Pm1004PerfLineCurrent24CntIndex_Type())
pm1004PerfLineCurrent24CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntIndex.setStatus(_A)
_Pm1004PerfLineCurrent24CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent24CntInvCvPortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntInvCvPortn=_Pm1004PerfLineCurrent24CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,2),_Pm1004PerfLineCurrent24CntInvCvPortn_Type())
pm1004PerfLineCurrent24CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntInvCvPortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntCvValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent24CntCvValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntCvValuePortn=_Pm1004PerfLineCurrent24CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,3),_Pm1004PerfLineCurrent24CntCvValuePortn_Type())
pm1004PerfLineCurrent24CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntCvValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent24CntInvEsPortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntInvEsPortn=_Pm1004PerfLineCurrent24CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,4),_Pm1004PerfLineCurrent24CntInvEsPortn_Type())
pm1004PerfLineCurrent24CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntInvEsPortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntEsValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent24CntEsValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntEsValuePortn=_Pm1004PerfLineCurrent24CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,5),_Pm1004PerfLineCurrent24CntEsValuePortn_Type())
pm1004PerfLineCurrent24CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntEsValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent24CntInvSesPortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntInvSesPortn=_Pm1004PerfLineCurrent24CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,6),_Pm1004PerfLineCurrent24CntInvSesPortn_Type())
pm1004PerfLineCurrent24CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntInvSesPortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntSesValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent24CntSesValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntSesValuePortn=_Pm1004PerfLineCurrent24CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,7),_Pm1004PerfLineCurrent24CntSesValuePortn_Type())
pm1004PerfLineCurrent24CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntSesValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent24CntInvSefsPortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntInvSefsPortn=_Pm1004PerfLineCurrent24CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,8),_Pm1004PerfLineCurrent24CntInvSefsPortn_Type())
pm1004PerfLineCurrent24CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntInvSefsPortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent24CntSefsValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntSefsValuePortn=_Pm1004PerfLineCurrent24CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,9),_Pm1004PerfLineCurrent24CntSefsValuePortn_Type())
pm1004PerfLineCurrent24CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntSefsValuePortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfLineCurrent24CntInvUasPortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntInvUasPortn=_Pm1004PerfLineCurrent24CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,10),_Pm1004PerfLineCurrent24CntInvUasPortn_Type())
pm1004PerfLineCurrent24CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntInvUasPortn.setStatus(_A)
_Pm1004PerfLineCurrent24CntUasValuePortn_Type=Unsigned32
_Pm1004PerfLineCurrent24CntUasValuePortn_Object=MibTableColumn
pm1004PerfLineCurrent24CntUasValuePortn=_Pm1004PerfLineCurrent24CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,130,1,11),_Pm1004PerfLineCurrent24CntUasValuePortn_Type())
pm1004PerfLineCurrent24CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLineCurrent24CntUasValuePortn.setStatus(_A)
_Pm1004PerfLinePast24CntTable_Object=MibTable
pm1004PerfLinePast24CntTable=_Pm1004PerfLinePast24CntTable_Object((1,3,6,1,4,1,20044,18,11,3,1,131))
if mibBuilder.loadTexts:pm1004PerfLinePast24CntTable.setStatus(_A)
_Pm1004PerfLinePast24CntEntry_Object=MibTableRow
pm1004PerfLinePast24CntEntry=_Pm1004PerfLinePast24CntEntry_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1))
pm1004PerfLinePast24CntEntry.setIndexNames((0,_C,_Ap))
if mibBuilder.loadTexts:pm1004PerfLinePast24CntEntry.setStatus(_A)
class _Pm1004PerfLinePast24CntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1004PerfLinePast24CntIndex_Type.__name__=_D
_Pm1004PerfLinePast24CntIndex_Object=MibTableColumn
pm1004PerfLinePast24CntIndex=_Pm1004PerfLinePast24CntIndex_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,1),_Pm1004PerfLinePast24CntIndex_Type())
pm1004PerfLinePast24CntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntIndex.setStatus(_A)
_Pm1004PerfLinePast24CntInvCvPortn_Type=EkiOnOff
_Pm1004PerfLinePast24CntInvCvPortn_Object=MibTableColumn
pm1004PerfLinePast24CntInvCvPortn=_Pm1004PerfLinePast24CntInvCvPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,2),_Pm1004PerfLinePast24CntInvCvPortn_Type())
pm1004PerfLinePast24CntInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntInvCvPortn.setStatus(_A)
_Pm1004PerfLinePast24CntCvValuePortn_Type=Unsigned32
_Pm1004PerfLinePast24CntCvValuePortn_Object=MibTableColumn
pm1004PerfLinePast24CntCvValuePortn=_Pm1004PerfLinePast24CntCvValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,3),_Pm1004PerfLinePast24CntCvValuePortn_Type())
pm1004PerfLinePast24CntCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntCvValuePortn.setStatus(_A)
_Pm1004PerfLinePast24CntInvEsPortn_Type=EkiOnOff
_Pm1004PerfLinePast24CntInvEsPortn_Object=MibTableColumn
pm1004PerfLinePast24CntInvEsPortn=_Pm1004PerfLinePast24CntInvEsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,4),_Pm1004PerfLinePast24CntInvEsPortn_Type())
pm1004PerfLinePast24CntInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntInvEsPortn.setStatus(_A)
_Pm1004PerfLinePast24CntEsValuePortn_Type=Unsigned32
_Pm1004PerfLinePast24CntEsValuePortn_Object=MibTableColumn
pm1004PerfLinePast24CntEsValuePortn=_Pm1004PerfLinePast24CntEsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,5),_Pm1004PerfLinePast24CntEsValuePortn_Type())
pm1004PerfLinePast24CntEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntEsValuePortn.setStatus(_A)
_Pm1004PerfLinePast24CntInvSesPortn_Type=EkiOnOff
_Pm1004PerfLinePast24CntInvSesPortn_Object=MibTableColumn
pm1004PerfLinePast24CntInvSesPortn=_Pm1004PerfLinePast24CntInvSesPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,6),_Pm1004PerfLinePast24CntInvSesPortn_Type())
pm1004PerfLinePast24CntInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntInvSesPortn.setStatus(_A)
_Pm1004PerfLinePast24CntSesValuePortn_Type=Unsigned32
_Pm1004PerfLinePast24CntSesValuePortn_Object=MibTableColumn
pm1004PerfLinePast24CntSesValuePortn=_Pm1004PerfLinePast24CntSesValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,7),_Pm1004PerfLinePast24CntSesValuePortn_Type())
pm1004PerfLinePast24CntSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntSesValuePortn.setStatus(_A)
_Pm1004PerfLinePast24CntInvSefsPortn_Type=EkiOnOff
_Pm1004PerfLinePast24CntInvSefsPortn_Object=MibTableColumn
pm1004PerfLinePast24CntInvSefsPortn=_Pm1004PerfLinePast24CntInvSefsPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,8),_Pm1004PerfLinePast24CntInvSefsPortn_Type())
pm1004PerfLinePast24CntInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntInvSefsPortn.setStatus(_A)
_Pm1004PerfLinePast24CntSefsValuePortn_Type=Unsigned32
_Pm1004PerfLinePast24CntSefsValuePortn_Object=MibTableColumn
pm1004PerfLinePast24CntSefsValuePortn=_Pm1004PerfLinePast24CntSefsValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,9),_Pm1004PerfLinePast24CntSefsValuePortn_Type())
pm1004PerfLinePast24CntSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntSefsValuePortn.setStatus(_A)
_Pm1004PerfLinePast24CntInvUasPortn_Type=EkiOnOff
_Pm1004PerfLinePast24CntInvUasPortn_Object=MibTableColumn
pm1004PerfLinePast24CntInvUasPortn=_Pm1004PerfLinePast24CntInvUasPortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,10),_Pm1004PerfLinePast24CntInvUasPortn_Type())
pm1004PerfLinePast24CntInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntInvUasPortn.setStatus(_A)
_Pm1004PerfLinePast24CntUasValuePortn_Type=Unsigned32
_Pm1004PerfLinePast24CntUasValuePortn_Object=MibTableColumn
pm1004PerfLinePast24CntUasValuePortn=_Pm1004PerfLinePast24CntUasValuePortn_Object((1,3,6,1,4,1,20044,18,11,3,1,131,1,11),_Pm1004PerfLinePast24CntUasValuePortn_Type())
pm1004PerfLinePast24CntUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1004PerfLinePast24CntUasValuePortn.setStatus(_A)
_Pm1004MonLineTraceIdentifier_ObjectIdentity=ObjectIdentity
pm1004MonLineTraceIdentifier=_Pm1004MonLineTraceIdentifier_ObjectIdentity((1,3,6,1,4,1,20044,18,11,3,2))
pm1004LineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,30))
pm1004LineTrapNotUrgentGoesOn.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1004LineTrapNotUrgentGoesOn.setStatus(_A)
pm1004LineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,31))
pm1004LineTrapNotUrgentGoesOff.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1004LineTrapNotUrgentGoesOff.setStatus(_A)
pm1004LineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,32))
pm1004LineTrapUrgentGoesOn.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1004LineTrapUrgentGoesOn.setStatus(_A)
pm1004LineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,33))
pm1004LineTrapUrgentGoesOff.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1004LineTrapUrgentGoesOff.setStatus(_A)
pm1004LineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,34))
pm1004LineTrapCritGoesOn.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1004LineTrapCritGoesOn.setStatus(_A)
pm1004LineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,35))
pm1004LineTrapCritGoesOff.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1004LineTrapCritGoesOff.setStatus(_A)
pm1004ClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,40))
pm1004ClientTrapNotUrgentGoesOn.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1004ClientTrapNotUrgentGoesOn.setStatus(_A)
pm1004ClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,41))
pm1004ClientTrapNotUrgentGoesOff.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1004ClientTrapNotUrgentGoesOff.setStatus(_A)
pm1004ClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,42))
pm1004ClientTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1004ClientTrapUrgentGoesOn.setStatus(_A)
pm1004ClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,43))
pm1004ClientTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1004ClientTrapUrgentGoesOff.setStatus(_A)
pm1004ClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,44))
pm1004ClientTrapCritGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1004ClientTrapCritGoesOn.setStatus(_A)
pm1004ClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,45))
pm1004ClientTrapCritGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1004ClientTrapCritGoesOff.setStatus(_A)
pm1004PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,18,10,50))
pm1004PowerTrapUrgentGoesOn.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pm1004PowerTrapUrgentGoesOn.setStatus(_A)
pm1004PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,18,10,51))
pm1004PowerTrapUrgentGoesOff.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pm1004PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Pm1004OtxMode':Pm1004OtxMode,'Pm1004OtxGrid':Pm1004OtxGrid,'Pm1004AdjustValue':Pm1004AdjustValue,'Pm1004OtxChannel':Pm1004OtxChannel,'modulePm1004':modulePm1004,'pm1004alarms':pm1004alarms,'pm1004AlmOther':pm1004AlmOther,'pm1004AlmOtherNurg':pm1004AlmOtherNurg,'pm1004AlmsynthAlm2':pm1004AlmsynthAlm2,'pm1004AlmConfTableSave':pm1004AlmConfTableSave,'pm1004AlmInvUpload':pm1004AlmInvUpload,'pm1004AlmConfTableLoad':pm1004AlmConfTableLoad,'pm1004AlmCorrelatOff':pm1004AlmCorrelatOff,'pm1004AlmMaintenanceOn':pm1004AlmMaintenanceOn,'pm1004AlmOtherUrg':pm1004AlmOtherUrg,'pm1004AlmmodInitFailLevel2':pm1004AlmmodInitFailLevel2,'pm1004AlmLedFail':pm1004AlmLedFail,'pm1004AlmNextColdBootForced':pm1004AlmNextColdBootForced,'pm1004AlmBootUndone':pm1004AlmBootUndone,'pm1004AlmResetHwInitFail':pm1004AlmResetHwInitFail,'pm1004AlmSwInitFail':pm1004AlmSwInitFail,'pm1004AlmmodInitFailLevel3':pm1004AlmmodInitFailLevel3,'pm1004AlmGwIdentFail':pm1004AlmGwIdentFail,'pm1004AlmObmTypeReadFail':pm1004AlmObmTypeReadFail,'pm1004AlmInitModuleFail':pm1004AlmInitModuleFail,'pm1004AlmXfp1InitFail':pm1004AlmXfp1InitFail,'pm1004AlmXfp2InitFail':pm1004AlmXfp2InitFail,'pm1004AlmLine1InitFail':pm1004AlmLine1InitFail,'pm1004AlmLine2InitFail':pm1004AlmLine2InitFail,'pm1004AlmClient1InitFail':pm1004AlmClient1InitFail,'pm1004AlmClient2InitFail':pm1004AlmClient2InitFail,'pm1004AlmClient3InitFail':pm1004AlmClient3InitFail,'pm1004AlmClient4InitFail':pm1004AlmClient4InitFail,'pm1004AlmOtherCrit':pm1004AlmOtherCrit,'pm1004AlmsynthAlm0':pm1004AlmsynthAlm0,'pm1004AlmModGlobFail':pm1004AlmModGlobFail,_U:pm1004AlmDefFuseA,_T:pm1004AlmDefFuseB,'pm1004AlmClient':pm1004AlmClient,'pm1004AlmClientNurg':pm1004AlmClientNurg,'pm1004AlmsfpWarnDdmTable':pm1004AlmsfpWarnDdmTable,'pm1004AlmsfpWarnDdmEntry':pm1004AlmsfpWarnDdmEntry,_V:pm1004AlmsfpWarnDdmIndex,'pm1004AlmTxPwLowWngPortn':pm1004AlmTxPwLowWngPortn,'pm1004AlmTxPwrHighWngPortn':pm1004AlmTxPwrHighWngPortn,'pm1004AlmTxBiasLowWngPortn':pm1004AlmTxBiasLowWngPortn,'pm1004AlmTxBiasHighWngPortn':pm1004AlmTxBiasHighWngPortn,'pm1004AlmVccLowWngPortn':pm1004AlmVccLowWngPortn,'pm1004AlmVccHighWngPortn':pm1004AlmVccHighWngPortn,'pm1004AlmTempLowWngPortn':pm1004AlmTempLowWngPortn,'pm1004AlmTempHighWngPortn':pm1004AlmTempHighWngPortn,'pm1004AlmRxPwrLowWngPortn':pm1004AlmRxPwrLowWngPortn,'pm1004AlmRxPwrHighWngPortn':pm1004AlmRxPwrHighWngPortn,'pm1004Almk1K2ClientTable':pm1004Almk1K2ClientTable,'pm1004Almk1K2ClientEntry':pm1004Almk1K2ClientEntry,_W:pm1004Almk1K2ClientIndex,'pm1004Almk1K2ClientPortn':pm1004Almk1K2ClientPortn,'pm1004AlmClientUrg':pm1004AlmClientUrg,'pm1004AlmsfpAlmDdmTable':pm1004AlmsfpAlmDdmTable,'pm1004AlmsfpAlmDdmEntry':pm1004AlmsfpAlmDdmEntry,_X:pm1004AlmsfpAlmDdmIndex,'pm1004AlmTxPwrLowAlaPortn':pm1004AlmTxPwrLowAlaPortn,'pm1004AlmTxPwrHighAlaPortn':pm1004AlmTxPwrHighAlaPortn,'pm1004AlmTxBiasLowAlaPortn':pm1004AlmTxBiasLowAlaPortn,'pm1004AlmTxBiasHighAlaPortn':pm1004AlmTxBiasHighAlaPortn,'pm1004AlmVccLowAlaPortn':pm1004AlmVccLowAlaPortn,'pm1004AlmVccHighAlaPortn':pm1004AlmVccHighAlaPortn,'pm1004AlmTempLowAlaPortn':pm1004AlmTempLowAlaPortn,'pm1004AlmTempHighAlaPortn':pm1004AlmTempHighAlaPortn,'pm1004AlmRxPwrLowAlaPortn':pm1004AlmRxPwrLowAlaPortn,'pm1004AlmRxPwrHighAlaPortn':pm1004AlmRxPwrHighAlaPortn,'pm1004AlmClientCrit':pm1004AlmClientCrit,'pm1004AlmsynthAlmPortTable':pm1004AlmsynthAlmPortTable,'pm1004AlmsynthAlmPortEntry':pm1004AlmsynthAlmPortEntry,_Y:pm1004AlmsynthAlmPortIndex,'pm1004AlmSfpAbsentPortn':pm1004AlmSfpAbsentPortn,'pm1004AlmDdmAbsentPortn':pm1004AlmDdmAbsentPortn,_S:pm1004AlmHwFailAccPortn,'pm1004AlmDwLsdPortn':pm1004AlmDwLsdPortn,'pm1004AlmClientLocalOosPortn':pm1004AlmClientLocalOosPortn,'pm1004AlmClientRemoteOosPortn':pm1004AlmClientRemoteOosPortn,'pm1004AlmDwCaisPortn':pm1004AlmDwCaisPortn,_P:pm1004AlmSfpDdmWarningPortn,_Q:pm1004AlmSfpDdmAlmPortn,_R:pm1004AlmFailAccPortn,'pm1004AlmUpCsfPortn':pm1004AlmUpCsfPortn,'pm1004AlmaccessioAlmTable':pm1004AlmaccessioAlmTable,'pm1004AlmaccessioAlmEntry':pm1004AlmaccessioAlmEntry,_Z:pm1004AlmaccessioAlmIndex,'pm1004AlmDwLasFailPortn':pm1004AlmDwLasFailPortn,'pm1004AlmUpLosPortn':pm1004AlmUpLosPortn,'pm1004AlmmapperDeAlmTable':pm1004AlmmapperDeAlmTable,'pm1004AlmmapperDeAlmEntry':pm1004AlmmapperDeAlmEntry,_a:pm1004AlmmapperDeAlmIndex,'pm1004AlmUpAccOosPortn':pm1004AlmUpAccOosPortn,'pm1004AlmUpBufferOvlPortn':pm1004AlmUpBufferOvlPortn,'pm1004AlmDwCsfDetPortn':pm1004AlmDwCsfDetPortn,'pm1004AlmDwBufferOvlPortn':pm1004AlmDwBufferOvlPortn,'pm1004AlmaccessioSdhAlarmTable':pm1004AlmaccessioSdhAlarmTable,'pm1004AlmaccessioSdhAlarmEntry':pm1004AlmaccessioSdhAlarmEntry,_b:pm1004AlmaccessioSdhAlarmIndex,'pm1004AlmFifoErrPortn':pm1004AlmFifoErrPortn,'pm1004AlmRxLossOfLockPortn':pm1004AlmRxLossOfLockPortn,'pm1004AlmTxLossOfLockPortn':pm1004AlmTxLossOfLockPortn,'pm1004AlmClientAisDetPortn':pm1004AlmClientAisDetPortn,'pm1004AlmClientRdiDetPortn':pm1004AlmClientRdiDetPortn,'pm1004AlmClientOofPortn':pm1004AlmClientOofPortn,'pm1004AlmLine':pm1004AlmLine,'pm1004AlmLineNurg':pm1004AlmLineNurg,'pm1004AlmlineXfp1WarningsTable':pm1004AlmlineXfp1WarningsTable,'pm1004AlmlineXfp1WarningsEntry':pm1004AlmlineXfp1WarningsEntry,_c:pm1004AlmlineXfp1WarningsIndex,'pm1004AlmTxPowerLowWarningPortn':pm1004AlmTxPowerLowWarningPortn,'pm1004AlmTxPowerHighWarningPortn':pm1004AlmTxPowerHighWarningPortn,'pm1004AlmTxBiasLowWarningPortn':pm1004AlmTxBiasLowWarningPortn,'pm1004AlmTxBiasHighWarningPortn':pm1004AlmTxBiasHighWarningPortn,'pm1004AlmTempLowWarningPortn':pm1004AlmTempLowWarningPortn,'pm1004AlmTempHighWarningPortn':pm1004AlmTempHighWarningPortn,'pm1004AlmRxPowerLowWarningPortn':pm1004AlmRxPowerLowWarningPortn,'pm1004AlmRxPowerHighWarningPortn':pm1004AlmRxPowerHighWarningPortn,'pm1004AlmlineOtx1TlhWarningsTable':pm1004AlmlineOtx1TlhWarningsTable,'pm1004AlmlineOtx1TlhWarningsEntry':pm1004AlmlineOtx1TlhWarningsEntry,_d:pm1004AlmlineOtx1TlhWarningsIndex,'pm1004AlmLineModulatorAgingHighWarningPortn':pm1004AlmLineModulatorAgingHighWarningPortn,'pm1004AlmLineAgingHighWarningPortn':pm1004AlmLineAgingHighWarningPortn,'pm1004AlmLineFreqDevHighWarningPortn':pm1004AlmLineFreqDevHighWarningPortn,'pm1004AlmLineLaserTempHighWarningPortn':pm1004AlmLineLaserTempHighWarningPortn,'pm1004AlmLineUrg':pm1004AlmLineUrg,'pm1004AlmdfrmBerTable':pm1004AlmdfrmBerTable,'pm1004AlmdfrmBerEntry':pm1004AlmdfrmBerEntry,_e:pm1004AlmdfrmBerIndex,'pm1004AlmLineSignalDegradePortn':pm1004AlmLineSignalDegradePortn,'pm1004AlmLineSignalFailPortn':pm1004AlmLineSignalFailPortn,'pm1004AlmLineDegradePortn':pm1004AlmLineDegradePortn,'pm1004AlmlineXfp1AlarmTable':pm1004AlmlineXfp1AlarmTable,'pm1004AlmlineXfp1AlarmEntry':pm1004AlmlineXfp1AlarmEntry,_f:pm1004AlmlineXfp1AlarmIndex,'pm1004AlmTxPowerLowAlarmPortn':pm1004AlmTxPowerLowAlarmPortn,'pm1004AlmTxPowerHighAlarmPortn':pm1004AlmTxPowerHighAlarmPortn,'pm1004AlmTxBiasLowAlarmPortn':pm1004AlmTxBiasLowAlarmPortn,'pm1004AlmTxBiasHighAlarmPortn':pm1004AlmTxBiasHighAlarmPortn,'pm1004AlmTempLowAlarmPortn':pm1004AlmTempLowAlarmPortn,'pm1004AlmTempHighAlarmPortn':pm1004AlmTempHighAlarmPortn,'pm1004AlmRxPowerLowAlarmPortn':pm1004AlmRxPowerLowAlarmPortn,'pm1004AlmRxPowerHighAlarmPortn':pm1004AlmRxPowerHighAlarmPortn,'pm1004AlmlineXfp1SupplyAlarmTable':pm1004AlmlineXfp1SupplyAlarmTable,'pm1004AlmlineXfp1SupplyAlarmEntry':pm1004AlmlineXfp1SupplyAlarmEntry,_g:pm1004AlmlineXfp1SupplyAlarmIndex,'pm1004AlmVee5LowAlarmPortn':pm1004AlmVee5LowAlarmPortn,'pm1004AlmVee5HighAlarmPortn':pm1004AlmVee5HighAlarmPortn,'pm1004AlmVcc2LowAlarmPortn':pm1004AlmVcc2LowAlarmPortn,'pm1004AlmVcc2HighAlarmPortn':pm1004AlmVcc2HighAlarmPortn,'pm1004AlmVcc3LowAlarmPortn':pm1004AlmVcc3LowAlarmPortn,'pm1004AlmVcc3HighAlarmPortn':pm1004AlmVcc3HighAlarmPortn,'pm1004AlmVcc5LowAlarmPortn':pm1004AlmVcc5LowAlarmPortn,'pm1004AlmVcc5HighAlarmPortn':pm1004AlmVcc5HighAlarmPortn,'pm1004AlmVee5LowWarningPortn':pm1004AlmVee5LowWarningPortn,'pm1004AlmVee5HighWarningPortn':pm1004AlmVee5HighWarningPortn,'pm1004AlmVcc2LowWarningPortn':pm1004AlmVcc2LowWarningPortn,'pm1004AlmVcc2HighWarningPortn':pm1004AlmVcc2HighWarningPortn,'pm1004AlmVcc3LowWarningPortn':pm1004AlmVcc3LowWarningPortn,'pm1004AlmVcc3HighWarningPortn':pm1004AlmVcc3HighWarningPortn,'pm1004AlmVcc5LowWarningPortn':pm1004AlmVcc5LowWarningPortn,'pm1004AlmVcc5HighWarningPortn':pm1004AlmVcc5HighWarningPortn,'pm1004AlmlineOtx1TlhAlarmsTable':pm1004AlmlineOtx1TlhAlarmsTable,'pm1004AlmlineOtx1TlhAlarmsEntry':pm1004AlmlineOtx1TlhAlarmsEntry,_h:pm1004AlmlineOtx1TlhAlarmsIndex,'pm1004AlmLineModulatorAgingHighAlaPortn':pm1004AlmLineModulatorAgingHighAlaPortn,'pm1004AlmLineAgingHighAlaPortn':pm1004AlmLineAgingHighAlaPortn,'pm1004AlmLineCdrNotReadyPortn':pm1004AlmLineCdrNotReadyPortn,'pm1004AlmLineFreqDevHighAlaPortn':pm1004AlmLineFreqDevHighAlaPortn,'pm1004AlmLineLaserTempHighAlaPortn':pm1004AlmLineLaserTempHighAlaPortn,'pm1004AlmLineCrit':pm1004AlmLineCrit,'pm1004AlmsynthAlmLineTable':pm1004AlmsynthAlmLineTable,'pm1004AlmsynthAlmLineEntry':pm1004AlmsynthAlmLineEntry,_i:pm1004AlmsynthAlmLineIndex,'pm1004AlmXfpAbsentPortn':pm1004AlmXfpAbsentPortn,'pm1004AlmXfpInitNotComplPortn':pm1004AlmXfpInitNotComplPortn,_O:pm1004AlmLineHwFailPortn,'pm1004AlmXfpTxOffPortn':pm1004AlmXfpTxOffPortn,'pm1004AlmLineLocalOosPortn':pm1004AlmLineLocalOosPortn,'pm1004AlmUpRdiInsPortn':pm1004AlmUpRdiInsPortn,_L:pm1004AlmLineDdmWarningPortn,_M:pm1004AlmLineDdmAlmPortn,_N:pm1004AlmLineFailPortn,'pm1004AlmLineActivePortn':pm1004AlmLineActivePortn,'pm1004AlmdfrmAlmTable':pm1004AlmdfrmAlmTable,'pm1004AlmdfrmAlmEntry':pm1004AlmdfrmAlmEntry,_j:pm1004AlmdfrmAlmIndex,'pm1004AlmDwAisDetPortn':pm1004AlmDwAisDetPortn,'pm1004AlmDwRdiDetPortn':pm1004AlmDwRdiDetPortn,'pm1004AlmDwOofPortn':pm1004AlmDwOofPortn,'pm1004AlmDwLofPortn':pm1004AlmDwLofPortn,'pm1004AlmlineSyncAlarmsTable':pm1004AlmlineSyncAlarmsTable,'pm1004AlmlineSyncAlarmsEntry':pm1004AlmlineSyncAlarmsEntry,_k:pm1004AlmlineSyncAlarmsIndex,'pm1004AlmDwLockerrPortn':pm1004AlmDwLockerrPortn,'pm1004AlmUpLockerrPortn':pm1004AlmUpLockerrPortn,'pm1004AlmDwLosPortn':pm1004AlmDwLosPortn,'pm1004AlmlineXfp1AlarmsTable':pm1004AlmlineXfp1AlarmsTable,'pm1004AlmlineXfp1AlarmsEntry':pm1004AlmlineXfp1AlarmsEntry,_l:pm1004AlmlineXfp1AlarmsIndex,'pm1004AlmModNrPortn':pm1004AlmModNrPortn,'pm1004AlmRxCdrNotLockedPortn':pm1004AlmRxCdrNotLockedPortn,'pm1004AlmRxNrPortn':pm1004AlmRxNrPortn,'pm1004AlmTxCdrNotLockedPortn':pm1004AlmTxCdrNotLockedPortn,'pm1004AlmTxFaultPortn':pm1004AlmTxFaultPortn,'pm1004AlmTxNrPortn':pm1004AlmTxNrPortn,'pm1004AlmChannelNotAcquiredPortn':pm1004AlmChannelNotAcquiredPortn,'pm1004AlmWavelengthUnlockedPortn':pm1004AlmWavelengthUnlockedPortn,'pm1004AlmTecFaultPortn':pm1004AlmTecFaultPortn,'pm1004AlmApdSupplyFaultPortn':pm1004AlmApdSupplyFaultPortn,'pm1004measures':pm1004measures,'pm1004MesrOther':pm1004MesrOther,'pm1004Mesrsynth0':pm1004Mesrsynth0,'pm1004Mesrsynth1':pm1004Mesrsynth1,'pm1004MesrClient':pm1004MesrClient,'pm1004MesrtempMeasTable':pm1004MesrtempMeasTable,'pm1004MesrtempMeasEntry':pm1004MesrtempMeasEntry,_m:pm1004MesrtempMeasIndex,'pm1004MesrtempMeasPortn':pm1004MesrtempMeasPortn,'pm1004MesrvoltMeasTable':pm1004MesrvoltMeasTable,'pm1004MesrvoltMeasEntry':pm1004MesrvoltMeasEntry,_n:pm1004MesrvoltMeasIndex,'pm1004MesrvoltMeasPortn':pm1004MesrvoltMeasPortn,'pm1004MesrbiasMeasTable':pm1004MesrbiasMeasTable,'pm1004MesrbiasMeasEntry':pm1004MesrbiasMeasEntry,_o:pm1004MesrbiasMeasIndex,'pm1004MesrbiasMeasPortn':pm1004MesrbiasMeasPortn,'pm1004MesrtxpwrMeasTable':pm1004MesrtxpwrMeasTable,'pm1004MesrtxpwrMeasEntry':pm1004MesrtxpwrMeasEntry,_p:pm1004MesrtxpwrMeasIndex,'pm1004MesrtxpwrMeasPortn':pm1004MesrtxpwrMeasPortn,'pm1004MesrrxpwrMeasTable':pm1004MesrrxpwrMeasTable,'pm1004MesrrxpwrMeasEntry':pm1004MesrrxpwrMeasEntry,_q:pm1004MesrrxpwrMeasIndex,'pm1004MesrrxpwrMeasPortn':pm1004MesrrxpwrMeasPortn,'pm1004MesrLine':pm1004MesrLine,'pm1004Mesrxfp1LxModTempMeasTable':pm1004Mesrxfp1LxModTempMeasTable,'pm1004Mesrxfp1LxModTempMeasEntry':pm1004Mesrxfp1LxModTempMeasEntry,_r:pm1004Mesrxfp1LxModTempMeasIndex,'pm1004Mesrxfp1LxModTempMeasPortn':pm1004Mesrxfp1LxModTempMeasPortn,'pm1004Mesrxfp1ReservedTable':pm1004Mesrxfp1ReservedTable,'pm1004Mesrxfp1ReservedEntry':pm1004Mesrxfp1ReservedEntry,_s:pm1004Mesrxfp1ReservedIndex,'pm1004Mesrxfp1ReservedPortn':pm1004Mesrxfp1ReservedPortn,'pm1004Mesrxfp1LoBiasCurrentMeasTable':pm1004Mesrxfp1LoBiasCurrentMeasTable,'pm1004Mesrxfp1LoBiasCurrentMeasEntry':pm1004Mesrxfp1LoBiasCurrentMeasEntry,_t:pm1004Mesrxfp1LoBiasCurrentMeasIndex,'pm1004Mesrxfp1LoBiasCurrentMeasPortn':pm1004Mesrxfp1LoBiasCurrentMeasPortn,'pm1004Mesrxfp1LoTxPowerMeasTable':pm1004Mesrxfp1LoTxPowerMeasTable,'pm1004Mesrxfp1LoTxPowerMeasEntry':pm1004Mesrxfp1LoTxPowerMeasEntry,_u:pm1004Mesrxfp1LoTxPowerMeasIndex,'pm1004Mesrxfp1LoTxPowerMeasPortn':pm1004Mesrxfp1LoTxPowerMeasPortn,'pm1004Mesrxfp1LiRxPowerMeasTable':pm1004Mesrxfp1LiRxPowerMeasTable,'pm1004Mesrxfp1LiRxPowerMeasEntry':pm1004Mesrxfp1LiRxPowerMeasEntry,_v:pm1004Mesrxfp1LiRxPowerMeasIndex,'pm1004Mesrxfp1LiRxPowerMeasPortn':pm1004Mesrxfp1LiRxPowerMeasPortn,'pm1004Mesrxfp1LxAux1MeasTable':pm1004Mesrxfp1LxAux1MeasTable,'pm1004Mesrxfp1LxAux1MeasEntry':pm1004Mesrxfp1LxAux1MeasEntry,_w:pm1004Mesrxfp1LxAux1MeasIndex,'pm1004Mesrxfp1LxAux1MeasPortn':pm1004Mesrxfp1LxAux1MeasPortn,'pm1004Mesrxfp1LxAux2MeasTable':pm1004Mesrxfp1LxAux2MeasTable,'pm1004Mesrxfp1LxAux2MeasEntry':pm1004Mesrxfp1LxAux2MeasEntry,_x:pm1004Mesrxfp1LxAux2MeasIndex,'pm1004Mesrxfp1LxAux2MeasPortn':pm1004Mesrxfp1LxAux2MeasPortn,'pm1004Mesrotx1AgingTable':pm1004Mesrotx1AgingTable,'pm1004Mesrotx1AgingEntry':pm1004Mesrotx1AgingEntry,_y:pm1004Mesrotx1AgingIndex,'pm1004Mesrotx1AgingPortn':pm1004Mesrotx1AgingPortn,'pm1004Mesrotx1LaserTemperatureTable':pm1004Mesrotx1LaserTemperatureTable,'pm1004Mesrotx1LaserTemperatureEntry':pm1004Mesrotx1LaserTemperatureEntry,_z:pm1004Mesrotx1LaserTemperatureIndex,'pm1004Mesrotx1LaserTemperaturePortn':pm1004Mesrotx1LaserTemperaturePortn,'pm1004Mesrotx1FreqDeviationTable':pm1004Mesrotx1FreqDeviationTable,'pm1004Mesrotx1FreqDeviationEntry':pm1004Mesrotx1FreqDeviationEntry,_A0:pm1004Mesrotx1FreqDeviationIndex,'pm1004Mesrotx1FreqDeviationPortn':pm1004Mesrotx1FreqDeviationPortn,'pm1004Mesrotx1LaserWvlengthTable':pm1004Mesrotx1LaserWvlengthTable,'pm1004Mesrotx1LaserWvlengthEntry':pm1004Mesrotx1LaserWvlengthEntry,_A1:pm1004Mesrotx1LaserWvlengthIndex,'pm1004Mesrotx1LaserWvlengthPortn':pm1004Mesrotx1LaserWvlengthPortn,'pm1004counters':pm1004counters,'pm1004CntOther':pm1004CntOther,'pm1004CntClient':pm1004CntClient,'pm1004CntupRaRemCntTable':pm1004CntupRaRemCntTable,'pm1004CntupRaRemCntEntry':pm1004CntupRaRemCntEntry,_A2:pm1004CntupRaRemCntIndex,'pm1004CntupRaRemCntValuePortn':pm1004CntupRaRemCntValuePortn,'pm1004CntupRaRemCntErrorPortn':pm1004CntupRaRemCntErrorPortn,'pm1004CntupRaRemCntOverloadPortn':pm1004CntupRaRemCntOverloadPortn,'pm1004CntupRaInsCntTable':pm1004CntupRaInsCntTable,'pm1004CntupRaInsCntEntry':pm1004CntupRaInsCntEntry,_A3:pm1004CntupRaInsCntIndex,'pm1004CntupRaInsCntValuePortn':pm1004CntupRaInsCntValuePortn,'pm1004CntupRaInsCntErrorPortn':pm1004CntupRaInsCntErrorPortn,'pm1004CntupRaInsCntOverloadPortn':pm1004CntupRaInsCntOverloadPortn,'pm1004CntupRdErrCntTable':pm1004CntupRdErrCntTable,'pm1004CntupRdErrCntEntry':pm1004CntupRdErrCntEntry,_A4:pm1004CntupRdErrCntIndex,'pm1004CntupRdErrCntValuePortn':pm1004CntupRdErrCntValuePortn,'pm1004CntupRdErrCntErrorPortn':pm1004CntupRdErrCntErrorPortn,'pm1004CntupRdErrCntOverloadPortn':pm1004CntupRdErrCntOverloadPortn,'pm1004CntupTimCntTable':pm1004CntupTimCntTable,'pm1004CntupTimCntEntry':pm1004CntupTimCntEntry,_A5:pm1004CntupTimCntIndex,'pm1004CntupTimCntValuePortn':pm1004CntupTimCntValuePortn,'pm1004CntupTimCntErrorPortn':pm1004CntupTimCntErrorPortn,'pm1004CntupTimCntOverloadPortn':pm1004CntupTimCntOverloadPortn,'pm1004CntupCvErrCntTable':pm1004CntupCvErrCntTable,'pm1004CntupCvErrCntEntry':pm1004CntupCvErrCntEntry,_A6:pm1004CntupCvErrCntIndex,'pm1004CntupCvErrCntValuePortn':pm1004CntupCvErrCntValuePortn,'pm1004CntupCvErrCntErrorPortn':pm1004CntupCvErrCntErrorPortn,'pm1004CntupCvErrCntOverloadPortn':pm1004CntupCvErrCntOverloadPortn,'pm1004CntdwCbipCntTable':pm1004CntdwCbipCntTable,'pm1004CntdwCbipCntEntry':pm1004CntdwCbipCntEntry,_A7:pm1004CntdwCbipCntIndex,'pm1004CntdwCbipCntValuePortn':pm1004CntdwCbipCntValuePortn,'pm1004CntdwCbipCntErrorPortn':pm1004CntdwCbipCntErrorPortn,'pm1004CntdwCbipCntOverloadPortn':pm1004CntdwCbipCntOverloadPortn,'pm1004CntdwTimCntTable':pm1004CntdwTimCntTable,'pm1004CntdwTimCntEntry':pm1004CntdwTimCntEntry,_A8:pm1004CntdwTimCntIndex,'pm1004CntdwTimCntValuePortn':pm1004CntdwTimCntValuePortn,'pm1004CntdwTimCntErrorPortn':pm1004CntdwTimCntErrorPortn,'pm1004CntdwTimCntOverloadPortn':pm1004CntdwTimCntOverloadPortn,'pm1004CntLine':pm1004CntLine,'pm1004CntdfrmB1ErrCntTable':pm1004CntdfrmB1ErrCntTable,'pm1004CntdfrmB1ErrCntEntry':pm1004CntdfrmB1ErrCntEntry,_A9:pm1004CntdfrmB1ErrCntIndex,'pm1004CntdfrmB1ErrCntValuePortn':pm1004CntdfrmB1ErrCntValuePortn,'pm1004CntdfrmB1ErrCntErrorPortn':pm1004CntdfrmB1ErrCntErrorPortn,'pm1004CntdfrmB1ErrCntOverloadPortn':pm1004CntdfrmB1ErrCntOverloadPortn,'pm1004CntdfrmTimCntTable':pm1004CntdfrmTimCntTable,'pm1004CntdfrmTimCntEntry':pm1004CntdfrmTimCntEntry,_AA:pm1004CntdfrmTimCntIndex,'pm1004CntdfrmTimCntValuePortn':pm1004CntdfrmTimCntValuePortn,'pm1004CntdfrmTimCntErrorPortn':pm1004CntdfrmTimCntErrorPortn,'pm1004CntdfrmTimCntOverloadPortn':pm1004CntdfrmTimCntOverloadPortn,'pm1004CntdfrmPrimLineErrCntTable':pm1004CntdfrmPrimLineErrCntTable,'pm1004CntdfrmPrimLineErrCntEntry':pm1004CntdfrmPrimLineErrCntEntry,_AB:pm1004CntdfrmPrimLineErrCntIndex,'pm1004CntdfrmPrimLineErrCntValuePortn':pm1004CntdfrmPrimLineErrCntValuePortn,'pm1004CntdfrmPrimLineErrCntErrorPortn':pm1004CntdfrmPrimLineErrCntErrorPortn,'pm1004CntdfrmPrimLineErrCntOverloadPortn':pm1004CntdfrmPrimLineErrCntOverloadPortn,'pm1004CntCountersReset':pm1004CntCountersReset,'pm1004CntCountersStop':pm1004CntCountersStop,'pm1004controlsWrite':pm1004controlsWrite,'pm1004CtrlOther':pm1004CtrlOther,'pm1004CtrlconfMgnt1':pm1004CtrlconfMgnt1,'pm1004CtrlConf1Load1':pm1004CtrlConf1Load1,'pm1004CtrlConf2Load1':pm1004CtrlConf2Load1,'pm1004CtrlConf2Flash1':pm1004CtrlConf2Flash1,'pm1004CtrlConf2Clear1':pm1004CtrlConf2Clear1,'pm1004Ctrlsynth4':pm1004Ctrlsynth4,'pm1004CtrlCorrelatOn':pm1004CtrlCorrelatOn,'pm1004CtrlCorrelatOff':pm1004CtrlCorrelatOff,'pm1004CtrlswMgnt':pm1004CtrlswMgnt,'pm1004CtrlColdReset':pm1004CtrlColdReset,'pm1004CtrlWarmReset':pm1004CtrlWarmReset,'pm1004CtrlLoadSwBank1':pm1004CtrlLoadSwBank1,'pm1004CtrlLoadSwBank2':pm1004CtrlLoadSwBank2,'pm1004CtrlgwMgnt':pm1004CtrlgwMgnt,'pm1004CtrlCurrentGwReset':pm1004CtrlCurrentGwReset,'pm1004CtrlLoadGwBank1':pm1004CtrlLoadGwBank1,'pm1004CtrlLoadGwBank2':pm1004CtrlLoadGwBank2,'pm1004CtrlLoadGwBank3':pm1004CtrlLoadGwBank3,'pm1004CtrlLoadGwBank4':pm1004CtrlLoadGwBank4,'pm1004CtrlledTest':pm1004CtrlledTest,'pm1004CtrlGreenLed':pm1004CtrlGreenLed,'pm1004CtrlRedLed':pm1004CtrlRedLed,'pm1004CtrlLedOff':pm1004CtrlLedOff,'pm1004CtrlmoduleOosMode':pm1004CtrlmoduleOosMode,'pm1004CtrlModuleOosMode':pm1004CtrlModuleOosMode,'pm1004CtrlmaintenanceMode':pm1004CtrlmaintenanceMode,'pm1004CtrlMaintenanceMode':pm1004CtrlMaintenanceMode,'pm1004CtrldccEnable':pm1004CtrldccEnable,'pm1004CtrlDccEnable':pm1004CtrlDccEnable,'pm1004CtrlClient':pm1004CtrlClient,'pm1004CtrlaccessLoopTable':pm1004CtrlaccessLoopTable,'pm1004CtrlaccessLoopEntry':pm1004CtrlaccessLoopEntry,_AC:pm1004CtrlaccessLoopIndex,'pm1004CtrlaccessLoopPortn':pm1004CtrlaccessLoopPortn,'pm1004CtrlportOosModeTable':pm1004CtrlportOosModeTable,'pm1004CtrlportOosModeEntry':pm1004CtrlportOosModeEntry,_AD:pm1004CtrlportOosModeIndex,'pm1004CtrlportOosModePortn':pm1004CtrlportOosModePortn,'pm1004CtrlsfpOnCtrlTable':pm1004CtrlsfpOnCtrlTable,'pm1004CtrlsfpOnCtrlEntry':pm1004CtrlsfpOnCtrlEntry,_AE:pm1004CtrlsfpOnCtrlIndex,'pm1004CtrlsfpOnCtrlPortn':pm1004CtrlsfpOnCtrlPortn,'pm1004CtrlsfpOffCtrlTable':pm1004CtrlsfpOffCtrlTable,'pm1004CtrlsfpOffCtrlEntry':pm1004CtrlsfpOffCtrlEntry,_AF:pm1004CtrlsfpOffCtrlIndex,'pm1004CtrlsfpOffCtrlPortn':pm1004CtrlsfpOffCtrlPortn,'pm1004CtrlcsfUpInsTable':pm1004CtrlcsfUpInsTable,'pm1004CtrlcsfUpInsEntry':pm1004CtrlcsfUpInsEntry,_AG:pm1004CtrlcsfUpInsIndex,'pm1004CtrlcsfUpInsPortn':pm1004CtrlcsfUpInsPortn,'pm1004CtrlcaisDwInsTable':pm1004CtrlcaisDwInsTable,'pm1004CtrlcaisDwInsEntry':pm1004CtrlcaisDwInsEntry,_AH:pm1004CtrlcaisDwInsIndex,'pm1004CtrlcaisDwInsPortn':pm1004CtrlcaisDwInsPortn,'pm1004CtrlclientAccessTermLoopTable':pm1004CtrlclientAccessTermLoopTable,'pm1004CtrlclientAccessTermLoopEntry':pm1004CtrlclientAccessTermLoopEntry,_AI:pm1004CtrlclientAccessTermLoopIndex,'pm1004CtrlclientAccessTermLoopPortn':pm1004CtrlclientAccessTermLoopPortn,'pm1004CtrlresetCount15PortTable':pm1004CtrlresetCount15PortTable,'pm1004CtrlresetCount15PortEntry':pm1004CtrlresetCount15PortEntry,_AJ:pm1004CtrlresetCount15PortIndex,'pm1004CtrlclientResetAllPerfCount15Portn':pm1004CtrlclientResetAllPerfCount15Portn,'pm1004CtrlresetCount24PortTable':pm1004CtrlresetCount24PortTable,'pm1004CtrlresetCount24PortEntry':pm1004CtrlresetCount24PortEntry,_AK:pm1004CtrlresetCount24PortIndex,'pm1004CtrlclientResetAllPerfCount24Portn':pm1004CtrlclientResetAllPerfCount24Portn,'pm1004CtrlprotocolTable':pm1004CtrlprotocolTable,'pm1004CtrlprotocolEntry':pm1004CtrlprotocolEntry,_AL:pm1004CtrlprotocolIndex,'pm1004CtrlprotocolPortn':pm1004CtrlprotocolPortn,'pm1004CtrlLine':pm1004CtrlLine,'pm1004CtrlcommAccessLoop':pm1004CtrlcommAccessLoop,'pm1004CtrlCommAccessloop':pm1004CtrlCommAccessloop,'pm1004CtrllineLoop':pm1004CtrllineLoop,'pm1004CtrlLineLoop':pm1004CtrlLineLoop,'pm1004CtrlmsAis':pm1004CtrlmsAis,'pm1004CtrlMsAis':pm1004CtrlMsAis,'pm1004CtrlfecDisableTable':pm1004CtrlfecDisableTable,'pm1004CtrlfecDisableEntry':pm1004CtrlfecDisableEntry,_AM:pm1004CtrlfecDisableIndex,'pm1004CtrlfecDisablePortn':pm1004CtrlfecDisablePortn,'pm1004CtrlProtMgnt':pm1004CtrlProtMgnt,'pm1004CtrlLineNumber':pm1004CtrlLineNumber,'pm1004CtrlProtMode':pm1004CtrlProtMode,'pm1004CtrllineOosModeTable':pm1004CtrllineOosModeTable,'pm1004CtrllineOosModeEntry':pm1004CtrllineOosModeEntry,_AN:pm1004CtrllineOosModeIndex,'pm1004CtrllineOosModePortn':pm1004CtrllineOosModePortn,'pm1004CtrllineResetCount15LineTable':pm1004CtrllineResetCount15LineTable,'pm1004CtrllineResetCount15LineEntry':pm1004CtrllineResetCount15LineEntry,_AO:pm1004CtrllineResetCount15LineIndex,'pm1004CtrlresetAllPerfCount15Portn':pm1004CtrlresetAllPerfCount15Portn,'pm1004CtrllineResetCount24LineTable':pm1004CtrllineResetCount24LineTable,'pm1004CtrllineResetCount24LineEntry':pm1004CtrllineResetCount24LineEntry,_AP:pm1004CtrllineResetCount24LineIndex,'pm1004CtrlresetAllPerfCount24Portn':pm1004CtrlresetAllPerfCount24Portn,'pm1004CtrlxfpOnoffTable':pm1004CtrlxfpOnoffTable,'pm1004CtrlxfpOnoffEntry':pm1004CtrlxfpOnoffEntry,_AQ:pm1004CtrlxfpOnoffIndex,'pm1004CtrlxfpOnoffPortn':pm1004CtrlxfpOnoffPortn,'pm1004CtrlxfpLineLoopTable':pm1004CtrlxfpLineLoopTable,'pm1004CtrlxfpLineLoopEntry':pm1004CtrlxfpLineLoopEntry,_AR:pm1004CtrlxfpLineLoopIndex,'pm1004CtrlxfpLineLoopPortn':pm1004CtrlxfpLineLoopPortn,'pm1004CtrlxfpXfiLoopTable':pm1004CtrlxfpXfiLoopTable,'pm1004CtrlxfpXfiLoopEntry':pm1004CtrlxfpXfiLoopEntry,_AS:pm1004CtrlxfpXfiLoopIndex,'pm1004CtrlxfpXfiLoopPortn':pm1004CtrlxfpXfiLoopPortn,'pm1004CtrllineTunableChannelTable':pm1004CtrllineTunableChannelTable,'pm1004CtrllineTunableChannelEntry':pm1004CtrllineTunableChannelEntry,_AT:pm1004CtrllineTunableChannelIndex,'pm1004CtrllineTunableChannelPortn':pm1004CtrllineTunableChannelPortn,'pm1004CtrllinePhotodiodeModeTable':pm1004CtrllinePhotodiodeModeTable,'pm1004CtrllinePhotodiodeModeEntry':pm1004CtrllinePhotodiodeModeEntry,_AU:pm1004CtrllinePhotodiodeModeIndex,'pm1004CtrllinePhotodiodeModePortn':pm1004CtrllinePhotodiodeModePortn,'pm1004CtrllinePhotodiodeValueTable':pm1004CtrllinePhotodiodeValueTable,'pm1004CtrllinePhotodiodeValueEntry':pm1004CtrllinePhotodiodeValueEntry,_AV:pm1004CtrllinePhotodiodeValueIndex,'pm1004CtrllinePhotodiodeValuePortn':pm1004CtrllinePhotodiodeValuePortn,'pm1004CtrllinePowerLaserTable':pm1004CtrllinePowerLaserTable,'pm1004CtrllinePowerLaserEntry':pm1004CtrllinePowerLaserEntry,_AW:pm1004CtrllinePowerLaserIndex,'pm1004CtrllinePowerLaserPortn':pm1004CtrllinePowerLaserPortn,'pm1004CtrlotxVlhReset':pm1004CtrlotxVlhReset,'pm1004CtrlOtxVlhReset':pm1004CtrlOtxVlhReset,'pm1004ri':pm1004ri,'pm1004riTable':pm1004riTable,'pm1004RinvSfpTable':pm1004RinvSfpTable,'pm1004RinvSfpEntry':pm1004RinvSfpEntry,_AX:pm1004RinvSfpIndex,'pm1004Rinvsfp':pm1004Rinvsfp,'pm1004RinvLineTable':pm1004RinvLineTable,'pm1004RinvLineEntry':pm1004RinvLineEntry,_AY:pm1004RinvLineIndex,'pm1004RinvxfpLine':pm1004RinvxfpLine,'pm1004RinvReloadInventory':pm1004RinvReloadInventory,'pm1004RinvHwPlatform':pm1004RinvHwPlatform,'pm1004RinvModulePlatform':pm1004RinvModulePlatform,'pm1004RinvSwPlatform':pm1004RinvSwPlatform,'pm1004RinvGwPlatform':pm1004RinvGwPlatform,'pm1004download':pm1004download,'pm1004DwlOther':pm1004DwlOther,'pm1004DwlrestartProcess':pm1004DwlrestartProcess,'pm1004DwlWarmRestartProcessed':pm1004DwlWarmRestartProcessed,'pm1004DwlColdRestartProcessed':pm1004DwlColdRestartProcessed,'pm1004DwlswBanksUsed':pm1004DwlswBanksUsed,'pm1004DwlSwBank1Used':pm1004DwlSwBank1Used,'pm1004DwlSwBank2Used':pm1004DwlSwBank2Used,'pm1004DwlSwBank1Notempty':pm1004DwlSwBank1Notempty,'pm1004DwlSwBank2Notempty':pm1004DwlSwBank2Notempty,'pm1004DwlgwBanksUsed':pm1004DwlgwBanksUsed,'pm1004DwlGwBank1Used':pm1004DwlGwBank1Used,'pm1004DwlGwBank2Used':pm1004DwlGwBank2Used,'pm1004DwlGwBank3Used':pm1004DwlGwBank3Used,'pm1004DwlGwBank4Used':pm1004DwlGwBank4Used,'pm1004DwlGwBank1Notempty':pm1004DwlGwBank1Notempty,'pm1004DwlGwBank2Notempty':pm1004DwlGwBank2Notempty,'pm1004DwlGwBank3Notempty':pm1004DwlGwBank3Notempty,'pm1004DwlGwBank4Notempty':pm1004DwlGwBank4Notempty,'pm1004DwlClient':pm1004DwlClient,'pm1004DwlLine':pm1004DwlLine,'pm1004Config':pm1004Config,'pm1004CfgAccessCAisCsf':pm1004CfgAccessCAisCsf,'pm1004CfgClientcaiscsfTable':pm1004CfgClientcaiscsfTable,'pm1004CfgClientcaiscsfEntry':pm1004CfgClientcaiscsfEntry,_AZ:pm1004CfgClientcaiscsfIndex,'pm1004CfgCAisModePortn':pm1004CfgCAisModePortn,'pm1004CfgUpAccessioAlmPortn':pm1004CfgUpAccessioAlmPortn,'pm1004CfgUpMapperDeAlmPortn':pm1004CfgUpMapperDeAlmPortn,'pm1004CfgUpAccessioSdhAlmPortn':pm1004CfgUpAccessioSdhAlmPortn,'pm1004CfgDownAccessioAlmPortn':pm1004CfgDownAccessioAlmPortn,'pm1004CfgDownMapperDeAlmPortn':pm1004CfgDownMapperDeAlmPortn,'pm1004CfgDownDfrmAlmPortn':pm1004CfgDownDfrmAlmPortn,'pm1004CfgDownLineSyncAlarmsPortn':pm1004CfgDownLineSyncAlarmsPortn,'pm1004CfgDownAccessioSdhAlmPortn':pm1004CfgDownAccessioSdhAlmPortn,'pm1004CfgStartup':pm1004CfgStartup,'pm1004CfgClientStartupTable':pm1004CfgClientStartupTable,'pm1004CfgClientStartupEntry':pm1004CfgClientStartupEntry,_Aa:pm1004CfgClientStartupIndex,'pm1004CfgSystConfPortPortn':pm1004CfgSystConfPortPortn,'pm1004CfgNetConfPortPortn':pm1004CfgNetConfPortPortn,'pm1004tablelineStartup':pm1004tablelineStartup,'pm1004CfgsystConfLine1':pm1004CfgsystConfLine1,'pm1004CfglineOptions1':pm1004CfglineOptions1,'pm1004CfgsystConfLine2':pm1004CfgsystConfLine2,'pm1004CfglineSelection':pm1004CfglineSelection,'pm1004CfgXfpTable':pm1004CfgXfpTable,'pm1004CfgXfpEntry':pm1004CfgXfpEntry,_Ab:pm1004CfgXfpIndex,'pm1004CfgSystConfXfpPortn':pm1004CfgSystConfXfpPortn,'pm1004CfgDataRateConfXfpPortn':pm1004CfgDataRateConfXfpPortn,'pm1004CfgModPerfConfig':pm1004CfgModPerfConfig,'pm1004tablemodPerfConfig':pm1004tablemodPerfConfig,'pm1004CfgperfMode':pm1004CfgperfMode,'pm1004CfgJ0Client':pm1004CfgJ0Client,'pm1004CfgEmptyTable':pm1004CfgEmptyTable,'pm1004CfgEmptyEntry':pm1004CfgEmptyEntry,_Ac:pm1004CfgEmptyIndex,'pm1004CfgClientExpectJ0SetupPortn':pm1004CfgClientExpectJ0SetupPortn,'pm1004CfgLabels':pm1004CfgLabels,'pm1004CfgLabelclientTable':pm1004CfgLabelclientTable,'pm1004CfgLabelclientEntry':pm1004CfgLabelclientEntry,_Ad:pm1004CfgLabelclientIndex,'pm1004CfgLabelclientPortn':pm1004CfgLabelclientPortn,'pm1004CfgLabellineTable':pm1004CfgLabellineTable,'pm1004CfgLabellineEntry':pm1004CfgLabellineEntry,_Ae:pm1004CfgLabellineIndex,'pm1004CfgLabellinePortn':pm1004CfgLabellinePortn,'pm1004CfgStartuptlh':pm1004CfgStartuptlh,'pm1004CfgOtxtlhTable':pm1004CfgOtxtlhTable,'pm1004CfgOtxtlhEntry':pm1004CfgOtxtlhEntry,_Af:pm1004CfgOtxtlhIndex,'pm1004CfgNuPortn':pm1004CfgNuPortn,'pm1004CfgLineDitherRatePortn':pm1004CfgLineDitherRatePortn,'pm1004CfgLineDitherFhzPortn':pm1004CfgLineDitherFhzPortn,'pm1004CfgLinePwrLaserPortn':pm1004CfgLinePwrLaserPortn,'pm1004CfgLineFCurrentPortn':pm1004CfgLineFCurrentPortn,'pm1004CfgLineGridCurrentPortn':pm1004CfgLineGridCurrentPortn,'pm1004CfgFPortn':pm1004CfgFPortn,'pm1004CfgReservedPortn':pm1004CfgReservedPortn,'pm1004CfgLinePhotodiodeModePortn':pm1004CfgLinePhotodiodeModePortn,'pm1004CfgLinePhotodiodeValuePortn':pm1004CfgLinePhotodiodeValuePortn,'pm1004CfgStartuptablefive':pm1004CfgStartuptablefive,'pm1004CfgOtxtlhcapabilitiesTable':pm1004CfgOtxtlhcapabilitiesTable,'pm1004CfgOtxtlhcapabilitiesEntry':pm1004CfgOtxtlhcapabilitiesEntry,_Ag:pm1004CfgOtxtlhcapabilitiesIndex,'pm1004CfgComponentTypePortn':pm1004CfgComponentTypePortn,'pm1004CfgMiscellaneousPortn':pm1004CfgMiscellaneousPortn,'pm1004CfgFirstChannelPortn':pm1004CfgFirstChannelPortn,'pm1004CfgLastChannelPortn':pm1004CfgLastChannelPortn,'pm1004CfgGridPortn':pm1004CfgGridPortn,'pm1004CfgWriteConfiguration':pm1004CfgWriteConfiguration,'pm1004traps':pm1004traps,_J:pm1004trapPortNumber,_I:pm1004trapLineNumber,_H:pm1004trapBoardNumber,'pm1004LineTrapNotUrgentGoesOn':pm1004LineTrapNotUrgentGoesOn,'pm1004LineTrapNotUrgentGoesOff':pm1004LineTrapNotUrgentGoesOff,'pm1004LineTrapUrgentGoesOn':pm1004LineTrapUrgentGoesOn,'pm1004LineTrapUrgentGoesOff':pm1004LineTrapUrgentGoesOff,'pm1004LineTrapCritGoesOn':pm1004LineTrapCritGoesOn,'pm1004LineTrapCritGoesOff':pm1004LineTrapCritGoesOff,'pm1004ClientTrapNotUrgentGoesOn':pm1004ClientTrapNotUrgentGoesOn,'pm1004ClientTrapNotUrgentGoesOff':pm1004ClientTrapNotUrgentGoesOff,'pm1004ClientTrapUrgentGoesOn':pm1004ClientTrapUrgentGoesOn,'pm1004ClientTrapUrgentGoesOff':pm1004ClientTrapUrgentGoesOff,'pm1004ClientTrapCritGoesOn':pm1004ClientTrapCritGoesOn,'pm1004ClientTrapCritGoesOff':pm1004ClientTrapCritGoesOff,'pm1004PowerTrapUrgentGoesOn':pm1004PowerTrapUrgentGoesOn,'pm1004PowerTrapUrgentGoesOff':pm1004PowerTrapUrgentGoesOff,'pm1004Monitoring':pm1004Monitoring,'pm1004MonOther':pm1004MonOther,'pm1004MonSync':pm1004MonSync,'pm1004PerfEnable':pm1004PerfEnable,'pm1004PerfSyncSource':pm1004PerfSyncSource,'pm1004Perf15minSync':pm1004Perf15minSync,'pm1004Perf24hSync':pm1004Perf24hSync,'pm1004MonTimeStamp':pm1004MonTimeStamp,'pm1004PerfCurrent15MinElapsedTime':pm1004PerfCurrent15MinElapsedTime,'pm1004PerfCurrent24HoursElapsedTime':pm1004PerfCurrent24HoursElapsedTime,'pm1004PerfPast15MinElapsedTime':pm1004PerfPast15MinElapsedTime,'pm1004PerfPast24HoursElapsedTime':pm1004PerfPast24HoursElapsedTime,'pm1004MonClient':pm1004MonClient,'pm1004MonClientPerformance':pm1004MonClientPerformance,'pm1004PerfUpCurrent15CntTable':pm1004PerfUpCurrent15CntTable,'pm1004PerfUpCurrent15CntEntry':pm1004PerfUpCurrent15CntEntry,_Ah:pm1004PerfUpCurrent15CntIndex,'pm1004PerfUpCurrent15CntInvCvPortn':pm1004PerfUpCurrent15CntInvCvPortn,'pm1004PerfUpCurrent15CntCvValuePortn':pm1004PerfUpCurrent15CntCvValuePortn,'pm1004PerfUpCurrent15CntInvEsPortn':pm1004PerfUpCurrent15CntInvEsPortn,'pm1004PerfUpCurrent15CntEsValuePortn':pm1004PerfUpCurrent15CntEsValuePortn,'pm1004PerfUpCurrent15CntInvSesPortn':pm1004PerfUpCurrent15CntInvSesPortn,'pm1004PerfUpCurrent15CntSesValuePortn':pm1004PerfUpCurrent15CntSesValuePortn,'pm1004PerfUpCurrent15CntInvSefsPortn':pm1004PerfUpCurrent15CntInvSefsPortn,'pm1004PerfUpCurrent15CntSefsValuePortn':pm1004PerfUpCurrent15CntSefsValuePortn,'pm1004PerfUpCurrent15CntInvUasPortn':pm1004PerfUpCurrent15CntInvUasPortn,'pm1004PerfUpCurrent15CntUasValuePortn':pm1004PerfUpCurrent15CntUasValuePortn,'pm1004PerfUpPast15CntTable':pm1004PerfUpPast15CntTable,'pm1004PerfUpPast15CntEntry':pm1004PerfUpPast15CntEntry,_Ai:pm1004PerfUpPast15CntIndex,'pm1004PerfUpPast15CntInvCvPortn':pm1004PerfUpPast15CntInvCvPortn,'pm1004PerfUpPast15CntCvValuePortn':pm1004PerfUpPast15CntCvValuePortn,'pm1004PerfUpPast15CntInvEsPortn':pm1004PerfUpPast15CntInvEsPortn,'pm1004PerfUpPast15CntEsValuePortn':pm1004PerfUpPast15CntEsValuePortn,'pm1004PerfUpPast15CntInvSesPortn':pm1004PerfUpPast15CntInvSesPortn,'pm1004PerfUpPast15CntSesValuePortn':pm1004PerfUpPast15CntSesValuePortn,'pm1004PerfUpPast15CntInvSefsPortn':pm1004PerfUpPast15CntInvSefsPortn,'pm1004PerfUpPast15CntSefsValuePortn':pm1004PerfUpPast15CntSefsValuePortn,'pm1004PerfUpPast15CntInvUasPortn':pm1004PerfUpPast15CntInvUasPortn,'pm1004PerfUpPast15CntUasValuePortn':pm1004PerfUpPast15CntUasValuePortn,'pm1004PerfUpCurrent24CntTable':pm1004PerfUpCurrent24CntTable,'pm1004PerfUpCurrent24CntEntry':pm1004PerfUpCurrent24CntEntry,_Aj:pm1004PerfUpCurrent24CntIndex,'pm1004PerfUpCurrent24CntInvCvPortn':pm1004PerfUpCurrent24CntInvCvPortn,'pm1004PerfUpCurrent24CntCvValuePortn':pm1004PerfUpCurrent24CntCvValuePortn,'pm1004PerfUpCurrent24CntInvEsPortn':pm1004PerfUpCurrent24CntInvEsPortn,'pm1004PerfUpCurrent24CntEsValuePortn':pm1004PerfUpCurrent24CntEsValuePortn,'pm1004PerfUpCurrent24CntInvSesPortn':pm1004PerfUpCurrent24CntInvSesPortn,'pm1004PerfUpCurrent24CntSesValuePortn':pm1004PerfUpCurrent24CntSesValuePortn,'pm1004PerfUpCurrent24CntInvSefsPortn':pm1004PerfUpCurrent24CntInvSefsPortn,'pm1004PerfUpCurrent24CntSefsValuePortn':pm1004PerfUpCurrent24CntSefsValuePortn,'pm1004PerfUpCurrent24CntInvUasPortn':pm1004PerfUpCurrent24CntInvUasPortn,'pm1004PerfUpCurrent24CntUasValuePortn':pm1004PerfUpCurrent24CntUasValuePortn,'pm1004PerfUpPast24CntTable':pm1004PerfUpPast24CntTable,'pm1004PerfUpPast24CntEntry':pm1004PerfUpPast24CntEntry,_Ak:pm1004PerfUpPast24CntIndex,'pm1004PerfUpPast24CntInvCvPortn':pm1004PerfUpPast24CntInvCvPortn,'pm1004PerfUpPast24CntCvValuePortn':pm1004PerfUpPast24CntCvValuePortn,'pm1004PerfUpPast24CntInvEsPortn':pm1004PerfUpPast24CntInvEsPortn,'pm1004PerfUpPast24CntEsValuePortn':pm1004PerfUpPast24CntEsValuePortn,'pm1004PerfUpPast24CntInvSesPortn':pm1004PerfUpPast24CntInvSesPortn,'pm1004PerfUpPast24CntSesValuePortn':pm1004PerfUpPast24CntSesValuePortn,'pm1004PerfUpPast24CntInvSefsPortn':pm1004PerfUpPast24CntInvSefsPortn,'pm1004PerfUpPast24CntSefsValuePortn':pm1004PerfUpPast24CntSefsValuePortn,'pm1004PerfUpPast24CntInvUasPortn':pm1004PerfUpPast24CntInvUasPortn,'pm1004PerfUpPast24CntUasValuePortn':pm1004PerfUpPast24CntUasValuePortn,'pm1004MonClientTraceIdentifier':pm1004MonClientTraceIdentifier,'pm1004Almj0AlarmTable':pm1004Almj0AlarmTable,'pm1004Almj0AlarmEntry':pm1004Almj0AlarmEntry,_Al:pm1004Almj0AlarmIndex,'pm1004AlmJ0TimAlarmPortn':pm1004AlmJ0TimAlarmPortn,'pm1004AlmJ0TiiAlarmPortn':pm1004AlmJ0TiiAlarmPortn,'pm1004AlmCrc7ErrorPortn':pm1004AlmCrc7ErrorPortn,'pm1004MonLine':pm1004MonLine,'pm1004MonLinePerformance':pm1004MonLinePerformance,'pm1004PerfLineCurrent15CntTable':pm1004PerfLineCurrent15CntTable,'pm1004PerfLineCurrent15CntEntry':pm1004PerfLineCurrent15CntEntry,_Am:pm1004PerfLineCurrent15CntIndex,'pm1004PerfLineCurrent15CntInvCvPortn':pm1004PerfLineCurrent15CntInvCvPortn,'pm1004PerfLineCurrent15CntCvValuePortn':pm1004PerfLineCurrent15CntCvValuePortn,'pm1004PerfLineCurrent15CntInvEsPortn':pm1004PerfLineCurrent15CntInvEsPortn,'pm1004PerfLineCurrent15CntEsValuePortn':pm1004PerfLineCurrent15CntEsValuePortn,'pm1004PerfLineCurrent15CntInvSesPortn':pm1004PerfLineCurrent15CntInvSesPortn,'pm1004PerfLineCurrent15CntSesValuePortn':pm1004PerfLineCurrent15CntSesValuePortn,'pm1004PerfLineCurrent15CntInvSefsPortn':pm1004PerfLineCurrent15CntInvSefsPortn,'pm1004PerfLineCurrent15CntSefsValuePortn':pm1004PerfLineCurrent15CntSefsValuePortn,'pm1004PerfLineCurrent15CntInvUasPortn':pm1004PerfLineCurrent15CntInvUasPortn,'pm1004PerfLineCurrent15CntUasValuePortn':pm1004PerfLineCurrent15CntUasValuePortn,'pm1004PerfLinePast15CntTable':pm1004PerfLinePast15CntTable,'pm1004PerfLinePast15CntEntry':pm1004PerfLinePast15CntEntry,_An:pm1004PerfLinePast15CntIndex,'pm1004PerfLinePast15CntInvCvPortn':pm1004PerfLinePast15CntInvCvPortn,'pm1004PerfLinePast15CntCvValuePortn':pm1004PerfLinePast15CntCvValuePortn,'pm1004PerfLinePast15CntInvEsPortn':pm1004PerfLinePast15CntInvEsPortn,'pm1004PerfLinePast15CntEsValuePortn':pm1004PerfLinePast15CntEsValuePortn,'pm1004PerfLinePast15CntInvSesPortn':pm1004PerfLinePast15CntInvSesPortn,'pm1004PerfLinePast15CntSesValuePortn':pm1004PerfLinePast15CntSesValuePortn,'pm1004PerfLinePast15CntInvSefsPortn':pm1004PerfLinePast15CntInvSefsPortn,'pm1004PerfLinePast15CntSefsValuePortn':pm1004PerfLinePast15CntSefsValuePortn,'pm1004PerfLinePast15CntInvUasPortn':pm1004PerfLinePast15CntInvUasPortn,'pm1004PerfLinePast15CntUasValuePortn':pm1004PerfLinePast15CntUasValuePortn,'pm1004PerfLineCurrent24CntTable':pm1004PerfLineCurrent24CntTable,'pm1004PerfLineCurrent24CntEntry':pm1004PerfLineCurrent24CntEntry,_Ao:pm1004PerfLineCurrent24CntIndex,'pm1004PerfLineCurrent24CntInvCvPortn':pm1004PerfLineCurrent24CntInvCvPortn,'pm1004PerfLineCurrent24CntCvValuePortn':pm1004PerfLineCurrent24CntCvValuePortn,'pm1004PerfLineCurrent24CntInvEsPortn':pm1004PerfLineCurrent24CntInvEsPortn,'pm1004PerfLineCurrent24CntEsValuePortn':pm1004PerfLineCurrent24CntEsValuePortn,'pm1004PerfLineCurrent24CntInvSesPortn':pm1004PerfLineCurrent24CntInvSesPortn,'pm1004PerfLineCurrent24CntSesValuePortn':pm1004PerfLineCurrent24CntSesValuePortn,'pm1004PerfLineCurrent24CntInvSefsPortn':pm1004PerfLineCurrent24CntInvSefsPortn,'pm1004PerfLineCurrent24CntSefsValuePortn':pm1004PerfLineCurrent24CntSefsValuePortn,'pm1004PerfLineCurrent24CntInvUasPortn':pm1004PerfLineCurrent24CntInvUasPortn,'pm1004PerfLineCurrent24CntUasValuePortn':pm1004PerfLineCurrent24CntUasValuePortn,'pm1004PerfLinePast24CntTable':pm1004PerfLinePast24CntTable,'pm1004PerfLinePast24CntEntry':pm1004PerfLinePast24CntEntry,_Ap:pm1004PerfLinePast24CntIndex,'pm1004PerfLinePast24CntInvCvPortn':pm1004PerfLinePast24CntInvCvPortn,'pm1004PerfLinePast24CntCvValuePortn':pm1004PerfLinePast24CntCvValuePortn,'pm1004PerfLinePast24CntInvEsPortn':pm1004PerfLinePast24CntInvEsPortn,'pm1004PerfLinePast24CntEsValuePortn':pm1004PerfLinePast24CntEsValuePortn,'pm1004PerfLinePast24CntInvSesPortn':pm1004PerfLinePast24CntInvSesPortn,'pm1004PerfLinePast24CntSesValuePortn':pm1004PerfLinePast24CntSesValuePortn,'pm1004PerfLinePast24CntInvSefsPortn':pm1004PerfLinePast24CntInvSefsPortn,'pm1004PerfLinePast24CntSefsValuePortn':pm1004PerfLinePast24CntSefsValuePortn,'pm1004PerfLinePast24CntInvUasPortn':pm1004PerfLinePast24CntInvUasPortn,'pm1004PerfLinePast24CntUasValuePortn':pm1004PerfLinePast24CntUasValuePortn,'pm1004MonLineTraceIdentifier':pm1004MonLineTraceIdentifier})