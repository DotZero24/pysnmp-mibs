_V='pm801rrCfgOtxtlhcapabilitiesIndex'
_U='pm801rrCfgLabellineIndex'
_T='pm801rrCfgLabelclientIndex'
_S='2010-08-26 00:00'
_R='pm801rrAlmDefFuseA'
_Q='pm801rrAlmDefFuseB'
_P='pm801rrAlmClientHwFail'
_O='pm801rrAlmClientFail'
_N='pm801rrAlmClientDdmAlm'
_M='pm801rrAlmClientDdmWarning'
_L='pm801rrAlmLineHwFail'
_K='pm801rrAlmLineFail'
_J='pm801rrAlmLineDdmAlm'
_I='pm801rrAlmLineDdmWarning'
_H='DisplayString'
_G='Integer32'
_F='pm801rrtrapBoardNumber'
_E='EKINOPS-Pm801RR-MIB'
_D='Unsigned32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
modulePm801RR=ModuleIdentity((1,3,6,1,4,1,20044,48))
if mibBuilder.loadTexts:modulePm801RR.setRevisions((_S,_S,'2010-11-03 00:00','2012-07-04 00:00','2014-03-25 00:00','2014-12-09 00:00','2016-05-23 00:00','2016-06-07 00:00'))
class Pm801rrBitRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('rateOC192',0),('rate10GBELAN',1),('rate10GBEWAN',2),('rate10GFC',3),('rate10FECG975',4),('rate10FECG709',5)))
class Pm801rrOtxMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('otx80mode',1),('otx60mode',2),('otxadjustmode',4)))
class Pm801rrOtxGrid(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200)));namedValues=NamedValues(*(('otxgrid50',50),('otxgrid100',100),('otxgrid200',200)))
class Pm801rrAdjustValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('otxadjustvalue0',0),('otxadjustvalue1',1),('otxadjustvalue2',2),('otxadjustvalue3',3),('otxadjustvalue4',4),('otxadjustvalue5',5),('otxadjustvalue6',6),('otxadjustvalue7',7),('otxadjustvalue8',8),('otxadjustvalue9',9),('otxadjustvalue10',10)))
class Pm801rrOtxChannel(TextualConvention,Integer32):status=_A
_Pm801rralarms_ObjectIdentity=ObjectIdentity
pm801rralarms=_Pm801rralarms_ObjectIdentity((1,3,6,1,4,1,20044,48,2))
_Pm801rrAlmOther_ObjectIdentity=ObjectIdentity
pm801rrAlmOther=_Pm801rrAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,48,2,1))
_Pm801rrAlmOtherNurg_ObjectIdentity=ObjectIdentity
pm801rrAlmOtherNurg=_Pm801rrAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,48,2,1,1))
_Pm801rrAlmOtherUrg_ObjectIdentity=ObjectIdentity
pm801rrAlmOtherUrg=_Pm801rrAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,48,2,1,2))
_Pm801rrAlmOtherCrit_ObjectIdentity=ObjectIdentity
pm801rrAlmOtherCrit=_Pm801rrAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,48,2,1,3))
_Pm801rrAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pm801rrAlmsynthAlm0=_Pm801rrAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,48,2,1,3,0))
_Pm801rrAlmModuleGlobFailure_Type=EkiOnOff
_Pm801rrAlmModuleGlobFailure_Object=MibScalar
pm801rrAlmModuleGlobFailure=_Pm801rrAlmModuleGlobFailure_Object((1,3,6,1,4,1,20044,48,2,1,3,0,9),_Pm801rrAlmModuleGlobFailure_Type())
pm801rrAlmModuleGlobFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmModuleGlobFailure.setStatus(_A)
_Pm801rrAlmDefFuseA_Type=EkiOnOff
_Pm801rrAlmDefFuseA_Object=MibScalar
pm801rrAlmDefFuseA=_Pm801rrAlmDefFuseA_Object((1,3,6,1,4,1,20044,48,2,1,3,0,15),_Pm801rrAlmDefFuseA_Type())
pm801rrAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmDefFuseA.setStatus(_A)
_Pm801rrAlmDefFuseB_Type=EkiOnOff
_Pm801rrAlmDefFuseB_Object=MibScalar
pm801rrAlmDefFuseB=_Pm801rrAlmDefFuseB_Object((1,3,6,1,4,1,20044,48,2,1,3,0,16),_Pm801rrAlmDefFuseB_Type())
pm801rrAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmDefFuseB.setStatus(_A)
_Pm801rrAlmClient_ObjectIdentity=ObjectIdentity
pm801rrAlmClient=_Pm801rrAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2))
_Pm801rrAlmClientNurg_ObjectIdentity=ObjectIdentity
pm801rrAlmClientNurg=_Pm801rrAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,1))
_Pm801rrAlmclientXfpWarnings_ObjectIdentity=ObjectIdentity
pm801rrAlmclientXfpWarnings=_Pm801rrAlmclientXfpWarnings_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,1,17))
_Pm801rrAlmClientTxPwrLowWng_Type=EkiOnOff
_Pm801rrAlmClientTxPwrLowWng_Object=MibScalar
pm801rrAlmClientTxPwrLowWng=_Pm801rrAlmClientTxPwrLowWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,1),_Pm801rrAlmClientTxPwrLowWng_Type())
pm801rrAlmClientTxPwrLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxPwrLowWng.setStatus(_A)
_Pm801rrAlmClientTxPwrHighWng_Type=EkiOnOff
_Pm801rrAlmClientTxPwrHighWng_Object=MibScalar
pm801rrAlmClientTxPwrHighWng=_Pm801rrAlmClientTxPwrHighWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,2),_Pm801rrAlmClientTxPwrHighWng_Type())
pm801rrAlmClientTxPwrHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxPwrHighWng.setStatus(_A)
_Pm801rrAlmClientTxBiasLowWng_Type=EkiOnOff
_Pm801rrAlmClientTxBiasLowWng_Object=MibScalar
pm801rrAlmClientTxBiasLowWng=_Pm801rrAlmClientTxBiasLowWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,3),_Pm801rrAlmClientTxBiasLowWng_Type())
pm801rrAlmClientTxBiasLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxBiasLowWng.setStatus(_A)
_Pm801rrAlmClientTxBiasHighWng_Type=EkiOnOff
_Pm801rrAlmClientTxBiasHighWng_Object=MibScalar
pm801rrAlmClientTxBiasHighWng=_Pm801rrAlmClientTxBiasHighWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,4),_Pm801rrAlmClientTxBiasHighWng_Type())
pm801rrAlmClientTxBiasHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxBiasHighWng.setStatus(_A)
_Pm801rrAlmClientTempLowWng_Type=EkiOnOff
_Pm801rrAlmClientTempLowWng_Object=MibScalar
pm801rrAlmClientTempLowWng=_Pm801rrAlmClientTempLowWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,7),_Pm801rrAlmClientTempLowWng_Type())
pm801rrAlmClientTempLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTempLowWng.setStatus(_A)
_Pm801rrAlmClientTempHighWng_Type=EkiOnOff
_Pm801rrAlmClientTempHighWng_Object=MibScalar
pm801rrAlmClientTempHighWng=_Pm801rrAlmClientTempHighWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,8),_Pm801rrAlmClientTempHighWng_Type())
pm801rrAlmClientTempHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTempHighWng.setStatus(_A)
_Pm801rrAlmClientRxPwrLowWng_Type=EkiOnOff
_Pm801rrAlmClientRxPwrLowWng_Object=MibScalar
pm801rrAlmClientRxPwrLowWng=_Pm801rrAlmClientRxPwrLowWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,15),_Pm801rrAlmClientRxPwrLowWng_Type())
pm801rrAlmClientRxPwrLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxPwrLowWng.setStatus(_A)
_Pm801rrAlmClientRxPwrHighWng_Type=EkiOnOff
_Pm801rrAlmClientRxPwrHighWng_Object=MibScalar
pm801rrAlmClientRxPwrHighWng=_Pm801rrAlmClientRxPwrHighWng_Object((1,3,6,1,4,1,20044,48,2,2,1,17,16),_Pm801rrAlmClientRxPwrHighWng_Type())
pm801rrAlmClientRxPwrHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxPwrHighWng.setStatus(_A)
_Pm801rrAlmclientOtxTlhWarnings_ObjectIdentity=ObjectIdentity
pm801rrAlmclientOtxTlhWarnings=_Pm801rrAlmclientOtxTlhWarnings_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,1,23))
_Pm801rrAlmClientModulatorAgingHighWarning_Type=EkiOnOff
_Pm801rrAlmClientModulatorAgingHighWarning_Object=MibScalar
pm801rrAlmClientModulatorAgingHighWarning=_Pm801rrAlmClientModulatorAgingHighWarning_Object((1,3,6,1,4,1,20044,48,2,2,1,23,5),_Pm801rrAlmClientModulatorAgingHighWarning_Type())
pm801rrAlmClientModulatorAgingHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientModulatorAgingHighWarning.setStatus(_A)
_Pm801rrAlmClientAgingHighWarning_Type=EkiOnOff
_Pm801rrAlmClientAgingHighWarning_Object=MibScalar
pm801rrAlmClientAgingHighWarning=_Pm801rrAlmClientAgingHighWarning_Object((1,3,6,1,4,1,20044,48,2,2,1,23,6),_Pm801rrAlmClientAgingHighWarning_Type())
pm801rrAlmClientAgingHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientAgingHighWarning.setStatus(_A)
_Pm801rrAlmClientFreqDevHighWarning_Type=EkiOnOff
_Pm801rrAlmClientFreqDevHighWarning_Object=MibScalar
pm801rrAlmClientFreqDevHighWarning=_Pm801rrAlmClientFreqDevHighWarning_Object((1,3,6,1,4,1,20044,48,2,2,1,23,12),_Pm801rrAlmClientFreqDevHighWarning_Type())
pm801rrAlmClientFreqDevHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientFreqDevHighWarning.setStatus(_A)
_Pm801rrAlmClientLaserTempHighWarning_Type=EkiOnOff
_Pm801rrAlmClientLaserTempHighWarning_Object=MibScalar
pm801rrAlmClientLaserTempHighWarning=_Pm801rrAlmClientLaserTempHighWarning_Object((1,3,6,1,4,1,20044,48,2,2,1,23,14),_Pm801rrAlmClientLaserTempHighWarning_Type())
pm801rrAlmClientLaserTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientLaserTempHighWarning.setStatus(_A)
_Pm801rrAlmClientUrg_ObjectIdentity=ObjectIdentity
pm801rrAlmClientUrg=_Pm801rrAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,2))
_Pm801rrAlmclientXfpAlarm1_ObjectIdentity=ObjectIdentity
pm801rrAlmclientXfpAlarm1=_Pm801rrAlmclientXfpAlarm1_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,2,16))
_Pm801rrAlmClientTxPwrLowAla_Type=EkiOnOff
_Pm801rrAlmClientTxPwrLowAla_Object=MibScalar
pm801rrAlmClientTxPwrLowAla=_Pm801rrAlmClientTxPwrLowAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,1),_Pm801rrAlmClientTxPwrLowAla_Type())
pm801rrAlmClientTxPwrLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxPwrLowAla.setStatus(_A)
_Pm801rrAlmClientTxPwrHighAla_Type=EkiOnOff
_Pm801rrAlmClientTxPwrHighAla_Object=MibScalar
pm801rrAlmClientTxPwrHighAla=_Pm801rrAlmClientTxPwrHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,2),_Pm801rrAlmClientTxPwrHighAla_Type())
pm801rrAlmClientTxPwrHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxPwrHighAla.setStatus(_A)
_Pm801rrAlmClientTxBiasLowAla_Type=EkiOnOff
_Pm801rrAlmClientTxBiasLowAla_Object=MibScalar
pm801rrAlmClientTxBiasLowAla=_Pm801rrAlmClientTxBiasLowAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,3),_Pm801rrAlmClientTxBiasLowAla_Type())
pm801rrAlmClientTxBiasLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxBiasLowAla.setStatus(_A)
_Pm801rrAlmClientTxBiasHighAla_Type=EkiOnOff
_Pm801rrAlmClientTxBiasHighAla_Object=MibScalar
pm801rrAlmClientTxBiasHighAla=_Pm801rrAlmClientTxBiasHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,4),_Pm801rrAlmClientTxBiasHighAla_Type())
pm801rrAlmClientTxBiasHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxBiasHighAla.setStatus(_A)
_Pm801rrAlmClientTempLowAla_Type=EkiOnOff
_Pm801rrAlmClientTempLowAla_Object=MibScalar
pm801rrAlmClientTempLowAla=_Pm801rrAlmClientTempLowAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,7),_Pm801rrAlmClientTempLowAla_Type())
pm801rrAlmClientTempLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTempLowAla.setStatus(_A)
_Pm801rrAlmClientTempHighAla_Type=EkiOnOff
_Pm801rrAlmClientTempHighAla_Object=MibScalar
pm801rrAlmClientTempHighAla=_Pm801rrAlmClientTempHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,8),_Pm801rrAlmClientTempHighAla_Type())
pm801rrAlmClientTempHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTempHighAla.setStatus(_A)
_Pm801rrAlmClientRxPwrLowAla_Type=EkiOnOff
_Pm801rrAlmClientRxPwrLowAla_Object=MibScalar
pm801rrAlmClientRxPwrLowAla=_Pm801rrAlmClientRxPwrLowAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,15),_Pm801rrAlmClientRxPwrLowAla_Type())
pm801rrAlmClientRxPwrLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxPwrLowAla.setStatus(_A)
_Pm801rrAlmClientRxPwrHighAla_Type=EkiOnOff
_Pm801rrAlmClientRxPwrHighAla_Object=MibScalar
pm801rrAlmClientRxPwrHighAla=_Pm801rrAlmClientRxPwrHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,16,16),_Pm801rrAlmClientRxPwrHighAla_Type())
pm801rrAlmClientRxPwrHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxPwrHighAla.setStatus(_A)
_Pm801rrAlmclientOtxTlhAlarms3_ObjectIdentity=ObjectIdentity
pm801rrAlmclientOtxTlhAlarms3=_Pm801rrAlmclientOtxTlhAlarms3_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,2,22))
_Pm801rrAlmClientModulatorAgingHighAla_Type=EkiOnOff
_Pm801rrAlmClientModulatorAgingHighAla_Object=MibScalar
pm801rrAlmClientModulatorAgingHighAla=_Pm801rrAlmClientModulatorAgingHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,22,5),_Pm801rrAlmClientModulatorAgingHighAla_Type())
pm801rrAlmClientModulatorAgingHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientModulatorAgingHighAla.setStatus(_A)
_Pm801rrAlmClientAgingHighAla_Type=EkiOnOff
_Pm801rrAlmClientAgingHighAla_Object=MibScalar
pm801rrAlmClientAgingHighAla=_Pm801rrAlmClientAgingHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,22,6),_Pm801rrAlmClientAgingHighAla_Type())
pm801rrAlmClientAgingHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientAgingHighAla.setStatus(_A)
_Pm801rrAlmClientCdrNotReady_Type=EkiOnOff
_Pm801rrAlmClientCdrNotReady_Object=MibScalar
pm801rrAlmClientCdrNotReady=_Pm801rrAlmClientCdrNotReady_Object((1,3,6,1,4,1,20044,48,2,2,2,22,9),_Pm801rrAlmClientCdrNotReady_Type())
pm801rrAlmClientCdrNotReady.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientCdrNotReady.setStatus(_A)
_Pm801rrAlmClientFreqDevHighAla_Type=EkiOnOff
_Pm801rrAlmClientFreqDevHighAla_Object=MibScalar
pm801rrAlmClientFreqDevHighAla=_Pm801rrAlmClientFreqDevHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,22,12),_Pm801rrAlmClientFreqDevHighAla_Type())
pm801rrAlmClientFreqDevHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientFreqDevHighAla.setStatus(_A)
_Pm801rrAlmClientLaserTempHighAla_Type=EkiOnOff
_Pm801rrAlmClientLaserTempHighAla_Object=MibScalar
pm801rrAlmClientLaserTempHighAla=_Pm801rrAlmClientLaserTempHighAla_Object((1,3,6,1,4,1,20044,48,2,2,2,22,14),_Pm801rrAlmClientLaserTempHighAla_Type())
pm801rrAlmClientLaserTempHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientLaserTempHighAla.setStatus(_A)
_Pm801rrAlmClientCrit_ObjectIdentity=ObjectIdentity
pm801rrAlmClientCrit=_Pm801rrAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,3))
_Pm801rrAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pm801rrAlmsynthAlm8=_Pm801rrAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,3,8))
_Pm801rrAlmClientXfpAbsent_Type=EkiOnOff
_Pm801rrAlmClientXfpAbsent_Object=MibScalar
pm801rrAlmClientXfpAbsent=_Pm801rrAlmClientXfpAbsent_Object((1,3,6,1,4,1,20044,48,2,2,3,8,1),_Pm801rrAlmClientXfpAbsent_Type())
pm801rrAlmClientXfpAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientXfpAbsent.setStatus(_A)
_Pm801rrAlmClientInitNotCompl_Type=EkiOnOff
_Pm801rrAlmClientInitNotCompl_Object=MibScalar
pm801rrAlmClientInitNotCompl=_Pm801rrAlmClientInitNotCompl_Object((1,3,6,1,4,1,20044,48,2,2,3,8,2),_Pm801rrAlmClientInitNotCompl_Type())
pm801rrAlmClientInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientInitNotCompl.setStatus(_A)
_Pm801rrAlmClientHwFail_Type=EkiOnOff
_Pm801rrAlmClientHwFail_Object=MibScalar
pm801rrAlmClientHwFail=_Pm801rrAlmClientHwFail_Object((1,3,6,1,4,1,20044,48,2,2,3,8,4),_Pm801rrAlmClientHwFail_Type())
pm801rrAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientHwFail.setStatus(_A)
_Pm801rrAlmClientXfpTxOff_Type=EkiOnOff
_Pm801rrAlmClientXfpTxOff_Object=MibScalar
pm801rrAlmClientXfpTxOff=_Pm801rrAlmClientXfpTxOff_Object((1,3,6,1,4,1,20044,48,2,2,3,8,5),_Pm801rrAlmClientXfpTxOff_Type())
pm801rrAlmClientXfpTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientXfpTxOff.setStatus(_A)
_Pm801rrAlmClientDdmWarning_Type=EkiOnOff
_Pm801rrAlmClientDdmWarning_Object=MibScalar
pm801rrAlmClientDdmWarning=_Pm801rrAlmClientDdmWarning_Object((1,3,6,1,4,1,20044,48,2,2,3,8,9),_Pm801rrAlmClientDdmWarning_Type())
pm801rrAlmClientDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientDdmWarning.setStatus(_A)
_Pm801rrAlmClientDdmAlm_Type=EkiOnOff
_Pm801rrAlmClientDdmAlm_Object=MibScalar
pm801rrAlmClientDdmAlm=_Pm801rrAlmClientDdmAlm_Object((1,3,6,1,4,1,20044,48,2,2,3,8,10),_Pm801rrAlmClientDdmAlm_Type())
pm801rrAlmClientDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientDdmAlm.setStatus(_A)
_Pm801rrAlmClientFail_Type=EkiOnOff
_Pm801rrAlmClientFail_Object=MibScalar
pm801rrAlmClientFail=_Pm801rrAlmClientFail_Object((1,3,6,1,4,1,20044,48,2,2,3,8,12),_Pm801rrAlmClientFail_Type())
pm801rrAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientFail.setStatus(_A)
_Pm801rrAlmClientVccWarning_Type=EkiOnOff
_Pm801rrAlmClientVccWarning_Object=MibScalar
pm801rrAlmClientVccWarning=_Pm801rrAlmClientVccWarning_Object((1,3,6,1,4,1,20044,48,2,2,3,8,14),_Pm801rrAlmClientVccWarning_Type())
pm801rrAlmClientVccWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientVccWarning.setStatus(_A)
_Pm801rrAlmClientVccAlarm_Type=EkiOnOff
_Pm801rrAlmClientVccAlarm_Object=MibScalar
pm801rrAlmClientVccAlarm=_Pm801rrAlmClientVccAlarm_Object((1,3,6,1,4,1,20044,48,2,2,3,8,15),_Pm801rrAlmClientVccAlarm_Type())
pm801rrAlmClientVccAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientVccAlarm.setStatus(_A)
_Pm801rrAlmclientXfpAlarms2_ObjectIdentity=ObjectIdentity
pm801rrAlmclientXfpAlarms2=_Pm801rrAlmclientXfpAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,48,2,2,3,19))
_Pm801rrAlmClientResetComplete_Type=EkiOnOff
_Pm801rrAlmClientResetComplete_Object=MibScalar
pm801rrAlmClientResetComplete=_Pm801rrAlmClientResetComplete_Object((1,3,6,1,4,1,20044,48,2,2,3,19,1),_Pm801rrAlmClientResetComplete_Type())
pm801rrAlmClientResetComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientResetComplete.setStatus(_A)
_Pm801rrAlmClientRxCdrNotLocked_Type=EkiOnOff
_Pm801rrAlmClientRxCdrNotLocked_Object=MibScalar
pm801rrAlmClientRxCdrNotLocked=_Pm801rrAlmClientRxCdrNotLocked_Object((1,3,6,1,4,1,20044,48,2,2,3,19,3),_Pm801rrAlmClientRxCdrNotLocked_Type())
pm801rrAlmClientRxCdrNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxCdrNotLocked.setStatus(_A)
_Pm801rrAlmClientRxLos_Type=EkiOnOff
_Pm801rrAlmClientRxLos_Object=MibScalar
pm801rrAlmClientRxLos=_Pm801rrAlmClientRxLos_Object((1,3,6,1,4,1,20044,48,2,2,3,19,4),_Pm801rrAlmClientRxLos_Type())
pm801rrAlmClientRxLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxLos.setStatus(_A)
_Pm801rrAlmClientRxNr_Type=EkiOnOff
_Pm801rrAlmClientRxNr_Object=MibScalar
pm801rrAlmClientRxNr=_Pm801rrAlmClientRxNr_Object((1,3,6,1,4,1,20044,48,2,2,3,19,5),_Pm801rrAlmClientRxNr_Type())
pm801rrAlmClientRxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientRxNr.setStatus(_A)
_Pm801rrAlmClientTxCdrNotLocked_Type=EkiOnOff
_Pm801rrAlmClientTxCdrNotLocked_Object=MibScalar
pm801rrAlmClientTxCdrNotLocked=_Pm801rrAlmClientTxCdrNotLocked_Object((1,3,6,1,4,1,20044,48,2,2,3,19,6),_Pm801rrAlmClientTxCdrNotLocked_Type())
pm801rrAlmClientTxCdrNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxCdrNotLocked.setStatus(_A)
_Pm801rrAlmClientTxFault_Type=EkiOnOff
_Pm801rrAlmClientTxFault_Object=MibScalar
pm801rrAlmClientTxFault=_Pm801rrAlmClientTxFault_Object((1,3,6,1,4,1,20044,48,2,2,3,19,7),_Pm801rrAlmClientTxFault_Type())
pm801rrAlmClientTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxFault.setStatus(_A)
_Pm801rrAlmClientTxNr_Type=EkiOnOff
_Pm801rrAlmClientTxNr_Object=MibScalar
pm801rrAlmClientTxNr=_Pm801rrAlmClientTxNr_Object((1,3,6,1,4,1,20044,48,2,2,3,19,8),_Pm801rrAlmClientTxNr_Type())
pm801rrAlmClientTxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTxNr.setStatus(_A)
_Pm801rrAlmClientChannelNotAcquired_Type=EkiOnOff
_Pm801rrAlmClientChannelNotAcquired_Object=MibScalar
pm801rrAlmClientChannelNotAcquired=_Pm801rrAlmClientChannelNotAcquired_Object((1,3,6,1,4,1,20044,48,2,2,3,19,10),_Pm801rrAlmClientChannelNotAcquired_Type())
pm801rrAlmClientChannelNotAcquired.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientChannelNotAcquired.setStatus(_A)
_Pm801rrAlmClientWavelengthUnlocked_Type=EkiOnOff
_Pm801rrAlmClientWavelengthUnlocked_Object=MibScalar
pm801rrAlmClientWavelengthUnlocked=_Pm801rrAlmClientWavelengthUnlocked_Object((1,3,6,1,4,1,20044,48,2,2,3,19,14),_Pm801rrAlmClientWavelengthUnlocked_Type())
pm801rrAlmClientWavelengthUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientWavelengthUnlocked.setStatus(_A)
_Pm801rrAlmClientTecFault_Type=EkiOnOff
_Pm801rrAlmClientTecFault_Object=MibScalar
pm801rrAlmClientTecFault=_Pm801rrAlmClientTecFault_Object((1,3,6,1,4,1,20044,48,2,2,3,19,15),_Pm801rrAlmClientTecFault_Type())
pm801rrAlmClientTecFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientTecFault.setStatus(_A)
_Pm801rrAlmClientApdSupplyFault_Type=EkiOnOff
_Pm801rrAlmClientApdSupplyFault_Object=MibScalar
pm801rrAlmClientApdSupplyFault=_Pm801rrAlmClientApdSupplyFault_Object((1,3,6,1,4,1,20044,48,2,2,3,19,16),_Pm801rrAlmClientApdSupplyFault_Type())
pm801rrAlmClientApdSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmClientApdSupplyFault.setStatus(_A)
_Pm801rrAlmLine_ObjectIdentity=ObjectIdentity
pm801rrAlmLine=_Pm801rrAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3))
_Pm801rrAlmLineNurg_ObjectIdentity=ObjectIdentity
pm801rrAlmLineNurg=_Pm801rrAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,1))
_Pm801rrAlmlineXfpWarnings_ObjectIdentity=ObjectIdentity
pm801rrAlmlineXfpWarnings=_Pm801rrAlmlineXfpWarnings_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,1,25))
_Pm801rrAlmLineTxPwrLowWng_Type=EkiOnOff
_Pm801rrAlmLineTxPwrLowWng_Object=MibScalar
pm801rrAlmLineTxPwrLowWng=_Pm801rrAlmLineTxPwrLowWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,1),_Pm801rrAlmLineTxPwrLowWng_Type())
pm801rrAlmLineTxPwrLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxPwrLowWng.setStatus(_A)
_Pm801rrAlmLineTxPwrHighWng_Type=EkiOnOff
_Pm801rrAlmLineTxPwrHighWng_Object=MibScalar
pm801rrAlmLineTxPwrHighWng=_Pm801rrAlmLineTxPwrHighWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,2),_Pm801rrAlmLineTxPwrHighWng_Type())
pm801rrAlmLineTxPwrHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxPwrHighWng.setStatus(_A)
_Pm801rrAlmLineTxBiasLowWng_Type=EkiOnOff
_Pm801rrAlmLineTxBiasLowWng_Object=MibScalar
pm801rrAlmLineTxBiasLowWng=_Pm801rrAlmLineTxBiasLowWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,3),_Pm801rrAlmLineTxBiasLowWng_Type())
pm801rrAlmLineTxBiasLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxBiasLowWng.setStatus(_A)
_Pm801rrAlmLineTxBiasHighWng_Type=EkiOnOff
_Pm801rrAlmLineTxBiasHighWng_Object=MibScalar
pm801rrAlmLineTxBiasHighWng=_Pm801rrAlmLineTxBiasHighWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,4),_Pm801rrAlmLineTxBiasHighWng_Type())
pm801rrAlmLineTxBiasHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxBiasHighWng.setStatus(_A)
_Pm801rrAlmLineTempLowWng_Type=EkiOnOff
_Pm801rrAlmLineTempLowWng_Object=MibScalar
pm801rrAlmLineTempLowWng=_Pm801rrAlmLineTempLowWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,7),_Pm801rrAlmLineTempLowWng_Type())
pm801rrAlmLineTempLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTempLowWng.setStatus(_A)
_Pm801rrAlmLineTempHighWng_Type=EkiOnOff
_Pm801rrAlmLineTempHighWng_Object=MibScalar
pm801rrAlmLineTempHighWng=_Pm801rrAlmLineTempHighWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,8),_Pm801rrAlmLineTempHighWng_Type())
pm801rrAlmLineTempHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTempHighWng.setStatus(_A)
_Pm801rrAlmLineRxPwrLowWng_Type=EkiOnOff
_Pm801rrAlmLineRxPwrLowWng_Object=MibScalar
pm801rrAlmLineRxPwrLowWng=_Pm801rrAlmLineRxPwrLowWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,15),_Pm801rrAlmLineRxPwrLowWng_Type())
pm801rrAlmLineRxPwrLowWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxPwrLowWng.setStatus(_A)
_Pm801rrAlmLineRxPwrHighWng_Type=EkiOnOff
_Pm801rrAlmLineRxPwrHighWng_Object=MibScalar
pm801rrAlmLineRxPwrHighWng=_Pm801rrAlmLineRxPwrHighWng_Object((1,3,6,1,4,1,20044,48,2,3,1,25,16),_Pm801rrAlmLineRxPwrHighWng_Type())
pm801rrAlmLineRxPwrHighWng.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxPwrHighWng.setStatus(_A)
_Pm801rrAlmrrLineOtxTlhWarnings_ObjectIdentity=ObjectIdentity
pm801rrAlmrrLineOtxTlhWarnings=_Pm801rrAlmrrLineOtxTlhWarnings_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,1,31))
_Pm801rrAlmLineModulatorAgingHighWarning_Type=EkiOnOff
_Pm801rrAlmLineModulatorAgingHighWarning_Object=MibScalar
pm801rrAlmLineModulatorAgingHighWarning=_Pm801rrAlmLineModulatorAgingHighWarning_Object((1,3,6,1,4,1,20044,48,2,3,1,31,5),_Pm801rrAlmLineModulatorAgingHighWarning_Type())
pm801rrAlmLineModulatorAgingHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineModulatorAgingHighWarning.setStatus(_A)
_Pm801rrAlmLineAgingHighWarning_Type=EkiOnOff
_Pm801rrAlmLineAgingHighWarning_Object=MibScalar
pm801rrAlmLineAgingHighWarning=_Pm801rrAlmLineAgingHighWarning_Object((1,3,6,1,4,1,20044,48,2,3,1,31,6),_Pm801rrAlmLineAgingHighWarning_Type())
pm801rrAlmLineAgingHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineAgingHighWarning.setStatus(_A)
_Pm801rrAlmLineFreqDevHighWarning_Type=EkiOnOff
_Pm801rrAlmLineFreqDevHighWarning_Object=MibScalar
pm801rrAlmLineFreqDevHighWarning=_Pm801rrAlmLineFreqDevHighWarning_Object((1,3,6,1,4,1,20044,48,2,3,1,31,12),_Pm801rrAlmLineFreqDevHighWarning_Type())
pm801rrAlmLineFreqDevHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineFreqDevHighWarning.setStatus(_A)
_Pm801rrAlmLineLaserTempHighWarning_Type=EkiOnOff
_Pm801rrAlmLineLaserTempHighWarning_Object=MibScalar
pm801rrAlmLineLaserTempHighWarning=_Pm801rrAlmLineLaserTempHighWarning_Object((1,3,6,1,4,1,20044,48,2,3,1,31,14),_Pm801rrAlmLineLaserTempHighWarning_Type())
pm801rrAlmLineLaserTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineLaserTempHighWarning.setStatus(_A)
_Pm801rrAlmLineUrg_ObjectIdentity=ObjectIdentity
pm801rrAlmLineUrg=_Pm801rrAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,2))
_Pm801rrAlmlineXfpAlarm1_ObjectIdentity=ObjectIdentity
pm801rrAlmlineXfpAlarm1=_Pm801rrAlmlineXfpAlarm1_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,2,24))
_Pm801rrAlmLineTxPwrLowAla_Type=EkiOnOff
_Pm801rrAlmLineTxPwrLowAla_Object=MibScalar
pm801rrAlmLineTxPwrLowAla=_Pm801rrAlmLineTxPwrLowAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,1),_Pm801rrAlmLineTxPwrLowAla_Type())
pm801rrAlmLineTxPwrLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxPwrLowAla.setStatus(_A)
_Pm801rrAlmLineTxPwrHighAla_Type=EkiOnOff
_Pm801rrAlmLineTxPwrHighAla_Object=MibScalar
pm801rrAlmLineTxPwrHighAla=_Pm801rrAlmLineTxPwrHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,2),_Pm801rrAlmLineTxPwrHighAla_Type())
pm801rrAlmLineTxPwrHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxPwrHighAla.setStatus(_A)
_Pm801rrAlmLineTxBiasLowAla_Type=EkiOnOff
_Pm801rrAlmLineTxBiasLowAla_Object=MibScalar
pm801rrAlmLineTxBiasLowAla=_Pm801rrAlmLineTxBiasLowAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,3),_Pm801rrAlmLineTxBiasLowAla_Type())
pm801rrAlmLineTxBiasLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxBiasLowAla.setStatus(_A)
_Pm801rrAlmLineTxBiasHighAla_Type=EkiOnOff
_Pm801rrAlmLineTxBiasHighAla_Object=MibScalar
pm801rrAlmLineTxBiasHighAla=_Pm801rrAlmLineTxBiasHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,4),_Pm801rrAlmLineTxBiasHighAla_Type())
pm801rrAlmLineTxBiasHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxBiasHighAla.setStatus(_A)
_Pm801rrAlmLineTempLowAla_Type=EkiOnOff
_Pm801rrAlmLineTempLowAla_Object=MibScalar
pm801rrAlmLineTempLowAla=_Pm801rrAlmLineTempLowAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,7),_Pm801rrAlmLineTempLowAla_Type())
pm801rrAlmLineTempLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTempLowAla.setStatus(_A)
_Pm801rrAlmLineTempHighAla_Type=EkiOnOff
_Pm801rrAlmLineTempHighAla_Object=MibScalar
pm801rrAlmLineTempHighAla=_Pm801rrAlmLineTempHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,8),_Pm801rrAlmLineTempHighAla_Type())
pm801rrAlmLineTempHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTempHighAla.setStatus(_A)
_Pm801rrAlmLineRxPwrLowAla_Type=EkiOnOff
_Pm801rrAlmLineRxPwrLowAla_Object=MibScalar
pm801rrAlmLineRxPwrLowAla=_Pm801rrAlmLineRxPwrLowAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,15),_Pm801rrAlmLineRxPwrLowAla_Type())
pm801rrAlmLineRxPwrLowAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxPwrLowAla.setStatus(_A)
_Pm801rrAlmLineRxPwrHighAla_Type=EkiOnOff
_Pm801rrAlmLineRxPwrHighAla_Object=MibScalar
pm801rrAlmLineRxPwrHighAla=_Pm801rrAlmLineRxPwrHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,24,16),_Pm801rrAlmLineRxPwrHighAla_Type())
pm801rrAlmLineRxPwrHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxPwrHighAla.setStatus(_A)
_Pm801rrAlmrrLineOtxTlhAlarms3_ObjectIdentity=ObjectIdentity
pm801rrAlmrrLineOtxTlhAlarms3=_Pm801rrAlmrrLineOtxTlhAlarms3_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,2,30))
_Pm801rrAlmLineModulatorAgingHighAla_Type=EkiOnOff
_Pm801rrAlmLineModulatorAgingHighAla_Object=MibScalar
pm801rrAlmLineModulatorAgingHighAla=_Pm801rrAlmLineModulatorAgingHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,30,5),_Pm801rrAlmLineModulatorAgingHighAla_Type())
pm801rrAlmLineModulatorAgingHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineModulatorAgingHighAla.setStatus(_A)
_Pm801rrAlmLineAgingHighAla_Type=EkiOnOff
_Pm801rrAlmLineAgingHighAla_Object=MibScalar
pm801rrAlmLineAgingHighAla=_Pm801rrAlmLineAgingHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,30,6),_Pm801rrAlmLineAgingHighAla_Type())
pm801rrAlmLineAgingHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineAgingHighAla.setStatus(_A)
_Pm801rrAlmLineCdrNotReady_Type=EkiOnOff
_Pm801rrAlmLineCdrNotReady_Object=MibScalar
pm801rrAlmLineCdrNotReady=_Pm801rrAlmLineCdrNotReady_Object((1,3,6,1,4,1,20044,48,2,3,2,30,9),_Pm801rrAlmLineCdrNotReady_Type())
pm801rrAlmLineCdrNotReady.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineCdrNotReady.setStatus(_A)
_Pm801rrAlmLineFreqDevHighAla_Type=EkiOnOff
_Pm801rrAlmLineFreqDevHighAla_Object=MibScalar
pm801rrAlmLineFreqDevHighAla=_Pm801rrAlmLineFreqDevHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,30,12),_Pm801rrAlmLineFreqDevHighAla_Type())
pm801rrAlmLineFreqDevHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineFreqDevHighAla.setStatus(_A)
_Pm801rrAlmLineLaserTempHighAla_Type=EkiOnOff
_Pm801rrAlmLineLaserTempHighAla_Object=MibScalar
pm801rrAlmLineLaserTempHighAla=_Pm801rrAlmLineLaserTempHighAla_Object((1,3,6,1,4,1,20044,48,2,3,2,30,14),_Pm801rrAlmLineLaserTempHighAla_Type())
pm801rrAlmLineLaserTempHighAla.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineLaserTempHighAla.setStatus(_A)
_Pm801rrAlmLineCrit_ObjectIdentity=ObjectIdentity
pm801rrAlmLineCrit=_Pm801rrAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,3))
_Pm801rrAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pm801rrAlmsynthAlm7=_Pm801rrAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,3,7))
_Pm801rrAlmLineXfpAbsent_Type=EkiOnOff
_Pm801rrAlmLineXfpAbsent_Object=MibScalar
pm801rrAlmLineXfpAbsent=_Pm801rrAlmLineXfpAbsent_Object((1,3,6,1,4,1,20044,48,2,3,3,7,1),_Pm801rrAlmLineXfpAbsent_Type())
pm801rrAlmLineXfpAbsent.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineXfpAbsent.setStatus(_A)
_Pm801rrAlmLineInitNotCompl_Type=EkiOnOff
_Pm801rrAlmLineInitNotCompl_Object=MibScalar
pm801rrAlmLineInitNotCompl=_Pm801rrAlmLineInitNotCompl_Object((1,3,6,1,4,1,20044,48,2,3,3,7,2),_Pm801rrAlmLineInitNotCompl_Type())
pm801rrAlmLineInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineInitNotCompl.setStatus(_A)
_Pm801rrAlmLineHwFail_Type=EkiOnOff
_Pm801rrAlmLineHwFail_Object=MibScalar
pm801rrAlmLineHwFail=_Pm801rrAlmLineHwFail_Object((1,3,6,1,4,1,20044,48,2,3,3,7,4),_Pm801rrAlmLineHwFail_Type())
pm801rrAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineHwFail.setStatus(_A)
_Pm801rrAlmLineXfpTxOff_Type=EkiOnOff
_Pm801rrAlmLineXfpTxOff_Object=MibScalar
pm801rrAlmLineXfpTxOff=_Pm801rrAlmLineXfpTxOff_Object((1,3,6,1,4,1,20044,48,2,3,3,7,5),_Pm801rrAlmLineXfpTxOff_Type())
pm801rrAlmLineXfpTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineXfpTxOff.setStatus(_A)
_Pm801rrAlmLineDdmWarning_Type=EkiOnOff
_Pm801rrAlmLineDdmWarning_Object=MibScalar
pm801rrAlmLineDdmWarning=_Pm801rrAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,48,2,3,3,7,9),_Pm801rrAlmLineDdmWarning_Type())
pm801rrAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineDdmWarning.setStatus(_A)
_Pm801rrAlmLineDdmAlm_Type=EkiOnOff
_Pm801rrAlmLineDdmAlm_Object=MibScalar
pm801rrAlmLineDdmAlm=_Pm801rrAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,48,2,3,3,7,10),_Pm801rrAlmLineDdmAlm_Type())
pm801rrAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineDdmAlm.setStatus(_A)
_Pm801rrAlmLineFail_Type=EkiOnOff
_Pm801rrAlmLineFail_Object=MibScalar
pm801rrAlmLineFail=_Pm801rrAlmLineFail_Object((1,3,6,1,4,1,20044,48,2,3,3,7,12),_Pm801rrAlmLineFail_Type())
pm801rrAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineFail.setStatus(_A)
_Pm801rrAlmLineVccWarning_Type=EkiOnOff
_Pm801rrAlmLineVccWarning_Object=MibScalar
pm801rrAlmLineVccWarning=_Pm801rrAlmLineVccWarning_Object((1,3,6,1,4,1,20044,48,2,3,3,7,14),_Pm801rrAlmLineVccWarning_Type())
pm801rrAlmLineVccWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineVccWarning.setStatus(_A)
_Pm801rrAlmLineVccAlarm_Type=EkiOnOff
_Pm801rrAlmLineVccAlarm_Object=MibScalar
pm801rrAlmLineVccAlarm=_Pm801rrAlmLineVccAlarm_Object((1,3,6,1,4,1,20044,48,2,3,3,7,15),_Pm801rrAlmLineVccAlarm_Type())
pm801rrAlmLineVccAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineVccAlarm.setStatus(_A)
_Pm801rrAlmlineXfpAlarms2_ObjectIdentity=ObjectIdentity
pm801rrAlmlineXfpAlarms2=_Pm801rrAlmlineXfpAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,48,2,3,3,27))
_Pm801rrAlmLineResetComplete_Type=EkiOnOff
_Pm801rrAlmLineResetComplete_Object=MibScalar
pm801rrAlmLineResetComplete=_Pm801rrAlmLineResetComplete_Object((1,3,6,1,4,1,20044,48,2,3,3,27,1),_Pm801rrAlmLineResetComplete_Type())
pm801rrAlmLineResetComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineResetComplete.setStatus(_A)
_Pm801rrAlmLineRxCdrNotLocked_Type=EkiOnOff
_Pm801rrAlmLineRxCdrNotLocked_Object=MibScalar
pm801rrAlmLineRxCdrNotLocked=_Pm801rrAlmLineRxCdrNotLocked_Object((1,3,6,1,4,1,20044,48,2,3,3,27,3),_Pm801rrAlmLineRxCdrNotLocked_Type())
pm801rrAlmLineRxCdrNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxCdrNotLocked.setStatus(_A)
_Pm801rrAlmLineRxLos_Type=EkiOnOff
_Pm801rrAlmLineRxLos_Object=MibScalar
pm801rrAlmLineRxLos=_Pm801rrAlmLineRxLos_Object((1,3,6,1,4,1,20044,48,2,3,3,27,4),_Pm801rrAlmLineRxLos_Type())
pm801rrAlmLineRxLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxLos.setStatus(_A)
_Pm801rrAlmLineRxNr_Type=EkiOnOff
_Pm801rrAlmLineRxNr_Object=MibScalar
pm801rrAlmLineRxNr=_Pm801rrAlmLineRxNr_Object((1,3,6,1,4,1,20044,48,2,3,3,27,5),_Pm801rrAlmLineRxNr_Type())
pm801rrAlmLineRxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineRxNr.setStatus(_A)
_Pm801rrAlmLineTxCdrNotLocked_Type=EkiOnOff
_Pm801rrAlmLineTxCdrNotLocked_Object=MibScalar
pm801rrAlmLineTxCdrNotLocked=_Pm801rrAlmLineTxCdrNotLocked_Object((1,3,6,1,4,1,20044,48,2,3,3,27,6),_Pm801rrAlmLineTxCdrNotLocked_Type())
pm801rrAlmLineTxCdrNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxCdrNotLocked.setStatus(_A)
_Pm801rrAlmLineTxFault_Type=EkiOnOff
_Pm801rrAlmLineTxFault_Object=MibScalar
pm801rrAlmLineTxFault=_Pm801rrAlmLineTxFault_Object((1,3,6,1,4,1,20044,48,2,3,3,27,7),_Pm801rrAlmLineTxFault_Type())
pm801rrAlmLineTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxFault.setStatus(_A)
_Pm801rrAlmLineTxNr_Type=EkiOnOff
_Pm801rrAlmLineTxNr_Object=MibScalar
pm801rrAlmLineTxNr=_Pm801rrAlmLineTxNr_Object((1,3,6,1,4,1,20044,48,2,3,3,27,8),_Pm801rrAlmLineTxNr_Type())
pm801rrAlmLineTxNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTxNr.setStatus(_A)
_Pm801rrAlmLineChannelNotAcquired_Type=EkiOnOff
_Pm801rrAlmLineChannelNotAcquired_Object=MibScalar
pm801rrAlmLineChannelNotAcquired=_Pm801rrAlmLineChannelNotAcquired_Object((1,3,6,1,4,1,20044,48,2,3,3,27,10),_Pm801rrAlmLineChannelNotAcquired_Type())
pm801rrAlmLineChannelNotAcquired.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineChannelNotAcquired.setStatus(_A)
_Pm801rrAlmLineWavelengthUnlocked_Type=EkiOnOff
_Pm801rrAlmLineWavelengthUnlocked_Object=MibScalar
pm801rrAlmLineWavelengthUnlocked=_Pm801rrAlmLineWavelengthUnlocked_Object((1,3,6,1,4,1,20044,48,2,3,3,27,14),_Pm801rrAlmLineWavelengthUnlocked_Type())
pm801rrAlmLineWavelengthUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineWavelengthUnlocked.setStatus(_A)
_Pm801rrAlmLineTecFault_Type=EkiOnOff
_Pm801rrAlmLineTecFault_Object=MibScalar
pm801rrAlmLineTecFault=_Pm801rrAlmLineTecFault_Object((1,3,6,1,4,1,20044,48,2,3,3,27,15),_Pm801rrAlmLineTecFault_Type())
pm801rrAlmLineTecFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineTecFault.setStatus(_A)
_Pm801rrAlmLineApdSupplyFault_Type=EkiOnOff
_Pm801rrAlmLineApdSupplyFault_Object=MibScalar
pm801rrAlmLineApdSupplyFault=_Pm801rrAlmLineApdSupplyFault_Object((1,3,6,1,4,1,20044,48,2,3,3,27,16),_Pm801rrAlmLineApdSupplyFault_Type())
pm801rrAlmLineApdSupplyFault.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrAlmLineApdSupplyFault.setStatus(_A)
_Pm801rrmeasures_ObjectIdentity=ObjectIdentity
pm801rrmeasures=_Pm801rrmeasures_ObjectIdentity((1,3,6,1,4,1,20044,48,3))
_Pm801rrMesrOther_ObjectIdentity=ObjectIdentity
pm801rrMesrOther=_Pm801rrMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,48,3,1))
_Pm801rrMesrClient_ObjectIdentity=ObjectIdentity
pm801rrMesrClient=_Pm801rrMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,48,3,2))
class _Pm801rrMesrclientTemperature_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientTemperature_Type.__name__=_D
_Pm801rrMesrclientTemperature_Object=MibScalar
pm801rrMesrclientTemperature=_Pm801rrMesrclientTemperature_Object((1,3,6,1,4,1,20044,48,3,2,16),_Pm801rrMesrclientTemperature_Type())
pm801rrMesrclientTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientTemperature.setStatus(_A)
class _Pm801rrMesrclientTxBias_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientTxBias_Type.__name__=_D
_Pm801rrMesrclientTxBias_Object=MibScalar
pm801rrMesrclientTxBias=_Pm801rrMesrclientTxBias_Object((1,3,6,1,4,1,20044,48,3,2,18),_Pm801rrMesrclientTxBias_Type())
pm801rrMesrclientTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientTxBias.setStatus(_A)
class _Pm801rrMesrclientTxPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientTxPower_Type.__name__=_D
_Pm801rrMesrclientTxPower_Object=MibScalar
pm801rrMesrclientTxPower=_Pm801rrMesrclientTxPower_Object((1,3,6,1,4,1,20044,48,3,2,19),_Pm801rrMesrclientTxPower_Type())
pm801rrMesrclientTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientTxPower.setStatus(_A)
class _Pm801rrMesrclientRxPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientRxPower_Type.__name__=_D
_Pm801rrMesrclientRxPower_Object=MibScalar
pm801rrMesrclientRxPower=_Pm801rrMesrclientRxPower_Object((1,3,6,1,4,1,20044,48,3,2,20),_Pm801rrMesrclientRxPower_Type())
pm801rrMesrclientRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientRxPower.setStatus(_A)
class _Pm801rrMesrclientAging_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientAging_Type.__name__=_D
_Pm801rrMesrclientAging_Object=MibScalar
pm801rrMesrclientAging=_Pm801rrMesrclientAging_Object((1,3,6,1,4,1,20044,48,3,2,32),_Pm801rrMesrclientAging_Type())
pm801rrMesrclientAging.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientAging.setStatus(_A)
class _Pm801rrMesrclientLaserTemperature_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientLaserTemperature_Type.__name__=_D
_Pm801rrMesrclientLaserTemperature_Object=MibScalar
pm801rrMesrclientLaserTemperature=_Pm801rrMesrclientLaserTemperature_Object((1,3,6,1,4,1,20044,48,3,2,33),_Pm801rrMesrclientLaserTemperature_Type())
pm801rrMesrclientLaserTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientLaserTemperature.setStatus(_A)
class _Pm801rrMesrclientFreqDeviation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientFreqDeviation_Type.__name__=_D
_Pm801rrMesrclientFreqDeviation_Object=MibScalar
pm801rrMesrclientFreqDeviation=_Pm801rrMesrclientFreqDeviation_Object((1,3,6,1,4,1,20044,48,3,2,34),_Pm801rrMesrclientFreqDeviation_Type())
pm801rrMesrclientFreqDeviation.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientFreqDeviation.setStatus(_A)
class _Pm801rrMesrclientLaserWvlength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrclientLaserWvlength_Type.__name__=_D
_Pm801rrMesrclientLaserWvlength_Object=MibScalar
pm801rrMesrclientLaserWvlength=_Pm801rrMesrclientLaserWvlength_Object((1,3,6,1,4,1,20044,48,3,2,35),_Pm801rrMesrclientLaserWvlength_Type())
pm801rrMesrclientLaserWvlength.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrclientLaserWvlength.setStatus(_A)
_Pm801rrMesrLine_ObjectIdentity=ObjectIdentity
pm801rrMesrLine=_Pm801rrMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,48,3,3))
class _Pm801rrMesrlineTemperature_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineTemperature_Type.__name__=_D
_Pm801rrMesrlineTemperature_Object=MibScalar
pm801rrMesrlineTemperature=_Pm801rrMesrlineTemperature_Object((1,3,6,1,4,1,20044,48,3,3,24),_Pm801rrMesrlineTemperature_Type())
pm801rrMesrlineTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineTemperature.setStatus(_A)
class _Pm801rrMesrlineTxBias_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineTxBias_Type.__name__=_D
_Pm801rrMesrlineTxBias_Object=MibScalar
pm801rrMesrlineTxBias=_Pm801rrMesrlineTxBias_Object((1,3,6,1,4,1,20044,48,3,3,26),_Pm801rrMesrlineTxBias_Type())
pm801rrMesrlineTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineTxBias.setStatus(_A)
class _Pm801rrMesrlineTxPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineTxPower_Type.__name__=_D
_Pm801rrMesrlineTxPower_Object=MibScalar
pm801rrMesrlineTxPower=_Pm801rrMesrlineTxPower_Object((1,3,6,1,4,1,20044,48,3,3,27),_Pm801rrMesrlineTxPower_Type())
pm801rrMesrlineTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineTxPower.setStatus(_A)
class _Pm801rrMesrlineRxPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineRxPower_Type.__name__=_D
_Pm801rrMesrlineRxPower_Object=MibScalar
pm801rrMesrlineRxPower=_Pm801rrMesrlineRxPower_Object((1,3,6,1,4,1,20044,48,3,3,28),_Pm801rrMesrlineRxPower_Type())
pm801rrMesrlineRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineRxPower.setStatus(_A)
class _Pm801rrMesrlineAging_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineAging_Type.__name__=_D
_Pm801rrMesrlineAging_Object=MibScalar
pm801rrMesrlineAging=_Pm801rrMesrlineAging_Object((1,3,6,1,4,1,20044,48,3,3,40),_Pm801rrMesrlineAging_Type())
pm801rrMesrlineAging.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineAging.setStatus(_A)
class _Pm801rrMesrlineLaserTemperature_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineLaserTemperature_Type.__name__=_D
_Pm801rrMesrlineLaserTemperature_Object=MibScalar
pm801rrMesrlineLaserTemperature=_Pm801rrMesrlineLaserTemperature_Object((1,3,6,1,4,1,20044,48,3,3,41),_Pm801rrMesrlineLaserTemperature_Type())
pm801rrMesrlineLaserTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineLaserTemperature.setStatus(_A)
class _Pm801rrMesrlineFreqDeviation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineFreqDeviation_Type.__name__=_D
_Pm801rrMesrlineFreqDeviation_Object=MibScalar
pm801rrMesrlineFreqDeviation=_Pm801rrMesrlineFreqDeviation_Object((1,3,6,1,4,1,20044,48,3,3,42),_Pm801rrMesrlineFreqDeviation_Type())
pm801rrMesrlineFreqDeviation.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineFreqDeviation.setStatus(_A)
class _Pm801rrMesrlineLaserWvlength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrMesrlineLaserWvlength_Type.__name__=_D
_Pm801rrMesrlineLaserWvlength_Object=MibScalar
pm801rrMesrlineLaserWvlength=_Pm801rrMesrlineLaserWvlength_Object((1,3,6,1,4,1,20044,48,3,3,43),_Pm801rrMesrlineLaserWvlength_Type())
pm801rrMesrlineLaserWvlength.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrMesrlineLaserWvlength.setStatus(_A)
_Pm801rrcontrolsWrite_ObjectIdentity=ObjectIdentity
pm801rrcontrolsWrite=_Pm801rrcontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,48,6))
_Pm801rrCtrlOther_ObjectIdentity=ObjectIdentity
pm801rrCtrlOther=_Pm801rrCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,48,6,1))
_Pm801rrCtrlsynth0_ObjectIdentity=ObjectIdentity
pm801rrCtrlsynth0=_Pm801rrCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,48,6,1,0))
_Pm801rrCtrlConfLoad_Type=EkiOnOff
_Pm801rrCtrlConfLoad_Object=MibScalar
pm801rrCtrlConfLoad=_Pm801rrCtrlConfLoad_Object((1,3,6,1,4,1,20044,48,6,1,0,1),_Pm801rrCtrlConfLoad_Type())
pm801rrCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlConfLoad.setStatus(_A)
_Pm801rrCtrlConfFlash_Type=EkiOnOff
_Pm801rrCtrlConfFlash_Object=MibScalar
pm801rrCtrlConfFlash=_Pm801rrCtrlConfFlash_Object((1,3,6,1,4,1,20044,48,6,1,0,9),_Pm801rrCtrlConfFlash_Type())
pm801rrCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlConfFlash.setStatus(_A)
_Pm801rrCtrlConfClear_Type=EkiOnOff
_Pm801rrCtrlConfClear_Object=MibScalar
pm801rrCtrlConfClear=_Pm801rrCtrlConfClear_Object((1,3,6,1,4,1,20044,48,6,1,0,13),_Pm801rrCtrlConfClear_Type())
pm801rrCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlConfClear.setStatus(_A)
_Pm801rrCtrlsynth4_ObjectIdentity=ObjectIdentity
pm801rrCtrlsynth4=_Pm801rrCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,48,6,1,4))
_Pm801rrCtrlCorrelatOn_Type=EkiOnOff
_Pm801rrCtrlCorrelatOn_Object=MibScalar
pm801rrCtrlCorrelatOn=_Pm801rrCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,48,6,1,4,1),_Pm801rrCtrlCorrelatOn_Type())
pm801rrCtrlCorrelatOn.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlCorrelatOn.setStatus(_A)
_Pm801rrCtrlCorrelatOff_Type=EkiOnOff
_Pm801rrCtrlCorrelatOff_Object=MibScalar
pm801rrCtrlCorrelatOff=_Pm801rrCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,48,6,1,4,2),_Pm801rrCtrlCorrelatOff_Type())
pm801rrCtrlCorrelatOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlCorrelatOff.setStatus(_A)
_Pm801rrCtrlswMgnt_ObjectIdentity=ObjectIdentity
pm801rrCtrlswMgnt=_Pm801rrCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,48,6,1,5))
_Pm801rrCtrlColdReset_Type=EkiOnOff
_Pm801rrCtrlColdReset_Object=MibScalar
pm801rrCtrlColdReset=_Pm801rrCtrlColdReset_Object((1,3,6,1,4,1,20044,48,6,1,5,2),_Pm801rrCtrlColdReset_Type())
pm801rrCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlColdReset.setStatus(_A)
_Pm801rrCtrlWarmReset_Type=EkiOnOff
_Pm801rrCtrlWarmReset_Object=MibScalar
pm801rrCtrlWarmReset=_Pm801rrCtrlWarmReset_Object((1,3,6,1,4,1,20044,48,6,1,5,3),_Pm801rrCtrlWarmReset_Type())
pm801rrCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlWarmReset.setStatus(_A)
_Pm801rrCtrlledTest_ObjectIdentity=ObjectIdentity
pm801rrCtrlledTest=_Pm801rrCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,48,6,1,64))
_Pm801rrCtrlGreenLed_Type=EkiOnOff
_Pm801rrCtrlGreenLed_Object=MibScalar
pm801rrCtrlGreenLed=_Pm801rrCtrlGreenLed_Object((1,3,6,1,4,1,20044,48,6,1,64,1),_Pm801rrCtrlGreenLed_Type())
pm801rrCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlGreenLed.setStatus(_A)
_Pm801rrCtrlRedLed_Type=EkiOnOff
_Pm801rrCtrlRedLed_Object=MibScalar
pm801rrCtrlRedLed=_Pm801rrCtrlRedLed_Object((1,3,6,1,4,1,20044,48,6,1,64,2),_Pm801rrCtrlRedLed_Type())
pm801rrCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlRedLed.setStatus(_A)
_Pm801rrCtrlLedOff_Type=EkiOnOff
_Pm801rrCtrlLedOff_Object=MibScalar
pm801rrCtrlLedOff=_Pm801rrCtrlLedOff_Object((1,3,6,1,4,1,20044,48,6,1,64,3),_Pm801rrCtrlLedOff_Type())
pm801rrCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlLedOff.setStatus(_A)
_Pm801rrCtrlClient_ObjectIdentity=ObjectIdentity
pm801rrCtrlClient=_Pm801rrCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,48,6,2))
_Pm801rrCtrlclientXfpOnoff_ObjectIdentity=ObjectIdentity
pm801rrCtrlclientXfpOnoff=_Pm801rrCtrlclientXfpOnoff_ObjectIdentity((1,3,6,1,4,1,20044,48,6,2,16))
_Pm801rrCtrlClientXfpOnoff_Type=EkiOnOff
_Pm801rrCtrlClientXfpOnoff_Object=MibScalar
pm801rrCtrlClientXfpOnoff=_Pm801rrCtrlClientXfpOnoff_Object((1,3,6,1,4,1,20044,48,6,2,16,1),_Pm801rrCtrlClientXfpOnoff_Type())
pm801rrCtrlClientXfpOnoff.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlClientXfpOnoff.setStatus(_A)
_Pm801rrCtrlclientXfpLineLoop_ObjectIdentity=ObjectIdentity
pm801rrCtrlclientXfpLineLoop=_Pm801rrCtrlclientXfpLineLoop_ObjectIdentity((1,3,6,1,4,1,20044,48,6,2,17))
_Pm801rrCtrlClientXfpLineLoop_Type=EkiOnOff
_Pm801rrCtrlClientXfpLineLoop_Object=MibScalar
pm801rrCtrlClientXfpLineLoop=_Pm801rrCtrlClientXfpLineLoop_Object((1,3,6,1,4,1,20044,48,6,2,17,1),_Pm801rrCtrlClientXfpLineLoop_Type())
pm801rrCtrlClientXfpLineLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlClientXfpLineLoop.setStatus(_A)
_Pm801rrCtrlclientXfiLoop_ObjectIdentity=ObjectIdentity
pm801rrCtrlclientXfiLoop=_Pm801rrCtrlclientXfiLoop_ObjectIdentity((1,3,6,1,4,1,20044,48,6,2,18))
_Pm801rrCtrlClientXfiLoop_Type=EkiOnOff
_Pm801rrCtrlClientXfiLoop_Object=MibScalar
pm801rrCtrlClientXfiLoop=_Pm801rrCtrlClientXfiLoop_Object((1,3,6,1,4,1,20044,48,6,2,18,1),_Pm801rrCtrlClientXfiLoop_Type())
pm801rrCtrlClientXfiLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlClientXfiLoop.setStatus(_A)
_Pm801rrCtrlclientTunableChannel_Type=Pm801rrOtxChannel
_Pm801rrCtrlclientTunableChannel_Object=MibScalar
pm801rrCtrlclientTunableChannel=_Pm801rrCtrlclientTunableChannel_Object((1,3,6,1,4,1,20044,48,6,2,19),_Pm801rrCtrlclientTunableChannel_Type())
pm801rrCtrlclientTunableChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlclientTunableChannel.setStatus(_A)
_Pm801rrCtrlclientPhotodiodeMode_Type=Pm801rrOtxMode
_Pm801rrCtrlclientPhotodiodeMode_Object=MibScalar
pm801rrCtrlclientPhotodiodeMode=_Pm801rrCtrlclientPhotodiodeMode_Object((1,3,6,1,4,1,20044,48,6,2,20),_Pm801rrCtrlclientPhotodiodeMode_Type())
pm801rrCtrlclientPhotodiodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlclientPhotodiodeMode.setStatus(_A)
_Pm801rrCtrlclientPhotodiodeValue_Type=Pm801rrAdjustValue
_Pm801rrCtrlclientPhotodiodeValue_Object=MibScalar
pm801rrCtrlclientPhotodiodeValue=_Pm801rrCtrlclientPhotodiodeValue_Object((1,3,6,1,4,1,20044,48,6,2,21),_Pm801rrCtrlclientPhotodiodeValue_Type())
pm801rrCtrlclientPhotodiodeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlclientPhotodiodeValue.setStatus(_A)
class _Pm801rrCtrlclientPowerLaser_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrCtrlclientPowerLaser_Type.__name__=_D
_Pm801rrCtrlclientPowerLaser_Object=MibScalar
pm801rrCtrlclientPowerLaser=_Pm801rrCtrlclientPowerLaser_Object((1,3,6,1,4,1,20044,48,6,2,22),_Pm801rrCtrlclientPowerLaser_Type())
pm801rrCtrlclientPowerLaser.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlclientPowerLaser.setStatus(_A)
_Pm801rrCtrlLine_ObjectIdentity=ObjectIdentity
pm801rrCtrlLine=_Pm801rrCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,48,6,3))
_Pm801rrCtrlclientOtxVlhReset_ObjectIdentity=ObjectIdentity
pm801rrCtrlclientOtxVlhReset=_Pm801rrCtrlclientOtxVlhReset_ObjectIdentity((1,3,6,1,4,1,20044,48,6,3,23))
_Pm801rrCtrlClientOtxVlhReset_Type=EkiOnOff
_Pm801rrCtrlClientOtxVlhReset_Object=MibScalar
pm801rrCtrlClientOtxVlhReset=_Pm801rrCtrlClientOtxVlhReset_Object((1,3,6,1,4,1,20044,48,6,3,23,1),_Pm801rrCtrlClientOtxVlhReset_Type())
pm801rrCtrlClientOtxVlhReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlClientOtxVlhReset.setStatus(_A)
_Pm801rrCtrllineXfpOnoff_ObjectIdentity=ObjectIdentity
pm801rrCtrllineXfpOnoff=_Pm801rrCtrllineXfpOnoff_ObjectIdentity((1,3,6,1,4,1,20044,48,6,3,24))
_Pm801rrCtrlLineXfpOnoff_Type=EkiOnOff
_Pm801rrCtrlLineXfpOnoff_Object=MibScalar
pm801rrCtrlLineXfpOnoff=_Pm801rrCtrlLineXfpOnoff_Object((1,3,6,1,4,1,20044,48,6,3,24,1),_Pm801rrCtrlLineXfpOnoff_Type())
pm801rrCtrlLineXfpOnoff.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlLineXfpOnoff.setStatus(_A)
_Pm801rrCtrllineXfpLineLoop_ObjectIdentity=ObjectIdentity
pm801rrCtrllineXfpLineLoop=_Pm801rrCtrllineXfpLineLoop_ObjectIdentity((1,3,6,1,4,1,20044,48,6,3,25))
_Pm801rrCtrlLineXfpLineLoop_Type=EkiOnOff
_Pm801rrCtrlLineXfpLineLoop_Object=MibScalar
pm801rrCtrlLineXfpLineLoop=_Pm801rrCtrlLineXfpLineLoop_Object((1,3,6,1,4,1,20044,48,6,3,25,1),_Pm801rrCtrlLineXfpLineLoop_Type())
pm801rrCtrlLineXfpLineLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlLineXfpLineLoop.setStatus(_A)
_Pm801rrCtrllineXfiLoop_ObjectIdentity=ObjectIdentity
pm801rrCtrllineXfiLoop=_Pm801rrCtrllineXfiLoop_ObjectIdentity((1,3,6,1,4,1,20044,48,6,3,26))
_Pm801rrCtrlLineXfiLoop_Type=EkiOnOff
_Pm801rrCtrlLineXfiLoop_Object=MibScalar
pm801rrCtrlLineXfiLoop=_Pm801rrCtrlLineXfiLoop_Object((1,3,6,1,4,1,20044,48,6,3,26,1),_Pm801rrCtrlLineXfiLoop_Type())
pm801rrCtrlLineXfiLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlLineXfiLoop.setStatus(_A)
_Pm801rrCtrllineTunableChannel_Type=Pm801rrOtxChannel
_Pm801rrCtrllineTunableChannel_Object=MibScalar
pm801rrCtrllineTunableChannel=_Pm801rrCtrllineTunableChannel_Object((1,3,6,1,4,1,20044,48,6,3,27),_Pm801rrCtrllineTunableChannel_Type())
pm801rrCtrllineTunableChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrllineTunableChannel.setStatus(_A)
_Pm801rrCtrllinePhotodiodeMode_Type=Pm801rrOtxMode
_Pm801rrCtrllinePhotodiodeMode_Object=MibScalar
pm801rrCtrllinePhotodiodeMode=_Pm801rrCtrllinePhotodiodeMode_Object((1,3,6,1,4,1,20044,48,6,3,28),_Pm801rrCtrllinePhotodiodeMode_Type())
pm801rrCtrllinePhotodiodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrllinePhotodiodeMode.setStatus(_A)
_Pm801rrCtrllinePhotodiodeValue_Type=Pm801rrAdjustValue
_Pm801rrCtrllinePhotodiodeValue_Object=MibScalar
pm801rrCtrllinePhotodiodeValue=_Pm801rrCtrllinePhotodiodeValue_Object((1,3,6,1,4,1,20044,48,6,3,29),_Pm801rrCtrllinePhotodiodeValue_Type())
pm801rrCtrllinePhotodiodeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrllinePhotodiodeValue.setStatus(_A)
class _Pm801rrCtrllinePowerLaser_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pm801rrCtrllinePowerLaser_Type.__name__=_D
_Pm801rrCtrllinePowerLaser_Object=MibScalar
pm801rrCtrllinePowerLaser=_Pm801rrCtrllinePowerLaser_Object((1,3,6,1,4,1,20044,48,6,3,30),_Pm801rrCtrllinePowerLaser_Type())
pm801rrCtrllinePowerLaser.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrllinePowerLaser.setStatus(_A)
_Pm801rrCtrllineOtxVlhReset_ObjectIdentity=ObjectIdentity
pm801rrCtrllineOtxVlhReset=_Pm801rrCtrllineOtxVlhReset_ObjectIdentity((1,3,6,1,4,1,20044,48,6,3,31))
_Pm801rrCtrlLineOtxVlhReset_Type=EkiOnOff
_Pm801rrCtrlLineOtxVlhReset_Object=MibScalar
pm801rrCtrlLineOtxVlhReset=_Pm801rrCtrlLineOtxVlhReset_Object((1,3,6,1,4,1,20044,48,6,3,31,1),_Pm801rrCtrlLineOtxVlhReset_Type())
pm801rrCtrlLineOtxVlhReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCtrlLineOtxVlhReset.setStatus(_A)
_Pm801rrri_ObjectIdentity=ObjectIdentity
pm801rrri=_Pm801rrri_ObjectIdentity((1,3,6,1,4,1,20044,48,7))
_Pm801rrRinvReloadInventory_Type=EkiOnOff
_Pm801rrRinvReloadInventory_Object=MibScalar
pm801rrRinvReloadInventory=_Pm801rrRinvReloadInventory_Object((1,3,6,1,4,1,20044,48,7,2),_Pm801rrRinvReloadInventory_Type())
pm801rrRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrRinvReloadInventory.setStatus(_A)
_Pm801rrRinvHwPlatform_Type=DisplayString
_Pm801rrRinvHwPlatform_Object=MibScalar
pm801rrRinvHwPlatform=_Pm801rrRinvHwPlatform_Object((1,3,6,1,4,1,20044,48,7,4),_Pm801rrRinvHwPlatform_Type())
pm801rrRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrRinvHwPlatform.setStatus(_A)
_Pm801rrRinvSwPlatform_Type=DisplayString
_Pm801rrRinvSwPlatform_Object=MibScalar
pm801rrRinvSwPlatform=_Pm801rrRinvSwPlatform_Object((1,3,6,1,4,1,20044,48,7,5),_Pm801rrRinvSwPlatform_Type())
pm801rrRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrRinvSwPlatform.setStatus(_A)
_Pm801rrRinvClientXFP_Type=DisplayString
_Pm801rrRinvClientXFP_Object=MibScalar
pm801rrRinvClientXFP=_Pm801rrRinvClientXFP_Object((1,3,6,1,4,1,20044,48,7,6),_Pm801rrRinvClientXFP_Type())
pm801rrRinvClientXFP.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrRinvClientXFP.setStatus(_A)
_Pm801rrRinvLineXFP_Type=DisplayString
_Pm801rrRinvLineXFP_Object=MibScalar
pm801rrRinvLineXFP=_Pm801rrRinvLineXFP_Object((1,3,6,1,4,1,20044,48,7,7),_Pm801rrRinvLineXFP_Type())
pm801rrRinvLineXFP.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrRinvLineXFP.setStatus(_A)
_Pm801rrConfig_ObjectIdentity=ObjectIdentity
pm801rrConfig=_Pm801rrConfig_ObjectIdentity((1,3,6,1,4,1,20044,48,9))
_Pm801rrCfgLsd_ObjectIdentity=ObjectIdentity
pm801rrCfgLsd=_Pm801rrCfgLsd_ObjectIdentity((1,3,6,1,4,1,20044,48,9,1))
_Pm801rrtableclientLsd_ObjectIdentity=ObjectIdentity
pm801rrtableclientLsd=_Pm801rrtableclientLsd_ObjectIdentity((1,3,6,1,4,1,20044,48,9,1,1))
class _Pm801rrCfglsdMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglsdMode_Type.__name__=_D
_Pm801rrCfglsdMode_Object=MibScalar
pm801rrCfglsdMode=_Pm801rrCfglsdMode_Object((1,3,6,1,4,1,20044,48,9,1,1,2),_Pm801rrCfglsdMode_Type())
pm801rrCfglsdMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglsdMode.setStatus(_A)
class _Pm801rrCfgclientXfpAlarms_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientXfpAlarms_Type.__name__=_D
_Pm801rrCfgclientXfpAlarms_Object=MibScalar
pm801rrCfgclientXfpAlarms=_Pm801rrCfgclientXfpAlarms_Object((1,3,6,1,4,1,20044,48,9,1,1,3),_Pm801rrCfgclientXfpAlarms_Type())
pm801rrCfgclientXfpAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientXfpAlarms.setStatus(_A)
class _Pm801rrCfgclientXfpAbsence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientXfpAbsence_Type.__name__=_D
_Pm801rrCfgclientXfpAbsence_Object=MibScalar
pm801rrCfgclientXfpAbsence=_Pm801rrCfgclientXfpAbsence_Object((1,3,6,1,4,1,20044,48,9,1,1,4),_Pm801rrCfgclientXfpAbsence_Type())
pm801rrCfgclientXfpAbsence.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientXfpAbsence.setStatus(_A)
class _Pm801rrCfglineXfpAlarms_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineXfpAlarms_Type.__name__=_D
_Pm801rrCfglineXfpAlarms_Object=MibScalar
pm801rrCfglineXfpAlarms=_Pm801rrCfglineXfpAlarms_Object((1,3,6,1,4,1,20044,48,9,1,1,5),_Pm801rrCfglineXfpAlarms_Type())
pm801rrCfglineXfpAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineXfpAlarms.setStatus(_A)
class _Pm801rrCfglineXfpAbsence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineXfpAbsence_Type.__name__=_D
_Pm801rrCfglineXfpAbsence_Object=MibScalar
pm801rrCfglineXfpAbsence=_Pm801rrCfglineXfpAbsence_Object((1,3,6,1,4,1,20044,48,9,1,1,6),_Pm801rrCfglineXfpAbsence_Type())
pm801rrCfglineXfpAbsence.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineXfpAbsence.setStatus(_A)
_Pm801rrCfgStartUp_ObjectIdentity=ObjectIdentity
pm801rrCfgStartUp=_Pm801rrCfgStartUp_ObjectIdentity((1,3,6,1,4,1,20044,48,9,2))
_Pm801rrtableclientStartup_ObjectIdentity=ObjectIdentity
pm801rrtableclientStartup=_Pm801rrtableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,48,9,2,1))
class _Pm801rrCfgclientXfpCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientXfpCtrl_Type.__name__=_D
_Pm801rrCfgclientXfpCtrl_Object=MibScalar
pm801rrCfgclientXfpCtrl=_Pm801rrCfgclientXfpCtrl_Object((1,3,6,1,4,1,20044,48,9,2,1,2),_Pm801rrCfgclientXfpCtrl_Type())
pm801rrCfgclientXfpCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientXfpCtrl.setStatus(_A)
_Pm801rrtablelineStartup_ObjectIdentity=ObjectIdentity
pm801rrtablelineStartup=_Pm801rrtablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,48,9,2,2))
class _Pm801rrCfglineXfpCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineXfpCtrl_Type.__name__=_D
_Pm801rrCfglineXfpCtrl_Object=MibScalar
pm801rrCfglineXfpCtrl=_Pm801rrCfglineXfpCtrl_Object((1,3,6,1,4,1,20044,48,9,2,2,2),_Pm801rrCfglineXfpCtrl_Type())
pm801rrCfglineXfpCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineXfpCtrl.setStatus(_A)
class _Pm801rrCfgprotocolSelect_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgprotocolSelect_Type.__name__=_D
_Pm801rrCfgprotocolSelect_Object=MibScalar
pm801rrCfgprotocolSelect=_Pm801rrCfgprotocolSelect_Object((1,3,6,1,4,1,20044,48,9,2,2,18),_Pm801rrCfgprotocolSelect_Type())
pm801rrCfgprotocolSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgprotocolSelect.setStatus(_A)
_Pm801rrtableclientOtxtlh_ObjectIdentity=ObjectIdentity
pm801rrtableclientOtxtlh=_Pm801rrtableclientOtxtlh_ObjectIdentity((1,3,6,1,4,1,20044,48,9,2,3))
class _Pm801rrCfgclientDitherControl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientDitherControl_Type.__name__=_D
_Pm801rrCfgclientDitherControl_Object=MibScalar
pm801rrCfgclientDitherControl=_Pm801rrCfgclientDitherControl_Object((1,3,6,1,4,1,20044,48,9,2,3,2),_Pm801rrCfgclientDitherControl_Type())
pm801rrCfgclientDitherControl.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientDitherControl.setStatus(_A)
class _Pm801rrCfgclientDitherRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientDitherRate_Type.__name__=_D
_Pm801rrCfgclientDitherRate_Object=MibScalar
pm801rrCfgclientDitherRate=_Pm801rrCfgclientDitherRate_Object((1,3,6,1,4,1,20044,48,9,2,3,3),_Pm801rrCfgclientDitherRate_Type())
pm801rrCfgclientDitherRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientDitherRate.setStatus(_A)
class _Pm801rrCfgclientDitherFhz_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientDitherFhz_Type.__name__=_D
_Pm801rrCfgclientDitherFhz_Object=MibScalar
pm801rrCfgclientDitherFhz=_Pm801rrCfgclientDitherFhz_Object((1,3,6,1,4,1,20044,48,9,2,3,4),_Pm801rrCfgclientDitherFhz_Type())
pm801rrCfgclientDitherFhz.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientDitherFhz.setStatus(_A)
class _Pm801rrCfgclientPwrLaser_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientPwrLaser_Type.__name__=_D
_Pm801rrCfgclientPwrLaser_Object=MibScalar
pm801rrCfgclientPwrLaser=_Pm801rrCfgclientPwrLaser_Object((1,3,6,1,4,1,20044,48,9,2,3,5),_Pm801rrCfgclientPwrLaser_Type())
pm801rrCfgclientPwrLaser.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientPwrLaser.setStatus(_A)
class _Pm801rrCfgclientFCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientFCurrent_Type.__name__=_D
_Pm801rrCfgclientFCurrent_Object=MibScalar
pm801rrCfgclientFCurrent=_Pm801rrCfgclientFCurrent_Object((1,3,6,1,4,1,20044,48,9,2,3,6),_Pm801rrCfgclientFCurrent_Type())
pm801rrCfgclientFCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientFCurrent.setStatus(_A)
class _Pm801rrCfgclientGridCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientGridCurrent_Type.__name__=_D
_Pm801rrCfgclientGridCurrent_Object=MibScalar
pm801rrCfgclientGridCurrent=_Pm801rrCfgclientGridCurrent_Object((1,3,6,1,4,1,20044,48,9,2,3,7),_Pm801rrCfgclientGridCurrent_Type())
pm801rrCfgclientGridCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientGridCurrent.setStatus(_A)
class _Pm801rrCfgclientF0_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientF0_Type.__name__=_D
_Pm801rrCfgclientF0_Object=MibScalar
pm801rrCfgclientF0=_Pm801rrCfgclientF0_Object((1,3,6,1,4,1,20044,48,9,2,3,8),_Pm801rrCfgclientF0_Type())
pm801rrCfgclientF0.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientF0.setStatus(_A)
class _Pm801rrCfgclientPhotodiodeMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientPhotodiodeMode_Type.__name__=_D
_Pm801rrCfgclientPhotodiodeMode_Object=MibScalar
pm801rrCfgclientPhotodiodeMode=_Pm801rrCfgclientPhotodiodeMode_Object((1,3,6,1,4,1,20044,48,9,2,3,10),_Pm801rrCfgclientPhotodiodeMode_Type())
pm801rrCfgclientPhotodiodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientPhotodiodeMode.setStatus(_A)
class _Pm801rrCfgclientPhotodiodeValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgclientPhotodiodeValue_Type.__name__=_D
_Pm801rrCfgclientPhotodiodeValue_Object=MibScalar
pm801rrCfgclientPhotodiodeValue=_Pm801rrCfgclientPhotodiodeValue_Object((1,3,6,1,4,1,20044,48,9,2,3,11),_Pm801rrCfgclientPhotodiodeValue_Type())
pm801rrCfgclientPhotodiodeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgclientPhotodiodeValue.setStatus(_A)
_Pm801rrtablelineOtxtlh_ObjectIdentity=ObjectIdentity
pm801rrtablelineOtxtlh=_Pm801rrtablelineOtxtlh_ObjectIdentity((1,3,6,1,4,1,20044,48,9,2,4))
class _Pm801rrCfglineDitherControl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineDitherControl_Type.__name__=_D
_Pm801rrCfglineDitherControl_Object=MibScalar
pm801rrCfglineDitherControl=_Pm801rrCfglineDitherControl_Object((1,3,6,1,4,1,20044,48,9,2,4,2),_Pm801rrCfglineDitherControl_Type())
pm801rrCfglineDitherControl.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineDitherControl.setStatus(_A)
class _Pm801rrCfglineDitherRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineDitherRate_Type.__name__=_D
_Pm801rrCfglineDitherRate_Object=MibScalar
pm801rrCfglineDitherRate=_Pm801rrCfglineDitherRate_Object((1,3,6,1,4,1,20044,48,9,2,4,3),_Pm801rrCfglineDitherRate_Type())
pm801rrCfglineDitherRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineDitherRate.setStatus(_A)
class _Pm801rrCfglineDitherFhz_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineDitherFhz_Type.__name__=_D
_Pm801rrCfglineDitherFhz_Object=MibScalar
pm801rrCfglineDitherFhz=_Pm801rrCfglineDitherFhz_Object((1,3,6,1,4,1,20044,48,9,2,4,4),_Pm801rrCfglineDitherFhz_Type())
pm801rrCfglineDitherFhz.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineDitherFhz.setStatus(_A)
class _Pm801rrCfglinePwrLaser_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglinePwrLaser_Type.__name__=_D
_Pm801rrCfglinePwrLaser_Object=MibScalar
pm801rrCfglinePwrLaser=_Pm801rrCfglinePwrLaser_Object((1,3,6,1,4,1,20044,48,9,2,4,5),_Pm801rrCfglinePwrLaser_Type())
pm801rrCfglinePwrLaser.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglinePwrLaser.setStatus(_A)
class _Pm801rrCfglineFCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineFCurrent_Type.__name__=_D
_Pm801rrCfglineFCurrent_Object=MibScalar
pm801rrCfglineFCurrent=_Pm801rrCfglineFCurrent_Object((1,3,6,1,4,1,20044,48,9,2,4,6),_Pm801rrCfglineFCurrent_Type())
pm801rrCfglineFCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineFCurrent.setStatus(_A)
class _Pm801rrCfglineGridCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineGridCurrent_Type.__name__=_D
_Pm801rrCfglineGridCurrent_Object=MibScalar
pm801rrCfglineGridCurrent=_Pm801rrCfglineGridCurrent_Object((1,3,6,1,4,1,20044,48,9,2,4,7),_Pm801rrCfglineGridCurrent_Type())
pm801rrCfglineGridCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineGridCurrent.setStatus(_A)
class _Pm801rrCfglineF0_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglineF0_Type.__name__=_D
_Pm801rrCfglineF0_Object=MibScalar
pm801rrCfglineF0=_Pm801rrCfglineF0_Object((1,3,6,1,4,1,20044,48,9,2,4,8),_Pm801rrCfglineF0_Type())
pm801rrCfglineF0.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglineF0.setStatus(_A)
class _Pm801rrCfglinePhotodiodeMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglinePhotodiodeMode_Type.__name__=_D
_Pm801rrCfglinePhotodiodeMode_Object=MibScalar
pm801rrCfglinePhotodiodeMode=_Pm801rrCfglinePhotodiodeMode_Object((1,3,6,1,4,1,20044,48,9,2,4,10),_Pm801rrCfglinePhotodiodeMode_Type())
pm801rrCfglinePhotodiodeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglinePhotodiodeMode.setStatus(_A)
class _Pm801rrCfglinePhotodiodeValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfglinePhotodiodeValue_Type.__name__=_D
_Pm801rrCfglinePhotodiodeValue_Object=MibScalar
pm801rrCfglinePhotodiodeValue=_Pm801rrCfglinePhotodiodeValue_Object((1,3,6,1,4,1,20044,48,9,2,4,11),_Pm801rrCfglinePhotodiodeValue_Type())
pm801rrCfglinePhotodiodeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfglinePhotodiodeValue.setStatus(_A)
_Pm801rrCfgLabels_ObjectIdentity=ObjectIdentity
pm801rrCfgLabels=_Pm801rrCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,48,9,3))
_Pm801rrCfgLabelclientTable_Object=MibTable
pm801rrCfgLabelclientTable=_Pm801rrCfgLabelclientTable_Object((1,3,6,1,4,1,20044,48,9,3,1))
if mibBuilder.loadTexts:pm801rrCfgLabelclientTable.setStatus(_A)
_Pm801rrCfgLabelclientEntry_Object=MibTableRow
pm801rrCfgLabelclientEntry=_Pm801rrCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,48,9,3,1,1))
pm801rrCfgLabelclientEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:pm801rrCfgLabelclientEntry.setStatus(_A)
class _Pm801rrCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm801rrCfgLabelclientIndex_Type.__name__=_G
_Pm801rrCfgLabelclientIndex_Object=MibTableColumn
pm801rrCfgLabelclientIndex=_Pm801rrCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,48,9,3,1,1,1),_Pm801rrCfgLabelclientIndex_Type())
pm801rrCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgLabelclientIndex.setStatus(_A)
class _Pm801rrCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm801rrCfgLabelclientPortn_Type.__name__=_H
_Pm801rrCfgLabelclientPortn_Object=MibTableColumn
pm801rrCfgLabelclientPortn=_Pm801rrCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,48,9,3,1,1,3),_Pm801rrCfgLabelclientPortn_Type())
pm801rrCfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgLabelclientPortn.setStatus(_A)
_Pm801rrCfgLabellineTable_Object=MibTable
pm801rrCfgLabellineTable=_Pm801rrCfgLabellineTable_Object((1,3,6,1,4,1,20044,48,9,3,2))
if mibBuilder.loadTexts:pm801rrCfgLabellineTable.setStatus(_A)
_Pm801rrCfgLabellineEntry_Object=MibTableRow
pm801rrCfgLabellineEntry=_Pm801rrCfgLabellineEntry_Object((1,3,6,1,4,1,20044,48,9,3,2,1))
pm801rrCfgLabellineEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:pm801rrCfgLabellineEntry.setStatus(_A)
class _Pm801rrCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm801rrCfgLabellineIndex_Type.__name__=_G
_Pm801rrCfgLabellineIndex_Object=MibTableColumn
pm801rrCfgLabellineIndex=_Pm801rrCfgLabellineIndex_Object((1,3,6,1,4,1,20044,48,9,3,2,1,1),_Pm801rrCfgLabellineIndex_Type())
pm801rrCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgLabellineIndex.setStatus(_A)
class _Pm801rrCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pm801rrCfgLabellinePortn_Type.__name__=_H
_Pm801rrCfgLabellinePortn_Object=MibTableColumn
pm801rrCfgLabellinePortn=_Pm801rrCfgLabellinePortn_Object((1,3,6,1,4,1,20044,48,9,3,2,1,3),_Pm801rrCfgLabellinePortn_Type())
pm801rrCfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgLabellinePortn.setStatus(_A)
_Pm801rrCfgStartuptablefive_ObjectIdentity=ObjectIdentity
pm801rrCfgStartuptablefive=_Pm801rrCfgStartuptablefive_ObjectIdentity((1,3,6,1,4,1,20044,48,9,4))
_Pm801rrCfgOtxtlhcapabilitiesTable_Object=MibTable
pm801rrCfgOtxtlhcapabilitiesTable=_Pm801rrCfgOtxtlhcapabilitiesTable_Object((1,3,6,1,4,1,20044,48,9,4,1))
if mibBuilder.loadTexts:pm801rrCfgOtxtlhcapabilitiesTable.setStatus(_A)
_Pm801rrCfgOtxtlhcapabilitiesEntry_Object=MibTableRow
pm801rrCfgOtxtlhcapabilitiesEntry=_Pm801rrCfgOtxtlhcapabilitiesEntry_Object((1,3,6,1,4,1,20044,48,9,4,1,1))
pm801rrCfgOtxtlhcapabilitiesEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:pm801rrCfgOtxtlhcapabilitiesEntry.setStatus(_A)
class _Pm801rrCfgOtxtlhcapabilitiesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pm801rrCfgOtxtlhcapabilitiesIndex_Type.__name__=_G
_Pm801rrCfgOtxtlhcapabilitiesIndex_Object=MibTableColumn
pm801rrCfgOtxtlhcapabilitiesIndex=_Pm801rrCfgOtxtlhcapabilitiesIndex_Object((1,3,6,1,4,1,20044,48,9,4,1,1,1),_Pm801rrCfgOtxtlhcapabilitiesIndex_Type())
pm801rrCfgOtxtlhcapabilitiesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgOtxtlhcapabilitiesIndex.setStatus(_A)
class _Pm801rrCfgComponentTypePortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgComponentTypePortn_Type.__name__=_D
_Pm801rrCfgComponentTypePortn_Object=MibTableColumn
pm801rrCfgComponentTypePortn=_Pm801rrCfgComponentTypePortn_Object((1,3,6,1,4,1,20044,48,9,4,1,1,3),_Pm801rrCfgComponentTypePortn_Type())
pm801rrCfgComponentTypePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgComponentTypePortn.setStatus(_A)
class _Pm801rrCfgMiscellaneousPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgMiscellaneousPortn_Type.__name__=_D
_Pm801rrCfgMiscellaneousPortn_Object=MibTableColumn
pm801rrCfgMiscellaneousPortn=_Pm801rrCfgMiscellaneousPortn_Object((1,3,6,1,4,1,20044,48,9,4,1,1,4),_Pm801rrCfgMiscellaneousPortn_Type())
pm801rrCfgMiscellaneousPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgMiscellaneousPortn.setStatus(_A)
class _Pm801rrCfgFirstChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgFirstChannelPortn_Type.__name__=_D
_Pm801rrCfgFirstChannelPortn_Object=MibTableColumn
pm801rrCfgFirstChannelPortn=_Pm801rrCfgFirstChannelPortn_Object((1,3,6,1,4,1,20044,48,9,4,1,1,5),_Pm801rrCfgFirstChannelPortn_Type())
pm801rrCfgFirstChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgFirstChannelPortn.setStatus(_A)
class _Pm801rrCfgLastChannelPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgLastChannelPortn_Type.__name__=_D
_Pm801rrCfgLastChannelPortn_Object=MibTableColumn
pm801rrCfgLastChannelPortn=_Pm801rrCfgLastChannelPortn_Object((1,3,6,1,4,1,20044,48,9,4,1,1,6),_Pm801rrCfgLastChannelPortn_Type())
pm801rrCfgLastChannelPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgLastChannelPortn.setStatus(_A)
class _Pm801rrCfgGridPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pm801rrCfgGridPortn_Type.__name__=_D
_Pm801rrCfgGridPortn_Object=MibTableColumn
pm801rrCfgGridPortn=_Pm801rrCfgGridPortn_Object((1,3,6,1,4,1,20044,48,9,4,1,1,7),_Pm801rrCfgGridPortn_Type())
pm801rrCfgGridPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrCfgGridPortn.setStatus(_A)
_Pm801rrCfgWriteConfiguration_Type=EkiOnOff
_Pm801rrCfgWriteConfiguration_Object=MibScalar
pm801rrCfgWriteConfiguration=_Pm801rrCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,48,9,257),_Pm801rrCfgWriteConfiguration_Type())
pm801rrCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pm801rrCfgWriteConfiguration.setStatus(_A)
_Pm801rrtraps_ObjectIdentity=ObjectIdentity
pm801rrtraps=_Pm801rrtraps_ObjectIdentity((1,3,6,1,4,1,20044,48,10))
class _Pm801rrtrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pm801rrtrapBoardNumber_Type.__name__=_G
_Pm801rrtrapBoardNumber_Object=MibScalar
pm801rrtrapBoardNumber=_Pm801rrtrapBoardNumber_Object((1,3,6,1,4,1,20044,48,10,4),_Pm801rrtrapBoardNumber_Type())
pm801rrtrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pm801rrtrapBoardNumber.setStatus(_A)
pm801rrLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,30))
pm801rrLineTrapNotUrgentGoesOn.setObjects(*((_E,_I),(_E,_F)))
if mibBuilder.loadTexts:pm801rrLineTrapNotUrgentGoesOn.setStatus(_A)
pm801rrLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,31))
pm801rrLineTrapNotUrgentGoesOff.setObjects(*((_E,_I),(_E,_F)))
if mibBuilder.loadTexts:pm801rrLineTrapNotUrgentGoesOff.setStatus(_A)
pm801rrLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,32))
pm801rrLineTrapUrgentGoesOn.setObjects(*((_E,_J),(_E,_F)))
if mibBuilder.loadTexts:pm801rrLineTrapUrgentGoesOn.setStatus(_A)
pm801rrLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,33))
pm801rrLineTrapUrgentGoesOff.setObjects(*((_E,_J),(_E,_F)))
if mibBuilder.loadTexts:pm801rrLineTrapUrgentGoesOff.setStatus(_A)
pm801rrLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,34))
pm801rrLineTrapCritGoesOn.setObjects(*((_E,_K),(_E,_L),(_E,_F)))
if mibBuilder.loadTexts:pm801rrLineTrapCritGoesOn.setStatus(_A)
pm801rrLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,35))
pm801rrLineTrapCritGoesOff.setObjects(*((_E,_K),(_E,_L),(_E,_F)))
if mibBuilder.loadTexts:pm801rrLineTrapCritGoesOff.setStatus(_A)
pm801rrClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,40))
pm801rrClientTrapNotUrgentGoesOn.setObjects(*((_E,_M),(_E,_F)))
if mibBuilder.loadTexts:pm801rrClientTrapNotUrgentGoesOn.setStatus(_A)
pm801rrClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,41))
pm801rrClientTrapNotUrgentGoesOff.setObjects(*((_E,_M),(_E,_F)))
if mibBuilder.loadTexts:pm801rrClientTrapNotUrgentGoesOff.setStatus(_A)
pm801rrClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,42))
pm801rrClientTrapUrgentGoesOn.setObjects(*((_E,_N),(_E,_F)))
if mibBuilder.loadTexts:pm801rrClientTrapUrgentGoesOn.setStatus(_A)
pm801rrClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,43))
pm801rrClientTrapUrgentGoesOff.setObjects(*((_E,_N),(_E,_F)))
if mibBuilder.loadTexts:pm801rrClientTrapUrgentGoesOff.setStatus(_A)
pm801rrClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,44))
pm801rrClientTrapCritGoesOn.setObjects(*((_E,_O),(_E,_P),(_E,_F)))
if mibBuilder.loadTexts:pm801rrClientTrapCritGoesOn.setStatus(_A)
pm801rrClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,45))
pm801rrClientTrapCritGoesOff.setObjects(*((_E,_O),(_E,_P),(_E,_F)))
if mibBuilder.loadTexts:pm801rrClientTrapCritGoesOff.setStatus(_A)
pm801rrPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,48,10,50))
pm801rrPowerTrapUrgentGoesOn.setObjects(*((_E,_Q),(_E,_R),(_E,_F)))
if mibBuilder.loadTexts:pm801rrPowerTrapUrgentGoesOn.setStatus(_A)
pm801rrPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,48,10,51))
pm801rrPowerTrapUrgentGoesOff.setObjects(*((_E,_Q),(_E,_R),(_E,_F)))
if mibBuilder.loadTexts:pm801rrPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Pm801rrBitRate':Pm801rrBitRate,'Pm801rrOtxMode':Pm801rrOtxMode,'Pm801rrOtxGrid':Pm801rrOtxGrid,'Pm801rrAdjustValue':Pm801rrAdjustValue,'Pm801rrOtxChannel':Pm801rrOtxChannel,'modulePm801RR':modulePm801RR,'pm801rralarms':pm801rralarms,'pm801rrAlmOther':pm801rrAlmOther,'pm801rrAlmOtherNurg':pm801rrAlmOtherNurg,'pm801rrAlmOtherUrg':pm801rrAlmOtherUrg,'pm801rrAlmOtherCrit':pm801rrAlmOtherCrit,'pm801rrAlmsynthAlm0':pm801rrAlmsynthAlm0,'pm801rrAlmModuleGlobFailure':pm801rrAlmModuleGlobFailure,_R:pm801rrAlmDefFuseA,_Q:pm801rrAlmDefFuseB,'pm801rrAlmClient':pm801rrAlmClient,'pm801rrAlmClientNurg':pm801rrAlmClientNurg,'pm801rrAlmclientXfpWarnings':pm801rrAlmclientXfpWarnings,'pm801rrAlmClientTxPwrLowWng':pm801rrAlmClientTxPwrLowWng,'pm801rrAlmClientTxPwrHighWng':pm801rrAlmClientTxPwrHighWng,'pm801rrAlmClientTxBiasLowWng':pm801rrAlmClientTxBiasLowWng,'pm801rrAlmClientTxBiasHighWng':pm801rrAlmClientTxBiasHighWng,'pm801rrAlmClientTempLowWng':pm801rrAlmClientTempLowWng,'pm801rrAlmClientTempHighWng':pm801rrAlmClientTempHighWng,'pm801rrAlmClientRxPwrLowWng':pm801rrAlmClientRxPwrLowWng,'pm801rrAlmClientRxPwrHighWng':pm801rrAlmClientRxPwrHighWng,'pm801rrAlmclientOtxTlhWarnings':pm801rrAlmclientOtxTlhWarnings,'pm801rrAlmClientModulatorAgingHighWarning':pm801rrAlmClientModulatorAgingHighWarning,'pm801rrAlmClientAgingHighWarning':pm801rrAlmClientAgingHighWarning,'pm801rrAlmClientFreqDevHighWarning':pm801rrAlmClientFreqDevHighWarning,'pm801rrAlmClientLaserTempHighWarning':pm801rrAlmClientLaserTempHighWarning,'pm801rrAlmClientUrg':pm801rrAlmClientUrg,'pm801rrAlmclientXfpAlarm1':pm801rrAlmclientXfpAlarm1,'pm801rrAlmClientTxPwrLowAla':pm801rrAlmClientTxPwrLowAla,'pm801rrAlmClientTxPwrHighAla':pm801rrAlmClientTxPwrHighAla,'pm801rrAlmClientTxBiasLowAla':pm801rrAlmClientTxBiasLowAla,'pm801rrAlmClientTxBiasHighAla':pm801rrAlmClientTxBiasHighAla,'pm801rrAlmClientTempLowAla':pm801rrAlmClientTempLowAla,'pm801rrAlmClientTempHighAla':pm801rrAlmClientTempHighAla,'pm801rrAlmClientRxPwrLowAla':pm801rrAlmClientRxPwrLowAla,'pm801rrAlmClientRxPwrHighAla':pm801rrAlmClientRxPwrHighAla,'pm801rrAlmclientOtxTlhAlarms3':pm801rrAlmclientOtxTlhAlarms3,'pm801rrAlmClientModulatorAgingHighAla':pm801rrAlmClientModulatorAgingHighAla,'pm801rrAlmClientAgingHighAla':pm801rrAlmClientAgingHighAla,'pm801rrAlmClientCdrNotReady':pm801rrAlmClientCdrNotReady,'pm801rrAlmClientFreqDevHighAla':pm801rrAlmClientFreqDevHighAla,'pm801rrAlmClientLaserTempHighAla':pm801rrAlmClientLaserTempHighAla,'pm801rrAlmClientCrit':pm801rrAlmClientCrit,'pm801rrAlmsynthAlm8':pm801rrAlmsynthAlm8,'pm801rrAlmClientXfpAbsent':pm801rrAlmClientXfpAbsent,'pm801rrAlmClientInitNotCompl':pm801rrAlmClientInitNotCompl,_P:pm801rrAlmClientHwFail,'pm801rrAlmClientXfpTxOff':pm801rrAlmClientXfpTxOff,_M:pm801rrAlmClientDdmWarning,_N:pm801rrAlmClientDdmAlm,_O:pm801rrAlmClientFail,'pm801rrAlmClientVccWarning':pm801rrAlmClientVccWarning,'pm801rrAlmClientVccAlarm':pm801rrAlmClientVccAlarm,'pm801rrAlmclientXfpAlarms2':pm801rrAlmclientXfpAlarms2,'pm801rrAlmClientResetComplete':pm801rrAlmClientResetComplete,'pm801rrAlmClientRxCdrNotLocked':pm801rrAlmClientRxCdrNotLocked,'pm801rrAlmClientRxLos':pm801rrAlmClientRxLos,'pm801rrAlmClientRxNr':pm801rrAlmClientRxNr,'pm801rrAlmClientTxCdrNotLocked':pm801rrAlmClientTxCdrNotLocked,'pm801rrAlmClientTxFault':pm801rrAlmClientTxFault,'pm801rrAlmClientTxNr':pm801rrAlmClientTxNr,'pm801rrAlmClientChannelNotAcquired':pm801rrAlmClientChannelNotAcquired,'pm801rrAlmClientWavelengthUnlocked':pm801rrAlmClientWavelengthUnlocked,'pm801rrAlmClientTecFault':pm801rrAlmClientTecFault,'pm801rrAlmClientApdSupplyFault':pm801rrAlmClientApdSupplyFault,'pm801rrAlmLine':pm801rrAlmLine,'pm801rrAlmLineNurg':pm801rrAlmLineNurg,'pm801rrAlmlineXfpWarnings':pm801rrAlmlineXfpWarnings,'pm801rrAlmLineTxPwrLowWng':pm801rrAlmLineTxPwrLowWng,'pm801rrAlmLineTxPwrHighWng':pm801rrAlmLineTxPwrHighWng,'pm801rrAlmLineTxBiasLowWng':pm801rrAlmLineTxBiasLowWng,'pm801rrAlmLineTxBiasHighWng':pm801rrAlmLineTxBiasHighWng,'pm801rrAlmLineTempLowWng':pm801rrAlmLineTempLowWng,'pm801rrAlmLineTempHighWng':pm801rrAlmLineTempHighWng,'pm801rrAlmLineRxPwrLowWng':pm801rrAlmLineRxPwrLowWng,'pm801rrAlmLineRxPwrHighWng':pm801rrAlmLineRxPwrHighWng,'pm801rrAlmrrLineOtxTlhWarnings':pm801rrAlmrrLineOtxTlhWarnings,'pm801rrAlmLineModulatorAgingHighWarning':pm801rrAlmLineModulatorAgingHighWarning,'pm801rrAlmLineAgingHighWarning':pm801rrAlmLineAgingHighWarning,'pm801rrAlmLineFreqDevHighWarning':pm801rrAlmLineFreqDevHighWarning,'pm801rrAlmLineLaserTempHighWarning':pm801rrAlmLineLaserTempHighWarning,'pm801rrAlmLineUrg':pm801rrAlmLineUrg,'pm801rrAlmlineXfpAlarm1':pm801rrAlmlineXfpAlarm1,'pm801rrAlmLineTxPwrLowAla':pm801rrAlmLineTxPwrLowAla,'pm801rrAlmLineTxPwrHighAla':pm801rrAlmLineTxPwrHighAla,'pm801rrAlmLineTxBiasLowAla':pm801rrAlmLineTxBiasLowAla,'pm801rrAlmLineTxBiasHighAla':pm801rrAlmLineTxBiasHighAla,'pm801rrAlmLineTempLowAla':pm801rrAlmLineTempLowAla,'pm801rrAlmLineTempHighAla':pm801rrAlmLineTempHighAla,'pm801rrAlmLineRxPwrLowAla':pm801rrAlmLineRxPwrLowAla,'pm801rrAlmLineRxPwrHighAla':pm801rrAlmLineRxPwrHighAla,'pm801rrAlmrrLineOtxTlhAlarms3':pm801rrAlmrrLineOtxTlhAlarms3,'pm801rrAlmLineModulatorAgingHighAla':pm801rrAlmLineModulatorAgingHighAla,'pm801rrAlmLineAgingHighAla':pm801rrAlmLineAgingHighAla,'pm801rrAlmLineCdrNotReady':pm801rrAlmLineCdrNotReady,'pm801rrAlmLineFreqDevHighAla':pm801rrAlmLineFreqDevHighAla,'pm801rrAlmLineLaserTempHighAla':pm801rrAlmLineLaserTempHighAla,'pm801rrAlmLineCrit':pm801rrAlmLineCrit,'pm801rrAlmsynthAlm7':pm801rrAlmsynthAlm7,'pm801rrAlmLineXfpAbsent':pm801rrAlmLineXfpAbsent,'pm801rrAlmLineInitNotCompl':pm801rrAlmLineInitNotCompl,_L:pm801rrAlmLineHwFail,'pm801rrAlmLineXfpTxOff':pm801rrAlmLineXfpTxOff,_I:pm801rrAlmLineDdmWarning,_J:pm801rrAlmLineDdmAlm,_K:pm801rrAlmLineFail,'pm801rrAlmLineVccWarning':pm801rrAlmLineVccWarning,'pm801rrAlmLineVccAlarm':pm801rrAlmLineVccAlarm,'pm801rrAlmlineXfpAlarms2':pm801rrAlmlineXfpAlarms2,'pm801rrAlmLineResetComplete':pm801rrAlmLineResetComplete,'pm801rrAlmLineRxCdrNotLocked':pm801rrAlmLineRxCdrNotLocked,'pm801rrAlmLineRxLos':pm801rrAlmLineRxLos,'pm801rrAlmLineRxNr':pm801rrAlmLineRxNr,'pm801rrAlmLineTxCdrNotLocked':pm801rrAlmLineTxCdrNotLocked,'pm801rrAlmLineTxFault':pm801rrAlmLineTxFault,'pm801rrAlmLineTxNr':pm801rrAlmLineTxNr,'pm801rrAlmLineChannelNotAcquired':pm801rrAlmLineChannelNotAcquired,'pm801rrAlmLineWavelengthUnlocked':pm801rrAlmLineWavelengthUnlocked,'pm801rrAlmLineTecFault':pm801rrAlmLineTecFault,'pm801rrAlmLineApdSupplyFault':pm801rrAlmLineApdSupplyFault,'pm801rrmeasures':pm801rrmeasures,'pm801rrMesrOther':pm801rrMesrOther,'pm801rrMesrClient':pm801rrMesrClient,'pm801rrMesrclientTemperature':pm801rrMesrclientTemperature,'pm801rrMesrclientTxBias':pm801rrMesrclientTxBias,'pm801rrMesrclientTxPower':pm801rrMesrclientTxPower,'pm801rrMesrclientRxPower':pm801rrMesrclientRxPower,'pm801rrMesrclientAging':pm801rrMesrclientAging,'pm801rrMesrclientLaserTemperature':pm801rrMesrclientLaserTemperature,'pm801rrMesrclientFreqDeviation':pm801rrMesrclientFreqDeviation,'pm801rrMesrclientLaserWvlength':pm801rrMesrclientLaserWvlength,'pm801rrMesrLine':pm801rrMesrLine,'pm801rrMesrlineTemperature':pm801rrMesrlineTemperature,'pm801rrMesrlineTxBias':pm801rrMesrlineTxBias,'pm801rrMesrlineTxPower':pm801rrMesrlineTxPower,'pm801rrMesrlineRxPower':pm801rrMesrlineRxPower,'pm801rrMesrlineAging':pm801rrMesrlineAging,'pm801rrMesrlineLaserTemperature':pm801rrMesrlineLaserTemperature,'pm801rrMesrlineFreqDeviation':pm801rrMesrlineFreqDeviation,'pm801rrMesrlineLaserWvlength':pm801rrMesrlineLaserWvlength,'pm801rrcontrolsWrite':pm801rrcontrolsWrite,'pm801rrCtrlOther':pm801rrCtrlOther,'pm801rrCtrlsynth0':pm801rrCtrlsynth0,'pm801rrCtrlConfLoad':pm801rrCtrlConfLoad,'pm801rrCtrlConfFlash':pm801rrCtrlConfFlash,'pm801rrCtrlConfClear':pm801rrCtrlConfClear,'pm801rrCtrlsynth4':pm801rrCtrlsynth4,'pm801rrCtrlCorrelatOn':pm801rrCtrlCorrelatOn,'pm801rrCtrlCorrelatOff':pm801rrCtrlCorrelatOff,'pm801rrCtrlswMgnt':pm801rrCtrlswMgnt,'pm801rrCtrlColdReset':pm801rrCtrlColdReset,'pm801rrCtrlWarmReset':pm801rrCtrlWarmReset,'pm801rrCtrlledTest':pm801rrCtrlledTest,'pm801rrCtrlGreenLed':pm801rrCtrlGreenLed,'pm801rrCtrlRedLed':pm801rrCtrlRedLed,'pm801rrCtrlLedOff':pm801rrCtrlLedOff,'pm801rrCtrlClient':pm801rrCtrlClient,'pm801rrCtrlclientXfpOnoff':pm801rrCtrlclientXfpOnoff,'pm801rrCtrlClientXfpOnoff':pm801rrCtrlClientXfpOnoff,'pm801rrCtrlclientXfpLineLoop':pm801rrCtrlclientXfpLineLoop,'pm801rrCtrlClientXfpLineLoop':pm801rrCtrlClientXfpLineLoop,'pm801rrCtrlclientXfiLoop':pm801rrCtrlclientXfiLoop,'pm801rrCtrlClientXfiLoop':pm801rrCtrlClientXfiLoop,'pm801rrCtrlclientTunableChannel':pm801rrCtrlclientTunableChannel,'pm801rrCtrlclientPhotodiodeMode':pm801rrCtrlclientPhotodiodeMode,'pm801rrCtrlclientPhotodiodeValue':pm801rrCtrlclientPhotodiodeValue,'pm801rrCtrlclientPowerLaser':pm801rrCtrlclientPowerLaser,'pm801rrCtrlLine':pm801rrCtrlLine,'pm801rrCtrlclientOtxVlhReset':pm801rrCtrlclientOtxVlhReset,'pm801rrCtrlClientOtxVlhReset':pm801rrCtrlClientOtxVlhReset,'pm801rrCtrllineXfpOnoff':pm801rrCtrllineXfpOnoff,'pm801rrCtrlLineXfpOnoff':pm801rrCtrlLineXfpOnoff,'pm801rrCtrllineXfpLineLoop':pm801rrCtrllineXfpLineLoop,'pm801rrCtrlLineXfpLineLoop':pm801rrCtrlLineXfpLineLoop,'pm801rrCtrllineXfiLoop':pm801rrCtrllineXfiLoop,'pm801rrCtrlLineXfiLoop':pm801rrCtrlLineXfiLoop,'pm801rrCtrllineTunableChannel':pm801rrCtrllineTunableChannel,'pm801rrCtrllinePhotodiodeMode':pm801rrCtrllinePhotodiodeMode,'pm801rrCtrllinePhotodiodeValue':pm801rrCtrllinePhotodiodeValue,'pm801rrCtrllinePowerLaser':pm801rrCtrllinePowerLaser,'pm801rrCtrllineOtxVlhReset':pm801rrCtrllineOtxVlhReset,'pm801rrCtrlLineOtxVlhReset':pm801rrCtrlLineOtxVlhReset,'pm801rrri':pm801rrri,'pm801rrRinvReloadInventory':pm801rrRinvReloadInventory,'pm801rrRinvHwPlatform':pm801rrRinvHwPlatform,'pm801rrRinvSwPlatform':pm801rrRinvSwPlatform,'pm801rrRinvClientXFP':pm801rrRinvClientXFP,'pm801rrRinvLineXFP':pm801rrRinvLineXFP,'pm801rrConfig':pm801rrConfig,'pm801rrCfgLsd':pm801rrCfgLsd,'pm801rrtableclientLsd':pm801rrtableclientLsd,'pm801rrCfglsdMode':pm801rrCfglsdMode,'pm801rrCfgclientXfpAlarms':pm801rrCfgclientXfpAlarms,'pm801rrCfgclientXfpAbsence':pm801rrCfgclientXfpAbsence,'pm801rrCfglineXfpAlarms':pm801rrCfglineXfpAlarms,'pm801rrCfglineXfpAbsence':pm801rrCfglineXfpAbsence,'pm801rrCfgStartUp':pm801rrCfgStartUp,'pm801rrtableclientStartup':pm801rrtableclientStartup,'pm801rrCfgclientXfpCtrl':pm801rrCfgclientXfpCtrl,'pm801rrtablelineStartup':pm801rrtablelineStartup,'pm801rrCfglineXfpCtrl':pm801rrCfglineXfpCtrl,'pm801rrCfgprotocolSelect':pm801rrCfgprotocolSelect,'pm801rrtableclientOtxtlh':pm801rrtableclientOtxtlh,'pm801rrCfgclientDitherControl':pm801rrCfgclientDitherControl,'pm801rrCfgclientDitherRate':pm801rrCfgclientDitherRate,'pm801rrCfgclientDitherFhz':pm801rrCfgclientDitherFhz,'pm801rrCfgclientPwrLaser':pm801rrCfgclientPwrLaser,'pm801rrCfgclientFCurrent':pm801rrCfgclientFCurrent,'pm801rrCfgclientGridCurrent':pm801rrCfgclientGridCurrent,'pm801rrCfgclientF0':pm801rrCfgclientF0,'pm801rrCfgclientPhotodiodeMode':pm801rrCfgclientPhotodiodeMode,'pm801rrCfgclientPhotodiodeValue':pm801rrCfgclientPhotodiodeValue,'pm801rrtablelineOtxtlh':pm801rrtablelineOtxtlh,'pm801rrCfglineDitherControl':pm801rrCfglineDitherControl,'pm801rrCfglineDitherRate':pm801rrCfglineDitherRate,'pm801rrCfglineDitherFhz':pm801rrCfglineDitherFhz,'pm801rrCfglinePwrLaser':pm801rrCfglinePwrLaser,'pm801rrCfglineFCurrent':pm801rrCfglineFCurrent,'pm801rrCfglineGridCurrent':pm801rrCfglineGridCurrent,'pm801rrCfglineF0':pm801rrCfglineF0,'pm801rrCfglinePhotodiodeMode':pm801rrCfglinePhotodiodeMode,'pm801rrCfglinePhotodiodeValue':pm801rrCfglinePhotodiodeValue,'pm801rrCfgLabels':pm801rrCfgLabels,'pm801rrCfgLabelclientTable':pm801rrCfgLabelclientTable,'pm801rrCfgLabelclientEntry':pm801rrCfgLabelclientEntry,_T:pm801rrCfgLabelclientIndex,'pm801rrCfgLabelclientPortn':pm801rrCfgLabelclientPortn,'pm801rrCfgLabellineTable':pm801rrCfgLabellineTable,'pm801rrCfgLabellineEntry':pm801rrCfgLabellineEntry,_U:pm801rrCfgLabellineIndex,'pm801rrCfgLabellinePortn':pm801rrCfgLabellinePortn,'pm801rrCfgStartuptablefive':pm801rrCfgStartuptablefive,'pm801rrCfgOtxtlhcapabilitiesTable':pm801rrCfgOtxtlhcapabilitiesTable,'pm801rrCfgOtxtlhcapabilitiesEntry':pm801rrCfgOtxtlhcapabilitiesEntry,_V:pm801rrCfgOtxtlhcapabilitiesIndex,'pm801rrCfgComponentTypePortn':pm801rrCfgComponentTypePortn,'pm801rrCfgMiscellaneousPortn':pm801rrCfgMiscellaneousPortn,'pm801rrCfgFirstChannelPortn':pm801rrCfgFirstChannelPortn,'pm801rrCfgLastChannelPortn':pm801rrCfgLastChannelPortn,'pm801rrCfgGridPortn':pm801rrCfgGridPortn,'pm801rrCfgWriteConfiguration':pm801rrCfgWriteConfiguration,'pm801rrtraps':pm801rrtraps,_F:pm801rrtrapBoardNumber,'pm801rrLineTrapNotUrgentGoesOn':pm801rrLineTrapNotUrgentGoesOn,'pm801rrLineTrapNotUrgentGoesOff':pm801rrLineTrapNotUrgentGoesOff,'pm801rrLineTrapUrgentGoesOn':pm801rrLineTrapUrgentGoesOn,'pm801rrLineTrapUrgentGoesOff':pm801rrLineTrapUrgentGoesOff,'pm801rrLineTrapCritGoesOn':pm801rrLineTrapCritGoesOn,'pm801rrLineTrapCritGoesOff':pm801rrLineTrapCritGoesOff,'pm801rrClientTrapNotUrgentGoesOn':pm801rrClientTrapNotUrgentGoesOn,'pm801rrClientTrapNotUrgentGoesOff':pm801rrClientTrapNotUrgentGoesOff,'pm801rrClientTrapUrgentGoesOn':pm801rrClientTrapUrgentGoesOn,'pm801rrClientTrapUrgentGoesOff':pm801rrClientTrapUrgentGoesOff,'pm801rrClientTrapCritGoesOn':pm801rrClientTrapCritGoesOn,'pm801rrClientTrapCritGoesOff':pm801rrClientTrapCritGoesOff,'pm801rrPowerTrapUrgentGoesOn':pm801rrPowerTrapUrgentGoesOn,'pm801rrPowerTrapUrgentGoesOff':pm801rrPowerTrapUrgentGoesOff})