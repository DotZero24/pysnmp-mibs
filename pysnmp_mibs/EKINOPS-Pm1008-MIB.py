_Ah='pm1008MonupRmonMulticastCntIndex'
_Ag='pm1008MonupRmonBroadcastCntIndex'
_Af='pm1008MonupRmonPacketsCntIndex'
_Ae='pm1008MonupRmonCrcErrorCntIndex'
_Ad='pm1008MonupRmonByteCntIndex'
_Ac='pm1008CfgOtxtlhcapabilitiesIndex'
_Ab='pm1008CfgOtxtlhIndex'
_Aa='pm1008CfgLabellineIndex'
_AZ='pm1008CfgLabelclientIndex'
_AY='pm1008CfgXfpIndex'
_AX='pm1008CfgClientStartupIndex'
_AW='pm1008CfgClientcaiscsfIndex'
_AV='pm1008RinvLineIndex'
_AU='pm1008RinvSfpIndex'
_AT='pm1008CtrllinePowerLaserIndex'
_AS='pm1008CtrllinePhotodiodeValueIndex'
_AR='pm1008CtrllinePhotodiodeModeIndex'
_AQ='pm1008CtrllineTunableChannelIndex'
_AP='pm1008CtrlxfpXfiLoopIndex'
_AO='pm1008CtrlxfpLineLoopIndex'
_AN='pm1008CtrlxfpOnoffIndex'
_AM='pm1008CtrllineOosModeIndex'
_AL='pm1008CtrlfecDisableIndex'
_AK='pm1008CtrlprotocolIndex'
_AJ='pm1008CtrlselectMultirateIndex'
_AI='pm1008CtrlclientAccessTermLoopIndex'
_AH='pm1008CtrlflowControlIndex'
_AG='pm1008CtrlcaisDwInsIndex'
_AF='pm1008CtrlcsfUpInsIndex'
_AE='pm1008CtrlsfpOffCtrlIndex'
_AD='pm1008CtrlsfpOnCtrlIndex'
_AC='pm1008CtrlportOosModeIndex'
_AB='pm1008CtrlaccessLoopIndex'
_AA='pm1008CntdfrmPrimLineErrCntIndex'
_A9='pm1008CntdfrmTimCntIndex'
_A8='pm1008CntdfrmB1ErrCntIndex'
_A7='pm1008CntdwTimCntIndex'
_A6='pm1008CntdwCbipCntIndex'
_A5='pm1008CntupCvErrCntIndex'
_A4='pm1008CntupTimCntIndex'
_A3='pm1008CntupRdErrCntIndex'
_A2='pm1008CntupRaInsCntIndex'
_A1='pm1008CntupRaRemCntIndex'
_A0='pm1008Mesrotx1LaserWvlengthIndex'
_z='pm1008Mesrotx1FreqDeviationIndex'
_y='pm1008Mesrotx1LaserTemperatureIndex'
_x='pm1008Mesrotx1AgingIndex'
_w='pm1008Mesrxfp1LxAux2MeasIndex'
_v='pm1008Mesrxfp1LxAux1MeasIndex'
_u='pm1008Mesrxfp1LiRxPowerMeasIndex'
_t='pm1008Mesrxfp1LoTxPowerMeasIndex'
_s='pm1008Mesrxfp1LoBiasCurrentMeasIndex'
_r='pm1008Mesrxfp1ReservedIndex'
_q='pm1008Mesrxfp1LxModTempMeasIndex'
_p='pm1008MesrrxpwrMeasIndex'
_o='pm1008MesrtxpwrMeasIndex'
_n='pm1008MesrbiasMeasIndex'
_m='pm1008MesrvoltMeasIndex'
_l='pm1008MesrtempMeasIndex'
_k='pm1008AlmlineXfp1AlarmsIndex'
_j='pm1008AlmlineSyncAlarmsIndex'
_i='pm1008AlmdfrmAlmIndex'
_h='pm1008AlmsynthAlmLineIndex'
_g='pm1008AlmlineOtx1TlhAlarmsIndex'
_f='pm1008AlmlineXfp1SupplyAlarmIndex'
_e='pm1008AlmlineXfp1AlarmIndex'
_d='pm1008AlmdfrmBerIndex'
_c='pm1008AlmlineOtx1TlhWarningsIndex'
_b='pm1008AlmlineXfp1WarningsIndex'
_a='pm1008AlmmapperDeAlmIndex'
_Z='pm1008AlmaccessioAlmIndex'
_Y='pm1008AlmsynthAlmPortIndex'
_X='pm1008AlmsfpAlmDdmIndex'
_W='pm1008AlmsfpWarnDdmIndex'
_V='2010-10-27 00:00'
_U='pm1008AlmDefFuseA'
_T='pm1008AlmDefFuseB'
_S='pm1008AlmHwFailAccPortn'
_R='pm1008AlmFailAccPortn'
_Q='pm1008AlmSfpDdmAlmPortn'
_P='pm1008AlmSfpDdmWarningPortn'
_O='pm1008AlmLineHwFailPortn'
_N='pm1008AlmLineFailPortn'
_M='pm1008AlmLineDdmAlmPortn'
_L='pm1008AlmLineDdmWarningPortn'
_K='DisplayString'
_J='pm1008trapPortNumber'
_I='pm1008trapLineNumber'
_H='pm1008trapBoardNumber'
_G='deprecated'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='EKINOPS-Pm1008-MIB'
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
modulePm1008=ModuleIdentity((1,3,6,1,4,1,20044,3))
if mibBuilder.loadTexts:modulePm1008.setRevisions(('2004-12-20 00:00','2005-06-03 00:00','2005-09-09 00:00','2005-10-21 00:00','2005-11-04 00:00','2006-01-31 00:00','2007-02-21 00:00','2007-09-17 00:00','2007-11-09 00:00','2008-05-28 00:00','2008-12-09 00:00','2009-04-09 00:00','2009-05-07 00:00','2010-02-15 00:00',_V,_V,'2012-07-02 00:00','2013-04-02 00:00','2014-03-25 00:00','2014-12-18 00:00','2016-05-19 00:00','2016-06-02 00:00'))
class Pm1008MultiRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('rate100Mhz',0),('rate250Mhz',1),('rate500Mhz',2),('rate1Ghz',3)))
class Pm1008OtxMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('otx80mode',1),('otx60mode',2),('otxadjustmode',4)))
class Pm1008OtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pm1008AdjustValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('otxadjustvalue0',0),('otxadjustvalue1',1),('otxadjustvalue2',2),('otxadjustvalue3',3),('otxadjustvalue4',4),('otxadjustvalue5',5),('otxadjustvalue6',6),('otxadjustvalue7',7),('otxadjustvalue8',8),('otxadjustvalue9',9),('otxadjustvalue10',10)))
class Pm1008OtxChannel(TextualConvention,Integer32):status=_A
_Pm1008alarms_ObjectIdentity=ObjectIdentity
pm1008alarms=_Pm1008alarms_ObjectIdentity((1,3,6,1,4,1,20044,3,2))
_Pm1008AlmOther_ObjectIdentity=ObjectIdentity
pm1008AlmOther=_Pm1008AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1))
_Pm1008AlmOtherNurg_ObjectIdentity=ObjectIdentity
pm1008AlmOtherNurg=_Pm1008AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,1))
_Pm1008AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm1008AlmsynthAlm2=_Pm1008AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,1,2))
_Pm1008AlmConfTableSave_Type=EkiOnOff
_Pm1008AlmConfTableSave_Object=MibScalar
pm1008AlmConfTableSave=_Pm1008AlmConfTableSave_Object((1,3,6,1,4,1,20044,3,2,1,1,2,1),_Pm1008AlmConfTableSave_Type())
pm1008AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmConfTableSave.setStatus(_A)
_Pm1008AlmInvUpload_Type=EkiOnOff
_Pm1008AlmInvUpload_Object=MibScalar
pm1008AlmInvUpload=_Pm1008AlmInvUpload_Object((1,3,6,1,4,1,20044,3,2,1,1,2,2),_Pm1008AlmInvUpload_Type())
pm1008AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmInvUpload.setStatus(_A)
_Pm1008AlmConfTableLoad_Type=EkiOnOff
_Pm1008AlmConfTableLoad_Object=MibScalar
pm1008AlmConfTableLoad=_Pm1008AlmConfTableLoad_Object((1,3,6,1,4,1,20044,3,2,1,1,2,3),_Pm1008AlmConfTableLoad_Type())
pm1008AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmConfTableLoad.setStatus(_A)
_Pm1008AlmCorrelatOff_Type=EkiOnOff
_Pm1008AlmCorrelatOff_Object=MibScalar
pm1008AlmCorrelatOff=_Pm1008AlmCorrelatOff_Object((1,3,6,1,4,1,20044,3,2,1,1,2,4),_Pm1008AlmCorrelatOff_Type())
pm1008AlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmCorrelatOff.setStatus(_A)
_Pm1008AlmMaintenanceOn_Type=EkiOnOff
_Pm1008AlmMaintenanceOn_Object=MibScalar
pm1008AlmMaintenanceOn=_Pm1008AlmMaintenanceOn_Object((1,3,6,1,4,1,20044,3,2,1,1,2,5),_Pm1008AlmMaintenanceOn_Type())
pm1008AlmMaintenanceOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmMaintenanceOn.setStatus(_A)
_Pm1008AlmOtherUrg_ObjectIdentity=ObjectIdentity
pm1008AlmOtherUrg=_Pm1008AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,2))
_Pm1008AlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pm1008AlmmodInitFailLevel2=_Pm1008AlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,2,194))
_Pm1008AlmLedFail_Type=EkiOnOff
_Pm1008AlmLedFail_Object=MibScalar
pm1008AlmLedFail=_Pm1008AlmLedFail_Object((1,3,6,1,4,1,20044,3,2,1,2,194,1),_Pm1008AlmLedFail_Type())
pm1008AlmLedFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLedFail.setStatus(_A)
_Pm1008AlmNextColdBootForced_Type=EkiOnOff
_Pm1008AlmNextColdBootForced_Object=MibScalar
pm1008AlmNextColdBootForced=_Pm1008AlmNextColdBootForced_Object((1,3,6,1,4,1,20044,3,2,1,2,194,2),_Pm1008AlmNextColdBootForced_Type())
pm1008AlmNextColdBootForced.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmNextColdBootForced.setStatus(_A)
_Pm1008AlmBootUndone_Type=EkiOnOff
_Pm1008AlmBootUndone_Object=MibScalar
pm1008AlmBootUndone=_Pm1008AlmBootUndone_Object((1,3,6,1,4,1,20044,3,2,1,2,194,3),_Pm1008AlmBootUndone_Type())
pm1008AlmBootUndone.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmBootUndone.setStatus(_A)
_Pm1008AlmResetHwInitFail_Type=EkiOnOff
_Pm1008AlmResetHwInitFail_Object=MibScalar
pm1008AlmResetHwInitFail=_Pm1008AlmResetHwInitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,194,4),_Pm1008AlmResetHwInitFail_Type())
pm1008AlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmResetHwInitFail.setStatus(_A)
_Pm1008AlmSwInitFail_Type=EkiOnOff
_Pm1008AlmSwInitFail_Object=MibScalar
pm1008AlmSwInitFail=_Pm1008AlmSwInitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,194,5),_Pm1008AlmSwInitFail_Type())
pm1008AlmSwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmSwInitFail.setStatus(_A)
_Pm1008AlmmodInitFailLevel3_ObjectIdentity=ObjectIdentity
pm1008AlmmodInitFailLevel3=_Pm1008AlmmodInitFailLevel3_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,2,195))
_Pm1008AlmGwIdentFail_Type=EkiOnOff
_Pm1008AlmGwIdentFail_Object=MibScalar
pm1008AlmGwIdentFail=_Pm1008AlmGwIdentFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,1),_Pm1008AlmGwIdentFail_Type())
pm1008AlmGwIdentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmGwIdentFail.setStatus(_A)
_Pm1008AlmObmTypeReadFail_Type=EkiOnOff
_Pm1008AlmObmTypeReadFail_Object=MibScalar
pm1008AlmObmTypeReadFail=_Pm1008AlmObmTypeReadFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,2),_Pm1008AlmObmTypeReadFail_Type())
pm1008AlmObmTypeReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmObmTypeReadFail.setStatus(_A)
_Pm1008AlmInitModuleFail_Type=EkiOnOff
_Pm1008AlmInitModuleFail_Object=MibScalar
pm1008AlmInitModuleFail=_Pm1008AlmInitModuleFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,3),_Pm1008AlmInitModuleFail_Type())
pm1008AlmInitModuleFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmInitModuleFail.setStatus(_A)
_Pm1008AlmXfp1InitFail_Type=EkiOnOff
_Pm1008AlmXfp1InitFail_Object=MibScalar
pm1008AlmXfp1InitFail=_Pm1008AlmXfp1InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,5),_Pm1008AlmXfp1InitFail_Type())
pm1008AlmXfp1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmXfp1InitFail.setStatus(_A)
_Pm1008AlmXfp2InitFail_Type=EkiOnOff
_Pm1008AlmXfp2InitFail_Object=MibScalar
pm1008AlmXfp2InitFail=_Pm1008AlmXfp2InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,6),_Pm1008AlmXfp2InitFail_Type())
pm1008AlmXfp2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmXfp2InitFail.setStatus(_A)
_Pm1008AlmLine1InitFail_Type=EkiOnOff
_Pm1008AlmLine1InitFail_Object=MibScalar
pm1008AlmLine1InitFail=_Pm1008AlmLine1InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,7),_Pm1008AlmLine1InitFail_Type())
pm1008AlmLine1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLine1InitFail.setStatus(_A)
_Pm1008AlmLine2InitFail_Type=EkiOnOff
_Pm1008AlmLine2InitFail_Object=MibScalar
pm1008AlmLine2InitFail=_Pm1008AlmLine2InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,8),_Pm1008AlmLine2InitFail_Type())
pm1008AlmLine2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLine2InitFail.setStatus(_A)
_Pm1008AlmClient1InitFail_Type=EkiOnOff
_Pm1008AlmClient1InitFail_Object=MibScalar
pm1008AlmClient1InitFail=_Pm1008AlmClient1InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,9),_Pm1008AlmClient1InitFail_Type())
pm1008AlmClient1InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient1InitFail.setStatus(_A)
_Pm1008AlmClient2InitFail_Type=EkiOnOff
_Pm1008AlmClient2InitFail_Object=MibScalar
pm1008AlmClient2InitFail=_Pm1008AlmClient2InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,10),_Pm1008AlmClient2InitFail_Type())
pm1008AlmClient2InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient2InitFail.setStatus(_A)
_Pm1008AlmClient3InitFail_Type=EkiOnOff
_Pm1008AlmClient3InitFail_Object=MibScalar
pm1008AlmClient3InitFail=_Pm1008AlmClient3InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,11),_Pm1008AlmClient3InitFail_Type())
pm1008AlmClient3InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient3InitFail.setStatus(_A)
_Pm1008AlmClient4InitFail_Type=EkiOnOff
_Pm1008AlmClient4InitFail_Object=MibScalar
pm1008AlmClient4InitFail=_Pm1008AlmClient4InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,12),_Pm1008AlmClient4InitFail_Type())
pm1008AlmClient4InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient4InitFail.setStatus(_A)
_Pm1008AlmClient5InitFail_Type=EkiOnOff
_Pm1008AlmClient5InitFail_Object=MibScalar
pm1008AlmClient5InitFail=_Pm1008AlmClient5InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,13),_Pm1008AlmClient5InitFail_Type())
pm1008AlmClient5InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient5InitFail.setStatus(_A)
_Pm1008AlmClient6InitFail_Type=EkiOnOff
_Pm1008AlmClient6InitFail_Object=MibScalar
pm1008AlmClient6InitFail=_Pm1008AlmClient6InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,14),_Pm1008AlmClient6InitFail_Type())
pm1008AlmClient6InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient6InitFail.setStatus(_A)
_Pm1008AlmClient7InitFail_Type=EkiOnOff
_Pm1008AlmClient7InitFail_Object=MibScalar
pm1008AlmClient7InitFail=_Pm1008AlmClient7InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,15),_Pm1008AlmClient7InitFail_Type())
pm1008AlmClient7InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient7InitFail.setStatus(_A)
_Pm1008AlmClient8InitFail_Type=EkiOnOff
_Pm1008AlmClient8InitFail_Object=MibScalar
pm1008AlmClient8InitFail=_Pm1008AlmClient8InitFail_Object((1,3,6,1,4,1,20044,3,2,1,2,195,16),_Pm1008AlmClient8InitFail_Type())
pm1008AlmClient8InitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClient8InitFail.setStatus(_A)
_Pm1008AlmOtherCrit_ObjectIdentity=ObjectIdentity
pm1008AlmOtherCrit=_Pm1008AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,3))
_Pm1008AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm1008AlmsynthAlm0=_Pm1008AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,3,2,1,3,0))
_Pm1008AlmModGlobFail_Type=EkiOnOff
_Pm1008AlmModGlobFail_Object=MibScalar
pm1008AlmModGlobFail=_Pm1008AlmModGlobFail_Object((1,3,6,1,4,1,20044,3,2,1,3,0,9),_Pm1008AlmModGlobFail_Type())
pm1008AlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmModGlobFail.setStatus(_A)
_Pm1008AlmDefFuseA_Type=EkiOnOff
_Pm1008AlmDefFuseA_Object=MibScalar
pm1008AlmDefFuseA=_Pm1008AlmDefFuseA_Object((1,3,6,1,4,1,20044,3,2,1,3,0,15),_Pm1008AlmDefFuseA_Type())
pm1008AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDefFuseA.setStatus(_A)
_Pm1008AlmDefFuseB_Type=EkiOnOff
_Pm1008AlmDefFuseB_Object=MibScalar
pm1008AlmDefFuseB=_Pm1008AlmDefFuseB_Object((1,3,6,1,4,1,20044,3,2,1,3,0,16),_Pm1008AlmDefFuseB_Type())
pm1008AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDefFuseB.setStatus(_A)
_Pm1008AlmClient_ObjectIdentity=ObjectIdentity
pm1008AlmClient=_Pm1008AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,3,2,2))
_Pm1008AlmClientNurg_ObjectIdentity=ObjectIdentity
pm1008AlmClientNurg=_Pm1008AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,3,2,2,1))
_Pm1008AlmsfpWarnDdmTable_Object=MibTable
pm1008AlmsfpWarnDdmTable=_Pm1008AlmsfpWarnDdmTable_Object((1,3,6,1,4,1,20044,3,2,2,1,48))
if mibBuilder.loadTexts:pm1008AlmsfpWarnDdmTable.setStatus(_A)
_Pm1008AlmsfpWarnDdmEntry_Object=MibTableRow
pm1008AlmsfpWarnDdmEntry=_Pm1008AlmsfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1))
pm1008AlmsfpWarnDdmEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm1008AlmsfpWarnDdmEntry.setStatus(_A)
class _Pm1008AlmsfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmsfpWarnDdmIndex_Type.__name__=_D
_Pm1008AlmsfpWarnDdmIndex_Object=MibTableColumn
pm1008AlmsfpWarnDdmIndex=_Pm1008AlmsfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,1),_Pm1008AlmsfpWarnDdmIndex_Type())
pm1008AlmsfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmsfpWarnDdmIndex.setStatus(_A)
_Pm1008AlmTxPwLowWngPortn_Type=EkiOnOff
_Pm1008AlmTxPwLowWngPortn_Object=MibTableColumn
pm1008AlmTxPwLowWngPortn=_Pm1008AlmTxPwLowWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,2),_Pm1008AlmTxPwLowWngPortn_Type())
pm1008AlmTxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPwLowWngPortn.setStatus(_A)
_Pm1008AlmTxPwrHighWngPortn_Type=EkiOnOff
_Pm1008AlmTxPwrHighWngPortn_Object=MibTableColumn
pm1008AlmTxPwrHighWngPortn=_Pm1008AlmTxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,3),_Pm1008AlmTxPwrHighWngPortn_Type())
pm1008AlmTxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPwrHighWngPortn.setStatus(_A)
_Pm1008AlmTxBiasLowWngPortn_Type=EkiOnOff
_Pm1008AlmTxBiasLowWngPortn_Object=MibTableColumn
pm1008AlmTxBiasLowWngPortn=_Pm1008AlmTxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,4),_Pm1008AlmTxBiasLowWngPortn_Type())
pm1008AlmTxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasLowWngPortn.setStatus(_A)
_Pm1008AlmTxBiasHighWngPortn_Type=EkiOnOff
_Pm1008AlmTxBiasHighWngPortn_Object=MibTableColumn
pm1008AlmTxBiasHighWngPortn=_Pm1008AlmTxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,5),_Pm1008AlmTxBiasHighWngPortn_Type())
pm1008AlmTxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasHighWngPortn.setStatus(_A)
_Pm1008AlmVccLowWngPortn_Type=EkiOnOff
_Pm1008AlmVccLowWngPortn_Object=MibTableColumn
pm1008AlmVccLowWngPortn=_Pm1008AlmVccLowWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,6),_Pm1008AlmVccLowWngPortn_Type())
pm1008AlmVccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVccLowWngPortn.setStatus(_A)
_Pm1008AlmVccHighWngPortn_Type=EkiOnOff
_Pm1008AlmVccHighWngPortn_Object=MibTableColumn
pm1008AlmVccHighWngPortn=_Pm1008AlmVccHighWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,7),_Pm1008AlmVccHighWngPortn_Type())
pm1008AlmVccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVccHighWngPortn.setStatus(_A)
_Pm1008AlmTempLowWngPortn_Type=EkiOnOff
_Pm1008AlmTempLowWngPortn_Object=MibTableColumn
pm1008AlmTempLowWngPortn=_Pm1008AlmTempLowWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,8),_Pm1008AlmTempLowWngPortn_Type())
pm1008AlmTempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempLowWngPortn.setStatus(_A)
_Pm1008AlmTempHighWngPortn_Type=EkiOnOff
_Pm1008AlmTempHighWngPortn_Object=MibTableColumn
pm1008AlmTempHighWngPortn=_Pm1008AlmTempHighWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,9),_Pm1008AlmTempHighWngPortn_Type())
pm1008AlmTempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempHighWngPortn.setStatus(_A)
_Pm1008AlmRxPwrLowWngPortn_Type=EkiOnOff
_Pm1008AlmRxPwrLowWngPortn_Object=MibTableColumn
pm1008AlmRxPwrLowWngPortn=_Pm1008AlmRxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,16),_Pm1008AlmRxPwrLowWngPortn_Type())
pm1008AlmRxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPwrLowWngPortn.setStatus(_A)
_Pm1008AlmRxPwrHighWngPortn_Type=EkiOnOff
_Pm1008AlmRxPwrHighWngPortn_Object=MibTableColumn
pm1008AlmRxPwrHighWngPortn=_Pm1008AlmRxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,3,2,2,1,48,1,17),_Pm1008AlmRxPwrHighWngPortn_Type())
pm1008AlmRxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPwrHighWngPortn.setStatus(_A)
_Pm1008AlmClientUrg_ObjectIdentity=ObjectIdentity
pm1008AlmClientUrg=_Pm1008AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,3,2,2,2))
_Pm1008AlmsfpAlmDdmTable_Object=MibTable
pm1008AlmsfpAlmDdmTable=_Pm1008AlmsfpAlmDdmTable_Object((1,3,6,1,4,1,20044,3,2,2,2,32))
if mibBuilder.loadTexts:pm1008AlmsfpAlmDdmTable.setStatus(_A)
_Pm1008AlmsfpAlmDdmEntry_Object=MibTableRow
pm1008AlmsfpAlmDdmEntry=_Pm1008AlmsfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1))
pm1008AlmsfpAlmDdmEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm1008AlmsfpAlmDdmEntry.setStatus(_A)
class _Pm1008AlmsfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmsfpAlmDdmIndex_Type.__name__=_D
_Pm1008AlmsfpAlmDdmIndex_Object=MibTableColumn
pm1008AlmsfpAlmDdmIndex=_Pm1008AlmsfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,1),_Pm1008AlmsfpAlmDdmIndex_Type())
pm1008AlmsfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmsfpAlmDdmIndex.setStatus(_A)
_Pm1008AlmTxPwrLowAlaPortn_Type=EkiOnOff
_Pm1008AlmTxPwrLowAlaPortn_Object=MibTableColumn
pm1008AlmTxPwrLowAlaPortn=_Pm1008AlmTxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,2),_Pm1008AlmTxPwrLowAlaPortn_Type())
pm1008AlmTxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPwrLowAlaPortn.setStatus(_A)
_Pm1008AlmTxPwrHighAlaPortn_Type=EkiOnOff
_Pm1008AlmTxPwrHighAlaPortn_Object=MibTableColumn
pm1008AlmTxPwrHighAlaPortn=_Pm1008AlmTxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,3),_Pm1008AlmTxPwrHighAlaPortn_Type())
pm1008AlmTxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPwrHighAlaPortn.setStatus(_A)
_Pm1008AlmTxBiasLowAlaPortn_Type=EkiOnOff
_Pm1008AlmTxBiasLowAlaPortn_Object=MibTableColumn
pm1008AlmTxBiasLowAlaPortn=_Pm1008AlmTxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,4),_Pm1008AlmTxBiasLowAlaPortn_Type())
pm1008AlmTxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasLowAlaPortn.setStatus(_A)
_Pm1008AlmTxBiasHighAlaPortn_Type=EkiOnOff
_Pm1008AlmTxBiasHighAlaPortn_Object=MibTableColumn
pm1008AlmTxBiasHighAlaPortn=_Pm1008AlmTxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,5),_Pm1008AlmTxBiasHighAlaPortn_Type())
pm1008AlmTxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasHighAlaPortn.setStatus(_A)
_Pm1008AlmVccLowAlaPortn_Type=EkiOnOff
_Pm1008AlmVccLowAlaPortn_Object=MibTableColumn
pm1008AlmVccLowAlaPortn=_Pm1008AlmVccLowAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,6),_Pm1008AlmVccLowAlaPortn_Type())
pm1008AlmVccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVccLowAlaPortn.setStatus(_A)
_Pm1008AlmVccHighAlaPortn_Type=EkiOnOff
_Pm1008AlmVccHighAlaPortn_Object=MibTableColumn
pm1008AlmVccHighAlaPortn=_Pm1008AlmVccHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,7),_Pm1008AlmVccHighAlaPortn_Type())
pm1008AlmVccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVccHighAlaPortn.setStatus(_A)
_Pm1008AlmTempLowAlaPortn_Type=EkiOnOff
_Pm1008AlmTempLowAlaPortn_Object=MibTableColumn
pm1008AlmTempLowAlaPortn=_Pm1008AlmTempLowAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,8),_Pm1008AlmTempLowAlaPortn_Type())
pm1008AlmTempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempLowAlaPortn.setStatus(_A)
_Pm1008AlmTempHighAlaPortn_Type=EkiOnOff
_Pm1008AlmTempHighAlaPortn_Object=MibTableColumn
pm1008AlmTempHighAlaPortn=_Pm1008AlmTempHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,9),_Pm1008AlmTempHighAlaPortn_Type())
pm1008AlmTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempHighAlaPortn.setStatus(_A)
_Pm1008AlmRxPwrLowAlaPortn_Type=EkiOnOff
_Pm1008AlmRxPwrLowAlaPortn_Object=MibTableColumn
pm1008AlmRxPwrLowAlaPortn=_Pm1008AlmRxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,16),_Pm1008AlmRxPwrLowAlaPortn_Type())
pm1008AlmRxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPwrLowAlaPortn.setStatus(_A)
_Pm1008AlmRxPwrHighAlaPortn_Type=EkiOnOff
_Pm1008AlmRxPwrHighAlaPortn_Object=MibTableColumn
pm1008AlmRxPwrHighAlaPortn=_Pm1008AlmRxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,2,2,32,1,17),_Pm1008AlmRxPwrHighAlaPortn_Type())
pm1008AlmRxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPwrHighAlaPortn.setStatus(_A)
_Pm1008AlmClientCrit_ObjectIdentity=ObjectIdentity
pm1008AlmClientCrit=_Pm1008AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,3,2,2,3))
_Pm1008AlmsynthAlmPortTable_Object=MibTable
pm1008AlmsynthAlmPortTable=_Pm1008AlmsynthAlmPortTable_Object((1,3,6,1,4,1,20044,3,2,2,3,8))
if mibBuilder.loadTexts:pm1008AlmsynthAlmPortTable.setStatus(_A)
_Pm1008AlmsynthAlmPortEntry_Object=MibTableRow
pm1008AlmsynthAlmPortEntry=_Pm1008AlmsynthAlmPortEntry_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1))
pm1008AlmsynthAlmPortEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm1008AlmsynthAlmPortEntry.setStatus(_A)
class _Pm1008AlmsynthAlmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmsynthAlmPortIndex_Type.__name__=_D
_Pm1008AlmsynthAlmPortIndex_Object=MibTableColumn
pm1008AlmsynthAlmPortIndex=_Pm1008AlmsynthAlmPortIndex_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,1),_Pm1008AlmsynthAlmPortIndex_Type())
pm1008AlmsynthAlmPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmsynthAlmPortIndex.setStatus(_A)
_Pm1008AlmSfpAbsentPortn_Type=EkiOnOff
_Pm1008AlmSfpAbsentPortn_Object=MibTableColumn
pm1008AlmSfpAbsentPortn=_Pm1008AlmSfpAbsentPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,2),_Pm1008AlmSfpAbsentPortn_Type())
pm1008AlmSfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmSfpAbsentPortn.setStatus(_A)
_Pm1008AlmDdmAbsentPortn_Type=EkiOnOff
_Pm1008AlmDdmAbsentPortn_Object=MibTableColumn
pm1008AlmDdmAbsentPortn=_Pm1008AlmDdmAbsentPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,3),_Pm1008AlmDdmAbsentPortn_Type())
pm1008AlmDdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDdmAbsentPortn.setStatus(_A)
_Pm1008AlmHwFailAccPortn_Type=EkiOnOff
_Pm1008AlmHwFailAccPortn_Object=MibTableColumn
pm1008AlmHwFailAccPortn=_Pm1008AlmHwFailAccPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,5),_Pm1008AlmHwFailAccPortn_Type())
pm1008AlmHwFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmHwFailAccPortn.setStatus(_A)
_Pm1008AlmDwLsdPortn_Type=EkiOnOff
_Pm1008AlmDwLsdPortn_Object=MibTableColumn
pm1008AlmDwLsdPortn=_Pm1008AlmDwLsdPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,6),_Pm1008AlmDwLsdPortn_Type())
pm1008AlmDwLsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwLsdPortn.setStatus(_A)
_Pm1008AlmClientLocalOosPortn_Type=EkiOnOff
_Pm1008AlmClientLocalOosPortn_Object=MibTableColumn
pm1008AlmClientLocalOosPortn=_Pm1008AlmClientLocalOosPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,7),_Pm1008AlmClientLocalOosPortn_Type())
pm1008AlmClientLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClientLocalOosPortn.setStatus(_A)
_Pm1008AlmClientRemoteOosPortn_Type=EkiOnOff
_Pm1008AlmClientRemoteOosPortn_Object=MibTableColumn
pm1008AlmClientRemoteOosPortn=_Pm1008AlmClientRemoteOosPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,8),_Pm1008AlmClientRemoteOosPortn_Type())
pm1008AlmClientRemoteOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmClientRemoteOosPortn.setStatus(_A)
_Pm1008AlmDwCaisPortn_Type=EkiOnOff
_Pm1008AlmDwCaisPortn_Object=MibTableColumn
pm1008AlmDwCaisPortn=_Pm1008AlmDwCaisPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,9),_Pm1008AlmDwCaisPortn_Type())
pm1008AlmDwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwCaisPortn.setStatus(_A)
_Pm1008AlmSfpDdmWarningPortn_Type=EkiOnOff
_Pm1008AlmSfpDdmWarningPortn_Object=MibTableColumn
pm1008AlmSfpDdmWarningPortn=_Pm1008AlmSfpDdmWarningPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,10),_Pm1008AlmSfpDdmWarningPortn_Type())
pm1008AlmSfpDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmSfpDdmWarningPortn.setStatus(_A)
_Pm1008AlmSfpDdmAlmPortn_Type=EkiOnOff
_Pm1008AlmSfpDdmAlmPortn_Object=MibTableColumn
pm1008AlmSfpDdmAlmPortn=_Pm1008AlmSfpDdmAlmPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,11),_Pm1008AlmSfpDdmAlmPortn_Type())
pm1008AlmSfpDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmSfpDdmAlmPortn.setStatus(_A)
_Pm1008AlmFailAccPortn_Type=EkiOnOff
_Pm1008AlmFailAccPortn_Object=MibTableColumn
pm1008AlmFailAccPortn=_Pm1008AlmFailAccPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,13),_Pm1008AlmFailAccPortn_Type())
pm1008AlmFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmFailAccPortn.setStatus(_A)
_Pm1008AlmUpCsfPortn_Type=EkiOnOff
_Pm1008AlmUpCsfPortn_Object=MibTableColumn
pm1008AlmUpCsfPortn=_Pm1008AlmUpCsfPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,8,1,17),_Pm1008AlmUpCsfPortn_Type())
pm1008AlmUpCsfPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmUpCsfPortn.setStatus(_A)
_Pm1008AlmaccessioAlmTable_Object=MibTable
pm1008AlmaccessioAlmTable=_Pm1008AlmaccessioAlmTable_Object((1,3,6,1,4,1,20044,3,2,2,3,16))
if mibBuilder.loadTexts:pm1008AlmaccessioAlmTable.setStatus(_A)
_Pm1008AlmaccessioAlmEntry_Object=MibTableRow
pm1008AlmaccessioAlmEntry=_Pm1008AlmaccessioAlmEntry_Object((1,3,6,1,4,1,20044,3,2,2,3,16,1))
pm1008AlmaccessioAlmEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm1008AlmaccessioAlmEntry.setStatus(_A)
class _Pm1008AlmaccessioAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmaccessioAlmIndex_Type.__name__=_D
_Pm1008AlmaccessioAlmIndex_Object=MibTableColumn
pm1008AlmaccessioAlmIndex=_Pm1008AlmaccessioAlmIndex_Object((1,3,6,1,4,1,20044,3,2,2,3,16,1,1),_Pm1008AlmaccessioAlmIndex_Type())
pm1008AlmaccessioAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmaccessioAlmIndex.setStatus(_A)
_Pm1008AlmDwLasFailPortn_Type=EkiOnOff
_Pm1008AlmDwLasFailPortn_Object=MibTableColumn
pm1008AlmDwLasFailPortn=_Pm1008AlmDwLasFailPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,16,1,2),_Pm1008AlmDwLasFailPortn_Type())
pm1008AlmDwLasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwLasFailPortn.setStatus(_A)
_Pm1008AlmUpLosPortn_Type=EkiOnOff
_Pm1008AlmUpLosPortn_Object=MibTableColumn
pm1008AlmUpLosPortn=_Pm1008AlmUpLosPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,16,1,5),_Pm1008AlmUpLosPortn_Type())
pm1008AlmUpLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmUpLosPortn.setStatus(_A)
_Pm1008AlmmapperDeAlmTable_Object=MibTable
pm1008AlmmapperDeAlmTable=_Pm1008AlmmapperDeAlmTable_Object((1,3,6,1,4,1,20044,3,2,2,3,72))
if mibBuilder.loadTexts:pm1008AlmmapperDeAlmTable.setStatus(_A)
_Pm1008AlmmapperDeAlmEntry_Object=MibTableRow
pm1008AlmmapperDeAlmEntry=_Pm1008AlmmapperDeAlmEntry_Object((1,3,6,1,4,1,20044,3,2,2,3,72,1))
pm1008AlmmapperDeAlmEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm1008AlmmapperDeAlmEntry.setStatus(_A)
class _Pm1008AlmmapperDeAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmmapperDeAlmIndex_Type.__name__=_D
_Pm1008AlmmapperDeAlmIndex_Object=MibTableColumn
pm1008AlmmapperDeAlmIndex=_Pm1008AlmmapperDeAlmIndex_Object((1,3,6,1,4,1,20044,3,2,2,3,72,1,1),_Pm1008AlmmapperDeAlmIndex_Type())
pm1008AlmmapperDeAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmmapperDeAlmIndex.setStatus(_A)
_Pm1008AlmUpAccOosPortn_Type=EkiOnOff
_Pm1008AlmUpAccOosPortn_Object=MibTableColumn
pm1008AlmUpAccOosPortn=_Pm1008AlmUpAccOosPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,72,1,2),_Pm1008AlmUpAccOosPortn_Type())
pm1008AlmUpAccOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmUpAccOosPortn.setStatus(_A)
_Pm1008AlmUpBufferOvlPortn_Type=EkiOnOff
_Pm1008AlmUpBufferOvlPortn_Object=MibTableColumn
pm1008AlmUpBufferOvlPortn=_Pm1008AlmUpBufferOvlPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,72,1,11),_Pm1008AlmUpBufferOvlPortn_Type())
pm1008AlmUpBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmUpBufferOvlPortn.setStatus(_A)
_Pm1008AlmDwCsfDetPortn_Type=EkiOnOff
_Pm1008AlmDwCsfDetPortn_Object=MibTableColumn
pm1008AlmDwCsfDetPortn=_Pm1008AlmDwCsfDetPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,72,1,12),_Pm1008AlmDwCsfDetPortn_Type())
pm1008AlmDwCsfDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwCsfDetPortn.setStatus(_A)
_Pm1008AlmDwBufferOvlPortn_Type=EkiOnOff
_Pm1008AlmDwBufferOvlPortn_Object=MibTableColumn
pm1008AlmDwBufferOvlPortn=_Pm1008AlmDwBufferOvlPortn_Object((1,3,6,1,4,1,20044,3,2,2,3,72,1,15),_Pm1008AlmDwBufferOvlPortn_Type())
pm1008AlmDwBufferOvlPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwBufferOvlPortn.setStatus(_A)
_Pm1008AlmLine_ObjectIdentity=ObjectIdentity
pm1008AlmLine=_Pm1008AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,3,2,3))
_Pm1008AlmLineNurg_ObjectIdentity=ObjectIdentity
pm1008AlmLineNurg=_Pm1008AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,3,2,3,1))
_Pm1008AlmlineXfp1WarningsTable_Object=MibTable
pm1008AlmlineXfp1WarningsTable=_Pm1008AlmlineXfp1WarningsTable_Object((1,3,6,1,4,1,20044,3,2,3,1,209))
if mibBuilder.loadTexts:pm1008AlmlineXfp1WarningsTable.setStatus(_A)
_Pm1008AlmlineXfp1WarningsEntry_Object=MibTableRow
pm1008AlmlineXfp1WarningsEntry=_Pm1008AlmlineXfp1WarningsEntry_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1))
pm1008AlmlineXfp1WarningsEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm1008AlmlineXfp1WarningsEntry.setStatus(_A)
class _Pm1008AlmlineXfp1WarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineXfp1WarningsIndex_Type.__name__=_D
_Pm1008AlmlineXfp1WarningsIndex_Object=MibTableColumn
pm1008AlmlineXfp1WarningsIndex=_Pm1008AlmlineXfp1WarningsIndex_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,1),_Pm1008AlmlineXfp1WarningsIndex_Type())
pm1008AlmlineXfp1WarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineXfp1WarningsIndex.setStatus(_A)
_Pm1008AlmTxPowerLowWarningPortn_Type=EkiOnOff
_Pm1008AlmTxPowerLowWarningPortn_Object=MibTableColumn
pm1008AlmTxPowerLowWarningPortn=_Pm1008AlmTxPowerLowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,2),_Pm1008AlmTxPowerLowWarningPortn_Type())
pm1008AlmTxPowerLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPowerLowWarningPortn.setStatus(_A)
_Pm1008AlmTxPowerHighWarningPortn_Type=EkiOnOff
_Pm1008AlmTxPowerHighWarningPortn_Object=MibTableColumn
pm1008AlmTxPowerHighWarningPortn=_Pm1008AlmTxPowerHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,3),_Pm1008AlmTxPowerHighWarningPortn_Type())
pm1008AlmTxPowerHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPowerHighWarningPortn.setStatus(_A)
_Pm1008AlmTxBiasLowWarningPortn_Type=EkiOnOff
_Pm1008AlmTxBiasLowWarningPortn_Object=MibTableColumn
pm1008AlmTxBiasLowWarningPortn=_Pm1008AlmTxBiasLowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,4),_Pm1008AlmTxBiasLowWarningPortn_Type())
pm1008AlmTxBiasLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasLowWarningPortn.setStatus(_A)
_Pm1008AlmTxBiasHighWarningPortn_Type=EkiOnOff
_Pm1008AlmTxBiasHighWarningPortn_Object=MibTableColumn
pm1008AlmTxBiasHighWarningPortn=_Pm1008AlmTxBiasHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,5),_Pm1008AlmTxBiasHighWarningPortn_Type())
pm1008AlmTxBiasHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasHighWarningPortn.setStatus(_A)
_Pm1008AlmTempLowWarningPortn_Type=EkiOnOff
_Pm1008AlmTempLowWarningPortn_Object=MibTableColumn
pm1008AlmTempLowWarningPortn=_Pm1008AlmTempLowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,8),_Pm1008AlmTempLowWarningPortn_Type())
pm1008AlmTempLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempLowWarningPortn.setStatus(_A)
_Pm1008AlmTempHighWarningPortn_Type=EkiOnOff
_Pm1008AlmTempHighWarningPortn_Object=MibTableColumn
pm1008AlmTempHighWarningPortn=_Pm1008AlmTempHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,9),_Pm1008AlmTempHighWarningPortn_Type())
pm1008AlmTempHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempHighWarningPortn.setStatus(_A)
_Pm1008AlmRxPowerLowWarningPortn_Type=EkiOnOff
_Pm1008AlmRxPowerLowWarningPortn_Object=MibTableColumn
pm1008AlmRxPowerLowWarningPortn=_Pm1008AlmRxPowerLowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,16),_Pm1008AlmRxPowerLowWarningPortn_Type())
pm1008AlmRxPowerLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPowerLowWarningPortn.setStatus(_A)
_Pm1008AlmRxPowerHighWarningPortn_Type=EkiOnOff
_Pm1008AlmRxPowerHighWarningPortn_Object=MibTableColumn
pm1008AlmRxPowerHighWarningPortn=_Pm1008AlmRxPowerHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,209,1,17),_Pm1008AlmRxPowerHighWarningPortn_Type())
pm1008AlmRxPowerHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPowerHighWarningPortn.setStatus(_A)
_Pm1008AlmlineOtx1TlhWarningsTable_Object=MibTable
pm1008AlmlineOtx1TlhWarningsTable=_Pm1008AlmlineOtx1TlhWarningsTable_Object((1,3,6,1,4,1,20044,3,2,3,1,225))
if mibBuilder.loadTexts:pm1008AlmlineOtx1TlhWarningsTable.setStatus(_A)
_Pm1008AlmlineOtx1TlhWarningsEntry_Object=MibTableRow
pm1008AlmlineOtx1TlhWarningsEntry=_Pm1008AlmlineOtx1TlhWarningsEntry_Object((1,3,6,1,4,1,20044,3,2,3,1,225,1))
pm1008AlmlineOtx1TlhWarningsEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm1008AlmlineOtx1TlhWarningsEntry.setStatus(_A)
class _Pm1008AlmlineOtx1TlhWarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineOtx1TlhWarningsIndex_Type.__name__=_D
_Pm1008AlmlineOtx1TlhWarningsIndex_Object=MibTableColumn
pm1008AlmlineOtx1TlhWarningsIndex=_Pm1008AlmlineOtx1TlhWarningsIndex_Object((1,3,6,1,4,1,20044,3,2,3,1,225,1,1),_Pm1008AlmlineOtx1TlhWarningsIndex_Type())
pm1008AlmlineOtx1TlhWarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineOtx1TlhWarningsIndex.setStatus(_A)
_Pm1008AlmLineModulatorAgingHighWarningPortn_Type=EkiOnOff
_Pm1008AlmLineModulatorAgingHighWarningPortn_Object=MibTableColumn
pm1008AlmLineModulatorAgingHighWarningPortn=_Pm1008AlmLineModulatorAgingHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,225,1,6),_Pm1008AlmLineModulatorAgingHighWarningPortn_Type())
pm1008AlmLineModulatorAgingHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineModulatorAgingHighWarningPortn.setStatus(_A)
_Pm1008AlmLineAgingHighWarningPortn_Type=EkiOnOff
_Pm1008AlmLineAgingHighWarningPortn_Object=MibTableColumn
pm1008AlmLineAgingHighWarningPortn=_Pm1008AlmLineAgingHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,225,1,7),_Pm1008AlmLineAgingHighWarningPortn_Type())
pm1008AlmLineAgingHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineAgingHighWarningPortn.setStatus(_A)
_Pm1008AlmLineFreqDevHighWarningPortn_Type=EkiOnOff
_Pm1008AlmLineFreqDevHighWarningPortn_Object=MibTableColumn
pm1008AlmLineFreqDevHighWarningPortn=_Pm1008AlmLineFreqDevHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,225,1,13),_Pm1008AlmLineFreqDevHighWarningPortn_Type())
pm1008AlmLineFreqDevHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineFreqDevHighWarningPortn.setStatus(_A)
_Pm1008AlmLineLaserTempHighWarningPortn_Type=EkiOnOff
_Pm1008AlmLineLaserTempHighWarningPortn_Object=MibTableColumn
pm1008AlmLineLaserTempHighWarningPortn=_Pm1008AlmLineLaserTempHighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,1,225,1,15),_Pm1008AlmLineLaserTempHighWarningPortn_Type())
pm1008AlmLineLaserTempHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineLaserTempHighWarningPortn.setStatus(_A)
_Pm1008AlmLineUrg_ObjectIdentity=ObjectIdentity
pm1008AlmLineUrg=_Pm1008AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,3,2,3,2))
_Pm1008AlmdfrmBerTable_Object=MibTable
pm1008AlmdfrmBerTable=_Pm1008AlmdfrmBerTable_Object((1,3,6,1,4,1,20044,3,2,3,2,129))
if mibBuilder.loadTexts:pm1008AlmdfrmBerTable.setStatus(_A)
_Pm1008AlmdfrmBerEntry_Object=MibTableRow
pm1008AlmdfrmBerEntry=_Pm1008AlmdfrmBerEntry_Object((1,3,6,1,4,1,20044,3,2,3,2,129,1))
pm1008AlmdfrmBerEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm1008AlmdfrmBerEntry.setStatus(_A)
class _Pm1008AlmdfrmBerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmdfrmBerIndex_Type.__name__=_D
_Pm1008AlmdfrmBerIndex_Object=MibTableColumn
pm1008AlmdfrmBerIndex=_Pm1008AlmdfrmBerIndex_Object((1,3,6,1,4,1,20044,3,2,3,2,129,1,1),_Pm1008AlmdfrmBerIndex_Type())
pm1008AlmdfrmBerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmdfrmBerIndex.setStatus(_A)
_Pm1008AlmLineSignalDegradePortn_Type=EkiOnOff
_Pm1008AlmLineSignalDegradePortn_Object=MibTableColumn
pm1008AlmLineSignalDegradePortn=_Pm1008AlmLineSignalDegradePortn_Object((1,3,6,1,4,1,20044,3,2,3,2,129,1,2),_Pm1008AlmLineSignalDegradePortn_Type())
pm1008AlmLineSignalDegradePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineSignalDegradePortn.setStatus(_A)
_Pm1008AlmLineSignalFailPortn_Type=EkiOnOff
_Pm1008AlmLineSignalFailPortn_Object=MibTableColumn
pm1008AlmLineSignalFailPortn=_Pm1008AlmLineSignalFailPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,129,1,3),_Pm1008AlmLineSignalFailPortn_Type())
pm1008AlmLineSignalFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineSignalFailPortn.setStatus(_A)
_Pm1008AlmLineDegradePortn_Type=EkiOnOff
_Pm1008AlmLineDegradePortn_Object=MibTableColumn
pm1008AlmLineDegradePortn=_Pm1008AlmLineDegradePortn_Object((1,3,6,1,4,1,20044,3,2,3,2,129,1,6),_Pm1008AlmLineDegradePortn_Type())
pm1008AlmLineDegradePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineDegradePortn.setStatus(_A)
_Pm1008AlmlineXfp1AlarmTable_Object=MibTable
pm1008AlmlineXfp1AlarmTable=_Pm1008AlmlineXfp1AlarmTable_Object((1,3,6,1,4,1,20044,3,2,3,2,208))
if mibBuilder.loadTexts:pm1008AlmlineXfp1AlarmTable.setStatus(_A)
_Pm1008AlmlineXfp1AlarmEntry_Object=MibTableRow
pm1008AlmlineXfp1AlarmEntry=_Pm1008AlmlineXfp1AlarmEntry_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1))
pm1008AlmlineXfp1AlarmEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm1008AlmlineXfp1AlarmEntry.setStatus(_A)
class _Pm1008AlmlineXfp1AlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineXfp1AlarmIndex_Type.__name__=_D
_Pm1008AlmlineXfp1AlarmIndex_Object=MibTableColumn
pm1008AlmlineXfp1AlarmIndex=_Pm1008AlmlineXfp1AlarmIndex_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,1),_Pm1008AlmlineXfp1AlarmIndex_Type())
pm1008AlmlineXfp1AlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineXfp1AlarmIndex.setStatus(_A)
_Pm1008AlmTxPowerLowAlarmPortn_Type=EkiOnOff
_Pm1008AlmTxPowerLowAlarmPortn_Object=MibTableColumn
pm1008AlmTxPowerLowAlarmPortn=_Pm1008AlmTxPowerLowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,2),_Pm1008AlmTxPowerLowAlarmPortn_Type())
pm1008AlmTxPowerLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPowerLowAlarmPortn.setStatus(_A)
_Pm1008AlmTxPowerHighAlarmPortn_Type=EkiOnOff
_Pm1008AlmTxPowerHighAlarmPortn_Object=MibTableColumn
pm1008AlmTxPowerHighAlarmPortn=_Pm1008AlmTxPowerHighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,3),_Pm1008AlmTxPowerHighAlarmPortn_Type())
pm1008AlmTxPowerHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxPowerHighAlarmPortn.setStatus(_A)
_Pm1008AlmTxBiasLowAlarmPortn_Type=EkiOnOff
_Pm1008AlmTxBiasLowAlarmPortn_Object=MibTableColumn
pm1008AlmTxBiasLowAlarmPortn=_Pm1008AlmTxBiasLowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,4),_Pm1008AlmTxBiasLowAlarmPortn_Type())
pm1008AlmTxBiasLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasLowAlarmPortn.setStatus(_A)
_Pm1008AlmTxBiasHighAlarmPortn_Type=EkiOnOff
_Pm1008AlmTxBiasHighAlarmPortn_Object=MibTableColumn
pm1008AlmTxBiasHighAlarmPortn=_Pm1008AlmTxBiasHighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,5),_Pm1008AlmTxBiasHighAlarmPortn_Type())
pm1008AlmTxBiasHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxBiasHighAlarmPortn.setStatus(_A)
_Pm1008AlmTempLowAlarmPortn_Type=EkiOnOff
_Pm1008AlmTempLowAlarmPortn_Object=MibTableColumn
pm1008AlmTempLowAlarmPortn=_Pm1008AlmTempLowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,8),_Pm1008AlmTempLowAlarmPortn_Type())
pm1008AlmTempLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempLowAlarmPortn.setStatus(_A)
_Pm1008AlmTempHighAlarmPortn_Type=EkiOnOff
_Pm1008AlmTempHighAlarmPortn_Object=MibTableColumn
pm1008AlmTempHighAlarmPortn=_Pm1008AlmTempHighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,9),_Pm1008AlmTempHighAlarmPortn_Type())
pm1008AlmTempHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTempHighAlarmPortn.setStatus(_A)
_Pm1008AlmRxPowerLowAlarmPortn_Type=EkiOnOff
_Pm1008AlmRxPowerLowAlarmPortn_Object=MibTableColumn
pm1008AlmRxPowerLowAlarmPortn=_Pm1008AlmRxPowerLowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,16),_Pm1008AlmRxPowerLowAlarmPortn_Type())
pm1008AlmRxPowerLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPowerLowAlarmPortn.setStatus(_A)
_Pm1008AlmRxPowerHighAlarmPortn_Type=EkiOnOff
_Pm1008AlmRxPowerHighAlarmPortn_Object=MibTableColumn
pm1008AlmRxPowerHighAlarmPortn=_Pm1008AlmRxPowerHighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,208,1,17),_Pm1008AlmRxPowerHighAlarmPortn_Type())
pm1008AlmRxPowerHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxPowerHighAlarmPortn.setStatus(_A)
_Pm1008AlmlineXfp1SupplyAlarmTable_Object=MibTable
pm1008AlmlineXfp1SupplyAlarmTable=_Pm1008AlmlineXfp1SupplyAlarmTable_Object((1,3,6,1,4,1,20044,3,2,3,2,212))
if mibBuilder.loadTexts:pm1008AlmlineXfp1SupplyAlarmTable.setStatus(_A)
_Pm1008AlmlineXfp1SupplyAlarmEntry_Object=MibTableRow
pm1008AlmlineXfp1SupplyAlarmEntry=_Pm1008AlmlineXfp1SupplyAlarmEntry_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1))
pm1008AlmlineXfp1SupplyAlarmEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm1008AlmlineXfp1SupplyAlarmEntry.setStatus(_A)
class _Pm1008AlmlineXfp1SupplyAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineXfp1SupplyAlarmIndex_Type.__name__=_D
_Pm1008AlmlineXfp1SupplyAlarmIndex_Object=MibTableColumn
pm1008AlmlineXfp1SupplyAlarmIndex=_Pm1008AlmlineXfp1SupplyAlarmIndex_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,1),_Pm1008AlmlineXfp1SupplyAlarmIndex_Type())
pm1008AlmlineXfp1SupplyAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineXfp1SupplyAlarmIndex.setStatus(_A)
_Pm1008AlmVee5LowAlarmPortn_Type=EkiOnOff
_Pm1008AlmVee5LowAlarmPortn_Object=MibTableColumn
pm1008AlmVee5LowAlarmPortn=_Pm1008AlmVee5LowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,2),_Pm1008AlmVee5LowAlarmPortn_Type())
pm1008AlmVee5LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVee5LowAlarmPortn.setStatus(_A)
_Pm1008AlmVee5HighAlarmPortn_Type=EkiOnOff
_Pm1008AlmVee5HighAlarmPortn_Object=MibTableColumn
pm1008AlmVee5HighAlarmPortn=_Pm1008AlmVee5HighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,3),_Pm1008AlmVee5HighAlarmPortn_Type())
pm1008AlmVee5HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVee5HighAlarmPortn.setStatus(_A)
_Pm1008AlmVcc2LowAlarmPortn_Type=EkiOnOff
_Pm1008AlmVcc2LowAlarmPortn_Object=MibTableColumn
pm1008AlmVcc2LowAlarmPortn=_Pm1008AlmVcc2LowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,4),_Pm1008AlmVcc2LowAlarmPortn_Type())
pm1008AlmVcc2LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc2LowAlarmPortn.setStatus(_A)
_Pm1008AlmVcc2HighAlarmPortn_Type=EkiOnOff
_Pm1008AlmVcc2HighAlarmPortn_Object=MibTableColumn
pm1008AlmVcc2HighAlarmPortn=_Pm1008AlmVcc2HighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,5),_Pm1008AlmVcc2HighAlarmPortn_Type())
pm1008AlmVcc2HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc2HighAlarmPortn.setStatus(_A)
_Pm1008AlmVcc3LowAlarmPortn_Type=EkiOnOff
_Pm1008AlmVcc3LowAlarmPortn_Object=MibTableColumn
pm1008AlmVcc3LowAlarmPortn=_Pm1008AlmVcc3LowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,6),_Pm1008AlmVcc3LowAlarmPortn_Type())
pm1008AlmVcc3LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc3LowAlarmPortn.setStatus(_A)
_Pm1008AlmVcc3HighAlarmPortn_Type=EkiOnOff
_Pm1008AlmVcc3HighAlarmPortn_Object=MibTableColumn
pm1008AlmVcc3HighAlarmPortn=_Pm1008AlmVcc3HighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,7),_Pm1008AlmVcc3HighAlarmPortn_Type())
pm1008AlmVcc3HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc3HighAlarmPortn.setStatus(_A)
_Pm1008AlmVcc5LowAlarmPortn_Type=EkiOnOff
_Pm1008AlmVcc5LowAlarmPortn_Object=MibTableColumn
pm1008AlmVcc5LowAlarmPortn=_Pm1008AlmVcc5LowAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,8),_Pm1008AlmVcc5LowAlarmPortn_Type())
pm1008AlmVcc5LowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc5LowAlarmPortn.setStatus(_A)
_Pm1008AlmVcc5HighAlarmPortn_Type=EkiOnOff
_Pm1008AlmVcc5HighAlarmPortn_Object=MibTableColumn
pm1008AlmVcc5HighAlarmPortn=_Pm1008AlmVcc5HighAlarmPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,9),_Pm1008AlmVcc5HighAlarmPortn_Type())
pm1008AlmVcc5HighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc5HighAlarmPortn.setStatus(_A)
_Pm1008AlmVee5LowWarningPortn_Type=EkiOnOff
_Pm1008AlmVee5LowWarningPortn_Object=MibTableColumn
pm1008AlmVee5LowWarningPortn=_Pm1008AlmVee5LowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,10),_Pm1008AlmVee5LowWarningPortn_Type())
pm1008AlmVee5LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVee5LowWarningPortn.setStatus(_A)
_Pm1008AlmVee5HighWarningPortn_Type=EkiOnOff
_Pm1008AlmVee5HighWarningPortn_Object=MibTableColumn
pm1008AlmVee5HighWarningPortn=_Pm1008AlmVee5HighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,11),_Pm1008AlmVee5HighWarningPortn_Type())
pm1008AlmVee5HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVee5HighWarningPortn.setStatus(_A)
_Pm1008AlmVcc2LowWarningPortn_Type=EkiOnOff
_Pm1008AlmVcc2LowWarningPortn_Object=MibTableColumn
pm1008AlmVcc2LowWarningPortn=_Pm1008AlmVcc2LowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,12),_Pm1008AlmVcc2LowWarningPortn_Type())
pm1008AlmVcc2LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc2LowWarningPortn.setStatus(_A)
_Pm1008AlmVcc2HighWarningPortn_Type=EkiOnOff
_Pm1008AlmVcc2HighWarningPortn_Object=MibTableColumn
pm1008AlmVcc2HighWarningPortn=_Pm1008AlmVcc2HighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,13),_Pm1008AlmVcc2HighWarningPortn_Type())
pm1008AlmVcc2HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc2HighWarningPortn.setStatus(_A)
_Pm1008AlmVcc3LowWarningPortn_Type=EkiOnOff
_Pm1008AlmVcc3LowWarningPortn_Object=MibTableColumn
pm1008AlmVcc3LowWarningPortn=_Pm1008AlmVcc3LowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,14),_Pm1008AlmVcc3LowWarningPortn_Type())
pm1008AlmVcc3LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc3LowWarningPortn.setStatus(_A)
_Pm1008AlmVcc3HighWarningPortn_Type=EkiOnOff
_Pm1008AlmVcc3HighWarningPortn_Object=MibTableColumn
pm1008AlmVcc3HighWarningPortn=_Pm1008AlmVcc3HighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,15),_Pm1008AlmVcc3HighWarningPortn_Type())
pm1008AlmVcc3HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc3HighWarningPortn.setStatus(_A)
_Pm1008AlmVcc5LowWarningPortn_Type=EkiOnOff
_Pm1008AlmVcc5LowWarningPortn_Object=MibTableColumn
pm1008AlmVcc5LowWarningPortn=_Pm1008AlmVcc5LowWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,16),_Pm1008AlmVcc5LowWarningPortn_Type())
pm1008AlmVcc5LowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc5LowWarningPortn.setStatus(_A)
_Pm1008AlmVcc5HighWarningPortn_Type=EkiOnOff
_Pm1008AlmVcc5HighWarningPortn_Object=MibTableColumn
pm1008AlmVcc5HighWarningPortn=_Pm1008AlmVcc5HighWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,212,1,17),_Pm1008AlmVcc5HighWarningPortn_Type())
pm1008AlmVcc5HighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmVcc5HighWarningPortn.setStatus(_A)
_Pm1008AlmlineOtx1TlhAlarmsTable_Object=MibTable
pm1008AlmlineOtx1TlhAlarmsTable=_Pm1008AlmlineOtx1TlhAlarmsTable_Object((1,3,6,1,4,1,20044,3,2,3,2,224))
if mibBuilder.loadTexts:pm1008AlmlineOtx1TlhAlarmsTable.setStatus(_A)
_Pm1008AlmlineOtx1TlhAlarmsEntry_Object=MibTableRow
pm1008AlmlineOtx1TlhAlarmsEntry=_Pm1008AlmlineOtx1TlhAlarmsEntry_Object((1,3,6,1,4,1,20044,3,2,3,2,224,1))
pm1008AlmlineOtx1TlhAlarmsEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm1008AlmlineOtx1TlhAlarmsEntry.setStatus(_A)
class _Pm1008AlmlineOtx1TlhAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineOtx1TlhAlarmsIndex_Type.__name__=_D
_Pm1008AlmlineOtx1TlhAlarmsIndex_Object=MibTableColumn
pm1008AlmlineOtx1TlhAlarmsIndex=_Pm1008AlmlineOtx1TlhAlarmsIndex_Object((1,3,6,1,4,1,20044,3,2,3,2,224,1,1),_Pm1008AlmlineOtx1TlhAlarmsIndex_Type())
pm1008AlmlineOtx1TlhAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineOtx1TlhAlarmsIndex.setStatus(_A)
_Pm1008AlmLineModulatorAgingHighAlaPortn_Type=EkiOnOff
_Pm1008AlmLineModulatorAgingHighAlaPortn_Object=MibTableColumn
pm1008AlmLineModulatorAgingHighAlaPortn=_Pm1008AlmLineModulatorAgingHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,224,1,6),_Pm1008AlmLineModulatorAgingHighAlaPortn_Type())
pm1008AlmLineModulatorAgingHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineModulatorAgingHighAlaPortn.setStatus(_A)
_Pm1008AlmLineAgingHighAlaPortn_Type=EkiOnOff
_Pm1008AlmLineAgingHighAlaPortn_Object=MibTableColumn
pm1008AlmLineAgingHighAlaPortn=_Pm1008AlmLineAgingHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,224,1,7),_Pm1008AlmLineAgingHighAlaPortn_Type())
pm1008AlmLineAgingHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineAgingHighAlaPortn.setStatus(_A)
_Pm1008AlmLineFreqDevHighAlaPortn_Type=EkiOnOff
_Pm1008AlmLineFreqDevHighAlaPortn_Object=MibTableColumn
pm1008AlmLineFreqDevHighAlaPortn=_Pm1008AlmLineFreqDevHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,224,1,13),_Pm1008AlmLineFreqDevHighAlaPortn_Type())
pm1008AlmLineFreqDevHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineFreqDevHighAlaPortn.setStatus(_A)
_Pm1008AlmLineLaserTempHighAlaPortn_Type=EkiOnOff
_Pm1008AlmLineLaserTempHighAlaPortn_Object=MibTableColumn
pm1008AlmLineLaserTempHighAlaPortn=_Pm1008AlmLineLaserTempHighAlaPortn_Object((1,3,6,1,4,1,20044,3,2,3,2,224,1,15),_Pm1008AlmLineLaserTempHighAlaPortn_Type())
pm1008AlmLineLaserTempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineLaserTempHighAlaPortn.setStatus(_A)
_Pm1008AlmLineCrit_ObjectIdentity=ObjectIdentity
pm1008AlmLineCrit=_Pm1008AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,3,2,3,3))
_Pm1008AlmsynthAlmLineTable_Object=MibTable
pm1008AlmsynthAlmLineTable=_Pm1008AlmsynthAlmLineTable_Object((1,3,6,1,4,1,20044,3,2,3,3,7))
if mibBuilder.loadTexts:pm1008AlmsynthAlmLineTable.setStatus(_A)
_Pm1008AlmsynthAlmLineEntry_Object=MibTableRow
pm1008AlmsynthAlmLineEntry=_Pm1008AlmsynthAlmLineEntry_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1))
pm1008AlmsynthAlmLineEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm1008AlmsynthAlmLineEntry.setStatus(_A)
class _Pm1008AlmsynthAlmLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmsynthAlmLineIndex_Type.__name__=_D
_Pm1008AlmsynthAlmLineIndex_Object=MibTableColumn
pm1008AlmsynthAlmLineIndex=_Pm1008AlmsynthAlmLineIndex_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,1),_Pm1008AlmsynthAlmLineIndex_Type())
pm1008AlmsynthAlmLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmsynthAlmLineIndex.setStatus(_A)
_Pm1008AlmXfpAbsentPortn_Type=EkiOnOff
_Pm1008AlmXfpAbsentPortn_Object=MibTableColumn
pm1008AlmXfpAbsentPortn=_Pm1008AlmXfpAbsentPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,2),_Pm1008AlmXfpAbsentPortn_Type())
pm1008AlmXfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmXfpAbsentPortn.setStatus(_A)
_Pm1008AlmXfpInitNotComplPortn_Type=EkiOnOff
_Pm1008AlmXfpInitNotComplPortn_Object=MibTableColumn
pm1008AlmXfpInitNotComplPortn=_Pm1008AlmXfpInitNotComplPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,3),_Pm1008AlmXfpInitNotComplPortn_Type())
pm1008AlmXfpInitNotComplPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmXfpInitNotComplPortn.setStatus(_A)
_Pm1008AlmLineHwFailPortn_Type=EkiOnOff
_Pm1008AlmLineHwFailPortn_Object=MibTableColumn
pm1008AlmLineHwFailPortn=_Pm1008AlmLineHwFailPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,5),_Pm1008AlmLineHwFailPortn_Type())
pm1008AlmLineHwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineHwFailPortn.setStatus(_A)
_Pm1008AlmXfpTxOffPortn_Type=EkiOnOff
_Pm1008AlmXfpTxOffPortn_Object=MibTableColumn
pm1008AlmXfpTxOffPortn=_Pm1008AlmXfpTxOffPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,6),_Pm1008AlmXfpTxOffPortn_Type())
pm1008AlmXfpTxOffPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmXfpTxOffPortn.setStatus(_A)
_Pm1008AlmLineLocalOosPortn_Type=EkiOnOff
_Pm1008AlmLineLocalOosPortn_Object=MibTableColumn
pm1008AlmLineLocalOosPortn=_Pm1008AlmLineLocalOosPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,7),_Pm1008AlmLineLocalOosPortn_Type())
pm1008AlmLineLocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineLocalOosPortn.setStatus(_A)
_Pm1008AlmUpRdiInsPortn_Type=EkiOnOff
_Pm1008AlmUpRdiInsPortn_Object=MibTableColumn
pm1008AlmUpRdiInsPortn=_Pm1008AlmUpRdiInsPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,9),_Pm1008AlmUpRdiInsPortn_Type())
pm1008AlmUpRdiInsPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmUpRdiInsPortn.setStatus(_A)
_Pm1008AlmLineDdmWarningPortn_Type=EkiOnOff
_Pm1008AlmLineDdmWarningPortn_Object=MibTableColumn
pm1008AlmLineDdmWarningPortn=_Pm1008AlmLineDdmWarningPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,10),_Pm1008AlmLineDdmWarningPortn_Type())
pm1008AlmLineDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineDdmWarningPortn.setStatus(_A)
_Pm1008AlmLineDdmAlmPortn_Type=EkiOnOff
_Pm1008AlmLineDdmAlmPortn_Object=MibTableColumn
pm1008AlmLineDdmAlmPortn=_Pm1008AlmLineDdmAlmPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,11),_Pm1008AlmLineDdmAlmPortn_Type())
pm1008AlmLineDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineDdmAlmPortn.setStatus(_A)
_Pm1008AlmLineFailPortn_Type=EkiOnOff
_Pm1008AlmLineFailPortn_Object=MibTableColumn
pm1008AlmLineFailPortn=_Pm1008AlmLineFailPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,13),_Pm1008AlmLineFailPortn_Type())
pm1008AlmLineFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineFailPortn.setStatus(_A)
_Pm1008AlmLineActivePortn_Type=EkiOnOff
_Pm1008AlmLineActivePortn_Object=MibTableColumn
pm1008AlmLineActivePortn=_Pm1008AlmLineActivePortn_Object((1,3,6,1,4,1,20044,3,2,3,3,7,1,17),_Pm1008AlmLineActivePortn_Type())
pm1008AlmLineActivePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmLineActivePortn.setStatus(_A)
_Pm1008AlmdfrmAlmTable_Object=MibTable
pm1008AlmdfrmAlmTable=_Pm1008AlmdfrmAlmTable_Object((1,3,6,1,4,1,20044,3,2,3,3,128))
if mibBuilder.loadTexts:pm1008AlmdfrmAlmTable.setStatus(_A)
_Pm1008AlmdfrmAlmEntry_Object=MibTableRow
pm1008AlmdfrmAlmEntry=_Pm1008AlmdfrmAlmEntry_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1))
pm1008AlmdfrmAlmEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm1008AlmdfrmAlmEntry.setStatus(_A)
class _Pm1008AlmdfrmAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmdfrmAlmIndex_Type.__name__=_D
_Pm1008AlmdfrmAlmIndex_Object=MibTableColumn
pm1008AlmdfrmAlmIndex=_Pm1008AlmdfrmAlmIndex_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,1),_Pm1008AlmdfrmAlmIndex_Type())
pm1008AlmdfrmAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmdfrmAlmIndex.setStatus(_A)
_Pm1008AlmDwAisDetPortn_Type=EkiOnOff
_Pm1008AlmDwAisDetPortn_Object=MibTableColumn
pm1008AlmDwAisDetPortn=_Pm1008AlmDwAisDetPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,2),_Pm1008AlmDwAisDetPortn_Type())
pm1008AlmDwAisDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwAisDetPortn.setStatus(_A)
_Pm1008AlmDwRdiDetPortn_Type=EkiOnOff
_Pm1008AlmDwRdiDetPortn_Object=MibTableColumn
pm1008AlmDwRdiDetPortn=_Pm1008AlmDwRdiDetPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,3),_Pm1008AlmDwRdiDetPortn_Type())
pm1008AlmDwRdiDetPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwRdiDetPortn.setStatus(_A)
_Pm1008AlmDwOofPortn_Type=EkiOnOff
_Pm1008AlmDwOofPortn_Object=MibTableColumn
pm1008AlmDwOofPortn=_Pm1008AlmDwOofPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,4),_Pm1008AlmDwOofPortn_Type())
pm1008AlmDwOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwOofPortn.setStatus(_A)
_Pm1008AlmDwLofPortn_Type=EkiOnOff
_Pm1008AlmDwLofPortn_Object=MibTableColumn
pm1008AlmDwLofPortn=_Pm1008AlmDwLofPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,5),_Pm1008AlmDwLofPortn_Type())
pm1008AlmDwLofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwLofPortn.setStatus(_A)
_Pm1008AlmDccLoopbackPortn_Type=EkiOnOff
_Pm1008AlmDccLoopbackPortn_Object=MibTableColumn
pm1008AlmDccLoopbackPortn=_Pm1008AlmDccLoopbackPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,15),_Pm1008AlmDccLoopbackPortn_Type())
pm1008AlmDccLoopbackPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDccLoopbackPortn.setStatus(_A)
_Pm1008AlmRxDccBroadStormPortn_Type=EkiOnOff
_Pm1008AlmRxDccBroadStormPortn_Object=MibTableColumn
pm1008AlmRxDccBroadStormPortn=_Pm1008AlmRxDccBroadStormPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,16),_Pm1008AlmRxDccBroadStormPortn_Type())
pm1008AlmRxDccBroadStormPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxDccBroadStormPortn.setStatus(_A)
_Pm1008AlmTxDccBroadStormPortn_Type=EkiOnOff
_Pm1008AlmTxDccBroadStormPortn_Object=MibTableColumn
pm1008AlmTxDccBroadStormPortn=_Pm1008AlmTxDccBroadStormPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,128,1,17),_Pm1008AlmTxDccBroadStormPortn_Type())
pm1008AlmTxDccBroadStormPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxDccBroadStormPortn.setStatus(_A)
_Pm1008AlmlineSyncAlarmsTable_Object=MibTable
pm1008AlmlineSyncAlarmsTable=_Pm1008AlmlineSyncAlarmsTable_Object((1,3,6,1,4,1,20044,3,2,3,3,133))
if mibBuilder.loadTexts:pm1008AlmlineSyncAlarmsTable.setStatus(_A)
_Pm1008AlmlineSyncAlarmsEntry_Object=MibTableRow
pm1008AlmlineSyncAlarmsEntry=_Pm1008AlmlineSyncAlarmsEntry_Object((1,3,6,1,4,1,20044,3,2,3,3,133,1))
pm1008AlmlineSyncAlarmsEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm1008AlmlineSyncAlarmsEntry.setStatus(_A)
class _Pm1008AlmlineSyncAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineSyncAlarmsIndex_Type.__name__=_D
_Pm1008AlmlineSyncAlarmsIndex_Object=MibTableColumn
pm1008AlmlineSyncAlarmsIndex=_Pm1008AlmlineSyncAlarmsIndex_Object((1,3,6,1,4,1,20044,3,2,3,3,133,1,1),_Pm1008AlmlineSyncAlarmsIndex_Type())
pm1008AlmlineSyncAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineSyncAlarmsIndex.setStatus(_A)
_Pm1008AlmDwLockerrPortn_Type=EkiOnOff
_Pm1008AlmDwLockerrPortn_Object=MibTableColumn
pm1008AlmDwLockerrPortn=_Pm1008AlmDwLockerrPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,133,1,13),_Pm1008AlmDwLockerrPortn_Type())
pm1008AlmDwLockerrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwLockerrPortn.setStatus(_A)
_Pm1008AlmUpLockerrPortn_Type=EkiOnOff
_Pm1008AlmUpLockerrPortn_Object=MibTableColumn
pm1008AlmUpLockerrPortn=_Pm1008AlmUpLockerrPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,133,1,14),_Pm1008AlmUpLockerrPortn_Type())
pm1008AlmUpLockerrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmUpLockerrPortn.setStatus(_A)
_Pm1008AlmDwLosPortn_Type=EkiOnOff
_Pm1008AlmDwLosPortn_Object=MibTableColumn
pm1008AlmDwLosPortn=_Pm1008AlmDwLosPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,133,1,17),_Pm1008AlmDwLosPortn_Type())
pm1008AlmDwLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmDwLosPortn.setStatus(_A)
_Pm1008AlmlineXfp1AlarmsTable_Object=MibTable
pm1008AlmlineXfp1AlarmsTable=_Pm1008AlmlineXfp1AlarmsTable_Object((1,3,6,1,4,1,20044,3,2,3,3,211))
if mibBuilder.loadTexts:pm1008AlmlineXfp1AlarmsTable.setStatus(_A)
_Pm1008AlmlineXfp1AlarmsEntry_Object=MibTableRow
pm1008AlmlineXfp1AlarmsEntry=_Pm1008AlmlineXfp1AlarmsEntry_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1))
pm1008AlmlineXfp1AlarmsEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm1008AlmlineXfp1AlarmsEntry.setStatus(_A)
class _Pm1008AlmlineXfp1AlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008AlmlineXfp1AlarmsIndex_Type.__name__=_D
_Pm1008AlmlineXfp1AlarmsIndex_Object=MibTableColumn
pm1008AlmlineXfp1AlarmsIndex=_Pm1008AlmlineXfp1AlarmsIndex_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,1),_Pm1008AlmlineXfp1AlarmsIndex_Type())
pm1008AlmlineXfp1AlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmlineXfp1AlarmsIndex.setStatus(_A)
_Pm1008AlmModNrPortn_Type=EkiOnOff
_Pm1008AlmModNrPortn_Object=MibTableColumn
pm1008AlmModNrPortn=_Pm1008AlmModNrPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,3),_Pm1008AlmModNrPortn_Type())
pm1008AlmModNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmModNrPortn.setStatus(_A)
_Pm1008AlmRxCdrNotLockedPortn_Type=EkiOnOff
_Pm1008AlmRxCdrNotLockedPortn_Object=MibTableColumn
pm1008AlmRxCdrNotLockedPortn=_Pm1008AlmRxCdrNotLockedPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,4),_Pm1008AlmRxCdrNotLockedPortn_Type())
pm1008AlmRxCdrNotLockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxCdrNotLockedPortn.setStatus(_A)
_Pm1008AlmRxNrPortn_Type=EkiOnOff
_Pm1008AlmRxNrPortn_Object=MibTableColumn
pm1008AlmRxNrPortn=_Pm1008AlmRxNrPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,6),_Pm1008AlmRxNrPortn_Type())
pm1008AlmRxNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmRxNrPortn.setStatus(_A)
_Pm1008AlmTxCdrNotLockedPortn_Type=EkiOnOff
_Pm1008AlmTxCdrNotLockedPortn_Object=MibTableColumn
pm1008AlmTxCdrNotLockedPortn=_Pm1008AlmTxCdrNotLockedPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,7),_Pm1008AlmTxCdrNotLockedPortn_Type())
pm1008AlmTxCdrNotLockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxCdrNotLockedPortn.setStatus(_A)
_Pm1008AlmTxFaultPortn_Type=EkiOnOff
_Pm1008AlmTxFaultPortn_Object=MibTableColumn
pm1008AlmTxFaultPortn=_Pm1008AlmTxFaultPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,8),_Pm1008AlmTxFaultPortn_Type())
pm1008AlmTxFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxFaultPortn.setStatus(_A)
_Pm1008AlmTxNrPortn_Type=EkiOnOff
_Pm1008AlmTxNrPortn_Object=MibTableColumn
pm1008AlmTxNrPortn=_Pm1008AlmTxNrPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,9),_Pm1008AlmTxNrPortn_Type())
pm1008AlmTxNrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTxNrPortn.setStatus(_A)
_Pm1008AlmWavelengthUnlockedPortn_Type=EkiOnOff
_Pm1008AlmWavelengthUnlockedPortn_Object=MibTableColumn
pm1008AlmWavelengthUnlockedPortn=_Pm1008AlmWavelengthUnlockedPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,15),_Pm1008AlmWavelengthUnlockedPortn_Type())
pm1008AlmWavelengthUnlockedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmWavelengthUnlockedPortn.setStatus(_A)
_Pm1008AlmTecFaultPortn_Type=EkiOnOff
_Pm1008AlmTecFaultPortn_Object=MibTableColumn
pm1008AlmTecFaultPortn=_Pm1008AlmTecFaultPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,16),_Pm1008AlmTecFaultPortn_Type())
pm1008AlmTecFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmTecFaultPortn.setStatus(_A)
_Pm1008AlmApdSupplyFaultPortn_Type=EkiOnOff
_Pm1008AlmApdSupplyFaultPortn_Object=MibTableColumn
pm1008AlmApdSupplyFaultPortn=_Pm1008AlmApdSupplyFaultPortn_Object((1,3,6,1,4,1,20044,3,2,3,3,211,1,17),_Pm1008AlmApdSupplyFaultPortn_Type())
pm1008AlmApdSupplyFaultPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008AlmApdSupplyFaultPortn.setStatus(_A)
_Pm1008measures_ObjectIdentity=ObjectIdentity
pm1008measures=_Pm1008measures_ObjectIdentity((1,3,6,1,4,1,20044,3,3))
_Pm1008MesrOther_ObjectIdentity=ObjectIdentity
pm1008MesrOther=_Pm1008MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,3,3,1))
_Pm1008Mesrsynth0_Type=EkiMeasureType
_Pm1008Mesrsynth0_Object=MibScalar
pm1008Mesrsynth0=_Pm1008Mesrsynth0_Object((1,3,6,1,4,1,20044,3,3,1,0),_Pm1008Mesrsynth0_Type())
pm1008Mesrsynth0.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrsynth0.setStatus(_G)
_Pm1008Mesrsynth1_Type=EkiMeasureType
_Pm1008Mesrsynth1_Object=MibScalar
pm1008Mesrsynth1=_Pm1008Mesrsynth1_Object((1,3,6,1,4,1,20044,3,3,1,1),_Pm1008Mesrsynth1_Type())
pm1008Mesrsynth1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrsynth1.setStatus(_G)
_Pm1008MesrClient_ObjectIdentity=ObjectIdentity
pm1008MesrClient=_Pm1008MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,3,3,2))
_Pm1008MesrtempMeasTable_Object=MibTable
pm1008MesrtempMeasTable=_Pm1008MesrtempMeasTable_Object((1,3,6,1,4,1,20044,3,3,2,16))
if mibBuilder.loadTexts:pm1008MesrtempMeasTable.setStatus(_A)
_Pm1008MesrtempMeasEntry_Object=MibTableRow
pm1008MesrtempMeasEntry=_Pm1008MesrtempMeasEntry_Object((1,3,6,1,4,1,20044,3,3,2,16,1))
pm1008MesrtempMeasEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm1008MesrtempMeasEntry.setStatus(_A)
class _Pm1008MesrtempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MesrtempMeasIndex_Type.__name__=_D
_Pm1008MesrtempMeasIndex_Object=MibTableColumn
pm1008MesrtempMeasIndex=_Pm1008MesrtempMeasIndex_Object((1,3,6,1,4,1,20044,3,3,2,16,1,1),_Pm1008MesrtempMeasIndex_Type())
pm1008MesrtempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrtempMeasIndex.setStatus(_A)
class _Pm1008MesrtempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008MesrtempMeasPortn_Type.__name__=_D
_Pm1008MesrtempMeasPortn_Object=MibTableColumn
pm1008MesrtempMeasPortn=_Pm1008MesrtempMeasPortn_Object((1,3,6,1,4,1,20044,3,3,2,16,1,2),_Pm1008MesrtempMeasPortn_Type())
pm1008MesrtempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrtempMeasPortn.setStatus(_A)
_Pm1008MesrvoltMeasTable_Object=MibTable
pm1008MesrvoltMeasTable=_Pm1008MesrvoltMeasTable_Object((1,3,6,1,4,1,20044,3,3,2,24))
if mibBuilder.loadTexts:pm1008MesrvoltMeasTable.setStatus(_A)
_Pm1008MesrvoltMeasEntry_Object=MibTableRow
pm1008MesrvoltMeasEntry=_Pm1008MesrvoltMeasEntry_Object((1,3,6,1,4,1,20044,3,3,2,24,1))
pm1008MesrvoltMeasEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm1008MesrvoltMeasEntry.setStatus(_A)
class _Pm1008MesrvoltMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MesrvoltMeasIndex_Type.__name__=_D
_Pm1008MesrvoltMeasIndex_Object=MibTableColumn
pm1008MesrvoltMeasIndex=_Pm1008MesrvoltMeasIndex_Object((1,3,6,1,4,1,20044,3,3,2,24,1,1),_Pm1008MesrvoltMeasIndex_Type())
pm1008MesrvoltMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrvoltMeasIndex.setStatus(_A)
class _Pm1008MesrvoltMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008MesrvoltMeasPortn_Type.__name__=_D
_Pm1008MesrvoltMeasPortn_Object=MibTableColumn
pm1008MesrvoltMeasPortn=_Pm1008MesrvoltMeasPortn_Object((1,3,6,1,4,1,20044,3,3,2,24,1,2),_Pm1008MesrvoltMeasPortn_Type())
pm1008MesrvoltMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrvoltMeasPortn.setStatus(_A)
_Pm1008MesrbiasMeasTable_Object=MibTable
pm1008MesrbiasMeasTable=_Pm1008MesrbiasMeasTable_Object((1,3,6,1,4,1,20044,3,3,2,32))
if mibBuilder.loadTexts:pm1008MesrbiasMeasTable.setStatus(_A)
_Pm1008MesrbiasMeasEntry_Object=MibTableRow
pm1008MesrbiasMeasEntry=_Pm1008MesrbiasMeasEntry_Object((1,3,6,1,4,1,20044,3,3,2,32,1))
pm1008MesrbiasMeasEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm1008MesrbiasMeasEntry.setStatus(_A)
class _Pm1008MesrbiasMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MesrbiasMeasIndex_Type.__name__=_D
_Pm1008MesrbiasMeasIndex_Object=MibTableColumn
pm1008MesrbiasMeasIndex=_Pm1008MesrbiasMeasIndex_Object((1,3,6,1,4,1,20044,3,3,2,32,1,1),_Pm1008MesrbiasMeasIndex_Type())
pm1008MesrbiasMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrbiasMeasIndex.setStatus(_A)
class _Pm1008MesrbiasMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008MesrbiasMeasPortn_Type.__name__=_D
_Pm1008MesrbiasMeasPortn_Object=MibTableColumn
pm1008MesrbiasMeasPortn=_Pm1008MesrbiasMeasPortn_Object((1,3,6,1,4,1,20044,3,3,2,32,1,2),_Pm1008MesrbiasMeasPortn_Type())
pm1008MesrbiasMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrbiasMeasPortn.setStatus(_A)
_Pm1008MesrtxpwrMeasTable_Object=MibTable
pm1008MesrtxpwrMeasTable=_Pm1008MesrtxpwrMeasTable_Object((1,3,6,1,4,1,20044,3,3,2,40))
if mibBuilder.loadTexts:pm1008MesrtxpwrMeasTable.setStatus(_A)
_Pm1008MesrtxpwrMeasEntry_Object=MibTableRow
pm1008MesrtxpwrMeasEntry=_Pm1008MesrtxpwrMeasEntry_Object((1,3,6,1,4,1,20044,3,3,2,40,1))
pm1008MesrtxpwrMeasEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm1008MesrtxpwrMeasEntry.setStatus(_A)
class _Pm1008MesrtxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MesrtxpwrMeasIndex_Type.__name__=_D
_Pm1008MesrtxpwrMeasIndex_Object=MibTableColumn
pm1008MesrtxpwrMeasIndex=_Pm1008MesrtxpwrMeasIndex_Object((1,3,6,1,4,1,20044,3,3,2,40,1,1),_Pm1008MesrtxpwrMeasIndex_Type())
pm1008MesrtxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrtxpwrMeasIndex.setStatus(_A)
class _Pm1008MesrtxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008MesrtxpwrMeasPortn_Type.__name__=_D
_Pm1008MesrtxpwrMeasPortn_Object=MibTableColumn
pm1008MesrtxpwrMeasPortn=_Pm1008MesrtxpwrMeasPortn_Object((1,3,6,1,4,1,20044,3,3,2,40,1,2),_Pm1008MesrtxpwrMeasPortn_Type())
pm1008MesrtxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrtxpwrMeasPortn.setStatus(_A)
_Pm1008MesrrxpwrMeasTable_Object=MibTable
pm1008MesrrxpwrMeasTable=_Pm1008MesrrxpwrMeasTable_Object((1,3,6,1,4,1,20044,3,3,2,48))
if mibBuilder.loadTexts:pm1008MesrrxpwrMeasTable.setStatus(_A)
_Pm1008MesrrxpwrMeasEntry_Object=MibTableRow
pm1008MesrrxpwrMeasEntry=_Pm1008MesrrxpwrMeasEntry_Object((1,3,6,1,4,1,20044,3,3,2,48,1))
pm1008MesrrxpwrMeasEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm1008MesrrxpwrMeasEntry.setStatus(_A)
class _Pm1008MesrrxpwrMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MesrrxpwrMeasIndex_Type.__name__=_D
_Pm1008MesrrxpwrMeasIndex_Object=MibTableColumn
pm1008MesrrxpwrMeasIndex=_Pm1008MesrrxpwrMeasIndex_Object((1,3,6,1,4,1,20044,3,3,2,48,1,1),_Pm1008MesrrxpwrMeasIndex_Type())
pm1008MesrrxpwrMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrrxpwrMeasIndex.setStatus(_A)
class _Pm1008MesrrxpwrMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008MesrrxpwrMeasPortn_Type.__name__=_D
_Pm1008MesrrxpwrMeasPortn_Object=MibTableColumn
pm1008MesrrxpwrMeasPortn=_Pm1008MesrrxpwrMeasPortn_Object((1,3,6,1,4,1,20044,3,3,2,48,1,2),_Pm1008MesrrxpwrMeasPortn_Type())
pm1008MesrrxpwrMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MesrrxpwrMeasPortn.setStatus(_A)
_Pm1008MesrLine_ObjectIdentity=ObjectIdentity
pm1008MesrLine=_Pm1008MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,3,3,3))
_Pm1008Mesrxfp1LxModTempMeasTable_Object=MibTable
pm1008Mesrxfp1LxModTempMeasTable=_Pm1008Mesrxfp1LxModTempMeasTable_Object((1,3,6,1,4,1,20044,3,3,3,208))
if mibBuilder.loadTexts:pm1008Mesrxfp1LxModTempMeasTable.setStatus(_A)
_Pm1008Mesrxfp1LxModTempMeasEntry_Object=MibTableRow
pm1008Mesrxfp1LxModTempMeasEntry=_Pm1008Mesrxfp1LxModTempMeasEntry_Object((1,3,6,1,4,1,20044,3,3,3,208,1))
pm1008Mesrxfp1LxModTempMeasEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm1008Mesrxfp1LxModTempMeasEntry.setStatus(_A)
class _Pm1008Mesrxfp1LxModTempMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1LxModTempMeasIndex_Type.__name__=_D
_Pm1008Mesrxfp1LxModTempMeasIndex_Object=MibTableColumn
pm1008Mesrxfp1LxModTempMeasIndex=_Pm1008Mesrxfp1LxModTempMeasIndex_Object((1,3,6,1,4,1,20044,3,3,3,208,1,1),_Pm1008Mesrxfp1LxModTempMeasIndex_Type())
pm1008Mesrxfp1LxModTempMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LxModTempMeasIndex.setStatus(_A)
class _Pm1008Mesrxfp1LxModTempMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1LxModTempMeasPortn_Type.__name__=_D
_Pm1008Mesrxfp1LxModTempMeasPortn_Object=MibTableColumn
pm1008Mesrxfp1LxModTempMeasPortn=_Pm1008Mesrxfp1LxModTempMeasPortn_Object((1,3,6,1,4,1,20044,3,3,3,208,1,2),_Pm1008Mesrxfp1LxModTempMeasPortn_Type())
pm1008Mesrxfp1LxModTempMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LxModTempMeasPortn.setStatus(_A)
_Pm1008Mesrxfp1ReservedTable_Object=MibTable
pm1008Mesrxfp1ReservedTable=_Pm1008Mesrxfp1ReservedTable_Object((1,3,6,1,4,1,20044,3,3,3,209))
if mibBuilder.loadTexts:pm1008Mesrxfp1ReservedTable.setStatus(_G)
_Pm1008Mesrxfp1ReservedEntry_Object=MibTableRow
pm1008Mesrxfp1ReservedEntry=_Pm1008Mesrxfp1ReservedEntry_Object((1,3,6,1,4,1,20044,3,3,3,209,1))
pm1008Mesrxfp1ReservedEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm1008Mesrxfp1ReservedEntry.setStatus(_G)
class _Pm1008Mesrxfp1ReservedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1ReservedIndex_Type.__name__=_D
_Pm1008Mesrxfp1ReservedIndex_Object=MibTableColumn
pm1008Mesrxfp1ReservedIndex=_Pm1008Mesrxfp1ReservedIndex_Object((1,3,6,1,4,1,20044,3,3,3,209,1,1),_Pm1008Mesrxfp1ReservedIndex_Type())
pm1008Mesrxfp1ReservedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1ReservedIndex.setStatus(_G)
class _Pm1008Mesrxfp1ReservedPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1ReservedPortn_Type.__name__=_D
_Pm1008Mesrxfp1ReservedPortn_Object=MibTableColumn
pm1008Mesrxfp1ReservedPortn=_Pm1008Mesrxfp1ReservedPortn_Object((1,3,6,1,4,1,20044,3,3,3,209,1,2),_Pm1008Mesrxfp1ReservedPortn_Type())
pm1008Mesrxfp1ReservedPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1ReservedPortn.setStatus(_G)
_Pm1008Mesrxfp1LoBiasCurrentMeasTable_Object=MibTable
pm1008Mesrxfp1LoBiasCurrentMeasTable=_Pm1008Mesrxfp1LoBiasCurrentMeasTable_Object((1,3,6,1,4,1,20044,3,3,3,210))
if mibBuilder.loadTexts:pm1008Mesrxfp1LoBiasCurrentMeasTable.setStatus(_A)
_Pm1008Mesrxfp1LoBiasCurrentMeasEntry_Object=MibTableRow
pm1008Mesrxfp1LoBiasCurrentMeasEntry=_Pm1008Mesrxfp1LoBiasCurrentMeasEntry_Object((1,3,6,1,4,1,20044,3,3,3,210,1))
pm1008Mesrxfp1LoBiasCurrentMeasEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm1008Mesrxfp1LoBiasCurrentMeasEntry.setStatus(_A)
class _Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Type.__name__=_D
_Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Object=MibTableColumn
pm1008Mesrxfp1LoBiasCurrentMeasIndex=_Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Object((1,3,6,1,4,1,20044,3,3,3,210,1,1),_Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Type())
pm1008Mesrxfp1LoBiasCurrentMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LoBiasCurrentMeasIndex.setStatus(_A)
class _Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Type.__name__=_D
_Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Object=MibTableColumn
pm1008Mesrxfp1LoBiasCurrentMeasPortn=_Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Object((1,3,6,1,4,1,20044,3,3,3,210,1,2),_Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Type())
pm1008Mesrxfp1LoBiasCurrentMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LoBiasCurrentMeasPortn.setStatus(_A)
_Pm1008Mesrxfp1LoTxPowerMeasTable_Object=MibTable
pm1008Mesrxfp1LoTxPowerMeasTable=_Pm1008Mesrxfp1LoTxPowerMeasTable_Object((1,3,6,1,4,1,20044,3,3,3,211))
if mibBuilder.loadTexts:pm1008Mesrxfp1LoTxPowerMeasTable.setStatus(_A)
_Pm1008Mesrxfp1LoTxPowerMeasEntry_Object=MibTableRow
pm1008Mesrxfp1LoTxPowerMeasEntry=_Pm1008Mesrxfp1LoTxPowerMeasEntry_Object((1,3,6,1,4,1,20044,3,3,3,211,1))
pm1008Mesrxfp1LoTxPowerMeasEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm1008Mesrxfp1LoTxPowerMeasEntry.setStatus(_A)
class _Pm1008Mesrxfp1LoTxPowerMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1LoTxPowerMeasIndex_Type.__name__=_D
_Pm1008Mesrxfp1LoTxPowerMeasIndex_Object=MibTableColumn
pm1008Mesrxfp1LoTxPowerMeasIndex=_Pm1008Mesrxfp1LoTxPowerMeasIndex_Object((1,3,6,1,4,1,20044,3,3,3,211,1,1),_Pm1008Mesrxfp1LoTxPowerMeasIndex_Type())
pm1008Mesrxfp1LoTxPowerMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LoTxPowerMeasIndex.setStatus(_A)
class _Pm1008Mesrxfp1LoTxPowerMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1LoTxPowerMeasPortn_Type.__name__=_D
_Pm1008Mesrxfp1LoTxPowerMeasPortn_Object=MibTableColumn
pm1008Mesrxfp1LoTxPowerMeasPortn=_Pm1008Mesrxfp1LoTxPowerMeasPortn_Object((1,3,6,1,4,1,20044,3,3,3,211,1,2),_Pm1008Mesrxfp1LoTxPowerMeasPortn_Type())
pm1008Mesrxfp1LoTxPowerMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LoTxPowerMeasPortn.setStatus(_A)
_Pm1008Mesrxfp1LiRxPowerMeasTable_Object=MibTable
pm1008Mesrxfp1LiRxPowerMeasTable=_Pm1008Mesrxfp1LiRxPowerMeasTable_Object((1,3,6,1,4,1,20044,3,3,3,212))
if mibBuilder.loadTexts:pm1008Mesrxfp1LiRxPowerMeasTable.setStatus(_A)
_Pm1008Mesrxfp1LiRxPowerMeasEntry_Object=MibTableRow
pm1008Mesrxfp1LiRxPowerMeasEntry=_Pm1008Mesrxfp1LiRxPowerMeasEntry_Object((1,3,6,1,4,1,20044,3,3,3,212,1))
pm1008Mesrxfp1LiRxPowerMeasEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm1008Mesrxfp1LiRxPowerMeasEntry.setStatus(_A)
class _Pm1008Mesrxfp1LiRxPowerMeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1LiRxPowerMeasIndex_Type.__name__=_D
_Pm1008Mesrxfp1LiRxPowerMeasIndex_Object=MibTableColumn
pm1008Mesrxfp1LiRxPowerMeasIndex=_Pm1008Mesrxfp1LiRxPowerMeasIndex_Object((1,3,6,1,4,1,20044,3,3,3,212,1,1),_Pm1008Mesrxfp1LiRxPowerMeasIndex_Type())
pm1008Mesrxfp1LiRxPowerMeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LiRxPowerMeasIndex.setStatus(_A)
class _Pm1008Mesrxfp1LiRxPowerMeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1LiRxPowerMeasPortn_Type.__name__=_D
_Pm1008Mesrxfp1LiRxPowerMeasPortn_Object=MibTableColumn
pm1008Mesrxfp1LiRxPowerMeasPortn=_Pm1008Mesrxfp1LiRxPowerMeasPortn_Object((1,3,6,1,4,1,20044,3,3,3,212,1,2),_Pm1008Mesrxfp1LiRxPowerMeasPortn_Type())
pm1008Mesrxfp1LiRxPowerMeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LiRxPowerMeasPortn.setStatus(_A)
_Pm1008Mesrxfp1LxAux1MeasTable_Object=MibTable
pm1008Mesrxfp1LxAux1MeasTable=_Pm1008Mesrxfp1LxAux1MeasTable_Object((1,3,6,1,4,1,20044,3,3,3,213))
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux1MeasTable.setStatus(_G)
_Pm1008Mesrxfp1LxAux1MeasEntry_Object=MibTableRow
pm1008Mesrxfp1LxAux1MeasEntry=_Pm1008Mesrxfp1LxAux1MeasEntry_Object((1,3,6,1,4,1,20044,3,3,3,213,1))
pm1008Mesrxfp1LxAux1MeasEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux1MeasEntry.setStatus(_G)
class _Pm1008Mesrxfp1LxAux1MeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1LxAux1MeasIndex_Type.__name__=_D
_Pm1008Mesrxfp1LxAux1MeasIndex_Object=MibTableColumn
pm1008Mesrxfp1LxAux1MeasIndex=_Pm1008Mesrxfp1LxAux1MeasIndex_Object((1,3,6,1,4,1,20044,3,3,3,213,1,1),_Pm1008Mesrxfp1LxAux1MeasIndex_Type())
pm1008Mesrxfp1LxAux1MeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux1MeasIndex.setStatus(_G)
class _Pm1008Mesrxfp1LxAux1MeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1LxAux1MeasPortn_Type.__name__=_D
_Pm1008Mesrxfp1LxAux1MeasPortn_Object=MibTableColumn
pm1008Mesrxfp1LxAux1MeasPortn=_Pm1008Mesrxfp1LxAux1MeasPortn_Object((1,3,6,1,4,1,20044,3,3,3,213,1,2),_Pm1008Mesrxfp1LxAux1MeasPortn_Type())
pm1008Mesrxfp1LxAux1MeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux1MeasPortn.setStatus(_G)
_Pm1008Mesrxfp1LxAux2MeasTable_Object=MibTable
pm1008Mesrxfp1LxAux2MeasTable=_Pm1008Mesrxfp1LxAux2MeasTable_Object((1,3,6,1,4,1,20044,3,3,3,214))
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux2MeasTable.setStatus(_G)
_Pm1008Mesrxfp1LxAux2MeasEntry_Object=MibTableRow
pm1008Mesrxfp1LxAux2MeasEntry=_Pm1008Mesrxfp1LxAux2MeasEntry_Object((1,3,6,1,4,1,20044,3,3,3,214,1))
pm1008Mesrxfp1LxAux2MeasEntry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux2MeasEntry.setStatus(_G)
class _Pm1008Mesrxfp1LxAux2MeasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrxfp1LxAux2MeasIndex_Type.__name__=_D
_Pm1008Mesrxfp1LxAux2MeasIndex_Object=MibTableColumn
pm1008Mesrxfp1LxAux2MeasIndex=_Pm1008Mesrxfp1LxAux2MeasIndex_Object((1,3,6,1,4,1,20044,3,3,3,214,1,1),_Pm1008Mesrxfp1LxAux2MeasIndex_Type())
pm1008Mesrxfp1LxAux2MeasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux2MeasIndex.setStatus(_G)
class _Pm1008Mesrxfp1LxAux2MeasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrxfp1LxAux2MeasPortn_Type.__name__=_D
_Pm1008Mesrxfp1LxAux2MeasPortn_Object=MibTableColumn
pm1008Mesrxfp1LxAux2MeasPortn=_Pm1008Mesrxfp1LxAux2MeasPortn_Object((1,3,6,1,4,1,20044,3,3,3,214,1,2),_Pm1008Mesrxfp1LxAux2MeasPortn_Type())
pm1008Mesrxfp1LxAux2MeasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrxfp1LxAux2MeasPortn.setStatus(_G)
_Pm1008Mesrotx1AgingTable_Object=MibTable
pm1008Mesrotx1AgingTable=_Pm1008Mesrotx1AgingTable_Object((1,3,6,1,4,1,20044,3,3,3,224))
if mibBuilder.loadTexts:pm1008Mesrotx1AgingTable.setStatus(_A)
_Pm1008Mesrotx1AgingEntry_Object=MibTableRow
pm1008Mesrotx1AgingEntry=_Pm1008Mesrotx1AgingEntry_Object((1,3,6,1,4,1,20044,3,3,3,224,1))
pm1008Mesrotx1AgingEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm1008Mesrotx1AgingEntry.setStatus(_A)
class _Pm1008Mesrotx1AgingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrotx1AgingIndex_Type.__name__=_D
_Pm1008Mesrotx1AgingIndex_Object=MibTableColumn
pm1008Mesrotx1AgingIndex=_Pm1008Mesrotx1AgingIndex_Object((1,3,6,1,4,1,20044,3,3,3,224,1,1),_Pm1008Mesrotx1AgingIndex_Type())
pm1008Mesrotx1AgingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1AgingIndex.setStatus(_A)
class _Pm1008Mesrotx1AgingPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrotx1AgingPortn_Type.__name__=_D
_Pm1008Mesrotx1AgingPortn_Object=MibTableColumn
pm1008Mesrotx1AgingPortn=_Pm1008Mesrotx1AgingPortn_Object((1,3,6,1,4,1,20044,3,3,3,224,1,2),_Pm1008Mesrotx1AgingPortn_Type())
pm1008Mesrotx1AgingPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1AgingPortn.setStatus(_A)
_Pm1008Mesrotx1LaserTemperatureTable_Object=MibTable
pm1008Mesrotx1LaserTemperatureTable=_Pm1008Mesrotx1LaserTemperatureTable_Object((1,3,6,1,4,1,20044,3,3,3,225))
if mibBuilder.loadTexts:pm1008Mesrotx1LaserTemperatureTable.setStatus(_G)
_Pm1008Mesrotx1LaserTemperatureEntry_Object=MibTableRow
pm1008Mesrotx1LaserTemperatureEntry=_Pm1008Mesrotx1LaserTemperatureEntry_Object((1,3,6,1,4,1,20044,3,3,3,225,1))
pm1008Mesrotx1LaserTemperatureEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm1008Mesrotx1LaserTemperatureEntry.setStatus(_G)
class _Pm1008Mesrotx1LaserTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrotx1LaserTemperatureIndex_Type.__name__=_D
_Pm1008Mesrotx1LaserTemperatureIndex_Object=MibTableColumn
pm1008Mesrotx1LaserTemperatureIndex=_Pm1008Mesrotx1LaserTemperatureIndex_Object((1,3,6,1,4,1,20044,3,3,3,225,1,1),_Pm1008Mesrotx1LaserTemperatureIndex_Type())
pm1008Mesrotx1LaserTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1LaserTemperatureIndex.setStatus(_G)
class _Pm1008Mesrotx1LaserTemperaturePortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrotx1LaserTemperaturePortn_Type.__name__=_D
_Pm1008Mesrotx1LaserTemperaturePortn_Object=MibTableColumn
pm1008Mesrotx1LaserTemperaturePortn=_Pm1008Mesrotx1LaserTemperaturePortn_Object((1,3,6,1,4,1,20044,3,3,3,225,1,2),_Pm1008Mesrotx1LaserTemperaturePortn_Type())
pm1008Mesrotx1LaserTemperaturePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1LaserTemperaturePortn.setStatus(_G)
_Pm1008Mesrotx1FreqDeviationTable_Object=MibTable
pm1008Mesrotx1FreqDeviationTable=_Pm1008Mesrotx1FreqDeviationTable_Object((1,3,6,1,4,1,20044,3,3,3,226))
if mibBuilder.loadTexts:pm1008Mesrotx1FreqDeviationTable.setStatus(_A)
_Pm1008Mesrotx1FreqDeviationEntry_Object=MibTableRow
pm1008Mesrotx1FreqDeviationEntry=_Pm1008Mesrotx1FreqDeviationEntry_Object((1,3,6,1,4,1,20044,3,3,3,226,1))
pm1008Mesrotx1FreqDeviationEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm1008Mesrotx1FreqDeviationEntry.setStatus(_A)
class _Pm1008Mesrotx1FreqDeviationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrotx1FreqDeviationIndex_Type.__name__=_D
_Pm1008Mesrotx1FreqDeviationIndex_Object=MibTableColumn
pm1008Mesrotx1FreqDeviationIndex=_Pm1008Mesrotx1FreqDeviationIndex_Object((1,3,6,1,4,1,20044,3,3,3,226,1,1),_Pm1008Mesrotx1FreqDeviationIndex_Type())
pm1008Mesrotx1FreqDeviationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1FreqDeviationIndex.setStatus(_A)
class _Pm1008Mesrotx1FreqDeviationPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrotx1FreqDeviationPortn_Type.__name__=_D
_Pm1008Mesrotx1FreqDeviationPortn_Object=MibTableColumn
pm1008Mesrotx1FreqDeviationPortn=_Pm1008Mesrotx1FreqDeviationPortn_Object((1,3,6,1,4,1,20044,3,3,3,226,1,2),_Pm1008Mesrotx1FreqDeviationPortn_Type())
pm1008Mesrotx1FreqDeviationPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1FreqDeviationPortn.setStatus(_A)
_Pm1008Mesrotx1LaserWvlengthTable_Object=MibTable
pm1008Mesrotx1LaserWvlengthTable=_Pm1008Mesrotx1LaserWvlengthTable_Object((1,3,6,1,4,1,20044,3,3,3,227))
if mibBuilder.loadTexts:pm1008Mesrotx1LaserWvlengthTable.setStatus(_A)
_Pm1008Mesrotx1LaserWvlengthEntry_Object=MibTableRow
pm1008Mesrotx1LaserWvlengthEntry=_Pm1008Mesrotx1LaserWvlengthEntry_Object((1,3,6,1,4,1,20044,3,3,3,227,1))
pm1008Mesrotx1LaserWvlengthEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm1008Mesrotx1LaserWvlengthEntry.setStatus(_A)
class _Pm1008Mesrotx1LaserWvlengthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008Mesrotx1LaserWvlengthIndex_Type.__name__=_D
_Pm1008Mesrotx1LaserWvlengthIndex_Object=MibTableColumn
pm1008Mesrotx1LaserWvlengthIndex=_Pm1008Mesrotx1LaserWvlengthIndex_Object((1,3,6,1,4,1,20044,3,3,3,227,1,1),_Pm1008Mesrotx1LaserWvlengthIndex_Type())
pm1008Mesrotx1LaserWvlengthIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1LaserWvlengthIndex.setStatus(_A)
class _Pm1008Mesrotx1LaserWvlengthPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1008Mesrotx1LaserWvlengthPortn_Type.__name__=_D
_Pm1008Mesrotx1LaserWvlengthPortn_Object=MibTableColumn
pm1008Mesrotx1LaserWvlengthPortn=_Pm1008Mesrotx1LaserWvlengthPortn_Object((1,3,6,1,4,1,20044,3,3,3,227,1,2),_Pm1008Mesrotx1LaserWvlengthPortn_Type())
pm1008Mesrotx1LaserWvlengthPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Mesrotx1LaserWvlengthPortn.setStatus(_A)
_Pm1008counters_ObjectIdentity=ObjectIdentity
pm1008counters=_Pm1008counters_ObjectIdentity((1,3,6,1,4,1,20044,3,4))
_Pm1008CntOther_ObjectIdentity=ObjectIdentity
pm1008CntOther=_Pm1008CntOther_ObjectIdentity((1,3,6,1,4,1,20044,3,4,1))
_Pm1008CntClient_ObjectIdentity=ObjectIdentity
pm1008CntClient=_Pm1008CntClient_ObjectIdentity((1,3,6,1,4,1,20044,3,4,2))
_Pm1008CntupRaRemCntTable_Object=MibTable
pm1008CntupRaRemCntTable=_Pm1008CntupRaRemCntTable_Object((1,3,6,1,4,1,20044,3,4,2,16))
if mibBuilder.loadTexts:pm1008CntupRaRemCntTable.setStatus(_A)
_Pm1008CntupRaRemCntEntry_Object=MibTableRow
pm1008CntupRaRemCntEntry=_Pm1008CntupRaRemCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,16,1))
pm1008CntupRaRemCntEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm1008CntupRaRemCntEntry.setStatus(_A)
class _Pm1008CntupRaRemCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntupRaRemCntIndex_Type.__name__=_D
_Pm1008CntupRaRemCntIndex_Object=MibTableColumn
pm1008CntupRaRemCntIndex=_Pm1008CntupRaRemCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,16,1,1),_Pm1008CntupRaRemCntIndex_Type())
pm1008CntupRaRemCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaRemCntIndex.setStatus(_A)
_Pm1008CntupRaRemCntValuePortn_Type=Counter32
_Pm1008CntupRaRemCntValuePortn_Object=MibTableColumn
pm1008CntupRaRemCntValuePortn=_Pm1008CntupRaRemCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,16,1,2),_Pm1008CntupRaRemCntValuePortn_Type())
pm1008CntupRaRemCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaRemCntValuePortn.setStatus(_A)
_Pm1008CntupRaRemCntErrorPortn_Type=EkiOnOff
_Pm1008CntupRaRemCntErrorPortn_Object=MibTableColumn
pm1008CntupRaRemCntErrorPortn=_Pm1008CntupRaRemCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,16,1,3),_Pm1008CntupRaRemCntErrorPortn_Type())
pm1008CntupRaRemCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaRemCntErrorPortn.setStatus(_A)
_Pm1008CntupRaRemCntOverloadPortn_Type=EkiOnOff
_Pm1008CntupRaRemCntOverloadPortn_Object=MibTableColumn
pm1008CntupRaRemCntOverloadPortn=_Pm1008CntupRaRemCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,16,1,4),_Pm1008CntupRaRemCntOverloadPortn_Type())
pm1008CntupRaRemCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaRemCntOverloadPortn.setStatus(_A)
_Pm1008CntupRaInsCntTable_Object=MibTable
pm1008CntupRaInsCntTable=_Pm1008CntupRaInsCntTable_Object((1,3,6,1,4,1,20044,3,4,2,24))
if mibBuilder.loadTexts:pm1008CntupRaInsCntTable.setStatus(_A)
_Pm1008CntupRaInsCntEntry_Object=MibTableRow
pm1008CntupRaInsCntEntry=_Pm1008CntupRaInsCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,24,1))
pm1008CntupRaInsCntEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm1008CntupRaInsCntEntry.setStatus(_A)
class _Pm1008CntupRaInsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntupRaInsCntIndex_Type.__name__=_D
_Pm1008CntupRaInsCntIndex_Object=MibTableColumn
pm1008CntupRaInsCntIndex=_Pm1008CntupRaInsCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,24,1,1),_Pm1008CntupRaInsCntIndex_Type())
pm1008CntupRaInsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaInsCntIndex.setStatus(_A)
_Pm1008CntupRaInsCntValuePortn_Type=Counter32
_Pm1008CntupRaInsCntValuePortn_Object=MibTableColumn
pm1008CntupRaInsCntValuePortn=_Pm1008CntupRaInsCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,24,1,2),_Pm1008CntupRaInsCntValuePortn_Type())
pm1008CntupRaInsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaInsCntValuePortn.setStatus(_A)
_Pm1008CntupRaInsCntErrorPortn_Type=EkiOnOff
_Pm1008CntupRaInsCntErrorPortn_Object=MibTableColumn
pm1008CntupRaInsCntErrorPortn=_Pm1008CntupRaInsCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,24,1,3),_Pm1008CntupRaInsCntErrorPortn_Type())
pm1008CntupRaInsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaInsCntErrorPortn.setStatus(_A)
_Pm1008CntupRaInsCntOverloadPortn_Type=EkiOnOff
_Pm1008CntupRaInsCntOverloadPortn_Object=MibTableColumn
pm1008CntupRaInsCntOverloadPortn=_Pm1008CntupRaInsCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,24,1,4),_Pm1008CntupRaInsCntOverloadPortn_Type())
pm1008CntupRaInsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRaInsCntOverloadPortn.setStatus(_A)
_Pm1008CntupRdErrCntTable_Object=MibTable
pm1008CntupRdErrCntTable=_Pm1008CntupRdErrCntTable_Object((1,3,6,1,4,1,20044,3,4,2,32))
if mibBuilder.loadTexts:pm1008CntupRdErrCntTable.setStatus(_A)
_Pm1008CntupRdErrCntEntry_Object=MibTableRow
pm1008CntupRdErrCntEntry=_Pm1008CntupRdErrCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,32,1))
pm1008CntupRdErrCntEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm1008CntupRdErrCntEntry.setStatus(_A)
class _Pm1008CntupRdErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntupRdErrCntIndex_Type.__name__=_D
_Pm1008CntupRdErrCntIndex_Object=MibTableColumn
pm1008CntupRdErrCntIndex=_Pm1008CntupRdErrCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,32,1,1),_Pm1008CntupRdErrCntIndex_Type())
pm1008CntupRdErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRdErrCntIndex.setStatus(_A)
_Pm1008CntupRdErrCntValuePortn_Type=Counter32
_Pm1008CntupRdErrCntValuePortn_Object=MibTableColumn
pm1008CntupRdErrCntValuePortn=_Pm1008CntupRdErrCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,32,1,2),_Pm1008CntupRdErrCntValuePortn_Type())
pm1008CntupRdErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRdErrCntValuePortn.setStatus(_A)
_Pm1008CntupRdErrCntErrorPortn_Type=EkiOnOff
_Pm1008CntupRdErrCntErrorPortn_Object=MibTableColumn
pm1008CntupRdErrCntErrorPortn=_Pm1008CntupRdErrCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,32,1,3),_Pm1008CntupRdErrCntErrorPortn_Type())
pm1008CntupRdErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRdErrCntErrorPortn.setStatus(_A)
_Pm1008CntupRdErrCntOverloadPortn_Type=EkiOnOff
_Pm1008CntupRdErrCntOverloadPortn_Object=MibTableColumn
pm1008CntupRdErrCntOverloadPortn=_Pm1008CntupRdErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,32,1,4),_Pm1008CntupRdErrCntOverloadPortn_Type())
pm1008CntupRdErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupRdErrCntOverloadPortn.setStatus(_A)
_Pm1008CntupTimCntTable_Object=MibTable
pm1008CntupTimCntTable=_Pm1008CntupTimCntTable_Object((1,3,6,1,4,1,20044,3,4,2,40))
if mibBuilder.loadTexts:pm1008CntupTimCntTable.setStatus(_A)
_Pm1008CntupTimCntEntry_Object=MibTableRow
pm1008CntupTimCntEntry=_Pm1008CntupTimCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,40,1))
pm1008CntupTimCntEntry.setIndexNames((0,_C,_A4))
if mibBuilder.loadTexts:pm1008CntupTimCntEntry.setStatus(_A)
class _Pm1008CntupTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntupTimCntIndex_Type.__name__=_D
_Pm1008CntupTimCntIndex_Object=MibTableColumn
pm1008CntupTimCntIndex=_Pm1008CntupTimCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,40,1,1),_Pm1008CntupTimCntIndex_Type())
pm1008CntupTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupTimCntIndex.setStatus(_A)
_Pm1008CntupTimCntValuePortn_Type=Counter32
_Pm1008CntupTimCntValuePortn_Object=MibTableColumn
pm1008CntupTimCntValuePortn=_Pm1008CntupTimCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,40,1,2),_Pm1008CntupTimCntValuePortn_Type())
pm1008CntupTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupTimCntValuePortn.setStatus(_A)
_Pm1008CntupTimCntErrorPortn_Type=EkiOnOff
_Pm1008CntupTimCntErrorPortn_Object=MibTableColumn
pm1008CntupTimCntErrorPortn=_Pm1008CntupTimCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,40,1,3),_Pm1008CntupTimCntErrorPortn_Type())
pm1008CntupTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupTimCntErrorPortn.setStatus(_A)
_Pm1008CntupTimCntOverloadPortn_Type=EkiOnOff
_Pm1008CntupTimCntOverloadPortn_Object=MibTableColumn
pm1008CntupTimCntOverloadPortn=_Pm1008CntupTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,40,1,4),_Pm1008CntupTimCntOverloadPortn_Type())
pm1008CntupTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupTimCntOverloadPortn.setStatus(_A)
_Pm1008CntupCvErrCntTable_Object=MibTable
pm1008CntupCvErrCntTable=_Pm1008CntupCvErrCntTable_Object((1,3,6,1,4,1,20044,3,4,2,48))
if mibBuilder.loadTexts:pm1008CntupCvErrCntTable.setStatus(_A)
_Pm1008CntupCvErrCntEntry_Object=MibTableRow
pm1008CntupCvErrCntEntry=_Pm1008CntupCvErrCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,48,1))
pm1008CntupCvErrCntEntry.setIndexNames((0,_C,_A5))
if mibBuilder.loadTexts:pm1008CntupCvErrCntEntry.setStatus(_A)
class _Pm1008CntupCvErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntupCvErrCntIndex_Type.__name__=_D
_Pm1008CntupCvErrCntIndex_Object=MibTableColumn
pm1008CntupCvErrCntIndex=_Pm1008CntupCvErrCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,48,1,1),_Pm1008CntupCvErrCntIndex_Type())
pm1008CntupCvErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupCvErrCntIndex.setStatus(_A)
_Pm1008CntupCvErrCntValuePortn_Type=Counter32
_Pm1008CntupCvErrCntValuePortn_Object=MibTableColumn
pm1008CntupCvErrCntValuePortn=_Pm1008CntupCvErrCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,48,1,2),_Pm1008CntupCvErrCntValuePortn_Type())
pm1008CntupCvErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupCvErrCntValuePortn.setStatus(_A)
_Pm1008CntupCvErrCntErrorPortn_Type=EkiOnOff
_Pm1008CntupCvErrCntErrorPortn_Object=MibTableColumn
pm1008CntupCvErrCntErrorPortn=_Pm1008CntupCvErrCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,48,1,3),_Pm1008CntupCvErrCntErrorPortn_Type())
pm1008CntupCvErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupCvErrCntErrorPortn.setStatus(_A)
_Pm1008CntupCvErrCntOverloadPortn_Type=EkiOnOff
_Pm1008CntupCvErrCntOverloadPortn_Object=MibTableColumn
pm1008CntupCvErrCntOverloadPortn=_Pm1008CntupCvErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,48,1,4),_Pm1008CntupCvErrCntOverloadPortn_Type())
pm1008CntupCvErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntupCvErrCntOverloadPortn.setStatus(_A)
_Pm1008CntdwCbipCntTable_Object=MibTable
pm1008CntdwCbipCntTable=_Pm1008CntdwCbipCntTable_Object((1,3,6,1,4,1,20044,3,4,2,64))
if mibBuilder.loadTexts:pm1008CntdwCbipCntTable.setStatus(_A)
_Pm1008CntdwCbipCntEntry_Object=MibTableRow
pm1008CntdwCbipCntEntry=_Pm1008CntdwCbipCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,64,1))
pm1008CntdwCbipCntEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:pm1008CntdwCbipCntEntry.setStatus(_A)
class _Pm1008CntdwCbipCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntdwCbipCntIndex_Type.__name__=_D
_Pm1008CntdwCbipCntIndex_Object=MibTableColumn
pm1008CntdwCbipCntIndex=_Pm1008CntdwCbipCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,64,1,1),_Pm1008CntdwCbipCntIndex_Type())
pm1008CntdwCbipCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwCbipCntIndex.setStatus(_A)
_Pm1008CntdwCbipCntValuePortn_Type=Counter32
_Pm1008CntdwCbipCntValuePortn_Object=MibTableColumn
pm1008CntdwCbipCntValuePortn=_Pm1008CntdwCbipCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,64,1,2),_Pm1008CntdwCbipCntValuePortn_Type())
pm1008CntdwCbipCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwCbipCntValuePortn.setStatus(_A)
_Pm1008CntdwCbipCntErrorPortn_Type=EkiOnOff
_Pm1008CntdwCbipCntErrorPortn_Object=MibTableColumn
pm1008CntdwCbipCntErrorPortn=_Pm1008CntdwCbipCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,64,1,3),_Pm1008CntdwCbipCntErrorPortn_Type())
pm1008CntdwCbipCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwCbipCntErrorPortn.setStatus(_A)
_Pm1008CntdwCbipCntOverloadPortn_Type=EkiOnOff
_Pm1008CntdwCbipCntOverloadPortn_Object=MibTableColumn
pm1008CntdwCbipCntOverloadPortn=_Pm1008CntdwCbipCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,64,1,4),_Pm1008CntdwCbipCntOverloadPortn_Type())
pm1008CntdwCbipCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwCbipCntOverloadPortn.setStatus(_A)
_Pm1008CntdwTimCntTable_Object=MibTable
pm1008CntdwTimCntTable=_Pm1008CntdwTimCntTable_Object((1,3,6,1,4,1,20044,3,4,2,72))
if mibBuilder.loadTexts:pm1008CntdwTimCntTable.setStatus(_A)
_Pm1008CntdwTimCntEntry_Object=MibTableRow
pm1008CntdwTimCntEntry=_Pm1008CntdwTimCntEntry_Object((1,3,6,1,4,1,20044,3,4,2,72,1))
pm1008CntdwTimCntEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:pm1008CntdwTimCntEntry.setStatus(_A)
class _Pm1008CntdwTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntdwTimCntIndex_Type.__name__=_D
_Pm1008CntdwTimCntIndex_Object=MibTableColumn
pm1008CntdwTimCntIndex=_Pm1008CntdwTimCntIndex_Object((1,3,6,1,4,1,20044,3,4,2,72,1,1),_Pm1008CntdwTimCntIndex_Type())
pm1008CntdwTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwTimCntIndex.setStatus(_A)
_Pm1008CntdwTimCntValuePortn_Type=Counter32
_Pm1008CntdwTimCntValuePortn_Object=MibTableColumn
pm1008CntdwTimCntValuePortn=_Pm1008CntdwTimCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,2,72,1,2),_Pm1008CntdwTimCntValuePortn_Type())
pm1008CntdwTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwTimCntValuePortn.setStatus(_A)
_Pm1008CntdwTimCntErrorPortn_Type=EkiOnOff
_Pm1008CntdwTimCntErrorPortn_Object=MibTableColumn
pm1008CntdwTimCntErrorPortn=_Pm1008CntdwTimCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,2,72,1,3),_Pm1008CntdwTimCntErrorPortn_Type())
pm1008CntdwTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwTimCntErrorPortn.setStatus(_A)
_Pm1008CntdwTimCntOverloadPortn_Type=EkiOnOff
_Pm1008CntdwTimCntOverloadPortn_Object=MibTableColumn
pm1008CntdwTimCntOverloadPortn=_Pm1008CntdwTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,2,72,1,4),_Pm1008CntdwTimCntOverloadPortn_Type())
pm1008CntdwTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdwTimCntOverloadPortn.setStatus(_A)
_Pm1008CntLine_ObjectIdentity=ObjectIdentity
pm1008CntLine=_Pm1008CntLine_ObjectIdentity((1,3,6,1,4,1,20044,3,4,3))
_Pm1008CntdfrmB1ErrCntTable_Object=MibTable
pm1008CntdfrmB1ErrCntTable=_Pm1008CntdfrmB1ErrCntTable_Object((1,3,6,1,4,1,20044,3,4,3,152))
if mibBuilder.loadTexts:pm1008CntdfrmB1ErrCntTable.setStatus(_A)
_Pm1008CntdfrmB1ErrCntEntry_Object=MibTableRow
pm1008CntdfrmB1ErrCntEntry=_Pm1008CntdfrmB1ErrCntEntry_Object((1,3,6,1,4,1,20044,3,4,3,152,1))
pm1008CntdfrmB1ErrCntEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:pm1008CntdfrmB1ErrCntEntry.setStatus(_A)
class _Pm1008CntdfrmB1ErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntdfrmB1ErrCntIndex_Type.__name__=_D
_Pm1008CntdfrmB1ErrCntIndex_Object=MibTableColumn
pm1008CntdfrmB1ErrCntIndex=_Pm1008CntdfrmB1ErrCntIndex_Object((1,3,6,1,4,1,20044,3,4,3,152,1,1),_Pm1008CntdfrmB1ErrCntIndex_Type())
pm1008CntdfrmB1ErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmB1ErrCntIndex.setStatus(_A)
_Pm1008CntdfrmB1ErrCntValuePortn_Type=Counter32
_Pm1008CntdfrmB1ErrCntValuePortn_Object=MibTableColumn
pm1008CntdfrmB1ErrCntValuePortn=_Pm1008CntdfrmB1ErrCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,3,152,1,2),_Pm1008CntdfrmB1ErrCntValuePortn_Type())
pm1008CntdfrmB1ErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmB1ErrCntValuePortn.setStatus(_A)
_Pm1008CntdfrmB1ErrCntErrorPortn_Type=EkiOnOff
_Pm1008CntdfrmB1ErrCntErrorPortn_Object=MibTableColumn
pm1008CntdfrmB1ErrCntErrorPortn=_Pm1008CntdfrmB1ErrCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,3,152,1,3),_Pm1008CntdfrmB1ErrCntErrorPortn_Type())
pm1008CntdfrmB1ErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmB1ErrCntErrorPortn.setStatus(_A)
_Pm1008CntdfrmB1ErrCntOverloadPortn_Type=EkiOnOff
_Pm1008CntdfrmB1ErrCntOverloadPortn_Object=MibTableColumn
pm1008CntdfrmB1ErrCntOverloadPortn=_Pm1008CntdfrmB1ErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,3,152,1,4),_Pm1008CntdfrmB1ErrCntOverloadPortn_Type())
pm1008CntdfrmB1ErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmB1ErrCntOverloadPortn.setStatus(_A)
_Pm1008CntdfrmTimCntTable_Object=MibTable
pm1008CntdfrmTimCntTable=_Pm1008CntdfrmTimCntTable_Object((1,3,6,1,4,1,20044,3,4,3,153))
if mibBuilder.loadTexts:pm1008CntdfrmTimCntTable.setStatus(_A)
_Pm1008CntdfrmTimCntEntry_Object=MibTableRow
pm1008CntdfrmTimCntEntry=_Pm1008CntdfrmTimCntEntry_Object((1,3,6,1,4,1,20044,3,4,3,153,1))
pm1008CntdfrmTimCntEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:pm1008CntdfrmTimCntEntry.setStatus(_A)
class _Pm1008CntdfrmTimCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntdfrmTimCntIndex_Type.__name__=_D
_Pm1008CntdfrmTimCntIndex_Object=MibTableColumn
pm1008CntdfrmTimCntIndex=_Pm1008CntdfrmTimCntIndex_Object((1,3,6,1,4,1,20044,3,4,3,153,1,1),_Pm1008CntdfrmTimCntIndex_Type())
pm1008CntdfrmTimCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmTimCntIndex.setStatus(_A)
_Pm1008CntdfrmTimCntValuePortn_Type=Counter32
_Pm1008CntdfrmTimCntValuePortn_Object=MibTableColumn
pm1008CntdfrmTimCntValuePortn=_Pm1008CntdfrmTimCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,3,153,1,2),_Pm1008CntdfrmTimCntValuePortn_Type())
pm1008CntdfrmTimCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmTimCntValuePortn.setStatus(_A)
_Pm1008CntdfrmTimCntErrorPortn_Type=EkiOnOff
_Pm1008CntdfrmTimCntErrorPortn_Object=MibTableColumn
pm1008CntdfrmTimCntErrorPortn=_Pm1008CntdfrmTimCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,3,153,1,3),_Pm1008CntdfrmTimCntErrorPortn_Type())
pm1008CntdfrmTimCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmTimCntErrorPortn.setStatus(_A)
_Pm1008CntdfrmTimCntOverloadPortn_Type=EkiOnOff
_Pm1008CntdfrmTimCntOverloadPortn_Object=MibTableColumn
pm1008CntdfrmTimCntOverloadPortn=_Pm1008CntdfrmTimCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,3,153,1,4),_Pm1008CntdfrmTimCntOverloadPortn_Type())
pm1008CntdfrmTimCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmTimCntOverloadPortn.setStatus(_A)
_Pm1008CntdfrmPrimLineErrCntTable_Object=MibTable
pm1008CntdfrmPrimLineErrCntTable=_Pm1008CntdfrmPrimLineErrCntTable_Object((1,3,6,1,4,1,20044,3,4,3,154))
if mibBuilder.loadTexts:pm1008CntdfrmPrimLineErrCntTable.setStatus(_A)
_Pm1008CntdfrmPrimLineErrCntEntry_Object=MibTableRow
pm1008CntdfrmPrimLineErrCntEntry=_Pm1008CntdfrmPrimLineErrCntEntry_Object((1,3,6,1,4,1,20044,3,4,3,154,1))
pm1008CntdfrmPrimLineErrCntEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:pm1008CntdfrmPrimLineErrCntEntry.setStatus(_A)
class _Pm1008CntdfrmPrimLineErrCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CntdfrmPrimLineErrCntIndex_Type.__name__=_D
_Pm1008CntdfrmPrimLineErrCntIndex_Object=MibTableColumn
pm1008CntdfrmPrimLineErrCntIndex=_Pm1008CntdfrmPrimLineErrCntIndex_Object((1,3,6,1,4,1,20044,3,4,3,154,1,1),_Pm1008CntdfrmPrimLineErrCntIndex_Type())
pm1008CntdfrmPrimLineErrCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmPrimLineErrCntIndex.setStatus(_A)
_Pm1008CntdfrmPrimLineErrCntValuePortn_Type=Counter32
_Pm1008CntdfrmPrimLineErrCntValuePortn_Object=MibTableColumn
pm1008CntdfrmPrimLineErrCntValuePortn=_Pm1008CntdfrmPrimLineErrCntValuePortn_Object((1,3,6,1,4,1,20044,3,4,3,154,1,2),_Pm1008CntdfrmPrimLineErrCntValuePortn_Type())
pm1008CntdfrmPrimLineErrCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmPrimLineErrCntValuePortn.setStatus(_A)
_Pm1008CntdfrmPrimLineErrCntErrorPortn_Type=EkiOnOff
_Pm1008CntdfrmPrimLineErrCntErrorPortn_Object=MibTableColumn
pm1008CntdfrmPrimLineErrCntErrorPortn=_Pm1008CntdfrmPrimLineErrCntErrorPortn_Object((1,3,6,1,4,1,20044,3,4,3,154,1,3),_Pm1008CntdfrmPrimLineErrCntErrorPortn_Type())
pm1008CntdfrmPrimLineErrCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmPrimLineErrCntErrorPortn.setStatus(_A)
_Pm1008CntdfrmPrimLineErrCntOverloadPortn_Type=EkiOnOff
_Pm1008CntdfrmPrimLineErrCntOverloadPortn_Object=MibTableColumn
pm1008CntdfrmPrimLineErrCntOverloadPortn=_Pm1008CntdfrmPrimLineErrCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,4,3,154,1,4),_Pm1008CntdfrmPrimLineErrCntOverloadPortn_Type())
pm1008CntdfrmPrimLineErrCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CntdfrmPrimLineErrCntOverloadPortn.setStatus(_A)
_Pm1008CntCountersReset_Type=EkiOnOff
_Pm1008CntCountersReset_Object=MibScalar
pm1008CntCountersReset=_Pm1008CntCountersReset_Object((1,3,6,1,4,1,20044,3,4,259),_Pm1008CntCountersReset_Type())
pm1008CntCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CntCountersReset.setStatus(_A)
_Pm1008CntCountersStop_Type=EkiOnOff
_Pm1008CntCountersStop_Object=MibScalar
pm1008CntCountersStop=_Pm1008CntCountersStop_Object((1,3,6,1,4,1,20044,3,4,260),_Pm1008CntCountersStop_Type())
pm1008CntCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CntCountersStop.setStatus(_A)
_Pm1008controlsWrite_ObjectIdentity=ObjectIdentity
pm1008controlsWrite=_Pm1008controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,3,6))
_Pm1008CtrlOther_ObjectIdentity=ObjectIdentity
pm1008CtrlOther=_Pm1008CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1))
_Pm1008CtrlconfMgnt1_ObjectIdentity=ObjectIdentity
pm1008CtrlconfMgnt1=_Pm1008CtrlconfMgnt1_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,1))
_Pm1008CtrlConf1Load1_Type=EkiOnOff
_Pm1008CtrlConf1Load1_Object=MibScalar
pm1008CtrlConf1Load1=_Pm1008CtrlConf1Load1_Object((1,3,6,1,4,1,20044,3,6,1,1,1),_Pm1008CtrlConf1Load1_Type())
pm1008CtrlConf1Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlConf1Load1.setStatus(_A)
_Pm1008CtrlConf2Load1_Type=EkiOnOff
_Pm1008CtrlConf2Load1_Object=MibScalar
pm1008CtrlConf2Load1=_Pm1008CtrlConf2Load1_Object((1,3,6,1,4,1,20044,3,6,1,1,2),_Pm1008CtrlConf2Load1_Type())
pm1008CtrlConf2Load1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlConf2Load1.setStatus(_A)
_Pm1008CtrlConf2Flash1_Type=EkiOnOff
_Pm1008CtrlConf2Flash1_Object=MibScalar
pm1008CtrlConf2Flash1=_Pm1008CtrlConf2Flash1_Object((1,3,6,1,4,1,20044,3,6,1,1,10),_Pm1008CtrlConf2Flash1_Type())
pm1008CtrlConf2Flash1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlConf2Flash1.setStatus(_A)
_Pm1008CtrlConf2Clear1_Type=EkiOnOff
_Pm1008CtrlConf2Clear1_Object=MibScalar
pm1008CtrlConf2Clear1=_Pm1008CtrlConf2Clear1_Object((1,3,6,1,4,1,20044,3,6,1,1,14),_Pm1008CtrlConf2Clear1_Type())
pm1008CtrlConf2Clear1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlConf2Clear1.setStatus(_A)
_Pm1008Ctrlsynth4_ObjectIdentity=ObjectIdentity
pm1008Ctrlsynth4=_Pm1008Ctrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,4))
_Pm1008CtrlCorrelatOn_Type=EkiOnOff
_Pm1008CtrlCorrelatOn_Object=MibScalar
pm1008CtrlCorrelatOn=_Pm1008CtrlCorrelatOn_Object((1,3,6,1,4,1,20044,3,6,1,4,1),_Pm1008CtrlCorrelatOn_Type())
pm1008CtrlCorrelatOn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlCorrelatOn.setStatus(_A)
_Pm1008CtrlCorrelatOff_Type=EkiOnOff
_Pm1008CtrlCorrelatOff_Object=MibScalar
pm1008CtrlCorrelatOff=_Pm1008CtrlCorrelatOff_Object((1,3,6,1,4,1,20044,3,6,1,4,2),_Pm1008CtrlCorrelatOff_Type())
pm1008CtrlCorrelatOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlCorrelatOff.setStatus(_A)
_Pm1008CtrlswMgnt_ObjectIdentity=ObjectIdentity
pm1008CtrlswMgnt=_Pm1008CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,5))
_Pm1008CtrlColdReset_Type=EkiOnOff
_Pm1008CtrlColdReset_Object=MibScalar
pm1008CtrlColdReset=_Pm1008CtrlColdReset_Object((1,3,6,1,4,1,20044,3,6,1,5,2),_Pm1008CtrlColdReset_Type())
pm1008CtrlColdReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlColdReset.setStatus(_A)
_Pm1008CtrlWarmReset_Type=EkiOnOff
_Pm1008CtrlWarmReset_Object=MibScalar
pm1008CtrlWarmReset=_Pm1008CtrlWarmReset_Object((1,3,6,1,4,1,20044,3,6,1,5,3),_Pm1008CtrlWarmReset_Type())
pm1008CtrlWarmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlWarmReset.setStatus(_A)
_Pm1008CtrlLoadSwBank1_Type=EkiOnOff
_Pm1008CtrlLoadSwBank1_Object=MibScalar
pm1008CtrlLoadSwBank1=_Pm1008CtrlLoadSwBank1_Object((1,3,6,1,4,1,20044,3,6,1,5,5),_Pm1008CtrlLoadSwBank1_Type())
pm1008CtrlLoadSwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLoadSwBank1.setStatus(_A)
_Pm1008CtrlLoadSwBank2_Type=EkiOnOff
_Pm1008CtrlLoadSwBank2_Object=MibScalar
pm1008CtrlLoadSwBank2=_Pm1008CtrlLoadSwBank2_Object((1,3,6,1,4,1,20044,3,6,1,5,6),_Pm1008CtrlLoadSwBank2_Type())
pm1008CtrlLoadSwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLoadSwBank2.setStatus(_A)
_Pm1008CtrlgwMgnt_ObjectIdentity=ObjectIdentity
pm1008CtrlgwMgnt=_Pm1008CtrlgwMgnt_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,6))
_Pm1008CtrlCurrentGwReset_Type=EkiOnOff
_Pm1008CtrlCurrentGwReset_Object=MibScalar
pm1008CtrlCurrentGwReset=_Pm1008CtrlCurrentGwReset_Object((1,3,6,1,4,1,20044,3,6,1,6,1),_Pm1008CtrlCurrentGwReset_Type())
pm1008CtrlCurrentGwReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlCurrentGwReset.setStatus(_A)
_Pm1008CtrlLoadGwBank1_Type=EkiOnOff
_Pm1008CtrlLoadGwBank1_Object=MibScalar
pm1008CtrlLoadGwBank1=_Pm1008CtrlLoadGwBank1_Object((1,3,6,1,4,1,20044,3,6,1,6,5),_Pm1008CtrlLoadGwBank1_Type())
pm1008CtrlLoadGwBank1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLoadGwBank1.setStatus(_A)
_Pm1008CtrlLoadGwBank2_Type=EkiOnOff
_Pm1008CtrlLoadGwBank2_Object=MibScalar
pm1008CtrlLoadGwBank2=_Pm1008CtrlLoadGwBank2_Object((1,3,6,1,4,1,20044,3,6,1,6,6),_Pm1008CtrlLoadGwBank2_Type())
pm1008CtrlLoadGwBank2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLoadGwBank2.setStatus(_A)
_Pm1008CtrlLoadGwBank3_Type=EkiOnOff
_Pm1008CtrlLoadGwBank3_Object=MibScalar
pm1008CtrlLoadGwBank3=_Pm1008CtrlLoadGwBank3_Object((1,3,6,1,4,1,20044,3,6,1,6,7),_Pm1008CtrlLoadGwBank3_Type())
pm1008CtrlLoadGwBank3.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLoadGwBank3.setStatus(_A)
_Pm1008CtrlLoadGwBank4_Type=EkiOnOff
_Pm1008CtrlLoadGwBank4_Object=MibScalar
pm1008CtrlLoadGwBank4=_Pm1008CtrlLoadGwBank4_Object((1,3,6,1,4,1,20044,3,6,1,6,8),_Pm1008CtrlLoadGwBank4_Type())
pm1008CtrlLoadGwBank4.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLoadGwBank4.setStatus(_A)
_Pm1008CtrlledTest_ObjectIdentity=ObjectIdentity
pm1008CtrlledTest=_Pm1008CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,192))
_Pm1008CtrlGreenLed_Type=EkiOnOff
_Pm1008CtrlGreenLed_Object=MibScalar
pm1008CtrlGreenLed=_Pm1008CtrlGreenLed_Object((1,3,6,1,4,1,20044,3,6,1,192,1),_Pm1008CtrlGreenLed_Type())
pm1008CtrlGreenLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlGreenLed.setStatus(_A)
_Pm1008CtrlRedLed_Type=EkiOnOff
_Pm1008CtrlRedLed_Object=MibScalar
pm1008CtrlRedLed=_Pm1008CtrlRedLed_Object((1,3,6,1,4,1,20044,3,6,1,192,2),_Pm1008CtrlRedLed_Type())
pm1008CtrlRedLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlRedLed.setStatus(_A)
_Pm1008CtrlLedOff_Type=EkiOnOff
_Pm1008CtrlLedOff_Object=MibScalar
pm1008CtrlLedOff=_Pm1008CtrlLedOff_Object((1,3,6,1,4,1,20044,3,6,1,192,3),_Pm1008CtrlLedOff_Type())
pm1008CtrlLedOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLedOff.setStatus(_A)
_Pm1008CtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm1008CtrlmoduleOosMode=_Pm1008CtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,193))
_Pm1008CtrlModuleOosMode_Type=EkiOnOff
_Pm1008CtrlModuleOosMode_Object=MibScalar
pm1008CtrlModuleOosMode=_Pm1008CtrlModuleOosMode_Object((1,3,6,1,4,1,20044,3,6,1,193,1),_Pm1008CtrlModuleOosMode_Type())
pm1008CtrlModuleOosMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlModuleOosMode.setStatus(_A)
_Pm1008CtrlmaintenanceMode_ObjectIdentity=ObjectIdentity
pm1008CtrlmaintenanceMode=_Pm1008CtrlmaintenanceMode_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,197))
_Pm1008CtrlMaintenanceMode_Type=EkiOnOff
_Pm1008CtrlMaintenanceMode_Object=MibScalar
pm1008CtrlMaintenanceMode=_Pm1008CtrlMaintenanceMode_Object((1,3,6,1,4,1,20044,3,6,1,197,1),_Pm1008CtrlMaintenanceMode_Type())
pm1008CtrlMaintenanceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlMaintenanceMode.setStatus(_A)
_Pm1008CtrldccEnable_ObjectIdentity=ObjectIdentity
pm1008CtrldccEnable=_Pm1008CtrldccEnable_ObjectIdentity((1,3,6,1,4,1,20044,3,6,1,198))
_Pm1008CtrlDccEnable_Type=EkiOnOff
_Pm1008CtrlDccEnable_Object=MibScalar
pm1008CtrlDccEnable=_Pm1008CtrlDccEnable_Object((1,3,6,1,4,1,20044,3,6,1,198,1),_Pm1008CtrlDccEnable_Type())
pm1008CtrlDccEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlDccEnable.setStatus(_A)
_Pm1008CtrlClient_ObjectIdentity=ObjectIdentity
pm1008CtrlClient=_Pm1008CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,3,6,2))
_Pm1008CtrlaccessLoopTable_Object=MibTable
pm1008CtrlaccessLoopTable=_Pm1008CtrlaccessLoopTable_Object((1,3,6,1,4,1,20044,3,6,2,16))
if mibBuilder.loadTexts:pm1008CtrlaccessLoopTable.setStatus(_A)
_Pm1008CtrlaccessLoopEntry_Object=MibTableRow
pm1008CtrlaccessLoopEntry=_Pm1008CtrlaccessLoopEntry_Object((1,3,6,1,4,1,20044,3,6,2,16,1))
pm1008CtrlaccessLoopEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:pm1008CtrlaccessLoopEntry.setStatus(_A)
class _Pm1008CtrlaccessLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlaccessLoopIndex_Type.__name__=_D
_Pm1008CtrlaccessLoopIndex_Object=MibTableColumn
pm1008CtrlaccessLoopIndex=_Pm1008CtrlaccessLoopIndex_Object((1,3,6,1,4,1,20044,3,6,2,16,1,1),_Pm1008CtrlaccessLoopIndex_Type())
pm1008CtrlaccessLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlaccessLoopIndex.setStatus(_A)
_Pm1008CtrlaccessLoopPortn_Type=EkiState
_Pm1008CtrlaccessLoopPortn_Object=MibTableColumn
pm1008CtrlaccessLoopPortn=_Pm1008CtrlaccessLoopPortn_Object((1,3,6,1,4,1,20044,3,6,2,16,1,2),_Pm1008CtrlaccessLoopPortn_Type())
pm1008CtrlaccessLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlaccessLoopPortn.setStatus(_A)
_Pm1008CtrlportOosModeTable_Object=MibTable
pm1008CtrlportOosModeTable=_Pm1008CtrlportOosModeTable_Object((1,3,6,1,4,1,20044,3,6,2,18))
if mibBuilder.loadTexts:pm1008CtrlportOosModeTable.setStatus(_A)
_Pm1008CtrlportOosModeEntry_Object=MibTableRow
pm1008CtrlportOosModeEntry=_Pm1008CtrlportOosModeEntry_Object((1,3,6,1,4,1,20044,3,6,2,18,1))
pm1008CtrlportOosModeEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:pm1008CtrlportOosModeEntry.setStatus(_A)
class _Pm1008CtrlportOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlportOosModeIndex_Type.__name__=_D
_Pm1008CtrlportOosModeIndex_Object=MibTableColumn
pm1008CtrlportOosModeIndex=_Pm1008CtrlportOosModeIndex_Object((1,3,6,1,4,1,20044,3,6,2,18,1,1),_Pm1008CtrlportOosModeIndex_Type())
pm1008CtrlportOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlportOosModeIndex.setStatus(_A)
_Pm1008CtrlportOosModePortn_Type=EkiState
_Pm1008CtrlportOosModePortn_Object=MibTableColumn
pm1008CtrlportOosModePortn=_Pm1008CtrlportOosModePortn_Object((1,3,6,1,4,1,20044,3,6,2,18,1,2),_Pm1008CtrlportOosModePortn_Type())
pm1008CtrlportOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlportOosModePortn.setStatus(_A)
_Pm1008CtrlsfpOnCtrlTable_Object=MibTable
pm1008CtrlsfpOnCtrlTable=_Pm1008CtrlsfpOnCtrlTable_Object((1,3,6,1,4,1,20044,3,6,2,19))
if mibBuilder.loadTexts:pm1008CtrlsfpOnCtrlTable.setStatus(_A)
_Pm1008CtrlsfpOnCtrlEntry_Object=MibTableRow
pm1008CtrlsfpOnCtrlEntry=_Pm1008CtrlsfpOnCtrlEntry_Object((1,3,6,1,4,1,20044,3,6,2,19,1))
pm1008CtrlsfpOnCtrlEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:pm1008CtrlsfpOnCtrlEntry.setStatus(_A)
class _Pm1008CtrlsfpOnCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlsfpOnCtrlIndex_Type.__name__=_D
_Pm1008CtrlsfpOnCtrlIndex_Object=MibTableColumn
pm1008CtrlsfpOnCtrlIndex=_Pm1008CtrlsfpOnCtrlIndex_Object((1,3,6,1,4,1,20044,3,6,2,19,1,1),_Pm1008CtrlsfpOnCtrlIndex_Type())
pm1008CtrlsfpOnCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlsfpOnCtrlIndex.setStatus(_A)
_Pm1008CtrlsfpOnCtrlPortn_Type=EkiState
_Pm1008CtrlsfpOnCtrlPortn_Object=MibTableColumn
pm1008CtrlsfpOnCtrlPortn=_Pm1008CtrlsfpOnCtrlPortn_Object((1,3,6,1,4,1,20044,3,6,2,19,1,2),_Pm1008CtrlsfpOnCtrlPortn_Type())
pm1008CtrlsfpOnCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlsfpOnCtrlPortn.setStatus(_A)
_Pm1008CtrlsfpOffCtrlTable_Object=MibTable
pm1008CtrlsfpOffCtrlTable=_Pm1008CtrlsfpOffCtrlTable_Object((1,3,6,1,4,1,20044,3,6,2,20))
if mibBuilder.loadTexts:pm1008CtrlsfpOffCtrlTable.setStatus(_A)
_Pm1008CtrlsfpOffCtrlEntry_Object=MibTableRow
pm1008CtrlsfpOffCtrlEntry=_Pm1008CtrlsfpOffCtrlEntry_Object((1,3,6,1,4,1,20044,3,6,2,20,1))
pm1008CtrlsfpOffCtrlEntry.setIndexNames((0,_C,_AE))
if mibBuilder.loadTexts:pm1008CtrlsfpOffCtrlEntry.setStatus(_A)
class _Pm1008CtrlsfpOffCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlsfpOffCtrlIndex_Type.__name__=_D
_Pm1008CtrlsfpOffCtrlIndex_Object=MibTableColumn
pm1008CtrlsfpOffCtrlIndex=_Pm1008CtrlsfpOffCtrlIndex_Object((1,3,6,1,4,1,20044,3,6,2,20,1,1),_Pm1008CtrlsfpOffCtrlIndex_Type())
pm1008CtrlsfpOffCtrlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlsfpOffCtrlIndex.setStatus(_A)
_Pm1008CtrlsfpOffCtrlPortn_Type=EkiState
_Pm1008CtrlsfpOffCtrlPortn_Object=MibTableColumn
pm1008CtrlsfpOffCtrlPortn=_Pm1008CtrlsfpOffCtrlPortn_Object((1,3,6,1,4,1,20044,3,6,2,20,1,2),_Pm1008CtrlsfpOffCtrlPortn_Type())
pm1008CtrlsfpOffCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlsfpOffCtrlPortn.setStatus(_A)
_Pm1008CtrlcsfUpInsTable_Object=MibTable
pm1008CtrlcsfUpInsTable=_Pm1008CtrlcsfUpInsTable_Object((1,3,6,1,4,1,20044,3,6,2,21))
if mibBuilder.loadTexts:pm1008CtrlcsfUpInsTable.setStatus(_A)
_Pm1008CtrlcsfUpInsEntry_Object=MibTableRow
pm1008CtrlcsfUpInsEntry=_Pm1008CtrlcsfUpInsEntry_Object((1,3,6,1,4,1,20044,3,6,2,21,1))
pm1008CtrlcsfUpInsEntry.setIndexNames((0,_C,_AF))
if mibBuilder.loadTexts:pm1008CtrlcsfUpInsEntry.setStatus(_A)
class _Pm1008CtrlcsfUpInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlcsfUpInsIndex_Type.__name__=_D
_Pm1008CtrlcsfUpInsIndex_Object=MibTableColumn
pm1008CtrlcsfUpInsIndex=_Pm1008CtrlcsfUpInsIndex_Object((1,3,6,1,4,1,20044,3,6,2,21,1,1),_Pm1008CtrlcsfUpInsIndex_Type())
pm1008CtrlcsfUpInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlcsfUpInsIndex.setStatus(_A)
_Pm1008CtrlcsfUpInsPortn_Type=EkiState
_Pm1008CtrlcsfUpInsPortn_Object=MibTableColumn
pm1008CtrlcsfUpInsPortn=_Pm1008CtrlcsfUpInsPortn_Object((1,3,6,1,4,1,20044,3,6,2,21,1,2),_Pm1008CtrlcsfUpInsPortn_Type())
pm1008CtrlcsfUpInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlcsfUpInsPortn.setStatus(_A)
_Pm1008CtrlcaisDwInsTable_Object=MibTable
pm1008CtrlcaisDwInsTable=_Pm1008CtrlcaisDwInsTable_Object((1,3,6,1,4,1,20044,3,6,2,22))
if mibBuilder.loadTexts:pm1008CtrlcaisDwInsTable.setStatus(_A)
_Pm1008CtrlcaisDwInsEntry_Object=MibTableRow
pm1008CtrlcaisDwInsEntry=_Pm1008CtrlcaisDwInsEntry_Object((1,3,6,1,4,1,20044,3,6,2,22,1))
pm1008CtrlcaisDwInsEntry.setIndexNames((0,_C,_AG))
if mibBuilder.loadTexts:pm1008CtrlcaisDwInsEntry.setStatus(_A)
class _Pm1008CtrlcaisDwInsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlcaisDwInsIndex_Type.__name__=_D
_Pm1008CtrlcaisDwInsIndex_Object=MibTableColumn
pm1008CtrlcaisDwInsIndex=_Pm1008CtrlcaisDwInsIndex_Object((1,3,6,1,4,1,20044,3,6,2,22,1,1),_Pm1008CtrlcaisDwInsIndex_Type())
pm1008CtrlcaisDwInsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlcaisDwInsIndex.setStatus(_A)
_Pm1008CtrlcaisDwInsPortn_Type=EkiState
_Pm1008CtrlcaisDwInsPortn_Object=MibTableColumn
pm1008CtrlcaisDwInsPortn=_Pm1008CtrlcaisDwInsPortn_Object((1,3,6,1,4,1,20044,3,6,2,22,1,2),_Pm1008CtrlcaisDwInsPortn_Type())
pm1008CtrlcaisDwInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlcaisDwInsPortn.setStatus(_A)
_Pm1008CtrlflowControlTable_Object=MibTable
pm1008CtrlflowControlTable=_Pm1008CtrlflowControlTable_Object((1,3,6,1,4,1,20044,3,6,2,23))
if mibBuilder.loadTexts:pm1008CtrlflowControlTable.setStatus(_A)
_Pm1008CtrlflowControlEntry_Object=MibTableRow
pm1008CtrlflowControlEntry=_Pm1008CtrlflowControlEntry_Object((1,3,6,1,4,1,20044,3,6,2,23,1))
pm1008CtrlflowControlEntry.setIndexNames((0,_C,_AH))
if mibBuilder.loadTexts:pm1008CtrlflowControlEntry.setStatus(_A)
class _Pm1008CtrlflowControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlflowControlIndex_Type.__name__=_D
_Pm1008CtrlflowControlIndex_Object=MibTableColumn
pm1008CtrlflowControlIndex=_Pm1008CtrlflowControlIndex_Object((1,3,6,1,4,1,20044,3,6,2,23,1,1),_Pm1008CtrlflowControlIndex_Type())
pm1008CtrlflowControlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlflowControlIndex.setStatus(_A)
_Pm1008CtrlflowControlPortn_Type=EkiState
_Pm1008CtrlflowControlPortn_Object=MibTableColumn
pm1008CtrlflowControlPortn=_Pm1008CtrlflowControlPortn_Object((1,3,6,1,4,1,20044,3,6,2,23,1,2),_Pm1008CtrlflowControlPortn_Type())
pm1008CtrlflowControlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlflowControlPortn.setStatus(_A)
_Pm1008CtrlclientAccessTermLoopTable_Object=MibTable
pm1008CtrlclientAccessTermLoopTable=_Pm1008CtrlclientAccessTermLoopTable_Object((1,3,6,1,4,1,20044,3,6,2,26))
if mibBuilder.loadTexts:pm1008CtrlclientAccessTermLoopTable.setStatus(_A)
_Pm1008CtrlclientAccessTermLoopEntry_Object=MibTableRow
pm1008CtrlclientAccessTermLoopEntry=_Pm1008CtrlclientAccessTermLoopEntry_Object((1,3,6,1,4,1,20044,3,6,2,26,1))
pm1008CtrlclientAccessTermLoopEntry.setIndexNames((0,_C,_AI))
if mibBuilder.loadTexts:pm1008CtrlclientAccessTermLoopEntry.setStatus(_A)
class _Pm1008CtrlclientAccessTermLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlclientAccessTermLoopIndex_Type.__name__=_D
_Pm1008CtrlclientAccessTermLoopIndex_Object=MibTableColumn
pm1008CtrlclientAccessTermLoopIndex=_Pm1008CtrlclientAccessTermLoopIndex_Object((1,3,6,1,4,1,20044,3,6,2,26,1,1),_Pm1008CtrlclientAccessTermLoopIndex_Type())
pm1008CtrlclientAccessTermLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlclientAccessTermLoopIndex.setStatus(_A)
_Pm1008CtrlclientAccessTermLoopPortn_Type=EkiState
_Pm1008CtrlclientAccessTermLoopPortn_Object=MibTableColumn
pm1008CtrlclientAccessTermLoopPortn=_Pm1008CtrlclientAccessTermLoopPortn_Object((1,3,6,1,4,1,20044,3,6,2,26,1,2),_Pm1008CtrlclientAccessTermLoopPortn_Type())
pm1008CtrlclientAccessTermLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlclientAccessTermLoopPortn.setStatus(_A)
_Pm1008CtrlselectMultirateTable_Object=MibTable
pm1008CtrlselectMultirateTable=_Pm1008CtrlselectMultirateTable_Object((1,3,6,1,4,1,20044,3,6,2,42))
if mibBuilder.loadTexts:pm1008CtrlselectMultirateTable.setStatus(_A)
_Pm1008CtrlselectMultirateEntry_Object=MibTableRow
pm1008CtrlselectMultirateEntry=_Pm1008CtrlselectMultirateEntry_Object((1,3,6,1,4,1,20044,3,6,2,42,1))
pm1008CtrlselectMultirateEntry.setIndexNames((0,_C,_AJ))
if mibBuilder.loadTexts:pm1008CtrlselectMultirateEntry.setStatus(_A)
class _Pm1008CtrlselectMultirateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlselectMultirateIndex_Type.__name__=_D
_Pm1008CtrlselectMultirateIndex_Object=MibTableColumn
pm1008CtrlselectMultirateIndex=_Pm1008CtrlselectMultirateIndex_Object((1,3,6,1,4,1,20044,3,6,2,42,1,1),_Pm1008CtrlselectMultirateIndex_Type())
pm1008CtrlselectMultirateIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlselectMultirateIndex.setStatus(_A)
_Pm1008CtrlselectMultiratePortn_Type=Pm1008MultiRate
_Pm1008CtrlselectMultiratePortn_Object=MibTableColumn
pm1008CtrlselectMultiratePortn=_Pm1008CtrlselectMultiratePortn_Object((1,3,6,1,4,1,20044,3,6,2,42,1,2),_Pm1008CtrlselectMultiratePortn_Type())
pm1008CtrlselectMultiratePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlselectMultiratePortn.setStatus(_A)
_Pm1008CtrlprotocolTable_Object=MibTable
pm1008CtrlprotocolTable=_Pm1008CtrlprotocolTable_Object((1,3,6,1,4,1,20044,3,6,2,48))
if mibBuilder.loadTexts:pm1008CtrlprotocolTable.setStatus(_A)
_Pm1008CtrlprotocolEntry_Object=MibTableRow
pm1008CtrlprotocolEntry=_Pm1008CtrlprotocolEntry_Object((1,3,6,1,4,1,20044,3,6,2,48,1))
pm1008CtrlprotocolEntry.setIndexNames((0,_C,_AK))
if mibBuilder.loadTexts:pm1008CtrlprotocolEntry.setStatus(_A)
class _Pm1008CtrlprotocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlprotocolIndex_Type.__name__=_D
_Pm1008CtrlprotocolIndex_Object=MibTableColumn
pm1008CtrlprotocolIndex=_Pm1008CtrlprotocolIndex_Object((1,3,6,1,4,1,20044,3,6,2,48,1,1),_Pm1008CtrlprotocolIndex_Type())
pm1008CtrlprotocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlprotocolIndex.setStatus(_A)
_Pm1008CtrlprotocolPortn_Type=EkiProtocol
_Pm1008CtrlprotocolPortn_Object=MibTableColumn
pm1008CtrlprotocolPortn=_Pm1008CtrlprotocolPortn_Object((1,3,6,1,4,1,20044,3,6,2,48,1,2),_Pm1008CtrlprotocolPortn_Type())
pm1008CtrlprotocolPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlprotocolPortn.setStatus(_A)
_Pm1008CtrlLine_ObjectIdentity=ObjectIdentity
pm1008CtrlLine=_Pm1008CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,3,6,3))
_Pm1008CtrlcommAccessLoop_ObjectIdentity=ObjectIdentity
pm1008CtrlcommAccessLoop=_Pm1008CtrlcommAccessLoop_ObjectIdentity((1,3,6,1,4,1,20044,3,6,3,64))
_Pm1008CtrlCommAccessloop_Type=EkiOnOff
_Pm1008CtrlCommAccessloop_Object=MibScalar
pm1008CtrlCommAccessloop=_Pm1008CtrlCommAccessloop_Object((1,3,6,1,4,1,20044,3,6,3,64,1),_Pm1008CtrlCommAccessloop_Type())
pm1008CtrlCommAccessloop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlCommAccessloop.setStatus(_G)
_Pm1008CtrllineLoop_ObjectIdentity=ObjectIdentity
pm1008CtrllineLoop=_Pm1008CtrllineLoop_ObjectIdentity((1,3,6,1,4,1,20044,3,6,3,66))
_Pm1008CtrlLineLoop_Type=EkiOnOff
_Pm1008CtrlLineLoop_Object=MibScalar
pm1008CtrlLineLoop=_Pm1008CtrlLineLoop_Object((1,3,6,1,4,1,20044,3,6,3,66,1),_Pm1008CtrlLineLoop_Type())
pm1008CtrlLineLoop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLineLoop.setStatus(_G)
_Pm1008CtrlmsAis_ObjectIdentity=ObjectIdentity
pm1008CtrlmsAis=_Pm1008CtrlmsAis_ObjectIdentity((1,3,6,1,4,1,20044,3,6,3,67))
_Pm1008CtrlMsAis_Type=EkiOnOff
_Pm1008CtrlMsAis_Object=MibScalar
pm1008CtrlMsAis=_Pm1008CtrlMsAis_Object((1,3,6,1,4,1,20044,3,6,3,67,1),_Pm1008CtrlMsAis_Type())
pm1008CtrlMsAis.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlMsAis.setStatus(_A)
_Pm1008CtrlfecDisableTable_Object=MibTable
pm1008CtrlfecDisableTable=_Pm1008CtrlfecDisableTable_Object((1,3,6,1,4,1,20044,3,6,3,69))
if mibBuilder.loadTexts:pm1008CtrlfecDisableTable.setStatus(_A)
_Pm1008CtrlfecDisableEntry_Object=MibTableRow
pm1008CtrlfecDisableEntry=_Pm1008CtrlfecDisableEntry_Object((1,3,6,1,4,1,20044,3,6,3,69,1))
pm1008CtrlfecDisableEntry.setIndexNames((0,_C,_AL))
if mibBuilder.loadTexts:pm1008CtrlfecDisableEntry.setStatus(_A)
class _Pm1008CtrlfecDisableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlfecDisableIndex_Type.__name__=_D
_Pm1008CtrlfecDisableIndex_Object=MibTableColumn
pm1008CtrlfecDisableIndex=_Pm1008CtrlfecDisableIndex_Object((1,3,6,1,4,1,20044,3,6,3,69,1,1),_Pm1008CtrlfecDisableIndex_Type())
pm1008CtrlfecDisableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlfecDisableIndex.setStatus(_A)
_Pm1008CtrlfecDisablePortn_Type=EkiState
_Pm1008CtrlfecDisablePortn_Object=MibTableColumn
pm1008CtrlfecDisablePortn=_Pm1008CtrlfecDisablePortn_Object((1,3,6,1,4,1,20044,3,6,3,69,1,2),_Pm1008CtrlfecDisablePortn_Type())
pm1008CtrlfecDisablePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlfecDisablePortn.setStatus(_A)
_Pm1008CtrlProtMgnt_ObjectIdentity=ObjectIdentity
pm1008CtrlProtMgnt=_Pm1008CtrlProtMgnt_ObjectIdentity((1,3,6,1,4,1,20044,3,6,3,73))
class _Pm1008CtrlLineNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pm1008CtrlLineNumber_Type.__name__=_F
_Pm1008CtrlLineNumber_Object=MibScalar
pm1008CtrlLineNumber=_Pm1008CtrlLineNumber_Object((1,3,6,1,4,1,20044,3,6,3,73,1),_Pm1008CtrlLineNumber_Type())
pm1008CtrlLineNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlLineNumber.setStatus(_A)
_Pm1008CtrlProtMode_Type=EkiMode
_Pm1008CtrlProtMode_Object=MibScalar
pm1008CtrlProtMode=_Pm1008CtrlProtMode_Object((1,3,6,1,4,1,20044,3,6,3,73,2),_Pm1008CtrlProtMode_Type())
pm1008CtrlProtMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlProtMode.setStatus(_A)
_Pm1008CtrllineOosModeTable_Object=MibTable
pm1008CtrllineOosModeTable=_Pm1008CtrllineOosModeTable_Object((1,3,6,1,4,1,20044,3,6,3,74))
if mibBuilder.loadTexts:pm1008CtrllineOosModeTable.setStatus(_A)
_Pm1008CtrllineOosModeEntry_Object=MibTableRow
pm1008CtrllineOosModeEntry=_Pm1008CtrllineOosModeEntry_Object((1,3,6,1,4,1,20044,3,6,3,74,1))
pm1008CtrllineOosModeEntry.setIndexNames((0,_C,_AM))
if mibBuilder.loadTexts:pm1008CtrllineOosModeEntry.setStatus(_A)
class _Pm1008CtrllineOosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrllineOosModeIndex_Type.__name__=_D
_Pm1008CtrllineOosModeIndex_Object=MibTableColumn
pm1008CtrllineOosModeIndex=_Pm1008CtrllineOosModeIndex_Object((1,3,6,1,4,1,20044,3,6,3,74,1,1),_Pm1008CtrllineOosModeIndex_Type())
pm1008CtrllineOosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrllineOosModeIndex.setStatus(_A)
_Pm1008CtrllineOosModePortn_Type=EkiState
_Pm1008CtrllineOosModePortn_Object=MibTableColumn
pm1008CtrllineOosModePortn=_Pm1008CtrllineOosModePortn_Object((1,3,6,1,4,1,20044,3,6,3,74,1,2),_Pm1008CtrllineOosModePortn_Type())
pm1008CtrllineOosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrllineOosModePortn.setStatus(_A)
_Pm1008CtrlxfpOnoffTable_Object=MibTable
pm1008CtrlxfpOnoffTable=_Pm1008CtrlxfpOnoffTable_Object((1,3,6,1,4,1,20044,3,6,3,208))
if mibBuilder.loadTexts:pm1008CtrlxfpOnoffTable.setStatus(_A)
_Pm1008CtrlxfpOnoffEntry_Object=MibTableRow
pm1008CtrlxfpOnoffEntry=_Pm1008CtrlxfpOnoffEntry_Object((1,3,6,1,4,1,20044,3,6,3,208,1))
pm1008CtrlxfpOnoffEntry.setIndexNames((0,_C,_AN))
if mibBuilder.loadTexts:pm1008CtrlxfpOnoffEntry.setStatus(_A)
class _Pm1008CtrlxfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlxfpOnoffIndex_Type.__name__=_D
_Pm1008CtrlxfpOnoffIndex_Object=MibTableColumn
pm1008CtrlxfpOnoffIndex=_Pm1008CtrlxfpOnoffIndex_Object((1,3,6,1,4,1,20044,3,6,3,208,1,1),_Pm1008CtrlxfpOnoffIndex_Type())
pm1008CtrlxfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlxfpOnoffIndex.setStatus(_A)
_Pm1008CtrlxfpOnoffPortn_Type=EkiState
_Pm1008CtrlxfpOnoffPortn_Object=MibTableColumn
pm1008CtrlxfpOnoffPortn=_Pm1008CtrlxfpOnoffPortn_Object((1,3,6,1,4,1,20044,3,6,3,208,1,2),_Pm1008CtrlxfpOnoffPortn_Type())
pm1008CtrlxfpOnoffPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlxfpOnoffPortn.setStatus(_A)
_Pm1008CtrlxfpLineLoopTable_Object=MibTable
pm1008CtrlxfpLineLoopTable=_Pm1008CtrlxfpLineLoopTable_Object((1,3,6,1,4,1,20044,3,6,3,209))
if mibBuilder.loadTexts:pm1008CtrlxfpLineLoopTable.setStatus(_A)
_Pm1008CtrlxfpLineLoopEntry_Object=MibTableRow
pm1008CtrlxfpLineLoopEntry=_Pm1008CtrlxfpLineLoopEntry_Object((1,3,6,1,4,1,20044,3,6,3,209,1))
pm1008CtrlxfpLineLoopEntry.setIndexNames((0,_C,_AO))
if mibBuilder.loadTexts:pm1008CtrlxfpLineLoopEntry.setStatus(_A)
class _Pm1008CtrlxfpLineLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlxfpLineLoopIndex_Type.__name__=_D
_Pm1008CtrlxfpLineLoopIndex_Object=MibTableColumn
pm1008CtrlxfpLineLoopIndex=_Pm1008CtrlxfpLineLoopIndex_Object((1,3,6,1,4,1,20044,3,6,3,209,1,1),_Pm1008CtrlxfpLineLoopIndex_Type())
pm1008CtrlxfpLineLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlxfpLineLoopIndex.setStatus(_A)
_Pm1008CtrlxfpLineLoopPortn_Type=EkiState
_Pm1008CtrlxfpLineLoopPortn_Object=MibTableColumn
pm1008CtrlxfpLineLoopPortn=_Pm1008CtrlxfpLineLoopPortn_Object((1,3,6,1,4,1,20044,3,6,3,209,1,2),_Pm1008CtrlxfpLineLoopPortn_Type())
pm1008CtrlxfpLineLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlxfpLineLoopPortn.setStatus(_A)
_Pm1008CtrlxfpXfiLoopTable_Object=MibTable
pm1008CtrlxfpXfiLoopTable=_Pm1008CtrlxfpXfiLoopTable_Object((1,3,6,1,4,1,20044,3,6,3,210))
if mibBuilder.loadTexts:pm1008CtrlxfpXfiLoopTable.setStatus(_A)
_Pm1008CtrlxfpXfiLoopEntry_Object=MibTableRow
pm1008CtrlxfpXfiLoopEntry=_Pm1008CtrlxfpXfiLoopEntry_Object((1,3,6,1,4,1,20044,3,6,3,210,1))
pm1008CtrlxfpXfiLoopEntry.setIndexNames((0,_C,_AP))
if mibBuilder.loadTexts:pm1008CtrlxfpXfiLoopEntry.setStatus(_A)
class _Pm1008CtrlxfpXfiLoopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrlxfpXfiLoopIndex_Type.__name__=_D
_Pm1008CtrlxfpXfiLoopIndex_Object=MibTableColumn
pm1008CtrlxfpXfiLoopIndex=_Pm1008CtrlxfpXfiLoopIndex_Object((1,3,6,1,4,1,20044,3,6,3,210,1,1),_Pm1008CtrlxfpXfiLoopIndex_Type())
pm1008CtrlxfpXfiLoopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrlxfpXfiLoopIndex.setStatus(_A)
_Pm1008CtrlxfpXfiLoopPortn_Type=EkiState
_Pm1008CtrlxfpXfiLoopPortn_Object=MibTableColumn
pm1008CtrlxfpXfiLoopPortn=_Pm1008CtrlxfpXfiLoopPortn_Object((1,3,6,1,4,1,20044,3,6,3,210,1,2),_Pm1008CtrlxfpXfiLoopPortn_Type())
pm1008CtrlxfpXfiLoopPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrlxfpXfiLoopPortn.setStatus(_A)
_Pm1008CtrllineTunableChannelTable_Object=MibTable
pm1008CtrllineTunableChannelTable=_Pm1008CtrllineTunableChannelTable_Object((1,3,6,1,4,1,20044,3,6,3,212))
if mibBuilder.loadTexts:pm1008CtrllineTunableChannelTable.setStatus(_A)
_Pm1008CtrllineTunableChannelEntry_Object=MibTableRow
pm1008CtrllineTunableChannelEntry=_Pm1008CtrllineTunableChannelEntry_Object((1,3,6,1,4,1,20044,3,6,3,212,1))
pm1008CtrllineTunableChannelEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:pm1008CtrllineTunableChannelEntry.setStatus(_A)
class _Pm1008CtrllineTunableChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrllineTunableChannelIndex_Type.__name__=_D
_Pm1008CtrllineTunableChannelIndex_Object=MibTableColumn
pm1008CtrllineTunableChannelIndex=_Pm1008CtrllineTunableChannelIndex_Object((1,3,6,1,4,1,20044,3,6,3,212,1,1),_Pm1008CtrllineTunableChannelIndex_Type())
pm1008CtrllineTunableChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrllineTunableChannelIndex.setStatus(_A)
_Pm1008CtrllineTunableChannelPortn_Type=Pm1008OtxChannel
_Pm1008CtrllineTunableChannelPortn_Object=MibTableColumn
pm1008CtrllineTunableChannelPortn=_Pm1008CtrllineTunableChannelPortn_Object((1,3,6,1,4,1,20044,3,6,3,212,1,2),_Pm1008CtrllineTunableChannelPortn_Type())
pm1008CtrllineTunableChannelPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrllineTunableChannelPortn.setStatus(_A)
_Pm1008CtrllinePhotodiodeModeTable_Object=MibTable
pm1008CtrllinePhotodiodeModeTable=_Pm1008CtrllinePhotodiodeModeTable_Object((1,3,6,1,4,1,20044,3,6,3,213))
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeModeTable.setStatus(_A)
_Pm1008CtrllinePhotodiodeModeEntry_Object=MibTableRow
pm1008CtrllinePhotodiodeModeEntry=_Pm1008CtrllinePhotodiodeModeEntry_Object((1,3,6,1,4,1,20044,3,6,3,213,1))
pm1008CtrllinePhotodiodeModeEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeModeEntry.setStatus(_A)
class _Pm1008CtrllinePhotodiodeModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrllinePhotodiodeModeIndex_Type.__name__=_D
_Pm1008CtrllinePhotodiodeModeIndex_Object=MibTableColumn
pm1008CtrllinePhotodiodeModeIndex=_Pm1008CtrllinePhotodiodeModeIndex_Object((1,3,6,1,4,1,20044,3,6,3,213,1,1),_Pm1008CtrllinePhotodiodeModeIndex_Type())
pm1008CtrllinePhotodiodeModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeModeIndex.setStatus(_A)
_Pm1008CtrllinePhotodiodeModePortn_Type=Pm1008OtxMode
_Pm1008CtrllinePhotodiodeModePortn_Object=MibTableColumn
pm1008CtrllinePhotodiodeModePortn=_Pm1008CtrllinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,3,6,3,213,1,2),_Pm1008CtrllinePhotodiodeModePortn_Type())
pm1008CtrllinePhotodiodeModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeModePortn.setStatus(_A)
_Pm1008CtrllinePhotodiodeValueTable_Object=MibTable
pm1008CtrllinePhotodiodeValueTable=_Pm1008CtrllinePhotodiodeValueTable_Object((1,3,6,1,4,1,20044,3,6,3,214))
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeValueTable.setStatus(_A)
_Pm1008CtrllinePhotodiodeValueEntry_Object=MibTableRow
pm1008CtrllinePhotodiodeValueEntry=_Pm1008CtrllinePhotodiodeValueEntry_Object((1,3,6,1,4,1,20044,3,6,3,214,1))
pm1008CtrllinePhotodiodeValueEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeValueEntry.setStatus(_A)
class _Pm1008CtrllinePhotodiodeValueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrllinePhotodiodeValueIndex_Type.__name__=_D
_Pm1008CtrllinePhotodiodeValueIndex_Object=MibTableColumn
pm1008CtrllinePhotodiodeValueIndex=_Pm1008CtrllinePhotodiodeValueIndex_Object((1,3,6,1,4,1,20044,3,6,3,214,1,1),_Pm1008CtrllinePhotodiodeValueIndex_Type())
pm1008CtrllinePhotodiodeValueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeValueIndex.setStatus(_A)
_Pm1008CtrllinePhotodiodeValuePortn_Type=Pm1008AdjustValue
_Pm1008CtrllinePhotodiodeValuePortn_Object=MibTableColumn
pm1008CtrllinePhotodiodeValuePortn=_Pm1008CtrllinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,3,6,3,214,1,2),_Pm1008CtrllinePhotodiodeValuePortn_Type())
pm1008CtrllinePhotodiodeValuePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrllinePhotodiodeValuePortn.setStatus(_A)
_Pm1008CtrllinePowerLaserTable_Object=MibTable
pm1008CtrllinePowerLaserTable=_Pm1008CtrllinePowerLaserTable_Object((1,3,6,1,4,1,20044,3,6,3,215))
if mibBuilder.loadTexts:pm1008CtrllinePowerLaserTable.setStatus(_A)
_Pm1008CtrllinePowerLaserEntry_Object=MibTableRow
pm1008CtrllinePowerLaserEntry=_Pm1008CtrllinePowerLaserEntry_Object((1,3,6,1,4,1,20044,3,6,3,215,1))
pm1008CtrllinePowerLaserEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:pm1008CtrllinePowerLaserEntry.setStatus(_A)
class _Pm1008CtrllinePowerLaserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CtrllinePowerLaserIndex_Type.__name__=_D
_Pm1008CtrllinePowerLaserIndex_Object=MibTableColumn
pm1008CtrllinePowerLaserIndex=_Pm1008CtrllinePowerLaserIndex_Object((1,3,6,1,4,1,20044,3,6,3,215,1,1),_Pm1008CtrllinePowerLaserIndex_Type())
pm1008CtrllinePowerLaserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CtrllinePowerLaserIndex.setStatus(_A)
class _Pm1008CtrllinePowerLaserPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Pm1008CtrllinePowerLaserPortn_Type.__name__=_D
_Pm1008CtrllinePowerLaserPortn_Object=MibTableColumn
pm1008CtrllinePowerLaserPortn=_Pm1008CtrllinePowerLaserPortn_Object((1,3,6,1,4,1,20044,3,6,3,215,1,2),_Pm1008CtrllinePowerLaserPortn_Type())
pm1008CtrllinePowerLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CtrllinePowerLaserPortn.setStatus(_A)
_Pm1008ri_ObjectIdentity=ObjectIdentity
pm1008ri=_Pm1008ri_ObjectIdentity((1,3,6,1,4,1,20044,3,7))
_Pm1008riTable_ObjectIdentity=ObjectIdentity
pm1008riTable=_Pm1008riTable_ObjectIdentity((1,3,6,1,4,1,20044,3,7,1))
_Pm1008RinvSfpTable_Object=MibTable
pm1008RinvSfpTable=_Pm1008RinvSfpTable_Object((1,3,6,1,4,1,20044,3,7,1,1))
if mibBuilder.loadTexts:pm1008RinvSfpTable.setStatus(_A)
_Pm1008RinvSfpEntry_Object=MibTableRow
pm1008RinvSfpEntry=_Pm1008RinvSfpEntry_Object((1,3,6,1,4,1,20044,3,7,1,1,1))
pm1008RinvSfpEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:pm1008RinvSfpEntry.setStatus(_A)
class _Pm1008RinvSfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1008RinvSfpIndex_Type.__name__=_D
_Pm1008RinvSfpIndex_Object=MibTableColumn
pm1008RinvSfpIndex=_Pm1008RinvSfpIndex_Object((1,3,6,1,4,1,20044,3,7,1,1,1,1),_Pm1008RinvSfpIndex_Type())
pm1008RinvSfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvSfpIndex.setStatus(_A)
_Pm1008Rinvsfp_Type=DisplayString
_Pm1008Rinvsfp_Object=MibTableColumn
pm1008Rinvsfp=_Pm1008Rinvsfp_Object((1,3,6,1,4,1,20044,3,7,1,1,1,2),_Pm1008Rinvsfp_Type())
pm1008Rinvsfp.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008Rinvsfp.setStatus(_A)
_Pm1008RinvLineTable_Object=MibTable
pm1008RinvLineTable=_Pm1008RinvLineTable_Object((1,3,6,1,4,1,20044,3,7,1,2))
if mibBuilder.loadTexts:pm1008RinvLineTable.setStatus(_A)
_Pm1008RinvLineEntry_Object=MibTableRow
pm1008RinvLineEntry=_Pm1008RinvLineEntry_Object((1,3,6,1,4,1,20044,3,7,1,2,1))
pm1008RinvLineEntry.setIndexNames((0,_C,_AV))
if mibBuilder.loadTexts:pm1008RinvLineEntry.setStatus(_A)
class _Pm1008RinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1008RinvLineIndex_Type.__name__=_D
_Pm1008RinvLineIndex_Object=MibTableColumn
pm1008RinvLineIndex=_Pm1008RinvLineIndex_Object((1,3,6,1,4,1,20044,3,7,1,2,1,1),_Pm1008RinvLineIndex_Type())
pm1008RinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvLineIndex.setStatus(_A)
_Pm1008RinvxfpLine_Type=DisplayString
_Pm1008RinvxfpLine_Object=MibTableColumn
pm1008RinvxfpLine=_Pm1008RinvxfpLine_Object((1,3,6,1,4,1,20044,3,7,1,2,1,2),_Pm1008RinvxfpLine_Type())
pm1008RinvxfpLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvxfpLine.setStatus(_A)
_Pm1008RinvReloadInventory_Type=EkiOnOff
_Pm1008RinvReloadInventory_Object=MibScalar
pm1008RinvReloadInventory=_Pm1008RinvReloadInventory_Object((1,3,6,1,4,1,20044,3,7,2),_Pm1008RinvReloadInventory_Type())
pm1008RinvReloadInventory.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008RinvReloadInventory.setStatus(_A)
_Pm1008RinvHwPlatform_Type=DisplayString
_Pm1008RinvHwPlatform_Object=MibScalar
pm1008RinvHwPlatform=_Pm1008RinvHwPlatform_Object((1,3,6,1,4,1,20044,3,7,3),_Pm1008RinvHwPlatform_Type())
pm1008RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvHwPlatform.setStatus(_A)
_Pm1008RinvModulePlatform_Type=DisplayString
_Pm1008RinvModulePlatform_Object=MibScalar
pm1008RinvModulePlatform=_Pm1008RinvModulePlatform_Object((1,3,6,1,4,1,20044,3,7,4),_Pm1008RinvModulePlatform_Type())
pm1008RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvModulePlatform.setStatus(_A)
_Pm1008RinvSwPlatform_Type=DisplayString
_Pm1008RinvSwPlatform_Object=MibScalar
pm1008RinvSwPlatform=_Pm1008RinvSwPlatform_Object((1,3,6,1,4,1,20044,3,7,5),_Pm1008RinvSwPlatform_Type())
pm1008RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvSwPlatform.setStatus(_A)
_Pm1008RinvGwPlatform_Type=DisplayString
_Pm1008RinvGwPlatform_Object=MibScalar
pm1008RinvGwPlatform=_Pm1008RinvGwPlatform_Object((1,3,6,1,4,1,20044,3,7,6),_Pm1008RinvGwPlatform_Type())
pm1008RinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008RinvGwPlatform.setStatus(_A)
_Pm1008download_ObjectIdentity=ObjectIdentity
pm1008download=_Pm1008download_ObjectIdentity((1,3,6,1,4,1,20044,3,8))
_Pm1008DwlOther_ObjectIdentity=ObjectIdentity
pm1008DwlOther=_Pm1008DwlOther_ObjectIdentity((1,3,6,1,4,1,20044,3,8,1))
_Pm1008DwlrestartProcess_ObjectIdentity=ObjectIdentity
pm1008DwlrestartProcess=_Pm1008DwlrestartProcess_ObjectIdentity((1,3,6,1,4,1,20044,3,8,1,0))
_Pm1008DwlWarmRestartProcessed_Type=EkiOnOff
_Pm1008DwlWarmRestartProcessed_Object=MibScalar
pm1008DwlWarmRestartProcessed=_Pm1008DwlWarmRestartProcessed_Object((1,3,6,1,4,1,20044,3,8,1,0,1),_Pm1008DwlWarmRestartProcessed_Type())
pm1008DwlWarmRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlWarmRestartProcessed.setStatus(_A)
_Pm1008DwlColdRestartProcessed_Type=EkiOnOff
_Pm1008DwlColdRestartProcessed_Object=MibScalar
pm1008DwlColdRestartProcessed=_Pm1008DwlColdRestartProcessed_Object((1,3,6,1,4,1,20044,3,8,1,0,2),_Pm1008DwlColdRestartProcessed_Type())
pm1008DwlColdRestartProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlColdRestartProcessed.setStatus(_A)
_Pm1008DwlswBanksUsed_ObjectIdentity=ObjectIdentity
pm1008DwlswBanksUsed=_Pm1008DwlswBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,3,8,1,1))
_Pm1008DwlSwBank1Used_Type=EkiOnOff
_Pm1008DwlSwBank1Used_Object=MibScalar
pm1008DwlSwBank1Used=_Pm1008DwlSwBank1Used_Object((1,3,6,1,4,1,20044,3,8,1,1,1),_Pm1008DwlSwBank1Used_Type())
pm1008DwlSwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlSwBank1Used.setStatus(_A)
_Pm1008DwlSwBank2Used_Type=EkiOnOff
_Pm1008DwlSwBank2Used_Object=MibScalar
pm1008DwlSwBank2Used=_Pm1008DwlSwBank2Used_Object((1,3,6,1,4,1,20044,3,8,1,1,2),_Pm1008DwlSwBank2Used_Type())
pm1008DwlSwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlSwBank2Used.setStatus(_A)
_Pm1008DwlSwBank1Notempty_Type=EkiOnOff
_Pm1008DwlSwBank1Notempty_Object=MibScalar
pm1008DwlSwBank1Notempty=_Pm1008DwlSwBank1Notempty_Object((1,3,6,1,4,1,20044,3,8,1,1,5),_Pm1008DwlSwBank1Notempty_Type())
pm1008DwlSwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlSwBank1Notempty.setStatus(_A)
_Pm1008DwlSwBank2Notempty_Type=EkiOnOff
_Pm1008DwlSwBank2Notempty_Object=MibScalar
pm1008DwlSwBank2Notempty=_Pm1008DwlSwBank2Notempty_Object((1,3,6,1,4,1,20044,3,8,1,1,6),_Pm1008DwlSwBank2Notempty_Type())
pm1008DwlSwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlSwBank2Notempty.setStatus(_A)
_Pm1008DwlgwBanksUsed_ObjectIdentity=ObjectIdentity
pm1008DwlgwBanksUsed=_Pm1008DwlgwBanksUsed_ObjectIdentity((1,3,6,1,4,1,20044,3,8,1,2))
_Pm1008DwlGwBank1Used_Type=EkiOnOff
_Pm1008DwlGwBank1Used_Object=MibScalar
pm1008DwlGwBank1Used=_Pm1008DwlGwBank1Used_Object((1,3,6,1,4,1,20044,3,8,1,2,1),_Pm1008DwlGwBank1Used_Type())
pm1008DwlGwBank1Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank1Used.setStatus(_A)
_Pm1008DwlGwBank2Used_Type=EkiOnOff
_Pm1008DwlGwBank2Used_Object=MibScalar
pm1008DwlGwBank2Used=_Pm1008DwlGwBank2Used_Object((1,3,6,1,4,1,20044,3,8,1,2,2),_Pm1008DwlGwBank2Used_Type())
pm1008DwlGwBank2Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank2Used.setStatus(_A)
_Pm1008DwlGwBank3Used_Type=EkiOnOff
_Pm1008DwlGwBank3Used_Object=MibScalar
pm1008DwlGwBank3Used=_Pm1008DwlGwBank3Used_Object((1,3,6,1,4,1,20044,3,8,1,2,3),_Pm1008DwlGwBank3Used_Type())
pm1008DwlGwBank3Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank3Used.setStatus(_A)
_Pm1008DwlGwBank4Used_Type=EkiOnOff
_Pm1008DwlGwBank4Used_Object=MibScalar
pm1008DwlGwBank4Used=_Pm1008DwlGwBank4Used_Object((1,3,6,1,4,1,20044,3,8,1,2,4),_Pm1008DwlGwBank4Used_Type())
pm1008DwlGwBank4Used.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank4Used.setStatus(_A)
_Pm1008DwlGwBank1Notempty_Type=EkiOnOff
_Pm1008DwlGwBank1Notempty_Object=MibScalar
pm1008DwlGwBank1Notempty=_Pm1008DwlGwBank1Notempty_Object((1,3,6,1,4,1,20044,3,8,1,2,5),_Pm1008DwlGwBank1Notempty_Type())
pm1008DwlGwBank1Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank1Notempty.setStatus(_A)
_Pm1008DwlGwBank2Notempty_Type=EkiOnOff
_Pm1008DwlGwBank2Notempty_Object=MibScalar
pm1008DwlGwBank2Notempty=_Pm1008DwlGwBank2Notempty_Object((1,3,6,1,4,1,20044,3,8,1,2,6),_Pm1008DwlGwBank2Notempty_Type())
pm1008DwlGwBank2Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank2Notempty.setStatus(_A)
_Pm1008DwlGwBank3Notempty_Type=EkiOnOff
_Pm1008DwlGwBank3Notempty_Object=MibScalar
pm1008DwlGwBank3Notempty=_Pm1008DwlGwBank3Notempty_Object((1,3,6,1,4,1,20044,3,8,1,2,7),_Pm1008DwlGwBank3Notempty_Type())
pm1008DwlGwBank3Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank3Notempty.setStatus(_A)
_Pm1008DwlGwBank4Notempty_Type=EkiOnOff
_Pm1008DwlGwBank4Notempty_Object=MibScalar
pm1008DwlGwBank4Notempty=_Pm1008DwlGwBank4Notempty_Object((1,3,6,1,4,1,20044,3,8,1,2,8),_Pm1008DwlGwBank4Notempty_Type())
pm1008DwlGwBank4Notempty.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008DwlGwBank4Notempty.setStatus(_A)
_Pm1008DwlClient_ObjectIdentity=ObjectIdentity
pm1008DwlClient=_Pm1008DwlClient_ObjectIdentity((1,3,6,1,4,1,20044,3,8,2))
_Pm1008DwlLine_ObjectIdentity=ObjectIdentity
pm1008DwlLine=_Pm1008DwlLine_ObjectIdentity((1,3,6,1,4,1,20044,3,8,3))
_Pm1008Config_ObjectIdentity=ObjectIdentity
pm1008Config=_Pm1008Config_ObjectIdentity((1,3,6,1,4,1,20044,3,9))
_Pm1008CfgAccessCAisCsf_ObjectIdentity=ObjectIdentity
pm1008CfgAccessCAisCsf=_Pm1008CfgAccessCAisCsf_ObjectIdentity((1,3,6,1,4,1,20044,3,9,1))
_Pm1008CfgClientcaiscsfTable_Object=MibTable
pm1008CfgClientcaiscsfTable=_Pm1008CfgClientcaiscsfTable_Object((1,3,6,1,4,1,20044,3,9,1,1))
if mibBuilder.loadTexts:pm1008CfgClientcaiscsfTable.setStatus(_A)
_Pm1008CfgClientcaiscsfEntry_Object=MibTableRow
pm1008CfgClientcaiscsfEntry=_Pm1008CfgClientcaiscsfEntry_Object((1,3,6,1,4,1,20044,3,9,1,1,1))
pm1008CfgClientcaiscsfEntry.setIndexNames((0,_C,_AW))
if mibBuilder.loadTexts:pm1008CfgClientcaiscsfEntry.setStatus(_A)
class _Pm1008CfgClientcaiscsfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgClientcaiscsfIndex_Type.__name__=_D
_Pm1008CfgClientcaiscsfIndex_Object=MibTableColumn
pm1008CfgClientcaiscsfIndex=_Pm1008CfgClientcaiscsfIndex_Object((1,3,6,1,4,1,20044,3,9,1,1,1,1),_Pm1008CfgClientcaiscsfIndex_Type())
pm1008CfgClientcaiscsfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgClientcaiscsfIndex.setStatus(_A)
class _Pm1008CfgCAisModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgCAisModePortn_Type.__name__=_F
_Pm1008CfgCAisModePortn_Object=MibTableColumn
pm1008CfgCAisModePortn=_Pm1008CfgCAisModePortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,3),_Pm1008CfgCAisModePortn_Type())
pm1008CfgCAisModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgCAisModePortn.setStatus(_A)
class _Pm1008CfgUpAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgUpAccessioAlmPortn_Type.__name__=_F
_Pm1008CfgUpAccessioAlmPortn_Object=MibTableColumn
pm1008CfgUpAccessioAlmPortn=_Pm1008CfgUpAccessioAlmPortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,9),_Pm1008CfgUpAccessioAlmPortn_Type())
pm1008CfgUpAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgUpAccessioAlmPortn.setStatus(_A)
class _Pm1008CfgUpMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgUpMapperDeAlmPortn_Type.__name__=_F
_Pm1008CfgUpMapperDeAlmPortn_Object=MibTableColumn
pm1008CfgUpMapperDeAlmPortn=_Pm1008CfgUpMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,10),_Pm1008CfgUpMapperDeAlmPortn_Type())
pm1008CfgUpMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgUpMapperDeAlmPortn.setStatus(_A)
class _Pm1008CfgDownAccessioAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgDownAccessioAlmPortn_Type.__name__=_F
_Pm1008CfgDownAccessioAlmPortn_Object=MibTableColumn
pm1008CfgDownAccessioAlmPortn=_Pm1008CfgDownAccessioAlmPortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,17),_Pm1008CfgDownAccessioAlmPortn_Type())
pm1008CfgDownAccessioAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgDownAccessioAlmPortn.setStatus(_A)
class _Pm1008CfgDownMapperDeAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgDownMapperDeAlmPortn_Type.__name__=_F
_Pm1008CfgDownMapperDeAlmPortn_Object=MibTableColumn
pm1008CfgDownMapperDeAlmPortn=_Pm1008CfgDownMapperDeAlmPortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,18),_Pm1008CfgDownMapperDeAlmPortn_Type())
pm1008CfgDownMapperDeAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgDownMapperDeAlmPortn.setStatus(_A)
class _Pm1008CfgDownDfrmAlmPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgDownDfrmAlmPortn_Type.__name__=_F
_Pm1008CfgDownDfrmAlmPortn_Object=MibTableColumn
pm1008CfgDownDfrmAlmPortn=_Pm1008CfgDownDfrmAlmPortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,19),_Pm1008CfgDownDfrmAlmPortn_Type())
pm1008CfgDownDfrmAlmPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgDownDfrmAlmPortn.setStatus(_A)
class _Pm1008CfgDownLineSyncAlarmsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgDownLineSyncAlarmsPortn_Type.__name__=_F
_Pm1008CfgDownLineSyncAlarmsPortn_Object=MibTableColumn
pm1008CfgDownLineSyncAlarmsPortn=_Pm1008CfgDownLineSyncAlarmsPortn_Object((1,3,6,1,4,1,20044,3,9,1,1,1,20),_Pm1008CfgDownLineSyncAlarmsPortn_Type())
pm1008CfgDownLineSyncAlarmsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgDownLineSyncAlarmsPortn.setStatus(_G)
_Pm1008CfgStartup_ObjectIdentity=ObjectIdentity
pm1008CfgStartup=_Pm1008CfgStartup_ObjectIdentity((1,3,6,1,4,1,20044,3,9,2))
_Pm1008CfgClientStartupTable_Object=MibTable
pm1008CfgClientStartupTable=_Pm1008CfgClientStartupTable_Object((1,3,6,1,4,1,20044,3,9,2,1))
if mibBuilder.loadTexts:pm1008CfgClientStartupTable.setStatus(_A)
_Pm1008CfgClientStartupEntry_Object=MibTableRow
pm1008CfgClientStartupEntry=_Pm1008CfgClientStartupEntry_Object((1,3,6,1,4,1,20044,3,9,2,1,1))
pm1008CfgClientStartupEntry.setIndexNames((0,_C,_AX))
if mibBuilder.loadTexts:pm1008CfgClientStartupEntry.setStatus(_A)
class _Pm1008CfgClientStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgClientStartupIndex_Type.__name__=_D
_Pm1008CfgClientStartupIndex_Object=MibTableColumn
pm1008CfgClientStartupIndex=_Pm1008CfgClientStartupIndex_Object((1,3,6,1,4,1,20044,3,9,2,1,1,1),_Pm1008CfgClientStartupIndex_Type())
pm1008CfgClientStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgClientStartupIndex.setStatus(_A)
class _Pm1008CfgSystConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgSystConfPortPortn_Type.__name__=_F
_Pm1008CfgSystConfPortPortn_Object=MibTableColumn
pm1008CfgSystConfPortPortn=_Pm1008CfgSystConfPortPortn_Object((1,3,6,1,4,1,20044,3,9,2,1,1,3),_Pm1008CfgSystConfPortPortn_Type())
pm1008CfgSystConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgSystConfPortPortn.setStatus(_A)
class _Pm1008CfgNetConfPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgNetConfPortPortn_Type.__name__=_F
_Pm1008CfgNetConfPortPortn_Object=MibTableColumn
pm1008CfgNetConfPortPortn=_Pm1008CfgNetConfPortPortn_Object((1,3,6,1,4,1,20044,3,9,2,1,1,4),_Pm1008CfgNetConfPortPortn_Type())
pm1008CfgNetConfPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgNetConfPortPortn.setStatus(_A)
class _Pm1008CfgOptionsPortPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgOptionsPortPortn_Type.__name__=_F
_Pm1008CfgOptionsPortPortn_Object=MibTableColumn
pm1008CfgOptionsPortPortn=_Pm1008CfgOptionsPortPortn_Object((1,3,6,1,4,1,20044,3,9,2,1,1,6),_Pm1008CfgOptionsPortPortn_Type())
pm1008CfgOptionsPortPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgOptionsPortPortn.setStatus(_A)
_Pm1008tablelineStartup_ObjectIdentity=ObjectIdentity
pm1008tablelineStartup=_Pm1008tablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,3,9,2,2))
class _Pm1008CfgsystConfLine1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgsystConfLine1_Type.__name__=_F
_Pm1008CfgsystConfLine1_Object=MibScalar
pm1008CfgsystConfLine1=_Pm1008CfgsystConfLine1_Object((1,3,6,1,4,1,20044,3,9,2,2,2),_Pm1008CfgsystConfLine1_Type())
pm1008CfgsystConfLine1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgsystConfLine1.setStatus(_A)
class _Pm1008CfglineOptions1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfglineOptions1_Type.__name__=_F
_Pm1008CfglineOptions1_Object=MibScalar
pm1008CfglineOptions1=_Pm1008CfglineOptions1_Object((1,3,6,1,4,1,20044,3,9,2,2,5),_Pm1008CfglineOptions1_Type())
pm1008CfglineOptions1.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfglineOptions1.setStatus(_A)
class _Pm1008CfgsystConfLine2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgsystConfLine2_Type.__name__=_F
_Pm1008CfgsystConfLine2_Object=MibScalar
pm1008CfgsystConfLine2=_Pm1008CfgsystConfLine2_Object((1,3,6,1,4,1,20044,3,9,2,2,6),_Pm1008CfgsystConfLine2_Type())
pm1008CfgsystConfLine2.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgsystConfLine2.setStatus(_A)
class _Pm1008CfglineSelection_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfglineSelection_Type.__name__=_F
_Pm1008CfglineSelection_Object=MibScalar
pm1008CfglineSelection=_Pm1008CfglineSelection_Object((1,3,6,1,4,1,20044,3,9,2,2,7),_Pm1008CfglineSelection_Type())
pm1008CfglineSelection.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfglineSelection.setStatus(_A)
_Pm1008CfgXfpTable_Object=MibTable
pm1008CfgXfpTable=_Pm1008CfgXfpTable_Object((1,3,6,1,4,1,20044,3,9,2,3))
if mibBuilder.loadTexts:pm1008CfgXfpTable.setStatus(_A)
_Pm1008CfgXfpEntry_Object=MibTableRow
pm1008CfgXfpEntry=_Pm1008CfgXfpEntry_Object((1,3,6,1,4,1,20044,3,9,2,3,1))
pm1008CfgXfpEntry.setIndexNames((0,_C,_AY))
if mibBuilder.loadTexts:pm1008CfgXfpEntry.setStatus(_A)
class _Pm1008CfgXfpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgXfpIndex_Type.__name__=_D
_Pm1008CfgXfpIndex_Object=MibTableColumn
pm1008CfgXfpIndex=_Pm1008CfgXfpIndex_Object((1,3,6,1,4,1,20044,3,9,2,3,1,1),_Pm1008CfgXfpIndex_Type())
pm1008CfgXfpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgXfpIndex.setStatus(_A)
class _Pm1008CfgSystConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgSystConfXfpPortn_Type.__name__=_F
_Pm1008CfgSystConfXfpPortn_Object=MibTableColumn
pm1008CfgSystConfXfpPortn=_Pm1008CfgSystConfXfpPortn_Object((1,3,6,1,4,1,20044,3,9,2,3,1,3),_Pm1008CfgSystConfXfpPortn_Type())
pm1008CfgSystConfXfpPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgSystConfXfpPortn.setStatus(_A)
class _Pm1008CfgDataRateConfXfpPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgDataRateConfXfpPortn_Type.__name__=_F
_Pm1008CfgDataRateConfXfpPortn_Object=MibTableColumn
pm1008CfgDataRateConfXfpPortn=_Pm1008CfgDataRateConfXfpPortn_Object((1,3,6,1,4,1,20044,3,9,2,3,1,4),_Pm1008CfgDataRateConfXfpPortn_Type())
pm1008CfgDataRateConfXfpPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgDataRateConfXfpPortn.setStatus(_G)
_Pm1008CfgLabels_ObjectIdentity=ObjectIdentity
pm1008CfgLabels=_Pm1008CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,3,9,3))
_Pm1008CfgLabelclientTable_Object=MibTable
pm1008CfgLabelclientTable=_Pm1008CfgLabelclientTable_Object((1,3,6,1,4,1,20044,3,9,3,1))
if mibBuilder.loadTexts:pm1008CfgLabelclientTable.setStatus(_A)
_Pm1008CfgLabelclientEntry_Object=MibTableRow
pm1008CfgLabelclientEntry=_Pm1008CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,3,9,3,1,1))
pm1008CfgLabelclientEntry.setIndexNames((0,_C,_AZ))
if mibBuilder.loadTexts:pm1008CfgLabelclientEntry.setStatus(_A)
class _Pm1008CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgLabelclientIndex_Type.__name__=_D
_Pm1008CfgLabelclientIndex_Object=MibTableColumn
pm1008CfgLabelclientIndex=_Pm1008CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,3,9,3,1,1,1),_Pm1008CfgLabelclientIndex_Type())
pm1008CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgLabelclientIndex.setStatus(_A)
class _Pm1008CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1008CfgLabelclientPortn_Type.__name__=_K
_Pm1008CfgLabelclientPortn_Object=MibTableColumn
pm1008CfgLabelclientPortn=_Pm1008CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,3,9,3,1,1,3),_Pm1008CfgLabelclientPortn_Type())
pm1008CfgLabelclientPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLabelclientPortn.setStatus(_A)
_Pm1008CfgLabellineTable_Object=MibTable
pm1008CfgLabellineTable=_Pm1008CfgLabellineTable_Object((1,3,6,1,4,1,20044,3,9,3,2))
if mibBuilder.loadTexts:pm1008CfgLabellineTable.setStatus(_A)
_Pm1008CfgLabellineEntry_Object=MibTableRow
pm1008CfgLabellineEntry=_Pm1008CfgLabellineEntry_Object((1,3,6,1,4,1,20044,3,9,3,2,1))
pm1008CfgLabellineEntry.setIndexNames((0,_C,_Aa))
if mibBuilder.loadTexts:pm1008CfgLabellineEntry.setStatus(_A)
class _Pm1008CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgLabellineIndex_Type.__name__=_D
_Pm1008CfgLabellineIndex_Object=MibTableColumn
pm1008CfgLabellineIndex=_Pm1008CfgLabellineIndex_Object((1,3,6,1,4,1,20044,3,9,3,2,1,1),_Pm1008CfgLabellineIndex_Type())
pm1008CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgLabellineIndex.setStatus(_A)
class _Pm1008CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1008CfgLabellinePortn_Type.__name__=_K
_Pm1008CfgLabellinePortn_Object=MibTableColumn
pm1008CfgLabellinePortn=_Pm1008CfgLabellinePortn_Object((1,3,6,1,4,1,20044,3,9,3,2,1,3),_Pm1008CfgLabellinePortn_Type())
pm1008CfgLabellinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLabellinePortn.setStatus(_A)
_Pm1008CfgStartuptlh_ObjectIdentity=ObjectIdentity
pm1008CfgStartuptlh=_Pm1008CfgStartuptlh_ObjectIdentity((1,3,6,1,4,1,20044,3,9,4))
_Pm1008CfgOtxtlhTable_Object=MibTable
pm1008CfgOtxtlhTable=_Pm1008CfgOtxtlhTable_Object((1,3,6,1,4,1,20044,3,9,4,1))
if mibBuilder.loadTexts:pm1008CfgOtxtlhTable.setStatus(_A)
_Pm1008CfgOtxtlhEntry_Object=MibTableRow
pm1008CfgOtxtlhEntry=_Pm1008CfgOtxtlhEntry_Object((1,3,6,1,4,1,20044,3,9,4,1,1))
pm1008CfgOtxtlhEntry.setIndexNames((0,_C,_Ab))
if mibBuilder.loadTexts:pm1008CfgOtxtlhEntry.setStatus(_A)
class _Pm1008CfgOtxtlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgOtxtlhIndex_Type.__name__=_D
_Pm1008CfgOtxtlhIndex_Object=MibTableColumn
pm1008CfgOtxtlhIndex=_Pm1008CfgOtxtlhIndex_Object((1,3,6,1,4,1,20044,3,9,4,1,1,1),_Pm1008CfgOtxtlhIndex_Type())
pm1008CfgOtxtlhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgOtxtlhIndex.setStatus(_A)
class _Pm1008CfgNuPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgNuPortn_Type.__name__=_F
_Pm1008CfgNuPortn_Object=MibTableColumn
pm1008CfgNuPortn=_Pm1008CfgNuPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,3),_Pm1008CfgNuPortn_Type())
pm1008CfgNuPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgNuPortn.setStatus(_G)
class _Pm1008CfgLineDitherRatePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLineDitherRatePortn_Type.__name__=_F
_Pm1008CfgLineDitherRatePortn_Object=MibTableColumn
pm1008CfgLineDitherRatePortn=_Pm1008CfgLineDitherRatePortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,4),_Pm1008CfgLineDitherRatePortn_Type())
pm1008CfgLineDitherRatePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLineDitherRatePortn.setStatus(_A)
class _Pm1008CfgLineDitherFhzPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLineDitherFhzPortn_Type.__name__=_F
_Pm1008CfgLineDitherFhzPortn_Object=MibTableColumn
pm1008CfgLineDitherFhzPortn=_Pm1008CfgLineDitherFhzPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,5),_Pm1008CfgLineDitherFhzPortn_Type())
pm1008CfgLineDitherFhzPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLineDitherFhzPortn.setStatus(_A)
class _Pm1008CfgLinePwrLaserPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLinePwrLaserPortn_Type.__name__=_F
_Pm1008CfgLinePwrLaserPortn_Object=MibTableColumn
pm1008CfgLinePwrLaserPortn=_Pm1008CfgLinePwrLaserPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,6),_Pm1008CfgLinePwrLaserPortn_Type())
pm1008CfgLinePwrLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLinePwrLaserPortn.setStatus(_A)
class _Pm1008CfgLineFCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLineFCurrentPortn_Type.__name__=_F
_Pm1008CfgLineFCurrentPortn_Object=MibTableColumn
pm1008CfgLineFCurrentPortn=_Pm1008CfgLineFCurrentPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,7),_Pm1008CfgLineFCurrentPortn_Type())
pm1008CfgLineFCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLineFCurrentPortn.setStatus(_A)
class _Pm1008CfgLineGridCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLineGridCurrentPortn_Type.__name__=_F
_Pm1008CfgLineGridCurrentPortn_Object=MibTableColumn
pm1008CfgLineGridCurrentPortn=_Pm1008CfgLineGridCurrentPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,8),_Pm1008CfgLineGridCurrentPortn_Type())
pm1008CfgLineGridCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLineGridCurrentPortn.setStatus(_A)
class _Pm1008CfgFPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgFPortn_Type.__name__=_F
_Pm1008CfgFPortn_Object=MibTableColumn
pm1008CfgFPortn=_Pm1008CfgFPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,9),_Pm1008CfgFPortn_Type())
pm1008CfgFPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgFPortn.setStatus(_A)
class _Pm1008CfgReservedPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgReservedPortn_Type.__name__=_F
_Pm1008CfgReservedPortn_Object=MibTableColumn
pm1008CfgReservedPortn=_Pm1008CfgReservedPortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,10),_Pm1008CfgReservedPortn_Type())
pm1008CfgReservedPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgReservedPortn.setStatus(_G)
class _Pm1008CfgLinePhotodiodeModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLinePhotodiodeModePortn_Type.__name__=_F
_Pm1008CfgLinePhotodiodeModePortn_Object=MibTableColumn
pm1008CfgLinePhotodiodeModePortn=_Pm1008CfgLinePhotodiodeModePortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,11),_Pm1008CfgLinePhotodiodeModePortn_Type())
pm1008CfgLinePhotodiodeModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLinePhotodiodeModePortn.setStatus(_A)
class _Pm1008CfgLinePhotodiodeValuePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLinePhotodiodeValuePortn_Type.__name__=_F
_Pm1008CfgLinePhotodiodeValuePortn_Object=MibTableColumn
pm1008CfgLinePhotodiodeValuePortn=_Pm1008CfgLinePhotodiodeValuePortn_Object((1,3,6,1,4,1,20044,3,9,4,1,1,12),_Pm1008CfgLinePhotodiodeValuePortn_Type())
pm1008CfgLinePhotodiodeValuePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgLinePhotodiodeValuePortn.setStatus(_A)
_Pm1008CfgStartuptablefive_ObjectIdentity=ObjectIdentity
pm1008CfgStartuptablefive=_Pm1008CfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,3,9,5))
_Pm1008CfgOtxtlhcapabilitiesTable_Object=MibTable
pm1008CfgOtxtlhcapabilitiesTable=_Pm1008CfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,3,9,5,1))
if mibBuilder.loadTexts:pm1008CfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pm1008CfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pm1008CfgOtxtlhcapabilitiesEntry=_Pm1008CfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,3,9,5,1,1))
pm1008CfgOtxtlhcapabilitiesEntry.setIndexNames((0,_C,_Ac))
if mibBuilder.loadTexts:pm1008CfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pm1008CfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008CfgOtxtlhcapabilitiesIndex_Type.__name__=_D
_Pm1008CfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pm1008CfgOtxtlhcapabilitiesIndex=_Pm1008CfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,3,9,5,1,1,1),_Pm1008CfgOtxtlhcapabilitiesIndex_Type())
pm1008CfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pm1008CfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgComponentTypePortn_Type.__name__=_F
_Pm1008CfgComponentTypePortn_Object=MibTableColumn
pm1008CfgComponentTypePortn=_Pm1008CfgComponentTypePortn_Object((1,3,6,1,4,1,20044,3,9,5,1,1,3),_Pm1008CfgComponentTypePortn_Type())
pm1008CfgComponentTypePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgComponentTypePortn.setStatus(_A)
class _Pm1008CfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgMiscellaneousPortn_Type.__name__=_F
_Pm1008CfgMiscellaneousPortn_Object=MibTableColumn
pm1008CfgMiscellaneousPortn=_Pm1008CfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,3,9,5,1,1,4),_Pm1008CfgMiscellaneousPortn_Type())
pm1008CfgMiscellaneousPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgMiscellaneousPortn.setStatus(_A)
class _Pm1008CfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgFirstChannelPortn_Type.__name__=_F
_Pm1008CfgFirstChannelPortn_Object=MibTableColumn
pm1008CfgFirstChannelPortn=_Pm1008CfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,3,9,5,1,1,5),_Pm1008CfgFirstChannelPortn_Type())
pm1008CfgFirstChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgFirstChannelPortn.setStatus(_A)
class _Pm1008CfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgLastChannelPortn_Type.__name__=_F
_Pm1008CfgLastChannelPortn_Object=MibTableColumn
pm1008CfgLastChannelPortn=_Pm1008CfgLastChannelPortn_Object((1,3,6,1,4,1,20044,3,9,5,1,1,6),_Pm1008CfgLastChannelPortn_Type())
pm1008CfgLastChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgLastChannelPortn.setStatus(_A)
class _Pm1008CfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1008CfgGridPortn_Type.__name__=_F
_Pm1008CfgGridPortn_Object=MibTableColumn
pm1008CfgGridPortn=_Pm1008CfgGridPortn_Object((1,3,6,1,4,1,20044,3,9,5,1,1,7),_Pm1008CfgGridPortn_Type())
pm1008CfgGridPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008CfgGridPortn.setStatus(_A)
_Pm1008CfgWriteConfiguration_Type=EkiOnOff
_Pm1008CfgWriteConfiguration_Object=MibScalar
pm1008CfgWriteConfiguration=_Pm1008CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,3,9,257),_Pm1008CfgWriteConfiguration_Type())
pm1008CfgWriteConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008CfgWriteConfiguration.setStatus(_A)
_Pm1008traps_ObjectIdentity=ObjectIdentity
pm1008traps=_Pm1008traps_ObjectIdentity((1,3,6,1,4,1,20044,3,10))
class _Pm1008trapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1008trapPortNumber_Type.__name__=_D
_Pm1008trapPortNumber_Object=MibScalar
pm1008trapPortNumber=_Pm1008trapPortNumber_Object((1,3,6,1,4,1,20044,3,10,2),_Pm1008trapPortNumber_Type())
pm1008trapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008trapPortNumber.setStatus(_A)
class _Pm1008trapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1008trapLineNumber_Type.__name__=_D
_Pm1008trapLineNumber_Object=MibScalar
pm1008trapLineNumber=_Pm1008trapLineNumber_Object((1,3,6,1,4,1,20044,3,10,3),_Pm1008trapLineNumber_Type())
pm1008trapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008trapLineNumber.setStatus(_A)
class _Pm1008trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1008trapBoardNumber_Type.__name__=_D
_Pm1008trapBoardNumber_Object=MibScalar
pm1008trapBoardNumber=_Pm1008trapBoardNumber_Object((1,3,6,1,4,1,20044,3,10,4),_Pm1008trapBoardNumber_Type())
pm1008trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008trapBoardNumber.setStatus(_A)
_Pm1008Monitoring_ObjectIdentity=ObjectIdentity
pm1008Monitoring=_Pm1008Monitoring_ObjectIdentity((1,3,6,1,4,1,20044,3,11))
_Pm1008MonOther_ObjectIdentity=ObjectIdentity
pm1008MonOther=_Pm1008MonOther_ObjectIdentity((1,3,6,1,4,1,20044,3,11,1))
_Pm1008MonRmon_ObjectIdentity=ObjectIdentity
pm1008MonRmon=_Pm1008MonRmon_ObjectIdentity((1,3,6,1,4,1,20044,3,11,1,3))
_Pm1008MonCountersReset_Type=EkiOnOff
_Pm1008MonCountersReset_Object=MibScalar
pm1008MonCountersReset=_Pm1008MonCountersReset_Object((1,3,6,1,4,1,20044,3,11,1,3,359),_Pm1008MonCountersReset_Type())
pm1008MonCountersReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008MonCountersReset.setStatus(_A)
_Pm1008MonCountersStop_Type=EkiOnOff
_Pm1008MonCountersStop_Object=MibScalar
pm1008MonCountersStop=_Pm1008MonCountersStop_Object((1,3,6,1,4,1,20044,3,11,1,3,360),_Pm1008MonCountersStop_Type())
pm1008MonCountersStop.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1008MonCountersStop.setStatus(_A)
_Pm1008MonClient_ObjectIdentity=ObjectIdentity
pm1008MonClient=_Pm1008MonClient_ObjectIdentity((1,3,6,1,4,1,20044,3,11,2))
_Pm1008MonClientRmonCounter_ObjectIdentity=ObjectIdentity
pm1008MonClientRmonCounter=_Pm1008MonClientRmonCounter_ObjectIdentity((1,3,6,1,4,1,20044,3,11,2,4))
_Pm1008MonupRmonByteCntTable_Object=MibTable
pm1008MonupRmonByteCntTable=_Pm1008MonupRmonByteCntTable_Object((1,3,6,1,4,1,20044,3,11,2,4,16))
if mibBuilder.loadTexts:pm1008MonupRmonByteCntTable.setStatus(_A)
_Pm1008MonupRmonByteCntEntry_Object=MibTableRow
pm1008MonupRmonByteCntEntry=_Pm1008MonupRmonByteCntEntry_Object((1,3,6,1,4,1,20044,3,11,2,4,16,1))
pm1008MonupRmonByteCntEntry.setIndexNames((0,_C,_Ad))
if mibBuilder.loadTexts:pm1008MonupRmonByteCntEntry.setStatus(_A)
class _Pm1008MonupRmonByteCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MonupRmonByteCntIndex_Type.__name__=_D
_Pm1008MonupRmonByteCntIndex_Object=MibTableColumn
pm1008MonupRmonByteCntIndex=_Pm1008MonupRmonByteCntIndex_Object((1,3,6,1,4,1,20044,3,11,2,4,16,1,1),_Pm1008MonupRmonByteCntIndex_Type())
pm1008MonupRmonByteCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonByteCntIndex.setStatus(_A)
_Pm1008MonupRmonByteCntValuePortn_Type=Counter64
_Pm1008MonupRmonByteCntValuePortn_Object=MibTableColumn
pm1008MonupRmonByteCntValuePortn=_Pm1008MonupRmonByteCntValuePortn_Object((1,3,6,1,4,1,20044,3,11,2,4,16,1,2),_Pm1008MonupRmonByteCntValuePortn_Type())
pm1008MonupRmonByteCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonByteCntValuePortn.setStatus(_A)
_Pm1008MonupRmonByteCntErrorPortn_Type=EkiOnOff
_Pm1008MonupRmonByteCntErrorPortn_Object=MibTableColumn
pm1008MonupRmonByteCntErrorPortn=_Pm1008MonupRmonByteCntErrorPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,16,1,3),_Pm1008MonupRmonByteCntErrorPortn_Type())
pm1008MonupRmonByteCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonByteCntErrorPortn.setStatus(_A)
_Pm1008MonupRmonByteCntOverloadPortn_Type=EkiOnOff
_Pm1008MonupRmonByteCntOverloadPortn_Object=MibTableColumn
pm1008MonupRmonByteCntOverloadPortn=_Pm1008MonupRmonByteCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,16,1,4),_Pm1008MonupRmonByteCntOverloadPortn_Type())
pm1008MonupRmonByteCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonByteCntOverloadPortn.setStatus(_A)
_Pm1008MonupRmonCrcErrorCntTable_Object=MibTable
pm1008MonupRmonCrcErrorCntTable=_Pm1008MonupRmonCrcErrorCntTable_Object((1,3,6,1,4,1,20044,3,11,2,4,24))
if mibBuilder.loadTexts:pm1008MonupRmonCrcErrorCntTable.setStatus(_A)
_Pm1008MonupRmonCrcErrorCntEntry_Object=MibTableRow
pm1008MonupRmonCrcErrorCntEntry=_Pm1008MonupRmonCrcErrorCntEntry_Object((1,3,6,1,4,1,20044,3,11,2,4,24,1))
pm1008MonupRmonCrcErrorCntEntry.setIndexNames((0,_C,_Ae))
if mibBuilder.loadTexts:pm1008MonupRmonCrcErrorCntEntry.setStatus(_A)
class _Pm1008MonupRmonCrcErrorCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MonupRmonCrcErrorCntIndex_Type.__name__=_D
_Pm1008MonupRmonCrcErrorCntIndex_Object=MibTableColumn
pm1008MonupRmonCrcErrorCntIndex=_Pm1008MonupRmonCrcErrorCntIndex_Object((1,3,6,1,4,1,20044,3,11,2,4,24,1,1),_Pm1008MonupRmonCrcErrorCntIndex_Type())
pm1008MonupRmonCrcErrorCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonCrcErrorCntIndex.setStatus(_A)
_Pm1008MonupRmonCrcErrorCntValuePortn_Type=Counter64
_Pm1008MonupRmonCrcErrorCntValuePortn_Object=MibTableColumn
pm1008MonupRmonCrcErrorCntValuePortn=_Pm1008MonupRmonCrcErrorCntValuePortn_Object((1,3,6,1,4,1,20044,3,11,2,4,24,1,2),_Pm1008MonupRmonCrcErrorCntValuePortn_Type())
pm1008MonupRmonCrcErrorCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonCrcErrorCntValuePortn.setStatus(_A)
_Pm1008MonupRmonCrcErrorCntErrorPortn_Type=EkiOnOff
_Pm1008MonupRmonCrcErrorCntErrorPortn_Object=MibTableColumn
pm1008MonupRmonCrcErrorCntErrorPortn=_Pm1008MonupRmonCrcErrorCntErrorPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,24,1,3),_Pm1008MonupRmonCrcErrorCntErrorPortn_Type())
pm1008MonupRmonCrcErrorCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonCrcErrorCntErrorPortn.setStatus(_A)
_Pm1008MonupRmonCrcErrorCntOverloadPortn_Type=EkiOnOff
_Pm1008MonupRmonCrcErrorCntOverloadPortn_Object=MibTableColumn
pm1008MonupRmonCrcErrorCntOverloadPortn=_Pm1008MonupRmonCrcErrorCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,24,1,4),_Pm1008MonupRmonCrcErrorCntOverloadPortn_Type())
pm1008MonupRmonCrcErrorCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonCrcErrorCntOverloadPortn.setStatus(_A)
_Pm1008MonupRmonPacketsCntTable_Object=MibTable
pm1008MonupRmonPacketsCntTable=_Pm1008MonupRmonPacketsCntTable_Object((1,3,6,1,4,1,20044,3,11,2,4,32))
if mibBuilder.loadTexts:pm1008MonupRmonPacketsCntTable.setStatus(_A)
_Pm1008MonupRmonPacketsCntEntry_Object=MibTableRow
pm1008MonupRmonPacketsCntEntry=_Pm1008MonupRmonPacketsCntEntry_Object((1,3,6,1,4,1,20044,3,11,2,4,32,1))
pm1008MonupRmonPacketsCntEntry.setIndexNames((0,_C,_Af))
if mibBuilder.loadTexts:pm1008MonupRmonPacketsCntEntry.setStatus(_A)
class _Pm1008MonupRmonPacketsCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MonupRmonPacketsCntIndex_Type.__name__=_D
_Pm1008MonupRmonPacketsCntIndex_Object=MibTableColumn
pm1008MonupRmonPacketsCntIndex=_Pm1008MonupRmonPacketsCntIndex_Object((1,3,6,1,4,1,20044,3,11,2,4,32,1,1),_Pm1008MonupRmonPacketsCntIndex_Type())
pm1008MonupRmonPacketsCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonPacketsCntIndex.setStatus(_A)
_Pm1008MonupRmonPacketsCntValuePortn_Type=Counter64
_Pm1008MonupRmonPacketsCntValuePortn_Object=MibTableColumn
pm1008MonupRmonPacketsCntValuePortn=_Pm1008MonupRmonPacketsCntValuePortn_Object((1,3,6,1,4,1,20044,3,11,2,4,32,1,2),_Pm1008MonupRmonPacketsCntValuePortn_Type())
pm1008MonupRmonPacketsCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonPacketsCntValuePortn.setStatus(_A)
_Pm1008MonupRmonPacketsCntErrorPortn_Type=EkiOnOff
_Pm1008MonupRmonPacketsCntErrorPortn_Object=MibTableColumn
pm1008MonupRmonPacketsCntErrorPortn=_Pm1008MonupRmonPacketsCntErrorPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,32,1,3),_Pm1008MonupRmonPacketsCntErrorPortn_Type())
pm1008MonupRmonPacketsCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonPacketsCntErrorPortn.setStatus(_A)
_Pm1008MonupRmonPacketsCntOverloadPortn_Type=EkiOnOff
_Pm1008MonupRmonPacketsCntOverloadPortn_Object=MibTableColumn
pm1008MonupRmonPacketsCntOverloadPortn=_Pm1008MonupRmonPacketsCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,32,1,4),_Pm1008MonupRmonPacketsCntOverloadPortn_Type())
pm1008MonupRmonPacketsCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonPacketsCntOverloadPortn.setStatus(_A)
_Pm1008MonupRmonBroadcastCntTable_Object=MibTable
pm1008MonupRmonBroadcastCntTable=_Pm1008MonupRmonBroadcastCntTable_Object((1,3,6,1,4,1,20044,3,11,2,4,40))
if mibBuilder.loadTexts:pm1008MonupRmonBroadcastCntTable.setStatus(_A)
_Pm1008MonupRmonBroadcastCntEntry_Object=MibTableRow
pm1008MonupRmonBroadcastCntEntry=_Pm1008MonupRmonBroadcastCntEntry_Object((1,3,6,1,4,1,20044,3,11,2,4,40,1))
pm1008MonupRmonBroadcastCntEntry.setIndexNames((0,_C,_Ag))
if mibBuilder.loadTexts:pm1008MonupRmonBroadcastCntEntry.setStatus(_A)
class _Pm1008MonupRmonBroadcastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MonupRmonBroadcastCntIndex_Type.__name__=_D
_Pm1008MonupRmonBroadcastCntIndex_Object=MibTableColumn
pm1008MonupRmonBroadcastCntIndex=_Pm1008MonupRmonBroadcastCntIndex_Object((1,3,6,1,4,1,20044,3,11,2,4,40,1,1),_Pm1008MonupRmonBroadcastCntIndex_Type())
pm1008MonupRmonBroadcastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonBroadcastCntIndex.setStatus(_A)
_Pm1008MonupRmonBroadcastCntValuePortn_Type=Counter64
_Pm1008MonupRmonBroadcastCntValuePortn_Object=MibTableColumn
pm1008MonupRmonBroadcastCntValuePortn=_Pm1008MonupRmonBroadcastCntValuePortn_Object((1,3,6,1,4,1,20044,3,11,2,4,40,1,2),_Pm1008MonupRmonBroadcastCntValuePortn_Type())
pm1008MonupRmonBroadcastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonBroadcastCntValuePortn.setStatus(_A)
_Pm1008MonupRmonBroadcastCntErrorPortn_Type=EkiOnOff
_Pm1008MonupRmonBroadcastCntErrorPortn_Object=MibTableColumn
pm1008MonupRmonBroadcastCntErrorPortn=_Pm1008MonupRmonBroadcastCntErrorPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,40,1,3),_Pm1008MonupRmonBroadcastCntErrorPortn_Type())
pm1008MonupRmonBroadcastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonBroadcastCntErrorPortn.setStatus(_A)
_Pm1008MonupRmonBroadcastCntOverloadPortn_Type=EkiOnOff
_Pm1008MonupRmonBroadcastCntOverloadPortn_Object=MibTableColumn
pm1008MonupRmonBroadcastCntOverloadPortn=_Pm1008MonupRmonBroadcastCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,40,1,4),_Pm1008MonupRmonBroadcastCntOverloadPortn_Type())
pm1008MonupRmonBroadcastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonBroadcastCntOverloadPortn.setStatus(_A)
_Pm1008MonupRmonMulticastCntTable_Object=MibTable
pm1008MonupRmonMulticastCntTable=_Pm1008MonupRmonMulticastCntTable_Object((1,3,6,1,4,1,20044,3,11,2,4,48))
if mibBuilder.loadTexts:pm1008MonupRmonMulticastCntTable.setStatus(_A)
_Pm1008MonupRmonMulticastCntEntry_Object=MibTableRow
pm1008MonupRmonMulticastCntEntry=_Pm1008MonupRmonMulticastCntEntry_Object((1,3,6,1,4,1,20044,3,11,2,4,48,1))
pm1008MonupRmonMulticastCntEntry.setIndexNames((0,_C,_Ah))
if mibBuilder.loadTexts:pm1008MonupRmonMulticastCntEntry.setStatus(_A)
class _Pm1008MonupRmonMulticastCntIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1008MonupRmonMulticastCntIndex_Type.__name__=_D
_Pm1008MonupRmonMulticastCntIndex_Object=MibTableColumn
pm1008MonupRmonMulticastCntIndex=_Pm1008MonupRmonMulticastCntIndex_Object((1,3,6,1,4,1,20044,3,11,2,4,48,1,1),_Pm1008MonupRmonMulticastCntIndex_Type())
pm1008MonupRmonMulticastCntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonMulticastCntIndex.setStatus(_A)
_Pm1008MonupRmonMulticastCntValuePortn_Type=Counter64
_Pm1008MonupRmonMulticastCntValuePortn_Object=MibTableColumn
pm1008MonupRmonMulticastCntValuePortn=_Pm1008MonupRmonMulticastCntValuePortn_Object((1,3,6,1,4,1,20044,3,11,2,4,48,1,2),_Pm1008MonupRmonMulticastCntValuePortn_Type())
pm1008MonupRmonMulticastCntValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonMulticastCntValuePortn.setStatus(_A)
_Pm1008MonupRmonMulticastCntErrorPortn_Type=EkiOnOff
_Pm1008MonupRmonMulticastCntErrorPortn_Object=MibTableColumn
pm1008MonupRmonMulticastCntErrorPortn=_Pm1008MonupRmonMulticastCntErrorPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,48,1,3),_Pm1008MonupRmonMulticastCntErrorPortn_Type())
pm1008MonupRmonMulticastCntErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonMulticastCntErrorPortn.setStatus(_A)
_Pm1008MonupRmonMulticastCntOverloadPortn_Type=EkiOnOff
_Pm1008MonupRmonMulticastCntOverloadPortn_Object=MibTableColumn
pm1008MonupRmonMulticastCntOverloadPortn=_Pm1008MonupRmonMulticastCntOverloadPortn_Object((1,3,6,1,4,1,20044,3,11,2,4,48,1,4),_Pm1008MonupRmonMulticastCntOverloadPortn_Type())
pm1008MonupRmonMulticastCntOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1008MonupRmonMulticastCntOverloadPortn.setStatus(_A)
pm1008LineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,30))
pm1008LineTrapNotUrgentGoesOn.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1008LineTrapNotUrgentGoesOn.setStatus(_A)
pm1008LineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,31))
pm1008LineTrapNotUrgentGoesOff.setObjects(*((_C,_L),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1008LineTrapNotUrgentGoesOff.setStatus(_A)
pm1008LineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,32))
pm1008LineTrapUrgentGoesOn.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1008LineTrapUrgentGoesOn.setStatus(_A)
pm1008LineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,33))
pm1008LineTrapUrgentGoesOff.setObjects(*((_C,_M),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1008LineTrapUrgentGoesOff.setStatus(_A)
pm1008LineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,34))
pm1008LineTrapCritGoesOn.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1008LineTrapCritGoesOn.setStatus(_A)
pm1008LineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,35))
pm1008LineTrapCritGoesOff.setObjects(*((_C,_N),(_C,_O),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:pm1008LineTrapCritGoesOff.setStatus(_A)
pm1008ClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,40))
pm1008ClientTrapNotUrgentGoesOn.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1008ClientTrapNotUrgentGoesOn.setStatus(_A)
pm1008ClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,41))
pm1008ClientTrapNotUrgentGoesOff.setObjects(*((_C,_P),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1008ClientTrapNotUrgentGoesOff.setStatus(_A)
pm1008ClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,42))
pm1008ClientTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1008ClientTrapUrgentGoesOn.setStatus(_A)
pm1008ClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,43))
pm1008ClientTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1008ClientTrapUrgentGoesOff.setStatus(_A)
pm1008ClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,44))
pm1008ClientTrapCritGoesOn.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1008ClientTrapCritGoesOn.setStatus(_A)
pm1008ClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,45))
pm1008ClientTrapCritGoesOff.setObjects(*((_C,_R),(_C,_S),(_C,_J),(_C,_H)))
if mibBuilder.loadTexts:pm1008ClientTrapCritGoesOff.setStatus(_A)
pm1008PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,3,10,50))
pm1008PowerTrapUrgentGoesOn.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pm1008PowerTrapUrgentGoesOn.setStatus(_A)
pm1008PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,3,10,51))
pm1008PowerTrapUrgentGoesOff.setObjects(*((_C,_T),(_C,_U),(_C,_H)))
if mibBuilder.loadTexts:pm1008PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Pm1008MultiRate':Pm1008MultiRate,'Pm1008OtxMode':Pm1008OtxMode,'Pm1008OtxGrid':Pm1008OtxGrid,'Pm1008AdjustValue':Pm1008AdjustValue,'Pm1008OtxChannel':Pm1008OtxChannel,'modulePm1008':modulePm1008,'pm1008alarms':pm1008alarms,'pm1008AlmOther':pm1008AlmOther,'pm1008AlmOtherNurg':pm1008AlmOtherNurg,'pm1008AlmsynthAlm2':pm1008AlmsynthAlm2,'pm1008AlmConfTableSave':pm1008AlmConfTableSave,'pm1008AlmInvUpload':pm1008AlmInvUpload,'pm1008AlmConfTableLoad':pm1008AlmConfTableLoad,'pm1008AlmCorrelatOff':pm1008AlmCorrelatOff,'pm1008AlmMaintenanceOn':pm1008AlmMaintenanceOn,'pm1008AlmOtherUrg':pm1008AlmOtherUrg,'pm1008AlmmodInitFailLevel2':pm1008AlmmodInitFailLevel2,'pm1008AlmLedFail':pm1008AlmLedFail,'pm1008AlmNextColdBootForced':pm1008AlmNextColdBootForced,'pm1008AlmBootUndone':pm1008AlmBootUndone,'pm1008AlmResetHwInitFail':pm1008AlmResetHwInitFail,'pm1008AlmSwInitFail':pm1008AlmSwInitFail,'pm1008AlmmodInitFailLevel3':pm1008AlmmodInitFailLevel3,'pm1008AlmGwIdentFail':pm1008AlmGwIdentFail,'pm1008AlmObmTypeReadFail':pm1008AlmObmTypeReadFail,'pm1008AlmInitModuleFail':pm1008AlmInitModuleFail,'pm1008AlmXfp1InitFail':pm1008AlmXfp1InitFail,'pm1008AlmXfp2InitFail':pm1008AlmXfp2InitFail,'pm1008AlmLine1InitFail':pm1008AlmLine1InitFail,'pm1008AlmLine2InitFail':pm1008AlmLine2InitFail,'pm1008AlmClient1InitFail':pm1008AlmClient1InitFail,'pm1008AlmClient2InitFail':pm1008AlmClient2InitFail,'pm1008AlmClient3InitFail':pm1008AlmClient3InitFail,'pm1008AlmClient4InitFail':pm1008AlmClient4InitFail,'pm1008AlmClient5InitFail':pm1008AlmClient5InitFail,'pm1008AlmClient6InitFail':pm1008AlmClient6InitFail,'pm1008AlmClient7InitFail':pm1008AlmClient7InitFail,'pm1008AlmClient8InitFail':pm1008AlmClient8InitFail,'pm1008AlmOtherCrit':pm1008AlmOtherCrit,'pm1008AlmsynthAlm0':pm1008AlmsynthAlm0,'pm1008AlmModGlobFail':pm1008AlmModGlobFail,_U:pm1008AlmDefFuseA,_T:pm1008AlmDefFuseB,'pm1008AlmClient':pm1008AlmClient,'pm1008AlmClientNurg':pm1008AlmClientNurg,'pm1008AlmsfpWarnDdmTable':pm1008AlmsfpWarnDdmTable,'pm1008AlmsfpWarnDdmEntry':pm1008AlmsfpWarnDdmEntry,_W:pm1008AlmsfpWarnDdmIndex,'pm1008AlmTxPwLowWngPortn':pm1008AlmTxPwLowWngPortn,'pm1008AlmTxPwrHighWngPortn':pm1008AlmTxPwrHighWngPortn,'pm1008AlmTxBiasLowWngPortn':pm1008AlmTxBiasLowWngPortn,'pm1008AlmTxBiasHighWngPortn':pm1008AlmTxBiasHighWngPortn,'pm1008AlmVccLowWngPortn':pm1008AlmVccLowWngPortn,'pm1008AlmVccHighWngPortn':pm1008AlmVccHighWngPortn,'pm1008AlmTempLowWngPortn':pm1008AlmTempLowWngPortn,'pm1008AlmTempHighWngPortn':pm1008AlmTempHighWngPortn,'pm1008AlmRxPwrLowWngPortn':pm1008AlmRxPwrLowWngPortn,'pm1008AlmRxPwrHighWngPortn':pm1008AlmRxPwrHighWngPortn,'pm1008AlmClientUrg':pm1008AlmClientUrg,'pm1008AlmsfpAlmDdmTable':pm1008AlmsfpAlmDdmTable,'pm1008AlmsfpAlmDdmEntry':pm1008AlmsfpAlmDdmEntry,_X:pm1008AlmsfpAlmDdmIndex,'pm1008AlmTxPwrLowAlaPortn':pm1008AlmTxPwrLowAlaPortn,'pm1008AlmTxPwrHighAlaPortn':pm1008AlmTxPwrHighAlaPortn,'pm1008AlmTxBiasLowAlaPortn':pm1008AlmTxBiasLowAlaPortn,'pm1008AlmTxBiasHighAlaPortn':pm1008AlmTxBiasHighAlaPortn,'pm1008AlmVccLowAlaPortn':pm1008AlmVccLowAlaPortn,'pm1008AlmVccHighAlaPortn':pm1008AlmVccHighAlaPortn,'pm1008AlmTempLowAlaPortn':pm1008AlmTempLowAlaPortn,'pm1008AlmTempHighAlaPortn':pm1008AlmTempHighAlaPortn,'pm1008AlmRxPwrLowAlaPortn':pm1008AlmRxPwrLowAlaPortn,'pm1008AlmRxPwrHighAlaPortn':pm1008AlmRxPwrHighAlaPortn,'pm1008AlmClientCrit':pm1008AlmClientCrit,'pm1008AlmsynthAlmPortTable':pm1008AlmsynthAlmPortTable,'pm1008AlmsynthAlmPortEntry':pm1008AlmsynthAlmPortEntry,_Y:pm1008AlmsynthAlmPortIndex,'pm1008AlmSfpAbsentPortn':pm1008AlmSfpAbsentPortn,'pm1008AlmDdmAbsentPortn':pm1008AlmDdmAbsentPortn,_S:pm1008AlmHwFailAccPortn,'pm1008AlmDwLsdPortn':pm1008AlmDwLsdPortn,'pm1008AlmClientLocalOosPortn':pm1008AlmClientLocalOosPortn,'pm1008AlmClientRemoteOosPortn':pm1008AlmClientRemoteOosPortn,'pm1008AlmDwCaisPortn':pm1008AlmDwCaisPortn,_P:pm1008AlmSfpDdmWarningPortn,_Q:pm1008AlmSfpDdmAlmPortn,_R:pm1008AlmFailAccPortn,'pm1008AlmUpCsfPortn':pm1008AlmUpCsfPortn,'pm1008AlmaccessioAlmTable':pm1008AlmaccessioAlmTable,'pm1008AlmaccessioAlmEntry':pm1008AlmaccessioAlmEntry,_Z:pm1008AlmaccessioAlmIndex,'pm1008AlmDwLasFailPortn':pm1008AlmDwLasFailPortn,'pm1008AlmUpLosPortn':pm1008AlmUpLosPortn,'pm1008AlmmapperDeAlmTable':pm1008AlmmapperDeAlmTable,'pm1008AlmmapperDeAlmEntry':pm1008AlmmapperDeAlmEntry,_a:pm1008AlmmapperDeAlmIndex,'pm1008AlmUpAccOosPortn':pm1008AlmUpAccOosPortn,'pm1008AlmUpBufferOvlPortn':pm1008AlmUpBufferOvlPortn,'pm1008AlmDwCsfDetPortn':pm1008AlmDwCsfDetPortn,'pm1008AlmDwBufferOvlPortn':pm1008AlmDwBufferOvlPortn,'pm1008AlmLine':pm1008AlmLine,'pm1008AlmLineNurg':pm1008AlmLineNurg,'pm1008AlmlineXfp1WarningsTable':pm1008AlmlineXfp1WarningsTable,'pm1008AlmlineXfp1WarningsEntry':pm1008AlmlineXfp1WarningsEntry,_b:pm1008AlmlineXfp1WarningsIndex,'pm1008AlmTxPowerLowWarningPortn':pm1008AlmTxPowerLowWarningPortn,'pm1008AlmTxPowerHighWarningPortn':pm1008AlmTxPowerHighWarningPortn,'pm1008AlmTxBiasLowWarningPortn':pm1008AlmTxBiasLowWarningPortn,'pm1008AlmTxBiasHighWarningPortn':pm1008AlmTxBiasHighWarningPortn,'pm1008AlmTempLowWarningPortn':pm1008AlmTempLowWarningPortn,'pm1008AlmTempHighWarningPortn':pm1008AlmTempHighWarningPortn,'pm1008AlmRxPowerLowWarningPortn':pm1008AlmRxPowerLowWarningPortn,'pm1008AlmRxPowerHighWarningPortn':pm1008AlmRxPowerHighWarningPortn,'pm1008AlmlineOtx1TlhWarningsTable':pm1008AlmlineOtx1TlhWarningsTable,'pm1008AlmlineOtx1TlhWarningsEntry':pm1008AlmlineOtx1TlhWarningsEntry,_c:pm1008AlmlineOtx1TlhWarningsIndex,'pm1008AlmLineModulatorAgingHighWarningPortn':pm1008AlmLineModulatorAgingHighWarningPortn,'pm1008AlmLineAgingHighWarningPortn':pm1008AlmLineAgingHighWarningPortn,'pm1008AlmLineFreqDevHighWarningPortn':pm1008AlmLineFreqDevHighWarningPortn,'pm1008AlmLineLaserTempHighWarningPortn':pm1008AlmLineLaserTempHighWarningPortn,'pm1008AlmLineUrg':pm1008AlmLineUrg,'pm1008AlmdfrmBerTable':pm1008AlmdfrmBerTable,'pm1008AlmdfrmBerEntry':pm1008AlmdfrmBerEntry,_d:pm1008AlmdfrmBerIndex,'pm1008AlmLineSignalDegradePortn':pm1008AlmLineSignalDegradePortn,'pm1008AlmLineSignalFailPortn':pm1008AlmLineSignalFailPortn,'pm1008AlmLineDegradePortn':pm1008AlmLineDegradePortn,'pm1008AlmlineXfp1AlarmTable':pm1008AlmlineXfp1AlarmTable,'pm1008AlmlineXfp1AlarmEntry':pm1008AlmlineXfp1AlarmEntry,_e:pm1008AlmlineXfp1AlarmIndex,'pm1008AlmTxPowerLowAlarmPortn':pm1008AlmTxPowerLowAlarmPortn,'pm1008AlmTxPowerHighAlarmPortn':pm1008AlmTxPowerHighAlarmPortn,'pm1008AlmTxBiasLowAlarmPortn':pm1008AlmTxBiasLowAlarmPortn,'pm1008AlmTxBiasHighAlarmPortn':pm1008AlmTxBiasHighAlarmPortn,'pm1008AlmTempLowAlarmPortn':pm1008AlmTempLowAlarmPortn,'pm1008AlmTempHighAlarmPortn':pm1008AlmTempHighAlarmPortn,'pm1008AlmRxPowerLowAlarmPortn':pm1008AlmRxPowerLowAlarmPortn,'pm1008AlmRxPowerHighAlarmPortn':pm1008AlmRxPowerHighAlarmPortn,'pm1008AlmlineXfp1SupplyAlarmTable':pm1008AlmlineXfp1SupplyAlarmTable,'pm1008AlmlineXfp1SupplyAlarmEntry':pm1008AlmlineXfp1SupplyAlarmEntry,_f:pm1008AlmlineXfp1SupplyAlarmIndex,'pm1008AlmVee5LowAlarmPortn':pm1008AlmVee5LowAlarmPortn,'pm1008AlmVee5HighAlarmPortn':pm1008AlmVee5HighAlarmPortn,'pm1008AlmVcc2LowAlarmPortn':pm1008AlmVcc2LowAlarmPortn,'pm1008AlmVcc2HighAlarmPortn':pm1008AlmVcc2HighAlarmPortn,'pm1008AlmVcc3LowAlarmPortn':pm1008AlmVcc3LowAlarmPortn,'pm1008AlmVcc3HighAlarmPortn':pm1008AlmVcc3HighAlarmPortn,'pm1008AlmVcc5LowAlarmPortn':pm1008AlmVcc5LowAlarmPortn,'pm1008AlmVcc5HighAlarmPortn':pm1008AlmVcc5HighAlarmPortn,'pm1008AlmVee5LowWarningPortn':pm1008AlmVee5LowWarningPortn,'pm1008AlmVee5HighWarningPortn':pm1008AlmVee5HighWarningPortn,'pm1008AlmVcc2LowWarningPortn':pm1008AlmVcc2LowWarningPortn,'pm1008AlmVcc2HighWarningPortn':pm1008AlmVcc2HighWarningPortn,'pm1008AlmVcc3LowWarningPortn':pm1008AlmVcc3LowWarningPortn,'pm1008AlmVcc3HighWarningPortn':pm1008AlmVcc3HighWarningPortn,'pm1008AlmVcc5LowWarningPortn':pm1008AlmVcc5LowWarningPortn,'pm1008AlmVcc5HighWarningPortn':pm1008AlmVcc5HighWarningPortn,'pm1008AlmlineOtx1TlhAlarmsTable':pm1008AlmlineOtx1TlhAlarmsTable,'pm1008AlmlineOtx1TlhAlarmsEntry':pm1008AlmlineOtx1TlhAlarmsEntry,_g:pm1008AlmlineOtx1TlhAlarmsIndex,'pm1008AlmLineModulatorAgingHighAlaPortn':pm1008AlmLineModulatorAgingHighAlaPortn,'pm1008AlmLineAgingHighAlaPortn':pm1008AlmLineAgingHighAlaPortn,'pm1008AlmLineFreqDevHighAlaPortn':pm1008AlmLineFreqDevHighAlaPortn,'pm1008AlmLineLaserTempHighAlaPortn':pm1008AlmLineLaserTempHighAlaPortn,'pm1008AlmLineCrit':pm1008AlmLineCrit,'pm1008AlmsynthAlmLineTable':pm1008AlmsynthAlmLineTable,'pm1008AlmsynthAlmLineEntry':pm1008AlmsynthAlmLineEntry,_h:pm1008AlmsynthAlmLineIndex,'pm1008AlmXfpAbsentPortn':pm1008AlmXfpAbsentPortn,'pm1008AlmXfpInitNotComplPortn':pm1008AlmXfpInitNotComplPortn,_O:pm1008AlmLineHwFailPortn,'pm1008AlmXfpTxOffPortn':pm1008AlmXfpTxOffPortn,'pm1008AlmLineLocalOosPortn':pm1008AlmLineLocalOosPortn,'pm1008AlmUpRdiInsPortn':pm1008AlmUpRdiInsPortn,_L:pm1008AlmLineDdmWarningPortn,_M:pm1008AlmLineDdmAlmPortn,_N:pm1008AlmLineFailPortn,'pm1008AlmLineActivePortn':pm1008AlmLineActivePortn,'pm1008AlmdfrmAlmTable':pm1008AlmdfrmAlmTable,'pm1008AlmdfrmAlmEntry':pm1008AlmdfrmAlmEntry,_i:pm1008AlmdfrmAlmIndex,'pm1008AlmDwAisDetPortn':pm1008AlmDwAisDetPortn,'pm1008AlmDwRdiDetPortn':pm1008AlmDwRdiDetPortn,'pm1008AlmDwOofPortn':pm1008AlmDwOofPortn,'pm1008AlmDwLofPortn':pm1008AlmDwLofPortn,'pm1008AlmDccLoopbackPortn':pm1008AlmDccLoopbackPortn,'pm1008AlmRxDccBroadStormPortn':pm1008AlmRxDccBroadStormPortn,'pm1008AlmTxDccBroadStormPortn':pm1008AlmTxDccBroadStormPortn,'pm1008AlmlineSyncAlarmsTable':pm1008AlmlineSyncAlarmsTable,'pm1008AlmlineSyncAlarmsEntry':pm1008AlmlineSyncAlarmsEntry,_j:pm1008AlmlineSyncAlarmsIndex,'pm1008AlmDwLockerrPortn':pm1008AlmDwLockerrPortn,'pm1008AlmUpLockerrPortn':pm1008AlmUpLockerrPortn,'pm1008AlmDwLosPortn':pm1008AlmDwLosPortn,'pm1008AlmlineXfp1AlarmsTable':pm1008AlmlineXfp1AlarmsTable,'pm1008AlmlineXfp1AlarmsEntry':pm1008AlmlineXfp1AlarmsEntry,_k:pm1008AlmlineXfp1AlarmsIndex,'pm1008AlmModNrPortn':pm1008AlmModNrPortn,'pm1008AlmRxCdrNotLockedPortn':pm1008AlmRxCdrNotLockedPortn,'pm1008AlmRxNrPortn':pm1008AlmRxNrPortn,'pm1008AlmTxCdrNotLockedPortn':pm1008AlmTxCdrNotLockedPortn,'pm1008AlmTxFaultPortn':pm1008AlmTxFaultPortn,'pm1008AlmTxNrPortn':pm1008AlmTxNrPortn,'pm1008AlmWavelengthUnlockedPortn':pm1008AlmWavelengthUnlockedPortn,'pm1008AlmTecFaultPortn':pm1008AlmTecFaultPortn,'pm1008AlmApdSupplyFaultPortn':pm1008AlmApdSupplyFaultPortn,'pm1008measures':pm1008measures,'pm1008MesrOther':pm1008MesrOther,'pm1008Mesrsynth0':pm1008Mesrsynth0,'pm1008Mesrsynth1':pm1008Mesrsynth1,'pm1008MesrClient':pm1008MesrClient,'pm1008MesrtempMeasTable':pm1008MesrtempMeasTable,'pm1008MesrtempMeasEntry':pm1008MesrtempMeasEntry,_l:pm1008MesrtempMeasIndex,'pm1008MesrtempMeasPortn':pm1008MesrtempMeasPortn,'pm1008MesrvoltMeasTable':pm1008MesrvoltMeasTable,'pm1008MesrvoltMeasEntry':pm1008MesrvoltMeasEntry,_m:pm1008MesrvoltMeasIndex,'pm1008MesrvoltMeasPortn':pm1008MesrvoltMeasPortn,'pm1008MesrbiasMeasTable':pm1008MesrbiasMeasTable,'pm1008MesrbiasMeasEntry':pm1008MesrbiasMeasEntry,_n:pm1008MesrbiasMeasIndex,'pm1008MesrbiasMeasPortn':pm1008MesrbiasMeasPortn,'pm1008MesrtxpwrMeasTable':pm1008MesrtxpwrMeasTable,'pm1008MesrtxpwrMeasEntry':pm1008MesrtxpwrMeasEntry,_o:pm1008MesrtxpwrMeasIndex,'pm1008MesrtxpwrMeasPortn':pm1008MesrtxpwrMeasPortn,'pm1008MesrrxpwrMeasTable':pm1008MesrrxpwrMeasTable,'pm1008MesrrxpwrMeasEntry':pm1008MesrrxpwrMeasEntry,_p:pm1008MesrrxpwrMeasIndex,'pm1008MesrrxpwrMeasPortn':pm1008MesrrxpwrMeasPortn,'pm1008MesrLine':pm1008MesrLine,'pm1008Mesrxfp1LxModTempMeasTable':pm1008Mesrxfp1LxModTempMeasTable,'pm1008Mesrxfp1LxModTempMeasEntry':pm1008Mesrxfp1LxModTempMeasEntry,_q:pm1008Mesrxfp1LxModTempMeasIndex,'pm1008Mesrxfp1LxModTempMeasPortn':pm1008Mesrxfp1LxModTempMeasPortn,'pm1008Mesrxfp1ReservedTable':pm1008Mesrxfp1ReservedTable,'pm1008Mesrxfp1ReservedEntry':pm1008Mesrxfp1ReservedEntry,_r:pm1008Mesrxfp1ReservedIndex,'pm1008Mesrxfp1ReservedPortn':pm1008Mesrxfp1ReservedPortn,'pm1008Mesrxfp1LoBiasCurrentMeasTable':pm1008Mesrxfp1LoBiasCurrentMeasTable,'pm1008Mesrxfp1LoBiasCurrentMeasEntry':pm1008Mesrxfp1LoBiasCurrentMeasEntry,_s:pm1008Mesrxfp1LoBiasCurrentMeasIndex,'pm1008Mesrxfp1LoBiasCurrentMeasPortn':pm1008Mesrxfp1LoBiasCurrentMeasPortn,'pm1008Mesrxfp1LoTxPowerMeasTable':pm1008Mesrxfp1LoTxPowerMeasTable,'pm1008Mesrxfp1LoTxPowerMeasEntry':pm1008Mesrxfp1LoTxPowerMeasEntry,_t:pm1008Mesrxfp1LoTxPowerMeasIndex,'pm1008Mesrxfp1LoTxPowerMeasPortn':pm1008Mesrxfp1LoTxPowerMeasPortn,'pm1008Mesrxfp1LiRxPowerMeasTable':pm1008Mesrxfp1LiRxPowerMeasTable,'pm1008Mesrxfp1LiRxPowerMeasEntry':pm1008Mesrxfp1LiRxPowerMeasEntry,_u:pm1008Mesrxfp1LiRxPowerMeasIndex,'pm1008Mesrxfp1LiRxPowerMeasPortn':pm1008Mesrxfp1LiRxPowerMeasPortn,'pm1008Mesrxfp1LxAux1MeasTable':pm1008Mesrxfp1LxAux1MeasTable,'pm1008Mesrxfp1LxAux1MeasEntry':pm1008Mesrxfp1LxAux1MeasEntry,_v:pm1008Mesrxfp1LxAux1MeasIndex,'pm1008Mesrxfp1LxAux1MeasPortn':pm1008Mesrxfp1LxAux1MeasPortn,'pm1008Mesrxfp1LxAux2MeasTable':pm1008Mesrxfp1LxAux2MeasTable,'pm1008Mesrxfp1LxAux2MeasEntry':pm1008Mesrxfp1LxAux2MeasEntry,_w:pm1008Mesrxfp1LxAux2MeasIndex,'pm1008Mesrxfp1LxAux2MeasPortn':pm1008Mesrxfp1LxAux2MeasPortn,'pm1008Mesrotx1AgingTable':pm1008Mesrotx1AgingTable,'pm1008Mesrotx1AgingEntry':pm1008Mesrotx1AgingEntry,_x:pm1008Mesrotx1AgingIndex,'pm1008Mesrotx1AgingPortn':pm1008Mesrotx1AgingPortn,'pm1008Mesrotx1LaserTemperatureTable':pm1008Mesrotx1LaserTemperatureTable,'pm1008Mesrotx1LaserTemperatureEntry':pm1008Mesrotx1LaserTemperatureEntry,_y:pm1008Mesrotx1LaserTemperatureIndex,'pm1008Mesrotx1LaserTemperaturePortn':pm1008Mesrotx1LaserTemperaturePortn,'pm1008Mesrotx1FreqDeviationTable':pm1008Mesrotx1FreqDeviationTable,'pm1008Mesrotx1FreqDeviationEntry':pm1008Mesrotx1FreqDeviationEntry,_z:pm1008Mesrotx1FreqDeviationIndex,'pm1008Mesrotx1FreqDeviationPortn':pm1008Mesrotx1FreqDeviationPortn,'pm1008Mesrotx1LaserWvlengthTable':pm1008Mesrotx1LaserWvlengthTable,'pm1008Mesrotx1LaserWvlengthEntry':pm1008Mesrotx1LaserWvlengthEntry,_A0:pm1008Mesrotx1LaserWvlengthIndex,'pm1008Mesrotx1LaserWvlengthPortn':pm1008Mesrotx1LaserWvlengthPortn,'pm1008counters':pm1008counters,'pm1008CntOther':pm1008CntOther,'pm1008CntClient':pm1008CntClient,'pm1008CntupRaRemCntTable':pm1008CntupRaRemCntTable,'pm1008CntupRaRemCntEntry':pm1008CntupRaRemCntEntry,_A1:pm1008CntupRaRemCntIndex,'pm1008CntupRaRemCntValuePortn':pm1008CntupRaRemCntValuePortn,'pm1008CntupRaRemCntErrorPortn':pm1008CntupRaRemCntErrorPortn,'pm1008CntupRaRemCntOverloadPortn':pm1008CntupRaRemCntOverloadPortn,'pm1008CntupRaInsCntTable':pm1008CntupRaInsCntTable,'pm1008CntupRaInsCntEntry':pm1008CntupRaInsCntEntry,_A2:pm1008CntupRaInsCntIndex,'pm1008CntupRaInsCntValuePortn':pm1008CntupRaInsCntValuePortn,'pm1008CntupRaInsCntErrorPortn':pm1008CntupRaInsCntErrorPortn,'pm1008CntupRaInsCntOverloadPortn':pm1008CntupRaInsCntOverloadPortn,'pm1008CntupRdErrCntTable':pm1008CntupRdErrCntTable,'pm1008CntupRdErrCntEntry':pm1008CntupRdErrCntEntry,_A3:pm1008CntupRdErrCntIndex,'pm1008CntupRdErrCntValuePortn':pm1008CntupRdErrCntValuePortn,'pm1008CntupRdErrCntErrorPortn':pm1008CntupRdErrCntErrorPortn,'pm1008CntupRdErrCntOverloadPortn':pm1008CntupRdErrCntOverloadPortn,'pm1008CntupTimCntTable':pm1008CntupTimCntTable,'pm1008CntupTimCntEntry':pm1008CntupTimCntEntry,_A4:pm1008CntupTimCntIndex,'pm1008CntupTimCntValuePortn':pm1008CntupTimCntValuePortn,'pm1008CntupTimCntErrorPortn':pm1008CntupTimCntErrorPortn,'pm1008CntupTimCntOverloadPortn':pm1008CntupTimCntOverloadPortn,'pm1008CntupCvErrCntTable':pm1008CntupCvErrCntTable,'pm1008CntupCvErrCntEntry':pm1008CntupCvErrCntEntry,_A5:pm1008CntupCvErrCntIndex,'pm1008CntupCvErrCntValuePortn':pm1008CntupCvErrCntValuePortn,'pm1008CntupCvErrCntErrorPortn':pm1008CntupCvErrCntErrorPortn,'pm1008CntupCvErrCntOverloadPortn':pm1008CntupCvErrCntOverloadPortn,'pm1008CntdwCbipCntTable':pm1008CntdwCbipCntTable,'pm1008CntdwCbipCntEntry':pm1008CntdwCbipCntEntry,_A6:pm1008CntdwCbipCntIndex,'pm1008CntdwCbipCntValuePortn':pm1008CntdwCbipCntValuePortn,'pm1008CntdwCbipCntErrorPortn':pm1008CntdwCbipCntErrorPortn,'pm1008CntdwCbipCntOverloadPortn':pm1008CntdwCbipCntOverloadPortn,'pm1008CntdwTimCntTable':pm1008CntdwTimCntTable,'pm1008CntdwTimCntEntry':pm1008CntdwTimCntEntry,_A7:pm1008CntdwTimCntIndex,'pm1008CntdwTimCntValuePortn':pm1008CntdwTimCntValuePortn,'pm1008CntdwTimCntErrorPortn':pm1008CntdwTimCntErrorPortn,'pm1008CntdwTimCntOverloadPortn':pm1008CntdwTimCntOverloadPortn,'pm1008CntLine':pm1008CntLine,'pm1008CntdfrmB1ErrCntTable':pm1008CntdfrmB1ErrCntTable,'pm1008CntdfrmB1ErrCntEntry':pm1008CntdfrmB1ErrCntEntry,_A8:pm1008CntdfrmB1ErrCntIndex,'pm1008CntdfrmB1ErrCntValuePortn':pm1008CntdfrmB1ErrCntValuePortn,'pm1008CntdfrmB1ErrCntErrorPortn':pm1008CntdfrmB1ErrCntErrorPortn,'pm1008CntdfrmB1ErrCntOverloadPortn':pm1008CntdfrmB1ErrCntOverloadPortn,'pm1008CntdfrmTimCntTable':pm1008CntdfrmTimCntTable,'pm1008CntdfrmTimCntEntry':pm1008CntdfrmTimCntEntry,_A9:pm1008CntdfrmTimCntIndex,'pm1008CntdfrmTimCntValuePortn':pm1008CntdfrmTimCntValuePortn,'pm1008CntdfrmTimCntErrorPortn':pm1008CntdfrmTimCntErrorPortn,'pm1008CntdfrmTimCntOverloadPortn':pm1008CntdfrmTimCntOverloadPortn,'pm1008CntdfrmPrimLineErrCntTable':pm1008CntdfrmPrimLineErrCntTable,'pm1008CntdfrmPrimLineErrCntEntry':pm1008CntdfrmPrimLineErrCntEntry,_AA:pm1008CntdfrmPrimLineErrCntIndex,'pm1008CntdfrmPrimLineErrCntValuePortn':pm1008CntdfrmPrimLineErrCntValuePortn,'pm1008CntdfrmPrimLineErrCntErrorPortn':pm1008CntdfrmPrimLineErrCntErrorPortn,'pm1008CntdfrmPrimLineErrCntOverloadPortn':pm1008CntdfrmPrimLineErrCntOverloadPortn,'pm1008CntCountersReset':pm1008CntCountersReset,'pm1008CntCountersStop':pm1008CntCountersStop,'pm1008controlsWrite':pm1008controlsWrite,'pm1008CtrlOther':pm1008CtrlOther,'pm1008CtrlconfMgnt1':pm1008CtrlconfMgnt1,'pm1008CtrlConf1Load1':pm1008CtrlConf1Load1,'pm1008CtrlConf2Load1':pm1008CtrlConf2Load1,'pm1008CtrlConf2Flash1':pm1008CtrlConf2Flash1,'pm1008CtrlConf2Clear1':pm1008CtrlConf2Clear1,'pm1008Ctrlsynth4':pm1008Ctrlsynth4,'pm1008CtrlCorrelatOn':pm1008CtrlCorrelatOn,'pm1008CtrlCorrelatOff':pm1008CtrlCorrelatOff,'pm1008CtrlswMgnt':pm1008CtrlswMgnt,'pm1008CtrlColdReset':pm1008CtrlColdReset,'pm1008CtrlWarmReset':pm1008CtrlWarmReset,'pm1008CtrlLoadSwBank1':pm1008CtrlLoadSwBank1,'pm1008CtrlLoadSwBank2':pm1008CtrlLoadSwBank2,'pm1008CtrlgwMgnt':pm1008CtrlgwMgnt,'pm1008CtrlCurrentGwReset':pm1008CtrlCurrentGwReset,'pm1008CtrlLoadGwBank1':pm1008CtrlLoadGwBank1,'pm1008CtrlLoadGwBank2':pm1008CtrlLoadGwBank2,'pm1008CtrlLoadGwBank3':pm1008CtrlLoadGwBank3,'pm1008CtrlLoadGwBank4':pm1008CtrlLoadGwBank4,'pm1008CtrlledTest':pm1008CtrlledTest,'pm1008CtrlGreenLed':pm1008CtrlGreenLed,'pm1008CtrlRedLed':pm1008CtrlRedLed,'pm1008CtrlLedOff':pm1008CtrlLedOff,'pm1008CtrlmoduleOosMode':pm1008CtrlmoduleOosMode,'pm1008CtrlModuleOosMode':pm1008CtrlModuleOosMode,'pm1008CtrlmaintenanceMode':pm1008CtrlmaintenanceMode,'pm1008CtrlMaintenanceMode':pm1008CtrlMaintenanceMode,'pm1008CtrldccEnable':pm1008CtrldccEnable,'pm1008CtrlDccEnable':pm1008CtrlDccEnable,'pm1008CtrlClient':pm1008CtrlClient,'pm1008CtrlaccessLoopTable':pm1008CtrlaccessLoopTable,'pm1008CtrlaccessLoopEntry':pm1008CtrlaccessLoopEntry,_AB:pm1008CtrlaccessLoopIndex,'pm1008CtrlaccessLoopPortn':pm1008CtrlaccessLoopPortn,'pm1008CtrlportOosModeTable':pm1008CtrlportOosModeTable,'pm1008CtrlportOosModeEntry':pm1008CtrlportOosModeEntry,_AC:pm1008CtrlportOosModeIndex,'pm1008CtrlportOosModePortn':pm1008CtrlportOosModePortn,'pm1008CtrlsfpOnCtrlTable':pm1008CtrlsfpOnCtrlTable,'pm1008CtrlsfpOnCtrlEntry':pm1008CtrlsfpOnCtrlEntry,_AD:pm1008CtrlsfpOnCtrlIndex,'pm1008CtrlsfpOnCtrlPortn':pm1008CtrlsfpOnCtrlPortn,'pm1008CtrlsfpOffCtrlTable':pm1008CtrlsfpOffCtrlTable,'pm1008CtrlsfpOffCtrlEntry':pm1008CtrlsfpOffCtrlEntry,_AE:pm1008CtrlsfpOffCtrlIndex,'pm1008CtrlsfpOffCtrlPortn':pm1008CtrlsfpOffCtrlPortn,'pm1008CtrlcsfUpInsTable':pm1008CtrlcsfUpInsTable,'pm1008CtrlcsfUpInsEntry':pm1008CtrlcsfUpInsEntry,_AF:pm1008CtrlcsfUpInsIndex,'pm1008CtrlcsfUpInsPortn':pm1008CtrlcsfUpInsPortn,'pm1008CtrlcaisDwInsTable':pm1008CtrlcaisDwInsTable,'pm1008CtrlcaisDwInsEntry':pm1008CtrlcaisDwInsEntry,_AG:pm1008CtrlcaisDwInsIndex,'pm1008CtrlcaisDwInsPortn':pm1008CtrlcaisDwInsPortn,'pm1008CtrlflowControlTable':pm1008CtrlflowControlTable,'pm1008CtrlflowControlEntry':pm1008CtrlflowControlEntry,_AH:pm1008CtrlflowControlIndex,'pm1008CtrlflowControlPortn':pm1008CtrlflowControlPortn,'pm1008CtrlclientAccessTermLoopTable':pm1008CtrlclientAccessTermLoopTable,'pm1008CtrlclientAccessTermLoopEntry':pm1008CtrlclientAccessTermLoopEntry,_AI:pm1008CtrlclientAccessTermLoopIndex,'pm1008CtrlclientAccessTermLoopPortn':pm1008CtrlclientAccessTermLoopPortn,'pm1008CtrlselectMultirateTable':pm1008CtrlselectMultirateTable,'pm1008CtrlselectMultirateEntry':pm1008CtrlselectMultirateEntry,_AJ:pm1008CtrlselectMultirateIndex,'pm1008CtrlselectMultiratePortn':pm1008CtrlselectMultiratePortn,'pm1008CtrlprotocolTable':pm1008CtrlprotocolTable,'pm1008CtrlprotocolEntry':pm1008CtrlprotocolEntry,_AK:pm1008CtrlprotocolIndex,'pm1008CtrlprotocolPortn':pm1008CtrlprotocolPortn,'pm1008CtrlLine':pm1008CtrlLine,'pm1008CtrlcommAccessLoop':pm1008CtrlcommAccessLoop,'pm1008CtrlCommAccessloop':pm1008CtrlCommAccessloop,'pm1008CtrllineLoop':pm1008CtrllineLoop,'pm1008CtrlLineLoop':pm1008CtrlLineLoop,'pm1008CtrlmsAis':pm1008CtrlmsAis,'pm1008CtrlMsAis':pm1008CtrlMsAis,'pm1008CtrlfecDisableTable':pm1008CtrlfecDisableTable,'pm1008CtrlfecDisableEntry':pm1008CtrlfecDisableEntry,_AL:pm1008CtrlfecDisableIndex,'pm1008CtrlfecDisablePortn':pm1008CtrlfecDisablePortn,'pm1008CtrlProtMgnt':pm1008CtrlProtMgnt,'pm1008CtrlLineNumber':pm1008CtrlLineNumber,'pm1008CtrlProtMode':pm1008CtrlProtMode,'pm1008CtrllineOosModeTable':pm1008CtrllineOosModeTable,'pm1008CtrllineOosModeEntry':pm1008CtrllineOosModeEntry,_AM:pm1008CtrllineOosModeIndex,'pm1008CtrllineOosModePortn':pm1008CtrllineOosModePortn,'pm1008CtrlxfpOnoffTable':pm1008CtrlxfpOnoffTable,'pm1008CtrlxfpOnoffEntry':pm1008CtrlxfpOnoffEntry,_AN:pm1008CtrlxfpOnoffIndex,'pm1008CtrlxfpOnoffPortn':pm1008CtrlxfpOnoffPortn,'pm1008CtrlxfpLineLoopTable':pm1008CtrlxfpLineLoopTable,'pm1008CtrlxfpLineLoopEntry':pm1008CtrlxfpLineLoopEntry,_AO:pm1008CtrlxfpLineLoopIndex,'pm1008CtrlxfpLineLoopPortn':pm1008CtrlxfpLineLoopPortn,'pm1008CtrlxfpXfiLoopTable':pm1008CtrlxfpXfiLoopTable,'pm1008CtrlxfpXfiLoopEntry':pm1008CtrlxfpXfiLoopEntry,_AP:pm1008CtrlxfpXfiLoopIndex,'pm1008CtrlxfpXfiLoopPortn':pm1008CtrlxfpXfiLoopPortn,'pm1008CtrllineTunableChannelTable':pm1008CtrllineTunableChannelTable,'pm1008CtrllineTunableChannelEntry':pm1008CtrllineTunableChannelEntry,_AQ:pm1008CtrllineTunableChannelIndex,'pm1008CtrllineTunableChannelPortn':pm1008CtrllineTunableChannelPortn,'pm1008CtrllinePhotodiodeModeTable':pm1008CtrllinePhotodiodeModeTable,'pm1008CtrllinePhotodiodeModeEntry':pm1008CtrllinePhotodiodeModeEntry,_AR:pm1008CtrllinePhotodiodeModeIndex,'pm1008CtrllinePhotodiodeModePortn':pm1008CtrllinePhotodiodeModePortn,'pm1008CtrllinePhotodiodeValueTable':pm1008CtrllinePhotodiodeValueTable,'pm1008CtrllinePhotodiodeValueEntry':pm1008CtrllinePhotodiodeValueEntry,_AS:pm1008CtrllinePhotodiodeValueIndex,'pm1008CtrllinePhotodiodeValuePortn':pm1008CtrllinePhotodiodeValuePortn,'pm1008CtrllinePowerLaserTable':pm1008CtrllinePowerLaserTable,'pm1008CtrllinePowerLaserEntry':pm1008CtrllinePowerLaserEntry,_AT:pm1008CtrllinePowerLaserIndex,'pm1008CtrllinePowerLaserPortn':pm1008CtrllinePowerLaserPortn,'pm1008ri':pm1008ri,'pm1008riTable':pm1008riTable,'pm1008RinvSfpTable':pm1008RinvSfpTable,'pm1008RinvSfpEntry':pm1008RinvSfpEntry,_AU:pm1008RinvSfpIndex,'pm1008Rinvsfp':pm1008Rinvsfp,'pm1008RinvLineTable':pm1008RinvLineTable,'pm1008RinvLineEntry':pm1008RinvLineEntry,_AV:pm1008RinvLineIndex,'pm1008RinvxfpLine':pm1008RinvxfpLine,'pm1008RinvReloadInventory':pm1008RinvReloadInventory,'pm1008RinvHwPlatform':pm1008RinvHwPlatform,'pm1008RinvModulePlatform':pm1008RinvModulePlatform,'pm1008RinvSwPlatform':pm1008RinvSwPlatform,'pm1008RinvGwPlatform':pm1008RinvGwPlatform,'pm1008download':pm1008download,'pm1008DwlOther':pm1008DwlOther,'pm1008DwlrestartProcess':pm1008DwlrestartProcess,'pm1008DwlWarmRestartProcessed':pm1008DwlWarmRestartProcessed,'pm1008DwlColdRestartProcessed':pm1008DwlColdRestartProcessed,'pm1008DwlswBanksUsed':pm1008DwlswBanksUsed,'pm1008DwlSwBank1Used':pm1008DwlSwBank1Used,'pm1008DwlSwBank2Used':pm1008DwlSwBank2Used,'pm1008DwlSwBank1Notempty':pm1008DwlSwBank1Notempty,'pm1008DwlSwBank2Notempty':pm1008DwlSwBank2Notempty,'pm1008DwlgwBanksUsed':pm1008DwlgwBanksUsed,'pm1008DwlGwBank1Used':pm1008DwlGwBank1Used,'pm1008DwlGwBank2Used':pm1008DwlGwBank2Used,'pm1008DwlGwBank3Used':pm1008DwlGwBank3Used,'pm1008DwlGwBank4Used':pm1008DwlGwBank4Used,'pm1008DwlGwBank1Notempty':pm1008DwlGwBank1Notempty,'pm1008DwlGwBank2Notempty':pm1008DwlGwBank2Notempty,'pm1008DwlGwBank3Notempty':pm1008DwlGwBank3Notempty,'pm1008DwlGwBank4Notempty':pm1008DwlGwBank4Notempty,'pm1008DwlClient':pm1008DwlClient,'pm1008DwlLine':pm1008DwlLine,'pm1008Config':pm1008Config,'pm1008CfgAccessCAisCsf':pm1008CfgAccessCAisCsf,'pm1008CfgClientcaiscsfTable':pm1008CfgClientcaiscsfTable,'pm1008CfgClientcaiscsfEntry':pm1008CfgClientcaiscsfEntry,_AW:pm1008CfgClientcaiscsfIndex,'pm1008CfgCAisModePortn':pm1008CfgCAisModePortn,'pm1008CfgUpAccessioAlmPortn':pm1008CfgUpAccessioAlmPortn,'pm1008CfgUpMapperDeAlmPortn':pm1008CfgUpMapperDeAlmPortn,'pm1008CfgDownAccessioAlmPortn':pm1008CfgDownAccessioAlmPortn,'pm1008CfgDownMapperDeAlmPortn':pm1008CfgDownMapperDeAlmPortn,'pm1008CfgDownDfrmAlmPortn':pm1008CfgDownDfrmAlmPortn,'pm1008CfgDownLineSyncAlarmsPortn':pm1008CfgDownLineSyncAlarmsPortn,'pm1008CfgStartup':pm1008CfgStartup,'pm1008CfgClientStartupTable':pm1008CfgClientStartupTable,'pm1008CfgClientStartupEntry':pm1008CfgClientStartupEntry,_AX:pm1008CfgClientStartupIndex,'pm1008CfgSystConfPortPortn':pm1008CfgSystConfPortPortn,'pm1008CfgNetConfPortPortn':pm1008CfgNetConfPortPortn,'pm1008CfgOptionsPortPortn':pm1008CfgOptionsPortPortn,'pm1008tablelineStartup':pm1008tablelineStartup,'pm1008CfgsystConfLine1':pm1008CfgsystConfLine1,'pm1008CfglineOptions1':pm1008CfglineOptions1,'pm1008CfgsystConfLine2':pm1008CfgsystConfLine2,'pm1008CfglineSelection':pm1008CfglineSelection,'pm1008CfgXfpTable':pm1008CfgXfpTable,'pm1008CfgXfpEntry':pm1008CfgXfpEntry,_AY:pm1008CfgXfpIndex,'pm1008CfgSystConfXfpPortn':pm1008CfgSystConfXfpPortn,'pm1008CfgDataRateConfXfpPortn':pm1008CfgDataRateConfXfpPortn,'pm1008CfgLabels':pm1008CfgLabels,'pm1008CfgLabelclientTable':pm1008CfgLabelclientTable,'pm1008CfgLabelclientEntry':pm1008CfgLabelclientEntry,_AZ:pm1008CfgLabelclientIndex,'pm1008CfgLabelclientPortn':pm1008CfgLabelclientPortn,'pm1008CfgLabellineTable':pm1008CfgLabellineTable,'pm1008CfgLabellineEntry':pm1008CfgLabellineEntry,_Aa:pm1008CfgLabellineIndex,'pm1008CfgLabellinePortn':pm1008CfgLabellinePortn,'pm1008CfgStartuptlh':pm1008CfgStartuptlh,'pm1008CfgOtxtlhTable':pm1008CfgOtxtlhTable,'pm1008CfgOtxtlhEntry':pm1008CfgOtxtlhEntry,_Ab:pm1008CfgOtxtlhIndex,'pm1008CfgNuPortn':pm1008CfgNuPortn,'pm1008CfgLineDitherRatePortn':pm1008CfgLineDitherRatePortn,'pm1008CfgLineDitherFhzPortn':pm1008CfgLineDitherFhzPortn,'pm1008CfgLinePwrLaserPortn':pm1008CfgLinePwrLaserPortn,'pm1008CfgLineFCurrentPortn':pm1008CfgLineFCurrentPortn,'pm1008CfgLineGridCurrentPortn':pm1008CfgLineGridCurrentPortn,'pm1008CfgFPortn':pm1008CfgFPortn,'pm1008CfgReservedPortn':pm1008CfgReservedPortn,'pm1008CfgLinePhotodiodeModePortn':pm1008CfgLinePhotodiodeModePortn,'pm1008CfgLinePhotodiodeValuePortn':pm1008CfgLinePhotodiodeValuePortn,'pm1008CfgStartuptablefive':pm1008CfgStartuptablefive,'pm1008CfgOtxtlhcapabilitiesTable':pm1008CfgOtxtlhcapabilitiesTable,'pm1008CfgOtxtlhcapabilitiesEntry':pm1008CfgOtxtlhcapabilitiesEntry,_Ac:pm1008CfgOtxtlhcapabilitiesIndex,'pm1008CfgComponentTypePortn':pm1008CfgComponentTypePortn,'pm1008CfgMiscellaneousPortn':pm1008CfgMiscellaneousPortn,'pm1008CfgFirstChannelPortn':pm1008CfgFirstChannelPortn,'pm1008CfgLastChannelPortn':pm1008CfgLastChannelPortn,'pm1008CfgGridPortn':pm1008CfgGridPortn,'pm1008CfgWriteConfiguration':pm1008CfgWriteConfiguration,'pm1008traps':pm1008traps,_J:pm1008trapPortNumber,_I:pm1008trapLineNumber,_H:pm1008trapBoardNumber,'pm1008LineTrapNotUrgentGoesOn':pm1008LineTrapNotUrgentGoesOn,'pm1008LineTrapNotUrgentGoesOff':pm1008LineTrapNotUrgentGoesOff,'pm1008LineTrapUrgentGoesOn':pm1008LineTrapUrgentGoesOn,'pm1008LineTrapUrgentGoesOff':pm1008LineTrapUrgentGoesOff,'pm1008LineTrapCritGoesOn':pm1008LineTrapCritGoesOn,'pm1008LineTrapCritGoesOff':pm1008LineTrapCritGoesOff,'pm1008ClientTrapNotUrgentGoesOn':pm1008ClientTrapNotUrgentGoesOn,'pm1008ClientTrapNotUrgentGoesOff':pm1008ClientTrapNotUrgentGoesOff,'pm1008ClientTrapUrgentGoesOn':pm1008ClientTrapUrgentGoesOn,'pm1008ClientTrapUrgentGoesOff':pm1008ClientTrapUrgentGoesOff,'pm1008ClientTrapCritGoesOn':pm1008ClientTrapCritGoesOn,'pm1008ClientTrapCritGoesOff':pm1008ClientTrapCritGoesOff,'pm1008PowerTrapUrgentGoesOn':pm1008PowerTrapUrgentGoesOn,'pm1008PowerTrapUrgentGoesOff':pm1008PowerTrapUrgentGoesOff,'pm1008Monitoring':pm1008Monitoring,'pm1008MonOther':pm1008MonOther,'pm1008MonRmon':pm1008MonRmon,'pm1008MonCountersReset':pm1008MonCountersReset,'pm1008MonCountersStop':pm1008MonCountersStop,'pm1008MonClient':pm1008MonClient,'pm1008MonClientRmonCounter':pm1008MonClientRmonCounter,'pm1008MonupRmonByteCntTable':pm1008MonupRmonByteCntTable,'pm1008MonupRmonByteCntEntry':pm1008MonupRmonByteCntEntry,_Ad:pm1008MonupRmonByteCntIndex,'pm1008MonupRmonByteCntValuePortn':pm1008MonupRmonByteCntValuePortn,'pm1008MonupRmonByteCntErrorPortn':pm1008MonupRmonByteCntErrorPortn,'pm1008MonupRmonByteCntOverloadPortn':pm1008MonupRmonByteCntOverloadPortn,'pm1008MonupRmonCrcErrorCntTable':pm1008MonupRmonCrcErrorCntTable,'pm1008MonupRmonCrcErrorCntEntry':pm1008MonupRmonCrcErrorCntEntry,_Ae:pm1008MonupRmonCrcErrorCntIndex,'pm1008MonupRmonCrcErrorCntValuePortn':pm1008MonupRmonCrcErrorCntValuePortn,'pm1008MonupRmonCrcErrorCntErrorPortn':pm1008MonupRmonCrcErrorCntErrorPortn,'pm1008MonupRmonCrcErrorCntOverloadPortn':pm1008MonupRmonCrcErrorCntOverloadPortn,'pm1008MonupRmonPacketsCntTable':pm1008MonupRmonPacketsCntTable,'pm1008MonupRmonPacketsCntEntry':pm1008MonupRmonPacketsCntEntry,_Af:pm1008MonupRmonPacketsCntIndex,'pm1008MonupRmonPacketsCntValuePortn':pm1008MonupRmonPacketsCntValuePortn,'pm1008MonupRmonPacketsCntErrorPortn':pm1008MonupRmonPacketsCntErrorPortn,'pm1008MonupRmonPacketsCntOverloadPortn':pm1008MonupRmonPacketsCntOverloadPortn,'pm1008MonupRmonBroadcastCntTable':pm1008MonupRmonBroadcastCntTable,'pm1008MonupRmonBroadcastCntEntry':pm1008MonupRmonBroadcastCntEntry,_Ag:pm1008MonupRmonBroadcastCntIndex,'pm1008MonupRmonBroadcastCntValuePortn':pm1008MonupRmonBroadcastCntValuePortn,'pm1008MonupRmonBroadcastCntErrorPortn':pm1008MonupRmonBroadcastCntErrorPortn,'pm1008MonupRmonBroadcastCntOverloadPortn':pm1008MonupRmonBroadcastCntOverloadPortn,'pm1008MonupRmonMulticastCntTable':pm1008MonupRmonMulticastCntTable,'pm1008MonupRmonMulticastCntEntry':pm1008MonupRmonMulticastCntEntry,_Ah:pm1008MonupRmonMulticastCntIndex,'pm1008MonupRmonMulticastCntValuePortn':pm1008MonupRmonMulticastCntValuePortn,'pm1008MonupRmonMulticastCntErrorPortn':pm1008MonupRmonMulticastCntErrorPortn,'pm1008MonupRmonMulticastCntOverloadPortn':pm1008MonupRmonMulticastCntOverloadPortn})