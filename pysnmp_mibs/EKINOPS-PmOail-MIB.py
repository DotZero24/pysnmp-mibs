_V='pmoailCfgLabellineIndex'
_U='pmoailCfgLabelclientIndex'
_T='pmoailRinvInLine2Index'
_S='pmoailRinvInLine1Index'
_R='pmoailAlmDefFuseA'
_Q='pmoailAlmDefFuseB'
_P='pmoailAlmClientHwFail'
_O='pmoailAlmClientFail'
_N='pmoailAlmClientDdmAlm'
_M='pmoailAlmClientDdmWarning'
_L='pmoailAlmLineHwFail'
_K='pmoailAlmLineFail'
_J='pmoailAlmLineDdmAlm'
_I='pmoailAlmLineDdmWarning'
_H='DisplayString'
_G='Unsigned32'
_F='pmoailtrapBoardNumber'
_E='Integer32'
_D='read-write'
_C='EKINOPS-PmOail-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
modulepmoail=ModuleIdentity((1,3,6,1,4,1,20044,36))
if mibBuilder.loadTexts:modulepmoail.setRevisions(('2009-03-23 00:00','2009-04-08 00:00','2009-09-24 00:00','2009-12-14 00:00','2010-02-24 00:00','2010-07-15 00:00','2010-10-29 00:00','2010-11-03 00:00','2012-07-04 00:00','2012-10-05 00:00','2014-03-26 00:00','2014-12-10 00:00','2016-05-23 00:00'))
class PmoailpreampMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oapreampdefaultmode',0),('oapreampconstantcurrentmode',1),('oapreampconstantpowermode',2)))
class PmoailboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oaboosterdefaultmode',0),('oaboosterconstantcurrentmode',1),('oaboosterconstantpowermode',2)))
_Pmoailalarms_ObjectIdentity=ObjectIdentity
pmoailalarms=_Pmoailalarms_ObjectIdentity((1,3,6,1,4,1,20044,36,2))
_PmoailAlmOther_ObjectIdentity=ObjectIdentity
pmoailAlmOther=_PmoailAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1))
_PmoailAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoailAlmOtherNurg=_PmoailAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,1))
_PmoailAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoailAlmsynthAlm2=_PmoailAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,1,2))
_PmoailAlmConfTableSave_Type=EkiOnOff
_PmoailAlmConfTableSave_Object=MibScalar
pmoailAlmConfTableSave=_PmoailAlmConfTableSave_Object((1,3,6,1,4,1,20044,36,2,1,1,2,1),_PmoailAlmConfTableSave_Type())
pmoailAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmConfTableSave.setStatus(_A)
_PmoailAlmInvUpload_Type=EkiOnOff
_PmoailAlmInvUpload_Object=MibScalar
pmoailAlmInvUpload=_PmoailAlmInvUpload_Object((1,3,6,1,4,1,20044,36,2,1,1,2,2),_PmoailAlmInvUpload_Type())
pmoailAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmInvUpload.setStatus(_A)
_PmoailAlmConfTableLoad_Type=EkiOnOff
_PmoailAlmConfTableLoad_Object=MibScalar
pmoailAlmConfTableLoad=_PmoailAlmConfTableLoad_Object((1,3,6,1,4,1,20044,36,2,1,1,2,3),_PmoailAlmConfTableLoad_Type())
pmoailAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmConfTableLoad.setStatus(_A)
_PmoailAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoailAlmfoaWarnings=_PmoailAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,1,75))
_PmoailAlm3v3LowWarning_Type=EkiOnOff
_PmoailAlm3v3LowWarning_Object=MibScalar
pmoailAlm3v3LowWarning=_PmoailAlm3v3LowWarning_Object((1,3,6,1,4,1,20044,36,2,1,1,75,5),_PmoailAlm3v3LowWarning_Type())
pmoailAlm3v3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlm3v3LowWarning.setStatus(_A)
_PmoailAlm3v3HighWarning_Type=EkiOnOff
_PmoailAlm3v3HighWarning_Object=MibScalar
pmoailAlm3v3HighWarning=_PmoailAlm3v3HighWarning_Object((1,3,6,1,4,1,20044,36,2,1,1,75,6),_PmoailAlm3v3HighWarning_Type())
pmoailAlm3v3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlm3v3HighWarning.setStatus(_A)
_PmoailAlmTermpLowWarning_Type=EkiOnOff
_PmoailAlmTermpLowWarning_Object=MibScalar
pmoailAlmTermpLowWarning=_PmoailAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,36,2,1,1,75,7),_PmoailAlmTermpLowWarning_Type())
pmoailAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmTermpLowWarning.setStatus(_A)
_PmoailAlmTempHighWarning_Type=EkiOnOff
_PmoailAlmTempHighWarning_Object=MibScalar
pmoailAlmTempHighWarning=_PmoailAlmTempHighWarning_Object((1,3,6,1,4,1,20044,36,2,1,1,75,8),_PmoailAlmTempHighWarning_Type())
pmoailAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmTempHighWarning.setStatus(_A)
_PmoailAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoailAlmOtherUrg=_PmoailAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,2))
_PmoailAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoailAlmfoaAlarms=_PmoailAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,2,74))
_PmoailAlm3v3LowAlarm_Type=EkiOnOff
_PmoailAlm3v3LowAlarm_Object=MibScalar
pmoailAlm3v3LowAlarm=_PmoailAlm3v3LowAlarm_Object((1,3,6,1,4,1,20044,36,2,1,2,74,5),_PmoailAlm3v3LowAlarm_Type())
pmoailAlm3v3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlm3v3LowAlarm.setStatus(_A)
_PmoailAlm3v3HighAlarm_Type=EkiOnOff
_PmoailAlm3v3HighAlarm_Object=MibScalar
pmoailAlm3v3HighAlarm=_PmoailAlm3v3HighAlarm_Object((1,3,6,1,4,1,20044,36,2,1,2,74,6),_PmoailAlm3v3HighAlarm_Type())
pmoailAlm3v3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlm3v3HighAlarm.setStatus(_A)
_PmoailAlmTermpLowAlarm_Type=EkiOnOff
_PmoailAlmTermpLowAlarm_Object=MibScalar
pmoailAlmTermpLowAlarm=_PmoailAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,36,2,1,2,74,7),_PmoailAlmTermpLowAlarm_Type())
pmoailAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmTermpLowAlarm.setStatus(_A)
_PmoailAlmTempHighAlarm_Type=EkiOnOff
_PmoailAlmTempHighAlarm_Object=MibScalar
pmoailAlmTempHighAlarm=_PmoailAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,36,2,1,2,74,8),_PmoailAlmTempHighAlarm_Type())
pmoailAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmTempHighAlarm.setStatus(_A)
_PmoailAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoailAlmOtherCrit=_PmoailAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,3))
_PmoailAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoailAlmsynthAlm0=_PmoailAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,36,2,1,3,0))
_PmoailAlmMaintenanceMode_Type=EkiOnOff
_PmoailAlmMaintenanceMode_Object=MibScalar
pmoailAlmMaintenanceMode=_PmoailAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,36,2,1,3,0,1),_PmoailAlmMaintenanceMode_Type())
pmoailAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmMaintenanceMode.setStatus(_A)
_PmoailAlmModGlobFail_Type=EkiOnOff
_PmoailAlmModGlobFail_Object=MibScalar
pmoailAlmModGlobFail=_PmoailAlmModGlobFail_Object((1,3,6,1,4,1,20044,36,2,1,3,0,9),_PmoailAlmModGlobFail_Type())
pmoailAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmModGlobFail.setStatus(_A)
_PmoailAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoailAlmUpEdfaInitNotCompl_Object=MibScalar
pmoailAlmUpEdfaInitNotCompl=_PmoailAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,36,2,1,3,0,10),_PmoailAlmUpEdfaInitNotCompl_Type())
pmoailAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoailAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoailAlmDwEdfaInitNotCompl_Object=MibScalar
pmoailAlmDwEdfaInitNotCompl=_PmoailAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,36,2,1,3,0,11),_PmoailAlmDwEdfaInitNotCompl_Type())
pmoailAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoailAlmExtPumpNotLocked_Type=EkiOnOff
_PmoailAlmExtPumpNotLocked_Object=MibScalar
pmoailAlmExtPumpNotLocked=_PmoailAlmExtPumpNotLocked_Object((1,3,6,1,4,1,20044,36,2,1,3,0,12),_PmoailAlmExtPumpNotLocked_Type())
pmoailAlmExtPumpNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmExtPumpNotLocked.setStatus(_A)
_PmoailAlmDefFuseA_Type=EkiOnOff
_PmoailAlmDefFuseA_Object=MibScalar
pmoailAlmDefFuseA=_PmoailAlmDefFuseA_Object((1,3,6,1,4,1,20044,36,2,1,3,0,15),_PmoailAlmDefFuseA_Type())
pmoailAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmDefFuseA.setStatus(_A)
_PmoailAlmDefFuseB_Type=EkiOnOff
_PmoailAlmDefFuseB_Object=MibScalar
pmoailAlmDefFuseB=_PmoailAlmDefFuseB_Object((1,3,6,1,4,1,20044,36,2,1,3,0,16),_PmoailAlmDefFuseB_Type())
pmoailAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmDefFuseB.setStatus(_A)
_PmoailAlmClient_ObjectIdentity=ObjectIdentity
pmoailAlmClient=_PmoailAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2))
_PmoailAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoailAlmClientNurg=_PmoailAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,1))
_PmoailAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoailAlmclientEdfaWarnings=_PmoailAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,1,33))
_PmoailAlmClientGainLowWarning_Type=EkiOnOff
_PmoailAlmClientGainLowWarning_Object=MibScalar
pmoailAlmClientGainLowWarning=_PmoailAlmClientGainLowWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,1),_PmoailAlmClientGainLowWarning_Type())
pmoailAlmClientGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientGainLowWarning.setStatus(_A)
_PmoailAlmClientGainHighWarning_Type=EkiOnOff
_PmoailAlmClientGainHighWarning_Object=MibScalar
pmoailAlmClientGainHighWarning=_PmoailAlmClientGainHighWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,2),_PmoailAlmClientGainHighWarning_Type())
pmoailAlmClientGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientGainHighWarning.setStatus(_A)
_PmoailAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoailAlmClientInputPwrLowWarning_Object=MibScalar
pmoailAlmClientInputPwrLowWarning=_PmoailAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,3),_PmoailAlmClientInputPwrLowWarning_Type())
pmoailAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientInputPwrLowWarning.setStatus(_A)
_PmoailAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoailAlmClientInputPwrHighWarning_Object=MibScalar
pmoailAlmClientInputPwrHighWarning=_PmoailAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,4),_PmoailAlmClientInputPwrHighWarning_Type())
pmoailAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientInputPwrHighWarning.setStatus(_A)
_PmoailAlmClientOutputPwrLowWarning_Type=EkiOnOff
_PmoailAlmClientOutputPwrLowWarning_Object=MibScalar
pmoailAlmClientOutputPwrLowWarning=_PmoailAlmClientOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,5),_PmoailAlmClientOutputPwrLowWarning_Type())
pmoailAlmClientOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientOutputPwrLowWarning.setStatus(_A)
_PmoailAlmClientOutputPwrHighWarning_Type=EkiOnOff
_PmoailAlmClientOutputPwrHighWarning_Object=MibScalar
pmoailAlmClientOutputPwrHighWarning=_PmoailAlmClientOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,6),_PmoailAlmClientOutputPwrHighWarning_Type())
pmoailAlmClientOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientOutputPwrHighWarning.setStatus(_A)
_PmoailAlmClientBiasLowWarning_Type=EkiOnOff
_PmoailAlmClientBiasLowWarning_Object=MibScalar
pmoailAlmClientBiasLowWarning=_PmoailAlmClientBiasLowWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,7),_PmoailAlmClientBiasLowWarning_Type())
pmoailAlmClientBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientBiasLowWarning.setStatus(_A)
_PmoailAlmClientBiasHighWarning_Type=EkiOnOff
_PmoailAlmClientBiasHighWarning_Object=MibScalar
pmoailAlmClientBiasHighWarning=_PmoailAlmClientBiasHighWarning_Object((1,3,6,1,4,1,20044,36,2,2,1,33,8),_PmoailAlmClientBiasHighWarning_Type())
pmoailAlmClientBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientBiasHighWarning.setStatus(_A)
_PmoailAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoailAlmClientUrg=_PmoailAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,2))
_PmoailAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoailAlmclientEdfaAlarms1=_PmoailAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,2,32))
_PmoailAlmClientGainLowAlarm_Type=EkiOnOff
_PmoailAlmClientGainLowAlarm_Object=MibScalar
pmoailAlmClientGainLowAlarm=_PmoailAlmClientGainLowAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,1),_PmoailAlmClientGainLowAlarm_Type())
pmoailAlmClientGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientGainLowAlarm.setStatus(_A)
_PmoailAlmClientGainHighAlarm_Type=EkiOnOff
_PmoailAlmClientGainHighAlarm_Object=MibScalar
pmoailAlmClientGainHighAlarm=_PmoailAlmClientGainHighAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,2),_PmoailAlmClientGainHighAlarm_Type())
pmoailAlmClientGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientGainHighAlarm.setStatus(_A)
_PmoailAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoailAlmClientInputPwrLowAlarm_Object=MibScalar
pmoailAlmClientInputPwrLowAlarm=_PmoailAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,3),_PmoailAlmClientInputPwrLowAlarm_Type())
pmoailAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoailAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoailAlmClientInputPwrHighAlarm_Object=MibScalar
pmoailAlmClientInputPwrHighAlarm=_PmoailAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,4),_PmoailAlmClientInputPwrHighAlarm_Type())
pmoailAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoailAlmClientOutputPwrLowAlarm_Type=EkiOnOff
_PmoailAlmClientOutputPwrLowAlarm_Object=MibScalar
pmoailAlmClientOutputPwrLowAlarm=_PmoailAlmClientOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,5),_PmoailAlmClientOutputPwrLowAlarm_Type())
pmoailAlmClientOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientOutputPwrLowAlarm.setStatus(_A)
_PmoailAlmClientOutputPwrHighAlarm_Type=EkiOnOff
_PmoailAlmClientOutputPwrHighAlarm_Object=MibScalar
pmoailAlmClientOutputPwrHighAlarm=_PmoailAlmClientOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,6),_PmoailAlmClientOutputPwrHighAlarm_Type())
pmoailAlmClientOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientOutputPwrHighAlarm.setStatus(_A)
_PmoailAlmClientBiasLowAlarm_Type=EkiOnOff
_PmoailAlmClientBiasLowAlarm_Object=MibScalar
pmoailAlmClientBiasLowAlarm=_PmoailAlmClientBiasLowAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,7),_PmoailAlmClientBiasLowAlarm_Type())
pmoailAlmClientBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientBiasLowAlarm.setStatus(_A)
_PmoailAlmClientBiasHighAlarm_Type=EkiOnOff
_PmoailAlmClientBiasHighAlarm_Object=MibScalar
pmoailAlmClientBiasHighAlarm=_PmoailAlmClientBiasHighAlarm_Object((1,3,6,1,4,1,20044,36,2,2,2,32,8),_PmoailAlmClientBiasHighAlarm_Type())
pmoailAlmClientBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientBiasHighAlarm.setStatus(_A)
_PmoailAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoailAlmClientCrit=_PmoailAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,3))
_PmoailAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoailAlmsynthAlm8=_PmoailAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,3,8))
_PmoailAlmClientHwFail_Type=EkiOnOff
_PmoailAlmClientHwFail_Object=MibScalar
pmoailAlmClientHwFail=_PmoailAlmClientHwFail_Object((1,3,6,1,4,1,20044,36,2,2,3,8,4),_PmoailAlmClientHwFail_Type())
pmoailAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientHwFail.setStatus(_A)
_PmoailAlmClientTxOff_Type=EkiOnOff
_PmoailAlmClientTxOff_Object=MibScalar
pmoailAlmClientTxOff=_PmoailAlmClientTxOff_Object((1,3,6,1,4,1,20044,36,2,2,3,8,5),_PmoailAlmClientTxOff_Type())
pmoailAlmClientTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientTxOff.setStatus(_A)
_PmoailAlmClientDdmWarning_Type=EkiOnOff
_PmoailAlmClientDdmWarning_Object=MibScalar
pmoailAlmClientDdmWarning=_PmoailAlmClientDdmWarning_Object((1,3,6,1,4,1,20044,36,2,2,3,8,9),_PmoailAlmClientDdmWarning_Type())
pmoailAlmClientDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientDdmWarning.setStatus(_A)
_PmoailAlmClientDdmAlm_Type=EkiOnOff
_PmoailAlmClientDdmAlm_Object=MibScalar
pmoailAlmClientDdmAlm=_PmoailAlmClientDdmAlm_Object((1,3,6,1,4,1,20044,36,2,2,3,8,10),_PmoailAlmClientDdmAlm_Type())
pmoailAlmClientDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientDdmAlm.setStatus(_A)
_PmoailAlmClientFail_Type=EkiOnOff
_PmoailAlmClientFail_Object=MibScalar
pmoailAlmClientFail=_PmoailAlmClientFail_Object((1,3,6,1,4,1,20044,36,2,2,3,8,12),_PmoailAlmClientFail_Type())
pmoailAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientFail.setStatus(_A)
_PmoailAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoailAlmclientEdfaAlarms2=_PmoailAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,36,2,2,3,35))
_PmoailAlmClientEdfaNr_Type=EkiOnOff
_PmoailAlmClientEdfaNr_Object=MibScalar
pmoailAlmClientEdfaNr=_PmoailAlmClientEdfaNr_Object((1,3,6,1,4,1,20044,36,2,2,3,35,1),_PmoailAlmClientEdfaNr_Type())
pmoailAlmClientEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientEdfaNr.setStatus(_A)
_PmoailAlmClientEdfaTecFail_Type=EkiOnOff
_PmoailAlmClientEdfaTecFail_Object=MibScalar
pmoailAlmClientEdfaTecFail=_PmoailAlmClientEdfaTecFail_Object((1,3,6,1,4,1,20044,36,2,2,3,35,2),_PmoailAlmClientEdfaTecFail_Type())
pmoailAlmClientEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientEdfaTecFail.setStatus(_A)
_PmoailAlmClientEdfaLaserFail_Type=EkiOnOff
_PmoailAlmClientEdfaLaserFail_Object=MibScalar
pmoailAlmClientEdfaLaserFail=_PmoailAlmClientEdfaLaserFail_Object((1,3,6,1,4,1,20044,36,2,2,3,35,3),_PmoailAlmClientEdfaLaserFail_Type())
pmoailAlmClientEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientEdfaLaserFail.setStatus(_A)
_PmoailAlmClientEdfaLos_Type=EkiOnOff
_PmoailAlmClientEdfaLos_Object=MibScalar
pmoailAlmClientEdfaLos=_PmoailAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,36,2,2,3,35,4),_PmoailAlmClientEdfaLos_Type())
pmoailAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientEdfaLos.setStatus(_A)
_PmoailAlmClientExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoailAlmClientExtPumpEdfaLowCurrent_Object=MibScalar
pmoailAlmClientExtPumpEdfaLowCurrent=_PmoailAlmClientExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,36,2,2,3,35,5),_PmoailAlmClientExtPumpEdfaLowCurrent_Type())
pmoailAlmClientExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmClientExtPumpEdfaLowCurrent.setStatus(_A)
_PmoailAlmLine_ObjectIdentity=ObjectIdentity
pmoailAlmLine=_PmoailAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3))
_PmoailAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoailAlmLineNurg=_PmoailAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,1))
_PmoailAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoailAlmlineEdfaWarnings=_PmoailAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,1,41))
_PmoailAlmLineGainLowWarning_Type=EkiOnOff
_PmoailAlmLineGainLowWarning_Object=MibScalar
pmoailAlmLineGainLowWarning=_PmoailAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,1),_PmoailAlmLineGainLowWarning_Type())
pmoailAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineGainLowWarning.setStatus(_A)
_PmoailAlmLineGainHighWarning_Type=EkiOnOff
_PmoailAlmLineGainHighWarning_Object=MibScalar
pmoailAlmLineGainHighWarning=_PmoailAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,2),_PmoailAlmLineGainHighWarning_Type())
pmoailAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineGainHighWarning.setStatus(_A)
_PmoailAlmLineInputPwrLowWarning_Type=EkiOnOff
_PmoailAlmLineInputPwrLowWarning_Object=MibScalar
pmoailAlmLineInputPwrLowWarning=_PmoailAlmLineInputPwrLowWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,3),_PmoailAlmLineInputPwrLowWarning_Type())
pmoailAlmLineInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineInputPwrLowWarning.setStatus(_A)
_PmoailAlmLineInputPwrHighWarning_Type=EkiOnOff
_PmoailAlmLineInputPwrHighWarning_Object=MibScalar
pmoailAlmLineInputPwrHighWarning=_PmoailAlmLineInputPwrHighWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,4),_PmoailAlmLineInputPwrHighWarning_Type())
pmoailAlmLineInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineInputPwrHighWarning.setStatus(_A)
_PmoailAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoailAlmLineOutputPwrLowWarning_Object=MibScalar
pmoailAlmLineOutputPwrLowWarning=_PmoailAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,5),_PmoailAlmLineOutputPwrLowWarning_Type())
pmoailAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoailAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoailAlmLineOutputPwrHighWarning_Object=MibScalar
pmoailAlmLineOutputPwrHighWarning=_PmoailAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,6),_PmoailAlmLineOutputPwrHighWarning_Type())
pmoailAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoailAlmLineBiasLowWarning_Type=EkiOnOff
_PmoailAlmLineBiasLowWarning_Object=MibScalar
pmoailAlmLineBiasLowWarning=_PmoailAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,7),_PmoailAlmLineBiasLowWarning_Type())
pmoailAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineBiasLowWarning.setStatus(_A)
_PmoailAlmLineBiasHighWarning_Type=EkiOnOff
_PmoailAlmLineBiasHighWarning_Object=MibScalar
pmoailAlmLineBiasHighWarning=_PmoailAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,36,2,3,1,41,8),_PmoailAlmLineBiasHighWarning_Type())
pmoailAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineBiasHighWarning.setStatus(_A)
_PmoailAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoailAlmLineUrg=_PmoailAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,2))
_PmoailAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoailAlmlineEdfaAlarms1=_PmoailAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,2,40))
_PmoailAlmLineGainLowAlarm_Type=EkiOnOff
_PmoailAlmLineGainLowAlarm_Object=MibScalar
pmoailAlmLineGainLowAlarm=_PmoailAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,1),_PmoailAlmLineGainLowAlarm_Type())
pmoailAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineGainLowAlarm.setStatus(_A)
_PmoailAlmLineGainHighAlarm_Type=EkiOnOff
_PmoailAlmLineGainHighAlarm_Object=MibScalar
pmoailAlmLineGainHighAlarm=_PmoailAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,2),_PmoailAlmLineGainHighAlarm_Type())
pmoailAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineGainHighAlarm.setStatus(_A)
_PmoailAlmLineInputPwrLowAlarm_Type=EkiOnOff
_PmoailAlmLineInputPwrLowAlarm_Object=MibScalar
pmoailAlmLineInputPwrLowAlarm=_PmoailAlmLineInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,3),_PmoailAlmLineInputPwrLowAlarm_Type())
pmoailAlmLineInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineInputPwrLowAlarm.setStatus(_A)
_PmoailAlmLineInputPwrHighAlarm_Type=EkiOnOff
_PmoailAlmLineInputPwrHighAlarm_Object=MibScalar
pmoailAlmLineInputPwrHighAlarm=_PmoailAlmLineInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,4),_PmoailAlmLineInputPwrHighAlarm_Type())
pmoailAlmLineInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineInputPwrHighAlarm.setStatus(_A)
_PmoailAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoailAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoailAlmLineOutputPwrLowAlarm=_PmoailAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,5),_PmoailAlmLineOutputPwrLowAlarm_Type())
pmoailAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoailAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoailAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoailAlmLineOutputPwrHighAlarm=_PmoailAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,6),_PmoailAlmLineOutputPwrHighAlarm_Type())
pmoailAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoailAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoailAlmLineBiasLowAlarm_Object=MibScalar
pmoailAlmLineBiasLowAlarm=_PmoailAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,7),_PmoailAlmLineBiasLowAlarm_Type())
pmoailAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineBiasLowAlarm.setStatus(_A)
_PmoailAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoailAlmLineBiasHighAlarm_Object=MibScalar
pmoailAlmLineBiasHighAlarm=_PmoailAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,36,2,3,2,40,8),_PmoailAlmLineBiasHighAlarm_Type())
pmoailAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineBiasHighAlarm.setStatus(_A)
_PmoailAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoailAlmLineCrit=_PmoailAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,3))
_PmoailAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoailAlmsynthAlm7=_PmoailAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,3,7))
_PmoailAlmLineHwFail_Type=EkiOnOff
_PmoailAlmLineHwFail_Object=MibScalar
pmoailAlmLineHwFail=_PmoailAlmLineHwFail_Object((1,3,6,1,4,1,20044,36,2,3,3,7,4),_PmoailAlmLineHwFail_Type())
pmoailAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineHwFail.setStatus(_A)
_PmoailAlmLineTxOff_Type=EkiOnOff
_PmoailAlmLineTxOff_Object=MibScalar
pmoailAlmLineTxOff=_PmoailAlmLineTxOff_Object((1,3,6,1,4,1,20044,36,2,3,3,7,5),_PmoailAlmLineTxOff_Type())
pmoailAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineTxOff.setStatus(_A)
_PmoailAlmLineDdmWarning_Type=EkiOnOff
_PmoailAlmLineDdmWarning_Object=MibScalar
pmoailAlmLineDdmWarning=_PmoailAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,36,2,3,3,7,9),_PmoailAlmLineDdmWarning_Type())
pmoailAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineDdmWarning.setStatus(_A)
_PmoailAlmLineDdmAlm_Type=EkiOnOff
_PmoailAlmLineDdmAlm_Object=MibScalar
pmoailAlmLineDdmAlm=_PmoailAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,36,2,3,3,7,10),_PmoailAlmLineDdmAlm_Type())
pmoailAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineDdmAlm.setStatus(_A)
_PmoailAlmLineFail_Type=EkiOnOff
_PmoailAlmLineFail_Object=MibScalar
pmoailAlmLineFail=_PmoailAlmLineFail_Object((1,3,6,1,4,1,20044,36,2,3,3,7,12),_PmoailAlmLineFail_Type())
pmoailAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineFail.setStatus(_A)
_PmoailAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoailAlmlineEdfaAlarms2=_PmoailAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,36,2,3,3,43))
_PmoailAlmLineEdfaNr_Type=EkiOnOff
_PmoailAlmLineEdfaNr_Object=MibScalar
pmoailAlmLineEdfaNr=_PmoailAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,36,2,3,3,43,1),_PmoailAlmLineEdfaNr_Type())
pmoailAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineEdfaNr.setStatus(_A)
_PmoailAlmLineEdfaTecFail_Type=EkiOnOff
_PmoailAlmLineEdfaTecFail_Object=MibScalar
pmoailAlmLineEdfaTecFail=_PmoailAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,36,2,3,3,43,2),_PmoailAlmLineEdfaTecFail_Type())
pmoailAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineEdfaTecFail.setStatus(_A)
_PmoailAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoailAlmLineEdfaLaserFail_Object=MibScalar
pmoailAlmLineEdfaLaserFail=_PmoailAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,36,2,3,3,43,3),_PmoailAlmLineEdfaLaserFail_Type())
pmoailAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineEdfaLaserFail.setStatus(_A)
_PmoailAlmLineEdfaLos_Type=EkiOnOff
_PmoailAlmLineEdfaLos_Object=MibScalar
pmoailAlmLineEdfaLos=_PmoailAlmLineEdfaLos_Object((1,3,6,1,4,1,20044,36,2,3,3,43,4),_PmoailAlmLineEdfaLos_Type())
pmoailAlmLineEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineEdfaLos.setStatus(_A)
_PmoailAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoailAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoailAlmLineExtPumpEdfaLowCurrent=_PmoailAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,36,2,3,3,43,5),_PmoailAlmLineExtPumpEdfaLowCurrent_Type())
pmoailAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_Pmoailmeasures_ObjectIdentity=ObjectIdentity
pmoailmeasures=_Pmoailmeasures_ObjectIdentity((1,3,6,1,4,1,20044,36,3))
_PmoailMesrOther_ObjectIdentity=ObjectIdentity
pmoailMesrOther=_PmoailMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,36,3,1))
class _PmoailMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrtempMeas_Type.__name__=_E
_PmoailMesrtempMeas_Object=MibScalar
pmoailMesrtempMeas=_PmoailMesrtempMeas_Object((1,3,6,1,4,1,20044,36,3,1,72),_PmoailMesrtempMeas_Type())
pmoailMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrtempMeas.setStatus(_A)
class _PmoailMesr3v3Meas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesr3v3Meas_Type.__name__=_E
_PmoailMesr3v3Meas_Object=MibScalar
pmoailMesr3v3Meas=_PmoailMesr3v3Meas_Object((1,3,6,1,4,1,20044,36,3,1,73),_PmoailMesr3v3Meas_Type())
pmoailMesr3v3Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesr3v3Meas.setStatus(_A)
_PmoailMesrClient_ObjectIdentity=ObjectIdentity
pmoailMesrClient=_PmoailMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,36,3,2))
class _PmoailMesrclientEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrclientEdfaBiasMeas_Type.__name__=_E
_PmoailMesrclientEdfaBiasMeas_Object=MibScalar
pmoailMesrclientEdfaBiasMeas=_PmoailMesrclientEdfaBiasMeas_Object((1,3,6,1,4,1,20044,36,3,2,32),_PmoailMesrclientEdfaBiasMeas_Type())
pmoailMesrclientEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrclientEdfaBiasMeas.setStatus(_A)
class _PmoailMesrclientEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrclientEdfaTxpwrMeas_Type.__name__=_E
_PmoailMesrclientEdfaTxpwrMeas_Object=MibScalar
pmoailMesrclientEdfaTxpwrMeas=_PmoailMesrclientEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,36,3,2,33),_PmoailMesrclientEdfaTxpwrMeas_Type())
pmoailMesrclientEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrclientEdfaTxpwrMeas.setStatus(_A)
class _PmoailMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrclientEdfaRxpwrMeas_Type.__name__=_E
_PmoailMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoailMesrclientEdfaRxpwrMeas=_PmoailMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,36,3,2,34),_PmoailMesrclientEdfaRxpwrMeas_Type())
pmoailMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrclientEdfaRxpwrMeas.setStatus(_A)
class _PmoailMesrclientEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrclientEdfaGainMeas_Type.__name__=_E
_PmoailMesrclientEdfaGainMeas_Object=MibScalar
pmoailMesrclientEdfaGainMeas=_PmoailMesrclientEdfaGainMeas_Object((1,3,6,1,4,1,20044,36,3,2,35),_PmoailMesrclientEdfaGainMeas_Type())
pmoailMesrclientEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrclientEdfaGainMeas.setStatus(_A)
_PmoailMesrLine_ObjectIdentity=ObjectIdentity
pmoailMesrLine=_PmoailMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,36,3,3))
class _PmoailMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrlineEdfaBiasMeas_Type.__name__=_E
_PmoailMesrlineEdfaBiasMeas_Object=MibScalar
pmoailMesrlineEdfaBiasMeas=_PmoailMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,36,3,3,40),_PmoailMesrlineEdfaBiasMeas_Type())
pmoailMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoailMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrlineEdfaTxpwrMeas_Type.__name__=_E
_PmoailMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoailMesrlineEdfaTxpwrMeas=_PmoailMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,36,3,3,41),_PmoailMesrlineEdfaTxpwrMeas_Type())
pmoailMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoailMesrlineEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrlineEdfaRxpwrMeas_Type.__name__=_E
_PmoailMesrlineEdfaRxpwrMeas_Object=MibScalar
pmoailMesrlineEdfaRxpwrMeas=_PmoailMesrlineEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,36,3,3,42),_PmoailMesrlineEdfaRxpwrMeas_Type())
pmoailMesrlineEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrlineEdfaRxpwrMeas.setStatus(_A)
class _PmoailMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailMesrlineEdfaGainMeas_Type.__name__=_E
_PmoailMesrlineEdfaGainMeas_Object=MibScalar
pmoailMesrlineEdfaGainMeas=_PmoailMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,36,3,3,43),_PmoailMesrlineEdfaGainMeas_Type())
pmoailMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailMesrlineEdfaGainMeas.setStatus(_A)
_PmoailcontrolsWrite_ObjectIdentity=ObjectIdentity
pmoailcontrolsWrite=_PmoailcontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,36,6))
_PmoailCtrlOther_ObjectIdentity=ObjectIdentity
pmoailCtrlOther=_PmoailCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,36,6,1))
_PmoailCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoailCtrlsynth0=_PmoailCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,36,6,1,0))
_PmoailCtrlConfLoad_Type=EkiOnOff
_PmoailCtrlConfLoad_Object=MibScalar
pmoailCtrlConfLoad=_PmoailCtrlConfLoad_Object((1,3,6,1,4,1,20044,36,6,1,0,1),_PmoailCtrlConfLoad_Type())
pmoailCtrlConfLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlConfLoad.setStatus(_A)
_PmoailCtrlConfFlash_Type=EkiOnOff
_PmoailCtrlConfFlash_Object=MibScalar
pmoailCtrlConfFlash=_PmoailCtrlConfFlash_Object((1,3,6,1,4,1,20044,36,6,1,0,9),_PmoailCtrlConfFlash_Type())
pmoailCtrlConfFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlConfFlash.setStatus(_A)
_PmoailCtrlConfClear_Type=EkiOnOff
_PmoailCtrlConfClear_Object=MibScalar
pmoailCtrlConfClear=_PmoailCtrlConfClear_Object((1,3,6,1,4,1,20044,36,6,1,0,13),_PmoailCtrlConfClear_Type())
pmoailCtrlConfClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlConfClear.setStatus(_A)
_PmoailCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoailCtrlswMgnt=_PmoailCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,36,6,1,5))
_PmoailCtrlColdReset_Type=EkiOnOff
_PmoailCtrlColdReset_Object=MibScalar
pmoailCtrlColdReset=_PmoailCtrlColdReset_Object((1,3,6,1,4,1,20044,36,6,1,5,2),_PmoailCtrlColdReset_Type())
pmoailCtrlColdReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlColdReset.setStatus(_A)
_PmoailCtrlWarmReset_Type=EkiOnOff
_PmoailCtrlWarmReset_Object=MibScalar
pmoailCtrlWarmReset=_PmoailCtrlWarmReset_Object((1,3,6,1,4,1,20044,36,6,1,5,3),_PmoailCtrlWarmReset_Type())
pmoailCtrlWarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlWarmReset.setStatus(_A)
_PmoailCtrlpowerDown_ObjectIdentity=ObjectIdentity
pmoailCtrlpowerDown=_PmoailCtrlpowerDown_ObjectIdentity((1,3,6,1,4,1,20044,36,6,1,72))
_PmoailCtrlSoftPowerDown_Type=EkiOnOff
_PmoailCtrlSoftPowerDown_Object=MibScalar
pmoailCtrlSoftPowerDown=_PmoailCtrlSoftPowerDown_Object((1,3,6,1,4,1,20044,36,6,1,72,1),_PmoailCtrlSoftPowerDown_Type())
pmoailCtrlSoftPowerDown.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlSoftPowerDown.setStatus(_A)
_PmoailCtrlledTest_ObjectIdentity=ObjectIdentity
pmoailCtrlledTest=_PmoailCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,36,6,1,73))
_PmoailCtrlGreenLed_Type=EkiOnOff
_PmoailCtrlGreenLed_Object=MibScalar
pmoailCtrlGreenLed=_PmoailCtrlGreenLed_Object((1,3,6,1,4,1,20044,36,6,1,73,1),_PmoailCtrlGreenLed_Type())
pmoailCtrlGreenLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlGreenLed.setStatus(_A)
_PmoailCtrlRedLed_Type=EkiOnOff
_PmoailCtrlRedLed_Object=MibScalar
pmoailCtrlRedLed=_PmoailCtrlRedLed_Object((1,3,6,1,4,1,20044,36,6,1,73,2),_PmoailCtrlRedLed_Type())
pmoailCtrlRedLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlRedLed.setStatus(_A)
_PmoailCtrlLedOff_Type=EkiOnOff
_PmoailCtrlLedOff_Object=MibScalar
pmoailCtrlLedOff=_PmoailCtrlLedOff_Object((1,3,6,1,4,1,20044,36,6,1,73,3),_PmoailCtrlLedOff_Type())
pmoailCtrlLedOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlLedOff.setStatus(_A)
_PmoailCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoailCtrlmaintMode=_PmoailCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,36,6,1,75))
_PmoailCtrlMaintenance_Type=EkiOnOff
_PmoailCtrlMaintenance_Object=MibScalar
pmoailCtrlMaintenance=_PmoailCtrlMaintenance_Object((1,3,6,1,4,1,20044,36,6,1,75,1),_PmoailCtrlMaintenance_Type())
pmoailCtrlMaintenance.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlMaintenance.setStatus(_A)
_PmoailCtrlClient_ObjectIdentity=ObjectIdentity
pmoailCtrlClient=_PmoailCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,36,6,2))
_PmoailCtrlclientEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoailCtrlclientEdfaLaserOff=_PmoailCtrlclientEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,36,6,2,32))
_PmoailCtrlClientEdfaLaserOff_Type=EkiOnOff
_PmoailCtrlClientEdfaLaserOff_Object=MibScalar
pmoailCtrlClientEdfaLaserOff=_PmoailCtrlClientEdfaLaserOff_Object((1,3,6,1,4,1,20044,36,6,2,32,1),_PmoailCtrlClientEdfaLaserOff_Type())
pmoailCtrlClientEdfaLaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlClientEdfaLaserOff.setStatus(_A)
_PmoailCtrlclientEdfaMode_Type=PmoailpreampMode
_PmoailCtrlclientEdfaMode_Object=MibScalar
pmoailCtrlclientEdfaMode=_PmoailCtrlclientEdfaMode_Object((1,3,6,1,4,1,20044,36,6,2,33),_PmoailCtrlclientEdfaMode_Type())
pmoailCtrlclientEdfaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlclientEdfaMode.setStatus(_A)
class _PmoailCtrlclientIlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrlclientIlasSettingValue_Type.__name__=_E
_PmoailCtrlclientIlasSettingValue_Object=MibScalar
pmoailCtrlclientIlasSettingValue=_PmoailCtrlclientIlasSettingValue_Object((1,3,6,1,4,1,20044,36,6,2,34),_PmoailCtrlclientIlasSettingValue_Type())
pmoailCtrlclientIlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlclientIlasSettingValue.setStatus(_A)
class _PmoailCtrlclientPlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrlclientPlasSettingValue_Type.__name__=_E
_PmoailCtrlclientPlasSettingValue_Object=MibScalar
pmoailCtrlclientPlasSettingValue=_PmoailCtrlclientPlasSettingValue_Object((1,3,6,1,4,1,20044,36,6,2,35),_PmoailCtrlclientPlasSettingValue_Type())
pmoailCtrlclientPlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlclientPlasSettingValue.setStatus(_A)
class _PmoailCtrlclientGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrlclientGainSettingValue_Type.__name__=_E
_PmoailCtrlclientGainSettingValue_Object=MibScalar
pmoailCtrlclientGainSettingValue=_PmoailCtrlclientGainSettingValue_Object((1,3,6,1,4,1,20044,36,6,2,36),_PmoailCtrlclientGainSettingValue_Type())
pmoailCtrlclientGainSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlclientGainSettingValue.setStatus(_A)
class _PmoailCtrlclientEffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrlclientEffPwrOutSettingValue_Type.__name__=_E
_PmoailCtrlclientEffPwrOutSettingValue_Object=MibScalar
pmoailCtrlclientEffPwrOutSettingValue=_PmoailCtrlclientEffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,36,6,2,37),_PmoailCtrlclientEffPwrOutSettingValue_Type())
pmoailCtrlclientEffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlclientEffPwrOutSettingValue.setStatus(_A)
_PmoailCtrlLine_ObjectIdentity=ObjectIdentity
pmoailCtrlLine=_PmoailCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,36,6,3))
_PmoailCtrllineEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoailCtrllineEdfaLaserOff=_PmoailCtrllineEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,36,6,3,40))
_PmoailCtrlLineEdfaLaserOff_Type=EkiOnOff
_PmoailCtrlLineEdfaLaserOff_Object=MibScalar
pmoailCtrlLineEdfaLaserOff=_PmoailCtrlLineEdfaLaserOff_Object((1,3,6,1,4,1,20044,36,6,3,40,1),_PmoailCtrlLineEdfaLaserOff_Type())
pmoailCtrlLineEdfaLaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrlLineEdfaLaserOff.setStatus(_A)
_PmoailCtrllineEdfaMode_Type=PmoailboosterMode
_PmoailCtrllineEdfaMode_Object=MibScalar
pmoailCtrllineEdfaMode=_PmoailCtrllineEdfaMode_Object((1,3,6,1,4,1,20044,36,6,3,41),_PmoailCtrllineEdfaMode_Type())
pmoailCtrllineEdfaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrllineEdfaMode.setStatus(_A)
class _PmoailCtrllineIlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrllineIlasSettingValue_Type.__name__=_E
_PmoailCtrllineIlasSettingValue_Object=MibScalar
pmoailCtrllineIlasSettingValue=_PmoailCtrllineIlasSettingValue_Object((1,3,6,1,4,1,20044,36,6,3,42),_PmoailCtrllineIlasSettingValue_Type())
pmoailCtrllineIlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrllineIlasSettingValue.setStatus(_A)
class _PmoailCtrllinePlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrllinePlasSettingValue_Type.__name__=_E
_PmoailCtrllinePlasSettingValue_Object=MibScalar
pmoailCtrllinePlasSettingValue=_PmoailCtrllinePlasSettingValue_Object((1,3,6,1,4,1,20044,36,6,3,43),_PmoailCtrllinePlasSettingValue_Type())
pmoailCtrllinePlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrllinePlasSettingValue.setStatus(_A)
class _PmoailCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrllineGainSettingValue_Type.__name__=_E
_PmoailCtrllineGainSettingValue_Object=MibScalar
pmoailCtrllineGainSettingValue=_PmoailCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,36,6,3,44),_PmoailCtrllineGainSettingValue_Type())
pmoailCtrllineGainSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrllineGainSettingValue.setStatus(_A)
class _PmoailCtrllineEffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailCtrllineEffPwrOutSettingValue_Type.__name__=_E
_PmoailCtrllineEffPwrOutSettingValue_Object=MibScalar
pmoailCtrllineEffPwrOutSettingValue=_PmoailCtrllineEffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,36,6,3,45),_PmoailCtrllineEffPwrOutSettingValue_Type())
pmoailCtrllineEffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCtrllineEffPwrOutSettingValue.setStatus(_A)
_Pmoailri_ObjectIdentity=ObjectIdentity
pmoailri=_Pmoailri_ObjectIdentity((1,3,6,1,4,1,20044,36,7))
_PmoailRinvReloadInventory_Type=EkiOnOff
_PmoailRinvReloadInventory_Object=MibScalar
pmoailRinvReloadInventory=_PmoailRinvReloadInventory_Object((1,3,6,1,4,1,20044,36,7,2),_PmoailRinvReloadInventory_Type())
pmoailRinvReloadInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailRinvReloadInventory.setStatus(_A)
_PmoailRinvModulePlatform_Type=DisplayString
_PmoailRinvModulePlatform_Object=MibScalar
pmoailRinvModulePlatform=_PmoailRinvModulePlatform_Object((1,3,6,1,4,1,20044,36,7,3),_PmoailRinvModulePlatform_Type())
pmoailRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvModulePlatform.setStatus(_A)
_PmoailRinvSwPlatform_Type=DisplayString
_PmoailRinvSwPlatform_Object=MibScalar
pmoailRinvSwPlatform=_PmoailRinvSwPlatform_Object((1,3,6,1,4,1,20044,36,7,4),_PmoailRinvSwPlatform_Type())
pmoailRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvSwPlatform.setStatus(_A)
_PmoailRinvSwFoa_Type=DisplayString
_PmoailRinvSwFoa_Object=MibScalar
pmoailRinvSwFoa=_PmoailRinvSwFoa_Object((1,3,6,1,4,1,20044,36,7,5),_PmoailRinvSwFoa_Type())
pmoailRinvSwFoa.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvSwFoa.setStatus(_A)
_PmoailRinvInLine1Table_Object=MibTable
pmoailRinvInLine1Table=_PmoailRinvInLine1Table_Object((1,3,6,1,4,1,20044,36,7,6))
if mibBuilder.loadTexts:pmoailRinvInLine1Table.setStatus(_A)
_PmoailRinvInLine1Entry_Object=MibTableRow
pmoailRinvInLine1Entry=_PmoailRinvInLine1Entry_Object((1,3,6,1,4,1,20044,36,7,6,1))
pmoailRinvInLine1Entry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:pmoailRinvInLine1Entry.setStatus(_A)
class _PmoailRinvInLine1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoailRinvInLine1Index_Type.__name__=_E
_PmoailRinvInLine1Index_Object=MibTableColumn
pmoailRinvInLine1Index=_PmoailRinvInLine1Index_Object((1,3,6,1,4,1,20044,36,7,6,1,1),_PmoailRinvInLine1Index_Type())
pmoailRinvInLine1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvInLine1Index.setStatus(_A)
_PmoailRinvInLine1_Type=DisplayString
_PmoailRinvInLine1_Object=MibTableColumn
pmoailRinvInLine1=_PmoailRinvInLine1_Object((1,3,6,1,4,1,20044,36,7,6,1,2),_PmoailRinvInLine1_Type())
pmoailRinvInLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvInLine1.setStatus(_A)
_PmoailRinvInLine2Table_Object=MibTable
pmoailRinvInLine2Table=_PmoailRinvInLine2Table_Object((1,3,6,1,4,1,20044,36,7,7))
if mibBuilder.loadTexts:pmoailRinvInLine2Table.setStatus(_A)
_PmoailRinvInLine2Entry_Object=MibTableRow
pmoailRinvInLine2Entry=_PmoailRinvInLine2Entry_Object((1,3,6,1,4,1,20044,36,7,7,1))
pmoailRinvInLine2Entry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:pmoailRinvInLine2Entry.setStatus(_A)
class _PmoailRinvInLine2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoailRinvInLine2Index_Type.__name__=_E
_PmoailRinvInLine2Index_Object=MibTableColumn
pmoailRinvInLine2Index=_PmoailRinvInLine2Index_Object((1,3,6,1,4,1,20044,36,7,7,1,1),_PmoailRinvInLine2Index_Type())
pmoailRinvInLine2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvInLine2Index.setStatus(_A)
_PmoailRinvInLine2_Type=DisplayString
_PmoailRinvInLine2_Object=MibTableColumn
pmoailRinvInLine2=_PmoailRinvInLine2_Object((1,3,6,1,4,1,20044,36,7,7,1,2),_PmoailRinvInLine2_Type())
pmoailRinvInLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailRinvInLine2.setStatus(_A)
_PmoailConfig_ObjectIdentity=ObjectIdentity
pmoailConfig=_PmoailConfig_ObjectIdentity((1,3,6,1,4,1,20044,36,9))
_PmoailCfgNoValue_ObjectIdentity=ObjectIdentity
pmoailCfgNoValue=_PmoailCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,36,9,1))
_PmoailtableclientStartup_ObjectIdentity=ObjectIdentity
pmoailtableclientStartup=_PmoailtableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,36,9,1,1))
class _PmoailCfgclientEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailCfgclientEdfaLaserCtrl_Type.__name__=_G
_PmoailCfgclientEdfaLaserCtrl_Object=MibScalar
pmoailCfgclientEdfaLaserCtrl=_PmoailCfgclientEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,36,9,1,1,2),_PmoailCfgclientEdfaLaserCtrl_Type())
pmoailCfgclientEdfaLaserCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfgclientEdfaLaserCtrl.setStatus(_A)
class _PmoailCfgclientEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailCfgclientEdfaLaserMode_Type.__name__=_G
_PmoailCfgclientEdfaLaserMode_Object=MibScalar
pmoailCfgclientEdfaLaserMode=_PmoailCfgclientEdfaLaserMode_Object((1,3,6,1,4,1,20044,36,9,1,1,3),_PmoailCfgclientEdfaLaserMode_Type())
pmoailCfgclientEdfaLaserMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfgclientEdfaLaserMode.setStatus(_A)
_PmoailCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoailCfgLineStartUp=_PmoailCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,36,9,2))
_PmoailtablelineStartup_ObjectIdentity=ObjectIdentity
pmoailtablelineStartup=_PmoailtablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,36,9,2,1))
class _PmoailCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailCfglineEdfaLaserCtrl_Type.__name__=_G
_PmoailCfglineEdfaLaserCtrl_Object=MibScalar
pmoailCfglineEdfaLaserCtrl=_PmoailCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,36,9,2,1,2),_PmoailCfglineEdfaLaserCtrl_Type())
pmoailCfglineEdfaLaserCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoailCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailCfglineEdfaLaserMode_Type.__name__=_G
_PmoailCfglineEdfaLaserMode_Object=MibScalar
pmoailCfglineEdfaLaserMode=_PmoailCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,36,9,2,1,3),_PmoailCfglineEdfaLaserMode_Type())
pmoailCfglineEdfaLaserMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfglineEdfaLaserMode.setStatus(_A)
_PmoailCfgLabels_ObjectIdentity=ObjectIdentity
pmoailCfgLabels=_PmoailCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,36,9,3))
_PmoailCfgLabelclientTable_Object=MibTable
pmoailCfgLabelclientTable=_PmoailCfgLabelclientTable_Object((1,3,6,1,4,1,20044,36,9,3,1))
if mibBuilder.loadTexts:pmoailCfgLabelclientTable.setStatus(_A)
_PmoailCfgLabelclientEntry_Object=MibTableRow
pmoailCfgLabelclientEntry=_PmoailCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,36,9,3,1,1))
pmoailCfgLabelclientEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pmoailCfgLabelclientEntry.setStatus(_A)
class _PmoailCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailCfgLabelclientIndex_Type.__name__=_E
_PmoailCfgLabelclientIndex_Object=MibTableColumn
pmoailCfgLabelclientIndex=_PmoailCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,36,9,3,1,1,1),_PmoailCfgLabelclientIndex_Type())
pmoailCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailCfgLabelclientIndex.setStatus(_A)
class _PmoailCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoailCfgLabelclientPortn_Type.__name__=_H
_PmoailCfgLabelclientPortn_Object=MibTableColumn
pmoailCfgLabelclientPortn=_PmoailCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,36,9,3,1,1,3),_PmoailCfgLabelclientPortn_Type())
pmoailCfgLabelclientPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfgLabelclientPortn.setStatus(_A)
_PmoailCfgLabellineTable_Object=MibTable
pmoailCfgLabellineTable=_PmoailCfgLabellineTable_Object((1,3,6,1,4,1,20044,36,9,3,2))
if mibBuilder.loadTexts:pmoailCfgLabellineTable.setStatus(_A)
_PmoailCfgLabellineEntry_Object=MibTableRow
pmoailCfgLabellineEntry=_PmoailCfgLabellineEntry_Object((1,3,6,1,4,1,20044,36,9,3,2,1))
pmoailCfgLabellineEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pmoailCfgLabellineEntry.setStatus(_A)
class _PmoailCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailCfgLabellineIndex_Type.__name__=_E
_PmoailCfgLabellineIndex_Object=MibTableColumn
pmoailCfgLabellineIndex=_PmoailCfgLabellineIndex_Object((1,3,6,1,4,1,20044,36,9,3,2,1,1),_PmoailCfgLabellineIndex_Type())
pmoailCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailCfgLabellineIndex.setStatus(_A)
class _PmoailCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoailCfgLabellinePortn_Type.__name__=_H
_PmoailCfgLabellinePortn_Object=MibTableColumn
pmoailCfgLabellinePortn=_PmoailCfgLabellinePortn_Object((1,3,6,1,4,1,20044,36,9,3,2,1,3),_PmoailCfgLabellinePortn_Type())
pmoailCfgLabellinePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfgLabellinePortn.setStatus(_A)
_PmoailCfgWriteConfiguration_Type=EkiOnOff
_PmoailCfgWriteConfiguration_Object=MibScalar
pmoailCfgWriteConfiguration=_PmoailCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,36,9,257),_PmoailCfgWriteConfiguration_Type())
pmoailCfgWriteConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoailCfgWriteConfiguration.setStatus(_A)
_Pmoailtraps_ObjectIdentity=ObjectIdentity
pmoailtraps=_Pmoailtraps_ObjectIdentity((1,3,6,1,4,1,20044,36,10))
class _PmoailtrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoailtrapBoardNumber_Type.__name__=_E
_PmoailtrapBoardNumber_Object=MibScalar
pmoailtrapBoardNumber=_PmoailtrapBoardNumber_Object((1,3,6,1,4,1,20044,36,10,4),_PmoailtrapBoardNumber_Type())
pmoailtrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailtrapBoardNumber.setStatus(_A)
pmoailLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,30))
pmoailLineTrapNotUrgentGoesOn.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmoailLineTrapNotUrgentGoesOn.setStatus(_A)
pmoailLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,31))
pmoailLineTrapNotUrgentGoesOff.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmoailLineTrapNotUrgentGoesOff.setStatus(_A)
pmoailLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,32))
pmoailLineTrapUrgentGoesOn.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmoailLineTrapUrgentGoesOn.setStatus(_A)
pmoailLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,33))
pmoailLineTrapUrgentGoesOff.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmoailLineTrapUrgentGoesOff.setStatus(_A)
pmoailLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,34))
pmoailLineTrapCritGoesOn.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmoailLineTrapCritGoesOn.setStatus(_A)
pmoailLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,35))
pmoailLineTrapCritGoesOff.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmoailLineTrapCritGoesOff.setStatus(_A)
pmoailClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,40))
pmoailClientTrapNotUrgentGoesOn.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmoailClientTrapNotUrgentGoesOn.setStatus(_A)
pmoailClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,41))
pmoailClientTrapNotUrgentGoesOff.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmoailClientTrapNotUrgentGoesOff.setStatus(_A)
pmoailClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,42))
pmoailClientTrapUrgentGoesOn.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmoailClientTrapUrgentGoesOn.setStatus(_A)
pmoailClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,43))
pmoailClientTrapUrgentGoesOff.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmoailClientTrapUrgentGoesOff.setStatus(_A)
pmoailClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,44))
pmoailClientTrapCritGoesOn.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmoailClientTrapCritGoesOn.setStatus(_A)
pmoailClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,45))
pmoailClientTrapCritGoesOff.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmoailClientTrapCritGoesOff.setStatus(_A)
pmoailPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,36,10,50))
pmoailPowerTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmoailPowerTrapUrgentGoesOn.setStatus(_A)
pmoailPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,36,10,51))
pmoailPowerTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmoailPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PmoailpreampMode':PmoailpreampMode,'PmoailboosterMode':PmoailboosterMode,'modulepmoail':modulepmoail,'pmoailalarms':pmoailalarms,'pmoailAlmOther':pmoailAlmOther,'pmoailAlmOtherNurg':pmoailAlmOtherNurg,'pmoailAlmsynthAlm2':pmoailAlmsynthAlm2,'pmoailAlmConfTableSave':pmoailAlmConfTableSave,'pmoailAlmInvUpload':pmoailAlmInvUpload,'pmoailAlmConfTableLoad':pmoailAlmConfTableLoad,'pmoailAlmfoaWarnings':pmoailAlmfoaWarnings,'pmoailAlm3v3LowWarning':pmoailAlm3v3LowWarning,'pmoailAlm3v3HighWarning':pmoailAlm3v3HighWarning,'pmoailAlmTermpLowWarning':pmoailAlmTermpLowWarning,'pmoailAlmTempHighWarning':pmoailAlmTempHighWarning,'pmoailAlmOtherUrg':pmoailAlmOtherUrg,'pmoailAlmfoaAlarms':pmoailAlmfoaAlarms,'pmoailAlm3v3LowAlarm':pmoailAlm3v3LowAlarm,'pmoailAlm3v3HighAlarm':pmoailAlm3v3HighAlarm,'pmoailAlmTermpLowAlarm':pmoailAlmTermpLowAlarm,'pmoailAlmTempHighAlarm':pmoailAlmTempHighAlarm,'pmoailAlmOtherCrit':pmoailAlmOtherCrit,'pmoailAlmsynthAlm0':pmoailAlmsynthAlm0,'pmoailAlmMaintenanceMode':pmoailAlmMaintenanceMode,'pmoailAlmModGlobFail':pmoailAlmModGlobFail,'pmoailAlmUpEdfaInitNotCompl':pmoailAlmUpEdfaInitNotCompl,'pmoailAlmDwEdfaInitNotCompl':pmoailAlmDwEdfaInitNotCompl,'pmoailAlmExtPumpNotLocked':pmoailAlmExtPumpNotLocked,_R:pmoailAlmDefFuseA,_Q:pmoailAlmDefFuseB,'pmoailAlmClient':pmoailAlmClient,'pmoailAlmClientNurg':pmoailAlmClientNurg,'pmoailAlmclientEdfaWarnings':pmoailAlmclientEdfaWarnings,'pmoailAlmClientGainLowWarning':pmoailAlmClientGainLowWarning,'pmoailAlmClientGainHighWarning':pmoailAlmClientGainHighWarning,'pmoailAlmClientInputPwrLowWarning':pmoailAlmClientInputPwrLowWarning,'pmoailAlmClientInputPwrHighWarning':pmoailAlmClientInputPwrHighWarning,'pmoailAlmClientOutputPwrLowWarning':pmoailAlmClientOutputPwrLowWarning,'pmoailAlmClientOutputPwrHighWarning':pmoailAlmClientOutputPwrHighWarning,'pmoailAlmClientBiasLowWarning':pmoailAlmClientBiasLowWarning,'pmoailAlmClientBiasHighWarning':pmoailAlmClientBiasHighWarning,'pmoailAlmClientUrg':pmoailAlmClientUrg,'pmoailAlmclientEdfaAlarms1':pmoailAlmclientEdfaAlarms1,'pmoailAlmClientGainLowAlarm':pmoailAlmClientGainLowAlarm,'pmoailAlmClientGainHighAlarm':pmoailAlmClientGainHighAlarm,'pmoailAlmClientInputPwrLowAlarm':pmoailAlmClientInputPwrLowAlarm,'pmoailAlmClientInputPwrHighAlarm':pmoailAlmClientInputPwrHighAlarm,'pmoailAlmClientOutputPwrLowAlarm':pmoailAlmClientOutputPwrLowAlarm,'pmoailAlmClientOutputPwrHighAlarm':pmoailAlmClientOutputPwrHighAlarm,'pmoailAlmClientBiasLowAlarm':pmoailAlmClientBiasLowAlarm,'pmoailAlmClientBiasHighAlarm':pmoailAlmClientBiasHighAlarm,'pmoailAlmClientCrit':pmoailAlmClientCrit,'pmoailAlmsynthAlm8':pmoailAlmsynthAlm8,_P:pmoailAlmClientHwFail,'pmoailAlmClientTxOff':pmoailAlmClientTxOff,_M:pmoailAlmClientDdmWarning,_N:pmoailAlmClientDdmAlm,_O:pmoailAlmClientFail,'pmoailAlmclientEdfaAlarms2':pmoailAlmclientEdfaAlarms2,'pmoailAlmClientEdfaNr':pmoailAlmClientEdfaNr,'pmoailAlmClientEdfaTecFail':pmoailAlmClientEdfaTecFail,'pmoailAlmClientEdfaLaserFail':pmoailAlmClientEdfaLaserFail,'pmoailAlmClientEdfaLos':pmoailAlmClientEdfaLos,'pmoailAlmClientExtPumpEdfaLowCurrent':pmoailAlmClientExtPumpEdfaLowCurrent,'pmoailAlmLine':pmoailAlmLine,'pmoailAlmLineNurg':pmoailAlmLineNurg,'pmoailAlmlineEdfaWarnings':pmoailAlmlineEdfaWarnings,'pmoailAlmLineGainLowWarning':pmoailAlmLineGainLowWarning,'pmoailAlmLineGainHighWarning':pmoailAlmLineGainHighWarning,'pmoailAlmLineInputPwrLowWarning':pmoailAlmLineInputPwrLowWarning,'pmoailAlmLineInputPwrHighWarning':pmoailAlmLineInputPwrHighWarning,'pmoailAlmLineOutputPwrLowWarning':pmoailAlmLineOutputPwrLowWarning,'pmoailAlmLineOutputPwrHighWarning':pmoailAlmLineOutputPwrHighWarning,'pmoailAlmLineBiasLowWarning':pmoailAlmLineBiasLowWarning,'pmoailAlmLineBiasHighWarning':pmoailAlmLineBiasHighWarning,'pmoailAlmLineUrg':pmoailAlmLineUrg,'pmoailAlmlineEdfaAlarms1':pmoailAlmlineEdfaAlarms1,'pmoailAlmLineGainLowAlarm':pmoailAlmLineGainLowAlarm,'pmoailAlmLineGainHighAlarm':pmoailAlmLineGainHighAlarm,'pmoailAlmLineInputPwrLowAlarm':pmoailAlmLineInputPwrLowAlarm,'pmoailAlmLineInputPwrHighAlarm':pmoailAlmLineInputPwrHighAlarm,'pmoailAlmLineOutputPwrLowAlarm':pmoailAlmLineOutputPwrLowAlarm,'pmoailAlmLineOutputPwrHighAlarm':pmoailAlmLineOutputPwrHighAlarm,'pmoailAlmLineBiasLowAlarm':pmoailAlmLineBiasLowAlarm,'pmoailAlmLineBiasHighAlarm':pmoailAlmLineBiasHighAlarm,'pmoailAlmLineCrit':pmoailAlmLineCrit,'pmoailAlmsynthAlm7':pmoailAlmsynthAlm7,_L:pmoailAlmLineHwFail,'pmoailAlmLineTxOff':pmoailAlmLineTxOff,_I:pmoailAlmLineDdmWarning,_J:pmoailAlmLineDdmAlm,_K:pmoailAlmLineFail,'pmoailAlmlineEdfaAlarms2':pmoailAlmlineEdfaAlarms2,'pmoailAlmLineEdfaNr':pmoailAlmLineEdfaNr,'pmoailAlmLineEdfaTecFail':pmoailAlmLineEdfaTecFail,'pmoailAlmLineEdfaLaserFail':pmoailAlmLineEdfaLaserFail,'pmoailAlmLineEdfaLos':pmoailAlmLineEdfaLos,'pmoailAlmLineExtPumpEdfaLowCurrent':pmoailAlmLineExtPumpEdfaLowCurrent,'pmoailmeasures':pmoailmeasures,'pmoailMesrOther':pmoailMesrOther,'pmoailMesrtempMeas':pmoailMesrtempMeas,'pmoailMesr3v3Meas':pmoailMesr3v3Meas,'pmoailMesrClient':pmoailMesrClient,'pmoailMesrclientEdfaBiasMeas':pmoailMesrclientEdfaBiasMeas,'pmoailMesrclientEdfaTxpwrMeas':pmoailMesrclientEdfaTxpwrMeas,'pmoailMesrclientEdfaRxpwrMeas':pmoailMesrclientEdfaRxpwrMeas,'pmoailMesrclientEdfaGainMeas':pmoailMesrclientEdfaGainMeas,'pmoailMesrLine':pmoailMesrLine,'pmoailMesrlineEdfaBiasMeas':pmoailMesrlineEdfaBiasMeas,'pmoailMesrlineEdfaTxpwrMeas':pmoailMesrlineEdfaTxpwrMeas,'pmoailMesrlineEdfaRxpwrMeas':pmoailMesrlineEdfaRxpwrMeas,'pmoailMesrlineEdfaGainMeas':pmoailMesrlineEdfaGainMeas,'pmoailcontrolsWrite':pmoailcontrolsWrite,'pmoailCtrlOther':pmoailCtrlOther,'pmoailCtrlsynth0':pmoailCtrlsynth0,'pmoailCtrlConfLoad':pmoailCtrlConfLoad,'pmoailCtrlConfFlash':pmoailCtrlConfFlash,'pmoailCtrlConfClear':pmoailCtrlConfClear,'pmoailCtrlswMgnt':pmoailCtrlswMgnt,'pmoailCtrlColdReset':pmoailCtrlColdReset,'pmoailCtrlWarmReset':pmoailCtrlWarmReset,'pmoailCtrlpowerDown':pmoailCtrlpowerDown,'pmoailCtrlSoftPowerDown':pmoailCtrlSoftPowerDown,'pmoailCtrlledTest':pmoailCtrlledTest,'pmoailCtrlGreenLed':pmoailCtrlGreenLed,'pmoailCtrlRedLed':pmoailCtrlRedLed,'pmoailCtrlLedOff':pmoailCtrlLedOff,'pmoailCtrlmaintMode':pmoailCtrlmaintMode,'pmoailCtrlMaintenance':pmoailCtrlMaintenance,'pmoailCtrlClient':pmoailCtrlClient,'pmoailCtrlclientEdfaLaserOff':pmoailCtrlclientEdfaLaserOff,'pmoailCtrlClientEdfaLaserOff':pmoailCtrlClientEdfaLaserOff,'pmoailCtrlclientEdfaMode':pmoailCtrlclientEdfaMode,'pmoailCtrlclientIlasSettingValue':pmoailCtrlclientIlasSettingValue,'pmoailCtrlclientPlasSettingValue':pmoailCtrlclientPlasSettingValue,'pmoailCtrlclientGainSettingValue':pmoailCtrlclientGainSettingValue,'pmoailCtrlclientEffPwrOutSettingValue':pmoailCtrlclientEffPwrOutSettingValue,'pmoailCtrlLine':pmoailCtrlLine,'pmoailCtrllineEdfaLaserOff':pmoailCtrllineEdfaLaserOff,'pmoailCtrlLineEdfaLaserOff':pmoailCtrlLineEdfaLaserOff,'pmoailCtrllineEdfaMode':pmoailCtrllineEdfaMode,'pmoailCtrllineIlasSettingValue':pmoailCtrllineIlasSettingValue,'pmoailCtrllinePlasSettingValue':pmoailCtrllinePlasSettingValue,'pmoailCtrllineGainSettingValue':pmoailCtrllineGainSettingValue,'pmoailCtrllineEffPwrOutSettingValue':pmoailCtrllineEffPwrOutSettingValue,'pmoailri':pmoailri,'pmoailRinvReloadInventory':pmoailRinvReloadInventory,'pmoailRinvModulePlatform':pmoailRinvModulePlatform,'pmoailRinvSwPlatform':pmoailRinvSwPlatform,'pmoailRinvSwFoa':pmoailRinvSwFoa,'pmoailRinvInLine1Table':pmoailRinvInLine1Table,'pmoailRinvInLine1Entry':pmoailRinvInLine1Entry,_S:pmoailRinvInLine1Index,'pmoailRinvInLine1':pmoailRinvInLine1,'pmoailRinvInLine2Table':pmoailRinvInLine2Table,'pmoailRinvInLine2Entry':pmoailRinvInLine2Entry,_T:pmoailRinvInLine2Index,'pmoailRinvInLine2':pmoailRinvInLine2,'pmoailConfig':pmoailConfig,'pmoailCfgNoValue':pmoailCfgNoValue,'pmoailtableclientStartup':pmoailtableclientStartup,'pmoailCfgclientEdfaLaserCtrl':pmoailCfgclientEdfaLaserCtrl,'pmoailCfgclientEdfaLaserMode':pmoailCfgclientEdfaLaserMode,'pmoailCfgLineStartUp':pmoailCfgLineStartUp,'pmoailtablelineStartup':pmoailtablelineStartup,'pmoailCfglineEdfaLaserCtrl':pmoailCfglineEdfaLaserCtrl,'pmoailCfglineEdfaLaserMode':pmoailCfglineEdfaLaserMode,'pmoailCfgLabels':pmoailCfgLabels,'pmoailCfgLabelclientTable':pmoailCfgLabelclientTable,'pmoailCfgLabelclientEntry':pmoailCfgLabelclientEntry,_U:pmoailCfgLabelclientIndex,'pmoailCfgLabelclientPortn':pmoailCfgLabelclientPortn,'pmoailCfgLabellineTable':pmoailCfgLabellineTable,'pmoailCfgLabellineEntry':pmoailCfgLabellineEntry,_V:pmoailCfgLabellineIndex,'pmoailCfgLabellinePortn':pmoailCfgLabellinePortn,'pmoailCfgWriteConfiguration':pmoailCfgWriteConfiguration,'pmoailtraps':pmoailtraps,_F:pmoailtrapBoardNumber,'pmoailLineTrapNotUrgentGoesOn':pmoailLineTrapNotUrgentGoesOn,'pmoailLineTrapNotUrgentGoesOff':pmoailLineTrapNotUrgentGoesOff,'pmoailLineTrapUrgentGoesOn':pmoailLineTrapUrgentGoesOn,'pmoailLineTrapUrgentGoesOff':pmoailLineTrapUrgentGoesOff,'pmoailLineTrapCritGoesOn':pmoailLineTrapCritGoesOn,'pmoailLineTrapCritGoesOff':pmoailLineTrapCritGoesOff,'pmoailClientTrapNotUrgentGoesOn':pmoailClientTrapNotUrgentGoesOn,'pmoailClientTrapNotUrgentGoesOff':pmoailClientTrapNotUrgentGoesOff,'pmoailClientTrapUrgentGoesOn':pmoailClientTrapUrgentGoesOn,'pmoailClientTrapUrgentGoesOff':pmoailClientTrapUrgentGoesOff,'pmoailClientTrapCritGoesOn':pmoailClientTrapCritGoesOn,'pmoailClientTrapCritGoesOff':pmoailClientTrapCritGoesOff,'pmoailPowerTrapUrgentGoesOn':pmoailPowerTrapUrgentGoesOn,'pmoailPowerTrapUrgentGoesOff':pmoailPowerTrapUrgentGoesOff})