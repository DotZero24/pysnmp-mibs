_AN='pm254dMonupRmonMulticastCntIndex'
_AM='pm254dMonupRmonBroadcastCntIndex'
_AL='pm254dMonupRmonPacketsCntIndex'
_AK='pm254dMonupRmonCrcErrorCntIndex'
_AJ='pm254dMonupRmonByteCntIndex'
_AI='pm254dCfgLabellineIndex'
_AH='pm254dCfgLabelclientIndex'
_AG='pm254dCfgClientStartupIndex'
_AF='pm254dCfgClientcaiscsfIndex'
_AE='pm254dRinvLineIndex'
_AD='pm254dRinvClientIndex'
_AC='pm254dCtrldccEnableIndex'
_AB='pm254dCtrllineSfpOnOffCtrlIndex'
_AA='pm254dCtrllineLoopTransceiverIndex'
_A9='pm254dCtrllineAccessLoopIndex'
_A8='pm254dCtrllineOosModeIndex'
_A7='pm254dCtrllineUpK2Index'
_A6='pm254dCtrllineUpK1Index'
_A5='pm254dCtrllineUpS1Index'
_A4='pm254dCtrlProtocolIndex'
_A3='pm254dCtrlclientAccessTermLoopIndex'
_A2='pm254dCtrlclientCaisDwInsIndex'
_A1='pm254dCtrlclientCsfUpInsIndex'
_A0='pm254dCtrlclientSfpOnOffCtrlIndex'
_z='pm254dCtrlclientOosModeIndex'
_y='pm254dCtrlclientAccessLoopIndex'
_x='pm254dCntlineDfrmTimCntIndex'
_w='pm254dCntlineDfrmB1ErrCntIndex'
_v='pm254dCntclientDwTimCntIndex'
_u='pm254dCntclientDwCbipCntIndex'
_t='pm254dCntclientUpTimCntIndex'
_s='pm254dCntclientUpDispErrCntIndex'
_r='pm254dCntclientUpRaInsCntIndex'
_q='pm254dCntclientUpRaRemCntIndex'
_p='pm254dMesrlineRxpwrMeasIndex'
_o='pm254dMesrlineTxpwrMeasIndex'
_n='pm254dMesrlineBiasMeasIndex'
_m='pm254dMesrlineVoltMeasIndex'
_l='pm254dMesrlineTempMeasIndex'
_k='pm254dMesrclientRxpwrMeasIndex'
_j='pm254dMesrclientTxpwrMeasIndex'
_i='pm254dMesrclientBiasMeasIndex'
_h='pm254dMesrclientVoltMeasIndex'
_g='pm254dMesrclientTempMeasIndex'
_f='pm254dAlmlineIoAlmIndex'
_e='pm254dAlmlineDfrmAlmIndex'
_d='pm254dAlmsynthAlmLineIndex'
_c='pm254dAlmlineSfpAlaDdmIndex'
_b='pm254dAlmlineSfpWarnDdmIndex'
_a='pm254dAlmlineDownK2Index'
_Z='pm254dAlmlineDownK1Index'
_Y='pm254dAlmlineDownS1Index'
_X='pm254dAlmclientMapperDeAlmIndex'
_W='pm254dAlmaccessioAlmIndex'
_V='pm254dAlmsynthAlmClientIndex'
_U='pm254dAlmclientSfpAlmDdmIndex'
_T='pm254dAlmclientSfpWarnDdmIndex'
_S='pm254dAlmClientHwFailAccPortn'
_R='pm254dAlmClientFailAccPortn'
_Q='pm254dAlmClientSfpDdmAlmPortn'
_P='pm254dAlmClientSfpDdmWarningPortn'
_O='pm254dAlmLineHwFailPortn'
_N='pm254dAlmLineFailPortn'
_M='pm254dAlmLineDdmAlmPortn'
_L='pm254dAlmLineDdmWarningPortn'
_K='deprecated'
_J='DisplayString'
_I='pm254dTrapPortNumber'
_H='pm254dTrapLineNumber'
_G='pm254dTrapBoardNumber'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='EKINOPS-Pm254d-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
modulePm254d=ModuleIdentity((1,3,6,1,4,1,20044,17))
if mibBuilder.loadTexts:modulePm254d.setRevisions(('2006-11-08 00:00','2007-08-30 00:00','2008-01-22 00:00','2009-04-10 00:00','2009-07-20 00:00','2009-10-07 00:00','2010-03-01 00:00','2010-11-05 00:00','2012-07-03 00:00','2013-07-05 00:00','2014-03-28 00:00','2015-01-20 00:00','2016-05-20 00:00'))
_Pm254dalarms_ObjectIdentity=ObjectIdentity
pm254dalarms=_Pm254dalarms_ObjectIdentity((1,3,6,1,4,1,20044,17,2))
_Pm254dAlmOther_ObjectIdentity=ObjectIdentity
pm254dAlmOther=_Pm254dAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1))
_Pm254dAlmOtherNurg_ObjectIdentity=ObjectIdentity
pm254dAlmOtherNurg=_Pm254dAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,1))
_Pm254dAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm254dAlmsynthAlm0=_Pm254dAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,1,0))
_Pm254dAlmModGlobFail_Type=EkiOnOff
_Pm254dAlmModGlobFail_Object=MibScalar
pm254dAlmModGlobFail=_Pm254dAlmModGlobFail_Object((1,3,6,1,4,1,20044,17,2,1,1,0,9),_Pm254dAlmModGlobFail_Type())
pm254dAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmModGlobFail.setStatus(_A)
_Pm254dAlmDefFuseA_Type=EkiOnOff
_Pm254dAlmDefFuseA_Object=MibScalar
pm254dAlmDefFuseA=_Pm254dAlmDefFuseA_Object((1,3,6,1,4,1,20044,17,2,1,1,0,15),_Pm254dAlmDefFuseA_Type())
pm254dAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmDefFuseA.setStatus(_A)
_Pm254dAlmDefFuseB_Type=EkiOnOff
_Pm254dAlmDefFuseB_Object=MibScalar
pm254dAlmDefFuseB=_Pm254dAlmDefFuseB_Object((1,3,6,1,4,1,20044,17,2,1,1,0,16),_Pm254dAlmDefFuseB_Type())
pm254dAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmDefFuseB.setStatus(_A)
_Pm254dAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm254dAlmsynthAlm2=_Pm254dAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,1,2))
_Pm254dAlmConfTableSave_Type=EkiOnOff
_Pm254dAlmConfTableSave_Object=MibScalar
pm254dAlmConfTableSave=_Pm254dAlmConfTableSave_Object((1,3,6,1,4,1,20044,17,2,1,1,2,1),_Pm254dAlmConfTableSave_Type())
pm254dAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmConfTableSave.setStatus(_A)
_Pm254dAlmInvUpload_Type=EkiOnOff
_Pm254dAlmInvUpload_Object=MibScalar
pm254dAlmInvUpload=_Pm254dAlmInvUpload_Object((1,3,6,1,4,1,20044,17,2,1,1,2,2),_Pm254dAlmInvUpload_Type())
pm254dAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmInvUpload.setStatus(_A)
_Pm254dAlmConfTableLoad_Type=EkiOnOff
_Pm254dAlmConfTableLoad_Object=MibScalar
pm254dAlmConfTableLoad=_Pm254dAlmConfTableLoad_Object((1,3,6,1,4,1,20044,17,2,1,1,2,3),_Pm254dAlmConfTableLoad_Type())
pm254dAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmConfTableLoad.setStatus(_A)
_Pm254dAlmCorrelatOff_Type=EkiOnOff
_Pm254dAlmCorrelatOff_Object=MibScalar
pm254dAlmCorrelatOff=_Pm254dAlmCorrelatOff_Object((1,3,6,1,4,1,20044,17,2,1,1,2,4),_Pm254dAlmCorrelatOff_Type())
pm254dAlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmCorrelatOff.setStatus(_A)
_Pm254dAlmMaintenanceOn_Type=EkiOnOff
_Pm254dAlmMaintenanceOn_Object=MibScalar
pm254dAlmMaintenanceOn=_Pm254dAlmMaintenanceOn_Object((1,3,6,1,4,1,20044,17,2,1,1,2,5),_Pm254dAlmMaintenanceOn_Type())
pm254dAlmMaintenanceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmMaintenanceOn.setStatus(_A)
_Pm254dAlmOtherUrg_ObjectIdentity=ObjectIdentity
pm254dAlmOtherUrg=_Pm254dAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,2))
_Pm254dAlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pm254dAlmmodInitFailLevel2=_Pm254dAlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,2,194))
_Pm254dAlmLedFail_Type=EkiOnOff
_Pm254dAlmLedFail_Object=MibScalar
pm254dAlmLedFail=_Pm254dAlmLedFail_Object((1,3,6,1,4,1,20044,17,2,1,2,194,1),_Pm254dAlmLedFail_Type())
pm254dAlmLedFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLedFail.setStatus(_A)
_Pm254dAlmNextColdBootForced_Type=EkiOnOff
_Pm254dAlmNextColdBootForced_Object=MibScalar
pm254dAlmNextColdBootForced=_Pm254dAlmNextColdBootForced_Object((1,3,6,1,4,1,20044,17,2,1,2,194,2),_Pm254dAlmNextColdBootForced_Type())
pm254dAlmNextColdBootForced.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmNextColdBootForced.setStatus(_A)
_Pm254dAlmBootUndone_Type=EkiOnOff
_Pm254dAlmBootUndone_Object=MibScalar
pm254dAlmBootUndone=_Pm254dAlmBootUndone_Object((1,3,6,1,4,1,20044,17,2,1,2,194,3),_Pm254dAlmBootUndone_Type())
pm254dAlmBootUndone.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmBootUndone.setStatus(_A)
_Pm254dAlmResetHwInitFail_Type=EkiOnOff
_Pm254dAlmResetHwInitFail_Object=MibScalar
pm254dAlmResetHwInitFail=_Pm254dAlmResetHwInitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,194,4),_Pm254dAlmResetHwInitFail_Type())
pm254dAlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmResetHwInitFail.setStatus(_A)
_Pm254dAlmSwInitFail_Type=EkiOnOff
_Pm254dAlmSwInitFail_Object=MibScalar
pm254dAlmSwInitFail=_Pm254dAlmSwInitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,194,5),_Pm254dAlmSwInitFail_Type())
pm254dAlmSwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmSwInitFail.setStatus(_A)
_Pm254dAlmmodInitFailLevel3_ObjectIdentity=ObjectIdentity
pm254dAlmmodInitFailLevel3=_Pm254dAlmmodInitFailLevel3_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,2,195))
_Pm254dAlmGwIdentFail_Type=EkiOnOff
_Pm254dAlmGwIdentFail_Object=MibScalar
pm254dAlmGwIdentFail=_Pm254dAlmGwIdentFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,1),_Pm254dAlmGwIdentFail_Type())
pm254dAlmGwIdentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmGwIdentFail.setStatus(_A)
_Pm254dAlmObmTypeReadFail_Type=EkiOnOff
_Pm254dAlmObmTypeReadFail_Object=MibScalar
pm254dAlmObmTypeReadFail=_Pm254dAlmObmTypeReadFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,2),_Pm254dAlmObmTypeReadFail_Type())
pm254dAlmObmTypeReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmObmTypeReadFail.setStatus(_A)
_Pm254dAlmInitModuleFail_Type=EkiOnOff
_Pm254dAlmInitModuleFail_Object=MibScalar
pm254dAlmInitModuleFail=_Pm254dAlmInitModuleFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,3),_Pm254dAlmInitModuleFail_Type())
pm254dAlmInitModuleFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmInitModuleFail.setStatus(_A)
_Pm254dAlmSfp1InitFail_Type=EkiOnOff
_Pm254dAlmSfp1InitFail_Object=MibScalar
pm254dAlmSfp1InitFail=_Pm254dAlmSfp1InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,5),_Pm254dAlmSfp1InitFail_Type())
pm254dAlmSfp1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmSfp1InitFail.setStatus(_A)
_Pm254dAlmSfp2InitFail_Type=EkiOnOff
_Pm254dAlmSfp2InitFail_Object=MibScalar
pm254dAlmSfp2InitFail=_Pm254dAlmSfp2InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,6),_Pm254dAlmSfp2InitFail_Type())
pm254dAlmSfp2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmSfp2InitFail.setStatus(_A)
_Pm254dAlmLine1InitFail_Type=EkiOnOff
_Pm254dAlmLine1InitFail_Object=MibScalar
pm254dAlmLine1InitFail=_Pm254dAlmLine1InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,7),_Pm254dAlmLine1InitFail_Type())
pm254dAlmLine1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLine1InitFail.setStatus(_A)
_Pm254dAlmLine2InitFail_Type=EkiOnOff
_Pm254dAlmLine2InitFail_Object=MibScalar
pm254dAlmLine2InitFail=_Pm254dAlmLine2InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,8),_Pm254dAlmLine2InitFail_Type())
pm254dAlmLine2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLine2InitFail.setStatus(_A)
_Pm254dAlmClient1InitFail_Type=EkiOnOff
_Pm254dAlmClient1InitFail_Object=MibScalar
pm254dAlmClient1InitFail=_Pm254dAlmClient1InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,9),_Pm254dAlmClient1InitFail_Type())
pm254dAlmClient1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClient1InitFail.setStatus(_A)
_Pm254dAlmClient2InitFail_Type=EkiOnOff
_Pm254dAlmClient2InitFail_Object=MibScalar
pm254dAlmClient2InitFail=_Pm254dAlmClient2InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,10),_Pm254dAlmClient2InitFail_Type())
pm254dAlmClient2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClient2InitFail.setStatus(_A)
_Pm254dAlmClient3InitFail_Type=EkiOnOff
_Pm254dAlmClient3InitFail_Object=MibScalar
pm254dAlmClient3InitFail=_Pm254dAlmClient3InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,11),_Pm254dAlmClient3InitFail_Type())
pm254dAlmClient3InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClient3InitFail.setStatus(_A)
_Pm254dAlmClient4InitFail_Type=EkiOnOff
_Pm254dAlmClient4InitFail_Object=MibScalar
pm254dAlmClient4InitFail=_Pm254dAlmClient4InitFail_Object((1,3,6,1,4,1,20044,17,2,1,2,195,12),_Pm254dAlmClient4InitFail_Type())
pm254dAlmClient4InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClient4InitFail.setStatus(_A)
_Pm254dAlmOtherCrit_ObjectIdentity=ObjectIdentity
pm254dAlmOtherCrit=_Pm254dAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,17,2,1,3))
_Pm254dAlmPort_ObjectIdentity=ObjectIdentity
pm254dAlmPort=_Pm254dAlmPort_ObjectIdentity((1,3,6,1,4,1,20044,17,2,2))
_Pm254dAlmPortNurg_ObjectIdentity=ObjectIdentity
pm254dAlmPortNurg=_Pm254dAlmPortNurg_ObjectIdentity((1,3,6,1,4,1,20044,17,2,2,1))
_Pm254dAlmclientSfpWarnDdmTable_Object=MibTable
pm254dAlmclientSfpWarnDdmTable=_Pm254dAlmclientSfpWarnDdmTable_Object((1,3,6,1,4,1,20044,17,2,2,1,48))
if mibBuilder.loadTexts:pm254dAlmclientSfpWarnDdmTable.setStatus(_A)
_Pm254dAlmclientSfpWarnDdmEntry_Object=MibTableRow
pm254dAlmclientSfpWarnDdmEntry=_Pm254dAlmclientSfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1))
pm254dAlmclientSfpWarnDdmEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:pm254dAlmclientSfpWarnDdmEntry.setStatus(_A)
class _Pm254dAlmclientSfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmclientSfpWarnDdmIndex_Type.__name__=_D
_Pm254dAlmclientSfpWarnDdmIndex_Object=MibTableColumn
pm254dAlmclientSfpWarnDdmIndex=_Pm254dAlmclientSfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,1),_Pm254dAlmclientSfpWarnDdmIndex_Type())
pm254dAlmclientSfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmclientSfpWarnDdmIndex.setStatus(_A)
_Pm254dAlmClientTxPwLowWngPortn_Type=EkiOnOff
_Pm254dAlmClientTxPwLowWngPortn_Object=MibTableColumn
pm254dAlmClientTxPwLowWngPortn=_Pm254dAlmClientTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,2),_Pm254dAlmClientTxPwLowWngPortn_Type())
pm254dAlmClientTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxPwLowWngPortn.setStatus(_A)
_Pm254dAlmClientTxPwrHighWngPortn_Type=EkiOnOff
_Pm254dAlmClientTxPwrHighWngPortn_Object=MibTableColumn
pm254dAlmClientTxPwrHighWngPortn=_Pm254dAlmClientTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,3),_Pm254dAlmClientTxPwrHighWngPortn_Type())
pm254dAlmClientTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxPwrHighWngPortn.setStatus(_A)
_Pm254dAlmClientTxBiasLowWngPortn_Type=EkiOnOff
_Pm254dAlmClientTxBiasLowWngPortn_Object=MibTableColumn
pm254dAlmClientTxBiasLowWngPortn=_Pm254dAlmClientTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,4),_Pm254dAlmClientTxBiasLowWngPortn_Type())
pm254dAlmClientTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxBiasLowWngPortn.setStatus(_A)
_Pm254dAlmClientTxBiasHighWngPortn_Type=EkiOnOff
_Pm254dAlmClientTxBiasHighWngPortn_Object=MibTableColumn
pm254dAlmClientTxBiasHighWngPortn=_Pm254dAlmClientTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,5),_Pm254dAlmClientTxBiasHighWngPortn_Type())
pm254dAlmClientTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxBiasHighWngPortn.setStatus(_A)
_Pm254dAlmClientVccLowWngPortn_Type=EkiOnOff
_Pm254dAlmClientVccLowWngPortn_Object=MibTableColumn
pm254dAlmClientVccLowWngPortn=_Pm254dAlmClientVccLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,6),_Pm254dAlmClientVccLowWngPortn_Type())
pm254dAlmClientVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientVccLowWngPortn.setStatus(_A)
_Pm254dAlmClientVccHighWngPortn_Type=EkiOnOff
_Pm254dAlmClientVccHighWngPortn_Object=MibTableColumn
pm254dAlmClientVccHighWngPortn=_Pm254dAlmClientVccHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,7),_Pm254dAlmClientVccHighWngPortn_Type())
pm254dAlmClientVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientVccHighWngPortn.setStatus(_A)
_Pm254dAlmClientTempLowWngPortn_Type=EkiOnOff
_Pm254dAlmClientTempLowWngPortn_Object=MibTableColumn
pm254dAlmClientTempLowWngPortn=_Pm254dAlmClientTempLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,8),_Pm254dAlmClientTempLowWngPortn_Type())
pm254dAlmClientTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTempLowWngPortn.setStatus(_A)
_Pm254dAlmClientTempHighWngPortn_Type=EkiOnOff
_Pm254dAlmClientTempHighWngPortn_Object=MibTableColumn
pm254dAlmClientTempHighWngPortn=_Pm254dAlmClientTempHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,9),_Pm254dAlmClientTempHighWngPortn_Type())
pm254dAlmClientTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTempHighWngPortn.setStatus(_A)
_Pm254dAlmClientRxPwrLowWngPortn_Type=EkiOnOff
_Pm254dAlmClientRxPwrLowWngPortn_Object=MibTableColumn
pm254dAlmClientRxPwrLowWngPortn=_Pm254dAlmClientRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,16),_Pm254dAlmClientRxPwrLowWngPortn_Type())
pm254dAlmClientRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientRxPwrLowWngPortn.setStatus(_A)
_Pm254dAlmClientRxPwrHighWngPortn_Type=EkiOnOff
_Pm254dAlmClientRxPwrHighWngPortn_Object=MibTableColumn
pm254dAlmClientRxPwrHighWngPortn=_Pm254dAlmClientRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,2,1,48,1,17),_Pm254dAlmClientRxPwrHighWngPortn_Type())
pm254dAlmClientRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientRxPwrHighWngPortn.setStatus(_A)
_Pm254dAlmPortUrg_ObjectIdentity=ObjectIdentity
pm254dAlmPortUrg=_Pm254dAlmPortUrg_ObjectIdentity((1,3,6,1,4,1,20044,17,2,2,2))
_Pm254dAlmclientSfpAlmDdmTable_Object=MibTable
pm254dAlmclientSfpAlmDdmTable=_Pm254dAlmclientSfpAlmDdmTable_Object((1,3,6,1,4,1,20044,17,2,2,2,32))
if mibBuilder.loadTexts:pm254dAlmclientSfpAlmDdmTable.setStatus(_A)
_Pm254dAlmclientSfpAlmDdmEntry_Object=MibTableRow
pm254dAlmclientSfpAlmDdmEntry=_Pm254dAlmclientSfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1))
pm254dAlmclientSfpAlmDdmEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pm254dAlmclientSfpAlmDdmEntry.setStatus(_A)
class _Pm254dAlmclientSfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmclientSfpAlmDdmIndex_Type.__name__=_D
_Pm254dAlmclientSfpAlmDdmIndex_Object=MibTableColumn
pm254dAlmclientSfpAlmDdmIndex=_Pm254dAlmclientSfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,1),_Pm254dAlmclientSfpAlmDdmIndex_Type())
pm254dAlmclientSfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmclientSfpAlmDdmIndex.setStatus(_A)
_Pm254dAlmClientTxPwrLowAlaPortn_Type=EkiOnOff
_Pm254dAlmClientTxPwrLowAlaPortn_Object=MibTableColumn
pm254dAlmClientTxPwrLowAlaPortn=_Pm254dAlmClientTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,2),_Pm254dAlmClientTxPwrLowAlaPortn_Type())
pm254dAlmClientTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxPwrLowAlaPortn.setStatus(_A)
_Pm254dAlmClientTxPwrHighAlaPortn_Type=EkiOnOff
_Pm254dAlmClientTxPwrHighAlaPortn_Object=MibTableColumn
pm254dAlmClientTxPwrHighAlaPortn=_Pm254dAlmClientTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,3),_Pm254dAlmClientTxPwrHighAlaPortn_Type())
pm254dAlmClientTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxPwrHighAlaPortn.setStatus(_A)
_Pm254dAlmClientTxBiasLowAlaPortn_Type=EkiOnOff
_Pm254dAlmClientTxBiasLowAlaPortn_Object=MibTableColumn
pm254dAlmClientTxBiasLowAlaPortn=_Pm254dAlmClientTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,4),_Pm254dAlmClientTxBiasLowAlaPortn_Type())
pm254dAlmClientTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxBiasLowAlaPortn.setStatus(_A)
_Pm254dAlmClientTxBiasHighAlaPortn_Type=EkiOnOff
_Pm254dAlmClientTxBiasHighAlaPortn_Object=MibTableColumn
pm254dAlmClientTxBiasHighAlaPortn=_Pm254dAlmClientTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,5),_Pm254dAlmClientTxBiasHighAlaPortn_Type())
pm254dAlmClientTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTxBiasHighAlaPortn.setStatus(_A)
_Pm254dAlmClientVccLowAlaPortn_Type=EkiOnOff
_Pm254dAlmClientVccLowAlaPortn_Object=MibTableColumn
pm254dAlmClientVccLowAlaPortn=_Pm254dAlmClientVccLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,6),_Pm254dAlmClientVccLowAlaPortn_Type())
pm254dAlmClientVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientVccLowAlaPortn.setStatus(_A)
_Pm254dAlmClientVccHighAlaPortn_Type=EkiOnOff
_Pm254dAlmClientVccHighAlaPortn_Object=MibTableColumn
pm254dAlmClientVccHighAlaPortn=_Pm254dAlmClientVccHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,7),_Pm254dAlmClientVccHighAlaPortn_Type())
pm254dAlmClientVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientVccHighAlaPortn.setStatus(_A)
_Pm254dAlmClientTempLowAlaPortn_Type=EkiOnOff
_Pm254dAlmClientTempLowAlaPortn_Object=MibTableColumn
pm254dAlmClientTempLowAlaPortn=_Pm254dAlmClientTempLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,8),_Pm254dAlmClientTempLowAlaPortn_Type())
pm254dAlmClientTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTempLowAlaPortn.setStatus(_A)
_Pm254dAlmClientTempHighAlaPortn_Type=EkiOnOff
_Pm254dAlmClientTempHighAlaPortn_Object=MibTableColumn
pm254dAlmClientTempHighAlaPortn=_Pm254dAlmClientTempHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,9),_Pm254dAlmClientTempHighAlaPortn_Type())
pm254dAlmClientTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientTempHighAlaPortn.setStatus(_A)
_Pm254dAlmClientRxPwrLowAlaPortn_Type=EkiOnOff
_Pm254dAlmClientRxPwrLowAlaPortn_Object=MibTableColumn
pm254dAlmClientRxPwrLowAlaPortn=_Pm254dAlmClientRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,16),_Pm254dAlmClientRxPwrLowAlaPortn_Type())
pm254dAlmClientRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientRxPwrLowAlaPortn.setStatus(_A)
_Pm254dAlmClientRxPwrHighAlaPortn_Type=EkiOnOff
_Pm254dAlmClientRxPwrHighAlaPortn_Object=MibTableColumn
pm254dAlmClientRxPwrHighAlaPortn=_Pm254dAlmClientRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,2,2,32,1,17),_Pm254dAlmClientRxPwrHighAlaPortn_Type())
pm254dAlmClientRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientRxPwrHighAlaPortn.setStatus(_A)
_Pm254dAlmPortCrit_ObjectIdentity=ObjectIdentity
pm254dAlmPortCrit=_Pm254dAlmPortCrit_ObjectIdentity((1,3,6,1,4,1,20044,17,2,2,3))
_Pm254dAlmsynthAlmClientTable_Object=MibTable
pm254dAlmsynthAlmClientTable=_Pm254dAlmsynthAlmClientTable_Object((1,3,6,1,4,1,20044,17,2,2,3,8))
if mibBuilder.loadTexts:pm254dAlmsynthAlmClientTable.setStatus(_A)
_Pm254dAlmsynthAlmClientEntry_Object=MibTableRow
pm254dAlmsynthAlmClientEntry=_Pm254dAlmsynthAlmClientEntry_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1))
pm254dAlmsynthAlmClientEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pm254dAlmsynthAlmClientEntry.setStatus(_A)
class _Pm254dAlmsynthAlmClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmsynthAlmClientIndex_Type.__name__=_D
_Pm254dAlmsynthAlmClientIndex_Object=MibTableColumn
pm254dAlmsynthAlmClientIndex=_Pm254dAlmsynthAlmClientIndex_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,1),_Pm254dAlmsynthAlmClientIndex_Type())
pm254dAlmsynthAlmClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmsynthAlmClientIndex.setStatus(_A)
_Pm254dAlmClientSfpAbsentPortn_Type=EkiOnOff
_Pm254dAlmClientSfpAbsentPortn_Object=MibTableColumn
pm254dAlmClientSfpAbsentPortn=_Pm254dAlmClientSfpAbsentPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,2),_Pm254dAlmClientSfpAbsentPortn_Type())
pm254dAlmClientSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientSfpAbsentPortn.setStatus(_A)
_Pm254dAlmClientDdmAbsentPortn_Type=EkiOnOff
_Pm254dAlmClientDdmAbsentPortn_Object=MibTableColumn
pm254dAlmClientDdmAbsentPortn=_Pm254dAlmClientDdmAbsentPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,3),_Pm254dAlmClientDdmAbsentPortn_Type())
pm254dAlmClientDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientDdmAbsentPortn.setStatus(_A)
_Pm254dAlmClientHwFailAccPortn_Type=EkiOnOff
_Pm254dAlmClientHwFailAccPortn_Object=MibTableColumn
pm254dAlmClientHwFailAccPortn=_Pm254dAlmClientHwFailAccPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,5),_Pm254dAlmClientHwFailAccPortn_Type())
pm254dAlmClientHwFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientHwFailAccPortn.setStatus(_A)
_Pm254dAlmClientLsdPortn_Type=EkiOnOff
_Pm254dAlmClientLsdPortn_Object=MibTableColumn
pm254dAlmClientLsdPortn=_Pm254dAlmClientLsdPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,6),_Pm254dAlmClientLsdPortn_Type())
pm254dAlmClientLsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientLsdPortn.setStatus(_A)
_Pm254dAlmClientLocalOosPortn_Type=EkiOnOff
_Pm254dAlmClientLocalOosPortn_Object=MibTableColumn
pm254dAlmClientLocalOosPortn=_Pm254dAlmClientLocalOosPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,7),_Pm254dAlmClientLocalOosPortn_Type())
pm254dAlmClientLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientLocalOosPortn.setStatus(_A)
_Pm254dAlmClientRemoteOosPortn_Type=EkiOnOff
_Pm254dAlmClientRemoteOosPortn_Object=MibTableColumn
pm254dAlmClientRemoteOosPortn=_Pm254dAlmClientRemoteOosPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,8),_Pm254dAlmClientRemoteOosPortn_Type())
pm254dAlmClientRemoteOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientRemoteOosPortn.setStatus(_A)
_Pm254dAlmClientDwCaisPortn_Type=EkiOnOff
_Pm254dAlmClientDwCaisPortn_Object=MibTableColumn
pm254dAlmClientDwCaisPortn=_Pm254dAlmClientDwCaisPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,9),_Pm254dAlmClientDwCaisPortn_Type())
pm254dAlmClientDwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientDwCaisPortn.setStatus(_A)
_Pm254dAlmClientSfpDdmWarningPortn_Type=EkiOnOff
_Pm254dAlmClientSfpDdmWarningPortn_Object=MibTableColumn
pm254dAlmClientSfpDdmWarningPortn=_Pm254dAlmClientSfpDdmWarningPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,10),_Pm254dAlmClientSfpDdmWarningPortn_Type())
pm254dAlmClientSfpDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientSfpDdmWarningPortn.setStatus(_A)
_Pm254dAlmClientSfpDdmAlmPortn_Type=EkiOnOff
_Pm254dAlmClientSfpDdmAlmPortn_Object=MibTableColumn
pm254dAlmClientSfpDdmAlmPortn=_Pm254dAlmClientSfpDdmAlmPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,11),_Pm254dAlmClientSfpDdmAlmPortn_Type())
pm254dAlmClientSfpDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientSfpDdmAlmPortn.setStatus(_A)
_Pm254dAlmClientFailAccPortn_Type=EkiOnOff
_Pm254dAlmClientFailAccPortn_Object=MibTableColumn
pm254dAlmClientFailAccPortn=_Pm254dAlmClientFailAccPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,13),_Pm254dAlmClientFailAccPortn_Type())
pm254dAlmClientFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientFailAccPortn.setStatus(_A)
_Pm254dAlmClientUpCsfPortn_Type=EkiOnOff
_Pm254dAlmClientUpCsfPortn_Object=MibTableColumn
pm254dAlmClientUpCsfPortn=_Pm254dAlmClientUpCsfPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,8,1,17),_Pm254dAlmClientUpCsfPortn_Type())
pm254dAlmClientUpCsfPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientUpCsfPortn.setStatus(_A)
_Pm254dAlmaccessioAlmTable_Object=MibTable
pm254dAlmaccessioAlmTable=_Pm254dAlmaccessioAlmTable_Object((1,3,6,1,4,1,20044,17,2,2,3,16))
if mibBuilder.loadTexts:pm254dAlmaccessioAlmTable.setStatus(_A)
_Pm254dAlmaccessioAlmEntry_Object=MibTableRow
pm254dAlmaccessioAlmEntry=_Pm254dAlmaccessioAlmEntry_Object((1,3,6,1,4,1,20044,17,2,2,3,16,1))
pm254dAlmaccessioAlmEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm254dAlmaccessioAlmEntry.setStatus(_A)
class _Pm254dAlmaccessioAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmaccessioAlmIndex_Type.__name__=_D
_Pm254dAlmaccessioAlmIndex_Object=MibTableColumn
pm254dAlmaccessioAlmIndex=_Pm254dAlmaccessioAlmIndex_Object((1,3,6,1,4,1,20044,17,2,2,3,16,1,1),_Pm254dAlmaccessioAlmIndex_Type())
pm254dAlmaccessioAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmaccessioAlmIndex.setStatus(_A)
_Pm254dAlmClientDwLasFailPortn_Type=EkiOnOff
_Pm254dAlmClientDwLasFailPortn_Object=MibTableColumn
pm254dAlmClientDwLasFailPortn=_Pm254dAlmClientDwLasFailPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,16,1,2),_Pm254dAlmClientDwLasFailPortn_Type())
pm254dAlmClientDwLasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientDwLasFailPortn.setStatus(_A)
_Pm254dAlmClientUpLosPortn_Type=EkiOnOff
_Pm254dAlmClientUpLosPortn_Object=MibTableColumn
pm254dAlmClientUpLosPortn=_Pm254dAlmClientUpLosPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,16,1,5),_Pm254dAlmClientUpLosPortn_Type())
pm254dAlmClientUpLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientUpLosPortn.setStatus(_A)
_Pm254dAlmclientMapperDeAlmTable_Object=MibTable
pm254dAlmclientMapperDeAlmTable=_Pm254dAlmclientMapperDeAlmTable_Object((1,3,6,1,4,1,20044,17,2,2,3,72))
if mibBuilder.loadTexts:pm254dAlmclientMapperDeAlmTable.setStatus(_A)
_Pm254dAlmclientMapperDeAlmEntry_Object=MibTableRow
pm254dAlmclientMapperDeAlmEntry=_Pm254dAlmclientMapperDeAlmEntry_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1))
pm254dAlmclientMapperDeAlmEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm254dAlmclientMapperDeAlmEntry.setStatus(_A)
class _Pm254dAlmclientMapperDeAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmclientMapperDeAlmIndex_Type.__name__=_D
_Pm254dAlmclientMapperDeAlmIndex_Object=MibTableColumn
pm254dAlmclientMapperDeAlmIndex=_Pm254dAlmclientMapperDeAlmIndex_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1,1),_Pm254dAlmclientMapperDeAlmIndex_Type())
pm254dAlmclientMapperDeAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmclientMapperDeAlmIndex.setStatus(_A)
_Pm254dAlmClientUpAccOosPortn_Type=EkiOnOff
_Pm254dAlmClientUpAccOosPortn_Object=MibTableColumn
pm254dAlmClientUpAccOosPortn=_Pm254dAlmClientUpAccOosPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1,2),_Pm254dAlmClientUpAccOosPortn_Type())
pm254dAlmClientUpAccOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientUpAccOosPortn.setStatus(_A)
_Pm254dAlmClientUpBufferOvlPortn_Type=EkiOnOff
_Pm254dAlmClientUpBufferOvlPortn_Object=MibTableColumn
pm254dAlmClientUpBufferOvlPortn=_Pm254dAlmClientUpBufferOvlPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1,11),_Pm254dAlmClientUpBufferOvlPortn_Type())
pm254dAlmClientUpBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientUpBufferOvlPortn.setStatus(_A)
_Pm254dAlmClientDwCsfDetPortn_Type=EkiOnOff
_Pm254dAlmClientDwCsfDetPortn_Object=MibTableColumn
pm254dAlmClientDwCsfDetPortn=_Pm254dAlmClientDwCsfDetPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1,12),_Pm254dAlmClientDwCsfDetPortn_Type())
pm254dAlmClientDwCsfDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientDwCsfDetPortn.setStatus(_A)
_Pm254dAlmClientDwBufferOvlPortn_Type=EkiOnOff
_Pm254dAlmClientDwBufferOvlPortn_Object=MibTableColumn
pm254dAlmClientDwBufferOvlPortn=_Pm254dAlmClientDwBufferOvlPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1,15),_Pm254dAlmClientDwBufferOvlPortn_Type())
pm254dAlmClientDwBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientDwBufferOvlPortn.setStatus(_A)
_Pm254dAlmClientLoopAccFifoFailPortn_Type=EkiOnOff
_Pm254dAlmClientLoopAccFifoFailPortn_Object=MibTableColumn
pm254dAlmClientLoopAccFifoFailPortn=_Pm254dAlmClientLoopAccFifoFailPortn_Object((1,3,6,1,4,1,20044,17,2,2,3,72,1,16),_Pm254dAlmClientLoopAccFifoFailPortn_Type())
pm254dAlmClientLoopAccFifoFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmClientLoopAccFifoFailPortn.setStatus(_K)
_Pm254dAlmLine_ObjectIdentity=ObjectIdentity
pm254dAlmLine=_Pm254dAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,17,2,3))
_Pm254dAlmLineNurg_ObjectIdentity=ObjectIdentity
pm254dAlmLineNurg=_Pm254dAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,17,2,3,1))
_Pm254dAlmlineDownS1Table_Object=MibTable
pm254dAlmlineDownS1Table=_Pm254dAlmlineDownS1Table_Object((1,3,6,1,4,1,20044,17,2,3,1,130))
if mibBuilder.loadTexts:pm254dAlmlineDownS1Table.setStatus(_A)
_Pm254dAlmlineDownS1Entry_Object=MibTableRow
pm254dAlmlineDownS1Entry=_Pm254dAlmlineDownS1Entry_Object((1,3,6,1,4,1,20044,17,2,3,1,130,1))
pm254dAlmlineDownS1Entry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm254dAlmlineDownS1Entry.setStatus(_A)
class _Pm254dAlmlineDownS1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineDownS1Index_Type.__name__=_D
_Pm254dAlmlineDownS1Index_Object=MibTableColumn
pm254dAlmlineDownS1Index=_Pm254dAlmlineDownS1Index_Object((1,3,6,1,4,1,20044,17,2,3,1,130,1,1),_Pm254dAlmlineDownS1Index_Type())
pm254dAlmlineDownS1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDownS1Index.setStatus(_A)
class _Pm254dAlmlineDownS1Portn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pm254dAlmlineDownS1Portn_Type.__name__=_D
_Pm254dAlmlineDownS1Portn_Object=MibTableColumn
pm254dAlmlineDownS1Portn=_Pm254dAlmlineDownS1Portn_Object((1,3,6,1,4,1,20044,17,2,3,1,130,1,2),_Pm254dAlmlineDownS1Portn_Type())
pm254dAlmlineDownS1Portn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDownS1Portn.setStatus(_A)
_Pm254dAlmlineDownK1Table_Object=MibTable
pm254dAlmlineDownK1Table=_Pm254dAlmlineDownK1Table_Object((1,3,6,1,4,1,20044,17,2,3,1,131))
if mibBuilder.loadTexts:pm254dAlmlineDownK1Table.setStatus(_A)
_Pm254dAlmlineDownK1Entry_Object=MibTableRow
pm254dAlmlineDownK1Entry=_Pm254dAlmlineDownK1Entry_Object((1,3,6,1,4,1,20044,17,2,3,1,131,1))
pm254dAlmlineDownK1Entry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm254dAlmlineDownK1Entry.setStatus(_A)
class _Pm254dAlmlineDownK1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineDownK1Index_Type.__name__=_D
_Pm254dAlmlineDownK1Index_Object=MibTableColumn
pm254dAlmlineDownK1Index=_Pm254dAlmlineDownK1Index_Object((1,3,6,1,4,1,20044,17,2,3,1,131,1,1),_Pm254dAlmlineDownK1Index_Type())
pm254dAlmlineDownK1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDownK1Index.setStatus(_A)
class _Pm254dAlmlineDownK1Portn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pm254dAlmlineDownK1Portn_Type.__name__=_D
_Pm254dAlmlineDownK1Portn_Object=MibTableColumn
pm254dAlmlineDownK1Portn=_Pm254dAlmlineDownK1Portn_Object((1,3,6,1,4,1,20044,17,2,3,1,131,1,2),_Pm254dAlmlineDownK1Portn_Type())
pm254dAlmlineDownK1Portn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDownK1Portn.setStatus(_A)
_Pm254dAlmlineDownK2Table_Object=MibTable
pm254dAlmlineDownK2Table=_Pm254dAlmlineDownK2Table_Object((1,3,6,1,4,1,20044,17,2,3,1,132))
if mibBuilder.loadTexts:pm254dAlmlineDownK2Table.setStatus(_A)
_Pm254dAlmlineDownK2Entry_Object=MibTableRow
pm254dAlmlineDownK2Entry=_Pm254dAlmlineDownK2Entry_Object((1,3,6,1,4,1,20044,17,2,3,1,132,1))
pm254dAlmlineDownK2Entry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm254dAlmlineDownK2Entry.setStatus(_A)
class _Pm254dAlmlineDownK2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineDownK2Index_Type.__name__=_D
_Pm254dAlmlineDownK2Index_Object=MibTableColumn
pm254dAlmlineDownK2Index=_Pm254dAlmlineDownK2Index_Object((1,3,6,1,4,1,20044,17,2,3,1,132,1,1),_Pm254dAlmlineDownK2Index_Type())
pm254dAlmlineDownK2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDownK2Index.setStatus(_A)
class _Pm254dAlmlineDownK2Portn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pm254dAlmlineDownK2Portn_Type.__name__=_D
_Pm254dAlmlineDownK2Portn_Object=MibTableColumn
pm254dAlmlineDownK2Portn=_Pm254dAlmlineDownK2Portn_Object((1,3,6,1,4,1,20044,17,2,3,1,132,1,2),_Pm254dAlmlineDownK2Portn_Type())
pm254dAlmlineDownK2Portn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDownK2Portn.setStatus(_A)
_Pm254dAlmlineSfpWarnDdmTable_Object=MibTable
pm254dAlmlineSfpWarnDdmTable=_Pm254dAlmlineSfpWarnDdmTable_Object((1,3,6,1,4,1,20044,17,2,3,1,164))
if mibBuilder.loadTexts:pm254dAlmlineSfpWarnDdmTable.setStatus(_A)
_Pm254dAlmlineSfpWarnDdmEntry_Object=MibTableRow
pm254dAlmlineSfpWarnDdmEntry=_Pm254dAlmlineSfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1))
pm254dAlmlineSfpWarnDdmEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm254dAlmlineSfpWarnDdmEntry.setStatus(_A)
class _Pm254dAlmlineSfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineSfpWarnDdmIndex_Type.__name__=_D
_Pm254dAlmlineSfpWarnDdmIndex_Object=MibTableColumn
pm254dAlmlineSfpWarnDdmIndex=_Pm254dAlmlineSfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,1),_Pm254dAlmlineSfpWarnDdmIndex_Type())
pm254dAlmlineSfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineSfpWarnDdmIndex.setStatus(_A)
_Pm254dAlmLineTxPwLowWngPortn_Type=EkiOnOff
_Pm254dAlmLineTxPwLowWngPortn_Object=MibTableColumn
pm254dAlmLineTxPwLowWngPortn=_Pm254dAlmLineTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,2),_Pm254dAlmLineTxPwLowWngPortn_Type())
pm254dAlmLineTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxPwLowWngPortn.setStatus(_A)
_Pm254dAlmLineTxPwrHighWngPortn_Type=EkiOnOff
_Pm254dAlmLineTxPwrHighWngPortn_Object=MibTableColumn
pm254dAlmLineTxPwrHighWngPortn=_Pm254dAlmLineTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,3),_Pm254dAlmLineTxPwrHighWngPortn_Type())
pm254dAlmLineTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxPwrHighWngPortn.setStatus(_A)
_Pm254dAlmLineTxBiasLowWngPortn_Type=EkiOnOff
_Pm254dAlmLineTxBiasLowWngPortn_Object=MibTableColumn
pm254dAlmLineTxBiasLowWngPortn=_Pm254dAlmLineTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,4),_Pm254dAlmLineTxBiasLowWngPortn_Type())
pm254dAlmLineTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxBiasLowWngPortn.setStatus(_A)
_Pm254dAlmLineTxBiasHighWngPortn_Type=EkiOnOff
_Pm254dAlmLineTxBiasHighWngPortn_Object=MibTableColumn
pm254dAlmLineTxBiasHighWngPortn=_Pm254dAlmLineTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,5),_Pm254dAlmLineTxBiasHighWngPortn_Type())
pm254dAlmLineTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxBiasHighWngPortn.setStatus(_A)
_Pm254dAlmLineVccLowWngPortn_Type=EkiOnOff
_Pm254dAlmLineVccLowWngPortn_Object=MibTableColumn
pm254dAlmLineVccLowWngPortn=_Pm254dAlmLineVccLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,6),_Pm254dAlmLineVccLowWngPortn_Type())
pm254dAlmLineVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineVccLowWngPortn.setStatus(_A)
_Pm254dAlmLineVccHighWngPortn_Type=EkiOnOff
_Pm254dAlmLineVccHighWngPortn_Object=MibTableColumn
pm254dAlmLineVccHighWngPortn=_Pm254dAlmLineVccHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,7),_Pm254dAlmLineVccHighWngPortn_Type())
pm254dAlmLineVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineVccHighWngPortn.setStatus(_A)
_Pm254dAlmLineTempLowWngPortn_Type=EkiOnOff
_Pm254dAlmLineTempLowWngPortn_Object=MibTableColumn
pm254dAlmLineTempLowWngPortn=_Pm254dAlmLineTempLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,8),_Pm254dAlmLineTempLowWngPortn_Type())
pm254dAlmLineTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTempLowWngPortn.setStatus(_A)
_Pm254dAlmLineTempHighWngPortn_Type=EkiOnOff
_Pm254dAlmLineTempHighWngPortn_Object=MibTableColumn
pm254dAlmLineTempHighWngPortn=_Pm254dAlmLineTempHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,9),_Pm254dAlmLineTempHighWngPortn_Type())
pm254dAlmLineTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTempHighWngPortn.setStatus(_A)
_Pm254dAlmLineRxPwrLowWngPortn_Type=EkiOnOff
_Pm254dAlmLineRxPwrLowWngPortn_Object=MibTableColumn
pm254dAlmLineRxPwrLowWngPortn=_Pm254dAlmLineRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,16),_Pm254dAlmLineRxPwrLowWngPortn_Type())
pm254dAlmLineRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineRxPwrLowWngPortn.setStatus(_A)
_Pm254dAlmLineRxPwrHighWngPortn_Type=EkiOnOff
_Pm254dAlmLineRxPwrHighWngPortn_Object=MibTableColumn
pm254dAlmLineRxPwrHighWngPortn=_Pm254dAlmLineRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,17,2,3,1,164,1,17),_Pm254dAlmLineRxPwrHighWngPortn_Type())
pm254dAlmLineRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineRxPwrHighWngPortn.setStatus(_A)
_Pm254dAlmLineUrg_ObjectIdentity=ObjectIdentity
pm254dAlmLineUrg=_Pm254dAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,17,2,3,2))
_Pm254dAlmlineSfpAlaDdmTable_Object=MibTable
pm254dAlmlineSfpAlaDdmTable=_Pm254dAlmlineSfpAlaDdmTable_Object((1,3,6,1,4,1,20044,17,2,3,2,162))
if mibBuilder.loadTexts:pm254dAlmlineSfpAlaDdmTable.setStatus(_A)
_Pm254dAlmlineSfpAlaDdmEntry_Object=MibTableRow
pm254dAlmlineSfpAlaDdmEntry=_Pm254dAlmlineSfpAlaDdmEntry_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1))
pm254dAlmlineSfpAlaDdmEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm254dAlmlineSfpAlaDdmEntry.setStatus(_A)
class _Pm254dAlmlineSfpAlaDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineSfpAlaDdmIndex_Type.__name__=_D
_Pm254dAlmlineSfpAlaDdmIndex_Object=MibTableColumn
pm254dAlmlineSfpAlaDdmIndex=_Pm254dAlmlineSfpAlaDdmIndex_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,1),_Pm254dAlmlineSfpAlaDdmIndex_Type())
pm254dAlmlineSfpAlaDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineSfpAlaDdmIndex.setStatus(_A)
_Pm254dAlmLineTxPwrLowAlaPortn_Type=EkiOnOff
_Pm254dAlmLineTxPwrLowAlaPortn_Object=MibTableColumn
pm254dAlmLineTxPwrLowAlaPortn=_Pm254dAlmLineTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,2),_Pm254dAlmLineTxPwrLowAlaPortn_Type())
pm254dAlmLineTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxPwrLowAlaPortn.setStatus(_A)
_Pm254dAlmLineTxPwrHighAlaPortn_Type=EkiOnOff
_Pm254dAlmLineTxPwrHighAlaPortn_Object=MibTableColumn
pm254dAlmLineTxPwrHighAlaPortn=_Pm254dAlmLineTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,3),_Pm254dAlmLineTxPwrHighAlaPortn_Type())
pm254dAlmLineTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxPwrHighAlaPortn.setStatus(_A)
_Pm254dAlmLineTxBiasLowAlaPortn_Type=EkiOnOff
_Pm254dAlmLineTxBiasLowAlaPortn_Object=MibTableColumn
pm254dAlmLineTxBiasLowAlaPortn=_Pm254dAlmLineTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,4),_Pm254dAlmLineTxBiasLowAlaPortn_Type())
pm254dAlmLineTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxBiasLowAlaPortn.setStatus(_A)
_Pm254dAlmLineTxBiasHighAlaPortn_Type=EkiOnOff
_Pm254dAlmLineTxBiasHighAlaPortn_Object=MibTableColumn
pm254dAlmLineTxBiasHighAlaPortn=_Pm254dAlmLineTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,5),_Pm254dAlmLineTxBiasHighAlaPortn_Type())
pm254dAlmLineTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTxBiasHighAlaPortn.setStatus(_A)
_Pm254dAlmLineVccLowAlaPortn_Type=EkiOnOff
_Pm254dAlmLineVccLowAlaPortn_Object=MibTableColumn
pm254dAlmLineVccLowAlaPortn=_Pm254dAlmLineVccLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,6),_Pm254dAlmLineVccLowAlaPortn_Type())
pm254dAlmLineVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineVccLowAlaPortn.setStatus(_A)
_Pm254dAlmLineVccHighAlaPortn_Type=EkiOnOff
_Pm254dAlmLineVccHighAlaPortn_Object=MibTableColumn
pm254dAlmLineVccHighAlaPortn=_Pm254dAlmLineVccHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,7),_Pm254dAlmLineVccHighAlaPortn_Type())
pm254dAlmLineVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineVccHighAlaPortn.setStatus(_A)
_Pm254dAlmLineTempLowAlaPortn_Type=EkiOnOff
_Pm254dAlmLineTempLowAlaPortn_Object=MibTableColumn
pm254dAlmLineTempLowAlaPortn=_Pm254dAlmLineTempLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,8),_Pm254dAlmLineTempLowAlaPortn_Type())
pm254dAlmLineTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTempLowAlaPortn.setStatus(_A)
_Pm254dAlmLineTempHighAlaPortn_Type=EkiOnOff
_Pm254dAlmLineTempHighAlaPortn_Object=MibTableColumn
pm254dAlmLineTempHighAlaPortn=_Pm254dAlmLineTempHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,9),_Pm254dAlmLineTempHighAlaPortn_Type())
pm254dAlmLineTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineTempHighAlaPortn.setStatus(_A)
_Pm254dAlmLineRxPwrLowAlaPortn_Type=EkiOnOff
_Pm254dAlmLineRxPwrLowAlaPortn_Object=MibTableColumn
pm254dAlmLineRxPwrLowAlaPortn=_Pm254dAlmLineRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,16),_Pm254dAlmLineRxPwrLowAlaPortn_Type())
pm254dAlmLineRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineRxPwrLowAlaPortn.setStatus(_A)
_Pm254dAlmLineRxPwrHighAlaPortn_Type=EkiOnOff
_Pm254dAlmLineRxPwrHighAlaPortn_Object=MibTableColumn
pm254dAlmLineRxPwrHighAlaPortn=_Pm254dAlmLineRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,17,2,3,2,162,1,17),_Pm254dAlmLineRxPwrHighAlaPortn_Type())
pm254dAlmLineRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineRxPwrHighAlaPortn.setStatus(_A)
_Pm254dAlmLineCrit_ObjectIdentity=ObjectIdentity
pm254dAlmLineCrit=_Pm254dAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,17,2,3,3))
_Pm254dAlmsynthAlmLineTable_Object=MibTable
pm254dAlmsynthAlmLineTable=_Pm254dAlmsynthAlmLineTable_Object((1,3,6,1,4,1,20044,17,2,3,3,5))
if mibBuilder.loadTexts:pm254dAlmsynthAlmLineTable.setStatus(_A)
_Pm254dAlmsynthAlmLineEntry_Object=MibTableRow
pm254dAlmsynthAlmLineEntry=_Pm254dAlmsynthAlmLineEntry_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1))
pm254dAlmsynthAlmLineEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm254dAlmsynthAlmLineEntry.setStatus(_A)
class _Pm254dAlmsynthAlmLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmsynthAlmLineIndex_Type.__name__=_D
_Pm254dAlmsynthAlmLineIndex_Object=MibTableColumn
pm254dAlmsynthAlmLineIndex=_Pm254dAlmsynthAlmLineIndex_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,1),_Pm254dAlmsynthAlmLineIndex_Type())
pm254dAlmsynthAlmLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmsynthAlmLineIndex.setStatus(_A)
_Pm254dAlmLineSfpAbsentPortn_Type=EkiOnOff
_Pm254dAlmLineSfpAbsentPortn_Object=MibTableColumn
pm254dAlmLineSfpAbsentPortn=_Pm254dAlmLineSfpAbsentPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,2),_Pm254dAlmLineSfpAbsentPortn_Type())
pm254dAlmLineSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineSfpAbsentPortn.setStatus(_A)
_Pm254dAlmLineDdmAbsentPortn_Type=EkiOnOff
_Pm254dAlmLineDdmAbsentPortn_Object=MibTableColumn
pm254dAlmLineDdmAbsentPortn=_Pm254dAlmLineDdmAbsentPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,3),_Pm254dAlmLineDdmAbsentPortn_Type())
pm254dAlmLineDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDdmAbsentPortn.setStatus(_A)
_Pm254dAlmLineHwFailPortn_Type=EkiOnOff
_Pm254dAlmLineHwFailPortn_Object=MibTableColumn
pm254dAlmLineHwFailPortn=_Pm254dAlmLineHwFailPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,5),_Pm254dAlmLineHwFailPortn_Type())
pm254dAlmLineHwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineHwFailPortn.setStatus(_A)
_Pm254dAlmLineLsdPortn_Type=EkiOnOff
_Pm254dAlmLineLsdPortn_Object=MibTableColumn
pm254dAlmLineLsdPortn=_Pm254dAlmLineLsdPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,6),_Pm254dAlmLineLsdPortn_Type())
pm254dAlmLineLsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineLsdPortn.setStatus(_A)
_Pm254dAlmLineLocalOosPortn_Type=EkiOnOff
_Pm254dAlmLineLocalOosPortn_Object=MibTableColumn
pm254dAlmLineLocalOosPortn=_Pm254dAlmLineLocalOosPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,7),_Pm254dAlmLineLocalOosPortn_Type())
pm254dAlmLineLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineLocalOosPortn.setStatus(_A)
_Pm254dAlmLineUpRdiInsPortn_Type=EkiOnOff
_Pm254dAlmLineUpRdiInsPortn_Object=MibTableColumn
pm254dAlmLineUpRdiInsPortn=_Pm254dAlmLineUpRdiInsPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,9),_Pm254dAlmLineUpRdiInsPortn_Type())
pm254dAlmLineUpRdiInsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineUpRdiInsPortn.setStatus(_A)
_Pm254dAlmLineDdmWarningPortn_Type=EkiOnOff
_Pm254dAlmLineDdmWarningPortn_Object=MibTableColumn
pm254dAlmLineDdmWarningPortn=_Pm254dAlmLineDdmWarningPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,10),_Pm254dAlmLineDdmWarningPortn_Type())
pm254dAlmLineDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDdmWarningPortn.setStatus(_A)
_Pm254dAlmLineDdmAlmPortn_Type=EkiOnOff
_Pm254dAlmLineDdmAlmPortn_Object=MibTableColumn
pm254dAlmLineDdmAlmPortn=_Pm254dAlmLineDdmAlmPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,11),_Pm254dAlmLineDdmAlmPortn_Type())
pm254dAlmLineDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDdmAlmPortn.setStatus(_A)
_Pm254dAlmLineFailPortn_Type=EkiOnOff
_Pm254dAlmLineFailPortn_Object=MibTableColumn
pm254dAlmLineFailPortn=_Pm254dAlmLineFailPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,13),_Pm254dAlmLineFailPortn_Type())
pm254dAlmLineFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineFailPortn.setStatus(_A)
_Pm254dAlmDccActivePortn_Type=EkiOnOff
_Pm254dAlmDccActivePortn_Object=MibTableColumn
pm254dAlmDccActivePortn=_Pm254dAlmDccActivePortn_Object((1,3,6,1,4,1,20044,17,2,3,3,5,1,17),_Pm254dAlmDccActivePortn_Type())
pm254dAlmDccActivePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmDccActivePortn.setStatus(_A)
_Pm254dAlmlineDfrmAlmTable_Object=MibTable
pm254dAlmlineDfrmAlmTable=_Pm254dAlmlineDfrmAlmTable_Object((1,3,6,1,4,1,20044,17,2,3,3,128))
if mibBuilder.loadTexts:pm254dAlmlineDfrmAlmTable.setStatus(_A)
_Pm254dAlmlineDfrmAlmEntry_Object=MibTableRow
pm254dAlmlineDfrmAlmEntry=_Pm254dAlmlineDfrmAlmEntry_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1))
pm254dAlmlineDfrmAlmEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm254dAlmlineDfrmAlmEntry.setStatus(_A)
class _Pm254dAlmlineDfrmAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineDfrmAlmIndex_Type.__name__=_D
_Pm254dAlmlineDfrmAlmIndex_Object=MibTableColumn
pm254dAlmlineDfrmAlmIndex=_Pm254dAlmlineDfrmAlmIndex_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,1),_Pm254dAlmlineDfrmAlmIndex_Type())
pm254dAlmlineDfrmAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineDfrmAlmIndex.setStatus(_A)
_Pm254dAlmLineDwAisDetPortn_Type=EkiOnOff
_Pm254dAlmLineDwAisDetPortn_Object=MibTableColumn
pm254dAlmLineDwAisDetPortn=_Pm254dAlmLineDwAisDetPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,2),_Pm254dAlmLineDwAisDetPortn_Type())
pm254dAlmLineDwAisDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDwAisDetPortn.setStatus(_A)
_Pm254dAlmLineDwRdiDetPortn_Type=EkiOnOff
_Pm254dAlmLineDwRdiDetPortn_Object=MibTableColumn
pm254dAlmLineDwRdiDetPortn=_Pm254dAlmLineDwRdiDetPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,3),_Pm254dAlmLineDwRdiDetPortn_Type())
pm254dAlmLineDwRdiDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDwRdiDetPortn.setStatus(_A)
_Pm254dAlmLineDwOofPortn_Type=EkiOnOff
_Pm254dAlmLineDwOofPortn_Object=MibTableColumn
pm254dAlmLineDwOofPortn=_Pm254dAlmLineDwOofPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,4),_Pm254dAlmLineDwOofPortn_Type())
pm254dAlmLineDwOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDwOofPortn.setStatus(_A)
_Pm254dAlmLineDwLofPortn_Type=EkiOnOff
_Pm254dAlmLineDwLofPortn_Object=MibTableColumn
pm254dAlmLineDwLofPortn=_Pm254dAlmLineDwLofPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,5),_Pm254dAlmLineDwLofPortn_Type())
pm254dAlmLineDwLofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDwLofPortn.setStatus(_A)
_Pm254dAlmDwLopPortn_Type=EkiOnOff
_Pm254dAlmDwLopPortn_Object=MibTableColumn
pm254dAlmDwLopPortn=_Pm254dAlmDwLopPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,10),_Pm254dAlmDwLopPortn_Type())
pm254dAlmDwLopPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmDwLopPortn.setStatus(_A)
_Pm254dAlmDwAuAisPortn_Type=EkiOnOff
_Pm254dAlmDwAuAisPortn_Object=MibTableColumn
pm254dAlmDwAuAisPortn=_Pm254dAlmDwAuAisPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,128,1,11),_Pm254dAlmDwAuAisPortn_Type())
pm254dAlmDwAuAisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmDwAuAisPortn.setStatus(_A)
_Pm254dAlmlineIoAlmTable_Object=MibTable
pm254dAlmlineIoAlmTable=_Pm254dAlmlineIoAlmTable_Object((1,3,6,1,4,1,20044,17,2,3,3,160))
if mibBuilder.loadTexts:pm254dAlmlineIoAlmTable.setStatus(_A)
_Pm254dAlmlineIoAlmEntry_Object=MibTableRow
pm254dAlmlineIoAlmEntry=_Pm254dAlmlineIoAlmEntry_Object((1,3,6,1,4,1,20044,17,2,3,3,160,1))
pm254dAlmlineIoAlmEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm254dAlmlineIoAlmEntry.setStatus(_A)
class _Pm254dAlmlineIoAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dAlmlineIoAlmIndex_Type.__name__=_D
_Pm254dAlmlineIoAlmIndex_Object=MibTableColumn
pm254dAlmlineIoAlmIndex=_Pm254dAlmlineIoAlmIndex_Object((1,3,6,1,4,1,20044,17,2,3,3,160,1,1),_Pm254dAlmlineIoAlmIndex_Type())
pm254dAlmlineIoAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmlineIoAlmIndex.setStatus(_A)
_Pm254dAlmLineUpLasFailPortn_Type=EkiOnOff
_Pm254dAlmLineUpLasFailPortn_Object=MibTableColumn
pm254dAlmLineUpLasFailPortn=_Pm254dAlmLineUpLasFailPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,160,1,2),_Pm254dAlmLineUpLasFailPortn_Type())
pm254dAlmLineUpLasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineUpLasFailPortn.setStatus(_A)
_Pm254dAlmLineDwLosPortn_Type=EkiOnOff
_Pm254dAlmLineDwLosPortn_Object=MibTableColumn
pm254dAlmLineDwLosPortn=_Pm254dAlmLineDwLosPortn_Object((1,3,6,1,4,1,20044,17,2,3,3,160,1,5),_Pm254dAlmLineDwLosPortn_Type())
pm254dAlmLineDwLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dAlmLineDwLosPortn.setStatus(_A)
_Pm254dmeasures_ObjectIdentity=ObjectIdentity
pm254dmeasures=_Pm254dmeasures_ObjectIdentity((1,3,6,1,4,1,20044,17,3))
_Pm254dMesrOther_ObjectIdentity=ObjectIdentity
pm254dMesrOther=_Pm254dMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,17,3,1))
_Pm254dMesrPort_ObjectIdentity=ObjectIdentity
pm254dMesrPort=_Pm254dMesrPort_ObjectIdentity((1,3,6,1,4,1,20044,17,3,2))
_Pm254dMesrclientTempMeasTable_Object=MibTable
pm254dMesrclientTempMeasTable=_Pm254dMesrclientTempMeasTable_Object((1,3,6,1,4,1,20044,17,3,2,16))
if mibBuilder.loadTexts:pm254dMesrclientTempMeasTable.setStatus(_A)
_Pm254dMesrclientTempMeasEntry_Object=MibTableRow
pm254dMesrclientTempMeasEntry=_Pm254dMesrclientTempMeasEntry_Object((1,3,6,1,4,1,20044,17,3,2,16,1))
pm254dMesrclientTempMeasEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm254dMesrclientTempMeasEntry.setStatus(_A)
class _Pm254dMesrclientTempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrclientTempMeasIndex_Type.__name__=_D
_Pm254dMesrclientTempMeasIndex_Object=MibTableColumn
pm254dMesrclientTempMeasIndex=_Pm254dMesrclientTempMeasIndex_Object((1,3,6,1,4,1,20044,17,3,2,16,1,1),_Pm254dMesrclientTempMeasIndex_Type())
pm254dMesrclientTempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientTempMeasIndex.setStatus(_A)
class _Pm254dMesrclientTempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrclientTempMeasPortn_Type.__name__=_D
_Pm254dMesrclientTempMeasPortn_Object=MibTableColumn
pm254dMesrclientTempMeasPortn=_Pm254dMesrclientTempMeasPortn_Object((1,3,6,1,4,1,20044,17,3,2,16,1,2),_Pm254dMesrclientTempMeasPortn_Type())
pm254dMesrclientTempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientTempMeasPortn.setStatus(_A)
_Pm254dMesrclientVoltMeasTable_Object=MibTable
pm254dMesrclientVoltMeasTable=_Pm254dMesrclientVoltMeasTable_Object((1,3,6,1,4,1,20044,17,3,2,24))
if mibBuilder.loadTexts:pm254dMesrclientVoltMeasTable.setStatus(_A)
_Pm254dMesrclientVoltMeasEntry_Object=MibTableRow
pm254dMesrclientVoltMeasEntry=_Pm254dMesrclientVoltMeasEntry_Object((1,3,6,1,4,1,20044,17,3,2,24,1))
pm254dMesrclientVoltMeasEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm254dMesrclientVoltMeasEntry.setStatus(_A)
class _Pm254dMesrclientVoltMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrclientVoltMeasIndex_Type.__name__=_D
_Pm254dMesrclientVoltMeasIndex_Object=MibTableColumn
pm254dMesrclientVoltMeasIndex=_Pm254dMesrclientVoltMeasIndex_Object((1,3,6,1,4,1,20044,17,3,2,24,1,1),_Pm254dMesrclientVoltMeasIndex_Type())
pm254dMesrclientVoltMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientVoltMeasIndex.setStatus(_A)
class _Pm254dMesrclientVoltMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrclientVoltMeasPortn_Type.__name__=_D
_Pm254dMesrclientVoltMeasPortn_Object=MibTableColumn
pm254dMesrclientVoltMeasPortn=_Pm254dMesrclientVoltMeasPortn_Object((1,3,6,1,4,1,20044,17,3,2,24,1,2),_Pm254dMesrclientVoltMeasPortn_Type())
pm254dMesrclientVoltMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientVoltMeasPortn.setStatus(_A)
_Pm254dMesrclientBiasMeasTable_Object=MibTable
pm254dMesrclientBiasMeasTable=_Pm254dMesrclientBiasMeasTable_Object((1,3,6,1,4,1,20044,17,3,2,32))
if mibBuilder.loadTexts:pm254dMesrclientBiasMeasTable.setStatus(_A)
_Pm254dMesrclientBiasMeasEntry_Object=MibTableRow
pm254dMesrclientBiasMeasEntry=_Pm254dMesrclientBiasMeasEntry_Object((1,3,6,1,4,1,20044,17,3,2,32,1))
pm254dMesrclientBiasMeasEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm254dMesrclientBiasMeasEntry.setStatus(_A)
class _Pm254dMesrclientBiasMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrclientBiasMeasIndex_Type.__name__=_D
_Pm254dMesrclientBiasMeasIndex_Object=MibTableColumn
pm254dMesrclientBiasMeasIndex=_Pm254dMesrclientBiasMeasIndex_Object((1,3,6,1,4,1,20044,17,3,2,32,1,1),_Pm254dMesrclientBiasMeasIndex_Type())
pm254dMesrclientBiasMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientBiasMeasIndex.setStatus(_A)
class _Pm254dMesrclientBiasMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrclientBiasMeasPortn_Type.__name__=_D
_Pm254dMesrclientBiasMeasPortn_Object=MibTableColumn
pm254dMesrclientBiasMeasPortn=_Pm254dMesrclientBiasMeasPortn_Object((1,3,6,1,4,1,20044,17,3,2,32,1,2),_Pm254dMesrclientBiasMeasPortn_Type())
pm254dMesrclientBiasMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientBiasMeasPortn.setStatus(_A)
_Pm254dMesrclientTxpwrMeasTable_Object=MibTable
pm254dMesrclientTxpwrMeasTable=_Pm254dMesrclientTxpwrMeasTable_Object((1,3,6,1,4,1,20044,17,3,2,40))
if mibBuilder.loadTexts:pm254dMesrclientTxpwrMeasTable.setStatus(_A)
_Pm254dMesrclientTxpwrMeasEntry_Object=MibTableRow
pm254dMesrclientTxpwrMeasEntry=_Pm254dMesrclientTxpwrMeasEntry_Object((1,3,6,1,4,1,20044,17,3,2,40,1))
pm254dMesrclientTxpwrMeasEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm254dMesrclientTxpwrMeasEntry.setStatus(_A)
class _Pm254dMesrclientTxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrclientTxpwrMeasIndex_Type.__name__=_D
_Pm254dMesrclientTxpwrMeasIndex_Object=MibTableColumn
pm254dMesrclientTxpwrMeasIndex=_Pm254dMesrclientTxpwrMeasIndex_Object((1,3,6,1,4,1,20044,17,3,2,40,1,1),_Pm254dMesrclientTxpwrMeasIndex_Type())
pm254dMesrclientTxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientTxpwrMeasIndex.setStatus(_A)
class _Pm254dMesrclientTxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrclientTxpwrMeasPortn_Type.__name__=_D
_Pm254dMesrclientTxpwrMeasPortn_Object=MibTableColumn
pm254dMesrclientTxpwrMeasPortn=_Pm254dMesrclientTxpwrMeasPortn_Object((1,3,6,1,4,1,20044,17,3,2,40,1,2),_Pm254dMesrclientTxpwrMeasPortn_Type())
pm254dMesrclientTxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientTxpwrMeasPortn.setStatus(_A)
_Pm254dMesrclientRxpwrMeasTable_Object=MibTable
pm254dMesrclientRxpwrMeasTable=_Pm254dMesrclientRxpwrMeasTable_Object((1,3,6,1,4,1,20044,17,3,2,48))
if mibBuilder.loadTexts:pm254dMesrclientRxpwrMeasTable.setStatus(_A)
_Pm254dMesrclientRxpwrMeasEntry_Object=MibTableRow
pm254dMesrclientRxpwrMeasEntry=_Pm254dMesrclientRxpwrMeasEntry_Object((1,3,6,1,4,1,20044,17,3,2,48,1))
pm254dMesrclientRxpwrMeasEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm254dMesrclientRxpwrMeasEntry.setStatus(_A)
class _Pm254dMesrclientRxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrclientRxpwrMeasIndex_Type.__name__=_D
_Pm254dMesrclientRxpwrMeasIndex_Object=MibTableColumn
pm254dMesrclientRxpwrMeasIndex=_Pm254dMesrclientRxpwrMeasIndex_Object((1,3,6,1,4,1,20044,17,3,2,48,1,1),_Pm254dMesrclientRxpwrMeasIndex_Type())
pm254dMesrclientRxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientRxpwrMeasIndex.setStatus(_A)
class _Pm254dMesrclientRxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrclientRxpwrMeasPortn_Type.__name__=_D
_Pm254dMesrclientRxpwrMeasPortn_Object=MibTableColumn
pm254dMesrclientRxpwrMeasPortn=_Pm254dMesrclientRxpwrMeasPortn_Object((1,3,6,1,4,1,20044,17,3,2,48,1,2),_Pm254dMesrclientRxpwrMeasPortn_Type())
pm254dMesrclientRxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrclientRxpwrMeasPortn.setStatus(_A)
_Pm254dMesrLine_ObjectIdentity=ObjectIdentity
pm254dMesrLine=_Pm254dMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,17,3,3))
_Pm254dMesrlineTempMeasTable_Object=MibTable
pm254dMesrlineTempMeasTable=_Pm254dMesrlineTempMeasTable_Object((1,3,6,1,4,1,20044,17,3,3,160))
if mibBuilder.loadTexts:pm254dMesrlineTempMeasTable.setStatus(_A)
_Pm254dMesrlineTempMeasEntry_Object=MibTableRow
pm254dMesrlineTempMeasEntry=_Pm254dMesrlineTempMeasEntry_Object((1,3,6,1,4,1,20044,17,3,3,160,1))
pm254dMesrlineTempMeasEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm254dMesrlineTempMeasEntry.setStatus(_A)
class _Pm254dMesrlineTempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrlineTempMeasIndex_Type.__name__=_D
_Pm254dMesrlineTempMeasIndex_Object=MibTableColumn
pm254dMesrlineTempMeasIndex=_Pm254dMesrlineTempMeasIndex_Object((1,3,6,1,4,1,20044,17,3,3,160,1,1),_Pm254dMesrlineTempMeasIndex_Type())
pm254dMesrlineTempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineTempMeasIndex.setStatus(_A)
class _Pm254dMesrlineTempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrlineTempMeasPortn_Type.__name__=_D
_Pm254dMesrlineTempMeasPortn_Object=MibTableColumn
pm254dMesrlineTempMeasPortn=_Pm254dMesrlineTempMeasPortn_Object((1,3,6,1,4,1,20044,17,3,3,160,1,2),_Pm254dMesrlineTempMeasPortn_Type())
pm254dMesrlineTempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineTempMeasPortn.setStatus(_A)
_Pm254dMesrlineVoltMeasTable_Object=MibTable
pm254dMesrlineVoltMeasTable=_Pm254dMesrlineVoltMeasTable_Object((1,3,6,1,4,1,20044,17,3,3,161))
if mibBuilder.loadTexts:pm254dMesrlineVoltMeasTable.setStatus(_A)
_Pm254dMesrlineVoltMeasEntry_Object=MibTableRow
pm254dMesrlineVoltMeasEntry=_Pm254dMesrlineVoltMeasEntry_Object((1,3,6,1,4,1,20044,17,3,3,161,1))
pm254dMesrlineVoltMeasEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm254dMesrlineVoltMeasEntry.setStatus(_A)
class _Pm254dMesrlineVoltMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrlineVoltMeasIndex_Type.__name__=_D
_Pm254dMesrlineVoltMeasIndex_Object=MibTableColumn
pm254dMesrlineVoltMeasIndex=_Pm254dMesrlineVoltMeasIndex_Object((1,3,6,1,4,1,20044,17,3,3,161,1,1),_Pm254dMesrlineVoltMeasIndex_Type())
pm254dMesrlineVoltMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineVoltMeasIndex.setStatus(_A)
class _Pm254dMesrlineVoltMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrlineVoltMeasPortn_Type.__name__=_D
_Pm254dMesrlineVoltMeasPortn_Object=MibTableColumn
pm254dMesrlineVoltMeasPortn=_Pm254dMesrlineVoltMeasPortn_Object((1,3,6,1,4,1,20044,17,3,3,161,1,2),_Pm254dMesrlineVoltMeasPortn_Type())
pm254dMesrlineVoltMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineVoltMeasPortn.setStatus(_A)
_Pm254dMesrlineBiasMeasTable_Object=MibTable
pm254dMesrlineBiasMeasTable=_Pm254dMesrlineBiasMeasTable_Object((1,3,6,1,4,1,20044,17,3,3,162))
if mibBuilder.loadTexts:pm254dMesrlineBiasMeasTable.setStatus(_A)
_Pm254dMesrlineBiasMeasEntry_Object=MibTableRow
pm254dMesrlineBiasMeasEntry=_Pm254dMesrlineBiasMeasEntry_Object((1,3,6,1,4,1,20044,17,3,3,162,1))
pm254dMesrlineBiasMeasEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm254dMesrlineBiasMeasEntry.setStatus(_A)
class _Pm254dMesrlineBiasMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrlineBiasMeasIndex_Type.__name__=_D
_Pm254dMesrlineBiasMeasIndex_Object=MibTableColumn
pm254dMesrlineBiasMeasIndex=_Pm254dMesrlineBiasMeasIndex_Object((1,3,6,1,4,1,20044,17,3,3,162,1,1),_Pm254dMesrlineBiasMeasIndex_Type())
pm254dMesrlineBiasMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineBiasMeasIndex.setStatus(_A)
class _Pm254dMesrlineBiasMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrlineBiasMeasPortn_Type.__name__=_D
_Pm254dMesrlineBiasMeasPortn_Object=MibTableColumn
pm254dMesrlineBiasMeasPortn=_Pm254dMesrlineBiasMeasPortn_Object((1,3,6,1,4,1,20044,17,3,3,162,1,2),_Pm254dMesrlineBiasMeasPortn_Type())
pm254dMesrlineBiasMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineBiasMeasPortn.setStatus(_A)
_Pm254dMesrlineTxpwrMeasTable_Object=MibTable
pm254dMesrlineTxpwrMeasTable=_Pm254dMesrlineTxpwrMeasTable_Object((1,3,6,1,4,1,20044,17,3,3,163))
if mibBuilder.loadTexts:pm254dMesrlineTxpwrMeasTable.setStatus(_A)
_Pm254dMesrlineTxpwrMeasEntry_Object=MibTableRow
pm254dMesrlineTxpwrMeasEntry=_Pm254dMesrlineTxpwrMeasEntry_Object((1,3,6,1,4,1,20044,17,3,3,163,1))
pm254dMesrlineTxpwrMeasEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm254dMesrlineTxpwrMeasEntry.setStatus(_A)
class _Pm254dMesrlineTxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrlineTxpwrMeasIndex_Type.__name__=_D
_Pm254dMesrlineTxpwrMeasIndex_Object=MibTableColumn
pm254dMesrlineTxpwrMeasIndex=_Pm254dMesrlineTxpwrMeasIndex_Object((1,3,6,1,4,1,20044,17,3,3,163,1,1),_Pm254dMesrlineTxpwrMeasIndex_Type())
pm254dMesrlineTxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineTxpwrMeasIndex.setStatus(_A)
class _Pm254dMesrlineTxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrlineTxpwrMeasPortn_Type.__name__=_D
_Pm254dMesrlineTxpwrMeasPortn_Object=MibTableColumn
pm254dMesrlineTxpwrMeasPortn=_Pm254dMesrlineTxpwrMeasPortn_Object((1,3,6,1,4,1,20044,17,3,3,163,1,2),_Pm254dMesrlineTxpwrMeasPortn_Type())
pm254dMesrlineTxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineTxpwrMeasPortn.setStatus(_A)
_Pm254dMesrlineRxpwrMeasTable_Object=MibTable
pm254dMesrlineRxpwrMeasTable=_Pm254dMesrlineRxpwrMeasTable_Object((1,3,6,1,4,1,20044,17,3,3,164))
if mibBuilder.loadTexts:pm254dMesrlineRxpwrMeasTable.setStatus(_A)
_Pm254dMesrlineRxpwrMeasEntry_Object=MibTableRow
pm254dMesrlineRxpwrMeasEntry=_Pm254dMesrlineRxpwrMeasEntry_Object((1,3,6,1,4,1,20044,17,3,3,164,1))
pm254dMesrlineRxpwrMeasEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm254dMesrlineRxpwrMeasEntry.setStatus(_A)
class _Pm254dMesrlineRxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMesrlineRxpwrMeasIndex_Type.__name__=_D
_Pm254dMesrlineRxpwrMeasIndex_Object=MibTableColumn
pm254dMesrlineRxpwrMeasIndex=_Pm254dMesrlineRxpwrMeasIndex_Object((1,3,6,1,4,1,20044,17,3,3,164,1,1),_Pm254dMesrlineRxpwrMeasIndex_Type())
pm254dMesrlineRxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineRxpwrMeasIndex.setStatus(_A)
class _Pm254dMesrlineRxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm254dMesrlineRxpwrMeasPortn_Type.__name__=_D
_Pm254dMesrlineRxpwrMeasPortn_Object=MibTableColumn
pm254dMesrlineRxpwrMeasPortn=_Pm254dMesrlineRxpwrMeasPortn_Object((1,3,6,1,4,1,20044,17,3,3,164,1,2),_Pm254dMesrlineRxpwrMeasPortn_Type())
pm254dMesrlineRxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMesrlineRxpwrMeasPortn.setStatus(_A)
_Pm254dcounters_ObjectIdentity=ObjectIdentity
pm254dcounters=_Pm254dcounters_ObjectIdentity((1,3,6,1,4,1,20044,17,4))
_Pm254dCntOther_ObjectIdentity=ObjectIdentity
pm254dCntOther=_Pm254dCntOther_ObjectIdentity((1,3,6,1,4,1,20044,17,4,1))
_Pm254dCntPort_ObjectIdentity=ObjectIdentity
pm254dCntPort=_Pm254dCntPort_ObjectIdentity((1,3,6,1,4,1,20044,17,4,2))
_Pm254dCntclientUpRaRemCntTable_Object=MibTable
pm254dCntclientUpRaRemCntTable=_Pm254dCntclientUpRaRemCntTable_Object((1,3,6,1,4,1,20044,17,4,2,16))
if mibBuilder.loadTexts:pm254dCntclientUpRaRemCntTable.setStatus(_A)
_Pm254dCntclientUpRaRemCntEntry_Object=MibTableRow
pm254dCntclientUpRaRemCntEntry=_Pm254dCntclientUpRaRemCntEntry_Object((1,3,6,1,4,1,20044,17,4,2,16,1))
pm254dCntclientUpRaRemCntEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm254dCntclientUpRaRemCntEntry.setStatus(_A)
class _Pm254dCntclientUpRaRemCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntclientUpRaRemCntIndex_Type.__name__=_D
_Pm254dCntclientUpRaRemCntIndex_Object=MibTableColumn
pm254dCntclientUpRaRemCntIndex=_Pm254dCntclientUpRaRemCntIndex_Object((1,3,6,1,4,1,20044,17,4,2,16,1,1),_Pm254dCntclientUpRaRemCntIndex_Type())
pm254dCntclientUpRaRemCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaRemCntIndex.setStatus(_A)
_Pm254dCntclientUpRaRemCntValuePortn_Type=Counter32
_Pm254dCntclientUpRaRemCntValuePortn_Object=MibTableColumn
pm254dCntclientUpRaRemCntValuePortn=_Pm254dCntclientUpRaRemCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,2,16,1,2),_Pm254dCntclientUpRaRemCntValuePortn_Type())
pm254dCntclientUpRaRemCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaRemCntValuePortn.setStatus(_A)
_Pm254dCntclientUpRaRemCntErrorPortn_Type=EkiOnOff
_Pm254dCntclientUpRaRemCntErrorPortn_Object=MibTableColumn
pm254dCntclientUpRaRemCntErrorPortn=_Pm254dCntclientUpRaRemCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,2,16,1,3),_Pm254dCntclientUpRaRemCntErrorPortn_Type())
pm254dCntclientUpRaRemCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaRemCntErrorPortn.setStatus(_A)
_Pm254dCntclientUpRaRemCntOverloadPortn_Type=EkiOnOff
_Pm254dCntclientUpRaRemCntOverloadPortn_Object=MibTableColumn
pm254dCntclientUpRaRemCntOverloadPortn=_Pm254dCntclientUpRaRemCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,2,16,1,4),_Pm254dCntclientUpRaRemCntOverloadPortn_Type())
pm254dCntclientUpRaRemCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaRemCntOverloadPortn.setStatus(_A)
_Pm254dCntclientUpRaInsCntTable_Object=MibTable
pm254dCntclientUpRaInsCntTable=_Pm254dCntclientUpRaInsCntTable_Object((1,3,6,1,4,1,20044,17,4,2,24))
if mibBuilder.loadTexts:pm254dCntclientUpRaInsCntTable.setStatus(_A)
_Pm254dCntclientUpRaInsCntEntry_Object=MibTableRow
pm254dCntclientUpRaInsCntEntry=_Pm254dCntclientUpRaInsCntEntry_Object((1,3,6,1,4,1,20044,17,4,2,24,1))
pm254dCntclientUpRaInsCntEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm254dCntclientUpRaInsCntEntry.setStatus(_A)
class _Pm254dCntclientUpRaInsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntclientUpRaInsCntIndex_Type.__name__=_D
_Pm254dCntclientUpRaInsCntIndex_Object=MibTableColumn
pm254dCntclientUpRaInsCntIndex=_Pm254dCntclientUpRaInsCntIndex_Object((1,3,6,1,4,1,20044,17,4,2,24,1,1),_Pm254dCntclientUpRaInsCntIndex_Type())
pm254dCntclientUpRaInsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaInsCntIndex.setStatus(_A)
_Pm254dCntclientUpRaInsCntValuePortn_Type=Counter32
_Pm254dCntclientUpRaInsCntValuePortn_Object=MibTableColumn
pm254dCntclientUpRaInsCntValuePortn=_Pm254dCntclientUpRaInsCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,2,24,1,2),_Pm254dCntclientUpRaInsCntValuePortn_Type())
pm254dCntclientUpRaInsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaInsCntValuePortn.setStatus(_A)
_Pm254dCntclientUpRaInsCntErrorPortn_Type=EkiOnOff
_Pm254dCntclientUpRaInsCntErrorPortn_Object=MibTableColumn
pm254dCntclientUpRaInsCntErrorPortn=_Pm254dCntclientUpRaInsCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,2,24,1,3),_Pm254dCntclientUpRaInsCntErrorPortn_Type())
pm254dCntclientUpRaInsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaInsCntErrorPortn.setStatus(_A)
_Pm254dCntclientUpRaInsCntOverloadPortn_Type=EkiOnOff
_Pm254dCntclientUpRaInsCntOverloadPortn_Object=MibTableColumn
pm254dCntclientUpRaInsCntOverloadPortn=_Pm254dCntclientUpRaInsCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,2,24,1,4),_Pm254dCntclientUpRaInsCntOverloadPortn_Type())
pm254dCntclientUpRaInsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpRaInsCntOverloadPortn.setStatus(_A)
_Pm254dCntclientUpDispErrCntTable_Object=MibTable
pm254dCntclientUpDispErrCntTable=_Pm254dCntclientUpDispErrCntTable_Object((1,3,6,1,4,1,20044,17,4,2,32))
if mibBuilder.loadTexts:pm254dCntclientUpDispErrCntTable.setStatus(_A)
_Pm254dCntclientUpDispErrCntEntry_Object=MibTableRow
pm254dCntclientUpDispErrCntEntry=_Pm254dCntclientUpDispErrCntEntry_Object((1,3,6,1,4,1,20044,17,4,2,32,1))
pm254dCntclientUpDispErrCntEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm254dCntclientUpDispErrCntEntry.setStatus(_A)
class _Pm254dCntclientUpDispErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntclientUpDispErrCntIndex_Type.__name__=_D
_Pm254dCntclientUpDispErrCntIndex_Object=MibTableColumn
pm254dCntclientUpDispErrCntIndex=_Pm254dCntclientUpDispErrCntIndex_Object((1,3,6,1,4,1,20044,17,4,2,32,1,1),_Pm254dCntclientUpDispErrCntIndex_Type())
pm254dCntclientUpDispErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpDispErrCntIndex.setStatus(_A)
_Pm254dCntclientUpDispErrCntValuePortn_Type=Counter32
_Pm254dCntclientUpDispErrCntValuePortn_Object=MibTableColumn
pm254dCntclientUpDispErrCntValuePortn=_Pm254dCntclientUpDispErrCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,2,32,1,2),_Pm254dCntclientUpDispErrCntValuePortn_Type())
pm254dCntclientUpDispErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpDispErrCntValuePortn.setStatus(_A)
_Pm254dCntclientUpDispErrCntErrorPortn_Type=EkiOnOff
_Pm254dCntclientUpDispErrCntErrorPortn_Object=MibTableColumn
pm254dCntclientUpDispErrCntErrorPortn=_Pm254dCntclientUpDispErrCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,2,32,1,3),_Pm254dCntclientUpDispErrCntErrorPortn_Type())
pm254dCntclientUpDispErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpDispErrCntErrorPortn.setStatus(_A)
_Pm254dCntclientUpDispErrCntOverloadPortn_Type=EkiOnOff
_Pm254dCntclientUpDispErrCntOverloadPortn_Object=MibTableColumn
pm254dCntclientUpDispErrCntOverloadPortn=_Pm254dCntclientUpDispErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,2,32,1,4),_Pm254dCntclientUpDispErrCntOverloadPortn_Type())
pm254dCntclientUpDispErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpDispErrCntOverloadPortn.setStatus(_A)
_Pm254dCntclientUpTimCntTable_Object=MibTable
pm254dCntclientUpTimCntTable=_Pm254dCntclientUpTimCntTable_Object((1,3,6,1,4,1,20044,17,4,2,40))
if mibBuilder.loadTexts:pm254dCntclientUpTimCntTable.setStatus(_A)
_Pm254dCntclientUpTimCntEntry_Object=MibTableRow
pm254dCntclientUpTimCntEntry=_Pm254dCntclientUpTimCntEntry_Object((1,3,6,1,4,1,20044,17,4,2,40,1))
pm254dCntclientUpTimCntEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm254dCntclientUpTimCntEntry.setStatus(_A)
class _Pm254dCntclientUpTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntclientUpTimCntIndex_Type.__name__=_D
_Pm254dCntclientUpTimCntIndex_Object=MibTableColumn
pm254dCntclientUpTimCntIndex=_Pm254dCntclientUpTimCntIndex_Object((1,3,6,1,4,1,20044,17,4,2,40,1,1),_Pm254dCntclientUpTimCntIndex_Type())
pm254dCntclientUpTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpTimCntIndex.setStatus(_A)
_Pm254dCntclientUpTimCntValuePortn_Type=Counter32
_Pm254dCntclientUpTimCntValuePortn_Object=MibTableColumn
pm254dCntclientUpTimCntValuePortn=_Pm254dCntclientUpTimCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,2,40,1,2),_Pm254dCntclientUpTimCntValuePortn_Type())
pm254dCntclientUpTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpTimCntValuePortn.setStatus(_A)
_Pm254dCntclientUpTimCntErrorPortn_Type=EkiOnOff
_Pm254dCntclientUpTimCntErrorPortn_Object=MibTableColumn
pm254dCntclientUpTimCntErrorPortn=_Pm254dCntclientUpTimCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,2,40,1,3),_Pm254dCntclientUpTimCntErrorPortn_Type())
pm254dCntclientUpTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpTimCntErrorPortn.setStatus(_A)
_Pm254dCntclientUpTimCntOverloadPortn_Type=EkiOnOff
_Pm254dCntclientUpTimCntOverloadPortn_Object=MibTableColumn
pm254dCntclientUpTimCntOverloadPortn=_Pm254dCntclientUpTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,2,40,1,4),_Pm254dCntclientUpTimCntOverloadPortn_Type())
pm254dCntclientUpTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientUpTimCntOverloadPortn.setStatus(_A)
_Pm254dCntclientDwCbipCntTable_Object=MibTable
pm254dCntclientDwCbipCntTable=_Pm254dCntclientDwCbipCntTable_Object((1,3,6,1,4,1,20044,17,4,2,64))
if mibBuilder.loadTexts:pm254dCntclientDwCbipCntTable.setStatus(_A)
_Pm254dCntclientDwCbipCntEntry_Object=MibTableRow
pm254dCntclientDwCbipCntEntry=_Pm254dCntclientDwCbipCntEntry_Object((1,3,6,1,4,1,20044,17,4,2,64,1))
pm254dCntclientDwCbipCntEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm254dCntclientDwCbipCntEntry.setStatus(_A)
class _Pm254dCntclientDwCbipCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntclientDwCbipCntIndex_Type.__name__=_D
_Pm254dCntclientDwCbipCntIndex_Object=MibTableColumn
pm254dCntclientDwCbipCntIndex=_Pm254dCntclientDwCbipCntIndex_Object((1,3,6,1,4,1,20044,17,4,2,64,1,1),_Pm254dCntclientDwCbipCntIndex_Type())
pm254dCntclientDwCbipCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwCbipCntIndex.setStatus(_A)
_Pm254dCntclientDwCbipCntValuePortn_Type=Counter32
_Pm254dCntclientDwCbipCntValuePortn_Object=MibTableColumn
pm254dCntclientDwCbipCntValuePortn=_Pm254dCntclientDwCbipCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,2,64,1,2),_Pm254dCntclientDwCbipCntValuePortn_Type())
pm254dCntclientDwCbipCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwCbipCntValuePortn.setStatus(_A)
_Pm254dCntclientDwCbipCntErrorPortn_Type=EkiOnOff
_Pm254dCntclientDwCbipCntErrorPortn_Object=MibTableColumn
pm254dCntclientDwCbipCntErrorPortn=_Pm254dCntclientDwCbipCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,2,64,1,3),_Pm254dCntclientDwCbipCntErrorPortn_Type())
pm254dCntclientDwCbipCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwCbipCntErrorPortn.setStatus(_A)
_Pm254dCntclientDwCbipCntOverloadPortn_Type=EkiOnOff
_Pm254dCntclientDwCbipCntOverloadPortn_Object=MibTableColumn
pm254dCntclientDwCbipCntOverloadPortn=_Pm254dCntclientDwCbipCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,2,64,1,4),_Pm254dCntclientDwCbipCntOverloadPortn_Type())
pm254dCntclientDwCbipCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwCbipCntOverloadPortn.setStatus(_A)
_Pm254dCntclientDwTimCntTable_Object=MibTable
pm254dCntclientDwTimCntTable=_Pm254dCntclientDwTimCntTable_Object((1,3,6,1,4,1,20044,17,4,2,72))
if mibBuilder.loadTexts:pm254dCntclientDwTimCntTable.setStatus(_A)
_Pm254dCntclientDwTimCntEntry_Object=MibTableRow
pm254dCntclientDwTimCntEntry=_Pm254dCntclientDwTimCntEntry_Object((1,3,6,1,4,1,20044,17,4,2,72,1))
pm254dCntclientDwTimCntEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm254dCntclientDwTimCntEntry.setStatus(_A)
class _Pm254dCntclientDwTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntclientDwTimCntIndex_Type.__name__=_D
_Pm254dCntclientDwTimCntIndex_Object=MibTableColumn
pm254dCntclientDwTimCntIndex=_Pm254dCntclientDwTimCntIndex_Object((1,3,6,1,4,1,20044,17,4,2,72,1,1),_Pm254dCntclientDwTimCntIndex_Type())
pm254dCntclientDwTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwTimCntIndex.setStatus(_A)
_Pm254dCntclientDwTimCntValuePortn_Type=Counter32
_Pm254dCntclientDwTimCntValuePortn_Object=MibTableColumn
pm254dCntclientDwTimCntValuePortn=_Pm254dCntclientDwTimCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,2,72,1,2),_Pm254dCntclientDwTimCntValuePortn_Type())
pm254dCntclientDwTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwTimCntValuePortn.setStatus(_A)
_Pm254dCntclientDwTimCntErrorPortn_Type=EkiOnOff
_Pm254dCntclientDwTimCntErrorPortn_Object=MibTableColumn
pm254dCntclientDwTimCntErrorPortn=_Pm254dCntclientDwTimCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,2,72,1,3),_Pm254dCntclientDwTimCntErrorPortn_Type())
pm254dCntclientDwTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwTimCntErrorPortn.setStatus(_A)
_Pm254dCntclientDwTimCntOverloadPortn_Type=EkiOnOff
_Pm254dCntclientDwTimCntOverloadPortn_Object=MibTableColumn
pm254dCntclientDwTimCntOverloadPortn=_Pm254dCntclientDwTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,2,72,1,4),_Pm254dCntclientDwTimCntOverloadPortn_Type())
pm254dCntclientDwTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntclientDwTimCntOverloadPortn.setStatus(_A)
_Pm254dCntLine_ObjectIdentity=ObjectIdentity
pm254dCntLine=_Pm254dCntLine_ObjectIdentity((1,3,6,1,4,1,20044,17,4,3))
_Pm254dCntlineDfrmB1ErrCntTable_Object=MibTable
pm254dCntlineDfrmB1ErrCntTable=_Pm254dCntlineDfrmB1ErrCntTable_Object((1,3,6,1,4,1,20044,17,4,3,152))
if mibBuilder.loadTexts:pm254dCntlineDfrmB1ErrCntTable.setStatus(_A)
_Pm254dCntlineDfrmB1ErrCntEntry_Object=MibTableRow
pm254dCntlineDfrmB1ErrCntEntry=_Pm254dCntlineDfrmB1ErrCntEntry_Object((1,3,6,1,4,1,20044,17,4,3,152,1))
pm254dCntlineDfrmB1ErrCntEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm254dCntlineDfrmB1ErrCntEntry.setStatus(_A)
class _Pm254dCntlineDfrmB1ErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntlineDfrmB1ErrCntIndex_Type.__name__=_D
_Pm254dCntlineDfrmB1ErrCntIndex_Object=MibTableColumn
pm254dCntlineDfrmB1ErrCntIndex=_Pm254dCntlineDfrmB1ErrCntIndex_Object((1,3,6,1,4,1,20044,17,4,3,152,1,1),_Pm254dCntlineDfrmB1ErrCntIndex_Type())
pm254dCntlineDfrmB1ErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmB1ErrCntIndex.setStatus(_A)
_Pm254dCntlineDfrmB1ErrCntValuePortn_Type=Counter32
_Pm254dCntlineDfrmB1ErrCntValuePortn_Object=MibTableColumn
pm254dCntlineDfrmB1ErrCntValuePortn=_Pm254dCntlineDfrmB1ErrCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,3,152,1,2),_Pm254dCntlineDfrmB1ErrCntValuePortn_Type())
pm254dCntlineDfrmB1ErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmB1ErrCntValuePortn.setStatus(_A)
_Pm254dCntlineDfrmB1ErrCntErrorPortn_Type=EkiOnOff
_Pm254dCntlineDfrmB1ErrCntErrorPortn_Object=MibTableColumn
pm254dCntlineDfrmB1ErrCntErrorPortn=_Pm254dCntlineDfrmB1ErrCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,3,152,1,3),_Pm254dCntlineDfrmB1ErrCntErrorPortn_Type())
pm254dCntlineDfrmB1ErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmB1ErrCntErrorPortn.setStatus(_A)
_Pm254dCntlineDfrmB1ErrCntOverloadPortn_Type=EkiOnOff
_Pm254dCntlineDfrmB1ErrCntOverloadPortn_Object=MibTableColumn
pm254dCntlineDfrmB1ErrCntOverloadPortn=_Pm254dCntlineDfrmB1ErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,3,152,1,4),_Pm254dCntlineDfrmB1ErrCntOverloadPortn_Type())
pm254dCntlineDfrmB1ErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmB1ErrCntOverloadPortn.setStatus(_A)
_Pm254dCntlineDfrmTimCntTable_Object=MibTable
pm254dCntlineDfrmTimCntTable=_Pm254dCntlineDfrmTimCntTable_Object((1,3,6,1,4,1,20044,17,4,3,153))
if mibBuilder.loadTexts:pm254dCntlineDfrmTimCntTable.setStatus(_A)
_Pm254dCntlineDfrmTimCntEntry_Object=MibTableRow
pm254dCntlineDfrmTimCntEntry=_Pm254dCntlineDfrmTimCntEntry_Object((1,3,6,1,4,1,20044,17,4,3,153,1))
pm254dCntlineDfrmTimCntEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm254dCntlineDfrmTimCntEntry.setStatus(_A)
class _Pm254dCntlineDfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCntlineDfrmTimCntIndex_Type.__name__=_D
_Pm254dCntlineDfrmTimCntIndex_Object=MibTableColumn
pm254dCntlineDfrmTimCntIndex=_Pm254dCntlineDfrmTimCntIndex_Object((1,3,6,1,4,1,20044,17,4,3,153,1,1),_Pm254dCntlineDfrmTimCntIndex_Type())
pm254dCntlineDfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmTimCntIndex.setStatus(_A)
_Pm254dCntlineDfrmTimCntValuePortn_Type=Counter32
_Pm254dCntlineDfrmTimCntValuePortn_Object=MibTableColumn
pm254dCntlineDfrmTimCntValuePortn=_Pm254dCntlineDfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,17,4,3,153,1,2),_Pm254dCntlineDfrmTimCntValuePortn_Type())
pm254dCntlineDfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmTimCntValuePortn.setStatus(_A)
_Pm254dCntlineDfrmTimCntErrorPortn_Type=EkiOnOff
_Pm254dCntlineDfrmTimCntErrorPortn_Object=MibTableColumn
pm254dCntlineDfrmTimCntErrorPortn=_Pm254dCntlineDfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,17,4,3,153,1,3),_Pm254dCntlineDfrmTimCntErrorPortn_Type())
pm254dCntlineDfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmTimCntErrorPortn.setStatus(_A)
_Pm254dCntlineDfrmTimCntOverloadPortn_Type=EkiOnOff
_Pm254dCntlineDfrmTimCntOverloadPortn_Object=MibTableColumn
pm254dCntlineDfrmTimCntOverloadPortn=_Pm254dCntlineDfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,4,3,153,1,4),_Pm254dCntlineDfrmTimCntOverloadPortn_Type())
pm254dCntlineDfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCntlineDfrmTimCntOverloadPortn.setStatus(_A)
_Pm254dCntCountersReset_Type=EkiOnOff
_Pm254dCntCountersReset_Object=MibScalar
pm254dCntCountersReset=_Pm254dCntCountersReset_Object((1,3,6,1,4,1,20044,17,4,259),_Pm254dCntCountersReset_Type())
pm254dCntCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCntCountersReset.setStatus(_A)
_Pm254dCntCountersStop_Type=EkiOnOff
_Pm254dCntCountersStop_Object=MibScalar
pm254dCntCountersStop=_Pm254dCntCountersStop_Object((1,3,6,1,4,1,20044,17,4,260),_Pm254dCntCountersStop_Type())
pm254dCntCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCntCountersStop.setStatus(_A)
_Pm254dcontrolsWrite_ObjectIdentity=ObjectIdentity
pm254dcontrolsWrite=_Pm254dcontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,17,6))
_Pm254dCtrlOther_ObjectIdentity=ObjectIdentity
pm254dCtrlOther=_Pm254dCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1))
_Pm254dCtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pm254dCtrlconfMgnt1=_Pm254dCtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,1))
_Pm254dCtrlConf1Load1_Type=EkiOnOff
_Pm254dCtrlConf1Load1_Object=MibScalar
pm254dCtrlConf1Load1=_Pm254dCtrlConf1Load1_Object((1,3,6,1,4,1,20044,17,6,1,1,1),_Pm254dCtrlConf1Load1_Type())
pm254dCtrlConf1Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlConf1Load1.setStatus(_A)
_Pm254dCtrlConf2Load1_Type=EkiOnOff
_Pm254dCtrlConf2Load1_Object=MibScalar
pm254dCtrlConf2Load1=_Pm254dCtrlConf2Load1_Object((1,3,6,1,4,1,20044,17,6,1,1,2),_Pm254dCtrlConf2Load1_Type())
pm254dCtrlConf2Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlConf2Load1.setStatus(_A)
_Pm254dCtrlConf2Flash1_Type=EkiOnOff
_Pm254dCtrlConf2Flash1_Object=MibScalar
pm254dCtrlConf2Flash1=_Pm254dCtrlConf2Flash1_Object((1,3,6,1,4,1,20044,17,6,1,1,10),_Pm254dCtrlConf2Flash1_Type())
pm254dCtrlConf2Flash1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlConf2Flash1.setStatus(_A)
_Pm254dCtrlConf2Clear1_Type=EkiOnOff
_Pm254dCtrlConf2Clear1_Object=MibScalar
pm254dCtrlConf2Clear1=_Pm254dCtrlConf2Clear1_Object((1,3,6,1,4,1,20044,17,6,1,1,14),_Pm254dCtrlConf2Clear1_Type())
pm254dCtrlConf2Clear1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlConf2Clear1.setStatus(_A)
_Pm254dCtrlsynth4_ObjectIdentity=ObjectIdentity
pm254dCtrlsynth4=_Pm254dCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,4))
_Pm254dCtrlCorrelatOn_Type=EkiOnOff
_Pm254dCtrlCorrelatOn_Object=MibScalar
pm254dCtrlCorrelatOn=_Pm254dCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,17,6,1,4,1),_Pm254dCtrlCorrelatOn_Type())
pm254dCtrlCorrelatOn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlCorrelatOn.setStatus(_A)
_Pm254dCtrlCorrelatOff_Type=EkiOnOff
_Pm254dCtrlCorrelatOff_Object=MibScalar
pm254dCtrlCorrelatOff=_Pm254dCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,17,6,1,4,2),_Pm254dCtrlCorrelatOff_Type())
pm254dCtrlCorrelatOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlCorrelatOff.setStatus(_A)
_Pm254dCtrlswMgnt_ObjectIdentity=ObjectIdentity
pm254dCtrlswMgnt=_Pm254dCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,5))
_Pm254dCtrlColdReset_Type=EkiOnOff
_Pm254dCtrlColdReset_Object=MibScalar
pm254dCtrlColdReset=_Pm254dCtrlColdReset_Object((1,3,6,1,4,1,20044,17,6,1,5,2),_Pm254dCtrlColdReset_Type())
pm254dCtrlColdReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlColdReset.setStatus(_A)
_Pm254dCtrlWarmReset_Type=EkiOnOff
_Pm254dCtrlWarmReset_Object=MibScalar
pm254dCtrlWarmReset=_Pm254dCtrlWarmReset_Object((1,3,6,1,4,1,20044,17,6,1,5,3),_Pm254dCtrlWarmReset_Type())
pm254dCtrlWarmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlWarmReset.setStatus(_A)
_Pm254dCtrlLoadSwBank1_Type=EkiOnOff
_Pm254dCtrlLoadSwBank1_Object=MibScalar
pm254dCtrlLoadSwBank1=_Pm254dCtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,17,6,1,5,5),_Pm254dCtrlLoadSwBank1_Type())
pm254dCtrlLoadSwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLoadSwBank1.setStatus(_A)
_Pm254dCtrlLoadSwBank2_Type=EkiOnOff
_Pm254dCtrlLoadSwBank2_Object=MibScalar
pm254dCtrlLoadSwBank2=_Pm254dCtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,17,6,1,5,6),_Pm254dCtrlLoadSwBank2_Type())
pm254dCtrlLoadSwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLoadSwBank2.setStatus(_A)
_Pm254dCtrlgwMgnt_ObjectIdentity=ObjectIdentity
pm254dCtrlgwMgnt=_Pm254dCtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,6))
_Pm254dCtrlCurrentGwReset_Type=EkiOnOff
_Pm254dCtrlCurrentGwReset_Object=MibScalar
pm254dCtrlCurrentGwReset=_Pm254dCtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,17,6,1,6,1),_Pm254dCtrlCurrentGwReset_Type())
pm254dCtrlCurrentGwReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlCurrentGwReset.setStatus(_A)
_Pm254dCtrlLoadGwBank1_Type=EkiOnOff
_Pm254dCtrlLoadGwBank1_Object=MibScalar
pm254dCtrlLoadGwBank1=_Pm254dCtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,17,6,1,6,5),_Pm254dCtrlLoadGwBank1_Type())
pm254dCtrlLoadGwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLoadGwBank1.setStatus(_A)
_Pm254dCtrlLoadGwBank2_Type=EkiOnOff
_Pm254dCtrlLoadGwBank2_Object=MibScalar
pm254dCtrlLoadGwBank2=_Pm254dCtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,17,6,1,6,6),_Pm254dCtrlLoadGwBank2_Type())
pm254dCtrlLoadGwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLoadGwBank2.setStatus(_A)
_Pm254dCtrlLoadGwBank3_Type=EkiOnOff
_Pm254dCtrlLoadGwBank3_Object=MibScalar
pm254dCtrlLoadGwBank3=_Pm254dCtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,17,6,1,6,7),_Pm254dCtrlLoadGwBank3_Type())
pm254dCtrlLoadGwBank3.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLoadGwBank3.setStatus(_A)
_Pm254dCtrlLoadGwBank4_Type=EkiOnOff
_Pm254dCtrlLoadGwBank4_Object=MibScalar
pm254dCtrlLoadGwBank4=_Pm254dCtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,17,6,1,6,8),_Pm254dCtrlLoadGwBank4_Type())
pm254dCtrlLoadGwBank4.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLoadGwBank4.setStatus(_A)
_Pm254dCtrlledTest_ObjectIdentity=ObjectIdentity
pm254dCtrlledTest=_Pm254dCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,192))
_Pm254dCtrlGreenLed_Type=EkiOnOff
_Pm254dCtrlGreenLed_Object=MibScalar
pm254dCtrlGreenLed=_Pm254dCtrlGreenLed_Object((1,3,6,1,4,1,20044,17,6,1,192,1),_Pm254dCtrlGreenLed_Type())
pm254dCtrlGreenLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlGreenLed.setStatus(_A)
_Pm254dCtrlRedLed_Type=EkiOnOff
_Pm254dCtrlRedLed_Object=MibScalar
pm254dCtrlRedLed=_Pm254dCtrlRedLed_Object((1,3,6,1,4,1,20044,17,6,1,192,2),_Pm254dCtrlRedLed_Type())
pm254dCtrlRedLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlRedLed.setStatus(_A)
_Pm254dCtrlLedOff_Type=EkiOnOff
_Pm254dCtrlLedOff_Object=MibScalar
pm254dCtrlLedOff=_Pm254dCtrlLedOff_Object((1,3,6,1,4,1,20044,17,6,1,192,3),_Pm254dCtrlLedOff_Type())
pm254dCtrlLedOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLedOff.setStatus(_A)
_Pm254dCtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm254dCtrlmoduleOosMode=_Pm254dCtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,193))
_Pm254dCtrlModuleOosMode_Type=EkiOnOff
_Pm254dCtrlModuleOosMode_Object=MibScalar
pm254dCtrlModuleOosMode=_Pm254dCtrlModuleOosMode_Object((1,3,6,1,4,1,20044,17,6,1,193,1),_Pm254dCtrlModuleOosMode_Type())
pm254dCtrlModuleOosMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlModuleOosMode.setStatus(_A)
_Pm254dCtrlmaintenanceMode_ObjectIdentity=ObjectIdentity
pm254dCtrlmaintenanceMode=_Pm254dCtrlmaintenanceMode_ObjectIdentity((1,3,6,1,4,1,20044,17,6,1,197))
_Pm254dCtrlMaintenanceMode_Type=EkiOnOff
_Pm254dCtrlMaintenanceMode_Object=MibScalar
pm254dCtrlMaintenanceMode=_Pm254dCtrlMaintenanceMode_Object((1,3,6,1,4,1,20044,17,6,1,197,1),_Pm254dCtrlMaintenanceMode_Type())
pm254dCtrlMaintenanceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlMaintenanceMode.setStatus(_A)
_Pm254dCtrlPort_ObjectIdentity=ObjectIdentity
pm254dCtrlPort=_Pm254dCtrlPort_ObjectIdentity((1,3,6,1,4,1,20044,17,6,2))
_Pm254dCtrlclientAccessLoopTable_Object=MibTable
pm254dCtrlclientAccessLoopTable=_Pm254dCtrlclientAccessLoopTable_Object((1,3,6,1,4,1,20044,17,6,2,16))
if mibBuilder.loadTexts:pm254dCtrlclientAccessLoopTable.setStatus(_A)
_Pm254dCtrlclientAccessLoopEntry_Object=MibTableRow
pm254dCtrlclientAccessLoopEntry=_Pm254dCtrlclientAccessLoopEntry_Object((1,3,6,1,4,1,20044,17,6,2,16,1))
pm254dCtrlclientAccessLoopEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm254dCtrlclientAccessLoopEntry.setStatus(_A)
class _Pm254dCtrlclientAccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlclientAccessLoopIndex_Type.__name__=_D
_Pm254dCtrlclientAccessLoopIndex_Object=MibTableColumn
pm254dCtrlclientAccessLoopIndex=_Pm254dCtrlclientAccessLoopIndex_Object((1,3,6,1,4,1,20044,17,6,2,16,1,1),_Pm254dCtrlclientAccessLoopIndex_Type())
pm254dCtrlclientAccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlclientAccessLoopIndex.setStatus(_A)
_Pm254dCtrlclientAccessLoopPortn_Type=EkiState
_Pm254dCtrlclientAccessLoopPortn_Object=MibTableColumn
pm254dCtrlclientAccessLoopPortn=_Pm254dCtrlclientAccessLoopPortn_Object((1,3,6,1,4,1,20044,17,6,2,16,1,2),_Pm254dCtrlclientAccessLoopPortn_Type())
pm254dCtrlclientAccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlclientAccessLoopPortn.setStatus(_A)
_Pm254dCtrlclientOosModeTable_Object=MibTable
pm254dCtrlclientOosModeTable=_Pm254dCtrlclientOosModeTable_Object((1,3,6,1,4,1,20044,17,6,2,18))
if mibBuilder.loadTexts:pm254dCtrlclientOosModeTable.setStatus(_A)
_Pm254dCtrlclientOosModeEntry_Object=MibTableRow
pm254dCtrlclientOosModeEntry=_Pm254dCtrlclientOosModeEntry_Object((1,3,6,1,4,1,20044,17,6,2,18,1))
pm254dCtrlclientOosModeEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm254dCtrlclientOosModeEntry.setStatus(_A)
class _Pm254dCtrlclientOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlclientOosModeIndex_Type.__name__=_D
_Pm254dCtrlclientOosModeIndex_Object=MibTableColumn
pm254dCtrlclientOosModeIndex=_Pm254dCtrlclientOosModeIndex_Object((1,3,6,1,4,1,20044,17,6,2,18,1,1),_Pm254dCtrlclientOosModeIndex_Type())
pm254dCtrlclientOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlclientOosModeIndex.setStatus(_A)
_Pm254dCtrlclientOosModePortn_Type=EkiState
_Pm254dCtrlclientOosModePortn_Object=MibTableColumn
pm254dCtrlclientOosModePortn=_Pm254dCtrlclientOosModePortn_Object((1,3,6,1,4,1,20044,17,6,2,18,1,2),_Pm254dCtrlclientOosModePortn_Type())
pm254dCtrlclientOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlclientOosModePortn.setStatus(_A)
_Pm254dCtrlclientSfpOnOffCtrlTable_Object=MibTable
pm254dCtrlclientSfpOnOffCtrlTable=_Pm254dCtrlclientSfpOnOffCtrlTable_Object((1,3,6,1,4,1,20044,17,6,2,20))
if mibBuilder.loadTexts:pm254dCtrlclientSfpOnOffCtrlTable.setStatus(_A)
_Pm254dCtrlclientSfpOnOffCtrlEntry_Object=MibTableRow
pm254dCtrlclientSfpOnOffCtrlEntry=_Pm254dCtrlclientSfpOnOffCtrlEntry_Object((1,3,6,1,4,1,20044,17,6,2,20,1))
pm254dCtrlclientSfpOnOffCtrlEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm254dCtrlclientSfpOnOffCtrlEntry.setStatus(_A)
class _Pm254dCtrlclientSfpOnOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlclientSfpOnOffCtrlIndex_Type.__name__=_D
_Pm254dCtrlclientSfpOnOffCtrlIndex_Object=MibTableColumn
pm254dCtrlclientSfpOnOffCtrlIndex=_Pm254dCtrlclientSfpOnOffCtrlIndex_Object((1,3,6,1,4,1,20044,17,6,2,20,1,1),_Pm254dCtrlclientSfpOnOffCtrlIndex_Type())
pm254dCtrlclientSfpOnOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlclientSfpOnOffCtrlIndex.setStatus(_A)
_Pm254dCtrlclientSfpOnOffCtrlPortn_Type=EkiState
_Pm254dCtrlclientSfpOnOffCtrlPortn_Object=MibTableColumn
pm254dCtrlclientSfpOnOffCtrlPortn=_Pm254dCtrlclientSfpOnOffCtrlPortn_Object((1,3,6,1,4,1,20044,17,6,2,20,1,2),_Pm254dCtrlclientSfpOnOffCtrlPortn_Type())
pm254dCtrlclientSfpOnOffCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlclientSfpOnOffCtrlPortn.setStatus(_A)
_Pm254dCtrlclientCsfUpInsTable_Object=MibTable
pm254dCtrlclientCsfUpInsTable=_Pm254dCtrlclientCsfUpInsTable_Object((1,3,6,1,4,1,20044,17,6,2,21))
if mibBuilder.loadTexts:pm254dCtrlclientCsfUpInsTable.setStatus(_A)
_Pm254dCtrlclientCsfUpInsEntry_Object=MibTableRow
pm254dCtrlclientCsfUpInsEntry=_Pm254dCtrlclientCsfUpInsEntry_Object((1,3,6,1,4,1,20044,17,6,2,21,1))
pm254dCtrlclientCsfUpInsEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm254dCtrlclientCsfUpInsEntry.setStatus(_A)
class _Pm254dCtrlclientCsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlclientCsfUpInsIndex_Type.__name__=_D
_Pm254dCtrlclientCsfUpInsIndex_Object=MibTableColumn
pm254dCtrlclientCsfUpInsIndex=_Pm254dCtrlclientCsfUpInsIndex_Object((1,3,6,1,4,1,20044,17,6,2,21,1,1),_Pm254dCtrlclientCsfUpInsIndex_Type())
pm254dCtrlclientCsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlclientCsfUpInsIndex.setStatus(_A)
_Pm254dCtrlclientCsfUpInsPortn_Type=EkiState
_Pm254dCtrlclientCsfUpInsPortn_Object=MibTableColumn
pm254dCtrlclientCsfUpInsPortn=_Pm254dCtrlclientCsfUpInsPortn_Object((1,3,6,1,4,1,20044,17,6,2,21,1,2),_Pm254dCtrlclientCsfUpInsPortn_Type())
pm254dCtrlclientCsfUpInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlclientCsfUpInsPortn.setStatus(_A)
_Pm254dCtrlclientCaisDwInsTable_Object=MibTable
pm254dCtrlclientCaisDwInsTable=_Pm254dCtrlclientCaisDwInsTable_Object((1,3,6,1,4,1,20044,17,6,2,22))
if mibBuilder.loadTexts:pm254dCtrlclientCaisDwInsTable.setStatus(_A)
_Pm254dCtrlclientCaisDwInsEntry_Object=MibTableRow
pm254dCtrlclientCaisDwInsEntry=_Pm254dCtrlclientCaisDwInsEntry_Object((1,3,6,1,4,1,20044,17,6,2,22,1))
pm254dCtrlclientCaisDwInsEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm254dCtrlclientCaisDwInsEntry.setStatus(_A)
class _Pm254dCtrlclientCaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlclientCaisDwInsIndex_Type.__name__=_D
_Pm254dCtrlclientCaisDwInsIndex_Object=MibTableColumn
pm254dCtrlclientCaisDwInsIndex=_Pm254dCtrlclientCaisDwInsIndex_Object((1,3,6,1,4,1,20044,17,6,2,22,1,1),_Pm254dCtrlclientCaisDwInsIndex_Type())
pm254dCtrlclientCaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlclientCaisDwInsIndex.setStatus(_A)
_Pm254dCtrlclientCaisDwInsPortn_Type=EkiState
_Pm254dCtrlclientCaisDwInsPortn_Object=MibTableColumn
pm254dCtrlclientCaisDwInsPortn=_Pm254dCtrlclientCaisDwInsPortn_Object((1,3,6,1,4,1,20044,17,6,2,22,1,2),_Pm254dCtrlclientCaisDwInsPortn_Type())
pm254dCtrlclientCaisDwInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlclientCaisDwInsPortn.setStatus(_A)
_Pm254dCtrlclientAccessTermLoopTable_Object=MibTable
pm254dCtrlclientAccessTermLoopTable=_Pm254dCtrlclientAccessTermLoopTable_Object((1,3,6,1,4,1,20044,17,6,2,26))
if mibBuilder.loadTexts:pm254dCtrlclientAccessTermLoopTable.setStatus(_A)
_Pm254dCtrlclientAccessTermLoopEntry_Object=MibTableRow
pm254dCtrlclientAccessTermLoopEntry=_Pm254dCtrlclientAccessTermLoopEntry_Object((1,3,6,1,4,1,20044,17,6,2,26,1))
pm254dCtrlclientAccessTermLoopEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm254dCtrlclientAccessTermLoopEntry.setStatus(_A)
class _Pm254dCtrlclientAccessTermLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlclientAccessTermLoopIndex_Type.__name__=_D
_Pm254dCtrlclientAccessTermLoopIndex_Object=MibTableColumn
pm254dCtrlclientAccessTermLoopIndex=_Pm254dCtrlclientAccessTermLoopIndex_Object((1,3,6,1,4,1,20044,17,6,2,26,1,1),_Pm254dCtrlclientAccessTermLoopIndex_Type())
pm254dCtrlclientAccessTermLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlclientAccessTermLoopIndex.setStatus(_A)
_Pm254dCtrlclientAccessTermLoopPortn_Type=EkiState
_Pm254dCtrlclientAccessTermLoopPortn_Object=MibTableColumn
pm254dCtrlclientAccessTermLoopPortn=_Pm254dCtrlclientAccessTermLoopPortn_Object((1,3,6,1,4,1,20044,17,6,2,26,1,2),_Pm254dCtrlclientAccessTermLoopPortn_Type())
pm254dCtrlclientAccessTermLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlclientAccessTermLoopPortn.setStatus(_A)
_Pm254dCtrlProtocolTable_Object=MibTable
pm254dCtrlProtocolTable=_Pm254dCtrlProtocolTable_Object((1,3,6,1,4,1,20044,17,6,2,48))
if mibBuilder.loadTexts:pm254dCtrlProtocolTable.setStatus(_A)
_Pm254dCtrlProtocolEntry_Object=MibTableRow
pm254dCtrlProtocolEntry=_Pm254dCtrlProtocolEntry_Object((1,3,6,1,4,1,20044,17,6,2,48,1))
pm254dCtrlProtocolEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pm254dCtrlProtocolEntry.setStatus(_A)
class _Pm254dCtrlProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrlProtocolIndex_Type.__name__=_D
_Pm254dCtrlProtocolIndex_Object=MibTableColumn
pm254dCtrlProtocolIndex=_Pm254dCtrlProtocolIndex_Object((1,3,6,1,4,1,20044,17,6,2,48,1,1),_Pm254dCtrlProtocolIndex_Type())
pm254dCtrlProtocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrlProtocolIndex.setStatus(_A)
_Pm254dCtrlProtocolPortn_Type=EkiProtocol
_Pm254dCtrlProtocolPortn_Object=MibTableColumn
pm254dCtrlProtocolPortn=_Pm254dCtrlProtocolPortn_Object((1,3,6,1,4,1,20044,17,6,2,48,1,2),_Pm254dCtrlProtocolPortn_Type())
pm254dCtrlProtocolPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlProtocolPortn.setStatus(_A)
_Pm254dCtrlLine_ObjectIdentity=ObjectIdentity
pm254dCtrlLine=_Pm254dCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,17,6,3))
_Pm254dCtrllineMsAis_ObjectIdentity=ObjectIdentity
pm254dCtrllineMsAis=_Pm254dCtrllineMsAis_ObjectIdentity((1,3,6,1,4,1,20044,17,6,3,67))
_Pm254dCtrlLineMsAis_Type=EkiOnOff
_Pm254dCtrlLineMsAis_Object=MibScalar
pm254dCtrlLineMsAis=_Pm254dCtrlLineMsAis_Object((1,3,6,1,4,1,20044,17,6,3,67,1),_Pm254dCtrlLineMsAis_Type())
pm254dCtrlLineMsAis.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLineMsAis.setStatus(_A)
_Pm254dCtrllineUpS1Table_Object=MibTable
pm254dCtrllineUpS1Table=_Pm254dCtrllineUpS1Table_Object((1,3,6,1,4,1,20044,17,6,3,70))
if mibBuilder.loadTexts:pm254dCtrllineUpS1Table.setStatus(_A)
_Pm254dCtrllineUpS1Entry_Object=MibTableRow
pm254dCtrllineUpS1Entry=_Pm254dCtrllineUpS1Entry_Object((1,3,6,1,4,1,20044,17,6,3,70,1))
pm254dCtrllineUpS1Entry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pm254dCtrllineUpS1Entry.setStatus(_A)
class _Pm254dCtrllineUpS1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineUpS1Index_Type.__name__=_D
_Pm254dCtrllineUpS1Index_Object=MibTableColumn
pm254dCtrllineUpS1Index=_Pm254dCtrllineUpS1Index_Object((1,3,6,1,4,1,20044,17,6,3,70,1,1),_Pm254dCtrllineUpS1Index_Type())
pm254dCtrllineUpS1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineUpS1Index.setStatus(_A)
class _Pm254dCtrllineUpS1Portn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pm254dCtrllineUpS1Portn_Type.__name__=_D
_Pm254dCtrllineUpS1Portn_Object=MibTableColumn
pm254dCtrllineUpS1Portn=_Pm254dCtrllineUpS1Portn_Object((1,3,6,1,4,1,20044,17,6,3,70,1,2),_Pm254dCtrllineUpS1Portn_Type())
pm254dCtrllineUpS1Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineUpS1Portn.setStatus(_A)
_Pm254dCtrllineUpK1Table_Object=MibTable
pm254dCtrllineUpK1Table=_Pm254dCtrllineUpK1Table_Object((1,3,6,1,4,1,20044,17,6,3,71))
if mibBuilder.loadTexts:pm254dCtrllineUpK1Table.setStatus(_A)
_Pm254dCtrllineUpK1Entry_Object=MibTableRow
pm254dCtrllineUpK1Entry=_Pm254dCtrllineUpK1Entry_Object((1,3,6,1,4,1,20044,17,6,3,71,1))
pm254dCtrllineUpK1Entry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pm254dCtrllineUpK1Entry.setStatus(_A)
class _Pm254dCtrllineUpK1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineUpK1Index_Type.__name__=_D
_Pm254dCtrllineUpK1Index_Object=MibTableColumn
pm254dCtrllineUpK1Index=_Pm254dCtrllineUpK1Index_Object((1,3,6,1,4,1,20044,17,6,3,71,1,1),_Pm254dCtrllineUpK1Index_Type())
pm254dCtrllineUpK1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineUpK1Index.setStatus(_A)
class _Pm254dCtrllineUpK1Portn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pm254dCtrllineUpK1Portn_Type.__name__=_D
_Pm254dCtrllineUpK1Portn_Object=MibTableColumn
pm254dCtrllineUpK1Portn=_Pm254dCtrllineUpK1Portn_Object((1,3,6,1,4,1,20044,17,6,3,71,1,2),_Pm254dCtrllineUpK1Portn_Type())
pm254dCtrllineUpK1Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineUpK1Portn.setStatus(_A)
_Pm254dCtrllineUpK2Table_Object=MibTable
pm254dCtrllineUpK2Table=_Pm254dCtrllineUpK2Table_Object((1,3,6,1,4,1,20044,17,6,3,72))
if mibBuilder.loadTexts:pm254dCtrllineUpK2Table.setStatus(_A)
_Pm254dCtrllineUpK2Entry_Object=MibTableRow
pm254dCtrllineUpK2Entry=_Pm254dCtrllineUpK2Entry_Object((1,3,6,1,4,1,20044,17,6,3,72,1))
pm254dCtrllineUpK2Entry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pm254dCtrllineUpK2Entry.setStatus(_A)
class _Pm254dCtrllineUpK2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineUpK2Index_Type.__name__=_D
_Pm254dCtrllineUpK2Index_Object=MibTableColumn
pm254dCtrllineUpK2Index=_Pm254dCtrllineUpK2Index_Object((1,3,6,1,4,1,20044,17,6,3,72,1,1),_Pm254dCtrllineUpK2Index_Type())
pm254dCtrllineUpK2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineUpK2Index.setStatus(_A)
class _Pm254dCtrllineUpK2Portn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pm254dCtrllineUpK2Portn_Type.__name__=_D
_Pm254dCtrllineUpK2Portn_Object=MibTableColumn
pm254dCtrllineUpK2Portn=_Pm254dCtrllineUpK2Portn_Object((1,3,6,1,4,1,20044,17,6,3,72,1,2),_Pm254dCtrllineUpK2Portn_Type())
pm254dCtrllineUpK2Portn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineUpK2Portn.setStatus(_A)
_Pm254dCtrllineOosModeTable_Object=MibTable
pm254dCtrllineOosModeTable=_Pm254dCtrllineOosModeTable_Object((1,3,6,1,4,1,20044,17,6,3,74))
if mibBuilder.loadTexts:pm254dCtrllineOosModeTable.setStatus(_A)
_Pm254dCtrllineOosModeEntry_Object=MibTableRow
pm254dCtrllineOosModeEntry=_Pm254dCtrllineOosModeEntry_Object((1,3,6,1,4,1,20044,17,6,3,74,1))
pm254dCtrllineOosModeEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pm254dCtrllineOosModeEntry.setStatus(_A)
class _Pm254dCtrllineOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineOosModeIndex_Type.__name__=_D
_Pm254dCtrllineOosModeIndex_Object=MibTableColumn
pm254dCtrllineOosModeIndex=_Pm254dCtrllineOosModeIndex_Object((1,3,6,1,4,1,20044,17,6,3,74,1,1),_Pm254dCtrllineOosModeIndex_Type())
pm254dCtrllineOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineOosModeIndex.setStatus(_A)
_Pm254dCtrllineOosModePortn_Type=EkiState
_Pm254dCtrllineOosModePortn_Object=MibTableColumn
pm254dCtrllineOosModePortn=_Pm254dCtrllineOosModePortn_Object((1,3,6,1,4,1,20044,17,6,3,74,1,2),_Pm254dCtrllineOosModePortn_Type())
pm254dCtrllineOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineOosModePortn.setStatus(_A)
_Pm254dCtrlDccMgnt_ObjectIdentity=ObjectIdentity
pm254dCtrlDccMgnt=_Pm254dCtrlDccMgnt_ObjectIdentity((1,3,6,1,4,1,20044,17,6,3,93))
class _Pm254dCtrlLineNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pm254dCtrlLineNumber_Type.__name__=_F
_Pm254dCtrlLineNumber_Object=MibScalar
pm254dCtrlLineNumber=_Pm254dCtrlLineNumber_Object((1,3,6,1,4,1,20044,17,6,3,93,1),_Pm254dCtrlLineNumber_Type())
pm254dCtrlLineNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlLineNumber.setStatus(_A)
_Pm254dCtrlDccMode_Type=EkiMode
_Pm254dCtrlDccMode_Object=MibScalar
pm254dCtrlDccMode=_Pm254dCtrlDccMode_Object((1,3,6,1,4,1,20044,17,6,3,93,2),_Pm254dCtrlDccMode_Type())
pm254dCtrlDccMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrlDccMode.setStatus(_A)
_Pm254dCtrllineAccessLoopTable_Object=MibTable
pm254dCtrllineAccessLoopTable=_Pm254dCtrllineAccessLoopTable_Object((1,3,6,1,4,1,20044,17,6,3,160))
if mibBuilder.loadTexts:pm254dCtrllineAccessLoopTable.setStatus(_A)
_Pm254dCtrllineAccessLoopEntry_Object=MibTableRow
pm254dCtrllineAccessLoopEntry=_Pm254dCtrllineAccessLoopEntry_Object((1,3,6,1,4,1,20044,17,6,3,160,1))
pm254dCtrllineAccessLoopEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pm254dCtrllineAccessLoopEntry.setStatus(_A)
class _Pm254dCtrllineAccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineAccessLoopIndex_Type.__name__=_D
_Pm254dCtrllineAccessLoopIndex_Object=MibTableColumn
pm254dCtrllineAccessLoopIndex=_Pm254dCtrllineAccessLoopIndex_Object((1,3,6,1,4,1,20044,17,6,3,160,1,1),_Pm254dCtrllineAccessLoopIndex_Type())
pm254dCtrllineAccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineAccessLoopIndex.setStatus(_A)
_Pm254dCtrllineAccessLoopPortn_Type=EkiState
_Pm254dCtrllineAccessLoopPortn_Object=MibTableColumn
pm254dCtrllineAccessLoopPortn=_Pm254dCtrllineAccessLoopPortn_Object((1,3,6,1,4,1,20044,17,6,3,160,1,2),_Pm254dCtrllineAccessLoopPortn_Type())
pm254dCtrllineAccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineAccessLoopPortn.setStatus(_A)
_Pm254dCtrllineLoopTransceiverTable_Object=MibTable
pm254dCtrllineLoopTransceiverTable=_Pm254dCtrllineLoopTransceiverTable_Object((1,3,6,1,4,1,20044,17,6,3,161))
if mibBuilder.loadTexts:pm254dCtrllineLoopTransceiverTable.setStatus(_A)
_Pm254dCtrllineLoopTransceiverEntry_Object=MibTableRow
pm254dCtrllineLoopTransceiverEntry=_Pm254dCtrllineLoopTransceiverEntry_Object((1,3,6,1,4,1,20044,17,6,3,161,1))
pm254dCtrllineLoopTransceiverEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pm254dCtrllineLoopTransceiverEntry.setStatus(_A)
class _Pm254dCtrllineLoopTransceiverIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineLoopTransceiverIndex_Type.__name__=_D
_Pm254dCtrllineLoopTransceiverIndex_Object=MibTableColumn
pm254dCtrllineLoopTransceiverIndex=_Pm254dCtrllineLoopTransceiverIndex_Object((1,3,6,1,4,1,20044,17,6,3,161,1,1),_Pm254dCtrllineLoopTransceiverIndex_Type())
pm254dCtrllineLoopTransceiverIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineLoopTransceiverIndex.setStatus(_A)
_Pm254dCtrllineLoopTransceiverPortn_Type=EkiState
_Pm254dCtrllineLoopTransceiverPortn_Object=MibTableColumn
pm254dCtrllineLoopTransceiverPortn=_Pm254dCtrllineLoopTransceiverPortn_Object((1,3,6,1,4,1,20044,17,6,3,161,1,2),_Pm254dCtrllineLoopTransceiverPortn_Type())
pm254dCtrllineLoopTransceiverPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineLoopTransceiverPortn.setStatus(_A)
_Pm254dCtrllineSfpOnOffCtrlTable_Object=MibTable
pm254dCtrllineSfpOnOffCtrlTable=_Pm254dCtrllineSfpOnOffCtrlTable_Object((1,3,6,1,4,1,20044,17,6,3,162))
if mibBuilder.loadTexts:pm254dCtrllineSfpOnOffCtrlTable.setStatus(_A)
_Pm254dCtrllineSfpOnOffCtrlEntry_Object=MibTableRow
pm254dCtrllineSfpOnOffCtrlEntry=_Pm254dCtrllineSfpOnOffCtrlEntry_Object((1,3,6,1,4,1,20044,17,6,3,162,1))
pm254dCtrllineSfpOnOffCtrlEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pm254dCtrllineSfpOnOffCtrlEntry.setStatus(_A)
class _Pm254dCtrllineSfpOnOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrllineSfpOnOffCtrlIndex_Type.__name__=_D
_Pm254dCtrllineSfpOnOffCtrlIndex_Object=MibTableColumn
pm254dCtrllineSfpOnOffCtrlIndex=_Pm254dCtrllineSfpOnOffCtrlIndex_Object((1,3,6,1,4,1,20044,17,6,3,162,1,1),_Pm254dCtrllineSfpOnOffCtrlIndex_Type())
pm254dCtrllineSfpOnOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrllineSfpOnOffCtrlIndex.setStatus(_A)
_Pm254dCtrllineSfpOnOffCtrlPortn_Type=EkiState
_Pm254dCtrllineSfpOnOffCtrlPortn_Object=MibTableColumn
pm254dCtrllineSfpOnOffCtrlPortn=_Pm254dCtrllineSfpOnOffCtrlPortn_Object((1,3,6,1,4,1,20044,17,6,3,162,1,2),_Pm254dCtrllineSfpOnOffCtrlPortn_Type())
pm254dCtrllineSfpOnOffCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrllineSfpOnOffCtrlPortn.setStatus(_A)
_Pm254dCtrldccEnableTable_Object=MibTable
pm254dCtrldccEnableTable=_Pm254dCtrldccEnableTable_Object((1,3,6,1,4,1,20044,17,6,3,198))
if mibBuilder.loadTexts:pm254dCtrldccEnableTable.setStatus(_A)
_Pm254dCtrldccEnableEntry_Object=MibTableRow
pm254dCtrldccEnableEntry=_Pm254dCtrldccEnableEntry_Object((1,3,6,1,4,1,20044,17,6,3,198,1))
pm254dCtrldccEnableEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pm254dCtrldccEnableEntry.setStatus(_A)
class _Pm254dCtrldccEnableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCtrldccEnableIndex_Type.__name__=_D
_Pm254dCtrldccEnableIndex_Object=MibTableColumn
pm254dCtrldccEnableIndex=_Pm254dCtrldccEnableIndex_Object((1,3,6,1,4,1,20044,17,6,3,198,1,1),_Pm254dCtrldccEnableIndex_Type())
pm254dCtrldccEnableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCtrldccEnableIndex.setStatus(_A)
_Pm254dCtrldccEnablePortn_Type=EkiState
_Pm254dCtrldccEnablePortn_Object=MibTableColumn
pm254dCtrldccEnablePortn=_Pm254dCtrldccEnablePortn_Object((1,3,6,1,4,1,20044,17,6,3,198,1,2),_Pm254dCtrldccEnablePortn_Type())
pm254dCtrldccEnablePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCtrldccEnablePortn.setStatus(_A)
_Pm254dri_ObjectIdentity=ObjectIdentity
pm254dri=_Pm254dri_ObjectIdentity((1,3,6,1,4,1,20044,17,7))
_Pm254driTable_ObjectIdentity=ObjectIdentity
pm254driTable=_Pm254driTable_ObjectIdentity((1,3,6,1,4,1,20044,17,7,1))
_Pm254dRinvClientTable_Object=MibTable
pm254dRinvClientTable=_Pm254dRinvClientTable_Object((1,3,6,1,4,1,20044,17,7,1,1))
if mibBuilder.loadTexts:pm254dRinvClientTable.setStatus(_A)
_Pm254dRinvClientEntry_Object=MibTableRow
pm254dRinvClientEntry=_Pm254dRinvClientEntry_Object((1,3,6,1,4,1,20044,17,7,1,1,1))
pm254dRinvClientEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pm254dRinvClientEntry.setStatus(_A)
class _Pm254dRinvClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm254dRinvClientIndex_Type.__name__=_D
_Pm254dRinvClientIndex_Object=MibTableColumn
pm254dRinvClientIndex=_Pm254dRinvClientIndex_Object((1,3,6,1,4,1,20044,17,7,1,1,1,1),_Pm254dRinvClientIndex_Type())
pm254dRinvClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvClientIndex.setStatus(_A)
_Pm254dRinvSfpClient_Type=DisplayString
_Pm254dRinvSfpClient_Object=MibTableColumn
pm254dRinvSfpClient=_Pm254dRinvSfpClient_Object((1,3,6,1,4,1,20044,17,7,1,1,1,2),_Pm254dRinvSfpClient_Type())
pm254dRinvSfpClient.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvSfpClient.setStatus(_A)
_Pm254dRinvLineTable_Object=MibTable
pm254dRinvLineTable=_Pm254dRinvLineTable_Object((1,3,6,1,4,1,20044,17,7,1,2))
if mibBuilder.loadTexts:pm254dRinvLineTable.setStatus(_A)
_Pm254dRinvLineEntry_Object=MibTableRow
pm254dRinvLineEntry=_Pm254dRinvLineEntry_Object((1,3,6,1,4,1,20044,17,7,1,2,1))
pm254dRinvLineEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pm254dRinvLineEntry.setStatus(_A)
class _Pm254dRinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm254dRinvLineIndex_Type.__name__=_D
_Pm254dRinvLineIndex_Object=MibTableColumn
pm254dRinvLineIndex=_Pm254dRinvLineIndex_Object((1,3,6,1,4,1,20044,17,7,1,2,1,1),_Pm254dRinvLineIndex_Type())
pm254dRinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvLineIndex.setStatus(_A)
_Pm254dRinvsfpLine_Type=DisplayString
_Pm254dRinvsfpLine_Object=MibTableColumn
pm254dRinvsfpLine=_Pm254dRinvsfpLine_Object((1,3,6,1,4,1,20044,17,7,1,2,1,2),_Pm254dRinvsfpLine_Type())
pm254dRinvsfpLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvsfpLine.setStatus(_A)
class _Pm254dRinvReloadInventory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pm254dRinvReloadInventory_Type.__name__=_D
_Pm254dRinvReloadInventory_Object=MibScalar
pm254dRinvReloadInventory=_Pm254dRinvReloadInventory_Object((1,3,6,1,4,1,20044,17,7,2),_Pm254dRinvReloadInventory_Type())
pm254dRinvReloadInventory.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dRinvReloadInventory.setStatus(_A)
_Pm254dRinvHwPlatform_Type=DisplayString
_Pm254dRinvHwPlatform_Object=MibScalar
pm254dRinvHwPlatform=_Pm254dRinvHwPlatform_Object((1,3,6,1,4,1,20044,17,7,3),_Pm254dRinvHwPlatform_Type())
pm254dRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvHwPlatform.setStatus(_A)
_Pm254dRinvModulePlatform_Type=DisplayString
_Pm254dRinvModulePlatform_Object=MibScalar
pm254dRinvModulePlatform=_Pm254dRinvModulePlatform_Object((1,3,6,1,4,1,20044,17,7,4),_Pm254dRinvModulePlatform_Type())
pm254dRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvModulePlatform.setStatus(_A)
_Pm254dRinvSwPlatform_Type=DisplayString
_Pm254dRinvSwPlatform_Object=MibScalar
pm254dRinvSwPlatform=_Pm254dRinvSwPlatform_Object((1,3,6,1,4,1,20044,17,7,5),_Pm254dRinvSwPlatform_Type())
pm254dRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvSwPlatform.setStatus(_A)
_Pm254dRinvGwPlatform_Type=DisplayString
_Pm254dRinvGwPlatform_Object=MibScalar
pm254dRinvGwPlatform=_Pm254dRinvGwPlatform_Object((1,3,6,1,4,1,20044,17,7,6),_Pm254dRinvGwPlatform_Type())
pm254dRinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dRinvGwPlatform.setStatus(_A)
_Pm254ddownload_ObjectIdentity=ObjectIdentity
pm254ddownload=_Pm254ddownload_ObjectIdentity((1,3,6,1,4,1,20044,17,8))
_Pm254dDwlOther_ObjectIdentity=ObjectIdentity
pm254dDwlOther=_Pm254dDwlOther_ObjectIdentity((1,3,6,1,4,1,20044,17,8,1))
_Pm254dDwlrestartProcess_ObjectIdentity=ObjectIdentity
pm254dDwlrestartProcess=_Pm254dDwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,17,8,1,0))
_Pm254dDwlWarmRestartProcessed_Type=EkiOnOff
_Pm254dDwlWarmRestartProcessed_Object=MibScalar
pm254dDwlWarmRestartProcessed=_Pm254dDwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,17,8,1,0,1),_Pm254dDwlWarmRestartProcessed_Type())
pm254dDwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlWarmRestartProcessed.setStatus(_A)
_Pm254dDwlColdRestartProcessed_Type=EkiOnOff
_Pm254dDwlColdRestartProcessed_Object=MibScalar
pm254dDwlColdRestartProcessed=_Pm254dDwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,17,8,1,0,2),_Pm254dDwlColdRestartProcessed_Type())
pm254dDwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlColdRestartProcessed.setStatus(_A)
_Pm254dDwlswBanksUsed_ObjectIdentity=ObjectIdentity
pm254dDwlswBanksUsed=_Pm254dDwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,17,8,1,1))
_Pm254dDwlSwBank1Used_Type=EkiOnOff
_Pm254dDwlSwBank1Used_Object=MibScalar
pm254dDwlSwBank1Used=_Pm254dDwlSwBank1Used_Object((1,3,6,1,4,1,20044,17,8,1,1,1),_Pm254dDwlSwBank1Used_Type())
pm254dDwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlSwBank1Used.setStatus(_A)
_Pm254dDwlSwBank2Used_Type=EkiOnOff
_Pm254dDwlSwBank2Used_Object=MibScalar
pm254dDwlSwBank2Used=_Pm254dDwlSwBank2Used_Object((1,3,6,1,4,1,20044,17,8,1,1,2),_Pm254dDwlSwBank2Used_Type())
pm254dDwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlSwBank2Used.setStatus(_A)
_Pm254dDwlSwBank1Notempty_Type=EkiOnOff
_Pm254dDwlSwBank1Notempty_Object=MibScalar
pm254dDwlSwBank1Notempty=_Pm254dDwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,17,8,1,1,5),_Pm254dDwlSwBank1Notempty_Type())
pm254dDwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlSwBank1Notempty.setStatus(_A)
_Pm254dDwlSwBank2Notempty_Type=EkiOnOff
_Pm254dDwlSwBank2Notempty_Object=MibScalar
pm254dDwlSwBank2Notempty=_Pm254dDwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,17,8,1,1,6),_Pm254dDwlSwBank2Notempty_Type())
pm254dDwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlSwBank2Notempty.setStatus(_A)
_Pm254dDwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pm254dDwlgwBanksUsed=_Pm254dDwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,17,8,1,2))
_Pm254dDwlGwBank1Used_Type=EkiOnOff
_Pm254dDwlGwBank1Used_Object=MibScalar
pm254dDwlGwBank1Used=_Pm254dDwlGwBank1Used_Object((1,3,6,1,4,1,20044,17,8,1,2,1),_Pm254dDwlGwBank1Used_Type())
pm254dDwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank1Used.setStatus(_A)
_Pm254dDwlGwBank2Used_Type=EkiOnOff
_Pm254dDwlGwBank2Used_Object=MibScalar
pm254dDwlGwBank2Used=_Pm254dDwlGwBank2Used_Object((1,3,6,1,4,1,20044,17,8,1,2,2),_Pm254dDwlGwBank2Used_Type())
pm254dDwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank2Used.setStatus(_A)
_Pm254dDwlGwBank3Used_Type=EkiOnOff
_Pm254dDwlGwBank3Used_Object=MibScalar
pm254dDwlGwBank3Used=_Pm254dDwlGwBank3Used_Object((1,3,6,1,4,1,20044,17,8,1,2,3),_Pm254dDwlGwBank3Used_Type())
pm254dDwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank3Used.setStatus(_A)
_Pm254dDwlGwBank4Used_Type=EkiOnOff
_Pm254dDwlGwBank4Used_Object=MibScalar
pm254dDwlGwBank4Used=_Pm254dDwlGwBank4Used_Object((1,3,6,1,4,1,20044,17,8,1,2,4),_Pm254dDwlGwBank4Used_Type())
pm254dDwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank4Used.setStatus(_A)
_Pm254dDwlGwBank1Notempty_Type=EkiOnOff
_Pm254dDwlGwBank1Notempty_Object=MibScalar
pm254dDwlGwBank1Notempty=_Pm254dDwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,17,8,1,2,5),_Pm254dDwlGwBank1Notempty_Type())
pm254dDwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank1Notempty.setStatus(_A)
_Pm254dDwlGwBank2Notempty_Type=EkiOnOff
_Pm254dDwlGwBank2Notempty_Object=MibScalar
pm254dDwlGwBank2Notempty=_Pm254dDwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,17,8,1,2,6),_Pm254dDwlGwBank2Notempty_Type())
pm254dDwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank2Notempty.setStatus(_A)
_Pm254dDwlGwBank3Notempty_Type=EkiOnOff
_Pm254dDwlGwBank3Notempty_Object=MibScalar
pm254dDwlGwBank3Notempty=_Pm254dDwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,17,8,1,2,7),_Pm254dDwlGwBank3Notempty_Type())
pm254dDwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank3Notempty.setStatus(_A)
_Pm254dDwlGwBank4Notempty_Type=EkiOnOff
_Pm254dDwlGwBank4Notempty_Object=MibScalar
pm254dDwlGwBank4Notempty=_Pm254dDwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,17,8,1,2,8),_Pm254dDwlGwBank4Notempty_Type())
pm254dDwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dDwlGwBank4Notempty.setStatus(_A)
_Pm254dDwlPort_ObjectIdentity=ObjectIdentity
pm254dDwlPort=_Pm254dDwlPort_ObjectIdentity((1,3,6,1,4,1,20044,17,8,2))
_Pm254dDwlLine_ObjectIdentity=ObjectIdentity
pm254dDwlLine=_Pm254dDwlLine_ObjectIdentity((1,3,6,1,4,1,20044,17,8,3))
_Pm254dConfig_ObjectIdentity=ObjectIdentity
pm254dConfig=_Pm254dConfig_ObjectIdentity((1,3,6,1,4,1,20044,17,9))
_Pm254dCfgAccessCAisCsf_ObjectIdentity=ObjectIdentity
pm254dCfgAccessCAisCsf=_Pm254dCfgAccessCAisCsf_ObjectIdentity((1,3,6,1,4,1,20044,17,9,1))
_Pm254dCfgClientcaiscsfTable_Object=MibTable
pm254dCfgClientcaiscsfTable=_Pm254dCfgClientcaiscsfTable_Object((1,3,6,1,4,1,20044,17,9,1,1))
if mibBuilder.loadTexts:pm254dCfgClientcaiscsfTable.setStatus(_A)
_Pm254dCfgClientcaiscsfEntry_Object=MibTableRow
pm254dCfgClientcaiscsfEntry=_Pm254dCfgClientcaiscsfEntry_Object((1,3,6,1,4,1,20044,17,9,1,1,1))
pm254dCfgClientcaiscsfEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pm254dCfgClientcaiscsfEntry.setStatus(_A)
class _Pm254dCfgClientcaiscsfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCfgClientcaiscsfIndex_Type.__name__=_D
_Pm254dCfgClientcaiscsfIndex_Object=MibTableColumn
pm254dCfgClientcaiscsfIndex=_Pm254dCfgClientcaiscsfIndex_Object((1,3,6,1,4,1,20044,17,9,1,1,1,1),_Pm254dCfgClientcaiscsfIndex_Type())
pm254dCfgClientcaiscsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCfgClientcaiscsfIndex.setStatus(_A)
class _Pm254dCfgCAisModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgCAisModePortn_Type.__name__=_F
_Pm254dCfgCAisModePortn_Object=MibTableColumn
pm254dCfgCAisModePortn=_Pm254dCfgCAisModePortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,3),_Pm254dCfgCAisModePortn_Type())
pm254dCfgCAisModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgCAisModePortn.setStatus(_A)
class _Pm254dCfgSts24cContribPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgSts24cContribPortn_Type.__name__=_F
_Pm254dCfgSts24cContribPortn_Object=MibTableColumn
pm254dCfgSts24cContribPortn=_Pm254dCfgSts24cContribPortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,4),_Pm254dCfgSts24cContribPortn_Type())
pm254dCfgSts24cContribPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgSts24cContribPortn.setStatus(_A)
class _Pm254dCfgUpAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgUpAccessioAlmPortn_Type.__name__=_F
_Pm254dCfgUpAccessioAlmPortn_Object=MibTableColumn
pm254dCfgUpAccessioAlmPortn=_Pm254dCfgUpAccessioAlmPortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,9),_Pm254dCfgUpAccessioAlmPortn_Type())
pm254dCfgUpAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgUpAccessioAlmPortn.setStatus(_A)
class _Pm254dCfgUpMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgUpMapperDeAlmPortn_Type.__name__=_F
_Pm254dCfgUpMapperDeAlmPortn_Object=MibTableColumn
pm254dCfgUpMapperDeAlmPortn=_Pm254dCfgUpMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,10),_Pm254dCfgUpMapperDeAlmPortn_Type())
pm254dCfgUpMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgUpMapperDeAlmPortn.setStatus(_A)
class _Pm254dCfgDownMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgDownMapperDeAlmPortn_Type.__name__=_F
_Pm254dCfgDownMapperDeAlmPortn_Object=MibTableColumn
pm254dCfgDownMapperDeAlmPortn=_Pm254dCfgDownMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,18),_Pm254dCfgDownMapperDeAlmPortn_Type())
pm254dCfgDownMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgDownMapperDeAlmPortn.setStatus(_A)
class _Pm254dCfgDownDfrmAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgDownDfrmAlmPortn_Type.__name__=_F
_Pm254dCfgDownDfrmAlmPortn_Object=MibTableColumn
pm254dCfgDownDfrmAlmPortn=_Pm254dCfgDownDfrmAlmPortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,19),_Pm254dCfgDownDfrmAlmPortn_Type())
pm254dCfgDownDfrmAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgDownDfrmAlmPortn.setStatus(_A)
class _Pm254dCfgDownLineIoAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgDownLineIoAlmPortn_Type.__name__=_F
_Pm254dCfgDownLineIoAlmPortn_Object=MibTableColumn
pm254dCfgDownLineIoAlmPortn=_Pm254dCfgDownLineIoAlmPortn_Object((1,3,6,1,4,1,20044,17,9,1,1,1,22),_Pm254dCfgDownLineIoAlmPortn_Type())
pm254dCfgDownLineIoAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgDownLineIoAlmPortn.setStatus(_K)
_Pm254dCfgStartup_ObjectIdentity=ObjectIdentity
pm254dCfgStartup=_Pm254dCfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,17,9,2))
_Pm254dCfgClientStartupTable_Object=MibTable
pm254dCfgClientStartupTable=_Pm254dCfgClientStartupTable_Object((1,3,6,1,4,1,20044,17,9,2,1))
if mibBuilder.loadTexts:pm254dCfgClientStartupTable.setStatus(_A)
_Pm254dCfgClientStartupEntry_Object=MibTableRow
pm254dCfgClientStartupEntry=_Pm254dCfgClientStartupEntry_Object((1,3,6,1,4,1,20044,17,9,2,1,1))
pm254dCfgClientStartupEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pm254dCfgClientStartupEntry.setStatus(_A)
class _Pm254dCfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCfgClientStartupIndex_Type.__name__=_D
_Pm254dCfgClientStartupIndex_Object=MibTableColumn
pm254dCfgClientStartupIndex=_Pm254dCfgClientStartupIndex_Object((1,3,6,1,4,1,20044,17,9,2,1,1,1),_Pm254dCfgClientStartupIndex_Type())
pm254dCfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCfgClientStartupIndex.setStatus(_A)
class _Pm254dCfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgSystConfPortPortn_Type.__name__=_F
_Pm254dCfgSystConfPortPortn_Object=MibTableColumn
pm254dCfgSystConfPortPortn=_Pm254dCfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,17,9,2,1,1,3),_Pm254dCfgSystConfPortPortn_Type())
pm254dCfgSystConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgSystConfPortPortn.setStatus(_A)
class _Pm254dCfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgNetConfPortPortn_Type.__name__=_F
_Pm254dCfgNetConfPortPortn_Object=MibTableColumn
pm254dCfgNetConfPortPortn=_Pm254dCfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,17,9,2,1,1,4),_Pm254dCfgNetConfPortPortn_Type())
pm254dCfgNetConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgNetConfPortPortn.setStatus(_A)
class _Pm254dCfgPortsOptionsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgPortsOptionsPortn_Type.__name__=_F
_Pm254dCfgPortsOptionsPortn_Object=MibTableColumn
pm254dCfgPortsOptionsPortn=_Pm254dCfgPortsOptionsPortn_Object((1,3,6,1,4,1,20044,17,9,2,1,1,6),_Pm254dCfgPortsOptionsPortn_Type())
pm254dCfgPortsOptionsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgPortsOptionsPortn.setStatus(_K)
_Pm254dtablelineStartup_ObjectIdentity=ObjectIdentity
pm254dtablelineStartup=_Pm254dtablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,17,9,2,2))
class _Pm254dCfgsystConfLine1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgsystConfLine1_Type.__name__=_F
_Pm254dCfgsystConfLine1_Object=MibScalar
pm254dCfgsystConfLine1=_Pm254dCfgsystConfLine1_Object((1,3,6,1,4,1,20044,17,9,2,2,2),_Pm254dCfgsystConfLine1_Type())
pm254dCfgsystConfLine1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgsystConfLine1.setStatus(_A)
class _Pm254dCfglineOptions1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfglineOptions1_Type.__name__=_F
_Pm254dCfglineOptions1_Object=MibScalar
pm254dCfglineOptions1=_Pm254dCfglineOptions1_Object((1,3,6,1,4,1,20044,17,9,2,2,5),_Pm254dCfglineOptions1_Type())
pm254dCfglineOptions1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfglineOptions1.setStatus(_A)
class _Pm254dCfgsystConfLine2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfgsystConfLine2_Type.__name__=_F
_Pm254dCfgsystConfLine2_Object=MibScalar
pm254dCfgsystConfLine2=_Pm254dCfgsystConfLine2_Object((1,3,6,1,4,1,20044,17,9,2,2,6),_Pm254dCfgsystConfLine2_Type())
pm254dCfgsystConfLine2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgsystConfLine2.setStatus(_A)
class _Pm254dCfglineSelection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfglineSelection_Type.__name__=_F
_Pm254dCfglineSelection_Object=MibScalar
pm254dCfglineSelection=_Pm254dCfglineSelection_Object((1,3,6,1,4,1,20044,17,9,2,2,7),_Pm254dCfglineSelection_Type())
pm254dCfglineSelection.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfglineSelection.setStatus(_A)
class _Pm254dCfglineOptions2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm254dCfglineOptions2_Type.__name__=_F
_Pm254dCfglineOptions2_Object=MibScalar
pm254dCfglineOptions2=_Pm254dCfglineOptions2_Object((1,3,6,1,4,1,20044,17,9,2,2,9),_Pm254dCfglineOptions2_Type())
pm254dCfglineOptions2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfglineOptions2.setStatus(_A)
_Pm254dCfgLabels_ObjectIdentity=ObjectIdentity
pm254dCfgLabels=_Pm254dCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,17,9,3))
_Pm254dCfgLabelclientTable_Object=MibTable
pm254dCfgLabelclientTable=_Pm254dCfgLabelclientTable_Object((1,3,6,1,4,1,20044,17,9,3,1))
if mibBuilder.loadTexts:pm254dCfgLabelclientTable.setStatus(_A)
_Pm254dCfgLabelclientEntry_Object=MibTableRow
pm254dCfgLabelclientEntry=_Pm254dCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,17,9,3,1,1))
pm254dCfgLabelclientEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pm254dCfgLabelclientEntry.setStatus(_A)
class _Pm254dCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCfgLabelclientIndex_Type.__name__=_D
_Pm254dCfgLabelclientIndex_Object=MibTableColumn
pm254dCfgLabelclientIndex=_Pm254dCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,17,9,3,1,1,1),_Pm254dCfgLabelclientIndex_Type())
pm254dCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCfgLabelclientIndex.setStatus(_A)
class _Pm254dCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm254dCfgLabelclientPortn_Type.__name__=_J
_Pm254dCfgLabelclientPortn_Object=MibTableColumn
pm254dCfgLabelclientPortn=_Pm254dCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,17,9,3,1,1,3),_Pm254dCfgLabelclientPortn_Type())
pm254dCfgLabelclientPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgLabelclientPortn.setStatus(_A)
_Pm254dCfgLabellineTable_Object=MibTable
pm254dCfgLabellineTable=_Pm254dCfgLabellineTable_Object((1,3,6,1,4,1,20044,17,9,3,2))
if mibBuilder.loadTexts:pm254dCfgLabellineTable.setStatus(_A)
_Pm254dCfgLabellineEntry_Object=MibTableRow
pm254dCfgLabellineEntry=_Pm254dCfgLabellineEntry_Object((1,3,6,1,4,1,20044,17,9,3,2,1))
pm254dCfgLabellineEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pm254dCfgLabellineEntry.setStatus(_A)
class _Pm254dCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dCfgLabellineIndex_Type.__name__=_D
_Pm254dCfgLabellineIndex_Object=MibTableColumn
pm254dCfgLabellineIndex=_Pm254dCfgLabellineIndex_Object((1,3,6,1,4,1,20044,17,9,3,2,1,1),_Pm254dCfgLabellineIndex_Type())
pm254dCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dCfgLabellineIndex.setStatus(_A)
class _Pm254dCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm254dCfgLabellinePortn_Type.__name__=_J
_Pm254dCfgLabellinePortn_Object=MibTableColumn
pm254dCfgLabellinePortn=_Pm254dCfgLabellinePortn_Object((1,3,6,1,4,1,20044,17,9,3,2,1,3),_Pm254dCfgLabellinePortn_Type())
pm254dCfgLabellinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgLabellinePortn.setStatus(_A)
_Pm254dCfgWriteConfiguration_Type=EkiOnOff
_Pm254dCfgWriteConfiguration_Object=MibScalar
pm254dCfgWriteConfiguration=_Pm254dCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,17,9,257),_Pm254dCfgWriteConfiguration_Type())
pm254dCfgWriteConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dCfgWriteConfiguration.setStatus(_A)
_Pm254dtraps_ObjectIdentity=ObjectIdentity
pm254dtraps=_Pm254dtraps_ObjectIdentity((1,3,6,1,4,1,20044,17,10))
class _Pm254dTrapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm254dTrapPortNumber_Type.__name__=_D
_Pm254dTrapPortNumber_Object=MibScalar
pm254dTrapPortNumber=_Pm254dTrapPortNumber_Object((1,3,6,1,4,1,20044,17,10,2),_Pm254dTrapPortNumber_Type())
pm254dTrapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dTrapPortNumber.setStatus(_A)
class _Pm254dTrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm254dTrapBoardNumber_Type.__name__=_D
_Pm254dTrapBoardNumber_Object=MibScalar
pm254dTrapBoardNumber=_Pm254dTrapBoardNumber_Object((1,3,6,1,4,1,20044,17,10,3),_Pm254dTrapBoardNumber_Type())
pm254dTrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dTrapBoardNumber.setStatus(_A)
class _Pm254dTrapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm254dTrapLineNumber_Type.__name__=_D
_Pm254dTrapLineNumber_Object=MibScalar
pm254dTrapLineNumber=_Pm254dTrapLineNumber_Object((1,3,6,1,4,1,20044,17,10,4),_Pm254dTrapLineNumber_Type())
pm254dTrapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dTrapLineNumber.setStatus(_A)
_Pm254dMonitoring_ObjectIdentity=ObjectIdentity
pm254dMonitoring=_Pm254dMonitoring_ObjectIdentity((1,3,6,1,4,1,20044,17,11))
_Pm254dMonOther_ObjectIdentity=ObjectIdentity
pm254dMonOther=_Pm254dMonOther_ObjectIdentity((1,3,6,1,4,1,20044,17,11,1))
_Pm254dMonRmon_ObjectIdentity=ObjectIdentity
pm254dMonRmon=_Pm254dMonRmon_ObjectIdentity((1,3,6,1,4,1,20044,17,11,1,3))
_Pm254dMonCountersReset_Type=EkiOnOff
_Pm254dMonCountersReset_Object=MibScalar
pm254dMonCountersReset=_Pm254dMonCountersReset_Object((1,3,6,1,4,1,20044,17,11,1,3,359),_Pm254dMonCountersReset_Type())
pm254dMonCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dMonCountersReset.setStatus(_A)
_Pm254dMonCountersStop_Type=EkiOnOff
_Pm254dMonCountersStop_Object=MibScalar
pm254dMonCountersStop=_Pm254dMonCountersStop_Object((1,3,6,1,4,1,20044,17,11,1,3,360),_Pm254dMonCountersStop_Type())
pm254dMonCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm254dMonCountersStop.setStatus(_A)
_Pm254dMonClient_ObjectIdentity=ObjectIdentity
pm254dMonClient=_Pm254dMonClient_ObjectIdentity((1,3,6,1,4,1,20044,17,11,2))
_Pm254dMonClientRmonCounter_ObjectIdentity=ObjectIdentity
pm254dMonClientRmonCounter=_Pm254dMonClientRmonCounter_ObjectIdentity((1,3,6,1,4,1,20044,17,11,2,4))
_Pm254dMonupRmonByteCntTable_Object=MibTable
pm254dMonupRmonByteCntTable=_Pm254dMonupRmonByteCntTable_Object((1,3,6,1,4,1,20044,17,11,2,4,16))
if mibBuilder.loadTexts:pm254dMonupRmonByteCntTable.setStatus(_A)
_Pm254dMonupRmonByteCntEntry_Object=MibTableRow
pm254dMonupRmonByteCntEntry=_Pm254dMonupRmonByteCntEntry_Object((1,3,6,1,4,1,20044,17,11,2,4,16,1))
pm254dMonupRmonByteCntEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pm254dMonupRmonByteCntEntry.setStatus(_A)
class _Pm254dMonupRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMonupRmonByteCntIndex_Type.__name__=_D
_Pm254dMonupRmonByteCntIndex_Object=MibTableColumn
pm254dMonupRmonByteCntIndex=_Pm254dMonupRmonByteCntIndex_Object((1,3,6,1,4,1,20044,17,11,2,4,16,1,1),_Pm254dMonupRmonByteCntIndex_Type())
pm254dMonupRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonByteCntIndex.setStatus(_A)
_Pm254dMonupRmonByteCntValuePortn_Type=Counter64
_Pm254dMonupRmonByteCntValuePortn_Object=MibTableColumn
pm254dMonupRmonByteCntValuePortn=_Pm254dMonupRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,17,11,2,4,16,1,2),_Pm254dMonupRmonByteCntValuePortn_Type())
pm254dMonupRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonByteCntValuePortn.setStatus(_A)
_Pm254dMonupRmonByteCntErrorPortn_Type=EkiOnOff
_Pm254dMonupRmonByteCntErrorPortn_Object=MibTableColumn
pm254dMonupRmonByteCntErrorPortn=_Pm254dMonupRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,16,1,3),_Pm254dMonupRmonByteCntErrorPortn_Type())
pm254dMonupRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonByteCntErrorPortn.setStatus(_A)
_Pm254dMonupRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm254dMonupRmonByteCntOverloadPortn_Object=MibTableColumn
pm254dMonupRmonByteCntOverloadPortn=_Pm254dMonupRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,16,1,4),_Pm254dMonupRmonByteCntOverloadPortn_Type())
pm254dMonupRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonByteCntOverloadPortn.setStatus(_A)
_Pm254dMonupRmonCrcErrorCntTable_Object=MibTable
pm254dMonupRmonCrcErrorCntTable=_Pm254dMonupRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,17,11,2,4,24))
if mibBuilder.loadTexts:pm254dMonupRmonCrcErrorCntTable.setStatus(_A)
_Pm254dMonupRmonCrcErrorCntEntry_Object=MibTableRow
pm254dMonupRmonCrcErrorCntEntry=_Pm254dMonupRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,17,11,2,4,24,1))
pm254dMonupRmonCrcErrorCntEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pm254dMonupRmonCrcErrorCntEntry.setStatus(_A)
class _Pm254dMonupRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMonupRmonCrcErrorCntIndex_Type.__name__=_D
_Pm254dMonupRmonCrcErrorCntIndex_Object=MibTableColumn
pm254dMonupRmonCrcErrorCntIndex=_Pm254dMonupRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,17,11,2,4,24,1,1),_Pm254dMonupRmonCrcErrorCntIndex_Type())
pm254dMonupRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonCrcErrorCntIndex.setStatus(_A)
_Pm254dMonupRmonCrcErrorCntValuePortn_Type=Counter64
_Pm254dMonupRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm254dMonupRmonCrcErrorCntValuePortn=_Pm254dMonupRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,17,11,2,4,24,1,2),_Pm254dMonupRmonCrcErrorCntValuePortn_Type())
pm254dMonupRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm254dMonupRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm254dMonupRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm254dMonupRmonCrcErrorCntErrorPortn=_Pm254dMonupRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,24,1,3),_Pm254dMonupRmonCrcErrorCntErrorPortn_Type())
pm254dMonupRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm254dMonupRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm254dMonupRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm254dMonupRmonCrcErrorCntOverloadPortn=_Pm254dMonupRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,24,1,4),_Pm254dMonupRmonCrcErrorCntOverloadPortn_Type())
pm254dMonupRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm254dMonupRmonPacketsCntTable_Object=MibTable
pm254dMonupRmonPacketsCntTable=_Pm254dMonupRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,17,11,2,4,32))
if mibBuilder.loadTexts:pm254dMonupRmonPacketsCntTable.setStatus(_A)
_Pm254dMonupRmonPacketsCntEntry_Object=MibTableRow
pm254dMonupRmonPacketsCntEntry=_Pm254dMonupRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,17,11,2,4,32,1))
pm254dMonupRmonPacketsCntEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pm254dMonupRmonPacketsCntEntry.setStatus(_A)
class _Pm254dMonupRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMonupRmonPacketsCntIndex_Type.__name__=_D
_Pm254dMonupRmonPacketsCntIndex_Object=MibTableColumn
pm254dMonupRmonPacketsCntIndex=_Pm254dMonupRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,17,11,2,4,32,1,1),_Pm254dMonupRmonPacketsCntIndex_Type())
pm254dMonupRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonPacketsCntIndex.setStatus(_A)
_Pm254dMonupRmonPacketsCntValuePortn_Type=Counter64
_Pm254dMonupRmonPacketsCntValuePortn_Object=MibTableColumn
pm254dMonupRmonPacketsCntValuePortn=_Pm254dMonupRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,17,11,2,4,32,1,2),_Pm254dMonupRmonPacketsCntValuePortn_Type())
pm254dMonupRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonPacketsCntValuePortn.setStatus(_A)
_Pm254dMonupRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm254dMonupRmonPacketsCntErrorPortn_Object=MibTableColumn
pm254dMonupRmonPacketsCntErrorPortn=_Pm254dMonupRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,32,1,3),_Pm254dMonupRmonPacketsCntErrorPortn_Type())
pm254dMonupRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonPacketsCntErrorPortn.setStatus(_A)
_Pm254dMonupRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm254dMonupRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm254dMonupRmonPacketsCntOverloadPortn=_Pm254dMonupRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,32,1,4),_Pm254dMonupRmonPacketsCntOverloadPortn_Type())
pm254dMonupRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm254dMonupRmonBroadcastCntTable_Object=MibTable
pm254dMonupRmonBroadcastCntTable=_Pm254dMonupRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,17,11,2,4,40))
if mibBuilder.loadTexts:pm254dMonupRmonBroadcastCntTable.setStatus(_A)
_Pm254dMonupRmonBroadcastCntEntry_Object=MibTableRow
pm254dMonupRmonBroadcastCntEntry=_Pm254dMonupRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,17,11,2,4,40,1))
pm254dMonupRmonBroadcastCntEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pm254dMonupRmonBroadcastCntEntry.setStatus(_A)
class _Pm254dMonupRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMonupRmonBroadcastCntIndex_Type.__name__=_D
_Pm254dMonupRmonBroadcastCntIndex_Object=MibTableColumn
pm254dMonupRmonBroadcastCntIndex=_Pm254dMonupRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,17,11,2,4,40,1,1),_Pm254dMonupRmonBroadcastCntIndex_Type())
pm254dMonupRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonBroadcastCntIndex.setStatus(_A)
_Pm254dMonupRmonBroadcastCntValuePortn_Type=Counter64
_Pm254dMonupRmonBroadcastCntValuePortn_Object=MibTableColumn
pm254dMonupRmonBroadcastCntValuePortn=_Pm254dMonupRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,17,11,2,4,40,1,2),_Pm254dMonupRmonBroadcastCntValuePortn_Type())
pm254dMonupRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonBroadcastCntValuePortn.setStatus(_A)
_Pm254dMonupRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm254dMonupRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm254dMonupRmonBroadcastCntErrorPortn=_Pm254dMonupRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,40,1,3),_Pm254dMonupRmonBroadcastCntErrorPortn_Type())
pm254dMonupRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm254dMonupRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm254dMonupRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm254dMonupRmonBroadcastCntOverloadPortn=_Pm254dMonupRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,40,1,4),_Pm254dMonupRmonBroadcastCntOverloadPortn_Type())
pm254dMonupRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm254dMonupRmonMulticastCntTable_Object=MibTable
pm254dMonupRmonMulticastCntTable=_Pm254dMonupRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,17,11,2,4,48))
if mibBuilder.loadTexts:pm254dMonupRmonMulticastCntTable.setStatus(_A)
_Pm254dMonupRmonMulticastCntEntry_Object=MibTableRow
pm254dMonupRmonMulticastCntEntry=_Pm254dMonupRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,17,11,2,4,48,1))
pm254dMonupRmonMulticastCntEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pm254dMonupRmonMulticastCntEntry.setStatus(_A)
class _Pm254dMonupRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm254dMonupRmonMulticastCntIndex_Type.__name__=_D
_Pm254dMonupRmonMulticastCntIndex_Object=MibTableColumn
pm254dMonupRmonMulticastCntIndex=_Pm254dMonupRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,17,11,2,4,48,1,1),_Pm254dMonupRmonMulticastCntIndex_Type())
pm254dMonupRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonMulticastCntIndex.setStatus(_A)
_Pm254dMonupRmonMulticastCntValuePortn_Type=Counter64
_Pm254dMonupRmonMulticastCntValuePortn_Object=MibTableColumn
pm254dMonupRmonMulticastCntValuePortn=_Pm254dMonupRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,17,11,2,4,48,1,2),_Pm254dMonupRmonMulticastCntValuePortn_Type())
pm254dMonupRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonMulticastCntValuePortn.setStatus(_A)
_Pm254dMonupRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm254dMonupRmonMulticastCntErrorPortn_Object=MibTableColumn
pm254dMonupRmonMulticastCntErrorPortn=_Pm254dMonupRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,48,1,3),_Pm254dMonupRmonMulticastCntErrorPortn_Type())
pm254dMonupRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonMulticastCntErrorPortn.setStatus(_A)
_Pm254dMonupRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm254dMonupRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm254dMonupRmonMulticastCntOverloadPortn=_Pm254dMonupRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,17,11,2,4,48,1,4),_Pm254dMonupRmonMulticastCntOverloadPortn_Type())
pm254dMonupRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm254dMonupRmonMulticastCntOverloadPortn.setStatus(_A)
pm254dLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,17,10,30))
pm254dLineTrapNotUrgentGoesOn.setObjects(*((_C,_L),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm254dLineTrapNotUrgentGoesOn.setStatus(_A)
pm254dLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,17,10,31))
pm254dLineTrapNotUrgentGoesOff.setObjects(*((_C,_L),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm254dLineTrapNotUrgentGoesOff.setStatus(_A)
pm254dLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,17,10,32))
pm254dLineTrapUrgentGoesOn.setObjects(*((_C,_M),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm254dLineTrapUrgentGoesOn.setStatus(_A)
pm254dLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,17,10,33))
pm254dLineTrapUrgentGoesOff.setObjects(*((_C,_M),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm254dLineTrapUrgentGoesOff.setStatus(_A)
pm254dLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,17,10,34))
pm254dLineTrapCritGoesOn.setObjects(*((_C,_N),(_C,_O),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm254dLineTrapCritGoesOn.setStatus(_A)
pm254dLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,17,10,35))
pm254dLineTrapCritGoesOff.setObjects(*((_C,_N),(_C,_O),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm254dLineTrapCritGoesOff.setStatus(_A)
pm254dClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,17,10,40))
pm254dClientTrapNotUrgentGoesOn.setObjects(*((_C,_P),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm254dClientTrapNotUrgentGoesOn.setStatus(_A)
pm254dClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,17,10,41))
pm254dClientTrapNotUrgentGoesOff.setObjects(*((_C,_P),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm254dClientTrapNotUrgentGoesOff.setStatus(_A)
pm254dClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,17,10,42))
pm254dClientTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm254dClientTrapUrgentGoesOn.setStatus(_A)
pm254dClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,17,10,43))
pm254dClientTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm254dClientTrapUrgentGoesOff.setStatus(_A)
pm254dClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,17,10,44))
pm254dClientTrapCritGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm254dClientTrapCritGoesOn.setStatus(_A)
pm254dClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,17,10,45))
pm254dClientTrapCritGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm254dClientTrapCritGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'modulePm254d':modulePm254d,'pm254dalarms':pm254dalarms,'pm254dAlmOther':pm254dAlmOther,'pm254dAlmOtherNurg':pm254dAlmOtherNurg,'pm254dAlmsynthAlm0':pm254dAlmsynthAlm0,'pm254dAlmModGlobFail':pm254dAlmModGlobFail,'pm254dAlmDefFuseA':pm254dAlmDefFuseA,'pm254dAlmDefFuseB':pm254dAlmDefFuseB,'pm254dAlmsynthAlm2':pm254dAlmsynthAlm2,'pm254dAlmConfTableSave':pm254dAlmConfTableSave,'pm254dAlmInvUpload':pm254dAlmInvUpload,'pm254dAlmConfTableLoad':pm254dAlmConfTableLoad,'pm254dAlmCorrelatOff':pm254dAlmCorrelatOff,'pm254dAlmMaintenanceOn':pm254dAlmMaintenanceOn,'pm254dAlmOtherUrg':pm254dAlmOtherUrg,'pm254dAlmmodInitFailLevel2':pm254dAlmmodInitFailLevel2,'pm254dAlmLedFail':pm254dAlmLedFail,'pm254dAlmNextColdBootForced':pm254dAlmNextColdBootForced,'pm254dAlmBootUndone':pm254dAlmBootUndone,'pm254dAlmResetHwInitFail':pm254dAlmResetHwInitFail,'pm254dAlmSwInitFail':pm254dAlmSwInitFail,'pm254dAlmmodInitFailLevel3':pm254dAlmmodInitFailLevel3,'pm254dAlmGwIdentFail':pm254dAlmGwIdentFail,'pm254dAlmObmTypeReadFail':pm254dAlmObmTypeReadFail,'pm254dAlmInitModuleFail':pm254dAlmInitModuleFail,'pm254dAlmSfp1InitFail':pm254dAlmSfp1InitFail,'pm254dAlmSfp2InitFail':pm254dAlmSfp2InitFail,'pm254dAlmLine1InitFail':pm254dAlmLine1InitFail,'pm254dAlmLine2InitFail':pm254dAlmLine2InitFail,'pm254dAlmClient1InitFail':pm254dAlmClient1InitFail,'pm254dAlmClient2InitFail':pm254dAlmClient2InitFail,'pm254dAlmClient3InitFail':pm254dAlmClient3InitFail,'pm254dAlmClient4InitFail':pm254dAlmClient4InitFail,'pm254dAlmOtherCrit':pm254dAlmOtherCrit,'pm254dAlmPort':pm254dAlmPort,'pm254dAlmPortNurg':pm254dAlmPortNurg,'pm254dAlmclientSfpWarnDdmTable':pm254dAlmclientSfpWarnDdmTable,'pm254dAlmclientSfpWarnDdmEntry':pm254dAlmclientSfpWarnDdmEntry,_T:pm254dAlmclientSfpWarnDdmIndex,'pm254dAlmClientTxPwLowWngPortn':pm254dAlmClientTxPwLowWngPortn,'pm254dAlmClientTxPwrHighWngPortn':pm254dAlmClientTxPwrHighWngPortn,'pm254dAlmClientTxBiasLowWngPortn':pm254dAlmClientTxBiasLowWngPortn,'pm254dAlmClientTxBiasHighWngPortn':pm254dAlmClientTxBiasHighWngPortn,'pm254dAlmClientVccLowWngPortn':pm254dAlmClientVccLowWngPortn,'pm254dAlmClientVccHighWngPortn':pm254dAlmClientVccHighWngPortn,'pm254dAlmClientTempLowWngPortn':pm254dAlmClientTempLowWngPortn,'pm254dAlmClientTempHighWngPortn':pm254dAlmClientTempHighWngPortn,'pm254dAlmClientRxPwrLowWngPortn':pm254dAlmClientRxPwrLowWngPortn,'pm254dAlmClientRxPwrHighWngPortn':pm254dAlmClientRxPwrHighWngPortn,'pm254dAlmPortUrg':pm254dAlmPortUrg,'pm254dAlmclientSfpAlmDdmTable':pm254dAlmclientSfpAlmDdmTable,'pm254dAlmclientSfpAlmDdmEntry':pm254dAlmclientSfpAlmDdmEntry,_U:pm254dAlmclientSfpAlmDdmIndex,'pm254dAlmClientTxPwrLowAlaPortn':pm254dAlmClientTxPwrLowAlaPortn,'pm254dAlmClientTxPwrHighAlaPortn':pm254dAlmClientTxPwrHighAlaPortn,'pm254dAlmClientTxBiasLowAlaPortn':pm254dAlmClientTxBiasLowAlaPortn,'pm254dAlmClientTxBiasHighAlaPortn':pm254dAlmClientTxBiasHighAlaPortn,'pm254dAlmClientVccLowAlaPortn':pm254dAlmClientVccLowAlaPortn,'pm254dAlmClientVccHighAlaPortn':pm254dAlmClientVccHighAlaPortn,'pm254dAlmClientTempLowAlaPortn':pm254dAlmClientTempLowAlaPortn,'pm254dAlmClientTempHighAlaPortn':pm254dAlmClientTempHighAlaPortn,'pm254dAlmClientRxPwrLowAlaPortn':pm254dAlmClientRxPwrLowAlaPortn,'pm254dAlmClientRxPwrHighAlaPortn':pm254dAlmClientRxPwrHighAlaPortn,'pm254dAlmPortCrit':pm254dAlmPortCrit,'pm254dAlmsynthAlmClientTable':pm254dAlmsynthAlmClientTable,'pm254dAlmsynthAlmClientEntry':pm254dAlmsynthAlmClientEntry,_V:pm254dAlmsynthAlmClientIndex,'pm254dAlmClientSfpAbsentPortn':pm254dAlmClientSfpAbsentPortn,'pm254dAlmClientDdmAbsentPortn':pm254dAlmClientDdmAbsentPortn,_S:pm254dAlmClientHwFailAccPortn,'pm254dAlmClientLsdPortn':pm254dAlmClientLsdPortn,'pm254dAlmClientLocalOosPortn':pm254dAlmClientLocalOosPortn,'pm254dAlmClientRemoteOosPortn':pm254dAlmClientRemoteOosPortn,'pm254dAlmClientDwCaisPortn':pm254dAlmClientDwCaisPortn,_P:pm254dAlmClientSfpDdmWarningPortn,_Q:pm254dAlmClientSfpDdmAlmPortn,_R:pm254dAlmClientFailAccPortn,'pm254dAlmClientUpCsfPortn':pm254dAlmClientUpCsfPortn,'pm254dAlmaccessioAlmTable':pm254dAlmaccessioAlmTable,'pm254dAlmaccessioAlmEntry':pm254dAlmaccessioAlmEntry,_W:pm254dAlmaccessioAlmIndex,'pm254dAlmClientDwLasFailPortn':pm254dAlmClientDwLasFailPortn,'pm254dAlmClientUpLosPortn':pm254dAlmClientUpLosPortn,'pm254dAlmclientMapperDeAlmTable':pm254dAlmclientMapperDeAlmTable,'pm254dAlmclientMapperDeAlmEntry':pm254dAlmclientMapperDeAlmEntry,_X:pm254dAlmclientMapperDeAlmIndex,'pm254dAlmClientUpAccOosPortn':pm254dAlmClientUpAccOosPortn,'pm254dAlmClientUpBufferOvlPortn':pm254dAlmClientUpBufferOvlPortn,'pm254dAlmClientDwCsfDetPortn':pm254dAlmClientDwCsfDetPortn,'pm254dAlmClientDwBufferOvlPortn':pm254dAlmClientDwBufferOvlPortn,'pm254dAlmClientLoopAccFifoFailPortn':pm254dAlmClientLoopAccFifoFailPortn,'pm254dAlmLine':pm254dAlmLine,'pm254dAlmLineNurg':pm254dAlmLineNurg,'pm254dAlmlineDownS1Table':pm254dAlmlineDownS1Table,'pm254dAlmlineDownS1Entry':pm254dAlmlineDownS1Entry,_Y:pm254dAlmlineDownS1Index,'pm254dAlmlineDownS1Portn':pm254dAlmlineDownS1Portn,'pm254dAlmlineDownK1Table':pm254dAlmlineDownK1Table,'pm254dAlmlineDownK1Entry':pm254dAlmlineDownK1Entry,_Z:pm254dAlmlineDownK1Index,'pm254dAlmlineDownK1Portn':pm254dAlmlineDownK1Portn,'pm254dAlmlineDownK2Table':pm254dAlmlineDownK2Table,'pm254dAlmlineDownK2Entry':pm254dAlmlineDownK2Entry,_a:pm254dAlmlineDownK2Index,'pm254dAlmlineDownK2Portn':pm254dAlmlineDownK2Portn,'pm254dAlmlineSfpWarnDdmTable':pm254dAlmlineSfpWarnDdmTable,'pm254dAlmlineSfpWarnDdmEntry':pm254dAlmlineSfpWarnDdmEntry,_b:pm254dAlmlineSfpWarnDdmIndex,'pm254dAlmLineTxPwLowWngPortn':pm254dAlmLineTxPwLowWngPortn,'pm254dAlmLineTxPwrHighWngPortn':pm254dAlmLineTxPwrHighWngPortn,'pm254dAlmLineTxBiasLowWngPortn':pm254dAlmLineTxBiasLowWngPortn,'pm254dAlmLineTxBiasHighWngPortn':pm254dAlmLineTxBiasHighWngPortn,'pm254dAlmLineVccLowWngPortn':pm254dAlmLineVccLowWngPortn,'pm254dAlmLineVccHighWngPortn':pm254dAlmLineVccHighWngPortn,'pm254dAlmLineTempLowWngPortn':pm254dAlmLineTempLowWngPortn,'pm254dAlmLineTempHighWngPortn':pm254dAlmLineTempHighWngPortn,'pm254dAlmLineRxPwrLowWngPortn':pm254dAlmLineRxPwrLowWngPortn,'pm254dAlmLineRxPwrHighWngPortn':pm254dAlmLineRxPwrHighWngPortn,'pm254dAlmLineUrg':pm254dAlmLineUrg,'pm254dAlmlineSfpAlaDdmTable':pm254dAlmlineSfpAlaDdmTable,'pm254dAlmlineSfpAlaDdmEntry':pm254dAlmlineSfpAlaDdmEntry,_c:pm254dAlmlineSfpAlaDdmIndex,'pm254dAlmLineTxPwrLowAlaPortn':pm254dAlmLineTxPwrLowAlaPortn,'pm254dAlmLineTxPwrHighAlaPortn':pm254dAlmLineTxPwrHighAlaPortn,'pm254dAlmLineTxBiasLowAlaPortn':pm254dAlmLineTxBiasLowAlaPortn,'pm254dAlmLineTxBiasHighAlaPortn':pm254dAlmLineTxBiasHighAlaPortn,'pm254dAlmLineVccLowAlaPortn':pm254dAlmLineVccLowAlaPortn,'pm254dAlmLineVccHighAlaPortn':pm254dAlmLineVccHighAlaPortn,'pm254dAlmLineTempLowAlaPortn':pm254dAlmLineTempLowAlaPortn,'pm254dAlmLineTempHighAlaPortn':pm254dAlmLineTempHighAlaPortn,'pm254dAlmLineRxPwrLowAlaPortn':pm254dAlmLineRxPwrLowAlaPortn,'pm254dAlmLineRxPwrHighAlaPortn':pm254dAlmLineRxPwrHighAlaPortn,'pm254dAlmLineCrit':pm254dAlmLineCrit,'pm254dAlmsynthAlmLineTable':pm254dAlmsynthAlmLineTable,'pm254dAlmsynthAlmLineEntry':pm254dAlmsynthAlmLineEntry,_d:pm254dAlmsynthAlmLineIndex,'pm254dAlmLineSfpAbsentPortn':pm254dAlmLineSfpAbsentPortn,'pm254dAlmLineDdmAbsentPortn':pm254dAlmLineDdmAbsentPortn,_O:pm254dAlmLineHwFailPortn,'pm254dAlmLineLsdPortn':pm254dAlmLineLsdPortn,'pm254dAlmLineLocalOosPortn':pm254dAlmLineLocalOosPortn,'pm254dAlmLineUpRdiInsPortn':pm254dAlmLineUpRdiInsPortn,_L:pm254dAlmLineDdmWarningPortn,_M:pm254dAlmLineDdmAlmPortn,_N:pm254dAlmLineFailPortn,'pm254dAlmDccActivePortn':pm254dAlmDccActivePortn,'pm254dAlmlineDfrmAlmTable':pm254dAlmlineDfrmAlmTable,'pm254dAlmlineDfrmAlmEntry':pm254dAlmlineDfrmAlmEntry,_e:pm254dAlmlineDfrmAlmIndex,'pm254dAlmLineDwAisDetPortn':pm254dAlmLineDwAisDetPortn,'pm254dAlmLineDwRdiDetPortn':pm254dAlmLineDwRdiDetPortn,'pm254dAlmLineDwOofPortn':pm254dAlmLineDwOofPortn,'pm254dAlmLineDwLofPortn':pm254dAlmLineDwLofPortn,'pm254dAlmDwLopPortn':pm254dAlmDwLopPortn,'pm254dAlmDwAuAisPortn':pm254dAlmDwAuAisPortn,'pm254dAlmlineIoAlmTable':pm254dAlmlineIoAlmTable,'pm254dAlmlineIoAlmEntry':pm254dAlmlineIoAlmEntry,_f:pm254dAlmlineIoAlmIndex,'pm254dAlmLineUpLasFailPortn':pm254dAlmLineUpLasFailPortn,'pm254dAlmLineDwLosPortn':pm254dAlmLineDwLosPortn,'pm254dmeasures':pm254dmeasures,'pm254dMesrOther':pm254dMesrOther,'pm254dMesrPort':pm254dMesrPort,'pm254dMesrclientTempMeasTable':pm254dMesrclientTempMeasTable,'pm254dMesrclientTempMeasEntry':pm254dMesrclientTempMeasEntry,_g:pm254dMesrclientTempMeasIndex,'pm254dMesrclientTempMeasPortn':pm254dMesrclientTempMeasPortn,'pm254dMesrclientVoltMeasTable':pm254dMesrclientVoltMeasTable,'pm254dMesrclientVoltMeasEntry':pm254dMesrclientVoltMeasEntry,_h:pm254dMesrclientVoltMeasIndex,'pm254dMesrclientVoltMeasPortn':pm254dMesrclientVoltMeasPortn,'pm254dMesrclientBiasMeasTable':pm254dMesrclientBiasMeasTable,'pm254dMesrclientBiasMeasEntry':pm254dMesrclientBiasMeasEntry,_i:pm254dMesrclientBiasMeasIndex,'pm254dMesrclientBiasMeasPortn':pm254dMesrclientBiasMeasPortn,'pm254dMesrclientTxpwrMeasTable':pm254dMesrclientTxpwrMeasTable,'pm254dMesrclientTxpwrMeasEntry':pm254dMesrclientTxpwrMeasEntry,_j:pm254dMesrclientTxpwrMeasIndex,'pm254dMesrclientTxpwrMeasPortn':pm254dMesrclientTxpwrMeasPortn,'pm254dMesrclientRxpwrMeasTable':pm254dMesrclientRxpwrMeasTable,'pm254dMesrclientRxpwrMeasEntry':pm254dMesrclientRxpwrMeasEntry,_k:pm254dMesrclientRxpwrMeasIndex,'pm254dMesrclientRxpwrMeasPortn':pm254dMesrclientRxpwrMeasPortn,'pm254dMesrLine':pm254dMesrLine,'pm254dMesrlineTempMeasTable':pm254dMesrlineTempMeasTable,'pm254dMesrlineTempMeasEntry':pm254dMesrlineTempMeasEntry,_l:pm254dMesrlineTempMeasIndex,'pm254dMesrlineTempMeasPortn':pm254dMesrlineTempMeasPortn,'pm254dMesrlineVoltMeasTable':pm254dMesrlineVoltMeasTable,'pm254dMesrlineVoltMeasEntry':pm254dMesrlineVoltMeasEntry,_m:pm254dMesrlineVoltMeasIndex,'pm254dMesrlineVoltMeasPortn':pm254dMesrlineVoltMeasPortn,'pm254dMesrlineBiasMeasTable':pm254dMesrlineBiasMeasTable,'pm254dMesrlineBiasMeasEntry':pm254dMesrlineBiasMeasEntry,_n:pm254dMesrlineBiasMeasIndex,'pm254dMesrlineBiasMeasPortn':pm254dMesrlineBiasMeasPortn,'pm254dMesrlineTxpwrMeasTable':pm254dMesrlineTxpwrMeasTable,'pm254dMesrlineTxpwrMeasEntry':pm254dMesrlineTxpwrMeasEntry,_o:pm254dMesrlineTxpwrMeasIndex,'pm254dMesrlineTxpwrMeasPortn':pm254dMesrlineTxpwrMeasPortn,'pm254dMesrlineRxpwrMeasTable':pm254dMesrlineRxpwrMeasTable,'pm254dMesrlineRxpwrMeasEntry':pm254dMesrlineRxpwrMeasEntry,_p:pm254dMesrlineRxpwrMeasIndex,'pm254dMesrlineRxpwrMeasPortn':pm254dMesrlineRxpwrMeasPortn,'pm254dcounters':pm254dcounters,'pm254dCntOther':pm254dCntOther,'pm254dCntPort':pm254dCntPort,'pm254dCntclientUpRaRemCntTable':pm254dCntclientUpRaRemCntTable,'pm254dCntclientUpRaRemCntEntry':pm254dCntclientUpRaRemCntEntry,_q:pm254dCntclientUpRaRemCntIndex,'pm254dCntclientUpRaRemCntValuePortn':pm254dCntclientUpRaRemCntValuePortn,'pm254dCntclientUpRaRemCntErrorPortn':pm254dCntclientUpRaRemCntErrorPortn,'pm254dCntclientUpRaRemCntOverloadPortn':pm254dCntclientUpRaRemCntOverloadPortn,'pm254dCntclientUpRaInsCntTable':pm254dCntclientUpRaInsCntTable,'pm254dCntclientUpRaInsCntEntry':pm254dCntclientUpRaInsCntEntry,_r:pm254dCntclientUpRaInsCntIndex,'pm254dCntclientUpRaInsCntValuePortn':pm254dCntclientUpRaInsCntValuePortn,'pm254dCntclientUpRaInsCntErrorPortn':pm254dCntclientUpRaInsCntErrorPortn,'pm254dCntclientUpRaInsCntOverloadPortn':pm254dCntclientUpRaInsCntOverloadPortn,'pm254dCntclientUpDispErrCntTable':pm254dCntclientUpDispErrCntTable,'pm254dCntclientUpDispErrCntEntry':pm254dCntclientUpDispErrCntEntry,_s:pm254dCntclientUpDispErrCntIndex,'pm254dCntclientUpDispErrCntValuePortn':pm254dCntclientUpDispErrCntValuePortn,'pm254dCntclientUpDispErrCntErrorPortn':pm254dCntclientUpDispErrCntErrorPortn,'pm254dCntclientUpDispErrCntOverloadPortn':pm254dCntclientUpDispErrCntOverloadPortn,'pm254dCntclientUpTimCntTable':pm254dCntclientUpTimCntTable,'pm254dCntclientUpTimCntEntry':pm254dCntclientUpTimCntEntry,_t:pm254dCntclientUpTimCntIndex,'pm254dCntclientUpTimCntValuePortn':pm254dCntclientUpTimCntValuePortn,'pm254dCntclientUpTimCntErrorPortn':pm254dCntclientUpTimCntErrorPortn,'pm254dCntclientUpTimCntOverloadPortn':pm254dCntclientUpTimCntOverloadPortn,'pm254dCntclientDwCbipCntTable':pm254dCntclientDwCbipCntTable,'pm254dCntclientDwCbipCntEntry':pm254dCntclientDwCbipCntEntry,_u:pm254dCntclientDwCbipCntIndex,'pm254dCntclientDwCbipCntValuePortn':pm254dCntclientDwCbipCntValuePortn,'pm254dCntclientDwCbipCntErrorPortn':pm254dCntclientDwCbipCntErrorPortn,'pm254dCntclientDwCbipCntOverloadPortn':pm254dCntclientDwCbipCntOverloadPortn,'pm254dCntclientDwTimCntTable':pm254dCntclientDwTimCntTable,'pm254dCntclientDwTimCntEntry':pm254dCntclientDwTimCntEntry,_v:pm254dCntclientDwTimCntIndex,'pm254dCntclientDwTimCntValuePortn':pm254dCntclientDwTimCntValuePortn,'pm254dCntclientDwTimCntErrorPortn':pm254dCntclientDwTimCntErrorPortn,'pm254dCntclientDwTimCntOverloadPortn':pm254dCntclientDwTimCntOverloadPortn,'pm254dCntLine':pm254dCntLine,'pm254dCntlineDfrmB1ErrCntTable':pm254dCntlineDfrmB1ErrCntTable,'pm254dCntlineDfrmB1ErrCntEntry':pm254dCntlineDfrmB1ErrCntEntry,_w:pm254dCntlineDfrmB1ErrCntIndex,'pm254dCntlineDfrmB1ErrCntValuePortn':pm254dCntlineDfrmB1ErrCntValuePortn,'pm254dCntlineDfrmB1ErrCntErrorPortn':pm254dCntlineDfrmB1ErrCntErrorPortn,'pm254dCntlineDfrmB1ErrCntOverloadPortn':pm254dCntlineDfrmB1ErrCntOverloadPortn,'pm254dCntlineDfrmTimCntTable':pm254dCntlineDfrmTimCntTable,'pm254dCntlineDfrmTimCntEntry':pm254dCntlineDfrmTimCntEntry,_x:pm254dCntlineDfrmTimCntIndex,'pm254dCntlineDfrmTimCntValuePortn':pm254dCntlineDfrmTimCntValuePortn,'pm254dCntlineDfrmTimCntErrorPortn':pm254dCntlineDfrmTimCntErrorPortn,'pm254dCntlineDfrmTimCntOverloadPortn':pm254dCntlineDfrmTimCntOverloadPortn,'pm254dCntCountersReset':pm254dCntCountersReset,'pm254dCntCountersStop':pm254dCntCountersStop,'pm254dcontrolsWrite':pm254dcontrolsWrite,'pm254dCtrlOther':pm254dCtrlOther,'pm254dCtrlconfMgnt1':pm254dCtrlconfMgnt1,'pm254dCtrlConf1Load1':pm254dCtrlConf1Load1,'pm254dCtrlConf2Load1':pm254dCtrlConf2Load1,'pm254dCtrlConf2Flash1':pm254dCtrlConf2Flash1,'pm254dCtrlConf2Clear1':pm254dCtrlConf2Clear1,'pm254dCtrlsynth4':pm254dCtrlsynth4,'pm254dCtrlCorrelatOn':pm254dCtrlCorrelatOn,'pm254dCtrlCorrelatOff':pm254dCtrlCorrelatOff,'pm254dCtrlswMgnt':pm254dCtrlswMgnt,'pm254dCtrlColdReset':pm254dCtrlColdReset,'pm254dCtrlWarmReset':pm254dCtrlWarmReset,'pm254dCtrlLoadSwBank1':pm254dCtrlLoadSwBank1,'pm254dCtrlLoadSwBank2':pm254dCtrlLoadSwBank2,'pm254dCtrlgwMgnt':pm254dCtrlgwMgnt,'pm254dCtrlCurrentGwReset':pm254dCtrlCurrentGwReset,'pm254dCtrlLoadGwBank1':pm254dCtrlLoadGwBank1,'pm254dCtrlLoadGwBank2':pm254dCtrlLoadGwBank2,'pm254dCtrlLoadGwBank3':pm254dCtrlLoadGwBank3,'pm254dCtrlLoadGwBank4':pm254dCtrlLoadGwBank4,'pm254dCtrlledTest':pm254dCtrlledTest,'pm254dCtrlGreenLed':pm254dCtrlGreenLed,'pm254dCtrlRedLed':pm254dCtrlRedLed,'pm254dCtrlLedOff':pm254dCtrlLedOff,'pm254dCtrlmoduleOosMode':pm254dCtrlmoduleOosMode,'pm254dCtrlModuleOosMode':pm254dCtrlModuleOosMode,'pm254dCtrlmaintenanceMode':pm254dCtrlmaintenanceMode,'pm254dCtrlMaintenanceMode':pm254dCtrlMaintenanceMode,'pm254dCtrlPort':pm254dCtrlPort,'pm254dCtrlclientAccessLoopTable':pm254dCtrlclientAccessLoopTable,'pm254dCtrlclientAccessLoopEntry':pm254dCtrlclientAccessLoopEntry,_y:pm254dCtrlclientAccessLoopIndex,'pm254dCtrlclientAccessLoopPortn':pm254dCtrlclientAccessLoopPortn,'pm254dCtrlclientOosModeTable':pm254dCtrlclientOosModeTable,'pm254dCtrlclientOosModeEntry':pm254dCtrlclientOosModeEntry,_z:pm254dCtrlclientOosModeIndex,'pm254dCtrlclientOosModePortn':pm254dCtrlclientOosModePortn,'pm254dCtrlclientSfpOnOffCtrlTable':pm254dCtrlclientSfpOnOffCtrlTable,'pm254dCtrlclientSfpOnOffCtrlEntry':pm254dCtrlclientSfpOnOffCtrlEntry,_A0:pm254dCtrlclientSfpOnOffCtrlIndex,'pm254dCtrlclientSfpOnOffCtrlPortn':pm254dCtrlclientSfpOnOffCtrlPortn,'pm254dCtrlclientCsfUpInsTable':pm254dCtrlclientCsfUpInsTable,'pm254dCtrlclientCsfUpInsEntry':pm254dCtrlclientCsfUpInsEntry,_A1:pm254dCtrlclientCsfUpInsIndex,'pm254dCtrlclientCsfUpInsPortn':pm254dCtrlclientCsfUpInsPortn,'pm254dCtrlclientCaisDwInsTable':pm254dCtrlclientCaisDwInsTable,'pm254dCtrlclientCaisDwInsEntry':pm254dCtrlclientCaisDwInsEntry,_A2:pm254dCtrlclientCaisDwInsIndex,'pm254dCtrlclientCaisDwInsPortn':pm254dCtrlclientCaisDwInsPortn,'pm254dCtrlclientAccessTermLoopTable':pm254dCtrlclientAccessTermLoopTable,'pm254dCtrlclientAccessTermLoopEntry':pm254dCtrlclientAccessTermLoopEntry,_A3:pm254dCtrlclientAccessTermLoopIndex,'pm254dCtrlclientAccessTermLoopPortn':pm254dCtrlclientAccessTermLoopPortn,'pm254dCtrlProtocolTable':pm254dCtrlProtocolTable,'pm254dCtrlProtocolEntry':pm254dCtrlProtocolEntry,_A4:pm254dCtrlProtocolIndex,'pm254dCtrlProtocolPortn':pm254dCtrlProtocolPortn,'pm254dCtrlLine':pm254dCtrlLine,'pm254dCtrllineMsAis':pm254dCtrllineMsAis,'pm254dCtrlLineMsAis':pm254dCtrlLineMsAis,'pm254dCtrllineUpS1Table':pm254dCtrllineUpS1Table,'pm254dCtrllineUpS1Entry':pm254dCtrllineUpS1Entry,_A5:pm254dCtrllineUpS1Index,'pm254dCtrllineUpS1Portn':pm254dCtrllineUpS1Portn,'pm254dCtrllineUpK1Table':pm254dCtrllineUpK1Table,'pm254dCtrllineUpK1Entry':pm254dCtrllineUpK1Entry,_A6:pm254dCtrllineUpK1Index,'pm254dCtrllineUpK1Portn':pm254dCtrllineUpK1Portn,'pm254dCtrllineUpK2Table':pm254dCtrllineUpK2Table,'pm254dCtrllineUpK2Entry':pm254dCtrllineUpK2Entry,_A7:pm254dCtrllineUpK2Index,'pm254dCtrllineUpK2Portn':pm254dCtrllineUpK2Portn,'pm254dCtrllineOosModeTable':pm254dCtrllineOosModeTable,'pm254dCtrllineOosModeEntry':pm254dCtrllineOosModeEntry,_A8:pm254dCtrllineOosModeIndex,'pm254dCtrllineOosModePortn':pm254dCtrllineOosModePortn,'pm254dCtrlDccMgnt':pm254dCtrlDccMgnt,'pm254dCtrlLineNumber':pm254dCtrlLineNumber,'pm254dCtrlDccMode':pm254dCtrlDccMode,'pm254dCtrllineAccessLoopTable':pm254dCtrllineAccessLoopTable,'pm254dCtrllineAccessLoopEntry':pm254dCtrllineAccessLoopEntry,_A9:pm254dCtrllineAccessLoopIndex,'pm254dCtrllineAccessLoopPortn':pm254dCtrllineAccessLoopPortn,'pm254dCtrllineLoopTransceiverTable':pm254dCtrllineLoopTransceiverTable,'pm254dCtrllineLoopTransceiverEntry':pm254dCtrllineLoopTransceiverEntry,_AA:pm254dCtrllineLoopTransceiverIndex,'pm254dCtrllineLoopTransceiverPortn':pm254dCtrllineLoopTransceiverPortn,'pm254dCtrllineSfpOnOffCtrlTable':pm254dCtrllineSfpOnOffCtrlTable,'pm254dCtrllineSfpOnOffCtrlEntry':pm254dCtrllineSfpOnOffCtrlEntry,_AB:pm254dCtrllineSfpOnOffCtrlIndex,'pm254dCtrllineSfpOnOffCtrlPortn':pm254dCtrllineSfpOnOffCtrlPortn,'pm254dCtrldccEnableTable':pm254dCtrldccEnableTable,'pm254dCtrldccEnableEntry':pm254dCtrldccEnableEntry,_AC:pm254dCtrldccEnableIndex,'pm254dCtrldccEnablePortn':pm254dCtrldccEnablePortn,'pm254dri':pm254dri,'pm254driTable':pm254driTable,'pm254dRinvClientTable':pm254dRinvClientTable,'pm254dRinvClientEntry':pm254dRinvClientEntry,_AD:pm254dRinvClientIndex,'pm254dRinvSfpClient':pm254dRinvSfpClient,'pm254dRinvLineTable':pm254dRinvLineTable,'pm254dRinvLineEntry':pm254dRinvLineEntry,_AE:pm254dRinvLineIndex,'pm254dRinvsfpLine':pm254dRinvsfpLine,'pm254dRinvReloadInventory':pm254dRinvReloadInventory,'pm254dRinvHwPlatform':pm254dRinvHwPlatform,'pm254dRinvModulePlatform':pm254dRinvModulePlatform,'pm254dRinvSwPlatform':pm254dRinvSwPlatform,'pm254dRinvGwPlatform':pm254dRinvGwPlatform,'pm254ddownload':pm254ddownload,'pm254dDwlOther':pm254dDwlOther,'pm254dDwlrestartProcess':pm254dDwlrestartProcess,'pm254dDwlWarmRestartProcessed':pm254dDwlWarmRestartProcessed,'pm254dDwlColdRestartProcessed':pm254dDwlColdRestartProcessed,'pm254dDwlswBanksUsed':pm254dDwlswBanksUsed,'pm254dDwlSwBank1Used':pm254dDwlSwBank1Used,'pm254dDwlSwBank2Used':pm254dDwlSwBank2Used,'pm254dDwlSwBank1Notempty':pm254dDwlSwBank1Notempty,'pm254dDwlSwBank2Notempty':pm254dDwlSwBank2Notempty,'pm254dDwlgwBanksUsed':pm254dDwlgwBanksUsed,'pm254dDwlGwBank1Used':pm254dDwlGwBank1Used,'pm254dDwlGwBank2Used':pm254dDwlGwBank2Used,'pm254dDwlGwBank3Used':pm254dDwlGwBank3Used,'pm254dDwlGwBank4Used':pm254dDwlGwBank4Used,'pm254dDwlGwBank1Notempty':pm254dDwlGwBank1Notempty,'pm254dDwlGwBank2Notempty':pm254dDwlGwBank2Notempty,'pm254dDwlGwBank3Notempty':pm254dDwlGwBank3Notempty,'pm254dDwlGwBank4Notempty':pm254dDwlGwBank4Notempty,'pm254dDwlPort':pm254dDwlPort,'pm254dDwlLine':pm254dDwlLine,'pm254dConfig':pm254dConfig,'pm254dCfgAccessCAisCsf':pm254dCfgAccessCAisCsf,'pm254dCfgClientcaiscsfTable':pm254dCfgClientcaiscsfTable,'pm254dCfgClientcaiscsfEntry':pm254dCfgClientcaiscsfEntry,_AF:pm254dCfgClientcaiscsfIndex,'pm254dCfgCAisModePortn':pm254dCfgCAisModePortn,'pm254dCfgSts24cContribPortn':pm254dCfgSts24cContribPortn,'pm254dCfgUpAccessioAlmPortn':pm254dCfgUpAccessioAlmPortn,'pm254dCfgUpMapperDeAlmPortn':pm254dCfgUpMapperDeAlmPortn,'pm254dCfgDownMapperDeAlmPortn':pm254dCfgDownMapperDeAlmPortn,'pm254dCfgDownDfrmAlmPortn':pm254dCfgDownDfrmAlmPortn,'pm254dCfgDownLineIoAlmPortn':pm254dCfgDownLineIoAlmPortn,'pm254dCfgStartup':pm254dCfgStartup,'pm254dCfgClientStartupTable':pm254dCfgClientStartupTable,'pm254dCfgClientStartupEntry':pm254dCfgClientStartupEntry,_AG:pm254dCfgClientStartupIndex,'pm254dCfgSystConfPortPortn':pm254dCfgSystConfPortPortn,'pm254dCfgNetConfPortPortn':pm254dCfgNetConfPortPortn,'pm254dCfgPortsOptionsPortn':pm254dCfgPortsOptionsPortn,'pm254dtablelineStartup':pm254dtablelineStartup,'pm254dCfgsystConfLine1':pm254dCfgsystConfLine1,'pm254dCfglineOptions1':pm254dCfglineOptions1,'pm254dCfgsystConfLine2':pm254dCfgsystConfLine2,'pm254dCfglineSelection':pm254dCfglineSelection,'pm254dCfglineOptions2':pm254dCfglineOptions2,'pm254dCfgLabels':pm254dCfgLabels,'pm254dCfgLabelclientTable':pm254dCfgLabelclientTable,'pm254dCfgLabelclientEntry':pm254dCfgLabelclientEntry,_AH:pm254dCfgLabelclientIndex,'pm254dCfgLabelclientPortn':pm254dCfgLabelclientPortn,'pm254dCfgLabellineTable':pm254dCfgLabellineTable,'pm254dCfgLabellineEntry':pm254dCfgLabellineEntry,_AI:pm254dCfgLabellineIndex,'pm254dCfgLabellinePortn':pm254dCfgLabellinePortn,'pm254dCfgWriteConfiguration':pm254dCfgWriteConfiguration,'pm254dtraps':pm254dtraps,_I:pm254dTrapPortNumber,_G:pm254dTrapBoardNumber,_H:pm254dTrapLineNumber,'pm254dLineTrapNotUrgentGoesOn':pm254dLineTrapNotUrgentGoesOn,'pm254dLineTrapNotUrgentGoesOff':pm254dLineTrapNotUrgentGoesOff,'pm254dLineTrapUrgentGoesOn':pm254dLineTrapUrgentGoesOn,'pm254dLineTrapUrgentGoesOff':pm254dLineTrapUrgentGoesOff,'pm254dLineTrapCritGoesOn':pm254dLineTrapCritGoesOn,'pm254dLineTrapCritGoesOff':pm254dLineTrapCritGoesOff,'pm254dClientTrapNotUrgentGoesOn':pm254dClientTrapNotUrgentGoesOn,'pm254dClientTrapNotUrgentGoesOff':pm254dClientTrapNotUrgentGoesOff,'pm254dClientTrapUrgentGoesOn':pm254dClientTrapUrgentGoesOn,'pm254dClientTrapUrgentGoesOff':pm254dClientTrapUrgentGoesOff,'pm254dClientTrapCritGoesOn':pm254dClientTrapCritGoesOn,'pm254dClientTrapCritGoesOff':pm254dClientTrapCritGoesOff,'pm254dMonitoring':pm254dMonitoring,'pm254dMonOther':pm254dMonOther,'pm254dMonRmon':pm254dMonRmon,'pm254dMonCountersReset':pm254dMonCountersReset,'pm254dMonCountersStop':pm254dMonCountersStop,'pm254dMonClient':pm254dMonClient,'pm254dMonClientRmonCounter':pm254dMonClientRmonCounter,'pm254dMonupRmonByteCntTable':pm254dMonupRmonByteCntTable,'pm254dMonupRmonByteCntEntry':pm254dMonupRmonByteCntEntry,_AJ:pm254dMonupRmonByteCntIndex,'pm254dMonupRmonByteCntValuePortn':pm254dMonupRmonByteCntValuePortn,'pm254dMonupRmonByteCntErrorPortn':pm254dMonupRmonByteCntErrorPortn,'pm254dMonupRmonByteCntOverloadPortn':pm254dMonupRmonByteCntOverloadPortn,'pm254dMonupRmonCrcErrorCntTable':pm254dMonupRmonCrcErrorCntTable,'pm254dMonupRmonCrcErrorCntEntry':pm254dMonupRmonCrcErrorCntEntry,_AK:pm254dMonupRmonCrcErrorCntIndex,'pm254dMonupRmonCrcErrorCntValuePortn':pm254dMonupRmonCrcErrorCntValuePortn,'pm254dMonupRmonCrcErrorCntErrorPortn':pm254dMonupRmonCrcErrorCntErrorPortn,'pm254dMonupRmonCrcErrorCntOverloadPortn':pm254dMonupRmonCrcErrorCntOverloadPortn,'pm254dMonupRmonPacketsCntTable':pm254dMonupRmonPacketsCntTable,'pm254dMonupRmonPacketsCntEntry':pm254dMonupRmonPacketsCntEntry,_AL:pm254dMonupRmonPacketsCntIndex,'pm254dMonupRmonPacketsCntValuePortn':pm254dMonupRmonPacketsCntValuePortn,'pm254dMonupRmonPacketsCntErrorPortn':pm254dMonupRmonPacketsCntErrorPortn,'pm254dMonupRmonPacketsCntOverloadPortn':pm254dMonupRmonPacketsCntOverloadPortn,'pm254dMonupRmonBroadcastCntTable':pm254dMonupRmonBroadcastCntTable,'pm254dMonupRmonBroadcastCntEntry':pm254dMonupRmonBroadcastCntEntry,_AM:pm254dMonupRmonBroadcastCntIndex,'pm254dMonupRmonBroadcastCntValuePortn':pm254dMonupRmonBroadcastCntValuePortn,'pm254dMonupRmonBroadcastCntErrorPortn':pm254dMonupRmonBroadcastCntErrorPortn,'pm254dMonupRmonBroadcastCntOverloadPortn':pm254dMonupRmonBroadcastCntOverloadPortn,'pm254dMonupRmonMulticastCntTable':pm254dMonupRmonMulticastCntTable,'pm254dMonupRmonMulticastCntEntry':pm254dMonupRmonMulticastCntEntry,_AN:pm254dMonupRmonMulticastCntIndex,'pm254dMonupRmonMulticastCntValuePortn':pm254dMonupRmonMulticastCntValuePortn,'pm254dMonupRmonMulticastCntErrorPortn':pm254dMonupRmonMulticastCntErrorPortn,'pm254dMonupRmonMulticastCntOverloadPortn':pm254dMonupRmonMulticastCntOverloadPortn})