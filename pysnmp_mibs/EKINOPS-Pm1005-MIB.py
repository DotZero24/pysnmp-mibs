_Ae='pm1005MonupRmonMulticastCntIndex'
_Ad='pm1005MonupRmonBroadcastCntIndex'
_Ac='pm1005MonupRmonPacketsCntIndex'
_Ab='pm1005MonupRmonCrcErrorCntIndex'
_Aa='pm1005MonupRmonByteCntIndex'
_AZ='pm1005CfgOtxtlhcapabilitiesIndex'
_AY='pm1005CfgOtxtlhIndex'
_AX='pm1005CfgLabellineIndex'
_AW='pm1005CfgLabelclientIndex'
_AV='pm1005CfgXfpIndex'
_AU='pm1005CfgClientStartupIndex'
_AT='pm1005CfgClientcaiscsfIndex'
_AS='pm1005RinvLineIndex'
_AR='pm1005RinvSfpIndex'
_AQ='pm1005CtrllinePowerLaserIndex'
_AP='pm1005CtrllinePhotodiodeValueIndex'
_AO='pm1005CtrllinePhotodiodeModeIndex'
_AN='pm1005CtrllineTunableChannelIndex'
_AM='pm1005CtrlxfpXfiLoopIndex'
_AL='pm1005CtrlxfpLineLoopIndex'
_AK='pm1005CtrlxfpOnoffIndex'
_AJ='pm1005CtrllineOosModeIndex'
_AI='pm1005CtrlfecDisableIndex'
_AH='pm1005CtrlprotocolIndex'
_AG='pm1005CtrlclientAccessTermLoopIndex'
_AF='pm1005CtrlcaisDwInsIndex'
_AE='pm1005CtrlcsfUpInsIndex'
_AD='pm1005CtrlsfpOffCtrlIndex'
_AC='pm1005CtrlsfpOnCtrlIndex'
_AB='pm1005CtrlportOosModeIndex'
_AA='pm1005CtrlaccessLoopIndex'
_A9='pm1005CntdfrmPrimLineErrCntIndex'
_A8='pm1005CntdfrmTimCntIndex'
_A7='pm1005CntdfrmB1ErrCntIndex'
_A6='pm1005CntdwTimCntIndex'
_A5='pm1005CntdwCbipCntIndex'
_A4='pm1005CntupCvErrCntIndex'
_A3='pm1005CntupTimCntIndex'
_A2='pm1005CntupRdErrCntIndex'
_A1='pm1005CntupRaInsCntIndex'
_A0='pm1005CntupRaRemCntIndex'
_z='pm1005Mesrotx1LaserWvlengthIndex'
_y='pm1005Mesrotx1FreqDeviationIndex'
_x='pm1005Mesrotx1LaserTemperatureIndex'
_w='pm1005Mesrotx1AgingIndex'
_v='pm1005Mesrxfp1LxAux2MeasIndex'
_u='pm1005Mesrxfp1LxAux1MeasIndex'
_t='pm1005Mesrxfp1LiRxPowerMeasIndex'
_s='pm1005Mesrxfp1LoTxPowerMeasIndex'
_r='pm1005Mesrxfp1LoBiasCurrentMeasIndex'
_q='pm1005Mesrxfp1ReservedIndex'
_p='pm1005Mesrxfp1LxModTempMeasIndex'
_o='pm1005MesrrxpwrMeasIndex'
_n='pm1005MesrtxpwrMeasIndex'
_m='pm1005MesrbiasMeasIndex'
_l='pm1005MesrvoltMeasIndex'
_k='pm1005MesrtempMeasIndex'
_j='pm1005AlmlineXfp1AlarmsIndex'
_i='pm1005AlmlineSyncAlarmsIndex'
_h='pm1005AlmdfrmAlmIndex'
_g='pm1005AlmsynthAlmLineIndex'
_f='pm1005AlmlineOtx1TlhAlarmsIndex'
_e='pm1005AlmlineXfp1SupplyAlarmIndex'
_d='pm1005AlmlineXfp1AlarmIndex'
_c='pm1005AlmdfrmBerIndex'
_b='pm1005AlmlineOtx1TlhWarningsIndex'
_a='pm1005AlmlineXfp1WarningsIndex'
_Z='pm1005AlmmapperDeAlmIndex'
_Y='pm1005AlmaccessioAlmIndex'
_X='pm1005AlmsynthAlmPortIndex'
_W='pm1005AlmsfpAlmDdmIndex'
_V='pm1005AlmsfpWarnDdmIndex'
_U='pm1005AlmDefFuseA'
_T='pm1005AlmDefFuseB'
_S='pm1005AlmHwFailAccPortn'
_R='pm1005AlmFailAccPortn'
_Q='pm1005AlmSfpDdmAlmPortn'
_P='pm1005AlmSfpDdmWarningPortn'
_O='pm1005AlmLineHwFailPortn'
_N='pm1005AlmLineFailPortn'
_M='pm1005AlmLineDdmAlmPortn'
_L='pm1005AlmLineDdmWarningPortn'
_K='DisplayString'
_J='pm1005trapPortNumber'
_I='pm1005trapLineNumber'
_H='pm1005trapBoardNumber'
_G='deprecated'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='EKINOPS-Pm1005-MIB'
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
modulePm1005=ModuleIdentity((1,3,6,1,4,1,20044,26))
if mibBuilder.loadTexts:modulePm1005.setRevisions(('2007-06-12 00:00','2007-07-10 00:00','2007-09-17 00:00','2007-11-26 00:00','2008-10-21 00:00','2009-04-06 00:00','2009-04-09 00:00','2009-06-24 00:00','2010-02-17 00:00','2011-02-03 00:00','2012-07-03 00:00','2013-04-02 00:00','2014-03-25 00:00','2014-12-19 00:00','2016-05-19 00:00','2016-06-02 00:00'))
class Pm1005OtxMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('otx80mode',1),('otx60mode',2),('otxadjustmode',4)))
class Pm1005OtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pm1005AdjustValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('otxadjustvalue0',0),('otxadjustvalue1',1),('otxadjustvalue2',2),('otxadjustvalue3',3),('otxadjustvalue4',4),('otxadjustvalue5',5),('otxadjustvalue6',6),('otxadjustvalue7',7),('otxadjustvalue8',8),('otxadjustvalue9',9),('otxadjustvalue10',10)))
class Pm1005OtxChannel(TextualConvention,Integer32):status=_A
_Pm1005alarms_ObjectIdentity=ObjectIdentity
pm1005alarms=_Pm1005alarms_ObjectIdentity((1,3,6,1,4,1,20044,26,2))
_Pm1005AlmOther_ObjectIdentity=ObjectIdentity
pm1005AlmOther=_Pm1005AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1))
_Pm1005AlmOtherNurg_ObjectIdentity=ObjectIdentity
pm1005AlmOtherNurg=_Pm1005AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,1))
_Pm1005AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm1005AlmsynthAlm2=_Pm1005AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,1,2))
_Pm1005AlmConfTableSave_Type=EkiOnOff
_Pm1005AlmConfTableSave_Object=MibScalar
pm1005AlmConfTableSave=_Pm1005AlmConfTableSave_Object((1,3,6,1,4,1,20044,26,2,1,1,2,1),_Pm1005AlmConfTableSave_Type())
pm1005AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmConfTableSave.setStatus(_A)
_Pm1005AlmInvUpload_Type=EkiOnOff
_Pm1005AlmInvUpload_Object=MibScalar
pm1005AlmInvUpload=_Pm1005AlmInvUpload_Object((1,3,6,1,4,1,20044,26,2,1,1,2,2),_Pm1005AlmInvUpload_Type())
pm1005AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmInvUpload.setStatus(_A)
_Pm1005AlmConfTableLoad_Type=EkiOnOff
_Pm1005AlmConfTableLoad_Object=MibScalar
pm1005AlmConfTableLoad=_Pm1005AlmConfTableLoad_Object((1,3,6,1,4,1,20044,26,2,1,1,2,3),_Pm1005AlmConfTableLoad_Type())
pm1005AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmConfTableLoad.setStatus(_A)
_Pm1005AlmCorrelatOff_Type=EkiOnOff
_Pm1005AlmCorrelatOff_Object=MibScalar
pm1005AlmCorrelatOff=_Pm1005AlmCorrelatOff_Object((1,3,6,1,4,1,20044,26,2,1,1,2,4),_Pm1005AlmCorrelatOff_Type())
pm1005AlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmCorrelatOff.setStatus(_A)
_Pm1005AlmMaintenanceOn_Type=EkiOnOff
_Pm1005AlmMaintenanceOn_Object=MibScalar
pm1005AlmMaintenanceOn=_Pm1005AlmMaintenanceOn_Object((1,3,6,1,4,1,20044,26,2,1,1,2,5),_Pm1005AlmMaintenanceOn_Type())
pm1005AlmMaintenanceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmMaintenanceOn.setStatus(_A)
_Pm1005AlmOtherUrg_ObjectIdentity=ObjectIdentity
pm1005AlmOtherUrg=_Pm1005AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,2))
_Pm1005AlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pm1005AlmmodInitFailLevel2=_Pm1005AlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,2,194))
_Pm1005AlmLedFail_Type=EkiOnOff
_Pm1005AlmLedFail_Object=MibScalar
pm1005AlmLedFail=_Pm1005AlmLedFail_Object((1,3,6,1,4,1,20044,26,2,1,2,194,1),_Pm1005AlmLedFail_Type())
pm1005AlmLedFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLedFail.setStatus(_A)
_Pm1005AlmNextColdBootForced_Type=EkiOnOff
_Pm1005AlmNextColdBootForced_Object=MibScalar
pm1005AlmNextColdBootForced=_Pm1005AlmNextColdBootForced_Object((1,3,6,1,4,1,20044,26,2,1,2,194,2),_Pm1005AlmNextColdBootForced_Type())
pm1005AlmNextColdBootForced.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmNextColdBootForced.setStatus(_A)
_Pm1005AlmBootUndone_Type=EkiOnOff
_Pm1005AlmBootUndone_Object=MibScalar
pm1005AlmBootUndone=_Pm1005AlmBootUndone_Object((1,3,6,1,4,1,20044,26,2,1,2,194,3),_Pm1005AlmBootUndone_Type())
pm1005AlmBootUndone.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmBootUndone.setStatus(_A)
_Pm1005AlmResetHwInitFail_Type=EkiOnOff
_Pm1005AlmResetHwInitFail_Object=MibScalar
pm1005AlmResetHwInitFail=_Pm1005AlmResetHwInitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,194,4),_Pm1005AlmResetHwInitFail_Type())
pm1005AlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmResetHwInitFail.setStatus(_A)
_Pm1005AlmSwInitFail_Type=EkiOnOff
_Pm1005AlmSwInitFail_Object=MibScalar
pm1005AlmSwInitFail=_Pm1005AlmSwInitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,194,5),_Pm1005AlmSwInitFail_Type())
pm1005AlmSwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmSwInitFail.setStatus(_A)
_Pm1005AlmmodInitFailLevel3_ObjectIdentity=ObjectIdentity
pm1005AlmmodInitFailLevel3=_Pm1005AlmmodInitFailLevel3_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,2,195))
_Pm1005AlmGwIdentFail_Type=EkiOnOff
_Pm1005AlmGwIdentFail_Object=MibScalar
pm1005AlmGwIdentFail=_Pm1005AlmGwIdentFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,1),_Pm1005AlmGwIdentFail_Type())
pm1005AlmGwIdentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmGwIdentFail.setStatus(_A)
_Pm1005AlmObmTypeReadFail_Type=EkiOnOff
_Pm1005AlmObmTypeReadFail_Object=MibScalar
pm1005AlmObmTypeReadFail=_Pm1005AlmObmTypeReadFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,2),_Pm1005AlmObmTypeReadFail_Type())
pm1005AlmObmTypeReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmObmTypeReadFail.setStatus(_A)
_Pm1005AlmInitModuleFail_Type=EkiOnOff
_Pm1005AlmInitModuleFail_Object=MibScalar
pm1005AlmInitModuleFail=_Pm1005AlmInitModuleFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,3),_Pm1005AlmInitModuleFail_Type())
pm1005AlmInitModuleFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmInitModuleFail.setStatus(_A)
_Pm1005AlmXfp1InitFail_Type=EkiOnOff
_Pm1005AlmXfp1InitFail_Object=MibScalar
pm1005AlmXfp1InitFail=_Pm1005AlmXfp1InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,5),_Pm1005AlmXfp1InitFail_Type())
pm1005AlmXfp1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmXfp1InitFail.setStatus(_A)
_Pm1005AlmXfp2InitFail_Type=EkiOnOff
_Pm1005AlmXfp2InitFail_Object=MibScalar
pm1005AlmXfp2InitFail=_Pm1005AlmXfp2InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,6),_Pm1005AlmXfp2InitFail_Type())
pm1005AlmXfp2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmXfp2InitFail.setStatus(_A)
_Pm1005AlmLine1InitFail_Type=EkiOnOff
_Pm1005AlmLine1InitFail_Object=MibScalar
pm1005AlmLine1InitFail=_Pm1005AlmLine1InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,7),_Pm1005AlmLine1InitFail_Type())
pm1005AlmLine1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLine1InitFail.setStatus(_A)
_Pm1005AlmLine2InitFail_Type=EkiOnOff
_Pm1005AlmLine2InitFail_Object=MibScalar
pm1005AlmLine2InitFail=_Pm1005AlmLine2InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,8),_Pm1005AlmLine2InitFail_Type())
pm1005AlmLine2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLine2InitFail.setStatus(_A)
_Pm1005AlmClient1InitFail_Type=EkiOnOff
_Pm1005AlmClient1InitFail_Object=MibScalar
pm1005AlmClient1InitFail=_Pm1005AlmClient1InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,9),_Pm1005AlmClient1InitFail_Type())
pm1005AlmClient1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient1InitFail.setStatus(_A)
_Pm1005AlmClient2InitFail_Type=EkiOnOff
_Pm1005AlmClient2InitFail_Object=MibScalar
pm1005AlmClient2InitFail=_Pm1005AlmClient2InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,10),_Pm1005AlmClient2InitFail_Type())
pm1005AlmClient2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient2InitFail.setStatus(_A)
_Pm1005AlmClient3InitFail_Type=EkiOnOff
_Pm1005AlmClient3InitFail_Object=MibScalar
pm1005AlmClient3InitFail=_Pm1005AlmClient3InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,11),_Pm1005AlmClient3InitFail_Type())
pm1005AlmClient3InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient3InitFail.setStatus(_A)
_Pm1005AlmClient4InitFail_Type=EkiOnOff
_Pm1005AlmClient4InitFail_Object=MibScalar
pm1005AlmClient4InitFail=_Pm1005AlmClient4InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,12),_Pm1005AlmClient4InitFail_Type())
pm1005AlmClient4InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient4InitFail.setStatus(_A)
_Pm1005AlmClient5InitFail_Type=EkiOnOff
_Pm1005AlmClient5InitFail_Object=MibScalar
pm1005AlmClient5InitFail=_Pm1005AlmClient5InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,13),_Pm1005AlmClient5InitFail_Type())
pm1005AlmClient5InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient5InitFail.setStatus(_A)
_Pm1005AlmClient6InitFail_Type=EkiOnOff
_Pm1005AlmClient6InitFail_Object=MibScalar
pm1005AlmClient6InitFail=_Pm1005AlmClient6InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,14),_Pm1005AlmClient6InitFail_Type())
pm1005AlmClient6InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient6InitFail.setStatus(_A)
_Pm1005AlmClient7InitFail_Type=EkiOnOff
_Pm1005AlmClient7InitFail_Object=MibScalar
pm1005AlmClient7InitFail=_Pm1005AlmClient7InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,15),_Pm1005AlmClient7InitFail_Type())
pm1005AlmClient7InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient7InitFail.setStatus(_A)
_Pm1005AlmClient8InitFail_Type=EkiOnOff
_Pm1005AlmClient8InitFail_Object=MibScalar
pm1005AlmClient8InitFail=_Pm1005AlmClient8InitFail_Object((1,3,6,1,4,1,20044,26,2,1,2,195,16),_Pm1005AlmClient8InitFail_Type())
pm1005AlmClient8InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClient8InitFail.setStatus(_A)
_Pm1005AlmOtherCrit_ObjectIdentity=ObjectIdentity
pm1005AlmOtherCrit=_Pm1005AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,3))
_Pm1005AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm1005AlmsynthAlm0=_Pm1005AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,26,2,1,3,0))
_Pm1005AlmModGlobFail_Type=EkiOnOff
_Pm1005AlmModGlobFail_Object=MibScalar
pm1005AlmModGlobFail=_Pm1005AlmModGlobFail_Object((1,3,6,1,4,1,20044,26,2,1,3,0,9),_Pm1005AlmModGlobFail_Type())
pm1005AlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmModGlobFail.setStatus(_A)
_Pm1005AlmDefFuseA_Type=EkiOnOff
_Pm1005AlmDefFuseA_Object=MibScalar
pm1005AlmDefFuseA=_Pm1005AlmDefFuseA_Object((1,3,6,1,4,1,20044,26,2,1,3,0,15),_Pm1005AlmDefFuseA_Type())
pm1005AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDefFuseA.setStatus(_A)
_Pm1005AlmDefFuseB_Type=EkiOnOff
_Pm1005AlmDefFuseB_Object=MibScalar
pm1005AlmDefFuseB=_Pm1005AlmDefFuseB_Object((1,3,6,1,4,1,20044,26,2,1,3,0,16),_Pm1005AlmDefFuseB_Type())
pm1005AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDefFuseB.setStatus(_A)
_Pm1005AlmClient_ObjectIdentity=ObjectIdentity
pm1005AlmClient=_Pm1005AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,26,2,2))
_Pm1005AlmClientNurg_ObjectIdentity=ObjectIdentity
pm1005AlmClientNurg=_Pm1005AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,26,2,2,1))
_Pm1005AlmsfpWarnDdmTable_Object=MibTable
pm1005AlmsfpWarnDdmTable=_Pm1005AlmsfpWarnDdmTable_Object((1,3,6,1,4,1,20044,26,2,2,1,48))
if mibBuilder.loadTexts:pm1005AlmsfpWarnDdmTable.setStatus(_A)
_Pm1005AlmsfpWarnDdmEntry_Object=MibTableRow
pm1005AlmsfpWarnDdmEntry=_Pm1005AlmsfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1))
pm1005AlmsfpWarnDdmEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pm1005AlmsfpWarnDdmEntry.setStatus(_A)
class _Pm1005AlmsfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmsfpWarnDdmIndex_Type.__name__=_D
_Pm1005AlmsfpWarnDdmIndex_Object=MibTableColumn
pm1005AlmsfpWarnDdmIndex=_Pm1005AlmsfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,1),_Pm1005AlmsfpWarnDdmIndex_Type())
pm1005AlmsfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmsfpWarnDdmIndex.setStatus(_A)
_Pm1005AlmTxPwLowWngPortn_Type=EkiOnOff
_Pm1005AlmTxPwLowWngPortn_Object=MibTableColumn
pm1005AlmTxPwLowWngPortn=_Pm1005AlmTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,2),_Pm1005AlmTxPwLowWngPortn_Type())
pm1005AlmTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPwLowWngPortn.setStatus(_A)
_Pm1005AlmTxPwrHighWngPortn_Type=EkiOnOff
_Pm1005AlmTxPwrHighWngPortn_Object=MibTableColumn
pm1005AlmTxPwrHighWngPortn=_Pm1005AlmTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,3),_Pm1005AlmTxPwrHighWngPortn_Type())
pm1005AlmTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPwrHighWngPortn.setStatus(_A)
_Pm1005AlmTxBiasLowWngPortn_Type=EkiOnOff
_Pm1005AlmTxBiasLowWngPortn_Object=MibTableColumn
pm1005AlmTxBiasLowWngPortn=_Pm1005AlmTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,4),_Pm1005AlmTxBiasLowWngPortn_Type())
pm1005AlmTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasLowWngPortn.setStatus(_A)
_Pm1005AlmTxBiasHighWngPortn_Type=EkiOnOff
_Pm1005AlmTxBiasHighWngPortn_Object=MibTableColumn
pm1005AlmTxBiasHighWngPortn=_Pm1005AlmTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,5),_Pm1005AlmTxBiasHighWngPortn_Type())
pm1005AlmTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasHighWngPortn.setStatus(_A)
_Pm1005AlmVccLowWngPortn_Type=EkiOnOff
_Pm1005AlmVccLowWngPortn_Object=MibTableColumn
pm1005AlmVccLowWngPortn=_Pm1005AlmVccLowWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,6),_Pm1005AlmVccLowWngPortn_Type())
pm1005AlmVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVccLowWngPortn.setStatus(_A)
_Pm1005AlmVccHighWngPortn_Type=EkiOnOff
_Pm1005AlmVccHighWngPortn_Object=MibTableColumn
pm1005AlmVccHighWngPortn=_Pm1005AlmVccHighWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,7),_Pm1005AlmVccHighWngPortn_Type())
pm1005AlmVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVccHighWngPortn.setStatus(_A)
_Pm1005AlmTempLowWngPortn_Type=EkiOnOff
_Pm1005AlmTempLowWngPortn_Object=MibTableColumn
pm1005AlmTempLowWngPortn=_Pm1005AlmTempLowWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,8),_Pm1005AlmTempLowWngPortn_Type())
pm1005AlmTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempLowWngPortn.setStatus(_A)
_Pm1005AlmTempHighWngPortn_Type=EkiOnOff
_Pm1005AlmTempHighWngPortn_Object=MibTableColumn
pm1005AlmTempHighWngPortn=_Pm1005AlmTempHighWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,9),_Pm1005AlmTempHighWngPortn_Type())
pm1005AlmTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempHighWngPortn.setStatus(_A)
_Pm1005AlmRxPwrLowWngPortn_Type=EkiOnOff
_Pm1005AlmRxPwrLowWngPortn_Object=MibTableColumn
pm1005AlmRxPwrLowWngPortn=_Pm1005AlmRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,16),_Pm1005AlmRxPwrLowWngPortn_Type())
pm1005AlmRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPwrLowWngPortn.setStatus(_A)
_Pm1005AlmRxPwrHighWngPortn_Type=EkiOnOff
_Pm1005AlmRxPwrHighWngPortn_Object=MibTableColumn
pm1005AlmRxPwrHighWngPortn=_Pm1005AlmRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,26,2,2,1,48,1,17),_Pm1005AlmRxPwrHighWngPortn_Type())
pm1005AlmRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPwrHighWngPortn.setStatus(_A)
_Pm1005AlmClientUrg_ObjectIdentity=ObjectIdentity
pm1005AlmClientUrg=_Pm1005AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,26,2,2,2))
_Pm1005AlmsfpAlmDdmTable_Object=MibTable
pm1005AlmsfpAlmDdmTable=_Pm1005AlmsfpAlmDdmTable_Object((1,3,6,1,4,1,20044,26,2,2,2,32))
if mibBuilder.loadTexts:pm1005AlmsfpAlmDdmTable.setStatus(_A)
_Pm1005AlmsfpAlmDdmEntry_Object=MibTableRow
pm1005AlmsfpAlmDdmEntry=_Pm1005AlmsfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1))
pm1005AlmsfpAlmDdmEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm1005AlmsfpAlmDdmEntry.setStatus(_A)
class _Pm1005AlmsfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmsfpAlmDdmIndex_Type.__name__=_D
_Pm1005AlmsfpAlmDdmIndex_Object=MibTableColumn
pm1005AlmsfpAlmDdmIndex=_Pm1005AlmsfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,1),_Pm1005AlmsfpAlmDdmIndex_Type())
pm1005AlmsfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmsfpAlmDdmIndex.setStatus(_A)
_Pm1005AlmTxPwrLowAlaPortn_Type=EkiOnOff
_Pm1005AlmTxPwrLowAlaPortn_Object=MibTableColumn
pm1005AlmTxPwrLowAlaPortn=_Pm1005AlmTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,2),_Pm1005AlmTxPwrLowAlaPortn_Type())
pm1005AlmTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPwrLowAlaPortn.setStatus(_A)
_Pm1005AlmTxPwrHighAlaPortn_Type=EkiOnOff
_Pm1005AlmTxPwrHighAlaPortn_Object=MibTableColumn
pm1005AlmTxPwrHighAlaPortn=_Pm1005AlmTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,3),_Pm1005AlmTxPwrHighAlaPortn_Type())
pm1005AlmTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPwrHighAlaPortn.setStatus(_A)
_Pm1005AlmTxBiasLowAlaPortn_Type=EkiOnOff
_Pm1005AlmTxBiasLowAlaPortn_Object=MibTableColumn
pm1005AlmTxBiasLowAlaPortn=_Pm1005AlmTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,4),_Pm1005AlmTxBiasLowAlaPortn_Type())
pm1005AlmTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasLowAlaPortn.setStatus(_A)
_Pm1005AlmTxBiasHighAlaPortn_Type=EkiOnOff
_Pm1005AlmTxBiasHighAlaPortn_Object=MibTableColumn
pm1005AlmTxBiasHighAlaPortn=_Pm1005AlmTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,5),_Pm1005AlmTxBiasHighAlaPortn_Type())
pm1005AlmTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasHighAlaPortn.setStatus(_A)
_Pm1005AlmVccLowAlaPortn_Type=EkiOnOff
_Pm1005AlmVccLowAlaPortn_Object=MibTableColumn
pm1005AlmVccLowAlaPortn=_Pm1005AlmVccLowAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,6),_Pm1005AlmVccLowAlaPortn_Type())
pm1005AlmVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVccLowAlaPortn.setStatus(_A)
_Pm1005AlmVccHighAlaPortn_Type=EkiOnOff
_Pm1005AlmVccHighAlaPortn_Object=MibTableColumn
pm1005AlmVccHighAlaPortn=_Pm1005AlmVccHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,7),_Pm1005AlmVccHighAlaPortn_Type())
pm1005AlmVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVccHighAlaPortn.setStatus(_A)
_Pm1005AlmTempLowAlaPortn_Type=EkiOnOff
_Pm1005AlmTempLowAlaPortn_Object=MibTableColumn
pm1005AlmTempLowAlaPortn=_Pm1005AlmTempLowAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,8),_Pm1005AlmTempLowAlaPortn_Type())
pm1005AlmTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempLowAlaPortn.setStatus(_A)
_Pm1005AlmTempHighAlaPortn_Type=EkiOnOff
_Pm1005AlmTempHighAlaPortn_Object=MibTableColumn
pm1005AlmTempHighAlaPortn=_Pm1005AlmTempHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,9),_Pm1005AlmTempHighAlaPortn_Type())
pm1005AlmTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempHighAlaPortn.setStatus(_A)
_Pm1005AlmRxPwrLowAlaPortn_Type=EkiOnOff
_Pm1005AlmRxPwrLowAlaPortn_Object=MibTableColumn
pm1005AlmRxPwrLowAlaPortn=_Pm1005AlmRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,16),_Pm1005AlmRxPwrLowAlaPortn_Type())
pm1005AlmRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPwrLowAlaPortn.setStatus(_A)
_Pm1005AlmRxPwrHighAlaPortn_Type=EkiOnOff
_Pm1005AlmRxPwrHighAlaPortn_Object=MibTableColumn
pm1005AlmRxPwrHighAlaPortn=_Pm1005AlmRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,2,2,32,1,17),_Pm1005AlmRxPwrHighAlaPortn_Type())
pm1005AlmRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPwrHighAlaPortn.setStatus(_A)
_Pm1005AlmClientCrit_ObjectIdentity=ObjectIdentity
pm1005AlmClientCrit=_Pm1005AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,26,2,2,3))
_Pm1005AlmsynthAlmPortTable_Object=MibTable
pm1005AlmsynthAlmPortTable=_Pm1005AlmsynthAlmPortTable_Object((1,3,6,1,4,1,20044,26,2,2,3,8))
if mibBuilder.loadTexts:pm1005AlmsynthAlmPortTable.setStatus(_A)
_Pm1005AlmsynthAlmPortEntry_Object=MibTableRow
pm1005AlmsynthAlmPortEntry=_Pm1005AlmsynthAlmPortEntry_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1))
pm1005AlmsynthAlmPortEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm1005AlmsynthAlmPortEntry.setStatus(_A)
class _Pm1005AlmsynthAlmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmsynthAlmPortIndex_Type.__name__=_D
_Pm1005AlmsynthAlmPortIndex_Object=MibTableColumn
pm1005AlmsynthAlmPortIndex=_Pm1005AlmsynthAlmPortIndex_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,1),_Pm1005AlmsynthAlmPortIndex_Type())
pm1005AlmsynthAlmPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmsynthAlmPortIndex.setStatus(_A)
_Pm1005AlmSfpAbsentPortn_Type=EkiOnOff
_Pm1005AlmSfpAbsentPortn_Object=MibTableColumn
pm1005AlmSfpAbsentPortn=_Pm1005AlmSfpAbsentPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,2),_Pm1005AlmSfpAbsentPortn_Type())
pm1005AlmSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmSfpAbsentPortn.setStatus(_A)
_Pm1005AlmDdmAbsentPortn_Type=EkiOnOff
_Pm1005AlmDdmAbsentPortn_Object=MibTableColumn
pm1005AlmDdmAbsentPortn=_Pm1005AlmDdmAbsentPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,3),_Pm1005AlmDdmAbsentPortn_Type())
pm1005AlmDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDdmAbsentPortn.setStatus(_A)
_Pm1005AlmHwFailAccPortn_Type=EkiOnOff
_Pm1005AlmHwFailAccPortn_Object=MibTableColumn
pm1005AlmHwFailAccPortn=_Pm1005AlmHwFailAccPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,5),_Pm1005AlmHwFailAccPortn_Type())
pm1005AlmHwFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmHwFailAccPortn.setStatus(_A)
_Pm1005AlmDwLsdPortn_Type=EkiOnOff
_Pm1005AlmDwLsdPortn_Object=MibTableColumn
pm1005AlmDwLsdPortn=_Pm1005AlmDwLsdPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,6),_Pm1005AlmDwLsdPortn_Type())
pm1005AlmDwLsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwLsdPortn.setStatus(_A)
_Pm1005AlmClientLocalOosPortn_Type=EkiOnOff
_Pm1005AlmClientLocalOosPortn_Object=MibTableColumn
pm1005AlmClientLocalOosPortn=_Pm1005AlmClientLocalOosPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,7),_Pm1005AlmClientLocalOosPortn_Type())
pm1005AlmClientLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClientLocalOosPortn.setStatus(_A)
_Pm1005AlmClientRemoteOosPortn_Type=EkiOnOff
_Pm1005AlmClientRemoteOosPortn_Object=MibTableColumn
pm1005AlmClientRemoteOosPortn=_Pm1005AlmClientRemoteOosPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,8),_Pm1005AlmClientRemoteOosPortn_Type())
pm1005AlmClientRemoteOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmClientRemoteOosPortn.setStatus(_A)
_Pm1005AlmDwCaisPortn_Type=EkiOnOff
_Pm1005AlmDwCaisPortn_Object=MibTableColumn
pm1005AlmDwCaisPortn=_Pm1005AlmDwCaisPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,9),_Pm1005AlmDwCaisPortn_Type())
pm1005AlmDwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwCaisPortn.setStatus(_A)
_Pm1005AlmSfpDdmWarningPortn_Type=EkiOnOff
_Pm1005AlmSfpDdmWarningPortn_Object=MibTableColumn
pm1005AlmSfpDdmWarningPortn=_Pm1005AlmSfpDdmWarningPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,10),_Pm1005AlmSfpDdmWarningPortn_Type())
pm1005AlmSfpDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmSfpDdmWarningPortn.setStatus(_A)
_Pm1005AlmSfpDdmAlmPortn_Type=EkiOnOff
_Pm1005AlmSfpDdmAlmPortn_Object=MibTableColumn
pm1005AlmSfpDdmAlmPortn=_Pm1005AlmSfpDdmAlmPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,11),_Pm1005AlmSfpDdmAlmPortn_Type())
pm1005AlmSfpDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmSfpDdmAlmPortn.setStatus(_A)
_Pm1005AlmFailAccPortn_Type=EkiOnOff
_Pm1005AlmFailAccPortn_Object=MibTableColumn
pm1005AlmFailAccPortn=_Pm1005AlmFailAccPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,13),_Pm1005AlmFailAccPortn_Type())
pm1005AlmFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmFailAccPortn.setStatus(_A)
_Pm1005AlmUpCsfPortn_Type=EkiOnOff
_Pm1005AlmUpCsfPortn_Object=MibTableColumn
pm1005AlmUpCsfPortn=_Pm1005AlmUpCsfPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,8,1,17),_Pm1005AlmUpCsfPortn_Type())
pm1005AlmUpCsfPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmUpCsfPortn.setStatus(_A)
_Pm1005AlmaccessioAlmTable_Object=MibTable
pm1005AlmaccessioAlmTable=_Pm1005AlmaccessioAlmTable_Object((1,3,6,1,4,1,20044,26,2,2,3,16))
if mibBuilder.loadTexts:pm1005AlmaccessioAlmTable.setStatus(_A)
_Pm1005AlmaccessioAlmEntry_Object=MibTableRow
pm1005AlmaccessioAlmEntry=_Pm1005AlmaccessioAlmEntry_Object((1,3,6,1,4,1,20044,26,2,2,3,16,1))
pm1005AlmaccessioAlmEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm1005AlmaccessioAlmEntry.setStatus(_A)
class _Pm1005AlmaccessioAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmaccessioAlmIndex_Type.__name__=_D
_Pm1005AlmaccessioAlmIndex_Object=MibTableColumn
pm1005AlmaccessioAlmIndex=_Pm1005AlmaccessioAlmIndex_Object((1,3,6,1,4,1,20044,26,2,2,3,16,1,1),_Pm1005AlmaccessioAlmIndex_Type())
pm1005AlmaccessioAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmaccessioAlmIndex.setStatus(_A)
_Pm1005AlmDwLasFailPortn_Type=EkiOnOff
_Pm1005AlmDwLasFailPortn_Object=MibTableColumn
pm1005AlmDwLasFailPortn=_Pm1005AlmDwLasFailPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,16,1,2),_Pm1005AlmDwLasFailPortn_Type())
pm1005AlmDwLasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwLasFailPortn.setStatus(_A)
_Pm1005AlmUpLosPortn_Type=EkiOnOff
_Pm1005AlmUpLosPortn_Object=MibTableColumn
pm1005AlmUpLosPortn=_Pm1005AlmUpLosPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,16,1,5),_Pm1005AlmUpLosPortn_Type())
pm1005AlmUpLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmUpLosPortn.setStatus(_A)
_Pm1005AlmmapperDeAlmTable_Object=MibTable
pm1005AlmmapperDeAlmTable=_Pm1005AlmmapperDeAlmTable_Object((1,3,6,1,4,1,20044,26,2,2,3,72))
if mibBuilder.loadTexts:pm1005AlmmapperDeAlmTable.setStatus(_A)
_Pm1005AlmmapperDeAlmEntry_Object=MibTableRow
pm1005AlmmapperDeAlmEntry=_Pm1005AlmmapperDeAlmEntry_Object((1,3,6,1,4,1,20044,26,2,2,3,72,1))
pm1005AlmmapperDeAlmEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm1005AlmmapperDeAlmEntry.setStatus(_A)
class _Pm1005AlmmapperDeAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmmapperDeAlmIndex_Type.__name__=_D
_Pm1005AlmmapperDeAlmIndex_Object=MibTableColumn
pm1005AlmmapperDeAlmIndex=_Pm1005AlmmapperDeAlmIndex_Object((1,3,6,1,4,1,20044,26,2,2,3,72,1,1),_Pm1005AlmmapperDeAlmIndex_Type())
pm1005AlmmapperDeAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmmapperDeAlmIndex.setStatus(_A)
_Pm1005AlmUpAccOosPortn_Type=EkiOnOff
_Pm1005AlmUpAccOosPortn_Object=MibTableColumn
pm1005AlmUpAccOosPortn=_Pm1005AlmUpAccOosPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,72,1,2),_Pm1005AlmUpAccOosPortn_Type())
pm1005AlmUpAccOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmUpAccOosPortn.setStatus(_A)
_Pm1005AlmUpBufferOvlPortn_Type=EkiOnOff
_Pm1005AlmUpBufferOvlPortn_Object=MibTableColumn
pm1005AlmUpBufferOvlPortn=_Pm1005AlmUpBufferOvlPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,72,1,11),_Pm1005AlmUpBufferOvlPortn_Type())
pm1005AlmUpBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmUpBufferOvlPortn.setStatus(_A)
_Pm1005AlmDwCsfDetPortn_Type=EkiOnOff
_Pm1005AlmDwCsfDetPortn_Object=MibTableColumn
pm1005AlmDwCsfDetPortn=_Pm1005AlmDwCsfDetPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,72,1,12),_Pm1005AlmDwCsfDetPortn_Type())
pm1005AlmDwCsfDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwCsfDetPortn.setStatus(_A)
_Pm1005AlmDwBufferOvlPortn_Type=EkiOnOff
_Pm1005AlmDwBufferOvlPortn_Object=MibTableColumn
pm1005AlmDwBufferOvlPortn=_Pm1005AlmDwBufferOvlPortn_Object((1,3,6,1,4,1,20044,26,2,2,3,72,1,15),_Pm1005AlmDwBufferOvlPortn_Type())
pm1005AlmDwBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwBufferOvlPortn.setStatus(_A)
_Pm1005AlmLine_ObjectIdentity=ObjectIdentity
pm1005AlmLine=_Pm1005AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,26,2,3))
_Pm1005AlmLineNurg_ObjectIdentity=ObjectIdentity
pm1005AlmLineNurg=_Pm1005AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,26,2,3,1))
_Pm1005AlmlineXfp1WarningsTable_Object=MibTable
pm1005AlmlineXfp1WarningsTable=_Pm1005AlmlineXfp1WarningsTable_Object((1,3,6,1,4,1,20044,26,2,3,1,209))
if mibBuilder.loadTexts:pm1005AlmlineXfp1WarningsTable.setStatus(_A)
_Pm1005AlmlineXfp1WarningsEntry_Object=MibTableRow
pm1005AlmlineXfp1WarningsEntry=_Pm1005AlmlineXfp1WarningsEntry_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1))
pm1005AlmlineXfp1WarningsEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm1005AlmlineXfp1WarningsEntry.setStatus(_A)
class _Pm1005AlmlineXfp1WarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineXfp1WarningsIndex_Type.__name__=_D
_Pm1005AlmlineXfp1WarningsIndex_Object=MibTableColumn
pm1005AlmlineXfp1WarningsIndex=_Pm1005AlmlineXfp1WarningsIndex_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,1),_Pm1005AlmlineXfp1WarningsIndex_Type())
pm1005AlmlineXfp1WarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineXfp1WarningsIndex.setStatus(_A)
_Pm1005AlmTxPowerLowWarningPortn_Type=EkiOnOff
_Pm1005AlmTxPowerLowWarningPortn_Object=MibTableColumn
pm1005AlmTxPowerLowWarningPortn=_Pm1005AlmTxPowerLowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,2),_Pm1005AlmTxPowerLowWarningPortn_Type())
pm1005AlmTxPowerLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPowerLowWarningPortn.setStatus(_A)
_Pm1005AlmTxPowerHighWarningPortn_Type=EkiOnOff
_Pm1005AlmTxPowerHighWarningPortn_Object=MibTableColumn
pm1005AlmTxPowerHighWarningPortn=_Pm1005AlmTxPowerHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,3),_Pm1005AlmTxPowerHighWarningPortn_Type())
pm1005AlmTxPowerHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPowerHighWarningPortn.setStatus(_A)
_Pm1005AlmTxBiasLowWarningPortn_Type=EkiOnOff
_Pm1005AlmTxBiasLowWarningPortn_Object=MibTableColumn
pm1005AlmTxBiasLowWarningPortn=_Pm1005AlmTxBiasLowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,4),_Pm1005AlmTxBiasLowWarningPortn_Type())
pm1005AlmTxBiasLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasLowWarningPortn.setStatus(_A)
_Pm1005AlmTxBiasHighWarningPortn_Type=EkiOnOff
_Pm1005AlmTxBiasHighWarningPortn_Object=MibTableColumn
pm1005AlmTxBiasHighWarningPortn=_Pm1005AlmTxBiasHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,5),_Pm1005AlmTxBiasHighWarningPortn_Type())
pm1005AlmTxBiasHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasHighWarningPortn.setStatus(_A)
_Pm1005AlmTempLowWarningPortn_Type=EkiOnOff
_Pm1005AlmTempLowWarningPortn_Object=MibTableColumn
pm1005AlmTempLowWarningPortn=_Pm1005AlmTempLowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,8),_Pm1005AlmTempLowWarningPortn_Type())
pm1005AlmTempLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempLowWarningPortn.setStatus(_A)
_Pm1005AlmTempHighWarningPortn_Type=EkiOnOff
_Pm1005AlmTempHighWarningPortn_Object=MibTableColumn
pm1005AlmTempHighWarningPortn=_Pm1005AlmTempHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,9),_Pm1005AlmTempHighWarningPortn_Type())
pm1005AlmTempHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempHighWarningPortn.setStatus(_A)
_Pm1005AlmRxPowerLowWarningPortn_Type=EkiOnOff
_Pm1005AlmRxPowerLowWarningPortn_Object=MibTableColumn
pm1005AlmRxPowerLowWarningPortn=_Pm1005AlmRxPowerLowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,16),_Pm1005AlmRxPowerLowWarningPortn_Type())
pm1005AlmRxPowerLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPowerLowWarningPortn.setStatus(_A)
_Pm1005AlmRxPowerHighWarningPortn_Type=EkiOnOff
_Pm1005AlmRxPowerHighWarningPortn_Object=MibTableColumn
pm1005AlmRxPowerHighWarningPortn=_Pm1005AlmRxPowerHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,209,1,17),_Pm1005AlmRxPowerHighWarningPortn_Type())
pm1005AlmRxPowerHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPowerHighWarningPortn.setStatus(_A)
_Pm1005AlmlineOtx1TlhWarningsTable_Object=MibTable
pm1005AlmlineOtx1TlhWarningsTable=_Pm1005AlmlineOtx1TlhWarningsTable_Object((1,3,6,1,4,1,20044,26,2,3,1,225))
if mibBuilder.loadTexts:pm1005AlmlineOtx1TlhWarningsTable.setStatus(_A)
_Pm1005AlmlineOtx1TlhWarningsEntry_Object=MibTableRow
pm1005AlmlineOtx1TlhWarningsEntry=_Pm1005AlmlineOtx1TlhWarningsEntry_Object((1,3,6,1,4,1,20044,26,2,3,1,225,1))
pm1005AlmlineOtx1TlhWarningsEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm1005AlmlineOtx1TlhWarningsEntry.setStatus(_A)
class _Pm1005AlmlineOtx1TlhWarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineOtx1TlhWarningsIndex_Type.__name__=_D
_Pm1005AlmlineOtx1TlhWarningsIndex_Object=MibTableColumn
pm1005AlmlineOtx1TlhWarningsIndex=_Pm1005AlmlineOtx1TlhWarningsIndex_Object((1,3,6,1,4,1,20044,26,2,3,1,225,1,1),_Pm1005AlmlineOtx1TlhWarningsIndex_Type())
pm1005AlmlineOtx1TlhWarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineOtx1TlhWarningsIndex.setStatus(_A)
_Pm1005AlmLineModulatorAgingHighWarningPortn_Type=EkiOnOff
_Pm1005AlmLineModulatorAgingHighWarningPortn_Object=MibTableColumn
pm1005AlmLineModulatorAgingHighWarningPortn=_Pm1005AlmLineModulatorAgingHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,225,1,6),_Pm1005AlmLineModulatorAgingHighWarningPortn_Type())
pm1005AlmLineModulatorAgingHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineModulatorAgingHighWarningPortn.setStatus(_A)
_Pm1005AlmLineAgingHighWarningPortn_Type=EkiOnOff
_Pm1005AlmLineAgingHighWarningPortn_Object=MibTableColumn
pm1005AlmLineAgingHighWarningPortn=_Pm1005AlmLineAgingHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,225,1,7),_Pm1005AlmLineAgingHighWarningPortn_Type())
pm1005AlmLineAgingHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineAgingHighWarningPortn.setStatus(_A)
_Pm1005AlmLineFreqDevHighWarningPortn_Type=EkiOnOff
_Pm1005AlmLineFreqDevHighWarningPortn_Object=MibTableColumn
pm1005AlmLineFreqDevHighWarningPortn=_Pm1005AlmLineFreqDevHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,225,1,13),_Pm1005AlmLineFreqDevHighWarningPortn_Type())
pm1005AlmLineFreqDevHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineFreqDevHighWarningPortn.setStatus(_A)
_Pm1005AlmLineLaserTempHighWarningPortn_Type=EkiOnOff
_Pm1005AlmLineLaserTempHighWarningPortn_Object=MibTableColumn
pm1005AlmLineLaserTempHighWarningPortn=_Pm1005AlmLineLaserTempHighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,1,225,1,15),_Pm1005AlmLineLaserTempHighWarningPortn_Type())
pm1005AlmLineLaserTempHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineLaserTempHighWarningPortn.setStatus(_A)
_Pm1005AlmLineUrg_ObjectIdentity=ObjectIdentity
pm1005AlmLineUrg=_Pm1005AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,26,2,3,2))
_Pm1005AlmdfrmBerTable_Object=MibTable
pm1005AlmdfrmBerTable=_Pm1005AlmdfrmBerTable_Object((1,3,6,1,4,1,20044,26,2,3,2,129))
if mibBuilder.loadTexts:pm1005AlmdfrmBerTable.setStatus(_A)
_Pm1005AlmdfrmBerEntry_Object=MibTableRow
pm1005AlmdfrmBerEntry=_Pm1005AlmdfrmBerEntry_Object((1,3,6,1,4,1,20044,26,2,3,2,129,1))
pm1005AlmdfrmBerEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm1005AlmdfrmBerEntry.setStatus(_A)
class _Pm1005AlmdfrmBerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmdfrmBerIndex_Type.__name__=_D
_Pm1005AlmdfrmBerIndex_Object=MibTableColumn
pm1005AlmdfrmBerIndex=_Pm1005AlmdfrmBerIndex_Object((1,3,6,1,4,1,20044,26,2,3,2,129,1,1),_Pm1005AlmdfrmBerIndex_Type())
pm1005AlmdfrmBerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmdfrmBerIndex.setStatus(_A)
_Pm1005AlmLineSignalDegradePortn_Type=EkiOnOff
_Pm1005AlmLineSignalDegradePortn_Object=MibTableColumn
pm1005AlmLineSignalDegradePortn=_Pm1005AlmLineSignalDegradePortn_Object((1,3,6,1,4,1,20044,26,2,3,2,129,1,2),_Pm1005AlmLineSignalDegradePortn_Type())
pm1005AlmLineSignalDegradePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineSignalDegradePortn.setStatus(_A)
_Pm1005AlmLineSignalFailPortn_Type=EkiOnOff
_Pm1005AlmLineSignalFailPortn_Object=MibTableColumn
pm1005AlmLineSignalFailPortn=_Pm1005AlmLineSignalFailPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,129,1,3),_Pm1005AlmLineSignalFailPortn_Type())
pm1005AlmLineSignalFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineSignalFailPortn.setStatus(_A)
_Pm1005AlmLineDegradePortn_Type=EkiOnOff
_Pm1005AlmLineDegradePortn_Object=MibTableColumn
pm1005AlmLineDegradePortn=_Pm1005AlmLineDegradePortn_Object((1,3,6,1,4,1,20044,26,2,3,2,129,1,6),_Pm1005AlmLineDegradePortn_Type())
pm1005AlmLineDegradePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineDegradePortn.setStatus(_A)
_Pm1005AlmlineXfp1AlarmTable_Object=MibTable
pm1005AlmlineXfp1AlarmTable=_Pm1005AlmlineXfp1AlarmTable_Object((1,3,6,1,4,1,20044,26,2,3,2,208))
if mibBuilder.loadTexts:pm1005AlmlineXfp1AlarmTable.setStatus(_A)
_Pm1005AlmlineXfp1AlarmEntry_Object=MibTableRow
pm1005AlmlineXfp1AlarmEntry=_Pm1005AlmlineXfp1AlarmEntry_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1))
pm1005AlmlineXfp1AlarmEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm1005AlmlineXfp1AlarmEntry.setStatus(_A)
class _Pm1005AlmlineXfp1AlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineXfp1AlarmIndex_Type.__name__=_D
_Pm1005AlmlineXfp1AlarmIndex_Object=MibTableColumn
pm1005AlmlineXfp1AlarmIndex=_Pm1005AlmlineXfp1AlarmIndex_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,1),_Pm1005AlmlineXfp1AlarmIndex_Type())
pm1005AlmlineXfp1AlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineXfp1AlarmIndex.setStatus(_A)
_Pm1005AlmTxPowerLowAlarmPortn_Type=EkiOnOff
_Pm1005AlmTxPowerLowAlarmPortn_Object=MibTableColumn
pm1005AlmTxPowerLowAlarmPortn=_Pm1005AlmTxPowerLowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,2),_Pm1005AlmTxPowerLowAlarmPortn_Type())
pm1005AlmTxPowerLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPowerLowAlarmPortn.setStatus(_A)
_Pm1005AlmTxPowerHighAlarmPortn_Type=EkiOnOff
_Pm1005AlmTxPowerHighAlarmPortn_Object=MibTableColumn
pm1005AlmTxPowerHighAlarmPortn=_Pm1005AlmTxPowerHighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,3),_Pm1005AlmTxPowerHighAlarmPortn_Type())
pm1005AlmTxPowerHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxPowerHighAlarmPortn.setStatus(_A)
_Pm1005AlmTxBiasLowAlarmPortn_Type=EkiOnOff
_Pm1005AlmTxBiasLowAlarmPortn_Object=MibTableColumn
pm1005AlmTxBiasLowAlarmPortn=_Pm1005AlmTxBiasLowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,4),_Pm1005AlmTxBiasLowAlarmPortn_Type())
pm1005AlmTxBiasLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasLowAlarmPortn.setStatus(_A)
_Pm1005AlmTxBiasHighAlarmPortn_Type=EkiOnOff
_Pm1005AlmTxBiasHighAlarmPortn_Object=MibTableColumn
pm1005AlmTxBiasHighAlarmPortn=_Pm1005AlmTxBiasHighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,5),_Pm1005AlmTxBiasHighAlarmPortn_Type())
pm1005AlmTxBiasHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxBiasHighAlarmPortn.setStatus(_A)
_Pm1005AlmTempLowAlarmPortn_Type=EkiOnOff
_Pm1005AlmTempLowAlarmPortn_Object=MibTableColumn
pm1005AlmTempLowAlarmPortn=_Pm1005AlmTempLowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,8),_Pm1005AlmTempLowAlarmPortn_Type())
pm1005AlmTempLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempLowAlarmPortn.setStatus(_A)
_Pm1005AlmTempHighAlarmPortn_Type=EkiOnOff
_Pm1005AlmTempHighAlarmPortn_Object=MibTableColumn
pm1005AlmTempHighAlarmPortn=_Pm1005AlmTempHighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,9),_Pm1005AlmTempHighAlarmPortn_Type())
pm1005AlmTempHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTempHighAlarmPortn.setStatus(_A)
_Pm1005AlmRxPowerLowAlarmPortn_Type=EkiOnOff
_Pm1005AlmRxPowerLowAlarmPortn_Object=MibTableColumn
pm1005AlmRxPowerLowAlarmPortn=_Pm1005AlmRxPowerLowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,16),_Pm1005AlmRxPowerLowAlarmPortn_Type())
pm1005AlmRxPowerLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPowerLowAlarmPortn.setStatus(_A)
_Pm1005AlmRxPowerHighAlarmPortn_Type=EkiOnOff
_Pm1005AlmRxPowerHighAlarmPortn_Object=MibTableColumn
pm1005AlmRxPowerHighAlarmPortn=_Pm1005AlmRxPowerHighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,208,1,17),_Pm1005AlmRxPowerHighAlarmPortn_Type())
pm1005AlmRxPowerHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxPowerHighAlarmPortn.setStatus(_A)
_Pm1005AlmlineXfp1SupplyAlarmTable_Object=MibTable
pm1005AlmlineXfp1SupplyAlarmTable=_Pm1005AlmlineXfp1SupplyAlarmTable_Object((1,3,6,1,4,1,20044,26,2,3,2,212))
if mibBuilder.loadTexts:pm1005AlmlineXfp1SupplyAlarmTable.setStatus(_A)
_Pm1005AlmlineXfp1SupplyAlarmEntry_Object=MibTableRow
pm1005AlmlineXfp1SupplyAlarmEntry=_Pm1005AlmlineXfp1SupplyAlarmEntry_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1))
pm1005AlmlineXfp1SupplyAlarmEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm1005AlmlineXfp1SupplyAlarmEntry.setStatus(_A)
class _Pm1005AlmlineXfp1SupplyAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineXfp1SupplyAlarmIndex_Type.__name__=_D
_Pm1005AlmlineXfp1SupplyAlarmIndex_Object=MibTableColumn
pm1005AlmlineXfp1SupplyAlarmIndex=_Pm1005AlmlineXfp1SupplyAlarmIndex_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,1),_Pm1005AlmlineXfp1SupplyAlarmIndex_Type())
pm1005AlmlineXfp1SupplyAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineXfp1SupplyAlarmIndex.setStatus(_A)
_Pm1005AlmVee5LowAlarmPortn_Type=EkiOnOff
_Pm1005AlmVee5LowAlarmPortn_Object=MibTableColumn
pm1005AlmVee5LowAlarmPortn=_Pm1005AlmVee5LowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,2),_Pm1005AlmVee5LowAlarmPortn_Type())
pm1005AlmVee5LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVee5LowAlarmPortn.setStatus(_A)
_Pm1005AlmVee5HighAlarmPortn_Type=EkiOnOff
_Pm1005AlmVee5HighAlarmPortn_Object=MibTableColumn
pm1005AlmVee5HighAlarmPortn=_Pm1005AlmVee5HighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,3),_Pm1005AlmVee5HighAlarmPortn_Type())
pm1005AlmVee5HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVee5HighAlarmPortn.setStatus(_A)
_Pm1005AlmVcc2LowAlarmPortn_Type=EkiOnOff
_Pm1005AlmVcc2LowAlarmPortn_Object=MibTableColumn
pm1005AlmVcc2LowAlarmPortn=_Pm1005AlmVcc2LowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,4),_Pm1005AlmVcc2LowAlarmPortn_Type())
pm1005AlmVcc2LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc2LowAlarmPortn.setStatus(_A)
_Pm1005AlmVcc2HighAlarmPortn_Type=EkiOnOff
_Pm1005AlmVcc2HighAlarmPortn_Object=MibTableColumn
pm1005AlmVcc2HighAlarmPortn=_Pm1005AlmVcc2HighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,5),_Pm1005AlmVcc2HighAlarmPortn_Type())
pm1005AlmVcc2HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc2HighAlarmPortn.setStatus(_A)
_Pm1005AlmVcc3LowAlarmPortn_Type=EkiOnOff
_Pm1005AlmVcc3LowAlarmPortn_Object=MibTableColumn
pm1005AlmVcc3LowAlarmPortn=_Pm1005AlmVcc3LowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,6),_Pm1005AlmVcc3LowAlarmPortn_Type())
pm1005AlmVcc3LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc3LowAlarmPortn.setStatus(_A)
_Pm1005AlmVcc3HighAlarmPortn_Type=EkiOnOff
_Pm1005AlmVcc3HighAlarmPortn_Object=MibTableColumn
pm1005AlmVcc3HighAlarmPortn=_Pm1005AlmVcc3HighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,7),_Pm1005AlmVcc3HighAlarmPortn_Type())
pm1005AlmVcc3HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc3HighAlarmPortn.setStatus(_A)
_Pm1005AlmVcc5LowAlarmPortn_Type=EkiOnOff
_Pm1005AlmVcc5LowAlarmPortn_Object=MibTableColumn
pm1005AlmVcc5LowAlarmPortn=_Pm1005AlmVcc5LowAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,8),_Pm1005AlmVcc5LowAlarmPortn_Type())
pm1005AlmVcc5LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc5LowAlarmPortn.setStatus(_A)
_Pm1005AlmVcc5HighAlarmPortn_Type=EkiOnOff
_Pm1005AlmVcc5HighAlarmPortn_Object=MibTableColumn
pm1005AlmVcc5HighAlarmPortn=_Pm1005AlmVcc5HighAlarmPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,9),_Pm1005AlmVcc5HighAlarmPortn_Type())
pm1005AlmVcc5HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc5HighAlarmPortn.setStatus(_A)
_Pm1005AlmVee5LowWarningPortn_Type=EkiOnOff
_Pm1005AlmVee5LowWarningPortn_Object=MibTableColumn
pm1005AlmVee5LowWarningPortn=_Pm1005AlmVee5LowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,10),_Pm1005AlmVee5LowWarningPortn_Type())
pm1005AlmVee5LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVee5LowWarningPortn.setStatus(_A)
_Pm1005AlmVee5HighWarningPortn_Type=EkiOnOff
_Pm1005AlmVee5HighWarningPortn_Object=MibTableColumn
pm1005AlmVee5HighWarningPortn=_Pm1005AlmVee5HighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,11),_Pm1005AlmVee5HighWarningPortn_Type())
pm1005AlmVee5HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVee5HighWarningPortn.setStatus(_A)
_Pm1005AlmVcc2LowWarningPortn_Type=EkiOnOff
_Pm1005AlmVcc2LowWarningPortn_Object=MibTableColumn
pm1005AlmVcc2LowWarningPortn=_Pm1005AlmVcc2LowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,12),_Pm1005AlmVcc2LowWarningPortn_Type())
pm1005AlmVcc2LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc2LowWarningPortn.setStatus(_A)
_Pm1005AlmVcc2HighWarningPortn_Type=EkiOnOff
_Pm1005AlmVcc2HighWarningPortn_Object=MibTableColumn
pm1005AlmVcc2HighWarningPortn=_Pm1005AlmVcc2HighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,13),_Pm1005AlmVcc2HighWarningPortn_Type())
pm1005AlmVcc2HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc2HighWarningPortn.setStatus(_A)
_Pm1005AlmVcc3LowWarningPortn_Type=EkiOnOff
_Pm1005AlmVcc3LowWarningPortn_Object=MibTableColumn
pm1005AlmVcc3LowWarningPortn=_Pm1005AlmVcc3LowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,14),_Pm1005AlmVcc3LowWarningPortn_Type())
pm1005AlmVcc3LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc3LowWarningPortn.setStatus(_A)
_Pm1005AlmVcc3HighWarningPortn_Type=EkiOnOff
_Pm1005AlmVcc3HighWarningPortn_Object=MibTableColumn
pm1005AlmVcc3HighWarningPortn=_Pm1005AlmVcc3HighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,15),_Pm1005AlmVcc3HighWarningPortn_Type())
pm1005AlmVcc3HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc3HighWarningPortn.setStatus(_A)
_Pm1005AlmVcc5LowWarningPortn_Type=EkiOnOff
_Pm1005AlmVcc5LowWarningPortn_Object=MibTableColumn
pm1005AlmVcc5LowWarningPortn=_Pm1005AlmVcc5LowWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,16),_Pm1005AlmVcc5LowWarningPortn_Type())
pm1005AlmVcc5LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc5LowWarningPortn.setStatus(_A)
_Pm1005AlmVcc5HighWarningPortn_Type=EkiOnOff
_Pm1005AlmVcc5HighWarningPortn_Object=MibTableColumn
pm1005AlmVcc5HighWarningPortn=_Pm1005AlmVcc5HighWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,212,1,17),_Pm1005AlmVcc5HighWarningPortn_Type())
pm1005AlmVcc5HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmVcc5HighWarningPortn.setStatus(_A)
_Pm1005AlmlineOtx1TlhAlarmsTable_Object=MibTable
pm1005AlmlineOtx1TlhAlarmsTable=_Pm1005AlmlineOtx1TlhAlarmsTable_Object((1,3,6,1,4,1,20044,26,2,3,2,224))
if mibBuilder.loadTexts:pm1005AlmlineOtx1TlhAlarmsTable.setStatus(_A)
_Pm1005AlmlineOtx1TlhAlarmsEntry_Object=MibTableRow
pm1005AlmlineOtx1TlhAlarmsEntry=_Pm1005AlmlineOtx1TlhAlarmsEntry_Object((1,3,6,1,4,1,20044,26,2,3,2,224,1))
pm1005AlmlineOtx1TlhAlarmsEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm1005AlmlineOtx1TlhAlarmsEntry.setStatus(_A)
class _Pm1005AlmlineOtx1TlhAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineOtx1TlhAlarmsIndex_Type.__name__=_D
_Pm1005AlmlineOtx1TlhAlarmsIndex_Object=MibTableColumn
pm1005AlmlineOtx1TlhAlarmsIndex=_Pm1005AlmlineOtx1TlhAlarmsIndex_Object((1,3,6,1,4,1,20044,26,2,3,2,224,1,1),_Pm1005AlmlineOtx1TlhAlarmsIndex_Type())
pm1005AlmlineOtx1TlhAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineOtx1TlhAlarmsIndex.setStatus(_A)
_Pm1005AlmLineModulatorAgingHighAlaPortn_Type=EkiOnOff
_Pm1005AlmLineModulatorAgingHighAlaPortn_Object=MibTableColumn
pm1005AlmLineModulatorAgingHighAlaPortn=_Pm1005AlmLineModulatorAgingHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,224,1,6),_Pm1005AlmLineModulatorAgingHighAlaPortn_Type())
pm1005AlmLineModulatorAgingHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineModulatorAgingHighAlaPortn.setStatus(_A)
_Pm1005AlmLineAgingHighAlaPortn_Type=EkiOnOff
_Pm1005AlmLineAgingHighAlaPortn_Object=MibTableColumn
pm1005AlmLineAgingHighAlaPortn=_Pm1005AlmLineAgingHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,224,1,7),_Pm1005AlmLineAgingHighAlaPortn_Type())
pm1005AlmLineAgingHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineAgingHighAlaPortn.setStatus(_A)
_Pm1005AlmLineFreqDevHighAlaPortn_Type=EkiOnOff
_Pm1005AlmLineFreqDevHighAlaPortn_Object=MibTableColumn
pm1005AlmLineFreqDevHighAlaPortn=_Pm1005AlmLineFreqDevHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,224,1,13),_Pm1005AlmLineFreqDevHighAlaPortn_Type())
pm1005AlmLineFreqDevHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineFreqDevHighAlaPortn.setStatus(_A)
_Pm1005AlmLineLaserTempHighAlaPortn_Type=EkiOnOff
_Pm1005AlmLineLaserTempHighAlaPortn_Object=MibTableColumn
pm1005AlmLineLaserTempHighAlaPortn=_Pm1005AlmLineLaserTempHighAlaPortn_Object((1,3,6,1,4,1,20044,26,2,3,2,224,1,15),_Pm1005AlmLineLaserTempHighAlaPortn_Type())
pm1005AlmLineLaserTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineLaserTempHighAlaPortn.setStatus(_A)
_Pm1005AlmLineCrit_ObjectIdentity=ObjectIdentity
pm1005AlmLineCrit=_Pm1005AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,26,2,3,3))
_Pm1005AlmsynthAlmLineTable_Object=MibTable
pm1005AlmsynthAlmLineTable=_Pm1005AlmsynthAlmLineTable_Object((1,3,6,1,4,1,20044,26,2,3,3,7))
if mibBuilder.loadTexts:pm1005AlmsynthAlmLineTable.setStatus(_A)
_Pm1005AlmsynthAlmLineEntry_Object=MibTableRow
pm1005AlmsynthAlmLineEntry=_Pm1005AlmsynthAlmLineEntry_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1))
pm1005AlmsynthAlmLineEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm1005AlmsynthAlmLineEntry.setStatus(_A)
class _Pm1005AlmsynthAlmLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmsynthAlmLineIndex_Type.__name__=_D
_Pm1005AlmsynthAlmLineIndex_Object=MibTableColumn
pm1005AlmsynthAlmLineIndex=_Pm1005AlmsynthAlmLineIndex_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,1),_Pm1005AlmsynthAlmLineIndex_Type())
pm1005AlmsynthAlmLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmsynthAlmLineIndex.setStatus(_A)
_Pm1005AlmXfpAbsentPortn_Type=EkiOnOff
_Pm1005AlmXfpAbsentPortn_Object=MibTableColumn
pm1005AlmXfpAbsentPortn=_Pm1005AlmXfpAbsentPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,2),_Pm1005AlmXfpAbsentPortn_Type())
pm1005AlmXfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmXfpAbsentPortn.setStatus(_A)
_Pm1005AlmXfpInitNotComplPortn_Type=EkiOnOff
_Pm1005AlmXfpInitNotComplPortn_Object=MibTableColumn
pm1005AlmXfpInitNotComplPortn=_Pm1005AlmXfpInitNotComplPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,3),_Pm1005AlmXfpInitNotComplPortn_Type())
pm1005AlmXfpInitNotComplPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmXfpInitNotComplPortn.setStatus(_A)
_Pm1005AlmLineHwFailPortn_Type=EkiOnOff
_Pm1005AlmLineHwFailPortn_Object=MibTableColumn
pm1005AlmLineHwFailPortn=_Pm1005AlmLineHwFailPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,5),_Pm1005AlmLineHwFailPortn_Type())
pm1005AlmLineHwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineHwFailPortn.setStatus(_A)
_Pm1005AlmXfpTxOffPortn_Type=EkiOnOff
_Pm1005AlmXfpTxOffPortn_Object=MibTableColumn
pm1005AlmXfpTxOffPortn=_Pm1005AlmXfpTxOffPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,6),_Pm1005AlmXfpTxOffPortn_Type())
pm1005AlmXfpTxOffPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmXfpTxOffPortn.setStatus(_A)
_Pm1005AlmLineLocalOosPortn_Type=EkiOnOff
_Pm1005AlmLineLocalOosPortn_Object=MibTableColumn
pm1005AlmLineLocalOosPortn=_Pm1005AlmLineLocalOosPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,7),_Pm1005AlmLineLocalOosPortn_Type())
pm1005AlmLineLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineLocalOosPortn.setStatus(_A)
_Pm1005AlmUpRdiInsPortn_Type=EkiOnOff
_Pm1005AlmUpRdiInsPortn_Object=MibTableColumn
pm1005AlmUpRdiInsPortn=_Pm1005AlmUpRdiInsPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,9),_Pm1005AlmUpRdiInsPortn_Type())
pm1005AlmUpRdiInsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmUpRdiInsPortn.setStatus(_A)
_Pm1005AlmLineDdmWarningPortn_Type=EkiOnOff
_Pm1005AlmLineDdmWarningPortn_Object=MibTableColumn
pm1005AlmLineDdmWarningPortn=_Pm1005AlmLineDdmWarningPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,10),_Pm1005AlmLineDdmWarningPortn_Type())
pm1005AlmLineDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineDdmWarningPortn.setStatus(_A)
_Pm1005AlmLineDdmAlmPortn_Type=EkiOnOff
_Pm1005AlmLineDdmAlmPortn_Object=MibTableColumn
pm1005AlmLineDdmAlmPortn=_Pm1005AlmLineDdmAlmPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,11),_Pm1005AlmLineDdmAlmPortn_Type())
pm1005AlmLineDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineDdmAlmPortn.setStatus(_A)
_Pm1005AlmLineFailPortn_Type=EkiOnOff
_Pm1005AlmLineFailPortn_Object=MibTableColumn
pm1005AlmLineFailPortn=_Pm1005AlmLineFailPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,13),_Pm1005AlmLineFailPortn_Type())
pm1005AlmLineFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineFailPortn.setStatus(_A)
_Pm1005AlmLineActivePortn_Type=EkiOnOff
_Pm1005AlmLineActivePortn_Object=MibTableColumn
pm1005AlmLineActivePortn=_Pm1005AlmLineActivePortn_Object((1,3,6,1,4,1,20044,26,2,3,3,7,1,17),_Pm1005AlmLineActivePortn_Type())
pm1005AlmLineActivePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmLineActivePortn.setStatus(_A)
_Pm1005AlmdfrmAlmTable_Object=MibTable
pm1005AlmdfrmAlmTable=_Pm1005AlmdfrmAlmTable_Object((1,3,6,1,4,1,20044,26,2,3,3,128))
if mibBuilder.loadTexts:pm1005AlmdfrmAlmTable.setStatus(_A)
_Pm1005AlmdfrmAlmEntry_Object=MibTableRow
pm1005AlmdfrmAlmEntry=_Pm1005AlmdfrmAlmEntry_Object((1,3,6,1,4,1,20044,26,2,3,3,128,1))
pm1005AlmdfrmAlmEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm1005AlmdfrmAlmEntry.setStatus(_A)
class _Pm1005AlmdfrmAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmdfrmAlmIndex_Type.__name__=_D
_Pm1005AlmdfrmAlmIndex_Object=MibTableColumn
pm1005AlmdfrmAlmIndex=_Pm1005AlmdfrmAlmIndex_Object((1,3,6,1,4,1,20044,26,2,3,3,128,1,1),_Pm1005AlmdfrmAlmIndex_Type())
pm1005AlmdfrmAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmdfrmAlmIndex.setStatus(_A)
_Pm1005AlmDwAisDetPortn_Type=EkiOnOff
_Pm1005AlmDwAisDetPortn_Object=MibTableColumn
pm1005AlmDwAisDetPortn=_Pm1005AlmDwAisDetPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,128,1,2),_Pm1005AlmDwAisDetPortn_Type())
pm1005AlmDwAisDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwAisDetPortn.setStatus(_A)
_Pm1005AlmDwRdiDetPortn_Type=EkiOnOff
_Pm1005AlmDwRdiDetPortn_Object=MibTableColumn
pm1005AlmDwRdiDetPortn=_Pm1005AlmDwRdiDetPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,128,1,3),_Pm1005AlmDwRdiDetPortn_Type())
pm1005AlmDwRdiDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwRdiDetPortn.setStatus(_A)
_Pm1005AlmDwOofPortn_Type=EkiOnOff
_Pm1005AlmDwOofPortn_Object=MibTableColumn
pm1005AlmDwOofPortn=_Pm1005AlmDwOofPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,128,1,4),_Pm1005AlmDwOofPortn_Type())
pm1005AlmDwOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwOofPortn.setStatus(_A)
_Pm1005AlmDwLofPortn_Type=EkiOnOff
_Pm1005AlmDwLofPortn_Object=MibTableColumn
pm1005AlmDwLofPortn=_Pm1005AlmDwLofPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,128,1,5),_Pm1005AlmDwLofPortn_Type())
pm1005AlmDwLofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwLofPortn.setStatus(_A)
_Pm1005AlmlineSyncAlarmsTable_Object=MibTable
pm1005AlmlineSyncAlarmsTable=_Pm1005AlmlineSyncAlarmsTable_Object((1,3,6,1,4,1,20044,26,2,3,3,133))
if mibBuilder.loadTexts:pm1005AlmlineSyncAlarmsTable.setStatus(_A)
_Pm1005AlmlineSyncAlarmsEntry_Object=MibTableRow
pm1005AlmlineSyncAlarmsEntry=_Pm1005AlmlineSyncAlarmsEntry_Object((1,3,6,1,4,1,20044,26,2,3,3,133,1))
pm1005AlmlineSyncAlarmsEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm1005AlmlineSyncAlarmsEntry.setStatus(_A)
class _Pm1005AlmlineSyncAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineSyncAlarmsIndex_Type.__name__=_D
_Pm1005AlmlineSyncAlarmsIndex_Object=MibTableColumn
pm1005AlmlineSyncAlarmsIndex=_Pm1005AlmlineSyncAlarmsIndex_Object((1,3,6,1,4,1,20044,26,2,3,3,133,1,1),_Pm1005AlmlineSyncAlarmsIndex_Type())
pm1005AlmlineSyncAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineSyncAlarmsIndex.setStatus(_A)
_Pm1005AlmDwLockerrPortn_Type=EkiOnOff
_Pm1005AlmDwLockerrPortn_Object=MibTableColumn
pm1005AlmDwLockerrPortn=_Pm1005AlmDwLockerrPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,133,1,13),_Pm1005AlmDwLockerrPortn_Type())
pm1005AlmDwLockerrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwLockerrPortn.setStatus(_A)
_Pm1005AlmUpLockerrPortn_Type=EkiOnOff
_Pm1005AlmUpLockerrPortn_Object=MibTableColumn
pm1005AlmUpLockerrPortn=_Pm1005AlmUpLockerrPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,133,1,14),_Pm1005AlmUpLockerrPortn_Type())
pm1005AlmUpLockerrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmUpLockerrPortn.setStatus(_A)
_Pm1005AlmDwLosPortn_Type=EkiOnOff
_Pm1005AlmDwLosPortn_Object=MibTableColumn
pm1005AlmDwLosPortn=_Pm1005AlmDwLosPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,133,1,17),_Pm1005AlmDwLosPortn_Type())
pm1005AlmDwLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmDwLosPortn.setStatus(_A)
_Pm1005AlmlineXfp1AlarmsTable_Object=MibTable
pm1005AlmlineXfp1AlarmsTable=_Pm1005AlmlineXfp1AlarmsTable_Object((1,3,6,1,4,1,20044,26,2,3,3,211))
if mibBuilder.loadTexts:pm1005AlmlineXfp1AlarmsTable.setStatus(_A)
_Pm1005AlmlineXfp1AlarmsEntry_Object=MibTableRow
pm1005AlmlineXfp1AlarmsEntry=_Pm1005AlmlineXfp1AlarmsEntry_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1))
pm1005AlmlineXfp1AlarmsEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm1005AlmlineXfp1AlarmsEntry.setStatus(_A)
class _Pm1005AlmlineXfp1AlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005AlmlineXfp1AlarmsIndex_Type.__name__=_D
_Pm1005AlmlineXfp1AlarmsIndex_Object=MibTableColumn
pm1005AlmlineXfp1AlarmsIndex=_Pm1005AlmlineXfp1AlarmsIndex_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,1),_Pm1005AlmlineXfp1AlarmsIndex_Type())
pm1005AlmlineXfp1AlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmlineXfp1AlarmsIndex.setStatus(_A)
_Pm1005AlmModNrPortn_Type=EkiOnOff
_Pm1005AlmModNrPortn_Object=MibTableColumn
pm1005AlmModNrPortn=_Pm1005AlmModNrPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,3),_Pm1005AlmModNrPortn_Type())
pm1005AlmModNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmModNrPortn.setStatus(_A)
_Pm1005AlmRxCdrNotLockedPortn_Type=EkiOnOff
_Pm1005AlmRxCdrNotLockedPortn_Object=MibTableColumn
pm1005AlmRxCdrNotLockedPortn=_Pm1005AlmRxCdrNotLockedPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,4),_Pm1005AlmRxCdrNotLockedPortn_Type())
pm1005AlmRxCdrNotLockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxCdrNotLockedPortn.setStatus(_A)
_Pm1005AlmRxNrPortn_Type=EkiOnOff
_Pm1005AlmRxNrPortn_Object=MibTableColumn
pm1005AlmRxNrPortn=_Pm1005AlmRxNrPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,6),_Pm1005AlmRxNrPortn_Type())
pm1005AlmRxNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmRxNrPortn.setStatus(_A)
_Pm1005AlmTxCdrNotLockedPortn_Type=EkiOnOff
_Pm1005AlmTxCdrNotLockedPortn_Object=MibTableColumn
pm1005AlmTxCdrNotLockedPortn=_Pm1005AlmTxCdrNotLockedPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,7),_Pm1005AlmTxCdrNotLockedPortn_Type())
pm1005AlmTxCdrNotLockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxCdrNotLockedPortn.setStatus(_A)
_Pm1005AlmTxFaultPortn_Type=EkiOnOff
_Pm1005AlmTxFaultPortn_Object=MibTableColumn
pm1005AlmTxFaultPortn=_Pm1005AlmTxFaultPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,8),_Pm1005AlmTxFaultPortn_Type())
pm1005AlmTxFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxFaultPortn.setStatus(_A)
_Pm1005AlmTxNrPortn_Type=EkiOnOff
_Pm1005AlmTxNrPortn_Object=MibTableColumn
pm1005AlmTxNrPortn=_Pm1005AlmTxNrPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,9),_Pm1005AlmTxNrPortn_Type())
pm1005AlmTxNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTxNrPortn.setStatus(_A)
_Pm1005AlmWavelengthUnlockedPortn_Type=EkiOnOff
_Pm1005AlmWavelengthUnlockedPortn_Object=MibTableColumn
pm1005AlmWavelengthUnlockedPortn=_Pm1005AlmWavelengthUnlockedPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,15),_Pm1005AlmWavelengthUnlockedPortn_Type())
pm1005AlmWavelengthUnlockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmWavelengthUnlockedPortn.setStatus(_A)
_Pm1005AlmTecFaultPortn_Type=EkiOnOff
_Pm1005AlmTecFaultPortn_Object=MibTableColumn
pm1005AlmTecFaultPortn=_Pm1005AlmTecFaultPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,16),_Pm1005AlmTecFaultPortn_Type())
pm1005AlmTecFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmTecFaultPortn.setStatus(_A)
_Pm1005AlmApdSupplyFaultPortn_Type=EkiOnOff
_Pm1005AlmApdSupplyFaultPortn_Object=MibTableColumn
pm1005AlmApdSupplyFaultPortn=_Pm1005AlmApdSupplyFaultPortn_Object((1,3,6,1,4,1,20044,26,2,3,3,211,1,17),_Pm1005AlmApdSupplyFaultPortn_Type())
pm1005AlmApdSupplyFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005AlmApdSupplyFaultPortn.setStatus(_A)
_Pm1005measures_ObjectIdentity=ObjectIdentity
pm1005measures=_Pm1005measures_ObjectIdentity((1,3,6,1,4,1,20044,26,3))
_Pm1005MesrOther_ObjectIdentity=ObjectIdentity
pm1005MesrOther=_Pm1005MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,26,3,1))
_Pm1005Mesrsynth0_Type=EkiMeasureType
_Pm1005Mesrsynth0_Object=MibScalar
pm1005Mesrsynth0=_Pm1005Mesrsynth0_Object((1,3,6,1,4,1,20044,26,3,1,0),_Pm1005Mesrsynth0_Type())
pm1005Mesrsynth0.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrsynth0.setStatus(_G)
_Pm1005Mesrsynth1_Type=EkiMeasureType
_Pm1005Mesrsynth1_Object=MibScalar
pm1005Mesrsynth1=_Pm1005Mesrsynth1_Object((1,3,6,1,4,1,20044,26,3,1,1),_Pm1005Mesrsynth1_Type())
pm1005Mesrsynth1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrsynth1.setStatus(_G)
_Pm1005MesrClient_ObjectIdentity=ObjectIdentity
pm1005MesrClient=_Pm1005MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,26,3,2))
_Pm1005MesrtempMeasTable_Object=MibTable
pm1005MesrtempMeasTable=_Pm1005MesrtempMeasTable_Object((1,3,6,1,4,1,20044,26,3,2,16))
if mibBuilder.loadTexts:pm1005MesrtempMeasTable.setStatus(_A)
_Pm1005MesrtempMeasEntry_Object=MibTableRow
pm1005MesrtempMeasEntry=_Pm1005MesrtempMeasEntry_Object((1,3,6,1,4,1,20044,26,3,2,16,1))
pm1005MesrtempMeasEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm1005MesrtempMeasEntry.setStatus(_A)
class _Pm1005MesrtempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MesrtempMeasIndex_Type.__name__=_D
_Pm1005MesrtempMeasIndex_Object=MibTableColumn
pm1005MesrtempMeasIndex=_Pm1005MesrtempMeasIndex_Object((1,3,6,1,4,1,20044,26,3,2,16,1,1),_Pm1005MesrtempMeasIndex_Type())
pm1005MesrtempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrtempMeasIndex.setStatus(_A)
class _Pm1005MesrtempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005MesrtempMeasPortn_Type.__name__=_D
_Pm1005MesrtempMeasPortn_Object=MibTableColumn
pm1005MesrtempMeasPortn=_Pm1005MesrtempMeasPortn_Object((1,3,6,1,4,1,20044,26,3,2,16,1,2),_Pm1005MesrtempMeasPortn_Type())
pm1005MesrtempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrtempMeasPortn.setStatus(_A)
_Pm1005MesrvoltMeasTable_Object=MibTable
pm1005MesrvoltMeasTable=_Pm1005MesrvoltMeasTable_Object((1,3,6,1,4,1,20044,26,3,2,24))
if mibBuilder.loadTexts:pm1005MesrvoltMeasTable.setStatus(_A)
_Pm1005MesrvoltMeasEntry_Object=MibTableRow
pm1005MesrvoltMeasEntry=_Pm1005MesrvoltMeasEntry_Object((1,3,6,1,4,1,20044,26,3,2,24,1))
pm1005MesrvoltMeasEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm1005MesrvoltMeasEntry.setStatus(_A)
class _Pm1005MesrvoltMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MesrvoltMeasIndex_Type.__name__=_D
_Pm1005MesrvoltMeasIndex_Object=MibTableColumn
pm1005MesrvoltMeasIndex=_Pm1005MesrvoltMeasIndex_Object((1,3,6,1,4,1,20044,26,3,2,24,1,1),_Pm1005MesrvoltMeasIndex_Type())
pm1005MesrvoltMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrvoltMeasIndex.setStatus(_A)
class _Pm1005MesrvoltMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005MesrvoltMeasPortn_Type.__name__=_D
_Pm1005MesrvoltMeasPortn_Object=MibTableColumn
pm1005MesrvoltMeasPortn=_Pm1005MesrvoltMeasPortn_Object((1,3,6,1,4,1,20044,26,3,2,24,1,2),_Pm1005MesrvoltMeasPortn_Type())
pm1005MesrvoltMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrvoltMeasPortn.setStatus(_A)
_Pm1005MesrbiasMeasTable_Object=MibTable
pm1005MesrbiasMeasTable=_Pm1005MesrbiasMeasTable_Object((1,3,6,1,4,1,20044,26,3,2,32))
if mibBuilder.loadTexts:pm1005MesrbiasMeasTable.setStatus(_A)
_Pm1005MesrbiasMeasEntry_Object=MibTableRow
pm1005MesrbiasMeasEntry=_Pm1005MesrbiasMeasEntry_Object((1,3,6,1,4,1,20044,26,3,2,32,1))
pm1005MesrbiasMeasEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm1005MesrbiasMeasEntry.setStatus(_A)
class _Pm1005MesrbiasMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MesrbiasMeasIndex_Type.__name__=_D
_Pm1005MesrbiasMeasIndex_Object=MibTableColumn
pm1005MesrbiasMeasIndex=_Pm1005MesrbiasMeasIndex_Object((1,3,6,1,4,1,20044,26,3,2,32,1,1),_Pm1005MesrbiasMeasIndex_Type())
pm1005MesrbiasMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrbiasMeasIndex.setStatus(_A)
class _Pm1005MesrbiasMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005MesrbiasMeasPortn_Type.__name__=_D
_Pm1005MesrbiasMeasPortn_Object=MibTableColumn
pm1005MesrbiasMeasPortn=_Pm1005MesrbiasMeasPortn_Object((1,3,6,1,4,1,20044,26,3,2,32,1,2),_Pm1005MesrbiasMeasPortn_Type())
pm1005MesrbiasMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrbiasMeasPortn.setStatus(_A)
_Pm1005MesrtxpwrMeasTable_Object=MibTable
pm1005MesrtxpwrMeasTable=_Pm1005MesrtxpwrMeasTable_Object((1,3,6,1,4,1,20044,26,3,2,40))
if mibBuilder.loadTexts:pm1005MesrtxpwrMeasTable.setStatus(_A)
_Pm1005MesrtxpwrMeasEntry_Object=MibTableRow
pm1005MesrtxpwrMeasEntry=_Pm1005MesrtxpwrMeasEntry_Object((1,3,6,1,4,1,20044,26,3,2,40,1))
pm1005MesrtxpwrMeasEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm1005MesrtxpwrMeasEntry.setStatus(_A)
class _Pm1005MesrtxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MesrtxpwrMeasIndex_Type.__name__=_D
_Pm1005MesrtxpwrMeasIndex_Object=MibTableColumn
pm1005MesrtxpwrMeasIndex=_Pm1005MesrtxpwrMeasIndex_Object((1,3,6,1,4,1,20044,26,3,2,40,1,1),_Pm1005MesrtxpwrMeasIndex_Type())
pm1005MesrtxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrtxpwrMeasIndex.setStatus(_A)
class _Pm1005MesrtxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005MesrtxpwrMeasPortn_Type.__name__=_D
_Pm1005MesrtxpwrMeasPortn_Object=MibTableColumn
pm1005MesrtxpwrMeasPortn=_Pm1005MesrtxpwrMeasPortn_Object((1,3,6,1,4,1,20044,26,3,2,40,1,2),_Pm1005MesrtxpwrMeasPortn_Type())
pm1005MesrtxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrtxpwrMeasPortn.setStatus(_A)
_Pm1005MesrrxpwrMeasTable_Object=MibTable
pm1005MesrrxpwrMeasTable=_Pm1005MesrrxpwrMeasTable_Object((1,3,6,1,4,1,20044,26,3,2,48))
if mibBuilder.loadTexts:pm1005MesrrxpwrMeasTable.setStatus(_A)
_Pm1005MesrrxpwrMeasEntry_Object=MibTableRow
pm1005MesrrxpwrMeasEntry=_Pm1005MesrrxpwrMeasEntry_Object((1,3,6,1,4,1,20044,26,3,2,48,1))
pm1005MesrrxpwrMeasEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm1005MesrrxpwrMeasEntry.setStatus(_A)
class _Pm1005MesrrxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MesrrxpwrMeasIndex_Type.__name__=_D
_Pm1005MesrrxpwrMeasIndex_Object=MibTableColumn
pm1005MesrrxpwrMeasIndex=_Pm1005MesrrxpwrMeasIndex_Object((1,3,6,1,4,1,20044,26,3,2,48,1,1),_Pm1005MesrrxpwrMeasIndex_Type())
pm1005MesrrxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrrxpwrMeasIndex.setStatus(_A)
class _Pm1005MesrrxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005MesrrxpwrMeasPortn_Type.__name__=_D
_Pm1005MesrrxpwrMeasPortn_Object=MibTableColumn
pm1005MesrrxpwrMeasPortn=_Pm1005MesrrxpwrMeasPortn_Object((1,3,6,1,4,1,20044,26,3,2,48,1,2),_Pm1005MesrrxpwrMeasPortn_Type())
pm1005MesrrxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MesrrxpwrMeasPortn.setStatus(_A)
_Pm1005MesrLine_ObjectIdentity=ObjectIdentity
pm1005MesrLine=_Pm1005MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,26,3,3))
_Pm1005Mesrxfp1LxModTempMeasTable_Object=MibTable
pm1005Mesrxfp1LxModTempMeasTable=_Pm1005Mesrxfp1LxModTempMeasTable_Object((1,3,6,1,4,1,20044,26,3,3,208))
if mibBuilder.loadTexts:pm1005Mesrxfp1LxModTempMeasTable.setStatus(_A)
_Pm1005Mesrxfp1LxModTempMeasEntry_Object=MibTableRow
pm1005Mesrxfp1LxModTempMeasEntry=_Pm1005Mesrxfp1LxModTempMeasEntry_Object((1,3,6,1,4,1,20044,26,3,3,208,1))
pm1005Mesrxfp1LxModTempMeasEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm1005Mesrxfp1LxModTempMeasEntry.setStatus(_A)
class _Pm1005Mesrxfp1LxModTempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1LxModTempMeasIndex_Type.__name__=_D
_Pm1005Mesrxfp1LxModTempMeasIndex_Object=MibTableColumn
pm1005Mesrxfp1LxModTempMeasIndex=_Pm1005Mesrxfp1LxModTempMeasIndex_Object((1,3,6,1,4,1,20044,26,3,3,208,1,1),_Pm1005Mesrxfp1LxModTempMeasIndex_Type())
pm1005Mesrxfp1LxModTempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LxModTempMeasIndex.setStatus(_A)
class _Pm1005Mesrxfp1LxModTempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1LxModTempMeasPortn_Type.__name__=_D
_Pm1005Mesrxfp1LxModTempMeasPortn_Object=MibTableColumn
pm1005Mesrxfp1LxModTempMeasPortn=_Pm1005Mesrxfp1LxModTempMeasPortn_Object((1,3,6,1,4,1,20044,26,3,3,208,1,2),_Pm1005Mesrxfp1LxModTempMeasPortn_Type())
pm1005Mesrxfp1LxModTempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LxModTempMeasPortn.setStatus(_A)
_Pm1005Mesrxfp1ReservedTable_Object=MibTable
pm1005Mesrxfp1ReservedTable=_Pm1005Mesrxfp1ReservedTable_Object((1,3,6,1,4,1,20044,26,3,3,209))
if mibBuilder.loadTexts:pm1005Mesrxfp1ReservedTable.setStatus(_G)
_Pm1005Mesrxfp1ReservedEntry_Object=MibTableRow
pm1005Mesrxfp1ReservedEntry=_Pm1005Mesrxfp1ReservedEntry_Object((1,3,6,1,4,1,20044,26,3,3,209,1))
pm1005Mesrxfp1ReservedEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm1005Mesrxfp1ReservedEntry.setStatus(_G)
class _Pm1005Mesrxfp1ReservedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1ReservedIndex_Type.__name__=_D
_Pm1005Mesrxfp1ReservedIndex_Object=MibTableColumn
pm1005Mesrxfp1ReservedIndex=_Pm1005Mesrxfp1ReservedIndex_Object((1,3,6,1,4,1,20044,26,3,3,209,1,1),_Pm1005Mesrxfp1ReservedIndex_Type())
pm1005Mesrxfp1ReservedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1ReservedIndex.setStatus(_G)
class _Pm1005Mesrxfp1ReservedPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1ReservedPortn_Type.__name__=_D
_Pm1005Mesrxfp1ReservedPortn_Object=MibTableColumn
pm1005Mesrxfp1ReservedPortn=_Pm1005Mesrxfp1ReservedPortn_Object((1,3,6,1,4,1,20044,26,3,3,209,1,2),_Pm1005Mesrxfp1ReservedPortn_Type())
pm1005Mesrxfp1ReservedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1ReservedPortn.setStatus(_G)
_Pm1005Mesrxfp1LoBiasCurrentMeasTable_Object=MibTable
pm1005Mesrxfp1LoBiasCurrentMeasTable=_Pm1005Mesrxfp1LoBiasCurrentMeasTable_Object((1,3,6,1,4,1,20044,26,3,3,210))
if mibBuilder.loadTexts:pm1005Mesrxfp1LoBiasCurrentMeasTable.setStatus(_A)
_Pm1005Mesrxfp1LoBiasCurrentMeasEntry_Object=MibTableRow
pm1005Mesrxfp1LoBiasCurrentMeasEntry=_Pm1005Mesrxfp1LoBiasCurrentMeasEntry_Object((1,3,6,1,4,1,20044,26,3,3,210,1))
pm1005Mesrxfp1LoBiasCurrentMeasEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm1005Mesrxfp1LoBiasCurrentMeasEntry.setStatus(_A)
class _Pm1005Mesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1LoBiasCurrentMeasIndex_Type.__name__=_D
_Pm1005Mesrxfp1LoBiasCurrentMeasIndex_Object=MibTableColumn
pm1005Mesrxfp1LoBiasCurrentMeasIndex=_Pm1005Mesrxfp1LoBiasCurrentMeasIndex_Object((1,3,6,1,4,1,20044,26,3,3,210,1,1),_Pm1005Mesrxfp1LoBiasCurrentMeasIndex_Type())
pm1005Mesrxfp1LoBiasCurrentMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LoBiasCurrentMeasIndex.setStatus(_A)
class _Pm1005Mesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1LoBiasCurrentMeasPortn_Type.__name__=_D
_Pm1005Mesrxfp1LoBiasCurrentMeasPortn_Object=MibTableColumn
pm1005Mesrxfp1LoBiasCurrentMeasPortn=_Pm1005Mesrxfp1LoBiasCurrentMeasPortn_Object((1,3,6,1,4,1,20044,26,3,3,210,1,2),_Pm1005Mesrxfp1LoBiasCurrentMeasPortn_Type())
pm1005Mesrxfp1LoBiasCurrentMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LoBiasCurrentMeasPortn.setStatus(_A)
_Pm1005Mesrxfp1LoTxPowerMeasTable_Object=MibTable
pm1005Mesrxfp1LoTxPowerMeasTable=_Pm1005Mesrxfp1LoTxPowerMeasTable_Object((1,3,6,1,4,1,20044,26,3,3,211))
if mibBuilder.loadTexts:pm1005Mesrxfp1LoTxPowerMeasTable.setStatus(_A)
_Pm1005Mesrxfp1LoTxPowerMeasEntry_Object=MibTableRow
pm1005Mesrxfp1LoTxPowerMeasEntry=_Pm1005Mesrxfp1LoTxPowerMeasEntry_Object((1,3,6,1,4,1,20044,26,3,3,211,1))
pm1005Mesrxfp1LoTxPowerMeasEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm1005Mesrxfp1LoTxPowerMeasEntry.setStatus(_A)
class _Pm1005Mesrxfp1LoTxPowerMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1LoTxPowerMeasIndex_Type.__name__=_D
_Pm1005Mesrxfp1LoTxPowerMeasIndex_Object=MibTableColumn
pm1005Mesrxfp1LoTxPowerMeasIndex=_Pm1005Mesrxfp1LoTxPowerMeasIndex_Object((1,3,6,1,4,1,20044,26,3,3,211,1,1),_Pm1005Mesrxfp1LoTxPowerMeasIndex_Type())
pm1005Mesrxfp1LoTxPowerMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LoTxPowerMeasIndex.setStatus(_A)
class _Pm1005Mesrxfp1LoTxPowerMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1LoTxPowerMeasPortn_Type.__name__=_D
_Pm1005Mesrxfp1LoTxPowerMeasPortn_Object=MibTableColumn
pm1005Mesrxfp1LoTxPowerMeasPortn=_Pm1005Mesrxfp1LoTxPowerMeasPortn_Object((1,3,6,1,4,1,20044,26,3,3,211,1,2),_Pm1005Mesrxfp1LoTxPowerMeasPortn_Type())
pm1005Mesrxfp1LoTxPowerMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LoTxPowerMeasPortn.setStatus(_A)
_Pm1005Mesrxfp1LiRxPowerMeasTable_Object=MibTable
pm1005Mesrxfp1LiRxPowerMeasTable=_Pm1005Mesrxfp1LiRxPowerMeasTable_Object((1,3,6,1,4,1,20044,26,3,3,212))
if mibBuilder.loadTexts:pm1005Mesrxfp1LiRxPowerMeasTable.setStatus(_A)
_Pm1005Mesrxfp1LiRxPowerMeasEntry_Object=MibTableRow
pm1005Mesrxfp1LiRxPowerMeasEntry=_Pm1005Mesrxfp1LiRxPowerMeasEntry_Object((1,3,6,1,4,1,20044,26,3,3,212,1))
pm1005Mesrxfp1LiRxPowerMeasEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm1005Mesrxfp1LiRxPowerMeasEntry.setStatus(_A)
class _Pm1005Mesrxfp1LiRxPowerMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1LiRxPowerMeasIndex_Type.__name__=_D
_Pm1005Mesrxfp1LiRxPowerMeasIndex_Object=MibTableColumn
pm1005Mesrxfp1LiRxPowerMeasIndex=_Pm1005Mesrxfp1LiRxPowerMeasIndex_Object((1,3,6,1,4,1,20044,26,3,3,212,1,1),_Pm1005Mesrxfp1LiRxPowerMeasIndex_Type())
pm1005Mesrxfp1LiRxPowerMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LiRxPowerMeasIndex.setStatus(_A)
class _Pm1005Mesrxfp1LiRxPowerMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1LiRxPowerMeasPortn_Type.__name__=_D
_Pm1005Mesrxfp1LiRxPowerMeasPortn_Object=MibTableColumn
pm1005Mesrxfp1LiRxPowerMeasPortn=_Pm1005Mesrxfp1LiRxPowerMeasPortn_Object((1,3,6,1,4,1,20044,26,3,3,212,1,2),_Pm1005Mesrxfp1LiRxPowerMeasPortn_Type())
pm1005Mesrxfp1LiRxPowerMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LiRxPowerMeasPortn.setStatus(_A)
_Pm1005Mesrxfp1LxAux1MeasTable_Object=MibTable
pm1005Mesrxfp1LxAux1MeasTable=_Pm1005Mesrxfp1LxAux1MeasTable_Object((1,3,6,1,4,1,20044,26,3,3,213))
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux1MeasTable.setStatus(_G)
_Pm1005Mesrxfp1LxAux1MeasEntry_Object=MibTableRow
pm1005Mesrxfp1LxAux1MeasEntry=_Pm1005Mesrxfp1LxAux1MeasEntry_Object((1,3,6,1,4,1,20044,26,3,3,213,1))
pm1005Mesrxfp1LxAux1MeasEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux1MeasEntry.setStatus(_G)
class _Pm1005Mesrxfp1LxAux1MeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1LxAux1MeasIndex_Type.__name__=_D
_Pm1005Mesrxfp1LxAux1MeasIndex_Object=MibTableColumn
pm1005Mesrxfp1LxAux1MeasIndex=_Pm1005Mesrxfp1LxAux1MeasIndex_Object((1,3,6,1,4,1,20044,26,3,3,213,1,1),_Pm1005Mesrxfp1LxAux1MeasIndex_Type())
pm1005Mesrxfp1LxAux1MeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux1MeasIndex.setStatus(_G)
class _Pm1005Mesrxfp1LxAux1MeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1LxAux1MeasPortn_Type.__name__=_D
_Pm1005Mesrxfp1LxAux1MeasPortn_Object=MibTableColumn
pm1005Mesrxfp1LxAux1MeasPortn=_Pm1005Mesrxfp1LxAux1MeasPortn_Object((1,3,6,1,4,1,20044,26,3,3,213,1,2),_Pm1005Mesrxfp1LxAux1MeasPortn_Type())
pm1005Mesrxfp1LxAux1MeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux1MeasPortn.setStatus(_G)
_Pm1005Mesrxfp1LxAux2MeasTable_Object=MibTable
pm1005Mesrxfp1LxAux2MeasTable=_Pm1005Mesrxfp1LxAux2MeasTable_Object((1,3,6,1,4,1,20044,26,3,3,214))
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux2MeasTable.setStatus(_G)
_Pm1005Mesrxfp1LxAux2MeasEntry_Object=MibTableRow
pm1005Mesrxfp1LxAux2MeasEntry=_Pm1005Mesrxfp1LxAux2MeasEntry_Object((1,3,6,1,4,1,20044,26,3,3,214,1))
pm1005Mesrxfp1LxAux2MeasEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux2MeasEntry.setStatus(_G)
class _Pm1005Mesrxfp1LxAux2MeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrxfp1LxAux2MeasIndex_Type.__name__=_D
_Pm1005Mesrxfp1LxAux2MeasIndex_Object=MibTableColumn
pm1005Mesrxfp1LxAux2MeasIndex=_Pm1005Mesrxfp1LxAux2MeasIndex_Object((1,3,6,1,4,1,20044,26,3,3,214,1,1),_Pm1005Mesrxfp1LxAux2MeasIndex_Type())
pm1005Mesrxfp1LxAux2MeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux2MeasIndex.setStatus(_G)
class _Pm1005Mesrxfp1LxAux2MeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrxfp1LxAux2MeasPortn_Type.__name__=_D
_Pm1005Mesrxfp1LxAux2MeasPortn_Object=MibTableColumn
pm1005Mesrxfp1LxAux2MeasPortn=_Pm1005Mesrxfp1LxAux2MeasPortn_Object((1,3,6,1,4,1,20044,26,3,3,214,1,2),_Pm1005Mesrxfp1LxAux2MeasPortn_Type())
pm1005Mesrxfp1LxAux2MeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrxfp1LxAux2MeasPortn.setStatus(_G)
_Pm1005Mesrotx1AgingTable_Object=MibTable
pm1005Mesrotx1AgingTable=_Pm1005Mesrotx1AgingTable_Object((1,3,6,1,4,1,20044,26,3,3,224))
if mibBuilder.loadTexts:pm1005Mesrotx1AgingTable.setStatus(_A)
_Pm1005Mesrotx1AgingEntry_Object=MibTableRow
pm1005Mesrotx1AgingEntry=_Pm1005Mesrotx1AgingEntry_Object((1,3,6,1,4,1,20044,26,3,3,224,1))
pm1005Mesrotx1AgingEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm1005Mesrotx1AgingEntry.setStatus(_A)
class _Pm1005Mesrotx1AgingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrotx1AgingIndex_Type.__name__=_D
_Pm1005Mesrotx1AgingIndex_Object=MibTableColumn
pm1005Mesrotx1AgingIndex=_Pm1005Mesrotx1AgingIndex_Object((1,3,6,1,4,1,20044,26,3,3,224,1,1),_Pm1005Mesrotx1AgingIndex_Type())
pm1005Mesrotx1AgingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1AgingIndex.setStatus(_A)
class _Pm1005Mesrotx1AgingPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrotx1AgingPortn_Type.__name__=_D
_Pm1005Mesrotx1AgingPortn_Object=MibTableColumn
pm1005Mesrotx1AgingPortn=_Pm1005Mesrotx1AgingPortn_Object((1,3,6,1,4,1,20044,26,3,3,224,1,2),_Pm1005Mesrotx1AgingPortn_Type())
pm1005Mesrotx1AgingPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1AgingPortn.setStatus(_A)
_Pm1005Mesrotx1LaserTemperatureTable_Object=MibTable
pm1005Mesrotx1LaserTemperatureTable=_Pm1005Mesrotx1LaserTemperatureTable_Object((1,3,6,1,4,1,20044,26,3,3,225))
if mibBuilder.loadTexts:pm1005Mesrotx1LaserTemperatureTable.setStatus(_G)
_Pm1005Mesrotx1LaserTemperatureEntry_Object=MibTableRow
pm1005Mesrotx1LaserTemperatureEntry=_Pm1005Mesrotx1LaserTemperatureEntry_Object((1,3,6,1,4,1,20044,26,3,3,225,1))
pm1005Mesrotx1LaserTemperatureEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm1005Mesrotx1LaserTemperatureEntry.setStatus(_G)
class _Pm1005Mesrotx1LaserTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrotx1LaserTemperatureIndex_Type.__name__=_D
_Pm1005Mesrotx1LaserTemperatureIndex_Object=MibTableColumn
pm1005Mesrotx1LaserTemperatureIndex=_Pm1005Mesrotx1LaserTemperatureIndex_Object((1,3,6,1,4,1,20044,26,3,3,225,1,1),_Pm1005Mesrotx1LaserTemperatureIndex_Type())
pm1005Mesrotx1LaserTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1LaserTemperatureIndex.setStatus(_G)
class _Pm1005Mesrotx1LaserTemperaturePortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrotx1LaserTemperaturePortn_Type.__name__=_D
_Pm1005Mesrotx1LaserTemperaturePortn_Object=MibTableColumn
pm1005Mesrotx1LaserTemperaturePortn=_Pm1005Mesrotx1LaserTemperaturePortn_Object((1,3,6,1,4,1,20044,26,3,3,225,1,2),_Pm1005Mesrotx1LaserTemperaturePortn_Type())
pm1005Mesrotx1LaserTemperaturePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1LaserTemperaturePortn.setStatus(_G)
_Pm1005Mesrotx1FreqDeviationTable_Object=MibTable
pm1005Mesrotx1FreqDeviationTable=_Pm1005Mesrotx1FreqDeviationTable_Object((1,3,6,1,4,1,20044,26,3,3,226))
if mibBuilder.loadTexts:pm1005Mesrotx1FreqDeviationTable.setStatus(_A)
_Pm1005Mesrotx1FreqDeviationEntry_Object=MibTableRow
pm1005Mesrotx1FreqDeviationEntry=_Pm1005Mesrotx1FreqDeviationEntry_Object((1,3,6,1,4,1,20044,26,3,3,226,1))
pm1005Mesrotx1FreqDeviationEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm1005Mesrotx1FreqDeviationEntry.setStatus(_A)
class _Pm1005Mesrotx1FreqDeviationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrotx1FreqDeviationIndex_Type.__name__=_D
_Pm1005Mesrotx1FreqDeviationIndex_Object=MibTableColumn
pm1005Mesrotx1FreqDeviationIndex=_Pm1005Mesrotx1FreqDeviationIndex_Object((1,3,6,1,4,1,20044,26,3,3,226,1,1),_Pm1005Mesrotx1FreqDeviationIndex_Type())
pm1005Mesrotx1FreqDeviationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1FreqDeviationIndex.setStatus(_A)
class _Pm1005Mesrotx1FreqDeviationPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrotx1FreqDeviationPortn_Type.__name__=_D
_Pm1005Mesrotx1FreqDeviationPortn_Object=MibTableColumn
pm1005Mesrotx1FreqDeviationPortn=_Pm1005Mesrotx1FreqDeviationPortn_Object((1,3,6,1,4,1,20044,26,3,3,226,1,2),_Pm1005Mesrotx1FreqDeviationPortn_Type())
pm1005Mesrotx1FreqDeviationPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1FreqDeviationPortn.setStatus(_A)
_Pm1005Mesrotx1LaserWvlengthTable_Object=MibTable
pm1005Mesrotx1LaserWvlengthTable=_Pm1005Mesrotx1LaserWvlengthTable_Object((1,3,6,1,4,1,20044,26,3,3,227))
if mibBuilder.loadTexts:pm1005Mesrotx1LaserWvlengthTable.setStatus(_A)
_Pm1005Mesrotx1LaserWvlengthEntry_Object=MibTableRow
pm1005Mesrotx1LaserWvlengthEntry=_Pm1005Mesrotx1LaserWvlengthEntry_Object((1,3,6,1,4,1,20044,26,3,3,227,1))
pm1005Mesrotx1LaserWvlengthEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm1005Mesrotx1LaserWvlengthEntry.setStatus(_A)
class _Pm1005Mesrotx1LaserWvlengthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005Mesrotx1LaserWvlengthIndex_Type.__name__=_D
_Pm1005Mesrotx1LaserWvlengthIndex_Object=MibTableColumn
pm1005Mesrotx1LaserWvlengthIndex=_Pm1005Mesrotx1LaserWvlengthIndex_Object((1,3,6,1,4,1,20044,26,3,3,227,1,1),_Pm1005Mesrotx1LaserWvlengthIndex_Type())
pm1005Mesrotx1LaserWvlengthIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1LaserWvlengthIndex.setStatus(_A)
class _Pm1005Mesrotx1LaserWvlengthPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1005Mesrotx1LaserWvlengthPortn_Type.__name__=_D
_Pm1005Mesrotx1LaserWvlengthPortn_Object=MibTableColumn
pm1005Mesrotx1LaserWvlengthPortn=_Pm1005Mesrotx1LaserWvlengthPortn_Object((1,3,6,1,4,1,20044,26,3,3,227,1,2),_Pm1005Mesrotx1LaserWvlengthPortn_Type())
pm1005Mesrotx1LaserWvlengthPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Mesrotx1LaserWvlengthPortn.setStatus(_A)
_Pm1005counters_ObjectIdentity=ObjectIdentity
pm1005counters=_Pm1005counters_ObjectIdentity((1,3,6,1,4,1,20044,26,4))
_Pm1005CntOther_ObjectIdentity=ObjectIdentity
pm1005CntOther=_Pm1005CntOther_ObjectIdentity((1,3,6,1,4,1,20044,26,4,1))
_Pm1005CntClient_ObjectIdentity=ObjectIdentity
pm1005CntClient=_Pm1005CntClient_ObjectIdentity((1,3,6,1,4,1,20044,26,4,2))
_Pm1005CntupRaRemCntTable_Object=MibTable
pm1005CntupRaRemCntTable=_Pm1005CntupRaRemCntTable_Object((1,3,6,1,4,1,20044,26,4,2,16))
if mibBuilder.loadTexts:pm1005CntupRaRemCntTable.setStatus(_A)
_Pm1005CntupRaRemCntEntry_Object=MibTableRow
pm1005CntupRaRemCntEntry=_Pm1005CntupRaRemCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,16,1))
pm1005CntupRaRemCntEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm1005CntupRaRemCntEntry.setStatus(_A)
class _Pm1005CntupRaRemCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntupRaRemCntIndex_Type.__name__=_D
_Pm1005CntupRaRemCntIndex_Object=MibTableColumn
pm1005CntupRaRemCntIndex=_Pm1005CntupRaRemCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,16,1,1),_Pm1005CntupRaRemCntIndex_Type())
pm1005CntupRaRemCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaRemCntIndex.setStatus(_A)
_Pm1005CntupRaRemCntValuePortn_Type=Counter32
_Pm1005CntupRaRemCntValuePortn_Object=MibTableColumn
pm1005CntupRaRemCntValuePortn=_Pm1005CntupRaRemCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,16,1,2),_Pm1005CntupRaRemCntValuePortn_Type())
pm1005CntupRaRemCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaRemCntValuePortn.setStatus(_A)
_Pm1005CntupRaRemCntErrorPortn_Type=EkiOnOff
_Pm1005CntupRaRemCntErrorPortn_Object=MibTableColumn
pm1005CntupRaRemCntErrorPortn=_Pm1005CntupRaRemCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,16,1,3),_Pm1005CntupRaRemCntErrorPortn_Type())
pm1005CntupRaRemCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaRemCntErrorPortn.setStatus(_A)
_Pm1005CntupRaRemCntOverloadPortn_Type=EkiOnOff
_Pm1005CntupRaRemCntOverloadPortn_Object=MibTableColumn
pm1005CntupRaRemCntOverloadPortn=_Pm1005CntupRaRemCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,16,1,4),_Pm1005CntupRaRemCntOverloadPortn_Type())
pm1005CntupRaRemCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaRemCntOverloadPortn.setStatus(_A)
_Pm1005CntupRaInsCntTable_Object=MibTable
pm1005CntupRaInsCntTable=_Pm1005CntupRaInsCntTable_Object((1,3,6,1,4,1,20044,26,4,2,24))
if mibBuilder.loadTexts:pm1005CntupRaInsCntTable.setStatus(_A)
_Pm1005CntupRaInsCntEntry_Object=MibTableRow
pm1005CntupRaInsCntEntry=_Pm1005CntupRaInsCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,24,1))
pm1005CntupRaInsCntEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm1005CntupRaInsCntEntry.setStatus(_A)
class _Pm1005CntupRaInsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntupRaInsCntIndex_Type.__name__=_D
_Pm1005CntupRaInsCntIndex_Object=MibTableColumn
pm1005CntupRaInsCntIndex=_Pm1005CntupRaInsCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,24,1,1),_Pm1005CntupRaInsCntIndex_Type())
pm1005CntupRaInsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaInsCntIndex.setStatus(_A)
_Pm1005CntupRaInsCntValuePortn_Type=Counter32
_Pm1005CntupRaInsCntValuePortn_Object=MibTableColumn
pm1005CntupRaInsCntValuePortn=_Pm1005CntupRaInsCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,24,1,2),_Pm1005CntupRaInsCntValuePortn_Type())
pm1005CntupRaInsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaInsCntValuePortn.setStatus(_A)
_Pm1005CntupRaInsCntErrorPortn_Type=EkiOnOff
_Pm1005CntupRaInsCntErrorPortn_Object=MibTableColumn
pm1005CntupRaInsCntErrorPortn=_Pm1005CntupRaInsCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,24,1,3),_Pm1005CntupRaInsCntErrorPortn_Type())
pm1005CntupRaInsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaInsCntErrorPortn.setStatus(_A)
_Pm1005CntupRaInsCntOverloadPortn_Type=EkiOnOff
_Pm1005CntupRaInsCntOverloadPortn_Object=MibTableColumn
pm1005CntupRaInsCntOverloadPortn=_Pm1005CntupRaInsCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,24,1,4),_Pm1005CntupRaInsCntOverloadPortn_Type())
pm1005CntupRaInsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRaInsCntOverloadPortn.setStatus(_A)
_Pm1005CntupRdErrCntTable_Object=MibTable
pm1005CntupRdErrCntTable=_Pm1005CntupRdErrCntTable_Object((1,3,6,1,4,1,20044,26,4,2,32))
if mibBuilder.loadTexts:pm1005CntupRdErrCntTable.setStatus(_A)
_Pm1005CntupRdErrCntEntry_Object=MibTableRow
pm1005CntupRdErrCntEntry=_Pm1005CntupRdErrCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,32,1))
pm1005CntupRdErrCntEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm1005CntupRdErrCntEntry.setStatus(_A)
class _Pm1005CntupRdErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntupRdErrCntIndex_Type.__name__=_D
_Pm1005CntupRdErrCntIndex_Object=MibTableColumn
pm1005CntupRdErrCntIndex=_Pm1005CntupRdErrCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,32,1,1),_Pm1005CntupRdErrCntIndex_Type())
pm1005CntupRdErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRdErrCntIndex.setStatus(_A)
_Pm1005CntupRdErrCntValuePortn_Type=Counter32
_Pm1005CntupRdErrCntValuePortn_Object=MibTableColumn
pm1005CntupRdErrCntValuePortn=_Pm1005CntupRdErrCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,32,1,2),_Pm1005CntupRdErrCntValuePortn_Type())
pm1005CntupRdErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRdErrCntValuePortn.setStatus(_A)
_Pm1005CntupRdErrCntErrorPortn_Type=EkiOnOff
_Pm1005CntupRdErrCntErrorPortn_Object=MibTableColumn
pm1005CntupRdErrCntErrorPortn=_Pm1005CntupRdErrCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,32,1,3),_Pm1005CntupRdErrCntErrorPortn_Type())
pm1005CntupRdErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRdErrCntErrorPortn.setStatus(_A)
_Pm1005CntupRdErrCntOverloadPortn_Type=EkiOnOff
_Pm1005CntupRdErrCntOverloadPortn_Object=MibTableColumn
pm1005CntupRdErrCntOverloadPortn=_Pm1005CntupRdErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,32,1,4),_Pm1005CntupRdErrCntOverloadPortn_Type())
pm1005CntupRdErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupRdErrCntOverloadPortn.setStatus(_A)
_Pm1005CntupTimCntTable_Object=MibTable
pm1005CntupTimCntTable=_Pm1005CntupTimCntTable_Object((1,3,6,1,4,1,20044,26,4,2,40))
if mibBuilder.loadTexts:pm1005CntupTimCntTable.setStatus(_A)
_Pm1005CntupTimCntEntry_Object=MibTableRow
pm1005CntupTimCntEntry=_Pm1005CntupTimCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,40,1))
pm1005CntupTimCntEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm1005CntupTimCntEntry.setStatus(_A)
class _Pm1005CntupTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntupTimCntIndex_Type.__name__=_D
_Pm1005CntupTimCntIndex_Object=MibTableColumn
pm1005CntupTimCntIndex=_Pm1005CntupTimCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,40,1,1),_Pm1005CntupTimCntIndex_Type())
pm1005CntupTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupTimCntIndex.setStatus(_A)
_Pm1005CntupTimCntValuePortn_Type=Counter32
_Pm1005CntupTimCntValuePortn_Object=MibTableColumn
pm1005CntupTimCntValuePortn=_Pm1005CntupTimCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,40,1,2),_Pm1005CntupTimCntValuePortn_Type())
pm1005CntupTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupTimCntValuePortn.setStatus(_A)
_Pm1005CntupTimCntErrorPortn_Type=EkiOnOff
_Pm1005CntupTimCntErrorPortn_Object=MibTableColumn
pm1005CntupTimCntErrorPortn=_Pm1005CntupTimCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,40,1,3),_Pm1005CntupTimCntErrorPortn_Type())
pm1005CntupTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupTimCntErrorPortn.setStatus(_A)
_Pm1005CntupTimCntOverloadPortn_Type=EkiOnOff
_Pm1005CntupTimCntOverloadPortn_Object=MibTableColumn
pm1005CntupTimCntOverloadPortn=_Pm1005CntupTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,40,1,4),_Pm1005CntupTimCntOverloadPortn_Type())
pm1005CntupTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupTimCntOverloadPortn.setStatus(_A)
_Pm1005CntupCvErrCntTable_Object=MibTable
pm1005CntupCvErrCntTable=_Pm1005CntupCvErrCntTable_Object((1,3,6,1,4,1,20044,26,4,2,48))
if mibBuilder.loadTexts:pm1005CntupCvErrCntTable.setStatus(_A)
_Pm1005CntupCvErrCntEntry_Object=MibTableRow
pm1005CntupCvErrCntEntry=_Pm1005CntupCvErrCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,48,1))
pm1005CntupCvErrCntEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pm1005CntupCvErrCntEntry.setStatus(_A)
class _Pm1005CntupCvErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntupCvErrCntIndex_Type.__name__=_D
_Pm1005CntupCvErrCntIndex_Object=MibTableColumn
pm1005CntupCvErrCntIndex=_Pm1005CntupCvErrCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,48,1,1),_Pm1005CntupCvErrCntIndex_Type())
pm1005CntupCvErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupCvErrCntIndex.setStatus(_A)
_Pm1005CntupCvErrCntValuePortn_Type=Counter32
_Pm1005CntupCvErrCntValuePortn_Object=MibTableColumn
pm1005CntupCvErrCntValuePortn=_Pm1005CntupCvErrCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,48,1,2),_Pm1005CntupCvErrCntValuePortn_Type())
pm1005CntupCvErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupCvErrCntValuePortn.setStatus(_A)
_Pm1005CntupCvErrCntErrorPortn_Type=EkiOnOff
_Pm1005CntupCvErrCntErrorPortn_Object=MibTableColumn
pm1005CntupCvErrCntErrorPortn=_Pm1005CntupCvErrCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,48,1,3),_Pm1005CntupCvErrCntErrorPortn_Type())
pm1005CntupCvErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupCvErrCntErrorPortn.setStatus(_A)
_Pm1005CntupCvErrCntOverloadPortn_Type=EkiOnOff
_Pm1005CntupCvErrCntOverloadPortn_Object=MibTableColumn
pm1005CntupCvErrCntOverloadPortn=_Pm1005CntupCvErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,48,1,4),_Pm1005CntupCvErrCntOverloadPortn_Type())
pm1005CntupCvErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntupCvErrCntOverloadPortn.setStatus(_A)
_Pm1005CntdwCbipCntTable_Object=MibTable
pm1005CntdwCbipCntTable=_Pm1005CntdwCbipCntTable_Object((1,3,6,1,4,1,20044,26,4,2,64))
if mibBuilder.loadTexts:pm1005CntdwCbipCntTable.setStatus(_A)
_Pm1005CntdwCbipCntEntry_Object=MibTableRow
pm1005CntdwCbipCntEntry=_Pm1005CntdwCbipCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,64,1))
pm1005CntdwCbipCntEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pm1005CntdwCbipCntEntry.setStatus(_A)
class _Pm1005CntdwCbipCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntdwCbipCntIndex_Type.__name__=_D
_Pm1005CntdwCbipCntIndex_Object=MibTableColumn
pm1005CntdwCbipCntIndex=_Pm1005CntdwCbipCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,64,1,1),_Pm1005CntdwCbipCntIndex_Type())
pm1005CntdwCbipCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwCbipCntIndex.setStatus(_A)
_Pm1005CntdwCbipCntValuePortn_Type=Counter32
_Pm1005CntdwCbipCntValuePortn_Object=MibTableColumn
pm1005CntdwCbipCntValuePortn=_Pm1005CntdwCbipCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,64,1,2),_Pm1005CntdwCbipCntValuePortn_Type())
pm1005CntdwCbipCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwCbipCntValuePortn.setStatus(_A)
_Pm1005CntdwCbipCntErrorPortn_Type=EkiOnOff
_Pm1005CntdwCbipCntErrorPortn_Object=MibTableColumn
pm1005CntdwCbipCntErrorPortn=_Pm1005CntdwCbipCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,64,1,3),_Pm1005CntdwCbipCntErrorPortn_Type())
pm1005CntdwCbipCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwCbipCntErrorPortn.setStatus(_A)
_Pm1005CntdwCbipCntOverloadPortn_Type=EkiOnOff
_Pm1005CntdwCbipCntOverloadPortn_Object=MibTableColumn
pm1005CntdwCbipCntOverloadPortn=_Pm1005CntdwCbipCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,64,1,4),_Pm1005CntdwCbipCntOverloadPortn_Type())
pm1005CntdwCbipCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwCbipCntOverloadPortn.setStatus(_A)
_Pm1005CntdwTimCntTable_Object=MibTable
pm1005CntdwTimCntTable=_Pm1005CntdwTimCntTable_Object((1,3,6,1,4,1,20044,26,4,2,72))
if mibBuilder.loadTexts:pm1005CntdwTimCntTable.setStatus(_A)
_Pm1005CntdwTimCntEntry_Object=MibTableRow
pm1005CntdwTimCntEntry=_Pm1005CntdwTimCntEntry_Object((1,3,6,1,4,1,20044,26,4,2,72,1))
pm1005CntdwTimCntEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pm1005CntdwTimCntEntry.setStatus(_A)
class _Pm1005CntdwTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntdwTimCntIndex_Type.__name__=_D
_Pm1005CntdwTimCntIndex_Object=MibTableColumn
pm1005CntdwTimCntIndex=_Pm1005CntdwTimCntIndex_Object((1,3,6,1,4,1,20044,26,4,2,72,1,1),_Pm1005CntdwTimCntIndex_Type())
pm1005CntdwTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwTimCntIndex.setStatus(_A)
_Pm1005CntdwTimCntValuePortn_Type=Counter32
_Pm1005CntdwTimCntValuePortn_Object=MibTableColumn
pm1005CntdwTimCntValuePortn=_Pm1005CntdwTimCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,2,72,1,2),_Pm1005CntdwTimCntValuePortn_Type())
pm1005CntdwTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwTimCntValuePortn.setStatus(_A)
_Pm1005CntdwTimCntErrorPortn_Type=EkiOnOff
_Pm1005CntdwTimCntErrorPortn_Object=MibTableColumn
pm1005CntdwTimCntErrorPortn=_Pm1005CntdwTimCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,2,72,1,3),_Pm1005CntdwTimCntErrorPortn_Type())
pm1005CntdwTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwTimCntErrorPortn.setStatus(_A)
_Pm1005CntdwTimCntOverloadPortn_Type=EkiOnOff
_Pm1005CntdwTimCntOverloadPortn_Object=MibTableColumn
pm1005CntdwTimCntOverloadPortn=_Pm1005CntdwTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,2,72,1,4),_Pm1005CntdwTimCntOverloadPortn_Type())
pm1005CntdwTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdwTimCntOverloadPortn.setStatus(_A)
_Pm1005CntLine_ObjectIdentity=ObjectIdentity
pm1005CntLine=_Pm1005CntLine_ObjectIdentity((1,3,6,1,4,1,20044,26,4,3))
_Pm1005CntdfrmB1ErrCntTable_Object=MibTable
pm1005CntdfrmB1ErrCntTable=_Pm1005CntdfrmB1ErrCntTable_Object((1,3,6,1,4,1,20044,26,4,3,152))
if mibBuilder.loadTexts:pm1005CntdfrmB1ErrCntTable.setStatus(_A)
_Pm1005CntdfrmB1ErrCntEntry_Object=MibTableRow
pm1005CntdfrmB1ErrCntEntry=_Pm1005CntdfrmB1ErrCntEntry_Object((1,3,6,1,4,1,20044,26,4,3,152,1))
pm1005CntdfrmB1ErrCntEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pm1005CntdfrmB1ErrCntEntry.setStatus(_A)
class _Pm1005CntdfrmB1ErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntdfrmB1ErrCntIndex_Type.__name__=_D
_Pm1005CntdfrmB1ErrCntIndex_Object=MibTableColumn
pm1005CntdfrmB1ErrCntIndex=_Pm1005CntdfrmB1ErrCntIndex_Object((1,3,6,1,4,1,20044,26,4,3,152,1,1),_Pm1005CntdfrmB1ErrCntIndex_Type())
pm1005CntdfrmB1ErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmB1ErrCntIndex.setStatus(_A)
_Pm1005CntdfrmB1ErrCntValuePortn_Type=Counter32
_Pm1005CntdfrmB1ErrCntValuePortn_Object=MibTableColumn
pm1005CntdfrmB1ErrCntValuePortn=_Pm1005CntdfrmB1ErrCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,3,152,1,2),_Pm1005CntdfrmB1ErrCntValuePortn_Type())
pm1005CntdfrmB1ErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmB1ErrCntValuePortn.setStatus(_A)
_Pm1005CntdfrmB1ErrCntErrorPortn_Type=EkiOnOff
_Pm1005CntdfrmB1ErrCntErrorPortn_Object=MibTableColumn
pm1005CntdfrmB1ErrCntErrorPortn=_Pm1005CntdfrmB1ErrCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,3,152,1,3),_Pm1005CntdfrmB1ErrCntErrorPortn_Type())
pm1005CntdfrmB1ErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmB1ErrCntErrorPortn.setStatus(_A)
_Pm1005CntdfrmB1ErrCntOverloadPortn_Type=EkiOnOff
_Pm1005CntdfrmB1ErrCntOverloadPortn_Object=MibTableColumn
pm1005CntdfrmB1ErrCntOverloadPortn=_Pm1005CntdfrmB1ErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,3,152,1,4),_Pm1005CntdfrmB1ErrCntOverloadPortn_Type())
pm1005CntdfrmB1ErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmB1ErrCntOverloadPortn.setStatus(_A)
_Pm1005CntdfrmTimCntTable_Object=MibTable
pm1005CntdfrmTimCntTable=_Pm1005CntdfrmTimCntTable_Object((1,3,6,1,4,1,20044,26,4,3,153))
if mibBuilder.loadTexts:pm1005CntdfrmTimCntTable.setStatus(_A)
_Pm1005CntdfrmTimCntEntry_Object=MibTableRow
pm1005CntdfrmTimCntEntry=_Pm1005CntdfrmTimCntEntry_Object((1,3,6,1,4,1,20044,26,4,3,153,1))
pm1005CntdfrmTimCntEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pm1005CntdfrmTimCntEntry.setStatus(_A)
class _Pm1005CntdfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntdfrmTimCntIndex_Type.__name__=_D
_Pm1005CntdfrmTimCntIndex_Object=MibTableColumn
pm1005CntdfrmTimCntIndex=_Pm1005CntdfrmTimCntIndex_Object((1,3,6,1,4,1,20044,26,4,3,153,1,1),_Pm1005CntdfrmTimCntIndex_Type())
pm1005CntdfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmTimCntIndex.setStatus(_A)
_Pm1005CntdfrmTimCntValuePortn_Type=Counter32
_Pm1005CntdfrmTimCntValuePortn_Object=MibTableColumn
pm1005CntdfrmTimCntValuePortn=_Pm1005CntdfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,3,153,1,2),_Pm1005CntdfrmTimCntValuePortn_Type())
pm1005CntdfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmTimCntValuePortn.setStatus(_A)
_Pm1005CntdfrmTimCntErrorPortn_Type=EkiOnOff
_Pm1005CntdfrmTimCntErrorPortn_Object=MibTableColumn
pm1005CntdfrmTimCntErrorPortn=_Pm1005CntdfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,3,153,1,3),_Pm1005CntdfrmTimCntErrorPortn_Type())
pm1005CntdfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmTimCntErrorPortn.setStatus(_A)
_Pm1005CntdfrmTimCntOverloadPortn_Type=EkiOnOff
_Pm1005CntdfrmTimCntOverloadPortn_Object=MibTableColumn
pm1005CntdfrmTimCntOverloadPortn=_Pm1005CntdfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,3,153,1,4),_Pm1005CntdfrmTimCntOverloadPortn_Type())
pm1005CntdfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmTimCntOverloadPortn.setStatus(_A)
_Pm1005CntdfrmPrimLineErrCntTable_Object=MibTable
pm1005CntdfrmPrimLineErrCntTable=_Pm1005CntdfrmPrimLineErrCntTable_Object((1,3,6,1,4,1,20044,26,4,3,154))
if mibBuilder.loadTexts:pm1005CntdfrmPrimLineErrCntTable.setStatus(_A)
_Pm1005CntdfrmPrimLineErrCntEntry_Object=MibTableRow
pm1005CntdfrmPrimLineErrCntEntry=_Pm1005CntdfrmPrimLineErrCntEntry_Object((1,3,6,1,4,1,20044,26,4,3,154,1))
pm1005CntdfrmPrimLineErrCntEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pm1005CntdfrmPrimLineErrCntEntry.setStatus(_A)
class _Pm1005CntdfrmPrimLineErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CntdfrmPrimLineErrCntIndex_Type.__name__=_D
_Pm1005CntdfrmPrimLineErrCntIndex_Object=MibTableColumn
pm1005CntdfrmPrimLineErrCntIndex=_Pm1005CntdfrmPrimLineErrCntIndex_Object((1,3,6,1,4,1,20044,26,4,3,154,1,1),_Pm1005CntdfrmPrimLineErrCntIndex_Type())
pm1005CntdfrmPrimLineErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmPrimLineErrCntIndex.setStatus(_A)
_Pm1005CntdfrmPrimLineErrCntValuePortn_Type=Counter32
_Pm1005CntdfrmPrimLineErrCntValuePortn_Object=MibTableColumn
pm1005CntdfrmPrimLineErrCntValuePortn=_Pm1005CntdfrmPrimLineErrCntValuePortn_Object((1,3,6,1,4,1,20044,26,4,3,154,1,2),_Pm1005CntdfrmPrimLineErrCntValuePortn_Type())
pm1005CntdfrmPrimLineErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmPrimLineErrCntValuePortn.setStatus(_A)
_Pm1005CntdfrmPrimLineErrCntErrorPortn_Type=EkiOnOff
_Pm1005CntdfrmPrimLineErrCntErrorPortn_Object=MibTableColumn
pm1005CntdfrmPrimLineErrCntErrorPortn=_Pm1005CntdfrmPrimLineErrCntErrorPortn_Object((1,3,6,1,4,1,20044,26,4,3,154,1,3),_Pm1005CntdfrmPrimLineErrCntErrorPortn_Type())
pm1005CntdfrmPrimLineErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmPrimLineErrCntErrorPortn.setStatus(_A)
_Pm1005CntdfrmPrimLineErrCntOverloadPortn_Type=EkiOnOff
_Pm1005CntdfrmPrimLineErrCntOverloadPortn_Object=MibTableColumn
pm1005CntdfrmPrimLineErrCntOverloadPortn=_Pm1005CntdfrmPrimLineErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,4,3,154,1,4),_Pm1005CntdfrmPrimLineErrCntOverloadPortn_Type())
pm1005CntdfrmPrimLineErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CntdfrmPrimLineErrCntOverloadPortn.setStatus(_A)
_Pm1005CntCountersReset_Type=EkiOnOff
_Pm1005CntCountersReset_Object=MibScalar
pm1005CntCountersReset=_Pm1005CntCountersReset_Object((1,3,6,1,4,1,20044,26,4,259),_Pm1005CntCountersReset_Type())
pm1005CntCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CntCountersReset.setStatus(_A)
_Pm1005CntCountersStop_Type=EkiOnOff
_Pm1005CntCountersStop_Object=MibScalar
pm1005CntCountersStop=_Pm1005CntCountersStop_Object((1,3,6,1,4,1,20044,26,4,260),_Pm1005CntCountersStop_Type())
pm1005CntCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CntCountersStop.setStatus(_A)
_Pm1005controlsWrite_ObjectIdentity=ObjectIdentity
pm1005controlsWrite=_Pm1005controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,26,6))
_Pm1005CtrlOther_ObjectIdentity=ObjectIdentity
pm1005CtrlOther=_Pm1005CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1))
_Pm1005CtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pm1005CtrlconfMgnt1=_Pm1005CtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,1))
_Pm1005CtrlConf1Load1_Type=EkiOnOff
_Pm1005CtrlConf1Load1_Object=MibScalar
pm1005CtrlConf1Load1=_Pm1005CtrlConf1Load1_Object((1,3,6,1,4,1,20044,26,6,1,1,1),_Pm1005CtrlConf1Load1_Type())
pm1005CtrlConf1Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlConf1Load1.setStatus(_A)
_Pm1005CtrlConf2Load1_Type=EkiOnOff
_Pm1005CtrlConf2Load1_Object=MibScalar
pm1005CtrlConf2Load1=_Pm1005CtrlConf2Load1_Object((1,3,6,1,4,1,20044,26,6,1,1,2),_Pm1005CtrlConf2Load1_Type())
pm1005CtrlConf2Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlConf2Load1.setStatus(_A)
_Pm1005CtrlConf2Flash1_Type=EkiOnOff
_Pm1005CtrlConf2Flash1_Object=MibScalar
pm1005CtrlConf2Flash1=_Pm1005CtrlConf2Flash1_Object((1,3,6,1,4,1,20044,26,6,1,1,10),_Pm1005CtrlConf2Flash1_Type())
pm1005CtrlConf2Flash1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlConf2Flash1.setStatus(_A)
_Pm1005CtrlConf2Clear1_Type=EkiOnOff
_Pm1005CtrlConf2Clear1_Object=MibScalar
pm1005CtrlConf2Clear1=_Pm1005CtrlConf2Clear1_Object((1,3,6,1,4,1,20044,26,6,1,1,14),_Pm1005CtrlConf2Clear1_Type())
pm1005CtrlConf2Clear1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlConf2Clear1.setStatus(_A)
_Pm1005Ctrlsynth4_ObjectIdentity=ObjectIdentity
pm1005Ctrlsynth4=_Pm1005Ctrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,4))
_Pm1005CtrlCorrelatOn_Type=EkiOnOff
_Pm1005CtrlCorrelatOn_Object=MibScalar
pm1005CtrlCorrelatOn=_Pm1005CtrlCorrelatOn_Object((1,3,6,1,4,1,20044,26,6,1,4,1),_Pm1005CtrlCorrelatOn_Type())
pm1005CtrlCorrelatOn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlCorrelatOn.setStatus(_A)
_Pm1005CtrlCorrelatOff_Type=EkiOnOff
_Pm1005CtrlCorrelatOff_Object=MibScalar
pm1005CtrlCorrelatOff=_Pm1005CtrlCorrelatOff_Object((1,3,6,1,4,1,20044,26,6,1,4,2),_Pm1005CtrlCorrelatOff_Type())
pm1005CtrlCorrelatOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlCorrelatOff.setStatus(_A)
_Pm1005CtrlswMgnt_ObjectIdentity=ObjectIdentity
pm1005CtrlswMgnt=_Pm1005CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,5))
_Pm1005CtrlColdReset_Type=EkiOnOff
_Pm1005CtrlColdReset_Object=MibScalar
pm1005CtrlColdReset=_Pm1005CtrlColdReset_Object((1,3,6,1,4,1,20044,26,6,1,5,2),_Pm1005CtrlColdReset_Type())
pm1005CtrlColdReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlColdReset.setStatus(_A)
_Pm1005CtrlWarmReset_Type=EkiOnOff
_Pm1005CtrlWarmReset_Object=MibScalar
pm1005CtrlWarmReset=_Pm1005CtrlWarmReset_Object((1,3,6,1,4,1,20044,26,6,1,5,3),_Pm1005CtrlWarmReset_Type())
pm1005CtrlWarmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlWarmReset.setStatus(_A)
_Pm1005CtrlLoadSwBank1_Type=EkiOnOff
_Pm1005CtrlLoadSwBank1_Object=MibScalar
pm1005CtrlLoadSwBank1=_Pm1005CtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,26,6,1,5,5),_Pm1005CtrlLoadSwBank1_Type())
pm1005CtrlLoadSwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLoadSwBank1.setStatus(_A)
_Pm1005CtrlLoadSwBank2_Type=EkiOnOff
_Pm1005CtrlLoadSwBank2_Object=MibScalar
pm1005CtrlLoadSwBank2=_Pm1005CtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,26,6,1,5,6),_Pm1005CtrlLoadSwBank2_Type())
pm1005CtrlLoadSwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLoadSwBank2.setStatus(_A)
_Pm1005CtrlgwMgnt_ObjectIdentity=ObjectIdentity
pm1005CtrlgwMgnt=_Pm1005CtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,6))
_Pm1005CtrlCurrentGwReset_Type=EkiOnOff
_Pm1005CtrlCurrentGwReset_Object=MibScalar
pm1005CtrlCurrentGwReset=_Pm1005CtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,26,6,1,6,1),_Pm1005CtrlCurrentGwReset_Type())
pm1005CtrlCurrentGwReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlCurrentGwReset.setStatus(_A)
_Pm1005CtrlLoadGwBank1_Type=EkiOnOff
_Pm1005CtrlLoadGwBank1_Object=MibScalar
pm1005CtrlLoadGwBank1=_Pm1005CtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,26,6,1,6,5),_Pm1005CtrlLoadGwBank1_Type())
pm1005CtrlLoadGwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLoadGwBank1.setStatus(_A)
_Pm1005CtrlLoadGwBank2_Type=EkiOnOff
_Pm1005CtrlLoadGwBank2_Object=MibScalar
pm1005CtrlLoadGwBank2=_Pm1005CtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,26,6,1,6,6),_Pm1005CtrlLoadGwBank2_Type())
pm1005CtrlLoadGwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLoadGwBank2.setStatus(_A)
_Pm1005CtrlLoadGwBank3_Type=EkiOnOff
_Pm1005CtrlLoadGwBank3_Object=MibScalar
pm1005CtrlLoadGwBank3=_Pm1005CtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,26,6,1,6,7),_Pm1005CtrlLoadGwBank3_Type())
pm1005CtrlLoadGwBank3.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLoadGwBank3.setStatus(_A)
_Pm1005CtrlLoadGwBank4_Type=EkiOnOff
_Pm1005CtrlLoadGwBank4_Object=MibScalar
pm1005CtrlLoadGwBank4=_Pm1005CtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,26,6,1,6,8),_Pm1005CtrlLoadGwBank4_Type())
pm1005CtrlLoadGwBank4.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLoadGwBank4.setStatus(_A)
_Pm1005CtrlledTest_ObjectIdentity=ObjectIdentity
pm1005CtrlledTest=_Pm1005CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,192))
_Pm1005CtrlGreenLed_Type=EkiOnOff
_Pm1005CtrlGreenLed_Object=MibScalar
pm1005CtrlGreenLed=_Pm1005CtrlGreenLed_Object((1,3,6,1,4,1,20044,26,6,1,192,1),_Pm1005CtrlGreenLed_Type())
pm1005CtrlGreenLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlGreenLed.setStatus(_A)
_Pm1005CtrlRedLed_Type=EkiOnOff
_Pm1005CtrlRedLed_Object=MibScalar
pm1005CtrlRedLed=_Pm1005CtrlRedLed_Object((1,3,6,1,4,1,20044,26,6,1,192,2),_Pm1005CtrlRedLed_Type())
pm1005CtrlRedLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlRedLed.setStatus(_A)
_Pm1005CtrlLedOff_Type=EkiOnOff
_Pm1005CtrlLedOff_Object=MibScalar
pm1005CtrlLedOff=_Pm1005CtrlLedOff_Object((1,3,6,1,4,1,20044,26,6,1,192,3),_Pm1005CtrlLedOff_Type())
pm1005CtrlLedOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLedOff.setStatus(_A)
_Pm1005CtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm1005CtrlmoduleOosMode=_Pm1005CtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,193))
_Pm1005CtrlModuleOosMode_Type=EkiOnOff
_Pm1005CtrlModuleOosMode_Object=MibScalar
pm1005CtrlModuleOosMode=_Pm1005CtrlModuleOosMode_Object((1,3,6,1,4,1,20044,26,6,1,193,1),_Pm1005CtrlModuleOosMode_Type())
pm1005CtrlModuleOosMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlModuleOosMode.setStatus(_A)
_Pm1005CtrlmaintenanceMode_ObjectIdentity=ObjectIdentity
pm1005CtrlmaintenanceMode=_Pm1005CtrlmaintenanceMode_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,197))
_Pm1005CtrlMaintenanceMode_Type=EkiOnOff
_Pm1005CtrlMaintenanceMode_Object=MibScalar
pm1005CtrlMaintenanceMode=_Pm1005CtrlMaintenanceMode_Object((1,3,6,1,4,1,20044,26,6,1,197,1),_Pm1005CtrlMaintenanceMode_Type())
pm1005CtrlMaintenanceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlMaintenanceMode.setStatus(_A)
_Pm1005CtrldccEnable_ObjectIdentity=ObjectIdentity
pm1005CtrldccEnable=_Pm1005CtrldccEnable_ObjectIdentity((1,3,6,1,4,1,20044,26,6,1,198))
_Pm1005CtrlDccEnable_Type=EkiOnOff
_Pm1005CtrlDccEnable_Object=MibScalar
pm1005CtrlDccEnable=_Pm1005CtrlDccEnable_Object((1,3,6,1,4,1,20044,26,6,1,198,1),_Pm1005CtrlDccEnable_Type())
pm1005CtrlDccEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlDccEnable.setStatus(_A)
_Pm1005CtrlClient_ObjectIdentity=ObjectIdentity
pm1005CtrlClient=_Pm1005CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,26,6,2))
_Pm1005CtrlaccessLoopTable_Object=MibTable
pm1005CtrlaccessLoopTable=_Pm1005CtrlaccessLoopTable_Object((1,3,6,1,4,1,20044,26,6,2,16))
if mibBuilder.loadTexts:pm1005CtrlaccessLoopTable.setStatus(_A)
_Pm1005CtrlaccessLoopEntry_Object=MibTableRow
pm1005CtrlaccessLoopEntry=_Pm1005CtrlaccessLoopEntry_Object((1,3,6,1,4,1,20044,26,6,2,16,1))
pm1005CtrlaccessLoopEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pm1005CtrlaccessLoopEntry.setStatus(_A)
class _Pm1005CtrlaccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlaccessLoopIndex_Type.__name__=_D
_Pm1005CtrlaccessLoopIndex_Object=MibTableColumn
pm1005CtrlaccessLoopIndex=_Pm1005CtrlaccessLoopIndex_Object((1,3,6,1,4,1,20044,26,6,2,16,1,1),_Pm1005CtrlaccessLoopIndex_Type())
pm1005CtrlaccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlaccessLoopIndex.setStatus(_A)
_Pm1005CtrlaccessLoopPortn_Type=EkiState
_Pm1005CtrlaccessLoopPortn_Object=MibTableColumn
pm1005CtrlaccessLoopPortn=_Pm1005CtrlaccessLoopPortn_Object((1,3,6,1,4,1,20044,26,6,2,16,1,2),_Pm1005CtrlaccessLoopPortn_Type())
pm1005CtrlaccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlaccessLoopPortn.setStatus(_A)
_Pm1005CtrlportOosModeTable_Object=MibTable
pm1005CtrlportOosModeTable=_Pm1005CtrlportOosModeTable_Object((1,3,6,1,4,1,20044,26,6,2,18))
if mibBuilder.loadTexts:pm1005CtrlportOosModeTable.setStatus(_A)
_Pm1005CtrlportOosModeEntry_Object=MibTableRow
pm1005CtrlportOosModeEntry=_Pm1005CtrlportOosModeEntry_Object((1,3,6,1,4,1,20044,26,6,2,18,1))
pm1005CtrlportOosModeEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pm1005CtrlportOosModeEntry.setStatus(_A)
class _Pm1005CtrlportOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlportOosModeIndex_Type.__name__=_D
_Pm1005CtrlportOosModeIndex_Object=MibTableColumn
pm1005CtrlportOosModeIndex=_Pm1005CtrlportOosModeIndex_Object((1,3,6,1,4,1,20044,26,6,2,18,1,1),_Pm1005CtrlportOosModeIndex_Type())
pm1005CtrlportOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlportOosModeIndex.setStatus(_A)
_Pm1005CtrlportOosModePortn_Type=EkiState
_Pm1005CtrlportOosModePortn_Object=MibTableColumn
pm1005CtrlportOosModePortn=_Pm1005CtrlportOosModePortn_Object((1,3,6,1,4,1,20044,26,6,2,18,1,2),_Pm1005CtrlportOosModePortn_Type())
pm1005CtrlportOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlportOosModePortn.setStatus(_A)
_Pm1005CtrlsfpOnCtrlTable_Object=MibTable
pm1005CtrlsfpOnCtrlTable=_Pm1005CtrlsfpOnCtrlTable_Object((1,3,6,1,4,1,20044,26,6,2,19))
if mibBuilder.loadTexts:pm1005CtrlsfpOnCtrlTable.setStatus(_A)
_Pm1005CtrlsfpOnCtrlEntry_Object=MibTableRow
pm1005CtrlsfpOnCtrlEntry=_Pm1005CtrlsfpOnCtrlEntry_Object((1,3,6,1,4,1,20044,26,6,2,19,1))
pm1005CtrlsfpOnCtrlEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pm1005CtrlsfpOnCtrlEntry.setStatus(_A)
class _Pm1005CtrlsfpOnCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlsfpOnCtrlIndex_Type.__name__=_D
_Pm1005CtrlsfpOnCtrlIndex_Object=MibTableColumn
pm1005CtrlsfpOnCtrlIndex=_Pm1005CtrlsfpOnCtrlIndex_Object((1,3,6,1,4,1,20044,26,6,2,19,1,1),_Pm1005CtrlsfpOnCtrlIndex_Type())
pm1005CtrlsfpOnCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlsfpOnCtrlIndex.setStatus(_A)
_Pm1005CtrlsfpOnCtrlPortn_Type=EkiState
_Pm1005CtrlsfpOnCtrlPortn_Object=MibTableColumn
pm1005CtrlsfpOnCtrlPortn=_Pm1005CtrlsfpOnCtrlPortn_Object((1,3,6,1,4,1,20044,26,6,2,19,1,2),_Pm1005CtrlsfpOnCtrlPortn_Type())
pm1005CtrlsfpOnCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlsfpOnCtrlPortn.setStatus(_A)
_Pm1005CtrlsfpOffCtrlTable_Object=MibTable
pm1005CtrlsfpOffCtrlTable=_Pm1005CtrlsfpOffCtrlTable_Object((1,3,6,1,4,1,20044,26,6,2,20))
if mibBuilder.loadTexts:pm1005CtrlsfpOffCtrlTable.setStatus(_A)
_Pm1005CtrlsfpOffCtrlEntry_Object=MibTableRow
pm1005CtrlsfpOffCtrlEntry=_Pm1005CtrlsfpOffCtrlEntry_Object((1,3,6,1,4,1,20044,26,6,2,20,1))
pm1005CtrlsfpOffCtrlEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pm1005CtrlsfpOffCtrlEntry.setStatus(_A)
class _Pm1005CtrlsfpOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlsfpOffCtrlIndex_Type.__name__=_D
_Pm1005CtrlsfpOffCtrlIndex_Object=MibTableColumn
pm1005CtrlsfpOffCtrlIndex=_Pm1005CtrlsfpOffCtrlIndex_Object((1,3,6,1,4,1,20044,26,6,2,20,1,1),_Pm1005CtrlsfpOffCtrlIndex_Type())
pm1005CtrlsfpOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlsfpOffCtrlIndex.setStatus(_A)
_Pm1005CtrlsfpOffCtrlPortn_Type=EkiState
_Pm1005CtrlsfpOffCtrlPortn_Object=MibTableColumn
pm1005CtrlsfpOffCtrlPortn=_Pm1005CtrlsfpOffCtrlPortn_Object((1,3,6,1,4,1,20044,26,6,2,20,1,2),_Pm1005CtrlsfpOffCtrlPortn_Type())
pm1005CtrlsfpOffCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlsfpOffCtrlPortn.setStatus(_A)
_Pm1005CtrlcsfUpInsTable_Object=MibTable
pm1005CtrlcsfUpInsTable=_Pm1005CtrlcsfUpInsTable_Object((1,3,6,1,4,1,20044,26,6,2,21))
if mibBuilder.loadTexts:pm1005CtrlcsfUpInsTable.setStatus(_A)
_Pm1005CtrlcsfUpInsEntry_Object=MibTableRow
pm1005CtrlcsfUpInsEntry=_Pm1005CtrlcsfUpInsEntry_Object((1,3,6,1,4,1,20044,26,6,2,21,1))
pm1005CtrlcsfUpInsEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pm1005CtrlcsfUpInsEntry.setStatus(_A)
class _Pm1005CtrlcsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlcsfUpInsIndex_Type.__name__=_D
_Pm1005CtrlcsfUpInsIndex_Object=MibTableColumn
pm1005CtrlcsfUpInsIndex=_Pm1005CtrlcsfUpInsIndex_Object((1,3,6,1,4,1,20044,26,6,2,21,1,1),_Pm1005CtrlcsfUpInsIndex_Type())
pm1005CtrlcsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlcsfUpInsIndex.setStatus(_A)
_Pm1005CtrlcsfUpInsPortn_Type=EkiState
_Pm1005CtrlcsfUpInsPortn_Object=MibTableColumn
pm1005CtrlcsfUpInsPortn=_Pm1005CtrlcsfUpInsPortn_Object((1,3,6,1,4,1,20044,26,6,2,21,1,2),_Pm1005CtrlcsfUpInsPortn_Type())
pm1005CtrlcsfUpInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlcsfUpInsPortn.setStatus(_A)
_Pm1005CtrlcaisDwInsTable_Object=MibTable
pm1005CtrlcaisDwInsTable=_Pm1005CtrlcaisDwInsTable_Object((1,3,6,1,4,1,20044,26,6,2,22))
if mibBuilder.loadTexts:pm1005CtrlcaisDwInsTable.setStatus(_A)
_Pm1005CtrlcaisDwInsEntry_Object=MibTableRow
pm1005CtrlcaisDwInsEntry=_Pm1005CtrlcaisDwInsEntry_Object((1,3,6,1,4,1,20044,26,6,2,22,1))
pm1005CtrlcaisDwInsEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pm1005CtrlcaisDwInsEntry.setStatus(_A)
class _Pm1005CtrlcaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlcaisDwInsIndex_Type.__name__=_D
_Pm1005CtrlcaisDwInsIndex_Object=MibTableColumn
pm1005CtrlcaisDwInsIndex=_Pm1005CtrlcaisDwInsIndex_Object((1,3,6,1,4,1,20044,26,6,2,22,1,1),_Pm1005CtrlcaisDwInsIndex_Type())
pm1005CtrlcaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlcaisDwInsIndex.setStatus(_A)
_Pm1005CtrlcaisDwInsPortn_Type=EkiState
_Pm1005CtrlcaisDwInsPortn_Object=MibTableColumn
pm1005CtrlcaisDwInsPortn=_Pm1005CtrlcaisDwInsPortn_Object((1,3,6,1,4,1,20044,26,6,2,22,1,2),_Pm1005CtrlcaisDwInsPortn_Type())
pm1005CtrlcaisDwInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlcaisDwInsPortn.setStatus(_A)
_Pm1005CtrlclientAccessTermLoopTable_Object=MibTable
pm1005CtrlclientAccessTermLoopTable=_Pm1005CtrlclientAccessTermLoopTable_Object((1,3,6,1,4,1,20044,26,6,2,26))
if mibBuilder.loadTexts:pm1005CtrlclientAccessTermLoopTable.setStatus(_A)
_Pm1005CtrlclientAccessTermLoopEntry_Object=MibTableRow
pm1005CtrlclientAccessTermLoopEntry=_Pm1005CtrlclientAccessTermLoopEntry_Object((1,3,6,1,4,1,20044,26,6,2,26,1))
pm1005CtrlclientAccessTermLoopEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pm1005CtrlclientAccessTermLoopEntry.setStatus(_A)
class _Pm1005CtrlclientAccessTermLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlclientAccessTermLoopIndex_Type.__name__=_D
_Pm1005CtrlclientAccessTermLoopIndex_Object=MibTableColumn
pm1005CtrlclientAccessTermLoopIndex=_Pm1005CtrlclientAccessTermLoopIndex_Object((1,3,6,1,4,1,20044,26,6,2,26,1,1),_Pm1005CtrlclientAccessTermLoopIndex_Type())
pm1005CtrlclientAccessTermLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlclientAccessTermLoopIndex.setStatus(_A)
_Pm1005CtrlclientAccessTermLoopPortn_Type=EkiState
_Pm1005CtrlclientAccessTermLoopPortn_Object=MibTableColumn
pm1005CtrlclientAccessTermLoopPortn=_Pm1005CtrlclientAccessTermLoopPortn_Object((1,3,6,1,4,1,20044,26,6,2,26,1,2),_Pm1005CtrlclientAccessTermLoopPortn_Type())
pm1005CtrlclientAccessTermLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlclientAccessTermLoopPortn.setStatus(_A)
_Pm1005CtrlprotocolTable_Object=MibTable
pm1005CtrlprotocolTable=_Pm1005CtrlprotocolTable_Object((1,3,6,1,4,1,20044,26,6,2,48))
if mibBuilder.loadTexts:pm1005CtrlprotocolTable.setStatus(_A)
_Pm1005CtrlprotocolEntry_Object=MibTableRow
pm1005CtrlprotocolEntry=_Pm1005CtrlprotocolEntry_Object((1,3,6,1,4,1,20044,26,6,2,48,1))
pm1005CtrlprotocolEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pm1005CtrlprotocolEntry.setStatus(_A)
class _Pm1005CtrlprotocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlprotocolIndex_Type.__name__=_D
_Pm1005CtrlprotocolIndex_Object=MibTableColumn
pm1005CtrlprotocolIndex=_Pm1005CtrlprotocolIndex_Object((1,3,6,1,4,1,20044,26,6,2,48,1,1),_Pm1005CtrlprotocolIndex_Type())
pm1005CtrlprotocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlprotocolIndex.setStatus(_A)
_Pm1005CtrlprotocolPortn_Type=EkiProtocol
_Pm1005CtrlprotocolPortn_Object=MibTableColumn
pm1005CtrlprotocolPortn=_Pm1005CtrlprotocolPortn_Object((1,3,6,1,4,1,20044,26,6,2,48,1,2),_Pm1005CtrlprotocolPortn_Type())
pm1005CtrlprotocolPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlprotocolPortn.setStatus(_A)
_Pm1005CtrlLine_ObjectIdentity=ObjectIdentity
pm1005CtrlLine=_Pm1005CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,26,6,3))
_Pm1005CtrlcommAccessLoop_ObjectIdentity=ObjectIdentity
pm1005CtrlcommAccessLoop=_Pm1005CtrlcommAccessLoop_ObjectIdentity((1,3,6,1,4,1,20044,26,6,3,64))
_Pm1005CtrlCommAccessloop_Type=EkiOnOff
_Pm1005CtrlCommAccessloop_Object=MibScalar
pm1005CtrlCommAccessloop=_Pm1005CtrlCommAccessloop_Object((1,3,6,1,4,1,20044,26,6,3,64,1),_Pm1005CtrlCommAccessloop_Type())
pm1005CtrlCommAccessloop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlCommAccessloop.setStatus(_G)
_Pm1005CtrllineLoop_ObjectIdentity=ObjectIdentity
pm1005CtrllineLoop=_Pm1005CtrllineLoop_ObjectIdentity((1,3,6,1,4,1,20044,26,6,3,66))
_Pm1005CtrlLineLoop_Type=EkiOnOff
_Pm1005CtrlLineLoop_Object=MibScalar
pm1005CtrlLineLoop=_Pm1005CtrlLineLoop_Object((1,3,6,1,4,1,20044,26,6,3,66,1),_Pm1005CtrlLineLoop_Type())
pm1005CtrlLineLoop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLineLoop.setStatus(_G)
_Pm1005CtrlmsAis_ObjectIdentity=ObjectIdentity
pm1005CtrlmsAis=_Pm1005CtrlmsAis_ObjectIdentity((1,3,6,1,4,1,20044,26,6,3,67))
_Pm1005CtrlMsAis_Type=EkiOnOff
_Pm1005CtrlMsAis_Object=MibScalar
pm1005CtrlMsAis=_Pm1005CtrlMsAis_Object((1,3,6,1,4,1,20044,26,6,3,67,1),_Pm1005CtrlMsAis_Type())
pm1005CtrlMsAis.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlMsAis.setStatus(_A)
_Pm1005CtrlfecDisableTable_Object=MibTable
pm1005CtrlfecDisableTable=_Pm1005CtrlfecDisableTable_Object((1,3,6,1,4,1,20044,26,6,3,69))
if mibBuilder.loadTexts:pm1005CtrlfecDisableTable.setStatus(_A)
_Pm1005CtrlfecDisableEntry_Object=MibTableRow
pm1005CtrlfecDisableEntry=_Pm1005CtrlfecDisableEntry_Object((1,3,6,1,4,1,20044,26,6,3,69,1))
pm1005CtrlfecDisableEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pm1005CtrlfecDisableEntry.setStatus(_A)
class _Pm1005CtrlfecDisableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlfecDisableIndex_Type.__name__=_D
_Pm1005CtrlfecDisableIndex_Object=MibTableColumn
pm1005CtrlfecDisableIndex=_Pm1005CtrlfecDisableIndex_Object((1,3,6,1,4,1,20044,26,6,3,69,1,1),_Pm1005CtrlfecDisableIndex_Type())
pm1005CtrlfecDisableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlfecDisableIndex.setStatus(_A)
_Pm1005CtrlfecDisablePortn_Type=EkiState
_Pm1005CtrlfecDisablePortn_Object=MibTableColumn
pm1005CtrlfecDisablePortn=_Pm1005CtrlfecDisablePortn_Object((1,3,6,1,4,1,20044,26,6,3,69,1,2),_Pm1005CtrlfecDisablePortn_Type())
pm1005CtrlfecDisablePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlfecDisablePortn.setStatus(_A)
_Pm1005CtrlProtMgnt_ObjectIdentity=ObjectIdentity
pm1005CtrlProtMgnt=_Pm1005CtrlProtMgnt_ObjectIdentity((1,3,6,1,4,1,20044,26,6,3,73))
class _Pm1005CtrlLineNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pm1005CtrlLineNumber_Type.__name__=_F
_Pm1005CtrlLineNumber_Object=MibScalar
pm1005CtrlLineNumber=_Pm1005CtrlLineNumber_Object((1,3,6,1,4,1,20044,26,6,3,73,1),_Pm1005CtrlLineNumber_Type())
pm1005CtrlLineNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlLineNumber.setStatus(_A)
_Pm1005CtrlProtMode_Type=EkiMode
_Pm1005CtrlProtMode_Object=MibScalar
pm1005CtrlProtMode=_Pm1005CtrlProtMode_Object((1,3,6,1,4,1,20044,26,6,3,73,2),_Pm1005CtrlProtMode_Type())
pm1005CtrlProtMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlProtMode.setStatus(_A)
_Pm1005CtrllineOosModeTable_Object=MibTable
pm1005CtrllineOosModeTable=_Pm1005CtrllineOosModeTable_Object((1,3,6,1,4,1,20044,26,6,3,74))
if mibBuilder.loadTexts:pm1005CtrllineOosModeTable.setStatus(_A)
_Pm1005CtrllineOosModeEntry_Object=MibTableRow
pm1005CtrllineOosModeEntry=_Pm1005CtrllineOosModeEntry_Object((1,3,6,1,4,1,20044,26,6,3,74,1))
pm1005CtrllineOosModeEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pm1005CtrllineOosModeEntry.setStatus(_A)
class _Pm1005CtrllineOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrllineOosModeIndex_Type.__name__=_D
_Pm1005CtrllineOosModeIndex_Object=MibTableColumn
pm1005CtrllineOosModeIndex=_Pm1005CtrllineOosModeIndex_Object((1,3,6,1,4,1,20044,26,6,3,74,1,1),_Pm1005CtrllineOosModeIndex_Type())
pm1005CtrllineOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrllineOosModeIndex.setStatus(_A)
_Pm1005CtrllineOosModePortn_Type=EkiState
_Pm1005CtrllineOosModePortn_Object=MibTableColumn
pm1005CtrllineOosModePortn=_Pm1005CtrllineOosModePortn_Object((1,3,6,1,4,1,20044,26,6,3,74,1,2),_Pm1005CtrllineOosModePortn_Type())
pm1005CtrllineOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrllineOosModePortn.setStatus(_A)
_Pm1005CtrlxfpOnoffTable_Object=MibTable
pm1005CtrlxfpOnoffTable=_Pm1005CtrlxfpOnoffTable_Object((1,3,6,1,4,1,20044,26,6,3,208))
if mibBuilder.loadTexts:pm1005CtrlxfpOnoffTable.setStatus(_A)
_Pm1005CtrlxfpOnoffEntry_Object=MibTableRow
pm1005CtrlxfpOnoffEntry=_Pm1005CtrlxfpOnoffEntry_Object((1,3,6,1,4,1,20044,26,6,3,208,1))
pm1005CtrlxfpOnoffEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pm1005CtrlxfpOnoffEntry.setStatus(_A)
class _Pm1005CtrlxfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlxfpOnoffIndex_Type.__name__=_D
_Pm1005CtrlxfpOnoffIndex_Object=MibTableColumn
pm1005CtrlxfpOnoffIndex=_Pm1005CtrlxfpOnoffIndex_Object((1,3,6,1,4,1,20044,26,6,3,208,1,1),_Pm1005CtrlxfpOnoffIndex_Type())
pm1005CtrlxfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlxfpOnoffIndex.setStatus(_A)
_Pm1005CtrlxfpOnoffPortn_Type=EkiState
_Pm1005CtrlxfpOnoffPortn_Object=MibTableColumn
pm1005CtrlxfpOnoffPortn=_Pm1005CtrlxfpOnoffPortn_Object((1,3,6,1,4,1,20044,26,6,3,208,1,2),_Pm1005CtrlxfpOnoffPortn_Type())
pm1005CtrlxfpOnoffPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlxfpOnoffPortn.setStatus(_A)
_Pm1005CtrlxfpLineLoopTable_Object=MibTable
pm1005CtrlxfpLineLoopTable=_Pm1005CtrlxfpLineLoopTable_Object((1,3,6,1,4,1,20044,26,6,3,209))
if mibBuilder.loadTexts:pm1005CtrlxfpLineLoopTable.setStatus(_A)
_Pm1005CtrlxfpLineLoopEntry_Object=MibTableRow
pm1005CtrlxfpLineLoopEntry=_Pm1005CtrlxfpLineLoopEntry_Object((1,3,6,1,4,1,20044,26,6,3,209,1))
pm1005CtrlxfpLineLoopEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pm1005CtrlxfpLineLoopEntry.setStatus(_A)
class _Pm1005CtrlxfpLineLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlxfpLineLoopIndex_Type.__name__=_D
_Pm1005CtrlxfpLineLoopIndex_Object=MibTableColumn
pm1005CtrlxfpLineLoopIndex=_Pm1005CtrlxfpLineLoopIndex_Object((1,3,6,1,4,1,20044,26,6,3,209,1,1),_Pm1005CtrlxfpLineLoopIndex_Type())
pm1005CtrlxfpLineLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlxfpLineLoopIndex.setStatus(_A)
_Pm1005CtrlxfpLineLoopPortn_Type=EkiState
_Pm1005CtrlxfpLineLoopPortn_Object=MibTableColumn
pm1005CtrlxfpLineLoopPortn=_Pm1005CtrlxfpLineLoopPortn_Object((1,3,6,1,4,1,20044,26,6,3,209,1,2),_Pm1005CtrlxfpLineLoopPortn_Type())
pm1005CtrlxfpLineLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlxfpLineLoopPortn.setStatus(_A)
_Pm1005CtrlxfpXfiLoopTable_Object=MibTable
pm1005CtrlxfpXfiLoopTable=_Pm1005CtrlxfpXfiLoopTable_Object((1,3,6,1,4,1,20044,26,6,3,210))
if mibBuilder.loadTexts:pm1005CtrlxfpXfiLoopTable.setStatus(_A)
_Pm1005CtrlxfpXfiLoopEntry_Object=MibTableRow
pm1005CtrlxfpXfiLoopEntry=_Pm1005CtrlxfpXfiLoopEntry_Object((1,3,6,1,4,1,20044,26,6,3,210,1))
pm1005CtrlxfpXfiLoopEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pm1005CtrlxfpXfiLoopEntry.setStatus(_A)
class _Pm1005CtrlxfpXfiLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrlxfpXfiLoopIndex_Type.__name__=_D
_Pm1005CtrlxfpXfiLoopIndex_Object=MibTableColumn
pm1005CtrlxfpXfiLoopIndex=_Pm1005CtrlxfpXfiLoopIndex_Object((1,3,6,1,4,1,20044,26,6,3,210,1,1),_Pm1005CtrlxfpXfiLoopIndex_Type())
pm1005CtrlxfpXfiLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrlxfpXfiLoopIndex.setStatus(_A)
_Pm1005CtrlxfpXfiLoopPortn_Type=EkiState
_Pm1005CtrlxfpXfiLoopPortn_Object=MibTableColumn
pm1005CtrlxfpXfiLoopPortn=_Pm1005CtrlxfpXfiLoopPortn_Object((1,3,6,1,4,1,20044,26,6,3,210,1,2),_Pm1005CtrlxfpXfiLoopPortn_Type())
pm1005CtrlxfpXfiLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrlxfpXfiLoopPortn.setStatus(_A)
_Pm1005CtrllineTunableChannelTable_Object=MibTable
pm1005CtrllineTunableChannelTable=_Pm1005CtrllineTunableChannelTable_Object((1,3,6,1,4,1,20044,26,6,3,212))
if mibBuilder.loadTexts:pm1005CtrllineTunableChannelTable.setStatus(_A)
_Pm1005CtrllineTunableChannelEntry_Object=MibTableRow
pm1005CtrllineTunableChannelEntry=_Pm1005CtrllineTunableChannelEntry_Object((1,3,6,1,4,1,20044,26,6,3,212,1))
pm1005CtrllineTunableChannelEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pm1005CtrllineTunableChannelEntry.setStatus(_A)
class _Pm1005CtrllineTunableChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrllineTunableChannelIndex_Type.__name__=_D
_Pm1005CtrllineTunableChannelIndex_Object=MibTableColumn
pm1005CtrllineTunableChannelIndex=_Pm1005CtrllineTunableChannelIndex_Object((1,3,6,1,4,1,20044,26,6,3,212,1,1),_Pm1005CtrllineTunableChannelIndex_Type())
pm1005CtrllineTunableChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrllineTunableChannelIndex.setStatus(_A)
_Pm1005CtrllineTunableChannelPortn_Type=Pm1005OtxChannel
_Pm1005CtrllineTunableChannelPortn_Object=MibTableColumn
pm1005CtrllineTunableChannelPortn=_Pm1005CtrllineTunableChannelPortn_Object((1,3,6,1,4,1,20044,26,6,3,212,1,2),_Pm1005CtrllineTunableChannelPortn_Type())
pm1005CtrllineTunableChannelPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrllineTunableChannelPortn.setStatus(_A)
_Pm1005CtrllinePhotodiodeModeTable_Object=MibTable
pm1005CtrllinePhotodiodeModeTable=_Pm1005CtrllinePhotodiodeModeTable_Object((1,3,6,1,4,1,20044,26,6,3,213))
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeModeTable.setStatus(_A)
_Pm1005CtrllinePhotodiodeModeEntry_Object=MibTableRow
pm1005CtrllinePhotodiodeModeEntry=_Pm1005CtrllinePhotodiodeModeEntry_Object((1,3,6,1,4,1,20044,26,6,3,213,1))
pm1005CtrllinePhotodiodeModeEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeModeEntry.setStatus(_A)
class _Pm1005CtrllinePhotodiodeModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrllinePhotodiodeModeIndex_Type.__name__=_D
_Pm1005CtrllinePhotodiodeModeIndex_Object=MibTableColumn
pm1005CtrllinePhotodiodeModeIndex=_Pm1005CtrllinePhotodiodeModeIndex_Object((1,3,6,1,4,1,20044,26,6,3,213,1,1),_Pm1005CtrllinePhotodiodeModeIndex_Type())
pm1005CtrllinePhotodiodeModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeModeIndex.setStatus(_A)
_Pm1005CtrllinePhotodiodeModePortn_Type=Pm1005OtxMode
_Pm1005CtrllinePhotodiodeModePortn_Object=MibTableColumn
pm1005CtrllinePhotodiodeModePortn=_Pm1005CtrllinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,26,6,3,213,1,2),_Pm1005CtrllinePhotodiodeModePortn_Type())
pm1005CtrllinePhotodiodeModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeModePortn.setStatus(_A)
_Pm1005CtrllinePhotodiodeValueTable_Object=MibTable
pm1005CtrllinePhotodiodeValueTable=_Pm1005CtrllinePhotodiodeValueTable_Object((1,3,6,1,4,1,20044,26,6,3,214))
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeValueTable.setStatus(_A)
_Pm1005CtrllinePhotodiodeValueEntry_Object=MibTableRow
pm1005CtrllinePhotodiodeValueEntry=_Pm1005CtrllinePhotodiodeValueEntry_Object((1,3,6,1,4,1,20044,26,6,3,214,1))
pm1005CtrllinePhotodiodeValueEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeValueEntry.setStatus(_A)
class _Pm1005CtrllinePhotodiodeValueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrllinePhotodiodeValueIndex_Type.__name__=_D
_Pm1005CtrllinePhotodiodeValueIndex_Object=MibTableColumn
pm1005CtrllinePhotodiodeValueIndex=_Pm1005CtrllinePhotodiodeValueIndex_Object((1,3,6,1,4,1,20044,26,6,3,214,1,1),_Pm1005CtrllinePhotodiodeValueIndex_Type())
pm1005CtrllinePhotodiodeValueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeValueIndex.setStatus(_A)
_Pm1005CtrllinePhotodiodeValuePortn_Type=Pm1005AdjustValue
_Pm1005CtrllinePhotodiodeValuePortn_Object=MibTableColumn
pm1005CtrllinePhotodiodeValuePortn=_Pm1005CtrllinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,26,6,3,214,1,2),_Pm1005CtrllinePhotodiodeValuePortn_Type())
pm1005CtrllinePhotodiodeValuePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrllinePhotodiodeValuePortn.setStatus(_A)
_Pm1005CtrllinePowerLaserTable_Object=MibTable
pm1005CtrllinePowerLaserTable=_Pm1005CtrllinePowerLaserTable_Object((1,3,6,1,4,1,20044,26,6,3,215))
if mibBuilder.loadTexts:pm1005CtrllinePowerLaserTable.setStatus(_A)
_Pm1005CtrllinePowerLaserEntry_Object=MibTableRow
pm1005CtrllinePowerLaserEntry=_Pm1005CtrllinePowerLaserEntry_Object((1,3,6,1,4,1,20044,26,6,3,215,1))
pm1005CtrllinePowerLaserEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:pm1005CtrllinePowerLaserEntry.setStatus(_A)
class _Pm1005CtrllinePowerLaserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CtrllinePowerLaserIndex_Type.__name__=_D
_Pm1005CtrllinePowerLaserIndex_Object=MibTableColumn
pm1005CtrllinePowerLaserIndex=_Pm1005CtrllinePowerLaserIndex_Object((1,3,6,1,4,1,20044,26,6,3,215,1,1),_Pm1005CtrllinePowerLaserIndex_Type())
pm1005CtrllinePowerLaserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CtrllinePowerLaserIndex.setStatus(_A)
class _Pm1005CtrllinePowerLaserPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pm1005CtrllinePowerLaserPortn_Type.__name__=_D
_Pm1005CtrllinePowerLaserPortn_Object=MibTableColumn
pm1005CtrllinePowerLaserPortn=_Pm1005CtrllinePowerLaserPortn_Object((1,3,6,1,4,1,20044,26,6,3,215,1,2),_Pm1005CtrllinePowerLaserPortn_Type())
pm1005CtrllinePowerLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CtrllinePowerLaserPortn.setStatus(_A)
_Pm1005ri_ObjectIdentity=ObjectIdentity
pm1005ri=_Pm1005ri_ObjectIdentity((1,3,6,1,4,1,20044,26,7))
_Pm1005riTable_ObjectIdentity=ObjectIdentity
pm1005riTable=_Pm1005riTable_ObjectIdentity((1,3,6,1,4,1,20044,26,7,1))
_Pm1005RinvSfpTable_Object=MibTable
pm1005RinvSfpTable=_Pm1005RinvSfpTable_Object((1,3,6,1,4,1,20044,26,7,1,1))
if mibBuilder.loadTexts:pm1005RinvSfpTable.setStatus(_A)
_Pm1005RinvSfpEntry_Object=MibTableRow
pm1005RinvSfpEntry=_Pm1005RinvSfpEntry_Object((1,3,6,1,4,1,20044,26,7,1,1,1))
pm1005RinvSfpEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:pm1005RinvSfpEntry.setStatus(_A)
class _Pm1005RinvSfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1005RinvSfpIndex_Type.__name__=_D
_Pm1005RinvSfpIndex_Object=MibTableColumn
pm1005RinvSfpIndex=_Pm1005RinvSfpIndex_Object((1,3,6,1,4,1,20044,26,7,1,1,1,1),_Pm1005RinvSfpIndex_Type())
pm1005RinvSfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvSfpIndex.setStatus(_A)
_Pm1005Rinvsfp_Type=DisplayString
_Pm1005Rinvsfp_Object=MibTableColumn
pm1005Rinvsfp=_Pm1005Rinvsfp_Object((1,3,6,1,4,1,20044,26,7,1,1,1,2),_Pm1005Rinvsfp_Type())
pm1005Rinvsfp.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005Rinvsfp.setStatus(_A)
_Pm1005RinvLineTable_Object=MibTable
pm1005RinvLineTable=_Pm1005RinvLineTable_Object((1,3,6,1,4,1,20044,26,7,1,2))
if mibBuilder.loadTexts:pm1005RinvLineTable.setStatus(_A)
_Pm1005RinvLineEntry_Object=MibTableRow
pm1005RinvLineEntry=_Pm1005RinvLineEntry_Object((1,3,6,1,4,1,20044,26,7,1,2,1))
pm1005RinvLineEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:pm1005RinvLineEntry.setStatus(_A)
class _Pm1005RinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1005RinvLineIndex_Type.__name__=_D
_Pm1005RinvLineIndex_Object=MibTableColumn
pm1005RinvLineIndex=_Pm1005RinvLineIndex_Object((1,3,6,1,4,1,20044,26,7,1,2,1,1),_Pm1005RinvLineIndex_Type())
pm1005RinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvLineIndex.setStatus(_A)
_Pm1005RinvxfpLine_Type=DisplayString
_Pm1005RinvxfpLine_Object=MibTableColumn
pm1005RinvxfpLine=_Pm1005RinvxfpLine_Object((1,3,6,1,4,1,20044,26,7,1,2,1,2),_Pm1005RinvxfpLine_Type())
pm1005RinvxfpLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvxfpLine.setStatus(_A)
_Pm1005RinvReloadInventory_Type=EkiOnOff
_Pm1005RinvReloadInventory_Object=MibScalar
pm1005RinvReloadInventory=_Pm1005RinvReloadInventory_Object((1,3,6,1,4,1,20044,26,7,2),_Pm1005RinvReloadInventory_Type())
pm1005RinvReloadInventory.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005RinvReloadInventory.setStatus(_A)
_Pm1005RinvHwPlatform_Type=DisplayString
_Pm1005RinvHwPlatform_Object=MibScalar
pm1005RinvHwPlatform=_Pm1005RinvHwPlatform_Object((1,3,6,1,4,1,20044,26,7,3),_Pm1005RinvHwPlatform_Type())
pm1005RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvHwPlatform.setStatus(_A)
_Pm1005RinvModulePlatform_Type=DisplayString
_Pm1005RinvModulePlatform_Object=MibScalar
pm1005RinvModulePlatform=_Pm1005RinvModulePlatform_Object((1,3,6,1,4,1,20044,26,7,4),_Pm1005RinvModulePlatform_Type())
pm1005RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvModulePlatform.setStatus(_A)
_Pm1005RinvSwPlatform_Type=DisplayString
_Pm1005RinvSwPlatform_Object=MibScalar
pm1005RinvSwPlatform=_Pm1005RinvSwPlatform_Object((1,3,6,1,4,1,20044,26,7,5),_Pm1005RinvSwPlatform_Type())
pm1005RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvSwPlatform.setStatus(_A)
_Pm1005RinvGwPlatform_Type=DisplayString
_Pm1005RinvGwPlatform_Object=MibScalar
pm1005RinvGwPlatform=_Pm1005RinvGwPlatform_Object((1,3,6,1,4,1,20044,26,7,6),_Pm1005RinvGwPlatform_Type())
pm1005RinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005RinvGwPlatform.setStatus(_A)
_Pm1005download_ObjectIdentity=ObjectIdentity
pm1005download=_Pm1005download_ObjectIdentity((1,3,6,1,4,1,20044,26,8))
_Pm1005DwlOther_ObjectIdentity=ObjectIdentity
pm1005DwlOther=_Pm1005DwlOther_ObjectIdentity((1,3,6,1,4,1,20044,26,8,1))
_Pm1005DwlrestartProcess_ObjectIdentity=ObjectIdentity
pm1005DwlrestartProcess=_Pm1005DwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,26,8,1,0))
_Pm1005DwlWarmRestartProcessed_Type=EkiOnOff
_Pm1005DwlWarmRestartProcessed_Object=MibScalar
pm1005DwlWarmRestartProcessed=_Pm1005DwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,26,8,1,0,1),_Pm1005DwlWarmRestartProcessed_Type())
pm1005DwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlWarmRestartProcessed.setStatus(_A)
_Pm1005DwlColdRestartProcessed_Type=EkiOnOff
_Pm1005DwlColdRestartProcessed_Object=MibScalar
pm1005DwlColdRestartProcessed=_Pm1005DwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,26,8,1,0,2),_Pm1005DwlColdRestartProcessed_Type())
pm1005DwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlColdRestartProcessed.setStatus(_A)
_Pm1005DwlswBanksUsed_ObjectIdentity=ObjectIdentity
pm1005DwlswBanksUsed=_Pm1005DwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,26,8,1,1))
_Pm1005DwlSwBank1Used_Type=EkiOnOff
_Pm1005DwlSwBank1Used_Object=MibScalar
pm1005DwlSwBank1Used=_Pm1005DwlSwBank1Used_Object((1,3,6,1,4,1,20044,26,8,1,1,1),_Pm1005DwlSwBank1Used_Type())
pm1005DwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlSwBank1Used.setStatus(_A)
_Pm1005DwlSwBank2Used_Type=EkiOnOff
_Pm1005DwlSwBank2Used_Object=MibScalar
pm1005DwlSwBank2Used=_Pm1005DwlSwBank2Used_Object((1,3,6,1,4,1,20044,26,8,1,1,2),_Pm1005DwlSwBank2Used_Type())
pm1005DwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlSwBank2Used.setStatus(_A)
_Pm1005DwlSwBank1Notempty_Type=EkiOnOff
_Pm1005DwlSwBank1Notempty_Object=MibScalar
pm1005DwlSwBank1Notempty=_Pm1005DwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,26,8,1,1,5),_Pm1005DwlSwBank1Notempty_Type())
pm1005DwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlSwBank1Notempty.setStatus(_A)
_Pm1005DwlSwBank2Notempty_Type=EkiOnOff
_Pm1005DwlSwBank2Notempty_Object=MibScalar
pm1005DwlSwBank2Notempty=_Pm1005DwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,26,8,1,1,6),_Pm1005DwlSwBank2Notempty_Type())
pm1005DwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlSwBank2Notempty.setStatus(_A)
_Pm1005DwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pm1005DwlgwBanksUsed=_Pm1005DwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,26,8,1,2))
_Pm1005DwlGwBank1Used_Type=EkiOnOff
_Pm1005DwlGwBank1Used_Object=MibScalar
pm1005DwlGwBank1Used=_Pm1005DwlGwBank1Used_Object((1,3,6,1,4,1,20044,26,8,1,2,1),_Pm1005DwlGwBank1Used_Type())
pm1005DwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank1Used.setStatus(_A)
_Pm1005DwlGwBank2Used_Type=EkiOnOff
_Pm1005DwlGwBank2Used_Object=MibScalar
pm1005DwlGwBank2Used=_Pm1005DwlGwBank2Used_Object((1,3,6,1,4,1,20044,26,8,1,2,2),_Pm1005DwlGwBank2Used_Type())
pm1005DwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank2Used.setStatus(_A)
_Pm1005DwlGwBank3Used_Type=EkiOnOff
_Pm1005DwlGwBank3Used_Object=MibScalar
pm1005DwlGwBank3Used=_Pm1005DwlGwBank3Used_Object((1,3,6,1,4,1,20044,26,8,1,2,3),_Pm1005DwlGwBank3Used_Type())
pm1005DwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank3Used.setStatus(_A)
_Pm1005DwlGwBank4Used_Type=EkiOnOff
_Pm1005DwlGwBank4Used_Object=MibScalar
pm1005DwlGwBank4Used=_Pm1005DwlGwBank4Used_Object((1,3,6,1,4,1,20044,26,8,1,2,4),_Pm1005DwlGwBank4Used_Type())
pm1005DwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank4Used.setStatus(_A)
_Pm1005DwlGwBank1Notempty_Type=EkiOnOff
_Pm1005DwlGwBank1Notempty_Object=MibScalar
pm1005DwlGwBank1Notempty=_Pm1005DwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,26,8,1,2,5),_Pm1005DwlGwBank1Notempty_Type())
pm1005DwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank1Notempty.setStatus(_A)
_Pm1005DwlGwBank2Notempty_Type=EkiOnOff
_Pm1005DwlGwBank2Notempty_Object=MibScalar
pm1005DwlGwBank2Notempty=_Pm1005DwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,26,8,1,2,6),_Pm1005DwlGwBank2Notempty_Type())
pm1005DwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank2Notempty.setStatus(_A)
_Pm1005DwlGwBank3Notempty_Type=EkiOnOff
_Pm1005DwlGwBank3Notempty_Object=MibScalar
pm1005DwlGwBank3Notempty=_Pm1005DwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,26,8,1,2,7),_Pm1005DwlGwBank3Notempty_Type())
pm1005DwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank3Notempty.setStatus(_A)
_Pm1005DwlGwBank4Notempty_Type=EkiOnOff
_Pm1005DwlGwBank4Notempty_Object=MibScalar
pm1005DwlGwBank4Notempty=_Pm1005DwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,26,8,1,2,8),_Pm1005DwlGwBank4Notempty_Type())
pm1005DwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005DwlGwBank4Notempty.setStatus(_A)
_Pm1005DwlClient_ObjectIdentity=ObjectIdentity
pm1005DwlClient=_Pm1005DwlClient_ObjectIdentity((1,3,6,1,4,1,20044,26,8,2))
_Pm1005DwlLine_ObjectIdentity=ObjectIdentity
pm1005DwlLine=_Pm1005DwlLine_ObjectIdentity((1,3,6,1,4,1,20044,26,8,3))
_Pm1005Config_ObjectIdentity=ObjectIdentity
pm1005Config=_Pm1005Config_ObjectIdentity((1,3,6,1,4,1,20044,26,9))
_Pm1005CfgAccessCAisCsf_ObjectIdentity=ObjectIdentity
pm1005CfgAccessCAisCsf=_Pm1005CfgAccessCAisCsf_ObjectIdentity((1,3,6,1,4,1,20044,26,9,1))
_Pm1005CfgClientcaiscsfTable_Object=MibTable
pm1005CfgClientcaiscsfTable=_Pm1005CfgClientcaiscsfTable_Object((1,3,6,1,4,1,20044,26,9,1,1))
if mibBuilder.loadTexts:pm1005CfgClientcaiscsfTable.setStatus(_A)
_Pm1005CfgClientcaiscsfEntry_Object=MibTableRow
pm1005CfgClientcaiscsfEntry=_Pm1005CfgClientcaiscsfEntry_Object((1,3,6,1,4,1,20044,26,9,1,1,1))
pm1005CfgClientcaiscsfEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:pm1005CfgClientcaiscsfEntry.setStatus(_A)
class _Pm1005CfgClientcaiscsfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgClientcaiscsfIndex_Type.__name__=_D
_Pm1005CfgClientcaiscsfIndex_Object=MibTableColumn
pm1005CfgClientcaiscsfIndex=_Pm1005CfgClientcaiscsfIndex_Object((1,3,6,1,4,1,20044,26,9,1,1,1,1),_Pm1005CfgClientcaiscsfIndex_Type())
pm1005CfgClientcaiscsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgClientcaiscsfIndex.setStatus(_A)
class _Pm1005CfgCAisModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgCAisModePortn_Type.__name__=_F
_Pm1005CfgCAisModePortn_Object=MibTableColumn
pm1005CfgCAisModePortn=_Pm1005CfgCAisModePortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,3),_Pm1005CfgCAisModePortn_Type())
pm1005CfgCAisModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgCAisModePortn.setStatus(_A)
class _Pm1005CfgUpAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgUpAccessioAlmPortn_Type.__name__=_F
_Pm1005CfgUpAccessioAlmPortn_Object=MibTableColumn
pm1005CfgUpAccessioAlmPortn=_Pm1005CfgUpAccessioAlmPortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,9),_Pm1005CfgUpAccessioAlmPortn_Type())
pm1005CfgUpAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgUpAccessioAlmPortn.setStatus(_A)
class _Pm1005CfgUpMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgUpMapperDeAlmPortn_Type.__name__=_F
_Pm1005CfgUpMapperDeAlmPortn_Object=MibTableColumn
pm1005CfgUpMapperDeAlmPortn=_Pm1005CfgUpMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,10),_Pm1005CfgUpMapperDeAlmPortn_Type())
pm1005CfgUpMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgUpMapperDeAlmPortn.setStatus(_A)
class _Pm1005CfgDownAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgDownAccessioAlmPortn_Type.__name__=_F
_Pm1005CfgDownAccessioAlmPortn_Object=MibTableColumn
pm1005CfgDownAccessioAlmPortn=_Pm1005CfgDownAccessioAlmPortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,17),_Pm1005CfgDownAccessioAlmPortn_Type())
pm1005CfgDownAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgDownAccessioAlmPortn.setStatus(_A)
class _Pm1005CfgDownMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgDownMapperDeAlmPortn_Type.__name__=_F
_Pm1005CfgDownMapperDeAlmPortn_Object=MibTableColumn
pm1005CfgDownMapperDeAlmPortn=_Pm1005CfgDownMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,18),_Pm1005CfgDownMapperDeAlmPortn_Type())
pm1005CfgDownMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgDownMapperDeAlmPortn.setStatus(_A)
class _Pm1005CfgDownDfrmAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgDownDfrmAlmPortn_Type.__name__=_F
_Pm1005CfgDownDfrmAlmPortn_Object=MibTableColumn
pm1005CfgDownDfrmAlmPortn=_Pm1005CfgDownDfrmAlmPortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,19),_Pm1005CfgDownDfrmAlmPortn_Type())
pm1005CfgDownDfrmAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgDownDfrmAlmPortn.setStatus(_A)
class _Pm1005CfgDownLineSyncAlarmsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgDownLineSyncAlarmsPortn_Type.__name__=_F
_Pm1005CfgDownLineSyncAlarmsPortn_Object=MibTableColumn
pm1005CfgDownLineSyncAlarmsPortn=_Pm1005CfgDownLineSyncAlarmsPortn_Object((1,3,6,1,4,1,20044,26,9,1,1,1,20),_Pm1005CfgDownLineSyncAlarmsPortn_Type())
pm1005CfgDownLineSyncAlarmsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgDownLineSyncAlarmsPortn.setStatus(_G)
_Pm1005CfgStartup_ObjectIdentity=ObjectIdentity
pm1005CfgStartup=_Pm1005CfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,26,9,2))
_Pm1005CfgClientStartupTable_Object=MibTable
pm1005CfgClientStartupTable=_Pm1005CfgClientStartupTable_Object((1,3,6,1,4,1,20044,26,9,2,1))
if mibBuilder.loadTexts:pm1005CfgClientStartupTable.setStatus(_A)
_Pm1005CfgClientStartupEntry_Object=MibTableRow
pm1005CfgClientStartupEntry=_Pm1005CfgClientStartupEntry_Object((1,3,6,1,4,1,20044,26,9,2,1,1))
pm1005CfgClientStartupEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:pm1005CfgClientStartupEntry.setStatus(_A)
class _Pm1005CfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgClientStartupIndex_Type.__name__=_D
_Pm1005CfgClientStartupIndex_Object=MibTableColumn
pm1005CfgClientStartupIndex=_Pm1005CfgClientStartupIndex_Object((1,3,6,1,4,1,20044,26,9,2,1,1,1),_Pm1005CfgClientStartupIndex_Type())
pm1005CfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgClientStartupIndex.setStatus(_A)
class _Pm1005CfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgSystConfPortPortn_Type.__name__=_F
_Pm1005CfgSystConfPortPortn_Object=MibTableColumn
pm1005CfgSystConfPortPortn=_Pm1005CfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,26,9,2,1,1,3),_Pm1005CfgSystConfPortPortn_Type())
pm1005CfgSystConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgSystConfPortPortn.setStatus(_A)
class _Pm1005CfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgNetConfPortPortn_Type.__name__=_F
_Pm1005CfgNetConfPortPortn_Object=MibTableColumn
pm1005CfgNetConfPortPortn=_Pm1005CfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,26,9,2,1,1,4),_Pm1005CfgNetConfPortPortn_Type())
pm1005CfgNetConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgNetConfPortPortn.setStatus(_A)
_Pm1005tablelineStartup_ObjectIdentity=ObjectIdentity
pm1005tablelineStartup=_Pm1005tablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,26,9,2,2))
class _Pm1005CfgsystConfLine1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgsystConfLine1_Type.__name__=_F
_Pm1005CfgsystConfLine1_Object=MibScalar
pm1005CfgsystConfLine1=_Pm1005CfgsystConfLine1_Object((1,3,6,1,4,1,20044,26,9,2,2,2),_Pm1005CfgsystConfLine1_Type())
pm1005CfgsystConfLine1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgsystConfLine1.setStatus(_A)
class _Pm1005CfglineOptions1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfglineOptions1_Type.__name__=_F
_Pm1005CfglineOptions1_Object=MibScalar
pm1005CfglineOptions1=_Pm1005CfglineOptions1_Object((1,3,6,1,4,1,20044,26,9,2,2,5),_Pm1005CfglineOptions1_Type())
pm1005CfglineOptions1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfglineOptions1.setStatus(_A)
class _Pm1005CfgsystConfLine2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgsystConfLine2_Type.__name__=_F
_Pm1005CfgsystConfLine2_Object=MibScalar
pm1005CfgsystConfLine2=_Pm1005CfgsystConfLine2_Object((1,3,6,1,4,1,20044,26,9,2,2,6),_Pm1005CfgsystConfLine2_Type())
pm1005CfgsystConfLine2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgsystConfLine2.setStatus(_A)
class _Pm1005CfglineSelection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfglineSelection_Type.__name__=_F
_Pm1005CfglineSelection_Object=MibScalar
pm1005CfglineSelection=_Pm1005CfglineSelection_Object((1,3,6,1,4,1,20044,26,9,2,2,7),_Pm1005CfglineSelection_Type())
pm1005CfglineSelection.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfglineSelection.setStatus(_A)
_Pm1005CfgXfpTable_Object=MibTable
pm1005CfgXfpTable=_Pm1005CfgXfpTable_Object((1,3,6,1,4,1,20044,26,9,2,3))
if mibBuilder.loadTexts:pm1005CfgXfpTable.setStatus(_A)
_Pm1005CfgXfpEntry_Object=MibTableRow
pm1005CfgXfpEntry=_Pm1005CfgXfpEntry_Object((1,3,6,1,4,1,20044,26,9,2,3,1))
pm1005CfgXfpEntry.setIndexNames((0,_C,_AV))
if mibBuilder.loadTexts:pm1005CfgXfpEntry.setStatus(_A)
class _Pm1005CfgXfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgXfpIndex_Type.__name__=_D
_Pm1005CfgXfpIndex_Object=MibTableColumn
pm1005CfgXfpIndex=_Pm1005CfgXfpIndex_Object((1,3,6,1,4,1,20044,26,9,2,3,1,1),_Pm1005CfgXfpIndex_Type())
pm1005CfgXfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgXfpIndex.setStatus(_A)
class _Pm1005CfgSystConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgSystConfXfpPortn_Type.__name__=_F
_Pm1005CfgSystConfXfpPortn_Object=MibTableColumn
pm1005CfgSystConfXfpPortn=_Pm1005CfgSystConfXfpPortn_Object((1,3,6,1,4,1,20044,26,9,2,3,1,3),_Pm1005CfgSystConfXfpPortn_Type())
pm1005CfgSystConfXfpPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgSystConfXfpPortn.setStatus(_A)
class _Pm1005CfgDataRateConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgDataRateConfXfpPortn_Type.__name__=_F
_Pm1005CfgDataRateConfXfpPortn_Object=MibTableColumn
pm1005CfgDataRateConfXfpPortn=_Pm1005CfgDataRateConfXfpPortn_Object((1,3,6,1,4,1,20044,26,9,2,3,1,4),_Pm1005CfgDataRateConfXfpPortn_Type())
pm1005CfgDataRateConfXfpPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgDataRateConfXfpPortn.setStatus(_G)
_Pm1005CfgLabels_ObjectIdentity=ObjectIdentity
pm1005CfgLabels=_Pm1005CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,26,9,3))
_Pm1005CfgLabelclientTable_Object=MibTable
pm1005CfgLabelclientTable=_Pm1005CfgLabelclientTable_Object((1,3,6,1,4,1,20044,26,9,3,1))
if mibBuilder.loadTexts:pm1005CfgLabelclientTable.setStatus(_A)
_Pm1005CfgLabelclientEntry_Object=MibTableRow
pm1005CfgLabelclientEntry=_Pm1005CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,26,9,3,1,1))
pm1005CfgLabelclientEntry.setIndexNames((0,_C,_AW))
if mibBuilder.loadTexts:pm1005CfgLabelclientEntry.setStatus(_A)
class _Pm1005CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgLabelclientIndex_Type.__name__=_D
_Pm1005CfgLabelclientIndex_Object=MibTableColumn
pm1005CfgLabelclientIndex=_Pm1005CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,26,9,3,1,1,1),_Pm1005CfgLabelclientIndex_Type())
pm1005CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgLabelclientIndex.setStatus(_A)
class _Pm1005CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1005CfgLabelclientPortn_Type.__name__=_K
_Pm1005CfgLabelclientPortn_Object=MibTableColumn
pm1005CfgLabelclientPortn=_Pm1005CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,26,9,3,1,1,3),_Pm1005CfgLabelclientPortn_Type())
pm1005CfgLabelclientPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLabelclientPortn.setStatus(_A)
_Pm1005CfgLabellineTable_Object=MibTable
pm1005CfgLabellineTable=_Pm1005CfgLabellineTable_Object((1,3,6,1,4,1,20044,26,9,3,2))
if mibBuilder.loadTexts:pm1005CfgLabellineTable.setStatus(_A)
_Pm1005CfgLabellineEntry_Object=MibTableRow
pm1005CfgLabellineEntry=_Pm1005CfgLabellineEntry_Object((1,3,6,1,4,1,20044,26,9,3,2,1))
pm1005CfgLabellineEntry.setIndexNames((0,_C,_AX))
if mibBuilder.loadTexts:pm1005CfgLabellineEntry.setStatus(_A)
class _Pm1005CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgLabellineIndex_Type.__name__=_D
_Pm1005CfgLabellineIndex_Object=MibTableColumn
pm1005CfgLabellineIndex=_Pm1005CfgLabellineIndex_Object((1,3,6,1,4,1,20044,26,9,3,2,1,1),_Pm1005CfgLabellineIndex_Type())
pm1005CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgLabellineIndex.setStatus(_A)
class _Pm1005CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1005CfgLabellinePortn_Type.__name__=_K
_Pm1005CfgLabellinePortn_Object=MibTableColumn
pm1005CfgLabellinePortn=_Pm1005CfgLabellinePortn_Object((1,3,6,1,4,1,20044,26,9,3,2,1,3),_Pm1005CfgLabellinePortn_Type())
pm1005CfgLabellinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLabellinePortn.setStatus(_A)
_Pm1005CfgStartuptlh_ObjectIdentity=ObjectIdentity
pm1005CfgStartuptlh=_Pm1005CfgStartuptlh_ObjectIdentity((1,3,6,1,4,1,20044,26,9,4))
_Pm1005CfgOtxtlhTable_Object=MibTable
pm1005CfgOtxtlhTable=_Pm1005CfgOtxtlhTable_Object((1,3,6,1,4,1,20044,26,9,4,1))
if mibBuilder.loadTexts:pm1005CfgOtxtlhTable.setStatus(_A)
_Pm1005CfgOtxtlhEntry_Object=MibTableRow
pm1005CfgOtxtlhEntry=_Pm1005CfgOtxtlhEntry_Object((1,3,6,1,4,1,20044,26,9,4,1,1))
pm1005CfgOtxtlhEntry.setIndexNames((0,_C,_AY))
if mibBuilder.loadTexts:pm1005CfgOtxtlhEntry.setStatus(_A)
class _Pm1005CfgOtxtlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgOtxtlhIndex_Type.__name__=_D
_Pm1005CfgOtxtlhIndex_Object=MibTableColumn
pm1005CfgOtxtlhIndex=_Pm1005CfgOtxtlhIndex_Object((1,3,6,1,4,1,20044,26,9,4,1,1,1),_Pm1005CfgOtxtlhIndex_Type())
pm1005CfgOtxtlhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgOtxtlhIndex.setStatus(_A)
class _Pm1005CfgNuPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgNuPortn_Type.__name__=_F
_Pm1005CfgNuPortn_Object=MibTableColumn
pm1005CfgNuPortn=_Pm1005CfgNuPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,3),_Pm1005CfgNuPortn_Type())
pm1005CfgNuPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgNuPortn.setStatus(_G)
class _Pm1005CfgLineDitherRatePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLineDitherRatePortn_Type.__name__=_F
_Pm1005CfgLineDitherRatePortn_Object=MibTableColumn
pm1005CfgLineDitherRatePortn=_Pm1005CfgLineDitherRatePortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,4),_Pm1005CfgLineDitherRatePortn_Type())
pm1005CfgLineDitherRatePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLineDitherRatePortn.setStatus(_A)
class _Pm1005CfgLineDitherFhzPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLineDitherFhzPortn_Type.__name__=_F
_Pm1005CfgLineDitherFhzPortn_Object=MibTableColumn
pm1005CfgLineDitherFhzPortn=_Pm1005CfgLineDitherFhzPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,5),_Pm1005CfgLineDitherFhzPortn_Type())
pm1005CfgLineDitherFhzPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLineDitherFhzPortn.setStatus(_A)
class _Pm1005CfgLinePwrLaserPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLinePwrLaserPortn_Type.__name__=_F
_Pm1005CfgLinePwrLaserPortn_Object=MibTableColumn
pm1005CfgLinePwrLaserPortn=_Pm1005CfgLinePwrLaserPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,6),_Pm1005CfgLinePwrLaserPortn_Type())
pm1005CfgLinePwrLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLinePwrLaserPortn.setStatus(_A)
class _Pm1005CfgLineFCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLineFCurrentPortn_Type.__name__=_F
_Pm1005CfgLineFCurrentPortn_Object=MibTableColumn
pm1005CfgLineFCurrentPortn=_Pm1005CfgLineFCurrentPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,7),_Pm1005CfgLineFCurrentPortn_Type())
pm1005CfgLineFCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLineFCurrentPortn.setStatus(_A)
class _Pm1005CfgLineGridCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLineGridCurrentPortn_Type.__name__=_F
_Pm1005CfgLineGridCurrentPortn_Object=MibTableColumn
pm1005CfgLineGridCurrentPortn=_Pm1005CfgLineGridCurrentPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,8),_Pm1005CfgLineGridCurrentPortn_Type())
pm1005CfgLineGridCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLineGridCurrentPortn.setStatus(_A)
class _Pm1005CfgFPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgFPortn_Type.__name__=_F
_Pm1005CfgFPortn_Object=MibTableColumn
pm1005CfgFPortn=_Pm1005CfgFPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,9),_Pm1005CfgFPortn_Type())
pm1005CfgFPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgFPortn.setStatus(_A)
class _Pm1005CfgReservedPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgReservedPortn_Type.__name__=_F
_Pm1005CfgReservedPortn_Object=MibTableColumn
pm1005CfgReservedPortn=_Pm1005CfgReservedPortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,10),_Pm1005CfgReservedPortn_Type())
pm1005CfgReservedPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgReservedPortn.setStatus(_G)
class _Pm1005CfgLinePhotodiodeModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLinePhotodiodeModePortn_Type.__name__=_F
_Pm1005CfgLinePhotodiodeModePortn_Object=MibTableColumn
pm1005CfgLinePhotodiodeModePortn=_Pm1005CfgLinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,11),_Pm1005CfgLinePhotodiodeModePortn_Type())
pm1005CfgLinePhotodiodeModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLinePhotodiodeModePortn.setStatus(_A)
class _Pm1005CfgLinePhotodiodeValuePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLinePhotodiodeValuePortn_Type.__name__=_F
_Pm1005CfgLinePhotodiodeValuePortn_Object=MibTableColumn
pm1005CfgLinePhotodiodeValuePortn=_Pm1005CfgLinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,26,9,4,1,1,12),_Pm1005CfgLinePhotodiodeValuePortn_Type())
pm1005CfgLinePhotodiodeValuePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgLinePhotodiodeValuePortn.setStatus(_A)
_Pm1005CfgStartuptablefive_ObjectIdentity=ObjectIdentity
pm1005CfgStartuptablefive=_Pm1005CfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,26,9,5))
_Pm1005CfgOtxtlhcapabilitiesTable_Object=MibTable
pm1005CfgOtxtlhcapabilitiesTable=_Pm1005CfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,26,9,5,1))
if mibBuilder.loadTexts:pm1005CfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pm1005CfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pm1005CfgOtxtlhcapabilitiesEntry=_Pm1005CfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,26,9,5,1,1))
pm1005CfgOtxtlhcapabilitiesEntry.setIndexNames((0,_C,_AZ))
if mibBuilder.loadTexts:pm1005CfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pm1005CfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005CfgOtxtlhcapabilitiesIndex_Type.__name__=_D
_Pm1005CfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pm1005CfgOtxtlhcapabilitiesIndex=_Pm1005CfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,26,9,5,1,1,1),_Pm1005CfgOtxtlhcapabilitiesIndex_Type())
pm1005CfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pm1005CfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgComponentTypePortn_Type.__name__=_F
_Pm1005CfgComponentTypePortn_Object=MibTableColumn
pm1005CfgComponentTypePortn=_Pm1005CfgComponentTypePortn_Object((1,3,6,1,4,1,20044,26,9,5,1,1,3),_Pm1005CfgComponentTypePortn_Type())
pm1005CfgComponentTypePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgComponentTypePortn.setStatus(_A)
class _Pm1005CfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgMiscellaneousPortn_Type.__name__=_F
_Pm1005CfgMiscellaneousPortn_Object=MibTableColumn
pm1005CfgMiscellaneousPortn=_Pm1005CfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,26,9,5,1,1,4),_Pm1005CfgMiscellaneousPortn_Type())
pm1005CfgMiscellaneousPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgMiscellaneousPortn.setStatus(_A)
class _Pm1005CfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgFirstChannelPortn_Type.__name__=_F
_Pm1005CfgFirstChannelPortn_Object=MibTableColumn
pm1005CfgFirstChannelPortn=_Pm1005CfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,26,9,5,1,1,5),_Pm1005CfgFirstChannelPortn_Type())
pm1005CfgFirstChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgFirstChannelPortn.setStatus(_A)
class _Pm1005CfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgLastChannelPortn_Type.__name__=_F
_Pm1005CfgLastChannelPortn_Object=MibTableColumn
pm1005CfgLastChannelPortn=_Pm1005CfgLastChannelPortn_Object((1,3,6,1,4,1,20044,26,9,5,1,1,6),_Pm1005CfgLastChannelPortn_Type())
pm1005CfgLastChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgLastChannelPortn.setStatus(_A)
class _Pm1005CfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1005CfgGridPortn_Type.__name__=_F
_Pm1005CfgGridPortn_Object=MibTableColumn
pm1005CfgGridPortn=_Pm1005CfgGridPortn_Object((1,3,6,1,4,1,20044,26,9,5,1,1,7),_Pm1005CfgGridPortn_Type())
pm1005CfgGridPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005CfgGridPortn.setStatus(_A)
_Pm1005CfgWriteConfiguration_Type=EkiOnOff
_Pm1005CfgWriteConfiguration_Object=MibScalar
pm1005CfgWriteConfiguration=_Pm1005CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,26,9,257),_Pm1005CfgWriteConfiguration_Type())
pm1005CfgWriteConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005CfgWriteConfiguration.setStatus(_A)
_Pm1005traps_ObjectIdentity=ObjectIdentity
pm1005traps=_Pm1005traps_ObjectIdentity((1,3,6,1,4,1,20044,26,10))
class _Pm1005trapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1005trapPortNumber_Type.__name__=_D
_Pm1005trapPortNumber_Object=MibScalar
pm1005trapPortNumber=_Pm1005trapPortNumber_Object((1,3,6,1,4,1,20044,26,10,2),_Pm1005trapPortNumber_Type())
pm1005trapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005trapPortNumber.setStatus(_A)
class _Pm1005trapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1005trapLineNumber_Type.__name__=_D
_Pm1005trapLineNumber_Object=MibScalar
pm1005trapLineNumber=_Pm1005trapLineNumber_Object((1,3,6,1,4,1,20044,26,10,3),_Pm1005trapLineNumber_Type())
pm1005trapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005trapLineNumber.setStatus(_A)
class _Pm1005trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1005trapBoardNumber_Type.__name__=_D
_Pm1005trapBoardNumber_Object=MibScalar
pm1005trapBoardNumber=_Pm1005trapBoardNumber_Object((1,3,6,1,4,1,20044,26,10,4),_Pm1005trapBoardNumber_Type())
pm1005trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005trapBoardNumber.setStatus(_A)
_Pm1005Monitoring_ObjectIdentity=ObjectIdentity
pm1005Monitoring=_Pm1005Monitoring_ObjectIdentity((1,3,6,1,4,1,20044,26,11))
_Pm1005MonOther_ObjectIdentity=ObjectIdentity
pm1005MonOther=_Pm1005MonOther_ObjectIdentity((1,3,6,1,4,1,20044,26,11,1))
_Pm1005MonRmon_ObjectIdentity=ObjectIdentity
pm1005MonRmon=_Pm1005MonRmon_ObjectIdentity((1,3,6,1,4,1,20044,26,11,1,3))
_Pm1005MonCountersReset_Type=EkiOnOff
_Pm1005MonCountersReset_Object=MibScalar
pm1005MonCountersReset=_Pm1005MonCountersReset_Object((1,3,6,1,4,1,20044,26,11,1,3,359),_Pm1005MonCountersReset_Type())
pm1005MonCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005MonCountersReset.setStatus(_A)
_Pm1005MonCountersStop_Type=EkiOnOff
_Pm1005MonCountersStop_Object=MibScalar
pm1005MonCountersStop=_Pm1005MonCountersStop_Object((1,3,6,1,4,1,20044,26,11,1,3,360),_Pm1005MonCountersStop_Type())
pm1005MonCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1005MonCountersStop.setStatus(_A)
_Pm1005MonClient_ObjectIdentity=ObjectIdentity
pm1005MonClient=_Pm1005MonClient_ObjectIdentity((1,3,6,1,4,1,20044,26,11,2))
_Pm1005MonClientRmonCounter_ObjectIdentity=ObjectIdentity
pm1005MonClientRmonCounter=_Pm1005MonClientRmonCounter_ObjectIdentity((1,3,6,1,4,1,20044,26,11,2,4))
_Pm1005MonupRmonByteCntTable_Object=MibTable
pm1005MonupRmonByteCntTable=_Pm1005MonupRmonByteCntTable_Object((1,3,6,1,4,1,20044,26,11,2,4,16))
if mibBuilder.loadTexts:pm1005MonupRmonByteCntTable.setStatus(_A)
_Pm1005MonupRmonByteCntEntry_Object=MibTableRow
pm1005MonupRmonByteCntEntry=_Pm1005MonupRmonByteCntEntry_Object((1,3,6,1,4,1,20044,26,11,2,4,16,1))
pm1005MonupRmonByteCntEntry.setIndexNames((0,_C,_Aa))
if mibBuilder.loadTexts:pm1005MonupRmonByteCntEntry.setStatus(_A)
class _Pm1005MonupRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MonupRmonByteCntIndex_Type.__name__=_D
_Pm1005MonupRmonByteCntIndex_Object=MibTableColumn
pm1005MonupRmonByteCntIndex=_Pm1005MonupRmonByteCntIndex_Object((1,3,6,1,4,1,20044,26,11,2,4,16,1,1),_Pm1005MonupRmonByteCntIndex_Type())
pm1005MonupRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonByteCntIndex.setStatus(_A)
_Pm1005MonupRmonByteCntValuePortn_Type=Counter64
_Pm1005MonupRmonByteCntValuePortn_Object=MibTableColumn
pm1005MonupRmonByteCntValuePortn=_Pm1005MonupRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,26,11,2,4,16,1,2),_Pm1005MonupRmonByteCntValuePortn_Type())
pm1005MonupRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonByteCntValuePortn.setStatus(_A)
_Pm1005MonupRmonByteCntErrorPortn_Type=EkiOnOff
_Pm1005MonupRmonByteCntErrorPortn_Object=MibTableColumn
pm1005MonupRmonByteCntErrorPortn=_Pm1005MonupRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,16,1,3),_Pm1005MonupRmonByteCntErrorPortn_Type())
pm1005MonupRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonByteCntErrorPortn.setStatus(_A)
_Pm1005MonupRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm1005MonupRmonByteCntOverloadPortn_Object=MibTableColumn
pm1005MonupRmonByteCntOverloadPortn=_Pm1005MonupRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,16,1,4),_Pm1005MonupRmonByteCntOverloadPortn_Type())
pm1005MonupRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonByteCntOverloadPortn.setStatus(_A)
_Pm1005MonupRmonCrcErrorCntTable_Object=MibTable
pm1005MonupRmonCrcErrorCntTable=_Pm1005MonupRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,26,11,2,4,24))
if mibBuilder.loadTexts:pm1005MonupRmonCrcErrorCntTable.setStatus(_A)
_Pm1005MonupRmonCrcErrorCntEntry_Object=MibTableRow
pm1005MonupRmonCrcErrorCntEntry=_Pm1005MonupRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,26,11,2,4,24,1))
pm1005MonupRmonCrcErrorCntEntry.setIndexNames((0,_C,_Ab))
if mibBuilder.loadTexts:pm1005MonupRmonCrcErrorCntEntry.setStatus(_A)
class _Pm1005MonupRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MonupRmonCrcErrorCntIndex_Type.__name__=_D
_Pm1005MonupRmonCrcErrorCntIndex_Object=MibTableColumn
pm1005MonupRmonCrcErrorCntIndex=_Pm1005MonupRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,26,11,2,4,24,1,1),_Pm1005MonupRmonCrcErrorCntIndex_Type())
pm1005MonupRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonCrcErrorCntIndex.setStatus(_A)
_Pm1005MonupRmonCrcErrorCntValuePortn_Type=Counter64
_Pm1005MonupRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm1005MonupRmonCrcErrorCntValuePortn=_Pm1005MonupRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,26,11,2,4,24,1,2),_Pm1005MonupRmonCrcErrorCntValuePortn_Type())
pm1005MonupRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm1005MonupRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm1005MonupRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm1005MonupRmonCrcErrorCntErrorPortn=_Pm1005MonupRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,24,1,3),_Pm1005MonupRmonCrcErrorCntErrorPortn_Type())
pm1005MonupRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm1005MonupRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm1005MonupRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm1005MonupRmonCrcErrorCntOverloadPortn=_Pm1005MonupRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,24,1,4),_Pm1005MonupRmonCrcErrorCntOverloadPortn_Type())
pm1005MonupRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm1005MonupRmonPacketsCntTable_Object=MibTable
pm1005MonupRmonPacketsCntTable=_Pm1005MonupRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,26,11,2,4,32))
if mibBuilder.loadTexts:pm1005MonupRmonPacketsCntTable.setStatus(_A)
_Pm1005MonupRmonPacketsCntEntry_Object=MibTableRow
pm1005MonupRmonPacketsCntEntry=_Pm1005MonupRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,26,11,2,4,32,1))
pm1005MonupRmonPacketsCntEntry.setIndexNames((0,_C,_Ac))
if mibBuilder.loadTexts:pm1005MonupRmonPacketsCntEntry.setStatus(_A)
class _Pm1005MonupRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MonupRmonPacketsCntIndex_Type.__name__=_D
_Pm1005MonupRmonPacketsCntIndex_Object=MibTableColumn
pm1005MonupRmonPacketsCntIndex=_Pm1005MonupRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,26,11,2,4,32,1,1),_Pm1005MonupRmonPacketsCntIndex_Type())
pm1005MonupRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonPacketsCntIndex.setStatus(_A)
_Pm1005MonupRmonPacketsCntValuePortn_Type=Counter64
_Pm1005MonupRmonPacketsCntValuePortn_Object=MibTableColumn
pm1005MonupRmonPacketsCntValuePortn=_Pm1005MonupRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,26,11,2,4,32,1,2),_Pm1005MonupRmonPacketsCntValuePortn_Type())
pm1005MonupRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonPacketsCntValuePortn.setStatus(_A)
_Pm1005MonupRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm1005MonupRmonPacketsCntErrorPortn_Object=MibTableColumn
pm1005MonupRmonPacketsCntErrorPortn=_Pm1005MonupRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,32,1,3),_Pm1005MonupRmonPacketsCntErrorPortn_Type())
pm1005MonupRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonPacketsCntErrorPortn.setStatus(_A)
_Pm1005MonupRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm1005MonupRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm1005MonupRmonPacketsCntOverloadPortn=_Pm1005MonupRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,32,1,4),_Pm1005MonupRmonPacketsCntOverloadPortn_Type())
pm1005MonupRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm1005MonupRmonBroadcastCntTable_Object=MibTable
pm1005MonupRmonBroadcastCntTable=_Pm1005MonupRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,26,11,2,4,40))
if mibBuilder.loadTexts:pm1005MonupRmonBroadcastCntTable.setStatus(_A)
_Pm1005MonupRmonBroadcastCntEntry_Object=MibTableRow
pm1005MonupRmonBroadcastCntEntry=_Pm1005MonupRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,26,11,2,4,40,1))
pm1005MonupRmonBroadcastCntEntry.setIndexNames((0,_C,_Ad))
if mibBuilder.loadTexts:pm1005MonupRmonBroadcastCntEntry.setStatus(_A)
class _Pm1005MonupRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MonupRmonBroadcastCntIndex_Type.__name__=_D
_Pm1005MonupRmonBroadcastCntIndex_Object=MibTableColumn
pm1005MonupRmonBroadcastCntIndex=_Pm1005MonupRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,26,11,2,4,40,1,1),_Pm1005MonupRmonBroadcastCntIndex_Type())
pm1005MonupRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonBroadcastCntIndex.setStatus(_A)
_Pm1005MonupRmonBroadcastCntValuePortn_Type=Counter64
_Pm1005MonupRmonBroadcastCntValuePortn_Object=MibTableColumn
pm1005MonupRmonBroadcastCntValuePortn=_Pm1005MonupRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,26,11,2,4,40,1,2),_Pm1005MonupRmonBroadcastCntValuePortn_Type())
pm1005MonupRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonBroadcastCntValuePortn.setStatus(_A)
_Pm1005MonupRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm1005MonupRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm1005MonupRmonBroadcastCntErrorPortn=_Pm1005MonupRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,40,1,3),_Pm1005MonupRmonBroadcastCntErrorPortn_Type())
pm1005MonupRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm1005MonupRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm1005MonupRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm1005MonupRmonBroadcastCntOverloadPortn=_Pm1005MonupRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,40,1,4),_Pm1005MonupRmonBroadcastCntOverloadPortn_Type())
pm1005MonupRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm1005MonupRmonMulticastCntTable_Object=MibTable
pm1005MonupRmonMulticastCntTable=_Pm1005MonupRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,26,11,2,4,48))
if mibBuilder.loadTexts:pm1005MonupRmonMulticastCntTable.setStatus(_A)
_Pm1005MonupRmonMulticastCntEntry_Object=MibTableRow
pm1005MonupRmonMulticastCntEntry=_Pm1005MonupRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,26,11,2,4,48,1))
pm1005MonupRmonMulticastCntEntry.setIndexNames((0,_C,_Ae))
if mibBuilder.loadTexts:pm1005MonupRmonMulticastCntEntry.setStatus(_A)
class _Pm1005MonupRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1005MonupRmonMulticastCntIndex_Type.__name__=_D
_Pm1005MonupRmonMulticastCntIndex_Object=MibTableColumn
pm1005MonupRmonMulticastCntIndex=_Pm1005MonupRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,26,11,2,4,48,1,1),_Pm1005MonupRmonMulticastCntIndex_Type())
pm1005MonupRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonMulticastCntIndex.setStatus(_A)
_Pm1005MonupRmonMulticastCntValuePortn_Type=Counter64
_Pm1005MonupRmonMulticastCntValuePortn_Object=MibTableColumn
pm1005MonupRmonMulticastCntValuePortn=_Pm1005MonupRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,26,11,2,4,48,1,2),_Pm1005MonupRmonMulticastCntValuePortn_Type())
pm1005MonupRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonMulticastCntValuePortn.setStatus(_A)
_Pm1005MonupRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm1005MonupRmonMulticastCntErrorPortn_Object=MibTableColumn
pm1005MonupRmonMulticastCntErrorPortn=_Pm1005MonupRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,48,1,3),_Pm1005MonupRmonMulticastCntErrorPortn_Type())
pm1005MonupRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonMulticastCntErrorPortn.setStatus(_A)
_Pm1005MonupRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm1005MonupRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm1005MonupRmonMulticastCntOverloadPortn=_Pm1005MonupRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,26,11,2,4,48,1,4),_Pm1005MonupRmonMulticastCntOverloadPortn_Type())
pm1005MonupRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1005MonupRmonMulticastCntOverloadPortn.setStatus(_A)
pm1005LineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,30))
pm1005LineTrapNotUrgentGoesOn.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1005LineTrapNotUrgentGoesOn.setStatus(_A)
pm1005LineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,31))
pm1005LineTrapNotUrgentGoesOff.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1005LineTrapNotUrgentGoesOff.setStatus(_A)
pm1005LineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,32))
pm1005LineTrapUrgentGoesOn.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1005LineTrapUrgentGoesOn.setStatus(_A)
pm1005LineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,33))
pm1005LineTrapUrgentGoesOff.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1005LineTrapUrgentGoesOff.setStatus(_A)
pm1005LineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,34))
pm1005LineTrapCritGoesOn.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1005LineTrapCritGoesOn.setStatus(_A)
pm1005LineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,35))
pm1005LineTrapCritGoesOff.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1005LineTrapCritGoesOff.setStatus(_A)
pm1005ClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,40))
pm1005ClientTrapNotUrgentGoesOn.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1005ClientTrapNotUrgentGoesOn.setStatus(_A)
pm1005ClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,41))
pm1005ClientTrapNotUrgentGoesOff.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1005ClientTrapNotUrgentGoesOff.setStatus(_A)
pm1005ClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,42))
pm1005ClientTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1005ClientTrapUrgentGoesOn.setStatus(_A)
pm1005ClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,43))
pm1005ClientTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1005ClientTrapUrgentGoesOff.setStatus(_A)
pm1005ClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,44))
pm1005ClientTrapCritGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1005ClientTrapCritGoesOn.setStatus(_A)
pm1005ClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,45))
pm1005ClientTrapCritGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1005ClientTrapCritGoesOff.setStatus(_A)
pm1005PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,26,10,50))
pm1005PowerTrapUrgentGoesOn.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pm1005PowerTrapUrgentGoesOn.setStatus(_A)
pm1005PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,26,10,51))
pm1005PowerTrapUrgentGoesOff.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pm1005PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Pm1005OtxMode':Pm1005OtxMode,'Pm1005OtxGrid':Pm1005OtxGrid,'Pm1005AdjustValue':Pm1005AdjustValue,'Pm1005OtxChannel':Pm1005OtxChannel,'modulePm1005':modulePm1005,'pm1005alarms':pm1005alarms,'pm1005AlmOther':pm1005AlmOther,'pm1005AlmOtherNurg':pm1005AlmOtherNurg,'pm1005AlmsynthAlm2':pm1005AlmsynthAlm2,'pm1005AlmConfTableSave':pm1005AlmConfTableSave,'pm1005AlmInvUpload':pm1005AlmInvUpload,'pm1005AlmConfTableLoad':pm1005AlmConfTableLoad,'pm1005AlmCorrelatOff':pm1005AlmCorrelatOff,'pm1005AlmMaintenanceOn':pm1005AlmMaintenanceOn,'pm1005AlmOtherUrg':pm1005AlmOtherUrg,'pm1005AlmmodInitFailLevel2':pm1005AlmmodInitFailLevel2,'pm1005AlmLedFail':pm1005AlmLedFail,'pm1005AlmNextColdBootForced':pm1005AlmNextColdBootForced,'pm1005AlmBootUndone':pm1005AlmBootUndone,'pm1005AlmResetHwInitFail':pm1005AlmResetHwInitFail,'pm1005AlmSwInitFail':pm1005AlmSwInitFail,'pm1005AlmmodInitFailLevel3':pm1005AlmmodInitFailLevel3,'pm1005AlmGwIdentFail':pm1005AlmGwIdentFail,'pm1005AlmObmTypeReadFail':pm1005AlmObmTypeReadFail,'pm1005AlmInitModuleFail':pm1005AlmInitModuleFail,'pm1005AlmXfp1InitFail':pm1005AlmXfp1InitFail,'pm1005AlmXfp2InitFail':pm1005AlmXfp2InitFail,'pm1005AlmLine1InitFail':pm1005AlmLine1InitFail,'pm1005AlmLine2InitFail':pm1005AlmLine2InitFail,'pm1005AlmClient1InitFail':pm1005AlmClient1InitFail,'pm1005AlmClient2InitFail':pm1005AlmClient2InitFail,'pm1005AlmClient3InitFail':pm1005AlmClient3InitFail,'pm1005AlmClient4InitFail':pm1005AlmClient4InitFail,'pm1005AlmClient5InitFail':pm1005AlmClient5InitFail,'pm1005AlmClient6InitFail':pm1005AlmClient6InitFail,'pm1005AlmClient7InitFail':pm1005AlmClient7InitFail,'pm1005AlmClient8InitFail':pm1005AlmClient8InitFail,'pm1005AlmOtherCrit':pm1005AlmOtherCrit,'pm1005AlmsynthAlm0':pm1005AlmsynthAlm0,'pm1005AlmModGlobFail':pm1005AlmModGlobFail,_U:pm1005AlmDefFuseA,_T:pm1005AlmDefFuseB,'pm1005AlmClient':pm1005AlmClient,'pm1005AlmClientNurg':pm1005AlmClientNurg,'pm1005AlmsfpWarnDdmTable':pm1005AlmsfpWarnDdmTable,'pm1005AlmsfpWarnDdmEntry':pm1005AlmsfpWarnDdmEntry,_V:pm1005AlmsfpWarnDdmIndex,'pm1005AlmTxPwLowWngPortn':pm1005AlmTxPwLowWngPortn,'pm1005AlmTxPwrHighWngPortn':pm1005AlmTxPwrHighWngPortn,'pm1005AlmTxBiasLowWngPortn':pm1005AlmTxBiasLowWngPortn,'pm1005AlmTxBiasHighWngPortn':pm1005AlmTxBiasHighWngPortn,'pm1005AlmVccLowWngPortn':pm1005AlmVccLowWngPortn,'pm1005AlmVccHighWngPortn':pm1005AlmVccHighWngPortn,'pm1005AlmTempLowWngPortn':pm1005AlmTempLowWngPortn,'pm1005AlmTempHighWngPortn':pm1005AlmTempHighWngPortn,'pm1005AlmRxPwrLowWngPortn':pm1005AlmRxPwrLowWngPortn,'pm1005AlmRxPwrHighWngPortn':pm1005AlmRxPwrHighWngPortn,'pm1005AlmClientUrg':pm1005AlmClientUrg,'pm1005AlmsfpAlmDdmTable':pm1005AlmsfpAlmDdmTable,'pm1005AlmsfpAlmDdmEntry':pm1005AlmsfpAlmDdmEntry,_W:pm1005AlmsfpAlmDdmIndex,'pm1005AlmTxPwrLowAlaPortn':pm1005AlmTxPwrLowAlaPortn,'pm1005AlmTxPwrHighAlaPortn':pm1005AlmTxPwrHighAlaPortn,'pm1005AlmTxBiasLowAlaPortn':pm1005AlmTxBiasLowAlaPortn,'pm1005AlmTxBiasHighAlaPortn':pm1005AlmTxBiasHighAlaPortn,'pm1005AlmVccLowAlaPortn':pm1005AlmVccLowAlaPortn,'pm1005AlmVccHighAlaPortn':pm1005AlmVccHighAlaPortn,'pm1005AlmTempLowAlaPortn':pm1005AlmTempLowAlaPortn,'pm1005AlmTempHighAlaPortn':pm1005AlmTempHighAlaPortn,'pm1005AlmRxPwrLowAlaPortn':pm1005AlmRxPwrLowAlaPortn,'pm1005AlmRxPwrHighAlaPortn':pm1005AlmRxPwrHighAlaPortn,'pm1005AlmClientCrit':pm1005AlmClientCrit,'pm1005AlmsynthAlmPortTable':pm1005AlmsynthAlmPortTable,'pm1005AlmsynthAlmPortEntry':pm1005AlmsynthAlmPortEntry,_X:pm1005AlmsynthAlmPortIndex,'pm1005AlmSfpAbsentPortn':pm1005AlmSfpAbsentPortn,'pm1005AlmDdmAbsentPortn':pm1005AlmDdmAbsentPortn,_S:pm1005AlmHwFailAccPortn,'pm1005AlmDwLsdPortn':pm1005AlmDwLsdPortn,'pm1005AlmClientLocalOosPortn':pm1005AlmClientLocalOosPortn,'pm1005AlmClientRemoteOosPortn':pm1005AlmClientRemoteOosPortn,'pm1005AlmDwCaisPortn':pm1005AlmDwCaisPortn,_P:pm1005AlmSfpDdmWarningPortn,_Q:pm1005AlmSfpDdmAlmPortn,_R:pm1005AlmFailAccPortn,'pm1005AlmUpCsfPortn':pm1005AlmUpCsfPortn,'pm1005AlmaccessioAlmTable':pm1005AlmaccessioAlmTable,'pm1005AlmaccessioAlmEntry':pm1005AlmaccessioAlmEntry,_Y:pm1005AlmaccessioAlmIndex,'pm1005AlmDwLasFailPortn':pm1005AlmDwLasFailPortn,'pm1005AlmUpLosPortn':pm1005AlmUpLosPortn,'pm1005AlmmapperDeAlmTable':pm1005AlmmapperDeAlmTable,'pm1005AlmmapperDeAlmEntry':pm1005AlmmapperDeAlmEntry,_Z:pm1005AlmmapperDeAlmIndex,'pm1005AlmUpAccOosPortn':pm1005AlmUpAccOosPortn,'pm1005AlmUpBufferOvlPortn':pm1005AlmUpBufferOvlPortn,'pm1005AlmDwCsfDetPortn':pm1005AlmDwCsfDetPortn,'pm1005AlmDwBufferOvlPortn':pm1005AlmDwBufferOvlPortn,'pm1005AlmLine':pm1005AlmLine,'pm1005AlmLineNurg':pm1005AlmLineNurg,'pm1005AlmlineXfp1WarningsTable':pm1005AlmlineXfp1WarningsTable,'pm1005AlmlineXfp1WarningsEntry':pm1005AlmlineXfp1WarningsEntry,_a:pm1005AlmlineXfp1WarningsIndex,'pm1005AlmTxPowerLowWarningPortn':pm1005AlmTxPowerLowWarningPortn,'pm1005AlmTxPowerHighWarningPortn':pm1005AlmTxPowerHighWarningPortn,'pm1005AlmTxBiasLowWarningPortn':pm1005AlmTxBiasLowWarningPortn,'pm1005AlmTxBiasHighWarningPortn':pm1005AlmTxBiasHighWarningPortn,'pm1005AlmTempLowWarningPortn':pm1005AlmTempLowWarningPortn,'pm1005AlmTempHighWarningPortn':pm1005AlmTempHighWarningPortn,'pm1005AlmRxPowerLowWarningPortn':pm1005AlmRxPowerLowWarningPortn,'pm1005AlmRxPowerHighWarningPortn':pm1005AlmRxPowerHighWarningPortn,'pm1005AlmlineOtx1TlhWarningsTable':pm1005AlmlineOtx1TlhWarningsTable,'pm1005AlmlineOtx1TlhWarningsEntry':pm1005AlmlineOtx1TlhWarningsEntry,_b:pm1005AlmlineOtx1TlhWarningsIndex,'pm1005AlmLineModulatorAgingHighWarningPortn':pm1005AlmLineModulatorAgingHighWarningPortn,'pm1005AlmLineAgingHighWarningPortn':pm1005AlmLineAgingHighWarningPortn,'pm1005AlmLineFreqDevHighWarningPortn':pm1005AlmLineFreqDevHighWarningPortn,'pm1005AlmLineLaserTempHighWarningPortn':pm1005AlmLineLaserTempHighWarningPortn,'pm1005AlmLineUrg':pm1005AlmLineUrg,'pm1005AlmdfrmBerTable':pm1005AlmdfrmBerTable,'pm1005AlmdfrmBerEntry':pm1005AlmdfrmBerEntry,_c:pm1005AlmdfrmBerIndex,'pm1005AlmLineSignalDegradePortn':pm1005AlmLineSignalDegradePortn,'pm1005AlmLineSignalFailPortn':pm1005AlmLineSignalFailPortn,'pm1005AlmLineDegradePortn':pm1005AlmLineDegradePortn,'pm1005AlmlineXfp1AlarmTable':pm1005AlmlineXfp1AlarmTable,'pm1005AlmlineXfp1AlarmEntry':pm1005AlmlineXfp1AlarmEntry,_d:pm1005AlmlineXfp1AlarmIndex,'pm1005AlmTxPowerLowAlarmPortn':pm1005AlmTxPowerLowAlarmPortn,'pm1005AlmTxPowerHighAlarmPortn':pm1005AlmTxPowerHighAlarmPortn,'pm1005AlmTxBiasLowAlarmPortn':pm1005AlmTxBiasLowAlarmPortn,'pm1005AlmTxBiasHighAlarmPortn':pm1005AlmTxBiasHighAlarmPortn,'pm1005AlmTempLowAlarmPortn':pm1005AlmTempLowAlarmPortn,'pm1005AlmTempHighAlarmPortn':pm1005AlmTempHighAlarmPortn,'pm1005AlmRxPowerLowAlarmPortn':pm1005AlmRxPowerLowAlarmPortn,'pm1005AlmRxPowerHighAlarmPortn':pm1005AlmRxPowerHighAlarmPortn,'pm1005AlmlineXfp1SupplyAlarmTable':pm1005AlmlineXfp1SupplyAlarmTable,'pm1005AlmlineXfp1SupplyAlarmEntry':pm1005AlmlineXfp1SupplyAlarmEntry,_e:pm1005AlmlineXfp1SupplyAlarmIndex,'pm1005AlmVee5LowAlarmPortn':pm1005AlmVee5LowAlarmPortn,'pm1005AlmVee5HighAlarmPortn':pm1005AlmVee5HighAlarmPortn,'pm1005AlmVcc2LowAlarmPortn':pm1005AlmVcc2LowAlarmPortn,'pm1005AlmVcc2HighAlarmPortn':pm1005AlmVcc2HighAlarmPortn,'pm1005AlmVcc3LowAlarmPortn':pm1005AlmVcc3LowAlarmPortn,'pm1005AlmVcc3HighAlarmPortn':pm1005AlmVcc3HighAlarmPortn,'pm1005AlmVcc5LowAlarmPortn':pm1005AlmVcc5LowAlarmPortn,'pm1005AlmVcc5HighAlarmPortn':pm1005AlmVcc5HighAlarmPortn,'pm1005AlmVee5LowWarningPortn':pm1005AlmVee5LowWarningPortn,'pm1005AlmVee5HighWarningPortn':pm1005AlmVee5HighWarningPortn,'pm1005AlmVcc2LowWarningPortn':pm1005AlmVcc2LowWarningPortn,'pm1005AlmVcc2HighWarningPortn':pm1005AlmVcc2HighWarningPortn,'pm1005AlmVcc3LowWarningPortn':pm1005AlmVcc3LowWarningPortn,'pm1005AlmVcc3HighWarningPortn':pm1005AlmVcc3HighWarningPortn,'pm1005AlmVcc5LowWarningPortn':pm1005AlmVcc5LowWarningPortn,'pm1005AlmVcc5HighWarningPortn':pm1005AlmVcc5HighWarningPortn,'pm1005AlmlineOtx1TlhAlarmsTable':pm1005AlmlineOtx1TlhAlarmsTable,'pm1005AlmlineOtx1TlhAlarmsEntry':pm1005AlmlineOtx1TlhAlarmsEntry,_f:pm1005AlmlineOtx1TlhAlarmsIndex,'pm1005AlmLineModulatorAgingHighAlaPortn':pm1005AlmLineModulatorAgingHighAlaPortn,'pm1005AlmLineAgingHighAlaPortn':pm1005AlmLineAgingHighAlaPortn,'pm1005AlmLineFreqDevHighAlaPortn':pm1005AlmLineFreqDevHighAlaPortn,'pm1005AlmLineLaserTempHighAlaPortn':pm1005AlmLineLaserTempHighAlaPortn,'pm1005AlmLineCrit':pm1005AlmLineCrit,'pm1005AlmsynthAlmLineTable':pm1005AlmsynthAlmLineTable,'pm1005AlmsynthAlmLineEntry':pm1005AlmsynthAlmLineEntry,_g:pm1005AlmsynthAlmLineIndex,'pm1005AlmXfpAbsentPortn':pm1005AlmXfpAbsentPortn,'pm1005AlmXfpInitNotComplPortn':pm1005AlmXfpInitNotComplPortn,_O:pm1005AlmLineHwFailPortn,'pm1005AlmXfpTxOffPortn':pm1005AlmXfpTxOffPortn,'pm1005AlmLineLocalOosPortn':pm1005AlmLineLocalOosPortn,'pm1005AlmUpRdiInsPortn':pm1005AlmUpRdiInsPortn,_L:pm1005AlmLineDdmWarningPortn,_M:pm1005AlmLineDdmAlmPortn,_N:pm1005AlmLineFailPortn,'pm1005AlmLineActivePortn':pm1005AlmLineActivePortn,'pm1005AlmdfrmAlmTable':pm1005AlmdfrmAlmTable,'pm1005AlmdfrmAlmEntry':pm1005AlmdfrmAlmEntry,_h:pm1005AlmdfrmAlmIndex,'pm1005AlmDwAisDetPortn':pm1005AlmDwAisDetPortn,'pm1005AlmDwRdiDetPortn':pm1005AlmDwRdiDetPortn,'pm1005AlmDwOofPortn':pm1005AlmDwOofPortn,'pm1005AlmDwLofPortn':pm1005AlmDwLofPortn,'pm1005AlmlineSyncAlarmsTable':pm1005AlmlineSyncAlarmsTable,'pm1005AlmlineSyncAlarmsEntry':pm1005AlmlineSyncAlarmsEntry,_i:pm1005AlmlineSyncAlarmsIndex,'pm1005AlmDwLockerrPortn':pm1005AlmDwLockerrPortn,'pm1005AlmUpLockerrPortn':pm1005AlmUpLockerrPortn,'pm1005AlmDwLosPortn':pm1005AlmDwLosPortn,'pm1005AlmlineXfp1AlarmsTable':pm1005AlmlineXfp1AlarmsTable,'pm1005AlmlineXfp1AlarmsEntry':pm1005AlmlineXfp1AlarmsEntry,_j:pm1005AlmlineXfp1AlarmsIndex,'pm1005AlmModNrPortn':pm1005AlmModNrPortn,'pm1005AlmRxCdrNotLockedPortn':pm1005AlmRxCdrNotLockedPortn,'pm1005AlmRxNrPortn':pm1005AlmRxNrPortn,'pm1005AlmTxCdrNotLockedPortn':pm1005AlmTxCdrNotLockedPortn,'pm1005AlmTxFaultPortn':pm1005AlmTxFaultPortn,'pm1005AlmTxNrPortn':pm1005AlmTxNrPortn,'pm1005AlmWavelengthUnlockedPortn':pm1005AlmWavelengthUnlockedPortn,'pm1005AlmTecFaultPortn':pm1005AlmTecFaultPortn,'pm1005AlmApdSupplyFaultPortn':pm1005AlmApdSupplyFaultPortn,'pm1005measures':pm1005measures,'pm1005MesrOther':pm1005MesrOther,'pm1005Mesrsynth0':pm1005Mesrsynth0,'pm1005Mesrsynth1':pm1005Mesrsynth1,'pm1005MesrClient':pm1005MesrClient,'pm1005MesrtempMeasTable':pm1005MesrtempMeasTable,'pm1005MesrtempMeasEntry':pm1005MesrtempMeasEntry,_k:pm1005MesrtempMeasIndex,'pm1005MesrtempMeasPortn':pm1005MesrtempMeasPortn,'pm1005MesrvoltMeasTable':pm1005MesrvoltMeasTable,'pm1005MesrvoltMeasEntry':pm1005MesrvoltMeasEntry,_l:pm1005MesrvoltMeasIndex,'pm1005MesrvoltMeasPortn':pm1005MesrvoltMeasPortn,'pm1005MesrbiasMeasTable':pm1005MesrbiasMeasTable,'pm1005MesrbiasMeasEntry':pm1005MesrbiasMeasEntry,_m:pm1005MesrbiasMeasIndex,'pm1005MesrbiasMeasPortn':pm1005MesrbiasMeasPortn,'pm1005MesrtxpwrMeasTable':pm1005MesrtxpwrMeasTable,'pm1005MesrtxpwrMeasEntry':pm1005MesrtxpwrMeasEntry,_n:pm1005MesrtxpwrMeasIndex,'pm1005MesrtxpwrMeasPortn':pm1005MesrtxpwrMeasPortn,'pm1005MesrrxpwrMeasTable':pm1005MesrrxpwrMeasTable,'pm1005MesrrxpwrMeasEntry':pm1005MesrrxpwrMeasEntry,_o:pm1005MesrrxpwrMeasIndex,'pm1005MesrrxpwrMeasPortn':pm1005MesrrxpwrMeasPortn,'pm1005MesrLine':pm1005MesrLine,'pm1005Mesrxfp1LxModTempMeasTable':pm1005Mesrxfp1LxModTempMeasTable,'pm1005Mesrxfp1LxModTempMeasEntry':pm1005Mesrxfp1LxModTempMeasEntry,_p:pm1005Mesrxfp1LxModTempMeasIndex,'pm1005Mesrxfp1LxModTempMeasPortn':pm1005Mesrxfp1LxModTempMeasPortn,'pm1005Mesrxfp1ReservedTable':pm1005Mesrxfp1ReservedTable,'pm1005Mesrxfp1ReservedEntry':pm1005Mesrxfp1ReservedEntry,_q:pm1005Mesrxfp1ReservedIndex,'pm1005Mesrxfp1ReservedPortn':pm1005Mesrxfp1ReservedPortn,'pm1005Mesrxfp1LoBiasCurrentMeasTable':pm1005Mesrxfp1LoBiasCurrentMeasTable,'pm1005Mesrxfp1LoBiasCurrentMeasEntry':pm1005Mesrxfp1LoBiasCurrentMeasEntry,_r:pm1005Mesrxfp1LoBiasCurrentMeasIndex,'pm1005Mesrxfp1LoBiasCurrentMeasPortn':pm1005Mesrxfp1LoBiasCurrentMeasPortn,'pm1005Mesrxfp1LoTxPowerMeasTable':pm1005Mesrxfp1LoTxPowerMeasTable,'pm1005Mesrxfp1LoTxPowerMeasEntry':pm1005Mesrxfp1LoTxPowerMeasEntry,_s:pm1005Mesrxfp1LoTxPowerMeasIndex,'pm1005Mesrxfp1LoTxPowerMeasPortn':pm1005Mesrxfp1LoTxPowerMeasPortn,'pm1005Mesrxfp1LiRxPowerMeasTable':pm1005Mesrxfp1LiRxPowerMeasTable,'pm1005Mesrxfp1LiRxPowerMeasEntry':pm1005Mesrxfp1LiRxPowerMeasEntry,_t:pm1005Mesrxfp1LiRxPowerMeasIndex,'pm1005Mesrxfp1LiRxPowerMeasPortn':pm1005Mesrxfp1LiRxPowerMeasPortn,'pm1005Mesrxfp1LxAux1MeasTable':pm1005Mesrxfp1LxAux1MeasTable,'pm1005Mesrxfp1LxAux1MeasEntry':pm1005Mesrxfp1LxAux1MeasEntry,_u:pm1005Mesrxfp1LxAux1MeasIndex,'pm1005Mesrxfp1LxAux1MeasPortn':pm1005Mesrxfp1LxAux1MeasPortn,'pm1005Mesrxfp1LxAux2MeasTable':pm1005Mesrxfp1LxAux2MeasTable,'pm1005Mesrxfp1LxAux2MeasEntry':pm1005Mesrxfp1LxAux2MeasEntry,_v:pm1005Mesrxfp1LxAux2MeasIndex,'pm1005Mesrxfp1LxAux2MeasPortn':pm1005Mesrxfp1LxAux2MeasPortn,'pm1005Mesrotx1AgingTable':pm1005Mesrotx1AgingTable,'pm1005Mesrotx1AgingEntry':pm1005Mesrotx1AgingEntry,_w:pm1005Mesrotx1AgingIndex,'pm1005Mesrotx1AgingPortn':pm1005Mesrotx1AgingPortn,'pm1005Mesrotx1LaserTemperatureTable':pm1005Mesrotx1LaserTemperatureTable,'pm1005Mesrotx1LaserTemperatureEntry':pm1005Mesrotx1LaserTemperatureEntry,_x:pm1005Mesrotx1LaserTemperatureIndex,'pm1005Mesrotx1LaserTemperaturePortn':pm1005Mesrotx1LaserTemperaturePortn,'pm1005Mesrotx1FreqDeviationTable':pm1005Mesrotx1FreqDeviationTable,'pm1005Mesrotx1FreqDeviationEntry':pm1005Mesrotx1FreqDeviationEntry,_y:pm1005Mesrotx1FreqDeviationIndex,'pm1005Mesrotx1FreqDeviationPortn':pm1005Mesrotx1FreqDeviationPortn,'pm1005Mesrotx1LaserWvlengthTable':pm1005Mesrotx1LaserWvlengthTable,'pm1005Mesrotx1LaserWvlengthEntry':pm1005Mesrotx1LaserWvlengthEntry,_z:pm1005Mesrotx1LaserWvlengthIndex,'pm1005Mesrotx1LaserWvlengthPortn':pm1005Mesrotx1LaserWvlengthPortn,'pm1005counters':pm1005counters,'pm1005CntOther':pm1005CntOther,'pm1005CntClient':pm1005CntClient,'pm1005CntupRaRemCntTable':pm1005CntupRaRemCntTable,'pm1005CntupRaRemCntEntry':pm1005CntupRaRemCntEntry,_A0:pm1005CntupRaRemCntIndex,'pm1005CntupRaRemCntValuePortn':pm1005CntupRaRemCntValuePortn,'pm1005CntupRaRemCntErrorPortn':pm1005CntupRaRemCntErrorPortn,'pm1005CntupRaRemCntOverloadPortn':pm1005CntupRaRemCntOverloadPortn,'pm1005CntupRaInsCntTable':pm1005CntupRaInsCntTable,'pm1005CntupRaInsCntEntry':pm1005CntupRaInsCntEntry,_A1:pm1005CntupRaInsCntIndex,'pm1005CntupRaInsCntValuePortn':pm1005CntupRaInsCntValuePortn,'pm1005CntupRaInsCntErrorPortn':pm1005CntupRaInsCntErrorPortn,'pm1005CntupRaInsCntOverloadPortn':pm1005CntupRaInsCntOverloadPortn,'pm1005CntupRdErrCntTable':pm1005CntupRdErrCntTable,'pm1005CntupRdErrCntEntry':pm1005CntupRdErrCntEntry,_A2:pm1005CntupRdErrCntIndex,'pm1005CntupRdErrCntValuePortn':pm1005CntupRdErrCntValuePortn,'pm1005CntupRdErrCntErrorPortn':pm1005CntupRdErrCntErrorPortn,'pm1005CntupRdErrCntOverloadPortn':pm1005CntupRdErrCntOverloadPortn,'pm1005CntupTimCntTable':pm1005CntupTimCntTable,'pm1005CntupTimCntEntry':pm1005CntupTimCntEntry,_A3:pm1005CntupTimCntIndex,'pm1005CntupTimCntValuePortn':pm1005CntupTimCntValuePortn,'pm1005CntupTimCntErrorPortn':pm1005CntupTimCntErrorPortn,'pm1005CntupTimCntOverloadPortn':pm1005CntupTimCntOverloadPortn,'pm1005CntupCvErrCntTable':pm1005CntupCvErrCntTable,'pm1005CntupCvErrCntEntry':pm1005CntupCvErrCntEntry,_A4:pm1005CntupCvErrCntIndex,'pm1005CntupCvErrCntValuePortn':pm1005CntupCvErrCntValuePortn,'pm1005CntupCvErrCntErrorPortn':pm1005CntupCvErrCntErrorPortn,'pm1005CntupCvErrCntOverloadPortn':pm1005CntupCvErrCntOverloadPortn,'pm1005CntdwCbipCntTable':pm1005CntdwCbipCntTable,'pm1005CntdwCbipCntEntry':pm1005CntdwCbipCntEntry,_A5:pm1005CntdwCbipCntIndex,'pm1005CntdwCbipCntValuePortn':pm1005CntdwCbipCntValuePortn,'pm1005CntdwCbipCntErrorPortn':pm1005CntdwCbipCntErrorPortn,'pm1005CntdwCbipCntOverloadPortn':pm1005CntdwCbipCntOverloadPortn,'pm1005CntdwTimCntTable':pm1005CntdwTimCntTable,'pm1005CntdwTimCntEntry':pm1005CntdwTimCntEntry,_A6:pm1005CntdwTimCntIndex,'pm1005CntdwTimCntValuePortn':pm1005CntdwTimCntValuePortn,'pm1005CntdwTimCntErrorPortn':pm1005CntdwTimCntErrorPortn,'pm1005CntdwTimCntOverloadPortn':pm1005CntdwTimCntOverloadPortn,'pm1005CntLine':pm1005CntLine,'pm1005CntdfrmB1ErrCntTable':pm1005CntdfrmB1ErrCntTable,'pm1005CntdfrmB1ErrCntEntry':pm1005CntdfrmB1ErrCntEntry,_A7:pm1005CntdfrmB1ErrCntIndex,'pm1005CntdfrmB1ErrCntValuePortn':pm1005CntdfrmB1ErrCntValuePortn,'pm1005CntdfrmB1ErrCntErrorPortn':pm1005CntdfrmB1ErrCntErrorPortn,'pm1005CntdfrmB1ErrCntOverloadPortn':pm1005CntdfrmB1ErrCntOverloadPortn,'pm1005CntdfrmTimCntTable':pm1005CntdfrmTimCntTable,'pm1005CntdfrmTimCntEntry':pm1005CntdfrmTimCntEntry,_A8:pm1005CntdfrmTimCntIndex,'pm1005CntdfrmTimCntValuePortn':pm1005CntdfrmTimCntValuePortn,'pm1005CntdfrmTimCntErrorPortn':pm1005CntdfrmTimCntErrorPortn,'pm1005CntdfrmTimCntOverloadPortn':pm1005CntdfrmTimCntOverloadPortn,'pm1005CntdfrmPrimLineErrCntTable':pm1005CntdfrmPrimLineErrCntTable,'pm1005CntdfrmPrimLineErrCntEntry':pm1005CntdfrmPrimLineErrCntEntry,_A9:pm1005CntdfrmPrimLineErrCntIndex,'pm1005CntdfrmPrimLineErrCntValuePortn':pm1005CntdfrmPrimLineErrCntValuePortn,'pm1005CntdfrmPrimLineErrCntErrorPortn':pm1005CntdfrmPrimLineErrCntErrorPortn,'pm1005CntdfrmPrimLineErrCntOverloadPortn':pm1005CntdfrmPrimLineErrCntOverloadPortn,'pm1005CntCountersReset':pm1005CntCountersReset,'pm1005CntCountersStop':pm1005CntCountersStop,'pm1005controlsWrite':pm1005controlsWrite,'pm1005CtrlOther':pm1005CtrlOther,'pm1005CtrlconfMgnt1':pm1005CtrlconfMgnt1,'pm1005CtrlConf1Load1':pm1005CtrlConf1Load1,'pm1005CtrlConf2Load1':pm1005CtrlConf2Load1,'pm1005CtrlConf2Flash1':pm1005CtrlConf2Flash1,'pm1005CtrlConf2Clear1':pm1005CtrlConf2Clear1,'pm1005Ctrlsynth4':pm1005Ctrlsynth4,'pm1005CtrlCorrelatOn':pm1005CtrlCorrelatOn,'pm1005CtrlCorrelatOff':pm1005CtrlCorrelatOff,'pm1005CtrlswMgnt':pm1005CtrlswMgnt,'pm1005CtrlColdReset':pm1005CtrlColdReset,'pm1005CtrlWarmReset':pm1005CtrlWarmReset,'pm1005CtrlLoadSwBank1':pm1005CtrlLoadSwBank1,'pm1005CtrlLoadSwBank2':pm1005CtrlLoadSwBank2,'pm1005CtrlgwMgnt':pm1005CtrlgwMgnt,'pm1005CtrlCurrentGwReset':pm1005CtrlCurrentGwReset,'pm1005CtrlLoadGwBank1':pm1005CtrlLoadGwBank1,'pm1005CtrlLoadGwBank2':pm1005CtrlLoadGwBank2,'pm1005CtrlLoadGwBank3':pm1005CtrlLoadGwBank3,'pm1005CtrlLoadGwBank4':pm1005CtrlLoadGwBank4,'pm1005CtrlledTest':pm1005CtrlledTest,'pm1005CtrlGreenLed':pm1005CtrlGreenLed,'pm1005CtrlRedLed':pm1005CtrlRedLed,'pm1005CtrlLedOff':pm1005CtrlLedOff,'pm1005CtrlmoduleOosMode':pm1005CtrlmoduleOosMode,'pm1005CtrlModuleOosMode':pm1005CtrlModuleOosMode,'pm1005CtrlmaintenanceMode':pm1005CtrlmaintenanceMode,'pm1005CtrlMaintenanceMode':pm1005CtrlMaintenanceMode,'pm1005CtrldccEnable':pm1005CtrldccEnable,'pm1005CtrlDccEnable':pm1005CtrlDccEnable,'pm1005CtrlClient':pm1005CtrlClient,'pm1005CtrlaccessLoopTable':pm1005CtrlaccessLoopTable,'pm1005CtrlaccessLoopEntry':pm1005CtrlaccessLoopEntry,_AA:pm1005CtrlaccessLoopIndex,'pm1005CtrlaccessLoopPortn':pm1005CtrlaccessLoopPortn,'pm1005CtrlportOosModeTable':pm1005CtrlportOosModeTable,'pm1005CtrlportOosModeEntry':pm1005CtrlportOosModeEntry,_AB:pm1005CtrlportOosModeIndex,'pm1005CtrlportOosModePortn':pm1005CtrlportOosModePortn,'pm1005CtrlsfpOnCtrlTable':pm1005CtrlsfpOnCtrlTable,'pm1005CtrlsfpOnCtrlEntry':pm1005CtrlsfpOnCtrlEntry,_AC:pm1005CtrlsfpOnCtrlIndex,'pm1005CtrlsfpOnCtrlPortn':pm1005CtrlsfpOnCtrlPortn,'pm1005CtrlsfpOffCtrlTable':pm1005CtrlsfpOffCtrlTable,'pm1005CtrlsfpOffCtrlEntry':pm1005CtrlsfpOffCtrlEntry,_AD:pm1005CtrlsfpOffCtrlIndex,'pm1005CtrlsfpOffCtrlPortn':pm1005CtrlsfpOffCtrlPortn,'pm1005CtrlcsfUpInsTable':pm1005CtrlcsfUpInsTable,'pm1005CtrlcsfUpInsEntry':pm1005CtrlcsfUpInsEntry,_AE:pm1005CtrlcsfUpInsIndex,'pm1005CtrlcsfUpInsPortn':pm1005CtrlcsfUpInsPortn,'pm1005CtrlcaisDwInsTable':pm1005CtrlcaisDwInsTable,'pm1005CtrlcaisDwInsEntry':pm1005CtrlcaisDwInsEntry,_AF:pm1005CtrlcaisDwInsIndex,'pm1005CtrlcaisDwInsPortn':pm1005CtrlcaisDwInsPortn,'pm1005CtrlclientAccessTermLoopTable':pm1005CtrlclientAccessTermLoopTable,'pm1005CtrlclientAccessTermLoopEntry':pm1005CtrlclientAccessTermLoopEntry,_AG:pm1005CtrlclientAccessTermLoopIndex,'pm1005CtrlclientAccessTermLoopPortn':pm1005CtrlclientAccessTermLoopPortn,'pm1005CtrlprotocolTable':pm1005CtrlprotocolTable,'pm1005CtrlprotocolEntry':pm1005CtrlprotocolEntry,_AH:pm1005CtrlprotocolIndex,'pm1005CtrlprotocolPortn':pm1005CtrlprotocolPortn,'pm1005CtrlLine':pm1005CtrlLine,'pm1005CtrlcommAccessLoop':pm1005CtrlcommAccessLoop,'pm1005CtrlCommAccessloop':pm1005CtrlCommAccessloop,'pm1005CtrllineLoop':pm1005CtrllineLoop,'pm1005CtrlLineLoop':pm1005CtrlLineLoop,'pm1005CtrlmsAis':pm1005CtrlmsAis,'pm1005CtrlMsAis':pm1005CtrlMsAis,'pm1005CtrlfecDisableTable':pm1005CtrlfecDisableTable,'pm1005CtrlfecDisableEntry':pm1005CtrlfecDisableEntry,_AI:pm1005CtrlfecDisableIndex,'pm1005CtrlfecDisablePortn':pm1005CtrlfecDisablePortn,'pm1005CtrlProtMgnt':pm1005CtrlProtMgnt,'pm1005CtrlLineNumber':pm1005CtrlLineNumber,'pm1005CtrlProtMode':pm1005CtrlProtMode,'pm1005CtrllineOosModeTable':pm1005CtrllineOosModeTable,'pm1005CtrllineOosModeEntry':pm1005CtrllineOosModeEntry,_AJ:pm1005CtrllineOosModeIndex,'pm1005CtrllineOosModePortn':pm1005CtrllineOosModePortn,'pm1005CtrlxfpOnoffTable':pm1005CtrlxfpOnoffTable,'pm1005CtrlxfpOnoffEntry':pm1005CtrlxfpOnoffEntry,_AK:pm1005CtrlxfpOnoffIndex,'pm1005CtrlxfpOnoffPortn':pm1005CtrlxfpOnoffPortn,'pm1005CtrlxfpLineLoopTable':pm1005CtrlxfpLineLoopTable,'pm1005CtrlxfpLineLoopEntry':pm1005CtrlxfpLineLoopEntry,_AL:pm1005CtrlxfpLineLoopIndex,'pm1005CtrlxfpLineLoopPortn':pm1005CtrlxfpLineLoopPortn,'pm1005CtrlxfpXfiLoopTable':pm1005CtrlxfpXfiLoopTable,'pm1005CtrlxfpXfiLoopEntry':pm1005CtrlxfpXfiLoopEntry,_AM:pm1005CtrlxfpXfiLoopIndex,'pm1005CtrlxfpXfiLoopPortn':pm1005CtrlxfpXfiLoopPortn,'pm1005CtrllineTunableChannelTable':pm1005CtrllineTunableChannelTable,'pm1005CtrllineTunableChannelEntry':pm1005CtrllineTunableChannelEntry,_AN:pm1005CtrllineTunableChannelIndex,'pm1005CtrllineTunableChannelPortn':pm1005CtrllineTunableChannelPortn,'pm1005CtrllinePhotodiodeModeTable':pm1005CtrllinePhotodiodeModeTable,'pm1005CtrllinePhotodiodeModeEntry':pm1005CtrllinePhotodiodeModeEntry,_AO:pm1005CtrllinePhotodiodeModeIndex,'pm1005CtrllinePhotodiodeModePortn':pm1005CtrllinePhotodiodeModePortn,'pm1005CtrllinePhotodiodeValueTable':pm1005CtrllinePhotodiodeValueTable,'pm1005CtrllinePhotodiodeValueEntry':pm1005CtrllinePhotodiodeValueEntry,_AP:pm1005CtrllinePhotodiodeValueIndex,'pm1005CtrllinePhotodiodeValuePortn':pm1005CtrllinePhotodiodeValuePortn,'pm1005CtrllinePowerLaserTable':pm1005CtrllinePowerLaserTable,'pm1005CtrllinePowerLaserEntry':pm1005CtrllinePowerLaserEntry,_AQ:pm1005CtrllinePowerLaserIndex,'pm1005CtrllinePowerLaserPortn':pm1005CtrllinePowerLaserPortn,'pm1005ri':pm1005ri,'pm1005riTable':pm1005riTable,'pm1005RinvSfpTable':pm1005RinvSfpTable,'pm1005RinvSfpEntry':pm1005RinvSfpEntry,_AR:pm1005RinvSfpIndex,'pm1005Rinvsfp':pm1005Rinvsfp,'pm1005RinvLineTable':pm1005RinvLineTable,'pm1005RinvLineEntry':pm1005RinvLineEntry,_AS:pm1005RinvLineIndex,'pm1005RinvxfpLine':pm1005RinvxfpLine,'pm1005RinvReloadInventory':pm1005RinvReloadInventory,'pm1005RinvHwPlatform':pm1005RinvHwPlatform,'pm1005RinvModulePlatform':pm1005RinvModulePlatform,'pm1005RinvSwPlatform':pm1005RinvSwPlatform,'pm1005RinvGwPlatform':pm1005RinvGwPlatform,'pm1005download':pm1005download,'pm1005DwlOther':pm1005DwlOther,'pm1005DwlrestartProcess':pm1005DwlrestartProcess,'pm1005DwlWarmRestartProcessed':pm1005DwlWarmRestartProcessed,'pm1005DwlColdRestartProcessed':pm1005DwlColdRestartProcessed,'pm1005DwlswBanksUsed':pm1005DwlswBanksUsed,'pm1005DwlSwBank1Used':pm1005DwlSwBank1Used,'pm1005DwlSwBank2Used':pm1005DwlSwBank2Used,'pm1005DwlSwBank1Notempty':pm1005DwlSwBank1Notempty,'pm1005DwlSwBank2Notempty':pm1005DwlSwBank2Notempty,'pm1005DwlgwBanksUsed':pm1005DwlgwBanksUsed,'pm1005DwlGwBank1Used':pm1005DwlGwBank1Used,'pm1005DwlGwBank2Used':pm1005DwlGwBank2Used,'pm1005DwlGwBank3Used':pm1005DwlGwBank3Used,'pm1005DwlGwBank4Used':pm1005DwlGwBank4Used,'pm1005DwlGwBank1Notempty':pm1005DwlGwBank1Notempty,'pm1005DwlGwBank2Notempty':pm1005DwlGwBank2Notempty,'pm1005DwlGwBank3Notempty':pm1005DwlGwBank3Notempty,'pm1005DwlGwBank4Notempty':pm1005DwlGwBank4Notempty,'pm1005DwlClient':pm1005DwlClient,'pm1005DwlLine':pm1005DwlLine,'pm1005Config':pm1005Config,'pm1005CfgAccessCAisCsf':pm1005CfgAccessCAisCsf,'pm1005CfgClientcaiscsfTable':pm1005CfgClientcaiscsfTable,'pm1005CfgClientcaiscsfEntry':pm1005CfgClientcaiscsfEntry,_AT:pm1005CfgClientcaiscsfIndex,'pm1005CfgCAisModePortn':pm1005CfgCAisModePortn,'pm1005CfgUpAccessioAlmPortn':pm1005CfgUpAccessioAlmPortn,'pm1005CfgUpMapperDeAlmPortn':pm1005CfgUpMapperDeAlmPortn,'pm1005CfgDownAccessioAlmPortn':pm1005CfgDownAccessioAlmPortn,'pm1005CfgDownMapperDeAlmPortn':pm1005CfgDownMapperDeAlmPortn,'pm1005CfgDownDfrmAlmPortn':pm1005CfgDownDfrmAlmPortn,'pm1005CfgDownLineSyncAlarmsPortn':pm1005CfgDownLineSyncAlarmsPortn,'pm1005CfgStartup':pm1005CfgStartup,'pm1005CfgClientStartupTable':pm1005CfgClientStartupTable,'pm1005CfgClientStartupEntry':pm1005CfgClientStartupEntry,_AU:pm1005CfgClientStartupIndex,'pm1005CfgSystConfPortPortn':pm1005CfgSystConfPortPortn,'pm1005CfgNetConfPortPortn':pm1005CfgNetConfPortPortn,'pm1005tablelineStartup':pm1005tablelineStartup,'pm1005CfgsystConfLine1':pm1005CfgsystConfLine1,'pm1005CfglineOptions1':pm1005CfglineOptions1,'pm1005CfgsystConfLine2':pm1005CfgsystConfLine2,'pm1005CfglineSelection':pm1005CfglineSelection,'pm1005CfgXfpTable':pm1005CfgXfpTable,'pm1005CfgXfpEntry':pm1005CfgXfpEntry,_AV:pm1005CfgXfpIndex,'pm1005CfgSystConfXfpPortn':pm1005CfgSystConfXfpPortn,'pm1005CfgDataRateConfXfpPortn':pm1005CfgDataRateConfXfpPortn,'pm1005CfgLabels':pm1005CfgLabels,'pm1005CfgLabelclientTable':pm1005CfgLabelclientTable,'pm1005CfgLabelclientEntry':pm1005CfgLabelclientEntry,_AW:pm1005CfgLabelclientIndex,'pm1005CfgLabelclientPortn':pm1005CfgLabelclientPortn,'pm1005CfgLabellineTable':pm1005CfgLabellineTable,'pm1005CfgLabellineEntry':pm1005CfgLabellineEntry,_AX:pm1005CfgLabellineIndex,'pm1005CfgLabellinePortn':pm1005CfgLabellinePortn,'pm1005CfgStartuptlh':pm1005CfgStartuptlh,'pm1005CfgOtxtlhTable':pm1005CfgOtxtlhTable,'pm1005CfgOtxtlhEntry':pm1005CfgOtxtlhEntry,_AY:pm1005CfgOtxtlhIndex,'pm1005CfgNuPortn':pm1005CfgNuPortn,'pm1005CfgLineDitherRatePortn':pm1005CfgLineDitherRatePortn,'pm1005CfgLineDitherFhzPortn':pm1005CfgLineDitherFhzPortn,'pm1005CfgLinePwrLaserPortn':pm1005CfgLinePwrLaserPortn,'pm1005CfgLineFCurrentPortn':pm1005CfgLineFCurrentPortn,'pm1005CfgLineGridCurrentPortn':pm1005CfgLineGridCurrentPortn,'pm1005CfgFPortn':pm1005CfgFPortn,'pm1005CfgReservedPortn':pm1005CfgReservedPortn,'pm1005CfgLinePhotodiodeModePortn':pm1005CfgLinePhotodiodeModePortn,'pm1005CfgLinePhotodiodeValuePortn':pm1005CfgLinePhotodiodeValuePortn,'pm1005CfgStartuptablefive':pm1005CfgStartuptablefive,'pm1005CfgOtxtlhcapabilitiesTable':pm1005CfgOtxtlhcapabilitiesTable,'pm1005CfgOtxtlhcapabilitiesEntry':pm1005CfgOtxtlhcapabilitiesEntry,_AZ:pm1005CfgOtxtlhcapabilitiesIndex,'pm1005CfgComponentTypePortn':pm1005CfgComponentTypePortn,'pm1005CfgMiscellaneousPortn':pm1005CfgMiscellaneousPortn,'pm1005CfgFirstChannelPortn':pm1005CfgFirstChannelPortn,'pm1005CfgLastChannelPortn':pm1005CfgLastChannelPortn,'pm1005CfgGridPortn':pm1005CfgGridPortn,'pm1005CfgWriteConfiguration':pm1005CfgWriteConfiguration,'pm1005traps':pm1005traps,_J:pm1005trapPortNumber,_I:pm1005trapLineNumber,_H:pm1005trapBoardNumber,'pm1005LineTrapNotUrgentGoesOn':pm1005LineTrapNotUrgentGoesOn,'pm1005LineTrapNotUrgentGoesOff':pm1005LineTrapNotUrgentGoesOff,'pm1005LineTrapUrgentGoesOn':pm1005LineTrapUrgentGoesOn,'pm1005LineTrapUrgentGoesOff':pm1005LineTrapUrgentGoesOff,'pm1005LineTrapCritGoesOn':pm1005LineTrapCritGoesOn,'pm1005LineTrapCritGoesOff':pm1005LineTrapCritGoesOff,'pm1005ClientTrapNotUrgentGoesOn':pm1005ClientTrapNotUrgentGoesOn,'pm1005ClientTrapNotUrgentGoesOff':pm1005ClientTrapNotUrgentGoesOff,'pm1005ClientTrapUrgentGoesOn':pm1005ClientTrapUrgentGoesOn,'pm1005ClientTrapUrgentGoesOff':pm1005ClientTrapUrgentGoesOff,'pm1005ClientTrapCritGoesOn':pm1005ClientTrapCritGoesOn,'pm1005ClientTrapCritGoesOff':pm1005ClientTrapCritGoesOff,'pm1005PowerTrapUrgentGoesOn':pm1005PowerTrapUrgentGoesOn,'pm1005PowerTrapUrgentGoesOff':pm1005PowerTrapUrgentGoesOff,'pm1005Monitoring':pm1005Monitoring,'pm1005MonOther':pm1005MonOther,'pm1005MonRmon':pm1005MonRmon,'pm1005MonCountersReset':pm1005MonCountersReset,'pm1005MonCountersStop':pm1005MonCountersStop,'pm1005MonClient':pm1005MonClient,'pm1005MonClientRmonCounter':pm1005MonClientRmonCounter,'pm1005MonupRmonByteCntTable':pm1005MonupRmonByteCntTable,'pm1005MonupRmonByteCntEntry':pm1005MonupRmonByteCntEntry,_Aa:pm1005MonupRmonByteCntIndex,'pm1005MonupRmonByteCntValuePortn':pm1005MonupRmonByteCntValuePortn,'pm1005MonupRmonByteCntErrorPortn':pm1005MonupRmonByteCntErrorPortn,'pm1005MonupRmonByteCntOverloadPortn':pm1005MonupRmonByteCntOverloadPortn,'pm1005MonupRmonCrcErrorCntTable':pm1005MonupRmonCrcErrorCntTable,'pm1005MonupRmonCrcErrorCntEntry':pm1005MonupRmonCrcErrorCntEntry,_Ab:pm1005MonupRmonCrcErrorCntIndex,'pm1005MonupRmonCrcErrorCntValuePortn':pm1005MonupRmonCrcErrorCntValuePortn,'pm1005MonupRmonCrcErrorCntErrorPortn':pm1005MonupRmonCrcErrorCntErrorPortn,'pm1005MonupRmonCrcErrorCntOverloadPortn':pm1005MonupRmonCrcErrorCntOverloadPortn,'pm1005MonupRmonPacketsCntTable':pm1005MonupRmonPacketsCntTable,'pm1005MonupRmonPacketsCntEntry':pm1005MonupRmonPacketsCntEntry,_Ac:pm1005MonupRmonPacketsCntIndex,'pm1005MonupRmonPacketsCntValuePortn':pm1005MonupRmonPacketsCntValuePortn,'pm1005MonupRmonPacketsCntErrorPortn':pm1005MonupRmonPacketsCntErrorPortn,'pm1005MonupRmonPacketsCntOverloadPortn':pm1005MonupRmonPacketsCntOverloadPortn,'pm1005MonupRmonBroadcastCntTable':pm1005MonupRmonBroadcastCntTable,'pm1005MonupRmonBroadcastCntEntry':pm1005MonupRmonBroadcastCntEntry,_Ad:pm1005MonupRmonBroadcastCntIndex,'pm1005MonupRmonBroadcastCntValuePortn':pm1005MonupRmonBroadcastCntValuePortn,'pm1005MonupRmonBroadcastCntErrorPortn':pm1005MonupRmonBroadcastCntErrorPortn,'pm1005MonupRmonBroadcastCntOverloadPortn':pm1005MonupRmonBroadcastCntOverloadPortn,'pm1005MonupRmonMulticastCntTable':pm1005MonupRmonMulticastCntTable,'pm1005MonupRmonMulticastCntEntry':pm1005MonupRmonMulticastCntEntry,_Ae:pm1005MonupRmonMulticastCntIndex,'pm1005MonupRmonMulticastCntValuePortn':pm1005MonupRmonMulticastCntValuePortn,'pm1005MonupRmonMulticastCntErrorPortn':pm1005MonupRmonMulticastCntErrorPortn,'pm1005MonupRmonMulticastCntOverloadPortn':pm1005MonupRmonMulticastCntOverloadPortn})