_V='pmoaCfgLabellineIndex'
_U='pmoaCfgLabelclientIndex'
_T='pmoaRinvPreAmpIndex'
_S='pmoaRinvBoosterIndex'
_R='pmoaAlmDefFuseA'
_Q='pmoaAlmDefFuseB'
_P='pmoaAlmClientHwFail'
_O='pmoaAlmClientFail'
_N='pmoaAlmClientDdmAlm'
_M='pmoaAlmClientDdmWarning'
_L='pmoaAlmLineHwFail'
_K='pmoaAlmLineFail'
_J='pmoaAlmLineDdmAlm'
_I='pmoaAlmLineDdmWarning'
_H='DisplayString'
_G='Unsigned32'
_F='pmoatrapBoardNumber'
_E='Integer32'
_D='read-write'
_C='EKINOPS-PmOa-MIB'
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
modulepmoa=ModuleIdentity((1,3,6,1,4,1,20044,9))
if mibBuilder.loadTexts:modulepmoa.setRevisions(('2006-01-05 00:00','2007-11-21 00:00','2009-02-05 00:00','2009-04-08 00:00','2009-09-14 00:00','2009-12-14 00:00','2010-02-24 00:00','2010-07-15 00:00','2010-10-29 00:00','2010-11-03 00:00','2012-07-04 00:00','2012-10-05 00:00','2014-03-26 00:00','2014-11-24 00:00','2016-05-23 00:00'))
class PmoapreampMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oapreampdefaultmode',0),('oapreampconstantcurrentmode',1),('oapreampconstantpowermode',2)))
class PmoaboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oaboosterdefaultmode',0),('oaboosterconstantcurrentmode',1),('oaboosterconstantpowermode',2)))
_Pmoaalarms_ObjectIdentity=ObjectIdentity
pmoaalarms=_Pmoaalarms_ObjectIdentity((1,3,6,1,4,1,20044,9,2))
_PmoaAlmOther_ObjectIdentity=ObjectIdentity
pmoaAlmOther=_PmoaAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1))
_PmoaAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoaAlmOtherNurg=_PmoaAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,1))
_PmoaAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoaAlmsynthAlm2=_PmoaAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,1,2))
_PmoaAlmConfTableSave_Type=EkiOnOff
_PmoaAlmConfTableSave_Object=MibScalar
pmoaAlmConfTableSave=_PmoaAlmConfTableSave_Object((1,3,6,1,4,1,20044,9,2,1,1,2,1),_PmoaAlmConfTableSave_Type())
pmoaAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmConfTableSave.setStatus(_A)
_PmoaAlmInvUpload_Type=EkiOnOff
_PmoaAlmInvUpload_Object=MibScalar
pmoaAlmInvUpload=_PmoaAlmInvUpload_Object((1,3,6,1,4,1,20044,9,2,1,1,2,2),_PmoaAlmInvUpload_Type())
pmoaAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmInvUpload.setStatus(_A)
_PmoaAlmConfTableLoad_Type=EkiOnOff
_PmoaAlmConfTableLoad_Object=MibScalar
pmoaAlmConfTableLoad=_PmoaAlmConfTableLoad_Object((1,3,6,1,4,1,20044,9,2,1,1,2,3),_PmoaAlmConfTableLoad_Type())
pmoaAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmConfTableLoad.setStatus(_A)
_PmoaAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoaAlmfoaWarnings=_PmoaAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,1,75))
_PmoaAlm3v3LowWarning_Type=EkiOnOff
_PmoaAlm3v3LowWarning_Object=MibScalar
pmoaAlm3v3LowWarning=_PmoaAlm3v3LowWarning_Object((1,3,6,1,4,1,20044,9,2,1,1,75,5),_PmoaAlm3v3LowWarning_Type())
pmoaAlm3v3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlm3v3LowWarning.setStatus(_A)
_PmoaAlm3v3HighWarning_Type=EkiOnOff
_PmoaAlm3v3HighWarning_Object=MibScalar
pmoaAlm3v3HighWarning=_PmoaAlm3v3HighWarning_Object((1,3,6,1,4,1,20044,9,2,1,1,75,6),_PmoaAlm3v3HighWarning_Type())
pmoaAlm3v3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlm3v3HighWarning.setStatus(_A)
_PmoaAlmTermpLowWarning_Type=EkiOnOff
_PmoaAlmTermpLowWarning_Object=MibScalar
pmoaAlmTermpLowWarning=_PmoaAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,9,2,1,1,75,7),_PmoaAlmTermpLowWarning_Type())
pmoaAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmTermpLowWarning.setStatus(_A)
_PmoaAlmTempHighWarning_Type=EkiOnOff
_PmoaAlmTempHighWarning_Object=MibScalar
pmoaAlmTempHighWarning=_PmoaAlmTempHighWarning_Object((1,3,6,1,4,1,20044,9,2,1,1,75,8),_PmoaAlmTempHighWarning_Type())
pmoaAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmTempHighWarning.setStatus(_A)
_PmoaAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoaAlmOtherUrg=_PmoaAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,2))
_PmoaAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoaAlmfoaAlarms=_PmoaAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,2,74))
_PmoaAlm3v3LowAlarm_Type=EkiOnOff
_PmoaAlm3v3LowAlarm_Object=MibScalar
pmoaAlm3v3LowAlarm=_PmoaAlm3v3LowAlarm_Object((1,3,6,1,4,1,20044,9,2,1,2,74,5),_PmoaAlm3v3LowAlarm_Type())
pmoaAlm3v3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlm3v3LowAlarm.setStatus(_A)
_PmoaAlm3v3HighAlarm_Type=EkiOnOff
_PmoaAlm3v3HighAlarm_Object=MibScalar
pmoaAlm3v3HighAlarm=_PmoaAlm3v3HighAlarm_Object((1,3,6,1,4,1,20044,9,2,1,2,74,6),_PmoaAlm3v3HighAlarm_Type())
pmoaAlm3v3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlm3v3HighAlarm.setStatus(_A)
_PmoaAlmTermpLowAlarm_Type=EkiOnOff
_PmoaAlmTermpLowAlarm_Object=MibScalar
pmoaAlmTermpLowAlarm=_PmoaAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,9,2,1,2,74,7),_PmoaAlmTermpLowAlarm_Type())
pmoaAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmTermpLowAlarm.setStatus(_A)
_PmoaAlmTempHighAlarm_Type=EkiOnOff
_PmoaAlmTempHighAlarm_Object=MibScalar
pmoaAlmTempHighAlarm=_PmoaAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,9,2,1,2,74,8),_PmoaAlmTempHighAlarm_Type())
pmoaAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmTempHighAlarm.setStatus(_A)
_PmoaAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoaAlmOtherCrit=_PmoaAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,3))
_PmoaAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoaAlmsynthAlm0=_PmoaAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,9,2,1,3,0))
_PmoaAlmMaintenanceMode_Type=EkiOnOff
_PmoaAlmMaintenanceMode_Object=MibScalar
pmoaAlmMaintenanceMode=_PmoaAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,9,2,1,3,0,1),_PmoaAlmMaintenanceMode_Type())
pmoaAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmMaintenanceMode.setStatus(_A)
_PmoaAlmModGlobFail_Type=EkiOnOff
_PmoaAlmModGlobFail_Object=MibScalar
pmoaAlmModGlobFail=_PmoaAlmModGlobFail_Object((1,3,6,1,4,1,20044,9,2,1,3,0,9),_PmoaAlmModGlobFail_Type())
pmoaAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmModGlobFail.setStatus(_A)
_PmoaAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoaAlmUpEdfaInitNotCompl_Object=MibScalar
pmoaAlmUpEdfaInitNotCompl=_PmoaAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,9,2,1,3,0,10),_PmoaAlmUpEdfaInitNotCompl_Type())
pmoaAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoaAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoaAlmDwEdfaInitNotCompl_Object=MibScalar
pmoaAlmDwEdfaInitNotCompl=_PmoaAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,9,2,1,3,0,11),_PmoaAlmDwEdfaInitNotCompl_Type())
pmoaAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoaAlmExtPumpNotLocked_Type=EkiOnOff
_PmoaAlmExtPumpNotLocked_Object=MibScalar
pmoaAlmExtPumpNotLocked=_PmoaAlmExtPumpNotLocked_Object((1,3,6,1,4,1,20044,9,2,1,3,0,12),_PmoaAlmExtPumpNotLocked_Type())
pmoaAlmExtPumpNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmExtPumpNotLocked.setStatus(_A)
_PmoaAlmDefFuseA_Type=EkiOnOff
_PmoaAlmDefFuseA_Object=MibScalar
pmoaAlmDefFuseA=_PmoaAlmDefFuseA_Object((1,3,6,1,4,1,20044,9,2,1,3,0,15),_PmoaAlmDefFuseA_Type())
pmoaAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmDefFuseA.setStatus(_A)
_PmoaAlmDefFuseB_Type=EkiOnOff
_PmoaAlmDefFuseB_Object=MibScalar
pmoaAlmDefFuseB=_PmoaAlmDefFuseB_Object((1,3,6,1,4,1,20044,9,2,1,3,0,16),_PmoaAlmDefFuseB_Type())
pmoaAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmDefFuseB.setStatus(_A)
_PmoaAlmClient_ObjectIdentity=ObjectIdentity
pmoaAlmClient=_PmoaAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2))
_PmoaAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoaAlmClientNurg=_PmoaAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,1))
_PmoaAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoaAlmclientEdfaWarnings=_PmoaAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,1,33))
_PmoaAlmClientGainLowWarning_Type=EkiOnOff
_PmoaAlmClientGainLowWarning_Object=MibScalar
pmoaAlmClientGainLowWarning=_PmoaAlmClientGainLowWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,1),_PmoaAlmClientGainLowWarning_Type())
pmoaAlmClientGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientGainLowWarning.setStatus(_A)
_PmoaAlmClientGainHighWarning_Type=EkiOnOff
_PmoaAlmClientGainHighWarning_Object=MibScalar
pmoaAlmClientGainHighWarning=_PmoaAlmClientGainHighWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,2),_PmoaAlmClientGainHighWarning_Type())
pmoaAlmClientGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientGainHighWarning.setStatus(_A)
_PmoaAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoaAlmClientInputPwrLowWarning_Object=MibScalar
pmoaAlmClientInputPwrLowWarning=_PmoaAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,3),_PmoaAlmClientInputPwrLowWarning_Type())
pmoaAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientInputPwrLowWarning.setStatus(_A)
_PmoaAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoaAlmClientInputPwrHighWarning_Object=MibScalar
pmoaAlmClientInputPwrHighWarning=_PmoaAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,4),_PmoaAlmClientInputPwrHighWarning_Type())
pmoaAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientInputPwrHighWarning.setStatus(_A)
_PmoaAlmClientOutputPwrLowWarning_Type=EkiOnOff
_PmoaAlmClientOutputPwrLowWarning_Object=MibScalar
pmoaAlmClientOutputPwrLowWarning=_PmoaAlmClientOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,5),_PmoaAlmClientOutputPwrLowWarning_Type())
pmoaAlmClientOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientOutputPwrLowWarning.setStatus(_A)
_PmoaAlmClientOutputPwrHighWarning_Type=EkiOnOff
_PmoaAlmClientOutputPwrHighWarning_Object=MibScalar
pmoaAlmClientOutputPwrHighWarning=_PmoaAlmClientOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,6),_PmoaAlmClientOutputPwrHighWarning_Type())
pmoaAlmClientOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientOutputPwrHighWarning.setStatus(_A)
_PmoaAlmClientBiasLowWarning_Type=EkiOnOff
_PmoaAlmClientBiasLowWarning_Object=MibScalar
pmoaAlmClientBiasLowWarning=_PmoaAlmClientBiasLowWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,7),_PmoaAlmClientBiasLowWarning_Type())
pmoaAlmClientBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientBiasLowWarning.setStatus(_A)
_PmoaAlmClientBiasHighWarning_Type=EkiOnOff
_PmoaAlmClientBiasHighWarning_Object=MibScalar
pmoaAlmClientBiasHighWarning=_PmoaAlmClientBiasHighWarning_Object((1,3,6,1,4,1,20044,9,2,2,1,33,8),_PmoaAlmClientBiasHighWarning_Type())
pmoaAlmClientBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientBiasHighWarning.setStatus(_A)
_PmoaAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoaAlmClientUrg=_PmoaAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,2))
_PmoaAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoaAlmclientEdfaAlarms1=_PmoaAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,2,32))
_PmoaAlmClientGainLowAlarm_Type=EkiOnOff
_PmoaAlmClientGainLowAlarm_Object=MibScalar
pmoaAlmClientGainLowAlarm=_PmoaAlmClientGainLowAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,1),_PmoaAlmClientGainLowAlarm_Type())
pmoaAlmClientGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientGainLowAlarm.setStatus(_A)
_PmoaAlmClientGainHighAlarm_Type=EkiOnOff
_PmoaAlmClientGainHighAlarm_Object=MibScalar
pmoaAlmClientGainHighAlarm=_PmoaAlmClientGainHighAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,2),_PmoaAlmClientGainHighAlarm_Type())
pmoaAlmClientGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientGainHighAlarm.setStatus(_A)
_PmoaAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoaAlmClientInputPwrLowAlarm_Object=MibScalar
pmoaAlmClientInputPwrLowAlarm=_PmoaAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,3),_PmoaAlmClientInputPwrLowAlarm_Type())
pmoaAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoaAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoaAlmClientInputPwrHighAlarm_Object=MibScalar
pmoaAlmClientInputPwrHighAlarm=_PmoaAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,4),_PmoaAlmClientInputPwrHighAlarm_Type())
pmoaAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoaAlmClientOutputPwrLowAlarm_Type=EkiOnOff
_PmoaAlmClientOutputPwrLowAlarm_Object=MibScalar
pmoaAlmClientOutputPwrLowAlarm=_PmoaAlmClientOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,5),_PmoaAlmClientOutputPwrLowAlarm_Type())
pmoaAlmClientOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientOutputPwrLowAlarm.setStatus(_A)
_PmoaAlmClientOutputPwrHighAlarm_Type=EkiOnOff
_PmoaAlmClientOutputPwrHighAlarm_Object=MibScalar
pmoaAlmClientOutputPwrHighAlarm=_PmoaAlmClientOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,6),_PmoaAlmClientOutputPwrHighAlarm_Type())
pmoaAlmClientOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientOutputPwrHighAlarm.setStatus(_A)
_PmoaAlmClientBiasLowAlarm_Type=EkiOnOff
_PmoaAlmClientBiasLowAlarm_Object=MibScalar
pmoaAlmClientBiasLowAlarm=_PmoaAlmClientBiasLowAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,7),_PmoaAlmClientBiasLowAlarm_Type())
pmoaAlmClientBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientBiasLowAlarm.setStatus(_A)
_PmoaAlmClientBiasHighAlarm_Type=EkiOnOff
_PmoaAlmClientBiasHighAlarm_Object=MibScalar
pmoaAlmClientBiasHighAlarm=_PmoaAlmClientBiasHighAlarm_Object((1,3,6,1,4,1,20044,9,2,2,2,32,8),_PmoaAlmClientBiasHighAlarm_Type())
pmoaAlmClientBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientBiasHighAlarm.setStatus(_A)
_PmoaAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoaAlmClientCrit=_PmoaAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,3))
_PmoaAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoaAlmsynthAlm8=_PmoaAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,3,8))
_PmoaAlmClientHwFail_Type=EkiOnOff
_PmoaAlmClientHwFail_Object=MibScalar
pmoaAlmClientHwFail=_PmoaAlmClientHwFail_Object((1,3,6,1,4,1,20044,9,2,2,3,8,4),_PmoaAlmClientHwFail_Type())
pmoaAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientHwFail.setStatus(_A)
_PmoaAlmClientTxOff_Type=EkiOnOff
_PmoaAlmClientTxOff_Object=MibScalar
pmoaAlmClientTxOff=_PmoaAlmClientTxOff_Object((1,3,6,1,4,1,20044,9,2,2,3,8,5),_PmoaAlmClientTxOff_Type())
pmoaAlmClientTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientTxOff.setStatus(_A)
_PmoaAlmClientDdmWarning_Type=EkiOnOff
_PmoaAlmClientDdmWarning_Object=MibScalar
pmoaAlmClientDdmWarning=_PmoaAlmClientDdmWarning_Object((1,3,6,1,4,1,20044,9,2,2,3,8,9),_PmoaAlmClientDdmWarning_Type())
pmoaAlmClientDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientDdmWarning.setStatus(_A)
_PmoaAlmClientDdmAlm_Type=EkiOnOff
_PmoaAlmClientDdmAlm_Object=MibScalar
pmoaAlmClientDdmAlm=_PmoaAlmClientDdmAlm_Object((1,3,6,1,4,1,20044,9,2,2,3,8,10),_PmoaAlmClientDdmAlm_Type())
pmoaAlmClientDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientDdmAlm.setStatus(_A)
_PmoaAlmClientFail_Type=EkiOnOff
_PmoaAlmClientFail_Object=MibScalar
pmoaAlmClientFail=_PmoaAlmClientFail_Object((1,3,6,1,4,1,20044,9,2,2,3,8,12),_PmoaAlmClientFail_Type())
pmoaAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientFail.setStatus(_A)
_PmoaAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoaAlmclientEdfaAlarms2=_PmoaAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,9,2,2,3,35))
_PmoaAlmClientEdfaNr_Type=EkiOnOff
_PmoaAlmClientEdfaNr_Object=MibScalar
pmoaAlmClientEdfaNr=_PmoaAlmClientEdfaNr_Object((1,3,6,1,4,1,20044,9,2,2,3,35,1),_PmoaAlmClientEdfaNr_Type())
pmoaAlmClientEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientEdfaNr.setStatus(_A)
_PmoaAlmClientEdfaTecFail_Type=EkiOnOff
_PmoaAlmClientEdfaTecFail_Object=MibScalar
pmoaAlmClientEdfaTecFail=_PmoaAlmClientEdfaTecFail_Object((1,3,6,1,4,1,20044,9,2,2,3,35,2),_PmoaAlmClientEdfaTecFail_Type())
pmoaAlmClientEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientEdfaTecFail.setStatus(_A)
_PmoaAlmClientEdfaLaserFail_Type=EkiOnOff
_PmoaAlmClientEdfaLaserFail_Object=MibScalar
pmoaAlmClientEdfaLaserFail=_PmoaAlmClientEdfaLaserFail_Object((1,3,6,1,4,1,20044,9,2,2,3,35,3),_PmoaAlmClientEdfaLaserFail_Type())
pmoaAlmClientEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientEdfaLaserFail.setStatus(_A)
_PmoaAlmClientEdfaLos_Type=EkiOnOff
_PmoaAlmClientEdfaLos_Object=MibScalar
pmoaAlmClientEdfaLos=_PmoaAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,9,2,2,3,35,4),_PmoaAlmClientEdfaLos_Type())
pmoaAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientEdfaLos.setStatus(_A)
_PmoaAlmClientExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoaAlmClientExtPumpEdfaLowCurrent_Object=MibScalar
pmoaAlmClientExtPumpEdfaLowCurrent=_PmoaAlmClientExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,9,2,2,3,35,5),_PmoaAlmClientExtPumpEdfaLowCurrent_Type())
pmoaAlmClientExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmClientExtPumpEdfaLowCurrent.setStatus(_A)
_PmoaAlmLine_ObjectIdentity=ObjectIdentity
pmoaAlmLine=_PmoaAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3))
_PmoaAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoaAlmLineNurg=_PmoaAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,1))
_PmoaAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoaAlmlineEdfaWarnings=_PmoaAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,1,41))
_PmoaAlmLineGainLowWarning_Type=EkiOnOff
_PmoaAlmLineGainLowWarning_Object=MibScalar
pmoaAlmLineGainLowWarning=_PmoaAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,1),_PmoaAlmLineGainLowWarning_Type())
pmoaAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineGainLowWarning.setStatus(_A)
_PmoaAlmLineGainHighWarning_Type=EkiOnOff
_PmoaAlmLineGainHighWarning_Object=MibScalar
pmoaAlmLineGainHighWarning=_PmoaAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,2),_PmoaAlmLineGainHighWarning_Type())
pmoaAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineGainHighWarning.setStatus(_A)
_PmoaAlmLineInputPwrLowWarning_Type=EkiOnOff
_PmoaAlmLineInputPwrLowWarning_Object=MibScalar
pmoaAlmLineInputPwrLowWarning=_PmoaAlmLineInputPwrLowWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,3),_PmoaAlmLineInputPwrLowWarning_Type())
pmoaAlmLineInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineInputPwrLowWarning.setStatus(_A)
_PmoaAlmLineInputPwrHighWarning_Type=EkiOnOff
_PmoaAlmLineInputPwrHighWarning_Object=MibScalar
pmoaAlmLineInputPwrHighWarning=_PmoaAlmLineInputPwrHighWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,4),_PmoaAlmLineInputPwrHighWarning_Type())
pmoaAlmLineInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineInputPwrHighWarning.setStatus(_A)
_PmoaAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoaAlmLineOutputPwrLowWarning_Object=MibScalar
pmoaAlmLineOutputPwrLowWarning=_PmoaAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,5),_PmoaAlmLineOutputPwrLowWarning_Type())
pmoaAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoaAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoaAlmLineOutputPwrHighWarning_Object=MibScalar
pmoaAlmLineOutputPwrHighWarning=_PmoaAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,6),_PmoaAlmLineOutputPwrHighWarning_Type())
pmoaAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoaAlmLineBiasLowWarning_Type=EkiOnOff
_PmoaAlmLineBiasLowWarning_Object=MibScalar
pmoaAlmLineBiasLowWarning=_PmoaAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,7),_PmoaAlmLineBiasLowWarning_Type())
pmoaAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineBiasLowWarning.setStatus(_A)
_PmoaAlmLineBiasHighWarning_Type=EkiOnOff
_PmoaAlmLineBiasHighWarning_Object=MibScalar
pmoaAlmLineBiasHighWarning=_PmoaAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,9,2,3,1,41,8),_PmoaAlmLineBiasHighWarning_Type())
pmoaAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineBiasHighWarning.setStatus(_A)
_PmoaAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoaAlmLineUrg=_PmoaAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,2))
_PmoaAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoaAlmlineEdfaAlarms1=_PmoaAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,2,40))
_PmoaAlmLineGainLowAlarm_Type=EkiOnOff
_PmoaAlmLineGainLowAlarm_Object=MibScalar
pmoaAlmLineGainLowAlarm=_PmoaAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,1),_PmoaAlmLineGainLowAlarm_Type())
pmoaAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineGainLowAlarm.setStatus(_A)
_PmoaAlmLineGainHighAlarm_Type=EkiOnOff
_PmoaAlmLineGainHighAlarm_Object=MibScalar
pmoaAlmLineGainHighAlarm=_PmoaAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,2),_PmoaAlmLineGainHighAlarm_Type())
pmoaAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineGainHighAlarm.setStatus(_A)
_PmoaAlmLineInputPwrLowAlarm_Type=EkiOnOff
_PmoaAlmLineInputPwrLowAlarm_Object=MibScalar
pmoaAlmLineInputPwrLowAlarm=_PmoaAlmLineInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,3),_PmoaAlmLineInputPwrLowAlarm_Type())
pmoaAlmLineInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineInputPwrLowAlarm.setStatus(_A)
_PmoaAlmLineInputPwrHighAlarm_Type=EkiOnOff
_PmoaAlmLineInputPwrHighAlarm_Object=MibScalar
pmoaAlmLineInputPwrHighAlarm=_PmoaAlmLineInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,4),_PmoaAlmLineInputPwrHighAlarm_Type())
pmoaAlmLineInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineInputPwrHighAlarm.setStatus(_A)
_PmoaAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoaAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoaAlmLineOutputPwrLowAlarm=_PmoaAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,5),_PmoaAlmLineOutputPwrLowAlarm_Type())
pmoaAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoaAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoaAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoaAlmLineOutputPwrHighAlarm=_PmoaAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,6),_PmoaAlmLineOutputPwrHighAlarm_Type())
pmoaAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoaAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoaAlmLineBiasLowAlarm_Object=MibScalar
pmoaAlmLineBiasLowAlarm=_PmoaAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,7),_PmoaAlmLineBiasLowAlarm_Type())
pmoaAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineBiasLowAlarm.setStatus(_A)
_PmoaAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoaAlmLineBiasHighAlarm_Object=MibScalar
pmoaAlmLineBiasHighAlarm=_PmoaAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,9,2,3,2,40,8),_PmoaAlmLineBiasHighAlarm_Type())
pmoaAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineBiasHighAlarm.setStatus(_A)
_PmoaAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoaAlmLineCrit=_PmoaAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,3))
_PmoaAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoaAlmsynthAlm7=_PmoaAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,3,7))
_PmoaAlmLineHwFail_Type=EkiOnOff
_PmoaAlmLineHwFail_Object=MibScalar
pmoaAlmLineHwFail=_PmoaAlmLineHwFail_Object((1,3,6,1,4,1,20044,9,2,3,3,7,4),_PmoaAlmLineHwFail_Type())
pmoaAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineHwFail.setStatus(_A)
_PmoaAlmLineTxOff_Type=EkiOnOff
_PmoaAlmLineTxOff_Object=MibScalar
pmoaAlmLineTxOff=_PmoaAlmLineTxOff_Object((1,3,6,1,4,1,20044,9,2,3,3,7,5),_PmoaAlmLineTxOff_Type())
pmoaAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineTxOff.setStatus(_A)
_PmoaAlmLineDdmWarning_Type=EkiOnOff
_PmoaAlmLineDdmWarning_Object=MibScalar
pmoaAlmLineDdmWarning=_PmoaAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,9,2,3,3,7,9),_PmoaAlmLineDdmWarning_Type())
pmoaAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineDdmWarning.setStatus(_A)
_PmoaAlmLineDdmAlm_Type=EkiOnOff
_PmoaAlmLineDdmAlm_Object=MibScalar
pmoaAlmLineDdmAlm=_PmoaAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,9,2,3,3,7,10),_PmoaAlmLineDdmAlm_Type())
pmoaAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineDdmAlm.setStatus(_A)
_PmoaAlmLineFail_Type=EkiOnOff
_PmoaAlmLineFail_Object=MibScalar
pmoaAlmLineFail=_PmoaAlmLineFail_Object((1,3,6,1,4,1,20044,9,2,3,3,7,12),_PmoaAlmLineFail_Type())
pmoaAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineFail.setStatus(_A)
_PmoaAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoaAlmlineEdfaAlarms2=_PmoaAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,9,2,3,3,43))
_PmoaAlmLineEdfaNr_Type=EkiOnOff
_PmoaAlmLineEdfaNr_Object=MibScalar
pmoaAlmLineEdfaNr=_PmoaAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,9,2,3,3,43,1),_PmoaAlmLineEdfaNr_Type())
pmoaAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineEdfaNr.setStatus(_A)
_PmoaAlmLineEdfaTecFail_Type=EkiOnOff
_PmoaAlmLineEdfaTecFail_Object=MibScalar
pmoaAlmLineEdfaTecFail=_PmoaAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,9,2,3,3,43,2),_PmoaAlmLineEdfaTecFail_Type())
pmoaAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineEdfaTecFail.setStatus(_A)
_PmoaAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoaAlmLineEdfaLaserFail_Object=MibScalar
pmoaAlmLineEdfaLaserFail=_PmoaAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,9,2,3,3,43,3),_PmoaAlmLineEdfaLaserFail_Type())
pmoaAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineEdfaLaserFail.setStatus(_A)
_PmoaAlmLineEdfaLos_Type=EkiOnOff
_PmoaAlmLineEdfaLos_Object=MibScalar
pmoaAlmLineEdfaLos=_PmoaAlmLineEdfaLos_Object((1,3,6,1,4,1,20044,9,2,3,3,43,4),_PmoaAlmLineEdfaLos_Type())
pmoaAlmLineEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineEdfaLos.setStatus(_A)
_PmoaAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoaAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoaAlmLineExtPumpEdfaLowCurrent=_PmoaAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,9,2,3,3,43,5),_PmoaAlmLineExtPumpEdfaLowCurrent_Type())
pmoaAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_Pmoameasures_ObjectIdentity=ObjectIdentity
pmoameasures=_Pmoameasures_ObjectIdentity((1,3,6,1,4,1,20044,9,3))
_PmoaMesrOther_ObjectIdentity=ObjectIdentity
pmoaMesrOther=_PmoaMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,9,3,1))
class _PmoaMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrtempMeas_Type.__name__=_E
_PmoaMesrtempMeas_Object=MibScalar
pmoaMesrtempMeas=_PmoaMesrtempMeas_Object((1,3,6,1,4,1,20044,9,3,1,72),_PmoaMesrtempMeas_Type())
pmoaMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrtempMeas.setStatus(_A)
class _PmoaMesr3v3Meas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesr3v3Meas_Type.__name__=_E
_PmoaMesr3v3Meas_Object=MibScalar
pmoaMesr3v3Meas=_PmoaMesr3v3Meas_Object((1,3,6,1,4,1,20044,9,3,1,73),_PmoaMesr3v3Meas_Type())
pmoaMesr3v3Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesr3v3Meas.setStatus(_A)
_PmoaMesrClient_ObjectIdentity=ObjectIdentity
pmoaMesrClient=_PmoaMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,9,3,2))
class _PmoaMesrclientEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrclientEdfaBiasMeas_Type.__name__=_E
_PmoaMesrclientEdfaBiasMeas_Object=MibScalar
pmoaMesrclientEdfaBiasMeas=_PmoaMesrclientEdfaBiasMeas_Object((1,3,6,1,4,1,20044,9,3,2,32),_PmoaMesrclientEdfaBiasMeas_Type())
pmoaMesrclientEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrclientEdfaBiasMeas.setStatus(_A)
class _PmoaMesrclientEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrclientEdfaTxpwrMeas_Type.__name__=_E
_PmoaMesrclientEdfaTxpwrMeas_Object=MibScalar
pmoaMesrclientEdfaTxpwrMeas=_PmoaMesrclientEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,9,3,2,33),_PmoaMesrclientEdfaTxpwrMeas_Type())
pmoaMesrclientEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrclientEdfaTxpwrMeas.setStatus(_A)
class _PmoaMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrclientEdfaRxpwrMeas_Type.__name__=_E
_PmoaMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoaMesrclientEdfaRxpwrMeas=_PmoaMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,9,3,2,34),_PmoaMesrclientEdfaRxpwrMeas_Type())
pmoaMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrclientEdfaRxpwrMeas.setStatus(_A)
class _PmoaMesrclientEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrclientEdfaGainMeas_Type.__name__=_E
_PmoaMesrclientEdfaGainMeas_Object=MibScalar
pmoaMesrclientEdfaGainMeas=_PmoaMesrclientEdfaGainMeas_Object((1,3,6,1,4,1,20044,9,3,2,35),_PmoaMesrclientEdfaGainMeas_Type())
pmoaMesrclientEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrclientEdfaGainMeas.setStatus(_A)
_PmoaMesrLine_ObjectIdentity=ObjectIdentity
pmoaMesrLine=_PmoaMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,9,3,3))
class _PmoaMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrlineEdfaBiasMeas_Type.__name__=_E
_PmoaMesrlineEdfaBiasMeas_Object=MibScalar
pmoaMesrlineEdfaBiasMeas=_PmoaMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,9,3,3,40),_PmoaMesrlineEdfaBiasMeas_Type())
pmoaMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoaMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrlineEdfaTxpwrMeas_Type.__name__=_E
_PmoaMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoaMesrlineEdfaTxpwrMeas=_PmoaMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,9,3,3,41),_PmoaMesrlineEdfaTxpwrMeas_Type())
pmoaMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoaMesrlineEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrlineEdfaRxpwrMeas_Type.__name__=_E
_PmoaMesrlineEdfaRxpwrMeas_Object=MibScalar
pmoaMesrlineEdfaRxpwrMeas=_PmoaMesrlineEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,9,3,3,42),_PmoaMesrlineEdfaRxpwrMeas_Type())
pmoaMesrlineEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrlineEdfaRxpwrMeas.setStatus(_A)
class _PmoaMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaMesrlineEdfaGainMeas_Type.__name__=_E
_PmoaMesrlineEdfaGainMeas_Object=MibScalar
pmoaMesrlineEdfaGainMeas=_PmoaMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,9,3,3,43),_PmoaMesrlineEdfaGainMeas_Type())
pmoaMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaMesrlineEdfaGainMeas.setStatus(_A)
_PmoacontrolsWrite_ObjectIdentity=ObjectIdentity
pmoacontrolsWrite=_PmoacontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,9,6))
_PmoaCtrlOther_ObjectIdentity=ObjectIdentity
pmoaCtrlOther=_PmoaCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,9,6,1))
_PmoaCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoaCtrlsynth0=_PmoaCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,9,6,1,0))
_PmoaCtrlConfLoad_Type=EkiOnOff
_PmoaCtrlConfLoad_Object=MibScalar
pmoaCtrlConfLoad=_PmoaCtrlConfLoad_Object((1,3,6,1,4,1,20044,9,6,1,0,1),_PmoaCtrlConfLoad_Type())
pmoaCtrlConfLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlConfLoad.setStatus(_A)
_PmoaCtrlConfFlash_Type=EkiOnOff
_PmoaCtrlConfFlash_Object=MibScalar
pmoaCtrlConfFlash=_PmoaCtrlConfFlash_Object((1,3,6,1,4,1,20044,9,6,1,0,9),_PmoaCtrlConfFlash_Type())
pmoaCtrlConfFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlConfFlash.setStatus(_A)
_PmoaCtrlConfClear_Type=EkiOnOff
_PmoaCtrlConfClear_Object=MibScalar
pmoaCtrlConfClear=_PmoaCtrlConfClear_Object((1,3,6,1,4,1,20044,9,6,1,0,13),_PmoaCtrlConfClear_Type())
pmoaCtrlConfClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlConfClear.setStatus(_A)
_PmoaCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoaCtrlswMgnt=_PmoaCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,9,6,1,5))
_PmoaCtrlColdReset_Type=EkiOnOff
_PmoaCtrlColdReset_Object=MibScalar
pmoaCtrlColdReset=_PmoaCtrlColdReset_Object((1,3,6,1,4,1,20044,9,6,1,5,2),_PmoaCtrlColdReset_Type())
pmoaCtrlColdReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlColdReset.setStatus(_A)
_PmoaCtrlWarmReset_Type=EkiOnOff
_PmoaCtrlWarmReset_Object=MibScalar
pmoaCtrlWarmReset=_PmoaCtrlWarmReset_Object((1,3,6,1,4,1,20044,9,6,1,5,3),_PmoaCtrlWarmReset_Type())
pmoaCtrlWarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlWarmReset.setStatus(_A)
_PmoaCtrlpowerDown_ObjectIdentity=ObjectIdentity
pmoaCtrlpowerDown=_PmoaCtrlpowerDown_ObjectIdentity((1,3,6,1,4,1,20044,9,6,1,72))
_PmoaCtrlSoftPowerDown_Type=EkiOnOff
_PmoaCtrlSoftPowerDown_Object=MibScalar
pmoaCtrlSoftPowerDown=_PmoaCtrlSoftPowerDown_Object((1,3,6,1,4,1,20044,9,6,1,72,1),_PmoaCtrlSoftPowerDown_Type())
pmoaCtrlSoftPowerDown.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlSoftPowerDown.setStatus(_A)
_PmoaCtrlledTest_ObjectIdentity=ObjectIdentity
pmoaCtrlledTest=_PmoaCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,9,6,1,73))
_PmoaCtrlGreenLed_Type=EkiOnOff
_PmoaCtrlGreenLed_Object=MibScalar
pmoaCtrlGreenLed=_PmoaCtrlGreenLed_Object((1,3,6,1,4,1,20044,9,6,1,73,1),_PmoaCtrlGreenLed_Type())
pmoaCtrlGreenLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlGreenLed.setStatus(_A)
_PmoaCtrlRedLed_Type=EkiOnOff
_PmoaCtrlRedLed_Object=MibScalar
pmoaCtrlRedLed=_PmoaCtrlRedLed_Object((1,3,6,1,4,1,20044,9,6,1,73,2),_PmoaCtrlRedLed_Type())
pmoaCtrlRedLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlRedLed.setStatus(_A)
_PmoaCtrlLedOff_Type=EkiOnOff
_PmoaCtrlLedOff_Object=MibScalar
pmoaCtrlLedOff=_PmoaCtrlLedOff_Object((1,3,6,1,4,1,20044,9,6,1,73,3),_PmoaCtrlLedOff_Type())
pmoaCtrlLedOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlLedOff.setStatus(_A)
_PmoaCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoaCtrlmaintMode=_PmoaCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,9,6,1,75))
_PmoaCtrlMaintenance_Type=EkiOnOff
_PmoaCtrlMaintenance_Object=MibScalar
pmoaCtrlMaintenance=_PmoaCtrlMaintenance_Object((1,3,6,1,4,1,20044,9,6,1,75,1),_PmoaCtrlMaintenance_Type())
pmoaCtrlMaintenance.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlMaintenance.setStatus(_A)
_PmoaCtrlClient_ObjectIdentity=ObjectIdentity
pmoaCtrlClient=_PmoaCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,9,6,2))
_PmoaCtrlclientEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoaCtrlclientEdfaLaserOff=_PmoaCtrlclientEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,9,6,2,32))
_PmoaCtrlClientEdfaLaserOff_Type=EkiOnOff
_PmoaCtrlClientEdfaLaserOff_Object=MibScalar
pmoaCtrlClientEdfaLaserOff=_PmoaCtrlClientEdfaLaserOff_Object((1,3,6,1,4,1,20044,9,6,2,32,1),_PmoaCtrlClientEdfaLaserOff_Type())
pmoaCtrlClientEdfaLaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlClientEdfaLaserOff.setStatus(_A)
_PmoaCtrlclientEdfaMode_Type=PmoapreampMode
_PmoaCtrlclientEdfaMode_Object=MibScalar
pmoaCtrlclientEdfaMode=_PmoaCtrlclientEdfaMode_Object((1,3,6,1,4,1,20044,9,6,2,33),_PmoaCtrlclientEdfaMode_Type())
pmoaCtrlclientEdfaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlclientEdfaMode.setStatus(_A)
class _PmoaCtrlclientIlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrlclientIlasSettingValue_Type.__name__=_E
_PmoaCtrlclientIlasSettingValue_Object=MibScalar
pmoaCtrlclientIlasSettingValue=_PmoaCtrlclientIlasSettingValue_Object((1,3,6,1,4,1,20044,9,6,2,34),_PmoaCtrlclientIlasSettingValue_Type())
pmoaCtrlclientIlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlclientIlasSettingValue.setStatus(_A)
class _PmoaCtrlclientPlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrlclientPlasSettingValue_Type.__name__=_E
_PmoaCtrlclientPlasSettingValue_Object=MibScalar
pmoaCtrlclientPlasSettingValue=_PmoaCtrlclientPlasSettingValue_Object((1,3,6,1,4,1,20044,9,6,2,35),_PmoaCtrlclientPlasSettingValue_Type())
pmoaCtrlclientPlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlclientPlasSettingValue.setStatus(_A)
class _PmoaCtrlclientGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrlclientGainSettingValue_Type.__name__=_E
_PmoaCtrlclientGainSettingValue_Object=MibScalar
pmoaCtrlclientGainSettingValue=_PmoaCtrlclientGainSettingValue_Object((1,3,6,1,4,1,20044,9,6,2,36),_PmoaCtrlclientGainSettingValue_Type())
pmoaCtrlclientGainSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlclientGainSettingValue.setStatus(_A)
class _PmoaCtrlclientEffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrlclientEffPwrOutSettingValue_Type.__name__=_E
_PmoaCtrlclientEffPwrOutSettingValue_Object=MibScalar
pmoaCtrlclientEffPwrOutSettingValue=_PmoaCtrlclientEffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,9,6,2,37),_PmoaCtrlclientEffPwrOutSettingValue_Type())
pmoaCtrlclientEffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlclientEffPwrOutSettingValue.setStatus(_A)
_PmoaCtrlLine_ObjectIdentity=ObjectIdentity
pmoaCtrlLine=_PmoaCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,9,6,3))
_PmoaCtrllineEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoaCtrllineEdfaLaserOff=_PmoaCtrllineEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,9,6,3,40))
_PmoaCtrlLineEdfaLaserOff_Type=EkiOnOff
_PmoaCtrlLineEdfaLaserOff_Object=MibScalar
pmoaCtrlLineEdfaLaserOff=_PmoaCtrlLineEdfaLaserOff_Object((1,3,6,1,4,1,20044,9,6,3,40,1),_PmoaCtrlLineEdfaLaserOff_Type())
pmoaCtrlLineEdfaLaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrlLineEdfaLaserOff.setStatus(_A)
_PmoaCtrllineEdfaMode_Type=PmoaboosterMode
_PmoaCtrllineEdfaMode_Object=MibScalar
pmoaCtrllineEdfaMode=_PmoaCtrllineEdfaMode_Object((1,3,6,1,4,1,20044,9,6,3,41),_PmoaCtrllineEdfaMode_Type())
pmoaCtrllineEdfaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrllineEdfaMode.setStatus(_A)
class _PmoaCtrllineIlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrllineIlasSettingValue_Type.__name__=_E
_PmoaCtrllineIlasSettingValue_Object=MibScalar
pmoaCtrllineIlasSettingValue=_PmoaCtrllineIlasSettingValue_Object((1,3,6,1,4,1,20044,9,6,3,42),_PmoaCtrllineIlasSettingValue_Type())
pmoaCtrllineIlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrllineIlasSettingValue.setStatus(_A)
class _PmoaCtrllinePlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrllinePlasSettingValue_Type.__name__=_E
_PmoaCtrllinePlasSettingValue_Object=MibScalar
pmoaCtrllinePlasSettingValue=_PmoaCtrllinePlasSettingValue_Object((1,3,6,1,4,1,20044,9,6,3,43),_PmoaCtrllinePlasSettingValue_Type())
pmoaCtrllinePlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrllinePlasSettingValue.setStatus(_A)
class _PmoaCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrllineGainSettingValue_Type.__name__=_E
_PmoaCtrllineGainSettingValue_Object=MibScalar
pmoaCtrllineGainSettingValue=_PmoaCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,9,6,3,44),_PmoaCtrllineGainSettingValue_Type())
pmoaCtrllineGainSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrllineGainSettingValue.setStatus(_A)
class _PmoaCtrllineEffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoaCtrllineEffPwrOutSettingValue_Type.__name__=_E
_PmoaCtrllineEffPwrOutSettingValue_Object=MibScalar
pmoaCtrllineEffPwrOutSettingValue=_PmoaCtrllineEffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,9,6,3,45),_PmoaCtrllineEffPwrOutSettingValue_Type())
pmoaCtrllineEffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCtrllineEffPwrOutSettingValue.setStatus(_A)
_Pmoari_ObjectIdentity=ObjectIdentity
pmoari=_Pmoari_ObjectIdentity((1,3,6,1,4,1,20044,9,7))
_PmoaRinvReloadInventory_Type=EkiOnOff
_PmoaRinvReloadInventory_Object=MibScalar
pmoaRinvReloadInventory=_PmoaRinvReloadInventory_Object((1,3,6,1,4,1,20044,9,7,2),_PmoaRinvReloadInventory_Type())
pmoaRinvReloadInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaRinvReloadInventory.setStatus(_A)
_PmoaRinvModulePlatform_Type=DisplayString
_PmoaRinvModulePlatform_Object=MibScalar
pmoaRinvModulePlatform=_PmoaRinvModulePlatform_Object((1,3,6,1,4,1,20044,9,7,3),_PmoaRinvModulePlatform_Type())
pmoaRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvModulePlatform.setStatus(_A)
_PmoaRinvSwPlatform_Type=DisplayString
_PmoaRinvSwPlatform_Object=MibScalar
pmoaRinvSwPlatform=_PmoaRinvSwPlatform_Object((1,3,6,1,4,1,20044,9,7,4),_PmoaRinvSwPlatform_Type())
pmoaRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvSwPlatform.setStatus(_A)
_PmoaRinvSwFoa_Type=DisplayString
_PmoaRinvSwFoa_Object=MibScalar
pmoaRinvSwFoa=_PmoaRinvSwFoa_Object((1,3,6,1,4,1,20044,9,7,5),_PmoaRinvSwFoa_Type())
pmoaRinvSwFoa.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvSwFoa.setStatus(_A)
_PmoaRinvBoosterTable_Object=MibTable
pmoaRinvBoosterTable=_PmoaRinvBoosterTable_Object((1,3,6,1,4,1,20044,9,7,6))
if mibBuilder.loadTexts:pmoaRinvBoosterTable.setStatus(_A)
_PmoaRinvBoosterEntry_Object=MibTableRow
pmoaRinvBoosterEntry=_PmoaRinvBoosterEntry_Object((1,3,6,1,4,1,20044,9,7,6,1))
pmoaRinvBoosterEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:pmoaRinvBoosterEntry.setStatus(_A)
class _PmoaRinvBoosterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoaRinvBoosterIndex_Type.__name__=_E
_PmoaRinvBoosterIndex_Object=MibTableColumn
pmoaRinvBoosterIndex=_PmoaRinvBoosterIndex_Object((1,3,6,1,4,1,20044,9,7,6,1,1),_PmoaRinvBoosterIndex_Type())
pmoaRinvBoosterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvBoosterIndex.setStatus(_A)
_PmoaRinvBooster_Type=DisplayString
_PmoaRinvBooster_Object=MibTableColumn
pmoaRinvBooster=_PmoaRinvBooster_Object((1,3,6,1,4,1,20044,9,7,6,1,2),_PmoaRinvBooster_Type())
pmoaRinvBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvBooster.setStatus(_A)
_PmoaRinvPreAmpTable_Object=MibTable
pmoaRinvPreAmpTable=_PmoaRinvPreAmpTable_Object((1,3,6,1,4,1,20044,9,7,7))
if mibBuilder.loadTexts:pmoaRinvPreAmpTable.setStatus(_A)
_PmoaRinvPreAmpEntry_Object=MibTableRow
pmoaRinvPreAmpEntry=_PmoaRinvPreAmpEntry_Object((1,3,6,1,4,1,20044,9,7,7,1))
pmoaRinvPreAmpEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:pmoaRinvPreAmpEntry.setStatus(_A)
class _PmoaRinvPreAmpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoaRinvPreAmpIndex_Type.__name__=_E
_PmoaRinvPreAmpIndex_Object=MibTableColumn
pmoaRinvPreAmpIndex=_PmoaRinvPreAmpIndex_Object((1,3,6,1,4,1,20044,9,7,7,1,1),_PmoaRinvPreAmpIndex_Type())
pmoaRinvPreAmpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvPreAmpIndex.setStatus(_A)
_PmoaRinvPreAmp_Type=DisplayString
_PmoaRinvPreAmp_Object=MibTableColumn
pmoaRinvPreAmp=_PmoaRinvPreAmp_Object((1,3,6,1,4,1,20044,9,7,7,1,2),_PmoaRinvPreAmp_Type())
pmoaRinvPreAmp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaRinvPreAmp.setStatus(_A)
_PmoaConfig_ObjectIdentity=ObjectIdentity
pmoaConfig=_PmoaConfig_ObjectIdentity((1,3,6,1,4,1,20044,9,9))
_PmoaCfgNoValue_ObjectIdentity=ObjectIdentity
pmoaCfgNoValue=_PmoaCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,9,9,1))
_PmoatableclientStartup_ObjectIdentity=ObjectIdentity
pmoatableclientStartup=_PmoatableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,9,9,1,1))
class _PmoaCfgclientEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoaCfgclientEdfaLaserCtrl_Type.__name__=_G
_PmoaCfgclientEdfaLaserCtrl_Object=MibScalar
pmoaCfgclientEdfaLaserCtrl=_PmoaCfgclientEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,9,9,1,1,2),_PmoaCfgclientEdfaLaserCtrl_Type())
pmoaCfgclientEdfaLaserCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfgclientEdfaLaserCtrl.setStatus(_A)
class _PmoaCfgclientEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoaCfgclientEdfaLaserMode_Type.__name__=_G
_PmoaCfgclientEdfaLaserMode_Object=MibScalar
pmoaCfgclientEdfaLaserMode=_PmoaCfgclientEdfaLaserMode_Object((1,3,6,1,4,1,20044,9,9,1,1,3),_PmoaCfgclientEdfaLaserMode_Type())
pmoaCfgclientEdfaLaserMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfgclientEdfaLaserMode.setStatus(_A)
_PmoaCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoaCfgLineStartUp=_PmoaCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,9,9,2))
_PmoatablelineStartup_ObjectIdentity=ObjectIdentity
pmoatablelineStartup=_PmoatablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,9,9,2,1))
class _PmoaCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoaCfglineEdfaLaserCtrl_Type.__name__=_G
_PmoaCfglineEdfaLaserCtrl_Object=MibScalar
pmoaCfglineEdfaLaserCtrl=_PmoaCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,9,9,2,1,2),_PmoaCfglineEdfaLaserCtrl_Type())
pmoaCfglineEdfaLaserCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoaCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoaCfglineEdfaLaserMode_Type.__name__=_G
_PmoaCfglineEdfaLaserMode_Object=MibScalar
pmoaCfglineEdfaLaserMode=_PmoaCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,9,9,2,1,3),_PmoaCfglineEdfaLaserMode_Type())
pmoaCfglineEdfaLaserMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfglineEdfaLaserMode.setStatus(_A)
_PmoaCfgLabels_ObjectIdentity=ObjectIdentity
pmoaCfgLabels=_PmoaCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,9,9,3))
_PmoaCfgLabelclientTable_Object=MibTable
pmoaCfgLabelclientTable=_PmoaCfgLabelclientTable_Object((1,3,6,1,4,1,20044,9,9,3,1))
if mibBuilder.loadTexts:pmoaCfgLabelclientTable.setStatus(_A)
_PmoaCfgLabelclientEntry_Object=MibTableRow
pmoaCfgLabelclientEntry=_PmoaCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,9,9,3,1,1))
pmoaCfgLabelclientEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pmoaCfgLabelclientEntry.setStatus(_A)
class _PmoaCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoaCfgLabelclientIndex_Type.__name__=_E
_PmoaCfgLabelclientIndex_Object=MibTableColumn
pmoaCfgLabelclientIndex=_PmoaCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,9,9,3,1,1,1),_PmoaCfgLabelclientIndex_Type())
pmoaCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaCfgLabelclientIndex.setStatus(_A)
class _PmoaCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoaCfgLabelclientPortn_Type.__name__=_H
_PmoaCfgLabelclientPortn_Object=MibTableColumn
pmoaCfgLabelclientPortn=_PmoaCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,9,9,3,1,1,3),_PmoaCfgLabelclientPortn_Type())
pmoaCfgLabelclientPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfgLabelclientPortn.setStatus(_A)
_PmoaCfgLabellineTable_Object=MibTable
pmoaCfgLabellineTable=_PmoaCfgLabellineTable_Object((1,3,6,1,4,1,20044,9,9,3,2))
if mibBuilder.loadTexts:pmoaCfgLabellineTable.setStatus(_A)
_PmoaCfgLabellineEntry_Object=MibTableRow
pmoaCfgLabellineEntry=_PmoaCfgLabellineEntry_Object((1,3,6,1,4,1,20044,9,9,3,2,1))
pmoaCfgLabellineEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pmoaCfgLabellineEntry.setStatus(_A)
class _PmoaCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoaCfgLabellineIndex_Type.__name__=_E
_PmoaCfgLabellineIndex_Object=MibTableColumn
pmoaCfgLabellineIndex=_PmoaCfgLabellineIndex_Object((1,3,6,1,4,1,20044,9,9,3,2,1,1),_PmoaCfgLabellineIndex_Type())
pmoaCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoaCfgLabellineIndex.setStatus(_A)
class _PmoaCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoaCfgLabellinePortn_Type.__name__=_H
_PmoaCfgLabellinePortn_Object=MibTableColumn
pmoaCfgLabellinePortn=_PmoaCfgLabellinePortn_Object((1,3,6,1,4,1,20044,9,9,3,2,1,3),_PmoaCfgLabellinePortn_Type())
pmoaCfgLabellinePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfgLabellinePortn.setStatus(_A)
_PmoaCfgWriteConfiguration_Type=EkiOnOff
_PmoaCfgWriteConfiguration_Object=MibScalar
pmoaCfgWriteConfiguration=_PmoaCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,9,9,257),_PmoaCfgWriteConfiguration_Type())
pmoaCfgWriteConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoaCfgWriteConfiguration.setStatus(_A)
_Pmoatraps_ObjectIdentity=ObjectIdentity
pmoatraps=_Pmoatraps_ObjectIdentity((1,3,6,1,4,1,20044,9,10))
class _PmoatrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoatrapBoardNumber_Type.__name__=_E
_PmoatrapBoardNumber_Object=MibScalar
pmoatrapBoardNumber=_PmoatrapBoardNumber_Object((1,3,6,1,4,1,20044,9,10,4),_PmoatrapBoardNumber_Type())
pmoatrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoatrapBoardNumber.setStatus(_A)
pmoaLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,30))
pmoaLineTrapNotUrgentGoesOn.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmoaLineTrapNotUrgentGoesOn.setStatus(_A)
pmoaLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,31))
pmoaLineTrapNotUrgentGoesOff.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmoaLineTrapNotUrgentGoesOff.setStatus(_A)
pmoaLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,32))
pmoaLineTrapUrgentGoesOn.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmoaLineTrapUrgentGoesOn.setStatus(_A)
pmoaLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,33))
pmoaLineTrapUrgentGoesOff.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmoaLineTrapUrgentGoesOff.setStatus(_A)
pmoaLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,34))
pmoaLineTrapCritGoesOn.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmoaLineTrapCritGoesOn.setStatus(_A)
pmoaLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,35))
pmoaLineTrapCritGoesOff.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmoaLineTrapCritGoesOff.setStatus(_A)
pmoaClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,40))
pmoaClientTrapNotUrgentGoesOn.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmoaClientTrapNotUrgentGoesOn.setStatus(_A)
pmoaClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,41))
pmoaClientTrapNotUrgentGoesOff.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmoaClientTrapNotUrgentGoesOff.setStatus(_A)
pmoaClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,42))
pmoaClientTrapUrgentGoesOn.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmoaClientTrapUrgentGoesOn.setStatus(_A)
pmoaClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,43))
pmoaClientTrapUrgentGoesOff.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmoaClientTrapUrgentGoesOff.setStatus(_A)
pmoaClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,44))
pmoaClientTrapCritGoesOn.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmoaClientTrapCritGoesOn.setStatus(_A)
pmoaClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,45))
pmoaClientTrapCritGoesOff.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmoaClientTrapCritGoesOff.setStatus(_A)
pmoaPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,9,10,50))
pmoaPowerTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmoaPowerTrapUrgentGoesOn.setStatus(_A)
pmoaPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,9,10,51))
pmoaPowerTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmoaPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PmoapreampMode':PmoapreampMode,'PmoaboosterMode':PmoaboosterMode,'modulepmoa':modulepmoa,'pmoaalarms':pmoaalarms,'pmoaAlmOther':pmoaAlmOther,'pmoaAlmOtherNurg':pmoaAlmOtherNurg,'pmoaAlmsynthAlm2':pmoaAlmsynthAlm2,'pmoaAlmConfTableSave':pmoaAlmConfTableSave,'pmoaAlmInvUpload':pmoaAlmInvUpload,'pmoaAlmConfTableLoad':pmoaAlmConfTableLoad,'pmoaAlmfoaWarnings':pmoaAlmfoaWarnings,'pmoaAlm3v3LowWarning':pmoaAlm3v3LowWarning,'pmoaAlm3v3HighWarning':pmoaAlm3v3HighWarning,'pmoaAlmTermpLowWarning':pmoaAlmTermpLowWarning,'pmoaAlmTempHighWarning':pmoaAlmTempHighWarning,'pmoaAlmOtherUrg':pmoaAlmOtherUrg,'pmoaAlmfoaAlarms':pmoaAlmfoaAlarms,'pmoaAlm3v3LowAlarm':pmoaAlm3v3LowAlarm,'pmoaAlm3v3HighAlarm':pmoaAlm3v3HighAlarm,'pmoaAlmTermpLowAlarm':pmoaAlmTermpLowAlarm,'pmoaAlmTempHighAlarm':pmoaAlmTempHighAlarm,'pmoaAlmOtherCrit':pmoaAlmOtherCrit,'pmoaAlmsynthAlm0':pmoaAlmsynthAlm0,'pmoaAlmMaintenanceMode':pmoaAlmMaintenanceMode,'pmoaAlmModGlobFail':pmoaAlmModGlobFail,'pmoaAlmUpEdfaInitNotCompl':pmoaAlmUpEdfaInitNotCompl,'pmoaAlmDwEdfaInitNotCompl':pmoaAlmDwEdfaInitNotCompl,'pmoaAlmExtPumpNotLocked':pmoaAlmExtPumpNotLocked,_R:pmoaAlmDefFuseA,_Q:pmoaAlmDefFuseB,'pmoaAlmClient':pmoaAlmClient,'pmoaAlmClientNurg':pmoaAlmClientNurg,'pmoaAlmclientEdfaWarnings':pmoaAlmclientEdfaWarnings,'pmoaAlmClientGainLowWarning':pmoaAlmClientGainLowWarning,'pmoaAlmClientGainHighWarning':pmoaAlmClientGainHighWarning,'pmoaAlmClientInputPwrLowWarning':pmoaAlmClientInputPwrLowWarning,'pmoaAlmClientInputPwrHighWarning':pmoaAlmClientInputPwrHighWarning,'pmoaAlmClientOutputPwrLowWarning':pmoaAlmClientOutputPwrLowWarning,'pmoaAlmClientOutputPwrHighWarning':pmoaAlmClientOutputPwrHighWarning,'pmoaAlmClientBiasLowWarning':pmoaAlmClientBiasLowWarning,'pmoaAlmClientBiasHighWarning':pmoaAlmClientBiasHighWarning,'pmoaAlmClientUrg':pmoaAlmClientUrg,'pmoaAlmclientEdfaAlarms1':pmoaAlmclientEdfaAlarms1,'pmoaAlmClientGainLowAlarm':pmoaAlmClientGainLowAlarm,'pmoaAlmClientGainHighAlarm':pmoaAlmClientGainHighAlarm,'pmoaAlmClientInputPwrLowAlarm':pmoaAlmClientInputPwrLowAlarm,'pmoaAlmClientInputPwrHighAlarm':pmoaAlmClientInputPwrHighAlarm,'pmoaAlmClientOutputPwrLowAlarm':pmoaAlmClientOutputPwrLowAlarm,'pmoaAlmClientOutputPwrHighAlarm':pmoaAlmClientOutputPwrHighAlarm,'pmoaAlmClientBiasLowAlarm':pmoaAlmClientBiasLowAlarm,'pmoaAlmClientBiasHighAlarm':pmoaAlmClientBiasHighAlarm,'pmoaAlmClientCrit':pmoaAlmClientCrit,'pmoaAlmsynthAlm8':pmoaAlmsynthAlm8,_P:pmoaAlmClientHwFail,'pmoaAlmClientTxOff':pmoaAlmClientTxOff,_M:pmoaAlmClientDdmWarning,_N:pmoaAlmClientDdmAlm,_O:pmoaAlmClientFail,'pmoaAlmclientEdfaAlarms2':pmoaAlmclientEdfaAlarms2,'pmoaAlmClientEdfaNr':pmoaAlmClientEdfaNr,'pmoaAlmClientEdfaTecFail':pmoaAlmClientEdfaTecFail,'pmoaAlmClientEdfaLaserFail':pmoaAlmClientEdfaLaserFail,'pmoaAlmClientEdfaLos':pmoaAlmClientEdfaLos,'pmoaAlmClientExtPumpEdfaLowCurrent':pmoaAlmClientExtPumpEdfaLowCurrent,'pmoaAlmLine':pmoaAlmLine,'pmoaAlmLineNurg':pmoaAlmLineNurg,'pmoaAlmlineEdfaWarnings':pmoaAlmlineEdfaWarnings,'pmoaAlmLineGainLowWarning':pmoaAlmLineGainLowWarning,'pmoaAlmLineGainHighWarning':pmoaAlmLineGainHighWarning,'pmoaAlmLineInputPwrLowWarning':pmoaAlmLineInputPwrLowWarning,'pmoaAlmLineInputPwrHighWarning':pmoaAlmLineInputPwrHighWarning,'pmoaAlmLineOutputPwrLowWarning':pmoaAlmLineOutputPwrLowWarning,'pmoaAlmLineOutputPwrHighWarning':pmoaAlmLineOutputPwrHighWarning,'pmoaAlmLineBiasLowWarning':pmoaAlmLineBiasLowWarning,'pmoaAlmLineBiasHighWarning':pmoaAlmLineBiasHighWarning,'pmoaAlmLineUrg':pmoaAlmLineUrg,'pmoaAlmlineEdfaAlarms1':pmoaAlmlineEdfaAlarms1,'pmoaAlmLineGainLowAlarm':pmoaAlmLineGainLowAlarm,'pmoaAlmLineGainHighAlarm':pmoaAlmLineGainHighAlarm,'pmoaAlmLineInputPwrLowAlarm':pmoaAlmLineInputPwrLowAlarm,'pmoaAlmLineInputPwrHighAlarm':pmoaAlmLineInputPwrHighAlarm,'pmoaAlmLineOutputPwrLowAlarm':pmoaAlmLineOutputPwrLowAlarm,'pmoaAlmLineOutputPwrHighAlarm':pmoaAlmLineOutputPwrHighAlarm,'pmoaAlmLineBiasLowAlarm':pmoaAlmLineBiasLowAlarm,'pmoaAlmLineBiasHighAlarm':pmoaAlmLineBiasHighAlarm,'pmoaAlmLineCrit':pmoaAlmLineCrit,'pmoaAlmsynthAlm7':pmoaAlmsynthAlm7,_L:pmoaAlmLineHwFail,'pmoaAlmLineTxOff':pmoaAlmLineTxOff,_I:pmoaAlmLineDdmWarning,_J:pmoaAlmLineDdmAlm,_K:pmoaAlmLineFail,'pmoaAlmlineEdfaAlarms2':pmoaAlmlineEdfaAlarms2,'pmoaAlmLineEdfaNr':pmoaAlmLineEdfaNr,'pmoaAlmLineEdfaTecFail':pmoaAlmLineEdfaTecFail,'pmoaAlmLineEdfaLaserFail':pmoaAlmLineEdfaLaserFail,'pmoaAlmLineEdfaLos':pmoaAlmLineEdfaLos,'pmoaAlmLineExtPumpEdfaLowCurrent':pmoaAlmLineExtPumpEdfaLowCurrent,'pmoameasures':pmoameasures,'pmoaMesrOther':pmoaMesrOther,'pmoaMesrtempMeas':pmoaMesrtempMeas,'pmoaMesr3v3Meas':pmoaMesr3v3Meas,'pmoaMesrClient':pmoaMesrClient,'pmoaMesrclientEdfaBiasMeas':pmoaMesrclientEdfaBiasMeas,'pmoaMesrclientEdfaTxpwrMeas':pmoaMesrclientEdfaTxpwrMeas,'pmoaMesrclientEdfaRxpwrMeas':pmoaMesrclientEdfaRxpwrMeas,'pmoaMesrclientEdfaGainMeas':pmoaMesrclientEdfaGainMeas,'pmoaMesrLine':pmoaMesrLine,'pmoaMesrlineEdfaBiasMeas':pmoaMesrlineEdfaBiasMeas,'pmoaMesrlineEdfaTxpwrMeas':pmoaMesrlineEdfaTxpwrMeas,'pmoaMesrlineEdfaRxpwrMeas':pmoaMesrlineEdfaRxpwrMeas,'pmoaMesrlineEdfaGainMeas':pmoaMesrlineEdfaGainMeas,'pmoacontrolsWrite':pmoacontrolsWrite,'pmoaCtrlOther':pmoaCtrlOther,'pmoaCtrlsynth0':pmoaCtrlsynth0,'pmoaCtrlConfLoad':pmoaCtrlConfLoad,'pmoaCtrlConfFlash':pmoaCtrlConfFlash,'pmoaCtrlConfClear':pmoaCtrlConfClear,'pmoaCtrlswMgnt':pmoaCtrlswMgnt,'pmoaCtrlColdReset':pmoaCtrlColdReset,'pmoaCtrlWarmReset':pmoaCtrlWarmReset,'pmoaCtrlpowerDown':pmoaCtrlpowerDown,'pmoaCtrlSoftPowerDown':pmoaCtrlSoftPowerDown,'pmoaCtrlledTest':pmoaCtrlledTest,'pmoaCtrlGreenLed':pmoaCtrlGreenLed,'pmoaCtrlRedLed':pmoaCtrlRedLed,'pmoaCtrlLedOff':pmoaCtrlLedOff,'pmoaCtrlmaintMode':pmoaCtrlmaintMode,'pmoaCtrlMaintenance':pmoaCtrlMaintenance,'pmoaCtrlClient':pmoaCtrlClient,'pmoaCtrlclientEdfaLaserOff':pmoaCtrlclientEdfaLaserOff,'pmoaCtrlClientEdfaLaserOff':pmoaCtrlClientEdfaLaserOff,'pmoaCtrlclientEdfaMode':pmoaCtrlclientEdfaMode,'pmoaCtrlclientIlasSettingValue':pmoaCtrlclientIlasSettingValue,'pmoaCtrlclientPlasSettingValue':pmoaCtrlclientPlasSettingValue,'pmoaCtrlclientGainSettingValue':pmoaCtrlclientGainSettingValue,'pmoaCtrlclientEffPwrOutSettingValue':pmoaCtrlclientEffPwrOutSettingValue,'pmoaCtrlLine':pmoaCtrlLine,'pmoaCtrllineEdfaLaserOff':pmoaCtrllineEdfaLaserOff,'pmoaCtrlLineEdfaLaserOff':pmoaCtrlLineEdfaLaserOff,'pmoaCtrllineEdfaMode':pmoaCtrllineEdfaMode,'pmoaCtrllineIlasSettingValue':pmoaCtrllineIlasSettingValue,'pmoaCtrllinePlasSettingValue':pmoaCtrllinePlasSettingValue,'pmoaCtrllineGainSettingValue':pmoaCtrllineGainSettingValue,'pmoaCtrllineEffPwrOutSettingValue':pmoaCtrllineEffPwrOutSettingValue,'pmoari':pmoari,'pmoaRinvReloadInventory':pmoaRinvReloadInventory,'pmoaRinvModulePlatform':pmoaRinvModulePlatform,'pmoaRinvSwPlatform':pmoaRinvSwPlatform,'pmoaRinvSwFoa':pmoaRinvSwFoa,'pmoaRinvBoosterTable':pmoaRinvBoosterTable,'pmoaRinvBoosterEntry':pmoaRinvBoosterEntry,_S:pmoaRinvBoosterIndex,'pmoaRinvBooster':pmoaRinvBooster,'pmoaRinvPreAmpTable':pmoaRinvPreAmpTable,'pmoaRinvPreAmpEntry':pmoaRinvPreAmpEntry,_T:pmoaRinvPreAmpIndex,'pmoaRinvPreAmp':pmoaRinvPreAmp,'pmoaConfig':pmoaConfig,'pmoaCfgNoValue':pmoaCfgNoValue,'pmoatableclientStartup':pmoatableclientStartup,'pmoaCfgclientEdfaLaserCtrl':pmoaCfgclientEdfaLaserCtrl,'pmoaCfgclientEdfaLaserMode':pmoaCfgclientEdfaLaserMode,'pmoaCfgLineStartUp':pmoaCfgLineStartUp,'pmoatablelineStartup':pmoatablelineStartup,'pmoaCfglineEdfaLaserCtrl':pmoaCfglineEdfaLaserCtrl,'pmoaCfglineEdfaLaserMode':pmoaCfglineEdfaLaserMode,'pmoaCfgLabels':pmoaCfgLabels,'pmoaCfgLabelclientTable':pmoaCfgLabelclientTable,'pmoaCfgLabelclientEntry':pmoaCfgLabelclientEntry,_U:pmoaCfgLabelclientIndex,'pmoaCfgLabelclientPortn':pmoaCfgLabelclientPortn,'pmoaCfgLabellineTable':pmoaCfgLabellineTable,'pmoaCfgLabellineEntry':pmoaCfgLabellineEntry,_V:pmoaCfgLabellineIndex,'pmoaCfgLabellinePortn':pmoaCfgLabellinePortn,'pmoaCfgWriteConfiguration':pmoaCfgWriteConfiguration,'pmoatraps':pmoatraps,_F:pmoatrapBoardNumber,'pmoaLineTrapNotUrgentGoesOn':pmoaLineTrapNotUrgentGoesOn,'pmoaLineTrapNotUrgentGoesOff':pmoaLineTrapNotUrgentGoesOff,'pmoaLineTrapUrgentGoesOn':pmoaLineTrapUrgentGoesOn,'pmoaLineTrapUrgentGoesOff':pmoaLineTrapUrgentGoesOff,'pmoaLineTrapCritGoesOn':pmoaLineTrapCritGoesOn,'pmoaLineTrapCritGoesOff':pmoaLineTrapCritGoesOff,'pmoaClientTrapNotUrgentGoesOn':pmoaClientTrapNotUrgentGoesOn,'pmoaClientTrapNotUrgentGoesOff':pmoaClientTrapNotUrgentGoesOff,'pmoaClientTrapUrgentGoesOn':pmoaClientTrapUrgentGoesOn,'pmoaClientTrapUrgentGoesOff':pmoaClientTrapUrgentGoesOff,'pmoaClientTrapCritGoesOn':pmoaClientTrapCritGoesOn,'pmoaClientTrapCritGoesOff':pmoaClientTrapCritGoesOff,'pmoaPowerTrapUrgentGoesOn':pmoaPowerTrapUrgentGoesOn,'pmoaPowerTrapUrgentGoesOff':pmoaPowerTrapUrgentGoesOff})