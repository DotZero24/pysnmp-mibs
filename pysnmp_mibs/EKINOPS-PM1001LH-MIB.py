_AU='pm1001lhMondwRmonNonUnicastCntIndex'
_AT='pm1001lhMondwRmonUnicastCntIndex'
_AS='pm1001lhMondwRmonBitsCntIndex'
_AR='pm1001lhMondwRmonTimerCntIndex'
_AQ='pm1001lhMondwRmonPauseFrameCntIndex'
_AP='pm1001lhMondwRmonMulticastCntIndex'
_AO='pm1001lhMondwRmonBroadcastCntIndex'
_AN='pm1001lhMondwRmonPacketsCntIndex'
_AM='pm1001lhMondwRmonCrcErrorCntIndex'
_AL='pm1001lhMondwRmonByteCntIndex'
_AK='pm1001lhMonupRmonNonUnicastCntIndex'
_AJ='pm1001lhMonupRmonUnicastCntIndex'
_AI='pm1001lhMonupRmonBitsCntIndex'
_AH='pm1001lhMonupRmonDropFrameCntIndex'
_AG='pm1001lhMonupRmonPauseFrameCntIndex'
_AF='pm1001lhMonupRmonTimerCntIndex'
_AE='pm1001lhMonupRmonMulticastCntIndex'
_AD='pm1001lhMonupRmonBroadcastCntIndex'
_AC='pm1001lhMonupRmonPacketsCntIndex'
_AB='pm1001lhMonupRmonCrcErrorCntIndex'
_AA='pm1001lhMonupRmonByteCntIndex'
_A9='pm1001lhPerfTelecomLinePast24StatHistoryPort1Index'
_A8='pm1001lhPerfTelecomLineCurrent24StatIndex'
_A7='pm1001lhPerfTelecomLinePast15StatHistoryPort1Index'
_A6='pm1001lhPerfTelecomLineCurrent15StatIndex'
_A5='pm1001lhPerfDatacomClientPast24StatHistoryPort1Index'
_A4='pm1001lhPerfDatacomClientCurrent24StatIndex'
_A3='pm1001lhPerfDatacomClientPast15StatHistoryPort1Index'
_A2='pm1001lhPerfDatacomClientCurrent15StatIndex'
_A1='pm1001lhPerfTelecomClientPast24StatHistoryPort1Index'
_A0='pm1001lhPerfTelecomClientCurrent24StatIndex'
_z='pm1001lhPerfTelecomClientPast15StatHistoryPort1Index'
_y='pm1001lhPerfTelecomClientCurrent15StatIndex'
_x='pm1001lhCfgOtxtlhcapabilitiesIndex'
_w='pm1001lhCfgLabellineIndex'
_v='pm1001lhCfgLabelclientIndex'
_u='pm1001lhCfgOtxtlhIndex'
_t='pm1001lhCfgXfpIndex'
_s='pm1001lhCfgClientStartupIndex'
_r='pm1001lhCfgClientcaiscsfIndex'
_q='pm1001lhCtrllineResetAllCountIndex'
_p='pm1001lhCtrllineLoopTransceiverIndex'
_o='pm1001lhCtrllineAccessLoopIndex'
_n='pm1001lhCtrlxfpLineXfiLoopIndex'
_m='pm1001lhCtrlxfpLineLoopIndex'
_l='pm1001lhCtrlxfpOnoffIndex'
_k='pm1001lhCtrlclientResetAllCountIndex'
_j='pm1001lhCtrlclientAccessTermLoopIndex'
_i='pm1001lhCtrlcaisDwInsIndex'
_h='pm1001lhCtrlcsfUpInsIndex'
_g='pm1001lhCtrlxfpOffCtrlIndex'
_f='pm1001lhCtrlportOosModeIndex'
_e='pm1001lhCtrlaccessLoopIndex'
_d='pm1001lhCntlineDfrmErrCntSIndex'
_c='pm1001lhCntlineDfrmPrimErrCntIndex'
_b='pm1001lhCntlineDfrmTimCntIndex'
_a='pm1001lhCntlineDfrmErrCntIndex'
_Z='pm1001lhCntclientDwTimCntIndex'
_Y='pm1001lhCntclientDwErrCntIndex'
_X='pm1001lhCntclientUpTimCntIndex'
_W='pm1001lhCntclientUpErrCntIndex'
_V='2015-01-14 00:00'
_U='2010-03-08 00:00'
_T='2010-02-23 00:00'
_S='pm1001lhAlmDefFuseA'
_R='pm1001lhAlmDefFuseB'
_Q='pm1001lhAlmClientHwFail'
_P='pm1001lhAlmClientFail'
_O='pm1001lhAlmClientXfpDdmAlm'
_N='pm1001lhAlmClientXfpDdmWarning'
_M='pm1001lhAlmLineHwFail'
_L='pm1001lhAlmLineFail'
_K='pm1001lhAlmLineDdmAlm'
_J='pm1001lhAlmLineDdmWarning'
_I='DisplayString'
_H='pm1001lhtrapBoardNumber'
_G='deprecated'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='EKINOPS-PM1001LH-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
modulepm1001lh=ModuleIdentity((1,3,6,1,4,1,20044,10))
if mibBuilder.loadTexts:modulepm1001lh.setRevisions(('2006-10-17 00:00','2007-02-21 00:00','2007-05-29 00:00','2007-06-29 00:00','2007-12-03 00:00','2008-04-21 00:00','2008-10-27 00:00','2008-11-25 00:00','2008-12-01 00:00','2008-12-04 00:00','2009-04-09 00:00','2009-05-15 00:00','2009-12-17 00:00','2010-01-28 00:00',_T,_T,_U,_U,'2010-06-01 00:00','2010-07-05 00:00','2010-08-31 00:00','2010-11-08 00:00','2011-01-07 00:00','2012-07-03 00:00','2013-04-03 00:00','2014-03-25 00:00',_V,_V,'2016-05-20 00:00','2016-06-02 00:00'))
class Pm1001lhOtxMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('otx80mode',1),('otx60mode',2),('otxadjustmode',4)))
class Pm1001lhOtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pm1001lhAdjustValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('otxadjustvalue0',0),('otxadjustvalue1',1),('otxadjustvalue2',2),('otxadjustvalue3',3),('otxadjustvalue4',4),('otxadjustvalue5',5),('otxadjustvalue6',6),('otxadjustvalue7',7),('otxadjustvalue8',8),('otxadjustvalue9',9),('otxadjustvalue10',10)))
class Pm1001lhOtxChannel(TextualConvention,Integer32):status=_A
_Pm1001lhalarms_ObjectIdentity=ObjectIdentity
pm1001lhalarms=_Pm1001lhalarms_ObjectIdentity((1,3,6,1,4,1,20044,10,2))
_Pm1001lhAlmOther_ObjectIdentity=ObjectIdentity
pm1001lhAlmOther=_Pm1001lhAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1))
_Pm1001lhAlmOtherNurg_ObjectIdentity=ObjectIdentity
pm1001lhAlmOtherNurg=_Pm1001lhAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,1))
_Pm1001lhAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm1001lhAlmsynthAlm2=_Pm1001lhAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,1,2))
_Pm1001lhAlmConfTableSave_Type=EkiOnOff
_Pm1001lhAlmConfTableSave_Object=MibScalar
pm1001lhAlmConfTableSave=_Pm1001lhAlmConfTableSave_Object((1,3,6,1,4,1,20044,10,2,1,1,2,1),_Pm1001lhAlmConfTableSave_Type())
pm1001lhAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmConfTableSave.setStatus(_A)
_Pm1001lhAlmInvUpload_Type=EkiOnOff
_Pm1001lhAlmInvUpload_Object=MibScalar
pm1001lhAlmInvUpload=_Pm1001lhAlmInvUpload_Object((1,3,6,1,4,1,20044,10,2,1,1,2,2),_Pm1001lhAlmInvUpload_Type())
pm1001lhAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmInvUpload.setStatus(_A)
_Pm1001lhAlmConfTableLoad_Type=EkiOnOff
_Pm1001lhAlmConfTableLoad_Object=MibScalar
pm1001lhAlmConfTableLoad=_Pm1001lhAlmConfTableLoad_Object((1,3,6,1,4,1,20044,10,2,1,1,2,3),_Pm1001lhAlmConfTableLoad_Type())
pm1001lhAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmConfTableLoad.setStatus(_A)
_Pm1001lhAlmCorrelatOff_Type=EkiOnOff
_Pm1001lhAlmCorrelatOff_Object=MibScalar
pm1001lhAlmCorrelatOff=_Pm1001lhAlmCorrelatOff_Object((1,3,6,1,4,1,20044,10,2,1,1,2,4),_Pm1001lhAlmCorrelatOff_Type())
pm1001lhAlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmCorrelatOff.setStatus(_A)
_Pm1001lhAlmMaintenanceOn_Type=EkiOnOff
_Pm1001lhAlmMaintenanceOn_Object=MibScalar
pm1001lhAlmMaintenanceOn=_Pm1001lhAlmMaintenanceOn_Object((1,3,6,1,4,1,20044,10,2,1,1,2,5),_Pm1001lhAlmMaintenanceOn_Type())
pm1001lhAlmMaintenanceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmMaintenanceOn.setStatus(_A)
_Pm1001lhAlmOtherUrg_ObjectIdentity=ObjectIdentity
pm1001lhAlmOtherUrg=_Pm1001lhAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,2))
_Pm1001lhAlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pm1001lhAlmmodInitFailLevel2=_Pm1001lhAlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,2,194))
_Pm1001lhAlmLedFail_Type=EkiOnOff
_Pm1001lhAlmLedFail_Object=MibScalar
pm1001lhAlmLedFail=_Pm1001lhAlmLedFail_Object((1,3,6,1,4,1,20044,10,2,1,2,194,1),_Pm1001lhAlmLedFail_Type())
pm1001lhAlmLedFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLedFail.setStatus(_A)
_Pm1001lhAlmNextColdBootForced_Type=EkiOnOff
_Pm1001lhAlmNextColdBootForced_Object=MibScalar
pm1001lhAlmNextColdBootForced=_Pm1001lhAlmNextColdBootForced_Object((1,3,6,1,4,1,20044,10,2,1,2,194,2),_Pm1001lhAlmNextColdBootForced_Type())
pm1001lhAlmNextColdBootForced.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmNextColdBootForced.setStatus(_A)
_Pm1001lhAlmBootUndone_Type=EkiOnOff
_Pm1001lhAlmBootUndone_Object=MibScalar
pm1001lhAlmBootUndone=_Pm1001lhAlmBootUndone_Object((1,3,6,1,4,1,20044,10,2,1,2,194,3),_Pm1001lhAlmBootUndone_Type())
pm1001lhAlmBootUndone.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmBootUndone.setStatus(_A)
_Pm1001lhAlmResetHwInitFail_Type=EkiOnOff
_Pm1001lhAlmResetHwInitFail_Object=MibScalar
pm1001lhAlmResetHwInitFail=_Pm1001lhAlmResetHwInitFail_Object((1,3,6,1,4,1,20044,10,2,1,2,194,4),_Pm1001lhAlmResetHwInitFail_Type())
pm1001lhAlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmResetHwInitFail.setStatus(_A)
_Pm1001lhAlmSwInitFail_Type=EkiOnOff
_Pm1001lhAlmSwInitFail_Object=MibScalar
pm1001lhAlmSwInitFail=_Pm1001lhAlmSwInitFail_Object((1,3,6,1,4,1,20044,10,2,1,2,194,5),_Pm1001lhAlmSwInitFail_Type())
pm1001lhAlmSwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmSwInitFail.setStatus(_A)
_Pm1001lhAlmmodInitFailLevel3_ObjectIdentity=ObjectIdentity
pm1001lhAlmmodInitFailLevel3=_Pm1001lhAlmmodInitFailLevel3_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,2,195))
_Pm1001lhAlmGwIdentFail_Type=EkiOnOff
_Pm1001lhAlmGwIdentFail_Object=MibScalar
pm1001lhAlmGwIdentFail=_Pm1001lhAlmGwIdentFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,1),_Pm1001lhAlmGwIdentFail_Type())
pm1001lhAlmGwIdentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmGwIdentFail.setStatus(_A)
_Pm1001lhAlmObmTypeReadFail_Type=EkiOnOff
_Pm1001lhAlmObmTypeReadFail_Object=MibScalar
pm1001lhAlmObmTypeReadFail=_Pm1001lhAlmObmTypeReadFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,2),_Pm1001lhAlmObmTypeReadFail_Type())
pm1001lhAlmObmTypeReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmObmTypeReadFail.setStatus(_A)
_Pm1001lhAlmInitModuleFail_Type=EkiOnOff
_Pm1001lhAlmInitModuleFail_Object=MibScalar
pm1001lhAlmInitModuleFail=_Pm1001lhAlmInitModuleFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,3),_Pm1001lhAlmInitModuleFail_Type())
pm1001lhAlmInitModuleFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmInitModuleFail.setStatus(_A)
_Pm1001lhAlmXfp1InitFail_Type=EkiOnOff
_Pm1001lhAlmXfp1InitFail_Object=MibScalar
pm1001lhAlmXfp1InitFail=_Pm1001lhAlmXfp1InitFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,5),_Pm1001lhAlmXfp1InitFail_Type())
pm1001lhAlmXfp1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmXfp1InitFail.setStatus(_A)
_Pm1001lhAlmXfp2InitFail_Type=EkiOnOff
_Pm1001lhAlmXfp2InitFail_Object=MibScalar
pm1001lhAlmXfp2InitFail=_Pm1001lhAlmXfp2InitFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,6),_Pm1001lhAlmXfp2InitFail_Type())
pm1001lhAlmXfp2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmXfp2InitFail.setStatus(_A)
_Pm1001lhAlmLine1InitFail_Type=EkiOnOff
_Pm1001lhAlmLine1InitFail_Object=MibScalar
pm1001lhAlmLine1InitFail=_Pm1001lhAlmLine1InitFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,7),_Pm1001lhAlmLine1InitFail_Type())
pm1001lhAlmLine1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLine1InitFail.setStatus(_A)
_Pm1001lhAlmClient1InitFail_Type=EkiOnOff
_Pm1001lhAlmClient1InitFail_Object=MibScalar
pm1001lhAlmClient1InitFail=_Pm1001lhAlmClient1InitFail_Object((1,3,6,1,4,1,20044,10,2,1,2,195,9),_Pm1001lhAlmClient1InitFail_Type())
pm1001lhAlmClient1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClient1InitFail.setStatus(_A)
_Pm1001lhAlmOtherCrit_ObjectIdentity=ObjectIdentity
pm1001lhAlmOtherCrit=_Pm1001lhAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,3))
_Pm1001lhAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm1001lhAlmsynthAlm0=_Pm1001lhAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,10,2,1,3,0))
_Pm1001lhAlmModGlobFail_Type=EkiOnOff
_Pm1001lhAlmModGlobFail_Object=MibScalar
pm1001lhAlmModGlobFail=_Pm1001lhAlmModGlobFail_Object((1,3,6,1,4,1,20044,10,2,1,3,0,9),_Pm1001lhAlmModGlobFail_Type())
pm1001lhAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmModGlobFail.setStatus(_A)
_Pm1001lhAlmDefFuseA_Type=EkiOnOff
_Pm1001lhAlmDefFuseA_Object=MibScalar
pm1001lhAlmDefFuseA=_Pm1001lhAlmDefFuseA_Object((1,3,6,1,4,1,20044,10,2,1,3,0,15),_Pm1001lhAlmDefFuseA_Type())
pm1001lhAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmDefFuseA.setStatus(_A)
_Pm1001lhAlmDefFuseB_Type=EkiOnOff
_Pm1001lhAlmDefFuseB_Object=MibScalar
pm1001lhAlmDefFuseB=_Pm1001lhAlmDefFuseB_Object((1,3,6,1,4,1,20044,10,2,1,3,0,16),_Pm1001lhAlmDefFuseB_Type())
pm1001lhAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmDefFuseB.setStatus(_A)
_Pm1001lhAlmClient_ObjectIdentity=ObjectIdentity
pm1001lhAlmClient=_Pm1001lhAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2))
_Pm1001lhAlmClientNurg_ObjectIdentity=ObjectIdentity
pm1001lhAlmClientNurg=_Pm1001lhAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,1))
_Pm1001lhAlmclientXfpWarnings_ObjectIdentity=ObjectIdentity
pm1001lhAlmclientXfpWarnings=_Pm1001lhAlmclientXfpWarnings_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,1,48))
_Pm1001lhAlmClientTxPowerLowWarning_Type=EkiOnOff
_Pm1001lhAlmClientTxPowerLowWarning_Object=MibScalar
pm1001lhAlmClientTxPowerLowWarning=_Pm1001lhAlmClientTxPowerLowWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,1),_Pm1001lhAlmClientTxPowerLowWarning_Type())
pm1001lhAlmClientTxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxPowerLowWarning.setStatus(_A)
_Pm1001lhAlmClientTxPowerHighWarning_Type=EkiOnOff
_Pm1001lhAlmClientTxPowerHighWarning_Object=MibScalar
pm1001lhAlmClientTxPowerHighWarning=_Pm1001lhAlmClientTxPowerHighWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,2),_Pm1001lhAlmClientTxPowerHighWarning_Type())
pm1001lhAlmClientTxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxPowerHighWarning.setStatus(_A)
_Pm1001lhAlmClientTxBiasLowWarning_Type=EkiOnOff
_Pm1001lhAlmClientTxBiasLowWarning_Object=MibScalar
pm1001lhAlmClientTxBiasLowWarning=_Pm1001lhAlmClientTxBiasLowWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,3),_Pm1001lhAlmClientTxBiasLowWarning_Type())
pm1001lhAlmClientTxBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxBiasLowWarning.setStatus(_A)
_Pm1001lhAlmClientTxBiasHighWarning_Type=EkiOnOff
_Pm1001lhAlmClientTxBiasHighWarning_Object=MibScalar
pm1001lhAlmClientTxBiasHighWarning=_Pm1001lhAlmClientTxBiasHighWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,4),_Pm1001lhAlmClientTxBiasHighWarning_Type())
pm1001lhAlmClientTxBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxBiasHighWarning.setStatus(_A)
_Pm1001lhAlmClientTempLowWarning_Type=EkiOnOff
_Pm1001lhAlmClientTempLowWarning_Object=MibScalar
pm1001lhAlmClientTempLowWarning=_Pm1001lhAlmClientTempLowWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,7),_Pm1001lhAlmClientTempLowWarning_Type())
pm1001lhAlmClientTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTempLowWarning.setStatus(_A)
_Pm1001lhAlmClientTempHighWarning_Type=EkiOnOff
_Pm1001lhAlmClientTempHighWarning_Object=MibScalar
pm1001lhAlmClientTempHighWarning=_Pm1001lhAlmClientTempHighWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,8),_Pm1001lhAlmClientTempHighWarning_Type())
pm1001lhAlmClientTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTempHighWarning.setStatus(_A)
_Pm1001lhAlmClientRxPowerLowWarning_Type=EkiOnOff
_Pm1001lhAlmClientRxPowerLowWarning_Object=MibScalar
pm1001lhAlmClientRxPowerLowWarning=_Pm1001lhAlmClientRxPowerLowWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,15),_Pm1001lhAlmClientRxPowerLowWarning_Type())
pm1001lhAlmClientRxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientRxPowerLowWarning.setStatus(_A)
_Pm1001lhAlmClientRxPowerHighWarning_Type=EkiOnOff
_Pm1001lhAlmClientRxPowerHighWarning_Object=MibScalar
pm1001lhAlmClientRxPowerHighWarning=_Pm1001lhAlmClientRxPowerHighWarning_Object((1,3,6,1,4,1,20044,10,2,2,1,48,16),_Pm1001lhAlmClientRxPowerHighWarning_Type())
pm1001lhAlmClientRxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientRxPowerHighWarning.setStatus(_A)
_Pm1001lhAlmClientUrg_ObjectIdentity=ObjectIdentity
pm1001lhAlmClientUrg=_Pm1001lhAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,2))
_Pm1001lhAlmclientXfpAlarm1_ObjectIdentity=ObjectIdentity
pm1001lhAlmclientXfpAlarm1=_Pm1001lhAlmclientXfpAlarm1_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,2,32))
_Pm1001lhAlmClientTxPowerLowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientTxPowerLowAlarm_Object=MibScalar
pm1001lhAlmClientTxPowerLowAlarm=_Pm1001lhAlmClientTxPowerLowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,1),_Pm1001lhAlmClientTxPowerLowAlarm_Type())
pm1001lhAlmClientTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxPowerLowAlarm.setStatus(_A)
_Pm1001lhAlmClientTxPowerHighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientTxPowerHighAlarm_Object=MibScalar
pm1001lhAlmClientTxPowerHighAlarm=_Pm1001lhAlmClientTxPowerHighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,2),_Pm1001lhAlmClientTxPowerHighAlarm_Type())
pm1001lhAlmClientTxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxPowerHighAlarm.setStatus(_A)
_Pm1001lhAlmClientTxBiasLowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientTxBiasLowAlarm_Object=MibScalar
pm1001lhAlmClientTxBiasLowAlarm=_Pm1001lhAlmClientTxBiasLowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,3),_Pm1001lhAlmClientTxBiasLowAlarm_Type())
pm1001lhAlmClientTxBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxBiasLowAlarm.setStatus(_A)
_Pm1001lhAlmClientTxBiasHighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientTxBiasHighAlarm_Object=MibScalar
pm1001lhAlmClientTxBiasHighAlarm=_Pm1001lhAlmClientTxBiasHighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,4),_Pm1001lhAlmClientTxBiasHighAlarm_Type())
pm1001lhAlmClientTxBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxBiasHighAlarm.setStatus(_A)
_Pm1001lhAlmClientTempLowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientTempLowAlarm_Object=MibScalar
pm1001lhAlmClientTempLowAlarm=_Pm1001lhAlmClientTempLowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,7),_Pm1001lhAlmClientTempLowAlarm_Type())
pm1001lhAlmClientTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTempLowAlarm.setStatus(_A)
_Pm1001lhAlmClientTempHighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientTempHighAlarm_Object=MibScalar
pm1001lhAlmClientTempHighAlarm=_Pm1001lhAlmClientTempHighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,8),_Pm1001lhAlmClientTempHighAlarm_Type())
pm1001lhAlmClientTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTempHighAlarm.setStatus(_A)
_Pm1001lhAlmClientRxPowerLowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientRxPowerLowAlarm_Object=MibScalar
pm1001lhAlmClientRxPowerLowAlarm=_Pm1001lhAlmClientRxPowerLowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,15),_Pm1001lhAlmClientRxPowerLowAlarm_Type())
pm1001lhAlmClientRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientRxPowerLowAlarm.setStatus(_A)
_Pm1001lhAlmClientRxPowerHighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientRxPowerHighAlarm_Object=MibScalar
pm1001lhAlmClientRxPowerHighAlarm=_Pm1001lhAlmClientRxPowerHighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,32,16),_Pm1001lhAlmClientRxPowerHighAlarm_Type())
pm1001lhAlmClientRxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientRxPowerHighAlarm.setStatus(_A)
_Pm1001lhAlmclientXfpSupplyAlarm_ObjectIdentity=ObjectIdentity
pm1001lhAlmclientXfpSupplyAlarm=_Pm1001lhAlmclientXfpSupplyAlarm_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,2,64))
_Pm1001lhAlmClientVee5LowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVee5LowAlarm_Object=MibScalar
pm1001lhAlmClientVee5LowAlarm=_Pm1001lhAlmClientVee5LowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,1),_Pm1001lhAlmClientVee5LowAlarm_Type())
pm1001lhAlmClientVee5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVee5LowAlarm.setStatus(_A)
_Pm1001lhAlmClientVee5HighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVee5HighAlarm_Object=MibScalar
pm1001lhAlmClientVee5HighAlarm=_Pm1001lhAlmClientVee5HighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,2),_Pm1001lhAlmClientVee5HighAlarm_Type())
pm1001lhAlmClientVee5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVee5HighAlarm.setStatus(_A)
_Pm1001lhAlmClientVcc2LowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVcc2LowAlarm_Object=MibScalar
pm1001lhAlmClientVcc2LowAlarm=_Pm1001lhAlmClientVcc2LowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,3),_Pm1001lhAlmClientVcc2LowAlarm_Type())
pm1001lhAlmClientVcc2LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc2LowAlarm.setStatus(_A)
_Pm1001lhAlmClientVcc2HighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVcc2HighAlarm_Object=MibScalar
pm1001lhAlmClientVcc2HighAlarm=_Pm1001lhAlmClientVcc2HighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,4),_Pm1001lhAlmClientVcc2HighAlarm_Type())
pm1001lhAlmClientVcc2HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc2HighAlarm.setStatus(_A)
_Pm1001lhAlmClientVcc3LowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVcc3LowAlarm_Object=MibScalar
pm1001lhAlmClientVcc3LowAlarm=_Pm1001lhAlmClientVcc3LowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,5),_Pm1001lhAlmClientVcc3LowAlarm_Type())
pm1001lhAlmClientVcc3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc3LowAlarm.setStatus(_A)
_Pm1001lhAlmClientVcc3HighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVcc3HighAlarm_Object=MibScalar
pm1001lhAlmClientVcc3HighAlarm=_Pm1001lhAlmClientVcc3HighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,6),_Pm1001lhAlmClientVcc3HighAlarm_Type())
pm1001lhAlmClientVcc3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc3HighAlarm.setStatus(_A)
_Pm1001lhAlmClientVcc5LowAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVcc5LowAlarm_Object=MibScalar
pm1001lhAlmClientVcc5LowAlarm=_Pm1001lhAlmClientVcc5LowAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,7),_Pm1001lhAlmClientVcc5LowAlarm_Type())
pm1001lhAlmClientVcc5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc5LowAlarm.setStatus(_A)
_Pm1001lhAlmClientVcc5HighAlarm_Type=EkiOnOff
_Pm1001lhAlmClientVcc5HighAlarm_Object=MibScalar
pm1001lhAlmClientVcc5HighAlarm=_Pm1001lhAlmClientVcc5HighAlarm_Object((1,3,6,1,4,1,20044,10,2,2,2,64,8),_Pm1001lhAlmClientVcc5HighAlarm_Type())
pm1001lhAlmClientVcc5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc5HighAlarm.setStatus(_A)
_Pm1001lhAlmClientVee5LowWarning_Type=EkiOnOff
_Pm1001lhAlmClientVee5LowWarning_Object=MibScalar
pm1001lhAlmClientVee5LowWarning=_Pm1001lhAlmClientVee5LowWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,9),_Pm1001lhAlmClientVee5LowWarning_Type())
pm1001lhAlmClientVee5LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVee5LowWarning.setStatus(_A)
_Pm1001lhAlmClientVee5HighWarning_Type=EkiOnOff
_Pm1001lhAlmClientVee5HighWarning_Object=MibScalar
pm1001lhAlmClientVee5HighWarning=_Pm1001lhAlmClientVee5HighWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,10),_Pm1001lhAlmClientVee5HighWarning_Type())
pm1001lhAlmClientVee5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVee5HighWarning.setStatus(_A)
_Pm1001lhAlmClientVcc2LowWarning_Type=EkiOnOff
_Pm1001lhAlmClientVcc2LowWarning_Object=MibScalar
pm1001lhAlmClientVcc2LowWarning=_Pm1001lhAlmClientVcc2LowWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,11),_Pm1001lhAlmClientVcc2LowWarning_Type())
pm1001lhAlmClientVcc2LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc2LowWarning.setStatus(_A)
_Pm1001lhAlmClientVcc2HighWarning_Type=EkiOnOff
_Pm1001lhAlmClientVcc2HighWarning_Object=MibScalar
pm1001lhAlmClientVcc2HighWarning=_Pm1001lhAlmClientVcc2HighWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,12),_Pm1001lhAlmClientVcc2HighWarning_Type())
pm1001lhAlmClientVcc2HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc2HighWarning.setStatus(_A)
_Pm1001lhAlmClientVcc3LowWarning_Type=EkiOnOff
_Pm1001lhAlmClientVcc3LowWarning_Object=MibScalar
pm1001lhAlmClientVcc3LowWarning=_Pm1001lhAlmClientVcc3LowWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,13),_Pm1001lhAlmClientVcc3LowWarning_Type())
pm1001lhAlmClientVcc3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc3LowWarning.setStatus(_A)
_Pm1001lhAlmClientVcc3HighWarning_Type=EkiOnOff
_Pm1001lhAlmClientVcc3HighWarning_Object=MibScalar
pm1001lhAlmClientVcc3HighWarning=_Pm1001lhAlmClientVcc3HighWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,14),_Pm1001lhAlmClientVcc3HighWarning_Type())
pm1001lhAlmClientVcc3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc3HighWarning.setStatus(_A)
_Pm1001lhAlmClientVcc5LowWarning_Type=EkiOnOff
_Pm1001lhAlmClientVcc5LowWarning_Object=MibScalar
pm1001lhAlmClientVcc5LowWarning=_Pm1001lhAlmClientVcc5LowWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,15),_Pm1001lhAlmClientVcc5LowWarning_Type())
pm1001lhAlmClientVcc5LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc5LowWarning.setStatus(_A)
_Pm1001lhAlmClientVcc5HighWarning_Type=EkiOnOff
_Pm1001lhAlmClientVcc5HighWarning_Object=MibScalar
pm1001lhAlmClientVcc5HighWarning=_Pm1001lhAlmClientVcc5HighWarning_Object((1,3,6,1,4,1,20044,10,2,2,2,64,16),_Pm1001lhAlmClientVcc5HighWarning_Type())
pm1001lhAlmClientVcc5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientVcc5HighWarning.setStatus(_A)
_Pm1001lhAlmClientCrit_ObjectIdentity=ObjectIdentity
pm1001lhAlmClientCrit=_Pm1001lhAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,3))
_Pm1001lhAlmsynthAlmPort_ObjectIdentity=ObjectIdentity
pm1001lhAlmsynthAlmPort=_Pm1001lhAlmsynthAlmPort_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,3,8))
_Pm1001lhAlmClientXfpAbsent_Type=EkiOnOff
_Pm1001lhAlmClientXfpAbsent_Object=MibScalar
pm1001lhAlmClientXfpAbsent=_Pm1001lhAlmClientXfpAbsent_Object((1,3,6,1,4,1,20044,10,2,2,3,8,1),_Pm1001lhAlmClientXfpAbsent_Type())
pm1001lhAlmClientXfpAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientXfpAbsent.setStatus(_A)
_Pm1001lhAlmClientDdmAbsent_Type=EkiOnOff
_Pm1001lhAlmClientDdmAbsent_Object=MibScalar
pm1001lhAlmClientDdmAbsent=_Pm1001lhAlmClientDdmAbsent_Object((1,3,6,1,4,1,20044,10,2,2,3,8,2),_Pm1001lhAlmClientDdmAbsent_Type())
pm1001lhAlmClientDdmAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientDdmAbsent.setStatus(_A)
_Pm1001lhAlmClientHwFail_Type=EkiOnOff
_Pm1001lhAlmClientHwFail_Object=MibScalar
pm1001lhAlmClientHwFail=_Pm1001lhAlmClientHwFail_Object((1,3,6,1,4,1,20044,10,2,2,3,8,4),_Pm1001lhAlmClientHwFail_Type())
pm1001lhAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientHwFail.setStatus(_A)
_Pm1001lhAlmClientDwLsd_Type=EkiOnOff
_Pm1001lhAlmClientDwLsd_Object=MibScalar
pm1001lhAlmClientDwLsd=_Pm1001lhAlmClientDwLsd_Object((1,3,6,1,4,1,20044,10,2,2,3,8,5),_Pm1001lhAlmClientDwLsd_Type())
pm1001lhAlmClientDwLsd.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientDwLsd.setStatus(_A)
_Pm1001lhAlmClientLocalOos_Type=EkiOnOff
_Pm1001lhAlmClientLocalOos_Object=MibScalar
pm1001lhAlmClientLocalOos=_Pm1001lhAlmClientLocalOos_Object((1,3,6,1,4,1,20044,10,2,2,3,8,6),_Pm1001lhAlmClientLocalOos_Type())
pm1001lhAlmClientLocalOos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientLocalOos.setStatus(_A)
_Pm1001lhAlmClientDwCais_Type=EkiOnOff
_Pm1001lhAlmClientDwCais_Object=MibScalar
pm1001lhAlmClientDwCais=_Pm1001lhAlmClientDwCais_Object((1,3,6,1,4,1,20044,10,2,2,3,8,8),_Pm1001lhAlmClientDwCais_Type())
pm1001lhAlmClientDwCais.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientDwCais.setStatus(_A)
_Pm1001lhAlmClientXfpDdmWarning_Type=EkiOnOff
_Pm1001lhAlmClientXfpDdmWarning_Object=MibScalar
pm1001lhAlmClientXfpDdmWarning=_Pm1001lhAlmClientXfpDdmWarning_Object((1,3,6,1,4,1,20044,10,2,2,3,8,9),_Pm1001lhAlmClientXfpDdmWarning_Type())
pm1001lhAlmClientXfpDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientXfpDdmWarning.setStatus(_A)
_Pm1001lhAlmClientXfpDdmAlm_Type=EkiOnOff
_Pm1001lhAlmClientXfpDdmAlm_Object=MibScalar
pm1001lhAlmClientXfpDdmAlm=_Pm1001lhAlmClientXfpDdmAlm_Object((1,3,6,1,4,1,20044,10,2,2,3,8,10),_Pm1001lhAlmClientXfpDdmAlm_Type())
pm1001lhAlmClientXfpDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientXfpDdmAlm.setStatus(_A)
_Pm1001lhAlmClientFail_Type=EkiOnOff
_Pm1001lhAlmClientFail_Object=MibScalar
pm1001lhAlmClientFail=_Pm1001lhAlmClientFail_Object((1,3,6,1,4,1,20044,10,2,2,3,8,12),_Pm1001lhAlmClientFail_Type())
pm1001lhAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientFail.setStatus(_A)
_Pm1001lhAlmClientUpCsf_Type=EkiOnOff
_Pm1001lhAlmClientUpCsf_Object=MibScalar
pm1001lhAlmClientUpCsf=_Pm1001lhAlmClientUpCsf_Object((1,3,6,1,4,1,20044,10,2,2,3,8,16),_Pm1001lhAlmClientUpCsf_Type())
pm1001lhAlmClientUpCsf.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientUpCsf.setStatus(_A)
_Pm1001lhAlmclientAccessioAlm_ObjectIdentity=ObjectIdentity
pm1001lhAlmclientAccessioAlm=_Pm1001lhAlmclientAccessioAlm_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,3,16))
_Pm1001lhAlmClientDwLasFail_Type=EkiOnOff
_Pm1001lhAlmClientDwLasFail_Object=MibScalar
pm1001lhAlmClientDwLasFail=_Pm1001lhAlmClientDwLasFail_Object((1,3,6,1,4,1,20044,10,2,2,3,16,1),_Pm1001lhAlmClientDwLasFail_Type())
pm1001lhAlmClientDwLasFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientDwLasFail.setStatus(_A)
_Pm1001lhAlmClientUpLos_Type=EkiOnOff
_Pm1001lhAlmClientUpLos_Object=MibScalar
pm1001lhAlmClientUpLos=_Pm1001lhAlmClientUpLos_Object((1,3,6,1,4,1,20044,10,2,2,3,16,4),_Pm1001lhAlmClientUpLos_Type())
pm1001lhAlmClientUpLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientUpLos.setStatus(_A)
_Pm1001lhAlmclientXfpAlarm2_ObjectIdentity=ObjectIdentity
pm1001lhAlmclientXfpAlarm2=_Pm1001lhAlmclientXfpAlarm2_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,3,40))
_Pm1001lhAlmClientModNr_Type=EkiOnOff
_Pm1001lhAlmClientModNr_Object=MibScalar
pm1001lhAlmClientModNr=_Pm1001lhAlmClientModNr_Object((1,3,6,1,4,1,20044,10,2,2,3,40,2),_Pm1001lhAlmClientModNr_Type())
pm1001lhAlmClientModNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientModNr.setStatus(_A)
_Pm1001lhAlmClientRxCdrNotLocked1_Type=EkiOnOff
_Pm1001lhAlmClientRxCdrNotLocked1_Object=MibScalar
pm1001lhAlmClientRxCdrNotLocked1=_Pm1001lhAlmClientRxCdrNotLocked1_Object((1,3,6,1,4,1,20044,10,2,2,3,40,3),_Pm1001lhAlmClientRxCdrNotLocked1_Type())
pm1001lhAlmClientRxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientRxCdrNotLocked1.setStatus(_A)
_Pm1001lhAlmClientRxNr_Type=EkiOnOff
_Pm1001lhAlmClientRxNr_Object=MibScalar
pm1001lhAlmClientRxNr=_Pm1001lhAlmClientRxNr_Object((1,3,6,1,4,1,20044,10,2,2,3,40,5),_Pm1001lhAlmClientRxNr_Type())
pm1001lhAlmClientRxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientRxNr.setStatus(_A)
_Pm1001lhAlmClientTxCdrNotLocked1_Type=EkiOnOff
_Pm1001lhAlmClientTxCdrNotLocked1_Object=MibScalar
pm1001lhAlmClientTxCdrNotLocked1=_Pm1001lhAlmClientTxCdrNotLocked1_Object((1,3,6,1,4,1,20044,10,2,2,3,40,6),_Pm1001lhAlmClientTxCdrNotLocked1_Type())
pm1001lhAlmClientTxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxCdrNotLocked1.setStatus(_A)
_Pm1001lhAlmClientTxFault_Type=EkiOnOff
_Pm1001lhAlmClientTxFault_Object=MibScalar
pm1001lhAlmClientTxFault=_Pm1001lhAlmClientTxFault_Object((1,3,6,1,4,1,20044,10,2,2,3,40,7),_Pm1001lhAlmClientTxFault_Type())
pm1001lhAlmClientTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxFault.setStatus(_A)
_Pm1001lhAlmClientTxNr_Type=EkiOnOff
_Pm1001lhAlmClientTxNr_Object=MibScalar
pm1001lhAlmClientTxNr=_Pm1001lhAlmClientTxNr_Object((1,3,6,1,4,1,20044,10,2,2,3,40,8),_Pm1001lhAlmClientTxNr_Type())
pm1001lhAlmClientTxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTxNr.setStatus(_A)
_Pm1001lhAlmClientWavelengthUnlocked_Type=EkiOnOff
_Pm1001lhAlmClientWavelengthUnlocked_Object=MibScalar
pm1001lhAlmClientWavelengthUnlocked=_Pm1001lhAlmClientWavelengthUnlocked_Object((1,3,6,1,4,1,20044,10,2,2,3,40,14),_Pm1001lhAlmClientWavelengthUnlocked_Type())
pm1001lhAlmClientWavelengthUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientWavelengthUnlocked.setStatus(_A)
_Pm1001lhAlmClientTecFault_Type=EkiOnOff
_Pm1001lhAlmClientTecFault_Object=MibScalar
pm1001lhAlmClientTecFault=_Pm1001lhAlmClientTecFault_Object((1,3,6,1,4,1,20044,10,2,2,3,40,15),_Pm1001lhAlmClientTecFault_Type())
pm1001lhAlmClientTecFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientTecFault.setStatus(_A)
_Pm1001lhAlmClientApdSupplyFault_Type=EkiOnOff
_Pm1001lhAlmClientApdSupplyFault_Object=MibScalar
pm1001lhAlmClientApdSupplyFault=_Pm1001lhAlmClientApdSupplyFault_Object((1,3,6,1,4,1,20044,10,2,2,3,40,16),_Pm1001lhAlmClientApdSupplyFault_Type())
pm1001lhAlmClientApdSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientApdSupplyFault.setStatus(_A)
_Pm1001lhAlmclientMapperDeAlm_ObjectIdentity=ObjectIdentity
pm1001lhAlmclientMapperDeAlm=_Pm1001lhAlmclientMapperDeAlm_ObjectIdentity((1,3,6,1,4,1,20044,10,2,2,3,72))
_Pm1001lhAlmClientUpAccOos_Type=EkiOnOff
_Pm1001lhAlmClientUpAccOos_Object=MibScalar
pm1001lhAlmClientUpAccOos=_Pm1001lhAlmClientUpAccOos_Object((1,3,6,1,4,1,20044,10,2,2,3,72,1),_Pm1001lhAlmClientUpAccOos_Type())
pm1001lhAlmClientUpAccOos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientUpAccOos.setStatus(_A)
_Pm1001lhAlmClientUpBufferOvl_Type=EkiOnOff
_Pm1001lhAlmClientUpBufferOvl_Object=MibScalar
pm1001lhAlmClientUpBufferOvl=_Pm1001lhAlmClientUpBufferOvl_Object((1,3,6,1,4,1,20044,10,2,2,3,72,10),_Pm1001lhAlmClientUpBufferOvl_Type())
pm1001lhAlmClientUpBufferOvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientUpBufferOvl.setStatus(_A)
_Pm1001lhAlmClientDwCsfDet_Type=EkiOnOff
_Pm1001lhAlmClientDwCsfDet_Object=MibScalar
pm1001lhAlmClientDwCsfDet=_Pm1001lhAlmClientDwCsfDet_Object((1,3,6,1,4,1,20044,10,2,2,3,72,11),_Pm1001lhAlmClientDwCsfDet_Type())
pm1001lhAlmClientDwCsfDet.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientDwCsfDet.setStatus(_A)
_Pm1001lhAlmClientDwBufferOvl_Type=EkiOnOff
_Pm1001lhAlmClientDwBufferOvl_Object=MibScalar
pm1001lhAlmClientDwBufferOvl=_Pm1001lhAlmClientDwBufferOvl_Object((1,3,6,1,4,1,20044,10,2,2,3,72,14),_Pm1001lhAlmClientDwBufferOvl_Type())
pm1001lhAlmClientDwBufferOvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmClientDwBufferOvl.setStatus(_A)
_Pm1001lhAlmLine_ObjectIdentity=ObjectIdentity
pm1001lhAlmLine=_Pm1001lhAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3))
_Pm1001lhAlmLineNurg_ObjectIdentity=ObjectIdentity
pm1001lhAlmLineNurg=_Pm1001lhAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,1))
_Pm1001lhAlmlineXfpWarnings_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineXfpWarnings=_Pm1001lhAlmlineXfpWarnings_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,1,209))
_Pm1001lhAlmLineTxPowerLowWarning_Type=EkiOnOff
_Pm1001lhAlmLineTxPowerLowWarning_Object=MibScalar
pm1001lhAlmLineTxPowerLowWarning=_Pm1001lhAlmLineTxPowerLowWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,1),_Pm1001lhAlmLineTxPowerLowWarning_Type())
pm1001lhAlmLineTxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxPowerLowWarning.setStatus(_A)
_Pm1001lhAlmLineTxPowerHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineTxPowerHighWarning_Object=MibScalar
pm1001lhAlmLineTxPowerHighWarning=_Pm1001lhAlmLineTxPowerHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,2),_Pm1001lhAlmLineTxPowerHighWarning_Type())
pm1001lhAlmLineTxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxPowerHighWarning.setStatus(_A)
_Pm1001lhAlmLineTxBiasLowWarning_Type=EkiOnOff
_Pm1001lhAlmLineTxBiasLowWarning_Object=MibScalar
pm1001lhAlmLineTxBiasLowWarning=_Pm1001lhAlmLineTxBiasLowWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,3),_Pm1001lhAlmLineTxBiasLowWarning_Type())
pm1001lhAlmLineTxBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxBiasLowWarning.setStatus(_A)
_Pm1001lhAlmLineTxBiasHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineTxBiasHighWarning_Object=MibScalar
pm1001lhAlmLineTxBiasHighWarning=_Pm1001lhAlmLineTxBiasHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,4),_Pm1001lhAlmLineTxBiasHighWarning_Type())
pm1001lhAlmLineTxBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxBiasHighWarning.setStatus(_A)
_Pm1001lhAlmLineTempLowWarning_Type=EkiOnOff
_Pm1001lhAlmLineTempLowWarning_Object=MibScalar
pm1001lhAlmLineTempLowWarning=_Pm1001lhAlmLineTempLowWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,7),_Pm1001lhAlmLineTempLowWarning_Type())
pm1001lhAlmLineTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTempLowWarning.setStatus(_A)
_Pm1001lhAlmLineTempHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineTempHighWarning_Object=MibScalar
pm1001lhAlmLineTempHighWarning=_Pm1001lhAlmLineTempHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,8),_Pm1001lhAlmLineTempHighWarning_Type())
pm1001lhAlmLineTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTempHighWarning.setStatus(_A)
_Pm1001lhAlmLineRxPowerLowWarning_Type=EkiOnOff
_Pm1001lhAlmLineRxPowerLowWarning_Object=MibScalar
pm1001lhAlmLineRxPowerLowWarning=_Pm1001lhAlmLineRxPowerLowWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,15),_Pm1001lhAlmLineRxPowerLowWarning_Type())
pm1001lhAlmLineRxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineRxPowerLowWarning.setStatus(_A)
_Pm1001lhAlmLineRxPowerHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineRxPowerHighWarning_Object=MibScalar
pm1001lhAlmLineRxPowerHighWarning=_Pm1001lhAlmLineRxPowerHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,209,16),_Pm1001lhAlmLineRxPowerHighWarning_Type())
pm1001lhAlmLineRxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineRxPowerHighWarning.setStatus(_A)
_Pm1001lhAlmlineOtxTlhWarnings_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineOtxTlhWarnings=_Pm1001lhAlmlineOtxTlhWarnings_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,1,225))
_Pm1001lhAlmLineModulatorAgingHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineModulatorAgingHighWarning_Object=MibScalar
pm1001lhAlmLineModulatorAgingHighWarning=_Pm1001lhAlmLineModulatorAgingHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,225,5),_Pm1001lhAlmLineModulatorAgingHighWarning_Type())
pm1001lhAlmLineModulatorAgingHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineModulatorAgingHighWarning.setStatus(_A)
_Pm1001lhAlmLineAgingHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineAgingHighWarning_Object=MibScalar
pm1001lhAlmLineAgingHighWarning=_Pm1001lhAlmLineAgingHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,225,6),_Pm1001lhAlmLineAgingHighWarning_Type())
pm1001lhAlmLineAgingHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineAgingHighWarning.setStatus(_A)
_Pm1001lhAlmLineFreqDevHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineFreqDevHighWarning_Object=MibScalar
pm1001lhAlmLineFreqDevHighWarning=_Pm1001lhAlmLineFreqDevHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,225,12),_Pm1001lhAlmLineFreqDevHighWarning_Type())
pm1001lhAlmLineFreqDevHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineFreqDevHighWarning.setStatus(_A)
_Pm1001lhAlmLineLaserTempHighWarning_Type=EkiOnOff
_Pm1001lhAlmLineLaserTempHighWarning_Object=MibScalar
pm1001lhAlmLineLaserTempHighWarning=_Pm1001lhAlmLineLaserTempHighWarning_Object((1,3,6,1,4,1,20044,10,2,3,1,225,14),_Pm1001lhAlmLineLaserTempHighWarning_Type())
pm1001lhAlmLineLaserTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineLaserTempHighWarning.setStatus(_A)
_Pm1001lhAlmLineUrg_ObjectIdentity=ObjectIdentity
pm1001lhAlmLineUrg=_Pm1001lhAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,2))
_Pm1001lhAlmdfrmBer_ObjectIdentity=ObjectIdentity
pm1001lhAlmdfrmBer=_Pm1001lhAlmdfrmBer_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,2,129))
_Pm1001lhAlmLineSignalDegrade_Type=EkiOnOff
_Pm1001lhAlmLineSignalDegrade_Object=MibScalar
pm1001lhAlmLineSignalDegrade=_Pm1001lhAlmLineSignalDegrade_Object((1,3,6,1,4,1,20044,10,2,3,2,129,1),_Pm1001lhAlmLineSignalDegrade_Type())
pm1001lhAlmLineSignalDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineSignalDegrade.setStatus(_A)
_Pm1001lhAlmLineSignalFail_Type=EkiOnOff
_Pm1001lhAlmLineSignalFail_Object=MibScalar
pm1001lhAlmLineSignalFail=_Pm1001lhAlmLineSignalFail_Object((1,3,6,1,4,1,20044,10,2,3,2,129,2),_Pm1001lhAlmLineSignalFail_Type())
pm1001lhAlmLineSignalFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineSignalFail.setStatus(_A)
_Pm1001lhAlmLineDegrade_Type=EkiOnOff
_Pm1001lhAlmLineDegrade_Object=MibScalar
pm1001lhAlmLineDegrade=_Pm1001lhAlmLineDegrade_Object((1,3,6,1,4,1,20044,10,2,3,2,129,5),_Pm1001lhAlmLineDegrade_Type())
pm1001lhAlmLineDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDegrade.setStatus(_A)
_Pm1001lhAlmlineXfpAlarm1_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineXfpAlarm1=_Pm1001lhAlmlineXfpAlarm1_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,2,208))
_Pm1001lhAlmLineTxPowerLowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineTxPowerLowAlarm_Object=MibScalar
pm1001lhAlmLineTxPowerLowAlarm=_Pm1001lhAlmLineTxPowerLowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,1),_Pm1001lhAlmLineTxPowerLowAlarm_Type())
pm1001lhAlmLineTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxPowerLowAlarm.setStatus(_A)
_Pm1001lhAlmLineTxPowerHighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineTxPowerHighAlarm_Object=MibScalar
pm1001lhAlmLineTxPowerHighAlarm=_Pm1001lhAlmLineTxPowerHighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,2),_Pm1001lhAlmLineTxPowerHighAlarm_Type())
pm1001lhAlmLineTxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxPowerHighAlarm.setStatus(_A)
_Pm1001lhAlmLineTxBiasLowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineTxBiasLowAlarm_Object=MibScalar
pm1001lhAlmLineTxBiasLowAlarm=_Pm1001lhAlmLineTxBiasLowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,3),_Pm1001lhAlmLineTxBiasLowAlarm_Type())
pm1001lhAlmLineTxBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxBiasLowAlarm.setStatus(_A)
_Pm1001lhAlmLineTxBiasHighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineTxBiasHighAlarm_Object=MibScalar
pm1001lhAlmLineTxBiasHighAlarm=_Pm1001lhAlmLineTxBiasHighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,4),_Pm1001lhAlmLineTxBiasHighAlarm_Type())
pm1001lhAlmLineTxBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxBiasHighAlarm.setStatus(_A)
_Pm1001lhAlmLineTempLowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineTempLowAlarm_Object=MibScalar
pm1001lhAlmLineTempLowAlarm=_Pm1001lhAlmLineTempLowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,7),_Pm1001lhAlmLineTempLowAlarm_Type())
pm1001lhAlmLineTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTempLowAlarm.setStatus(_A)
_Pm1001lhAlmLineTempHighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineTempHighAlarm_Object=MibScalar
pm1001lhAlmLineTempHighAlarm=_Pm1001lhAlmLineTempHighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,8),_Pm1001lhAlmLineTempHighAlarm_Type())
pm1001lhAlmLineTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTempHighAlarm.setStatus(_A)
_Pm1001lhAlmLineRxPowerLowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineRxPowerLowAlarm_Object=MibScalar
pm1001lhAlmLineRxPowerLowAlarm=_Pm1001lhAlmLineRxPowerLowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,15),_Pm1001lhAlmLineRxPowerLowAlarm_Type())
pm1001lhAlmLineRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineRxPowerLowAlarm.setStatus(_A)
_Pm1001lhAlmLineRxPowerHighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineRxPowerHighAlarm_Object=MibScalar
pm1001lhAlmLineRxPowerHighAlarm=_Pm1001lhAlmLineRxPowerHighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,208,16),_Pm1001lhAlmLineRxPowerHighAlarm_Type())
pm1001lhAlmLineRxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineRxPowerHighAlarm.setStatus(_A)
_Pm1001lhAlmlineXfpSupplyAlarm_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineXfpSupplyAlarm=_Pm1001lhAlmlineXfpSupplyAlarm_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,2,212))
_Pm1001lhAlmLineVee5LowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVee5LowAlarm_Object=MibScalar
pm1001lhAlmLineVee5LowAlarm=_Pm1001lhAlmLineVee5LowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,1),_Pm1001lhAlmLineVee5LowAlarm_Type())
pm1001lhAlmLineVee5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVee5LowAlarm.setStatus(_A)
_Pm1001lhAlmLineVee5HighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVee5HighAlarm_Object=MibScalar
pm1001lhAlmLineVee5HighAlarm=_Pm1001lhAlmLineVee5HighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,2),_Pm1001lhAlmLineVee5HighAlarm_Type())
pm1001lhAlmLineVee5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVee5HighAlarm.setStatus(_A)
_Pm1001lhAlmLineVcc2LowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVcc2LowAlarm_Object=MibScalar
pm1001lhAlmLineVcc2LowAlarm=_Pm1001lhAlmLineVcc2LowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,3),_Pm1001lhAlmLineVcc2LowAlarm_Type())
pm1001lhAlmLineVcc2LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc2LowAlarm.setStatus(_A)
_Pm1001lhAlmLineVcc2HighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVcc2HighAlarm_Object=MibScalar
pm1001lhAlmLineVcc2HighAlarm=_Pm1001lhAlmLineVcc2HighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,4),_Pm1001lhAlmLineVcc2HighAlarm_Type())
pm1001lhAlmLineVcc2HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc2HighAlarm.setStatus(_A)
_Pm1001lhAlmLineVcc3LowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVcc3LowAlarm_Object=MibScalar
pm1001lhAlmLineVcc3LowAlarm=_Pm1001lhAlmLineVcc3LowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,5),_Pm1001lhAlmLineVcc3LowAlarm_Type())
pm1001lhAlmLineVcc3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc3LowAlarm.setStatus(_A)
_Pm1001lhAlmLineVcc3HighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVcc3HighAlarm_Object=MibScalar
pm1001lhAlmLineVcc3HighAlarm=_Pm1001lhAlmLineVcc3HighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,6),_Pm1001lhAlmLineVcc3HighAlarm_Type())
pm1001lhAlmLineVcc3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc3HighAlarm.setStatus(_A)
_Pm1001lhAlmLineVcc5LowAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVcc5LowAlarm_Object=MibScalar
pm1001lhAlmLineVcc5LowAlarm=_Pm1001lhAlmLineVcc5LowAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,7),_Pm1001lhAlmLineVcc5LowAlarm_Type())
pm1001lhAlmLineVcc5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc5LowAlarm.setStatus(_A)
_Pm1001lhAlmLineVcc5HighAlarm_Type=EkiOnOff
_Pm1001lhAlmLineVcc5HighAlarm_Object=MibScalar
pm1001lhAlmLineVcc5HighAlarm=_Pm1001lhAlmLineVcc5HighAlarm_Object((1,3,6,1,4,1,20044,10,2,3,2,212,8),_Pm1001lhAlmLineVcc5HighAlarm_Type())
pm1001lhAlmLineVcc5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc5HighAlarm.setStatus(_A)
_Pm1001lhAlmLineVee5LowLineWarning_Type=EkiOnOff
_Pm1001lhAlmLineVee5LowLineWarning_Object=MibScalar
pm1001lhAlmLineVee5LowLineWarning=_Pm1001lhAlmLineVee5LowLineWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,9),_Pm1001lhAlmLineVee5LowLineWarning_Type())
pm1001lhAlmLineVee5LowLineWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVee5LowLineWarning.setStatus(_A)
_Pm1001lhAlmLineVee5HighWarning_Type=EkiOnOff
_Pm1001lhAlmLineVee5HighWarning_Object=MibScalar
pm1001lhAlmLineVee5HighWarning=_Pm1001lhAlmLineVee5HighWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,10),_Pm1001lhAlmLineVee5HighWarning_Type())
pm1001lhAlmLineVee5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVee5HighWarning.setStatus(_A)
_Pm1001lhAlmLineVcc2LowWarning_Type=EkiOnOff
_Pm1001lhAlmLineVcc2LowWarning_Object=MibScalar
pm1001lhAlmLineVcc2LowWarning=_Pm1001lhAlmLineVcc2LowWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,11),_Pm1001lhAlmLineVcc2LowWarning_Type())
pm1001lhAlmLineVcc2LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc2LowWarning.setStatus(_A)
_Pm1001lhAlmLineVcc2HighWarning_Type=EkiOnOff
_Pm1001lhAlmLineVcc2HighWarning_Object=MibScalar
pm1001lhAlmLineVcc2HighWarning=_Pm1001lhAlmLineVcc2HighWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,12),_Pm1001lhAlmLineVcc2HighWarning_Type())
pm1001lhAlmLineVcc2HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc2HighWarning.setStatus(_A)
_Pm1001lhAlmLineVcc3LowWarning_Type=EkiOnOff
_Pm1001lhAlmLineVcc3LowWarning_Object=MibScalar
pm1001lhAlmLineVcc3LowWarning=_Pm1001lhAlmLineVcc3LowWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,13),_Pm1001lhAlmLineVcc3LowWarning_Type())
pm1001lhAlmLineVcc3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc3LowWarning.setStatus(_A)
_Pm1001lhAlmLineVcc3HighWarning_Type=EkiOnOff
_Pm1001lhAlmLineVcc3HighWarning_Object=MibScalar
pm1001lhAlmLineVcc3HighWarning=_Pm1001lhAlmLineVcc3HighWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,14),_Pm1001lhAlmLineVcc3HighWarning_Type())
pm1001lhAlmLineVcc3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc3HighWarning.setStatus(_A)
_Pm1001lhAlmLineVcc5LowWarning_Type=EkiOnOff
_Pm1001lhAlmLineVcc5LowWarning_Object=MibScalar
pm1001lhAlmLineVcc5LowWarning=_Pm1001lhAlmLineVcc5LowWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,15),_Pm1001lhAlmLineVcc5LowWarning_Type())
pm1001lhAlmLineVcc5LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc5LowWarning.setStatus(_A)
_Pm1001lhAlmLineVcc5HighWarning_Type=EkiOnOff
_Pm1001lhAlmLineVcc5HighWarning_Object=MibScalar
pm1001lhAlmLineVcc5HighWarning=_Pm1001lhAlmLineVcc5HighWarning_Object((1,3,6,1,4,1,20044,10,2,3,2,212,16),_Pm1001lhAlmLineVcc5HighWarning_Type())
pm1001lhAlmLineVcc5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineVcc5HighWarning.setStatus(_A)
_Pm1001lhAlmlineOtxTlhAlarms3_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineOtxTlhAlarms3=_Pm1001lhAlmlineOtxTlhAlarms3_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,2,224))
_Pm1001lhAlmLineModulatorAgingHighAla_Type=EkiOnOff
_Pm1001lhAlmLineModulatorAgingHighAla_Object=MibScalar
pm1001lhAlmLineModulatorAgingHighAla=_Pm1001lhAlmLineModulatorAgingHighAla_Object((1,3,6,1,4,1,20044,10,2,3,2,224,5),_Pm1001lhAlmLineModulatorAgingHighAla_Type())
pm1001lhAlmLineModulatorAgingHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineModulatorAgingHighAla.setStatus(_A)
_Pm1001lhAlmLineAgingHighAla_Type=EkiOnOff
_Pm1001lhAlmLineAgingHighAla_Object=MibScalar
pm1001lhAlmLineAgingHighAla=_Pm1001lhAlmLineAgingHighAla_Object((1,3,6,1,4,1,20044,10,2,3,2,224,6),_Pm1001lhAlmLineAgingHighAla_Type())
pm1001lhAlmLineAgingHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineAgingHighAla.setStatus(_A)
_Pm1001lhAlmLineCdrNotReady_Type=EkiOnOff
_Pm1001lhAlmLineCdrNotReady_Object=MibScalar
pm1001lhAlmLineCdrNotReady=_Pm1001lhAlmLineCdrNotReady_Object((1,3,6,1,4,1,20044,10,2,3,2,224,9),_Pm1001lhAlmLineCdrNotReady_Type())
pm1001lhAlmLineCdrNotReady.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineCdrNotReady.setStatus(_A)
_Pm1001lhAlmLineFreqDevHighAla_Type=EkiOnOff
_Pm1001lhAlmLineFreqDevHighAla_Object=MibScalar
pm1001lhAlmLineFreqDevHighAla=_Pm1001lhAlmLineFreqDevHighAla_Object((1,3,6,1,4,1,20044,10,2,3,2,224,12),_Pm1001lhAlmLineFreqDevHighAla_Type())
pm1001lhAlmLineFreqDevHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineFreqDevHighAla.setStatus(_A)
_Pm1001lhAlmLineLaserTempHighAla_Type=EkiOnOff
_Pm1001lhAlmLineLaserTempHighAla_Object=MibScalar
pm1001lhAlmLineLaserTempHighAla=_Pm1001lhAlmLineLaserTempHighAla_Object((1,3,6,1,4,1,20044,10,2,3,2,224,14),_Pm1001lhAlmLineLaserTempHighAla_Type())
pm1001lhAlmLineLaserTempHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineLaserTempHighAla.setStatus(_A)
_Pm1001lhAlmLineCrit_ObjectIdentity=ObjectIdentity
pm1001lhAlmLineCrit=_Pm1001lhAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,3))
_Pm1001lhAlmsynthAlmLine_ObjectIdentity=ObjectIdentity
pm1001lhAlmsynthAlmLine=_Pm1001lhAlmsynthAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,3,7))
_Pm1001lhAlmLineXfpAbsent_Type=EkiOnOff
_Pm1001lhAlmLineXfpAbsent_Object=MibScalar
pm1001lhAlmLineXfpAbsent=_Pm1001lhAlmLineXfpAbsent_Object((1,3,6,1,4,1,20044,10,2,3,3,7,1),_Pm1001lhAlmLineXfpAbsent_Type())
pm1001lhAlmLineXfpAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineXfpAbsent.setStatus(_A)
_Pm1001lhAlmLineXfpInitNotCompl_Type=EkiOnOff
_Pm1001lhAlmLineXfpInitNotCompl_Object=MibScalar
pm1001lhAlmLineXfpInitNotCompl=_Pm1001lhAlmLineXfpInitNotCompl_Object((1,3,6,1,4,1,20044,10,2,3,3,7,2),_Pm1001lhAlmLineXfpInitNotCompl_Type())
pm1001lhAlmLineXfpInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineXfpInitNotCompl.setStatus(_A)
_Pm1001lhAlmLineHwFail_Type=EkiOnOff
_Pm1001lhAlmLineHwFail_Object=MibScalar
pm1001lhAlmLineHwFail=_Pm1001lhAlmLineHwFail_Object((1,3,6,1,4,1,20044,10,2,3,3,7,4),_Pm1001lhAlmLineHwFail_Type())
pm1001lhAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineHwFail.setStatus(_A)
_Pm1001lhAlmLineXfpTxOff_Type=EkiOnOff
_Pm1001lhAlmLineXfpTxOff_Object=MibScalar
pm1001lhAlmLineXfpTxOff=_Pm1001lhAlmLineXfpTxOff_Object((1,3,6,1,4,1,20044,10,2,3,3,7,5),_Pm1001lhAlmLineXfpTxOff_Type())
pm1001lhAlmLineXfpTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineXfpTxOff.setStatus(_A)
_Pm1001lhAlmLineLocalOos_Type=EkiOnOff
_Pm1001lhAlmLineLocalOos_Object=MibScalar
pm1001lhAlmLineLocalOos=_Pm1001lhAlmLineLocalOos_Object((1,3,6,1,4,1,20044,10,2,3,3,7,6),_Pm1001lhAlmLineLocalOos_Type())
pm1001lhAlmLineLocalOos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineLocalOos.setStatus(_A)
_Pm1001lhAlmLineUpRdiIns_Type=EkiOnOff
_Pm1001lhAlmLineUpRdiIns_Object=MibScalar
pm1001lhAlmLineUpRdiIns=_Pm1001lhAlmLineUpRdiIns_Object((1,3,6,1,4,1,20044,10,2,3,3,7,8),_Pm1001lhAlmLineUpRdiIns_Type())
pm1001lhAlmLineUpRdiIns.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineUpRdiIns.setStatus(_A)
_Pm1001lhAlmLineDdmWarning_Type=EkiOnOff
_Pm1001lhAlmLineDdmWarning_Object=MibScalar
pm1001lhAlmLineDdmWarning=_Pm1001lhAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,10,2,3,3,7,9),_Pm1001lhAlmLineDdmWarning_Type())
pm1001lhAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDdmWarning.setStatus(_A)
_Pm1001lhAlmLineDdmAlm_Type=EkiOnOff
_Pm1001lhAlmLineDdmAlm_Object=MibScalar
pm1001lhAlmLineDdmAlm=_Pm1001lhAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,10,2,3,3,7,10),_Pm1001lhAlmLineDdmAlm_Type())
pm1001lhAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDdmAlm.setStatus(_A)
_Pm1001lhAlmLineFail_Type=EkiOnOff
_Pm1001lhAlmLineFail_Object=MibScalar
pm1001lhAlmLineFail=_Pm1001lhAlmLineFail_Object((1,3,6,1,4,1,20044,10,2,3,3,7,12),_Pm1001lhAlmLineFail_Type())
pm1001lhAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineFail.setStatus(_A)
_Pm1001lhAlmdfrmAlm_ObjectIdentity=ObjectIdentity
pm1001lhAlmdfrmAlm=_Pm1001lhAlmdfrmAlm_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,3,128))
_Pm1001lhAlmLineDwAisDet_Type=EkiOnOff
_Pm1001lhAlmLineDwAisDet_Object=MibScalar
pm1001lhAlmLineDwAisDet=_Pm1001lhAlmLineDwAisDet_Object((1,3,6,1,4,1,20044,10,2,3,3,128,1),_Pm1001lhAlmLineDwAisDet_Type())
pm1001lhAlmLineDwAisDet.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDwAisDet.setStatus(_A)
_Pm1001lhAlmLineDwRdiDet_Type=EkiOnOff
_Pm1001lhAlmLineDwRdiDet_Object=MibScalar
pm1001lhAlmLineDwRdiDet=_Pm1001lhAlmLineDwRdiDet_Object((1,3,6,1,4,1,20044,10,2,3,3,128,2),_Pm1001lhAlmLineDwRdiDet_Type())
pm1001lhAlmLineDwRdiDet.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDwRdiDet.setStatus(_A)
_Pm1001lhAlmLineDwOof_Type=EkiOnOff
_Pm1001lhAlmLineDwOof_Object=MibScalar
pm1001lhAlmLineDwOof=_Pm1001lhAlmLineDwOof_Object((1,3,6,1,4,1,20044,10,2,3,3,128,3),_Pm1001lhAlmLineDwOof_Type())
pm1001lhAlmLineDwOof.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDwOof.setStatus(_A)
_Pm1001lhAlmLineDwLof_Type=EkiOnOff
_Pm1001lhAlmLineDwLof_Object=MibScalar
pm1001lhAlmLineDwLof=_Pm1001lhAlmLineDwLof_Object((1,3,6,1,4,1,20044,10,2,3,3,128,4),_Pm1001lhAlmLineDwLof_Type())
pm1001lhAlmLineDwLof.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDwLof.setStatus(_A)
_Pm1001lhAlmLineFecFail_Type=EkiOnOff
_Pm1001lhAlmLineFecFail_Object=MibScalar
pm1001lhAlmLineFecFail=_Pm1001lhAlmLineFecFail_Object((1,3,6,1,4,1,20044,10,2,3,3,128,5),_Pm1001lhAlmLineFecFail_Type())
pm1001lhAlmLineFecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineFecFail.setStatus(_A)
_Pm1001lhAlmlineSyncAlarms_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineSyncAlarms=_Pm1001lhAlmlineSyncAlarms_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,3,133))
_Pm1001lhAlmLineDwLockerr_Type=EkiOnOff
_Pm1001lhAlmLineDwLockerr_Object=MibScalar
pm1001lhAlmLineDwLockerr=_Pm1001lhAlmLineDwLockerr_Object((1,3,6,1,4,1,20044,10,2,3,3,133,12),_Pm1001lhAlmLineDwLockerr_Type())
pm1001lhAlmLineDwLockerr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDwLockerr.setStatus(_A)
_Pm1001lhAlmLineUpLockerr_Type=EkiOnOff
_Pm1001lhAlmLineUpLockerr_Object=MibScalar
pm1001lhAlmLineUpLockerr=_Pm1001lhAlmLineUpLockerr_Object((1,3,6,1,4,1,20044,10,2,3,3,133,13),_Pm1001lhAlmLineUpLockerr_Type())
pm1001lhAlmLineUpLockerr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineUpLockerr.setStatus(_A)
_Pm1001lhAlmLineDwLos_Type=EkiOnOff
_Pm1001lhAlmLineDwLos_Object=MibScalar
pm1001lhAlmLineDwLos=_Pm1001lhAlmLineDwLos_Object((1,3,6,1,4,1,20044,10,2,3,3,133,16),_Pm1001lhAlmLineDwLos_Type())
pm1001lhAlmLineDwLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineDwLos.setStatus(_A)
_Pm1001lhAlmlineXfpAlarms2_ObjectIdentity=ObjectIdentity
pm1001lhAlmlineXfpAlarms2=_Pm1001lhAlmlineXfpAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,10,2,3,3,211))
_Pm1001lhAlmLineModNr_Type=EkiOnOff
_Pm1001lhAlmLineModNr_Object=MibScalar
pm1001lhAlmLineModNr=_Pm1001lhAlmLineModNr_Object((1,3,6,1,4,1,20044,10,2,3,3,211,2),_Pm1001lhAlmLineModNr_Type())
pm1001lhAlmLineModNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineModNr.setStatus(_A)
_Pm1001lhAlmLineRxCdrNotLocked1_Type=EkiOnOff
_Pm1001lhAlmLineRxCdrNotLocked1_Object=MibScalar
pm1001lhAlmLineRxCdrNotLocked1=_Pm1001lhAlmLineRxCdrNotLocked1_Object((1,3,6,1,4,1,20044,10,2,3,3,211,3),_Pm1001lhAlmLineRxCdrNotLocked1_Type())
pm1001lhAlmLineRxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineRxCdrNotLocked1.setStatus(_A)
_Pm1001lhAlmLineRxNr_Type=EkiOnOff
_Pm1001lhAlmLineRxNr_Object=MibScalar
pm1001lhAlmLineRxNr=_Pm1001lhAlmLineRxNr_Object((1,3,6,1,4,1,20044,10,2,3,3,211,5),_Pm1001lhAlmLineRxNr_Type())
pm1001lhAlmLineRxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineRxNr.setStatus(_A)
_Pm1001lhAlmLineTxCdrNotLocked1_Type=EkiOnOff
_Pm1001lhAlmLineTxCdrNotLocked1_Object=MibScalar
pm1001lhAlmLineTxCdrNotLocked1=_Pm1001lhAlmLineTxCdrNotLocked1_Object((1,3,6,1,4,1,20044,10,2,3,3,211,6),_Pm1001lhAlmLineTxCdrNotLocked1_Type())
pm1001lhAlmLineTxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxCdrNotLocked1.setStatus(_A)
_Pm1001lhAlmLineTxFault_Type=EkiOnOff
_Pm1001lhAlmLineTxFault_Object=MibScalar
pm1001lhAlmLineTxFault=_Pm1001lhAlmLineTxFault_Object((1,3,6,1,4,1,20044,10,2,3,3,211,7),_Pm1001lhAlmLineTxFault_Type())
pm1001lhAlmLineTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxFault.setStatus(_A)
_Pm1001lhAlmLineTxNr_Type=EkiOnOff
_Pm1001lhAlmLineTxNr_Object=MibScalar
pm1001lhAlmLineTxNr=_Pm1001lhAlmLineTxNr_Object((1,3,6,1,4,1,20044,10,2,3,3,211,8),_Pm1001lhAlmLineTxNr_Type())
pm1001lhAlmLineTxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTxNr.setStatus(_A)
_Pm1001lhAlmLineChannelNotAcquired_Type=EkiOnOff
_Pm1001lhAlmLineChannelNotAcquired_Object=MibScalar
pm1001lhAlmLineChannelNotAcquired=_Pm1001lhAlmLineChannelNotAcquired_Object((1,3,6,1,4,1,20044,10,2,3,3,211,10),_Pm1001lhAlmLineChannelNotAcquired_Type())
pm1001lhAlmLineChannelNotAcquired.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineChannelNotAcquired.setStatus(_A)
_Pm1001lhAlmLineWavelengthUnlocked_Type=EkiOnOff
_Pm1001lhAlmLineWavelengthUnlocked_Object=MibScalar
pm1001lhAlmLineWavelengthUnlocked=_Pm1001lhAlmLineWavelengthUnlocked_Object((1,3,6,1,4,1,20044,10,2,3,3,211,14),_Pm1001lhAlmLineWavelengthUnlocked_Type())
pm1001lhAlmLineWavelengthUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineWavelengthUnlocked.setStatus(_A)
_Pm1001lhAlmLineTecFault_Type=EkiOnOff
_Pm1001lhAlmLineTecFault_Object=MibScalar
pm1001lhAlmLineTecFault=_Pm1001lhAlmLineTecFault_Object((1,3,6,1,4,1,20044,10,2,3,3,211,15),_Pm1001lhAlmLineTecFault_Type())
pm1001lhAlmLineTecFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineTecFault.setStatus(_A)
_Pm1001lhAlmLineApdSupplyFault_Type=EkiOnOff
_Pm1001lhAlmLineApdSupplyFault_Object=MibScalar
pm1001lhAlmLineApdSupplyFault=_Pm1001lhAlmLineApdSupplyFault_Object((1,3,6,1,4,1,20044,10,2,3,3,211,16),_Pm1001lhAlmLineApdSupplyFault_Type())
pm1001lhAlmLineApdSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhAlmLineApdSupplyFault.setStatus(_A)
_Pm1001lhmeasures_ObjectIdentity=ObjectIdentity
pm1001lhmeasures=_Pm1001lhmeasures_ObjectIdentity((1,3,6,1,4,1,20044,10,3))
_Pm1001lhMesrOther_ObjectIdentity=ObjectIdentity
pm1001lhMesrOther=_Pm1001lhMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,10,3,1))
_Pm1001lhMesrsynth0_Type=EkiMeasureType
_Pm1001lhMesrsynth0_Object=MibScalar
pm1001lhMesrsynth0=_Pm1001lhMesrsynth0_Object((1,3,6,1,4,1,20044,10,3,1,0),_Pm1001lhMesrsynth0_Type())
pm1001lhMesrsynth0.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrsynth0.setStatus(_G)
_Pm1001lhMesrsynth1_Type=EkiMeasureType
_Pm1001lhMesrsynth1_Object=MibScalar
pm1001lhMesrsynth1=_Pm1001lhMesrsynth1_Object((1,3,6,1,4,1,20044,10,3,1,1),_Pm1001lhMesrsynth1_Type())
pm1001lhMesrsynth1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrsynth1.setStatus(_G)
_Pm1001lhMesrClient_ObjectIdentity=ObjectIdentity
pm1001lhMesrClient=_Pm1001lhMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,10,3,2))
class _Pm1001lhMesrclientModTempMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrclientModTempMeas_Type.__name__=_F
_Pm1001lhMesrclientModTempMeas_Object=MibScalar
pm1001lhMesrclientModTempMeas=_Pm1001lhMesrclientModTempMeas_Object((1,3,6,1,4,1,20044,10,3,2,16),_Pm1001lhMesrclientModTempMeas_Type())
pm1001lhMesrclientModTempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrclientModTempMeas.setStatus(_A)
class _Pm1001lhMesrclientBiasCurrentMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrclientBiasCurrentMeas_Type.__name__=_F
_Pm1001lhMesrclientBiasCurrentMeas_Object=MibScalar
pm1001lhMesrclientBiasCurrentMeas=_Pm1001lhMesrclientBiasCurrentMeas_Object((1,3,6,1,4,1,20044,10,3,2,32),_Pm1001lhMesrclientBiasCurrentMeas_Type())
pm1001lhMesrclientBiasCurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrclientBiasCurrentMeas.setStatus(_A)
class _Pm1001lhMesrclientTxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrclientTxPowerMeas_Type.__name__=_F
_Pm1001lhMesrclientTxPowerMeas_Object=MibScalar
pm1001lhMesrclientTxPowerMeas=_Pm1001lhMesrclientTxPowerMeas_Object((1,3,6,1,4,1,20044,10,3,2,40),_Pm1001lhMesrclientTxPowerMeas_Type())
pm1001lhMesrclientTxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrclientTxPowerMeas.setStatus(_A)
class _Pm1001lhMesrclientRxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrclientRxPowerMeas_Type.__name__=_F
_Pm1001lhMesrclientRxPowerMeas_Object=MibScalar
pm1001lhMesrclientRxPowerMeas=_Pm1001lhMesrclientRxPowerMeas_Object((1,3,6,1,4,1,20044,10,3,2,48),_Pm1001lhMesrclientRxPowerMeas_Type())
pm1001lhMesrclientRxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrclientRxPowerMeas.setStatus(_A)
_Pm1001lhMesrLine_ObjectIdentity=ObjectIdentity
pm1001lhMesrLine=_Pm1001lhMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,10,3,3))
class _Pm1001lhMesrlineModTempMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineModTempMeas_Type.__name__=_F
_Pm1001lhMesrlineModTempMeas_Object=MibScalar
pm1001lhMesrlineModTempMeas=_Pm1001lhMesrlineModTempMeas_Object((1,3,6,1,4,1,20044,10,3,3,208),_Pm1001lhMesrlineModTempMeas_Type())
pm1001lhMesrlineModTempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineModTempMeas.setStatus(_A)
class _Pm1001lhMesrlineReserved_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineReserved_Type.__name__=_F
_Pm1001lhMesrlineReserved_Object=MibScalar
pm1001lhMesrlineReserved=_Pm1001lhMesrlineReserved_Object((1,3,6,1,4,1,20044,10,3,3,209),_Pm1001lhMesrlineReserved_Type())
pm1001lhMesrlineReserved.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineReserved.setStatus(_G)
class _Pm1001lhMesrlineBiasCurrentMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineBiasCurrentMeas_Type.__name__=_F
_Pm1001lhMesrlineBiasCurrentMeas_Object=MibScalar
pm1001lhMesrlineBiasCurrentMeas=_Pm1001lhMesrlineBiasCurrentMeas_Object((1,3,6,1,4,1,20044,10,3,3,210),_Pm1001lhMesrlineBiasCurrentMeas_Type())
pm1001lhMesrlineBiasCurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineBiasCurrentMeas.setStatus(_A)
class _Pm1001lhMesrlineTxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineTxPowerMeas_Type.__name__=_F
_Pm1001lhMesrlineTxPowerMeas_Object=MibScalar
pm1001lhMesrlineTxPowerMeas=_Pm1001lhMesrlineTxPowerMeas_Object((1,3,6,1,4,1,20044,10,3,3,211),_Pm1001lhMesrlineTxPowerMeas_Type())
pm1001lhMesrlineTxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineTxPowerMeas.setStatus(_A)
class _Pm1001lhMesrlineRxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineRxPowerMeas_Type.__name__=_F
_Pm1001lhMesrlineRxPowerMeas_Object=MibScalar
pm1001lhMesrlineRxPowerMeas=_Pm1001lhMesrlineRxPowerMeas_Object((1,3,6,1,4,1,20044,10,3,3,212),_Pm1001lhMesrlineRxPowerMeas_Type())
pm1001lhMesrlineRxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineRxPowerMeas.setStatus(_A)
class _Pm1001lhMesrlineAux1Meas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineAux1Meas_Type.__name__=_F
_Pm1001lhMesrlineAux1Meas_Object=MibScalar
pm1001lhMesrlineAux1Meas=_Pm1001lhMesrlineAux1Meas_Object((1,3,6,1,4,1,20044,10,3,3,213),_Pm1001lhMesrlineAux1Meas_Type())
pm1001lhMesrlineAux1Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineAux1Meas.setStatus(_G)
class _Pm1001lhMesrlineAux2Meas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineAux2Meas_Type.__name__=_F
_Pm1001lhMesrlineAux2Meas_Object=MibScalar
pm1001lhMesrlineAux2Meas=_Pm1001lhMesrlineAux2Meas_Object((1,3,6,1,4,1,20044,10,3,3,214),_Pm1001lhMesrlineAux2Meas_Type())
pm1001lhMesrlineAux2Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineAux2Meas.setStatus(_G)
class _Pm1001lhMesrlineAging_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineAging_Type.__name__=_F
_Pm1001lhMesrlineAging_Object=MibScalar
pm1001lhMesrlineAging=_Pm1001lhMesrlineAging_Object((1,3,6,1,4,1,20044,10,3,3,224),_Pm1001lhMesrlineAging_Type())
pm1001lhMesrlineAging.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineAging.setStatus(_A)
class _Pm1001lhMesrlineLaserTemperature_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineLaserTemperature_Type.__name__=_F
_Pm1001lhMesrlineLaserTemperature_Object=MibScalar
pm1001lhMesrlineLaserTemperature=_Pm1001lhMesrlineLaserTemperature_Object((1,3,6,1,4,1,20044,10,3,3,225),_Pm1001lhMesrlineLaserTemperature_Type())
pm1001lhMesrlineLaserTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineLaserTemperature.setStatus(_G)
class _Pm1001lhMesrlineFreqDeviation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineFreqDeviation_Type.__name__=_F
_Pm1001lhMesrlineFreqDeviation_Object=MibScalar
pm1001lhMesrlineFreqDeviation=_Pm1001lhMesrlineFreqDeviation_Object((1,3,6,1,4,1,20044,10,3,3,226),_Pm1001lhMesrlineFreqDeviation_Type())
pm1001lhMesrlineFreqDeviation.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineFreqDeviation.setStatus(_A)
class _Pm1001lhMesrlineLaserWvlength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhMesrlineLaserWvlength_Type.__name__=_F
_Pm1001lhMesrlineLaserWvlength_Object=MibScalar
pm1001lhMesrlineLaserWvlength=_Pm1001lhMesrlineLaserWvlength_Object((1,3,6,1,4,1,20044,10,3,3,227),_Pm1001lhMesrlineLaserWvlength_Type())
pm1001lhMesrlineLaserWvlength.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMesrlineLaserWvlength.setStatus(_A)
_Pm1001lhcounters_ObjectIdentity=ObjectIdentity
pm1001lhcounters=_Pm1001lhcounters_ObjectIdentity((1,3,6,1,4,1,20044,10,4))
_Pm1001lhCntOther_ObjectIdentity=ObjectIdentity
pm1001lhCntOther=_Pm1001lhCntOther_ObjectIdentity((1,3,6,1,4,1,20044,10,4,1))
_Pm1001lhCntClient_ObjectIdentity=ObjectIdentity
pm1001lhCntClient=_Pm1001lhCntClient_ObjectIdentity((1,3,6,1,4,1,20044,10,4,2))
_Pm1001lhCntclientUpErrCntTable_Object=MibTable
pm1001lhCntclientUpErrCntTable=_Pm1001lhCntclientUpErrCntTable_Object((1,3,6,1,4,1,20044,10,4,2,32))
if mibBuilder.loadTexts:pm1001lhCntclientUpErrCntTable.setStatus(_A)
_Pm1001lhCntclientUpErrCntEntry_Object=MibTableRow
pm1001lhCntclientUpErrCntEntry=_Pm1001lhCntclientUpErrCntEntry_Object((1,3,6,1,4,1,20044,10,4,2,32,1))
pm1001lhCntclientUpErrCntEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm1001lhCntclientUpErrCntEntry.setStatus(_A)
class _Pm1001lhCntclientUpErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntclientUpErrCntIndex_Type.__name__=_E
_Pm1001lhCntclientUpErrCntIndex_Object=MibTableColumn
pm1001lhCntclientUpErrCntIndex=_Pm1001lhCntclientUpErrCntIndex_Object((1,3,6,1,4,1,20044,10,4,2,32,1,1),_Pm1001lhCntclientUpErrCntIndex_Type())
pm1001lhCntclientUpErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpErrCntIndex.setStatus(_A)
_Pm1001lhCntclientUpErrCntValuePortn_Type=Counter32
_Pm1001lhCntclientUpErrCntValuePortn_Object=MibTableColumn
pm1001lhCntclientUpErrCntValuePortn=_Pm1001lhCntclientUpErrCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,2,32,1,2),_Pm1001lhCntclientUpErrCntValuePortn_Type())
pm1001lhCntclientUpErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpErrCntValuePortn.setStatus(_A)
_Pm1001lhCntclientUpErrCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntclientUpErrCntErrorPortn_Object=MibTableColumn
pm1001lhCntclientUpErrCntErrorPortn=_Pm1001lhCntclientUpErrCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,2,32,1,3),_Pm1001lhCntclientUpErrCntErrorPortn_Type())
pm1001lhCntclientUpErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpErrCntErrorPortn.setStatus(_A)
_Pm1001lhCntclientUpErrCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntclientUpErrCntOverloadPortn_Object=MibTableColumn
pm1001lhCntclientUpErrCntOverloadPortn=_Pm1001lhCntclientUpErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,2,32,1,4),_Pm1001lhCntclientUpErrCntOverloadPortn_Type())
pm1001lhCntclientUpErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpErrCntOverloadPortn.setStatus(_A)
_Pm1001lhCntclientUpTimCntTable_Object=MibTable
pm1001lhCntclientUpTimCntTable=_Pm1001lhCntclientUpTimCntTable_Object((1,3,6,1,4,1,20044,10,4,2,40))
if mibBuilder.loadTexts:pm1001lhCntclientUpTimCntTable.setStatus(_A)
_Pm1001lhCntclientUpTimCntEntry_Object=MibTableRow
pm1001lhCntclientUpTimCntEntry=_Pm1001lhCntclientUpTimCntEntry_Object((1,3,6,1,4,1,20044,10,4,2,40,1))
pm1001lhCntclientUpTimCntEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm1001lhCntclientUpTimCntEntry.setStatus(_A)
class _Pm1001lhCntclientUpTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntclientUpTimCntIndex_Type.__name__=_E
_Pm1001lhCntclientUpTimCntIndex_Object=MibTableColumn
pm1001lhCntclientUpTimCntIndex=_Pm1001lhCntclientUpTimCntIndex_Object((1,3,6,1,4,1,20044,10,4,2,40,1,1),_Pm1001lhCntclientUpTimCntIndex_Type())
pm1001lhCntclientUpTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpTimCntIndex.setStatus(_A)
_Pm1001lhCntclientUpTimCntValuePortn_Type=Counter32
_Pm1001lhCntclientUpTimCntValuePortn_Object=MibTableColumn
pm1001lhCntclientUpTimCntValuePortn=_Pm1001lhCntclientUpTimCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,2,40,1,2),_Pm1001lhCntclientUpTimCntValuePortn_Type())
pm1001lhCntclientUpTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpTimCntValuePortn.setStatus(_A)
_Pm1001lhCntclientUpTimCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntclientUpTimCntErrorPortn_Object=MibTableColumn
pm1001lhCntclientUpTimCntErrorPortn=_Pm1001lhCntclientUpTimCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,2,40,1,3),_Pm1001lhCntclientUpTimCntErrorPortn_Type())
pm1001lhCntclientUpTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpTimCntErrorPortn.setStatus(_A)
_Pm1001lhCntclientUpTimCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntclientUpTimCntOverloadPortn_Object=MibTableColumn
pm1001lhCntclientUpTimCntOverloadPortn=_Pm1001lhCntclientUpTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,2,40,1,4),_Pm1001lhCntclientUpTimCntOverloadPortn_Type())
pm1001lhCntclientUpTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientUpTimCntOverloadPortn.setStatus(_A)
_Pm1001lhCntclientDwErrCntTable_Object=MibTable
pm1001lhCntclientDwErrCntTable=_Pm1001lhCntclientDwErrCntTable_Object((1,3,6,1,4,1,20044,10,4,2,64))
if mibBuilder.loadTexts:pm1001lhCntclientDwErrCntTable.setStatus(_A)
_Pm1001lhCntclientDwErrCntEntry_Object=MibTableRow
pm1001lhCntclientDwErrCntEntry=_Pm1001lhCntclientDwErrCntEntry_Object((1,3,6,1,4,1,20044,10,4,2,64,1))
pm1001lhCntclientDwErrCntEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm1001lhCntclientDwErrCntEntry.setStatus(_A)
class _Pm1001lhCntclientDwErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntclientDwErrCntIndex_Type.__name__=_E
_Pm1001lhCntclientDwErrCntIndex_Object=MibTableColumn
pm1001lhCntclientDwErrCntIndex=_Pm1001lhCntclientDwErrCntIndex_Object((1,3,6,1,4,1,20044,10,4,2,64,1,1),_Pm1001lhCntclientDwErrCntIndex_Type())
pm1001lhCntclientDwErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwErrCntIndex.setStatus(_A)
_Pm1001lhCntclientDwErrCntValuePortn_Type=Counter32
_Pm1001lhCntclientDwErrCntValuePortn_Object=MibTableColumn
pm1001lhCntclientDwErrCntValuePortn=_Pm1001lhCntclientDwErrCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,2,64,1,2),_Pm1001lhCntclientDwErrCntValuePortn_Type())
pm1001lhCntclientDwErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwErrCntValuePortn.setStatus(_A)
_Pm1001lhCntclientDwErrCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntclientDwErrCntErrorPortn_Object=MibTableColumn
pm1001lhCntclientDwErrCntErrorPortn=_Pm1001lhCntclientDwErrCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,2,64,1,3),_Pm1001lhCntclientDwErrCntErrorPortn_Type())
pm1001lhCntclientDwErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwErrCntErrorPortn.setStatus(_A)
_Pm1001lhCntclientDwErrCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntclientDwErrCntOverloadPortn_Object=MibTableColumn
pm1001lhCntclientDwErrCntOverloadPortn=_Pm1001lhCntclientDwErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,2,64,1,4),_Pm1001lhCntclientDwErrCntOverloadPortn_Type())
pm1001lhCntclientDwErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwErrCntOverloadPortn.setStatus(_A)
_Pm1001lhCntclientDwTimCntTable_Object=MibTable
pm1001lhCntclientDwTimCntTable=_Pm1001lhCntclientDwTimCntTable_Object((1,3,6,1,4,1,20044,10,4,2,72))
if mibBuilder.loadTexts:pm1001lhCntclientDwTimCntTable.setStatus(_A)
_Pm1001lhCntclientDwTimCntEntry_Object=MibTableRow
pm1001lhCntclientDwTimCntEntry=_Pm1001lhCntclientDwTimCntEntry_Object((1,3,6,1,4,1,20044,10,4,2,72,1))
pm1001lhCntclientDwTimCntEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm1001lhCntclientDwTimCntEntry.setStatus(_A)
class _Pm1001lhCntclientDwTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntclientDwTimCntIndex_Type.__name__=_E
_Pm1001lhCntclientDwTimCntIndex_Object=MibTableColumn
pm1001lhCntclientDwTimCntIndex=_Pm1001lhCntclientDwTimCntIndex_Object((1,3,6,1,4,1,20044,10,4,2,72,1,1),_Pm1001lhCntclientDwTimCntIndex_Type())
pm1001lhCntclientDwTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwTimCntIndex.setStatus(_A)
_Pm1001lhCntclientDwTimCntValuePortn_Type=Counter32
_Pm1001lhCntclientDwTimCntValuePortn_Object=MibTableColumn
pm1001lhCntclientDwTimCntValuePortn=_Pm1001lhCntclientDwTimCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,2,72,1,2),_Pm1001lhCntclientDwTimCntValuePortn_Type())
pm1001lhCntclientDwTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwTimCntValuePortn.setStatus(_A)
_Pm1001lhCntclientDwTimCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntclientDwTimCntErrorPortn_Object=MibTableColumn
pm1001lhCntclientDwTimCntErrorPortn=_Pm1001lhCntclientDwTimCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,2,72,1,3),_Pm1001lhCntclientDwTimCntErrorPortn_Type())
pm1001lhCntclientDwTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwTimCntErrorPortn.setStatus(_A)
_Pm1001lhCntclientDwTimCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntclientDwTimCntOverloadPortn_Object=MibTableColumn
pm1001lhCntclientDwTimCntOverloadPortn=_Pm1001lhCntclientDwTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,2,72,1,4),_Pm1001lhCntclientDwTimCntOverloadPortn_Type())
pm1001lhCntclientDwTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntclientDwTimCntOverloadPortn.setStatus(_A)
_Pm1001lhCntLine_ObjectIdentity=ObjectIdentity
pm1001lhCntLine=_Pm1001lhCntLine_ObjectIdentity((1,3,6,1,4,1,20044,10,4,3))
_Pm1001lhCntlineDfrmErrCntTable_Object=MibTable
pm1001lhCntlineDfrmErrCntTable=_Pm1001lhCntlineDfrmErrCntTable_Object((1,3,6,1,4,1,20044,10,4,3,152))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntTable.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntEntry_Object=MibTableRow
pm1001lhCntlineDfrmErrCntEntry=_Pm1001lhCntlineDfrmErrCntEntry_Object((1,3,6,1,4,1,20044,10,4,3,152,1))
pm1001lhCntlineDfrmErrCntEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntEntry.setStatus(_A)
class _Pm1001lhCntlineDfrmErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntlineDfrmErrCntIndex_Type.__name__=_E
_Pm1001lhCntlineDfrmErrCntIndex_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntIndex=_Pm1001lhCntlineDfrmErrCntIndex_Object((1,3,6,1,4,1,20044,10,4,3,152,1,1),_Pm1001lhCntlineDfrmErrCntIndex_Type())
pm1001lhCntlineDfrmErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntIndex.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntValuePortn_Type=Counter32
_Pm1001lhCntlineDfrmErrCntValuePortn_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntValuePortn=_Pm1001lhCntlineDfrmErrCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,3,152,1,2),_Pm1001lhCntlineDfrmErrCntValuePortn_Type())
pm1001lhCntlineDfrmErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntValuePortn.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmErrCntErrorPortn_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntErrorPortn=_Pm1001lhCntlineDfrmErrCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,3,152,1,3),_Pm1001lhCntlineDfrmErrCntErrorPortn_Type())
pm1001lhCntlineDfrmErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntErrorPortn.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmErrCntOverloadPortn_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntOverloadPortn=_Pm1001lhCntlineDfrmErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,3,152,1,4),_Pm1001lhCntlineDfrmErrCntOverloadPortn_Type())
pm1001lhCntlineDfrmErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntOverloadPortn.setStatus(_A)
_Pm1001lhCntlineDfrmTimCntTable_Object=MibTable
pm1001lhCntlineDfrmTimCntTable=_Pm1001lhCntlineDfrmTimCntTable_Object((1,3,6,1,4,1,20044,10,4,3,153))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmTimCntTable.setStatus(_A)
_Pm1001lhCntlineDfrmTimCntEntry_Object=MibTableRow
pm1001lhCntlineDfrmTimCntEntry=_Pm1001lhCntlineDfrmTimCntEntry_Object((1,3,6,1,4,1,20044,10,4,3,153,1))
pm1001lhCntlineDfrmTimCntEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmTimCntEntry.setStatus(_A)
class _Pm1001lhCntlineDfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntlineDfrmTimCntIndex_Type.__name__=_E
_Pm1001lhCntlineDfrmTimCntIndex_Object=MibTableColumn
pm1001lhCntlineDfrmTimCntIndex=_Pm1001lhCntlineDfrmTimCntIndex_Object((1,3,6,1,4,1,20044,10,4,3,153,1,1),_Pm1001lhCntlineDfrmTimCntIndex_Type())
pm1001lhCntlineDfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmTimCntIndex.setStatus(_A)
_Pm1001lhCntlineDfrmTimCntValuePortn_Type=Counter32
_Pm1001lhCntlineDfrmTimCntValuePortn_Object=MibTableColumn
pm1001lhCntlineDfrmTimCntValuePortn=_Pm1001lhCntlineDfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,3,153,1,2),_Pm1001lhCntlineDfrmTimCntValuePortn_Type())
pm1001lhCntlineDfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmTimCntValuePortn.setStatus(_A)
_Pm1001lhCntlineDfrmTimCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmTimCntErrorPortn_Object=MibTableColumn
pm1001lhCntlineDfrmTimCntErrorPortn=_Pm1001lhCntlineDfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,3,153,1,3),_Pm1001lhCntlineDfrmTimCntErrorPortn_Type())
pm1001lhCntlineDfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmTimCntErrorPortn.setStatus(_A)
_Pm1001lhCntlineDfrmTimCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmTimCntOverloadPortn_Object=MibTableColumn
pm1001lhCntlineDfrmTimCntOverloadPortn=_Pm1001lhCntlineDfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,3,153,1,4),_Pm1001lhCntlineDfrmTimCntOverloadPortn_Type())
pm1001lhCntlineDfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmTimCntOverloadPortn.setStatus(_A)
_Pm1001lhCntlineDfrmPrimErrCntTable_Object=MibTable
pm1001lhCntlineDfrmPrimErrCntTable=_Pm1001lhCntlineDfrmPrimErrCntTable_Object((1,3,6,1,4,1,20044,10,4,3,154))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmPrimErrCntTable.setStatus(_A)
_Pm1001lhCntlineDfrmPrimErrCntEntry_Object=MibTableRow
pm1001lhCntlineDfrmPrimErrCntEntry=_Pm1001lhCntlineDfrmPrimErrCntEntry_Object((1,3,6,1,4,1,20044,10,4,3,154,1))
pm1001lhCntlineDfrmPrimErrCntEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmPrimErrCntEntry.setStatus(_A)
class _Pm1001lhCntlineDfrmPrimErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntlineDfrmPrimErrCntIndex_Type.__name__=_E
_Pm1001lhCntlineDfrmPrimErrCntIndex_Object=MibTableColumn
pm1001lhCntlineDfrmPrimErrCntIndex=_Pm1001lhCntlineDfrmPrimErrCntIndex_Object((1,3,6,1,4,1,20044,10,4,3,154,1,1),_Pm1001lhCntlineDfrmPrimErrCntIndex_Type())
pm1001lhCntlineDfrmPrimErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmPrimErrCntIndex.setStatus(_A)
_Pm1001lhCntlineDfrmPrimErrCntValuePortn_Type=Counter32
_Pm1001lhCntlineDfrmPrimErrCntValuePortn_Object=MibTableColumn
pm1001lhCntlineDfrmPrimErrCntValuePortn=_Pm1001lhCntlineDfrmPrimErrCntValuePortn_Object((1,3,6,1,4,1,20044,10,4,3,154,1,2),_Pm1001lhCntlineDfrmPrimErrCntValuePortn_Type())
pm1001lhCntlineDfrmPrimErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmPrimErrCntValuePortn.setStatus(_A)
_Pm1001lhCntlineDfrmPrimErrCntErrorPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmPrimErrCntErrorPortn_Object=MibTableColumn
pm1001lhCntlineDfrmPrimErrCntErrorPortn=_Pm1001lhCntlineDfrmPrimErrCntErrorPortn_Object((1,3,6,1,4,1,20044,10,4,3,154,1,3),_Pm1001lhCntlineDfrmPrimErrCntErrorPortn_Type())
pm1001lhCntlineDfrmPrimErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmPrimErrCntErrorPortn.setStatus(_A)
_Pm1001lhCntlineDfrmPrimErrCntOverloadPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmPrimErrCntOverloadPortn_Object=MibTableColumn
pm1001lhCntlineDfrmPrimErrCntOverloadPortn=_Pm1001lhCntlineDfrmPrimErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,3,154,1,4),_Pm1001lhCntlineDfrmPrimErrCntOverloadPortn_Type())
pm1001lhCntlineDfrmPrimErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmPrimErrCntOverloadPortn.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntSTable_Object=MibTable
pm1001lhCntlineDfrmErrCntSTable=_Pm1001lhCntlineDfrmErrCntSTable_Object((1,3,6,1,4,1,20044,10,4,3,1160))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntSTable.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntSEntry_Object=MibTableRow
pm1001lhCntlineDfrmErrCntSEntry=_Pm1001lhCntlineDfrmErrCntSEntry_Object((1,3,6,1,4,1,20044,10,4,3,1160,1))
pm1001lhCntlineDfrmErrCntSEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntSEntry.setStatus(_A)
class _Pm1001lhCntlineDfrmErrCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCntlineDfrmErrCntSIndex_Type.__name__=_E
_Pm1001lhCntlineDfrmErrCntSIndex_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntSIndex=_Pm1001lhCntlineDfrmErrCntSIndex_Object((1,3,6,1,4,1,20044,10,4,3,1160,1,1),_Pm1001lhCntlineDfrmErrCntSIndex_Type())
pm1001lhCntlineDfrmErrCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntSIndex.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntSValuePortn_Type=Counter32
_Pm1001lhCntlineDfrmErrCntSValuePortn_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntSValuePortn=_Pm1001lhCntlineDfrmErrCntSValuePortn_Object((1,3,6,1,4,1,20044,10,4,3,1160,1,2),_Pm1001lhCntlineDfrmErrCntSValuePortn_Type())
pm1001lhCntlineDfrmErrCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntSValuePortn.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntSErrorPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmErrCntSErrorPortn_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntSErrorPortn=_Pm1001lhCntlineDfrmErrCntSErrorPortn_Object((1,3,6,1,4,1,20044,10,4,3,1160,1,3),_Pm1001lhCntlineDfrmErrCntSErrorPortn_Type())
pm1001lhCntlineDfrmErrCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntSErrorPortn.setStatus(_A)
_Pm1001lhCntlineDfrmErrCntSOverloadPortn_Type=EkiOnOff
_Pm1001lhCntlineDfrmErrCntSOverloadPortn_Object=MibTableColumn
pm1001lhCntlineDfrmErrCntSOverloadPortn=_Pm1001lhCntlineDfrmErrCntSOverloadPortn_Object((1,3,6,1,4,1,20044,10,4,3,1160,1,4),_Pm1001lhCntlineDfrmErrCntSOverloadPortn_Type())
pm1001lhCntlineDfrmErrCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCntlineDfrmErrCntSOverloadPortn.setStatus(_A)
_Pm1001lhCntCountersReset_Type=EkiOnOff
_Pm1001lhCntCountersReset_Object=MibScalar
pm1001lhCntCountersReset=_Pm1001lhCntCountersReset_Object((1,3,6,1,4,1,20044,10,4,259),_Pm1001lhCntCountersReset_Type())
pm1001lhCntCountersReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCntCountersReset.setStatus(_A)
_Pm1001lhCntCountersStop_Type=EkiOnOff
_Pm1001lhCntCountersStop_Object=MibScalar
pm1001lhCntCountersStop=_Pm1001lhCntCountersStop_Object((1,3,6,1,4,1,20044,10,4,260),_Pm1001lhCntCountersStop_Type())
pm1001lhCntCountersStop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCntCountersStop.setStatus(_A)
_Pm1001lhcontrolsWrite_ObjectIdentity=ObjectIdentity
pm1001lhcontrolsWrite=_Pm1001lhcontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,10,6))
_Pm1001lhCtrlOther_ObjectIdentity=ObjectIdentity
pm1001lhCtrlOther=_Pm1001lhCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1))
_Pm1001lhCtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pm1001lhCtrlconfMgnt1=_Pm1001lhCtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,1))
_Pm1001lhCtrlConf1Load1_Type=EkiOnOff
_Pm1001lhCtrlConf1Load1_Object=MibScalar
pm1001lhCtrlConf1Load1=_Pm1001lhCtrlConf1Load1_Object((1,3,6,1,4,1,20044,10,6,1,1,1),_Pm1001lhCtrlConf1Load1_Type())
pm1001lhCtrlConf1Load1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlConf1Load1.setStatus(_A)
_Pm1001lhCtrlConf2Load1_Type=EkiOnOff
_Pm1001lhCtrlConf2Load1_Object=MibScalar
pm1001lhCtrlConf2Load1=_Pm1001lhCtrlConf2Load1_Object((1,3,6,1,4,1,20044,10,6,1,1,2),_Pm1001lhCtrlConf2Load1_Type())
pm1001lhCtrlConf2Load1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlConf2Load1.setStatus(_A)
_Pm1001lhCtrlConf2Flash1_Type=EkiOnOff
_Pm1001lhCtrlConf2Flash1_Object=MibScalar
pm1001lhCtrlConf2Flash1=_Pm1001lhCtrlConf2Flash1_Object((1,3,6,1,4,1,20044,10,6,1,1,10),_Pm1001lhCtrlConf2Flash1_Type())
pm1001lhCtrlConf2Flash1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlConf2Flash1.setStatus(_A)
_Pm1001lhCtrlConf2Clear1_Type=EkiOnOff
_Pm1001lhCtrlConf2Clear1_Object=MibScalar
pm1001lhCtrlConf2Clear1=_Pm1001lhCtrlConf2Clear1_Object((1,3,6,1,4,1,20044,10,6,1,1,14),_Pm1001lhCtrlConf2Clear1_Type())
pm1001lhCtrlConf2Clear1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlConf2Clear1.setStatus(_A)
_Pm1001lhCtrlsynth4_ObjectIdentity=ObjectIdentity
pm1001lhCtrlsynth4=_Pm1001lhCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,4))
_Pm1001lhCtrlCorrelatOn_Type=EkiOnOff
_Pm1001lhCtrlCorrelatOn_Object=MibScalar
pm1001lhCtrlCorrelatOn=_Pm1001lhCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,10,6,1,4,1),_Pm1001lhCtrlCorrelatOn_Type())
pm1001lhCtrlCorrelatOn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlCorrelatOn.setStatus(_A)
_Pm1001lhCtrlCorrelatOff_Type=EkiOnOff
_Pm1001lhCtrlCorrelatOff_Object=MibScalar
pm1001lhCtrlCorrelatOff=_Pm1001lhCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,10,6,1,4,2),_Pm1001lhCtrlCorrelatOff_Type())
pm1001lhCtrlCorrelatOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlCorrelatOff.setStatus(_A)
_Pm1001lhCtrlswMgnt_ObjectIdentity=ObjectIdentity
pm1001lhCtrlswMgnt=_Pm1001lhCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,5))
_Pm1001lhCtrlColdReset_Type=EkiOnOff
_Pm1001lhCtrlColdReset_Object=MibScalar
pm1001lhCtrlColdReset=_Pm1001lhCtrlColdReset_Object((1,3,6,1,4,1,20044,10,6,1,5,2),_Pm1001lhCtrlColdReset_Type())
pm1001lhCtrlColdReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlColdReset.setStatus(_A)
_Pm1001lhCtrlWarmReset_Type=EkiOnOff
_Pm1001lhCtrlWarmReset_Object=MibScalar
pm1001lhCtrlWarmReset=_Pm1001lhCtrlWarmReset_Object((1,3,6,1,4,1,20044,10,6,1,5,3),_Pm1001lhCtrlWarmReset_Type())
pm1001lhCtrlWarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlWarmReset.setStatus(_A)
_Pm1001lhCtrlLoadSwBank1_Type=EkiOnOff
_Pm1001lhCtrlLoadSwBank1_Object=MibScalar
pm1001lhCtrlLoadSwBank1=_Pm1001lhCtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,10,6,1,5,5),_Pm1001lhCtrlLoadSwBank1_Type())
pm1001lhCtrlLoadSwBank1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLoadSwBank1.setStatus(_A)
_Pm1001lhCtrlLoadSwBank2_Type=EkiOnOff
_Pm1001lhCtrlLoadSwBank2_Object=MibScalar
pm1001lhCtrlLoadSwBank2=_Pm1001lhCtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,10,6,1,5,6),_Pm1001lhCtrlLoadSwBank2_Type())
pm1001lhCtrlLoadSwBank2.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLoadSwBank2.setStatus(_A)
_Pm1001lhCtrlgwMgnt_ObjectIdentity=ObjectIdentity
pm1001lhCtrlgwMgnt=_Pm1001lhCtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,6))
_Pm1001lhCtrlCurrentGwReset_Type=EkiOnOff
_Pm1001lhCtrlCurrentGwReset_Object=MibScalar
pm1001lhCtrlCurrentGwReset=_Pm1001lhCtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,10,6,1,6,1),_Pm1001lhCtrlCurrentGwReset_Type())
pm1001lhCtrlCurrentGwReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlCurrentGwReset.setStatus(_A)
_Pm1001lhCtrlLoadGwBank1_Type=EkiOnOff
_Pm1001lhCtrlLoadGwBank1_Object=MibScalar
pm1001lhCtrlLoadGwBank1=_Pm1001lhCtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,10,6,1,6,5),_Pm1001lhCtrlLoadGwBank1_Type())
pm1001lhCtrlLoadGwBank1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLoadGwBank1.setStatus(_A)
_Pm1001lhCtrlLoadGwBank2_Type=EkiOnOff
_Pm1001lhCtrlLoadGwBank2_Object=MibScalar
pm1001lhCtrlLoadGwBank2=_Pm1001lhCtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,10,6,1,6,6),_Pm1001lhCtrlLoadGwBank2_Type())
pm1001lhCtrlLoadGwBank2.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLoadGwBank2.setStatus(_A)
_Pm1001lhCtrlLoadGwBank3_Type=EkiOnOff
_Pm1001lhCtrlLoadGwBank3_Object=MibScalar
pm1001lhCtrlLoadGwBank3=_Pm1001lhCtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,10,6,1,6,7),_Pm1001lhCtrlLoadGwBank3_Type())
pm1001lhCtrlLoadGwBank3.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLoadGwBank3.setStatus(_A)
_Pm1001lhCtrlLoadGwBank4_Type=EkiOnOff
_Pm1001lhCtrlLoadGwBank4_Object=MibScalar
pm1001lhCtrlLoadGwBank4=_Pm1001lhCtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,10,6,1,6,8),_Pm1001lhCtrlLoadGwBank4_Type())
pm1001lhCtrlLoadGwBank4.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLoadGwBank4.setStatus(_A)
_Pm1001lhCtrlledTest_ObjectIdentity=ObjectIdentity
pm1001lhCtrlledTest=_Pm1001lhCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,192))
_Pm1001lhCtrlGreenLed_Type=EkiOnOff
_Pm1001lhCtrlGreenLed_Object=MibScalar
pm1001lhCtrlGreenLed=_Pm1001lhCtrlGreenLed_Object((1,3,6,1,4,1,20044,10,6,1,192,1),_Pm1001lhCtrlGreenLed_Type())
pm1001lhCtrlGreenLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlGreenLed.setStatus(_A)
_Pm1001lhCtrlRedLed_Type=EkiOnOff
_Pm1001lhCtrlRedLed_Object=MibScalar
pm1001lhCtrlRedLed=_Pm1001lhCtrlRedLed_Object((1,3,6,1,4,1,20044,10,6,1,192,2),_Pm1001lhCtrlRedLed_Type())
pm1001lhCtrlRedLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlRedLed.setStatus(_A)
_Pm1001lhCtrlLedOff_Type=EkiOnOff
_Pm1001lhCtrlLedOff_Object=MibScalar
pm1001lhCtrlLedOff=_Pm1001lhCtrlLedOff_Object((1,3,6,1,4,1,20044,10,6,1,192,3),_Pm1001lhCtrlLedOff_Type())
pm1001lhCtrlLedOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLedOff.setStatus(_A)
_Pm1001lhCtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm1001lhCtrlmoduleOosMode=_Pm1001lhCtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,193))
_Pm1001lhCtrlModuleOosMode_Type=EkiOnOff
_Pm1001lhCtrlModuleOosMode_Object=MibScalar
pm1001lhCtrlModuleOosMode=_Pm1001lhCtrlModuleOosMode_Object((1,3,6,1,4,1,20044,10,6,1,193,1),_Pm1001lhCtrlModuleOosMode_Type())
pm1001lhCtrlModuleOosMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlModuleOosMode.setStatus(_A)
_Pm1001lhCtrlmaintenanceMode_ObjectIdentity=ObjectIdentity
pm1001lhCtrlmaintenanceMode=_Pm1001lhCtrlmaintenanceMode_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,197))
_Pm1001lhCtrlMaintenanceMode_Type=EkiOnOff
_Pm1001lhCtrlMaintenanceMode_Object=MibScalar
pm1001lhCtrlMaintenanceMode=_Pm1001lhCtrlMaintenanceMode_Object((1,3,6,1,4,1,20044,10,6,1,197,1),_Pm1001lhCtrlMaintenanceMode_Type())
pm1001lhCtrlMaintenanceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlMaintenanceMode.setStatus(_A)
_Pm1001lhCtrldccEnable_ObjectIdentity=ObjectIdentity
pm1001lhCtrldccEnable=_Pm1001lhCtrldccEnable_ObjectIdentity((1,3,6,1,4,1,20044,10,6,1,198))
_Pm1001lhCtrlDccEnable_Type=EkiOnOff
_Pm1001lhCtrlDccEnable_Object=MibScalar
pm1001lhCtrlDccEnable=_Pm1001lhCtrlDccEnable_Object((1,3,6,1,4,1,20044,10,6,1,198,1),_Pm1001lhCtrlDccEnable_Type())
pm1001lhCtrlDccEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlDccEnable.setStatus(_A)
_Pm1001lhCtrlClient_ObjectIdentity=ObjectIdentity
pm1001lhCtrlClient=_Pm1001lhCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,10,6,2))
_Pm1001lhCtrlaccessLoopTable_Object=MibTable
pm1001lhCtrlaccessLoopTable=_Pm1001lhCtrlaccessLoopTable_Object((1,3,6,1,4,1,20044,10,6,2,16))
if mibBuilder.loadTexts:pm1001lhCtrlaccessLoopTable.setStatus(_A)
_Pm1001lhCtrlaccessLoopEntry_Object=MibTableRow
pm1001lhCtrlaccessLoopEntry=_Pm1001lhCtrlaccessLoopEntry_Object((1,3,6,1,4,1,20044,10,6,2,16,1))
pm1001lhCtrlaccessLoopEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm1001lhCtrlaccessLoopEntry.setStatus(_A)
class _Pm1001lhCtrlaccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlaccessLoopIndex_Type.__name__=_E
_Pm1001lhCtrlaccessLoopIndex_Object=MibTableColumn
pm1001lhCtrlaccessLoopIndex=_Pm1001lhCtrlaccessLoopIndex_Object((1,3,6,1,4,1,20044,10,6,2,16,1,1),_Pm1001lhCtrlaccessLoopIndex_Type())
pm1001lhCtrlaccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlaccessLoopIndex.setStatus(_A)
_Pm1001lhCtrlaccessLoopPortn_Type=EkiState
_Pm1001lhCtrlaccessLoopPortn_Object=MibTableColumn
pm1001lhCtrlaccessLoopPortn=_Pm1001lhCtrlaccessLoopPortn_Object((1,3,6,1,4,1,20044,10,6,2,16,1,2),_Pm1001lhCtrlaccessLoopPortn_Type())
pm1001lhCtrlaccessLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlaccessLoopPortn.setStatus(_A)
_Pm1001lhCtrlportOosModeTable_Object=MibTable
pm1001lhCtrlportOosModeTable=_Pm1001lhCtrlportOosModeTable_Object((1,3,6,1,4,1,20044,10,6,2,18))
if mibBuilder.loadTexts:pm1001lhCtrlportOosModeTable.setStatus(_A)
_Pm1001lhCtrlportOosModeEntry_Object=MibTableRow
pm1001lhCtrlportOosModeEntry=_Pm1001lhCtrlportOosModeEntry_Object((1,3,6,1,4,1,20044,10,6,2,18,1))
pm1001lhCtrlportOosModeEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm1001lhCtrlportOosModeEntry.setStatus(_A)
class _Pm1001lhCtrlportOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlportOosModeIndex_Type.__name__=_E
_Pm1001lhCtrlportOosModeIndex_Object=MibTableColumn
pm1001lhCtrlportOosModeIndex=_Pm1001lhCtrlportOosModeIndex_Object((1,3,6,1,4,1,20044,10,6,2,18,1,1),_Pm1001lhCtrlportOosModeIndex_Type())
pm1001lhCtrlportOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlportOosModeIndex.setStatus(_A)
_Pm1001lhCtrlportOosModePortn_Type=EkiState
_Pm1001lhCtrlportOosModePortn_Object=MibTableColumn
pm1001lhCtrlportOosModePortn=_Pm1001lhCtrlportOosModePortn_Object((1,3,6,1,4,1,20044,10,6,2,18,1,2),_Pm1001lhCtrlportOosModePortn_Type())
pm1001lhCtrlportOosModePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlportOosModePortn.setStatus(_A)
_Pm1001lhCtrlxfpOffCtrlTable_Object=MibTable
pm1001lhCtrlxfpOffCtrlTable=_Pm1001lhCtrlxfpOffCtrlTable_Object((1,3,6,1,4,1,20044,10,6,2,20))
if mibBuilder.loadTexts:pm1001lhCtrlxfpOffCtrlTable.setStatus(_A)
_Pm1001lhCtrlxfpOffCtrlEntry_Object=MibTableRow
pm1001lhCtrlxfpOffCtrlEntry=_Pm1001lhCtrlxfpOffCtrlEntry_Object((1,3,6,1,4,1,20044,10,6,2,20,1))
pm1001lhCtrlxfpOffCtrlEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm1001lhCtrlxfpOffCtrlEntry.setStatus(_A)
class _Pm1001lhCtrlxfpOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlxfpOffCtrlIndex_Type.__name__=_E
_Pm1001lhCtrlxfpOffCtrlIndex_Object=MibTableColumn
pm1001lhCtrlxfpOffCtrlIndex=_Pm1001lhCtrlxfpOffCtrlIndex_Object((1,3,6,1,4,1,20044,10,6,2,20,1,1),_Pm1001lhCtrlxfpOffCtrlIndex_Type())
pm1001lhCtrlxfpOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlxfpOffCtrlIndex.setStatus(_A)
_Pm1001lhCtrlxfpOffCtrlPortn_Type=EkiState
_Pm1001lhCtrlxfpOffCtrlPortn_Object=MibTableColumn
pm1001lhCtrlxfpOffCtrlPortn=_Pm1001lhCtrlxfpOffCtrlPortn_Object((1,3,6,1,4,1,20044,10,6,2,20,1,2),_Pm1001lhCtrlxfpOffCtrlPortn_Type())
pm1001lhCtrlxfpOffCtrlPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlxfpOffCtrlPortn.setStatus(_A)
_Pm1001lhCtrlcsfUpInsTable_Object=MibTable
pm1001lhCtrlcsfUpInsTable=_Pm1001lhCtrlcsfUpInsTable_Object((1,3,6,1,4,1,20044,10,6,2,21))
if mibBuilder.loadTexts:pm1001lhCtrlcsfUpInsTable.setStatus(_A)
_Pm1001lhCtrlcsfUpInsEntry_Object=MibTableRow
pm1001lhCtrlcsfUpInsEntry=_Pm1001lhCtrlcsfUpInsEntry_Object((1,3,6,1,4,1,20044,10,6,2,21,1))
pm1001lhCtrlcsfUpInsEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm1001lhCtrlcsfUpInsEntry.setStatus(_A)
class _Pm1001lhCtrlcsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlcsfUpInsIndex_Type.__name__=_E
_Pm1001lhCtrlcsfUpInsIndex_Object=MibTableColumn
pm1001lhCtrlcsfUpInsIndex=_Pm1001lhCtrlcsfUpInsIndex_Object((1,3,6,1,4,1,20044,10,6,2,21,1,1),_Pm1001lhCtrlcsfUpInsIndex_Type())
pm1001lhCtrlcsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlcsfUpInsIndex.setStatus(_A)
_Pm1001lhCtrlcsfUpInsPortn_Type=EkiState
_Pm1001lhCtrlcsfUpInsPortn_Object=MibTableColumn
pm1001lhCtrlcsfUpInsPortn=_Pm1001lhCtrlcsfUpInsPortn_Object((1,3,6,1,4,1,20044,10,6,2,21,1,2),_Pm1001lhCtrlcsfUpInsPortn_Type())
pm1001lhCtrlcsfUpInsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlcsfUpInsPortn.setStatus(_A)
_Pm1001lhCtrlcaisDwInsTable_Object=MibTable
pm1001lhCtrlcaisDwInsTable=_Pm1001lhCtrlcaisDwInsTable_Object((1,3,6,1,4,1,20044,10,6,2,22))
if mibBuilder.loadTexts:pm1001lhCtrlcaisDwInsTable.setStatus(_A)
_Pm1001lhCtrlcaisDwInsEntry_Object=MibTableRow
pm1001lhCtrlcaisDwInsEntry=_Pm1001lhCtrlcaisDwInsEntry_Object((1,3,6,1,4,1,20044,10,6,2,22,1))
pm1001lhCtrlcaisDwInsEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm1001lhCtrlcaisDwInsEntry.setStatus(_A)
class _Pm1001lhCtrlcaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlcaisDwInsIndex_Type.__name__=_E
_Pm1001lhCtrlcaisDwInsIndex_Object=MibTableColumn
pm1001lhCtrlcaisDwInsIndex=_Pm1001lhCtrlcaisDwInsIndex_Object((1,3,6,1,4,1,20044,10,6,2,22,1,1),_Pm1001lhCtrlcaisDwInsIndex_Type())
pm1001lhCtrlcaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlcaisDwInsIndex.setStatus(_A)
_Pm1001lhCtrlcaisDwInsPortn_Type=EkiState
_Pm1001lhCtrlcaisDwInsPortn_Object=MibTableColumn
pm1001lhCtrlcaisDwInsPortn=_Pm1001lhCtrlcaisDwInsPortn_Object((1,3,6,1,4,1,20044,10,6,2,22,1,2),_Pm1001lhCtrlcaisDwInsPortn_Type())
pm1001lhCtrlcaisDwInsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlcaisDwInsPortn.setStatus(_A)
_Pm1001lhCtrlclientAccessTermLoopTable_Object=MibTable
pm1001lhCtrlclientAccessTermLoopTable=_Pm1001lhCtrlclientAccessTermLoopTable_Object((1,3,6,1,4,1,20044,10,6,2,26))
if mibBuilder.loadTexts:pm1001lhCtrlclientAccessTermLoopTable.setStatus(_A)
_Pm1001lhCtrlclientAccessTermLoopEntry_Object=MibTableRow
pm1001lhCtrlclientAccessTermLoopEntry=_Pm1001lhCtrlclientAccessTermLoopEntry_Object((1,3,6,1,4,1,20044,10,6,2,26,1))
pm1001lhCtrlclientAccessTermLoopEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm1001lhCtrlclientAccessTermLoopEntry.setStatus(_A)
class _Pm1001lhCtrlclientAccessTermLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlclientAccessTermLoopIndex_Type.__name__=_E
_Pm1001lhCtrlclientAccessTermLoopIndex_Object=MibTableColumn
pm1001lhCtrlclientAccessTermLoopIndex=_Pm1001lhCtrlclientAccessTermLoopIndex_Object((1,3,6,1,4,1,20044,10,6,2,26,1,1),_Pm1001lhCtrlclientAccessTermLoopIndex_Type())
pm1001lhCtrlclientAccessTermLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlclientAccessTermLoopIndex.setStatus(_A)
_Pm1001lhCtrlclientAccessTermLoopPortn_Type=EkiState
_Pm1001lhCtrlclientAccessTermLoopPortn_Object=MibTableColumn
pm1001lhCtrlclientAccessTermLoopPortn=_Pm1001lhCtrlclientAccessTermLoopPortn_Object((1,3,6,1,4,1,20044,10,6,2,26,1,2),_Pm1001lhCtrlclientAccessTermLoopPortn_Type())
pm1001lhCtrlclientAccessTermLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlclientAccessTermLoopPortn.setStatus(_A)
_Pm1001lhCtrlprotocol_Type=EkiProtocol
_Pm1001lhCtrlprotocol_Object=MibScalar
pm1001lhCtrlprotocol=_Pm1001lhCtrlprotocol_Object((1,3,6,1,4,1,20044,10,6,2,52),_Pm1001lhCtrlprotocol_Type())
pm1001lhCtrlprotocol.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlprotocol.setStatus(_A)
_Pm1001lhCtrlclientResetAllCountTable_Object=MibTable
pm1001lhCtrlclientResetAllCountTable=_Pm1001lhCtrlclientResetAllCountTable_Object((1,3,6,1,4,1,20044,10,6,2,271))
if mibBuilder.loadTexts:pm1001lhCtrlclientResetAllCountTable.setStatus(_A)
_Pm1001lhCtrlclientResetAllCountEntry_Object=MibTableRow
pm1001lhCtrlclientResetAllCountEntry=_Pm1001lhCtrlclientResetAllCountEntry_Object((1,3,6,1,4,1,20044,10,6,2,271,1))
pm1001lhCtrlclientResetAllCountEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm1001lhCtrlclientResetAllCountEntry.setStatus(_A)
class _Pm1001lhCtrlclientResetAllCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlclientResetAllCountIndex_Type.__name__=_E
_Pm1001lhCtrlclientResetAllCountIndex_Object=MibTableColumn
pm1001lhCtrlclientResetAllCountIndex=_Pm1001lhCtrlclientResetAllCountIndex_Object((1,3,6,1,4,1,20044,10,6,2,271,1,1),_Pm1001lhCtrlclientResetAllCountIndex_Type())
pm1001lhCtrlclientResetAllCountIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlclientResetAllCountIndex.setStatus(_A)
_Pm1001lhCtrlclientResetAllCountsPortn_Type=EkiState
_Pm1001lhCtrlclientResetAllCountsPortn_Object=MibTableColumn
pm1001lhCtrlclientResetAllCountsPortn=_Pm1001lhCtrlclientResetAllCountsPortn_Object((1,3,6,1,4,1,20044,10,6,2,271,1,2),_Pm1001lhCtrlclientResetAllCountsPortn_Type())
pm1001lhCtrlclientResetAllCountsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlclientResetAllCountsPortn.setStatus(_A)
_Pm1001lhCtrlLine_ObjectIdentity=ObjectIdentity
pm1001lhCtrlLine=_Pm1001lhCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3))
_Pm1001lhCtrlcommAccessLoop_ObjectIdentity=ObjectIdentity
pm1001lhCtrlcommAccessLoop=_Pm1001lhCtrlcommAccessLoop_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3,64))
_Pm1001lhCtrlCommAccessloop_Type=EkiOnOff
_Pm1001lhCtrlCommAccessloop_Object=MibScalar
pm1001lhCtrlCommAccessloop=_Pm1001lhCtrlCommAccessloop_Object((1,3,6,1,4,1,20044,10,6,3,64,1),_Pm1001lhCtrlCommAccessloop_Type())
pm1001lhCtrlCommAccessloop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlCommAccessloop.setStatus(_G)
_Pm1001lhCtrllineLoop_ObjectIdentity=ObjectIdentity
pm1001lhCtrllineLoop=_Pm1001lhCtrllineLoop_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3,66))
_Pm1001lhCtrlLineLoop_Type=EkiOnOff
_Pm1001lhCtrlLineLoop_Object=MibScalar
pm1001lhCtrlLineLoop=_Pm1001lhCtrlLineLoop_Object((1,3,6,1,4,1,20044,10,6,3,66,1),_Pm1001lhCtrlLineLoop_Type())
pm1001lhCtrlLineLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLineLoop.setStatus(_G)
_Pm1001lhCtrlmsAis_ObjectIdentity=ObjectIdentity
pm1001lhCtrlmsAis=_Pm1001lhCtrlmsAis_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3,67))
_Pm1001lhCtrlMsAis_Type=EkiOnOff
_Pm1001lhCtrlMsAis_Object=MibScalar
pm1001lhCtrlMsAis=_Pm1001lhCtrlMsAis_Object((1,3,6,1,4,1,20044,10,6,3,67,1),_Pm1001lhCtrlMsAis_Type())
pm1001lhCtrlMsAis.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlMsAis.setStatus(_A)
_Pm1001lhCtrlfecDisable_ObjectIdentity=ObjectIdentity
pm1001lhCtrlfecDisable=_Pm1001lhCtrlfecDisable_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3,69))
_Pm1001lhCtrlFecInhibition_Type=EkiOnOff
_Pm1001lhCtrlFecInhibition_Object=MibScalar
pm1001lhCtrlFecInhibition=_Pm1001lhCtrlFecInhibition_Object((1,3,6,1,4,1,20044,10,6,3,69,1),_Pm1001lhCtrlFecInhibition_Type())
pm1001lhCtrlFecInhibition.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlFecInhibition.setStatus(_A)
_Pm1001lhCtrllineOosMode_ObjectIdentity=ObjectIdentity
pm1001lhCtrllineOosMode=_Pm1001lhCtrllineOosMode_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3,74))
_Pm1001lhCtrlLineOosMode_Type=EkiOnOff
_Pm1001lhCtrlLineOosMode_Object=MibScalar
pm1001lhCtrlLineOosMode=_Pm1001lhCtrlLineOosMode_Object((1,3,6,1,4,1,20044,10,6,3,74,1),_Pm1001lhCtrlLineOosMode_Type())
pm1001lhCtrlLineOosMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlLineOosMode.setStatus(_A)
_Pm1001lhCtrlxfpOnoffTable_Object=MibTable
pm1001lhCtrlxfpOnoffTable=_Pm1001lhCtrlxfpOnoffTable_Object((1,3,6,1,4,1,20044,10,6,3,208))
if mibBuilder.loadTexts:pm1001lhCtrlxfpOnoffTable.setStatus(_A)
_Pm1001lhCtrlxfpOnoffEntry_Object=MibTableRow
pm1001lhCtrlxfpOnoffEntry=_Pm1001lhCtrlxfpOnoffEntry_Object((1,3,6,1,4,1,20044,10,6,3,208,1))
pm1001lhCtrlxfpOnoffEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm1001lhCtrlxfpOnoffEntry.setStatus(_A)
class _Pm1001lhCtrlxfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlxfpOnoffIndex_Type.__name__=_E
_Pm1001lhCtrlxfpOnoffIndex_Object=MibTableColumn
pm1001lhCtrlxfpOnoffIndex=_Pm1001lhCtrlxfpOnoffIndex_Object((1,3,6,1,4,1,20044,10,6,3,208,1,1),_Pm1001lhCtrlxfpOnoffIndex_Type())
pm1001lhCtrlxfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlxfpOnoffIndex.setStatus(_A)
_Pm1001lhCtrlxfpOnoffPortn_Type=EkiState
_Pm1001lhCtrlxfpOnoffPortn_Object=MibTableColumn
pm1001lhCtrlxfpOnoffPortn=_Pm1001lhCtrlxfpOnoffPortn_Object((1,3,6,1,4,1,20044,10,6,3,208,1,2),_Pm1001lhCtrlxfpOnoffPortn_Type())
pm1001lhCtrlxfpOnoffPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlxfpOnoffPortn.setStatus(_A)
_Pm1001lhCtrlxfpLineLoopTable_Object=MibTable
pm1001lhCtrlxfpLineLoopTable=_Pm1001lhCtrlxfpLineLoopTable_Object((1,3,6,1,4,1,20044,10,6,3,209))
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineLoopTable.setStatus(_A)
_Pm1001lhCtrlxfpLineLoopEntry_Object=MibTableRow
pm1001lhCtrlxfpLineLoopEntry=_Pm1001lhCtrlxfpLineLoopEntry_Object((1,3,6,1,4,1,20044,10,6,3,209,1))
pm1001lhCtrlxfpLineLoopEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineLoopEntry.setStatus(_A)
class _Pm1001lhCtrlxfpLineLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlxfpLineLoopIndex_Type.__name__=_E
_Pm1001lhCtrlxfpLineLoopIndex_Object=MibTableColumn
pm1001lhCtrlxfpLineLoopIndex=_Pm1001lhCtrlxfpLineLoopIndex_Object((1,3,6,1,4,1,20044,10,6,3,209,1,1),_Pm1001lhCtrlxfpLineLoopIndex_Type())
pm1001lhCtrlxfpLineLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineLoopIndex.setStatus(_A)
_Pm1001lhCtrlxfpLineLoopPortn_Type=EkiState
_Pm1001lhCtrlxfpLineLoopPortn_Object=MibTableColumn
pm1001lhCtrlxfpLineLoopPortn=_Pm1001lhCtrlxfpLineLoopPortn_Object((1,3,6,1,4,1,20044,10,6,3,209,1,2),_Pm1001lhCtrlxfpLineLoopPortn_Type())
pm1001lhCtrlxfpLineLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineLoopPortn.setStatus(_A)
_Pm1001lhCtrlxfpLineXfiLoopTable_Object=MibTable
pm1001lhCtrlxfpLineXfiLoopTable=_Pm1001lhCtrlxfpLineXfiLoopTable_Object((1,3,6,1,4,1,20044,10,6,3,210))
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineXfiLoopTable.setStatus(_A)
_Pm1001lhCtrlxfpLineXfiLoopEntry_Object=MibTableRow
pm1001lhCtrlxfpLineXfiLoopEntry=_Pm1001lhCtrlxfpLineXfiLoopEntry_Object((1,3,6,1,4,1,20044,10,6,3,210,1))
pm1001lhCtrlxfpLineXfiLoopEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineXfiLoopEntry.setStatus(_A)
class _Pm1001lhCtrlxfpLineXfiLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrlxfpLineXfiLoopIndex_Type.__name__=_E
_Pm1001lhCtrlxfpLineXfiLoopIndex_Object=MibTableColumn
pm1001lhCtrlxfpLineXfiLoopIndex=_Pm1001lhCtrlxfpLineXfiLoopIndex_Object((1,3,6,1,4,1,20044,10,6,3,210,1,1),_Pm1001lhCtrlxfpLineXfiLoopIndex_Type())
pm1001lhCtrlxfpLineXfiLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineXfiLoopIndex.setStatus(_A)
_Pm1001lhCtrlxfpLineXfiLoopPortn_Type=EkiState
_Pm1001lhCtrlxfpLineXfiLoopPortn_Object=MibTableColumn
pm1001lhCtrlxfpLineXfiLoopPortn=_Pm1001lhCtrlxfpLineXfiLoopPortn_Object((1,3,6,1,4,1,20044,10,6,3,210,1,2),_Pm1001lhCtrlxfpLineXfiLoopPortn_Type())
pm1001lhCtrlxfpLineXfiLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlxfpLineXfiLoopPortn.setStatus(_A)
_Pm1001lhCtrllineTunableChannel_Type=Pm1001lhOtxChannel
_Pm1001lhCtrllineTunableChannel_Object=MibScalar
pm1001lhCtrllineTunableChannel=_Pm1001lhCtrllineTunableChannel_Object((1,3,6,1,4,1,20044,10,6,3,212),_Pm1001lhCtrllineTunableChannel_Type())
pm1001lhCtrllineTunableChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllineTunableChannel.setStatus(_A)
_Pm1001lhCtrllinePhotodiodeMode_Type=Pm1001lhOtxMode
_Pm1001lhCtrllinePhotodiodeMode_Object=MibScalar
pm1001lhCtrllinePhotodiodeMode=_Pm1001lhCtrllinePhotodiodeMode_Object((1,3,6,1,4,1,20044,10,6,3,213),_Pm1001lhCtrllinePhotodiodeMode_Type())
pm1001lhCtrllinePhotodiodeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllinePhotodiodeMode.setStatus(_A)
_Pm1001lhCtrllinePhotodiodeValue_Type=Pm1001lhAdjustValue
_Pm1001lhCtrllinePhotodiodeValue_Object=MibScalar
pm1001lhCtrllinePhotodiodeValue=_Pm1001lhCtrllinePhotodiodeValue_Object((1,3,6,1,4,1,20044,10,6,3,214),_Pm1001lhCtrllinePhotodiodeValue_Type())
pm1001lhCtrllinePhotodiodeValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllinePhotodiodeValue.setStatus(_A)
class _Pm1001lhCtrllinePowerLaser_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001lhCtrllinePowerLaser_Type.__name__=_F
_Pm1001lhCtrllinePowerLaser_Object=MibScalar
pm1001lhCtrllinePowerLaser=_Pm1001lhCtrllinePowerLaser_Object((1,3,6,1,4,1,20044,10,6,3,215),_Pm1001lhCtrllinePowerLaser_Type())
pm1001lhCtrllinePowerLaser.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllinePowerLaser.setStatus(_A)
_Pm1001lhCtrlotxVlhReset_ObjectIdentity=ObjectIdentity
pm1001lhCtrlotxVlhReset=_Pm1001lhCtrlotxVlhReset_ObjectIdentity((1,3,6,1,4,1,20044,10,6,3,216))
_Pm1001lhCtrlOtxVlhReset_Type=EkiOnOff
_Pm1001lhCtrlOtxVlhReset_Object=MibScalar
pm1001lhCtrlOtxVlhReset=_Pm1001lhCtrlOtxVlhReset_Object((1,3,6,1,4,1,20044,10,6,3,216,1),_Pm1001lhCtrlOtxVlhReset_Type())
pm1001lhCtrlOtxVlhReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrlOtxVlhReset.setStatus(_A)
_Pm1001lhCtrllineAccessLoopTable_Object=MibTable
pm1001lhCtrllineAccessLoopTable=_Pm1001lhCtrllineAccessLoopTable_Object((1,3,6,1,4,1,20044,10,6,3,217))
if mibBuilder.loadTexts:pm1001lhCtrllineAccessLoopTable.setStatus(_A)
_Pm1001lhCtrllineAccessLoopEntry_Object=MibTableRow
pm1001lhCtrllineAccessLoopEntry=_Pm1001lhCtrllineAccessLoopEntry_Object((1,3,6,1,4,1,20044,10,6,3,217,1))
pm1001lhCtrllineAccessLoopEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm1001lhCtrllineAccessLoopEntry.setStatus(_A)
class _Pm1001lhCtrllineAccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrllineAccessLoopIndex_Type.__name__=_E
_Pm1001lhCtrllineAccessLoopIndex_Object=MibTableColumn
pm1001lhCtrllineAccessLoopIndex=_Pm1001lhCtrllineAccessLoopIndex_Object((1,3,6,1,4,1,20044,10,6,3,217,1,1),_Pm1001lhCtrllineAccessLoopIndex_Type())
pm1001lhCtrllineAccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrllineAccessLoopIndex.setStatus(_A)
_Pm1001lhCtrllineAccessLoopPortn_Type=EkiState
_Pm1001lhCtrllineAccessLoopPortn_Object=MibTableColumn
pm1001lhCtrllineAccessLoopPortn=_Pm1001lhCtrllineAccessLoopPortn_Object((1,3,6,1,4,1,20044,10,6,3,217,1,2),_Pm1001lhCtrllineAccessLoopPortn_Type())
pm1001lhCtrllineAccessLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllineAccessLoopPortn.setStatus(_A)
_Pm1001lhCtrllineLoopTransceiverTable_Object=MibTable
pm1001lhCtrllineLoopTransceiverTable=_Pm1001lhCtrllineLoopTransceiverTable_Object((1,3,6,1,4,1,20044,10,6,3,218))
if mibBuilder.loadTexts:pm1001lhCtrllineLoopTransceiverTable.setStatus(_A)
_Pm1001lhCtrllineLoopTransceiverEntry_Object=MibTableRow
pm1001lhCtrllineLoopTransceiverEntry=_Pm1001lhCtrllineLoopTransceiverEntry_Object((1,3,6,1,4,1,20044,10,6,3,218,1))
pm1001lhCtrllineLoopTransceiverEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm1001lhCtrllineLoopTransceiverEntry.setStatus(_A)
class _Pm1001lhCtrllineLoopTransceiverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrllineLoopTransceiverIndex_Type.__name__=_E
_Pm1001lhCtrllineLoopTransceiverIndex_Object=MibTableColumn
pm1001lhCtrllineLoopTransceiverIndex=_Pm1001lhCtrllineLoopTransceiverIndex_Object((1,3,6,1,4,1,20044,10,6,3,218,1,1),_Pm1001lhCtrllineLoopTransceiverIndex_Type())
pm1001lhCtrllineLoopTransceiverIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrllineLoopTransceiverIndex.setStatus(_A)
_Pm1001lhCtrllineLoopTransceiverPortn_Type=EkiState
_Pm1001lhCtrllineLoopTransceiverPortn_Object=MibTableColumn
pm1001lhCtrllineLoopTransceiverPortn=_Pm1001lhCtrllineLoopTransceiverPortn_Object((1,3,6,1,4,1,20044,10,6,3,218,1,2),_Pm1001lhCtrllineLoopTransceiverPortn_Type())
pm1001lhCtrllineLoopTransceiverPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllineLoopTransceiverPortn.setStatus(_A)
_Pm1001lhCtrllineResetAllCountTable_Object=MibTable
pm1001lhCtrllineResetAllCountTable=_Pm1001lhCtrllineResetAllCountTable_Object((1,3,6,1,4,1,20044,10,6,3,335))
if mibBuilder.loadTexts:pm1001lhCtrllineResetAllCountTable.setStatus(_A)
_Pm1001lhCtrllineResetAllCountEntry_Object=MibTableRow
pm1001lhCtrllineResetAllCountEntry=_Pm1001lhCtrllineResetAllCountEntry_Object((1,3,6,1,4,1,20044,10,6,3,335,1))
pm1001lhCtrllineResetAllCountEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm1001lhCtrllineResetAllCountEntry.setStatus(_A)
class _Pm1001lhCtrllineResetAllCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCtrllineResetAllCountIndex_Type.__name__=_E
_Pm1001lhCtrllineResetAllCountIndex_Object=MibTableColumn
pm1001lhCtrllineResetAllCountIndex=_Pm1001lhCtrllineResetAllCountIndex_Object((1,3,6,1,4,1,20044,10,6,3,335,1,1),_Pm1001lhCtrllineResetAllCountIndex_Type())
pm1001lhCtrllineResetAllCountIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCtrllineResetAllCountIndex.setStatus(_A)
_Pm1001lhCtrllineResetAllCountsPortn_Type=EkiState
_Pm1001lhCtrllineResetAllCountsPortn_Object=MibTableColumn
pm1001lhCtrllineResetAllCountsPortn=_Pm1001lhCtrllineResetAllCountsPortn_Object((1,3,6,1,4,1,20044,10,6,3,335,1,2),_Pm1001lhCtrllineResetAllCountsPortn_Type())
pm1001lhCtrllineResetAllCountsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCtrllineResetAllCountsPortn.setStatus(_A)
_Pm1001lhri_ObjectIdentity=ObjectIdentity
pm1001lhri=_Pm1001lhri_ObjectIdentity((1,3,6,1,4,1,20044,10,7))
_Pm1001lhriTable_ObjectIdentity=ObjectIdentity
pm1001lhriTable=_Pm1001lhriTable_ObjectIdentity((1,3,6,1,4,1,20044,10,7,1))
_Pm1001lhRinvReloadInventory_Type=EkiOnOff
_Pm1001lhRinvReloadInventory_Object=MibScalar
pm1001lhRinvReloadInventory=_Pm1001lhRinvReloadInventory_Object((1,3,6,1,4,1,20044,10,7,2),_Pm1001lhRinvReloadInventory_Type())
pm1001lhRinvReloadInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhRinvReloadInventory.setStatus(_A)
_Pm1001lhRinvHwPlatform_Type=DisplayString
_Pm1001lhRinvHwPlatform_Object=MibScalar
pm1001lhRinvHwPlatform=_Pm1001lhRinvHwPlatform_Object((1,3,6,1,4,1,20044,10,7,3),_Pm1001lhRinvHwPlatform_Type())
pm1001lhRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhRinvHwPlatform.setStatus(_A)
_Pm1001lhRinvModulePlatform_Type=DisplayString
_Pm1001lhRinvModulePlatform_Object=MibScalar
pm1001lhRinvModulePlatform=_Pm1001lhRinvModulePlatform_Object((1,3,6,1,4,1,20044,10,7,4),_Pm1001lhRinvModulePlatform_Type())
pm1001lhRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhRinvModulePlatform.setStatus(_A)
_Pm1001lhRinvSwPlatform_Type=DisplayString
_Pm1001lhRinvSwPlatform_Object=MibScalar
pm1001lhRinvSwPlatform=_Pm1001lhRinvSwPlatform_Object((1,3,6,1,4,1,20044,10,7,5),_Pm1001lhRinvSwPlatform_Type())
pm1001lhRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhRinvSwPlatform.setStatus(_A)
_Pm1001lhRinvGwPlatform_Type=DisplayString
_Pm1001lhRinvGwPlatform_Object=MibScalar
pm1001lhRinvGwPlatform=_Pm1001lhRinvGwPlatform_Object((1,3,6,1,4,1,20044,10,7,6),_Pm1001lhRinvGwPlatform_Type())
pm1001lhRinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhRinvGwPlatform.setStatus(_A)
_Pm1001lhRinvClient_Type=DisplayString
_Pm1001lhRinvClient_Object=MibScalar
pm1001lhRinvClient=_Pm1001lhRinvClient_Object((1,3,6,1,4,1,20044,10,7,7),_Pm1001lhRinvClient_Type())
pm1001lhRinvClient.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhRinvClient.setStatus(_A)
_Pm1001lhRinvLine_Type=DisplayString
_Pm1001lhRinvLine_Object=MibScalar
pm1001lhRinvLine=_Pm1001lhRinvLine_Object((1,3,6,1,4,1,20044,10,7,8),_Pm1001lhRinvLine_Type())
pm1001lhRinvLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhRinvLine.setStatus(_A)
_Pm1001lhdownload_ObjectIdentity=ObjectIdentity
pm1001lhdownload=_Pm1001lhdownload_ObjectIdentity((1,3,6,1,4,1,20044,10,8))
_Pm1001lhDwlOther_ObjectIdentity=ObjectIdentity
pm1001lhDwlOther=_Pm1001lhDwlOther_ObjectIdentity((1,3,6,1,4,1,20044,10,8,1))
_Pm1001lhDwlrestartProcess_ObjectIdentity=ObjectIdentity
pm1001lhDwlrestartProcess=_Pm1001lhDwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,10,8,1,0))
_Pm1001lhDwlWarmRestartProcessed_Type=EkiOnOff
_Pm1001lhDwlWarmRestartProcessed_Object=MibScalar
pm1001lhDwlWarmRestartProcessed=_Pm1001lhDwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,10,8,1,0,1),_Pm1001lhDwlWarmRestartProcessed_Type())
pm1001lhDwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlWarmRestartProcessed.setStatus(_A)
_Pm1001lhDwlColdRestartProcessed_Type=EkiOnOff
_Pm1001lhDwlColdRestartProcessed_Object=MibScalar
pm1001lhDwlColdRestartProcessed=_Pm1001lhDwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,10,8,1,0,2),_Pm1001lhDwlColdRestartProcessed_Type())
pm1001lhDwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlColdRestartProcessed.setStatus(_A)
_Pm1001lhDwlswBanksUsed_ObjectIdentity=ObjectIdentity
pm1001lhDwlswBanksUsed=_Pm1001lhDwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,10,8,1,1))
_Pm1001lhDwlSwBank1Used_Type=EkiOnOff
_Pm1001lhDwlSwBank1Used_Object=MibScalar
pm1001lhDwlSwBank1Used=_Pm1001lhDwlSwBank1Used_Object((1,3,6,1,4,1,20044,10,8,1,1,1),_Pm1001lhDwlSwBank1Used_Type())
pm1001lhDwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlSwBank1Used.setStatus(_A)
_Pm1001lhDwlSwBank2Used_Type=EkiOnOff
_Pm1001lhDwlSwBank2Used_Object=MibScalar
pm1001lhDwlSwBank2Used=_Pm1001lhDwlSwBank2Used_Object((1,3,6,1,4,1,20044,10,8,1,1,2),_Pm1001lhDwlSwBank2Used_Type())
pm1001lhDwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlSwBank2Used.setStatus(_A)
_Pm1001lhDwlSwBank1Notempty_Type=EkiOnOff
_Pm1001lhDwlSwBank1Notempty_Object=MibScalar
pm1001lhDwlSwBank1Notempty=_Pm1001lhDwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,10,8,1,1,5),_Pm1001lhDwlSwBank1Notempty_Type())
pm1001lhDwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlSwBank1Notempty.setStatus(_A)
_Pm1001lhDwlSwBank2Notempty_Type=EkiOnOff
_Pm1001lhDwlSwBank2Notempty_Object=MibScalar
pm1001lhDwlSwBank2Notempty=_Pm1001lhDwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,10,8,1,1,6),_Pm1001lhDwlSwBank2Notempty_Type())
pm1001lhDwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlSwBank2Notempty.setStatus(_A)
_Pm1001lhDwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pm1001lhDwlgwBanksUsed=_Pm1001lhDwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,10,8,1,2))
_Pm1001lhDwlGwBank1Used_Type=EkiOnOff
_Pm1001lhDwlGwBank1Used_Object=MibScalar
pm1001lhDwlGwBank1Used=_Pm1001lhDwlGwBank1Used_Object((1,3,6,1,4,1,20044,10,8,1,2,1),_Pm1001lhDwlGwBank1Used_Type())
pm1001lhDwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank1Used.setStatus(_A)
_Pm1001lhDwlGwBank2Used_Type=EkiOnOff
_Pm1001lhDwlGwBank2Used_Object=MibScalar
pm1001lhDwlGwBank2Used=_Pm1001lhDwlGwBank2Used_Object((1,3,6,1,4,1,20044,10,8,1,2,2),_Pm1001lhDwlGwBank2Used_Type())
pm1001lhDwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank2Used.setStatus(_G)
_Pm1001lhDwlGwBank3Used_Type=EkiOnOff
_Pm1001lhDwlGwBank3Used_Object=MibScalar
pm1001lhDwlGwBank3Used=_Pm1001lhDwlGwBank3Used_Object((1,3,6,1,4,1,20044,10,8,1,2,3),_Pm1001lhDwlGwBank3Used_Type())
pm1001lhDwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank3Used.setStatus(_A)
_Pm1001lhDwlGwBank4Used_Type=EkiOnOff
_Pm1001lhDwlGwBank4Used_Object=MibScalar
pm1001lhDwlGwBank4Used=_Pm1001lhDwlGwBank4Used_Object((1,3,6,1,4,1,20044,10,8,1,2,4),_Pm1001lhDwlGwBank4Used_Type())
pm1001lhDwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank4Used.setStatus(_G)
_Pm1001lhDwlGwBank1Notempty_Type=EkiOnOff
_Pm1001lhDwlGwBank1Notempty_Object=MibScalar
pm1001lhDwlGwBank1Notempty=_Pm1001lhDwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,10,8,1,2,5),_Pm1001lhDwlGwBank1Notempty_Type())
pm1001lhDwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank1Notempty.setStatus(_A)
_Pm1001lhDwlGwBank2Notempty_Type=EkiOnOff
_Pm1001lhDwlGwBank2Notempty_Object=MibScalar
pm1001lhDwlGwBank2Notempty=_Pm1001lhDwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,10,8,1,2,6),_Pm1001lhDwlGwBank2Notempty_Type())
pm1001lhDwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank2Notempty.setStatus(_G)
_Pm1001lhDwlGwBank3Notempty_Type=EkiOnOff
_Pm1001lhDwlGwBank3Notempty_Object=MibScalar
pm1001lhDwlGwBank3Notempty=_Pm1001lhDwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,10,8,1,2,7),_Pm1001lhDwlGwBank3Notempty_Type())
pm1001lhDwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank3Notempty.setStatus(_A)
_Pm1001lhDwlGwBank4Notempty_Type=EkiOnOff
_Pm1001lhDwlGwBank4Notempty_Object=MibScalar
pm1001lhDwlGwBank4Notempty=_Pm1001lhDwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,10,8,1,2,8),_Pm1001lhDwlGwBank4Notempty_Type())
pm1001lhDwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhDwlGwBank4Notempty.setStatus(_G)
_Pm1001lhDwlClient_ObjectIdentity=ObjectIdentity
pm1001lhDwlClient=_Pm1001lhDwlClient_ObjectIdentity((1,3,6,1,4,1,20044,10,8,2))
_Pm1001lhDwlLine_ObjectIdentity=ObjectIdentity
pm1001lhDwlLine=_Pm1001lhDwlLine_ObjectIdentity((1,3,6,1,4,1,20044,10,8,3))
_Pm1001lhConfig_ObjectIdentity=ObjectIdentity
pm1001lhConfig=_Pm1001lhConfig_ObjectIdentity((1,3,6,1,4,1,20044,10,10))
_Pm1001lhCfgAccessCAisCsf_ObjectIdentity=ObjectIdentity
pm1001lhCfgAccessCAisCsf=_Pm1001lhCfgAccessCAisCsf_ObjectIdentity((1,3,6,1,4,1,20044,10,10,1))
_Pm1001lhCfgClientcaiscsfTable_Object=MibTable
pm1001lhCfgClientcaiscsfTable=_Pm1001lhCfgClientcaiscsfTable_Object((1,3,6,1,4,1,20044,10,10,1,1))
if mibBuilder.loadTexts:pm1001lhCfgClientcaiscsfTable.setStatus(_A)
_Pm1001lhCfgClientcaiscsfEntry_Object=MibTableRow
pm1001lhCfgClientcaiscsfEntry=_Pm1001lhCfgClientcaiscsfEntry_Object((1,3,6,1,4,1,20044,10,10,1,1,1))
pm1001lhCfgClientcaiscsfEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm1001lhCfgClientcaiscsfEntry.setStatus(_A)
class _Pm1001lhCfgClientcaiscsfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgClientcaiscsfIndex_Type.__name__=_E
_Pm1001lhCfgClientcaiscsfIndex_Object=MibTableColumn
pm1001lhCfgClientcaiscsfIndex=_Pm1001lhCfgClientcaiscsfIndex_Object((1,3,6,1,4,1,20044,10,10,1,1,1,1),_Pm1001lhCfgClientcaiscsfIndex_Type())
pm1001lhCfgClientcaiscsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgClientcaiscsfIndex.setStatus(_A)
class _Pm1001lhCfgCAisModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgCAisModePortn_Type.__name__=_F
_Pm1001lhCfgCAisModePortn_Object=MibTableColumn
pm1001lhCfgCAisModePortn=_Pm1001lhCfgCAisModePortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,3),_Pm1001lhCfgCAisModePortn_Type())
pm1001lhCfgCAisModePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgCAisModePortn.setStatus(_A)
class _Pm1001lhCfgUpAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgUpAccessioAlmPortn_Type.__name__=_F
_Pm1001lhCfgUpAccessioAlmPortn_Object=MibTableColumn
pm1001lhCfgUpAccessioAlmPortn=_Pm1001lhCfgUpAccessioAlmPortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,9),_Pm1001lhCfgUpAccessioAlmPortn_Type())
pm1001lhCfgUpAccessioAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgUpAccessioAlmPortn.setStatus(_A)
class _Pm1001lhCfgUpMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgUpMapperDeAlmPortn_Type.__name__=_F
_Pm1001lhCfgUpMapperDeAlmPortn_Object=MibTableColumn
pm1001lhCfgUpMapperDeAlmPortn=_Pm1001lhCfgUpMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,10),_Pm1001lhCfgUpMapperDeAlmPortn_Type())
pm1001lhCfgUpMapperDeAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgUpMapperDeAlmPortn.setStatus(_A)
class _Pm1001lhCfgDownAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgDownAccessioAlmPortn_Type.__name__=_F
_Pm1001lhCfgDownAccessioAlmPortn_Object=MibTableColumn
pm1001lhCfgDownAccessioAlmPortn=_Pm1001lhCfgDownAccessioAlmPortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,17),_Pm1001lhCfgDownAccessioAlmPortn_Type())
pm1001lhCfgDownAccessioAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgDownAccessioAlmPortn.setStatus(_A)
class _Pm1001lhCfgDownMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgDownMapperDeAlmPortn_Type.__name__=_F
_Pm1001lhCfgDownMapperDeAlmPortn_Object=MibTableColumn
pm1001lhCfgDownMapperDeAlmPortn=_Pm1001lhCfgDownMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,18),_Pm1001lhCfgDownMapperDeAlmPortn_Type())
pm1001lhCfgDownMapperDeAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgDownMapperDeAlmPortn.setStatus(_A)
class _Pm1001lhCfgDownDfrmAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgDownDfrmAlmPortn_Type.__name__=_F
_Pm1001lhCfgDownDfrmAlmPortn_Object=MibTableColumn
pm1001lhCfgDownDfrmAlmPortn=_Pm1001lhCfgDownDfrmAlmPortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,19),_Pm1001lhCfgDownDfrmAlmPortn_Type())
pm1001lhCfgDownDfrmAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgDownDfrmAlmPortn.setStatus(_A)
class _Pm1001lhCfgDownLineSyncAlarmsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgDownLineSyncAlarmsPortn_Type.__name__=_F
_Pm1001lhCfgDownLineSyncAlarmsPortn_Object=MibTableColumn
pm1001lhCfgDownLineSyncAlarmsPortn=_Pm1001lhCfgDownLineSyncAlarmsPortn_Object((1,3,6,1,4,1,20044,10,10,1,1,1,20),_Pm1001lhCfgDownLineSyncAlarmsPortn_Type())
pm1001lhCfgDownLineSyncAlarmsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgDownLineSyncAlarmsPortn.setStatus(_G)
_Pm1001lhCfgStartup_ObjectIdentity=ObjectIdentity
pm1001lhCfgStartup=_Pm1001lhCfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,10,10,2))
_Pm1001lhCfgClientStartupTable_Object=MibTable
pm1001lhCfgClientStartupTable=_Pm1001lhCfgClientStartupTable_Object((1,3,6,1,4,1,20044,10,10,2,1))
if mibBuilder.loadTexts:pm1001lhCfgClientStartupTable.setStatus(_A)
_Pm1001lhCfgClientStartupEntry_Object=MibTableRow
pm1001lhCfgClientStartupEntry=_Pm1001lhCfgClientStartupEntry_Object((1,3,6,1,4,1,20044,10,10,2,1,1))
pm1001lhCfgClientStartupEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm1001lhCfgClientStartupEntry.setStatus(_A)
class _Pm1001lhCfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgClientStartupIndex_Type.__name__=_E
_Pm1001lhCfgClientStartupIndex_Object=MibTableColumn
pm1001lhCfgClientStartupIndex=_Pm1001lhCfgClientStartupIndex_Object((1,3,6,1,4,1,20044,10,10,2,1,1,1),_Pm1001lhCfgClientStartupIndex_Type())
pm1001lhCfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgClientStartupIndex.setStatus(_A)
class _Pm1001lhCfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgSystConfPortPortn_Type.__name__=_F
_Pm1001lhCfgSystConfPortPortn_Object=MibTableColumn
pm1001lhCfgSystConfPortPortn=_Pm1001lhCfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,10,10,2,1,1,3),_Pm1001lhCfgSystConfPortPortn_Type())
pm1001lhCfgSystConfPortPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgSystConfPortPortn.setStatus(_A)
class _Pm1001lhCfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgNetConfPortPortn_Type.__name__=_F
_Pm1001lhCfgNetConfPortPortn_Object=MibTableColumn
pm1001lhCfgNetConfPortPortn=_Pm1001lhCfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,10,10,2,1,1,4),_Pm1001lhCfgNetConfPortPortn_Type())
pm1001lhCfgNetConfPortPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgNetConfPortPortn.setStatus(_A)
class _Pm1001lhCfgPortsOptionsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgPortsOptionsPortn_Type.__name__=_F
_Pm1001lhCfgPortsOptionsPortn_Object=MibTableColumn
pm1001lhCfgPortsOptionsPortn=_Pm1001lhCfgPortsOptionsPortn_Object((1,3,6,1,4,1,20044,10,10,2,1,1,6),_Pm1001lhCfgPortsOptionsPortn_Type())
pm1001lhCfgPortsOptionsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgPortsOptionsPortn.setStatus(_A)
_Pm1001lhtablelineStartup_ObjectIdentity=ObjectIdentity
pm1001lhtablelineStartup=_Pm1001lhtablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,10,10,2,2))
class _Pm1001lhCfgsynthTransLine_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgsynthTransLine_Type.__name__=_F
_Pm1001lhCfgsynthTransLine_Object=MibScalar
pm1001lhCfgsynthTransLine=_Pm1001lhCfgsynthTransLine_Object((1,3,6,1,4,1,20044,10,10,2,2,2),_Pm1001lhCfgsynthTransLine_Type())
pm1001lhCfgsynthTransLine.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgsynthTransLine.setStatus(_A)
class _Pm1001lhCfglineOptions1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfglineOptions1_Type.__name__=_F
_Pm1001lhCfglineOptions1_Object=MibScalar
pm1001lhCfglineOptions1=_Pm1001lhCfglineOptions1_Object((1,3,6,1,4,1,20044,10,10,2,2,5),_Pm1001lhCfglineOptions1_Type())
pm1001lhCfglineOptions1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfglineOptions1.setStatus(_A)
_Pm1001lhCfgXfpTable_Object=MibTable
pm1001lhCfgXfpTable=_Pm1001lhCfgXfpTable_Object((1,3,6,1,4,1,20044,10,10,2,3))
if mibBuilder.loadTexts:pm1001lhCfgXfpTable.setStatus(_A)
_Pm1001lhCfgXfpEntry_Object=MibTableRow
pm1001lhCfgXfpEntry=_Pm1001lhCfgXfpEntry_Object((1,3,6,1,4,1,20044,10,10,2,3,1))
pm1001lhCfgXfpEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm1001lhCfgXfpEntry.setStatus(_A)
class _Pm1001lhCfgXfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgXfpIndex_Type.__name__=_E
_Pm1001lhCfgXfpIndex_Object=MibTableColumn
pm1001lhCfgXfpIndex=_Pm1001lhCfgXfpIndex_Object((1,3,6,1,4,1,20044,10,10,2,3,1,1),_Pm1001lhCfgXfpIndex_Type())
pm1001lhCfgXfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgXfpIndex.setStatus(_A)
class _Pm1001lhCfgSystConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgSystConfXfpPortn_Type.__name__=_F
_Pm1001lhCfgSystConfXfpPortn_Object=MibTableColumn
pm1001lhCfgSystConfXfpPortn=_Pm1001lhCfgSystConfXfpPortn_Object((1,3,6,1,4,1,20044,10,10,2,3,1,3),_Pm1001lhCfgSystConfXfpPortn_Type())
pm1001lhCfgSystConfXfpPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgSystConfXfpPortn.setStatus(_A)
class _Pm1001lhCfgDataRateConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgDataRateConfXfpPortn_Type.__name__=_F
_Pm1001lhCfgDataRateConfXfpPortn_Object=MibTableColumn
pm1001lhCfgDataRateConfXfpPortn=_Pm1001lhCfgDataRateConfXfpPortn_Object((1,3,6,1,4,1,20044,10,10,2,3,1,4),_Pm1001lhCfgDataRateConfXfpPortn_Type())
pm1001lhCfgDataRateConfXfpPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgDataRateConfXfpPortn.setStatus(_G)
_Pm1001lhCfgOtxtlhTable_Object=MibTable
pm1001lhCfgOtxtlhTable=_Pm1001lhCfgOtxtlhTable_Object((1,3,6,1,4,1,20044,10,10,2,4))
if mibBuilder.loadTexts:pm1001lhCfgOtxtlhTable.setStatus(_A)
_Pm1001lhCfgOtxtlhEntry_Object=MibTableRow
pm1001lhCfgOtxtlhEntry=_Pm1001lhCfgOtxtlhEntry_Object((1,3,6,1,4,1,20044,10,10,2,4,1))
pm1001lhCfgOtxtlhEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm1001lhCfgOtxtlhEntry.setStatus(_A)
class _Pm1001lhCfgOtxtlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgOtxtlhIndex_Type.__name__=_E
_Pm1001lhCfgOtxtlhIndex_Object=MibTableColumn
pm1001lhCfgOtxtlhIndex=_Pm1001lhCfgOtxtlhIndex_Object((1,3,6,1,4,1,20044,10,10,2,4,1,1),_Pm1001lhCfgOtxtlhIndex_Type())
pm1001lhCfgOtxtlhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgOtxtlhIndex.setStatus(_A)
class _Pm1001lhCfgLineOtxMiscPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLineOtxMiscPortn_Type.__name__=_F
_Pm1001lhCfgLineOtxMiscPortn_Object=MibTableColumn
pm1001lhCfgLineOtxMiscPortn=_Pm1001lhCfgLineOtxMiscPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,3),_Pm1001lhCfgLineOtxMiscPortn_Type())
pm1001lhCfgLineOtxMiscPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLineOtxMiscPortn.setStatus(_A)
class _Pm1001lhCfgLineDitherRatePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLineDitherRatePortn_Type.__name__=_F
_Pm1001lhCfgLineDitherRatePortn_Object=MibTableColumn
pm1001lhCfgLineDitherRatePortn=_Pm1001lhCfgLineDitherRatePortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,4),_Pm1001lhCfgLineDitherRatePortn_Type())
pm1001lhCfgLineDitherRatePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLineDitherRatePortn.setStatus(_A)
class _Pm1001lhCfgLineDitherFhzPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLineDitherFhzPortn_Type.__name__=_F
_Pm1001lhCfgLineDitherFhzPortn_Object=MibTableColumn
pm1001lhCfgLineDitherFhzPortn=_Pm1001lhCfgLineDitherFhzPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,5),_Pm1001lhCfgLineDitherFhzPortn_Type())
pm1001lhCfgLineDitherFhzPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLineDitherFhzPortn.setStatus(_A)
class _Pm1001lhCfgLinePwrLaserPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLinePwrLaserPortn_Type.__name__=_F
_Pm1001lhCfgLinePwrLaserPortn_Object=MibTableColumn
pm1001lhCfgLinePwrLaserPortn=_Pm1001lhCfgLinePwrLaserPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,6),_Pm1001lhCfgLinePwrLaserPortn_Type())
pm1001lhCfgLinePwrLaserPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLinePwrLaserPortn.setStatus(_A)
class _Pm1001lhCfgLineFCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLineFCurrentPortn_Type.__name__=_F
_Pm1001lhCfgLineFCurrentPortn_Object=MibTableColumn
pm1001lhCfgLineFCurrentPortn=_Pm1001lhCfgLineFCurrentPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,7),_Pm1001lhCfgLineFCurrentPortn_Type())
pm1001lhCfgLineFCurrentPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLineFCurrentPortn.setStatus(_A)
class _Pm1001lhCfgLineGridCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLineGridCurrentPortn_Type.__name__=_F
_Pm1001lhCfgLineGridCurrentPortn_Object=MibTableColumn
pm1001lhCfgLineGridCurrentPortn=_Pm1001lhCfgLineGridCurrentPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,8),_Pm1001lhCfgLineGridCurrentPortn_Type())
pm1001lhCfgLineGridCurrentPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLineGridCurrentPortn.setStatus(_A)
class _Pm1001lhCfgFPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgFPortn_Type.__name__=_F
_Pm1001lhCfgFPortn_Object=MibTableColumn
pm1001lhCfgFPortn=_Pm1001lhCfgFPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,9),_Pm1001lhCfgFPortn_Type())
pm1001lhCfgFPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgFPortn.setStatus(_A)
class _Pm1001lhCfgReservedPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgReservedPortn_Type.__name__=_F
_Pm1001lhCfgReservedPortn_Object=MibTableColumn
pm1001lhCfgReservedPortn=_Pm1001lhCfgReservedPortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,10),_Pm1001lhCfgReservedPortn_Type())
pm1001lhCfgReservedPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgReservedPortn.setStatus(_G)
class _Pm1001lhCfgLinePhotodiodeModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLinePhotodiodeModePortn_Type.__name__=_F
_Pm1001lhCfgLinePhotodiodeModePortn_Object=MibTableColumn
pm1001lhCfgLinePhotodiodeModePortn=_Pm1001lhCfgLinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,11),_Pm1001lhCfgLinePhotodiodeModePortn_Type())
pm1001lhCfgLinePhotodiodeModePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLinePhotodiodeModePortn.setStatus(_A)
class _Pm1001lhCfgLinePhotodiodeValuePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLinePhotodiodeValuePortn_Type.__name__=_F
_Pm1001lhCfgLinePhotodiodeValuePortn_Object=MibTableColumn
pm1001lhCfgLinePhotodiodeValuePortn=_Pm1001lhCfgLinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,10,10,2,4,1,12),_Pm1001lhCfgLinePhotodiodeValuePortn_Type())
pm1001lhCfgLinePhotodiodeValuePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLinePhotodiodeValuePortn.setStatus(_A)
_Pm1001lhCfgLabels_ObjectIdentity=ObjectIdentity
pm1001lhCfgLabels=_Pm1001lhCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,10,10,3))
_Pm1001lhCfgLabelclientTable_Object=MibTable
pm1001lhCfgLabelclientTable=_Pm1001lhCfgLabelclientTable_Object((1,3,6,1,4,1,20044,10,10,3,1))
if mibBuilder.loadTexts:pm1001lhCfgLabelclientTable.setStatus(_A)
_Pm1001lhCfgLabelclientEntry_Object=MibTableRow
pm1001lhCfgLabelclientEntry=_Pm1001lhCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,10,10,3,1,1))
pm1001lhCfgLabelclientEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm1001lhCfgLabelclientEntry.setStatus(_A)
class _Pm1001lhCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgLabelclientIndex_Type.__name__=_E
_Pm1001lhCfgLabelclientIndex_Object=MibTableColumn
pm1001lhCfgLabelclientIndex=_Pm1001lhCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,10,10,3,1,1,1),_Pm1001lhCfgLabelclientIndex_Type())
pm1001lhCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgLabelclientIndex.setStatus(_A)
class _Pm1001lhCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1001lhCfgLabelclientPortn_Type.__name__=_I
_Pm1001lhCfgLabelclientPortn_Object=MibTableColumn
pm1001lhCfgLabelclientPortn=_Pm1001lhCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,10,10,3,1,1,3),_Pm1001lhCfgLabelclientPortn_Type())
pm1001lhCfgLabelclientPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLabelclientPortn.setStatus(_A)
_Pm1001lhCfgLabellineTable_Object=MibTable
pm1001lhCfgLabellineTable=_Pm1001lhCfgLabellineTable_Object((1,3,6,1,4,1,20044,10,10,3,2))
if mibBuilder.loadTexts:pm1001lhCfgLabellineTable.setStatus(_A)
_Pm1001lhCfgLabellineEntry_Object=MibTableRow
pm1001lhCfgLabellineEntry=_Pm1001lhCfgLabellineEntry_Object((1,3,6,1,4,1,20044,10,10,3,2,1))
pm1001lhCfgLabellineEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm1001lhCfgLabellineEntry.setStatus(_A)
class _Pm1001lhCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgLabellineIndex_Type.__name__=_E
_Pm1001lhCfgLabellineIndex_Object=MibTableColumn
pm1001lhCfgLabellineIndex=_Pm1001lhCfgLabellineIndex_Object((1,3,6,1,4,1,20044,10,10,3,2,1,1),_Pm1001lhCfgLabellineIndex_Type())
pm1001lhCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgLabellineIndex.setStatus(_A)
class _Pm1001lhCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1001lhCfgLabellinePortn_Type.__name__=_I
_Pm1001lhCfgLabellinePortn_Object=MibTableColumn
pm1001lhCfgLabellinePortn=_Pm1001lhCfgLabellinePortn_Object((1,3,6,1,4,1,20044,10,10,3,2,1,3),_Pm1001lhCfgLabellinePortn_Type())
pm1001lhCfgLabellinePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgLabellinePortn.setStatus(_A)
_Pm1001lhCfgStartuptablefive_ObjectIdentity=ObjectIdentity
pm1001lhCfgStartuptablefive=_Pm1001lhCfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,10,10,4))
_Pm1001lhCfgOtxtlhcapabilitiesTable_Object=MibTable
pm1001lhCfgOtxtlhcapabilitiesTable=_Pm1001lhCfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,10,10,4,1))
if mibBuilder.loadTexts:pm1001lhCfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pm1001lhCfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pm1001lhCfgOtxtlhcapabilitiesEntry=_Pm1001lhCfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,10,10,4,1,1))
pm1001lhCfgOtxtlhcapabilitiesEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm1001lhCfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pm1001lhCfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhCfgOtxtlhcapabilitiesIndex_Type.__name__=_E
_Pm1001lhCfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pm1001lhCfgOtxtlhcapabilitiesIndex=_Pm1001lhCfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,10,10,4,1,1,1),_Pm1001lhCfgOtxtlhcapabilitiesIndex_Type())
pm1001lhCfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pm1001lhCfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgComponentTypePortn_Type.__name__=_F
_Pm1001lhCfgComponentTypePortn_Object=MibTableColumn
pm1001lhCfgComponentTypePortn=_Pm1001lhCfgComponentTypePortn_Object((1,3,6,1,4,1,20044,10,10,4,1,1,3),_Pm1001lhCfgComponentTypePortn_Type())
pm1001lhCfgComponentTypePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgComponentTypePortn.setStatus(_A)
class _Pm1001lhCfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgMiscellaneousPortn_Type.__name__=_F
_Pm1001lhCfgMiscellaneousPortn_Object=MibTableColumn
pm1001lhCfgMiscellaneousPortn=_Pm1001lhCfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,10,10,4,1,1,4),_Pm1001lhCfgMiscellaneousPortn_Type())
pm1001lhCfgMiscellaneousPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgMiscellaneousPortn.setStatus(_A)
class _Pm1001lhCfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgFirstChannelPortn_Type.__name__=_F
_Pm1001lhCfgFirstChannelPortn_Object=MibTableColumn
pm1001lhCfgFirstChannelPortn=_Pm1001lhCfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,10,10,4,1,1,5),_Pm1001lhCfgFirstChannelPortn_Type())
pm1001lhCfgFirstChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgFirstChannelPortn.setStatus(_A)
class _Pm1001lhCfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgLastChannelPortn_Type.__name__=_F
_Pm1001lhCfgLastChannelPortn_Object=MibTableColumn
pm1001lhCfgLastChannelPortn=_Pm1001lhCfgLastChannelPortn_Object((1,3,6,1,4,1,20044,10,10,4,1,1,6),_Pm1001lhCfgLastChannelPortn_Type())
pm1001lhCfgLastChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgLastChannelPortn.setStatus(_A)
class _Pm1001lhCfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001lhCfgGridPortn_Type.__name__=_F
_Pm1001lhCfgGridPortn_Object=MibTableColumn
pm1001lhCfgGridPortn=_Pm1001lhCfgGridPortn_Object((1,3,6,1,4,1,20044,10,10,4,1,1,7),_Pm1001lhCfgGridPortn_Type())
pm1001lhCfgGridPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhCfgGridPortn.setStatus(_A)
_Pm1001lhCfgWriteConfiguration_Type=EkiOnOff
_Pm1001lhCfgWriteConfiguration_Object=MibScalar
pm1001lhCfgWriteConfiguration=_Pm1001lhCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,10,10,257),_Pm1001lhCfgWriteConfiguration_Type())
pm1001lhCfgWriteConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhCfgWriteConfiguration.setStatus(_A)
_Pm1001lhtraps_ObjectIdentity=ObjectIdentity
pm1001lhtraps=_Pm1001lhtraps_ObjectIdentity((1,3,6,1,4,1,20044,10,11))
class _Pm1001lhtrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1001lhtrapBoardNumber_Type.__name__=_E
_Pm1001lhtrapBoardNumber_Object=MibScalar
pm1001lhtrapBoardNumber=_Pm1001lhtrapBoardNumber_Object((1,3,6,1,4,1,20044,10,11,1),_Pm1001lhtrapBoardNumber_Type())
pm1001lhtrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhtrapBoardNumber.setStatus(_A)
_Pm1001lhMonitoring_ObjectIdentity=ObjectIdentity
pm1001lhMonitoring=_Pm1001lhMonitoring_ObjectIdentity((1,3,6,1,4,1,20044,10,12))
_Pm1001lhMonOther_ObjectIdentity=ObjectIdentity
pm1001lhMonOther=_Pm1001lhMonOther_ObjectIdentity((1,3,6,1,4,1,20044,10,12,1))
_Pm1001lhMonSync_ObjectIdentity=ObjectIdentity
pm1001lhMonSync=_Pm1001lhMonSync_ObjectIdentity((1,3,6,1,4,1,20044,10,12,1,1))
_Pm1001lhPerfEnable_Type=EkiOnOff
_Pm1001lhPerfEnable_Object=MibScalar
pm1001lhPerfEnable=_Pm1001lhPerfEnable_Object((1,3,6,1,4,1,20044,10,12,1,1,257),_Pm1001lhPerfEnable_Type())
pm1001lhPerfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerfEnable.setStatus(_A)
_Pm1001lhPerf15minSync_Type=EkiOnOff
_Pm1001lhPerf15minSync_Object=MibScalar
pm1001lhPerf15minSync=_Pm1001lhPerf15minSync_Object((1,3,6,1,4,1,20044,10,12,1,1,259),_Pm1001lhPerf15minSync_Type())
pm1001lhPerf15minSync.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerf15minSync.setStatus(_A)
_Pm1001lhPerf24hSync_Type=EkiOnOff
_Pm1001lhPerf24hSync_Object=MibScalar
pm1001lhPerf24hSync=_Pm1001lhPerf24hSync_Object((1,3,6,1,4,1,20044,10,12,1,1,260),_Pm1001lhPerf24hSync_Type())
pm1001lhPerf24hSync.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerf24hSync.setStatus(_A)
_Pm1001lhMonTimeStamp_ObjectIdentity=ObjectIdentity
pm1001lhMonTimeStamp=_Pm1001lhMonTimeStamp_ObjectIdentity((1,3,6,1,4,1,20044,10,12,1,2))
_Pm1001lhPerf15MinShort_Type=EkiOnOff
_Pm1001lhPerf15MinShort_Object=MibScalar
pm1001lhPerf15MinShort=_Pm1001lhPerf15MinShort_Object((1,3,6,1,4,1,20044,10,12,1,2,1),_Pm1001lhPerf15MinShort_Type())
pm1001lhPerf15MinShort.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerf15MinShort.setStatus(_A)
_Pm1001lhPerf15MinLong_Type=EkiOnOff
_Pm1001lhPerf15MinLong_Object=MibScalar
pm1001lhPerf15MinLong=_Pm1001lhPerf15MinLong_Object((1,3,6,1,4,1,20044,10,12,1,2,2),_Pm1001lhPerf15MinLong_Type())
pm1001lhPerf15MinLong.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerf15MinLong.setStatus(_A)
_Pm1001lhPerf24HoursShort_Type=Counter32
_Pm1001lhPerf24HoursShort_Object=MibScalar
pm1001lhPerf24HoursShort=_Pm1001lhPerf24HoursShort_Object((1,3,6,1,4,1,20044,10,12,1,2,5),_Pm1001lhPerf24HoursShort_Type())
pm1001lhPerf24HoursShort.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerf24HoursShort.setStatus(_A)
_Pm1001lhPerf24HoursLong_Type=Counter32
_Pm1001lhPerf24HoursLong_Object=MibScalar
pm1001lhPerf24HoursLong=_Pm1001lhPerf24HoursLong_Object((1,3,6,1,4,1,20044,10,12,1,2,6),_Pm1001lhPerf24HoursLong_Type())
pm1001lhPerf24HoursLong.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerf24HoursLong.setStatus(_A)
_Pm1001lhPerfCurrent15MinElapsedTime_Type=Counter32
_Pm1001lhPerfCurrent15MinElapsedTime_Object=MibScalar
pm1001lhPerfCurrent15MinElapsedTime=_Pm1001lhPerfCurrent15MinElapsedTime_Object((1,3,6,1,4,1,20044,10,12,1,2,7),_Pm1001lhPerfCurrent15MinElapsedTime_Type())
pm1001lhPerfCurrent15MinElapsedTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerfCurrent15MinElapsedTime.setStatus(_A)
_Pm1001lhPerfCurrent24HoursElapsedTime_Type=Counter32
_Pm1001lhPerfCurrent24HoursElapsedTime_Object=MibScalar
pm1001lhPerfCurrent24HoursElapsedTime=_Pm1001lhPerfCurrent24HoursElapsedTime_Object((1,3,6,1,4,1,20044,10,12,1,2,8),_Pm1001lhPerfCurrent24HoursElapsedTime_Type())
pm1001lhPerfCurrent24HoursElapsedTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhPerfCurrent24HoursElapsedTime.setStatus(_A)
_Pm1001lhMonClient_ObjectIdentity=ObjectIdentity
pm1001lhMonClient=_Pm1001lhMonClient_ObjectIdentity((1,3,6,1,4,1,20044,10,12,2))
_Pm1001lhPerfTelecomClientCurrent15StatTable_Object=MibTable
pm1001lhPerfTelecomClientCurrent15StatTable=_Pm1001lhPerfTelecomClientCurrent15StatTable_Object((1,3,6,1,4,1,20044,10,12,2,16))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatTable.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatEntry_Object=MibTableRow
pm1001lhPerfTelecomClientCurrent15StatEntry=_Pm1001lhPerfTelecomClientCurrent15StatEntry_Object((1,3,6,1,4,1,20044,10,12,2,16,1))
pm1001lhPerfTelecomClientCurrent15StatEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatEntry.setStatus(_A)
class _Pm1001lhPerfTelecomClientCurrent15StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomClientCurrent15StatIndex_Type.__name__=_E
_Pm1001lhPerfTelecomClientCurrent15StatIndex_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatIndex=_Pm1001lhPerfTelecomClientCurrent15StatIndex_Object((1,3,6,1,4,1,20044,10,12,2,16,1,1),_Pm1001lhPerfTelecomClientCurrent15StatIndex_Type())
pm1001lhPerfTelecomClientCurrent15StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatIndex.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatInvCvPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent15StatInvCvPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatInvCvPortn=_Pm1001lhPerfTelecomClientCurrent15StatInvCvPortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,2),_Pm1001lhPerfTelecomClientCurrent15StatInvCvPortn_Type())
pm1001lhPerfTelecomClientCurrent15StatInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatInvCvPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatCvValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent15StatCvValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatCvValuePortn=_Pm1001lhPerfTelecomClientCurrent15StatCvValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,3),_Pm1001lhPerfTelecomClientCurrent15StatCvValuePortn_Type())
pm1001lhPerfTelecomClientCurrent15StatCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatCvValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatInvEsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent15StatInvEsPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatInvEsPortn=_Pm1001lhPerfTelecomClientCurrent15StatInvEsPortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,4),_Pm1001lhPerfTelecomClientCurrent15StatInvEsPortn_Type())
pm1001lhPerfTelecomClientCurrent15StatInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatInvEsPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatEsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent15StatEsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatEsValuePortn=_Pm1001lhPerfTelecomClientCurrent15StatEsValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,5),_Pm1001lhPerfTelecomClientCurrent15StatEsValuePortn_Type())
pm1001lhPerfTelecomClientCurrent15StatEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatEsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatInvSesPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent15StatInvSesPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatInvSesPortn=_Pm1001lhPerfTelecomClientCurrent15StatInvSesPortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,6),_Pm1001lhPerfTelecomClientCurrent15StatInvSesPortn_Type())
pm1001lhPerfTelecomClientCurrent15StatInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatInvSesPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatSesValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent15StatSesValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatSesValuePortn=_Pm1001lhPerfTelecomClientCurrent15StatSesValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,7),_Pm1001lhPerfTelecomClientCurrent15StatSesValuePortn_Type())
pm1001lhPerfTelecomClientCurrent15StatSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatSesValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn=_Pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,8),_Pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn_Type())
pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn=_Pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,9),_Pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn_Type())
pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatInvUasPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent15StatInvUasPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatInvUasPortn=_Pm1001lhPerfTelecomClientCurrent15StatInvUasPortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,10),_Pm1001lhPerfTelecomClientCurrent15StatInvUasPortn_Type())
pm1001lhPerfTelecomClientCurrent15StatInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatInvUasPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent15StatUasValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent15StatUasValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent15StatUasValuePortn=_Pm1001lhPerfTelecomClientCurrent15StatUasValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,16,1,11),_Pm1001lhPerfTelecomClientCurrent15StatUasValuePortn_Type())
pm1001lhPerfTelecomClientCurrent15StatUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent15StatUasValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Table_Object=MibTable
pm1001lhPerfTelecomClientPast15StatHistoryPort1Table=_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Table_Object((1,3,6,1,4,1,20044,10,12,2,24))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryPort1Table.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry_Object=MibTableRow
pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry=_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry_Object((1,3,6,1,4,1,20044,10,12,2,24,1))
pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry.setStatus(_A)
class _Pm1001lhPerfTelecomClientPast15StatHistoryPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Index_Type.__name__=_E
_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Index_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryPort1Index=_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Index_Object((1,3,6,1,4,1,20044,10,12,2,24,1,1),_Pm1001lhPerfTelecomClientPast15StatHistoryPort1Index_Type())
pm1001lhPerfTelecomClientPast15StatHistoryPort1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryPort1Index.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1=_Pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,2),_Pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1=_Pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,3),_Pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1=_Pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,4),_Pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1=_Pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,5),_Pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1=_Pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,6),_Pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1=_Pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,7),_Pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1_Type())
pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1=_Pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,8),_Pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1=_Pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,9),_Pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1_Type())
pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1=_Pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,10),_Pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1=_Pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,24,1,11),_Pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1_Type())
pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatTable_Object=MibTable
pm1001lhPerfTelecomClientCurrent24StatTable=_Pm1001lhPerfTelecomClientCurrent24StatTable_Object((1,3,6,1,4,1,20044,10,12,2,32))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatTable.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatEntry_Object=MibTableRow
pm1001lhPerfTelecomClientCurrent24StatEntry=_Pm1001lhPerfTelecomClientCurrent24StatEntry_Object((1,3,6,1,4,1,20044,10,12,2,32,1))
pm1001lhPerfTelecomClientCurrent24StatEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatEntry.setStatus(_A)
class _Pm1001lhPerfTelecomClientCurrent24StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomClientCurrent24StatIndex_Type.__name__=_E
_Pm1001lhPerfTelecomClientCurrent24StatIndex_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatIndex=_Pm1001lhPerfTelecomClientCurrent24StatIndex_Object((1,3,6,1,4,1,20044,10,12,2,32,1,1),_Pm1001lhPerfTelecomClientCurrent24StatIndex_Type())
pm1001lhPerfTelecomClientCurrent24StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatIndex.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatInvCvPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent24StatInvCvPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatInvCvPortn=_Pm1001lhPerfTelecomClientCurrent24StatInvCvPortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,2),_Pm1001lhPerfTelecomClientCurrent24StatInvCvPortn_Type())
pm1001lhPerfTelecomClientCurrent24StatInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatInvCvPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatCvValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent24StatCvValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatCvValuePortn=_Pm1001lhPerfTelecomClientCurrent24StatCvValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,3),_Pm1001lhPerfTelecomClientCurrent24StatCvValuePortn_Type())
pm1001lhPerfTelecomClientCurrent24StatCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatCvValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatInvEsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent24StatInvEsPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatInvEsPortn=_Pm1001lhPerfTelecomClientCurrent24StatInvEsPortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,4),_Pm1001lhPerfTelecomClientCurrent24StatInvEsPortn_Type())
pm1001lhPerfTelecomClientCurrent24StatInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatInvEsPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatEsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent24StatEsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatEsValuePortn=_Pm1001lhPerfTelecomClientCurrent24StatEsValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,5),_Pm1001lhPerfTelecomClientCurrent24StatEsValuePortn_Type())
pm1001lhPerfTelecomClientCurrent24StatEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatEsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatInvSesPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent24StatInvSesPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatInvSesPortn=_Pm1001lhPerfTelecomClientCurrent24StatInvSesPortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,6),_Pm1001lhPerfTelecomClientCurrent24StatInvSesPortn_Type())
pm1001lhPerfTelecomClientCurrent24StatInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatInvSesPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatSesValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent24StatSesValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatSesValuePortn=_Pm1001lhPerfTelecomClientCurrent24StatSesValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,7),_Pm1001lhPerfTelecomClientCurrent24StatSesValuePortn_Type())
pm1001lhPerfTelecomClientCurrent24StatSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatSesValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn=_Pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,8),_Pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn_Type())
pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn=_Pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,9),_Pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn_Type())
pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatInvUasPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomClientCurrent24StatInvUasPortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatInvUasPortn=_Pm1001lhPerfTelecomClientCurrent24StatInvUasPortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,10),_Pm1001lhPerfTelecomClientCurrent24StatInvUasPortn_Type())
pm1001lhPerfTelecomClientCurrent24StatInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatInvUasPortn.setStatus(_A)
_Pm1001lhPerfTelecomClientCurrent24StatUasValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomClientCurrent24StatUasValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomClientCurrent24StatUasValuePortn=_Pm1001lhPerfTelecomClientCurrent24StatUasValuePortn_Object((1,3,6,1,4,1,20044,10,12,2,32,1,11),_Pm1001lhPerfTelecomClientCurrent24StatUasValuePortn_Type())
pm1001lhPerfTelecomClientCurrent24StatUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientCurrent24StatUasValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Table_Object=MibTable
pm1001lhPerfTelecomClientPast24StatHistoryPort1Table=_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Table_Object((1,3,6,1,4,1,20044,10,12,2,40))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryPort1Table.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry_Object=MibTableRow
pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry=_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry_Object((1,3,6,1,4,1,20044,10,12,2,40,1))
pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry.setStatus(_A)
class _Pm1001lhPerfTelecomClientPast24StatHistoryPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Index_Type.__name__=_E
_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Index_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryPort1Index=_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Index_Object((1,3,6,1,4,1,20044,10,12,2,40,1,1),_Pm1001lhPerfTelecomClientPast24StatHistoryPort1Index_Type())
pm1001lhPerfTelecomClientPast24StatHistoryPort1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryPort1Index.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1=_Pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,2),_Pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1=_Pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,3),_Pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1=_Pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,4),_Pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1=_Pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,5),_Pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1=_Pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,6),_Pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1=_Pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,7),_Pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1_Type())
pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1=_Pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,8),_Pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1=_Pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,9),_Pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1_Type())
pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1=_Pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,10),_Pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1.setStatus(_A)
_Pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1=_Pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1_Object((1,3,6,1,4,1,20044,10,12,2,40,1,11),_Pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1_Type())
pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1.setStatus(_A)
_Pm1001lhPerfDatacomClientCurrent15StatTable_Object=MibTable
pm1001lhPerfDatacomClientCurrent15StatTable=_Pm1001lhPerfDatacomClientCurrent15StatTable_Object((1,3,6,1,4,1,20044,10,12,2,256))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientCurrent15StatTable.setStatus(_A)
_Pm1001lhPerfDatacomClientCurrent15StatEntry_Object=MibTableRow
pm1001lhPerfDatacomClientCurrent15StatEntry=_Pm1001lhPerfDatacomClientCurrent15StatEntry_Object((1,3,6,1,4,1,20044,10,12,2,256,1))
pm1001lhPerfDatacomClientCurrent15StatEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientCurrent15StatEntry.setStatus(_A)
class _Pm1001lhPerfDatacomClientCurrent15StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfDatacomClientCurrent15StatIndex_Type.__name__=_E
_Pm1001lhPerfDatacomClientCurrent15StatIndex_Object=MibTableColumn
pm1001lhPerfDatacomClientCurrent15StatIndex=_Pm1001lhPerfDatacomClientCurrent15StatIndex_Object((1,3,6,1,4,1,20044,10,12,2,256,1,1),_Pm1001lhPerfDatacomClientCurrent15StatIndex_Type())
pm1001lhPerfDatacomClientCurrent15StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientCurrent15StatIndex.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,2),_Pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn=_Pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,3),_Pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,4),_Pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn=_Pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,5),_Pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,8),_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,9),_Pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,10),_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,11),_Pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,20),_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,21),_Pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,22),_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,23),_Pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,26),_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn=_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,27),_Pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,32),_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,33),_Pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,34),_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,35),_Pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,42),_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,43),_Pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,44),_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn=_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,256,1,45),_Pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn.setStatus(_A)
_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Table_Object=MibTable
pm1001lhPerfDatacomClientPast15StatHistoryPort1Table=_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Table_Object((1,3,6,1,4,1,20044,10,12,2,264))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientPast15StatHistoryPort1Table.setStatus(_A)
_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry_Object=MibTableRow
pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry=_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry_Object((1,3,6,1,4,1,20044,10,12,2,264,1))
pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry.setStatus(_A)
class _Pm1001lhPerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Index_Type.__name__=_E
_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Index_Object=MibTableColumn
pm1001lhPerfDatacomClientPast15StatHistoryPort1Index=_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Index_Object((1,3,6,1,4,1,20044,10,12,2,264,1,1),_Pm1001lhPerfDatacomClientPast15StatHistoryPort1Index_Type())
pm1001lhPerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientPast15StatHistoryPort1Index.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1=_Pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,2),_Pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInBytesCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatInBytesCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInBytesCountPort1=_Pm1001lhperfdatacomclientPast15StatInBytesCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,3),_Pm1001lhperfdatacomclientPast15StatInBytesCountPort1_Type())
pm1001lhperfdatacomclientPast15StatInBytesCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInBytesCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1=_Pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,4),_Pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInCrcCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatInCrcCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInCrcCountPort1=_Pm1001lhperfdatacomclientPast15StatInCrcCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,5),_Pm1001lhperfdatacomclientPast15StatInCrcCountPort1_Type())
pm1001lhperfdatacomclientPast15StatInCrcCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInCrcCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,8),_Pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1=_Pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,9),_Pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,10),_Pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInMulticastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatInMulticastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInMulticastCountPort1=_Pm1001lhperfdatacomclientPast15StatInMulticastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,11),_Pm1001lhperfdatacomclientPast15StatInMulticastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatInMulticastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInMulticastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,20),_Pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInUnicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatInUnicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInUnicastCountPort1=_Pm1001lhperfdatacomclientPast15StatInUnicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,21),_Pm1001lhperfdatacomclientPast15StatInUnicastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatInUnicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInUnicastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,22),_Pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1=_Pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,23),_Pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1=_Pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,26),_Pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutBytesCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatOutBytesCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutBytesCountPort1=_Pm1001lhperfdatacomclientPast15StatOutBytesCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,27),_Pm1001lhperfdatacomclientPast15StatOutBytesCountPort1_Type())
pm1001lhperfdatacomclientPast15StatOutBytesCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutBytesCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,32),_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1=_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,33),_Pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,34),_Pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1=_Pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,35),_Pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,42),_Pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1=_Pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,43),_Pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1=_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,44),_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1=_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,264,1,45),_Pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1_Type())
pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1.setStatus(_A)
_Pm1001lhPerfDatacomClientCurrent24StatTable_Object=MibTable
pm1001lhPerfDatacomClientCurrent24StatTable=_Pm1001lhPerfDatacomClientCurrent24StatTable_Object((1,3,6,1,4,1,20044,10,12,2,272))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientCurrent24StatTable.setStatus(_A)
_Pm1001lhPerfDatacomClientCurrent24StatEntry_Object=MibTableRow
pm1001lhPerfDatacomClientCurrent24StatEntry=_Pm1001lhPerfDatacomClientCurrent24StatEntry_Object((1,3,6,1,4,1,20044,10,12,2,272,1))
pm1001lhPerfDatacomClientCurrent24StatEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientCurrent24StatEntry.setStatus(_A)
class _Pm1001lhPerfDatacomClientCurrent24StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfDatacomClientCurrent24StatIndex_Type.__name__=_E
_Pm1001lhPerfDatacomClientCurrent24StatIndex_Object=MibTableColumn
pm1001lhPerfDatacomClientCurrent24StatIndex=_Pm1001lhPerfDatacomClientCurrent24StatIndex_Object((1,3,6,1,4,1,20044,10,12,2,272,1,1),_Pm1001lhPerfDatacomClientCurrent24StatIndex_Type())
pm1001lhPerfDatacomClientCurrent24StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientCurrent24StatIndex.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,2),_Pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn=_Pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,3),_Pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,4),_Pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn=_Pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,5),_Pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,8),_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,9),_Pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,10),_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,11),_Pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,20),_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,21),_Pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,22),_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,23),_Pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,26),_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn=_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,27),_Pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,32),_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,33),_Pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,34),_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,35),_Pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,42),_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,43),_Pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type=EkiOnOff
_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn=_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,44),_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setStatus(_A)
_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn_Type=Counter64
_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn_Object=MibTableColumn
pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn=_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn_Object((1,3,6,1,4,1,20044,10,12,2,272,1,45),_Pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn_Type())
pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn.setStatus(_A)
_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Table_Object=MibTable
pm1001lhPerfDatacomClientPast24StatHistoryPort1Table=_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Table_Object((1,3,6,1,4,1,20044,10,12,2,280))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientPast24StatHistoryPort1Table.setStatus(_A)
_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry_Object=MibTableRow
pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry=_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry_Object((1,3,6,1,4,1,20044,10,12,2,280,1))
pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry.setStatus(_A)
class _Pm1001lhPerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Index_Type.__name__=_E
_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Index_Object=MibTableColumn
pm1001lhPerfDatacomClientPast24StatHistoryPort1Index=_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Index_Object((1,3,6,1,4,1,20044,10,12,2,280,1,1),_Pm1001lhPerfDatacomClientPast24StatHistoryPort1Index_Type())
pm1001lhPerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfDatacomClientPast24StatHistoryPort1Index.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1=_Pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,2),_Pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInBytesCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatInBytesCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInBytesCountPort1=_Pm1001lhperfdatacomclientPast24StatInBytesCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,3),_Pm1001lhperfdatacomclientPast24StatInBytesCountPort1_Type())
pm1001lhperfdatacomclientPast24StatInBytesCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInBytesCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1=_Pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,4),_Pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInCrcCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatInCrcCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInCrcCountPort1=_Pm1001lhperfdatacomclientPast24StatInCrcCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,5),_Pm1001lhperfdatacomclientPast24StatInCrcCountPort1_Type())
pm1001lhperfdatacomclientPast24StatInCrcCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInCrcCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,8),_Pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1=_Pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,9),_Pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,10),_Pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInMulticastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatInMulticastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInMulticastCountPort1=_Pm1001lhperfdatacomclientPast24StatInMulticastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,11),_Pm1001lhperfdatacomclientPast24StatInMulticastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatInMulticastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInMulticastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,20),_Pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInUnicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatInUnicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInUnicastCountPort1=_Pm1001lhperfdatacomclientPast24StatInUnicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,21),_Pm1001lhperfdatacomclientPast24StatInUnicastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatInUnicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInUnicastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,22),_Pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1=_Pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,23),_Pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1=_Pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,26),_Pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutBytesCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatOutBytesCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutBytesCountPort1=_Pm1001lhperfdatacomclientPast24StatOutBytesCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,27),_Pm1001lhperfdatacomclientPast24StatOutBytesCountPort1_Type())
pm1001lhperfdatacomclientPast24StatOutBytesCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutBytesCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,32),_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1=_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,33),_Pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,34),_Pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1=_Pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,35),_Pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,42),_Pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1=_Pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,43),_Pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1_Type=EkiOnOff
_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1=_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,44),_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1_Type())
pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1.setStatus(_A)
_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1_Type=Counter64
_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1_Object=MibTableColumn
pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1=_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1_Object((1,3,6,1,4,1,20044,10,12,2,280,1,45),_Pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1_Type())
pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1.setStatus(_A)
_Pm1001lhMonLine_ObjectIdentity=ObjectIdentity
pm1001lhMonLine=_Pm1001lhMonLine_ObjectIdentity((1,3,6,1,4,1,20044,10,12,3))
_Pm1001lhPerfTelecomLineCurrent15StatTable_Object=MibTable
pm1001lhPerfTelecomLineCurrent15StatTable=_Pm1001lhPerfTelecomLineCurrent15StatTable_Object((1,3,6,1,4,1,20044,10,12,3,128))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatTable.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatEntry_Object=MibTableRow
pm1001lhPerfTelecomLineCurrent15StatEntry=_Pm1001lhPerfTelecomLineCurrent15StatEntry_Object((1,3,6,1,4,1,20044,10,12,3,128,1))
pm1001lhPerfTelecomLineCurrent15StatEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatEntry.setStatus(_A)
class _Pm1001lhPerfTelecomLineCurrent15StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomLineCurrent15StatIndex_Type.__name__=_E
_Pm1001lhPerfTelecomLineCurrent15StatIndex_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatIndex=_Pm1001lhPerfTelecomLineCurrent15StatIndex_Object((1,3,6,1,4,1,20044,10,12,3,128,1,1),_Pm1001lhPerfTelecomLineCurrent15StatIndex_Type())
pm1001lhPerfTelecomLineCurrent15StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatIndex.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatInvCvPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent15StatInvCvPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatInvCvPortn=_Pm1001lhPerfTelecomLineCurrent15StatInvCvPortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,2),_Pm1001lhPerfTelecomLineCurrent15StatInvCvPortn_Type())
pm1001lhPerfTelecomLineCurrent15StatInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatInvCvPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatCvValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent15StatCvValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatCvValuePortn=_Pm1001lhPerfTelecomLineCurrent15StatCvValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,3),_Pm1001lhPerfTelecomLineCurrent15StatCvValuePortn_Type())
pm1001lhPerfTelecomLineCurrent15StatCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatCvValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatInvEsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent15StatInvEsPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatInvEsPortn=_Pm1001lhPerfTelecomLineCurrent15StatInvEsPortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,4),_Pm1001lhPerfTelecomLineCurrent15StatInvEsPortn_Type())
pm1001lhPerfTelecomLineCurrent15StatInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatInvEsPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatEsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent15StatEsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatEsValuePortn=_Pm1001lhPerfTelecomLineCurrent15StatEsValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,5),_Pm1001lhPerfTelecomLineCurrent15StatEsValuePortn_Type())
pm1001lhPerfTelecomLineCurrent15StatEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatEsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatInvSesPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent15StatInvSesPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatInvSesPortn=_Pm1001lhPerfTelecomLineCurrent15StatInvSesPortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,6),_Pm1001lhPerfTelecomLineCurrent15StatInvSesPortn_Type())
pm1001lhPerfTelecomLineCurrent15StatInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatInvSesPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatSesValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent15StatSesValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatSesValuePortn=_Pm1001lhPerfTelecomLineCurrent15StatSesValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,7),_Pm1001lhPerfTelecomLineCurrent15StatSesValuePortn_Type())
pm1001lhPerfTelecomLineCurrent15StatSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatSesValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn=_Pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,8),_Pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn_Type())
pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn=_Pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,9),_Pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn_Type())
pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatInvUasPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent15StatInvUasPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatInvUasPortn=_Pm1001lhPerfTelecomLineCurrent15StatInvUasPortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,10),_Pm1001lhPerfTelecomLineCurrent15StatInvUasPortn_Type())
pm1001lhPerfTelecomLineCurrent15StatInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatInvUasPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent15StatUasValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent15StatUasValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent15StatUasValuePortn=_Pm1001lhPerfTelecomLineCurrent15StatUasValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,128,1,11),_Pm1001lhPerfTelecomLineCurrent15StatUasValuePortn_Type())
pm1001lhPerfTelecomLineCurrent15StatUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent15StatUasValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Table_Object=MibTable
pm1001lhPerfTelecomLinePast15StatHistoryPort1Table=_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Table_Object((1,3,6,1,4,1,20044,10,12,3,129))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryPort1Table.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry_Object=MibTableRow
pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry=_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry_Object((1,3,6,1,4,1,20044,10,12,3,129,1))
pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry.setStatus(_A)
class _Pm1001lhPerfTelecomLinePast15StatHistoryPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Index_Type.__name__=_E
_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Index_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryPort1Index=_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Index_Object((1,3,6,1,4,1,20044,10,12,3,129,1,1),_Pm1001lhPerfTelecomLinePast15StatHistoryPort1Index_Type())
pm1001lhPerfTelecomLinePast15StatHistoryPort1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryPort1Index.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1=_Pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,2),_Pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1=_Pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,3),_Pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1=_Pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,4),_Pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1=_Pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,5),_Pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1=_Pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,6),_Pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1=_Pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,7),_Pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1_Type())
pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1=_Pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,8),_Pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1=_Pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,9),_Pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1_Type())
pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1=_Pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,10),_Pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1=_Pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,129,1,11),_Pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1_Type())
pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatTable_Object=MibTable
pm1001lhPerfTelecomLineCurrent24StatTable=_Pm1001lhPerfTelecomLineCurrent24StatTable_Object((1,3,6,1,4,1,20044,10,12,3,130))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatTable.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatEntry_Object=MibTableRow
pm1001lhPerfTelecomLineCurrent24StatEntry=_Pm1001lhPerfTelecomLineCurrent24StatEntry_Object((1,3,6,1,4,1,20044,10,12,3,130,1))
pm1001lhPerfTelecomLineCurrent24StatEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatEntry.setStatus(_A)
class _Pm1001lhPerfTelecomLineCurrent24StatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomLineCurrent24StatIndex_Type.__name__=_E
_Pm1001lhPerfTelecomLineCurrent24StatIndex_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatIndex=_Pm1001lhPerfTelecomLineCurrent24StatIndex_Object((1,3,6,1,4,1,20044,10,12,3,130,1,1),_Pm1001lhPerfTelecomLineCurrent24StatIndex_Type())
pm1001lhPerfTelecomLineCurrent24StatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatIndex.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatInvCvPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent24StatInvCvPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatInvCvPortn=_Pm1001lhPerfTelecomLineCurrent24StatInvCvPortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,2),_Pm1001lhPerfTelecomLineCurrent24StatInvCvPortn_Type())
pm1001lhPerfTelecomLineCurrent24StatInvCvPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatInvCvPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatCvValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent24StatCvValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatCvValuePortn=_Pm1001lhPerfTelecomLineCurrent24StatCvValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,3),_Pm1001lhPerfTelecomLineCurrent24StatCvValuePortn_Type())
pm1001lhPerfTelecomLineCurrent24StatCvValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatCvValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatInvEsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent24StatInvEsPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatInvEsPortn=_Pm1001lhPerfTelecomLineCurrent24StatInvEsPortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,4),_Pm1001lhPerfTelecomLineCurrent24StatInvEsPortn_Type())
pm1001lhPerfTelecomLineCurrent24StatInvEsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatInvEsPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatEsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent24StatEsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatEsValuePortn=_Pm1001lhPerfTelecomLineCurrent24StatEsValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,5),_Pm1001lhPerfTelecomLineCurrent24StatEsValuePortn_Type())
pm1001lhPerfTelecomLineCurrent24StatEsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatEsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatInvSesPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent24StatInvSesPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatInvSesPortn=_Pm1001lhPerfTelecomLineCurrent24StatInvSesPortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,6),_Pm1001lhPerfTelecomLineCurrent24StatInvSesPortn_Type())
pm1001lhPerfTelecomLineCurrent24StatInvSesPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatInvSesPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatSesValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent24StatSesValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatSesValuePortn=_Pm1001lhPerfTelecomLineCurrent24StatSesValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,7),_Pm1001lhPerfTelecomLineCurrent24StatSesValuePortn_Type())
pm1001lhPerfTelecomLineCurrent24StatSesValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatSesValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn=_Pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,8),_Pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn_Type())
pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn=_Pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,9),_Pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn_Type())
pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatInvUasPortn_Type=EkiOnOff
_Pm1001lhPerfTelecomLineCurrent24StatInvUasPortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatInvUasPortn=_Pm1001lhPerfTelecomLineCurrent24StatInvUasPortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,10),_Pm1001lhPerfTelecomLineCurrent24StatInvUasPortn_Type())
pm1001lhPerfTelecomLineCurrent24StatInvUasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatInvUasPortn.setStatus(_A)
_Pm1001lhPerfTelecomLineCurrent24StatUasValuePortn_Type=Unsigned32
_Pm1001lhPerfTelecomLineCurrent24StatUasValuePortn_Object=MibTableColumn
pm1001lhPerfTelecomLineCurrent24StatUasValuePortn=_Pm1001lhPerfTelecomLineCurrent24StatUasValuePortn_Object((1,3,6,1,4,1,20044,10,12,3,130,1,11),_Pm1001lhPerfTelecomLineCurrent24StatUasValuePortn_Type())
pm1001lhPerfTelecomLineCurrent24StatUasValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLineCurrent24StatUasValuePortn.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Table_Object=MibTable
pm1001lhPerfTelecomLinePast24StatHistoryPort1Table=_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Table_Object((1,3,6,1,4,1,20044,10,12,3,131))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryPort1Table.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry_Object=MibTableRow
pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry=_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry_Object((1,3,6,1,4,1,20044,10,12,3,131,1))
pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry.setStatus(_A)
class _Pm1001lhPerfTelecomLinePast24StatHistoryPort1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Index_Type.__name__=_E
_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Index_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryPort1Index=_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Index_Object((1,3,6,1,4,1,20044,10,12,3,131,1,1),_Pm1001lhPerfTelecomLinePast24StatHistoryPort1Index_Type())
pm1001lhPerfTelecomLinePast24StatHistoryPort1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryPort1Index.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1=_Pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,2),_Pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1=_Pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,3),_Pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1=_Pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,4),_Pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1=_Pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,5),_Pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1=_Pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,6),_Pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1=_Pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,7),_Pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1_Type())
pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1=_Pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,8),_Pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1=_Pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,9),_Pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1_Type())
pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1_Type=EkiOnOff
_Pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1=_Pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,10),_Pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1.setStatus(_A)
_Pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1_Type=Unsigned32
_Pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1_Object=MibTableColumn
pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1=_Pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1_Object((1,3,6,1,4,1,20044,10,12,3,131,1,11),_Pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1_Type())
pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1.setStatus(_A)
_Pm1001lhRmon_ObjectIdentity=ObjectIdentity
pm1001lhRmon=_Pm1001lhRmon_ObjectIdentity((1,3,6,1,4,1,20044,10,12,4))
_Pm1001lhRmonClient_ObjectIdentity=ObjectIdentity
pm1001lhRmonClient=_Pm1001lhRmonClient_ObjectIdentity((1,3,6,1,4,1,20044,10,12,4,1))
_Pm1001lhMonupRmonByteCntTable_Object=MibTable
pm1001lhMonupRmonByteCntTable=_Pm1001lhMonupRmonByteCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,16))
if mibBuilder.loadTexts:pm1001lhMonupRmonByteCntTable.setStatus(_A)
_Pm1001lhMonupRmonByteCntEntry_Object=MibTableRow
pm1001lhMonupRmonByteCntEntry=_Pm1001lhMonupRmonByteCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,16,1))
pm1001lhMonupRmonByteCntEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pm1001lhMonupRmonByteCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonByteCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonByteCntIndex_Object=MibTableColumn
pm1001lhMonupRmonByteCntIndex=_Pm1001lhMonupRmonByteCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,16,1,1),_Pm1001lhMonupRmonByteCntIndex_Type())
pm1001lhMonupRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonByteCntIndex.setStatus(_A)
_Pm1001lhMonupRmonByteCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonByteCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonByteCntValuePortn=_Pm1001lhMonupRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,16,1,2),_Pm1001lhMonupRmonByteCntValuePortn_Type())
pm1001lhMonupRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonByteCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonByteCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonByteCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonByteCntErrorPortn=_Pm1001lhMonupRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,16,1,3),_Pm1001lhMonupRmonByteCntErrorPortn_Type())
pm1001lhMonupRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonByteCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonByteCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonByteCntOverloadPortn=_Pm1001lhMonupRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,16,1,4),_Pm1001lhMonupRmonByteCntOverloadPortn_Type())
pm1001lhMonupRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonByteCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonCrcErrorCntTable_Object=MibTable
pm1001lhMonupRmonCrcErrorCntTable=_Pm1001lhMonupRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,24))
if mibBuilder.loadTexts:pm1001lhMonupRmonCrcErrorCntTable.setStatus(_A)
_Pm1001lhMonupRmonCrcErrorCntEntry_Object=MibTableRow
pm1001lhMonupRmonCrcErrorCntEntry=_Pm1001lhMonupRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,24,1))
pm1001lhMonupRmonCrcErrorCntEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pm1001lhMonupRmonCrcErrorCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonCrcErrorCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonCrcErrorCntIndex_Object=MibTableColumn
pm1001lhMonupRmonCrcErrorCntIndex=_Pm1001lhMonupRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,24,1,1),_Pm1001lhMonupRmonCrcErrorCntIndex_Type())
pm1001lhMonupRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonCrcErrorCntIndex.setStatus(_A)
_Pm1001lhMonupRmonCrcErrorCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonCrcErrorCntValuePortn=_Pm1001lhMonupRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,24,1,2),_Pm1001lhMonupRmonCrcErrorCntValuePortn_Type())
pm1001lhMonupRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonCrcErrorCntErrorPortn=_Pm1001lhMonupRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,24,1,3),_Pm1001lhMonupRmonCrcErrorCntErrorPortn_Type())
pm1001lhMonupRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonCrcErrorCntOverloadPortn=_Pm1001lhMonupRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,24,1,4),_Pm1001lhMonupRmonCrcErrorCntOverloadPortn_Type())
pm1001lhMonupRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonPacketsCntTable_Object=MibTable
pm1001lhMonupRmonPacketsCntTable=_Pm1001lhMonupRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,32))
if mibBuilder.loadTexts:pm1001lhMonupRmonPacketsCntTable.setStatus(_A)
_Pm1001lhMonupRmonPacketsCntEntry_Object=MibTableRow
pm1001lhMonupRmonPacketsCntEntry=_Pm1001lhMonupRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,32,1))
pm1001lhMonupRmonPacketsCntEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pm1001lhMonupRmonPacketsCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonPacketsCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonPacketsCntIndex_Object=MibTableColumn
pm1001lhMonupRmonPacketsCntIndex=_Pm1001lhMonupRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,32,1,1),_Pm1001lhMonupRmonPacketsCntIndex_Type())
pm1001lhMonupRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPacketsCntIndex.setStatus(_A)
_Pm1001lhMonupRmonPacketsCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonPacketsCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonPacketsCntValuePortn=_Pm1001lhMonupRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,32,1,2),_Pm1001lhMonupRmonPacketsCntValuePortn_Type())
pm1001lhMonupRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPacketsCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonPacketsCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonPacketsCntErrorPortn=_Pm1001lhMonupRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,32,1,3),_Pm1001lhMonupRmonPacketsCntErrorPortn_Type())
pm1001lhMonupRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPacketsCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonPacketsCntOverloadPortn=_Pm1001lhMonupRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,32,1,4),_Pm1001lhMonupRmonPacketsCntOverloadPortn_Type())
pm1001lhMonupRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonBroadcastCntTable_Object=MibTable
pm1001lhMonupRmonBroadcastCntTable=_Pm1001lhMonupRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,40))
if mibBuilder.loadTexts:pm1001lhMonupRmonBroadcastCntTable.setStatus(_A)
_Pm1001lhMonupRmonBroadcastCntEntry_Object=MibTableRow
pm1001lhMonupRmonBroadcastCntEntry=_Pm1001lhMonupRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,40,1))
pm1001lhMonupRmonBroadcastCntEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pm1001lhMonupRmonBroadcastCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonBroadcastCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonBroadcastCntIndex_Object=MibTableColumn
pm1001lhMonupRmonBroadcastCntIndex=_Pm1001lhMonupRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,40,1,1),_Pm1001lhMonupRmonBroadcastCntIndex_Type())
pm1001lhMonupRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBroadcastCntIndex.setStatus(_A)
_Pm1001lhMonupRmonBroadcastCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonBroadcastCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonBroadcastCntValuePortn=_Pm1001lhMonupRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,40,1,2),_Pm1001lhMonupRmonBroadcastCntValuePortn_Type())
pm1001lhMonupRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBroadcastCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonBroadcastCntErrorPortn=_Pm1001lhMonupRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,40,1,3),_Pm1001lhMonupRmonBroadcastCntErrorPortn_Type())
pm1001lhMonupRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonBroadcastCntOverloadPortn=_Pm1001lhMonupRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,40,1,4),_Pm1001lhMonupRmonBroadcastCntOverloadPortn_Type())
pm1001lhMonupRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonMulticastCntTable_Object=MibTable
pm1001lhMonupRmonMulticastCntTable=_Pm1001lhMonupRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,48))
if mibBuilder.loadTexts:pm1001lhMonupRmonMulticastCntTable.setStatus(_A)
_Pm1001lhMonupRmonMulticastCntEntry_Object=MibTableRow
pm1001lhMonupRmonMulticastCntEntry=_Pm1001lhMonupRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,48,1))
pm1001lhMonupRmonMulticastCntEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pm1001lhMonupRmonMulticastCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonMulticastCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonMulticastCntIndex_Object=MibTableColumn
pm1001lhMonupRmonMulticastCntIndex=_Pm1001lhMonupRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,48,1,1),_Pm1001lhMonupRmonMulticastCntIndex_Type())
pm1001lhMonupRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonMulticastCntIndex.setStatus(_A)
_Pm1001lhMonupRmonMulticastCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonMulticastCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonMulticastCntValuePortn=_Pm1001lhMonupRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,48,1,2),_Pm1001lhMonupRmonMulticastCntValuePortn_Type())
pm1001lhMonupRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonMulticastCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonMulticastCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonMulticastCntErrorPortn=_Pm1001lhMonupRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,48,1,3),_Pm1001lhMonupRmonMulticastCntErrorPortn_Type())
pm1001lhMonupRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonMulticastCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonMulticastCntOverloadPortn=_Pm1001lhMonupRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,48,1,4),_Pm1001lhMonupRmonMulticastCntOverloadPortn_Type())
pm1001lhMonupRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonMulticastCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonTimerCntTable_Object=MibTable
pm1001lhMonupRmonTimerCntTable=_Pm1001lhMonupRmonTimerCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,56))
if mibBuilder.loadTexts:pm1001lhMonupRmonTimerCntTable.setStatus(_A)
_Pm1001lhMonupRmonTimerCntEntry_Object=MibTableRow
pm1001lhMonupRmonTimerCntEntry=_Pm1001lhMonupRmonTimerCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,56,1))
pm1001lhMonupRmonTimerCntEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pm1001lhMonupRmonTimerCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonTimerCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonTimerCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonTimerCntIndex_Object=MibTableColumn
pm1001lhMonupRmonTimerCntIndex=_Pm1001lhMonupRmonTimerCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,56,1,1),_Pm1001lhMonupRmonTimerCntIndex_Type())
pm1001lhMonupRmonTimerCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonTimerCntIndex.setStatus(_A)
_Pm1001lhMonupRmonTimerCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonTimerCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonTimerCntValuePortn=_Pm1001lhMonupRmonTimerCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,56,1,2),_Pm1001lhMonupRmonTimerCntValuePortn_Type())
pm1001lhMonupRmonTimerCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonTimerCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonTimerCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonTimerCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonTimerCntErrorPortn=_Pm1001lhMonupRmonTimerCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,56,1,3),_Pm1001lhMonupRmonTimerCntErrorPortn_Type())
pm1001lhMonupRmonTimerCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonTimerCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonTimerCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonTimerCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonTimerCntOverloadPortn=_Pm1001lhMonupRmonTimerCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,56,1,4),_Pm1001lhMonupRmonTimerCntOverloadPortn_Type())
pm1001lhMonupRmonTimerCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonTimerCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonPauseFrameCntTable_Object=MibTable
pm1001lhMonupRmonPauseFrameCntTable=_Pm1001lhMonupRmonPauseFrameCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,64))
if mibBuilder.loadTexts:pm1001lhMonupRmonPauseFrameCntTable.setStatus(_A)
_Pm1001lhMonupRmonPauseFrameCntEntry_Object=MibTableRow
pm1001lhMonupRmonPauseFrameCntEntry=_Pm1001lhMonupRmonPauseFrameCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,64,1))
pm1001lhMonupRmonPauseFrameCntEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pm1001lhMonupRmonPauseFrameCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonPauseFrameCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonPauseFrameCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonPauseFrameCntIndex_Object=MibTableColumn
pm1001lhMonupRmonPauseFrameCntIndex=_Pm1001lhMonupRmonPauseFrameCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,64,1,1),_Pm1001lhMonupRmonPauseFrameCntIndex_Type())
pm1001lhMonupRmonPauseFrameCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPauseFrameCntIndex.setStatus(_A)
_Pm1001lhMonupRmonPauseFrameCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonPauseFrameCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonPauseFrameCntValuePortn=_Pm1001lhMonupRmonPauseFrameCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,64,1,2),_Pm1001lhMonupRmonPauseFrameCntValuePortn_Type())
pm1001lhMonupRmonPauseFrameCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPauseFrameCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonPauseFrameCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonPauseFrameCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonPauseFrameCntErrorPortn=_Pm1001lhMonupRmonPauseFrameCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,64,1,3),_Pm1001lhMonupRmonPauseFrameCntErrorPortn_Type())
pm1001lhMonupRmonPauseFrameCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPauseFrameCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonPauseFrameCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonPauseFrameCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonPauseFrameCntOverloadPortn=_Pm1001lhMonupRmonPauseFrameCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,64,1,4),_Pm1001lhMonupRmonPauseFrameCntOverloadPortn_Type())
pm1001lhMonupRmonPauseFrameCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonPauseFrameCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonDropFrameCntTable_Object=MibTable
pm1001lhMonupRmonDropFrameCntTable=_Pm1001lhMonupRmonDropFrameCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,72))
if mibBuilder.loadTexts:pm1001lhMonupRmonDropFrameCntTable.setStatus(_A)
_Pm1001lhMonupRmonDropFrameCntEntry_Object=MibTableRow
pm1001lhMonupRmonDropFrameCntEntry=_Pm1001lhMonupRmonDropFrameCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,72,1))
pm1001lhMonupRmonDropFrameCntEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pm1001lhMonupRmonDropFrameCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonDropFrameCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonDropFrameCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonDropFrameCntIndex_Object=MibTableColumn
pm1001lhMonupRmonDropFrameCntIndex=_Pm1001lhMonupRmonDropFrameCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,72,1,1),_Pm1001lhMonupRmonDropFrameCntIndex_Type())
pm1001lhMonupRmonDropFrameCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonDropFrameCntIndex.setStatus(_A)
_Pm1001lhMonupRmonDropFrameCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonDropFrameCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonDropFrameCntValuePortn=_Pm1001lhMonupRmonDropFrameCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,72,1,2),_Pm1001lhMonupRmonDropFrameCntValuePortn_Type())
pm1001lhMonupRmonDropFrameCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonDropFrameCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonDropFrameCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonDropFrameCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonDropFrameCntErrorPortn=_Pm1001lhMonupRmonDropFrameCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,72,1,3),_Pm1001lhMonupRmonDropFrameCntErrorPortn_Type())
pm1001lhMonupRmonDropFrameCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonDropFrameCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonDropFrameCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonDropFrameCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonDropFrameCntOverloadPortn=_Pm1001lhMonupRmonDropFrameCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,72,1,4),_Pm1001lhMonupRmonDropFrameCntOverloadPortn_Type())
pm1001lhMonupRmonDropFrameCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonDropFrameCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonBitsCntTable_Object=MibTable
pm1001lhMonupRmonBitsCntTable=_Pm1001lhMonupRmonBitsCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,80))
if mibBuilder.loadTexts:pm1001lhMonupRmonBitsCntTable.setStatus(_A)
_Pm1001lhMonupRmonBitsCntEntry_Object=MibTableRow
pm1001lhMonupRmonBitsCntEntry=_Pm1001lhMonupRmonBitsCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,80,1))
pm1001lhMonupRmonBitsCntEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pm1001lhMonupRmonBitsCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonBitsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonBitsCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonBitsCntIndex_Object=MibTableColumn
pm1001lhMonupRmonBitsCntIndex=_Pm1001lhMonupRmonBitsCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,80,1,1),_Pm1001lhMonupRmonBitsCntIndex_Type())
pm1001lhMonupRmonBitsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBitsCntIndex.setStatus(_A)
_Pm1001lhMonupRmonBitsCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonBitsCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonBitsCntValuePortn=_Pm1001lhMonupRmonBitsCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,80,1,2),_Pm1001lhMonupRmonBitsCntValuePortn_Type())
pm1001lhMonupRmonBitsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBitsCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonBitsCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonBitsCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonBitsCntErrorPortn=_Pm1001lhMonupRmonBitsCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,80,1,3),_Pm1001lhMonupRmonBitsCntErrorPortn_Type())
pm1001lhMonupRmonBitsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBitsCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonBitsCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonBitsCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonBitsCntOverloadPortn=_Pm1001lhMonupRmonBitsCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,80,1,4),_Pm1001lhMonupRmonBitsCntOverloadPortn_Type())
pm1001lhMonupRmonBitsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonBitsCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonUnicastCntTable_Object=MibTable
pm1001lhMonupRmonUnicastCntTable=_Pm1001lhMonupRmonUnicastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,88))
if mibBuilder.loadTexts:pm1001lhMonupRmonUnicastCntTable.setStatus(_A)
_Pm1001lhMonupRmonUnicastCntEntry_Object=MibTableRow
pm1001lhMonupRmonUnicastCntEntry=_Pm1001lhMonupRmonUnicastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,88,1))
pm1001lhMonupRmonUnicastCntEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pm1001lhMonupRmonUnicastCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonUnicastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonUnicastCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonUnicastCntIndex_Object=MibTableColumn
pm1001lhMonupRmonUnicastCntIndex=_Pm1001lhMonupRmonUnicastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,88,1,1),_Pm1001lhMonupRmonUnicastCntIndex_Type())
pm1001lhMonupRmonUnicastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonUnicastCntIndex.setStatus(_A)
_Pm1001lhMonupRmonUnicastCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonUnicastCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonUnicastCntValuePortn=_Pm1001lhMonupRmonUnicastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,88,1,2),_Pm1001lhMonupRmonUnicastCntValuePortn_Type())
pm1001lhMonupRmonUnicastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonUnicastCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonUnicastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonUnicastCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonUnicastCntErrorPortn=_Pm1001lhMonupRmonUnicastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,88,1,3),_Pm1001lhMonupRmonUnicastCntErrorPortn_Type())
pm1001lhMonupRmonUnicastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonUnicastCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonUnicastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonUnicastCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonUnicastCntOverloadPortn=_Pm1001lhMonupRmonUnicastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,88,1,4),_Pm1001lhMonupRmonUnicastCntOverloadPortn_Type())
pm1001lhMonupRmonUnicastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonUnicastCntOverloadPortn.setStatus(_A)
_Pm1001lhMonupRmonNonUnicastCntTable_Object=MibTable
pm1001lhMonupRmonNonUnicastCntTable=_Pm1001lhMonupRmonNonUnicastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,96))
if mibBuilder.loadTexts:pm1001lhMonupRmonNonUnicastCntTable.setStatus(_A)
_Pm1001lhMonupRmonNonUnicastCntEntry_Object=MibTableRow
pm1001lhMonupRmonNonUnicastCntEntry=_Pm1001lhMonupRmonNonUnicastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,96,1))
pm1001lhMonupRmonNonUnicastCntEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pm1001lhMonupRmonNonUnicastCntEntry.setStatus(_A)
class _Pm1001lhMonupRmonNonUnicastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMonupRmonNonUnicastCntIndex_Type.__name__=_E
_Pm1001lhMonupRmonNonUnicastCntIndex_Object=MibTableColumn
pm1001lhMonupRmonNonUnicastCntIndex=_Pm1001lhMonupRmonNonUnicastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,96,1,1),_Pm1001lhMonupRmonNonUnicastCntIndex_Type())
pm1001lhMonupRmonNonUnicastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonNonUnicastCntIndex.setStatus(_A)
_Pm1001lhMonupRmonNonUnicastCntValuePortn_Type=Counter64
_Pm1001lhMonupRmonNonUnicastCntValuePortn_Object=MibTableColumn
pm1001lhMonupRmonNonUnicastCntValuePortn=_Pm1001lhMonupRmonNonUnicastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,96,1,2),_Pm1001lhMonupRmonNonUnicastCntValuePortn_Type())
pm1001lhMonupRmonNonUnicastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonNonUnicastCntValuePortn.setStatus(_A)
_Pm1001lhMonupRmonNonUnicastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMonupRmonNonUnicastCntErrorPortn_Object=MibTableColumn
pm1001lhMonupRmonNonUnicastCntErrorPortn=_Pm1001lhMonupRmonNonUnicastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,96,1,3),_Pm1001lhMonupRmonNonUnicastCntErrorPortn_Type())
pm1001lhMonupRmonNonUnicastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonNonUnicastCntErrorPortn.setStatus(_A)
_Pm1001lhMonupRmonNonUnicastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMonupRmonNonUnicastCntOverloadPortn_Object=MibTableColumn
pm1001lhMonupRmonNonUnicastCntOverloadPortn=_Pm1001lhMonupRmonNonUnicastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,96,1,4),_Pm1001lhMonupRmonNonUnicastCntOverloadPortn_Type())
pm1001lhMonupRmonNonUnicastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMonupRmonNonUnicastCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonByteCntTable_Object=MibTable
pm1001lhMondwRmonByteCntTable=_Pm1001lhMondwRmonByteCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,112))
if mibBuilder.loadTexts:pm1001lhMondwRmonByteCntTable.setStatus(_A)
_Pm1001lhMondwRmonByteCntEntry_Object=MibTableRow
pm1001lhMondwRmonByteCntEntry=_Pm1001lhMondwRmonByteCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,112,1))
pm1001lhMondwRmonByteCntEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pm1001lhMondwRmonByteCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonByteCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonByteCntIndex_Object=MibTableColumn
pm1001lhMondwRmonByteCntIndex=_Pm1001lhMondwRmonByteCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,112,1,1),_Pm1001lhMondwRmonByteCntIndex_Type())
pm1001lhMondwRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonByteCntIndex.setStatus(_A)
_Pm1001lhMondwRmonByteCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonByteCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonByteCntValuePortn=_Pm1001lhMondwRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,112,1,2),_Pm1001lhMondwRmonByteCntValuePortn_Type())
pm1001lhMondwRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonByteCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonByteCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonByteCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonByteCntErrorPortn=_Pm1001lhMondwRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,112,1,3),_Pm1001lhMondwRmonByteCntErrorPortn_Type())
pm1001lhMondwRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonByteCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonByteCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonByteCntOverloadPortn=_Pm1001lhMondwRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,112,1,4),_Pm1001lhMondwRmonByteCntOverloadPortn_Type())
pm1001lhMondwRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonByteCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonCrcErrorCntTable_Object=MibTable
pm1001lhMondwRmonCrcErrorCntTable=_Pm1001lhMondwRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,120))
if mibBuilder.loadTexts:pm1001lhMondwRmonCrcErrorCntTable.setStatus(_A)
_Pm1001lhMondwRmonCrcErrorCntEntry_Object=MibTableRow
pm1001lhMondwRmonCrcErrorCntEntry=_Pm1001lhMondwRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,120,1))
pm1001lhMondwRmonCrcErrorCntEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pm1001lhMondwRmonCrcErrorCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonCrcErrorCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonCrcErrorCntIndex_Object=MibTableColumn
pm1001lhMondwRmonCrcErrorCntIndex=_Pm1001lhMondwRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,120,1,1),_Pm1001lhMondwRmonCrcErrorCntIndex_Type())
pm1001lhMondwRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonCrcErrorCntIndex.setStatus(_A)
_Pm1001lhMondwRmonCrcErrorCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonCrcErrorCntValuePortn=_Pm1001lhMondwRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,120,1,2),_Pm1001lhMondwRmonCrcErrorCntValuePortn_Type())
pm1001lhMondwRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonCrcErrorCntErrorPortn=_Pm1001lhMondwRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,120,1,3),_Pm1001lhMondwRmonCrcErrorCntErrorPortn_Type())
pm1001lhMondwRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonCrcErrorCntOverloadPortn=_Pm1001lhMondwRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,120,1,4),_Pm1001lhMondwRmonCrcErrorCntOverloadPortn_Type())
pm1001lhMondwRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonPacketsCntTable_Object=MibTable
pm1001lhMondwRmonPacketsCntTable=_Pm1001lhMondwRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,128))
if mibBuilder.loadTexts:pm1001lhMondwRmonPacketsCntTable.setStatus(_A)
_Pm1001lhMondwRmonPacketsCntEntry_Object=MibTableRow
pm1001lhMondwRmonPacketsCntEntry=_Pm1001lhMondwRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,128,1))
pm1001lhMondwRmonPacketsCntEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pm1001lhMondwRmonPacketsCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonPacketsCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonPacketsCntIndex_Object=MibTableColumn
pm1001lhMondwRmonPacketsCntIndex=_Pm1001lhMondwRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,128,1,1),_Pm1001lhMondwRmonPacketsCntIndex_Type())
pm1001lhMondwRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPacketsCntIndex.setStatus(_A)
_Pm1001lhMondwRmonPacketsCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonPacketsCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonPacketsCntValuePortn=_Pm1001lhMondwRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,128,1,2),_Pm1001lhMondwRmonPacketsCntValuePortn_Type())
pm1001lhMondwRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPacketsCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonPacketsCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonPacketsCntErrorPortn=_Pm1001lhMondwRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,128,1,3),_Pm1001lhMondwRmonPacketsCntErrorPortn_Type())
pm1001lhMondwRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPacketsCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonPacketsCntOverloadPortn=_Pm1001lhMondwRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,128,1,4),_Pm1001lhMondwRmonPacketsCntOverloadPortn_Type())
pm1001lhMondwRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonBroadcastCntTable_Object=MibTable
pm1001lhMondwRmonBroadcastCntTable=_Pm1001lhMondwRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,136))
if mibBuilder.loadTexts:pm1001lhMondwRmonBroadcastCntTable.setStatus(_A)
_Pm1001lhMondwRmonBroadcastCntEntry_Object=MibTableRow
pm1001lhMondwRmonBroadcastCntEntry=_Pm1001lhMondwRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,136,1))
pm1001lhMondwRmonBroadcastCntEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:pm1001lhMondwRmonBroadcastCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonBroadcastCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonBroadcastCntIndex_Object=MibTableColumn
pm1001lhMondwRmonBroadcastCntIndex=_Pm1001lhMondwRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,136,1,1),_Pm1001lhMondwRmonBroadcastCntIndex_Type())
pm1001lhMondwRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBroadcastCntIndex.setStatus(_A)
_Pm1001lhMondwRmonBroadcastCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonBroadcastCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonBroadcastCntValuePortn=_Pm1001lhMondwRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,136,1,2),_Pm1001lhMondwRmonBroadcastCntValuePortn_Type())
pm1001lhMondwRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBroadcastCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonBroadcastCntErrorPortn=_Pm1001lhMondwRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,136,1,3),_Pm1001lhMondwRmonBroadcastCntErrorPortn_Type())
pm1001lhMondwRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonBroadcastCntOverloadPortn=_Pm1001lhMondwRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,136,1,4),_Pm1001lhMondwRmonBroadcastCntOverloadPortn_Type())
pm1001lhMondwRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonMulticastCntTable_Object=MibTable
pm1001lhMondwRmonMulticastCntTable=_Pm1001lhMondwRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,144))
if mibBuilder.loadTexts:pm1001lhMondwRmonMulticastCntTable.setStatus(_A)
_Pm1001lhMondwRmonMulticastCntEntry_Object=MibTableRow
pm1001lhMondwRmonMulticastCntEntry=_Pm1001lhMondwRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,144,1))
pm1001lhMondwRmonMulticastCntEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:pm1001lhMondwRmonMulticastCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonMulticastCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonMulticastCntIndex_Object=MibTableColumn
pm1001lhMondwRmonMulticastCntIndex=_Pm1001lhMondwRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,144,1,1),_Pm1001lhMondwRmonMulticastCntIndex_Type())
pm1001lhMondwRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonMulticastCntIndex.setStatus(_A)
_Pm1001lhMondwRmonMulticastCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonMulticastCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonMulticastCntValuePortn=_Pm1001lhMondwRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,144,1,2),_Pm1001lhMondwRmonMulticastCntValuePortn_Type())
pm1001lhMondwRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonMulticastCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonMulticastCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonMulticastCntErrorPortn=_Pm1001lhMondwRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,144,1,3),_Pm1001lhMondwRmonMulticastCntErrorPortn_Type())
pm1001lhMondwRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonMulticastCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonMulticastCntOverloadPortn=_Pm1001lhMondwRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,144,1,4),_Pm1001lhMondwRmonMulticastCntOverloadPortn_Type())
pm1001lhMondwRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonMulticastCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonPauseFrameCntTable_Object=MibTable
pm1001lhMondwRmonPauseFrameCntTable=_Pm1001lhMondwRmonPauseFrameCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,152))
if mibBuilder.loadTexts:pm1001lhMondwRmonPauseFrameCntTable.setStatus(_A)
_Pm1001lhMondwRmonPauseFrameCntEntry_Object=MibTableRow
pm1001lhMondwRmonPauseFrameCntEntry=_Pm1001lhMondwRmonPauseFrameCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,152,1))
pm1001lhMondwRmonPauseFrameCntEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:pm1001lhMondwRmonPauseFrameCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonPauseFrameCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonPauseFrameCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonPauseFrameCntIndex_Object=MibTableColumn
pm1001lhMondwRmonPauseFrameCntIndex=_Pm1001lhMondwRmonPauseFrameCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,152,1,1),_Pm1001lhMondwRmonPauseFrameCntIndex_Type())
pm1001lhMondwRmonPauseFrameCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPauseFrameCntIndex.setStatus(_A)
_Pm1001lhMondwRmonPauseFrameCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonPauseFrameCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonPauseFrameCntValuePortn=_Pm1001lhMondwRmonPauseFrameCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,152,1,2),_Pm1001lhMondwRmonPauseFrameCntValuePortn_Type())
pm1001lhMondwRmonPauseFrameCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPauseFrameCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonPauseFrameCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonPauseFrameCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonPauseFrameCntErrorPortn=_Pm1001lhMondwRmonPauseFrameCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,152,1,3),_Pm1001lhMondwRmonPauseFrameCntErrorPortn_Type())
pm1001lhMondwRmonPauseFrameCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPauseFrameCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonPauseFrameCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonPauseFrameCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonPauseFrameCntOverloadPortn=_Pm1001lhMondwRmonPauseFrameCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,152,1,4),_Pm1001lhMondwRmonPauseFrameCntOverloadPortn_Type())
pm1001lhMondwRmonPauseFrameCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonPauseFrameCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonTimerCntTable_Object=MibTable
pm1001lhMondwRmonTimerCntTable=_Pm1001lhMondwRmonTimerCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,160))
if mibBuilder.loadTexts:pm1001lhMondwRmonTimerCntTable.setStatus(_A)
_Pm1001lhMondwRmonTimerCntEntry_Object=MibTableRow
pm1001lhMondwRmonTimerCntEntry=_Pm1001lhMondwRmonTimerCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,160,1))
pm1001lhMondwRmonTimerCntEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:pm1001lhMondwRmonTimerCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonTimerCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonTimerCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonTimerCntIndex_Object=MibTableColumn
pm1001lhMondwRmonTimerCntIndex=_Pm1001lhMondwRmonTimerCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,160,1,1),_Pm1001lhMondwRmonTimerCntIndex_Type())
pm1001lhMondwRmonTimerCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonTimerCntIndex.setStatus(_A)
_Pm1001lhMondwRmonTimerCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonTimerCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonTimerCntValuePortn=_Pm1001lhMondwRmonTimerCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,160,1,2),_Pm1001lhMondwRmonTimerCntValuePortn_Type())
pm1001lhMondwRmonTimerCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonTimerCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonTimerCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonTimerCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonTimerCntErrorPortn=_Pm1001lhMondwRmonTimerCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,160,1,3),_Pm1001lhMondwRmonTimerCntErrorPortn_Type())
pm1001lhMondwRmonTimerCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonTimerCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonTimerCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonTimerCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonTimerCntOverloadPortn=_Pm1001lhMondwRmonTimerCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,160,1,4),_Pm1001lhMondwRmonTimerCntOverloadPortn_Type())
pm1001lhMondwRmonTimerCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonTimerCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonBitsCntTable_Object=MibTable
pm1001lhMondwRmonBitsCntTable=_Pm1001lhMondwRmonBitsCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,168))
if mibBuilder.loadTexts:pm1001lhMondwRmonBitsCntTable.setStatus(_A)
_Pm1001lhMondwRmonBitsCntEntry_Object=MibTableRow
pm1001lhMondwRmonBitsCntEntry=_Pm1001lhMondwRmonBitsCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,168,1))
pm1001lhMondwRmonBitsCntEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:pm1001lhMondwRmonBitsCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonBitsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonBitsCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonBitsCntIndex_Object=MibTableColumn
pm1001lhMondwRmonBitsCntIndex=_Pm1001lhMondwRmonBitsCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,168,1,1),_Pm1001lhMondwRmonBitsCntIndex_Type())
pm1001lhMondwRmonBitsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBitsCntIndex.setStatus(_A)
_Pm1001lhMondwRmonBitsCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonBitsCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonBitsCntValuePortn=_Pm1001lhMondwRmonBitsCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,168,1,2),_Pm1001lhMondwRmonBitsCntValuePortn_Type())
pm1001lhMondwRmonBitsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBitsCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonBitsCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonBitsCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonBitsCntErrorPortn=_Pm1001lhMondwRmonBitsCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,168,1,3),_Pm1001lhMondwRmonBitsCntErrorPortn_Type())
pm1001lhMondwRmonBitsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBitsCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonBitsCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonBitsCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonBitsCntOverloadPortn=_Pm1001lhMondwRmonBitsCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,168,1,4),_Pm1001lhMondwRmonBitsCntOverloadPortn_Type())
pm1001lhMondwRmonBitsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonBitsCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonUnicastCntTable_Object=MibTable
pm1001lhMondwRmonUnicastCntTable=_Pm1001lhMondwRmonUnicastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,176))
if mibBuilder.loadTexts:pm1001lhMondwRmonUnicastCntTable.setStatus(_A)
_Pm1001lhMondwRmonUnicastCntEntry_Object=MibTableRow
pm1001lhMondwRmonUnicastCntEntry=_Pm1001lhMondwRmonUnicastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,176,1))
pm1001lhMondwRmonUnicastCntEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:pm1001lhMondwRmonUnicastCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonUnicastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonUnicastCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonUnicastCntIndex_Object=MibTableColumn
pm1001lhMondwRmonUnicastCntIndex=_Pm1001lhMondwRmonUnicastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,176,1,1),_Pm1001lhMondwRmonUnicastCntIndex_Type())
pm1001lhMondwRmonUnicastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonUnicastCntIndex.setStatus(_A)
_Pm1001lhMondwRmonUnicastCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonUnicastCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonUnicastCntValuePortn=_Pm1001lhMondwRmonUnicastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,176,1,2),_Pm1001lhMondwRmonUnicastCntValuePortn_Type())
pm1001lhMondwRmonUnicastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonUnicastCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonUnicastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonUnicastCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonUnicastCntErrorPortn=_Pm1001lhMondwRmonUnicastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,176,1,3),_Pm1001lhMondwRmonUnicastCntErrorPortn_Type())
pm1001lhMondwRmonUnicastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonUnicastCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonUnicastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonUnicastCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonUnicastCntOverloadPortn=_Pm1001lhMondwRmonUnicastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,176,1,4),_Pm1001lhMondwRmonUnicastCntOverloadPortn_Type())
pm1001lhMondwRmonUnicastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonUnicastCntOverloadPortn.setStatus(_A)
_Pm1001lhMondwRmonNonUnicastCntTable_Object=MibTable
pm1001lhMondwRmonNonUnicastCntTable=_Pm1001lhMondwRmonNonUnicastCntTable_Object((1,3,6,1,4,1,20044,10,12,4,1,184))
if mibBuilder.loadTexts:pm1001lhMondwRmonNonUnicastCntTable.setStatus(_A)
_Pm1001lhMondwRmonNonUnicastCntEntry_Object=MibTableRow
pm1001lhMondwRmonNonUnicastCntEntry=_Pm1001lhMondwRmonNonUnicastCntEntry_Object((1,3,6,1,4,1,20044,10,12,4,1,184,1))
pm1001lhMondwRmonNonUnicastCntEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:pm1001lhMondwRmonNonUnicastCntEntry.setStatus(_A)
class _Pm1001lhMondwRmonNonUnicastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001lhMondwRmonNonUnicastCntIndex_Type.__name__=_E
_Pm1001lhMondwRmonNonUnicastCntIndex_Object=MibTableColumn
pm1001lhMondwRmonNonUnicastCntIndex=_Pm1001lhMondwRmonNonUnicastCntIndex_Object((1,3,6,1,4,1,20044,10,12,4,1,184,1,1),_Pm1001lhMondwRmonNonUnicastCntIndex_Type())
pm1001lhMondwRmonNonUnicastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonNonUnicastCntIndex.setStatus(_A)
_Pm1001lhMondwRmonNonUnicastCntValuePortn_Type=Counter64
_Pm1001lhMondwRmonNonUnicastCntValuePortn_Object=MibTableColumn
pm1001lhMondwRmonNonUnicastCntValuePortn=_Pm1001lhMondwRmonNonUnicastCntValuePortn_Object((1,3,6,1,4,1,20044,10,12,4,1,184,1,2),_Pm1001lhMondwRmonNonUnicastCntValuePortn_Type())
pm1001lhMondwRmonNonUnicastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonNonUnicastCntValuePortn.setStatus(_A)
_Pm1001lhMondwRmonNonUnicastCntErrorPortn_Type=EkiOnOff
_Pm1001lhMondwRmonNonUnicastCntErrorPortn_Object=MibTableColumn
pm1001lhMondwRmonNonUnicastCntErrorPortn=_Pm1001lhMondwRmonNonUnicastCntErrorPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,184,1,3),_Pm1001lhMondwRmonNonUnicastCntErrorPortn_Type())
pm1001lhMondwRmonNonUnicastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonNonUnicastCntErrorPortn.setStatus(_A)
_Pm1001lhMondwRmonNonUnicastCntOverloadPortn_Type=EkiOnOff
_Pm1001lhMondwRmonNonUnicastCntOverloadPortn_Object=MibTableColumn
pm1001lhMondwRmonNonUnicastCntOverloadPortn=_Pm1001lhMondwRmonNonUnicastCntOverloadPortn_Object((1,3,6,1,4,1,20044,10,12,4,1,184,1,4),_Pm1001lhMondwRmonNonUnicastCntOverloadPortn_Type())
pm1001lhMondwRmonNonUnicastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001lhMondwRmonNonUnicastCntOverloadPortn.setStatus(_A)
_Pm1001lhRmonLine_ObjectIdentity=ObjectIdentity
pm1001lhRmonLine=_Pm1001lhRmonLine_ObjectIdentity((1,3,6,1,4,1,20044,10,12,4,2))
_Pm1001lhRmonOther_ObjectIdentity=ObjectIdentity
pm1001lhRmonOther=_Pm1001lhRmonOther_ObjectIdentity((1,3,6,1,4,1,20044,10,12,4,3))
_Pm1001lhMonCountersReset_Type=EkiOnOff
_Pm1001lhMonCountersReset_Object=MibScalar
pm1001lhMonCountersReset=_Pm1001lhMonCountersReset_Object((1,3,6,1,4,1,20044,10,12,4,3,359),_Pm1001lhMonCountersReset_Type())
pm1001lhMonCountersReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhMonCountersReset.setStatus(_A)
_Pm1001lhMonCountersStop_Type=EkiOnOff
_Pm1001lhMonCountersStop_Object=MibScalar
pm1001lhMonCountersStop=_Pm1001lhMonCountersStop_Object((1,3,6,1,4,1,20044,10,12,4,3,360),_Pm1001lhMonCountersStop_Type())
pm1001lhMonCountersStop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001lhMonCountersStop.setStatus(_A)
pm1001lhLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,30))
pm1001lhLineTrapNotUrgentGoesOn.setObjects(*((_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhLineTrapNotUrgentGoesOn.setStatus(_A)
pm1001lhLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,31))
pm1001lhLineTrapNotUrgentGoesOff.setObjects(*((_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhLineTrapNotUrgentGoesOff.setStatus(_A)
pm1001lhLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,32))
pm1001lhLineTrapUrgentGoesOn.setObjects(*((_C,_K),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhLineTrapUrgentGoesOn.setStatus(_A)
pm1001lhLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,33))
pm1001lhLineTrapUrgentGoesOff.setObjects(*((_C,_K),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhLineTrapUrgentGoesOff.setStatus(_A)
pm1001lhLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,34))
pm1001lhLineTrapCritGoesOn.setObjects(*((_C,_L),(_C,_M),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhLineTrapCritGoesOn.setStatus(_A)
pm1001lhLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,35))
pm1001lhLineTrapCritGoesOff.setObjects(*((_C,_L),(_C,_M),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhLineTrapCritGoesOff.setStatus(_A)
pm1001lhClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,40))
pm1001lhClientTrapNotUrgentGoesOn.setObjects(*((_C,_N),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhClientTrapNotUrgentGoesOn.setStatus(_A)
pm1001lhClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,41))
pm1001lhClientTrapNotUrgentGoesOff.setObjects(*((_C,_N),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhClientTrapNotUrgentGoesOff.setStatus(_A)
pm1001lhClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,42))
pm1001lhClientTrapUrgentGoesOn.setObjects(*((_C,_O),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhClientTrapUrgentGoesOn.setStatus(_A)
pm1001lhClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,43))
pm1001lhClientTrapUrgentGoesOff.setObjects(*((_C,_O),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhClientTrapUrgentGoesOff.setStatus(_A)
pm1001lhClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,44))
pm1001lhClientTrapCritGoesOn.setObjects(*((_C,_P),(_C,_Q),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhClientTrapCritGoesOn.setStatus(_A)
pm1001lhClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,45))
pm1001lhClientTrapCritGoesOff.setObjects(*((_C,_P),(_C,_Q),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhClientTrapCritGoesOff.setStatus(_A)
pm1001lhPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,10,11,50))
pm1001lhPowerTrapUrgentGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhPowerTrapUrgentGoesOn.setStatus(_A)
pm1001lhPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,10,11,51))
pm1001lhPowerTrapUrgentGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_H)))
if mibBuilder.loadTexts:pm1001lhPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Pm1001lhOtxMode':Pm1001lhOtxMode,'Pm1001lhOtxGrid':Pm1001lhOtxGrid,'Pm1001lhAdjustValue':Pm1001lhAdjustValue,'Pm1001lhOtxChannel':Pm1001lhOtxChannel,'modulepm1001lh':modulepm1001lh,'pm1001lhalarms':pm1001lhalarms,'pm1001lhAlmOther':pm1001lhAlmOther,'pm1001lhAlmOtherNurg':pm1001lhAlmOtherNurg,'pm1001lhAlmsynthAlm2':pm1001lhAlmsynthAlm2,'pm1001lhAlmConfTableSave':pm1001lhAlmConfTableSave,'pm1001lhAlmInvUpload':pm1001lhAlmInvUpload,'pm1001lhAlmConfTableLoad':pm1001lhAlmConfTableLoad,'pm1001lhAlmCorrelatOff':pm1001lhAlmCorrelatOff,'pm1001lhAlmMaintenanceOn':pm1001lhAlmMaintenanceOn,'pm1001lhAlmOtherUrg':pm1001lhAlmOtherUrg,'pm1001lhAlmmodInitFailLevel2':pm1001lhAlmmodInitFailLevel2,'pm1001lhAlmLedFail':pm1001lhAlmLedFail,'pm1001lhAlmNextColdBootForced':pm1001lhAlmNextColdBootForced,'pm1001lhAlmBootUndone':pm1001lhAlmBootUndone,'pm1001lhAlmResetHwInitFail':pm1001lhAlmResetHwInitFail,'pm1001lhAlmSwInitFail':pm1001lhAlmSwInitFail,'pm1001lhAlmmodInitFailLevel3':pm1001lhAlmmodInitFailLevel3,'pm1001lhAlmGwIdentFail':pm1001lhAlmGwIdentFail,'pm1001lhAlmObmTypeReadFail':pm1001lhAlmObmTypeReadFail,'pm1001lhAlmInitModuleFail':pm1001lhAlmInitModuleFail,'pm1001lhAlmXfp1InitFail':pm1001lhAlmXfp1InitFail,'pm1001lhAlmXfp2InitFail':pm1001lhAlmXfp2InitFail,'pm1001lhAlmLine1InitFail':pm1001lhAlmLine1InitFail,'pm1001lhAlmClient1InitFail':pm1001lhAlmClient1InitFail,'pm1001lhAlmOtherCrit':pm1001lhAlmOtherCrit,'pm1001lhAlmsynthAlm0':pm1001lhAlmsynthAlm0,'pm1001lhAlmModGlobFail':pm1001lhAlmModGlobFail,_S:pm1001lhAlmDefFuseA,_R:pm1001lhAlmDefFuseB,'pm1001lhAlmClient':pm1001lhAlmClient,'pm1001lhAlmClientNurg':pm1001lhAlmClientNurg,'pm1001lhAlmclientXfpWarnings':pm1001lhAlmclientXfpWarnings,'pm1001lhAlmClientTxPowerLowWarning':pm1001lhAlmClientTxPowerLowWarning,'pm1001lhAlmClientTxPowerHighWarning':pm1001lhAlmClientTxPowerHighWarning,'pm1001lhAlmClientTxBiasLowWarning':pm1001lhAlmClientTxBiasLowWarning,'pm1001lhAlmClientTxBiasHighWarning':pm1001lhAlmClientTxBiasHighWarning,'pm1001lhAlmClientTempLowWarning':pm1001lhAlmClientTempLowWarning,'pm1001lhAlmClientTempHighWarning':pm1001lhAlmClientTempHighWarning,'pm1001lhAlmClientRxPowerLowWarning':pm1001lhAlmClientRxPowerLowWarning,'pm1001lhAlmClientRxPowerHighWarning':pm1001lhAlmClientRxPowerHighWarning,'pm1001lhAlmClientUrg':pm1001lhAlmClientUrg,'pm1001lhAlmclientXfpAlarm1':pm1001lhAlmclientXfpAlarm1,'pm1001lhAlmClientTxPowerLowAlarm':pm1001lhAlmClientTxPowerLowAlarm,'pm1001lhAlmClientTxPowerHighAlarm':pm1001lhAlmClientTxPowerHighAlarm,'pm1001lhAlmClientTxBiasLowAlarm':pm1001lhAlmClientTxBiasLowAlarm,'pm1001lhAlmClientTxBiasHighAlarm':pm1001lhAlmClientTxBiasHighAlarm,'pm1001lhAlmClientTempLowAlarm':pm1001lhAlmClientTempLowAlarm,'pm1001lhAlmClientTempHighAlarm':pm1001lhAlmClientTempHighAlarm,'pm1001lhAlmClientRxPowerLowAlarm':pm1001lhAlmClientRxPowerLowAlarm,'pm1001lhAlmClientRxPowerHighAlarm':pm1001lhAlmClientRxPowerHighAlarm,'pm1001lhAlmclientXfpSupplyAlarm':pm1001lhAlmclientXfpSupplyAlarm,'pm1001lhAlmClientVee5LowAlarm':pm1001lhAlmClientVee5LowAlarm,'pm1001lhAlmClientVee5HighAlarm':pm1001lhAlmClientVee5HighAlarm,'pm1001lhAlmClientVcc2LowAlarm':pm1001lhAlmClientVcc2LowAlarm,'pm1001lhAlmClientVcc2HighAlarm':pm1001lhAlmClientVcc2HighAlarm,'pm1001lhAlmClientVcc3LowAlarm':pm1001lhAlmClientVcc3LowAlarm,'pm1001lhAlmClientVcc3HighAlarm':pm1001lhAlmClientVcc3HighAlarm,'pm1001lhAlmClientVcc5LowAlarm':pm1001lhAlmClientVcc5LowAlarm,'pm1001lhAlmClientVcc5HighAlarm':pm1001lhAlmClientVcc5HighAlarm,'pm1001lhAlmClientVee5LowWarning':pm1001lhAlmClientVee5LowWarning,'pm1001lhAlmClientVee5HighWarning':pm1001lhAlmClientVee5HighWarning,'pm1001lhAlmClientVcc2LowWarning':pm1001lhAlmClientVcc2LowWarning,'pm1001lhAlmClientVcc2HighWarning':pm1001lhAlmClientVcc2HighWarning,'pm1001lhAlmClientVcc3LowWarning':pm1001lhAlmClientVcc3LowWarning,'pm1001lhAlmClientVcc3HighWarning':pm1001lhAlmClientVcc3HighWarning,'pm1001lhAlmClientVcc5LowWarning':pm1001lhAlmClientVcc5LowWarning,'pm1001lhAlmClientVcc5HighWarning':pm1001lhAlmClientVcc5HighWarning,'pm1001lhAlmClientCrit':pm1001lhAlmClientCrit,'pm1001lhAlmsynthAlmPort':pm1001lhAlmsynthAlmPort,'pm1001lhAlmClientXfpAbsent':pm1001lhAlmClientXfpAbsent,'pm1001lhAlmClientDdmAbsent':pm1001lhAlmClientDdmAbsent,_Q:pm1001lhAlmClientHwFail,'pm1001lhAlmClientDwLsd':pm1001lhAlmClientDwLsd,'pm1001lhAlmClientLocalOos':pm1001lhAlmClientLocalOos,'pm1001lhAlmClientDwCais':pm1001lhAlmClientDwCais,_N:pm1001lhAlmClientXfpDdmWarning,_O:pm1001lhAlmClientXfpDdmAlm,_P:pm1001lhAlmClientFail,'pm1001lhAlmClientUpCsf':pm1001lhAlmClientUpCsf,'pm1001lhAlmclientAccessioAlm':pm1001lhAlmclientAccessioAlm,'pm1001lhAlmClientDwLasFail':pm1001lhAlmClientDwLasFail,'pm1001lhAlmClientUpLos':pm1001lhAlmClientUpLos,'pm1001lhAlmclientXfpAlarm2':pm1001lhAlmclientXfpAlarm2,'pm1001lhAlmClientModNr':pm1001lhAlmClientModNr,'pm1001lhAlmClientRxCdrNotLocked1':pm1001lhAlmClientRxCdrNotLocked1,'pm1001lhAlmClientRxNr':pm1001lhAlmClientRxNr,'pm1001lhAlmClientTxCdrNotLocked1':pm1001lhAlmClientTxCdrNotLocked1,'pm1001lhAlmClientTxFault':pm1001lhAlmClientTxFault,'pm1001lhAlmClientTxNr':pm1001lhAlmClientTxNr,'pm1001lhAlmClientWavelengthUnlocked':pm1001lhAlmClientWavelengthUnlocked,'pm1001lhAlmClientTecFault':pm1001lhAlmClientTecFault,'pm1001lhAlmClientApdSupplyFault':pm1001lhAlmClientApdSupplyFault,'pm1001lhAlmclientMapperDeAlm':pm1001lhAlmclientMapperDeAlm,'pm1001lhAlmClientUpAccOos':pm1001lhAlmClientUpAccOos,'pm1001lhAlmClientUpBufferOvl':pm1001lhAlmClientUpBufferOvl,'pm1001lhAlmClientDwCsfDet':pm1001lhAlmClientDwCsfDet,'pm1001lhAlmClientDwBufferOvl':pm1001lhAlmClientDwBufferOvl,'pm1001lhAlmLine':pm1001lhAlmLine,'pm1001lhAlmLineNurg':pm1001lhAlmLineNurg,'pm1001lhAlmlineXfpWarnings':pm1001lhAlmlineXfpWarnings,'pm1001lhAlmLineTxPowerLowWarning':pm1001lhAlmLineTxPowerLowWarning,'pm1001lhAlmLineTxPowerHighWarning':pm1001lhAlmLineTxPowerHighWarning,'pm1001lhAlmLineTxBiasLowWarning':pm1001lhAlmLineTxBiasLowWarning,'pm1001lhAlmLineTxBiasHighWarning':pm1001lhAlmLineTxBiasHighWarning,'pm1001lhAlmLineTempLowWarning':pm1001lhAlmLineTempLowWarning,'pm1001lhAlmLineTempHighWarning':pm1001lhAlmLineTempHighWarning,'pm1001lhAlmLineRxPowerLowWarning':pm1001lhAlmLineRxPowerLowWarning,'pm1001lhAlmLineRxPowerHighWarning':pm1001lhAlmLineRxPowerHighWarning,'pm1001lhAlmlineOtxTlhWarnings':pm1001lhAlmlineOtxTlhWarnings,'pm1001lhAlmLineModulatorAgingHighWarning':pm1001lhAlmLineModulatorAgingHighWarning,'pm1001lhAlmLineAgingHighWarning':pm1001lhAlmLineAgingHighWarning,'pm1001lhAlmLineFreqDevHighWarning':pm1001lhAlmLineFreqDevHighWarning,'pm1001lhAlmLineLaserTempHighWarning':pm1001lhAlmLineLaserTempHighWarning,'pm1001lhAlmLineUrg':pm1001lhAlmLineUrg,'pm1001lhAlmdfrmBer':pm1001lhAlmdfrmBer,'pm1001lhAlmLineSignalDegrade':pm1001lhAlmLineSignalDegrade,'pm1001lhAlmLineSignalFail':pm1001lhAlmLineSignalFail,'pm1001lhAlmLineDegrade':pm1001lhAlmLineDegrade,'pm1001lhAlmlineXfpAlarm1':pm1001lhAlmlineXfpAlarm1,'pm1001lhAlmLineTxPowerLowAlarm':pm1001lhAlmLineTxPowerLowAlarm,'pm1001lhAlmLineTxPowerHighAlarm':pm1001lhAlmLineTxPowerHighAlarm,'pm1001lhAlmLineTxBiasLowAlarm':pm1001lhAlmLineTxBiasLowAlarm,'pm1001lhAlmLineTxBiasHighAlarm':pm1001lhAlmLineTxBiasHighAlarm,'pm1001lhAlmLineTempLowAlarm':pm1001lhAlmLineTempLowAlarm,'pm1001lhAlmLineTempHighAlarm':pm1001lhAlmLineTempHighAlarm,'pm1001lhAlmLineRxPowerLowAlarm':pm1001lhAlmLineRxPowerLowAlarm,'pm1001lhAlmLineRxPowerHighAlarm':pm1001lhAlmLineRxPowerHighAlarm,'pm1001lhAlmlineXfpSupplyAlarm':pm1001lhAlmlineXfpSupplyAlarm,'pm1001lhAlmLineVee5LowAlarm':pm1001lhAlmLineVee5LowAlarm,'pm1001lhAlmLineVee5HighAlarm':pm1001lhAlmLineVee5HighAlarm,'pm1001lhAlmLineVcc2LowAlarm':pm1001lhAlmLineVcc2LowAlarm,'pm1001lhAlmLineVcc2HighAlarm':pm1001lhAlmLineVcc2HighAlarm,'pm1001lhAlmLineVcc3LowAlarm':pm1001lhAlmLineVcc3LowAlarm,'pm1001lhAlmLineVcc3HighAlarm':pm1001lhAlmLineVcc3HighAlarm,'pm1001lhAlmLineVcc5LowAlarm':pm1001lhAlmLineVcc5LowAlarm,'pm1001lhAlmLineVcc5HighAlarm':pm1001lhAlmLineVcc5HighAlarm,'pm1001lhAlmLineVee5LowLineWarning':pm1001lhAlmLineVee5LowLineWarning,'pm1001lhAlmLineVee5HighWarning':pm1001lhAlmLineVee5HighWarning,'pm1001lhAlmLineVcc2LowWarning':pm1001lhAlmLineVcc2LowWarning,'pm1001lhAlmLineVcc2HighWarning':pm1001lhAlmLineVcc2HighWarning,'pm1001lhAlmLineVcc3LowWarning':pm1001lhAlmLineVcc3LowWarning,'pm1001lhAlmLineVcc3HighWarning':pm1001lhAlmLineVcc3HighWarning,'pm1001lhAlmLineVcc5LowWarning':pm1001lhAlmLineVcc5LowWarning,'pm1001lhAlmLineVcc5HighWarning':pm1001lhAlmLineVcc5HighWarning,'pm1001lhAlmlineOtxTlhAlarms3':pm1001lhAlmlineOtxTlhAlarms3,'pm1001lhAlmLineModulatorAgingHighAla':pm1001lhAlmLineModulatorAgingHighAla,'pm1001lhAlmLineAgingHighAla':pm1001lhAlmLineAgingHighAla,'pm1001lhAlmLineCdrNotReady':pm1001lhAlmLineCdrNotReady,'pm1001lhAlmLineFreqDevHighAla':pm1001lhAlmLineFreqDevHighAla,'pm1001lhAlmLineLaserTempHighAla':pm1001lhAlmLineLaserTempHighAla,'pm1001lhAlmLineCrit':pm1001lhAlmLineCrit,'pm1001lhAlmsynthAlmLine':pm1001lhAlmsynthAlmLine,'pm1001lhAlmLineXfpAbsent':pm1001lhAlmLineXfpAbsent,'pm1001lhAlmLineXfpInitNotCompl':pm1001lhAlmLineXfpInitNotCompl,_M:pm1001lhAlmLineHwFail,'pm1001lhAlmLineXfpTxOff':pm1001lhAlmLineXfpTxOff,'pm1001lhAlmLineLocalOos':pm1001lhAlmLineLocalOos,'pm1001lhAlmLineUpRdiIns':pm1001lhAlmLineUpRdiIns,_J:pm1001lhAlmLineDdmWarning,_K:pm1001lhAlmLineDdmAlm,_L:pm1001lhAlmLineFail,'pm1001lhAlmdfrmAlm':pm1001lhAlmdfrmAlm,'pm1001lhAlmLineDwAisDet':pm1001lhAlmLineDwAisDet,'pm1001lhAlmLineDwRdiDet':pm1001lhAlmLineDwRdiDet,'pm1001lhAlmLineDwOof':pm1001lhAlmLineDwOof,'pm1001lhAlmLineDwLof':pm1001lhAlmLineDwLof,'pm1001lhAlmLineFecFail':pm1001lhAlmLineFecFail,'pm1001lhAlmlineSyncAlarms':pm1001lhAlmlineSyncAlarms,'pm1001lhAlmLineDwLockerr':pm1001lhAlmLineDwLockerr,'pm1001lhAlmLineUpLockerr':pm1001lhAlmLineUpLockerr,'pm1001lhAlmLineDwLos':pm1001lhAlmLineDwLos,'pm1001lhAlmlineXfpAlarms2':pm1001lhAlmlineXfpAlarms2,'pm1001lhAlmLineModNr':pm1001lhAlmLineModNr,'pm1001lhAlmLineRxCdrNotLocked1':pm1001lhAlmLineRxCdrNotLocked1,'pm1001lhAlmLineRxNr':pm1001lhAlmLineRxNr,'pm1001lhAlmLineTxCdrNotLocked1':pm1001lhAlmLineTxCdrNotLocked1,'pm1001lhAlmLineTxFault':pm1001lhAlmLineTxFault,'pm1001lhAlmLineTxNr':pm1001lhAlmLineTxNr,'pm1001lhAlmLineChannelNotAcquired':pm1001lhAlmLineChannelNotAcquired,'pm1001lhAlmLineWavelengthUnlocked':pm1001lhAlmLineWavelengthUnlocked,'pm1001lhAlmLineTecFault':pm1001lhAlmLineTecFault,'pm1001lhAlmLineApdSupplyFault':pm1001lhAlmLineApdSupplyFault,'pm1001lhmeasures':pm1001lhmeasures,'pm1001lhMesrOther':pm1001lhMesrOther,'pm1001lhMesrsynth0':pm1001lhMesrsynth0,'pm1001lhMesrsynth1':pm1001lhMesrsynth1,'pm1001lhMesrClient':pm1001lhMesrClient,'pm1001lhMesrclientModTempMeas':pm1001lhMesrclientModTempMeas,'pm1001lhMesrclientBiasCurrentMeas':pm1001lhMesrclientBiasCurrentMeas,'pm1001lhMesrclientTxPowerMeas':pm1001lhMesrclientTxPowerMeas,'pm1001lhMesrclientRxPowerMeas':pm1001lhMesrclientRxPowerMeas,'pm1001lhMesrLine':pm1001lhMesrLine,'pm1001lhMesrlineModTempMeas':pm1001lhMesrlineModTempMeas,'pm1001lhMesrlineReserved':pm1001lhMesrlineReserved,'pm1001lhMesrlineBiasCurrentMeas':pm1001lhMesrlineBiasCurrentMeas,'pm1001lhMesrlineTxPowerMeas':pm1001lhMesrlineTxPowerMeas,'pm1001lhMesrlineRxPowerMeas':pm1001lhMesrlineRxPowerMeas,'pm1001lhMesrlineAux1Meas':pm1001lhMesrlineAux1Meas,'pm1001lhMesrlineAux2Meas':pm1001lhMesrlineAux2Meas,'pm1001lhMesrlineAging':pm1001lhMesrlineAging,'pm1001lhMesrlineLaserTemperature':pm1001lhMesrlineLaserTemperature,'pm1001lhMesrlineFreqDeviation':pm1001lhMesrlineFreqDeviation,'pm1001lhMesrlineLaserWvlength':pm1001lhMesrlineLaserWvlength,'pm1001lhcounters':pm1001lhcounters,'pm1001lhCntOther':pm1001lhCntOther,'pm1001lhCntClient':pm1001lhCntClient,'pm1001lhCntclientUpErrCntTable':pm1001lhCntclientUpErrCntTable,'pm1001lhCntclientUpErrCntEntry':pm1001lhCntclientUpErrCntEntry,_W:pm1001lhCntclientUpErrCntIndex,'pm1001lhCntclientUpErrCntValuePortn':pm1001lhCntclientUpErrCntValuePortn,'pm1001lhCntclientUpErrCntErrorPortn':pm1001lhCntclientUpErrCntErrorPortn,'pm1001lhCntclientUpErrCntOverloadPortn':pm1001lhCntclientUpErrCntOverloadPortn,'pm1001lhCntclientUpTimCntTable':pm1001lhCntclientUpTimCntTable,'pm1001lhCntclientUpTimCntEntry':pm1001lhCntclientUpTimCntEntry,_X:pm1001lhCntclientUpTimCntIndex,'pm1001lhCntclientUpTimCntValuePortn':pm1001lhCntclientUpTimCntValuePortn,'pm1001lhCntclientUpTimCntErrorPortn':pm1001lhCntclientUpTimCntErrorPortn,'pm1001lhCntclientUpTimCntOverloadPortn':pm1001lhCntclientUpTimCntOverloadPortn,'pm1001lhCntclientDwErrCntTable':pm1001lhCntclientDwErrCntTable,'pm1001lhCntclientDwErrCntEntry':pm1001lhCntclientDwErrCntEntry,_Y:pm1001lhCntclientDwErrCntIndex,'pm1001lhCntclientDwErrCntValuePortn':pm1001lhCntclientDwErrCntValuePortn,'pm1001lhCntclientDwErrCntErrorPortn':pm1001lhCntclientDwErrCntErrorPortn,'pm1001lhCntclientDwErrCntOverloadPortn':pm1001lhCntclientDwErrCntOverloadPortn,'pm1001lhCntclientDwTimCntTable':pm1001lhCntclientDwTimCntTable,'pm1001lhCntclientDwTimCntEntry':pm1001lhCntclientDwTimCntEntry,_Z:pm1001lhCntclientDwTimCntIndex,'pm1001lhCntclientDwTimCntValuePortn':pm1001lhCntclientDwTimCntValuePortn,'pm1001lhCntclientDwTimCntErrorPortn':pm1001lhCntclientDwTimCntErrorPortn,'pm1001lhCntclientDwTimCntOverloadPortn':pm1001lhCntclientDwTimCntOverloadPortn,'pm1001lhCntLine':pm1001lhCntLine,'pm1001lhCntlineDfrmErrCntTable':pm1001lhCntlineDfrmErrCntTable,'pm1001lhCntlineDfrmErrCntEntry':pm1001lhCntlineDfrmErrCntEntry,_a:pm1001lhCntlineDfrmErrCntIndex,'pm1001lhCntlineDfrmErrCntValuePortn':pm1001lhCntlineDfrmErrCntValuePortn,'pm1001lhCntlineDfrmErrCntErrorPortn':pm1001lhCntlineDfrmErrCntErrorPortn,'pm1001lhCntlineDfrmErrCntOverloadPortn':pm1001lhCntlineDfrmErrCntOverloadPortn,'pm1001lhCntlineDfrmTimCntTable':pm1001lhCntlineDfrmTimCntTable,'pm1001lhCntlineDfrmTimCntEntry':pm1001lhCntlineDfrmTimCntEntry,_b:pm1001lhCntlineDfrmTimCntIndex,'pm1001lhCntlineDfrmTimCntValuePortn':pm1001lhCntlineDfrmTimCntValuePortn,'pm1001lhCntlineDfrmTimCntErrorPortn':pm1001lhCntlineDfrmTimCntErrorPortn,'pm1001lhCntlineDfrmTimCntOverloadPortn':pm1001lhCntlineDfrmTimCntOverloadPortn,'pm1001lhCntlineDfrmPrimErrCntTable':pm1001lhCntlineDfrmPrimErrCntTable,'pm1001lhCntlineDfrmPrimErrCntEntry':pm1001lhCntlineDfrmPrimErrCntEntry,_c:pm1001lhCntlineDfrmPrimErrCntIndex,'pm1001lhCntlineDfrmPrimErrCntValuePortn':pm1001lhCntlineDfrmPrimErrCntValuePortn,'pm1001lhCntlineDfrmPrimErrCntErrorPortn':pm1001lhCntlineDfrmPrimErrCntErrorPortn,'pm1001lhCntlineDfrmPrimErrCntOverloadPortn':pm1001lhCntlineDfrmPrimErrCntOverloadPortn,'pm1001lhCntlineDfrmErrCntSTable':pm1001lhCntlineDfrmErrCntSTable,'pm1001lhCntlineDfrmErrCntSEntry':pm1001lhCntlineDfrmErrCntSEntry,_d:pm1001lhCntlineDfrmErrCntSIndex,'pm1001lhCntlineDfrmErrCntSValuePortn':pm1001lhCntlineDfrmErrCntSValuePortn,'pm1001lhCntlineDfrmErrCntSErrorPortn':pm1001lhCntlineDfrmErrCntSErrorPortn,'pm1001lhCntlineDfrmErrCntSOverloadPortn':pm1001lhCntlineDfrmErrCntSOverloadPortn,'pm1001lhCntCountersReset':pm1001lhCntCountersReset,'pm1001lhCntCountersStop':pm1001lhCntCountersStop,'pm1001lhcontrolsWrite':pm1001lhcontrolsWrite,'pm1001lhCtrlOther':pm1001lhCtrlOther,'pm1001lhCtrlconfMgnt1':pm1001lhCtrlconfMgnt1,'pm1001lhCtrlConf1Load1':pm1001lhCtrlConf1Load1,'pm1001lhCtrlConf2Load1':pm1001lhCtrlConf2Load1,'pm1001lhCtrlConf2Flash1':pm1001lhCtrlConf2Flash1,'pm1001lhCtrlConf2Clear1':pm1001lhCtrlConf2Clear1,'pm1001lhCtrlsynth4':pm1001lhCtrlsynth4,'pm1001lhCtrlCorrelatOn':pm1001lhCtrlCorrelatOn,'pm1001lhCtrlCorrelatOff':pm1001lhCtrlCorrelatOff,'pm1001lhCtrlswMgnt':pm1001lhCtrlswMgnt,'pm1001lhCtrlColdReset':pm1001lhCtrlColdReset,'pm1001lhCtrlWarmReset':pm1001lhCtrlWarmReset,'pm1001lhCtrlLoadSwBank1':pm1001lhCtrlLoadSwBank1,'pm1001lhCtrlLoadSwBank2':pm1001lhCtrlLoadSwBank2,'pm1001lhCtrlgwMgnt':pm1001lhCtrlgwMgnt,'pm1001lhCtrlCurrentGwReset':pm1001lhCtrlCurrentGwReset,'pm1001lhCtrlLoadGwBank1':pm1001lhCtrlLoadGwBank1,'pm1001lhCtrlLoadGwBank2':pm1001lhCtrlLoadGwBank2,'pm1001lhCtrlLoadGwBank3':pm1001lhCtrlLoadGwBank3,'pm1001lhCtrlLoadGwBank4':pm1001lhCtrlLoadGwBank4,'pm1001lhCtrlledTest':pm1001lhCtrlledTest,'pm1001lhCtrlGreenLed':pm1001lhCtrlGreenLed,'pm1001lhCtrlRedLed':pm1001lhCtrlRedLed,'pm1001lhCtrlLedOff':pm1001lhCtrlLedOff,'pm1001lhCtrlmoduleOosMode':pm1001lhCtrlmoduleOosMode,'pm1001lhCtrlModuleOosMode':pm1001lhCtrlModuleOosMode,'pm1001lhCtrlmaintenanceMode':pm1001lhCtrlmaintenanceMode,'pm1001lhCtrlMaintenanceMode':pm1001lhCtrlMaintenanceMode,'pm1001lhCtrldccEnable':pm1001lhCtrldccEnable,'pm1001lhCtrlDccEnable':pm1001lhCtrlDccEnable,'pm1001lhCtrlClient':pm1001lhCtrlClient,'pm1001lhCtrlaccessLoopTable':pm1001lhCtrlaccessLoopTable,'pm1001lhCtrlaccessLoopEntry':pm1001lhCtrlaccessLoopEntry,_e:pm1001lhCtrlaccessLoopIndex,'pm1001lhCtrlaccessLoopPortn':pm1001lhCtrlaccessLoopPortn,'pm1001lhCtrlportOosModeTable':pm1001lhCtrlportOosModeTable,'pm1001lhCtrlportOosModeEntry':pm1001lhCtrlportOosModeEntry,_f:pm1001lhCtrlportOosModeIndex,'pm1001lhCtrlportOosModePortn':pm1001lhCtrlportOosModePortn,'pm1001lhCtrlxfpOffCtrlTable':pm1001lhCtrlxfpOffCtrlTable,'pm1001lhCtrlxfpOffCtrlEntry':pm1001lhCtrlxfpOffCtrlEntry,_g:pm1001lhCtrlxfpOffCtrlIndex,'pm1001lhCtrlxfpOffCtrlPortn':pm1001lhCtrlxfpOffCtrlPortn,'pm1001lhCtrlcsfUpInsTable':pm1001lhCtrlcsfUpInsTable,'pm1001lhCtrlcsfUpInsEntry':pm1001lhCtrlcsfUpInsEntry,_h:pm1001lhCtrlcsfUpInsIndex,'pm1001lhCtrlcsfUpInsPortn':pm1001lhCtrlcsfUpInsPortn,'pm1001lhCtrlcaisDwInsTable':pm1001lhCtrlcaisDwInsTable,'pm1001lhCtrlcaisDwInsEntry':pm1001lhCtrlcaisDwInsEntry,_i:pm1001lhCtrlcaisDwInsIndex,'pm1001lhCtrlcaisDwInsPortn':pm1001lhCtrlcaisDwInsPortn,'pm1001lhCtrlclientAccessTermLoopTable':pm1001lhCtrlclientAccessTermLoopTable,'pm1001lhCtrlclientAccessTermLoopEntry':pm1001lhCtrlclientAccessTermLoopEntry,_j:pm1001lhCtrlclientAccessTermLoopIndex,'pm1001lhCtrlclientAccessTermLoopPortn':pm1001lhCtrlclientAccessTermLoopPortn,'pm1001lhCtrlprotocol':pm1001lhCtrlprotocol,'pm1001lhCtrlclientResetAllCountTable':pm1001lhCtrlclientResetAllCountTable,'pm1001lhCtrlclientResetAllCountEntry':pm1001lhCtrlclientResetAllCountEntry,_k:pm1001lhCtrlclientResetAllCountIndex,'pm1001lhCtrlclientResetAllCountsPortn':pm1001lhCtrlclientResetAllCountsPortn,'pm1001lhCtrlLine':pm1001lhCtrlLine,'pm1001lhCtrlcommAccessLoop':pm1001lhCtrlcommAccessLoop,'pm1001lhCtrlCommAccessloop':pm1001lhCtrlCommAccessloop,'pm1001lhCtrllineLoop':pm1001lhCtrllineLoop,'pm1001lhCtrlLineLoop':pm1001lhCtrlLineLoop,'pm1001lhCtrlmsAis':pm1001lhCtrlmsAis,'pm1001lhCtrlMsAis':pm1001lhCtrlMsAis,'pm1001lhCtrlfecDisable':pm1001lhCtrlfecDisable,'pm1001lhCtrlFecInhibition':pm1001lhCtrlFecInhibition,'pm1001lhCtrllineOosMode':pm1001lhCtrllineOosMode,'pm1001lhCtrlLineOosMode':pm1001lhCtrlLineOosMode,'pm1001lhCtrlxfpOnoffTable':pm1001lhCtrlxfpOnoffTable,'pm1001lhCtrlxfpOnoffEntry':pm1001lhCtrlxfpOnoffEntry,_l:pm1001lhCtrlxfpOnoffIndex,'pm1001lhCtrlxfpOnoffPortn':pm1001lhCtrlxfpOnoffPortn,'pm1001lhCtrlxfpLineLoopTable':pm1001lhCtrlxfpLineLoopTable,'pm1001lhCtrlxfpLineLoopEntry':pm1001lhCtrlxfpLineLoopEntry,_m:pm1001lhCtrlxfpLineLoopIndex,'pm1001lhCtrlxfpLineLoopPortn':pm1001lhCtrlxfpLineLoopPortn,'pm1001lhCtrlxfpLineXfiLoopTable':pm1001lhCtrlxfpLineXfiLoopTable,'pm1001lhCtrlxfpLineXfiLoopEntry':pm1001lhCtrlxfpLineXfiLoopEntry,_n:pm1001lhCtrlxfpLineXfiLoopIndex,'pm1001lhCtrlxfpLineXfiLoopPortn':pm1001lhCtrlxfpLineXfiLoopPortn,'pm1001lhCtrllineTunableChannel':pm1001lhCtrllineTunableChannel,'pm1001lhCtrllinePhotodiodeMode':pm1001lhCtrllinePhotodiodeMode,'pm1001lhCtrllinePhotodiodeValue':pm1001lhCtrllinePhotodiodeValue,'pm1001lhCtrllinePowerLaser':pm1001lhCtrllinePowerLaser,'pm1001lhCtrlotxVlhReset':pm1001lhCtrlotxVlhReset,'pm1001lhCtrlOtxVlhReset':pm1001lhCtrlOtxVlhReset,'pm1001lhCtrllineAccessLoopTable':pm1001lhCtrllineAccessLoopTable,'pm1001lhCtrllineAccessLoopEntry':pm1001lhCtrllineAccessLoopEntry,_o:pm1001lhCtrllineAccessLoopIndex,'pm1001lhCtrllineAccessLoopPortn':pm1001lhCtrllineAccessLoopPortn,'pm1001lhCtrllineLoopTransceiverTable':pm1001lhCtrllineLoopTransceiverTable,'pm1001lhCtrllineLoopTransceiverEntry':pm1001lhCtrllineLoopTransceiverEntry,_p:pm1001lhCtrllineLoopTransceiverIndex,'pm1001lhCtrllineLoopTransceiverPortn':pm1001lhCtrllineLoopTransceiverPortn,'pm1001lhCtrllineResetAllCountTable':pm1001lhCtrllineResetAllCountTable,'pm1001lhCtrllineResetAllCountEntry':pm1001lhCtrllineResetAllCountEntry,_q:pm1001lhCtrllineResetAllCountIndex,'pm1001lhCtrllineResetAllCountsPortn':pm1001lhCtrllineResetAllCountsPortn,'pm1001lhri':pm1001lhri,'pm1001lhriTable':pm1001lhriTable,'pm1001lhRinvReloadInventory':pm1001lhRinvReloadInventory,'pm1001lhRinvHwPlatform':pm1001lhRinvHwPlatform,'pm1001lhRinvModulePlatform':pm1001lhRinvModulePlatform,'pm1001lhRinvSwPlatform':pm1001lhRinvSwPlatform,'pm1001lhRinvGwPlatform':pm1001lhRinvGwPlatform,'pm1001lhRinvClient':pm1001lhRinvClient,'pm1001lhRinvLine':pm1001lhRinvLine,'pm1001lhdownload':pm1001lhdownload,'pm1001lhDwlOther':pm1001lhDwlOther,'pm1001lhDwlrestartProcess':pm1001lhDwlrestartProcess,'pm1001lhDwlWarmRestartProcessed':pm1001lhDwlWarmRestartProcessed,'pm1001lhDwlColdRestartProcessed':pm1001lhDwlColdRestartProcessed,'pm1001lhDwlswBanksUsed':pm1001lhDwlswBanksUsed,'pm1001lhDwlSwBank1Used':pm1001lhDwlSwBank1Used,'pm1001lhDwlSwBank2Used':pm1001lhDwlSwBank2Used,'pm1001lhDwlSwBank1Notempty':pm1001lhDwlSwBank1Notempty,'pm1001lhDwlSwBank2Notempty':pm1001lhDwlSwBank2Notempty,'pm1001lhDwlgwBanksUsed':pm1001lhDwlgwBanksUsed,'pm1001lhDwlGwBank1Used':pm1001lhDwlGwBank1Used,'pm1001lhDwlGwBank2Used':pm1001lhDwlGwBank2Used,'pm1001lhDwlGwBank3Used':pm1001lhDwlGwBank3Used,'pm1001lhDwlGwBank4Used':pm1001lhDwlGwBank4Used,'pm1001lhDwlGwBank1Notempty':pm1001lhDwlGwBank1Notempty,'pm1001lhDwlGwBank2Notempty':pm1001lhDwlGwBank2Notempty,'pm1001lhDwlGwBank3Notempty':pm1001lhDwlGwBank3Notempty,'pm1001lhDwlGwBank4Notempty':pm1001lhDwlGwBank4Notempty,'pm1001lhDwlClient':pm1001lhDwlClient,'pm1001lhDwlLine':pm1001lhDwlLine,'pm1001lhConfig':pm1001lhConfig,'pm1001lhCfgAccessCAisCsf':pm1001lhCfgAccessCAisCsf,'pm1001lhCfgClientcaiscsfTable':pm1001lhCfgClientcaiscsfTable,'pm1001lhCfgClientcaiscsfEntry':pm1001lhCfgClientcaiscsfEntry,_r:pm1001lhCfgClientcaiscsfIndex,'pm1001lhCfgCAisModePortn':pm1001lhCfgCAisModePortn,'pm1001lhCfgUpAccessioAlmPortn':pm1001lhCfgUpAccessioAlmPortn,'pm1001lhCfgUpMapperDeAlmPortn':pm1001lhCfgUpMapperDeAlmPortn,'pm1001lhCfgDownAccessioAlmPortn':pm1001lhCfgDownAccessioAlmPortn,'pm1001lhCfgDownMapperDeAlmPortn':pm1001lhCfgDownMapperDeAlmPortn,'pm1001lhCfgDownDfrmAlmPortn':pm1001lhCfgDownDfrmAlmPortn,'pm1001lhCfgDownLineSyncAlarmsPortn':pm1001lhCfgDownLineSyncAlarmsPortn,'pm1001lhCfgStartup':pm1001lhCfgStartup,'pm1001lhCfgClientStartupTable':pm1001lhCfgClientStartupTable,'pm1001lhCfgClientStartupEntry':pm1001lhCfgClientStartupEntry,_s:pm1001lhCfgClientStartupIndex,'pm1001lhCfgSystConfPortPortn':pm1001lhCfgSystConfPortPortn,'pm1001lhCfgNetConfPortPortn':pm1001lhCfgNetConfPortPortn,'pm1001lhCfgPortsOptionsPortn':pm1001lhCfgPortsOptionsPortn,'pm1001lhtablelineStartup':pm1001lhtablelineStartup,'pm1001lhCfgsynthTransLine':pm1001lhCfgsynthTransLine,'pm1001lhCfglineOptions1':pm1001lhCfglineOptions1,'pm1001lhCfgXfpTable':pm1001lhCfgXfpTable,'pm1001lhCfgXfpEntry':pm1001lhCfgXfpEntry,_t:pm1001lhCfgXfpIndex,'pm1001lhCfgSystConfXfpPortn':pm1001lhCfgSystConfXfpPortn,'pm1001lhCfgDataRateConfXfpPortn':pm1001lhCfgDataRateConfXfpPortn,'pm1001lhCfgOtxtlhTable':pm1001lhCfgOtxtlhTable,'pm1001lhCfgOtxtlhEntry':pm1001lhCfgOtxtlhEntry,_u:pm1001lhCfgOtxtlhIndex,'pm1001lhCfgLineOtxMiscPortn':pm1001lhCfgLineOtxMiscPortn,'pm1001lhCfgLineDitherRatePortn':pm1001lhCfgLineDitherRatePortn,'pm1001lhCfgLineDitherFhzPortn':pm1001lhCfgLineDitherFhzPortn,'pm1001lhCfgLinePwrLaserPortn':pm1001lhCfgLinePwrLaserPortn,'pm1001lhCfgLineFCurrentPortn':pm1001lhCfgLineFCurrentPortn,'pm1001lhCfgLineGridCurrentPortn':pm1001lhCfgLineGridCurrentPortn,'pm1001lhCfgFPortn':pm1001lhCfgFPortn,'pm1001lhCfgReservedPortn':pm1001lhCfgReservedPortn,'pm1001lhCfgLinePhotodiodeModePortn':pm1001lhCfgLinePhotodiodeModePortn,'pm1001lhCfgLinePhotodiodeValuePortn':pm1001lhCfgLinePhotodiodeValuePortn,'pm1001lhCfgLabels':pm1001lhCfgLabels,'pm1001lhCfgLabelclientTable':pm1001lhCfgLabelclientTable,'pm1001lhCfgLabelclientEntry':pm1001lhCfgLabelclientEntry,_v:pm1001lhCfgLabelclientIndex,'pm1001lhCfgLabelclientPortn':pm1001lhCfgLabelclientPortn,'pm1001lhCfgLabellineTable':pm1001lhCfgLabellineTable,'pm1001lhCfgLabellineEntry':pm1001lhCfgLabellineEntry,_w:pm1001lhCfgLabellineIndex,'pm1001lhCfgLabellinePortn':pm1001lhCfgLabellinePortn,'pm1001lhCfgStartuptablefive':pm1001lhCfgStartuptablefive,'pm1001lhCfgOtxtlhcapabilitiesTable':pm1001lhCfgOtxtlhcapabilitiesTable,'pm1001lhCfgOtxtlhcapabilitiesEntry':pm1001lhCfgOtxtlhcapabilitiesEntry,_x:pm1001lhCfgOtxtlhcapabilitiesIndex,'pm1001lhCfgComponentTypePortn':pm1001lhCfgComponentTypePortn,'pm1001lhCfgMiscellaneousPortn':pm1001lhCfgMiscellaneousPortn,'pm1001lhCfgFirstChannelPortn':pm1001lhCfgFirstChannelPortn,'pm1001lhCfgLastChannelPortn':pm1001lhCfgLastChannelPortn,'pm1001lhCfgGridPortn':pm1001lhCfgGridPortn,'pm1001lhCfgWriteConfiguration':pm1001lhCfgWriteConfiguration,'pm1001lhtraps':pm1001lhtraps,_H:pm1001lhtrapBoardNumber,'pm1001lhLineTrapNotUrgentGoesOn':pm1001lhLineTrapNotUrgentGoesOn,'pm1001lhLineTrapNotUrgentGoesOff':pm1001lhLineTrapNotUrgentGoesOff,'pm1001lhLineTrapUrgentGoesOn':pm1001lhLineTrapUrgentGoesOn,'pm1001lhLineTrapUrgentGoesOff':pm1001lhLineTrapUrgentGoesOff,'pm1001lhLineTrapCritGoesOn':pm1001lhLineTrapCritGoesOn,'pm1001lhLineTrapCritGoesOff':pm1001lhLineTrapCritGoesOff,'pm1001lhClientTrapNotUrgentGoesOn':pm1001lhClientTrapNotUrgentGoesOn,'pm1001lhClientTrapNotUrgentGoesOff':pm1001lhClientTrapNotUrgentGoesOff,'pm1001lhClientTrapUrgentGoesOn':pm1001lhClientTrapUrgentGoesOn,'pm1001lhClientTrapUrgentGoesOff':pm1001lhClientTrapUrgentGoesOff,'pm1001lhClientTrapCritGoesOn':pm1001lhClientTrapCritGoesOn,'pm1001lhClientTrapCritGoesOff':pm1001lhClientTrapCritGoesOff,'pm1001lhPowerTrapUrgentGoesOn':pm1001lhPowerTrapUrgentGoesOn,'pm1001lhPowerTrapUrgentGoesOff':pm1001lhPowerTrapUrgentGoesOff,'pm1001lhMonitoring':pm1001lhMonitoring,'pm1001lhMonOther':pm1001lhMonOther,'pm1001lhMonSync':pm1001lhMonSync,'pm1001lhPerfEnable':pm1001lhPerfEnable,'pm1001lhPerf15minSync':pm1001lhPerf15minSync,'pm1001lhPerf24hSync':pm1001lhPerf24hSync,'pm1001lhMonTimeStamp':pm1001lhMonTimeStamp,'pm1001lhPerf15MinShort':pm1001lhPerf15MinShort,'pm1001lhPerf15MinLong':pm1001lhPerf15MinLong,'pm1001lhPerf24HoursShort':pm1001lhPerf24HoursShort,'pm1001lhPerf24HoursLong':pm1001lhPerf24HoursLong,'pm1001lhPerfCurrent15MinElapsedTime':pm1001lhPerfCurrent15MinElapsedTime,'pm1001lhPerfCurrent24HoursElapsedTime':pm1001lhPerfCurrent24HoursElapsedTime,'pm1001lhMonClient':pm1001lhMonClient,'pm1001lhPerfTelecomClientCurrent15StatTable':pm1001lhPerfTelecomClientCurrent15StatTable,'pm1001lhPerfTelecomClientCurrent15StatEntry':pm1001lhPerfTelecomClientCurrent15StatEntry,_y:pm1001lhPerfTelecomClientCurrent15StatIndex,'pm1001lhPerfTelecomClientCurrent15StatInvCvPortn':pm1001lhPerfTelecomClientCurrent15StatInvCvPortn,'pm1001lhPerfTelecomClientCurrent15StatCvValuePortn':pm1001lhPerfTelecomClientCurrent15StatCvValuePortn,'pm1001lhPerfTelecomClientCurrent15StatInvEsPortn':pm1001lhPerfTelecomClientCurrent15StatInvEsPortn,'pm1001lhPerfTelecomClientCurrent15StatEsValuePortn':pm1001lhPerfTelecomClientCurrent15StatEsValuePortn,'pm1001lhPerfTelecomClientCurrent15StatInvSesPortn':pm1001lhPerfTelecomClientCurrent15StatInvSesPortn,'pm1001lhPerfTelecomClientCurrent15StatSesValuePortn':pm1001lhPerfTelecomClientCurrent15StatSesValuePortn,'pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn':pm1001lhPerfTelecomClientCurrent15StatInvSefsPortn,'pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn':pm1001lhPerfTelecomClientCurrent15StatSefsValuePortn,'pm1001lhPerfTelecomClientCurrent15StatInvUasPortn':pm1001lhPerfTelecomClientCurrent15StatInvUasPortn,'pm1001lhPerfTelecomClientCurrent15StatUasValuePortn':pm1001lhPerfTelecomClientCurrent15StatUasValuePortn,'pm1001lhPerfTelecomClientPast15StatHistoryPort1Table':pm1001lhPerfTelecomClientPast15StatHistoryPort1Table,'pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry':pm1001lhPerfTelecomClientPast15StatHistoryPort1Entry,_z:pm1001lhPerfTelecomClientPast15StatHistoryPort1Index,'pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1':pm1001lhPerfTelecomClientPast15StatHistoryInvCvPort1,'pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1':pm1001lhPerfTelecomClientPast15StatHistoryCvValuePort1,'pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1':pm1001lhPerfTelecomClientPast15StatHistoryInvEsPort1,'pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1':pm1001lhPerfTelecomClientPast15StatHistoryEsValuePort1,'pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1':pm1001lhPerfTelecomClientPast15StatHistoryInvSesPort1,'pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1':pm1001lhPerfTelecomClientPast15StatHistorySesValuePort1,'pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1':pm1001lhPerfTelecomClientPast15StatHistoryInvSefsPort1,'pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1':pm1001lhPerfTelecomClientPast15StatHistorySefsValuePort1,'pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1':pm1001lhPerfTelecomClientPast15StatHistoryInvUasPort1,'pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1':pm1001lhPerfTelecomClientPast15StatHistoryUasValuePort1,'pm1001lhPerfTelecomClientCurrent24StatTable':pm1001lhPerfTelecomClientCurrent24StatTable,'pm1001lhPerfTelecomClientCurrent24StatEntry':pm1001lhPerfTelecomClientCurrent24StatEntry,_A0:pm1001lhPerfTelecomClientCurrent24StatIndex,'pm1001lhPerfTelecomClientCurrent24StatInvCvPortn':pm1001lhPerfTelecomClientCurrent24StatInvCvPortn,'pm1001lhPerfTelecomClientCurrent24StatCvValuePortn':pm1001lhPerfTelecomClientCurrent24StatCvValuePortn,'pm1001lhPerfTelecomClientCurrent24StatInvEsPortn':pm1001lhPerfTelecomClientCurrent24StatInvEsPortn,'pm1001lhPerfTelecomClientCurrent24StatEsValuePortn':pm1001lhPerfTelecomClientCurrent24StatEsValuePortn,'pm1001lhPerfTelecomClientCurrent24StatInvSesPortn':pm1001lhPerfTelecomClientCurrent24StatInvSesPortn,'pm1001lhPerfTelecomClientCurrent24StatSesValuePortn':pm1001lhPerfTelecomClientCurrent24StatSesValuePortn,'pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn':pm1001lhPerfTelecomClientCurrent24StatInvSefsPortn,'pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn':pm1001lhPerfTelecomClientCurrent24StatSefsValuePortn,'pm1001lhPerfTelecomClientCurrent24StatInvUasPortn':pm1001lhPerfTelecomClientCurrent24StatInvUasPortn,'pm1001lhPerfTelecomClientCurrent24StatUasValuePortn':pm1001lhPerfTelecomClientCurrent24StatUasValuePortn,'pm1001lhPerfTelecomClientPast24StatHistoryPort1Table':pm1001lhPerfTelecomClientPast24StatHistoryPort1Table,'pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry':pm1001lhPerfTelecomClientPast24StatHistoryPort1Entry,_A1:pm1001lhPerfTelecomClientPast24StatHistoryPort1Index,'pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1':pm1001lhPerfTelecomClientPast24StatHistoryInvCvPort1,'pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1':pm1001lhPerfTelecomClientPast24StatHistoryCvValuePort1,'pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1':pm1001lhPerfTelecomClientPast24StatHistoryInvEsPort1,'pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1':pm1001lhPerfTelecomClientPast24StatHistoryEsValuePort1,'pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1':pm1001lhPerfTelecomClientPast24StatHistoryInvSesPort1,'pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1':pm1001lhPerfTelecomClientPast24StatHistorySesValuePort1,'pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1':pm1001lhPerfTelecomClientPast24StatHistoryInvSefsPort1,'pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1':pm1001lhPerfTelecomClientPast24StatHistorySefsValuePort1,'pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1':pm1001lhPerfTelecomClientPast24StatHistoryInvUasPort1,'pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1':pm1001lhPerfTelecomClientPast24StatHistoryUasValuePort1,'pm1001lhPerfDatacomClientCurrent15StatTable':pm1001lhPerfDatacomClientCurrent15StatTable,'pm1001lhPerfDatacomClientCurrent15StatEntry':pm1001lhPerfDatacomClientCurrent15StatEntry,_A2:pm1001lhPerfDatacomClientCurrent15StatIndex,'pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn':pm1001lhperfdatacomclientCurrent15StatInBytesCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn':pm1001lhperfdatacomclientCurrent15StatInBytesCountPortn,'pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn':pm1001lhperfdatacomclientCurrent15StatInCrcCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn':pm1001lhperfdatacomclientCurrent15StatInCrcCountPortn,'pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatInBroadcastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn':pm1001lhperfdatacomclientCurrent15StatInBroadcastCountPortn,'pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatInMulticastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn':pm1001lhperfdatacomclientCurrent15StatInMulticastCountPortn,'pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatInUnicastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn':pm1001lhperfdatacomclientCurrent15StatInUnicastCountPortn,'pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatInNonunicastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn':pm1001lhperfdatacomclientCurrent15StatInNonunicastCountPortn,'pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn':pm1001lhperfdatacomclientCurrent15StatOutBytesCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn':pm1001lhperfdatacomclientCurrent15StatOutBytesCountPortn,'pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn':pm1001lhperfdatacomclientCurrent15StatOutBroadcastCountPortn,'pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatOutMulticastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn':pm1001lhperfdatacomclientCurrent15StatOutMulticastCountPortn,'pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatOutUnicastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn':pm1001lhperfdatacomclientCurrent15StatOutUnicastCountPortn,'pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn':pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountInvPortn,'pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn':pm1001lhperfdatacomclientCurrent15StatOutNonunicastCountPortn,'pm1001lhPerfDatacomClientPast15StatHistoryPort1Table':pm1001lhPerfDatacomClientPast15StatHistoryPort1Table,'pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry':pm1001lhPerfDatacomClientPast15StatHistoryPort1Entry,_A3:pm1001lhPerfDatacomClientPast15StatHistoryPort1Index,'pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1':pm1001lhperfdatacomclientPast15StatInBytesCountInvPort1,'pm1001lhperfdatacomclientPast15StatInBytesCountPort1':pm1001lhperfdatacomclientPast15StatInBytesCountPort1,'pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1':pm1001lhperfdatacomclientPast15StatInCrcCountInvPort1,'pm1001lhperfdatacomclientPast15StatInCrcCountPort1':pm1001lhperfdatacomclientPast15StatInCrcCountPort1,'pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1':pm1001lhperfdatacomclientPast15StatInBroadcastCountInvPort1,'pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1':pm1001lhperfdatacomclientPast15StatInBroadcastCountPort1,'pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1':pm1001lhperfdatacomclientPast15StatInMulticastCountInvPort1,'pm1001lhperfdatacomclientPast15StatInMulticastCountPort1':pm1001lhperfdatacomclientPast15StatInMulticastCountPort1,'pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1':pm1001lhperfdatacomclientPast15StatInUnicastCountInvPort1,'pm1001lhperfdatacomclientPast15StatInUnicastCountPort1':pm1001lhperfdatacomclientPast15StatInUnicastCountPort1,'pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1':pm1001lhperfdatacomclientPast15StatInNonunicastCountInvPort1,'pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1':pm1001lhperfdatacomclientPast15StatInNonunicastCountPort1,'pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1':pm1001lhperfdatacomclientPast15StatOutBytesCountInvPort1,'pm1001lhperfdatacomclientPast15StatOutBytesCountPort1':pm1001lhperfdatacomclientPast15StatOutBytesCountPort1,'pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1':pm1001lhperfdatacomclientPast15StatOutBroadcastCountInvPort1,'pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1':pm1001lhperfdatacomclientPast15StatOutBroadcastCountPort1,'pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1':pm1001lhperfdatacomclientPast15StatOutMulticastCountInvPort1,'pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1':pm1001lhperfdatacomclientPast15StatOutMulticastCountPort1,'pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1':pm1001lhperfdatacomclientPast15StatOutUnicastCountInvPort1,'pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1':pm1001lhperfdatacomclientPast15StatOutUnicastCountPort1,'pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1':pm1001lhperfdatacomclientPast15StatOutNonunicastCountInvPort1,'pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1':pm1001lhperfdatacomclientPast15StatOutNonunicastCountPort1,'pm1001lhPerfDatacomClientCurrent24StatTable':pm1001lhPerfDatacomClientCurrent24StatTable,'pm1001lhPerfDatacomClientCurrent24StatEntry':pm1001lhPerfDatacomClientCurrent24StatEntry,_A4:pm1001lhPerfDatacomClientCurrent24StatIndex,'pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn':pm1001lhperfdatacomclientCurrent24StatInBytesCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn':pm1001lhperfdatacomclientCurrent24StatInBytesCountPortn,'pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn':pm1001lhperfdatacomclientCurrent24StatInCrcCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn':pm1001lhperfdatacomclientCurrent24StatInCrcCountPortn,'pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatInBroadcastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn':pm1001lhperfdatacomclientCurrent24StatInBroadcastCountPortn,'pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatInMulticastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn':pm1001lhperfdatacomclientCurrent24StatInMulticastCountPortn,'pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatInUnicastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn':pm1001lhperfdatacomclientCurrent24StatInUnicastCountPortn,'pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatInNonunicastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn':pm1001lhperfdatacomclientCurrent24StatInNonunicastCountPortn,'pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn':pm1001lhperfdatacomclientCurrent24StatOutBytesCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn':pm1001lhperfdatacomclientCurrent24StatOutBytesCountPortn,'pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn':pm1001lhperfdatacomclientCurrent24StatOutBroadcastCountPortn,'pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatOutMulticastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn':pm1001lhperfdatacomclientCurrent24StatOutMulticastCountPortn,'pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatOutUnicastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn':pm1001lhperfdatacomclientCurrent24StatOutUnicastCountPortn,'pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn':pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountInvPortn,'pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn':pm1001lhperfdatacomclientCurrent24StatOutNonunicastCountPortn,'pm1001lhPerfDatacomClientPast24StatHistoryPort1Table':pm1001lhPerfDatacomClientPast24StatHistoryPort1Table,'pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry':pm1001lhPerfDatacomClientPast24StatHistoryPort1Entry,_A5:pm1001lhPerfDatacomClientPast24StatHistoryPort1Index,'pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1':pm1001lhperfdatacomclientPast24StatInBytesCountInvPort1,'pm1001lhperfdatacomclientPast24StatInBytesCountPort1':pm1001lhperfdatacomclientPast24StatInBytesCountPort1,'pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1':pm1001lhperfdatacomclientPast24StatInCrcCountInvPort1,'pm1001lhperfdatacomclientPast24StatInCrcCountPort1':pm1001lhperfdatacomclientPast24StatInCrcCountPort1,'pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1':pm1001lhperfdatacomclientPast24StatInBroadcastCountInvPort1,'pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1':pm1001lhperfdatacomclientPast24StatInBroadcastCountPort1,'pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1':pm1001lhperfdatacomclientPast24StatInMulticastCountInvPort1,'pm1001lhperfdatacomclientPast24StatInMulticastCountPort1':pm1001lhperfdatacomclientPast24StatInMulticastCountPort1,'pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1':pm1001lhperfdatacomclientPast24StatInUnicastCountInvPort1,'pm1001lhperfdatacomclientPast24StatInUnicastCountPort1':pm1001lhperfdatacomclientPast24StatInUnicastCountPort1,'pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1':pm1001lhperfdatacomclientPast24StatInNonunicastCountInvPort1,'pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1':pm1001lhperfdatacomclientPast24StatInNonunicastCountPort1,'pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1':pm1001lhperfdatacomclientPast24StatOutBytesCountInvPort1,'pm1001lhperfdatacomclientPast24StatOutBytesCountPort1':pm1001lhperfdatacomclientPast24StatOutBytesCountPort1,'pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1':pm1001lhperfdatacomclientPast24StatOutBroadcastCountInvPort1,'pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1':pm1001lhperfdatacomclientPast24StatOutBroadcastCountPort1,'pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1':pm1001lhperfdatacomclientPast24StatOutMulticastCountInvPort1,'pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1':pm1001lhperfdatacomclientPast24StatOutMulticastCountPort1,'pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1':pm1001lhperfdatacomclientPast24StatOutUnicastCountInvPort1,'pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1':pm1001lhperfdatacomclientPast24StatOutUnicastCountPort1,'pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1':pm1001lhperfdatacomclientPast24StatOutNonunicastCountInvPort1,'pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1':pm1001lhperfdatacomclientPast24StatOutNonunicastCountPort1,'pm1001lhMonLine':pm1001lhMonLine,'pm1001lhPerfTelecomLineCurrent15StatTable':pm1001lhPerfTelecomLineCurrent15StatTable,'pm1001lhPerfTelecomLineCurrent15StatEntry':pm1001lhPerfTelecomLineCurrent15StatEntry,_A6:pm1001lhPerfTelecomLineCurrent15StatIndex,'pm1001lhPerfTelecomLineCurrent15StatInvCvPortn':pm1001lhPerfTelecomLineCurrent15StatInvCvPortn,'pm1001lhPerfTelecomLineCurrent15StatCvValuePortn':pm1001lhPerfTelecomLineCurrent15StatCvValuePortn,'pm1001lhPerfTelecomLineCurrent15StatInvEsPortn':pm1001lhPerfTelecomLineCurrent15StatInvEsPortn,'pm1001lhPerfTelecomLineCurrent15StatEsValuePortn':pm1001lhPerfTelecomLineCurrent15StatEsValuePortn,'pm1001lhPerfTelecomLineCurrent15StatInvSesPortn':pm1001lhPerfTelecomLineCurrent15StatInvSesPortn,'pm1001lhPerfTelecomLineCurrent15StatSesValuePortn':pm1001lhPerfTelecomLineCurrent15StatSesValuePortn,'pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn':pm1001lhPerfTelecomLineCurrent15StatInvSefsPortn,'pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn':pm1001lhPerfTelecomLineCurrent15StatSefsValuePortn,'pm1001lhPerfTelecomLineCurrent15StatInvUasPortn':pm1001lhPerfTelecomLineCurrent15StatInvUasPortn,'pm1001lhPerfTelecomLineCurrent15StatUasValuePortn':pm1001lhPerfTelecomLineCurrent15StatUasValuePortn,'pm1001lhPerfTelecomLinePast15StatHistoryPort1Table':pm1001lhPerfTelecomLinePast15StatHistoryPort1Table,'pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry':pm1001lhPerfTelecomLinePast15StatHistoryPort1Entry,_A7:pm1001lhPerfTelecomLinePast15StatHistoryPort1Index,'pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1':pm1001lhPerfTelecomLinePast15StatHistoryInvCvPort1,'pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1':pm1001lhPerfTelecomLinePast15StatHistoryCvValuePort1,'pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1':pm1001lhPerfTelecomLinePast15StatHistoryInvEsPort1,'pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1':pm1001lhPerfTelecomLinePast15StatHistoryEsValuePort1,'pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1':pm1001lhPerfTelecomLinePast15StatHistoryInvSesPort1,'pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1':pm1001lhPerfTelecomLinePast15StatHistorySesValuePort1,'pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1':pm1001lhPerfTelecomLinePast15StatHistoryInvSefsPort1,'pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1':pm1001lhPerfTelecomLinePast15StatHistorySefsValuePort1,'pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1':pm1001lhPerfTelecomLinePast15StatHistoryInvUasPort1,'pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1':pm1001lhPerfTelecomLinePast15StatHistoryUasValuePort1,'pm1001lhPerfTelecomLineCurrent24StatTable':pm1001lhPerfTelecomLineCurrent24StatTable,'pm1001lhPerfTelecomLineCurrent24StatEntry':pm1001lhPerfTelecomLineCurrent24StatEntry,_A8:pm1001lhPerfTelecomLineCurrent24StatIndex,'pm1001lhPerfTelecomLineCurrent24StatInvCvPortn':pm1001lhPerfTelecomLineCurrent24StatInvCvPortn,'pm1001lhPerfTelecomLineCurrent24StatCvValuePortn':pm1001lhPerfTelecomLineCurrent24StatCvValuePortn,'pm1001lhPerfTelecomLineCurrent24StatInvEsPortn':pm1001lhPerfTelecomLineCurrent24StatInvEsPortn,'pm1001lhPerfTelecomLineCurrent24StatEsValuePortn':pm1001lhPerfTelecomLineCurrent24StatEsValuePortn,'pm1001lhPerfTelecomLineCurrent24StatInvSesPortn':pm1001lhPerfTelecomLineCurrent24StatInvSesPortn,'pm1001lhPerfTelecomLineCurrent24StatSesValuePortn':pm1001lhPerfTelecomLineCurrent24StatSesValuePortn,'pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn':pm1001lhPerfTelecomLineCurrent24StatInvSefsPortn,'pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn':pm1001lhPerfTelecomLineCurrent24StatSefsValuePortn,'pm1001lhPerfTelecomLineCurrent24StatInvUasPortn':pm1001lhPerfTelecomLineCurrent24StatInvUasPortn,'pm1001lhPerfTelecomLineCurrent24StatUasValuePortn':pm1001lhPerfTelecomLineCurrent24StatUasValuePortn,'pm1001lhPerfTelecomLinePast24StatHistoryPort1Table':pm1001lhPerfTelecomLinePast24StatHistoryPort1Table,'pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry':pm1001lhPerfTelecomLinePast24StatHistoryPort1Entry,_A9:pm1001lhPerfTelecomLinePast24StatHistoryPort1Index,'pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1':pm1001lhPerfTelecomLinePast24StatHistoryInvCvPort1,'pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1':pm1001lhPerfTelecomLinePast24StatHistoryCvValuePort1,'pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1':pm1001lhPerfTelecomLinePast24StatHistoryInvEsPort1,'pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1':pm1001lhPerfTelecomLinePast24StatHistoryEsValuePort1,'pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1':pm1001lhPerfTelecomLinePast24StatHistoryInvSesPort1,'pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1':pm1001lhPerfTelecomLinePast24StatHistorySesValuePort1,'pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1':pm1001lhPerfTelecomLinePast24StatHistoryInvSefsPort1,'pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1':pm1001lhPerfTelecomLinePast24StatHistorySefsValuePort1,'pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1':pm1001lhPerfTelecomLinePast24StatHistoryInvUasPort1,'pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1':pm1001lhPerfTelecomLinePast24StatHistoryUasValuePort1,'pm1001lhRmon':pm1001lhRmon,'pm1001lhRmonClient':pm1001lhRmonClient,'pm1001lhMonupRmonByteCntTable':pm1001lhMonupRmonByteCntTable,'pm1001lhMonupRmonByteCntEntry':pm1001lhMonupRmonByteCntEntry,_AA:pm1001lhMonupRmonByteCntIndex,'pm1001lhMonupRmonByteCntValuePortn':pm1001lhMonupRmonByteCntValuePortn,'pm1001lhMonupRmonByteCntErrorPortn':pm1001lhMonupRmonByteCntErrorPortn,'pm1001lhMonupRmonByteCntOverloadPortn':pm1001lhMonupRmonByteCntOverloadPortn,'pm1001lhMonupRmonCrcErrorCntTable':pm1001lhMonupRmonCrcErrorCntTable,'pm1001lhMonupRmonCrcErrorCntEntry':pm1001lhMonupRmonCrcErrorCntEntry,_AB:pm1001lhMonupRmonCrcErrorCntIndex,'pm1001lhMonupRmonCrcErrorCntValuePortn':pm1001lhMonupRmonCrcErrorCntValuePortn,'pm1001lhMonupRmonCrcErrorCntErrorPortn':pm1001lhMonupRmonCrcErrorCntErrorPortn,'pm1001lhMonupRmonCrcErrorCntOverloadPortn':pm1001lhMonupRmonCrcErrorCntOverloadPortn,'pm1001lhMonupRmonPacketsCntTable':pm1001lhMonupRmonPacketsCntTable,'pm1001lhMonupRmonPacketsCntEntry':pm1001lhMonupRmonPacketsCntEntry,_AC:pm1001lhMonupRmonPacketsCntIndex,'pm1001lhMonupRmonPacketsCntValuePortn':pm1001lhMonupRmonPacketsCntValuePortn,'pm1001lhMonupRmonPacketsCntErrorPortn':pm1001lhMonupRmonPacketsCntErrorPortn,'pm1001lhMonupRmonPacketsCntOverloadPortn':pm1001lhMonupRmonPacketsCntOverloadPortn,'pm1001lhMonupRmonBroadcastCntTable':pm1001lhMonupRmonBroadcastCntTable,'pm1001lhMonupRmonBroadcastCntEntry':pm1001lhMonupRmonBroadcastCntEntry,_AD:pm1001lhMonupRmonBroadcastCntIndex,'pm1001lhMonupRmonBroadcastCntValuePortn':pm1001lhMonupRmonBroadcastCntValuePortn,'pm1001lhMonupRmonBroadcastCntErrorPortn':pm1001lhMonupRmonBroadcastCntErrorPortn,'pm1001lhMonupRmonBroadcastCntOverloadPortn':pm1001lhMonupRmonBroadcastCntOverloadPortn,'pm1001lhMonupRmonMulticastCntTable':pm1001lhMonupRmonMulticastCntTable,'pm1001lhMonupRmonMulticastCntEntry':pm1001lhMonupRmonMulticastCntEntry,_AE:pm1001lhMonupRmonMulticastCntIndex,'pm1001lhMonupRmonMulticastCntValuePortn':pm1001lhMonupRmonMulticastCntValuePortn,'pm1001lhMonupRmonMulticastCntErrorPortn':pm1001lhMonupRmonMulticastCntErrorPortn,'pm1001lhMonupRmonMulticastCntOverloadPortn':pm1001lhMonupRmonMulticastCntOverloadPortn,'pm1001lhMonupRmonTimerCntTable':pm1001lhMonupRmonTimerCntTable,'pm1001lhMonupRmonTimerCntEntry':pm1001lhMonupRmonTimerCntEntry,_AF:pm1001lhMonupRmonTimerCntIndex,'pm1001lhMonupRmonTimerCntValuePortn':pm1001lhMonupRmonTimerCntValuePortn,'pm1001lhMonupRmonTimerCntErrorPortn':pm1001lhMonupRmonTimerCntErrorPortn,'pm1001lhMonupRmonTimerCntOverloadPortn':pm1001lhMonupRmonTimerCntOverloadPortn,'pm1001lhMonupRmonPauseFrameCntTable':pm1001lhMonupRmonPauseFrameCntTable,'pm1001lhMonupRmonPauseFrameCntEntry':pm1001lhMonupRmonPauseFrameCntEntry,_AG:pm1001lhMonupRmonPauseFrameCntIndex,'pm1001lhMonupRmonPauseFrameCntValuePortn':pm1001lhMonupRmonPauseFrameCntValuePortn,'pm1001lhMonupRmonPauseFrameCntErrorPortn':pm1001lhMonupRmonPauseFrameCntErrorPortn,'pm1001lhMonupRmonPauseFrameCntOverloadPortn':pm1001lhMonupRmonPauseFrameCntOverloadPortn,'pm1001lhMonupRmonDropFrameCntTable':pm1001lhMonupRmonDropFrameCntTable,'pm1001lhMonupRmonDropFrameCntEntry':pm1001lhMonupRmonDropFrameCntEntry,_AH:pm1001lhMonupRmonDropFrameCntIndex,'pm1001lhMonupRmonDropFrameCntValuePortn':pm1001lhMonupRmonDropFrameCntValuePortn,'pm1001lhMonupRmonDropFrameCntErrorPortn':pm1001lhMonupRmonDropFrameCntErrorPortn,'pm1001lhMonupRmonDropFrameCntOverloadPortn':pm1001lhMonupRmonDropFrameCntOverloadPortn,'pm1001lhMonupRmonBitsCntTable':pm1001lhMonupRmonBitsCntTable,'pm1001lhMonupRmonBitsCntEntry':pm1001lhMonupRmonBitsCntEntry,_AI:pm1001lhMonupRmonBitsCntIndex,'pm1001lhMonupRmonBitsCntValuePortn':pm1001lhMonupRmonBitsCntValuePortn,'pm1001lhMonupRmonBitsCntErrorPortn':pm1001lhMonupRmonBitsCntErrorPortn,'pm1001lhMonupRmonBitsCntOverloadPortn':pm1001lhMonupRmonBitsCntOverloadPortn,'pm1001lhMonupRmonUnicastCntTable':pm1001lhMonupRmonUnicastCntTable,'pm1001lhMonupRmonUnicastCntEntry':pm1001lhMonupRmonUnicastCntEntry,_AJ:pm1001lhMonupRmonUnicastCntIndex,'pm1001lhMonupRmonUnicastCntValuePortn':pm1001lhMonupRmonUnicastCntValuePortn,'pm1001lhMonupRmonUnicastCntErrorPortn':pm1001lhMonupRmonUnicastCntErrorPortn,'pm1001lhMonupRmonUnicastCntOverloadPortn':pm1001lhMonupRmonUnicastCntOverloadPortn,'pm1001lhMonupRmonNonUnicastCntTable':pm1001lhMonupRmonNonUnicastCntTable,'pm1001lhMonupRmonNonUnicastCntEntry':pm1001lhMonupRmonNonUnicastCntEntry,_AK:pm1001lhMonupRmonNonUnicastCntIndex,'pm1001lhMonupRmonNonUnicastCntValuePortn':pm1001lhMonupRmonNonUnicastCntValuePortn,'pm1001lhMonupRmonNonUnicastCntErrorPortn':pm1001lhMonupRmonNonUnicastCntErrorPortn,'pm1001lhMonupRmonNonUnicastCntOverloadPortn':pm1001lhMonupRmonNonUnicastCntOverloadPortn,'pm1001lhMondwRmonByteCntTable':pm1001lhMondwRmonByteCntTable,'pm1001lhMondwRmonByteCntEntry':pm1001lhMondwRmonByteCntEntry,_AL:pm1001lhMondwRmonByteCntIndex,'pm1001lhMondwRmonByteCntValuePortn':pm1001lhMondwRmonByteCntValuePortn,'pm1001lhMondwRmonByteCntErrorPortn':pm1001lhMondwRmonByteCntErrorPortn,'pm1001lhMondwRmonByteCntOverloadPortn':pm1001lhMondwRmonByteCntOverloadPortn,'pm1001lhMondwRmonCrcErrorCntTable':pm1001lhMondwRmonCrcErrorCntTable,'pm1001lhMondwRmonCrcErrorCntEntry':pm1001lhMondwRmonCrcErrorCntEntry,_AM:pm1001lhMondwRmonCrcErrorCntIndex,'pm1001lhMondwRmonCrcErrorCntValuePortn':pm1001lhMondwRmonCrcErrorCntValuePortn,'pm1001lhMondwRmonCrcErrorCntErrorPortn':pm1001lhMondwRmonCrcErrorCntErrorPortn,'pm1001lhMondwRmonCrcErrorCntOverloadPortn':pm1001lhMondwRmonCrcErrorCntOverloadPortn,'pm1001lhMondwRmonPacketsCntTable':pm1001lhMondwRmonPacketsCntTable,'pm1001lhMondwRmonPacketsCntEntry':pm1001lhMondwRmonPacketsCntEntry,_AN:pm1001lhMondwRmonPacketsCntIndex,'pm1001lhMondwRmonPacketsCntValuePortn':pm1001lhMondwRmonPacketsCntValuePortn,'pm1001lhMondwRmonPacketsCntErrorPortn':pm1001lhMondwRmonPacketsCntErrorPortn,'pm1001lhMondwRmonPacketsCntOverloadPortn':pm1001lhMondwRmonPacketsCntOverloadPortn,'pm1001lhMondwRmonBroadcastCntTable':pm1001lhMondwRmonBroadcastCntTable,'pm1001lhMondwRmonBroadcastCntEntry':pm1001lhMondwRmonBroadcastCntEntry,_AO:pm1001lhMondwRmonBroadcastCntIndex,'pm1001lhMondwRmonBroadcastCntValuePortn':pm1001lhMondwRmonBroadcastCntValuePortn,'pm1001lhMondwRmonBroadcastCntErrorPortn':pm1001lhMondwRmonBroadcastCntErrorPortn,'pm1001lhMondwRmonBroadcastCntOverloadPortn':pm1001lhMondwRmonBroadcastCntOverloadPortn,'pm1001lhMondwRmonMulticastCntTable':pm1001lhMondwRmonMulticastCntTable,'pm1001lhMondwRmonMulticastCntEntry':pm1001lhMondwRmonMulticastCntEntry,_AP:pm1001lhMondwRmonMulticastCntIndex,'pm1001lhMondwRmonMulticastCntValuePortn':pm1001lhMondwRmonMulticastCntValuePortn,'pm1001lhMondwRmonMulticastCntErrorPortn':pm1001lhMondwRmonMulticastCntErrorPortn,'pm1001lhMondwRmonMulticastCntOverloadPortn':pm1001lhMondwRmonMulticastCntOverloadPortn,'pm1001lhMondwRmonPauseFrameCntTable':pm1001lhMondwRmonPauseFrameCntTable,'pm1001lhMondwRmonPauseFrameCntEntry':pm1001lhMondwRmonPauseFrameCntEntry,_AQ:pm1001lhMondwRmonPauseFrameCntIndex,'pm1001lhMondwRmonPauseFrameCntValuePortn':pm1001lhMondwRmonPauseFrameCntValuePortn,'pm1001lhMondwRmonPauseFrameCntErrorPortn':pm1001lhMondwRmonPauseFrameCntErrorPortn,'pm1001lhMondwRmonPauseFrameCntOverloadPortn':pm1001lhMondwRmonPauseFrameCntOverloadPortn,'pm1001lhMondwRmonTimerCntTable':pm1001lhMondwRmonTimerCntTable,'pm1001lhMondwRmonTimerCntEntry':pm1001lhMondwRmonTimerCntEntry,_AR:pm1001lhMondwRmonTimerCntIndex,'pm1001lhMondwRmonTimerCntValuePortn':pm1001lhMondwRmonTimerCntValuePortn,'pm1001lhMondwRmonTimerCntErrorPortn':pm1001lhMondwRmonTimerCntErrorPortn,'pm1001lhMondwRmonTimerCntOverloadPortn':pm1001lhMondwRmonTimerCntOverloadPortn,'pm1001lhMondwRmonBitsCntTable':pm1001lhMondwRmonBitsCntTable,'pm1001lhMondwRmonBitsCntEntry':pm1001lhMondwRmonBitsCntEntry,_AS:pm1001lhMondwRmonBitsCntIndex,'pm1001lhMondwRmonBitsCntValuePortn':pm1001lhMondwRmonBitsCntValuePortn,'pm1001lhMondwRmonBitsCntErrorPortn':pm1001lhMondwRmonBitsCntErrorPortn,'pm1001lhMondwRmonBitsCntOverloadPortn':pm1001lhMondwRmonBitsCntOverloadPortn,'pm1001lhMondwRmonUnicastCntTable':pm1001lhMondwRmonUnicastCntTable,'pm1001lhMondwRmonUnicastCntEntry':pm1001lhMondwRmonUnicastCntEntry,_AT:pm1001lhMondwRmonUnicastCntIndex,'pm1001lhMondwRmonUnicastCntValuePortn':pm1001lhMondwRmonUnicastCntValuePortn,'pm1001lhMondwRmonUnicastCntErrorPortn':pm1001lhMondwRmonUnicastCntErrorPortn,'pm1001lhMondwRmonUnicastCntOverloadPortn':pm1001lhMondwRmonUnicastCntOverloadPortn,'pm1001lhMondwRmonNonUnicastCntTable':pm1001lhMondwRmonNonUnicastCntTable,'pm1001lhMondwRmonNonUnicastCntEntry':pm1001lhMondwRmonNonUnicastCntEntry,_AU:pm1001lhMondwRmonNonUnicastCntIndex,'pm1001lhMondwRmonNonUnicastCntValuePortn':pm1001lhMondwRmonNonUnicastCntValuePortn,'pm1001lhMondwRmonNonUnicastCntErrorPortn':pm1001lhMondwRmonNonUnicastCntErrorPortn,'pm1001lhMondwRmonNonUnicastCntOverloadPortn':pm1001lhMondwRmonNonUnicastCntOverloadPortn,'pm1001lhRmonLine':pm1001lhRmonLine,'pm1001lhRmonOther':pm1001lhRmonOther,'pm1001lhMonCountersReset':pm1001lhMonCountersReset,'pm1001lhMonCountersStop':pm1001lhMonCountersStop})