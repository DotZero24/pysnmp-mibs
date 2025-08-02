_A3='pm1604CfgOtxtlhcapabilitiesIndex'
_A2='pm1604CfgLabellineIndex'
_A1='pm1604CfgLabelclientIndex'
_A0='pm1604CfgOtxtlhIndex'
_z='pm1604CfgLine2StartupIndex'
_y='pm1604CfgLine1StartupIndex'
_x='pm1604CfgLine1LsdIndex'
_w='pm1604RinvLine2Index'
_v='pm1604RinvLine1Index'
_u='pm1604Ctrlline2LoopbackTermIndex'
_t='pm1604Ctrlline2LoopbackIndex'
_s='pm1604Ctrlline2OosModeIndex'
_r='pm1604Ctrlline2SfpOnoffIndex'
_q='pm1604CtrlprotocolIndex'
_p='pm1604Ctrlline1OosModeIndex'
_o='pm1604Ctrlline1LoopbackTermIndex'
_n='pm1604Ctrlline1LoopbackIndex'
_m='pm1604Ctrlline1SfpOnoffIndex'
_l='pm1604Mesrline2RxPowerIndex'
_k='pm1604Mesrline2TxPowerIndex'
_j='pm1604Mesrline2TxBiasIndex'
_i='pm1604Mesrline2VoltIndex'
_h='pm1604Mesrline2TemperatureIndex'
_g='pm1604Mesrline1RxPowerIndex'
_f='pm1604Mesrline1TxPowerIndex'
_e='pm1604Mesrline1TxBiasIndex'
_d='pm1604Mesrline1VoltIndex'
_c='pm1604Mesrline1TemperatureIndex'
_b='pm1604Almline2AccessioAlmIndex'
_a='pm1604AlmsynthAlmLine2Index'
_Z='pm1604Almline2SfpAlmDdmIndex'
_Y='pm1604Almline2SfpWarnDdmIndex'
_X='pm1604Almline1AccessioAlmIndex'
_W='pm1604AlmsynthAlmLine1Index'
_V='pm1604Almline1SfpAlmDdmIndex'
_U='pm1604Almline1SfpWarnDdmIndex'
_T='pm1604AlmDefFuseA'
_S='pm1604AlmDefFuseB'
_R='pm1604AlmLine1HwFailAccPortn'
_Q='pm1604AlmLine1FailAccPortn'
_P='pm1604AlmLine1SfpDdmAlmPortn'
_O='pm1604AlmLine1SfpDdmWarningPortn'
_N='pm1604AlmLine2HwFailPortn'
_M='pm1604AlmLine2FailPortn'
_L='pm1604AlmLine2DdmAlmPortn'
_K='pm1604AlmLine2DdmWarningPortn'
_J='DisplayString'
_I='pm1604trapPortNumber'
_H='pm1604trapLineNumber'
_G='pm1604trapBoardNumber'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='EKINOPS-Pm1604-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
modulePm1604=ModuleIdentity((1,3,6,1,4,1,20044,77))
if mibBuilder.loadTexts:modulePm1604.setRevisions(('2016-05-23 00:00','2017-02-08 00:00'))
class Pm1604OtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pm1604LineChannel(TextualConvention,Integer32):status=_A
class Pm1604ClientProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('protocol10GBE',1),('protocol8GFC',2),('protocol10GFC',3),('protocol16GFC',4)))
_Pm1604alarms_ObjectIdentity=ObjectIdentity
pm1604alarms=_Pm1604alarms_ObjectIdentity((1,3,6,1,4,1,20044,77,2))
_Pm1604AlmOther_ObjectIdentity=ObjectIdentity
pm1604AlmOther=_Pm1604AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,77,2,1))
_Pm1604AlmOtherNurg_ObjectIdentity=ObjectIdentity
pm1604AlmOtherNurg=_Pm1604AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,77,2,1,1))
_Pm1604AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pm1604AlmsynthAlm2=_Pm1604AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,77,2,1,1,2))
_Pm1604AlmConfTableSave_Type=EkiOnOff
_Pm1604AlmConfTableSave_Object=MibScalar
pm1604AlmConfTableSave=_Pm1604AlmConfTableSave_Object((1,3,6,1,4,1,20044,77,2,1,1,2,1),_Pm1604AlmConfTableSave_Type())
pm1604AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmConfTableSave.setStatus(_A)
_Pm1604AlmInvUpload_Type=EkiOnOff
_Pm1604AlmInvUpload_Object=MibScalar
pm1604AlmInvUpload=_Pm1604AlmInvUpload_Object((1,3,6,1,4,1,20044,77,2,1,1,2,2),_Pm1604AlmInvUpload_Type())
pm1604AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmInvUpload.setStatus(_A)
_Pm1604AlmConfTableLoad_Type=EkiOnOff
_Pm1604AlmConfTableLoad_Object=MibScalar
pm1604AlmConfTableLoad=_Pm1604AlmConfTableLoad_Object((1,3,6,1,4,1,20044,77,2,1,1,2,3),_Pm1604AlmConfTableLoad_Type())
pm1604AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmConfTableLoad.setStatus(_A)
_Pm1604AlmCorrelatOff_Type=EkiOnOff
_Pm1604AlmCorrelatOff_Object=MibScalar
pm1604AlmCorrelatOff=_Pm1604AlmCorrelatOff_Object((1,3,6,1,4,1,20044,77,2,1,1,2,4),_Pm1604AlmCorrelatOff_Type())
pm1604AlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmCorrelatOff.setStatus(_A)
_Pm1604AlmOtherUrg_ObjectIdentity=ObjectIdentity
pm1604AlmOtherUrg=_Pm1604AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,77,2,1,2))
_Pm1604AlmOtherCrit_ObjectIdentity=ObjectIdentity
pm1604AlmOtherCrit=_Pm1604AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,77,2,1,3))
_Pm1604AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm1604AlmsynthAlm0=_Pm1604AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,77,2,1,3,0))
_Pm1604AlmModuleGlobFailure_Type=EkiOnOff
_Pm1604AlmModuleGlobFailure_Object=MibScalar
pm1604AlmModuleGlobFailure=_Pm1604AlmModuleGlobFailure_Object((1,3,6,1,4,1,20044,77,2,1,3,0,9),_Pm1604AlmModuleGlobFailure_Type())
pm1604AlmModuleGlobFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmModuleGlobFailure.setStatus(_A)
_Pm1604AlmDefFuseA_Type=EkiOnOff
_Pm1604AlmDefFuseA_Object=MibScalar
pm1604AlmDefFuseA=_Pm1604AlmDefFuseA_Object((1,3,6,1,4,1,20044,77,2,1,3,0,15),_Pm1604AlmDefFuseA_Type())
pm1604AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmDefFuseA.setStatus(_A)
_Pm1604AlmDefFuseB_Type=EkiOnOff
_Pm1604AlmDefFuseB_Object=MibScalar
pm1604AlmDefFuseB=_Pm1604AlmDefFuseB_Object((1,3,6,1,4,1,20044,77,2,1,3,0,16),_Pm1604AlmDefFuseB_Type())
pm1604AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmDefFuseB.setStatus(_A)
_Pm1604AlmClient_ObjectIdentity=ObjectIdentity
pm1604AlmClient=_Pm1604AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,77,2,2))
_Pm1604AlmClientNurg_ObjectIdentity=ObjectIdentity
pm1604AlmClientNurg=_Pm1604AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,77,2,2,1))
_Pm1604Almline1SfpWarnDdmTable_Object=MibTable
pm1604Almline1SfpWarnDdmTable=_Pm1604Almline1SfpWarnDdmTable_Object((1,3,6,1,4,1,20044,77,2,2,1,32))
if mibBuilder.loadTexts:pm1604Almline1SfpWarnDdmTable.setStatus(_A)
_Pm1604Almline1SfpWarnDdmEntry_Object=MibTableRow
pm1604Almline1SfpWarnDdmEntry=_Pm1604Almline1SfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1))
pm1604Almline1SfpWarnDdmEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pm1604Almline1SfpWarnDdmEntry.setStatus(_A)
class _Pm1604Almline1SfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Almline1SfpWarnDdmIndex_Type.__name__=_D
_Pm1604Almline1SfpWarnDdmIndex_Object=MibTableColumn
pm1604Almline1SfpWarnDdmIndex=_Pm1604Almline1SfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,1),_Pm1604Almline1SfpWarnDdmIndex_Type())
pm1604Almline1SfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Almline1SfpWarnDdmIndex.setStatus(_A)
_Pm1604AlmLine1TxPwLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine1TxPwLowWngPortn_Object=MibTableColumn
pm1604AlmLine1TxPwLowWngPortn=_Pm1604AlmLine1TxPwLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,2),_Pm1604AlmLine1TxPwLowWngPortn_Type())
pm1604AlmLine1TxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxPwLowWngPortn.setStatus(_A)
_Pm1604AlmLine1TxPwrHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine1TxPwrHighWngPortn_Object=MibTableColumn
pm1604AlmLine1TxPwrHighWngPortn=_Pm1604AlmLine1TxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,3),_Pm1604AlmLine1TxPwrHighWngPortn_Type())
pm1604AlmLine1TxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxPwrHighWngPortn.setStatus(_A)
_Pm1604AlmLine1TxBiasLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine1TxBiasLowWngPortn_Object=MibTableColumn
pm1604AlmLine1TxBiasLowWngPortn=_Pm1604AlmLine1TxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,4),_Pm1604AlmLine1TxBiasLowWngPortn_Type())
pm1604AlmLine1TxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxBiasLowWngPortn.setStatus(_A)
_Pm1604AlmLine1TxBiasHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine1TxBiasHighWngPortn_Object=MibTableColumn
pm1604AlmLine1TxBiasHighWngPortn=_Pm1604AlmLine1TxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,5),_Pm1604AlmLine1TxBiasHighWngPortn_Type())
pm1604AlmLine1TxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxBiasHighWngPortn.setStatus(_A)
_Pm1604AlmLine1VccLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine1VccLowWngPortn_Object=MibTableColumn
pm1604AlmLine1VccLowWngPortn=_Pm1604AlmLine1VccLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,6),_Pm1604AlmLine1VccLowWngPortn_Type())
pm1604AlmLine1VccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1VccLowWngPortn.setStatus(_A)
_Pm1604AlmLine1VccHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine1VccHighWngPortn_Object=MibTableColumn
pm1604AlmLine1VccHighWngPortn=_Pm1604AlmLine1VccHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,7),_Pm1604AlmLine1VccHighWngPortn_Type())
pm1604AlmLine1VccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1VccHighWngPortn.setStatus(_A)
_Pm1604AlmLine1TempLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine1TempLowWngPortn_Object=MibTableColumn
pm1604AlmLine1TempLowWngPortn=_Pm1604AlmLine1TempLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,8),_Pm1604AlmLine1TempLowWngPortn_Type())
pm1604AlmLine1TempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TempLowWngPortn.setStatus(_A)
_Pm1604AlmLine1TempHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine1TempHighWngPortn_Object=MibTableColumn
pm1604AlmLine1TempHighWngPortn=_Pm1604AlmLine1TempHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,9),_Pm1604AlmLine1TempHighWngPortn_Type())
pm1604AlmLine1TempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TempHighWngPortn.setStatus(_A)
_Pm1604AlmLine1RxPwrLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine1RxPwrLowWngPortn_Object=MibTableColumn
pm1604AlmLine1RxPwrLowWngPortn=_Pm1604AlmLine1RxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,16),_Pm1604AlmLine1RxPwrLowWngPortn_Type())
pm1604AlmLine1RxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1RxPwrLowWngPortn.setStatus(_A)
_Pm1604AlmLine1RxPwrHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine1RxPwrHighWngPortn_Object=MibTableColumn
pm1604AlmLine1RxPwrHighWngPortn=_Pm1604AlmLine1RxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,2,1,32,1,17),_Pm1604AlmLine1RxPwrHighWngPortn_Type())
pm1604AlmLine1RxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1RxPwrHighWngPortn.setStatus(_A)
_Pm1604AlmClientUrg_ObjectIdentity=ObjectIdentity
pm1604AlmClientUrg=_Pm1604AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,77,2,2,2))
_Pm1604Almline1SfpAlmDdmTable_Object=MibTable
pm1604Almline1SfpAlmDdmTable=_Pm1604Almline1SfpAlmDdmTable_Object((1,3,6,1,4,1,20044,77,2,2,2,24))
if mibBuilder.loadTexts:pm1604Almline1SfpAlmDdmTable.setStatus(_A)
_Pm1604Almline1SfpAlmDdmEntry_Object=MibTableRow
pm1604Almline1SfpAlmDdmEntry=_Pm1604Almline1SfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1))
pm1604Almline1SfpAlmDdmEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pm1604Almline1SfpAlmDdmEntry.setStatus(_A)
class _Pm1604Almline1SfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Almline1SfpAlmDdmIndex_Type.__name__=_D
_Pm1604Almline1SfpAlmDdmIndex_Object=MibTableColumn
pm1604Almline1SfpAlmDdmIndex=_Pm1604Almline1SfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,1),_Pm1604Almline1SfpAlmDdmIndex_Type())
pm1604Almline1SfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Almline1SfpAlmDdmIndex.setStatus(_A)
_Pm1604AlmLine1TxPwrLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1TxPwrLowAlaPortn_Object=MibTableColumn
pm1604AlmLine1TxPwrLowAlaPortn=_Pm1604AlmLine1TxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,2),_Pm1604AlmLine1TxPwrLowAlaPortn_Type())
pm1604AlmLine1TxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxPwrLowAlaPortn.setStatus(_A)
_Pm1604AlmLine1Line1TxPwrHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1Line1TxPwrHighAlaPortn_Object=MibTableColumn
pm1604AlmLine1Line1TxPwrHighAlaPortn=_Pm1604AlmLine1Line1TxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,3),_Pm1604AlmLine1Line1TxPwrHighAlaPortn_Type())
pm1604AlmLine1Line1TxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1Line1TxPwrHighAlaPortn.setStatus(_A)
_Pm1604AlmLine1TxBiasLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1TxBiasLowAlaPortn_Object=MibTableColumn
pm1604AlmLine1TxBiasLowAlaPortn=_Pm1604AlmLine1TxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,4),_Pm1604AlmLine1TxBiasLowAlaPortn_Type())
pm1604AlmLine1TxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxBiasLowAlaPortn.setStatus(_A)
_Pm1604AlmLine1TxBiasHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1TxBiasHighAlaPortn_Object=MibTableColumn
pm1604AlmLine1TxBiasHighAlaPortn=_Pm1604AlmLine1TxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,5),_Pm1604AlmLine1TxBiasHighAlaPortn_Type())
pm1604AlmLine1TxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TxBiasHighAlaPortn.setStatus(_A)
_Pm1604AlmLine1VccLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1VccLowAlaPortn_Object=MibTableColumn
pm1604AlmLine1VccLowAlaPortn=_Pm1604AlmLine1VccLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,6),_Pm1604AlmLine1VccLowAlaPortn_Type())
pm1604AlmLine1VccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1VccLowAlaPortn.setStatus(_A)
_Pm1604AlmLine1VccHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1VccHighAlaPortn_Object=MibTableColumn
pm1604AlmLine1VccHighAlaPortn=_Pm1604AlmLine1VccHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,7),_Pm1604AlmLine1VccHighAlaPortn_Type())
pm1604AlmLine1VccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1VccHighAlaPortn.setStatus(_A)
_Pm1604AlmLine1TempLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1TempLowAlaPortn_Object=MibTableColumn
pm1604AlmLine1TempLowAlaPortn=_Pm1604AlmLine1TempLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,8),_Pm1604AlmLine1TempLowAlaPortn_Type())
pm1604AlmLine1TempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TempLowAlaPortn.setStatus(_A)
_Pm1604AlmLine1TempHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1TempHighAlaPortn_Object=MibTableColumn
pm1604AlmLine1TempHighAlaPortn=_Pm1604AlmLine1TempHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,9),_Pm1604AlmLine1TempHighAlaPortn_Type())
pm1604AlmLine1TempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1TempHighAlaPortn.setStatus(_A)
_Pm1604AlmLine1RxPwrLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1RxPwrLowAlaPortn_Object=MibTableColumn
pm1604AlmLine1RxPwrLowAlaPortn=_Pm1604AlmLine1RxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,16),_Pm1604AlmLine1RxPwrLowAlaPortn_Type())
pm1604AlmLine1RxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1RxPwrLowAlaPortn.setStatus(_A)
_Pm1604AlmLine1RxPwrHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine1RxPwrHighAlaPortn_Object=MibTableColumn
pm1604AlmLine1RxPwrHighAlaPortn=_Pm1604AlmLine1RxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,2,2,24,1,17),_Pm1604AlmLine1RxPwrHighAlaPortn_Type())
pm1604AlmLine1RxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1RxPwrHighAlaPortn.setStatus(_A)
_Pm1604AlmClientCrit_ObjectIdentity=ObjectIdentity
pm1604AlmClientCrit=_Pm1604AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,77,2,2,3))
_Pm1604AlmsynthAlmLine1Table_Object=MibTable
pm1604AlmsynthAlmLine1Table=_Pm1604AlmsynthAlmLine1Table_Object((1,3,6,1,4,1,20044,77,2,2,3,8))
if mibBuilder.loadTexts:pm1604AlmsynthAlmLine1Table.setStatus(_A)
_Pm1604AlmsynthAlmLine1Entry_Object=MibTableRow
pm1604AlmsynthAlmLine1Entry=_Pm1604AlmsynthAlmLine1Entry_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1))
pm1604AlmsynthAlmLine1Entry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:pm1604AlmsynthAlmLine1Entry.setStatus(_A)
class _Pm1604AlmsynthAlmLine1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604AlmsynthAlmLine1Index_Type.__name__=_D
_Pm1604AlmsynthAlmLine1Index_Object=MibTableColumn
pm1604AlmsynthAlmLine1Index=_Pm1604AlmsynthAlmLine1Index_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,1),_Pm1604AlmsynthAlmLine1Index_Type())
pm1604AlmsynthAlmLine1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmsynthAlmLine1Index.setStatus(_A)
_Pm1604AlmLine1SfpAbsentPortn_Type=EkiOnOff
_Pm1604AlmLine1SfpAbsentPortn_Object=MibTableColumn
pm1604AlmLine1SfpAbsentPortn=_Pm1604AlmLine1SfpAbsentPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,2),_Pm1604AlmLine1SfpAbsentPortn_Type())
pm1604AlmLine1SfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1SfpAbsentPortn.setStatus(_A)
_Pm1604AlmLine1DdmAbsentPortn_Type=EkiOnOff
_Pm1604AlmLine1DdmAbsentPortn_Object=MibTableColumn
pm1604AlmLine1DdmAbsentPortn=_Pm1604AlmLine1DdmAbsentPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,3),_Pm1604AlmLine1DdmAbsentPortn_Type())
pm1604AlmLine1DdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1DdmAbsentPortn.setStatus(_A)
_Pm1604AlmLine1HwFailAccPortn_Type=EkiOnOff
_Pm1604AlmLine1HwFailAccPortn_Object=MibTableColumn
pm1604AlmLine1HwFailAccPortn=_Pm1604AlmLine1HwFailAccPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,5),_Pm1604AlmLine1HwFailAccPortn_Type())
pm1604AlmLine1HwFailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1HwFailAccPortn.setStatus(_A)
_Pm1604AlmLine1LsdPortn_Type=EkiOnOff
_Pm1604AlmLine1LsdPortn_Object=MibTableColumn
pm1604AlmLine1LsdPortn=_Pm1604AlmLine1LsdPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,6),_Pm1604AlmLine1LsdPortn_Type())
pm1604AlmLine1LsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1LsdPortn.setStatus(_A)
_Pm1604AlmLine1LocalOosPortn_Type=EkiOnOff
_Pm1604AlmLine1LocalOosPortn_Object=MibTableColumn
pm1604AlmLine1LocalOosPortn=_Pm1604AlmLine1LocalOosPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,7),_Pm1604AlmLine1LocalOosPortn_Type())
pm1604AlmLine1LocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1LocalOosPortn.setStatus(_A)
_Pm1604AlmLine1DwCaisPortn_Type=EkiOnOff
_Pm1604AlmLine1DwCaisPortn_Object=MibTableColumn
pm1604AlmLine1DwCaisPortn=_Pm1604AlmLine1DwCaisPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,9),_Pm1604AlmLine1DwCaisPortn_Type())
pm1604AlmLine1DwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1DwCaisPortn.setStatus(_A)
_Pm1604AlmLine1SfpDdmWarningPortn_Type=EkiOnOff
_Pm1604AlmLine1SfpDdmWarningPortn_Object=MibTableColumn
pm1604AlmLine1SfpDdmWarningPortn=_Pm1604AlmLine1SfpDdmWarningPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,10),_Pm1604AlmLine1SfpDdmWarningPortn_Type())
pm1604AlmLine1SfpDdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1SfpDdmWarningPortn.setStatus(_A)
_Pm1604AlmLine1SfpDdmAlmPortn_Type=EkiOnOff
_Pm1604AlmLine1SfpDdmAlmPortn_Object=MibTableColumn
pm1604AlmLine1SfpDdmAlmPortn=_Pm1604AlmLine1SfpDdmAlmPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,11),_Pm1604AlmLine1SfpDdmAlmPortn_Type())
pm1604AlmLine1SfpDdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1SfpDdmAlmPortn.setStatus(_A)
_Pm1604AlmLine1FailAccPortn_Type=EkiOnOff
_Pm1604AlmLine1FailAccPortn_Object=MibTableColumn
pm1604AlmLine1FailAccPortn=_Pm1604AlmLine1FailAccPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,8,1,13),_Pm1604AlmLine1FailAccPortn_Type())
pm1604AlmLine1FailAccPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1FailAccPortn.setStatus(_A)
_Pm1604Almline1AccessioAlmTable_Object=MibTable
pm1604Almline1AccessioAlmTable=_Pm1604Almline1AccessioAlmTable_Object((1,3,6,1,4,1,20044,77,2,2,3,16))
if mibBuilder.loadTexts:pm1604Almline1AccessioAlmTable.setStatus(_A)
_Pm1604Almline1AccessioAlmEntry_Object=MibTableRow
pm1604Almline1AccessioAlmEntry=_Pm1604Almline1AccessioAlmEntry_Object((1,3,6,1,4,1,20044,77,2,2,3,16,1))
pm1604Almline1AccessioAlmEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:pm1604Almline1AccessioAlmEntry.setStatus(_A)
class _Pm1604Almline1AccessioAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Almline1AccessioAlmIndex_Type.__name__=_D
_Pm1604Almline1AccessioAlmIndex_Object=MibTableColumn
pm1604Almline1AccessioAlmIndex=_Pm1604Almline1AccessioAlmIndex_Object((1,3,6,1,4,1,20044,77,2,2,3,16,1,1),_Pm1604Almline1AccessioAlmIndex_Type())
pm1604Almline1AccessioAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Almline1AccessioAlmIndex.setStatus(_A)
_Pm1604AlmLine1LasFailPortn_Type=EkiOnOff
_Pm1604AlmLine1LasFailPortn_Object=MibTableColumn
pm1604AlmLine1LasFailPortn=_Pm1604AlmLine1LasFailPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,16,1,2),_Pm1604AlmLine1LasFailPortn_Type())
pm1604AlmLine1LasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1LasFailPortn.setStatus(_A)
_Pm1604AlmLine1LosPortn_Type=EkiOnOff
_Pm1604AlmLine1LosPortn_Object=MibTableColumn
pm1604AlmLine1LosPortn=_Pm1604AlmLine1LosPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,16,1,5),_Pm1604AlmLine1LosPortn_Type())
pm1604AlmLine1LosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1LosPortn.setStatus(_A)
_Pm1604AlmLine1LosCdrPortn_Type=EkiOnOff
_Pm1604AlmLine1LosCdrPortn_Object=MibTableColumn
pm1604AlmLine1LosCdrPortn=_Pm1604AlmLine1LosCdrPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,16,1,7),_Pm1604AlmLine1LosCdrPortn_Type())
pm1604AlmLine1LosCdrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1LosCdrPortn.setStatus(_A)
_Pm1604AlmLine1ErrSigCdrPortn_Type=EkiOnOff
_Pm1604AlmLine1ErrSigCdrPortn_Object=MibTableColumn
pm1604AlmLine1ErrSigCdrPortn=_Pm1604AlmLine1ErrSigCdrPortn_Object((1,3,6,1,4,1,20044,77,2,2,3,16,1,8),_Pm1604AlmLine1ErrSigCdrPortn_Type())
pm1604AlmLine1ErrSigCdrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine1ErrSigCdrPortn.setStatus(_A)
_Pm1604AlmLine_ObjectIdentity=ObjectIdentity
pm1604AlmLine=_Pm1604AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,77,2,3))
_Pm1604AlmLineNurg_ObjectIdentity=ObjectIdentity
pm1604AlmLineNurg=_Pm1604AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,77,2,3,1))
_Pm1604Almline2SfpWarnDdmTable_Object=MibTable
pm1604Almline2SfpWarnDdmTable=_Pm1604Almline2SfpWarnDdmTable_Object((1,3,6,1,4,1,20044,77,2,3,1,36))
if mibBuilder.loadTexts:pm1604Almline2SfpWarnDdmTable.setStatus(_A)
_Pm1604Almline2SfpWarnDdmEntry_Object=MibTableRow
pm1604Almline2SfpWarnDdmEntry=_Pm1604Almline2SfpWarnDdmEntry_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1))
pm1604Almline2SfpWarnDdmEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:pm1604Almline2SfpWarnDdmEntry.setStatus(_A)
class _Pm1604Almline2SfpWarnDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Almline2SfpWarnDdmIndex_Type.__name__=_D
_Pm1604Almline2SfpWarnDdmIndex_Object=MibTableColumn
pm1604Almline2SfpWarnDdmIndex=_Pm1604Almline2SfpWarnDdmIndex_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,1),_Pm1604Almline2SfpWarnDdmIndex_Type())
pm1604Almline2SfpWarnDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Almline2SfpWarnDdmIndex.setStatus(_A)
_Pm1604AlmLine2TxPwLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine2TxPwLowWngPortn_Object=MibTableColumn
pm1604AlmLine2TxPwLowWngPortn=_Pm1604AlmLine2TxPwLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,2),_Pm1604AlmLine2TxPwLowWngPortn_Type())
pm1604AlmLine2TxPwLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxPwLowWngPortn.setStatus(_A)
_Pm1604AlmLine2TxPwrHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine2TxPwrHighWngPortn_Object=MibTableColumn
pm1604AlmLine2TxPwrHighWngPortn=_Pm1604AlmLine2TxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,3),_Pm1604AlmLine2TxPwrHighWngPortn_Type())
pm1604AlmLine2TxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxPwrHighWngPortn.setStatus(_A)
_Pm1604AlmLine2TxBiasLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine2TxBiasLowWngPortn_Object=MibTableColumn
pm1604AlmLine2TxBiasLowWngPortn=_Pm1604AlmLine2TxBiasLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,4),_Pm1604AlmLine2TxBiasLowWngPortn_Type())
pm1604AlmLine2TxBiasLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxBiasLowWngPortn.setStatus(_A)
_Pm1604AlmLine2TxBiasHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine2TxBiasHighWngPortn_Object=MibTableColumn
pm1604AlmLine2TxBiasHighWngPortn=_Pm1604AlmLine2TxBiasHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,5),_Pm1604AlmLine2TxBiasHighWngPortn_Type())
pm1604AlmLine2TxBiasHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxBiasHighWngPortn.setStatus(_A)
_Pm1604AlmLine2VccLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine2VccLowWngPortn_Object=MibTableColumn
pm1604AlmLine2VccLowWngPortn=_Pm1604AlmLine2VccLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,6),_Pm1604AlmLine2VccLowWngPortn_Type())
pm1604AlmLine2VccLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2VccLowWngPortn.setStatus(_A)
_Pm1604AlmLine2VccHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine2VccHighWngPortn_Object=MibTableColumn
pm1604AlmLine2VccHighWngPortn=_Pm1604AlmLine2VccHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,7),_Pm1604AlmLine2VccHighWngPortn_Type())
pm1604AlmLine2VccHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2VccHighWngPortn.setStatus(_A)
_Pm1604AlmLine2TempLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine2TempLowWngPortn_Object=MibTableColumn
pm1604AlmLine2TempLowWngPortn=_Pm1604AlmLine2TempLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,8),_Pm1604AlmLine2TempLowWngPortn_Type())
pm1604AlmLine2TempLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TempLowWngPortn.setStatus(_A)
_Pm1604AlmLine2TempHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine2TempHighWngPortn_Object=MibTableColumn
pm1604AlmLine2TempHighWngPortn=_Pm1604AlmLine2TempHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,9),_Pm1604AlmLine2TempHighWngPortn_Type())
pm1604AlmLine2TempHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TempHighWngPortn.setStatus(_A)
_Pm1604AlmLine2RxPwrLowWngPortn_Type=EkiOnOff
_Pm1604AlmLine2RxPwrLowWngPortn_Object=MibTableColumn
pm1604AlmLine2RxPwrLowWngPortn=_Pm1604AlmLine2RxPwrLowWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,16),_Pm1604AlmLine2RxPwrLowWngPortn_Type())
pm1604AlmLine2RxPwrLowWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2RxPwrLowWngPortn.setStatus(_A)
_Pm1604AlmLine2RxPwrHighWngPortn_Type=EkiOnOff
_Pm1604AlmLine2RxPwrHighWngPortn_Object=MibTableColumn
pm1604AlmLine2RxPwrHighWngPortn=_Pm1604AlmLine2RxPwrHighWngPortn_Object((1,3,6,1,4,1,20044,77,2,3,1,36,1,17),_Pm1604AlmLine2RxPwrHighWngPortn_Type())
pm1604AlmLine2RxPwrHighWngPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2RxPwrHighWngPortn.setStatus(_A)
_Pm1604AlmLineUrg_ObjectIdentity=ObjectIdentity
pm1604AlmLineUrg=_Pm1604AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,77,2,3,2))
_Pm1604Almline2SfpAlmDdmTable_Object=MibTable
pm1604Almline2SfpAlmDdmTable=_Pm1604Almline2SfpAlmDdmTable_Object((1,3,6,1,4,1,20044,77,2,3,2,28))
if mibBuilder.loadTexts:pm1604Almline2SfpAlmDdmTable.setStatus(_A)
_Pm1604Almline2SfpAlmDdmEntry_Object=MibTableRow
pm1604Almline2SfpAlmDdmEntry=_Pm1604Almline2SfpAlmDdmEntry_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1))
pm1604Almline2SfpAlmDdmEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:pm1604Almline2SfpAlmDdmEntry.setStatus(_A)
class _Pm1604Almline2SfpAlmDdmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Almline2SfpAlmDdmIndex_Type.__name__=_D
_Pm1604Almline2SfpAlmDdmIndex_Object=MibTableColumn
pm1604Almline2SfpAlmDdmIndex=_Pm1604Almline2SfpAlmDdmIndex_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,1),_Pm1604Almline2SfpAlmDdmIndex_Type())
pm1604Almline2SfpAlmDdmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Almline2SfpAlmDdmIndex.setStatus(_A)
_Pm1604AlmLine2TxPwrLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2TxPwrLowAlaPortn_Object=MibTableColumn
pm1604AlmLine2TxPwrLowAlaPortn=_Pm1604AlmLine2TxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,2),_Pm1604AlmLine2TxPwrLowAlaPortn_Type())
pm1604AlmLine2TxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxPwrLowAlaPortn.setStatus(_A)
_Pm1604AlmLine2Line2TxPwrHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2Line2TxPwrHighAlaPortn_Object=MibTableColumn
pm1604AlmLine2Line2TxPwrHighAlaPortn=_Pm1604AlmLine2Line2TxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,3),_Pm1604AlmLine2Line2TxPwrHighAlaPortn_Type())
pm1604AlmLine2Line2TxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2Line2TxPwrHighAlaPortn.setStatus(_A)
_Pm1604AlmLine2TxBiasLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2TxBiasLowAlaPortn_Object=MibTableColumn
pm1604AlmLine2TxBiasLowAlaPortn=_Pm1604AlmLine2TxBiasLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,4),_Pm1604AlmLine2TxBiasLowAlaPortn_Type())
pm1604AlmLine2TxBiasLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxBiasLowAlaPortn.setStatus(_A)
_Pm1604AlmLine2TxBiasHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2TxBiasHighAlaPortn_Object=MibTableColumn
pm1604AlmLine2TxBiasHighAlaPortn=_Pm1604AlmLine2TxBiasHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,5),_Pm1604AlmLine2TxBiasHighAlaPortn_Type())
pm1604AlmLine2TxBiasHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TxBiasHighAlaPortn.setStatus(_A)
_Pm1604AlmLine2VccLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2VccLowAlaPortn_Object=MibTableColumn
pm1604AlmLine2VccLowAlaPortn=_Pm1604AlmLine2VccLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,6),_Pm1604AlmLine2VccLowAlaPortn_Type())
pm1604AlmLine2VccLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2VccLowAlaPortn.setStatus(_A)
_Pm1604AlmLine2VccHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2VccHighAlaPortn_Object=MibTableColumn
pm1604AlmLine2VccHighAlaPortn=_Pm1604AlmLine2VccHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,7),_Pm1604AlmLine2VccHighAlaPortn_Type())
pm1604AlmLine2VccHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2VccHighAlaPortn.setStatus(_A)
_Pm1604AlmLine2TempLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2TempLowAlaPortn_Object=MibTableColumn
pm1604AlmLine2TempLowAlaPortn=_Pm1604AlmLine2TempLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,8),_Pm1604AlmLine2TempLowAlaPortn_Type())
pm1604AlmLine2TempLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TempLowAlaPortn.setStatus(_A)
_Pm1604AlmLine2TempHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2TempHighAlaPortn_Object=MibTableColumn
pm1604AlmLine2TempHighAlaPortn=_Pm1604AlmLine2TempHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,9),_Pm1604AlmLine2TempHighAlaPortn_Type())
pm1604AlmLine2TempHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2TempHighAlaPortn.setStatus(_A)
_Pm1604AlmLine2RxPwrLowAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2RxPwrLowAlaPortn_Object=MibTableColumn
pm1604AlmLine2RxPwrLowAlaPortn=_Pm1604AlmLine2RxPwrLowAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,16),_Pm1604AlmLine2RxPwrLowAlaPortn_Type())
pm1604AlmLine2RxPwrLowAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2RxPwrLowAlaPortn.setStatus(_A)
_Pm1604AlmLine2RxPwrHighAlaPortn_Type=EkiOnOff
_Pm1604AlmLine2RxPwrHighAlaPortn_Object=MibTableColumn
pm1604AlmLine2RxPwrHighAlaPortn=_Pm1604AlmLine2RxPwrHighAlaPortn_Object((1,3,6,1,4,1,20044,77,2,3,2,28,1,17),_Pm1604AlmLine2RxPwrHighAlaPortn_Type())
pm1604AlmLine2RxPwrHighAlaPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2RxPwrHighAlaPortn.setStatus(_A)
_Pm1604AlmLineCrit_ObjectIdentity=ObjectIdentity
pm1604AlmLineCrit=_Pm1604AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,77,2,3,3))
_Pm1604AlmsynthAlmLine2Table_Object=MibTable
pm1604AlmsynthAlmLine2Table=_Pm1604AlmsynthAlmLine2Table_Object((1,3,6,1,4,1,20044,77,2,3,3,12))
if mibBuilder.loadTexts:pm1604AlmsynthAlmLine2Table.setStatus(_A)
_Pm1604AlmsynthAlmLine2Entry_Object=MibTableRow
pm1604AlmsynthAlmLine2Entry=_Pm1604AlmsynthAlmLine2Entry_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1))
pm1604AlmsynthAlmLine2Entry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:pm1604AlmsynthAlmLine2Entry.setStatus(_A)
class _Pm1604AlmsynthAlmLine2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604AlmsynthAlmLine2Index_Type.__name__=_D
_Pm1604AlmsynthAlmLine2Index_Object=MibTableColumn
pm1604AlmsynthAlmLine2Index=_Pm1604AlmsynthAlmLine2Index_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,1),_Pm1604AlmsynthAlmLine2Index_Type())
pm1604AlmsynthAlmLine2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmsynthAlmLine2Index.setStatus(_A)
_Pm1604AlmLine2SfpAbsentPortn_Type=EkiOnOff
_Pm1604AlmLine2SfpAbsentPortn_Object=MibTableColumn
pm1604AlmLine2SfpAbsentPortn=_Pm1604AlmLine2SfpAbsentPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,2),_Pm1604AlmLine2SfpAbsentPortn_Type())
pm1604AlmLine2SfpAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2SfpAbsentPortn.setStatus(_A)
_Pm1604AlmLine2DdmAbsentPortn_Type=EkiOnOff
_Pm1604AlmLine2DdmAbsentPortn_Object=MibTableColumn
pm1604AlmLine2DdmAbsentPortn=_Pm1604AlmLine2DdmAbsentPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,3),_Pm1604AlmLine2DdmAbsentPortn_Type())
pm1604AlmLine2DdmAbsentPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2DdmAbsentPortn.setStatus(_A)
_Pm1604AlmLine2HwFailPortn_Type=EkiOnOff
_Pm1604AlmLine2HwFailPortn_Object=MibTableColumn
pm1604AlmLine2HwFailPortn=_Pm1604AlmLine2HwFailPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,5),_Pm1604AlmLine2HwFailPortn_Type())
pm1604AlmLine2HwFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2HwFailPortn.setStatus(_A)
_Pm1604AlmLine2LsdPortn_Type=EkiOnOff
_Pm1604AlmLine2LsdPortn_Object=MibTableColumn
pm1604AlmLine2LsdPortn=_Pm1604AlmLine2LsdPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,6),_Pm1604AlmLine2LsdPortn_Type())
pm1604AlmLine2LsdPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2LsdPortn.setStatus(_A)
_Pm1604AlmLine2LocalOosPortn_Type=EkiOnOff
_Pm1604AlmLine2LocalOosPortn_Object=MibTableColumn
pm1604AlmLine2LocalOosPortn=_Pm1604AlmLine2LocalOosPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,7),_Pm1604AlmLine2LocalOosPortn_Type())
pm1604AlmLine2LocalOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2LocalOosPortn.setStatus(_A)
_Pm1604AlmLine2DwCaisPortn_Type=EkiOnOff
_Pm1604AlmLine2DwCaisPortn_Object=MibTableColumn
pm1604AlmLine2DwCaisPortn=_Pm1604AlmLine2DwCaisPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,9),_Pm1604AlmLine2DwCaisPortn_Type())
pm1604AlmLine2DwCaisPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2DwCaisPortn.setStatus(_A)
_Pm1604AlmLine2DdmWarningPortn_Type=EkiOnOff
_Pm1604AlmLine2DdmWarningPortn_Object=MibTableColumn
pm1604AlmLine2DdmWarningPortn=_Pm1604AlmLine2DdmWarningPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,10),_Pm1604AlmLine2DdmWarningPortn_Type())
pm1604AlmLine2DdmWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2DdmWarningPortn.setStatus(_A)
_Pm1604AlmLine2DdmAlmPortn_Type=EkiOnOff
_Pm1604AlmLine2DdmAlmPortn_Object=MibTableColumn
pm1604AlmLine2DdmAlmPortn=_Pm1604AlmLine2DdmAlmPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,11),_Pm1604AlmLine2DdmAlmPortn_Type())
pm1604AlmLine2DdmAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2DdmAlmPortn.setStatus(_A)
_Pm1604AlmLine2FailPortn_Type=EkiOnOff
_Pm1604AlmLine2FailPortn_Object=MibTableColumn
pm1604AlmLine2FailPortn=_Pm1604AlmLine2FailPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,12,1,13),_Pm1604AlmLine2FailPortn_Type())
pm1604AlmLine2FailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2FailPortn.setStatus(_A)
_Pm1604Almline2AccessioAlmTable_Object=MibTable
pm1604Almline2AccessioAlmTable=_Pm1604Almline2AccessioAlmTable_Object((1,3,6,1,4,1,20044,77,2,3,3,20))
if mibBuilder.loadTexts:pm1604Almline2AccessioAlmTable.setStatus(_A)
_Pm1604Almline2AccessioAlmEntry_Object=MibTableRow
pm1604Almline2AccessioAlmEntry=_Pm1604Almline2AccessioAlmEntry_Object((1,3,6,1,4,1,20044,77,2,3,3,20,1))
pm1604Almline2AccessioAlmEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:pm1604Almline2AccessioAlmEntry.setStatus(_A)
class _Pm1604Almline2AccessioAlmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Almline2AccessioAlmIndex_Type.__name__=_D
_Pm1604Almline2AccessioAlmIndex_Object=MibTableColumn
pm1604Almline2AccessioAlmIndex=_Pm1604Almline2AccessioAlmIndex_Object((1,3,6,1,4,1,20044,77,2,3,3,20,1,1),_Pm1604Almline2AccessioAlmIndex_Type())
pm1604Almline2AccessioAlmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Almline2AccessioAlmIndex.setStatus(_A)
_Pm1604AlmLine2LasFailPortn_Type=EkiOnOff
_Pm1604AlmLine2LasFailPortn_Object=MibTableColumn
pm1604AlmLine2LasFailPortn=_Pm1604AlmLine2LasFailPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,20,1,2),_Pm1604AlmLine2LasFailPortn_Type())
pm1604AlmLine2LasFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2LasFailPortn.setStatus(_A)
_Pm1604AlmLine2LosPortn_Type=EkiOnOff
_Pm1604AlmLine2LosPortn_Object=MibTableColumn
pm1604AlmLine2LosPortn=_Pm1604AlmLine2LosPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,20,1,5),_Pm1604AlmLine2LosPortn_Type())
pm1604AlmLine2LosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2LosPortn.setStatus(_A)
_Pm1604AlmLine2LosCdrPortn_Type=EkiOnOff
_Pm1604AlmLine2LosCdrPortn_Object=MibTableColumn
pm1604AlmLine2LosCdrPortn=_Pm1604AlmLine2LosCdrPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,20,1,7),_Pm1604AlmLine2LosCdrPortn_Type())
pm1604AlmLine2LosCdrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2LosCdrPortn.setStatus(_A)
_Pm1604AlmLine2ErrSigCdrPortn_Type=EkiOnOff
_Pm1604AlmLine2ErrSigCdrPortn_Object=MibTableColumn
pm1604AlmLine2ErrSigCdrPortn=_Pm1604AlmLine2ErrSigCdrPortn_Object((1,3,6,1,4,1,20044,77,2,3,3,20,1,8),_Pm1604AlmLine2ErrSigCdrPortn_Type())
pm1604AlmLine2ErrSigCdrPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604AlmLine2ErrSigCdrPortn.setStatus(_A)
_Pm1604measures_ObjectIdentity=ObjectIdentity
pm1604measures=_Pm1604measures_ObjectIdentity((1,3,6,1,4,1,20044,77,3))
_Pm1604MesrOther_ObjectIdentity=ObjectIdentity
pm1604MesrOther=_Pm1604MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,77,3,1))
_Pm1604MesrClient_ObjectIdentity=ObjectIdentity
pm1604MesrClient=_Pm1604MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,77,3,2))
_Pm1604Mesrline1TemperatureTable_Object=MibTable
pm1604Mesrline1TemperatureTable=_Pm1604Mesrline1TemperatureTable_Object((1,3,6,1,4,1,20044,77,3,2,16))
if mibBuilder.loadTexts:pm1604Mesrline1TemperatureTable.setStatus(_A)
_Pm1604Mesrline1TemperatureEntry_Object=MibTableRow
pm1604Mesrline1TemperatureEntry=_Pm1604Mesrline1TemperatureEntry_Object((1,3,6,1,4,1,20044,77,3,2,16,1))
pm1604Mesrline1TemperatureEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:pm1604Mesrline1TemperatureEntry.setStatus(_A)
class _Pm1604Mesrline1TemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline1TemperatureIndex_Type.__name__=_D
_Pm1604Mesrline1TemperatureIndex_Object=MibTableColumn
pm1604Mesrline1TemperatureIndex=_Pm1604Mesrline1TemperatureIndex_Object((1,3,6,1,4,1,20044,77,3,2,16,1,1),_Pm1604Mesrline1TemperatureIndex_Type())
pm1604Mesrline1TemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1TemperatureIndex.setStatus(_A)
class _Pm1604Mesrline1TemperaturePortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline1TemperaturePortn_Type.__name__=_D
_Pm1604Mesrline1TemperaturePortn_Object=MibTableColumn
pm1604Mesrline1TemperaturePortn=_Pm1604Mesrline1TemperaturePortn_Object((1,3,6,1,4,1,20044,77,3,2,16,1,2),_Pm1604Mesrline1TemperaturePortn_Type())
pm1604Mesrline1TemperaturePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1TemperaturePortn.setStatus(_A)
_Pm1604Mesrline1VoltTable_Object=MibTable
pm1604Mesrline1VoltTable=_Pm1604Mesrline1VoltTable_Object((1,3,6,1,4,1,20044,77,3,2,24))
if mibBuilder.loadTexts:pm1604Mesrline1VoltTable.setStatus(_A)
_Pm1604Mesrline1VoltEntry_Object=MibTableRow
pm1604Mesrline1VoltEntry=_Pm1604Mesrline1VoltEntry_Object((1,3,6,1,4,1,20044,77,3,2,24,1))
pm1604Mesrline1VoltEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:pm1604Mesrline1VoltEntry.setStatus(_A)
class _Pm1604Mesrline1VoltIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline1VoltIndex_Type.__name__=_D
_Pm1604Mesrline1VoltIndex_Object=MibTableColumn
pm1604Mesrline1VoltIndex=_Pm1604Mesrline1VoltIndex_Object((1,3,6,1,4,1,20044,77,3,2,24,1,1),_Pm1604Mesrline1VoltIndex_Type())
pm1604Mesrline1VoltIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1VoltIndex.setStatus(_A)
class _Pm1604Mesrline1VoltPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline1VoltPortn_Type.__name__=_D
_Pm1604Mesrline1VoltPortn_Object=MibTableColumn
pm1604Mesrline1VoltPortn=_Pm1604Mesrline1VoltPortn_Object((1,3,6,1,4,1,20044,77,3,2,24,1,2),_Pm1604Mesrline1VoltPortn_Type())
pm1604Mesrline1VoltPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1VoltPortn.setStatus(_A)
_Pm1604Mesrline1TxBiasTable_Object=MibTable
pm1604Mesrline1TxBiasTable=_Pm1604Mesrline1TxBiasTable_Object((1,3,6,1,4,1,20044,77,3,2,32))
if mibBuilder.loadTexts:pm1604Mesrline1TxBiasTable.setStatus(_A)
_Pm1604Mesrline1TxBiasEntry_Object=MibTableRow
pm1604Mesrline1TxBiasEntry=_Pm1604Mesrline1TxBiasEntry_Object((1,3,6,1,4,1,20044,77,3,2,32,1))
pm1604Mesrline1TxBiasEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:pm1604Mesrline1TxBiasEntry.setStatus(_A)
class _Pm1604Mesrline1TxBiasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline1TxBiasIndex_Type.__name__=_D
_Pm1604Mesrline1TxBiasIndex_Object=MibTableColumn
pm1604Mesrline1TxBiasIndex=_Pm1604Mesrline1TxBiasIndex_Object((1,3,6,1,4,1,20044,77,3,2,32,1,1),_Pm1604Mesrline1TxBiasIndex_Type())
pm1604Mesrline1TxBiasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1TxBiasIndex.setStatus(_A)
class _Pm1604Mesrline1TxBiasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline1TxBiasPortn_Type.__name__=_D
_Pm1604Mesrline1TxBiasPortn_Object=MibTableColumn
pm1604Mesrline1TxBiasPortn=_Pm1604Mesrline1TxBiasPortn_Object((1,3,6,1,4,1,20044,77,3,2,32,1,2),_Pm1604Mesrline1TxBiasPortn_Type())
pm1604Mesrline1TxBiasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1TxBiasPortn.setStatus(_A)
_Pm1604Mesrline1TxPowerTable_Object=MibTable
pm1604Mesrline1TxPowerTable=_Pm1604Mesrline1TxPowerTable_Object((1,3,6,1,4,1,20044,77,3,2,40))
if mibBuilder.loadTexts:pm1604Mesrline1TxPowerTable.setStatus(_A)
_Pm1604Mesrline1TxPowerEntry_Object=MibTableRow
pm1604Mesrline1TxPowerEntry=_Pm1604Mesrline1TxPowerEntry_Object((1,3,6,1,4,1,20044,77,3,2,40,1))
pm1604Mesrline1TxPowerEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:pm1604Mesrline1TxPowerEntry.setStatus(_A)
class _Pm1604Mesrline1TxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline1TxPowerIndex_Type.__name__=_D
_Pm1604Mesrline1TxPowerIndex_Object=MibTableColumn
pm1604Mesrline1TxPowerIndex=_Pm1604Mesrline1TxPowerIndex_Object((1,3,6,1,4,1,20044,77,3,2,40,1,1),_Pm1604Mesrline1TxPowerIndex_Type())
pm1604Mesrline1TxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1TxPowerIndex.setStatus(_A)
class _Pm1604Mesrline1TxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline1TxPowerPortn_Type.__name__=_D
_Pm1604Mesrline1TxPowerPortn_Object=MibTableColumn
pm1604Mesrline1TxPowerPortn=_Pm1604Mesrline1TxPowerPortn_Object((1,3,6,1,4,1,20044,77,3,2,40,1,2),_Pm1604Mesrline1TxPowerPortn_Type())
pm1604Mesrline1TxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1TxPowerPortn.setStatus(_A)
_Pm1604Mesrline1RxPowerTable_Object=MibTable
pm1604Mesrline1RxPowerTable=_Pm1604Mesrline1RxPowerTable_Object((1,3,6,1,4,1,20044,77,3,2,48))
if mibBuilder.loadTexts:pm1604Mesrline1RxPowerTable.setStatus(_A)
_Pm1604Mesrline1RxPowerEntry_Object=MibTableRow
pm1604Mesrline1RxPowerEntry=_Pm1604Mesrline1RxPowerEntry_Object((1,3,6,1,4,1,20044,77,3,2,48,1))
pm1604Mesrline1RxPowerEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:pm1604Mesrline1RxPowerEntry.setStatus(_A)
class _Pm1604Mesrline1RxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline1RxPowerIndex_Type.__name__=_D
_Pm1604Mesrline1RxPowerIndex_Object=MibTableColumn
pm1604Mesrline1RxPowerIndex=_Pm1604Mesrline1RxPowerIndex_Object((1,3,6,1,4,1,20044,77,3,2,48,1,1),_Pm1604Mesrline1RxPowerIndex_Type())
pm1604Mesrline1RxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1RxPowerIndex.setStatus(_A)
class _Pm1604Mesrline1RxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline1RxPowerPortn_Type.__name__=_D
_Pm1604Mesrline1RxPowerPortn_Object=MibTableColumn
pm1604Mesrline1RxPowerPortn=_Pm1604Mesrline1RxPowerPortn_Object((1,3,6,1,4,1,20044,77,3,2,48,1,2),_Pm1604Mesrline1RxPowerPortn_Type())
pm1604Mesrline1RxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline1RxPowerPortn.setStatus(_A)
_Pm1604MesrLine_ObjectIdentity=ObjectIdentity
pm1604MesrLine=_Pm1604MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,77,3,3))
_Pm1604Mesrline2TemperatureTable_Object=MibTable
pm1604Mesrline2TemperatureTable=_Pm1604Mesrline2TemperatureTable_Object((1,3,6,1,4,1,20044,77,3,3,20))
if mibBuilder.loadTexts:pm1604Mesrline2TemperatureTable.setStatus(_A)
_Pm1604Mesrline2TemperatureEntry_Object=MibTableRow
pm1604Mesrline2TemperatureEntry=_Pm1604Mesrline2TemperatureEntry_Object((1,3,6,1,4,1,20044,77,3,3,20,1))
pm1604Mesrline2TemperatureEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:pm1604Mesrline2TemperatureEntry.setStatus(_A)
class _Pm1604Mesrline2TemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline2TemperatureIndex_Type.__name__=_D
_Pm1604Mesrline2TemperatureIndex_Object=MibTableColumn
pm1604Mesrline2TemperatureIndex=_Pm1604Mesrline2TemperatureIndex_Object((1,3,6,1,4,1,20044,77,3,3,20,1,1),_Pm1604Mesrline2TemperatureIndex_Type())
pm1604Mesrline2TemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2TemperatureIndex.setStatus(_A)
class _Pm1604Mesrline2TemperaturePortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline2TemperaturePortn_Type.__name__=_D
_Pm1604Mesrline2TemperaturePortn_Object=MibTableColumn
pm1604Mesrline2TemperaturePortn=_Pm1604Mesrline2TemperaturePortn_Object((1,3,6,1,4,1,20044,77,3,3,20,1,2),_Pm1604Mesrline2TemperaturePortn_Type())
pm1604Mesrline2TemperaturePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2TemperaturePortn.setStatus(_A)
_Pm1604Mesrline2VoltTable_Object=MibTable
pm1604Mesrline2VoltTable=_Pm1604Mesrline2VoltTable_Object((1,3,6,1,4,1,20044,77,3,3,28))
if mibBuilder.loadTexts:pm1604Mesrline2VoltTable.setStatus(_A)
_Pm1604Mesrline2VoltEntry_Object=MibTableRow
pm1604Mesrline2VoltEntry=_Pm1604Mesrline2VoltEntry_Object((1,3,6,1,4,1,20044,77,3,3,28,1))
pm1604Mesrline2VoltEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:pm1604Mesrline2VoltEntry.setStatus(_A)
class _Pm1604Mesrline2VoltIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline2VoltIndex_Type.__name__=_D
_Pm1604Mesrline2VoltIndex_Object=MibTableColumn
pm1604Mesrline2VoltIndex=_Pm1604Mesrline2VoltIndex_Object((1,3,6,1,4,1,20044,77,3,3,28,1,1),_Pm1604Mesrline2VoltIndex_Type())
pm1604Mesrline2VoltIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2VoltIndex.setStatus(_A)
class _Pm1604Mesrline2VoltPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline2VoltPortn_Type.__name__=_D
_Pm1604Mesrline2VoltPortn_Object=MibTableColumn
pm1604Mesrline2VoltPortn=_Pm1604Mesrline2VoltPortn_Object((1,3,6,1,4,1,20044,77,3,3,28,1,2),_Pm1604Mesrline2VoltPortn_Type())
pm1604Mesrline2VoltPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2VoltPortn.setStatus(_A)
_Pm1604Mesrline2TxBiasTable_Object=MibTable
pm1604Mesrline2TxBiasTable=_Pm1604Mesrline2TxBiasTable_Object((1,3,6,1,4,1,20044,77,3,3,36))
if mibBuilder.loadTexts:pm1604Mesrline2TxBiasTable.setStatus(_A)
_Pm1604Mesrline2TxBiasEntry_Object=MibTableRow
pm1604Mesrline2TxBiasEntry=_Pm1604Mesrline2TxBiasEntry_Object((1,3,6,1,4,1,20044,77,3,3,36,1))
pm1604Mesrline2TxBiasEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:pm1604Mesrline2TxBiasEntry.setStatus(_A)
class _Pm1604Mesrline2TxBiasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline2TxBiasIndex_Type.__name__=_D
_Pm1604Mesrline2TxBiasIndex_Object=MibTableColumn
pm1604Mesrline2TxBiasIndex=_Pm1604Mesrline2TxBiasIndex_Object((1,3,6,1,4,1,20044,77,3,3,36,1,1),_Pm1604Mesrline2TxBiasIndex_Type())
pm1604Mesrline2TxBiasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2TxBiasIndex.setStatus(_A)
class _Pm1604Mesrline2TxBiasPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline2TxBiasPortn_Type.__name__=_D
_Pm1604Mesrline2TxBiasPortn_Object=MibTableColumn
pm1604Mesrline2TxBiasPortn=_Pm1604Mesrline2TxBiasPortn_Object((1,3,6,1,4,1,20044,77,3,3,36,1,2),_Pm1604Mesrline2TxBiasPortn_Type())
pm1604Mesrline2TxBiasPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2TxBiasPortn.setStatus(_A)
_Pm1604Mesrline2TxPowerTable_Object=MibTable
pm1604Mesrline2TxPowerTable=_Pm1604Mesrline2TxPowerTable_Object((1,3,6,1,4,1,20044,77,3,3,44))
if mibBuilder.loadTexts:pm1604Mesrline2TxPowerTable.setStatus(_A)
_Pm1604Mesrline2TxPowerEntry_Object=MibTableRow
pm1604Mesrline2TxPowerEntry=_Pm1604Mesrline2TxPowerEntry_Object((1,3,6,1,4,1,20044,77,3,3,44,1))
pm1604Mesrline2TxPowerEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:pm1604Mesrline2TxPowerEntry.setStatus(_A)
class _Pm1604Mesrline2TxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline2TxPowerIndex_Type.__name__=_D
_Pm1604Mesrline2TxPowerIndex_Object=MibTableColumn
pm1604Mesrline2TxPowerIndex=_Pm1604Mesrline2TxPowerIndex_Object((1,3,6,1,4,1,20044,77,3,3,44,1,1),_Pm1604Mesrline2TxPowerIndex_Type())
pm1604Mesrline2TxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2TxPowerIndex.setStatus(_A)
class _Pm1604Mesrline2TxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline2TxPowerPortn_Type.__name__=_D
_Pm1604Mesrline2TxPowerPortn_Object=MibTableColumn
pm1604Mesrline2TxPowerPortn=_Pm1604Mesrline2TxPowerPortn_Object((1,3,6,1,4,1,20044,77,3,3,44,1,2),_Pm1604Mesrline2TxPowerPortn_Type())
pm1604Mesrline2TxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2TxPowerPortn.setStatus(_A)
_Pm1604Mesrline2RxPowerTable_Object=MibTable
pm1604Mesrline2RxPowerTable=_Pm1604Mesrline2RxPowerTable_Object((1,3,6,1,4,1,20044,77,3,3,52))
if mibBuilder.loadTexts:pm1604Mesrline2RxPowerTable.setStatus(_A)
_Pm1604Mesrline2RxPowerEntry_Object=MibTableRow
pm1604Mesrline2RxPowerEntry=_Pm1604Mesrline2RxPowerEntry_Object((1,3,6,1,4,1,20044,77,3,3,52,1))
pm1604Mesrline2RxPowerEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:pm1604Mesrline2RxPowerEntry.setStatus(_A)
class _Pm1604Mesrline2RxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Mesrline2RxPowerIndex_Type.__name__=_D
_Pm1604Mesrline2RxPowerIndex_Object=MibTableColumn
pm1604Mesrline2RxPowerIndex=_Pm1604Mesrline2RxPowerIndex_Object((1,3,6,1,4,1,20044,77,3,3,52,1,1),_Pm1604Mesrline2RxPowerIndex_Type())
pm1604Mesrline2RxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2RxPowerIndex.setStatus(_A)
class _Pm1604Mesrline2RxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm1604Mesrline2RxPowerPortn_Type.__name__=_D
_Pm1604Mesrline2RxPowerPortn_Object=MibTableColumn
pm1604Mesrline2RxPowerPortn=_Pm1604Mesrline2RxPowerPortn_Object((1,3,6,1,4,1,20044,77,3,3,52,1,2),_Pm1604Mesrline2RxPowerPortn_Type())
pm1604Mesrline2RxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Mesrline2RxPowerPortn.setStatus(_A)
_Pm1604counters_ObjectIdentity=ObjectIdentity
pm1604counters=_Pm1604counters_ObjectIdentity((1,3,6,1,4,1,20044,77,4))
_Pm1604CntOther_ObjectIdentity=ObjectIdentity
pm1604CntOther=_Pm1604CntOther_ObjectIdentity((1,3,6,1,4,1,20044,77,4,1))
_Pm1604CntClient_ObjectIdentity=ObjectIdentity
pm1604CntClient=_Pm1604CntClient_ObjectIdentity((1,3,6,1,4,1,20044,77,4,2))
_Pm1604CntLine_ObjectIdentity=ObjectIdentity
pm1604CntLine=_Pm1604CntLine_ObjectIdentity((1,3,6,1,4,1,20044,77,4,3))
_Pm1604controlsWrite_ObjectIdentity=ObjectIdentity
pm1604controlsWrite=_Pm1604controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,77,6))
_Pm1604CtrlOther_ObjectIdentity=ObjectIdentity
pm1604CtrlOther=_Pm1604CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,77,6,1))
_Pm1604Ctrlsynth0_ObjectIdentity=ObjectIdentity
pm1604Ctrlsynth0=_Pm1604Ctrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,77,6,1,0))
_Pm1604CtrlConfLoad_Type=EkiOnOff
_Pm1604CtrlConfLoad_Object=MibScalar
pm1604CtrlConfLoad=_Pm1604CtrlConfLoad_Object((1,3,6,1,4,1,20044,77,6,1,0,1),_Pm1604CtrlConfLoad_Type())
pm1604CtrlConfLoad.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlConfLoad.setStatus(_A)
_Pm1604CtrlConfFlash_Type=EkiOnOff
_Pm1604CtrlConfFlash_Object=MibScalar
pm1604CtrlConfFlash=_Pm1604CtrlConfFlash_Object((1,3,6,1,4,1,20044,77,6,1,0,9),_Pm1604CtrlConfFlash_Type())
pm1604CtrlConfFlash.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlConfFlash.setStatus(_A)
_Pm1604CtrlConfClear_Type=EkiOnOff
_Pm1604CtrlConfClear_Object=MibScalar
pm1604CtrlConfClear=_Pm1604CtrlConfClear_Object((1,3,6,1,4,1,20044,77,6,1,0,13),_Pm1604CtrlConfClear_Type())
pm1604CtrlConfClear.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlConfClear.setStatus(_A)
_Pm1604Ctrlsynth4_ObjectIdentity=ObjectIdentity
pm1604Ctrlsynth4=_Pm1604Ctrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,77,6,1,4))
_Pm1604CtrlCorrelatOn_Type=EkiOnOff
_Pm1604CtrlCorrelatOn_Object=MibScalar
pm1604CtrlCorrelatOn=_Pm1604CtrlCorrelatOn_Object((1,3,6,1,4,1,20044,77,6,1,4,1),_Pm1604CtrlCorrelatOn_Type())
pm1604CtrlCorrelatOn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlCorrelatOn.setStatus(_A)
_Pm1604CtrlCorrelatOff_Type=EkiOnOff
_Pm1604CtrlCorrelatOff_Object=MibScalar
pm1604CtrlCorrelatOff=_Pm1604CtrlCorrelatOff_Object((1,3,6,1,4,1,20044,77,6,1,4,2),_Pm1604CtrlCorrelatOff_Type())
pm1604CtrlCorrelatOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlCorrelatOff.setStatus(_A)
_Pm1604CtrlswMgnt_ObjectIdentity=ObjectIdentity
pm1604CtrlswMgnt=_Pm1604CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,77,6,1,5))
_Pm1604CtrlColdReset_Type=EkiOnOff
_Pm1604CtrlColdReset_Object=MibScalar
pm1604CtrlColdReset=_Pm1604CtrlColdReset_Object((1,3,6,1,4,1,20044,77,6,1,5,2),_Pm1604CtrlColdReset_Type())
pm1604CtrlColdReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlColdReset.setStatus(_A)
_Pm1604CtrlWarmReset_Type=EkiOnOff
_Pm1604CtrlWarmReset_Object=MibScalar
pm1604CtrlWarmReset=_Pm1604CtrlWarmReset_Object((1,3,6,1,4,1,20044,77,6,1,5,3),_Pm1604CtrlWarmReset_Type())
pm1604CtrlWarmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlWarmReset.setStatus(_A)
_Pm1604CtrlledTest_ObjectIdentity=ObjectIdentity
pm1604CtrlledTest=_Pm1604CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,77,6,1,72))
_Pm1604CtrlGreenLed_Type=EkiOnOff
_Pm1604CtrlGreenLed_Object=MibScalar
pm1604CtrlGreenLed=_Pm1604CtrlGreenLed_Object((1,3,6,1,4,1,20044,77,6,1,72,1),_Pm1604CtrlGreenLed_Type())
pm1604CtrlGreenLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlGreenLed.setStatus(_A)
_Pm1604CtrlRedLed_Type=EkiOnOff
_Pm1604CtrlRedLed_Object=MibScalar
pm1604CtrlRedLed=_Pm1604CtrlRedLed_Object((1,3,6,1,4,1,20044,77,6,1,72,2),_Pm1604CtrlRedLed_Type())
pm1604CtrlRedLed.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlRedLed.setStatus(_A)
_Pm1604CtrlLedOff_Type=EkiOnOff
_Pm1604CtrlLedOff_Object=MibScalar
pm1604CtrlLedOff=_Pm1604CtrlLedOff_Object((1,3,6,1,4,1,20044,77,6,1,72,3),_Pm1604CtrlLedOff_Type())
pm1604CtrlLedOff.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlLedOff.setStatus(_A)
_Pm1604CtrlmoduleOosMode_ObjectIdentity=ObjectIdentity
pm1604CtrlmoduleOosMode=_Pm1604CtrlmoduleOosMode_ObjectIdentity((1,3,6,1,4,1,20044,77,6,1,73))
_Pm1604CtrlModuleOosMode_Type=EkiOnOff
_Pm1604CtrlModuleOosMode_Object=MibScalar
pm1604CtrlModuleOosMode=_Pm1604CtrlModuleOosMode_Object((1,3,6,1,4,1,20044,77,6,1,73,1),_Pm1604CtrlModuleOosMode_Type())
pm1604CtrlModuleOosMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlModuleOosMode.setStatus(_A)
_Pm1604CtrlClient_ObjectIdentity=ObjectIdentity
pm1604CtrlClient=_Pm1604CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,77,6,2))
_Pm1604Ctrlline1SfpOnoffTable_Object=MibTable
pm1604Ctrlline1SfpOnoffTable=_Pm1604Ctrlline1SfpOnoffTable_Object((1,3,6,1,4,1,20044,77,6,2,16))
if mibBuilder.loadTexts:pm1604Ctrlline1SfpOnoffTable.setStatus(_A)
_Pm1604Ctrlline1SfpOnoffEntry_Object=MibTableRow
pm1604Ctrlline1SfpOnoffEntry=_Pm1604Ctrlline1SfpOnoffEntry_Object((1,3,6,1,4,1,20044,77,6,2,16,1))
pm1604Ctrlline1SfpOnoffEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:pm1604Ctrlline1SfpOnoffEntry.setStatus(_A)
class _Pm1604Ctrlline1SfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline1SfpOnoffIndex_Type.__name__=_D
_Pm1604Ctrlline1SfpOnoffIndex_Object=MibTableColumn
pm1604Ctrlline1SfpOnoffIndex=_Pm1604Ctrlline1SfpOnoffIndex_Object((1,3,6,1,4,1,20044,77,6,2,16,1,1),_Pm1604Ctrlline1SfpOnoffIndex_Type())
pm1604Ctrlline1SfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline1SfpOnoffIndex.setStatus(_A)
_Pm1604Ctrlline1SfpOnoffPortn_Type=EkiState
_Pm1604Ctrlline1SfpOnoffPortn_Object=MibTableColumn
pm1604Ctrlline1SfpOnoffPortn=_Pm1604Ctrlline1SfpOnoffPortn_Object((1,3,6,1,4,1,20044,77,6,2,16,1,2),_Pm1604Ctrlline1SfpOnoffPortn_Type())
pm1604Ctrlline1SfpOnoffPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline1SfpOnoffPortn.setStatus(_A)
_Pm1604Ctrlline1LoopbackTable_Object=MibTable
pm1604Ctrlline1LoopbackTable=_Pm1604Ctrlline1LoopbackTable_Object((1,3,6,1,4,1,20044,77,6,2,17))
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackTable.setStatus(_A)
_Pm1604Ctrlline1LoopbackEntry_Object=MibTableRow
pm1604Ctrlline1LoopbackEntry=_Pm1604Ctrlline1LoopbackEntry_Object((1,3,6,1,4,1,20044,77,6,2,17,1))
pm1604Ctrlline1LoopbackEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackEntry.setStatus(_A)
class _Pm1604Ctrlline1LoopbackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline1LoopbackIndex_Type.__name__=_D
_Pm1604Ctrlline1LoopbackIndex_Object=MibTableColumn
pm1604Ctrlline1LoopbackIndex=_Pm1604Ctrlline1LoopbackIndex_Object((1,3,6,1,4,1,20044,77,6,2,17,1,1),_Pm1604Ctrlline1LoopbackIndex_Type())
pm1604Ctrlline1LoopbackIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackIndex.setStatus(_A)
_Pm1604Ctrlline1LoopbackPortn_Type=EkiState
_Pm1604Ctrlline1LoopbackPortn_Object=MibTableColumn
pm1604Ctrlline1LoopbackPortn=_Pm1604Ctrlline1LoopbackPortn_Object((1,3,6,1,4,1,20044,77,6,2,17,1,2),_Pm1604Ctrlline1LoopbackPortn_Type())
pm1604Ctrlline1LoopbackPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackPortn.setStatus(_A)
_Pm1604Ctrlline1LoopbackTermTable_Object=MibTable
pm1604Ctrlline1LoopbackTermTable=_Pm1604Ctrlline1LoopbackTermTable_Object((1,3,6,1,4,1,20044,77,6,2,18))
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackTermTable.setStatus(_A)
_Pm1604Ctrlline1LoopbackTermEntry_Object=MibTableRow
pm1604Ctrlline1LoopbackTermEntry=_Pm1604Ctrlline1LoopbackTermEntry_Object((1,3,6,1,4,1,20044,77,6,2,18,1))
pm1604Ctrlline1LoopbackTermEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackTermEntry.setStatus(_A)
class _Pm1604Ctrlline1LoopbackTermIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline1LoopbackTermIndex_Type.__name__=_D
_Pm1604Ctrlline1LoopbackTermIndex_Object=MibTableColumn
pm1604Ctrlline1LoopbackTermIndex=_Pm1604Ctrlline1LoopbackTermIndex_Object((1,3,6,1,4,1,20044,77,6,2,18,1,1),_Pm1604Ctrlline1LoopbackTermIndex_Type())
pm1604Ctrlline1LoopbackTermIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackTermIndex.setStatus(_A)
_Pm1604Ctrlline1LoopbackTermPortn_Type=EkiState
_Pm1604Ctrlline1LoopbackTermPortn_Object=MibTableColumn
pm1604Ctrlline1LoopbackTermPortn=_Pm1604Ctrlline1LoopbackTermPortn_Object((1,3,6,1,4,1,20044,77,6,2,18,1,2),_Pm1604Ctrlline1LoopbackTermPortn_Type())
pm1604Ctrlline1LoopbackTermPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline1LoopbackTermPortn.setStatus(_A)
_Pm1604Ctrlline1OosModeTable_Object=MibTable
pm1604Ctrlline1OosModeTable=_Pm1604Ctrlline1OosModeTable_Object((1,3,6,1,4,1,20044,77,6,2,20))
if mibBuilder.loadTexts:pm1604Ctrlline1OosModeTable.setStatus(_A)
_Pm1604Ctrlline1OosModeEntry_Object=MibTableRow
pm1604Ctrlline1OosModeEntry=_Pm1604Ctrlline1OosModeEntry_Object((1,3,6,1,4,1,20044,77,6,2,20,1))
pm1604Ctrlline1OosModeEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:pm1604Ctrlline1OosModeEntry.setStatus(_A)
class _Pm1604Ctrlline1OosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline1OosModeIndex_Type.__name__=_D
_Pm1604Ctrlline1OosModeIndex_Object=MibTableColumn
pm1604Ctrlline1OosModeIndex=_Pm1604Ctrlline1OosModeIndex_Object((1,3,6,1,4,1,20044,77,6,2,20,1,1),_Pm1604Ctrlline1OosModeIndex_Type())
pm1604Ctrlline1OosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline1OosModeIndex.setStatus(_A)
_Pm1604Ctrlline1OosModePortn_Type=EkiState
_Pm1604Ctrlline1OosModePortn_Object=MibTableColumn
pm1604Ctrlline1OosModePortn=_Pm1604Ctrlline1OosModePortn_Object((1,3,6,1,4,1,20044,77,6,2,20,1,2),_Pm1604Ctrlline1OosModePortn_Type())
pm1604Ctrlline1OosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline1OosModePortn.setStatus(_A)
_Pm1604CtrlprotocolTable_Object=MibTable
pm1604CtrlprotocolTable=_Pm1604CtrlprotocolTable_Object((1,3,6,1,4,1,20044,77,6,2,48))
if mibBuilder.loadTexts:pm1604CtrlprotocolTable.setStatus(_A)
_Pm1604CtrlprotocolEntry_Object=MibTableRow
pm1604CtrlprotocolEntry=_Pm1604CtrlprotocolEntry_Object((1,3,6,1,4,1,20044,77,6,2,48,1))
pm1604CtrlprotocolEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:pm1604CtrlprotocolEntry.setStatus(_A)
class _Pm1604CtrlprotocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CtrlprotocolIndex_Type.__name__=_D
_Pm1604CtrlprotocolIndex_Object=MibTableColumn
pm1604CtrlprotocolIndex=_Pm1604CtrlprotocolIndex_Object((1,3,6,1,4,1,20044,77,6,2,48,1,1),_Pm1604CtrlprotocolIndex_Type())
pm1604CtrlprotocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CtrlprotocolIndex.setStatus(_A)
_Pm1604CtrlprotocolPortn_Type=EkiProtocol
_Pm1604CtrlprotocolPortn_Object=MibTableColumn
pm1604CtrlprotocolPortn=_Pm1604CtrlprotocolPortn_Object((1,3,6,1,4,1,20044,77,6,2,48,1,2),_Pm1604CtrlprotocolPortn_Type())
pm1604CtrlprotocolPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CtrlprotocolPortn.setStatus(_A)
_Pm1604CtrlLine_ObjectIdentity=ObjectIdentity
pm1604CtrlLine=_Pm1604CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,77,6,3))
_Pm1604Ctrlline2SfpOnoffTable_Object=MibTable
pm1604Ctrlline2SfpOnoffTable=_Pm1604Ctrlline2SfpOnoffTable_Object((1,3,6,1,4,1,20044,77,6,3,64))
if mibBuilder.loadTexts:pm1604Ctrlline2SfpOnoffTable.setStatus(_A)
_Pm1604Ctrlline2SfpOnoffEntry_Object=MibTableRow
pm1604Ctrlline2SfpOnoffEntry=_Pm1604Ctrlline2SfpOnoffEntry_Object((1,3,6,1,4,1,20044,77,6,3,64,1))
pm1604Ctrlline2SfpOnoffEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:pm1604Ctrlline2SfpOnoffEntry.setStatus(_A)
class _Pm1604Ctrlline2SfpOnoffIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline2SfpOnoffIndex_Type.__name__=_D
_Pm1604Ctrlline2SfpOnoffIndex_Object=MibTableColumn
pm1604Ctrlline2SfpOnoffIndex=_Pm1604Ctrlline2SfpOnoffIndex_Object((1,3,6,1,4,1,20044,77,6,3,64,1,1),_Pm1604Ctrlline2SfpOnoffIndex_Type())
pm1604Ctrlline2SfpOnoffIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline2SfpOnoffIndex.setStatus(_A)
_Pm1604Ctrlline2SfpOnoffPortn_Type=EkiState
_Pm1604Ctrlline2SfpOnoffPortn_Object=MibTableColumn
pm1604Ctrlline2SfpOnoffPortn=_Pm1604Ctrlline2SfpOnoffPortn_Object((1,3,6,1,4,1,20044,77,6,3,64,1,2),_Pm1604Ctrlline2SfpOnoffPortn_Type())
pm1604Ctrlline2SfpOnoffPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline2SfpOnoffPortn.setStatus(_A)
_Pm1604Ctrlline2OosModeTable_Object=MibTable
pm1604Ctrlline2OosModeTable=_Pm1604Ctrlline2OosModeTable_Object((1,3,6,1,4,1,20044,77,6,3,65))
if mibBuilder.loadTexts:pm1604Ctrlline2OosModeTable.setStatus(_A)
_Pm1604Ctrlline2OosModeEntry_Object=MibTableRow
pm1604Ctrlline2OosModeEntry=_Pm1604Ctrlline2OosModeEntry_Object((1,3,6,1,4,1,20044,77,6,3,65,1))
pm1604Ctrlline2OosModeEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:pm1604Ctrlline2OosModeEntry.setStatus(_A)
class _Pm1604Ctrlline2OosModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline2OosModeIndex_Type.__name__=_D
_Pm1604Ctrlline2OosModeIndex_Object=MibTableColumn
pm1604Ctrlline2OosModeIndex=_Pm1604Ctrlline2OosModeIndex_Object((1,3,6,1,4,1,20044,77,6,3,65,1,1),_Pm1604Ctrlline2OosModeIndex_Type())
pm1604Ctrlline2OosModeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline2OosModeIndex.setStatus(_A)
_Pm1604Ctrlline2OosModePortn_Type=EkiState
_Pm1604Ctrlline2OosModePortn_Object=MibTableColumn
pm1604Ctrlline2OosModePortn=_Pm1604Ctrlline2OosModePortn_Object((1,3,6,1,4,1,20044,77,6,3,65,1,2),_Pm1604Ctrlline2OosModePortn_Type())
pm1604Ctrlline2OosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline2OosModePortn.setStatus(_A)
_Pm1604Ctrlline2LoopbackTable_Object=MibTable
pm1604Ctrlline2LoopbackTable=_Pm1604Ctrlline2LoopbackTable_Object((1,3,6,1,4,1,20044,77,6,3,66))
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackTable.setStatus(_A)
_Pm1604Ctrlline2LoopbackEntry_Object=MibTableRow
pm1604Ctrlline2LoopbackEntry=_Pm1604Ctrlline2LoopbackEntry_Object((1,3,6,1,4,1,20044,77,6,3,66,1))
pm1604Ctrlline2LoopbackEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackEntry.setStatus(_A)
class _Pm1604Ctrlline2LoopbackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline2LoopbackIndex_Type.__name__=_D
_Pm1604Ctrlline2LoopbackIndex_Object=MibTableColumn
pm1604Ctrlline2LoopbackIndex=_Pm1604Ctrlline2LoopbackIndex_Object((1,3,6,1,4,1,20044,77,6,3,66,1,1),_Pm1604Ctrlline2LoopbackIndex_Type())
pm1604Ctrlline2LoopbackIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackIndex.setStatus(_A)
_Pm1604Ctrlline2LoopbackPortn_Type=EkiState
_Pm1604Ctrlline2LoopbackPortn_Object=MibTableColumn
pm1604Ctrlline2LoopbackPortn=_Pm1604Ctrlline2LoopbackPortn_Object((1,3,6,1,4,1,20044,77,6,3,66,1,2),_Pm1604Ctrlline2LoopbackPortn_Type())
pm1604Ctrlline2LoopbackPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackPortn.setStatus(_A)
_Pm1604Ctrlline2LoopbackTermTable_Object=MibTable
pm1604Ctrlline2LoopbackTermTable=_Pm1604Ctrlline2LoopbackTermTable_Object((1,3,6,1,4,1,20044,77,6,3,67))
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackTermTable.setStatus(_A)
_Pm1604Ctrlline2LoopbackTermEntry_Object=MibTableRow
pm1604Ctrlline2LoopbackTermEntry=_Pm1604Ctrlline2LoopbackTermEntry_Object((1,3,6,1,4,1,20044,77,6,3,67,1))
pm1604Ctrlline2LoopbackTermEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackTermEntry.setStatus(_A)
class _Pm1604Ctrlline2LoopbackTermIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604Ctrlline2LoopbackTermIndex_Type.__name__=_D
_Pm1604Ctrlline2LoopbackTermIndex_Object=MibTableColumn
pm1604Ctrlline2LoopbackTermIndex=_Pm1604Ctrlline2LoopbackTermIndex_Object((1,3,6,1,4,1,20044,77,6,3,67,1,1),_Pm1604Ctrlline2LoopbackTermIndex_Type())
pm1604Ctrlline2LoopbackTermIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackTermIndex.setStatus(_A)
_Pm1604Ctrlline2LoopbackTermPortn_Type=EkiState
_Pm1604Ctrlline2LoopbackTermPortn_Object=MibTableColumn
pm1604Ctrlline2LoopbackTermPortn=_Pm1604Ctrlline2LoopbackTermPortn_Object((1,3,6,1,4,1,20044,77,6,3,67,1,2),_Pm1604Ctrlline2LoopbackTermPortn_Type())
pm1604Ctrlline2LoopbackTermPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604Ctrlline2LoopbackTermPortn.setStatus(_A)
_Pm1604ri_ObjectIdentity=ObjectIdentity
pm1604ri=_Pm1604ri_ObjectIdentity((1,3,6,1,4,1,20044,77,7))
_Pm1604riTable_ObjectIdentity=ObjectIdentity
pm1604riTable=_Pm1604riTable_ObjectIdentity((1,3,6,1,4,1,20044,77,7,1))
_Pm1604RinvLine1Table_Object=MibTable
pm1604RinvLine1Table=_Pm1604RinvLine1Table_Object((1,3,6,1,4,1,20044,77,7,1,1))
if mibBuilder.loadTexts:pm1604RinvLine1Table.setStatus(_A)
_Pm1604RinvLine1Entry_Object=MibTableRow
pm1604RinvLine1Entry=_Pm1604RinvLine1Entry_Object((1,3,6,1,4,1,20044,77,7,1,1,1))
pm1604RinvLine1Entry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:pm1604RinvLine1Entry.setStatus(_A)
class _Pm1604RinvLine1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1604RinvLine1Index_Type.__name__=_D
_Pm1604RinvLine1Index_Object=MibTableColumn
pm1604RinvLine1Index=_Pm1604RinvLine1Index_Object((1,3,6,1,4,1,20044,77,7,1,1,1,1),_Pm1604RinvLine1Index_Type())
pm1604RinvLine1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvLine1Index.setStatus(_A)
_Pm1604RinvSfpLine1_Type=DisplayString
_Pm1604RinvSfpLine1_Object=MibTableColumn
pm1604RinvSfpLine1=_Pm1604RinvSfpLine1_Object((1,3,6,1,4,1,20044,77,7,1,1,1,2),_Pm1604RinvSfpLine1_Type())
pm1604RinvSfpLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvSfpLine1.setStatus(_A)
_Pm1604RinvLine2Table_Object=MibTable
pm1604RinvLine2Table=_Pm1604RinvLine2Table_Object((1,3,6,1,4,1,20044,77,7,1,2))
if mibBuilder.loadTexts:pm1604RinvLine2Table.setStatus(_A)
_Pm1604RinvLine2Entry_Object=MibTableRow
pm1604RinvLine2Entry=_Pm1604RinvLine2Entry_Object((1,3,6,1,4,1,20044,77,7,1,2,1))
pm1604RinvLine2Entry.setIndexNames((0,_C,_w))
if mibBuilder.loadTexts:pm1604RinvLine2Entry.setStatus(_A)
class _Pm1604RinvLine2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pm1604RinvLine2Index_Type.__name__=_D
_Pm1604RinvLine2Index_Object=MibTableColumn
pm1604RinvLine2Index=_Pm1604RinvLine2Index_Object((1,3,6,1,4,1,20044,77,7,1,2,1,1),_Pm1604RinvLine2Index_Type())
pm1604RinvLine2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvLine2Index.setStatus(_A)
_Pm1604RinvsfpLine2_Type=DisplayString
_Pm1604RinvsfpLine2_Object=MibTableColumn
pm1604RinvsfpLine2=_Pm1604RinvsfpLine2_Object((1,3,6,1,4,1,20044,77,7,1,2,1,2),_Pm1604RinvsfpLine2_Type())
pm1604RinvsfpLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvsfpLine2.setStatus(_A)
_Pm1604RinvReloadInventory_Type=EkiOnOff
_Pm1604RinvReloadInventory_Object=MibScalar
pm1604RinvReloadInventory=_Pm1604RinvReloadInventory_Object((1,3,6,1,4,1,20044,77,7,2),_Pm1604RinvReloadInventory_Type())
pm1604RinvReloadInventory.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604RinvReloadInventory.setStatus(_A)
_Pm1604RinvHwPlatform_Type=DisplayString
_Pm1604RinvHwPlatform_Object=MibScalar
pm1604RinvHwPlatform=_Pm1604RinvHwPlatform_Object((1,3,6,1,4,1,20044,77,7,3),_Pm1604RinvHwPlatform_Type())
pm1604RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvHwPlatform.setStatus(_A)
_Pm1604RinvModulePlatform_Type=DisplayString
_Pm1604RinvModulePlatform_Object=MibScalar
pm1604RinvModulePlatform=_Pm1604RinvModulePlatform_Object((1,3,6,1,4,1,20044,77,7,4),_Pm1604RinvModulePlatform_Type())
pm1604RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvModulePlatform.setStatus(_A)
_Pm1604RinvSwPlatform_Type=DisplayString
_Pm1604RinvSwPlatform_Object=MibScalar
pm1604RinvSwPlatform=_Pm1604RinvSwPlatform_Object((1,3,6,1,4,1,20044,77,7,5),_Pm1604RinvSwPlatform_Type())
pm1604RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvSwPlatform.setStatus(_A)
_Pm1604RinvGwPlatform_Type=DisplayString
_Pm1604RinvGwPlatform_Object=MibScalar
pm1604RinvGwPlatform=_Pm1604RinvGwPlatform_Object((1,3,6,1,4,1,20044,77,7,6),_Pm1604RinvGwPlatform_Type())
pm1604RinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604RinvGwPlatform.setStatus(_A)
_Pm1604Config_ObjectIdentity=ObjectIdentity
pm1604Config=_Pm1604Config_ObjectIdentity((1,3,6,1,4,1,20044,77,9))
_Pm1604CfgLsd_ObjectIdentity=ObjectIdentity
pm1604CfgLsd=_Pm1604CfgLsd_ObjectIdentity((1,3,6,1,4,1,20044,77,9,1))
_Pm1604CfgLine1LsdTable_Object=MibTable
pm1604CfgLine1LsdTable=_Pm1604CfgLine1LsdTable_Object((1,3,6,1,4,1,20044,77,9,1,1))
if mibBuilder.loadTexts:pm1604CfgLine1LsdTable.setStatus(_A)
_Pm1604CfgLine1LsdEntry_Object=MibTableRow
pm1604CfgLine1LsdEntry=_Pm1604CfgLine1LsdEntry_Object((1,3,6,1,4,1,20044,77,9,1,1,1))
pm1604CfgLine1LsdEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:pm1604CfgLine1LsdEntry.setStatus(_A)
class _Pm1604CfgLine1LsdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgLine1LsdIndex_Type.__name__=_D
_Pm1604CfgLine1LsdIndex_Object=MibTableColumn
pm1604CfgLine1LsdIndex=_Pm1604CfgLine1LsdIndex_Object((1,3,6,1,4,1,20044,77,9,1,1,1,1),_Pm1604CfgLine1LsdIndex_Type())
pm1604CfgLine1LsdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgLine1LsdIndex.setStatus(_A)
class _Pm1604CfgLine1LsdModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine1LsdModePortn_Type.__name__=_F
_Pm1604CfgLine1LsdModePortn_Object=MibTableColumn
pm1604CfgLine1LsdModePortn=_Pm1604CfgLine1LsdModePortn_Object((1,3,6,1,4,1,20044,77,9,1,1,1,3),_Pm1604CfgLine1LsdModePortn_Type())
pm1604CfgLine1LsdModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine1LsdModePortn.setStatus(_A)
class _Pm1604CfgLine1AccessioCtrbInsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine1AccessioCtrbInsPortn_Type.__name__=_F
_Pm1604CfgLine1AccessioCtrbInsPortn_Object=MibTableColumn
pm1604CfgLine1AccessioCtrbInsPortn=_Pm1604CfgLine1AccessioCtrbInsPortn_Object((1,3,6,1,4,1,20044,77,9,1,1,1,4),_Pm1604CfgLine1AccessioCtrbInsPortn_Type())
pm1604CfgLine1AccessioCtrbInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine1AccessioCtrbInsPortn.setStatus(_A)
class _Pm1604CfgLine2AccessioCtrbInsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine2AccessioCtrbInsPortn_Type.__name__=_F
_Pm1604CfgLine2AccessioCtrbInsPortn_Object=MibTableColumn
pm1604CfgLine2AccessioCtrbInsPortn=_Pm1604CfgLine2AccessioCtrbInsPortn_Object((1,3,6,1,4,1,20044,77,9,1,1,1,7),_Pm1604CfgLine2AccessioCtrbInsPortn_Type())
pm1604CfgLine2AccessioCtrbInsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine2AccessioCtrbInsPortn.setStatus(_A)
_Pm1604CfgStartUp_ObjectIdentity=ObjectIdentity
pm1604CfgStartUp=_Pm1604CfgStartUp_ObjectIdentity((1,3,6,1,4,1,20044,77,9,2))
_Pm1604CfgLine1StartupTable_Object=MibTable
pm1604CfgLine1StartupTable=_Pm1604CfgLine1StartupTable_Object((1,3,6,1,4,1,20044,77,9,2,1))
if mibBuilder.loadTexts:pm1604CfgLine1StartupTable.setStatus(_A)
_Pm1604CfgLine1StartupEntry_Object=MibTableRow
pm1604CfgLine1StartupEntry=_Pm1604CfgLine1StartupEntry_Object((1,3,6,1,4,1,20044,77,9,2,1,1))
pm1604CfgLine1StartupEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:pm1604CfgLine1StartupEntry.setStatus(_A)
class _Pm1604CfgLine1StartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgLine1StartupIndex_Type.__name__=_D
_Pm1604CfgLine1StartupIndex_Object=MibTableColumn
pm1604CfgLine1StartupIndex=_Pm1604CfgLine1StartupIndex_Object((1,3,6,1,4,1,20044,77,9,2,1,1,1),_Pm1604CfgLine1StartupIndex_Type())
pm1604CfgLine1StartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgLine1StartupIndex.setStatus(_A)
class _Pm1604CfgLine1TrscvCtrlPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine1TrscvCtrlPortn_Type.__name__=_F
_Pm1604CfgLine1TrscvCtrlPortn_Object=MibTableColumn
pm1604CfgLine1TrscvCtrlPortn=_Pm1604CfgLine1TrscvCtrlPortn_Object((1,3,6,1,4,1,20044,77,9,2,1,1,3),_Pm1604CfgLine1TrscvCtrlPortn_Type())
pm1604CfgLine1TrscvCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine1TrscvCtrlPortn.setStatus(_A)
class _Pm1604CfgLine1ProtocolPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine1ProtocolPortn_Type.__name__=_F
_Pm1604CfgLine1ProtocolPortn_Object=MibTableColumn
pm1604CfgLine1ProtocolPortn=_Pm1604CfgLine1ProtocolPortn_Object((1,3,6,1,4,1,20044,77,9,2,1,1,4),_Pm1604CfgLine1ProtocolPortn_Type())
pm1604CfgLine1ProtocolPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine1ProtocolPortn.setStatus(_A)
class _Pm1604CfgLine1OosModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine1OosModePortn_Type.__name__=_F
_Pm1604CfgLine1OosModePortn_Object=MibTableColumn
pm1604CfgLine1OosModePortn=_Pm1604CfgLine1OosModePortn_Object((1,3,6,1,4,1,20044,77,9,2,1,1,5),_Pm1604CfgLine1OosModePortn_Type())
pm1604CfgLine1OosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine1OosModePortn.setStatus(_A)
_Pm1604CfgLine2StartupTable_Object=MibTable
pm1604CfgLine2StartupTable=_Pm1604CfgLine2StartupTable_Object((1,3,6,1,4,1,20044,77,9,2,2))
if mibBuilder.loadTexts:pm1604CfgLine2StartupTable.setStatus(_A)
_Pm1604CfgLine2StartupEntry_Object=MibTableRow
pm1604CfgLine2StartupEntry=_Pm1604CfgLine2StartupEntry_Object((1,3,6,1,4,1,20044,77,9,2,2,1))
pm1604CfgLine2StartupEntry.setIndexNames((0,_C,_z))
if mibBuilder.loadTexts:pm1604CfgLine2StartupEntry.setStatus(_A)
class _Pm1604CfgLine2StartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgLine2StartupIndex_Type.__name__=_D
_Pm1604CfgLine2StartupIndex_Object=MibTableColumn
pm1604CfgLine2StartupIndex=_Pm1604CfgLine2StartupIndex_Object((1,3,6,1,4,1,20044,77,9,2,2,1,1),_Pm1604CfgLine2StartupIndex_Type())
pm1604CfgLine2StartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgLine2StartupIndex.setStatus(_A)
class _Pm1604CfgLine2TrscvCtrlPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine2TrscvCtrlPortn_Type.__name__=_F
_Pm1604CfgLine2TrscvCtrlPortn_Object=MibTableColumn
pm1604CfgLine2TrscvCtrlPortn=_Pm1604CfgLine2TrscvCtrlPortn_Object((1,3,6,1,4,1,20044,77,9,2,2,1,3),_Pm1604CfgLine2TrscvCtrlPortn_Type())
pm1604CfgLine2TrscvCtrlPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine2TrscvCtrlPortn.setStatus(_A)
class _Pm1604CfgLine2OosModePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLine2OosModePortn_Type.__name__=_F
_Pm1604CfgLine2OosModePortn_Object=MibTableColumn
pm1604CfgLine2OosModePortn=_Pm1604CfgLine2OosModePortn_Object((1,3,6,1,4,1,20044,77,9,2,2,1,4),_Pm1604CfgLine2OosModePortn_Type())
pm1604CfgLine2OosModePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLine2OosModePortn.setStatus(_A)
_Pm1604CfgOtxtlhTable_Object=MibTable
pm1604CfgOtxtlhTable=_Pm1604CfgOtxtlhTable_Object((1,3,6,1,4,1,20044,77,9,2,3))
if mibBuilder.loadTexts:pm1604CfgOtxtlhTable.setStatus(_A)
_Pm1604CfgOtxtlhEntry_Object=MibTableRow
pm1604CfgOtxtlhEntry=_Pm1604CfgOtxtlhEntry_Object((1,3,6,1,4,1,20044,77,9,2,3,1))
pm1604CfgOtxtlhEntry.setIndexNames((0,_C,_A0))
if mibBuilder.loadTexts:pm1604CfgOtxtlhEntry.setStatus(_A)
class _Pm1604CfgOtxtlhIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgOtxtlhIndex_Type.__name__=_D
_Pm1604CfgOtxtlhIndex_Object=MibTableColumn
pm1604CfgOtxtlhIndex=_Pm1604CfgOtxtlhIndex_Object((1,3,6,1,4,1,20044,77,9,2,3,1,1),_Pm1604CfgOtxtlhIndex_Type())
pm1604CfgOtxtlhIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgOtxtlhIndex.setStatus(_A)
class _Pm1604CfgLineControlsPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLineControlsPortn_Type.__name__=_F
_Pm1604CfgLineControlsPortn_Object=MibTableColumn
pm1604CfgLineControlsPortn=_Pm1604CfgLineControlsPortn_Object((1,3,6,1,4,1,20044,77,9,2,3,1,3),_Pm1604CfgLineControlsPortn_Type())
pm1604CfgLineControlsPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLineControlsPortn.setStatus('deprecated')
class _Pm1604CfgLinePwrLaserPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLinePwrLaserPortn_Type.__name__=_F
_Pm1604CfgLinePwrLaserPortn_Object=MibTableColumn
pm1604CfgLinePwrLaserPortn=_Pm1604CfgLinePwrLaserPortn_Object((1,3,6,1,4,1,20044,77,9,2,3,1,6),_Pm1604CfgLinePwrLaserPortn_Type())
pm1604CfgLinePwrLaserPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLinePwrLaserPortn.setStatus(_A)
class _Pm1604CfgLineFCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLineFCurrentPortn_Type.__name__=_F
_Pm1604CfgLineFCurrentPortn_Object=MibTableColumn
pm1604CfgLineFCurrentPortn=_Pm1604CfgLineFCurrentPortn_Object((1,3,6,1,4,1,20044,77,9,2,3,1,7),_Pm1604CfgLineFCurrentPortn_Type())
pm1604CfgLineFCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLineFCurrentPortn.setStatus(_A)
class _Pm1604CfgLineGridCurrentPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLineGridCurrentPortn_Type.__name__=_F
_Pm1604CfgLineGridCurrentPortn_Object=MibTableColumn
pm1604CfgLineGridCurrentPortn=_Pm1604CfgLineGridCurrentPortn_Object((1,3,6,1,4,1,20044,77,9,2,3,1,8),_Pm1604CfgLineGridCurrentPortn_Type())
pm1604CfgLineGridCurrentPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLineGridCurrentPortn.setStatus(_A)
class _Pm1604CfgLineFoPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLineFoPortn_Type.__name__=_F
_Pm1604CfgLineFoPortn_Object=MibTableColumn
pm1604CfgLineFoPortn=_Pm1604CfgLineFoPortn_Object((1,3,6,1,4,1,20044,77,9,2,3,1,9),_Pm1604CfgLineFoPortn_Type())
pm1604CfgLineFoPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLineFoPortn.setStatus(_A)
_Pm1604CfgLabels_ObjectIdentity=ObjectIdentity
pm1604CfgLabels=_Pm1604CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,77,9,3))
_Pm1604CfgLabelclientTable_Object=MibTable
pm1604CfgLabelclientTable=_Pm1604CfgLabelclientTable_Object((1,3,6,1,4,1,20044,77,9,3,1))
if mibBuilder.loadTexts:pm1604CfgLabelclientTable.setStatus(_A)
_Pm1604CfgLabelclientEntry_Object=MibTableRow
pm1604CfgLabelclientEntry=_Pm1604CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,77,9,3,1,1))
pm1604CfgLabelclientEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:pm1604CfgLabelclientEntry.setStatus(_A)
class _Pm1604CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgLabelclientIndex_Type.__name__=_D
_Pm1604CfgLabelclientIndex_Object=MibTableColumn
pm1604CfgLabelclientIndex=_Pm1604CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,77,9,3,1,1,1),_Pm1604CfgLabelclientIndex_Type())
pm1604CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgLabelclientIndex.setStatus(_A)
class _Pm1604CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1604CfgLabelclientPortn_Type.__name__=_J
_Pm1604CfgLabelclientPortn_Object=MibTableColumn
pm1604CfgLabelclientPortn=_Pm1604CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,77,9,3,1,1,3),_Pm1604CfgLabelclientPortn_Type())
pm1604CfgLabelclientPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLabelclientPortn.setStatus(_A)
_Pm1604CfgLabellineTable_Object=MibTable
pm1604CfgLabellineTable=_Pm1604CfgLabellineTable_Object((1,3,6,1,4,1,20044,77,9,3,2))
if mibBuilder.loadTexts:pm1604CfgLabellineTable.setStatus(_A)
_Pm1604CfgLabellineEntry_Object=MibTableRow
pm1604CfgLabellineEntry=_Pm1604CfgLabellineEntry_Object((1,3,6,1,4,1,20044,77,9,3,2,1))
pm1604CfgLabellineEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:pm1604CfgLabellineEntry.setStatus(_A)
class _Pm1604CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgLabellineIndex_Type.__name__=_D
_Pm1604CfgLabellineIndex_Object=MibTableColumn
pm1604CfgLabellineIndex=_Pm1604CfgLabellineIndex_Object((1,3,6,1,4,1,20044,77,9,3,2,1,1),_Pm1604CfgLabellineIndex_Type())
pm1604CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgLabellineIndex.setStatus(_A)
class _Pm1604CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm1604CfgLabellinePortn_Type.__name__=_J
_Pm1604CfgLabellinePortn_Object=MibTableColumn
pm1604CfgLabellinePortn=_Pm1604CfgLabellinePortn_Object((1,3,6,1,4,1,20044,77,9,3,2,1,3),_Pm1604CfgLabellinePortn_Type())
pm1604CfgLabellinePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLabellinePortn.setStatus(_A)
_Pm1604CfgStartuptablefive_ObjectIdentity=ObjectIdentity
pm1604CfgStartuptablefive=_Pm1604CfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,77,9,4))
_Pm1604CfgOtxtlhcapabilitiesTable_Object=MibTable
pm1604CfgOtxtlhcapabilitiesTable=_Pm1604CfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,77,9,4,1))
if mibBuilder.loadTexts:pm1604CfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pm1604CfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pm1604CfgOtxtlhcapabilitiesEntry=_Pm1604CfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,77,9,4,1,1))
pm1604CfgOtxtlhcapabilitiesEntry.setIndexNames((0,_C,_A3))
if mibBuilder.loadTexts:pm1604CfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pm1604CfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm1604CfgOtxtlhcapabilitiesIndex_Type.__name__=_D
_Pm1604CfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pm1604CfgOtxtlhcapabilitiesIndex=_Pm1604CfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,77,9,4,1,1,1),_Pm1604CfgOtxtlhcapabilitiesIndex_Type())
pm1604CfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604CfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pm1604CfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgComponentTypePortn_Type.__name__=_F
_Pm1604CfgComponentTypePortn_Object=MibTableColumn
pm1604CfgComponentTypePortn=_Pm1604CfgComponentTypePortn_Object((1,3,6,1,4,1,20044,77,9,4,1,1,3),_Pm1604CfgComponentTypePortn_Type())
pm1604CfgComponentTypePortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgComponentTypePortn.setStatus(_A)
class _Pm1604CfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgMiscellaneousPortn_Type.__name__=_F
_Pm1604CfgMiscellaneousPortn_Object=MibTableColumn
pm1604CfgMiscellaneousPortn=_Pm1604CfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,77,9,4,1,1,4),_Pm1604CfgMiscellaneousPortn_Type())
pm1604CfgMiscellaneousPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgMiscellaneousPortn.setStatus(_A)
class _Pm1604CfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgFirstChannelPortn_Type.__name__=_F
_Pm1604CfgFirstChannelPortn_Object=MibTableColumn
pm1604CfgFirstChannelPortn=_Pm1604CfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,77,9,4,1,1,5),_Pm1604CfgFirstChannelPortn_Type())
pm1604CfgFirstChannelPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgFirstChannelPortn.setStatus(_A)
class _Pm1604CfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgLastChannelPortn_Type.__name__=_F
_Pm1604CfgLastChannelPortn_Object=MibTableColumn
pm1604CfgLastChannelPortn=_Pm1604CfgLastChannelPortn_Object((1,3,6,1,4,1,20044,77,9,4,1,1,6),_Pm1604CfgLastChannelPortn_Type())
pm1604CfgLastChannelPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgLastChannelPortn.setStatus(_A)
class _Pm1604CfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm1604CfgGridPortn_Type.__name__=_F
_Pm1604CfgGridPortn_Object=MibTableColumn
pm1604CfgGridPortn=_Pm1604CfgGridPortn_Object((1,3,6,1,4,1,20044,77,9,4,1,1,7),_Pm1604CfgGridPortn_Type())
pm1604CfgGridPortn.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgGridPortn.setStatus(_A)
_Pm1604CfgWriteConfiguration_Type=EkiOnOff
_Pm1604CfgWriteConfiguration_Object=MibScalar
pm1604CfgWriteConfiguration=_Pm1604CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,77,9,257),_Pm1604CfgWriteConfiguration_Type())
pm1604CfgWriteConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:pm1604CfgWriteConfiguration.setStatus(_A)
_Pm1604traps_ObjectIdentity=ObjectIdentity
pm1604traps=_Pm1604traps_ObjectIdentity((1,3,6,1,4,1,20044,77,10))
class _Pm1604trapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1604trapPortNumber_Type.__name__=_D
_Pm1604trapPortNumber_Object=MibScalar
pm1604trapPortNumber=_Pm1604trapPortNumber_Object((1,3,6,1,4,1,20044,77,10,2),_Pm1604trapPortNumber_Type())
pm1604trapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604trapPortNumber.setStatus(_A)
class _Pm1604trapLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1604trapLineNumber_Type.__name__=_D
_Pm1604trapLineNumber_Object=MibScalar
pm1604trapLineNumber=_Pm1604trapLineNumber_Object((1,3,6,1,4,1,20044,77,10,3),_Pm1604trapLineNumber_Type())
pm1604trapLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604trapLineNumber.setStatus(_A)
class _Pm1604trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm1604trapBoardNumber_Type.__name__=_D
_Pm1604trapBoardNumber_Object=MibScalar
pm1604trapBoardNumber=_Pm1604trapBoardNumber_Object((1,3,6,1,4,1,20044,77,10,4),_Pm1604trapBoardNumber_Type())
pm1604trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm1604trapBoardNumber.setStatus(_A)
pm1604Line2TrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,30))
pm1604Line2TrapNotUrgentGoesOn.setObjects(*((_C,_K),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line2TrapNotUrgentGoesOn.setStatus(_A)
pm1604Line2TrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,31))
pm1604Line2TrapNotUrgentGoesOff.setObjects(*((_C,_K),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line2TrapNotUrgentGoesOff.setStatus(_A)
pm1604Line2TrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,32))
pm1604Line2TrapUrgentGoesOn.setObjects(*((_C,_L),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line2TrapUrgentGoesOn.setStatus(_A)
pm1604Line2TrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,33))
pm1604Line2TrapUrgentGoesOff.setObjects(*((_C,_L),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line2TrapUrgentGoesOff.setStatus(_A)
pm1604Line2TrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,34))
pm1604Line2TrapCritGoesOn.setObjects(*((_C,_M),(_C,_N),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line2TrapCritGoesOn.setStatus(_A)
pm1604Line2TrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,35))
pm1604Line2TrapCritGoesOff.setObjects(*((_C,_M),(_C,_N),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line2TrapCritGoesOff.setStatus(_A)
pm1604Line1TrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,40))
pm1604Line1TrapNotUrgentGoesOn.setObjects(*((_C,_O),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line1TrapNotUrgentGoesOn.setStatus(_A)
pm1604Line1TrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,41))
pm1604Line1TrapNotUrgentGoesOff.setObjects(*((_C,_O),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line1TrapNotUrgentGoesOff.setStatus(_A)
pm1604Line1TrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,42))
pm1604Line1TrapUrgentGoesOn.setObjects(*((_C,_P),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line1TrapUrgentGoesOn.setStatus(_A)
pm1604Line1TrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,43))
pm1604Line1TrapUrgentGoesOff.setObjects(*((_C,_P),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line1TrapUrgentGoesOff.setStatus(_A)
pm1604Line1TrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,44))
pm1604Line1TrapCritGoesOn.setObjects(*((_C,_Q),(_C,_R),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line1TrapCritGoesOn.setStatus(_A)
pm1604Line1TrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,45))
pm1604Line1TrapCritGoesOff.setObjects(*((_C,_Q),(_C,_R),(_C,_I),(_C,_G)))
if mibBuilder.loadTexts:pm1604Line1TrapCritGoesOff.setStatus(_A)
pm1604PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,77,10,50))
pm1604PowerTrapUrgentGoesOn.setObjects(*((_C,_S),(_C,_T),(_C,_G)))
if mibBuilder.loadTexts:pm1604PowerTrapUrgentGoesOn.setStatus(_A)
pm1604PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,77,10,51))
pm1604PowerTrapUrgentGoesOff.setObjects(*((_C,_S),(_C,_T),(_C,_G)))
if mibBuilder.loadTexts:pm1604PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Pm1604OtxGrid':Pm1604OtxGrid,'Pm1604LineChannel':Pm1604LineChannel,'Pm1604ClientProtocol':Pm1604ClientProtocol,'modulePm1604':modulePm1604,'pm1604alarms':pm1604alarms,'pm1604AlmOther':pm1604AlmOther,'pm1604AlmOtherNurg':pm1604AlmOtherNurg,'pm1604AlmsynthAlm2':pm1604AlmsynthAlm2,'pm1604AlmConfTableSave':pm1604AlmConfTableSave,'pm1604AlmInvUpload':pm1604AlmInvUpload,'pm1604AlmConfTableLoad':pm1604AlmConfTableLoad,'pm1604AlmCorrelatOff':pm1604AlmCorrelatOff,'pm1604AlmOtherUrg':pm1604AlmOtherUrg,'pm1604AlmOtherCrit':pm1604AlmOtherCrit,'pm1604AlmsynthAlm0':pm1604AlmsynthAlm0,'pm1604AlmModuleGlobFailure':pm1604AlmModuleGlobFailure,_T:pm1604AlmDefFuseA,_S:pm1604AlmDefFuseB,'pm1604AlmClient':pm1604AlmClient,'pm1604AlmClientNurg':pm1604AlmClientNurg,'pm1604Almline1SfpWarnDdmTable':pm1604Almline1SfpWarnDdmTable,'pm1604Almline1SfpWarnDdmEntry':pm1604Almline1SfpWarnDdmEntry,_U:pm1604Almline1SfpWarnDdmIndex,'pm1604AlmLine1TxPwLowWngPortn':pm1604AlmLine1TxPwLowWngPortn,'pm1604AlmLine1TxPwrHighWngPortn':pm1604AlmLine1TxPwrHighWngPortn,'pm1604AlmLine1TxBiasLowWngPortn':pm1604AlmLine1TxBiasLowWngPortn,'pm1604AlmLine1TxBiasHighWngPortn':pm1604AlmLine1TxBiasHighWngPortn,'pm1604AlmLine1VccLowWngPortn':pm1604AlmLine1VccLowWngPortn,'pm1604AlmLine1VccHighWngPortn':pm1604AlmLine1VccHighWngPortn,'pm1604AlmLine1TempLowWngPortn':pm1604AlmLine1TempLowWngPortn,'pm1604AlmLine1TempHighWngPortn':pm1604AlmLine1TempHighWngPortn,'pm1604AlmLine1RxPwrLowWngPortn':pm1604AlmLine1RxPwrLowWngPortn,'pm1604AlmLine1RxPwrHighWngPortn':pm1604AlmLine1RxPwrHighWngPortn,'pm1604AlmClientUrg':pm1604AlmClientUrg,'pm1604Almline1SfpAlmDdmTable':pm1604Almline1SfpAlmDdmTable,'pm1604Almline1SfpAlmDdmEntry':pm1604Almline1SfpAlmDdmEntry,_V:pm1604Almline1SfpAlmDdmIndex,'pm1604AlmLine1TxPwrLowAlaPortn':pm1604AlmLine1TxPwrLowAlaPortn,'pm1604AlmLine1Line1TxPwrHighAlaPortn':pm1604AlmLine1Line1TxPwrHighAlaPortn,'pm1604AlmLine1TxBiasLowAlaPortn':pm1604AlmLine1TxBiasLowAlaPortn,'pm1604AlmLine1TxBiasHighAlaPortn':pm1604AlmLine1TxBiasHighAlaPortn,'pm1604AlmLine1VccLowAlaPortn':pm1604AlmLine1VccLowAlaPortn,'pm1604AlmLine1VccHighAlaPortn':pm1604AlmLine1VccHighAlaPortn,'pm1604AlmLine1TempLowAlaPortn':pm1604AlmLine1TempLowAlaPortn,'pm1604AlmLine1TempHighAlaPortn':pm1604AlmLine1TempHighAlaPortn,'pm1604AlmLine1RxPwrLowAlaPortn':pm1604AlmLine1RxPwrLowAlaPortn,'pm1604AlmLine1RxPwrHighAlaPortn':pm1604AlmLine1RxPwrHighAlaPortn,'pm1604AlmClientCrit':pm1604AlmClientCrit,'pm1604AlmsynthAlmLine1Table':pm1604AlmsynthAlmLine1Table,'pm1604AlmsynthAlmLine1Entry':pm1604AlmsynthAlmLine1Entry,_W:pm1604AlmsynthAlmLine1Index,'pm1604AlmLine1SfpAbsentPortn':pm1604AlmLine1SfpAbsentPortn,'pm1604AlmLine1DdmAbsentPortn':pm1604AlmLine1DdmAbsentPortn,_R:pm1604AlmLine1HwFailAccPortn,'pm1604AlmLine1LsdPortn':pm1604AlmLine1LsdPortn,'pm1604AlmLine1LocalOosPortn':pm1604AlmLine1LocalOosPortn,'pm1604AlmLine1DwCaisPortn':pm1604AlmLine1DwCaisPortn,_O:pm1604AlmLine1SfpDdmWarningPortn,_P:pm1604AlmLine1SfpDdmAlmPortn,_Q:pm1604AlmLine1FailAccPortn,'pm1604Almline1AccessioAlmTable':pm1604Almline1AccessioAlmTable,'pm1604Almline1AccessioAlmEntry':pm1604Almline1AccessioAlmEntry,_X:pm1604Almline1AccessioAlmIndex,'pm1604AlmLine1LasFailPortn':pm1604AlmLine1LasFailPortn,'pm1604AlmLine1LosPortn':pm1604AlmLine1LosPortn,'pm1604AlmLine1LosCdrPortn':pm1604AlmLine1LosCdrPortn,'pm1604AlmLine1ErrSigCdrPortn':pm1604AlmLine1ErrSigCdrPortn,'pm1604AlmLine':pm1604AlmLine,'pm1604AlmLineNurg':pm1604AlmLineNurg,'pm1604Almline2SfpWarnDdmTable':pm1604Almline2SfpWarnDdmTable,'pm1604Almline2SfpWarnDdmEntry':pm1604Almline2SfpWarnDdmEntry,_Y:pm1604Almline2SfpWarnDdmIndex,'pm1604AlmLine2TxPwLowWngPortn':pm1604AlmLine2TxPwLowWngPortn,'pm1604AlmLine2TxPwrHighWngPortn':pm1604AlmLine2TxPwrHighWngPortn,'pm1604AlmLine2TxBiasLowWngPortn':pm1604AlmLine2TxBiasLowWngPortn,'pm1604AlmLine2TxBiasHighWngPortn':pm1604AlmLine2TxBiasHighWngPortn,'pm1604AlmLine2VccLowWngPortn':pm1604AlmLine2VccLowWngPortn,'pm1604AlmLine2VccHighWngPortn':pm1604AlmLine2VccHighWngPortn,'pm1604AlmLine2TempLowWngPortn':pm1604AlmLine2TempLowWngPortn,'pm1604AlmLine2TempHighWngPortn':pm1604AlmLine2TempHighWngPortn,'pm1604AlmLine2RxPwrLowWngPortn':pm1604AlmLine2RxPwrLowWngPortn,'pm1604AlmLine2RxPwrHighWngPortn':pm1604AlmLine2RxPwrHighWngPortn,'pm1604AlmLineUrg':pm1604AlmLineUrg,'pm1604Almline2SfpAlmDdmTable':pm1604Almline2SfpAlmDdmTable,'pm1604Almline2SfpAlmDdmEntry':pm1604Almline2SfpAlmDdmEntry,_Z:pm1604Almline2SfpAlmDdmIndex,'pm1604AlmLine2TxPwrLowAlaPortn':pm1604AlmLine2TxPwrLowAlaPortn,'pm1604AlmLine2Line2TxPwrHighAlaPortn':pm1604AlmLine2Line2TxPwrHighAlaPortn,'pm1604AlmLine2TxBiasLowAlaPortn':pm1604AlmLine2TxBiasLowAlaPortn,'pm1604AlmLine2TxBiasHighAlaPortn':pm1604AlmLine2TxBiasHighAlaPortn,'pm1604AlmLine2VccLowAlaPortn':pm1604AlmLine2VccLowAlaPortn,'pm1604AlmLine2VccHighAlaPortn':pm1604AlmLine2VccHighAlaPortn,'pm1604AlmLine2TempLowAlaPortn':pm1604AlmLine2TempLowAlaPortn,'pm1604AlmLine2TempHighAlaPortn':pm1604AlmLine2TempHighAlaPortn,'pm1604AlmLine2RxPwrLowAlaPortn':pm1604AlmLine2RxPwrLowAlaPortn,'pm1604AlmLine2RxPwrHighAlaPortn':pm1604AlmLine2RxPwrHighAlaPortn,'pm1604AlmLineCrit':pm1604AlmLineCrit,'pm1604AlmsynthAlmLine2Table':pm1604AlmsynthAlmLine2Table,'pm1604AlmsynthAlmLine2Entry':pm1604AlmsynthAlmLine2Entry,_a:pm1604AlmsynthAlmLine2Index,'pm1604AlmLine2SfpAbsentPortn':pm1604AlmLine2SfpAbsentPortn,'pm1604AlmLine2DdmAbsentPortn':pm1604AlmLine2DdmAbsentPortn,_N:pm1604AlmLine2HwFailPortn,'pm1604AlmLine2LsdPortn':pm1604AlmLine2LsdPortn,'pm1604AlmLine2LocalOosPortn':pm1604AlmLine2LocalOosPortn,'pm1604AlmLine2DwCaisPortn':pm1604AlmLine2DwCaisPortn,_K:pm1604AlmLine2DdmWarningPortn,_L:pm1604AlmLine2DdmAlmPortn,_M:pm1604AlmLine2FailPortn,'pm1604Almline2AccessioAlmTable':pm1604Almline2AccessioAlmTable,'pm1604Almline2AccessioAlmEntry':pm1604Almline2AccessioAlmEntry,_b:pm1604Almline2AccessioAlmIndex,'pm1604AlmLine2LasFailPortn':pm1604AlmLine2LasFailPortn,'pm1604AlmLine2LosPortn':pm1604AlmLine2LosPortn,'pm1604AlmLine2LosCdrPortn':pm1604AlmLine2LosCdrPortn,'pm1604AlmLine2ErrSigCdrPortn':pm1604AlmLine2ErrSigCdrPortn,'pm1604measures':pm1604measures,'pm1604MesrOther':pm1604MesrOther,'pm1604MesrClient':pm1604MesrClient,'pm1604Mesrline1TemperatureTable':pm1604Mesrline1TemperatureTable,'pm1604Mesrline1TemperatureEntry':pm1604Mesrline1TemperatureEntry,_c:pm1604Mesrline1TemperatureIndex,'pm1604Mesrline1TemperaturePortn':pm1604Mesrline1TemperaturePortn,'pm1604Mesrline1VoltTable':pm1604Mesrline1VoltTable,'pm1604Mesrline1VoltEntry':pm1604Mesrline1VoltEntry,_d:pm1604Mesrline1VoltIndex,'pm1604Mesrline1VoltPortn':pm1604Mesrline1VoltPortn,'pm1604Mesrline1TxBiasTable':pm1604Mesrline1TxBiasTable,'pm1604Mesrline1TxBiasEntry':pm1604Mesrline1TxBiasEntry,_e:pm1604Mesrline1TxBiasIndex,'pm1604Mesrline1TxBiasPortn':pm1604Mesrline1TxBiasPortn,'pm1604Mesrline1TxPowerTable':pm1604Mesrline1TxPowerTable,'pm1604Mesrline1TxPowerEntry':pm1604Mesrline1TxPowerEntry,_f:pm1604Mesrline1TxPowerIndex,'pm1604Mesrline1TxPowerPortn':pm1604Mesrline1TxPowerPortn,'pm1604Mesrline1RxPowerTable':pm1604Mesrline1RxPowerTable,'pm1604Mesrline1RxPowerEntry':pm1604Mesrline1RxPowerEntry,_g:pm1604Mesrline1RxPowerIndex,'pm1604Mesrline1RxPowerPortn':pm1604Mesrline1RxPowerPortn,'pm1604MesrLine':pm1604MesrLine,'pm1604Mesrline2TemperatureTable':pm1604Mesrline2TemperatureTable,'pm1604Mesrline2TemperatureEntry':pm1604Mesrline2TemperatureEntry,_h:pm1604Mesrline2TemperatureIndex,'pm1604Mesrline2TemperaturePortn':pm1604Mesrline2TemperaturePortn,'pm1604Mesrline2VoltTable':pm1604Mesrline2VoltTable,'pm1604Mesrline2VoltEntry':pm1604Mesrline2VoltEntry,_i:pm1604Mesrline2VoltIndex,'pm1604Mesrline2VoltPortn':pm1604Mesrline2VoltPortn,'pm1604Mesrline2TxBiasTable':pm1604Mesrline2TxBiasTable,'pm1604Mesrline2TxBiasEntry':pm1604Mesrline2TxBiasEntry,_j:pm1604Mesrline2TxBiasIndex,'pm1604Mesrline2TxBiasPortn':pm1604Mesrline2TxBiasPortn,'pm1604Mesrline2TxPowerTable':pm1604Mesrline2TxPowerTable,'pm1604Mesrline2TxPowerEntry':pm1604Mesrline2TxPowerEntry,_k:pm1604Mesrline2TxPowerIndex,'pm1604Mesrline2TxPowerPortn':pm1604Mesrline2TxPowerPortn,'pm1604Mesrline2RxPowerTable':pm1604Mesrline2RxPowerTable,'pm1604Mesrline2RxPowerEntry':pm1604Mesrline2RxPowerEntry,_l:pm1604Mesrline2RxPowerIndex,'pm1604Mesrline2RxPowerPortn':pm1604Mesrline2RxPowerPortn,'pm1604counters':pm1604counters,'pm1604CntOther':pm1604CntOther,'pm1604CntClient':pm1604CntClient,'pm1604CntLine':pm1604CntLine,'pm1604controlsWrite':pm1604controlsWrite,'pm1604CtrlOther':pm1604CtrlOther,'pm1604Ctrlsynth0':pm1604Ctrlsynth0,'pm1604CtrlConfLoad':pm1604CtrlConfLoad,'pm1604CtrlConfFlash':pm1604CtrlConfFlash,'pm1604CtrlConfClear':pm1604CtrlConfClear,'pm1604Ctrlsynth4':pm1604Ctrlsynth4,'pm1604CtrlCorrelatOn':pm1604CtrlCorrelatOn,'pm1604CtrlCorrelatOff':pm1604CtrlCorrelatOff,'pm1604CtrlswMgnt':pm1604CtrlswMgnt,'pm1604CtrlColdReset':pm1604CtrlColdReset,'pm1604CtrlWarmReset':pm1604CtrlWarmReset,'pm1604CtrlledTest':pm1604CtrlledTest,'pm1604CtrlGreenLed':pm1604CtrlGreenLed,'pm1604CtrlRedLed':pm1604CtrlRedLed,'pm1604CtrlLedOff':pm1604CtrlLedOff,'pm1604CtrlmoduleOosMode':pm1604CtrlmoduleOosMode,'pm1604CtrlModuleOosMode':pm1604CtrlModuleOosMode,'pm1604CtrlClient':pm1604CtrlClient,'pm1604Ctrlline1SfpOnoffTable':pm1604Ctrlline1SfpOnoffTable,'pm1604Ctrlline1SfpOnoffEntry':pm1604Ctrlline1SfpOnoffEntry,_m:pm1604Ctrlline1SfpOnoffIndex,'pm1604Ctrlline1SfpOnoffPortn':pm1604Ctrlline1SfpOnoffPortn,'pm1604Ctrlline1LoopbackTable':pm1604Ctrlline1LoopbackTable,'pm1604Ctrlline1LoopbackEntry':pm1604Ctrlline1LoopbackEntry,_n:pm1604Ctrlline1LoopbackIndex,'pm1604Ctrlline1LoopbackPortn':pm1604Ctrlline1LoopbackPortn,'pm1604Ctrlline1LoopbackTermTable':pm1604Ctrlline1LoopbackTermTable,'pm1604Ctrlline1LoopbackTermEntry':pm1604Ctrlline1LoopbackTermEntry,_o:pm1604Ctrlline1LoopbackTermIndex,'pm1604Ctrlline1LoopbackTermPortn':pm1604Ctrlline1LoopbackTermPortn,'pm1604Ctrlline1OosModeTable':pm1604Ctrlline1OosModeTable,'pm1604Ctrlline1OosModeEntry':pm1604Ctrlline1OosModeEntry,_p:pm1604Ctrlline1OosModeIndex,'pm1604Ctrlline1OosModePortn':pm1604Ctrlline1OosModePortn,'pm1604CtrlprotocolTable':pm1604CtrlprotocolTable,'pm1604CtrlprotocolEntry':pm1604CtrlprotocolEntry,_q:pm1604CtrlprotocolIndex,'pm1604CtrlprotocolPortn':pm1604CtrlprotocolPortn,'pm1604CtrlLine':pm1604CtrlLine,'pm1604Ctrlline2SfpOnoffTable':pm1604Ctrlline2SfpOnoffTable,'pm1604Ctrlline2SfpOnoffEntry':pm1604Ctrlline2SfpOnoffEntry,_r:pm1604Ctrlline2SfpOnoffIndex,'pm1604Ctrlline2SfpOnoffPortn':pm1604Ctrlline2SfpOnoffPortn,'pm1604Ctrlline2OosModeTable':pm1604Ctrlline2OosModeTable,'pm1604Ctrlline2OosModeEntry':pm1604Ctrlline2OosModeEntry,_s:pm1604Ctrlline2OosModeIndex,'pm1604Ctrlline2OosModePortn':pm1604Ctrlline2OosModePortn,'pm1604Ctrlline2LoopbackTable':pm1604Ctrlline2LoopbackTable,'pm1604Ctrlline2LoopbackEntry':pm1604Ctrlline2LoopbackEntry,_t:pm1604Ctrlline2LoopbackIndex,'pm1604Ctrlline2LoopbackPortn':pm1604Ctrlline2LoopbackPortn,'pm1604Ctrlline2LoopbackTermTable':pm1604Ctrlline2LoopbackTermTable,'pm1604Ctrlline2LoopbackTermEntry':pm1604Ctrlline2LoopbackTermEntry,_u:pm1604Ctrlline2LoopbackTermIndex,'pm1604Ctrlline2LoopbackTermPortn':pm1604Ctrlline2LoopbackTermPortn,'pm1604ri':pm1604ri,'pm1604riTable':pm1604riTable,'pm1604RinvLine1Table':pm1604RinvLine1Table,'pm1604RinvLine1Entry':pm1604RinvLine1Entry,_v:pm1604RinvLine1Index,'pm1604RinvSfpLine1':pm1604RinvSfpLine1,'pm1604RinvLine2Table':pm1604RinvLine2Table,'pm1604RinvLine2Entry':pm1604RinvLine2Entry,_w:pm1604RinvLine2Index,'pm1604RinvsfpLine2':pm1604RinvsfpLine2,'pm1604RinvReloadInventory':pm1604RinvReloadInventory,'pm1604RinvHwPlatform':pm1604RinvHwPlatform,'pm1604RinvModulePlatform':pm1604RinvModulePlatform,'pm1604RinvSwPlatform':pm1604RinvSwPlatform,'pm1604RinvGwPlatform':pm1604RinvGwPlatform,'pm1604Config':pm1604Config,'pm1604CfgLsd':pm1604CfgLsd,'pm1604CfgLine1LsdTable':pm1604CfgLine1LsdTable,'pm1604CfgLine1LsdEntry':pm1604CfgLine1LsdEntry,_x:pm1604CfgLine1LsdIndex,'pm1604CfgLine1LsdModePortn':pm1604CfgLine1LsdModePortn,'pm1604CfgLine1AccessioCtrbInsPortn':pm1604CfgLine1AccessioCtrbInsPortn,'pm1604CfgLine2AccessioCtrbInsPortn':pm1604CfgLine2AccessioCtrbInsPortn,'pm1604CfgStartUp':pm1604CfgStartUp,'pm1604CfgLine1StartupTable':pm1604CfgLine1StartupTable,'pm1604CfgLine1StartupEntry':pm1604CfgLine1StartupEntry,_y:pm1604CfgLine1StartupIndex,'pm1604CfgLine1TrscvCtrlPortn':pm1604CfgLine1TrscvCtrlPortn,'pm1604CfgLine1ProtocolPortn':pm1604CfgLine1ProtocolPortn,'pm1604CfgLine1OosModePortn':pm1604CfgLine1OosModePortn,'pm1604CfgLine2StartupTable':pm1604CfgLine2StartupTable,'pm1604CfgLine2StartupEntry':pm1604CfgLine2StartupEntry,_z:pm1604CfgLine2StartupIndex,'pm1604CfgLine2TrscvCtrlPortn':pm1604CfgLine2TrscvCtrlPortn,'pm1604CfgLine2OosModePortn':pm1604CfgLine2OosModePortn,'pm1604CfgOtxtlhTable':pm1604CfgOtxtlhTable,'pm1604CfgOtxtlhEntry':pm1604CfgOtxtlhEntry,_A0:pm1604CfgOtxtlhIndex,'pm1604CfgLineControlsPortn':pm1604CfgLineControlsPortn,'pm1604CfgLinePwrLaserPortn':pm1604CfgLinePwrLaserPortn,'pm1604CfgLineFCurrentPortn':pm1604CfgLineFCurrentPortn,'pm1604CfgLineGridCurrentPortn':pm1604CfgLineGridCurrentPortn,'pm1604CfgLineFoPortn':pm1604CfgLineFoPortn,'pm1604CfgLabels':pm1604CfgLabels,'pm1604CfgLabelclientTable':pm1604CfgLabelclientTable,'pm1604CfgLabelclientEntry':pm1604CfgLabelclientEntry,_A1:pm1604CfgLabelclientIndex,'pm1604CfgLabelclientPortn':pm1604CfgLabelclientPortn,'pm1604CfgLabellineTable':pm1604CfgLabellineTable,'pm1604CfgLabellineEntry':pm1604CfgLabellineEntry,_A2:pm1604CfgLabellineIndex,'pm1604CfgLabellinePortn':pm1604CfgLabellinePortn,'pm1604CfgStartuptablefive':pm1604CfgStartuptablefive,'pm1604CfgOtxtlhcapabilitiesTable':pm1604CfgOtxtlhcapabilitiesTable,'pm1604CfgOtxtlhcapabilitiesEntry':pm1604CfgOtxtlhcapabilitiesEntry,_A3:pm1604CfgOtxtlhcapabilitiesIndex,'pm1604CfgComponentTypePortn':pm1604CfgComponentTypePortn,'pm1604CfgMiscellaneousPortn':pm1604CfgMiscellaneousPortn,'pm1604CfgFirstChannelPortn':pm1604CfgFirstChannelPortn,'pm1604CfgLastChannelPortn':pm1604CfgLastChannelPortn,'pm1604CfgGridPortn':pm1604CfgGridPortn,'pm1604CfgWriteConfiguration':pm1604CfgWriteConfiguration,'pm1604traps':pm1604traps,_I:pm1604trapPortNumber,_H:pm1604trapLineNumber,_G:pm1604trapBoardNumber,'pm1604Line2TrapNotUrgentGoesOn':pm1604Line2TrapNotUrgentGoesOn,'pm1604Line2TrapNotUrgentGoesOff':pm1604Line2TrapNotUrgentGoesOff,'pm1604Line2TrapUrgentGoesOn':pm1604Line2TrapUrgentGoesOn,'pm1604Line2TrapUrgentGoesOff':pm1604Line2TrapUrgentGoesOff,'pm1604Line2TrapCritGoesOn':pm1604Line2TrapCritGoesOn,'pm1604Line2TrapCritGoesOff':pm1604Line2TrapCritGoesOff,'pm1604Line1TrapNotUrgentGoesOn':pm1604Line1TrapNotUrgentGoesOn,'pm1604Line1TrapNotUrgentGoesOff':pm1604Line1TrapNotUrgentGoesOff,'pm1604Line1TrapUrgentGoesOn':pm1604Line1TrapUrgentGoesOn,'pm1604Line1TrapUrgentGoesOff':pm1604Line1TrapUrgentGoesOff,'pm1604Line1TrapCritGoesOn':pm1604Line1TrapCritGoesOn,'pm1604Line1TrapCritGoesOff':pm1604Line1TrapCritGoesOff,'pm1604PowerTrapUrgentGoesOn':pm1604PowerTrapUrgentGoesOn,'pm1604PowerTrapUrgentGoesOff':pm1604PowerTrapUrgentGoesOff})