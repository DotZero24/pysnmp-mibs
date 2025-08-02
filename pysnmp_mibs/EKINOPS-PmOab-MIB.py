_U='pmoabCfgLabellineIndex'
_T='pmoabCfgLabelclientIndex'
_S='pmoabRinvBoosterIndex'
_R='pmoabAlmDefFuseA'
_Q='pmoabAlmDefFuseB'
_P='pmoabAlmClientHwFail'
_O='pmoabAlmClientFail'
_N='pmoabAlmClientDdmAlm'
_M='pmoabAlmClientDdmWarning'
_L='pmoabAlmLineHwFail'
_K='pmoabAlmLineFail'
_J='pmoabAlmLineDdmAlm'
_I='pmoabAlmLineDdmWarning'
_H='DisplayString'
_G='Unsigned32'
_F='pmoabtrapBoardNumber'
_E='Integer32'
_D='read-write'
_C='EKINOPS-PmOab-MIB'
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
modulepmoab=ModuleIdentity((1,3,6,1,4,1,20044,23))
if mibBuilder.loadTexts:modulepmoab.setRevisions(('2007-02-07 00:00','2007-07-06 00:00','2007-11-21 00:00','2009-04-15 00:00','2009-09-21 00:00','2009-12-14 00:00','2010-02-25 00:00','2010-07-15 00:00','2010-10-29 00:00','2010-11-03 00:00','2012-07-04 00:00','2014-03-26 00:00','2014-12-10 00:00','2016-05-23 00:00'))
class PmoabboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oaboosterdefaultmode',0),('oaboosterconstantcurrentmode',1),('oaboosterconstantpowermode',2)))
_Pmoabalarms_ObjectIdentity=ObjectIdentity
pmoabalarms=_Pmoabalarms_ObjectIdentity((1,3,6,1,4,1,20044,23,2))
_PmoabAlmOther_ObjectIdentity=ObjectIdentity
pmoabAlmOther=_PmoabAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1))
_PmoabAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoabAlmOtherNurg=_PmoabAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,1))
_PmoabAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoabAlmsynthAlm2=_PmoabAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,1,2))
_PmoabAlmConfTableSave_Type=EkiOnOff
_PmoabAlmConfTableSave_Object=MibScalar
pmoabAlmConfTableSave=_PmoabAlmConfTableSave_Object((1,3,6,1,4,1,20044,23,2,1,1,2,1),_PmoabAlmConfTableSave_Type())
pmoabAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmConfTableSave.setStatus(_A)
_PmoabAlmInvUpload_Type=EkiOnOff
_PmoabAlmInvUpload_Object=MibScalar
pmoabAlmInvUpload=_PmoabAlmInvUpload_Object((1,3,6,1,4,1,20044,23,2,1,1,2,2),_PmoabAlmInvUpload_Type())
pmoabAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmInvUpload.setStatus(_A)
_PmoabAlmConfTableLoad_Type=EkiOnOff
_PmoabAlmConfTableLoad_Object=MibScalar
pmoabAlmConfTableLoad=_PmoabAlmConfTableLoad_Object((1,3,6,1,4,1,20044,23,2,1,1,2,3),_PmoabAlmConfTableLoad_Type())
pmoabAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmConfTableLoad.setStatus(_A)
_PmoabAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoabAlmfoaWarnings=_PmoabAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,1,75))
_PmoabAlm3v3LowWarning_Type=EkiOnOff
_PmoabAlm3v3LowWarning_Object=MibScalar
pmoabAlm3v3LowWarning=_PmoabAlm3v3LowWarning_Object((1,3,6,1,4,1,20044,23,2,1,1,75,5),_PmoabAlm3v3LowWarning_Type())
pmoabAlm3v3LowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlm3v3LowWarning.setStatus(_A)
_PmoabAlm3v3HighWarning_Type=EkiOnOff
_PmoabAlm3v3HighWarning_Object=MibScalar
pmoabAlm3v3HighWarning=_PmoabAlm3v3HighWarning_Object((1,3,6,1,4,1,20044,23,2,1,1,75,6),_PmoabAlm3v3HighWarning_Type())
pmoabAlm3v3HighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlm3v3HighWarning.setStatus(_A)
_PmoabAlmTermpLowWarning_Type=EkiOnOff
_PmoabAlmTermpLowWarning_Object=MibScalar
pmoabAlmTermpLowWarning=_PmoabAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,23,2,1,1,75,7),_PmoabAlmTermpLowWarning_Type())
pmoabAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmTermpLowWarning.setStatus(_A)
_PmoabAlmTempHighWarning_Type=EkiOnOff
_PmoabAlmTempHighWarning_Object=MibScalar
pmoabAlmTempHighWarning=_PmoabAlmTempHighWarning_Object((1,3,6,1,4,1,20044,23,2,1,1,75,8),_PmoabAlmTempHighWarning_Type())
pmoabAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmTempHighWarning.setStatus(_A)
_PmoabAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoabAlmOtherUrg=_PmoabAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,2))
_PmoabAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoabAlmfoaAlarms=_PmoabAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,2,74))
_PmoabAlm3v3LowAlarm_Type=EkiOnOff
_PmoabAlm3v3LowAlarm_Object=MibScalar
pmoabAlm3v3LowAlarm=_PmoabAlm3v3LowAlarm_Object((1,3,6,1,4,1,20044,23,2,1,2,74,5),_PmoabAlm3v3LowAlarm_Type())
pmoabAlm3v3LowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlm3v3LowAlarm.setStatus(_A)
_PmoabAlm3v3HighAlarm_Type=EkiOnOff
_PmoabAlm3v3HighAlarm_Object=MibScalar
pmoabAlm3v3HighAlarm=_PmoabAlm3v3HighAlarm_Object((1,3,6,1,4,1,20044,23,2,1,2,74,6),_PmoabAlm3v3HighAlarm_Type())
pmoabAlm3v3HighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlm3v3HighAlarm.setStatus(_A)
_PmoabAlmTermpLowAlarm_Type=EkiOnOff
_PmoabAlmTermpLowAlarm_Object=MibScalar
pmoabAlmTermpLowAlarm=_PmoabAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,23,2,1,2,74,7),_PmoabAlmTermpLowAlarm_Type())
pmoabAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmTermpLowAlarm.setStatus(_A)
_PmoabAlmTempHighAlarm_Type=EkiOnOff
_PmoabAlmTempHighAlarm_Object=MibScalar
pmoabAlmTempHighAlarm=_PmoabAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,23,2,1,2,74,8),_PmoabAlmTempHighAlarm_Type())
pmoabAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmTempHighAlarm.setStatus(_A)
_PmoabAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoabAlmOtherCrit=_PmoabAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,3))
_PmoabAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoabAlmsynthAlm0=_PmoabAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,23,2,1,3,0))
_PmoabAlmMaintenanceMode_Type=EkiOnOff
_PmoabAlmMaintenanceMode_Object=MibScalar
pmoabAlmMaintenanceMode=_PmoabAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,23,2,1,3,0,1),_PmoabAlmMaintenanceMode_Type())
pmoabAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmMaintenanceMode.setStatus(_A)
_PmoabAlmModGlobFail_Type=EkiOnOff
_PmoabAlmModGlobFail_Object=MibScalar
pmoabAlmModGlobFail=_PmoabAlmModGlobFail_Object((1,3,6,1,4,1,20044,23,2,1,3,0,9),_PmoabAlmModGlobFail_Type())
pmoabAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmModGlobFail.setStatus(_A)
_PmoabAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoabAlmUpEdfaInitNotCompl_Object=MibScalar
pmoabAlmUpEdfaInitNotCompl=_PmoabAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,23,2,1,3,0,10),_PmoabAlmUpEdfaInitNotCompl_Type())
pmoabAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoabAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoabAlmDwEdfaInitNotCompl_Object=MibScalar
pmoabAlmDwEdfaInitNotCompl=_PmoabAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,23,2,1,3,0,11),_PmoabAlmDwEdfaInitNotCompl_Type())
pmoabAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoabAlmExtPumpNotLocked_Type=EkiOnOff
_PmoabAlmExtPumpNotLocked_Object=MibScalar
pmoabAlmExtPumpNotLocked=_PmoabAlmExtPumpNotLocked_Object((1,3,6,1,4,1,20044,23,2,1,3,0,12),_PmoabAlmExtPumpNotLocked_Type())
pmoabAlmExtPumpNotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmExtPumpNotLocked.setStatus(_A)
_PmoabAlmDefFuseA_Type=EkiOnOff
_PmoabAlmDefFuseA_Object=MibScalar
pmoabAlmDefFuseA=_PmoabAlmDefFuseA_Object((1,3,6,1,4,1,20044,23,2,1,3,0,15),_PmoabAlmDefFuseA_Type())
pmoabAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmDefFuseA.setStatus(_A)
_PmoabAlmDefFuseB_Type=EkiOnOff
_PmoabAlmDefFuseB_Object=MibScalar
pmoabAlmDefFuseB=_PmoabAlmDefFuseB_Object((1,3,6,1,4,1,20044,23,2,1,3,0,16),_PmoabAlmDefFuseB_Type())
pmoabAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmDefFuseB.setStatus(_A)
_PmoabAlmClient_ObjectIdentity=ObjectIdentity
pmoabAlmClient=_PmoabAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2))
_PmoabAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoabAlmClientNurg=_PmoabAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,1))
_PmoabAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoabAlmclientEdfaWarnings=_PmoabAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,1,33))
_PmoabAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoabAlmClientInputPwrLowWarning_Object=MibScalar
pmoabAlmClientInputPwrLowWarning=_PmoabAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,23,2,2,1,33,3),_PmoabAlmClientInputPwrLowWarning_Type())
pmoabAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientInputPwrLowWarning.setStatus(_A)
_PmoabAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoabAlmClientInputPwrHighWarning_Object=MibScalar
pmoabAlmClientInputPwrHighWarning=_PmoabAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,23,2,2,1,33,4),_PmoabAlmClientInputPwrHighWarning_Type())
pmoabAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientInputPwrHighWarning.setStatus(_A)
_PmoabAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoabAlmClientUrg=_PmoabAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,2))
_PmoabAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoabAlmclientEdfaAlarms1=_PmoabAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,2,32))
_PmoabAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoabAlmClientInputPwrLowAlarm_Object=MibScalar
pmoabAlmClientInputPwrLowAlarm=_PmoabAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,23,2,2,2,32,3),_PmoabAlmClientInputPwrLowAlarm_Type())
pmoabAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoabAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoabAlmClientInputPwrHighAlarm_Object=MibScalar
pmoabAlmClientInputPwrHighAlarm=_PmoabAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,23,2,2,2,32,4),_PmoabAlmClientInputPwrHighAlarm_Type())
pmoabAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoabAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoabAlmClientCrit=_PmoabAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,3))
_PmoabAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoabAlmsynthAlm8=_PmoabAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,3,8))
_PmoabAlmClientHwFail_Type=EkiOnOff
_PmoabAlmClientHwFail_Object=MibScalar
pmoabAlmClientHwFail=_PmoabAlmClientHwFail_Object((1,3,6,1,4,1,20044,23,2,2,3,8,4),_PmoabAlmClientHwFail_Type())
pmoabAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientHwFail.setStatus(_A)
_PmoabAlmClientDdmWarning_Type=EkiOnOff
_PmoabAlmClientDdmWarning_Object=MibScalar
pmoabAlmClientDdmWarning=_PmoabAlmClientDdmWarning_Object((1,3,6,1,4,1,20044,23,2,2,3,8,9),_PmoabAlmClientDdmWarning_Type())
pmoabAlmClientDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientDdmWarning.setStatus(_A)
_PmoabAlmClientDdmAlm_Type=EkiOnOff
_PmoabAlmClientDdmAlm_Object=MibScalar
pmoabAlmClientDdmAlm=_PmoabAlmClientDdmAlm_Object((1,3,6,1,4,1,20044,23,2,2,3,8,10),_PmoabAlmClientDdmAlm_Type())
pmoabAlmClientDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientDdmAlm.setStatus(_A)
_PmoabAlmClientFail_Type=EkiOnOff
_PmoabAlmClientFail_Object=MibScalar
pmoabAlmClientFail=_PmoabAlmClientFail_Object((1,3,6,1,4,1,20044,23,2,2,3,8,12),_PmoabAlmClientFail_Type())
pmoabAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientFail.setStatus(_A)
_PmoabAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoabAlmclientEdfaAlarms2=_PmoabAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,23,2,2,3,35))
_PmoabAlmClientEdfaLos_Type=EkiOnOff
_PmoabAlmClientEdfaLos_Object=MibScalar
pmoabAlmClientEdfaLos=_PmoabAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,23,2,2,3,35,4),_PmoabAlmClientEdfaLos_Type())
pmoabAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmClientEdfaLos.setStatus(_A)
_PmoabAlmLine_ObjectIdentity=ObjectIdentity
pmoabAlmLine=_PmoabAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3))
_PmoabAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoabAlmLineNurg=_PmoabAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,1))
_PmoabAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoabAlmlineEdfaWarnings=_PmoabAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,1,41))
_PmoabAlmLineGainLowWarning_Type=EkiOnOff
_PmoabAlmLineGainLowWarning_Object=MibScalar
pmoabAlmLineGainLowWarning=_PmoabAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,23,2,3,1,41,1),_PmoabAlmLineGainLowWarning_Type())
pmoabAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineGainLowWarning.setStatus(_A)
_PmoabAlmLineGainHighWarning_Type=EkiOnOff
_PmoabAlmLineGainHighWarning_Object=MibScalar
pmoabAlmLineGainHighWarning=_PmoabAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,23,2,3,1,41,2),_PmoabAlmLineGainHighWarning_Type())
pmoabAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineGainHighWarning.setStatus(_A)
_PmoabAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoabAlmLineOutputPwrLowWarning_Object=MibScalar
pmoabAlmLineOutputPwrLowWarning=_PmoabAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,23,2,3,1,41,5),_PmoabAlmLineOutputPwrLowWarning_Type())
pmoabAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoabAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoabAlmLineOutputPwrHighWarning_Object=MibScalar
pmoabAlmLineOutputPwrHighWarning=_PmoabAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,23,2,3,1,41,6),_PmoabAlmLineOutputPwrHighWarning_Type())
pmoabAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoabAlmLineBiasLowWarning_Type=EkiOnOff
_PmoabAlmLineBiasLowWarning_Object=MibScalar
pmoabAlmLineBiasLowWarning=_PmoabAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,23,2,3,1,41,7),_PmoabAlmLineBiasLowWarning_Type())
pmoabAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineBiasLowWarning.setStatus(_A)
_PmoabAlmLineBiasHighWarning_Type=EkiOnOff
_PmoabAlmLineBiasHighWarning_Object=MibScalar
pmoabAlmLineBiasHighWarning=_PmoabAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,23,2,3,1,41,8),_PmoabAlmLineBiasHighWarning_Type())
pmoabAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineBiasHighWarning.setStatus(_A)
_PmoabAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoabAlmLineUrg=_PmoabAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,2))
_PmoabAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoabAlmlineEdfaAlarms1=_PmoabAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,2,40))
_PmoabAlmLineGainLowAlarm_Type=EkiOnOff
_PmoabAlmLineGainLowAlarm_Object=MibScalar
pmoabAlmLineGainLowAlarm=_PmoabAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,23,2,3,2,40,1),_PmoabAlmLineGainLowAlarm_Type())
pmoabAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineGainLowAlarm.setStatus(_A)
_PmoabAlmLineGainHighAlarm_Type=EkiOnOff
_PmoabAlmLineGainHighAlarm_Object=MibScalar
pmoabAlmLineGainHighAlarm=_PmoabAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,23,2,3,2,40,2),_PmoabAlmLineGainHighAlarm_Type())
pmoabAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineGainHighAlarm.setStatus(_A)
_PmoabAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoabAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoabAlmLineOutputPwrLowAlarm=_PmoabAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,23,2,3,2,40,5),_PmoabAlmLineOutputPwrLowAlarm_Type())
pmoabAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoabAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoabAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoabAlmLineOutputPwrHighAlarm=_PmoabAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,23,2,3,2,40,6),_PmoabAlmLineOutputPwrHighAlarm_Type())
pmoabAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoabAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoabAlmLineBiasLowAlarm_Object=MibScalar
pmoabAlmLineBiasLowAlarm=_PmoabAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,23,2,3,2,40,7),_PmoabAlmLineBiasLowAlarm_Type())
pmoabAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineBiasLowAlarm.setStatus(_A)
_PmoabAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoabAlmLineBiasHighAlarm_Object=MibScalar
pmoabAlmLineBiasHighAlarm=_PmoabAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,23,2,3,2,40,8),_PmoabAlmLineBiasHighAlarm_Type())
pmoabAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineBiasHighAlarm.setStatus(_A)
_PmoabAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoabAlmLineCrit=_PmoabAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,3))
_PmoabAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoabAlmsynthAlm7=_PmoabAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,3,7))
_PmoabAlmLineHwFail_Type=EkiOnOff
_PmoabAlmLineHwFail_Object=MibScalar
pmoabAlmLineHwFail=_PmoabAlmLineHwFail_Object((1,3,6,1,4,1,20044,23,2,3,3,7,4),_PmoabAlmLineHwFail_Type())
pmoabAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineHwFail.setStatus(_A)
_PmoabAlmLineTxOff_Type=EkiOnOff
_PmoabAlmLineTxOff_Object=MibScalar
pmoabAlmLineTxOff=_PmoabAlmLineTxOff_Object((1,3,6,1,4,1,20044,23,2,3,3,7,5),_PmoabAlmLineTxOff_Type())
pmoabAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineTxOff.setStatus(_A)
_PmoabAlmLineDdmWarning_Type=EkiOnOff
_PmoabAlmLineDdmWarning_Object=MibScalar
pmoabAlmLineDdmWarning=_PmoabAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,23,2,3,3,7,9),_PmoabAlmLineDdmWarning_Type())
pmoabAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineDdmWarning.setStatus(_A)
_PmoabAlmLineDdmAlm_Type=EkiOnOff
_PmoabAlmLineDdmAlm_Object=MibScalar
pmoabAlmLineDdmAlm=_PmoabAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,23,2,3,3,7,10),_PmoabAlmLineDdmAlm_Type())
pmoabAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineDdmAlm.setStatus(_A)
_PmoabAlmLineFail_Type=EkiOnOff
_PmoabAlmLineFail_Object=MibScalar
pmoabAlmLineFail=_PmoabAlmLineFail_Object((1,3,6,1,4,1,20044,23,2,3,3,7,12),_PmoabAlmLineFail_Type())
pmoabAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineFail.setStatus(_A)
_PmoabAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoabAlmlineEdfaAlarms2=_PmoabAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,23,2,3,3,43))
_PmoabAlmLineEdfaNr_Type=EkiOnOff
_PmoabAlmLineEdfaNr_Object=MibScalar
pmoabAlmLineEdfaNr=_PmoabAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,23,2,3,3,43,1),_PmoabAlmLineEdfaNr_Type())
pmoabAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineEdfaNr.setStatus(_A)
_PmoabAlmLineEdfaTecFail_Type=EkiOnOff
_PmoabAlmLineEdfaTecFail_Object=MibScalar
pmoabAlmLineEdfaTecFail=_PmoabAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,23,2,3,3,43,2),_PmoabAlmLineEdfaTecFail_Type())
pmoabAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineEdfaTecFail.setStatus(_A)
_PmoabAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoabAlmLineEdfaLaserFail_Object=MibScalar
pmoabAlmLineEdfaLaserFail=_PmoabAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,23,2,3,3,43,3),_PmoabAlmLineEdfaLaserFail_Type())
pmoabAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineEdfaLaserFail.setStatus(_A)
_PmoabAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoabAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoabAlmLineExtPumpEdfaLowCurrent=_PmoabAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,23,2,3,3,43,5),_PmoabAlmLineExtPumpEdfaLowCurrent_Type())
pmoabAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_Pmoabmeasures_ObjectIdentity=ObjectIdentity
pmoabmeasures=_Pmoabmeasures_ObjectIdentity((1,3,6,1,4,1,20044,23,3))
_PmoabMesrOther_ObjectIdentity=ObjectIdentity
pmoabMesrOther=_PmoabMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,23,3,1))
class _PmoabMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabMesrtempMeas_Type.__name__=_E
_PmoabMesrtempMeas_Object=MibScalar
pmoabMesrtempMeas=_PmoabMesrtempMeas_Object((1,3,6,1,4,1,20044,23,3,1,72),_PmoabMesrtempMeas_Type())
pmoabMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabMesrtempMeas.setStatus(_A)
class _PmoabMesr3v3Meas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabMesr3v3Meas_Type.__name__=_E
_PmoabMesr3v3Meas_Object=MibScalar
pmoabMesr3v3Meas=_PmoabMesr3v3Meas_Object((1,3,6,1,4,1,20044,23,3,1,73),_PmoabMesr3v3Meas_Type())
pmoabMesr3v3Meas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabMesr3v3Meas.setStatus(_A)
_PmoabMesrClient_ObjectIdentity=ObjectIdentity
pmoabMesrClient=_PmoabMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,23,3,2))
class _PmoabMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabMesrclientEdfaRxpwrMeas_Type.__name__=_E
_PmoabMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoabMesrclientEdfaRxpwrMeas=_PmoabMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,23,3,2,34),_PmoabMesrclientEdfaRxpwrMeas_Type())
pmoabMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabMesrclientEdfaRxpwrMeas.setStatus(_A)
_PmoabMesrLine_ObjectIdentity=ObjectIdentity
pmoabMesrLine=_PmoabMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,23,3,3))
class _PmoabMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabMesrlineEdfaBiasMeas_Type.__name__=_E
_PmoabMesrlineEdfaBiasMeas_Object=MibScalar
pmoabMesrlineEdfaBiasMeas=_PmoabMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,23,3,3,40),_PmoabMesrlineEdfaBiasMeas_Type())
pmoabMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoabMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabMesrlineEdfaTxpwrMeas_Type.__name__=_E
_PmoabMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoabMesrlineEdfaTxpwrMeas=_PmoabMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,23,3,3,41),_PmoabMesrlineEdfaTxpwrMeas_Type())
pmoabMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoabMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabMesrlineEdfaGainMeas_Type.__name__=_E
_PmoabMesrlineEdfaGainMeas_Object=MibScalar
pmoabMesrlineEdfaGainMeas=_PmoabMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,23,3,3,43),_PmoabMesrlineEdfaGainMeas_Type())
pmoabMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabMesrlineEdfaGainMeas.setStatus(_A)
_PmoabcontrolsWrite_ObjectIdentity=ObjectIdentity
pmoabcontrolsWrite=_PmoabcontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,23,6))
_PmoabCtrlOther_ObjectIdentity=ObjectIdentity
pmoabCtrlOther=_PmoabCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,23,6,1))
_PmoabCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoabCtrlsynth0=_PmoabCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,23,6,1,0))
_PmoabCtrlConfLoad_Type=EkiOnOff
_PmoabCtrlConfLoad_Object=MibScalar
pmoabCtrlConfLoad=_PmoabCtrlConfLoad_Object((1,3,6,1,4,1,20044,23,6,1,0,1),_PmoabCtrlConfLoad_Type())
pmoabCtrlConfLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlConfLoad.setStatus(_A)
_PmoabCtrlConfFlash_Type=EkiOnOff
_PmoabCtrlConfFlash_Object=MibScalar
pmoabCtrlConfFlash=_PmoabCtrlConfFlash_Object((1,3,6,1,4,1,20044,23,6,1,0,9),_PmoabCtrlConfFlash_Type())
pmoabCtrlConfFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlConfFlash.setStatus(_A)
_PmoabCtrlConfClear_Type=EkiOnOff
_PmoabCtrlConfClear_Object=MibScalar
pmoabCtrlConfClear=_PmoabCtrlConfClear_Object((1,3,6,1,4,1,20044,23,6,1,0,13),_PmoabCtrlConfClear_Type())
pmoabCtrlConfClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlConfClear.setStatus(_A)
_PmoabCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoabCtrlswMgnt=_PmoabCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,23,6,1,5))
_PmoabCtrlColdReset_Type=EkiOnOff
_PmoabCtrlColdReset_Object=MibScalar
pmoabCtrlColdReset=_PmoabCtrlColdReset_Object((1,3,6,1,4,1,20044,23,6,1,5,2),_PmoabCtrlColdReset_Type())
pmoabCtrlColdReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlColdReset.setStatus(_A)
_PmoabCtrlWarmReset_Type=EkiOnOff
_PmoabCtrlWarmReset_Object=MibScalar
pmoabCtrlWarmReset=_PmoabCtrlWarmReset_Object((1,3,6,1,4,1,20044,23,6,1,5,3),_PmoabCtrlWarmReset_Type())
pmoabCtrlWarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlWarmReset.setStatus(_A)
_PmoabCtrlpowerDown_ObjectIdentity=ObjectIdentity
pmoabCtrlpowerDown=_PmoabCtrlpowerDown_ObjectIdentity((1,3,6,1,4,1,20044,23,6,1,72))
_PmoabCtrlSoftPowerDown_Type=EkiOnOff
_PmoabCtrlSoftPowerDown_Object=MibScalar
pmoabCtrlSoftPowerDown=_PmoabCtrlSoftPowerDown_Object((1,3,6,1,4,1,20044,23,6,1,72,1),_PmoabCtrlSoftPowerDown_Type())
pmoabCtrlSoftPowerDown.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlSoftPowerDown.setStatus(_A)
_PmoabCtrlledTest_ObjectIdentity=ObjectIdentity
pmoabCtrlledTest=_PmoabCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,23,6,1,73))
_PmoabCtrlGreenLed_Type=EkiOnOff
_PmoabCtrlGreenLed_Object=MibScalar
pmoabCtrlGreenLed=_PmoabCtrlGreenLed_Object((1,3,6,1,4,1,20044,23,6,1,73,1),_PmoabCtrlGreenLed_Type())
pmoabCtrlGreenLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlGreenLed.setStatus(_A)
_PmoabCtrlRedLed_Type=EkiOnOff
_PmoabCtrlRedLed_Object=MibScalar
pmoabCtrlRedLed=_PmoabCtrlRedLed_Object((1,3,6,1,4,1,20044,23,6,1,73,2),_PmoabCtrlRedLed_Type())
pmoabCtrlRedLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlRedLed.setStatus(_A)
_PmoabCtrlLedOff_Type=EkiOnOff
_PmoabCtrlLedOff_Object=MibScalar
pmoabCtrlLedOff=_PmoabCtrlLedOff_Object((1,3,6,1,4,1,20044,23,6,1,73,3),_PmoabCtrlLedOff_Type())
pmoabCtrlLedOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlLedOff.setStatus(_A)
_PmoabCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoabCtrlmaintMode=_PmoabCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,23,6,1,75))
_PmoabCtrlMaintenance_Type=EkiOnOff
_PmoabCtrlMaintenance_Object=MibScalar
pmoabCtrlMaintenance=_PmoabCtrlMaintenance_Object((1,3,6,1,4,1,20044,23,6,1,75,1),_PmoabCtrlMaintenance_Type())
pmoabCtrlMaintenance.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlMaintenance.setStatus(_A)
_PmoabCtrlClient_ObjectIdentity=ObjectIdentity
pmoabCtrlClient=_PmoabCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,23,6,2))
_PmoabCtrlLine_ObjectIdentity=ObjectIdentity
pmoabCtrlLine=_PmoabCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,23,6,3))
_PmoabCtrllineEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoabCtrllineEdfaLaserOff=_PmoabCtrllineEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,23,6,3,40))
_PmoabCtrlLineEdfaLaserOff_Type=EkiOnOff
_PmoabCtrlLineEdfaLaserOff_Object=MibScalar
pmoabCtrlLineEdfaLaserOff=_PmoabCtrlLineEdfaLaserOff_Object((1,3,6,1,4,1,20044,23,6,3,40,1),_PmoabCtrlLineEdfaLaserOff_Type())
pmoabCtrlLineEdfaLaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrlLineEdfaLaserOff.setStatus(_A)
_PmoabCtrllineEdfaMode_Type=PmoabboosterMode
_PmoabCtrllineEdfaMode_Object=MibScalar
pmoabCtrllineEdfaMode=_PmoabCtrllineEdfaMode_Object((1,3,6,1,4,1,20044,23,6,3,41),_PmoabCtrllineEdfaMode_Type())
pmoabCtrllineEdfaMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrllineEdfaMode.setStatus(_A)
class _PmoabCtrllineIlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabCtrllineIlasSettingValue_Type.__name__=_E
_PmoabCtrllineIlasSettingValue_Object=MibScalar
pmoabCtrllineIlasSettingValue=_PmoabCtrllineIlasSettingValue_Object((1,3,6,1,4,1,20044,23,6,3,42),_PmoabCtrllineIlasSettingValue_Type())
pmoabCtrllineIlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrllineIlasSettingValue.setStatus(_A)
class _PmoabCtrllinePlasSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabCtrllinePlasSettingValue_Type.__name__=_E
_PmoabCtrllinePlasSettingValue_Object=MibScalar
pmoabCtrllinePlasSettingValue=_PmoabCtrllinePlasSettingValue_Object((1,3,6,1,4,1,20044,23,6,3,43),_PmoabCtrllinePlasSettingValue_Type())
pmoabCtrllinePlasSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrllinePlasSettingValue.setStatus(_A)
class _PmoabCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabCtrllineGainSettingValue_Type.__name__=_E
_PmoabCtrllineGainSettingValue_Object=MibScalar
pmoabCtrllineGainSettingValue=_PmoabCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,23,6,3,44),_PmoabCtrllineGainSettingValue_Type())
pmoabCtrllineGainSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrllineGainSettingValue.setStatus(_A)
class _PmoabCtrllineEffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabCtrllineEffPwrOutSettingValue_Type.__name__=_E
_PmoabCtrllineEffPwrOutSettingValue_Object=MibScalar
pmoabCtrllineEffPwrOutSettingValue=_PmoabCtrllineEffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,23,6,3,45),_PmoabCtrllineEffPwrOutSettingValue_Type())
pmoabCtrllineEffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCtrllineEffPwrOutSettingValue.setStatus(_A)
_Pmoabri_ObjectIdentity=ObjectIdentity
pmoabri=_Pmoabri_ObjectIdentity((1,3,6,1,4,1,20044,23,7))
_PmoabRinvReloadInventory_Type=EkiOnOff
_PmoabRinvReloadInventory_Object=MibScalar
pmoabRinvReloadInventory=_PmoabRinvReloadInventory_Object((1,3,6,1,4,1,20044,23,7,2),_PmoabRinvReloadInventory_Type())
pmoabRinvReloadInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabRinvReloadInventory.setStatus(_A)
_PmoabRinvModulePlatform_Type=DisplayString
_PmoabRinvModulePlatform_Object=MibScalar
pmoabRinvModulePlatform=_PmoabRinvModulePlatform_Object((1,3,6,1,4,1,20044,23,7,3),_PmoabRinvModulePlatform_Type())
pmoabRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabRinvModulePlatform.setStatus(_A)
_PmoabRinvSwPlatform_Type=DisplayString
_PmoabRinvSwPlatform_Object=MibScalar
pmoabRinvSwPlatform=_PmoabRinvSwPlatform_Object((1,3,6,1,4,1,20044,23,7,4),_PmoabRinvSwPlatform_Type())
pmoabRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabRinvSwPlatform.setStatus(_A)
_PmoabRinvSwFoa_Type=DisplayString
_PmoabRinvSwFoa_Object=MibScalar
pmoabRinvSwFoa=_PmoabRinvSwFoa_Object((1,3,6,1,4,1,20044,23,7,5),_PmoabRinvSwFoa_Type())
pmoabRinvSwFoa.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabRinvSwFoa.setStatus(_A)
_PmoabRinvBoosterTable_Object=MibTable
pmoabRinvBoosterTable=_PmoabRinvBoosterTable_Object((1,3,6,1,4,1,20044,23,7,6))
if mibBuilder.loadTexts:pmoabRinvBoosterTable.setStatus(_A)
_PmoabRinvBoosterEntry_Object=MibTableRow
pmoabRinvBoosterEntry=_PmoabRinvBoosterEntry_Object((1,3,6,1,4,1,20044,23,7,6,1))
pmoabRinvBoosterEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:pmoabRinvBoosterEntry.setStatus(_A)
class _PmoabRinvBoosterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoabRinvBoosterIndex_Type.__name__=_E
_PmoabRinvBoosterIndex_Object=MibTableColumn
pmoabRinvBoosterIndex=_PmoabRinvBoosterIndex_Object((1,3,6,1,4,1,20044,23,7,6,1,1),_PmoabRinvBoosterIndex_Type())
pmoabRinvBoosterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabRinvBoosterIndex.setStatus(_A)
_PmoabRinvBooster_Type=DisplayString
_PmoabRinvBooster_Object=MibTableColumn
pmoabRinvBooster=_PmoabRinvBooster_Object((1,3,6,1,4,1,20044,23,7,6,1,2),_PmoabRinvBooster_Type())
pmoabRinvBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabRinvBooster.setStatus(_A)
_PmoabConfig_ObjectIdentity=ObjectIdentity
pmoabConfig=_PmoabConfig_ObjectIdentity((1,3,6,1,4,1,20044,23,9))
_PmoabCfgNoValue_ObjectIdentity=ObjectIdentity
pmoabCfgNoValue=_PmoabCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,23,9,1))
_PmoabtableclientStartup_ObjectIdentity=ObjectIdentity
pmoabtableclientStartup=_PmoabtableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,23,9,1,1))
_PmoabCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoabCfgLineStartUp=_PmoabCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,23,9,2))
_PmoabtablelineStartup_ObjectIdentity=ObjectIdentity
pmoabtablelineStartup=_PmoabtablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,23,9,2,1))
class _PmoabCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabCfglineEdfaLaserCtrl_Type.__name__=_G
_PmoabCfglineEdfaLaserCtrl_Object=MibScalar
pmoabCfglineEdfaLaserCtrl=_PmoabCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,23,9,2,1,2),_PmoabCfglineEdfaLaserCtrl_Type())
pmoabCfglineEdfaLaserCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoabCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabCfglineEdfaLaserMode_Type.__name__=_G
_PmoabCfglineEdfaLaserMode_Object=MibScalar
pmoabCfglineEdfaLaserMode=_PmoabCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,23,9,2,1,3),_PmoabCfglineEdfaLaserMode_Type())
pmoabCfglineEdfaLaserMode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCfglineEdfaLaserMode.setStatus(_A)
_PmoabCfgLabels_ObjectIdentity=ObjectIdentity
pmoabCfgLabels=_PmoabCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,23,9,3))
_PmoabCfgLabelclientTable_Object=MibTable
pmoabCfgLabelclientTable=_PmoabCfgLabelclientTable_Object((1,3,6,1,4,1,20044,23,9,3,1))
if mibBuilder.loadTexts:pmoabCfgLabelclientTable.setStatus(_A)
_PmoabCfgLabelclientEntry_Object=MibTableRow
pmoabCfgLabelclientEntry=_PmoabCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,23,9,3,1,1))
pmoabCfgLabelclientEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:pmoabCfgLabelclientEntry.setStatus(_A)
class _PmoabCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabCfgLabelclientIndex_Type.__name__=_E
_PmoabCfgLabelclientIndex_Object=MibTableColumn
pmoabCfgLabelclientIndex=_PmoabCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,23,9,3,1,1,1),_PmoabCfgLabelclientIndex_Type())
pmoabCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabCfgLabelclientIndex.setStatus(_A)
class _PmoabCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoabCfgLabelclientPortn_Type.__name__=_H
_PmoabCfgLabelclientPortn_Object=MibTableColumn
pmoabCfgLabelclientPortn=_PmoabCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,23,9,3,1,1,3),_PmoabCfgLabelclientPortn_Type())
pmoabCfgLabelclientPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCfgLabelclientPortn.setStatus(_A)
_PmoabCfgLabellineTable_Object=MibTable
pmoabCfgLabellineTable=_PmoabCfgLabellineTable_Object((1,3,6,1,4,1,20044,23,9,3,2))
if mibBuilder.loadTexts:pmoabCfgLabellineTable.setStatus(_A)
_PmoabCfgLabellineEntry_Object=MibTableRow
pmoabCfgLabellineEntry=_PmoabCfgLabellineEntry_Object((1,3,6,1,4,1,20044,23,9,3,2,1))
pmoabCfgLabellineEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pmoabCfgLabellineEntry.setStatus(_A)
class _PmoabCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabCfgLabellineIndex_Type.__name__=_E
_PmoabCfgLabellineIndex_Object=MibTableColumn
pmoabCfgLabellineIndex=_PmoabCfgLabellineIndex_Object((1,3,6,1,4,1,20044,23,9,3,2,1,1),_PmoabCfgLabellineIndex_Type())
pmoabCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabCfgLabellineIndex.setStatus(_A)
class _PmoabCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoabCfgLabellinePortn_Type.__name__=_H
_PmoabCfgLabellinePortn_Object=MibTableColumn
pmoabCfgLabellinePortn=_PmoabCfgLabellinePortn_Object((1,3,6,1,4,1,20044,23,9,3,2,1,3),_PmoabCfgLabellinePortn_Type())
pmoabCfgLabellinePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCfgLabellinePortn.setStatus(_A)
_PmoabCfgWriteConfiguration_Type=EkiOnOff
_PmoabCfgWriteConfiguration_Object=MibScalar
pmoabCfgWriteConfiguration=_PmoabCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,23,9,257),_PmoabCfgWriteConfiguration_Type())
pmoabCfgWriteConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:pmoabCfgWriteConfiguration.setStatus(_A)
_Pmoabtraps_ObjectIdentity=ObjectIdentity
pmoabtraps=_Pmoabtraps_ObjectIdentity((1,3,6,1,4,1,20044,23,10))
class _PmoabtrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoabtrapBoardNumber_Type.__name__=_E
_PmoabtrapBoardNumber_Object=MibScalar
pmoabtrapBoardNumber=_PmoabtrapBoardNumber_Object((1,3,6,1,4,1,20044,23,10,4),_PmoabtrapBoardNumber_Type())
pmoabtrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabtrapBoardNumber.setStatus(_A)
pmoabLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,30))
pmoabLineTrapNotUrgentGoesOn.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmoabLineTrapNotUrgentGoesOn.setStatus(_A)
pmoabLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,31))
pmoabLineTrapNotUrgentGoesOff.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmoabLineTrapNotUrgentGoesOff.setStatus(_A)
pmoabLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,32))
pmoabLineTrapUrgentGoesOn.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmoabLineTrapUrgentGoesOn.setStatus(_A)
pmoabLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,33))
pmoabLineTrapUrgentGoesOff.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmoabLineTrapUrgentGoesOff.setStatus(_A)
pmoabLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,34))
pmoabLineTrapCritGoesOn.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmoabLineTrapCritGoesOn.setStatus(_A)
pmoabLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,35))
pmoabLineTrapCritGoesOff.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmoabLineTrapCritGoesOff.setStatus(_A)
pmoabClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,40))
pmoabClientTrapNotUrgentGoesOn.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmoabClientTrapNotUrgentGoesOn.setStatus(_A)
pmoabClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,41))
pmoabClientTrapNotUrgentGoesOff.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmoabClientTrapNotUrgentGoesOff.setStatus(_A)
pmoabClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,42))
pmoabClientTrapUrgentGoesOn.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmoabClientTrapUrgentGoesOn.setStatus(_A)
pmoabClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,43))
pmoabClientTrapUrgentGoesOff.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmoabClientTrapUrgentGoesOff.setStatus(_A)
pmoabClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,44))
pmoabClientTrapCritGoesOn.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmoabClientTrapCritGoesOn.setStatus(_A)
pmoabClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,45))
pmoabClientTrapCritGoesOff.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmoabClientTrapCritGoesOff.setStatus(_A)
pmoabPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,23,10,50))
pmoabPowerTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmoabPowerTrapUrgentGoesOn.setStatus(_A)
pmoabPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,23,10,51))
pmoabPowerTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmoabPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PmoabboosterMode':PmoabboosterMode,'modulepmoab':modulepmoab,'pmoabalarms':pmoabalarms,'pmoabAlmOther':pmoabAlmOther,'pmoabAlmOtherNurg':pmoabAlmOtherNurg,'pmoabAlmsynthAlm2':pmoabAlmsynthAlm2,'pmoabAlmConfTableSave':pmoabAlmConfTableSave,'pmoabAlmInvUpload':pmoabAlmInvUpload,'pmoabAlmConfTableLoad':pmoabAlmConfTableLoad,'pmoabAlmfoaWarnings':pmoabAlmfoaWarnings,'pmoabAlm3v3LowWarning':pmoabAlm3v3LowWarning,'pmoabAlm3v3HighWarning':pmoabAlm3v3HighWarning,'pmoabAlmTermpLowWarning':pmoabAlmTermpLowWarning,'pmoabAlmTempHighWarning':pmoabAlmTempHighWarning,'pmoabAlmOtherUrg':pmoabAlmOtherUrg,'pmoabAlmfoaAlarms':pmoabAlmfoaAlarms,'pmoabAlm3v3LowAlarm':pmoabAlm3v3LowAlarm,'pmoabAlm3v3HighAlarm':pmoabAlm3v3HighAlarm,'pmoabAlmTermpLowAlarm':pmoabAlmTermpLowAlarm,'pmoabAlmTempHighAlarm':pmoabAlmTempHighAlarm,'pmoabAlmOtherCrit':pmoabAlmOtherCrit,'pmoabAlmsynthAlm0':pmoabAlmsynthAlm0,'pmoabAlmMaintenanceMode':pmoabAlmMaintenanceMode,'pmoabAlmModGlobFail':pmoabAlmModGlobFail,'pmoabAlmUpEdfaInitNotCompl':pmoabAlmUpEdfaInitNotCompl,'pmoabAlmDwEdfaInitNotCompl':pmoabAlmDwEdfaInitNotCompl,'pmoabAlmExtPumpNotLocked':pmoabAlmExtPumpNotLocked,_R:pmoabAlmDefFuseA,_Q:pmoabAlmDefFuseB,'pmoabAlmClient':pmoabAlmClient,'pmoabAlmClientNurg':pmoabAlmClientNurg,'pmoabAlmclientEdfaWarnings':pmoabAlmclientEdfaWarnings,'pmoabAlmClientInputPwrLowWarning':pmoabAlmClientInputPwrLowWarning,'pmoabAlmClientInputPwrHighWarning':pmoabAlmClientInputPwrHighWarning,'pmoabAlmClientUrg':pmoabAlmClientUrg,'pmoabAlmclientEdfaAlarms1':pmoabAlmclientEdfaAlarms1,'pmoabAlmClientInputPwrLowAlarm':pmoabAlmClientInputPwrLowAlarm,'pmoabAlmClientInputPwrHighAlarm':pmoabAlmClientInputPwrHighAlarm,'pmoabAlmClientCrit':pmoabAlmClientCrit,'pmoabAlmsynthAlm8':pmoabAlmsynthAlm8,_P:pmoabAlmClientHwFail,_M:pmoabAlmClientDdmWarning,_N:pmoabAlmClientDdmAlm,_O:pmoabAlmClientFail,'pmoabAlmclientEdfaAlarms2':pmoabAlmclientEdfaAlarms2,'pmoabAlmClientEdfaLos':pmoabAlmClientEdfaLos,'pmoabAlmLine':pmoabAlmLine,'pmoabAlmLineNurg':pmoabAlmLineNurg,'pmoabAlmlineEdfaWarnings':pmoabAlmlineEdfaWarnings,'pmoabAlmLineGainLowWarning':pmoabAlmLineGainLowWarning,'pmoabAlmLineGainHighWarning':pmoabAlmLineGainHighWarning,'pmoabAlmLineOutputPwrLowWarning':pmoabAlmLineOutputPwrLowWarning,'pmoabAlmLineOutputPwrHighWarning':pmoabAlmLineOutputPwrHighWarning,'pmoabAlmLineBiasLowWarning':pmoabAlmLineBiasLowWarning,'pmoabAlmLineBiasHighWarning':pmoabAlmLineBiasHighWarning,'pmoabAlmLineUrg':pmoabAlmLineUrg,'pmoabAlmlineEdfaAlarms1':pmoabAlmlineEdfaAlarms1,'pmoabAlmLineGainLowAlarm':pmoabAlmLineGainLowAlarm,'pmoabAlmLineGainHighAlarm':pmoabAlmLineGainHighAlarm,'pmoabAlmLineOutputPwrLowAlarm':pmoabAlmLineOutputPwrLowAlarm,'pmoabAlmLineOutputPwrHighAlarm':pmoabAlmLineOutputPwrHighAlarm,'pmoabAlmLineBiasLowAlarm':pmoabAlmLineBiasLowAlarm,'pmoabAlmLineBiasHighAlarm':pmoabAlmLineBiasHighAlarm,'pmoabAlmLineCrit':pmoabAlmLineCrit,'pmoabAlmsynthAlm7':pmoabAlmsynthAlm7,_L:pmoabAlmLineHwFail,'pmoabAlmLineTxOff':pmoabAlmLineTxOff,_I:pmoabAlmLineDdmWarning,_J:pmoabAlmLineDdmAlm,_K:pmoabAlmLineFail,'pmoabAlmlineEdfaAlarms2':pmoabAlmlineEdfaAlarms2,'pmoabAlmLineEdfaNr':pmoabAlmLineEdfaNr,'pmoabAlmLineEdfaTecFail':pmoabAlmLineEdfaTecFail,'pmoabAlmLineEdfaLaserFail':pmoabAlmLineEdfaLaserFail,'pmoabAlmLineExtPumpEdfaLowCurrent':pmoabAlmLineExtPumpEdfaLowCurrent,'pmoabmeasures':pmoabmeasures,'pmoabMesrOther':pmoabMesrOther,'pmoabMesrtempMeas':pmoabMesrtempMeas,'pmoabMesr3v3Meas':pmoabMesr3v3Meas,'pmoabMesrClient':pmoabMesrClient,'pmoabMesrclientEdfaRxpwrMeas':pmoabMesrclientEdfaRxpwrMeas,'pmoabMesrLine':pmoabMesrLine,'pmoabMesrlineEdfaBiasMeas':pmoabMesrlineEdfaBiasMeas,'pmoabMesrlineEdfaTxpwrMeas':pmoabMesrlineEdfaTxpwrMeas,'pmoabMesrlineEdfaGainMeas':pmoabMesrlineEdfaGainMeas,'pmoabcontrolsWrite':pmoabcontrolsWrite,'pmoabCtrlOther':pmoabCtrlOther,'pmoabCtrlsynth0':pmoabCtrlsynth0,'pmoabCtrlConfLoad':pmoabCtrlConfLoad,'pmoabCtrlConfFlash':pmoabCtrlConfFlash,'pmoabCtrlConfClear':pmoabCtrlConfClear,'pmoabCtrlswMgnt':pmoabCtrlswMgnt,'pmoabCtrlColdReset':pmoabCtrlColdReset,'pmoabCtrlWarmReset':pmoabCtrlWarmReset,'pmoabCtrlpowerDown':pmoabCtrlpowerDown,'pmoabCtrlSoftPowerDown':pmoabCtrlSoftPowerDown,'pmoabCtrlledTest':pmoabCtrlledTest,'pmoabCtrlGreenLed':pmoabCtrlGreenLed,'pmoabCtrlRedLed':pmoabCtrlRedLed,'pmoabCtrlLedOff':pmoabCtrlLedOff,'pmoabCtrlmaintMode':pmoabCtrlmaintMode,'pmoabCtrlMaintenance':pmoabCtrlMaintenance,'pmoabCtrlClient':pmoabCtrlClient,'pmoabCtrlLine':pmoabCtrlLine,'pmoabCtrllineEdfaLaserOff':pmoabCtrllineEdfaLaserOff,'pmoabCtrlLineEdfaLaserOff':pmoabCtrlLineEdfaLaserOff,'pmoabCtrllineEdfaMode':pmoabCtrllineEdfaMode,'pmoabCtrllineIlasSettingValue':pmoabCtrllineIlasSettingValue,'pmoabCtrllinePlasSettingValue':pmoabCtrllinePlasSettingValue,'pmoabCtrllineGainSettingValue':pmoabCtrllineGainSettingValue,'pmoabCtrllineEffPwrOutSettingValue':pmoabCtrllineEffPwrOutSettingValue,'pmoabri':pmoabri,'pmoabRinvReloadInventory':pmoabRinvReloadInventory,'pmoabRinvModulePlatform':pmoabRinvModulePlatform,'pmoabRinvSwPlatform':pmoabRinvSwPlatform,'pmoabRinvSwFoa':pmoabRinvSwFoa,'pmoabRinvBoosterTable':pmoabRinvBoosterTable,'pmoabRinvBoosterEntry':pmoabRinvBoosterEntry,_S:pmoabRinvBoosterIndex,'pmoabRinvBooster':pmoabRinvBooster,'pmoabConfig':pmoabConfig,'pmoabCfgNoValue':pmoabCfgNoValue,'pmoabtableclientStartup':pmoabtableclientStartup,'pmoabCfgLineStartUp':pmoabCfgLineStartUp,'pmoabtablelineStartup':pmoabtablelineStartup,'pmoabCfglineEdfaLaserCtrl':pmoabCfglineEdfaLaserCtrl,'pmoabCfglineEdfaLaserMode':pmoabCfglineEdfaLaserMode,'pmoabCfgLabels':pmoabCfgLabels,'pmoabCfgLabelclientTable':pmoabCfgLabelclientTable,'pmoabCfgLabelclientEntry':pmoabCfgLabelclientEntry,_T:pmoabCfgLabelclientIndex,'pmoabCfgLabelclientPortn':pmoabCfgLabelclientPortn,'pmoabCfgLabellineTable':pmoabCfgLabellineTable,'pmoabCfgLabellineEntry':pmoabCfgLabellineEntry,_U:pmoabCfgLabellineIndex,'pmoabCfgLabellinePortn':pmoabCfgLabellinePortn,'pmoabCfgWriteConfiguration':pmoabCfgWriteConfiguration,'pmoabtraps':pmoabtraps,_F:pmoabtrapBoardNumber,'pmoabLineTrapNotUrgentGoesOn':pmoabLineTrapNotUrgentGoesOn,'pmoabLineTrapNotUrgentGoesOff':pmoabLineTrapNotUrgentGoesOff,'pmoabLineTrapUrgentGoesOn':pmoabLineTrapUrgentGoesOn,'pmoabLineTrapUrgentGoesOff':pmoabLineTrapUrgentGoesOff,'pmoabLineTrapCritGoesOn':pmoabLineTrapCritGoesOn,'pmoabLineTrapCritGoesOff':pmoabLineTrapCritGoesOff,'pmoabClientTrapNotUrgentGoesOn':pmoabClientTrapNotUrgentGoesOn,'pmoabClientTrapNotUrgentGoesOff':pmoabClientTrapNotUrgentGoesOff,'pmoabClientTrapUrgentGoesOn':pmoabClientTrapUrgentGoesOn,'pmoabClientTrapUrgentGoesOff':pmoabClientTrapUrgentGoesOff,'pmoabClientTrapCritGoesOn':pmoabClientTrapCritGoesOn,'pmoabClientTrapCritGoesOff':pmoabClientTrapCritGoesOff,'pmoabPowerTrapUrgentGoesOn':pmoabPowerTrapUrgentGoesOn,'pmoabPowerTrapUrgentGoesOff':pmoabPowerTrapUrgentGoesOff})