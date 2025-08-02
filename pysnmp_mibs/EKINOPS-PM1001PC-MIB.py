_AN='pm1001pcCfgLabellineIndex'
_AM='pm1001pcCfgLabelclientIndex'
_AL='pm1001pcCfgXfpIndex'
_AK='pm1001pcCfgClientStartupIndex'
_AJ='pm1001pcCfgClientcaiscsfIndex'
_AI='pm1001pcMondwRmonBitsCntSIndex'
_AH='pm1001pcMondwRmonPauseFrameCntSIndex'
_AG='pm1001pcMondwRmonMulticastCntSIndex'
_AF='pm1001pcMondwRmonBroadcastCntSIndex'
_AE='pm1001pcMondwRmonPacketsCntSIndex'
_AD='pm1001pcMondwRmonCrcErrorCntSIndex'
_AC='pm1001pcMondwRmonByteCntSIndex'
_AB='pm1001pcMonupRmonBitsCntSIndex'
_AA='pm1001pcMonupRmonDropFrameCntSIndex'
_A9='pm1001pcMonupRmonPauseFrameCntSIndex'
_A8='pm1001pcMonupRmonMulticastCntSIndex'
_A7='pm1001pcMonupRmonBroadcastCntSIndex'
_A6='pm1001pcMonupRmonPacketsCntSIndex'
_A5='pm1001pcMonupRmonCrcErrorCntSIndex'
_A4='pm1001pcMonupRmonByteCntSIndex'
_A3='pm1001pcMondwRmonBitsCntIndex'
_A2='pm1001pcMondwRmonTimerCntIndex'
_A1='pm1001pcMondwRmonPauseFrameCntIndex'
_A0='pm1001pcMondwRmonMulticastCntIndex'
_z='pm1001pcMondwRmonBroadcastCntIndex'
_y='pm1001pcMondwRmonPacketsCntIndex'
_x='pm1001pcMondwRmonCrcErrorCntIndex'
_w='pm1001pcMondwRmonByteCntIndex'
_v='pm1001pcMonupRmonBitsCntIndex'
_u='pm1001pcMonupRmonDropFrameCntIndex'
_t='pm1001pcMonupRmonPauseFrameCntIndex'
_s='pm1001pcMonupRmonTimerCntIndex'
_r='pm1001pcMonupRmonMulticastCntIndex'
_q='pm1001pcMonupRmonBroadcastCntIndex'
_p='pm1001pcMonupRmonPacketsCntIndex'
_o='pm1001pcMonupRmonCrcErrorCntIndex'
_n='pm1001pcMonupRmonByteCntIndex'
_m='pm1001pcCtrllineLoopTransceiverIndex'
_l='pm1001pcCtrlxfpLineXfiLoopIndex'
_k='pm1001pcCtrlxfpLineLoopIndex'
_j='pm1001pcCtrlxfpOnoffIndex'
_i='pm1001pcCtrlxfpXfiLoopIndex'
_h='pm1001pcCtrlclientAccessTermLoopIndex'
_g='pm1001pcCtrlflowControlIndex'
_f='pm1001pcCtrlcaisDwInsIndex'
_e='pm1001pcCtrlcsfUpInsIndex'
_d='pm1001pcCtrlxfpOffCtrlIndex'
_c='pm1001pcCtrlportOosModeIndex'
_b='pm1001pcCtrlaccessLoopIndex'
_a='pm1001pcCntlineDfrmErrCntSIndex'
_Z='pm1001pcCntlineDfrmPrimErrCntIndex'
_Y='pm1001pcCntlineDfrmTimCntIndex'
_X='pm1001pcCntlineDfrmErrCntIndex'
_W='pm1001pcCntclientDwTimCntIndex'
_V='pm1001pcCntclientDwErrCntIndex'
_U='pm1001pcCntclientUpTimCntIndex'
_T='pm1001pcCntclientUpErrCntIndex'
_S='pm1001pcAlmDefFuseA'
_R='pm1001pcAlmDefFuseB'
_Q='pm1001pcAlmClientHwFail'
_P='pm1001pcAlmClientFail'
_O='pm1001pcAlmClientXfpDdmAlm'
_N='pm1001pcAlmClientXfpDdmWarning'
_M='pm1001pcAlmLineHwFail'
_L='pm1001pcAlmLineFail'
_K='pm1001pcAlmLineDdmAlm'
_J='pm1001pcAlmLineDdmWarning'
_I='DisplayString'
_H='deprecated'
_G='pm1001pctrapBoardNumber'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='EKINOPS-PM1001PC-MIB'
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
modulepm1001pc=ModuleIdentity((1,3,6,1,4,1,20044,12))
if mibBuilder.loadTexts:modulepm1001pc.setRevisions(('2006-01-19 00:00','2007-02-21 00:00','2007-06-29 00:00','2007-12-03 00:00','2009-03-05 00:00','2009-04-07 00:00','2009-04-09 00:00','2009-10-05 00:00','2010-03-01 00:00','2010-10-19 00:00','2010-11-10 00:00','2012-07-03 00:00','2013-04-03 00:00','2014-03-25 00:00','2014-12-24 00:00','2016-05-20 00:00'))
_Pm1001pcalarms_ObjectIdentity=ObjectIdentity
pm1001pcalarms=_Pm1001pcalarms_ObjectIdentity((1,3,6,1,4,1,20044,12,2))
_Pm1001pcAlmOther_ObjectIdentity=ObjectIdentity
pm1001pcAlmOther=_Pm1001pcAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1))
_Pm1001pcAlmOtherNurg_ObjectIdentity=ObjectIdentity
pm1001pcAlmOtherNurg=_Pm1001pcAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,1))
_Pm1001pcAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm1001pcAlmsynthAlm2=_Pm1001pcAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,1,2))
_Pm1001pcAlmConfTableSave_Type=EkiOnOff
_Pm1001pcAlmConfTableSave_Object=MibScalar
pm1001pcAlmConfTableSave=_Pm1001pcAlmConfTableSave_Object((1,3,6,1,4,1,20044,12,2,1,1,2,1),_Pm1001pcAlmConfTableSave_Type())
pm1001pcAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmConfTableSave.setStatus(_A)
_Pm1001pcAlmInvUpload_Type=EkiOnOff
_Pm1001pcAlmInvUpload_Object=MibScalar
pm1001pcAlmInvUpload=_Pm1001pcAlmInvUpload_Object((1,3,6,1,4,1,20044,12,2,1,1,2,2),_Pm1001pcAlmInvUpload_Type())
pm1001pcAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmInvUpload.setStatus(_A)
_Pm1001pcAlmConfTableLoad_Type=EkiOnOff
_Pm1001pcAlmConfTableLoad_Object=MibScalar
pm1001pcAlmConfTableLoad=_Pm1001pcAlmConfTableLoad_Object((1,3,6,1,4,1,20044,12,2,1,1,2,3),_Pm1001pcAlmConfTableLoad_Type())
pm1001pcAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmConfTableLoad.setStatus(_A)
_Pm1001pcAlmCorrelatOff_Type=EkiOnOff
_Pm1001pcAlmCorrelatOff_Object=MibScalar
pm1001pcAlmCorrelatOff=_Pm1001pcAlmCorrelatOff_Object((1,3,6,1,4,1,20044,12,2,1,1,2,4),_Pm1001pcAlmCorrelatOff_Type())
pm1001pcAlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmCorrelatOff.setStatus(_A)
_Pm1001pcAlmMaintenanceOn_Type=EkiOnOff
_Pm1001pcAlmMaintenanceOn_Object=MibScalar
pm1001pcAlmMaintenanceOn=_Pm1001pcAlmMaintenanceOn_Object((1,3,6,1,4,1,20044,12,2,1,1,2,5),_Pm1001pcAlmMaintenanceOn_Type())
pm1001pcAlmMaintenanceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmMaintenanceOn.setStatus(_A)
_Pm1001pcAlmOtherUrg_ObjectIdentity=ObjectIdentity
pm1001pcAlmOtherUrg=_Pm1001pcAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,2))
_Pm1001pcAlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pm1001pcAlmmodInitFailLevel2=_Pm1001pcAlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,2,194))
_Pm1001pcAlmLedFail_Type=EkiOnOff
_Pm1001pcAlmLedFail_Object=MibScalar
pm1001pcAlmLedFail=_Pm1001pcAlmLedFail_Object((1,3,6,1,4,1,20044,12,2,1,2,194,1),_Pm1001pcAlmLedFail_Type())
pm1001pcAlmLedFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLedFail.setStatus(_A)
_Pm1001pcAlmNextColdBootForced_Type=EkiOnOff
_Pm1001pcAlmNextColdBootForced_Object=MibScalar
pm1001pcAlmNextColdBootForced=_Pm1001pcAlmNextColdBootForced_Object((1,3,6,1,4,1,20044,12,2,1,2,194,2),_Pm1001pcAlmNextColdBootForced_Type())
pm1001pcAlmNextColdBootForced.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmNextColdBootForced.setStatus(_A)
_Pm1001pcAlmBootUndone_Type=EkiOnOff
_Pm1001pcAlmBootUndone_Object=MibScalar
pm1001pcAlmBootUndone=_Pm1001pcAlmBootUndone_Object((1,3,6,1,4,1,20044,12,2,1,2,194,3),_Pm1001pcAlmBootUndone_Type())
pm1001pcAlmBootUndone.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmBootUndone.setStatus(_A)
_Pm1001pcAlmResetHwInitFail_Type=EkiOnOff
_Pm1001pcAlmResetHwInitFail_Object=MibScalar
pm1001pcAlmResetHwInitFail=_Pm1001pcAlmResetHwInitFail_Object((1,3,6,1,4,1,20044,12,2,1,2,194,4),_Pm1001pcAlmResetHwInitFail_Type())
pm1001pcAlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmResetHwInitFail.setStatus(_A)
_Pm1001pcAlmSwInitFail_Type=EkiOnOff
_Pm1001pcAlmSwInitFail_Object=MibScalar
pm1001pcAlmSwInitFail=_Pm1001pcAlmSwInitFail_Object((1,3,6,1,4,1,20044,12,2,1,2,194,5),_Pm1001pcAlmSwInitFail_Type())
pm1001pcAlmSwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmSwInitFail.setStatus(_A)
_Pm1001pcAlmmodInitFailLevel3_ObjectIdentity=ObjectIdentity
pm1001pcAlmmodInitFailLevel3=_Pm1001pcAlmmodInitFailLevel3_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,2,195))
_Pm1001pcAlmGwIdentFail_Type=EkiOnOff
_Pm1001pcAlmGwIdentFail_Object=MibScalar
pm1001pcAlmGwIdentFail=_Pm1001pcAlmGwIdentFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,1),_Pm1001pcAlmGwIdentFail_Type())
pm1001pcAlmGwIdentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmGwIdentFail.setStatus(_A)
_Pm1001pcAlmObmTypeReadFail_Type=EkiOnOff
_Pm1001pcAlmObmTypeReadFail_Object=MibScalar
pm1001pcAlmObmTypeReadFail=_Pm1001pcAlmObmTypeReadFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,2),_Pm1001pcAlmObmTypeReadFail_Type())
pm1001pcAlmObmTypeReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmObmTypeReadFail.setStatus(_A)
_Pm1001pcAlmInitModuleFail_Type=EkiOnOff
_Pm1001pcAlmInitModuleFail_Object=MibScalar
pm1001pcAlmInitModuleFail=_Pm1001pcAlmInitModuleFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,3),_Pm1001pcAlmInitModuleFail_Type())
pm1001pcAlmInitModuleFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmInitModuleFail.setStatus(_A)
_Pm1001pcAlmXfp1InitFail_Type=EkiOnOff
_Pm1001pcAlmXfp1InitFail_Object=MibScalar
pm1001pcAlmXfp1InitFail=_Pm1001pcAlmXfp1InitFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,5),_Pm1001pcAlmXfp1InitFail_Type())
pm1001pcAlmXfp1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmXfp1InitFail.setStatus(_A)
_Pm1001pcAlmXfp2InitFail_Type=EkiOnOff
_Pm1001pcAlmXfp2InitFail_Object=MibScalar
pm1001pcAlmXfp2InitFail=_Pm1001pcAlmXfp2InitFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,6),_Pm1001pcAlmXfp2InitFail_Type())
pm1001pcAlmXfp2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmXfp2InitFail.setStatus(_A)
_Pm1001pcAlmLineInitFail_Type=EkiOnOff
_Pm1001pcAlmLineInitFail_Object=MibScalar
pm1001pcAlmLineInitFail=_Pm1001pcAlmLineInitFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,7),_Pm1001pcAlmLineInitFail_Type())
pm1001pcAlmLineInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineInitFail.setStatus(_A)
_Pm1001pcAlmClientInitFail_Type=EkiOnOff
_Pm1001pcAlmClientInitFail_Object=MibScalar
pm1001pcAlmClientInitFail=_Pm1001pcAlmClientInitFail_Object((1,3,6,1,4,1,20044,12,2,1,2,195,9),_Pm1001pcAlmClientInitFail_Type())
pm1001pcAlmClientInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientInitFail.setStatus(_A)
_Pm1001pcAlmOtherCrit_ObjectIdentity=ObjectIdentity
pm1001pcAlmOtherCrit=_Pm1001pcAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,3))
_Pm1001pcAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm1001pcAlmsynthAlm0=_Pm1001pcAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,12,2,1,3,0))
_Pm1001pcAlmModGlobFail_Type=EkiOnOff
_Pm1001pcAlmModGlobFail_Object=MibScalar
pm1001pcAlmModGlobFail=_Pm1001pcAlmModGlobFail_Object((1,3,6,1,4,1,20044,12,2,1,3,0,9),_Pm1001pcAlmModGlobFail_Type())
pm1001pcAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmModGlobFail.setStatus(_A)
_Pm1001pcAlmDefFuseA_Type=EkiOnOff
_Pm1001pcAlmDefFuseA_Object=MibScalar
pm1001pcAlmDefFuseA=_Pm1001pcAlmDefFuseA_Object((1,3,6,1,4,1,20044,12,2,1,3,0,15),_Pm1001pcAlmDefFuseA_Type())
pm1001pcAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmDefFuseA.setStatus(_A)
_Pm1001pcAlmDefFuseB_Type=EkiOnOff
_Pm1001pcAlmDefFuseB_Object=MibScalar
pm1001pcAlmDefFuseB=_Pm1001pcAlmDefFuseB_Object((1,3,6,1,4,1,20044,12,2,1,3,0,16),_Pm1001pcAlmDefFuseB_Type())
pm1001pcAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmDefFuseB.setStatus(_A)
_Pm1001pcAlmClient_ObjectIdentity=ObjectIdentity
pm1001pcAlmClient=_Pm1001pcAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2))
_Pm1001pcAlmClientNurg_ObjectIdentity=ObjectIdentity
pm1001pcAlmClientNurg=_Pm1001pcAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,1))
_Pm1001pcAlmclientXfpWarnings_ObjectIdentity=ObjectIdentity
pm1001pcAlmclientXfpWarnings=_Pm1001pcAlmclientXfpWarnings_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,1,48))
_Pm1001pcAlmClientTxPowerLowWarning_Type=EkiOnOff
_Pm1001pcAlmClientTxPowerLowWarning_Object=MibScalar
pm1001pcAlmClientTxPowerLowWarning=_Pm1001pcAlmClientTxPowerLowWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,1),_Pm1001pcAlmClientTxPowerLowWarning_Type())
pm1001pcAlmClientTxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxPowerLowWarning.setStatus(_A)
_Pm1001pcAlmClientTxPowerHighWarning_Type=EkiOnOff
_Pm1001pcAlmClientTxPowerHighWarning_Object=MibScalar
pm1001pcAlmClientTxPowerHighWarning=_Pm1001pcAlmClientTxPowerHighWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,2),_Pm1001pcAlmClientTxPowerHighWarning_Type())
pm1001pcAlmClientTxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxPowerHighWarning.setStatus(_A)
_Pm1001pcAlmClientTxBiasLowWarning_Type=EkiOnOff
_Pm1001pcAlmClientTxBiasLowWarning_Object=MibScalar
pm1001pcAlmClientTxBiasLowWarning=_Pm1001pcAlmClientTxBiasLowWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,3),_Pm1001pcAlmClientTxBiasLowWarning_Type())
pm1001pcAlmClientTxBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxBiasLowWarning.setStatus(_A)
_Pm1001pcAlmClientTxBiasHighWarning_Type=EkiOnOff
_Pm1001pcAlmClientTxBiasHighWarning_Object=MibScalar
pm1001pcAlmClientTxBiasHighWarning=_Pm1001pcAlmClientTxBiasHighWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,4),_Pm1001pcAlmClientTxBiasHighWarning_Type())
pm1001pcAlmClientTxBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxBiasHighWarning.setStatus(_A)
_Pm1001pcAlmClientTempLowWarning_Type=EkiOnOff
_Pm1001pcAlmClientTempLowWarning_Object=MibScalar
pm1001pcAlmClientTempLowWarning=_Pm1001pcAlmClientTempLowWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,7),_Pm1001pcAlmClientTempLowWarning_Type())
pm1001pcAlmClientTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTempLowWarning.setStatus(_A)
_Pm1001pcAlmClientTempHighWarning_Type=EkiOnOff
_Pm1001pcAlmClientTempHighWarning_Object=MibScalar
pm1001pcAlmClientTempHighWarning=_Pm1001pcAlmClientTempHighWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,8),_Pm1001pcAlmClientTempHighWarning_Type())
pm1001pcAlmClientTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTempHighWarning.setStatus(_A)
_Pm1001pcAlmClientRxPowerLowWarning_Type=EkiOnOff
_Pm1001pcAlmClientRxPowerLowWarning_Object=MibScalar
pm1001pcAlmClientRxPowerLowWarning=_Pm1001pcAlmClientRxPowerLowWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,15),_Pm1001pcAlmClientRxPowerLowWarning_Type())
pm1001pcAlmClientRxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientRxPowerLowWarning.setStatus(_A)
_Pm1001pcAlmClientRxPowerHighWarning_Type=EkiOnOff
_Pm1001pcAlmClientRxPowerHighWarning_Object=MibScalar
pm1001pcAlmClientRxPowerHighWarning=_Pm1001pcAlmClientRxPowerHighWarning_Object((1,3,6,1,4,1,20044,12,2,2,1,48,16),_Pm1001pcAlmClientRxPowerHighWarning_Type())
pm1001pcAlmClientRxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientRxPowerHighWarning.setStatus(_A)
_Pm1001pcAlmClientUrg_ObjectIdentity=ObjectIdentity
pm1001pcAlmClientUrg=_Pm1001pcAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,2))
_Pm1001pcAlmclientXfpAlarm1_ObjectIdentity=ObjectIdentity
pm1001pcAlmclientXfpAlarm1=_Pm1001pcAlmclientXfpAlarm1_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,2,32))
_Pm1001pcAlmClientTxPowerLowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientTxPowerLowAlarm_Object=MibScalar
pm1001pcAlmClientTxPowerLowAlarm=_Pm1001pcAlmClientTxPowerLowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,1),_Pm1001pcAlmClientTxPowerLowAlarm_Type())
pm1001pcAlmClientTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxPowerLowAlarm.setStatus(_A)
_Pm1001pcAlmClientTxPowerHighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientTxPowerHighAlarm_Object=MibScalar
pm1001pcAlmClientTxPowerHighAlarm=_Pm1001pcAlmClientTxPowerHighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,2),_Pm1001pcAlmClientTxPowerHighAlarm_Type())
pm1001pcAlmClientTxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxPowerHighAlarm.setStatus(_A)
_Pm1001pcAlmClientTxBiasLowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientTxBiasLowAlarm_Object=MibScalar
pm1001pcAlmClientTxBiasLowAlarm=_Pm1001pcAlmClientTxBiasLowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,3),_Pm1001pcAlmClientTxBiasLowAlarm_Type())
pm1001pcAlmClientTxBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxBiasLowAlarm.setStatus(_A)
_Pm1001pcAlmClientTxBiasHighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientTxBiasHighAlarm_Object=MibScalar
pm1001pcAlmClientTxBiasHighAlarm=_Pm1001pcAlmClientTxBiasHighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,4),_Pm1001pcAlmClientTxBiasHighAlarm_Type())
pm1001pcAlmClientTxBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxBiasHighAlarm.setStatus(_A)
_Pm1001pcAlmClientTempLowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientTempLowAlarm_Object=MibScalar
pm1001pcAlmClientTempLowAlarm=_Pm1001pcAlmClientTempLowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,7),_Pm1001pcAlmClientTempLowAlarm_Type())
pm1001pcAlmClientTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTempLowAlarm.setStatus(_A)
_Pm1001pcAlmClientTempHighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientTempHighAlarm_Object=MibScalar
pm1001pcAlmClientTempHighAlarm=_Pm1001pcAlmClientTempHighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,8),_Pm1001pcAlmClientTempHighAlarm_Type())
pm1001pcAlmClientTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTempHighAlarm.setStatus(_A)
_Pm1001pcAlmClientRxPowerLowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientRxPowerLowAlarm_Object=MibScalar
pm1001pcAlmClientRxPowerLowAlarm=_Pm1001pcAlmClientRxPowerLowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,15),_Pm1001pcAlmClientRxPowerLowAlarm_Type())
pm1001pcAlmClientRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientRxPowerLowAlarm.setStatus(_A)
_Pm1001pcAlmClientRxPowerHighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientRxPowerHighAlarm_Object=MibScalar
pm1001pcAlmClientRxPowerHighAlarm=_Pm1001pcAlmClientRxPowerHighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,32,16),_Pm1001pcAlmClientRxPowerHighAlarm_Type())
pm1001pcAlmClientRxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientRxPowerHighAlarm.setStatus(_A)
_Pm1001pcAlmclientXfpSupplyAlarm_ObjectIdentity=ObjectIdentity
pm1001pcAlmclientXfpSupplyAlarm=_Pm1001pcAlmclientXfpSupplyAlarm_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,2,64))
_Pm1001pcAlmClientVee5LowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVee5LowAlarm_Object=MibScalar
pm1001pcAlmClientVee5LowAlarm=_Pm1001pcAlmClientVee5LowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,1),_Pm1001pcAlmClientVee5LowAlarm_Type())
pm1001pcAlmClientVee5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVee5LowAlarm.setStatus(_A)
_Pm1001pcAlmClientVee5HighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVee5HighAlarm_Object=MibScalar
pm1001pcAlmClientVee5HighAlarm=_Pm1001pcAlmClientVee5HighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,2),_Pm1001pcAlmClientVee5HighAlarm_Type())
pm1001pcAlmClientVee5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVee5HighAlarm.setStatus(_A)
_Pm1001pcAlmClientVcc2LowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVcc2LowAlarm_Object=MibScalar
pm1001pcAlmClientVcc2LowAlarm=_Pm1001pcAlmClientVcc2LowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,3),_Pm1001pcAlmClientVcc2LowAlarm_Type())
pm1001pcAlmClientVcc2LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc2LowAlarm.setStatus(_A)
_Pm1001pcAlmClientVcc2HighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVcc2HighAlarm_Object=MibScalar
pm1001pcAlmClientVcc2HighAlarm=_Pm1001pcAlmClientVcc2HighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,4),_Pm1001pcAlmClientVcc2HighAlarm_Type())
pm1001pcAlmClientVcc2HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc2HighAlarm.setStatus(_A)
_Pm1001pcAlmClientVcc3LowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVcc3LowAlarm_Object=MibScalar
pm1001pcAlmClientVcc3LowAlarm=_Pm1001pcAlmClientVcc3LowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,5),_Pm1001pcAlmClientVcc3LowAlarm_Type())
pm1001pcAlmClientVcc3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc3LowAlarm.setStatus(_A)
_Pm1001pcAlmClientVcc3HighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVcc3HighAlarm_Object=MibScalar
pm1001pcAlmClientVcc3HighAlarm=_Pm1001pcAlmClientVcc3HighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,6),_Pm1001pcAlmClientVcc3HighAlarm_Type())
pm1001pcAlmClientVcc3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc3HighAlarm.setStatus(_A)
_Pm1001pcAlmClientVcc5LowAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVcc5LowAlarm_Object=MibScalar
pm1001pcAlmClientVcc5LowAlarm=_Pm1001pcAlmClientVcc5LowAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,7),_Pm1001pcAlmClientVcc5LowAlarm_Type())
pm1001pcAlmClientVcc5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc5LowAlarm.setStatus(_A)
_Pm1001pcAlmClientVcc5HighAlarm_Type=EkiOnOff
_Pm1001pcAlmClientVcc5HighAlarm_Object=MibScalar
pm1001pcAlmClientVcc5HighAlarm=_Pm1001pcAlmClientVcc5HighAlarm_Object((1,3,6,1,4,1,20044,12,2,2,2,64,8),_Pm1001pcAlmClientVcc5HighAlarm_Type())
pm1001pcAlmClientVcc5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc5HighAlarm.setStatus(_A)
_Pm1001pcAlmClientVee5LowWarning_Type=EkiOnOff
_Pm1001pcAlmClientVee5LowWarning_Object=MibScalar
pm1001pcAlmClientVee5LowWarning=_Pm1001pcAlmClientVee5LowWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,9),_Pm1001pcAlmClientVee5LowWarning_Type())
pm1001pcAlmClientVee5LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVee5LowWarning.setStatus(_A)
_Pm1001pcAlmClientVee5HighWarning_Type=EkiOnOff
_Pm1001pcAlmClientVee5HighWarning_Object=MibScalar
pm1001pcAlmClientVee5HighWarning=_Pm1001pcAlmClientVee5HighWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,10),_Pm1001pcAlmClientVee5HighWarning_Type())
pm1001pcAlmClientVee5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVee5HighWarning.setStatus(_A)
_Pm1001pcAlmClientVcc2LowWarning_Type=EkiOnOff
_Pm1001pcAlmClientVcc2LowWarning_Object=MibScalar
pm1001pcAlmClientVcc2LowWarning=_Pm1001pcAlmClientVcc2LowWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,11),_Pm1001pcAlmClientVcc2LowWarning_Type())
pm1001pcAlmClientVcc2LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc2LowWarning.setStatus(_A)
_Pm1001pcAlmClientVcc2HighWarning_Type=EkiOnOff
_Pm1001pcAlmClientVcc2HighWarning_Object=MibScalar
pm1001pcAlmClientVcc2HighWarning=_Pm1001pcAlmClientVcc2HighWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,12),_Pm1001pcAlmClientVcc2HighWarning_Type())
pm1001pcAlmClientVcc2HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc2HighWarning.setStatus(_A)
_Pm1001pcAlmClientVcc3LowWarning_Type=EkiOnOff
_Pm1001pcAlmClientVcc3LowWarning_Object=MibScalar
pm1001pcAlmClientVcc3LowWarning=_Pm1001pcAlmClientVcc3LowWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,13),_Pm1001pcAlmClientVcc3LowWarning_Type())
pm1001pcAlmClientVcc3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc3LowWarning.setStatus(_A)
_Pm1001pcAlmClientVcc3HighWarning_Type=EkiOnOff
_Pm1001pcAlmClientVcc3HighWarning_Object=MibScalar
pm1001pcAlmClientVcc3HighWarning=_Pm1001pcAlmClientVcc3HighWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,14),_Pm1001pcAlmClientVcc3HighWarning_Type())
pm1001pcAlmClientVcc3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc3HighWarning.setStatus(_A)
_Pm1001pcAlmClientVcc5LowWarning_Type=EkiOnOff
_Pm1001pcAlmClientVcc5LowWarning_Object=MibScalar
pm1001pcAlmClientVcc5LowWarning=_Pm1001pcAlmClientVcc5LowWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,15),_Pm1001pcAlmClientVcc5LowWarning_Type())
pm1001pcAlmClientVcc5LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc5LowWarning.setStatus(_A)
_Pm1001pcAlmClientVcc5HighWarning_Type=EkiOnOff
_Pm1001pcAlmClientVcc5HighWarning_Object=MibScalar
pm1001pcAlmClientVcc5HighWarning=_Pm1001pcAlmClientVcc5HighWarning_Object((1,3,6,1,4,1,20044,12,2,2,2,64,16),_Pm1001pcAlmClientVcc5HighWarning_Type())
pm1001pcAlmClientVcc5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientVcc5HighWarning.setStatus(_A)
_Pm1001pcAlmClientCrit_ObjectIdentity=ObjectIdentity
pm1001pcAlmClientCrit=_Pm1001pcAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,3))
_Pm1001pcAlmsynthAlmPort_ObjectIdentity=ObjectIdentity
pm1001pcAlmsynthAlmPort=_Pm1001pcAlmsynthAlmPort_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,3,8))
_Pm1001pcAlmClientXfpAbsent_Type=EkiOnOff
_Pm1001pcAlmClientXfpAbsent_Object=MibScalar
pm1001pcAlmClientXfpAbsent=_Pm1001pcAlmClientXfpAbsent_Object((1,3,6,1,4,1,20044,12,2,2,3,8,1),_Pm1001pcAlmClientXfpAbsent_Type())
pm1001pcAlmClientXfpAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientXfpAbsent.setStatus(_A)
_Pm1001pcAlmClientDdmAbsent_Type=EkiOnOff
_Pm1001pcAlmClientDdmAbsent_Object=MibScalar
pm1001pcAlmClientDdmAbsent=_Pm1001pcAlmClientDdmAbsent_Object((1,3,6,1,4,1,20044,12,2,2,3,8,2),_Pm1001pcAlmClientDdmAbsent_Type())
pm1001pcAlmClientDdmAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientDdmAbsent.setStatus(_A)
_Pm1001pcAlmClientHwFail_Type=EkiOnOff
_Pm1001pcAlmClientHwFail_Object=MibScalar
pm1001pcAlmClientHwFail=_Pm1001pcAlmClientHwFail_Object((1,3,6,1,4,1,20044,12,2,2,3,8,4),_Pm1001pcAlmClientHwFail_Type())
pm1001pcAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientHwFail.setStatus(_A)
_Pm1001pcAlmClientDwLsd_Type=EkiOnOff
_Pm1001pcAlmClientDwLsd_Object=MibScalar
pm1001pcAlmClientDwLsd=_Pm1001pcAlmClientDwLsd_Object((1,3,6,1,4,1,20044,12,2,2,3,8,5),_Pm1001pcAlmClientDwLsd_Type())
pm1001pcAlmClientDwLsd.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientDwLsd.setStatus(_A)
_Pm1001pcAlmClientLocalOos_Type=EkiOnOff
_Pm1001pcAlmClientLocalOos_Object=MibScalar
pm1001pcAlmClientLocalOos=_Pm1001pcAlmClientLocalOos_Object((1,3,6,1,4,1,20044,12,2,2,3,8,6),_Pm1001pcAlmClientLocalOos_Type())
pm1001pcAlmClientLocalOos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientLocalOos.setStatus(_A)
_Pm1001pcAlmClientDwCais_Type=EkiOnOff
_Pm1001pcAlmClientDwCais_Object=MibScalar
pm1001pcAlmClientDwCais=_Pm1001pcAlmClientDwCais_Object((1,3,6,1,4,1,20044,12,2,2,3,8,8),_Pm1001pcAlmClientDwCais_Type())
pm1001pcAlmClientDwCais.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientDwCais.setStatus(_A)
_Pm1001pcAlmClientXfpDdmWarning_Type=EkiOnOff
_Pm1001pcAlmClientXfpDdmWarning_Object=MibScalar
pm1001pcAlmClientXfpDdmWarning=_Pm1001pcAlmClientXfpDdmWarning_Object((1,3,6,1,4,1,20044,12,2,2,3,8,9),_Pm1001pcAlmClientXfpDdmWarning_Type())
pm1001pcAlmClientXfpDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientXfpDdmWarning.setStatus(_A)
_Pm1001pcAlmClientXfpDdmAlm_Type=EkiOnOff
_Pm1001pcAlmClientXfpDdmAlm_Object=MibScalar
pm1001pcAlmClientXfpDdmAlm=_Pm1001pcAlmClientXfpDdmAlm_Object((1,3,6,1,4,1,20044,12,2,2,3,8,10),_Pm1001pcAlmClientXfpDdmAlm_Type())
pm1001pcAlmClientXfpDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientXfpDdmAlm.setStatus(_A)
_Pm1001pcAlmClientFail_Type=EkiOnOff
_Pm1001pcAlmClientFail_Object=MibScalar
pm1001pcAlmClientFail=_Pm1001pcAlmClientFail_Object((1,3,6,1,4,1,20044,12,2,2,3,8,12),_Pm1001pcAlmClientFail_Type())
pm1001pcAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientFail.setStatus(_A)
_Pm1001pcAlmClientUpCsf_Type=EkiOnOff
_Pm1001pcAlmClientUpCsf_Object=MibScalar
pm1001pcAlmClientUpCsf=_Pm1001pcAlmClientUpCsf_Object((1,3,6,1,4,1,20044,12,2,2,3,8,16),_Pm1001pcAlmClientUpCsf_Type())
pm1001pcAlmClientUpCsf.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientUpCsf.setStatus(_A)
_Pm1001pcAlmclientAccessioAlm_ObjectIdentity=ObjectIdentity
pm1001pcAlmclientAccessioAlm=_Pm1001pcAlmclientAccessioAlm_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,3,16))
_Pm1001pcAlmClientDwLasFail_Type=EkiOnOff
_Pm1001pcAlmClientDwLasFail_Object=MibScalar
pm1001pcAlmClientDwLasFail=_Pm1001pcAlmClientDwLasFail_Object((1,3,6,1,4,1,20044,12,2,2,3,16,1),_Pm1001pcAlmClientDwLasFail_Type())
pm1001pcAlmClientDwLasFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientDwLasFail.setStatus(_A)
_Pm1001pcAlmClientUpLos_Type=EkiOnOff
_Pm1001pcAlmClientUpLos_Object=MibScalar
pm1001pcAlmClientUpLos=_Pm1001pcAlmClientUpLos_Object((1,3,6,1,4,1,20044,12,2,2,3,16,4),_Pm1001pcAlmClientUpLos_Type())
pm1001pcAlmClientUpLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientUpLos.setStatus(_A)
_Pm1001pcAlmclientXfpAlarm2_ObjectIdentity=ObjectIdentity
pm1001pcAlmclientXfpAlarm2=_Pm1001pcAlmclientXfpAlarm2_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,3,40))
_Pm1001pcAlmClientModNr_Type=EkiOnOff
_Pm1001pcAlmClientModNr_Object=MibScalar
pm1001pcAlmClientModNr=_Pm1001pcAlmClientModNr_Object((1,3,6,1,4,1,20044,12,2,2,3,40,2),_Pm1001pcAlmClientModNr_Type())
pm1001pcAlmClientModNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientModNr.setStatus(_A)
_Pm1001pcAlmClientRxCdrNotLocked1_Type=EkiOnOff
_Pm1001pcAlmClientRxCdrNotLocked1_Object=MibScalar
pm1001pcAlmClientRxCdrNotLocked1=_Pm1001pcAlmClientRxCdrNotLocked1_Object((1,3,6,1,4,1,20044,12,2,2,3,40,3),_Pm1001pcAlmClientRxCdrNotLocked1_Type())
pm1001pcAlmClientRxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientRxCdrNotLocked1.setStatus(_A)
_Pm1001pcAlmClientRxNr_Type=EkiOnOff
_Pm1001pcAlmClientRxNr_Object=MibScalar
pm1001pcAlmClientRxNr=_Pm1001pcAlmClientRxNr_Object((1,3,6,1,4,1,20044,12,2,2,3,40,5),_Pm1001pcAlmClientRxNr_Type())
pm1001pcAlmClientRxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientRxNr.setStatus(_A)
_Pm1001pcAlmClientTxCdrNotLocked1_Type=EkiOnOff
_Pm1001pcAlmClientTxCdrNotLocked1_Object=MibScalar
pm1001pcAlmClientTxCdrNotLocked1=_Pm1001pcAlmClientTxCdrNotLocked1_Object((1,3,6,1,4,1,20044,12,2,2,3,40,6),_Pm1001pcAlmClientTxCdrNotLocked1_Type())
pm1001pcAlmClientTxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxCdrNotLocked1.setStatus(_A)
_Pm1001pcAlmClientTxFault_Type=EkiOnOff
_Pm1001pcAlmClientTxFault_Object=MibScalar
pm1001pcAlmClientTxFault=_Pm1001pcAlmClientTxFault_Object((1,3,6,1,4,1,20044,12,2,2,3,40,7),_Pm1001pcAlmClientTxFault_Type())
pm1001pcAlmClientTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxFault.setStatus(_A)
_Pm1001pcAlmClientTxNr_Type=EkiOnOff
_Pm1001pcAlmClientTxNr_Object=MibScalar
pm1001pcAlmClientTxNr=_Pm1001pcAlmClientTxNr_Object((1,3,6,1,4,1,20044,12,2,2,3,40,8),_Pm1001pcAlmClientTxNr_Type())
pm1001pcAlmClientTxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTxNr.setStatus(_A)
_Pm1001pcAlmClientWavelengthUnlocked_Type=EkiOnOff
_Pm1001pcAlmClientWavelengthUnlocked_Object=MibScalar
pm1001pcAlmClientWavelengthUnlocked=_Pm1001pcAlmClientWavelengthUnlocked_Object((1,3,6,1,4,1,20044,12,2,2,3,40,14),_Pm1001pcAlmClientWavelengthUnlocked_Type())
pm1001pcAlmClientWavelengthUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientWavelengthUnlocked.setStatus(_A)
_Pm1001pcAlmClientTecFault_Type=EkiOnOff
_Pm1001pcAlmClientTecFault_Object=MibScalar
pm1001pcAlmClientTecFault=_Pm1001pcAlmClientTecFault_Object((1,3,6,1,4,1,20044,12,2,2,3,40,15),_Pm1001pcAlmClientTecFault_Type())
pm1001pcAlmClientTecFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientTecFault.setStatus(_A)
_Pm1001pcAlmClientApdSupplyFault_Type=EkiOnOff
_Pm1001pcAlmClientApdSupplyFault_Object=MibScalar
pm1001pcAlmClientApdSupplyFault=_Pm1001pcAlmClientApdSupplyFault_Object((1,3,6,1,4,1,20044,12,2,2,3,40,16),_Pm1001pcAlmClientApdSupplyFault_Type())
pm1001pcAlmClientApdSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientApdSupplyFault.setStatus(_A)
_Pm1001pcAlmclientMapperDeAlm_ObjectIdentity=ObjectIdentity
pm1001pcAlmclientMapperDeAlm=_Pm1001pcAlmclientMapperDeAlm_ObjectIdentity((1,3,6,1,4,1,20044,12,2,2,3,72))
_Pm1001pcAlmClientUpAccOos_Type=EkiOnOff
_Pm1001pcAlmClientUpAccOos_Object=MibScalar
pm1001pcAlmClientUpAccOos=_Pm1001pcAlmClientUpAccOos_Object((1,3,6,1,4,1,20044,12,2,2,3,72,1),_Pm1001pcAlmClientUpAccOos_Type())
pm1001pcAlmClientUpAccOos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientUpAccOos.setStatus(_A)
_Pm1001pcAlmClientUpBufferOvl_Type=EkiOnOff
_Pm1001pcAlmClientUpBufferOvl_Object=MibScalar
pm1001pcAlmClientUpBufferOvl=_Pm1001pcAlmClientUpBufferOvl_Object((1,3,6,1,4,1,20044,12,2,2,3,72,10),_Pm1001pcAlmClientUpBufferOvl_Type())
pm1001pcAlmClientUpBufferOvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientUpBufferOvl.setStatus(_A)
_Pm1001pcAlmClientDwCsfDet_Type=EkiOnOff
_Pm1001pcAlmClientDwCsfDet_Object=MibScalar
pm1001pcAlmClientDwCsfDet=_Pm1001pcAlmClientDwCsfDet_Object((1,3,6,1,4,1,20044,12,2,2,3,72,11),_Pm1001pcAlmClientDwCsfDet_Type())
pm1001pcAlmClientDwCsfDet.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientDwCsfDet.setStatus(_A)
_Pm1001pcAlmClientDwBufferOvl_Type=EkiOnOff
_Pm1001pcAlmClientDwBufferOvl_Object=MibScalar
pm1001pcAlmClientDwBufferOvl=_Pm1001pcAlmClientDwBufferOvl_Object((1,3,6,1,4,1,20044,12,2,2,3,72,14),_Pm1001pcAlmClientDwBufferOvl_Type())
pm1001pcAlmClientDwBufferOvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmClientDwBufferOvl.setStatus(_A)
_Pm1001pcAlmLine_ObjectIdentity=ObjectIdentity
pm1001pcAlmLine=_Pm1001pcAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3))
_Pm1001pcAlmLineNurg_ObjectIdentity=ObjectIdentity
pm1001pcAlmLineNurg=_Pm1001pcAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,1))
_Pm1001pcAlmlineXfpWarnings_ObjectIdentity=ObjectIdentity
pm1001pcAlmlineXfpWarnings=_Pm1001pcAlmlineXfpWarnings_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,1,209))
_Pm1001pcAlmLineTxPowerLowWarning_Type=EkiOnOff
_Pm1001pcAlmLineTxPowerLowWarning_Object=MibScalar
pm1001pcAlmLineTxPowerLowWarning=_Pm1001pcAlmLineTxPowerLowWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,1),_Pm1001pcAlmLineTxPowerLowWarning_Type())
pm1001pcAlmLineTxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxPowerLowWarning.setStatus(_A)
_Pm1001pcAlmLineTxPowerHighWarning_Type=EkiOnOff
_Pm1001pcAlmLineTxPowerHighWarning_Object=MibScalar
pm1001pcAlmLineTxPowerHighWarning=_Pm1001pcAlmLineTxPowerHighWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,2),_Pm1001pcAlmLineTxPowerHighWarning_Type())
pm1001pcAlmLineTxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxPowerHighWarning.setStatus(_A)
_Pm1001pcAlmLineTxBiasLowWarning_Type=EkiOnOff
_Pm1001pcAlmLineTxBiasLowWarning_Object=MibScalar
pm1001pcAlmLineTxBiasLowWarning=_Pm1001pcAlmLineTxBiasLowWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,3),_Pm1001pcAlmLineTxBiasLowWarning_Type())
pm1001pcAlmLineTxBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxBiasLowWarning.setStatus(_A)
_Pm1001pcAlmLineTxBiasHighWarning_Type=EkiOnOff
_Pm1001pcAlmLineTxBiasHighWarning_Object=MibScalar
pm1001pcAlmLineTxBiasHighWarning=_Pm1001pcAlmLineTxBiasHighWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,4),_Pm1001pcAlmLineTxBiasHighWarning_Type())
pm1001pcAlmLineTxBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxBiasHighWarning.setStatus(_A)
_Pm1001pcAlmLineTempLowWarning_Type=EkiOnOff
_Pm1001pcAlmLineTempLowWarning_Object=MibScalar
pm1001pcAlmLineTempLowWarning=_Pm1001pcAlmLineTempLowWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,7),_Pm1001pcAlmLineTempLowWarning_Type())
pm1001pcAlmLineTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTempLowWarning.setStatus(_A)
_Pm1001pcAlmLineTempHighWarning_Type=EkiOnOff
_Pm1001pcAlmLineTempHighWarning_Object=MibScalar
pm1001pcAlmLineTempHighWarning=_Pm1001pcAlmLineTempHighWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,8),_Pm1001pcAlmLineTempHighWarning_Type())
pm1001pcAlmLineTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTempHighWarning.setStatus(_A)
_Pm1001pcAlmLineRxPowerLowWarning_Type=EkiOnOff
_Pm1001pcAlmLineRxPowerLowWarning_Object=MibScalar
pm1001pcAlmLineRxPowerLowWarning=_Pm1001pcAlmLineRxPowerLowWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,15),_Pm1001pcAlmLineRxPowerLowWarning_Type())
pm1001pcAlmLineRxPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineRxPowerLowWarning.setStatus(_A)
_Pm1001pcAlmLineRxPowerHighWarning_Type=EkiOnOff
_Pm1001pcAlmLineRxPowerHighWarning_Object=MibScalar
pm1001pcAlmLineRxPowerHighWarning=_Pm1001pcAlmLineRxPowerHighWarning_Object((1,3,6,1,4,1,20044,12,2,3,1,209,16),_Pm1001pcAlmLineRxPowerHighWarning_Type())
pm1001pcAlmLineRxPowerHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineRxPowerHighWarning.setStatus(_A)
_Pm1001pcAlmLineUrg_ObjectIdentity=ObjectIdentity
pm1001pcAlmLineUrg=_Pm1001pcAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,2))
_Pm1001pcAlmdfrmBer_ObjectIdentity=ObjectIdentity
pm1001pcAlmdfrmBer=_Pm1001pcAlmdfrmBer_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,2,129))
_Pm1001pcAlmLineSignalDegrade_Type=EkiOnOff
_Pm1001pcAlmLineSignalDegrade_Object=MibScalar
pm1001pcAlmLineSignalDegrade=_Pm1001pcAlmLineSignalDegrade_Object((1,3,6,1,4,1,20044,12,2,3,2,129,1),_Pm1001pcAlmLineSignalDegrade_Type())
pm1001pcAlmLineSignalDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineSignalDegrade.setStatus(_A)
_Pm1001pcAlmLineSignalFail_Type=EkiOnOff
_Pm1001pcAlmLineSignalFail_Object=MibScalar
pm1001pcAlmLineSignalFail=_Pm1001pcAlmLineSignalFail_Object((1,3,6,1,4,1,20044,12,2,3,2,129,2),_Pm1001pcAlmLineSignalFail_Type())
pm1001pcAlmLineSignalFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineSignalFail.setStatus(_A)
_Pm1001pcAlmLineDegrade_Type=EkiOnOff
_Pm1001pcAlmLineDegrade_Object=MibScalar
pm1001pcAlmLineDegrade=_Pm1001pcAlmLineDegrade_Object((1,3,6,1,4,1,20044,12,2,3,2,129,5),_Pm1001pcAlmLineDegrade_Type())
pm1001pcAlmLineDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDegrade.setStatus(_A)
_Pm1001pcAlmlineXfpAlarm1_ObjectIdentity=ObjectIdentity
pm1001pcAlmlineXfpAlarm1=_Pm1001pcAlmlineXfpAlarm1_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,2,208))
_Pm1001pcAlmLineTxPowerLowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineTxPowerLowAlarm_Object=MibScalar
pm1001pcAlmLineTxPowerLowAlarm=_Pm1001pcAlmLineTxPowerLowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,1),_Pm1001pcAlmLineTxPowerLowAlarm_Type())
pm1001pcAlmLineTxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxPowerLowAlarm.setStatus(_A)
_Pm1001pcAlmLineTxPowerHighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineTxPowerHighAlarm_Object=MibScalar
pm1001pcAlmLineTxPowerHighAlarm=_Pm1001pcAlmLineTxPowerHighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,2),_Pm1001pcAlmLineTxPowerHighAlarm_Type())
pm1001pcAlmLineTxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxPowerHighAlarm.setStatus(_A)
_Pm1001pcAlmLineTxBiasLowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineTxBiasLowAlarm_Object=MibScalar
pm1001pcAlmLineTxBiasLowAlarm=_Pm1001pcAlmLineTxBiasLowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,3),_Pm1001pcAlmLineTxBiasLowAlarm_Type())
pm1001pcAlmLineTxBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxBiasLowAlarm.setStatus(_A)
_Pm1001pcAlmLineTxBiasHighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineTxBiasHighAlarm_Object=MibScalar
pm1001pcAlmLineTxBiasHighAlarm=_Pm1001pcAlmLineTxBiasHighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,4),_Pm1001pcAlmLineTxBiasHighAlarm_Type())
pm1001pcAlmLineTxBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxBiasHighAlarm.setStatus(_A)
_Pm1001pcAlmLineTempLowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineTempLowAlarm_Object=MibScalar
pm1001pcAlmLineTempLowAlarm=_Pm1001pcAlmLineTempLowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,7),_Pm1001pcAlmLineTempLowAlarm_Type())
pm1001pcAlmLineTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTempLowAlarm.setStatus(_A)
_Pm1001pcAlmLineTempHighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineTempHighAlarm_Object=MibScalar
pm1001pcAlmLineTempHighAlarm=_Pm1001pcAlmLineTempHighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,8),_Pm1001pcAlmLineTempHighAlarm_Type())
pm1001pcAlmLineTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTempHighAlarm.setStatus(_A)
_Pm1001pcAlmLineRxPowerLowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineRxPowerLowAlarm_Object=MibScalar
pm1001pcAlmLineRxPowerLowAlarm=_Pm1001pcAlmLineRxPowerLowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,15),_Pm1001pcAlmLineRxPowerLowAlarm_Type())
pm1001pcAlmLineRxPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineRxPowerLowAlarm.setStatus(_A)
_Pm1001pcAlmLineRxPowerHighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineRxPowerHighAlarm_Object=MibScalar
pm1001pcAlmLineRxPowerHighAlarm=_Pm1001pcAlmLineRxPowerHighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,208,16),_Pm1001pcAlmLineRxPowerHighAlarm_Type())
pm1001pcAlmLineRxPowerHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineRxPowerHighAlarm.setStatus(_A)
_Pm1001pcAlmlineXfpSupplyAlarm_ObjectIdentity=ObjectIdentity
pm1001pcAlmlineXfpSupplyAlarm=_Pm1001pcAlmlineXfpSupplyAlarm_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,2,212))
_Pm1001pcAlmLineVee5LowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVee5LowAlarm_Object=MibScalar
pm1001pcAlmLineVee5LowAlarm=_Pm1001pcAlmLineVee5LowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,1),_Pm1001pcAlmLineVee5LowAlarm_Type())
pm1001pcAlmLineVee5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVee5LowAlarm.setStatus(_A)
_Pm1001pcAlmLineVee5HighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVee5HighAlarm_Object=MibScalar
pm1001pcAlmLineVee5HighAlarm=_Pm1001pcAlmLineVee5HighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,2),_Pm1001pcAlmLineVee5HighAlarm_Type())
pm1001pcAlmLineVee5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVee5HighAlarm.setStatus(_A)
_Pm1001pcAlmLineVcc2LowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVcc2LowAlarm_Object=MibScalar
pm1001pcAlmLineVcc2LowAlarm=_Pm1001pcAlmLineVcc2LowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,3),_Pm1001pcAlmLineVcc2LowAlarm_Type())
pm1001pcAlmLineVcc2LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc2LowAlarm.setStatus(_A)
_Pm1001pcAlmLineVcc2HighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVcc2HighAlarm_Object=MibScalar
pm1001pcAlmLineVcc2HighAlarm=_Pm1001pcAlmLineVcc2HighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,4),_Pm1001pcAlmLineVcc2HighAlarm_Type())
pm1001pcAlmLineVcc2HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc2HighAlarm.setStatus(_A)
_Pm1001pcAlmLineVcc3LowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVcc3LowAlarm_Object=MibScalar
pm1001pcAlmLineVcc3LowAlarm=_Pm1001pcAlmLineVcc3LowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,5),_Pm1001pcAlmLineVcc3LowAlarm_Type())
pm1001pcAlmLineVcc3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc3LowAlarm.setStatus(_A)
_Pm1001pcAlmLineVcc3HighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVcc3HighAlarm_Object=MibScalar
pm1001pcAlmLineVcc3HighAlarm=_Pm1001pcAlmLineVcc3HighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,6),_Pm1001pcAlmLineVcc3HighAlarm_Type())
pm1001pcAlmLineVcc3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc3HighAlarm.setStatus(_A)
_Pm1001pcAlmLineVcc5LowAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVcc5LowAlarm_Object=MibScalar
pm1001pcAlmLineVcc5LowAlarm=_Pm1001pcAlmLineVcc5LowAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,7),_Pm1001pcAlmLineVcc5LowAlarm_Type())
pm1001pcAlmLineVcc5LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc5LowAlarm.setStatus(_A)
_Pm1001pcAlmLineVcc5HighAlarm_Type=EkiOnOff
_Pm1001pcAlmLineVcc5HighAlarm_Object=MibScalar
pm1001pcAlmLineVcc5HighAlarm=_Pm1001pcAlmLineVcc5HighAlarm_Object((1,3,6,1,4,1,20044,12,2,3,2,212,8),_Pm1001pcAlmLineVcc5HighAlarm_Type())
pm1001pcAlmLineVcc5HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc5HighAlarm.setStatus(_A)
_Pm1001pcAlmLineVee5LowLineWarning_Type=EkiOnOff
_Pm1001pcAlmLineVee5LowLineWarning_Object=MibScalar
pm1001pcAlmLineVee5LowLineWarning=_Pm1001pcAlmLineVee5LowLineWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,9),_Pm1001pcAlmLineVee5LowLineWarning_Type())
pm1001pcAlmLineVee5LowLineWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVee5LowLineWarning.setStatus(_A)
_Pm1001pcAlmLineVee5HighWarning_Type=EkiOnOff
_Pm1001pcAlmLineVee5HighWarning_Object=MibScalar
pm1001pcAlmLineVee5HighWarning=_Pm1001pcAlmLineVee5HighWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,10),_Pm1001pcAlmLineVee5HighWarning_Type())
pm1001pcAlmLineVee5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVee5HighWarning.setStatus(_A)
_Pm1001pcAlmLineVcc2LowWarning_Type=EkiOnOff
_Pm1001pcAlmLineVcc2LowWarning_Object=MibScalar
pm1001pcAlmLineVcc2LowWarning=_Pm1001pcAlmLineVcc2LowWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,11),_Pm1001pcAlmLineVcc2LowWarning_Type())
pm1001pcAlmLineVcc2LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc2LowWarning.setStatus(_A)
_Pm1001pcAlmLineVcc2HighWarning_Type=EkiOnOff
_Pm1001pcAlmLineVcc2HighWarning_Object=MibScalar
pm1001pcAlmLineVcc2HighWarning=_Pm1001pcAlmLineVcc2HighWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,12),_Pm1001pcAlmLineVcc2HighWarning_Type())
pm1001pcAlmLineVcc2HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc2HighWarning.setStatus(_A)
_Pm1001pcAlmLineVcc3LowWarning_Type=EkiOnOff
_Pm1001pcAlmLineVcc3LowWarning_Object=MibScalar
pm1001pcAlmLineVcc3LowWarning=_Pm1001pcAlmLineVcc3LowWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,13),_Pm1001pcAlmLineVcc3LowWarning_Type())
pm1001pcAlmLineVcc3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc3LowWarning.setStatus(_A)
_Pm1001pcAlmLineVcc3HighWarning_Type=EkiOnOff
_Pm1001pcAlmLineVcc3HighWarning_Object=MibScalar
pm1001pcAlmLineVcc3HighWarning=_Pm1001pcAlmLineVcc3HighWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,14),_Pm1001pcAlmLineVcc3HighWarning_Type())
pm1001pcAlmLineVcc3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc3HighWarning.setStatus(_A)
_Pm1001pcAlmLineVcc5LowWarning_Type=EkiOnOff
_Pm1001pcAlmLineVcc5LowWarning_Object=MibScalar
pm1001pcAlmLineVcc5LowWarning=_Pm1001pcAlmLineVcc5LowWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,15),_Pm1001pcAlmLineVcc5LowWarning_Type())
pm1001pcAlmLineVcc5LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc5LowWarning.setStatus(_A)
_Pm1001pcAlmLineVcc5HighWarning_Type=EkiOnOff
_Pm1001pcAlmLineVcc5HighWarning_Object=MibScalar
pm1001pcAlmLineVcc5HighWarning=_Pm1001pcAlmLineVcc5HighWarning_Object((1,3,6,1,4,1,20044,12,2,3,2,212,16),_Pm1001pcAlmLineVcc5HighWarning_Type())
pm1001pcAlmLineVcc5HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineVcc5HighWarning.setStatus(_A)
_Pm1001pcAlmLineCrit_ObjectIdentity=ObjectIdentity
pm1001pcAlmLineCrit=_Pm1001pcAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,3))
_Pm1001pcAlmsynthAlmLine_ObjectIdentity=ObjectIdentity
pm1001pcAlmsynthAlmLine=_Pm1001pcAlmsynthAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,3,7))
_Pm1001pcAlmLineXfpAbsent_Type=EkiOnOff
_Pm1001pcAlmLineXfpAbsent_Object=MibScalar
pm1001pcAlmLineXfpAbsent=_Pm1001pcAlmLineXfpAbsent_Object((1,3,6,1,4,1,20044,12,2,3,3,7,1),_Pm1001pcAlmLineXfpAbsent_Type())
pm1001pcAlmLineXfpAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineXfpAbsent.setStatus(_A)
_Pm1001pcAlmLineXfpInitNotCompl_Type=EkiOnOff
_Pm1001pcAlmLineXfpInitNotCompl_Object=MibScalar
pm1001pcAlmLineXfpInitNotCompl=_Pm1001pcAlmLineXfpInitNotCompl_Object((1,3,6,1,4,1,20044,12,2,3,3,7,2),_Pm1001pcAlmLineXfpInitNotCompl_Type())
pm1001pcAlmLineXfpInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineXfpInitNotCompl.setStatus(_A)
_Pm1001pcAlmLineHwFail_Type=EkiOnOff
_Pm1001pcAlmLineHwFail_Object=MibScalar
pm1001pcAlmLineHwFail=_Pm1001pcAlmLineHwFail_Object((1,3,6,1,4,1,20044,12,2,3,3,7,4),_Pm1001pcAlmLineHwFail_Type())
pm1001pcAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineHwFail.setStatus(_A)
_Pm1001pcAlmLineXfpTxOff_Type=EkiOnOff
_Pm1001pcAlmLineXfpTxOff_Object=MibScalar
pm1001pcAlmLineXfpTxOff=_Pm1001pcAlmLineXfpTxOff_Object((1,3,6,1,4,1,20044,12,2,3,3,7,5),_Pm1001pcAlmLineXfpTxOff_Type())
pm1001pcAlmLineXfpTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineXfpTxOff.setStatus(_A)
_Pm1001pcAlmLineLocalOos_Type=EkiOnOff
_Pm1001pcAlmLineLocalOos_Object=MibScalar
pm1001pcAlmLineLocalOos=_Pm1001pcAlmLineLocalOos_Object((1,3,6,1,4,1,20044,12,2,3,3,7,6),_Pm1001pcAlmLineLocalOos_Type())
pm1001pcAlmLineLocalOos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineLocalOos.setStatus(_A)
_Pm1001pcAlmLineUpRdiIns_Type=EkiOnOff
_Pm1001pcAlmLineUpRdiIns_Object=MibScalar
pm1001pcAlmLineUpRdiIns=_Pm1001pcAlmLineUpRdiIns_Object((1,3,6,1,4,1,20044,12,2,3,3,7,8),_Pm1001pcAlmLineUpRdiIns_Type())
pm1001pcAlmLineUpRdiIns.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineUpRdiIns.setStatus(_A)
_Pm1001pcAlmLineDdmWarning_Type=EkiOnOff
_Pm1001pcAlmLineDdmWarning_Object=MibScalar
pm1001pcAlmLineDdmWarning=_Pm1001pcAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,12,2,3,3,7,9),_Pm1001pcAlmLineDdmWarning_Type())
pm1001pcAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDdmWarning.setStatus(_A)
_Pm1001pcAlmLineDdmAlm_Type=EkiOnOff
_Pm1001pcAlmLineDdmAlm_Object=MibScalar
pm1001pcAlmLineDdmAlm=_Pm1001pcAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,12,2,3,3,7,10),_Pm1001pcAlmLineDdmAlm_Type())
pm1001pcAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDdmAlm.setStatus(_A)
_Pm1001pcAlmLineFail_Type=EkiOnOff
_Pm1001pcAlmLineFail_Object=MibScalar
pm1001pcAlmLineFail=_Pm1001pcAlmLineFail_Object((1,3,6,1,4,1,20044,12,2,3,3,7,12),_Pm1001pcAlmLineFail_Type())
pm1001pcAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineFail.setStatus(_A)
_Pm1001pcAlmdfrmAlm_ObjectIdentity=ObjectIdentity
pm1001pcAlmdfrmAlm=_Pm1001pcAlmdfrmAlm_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,3,128))
_Pm1001pcAlmLineDwAisDet_Type=EkiOnOff
_Pm1001pcAlmLineDwAisDet_Object=MibScalar
pm1001pcAlmLineDwAisDet=_Pm1001pcAlmLineDwAisDet_Object((1,3,6,1,4,1,20044,12,2,3,3,128,1),_Pm1001pcAlmLineDwAisDet_Type())
pm1001pcAlmLineDwAisDet.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDwAisDet.setStatus(_A)
_Pm1001pcAlmLineDwRdiDet_Type=EkiOnOff
_Pm1001pcAlmLineDwRdiDet_Object=MibScalar
pm1001pcAlmLineDwRdiDet=_Pm1001pcAlmLineDwRdiDet_Object((1,3,6,1,4,1,20044,12,2,3,3,128,2),_Pm1001pcAlmLineDwRdiDet_Type())
pm1001pcAlmLineDwRdiDet.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDwRdiDet.setStatus(_A)
_Pm1001pcAlmLineDwOof_Type=EkiOnOff
_Pm1001pcAlmLineDwOof_Object=MibScalar
pm1001pcAlmLineDwOof=_Pm1001pcAlmLineDwOof_Object((1,3,6,1,4,1,20044,12,2,3,3,128,3),_Pm1001pcAlmLineDwOof_Type())
pm1001pcAlmLineDwOof.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDwOof.setStatus(_H)
_Pm1001pcAlmLineDwLof_Type=EkiOnOff
_Pm1001pcAlmLineDwLof_Object=MibScalar
pm1001pcAlmLineDwLof=_Pm1001pcAlmLineDwLof_Object((1,3,6,1,4,1,20044,12,2,3,3,128,4),_Pm1001pcAlmLineDwLof_Type())
pm1001pcAlmLineDwLof.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDwLof.setStatus(_A)
_Pm1001pcAlmlineSyncAlarms_ObjectIdentity=ObjectIdentity
pm1001pcAlmlineSyncAlarms=_Pm1001pcAlmlineSyncAlarms_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,3,133))
_Pm1001pcAlmLineDwLockerr_Type=EkiOnOff
_Pm1001pcAlmLineDwLockerr_Object=MibScalar
pm1001pcAlmLineDwLockerr=_Pm1001pcAlmLineDwLockerr_Object((1,3,6,1,4,1,20044,12,2,3,3,133,12),_Pm1001pcAlmLineDwLockerr_Type())
pm1001pcAlmLineDwLockerr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDwLockerr.setStatus(_A)
_Pm1001pcAlmLineUpLockerr_Type=EkiOnOff
_Pm1001pcAlmLineUpLockerr_Object=MibScalar
pm1001pcAlmLineUpLockerr=_Pm1001pcAlmLineUpLockerr_Object((1,3,6,1,4,1,20044,12,2,3,3,133,13),_Pm1001pcAlmLineUpLockerr_Type())
pm1001pcAlmLineUpLockerr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineUpLockerr.setStatus(_A)
_Pm1001pcAlmLineDwLos_Type=EkiOnOff
_Pm1001pcAlmLineDwLos_Object=MibScalar
pm1001pcAlmLineDwLos=_Pm1001pcAlmLineDwLos_Object((1,3,6,1,4,1,20044,12,2,3,3,133,16),_Pm1001pcAlmLineDwLos_Type())
pm1001pcAlmLineDwLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineDwLos.setStatus(_A)
_Pm1001pcAlmlineXfpAlarms2_ObjectIdentity=ObjectIdentity
pm1001pcAlmlineXfpAlarms2=_Pm1001pcAlmlineXfpAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,12,2,3,3,211))
_Pm1001pcAlmLineModNr_Type=EkiOnOff
_Pm1001pcAlmLineModNr_Object=MibScalar
pm1001pcAlmLineModNr=_Pm1001pcAlmLineModNr_Object((1,3,6,1,4,1,20044,12,2,3,3,211,2),_Pm1001pcAlmLineModNr_Type())
pm1001pcAlmLineModNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineModNr.setStatus(_A)
_Pm1001pcAlmLineRxCdrNotLocked1_Type=EkiOnOff
_Pm1001pcAlmLineRxCdrNotLocked1_Object=MibScalar
pm1001pcAlmLineRxCdrNotLocked1=_Pm1001pcAlmLineRxCdrNotLocked1_Object((1,3,6,1,4,1,20044,12,2,3,3,211,3),_Pm1001pcAlmLineRxCdrNotLocked1_Type())
pm1001pcAlmLineRxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineRxCdrNotLocked1.setStatus(_A)
_Pm1001pcAlmLineRxNr_Type=EkiOnOff
_Pm1001pcAlmLineRxNr_Object=MibScalar
pm1001pcAlmLineRxNr=_Pm1001pcAlmLineRxNr_Object((1,3,6,1,4,1,20044,12,2,3,3,211,5),_Pm1001pcAlmLineRxNr_Type())
pm1001pcAlmLineRxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineRxNr.setStatus(_A)
_Pm1001pcAlmLineTxCdrNotLocked1_Type=EkiOnOff
_Pm1001pcAlmLineTxCdrNotLocked1_Object=MibScalar
pm1001pcAlmLineTxCdrNotLocked1=_Pm1001pcAlmLineTxCdrNotLocked1_Object((1,3,6,1,4,1,20044,12,2,3,3,211,6),_Pm1001pcAlmLineTxCdrNotLocked1_Type())
pm1001pcAlmLineTxCdrNotLocked1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxCdrNotLocked1.setStatus(_A)
_Pm1001pcAlmLineTxFault_Type=EkiOnOff
_Pm1001pcAlmLineTxFault_Object=MibScalar
pm1001pcAlmLineTxFault=_Pm1001pcAlmLineTxFault_Object((1,3,6,1,4,1,20044,12,2,3,3,211,7),_Pm1001pcAlmLineTxFault_Type())
pm1001pcAlmLineTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxFault.setStatus(_A)
_Pm1001pcAlmLineTxNr_Type=EkiOnOff
_Pm1001pcAlmLineTxNr_Object=MibScalar
pm1001pcAlmLineTxNr=_Pm1001pcAlmLineTxNr_Object((1,3,6,1,4,1,20044,12,2,3,3,211,8),_Pm1001pcAlmLineTxNr_Type())
pm1001pcAlmLineTxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTxNr.setStatus(_A)
_Pm1001pcAlmLineWavelengthUnlocked_Type=EkiOnOff
_Pm1001pcAlmLineWavelengthUnlocked_Object=MibScalar
pm1001pcAlmLineWavelengthUnlocked=_Pm1001pcAlmLineWavelengthUnlocked_Object((1,3,6,1,4,1,20044,12,2,3,3,211,14),_Pm1001pcAlmLineWavelengthUnlocked_Type())
pm1001pcAlmLineWavelengthUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineWavelengthUnlocked.setStatus(_A)
_Pm1001pcAlmLineTecFault_Type=EkiOnOff
_Pm1001pcAlmLineTecFault_Object=MibScalar
pm1001pcAlmLineTecFault=_Pm1001pcAlmLineTecFault_Object((1,3,6,1,4,1,20044,12,2,3,3,211,15),_Pm1001pcAlmLineTecFault_Type())
pm1001pcAlmLineTecFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineTecFault.setStatus(_A)
_Pm1001pcAlmLineApdSupplyFault_Type=EkiOnOff
_Pm1001pcAlmLineApdSupplyFault_Object=MibScalar
pm1001pcAlmLineApdSupplyFault=_Pm1001pcAlmLineApdSupplyFault_Object((1,3,6,1,4,1,20044,12,2,3,3,211,16),_Pm1001pcAlmLineApdSupplyFault_Type())
pm1001pcAlmLineApdSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcAlmLineApdSupplyFault.setStatus(_A)
_Pm1001pcmeasures_ObjectIdentity=ObjectIdentity
pm1001pcmeasures=_Pm1001pcmeasures_ObjectIdentity((1,3,6,1,4,1,20044,12,3))
_Pm1001pcMesrOther_ObjectIdentity=ObjectIdentity
pm1001pcMesrOther=_Pm1001pcMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,12,3,1))
_Pm1001pcMesrsynth0_Type=EkiMeasureType
_Pm1001pcMesrsynth0_Object=MibScalar
pm1001pcMesrsynth0=_Pm1001pcMesrsynth0_Object((1,3,6,1,4,1,20044,12,3,1,0),_Pm1001pcMesrsynth0_Type())
pm1001pcMesrsynth0.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrsynth0.setStatus(_H)
_Pm1001pcMesrsynth1_Type=EkiMeasureType
_Pm1001pcMesrsynth1_Object=MibScalar
pm1001pcMesrsynth1=_Pm1001pcMesrsynth1_Object((1,3,6,1,4,1,20044,12,3,1,1),_Pm1001pcMesrsynth1_Type())
pm1001pcMesrsynth1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrsynth1.setStatus(_H)
_Pm1001pcMesrClient_ObjectIdentity=ObjectIdentity
pm1001pcMesrClient=_Pm1001pcMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,12,3,2))
class _Pm1001pcMesrclientModTempMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrclientModTempMeas_Type.__name__=_F
_Pm1001pcMesrclientModTempMeas_Object=MibScalar
pm1001pcMesrclientModTempMeas=_Pm1001pcMesrclientModTempMeas_Object((1,3,6,1,4,1,20044,12,3,2,16),_Pm1001pcMesrclientModTempMeas_Type())
pm1001pcMesrclientModTempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrclientModTempMeas.setStatus(_A)
class _Pm1001pcMesrclientBiasCurrentMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrclientBiasCurrentMeas_Type.__name__=_F
_Pm1001pcMesrclientBiasCurrentMeas_Object=MibScalar
pm1001pcMesrclientBiasCurrentMeas=_Pm1001pcMesrclientBiasCurrentMeas_Object((1,3,6,1,4,1,20044,12,3,2,32),_Pm1001pcMesrclientBiasCurrentMeas_Type())
pm1001pcMesrclientBiasCurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrclientBiasCurrentMeas.setStatus(_A)
class _Pm1001pcMesrclientTxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrclientTxPowerMeas_Type.__name__=_F
_Pm1001pcMesrclientTxPowerMeas_Object=MibScalar
pm1001pcMesrclientTxPowerMeas=_Pm1001pcMesrclientTxPowerMeas_Object((1,3,6,1,4,1,20044,12,3,2,40),_Pm1001pcMesrclientTxPowerMeas_Type())
pm1001pcMesrclientTxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrclientTxPowerMeas.setStatus(_A)
class _Pm1001pcMesrclientRxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrclientRxPowerMeas_Type.__name__=_F
_Pm1001pcMesrclientRxPowerMeas_Object=MibScalar
pm1001pcMesrclientRxPowerMeas=_Pm1001pcMesrclientRxPowerMeas_Object((1,3,6,1,4,1,20044,12,3,2,48),_Pm1001pcMesrclientRxPowerMeas_Type())
pm1001pcMesrclientRxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrclientRxPowerMeas.setStatus(_A)
_Pm1001pcMesrLine_ObjectIdentity=ObjectIdentity
pm1001pcMesrLine=_Pm1001pcMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,12,3,3))
class _Pm1001pcMesrlineModTempMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineModTempMeas_Type.__name__=_F
_Pm1001pcMesrlineModTempMeas_Object=MibScalar
pm1001pcMesrlineModTempMeas=_Pm1001pcMesrlineModTempMeas_Object((1,3,6,1,4,1,20044,12,3,3,208),_Pm1001pcMesrlineModTempMeas_Type())
pm1001pcMesrlineModTempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineModTempMeas.setStatus(_A)
class _Pm1001pcMesrlineReserved_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineReserved_Type.__name__=_F
_Pm1001pcMesrlineReserved_Object=MibScalar
pm1001pcMesrlineReserved=_Pm1001pcMesrlineReserved_Object((1,3,6,1,4,1,20044,12,3,3,209),_Pm1001pcMesrlineReserved_Type())
pm1001pcMesrlineReserved.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineReserved.setStatus(_H)
class _Pm1001pcMesrlineBiasCurrentMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineBiasCurrentMeas_Type.__name__=_F
_Pm1001pcMesrlineBiasCurrentMeas_Object=MibScalar
pm1001pcMesrlineBiasCurrentMeas=_Pm1001pcMesrlineBiasCurrentMeas_Object((1,3,6,1,4,1,20044,12,3,3,210),_Pm1001pcMesrlineBiasCurrentMeas_Type())
pm1001pcMesrlineBiasCurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineBiasCurrentMeas.setStatus(_A)
class _Pm1001pcMesrlineTxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineTxPowerMeas_Type.__name__=_F
_Pm1001pcMesrlineTxPowerMeas_Object=MibScalar
pm1001pcMesrlineTxPowerMeas=_Pm1001pcMesrlineTxPowerMeas_Object((1,3,6,1,4,1,20044,12,3,3,211),_Pm1001pcMesrlineTxPowerMeas_Type())
pm1001pcMesrlineTxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineTxPowerMeas.setStatus(_A)
class _Pm1001pcMesrlineRxPowerMeas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineRxPowerMeas_Type.__name__=_F
_Pm1001pcMesrlineRxPowerMeas_Object=MibScalar
pm1001pcMesrlineRxPowerMeas=_Pm1001pcMesrlineRxPowerMeas_Object((1,3,6,1,4,1,20044,12,3,3,212),_Pm1001pcMesrlineRxPowerMeas_Type())
pm1001pcMesrlineRxPowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineRxPowerMeas.setStatus(_A)
class _Pm1001pcMesrlineAux1Meas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineAux1Meas_Type.__name__=_F
_Pm1001pcMesrlineAux1Meas_Object=MibScalar
pm1001pcMesrlineAux1Meas=_Pm1001pcMesrlineAux1Meas_Object((1,3,6,1,4,1,20044,12,3,3,213),_Pm1001pcMesrlineAux1Meas_Type())
pm1001pcMesrlineAux1Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineAux1Meas.setStatus(_H)
class _Pm1001pcMesrlineAux2Meas_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1001pcMesrlineAux2Meas_Type.__name__=_F
_Pm1001pcMesrlineAux2Meas_Object=MibScalar
pm1001pcMesrlineAux2Meas=_Pm1001pcMesrlineAux2Meas_Object((1,3,6,1,4,1,20044,12,3,3,214),_Pm1001pcMesrlineAux2Meas_Type())
pm1001pcMesrlineAux2Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMesrlineAux2Meas.setStatus(_H)
_Pm1001pccounters_ObjectIdentity=ObjectIdentity
pm1001pccounters=_Pm1001pccounters_ObjectIdentity((1,3,6,1,4,1,20044,12,4))
_Pm1001pcCntOther_ObjectIdentity=ObjectIdentity
pm1001pcCntOther=_Pm1001pcCntOther_ObjectIdentity((1,3,6,1,4,1,20044,12,4,1))
_Pm1001pcCntClient_ObjectIdentity=ObjectIdentity
pm1001pcCntClient=_Pm1001pcCntClient_ObjectIdentity((1,3,6,1,4,1,20044,12,4,2))
_Pm1001pcCntclientUpErrCntTable_Object=MibTable
pm1001pcCntclientUpErrCntTable=_Pm1001pcCntclientUpErrCntTable_Object((1,3,6,1,4,1,20044,12,4,2,32))
if mibBuilder.loadTexts:pm1001pcCntclientUpErrCntTable.setStatus(_A)
_Pm1001pcCntclientUpErrCntEntry_Object=MibTableRow
pm1001pcCntclientUpErrCntEntry=_Pm1001pcCntclientUpErrCntEntry_Object((1,3,6,1,4,1,20044,12,4,2,32,1))
pm1001pcCntclientUpErrCntEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:pm1001pcCntclientUpErrCntEntry.setStatus(_A)
class _Pm1001pcCntclientUpErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntclientUpErrCntIndex_Type.__name__=_E
_Pm1001pcCntclientUpErrCntIndex_Object=MibTableColumn
pm1001pcCntclientUpErrCntIndex=_Pm1001pcCntclientUpErrCntIndex_Object((1,3,6,1,4,1,20044,12,4,2,32,1,1),_Pm1001pcCntclientUpErrCntIndex_Type())
pm1001pcCntclientUpErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpErrCntIndex.setStatus(_A)
_Pm1001pcCntclientUpErrCntValuePortn_Type=Counter32
_Pm1001pcCntclientUpErrCntValuePortn_Object=MibTableColumn
pm1001pcCntclientUpErrCntValuePortn=_Pm1001pcCntclientUpErrCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,2,32,1,2),_Pm1001pcCntclientUpErrCntValuePortn_Type())
pm1001pcCntclientUpErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpErrCntValuePortn.setStatus(_A)
_Pm1001pcCntclientUpErrCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntclientUpErrCntErrorPortn_Object=MibTableColumn
pm1001pcCntclientUpErrCntErrorPortn=_Pm1001pcCntclientUpErrCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,2,32,1,3),_Pm1001pcCntclientUpErrCntErrorPortn_Type())
pm1001pcCntclientUpErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpErrCntErrorPortn.setStatus(_A)
_Pm1001pcCntclientUpErrCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntclientUpErrCntOverloadPortn_Object=MibTableColumn
pm1001pcCntclientUpErrCntOverloadPortn=_Pm1001pcCntclientUpErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,2,32,1,4),_Pm1001pcCntclientUpErrCntOverloadPortn_Type())
pm1001pcCntclientUpErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpErrCntOverloadPortn.setStatus(_A)
_Pm1001pcCntclientUpTimCntTable_Object=MibTable
pm1001pcCntclientUpTimCntTable=_Pm1001pcCntclientUpTimCntTable_Object((1,3,6,1,4,1,20044,12,4,2,40))
if mibBuilder.loadTexts:pm1001pcCntclientUpTimCntTable.setStatus(_A)
_Pm1001pcCntclientUpTimCntEntry_Object=MibTableRow
pm1001pcCntclientUpTimCntEntry=_Pm1001pcCntclientUpTimCntEntry_Object((1,3,6,1,4,1,20044,12,4,2,40,1))
pm1001pcCntclientUpTimCntEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pm1001pcCntclientUpTimCntEntry.setStatus(_A)
class _Pm1001pcCntclientUpTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntclientUpTimCntIndex_Type.__name__=_E
_Pm1001pcCntclientUpTimCntIndex_Object=MibTableColumn
pm1001pcCntclientUpTimCntIndex=_Pm1001pcCntclientUpTimCntIndex_Object((1,3,6,1,4,1,20044,12,4,2,40,1,1),_Pm1001pcCntclientUpTimCntIndex_Type())
pm1001pcCntclientUpTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpTimCntIndex.setStatus(_A)
_Pm1001pcCntclientUpTimCntValuePortn_Type=Counter32
_Pm1001pcCntclientUpTimCntValuePortn_Object=MibTableColumn
pm1001pcCntclientUpTimCntValuePortn=_Pm1001pcCntclientUpTimCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,2,40,1,2),_Pm1001pcCntclientUpTimCntValuePortn_Type())
pm1001pcCntclientUpTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpTimCntValuePortn.setStatus(_A)
_Pm1001pcCntclientUpTimCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntclientUpTimCntErrorPortn_Object=MibTableColumn
pm1001pcCntclientUpTimCntErrorPortn=_Pm1001pcCntclientUpTimCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,2,40,1,3),_Pm1001pcCntclientUpTimCntErrorPortn_Type())
pm1001pcCntclientUpTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpTimCntErrorPortn.setStatus(_A)
_Pm1001pcCntclientUpTimCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntclientUpTimCntOverloadPortn_Object=MibTableColumn
pm1001pcCntclientUpTimCntOverloadPortn=_Pm1001pcCntclientUpTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,2,40,1,4),_Pm1001pcCntclientUpTimCntOverloadPortn_Type())
pm1001pcCntclientUpTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientUpTimCntOverloadPortn.setStatus(_A)
_Pm1001pcCntclientDwErrCntTable_Object=MibTable
pm1001pcCntclientDwErrCntTable=_Pm1001pcCntclientDwErrCntTable_Object((1,3,6,1,4,1,20044,12,4,2,64))
if mibBuilder.loadTexts:pm1001pcCntclientDwErrCntTable.setStatus(_A)
_Pm1001pcCntclientDwErrCntEntry_Object=MibTableRow
pm1001pcCntclientDwErrCntEntry=_Pm1001pcCntclientDwErrCntEntry_Object((1,3,6,1,4,1,20044,12,4,2,64,1))
pm1001pcCntclientDwErrCntEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pm1001pcCntclientDwErrCntEntry.setStatus(_A)
class _Pm1001pcCntclientDwErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntclientDwErrCntIndex_Type.__name__=_E
_Pm1001pcCntclientDwErrCntIndex_Object=MibTableColumn
pm1001pcCntclientDwErrCntIndex=_Pm1001pcCntclientDwErrCntIndex_Object((1,3,6,1,4,1,20044,12,4,2,64,1,1),_Pm1001pcCntclientDwErrCntIndex_Type())
pm1001pcCntclientDwErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwErrCntIndex.setStatus(_A)
_Pm1001pcCntclientDwErrCntValuePortn_Type=Counter32
_Pm1001pcCntclientDwErrCntValuePortn_Object=MibTableColumn
pm1001pcCntclientDwErrCntValuePortn=_Pm1001pcCntclientDwErrCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,2,64,1,2),_Pm1001pcCntclientDwErrCntValuePortn_Type())
pm1001pcCntclientDwErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwErrCntValuePortn.setStatus(_A)
_Pm1001pcCntclientDwErrCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntclientDwErrCntErrorPortn_Object=MibTableColumn
pm1001pcCntclientDwErrCntErrorPortn=_Pm1001pcCntclientDwErrCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,2,64,1,3),_Pm1001pcCntclientDwErrCntErrorPortn_Type())
pm1001pcCntclientDwErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwErrCntErrorPortn.setStatus(_A)
_Pm1001pcCntclientDwErrCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntclientDwErrCntOverloadPortn_Object=MibTableColumn
pm1001pcCntclientDwErrCntOverloadPortn=_Pm1001pcCntclientDwErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,2,64,1,4),_Pm1001pcCntclientDwErrCntOverloadPortn_Type())
pm1001pcCntclientDwErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwErrCntOverloadPortn.setStatus(_A)
_Pm1001pcCntclientDwTimCntTable_Object=MibTable
pm1001pcCntclientDwTimCntTable=_Pm1001pcCntclientDwTimCntTable_Object((1,3,6,1,4,1,20044,12,4,2,72))
if mibBuilder.loadTexts:pm1001pcCntclientDwTimCntTable.setStatus(_A)
_Pm1001pcCntclientDwTimCntEntry_Object=MibTableRow
pm1001pcCntclientDwTimCntEntry=_Pm1001pcCntclientDwTimCntEntry_Object((1,3,6,1,4,1,20044,12,4,2,72,1))
pm1001pcCntclientDwTimCntEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm1001pcCntclientDwTimCntEntry.setStatus(_A)
class _Pm1001pcCntclientDwTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntclientDwTimCntIndex_Type.__name__=_E
_Pm1001pcCntclientDwTimCntIndex_Object=MibTableColumn
pm1001pcCntclientDwTimCntIndex=_Pm1001pcCntclientDwTimCntIndex_Object((1,3,6,1,4,1,20044,12,4,2,72,1,1),_Pm1001pcCntclientDwTimCntIndex_Type())
pm1001pcCntclientDwTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwTimCntIndex.setStatus(_A)
_Pm1001pcCntclientDwTimCntValuePortn_Type=Counter32
_Pm1001pcCntclientDwTimCntValuePortn_Object=MibTableColumn
pm1001pcCntclientDwTimCntValuePortn=_Pm1001pcCntclientDwTimCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,2,72,1,2),_Pm1001pcCntclientDwTimCntValuePortn_Type())
pm1001pcCntclientDwTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwTimCntValuePortn.setStatus(_A)
_Pm1001pcCntclientDwTimCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntclientDwTimCntErrorPortn_Object=MibTableColumn
pm1001pcCntclientDwTimCntErrorPortn=_Pm1001pcCntclientDwTimCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,2,72,1,3),_Pm1001pcCntclientDwTimCntErrorPortn_Type())
pm1001pcCntclientDwTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwTimCntErrorPortn.setStatus(_A)
_Pm1001pcCntclientDwTimCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntclientDwTimCntOverloadPortn_Object=MibTableColumn
pm1001pcCntclientDwTimCntOverloadPortn=_Pm1001pcCntclientDwTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,2,72,1,4),_Pm1001pcCntclientDwTimCntOverloadPortn_Type())
pm1001pcCntclientDwTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntclientDwTimCntOverloadPortn.setStatus(_A)
_Pm1001pcCntLine_ObjectIdentity=ObjectIdentity
pm1001pcCntLine=_Pm1001pcCntLine_ObjectIdentity((1,3,6,1,4,1,20044,12,4,3))
_Pm1001pcCntlineDfrmErrCntTable_Object=MibTable
pm1001pcCntlineDfrmErrCntTable=_Pm1001pcCntlineDfrmErrCntTable_Object((1,3,6,1,4,1,20044,12,4,3,152))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntTable.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntEntry_Object=MibTableRow
pm1001pcCntlineDfrmErrCntEntry=_Pm1001pcCntlineDfrmErrCntEntry_Object((1,3,6,1,4,1,20044,12,4,3,152,1))
pm1001pcCntlineDfrmErrCntEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntEntry.setStatus(_A)
class _Pm1001pcCntlineDfrmErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntlineDfrmErrCntIndex_Type.__name__=_E
_Pm1001pcCntlineDfrmErrCntIndex_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntIndex=_Pm1001pcCntlineDfrmErrCntIndex_Object((1,3,6,1,4,1,20044,12,4,3,152,1,1),_Pm1001pcCntlineDfrmErrCntIndex_Type())
pm1001pcCntlineDfrmErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntIndex.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntValuePortn_Type=Counter32
_Pm1001pcCntlineDfrmErrCntValuePortn_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntValuePortn=_Pm1001pcCntlineDfrmErrCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,3,152,1,2),_Pm1001pcCntlineDfrmErrCntValuePortn_Type())
pm1001pcCntlineDfrmErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntValuePortn.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmErrCntErrorPortn_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntErrorPortn=_Pm1001pcCntlineDfrmErrCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,3,152,1,3),_Pm1001pcCntlineDfrmErrCntErrorPortn_Type())
pm1001pcCntlineDfrmErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntErrorPortn.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmErrCntOverloadPortn_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntOverloadPortn=_Pm1001pcCntlineDfrmErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,3,152,1,4),_Pm1001pcCntlineDfrmErrCntOverloadPortn_Type())
pm1001pcCntlineDfrmErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntOverloadPortn.setStatus(_A)
_Pm1001pcCntlineDfrmTimCntTable_Object=MibTable
pm1001pcCntlineDfrmTimCntTable=_Pm1001pcCntlineDfrmTimCntTable_Object((1,3,6,1,4,1,20044,12,4,3,153))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmTimCntTable.setStatus(_A)
_Pm1001pcCntlineDfrmTimCntEntry_Object=MibTableRow
pm1001pcCntlineDfrmTimCntEntry=_Pm1001pcCntlineDfrmTimCntEntry_Object((1,3,6,1,4,1,20044,12,4,3,153,1))
pm1001pcCntlineDfrmTimCntEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmTimCntEntry.setStatus(_A)
class _Pm1001pcCntlineDfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntlineDfrmTimCntIndex_Type.__name__=_E
_Pm1001pcCntlineDfrmTimCntIndex_Object=MibTableColumn
pm1001pcCntlineDfrmTimCntIndex=_Pm1001pcCntlineDfrmTimCntIndex_Object((1,3,6,1,4,1,20044,12,4,3,153,1,1),_Pm1001pcCntlineDfrmTimCntIndex_Type())
pm1001pcCntlineDfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmTimCntIndex.setStatus(_A)
_Pm1001pcCntlineDfrmTimCntValuePortn_Type=Counter32
_Pm1001pcCntlineDfrmTimCntValuePortn_Object=MibTableColumn
pm1001pcCntlineDfrmTimCntValuePortn=_Pm1001pcCntlineDfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,3,153,1,2),_Pm1001pcCntlineDfrmTimCntValuePortn_Type())
pm1001pcCntlineDfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmTimCntValuePortn.setStatus(_A)
_Pm1001pcCntlineDfrmTimCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmTimCntErrorPortn_Object=MibTableColumn
pm1001pcCntlineDfrmTimCntErrorPortn=_Pm1001pcCntlineDfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,3,153,1,3),_Pm1001pcCntlineDfrmTimCntErrorPortn_Type())
pm1001pcCntlineDfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmTimCntErrorPortn.setStatus(_A)
_Pm1001pcCntlineDfrmTimCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmTimCntOverloadPortn_Object=MibTableColumn
pm1001pcCntlineDfrmTimCntOverloadPortn=_Pm1001pcCntlineDfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,3,153,1,4),_Pm1001pcCntlineDfrmTimCntOverloadPortn_Type())
pm1001pcCntlineDfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmTimCntOverloadPortn.setStatus(_A)
_Pm1001pcCntlineDfrmPrimErrCntTable_Object=MibTable
pm1001pcCntlineDfrmPrimErrCntTable=_Pm1001pcCntlineDfrmPrimErrCntTable_Object((1,3,6,1,4,1,20044,12,4,3,154))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmPrimErrCntTable.setStatus(_A)
_Pm1001pcCntlineDfrmPrimErrCntEntry_Object=MibTableRow
pm1001pcCntlineDfrmPrimErrCntEntry=_Pm1001pcCntlineDfrmPrimErrCntEntry_Object((1,3,6,1,4,1,20044,12,4,3,154,1))
pm1001pcCntlineDfrmPrimErrCntEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmPrimErrCntEntry.setStatus(_A)
class _Pm1001pcCntlineDfrmPrimErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntlineDfrmPrimErrCntIndex_Type.__name__=_E
_Pm1001pcCntlineDfrmPrimErrCntIndex_Object=MibTableColumn
pm1001pcCntlineDfrmPrimErrCntIndex=_Pm1001pcCntlineDfrmPrimErrCntIndex_Object((1,3,6,1,4,1,20044,12,4,3,154,1,1),_Pm1001pcCntlineDfrmPrimErrCntIndex_Type())
pm1001pcCntlineDfrmPrimErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmPrimErrCntIndex.setStatus(_A)
_Pm1001pcCntlineDfrmPrimErrCntValuePortn_Type=Counter32
_Pm1001pcCntlineDfrmPrimErrCntValuePortn_Object=MibTableColumn
pm1001pcCntlineDfrmPrimErrCntValuePortn=_Pm1001pcCntlineDfrmPrimErrCntValuePortn_Object((1,3,6,1,4,1,20044,12,4,3,154,1,2),_Pm1001pcCntlineDfrmPrimErrCntValuePortn_Type())
pm1001pcCntlineDfrmPrimErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmPrimErrCntValuePortn.setStatus(_A)
_Pm1001pcCntlineDfrmPrimErrCntErrorPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmPrimErrCntErrorPortn_Object=MibTableColumn
pm1001pcCntlineDfrmPrimErrCntErrorPortn=_Pm1001pcCntlineDfrmPrimErrCntErrorPortn_Object((1,3,6,1,4,1,20044,12,4,3,154,1,3),_Pm1001pcCntlineDfrmPrimErrCntErrorPortn_Type())
pm1001pcCntlineDfrmPrimErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmPrimErrCntErrorPortn.setStatus(_A)
_Pm1001pcCntlineDfrmPrimErrCntOverloadPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmPrimErrCntOverloadPortn_Object=MibTableColumn
pm1001pcCntlineDfrmPrimErrCntOverloadPortn=_Pm1001pcCntlineDfrmPrimErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,3,154,1,4),_Pm1001pcCntlineDfrmPrimErrCntOverloadPortn_Type())
pm1001pcCntlineDfrmPrimErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmPrimErrCntOverloadPortn.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntSTable_Object=MibTable
pm1001pcCntlineDfrmErrCntSTable=_Pm1001pcCntlineDfrmErrCntSTable_Object((1,3,6,1,4,1,20044,12,4,3,1160))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntSTable.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntSEntry_Object=MibTableRow
pm1001pcCntlineDfrmErrCntSEntry=_Pm1001pcCntlineDfrmErrCntSEntry_Object((1,3,6,1,4,1,20044,12,4,3,1160,1))
pm1001pcCntlineDfrmErrCntSEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntSEntry.setStatus(_A)
class _Pm1001pcCntlineDfrmErrCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCntlineDfrmErrCntSIndex_Type.__name__=_E
_Pm1001pcCntlineDfrmErrCntSIndex_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntSIndex=_Pm1001pcCntlineDfrmErrCntSIndex_Object((1,3,6,1,4,1,20044,12,4,3,1160,1,1),_Pm1001pcCntlineDfrmErrCntSIndex_Type())
pm1001pcCntlineDfrmErrCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntSIndex.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntSValuePortn_Type=Counter32
_Pm1001pcCntlineDfrmErrCntSValuePortn_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntSValuePortn=_Pm1001pcCntlineDfrmErrCntSValuePortn_Object((1,3,6,1,4,1,20044,12,4,3,1160,1,2),_Pm1001pcCntlineDfrmErrCntSValuePortn_Type())
pm1001pcCntlineDfrmErrCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntSValuePortn.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntSErrorPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmErrCntSErrorPortn_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntSErrorPortn=_Pm1001pcCntlineDfrmErrCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,4,3,1160,1,3),_Pm1001pcCntlineDfrmErrCntSErrorPortn_Type())
pm1001pcCntlineDfrmErrCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntSErrorPortn.setStatus(_A)
_Pm1001pcCntlineDfrmErrCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcCntlineDfrmErrCntSOverloadPortn_Object=MibTableColumn
pm1001pcCntlineDfrmErrCntSOverloadPortn=_Pm1001pcCntlineDfrmErrCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,4,3,1160,1,4),_Pm1001pcCntlineDfrmErrCntSOverloadPortn_Type())
pm1001pcCntlineDfrmErrCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCntlineDfrmErrCntSOverloadPortn.setStatus(_A)
_Pm1001pcCntCountersReset_Type=EkiOnOff
_Pm1001pcCntCountersReset_Object=MibScalar
pm1001pcCntCountersReset=_Pm1001pcCntCountersReset_Object((1,3,6,1,4,1,20044,12,4,259),_Pm1001pcCntCountersReset_Type())
pm1001pcCntCountersReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCntCountersReset.setStatus(_A)
_Pm1001pcCntCountersStop_Type=EkiOnOff
_Pm1001pcCntCountersStop_Object=MibScalar
pm1001pcCntCountersStop=_Pm1001pcCntCountersStop_Object((1,3,6,1,4,1,20044,12,4,260),_Pm1001pcCntCountersStop_Type())
pm1001pcCntCountersStop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCntCountersStop.setStatus(_A)
_Pm1001pccontrolsWrite_ObjectIdentity=ObjectIdentity
pm1001pccontrolsWrite=_Pm1001pccontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,12,6))
_Pm1001pcCtrlOther_ObjectIdentity=ObjectIdentity
pm1001pcCtrlOther=_Pm1001pcCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1))
_Pm1001pcCtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pm1001pcCtrlconfMgnt1=_Pm1001pcCtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,1))
_Pm1001pcCtrlConf1Load1_Type=EkiOnOff
_Pm1001pcCtrlConf1Load1_Object=MibScalar
pm1001pcCtrlConf1Load1=_Pm1001pcCtrlConf1Load1_Object((1,3,6,1,4,1,20044,12,6,1,1,1),_Pm1001pcCtrlConf1Load1_Type())
pm1001pcCtrlConf1Load1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlConf1Load1.setStatus(_A)
_Pm1001pcCtrlConf2Load1_Type=EkiOnOff
_Pm1001pcCtrlConf2Load1_Object=MibScalar
pm1001pcCtrlConf2Load1=_Pm1001pcCtrlConf2Load1_Object((1,3,6,1,4,1,20044,12,6,1,1,2),_Pm1001pcCtrlConf2Load1_Type())
pm1001pcCtrlConf2Load1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlConf2Load1.setStatus(_A)
_Pm1001pcCtrlConf2Flash1_Type=EkiOnOff
_Pm1001pcCtrlConf2Flash1_Object=MibScalar
pm1001pcCtrlConf2Flash1=_Pm1001pcCtrlConf2Flash1_Object((1,3,6,1,4,1,20044,12,6,1,1,10),_Pm1001pcCtrlConf2Flash1_Type())
pm1001pcCtrlConf2Flash1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlConf2Flash1.setStatus(_A)
_Pm1001pcCtrlConf2Clear1_Type=EkiOnOff
_Pm1001pcCtrlConf2Clear1_Object=MibScalar
pm1001pcCtrlConf2Clear1=_Pm1001pcCtrlConf2Clear1_Object((1,3,6,1,4,1,20044,12,6,1,1,14),_Pm1001pcCtrlConf2Clear1_Type())
pm1001pcCtrlConf2Clear1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlConf2Clear1.setStatus(_A)
_Pm1001pcCtrlsynth4_ObjectIdentity=ObjectIdentity
pm1001pcCtrlsynth4=_Pm1001pcCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,4))
_Pm1001pcCtrlCorrelatOn_Type=EkiOnOff
_Pm1001pcCtrlCorrelatOn_Object=MibScalar
pm1001pcCtrlCorrelatOn=_Pm1001pcCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,12,6,1,4,1),_Pm1001pcCtrlCorrelatOn_Type())
pm1001pcCtrlCorrelatOn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlCorrelatOn.setStatus(_A)
_Pm1001pcCtrlCorrelatOff_Type=EkiOnOff
_Pm1001pcCtrlCorrelatOff_Object=MibScalar
pm1001pcCtrlCorrelatOff=_Pm1001pcCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,12,6,1,4,2),_Pm1001pcCtrlCorrelatOff_Type())
pm1001pcCtrlCorrelatOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlCorrelatOff.setStatus(_A)
_Pm1001pcCtrlswMgnt_ObjectIdentity=ObjectIdentity
pm1001pcCtrlswMgnt=_Pm1001pcCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,5))
_Pm1001pcCtrlColdReset_Type=EkiOnOff
_Pm1001pcCtrlColdReset_Object=MibScalar
pm1001pcCtrlColdReset=_Pm1001pcCtrlColdReset_Object((1,3,6,1,4,1,20044,12,6,1,5,2),_Pm1001pcCtrlColdReset_Type())
pm1001pcCtrlColdReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlColdReset.setStatus(_A)
_Pm1001pcCtrlWarmReset_Type=EkiOnOff
_Pm1001pcCtrlWarmReset_Object=MibScalar
pm1001pcCtrlWarmReset=_Pm1001pcCtrlWarmReset_Object((1,3,6,1,4,1,20044,12,6,1,5,3),_Pm1001pcCtrlWarmReset_Type())
pm1001pcCtrlWarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlWarmReset.setStatus(_A)
_Pm1001pcCtrlLoadSwBank1_Type=EkiOnOff
_Pm1001pcCtrlLoadSwBank1_Object=MibScalar
pm1001pcCtrlLoadSwBank1=_Pm1001pcCtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,12,6,1,5,5),_Pm1001pcCtrlLoadSwBank1_Type())
pm1001pcCtrlLoadSwBank1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLoadSwBank1.setStatus(_A)
_Pm1001pcCtrlLoadSwBank2_Type=EkiOnOff
_Pm1001pcCtrlLoadSwBank2_Object=MibScalar
pm1001pcCtrlLoadSwBank2=_Pm1001pcCtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,12,6,1,5,6),_Pm1001pcCtrlLoadSwBank2_Type())
pm1001pcCtrlLoadSwBank2.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLoadSwBank2.setStatus(_A)
_Pm1001pcCtrlgwMgnt_ObjectIdentity=ObjectIdentity
pm1001pcCtrlgwMgnt=_Pm1001pcCtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,6))
_Pm1001pcCtrlCurrentGwReset_Type=EkiOnOff
_Pm1001pcCtrlCurrentGwReset_Object=MibScalar
pm1001pcCtrlCurrentGwReset=_Pm1001pcCtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,12,6,1,6,1),_Pm1001pcCtrlCurrentGwReset_Type())
pm1001pcCtrlCurrentGwReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlCurrentGwReset.setStatus(_A)
_Pm1001pcCtrlLoadGwBank1_Type=EkiOnOff
_Pm1001pcCtrlLoadGwBank1_Object=MibScalar
pm1001pcCtrlLoadGwBank1=_Pm1001pcCtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,12,6,1,6,5),_Pm1001pcCtrlLoadGwBank1_Type())
pm1001pcCtrlLoadGwBank1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLoadGwBank1.setStatus(_A)
_Pm1001pcCtrlLoadGwBank2_Type=EkiOnOff
_Pm1001pcCtrlLoadGwBank2_Object=MibScalar
pm1001pcCtrlLoadGwBank2=_Pm1001pcCtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,12,6,1,6,6),_Pm1001pcCtrlLoadGwBank2_Type())
pm1001pcCtrlLoadGwBank2.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLoadGwBank2.setStatus(_A)
_Pm1001pcCtrlLoadGwBank3_Type=EkiOnOff
_Pm1001pcCtrlLoadGwBank3_Object=MibScalar
pm1001pcCtrlLoadGwBank3=_Pm1001pcCtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,12,6,1,6,7),_Pm1001pcCtrlLoadGwBank3_Type())
pm1001pcCtrlLoadGwBank3.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLoadGwBank3.setStatus(_A)
_Pm1001pcCtrlLoadGwBank4_Type=EkiOnOff
_Pm1001pcCtrlLoadGwBank4_Object=MibScalar
pm1001pcCtrlLoadGwBank4=_Pm1001pcCtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,12,6,1,6,8),_Pm1001pcCtrlLoadGwBank4_Type())
pm1001pcCtrlLoadGwBank4.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLoadGwBank4.setStatus(_A)
_Pm1001pcCtrlledTest_ObjectIdentity=ObjectIdentity
pm1001pcCtrlledTest=_Pm1001pcCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,192))
_Pm1001pcCtrlGreenLed_Type=EkiOnOff
_Pm1001pcCtrlGreenLed_Object=MibScalar
pm1001pcCtrlGreenLed=_Pm1001pcCtrlGreenLed_Object((1,3,6,1,4,1,20044,12,6,1,192,1),_Pm1001pcCtrlGreenLed_Type())
pm1001pcCtrlGreenLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlGreenLed.setStatus(_A)
_Pm1001pcCtrlRedLed_Type=EkiOnOff
_Pm1001pcCtrlRedLed_Object=MibScalar
pm1001pcCtrlRedLed=_Pm1001pcCtrlRedLed_Object((1,3,6,1,4,1,20044,12,6,1,192,2),_Pm1001pcCtrlRedLed_Type())
pm1001pcCtrlRedLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlRedLed.setStatus(_A)
_Pm1001pcCtrlLedOff_Type=EkiOnOff
_Pm1001pcCtrlLedOff_Object=MibScalar
pm1001pcCtrlLedOff=_Pm1001pcCtrlLedOff_Object((1,3,6,1,4,1,20044,12,6,1,192,3),_Pm1001pcCtrlLedOff_Type())
pm1001pcCtrlLedOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLedOff.setStatus(_A)
_Pm1001pcCtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm1001pcCtrlmoduleOosMode=_Pm1001pcCtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,193))
_Pm1001pcCtrlModuleOosMode_Type=EkiOnOff
_Pm1001pcCtrlModuleOosMode_Object=MibScalar
pm1001pcCtrlModuleOosMode=_Pm1001pcCtrlModuleOosMode_Object((1,3,6,1,4,1,20044,12,6,1,193,1),_Pm1001pcCtrlModuleOosMode_Type())
pm1001pcCtrlModuleOosMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlModuleOosMode.setStatus(_A)
_Pm1001pcCtrlmaintenanceMode_ObjectIdentity=ObjectIdentity
pm1001pcCtrlmaintenanceMode=_Pm1001pcCtrlmaintenanceMode_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,197))
_Pm1001pcCtrlMaintenanceMode_Type=EkiOnOff
_Pm1001pcCtrlMaintenanceMode_Object=MibScalar
pm1001pcCtrlMaintenanceMode=_Pm1001pcCtrlMaintenanceMode_Object((1,3,6,1,4,1,20044,12,6,1,197,1),_Pm1001pcCtrlMaintenanceMode_Type())
pm1001pcCtrlMaintenanceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlMaintenanceMode.setStatus(_A)
_Pm1001pcCtrldccEnable_ObjectIdentity=ObjectIdentity
pm1001pcCtrldccEnable=_Pm1001pcCtrldccEnable_ObjectIdentity((1,3,6,1,4,1,20044,12,6,1,198))
_Pm1001pcCtrlDccEnable_Type=EkiOnOff
_Pm1001pcCtrlDccEnable_Object=MibScalar
pm1001pcCtrlDccEnable=_Pm1001pcCtrlDccEnable_Object((1,3,6,1,4,1,20044,12,6,1,198,1),_Pm1001pcCtrlDccEnable_Type())
pm1001pcCtrlDccEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlDccEnable.setStatus(_A)
_Pm1001pcCtrlClient_ObjectIdentity=ObjectIdentity
pm1001pcCtrlClient=_Pm1001pcCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,12,6,2))
_Pm1001pcCtrlaccessLoopTable_Object=MibTable
pm1001pcCtrlaccessLoopTable=_Pm1001pcCtrlaccessLoopTable_Object((1,3,6,1,4,1,20044,12,6,2,16))
if mibBuilder.loadTexts:pm1001pcCtrlaccessLoopTable.setStatus(_A)
_Pm1001pcCtrlaccessLoopEntry_Object=MibTableRow
pm1001pcCtrlaccessLoopEntry=_Pm1001pcCtrlaccessLoopEntry_Object((1,3,6,1,4,1,20044,12,6,2,16,1))
pm1001pcCtrlaccessLoopEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm1001pcCtrlaccessLoopEntry.setStatus(_A)
class _Pm1001pcCtrlaccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlaccessLoopIndex_Type.__name__=_E
_Pm1001pcCtrlaccessLoopIndex_Object=MibTableColumn
pm1001pcCtrlaccessLoopIndex=_Pm1001pcCtrlaccessLoopIndex_Object((1,3,6,1,4,1,20044,12,6,2,16,1,1),_Pm1001pcCtrlaccessLoopIndex_Type())
pm1001pcCtrlaccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlaccessLoopIndex.setStatus(_A)
_Pm1001pcCtrlaccessLoopPortn_Type=EkiState
_Pm1001pcCtrlaccessLoopPortn_Object=MibTableColumn
pm1001pcCtrlaccessLoopPortn=_Pm1001pcCtrlaccessLoopPortn_Object((1,3,6,1,4,1,20044,12,6,2,16,1,2),_Pm1001pcCtrlaccessLoopPortn_Type())
pm1001pcCtrlaccessLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlaccessLoopPortn.setStatus(_A)
_Pm1001pcCtrlportOosModeTable_Object=MibTable
pm1001pcCtrlportOosModeTable=_Pm1001pcCtrlportOosModeTable_Object((1,3,6,1,4,1,20044,12,6,2,18))
if mibBuilder.loadTexts:pm1001pcCtrlportOosModeTable.setStatus(_A)
_Pm1001pcCtrlportOosModeEntry_Object=MibTableRow
pm1001pcCtrlportOosModeEntry=_Pm1001pcCtrlportOosModeEntry_Object((1,3,6,1,4,1,20044,12,6,2,18,1))
pm1001pcCtrlportOosModeEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm1001pcCtrlportOosModeEntry.setStatus(_A)
class _Pm1001pcCtrlportOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlportOosModeIndex_Type.__name__=_E
_Pm1001pcCtrlportOosModeIndex_Object=MibTableColumn
pm1001pcCtrlportOosModeIndex=_Pm1001pcCtrlportOosModeIndex_Object((1,3,6,1,4,1,20044,12,6,2,18,1,1),_Pm1001pcCtrlportOosModeIndex_Type())
pm1001pcCtrlportOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlportOosModeIndex.setStatus(_A)
_Pm1001pcCtrlportOosModePortn_Type=EkiState
_Pm1001pcCtrlportOosModePortn_Object=MibTableColumn
pm1001pcCtrlportOosModePortn=_Pm1001pcCtrlportOosModePortn_Object((1,3,6,1,4,1,20044,12,6,2,18,1,2),_Pm1001pcCtrlportOosModePortn_Type())
pm1001pcCtrlportOosModePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlportOosModePortn.setStatus(_A)
_Pm1001pcCtrlxfpOffCtrlTable_Object=MibTable
pm1001pcCtrlxfpOffCtrlTable=_Pm1001pcCtrlxfpOffCtrlTable_Object((1,3,6,1,4,1,20044,12,6,2,20))
if mibBuilder.loadTexts:pm1001pcCtrlxfpOffCtrlTable.setStatus(_A)
_Pm1001pcCtrlxfpOffCtrlEntry_Object=MibTableRow
pm1001pcCtrlxfpOffCtrlEntry=_Pm1001pcCtrlxfpOffCtrlEntry_Object((1,3,6,1,4,1,20044,12,6,2,20,1))
pm1001pcCtrlxfpOffCtrlEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm1001pcCtrlxfpOffCtrlEntry.setStatus(_A)
class _Pm1001pcCtrlxfpOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlxfpOffCtrlIndex_Type.__name__=_E
_Pm1001pcCtrlxfpOffCtrlIndex_Object=MibTableColumn
pm1001pcCtrlxfpOffCtrlIndex=_Pm1001pcCtrlxfpOffCtrlIndex_Object((1,3,6,1,4,1,20044,12,6,2,20,1,1),_Pm1001pcCtrlxfpOffCtrlIndex_Type())
pm1001pcCtrlxfpOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlxfpOffCtrlIndex.setStatus(_A)
_Pm1001pcCtrlxfpOffCtrlPortn_Type=EkiState
_Pm1001pcCtrlxfpOffCtrlPortn_Object=MibTableColumn
pm1001pcCtrlxfpOffCtrlPortn=_Pm1001pcCtrlxfpOffCtrlPortn_Object((1,3,6,1,4,1,20044,12,6,2,20,1,2),_Pm1001pcCtrlxfpOffCtrlPortn_Type())
pm1001pcCtrlxfpOffCtrlPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlxfpOffCtrlPortn.setStatus(_A)
_Pm1001pcCtrlcsfUpInsTable_Object=MibTable
pm1001pcCtrlcsfUpInsTable=_Pm1001pcCtrlcsfUpInsTable_Object((1,3,6,1,4,1,20044,12,6,2,21))
if mibBuilder.loadTexts:pm1001pcCtrlcsfUpInsTable.setStatus(_A)
_Pm1001pcCtrlcsfUpInsEntry_Object=MibTableRow
pm1001pcCtrlcsfUpInsEntry=_Pm1001pcCtrlcsfUpInsEntry_Object((1,3,6,1,4,1,20044,12,6,2,21,1))
pm1001pcCtrlcsfUpInsEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm1001pcCtrlcsfUpInsEntry.setStatus(_A)
class _Pm1001pcCtrlcsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlcsfUpInsIndex_Type.__name__=_E
_Pm1001pcCtrlcsfUpInsIndex_Object=MibTableColumn
pm1001pcCtrlcsfUpInsIndex=_Pm1001pcCtrlcsfUpInsIndex_Object((1,3,6,1,4,1,20044,12,6,2,21,1,1),_Pm1001pcCtrlcsfUpInsIndex_Type())
pm1001pcCtrlcsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlcsfUpInsIndex.setStatus(_A)
_Pm1001pcCtrlcsfUpInsPortn_Type=EkiState
_Pm1001pcCtrlcsfUpInsPortn_Object=MibTableColumn
pm1001pcCtrlcsfUpInsPortn=_Pm1001pcCtrlcsfUpInsPortn_Object((1,3,6,1,4,1,20044,12,6,2,21,1,2),_Pm1001pcCtrlcsfUpInsPortn_Type())
pm1001pcCtrlcsfUpInsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlcsfUpInsPortn.setStatus(_A)
_Pm1001pcCtrlcaisDwInsTable_Object=MibTable
pm1001pcCtrlcaisDwInsTable=_Pm1001pcCtrlcaisDwInsTable_Object((1,3,6,1,4,1,20044,12,6,2,22))
if mibBuilder.loadTexts:pm1001pcCtrlcaisDwInsTable.setStatus(_A)
_Pm1001pcCtrlcaisDwInsEntry_Object=MibTableRow
pm1001pcCtrlcaisDwInsEntry=_Pm1001pcCtrlcaisDwInsEntry_Object((1,3,6,1,4,1,20044,12,6,2,22,1))
pm1001pcCtrlcaisDwInsEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm1001pcCtrlcaisDwInsEntry.setStatus(_A)
class _Pm1001pcCtrlcaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlcaisDwInsIndex_Type.__name__=_E
_Pm1001pcCtrlcaisDwInsIndex_Object=MibTableColumn
pm1001pcCtrlcaisDwInsIndex=_Pm1001pcCtrlcaisDwInsIndex_Object((1,3,6,1,4,1,20044,12,6,2,22,1,1),_Pm1001pcCtrlcaisDwInsIndex_Type())
pm1001pcCtrlcaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlcaisDwInsIndex.setStatus(_A)
_Pm1001pcCtrlcaisDwInsPortn_Type=EkiState
_Pm1001pcCtrlcaisDwInsPortn_Object=MibTableColumn
pm1001pcCtrlcaisDwInsPortn=_Pm1001pcCtrlcaisDwInsPortn_Object((1,3,6,1,4,1,20044,12,6,2,22,1,2),_Pm1001pcCtrlcaisDwInsPortn_Type())
pm1001pcCtrlcaisDwInsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlcaisDwInsPortn.setStatus(_A)
_Pm1001pcCtrlflowControlTable_Object=MibTable
pm1001pcCtrlflowControlTable=_Pm1001pcCtrlflowControlTable_Object((1,3,6,1,4,1,20044,12,6,2,23))
if mibBuilder.loadTexts:pm1001pcCtrlflowControlTable.setStatus(_A)
_Pm1001pcCtrlflowControlEntry_Object=MibTableRow
pm1001pcCtrlflowControlEntry=_Pm1001pcCtrlflowControlEntry_Object((1,3,6,1,4,1,20044,12,6,2,23,1))
pm1001pcCtrlflowControlEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm1001pcCtrlflowControlEntry.setStatus(_A)
class _Pm1001pcCtrlflowControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlflowControlIndex_Type.__name__=_E
_Pm1001pcCtrlflowControlIndex_Object=MibTableColumn
pm1001pcCtrlflowControlIndex=_Pm1001pcCtrlflowControlIndex_Object((1,3,6,1,4,1,20044,12,6,2,23,1,1),_Pm1001pcCtrlflowControlIndex_Type())
pm1001pcCtrlflowControlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlflowControlIndex.setStatus(_A)
_Pm1001pcCtrlflowControlPortn_Type=EkiState
_Pm1001pcCtrlflowControlPortn_Object=MibTableColumn
pm1001pcCtrlflowControlPortn=_Pm1001pcCtrlflowControlPortn_Object((1,3,6,1,4,1,20044,12,6,2,23,1,2),_Pm1001pcCtrlflowControlPortn_Type())
pm1001pcCtrlflowControlPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlflowControlPortn.setStatus(_A)
class _Pm1001pcCtrlfiberLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pm1001pcCtrlfiberLength_Type.__name__=_F
_Pm1001pcCtrlfiberLength_Object=MibScalar
pm1001pcCtrlfiberLength=_Pm1001pcCtrlfiberLength_Object((1,3,6,1,4,1,20044,12,6,2,25),_Pm1001pcCtrlfiberLength_Type())
pm1001pcCtrlfiberLength.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlfiberLength.setStatus(_A)
_Pm1001pcCtrlclientAccessTermLoopTable_Object=MibTable
pm1001pcCtrlclientAccessTermLoopTable=_Pm1001pcCtrlclientAccessTermLoopTable_Object((1,3,6,1,4,1,20044,12,6,2,26))
if mibBuilder.loadTexts:pm1001pcCtrlclientAccessTermLoopTable.setStatus(_A)
_Pm1001pcCtrlclientAccessTermLoopEntry_Object=MibTableRow
pm1001pcCtrlclientAccessTermLoopEntry=_Pm1001pcCtrlclientAccessTermLoopEntry_Object((1,3,6,1,4,1,20044,12,6,2,26,1))
pm1001pcCtrlclientAccessTermLoopEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm1001pcCtrlclientAccessTermLoopEntry.setStatus(_A)
class _Pm1001pcCtrlclientAccessTermLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlclientAccessTermLoopIndex_Type.__name__=_E
_Pm1001pcCtrlclientAccessTermLoopIndex_Object=MibTableColumn
pm1001pcCtrlclientAccessTermLoopIndex=_Pm1001pcCtrlclientAccessTermLoopIndex_Object((1,3,6,1,4,1,20044,12,6,2,26,1,1),_Pm1001pcCtrlclientAccessTermLoopIndex_Type())
pm1001pcCtrlclientAccessTermLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlclientAccessTermLoopIndex.setStatus(_A)
_Pm1001pcCtrlclientAccessTermLoopPortn_Type=EkiState
_Pm1001pcCtrlclientAccessTermLoopPortn_Object=MibTableColumn
pm1001pcCtrlclientAccessTermLoopPortn=_Pm1001pcCtrlclientAccessTermLoopPortn_Object((1,3,6,1,4,1,20044,12,6,2,26,1,2),_Pm1001pcCtrlclientAccessTermLoopPortn_Type())
pm1001pcCtrlclientAccessTermLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlclientAccessTermLoopPortn.setStatus(_A)
_Pm1001pcCtrlxfpXfiLoopTable_Object=MibTable
pm1001pcCtrlxfpXfiLoopTable=_Pm1001pcCtrlxfpXfiLoopTable_Object((1,3,6,1,4,1,20044,12,6,2,39))
if mibBuilder.loadTexts:pm1001pcCtrlxfpXfiLoopTable.setStatus(_A)
_Pm1001pcCtrlxfpXfiLoopEntry_Object=MibTableRow
pm1001pcCtrlxfpXfiLoopEntry=_Pm1001pcCtrlxfpXfiLoopEntry_Object((1,3,6,1,4,1,20044,12,6,2,39,1))
pm1001pcCtrlxfpXfiLoopEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm1001pcCtrlxfpXfiLoopEntry.setStatus(_A)
class _Pm1001pcCtrlxfpXfiLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlxfpXfiLoopIndex_Type.__name__=_E
_Pm1001pcCtrlxfpXfiLoopIndex_Object=MibTableColumn
pm1001pcCtrlxfpXfiLoopIndex=_Pm1001pcCtrlxfpXfiLoopIndex_Object((1,3,6,1,4,1,20044,12,6,2,39,1,1),_Pm1001pcCtrlxfpXfiLoopIndex_Type())
pm1001pcCtrlxfpXfiLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlxfpXfiLoopIndex.setStatus(_A)
_Pm1001pcCtrlxfpXfiLoopPortn_Type=EkiState
_Pm1001pcCtrlxfpXfiLoopPortn_Object=MibTableColumn
pm1001pcCtrlxfpXfiLoopPortn=_Pm1001pcCtrlxfpXfiLoopPortn_Object((1,3,6,1,4,1,20044,12,6,2,39,1,2),_Pm1001pcCtrlxfpXfiLoopPortn_Type())
pm1001pcCtrlxfpXfiLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlxfpXfiLoopPortn.setStatus(_A)
_Pm1001pcCtrlLine_ObjectIdentity=ObjectIdentity
pm1001pcCtrlLine=_Pm1001pcCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,12,6,3))
_Pm1001pcCtrlcommAccessLoop_ObjectIdentity=ObjectIdentity
pm1001pcCtrlcommAccessLoop=_Pm1001pcCtrlcommAccessLoop_ObjectIdentity((1,3,6,1,4,1,20044,12,6,3,64))
_Pm1001pcCtrlCommAccessloop_Type=EkiOnOff
_Pm1001pcCtrlCommAccessloop_Object=MibScalar
pm1001pcCtrlCommAccessloop=_Pm1001pcCtrlCommAccessloop_Object((1,3,6,1,4,1,20044,12,6,3,64,1),_Pm1001pcCtrlCommAccessloop_Type())
pm1001pcCtrlCommAccessloop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlCommAccessloop.setStatus(_H)
_Pm1001pcCtrllineLoop_ObjectIdentity=ObjectIdentity
pm1001pcCtrllineLoop=_Pm1001pcCtrllineLoop_ObjectIdentity((1,3,6,1,4,1,20044,12,6,3,66))
_Pm1001pcCtrlLineLoop_Type=EkiOnOff
_Pm1001pcCtrlLineLoop_Object=MibScalar
pm1001pcCtrlLineLoop=_Pm1001pcCtrlLineLoop_Object((1,3,6,1,4,1,20044,12,6,3,66,1),_Pm1001pcCtrlLineLoop_Type())
pm1001pcCtrlLineLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLineLoop.setStatus(_A)
_Pm1001pcCtrlmsAis_ObjectIdentity=ObjectIdentity
pm1001pcCtrlmsAis=_Pm1001pcCtrlmsAis_ObjectIdentity((1,3,6,1,4,1,20044,12,6,3,67))
_Pm1001pcCtrlMsAis_Type=EkiOnOff
_Pm1001pcCtrlMsAis_Object=MibScalar
pm1001pcCtrlMsAis=_Pm1001pcCtrlMsAis_Object((1,3,6,1,4,1,20044,12,6,3,67,1),_Pm1001pcCtrlMsAis_Type())
pm1001pcCtrlMsAis.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlMsAis.setStatus(_A)
_Pm1001pcCtrllineOosMode_ObjectIdentity=ObjectIdentity
pm1001pcCtrllineOosMode=_Pm1001pcCtrllineOosMode_ObjectIdentity((1,3,6,1,4,1,20044,12,6,3,74))
_Pm1001pcCtrlLineOosMode_Type=EkiOnOff
_Pm1001pcCtrlLineOosMode_Object=MibScalar
pm1001pcCtrlLineOosMode=_Pm1001pcCtrlLineOosMode_Object((1,3,6,1,4,1,20044,12,6,3,74,1),_Pm1001pcCtrlLineOosMode_Type())
pm1001pcCtrlLineOosMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlLineOosMode.setStatus(_A)
_Pm1001pcCtrlxfpOnoffTable_Object=MibTable
pm1001pcCtrlxfpOnoffTable=_Pm1001pcCtrlxfpOnoffTable_Object((1,3,6,1,4,1,20044,12,6,3,208))
if mibBuilder.loadTexts:pm1001pcCtrlxfpOnoffTable.setStatus(_A)
_Pm1001pcCtrlxfpOnoffEntry_Object=MibTableRow
pm1001pcCtrlxfpOnoffEntry=_Pm1001pcCtrlxfpOnoffEntry_Object((1,3,6,1,4,1,20044,12,6,3,208,1))
pm1001pcCtrlxfpOnoffEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm1001pcCtrlxfpOnoffEntry.setStatus(_A)
class _Pm1001pcCtrlxfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlxfpOnoffIndex_Type.__name__=_E
_Pm1001pcCtrlxfpOnoffIndex_Object=MibTableColumn
pm1001pcCtrlxfpOnoffIndex=_Pm1001pcCtrlxfpOnoffIndex_Object((1,3,6,1,4,1,20044,12,6,3,208,1,1),_Pm1001pcCtrlxfpOnoffIndex_Type())
pm1001pcCtrlxfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlxfpOnoffIndex.setStatus(_A)
_Pm1001pcCtrlxfpOnoffPortn_Type=EkiState
_Pm1001pcCtrlxfpOnoffPortn_Object=MibTableColumn
pm1001pcCtrlxfpOnoffPortn=_Pm1001pcCtrlxfpOnoffPortn_Object((1,3,6,1,4,1,20044,12,6,3,208,1,2),_Pm1001pcCtrlxfpOnoffPortn_Type())
pm1001pcCtrlxfpOnoffPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlxfpOnoffPortn.setStatus(_A)
_Pm1001pcCtrlxfpLineLoopTable_Object=MibTable
pm1001pcCtrlxfpLineLoopTable=_Pm1001pcCtrlxfpLineLoopTable_Object((1,3,6,1,4,1,20044,12,6,3,209))
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineLoopTable.setStatus(_A)
_Pm1001pcCtrlxfpLineLoopEntry_Object=MibTableRow
pm1001pcCtrlxfpLineLoopEntry=_Pm1001pcCtrlxfpLineLoopEntry_Object((1,3,6,1,4,1,20044,12,6,3,209,1))
pm1001pcCtrlxfpLineLoopEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineLoopEntry.setStatus(_A)
class _Pm1001pcCtrlxfpLineLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlxfpLineLoopIndex_Type.__name__=_E
_Pm1001pcCtrlxfpLineLoopIndex_Object=MibTableColumn
pm1001pcCtrlxfpLineLoopIndex=_Pm1001pcCtrlxfpLineLoopIndex_Object((1,3,6,1,4,1,20044,12,6,3,209,1,1),_Pm1001pcCtrlxfpLineLoopIndex_Type())
pm1001pcCtrlxfpLineLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineLoopIndex.setStatus(_A)
_Pm1001pcCtrlxfpLineLoopPortn_Type=EkiState
_Pm1001pcCtrlxfpLineLoopPortn_Object=MibTableColumn
pm1001pcCtrlxfpLineLoopPortn=_Pm1001pcCtrlxfpLineLoopPortn_Object((1,3,6,1,4,1,20044,12,6,3,209,1,2),_Pm1001pcCtrlxfpLineLoopPortn_Type())
pm1001pcCtrlxfpLineLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineLoopPortn.setStatus(_A)
_Pm1001pcCtrlxfpLineXfiLoopTable_Object=MibTable
pm1001pcCtrlxfpLineXfiLoopTable=_Pm1001pcCtrlxfpLineXfiLoopTable_Object((1,3,6,1,4,1,20044,12,6,3,210))
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineXfiLoopTable.setStatus(_A)
_Pm1001pcCtrlxfpLineXfiLoopEntry_Object=MibTableRow
pm1001pcCtrlxfpLineXfiLoopEntry=_Pm1001pcCtrlxfpLineXfiLoopEntry_Object((1,3,6,1,4,1,20044,12,6,3,210,1))
pm1001pcCtrlxfpLineXfiLoopEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineXfiLoopEntry.setStatus(_A)
class _Pm1001pcCtrlxfpLineXfiLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrlxfpLineXfiLoopIndex_Type.__name__=_E
_Pm1001pcCtrlxfpLineXfiLoopIndex_Object=MibTableColumn
pm1001pcCtrlxfpLineXfiLoopIndex=_Pm1001pcCtrlxfpLineXfiLoopIndex_Object((1,3,6,1,4,1,20044,12,6,3,210,1,1),_Pm1001pcCtrlxfpLineXfiLoopIndex_Type())
pm1001pcCtrlxfpLineXfiLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineXfiLoopIndex.setStatus(_A)
_Pm1001pcCtrlxfpLineXfiLoopPortn_Type=EkiState
_Pm1001pcCtrlxfpLineXfiLoopPortn_Object=MibTableColumn
pm1001pcCtrlxfpLineXfiLoopPortn=_Pm1001pcCtrlxfpLineXfiLoopPortn_Object((1,3,6,1,4,1,20044,12,6,3,210,1,2),_Pm1001pcCtrlxfpLineXfiLoopPortn_Type())
pm1001pcCtrlxfpLineXfiLoopPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrlxfpLineXfiLoopPortn.setStatus(_A)
_Pm1001pcCtrllineLoopTransceiverTable_Object=MibTable
pm1001pcCtrllineLoopTransceiverTable=_Pm1001pcCtrllineLoopTransceiverTable_Object((1,3,6,1,4,1,20044,12,6,3,218))
if mibBuilder.loadTexts:pm1001pcCtrllineLoopTransceiverTable.setStatus(_A)
_Pm1001pcCtrllineLoopTransceiverEntry_Object=MibTableRow
pm1001pcCtrllineLoopTransceiverEntry=_Pm1001pcCtrllineLoopTransceiverEntry_Object((1,3,6,1,4,1,20044,12,6,3,218,1))
pm1001pcCtrllineLoopTransceiverEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm1001pcCtrllineLoopTransceiverEntry.setStatus(_A)
class _Pm1001pcCtrllineLoopTransceiverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCtrllineLoopTransceiverIndex_Type.__name__=_E
_Pm1001pcCtrllineLoopTransceiverIndex_Object=MibTableColumn
pm1001pcCtrllineLoopTransceiverIndex=_Pm1001pcCtrllineLoopTransceiverIndex_Object((1,3,6,1,4,1,20044,12,6,3,218,1,1),_Pm1001pcCtrllineLoopTransceiverIndex_Type())
pm1001pcCtrllineLoopTransceiverIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCtrllineLoopTransceiverIndex.setStatus(_A)
_Pm1001pcCtrllineLoopTransceiverPortn_Type=EkiState
_Pm1001pcCtrllineLoopTransceiverPortn_Object=MibTableColumn
pm1001pcCtrllineLoopTransceiverPortn=_Pm1001pcCtrllineLoopTransceiverPortn_Object((1,3,6,1,4,1,20044,12,6,3,218,1,2),_Pm1001pcCtrllineLoopTransceiverPortn_Type())
pm1001pcCtrllineLoopTransceiverPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCtrllineLoopTransceiverPortn.setStatus(_A)
_Pm1001pcri_ObjectIdentity=ObjectIdentity
pm1001pcri=_Pm1001pcri_ObjectIdentity((1,3,6,1,4,1,20044,12,7))
_Pm1001pcriTable_ObjectIdentity=ObjectIdentity
pm1001pcriTable=_Pm1001pcriTable_ObjectIdentity((1,3,6,1,4,1,20044,12,7,1))
_Pm1001pcRinvReloadInventory_Type=EkiOnOff
_Pm1001pcRinvReloadInventory_Object=MibScalar
pm1001pcRinvReloadInventory=_Pm1001pcRinvReloadInventory_Object((1,3,6,1,4,1,20044,12,7,2),_Pm1001pcRinvReloadInventory_Type())
pm1001pcRinvReloadInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcRinvReloadInventory.setStatus(_A)
_Pm1001pcRinvHwPlatform_Type=DisplayString
_Pm1001pcRinvHwPlatform_Object=MibScalar
pm1001pcRinvHwPlatform=_Pm1001pcRinvHwPlatform_Object((1,3,6,1,4,1,20044,12,7,3),_Pm1001pcRinvHwPlatform_Type())
pm1001pcRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcRinvHwPlatform.setStatus(_A)
_Pm1001pcRinvModulePlatform_Type=DisplayString
_Pm1001pcRinvModulePlatform_Object=MibScalar
pm1001pcRinvModulePlatform=_Pm1001pcRinvModulePlatform_Object((1,3,6,1,4,1,20044,12,7,4),_Pm1001pcRinvModulePlatform_Type())
pm1001pcRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcRinvModulePlatform.setStatus(_A)
_Pm1001pcRinvSwPlatform_Type=DisplayString
_Pm1001pcRinvSwPlatform_Object=MibScalar
pm1001pcRinvSwPlatform=_Pm1001pcRinvSwPlatform_Object((1,3,6,1,4,1,20044,12,7,5),_Pm1001pcRinvSwPlatform_Type())
pm1001pcRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcRinvSwPlatform.setStatus(_A)
_Pm1001pcRinvGwPlatform_Type=DisplayString
_Pm1001pcRinvGwPlatform_Object=MibScalar
pm1001pcRinvGwPlatform=_Pm1001pcRinvGwPlatform_Object((1,3,6,1,4,1,20044,12,7,6),_Pm1001pcRinvGwPlatform_Type())
pm1001pcRinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcRinvGwPlatform.setStatus(_A)
_Pm1001pcRinvClient_Type=DisplayString
_Pm1001pcRinvClient_Object=MibScalar
pm1001pcRinvClient=_Pm1001pcRinvClient_Object((1,3,6,1,4,1,20044,12,7,7),_Pm1001pcRinvClient_Type())
pm1001pcRinvClient.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcRinvClient.setStatus(_A)
_Pm1001pcRinvLine_Type=DisplayString
_Pm1001pcRinvLine_Object=MibScalar
pm1001pcRinvLine=_Pm1001pcRinvLine_Object((1,3,6,1,4,1,20044,12,7,8),_Pm1001pcRinvLine_Type())
pm1001pcRinvLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcRinvLine.setStatus(_A)
_Pm1001pcdownload_ObjectIdentity=ObjectIdentity
pm1001pcdownload=_Pm1001pcdownload_ObjectIdentity((1,3,6,1,4,1,20044,12,8))
_Pm1001pcDwlOther_ObjectIdentity=ObjectIdentity
pm1001pcDwlOther=_Pm1001pcDwlOther_ObjectIdentity((1,3,6,1,4,1,20044,12,8,1))
_Pm1001pcDwlrestartProcess_ObjectIdentity=ObjectIdentity
pm1001pcDwlrestartProcess=_Pm1001pcDwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,12,8,1,0))
_Pm1001pcDwlWarmRestartProcessed_Type=EkiOnOff
_Pm1001pcDwlWarmRestartProcessed_Object=MibScalar
pm1001pcDwlWarmRestartProcessed=_Pm1001pcDwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,12,8,1,0,1),_Pm1001pcDwlWarmRestartProcessed_Type())
pm1001pcDwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlWarmRestartProcessed.setStatus(_A)
_Pm1001pcDwlColdRestartProcessed_Type=EkiOnOff
_Pm1001pcDwlColdRestartProcessed_Object=MibScalar
pm1001pcDwlColdRestartProcessed=_Pm1001pcDwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,12,8,1,0,2),_Pm1001pcDwlColdRestartProcessed_Type())
pm1001pcDwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlColdRestartProcessed.setStatus(_A)
_Pm1001pcDwlswBanksUsed_ObjectIdentity=ObjectIdentity
pm1001pcDwlswBanksUsed=_Pm1001pcDwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,12,8,1,1))
_Pm1001pcDwlSwBank1Used_Type=EkiOnOff
_Pm1001pcDwlSwBank1Used_Object=MibScalar
pm1001pcDwlSwBank1Used=_Pm1001pcDwlSwBank1Used_Object((1,3,6,1,4,1,20044,12,8,1,1,1),_Pm1001pcDwlSwBank1Used_Type())
pm1001pcDwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlSwBank1Used.setStatus(_A)
_Pm1001pcDwlSwBank2Used_Type=EkiOnOff
_Pm1001pcDwlSwBank2Used_Object=MibScalar
pm1001pcDwlSwBank2Used=_Pm1001pcDwlSwBank2Used_Object((1,3,6,1,4,1,20044,12,8,1,1,2),_Pm1001pcDwlSwBank2Used_Type())
pm1001pcDwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlSwBank2Used.setStatus(_A)
_Pm1001pcDwlSwBank1Notempty_Type=EkiOnOff
_Pm1001pcDwlSwBank1Notempty_Object=MibScalar
pm1001pcDwlSwBank1Notempty=_Pm1001pcDwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,12,8,1,1,5),_Pm1001pcDwlSwBank1Notempty_Type())
pm1001pcDwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlSwBank1Notempty.setStatus(_A)
_Pm1001pcDwlSwBank2Notempty_Type=EkiOnOff
_Pm1001pcDwlSwBank2Notempty_Object=MibScalar
pm1001pcDwlSwBank2Notempty=_Pm1001pcDwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,12,8,1,1,6),_Pm1001pcDwlSwBank2Notempty_Type())
pm1001pcDwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlSwBank2Notempty.setStatus(_A)
_Pm1001pcDwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pm1001pcDwlgwBanksUsed=_Pm1001pcDwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,12,8,1,2))
_Pm1001pcDwlGwBank1Used_Type=EkiOnOff
_Pm1001pcDwlGwBank1Used_Object=MibScalar
pm1001pcDwlGwBank1Used=_Pm1001pcDwlGwBank1Used_Object((1,3,6,1,4,1,20044,12,8,1,2,1),_Pm1001pcDwlGwBank1Used_Type())
pm1001pcDwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank1Used.setStatus(_A)
_Pm1001pcDwlGwBank2Used_Type=EkiOnOff
_Pm1001pcDwlGwBank2Used_Object=MibScalar
pm1001pcDwlGwBank2Used=_Pm1001pcDwlGwBank2Used_Object((1,3,6,1,4,1,20044,12,8,1,2,2),_Pm1001pcDwlGwBank2Used_Type())
pm1001pcDwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank2Used.setStatus(_H)
_Pm1001pcDwlGwBank3Used_Type=EkiOnOff
_Pm1001pcDwlGwBank3Used_Object=MibScalar
pm1001pcDwlGwBank3Used=_Pm1001pcDwlGwBank3Used_Object((1,3,6,1,4,1,20044,12,8,1,2,3),_Pm1001pcDwlGwBank3Used_Type())
pm1001pcDwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank3Used.setStatus(_A)
_Pm1001pcDwlGwBank4Used_Type=EkiOnOff
_Pm1001pcDwlGwBank4Used_Object=MibScalar
pm1001pcDwlGwBank4Used=_Pm1001pcDwlGwBank4Used_Object((1,3,6,1,4,1,20044,12,8,1,2,4),_Pm1001pcDwlGwBank4Used_Type())
pm1001pcDwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank4Used.setStatus(_H)
_Pm1001pcDwlGwBank1Notempty_Type=EkiOnOff
_Pm1001pcDwlGwBank1Notempty_Object=MibScalar
pm1001pcDwlGwBank1Notempty=_Pm1001pcDwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,12,8,1,2,5),_Pm1001pcDwlGwBank1Notempty_Type())
pm1001pcDwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank1Notempty.setStatus(_A)
_Pm1001pcDwlGwBank2Notempty_Type=EkiOnOff
_Pm1001pcDwlGwBank2Notempty_Object=MibScalar
pm1001pcDwlGwBank2Notempty=_Pm1001pcDwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,12,8,1,2,6),_Pm1001pcDwlGwBank2Notempty_Type())
pm1001pcDwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank2Notempty.setStatus(_H)
_Pm1001pcDwlGwBank3Notempty_Type=EkiOnOff
_Pm1001pcDwlGwBank3Notempty_Object=MibScalar
pm1001pcDwlGwBank3Notempty=_Pm1001pcDwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,12,8,1,2,7),_Pm1001pcDwlGwBank3Notempty_Type())
pm1001pcDwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank3Notempty.setStatus(_A)
_Pm1001pcDwlGwBank4Notempty_Type=EkiOnOff
_Pm1001pcDwlGwBank4Notempty_Object=MibScalar
pm1001pcDwlGwBank4Notempty=_Pm1001pcDwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,12,8,1,2,8),_Pm1001pcDwlGwBank4Notempty_Type())
pm1001pcDwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcDwlGwBank4Notempty.setStatus(_H)
_Pm1001pcDwlClient_ObjectIdentity=ObjectIdentity
pm1001pcDwlClient=_Pm1001pcDwlClient_ObjectIdentity((1,3,6,1,4,1,20044,12,8,2))
_Pm1001pcDwlLine_ObjectIdentity=ObjectIdentity
pm1001pcDwlLine=_Pm1001pcDwlLine_ObjectIdentity((1,3,6,1,4,1,20044,12,8,3))
_Pm1001pcrmon_ObjectIdentity=ObjectIdentity
pm1001pcrmon=_Pm1001pcrmon_ObjectIdentity((1,3,6,1,4,1,20044,12,9))
_Pm1001pcRmonOther_ObjectIdentity=ObjectIdentity
pm1001pcRmonOther=_Pm1001pcRmonOther_ObjectIdentity((1,3,6,1,4,1,20044,12,9,1))
_Pm1001pcMonCountersReset_Type=EkiOnOff
_Pm1001pcMonCountersReset_Object=MibScalar
pm1001pcMonCountersReset=_Pm1001pcMonCountersReset_Object((1,3,6,1,4,1,20044,12,9,1,359),_Pm1001pcMonCountersReset_Type())
pm1001pcMonCountersReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcMonCountersReset.setStatus(_A)
_Pm1001pcMonCountersStop_Type=EkiOnOff
_Pm1001pcMonCountersStop_Object=MibScalar
pm1001pcMonCountersStop=_Pm1001pcMonCountersStop_Object((1,3,6,1,4,1,20044,12,9,1,360),_Pm1001pcMonCountersStop_Type())
pm1001pcMonCountersStop.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcMonCountersStop.setStatus(_A)
_Pm1001pcRmonClient_ObjectIdentity=ObjectIdentity
pm1001pcRmonClient=_Pm1001pcRmonClient_ObjectIdentity((1,3,6,1,4,1,20044,12,9,2))
_Pm1001pcMonupRmonByteCntTable_Object=MibTable
pm1001pcMonupRmonByteCntTable=_Pm1001pcMonupRmonByteCntTable_Object((1,3,6,1,4,1,20044,12,9,2,16))
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntTable.setStatus(_A)
_Pm1001pcMonupRmonByteCntEntry_Object=MibTableRow
pm1001pcMonupRmonByteCntEntry=_Pm1001pcMonupRmonByteCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,16,1))
pm1001pcMonupRmonByteCntEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonByteCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonByteCntIndex_Object=MibTableColumn
pm1001pcMonupRmonByteCntIndex=_Pm1001pcMonupRmonByteCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,16,1,1),_Pm1001pcMonupRmonByteCntIndex_Type())
pm1001pcMonupRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntIndex.setStatus(_A)
_Pm1001pcMonupRmonByteCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonByteCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonByteCntValuePortn=_Pm1001pcMonupRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,16,1,2),_Pm1001pcMonupRmonByteCntValuePortn_Type())
pm1001pcMonupRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonByteCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonByteCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonByteCntErrorPortn=_Pm1001pcMonupRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,16,1,3),_Pm1001pcMonupRmonByteCntErrorPortn_Type())
pm1001pcMonupRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonByteCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonByteCntOverloadPortn=_Pm1001pcMonupRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,16,1,4),_Pm1001pcMonupRmonByteCntOverloadPortn_Type())
pm1001pcMonupRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntTable_Object=MibTable
pm1001pcMonupRmonCrcErrorCntTable=_Pm1001pcMonupRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,12,9,2,24))
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntTable.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntEntry_Object=MibTableRow
pm1001pcMonupRmonCrcErrorCntEntry=_Pm1001pcMonupRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,24,1))
pm1001pcMonupRmonCrcErrorCntEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonCrcErrorCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonCrcErrorCntIndex_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntIndex=_Pm1001pcMonupRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,24,1,1),_Pm1001pcMonupRmonCrcErrorCntIndex_Type())
pm1001pcMonupRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntIndex.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntValuePortn=_Pm1001pcMonupRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,24,1,2),_Pm1001pcMonupRmonCrcErrorCntValuePortn_Type())
pm1001pcMonupRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntErrorPortn=_Pm1001pcMonupRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,24,1,3),_Pm1001pcMonupRmonCrcErrorCntErrorPortn_Type())
pm1001pcMonupRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntOverloadPortn=_Pm1001pcMonupRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,24,1,4),_Pm1001pcMonupRmonCrcErrorCntOverloadPortn_Type())
pm1001pcMonupRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntTable_Object=MibTable
pm1001pcMonupRmonPacketsCntTable=_Pm1001pcMonupRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,12,9,2,32))
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntTable.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntEntry_Object=MibTableRow
pm1001pcMonupRmonPacketsCntEntry=_Pm1001pcMonupRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,32,1))
pm1001pcMonupRmonPacketsCntEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonPacketsCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonPacketsCntIndex_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntIndex=_Pm1001pcMonupRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,32,1,1),_Pm1001pcMonupRmonPacketsCntIndex_Type())
pm1001pcMonupRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntIndex.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonPacketsCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntValuePortn=_Pm1001pcMonupRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,32,1,2),_Pm1001pcMonupRmonPacketsCntValuePortn_Type())
pm1001pcMonupRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPacketsCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntErrorPortn=_Pm1001pcMonupRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,32,1,3),_Pm1001pcMonupRmonPacketsCntErrorPortn_Type())
pm1001pcMonupRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntOverloadPortn=_Pm1001pcMonupRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,32,1,4),_Pm1001pcMonupRmonPacketsCntOverloadPortn_Type())
pm1001pcMonupRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntTable_Object=MibTable
pm1001pcMonupRmonBroadcastCntTable=_Pm1001pcMonupRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,12,9,2,40))
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntTable.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntEntry_Object=MibTableRow
pm1001pcMonupRmonBroadcastCntEntry=_Pm1001pcMonupRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,40,1))
pm1001pcMonupRmonBroadcastCntEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonBroadcastCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonBroadcastCntIndex_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntIndex=_Pm1001pcMonupRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,40,1,1),_Pm1001pcMonupRmonBroadcastCntIndex_Type())
pm1001pcMonupRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntIndex.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonBroadcastCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntValuePortn=_Pm1001pcMonupRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,40,1,2),_Pm1001pcMonupRmonBroadcastCntValuePortn_Type())
pm1001pcMonupRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntErrorPortn=_Pm1001pcMonupRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,40,1,3),_Pm1001pcMonupRmonBroadcastCntErrorPortn_Type())
pm1001pcMonupRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntOverloadPortn=_Pm1001pcMonupRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,40,1,4),_Pm1001pcMonupRmonBroadcastCntOverloadPortn_Type())
pm1001pcMonupRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntTable_Object=MibTable
pm1001pcMonupRmonMulticastCntTable=_Pm1001pcMonupRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,12,9,2,48))
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntTable.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntEntry_Object=MibTableRow
pm1001pcMonupRmonMulticastCntEntry=_Pm1001pcMonupRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,48,1))
pm1001pcMonupRmonMulticastCntEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonMulticastCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonMulticastCntIndex_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntIndex=_Pm1001pcMonupRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,48,1,1),_Pm1001pcMonupRmonMulticastCntIndex_Type())
pm1001pcMonupRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntIndex.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonMulticastCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntValuePortn=_Pm1001pcMonupRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,48,1,2),_Pm1001pcMonupRmonMulticastCntValuePortn_Type())
pm1001pcMonupRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonMulticastCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntErrorPortn=_Pm1001pcMonupRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,48,1,3),_Pm1001pcMonupRmonMulticastCntErrorPortn_Type())
pm1001pcMonupRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntOverloadPortn=_Pm1001pcMonupRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,48,1,4),_Pm1001pcMonupRmonMulticastCntOverloadPortn_Type())
pm1001pcMonupRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonTimerCntTable_Object=MibTable
pm1001pcMonupRmonTimerCntTable=_Pm1001pcMonupRmonTimerCntTable_Object((1,3,6,1,4,1,20044,12,9,2,56))
if mibBuilder.loadTexts:pm1001pcMonupRmonTimerCntTable.setStatus(_A)
_Pm1001pcMonupRmonTimerCntEntry_Object=MibTableRow
pm1001pcMonupRmonTimerCntEntry=_Pm1001pcMonupRmonTimerCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,56,1))
pm1001pcMonupRmonTimerCntEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm1001pcMonupRmonTimerCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonTimerCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonTimerCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonTimerCntIndex_Object=MibTableColumn
pm1001pcMonupRmonTimerCntIndex=_Pm1001pcMonupRmonTimerCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,56,1,1),_Pm1001pcMonupRmonTimerCntIndex_Type())
pm1001pcMonupRmonTimerCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonTimerCntIndex.setStatus(_A)
_Pm1001pcMonupRmonTimerCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonTimerCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonTimerCntValuePortn=_Pm1001pcMonupRmonTimerCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,56,1,2),_Pm1001pcMonupRmonTimerCntValuePortn_Type())
pm1001pcMonupRmonTimerCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonTimerCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonTimerCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonTimerCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonTimerCntErrorPortn=_Pm1001pcMonupRmonTimerCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,56,1,3),_Pm1001pcMonupRmonTimerCntErrorPortn_Type())
pm1001pcMonupRmonTimerCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonTimerCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonTimerCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonTimerCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonTimerCntOverloadPortn=_Pm1001pcMonupRmonTimerCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,56,1,4),_Pm1001pcMonupRmonTimerCntOverloadPortn_Type())
pm1001pcMonupRmonTimerCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonTimerCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntTable_Object=MibTable
pm1001pcMonupRmonPauseFrameCntTable=_Pm1001pcMonupRmonPauseFrameCntTable_Object((1,3,6,1,4,1,20044,12,9,2,64))
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntTable.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntEntry_Object=MibTableRow
pm1001pcMonupRmonPauseFrameCntEntry=_Pm1001pcMonupRmonPauseFrameCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,64,1))
pm1001pcMonupRmonPauseFrameCntEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonPauseFrameCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonPauseFrameCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonPauseFrameCntIndex_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntIndex=_Pm1001pcMonupRmonPauseFrameCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,64,1,1),_Pm1001pcMonupRmonPauseFrameCntIndex_Type())
pm1001pcMonupRmonPauseFrameCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntIndex.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonPauseFrameCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntValuePortn=_Pm1001pcMonupRmonPauseFrameCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,64,1,2),_Pm1001pcMonupRmonPauseFrameCntValuePortn_Type())
pm1001pcMonupRmonPauseFrameCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPauseFrameCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntErrorPortn=_Pm1001pcMonupRmonPauseFrameCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,64,1,3),_Pm1001pcMonupRmonPauseFrameCntErrorPortn_Type())
pm1001pcMonupRmonPauseFrameCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPauseFrameCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntOverloadPortn=_Pm1001pcMonupRmonPauseFrameCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,64,1,4),_Pm1001pcMonupRmonPauseFrameCntOverloadPortn_Type())
pm1001pcMonupRmonPauseFrameCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntTable_Object=MibTable
pm1001pcMonupRmonDropFrameCntTable=_Pm1001pcMonupRmonDropFrameCntTable_Object((1,3,6,1,4,1,20044,12,9,2,72))
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntTable.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntEntry_Object=MibTableRow
pm1001pcMonupRmonDropFrameCntEntry=_Pm1001pcMonupRmonDropFrameCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,72,1))
pm1001pcMonupRmonDropFrameCntEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonDropFrameCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonDropFrameCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonDropFrameCntIndex_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntIndex=_Pm1001pcMonupRmonDropFrameCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,72,1,1),_Pm1001pcMonupRmonDropFrameCntIndex_Type())
pm1001pcMonupRmonDropFrameCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntIndex.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonDropFrameCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntValuePortn=_Pm1001pcMonupRmonDropFrameCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,72,1,2),_Pm1001pcMonupRmonDropFrameCntValuePortn_Type())
pm1001pcMonupRmonDropFrameCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonDropFrameCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntErrorPortn=_Pm1001pcMonupRmonDropFrameCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,72,1,3),_Pm1001pcMonupRmonDropFrameCntErrorPortn_Type())
pm1001pcMonupRmonDropFrameCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonDropFrameCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntOverloadPortn=_Pm1001pcMonupRmonDropFrameCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,72,1,4),_Pm1001pcMonupRmonDropFrameCntOverloadPortn_Type())
pm1001pcMonupRmonDropFrameCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonBitsCntTable_Object=MibTable
pm1001pcMonupRmonBitsCntTable=_Pm1001pcMonupRmonBitsCntTable_Object((1,3,6,1,4,1,20044,12,9,2,80))
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntTable.setStatus(_A)
_Pm1001pcMonupRmonBitsCntEntry_Object=MibTableRow
pm1001pcMonupRmonBitsCntEntry=_Pm1001pcMonupRmonBitsCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,80,1))
pm1001pcMonupRmonBitsCntEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntEntry.setStatus(_A)
class _Pm1001pcMonupRmonBitsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonBitsCntIndex_Type.__name__=_E
_Pm1001pcMonupRmonBitsCntIndex_Object=MibTableColumn
pm1001pcMonupRmonBitsCntIndex=_Pm1001pcMonupRmonBitsCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,80,1,1),_Pm1001pcMonupRmonBitsCntIndex_Type())
pm1001pcMonupRmonBitsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntIndex.setStatus(_A)
_Pm1001pcMonupRmonBitsCntValuePortn_Type=Counter64
_Pm1001pcMonupRmonBitsCntValuePortn_Object=MibTableColumn
pm1001pcMonupRmonBitsCntValuePortn=_Pm1001pcMonupRmonBitsCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,80,1,2),_Pm1001pcMonupRmonBitsCntValuePortn_Type())
pm1001pcMonupRmonBitsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntValuePortn.setStatus(_A)
_Pm1001pcMonupRmonBitsCntErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBitsCntErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonBitsCntErrorPortn=_Pm1001pcMonupRmonBitsCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,80,1,3),_Pm1001pcMonupRmonBitsCntErrorPortn_Type())
pm1001pcMonupRmonBitsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonBitsCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBitsCntOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonBitsCntOverloadPortn=_Pm1001pcMonupRmonBitsCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,80,1,4),_Pm1001pcMonupRmonBitsCntOverloadPortn_Type())
pm1001pcMonupRmonBitsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonByteCntTable_Object=MibTable
pm1001pcMondwRmonByteCntTable=_Pm1001pcMondwRmonByteCntTable_Object((1,3,6,1,4,1,20044,12,9,2,112))
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntTable.setStatus(_A)
_Pm1001pcMondwRmonByteCntEntry_Object=MibTableRow
pm1001pcMondwRmonByteCntEntry=_Pm1001pcMondwRmonByteCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,112,1))
pm1001pcMondwRmonByteCntEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonByteCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonByteCntIndex_Object=MibTableColumn
pm1001pcMondwRmonByteCntIndex=_Pm1001pcMondwRmonByteCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,112,1,1),_Pm1001pcMondwRmonByteCntIndex_Type())
pm1001pcMondwRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntIndex.setStatus(_A)
_Pm1001pcMondwRmonByteCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonByteCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonByteCntValuePortn=_Pm1001pcMondwRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,112,1,2),_Pm1001pcMondwRmonByteCntValuePortn_Type())
pm1001pcMondwRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonByteCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonByteCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonByteCntErrorPortn=_Pm1001pcMondwRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,112,1,3),_Pm1001pcMondwRmonByteCntErrorPortn_Type())
pm1001pcMondwRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonByteCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonByteCntOverloadPortn=_Pm1001pcMondwRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,112,1,4),_Pm1001pcMondwRmonByteCntOverloadPortn_Type())
pm1001pcMondwRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntTable_Object=MibTable
pm1001pcMondwRmonCrcErrorCntTable=_Pm1001pcMondwRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,12,9,2,120))
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntTable.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntEntry_Object=MibTableRow
pm1001pcMondwRmonCrcErrorCntEntry=_Pm1001pcMondwRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,120,1))
pm1001pcMondwRmonCrcErrorCntEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonCrcErrorCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonCrcErrorCntIndex_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntIndex=_Pm1001pcMondwRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,120,1,1),_Pm1001pcMondwRmonCrcErrorCntIndex_Type())
pm1001pcMondwRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntIndex.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntValuePortn=_Pm1001pcMondwRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,120,1,2),_Pm1001pcMondwRmonCrcErrorCntValuePortn_Type())
pm1001pcMondwRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntErrorPortn=_Pm1001pcMondwRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,120,1,3),_Pm1001pcMondwRmonCrcErrorCntErrorPortn_Type())
pm1001pcMondwRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntOverloadPortn=_Pm1001pcMondwRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,120,1,4),_Pm1001pcMondwRmonCrcErrorCntOverloadPortn_Type())
pm1001pcMondwRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntTable_Object=MibTable
pm1001pcMondwRmonPacketsCntTable=_Pm1001pcMondwRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,12,9,2,128))
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntTable.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntEntry_Object=MibTableRow
pm1001pcMondwRmonPacketsCntEntry=_Pm1001pcMondwRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,128,1))
pm1001pcMondwRmonPacketsCntEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonPacketsCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonPacketsCntIndex_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntIndex=_Pm1001pcMondwRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,128,1,1),_Pm1001pcMondwRmonPacketsCntIndex_Type())
pm1001pcMondwRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntIndex.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonPacketsCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntValuePortn=_Pm1001pcMondwRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,128,1,2),_Pm1001pcMondwRmonPacketsCntValuePortn_Type())
pm1001pcMondwRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPacketsCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntErrorPortn=_Pm1001pcMondwRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,128,1,3),_Pm1001pcMondwRmonPacketsCntErrorPortn_Type())
pm1001pcMondwRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntOverloadPortn=_Pm1001pcMondwRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,128,1,4),_Pm1001pcMondwRmonPacketsCntOverloadPortn_Type())
pm1001pcMondwRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntTable_Object=MibTable
pm1001pcMondwRmonBroadcastCntTable=_Pm1001pcMondwRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,12,9,2,136))
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntTable.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntEntry_Object=MibTableRow
pm1001pcMondwRmonBroadcastCntEntry=_Pm1001pcMondwRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,136,1))
pm1001pcMondwRmonBroadcastCntEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonBroadcastCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonBroadcastCntIndex_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntIndex=_Pm1001pcMondwRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,136,1,1),_Pm1001pcMondwRmonBroadcastCntIndex_Type())
pm1001pcMondwRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntIndex.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonBroadcastCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntValuePortn=_Pm1001pcMondwRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,136,1,2),_Pm1001pcMondwRmonBroadcastCntValuePortn_Type())
pm1001pcMondwRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntErrorPortn=_Pm1001pcMondwRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,136,1,3),_Pm1001pcMondwRmonBroadcastCntErrorPortn_Type())
pm1001pcMondwRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntOverloadPortn=_Pm1001pcMondwRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,136,1,4),_Pm1001pcMondwRmonBroadcastCntOverloadPortn_Type())
pm1001pcMondwRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntTable_Object=MibTable
pm1001pcMondwRmonMulticastCntTable=_Pm1001pcMondwRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,12,9,2,144))
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntTable.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntEntry_Object=MibTableRow
pm1001pcMondwRmonMulticastCntEntry=_Pm1001pcMondwRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,144,1))
pm1001pcMondwRmonMulticastCntEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonMulticastCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonMulticastCntIndex_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntIndex=_Pm1001pcMondwRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,144,1,1),_Pm1001pcMondwRmonMulticastCntIndex_Type())
pm1001pcMondwRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntIndex.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonMulticastCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntValuePortn=_Pm1001pcMondwRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,144,1,2),_Pm1001pcMondwRmonMulticastCntValuePortn_Type())
pm1001pcMondwRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonMulticastCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntErrorPortn=_Pm1001pcMondwRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,144,1,3),_Pm1001pcMondwRmonMulticastCntErrorPortn_Type())
pm1001pcMondwRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntOverloadPortn=_Pm1001pcMondwRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,144,1,4),_Pm1001pcMondwRmonMulticastCntOverloadPortn_Type())
pm1001pcMondwRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntTable_Object=MibTable
pm1001pcMondwRmonPauseFrameCntTable=_Pm1001pcMondwRmonPauseFrameCntTable_Object((1,3,6,1,4,1,20044,12,9,2,152))
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntTable.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntEntry_Object=MibTableRow
pm1001pcMondwRmonPauseFrameCntEntry=_Pm1001pcMondwRmonPauseFrameCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,152,1))
pm1001pcMondwRmonPauseFrameCntEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonPauseFrameCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonPauseFrameCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonPauseFrameCntIndex_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntIndex=_Pm1001pcMondwRmonPauseFrameCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,152,1,1),_Pm1001pcMondwRmonPauseFrameCntIndex_Type())
pm1001pcMondwRmonPauseFrameCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntIndex.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonPauseFrameCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntValuePortn=_Pm1001pcMondwRmonPauseFrameCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,152,1,2),_Pm1001pcMondwRmonPauseFrameCntValuePortn_Type())
pm1001pcMondwRmonPauseFrameCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPauseFrameCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntErrorPortn=_Pm1001pcMondwRmonPauseFrameCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,152,1,3),_Pm1001pcMondwRmonPauseFrameCntErrorPortn_Type())
pm1001pcMondwRmonPauseFrameCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPauseFrameCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntOverloadPortn=_Pm1001pcMondwRmonPauseFrameCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,152,1,4),_Pm1001pcMondwRmonPauseFrameCntOverloadPortn_Type())
pm1001pcMondwRmonPauseFrameCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonTimerCntTable_Object=MibTable
pm1001pcMondwRmonTimerCntTable=_Pm1001pcMondwRmonTimerCntTable_Object((1,3,6,1,4,1,20044,12,9,2,160))
if mibBuilder.loadTexts:pm1001pcMondwRmonTimerCntTable.setStatus(_A)
_Pm1001pcMondwRmonTimerCntEntry_Object=MibTableRow
pm1001pcMondwRmonTimerCntEntry=_Pm1001pcMondwRmonTimerCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,160,1))
pm1001pcMondwRmonTimerCntEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm1001pcMondwRmonTimerCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonTimerCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonTimerCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonTimerCntIndex_Object=MibTableColumn
pm1001pcMondwRmonTimerCntIndex=_Pm1001pcMondwRmonTimerCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,160,1,1),_Pm1001pcMondwRmonTimerCntIndex_Type())
pm1001pcMondwRmonTimerCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonTimerCntIndex.setStatus(_A)
_Pm1001pcMondwRmonTimerCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonTimerCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonTimerCntValuePortn=_Pm1001pcMondwRmonTimerCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,160,1,2),_Pm1001pcMondwRmonTimerCntValuePortn_Type())
pm1001pcMondwRmonTimerCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonTimerCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonTimerCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonTimerCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonTimerCntErrorPortn=_Pm1001pcMondwRmonTimerCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,160,1,3),_Pm1001pcMondwRmonTimerCntErrorPortn_Type())
pm1001pcMondwRmonTimerCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonTimerCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonTimerCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonTimerCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonTimerCntOverloadPortn=_Pm1001pcMondwRmonTimerCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,160,1,4),_Pm1001pcMondwRmonTimerCntOverloadPortn_Type())
pm1001pcMondwRmonTimerCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonTimerCntOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonBitsCntTable_Object=MibTable
pm1001pcMondwRmonBitsCntTable=_Pm1001pcMondwRmonBitsCntTable_Object((1,3,6,1,4,1,20044,12,9,2,168))
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntTable.setStatus(_A)
_Pm1001pcMondwRmonBitsCntEntry_Object=MibTableRow
pm1001pcMondwRmonBitsCntEntry=_Pm1001pcMondwRmonBitsCntEntry_Object((1,3,6,1,4,1,20044,12,9,2,168,1))
pm1001pcMondwRmonBitsCntEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntEntry.setStatus(_A)
class _Pm1001pcMondwRmonBitsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonBitsCntIndex_Type.__name__=_E
_Pm1001pcMondwRmonBitsCntIndex_Object=MibTableColumn
pm1001pcMondwRmonBitsCntIndex=_Pm1001pcMondwRmonBitsCntIndex_Object((1,3,6,1,4,1,20044,12,9,2,168,1,1),_Pm1001pcMondwRmonBitsCntIndex_Type())
pm1001pcMondwRmonBitsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntIndex.setStatus(_A)
_Pm1001pcMondwRmonBitsCntValuePortn_Type=Counter64
_Pm1001pcMondwRmonBitsCntValuePortn_Object=MibTableColumn
pm1001pcMondwRmonBitsCntValuePortn=_Pm1001pcMondwRmonBitsCntValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,168,1,2),_Pm1001pcMondwRmonBitsCntValuePortn_Type())
pm1001pcMondwRmonBitsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntValuePortn.setStatus(_A)
_Pm1001pcMondwRmonBitsCntErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBitsCntErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonBitsCntErrorPortn=_Pm1001pcMondwRmonBitsCntErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,168,1,3),_Pm1001pcMondwRmonBitsCntErrorPortn_Type())
pm1001pcMondwRmonBitsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonBitsCntOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBitsCntOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonBitsCntOverloadPortn=_Pm1001pcMondwRmonBitsCntOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,168,1,4),_Pm1001pcMondwRmonBitsCntOverloadPortn_Type())
pm1001pcMondwRmonBitsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonByteCntSTable_Object=MibTable
pm1001pcMonupRmonByteCntSTable=_Pm1001pcMonupRmonByteCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1024))
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntSTable.setStatus(_A)
_Pm1001pcMonupRmonByteCntSEntry_Object=MibTableRow
pm1001pcMonupRmonByteCntSEntry=_Pm1001pcMonupRmonByteCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1024,1))
pm1001pcMonupRmonByteCntSEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonByteCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonByteCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonByteCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonByteCntSIndex=_Pm1001pcMonupRmonByteCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1024,1,1),_Pm1001pcMonupRmonByteCntSIndex_Type())
pm1001pcMonupRmonByteCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonByteCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonByteCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonByteCntSValuePortn=_Pm1001pcMonupRmonByteCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1024,1,2),_Pm1001pcMonupRmonByteCntSValuePortn_Type())
pm1001pcMonupRmonByteCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonByteCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonByteCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonByteCntSErrorPortn=_Pm1001pcMonupRmonByteCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1024,1,3),_Pm1001pcMonupRmonByteCntSErrorPortn_Type())
pm1001pcMonupRmonByteCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonByteCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonByteCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonByteCntSOverloadPortn=_Pm1001pcMonupRmonByteCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1024,1,4),_Pm1001pcMonupRmonByteCntSOverloadPortn_Type())
pm1001pcMonupRmonByteCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonByteCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntSTable_Object=MibTable
pm1001pcMonupRmonCrcErrorCntSTable=_Pm1001pcMonupRmonCrcErrorCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1032))
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntSTable.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntSEntry_Object=MibTableRow
pm1001pcMonupRmonCrcErrorCntSEntry=_Pm1001pcMonupRmonCrcErrorCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1032,1))
pm1001pcMonupRmonCrcErrorCntSEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonCrcErrorCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonCrcErrorCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonCrcErrorCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntSIndex=_Pm1001pcMonupRmonCrcErrorCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1032,1,1),_Pm1001pcMonupRmonCrcErrorCntSIndex_Type())
pm1001pcMonupRmonCrcErrorCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonCrcErrorCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntSValuePortn=_Pm1001pcMonupRmonCrcErrorCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1032,1,2),_Pm1001pcMonupRmonCrcErrorCntSValuePortn_Type())
pm1001pcMonupRmonCrcErrorCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonCrcErrorCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntSErrorPortn=_Pm1001pcMonupRmonCrcErrorCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1032,1,3),_Pm1001pcMonupRmonCrcErrorCntSErrorPortn_Type())
pm1001pcMonupRmonCrcErrorCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonCrcErrorCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonCrcErrorCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonCrcErrorCntSOverloadPortn=_Pm1001pcMonupRmonCrcErrorCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1032,1,4),_Pm1001pcMonupRmonCrcErrorCntSOverloadPortn_Type())
pm1001pcMonupRmonCrcErrorCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonCrcErrorCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntSTable_Object=MibTable
pm1001pcMonupRmonPacketsCntSTable=_Pm1001pcMonupRmonPacketsCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1040))
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntSTable.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntSEntry_Object=MibTableRow
pm1001pcMonupRmonPacketsCntSEntry=_Pm1001pcMonupRmonPacketsCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1040,1))
pm1001pcMonupRmonPacketsCntSEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonPacketsCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonPacketsCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonPacketsCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntSIndex=_Pm1001pcMonupRmonPacketsCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1040,1,1),_Pm1001pcMonupRmonPacketsCntSIndex_Type())
pm1001pcMonupRmonPacketsCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonPacketsCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntSValuePortn=_Pm1001pcMonupRmonPacketsCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1040,1,2),_Pm1001pcMonupRmonPacketsCntSValuePortn_Type())
pm1001pcMonupRmonPacketsCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPacketsCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntSErrorPortn=_Pm1001pcMonupRmonPacketsCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1040,1,3),_Pm1001pcMonupRmonPacketsCntSErrorPortn_Type())
pm1001pcMonupRmonPacketsCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonPacketsCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPacketsCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonPacketsCntSOverloadPortn=_Pm1001pcMonupRmonPacketsCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1040,1,4),_Pm1001pcMonupRmonPacketsCntSOverloadPortn_Type())
pm1001pcMonupRmonPacketsCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPacketsCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntSTable_Object=MibTable
pm1001pcMonupRmonBroadcastCntSTable=_Pm1001pcMonupRmonBroadcastCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1048))
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntSTable.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntSEntry_Object=MibTableRow
pm1001pcMonupRmonBroadcastCntSEntry=_Pm1001pcMonupRmonBroadcastCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1048,1))
pm1001pcMonupRmonBroadcastCntSEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonBroadcastCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonBroadcastCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonBroadcastCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntSIndex=_Pm1001pcMonupRmonBroadcastCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1048,1,1),_Pm1001pcMonupRmonBroadcastCntSIndex_Type())
pm1001pcMonupRmonBroadcastCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonBroadcastCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntSValuePortn=_Pm1001pcMonupRmonBroadcastCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1048,1,2),_Pm1001pcMonupRmonBroadcastCntSValuePortn_Type())
pm1001pcMonupRmonBroadcastCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBroadcastCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntSErrorPortn=_Pm1001pcMonupRmonBroadcastCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1048,1,3),_Pm1001pcMonupRmonBroadcastCntSErrorPortn_Type())
pm1001pcMonupRmonBroadcastCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonBroadcastCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBroadcastCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonBroadcastCntSOverloadPortn=_Pm1001pcMonupRmonBroadcastCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1048,1,4),_Pm1001pcMonupRmonBroadcastCntSOverloadPortn_Type())
pm1001pcMonupRmonBroadcastCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBroadcastCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntSTable_Object=MibTable
pm1001pcMonupRmonMulticastCntSTable=_Pm1001pcMonupRmonMulticastCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1056))
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntSTable.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntSEntry_Object=MibTableRow
pm1001pcMonupRmonMulticastCntSEntry=_Pm1001pcMonupRmonMulticastCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1056,1))
pm1001pcMonupRmonMulticastCntSEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonMulticastCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonMulticastCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonMulticastCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntSIndex=_Pm1001pcMonupRmonMulticastCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1056,1,1),_Pm1001pcMonupRmonMulticastCntSIndex_Type())
pm1001pcMonupRmonMulticastCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonMulticastCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntSValuePortn=_Pm1001pcMonupRmonMulticastCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1056,1,2),_Pm1001pcMonupRmonMulticastCntSValuePortn_Type())
pm1001pcMonupRmonMulticastCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonMulticastCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntSErrorPortn=_Pm1001pcMonupRmonMulticastCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1056,1,3),_Pm1001pcMonupRmonMulticastCntSErrorPortn_Type())
pm1001pcMonupRmonMulticastCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonMulticastCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonMulticastCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonMulticastCntSOverloadPortn=_Pm1001pcMonupRmonMulticastCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1056,1,4),_Pm1001pcMonupRmonMulticastCntSOverloadPortn_Type())
pm1001pcMonupRmonMulticastCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonMulticastCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntSTable_Object=MibTable
pm1001pcMonupRmonPauseFrameCntSTable=_Pm1001pcMonupRmonPauseFrameCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1072))
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntSTable.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntSEntry_Object=MibTableRow
pm1001pcMonupRmonPauseFrameCntSEntry=_Pm1001pcMonupRmonPauseFrameCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1072,1))
pm1001pcMonupRmonPauseFrameCntSEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonPauseFrameCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonPauseFrameCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonPauseFrameCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntSIndex=_Pm1001pcMonupRmonPauseFrameCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1072,1,1),_Pm1001pcMonupRmonPauseFrameCntSIndex_Type())
pm1001pcMonupRmonPauseFrameCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonPauseFrameCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntSValuePortn=_Pm1001pcMonupRmonPauseFrameCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1072,1,2),_Pm1001pcMonupRmonPauseFrameCntSValuePortn_Type())
pm1001pcMonupRmonPauseFrameCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPauseFrameCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntSErrorPortn=_Pm1001pcMonupRmonPauseFrameCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1072,1,3),_Pm1001pcMonupRmonPauseFrameCntSErrorPortn_Type())
pm1001pcMonupRmonPauseFrameCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonPauseFrameCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonPauseFrameCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonPauseFrameCntSOverloadPortn=_Pm1001pcMonupRmonPauseFrameCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1072,1,4),_Pm1001pcMonupRmonPauseFrameCntSOverloadPortn_Type())
pm1001pcMonupRmonPauseFrameCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonPauseFrameCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntSTable_Object=MibTable
pm1001pcMonupRmonDropFrameCntSTable=_Pm1001pcMonupRmonDropFrameCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1080))
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntSTable.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntSEntry_Object=MibTableRow
pm1001pcMonupRmonDropFrameCntSEntry=_Pm1001pcMonupRmonDropFrameCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1080,1))
pm1001pcMonupRmonDropFrameCntSEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonDropFrameCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonDropFrameCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonDropFrameCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntSIndex=_Pm1001pcMonupRmonDropFrameCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1080,1,1),_Pm1001pcMonupRmonDropFrameCntSIndex_Type())
pm1001pcMonupRmonDropFrameCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonDropFrameCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntSValuePortn=_Pm1001pcMonupRmonDropFrameCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1080,1,2),_Pm1001pcMonupRmonDropFrameCntSValuePortn_Type())
pm1001pcMonupRmonDropFrameCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonDropFrameCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntSErrorPortn=_Pm1001pcMonupRmonDropFrameCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1080,1,3),_Pm1001pcMonupRmonDropFrameCntSErrorPortn_Type())
pm1001pcMonupRmonDropFrameCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonDropFrameCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonDropFrameCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonDropFrameCntSOverloadPortn=_Pm1001pcMonupRmonDropFrameCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1080,1,4),_Pm1001pcMonupRmonDropFrameCntSOverloadPortn_Type())
pm1001pcMonupRmonDropFrameCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonDropFrameCntSOverloadPortn.setStatus(_A)
_Pm1001pcMonupRmonBitsCntSTable_Object=MibTable
pm1001pcMonupRmonBitsCntSTable=_Pm1001pcMonupRmonBitsCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1088))
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntSTable.setStatus(_A)
_Pm1001pcMonupRmonBitsCntSEntry_Object=MibTableRow
pm1001pcMonupRmonBitsCntSEntry=_Pm1001pcMonupRmonBitsCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1088,1))
pm1001pcMonupRmonBitsCntSEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntSEntry.setStatus(_A)
class _Pm1001pcMonupRmonBitsCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMonupRmonBitsCntSIndex_Type.__name__=_E
_Pm1001pcMonupRmonBitsCntSIndex_Object=MibTableColumn
pm1001pcMonupRmonBitsCntSIndex=_Pm1001pcMonupRmonBitsCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1088,1,1),_Pm1001pcMonupRmonBitsCntSIndex_Type())
pm1001pcMonupRmonBitsCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntSIndex.setStatus(_A)
_Pm1001pcMonupRmonBitsCntSValuePortn_Type=Counter64
_Pm1001pcMonupRmonBitsCntSValuePortn_Object=MibTableColumn
pm1001pcMonupRmonBitsCntSValuePortn=_Pm1001pcMonupRmonBitsCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1088,1,2),_Pm1001pcMonupRmonBitsCntSValuePortn_Type())
pm1001pcMonupRmonBitsCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntSValuePortn.setStatus(_A)
_Pm1001pcMonupRmonBitsCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBitsCntSErrorPortn_Object=MibTableColumn
pm1001pcMonupRmonBitsCntSErrorPortn=_Pm1001pcMonupRmonBitsCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1088,1,3),_Pm1001pcMonupRmonBitsCntSErrorPortn_Type())
pm1001pcMonupRmonBitsCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntSErrorPortn.setStatus(_A)
_Pm1001pcMonupRmonBitsCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMonupRmonBitsCntSOverloadPortn_Object=MibTableColumn
pm1001pcMonupRmonBitsCntSOverloadPortn=_Pm1001pcMonupRmonBitsCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1088,1,4),_Pm1001pcMonupRmonBitsCntSOverloadPortn_Type())
pm1001pcMonupRmonBitsCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMonupRmonBitsCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonByteCntSTable_Object=MibTable
pm1001pcMondwRmonByteCntSTable=_Pm1001pcMondwRmonByteCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1120))
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntSTable.setStatus(_A)
_Pm1001pcMondwRmonByteCntSEntry_Object=MibTableRow
pm1001pcMondwRmonByteCntSEntry=_Pm1001pcMondwRmonByteCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1120,1))
pm1001pcMondwRmonByteCntSEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonByteCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonByteCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonByteCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonByteCntSIndex=_Pm1001pcMondwRmonByteCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1120,1,1),_Pm1001pcMondwRmonByteCntSIndex_Type())
pm1001pcMondwRmonByteCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonByteCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonByteCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonByteCntSValuePortn=_Pm1001pcMondwRmonByteCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1120,1,2),_Pm1001pcMondwRmonByteCntSValuePortn_Type())
pm1001pcMondwRmonByteCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonByteCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonByteCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonByteCntSErrorPortn=_Pm1001pcMondwRmonByteCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1120,1,3),_Pm1001pcMondwRmonByteCntSErrorPortn_Type())
pm1001pcMondwRmonByteCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonByteCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonByteCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonByteCntSOverloadPortn=_Pm1001pcMondwRmonByteCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1120,1,4),_Pm1001pcMondwRmonByteCntSOverloadPortn_Type())
pm1001pcMondwRmonByteCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonByteCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntSTable_Object=MibTable
pm1001pcMondwRmonCrcErrorCntSTable=_Pm1001pcMondwRmonCrcErrorCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1128))
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntSTable.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntSEntry_Object=MibTableRow
pm1001pcMondwRmonCrcErrorCntSEntry=_Pm1001pcMondwRmonCrcErrorCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1128,1))
pm1001pcMondwRmonCrcErrorCntSEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonCrcErrorCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonCrcErrorCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonCrcErrorCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntSIndex=_Pm1001pcMondwRmonCrcErrorCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1128,1,1),_Pm1001pcMondwRmonCrcErrorCntSIndex_Type())
pm1001pcMondwRmonCrcErrorCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonCrcErrorCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntSValuePortn=_Pm1001pcMondwRmonCrcErrorCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1128,1,2),_Pm1001pcMondwRmonCrcErrorCntSValuePortn_Type())
pm1001pcMondwRmonCrcErrorCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonCrcErrorCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntSErrorPortn=_Pm1001pcMondwRmonCrcErrorCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1128,1,3),_Pm1001pcMondwRmonCrcErrorCntSErrorPortn_Type())
pm1001pcMondwRmonCrcErrorCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonCrcErrorCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonCrcErrorCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonCrcErrorCntSOverloadPortn=_Pm1001pcMondwRmonCrcErrorCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1128,1,4),_Pm1001pcMondwRmonCrcErrorCntSOverloadPortn_Type())
pm1001pcMondwRmonCrcErrorCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonCrcErrorCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntSTable_Object=MibTable
pm1001pcMondwRmonPacketsCntSTable=_Pm1001pcMondwRmonPacketsCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1136))
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntSTable.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntSEntry_Object=MibTableRow
pm1001pcMondwRmonPacketsCntSEntry=_Pm1001pcMondwRmonPacketsCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1136,1))
pm1001pcMondwRmonPacketsCntSEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonPacketsCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonPacketsCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonPacketsCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntSIndex=_Pm1001pcMondwRmonPacketsCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1136,1,1),_Pm1001pcMondwRmonPacketsCntSIndex_Type())
pm1001pcMondwRmonPacketsCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonPacketsCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntSValuePortn=_Pm1001pcMondwRmonPacketsCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1136,1,2),_Pm1001pcMondwRmonPacketsCntSValuePortn_Type())
pm1001pcMondwRmonPacketsCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPacketsCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntSErrorPortn=_Pm1001pcMondwRmonPacketsCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1136,1,3),_Pm1001pcMondwRmonPacketsCntSErrorPortn_Type())
pm1001pcMondwRmonPacketsCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonPacketsCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPacketsCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonPacketsCntSOverloadPortn=_Pm1001pcMondwRmonPacketsCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1136,1,4),_Pm1001pcMondwRmonPacketsCntSOverloadPortn_Type())
pm1001pcMondwRmonPacketsCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPacketsCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntSTable_Object=MibTable
pm1001pcMondwRmonBroadcastCntSTable=_Pm1001pcMondwRmonBroadcastCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1144))
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntSTable.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntSEntry_Object=MibTableRow
pm1001pcMondwRmonBroadcastCntSEntry=_Pm1001pcMondwRmonBroadcastCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1144,1))
pm1001pcMondwRmonBroadcastCntSEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonBroadcastCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonBroadcastCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonBroadcastCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntSIndex=_Pm1001pcMondwRmonBroadcastCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1144,1,1),_Pm1001pcMondwRmonBroadcastCntSIndex_Type())
pm1001pcMondwRmonBroadcastCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonBroadcastCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntSValuePortn=_Pm1001pcMondwRmonBroadcastCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1144,1,2),_Pm1001pcMondwRmonBroadcastCntSValuePortn_Type())
pm1001pcMondwRmonBroadcastCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBroadcastCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntSErrorPortn=_Pm1001pcMondwRmonBroadcastCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1144,1,3),_Pm1001pcMondwRmonBroadcastCntSErrorPortn_Type())
pm1001pcMondwRmonBroadcastCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonBroadcastCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBroadcastCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonBroadcastCntSOverloadPortn=_Pm1001pcMondwRmonBroadcastCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1144,1,4),_Pm1001pcMondwRmonBroadcastCntSOverloadPortn_Type())
pm1001pcMondwRmonBroadcastCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBroadcastCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntSTable_Object=MibTable
pm1001pcMondwRmonMulticastCntSTable=_Pm1001pcMondwRmonMulticastCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1152))
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntSTable.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntSEntry_Object=MibTableRow
pm1001pcMondwRmonMulticastCntSEntry=_Pm1001pcMondwRmonMulticastCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1152,1))
pm1001pcMondwRmonMulticastCntSEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonMulticastCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonMulticastCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonMulticastCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntSIndex=_Pm1001pcMondwRmonMulticastCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1152,1,1),_Pm1001pcMondwRmonMulticastCntSIndex_Type())
pm1001pcMondwRmonMulticastCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonMulticastCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntSValuePortn=_Pm1001pcMondwRmonMulticastCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1152,1,2),_Pm1001pcMondwRmonMulticastCntSValuePortn_Type())
pm1001pcMondwRmonMulticastCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonMulticastCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntSErrorPortn=_Pm1001pcMondwRmonMulticastCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1152,1,3),_Pm1001pcMondwRmonMulticastCntSErrorPortn_Type())
pm1001pcMondwRmonMulticastCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonMulticastCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonMulticastCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonMulticastCntSOverloadPortn=_Pm1001pcMondwRmonMulticastCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1152,1,4),_Pm1001pcMondwRmonMulticastCntSOverloadPortn_Type())
pm1001pcMondwRmonMulticastCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonMulticastCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntSTable_Object=MibTable
pm1001pcMondwRmonPauseFrameCntSTable=_Pm1001pcMondwRmonPauseFrameCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1160))
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntSTable.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntSEntry_Object=MibTableRow
pm1001pcMondwRmonPauseFrameCntSEntry=_Pm1001pcMondwRmonPauseFrameCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1160,1))
pm1001pcMondwRmonPauseFrameCntSEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonPauseFrameCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonPauseFrameCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonPauseFrameCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntSIndex=_Pm1001pcMondwRmonPauseFrameCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1160,1,1),_Pm1001pcMondwRmonPauseFrameCntSIndex_Type())
pm1001pcMondwRmonPauseFrameCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonPauseFrameCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntSValuePortn=_Pm1001pcMondwRmonPauseFrameCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1160,1,2),_Pm1001pcMondwRmonPauseFrameCntSValuePortn_Type())
pm1001pcMondwRmonPauseFrameCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPauseFrameCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntSErrorPortn=_Pm1001pcMondwRmonPauseFrameCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1160,1,3),_Pm1001pcMondwRmonPauseFrameCntSErrorPortn_Type())
pm1001pcMondwRmonPauseFrameCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonPauseFrameCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonPauseFrameCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonPauseFrameCntSOverloadPortn=_Pm1001pcMondwRmonPauseFrameCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1160,1,4),_Pm1001pcMondwRmonPauseFrameCntSOverloadPortn_Type())
pm1001pcMondwRmonPauseFrameCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonPauseFrameCntSOverloadPortn.setStatus(_A)
_Pm1001pcMondwRmonBitsCntSTable_Object=MibTable
pm1001pcMondwRmonBitsCntSTable=_Pm1001pcMondwRmonBitsCntSTable_Object((1,3,6,1,4,1,20044,12,9,2,1176))
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntSTable.setStatus(_A)
_Pm1001pcMondwRmonBitsCntSEntry_Object=MibTableRow
pm1001pcMondwRmonBitsCntSEntry=_Pm1001pcMondwRmonBitsCntSEntry_Object((1,3,6,1,4,1,20044,12,9,2,1176,1))
pm1001pcMondwRmonBitsCntSEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntSEntry.setStatus(_A)
class _Pm1001pcMondwRmonBitsCntSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcMondwRmonBitsCntSIndex_Type.__name__=_E
_Pm1001pcMondwRmonBitsCntSIndex_Object=MibTableColumn
pm1001pcMondwRmonBitsCntSIndex=_Pm1001pcMondwRmonBitsCntSIndex_Object((1,3,6,1,4,1,20044,12,9,2,1176,1,1),_Pm1001pcMondwRmonBitsCntSIndex_Type())
pm1001pcMondwRmonBitsCntSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntSIndex.setStatus(_A)
_Pm1001pcMondwRmonBitsCntSValuePortn_Type=Counter64
_Pm1001pcMondwRmonBitsCntSValuePortn_Object=MibTableColumn
pm1001pcMondwRmonBitsCntSValuePortn=_Pm1001pcMondwRmonBitsCntSValuePortn_Object((1,3,6,1,4,1,20044,12,9,2,1176,1,2),_Pm1001pcMondwRmonBitsCntSValuePortn_Type())
pm1001pcMondwRmonBitsCntSValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntSValuePortn.setStatus(_A)
_Pm1001pcMondwRmonBitsCntSErrorPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBitsCntSErrorPortn_Object=MibTableColumn
pm1001pcMondwRmonBitsCntSErrorPortn=_Pm1001pcMondwRmonBitsCntSErrorPortn_Object((1,3,6,1,4,1,20044,12,9,2,1176,1,3),_Pm1001pcMondwRmonBitsCntSErrorPortn_Type())
pm1001pcMondwRmonBitsCntSErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntSErrorPortn.setStatus(_A)
_Pm1001pcMondwRmonBitsCntSOverloadPortn_Type=EkiOnOff
_Pm1001pcMondwRmonBitsCntSOverloadPortn_Object=MibTableColumn
pm1001pcMondwRmonBitsCntSOverloadPortn=_Pm1001pcMondwRmonBitsCntSOverloadPortn_Object((1,3,6,1,4,1,20044,12,9,2,1176,1,4),_Pm1001pcMondwRmonBitsCntSOverloadPortn_Type())
pm1001pcMondwRmonBitsCntSOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcMondwRmonBitsCntSOverloadPortn.setStatus(_A)
_Pm1001pcRmonLine_ObjectIdentity=ObjectIdentity
pm1001pcRmonLine=_Pm1001pcRmonLine_ObjectIdentity((1,3,6,1,4,1,20044,12,9,3))
_Pm1001pcConfig_ObjectIdentity=ObjectIdentity
pm1001pcConfig=_Pm1001pcConfig_ObjectIdentity((1,3,6,1,4,1,20044,12,10))
_Pm1001pcCfgAccessCAisCsf_ObjectIdentity=ObjectIdentity
pm1001pcCfgAccessCAisCsf=_Pm1001pcCfgAccessCAisCsf_ObjectIdentity((1,3,6,1,4,1,20044,12,10,1))
_Pm1001pcCfgClientcaiscsfTable_Object=MibTable
pm1001pcCfgClientcaiscsfTable=_Pm1001pcCfgClientcaiscsfTable_Object((1,3,6,1,4,1,20044,12,10,1,1))
if mibBuilder.loadTexts:pm1001pcCfgClientcaiscsfTable.setStatus(_A)
_Pm1001pcCfgClientcaiscsfEntry_Object=MibTableRow
pm1001pcCfgClientcaiscsfEntry=_Pm1001pcCfgClientcaiscsfEntry_Object((1,3,6,1,4,1,20044,12,10,1,1,1))
pm1001pcCfgClientcaiscsfEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pm1001pcCfgClientcaiscsfEntry.setStatus(_A)
class _Pm1001pcCfgClientcaiscsfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCfgClientcaiscsfIndex_Type.__name__=_E
_Pm1001pcCfgClientcaiscsfIndex_Object=MibTableColumn
pm1001pcCfgClientcaiscsfIndex=_Pm1001pcCfgClientcaiscsfIndex_Object((1,3,6,1,4,1,20044,12,10,1,1,1,1),_Pm1001pcCfgClientcaiscsfIndex_Type())
pm1001pcCfgClientcaiscsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCfgClientcaiscsfIndex.setStatus(_A)
class _Pm1001pcCfgCAisModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgCAisModePortn_Type.__name__=_F
_Pm1001pcCfgCAisModePortn_Object=MibTableColumn
pm1001pcCfgCAisModePortn=_Pm1001pcCfgCAisModePortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,3),_Pm1001pcCfgCAisModePortn_Type())
pm1001pcCfgCAisModePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgCAisModePortn.setStatus(_A)
class _Pm1001pcCfgUpAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgUpAccessioAlmPortn_Type.__name__=_F
_Pm1001pcCfgUpAccessioAlmPortn_Object=MibTableColumn
pm1001pcCfgUpAccessioAlmPortn=_Pm1001pcCfgUpAccessioAlmPortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,9),_Pm1001pcCfgUpAccessioAlmPortn_Type())
pm1001pcCfgUpAccessioAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgUpAccessioAlmPortn.setStatus(_A)
class _Pm1001pcCfgUpMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgUpMapperDeAlmPortn_Type.__name__=_F
_Pm1001pcCfgUpMapperDeAlmPortn_Object=MibTableColumn
pm1001pcCfgUpMapperDeAlmPortn=_Pm1001pcCfgUpMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,10),_Pm1001pcCfgUpMapperDeAlmPortn_Type())
pm1001pcCfgUpMapperDeAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgUpMapperDeAlmPortn.setStatus(_A)
class _Pm1001pcCfgDownAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgDownAccessioAlmPortn_Type.__name__=_F
_Pm1001pcCfgDownAccessioAlmPortn_Object=MibTableColumn
pm1001pcCfgDownAccessioAlmPortn=_Pm1001pcCfgDownAccessioAlmPortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,17),_Pm1001pcCfgDownAccessioAlmPortn_Type())
pm1001pcCfgDownAccessioAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgDownAccessioAlmPortn.setStatus(_A)
class _Pm1001pcCfgDownMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgDownMapperDeAlmPortn_Type.__name__=_F
_Pm1001pcCfgDownMapperDeAlmPortn_Object=MibTableColumn
pm1001pcCfgDownMapperDeAlmPortn=_Pm1001pcCfgDownMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,18),_Pm1001pcCfgDownMapperDeAlmPortn_Type())
pm1001pcCfgDownMapperDeAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgDownMapperDeAlmPortn.setStatus(_A)
class _Pm1001pcCfgDownDfrmAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgDownDfrmAlmPortn_Type.__name__=_F
_Pm1001pcCfgDownDfrmAlmPortn_Object=MibTableColumn
pm1001pcCfgDownDfrmAlmPortn=_Pm1001pcCfgDownDfrmAlmPortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,19),_Pm1001pcCfgDownDfrmAlmPortn_Type())
pm1001pcCfgDownDfrmAlmPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgDownDfrmAlmPortn.setStatus(_A)
class _Pm1001pcCfgDownLineSyncAlarmsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgDownLineSyncAlarmsPortn_Type.__name__=_F
_Pm1001pcCfgDownLineSyncAlarmsPortn_Object=MibTableColumn
pm1001pcCfgDownLineSyncAlarmsPortn=_Pm1001pcCfgDownLineSyncAlarmsPortn_Object((1,3,6,1,4,1,20044,12,10,1,1,1,20),_Pm1001pcCfgDownLineSyncAlarmsPortn_Type())
pm1001pcCfgDownLineSyncAlarmsPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgDownLineSyncAlarmsPortn.setStatus(_H)
_Pm1001pcCfgStartup_ObjectIdentity=ObjectIdentity
pm1001pcCfgStartup=_Pm1001pcCfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,12,10,2))
_Pm1001pcCfgClientStartupTable_Object=MibTable
pm1001pcCfgClientStartupTable=_Pm1001pcCfgClientStartupTable_Object((1,3,6,1,4,1,20044,12,10,2,1))
if mibBuilder.loadTexts:pm1001pcCfgClientStartupTable.setStatus(_A)
_Pm1001pcCfgClientStartupEntry_Object=MibTableRow
pm1001pcCfgClientStartupEntry=_Pm1001pcCfgClientStartupEntry_Object((1,3,6,1,4,1,20044,12,10,2,1,1))
pm1001pcCfgClientStartupEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pm1001pcCfgClientStartupEntry.setStatus(_A)
class _Pm1001pcCfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCfgClientStartupIndex_Type.__name__=_E
_Pm1001pcCfgClientStartupIndex_Object=MibTableColumn
pm1001pcCfgClientStartupIndex=_Pm1001pcCfgClientStartupIndex_Object((1,3,6,1,4,1,20044,12,10,2,1,1,1),_Pm1001pcCfgClientStartupIndex_Type())
pm1001pcCfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCfgClientStartupIndex.setStatus(_A)
class _Pm1001pcCfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgSystConfPortPortn_Type.__name__=_F
_Pm1001pcCfgSystConfPortPortn_Object=MibTableColumn
pm1001pcCfgSystConfPortPortn=_Pm1001pcCfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,12,10,2,1,1,3),_Pm1001pcCfgSystConfPortPortn_Type())
pm1001pcCfgSystConfPortPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgSystConfPortPortn.setStatus(_A)
class _Pm1001pcCfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgNetConfPortPortn_Type.__name__=_F
_Pm1001pcCfgNetConfPortPortn_Object=MibTableColumn
pm1001pcCfgNetConfPortPortn=_Pm1001pcCfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,12,10,2,1,1,4),_Pm1001pcCfgNetConfPortPortn_Type())
pm1001pcCfgNetConfPortPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgNetConfPortPortn.setStatus(_A)
class _Pm1001pcCfgFiberLengthPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgFiberLengthPortn_Type.__name__=_F
_Pm1001pcCfgFiberLengthPortn_Object=MibTableColumn
pm1001pcCfgFiberLengthPortn=_Pm1001pcCfgFiberLengthPortn_Object((1,3,6,1,4,1,20044,12,10,2,1,1,5),_Pm1001pcCfgFiberLengthPortn_Type())
pm1001pcCfgFiberLengthPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgFiberLengthPortn.setStatus(_A)
_Pm1001pctablelineStartup_ObjectIdentity=ObjectIdentity
pm1001pctablelineStartup=_Pm1001pctablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,12,10,2,2))
class _Pm1001pcCfgsynthTransLine_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgsynthTransLine_Type.__name__=_F
_Pm1001pcCfgsynthTransLine_Object=MibScalar
pm1001pcCfgsynthTransLine=_Pm1001pcCfgsynthTransLine_Object((1,3,6,1,4,1,20044,12,10,2,2,2),_Pm1001pcCfgsynthTransLine_Type())
pm1001pcCfgsynthTransLine.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgsynthTransLine.setStatus(_A)
class _Pm1001pcCfglineOptions1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfglineOptions1_Type.__name__=_F
_Pm1001pcCfglineOptions1_Object=MibScalar
pm1001pcCfglineOptions1=_Pm1001pcCfglineOptions1_Object((1,3,6,1,4,1,20044,12,10,2,2,5),_Pm1001pcCfglineOptions1_Type())
pm1001pcCfglineOptions1.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfglineOptions1.setStatus(_A)
_Pm1001pcCfgXfpTable_Object=MibTable
pm1001pcCfgXfpTable=_Pm1001pcCfgXfpTable_Object((1,3,6,1,4,1,20044,12,10,2,3))
if mibBuilder.loadTexts:pm1001pcCfgXfpTable.setStatus(_A)
_Pm1001pcCfgXfpEntry_Object=MibTableRow
pm1001pcCfgXfpEntry=_Pm1001pcCfgXfpEntry_Object((1,3,6,1,4,1,20044,12,10,2,3,1))
pm1001pcCfgXfpEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pm1001pcCfgXfpEntry.setStatus(_A)
class _Pm1001pcCfgXfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCfgXfpIndex_Type.__name__=_E
_Pm1001pcCfgXfpIndex_Object=MibTableColumn
pm1001pcCfgXfpIndex=_Pm1001pcCfgXfpIndex_Object((1,3,6,1,4,1,20044,12,10,2,3,1,1),_Pm1001pcCfgXfpIndex_Type())
pm1001pcCfgXfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCfgXfpIndex.setStatus(_A)
class _Pm1001pcCfgSystConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgSystConfXfpPortn_Type.__name__=_F
_Pm1001pcCfgSystConfXfpPortn_Object=MibTableColumn
pm1001pcCfgSystConfXfpPortn=_Pm1001pcCfgSystConfXfpPortn_Object((1,3,6,1,4,1,20044,12,10,2,3,1,3),_Pm1001pcCfgSystConfXfpPortn_Type())
pm1001pcCfgSystConfXfpPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgSystConfXfpPortn.setStatus(_A)
class _Pm1001pcCfgDataRateConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1001pcCfgDataRateConfXfpPortn_Type.__name__=_F
_Pm1001pcCfgDataRateConfXfpPortn_Object=MibTableColumn
pm1001pcCfgDataRateConfXfpPortn=_Pm1001pcCfgDataRateConfXfpPortn_Object((1,3,6,1,4,1,20044,12,10,2,3,1,4),_Pm1001pcCfgDataRateConfXfpPortn_Type())
pm1001pcCfgDataRateConfXfpPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgDataRateConfXfpPortn.setStatus(_H)
_Pm1001pcCfgLabels_ObjectIdentity=ObjectIdentity
pm1001pcCfgLabels=_Pm1001pcCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,12,10,3))
_Pm1001pcCfgLabelclientTable_Object=MibTable
pm1001pcCfgLabelclientTable=_Pm1001pcCfgLabelclientTable_Object((1,3,6,1,4,1,20044,12,10,3,1))
if mibBuilder.loadTexts:pm1001pcCfgLabelclientTable.setStatus(_A)
_Pm1001pcCfgLabelclientEntry_Object=MibTableRow
pm1001pcCfgLabelclientEntry=_Pm1001pcCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,12,10,3,1,1))
pm1001pcCfgLabelclientEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pm1001pcCfgLabelclientEntry.setStatus(_A)
class _Pm1001pcCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCfgLabelclientIndex_Type.__name__=_E
_Pm1001pcCfgLabelclientIndex_Object=MibTableColumn
pm1001pcCfgLabelclientIndex=_Pm1001pcCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,12,10,3,1,1,1),_Pm1001pcCfgLabelclientIndex_Type())
pm1001pcCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCfgLabelclientIndex.setStatus(_A)
class _Pm1001pcCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1001pcCfgLabelclientPortn_Type.__name__=_I
_Pm1001pcCfgLabelclientPortn_Object=MibTableColumn
pm1001pcCfgLabelclientPortn=_Pm1001pcCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,12,10,3,1,1,3),_Pm1001pcCfgLabelclientPortn_Type())
pm1001pcCfgLabelclientPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgLabelclientPortn.setStatus(_A)
_Pm1001pcCfgLabellineTable_Object=MibTable
pm1001pcCfgLabellineTable=_Pm1001pcCfgLabellineTable_Object((1,3,6,1,4,1,20044,12,10,3,2))
if mibBuilder.loadTexts:pm1001pcCfgLabellineTable.setStatus(_A)
_Pm1001pcCfgLabellineEntry_Object=MibTableRow
pm1001pcCfgLabellineEntry=_Pm1001pcCfgLabellineEntry_Object((1,3,6,1,4,1,20044,12,10,3,2,1))
pm1001pcCfgLabellineEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pm1001pcCfgLabellineEntry.setStatus(_A)
class _Pm1001pcCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1001pcCfgLabellineIndex_Type.__name__=_E
_Pm1001pcCfgLabellineIndex_Object=MibTableColumn
pm1001pcCfgLabellineIndex=_Pm1001pcCfgLabellineIndex_Object((1,3,6,1,4,1,20044,12,10,3,2,1,1),_Pm1001pcCfgLabellineIndex_Type())
pm1001pcCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pcCfgLabellineIndex.setStatus(_A)
class _Pm1001pcCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1001pcCfgLabellinePortn_Type.__name__=_I
_Pm1001pcCfgLabellinePortn_Object=MibTableColumn
pm1001pcCfgLabellinePortn=_Pm1001pcCfgLabellinePortn_Object((1,3,6,1,4,1,20044,12,10,3,2,1,3),_Pm1001pcCfgLabellinePortn_Type())
pm1001pcCfgLabellinePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgLabellinePortn.setStatus(_A)
_Pm1001pcCfgWriteConfiguration_Type=EkiOnOff
_Pm1001pcCfgWriteConfiguration_Object=MibScalar
pm1001pcCfgWriteConfiguration=_Pm1001pcCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,12,10,257),_Pm1001pcCfgWriteConfiguration_Type())
pm1001pcCfgWriteConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:pm1001pcCfgWriteConfiguration.setStatus(_A)
_Pm1001pctraps_ObjectIdentity=ObjectIdentity
pm1001pctraps=_Pm1001pctraps_ObjectIdentity((1,3,6,1,4,1,20044,12,11))
class _Pm1001pctrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1001pctrapBoardNumber_Type.__name__=_E
_Pm1001pctrapBoardNumber_Object=MibScalar
pm1001pctrapBoardNumber=_Pm1001pctrapBoardNumber_Object((1,3,6,1,4,1,20044,12,11,1),_Pm1001pctrapBoardNumber_Type())
pm1001pctrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1001pctrapBoardNumber.setStatus(_A)
pm1001pcLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,30))
pm1001pcLineTrapNotUrgentGoesOn.setObjects(*((_C,_J),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcLineTrapNotUrgentGoesOn.setStatus(_A)
pm1001pcLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,31))
pm1001pcLineTrapNotUrgentGoesOff.setObjects(*((_C,_J),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcLineTrapNotUrgentGoesOff.setStatus(_A)
pm1001pcLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,32))
pm1001pcLineTrapUrgentGoesOn.setObjects(*((_C,_K),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcLineTrapUrgentGoesOn.setStatus(_A)
pm1001pcLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,33))
pm1001pcLineTrapUrgentGoesOff.setObjects(*((_C,_K),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcLineTrapUrgentGoesOff.setStatus(_A)
pm1001pcLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,34))
pm1001pcLineTrapCritGoesOn.setObjects(*((_C,_L),(_C,_M),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcLineTrapCritGoesOn.setStatus(_A)
pm1001pcLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,35))
pm1001pcLineTrapCritGoesOff.setObjects(*((_C,_L),(_C,_M),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcLineTrapCritGoesOff.setStatus(_A)
pm1001pcClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,40))
pm1001pcClientTrapNotUrgentGoesOn.setObjects(*((_C,_N),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcClientTrapNotUrgentGoesOn.setStatus(_A)
pm1001pcClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,41))
pm1001pcClientTrapNotUrgentGoesOff.setObjects(*((_C,_N),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcClientTrapNotUrgentGoesOff.setStatus(_A)
pm1001pcClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,42))
pm1001pcClientTrapUrgentGoesOn.setObjects(*((_C,_O),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcClientTrapUrgentGoesOn.setStatus(_A)
pm1001pcClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,43))
pm1001pcClientTrapUrgentGoesOff.setObjects(*((_C,_O),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcClientTrapUrgentGoesOff.setStatus(_A)
pm1001pcClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,44))
pm1001pcClientTrapCritGoesOn.setObjects(*((_C,_P),(_C,_Q),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcClientTrapCritGoesOn.setStatus(_A)
pm1001pcClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,45))
pm1001pcClientTrapCritGoesOff.setObjects(*((_C,_P),(_C,_Q),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcClientTrapCritGoesOff.setStatus(_A)
pm1001pcPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,12,11,50))
pm1001pcPowerTrapUrgentGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcPowerTrapUrgentGoesOn.setStatus(_A)
pm1001pcPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,12,11,51))
pm1001pcPowerTrapUrgentGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_G)))
if mibBuilder.loadTexts:pm1001pcPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'modulepm1001pc':modulepm1001pc,'pm1001pcalarms':pm1001pcalarms,'pm1001pcAlmOther':pm1001pcAlmOther,'pm1001pcAlmOtherNurg':pm1001pcAlmOtherNurg,'pm1001pcAlmsynthAlm2':pm1001pcAlmsynthAlm2,'pm1001pcAlmConfTableSave':pm1001pcAlmConfTableSave,'pm1001pcAlmInvUpload':pm1001pcAlmInvUpload,'pm1001pcAlmConfTableLoad':pm1001pcAlmConfTableLoad,'pm1001pcAlmCorrelatOff':pm1001pcAlmCorrelatOff,'pm1001pcAlmMaintenanceOn':pm1001pcAlmMaintenanceOn,'pm1001pcAlmOtherUrg':pm1001pcAlmOtherUrg,'pm1001pcAlmmodInitFailLevel2':pm1001pcAlmmodInitFailLevel2,'pm1001pcAlmLedFail':pm1001pcAlmLedFail,'pm1001pcAlmNextColdBootForced':pm1001pcAlmNextColdBootForced,'pm1001pcAlmBootUndone':pm1001pcAlmBootUndone,'pm1001pcAlmResetHwInitFail':pm1001pcAlmResetHwInitFail,'pm1001pcAlmSwInitFail':pm1001pcAlmSwInitFail,'pm1001pcAlmmodInitFailLevel3':pm1001pcAlmmodInitFailLevel3,'pm1001pcAlmGwIdentFail':pm1001pcAlmGwIdentFail,'pm1001pcAlmObmTypeReadFail':pm1001pcAlmObmTypeReadFail,'pm1001pcAlmInitModuleFail':pm1001pcAlmInitModuleFail,'pm1001pcAlmXfp1InitFail':pm1001pcAlmXfp1InitFail,'pm1001pcAlmXfp2InitFail':pm1001pcAlmXfp2InitFail,'pm1001pcAlmLineInitFail':pm1001pcAlmLineInitFail,'pm1001pcAlmClientInitFail':pm1001pcAlmClientInitFail,'pm1001pcAlmOtherCrit':pm1001pcAlmOtherCrit,'pm1001pcAlmsynthAlm0':pm1001pcAlmsynthAlm0,'pm1001pcAlmModGlobFail':pm1001pcAlmModGlobFail,_S:pm1001pcAlmDefFuseA,_R:pm1001pcAlmDefFuseB,'pm1001pcAlmClient':pm1001pcAlmClient,'pm1001pcAlmClientNurg':pm1001pcAlmClientNurg,'pm1001pcAlmclientXfpWarnings':pm1001pcAlmclientXfpWarnings,'pm1001pcAlmClientTxPowerLowWarning':pm1001pcAlmClientTxPowerLowWarning,'pm1001pcAlmClientTxPowerHighWarning':pm1001pcAlmClientTxPowerHighWarning,'pm1001pcAlmClientTxBiasLowWarning':pm1001pcAlmClientTxBiasLowWarning,'pm1001pcAlmClientTxBiasHighWarning':pm1001pcAlmClientTxBiasHighWarning,'pm1001pcAlmClientTempLowWarning':pm1001pcAlmClientTempLowWarning,'pm1001pcAlmClientTempHighWarning':pm1001pcAlmClientTempHighWarning,'pm1001pcAlmClientRxPowerLowWarning':pm1001pcAlmClientRxPowerLowWarning,'pm1001pcAlmClientRxPowerHighWarning':pm1001pcAlmClientRxPowerHighWarning,'pm1001pcAlmClientUrg':pm1001pcAlmClientUrg,'pm1001pcAlmclientXfpAlarm1':pm1001pcAlmclientXfpAlarm1,'pm1001pcAlmClientTxPowerLowAlarm':pm1001pcAlmClientTxPowerLowAlarm,'pm1001pcAlmClientTxPowerHighAlarm':pm1001pcAlmClientTxPowerHighAlarm,'pm1001pcAlmClientTxBiasLowAlarm':pm1001pcAlmClientTxBiasLowAlarm,'pm1001pcAlmClientTxBiasHighAlarm':pm1001pcAlmClientTxBiasHighAlarm,'pm1001pcAlmClientTempLowAlarm':pm1001pcAlmClientTempLowAlarm,'pm1001pcAlmClientTempHighAlarm':pm1001pcAlmClientTempHighAlarm,'pm1001pcAlmClientRxPowerLowAlarm':pm1001pcAlmClientRxPowerLowAlarm,'pm1001pcAlmClientRxPowerHighAlarm':pm1001pcAlmClientRxPowerHighAlarm,'pm1001pcAlmclientXfpSupplyAlarm':pm1001pcAlmclientXfpSupplyAlarm,'pm1001pcAlmClientVee5LowAlarm':pm1001pcAlmClientVee5LowAlarm,'pm1001pcAlmClientVee5HighAlarm':pm1001pcAlmClientVee5HighAlarm,'pm1001pcAlmClientVcc2LowAlarm':pm1001pcAlmClientVcc2LowAlarm,'pm1001pcAlmClientVcc2HighAlarm':pm1001pcAlmClientVcc2HighAlarm,'pm1001pcAlmClientVcc3LowAlarm':pm1001pcAlmClientVcc3LowAlarm,'pm1001pcAlmClientVcc3HighAlarm':pm1001pcAlmClientVcc3HighAlarm,'pm1001pcAlmClientVcc5LowAlarm':pm1001pcAlmClientVcc5LowAlarm,'pm1001pcAlmClientVcc5HighAlarm':pm1001pcAlmClientVcc5HighAlarm,'pm1001pcAlmClientVee5LowWarning':pm1001pcAlmClientVee5LowWarning,'pm1001pcAlmClientVee5HighWarning':pm1001pcAlmClientVee5HighWarning,'pm1001pcAlmClientVcc2LowWarning':pm1001pcAlmClientVcc2LowWarning,'pm1001pcAlmClientVcc2HighWarning':pm1001pcAlmClientVcc2HighWarning,'pm1001pcAlmClientVcc3LowWarning':pm1001pcAlmClientVcc3LowWarning,'pm1001pcAlmClientVcc3HighWarning':pm1001pcAlmClientVcc3HighWarning,'pm1001pcAlmClientVcc5LowWarning':pm1001pcAlmClientVcc5LowWarning,'pm1001pcAlmClientVcc5HighWarning':pm1001pcAlmClientVcc5HighWarning,'pm1001pcAlmClientCrit':pm1001pcAlmClientCrit,'pm1001pcAlmsynthAlmPort':pm1001pcAlmsynthAlmPort,'pm1001pcAlmClientXfpAbsent':pm1001pcAlmClientXfpAbsent,'pm1001pcAlmClientDdmAbsent':pm1001pcAlmClientDdmAbsent,_Q:pm1001pcAlmClientHwFail,'pm1001pcAlmClientDwLsd':pm1001pcAlmClientDwLsd,'pm1001pcAlmClientLocalOos':pm1001pcAlmClientLocalOos,'pm1001pcAlmClientDwCais':pm1001pcAlmClientDwCais,_N:pm1001pcAlmClientXfpDdmWarning,_O:pm1001pcAlmClientXfpDdmAlm,_P:pm1001pcAlmClientFail,'pm1001pcAlmClientUpCsf':pm1001pcAlmClientUpCsf,'pm1001pcAlmclientAccessioAlm':pm1001pcAlmclientAccessioAlm,'pm1001pcAlmClientDwLasFail':pm1001pcAlmClientDwLasFail,'pm1001pcAlmClientUpLos':pm1001pcAlmClientUpLos,'pm1001pcAlmclientXfpAlarm2':pm1001pcAlmclientXfpAlarm2,'pm1001pcAlmClientModNr':pm1001pcAlmClientModNr,'pm1001pcAlmClientRxCdrNotLocked1':pm1001pcAlmClientRxCdrNotLocked1,'pm1001pcAlmClientRxNr':pm1001pcAlmClientRxNr,'pm1001pcAlmClientTxCdrNotLocked1':pm1001pcAlmClientTxCdrNotLocked1,'pm1001pcAlmClientTxFault':pm1001pcAlmClientTxFault,'pm1001pcAlmClientTxNr':pm1001pcAlmClientTxNr,'pm1001pcAlmClientWavelengthUnlocked':pm1001pcAlmClientWavelengthUnlocked,'pm1001pcAlmClientTecFault':pm1001pcAlmClientTecFault,'pm1001pcAlmClientApdSupplyFault':pm1001pcAlmClientApdSupplyFault,'pm1001pcAlmclientMapperDeAlm':pm1001pcAlmclientMapperDeAlm,'pm1001pcAlmClientUpAccOos':pm1001pcAlmClientUpAccOos,'pm1001pcAlmClientUpBufferOvl':pm1001pcAlmClientUpBufferOvl,'pm1001pcAlmClientDwCsfDet':pm1001pcAlmClientDwCsfDet,'pm1001pcAlmClientDwBufferOvl':pm1001pcAlmClientDwBufferOvl,'pm1001pcAlmLine':pm1001pcAlmLine,'pm1001pcAlmLineNurg':pm1001pcAlmLineNurg,'pm1001pcAlmlineXfpWarnings':pm1001pcAlmlineXfpWarnings,'pm1001pcAlmLineTxPowerLowWarning':pm1001pcAlmLineTxPowerLowWarning,'pm1001pcAlmLineTxPowerHighWarning':pm1001pcAlmLineTxPowerHighWarning,'pm1001pcAlmLineTxBiasLowWarning':pm1001pcAlmLineTxBiasLowWarning,'pm1001pcAlmLineTxBiasHighWarning':pm1001pcAlmLineTxBiasHighWarning,'pm1001pcAlmLineTempLowWarning':pm1001pcAlmLineTempLowWarning,'pm1001pcAlmLineTempHighWarning':pm1001pcAlmLineTempHighWarning,'pm1001pcAlmLineRxPowerLowWarning':pm1001pcAlmLineRxPowerLowWarning,'pm1001pcAlmLineRxPowerHighWarning':pm1001pcAlmLineRxPowerHighWarning,'pm1001pcAlmLineUrg':pm1001pcAlmLineUrg,'pm1001pcAlmdfrmBer':pm1001pcAlmdfrmBer,'pm1001pcAlmLineSignalDegrade':pm1001pcAlmLineSignalDegrade,'pm1001pcAlmLineSignalFail':pm1001pcAlmLineSignalFail,'pm1001pcAlmLineDegrade':pm1001pcAlmLineDegrade,'pm1001pcAlmlineXfpAlarm1':pm1001pcAlmlineXfpAlarm1,'pm1001pcAlmLineTxPowerLowAlarm':pm1001pcAlmLineTxPowerLowAlarm,'pm1001pcAlmLineTxPowerHighAlarm':pm1001pcAlmLineTxPowerHighAlarm,'pm1001pcAlmLineTxBiasLowAlarm':pm1001pcAlmLineTxBiasLowAlarm,'pm1001pcAlmLineTxBiasHighAlarm':pm1001pcAlmLineTxBiasHighAlarm,'pm1001pcAlmLineTempLowAlarm':pm1001pcAlmLineTempLowAlarm,'pm1001pcAlmLineTempHighAlarm':pm1001pcAlmLineTempHighAlarm,'pm1001pcAlmLineRxPowerLowAlarm':pm1001pcAlmLineRxPowerLowAlarm,'pm1001pcAlmLineRxPowerHighAlarm':pm1001pcAlmLineRxPowerHighAlarm,'pm1001pcAlmlineXfpSupplyAlarm':pm1001pcAlmlineXfpSupplyAlarm,'pm1001pcAlmLineVee5LowAlarm':pm1001pcAlmLineVee5LowAlarm,'pm1001pcAlmLineVee5HighAlarm':pm1001pcAlmLineVee5HighAlarm,'pm1001pcAlmLineVcc2LowAlarm':pm1001pcAlmLineVcc2LowAlarm,'pm1001pcAlmLineVcc2HighAlarm':pm1001pcAlmLineVcc2HighAlarm,'pm1001pcAlmLineVcc3LowAlarm':pm1001pcAlmLineVcc3LowAlarm,'pm1001pcAlmLineVcc3HighAlarm':pm1001pcAlmLineVcc3HighAlarm,'pm1001pcAlmLineVcc5LowAlarm':pm1001pcAlmLineVcc5LowAlarm,'pm1001pcAlmLineVcc5HighAlarm':pm1001pcAlmLineVcc5HighAlarm,'pm1001pcAlmLineVee5LowLineWarning':pm1001pcAlmLineVee5LowLineWarning,'pm1001pcAlmLineVee5HighWarning':pm1001pcAlmLineVee5HighWarning,'pm1001pcAlmLineVcc2LowWarning':pm1001pcAlmLineVcc2LowWarning,'pm1001pcAlmLineVcc2HighWarning':pm1001pcAlmLineVcc2HighWarning,'pm1001pcAlmLineVcc3LowWarning':pm1001pcAlmLineVcc3LowWarning,'pm1001pcAlmLineVcc3HighWarning':pm1001pcAlmLineVcc3HighWarning,'pm1001pcAlmLineVcc5LowWarning':pm1001pcAlmLineVcc5LowWarning,'pm1001pcAlmLineVcc5HighWarning':pm1001pcAlmLineVcc5HighWarning,'pm1001pcAlmLineCrit':pm1001pcAlmLineCrit,'pm1001pcAlmsynthAlmLine':pm1001pcAlmsynthAlmLine,'pm1001pcAlmLineXfpAbsent':pm1001pcAlmLineXfpAbsent,'pm1001pcAlmLineXfpInitNotCompl':pm1001pcAlmLineXfpInitNotCompl,_M:pm1001pcAlmLineHwFail,'pm1001pcAlmLineXfpTxOff':pm1001pcAlmLineXfpTxOff,'pm1001pcAlmLineLocalOos':pm1001pcAlmLineLocalOos,'pm1001pcAlmLineUpRdiIns':pm1001pcAlmLineUpRdiIns,_J:pm1001pcAlmLineDdmWarning,_K:pm1001pcAlmLineDdmAlm,_L:pm1001pcAlmLineFail,'pm1001pcAlmdfrmAlm':pm1001pcAlmdfrmAlm,'pm1001pcAlmLineDwAisDet':pm1001pcAlmLineDwAisDet,'pm1001pcAlmLineDwRdiDet':pm1001pcAlmLineDwRdiDet,'pm1001pcAlmLineDwOof':pm1001pcAlmLineDwOof,'pm1001pcAlmLineDwLof':pm1001pcAlmLineDwLof,'pm1001pcAlmlineSyncAlarms':pm1001pcAlmlineSyncAlarms,'pm1001pcAlmLineDwLockerr':pm1001pcAlmLineDwLockerr,'pm1001pcAlmLineUpLockerr':pm1001pcAlmLineUpLockerr,'pm1001pcAlmLineDwLos':pm1001pcAlmLineDwLos,'pm1001pcAlmlineXfpAlarms2':pm1001pcAlmlineXfpAlarms2,'pm1001pcAlmLineModNr':pm1001pcAlmLineModNr,'pm1001pcAlmLineRxCdrNotLocked1':pm1001pcAlmLineRxCdrNotLocked1,'pm1001pcAlmLineRxNr':pm1001pcAlmLineRxNr,'pm1001pcAlmLineTxCdrNotLocked1':pm1001pcAlmLineTxCdrNotLocked1,'pm1001pcAlmLineTxFault':pm1001pcAlmLineTxFault,'pm1001pcAlmLineTxNr':pm1001pcAlmLineTxNr,'pm1001pcAlmLineWavelengthUnlocked':pm1001pcAlmLineWavelengthUnlocked,'pm1001pcAlmLineTecFault':pm1001pcAlmLineTecFault,'pm1001pcAlmLineApdSupplyFault':pm1001pcAlmLineApdSupplyFault,'pm1001pcmeasures':pm1001pcmeasures,'pm1001pcMesrOther':pm1001pcMesrOther,'pm1001pcMesrsynth0':pm1001pcMesrsynth0,'pm1001pcMesrsynth1':pm1001pcMesrsynth1,'pm1001pcMesrClient':pm1001pcMesrClient,'pm1001pcMesrclientModTempMeas':pm1001pcMesrclientModTempMeas,'pm1001pcMesrclientBiasCurrentMeas':pm1001pcMesrclientBiasCurrentMeas,'pm1001pcMesrclientTxPowerMeas':pm1001pcMesrclientTxPowerMeas,'pm1001pcMesrclientRxPowerMeas':pm1001pcMesrclientRxPowerMeas,'pm1001pcMesrLine':pm1001pcMesrLine,'pm1001pcMesrlineModTempMeas':pm1001pcMesrlineModTempMeas,'pm1001pcMesrlineReserved':pm1001pcMesrlineReserved,'pm1001pcMesrlineBiasCurrentMeas':pm1001pcMesrlineBiasCurrentMeas,'pm1001pcMesrlineTxPowerMeas':pm1001pcMesrlineTxPowerMeas,'pm1001pcMesrlineRxPowerMeas':pm1001pcMesrlineRxPowerMeas,'pm1001pcMesrlineAux1Meas':pm1001pcMesrlineAux1Meas,'pm1001pcMesrlineAux2Meas':pm1001pcMesrlineAux2Meas,'pm1001pccounters':pm1001pccounters,'pm1001pcCntOther':pm1001pcCntOther,'pm1001pcCntClient':pm1001pcCntClient,'pm1001pcCntclientUpErrCntTable':pm1001pcCntclientUpErrCntTable,'pm1001pcCntclientUpErrCntEntry':pm1001pcCntclientUpErrCntEntry,_T:pm1001pcCntclientUpErrCntIndex,'pm1001pcCntclientUpErrCntValuePortn':pm1001pcCntclientUpErrCntValuePortn,'pm1001pcCntclientUpErrCntErrorPortn':pm1001pcCntclientUpErrCntErrorPortn,'pm1001pcCntclientUpErrCntOverloadPortn':pm1001pcCntclientUpErrCntOverloadPortn,'pm1001pcCntclientUpTimCntTable':pm1001pcCntclientUpTimCntTable,'pm1001pcCntclientUpTimCntEntry':pm1001pcCntclientUpTimCntEntry,_U:pm1001pcCntclientUpTimCntIndex,'pm1001pcCntclientUpTimCntValuePortn':pm1001pcCntclientUpTimCntValuePortn,'pm1001pcCntclientUpTimCntErrorPortn':pm1001pcCntclientUpTimCntErrorPortn,'pm1001pcCntclientUpTimCntOverloadPortn':pm1001pcCntclientUpTimCntOverloadPortn,'pm1001pcCntclientDwErrCntTable':pm1001pcCntclientDwErrCntTable,'pm1001pcCntclientDwErrCntEntry':pm1001pcCntclientDwErrCntEntry,_V:pm1001pcCntclientDwErrCntIndex,'pm1001pcCntclientDwErrCntValuePortn':pm1001pcCntclientDwErrCntValuePortn,'pm1001pcCntclientDwErrCntErrorPortn':pm1001pcCntclientDwErrCntErrorPortn,'pm1001pcCntclientDwErrCntOverloadPortn':pm1001pcCntclientDwErrCntOverloadPortn,'pm1001pcCntclientDwTimCntTable':pm1001pcCntclientDwTimCntTable,'pm1001pcCntclientDwTimCntEntry':pm1001pcCntclientDwTimCntEntry,_W:pm1001pcCntclientDwTimCntIndex,'pm1001pcCntclientDwTimCntValuePortn':pm1001pcCntclientDwTimCntValuePortn,'pm1001pcCntclientDwTimCntErrorPortn':pm1001pcCntclientDwTimCntErrorPortn,'pm1001pcCntclientDwTimCntOverloadPortn':pm1001pcCntclientDwTimCntOverloadPortn,'pm1001pcCntLine':pm1001pcCntLine,'pm1001pcCntlineDfrmErrCntTable':pm1001pcCntlineDfrmErrCntTable,'pm1001pcCntlineDfrmErrCntEntry':pm1001pcCntlineDfrmErrCntEntry,_X:pm1001pcCntlineDfrmErrCntIndex,'pm1001pcCntlineDfrmErrCntValuePortn':pm1001pcCntlineDfrmErrCntValuePortn,'pm1001pcCntlineDfrmErrCntErrorPortn':pm1001pcCntlineDfrmErrCntErrorPortn,'pm1001pcCntlineDfrmErrCntOverloadPortn':pm1001pcCntlineDfrmErrCntOverloadPortn,'pm1001pcCntlineDfrmTimCntTable':pm1001pcCntlineDfrmTimCntTable,'pm1001pcCntlineDfrmTimCntEntry':pm1001pcCntlineDfrmTimCntEntry,_Y:pm1001pcCntlineDfrmTimCntIndex,'pm1001pcCntlineDfrmTimCntValuePortn':pm1001pcCntlineDfrmTimCntValuePortn,'pm1001pcCntlineDfrmTimCntErrorPortn':pm1001pcCntlineDfrmTimCntErrorPortn,'pm1001pcCntlineDfrmTimCntOverloadPortn':pm1001pcCntlineDfrmTimCntOverloadPortn,'pm1001pcCntlineDfrmPrimErrCntTable':pm1001pcCntlineDfrmPrimErrCntTable,'pm1001pcCntlineDfrmPrimErrCntEntry':pm1001pcCntlineDfrmPrimErrCntEntry,_Z:pm1001pcCntlineDfrmPrimErrCntIndex,'pm1001pcCntlineDfrmPrimErrCntValuePortn':pm1001pcCntlineDfrmPrimErrCntValuePortn,'pm1001pcCntlineDfrmPrimErrCntErrorPortn':pm1001pcCntlineDfrmPrimErrCntErrorPortn,'pm1001pcCntlineDfrmPrimErrCntOverloadPortn':pm1001pcCntlineDfrmPrimErrCntOverloadPortn,'pm1001pcCntlineDfrmErrCntSTable':pm1001pcCntlineDfrmErrCntSTable,'pm1001pcCntlineDfrmErrCntSEntry':pm1001pcCntlineDfrmErrCntSEntry,_a:pm1001pcCntlineDfrmErrCntSIndex,'pm1001pcCntlineDfrmErrCntSValuePortn':pm1001pcCntlineDfrmErrCntSValuePortn,'pm1001pcCntlineDfrmErrCntSErrorPortn':pm1001pcCntlineDfrmErrCntSErrorPortn,'pm1001pcCntlineDfrmErrCntSOverloadPortn':pm1001pcCntlineDfrmErrCntSOverloadPortn,'pm1001pcCntCountersReset':pm1001pcCntCountersReset,'pm1001pcCntCountersStop':pm1001pcCntCountersStop,'pm1001pccontrolsWrite':pm1001pccontrolsWrite,'pm1001pcCtrlOther':pm1001pcCtrlOther,'pm1001pcCtrlconfMgnt1':pm1001pcCtrlconfMgnt1,'pm1001pcCtrlConf1Load1':pm1001pcCtrlConf1Load1,'pm1001pcCtrlConf2Load1':pm1001pcCtrlConf2Load1,'pm1001pcCtrlConf2Flash1':pm1001pcCtrlConf2Flash1,'pm1001pcCtrlConf2Clear1':pm1001pcCtrlConf2Clear1,'pm1001pcCtrlsynth4':pm1001pcCtrlsynth4,'pm1001pcCtrlCorrelatOn':pm1001pcCtrlCorrelatOn,'pm1001pcCtrlCorrelatOff':pm1001pcCtrlCorrelatOff,'pm1001pcCtrlswMgnt':pm1001pcCtrlswMgnt,'pm1001pcCtrlColdReset':pm1001pcCtrlColdReset,'pm1001pcCtrlWarmReset':pm1001pcCtrlWarmReset,'pm1001pcCtrlLoadSwBank1':pm1001pcCtrlLoadSwBank1,'pm1001pcCtrlLoadSwBank2':pm1001pcCtrlLoadSwBank2,'pm1001pcCtrlgwMgnt':pm1001pcCtrlgwMgnt,'pm1001pcCtrlCurrentGwReset':pm1001pcCtrlCurrentGwReset,'pm1001pcCtrlLoadGwBank1':pm1001pcCtrlLoadGwBank1,'pm1001pcCtrlLoadGwBank2':pm1001pcCtrlLoadGwBank2,'pm1001pcCtrlLoadGwBank3':pm1001pcCtrlLoadGwBank3,'pm1001pcCtrlLoadGwBank4':pm1001pcCtrlLoadGwBank4,'pm1001pcCtrlledTest':pm1001pcCtrlledTest,'pm1001pcCtrlGreenLed':pm1001pcCtrlGreenLed,'pm1001pcCtrlRedLed':pm1001pcCtrlRedLed,'pm1001pcCtrlLedOff':pm1001pcCtrlLedOff,'pm1001pcCtrlmoduleOosMode':pm1001pcCtrlmoduleOosMode,'pm1001pcCtrlModuleOosMode':pm1001pcCtrlModuleOosMode,'pm1001pcCtrlmaintenanceMode':pm1001pcCtrlmaintenanceMode,'pm1001pcCtrlMaintenanceMode':pm1001pcCtrlMaintenanceMode,'pm1001pcCtrldccEnable':pm1001pcCtrldccEnable,'pm1001pcCtrlDccEnable':pm1001pcCtrlDccEnable,'pm1001pcCtrlClient':pm1001pcCtrlClient,'pm1001pcCtrlaccessLoopTable':pm1001pcCtrlaccessLoopTable,'pm1001pcCtrlaccessLoopEntry':pm1001pcCtrlaccessLoopEntry,_b:pm1001pcCtrlaccessLoopIndex,'pm1001pcCtrlaccessLoopPortn':pm1001pcCtrlaccessLoopPortn,'pm1001pcCtrlportOosModeTable':pm1001pcCtrlportOosModeTable,'pm1001pcCtrlportOosModeEntry':pm1001pcCtrlportOosModeEntry,_c:pm1001pcCtrlportOosModeIndex,'pm1001pcCtrlportOosModePortn':pm1001pcCtrlportOosModePortn,'pm1001pcCtrlxfpOffCtrlTable':pm1001pcCtrlxfpOffCtrlTable,'pm1001pcCtrlxfpOffCtrlEntry':pm1001pcCtrlxfpOffCtrlEntry,_d:pm1001pcCtrlxfpOffCtrlIndex,'pm1001pcCtrlxfpOffCtrlPortn':pm1001pcCtrlxfpOffCtrlPortn,'pm1001pcCtrlcsfUpInsTable':pm1001pcCtrlcsfUpInsTable,'pm1001pcCtrlcsfUpInsEntry':pm1001pcCtrlcsfUpInsEntry,_e:pm1001pcCtrlcsfUpInsIndex,'pm1001pcCtrlcsfUpInsPortn':pm1001pcCtrlcsfUpInsPortn,'pm1001pcCtrlcaisDwInsTable':pm1001pcCtrlcaisDwInsTable,'pm1001pcCtrlcaisDwInsEntry':pm1001pcCtrlcaisDwInsEntry,_f:pm1001pcCtrlcaisDwInsIndex,'pm1001pcCtrlcaisDwInsPortn':pm1001pcCtrlcaisDwInsPortn,'pm1001pcCtrlflowControlTable':pm1001pcCtrlflowControlTable,'pm1001pcCtrlflowControlEntry':pm1001pcCtrlflowControlEntry,_g:pm1001pcCtrlflowControlIndex,'pm1001pcCtrlflowControlPortn':pm1001pcCtrlflowControlPortn,'pm1001pcCtrlfiberLength':pm1001pcCtrlfiberLength,'pm1001pcCtrlclientAccessTermLoopTable':pm1001pcCtrlclientAccessTermLoopTable,'pm1001pcCtrlclientAccessTermLoopEntry':pm1001pcCtrlclientAccessTermLoopEntry,_h:pm1001pcCtrlclientAccessTermLoopIndex,'pm1001pcCtrlclientAccessTermLoopPortn':pm1001pcCtrlclientAccessTermLoopPortn,'pm1001pcCtrlxfpXfiLoopTable':pm1001pcCtrlxfpXfiLoopTable,'pm1001pcCtrlxfpXfiLoopEntry':pm1001pcCtrlxfpXfiLoopEntry,_i:pm1001pcCtrlxfpXfiLoopIndex,'pm1001pcCtrlxfpXfiLoopPortn':pm1001pcCtrlxfpXfiLoopPortn,'pm1001pcCtrlLine':pm1001pcCtrlLine,'pm1001pcCtrlcommAccessLoop':pm1001pcCtrlcommAccessLoop,'pm1001pcCtrlCommAccessloop':pm1001pcCtrlCommAccessloop,'pm1001pcCtrllineLoop':pm1001pcCtrllineLoop,'pm1001pcCtrlLineLoop':pm1001pcCtrlLineLoop,'pm1001pcCtrlmsAis':pm1001pcCtrlmsAis,'pm1001pcCtrlMsAis':pm1001pcCtrlMsAis,'pm1001pcCtrllineOosMode':pm1001pcCtrllineOosMode,'pm1001pcCtrlLineOosMode':pm1001pcCtrlLineOosMode,'pm1001pcCtrlxfpOnoffTable':pm1001pcCtrlxfpOnoffTable,'pm1001pcCtrlxfpOnoffEntry':pm1001pcCtrlxfpOnoffEntry,_j:pm1001pcCtrlxfpOnoffIndex,'pm1001pcCtrlxfpOnoffPortn':pm1001pcCtrlxfpOnoffPortn,'pm1001pcCtrlxfpLineLoopTable':pm1001pcCtrlxfpLineLoopTable,'pm1001pcCtrlxfpLineLoopEntry':pm1001pcCtrlxfpLineLoopEntry,_k:pm1001pcCtrlxfpLineLoopIndex,'pm1001pcCtrlxfpLineLoopPortn':pm1001pcCtrlxfpLineLoopPortn,'pm1001pcCtrlxfpLineXfiLoopTable':pm1001pcCtrlxfpLineXfiLoopTable,'pm1001pcCtrlxfpLineXfiLoopEntry':pm1001pcCtrlxfpLineXfiLoopEntry,_l:pm1001pcCtrlxfpLineXfiLoopIndex,'pm1001pcCtrlxfpLineXfiLoopPortn':pm1001pcCtrlxfpLineXfiLoopPortn,'pm1001pcCtrllineLoopTransceiverTable':pm1001pcCtrllineLoopTransceiverTable,'pm1001pcCtrllineLoopTransceiverEntry':pm1001pcCtrllineLoopTransceiverEntry,_m:pm1001pcCtrllineLoopTransceiverIndex,'pm1001pcCtrllineLoopTransceiverPortn':pm1001pcCtrllineLoopTransceiverPortn,'pm1001pcri':pm1001pcri,'pm1001pcriTable':pm1001pcriTable,'pm1001pcRinvReloadInventory':pm1001pcRinvReloadInventory,'pm1001pcRinvHwPlatform':pm1001pcRinvHwPlatform,'pm1001pcRinvModulePlatform':pm1001pcRinvModulePlatform,'pm1001pcRinvSwPlatform':pm1001pcRinvSwPlatform,'pm1001pcRinvGwPlatform':pm1001pcRinvGwPlatform,'pm1001pcRinvClient':pm1001pcRinvClient,'pm1001pcRinvLine':pm1001pcRinvLine,'pm1001pcdownload':pm1001pcdownload,'pm1001pcDwlOther':pm1001pcDwlOther,'pm1001pcDwlrestartProcess':pm1001pcDwlrestartProcess,'pm1001pcDwlWarmRestartProcessed':pm1001pcDwlWarmRestartProcessed,'pm1001pcDwlColdRestartProcessed':pm1001pcDwlColdRestartProcessed,'pm1001pcDwlswBanksUsed':pm1001pcDwlswBanksUsed,'pm1001pcDwlSwBank1Used':pm1001pcDwlSwBank1Used,'pm1001pcDwlSwBank2Used':pm1001pcDwlSwBank2Used,'pm1001pcDwlSwBank1Notempty':pm1001pcDwlSwBank1Notempty,'pm1001pcDwlSwBank2Notempty':pm1001pcDwlSwBank2Notempty,'pm1001pcDwlgwBanksUsed':pm1001pcDwlgwBanksUsed,'pm1001pcDwlGwBank1Used':pm1001pcDwlGwBank1Used,'pm1001pcDwlGwBank2Used':pm1001pcDwlGwBank2Used,'pm1001pcDwlGwBank3Used':pm1001pcDwlGwBank3Used,'pm1001pcDwlGwBank4Used':pm1001pcDwlGwBank4Used,'pm1001pcDwlGwBank1Notempty':pm1001pcDwlGwBank1Notempty,'pm1001pcDwlGwBank2Notempty':pm1001pcDwlGwBank2Notempty,'pm1001pcDwlGwBank3Notempty':pm1001pcDwlGwBank3Notempty,'pm1001pcDwlGwBank4Notempty':pm1001pcDwlGwBank4Notempty,'pm1001pcDwlClient':pm1001pcDwlClient,'pm1001pcDwlLine':pm1001pcDwlLine,'pm1001pcrmon':pm1001pcrmon,'pm1001pcRmonOther':pm1001pcRmonOther,'pm1001pcMonCountersReset':pm1001pcMonCountersReset,'pm1001pcMonCountersStop':pm1001pcMonCountersStop,'pm1001pcRmonClient':pm1001pcRmonClient,'pm1001pcMonupRmonByteCntTable':pm1001pcMonupRmonByteCntTable,'pm1001pcMonupRmonByteCntEntry':pm1001pcMonupRmonByteCntEntry,_n:pm1001pcMonupRmonByteCntIndex,'pm1001pcMonupRmonByteCntValuePortn':pm1001pcMonupRmonByteCntValuePortn,'pm1001pcMonupRmonByteCntErrorPortn':pm1001pcMonupRmonByteCntErrorPortn,'pm1001pcMonupRmonByteCntOverloadPortn':pm1001pcMonupRmonByteCntOverloadPortn,'pm1001pcMonupRmonCrcErrorCntTable':pm1001pcMonupRmonCrcErrorCntTable,'pm1001pcMonupRmonCrcErrorCntEntry':pm1001pcMonupRmonCrcErrorCntEntry,_o:pm1001pcMonupRmonCrcErrorCntIndex,'pm1001pcMonupRmonCrcErrorCntValuePortn':pm1001pcMonupRmonCrcErrorCntValuePortn,'pm1001pcMonupRmonCrcErrorCntErrorPortn':pm1001pcMonupRmonCrcErrorCntErrorPortn,'pm1001pcMonupRmonCrcErrorCntOverloadPortn':pm1001pcMonupRmonCrcErrorCntOverloadPortn,'pm1001pcMonupRmonPacketsCntTable':pm1001pcMonupRmonPacketsCntTable,'pm1001pcMonupRmonPacketsCntEntry':pm1001pcMonupRmonPacketsCntEntry,_p:pm1001pcMonupRmonPacketsCntIndex,'pm1001pcMonupRmonPacketsCntValuePortn':pm1001pcMonupRmonPacketsCntValuePortn,'pm1001pcMonupRmonPacketsCntErrorPortn':pm1001pcMonupRmonPacketsCntErrorPortn,'pm1001pcMonupRmonPacketsCntOverloadPortn':pm1001pcMonupRmonPacketsCntOverloadPortn,'pm1001pcMonupRmonBroadcastCntTable':pm1001pcMonupRmonBroadcastCntTable,'pm1001pcMonupRmonBroadcastCntEntry':pm1001pcMonupRmonBroadcastCntEntry,_q:pm1001pcMonupRmonBroadcastCntIndex,'pm1001pcMonupRmonBroadcastCntValuePortn':pm1001pcMonupRmonBroadcastCntValuePortn,'pm1001pcMonupRmonBroadcastCntErrorPortn':pm1001pcMonupRmonBroadcastCntErrorPortn,'pm1001pcMonupRmonBroadcastCntOverloadPortn':pm1001pcMonupRmonBroadcastCntOverloadPortn,'pm1001pcMonupRmonMulticastCntTable':pm1001pcMonupRmonMulticastCntTable,'pm1001pcMonupRmonMulticastCntEntry':pm1001pcMonupRmonMulticastCntEntry,_r:pm1001pcMonupRmonMulticastCntIndex,'pm1001pcMonupRmonMulticastCntValuePortn':pm1001pcMonupRmonMulticastCntValuePortn,'pm1001pcMonupRmonMulticastCntErrorPortn':pm1001pcMonupRmonMulticastCntErrorPortn,'pm1001pcMonupRmonMulticastCntOverloadPortn':pm1001pcMonupRmonMulticastCntOverloadPortn,'pm1001pcMonupRmonTimerCntTable':pm1001pcMonupRmonTimerCntTable,'pm1001pcMonupRmonTimerCntEntry':pm1001pcMonupRmonTimerCntEntry,_s:pm1001pcMonupRmonTimerCntIndex,'pm1001pcMonupRmonTimerCntValuePortn':pm1001pcMonupRmonTimerCntValuePortn,'pm1001pcMonupRmonTimerCntErrorPortn':pm1001pcMonupRmonTimerCntErrorPortn,'pm1001pcMonupRmonTimerCntOverloadPortn':pm1001pcMonupRmonTimerCntOverloadPortn,'pm1001pcMonupRmonPauseFrameCntTable':pm1001pcMonupRmonPauseFrameCntTable,'pm1001pcMonupRmonPauseFrameCntEntry':pm1001pcMonupRmonPauseFrameCntEntry,_t:pm1001pcMonupRmonPauseFrameCntIndex,'pm1001pcMonupRmonPauseFrameCntValuePortn':pm1001pcMonupRmonPauseFrameCntValuePortn,'pm1001pcMonupRmonPauseFrameCntErrorPortn':pm1001pcMonupRmonPauseFrameCntErrorPortn,'pm1001pcMonupRmonPauseFrameCntOverloadPortn':pm1001pcMonupRmonPauseFrameCntOverloadPortn,'pm1001pcMonupRmonDropFrameCntTable':pm1001pcMonupRmonDropFrameCntTable,'pm1001pcMonupRmonDropFrameCntEntry':pm1001pcMonupRmonDropFrameCntEntry,_u:pm1001pcMonupRmonDropFrameCntIndex,'pm1001pcMonupRmonDropFrameCntValuePortn':pm1001pcMonupRmonDropFrameCntValuePortn,'pm1001pcMonupRmonDropFrameCntErrorPortn':pm1001pcMonupRmonDropFrameCntErrorPortn,'pm1001pcMonupRmonDropFrameCntOverloadPortn':pm1001pcMonupRmonDropFrameCntOverloadPortn,'pm1001pcMonupRmonBitsCntTable':pm1001pcMonupRmonBitsCntTable,'pm1001pcMonupRmonBitsCntEntry':pm1001pcMonupRmonBitsCntEntry,_v:pm1001pcMonupRmonBitsCntIndex,'pm1001pcMonupRmonBitsCntValuePortn':pm1001pcMonupRmonBitsCntValuePortn,'pm1001pcMonupRmonBitsCntErrorPortn':pm1001pcMonupRmonBitsCntErrorPortn,'pm1001pcMonupRmonBitsCntOverloadPortn':pm1001pcMonupRmonBitsCntOverloadPortn,'pm1001pcMondwRmonByteCntTable':pm1001pcMondwRmonByteCntTable,'pm1001pcMondwRmonByteCntEntry':pm1001pcMondwRmonByteCntEntry,_w:pm1001pcMondwRmonByteCntIndex,'pm1001pcMondwRmonByteCntValuePortn':pm1001pcMondwRmonByteCntValuePortn,'pm1001pcMondwRmonByteCntErrorPortn':pm1001pcMondwRmonByteCntErrorPortn,'pm1001pcMondwRmonByteCntOverloadPortn':pm1001pcMondwRmonByteCntOverloadPortn,'pm1001pcMondwRmonCrcErrorCntTable':pm1001pcMondwRmonCrcErrorCntTable,'pm1001pcMondwRmonCrcErrorCntEntry':pm1001pcMondwRmonCrcErrorCntEntry,_x:pm1001pcMondwRmonCrcErrorCntIndex,'pm1001pcMondwRmonCrcErrorCntValuePortn':pm1001pcMondwRmonCrcErrorCntValuePortn,'pm1001pcMondwRmonCrcErrorCntErrorPortn':pm1001pcMondwRmonCrcErrorCntErrorPortn,'pm1001pcMondwRmonCrcErrorCntOverloadPortn':pm1001pcMondwRmonCrcErrorCntOverloadPortn,'pm1001pcMondwRmonPacketsCntTable':pm1001pcMondwRmonPacketsCntTable,'pm1001pcMondwRmonPacketsCntEntry':pm1001pcMondwRmonPacketsCntEntry,_y:pm1001pcMondwRmonPacketsCntIndex,'pm1001pcMondwRmonPacketsCntValuePortn':pm1001pcMondwRmonPacketsCntValuePortn,'pm1001pcMondwRmonPacketsCntErrorPortn':pm1001pcMondwRmonPacketsCntErrorPortn,'pm1001pcMondwRmonPacketsCntOverloadPortn':pm1001pcMondwRmonPacketsCntOverloadPortn,'pm1001pcMondwRmonBroadcastCntTable':pm1001pcMondwRmonBroadcastCntTable,'pm1001pcMondwRmonBroadcastCntEntry':pm1001pcMondwRmonBroadcastCntEntry,_z:pm1001pcMondwRmonBroadcastCntIndex,'pm1001pcMondwRmonBroadcastCntValuePortn':pm1001pcMondwRmonBroadcastCntValuePortn,'pm1001pcMondwRmonBroadcastCntErrorPortn':pm1001pcMondwRmonBroadcastCntErrorPortn,'pm1001pcMondwRmonBroadcastCntOverloadPortn':pm1001pcMondwRmonBroadcastCntOverloadPortn,'pm1001pcMondwRmonMulticastCntTable':pm1001pcMondwRmonMulticastCntTable,'pm1001pcMondwRmonMulticastCntEntry':pm1001pcMondwRmonMulticastCntEntry,_A0:pm1001pcMondwRmonMulticastCntIndex,'pm1001pcMondwRmonMulticastCntValuePortn':pm1001pcMondwRmonMulticastCntValuePortn,'pm1001pcMondwRmonMulticastCntErrorPortn':pm1001pcMondwRmonMulticastCntErrorPortn,'pm1001pcMondwRmonMulticastCntOverloadPortn':pm1001pcMondwRmonMulticastCntOverloadPortn,'pm1001pcMondwRmonPauseFrameCntTable':pm1001pcMondwRmonPauseFrameCntTable,'pm1001pcMondwRmonPauseFrameCntEntry':pm1001pcMondwRmonPauseFrameCntEntry,_A1:pm1001pcMondwRmonPauseFrameCntIndex,'pm1001pcMondwRmonPauseFrameCntValuePortn':pm1001pcMondwRmonPauseFrameCntValuePortn,'pm1001pcMondwRmonPauseFrameCntErrorPortn':pm1001pcMondwRmonPauseFrameCntErrorPortn,'pm1001pcMondwRmonPauseFrameCntOverloadPortn':pm1001pcMondwRmonPauseFrameCntOverloadPortn,'pm1001pcMondwRmonTimerCntTable':pm1001pcMondwRmonTimerCntTable,'pm1001pcMondwRmonTimerCntEntry':pm1001pcMondwRmonTimerCntEntry,_A2:pm1001pcMondwRmonTimerCntIndex,'pm1001pcMondwRmonTimerCntValuePortn':pm1001pcMondwRmonTimerCntValuePortn,'pm1001pcMondwRmonTimerCntErrorPortn':pm1001pcMondwRmonTimerCntErrorPortn,'pm1001pcMondwRmonTimerCntOverloadPortn':pm1001pcMondwRmonTimerCntOverloadPortn,'pm1001pcMondwRmonBitsCntTable':pm1001pcMondwRmonBitsCntTable,'pm1001pcMondwRmonBitsCntEntry':pm1001pcMondwRmonBitsCntEntry,_A3:pm1001pcMondwRmonBitsCntIndex,'pm1001pcMondwRmonBitsCntValuePortn':pm1001pcMondwRmonBitsCntValuePortn,'pm1001pcMondwRmonBitsCntErrorPortn':pm1001pcMondwRmonBitsCntErrorPortn,'pm1001pcMondwRmonBitsCntOverloadPortn':pm1001pcMondwRmonBitsCntOverloadPortn,'pm1001pcMonupRmonByteCntSTable':pm1001pcMonupRmonByteCntSTable,'pm1001pcMonupRmonByteCntSEntry':pm1001pcMonupRmonByteCntSEntry,_A4:pm1001pcMonupRmonByteCntSIndex,'pm1001pcMonupRmonByteCntSValuePortn':pm1001pcMonupRmonByteCntSValuePortn,'pm1001pcMonupRmonByteCntSErrorPortn':pm1001pcMonupRmonByteCntSErrorPortn,'pm1001pcMonupRmonByteCntSOverloadPortn':pm1001pcMonupRmonByteCntSOverloadPortn,'pm1001pcMonupRmonCrcErrorCntSTable':pm1001pcMonupRmonCrcErrorCntSTable,'pm1001pcMonupRmonCrcErrorCntSEntry':pm1001pcMonupRmonCrcErrorCntSEntry,_A5:pm1001pcMonupRmonCrcErrorCntSIndex,'pm1001pcMonupRmonCrcErrorCntSValuePortn':pm1001pcMonupRmonCrcErrorCntSValuePortn,'pm1001pcMonupRmonCrcErrorCntSErrorPortn':pm1001pcMonupRmonCrcErrorCntSErrorPortn,'pm1001pcMonupRmonCrcErrorCntSOverloadPortn':pm1001pcMonupRmonCrcErrorCntSOverloadPortn,'pm1001pcMonupRmonPacketsCntSTable':pm1001pcMonupRmonPacketsCntSTable,'pm1001pcMonupRmonPacketsCntSEntry':pm1001pcMonupRmonPacketsCntSEntry,_A6:pm1001pcMonupRmonPacketsCntSIndex,'pm1001pcMonupRmonPacketsCntSValuePortn':pm1001pcMonupRmonPacketsCntSValuePortn,'pm1001pcMonupRmonPacketsCntSErrorPortn':pm1001pcMonupRmonPacketsCntSErrorPortn,'pm1001pcMonupRmonPacketsCntSOverloadPortn':pm1001pcMonupRmonPacketsCntSOverloadPortn,'pm1001pcMonupRmonBroadcastCntSTable':pm1001pcMonupRmonBroadcastCntSTable,'pm1001pcMonupRmonBroadcastCntSEntry':pm1001pcMonupRmonBroadcastCntSEntry,_A7:pm1001pcMonupRmonBroadcastCntSIndex,'pm1001pcMonupRmonBroadcastCntSValuePortn':pm1001pcMonupRmonBroadcastCntSValuePortn,'pm1001pcMonupRmonBroadcastCntSErrorPortn':pm1001pcMonupRmonBroadcastCntSErrorPortn,'pm1001pcMonupRmonBroadcastCntSOverloadPortn':pm1001pcMonupRmonBroadcastCntSOverloadPortn,'pm1001pcMonupRmonMulticastCntSTable':pm1001pcMonupRmonMulticastCntSTable,'pm1001pcMonupRmonMulticastCntSEntry':pm1001pcMonupRmonMulticastCntSEntry,_A8:pm1001pcMonupRmonMulticastCntSIndex,'pm1001pcMonupRmonMulticastCntSValuePortn':pm1001pcMonupRmonMulticastCntSValuePortn,'pm1001pcMonupRmonMulticastCntSErrorPortn':pm1001pcMonupRmonMulticastCntSErrorPortn,'pm1001pcMonupRmonMulticastCntSOverloadPortn':pm1001pcMonupRmonMulticastCntSOverloadPortn,'pm1001pcMonupRmonPauseFrameCntSTable':pm1001pcMonupRmonPauseFrameCntSTable,'pm1001pcMonupRmonPauseFrameCntSEntry':pm1001pcMonupRmonPauseFrameCntSEntry,_A9:pm1001pcMonupRmonPauseFrameCntSIndex,'pm1001pcMonupRmonPauseFrameCntSValuePortn':pm1001pcMonupRmonPauseFrameCntSValuePortn,'pm1001pcMonupRmonPauseFrameCntSErrorPortn':pm1001pcMonupRmonPauseFrameCntSErrorPortn,'pm1001pcMonupRmonPauseFrameCntSOverloadPortn':pm1001pcMonupRmonPauseFrameCntSOverloadPortn,'pm1001pcMonupRmonDropFrameCntSTable':pm1001pcMonupRmonDropFrameCntSTable,'pm1001pcMonupRmonDropFrameCntSEntry':pm1001pcMonupRmonDropFrameCntSEntry,_AA:pm1001pcMonupRmonDropFrameCntSIndex,'pm1001pcMonupRmonDropFrameCntSValuePortn':pm1001pcMonupRmonDropFrameCntSValuePortn,'pm1001pcMonupRmonDropFrameCntSErrorPortn':pm1001pcMonupRmonDropFrameCntSErrorPortn,'pm1001pcMonupRmonDropFrameCntSOverloadPortn':pm1001pcMonupRmonDropFrameCntSOverloadPortn,'pm1001pcMonupRmonBitsCntSTable':pm1001pcMonupRmonBitsCntSTable,'pm1001pcMonupRmonBitsCntSEntry':pm1001pcMonupRmonBitsCntSEntry,_AB:pm1001pcMonupRmonBitsCntSIndex,'pm1001pcMonupRmonBitsCntSValuePortn':pm1001pcMonupRmonBitsCntSValuePortn,'pm1001pcMonupRmonBitsCntSErrorPortn':pm1001pcMonupRmonBitsCntSErrorPortn,'pm1001pcMonupRmonBitsCntSOverloadPortn':pm1001pcMonupRmonBitsCntSOverloadPortn,'pm1001pcMondwRmonByteCntSTable':pm1001pcMondwRmonByteCntSTable,'pm1001pcMondwRmonByteCntSEntry':pm1001pcMondwRmonByteCntSEntry,_AC:pm1001pcMondwRmonByteCntSIndex,'pm1001pcMondwRmonByteCntSValuePortn':pm1001pcMondwRmonByteCntSValuePortn,'pm1001pcMondwRmonByteCntSErrorPortn':pm1001pcMondwRmonByteCntSErrorPortn,'pm1001pcMondwRmonByteCntSOverloadPortn':pm1001pcMondwRmonByteCntSOverloadPortn,'pm1001pcMondwRmonCrcErrorCntSTable':pm1001pcMondwRmonCrcErrorCntSTable,'pm1001pcMondwRmonCrcErrorCntSEntry':pm1001pcMondwRmonCrcErrorCntSEntry,_AD:pm1001pcMondwRmonCrcErrorCntSIndex,'pm1001pcMondwRmonCrcErrorCntSValuePortn':pm1001pcMondwRmonCrcErrorCntSValuePortn,'pm1001pcMondwRmonCrcErrorCntSErrorPortn':pm1001pcMondwRmonCrcErrorCntSErrorPortn,'pm1001pcMondwRmonCrcErrorCntSOverloadPortn':pm1001pcMondwRmonCrcErrorCntSOverloadPortn,'pm1001pcMondwRmonPacketsCntSTable':pm1001pcMondwRmonPacketsCntSTable,'pm1001pcMondwRmonPacketsCntSEntry':pm1001pcMondwRmonPacketsCntSEntry,_AE:pm1001pcMondwRmonPacketsCntSIndex,'pm1001pcMondwRmonPacketsCntSValuePortn':pm1001pcMondwRmonPacketsCntSValuePortn,'pm1001pcMondwRmonPacketsCntSErrorPortn':pm1001pcMondwRmonPacketsCntSErrorPortn,'pm1001pcMondwRmonPacketsCntSOverloadPortn':pm1001pcMondwRmonPacketsCntSOverloadPortn,'pm1001pcMondwRmonBroadcastCntSTable':pm1001pcMondwRmonBroadcastCntSTable,'pm1001pcMondwRmonBroadcastCntSEntry':pm1001pcMondwRmonBroadcastCntSEntry,_AF:pm1001pcMondwRmonBroadcastCntSIndex,'pm1001pcMondwRmonBroadcastCntSValuePortn':pm1001pcMondwRmonBroadcastCntSValuePortn,'pm1001pcMondwRmonBroadcastCntSErrorPortn':pm1001pcMondwRmonBroadcastCntSErrorPortn,'pm1001pcMondwRmonBroadcastCntSOverloadPortn':pm1001pcMondwRmonBroadcastCntSOverloadPortn,'pm1001pcMondwRmonMulticastCntSTable':pm1001pcMondwRmonMulticastCntSTable,'pm1001pcMondwRmonMulticastCntSEntry':pm1001pcMondwRmonMulticastCntSEntry,_AG:pm1001pcMondwRmonMulticastCntSIndex,'pm1001pcMondwRmonMulticastCntSValuePortn':pm1001pcMondwRmonMulticastCntSValuePortn,'pm1001pcMondwRmonMulticastCntSErrorPortn':pm1001pcMondwRmonMulticastCntSErrorPortn,'pm1001pcMondwRmonMulticastCntSOverloadPortn':pm1001pcMondwRmonMulticastCntSOverloadPortn,'pm1001pcMondwRmonPauseFrameCntSTable':pm1001pcMondwRmonPauseFrameCntSTable,'pm1001pcMondwRmonPauseFrameCntSEntry':pm1001pcMondwRmonPauseFrameCntSEntry,_AH:pm1001pcMondwRmonPauseFrameCntSIndex,'pm1001pcMondwRmonPauseFrameCntSValuePortn':pm1001pcMondwRmonPauseFrameCntSValuePortn,'pm1001pcMondwRmonPauseFrameCntSErrorPortn':pm1001pcMondwRmonPauseFrameCntSErrorPortn,'pm1001pcMondwRmonPauseFrameCntSOverloadPortn':pm1001pcMondwRmonPauseFrameCntSOverloadPortn,'pm1001pcMondwRmonBitsCntSTable':pm1001pcMondwRmonBitsCntSTable,'pm1001pcMondwRmonBitsCntSEntry':pm1001pcMondwRmonBitsCntSEntry,_AI:pm1001pcMondwRmonBitsCntSIndex,'pm1001pcMondwRmonBitsCntSValuePortn':pm1001pcMondwRmonBitsCntSValuePortn,'pm1001pcMondwRmonBitsCntSErrorPortn':pm1001pcMondwRmonBitsCntSErrorPortn,'pm1001pcMondwRmonBitsCntSOverloadPortn':pm1001pcMondwRmonBitsCntSOverloadPortn,'pm1001pcRmonLine':pm1001pcRmonLine,'pm1001pcConfig':pm1001pcConfig,'pm1001pcCfgAccessCAisCsf':pm1001pcCfgAccessCAisCsf,'pm1001pcCfgClientcaiscsfTable':pm1001pcCfgClientcaiscsfTable,'pm1001pcCfgClientcaiscsfEntry':pm1001pcCfgClientcaiscsfEntry,_AJ:pm1001pcCfgClientcaiscsfIndex,'pm1001pcCfgCAisModePortn':pm1001pcCfgCAisModePortn,'pm1001pcCfgUpAccessioAlmPortn':pm1001pcCfgUpAccessioAlmPortn,'pm1001pcCfgUpMapperDeAlmPortn':pm1001pcCfgUpMapperDeAlmPortn,'pm1001pcCfgDownAccessioAlmPortn':pm1001pcCfgDownAccessioAlmPortn,'pm1001pcCfgDownMapperDeAlmPortn':pm1001pcCfgDownMapperDeAlmPortn,'pm1001pcCfgDownDfrmAlmPortn':pm1001pcCfgDownDfrmAlmPortn,'pm1001pcCfgDownLineSyncAlarmsPortn':pm1001pcCfgDownLineSyncAlarmsPortn,'pm1001pcCfgStartup':pm1001pcCfgStartup,'pm1001pcCfgClientStartupTable':pm1001pcCfgClientStartupTable,'pm1001pcCfgClientStartupEntry':pm1001pcCfgClientStartupEntry,_AK:pm1001pcCfgClientStartupIndex,'pm1001pcCfgSystConfPortPortn':pm1001pcCfgSystConfPortPortn,'pm1001pcCfgNetConfPortPortn':pm1001pcCfgNetConfPortPortn,'pm1001pcCfgFiberLengthPortn':pm1001pcCfgFiberLengthPortn,'pm1001pctablelineStartup':pm1001pctablelineStartup,'pm1001pcCfgsynthTransLine':pm1001pcCfgsynthTransLine,'pm1001pcCfglineOptions1':pm1001pcCfglineOptions1,'pm1001pcCfgXfpTable':pm1001pcCfgXfpTable,'pm1001pcCfgXfpEntry':pm1001pcCfgXfpEntry,_AL:pm1001pcCfgXfpIndex,'pm1001pcCfgSystConfXfpPortn':pm1001pcCfgSystConfXfpPortn,'pm1001pcCfgDataRateConfXfpPortn':pm1001pcCfgDataRateConfXfpPortn,'pm1001pcCfgLabels':pm1001pcCfgLabels,'pm1001pcCfgLabelclientTable':pm1001pcCfgLabelclientTable,'pm1001pcCfgLabelclientEntry':pm1001pcCfgLabelclientEntry,_AM:pm1001pcCfgLabelclientIndex,'pm1001pcCfgLabelclientPortn':pm1001pcCfgLabelclientPortn,'pm1001pcCfgLabellineTable':pm1001pcCfgLabellineTable,'pm1001pcCfgLabellineEntry':pm1001pcCfgLabellineEntry,_AN:pm1001pcCfgLabellineIndex,'pm1001pcCfgLabellinePortn':pm1001pcCfgLabellinePortn,'pm1001pcCfgWriteConfiguration':pm1001pcCfgWriteConfiguration,'pm1001pctraps':pm1001pctraps,_G:pm1001pctrapBoardNumber,'pm1001pcLineTrapNotUrgentGoesOn':pm1001pcLineTrapNotUrgentGoesOn,'pm1001pcLineTrapNotUrgentGoesOff':pm1001pcLineTrapNotUrgentGoesOff,'pm1001pcLineTrapUrgentGoesOn':pm1001pcLineTrapUrgentGoesOn,'pm1001pcLineTrapUrgentGoesOff':pm1001pcLineTrapUrgentGoesOff,'pm1001pcLineTrapCritGoesOn':pm1001pcLineTrapCritGoesOn,'pm1001pcLineTrapCritGoesOff':pm1001pcLineTrapCritGoesOff,'pm1001pcClientTrapNotUrgentGoesOn':pm1001pcClientTrapNotUrgentGoesOn,'pm1001pcClientTrapNotUrgentGoesOff':pm1001pcClientTrapNotUrgentGoesOff,'pm1001pcClientTrapUrgentGoesOn':pm1001pcClientTrapUrgentGoesOn,'pm1001pcClientTrapUrgentGoesOff':pm1001pcClientTrapUrgentGoesOff,'pm1001pcClientTrapCritGoesOn':pm1001pcClientTrapCritGoesOn,'pm1001pcClientTrapCritGoesOff':pm1001pcClientTrapCritGoesOff,'pm1001pcPowerTrapUrgentGoesOn':pm1001pcPowerTrapUrgentGoesOn,'pm1001pcPowerTrapUrgentGoesOff':pm1001pcPowerTrapUrgentGoesOff})