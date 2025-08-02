_AX='pmo6006MondwRmonPacketsCounterClientInputIndex'
_AW='pmo6006MondwRmonCrcErrorsCounterClientInputIndex'
_AV='pmo6006MonupRmonPauseFrameCounterClientInputIndex'
_AU='pmo6006MonupRmonMulticastCounterClientInputIndex'
_AT='pmo6006MonupRmonBroadcastCounterClientInputIndex'
_AS='pmo6006MonupRmonPacketsCounterClientInputIndex'
_AR='pmo6006MonupRmonCrcErrorsCounterClientInputIndex'
_AQ='pmo6006MonupRmonBytesCounterClientInputIndex'
_AP='pmo6006CfgOtxtlhcapabilitiesIndex'
_AO='pmo6006CfgLineDapiAccOtuIndex'
_AN='pmo6006CfgLineDapiExpOtuIndex'
_AM='pmo6006CfgLineDapiTxOtuIndex'
_AL='pmo6006CfgLineSapiAccOtuIndex'
_AK='pmo6006CfgLineSapiExpOtuIndex'
_AJ='pmo6006CfgLineSapiTxOtuIndex'
_AI='pmo6006CfgClientDapiAccOduIndex'
_AH='pmo6006CfgClientDapiExpOduIndex'
_AG='pmo6006CfgClientDapiTxOduIndex'
_AF='pmo6006CfgClientSapiAccOduIndex'
_AE='pmo6006CfgClientSapiExpOduIndex'
_AD='pmo6006CfgClientSapiTxOduIndex'
_AC='pmo6006CfgLinexStartupOtuIndex'
_AB='pmo6006CfgClientStartupOduIndex'
_AA='pmo6006CfgLabellineIndex'
_A9='pmo6006CfgLabelclientIndex'
_A8='pmo6006CfgOtxtlhIndex'
_A7='pmo6006CfgLinexr1StartupIndex'
_A6='pmo6006CfgClientStartupIndex'
_A5='pmo6006RinvLineIndex'
_A4='pmo6006RinvSfpIndex'
_A3='pmo6006CtrllineBdiIndex'
_A2='pmo6006CtrlfecDisableIndex'
_A1='pmo6006CtrllineLoopIndex'
_A0='pmo6006CtrlcommAccessLoopIndex'
_z='pmo6006CtrlclientBdiIndex'
_y='pmo6006CtrlclientAisIndex'
_x='pmo6006CtrlclientLckIndex'
_w='pmo6006CtrlclientOciIndex'
_v='pmo6006CtrlcaisDwInsIndex'
_u='pmo6006CtrlcsfUpInsIndex'
_t='pmo6006CtrlclientLoopToLineIndex'
_s='pmo6006CtrlaccessLoopIndex'
_r='pmo6006CntlineDfrmTimCntIndex'
_q='pmo6006CntremoteLineSmBip8ErrorCounterIndex'
_p='pmo6006CntlocalLineFecCorrectedErrorsCounterIndex'
_o='pmo6006CntlocalLineSmBip8ErrorCounterIndex'
_n='pmo6006CntclientCbipCounterIndex'
_m='pmo6006CntclientRemoteBipIndex'
_l='pmo6006MesrlineRxPwrIndex'
_k='pmo6006MesrlineTxBiasIndex'
_j='pmo6006MesrlineTempIndex'
_i='pmo6006MesrlineTxPwrIndex'
_h='pmo6006MesrclientRxPwrIndex'
_g='pmo6006MesrclientTxPwrIndex'
_f='pmo6006MesrclientTxBiasIndex'
_e='pmo6006MesrclientTempIndex'
_d='pmo6006AlmsynthAlmLineIndex'
_c='pmo6006AlmlineHostLaneFaultIndex'
_b='pmo6006AlmlineNetworkLaneAlarmWarning2Index'
_a='pmo6006AlmlineNetworkLaneAlarmWarning1Index'
_Z='pmo6006AlmsynthAlmPortIndex'
_Y='pmo6006AlmclientSfpAlmDdmIndex'
_X='pmo6006AlmclientHostLaneFaultIndex'
_W='pmo6006AlmclientSfpWarnDdmIndex'
_V='sapidapi'
_U='pmo6006AlmDefFuseA'
_T='pmo6006AlmDefFuseB'
_S='pmo6006AlmHwFailAccPortn'
_R='pmo6006AlmFailAccPortn'
_Q='pmo6006AlmSfpDdmAlmPortn'
_P='pmo6006AlmSfpDdmWarningPortn'
_O='pmo6006AlmLineHwFailPortn'
_N='pmo6006AlmLineFailPortn'
_M='pmo6006AlmLineDdmAlmPortn'
_L='pmo6006AlmLineDdmWarningPortn'
_K='deprecated'
_J='pmo6006trapPortNumber'
_I='pmo6006trapLineNumber'
_H='pmo6006trapBoardNumber'
_G='DisplayString'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='EKINOPS-Pmo6006-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
modulePmo6006=ModuleIdentity((1,3,6,1,4,1,20044,70))
if mibBuilder.loadTexts:modulePmo6006.setRevisions(('2015-03-26 00:00','2015-03-30 00:00','2016-01-29 00:00','2016-05-20 00:00','2016-06-03 00:00'))
class Pmo6006OtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pmo6006DccMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dccNo',0),('dccLine1',1),('dccLine2',2)))
class Pmo6006LineChannel(TextualConvention,Integer32):status=_A
class Pmo6006Odu2SapiMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('sapi',1),('dapi',2),(_V,3)))
class Pmo6006Otu2SapiMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('sapi',1),('dapi',2),(_V,3)))
_Pmo6006alarms_ObjectIdentity=ObjectIdentity
pmo6006alarms=_Pmo6006alarms_ObjectIdentity((1,3,6,1,4,1,20044,70,2))
_Pmo6006AlmOther_ObjectIdentity=ObjectIdentity
pmo6006AlmOther=_Pmo6006AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,70,2,1))
_Pmo6006AlmOtherNurg_ObjectIdentity=ObjectIdentity
pmo6006AlmOtherNurg=_Pmo6006AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,70,2,1,1))
_Pmo6006AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmo6006AlmsynthAlm2=_Pmo6006AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,70,2,1,1,2))
_Pmo6006AlmConfTableSave_Type=EkiOnOff
_Pmo6006AlmConfTableSave_Object=MibScalar
pmo6006AlmConfTableSave=_Pmo6006AlmConfTableSave_Object((1,3,6,1,4,1,20044,70,2,1,1,2,1),_Pmo6006AlmConfTableSave_Type())
pmo6006AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmConfTableSave.setStatus(_A)
_Pmo6006AlmInvUpload_Type=EkiOnOff
_Pmo6006AlmInvUpload_Object=MibScalar
pmo6006AlmInvUpload=_Pmo6006AlmInvUpload_Object((1,3,6,1,4,1,20044,70,2,1,1,2,2),_Pmo6006AlmInvUpload_Type())
pmo6006AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmInvUpload.setStatus(_A)
_Pmo6006AlmConfTableLoad_Type=EkiOnOff
_Pmo6006AlmConfTableLoad_Object=MibScalar
pmo6006AlmConfTableLoad=_Pmo6006AlmConfTableLoad_Object((1,3,6,1,4,1,20044,70,2,1,1,2,3),_Pmo6006AlmConfTableLoad_Type())
pmo6006AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmConfTableLoad.setStatus(_A)
_Pmo6006AlmCorrelatOff_Type=EkiOnOff
_Pmo6006AlmCorrelatOff_Object=MibScalar
pmo6006AlmCorrelatOff=_Pmo6006AlmCorrelatOff_Object((1,3,6,1,4,1,20044,70,2,1,1,2,4),_Pmo6006AlmCorrelatOff_Type())
pmo6006AlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmCorrelatOff.setStatus(_A)
_Pmo6006AlmOtherUrg_ObjectIdentity=ObjectIdentity
pmo6006AlmOtherUrg=_Pmo6006AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,70,2,1,2))
_Pmo6006AlmOtherCrit_ObjectIdentity=ObjectIdentity
pmo6006AlmOtherCrit=_Pmo6006AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,70,2,1,3))
_Pmo6006AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmo6006AlmsynthAlm0=_Pmo6006AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,70,2,1,3,0))
_Pmo6006AlmModGlobFail_Type=EkiOnOff
_Pmo6006AlmModGlobFail_Object=MibScalar
pmo6006AlmModGlobFail=_Pmo6006AlmModGlobFail_Object((1,3,6,1,4,1,20044,70,2,1,3,0,9),_Pmo6006AlmModGlobFail_Type())
pmo6006AlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmModGlobFail.setStatus(_A)
_Pmo6006AlmDefFuseA_Type=EkiOnOff
_Pmo6006AlmDefFuseA_Object=MibScalar
pmo6006AlmDefFuseA=_Pmo6006AlmDefFuseA_Object((1,3,6,1,4,1,20044,70,2,1,3,0,15),_Pmo6006AlmDefFuseA_Type())
pmo6006AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmDefFuseA.setStatus(_A)
_Pmo6006AlmDefFuseB_Type=EkiOnOff
_Pmo6006AlmDefFuseB_Object=MibScalar
pmo6006AlmDefFuseB=_Pmo6006AlmDefFuseB_Object((1,3,6,1,4,1,20044,70,2,1,3,0,16),_Pmo6006AlmDefFuseB_Type())
pmo6006AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmDefFuseB.setStatus(_A)
_Pmo6006AlmClient_ObjectIdentity=ObjectIdentity
pmo6006AlmClient=_Pmo6006AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,70,2,2))
_Pmo6006AlmClientNurg_ObjectIdentity=ObjectIdentity
pmo6006AlmClientNurg=_Pmo6006AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,70,2,2,1))
_Pmo6006AlmclientSfpWarnDdmTable_Object=MibTable
pmo6006AlmclientSfpWarnDdmTable=_Pmo6006AlmclientSfpWarnDdmTable_Object((1,3,6,1,4,1,20044,70,2,2,1,232))
if mibBuilder.loadTexts:pmo6006AlmclientSfpWarnDdmTable.setStatus(_A)
_Pmo6006AlmclientSfpWarnDdmEntry_Object=MibTableRow
pmo6006AlmclientSfpWarnDdmEntry=_Pmo6006AlmclientSfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1))
pmo6006AlmclientSfpWarnDdmEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pmo6006AlmclientSfpWarnDdmEntry.setStatus(_A)
class _Pmo6006AlmclientSfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmclientSfpWarnDdmIndex_Type.__name__=_D
_Pmo6006AlmclientSfpWarnDdmIndex_Object=MibTableColumn
pmo6006AlmclientSfpWarnDdmIndex=_Pmo6006AlmclientSfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,1),_Pmo6006AlmclientSfpWarnDdmIndex_Type())
pmo6006AlmclientSfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmclientSfpWarnDdmIndex.setStatus(_A)
_Pmo6006AlmClientTxPwLowWngPortn_Type=EkiOnOff
_Pmo6006AlmClientTxPwLowWngPortn_Object=MibTableColumn
pmo6006AlmClientTxPwLowWngPortn=_Pmo6006AlmClientTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,2),_Pmo6006AlmClientTxPwLowWngPortn_Type())
pmo6006AlmClientTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxPwLowWngPortn.setStatus(_A)
_Pmo6006AlmClientTxPwrHighWngPortn_Type=EkiOnOff
_Pmo6006AlmClientTxPwrHighWngPortn_Object=MibTableColumn
pmo6006AlmClientTxPwrHighWngPortn=_Pmo6006AlmClientTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,3),_Pmo6006AlmClientTxPwrHighWngPortn_Type())
pmo6006AlmClientTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxPwrHighWngPortn.setStatus(_A)
_Pmo6006AlmClientTxBiasLowWngPortn_Type=EkiOnOff
_Pmo6006AlmClientTxBiasLowWngPortn_Object=MibTableColumn
pmo6006AlmClientTxBiasLowWngPortn=_Pmo6006AlmClientTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,4),_Pmo6006AlmClientTxBiasLowWngPortn_Type())
pmo6006AlmClientTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxBiasLowWngPortn.setStatus(_A)
_Pmo6006AlmClientTxBiasHighWngPortn_Type=EkiOnOff
_Pmo6006AlmClientTxBiasHighWngPortn_Object=MibTableColumn
pmo6006AlmClientTxBiasHighWngPortn=_Pmo6006AlmClientTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,5),_Pmo6006AlmClientTxBiasHighWngPortn_Type())
pmo6006AlmClientTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxBiasHighWngPortn.setStatus(_A)
_Pmo6006AlmClientVccLowWngPortn_Type=EkiOnOff
_Pmo6006AlmClientVccLowWngPortn_Object=MibTableColumn
pmo6006AlmClientVccLowWngPortn=_Pmo6006AlmClientVccLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,6),_Pmo6006AlmClientVccLowWngPortn_Type())
pmo6006AlmClientVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientVccLowWngPortn.setStatus(_A)
_Pmo6006AlmClientVccHighWngPortn_Type=EkiOnOff
_Pmo6006AlmClientVccHighWngPortn_Object=MibTableColumn
pmo6006AlmClientVccHighWngPortn=_Pmo6006AlmClientVccHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,7),_Pmo6006AlmClientVccHighWngPortn_Type())
pmo6006AlmClientVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientVccHighWngPortn.setStatus(_A)
_Pmo6006AlmClientTempLowWngPortn_Type=EkiOnOff
_Pmo6006AlmClientTempLowWngPortn_Object=MibTableColumn
pmo6006AlmClientTempLowWngPortn=_Pmo6006AlmClientTempLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,8),_Pmo6006AlmClientTempLowWngPortn_Type())
pmo6006AlmClientTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTempLowWngPortn.setStatus(_A)
_Pmo6006AlmClientTempHighWngPortn_Type=EkiOnOff
_Pmo6006AlmClientTempHighWngPortn_Object=MibTableColumn
pmo6006AlmClientTempHighWngPortn=_Pmo6006AlmClientTempHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,9),_Pmo6006AlmClientTempHighWngPortn_Type())
pmo6006AlmClientTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTempHighWngPortn.setStatus(_A)
_Pmo6006AlmClientRxPwrLowWngPortn_Type=EkiOnOff
_Pmo6006AlmClientRxPwrLowWngPortn_Object=MibTableColumn
pmo6006AlmClientRxPwrLowWngPortn=_Pmo6006AlmClientRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,16),_Pmo6006AlmClientRxPwrLowWngPortn_Type())
pmo6006AlmClientRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientRxPwrLowWngPortn.setStatus(_A)
_Pmo6006AlmClientRxPwrHighWngPortn_Type=EkiOnOff
_Pmo6006AlmClientRxPwrHighWngPortn_Object=MibTableColumn
pmo6006AlmClientRxPwrHighWngPortn=_Pmo6006AlmClientRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,2,1,232,1,17),_Pmo6006AlmClientRxPwrHighWngPortn_Type())
pmo6006AlmClientRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientRxPwrHighWngPortn.setStatus(_A)
_Pmo6006AlmClientUrg_ObjectIdentity=ObjectIdentity
pmo6006AlmClientUrg=_Pmo6006AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,70,2,2,2))
_Pmo6006AlmclientHostLaneFaultTable_Object=MibTable
pmo6006AlmclientHostLaneFaultTable=_Pmo6006AlmclientHostLaneFaultTable_Object((1,3,6,1,4,1,20044,70,2,2,2,88))
if mibBuilder.loadTexts:pmo6006AlmclientHostLaneFaultTable.setStatus(_A)
_Pmo6006AlmclientHostLaneFaultEntry_Object=MibTableRow
pmo6006AlmclientHostLaneFaultEntry=_Pmo6006AlmclientHostLaneFaultEntry_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1))
pmo6006AlmclientHostLaneFaultEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pmo6006AlmclientHostLaneFaultEntry.setStatus(_A)
class _Pmo6006AlmclientHostLaneFaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmclientHostLaneFaultIndex_Type.__name__=_D
_Pmo6006AlmclientHostLaneFaultIndex_Object=MibTableColumn
pmo6006AlmclientHostLaneFaultIndex=_Pmo6006AlmclientHostLaneFaultIndex_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,1),_Pmo6006AlmclientHostLaneFaultIndex_Type())
pmo6006AlmclientHostLaneFaultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmclientHostLaneFaultIndex.setStatus(_A)
_Pmo6006AlmClientLossOfSyncPortn_Type=EkiOnOff
_Pmo6006AlmClientLossOfSyncPortn_Object=MibTableColumn
pmo6006AlmClientLossOfSyncPortn=_Pmo6006AlmClientLossOfSyncPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,2),_Pmo6006AlmClientLossOfSyncPortn_Type())
pmo6006AlmClientLossOfSyncPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientLossOfSyncPortn.setStatus(_A)
_Pmo6006AlmClientInputLossOfSigPortn_Type=EkiOnOff
_Pmo6006AlmClientInputLossOfSigPortn_Object=MibTableColumn
pmo6006AlmClientInputLossOfSigPortn=_Pmo6006AlmClientInputLossOfSigPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,3),_Pmo6006AlmClientInputLossOfSigPortn_Type())
pmo6006AlmClientInputLossOfSigPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientInputLossOfSigPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDplmPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDplmPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDplmPortn=_Pmo6006AlmClientOdu2eDplmPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,4),_Pmo6006AlmClientOdu2eDplmPortn_Type())
pmo6006AlmClientOdu2eDplmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDplmPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDdegPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDdegPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDdegPortn=_Pmo6006AlmClientOdu2eDdegPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,6),_Pmo6006AlmClientOdu2eDdegPortn_Type())
pmo6006AlmClientOdu2eDdegPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDdegPortn.setStatus(_A)
_Pmo6006AlmClientCsfDetectedPortn_Type=EkiOnOff
_Pmo6006AlmClientCsfDetectedPortn_Object=MibTableColumn
pmo6006AlmClientCsfDetectedPortn=_Pmo6006AlmClientCsfDetectedPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,7),_Pmo6006AlmClientCsfDetectedPortn_Type())
pmo6006AlmClientCsfDetectedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientCsfDetectedPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eIaisPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eIaisPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eIaisPortn=_Pmo6006AlmClientOdu2eIaisPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,8),_Pmo6006AlmClientOdu2eIaisPortn_Type())
pmo6006AlmClientOdu2eIaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eIaisPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDtimPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDtimPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDtimPortn=_Pmo6006AlmClientOdu2eDtimPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,9),_Pmo6006AlmClientOdu2eDtimPortn_Type())
pmo6006AlmClientOdu2eDtimPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDtimPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDaisPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDaisPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDaisPortn=_Pmo6006AlmClientOdu2eDaisPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,10),_Pmo6006AlmClientOdu2eDaisPortn_Type())
pmo6006AlmClientOdu2eDaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDaisPortn.setStatus(_A)
_Pmo6006AlmClientLaneTxFifoErrorPortn_Type=EkiOnOff
_Pmo6006AlmClientLaneTxFifoErrorPortn_Object=MibTableColumn
pmo6006AlmClientLaneTxFifoErrorPortn=_Pmo6006AlmClientLaneTxFifoErrorPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,11),_Pmo6006AlmClientLaneTxFifoErrorPortn_Type())
pmo6006AlmClientLaneTxFifoErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientLaneTxFifoErrorPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eIociPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eIociPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eIociPortn=_Pmo6006AlmClientOdu2eIociPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,12),_Pmo6006AlmClientOdu2eIociPortn_Type())
pmo6006AlmClientOdu2eIociPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eIociPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDociPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDociPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDociPortn=_Pmo6006AlmClientOdu2eDociPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,13),_Pmo6006AlmClientOdu2eDociPortn_Type())
pmo6006AlmClientOdu2eDociPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDociPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eIbdiPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eIbdiPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eIbdiPortn=_Pmo6006AlmClientOdu2eIbdiPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,14),_Pmo6006AlmClientOdu2eIbdiPortn_Type())
pmo6006AlmClientOdu2eIbdiPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eIbdiPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDbdiPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDbdiPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDbdiPortn=_Pmo6006AlmClientOdu2eDbdiPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,15),_Pmo6006AlmClientOdu2eDbdiPortn_Type())
pmo6006AlmClientOdu2eDbdiPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDbdiPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eIlckPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eIlckPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eIlckPortn=_Pmo6006AlmClientOdu2eIlckPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,16),_Pmo6006AlmClientOdu2eIlckPortn_Type())
pmo6006AlmClientOdu2eIlckPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eIlckPortn.setStatus(_A)
_Pmo6006AlmClientOdu2eDlckPortn_Type=EkiOnOff
_Pmo6006AlmClientOdu2eDlckPortn_Object=MibTableColumn
pmo6006AlmClientOdu2eDlckPortn=_Pmo6006AlmClientOdu2eDlckPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,88,1,17),_Pmo6006AlmClientOdu2eDlckPortn_Type())
pmo6006AlmClientOdu2eDlckPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOdu2eDlckPortn.setStatus(_A)
_Pmo6006AlmclientSfpAlmDdmTable_Object=MibTable
pmo6006AlmclientSfpAlmDdmTable=_Pmo6006AlmclientSfpAlmDdmTable_Object((1,3,6,1,4,1,20044,70,2,2,2,216))
if mibBuilder.loadTexts:pmo6006AlmclientSfpAlmDdmTable.setStatus(_A)
_Pmo6006AlmclientSfpAlmDdmEntry_Object=MibTableRow
pmo6006AlmclientSfpAlmDdmEntry=_Pmo6006AlmclientSfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1))
pmo6006AlmclientSfpAlmDdmEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pmo6006AlmclientSfpAlmDdmEntry.setStatus(_A)
class _Pmo6006AlmclientSfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmclientSfpAlmDdmIndex_Type.__name__=_D
_Pmo6006AlmclientSfpAlmDdmIndex_Object=MibTableColumn
pmo6006AlmclientSfpAlmDdmIndex=_Pmo6006AlmclientSfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,1),_Pmo6006AlmclientSfpAlmDdmIndex_Type())
pmo6006AlmclientSfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmclientSfpAlmDdmIndex.setStatus(_A)
_Pmo6006AlmClientTxPwrLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientTxPwrLowAlaPortn_Object=MibTableColumn
pmo6006AlmClientTxPwrLowAlaPortn=_Pmo6006AlmClientTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,2),_Pmo6006AlmClientTxPwrLowAlaPortn_Type())
pmo6006AlmClientTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxPwrLowAlaPortn.setStatus(_A)
_Pmo6006AlmClientTxPwrHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientTxPwrHighAlaPortn_Object=MibTableColumn
pmo6006AlmClientTxPwrHighAlaPortn=_Pmo6006AlmClientTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,3),_Pmo6006AlmClientTxPwrHighAlaPortn_Type())
pmo6006AlmClientTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxPwrHighAlaPortn.setStatus(_A)
_Pmo6006AlmClientTxBiasLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientTxBiasLowAlaPortn_Object=MibTableColumn
pmo6006AlmClientTxBiasLowAlaPortn=_Pmo6006AlmClientTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,4),_Pmo6006AlmClientTxBiasLowAlaPortn_Type())
pmo6006AlmClientTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxBiasLowAlaPortn.setStatus(_A)
_Pmo6006AlmClientTxBiasHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientTxBiasHighAlaPortn_Object=MibTableColumn
pmo6006AlmClientTxBiasHighAlaPortn=_Pmo6006AlmClientTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,5),_Pmo6006AlmClientTxBiasHighAlaPortn_Type())
pmo6006AlmClientTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTxBiasHighAlaPortn.setStatus(_A)
_Pmo6006AlmClientVccLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientVccLowAlaPortn_Object=MibTableColumn
pmo6006AlmClientVccLowAlaPortn=_Pmo6006AlmClientVccLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,6),_Pmo6006AlmClientVccLowAlaPortn_Type())
pmo6006AlmClientVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientVccLowAlaPortn.setStatus(_A)
_Pmo6006AlmClientVccHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientVccHighAlaPortn_Object=MibTableColumn
pmo6006AlmClientVccHighAlaPortn=_Pmo6006AlmClientVccHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,7),_Pmo6006AlmClientVccHighAlaPortn_Type())
pmo6006AlmClientVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientVccHighAlaPortn.setStatus(_A)
_Pmo6006AlmClientTempLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientTempLowAlaPortn_Object=MibTableColumn
pmo6006AlmClientTempLowAlaPortn=_Pmo6006AlmClientTempLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,8),_Pmo6006AlmClientTempLowAlaPortn_Type())
pmo6006AlmClientTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTempLowAlaPortn.setStatus(_A)
_Pmo6006AlmClientTempHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientTempHighAlaPortn_Object=MibTableColumn
pmo6006AlmClientTempHighAlaPortn=_Pmo6006AlmClientTempHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,9),_Pmo6006AlmClientTempHighAlaPortn_Type())
pmo6006AlmClientTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientTempHighAlaPortn.setStatus(_A)
_Pmo6006AlmClientRxPwrLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientRxPwrLowAlaPortn_Object=MibTableColumn
pmo6006AlmClientRxPwrLowAlaPortn=_Pmo6006AlmClientRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,16),_Pmo6006AlmClientRxPwrLowAlaPortn_Type())
pmo6006AlmClientRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientRxPwrLowAlaPortn.setStatus(_A)
_Pmo6006AlmClientRxPwrHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmClientRxPwrHighAlaPortn_Object=MibTableColumn
pmo6006AlmClientRxPwrHighAlaPortn=_Pmo6006AlmClientRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,2,2,216,1,17),_Pmo6006AlmClientRxPwrHighAlaPortn_Type())
pmo6006AlmClientRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientRxPwrHighAlaPortn.setStatus(_A)
_Pmo6006AlmClientCrit_ObjectIdentity=ObjectIdentity
pmo6006AlmClientCrit=_Pmo6006AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,70,2,2,3))
_Pmo6006AlmsynthAlmPortTable_Object=MibTable
pmo6006AlmsynthAlmPortTable=_Pmo6006AlmsynthAlmPortTable_Object((1,3,6,1,4,1,20044,70,2,2,3,8))
if mibBuilder.loadTexts:pmo6006AlmsynthAlmPortTable.setStatus(_A)
_Pmo6006AlmsynthAlmPortEntry_Object=MibTableRow
pmo6006AlmsynthAlmPortEntry=_Pmo6006AlmsynthAlmPortEntry_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1))
pmo6006AlmsynthAlmPortEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pmo6006AlmsynthAlmPortEntry.setStatus(_A)
class _Pmo6006AlmsynthAlmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmsynthAlmPortIndex_Type.__name__=_D
_Pmo6006AlmsynthAlmPortIndex_Object=MibTableColumn
pmo6006AlmsynthAlmPortIndex=_Pmo6006AlmsynthAlmPortIndex_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,1),_Pmo6006AlmsynthAlmPortIndex_Type())
pmo6006AlmsynthAlmPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmsynthAlmPortIndex.setStatus(_A)
_Pmo6006AlmSfpAbsentPortn_Type=EkiOnOff
_Pmo6006AlmSfpAbsentPortn_Object=MibTableColumn
pmo6006AlmSfpAbsentPortn=_Pmo6006AlmSfpAbsentPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,2),_Pmo6006AlmSfpAbsentPortn_Type())
pmo6006AlmSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmSfpAbsentPortn.setStatus(_A)
_Pmo6006AlmDdmAbsentPortn_Type=EkiOnOff
_Pmo6006AlmDdmAbsentPortn_Object=MibTableColumn
pmo6006AlmDdmAbsentPortn=_Pmo6006AlmDdmAbsentPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,3),_Pmo6006AlmDdmAbsentPortn_Type())
pmo6006AlmDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmDdmAbsentPortn.setStatus(_A)
_Pmo6006AlmHwFailAccPortn_Type=EkiOnOff
_Pmo6006AlmHwFailAccPortn_Object=MibTableColumn
pmo6006AlmHwFailAccPortn=_Pmo6006AlmHwFailAccPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,5),_Pmo6006AlmHwFailAccPortn_Type())
pmo6006AlmHwFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmHwFailAccPortn.setStatus(_A)
_Pmo6006AlmDwLsdPortn_Type=EkiOnOff
_Pmo6006AlmDwLsdPortn_Object=MibTableColumn
pmo6006AlmDwLsdPortn=_Pmo6006AlmDwLsdPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,6),_Pmo6006AlmDwLsdPortn_Type())
pmo6006AlmDwLsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmDwLsdPortn.setStatus(_A)
_Pmo6006AlmClientLocalOosPortn_Type=EkiOnOff
_Pmo6006AlmClientLocalOosPortn_Object=MibTableColumn
pmo6006AlmClientLocalOosPortn=_Pmo6006AlmClientLocalOosPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,7),_Pmo6006AlmClientLocalOosPortn_Type())
pmo6006AlmClientLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientLocalOosPortn.setStatus(_A)
_Pmo6006AlmClientRemoteOosPortn_Type=EkiOnOff
_Pmo6006AlmClientRemoteOosPortn_Object=MibTableColumn
pmo6006AlmClientRemoteOosPortn=_Pmo6006AlmClientRemoteOosPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,8),_Pmo6006AlmClientRemoteOosPortn_Type())
pmo6006AlmClientRemoteOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientRemoteOosPortn.setStatus(_A)
_Pmo6006AlmDwCaisPortn_Type=EkiOnOff
_Pmo6006AlmDwCaisPortn_Object=MibTableColumn
pmo6006AlmDwCaisPortn=_Pmo6006AlmDwCaisPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,9),_Pmo6006AlmDwCaisPortn_Type())
pmo6006AlmDwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmDwCaisPortn.setStatus(_A)
_Pmo6006AlmSfpDdmWarningPortn_Type=EkiOnOff
_Pmo6006AlmSfpDdmWarningPortn_Object=MibTableColumn
pmo6006AlmSfpDdmWarningPortn=_Pmo6006AlmSfpDdmWarningPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,10),_Pmo6006AlmSfpDdmWarningPortn_Type())
pmo6006AlmSfpDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmSfpDdmWarningPortn.setStatus(_A)
_Pmo6006AlmSfpDdmAlmPortn_Type=EkiOnOff
_Pmo6006AlmSfpDdmAlmPortn_Object=MibTableColumn
pmo6006AlmSfpDdmAlmPortn=_Pmo6006AlmSfpDdmAlmPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,11),_Pmo6006AlmSfpDdmAlmPortn_Type())
pmo6006AlmSfpDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmSfpDdmAlmPortn.setStatus(_A)
_Pmo6006AlmFailAccPortn_Type=EkiOnOff
_Pmo6006AlmFailAccPortn_Object=MibTableColumn
pmo6006AlmFailAccPortn=_Pmo6006AlmFailAccPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,13),_Pmo6006AlmFailAccPortn_Type())
pmo6006AlmFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmFailAccPortn.setStatus(_A)
_Pmo6006AlmUpCsfPortn_Type=EkiOnOff
_Pmo6006AlmUpCsfPortn_Object=MibTableColumn
pmo6006AlmUpCsfPortn=_Pmo6006AlmUpCsfPortn_Object((1,3,6,1,4,1,20044,70,2,2,3,8,1,17),_Pmo6006AlmUpCsfPortn_Type())
pmo6006AlmUpCsfPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmUpCsfPortn.setStatus(_A)
_Pmo6006AlmLine_ObjectIdentity=ObjectIdentity
pmo6006AlmLine=_Pmo6006AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,70,2,3))
_Pmo6006AlmLineNurg_ObjectIdentity=ObjectIdentity
pmo6006AlmLineNurg=_Pmo6006AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,70,2,3,1))
_Pmo6006AlmLineUrg_ObjectIdentity=ObjectIdentity
pmo6006AlmLineUrg=_Pmo6006AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,70,2,3,2))
_Pmo6006AlmlineNetworkLaneAlarmWarning1Table_Object=MibTable
pmo6006AlmlineNetworkLaneAlarmWarning1Table=_Pmo6006AlmlineNetworkLaneAlarmWarning1Table_Object((1,3,6,1,4,1,20044,70,2,3,2,104))
if mibBuilder.loadTexts:pmo6006AlmlineNetworkLaneAlarmWarning1Table.setStatus(_A)
_Pmo6006AlmlineNetworkLaneAlarmWarning1Entry_Object=MibTableRow
pmo6006AlmlineNetworkLaneAlarmWarning1Entry=_Pmo6006AlmlineNetworkLaneAlarmWarning1Entry_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1))
pmo6006AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pmo6006AlmlineNetworkLaneAlarmWarning1Entry.setStatus(_A)
class _Pmo6006AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmlineNetworkLaneAlarmWarning1Index_Type.__name__=_D
_Pmo6006AlmlineNetworkLaneAlarmWarning1Index_Object=MibTableColumn
pmo6006AlmlineNetworkLaneAlarmWarning1Index=_Pmo6006AlmlineNetworkLaneAlarmWarning1Index_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,1),_Pmo6006AlmlineNetworkLaneAlarmWarning1Index_Type())
pmo6006AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmlineNetworkLaneAlarmWarning1Index.setStatus(_A)
_Pmo6006AlmLineTxPwrLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineTxPwrLowAlaPortn_Object=MibTableColumn
pmo6006AlmLineTxPwrLowAlaPortn=_Pmo6006AlmLineTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,2),_Pmo6006AlmLineTxPwrLowAlaPortn_Type())
pmo6006AlmLineTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxPwrLowAlaPortn.setStatus(_A)
_Pmo6006AlmLineTxPwrHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineTxPwrHighAlaPortn_Object=MibTableColumn
pmo6006AlmLineTxPwrHighAlaPortn=_Pmo6006AlmLineTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,3),_Pmo6006AlmLineTxPwrHighAlaPortn_Type())
pmo6006AlmLineTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxPwrHighAlaPortn.setStatus(_A)
_Pmo6006AlmLineTxBiasLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineTxBiasLowAlaPortn_Object=MibTableColumn
pmo6006AlmLineTxBiasLowAlaPortn=_Pmo6006AlmLineTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,4),_Pmo6006AlmLineTxBiasLowAlaPortn_Type())
pmo6006AlmLineTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxBiasLowAlaPortn.setStatus(_A)
_Pmo6006AlmLineTxBiasHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineTxBiasHighAlaPortn_Object=MibTableColumn
pmo6006AlmLineTxBiasHighAlaPortn=_Pmo6006AlmLineTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,5),_Pmo6006AlmLineTxBiasHighAlaPortn_Type())
pmo6006AlmLineTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxBiasHighAlaPortn.setStatus(_A)
_Pmo6006AlmLineVccLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineVccLowAlaPortn_Object=MibTableColumn
pmo6006AlmLineVccLowAlaPortn=_Pmo6006AlmLineVccLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,6),_Pmo6006AlmLineVccLowAlaPortn_Type())
pmo6006AlmLineVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineVccLowAlaPortn.setStatus(_A)
_Pmo6006AlmLineVccHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineVccHighAlaPortn_Object=MibTableColumn
pmo6006AlmLineVccHighAlaPortn=_Pmo6006AlmLineVccHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,7),_Pmo6006AlmLineVccHighAlaPortn_Type())
pmo6006AlmLineVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineVccHighAlaPortn.setStatus(_A)
_Pmo6006AlmLineTempLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineTempLowAlaPortn_Object=MibTableColumn
pmo6006AlmLineTempLowAlaPortn=_Pmo6006AlmLineTempLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,8),_Pmo6006AlmLineTempLowAlaPortn_Type())
pmo6006AlmLineTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTempLowAlaPortn.setStatus(_A)
_Pmo6006AlmLineTempHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineTempHighAlaPortn_Object=MibTableColumn
pmo6006AlmLineTempHighAlaPortn=_Pmo6006AlmLineTempHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,9),_Pmo6006AlmLineTempHighAlaPortn_Type())
pmo6006AlmLineTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTempHighAlaPortn.setStatus(_A)
_Pmo6006AlmLineRxPwrLowAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineRxPwrLowAlaPortn_Object=MibTableColumn
pmo6006AlmLineRxPwrLowAlaPortn=_Pmo6006AlmLineRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,16),_Pmo6006AlmLineRxPwrLowAlaPortn_Type())
pmo6006AlmLineRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineRxPwrLowAlaPortn.setStatus(_A)
_Pmo6006AlmLineRxPwrHighAlaPortn_Type=EkiOnOff
_Pmo6006AlmLineRxPwrHighAlaPortn_Object=MibTableColumn
pmo6006AlmLineRxPwrHighAlaPortn=_Pmo6006AlmLineRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,104,1,17),_Pmo6006AlmLineRxPwrHighAlaPortn_Type())
pmo6006AlmLineRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineRxPwrHighAlaPortn.setStatus(_A)
_Pmo6006AlmlineNetworkLaneAlarmWarning2Table_Object=MibTable
pmo6006AlmlineNetworkLaneAlarmWarning2Table=_Pmo6006AlmlineNetworkLaneAlarmWarning2Table_Object((1,3,6,1,4,1,20044,70,2,3,2,120))
if mibBuilder.loadTexts:pmo6006AlmlineNetworkLaneAlarmWarning2Table.setStatus(_A)
_Pmo6006AlmlineNetworkLaneAlarmWarning2Entry_Object=MibTableRow
pmo6006AlmlineNetworkLaneAlarmWarning2Entry=_Pmo6006AlmlineNetworkLaneAlarmWarning2Entry_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1))
pmo6006AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pmo6006AlmlineNetworkLaneAlarmWarning2Entry.setStatus(_A)
class _Pmo6006AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmlineNetworkLaneAlarmWarning2Index_Type.__name__=_D
_Pmo6006AlmlineNetworkLaneAlarmWarning2Index_Object=MibTableColumn
pmo6006AlmlineNetworkLaneAlarmWarning2Index=_Pmo6006AlmlineNetworkLaneAlarmWarning2Index_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,1),_Pmo6006AlmlineNetworkLaneAlarmWarning2Index_Type())
pmo6006AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmlineNetworkLaneAlarmWarning2Index.setStatus(_A)
_Pmo6006AlmLineTxPwLowWngPortn_Type=EkiOnOff
_Pmo6006AlmLineTxPwLowWngPortn_Object=MibTableColumn
pmo6006AlmLineTxPwLowWngPortn=_Pmo6006AlmLineTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,2),_Pmo6006AlmLineTxPwLowWngPortn_Type())
pmo6006AlmLineTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxPwLowWngPortn.setStatus(_A)
_Pmo6006AlmLineTxPwrHighWngPortn_Type=EkiOnOff
_Pmo6006AlmLineTxPwrHighWngPortn_Object=MibTableColumn
pmo6006AlmLineTxPwrHighWngPortn=_Pmo6006AlmLineTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,3),_Pmo6006AlmLineTxPwrHighWngPortn_Type())
pmo6006AlmLineTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxPwrHighWngPortn.setStatus(_A)
_Pmo6006AlmLineTxBiasLowWngPortn_Type=EkiOnOff
_Pmo6006AlmLineTxBiasLowWngPortn_Object=MibTableColumn
pmo6006AlmLineTxBiasLowWngPortn=_Pmo6006AlmLineTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,4),_Pmo6006AlmLineTxBiasLowWngPortn_Type())
pmo6006AlmLineTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxBiasLowWngPortn.setStatus(_A)
_Pmo6006AlmLineTxBiasHighWngPortn_Type=EkiOnOff
_Pmo6006AlmLineTxBiasHighWngPortn_Object=MibTableColumn
pmo6006AlmLineTxBiasHighWngPortn=_Pmo6006AlmLineTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,5),_Pmo6006AlmLineTxBiasHighWngPortn_Type())
pmo6006AlmLineTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxBiasHighWngPortn.setStatus(_A)
_Pmo6006AlmLineVccLowWngPortn_Type=EkiOnOff
_Pmo6006AlmLineVccLowWngPortn_Object=MibTableColumn
pmo6006AlmLineVccLowWngPortn=_Pmo6006AlmLineVccLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,6),_Pmo6006AlmLineVccLowWngPortn_Type())
pmo6006AlmLineVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineVccLowWngPortn.setStatus(_A)
_Pmo6006AlmLineVccHighWngPortn_Type=EkiOnOff
_Pmo6006AlmLineVccHighWngPortn_Object=MibTableColumn
pmo6006AlmLineVccHighWngPortn=_Pmo6006AlmLineVccHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,7),_Pmo6006AlmLineVccHighWngPortn_Type())
pmo6006AlmLineVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineVccHighWngPortn.setStatus(_A)
_Pmo6006AlmLineTempLowWngPortn_Type=EkiOnOff
_Pmo6006AlmLineTempLowWngPortn_Object=MibTableColumn
pmo6006AlmLineTempLowWngPortn=_Pmo6006AlmLineTempLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,8),_Pmo6006AlmLineTempLowWngPortn_Type())
pmo6006AlmLineTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTempLowWngPortn.setStatus(_A)
_Pmo6006AlmLineTempHighWngPortn_Type=EkiOnOff
_Pmo6006AlmLineTempHighWngPortn_Object=MibTableColumn
pmo6006AlmLineTempHighWngPortn=_Pmo6006AlmLineTempHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,9),_Pmo6006AlmLineTempHighWngPortn_Type())
pmo6006AlmLineTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTempHighWngPortn.setStatus(_A)
_Pmo6006AlmLineRxPwrLowWngPortn_Type=EkiOnOff
_Pmo6006AlmLineRxPwrLowWngPortn_Object=MibTableColumn
pmo6006AlmLineRxPwrLowWngPortn=_Pmo6006AlmLineRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,16),_Pmo6006AlmLineRxPwrLowWngPortn_Type())
pmo6006AlmLineRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineRxPwrLowWngPortn.setStatus(_A)
_Pmo6006AlmLineRxPwrHighWngPortn_Type=EkiOnOff
_Pmo6006AlmLineRxPwrHighWngPortn_Object=MibTableColumn
pmo6006AlmLineRxPwrHighWngPortn=_Pmo6006AlmLineRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,120,1,17),_Pmo6006AlmLineRxPwrHighWngPortn_Type())
pmo6006AlmLineRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineRxPwrHighWngPortn.setStatus(_A)
_Pmo6006AlmlineHostLaneFaultTable_Object=MibTable
pmo6006AlmlineHostLaneFaultTable=_Pmo6006AlmlineHostLaneFaultTable_Object((1,3,6,1,4,1,20044,70,2,3,2,152))
if mibBuilder.loadTexts:pmo6006AlmlineHostLaneFaultTable.setStatus(_A)
_Pmo6006AlmlineHostLaneFaultEntry_Object=MibTableRow
pmo6006AlmlineHostLaneFaultEntry=_Pmo6006AlmlineHostLaneFaultEntry_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1))
pmo6006AlmlineHostLaneFaultEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pmo6006AlmlineHostLaneFaultEntry.setStatus(_A)
class _Pmo6006AlmlineHostLaneFaultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmlineHostLaneFaultIndex_Type.__name__=_D
_Pmo6006AlmlineHostLaneFaultIndex_Object=MibTableColumn
pmo6006AlmlineHostLaneFaultIndex=_Pmo6006AlmlineHostLaneFaultIndex_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,1),_Pmo6006AlmlineHostLaneFaultIndex_Type())
pmo6006AlmlineHostLaneFaultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmlineHostLaneFaultIndex.setStatus(_A)
_Pmo6006AlmLineInputLossOfSignalPortn_Type=EkiOnOff
_Pmo6006AlmLineInputLossOfSignalPortn_Object=MibTableColumn
pmo6006AlmLineInputLossOfSignalPortn=_Pmo6006AlmLineInputLossOfSignalPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,2),_Pmo6006AlmLineInputLossOfSignalPortn_Type())
pmo6006AlmLineInputLossOfSignalPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineInputLossOfSignalPortn.setStatus(_A)
_Pmo6006AlmLineLossOfFramePortn_Type=EkiOnOff
_Pmo6006AlmLineLossOfFramePortn_Object=MibTableColumn
pmo6006AlmLineLossOfFramePortn=_Pmo6006AlmLineLossOfFramePortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,3),_Pmo6006AlmLineLossOfFramePortn_Type())
pmo6006AlmLineLossOfFramePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineLossOfFramePortn.setStatus(_A)
_Pmo6006AlmLineSmBdiInsertedPortn_Type=EkiOnOff
_Pmo6006AlmLineSmBdiInsertedPortn_Object=MibTableColumn
pmo6006AlmLineSmBdiInsertedPortn=_Pmo6006AlmLineSmBdiInsertedPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,4),_Pmo6006AlmLineSmBdiInsertedPortn_Type())
pmo6006AlmLineSmBdiInsertedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineSmBdiInsertedPortn.setStatus(_A)
_Pmo6006AlmLineSmBdiDetectedPortn_Type=EkiOnOff
_Pmo6006AlmLineSmBdiDetectedPortn_Object=MibTableColumn
pmo6006AlmLineSmBdiDetectedPortn=_Pmo6006AlmLineSmBdiDetectedPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,5),_Pmo6006AlmLineSmBdiDetectedPortn_Type())
pmo6006AlmLineSmBdiDetectedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineSmBdiDetectedPortn.setStatus(_A)
_Pmo6006AlmOtu2eDdegPortn_Type=EkiOnOff
_Pmo6006AlmOtu2eDdegPortn_Object=MibTableColumn
pmo6006AlmOtu2eDdegPortn=_Pmo6006AlmOtu2eDdegPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,8),_Pmo6006AlmOtu2eDdegPortn_Type())
pmo6006AlmOtu2eDdegPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmOtu2eDdegPortn.setStatus(_A)
_Pmo6006AlmClientOtu2eDtimPortn_Type=EkiOnOff
_Pmo6006AlmClientOtu2eDtimPortn_Object=MibTableColumn
pmo6006AlmClientOtu2eDtimPortn=_Pmo6006AlmClientOtu2eDtimPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,9),_Pmo6006AlmClientOtu2eDtimPortn_Type())
pmo6006AlmClientOtu2eDtimPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmClientOtu2eDtimPortn.setStatus(_A)
_Pmo6006AlmLineOchr2eDlosPPortn_Type=EkiOnOff
_Pmo6006AlmLineOchr2eDlosPPortn_Object=MibTableColumn
pmo6006AlmLineOchr2eDlosPPortn=_Pmo6006AlmLineOchr2eDlosPPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,12),_Pmo6006AlmLineOchr2eDlosPPortn_Type())
pmo6006AlmLineOchr2eDlosPPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineOchr2eDlosPPortn.setStatus(_A)
_Pmo6006AlmLineOtu2eDssfPortn_Type=EkiOnOff
_Pmo6006AlmLineOtu2eDssfPortn_Object=MibTableColumn
pmo6006AlmLineOtu2eDssfPortn=_Pmo6006AlmLineOtu2eDssfPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,16),_Pmo6006AlmLineOtu2eDssfPortn_Type())
pmo6006AlmLineOtu2eDssfPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineOtu2eDssfPortn.setStatus(_A)
_Pmo6006AlmLineOtu2eDlomPortn_Type=EkiOnOff
_Pmo6006AlmLineOtu2eDlomPortn_Object=MibTableColumn
pmo6006AlmLineOtu2eDlomPortn=_Pmo6006AlmLineOtu2eDlomPortn_Object((1,3,6,1,4,1,20044,70,2,3,2,152,1,17),_Pmo6006AlmLineOtu2eDlomPortn_Type())
pmo6006AlmLineOtu2eDlomPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineOtu2eDlomPortn.setStatus(_A)
_Pmo6006AlmLineCrit_ObjectIdentity=ObjectIdentity
pmo6006AlmLineCrit=_Pmo6006AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,70,2,3,3))
_Pmo6006AlmsynthAlmLineTable_Object=MibTable
pmo6006AlmsynthAlmLineTable=_Pmo6006AlmsynthAlmLineTable_Object((1,3,6,1,4,1,20044,70,2,3,3,24))
if mibBuilder.loadTexts:pmo6006AlmsynthAlmLineTable.setStatus(_A)
_Pmo6006AlmsynthAlmLineEntry_Object=MibTableRow
pmo6006AlmsynthAlmLineEntry=_Pmo6006AlmsynthAlmLineEntry_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1))
pmo6006AlmsynthAlmLineEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pmo6006AlmsynthAlmLineEntry.setStatus(_A)
class _Pmo6006AlmsynthAlmLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006AlmsynthAlmLineIndex_Type.__name__=_D
_Pmo6006AlmsynthAlmLineIndex_Object=MibTableColumn
pmo6006AlmsynthAlmLineIndex=_Pmo6006AlmsynthAlmLineIndex_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,1),_Pmo6006AlmsynthAlmLineIndex_Type())
pmo6006AlmsynthAlmLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmsynthAlmLineIndex.setStatus(_A)
_Pmo6006AlmLineSfpAbsentPortn_Type=EkiOnOff
_Pmo6006AlmLineSfpAbsentPortn_Object=MibTableColumn
pmo6006AlmLineSfpAbsentPortn=_Pmo6006AlmLineSfpAbsentPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,2),_Pmo6006AlmLineSfpAbsentPortn_Type())
pmo6006AlmLineSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineSfpAbsentPortn.setStatus(_A)
_Pmo6006AlmLineDdmAbsentPortn_Type=EkiOnOff
_Pmo6006AlmLineDdmAbsentPortn_Object=MibTableColumn
pmo6006AlmLineDdmAbsentPortn=_Pmo6006AlmLineDdmAbsentPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,3),_Pmo6006AlmLineDdmAbsentPortn_Type())
pmo6006AlmLineDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineDdmAbsentPortn.setStatus(_A)
_Pmo6006AlmLineHwFailPortn_Type=EkiOnOff
_Pmo6006AlmLineHwFailPortn_Object=MibTableColumn
pmo6006AlmLineHwFailPortn=_Pmo6006AlmLineHwFailPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,5),_Pmo6006AlmLineHwFailPortn_Type())
pmo6006AlmLineHwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineHwFailPortn.setStatus(_A)
_Pmo6006AlmLineTxOffPortn_Type=EkiOnOff
_Pmo6006AlmLineTxOffPortn_Object=MibTableColumn
pmo6006AlmLineTxOffPortn=_Pmo6006AlmLineTxOffPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,6),_Pmo6006AlmLineTxOffPortn_Type())
pmo6006AlmLineTxOffPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineTxOffPortn.setStatus(_A)
_Pmo6006AlmLineLocalOosPortn_Type=EkiOnOff
_Pmo6006AlmLineLocalOosPortn_Object=MibTableColumn
pmo6006AlmLineLocalOosPortn=_Pmo6006AlmLineLocalOosPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,7),_Pmo6006AlmLineLocalOosPortn_Type())
pmo6006AlmLineLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineLocalOosPortn.setStatus(_A)
_Pmo6006AlmUpRdiInsPortn_Type=EkiOnOff
_Pmo6006AlmUpRdiInsPortn_Object=MibTableColumn
pmo6006AlmUpRdiInsPortn=_Pmo6006AlmUpRdiInsPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,9),_Pmo6006AlmUpRdiInsPortn_Type())
pmo6006AlmUpRdiInsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmUpRdiInsPortn.setStatus(_A)
_Pmo6006AlmLineDdmWarningPortn_Type=EkiOnOff
_Pmo6006AlmLineDdmWarningPortn_Object=MibTableColumn
pmo6006AlmLineDdmWarningPortn=_Pmo6006AlmLineDdmWarningPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,10),_Pmo6006AlmLineDdmWarningPortn_Type())
pmo6006AlmLineDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineDdmWarningPortn.setStatus(_A)
_Pmo6006AlmLineDdmAlmPortn_Type=EkiOnOff
_Pmo6006AlmLineDdmAlmPortn_Object=MibTableColumn
pmo6006AlmLineDdmAlmPortn=_Pmo6006AlmLineDdmAlmPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,11),_Pmo6006AlmLineDdmAlmPortn_Type())
pmo6006AlmLineDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineDdmAlmPortn.setStatus(_A)
_Pmo6006AlmLineFailPortn_Type=EkiOnOff
_Pmo6006AlmLineFailPortn_Object=MibTableColumn
pmo6006AlmLineFailPortn=_Pmo6006AlmLineFailPortn_Object((1,3,6,1,4,1,20044,70,2,3,3,24,1,13),_Pmo6006AlmLineFailPortn_Type())
pmo6006AlmLineFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006AlmLineFailPortn.setStatus(_A)
_Pmo6006measures_ObjectIdentity=ObjectIdentity
pmo6006measures=_Pmo6006measures_ObjectIdentity((1,3,6,1,4,1,20044,70,3))
_Pmo6006MesrOther_ObjectIdentity=ObjectIdentity
pmo6006MesrOther=_Pmo6006MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,70,3,1))
_Pmo6006MesrClient_ObjectIdentity=ObjectIdentity
pmo6006MesrClient=_Pmo6006MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,70,3,2))
_Pmo6006MesrclientTempTable_Object=MibTable
pmo6006MesrclientTempTable=_Pmo6006MesrclientTempTable_Object((1,3,6,1,4,1,20044,70,3,2,16))
if mibBuilder.loadTexts:pmo6006MesrclientTempTable.setStatus(_A)
_Pmo6006MesrclientTempEntry_Object=MibTableRow
pmo6006MesrclientTempEntry=_Pmo6006MesrclientTempEntry_Object((1,3,6,1,4,1,20044,70,3,2,16,1))
pmo6006MesrclientTempEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pmo6006MesrclientTempEntry.setStatus(_A)
class _Pmo6006MesrclientTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrclientTempIndex_Type.__name__=_D
_Pmo6006MesrclientTempIndex_Object=MibTableColumn
pmo6006MesrclientTempIndex=_Pmo6006MesrclientTempIndex_Object((1,3,6,1,4,1,20044,70,3,2,16,1,1),_Pmo6006MesrclientTempIndex_Type())
pmo6006MesrclientTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientTempIndex.setStatus(_A)
class _Pmo6006MesrclientTempPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrclientTempPortn_Type.__name__=_D
_Pmo6006MesrclientTempPortn_Object=MibTableColumn
pmo6006MesrclientTempPortn=_Pmo6006MesrclientTempPortn_Object((1,3,6,1,4,1,20044,70,3,2,16,1,2),_Pmo6006MesrclientTempPortn_Type())
pmo6006MesrclientTempPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientTempPortn.setStatus(_A)
_Pmo6006MesrclientTxBiasTable_Object=MibTable
pmo6006MesrclientTxBiasTable=_Pmo6006MesrclientTxBiasTable_Object((1,3,6,1,4,1,20044,70,3,2,32))
if mibBuilder.loadTexts:pmo6006MesrclientTxBiasTable.setStatus(_A)
_Pmo6006MesrclientTxBiasEntry_Object=MibTableRow
pmo6006MesrclientTxBiasEntry=_Pmo6006MesrclientTxBiasEntry_Object((1,3,6,1,4,1,20044,70,3,2,32,1))
pmo6006MesrclientTxBiasEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pmo6006MesrclientTxBiasEntry.setStatus(_A)
class _Pmo6006MesrclientTxBiasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrclientTxBiasIndex_Type.__name__=_D
_Pmo6006MesrclientTxBiasIndex_Object=MibTableColumn
pmo6006MesrclientTxBiasIndex=_Pmo6006MesrclientTxBiasIndex_Object((1,3,6,1,4,1,20044,70,3,2,32,1,1),_Pmo6006MesrclientTxBiasIndex_Type())
pmo6006MesrclientTxBiasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientTxBiasIndex.setStatus(_A)
class _Pmo6006MesrclientTxBiasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrclientTxBiasPortn_Type.__name__=_D
_Pmo6006MesrclientTxBiasPortn_Object=MibTableColumn
pmo6006MesrclientTxBiasPortn=_Pmo6006MesrclientTxBiasPortn_Object((1,3,6,1,4,1,20044,70,3,2,32,1,2),_Pmo6006MesrclientTxBiasPortn_Type())
pmo6006MesrclientTxBiasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientTxBiasPortn.setStatus(_A)
_Pmo6006MesrclientTxPwrTable_Object=MibTable
pmo6006MesrclientTxPwrTable=_Pmo6006MesrclientTxPwrTable_Object((1,3,6,1,4,1,20044,70,3,2,48))
if mibBuilder.loadTexts:pmo6006MesrclientTxPwrTable.setStatus(_A)
_Pmo6006MesrclientTxPwrEntry_Object=MibTableRow
pmo6006MesrclientTxPwrEntry=_Pmo6006MesrclientTxPwrEntry_Object((1,3,6,1,4,1,20044,70,3,2,48,1))
pmo6006MesrclientTxPwrEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pmo6006MesrclientTxPwrEntry.setStatus(_A)
class _Pmo6006MesrclientTxPwrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrclientTxPwrIndex_Type.__name__=_D
_Pmo6006MesrclientTxPwrIndex_Object=MibTableColumn
pmo6006MesrclientTxPwrIndex=_Pmo6006MesrclientTxPwrIndex_Object((1,3,6,1,4,1,20044,70,3,2,48,1,1),_Pmo6006MesrclientTxPwrIndex_Type())
pmo6006MesrclientTxPwrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientTxPwrIndex.setStatus(_A)
class _Pmo6006MesrclientTxPwrPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrclientTxPwrPortn_Type.__name__=_D
_Pmo6006MesrclientTxPwrPortn_Object=MibTableColumn
pmo6006MesrclientTxPwrPortn=_Pmo6006MesrclientTxPwrPortn_Object((1,3,6,1,4,1,20044,70,3,2,48,1,2),_Pmo6006MesrclientTxPwrPortn_Type())
pmo6006MesrclientTxPwrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientTxPwrPortn.setStatus(_A)
_Pmo6006MesrclientRxPwrTable_Object=MibTable
pmo6006MesrclientRxPwrTable=_Pmo6006MesrclientRxPwrTable_Object((1,3,6,1,4,1,20044,70,3,2,64))
if mibBuilder.loadTexts:pmo6006MesrclientRxPwrTable.setStatus(_A)
_Pmo6006MesrclientRxPwrEntry_Object=MibTableRow
pmo6006MesrclientRxPwrEntry=_Pmo6006MesrclientRxPwrEntry_Object((1,3,6,1,4,1,20044,70,3,2,64,1))
pmo6006MesrclientRxPwrEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pmo6006MesrclientRxPwrEntry.setStatus(_A)
class _Pmo6006MesrclientRxPwrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrclientRxPwrIndex_Type.__name__=_D
_Pmo6006MesrclientRxPwrIndex_Object=MibTableColumn
pmo6006MesrclientRxPwrIndex=_Pmo6006MesrclientRxPwrIndex_Object((1,3,6,1,4,1,20044,70,3,2,64,1,1),_Pmo6006MesrclientRxPwrIndex_Type())
pmo6006MesrclientRxPwrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientRxPwrIndex.setStatus(_A)
class _Pmo6006MesrclientRxPwrPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrclientRxPwrPortn_Type.__name__=_D
_Pmo6006MesrclientRxPwrPortn_Object=MibTableColumn
pmo6006MesrclientRxPwrPortn=_Pmo6006MesrclientRxPwrPortn_Object((1,3,6,1,4,1,20044,70,3,2,64,1,2),_Pmo6006MesrclientRxPwrPortn_Type())
pmo6006MesrclientRxPwrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrclientRxPwrPortn.setStatus(_A)
_Pmo6006MesrLine_ObjectIdentity=ObjectIdentity
pmo6006MesrLine=_Pmo6006MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,70,3,3))
_Pmo6006MesrlineTxPwrTable_Object=MibTable
pmo6006MesrlineTxPwrTable=_Pmo6006MesrlineTxPwrTable_Object((1,3,6,1,4,1,20044,70,3,3,80))
if mibBuilder.loadTexts:pmo6006MesrlineTxPwrTable.setStatus(_A)
_Pmo6006MesrlineTxPwrEntry_Object=MibTableRow
pmo6006MesrlineTxPwrEntry=_Pmo6006MesrlineTxPwrEntry_Object((1,3,6,1,4,1,20044,70,3,3,80,1))
pmo6006MesrlineTxPwrEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pmo6006MesrlineTxPwrEntry.setStatus(_A)
class _Pmo6006MesrlineTxPwrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrlineTxPwrIndex_Type.__name__=_D
_Pmo6006MesrlineTxPwrIndex_Object=MibTableColumn
pmo6006MesrlineTxPwrIndex=_Pmo6006MesrlineTxPwrIndex_Object((1,3,6,1,4,1,20044,70,3,3,80,1,1),_Pmo6006MesrlineTxPwrIndex_Type())
pmo6006MesrlineTxPwrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineTxPwrIndex.setStatus(_A)
class _Pmo6006MesrlineTxPwrPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrlineTxPwrPortn_Type.__name__=_D
_Pmo6006MesrlineTxPwrPortn_Object=MibTableColumn
pmo6006MesrlineTxPwrPortn=_Pmo6006MesrlineTxPwrPortn_Object((1,3,6,1,4,1,20044,70,3,3,80,1,2),_Pmo6006MesrlineTxPwrPortn_Type())
pmo6006MesrlineTxPwrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineTxPwrPortn.setStatus(_A)
_Pmo6006MesrlineTempTable_Object=MibTable
pmo6006MesrlineTempTable=_Pmo6006MesrlineTempTable_Object((1,3,6,1,4,1,20044,70,3,3,96))
if mibBuilder.loadTexts:pmo6006MesrlineTempTable.setStatus(_A)
_Pmo6006MesrlineTempEntry_Object=MibTableRow
pmo6006MesrlineTempEntry=_Pmo6006MesrlineTempEntry_Object((1,3,6,1,4,1,20044,70,3,3,96,1))
pmo6006MesrlineTempEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pmo6006MesrlineTempEntry.setStatus(_A)
class _Pmo6006MesrlineTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrlineTempIndex_Type.__name__=_D
_Pmo6006MesrlineTempIndex_Object=MibTableColumn
pmo6006MesrlineTempIndex=_Pmo6006MesrlineTempIndex_Object((1,3,6,1,4,1,20044,70,3,3,96,1,1),_Pmo6006MesrlineTempIndex_Type())
pmo6006MesrlineTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineTempIndex.setStatus(_A)
class _Pmo6006MesrlineTempPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrlineTempPortn_Type.__name__=_D
_Pmo6006MesrlineTempPortn_Object=MibTableColumn
pmo6006MesrlineTempPortn=_Pmo6006MesrlineTempPortn_Object((1,3,6,1,4,1,20044,70,3,3,96,1,2),_Pmo6006MesrlineTempPortn_Type())
pmo6006MesrlineTempPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineTempPortn.setStatus(_A)
_Pmo6006MesrlineTxBiasTable_Object=MibTable
pmo6006MesrlineTxBiasTable=_Pmo6006MesrlineTxBiasTable_Object((1,3,6,1,4,1,20044,70,3,3,112))
if mibBuilder.loadTexts:pmo6006MesrlineTxBiasTable.setStatus(_A)
_Pmo6006MesrlineTxBiasEntry_Object=MibTableRow
pmo6006MesrlineTxBiasEntry=_Pmo6006MesrlineTxBiasEntry_Object((1,3,6,1,4,1,20044,70,3,3,112,1))
pmo6006MesrlineTxBiasEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pmo6006MesrlineTxBiasEntry.setStatus(_A)
class _Pmo6006MesrlineTxBiasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrlineTxBiasIndex_Type.__name__=_D
_Pmo6006MesrlineTxBiasIndex_Object=MibTableColumn
pmo6006MesrlineTxBiasIndex=_Pmo6006MesrlineTxBiasIndex_Object((1,3,6,1,4,1,20044,70,3,3,112,1,1),_Pmo6006MesrlineTxBiasIndex_Type())
pmo6006MesrlineTxBiasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineTxBiasIndex.setStatus(_A)
class _Pmo6006MesrlineTxBiasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrlineTxBiasPortn_Type.__name__=_D
_Pmo6006MesrlineTxBiasPortn_Object=MibTableColumn
pmo6006MesrlineTxBiasPortn=_Pmo6006MesrlineTxBiasPortn_Object((1,3,6,1,4,1,20044,70,3,3,112,1,2),_Pmo6006MesrlineTxBiasPortn_Type())
pmo6006MesrlineTxBiasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineTxBiasPortn.setStatus(_A)
_Pmo6006MesrlineRxPwrTable_Object=MibTable
pmo6006MesrlineRxPwrTable=_Pmo6006MesrlineRxPwrTable_Object((1,3,6,1,4,1,20044,70,3,3,128))
if mibBuilder.loadTexts:pmo6006MesrlineRxPwrTable.setStatus(_A)
_Pmo6006MesrlineRxPwrEntry_Object=MibTableRow
pmo6006MesrlineRxPwrEntry=_Pmo6006MesrlineRxPwrEntry_Object((1,3,6,1,4,1,20044,70,3,3,128,1))
pmo6006MesrlineRxPwrEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pmo6006MesrlineRxPwrEntry.setStatus(_A)
class _Pmo6006MesrlineRxPwrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MesrlineRxPwrIndex_Type.__name__=_D
_Pmo6006MesrlineRxPwrIndex_Object=MibTableColumn
pmo6006MesrlineRxPwrIndex=_Pmo6006MesrlineRxPwrIndex_Object((1,3,6,1,4,1,20044,70,3,3,128,1,1),_Pmo6006MesrlineRxPwrIndex_Type())
pmo6006MesrlineRxPwrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineRxPwrIndex.setStatus(_A)
class _Pmo6006MesrlineRxPwrPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmo6006MesrlineRxPwrPortn_Type.__name__=_D
_Pmo6006MesrlineRxPwrPortn_Object=MibTableColumn
pmo6006MesrlineRxPwrPortn=_Pmo6006MesrlineRxPwrPortn_Object((1,3,6,1,4,1,20044,70,3,3,128,1,2),_Pmo6006MesrlineRxPwrPortn_Type())
pmo6006MesrlineRxPwrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MesrlineRxPwrPortn.setStatus(_A)
_Pmo6006counters_ObjectIdentity=ObjectIdentity
pmo6006counters=_Pmo6006counters_ObjectIdentity((1,3,6,1,4,1,20044,70,4))
_Pmo6006CntOther_ObjectIdentity=ObjectIdentity
pmo6006CntOther=_Pmo6006CntOther_ObjectIdentity((1,3,6,1,4,1,20044,70,4,1))
_Pmo6006CntClient_ObjectIdentity=ObjectIdentity
pmo6006CntClient=_Pmo6006CntClient_ObjectIdentity((1,3,6,1,4,1,20044,70,4,2))
_Pmo6006CntclientRemoteBipTable_Object=MibTable
pmo6006CntclientRemoteBipTable=_Pmo6006CntclientRemoteBipTable_Object((1,3,6,1,4,1,20044,70,4,2,64))
if mibBuilder.loadTexts:pmo6006CntclientRemoteBipTable.setStatus(_A)
_Pmo6006CntclientRemoteBipEntry_Object=MibTableRow
pmo6006CntclientRemoteBipEntry=_Pmo6006CntclientRemoteBipEntry_Object((1,3,6,1,4,1,20044,70,4,2,64,1))
pmo6006CntclientRemoteBipEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pmo6006CntclientRemoteBipEntry.setStatus(_A)
class _Pmo6006CntclientRemoteBipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CntclientRemoteBipIndex_Type.__name__=_D
_Pmo6006CntclientRemoteBipIndex_Object=MibTableColumn
pmo6006CntclientRemoteBipIndex=_Pmo6006CntclientRemoteBipIndex_Object((1,3,6,1,4,1,20044,70,4,2,64,1,1),_Pmo6006CntclientRemoteBipIndex_Type())
pmo6006CntclientRemoteBipIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientRemoteBipIndex.setStatus(_A)
_Pmo6006CntclientRemoteBipValuePortn_Type=Counter32
_Pmo6006CntclientRemoteBipValuePortn_Object=MibTableColumn
pmo6006CntclientRemoteBipValuePortn=_Pmo6006CntclientRemoteBipValuePortn_Object((1,3,6,1,4,1,20044,70,4,2,64,1,2),_Pmo6006CntclientRemoteBipValuePortn_Type())
pmo6006CntclientRemoteBipValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientRemoteBipValuePortn.setStatus(_A)
_Pmo6006CntclientRemoteBipErrorPortn_Type=EkiOnOff
_Pmo6006CntclientRemoteBipErrorPortn_Object=MibTableColumn
pmo6006CntclientRemoteBipErrorPortn=_Pmo6006CntclientRemoteBipErrorPortn_Object((1,3,6,1,4,1,20044,70,4,2,64,1,3),_Pmo6006CntclientRemoteBipErrorPortn_Type())
pmo6006CntclientRemoteBipErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientRemoteBipErrorPortn.setStatus(_A)
_Pmo6006CntclientRemoteBipOverloadPortn_Type=EkiOnOff
_Pmo6006CntclientRemoteBipOverloadPortn_Object=MibTableColumn
pmo6006CntclientRemoteBipOverloadPortn=_Pmo6006CntclientRemoteBipOverloadPortn_Object((1,3,6,1,4,1,20044,70,4,2,64,1,4),_Pmo6006CntclientRemoteBipOverloadPortn_Type())
pmo6006CntclientRemoteBipOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientRemoteBipOverloadPortn.setStatus(_A)
_Pmo6006CntclientCbipCounterTable_Object=MibTable
pmo6006CntclientCbipCounterTable=_Pmo6006CntclientCbipCounterTable_Object((1,3,6,1,4,1,20044,70,4,2,96))
if mibBuilder.loadTexts:pmo6006CntclientCbipCounterTable.setStatus(_A)
_Pmo6006CntclientCbipCounterEntry_Object=MibTableRow
pmo6006CntclientCbipCounterEntry=_Pmo6006CntclientCbipCounterEntry_Object((1,3,6,1,4,1,20044,70,4,2,96,1))
pmo6006CntclientCbipCounterEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pmo6006CntclientCbipCounterEntry.setStatus(_A)
class _Pmo6006CntclientCbipCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CntclientCbipCounterIndex_Type.__name__=_D
_Pmo6006CntclientCbipCounterIndex_Object=MibTableColumn
pmo6006CntclientCbipCounterIndex=_Pmo6006CntclientCbipCounterIndex_Object((1,3,6,1,4,1,20044,70,4,2,96,1,1),_Pmo6006CntclientCbipCounterIndex_Type())
pmo6006CntclientCbipCounterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientCbipCounterIndex.setStatus(_A)
_Pmo6006CntclientCbipCounterValuePortn_Type=Counter32
_Pmo6006CntclientCbipCounterValuePortn_Object=MibTableColumn
pmo6006CntclientCbipCounterValuePortn=_Pmo6006CntclientCbipCounterValuePortn_Object((1,3,6,1,4,1,20044,70,4,2,96,1,2),_Pmo6006CntclientCbipCounterValuePortn_Type())
pmo6006CntclientCbipCounterValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientCbipCounterValuePortn.setStatus(_A)
_Pmo6006CntclientCbipCounterErrorPortn_Type=EkiOnOff
_Pmo6006CntclientCbipCounterErrorPortn_Object=MibTableColumn
pmo6006CntclientCbipCounterErrorPortn=_Pmo6006CntclientCbipCounterErrorPortn_Object((1,3,6,1,4,1,20044,70,4,2,96,1,3),_Pmo6006CntclientCbipCounterErrorPortn_Type())
pmo6006CntclientCbipCounterErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientCbipCounterErrorPortn.setStatus(_A)
_Pmo6006CntclientCbipCounterOverloadPortn_Type=EkiOnOff
_Pmo6006CntclientCbipCounterOverloadPortn_Object=MibTableColumn
pmo6006CntclientCbipCounterOverloadPortn=_Pmo6006CntclientCbipCounterOverloadPortn_Object((1,3,6,1,4,1,20044,70,4,2,96,1,4),_Pmo6006CntclientCbipCounterOverloadPortn_Type())
pmo6006CntclientCbipCounterOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntclientCbipCounterOverloadPortn.setStatus(_A)
_Pmo6006CntLine_ObjectIdentity=ObjectIdentity
pmo6006CntLine=_Pmo6006CntLine_ObjectIdentity((1,3,6,1,4,1,20044,70,4,3))
_Pmo6006CntlocalLineSmBip8ErrorCounterTable_Object=MibTable
pmo6006CntlocalLineSmBip8ErrorCounterTable=_Pmo6006CntlocalLineSmBip8ErrorCounterTable_Object((1,3,6,1,4,1,20044,70,4,3,192))
if mibBuilder.loadTexts:pmo6006CntlocalLineSmBip8ErrorCounterTable.setStatus(_A)
_Pmo6006CntlocalLineSmBip8ErrorCounterEntry_Object=MibTableRow
pmo6006CntlocalLineSmBip8ErrorCounterEntry=_Pmo6006CntlocalLineSmBip8ErrorCounterEntry_Object((1,3,6,1,4,1,20044,70,4,3,192,1))
pmo6006CntlocalLineSmBip8ErrorCounterEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pmo6006CntlocalLineSmBip8ErrorCounterEntry.setStatus(_A)
class _Pmo6006CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CntlocalLineSmBip8ErrorCounterIndex_Type.__name__=_D
_Pmo6006CntlocalLineSmBip8ErrorCounterIndex_Object=MibTableColumn
pmo6006CntlocalLineSmBip8ErrorCounterIndex=_Pmo6006CntlocalLineSmBip8ErrorCounterIndex_Object((1,3,6,1,4,1,20044,70,4,3,192,1,1),_Pmo6006CntlocalLineSmBip8ErrorCounterIndex_Type())
pmo6006CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineSmBip8ErrorCounterIndex.setStatus(_A)
_Pmo6006CntlocalLineSmBip8ErrorCounterValuePortn_Type=Counter32
_Pmo6006CntlocalLineSmBip8ErrorCounterValuePortn_Object=MibTableColumn
pmo6006CntlocalLineSmBip8ErrorCounterValuePortn=_Pmo6006CntlocalLineSmBip8ErrorCounterValuePortn_Object((1,3,6,1,4,1,20044,70,4,3,192,1,2),_Pmo6006CntlocalLineSmBip8ErrorCounterValuePortn_Type())
pmo6006CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineSmBip8ErrorCounterValuePortn.setStatus(_A)
_Pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn_Type=EkiOnOff
_Pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn_Object=MibTableColumn
pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn=_Pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn_Object((1,3,6,1,4,1,20044,70,4,3,192,1,3),_Pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn_Type())
pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus(_A)
_Pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn_Type=EkiOnOff
_Pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn_Object=MibTableColumn
pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn=_Pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn_Object((1,3,6,1,4,1,20044,70,4,3,192,1,4),_Pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn_Type())
pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus(_A)
_Pmo6006CntlocalLineFecCorrectedErrorsCounterTable_Object=MibTable
pmo6006CntlocalLineFecCorrectedErrorsCounterTable=_Pmo6006CntlocalLineFecCorrectedErrorsCounterTable_Object((1,3,6,1,4,1,20044,70,4,3,200))
if mibBuilder.loadTexts:pmo6006CntlocalLineFecCorrectedErrorsCounterTable.setStatus(_A)
_Pmo6006CntlocalLineFecCorrectedErrorsCounterEntry_Object=MibTableRow
pmo6006CntlocalLineFecCorrectedErrorsCounterEntry=_Pmo6006CntlocalLineFecCorrectedErrorsCounterEntry_Object((1,3,6,1,4,1,20044,70,4,3,200,1))
pmo6006CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pmo6006CntlocalLineFecCorrectedErrorsCounterEntry.setStatus(_A)
class _Pmo6006CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__=_D
_Pmo6006CntlocalLineFecCorrectedErrorsCounterIndex_Object=MibTableColumn
pmo6006CntlocalLineFecCorrectedErrorsCounterIndex=_Pmo6006CntlocalLineFecCorrectedErrorsCounterIndex_Object((1,3,6,1,4,1,20044,70,4,3,200,1,1),_Pmo6006CntlocalLineFecCorrectedErrorsCounterIndex_Type())
pmo6006CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineFecCorrectedErrorsCounterIndex.setStatus(_A)
_Pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn_Type=Counter32
_Pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn_Object=MibTableColumn
pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn=_Pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn_Object((1,3,6,1,4,1,20044,70,4,3,200,1,2),_Pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn_Type())
pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus(_A)
_Pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type=EkiOnOff
_Pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object=MibTableColumn
pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn=_Pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object((1,3,6,1,4,1,20044,70,4,3,200,1,3),_Pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type())
pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus(_A)
_Pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type=EkiOnOff
_Pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object=MibTableColumn
pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn=_Pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object((1,3,6,1,4,1,20044,70,4,3,200,1,4),_Pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type())
pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus(_A)
_Pmo6006CntremoteLineSmBip8ErrorCounterTable_Object=MibTable
pmo6006CntremoteLineSmBip8ErrorCounterTable=_Pmo6006CntremoteLineSmBip8ErrorCounterTable_Object((1,3,6,1,4,1,20044,70,4,3,208))
if mibBuilder.loadTexts:pmo6006CntremoteLineSmBip8ErrorCounterTable.setStatus(_A)
_Pmo6006CntremoteLineSmBip8ErrorCounterEntry_Object=MibTableRow
pmo6006CntremoteLineSmBip8ErrorCounterEntry=_Pmo6006CntremoteLineSmBip8ErrorCounterEntry_Object((1,3,6,1,4,1,20044,70,4,3,208,1))
pmo6006CntremoteLineSmBip8ErrorCounterEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pmo6006CntremoteLineSmBip8ErrorCounterEntry.setStatus(_A)
class _Pmo6006CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CntremoteLineSmBip8ErrorCounterIndex_Type.__name__=_D
_Pmo6006CntremoteLineSmBip8ErrorCounterIndex_Object=MibTableColumn
pmo6006CntremoteLineSmBip8ErrorCounterIndex=_Pmo6006CntremoteLineSmBip8ErrorCounterIndex_Object((1,3,6,1,4,1,20044,70,4,3,208,1,1),_Pmo6006CntremoteLineSmBip8ErrorCounterIndex_Type())
pmo6006CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntremoteLineSmBip8ErrorCounterIndex.setStatus(_A)
_Pmo6006CntremoteLineSmBip8ErrorCounterValuePortn_Type=Counter32
_Pmo6006CntremoteLineSmBip8ErrorCounterValuePortn_Object=MibTableColumn
pmo6006CntremoteLineSmBip8ErrorCounterValuePortn=_Pmo6006CntremoteLineSmBip8ErrorCounterValuePortn_Object((1,3,6,1,4,1,20044,70,4,3,208,1,2),_Pmo6006CntremoteLineSmBip8ErrorCounterValuePortn_Type())
pmo6006CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntremoteLineSmBip8ErrorCounterValuePortn.setStatus(_A)
_Pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn_Type=EkiOnOff
_Pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn_Object=MibTableColumn
pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn=_Pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn_Object((1,3,6,1,4,1,20044,70,4,3,208,1,3),_Pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn_Type())
pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus(_A)
_Pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn_Type=EkiOnOff
_Pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn_Object=MibTableColumn
pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn=_Pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn_Object((1,3,6,1,4,1,20044,70,4,3,208,1,4),_Pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn_Type())
pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus(_A)
_Pmo6006CntlineDfrmTimCntTable_Object=MibTable
pmo6006CntlineDfrmTimCntTable=_Pmo6006CntlineDfrmTimCntTable_Object((1,3,6,1,4,1,20044,70,4,3,216))
if mibBuilder.loadTexts:pmo6006CntlineDfrmTimCntTable.setStatus(_A)
_Pmo6006CntlineDfrmTimCntEntry_Object=MibTableRow
pmo6006CntlineDfrmTimCntEntry=_Pmo6006CntlineDfrmTimCntEntry_Object((1,3,6,1,4,1,20044,70,4,3,216,1))
pmo6006CntlineDfrmTimCntEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pmo6006CntlineDfrmTimCntEntry.setStatus(_A)
class _Pmo6006CntlineDfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CntlineDfrmTimCntIndex_Type.__name__=_D
_Pmo6006CntlineDfrmTimCntIndex_Object=MibTableColumn
pmo6006CntlineDfrmTimCntIndex=_Pmo6006CntlineDfrmTimCntIndex_Object((1,3,6,1,4,1,20044,70,4,3,216,1,1),_Pmo6006CntlineDfrmTimCntIndex_Type())
pmo6006CntlineDfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlineDfrmTimCntIndex.setStatus(_A)
_Pmo6006CntlineDfrmTimCntValuePortn_Type=Counter32
_Pmo6006CntlineDfrmTimCntValuePortn_Object=MibTableColumn
pmo6006CntlineDfrmTimCntValuePortn=_Pmo6006CntlineDfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,70,4,3,216,1,2),_Pmo6006CntlineDfrmTimCntValuePortn_Type())
pmo6006CntlineDfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlineDfrmTimCntValuePortn.setStatus(_A)
_Pmo6006CntlineDfrmTimCntErrorPortn_Type=EkiOnOff
_Pmo6006CntlineDfrmTimCntErrorPortn_Object=MibTableColumn
pmo6006CntlineDfrmTimCntErrorPortn=_Pmo6006CntlineDfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,70,4,3,216,1,3),_Pmo6006CntlineDfrmTimCntErrorPortn_Type())
pmo6006CntlineDfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlineDfrmTimCntErrorPortn.setStatus(_A)
_Pmo6006CntlineDfrmTimCntOverloadPortn_Type=EkiOnOff
_Pmo6006CntlineDfrmTimCntOverloadPortn_Object=MibTableColumn
pmo6006CntlineDfrmTimCntOverloadPortn=_Pmo6006CntlineDfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,70,4,3,216,1,4),_Pmo6006CntlineDfrmTimCntOverloadPortn_Type())
pmo6006CntlineDfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CntlineDfrmTimCntOverloadPortn.setStatus(_A)
_Pmo6006CntCountersReset_Type=EkiOnOff
_Pmo6006CntCountersReset_Object=MibScalar
pmo6006CntCountersReset=_Pmo6006CntCountersReset_Object((1,3,6,1,4,1,20044,70,4,259),_Pmo6006CntCountersReset_Type())
pmo6006CntCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CntCountersReset.setStatus(_A)
_Pmo6006CntCountersStop_Type=EkiOnOff
_Pmo6006CntCountersStop_Object=MibScalar
pmo6006CntCountersStop=_Pmo6006CntCountersStop_Object((1,3,6,1,4,1,20044,70,4,260),_Pmo6006CntCountersStop_Type())
pmo6006CntCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CntCountersStop.setStatus(_A)
_Pmo6006controlsWrite_ObjectIdentity=ObjectIdentity
pmo6006controlsWrite=_Pmo6006controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,70,6))
_Pmo6006CtrlOther_ObjectIdentity=ObjectIdentity
pmo6006CtrlOther=_Pmo6006CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,70,6,1))
_Pmo6006CtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pmo6006CtrlconfMgnt1=_Pmo6006CtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,70,6,1,1))
_Pmo6006CtrlConf1Load1_Type=EkiOnOff
_Pmo6006CtrlConf1Load1_Object=MibScalar
pmo6006CtrlConf1Load1=_Pmo6006CtrlConf1Load1_Object((1,3,6,1,4,1,20044,70,6,1,1,1),_Pmo6006CtrlConf1Load1_Type())
pmo6006CtrlConf1Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlConf1Load1.setStatus(_A)
_Pmo6006CtrlConf2Load1_Type=EkiOnOff
_Pmo6006CtrlConf2Load1_Object=MibScalar
pmo6006CtrlConf2Load1=_Pmo6006CtrlConf2Load1_Object((1,3,6,1,4,1,20044,70,6,1,1,2),_Pmo6006CtrlConf2Load1_Type())
pmo6006CtrlConf2Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlConf2Load1.setStatus(_A)
_Pmo6006CtrlConf2Flash1_Type=EkiOnOff
_Pmo6006CtrlConf2Flash1_Object=MibScalar
pmo6006CtrlConf2Flash1=_Pmo6006CtrlConf2Flash1_Object((1,3,6,1,4,1,20044,70,6,1,1,10),_Pmo6006CtrlConf2Flash1_Type())
pmo6006CtrlConf2Flash1.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlConf2Flash1.setStatus(_A)
_Pmo6006CtrlConf2Clear1_Type=EkiOnOff
_Pmo6006CtrlConf2Clear1_Object=MibScalar
pmo6006CtrlConf2Clear1=_Pmo6006CtrlConf2Clear1_Object((1,3,6,1,4,1,20044,70,6,1,1,14),_Pmo6006CtrlConf2Clear1_Type())
pmo6006CtrlConf2Clear1.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlConf2Clear1.setStatus(_A)
_Pmo6006Ctrlsynth4_ObjectIdentity=ObjectIdentity
pmo6006Ctrlsynth4=_Pmo6006Ctrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,70,6,1,4))
_Pmo6006CtrlCorrelatOn_Type=EkiOnOff
_Pmo6006CtrlCorrelatOn_Object=MibScalar
pmo6006CtrlCorrelatOn=_Pmo6006CtrlCorrelatOn_Object((1,3,6,1,4,1,20044,70,6,1,4,1),_Pmo6006CtrlCorrelatOn_Type())
pmo6006CtrlCorrelatOn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlCorrelatOn.setStatus(_A)
_Pmo6006CtrlCorrelatOff_Type=EkiOnOff
_Pmo6006CtrlCorrelatOff_Object=MibScalar
pmo6006CtrlCorrelatOff=_Pmo6006CtrlCorrelatOff_Object((1,3,6,1,4,1,20044,70,6,1,4,2),_Pmo6006CtrlCorrelatOff_Type())
pmo6006CtrlCorrelatOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlCorrelatOff.setStatus(_A)
_Pmo6006CtrlswMgnt_ObjectIdentity=ObjectIdentity
pmo6006CtrlswMgnt=_Pmo6006CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,70,6,1,5))
_Pmo6006CtrlColdReset_Type=EkiOnOff
_Pmo6006CtrlColdReset_Object=MibScalar
pmo6006CtrlColdReset=_Pmo6006CtrlColdReset_Object((1,3,6,1,4,1,20044,70,6,1,5,2),_Pmo6006CtrlColdReset_Type())
pmo6006CtrlColdReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlColdReset.setStatus(_A)
_Pmo6006CtrlWarmReset_Type=EkiOnOff
_Pmo6006CtrlWarmReset_Object=MibScalar
pmo6006CtrlWarmReset=_Pmo6006CtrlWarmReset_Object((1,3,6,1,4,1,20044,70,6,1,5,3),_Pmo6006CtrlWarmReset_Type())
pmo6006CtrlWarmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlWarmReset.setStatus(_A)
_Pmo6006CtrlLoadSwBank1_Type=EkiOnOff
_Pmo6006CtrlLoadSwBank1_Object=MibScalar
pmo6006CtrlLoadSwBank1=_Pmo6006CtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,70,6,1,5,5),_Pmo6006CtrlLoadSwBank1_Type())
pmo6006CtrlLoadSwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLoadSwBank1.setStatus(_A)
_Pmo6006CtrlLoadSwBank2_Type=EkiOnOff
_Pmo6006CtrlLoadSwBank2_Object=MibScalar
pmo6006CtrlLoadSwBank2=_Pmo6006CtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,70,6,1,5,6),_Pmo6006CtrlLoadSwBank2_Type())
pmo6006CtrlLoadSwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLoadSwBank2.setStatus(_A)
_Pmo6006CtrlgwMgnt_ObjectIdentity=ObjectIdentity
pmo6006CtrlgwMgnt=_Pmo6006CtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,70,6,1,6))
_Pmo6006CtrlCurrentGwReset_Type=EkiOnOff
_Pmo6006CtrlCurrentGwReset_Object=MibScalar
pmo6006CtrlCurrentGwReset=_Pmo6006CtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,70,6,1,6,1),_Pmo6006CtrlCurrentGwReset_Type())
pmo6006CtrlCurrentGwReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlCurrentGwReset.setStatus(_A)
_Pmo6006CtrlLoadGwBank1_Type=EkiOnOff
_Pmo6006CtrlLoadGwBank1_Object=MibScalar
pmo6006CtrlLoadGwBank1=_Pmo6006CtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,70,6,1,6,5),_Pmo6006CtrlLoadGwBank1_Type())
pmo6006CtrlLoadGwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLoadGwBank1.setStatus(_A)
_Pmo6006CtrlLoadGwBank2_Type=EkiOnOff
_Pmo6006CtrlLoadGwBank2_Object=MibScalar
pmo6006CtrlLoadGwBank2=_Pmo6006CtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,70,6,1,6,6),_Pmo6006CtrlLoadGwBank2_Type())
pmo6006CtrlLoadGwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLoadGwBank2.setStatus(_A)
_Pmo6006CtrlLoadGwBank3_Type=EkiOnOff
_Pmo6006CtrlLoadGwBank3_Object=MibScalar
pmo6006CtrlLoadGwBank3=_Pmo6006CtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,70,6,1,6,7),_Pmo6006CtrlLoadGwBank3_Type())
pmo6006CtrlLoadGwBank3.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLoadGwBank3.setStatus(_A)
_Pmo6006CtrlLoadGwBank4_Type=EkiOnOff
_Pmo6006CtrlLoadGwBank4_Object=MibScalar
pmo6006CtrlLoadGwBank4=_Pmo6006CtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,70,6,1,6,8),_Pmo6006CtrlLoadGwBank4_Type())
pmo6006CtrlLoadGwBank4.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLoadGwBank4.setStatus(_A)
_Pmo6006CtrlledTest_ObjectIdentity=ObjectIdentity
pmo6006CtrlledTest=_Pmo6006CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,70,6,1,192))
_Pmo6006CtrlGreenLed_Type=EkiOnOff
_Pmo6006CtrlGreenLed_Object=MibScalar
pmo6006CtrlGreenLed=_Pmo6006CtrlGreenLed_Object((1,3,6,1,4,1,20044,70,6,1,192,1),_Pmo6006CtrlGreenLed_Type())
pmo6006CtrlGreenLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlGreenLed.setStatus(_A)
_Pmo6006CtrlRedLed_Type=EkiOnOff
_Pmo6006CtrlRedLed_Object=MibScalar
pmo6006CtrlRedLed=_Pmo6006CtrlRedLed_Object((1,3,6,1,4,1,20044,70,6,1,192,2),_Pmo6006CtrlRedLed_Type())
pmo6006CtrlRedLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlRedLed.setStatus(_A)
_Pmo6006CtrlLedOff_Type=EkiOnOff
_Pmo6006CtrlLedOff_Object=MibScalar
pmo6006CtrlLedOff=_Pmo6006CtrlLedOff_Object((1,3,6,1,4,1,20044,70,6,1,192,3),_Pmo6006CtrlLedOff_Type())
pmo6006CtrlLedOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlLedOff.setStatus(_A)
_Pmo6006CtrlClient_ObjectIdentity=ObjectIdentity
pmo6006CtrlClient=_Pmo6006CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,70,6,2))
_Pmo6006CtrlaccessLoopTable_Object=MibTable
pmo6006CtrlaccessLoopTable=_Pmo6006CtrlaccessLoopTable_Object((1,3,6,1,4,1,20044,70,6,2,16))
if mibBuilder.loadTexts:pmo6006CtrlaccessLoopTable.setStatus(_A)
_Pmo6006CtrlaccessLoopEntry_Object=MibTableRow
pmo6006CtrlaccessLoopEntry=_Pmo6006CtrlaccessLoopEntry_Object((1,3,6,1,4,1,20044,70,6,2,16,1))
pmo6006CtrlaccessLoopEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pmo6006CtrlaccessLoopEntry.setStatus(_A)
class _Pmo6006CtrlaccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlaccessLoopIndex_Type.__name__=_D
_Pmo6006CtrlaccessLoopIndex_Object=MibTableColumn
pmo6006CtrlaccessLoopIndex=_Pmo6006CtrlaccessLoopIndex_Object((1,3,6,1,4,1,20044,70,6,2,16,1,1),_Pmo6006CtrlaccessLoopIndex_Type())
pmo6006CtrlaccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlaccessLoopIndex.setStatus(_A)
_Pmo6006CtrlaccessLoopPortn_Type=EkiState
_Pmo6006CtrlaccessLoopPortn_Object=MibTableColumn
pmo6006CtrlaccessLoopPortn=_Pmo6006CtrlaccessLoopPortn_Object((1,3,6,1,4,1,20044,70,6,2,16,1,2),_Pmo6006CtrlaccessLoopPortn_Type())
pmo6006CtrlaccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlaccessLoopPortn.setStatus(_A)
_Pmo6006CtrlclientLoopToLineTable_Object=MibTable
pmo6006CtrlclientLoopToLineTable=_Pmo6006CtrlclientLoopToLineTable_Object((1,3,6,1,4,1,20044,70,6,2,17))
if mibBuilder.loadTexts:pmo6006CtrlclientLoopToLineTable.setStatus(_A)
_Pmo6006CtrlclientLoopToLineEntry_Object=MibTableRow
pmo6006CtrlclientLoopToLineEntry=_Pmo6006CtrlclientLoopToLineEntry_Object((1,3,6,1,4,1,20044,70,6,2,17,1))
pmo6006CtrlclientLoopToLineEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pmo6006CtrlclientLoopToLineEntry.setStatus(_A)
class _Pmo6006CtrlclientLoopToLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlclientLoopToLineIndex_Type.__name__=_D
_Pmo6006CtrlclientLoopToLineIndex_Object=MibTableColumn
pmo6006CtrlclientLoopToLineIndex=_Pmo6006CtrlclientLoopToLineIndex_Object((1,3,6,1,4,1,20044,70,6,2,17,1,1),_Pmo6006CtrlclientLoopToLineIndex_Type())
pmo6006CtrlclientLoopToLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlclientLoopToLineIndex.setStatus(_A)
_Pmo6006CtrlclientLoopToLinePortn_Type=EkiState
_Pmo6006CtrlclientLoopToLinePortn_Object=MibTableColumn
pmo6006CtrlclientLoopToLinePortn=_Pmo6006CtrlclientLoopToLinePortn_Object((1,3,6,1,4,1,20044,70,6,2,17,1,2),_Pmo6006CtrlclientLoopToLinePortn_Type())
pmo6006CtrlclientLoopToLinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlclientLoopToLinePortn.setStatus(_A)
_Pmo6006CtrlcsfUpInsTable_Object=MibTable
pmo6006CtrlcsfUpInsTable=_Pmo6006CtrlcsfUpInsTable_Object((1,3,6,1,4,1,20044,70,6,2,21))
if mibBuilder.loadTexts:pmo6006CtrlcsfUpInsTable.setStatus(_A)
_Pmo6006CtrlcsfUpInsEntry_Object=MibTableRow
pmo6006CtrlcsfUpInsEntry=_Pmo6006CtrlcsfUpInsEntry_Object((1,3,6,1,4,1,20044,70,6,2,21,1))
pmo6006CtrlcsfUpInsEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pmo6006CtrlcsfUpInsEntry.setStatus(_A)
class _Pmo6006CtrlcsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlcsfUpInsIndex_Type.__name__=_D
_Pmo6006CtrlcsfUpInsIndex_Object=MibTableColumn
pmo6006CtrlcsfUpInsIndex=_Pmo6006CtrlcsfUpInsIndex_Object((1,3,6,1,4,1,20044,70,6,2,21,1,1),_Pmo6006CtrlcsfUpInsIndex_Type())
pmo6006CtrlcsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlcsfUpInsIndex.setStatus(_A)
_Pmo6006CtrlcsfUpInsPortn_Type=EkiState
_Pmo6006CtrlcsfUpInsPortn_Object=MibTableColumn
pmo6006CtrlcsfUpInsPortn=_Pmo6006CtrlcsfUpInsPortn_Object((1,3,6,1,4,1,20044,70,6,2,21,1,2),_Pmo6006CtrlcsfUpInsPortn_Type())
pmo6006CtrlcsfUpInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlcsfUpInsPortn.setStatus(_A)
_Pmo6006CtrlcaisDwInsTable_Object=MibTable
pmo6006CtrlcaisDwInsTable=_Pmo6006CtrlcaisDwInsTable_Object((1,3,6,1,4,1,20044,70,6,2,22))
if mibBuilder.loadTexts:pmo6006CtrlcaisDwInsTable.setStatus(_A)
_Pmo6006CtrlcaisDwInsEntry_Object=MibTableRow
pmo6006CtrlcaisDwInsEntry=_Pmo6006CtrlcaisDwInsEntry_Object((1,3,6,1,4,1,20044,70,6,2,22,1))
pmo6006CtrlcaisDwInsEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pmo6006CtrlcaisDwInsEntry.setStatus(_A)
class _Pmo6006CtrlcaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlcaisDwInsIndex_Type.__name__=_D
_Pmo6006CtrlcaisDwInsIndex_Object=MibTableColumn
pmo6006CtrlcaisDwInsIndex=_Pmo6006CtrlcaisDwInsIndex_Object((1,3,6,1,4,1,20044,70,6,2,22,1,1),_Pmo6006CtrlcaisDwInsIndex_Type())
pmo6006CtrlcaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlcaisDwInsIndex.setStatus(_A)
_Pmo6006CtrlcaisDwInsPortn_Type=EkiState
_Pmo6006CtrlcaisDwInsPortn_Object=MibTableColumn
pmo6006CtrlcaisDwInsPortn=_Pmo6006CtrlcaisDwInsPortn_Object((1,3,6,1,4,1,20044,70,6,2,22,1,2),_Pmo6006CtrlcaisDwInsPortn_Type())
pmo6006CtrlcaisDwInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlcaisDwInsPortn.setStatus(_A)
_Pmo6006CtrlclientOciTable_Object=MibTable
pmo6006CtrlclientOciTable=_Pmo6006CtrlclientOciTable_Object((1,3,6,1,4,1,20044,70,6,2,23))
if mibBuilder.loadTexts:pmo6006CtrlclientOciTable.setStatus(_A)
_Pmo6006CtrlclientOciEntry_Object=MibTableRow
pmo6006CtrlclientOciEntry=_Pmo6006CtrlclientOciEntry_Object((1,3,6,1,4,1,20044,70,6,2,23,1))
pmo6006CtrlclientOciEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pmo6006CtrlclientOciEntry.setStatus(_A)
class _Pmo6006CtrlclientOciIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlclientOciIndex_Type.__name__=_D
_Pmo6006CtrlclientOciIndex_Object=MibTableColumn
pmo6006CtrlclientOciIndex=_Pmo6006CtrlclientOciIndex_Object((1,3,6,1,4,1,20044,70,6,2,23,1,1),_Pmo6006CtrlclientOciIndex_Type())
pmo6006CtrlclientOciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlclientOciIndex.setStatus(_A)
_Pmo6006CtrlclientOciPortn_Type=EkiState
_Pmo6006CtrlclientOciPortn_Object=MibTableColumn
pmo6006CtrlclientOciPortn=_Pmo6006CtrlclientOciPortn_Object((1,3,6,1,4,1,20044,70,6,2,23,1,2),_Pmo6006CtrlclientOciPortn_Type())
pmo6006CtrlclientOciPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlclientOciPortn.setStatus(_A)
_Pmo6006CtrlclientLckTable_Object=MibTable
pmo6006CtrlclientLckTable=_Pmo6006CtrlclientLckTable_Object((1,3,6,1,4,1,20044,70,6,2,24))
if mibBuilder.loadTexts:pmo6006CtrlclientLckTable.setStatus(_A)
_Pmo6006CtrlclientLckEntry_Object=MibTableRow
pmo6006CtrlclientLckEntry=_Pmo6006CtrlclientLckEntry_Object((1,3,6,1,4,1,20044,70,6,2,24,1))
pmo6006CtrlclientLckEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pmo6006CtrlclientLckEntry.setStatus(_A)
class _Pmo6006CtrlclientLckIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlclientLckIndex_Type.__name__=_D
_Pmo6006CtrlclientLckIndex_Object=MibTableColumn
pmo6006CtrlclientLckIndex=_Pmo6006CtrlclientLckIndex_Object((1,3,6,1,4,1,20044,70,6,2,24,1,1),_Pmo6006CtrlclientLckIndex_Type())
pmo6006CtrlclientLckIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlclientLckIndex.setStatus(_A)
_Pmo6006CtrlclientLckPortn_Type=EkiState
_Pmo6006CtrlclientLckPortn_Object=MibTableColumn
pmo6006CtrlclientLckPortn=_Pmo6006CtrlclientLckPortn_Object((1,3,6,1,4,1,20044,70,6,2,24,1,2),_Pmo6006CtrlclientLckPortn_Type())
pmo6006CtrlclientLckPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlclientLckPortn.setStatus(_A)
_Pmo6006CtrlclientAisTable_Object=MibTable
pmo6006CtrlclientAisTable=_Pmo6006CtrlclientAisTable_Object((1,3,6,1,4,1,20044,70,6,2,25))
if mibBuilder.loadTexts:pmo6006CtrlclientAisTable.setStatus(_A)
_Pmo6006CtrlclientAisEntry_Object=MibTableRow
pmo6006CtrlclientAisEntry=_Pmo6006CtrlclientAisEntry_Object((1,3,6,1,4,1,20044,70,6,2,25,1))
pmo6006CtrlclientAisEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pmo6006CtrlclientAisEntry.setStatus(_A)
class _Pmo6006CtrlclientAisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlclientAisIndex_Type.__name__=_D
_Pmo6006CtrlclientAisIndex_Object=MibTableColumn
pmo6006CtrlclientAisIndex=_Pmo6006CtrlclientAisIndex_Object((1,3,6,1,4,1,20044,70,6,2,25,1,1),_Pmo6006CtrlclientAisIndex_Type())
pmo6006CtrlclientAisIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlclientAisIndex.setStatus(_A)
_Pmo6006CtrlclientAisPortn_Type=EkiState
_Pmo6006CtrlclientAisPortn_Object=MibTableColumn
pmo6006CtrlclientAisPortn=_Pmo6006CtrlclientAisPortn_Object((1,3,6,1,4,1,20044,70,6,2,25,1,2),_Pmo6006CtrlclientAisPortn_Type())
pmo6006CtrlclientAisPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlclientAisPortn.setStatus(_A)
_Pmo6006CtrlclientBdiTable_Object=MibTable
pmo6006CtrlclientBdiTable=_Pmo6006CtrlclientBdiTable_Object((1,3,6,1,4,1,20044,70,6,2,26))
if mibBuilder.loadTexts:pmo6006CtrlclientBdiTable.setStatus(_A)
_Pmo6006CtrlclientBdiEntry_Object=MibTableRow
pmo6006CtrlclientBdiEntry=_Pmo6006CtrlclientBdiEntry_Object((1,3,6,1,4,1,20044,70,6,2,26,1))
pmo6006CtrlclientBdiEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pmo6006CtrlclientBdiEntry.setStatus(_A)
class _Pmo6006CtrlclientBdiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlclientBdiIndex_Type.__name__=_D
_Pmo6006CtrlclientBdiIndex_Object=MibTableColumn
pmo6006CtrlclientBdiIndex=_Pmo6006CtrlclientBdiIndex_Object((1,3,6,1,4,1,20044,70,6,2,26,1,1),_Pmo6006CtrlclientBdiIndex_Type())
pmo6006CtrlclientBdiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlclientBdiIndex.setStatus(_A)
_Pmo6006CtrlclientBdiPortn_Type=EkiState
_Pmo6006CtrlclientBdiPortn_Object=MibTableColumn
pmo6006CtrlclientBdiPortn=_Pmo6006CtrlclientBdiPortn_Object((1,3,6,1,4,1,20044,70,6,2,26,1,2),_Pmo6006CtrlclientBdiPortn_Type())
pmo6006CtrlclientBdiPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlclientBdiPortn.setStatus(_A)
_Pmo6006CtrlLine_ObjectIdentity=ObjectIdentity
pmo6006CtrlLine=_Pmo6006CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,70,6,3))
_Pmo6006CtrlcommAccessLoopTable_Object=MibTable
pmo6006CtrlcommAccessLoopTable=_Pmo6006CtrlcommAccessLoopTable_Object((1,3,6,1,4,1,20044,70,6,3,64))
if mibBuilder.loadTexts:pmo6006CtrlcommAccessLoopTable.setStatus(_A)
_Pmo6006CtrlcommAccessLoopEntry_Object=MibTableRow
pmo6006CtrlcommAccessLoopEntry=_Pmo6006CtrlcommAccessLoopEntry_Object((1,3,6,1,4,1,20044,70,6,3,64,1))
pmo6006CtrlcommAccessLoopEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pmo6006CtrlcommAccessLoopEntry.setStatus(_A)
class _Pmo6006CtrlcommAccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlcommAccessLoopIndex_Type.__name__=_D
_Pmo6006CtrlcommAccessLoopIndex_Object=MibTableColumn
pmo6006CtrlcommAccessLoopIndex=_Pmo6006CtrlcommAccessLoopIndex_Object((1,3,6,1,4,1,20044,70,6,3,64,1,1),_Pmo6006CtrlcommAccessLoopIndex_Type())
pmo6006CtrlcommAccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlcommAccessLoopIndex.setStatus(_A)
_Pmo6006CtrlcommAccessLoopPortn_Type=EkiState
_Pmo6006CtrlcommAccessLoopPortn_Object=MibTableColumn
pmo6006CtrlcommAccessLoopPortn=_Pmo6006CtrlcommAccessLoopPortn_Object((1,3,6,1,4,1,20044,70,6,3,64,1,2),_Pmo6006CtrlcommAccessLoopPortn_Type())
pmo6006CtrlcommAccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlcommAccessLoopPortn.setStatus(_A)
_Pmo6006CtrllineLoopTable_Object=MibTable
pmo6006CtrllineLoopTable=_Pmo6006CtrllineLoopTable_Object((1,3,6,1,4,1,20044,70,6,3,66))
if mibBuilder.loadTexts:pmo6006CtrllineLoopTable.setStatus(_A)
_Pmo6006CtrllineLoopEntry_Object=MibTableRow
pmo6006CtrllineLoopEntry=_Pmo6006CtrllineLoopEntry_Object((1,3,6,1,4,1,20044,70,6,3,66,1))
pmo6006CtrllineLoopEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pmo6006CtrllineLoopEntry.setStatus(_A)
class _Pmo6006CtrllineLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrllineLoopIndex_Type.__name__=_D
_Pmo6006CtrllineLoopIndex_Object=MibTableColumn
pmo6006CtrllineLoopIndex=_Pmo6006CtrllineLoopIndex_Object((1,3,6,1,4,1,20044,70,6,3,66,1,1),_Pmo6006CtrllineLoopIndex_Type())
pmo6006CtrllineLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrllineLoopIndex.setStatus(_A)
_Pmo6006CtrllineLoopPortn_Type=EkiState
_Pmo6006CtrllineLoopPortn_Object=MibTableColumn
pmo6006CtrllineLoopPortn=_Pmo6006CtrllineLoopPortn_Object((1,3,6,1,4,1,20044,70,6,3,66,1,2),_Pmo6006CtrllineLoopPortn_Type())
pmo6006CtrllineLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrllineLoopPortn.setStatus(_A)
_Pmo6006CtrlfecDisableTable_Object=MibTable
pmo6006CtrlfecDisableTable=_Pmo6006CtrlfecDisableTable_Object((1,3,6,1,4,1,20044,70,6,3,69))
if mibBuilder.loadTexts:pmo6006CtrlfecDisableTable.setStatus(_A)
_Pmo6006CtrlfecDisableEntry_Object=MibTableRow
pmo6006CtrlfecDisableEntry=_Pmo6006CtrlfecDisableEntry_Object((1,3,6,1,4,1,20044,70,6,3,69,1))
pmo6006CtrlfecDisableEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pmo6006CtrlfecDisableEntry.setStatus(_A)
class _Pmo6006CtrlfecDisableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrlfecDisableIndex_Type.__name__=_D
_Pmo6006CtrlfecDisableIndex_Object=MibTableColumn
pmo6006CtrlfecDisableIndex=_Pmo6006CtrlfecDisableIndex_Object((1,3,6,1,4,1,20044,70,6,3,69,1,1),_Pmo6006CtrlfecDisableIndex_Type())
pmo6006CtrlfecDisableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrlfecDisableIndex.setStatus(_A)
_Pmo6006CtrlfecDisablePortn_Type=EkiState
_Pmo6006CtrlfecDisablePortn_Object=MibTableColumn
pmo6006CtrlfecDisablePortn=_Pmo6006CtrlfecDisablePortn_Object((1,3,6,1,4,1,20044,70,6,3,69,1,2),_Pmo6006CtrlfecDisablePortn_Type())
pmo6006CtrlfecDisablePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrlfecDisablePortn.setStatus(_A)
_Pmo6006CtrllineBdiTable_Object=MibTable
pmo6006CtrllineBdiTable=_Pmo6006CtrllineBdiTable_Object((1,3,6,1,4,1,20044,70,6,3,70))
if mibBuilder.loadTexts:pmo6006CtrllineBdiTable.setStatus(_A)
_Pmo6006CtrllineBdiEntry_Object=MibTableRow
pmo6006CtrllineBdiEntry=_Pmo6006CtrllineBdiEntry_Object((1,3,6,1,4,1,20044,70,6,3,70,1))
pmo6006CtrllineBdiEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pmo6006CtrllineBdiEntry.setStatus(_A)
class _Pmo6006CtrllineBdiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CtrllineBdiIndex_Type.__name__=_D
_Pmo6006CtrllineBdiIndex_Object=MibTableColumn
pmo6006CtrllineBdiIndex=_Pmo6006CtrllineBdiIndex_Object((1,3,6,1,4,1,20044,70,6,3,70,1,1),_Pmo6006CtrllineBdiIndex_Type())
pmo6006CtrllineBdiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CtrllineBdiIndex.setStatus(_A)
_Pmo6006CtrllineBdiPortn_Type=EkiState
_Pmo6006CtrllineBdiPortn_Object=MibTableColumn
pmo6006CtrllineBdiPortn=_Pmo6006CtrllineBdiPortn_Object((1,3,6,1,4,1,20044,70,6,3,70,1,2),_Pmo6006CtrllineBdiPortn_Type())
pmo6006CtrllineBdiPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CtrllineBdiPortn.setStatus(_A)
_Pmo6006ri_ObjectIdentity=ObjectIdentity
pmo6006ri=_Pmo6006ri_ObjectIdentity((1,3,6,1,4,1,20044,70,7))
_Pmo6006riTable_ObjectIdentity=ObjectIdentity
pmo6006riTable=_Pmo6006riTable_ObjectIdentity((1,3,6,1,4,1,20044,70,7,1))
_Pmo6006RinvSfpTable_Object=MibTable
pmo6006RinvSfpTable=_Pmo6006RinvSfpTable_Object((1,3,6,1,4,1,20044,70,7,1,1))
if mibBuilder.loadTexts:pmo6006RinvSfpTable.setStatus(_A)
_Pmo6006RinvSfpEntry_Object=MibTableRow
pmo6006RinvSfpEntry=_Pmo6006RinvSfpEntry_Object((1,3,6,1,4,1,20044,70,7,1,1,1))
pmo6006RinvSfpEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pmo6006RinvSfpEntry.setStatus(_A)
class _Pmo6006RinvSfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pmo6006RinvSfpIndex_Type.__name__=_D
_Pmo6006RinvSfpIndex_Object=MibTableColumn
pmo6006RinvSfpIndex=_Pmo6006RinvSfpIndex_Object((1,3,6,1,4,1,20044,70,7,1,1,1,1),_Pmo6006RinvSfpIndex_Type())
pmo6006RinvSfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvSfpIndex.setStatus(_A)
_Pmo6006Rinvsfp_Type=DisplayString
_Pmo6006Rinvsfp_Object=MibTableColumn
pmo6006Rinvsfp=_Pmo6006Rinvsfp_Object((1,3,6,1,4,1,20044,70,7,1,1,1,2),_Pmo6006Rinvsfp_Type())
pmo6006Rinvsfp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006Rinvsfp.setStatus(_A)
_Pmo6006RinvLineTable_Object=MibTable
pmo6006RinvLineTable=_Pmo6006RinvLineTable_Object((1,3,6,1,4,1,20044,70,7,1,2))
if mibBuilder.loadTexts:pmo6006RinvLineTable.setStatus(_A)
_Pmo6006RinvLineEntry_Object=MibTableRow
pmo6006RinvLineEntry=_Pmo6006RinvLineEntry_Object((1,3,6,1,4,1,20044,70,7,1,2,1))
pmo6006RinvLineEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pmo6006RinvLineEntry.setStatus(_A)
class _Pmo6006RinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pmo6006RinvLineIndex_Type.__name__=_D
_Pmo6006RinvLineIndex_Object=MibTableColumn
pmo6006RinvLineIndex=_Pmo6006RinvLineIndex_Object((1,3,6,1,4,1,20044,70,7,1,2,1,1),_Pmo6006RinvLineIndex_Type())
pmo6006RinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvLineIndex.setStatus(_A)
_Pmo6006RinvxfpLine_Type=DisplayString
_Pmo6006RinvxfpLine_Object=MibTableColumn
pmo6006RinvxfpLine=_Pmo6006RinvxfpLine_Object((1,3,6,1,4,1,20044,70,7,1,2,1,2),_Pmo6006RinvxfpLine_Type())
pmo6006RinvxfpLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvxfpLine.setStatus(_A)
_Pmo6006RinvReloadInventory_Type=EkiOnOff
_Pmo6006RinvReloadInventory_Object=MibScalar
pmo6006RinvReloadInventory=_Pmo6006RinvReloadInventory_Object((1,3,6,1,4,1,20044,70,7,2),_Pmo6006RinvReloadInventory_Type())
pmo6006RinvReloadInventory.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006RinvReloadInventory.setStatus(_A)
_Pmo6006RinvHwPlatform_Type=DisplayString
_Pmo6006RinvHwPlatform_Object=MibScalar
pmo6006RinvHwPlatform=_Pmo6006RinvHwPlatform_Object((1,3,6,1,4,1,20044,70,7,3),_Pmo6006RinvHwPlatform_Type())
pmo6006RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvHwPlatform.setStatus(_A)
_Pmo6006RinvModulePlatform_Type=DisplayString
_Pmo6006RinvModulePlatform_Object=MibScalar
pmo6006RinvModulePlatform=_Pmo6006RinvModulePlatform_Object((1,3,6,1,4,1,20044,70,7,4),_Pmo6006RinvModulePlatform_Type())
pmo6006RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvModulePlatform.setStatus(_A)
_Pmo6006RinvSwPlatform_Type=DisplayString
_Pmo6006RinvSwPlatform_Object=MibScalar
pmo6006RinvSwPlatform=_Pmo6006RinvSwPlatform_Object((1,3,6,1,4,1,20044,70,7,5),_Pmo6006RinvSwPlatform_Type())
pmo6006RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvSwPlatform.setStatus(_A)
_Pmo6006RinvGwPlatform_Type=DisplayString
_Pmo6006RinvGwPlatform_Object=MibScalar
pmo6006RinvGwPlatform=_Pmo6006RinvGwPlatform_Object((1,3,6,1,4,1,20044,70,7,6),_Pmo6006RinvGwPlatform_Type())
pmo6006RinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006RinvGwPlatform.setStatus(_A)
_Pmo6006download_ObjectIdentity=ObjectIdentity
pmo6006download=_Pmo6006download_ObjectIdentity((1,3,6,1,4,1,20044,70,8))
_Pmo6006DwlOther_ObjectIdentity=ObjectIdentity
pmo6006DwlOther=_Pmo6006DwlOther_ObjectIdentity((1,3,6,1,4,1,20044,70,8,1))
_Pmo6006DwlrestartProcess_ObjectIdentity=ObjectIdentity
pmo6006DwlrestartProcess=_Pmo6006DwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,70,8,1,0))
_Pmo6006DwlWarmRestartProcessed_Type=EkiOnOff
_Pmo6006DwlWarmRestartProcessed_Object=MibScalar
pmo6006DwlWarmRestartProcessed=_Pmo6006DwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,70,8,1,0,1),_Pmo6006DwlWarmRestartProcessed_Type())
pmo6006DwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlWarmRestartProcessed.setStatus(_A)
_Pmo6006DwlColdRestartProcessed_Type=EkiOnOff
_Pmo6006DwlColdRestartProcessed_Object=MibScalar
pmo6006DwlColdRestartProcessed=_Pmo6006DwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,70,8,1,0,2),_Pmo6006DwlColdRestartProcessed_Type())
pmo6006DwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlColdRestartProcessed.setStatus(_A)
_Pmo6006DwlswBanksUsed_ObjectIdentity=ObjectIdentity
pmo6006DwlswBanksUsed=_Pmo6006DwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,70,8,1,1))
_Pmo6006DwlSwBank1Used_Type=EkiOnOff
_Pmo6006DwlSwBank1Used_Object=MibScalar
pmo6006DwlSwBank1Used=_Pmo6006DwlSwBank1Used_Object((1,3,6,1,4,1,20044,70,8,1,1,1),_Pmo6006DwlSwBank1Used_Type())
pmo6006DwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlSwBank1Used.setStatus(_A)
_Pmo6006DwlSwBank2Used_Type=EkiOnOff
_Pmo6006DwlSwBank2Used_Object=MibScalar
pmo6006DwlSwBank2Used=_Pmo6006DwlSwBank2Used_Object((1,3,6,1,4,1,20044,70,8,1,1,2),_Pmo6006DwlSwBank2Used_Type())
pmo6006DwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlSwBank2Used.setStatus(_A)
_Pmo6006DwlSwBank1Notempty_Type=EkiOnOff
_Pmo6006DwlSwBank1Notempty_Object=MibScalar
pmo6006DwlSwBank1Notempty=_Pmo6006DwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,70,8,1,1,5),_Pmo6006DwlSwBank1Notempty_Type())
pmo6006DwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlSwBank1Notempty.setStatus(_A)
_Pmo6006DwlSwBank2Notempty_Type=EkiOnOff
_Pmo6006DwlSwBank2Notempty_Object=MibScalar
pmo6006DwlSwBank2Notempty=_Pmo6006DwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,70,8,1,1,6),_Pmo6006DwlSwBank2Notempty_Type())
pmo6006DwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlSwBank2Notempty.setStatus(_A)
_Pmo6006DwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pmo6006DwlgwBanksUsed=_Pmo6006DwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,70,8,1,2))
_Pmo6006DwlGwBank1Used_Type=EkiOnOff
_Pmo6006DwlGwBank1Used_Object=MibScalar
pmo6006DwlGwBank1Used=_Pmo6006DwlGwBank1Used_Object((1,3,6,1,4,1,20044,70,8,1,2,1),_Pmo6006DwlGwBank1Used_Type())
pmo6006DwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank1Used.setStatus(_A)
_Pmo6006DwlGwBank2Used_Type=EkiOnOff
_Pmo6006DwlGwBank2Used_Object=MibScalar
pmo6006DwlGwBank2Used=_Pmo6006DwlGwBank2Used_Object((1,3,6,1,4,1,20044,70,8,1,2,2),_Pmo6006DwlGwBank2Used_Type())
pmo6006DwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank2Used.setStatus(_A)
_Pmo6006DwlGwBank3Used_Type=EkiOnOff
_Pmo6006DwlGwBank3Used_Object=MibScalar
pmo6006DwlGwBank3Used=_Pmo6006DwlGwBank3Used_Object((1,3,6,1,4,1,20044,70,8,1,2,3),_Pmo6006DwlGwBank3Used_Type())
pmo6006DwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank3Used.setStatus(_A)
_Pmo6006DwlGwBank4Used_Type=EkiOnOff
_Pmo6006DwlGwBank4Used_Object=MibScalar
pmo6006DwlGwBank4Used=_Pmo6006DwlGwBank4Used_Object((1,3,6,1,4,1,20044,70,8,1,2,4),_Pmo6006DwlGwBank4Used_Type())
pmo6006DwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank4Used.setStatus(_A)
_Pmo6006DwlGwBank1Notempty_Type=EkiOnOff
_Pmo6006DwlGwBank1Notempty_Object=MibScalar
pmo6006DwlGwBank1Notempty=_Pmo6006DwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,70,8,1,2,5),_Pmo6006DwlGwBank1Notempty_Type())
pmo6006DwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank1Notempty.setStatus(_A)
_Pmo6006DwlGwBank2Notempty_Type=EkiOnOff
_Pmo6006DwlGwBank2Notempty_Object=MibScalar
pmo6006DwlGwBank2Notempty=_Pmo6006DwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,70,8,1,2,6),_Pmo6006DwlGwBank2Notempty_Type())
pmo6006DwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank2Notempty.setStatus(_A)
_Pmo6006DwlGwBank3Notempty_Type=EkiOnOff
_Pmo6006DwlGwBank3Notempty_Object=MibScalar
pmo6006DwlGwBank3Notempty=_Pmo6006DwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,70,8,1,2,7),_Pmo6006DwlGwBank3Notempty_Type())
pmo6006DwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank3Notempty.setStatus(_A)
_Pmo6006DwlGwBank4Notempty_Type=EkiOnOff
_Pmo6006DwlGwBank4Notempty_Object=MibScalar
pmo6006DwlGwBank4Notempty=_Pmo6006DwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,70,8,1,2,8),_Pmo6006DwlGwBank4Notempty_Type())
pmo6006DwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006DwlGwBank4Notempty.setStatus(_A)
_Pmo6006DwlClient_ObjectIdentity=ObjectIdentity
pmo6006DwlClient=_Pmo6006DwlClient_ObjectIdentity((1,3,6,1,4,1,20044,70,8,2))
_Pmo6006DwlLine_ObjectIdentity=ObjectIdentity
pmo6006DwlLine=_Pmo6006DwlLine_ObjectIdentity((1,3,6,1,4,1,20044,70,8,3))
_Pmo6006Config_ObjectIdentity=ObjectIdentity
pmo6006Config=_Pmo6006Config_ObjectIdentity((1,3,6,1,4,1,20044,70,9))
_Pmo6006CfgStartup_ObjectIdentity=ObjectIdentity
pmo6006CfgStartup=_Pmo6006CfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,70,9,1))
_Pmo6006CfgClientStartupTable_Object=MibTable
pmo6006CfgClientStartupTable=_Pmo6006CfgClientStartupTable_Object((1,3,6,1,4,1,20044,70,9,1,1))
if mibBuilder.loadTexts:pmo6006CfgClientStartupTable.setStatus(_A)
_Pmo6006CfgClientStartupEntry_Object=MibTableRow
pmo6006CfgClientStartupEntry=_Pmo6006CfgClientStartupEntry_Object((1,3,6,1,4,1,20044,70,9,1,1,1))
pmo6006CfgClientStartupEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pmo6006CfgClientStartupEntry.setStatus(_A)
class _Pmo6006CfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientStartupIndex_Type.__name__=_D
_Pmo6006CfgClientStartupIndex_Object=MibTableColumn
pmo6006CfgClientStartupIndex=_Pmo6006CfgClientStartupIndex_Object((1,3,6,1,4,1,20044,70,9,1,1,1,1),_Pmo6006CfgClientStartupIndex_Type())
pmo6006CfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientStartupIndex.setStatus(_A)
class _Pmo6006CfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgSystConfPortPortn_Type.__name__=_F
_Pmo6006CfgSystConfPortPortn_Object=MibTableColumn
pmo6006CfgSystConfPortPortn=_Pmo6006CfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,70,9,1,1,1,3),_Pmo6006CfgSystConfPortPortn_Type())
pmo6006CfgSystConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgSystConfPortPortn.setStatus(_A)
class _Pmo6006CfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgNetConfPortPortn_Type.__name__=_F
_Pmo6006CfgNetConfPortPortn_Object=MibTableColumn
pmo6006CfgNetConfPortPortn=_Pmo6006CfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,70,9,1,1,1,4),_Pmo6006CfgNetConfPortPortn_Type())
pmo6006CfgNetConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgNetConfPortPortn.setStatus(_A)
class _Pmo6006CfgOptionsPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOptionsPortPortn_Type.__name__=_F
_Pmo6006CfgOptionsPortPortn_Object=MibTableColumn
pmo6006CfgOptionsPortPortn=_Pmo6006CfgOptionsPortPortn_Object((1,3,6,1,4,1,20044,70,9,1,1,1,14),_Pmo6006CfgOptionsPortPortn_Type())
pmo6006CfgOptionsPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOptionsPortPortn.setStatus(_A)
_Pmo6006CfgLinexr1StartupTable_Object=MibTable
pmo6006CfgLinexr1StartupTable=_Pmo6006CfgLinexr1StartupTable_Object((1,3,6,1,4,1,20044,70,9,1,2))
if mibBuilder.loadTexts:pmo6006CfgLinexr1StartupTable.setStatus(_A)
_Pmo6006CfgLinexr1StartupEntry_Object=MibTableRow
pmo6006CfgLinexr1StartupEntry=_Pmo6006CfgLinexr1StartupEntry_Object((1,3,6,1,4,1,20044,70,9,1,2,1))
pmo6006CfgLinexr1StartupEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pmo6006CfgLinexr1StartupEntry.setStatus(_A)
class _Pmo6006CfgLinexr1StartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLinexr1StartupIndex_Type.__name__=_D
_Pmo6006CfgLinexr1StartupIndex_Object=MibTableColumn
pmo6006CfgLinexr1StartupIndex=_Pmo6006CfgLinexr1StartupIndex_Object((1,3,6,1,4,1,20044,70,9,1,2,1,1),_Pmo6006CfgLinexr1StartupIndex_Type())
pmo6006CfgLinexr1StartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLinexr1StartupIndex.setStatus(_A)
class _Pmo6006CfgSystConfLinePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgSystConfLinePortn_Type.__name__=_F
_Pmo6006CfgSystConfLinePortn_Object=MibTableColumn
pmo6006CfgSystConfLinePortn=_Pmo6006CfgSystConfLinePortn_Object((1,3,6,1,4,1,20044,70,9,1,2,1,3),_Pmo6006CfgSystConfLinePortn_Type())
pmo6006CfgSystConfLinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgSystConfLinePortn.setStatus(_A)
class _Pmo6006CfgOptionsLinePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOptionsLinePortn_Type.__name__=_F
_Pmo6006CfgOptionsLinePortn_Object=MibTableColumn
pmo6006CfgOptionsLinePortn=_Pmo6006CfgOptionsLinePortn_Object((1,3,6,1,4,1,20044,70,9,1,2,1,14),_Pmo6006CfgOptionsLinePortn_Type())
pmo6006CfgOptionsLinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOptionsLinePortn.setStatus(_A)
_Pmo6006CfgOtxtlhTable_Object=MibTable
pmo6006CfgOtxtlhTable=_Pmo6006CfgOtxtlhTable_Object((1,3,6,1,4,1,20044,70,9,1,3))
if mibBuilder.loadTexts:pmo6006CfgOtxtlhTable.setStatus(_A)
_Pmo6006CfgOtxtlhEntry_Object=MibTableRow
pmo6006CfgOtxtlhEntry=_Pmo6006CfgOtxtlhEntry_Object((1,3,6,1,4,1,20044,70,9,1,3,1))
pmo6006CfgOtxtlhEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pmo6006CfgOtxtlhEntry.setStatus(_A)
class _Pmo6006CfgOtxtlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgOtxtlhIndex_Type.__name__=_D
_Pmo6006CfgOtxtlhIndex_Object=MibTableColumn
pmo6006CfgOtxtlhIndex=_Pmo6006CfgOtxtlhIndex_Object((1,3,6,1,4,1,20044,70,9,1,3,1,1),_Pmo6006CfgOtxtlhIndex_Type())
pmo6006CfgOtxtlhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgOtxtlhIndex.setStatus(_A)
class _Pmo6006CfgLineControlsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgLineControlsPortn_Type.__name__=_F
_Pmo6006CfgLineControlsPortn_Object=MibTableColumn
pmo6006CfgLineControlsPortn=_Pmo6006CfgLineControlsPortn_Object((1,3,6,1,4,1,20044,70,9,1,3,1,3),_Pmo6006CfgLineControlsPortn_Type())
pmo6006CfgLineControlsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineControlsPortn.setStatus(_K)
class _Pmo6006CfgLinePwrLaserPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgLinePwrLaserPortn_Type.__name__=_F
_Pmo6006CfgLinePwrLaserPortn_Object=MibTableColumn
pmo6006CfgLinePwrLaserPortn=_Pmo6006CfgLinePwrLaserPortn_Object((1,3,6,1,4,1,20044,70,9,1,3,1,6),_Pmo6006CfgLinePwrLaserPortn_Type())
pmo6006CfgLinePwrLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLinePwrLaserPortn.setStatus(_A)
class _Pmo6006CfgLineFCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgLineFCurrentPortn_Type.__name__=_F
_Pmo6006CfgLineFCurrentPortn_Object=MibTableColumn
pmo6006CfgLineFCurrentPortn=_Pmo6006CfgLineFCurrentPortn_Object((1,3,6,1,4,1,20044,70,9,1,3,1,7),_Pmo6006CfgLineFCurrentPortn_Type())
pmo6006CfgLineFCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineFCurrentPortn.setStatus(_A)
class _Pmo6006CfgLineGridCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgLineGridCurrentPortn_Type.__name__=_F
_Pmo6006CfgLineGridCurrentPortn_Object=MibTableColumn
pmo6006CfgLineGridCurrentPortn=_Pmo6006CfgLineGridCurrentPortn_Object((1,3,6,1,4,1,20044,70,9,1,3,1,8),_Pmo6006CfgLineGridCurrentPortn_Type())
pmo6006CfgLineGridCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineGridCurrentPortn.setStatus(_A)
class _Pmo6006CfgLineFoPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgLineFoPortn_Type.__name__=_F
_Pmo6006CfgLineFoPortn_Object=MibTableColumn
pmo6006CfgLineFoPortn=_Pmo6006CfgLineFoPortn_Object((1,3,6,1,4,1,20044,70,9,1,3,1,9),_Pmo6006CfgLineFoPortn_Type())
pmo6006CfgLineFoPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineFoPortn.setStatus(_A)
_Pmo6006CfgLabels_ObjectIdentity=ObjectIdentity
pmo6006CfgLabels=_Pmo6006CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,70,9,2))
_Pmo6006CfgLabelclientTable_Object=MibTable
pmo6006CfgLabelclientTable=_Pmo6006CfgLabelclientTable_Object((1,3,6,1,4,1,20044,70,9,2,1))
if mibBuilder.loadTexts:pmo6006CfgLabelclientTable.setStatus(_A)
_Pmo6006CfgLabelclientEntry_Object=MibTableRow
pmo6006CfgLabelclientEntry=_Pmo6006CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,70,9,2,1,1))
pmo6006CfgLabelclientEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pmo6006CfgLabelclientEntry.setStatus(_A)
class _Pmo6006CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLabelclientIndex_Type.__name__=_D
_Pmo6006CfgLabelclientIndex_Object=MibTableColumn
pmo6006CfgLabelclientIndex=_Pmo6006CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,70,9,2,1,1,1),_Pmo6006CfgLabelclientIndex_Type())
pmo6006CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLabelclientIndex.setStatus(_A)
class _Pmo6006CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLabelclientPortn_Type.__name__=_G
_Pmo6006CfgLabelclientPortn_Object=MibTableColumn
pmo6006CfgLabelclientPortn=_Pmo6006CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,70,9,2,1,1,3),_Pmo6006CfgLabelclientPortn_Type())
pmo6006CfgLabelclientPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLabelclientPortn.setStatus(_A)
_Pmo6006CfgLabellineTable_Object=MibTable
pmo6006CfgLabellineTable=_Pmo6006CfgLabellineTable_Object((1,3,6,1,4,1,20044,70,9,2,2))
if mibBuilder.loadTexts:pmo6006CfgLabellineTable.setStatus(_A)
_Pmo6006CfgLabellineEntry_Object=MibTableRow
pmo6006CfgLabellineEntry=_Pmo6006CfgLabellineEntry_Object((1,3,6,1,4,1,20044,70,9,2,2,1))
pmo6006CfgLabellineEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pmo6006CfgLabellineEntry.setStatus(_A)
class _Pmo6006CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLabellineIndex_Type.__name__=_D
_Pmo6006CfgLabellineIndex_Object=MibTableColumn
pmo6006CfgLabellineIndex=_Pmo6006CfgLabellineIndex_Object((1,3,6,1,4,1,20044,70,9,2,2,1,1),_Pmo6006CfgLabellineIndex_Type())
pmo6006CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLabellineIndex.setStatus(_A)
class _Pmo6006CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLabellinePortn_Type.__name__=_G
_Pmo6006CfgLabellinePortn_Object=MibTableColumn
pmo6006CfgLabellinePortn=_Pmo6006CfgLabellinePortn_Object((1,3,6,1,4,1,20044,70,9,2,2,1,3),_Pmo6006CfgLabellinePortn_Type())
pmo6006CfgLabellinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLabellinePortn.setStatus(_A)
_Pmo6006CfgOther_ObjectIdentity=ObjectIdentity
pmo6006CfgOther=_Pmo6006CfgOther_ObjectIdentity((1,3,6,1,4,1,20044,70,9,3))
_Pmo6006tablemoduleOther_ObjectIdentity=ObjectIdentity
pmo6006tablemoduleOther=_Pmo6006tablemoduleOther_ObjectIdentity((1,3,6,1,4,1,20044,70,9,3,1))
class _Pmo6006Cfgmode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006Cfgmode_Type.__name__=_F
_Pmo6006Cfgmode_Object=MibScalar
pmo6006Cfgmode=_Pmo6006Cfgmode_Object((1,3,6,1,4,1,20044,70,9,3,1,2),_Pmo6006Cfgmode_Type())
pmo6006Cfgmode.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006Cfgmode.setStatus(_A)
_Pmo6006CfgOdu2Clienta_ObjectIdentity=ObjectIdentity
pmo6006CfgOdu2Clienta=_Pmo6006CfgOdu2Clienta_ObjectIdentity((1,3,6,1,4,1,20044,70,9,4))
_Pmo6006CfgClientStartupOduTable_Object=MibTable
pmo6006CfgClientStartupOduTable=_Pmo6006CfgClientStartupOduTable_Object((1,3,6,1,4,1,20044,70,9,4,1))
if mibBuilder.loadTexts:pmo6006CfgClientStartupOduTable.setStatus(_A)
_Pmo6006CfgClientStartupOduEntry_Object=MibTableRow
pmo6006CfgClientStartupOduEntry=_Pmo6006CfgClientStartupOduEntry_Object((1,3,6,1,4,1,20044,70,9,4,1,1))
pmo6006CfgClientStartupOduEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pmo6006CfgClientStartupOduEntry.setStatus(_A)
class _Pmo6006CfgClientStartupOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientStartupOduIndex_Type.__name__=_D
_Pmo6006CfgClientStartupOduIndex_Object=MibTableColumn
pmo6006CfgClientStartupOduIndex=_Pmo6006CfgClientStartupOduIndex_Object((1,3,6,1,4,1,20044,70,9,4,1,1,1),_Pmo6006CfgClientStartupOduIndex_Type())
pmo6006CfgClientStartupOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientStartupOduIndex.setStatus(_A)
class _Pmo6006CfgOdu2ReserveLsbPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOdu2ReserveLsbPortn_Type.__name__=_F
_Pmo6006CfgOdu2ReserveLsbPortn_Object=MibTableColumn
pmo6006CfgOdu2ReserveLsbPortn=_Pmo6006CfgOdu2ReserveLsbPortn_Object((1,3,6,1,4,1,20044,70,9,4,1,1,3),_Pmo6006CfgOdu2ReserveLsbPortn_Type())
pmo6006CfgOdu2ReserveLsbPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOdu2ReserveLsbPortn.setStatus(_A)
class _Pmo6006CfgOdu2DegthresholdPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOdu2DegthresholdPortn_Type.__name__=_F
_Pmo6006CfgOdu2DegthresholdPortn_Object=MibTableColumn
pmo6006CfgOdu2DegthresholdPortn=_Pmo6006CfgOdu2DegthresholdPortn_Object((1,3,6,1,4,1,20044,70,9,4,1,1,4),_Pmo6006CfgOdu2DegthresholdPortn_Type())
pmo6006CfgOdu2DegthresholdPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOdu2DegthresholdPortn.setStatus(_A)
class _Pmo6006CfgOdu2DegmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOdu2DegmPortn_Type.__name__=_F
_Pmo6006CfgOdu2DegmPortn_Object=MibTableColumn
pmo6006CfgOdu2DegmPortn=_Pmo6006CfgOdu2DegmPortn_Object((1,3,6,1,4,1,20044,70,9,4,1,1,5),_Pmo6006CfgOdu2DegmPortn_Type())
pmo6006CfgOdu2DegmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOdu2DegmPortn.setStatus(_A)
class _Pmo6006CfgOdu2SettingsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOdu2SettingsPortn_Type.__name__=_F
_Pmo6006CfgOdu2SettingsPortn_Object=MibTableColumn
pmo6006CfgOdu2SettingsPortn=_Pmo6006CfgOdu2SettingsPortn_Object((1,3,6,1,4,1,20044,70,9,4,1,1,6),_Pmo6006CfgOdu2SettingsPortn_Type())
pmo6006CfgOdu2SettingsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOdu2SettingsPortn.setStatus(_A)
_Pmo6006CfgOtu2Line_ObjectIdentity=ObjectIdentity
pmo6006CfgOtu2Line=_Pmo6006CfgOtu2Line_ObjectIdentity((1,3,6,1,4,1,20044,70,9,5))
_Pmo6006CfgLinexStartupOtuTable_Object=MibTable
pmo6006CfgLinexStartupOtuTable=_Pmo6006CfgLinexStartupOtuTable_Object((1,3,6,1,4,1,20044,70,9,5,1))
if mibBuilder.loadTexts:pmo6006CfgLinexStartupOtuTable.setStatus(_A)
_Pmo6006CfgLinexStartupOtuEntry_Object=MibTableRow
pmo6006CfgLinexStartupOtuEntry=_Pmo6006CfgLinexStartupOtuEntry_Object((1,3,6,1,4,1,20044,70,9,5,1,1))
pmo6006CfgLinexStartupOtuEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pmo6006CfgLinexStartupOtuEntry.setStatus(_A)
class _Pmo6006CfgLinexStartupOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLinexStartupOtuIndex_Type.__name__=_D
_Pmo6006CfgLinexStartupOtuIndex_Object=MibTableColumn
pmo6006CfgLinexStartupOtuIndex=_Pmo6006CfgLinexStartupOtuIndex_Object((1,3,6,1,4,1,20044,70,9,5,1,1,1),_Pmo6006CfgLinexStartupOtuIndex_Type())
pmo6006CfgLinexStartupOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLinexStartupOtuIndex.setStatus(_A)
class _Pmo6006CfgOtu2ReserveMsbPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOtu2ReserveMsbPortn_Type.__name__=_F
_Pmo6006CfgOtu2ReserveMsbPortn_Object=MibTableColumn
pmo6006CfgOtu2ReserveMsbPortn=_Pmo6006CfgOtu2ReserveMsbPortn_Object((1,3,6,1,4,1,20044,70,9,5,1,1,3),_Pmo6006CfgOtu2ReserveMsbPortn_Type())
pmo6006CfgOtu2ReserveMsbPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOtu2ReserveMsbPortn.setStatus(_A)
class _Pmo6006CfgOtu2DegthresholdPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOtu2DegthresholdPortn_Type.__name__=_F
_Pmo6006CfgOtu2DegthresholdPortn_Object=MibTableColumn
pmo6006CfgOtu2DegthresholdPortn=_Pmo6006CfgOtu2DegthresholdPortn_Object((1,3,6,1,4,1,20044,70,9,5,1,1,4),_Pmo6006CfgOtu2DegthresholdPortn_Type())
pmo6006CfgOtu2DegthresholdPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOtu2DegthresholdPortn.setStatus(_A)
class _Pmo6006CfgOtu2DegmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOtu2DegmPortn_Type.__name__=_F
_Pmo6006CfgOtu2DegmPortn_Object=MibTableColumn
pmo6006CfgOtu2DegmPortn=_Pmo6006CfgOtu2DegmPortn_Object((1,3,6,1,4,1,20044,70,9,5,1,1,5),_Pmo6006CfgOtu2DegmPortn_Type())
pmo6006CfgOtu2DegmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOtu2DegmPortn.setStatus(_A)
class _Pmo6006CfgOtu2SettingsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgOtu2SettingsPortn_Type.__name__=_F
_Pmo6006CfgOtu2SettingsPortn_Object=MibTableColumn
pmo6006CfgOtu2SettingsPortn=_Pmo6006CfgOtu2SettingsPortn_Object((1,3,6,1,4,1,20044,70,9,5,1,1,6),_Pmo6006CfgOtu2SettingsPortn_Type())
pmo6006CfgOtu2SettingsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgOtu2SettingsPortn.setStatus(_A)
_Pmo6006CfgSapiTxClient_ObjectIdentity=ObjectIdentity
pmo6006CfgSapiTxClient=_Pmo6006CfgSapiTxClient_ObjectIdentity((1,3,6,1,4,1,20044,70,9,6))
_Pmo6006CfgClientSapiTxOduTable_Object=MibTable
pmo6006CfgClientSapiTxOduTable=_Pmo6006CfgClientSapiTxOduTable_Object((1,3,6,1,4,1,20044,70,9,6,1))
if mibBuilder.loadTexts:pmo6006CfgClientSapiTxOduTable.setStatus(_A)
_Pmo6006CfgClientSapiTxOduEntry_Object=MibTableRow
pmo6006CfgClientSapiTxOduEntry=_Pmo6006CfgClientSapiTxOduEntry_Object((1,3,6,1,4,1,20044,70,9,6,1,1))
pmo6006CfgClientSapiTxOduEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pmo6006CfgClientSapiTxOduEntry.setStatus(_A)
class _Pmo6006CfgClientSapiTxOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientSapiTxOduIndex_Type.__name__=_D
_Pmo6006CfgClientSapiTxOduIndex_Object=MibTableColumn
pmo6006CfgClientSapiTxOduIndex=_Pmo6006CfgClientSapiTxOduIndex_Object((1,3,6,1,4,1,20044,70,9,6,1,1,1),_Pmo6006CfgClientSapiTxOduIndex_Type())
pmo6006CfgClientSapiTxOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientSapiTxOduIndex.setStatus(_A)
class _Pmo6006CfgClientSapiTxSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgClientSapiTxSetupPortn_Type.__name__=_G
_Pmo6006CfgClientSapiTxSetupPortn_Object=MibTableColumn
pmo6006CfgClientSapiTxSetupPortn=_Pmo6006CfgClientSapiTxSetupPortn_Object((1,3,6,1,4,1,20044,70,9,6,1,1,3),_Pmo6006CfgClientSapiTxSetupPortn_Type())
pmo6006CfgClientSapiTxSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgClientSapiTxSetupPortn.setStatus(_A)
_Pmo6006CfgSapiExpClient_ObjectIdentity=ObjectIdentity
pmo6006CfgSapiExpClient=_Pmo6006CfgSapiExpClient_ObjectIdentity((1,3,6,1,4,1,20044,70,9,7))
_Pmo6006CfgClientSapiExpOduTable_Object=MibTable
pmo6006CfgClientSapiExpOduTable=_Pmo6006CfgClientSapiExpOduTable_Object((1,3,6,1,4,1,20044,70,9,7,1))
if mibBuilder.loadTexts:pmo6006CfgClientSapiExpOduTable.setStatus(_A)
_Pmo6006CfgClientSapiExpOduEntry_Object=MibTableRow
pmo6006CfgClientSapiExpOduEntry=_Pmo6006CfgClientSapiExpOduEntry_Object((1,3,6,1,4,1,20044,70,9,7,1,1))
pmo6006CfgClientSapiExpOduEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pmo6006CfgClientSapiExpOduEntry.setStatus(_A)
class _Pmo6006CfgClientSapiExpOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientSapiExpOduIndex_Type.__name__=_D
_Pmo6006CfgClientSapiExpOduIndex_Object=MibTableColumn
pmo6006CfgClientSapiExpOduIndex=_Pmo6006CfgClientSapiExpOduIndex_Object((1,3,6,1,4,1,20044,70,9,7,1,1,1),_Pmo6006CfgClientSapiExpOduIndex_Type())
pmo6006CfgClientSapiExpOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientSapiExpOduIndex.setStatus(_A)
class _Pmo6006CfgClientSapiExpSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgClientSapiExpSetupPortn_Type.__name__=_G
_Pmo6006CfgClientSapiExpSetupPortn_Object=MibTableColumn
pmo6006CfgClientSapiExpSetupPortn=_Pmo6006CfgClientSapiExpSetupPortn_Object((1,3,6,1,4,1,20044,70,9,7,1,1,3),_Pmo6006CfgClientSapiExpSetupPortn_Type())
pmo6006CfgClientSapiExpSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgClientSapiExpSetupPortn.setStatus(_A)
_Pmo6006CfgSapiAccClient_ObjectIdentity=ObjectIdentity
pmo6006CfgSapiAccClient=_Pmo6006CfgSapiAccClient_ObjectIdentity((1,3,6,1,4,1,20044,70,9,8))
_Pmo6006CfgClientSapiAccOduTable_Object=MibTable
pmo6006CfgClientSapiAccOduTable=_Pmo6006CfgClientSapiAccOduTable_Object((1,3,6,1,4,1,20044,70,9,8,1))
if mibBuilder.loadTexts:pmo6006CfgClientSapiAccOduTable.setStatus(_A)
_Pmo6006CfgClientSapiAccOduEntry_Object=MibTableRow
pmo6006CfgClientSapiAccOduEntry=_Pmo6006CfgClientSapiAccOduEntry_Object((1,3,6,1,4,1,20044,70,9,8,1,1))
pmo6006CfgClientSapiAccOduEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pmo6006CfgClientSapiAccOduEntry.setStatus(_A)
class _Pmo6006CfgClientSapiAccOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientSapiAccOduIndex_Type.__name__=_D
_Pmo6006CfgClientSapiAccOduIndex_Object=MibTableColumn
pmo6006CfgClientSapiAccOduIndex=_Pmo6006CfgClientSapiAccOduIndex_Object((1,3,6,1,4,1,20044,70,9,8,1,1,1),_Pmo6006CfgClientSapiAccOduIndex_Type())
pmo6006CfgClientSapiAccOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientSapiAccOduIndex.setStatus(_A)
class _Pmo6006CfgClientSapiAccSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgClientSapiAccSetupPortn_Type.__name__=_G
_Pmo6006CfgClientSapiAccSetupPortn_Object=MibTableColumn
pmo6006CfgClientSapiAccSetupPortn=_Pmo6006CfgClientSapiAccSetupPortn_Object((1,3,6,1,4,1,20044,70,9,8,1,1,3),_Pmo6006CfgClientSapiAccSetupPortn_Type())
pmo6006CfgClientSapiAccSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgClientSapiAccSetupPortn.setStatus(_K)
_Pmo6006CfgDapiTxClient_ObjectIdentity=ObjectIdentity
pmo6006CfgDapiTxClient=_Pmo6006CfgDapiTxClient_ObjectIdentity((1,3,6,1,4,1,20044,70,9,9))
_Pmo6006CfgClientDapiTxOduTable_Object=MibTable
pmo6006CfgClientDapiTxOduTable=_Pmo6006CfgClientDapiTxOduTable_Object((1,3,6,1,4,1,20044,70,9,9,1))
if mibBuilder.loadTexts:pmo6006CfgClientDapiTxOduTable.setStatus(_A)
_Pmo6006CfgClientDapiTxOduEntry_Object=MibTableRow
pmo6006CfgClientDapiTxOduEntry=_Pmo6006CfgClientDapiTxOduEntry_Object((1,3,6,1,4,1,20044,70,9,9,1,1))
pmo6006CfgClientDapiTxOduEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pmo6006CfgClientDapiTxOduEntry.setStatus(_A)
class _Pmo6006CfgClientDapiTxOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientDapiTxOduIndex_Type.__name__=_D
_Pmo6006CfgClientDapiTxOduIndex_Object=MibTableColumn
pmo6006CfgClientDapiTxOduIndex=_Pmo6006CfgClientDapiTxOduIndex_Object((1,3,6,1,4,1,20044,70,9,9,1,1,1),_Pmo6006CfgClientDapiTxOduIndex_Type())
pmo6006CfgClientDapiTxOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientDapiTxOduIndex.setStatus(_A)
class _Pmo6006CfgClientDapiTxSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgClientDapiTxSetupPortn_Type.__name__=_G
_Pmo6006CfgClientDapiTxSetupPortn_Object=MibTableColumn
pmo6006CfgClientDapiTxSetupPortn=_Pmo6006CfgClientDapiTxSetupPortn_Object((1,3,6,1,4,1,20044,70,9,9,1,1,3),_Pmo6006CfgClientDapiTxSetupPortn_Type())
pmo6006CfgClientDapiTxSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgClientDapiTxSetupPortn.setStatus(_A)
_Pmo6006CfgDapiExpClient_ObjectIdentity=ObjectIdentity
pmo6006CfgDapiExpClient=_Pmo6006CfgDapiExpClient_ObjectIdentity((1,3,6,1,4,1,20044,70,9,10))
_Pmo6006CfgClientDapiExpOduTable_Object=MibTable
pmo6006CfgClientDapiExpOduTable=_Pmo6006CfgClientDapiExpOduTable_Object((1,3,6,1,4,1,20044,70,9,10,1))
if mibBuilder.loadTexts:pmo6006CfgClientDapiExpOduTable.setStatus(_A)
_Pmo6006CfgClientDapiExpOduEntry_Object=MibTableRow
pmo6006CfgClientDapiExpOduEntry=_Pmo6006CfgClientDapiExpOduEntry_Object((1,3,6,1,4,1,20044,70,9,10,1,1))
pmo6006CfgClientDapiExpOduEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pmo6006CfgClientDapiExpOduEntry.setStatus(_A)
class _Pmo6006CfgClientDapiExpOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientDapiExpOduIndex_Type.__name__=_D
_Pmo6006CfgClientDapiExpOduIndex_Object=MibTableColumn
pmo6006CfgClientDapiExpOduIndex=_Pmo6006CfgClientDapiExpOduIndex_Object((1,3,6,1,4,1,20044,70,9,10,1,1,1),_Pmo6006CfgClientDapiExpOduIndex_Type())
pmo6006CfgClientDapiExpOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientDapiExpOduIndex.setStatus(_A)
class _Pmo6006CfgClientDapiExpSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgClientDapiExpSetupPortn_Type.__name__=_G
_Pmo6006CfgClientDapiExpSetupPortn_Object=MibTableColumn
pmo6006CfgClientDapiExpSetupPortn=_Pmo6006CfgClientDapiExpSetupPortn_Object((1,3,6,1,4,1,20044,70,9,10,1,1,3),_Pmo6006CfgClientDapiExpSetupPortn_Type())
pmo6006CfgClientDapiExpSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgClientDapiExpSetupPortn.setStatus(_A)
_Pmo6006CfgDapiAccClient_ObjectIdentity=ObjectIdentity
pmo6006CfgDapiAccClient=_Pmo6006CfgDapiAccClient_ObjectIdentity((1,3,6,1,4,1,20044,70,9,11))
_Pmo6006CfgClientDapiAccOduTable_Object=MibTable
pmo6006CfgClientDapiAccOduTable=_Pmo6006CfgClientDapiAccOduTable_Object((1,3,6,1,4,1,20044,70,9,11,1))
if mibBuilder.loadTexts:pmo6006CfgClientDapiAccOduTable.setStatus(_A)
_Pmo6006CfgClientDapiAccOduEntry_Object=MibTableRow
pmo6006CfgClientDapiAccOduEntry=_Pmo6006CfgClientDapiAccOduEntry_Object((1,3,6,1,4,1,20044,70,9,11,1,1))
pmo6006CfgClientDapiAccOduEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pmo6006CfgClientDapiAccOduEntry.setStatus(_A)
class _Pmo6006CfgClientDapiAccOduIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgClientDapiAccOduIndex_Type.__name__=_D
_Pmo6006CfgClientDapiAccOduIndex_Object=MibTableColumn
pmo6006CfgClientDapiAccOduIndex=_Pmo6006CfgClientDapiAccOduIndex_Object((1,3,6,1,4,1,20044,70,9,11,1,1,1),_Pmo6006CfgClientDapiAccOduIndex_Type())
pmo6006CfgClientDapiAccOduIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgClientDapiAccOduIndex.setStatus(_A)
class _Pmo6006CfgClientDapiAccSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgClientDapiAccSetupPortn_Type.__name__=_G
_Pmo6006CfgClientDapiAccSetupPortn_Object=MibTableColumn
pmo6006CfgClientDapiAccSetupPortn=_Pmo6006CfgClientDapiAccSetupPortn_Object((1,3,6,1,4,1,20044,70,9,11,1,1,3),_Pmo6006CfgClientDapiAccSetupPortn_Type())
pmo6006CfgClientDapiAccSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgClientDapiAccSetupPortn.setStatus(_K)
_Pmo6006CfgSapiTxLine_ObjectIdentity=ObjectIdentity
pmo6006CfgSapiTxLine=_Pmo6006CfgSapiTxLine_ObjectIdentity((1,3,6,1,4,1,20044,70,9,12))
_Pmo6006CfgLineSapiTxOtuTable_Object=MibTable
pmo6006CfgLineSapiTxOtuTable=_Pmo6006CfgLineSapiTxOtuTable_Object((1,3,6,1,4,1,20044,70,9,12,1))
if mibBuilder.loadTexts:pmo6006CfgLineSapiTxOtuTable.setStatus(_A)
_Pmo6006CfgLineSapiTxOtuEntry_Object=MibTableRow
pmo6006CfgLineSapiTxOtuEntry=_Pmo6006CfgLineSapiTxOtuEntry_Object((1,3,6,1,4,1,20044,70,9,12,1,1))
pmo6006CfgLineSapiTxOtuEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pmo6006CfgLineSapiTxOtuEntry.setStatus(_A)
class _Pmo6006CfgLineSapiTxOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLineSapiTxOtuIndex_Type.__name__=_D
_Pmo6006CfgLineSapiTxOtuIndex_Object=MibTableColumn
pmo6006CfgLineSapiTxOtuIndex=_Pmo6006CfgLineSapiTxOtuIndex_Object((1,3,6,1,4,1,20044,70,9,12,1,1,1),_Pmo6006CfgLineSapiTxOtuIndex_Type())
pmo6006CfgLineSapiTxOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLineSapiTxOtuIndex.setStatus(_A)
class _Pmo6006CfgLineSapiTxSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLineSapiTxSetupPortn_Type.__name__=_G
_Pmo6006CfgLineSapiTxSetupPortn_Object=MibTableColumn
pmo6006CfgLineSapiTxSetupPortn=_Pmo6006CfgLineSapiTxSetupPortn_Object((1,3,6,1,4,1,20044,70,9,12,1,1,3),_Pmo6006CfgLineSapiTxSetupPortn_Type())
pmo6006CfgLineSapiTxSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineSapiTxSetupPortn.setStatus(_A)
_Pmo6006CfgSapiExpLine_ObjectIdentity=ObjectIdentity
pmo6006CfgSapiExpLine=_Pmo6006CfgSapiExpLine_ObjectIdentity((1,3,6,1,4,1,20044,70,9,13))
_Pmo6006CfgLineSapiExpOtuTable_Object=MibTable
pmo6006CfgLineSapiExpOtuTable=_Pmo6006CfgLineSapiExpOtuTable_Object((1,3,6,1,4,1,20044,70,9,13,1))
if mibBuilder.loadTexts:pmo6006CfgLineSapiExpOtuTable.setStatus(_A)
_Pmo6006CfgLineSapiExpOtuEntry_Object=MibTableRow
pmo6006CfgLineSapiExpOtuEntry=_Pmo6006CfgLineSapiExpOtuEntry_Object((1,3,6,1,4,1,20044,70,9,13,1,1))
pmo6006CfgLineSapiExpOtuEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pmo6006CfgLineSapiExpOtuEntry.setStatus(_A)
class _Pmo6006CfgLineSapiExpOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLineSapiExpOtuIndex_Type.__name__=_D
_Pmo6006CfgLineSapiExpOtuIndex_Object=MibTableColumn
pmo6006CfgLineSapiExpOtuIndex=_Pmo6006CfgLineSapiExpOtuIndex_Object((1,3,6,1,4,1,20044,70,9,13,1,1,1),_Pmo6006CfgLineSapiExpOtuIndex_Type())
pmo6006CfgLineSapiExpOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLineSapiExpOtuIndex.setStatus(_A)
class _Pmo6006CfgLineSapiExpSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLineSapiExpSetupPortn_Type.__name__=_G
_Pmo6006CfgLineSapiExpSetupPortn_Object=MibTableColumn
pmo6006CfgLineSapiExpSetupPortn=_Pmo6006CfgLineSapiExpSetupPortn_Object((1,3,6,1,4,1,20044,70,9,13,1,1,3),_Pmo6006CfgLineSapiExpSetupPortn_Type())
pmo6006CfgLineSapiExpSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineSapiExpSetupPortn.setStatus(_A)
_Pmo6006CfgSapiAccLine_ObjectIdentity=ObjectIdentity
pmo6006CfgSapiAccLine=_Pmo6006CfgSapiAccLine_ObjectIdentity((1,3,6,1,4,1,20044,70,9,14))
_Pmo6006CfgLineSapiAccOtuTable_Object=MibTable
pmo6006CfgLineSapiAccOtuTable=_Pmo6006CfgLineSapiAccOtuTable_Object((1,3,6,1,4,1,20044,70,9,14,1))
if mibBuilder.loadTexts:pmo6006CfgLineSapiAccOtuTable.setStatus(_A)
_Pmo6006CfgLineSapiAccOtuEntry_Object=MibTableRow
pmo6006CfgLineSapiAccOtuEntry=_Pmo6006CfgLineSapiAccOtuEntry_Object((1,3,6,1,4,1,20044,70,9,14,1,1))
pmo6006CfgLineSapiAccOtuEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pmo6006CfgLineSapiAccOtuEntry.setStatus(_A)
class _Pmo6006CfgLineSapiAccOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLineSapiAccOtuIndex_Type.__name__=_D
_Pmo6006CfgLineSapiAccOtuIndex_Object=MibTableColumn
pmo6006CfgLineSapiAccOtuIndex=_Pmo6006CfgLineSapiAccOtuIndex_Object((1,3,6,1,4,1,20044,70,9,14,1,1,1),_Pmo6006CfgLineSapiAccOtuIndex_Type())
pmo6006CfgLineSapiAccOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLineSapiAccOtuIndex.setStatus(_A)
class _Pmo6006CfgLineSapiAccSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLineSapiAccSetupPortn_Type.__name__=_G
_Pmo6006CfgLineSapiAccSetupPortn_Object=MibTableColumn
pmo6006CfgLineSapiAccSetupPortn=_Pmo6006CfgLineSapiAccSetupPortn_Object((1,3,6,1,4,1,20044,70,9,14,1,1,3),_Pmo6006CfgLineSapiAccSetupPortn_Type())
pmo6006CfgLineSapiAccSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineSapiAccSetupPortn.setStatus(_K)
_Pmo6006CfgDapiTxLine_ObjectIdentity=ObjectIdentity
pmo6006CfgDapiTxLine=_Pmo6006CfgDapiTxLine_ObjectIdentity((1,3,6,1,4,1,20044,70,9,15))
_Pmo6006CfgLineDapiTxOtuTable_Object=MibTable
pmo6006CfgLineDapiTxOtuTable=_Pmo6006CfgLineDapiTxOtuTable_Object((1,3,6,1,4,1,20044,70,9,15,1))
if mibBuilder.loadTexts:pmo6006CfgLineDapiTxOtuTable.setStatus(_A)
_Pmo6006CfgLineDapiTxOtuEntry_Object=MibTableRow
pmo6006CfgLineDapiTxOtuEntry=_Pmo6006CfgLineDapiTxOtuEntry_Object((1,3,6,1,4,1,20044,70,9,15,1,1))
pmo6006CfgLineDapiTxOtuEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pmo6006CfgLineDapiTxOtuEntry.setStatus(_A)
class _Pmo6006CfgLineDapiTxOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLineDapiTxOtuIndex_Type.__name__=_D
_Pmo6006CfgLineDapiTxOtuIndex_Object=MibTableColumn
pmo6006CfgLineDapiTxOtuIndex=_Pmo6006CfgLineDapiTxOtuIndex_Object((1,3,6,1,4,1,20044,70,9,15,1,1,1),_Pmo6006CfgLineDapiTxOtuIndex_Type())
pmo6006CfgLineDapiTxOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLineDapiTxOtuIndex.setStatus(_A)
class _Pmo6006CfgLineDapiTxSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLineDapiTxSetupPortn_Type.__name__=_G
_Pmo6006CfgLineDapiTxSetupPortn_Object=MibTableColumn
pmo6006CfgLineDapiTxSetupPortn=_Pmo6006CfgLineDapiTxSetupPortn_Object((1,3,6,1,4,1,20044,70,9,15,1,1,3),_Pmo6006CfgLineDapiTxSetupPortn_Type())
pmo6006CfgLineDapiTxSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineDapiTxSetupPortn.setStatus(_A)
_Pmo6006CfgDapiExpLine_ObjectIdentity=ObjectIdentity
pmo6006CfgDapiExpLine=_Pmo6006CfgDapiExpLine_ObjectIdentity((1,3,6,1,4,1,20044,70,9,16))
_Pmo6006CfgLineDapiExpOtuTable_Object=MibTable
pmo6006CfgLineDapiExpOtuTable=_Pmo6006CfgLineDapiExpOtuTable_Object((1,3,6,1,4,1,20044,70,9,16,1))
if mibBuilder.loadTexts:pmo6006CfgLineDapiExpOtuTable.setStatus(_A)
_Pmo6006CfgLineDapiExpOtuEntry_Object=MibTableRow
pmo6006CfgLineDapiExpOtuEntry=_Pmo6006CfgLineDapiExpOtuEntry_Object((1,3,6,1,4,1,20044,70,9,16,1,1))
pmo6006CfgLineDapiExpOtuEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pmo6006CfgLineDapiExpOtuEntry.setStatus(_A)
class _Pmo6006CfgLineDapiExpOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLineDapiExpOtuIndex_Type.__name__=_D
_Pmo6006CfgLineDapiExpOtuIndex_Object=MibTableColumn
pmo6006CfgLineDapiExpOtuIndex=_Pmo6006CfgLineDapiExpOtuIndex_Object((1,3,6,1,4,1,20044,70,9,16,1,1,1),_Pmo6006CfgLineDapiExpOtuIndex_Type())
pmo6006CfgLineDapiExpOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLineDapiExpOtuIndex.setStatus(_A)
class _Pmo6006CfgLineDapiExpSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLineDapiExpSetupPortn_Type.__name__=_G
_Pmo6006CfgLineDapiExpSetupPortn_Object=MibTableColumn
pmo6006CfgLineDapiExpSetupPortn=_Pmo6006CfgLineDapiExpSetupPortn_Object((1,3,6,1,4,1,20044,70,9,16,1,1,3),_Pmo6006CfgLineDapiExpSetupPortn_Type())
pmo6006CfgLineDapiExpSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineDapiExpSetupPortn.setStatus(_A)
_Pmo6006CfgDapiAccLine_ObjectIdentity=ObjectIdentity
pmo6006CfgDapiAccLine=_Pmo6006CfgDapiAccLine_ObjectIdentity((1,3,6,1,4,1,20044,70,9,17))
_Pmo6006CfgLineDapiAccOtuTable_Object=MibTable
pmo6006CfgLineDapiAccOtuTable=_Pmo6006CfgLineDapiAccOtuTable_Object((1,3,6,1,4,1,20044,70,9,17,1))
if mibBuilder.loadTexts:pmo6006CfgLineDapiAccOtuTable.setStatus(_A)
_Pmo6006CfgLineDapiAccOtuEntry_Object=MibTableRow
pmo6006CfgLineDapiAccOtuEntry=_Pmo6006CfgLineDapiAccOtuEntry_Object((1,3,6,1,4,1,20044,70,9,17,1,1))
pmo6006CfgLineDapiAccOtuEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:pmo6006CfgLineDapiAccOtuEntry.setStatus(_A)
class _Pmo6006CfgLineDapiAccOtuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgLineDapiAccOtuIndex_Type.__name__=_D
_Pmo6006CfgLineDapiAccOtuIndex_Object=MibTableColumn
pmo6006CfgLineDapiAccOtuIndex=_Pmo6006CfgLineDapiAccOtuIndex_Object((1,3,6,1,4,1,20044,70,9,17,1,1,1),_Pmo6006CfgLineDapiAccOtuIndex_Type())
pmo6006CfgLineDapiAccOtuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLineDapiAccOtuIndex.setStatus(_A)
class _Pmo6006CfgLineDapiAccSetupPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmo6006CfgLineDapiAccSetupPortn_Type.__name__=_G
_Pmo6006CfgLineDapiAccSetupPortn_Object=MibTableColumn
pmo6006CfgLineDapiAccSetupPortn=_Pmo6006CfgLineDapiAccSetupPortn_Object((1,3,6,1,4,1,20044,70,9,17,1,1,3),_Pmo6006CfgLineDapiAccSetupPortn_Type())
pmo6006CfgLineDapiAccSetupPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgLineDapiAccSetupPortn.setStatus(_K)
_Pmo6006CfgStartuptablefive_ObjectIdentity=ObjectIdentity
pmo6006CfgStartuptablefive=_Pmo6006CfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,70,9,18))
_Pmo6006CfgOtxtlhcapabilitiesTable_Object=MibTable
pmo6006CfgOtxtlhcapabilitiesTable=_Pmo6006CfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,70,9,18,1))
if mibBuilder.loadTexts:pmo6006CfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pmo6006CfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pmo6006CfgOtxtlhcapabilitiesEntry=_Pmo6006CfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,70,9,18,1,1))
pmo6006CfgOtxtlhcapabilitiesEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:pmo6006CfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pmo6006CfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006CfgOtxtlhcapabilitiesIndex_Type.__name__=_D
_Pmo6006CfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pmo6006CfgOtxtlhcapabilitiesIndex=_Pmo6006CfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,70,9,18,1,1,1),_Pmo6006CfgOtxtlhcapabilitiesIndex_Type())
pmo6006CfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pmo6006CfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgComponentTypePortn_Type.__name__=_F
_Pmo6006CfgComponentTypePortn_Object=MibTableColumn
pmo6006CfgComponentTypePortn=_Pmo6006CfgComponentTypePortn_Object((1,3,6,1,4,1,20044,70,9,18,1,1,3),_Pmo6006CfgComponentTypePortn_Type())
pmo6006CfgComponentTypePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgComponentTypePortn.setStatus(_A)
class _Pmo6006CfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgMiscellaneousPortn_Type.__name__=_F
_Pmo6006CfgMiscellaneousPortn_Object=MibTableColumn
pmo6006CfgMiscellaneousPortn=_Pmo6006CfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,70,9,18,1,1,4),_Pmo6006CfgMiscellaneousPortn_Type())
pmo6006CfgMiscellaneousPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgMiscellaneousPortn.setStatus(_A)
class _Pmo6006CfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgFirstChannelPortn_Type.__name__=_F
_Pmo6006CfgFirstChannelPortn_Object=MibTableColumn
pmo6006CfgFirstChannelPortn=_Pmo6006CfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,70,9,18,1,1,5),_Pmo6006CfgFirstChannelPortn_Type())
pmo6006CfgFirstChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgFirstChannelPortn.setStatus(_A)
class _Pmo6006CfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgLastChannelPortn_Type.__name__=_F
_Pmo6006CfgLastChannelPortn_Object=MibTableColumn
pmo6006CfgLastChannelPortn=_Pmo6006CfgLastChannelPortn_Object((1,3,6,1,4,1,20044,70,9,18,1,1,6),_Pmo6006CfgLastChannelPortn_Type())
pmo6006CfgLastChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgLastChannelPortn.setStatus(_A)
class _Pmo6006CfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmo6006CfgGridPortn_Type.__name__=_F
_Pmo6006CfgGridPortn_Object=MibTableColumn
pmo6006CfgGridPortn=_Pmo6006CfgGridPortn_Object((1,3,6,1,4,1,20044,70,9,18,1,1,7),_Pmo6006CfgGridPortn_Type())
pmo6006CfgGridPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006CfgGridPortn.setStatus(_A)
_Pmo6006CfgWriteConfiguration_Type=EkiOnOff
_Pmo6006CfgWriteConfiguration_Object=MibScalar
pmo6006CfgWriteConfiguration=_Pmo6006CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,70,9,257),_Pmo6006CfgWriteConfiguration_Type())
pmo6006CfgWriteConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006CfgWriteConfiguration.setStatus(_A)
_Pmo6006traps_ObjectIdentity=ObjectIdentity
pmo6006traps=_Pmo6006traps_ObjectIdentity((1,3,6,1,4,1,20044,70,10))
class _Pmo6006trapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pmo6006trapPortNumber_Type.__name__=_D
_Pmo6006trapPortNumber_Object=MibScalar
pmo6006trapPortNumber=_Pmo6006trapPortNumber_Object((1,3,6,1,4,1,20044,70,10,2),_Pmo6006trapPortNumber_Type())
pmo6006trapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006trapPortNumber.setStatus(_A)
class _Pmo6006trapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pmo6006trapLineNumber_Type.__name__=_D
_Pmo6006trapLineNumber_Object=MibScalar
pmo6006trapLineNumber=_Pmo6006trapLineNumber_Object((1,3,6,1,4,1,20044,70,10,3),_Pmo6006trapLineNumber_Type())
pmo6006trapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006trapLineNumber.setStatus(_A)
class _Pmo6006trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pmo6006trapBoardNumber_Type.__name__=_D
_Pmo6006trapBoardNumber_Object=MibScalar
pmo6006trapBoardNumber=_Pmo6006trapBoardNumber_Object((1,3,6,1,4,1,20044,70,10,4),_Pmo6006trapBoardNumber_Type())
pmo6006trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006trapBoardNumber.setStatus(_A)
_Pmo6006Monitoring_ObjectIdentity=ObjectIdentity
pmo6006Monitoring=_Pmo6006Monitoring_ObjectIdentity((1,3,6,1,4,1,20044,70,11))
_Pmo6006MonOther_ObjectIdentity=ObjectIdentity
pmo6006MonOther=_Pmo6006MonOther_ObjectIdentity((1,3,6,1,4,1,20044,70,11,1))
_Pmo6006MonRmon_ObjectIdentity=ObjectIdentity
pmo6006MonRmon=_Pmo6006MonRmon_ObjectIdentity((1,3,6,1,4,1,20044,70,11,1,3))
_Pmo6006MonCountersReset_Type=EkiOnOff
_Pmo6006MonCountersReset_Object=MibScalar
pmo6006MonCountersReset=_Pmo6006MonCountersReset_Object((1,3,6,1,4,1,20044,70,11,1,3,359),_Pmo6006MonCountersReset_Type())
pmo6006MonCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006MonCountersReset.setStatus(_A)
_Pmo6006MonCountersStop_Type=EkiOnOff
_Pmo6006MonCountersStop_Object=MibScalar
pmo6006MonCountersStop=_Pmo6006MonCountersStop_Object((1,3,6,1,4,1,20044,70,11,1,3,360),_Pmo6006MonCountersStop_Type())
pmo6006MonCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pmo6006MonCountersStop.setStatus(_A)
_Pmo6006MonClient_ObjectIdentity=ObjectIdentity
pmo6006MonClient=_Pmo6006MonClient_ObjectIdentity((1,3,6,1,4,1,20044,70,11,2))
_Pmo6006MonClientRmonCounter_ObjectIdentity=ObjectIdentity
pmo6006MonClientRmonCounter=_Pmo6006MonClientRmonCounter_ObjectIdentity((1,3,6,1,4,1,20044,70,11,2,4))
_Pmo6006MonupRmonBytesCounterClientInputTable_Object=MibTable
pmo6006MonupRmonBytesCounterClientInputTable=_Pmo6006MonupRmonBytesCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,16))
if mibBuilder.loadTexts:pmo6006MonupRmonBytesCounterClientInputTable.setStatus(_A)
_Pmo6006MonupRmonBytesCounterClientInputEntry_Object=MibTableRow
pmo6006MonupRmonBytesCounterClientInputEntry=_Pmo6006MonupRmonBytesCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,16,1))
pmo6006MonupRmonBytesCounterClientInputEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:pmo6006MonupRmonBytesCounterClientInputEntry.setStatus(_A)
class _Pmo6006MonupRmonBytesCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MonupRmonBytesCounterClientInputIndex_Type.__name__=_D
_Pmo6006MonupRmonBytesCounterClientInputIndex_Object=MibTableColumn
pmo6006MonupRmonBytesCounterClientInputIndex=_Pmo6006MonupRmonBytesCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,16,1,1),_Pmo6006MonupRmonBytesCounterClientInputIndex_Type())
pmo6006MonupRmonBytesCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBytesCounterClientInputIndex.setStatus(_A)
_Pmo6006MonupRmonBytesCounterClientInputValuePortn_Type=Counter64
_Pmo6006MonupRmonBytesCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MonupRmonBytesCounterClientInputValuePortn=_Pmo6006MonupRmonBytesCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,16,1,2),_Pmo6006MonupRmonBytesCounterClientInputValuePortn_Type())
pmo6006MonupRmonBytesCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBytesCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MonupRmonBytesCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MonupRmonBytesCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MonupRmonBytesCounterClientInputErrorPortn=_Pmo6006MonupRmonBytesCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,16,1,3),_Pmo6006MonupRmonBytesCounterClientInputErrorPortn_Type())
pmo6006MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBytesCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MonupRmonBytesCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MonupRmonBytesCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MonupRmonBytesCounterClientInputOverloadPortn=_Pmo6006MonupRmonBytesCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,16,1,4),_Pmo6006MonupRmonBytesCounterClientInputOverloadPortn_Type())
pmo6006MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBytesCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MonupRmonCrcErrorsCounterClientInputTable_Object=MibTable
pmo6006MonupRmonCrcErrorsCounterClientInputTable=_Pmo6006MonupRmonCrcErrorsCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,32))
if mibBuilder.loadTexts:pmo6006MonupRmonCrcErrorsCounterClientInputTable.setStatus(_A)
_Pmo6006MonupRmonCrcErrorsCounterClientInputEntry_Object=MibTableRow
pmo6006MonupRmonCrcErrorsCounterClientInputEntry=_Pmo6006MonupRmonCrcErrorsCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,32,1))
pmo6006MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:pmo6006MonupRmonCrcErrorsCounterClientInputEntry.setStatus(_A)
class _Pmo6006MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__=_D
_Pmo6006MonupRmonCrcErrorsCounterClientInputIndex_Object=MibTableColumn
pmo6006MonupRmonCrcErrorsCounterClientInputIndex=_Pmo6006MonupRmonCrcErrorsCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,32,1,1),_Pmo6006MonupRmonCrcErrorsCounterClientInputIndex_Type())
pmo6006MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonCrcErrorsCounterClientInputIndex.setStatus(_A)
_Pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn_Type=Counter64
_Pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn=_Pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,32,1,2),_Pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn_Type())
pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn=_Pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,32,1,3),_Pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn_Type())
pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn=_Pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,32,1,4),_Pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type())
pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MonupRmonPacketsCounterClientInputTable_Object=MibTable
pmo6006MonupRmonPacketsCounterClientInputTable=_Pmo6006MonupRmonPacketsCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,48))
if mibBuilder.loadTexts:pmo6006MonupRmonPacketsCounterClientInputTable.setStatus(_A)
_Pmo6006MonupRmonPacketsCounterClientInputEntry_Object=MibTableRow
pmo6006MonupRmonPacketsCounterClientInputEntry=_Pmo6006MonupRmonPacketsCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,48,1))
pmo6006MonupRmonPacketsCounterClientInputEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:pmo6006MonupRmonPacketsCounterClientInputEntry.setStatus(_A)
class _Pmo6006MonupRmonPacketsCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MonupRmonPacketsCounterClientInputIndex_Type.__name__=_D
_Pmo6006MonupRmonPacketsCounterClientInputIndex_Object=MibTableColumn
pmo6006MonupRmonPacketsCounterClientInputIndex=_Pmo6006MonupRmonPacketsCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,48,1,1),_Pmo6006MonupRmonPacketsCounterClientInputIndex_Type())
pmo6006MonupRmonPacketsCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPacketsCounterClientInputIndex.setStatus(_A)
_Pmo6006MonupRmonPacketsCounterClientInputValuePortn_Type=Counter64
_Pmo6006MonupRmonPacketsCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MonupRmonPacketsCounterClientInputValuePortn=_Pmo6006MonupRmonPacketsCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,48,1,2),_Pmo6006MonupRmonPacketsCounterClientInputValuePortn_Type())
pmo6006MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPacketsCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MonupRmonPacketsCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MonupRmonPacketsCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MonupRmonPacketsCounterClientInputErrorPortn=_Pmo6006MonupRmonPacketsCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,48,1,3),_Pmo6006MonupRmonPacketsCounterClientInputErrorPortn_Type())
pmo6006MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPacketsCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MonupRmonPacketsCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MonupRmonPacketsCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MonupRmonPacketsCounterClientInputOverloadPortn=_Pmo6006MonupRmonPacketsCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,48,1,4),_Pmo6006MonupRmonPacketsCounterClientInputOverloadPortn_Type())
pmo6006MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPacketsCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MonupRmonBroadcastCounterClientInputTable_Object=MibTable
pmo6006MonupRmonBroadcastCounterClientInputTable=_Pmo6006MonupRmonBroadcastCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,64))
if mibBuilder.loadTexts:pmo6006MonupRmonBroadcastCounterClientInputTable.setStatus(_A)
_Pmo6006MonupRmonBroadcastCounterClientInputEntry_Object=MibTableRow
pmo6006MonupRmonBroadcastCounterClientInputEntry=_Pmo6006MonupRmonBroadcastCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,64,1))
pmo6006MonupRmonBroadcastCounterClientInputEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:pmo6006MonupRmonBroadcastCounterClientInputEntry.setStatus(_A)
class _Pmo6006MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MonupRmonBroadcastCounterClientInputIndex_Type.__name__=_D
_Pmo6006MonupRmonBroadcastCounterClientInputIndex_Object=MibTableColumn
pmo6006MonupRmonBroadcastCounterClientInputIndex=_Pmo6006MonupRmonBroadcastCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,64,1,1),_Pmo6006MonupRmonBroadcastCounterClientInputIndex_Type())
pmo6006MonupRmonBroadcastCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBroadcastCounterClientInputIndex.setStatus(_A)
_Pmo6006MonupRmonBroadcastCounterClientInputValuePortn_Type=Counter64
_Pmo6006MonupRmonBroadcastCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MonupRmonBroadcastCounterClientInputValuePortn=_Pmo6006MonupRmonBroadcastCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,64,1,2),_Pmo6006MonupRmonBroadcastCounterClientInputValuePortn_Type())
pmo6006MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBroadcastCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MonupRmonBroadcastCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MonupRmonBroadcastCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MonupRmonBroadcastCounterClientInputErrorPortn=_Pmo6006MonupRmonBroadcastCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,64,1,3),_Pmo6006MonupRmonBroadcastCounterClientInputErrorPortn_Type())
pmo6006MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBroadcastCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn=_Pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,64,1,4),_Pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn_Type())
pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MonupRmonMulticastCounterClientInputTable_Object=MibTable
pmo6006MonupRmonMulticastCounterClientInputTable=_Pmo6006MonupRmonMulticastCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,80))
if mibBuilder.loadTexts:pmo6006MonupRmonMulticastCounterClientInputTable.setStatus(_A)
_Pmo6006MonupRmonMulticastCounterClientInputEntry_Object=MibTableRow
pmo6006MonupRmonMulticastCounterClientInputEntry=_Pmo6006MonupRmonMulticastCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,80,1))
pmo6006MonupRmonMulticastCounterClientInputEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:pmo6006MonupRmonMulticastCounterClientInputEntry.setStatus(_A)
class _Pmo6006MonupRmonMulticastCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MonupRmonMulticastCounterClientInputIndex_Type.__name__=_D
_Pmo6006MonupRmonMulticastCounterClientInputIndex_Object=MibTableColumn
pmo6006MonupRmonMulticastCounterClientInputIndex=_Pmo6006MonupRmonMulticastCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,80,1,1),_Pmo6006MonupRmonMulticastCounterClientInputIndex_Type())
pmo6006MonupRmonMulticastCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonMulticastCounterClientInputIndex.setStatus(_A)
_Pmo6006MonupRmonMulticastCounterClientInputValuePortn_Type=Counter64
_Pmo6006MonupRmonMulticastCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MonupRmonMulticastCounterClientInputValuePortn=_Pmo6006MonupRmonMulticastCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,80,1,2),_Pmo6006MonupRmonMulticastCounterClientInputValuePortn_Type())
pmo6006MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonMulticastCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MonupRmonMulticastCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MonupRmonMulticastCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MonupRmonMulticastCounterClientInputErrorPortn=_Pmo6006MonupRmonMulticastCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,80,1,3),_Pmo6006MonupRmonMulticastCounterClientInputErrorPortn_Type())
pmo6006MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonMulticastCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MonupRmonMulticastCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MonupRmonMulticastCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MonupRmonMulticastCounterClientInputOverloadPortn=_Pmo6006MonupRmonMulticastCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,80,1,4),_Pmo6006MonupRmonMulticastCounterClientInputOverloadPortn_Type())
pmo6006MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonMulticastCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MonupRmonPauseFrameCounterClientInputTable_Object=MibTable
pmo6006MonupRmonPauseFrameCounterClientInputTable=_Pmo6006MonupRmonPauseFrameCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,96))
if mibBuilder.loadTexts:pmo6006MonupRmonPauseFrameCounterClientInputTable.setStatus(_A)
_Pmo6006MonupRmonPauseFrameCounterClientInputEntry_Object=MibTableRow
pmo6006MonupRmonPauseFrameCounterClientInputEntry=_Pmo6006MonupRmonPauseFrameCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,96,1))
pmo6006MonupRmonPauseFrameCounterClientInputEntry.setIndexNames((0,_C,_AV))
if mibBuilder.loadTexts:pmo6006MonupRmonPauseFrameCounterClientInputEntry.setStatus(_A)
class _Pmo6006MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MonupRmonPauseFrameCounterClientInputIndex_Type.__name__=_D
_Pmo6006MonupRmonPauseFrameCounterClientInputIndex_Object=MibTableColumn
pmo6006MonupRmonPauseFrameCounterClientInputIndex=_Pmo6006MonupRmonPauseFrameCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,96,1,1),_Pmo6006MonupRmonPauseFrameCounterClientInputIndex_Type())
pmo6006MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPauseFrameCounterClientInputIndex.setStatus(_A)
_Pmo6006MonupRmonPauseFrameCounterClientInputValuePortn_Type=Counter64
_Pmo6006MonupRmonPauseFrameCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MonupRmonPauseFrameCounterClientInputValuePortn=_Pmo6006MonupRmonPauseFrameCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,96,1,2),_Pmo6006MonupRmonPauseFrameCounterClientInputValuePortn_Type())
pmo6006MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPauseFrameCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn=_Pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,96,1,3),_Pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn_Type())
pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn=_Pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,96,1,4),_Pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn_Type())
pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MondwRmonCrcErrorsCounterClientInputTable_Object=MibTable
pmo6006MondwRmonCrcErrorsCounterClientInputTable=_Pmo6006MondwRmonCrcErrorsCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,224))
if mibBuilder.loadTexts:pmo6006MondwRmonCrcErrorsCounterClientInputTable.setStatus(_A)
_Pmo6006MondwRmonCrcErrorsCounterClientInputEntry_Object=MibTableRow
pmo6006MondwRmonCrcErrorsCounterClientInputEntry=_Pmo6006MondwRmonCrcErrorsCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,224,1))
pmo6006MondwRmonCrcErrorsCounterClientInputEntry.setIndexNames((0,_C,_AW))
if mibBuilder.loadTexts:pmo6006MondwRmonCrcErrorsCounterClientInputEntry.setStatus(_A)
class _Pmo6006MondwRmonCrcErrorsCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MondwRmonCrcErrorsCounterClientInputIndex_Type.__name__=_D
_Pmo6006MondwRmonCrcErrorsCounterClientInputIndex_Object=MibTableColumn
pmo6006MondwRmonCrcErrorsCounterClientInputIndex=_Pmo6006MondwRmonCrcErrorsCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,224,1,1),_Pmo6006MondwRmonCrcErrorsCounterClientInputIndex_Type())
pmo6006MondwRmonCrcErrorsCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonCrcErrorsCounterClientInputIndex.setStatus(_A)
_Pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn_Type=Counter64
_Pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn=_Pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,224,1,2),_Pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn_Type())
pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn=_Pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,224,1,3),_Pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn_Type())
pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn=_Pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,224,1,4),_Pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn_Type())
pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn.setStatus(_A)
_Pmo6006MondwRmonPacketsCounterClientInputTable_Object=MibTable
pmo6006MondwRmonPacketsCounterClientInputTable=_Pmo6006MondwRmonPacketsCounterClientInputTable_Object((1,3,6,1,4,1,20044,70,11,2,4,240))
if mibBuilder.loadTexts:pmo6006MondwRmonPacketsCounterClientInputTable.setStatus(_A)
_Pmo6006MondwRmonPacketsCounterClientInputEntry_Object=MibTableRow
pmo6006MondwRmonPacketsCounterClientInputEntry=_Pmo6006MondwRmonPacketsCounterClientInputEntry_Object((1,3,6,1,4,1,20044,70,11,2,4,240,1))
pmo6006MondwRmonPacketsCounterClientInputEntry.setIndexNames((0,_C,_AX))
if mibBuilder.loadTexts:pmo6006MondwRmonPacketsCounterClientInputEntry.setStatus(_A)
class _Pmo6006MondwRmonPacketsCounterClientInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmo6006MondwRmonPacketsCounterClientInputIndex_Type.__name__=_D
_Pmo6006MondwRmonPacketsCounterClientInputIndex_Object=MibTableColumn
pmo6006MondwRmonPacketsCounterClientInputIndex=_Pmo6006MondwRmonPacketsCounterClientInputIndex_Object((1,3,6,1,4,1,20044,70,11,2,4,240,1,1),_Pmo6006MondwRmonPacketsCounterClientInputIndex_Type())
pmo6006MondwRmonPacketsCounterClientInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonPacketsCounterClientInputIndex.setStatus(_A)
_Pmo6006MondwRmonPacketsCounterClientInputValuePortn_Type=Counter64
_Pmo6006MondwRmonPacketsCounterClientInputValuePortn_Object=MibTableColumn
pmo6006MondwRmonPacketsCounterClientInputValuePortn=_Pmo6006MondwRmonPacketsCounterClientInputValuePortn_Object((1,3,6,1,4,1,20044,70,11,2,4,240,1,2),_Pmo6006MondwRmonPacketsCounterClientInputValuePortn_Type())
pmo6006MondwRmonPacketsCounterClientInputValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonPacketsCounterClientInputValuePortn.setStatus(_A)
_Pmo6006MondwRmonPacketsCounterClientInputErrorPortn_Type=EkiOnOff
_Pmo6006MondwRmonPacketsCounterClientInputErrorPortn_Object=MibTableColumn
pmo6006MondwRmonPacketsCounterClientInputErrorPortn=_Pmo6006MondwRmonPacketsCounterClientInputErrorPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,240,1,3),_Pmo6006MondwRmonPacketsCounterClientInputErrorPortn_Type())
pmo6006MondwRmonPacketsCounterClientInputErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonPacketsCounterClientInputErrorPortn.setStatus(_A)
_Pmo6006MondwRmonPacketsCounterClientInputOverloadPortn_Type=EkiOnOff
_Pmo6006MondwRmonPacketsCounterClientInputOverloadPortn_Object=MibTableColumn
pmo6006MondwRmonPacketsCounterClientInputOverloadPortn=_Pmo6006MondwRmonPacketsCounterClientInputOverloadPortn_Object((1,3,6,1,4,1,20044,70,11,2,4,240,1,4),_Pmo6006MondwRmonPacketsCounterClientInputOverloadPortn_Type())
pmo6006MondwRmonPacketsCounterClientInputOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmo6006MondwRmonPacketsCounterClientInputOverloadPortn.setStatus(_A)
pmo6006LineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,30))
pmo6006LineTrapNotUrgentGoesOn.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pmo6006LineTrapNotUrgentGoesOn.setStatus(_A)
pmo6006LineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,31))
pmo6006LineTrapNotUrgentGoesOff.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pmo6006LineTrapNotUrgentGoesOff.setStatus(_A)
pmo6006LineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,32))
pmo6006LineTrapUrgentGoesOn.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pmo6006LineTrapUrgentGoesOn.setStatus(_A)
pmo6006LineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,33))
pmo6006LineTrapUrgentGoesOff.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pmo6006LineTrapUrgentGoesOff.setStatus(_A)
pmo6006LineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,34))
pmo6006LineTrapCritGoesOn.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pmo6006LineTrapCritGoesOn.setStatus(_A)
pmo6006LineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,35))
pmo6006LineTrapCritGoesOff.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pmo6006LineTrapCritGoesOff.setStatus(_A)
pmo6006ClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,40))
pmo6006ClientTrapNotUrgentGoesOn.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pmo6006ClientTrapNotUrgentGoesOn.setStatus(_A)
pmo6006ClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,41))
pmo6006ClientTrapNotUrgentGoesOff.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pmo6006ClientTrapNotUrgentGoesOff.setStatus(_A)
pmo6006ClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,42))
pmo6006ClientTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pmo6006ClientTrapUrgentGoesOn.setStatus(_A)
pmo6006ClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,43))
pmo6006ClientTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pmo6006ClientTrapUrgentGoesOff.setStatus(_A)
pmo6006ClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,44))
pmo6006ClientTrapCritGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pmo6006ClientTrapCritGoesOn.setStatus(_A)
pmo6006ClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,45))
pmo6006ClientTrapCritGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pmo6006ClientTrapCritGoesOff.setStatus(_A)
pmo6006PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,70,10,50))
pmo6006PowerTrapUrgentGoesOn.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pmo6006PowerTrapUrgentGoesOn.setStatus(_A)
pmo6006PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,70,10,51))
pmo6006PowerTrapUrgentGoesOff.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pmo6006PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Pmo6006OtxGrid':Pmo6006OtxGrid,'Pmo6006DccMode':Pmo6006DccMode,'Pmo6006LineChannel':Pmo6006LineChannel,'Pmo6006Odu2SapiMode':Pmo6006Odu2SapiMode,'Pmo6006Otu2SapiMode':Pmo6006Otu2SapiMode,'modulePmo6006':modulePmo6006,'pmo6006alarms':pmo6006alarms,'pmo6006AlmOther':pmo6006AlmOther,'pmo6006AlmOtherNurg':pmo6006AlmOtherNurg,'pmo6006AlmsynthAlm2':pmo6006AlmsynthAlm2,'pmo6006AlmConfTableSave':pmo6006AlmConfTableSave,'pmo6006AlmInvUpload':pmo6006AlmInvUpload,'pmo6006AlmConfTableLoad':pmo6006AlmConfTableLoad,'pmo6006AlmCorrelatOff':pmo6006AlmCorrelatOff,'pmo6006AlmOtherUrg':pmo6006AlmOtherUrg,'pmo6006AlmOtherCrit':pmo6006AlmOtherCrit,'pmo6006AlmsynthAlm0':pmo6006AlmsynthAlm0,'pmo6006AlmModGlobFail':pmo6006AlmModGlobFail,_U:pmo6006AlmDefFuseA,_T:pmo6006AlmDefFuseB,'pmo6006AlmClient':pmo6006AlmClient,'pmo6006AlmClientNurg':pmo6006AlmClientNurg,'pmo6006AlmclientSfpWarnDdmTable':pmo6006AlmclientSfpWarnDdmTable,'pmo6006AlmclientSfpWarnDdmEntry':pmo6006AlmclientSfpWarnDdmEntry,_W:pmo6006AlmclientSfpWarnDdmIndex,'pmo6006AlmClientTxPwLowWngPortn':pmo6006AlmClientTxPwLowWngPortn,'pmo6006AlmClientTxPwrHighWngPortn':pmo6006AlmClientTxPwrHighWngPortn,'pmo6006AlmClientTxBiasLowWngPortn':pmo6006AlmClientTxBiasLowWngPortn,'pmo6006AlmClientTxBiasHighWngPortn':pmo6006AlmClientTxBiasHighWngPortn,'pmo6006AlmClientVccLowWngPortn':pmo6006AlmClientVccLowWngPortn,'pmo6006AlmClientVccHighWngPortn':pmo6006AlmClientVccHighWngPortn,'pmo6006AlmClientTempLowWngPortn':pmo6006AlmClientTempLowWngPortn,'pmo6006AlmClientTempHighWngPortn':pmo6006AlmClientTempHighWngPortn,'pmo6006AlmClientRxPwrLowWngPortn':pmo6006AlmClientRxPwrLowWngPortn,'pmo6006AlmClientRxPwrHighWngPortn':pmo6006AlmClientRxPwrHighWngPortn,'pmo6006AlmClientUrg':pmo6006AlmClientUrg,'pmo6006AlmclientHostLaneFaultTable':pmo6006AlmclientHostLaneFaultTable,'pmo6006AlmclientHostLaneFaultEntry':pmo6006AlmclientHostLaneFaultEntry,_X:pmo6006AlmclientHostLaneFaultIndex,'pmo6006AlmClientLossOfSyncPortn':pmo6006AlmClientLossOfSyncPortn,'pmo6006AlmClientInputLossOfSigPortn':pmo6006AlmClientInputLossOfSigPortn,'pmo6006AlmClientOdu2eDplmPortn':pmo6006AlmClientOdu2eDplmPortn,'pmo6006AlmClientOdu2eDdegPortn':pmo6006AlmClientOdu2eDdegPortn,'pmo6006AlmClientCsfDetectedPortn':pmo6006AlmClientCsfDetectedPortn,'pmo6006AlmClientOdu2eIaisPortn':pmo6006AlmClientOdu2eIaisPortn,'pmo6006AlmClientOdu2eDtimPortn':pmo6006AlmClientOdu2eDtimPortn,'pmo6006AlmClientOdu2eDaisPortn':pmo6006AlmClientOdu2eDaisPortn,'pmo6006AlmClientLaneTxFifoErrorPortn':pmo6006AlmClientLaneTxFifoErrorPortn,'pmo6006AlmClientOdu2eIociPortn':pmo6006AlmClientOdu2eIociPortn,'pmo6006AlmClientOdu2eDociPortn':pmo6006AlmClientOdu2eDociPortn,'pmo6006AlmClientOdu2eIbdiPortn':pmo6006AlmClientOdu2eIbdiPortn,'pmo6006AlmClientOdu2eDbdiPortn':pmo6006AlmClientOdu2eDbdiPortn,'pmo6006AlmClientOdu2eIlckPortn':pmo6006AlmClientOdu2eIlckPortn,'pmo6006AlmClientOdu2eDlckPortn':pmo6006AlmClientOdu2eDlckPortn,'pmo6006AlmclientSfpAlmDdmTable':pmo6006AlmclientSfpAlmDdmTable,'pmo6006AlmclientSfpAlmDdmEntry':pmo6006AlmclientSfpAlmDdmEntry,_Y:pmo6006AlmclientSfpAlmDdmIndex,'pmo6006AlmClientTxPwrLowAlaPortn':pmo6006AlmClientTxPwrLowAlaPortn,'pmo6006AlmClientTxPwrHighAlaPortn':pmo6006AlmClientTxPwrHighAlaPortn,'pmo6006AlmClientTxBiasLowAlaPortn':pmo6006AlmClientTxBiasLowAlaPortn,'pmo6006AlmClientTxBiasHighAlaPortn':pmo6006AlmClientTxBiasHighAlaPortn,'pmo6006AlmClientVccLowAlaPortn':pmo6006AlmClientVccLowAlaPortn,'pmo6006AlmClientVccHighAlaPortn':pmo6006AlmClientVccHighAlaPortn,'pmo6006AlmClientTempLowAlaPortn':pmo6006AlmClientTempLowAlaPortn,'pmo6006AlmClientTempHighAlaPortn':pmo6006AlmClientTempHighAlaPortn,'pmo6006AlmClientRxPwrLowAlaPortn':pmo6006AlmClientRxPwrLowAlaPortn,'pmo6006AlmClientRxPwrHighAlaPortn':pmo6006AlmClientRxPwrHighAlaPortn,'pmo6006AlmClientCrit':pmo6006AlmClientCrit,'pmo6006AlmsynthAlmPortTable':pmo6006AlmsynthAlmPortTable,'pmo6006AlmsynthAlmPortEntry':pmo6006AlmsynthAlmPortEntry,_Z:pmo6006AlmsynthAlmPortIndex,'pmo6006AlmSfpAbsentPortn':pmo6006AlmSfpAbsentPortn,'pmo6006AlmDdmAbsentPortn':pmo6006AlmDdmAbsentPortn,_S:pmo6006AlmHwFailAccPortn,'pmo6006AlmDwLsdPortn':pmo6006AlmDwLsdPortn,'pmo6006AlmClientLocalOosPortn':pmo6006AlmClientLocalOosPortn,'pmo6006AlmClientRemoteOosPortn':pmo6006AlmClientRemoteOosPortn,'pmo6006AlmDwCaisPortn':pmo6006AlmDwCaisPortn,_P:pmo6006AlmSfpDdmWarningPortn,_Q:pmo6006AlmSfpDdmAlmPortn,_R:pmo6006AlmFailAccPortn,'pmo6006AlmUpCsfPortn':pmo6006AlmUpCsfPortn,'pmo6006AlmLine':pmo6006AlmLine,'pmo6006AlmLineNurg':pmo6006AlmLineNurg,'pmo6006AlmLineUrg':pmo6006AlmLineUrg,'pmo6006AlmlineNetworkLaneAlarmWarning1Table':pmo6006AlmlineNetworkLaneAlarmWarning1Table,'pmo6006AlmlineNetworkLaneAlarmWarning1Entry':pmo6006AlmlineNetworkLaneAlarmWarning1Entry,_a:pmo6006AlmlineNetworkLaneAlarmWarning1Index,'pmo6006AlmLineTxPwrLowAlaPortn':pmo6006AlmLineTxPwrLowAlaPortn,'pmo6006AlmLineTxPwrHighAlaPortn':pmo6006AlmLineTxPwrHighAlaPortn,'pmo6006AlmLineTxBiasLowAlaPortn':pmo6006AlmLineTxBiasLowAlaPortn,'pmo6006AlmLineTxBiasHighAlaPortn':pmo6006AlmLineTxBiasHighAlaPortn,'pmo6006AlmLineVccLowAlaPortn':pmo6006AlmLineVccLowAlaPortn,'pmo6006AlmLineVccHighAlaPortn':pmo6006AlmLineVccHighAlaPortn,'pmo6006AlmLineTempLowAlaPortn':pmo6006AlmLineTempLowAlaPortn,'pmo6006AlmLineTempHighAlaPortn':pmo6006AlmLineTempHighAlaPortn,'pmo6006AlmLineRxPwrLowAlaPortn':pmo6006AlmLineRxPwrLowAlaPortn,'pmo6006AlmLineRxPwrHighAlaPortn':pmo6006AlmLineRxPwrHighAlaPortn,'pmo6006AlmlineNetworkLaneAlarmWarning2Table':pmo6006AlmlineNetworkLaneAlarmWarning2Table,'pmo6006AlmlineNetworkLaneAlarmWarning2Entry':pmo6006AlmlineNetworkLaneAlarmWarning2Entry,_b:pmo6006AlmlineNetworkLaneAlarmWarning2Index,'pmo6006AlmLineTxPwLowWngPortn':pmo6006AlmLineTxPwLowWngPortn,'pmo6006AlmLineTxPwrHighWngPortn':pmo6006AlmLineTxPwrHighWngPortn,'pmo6006AlmLineTxBiasLowWngPortn':pmo6006AlmLineTxBiasLowWngPortn,'pmo6006AlmLineTxBiasHighWngPortn':pmo6006AlmLineTxBiasHighWngPortn,'pmo6006AlmLineVccLowWngPortn':pmo6006AlmLineVccLowWngPortn,'pmo6006AlmLineVccHighWngPortn':pmo6006AlmLineVccHighWngPortn,'pmo6006AlmLineTempLowWngPortn':pmo6006AlmLineTempLowWngPortn,'pmo6006AlmLineTempHighWngPortn':pmo6006AlmLineTempHighWngPortn,'pmo6006AlmLineRxPwrLowWngPortn':pmo6006AlmLineRxPwrLowWngPortn,'pmo6006AlmLineRxPwrHighWngPortn':pmo6006AlmLineRxPwrHighWngPortn,'pmo6006AlmlineHostLaneFaultTable':pmo6006AlmlineHostLaneFaultTable,'pmo6006AlmlineHostLaneFaultEntry':pmo6006AlmlineHostLaneFaultEntry,_c:pmo6006AlmlineHostLaneFaultIndex,'pmo6006AlmLineInputLossOfSignalPortn':pmo6006AlmLineInputLossOfSignalPortn,'pmo6006AlmLineLossOfFramePortn':pmo6006AlmLineLossOfFramePortn,'pmo6006AlmLineSmBdiInsertedPortn':pmo6006AlmLineSmBdiInsertedPortn,'pmo6006AlmLineSmBdiDetectedPortn':pmo6006AlmLineSmBdiDetectedPortn,'pmo6006AlmOtu2eDdegPortn':pmo6006AlmOtu2eDdegPortn,'pmo6006AlmClientOtu2eDtimPortn':pmo6006AlmClientOtu2eDtimPortn,'pmo6006AlmLineOchr2eDlosPPortn':pmo6006AlmLineOchr2eDlosPPortn,'pmo6006AlmLineOtu2eDssfPortn':pmo6006AlmLineOtu2eDssfPortn,'pmo6006AlmLineOtu2eDlomPortn':pmo6006AlmLineOtu2eDlomPortn,'pmo6006AlmLineCrit':pmo6006AlmLineCrit,'pmo6006AlmsynthAlmLineTable':pmo6006AlmsynthAlmLineTable,'pmo6006AlmsynthAlmLineEntry':pmo6006AlmsynthAlmLineEntry,_d:pmo6006AlmsynthAlmLineIndex,'pmo6006AlmLineSfpAbsentPortn':pmo6006AlmLineSfpAbsentPortn,'pmo6006AlmLineDdmAbsentPortn':pmo6006AlmLineDdmAbsentPortn,_O:pmo6006AlmLineHwFailPortn,'pmo6006AlmLineTxOffPortn':pmo6006AlmLineTxOffPortn,'pmo6006AlmLineLocalOosPortn':pmo6006AlmLineLocalOosPortn,'pmo6006AlmUpRdiInsPortn':pmo6006AlmUpRdiInsPortn,_L:pmo6006AlmLineDdmWarningPortn,_M:pmo6006AlmLineDdmAlmPortn,_N:pmo6006AlmLineFailPortn,'pmo6006measures':pmo6006measures,'pmo6006MesrOther':pmo6006MesrOther,'pmo6006MesrClient':pmo6006MesrClient,'pmo6006MesrclientTempTable':pmo6006MesrclientTempTable,'pmo6006MesrclientTempEntry':pmo6006MesrclientTempEntry,_e:pmo6006MesrclientTempIndex,'pmo6006MesrclientTempPortn':pmo6006MesrclientTempPortn,'pmo6006MesrclientTxBiasTable':pmo6006MesrclientTxBiasTable,'pmo6006MesrclientTxBiasEntry':pmo6006MesrclientTxBiasEntry,_f:pmo6006MesrclientTxBiasIndex,'pmo6006MesrclientTxBiasPortn':pmo6006MesrclientTxBiasPortn,'pmo6006MesrclientTxPwrTable':pmo6006MesrclientTxPwrTable,'pmo6006MesrclientTxPwrEntry':pmo6006MesrclientTxPwrEntry,_g:pmo6006MesrclientTxPwrIndex,'pmo6006MesrclientTxPwrPortn':pmo6006MesrclientTxPwrPortn,'pmo6006MesrclientRxPwrTable':pmo6006MesrclientRxPwrTable,'pmo6006MesrclientRxPwrEntry':pmo6006MesrclientRxPwrEntry,_h:pmo6006MesrclientRxPwrIndex,'pmo6006MesrclientRxPwrPortn':pmo6006MesrclientRxPwrPortn,'pmo6006MesrLine':pmo6006MesrLine,'pmo6006MesrlineTxPwrTable':pmo6006MesrlineTxPwrTable,'pmo6006MesrlineTxPwrEntry':pmo6006MesrlineTxPwrEntry,_i:pmo6006MesrlineTxPwrIndex,'pmo6006MesrlineTxPwrPortn':pmo6006MesrlineTxPwrPortn,'pmo6006MesrlineTempTable':pmo6006MesrlineTempTable,'pmo6006MesrlineTempEntry':pmo6006MesrlineTempEntry,_j:pmo6006MesrlineTempIndex,'pmo6006MesrlineTempPortn':pmo6006MesrlineTempPortn,'pmo6006MesrlineTxBiasTable':pmo6006MesrlineTxBiasTable,'pmo6006MesrlineTxBiasEntry':pmo6006MesrlineTxBiasEntry,_k:pmo6006MesrlineTxBiasIndex,'pmo6006MesrlineTxBiasPortn':pmo6006MesrlineTxBiasPortn,'pmo6006MesrlineRxPwrTable':pmo6006MesrlineRxPwrTable,'pmo6006MesrlineRxPwrEntry':pmo6006MesrlineRxPwrEntry,_l:pmo6006MesrlineRxPwrIndex,'pmo6006MesrlineRxPwrPortn':pmo6006MesrlineRxPwrPortn,'pmo6006counters':pmo6006counters,'pmo6006CntOther':pmo6006CntOther,'pmo6006CntClient':pmo6006CntClient,'pmo6006CntclientRemoteBipTable':pmo6006CntclientRemoteBipTable,'pmo6006CntclientRemoteBipEntry':pmo6006CntclientRemoteBipEntry,_m:pmo6006CntclientRemoteBipIndex,'pmo6006CntclientRemoteBipValuePortn':pmo6006CntclientRemoteBipValuePortn,'pmo6006CntclientRemoteBipErrorPortn':pmo6006CntclientRemoteBipErrorPortn,'pmo6006CntclientRemoteBipOverloadPortn':pmo6006CntclientRemoteBipOverloadPortn,'pmo6006CntclientCbipCounterTable':pmo6006CntclientCbipCounterTable,'pmo6006CntclientCbipCounterEntry':pmo6006CntclientCbipCounterEntry,_n:pmo6006CntclientCbipCounterIndex,'pmo6006CntclientCbipCounterValuePortn':pmo6006CntclientCbipCounterValuePortn,'pmo6006CntclientCbipCounterErrorPortn':pmo6006CntclientCbipCounterErrorPortn,'pmo6006CntclientCbipCounterOverloadPortn':pmo6006CntclientCbipCounterOverloadPortn,'pmo6006CntLine':pmo6006CntLine,'pmo6006CntlocalLineSmBip8ErrorCounterTable':pmo6006CntlocalLineSmBip8ErrorCounterTable,'pmo6006CntlocalLineSmBip8ErrorCounterEntry':pmo6006CntlocalLineSmBip8ErrorCounterEntry,_o:pmo6006CntlocalLineSmBip8ErrorCounterIndex,'pmo6006CntlocalLineSmBip8ErrorCounterValuePortn':pmo6006CntlocalLineSmBip8ErrorCounterValuePortn,'pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn':pmo6006CntlocalLineSmBip8ErrorCounterErrorPortn,'pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn':pmo6006CntlocalLineSmBip8ErrorCounterOverloadPortn,'pmo6006CntlocalLineFecCorrectedErrorsCounterTable':pmo6006CntlocalLineFecCorrectedErrorsCounterTable,'pmo6006CntlocalLineFecCorrectedErrorsCounterEntry':pmo6006CntlocalLineFecCorrectedErrorsCounterEntry,_p:pmo6006CntlocalLineFecCorrectedErrorsCounterIndex,'pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn':pmo6006CntlocalLineFecCorrectedErrorsCounterValuePortn,'pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn':pmo6006CntlocalLineFecCorrectedErrorsCounterErrorPortn,'pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn':pmo6006CntlocalLineFecCorrectedErrorsCounterOverloadPortn,'pmo6006CntremoteLineSmBip8ErrorCounterTable':pmo6006CntremoteLineSmBip8ErrorCounterTable,'pmo6006CntremoteLineSmBip8ErrorCounterEntry':pmo6006CntremoteLineSmBip8ErrorCounterEntry,_q:pmo6006CntremoteLineSmBip8ErrorCounterIndex,'pmo6006CntremoteLineSmBip8ErrorCounterValuePortn':pmo6006CntremoteLineSmBip8ErrorCounterValuePortn,'pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn':pmo6006CntremoteLineSmBip8ErrorCounterErrorPortn,'pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn':pmo6006CntremoteLineSmBip8ErrorCounterOverloadPortn,'pmo6006CntlineDfrmTimCntTable':pmo6006CntlineDfrmTimCntTable,'pmo6006CntlineDfrmTimCntEntry':pmo6006CntlineDfrmTimCntEntry,_r:pmo6006CntlineDfrmTimCntIndex,'pmo6006CntlineDfrmTimCntValuePortn':pmo6006CntlineDfrmTimCntValuePortn,'pmo6006CntlineDfrmTimCntErrorPortn':pmo6006CntlineDfrmTimCntErrorPortn,'pmo6006CntlineDfrmTimCntOverloadPortn':pmo6006CntlineDfrmTimCntOverloadPortn,'pmo6006CntCountersReset':pmo6006CntCountersReset,'pmo6006CntCountersStop':pmo6006CntCountersStop,'pmo6006controlsWrite':pmo6006controlsWrite,'pmo6006CtrlOther':pmo6006CtrlOther,'pmo6006CtrlconfMgnt1':pmo6006CtrlconfMgnt1,'pmo6006CtrlConf1Load1':pmo6006CtrlConf1Load1,'pmo6006CtrlConf2Load1':pmo6006CtrlConf2Load1,'pmo6006CtrlConf2Flash1':pmo6006CtrlConf2Flash1,'pmo6006CtrlConf2Clear1':pmo6006CtrlConf2Clear1,'pmo6006Ctrlsynth4':pmo6006Ctrlsynth4,'pmo6006CtrlCorrelatOn':pmo6006CtrlCorrelatOn,'pmo6006CtrlCorrelatOff':pmo6006CtrlCorrelatOff,'pmo6006CtrlswMgnt':pmo6006CtrlswMgnt,'pmo6006CtrlColdReset':pmo6006CtrlColdReset,'pmo6006CtrlWarmReset':pmo6006CtrlWarmReset,'pmo6006CtrlLoadSwBank1':pmo6006CtrlLoadSwBank1,'pmo6006CtrlLoadSwBank2':pmo6006CtrlLoadSwBank2,'pmo6006CtrlgwMgnt':pmo6006CtrlgwMgnt,'pmo6006CtrlCurrentGwReset':pmo6006CtrlCurrentGwReset,'pmo6006CtrlLoadGwBank1':pmo6006CtrlLoadGwBank1,'pmo6006CtrlLoadGwBank2':pmo6006CtrlLoadGwBank2,'pmo6006CtrlLoadGwBank3':pmo6006CtrlLoadGwBank3,'pmo6006CtrlLoadGwBank4':pmo6006CtrlLoadGwBank4,'pmo6006CtrlledTest':pmo6006CtrlledTest,'pmo6006CtrlGreenLed':pmo6006CtrlGreenLed,'pmo6006CtrlRedLed':pmo6006CtrlRedLed,'pmo6006CtrlLedOff':pmo6006CtrlLedOff,'pmo6006CtrlClient':pmo6006CtrlClient,'pmo6006CtrlaccessLoopTable':pmo6006CtrlaccessLoopTable,'pmo6006CtrlaccessLoopEntry':pmo6006CtrlaccessLoopEntry,_s:pmo6006CtrlaccessLoopIndex,'pmo6006CtrlaccessLoopPortn':pmo6006CtrlaccessLoopPortn,'pmo6006CtrlclientLoopToLineTable':pmo6006CtrlclientLoopToLineTable,'pmo6006CtrlclientLoopToLineEntry':pmo6006CtrlclientLoopToLineEntry,_t:pmo6006CtrlclientLoopToLineIndex,'pmo6006CtrlclientLoopToLinePortn':pmo6006CtrlclientLoopToLinePortn,'pmo6006CtrlcsfUpInsTable':pmo6006CtrlcsfUpInsTable,'pmo6006CtrlcsfUpInsEntry':pmo6006CtrlcsfUpInsEntry,_u:pmo6006CtrlcsfUpInsIndex,'pmo6006CtrlcsfUpInsPortn':pmo6006CtrlcsfUpInsPortn,'pmo6006CtrlcaisDwInsTable':pmo6006CtrlcaisDwInsTable,'pmo6006CtrlcaisDwInsEntry':pmo6006CtrlcaisDwInsEntry,_v:pmo6006CtrlcaisDwInsIndex,'pmo6006CtrlcaisDwInsPortn':pmo6006CtrlcaisDwInsPortn,'pmo6006CtrlclientOciTable':pmo6006CtrlclientOciTable,'pmo6006CtrlclientOciEntry':pmo6006CtrlclientOciEntry,_w:pmo6006CtrlclientOciIndex,'pmo6006CtrlclientOciPortn':pmo6006CtrlclientOciPortn,'pmo6006CtrlclientLckTable':pmo6006CtrlclientLckTable,'pmo6006CtrlclientLckEntry':pmo6006CtrlclientLckEntry,_x:pmo6006CtrlclientLckIndex,'pmo6006CtrlclientLckPortn':pmo6006CtrlclientLckPortn,'pmo6006CtrlclientAisTable':pmo6006CtrlclientAisTable,'pmo6006CtrlclientAisEntry':pmo6006CtrlclientAisEntry,_y:pmo6006CtrlclientAisIndex,'pmo6006CtrlclientAisPortn':pmo6006CtrlclientAisPortn,'pmo6006CtrlclientBdiTable':pmo6006CtrlclientBdiTable,'pmo6006CtrlclientBdiEntry':pmo6006CtrlclientBdiEntry,_z:pmo6006CtrlclientBdiIndex,'pmo6006CtrlclientBdiPortn':pmo6006CtrlclientBdiPortn,'pmo6006CtrlLine':pmo6006CtrlLine,'pmo6006CtrlcommAccessLoopTable':pmo6006CtrlcommAccessLoopTable,'pmo6006CtrlcommAccessLoopEntry':pmo6006CtrlcommAccessLoopEntry,_A0:pmo6006CtrlcommAccessLoopIndex,'pmo6006CtrlcommAccessLoopPortn':pmo6006CtrlcommAccessLoopPortn,'pmo6006CtrllineLoopTable':pmo6006CtrllineLoopTable,'pmo6006CtrllineLoopEntry':pmo6006CtrllineLoopEntry,_A1:pmo6006CtrllineLoopIndex,'pmo6006CtrllineLoopPortn':pmo6006CtrllineLoopPortn,'pmo6006CtrlfecDisableTable':pmo6006CtrlfecDisableTable,'pmo6006CtrlfecDisableEntry':pmo6006CtrlfecDisableEntry,_A2:pmo6006CtrlfecDisableIndex,'pmo6006CtrlfecDisablePortn':pmo6006CtrlfecDisablePortn,'pmo6006CtrllineBdiTable':pmo6006CtrllineBdiTable,'pmo6006CtrllineBdiEntry':pmo6006CtrllineBdiEntry,_A3:pmo6006CtrllineBdiIndex,'pmo6006CtrllineBdiPortn':pmo6006CtrllineBdiPortn,'pmo6006ri':pmo6006ri,'pmo6006riTable':pmo6006riTable,'pmo6006RinvSfpTable':pmo6006RinvSfpTable,'pmo6006RinvSfpEntry':pmo6006RinvSfpEntry,_A4:pmo6006RinvSfpIndex,'pmo6006Rinvsfp':pmo6006Rinvsfp,'pmo6006RinvLineTable':pmo6006RinvLineTable,'pmo6006RinvLineEntry':pmo6006RinvLineEntry,_A5:pmo6006RinvLineIndex,'pmo6006RinvxfpLine':pmo6006RinvxfpLine,'pmo6006RinvReloadInventory':pmo6006RinvReloadInventory,'pmo6006RinvHwPlatform':pmo6006RinvHwPlatform,'pmo6006RinvModulePlatform':pmo6006RinvModulePlatform,'pmo6006RinvSwPlatform':pmo6006RinvSwPlatform,'pmo6006RinvGwPlatform':pmo6006RinvGwPlatform,'pmo6006download':pmo6006download,'pmo6006DwlOther':pmo6006DwlOther,'pmo6006DwlrestartProcess':pmo6006DwlrestartProcess,'pmo6006DwlWarmRestartProcessed':pmo6006DwlWarmRestartProcessed,'pmo6006DwlColdRestartProcessed':pmo6006DwlColdRestartProcessed,'pmo6006DwlswBanksUsed':pmo6006DwlswBanksUsed,'pmo6006DwlSwBank1Used':pmo6006DwlSwBank1Used,'pmo6006DwlSwBank2Used':pmo6006DwlSwBank2Used,'pmo6006DwlSwBank1Notempty':pmo6006DwlSwBank1Notempty,'pmo6006DwlSwBank2Notempty':pmo6006DwlSwBank2Notempty,'pmo6006DwlgwBanksUsed':pmo6006DwlgwBanksUsed,'pmo6006DwlGwBank1Used':pmo6006DwlGwBank1Used,'pmo6006DwlGwBank2Used':pmo6006DwlGwBank2Used,'pmo6006DwlGwBank3Used':pmo6006DwlGwBank3Used,'pmo6006DwlGwBank4Used':pmo6006DwlGwBank4Used,'pmo6006DwlGwBank1Notempty':pmo6006DwlGwBank1Notempty,'pmo6006DwlGwBank2Notempty':pmo6006DwlGwBank2Notempty,'pmo6006DwlGwBank3Notempty':pmo6006DwlGwBank3Notempty,'pmo6006DwlGwBank4Notempty':pmo6006DwlGwBank4Notempty,'pmo6006DwlClient':pmo6006DwlClient,'pmo6006DwlLine':pmo6006DwlLine,'pmo6006Config':pmo6006Config,'pmo6006CfgStartup':pmo6006CfgStartup,'pmo6006CfgClientStartupTable':pmo6006CfgClientStartupTable,'pmo6006CfgClientStartupEntry':pmo6006CfgClientStartupEntry,_A6:pmo6006CfgClientStartupIndex,'pmo6006CfgSystConfPortPortn':pmo6006CfgSystConfPortPortn,'pmo6006CfgNetConfPortPortn':pmo6006CfgNetConfPortPortn,'pmo6006CfgOptionsPortPortn':pmo6006CfgOptionsPortPortn,'pmo6006CfgLinexr1StartupTable':pmo6006CfgLinexr1StartupTable,'pmo6006CfgLinexr1StartupEntry':pmo6006CfgLinexr1StartupEntry,_A7:pmo6006CfgLinexr1StartupIndex,'pmo6006CfgSystConfLinePortn':pmo6006CfgSystConfLinePortn,'pmo6006CfgOptionsLinePortn':pmo6006CfgOptionsLinePortn,'pmo6006CfgOtxtlhTable':pmo6006CfgOtxtlhTable,'pmo6006CfgOtxtlhEntry':pmo6006CfgOtxtlhEntry,_A8:pmo6006CfgOtxtlhIndex,'pmo6006CfgLineControlsPortn':pmo6006CfgLineControlsPortn,'pmo6006CfgLinePwrLaserPortn':pmo6006CfgLinePwrLaserPortn,'pmo6006CfgLineFCurrentPortn':pmo6006CfgLineFCurrentPortn,'pmo6006CfgLineGridCurrentPortn':pmo6006CfgLineGridCurrentPortn,'pmo6006CfgLineFoPortn':pmo6006CfgLineFoPortn,'pmo6006CfgLabels':pmo6006CfgLabels,'pmo6006CfgLabelclientTable':pmo6006CfgLabelclientTable,'pmo6006CfgLabelclientEntry':pmo6006CfgLabelclientEntry,_A9:pmo6006CfgLabelclientIndex,'pmo6006CfgLabelclientPortn':pmo6006CfgLabelclientPortn,'pmo6006CfgLabellineTable':pmo6006CfgLabellineTable,'pmo6006CfgLabellineEntry':pmo6006CfgLabellineEntry,_AA:pmo6006CfgLabellineIndex,'pmo6006CfgLabellinePortn':pmo6006CfgLabellinePortn,'pmo6006CfgOther':pmo6006CfgOther,'pmo6006tablemoduleOther':pmo6006tablemoduleOther,'pmo6006Cfgmode':pmo6006Cfgmode,'pmo6006CfgOdu2Clienta':pmo6006CfgOdu2Clienta,'pmo6006CfgClientStartupOduTable':pmo6006CfgClientStartupOduTable,'pmo6006CfgClientStartupOduEntry':pmo6006CfgClientStartupOduEntry,_AB:pmo6006CfgClientStartupOduIndex,'pmo6006CfgOdu2ReserveLsbPortn':pmo6006CfgOdu2ReserveLsbPortn,'pmo6006CfgOdu2DegthresholdPortn':pmo6006CfgOdu2DegthresholdPortn,'pmo6006CfgOdu2DegmPortn':pmo6006CfgOdu2DegmPortn,'pmo6006CfgOdu2SettingsPortn':pmo6006CfgOdu2SettingsPortn,'pmo6006CfgOtu2Line':pmo6006CfgOtu2Line,'pmo6006CfgLinexStartupOtuTable':pmo6006CfgLinexStartupOtuTable,'pmo6006CfgLinexStartupOtuEntry':pmo6006CfgLinexStartupOtuEntry,_AC:pmo6006CfgLinexStartupOtuIndex,'pmo6006CfgOtu2ReserveMsbPortn':pmo6006CfgOtu2ReserveMsbPortn,'pmo6006CfgOtu2DegthresholdPortn':pmo6006CfgOtu2DegthresholdPortn,'pmo6006CfgOtu2DegmPortn':pmo6006CfgOtu2DegmPortn,'pmo6006CfgOtu2SettingsPortn':pmo6006CfgOtu2SettingsPortn,'pmo6006CfgSapiTxClient':pmo6006CfgSapiTxClient,'pmo6006CfgClientSapiTxOduTable':pmo6006CfgClientSapiTxOduTable,'pmo6006CfgClientSapiTxOduEntry':pmo6006CfgClientSapiTxOduEntry,_AD:pmo6006CfgClientSapiTxOduIndex,'pmo6006CfgClientSapiTxSetupPortn':pmo6006CfgClientSapiTxSetupPortn,'pmo6006CfgSapiExpClient':pmo6006CfgSapiExpClient,'pmo6006CfgClientSapiExpOduTable':pmo6006CfgClientSapiExpOduTable,'pmo6006CfgClientSapiExpOduEntry':pmo6006CfgClientSapiExpOduEntry,_AE:pmo6006CfgClientSapiExpOduIndex,'pmo6006CfgClientSapiExpSetupPortn':pmo6006CfgClientSapiExpSetupPortn,'pmo6006CfgSapiAccClient':pmo6006CfgSapiAccClient,'pmo6006CfgClientSapiAccOduTable':pmo6006CfgClientSapiAccOduTable,'pmo6006CfgClientSapiAccOduEntry':pmo6006CfgClientSapiAccOduEntry,_AF:pmo6006CfgClientSapiAccOduIndex,'pmo6006CfgClientSapiAccSetupPortn':pmo6006CfgClientSapiAccSetupPortn,'pmo6006CfgDapiTxClient':pmo6006CfgDapiTxClient,'pmo6006CfgClientDapiTxOduTable':pmo6006CfgClientDapiTxOduTable,'pmo6006CfgClientDapiTxOduEntry':pmo6006CfgClientDapiTxOduEntry,_AG:pmo6006CfgClientDapiTxOduIndex,'pmo6006CfgClientDapiTxSetupPortn':pmo6006CfgClientDapiTxSetupPortn,'pmo6006CfgDapiExpClient':pmo6006CfgDapiExpClient,'pmo6006CfgClientDapiExpOduTable':pmo6006CfgClientDapiExpOduTable,'pmo6006CfgClientDapiExpOduEntry':pmo6006CfgClientDapiExpOduEntry,_AH:pmo6006CfgClientDapiExpOduIndex,'pmo6006CfgClientDapiExpSetupPortn':pmo6006CfgClientDapiExpSetupPortn,'pmo6006CfgDapiAccClient':pmo6006CfgDapiAccClient,'pmo6006CfgClientDapiAccOduTable':pmo6006CfgClientDapiAccOduTable,'pmo6006CfgClientDapiAccOduEntry':pmo6006CfgClientDapiAccOduEntry,_AI:pmo6006CfgClientDapiAccOduIndex,'pmo6006CfgClientDapiAccSetupPortn':pmo6006CfgClientDapiAccSetupPortn,'pmo6006CfgSapiTxLine':pmo6006CfgSapiTxLine,'pmo6006CfgLineSapiTxOtuTable':pmo6006CfgLineSapiTxOtuTable,'pmo6006CfgLineSapiTxOtuEntry':pmo6006CfgLineSapiTxOtuEntry,_AJ:pmo6006CfgLineSapiTxOtuIndex,'pmo6006CfgLineSapiTxSetupPortn':pmo6006CfgLineSapiTxSetupPortn,'pmo6006CfgSapiExpLine':pmo6006CfgSapiExpLine,'pmo6006CfgLineSapiExpOtuTable':pmo6006CfgLineSapiExpOtuTable,'pmo6006CfgLineSapiExpOtuEntry':pmo6006CfgLineSapiExpOtuEntry,_AK:pmo6006CfgLineSapiExpOtuIndex,'pmo6006CfgLineSapiExpSetupPortn':pmo6006CfgLineSapiExpSetupPortn,'pmo6006CfgSapiAccLine':pmo6006CfgSapiAccLine,'pmo6006CfgLineSapiAccOtuTable':pmo6006CfgLineSapiAccOtuTable,'pmo6006CfgLineSapiAccOtuEntry':pmo6006CfgLineSapiAccOtuEntry,_AL:pmo6006CfgLineSapiAccOtuIndex,'pmo6006CfgLineSapiAccSetupPortn':pmo6006CfgLineSapiAccSetupPortn,'pmo6006CfgDapiTxLine':pmo6006CfgDapiTxLine,'pmo6006CfgLineDapiTxOtuTable':pmo6006CfgLineDapiTxOtuTable,'pmo6006CfgLineDapiTxOtuEntry':pmo6006CfgLineDapiTxOtuEntry,_AM:pmo6006CfgLineDapiTxOtuIndex,'pmo6006CfgLineDapiTxSetupPortn':pmo6006CfgLineDapiTxSetupPortn,'pmo6006CfgDapiExpLine':pmo6006CfgDapiExpLine,'pmo6006CfgLineDapiExpOtuTable':pmo6006CfgLineDapiExpOtuTable,'pmo6006CfgLineDapiExpOtuEntry':pmo6006CfgLineDapiExpOtuEntry,_AN:pmo6006CfgLineDapiExpOtuIndex,'pmo6006CfgLineDapiExpSetupPortn':pmo6006CfgLineDapiExpSetupPortn,'pmo6006CfgDapiAccLine':pmo6006CfgDapiAccLine,'pmo6006CfgLineDapiAccOtuTable':pmo6006CfgLineDapiAccOtuTable,'pmo6006CfgLineDapiAccOtuEntry':pmo6006CfgLineDapiAccOtuEntry,_AO:pmo6006CfgLineDapiAccOtuIndex,'pmo6006CfgLineDapiAccSetupPortn':pmo6006CfgLineDapiAccSetupPortn,'pmo6006CfgStartuptablefive':pmo6006CfgStartuptablefive,'pmo6006CfgOtxtlhcapabilitiesTable':pmo6006CfgOtxtlhcapabilitiesTable,'pmo6006CfgOtxtlhcapabilitiesEntry':pmo6006CfgOtxtlhcapabilitiesEntry,_AP:pmo6006CfgOtxtlhcapabilitiesIndex,'pmo6006CfgComponentTypePortn':pmo6006CfgComponentTypePortn,'pmo6006CfgMiscellaneousPortn':pmo6006CfgMiscellaneousPortn,'pmo6006CfgFirstChannelPortn':pmo6006CfgFirstChannelPortn,'pmo6006CfgLastChannelPortn':pmo6006CfgLastChannelPortn,'pmo6006CfgGridPortn':pmo6006CfgGridPortn,'pmo6006CfgWriteConfiguration':pmo6006CfgWriteConfiguration,'pmo6006traps':pmo6006traps,_J:pmo6006trapPortNumber,_I:pmo6006trapLineNumber,_H:pmo6006trapBoardNumber,'pmo6006LineTrapNotUrgentGoesOn':pmo6006LineTrapNotUrgentGoesOn,'pmo6006LineTrapNotUrgentGoesOff':pmo6006LineTrapNotUrgentGoesOff,'pmo6006LineTrapUrgentGoesOn':pmo6006LineTrapUrgentGoesOn,'pmo6006LineTrapUrgentGoesOff':pmo6006LineTrapUrgentGoesOff,'pmo6006LineTrapCritGoesOn':pmo6006LineTrapCritGoesOn,'pmo6006LineTrapCritGoesOff':pmo6006LineTrapCritGoesOff,'pmo6006ClientTrapNotUrgentGoesOn':pmo6006ClientTrapNotUrgentGoesOn,'pmo6006ClientTrapNotUrgentGoesOff':pmo6006ClientTrapNotUrgentGoesOff,'pmo6006ClientTrapUrgentGoesOn':pmo6006ClientTrapUrgentGoesOn,'pmo6006ClientTrapUrgentGoesOff':pmo6006ClientTrapUrgentGoesOff,'pmo6006ClientTrapCritGoesOn':pmo6006ClientTrapCritGoesOn,'pmo6006ClientTrapCritGoesOff':pmo6006ClientTrapCritGoesOff,'pmo6006PowerTrapUrgentGoesOn':pmo6006PowerTrapUrgentGoesOn,'pmo6006PowerTrapUrgentGoesOff':pmo6006PowerTrapUrgentGoesOff,'pmo6006Monitoring':pmo6006Monitoring,'pmo6006MonOther':pmo6006MonOther,'pmo6006MonRmon':pmo6006MonRmon,'pmo6006MonCountersReset':pmo6006MonCountersReset,'pmo6006MonCountersStop':pmo6006MonCountersStop,'pmo6006MonClient':pmo6006MonClient,'pmo6006MonClientRmonCounter':pmo6006MonClientRmonCounter,'pmo6006MonupRmonBytesCounterClientInputTable':pmo6006MonupRmonBytesCounterClientInputTable,'pmo6006MonupRmonBytesCounterClientInputEntry':pmo6006MonupRmonBytesCounterClientInputEntry,_AQ:pmo6006MonupRmonBytesCounterClientInputIndex,'pmo6006MonupRmonBytesCounterClientInputValuePortn':pmo6006MonupRmonBytesCounterClientInputValuePortn,'pmo6006MonupRmonBytesCounterClientInputErrorPortn':pmo6006MonupRmonBytesCounterClientInputErrorPortn,'pmo6006MonupRmonBytesCounterClientInputOverloadPortn':pmo6006MonupRmonBytesCounterClientInputOverloadPortn,'pmo6006MonupRmonCrcErrorsCounterClientInputTable':pmo6006MonupRmonCrcErrorsCounterClientInputTable,'pmo6006MonupRmonCrcErrorsCounterClientInputEntry':pmo6006MonupRmonCrcErrorsCounterClientInputEntry,_AR:pmo6006MonupRmonCrcErrorsCounterClientInputIndex,'pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn':pmo6006MonupRmonCrcErrorsCounterClientInputValuePortn,'pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn':pmo6006MonupRmonCrcErrorsCounterClientInputErrorPortn,'pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn':pmo6006MonupRmonCrcErrorsCounterClientInputOverloadPortn,'pmo6006MonupRmonPacketsCounterClientInputTable':pmo6006MonupRmonPacketsCounterClientInputTable,'pmo6006MonupRmonPacketsCounterClientInputEntry':pmo6006MonupRmonPacketsCounterClientInputEntry,_AS:pmo6006MonupRmonPacketsCounterClientInputIndex,'pmo6006MonupRmonPacketsCounterClientInputValuePortn':pmo6006MonupRmonPacketsCounterClientInputValuePortn,'pmo6006MonupRmonPacketsCounterClientInputErrorPortn':pmo6006MonupRmonPacketsCounterClientInputErrorPortn,'pmo6006MonupRmonPacketsCounterClientInputOverloadPortn':pmo6006MonupRmonPacketsCounterClientInputOverloadPortn,'pmo6006MonupRmonBroadcastCounterClientInputTable':pmo6006MonupRmonBroadcastCounterClientInputTable,'pmo6006MonupRmonBroadcastCounterClientInputEntry':pmo6006MonupRmonBroadcastCounterClientInputEntry,_AT:pmo6006MonupRmonBroadcastCounterClientInputIndex,'pmo6006MonupRmonBroadcastCounterClientInputValuePortn':pmo6006MonupRmonBroadcastCounterClientInputValuePortn,'pmo6006MonupRmonBroadcastCounterClientInputErrorPortn':pmo6006MonupRmonBroadcastCounterClientInputErrorPortn,'pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn':pmo6006MonupRmonBroadcastCounterClientInputOverloadPortn,'pmo6006MonupRmonMulticastCounterClientInputTable':pmo6006MonupRmonMulticastCounterClientInputTable,'pmo6006MonupRmonMulticastCounterClientInputEntry':pmo6006MonupRmonMulticastCounterClientInputEntry,_AU:pmo6006MonupRmonMulticastCounterClientInputIndex,'pmo6006MonupRmonMulticastCounterClientInputValuePortn':pmo6006MonupRmonMulticastCounterClientInputValuePortn,'pmo6006MonupRmonMulticastCounterClientInputErrorPortn':pmo6006MonupRmonMulticastCounterClientInputErrorPortn,'pmo6006MonupRmonMulticastCounterClientInputOverloadPortn':pmo6006MonupRmonMulticastCounterClientInputOverloadPortn,'pmo6006MonupRmonPauseFrameCounterClientInputTable':pmo6006MonupRmonPauseFrameCounterClientInputTable,'pmo6006MonupRmonPauseFrameCounterClientInputEntry':pmo6006MonupRmonPauseFrameCounterClientInputEntry,_AV:pmo6006MonupRmonPauseFrameCounterClientInputIndex,'pmo6006MonupRmonPauseFrameCounterClientInputValuePortn':pmo6006MonupRmonPauseFrameCounterClientInputValuePortn,'pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn':pmo6006MonupRmonPauseFrameCounterClientInputErrorPortn,'pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn':pmo6006MonupRmonPauseFrameCounterClientInputOverloadPortn,'pmo6006MondwRmonCrcErrorsCounterClientInputTable':pmo6006MondwRmonCrcErrorsCounterClientInputTable,'pmo6006MondwRmonCrcErrorsCounterClientInputEntry':pmo6006MondwRmonCrcErrorsCounterClientInputEntry,_AW:pmo6006MondwRmonCrcErrorsCounterClientInputIndex,'pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn':pmo6006MondwRmonCrcErrorsCounterClientInputValuePortn,'pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn':pmo6006MondwRmonCrcErrorsCounterClientInputErrorPortn,'pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn':pmo6006MondwRmonCrcErrorsCounterClientInputOverloadPortn,'pmo6006MondwRmonPacketsCounterClientInputTable':pmo6006MondwRmonPacketsCounterClientInputTable,'pmo6006MondwRmonPacketsCounterClientInputEntry':pmo6006MondwRmonPacketsCounterClientInputEntry,_AX:pmo6006MondwRmonPacketsCounterClientInputIndex,'pmo6006MondwRmonPacketsCounterClientInputValuePortn':pmo6006MondwRmonPacketsCounterClientInputValuePortn,'pmo6006MondwRmonPacketsCounterClientInputErrorPortn':pmo6006MondwRmonPacketsCounterClientInputErrorPortn,'pmo6006MondwRmonPacketsCounterClientInputOverloadPortn':pmo6006MondwRmonPacketsCounterClientInputOverloadPortn})