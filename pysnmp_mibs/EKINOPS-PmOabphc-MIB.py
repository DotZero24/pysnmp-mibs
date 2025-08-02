_W='pmoabphcCfgLabellineIndex'
_V='pmoabphcCfgLabelclientIndex'
_U='pmoabphcRinvPreAmpIndex'
_T='pmoabphcRinvBoosterIndex'
_S='2011-07-06 00:00'
_R='pmoabphcAlmDefFuseA'
_Q='pmoabphcAlmDefFuseB'
_P='pmoabphcAlmClientHwFail'
_O='pmoabphcAlmClientFail'
_N='pmoabphcAlmClientDdmAlm'
_M='pmoabphcAlmClientDdmWarning'
_L='pmoabphcAlmLineHwFail'
_K='pmoabphcAlmLineFail'
_J='pmoabphcAlmLineDdmAlm'
_I='pmoabphcAlmLineDdmWarning'
_H='DisplayString'
_G='pmoabphctrapBoardNumber'
_F='Unsigned32'
_E='Integer32'
_D='EKINOPS-PmOabphc-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
modulepmoabphc=ModuleIdentity((1,3,6,1,4,1,20044,51))
if mibBuilder.loadTexts:modulepmoabphc.setRevisions((_S,_S,'2013-02-08 00:00','2013-07-01 00:00','2013-09-16 00:00','2013-12-02 00:00','2014-03-26 00:00','2014-12-10 00:00','2016-05-23 00:00'))
class PmoabphcpreampMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oabphcpreampdefaultmode',0),('oabphcpreampconstantcurrentmode',1),('oabphcpreampconstantpowermode',2),('oabphcpreampconstantgainmode',3),('oabphcpreamppoutpinmode',4),('oabphcpreampmanualmode',5),('oabphcpreampfeedforwardmode',6),('oabphcpreamptransientsupmode',7)))
class PmoabphcboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oabphcboosterdefaultmode',0),('oabphcboosterconstantcurrentmode',1),('oabphcboosterconstantpowermode',2),('oabphcboosterconstantgainmode',3),('oabphcboosterpoutpinmode',4),('oabphcboostermanualmode',5),('oabphcboosterfeedforwardmode',6),('oabphcboostertransientsupmode',7)))
class PmoabphcaprMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('oabphcaproffmode',0),('oabphcaprsemiautomode',1),('oabphcaprautomode',2),('oabphcaprlossforwardingmode',3),('oabphcaprrepeatmode',4)))
class PmoabphcPreampGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oabphcpreampgainadjmanualmode',0),('oabphcpreampgainadjsemiautomode',1),('oabphcpreampgainadjautomode',2)))
class PmoabphcBoosterGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oabphcboostergainadjmanualmode',0),('oabphcboostergainadjsemiautomode',1),('oabphcboostergainadjautomode',2)))
class PmoabphcPreampCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oabphcpreampcstgainadjsemiautomode',1),('oabphcpreampcstgainadjautomode',2)))
class PmoabphcBoosterCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oabphcboostercstgainadjsemiautomode',1),('oabphcboostercstgainadjautomode',2)))
_Pmoabphcalarms_ObjectIdentity=ObjectIdentity
pmoabphcalarms=_Pmoabphcalarms_ObjectIdentity((1,3,6,1,4,1,20044,51,2))
_PmoabphcAlmOther_ObjectIdentity=ObjectIdentity
pmoabphcAlmOther=_PmoabphcAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1))
_PmoabphcAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoabphcAlmOtherNurg=_PmoabphcAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,1))
_PmoabphcAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoabphcAlmsynthAlm2=_PmoabphcAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,1,2))
_PmoabphcAlmConfTableSave_Type=EkiOnOff
_PmoabphcAlmConfTableSave_Object=MibScalar
pmoabphcAlmConfTableSave=_PmoabphcAlmConfTableSave_Object((1,3,6,1,4,1,20044,51,2,1,1,2,1),_PmoabphcAlmConfTableSave_Type())
pmoabphcAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmConfTableSave.setStatus(_A)
_PmoabphcAlmInvUpload_Type=EkiOnOff
_PmoabphcAlmInvUpload_Object=MibScalar
pmoabphcAlmInvUpload=_PmoabphcAlmInvUpload_Object((1,3,6,1,4,1,20044,51,2,1,1,2,2),_PmoabphcAlmInvUpload_Type())
pmoabphcAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmInvUpload.setStatus(_A)
_PmoabphcAlmConfTableLoad_Type=EkiOnOff
_PmoabphcAlmConfTableLoad_Object=MibScalar
pmoabphcAlmConfTableLoad=_PmoabphcAlmConfTableLoad_Object((1,3,6,1,4,1,20044,51,2,1,1,2,3),_PmoabphcAlmConfTableLoad_Type())
pmoabphcAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmConfTableLoad.setStatus(_A)
_PmoabphcAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoabphcAlmfoaWarnings=_PmoabphcAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,1,75))
_PmoabphcAlmTermpLowWarning_Type=EkiOnOff
_PmoabphcAlmTermpLowWarning_Object=MibScalar
pmoabphcAlmTermpLowWarning=_PmoabphcAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,51,2,1,1,75,7),_PmoabphcAlmTermpLowWarning_Type())
pmoabphcAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmTermpLowWarning.setStatus(_A)
_PmoabphcAlmTempHighWarning_Type=EkiOnOff
_PmoabphcAlmTempHighWarning_Object=MibScalar
pmoabphcAlmTempHighWarning=_PmoabphcAlmTempHighWarning_Object((1,3,6,1,4,1,20044,51,2,1,1,75,8),_PmoabphcAlmTempHighWarning_Type())
pmoabphcAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmTempHighWarning.setStatus(_A)
_PmoabphcAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoabphcAlmOtherUrg=_PmoabphcAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,2))
_PmoabphcAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoabphcAlmfoaAlarms=_PmoabphcAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,2,74))
_PmoabphcAlmTermpLowAlarm_Type=EkiOnOff
_PmoabphcAlmTermpLowAlarm_Object=MibScalar
pmoabphcAlmTermpLowAlarm=_PmoabphcAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,51,2,1,2,74,7),_PmoabphcAlmTermpLowAlarm_Type())
pmoabphcAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmTermpLowAlarm.setStatus(_A)
_PmoabphcAlmTempHighAlarm_Type=EkiOnOff
_PmoabphcAlmTempHighAlarm_Object=MibScalar
pmoabphcAlmTempHighAlarm=_PmoabphcAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,51,2,1,2,74,8),_PmoabphcAlmTempHighAlarm_Type())
pmoabphcAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmTempHighAlarm.setStatus(_A)
_PmoabphcAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoabphcAlmOtherCrit=_PmoabphcAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,3))
_PmoabphcAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoabphcAlmsynthAlm0=_PmoabphcAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,51,2,1,3,0))
_PmoabphcAlmMaintenanceMode_Type=EkiOnOff
_PmoabphcAlmMaintenanceMode_Object=MibScalar
pmoabphcAlmMaintenanceMode=_PmoabphcAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,51,2,1,3,0,1),_PmoabphcAlmMaintenanceMode_Type())
pmoabphcAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmMaintenanceMode.setStatus(_A)
_PmoabphcAlmAprOn_Type=EkiOnOff
_PmoabphcAlmAprOn_Object=MibScalar
pmoabphcAlmAprOn=_PmoabphcAlmAprOn_Object((1,3,6,1,4,1,20044,51,2,1,3,0,2),_PmoabphcAlmAprOn_Type())
pmoabphcAlmAprOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmAprOn.setStatus(_A)
_PmoabphcAlmModGlobFail_Type=EkiOnOff
_PmoabphcAlmModGlobFail_Object=MibScalar
pmoabphcAlmModGlobFail=_PmoabphcAlmModGlobFail_Object((1,3,6,1,4,1,20044,51,2,1,3,0,9),_PmoabphcAlmModGlobFail_Type())
pmoabphcAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmModGlobFail.setStatus(_A)
_PmoabphcAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoabphcAlmUpEdfaInitNotCompl_Object=MibScalar
pmoabphcAlmUpEdfaInitNotCompl=_PmoabphcAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,51,2,1,3,0,10),_PmoabphcAlmUpEdfaInitNotCompl_Type())
pmoabphcAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoabphcAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoabphcAlmDwEdfaInitNotCompl_Object=MibScalar
pmoabphcAlmDwEdfaInitNotCompl=_PmoabphcAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,51,2,1,3,0,11),_PmoabphcAlmDwEdfaInitNotCompl_Type())
pmoabphcAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoabphcAlmExtPump1NotLocked_Type=EkiOnOff
_PmoabphcAlmExtPump1NotLocked_Object=MibScalar
pmoabphcAlmExtPump1NotLocked=_PmoabphcAlmExtPump1NotLocked_Object((1,3,6,1,4,1,20044,51,2,1,3,0,12),_PmoabphcAlmExtPump1NotLocked_Type())
pmoabphcAlmExtPump1NotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmExtPump1NotLocked.setStatus(_A)
_PmoabphcAlmExtPump2NotLocked_Type=EkiOnOff
_PmoabphcAlmExtPump2NotLocked_Object=MibScalar
pmoabphcAlmExtPump2NotLocked=_PmoabphcAlmExtPump2NotLocked_Object((1,3,6,1,4,1,20044,51,2,1,3,0,13),_PmoabphcAlmExtPump2NotLocked_Type())
pmoabphcAlmExtPump2NotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmExtPump2NotLocked.setStatus(_A)
_PmoabphcAlmDefFuseA_Type=EkiOnOff
_PmoabphcAlmDefFuseA_Object=MibScalar
pmoabphcAlmDefFuseA=_PmoabphcAlmDefFuseA_Object((1,3,6,1,4,1,20044,51,2,1,3,0,15),_PmoabphcAlmDefFuseA_Type())
pmoabphcAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmDefFuseA.setStatus(_A)
_PmoabphcAlmDefFuseB_Type=EkiOnOff
_PmoabphcAlmDefFuseB_Object=MibScalar
pmoabphcAlmDefFuseB=_PmoabphcAlmDefFuseB_Object((1,3,6,1,4,1,20044,51,2,1,3,0,16),_PmoabphcAlmDefFuseB_Type())
pmoabphcAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmDefFuseB.setStatus(_A)
_PmoabphcAlmClient_ObjectIdentity=ObjectIdentity
pmoabphcAlmClient=_PmoabphcAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2))
_PmoabphcAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoabphcAlmClientNurg=_PmoabphcAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,1))
_PmoabphcAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoabphcAlmclientEdfaWarnings=_PmoabphcAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,1,33))
_PmoabphcAlmClientGainLowWarning_Type=EkiOnOff
_PmoabphcAlmClientGainLowWarning_Object=MibScalar
pmoabphcAlmClientGainLowWarning=_PmoabphcAlmClientGainLowWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,1),_PmoabphcAlmClientGainLowWarning_Type())
pmoabphcAlmClientGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientGainLowWarning.setStatus(_A)
_PmoabphcAlmClientGainHighWarning_Type=EkiOnOff
_PmoabphcAlmClientGainHighWarning_Object=MibScalar
pmoabphcAlmClientGainHighWarning=_PmoabphcAlmClientGainHighWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,2),_PmoabphcAlmClientGainHighWarning_Type())
pmoabphcAlmClientGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientGainHighWarning.setStatus(_A)
_PmoabphcAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoabphcAlmClientInputPwrLowWarning_Object=MibScalar
pmoabphcAlmClientInputPwrLowWarning=_PmoabphcAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,3),_PmoabphcAlmClientInputPwrLowWarning_Type())
pmoabphcAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientInputPwrLowWarning.setStatus(_A)
_PmoabphcAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoabphcAlmClientInputPwrHighWarning_Object=MibScalar
pmoabphcAlmClientInputPwrHighWarning=_PmoabphcAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,4),_PmoabphcAlmClientInputPwrHighWarning_Type())
pmoabphcAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientInputPwrHighWarning.setStatus(_A)
_PmoabphcAlmClientOutputPwrLowWarning_Type=EkiOnOff
_PmoabphcAlmClientOutputPwrLowWarning_Object=MibScalar
pmoabphcAlmClientOutputPwrLowWarning=_PmoabphcAlmClientOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,5),_PmoabphcAlmClientOutputPwrLowWarning_Type())
pmoabphcAlmClientOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientOutputPwrLowWarning.setStatus(_A)
_PmoabphcAlmClientOutputPwrHighWarning_Type=EkiOnOff
_PmoabphcAlmClientOutputPwrHighWarning_Object=MibScalar
pmoabphcAlmClientOutputPwrHighWarning=_PmoabphcAlmClientOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,6),_PmoabphcAlmClientOutputPwrHighWarning_Type())
pmoabphcAlmClientOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientOutputPwrHighWarning.setStatus(_A)
_PmoabphcAlmClientBiasLowWarning_Type=EkiOnOff
_PmoabphcAlmClientBiasLowWarning_Object=MibScalar
pmoabphcAlmClientBiasLowWarning=_PmoabphcAlmClientBiasLowWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,7),_PmoabphcAlmClientBiasLowWarning_Type())
pmoabphcAlmClientBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientBiasLowWarning.setStatus(_A)
_PmoabphcAlmClientBiasHighWarning_Type=EkiOnOff
_PmoabphcAlmClientBiasHighWarning_Object=MibScalar
pmoabphcAlmClientBiasHighWarning=_PmoabphcAlmClientBiasHighWarning_Object((1,3,6,1,4,1,20044,51,2,2,1,33,8),_PmoabphcAlmClientBiasHighWarning_Type())
pmoabphcAlmClientBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientBiasHighWarning.setStatus(_A)
_PmoabphcAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoabphcAlmClientUrg=_PmoabphcAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,2))
_PmoabphcAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoabphcAlmclientEdfaAlarms1=_PmoabphcAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,2,32))
_PmoabphcAlmClientGainLowAlarm_Type=EkiOnOff
_PmoabphcAlmClientGainLowAlarm_Object=MibScalar
pmoabphcAlmClientGainLowAlarm=_PmoabphcAlmClientGainLowAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,1),_PmoabphcAlmClientGainLowAlarm_Type())
pmoabphcAlmClientGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientGainLowAlarm.setStatus(_A)
_PmoabphcAlmClientGainHighAlarm_Type=EkiOnOff
_PmoabphcAlmClientGainHighAlarm_Object=MibScalar
pmoabphcAlmClientGainHighAlarm=_PmoabphcAlmClientGainHighAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,2),_PmoabphcAlmClientGainHighAlarm_Type())
pmoabphcAlmClientGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientGainHighAlarm.setStatus(_A)
_PmoabphcAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoabphcAlmClientInputPwrLowAlarm_Object=MibScalar
pmoabphcAlmClientInputPwrLowAlarm=_PmoabphcAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,3),_PmoabphcAlmClientInputPwrLowAlarm_Type())
pmoabphcAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoabphcAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoabphcAlmClientInputPwrHighAlarm_Object=MibScalar
pmoabphcAlmClientInputPwrHighAlarm=_PmoabphcAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,4),_PmoabphcAlmClientInputPwrHighAlarm_Type())
pmoabphcAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoabphcAlmClientOutputPwrLowAlarm_Type=EkiOnOff
_PmoabphcAlmClientOutputPwrLowAlarm_Object=MibScalar
pmoabphcAlmClientOutputPwrLowAlarm=_PmoabphcAlmClientOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,5),_PmoabphcAlmClientOutputPwrLowAlarm_Type())
pmoabphcAlmClientOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientOutputPwrLowAlarm.setStatus(_A)
_PmoabphcAlmClientOutputPwrHighAlarm_Type=EkiOnOff
_PmoabphcAlmClientOutputPwrHighAlarm_Object=MibScalar
pmoabphcAlmClientOutputPwrHighAlarm=_PmoabphcAlmClientOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,6),_PmoabphcAlmClientOutputPwrHighAlarm_Type())
pmoabphcAlmClientOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientOutputPwrHighAlarm.setStatus(_A)
_PmoabphcAlmClientBiasLowAlarm_Type=EkiOnOff
_PmoabphcAlmClientBiasLowAlarm_Object=MibScalar
pmoabphcAlmClientBiasLowAlarm=_PmoabphcAlmClientBiasLowAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,7),_PmoabphcAlmClientBiasLowAlarm_Type())
pmoabphcAlmClientBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientBiasLowAlarm.setStatus(_A)
_PmoabphcAlmClientBiasHighAlarm_Type=EkiOnOff
_PmoabphcAlmClientBiasHighAlarm_Object=MibScalar
pmoabphcAlmClientBiasHighAlarm=_PmoabphcAlmClientBiasHighAlarm_Object((1,3,6,1,4,1,20044,51,2,2,2,32,8),_PmoabphcAlmClientBiasHighAlarm_Type())
pmoabphcAlmClientBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientBiasHighAlarm.setStatus(_A)
_PmoabphcAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoabphcAlmClientCrit=_PmoabphcAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,3))
_PmoabphcAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoabphcAlmsynthAlm8=_PmoabphcAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,3,8))
_PmoabphcAlmClientHwFail_Type=EkiOnOff
_PmoabphcAlmClientHwFail_Object=MibScalar
pmoabphcAlmClientHwFail=_PmoabphcAlmClientHwFail_Object((1,3,6,1,4,1,20044,51,2,2,3,8,4),_PmoabphcAlmClientHwFail_Type())
pmoabphcAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientHwFail.setStatus(_A)
_PmoabphcAlmClientTxOff_Type=EkiOnOff
_PmoabphcAlmClientTxOff_Object=MibScalar
pmoabphcAlmClientTxOff=_PmoabphcAlmClientTxOff_Object((1,3,6,1,4,1,20044,51,2,2,3,8,5),_PmoabphcAlmClientTxOff_Type())
pmoabphcAlmClientTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientTxOff.setStatus(_A)
_PmoabphcAlmClientDdmWarning_Type=EkiOnOff
_PmoabphcAlmClientDdmWarning_Object=MibScalar
pmoabphcAlmClientDdmWarning=_PmoabphcAlmClientDdmWarning_Object((1,3,6,1,4,1,20044,51,2,2,3,8,9),_PmoabphcAlmClientDdmWarning_Type())
pmoabphcAlmClientDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientDdmWarning.setStatus(_A)
_PmoabphcAlmClientDdmAlm_Type=EkiOnOff
_PmoabphcAlmClientDdmAlm_Object=MibScalar
pmoabphcAlmClientDdmAlm=_PmoabphcAlmClientDdmAlm_Object((1,3,6,1,4,1,20044,51,2,2,3,8,10),_PmoabphcAlmClientDdmAlm_Type())
pmoabphcAlmClientDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientDdmAlm.setStatus(_A)
_PmoabphcAlmClientFail_Type=EkiOnOff
_PmoabphcAlmClientFail_Object=MibScalar
pmoabphcAlmClientFail=_PmoabphcAlmClientFail_Object((1,3,6,1,4,1,20044,51,2,2,3,8,12),_PmoabphcAlmClientFail_Type())
pmoabphcAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientFail.setStatus(_A)
_PmoabphcAlmClientExtPumpFail_Type=EkiOnOff
_PmoabphcAlmClientExtPumpFail_Object=MibScalar
pmoabphcAlmClientExtPumpFail=_PmoabphcAlmClientExtPumpFail_Object((1,3,6,1,4,1,20044,51,2,2,3,8,13),_PmoabphcAlmClientExtPumpFail_Type())
pmoabphcAlmClientExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientExtPumpFail.setStatus(_A)
_PmoabphcAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoabphcAlmclientEdfaAlarms2=_PmoabphcAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,51,2,2,3,35))
_PmoabphcAlmClientEdfaNr_Type=EkiOnOff
_PmoabphcAlmClientEdfaNr_Object=MibScalar
pmoabphcAlmClientEdfaNr=_PmoabphcAlmClientEdfaNr_Object((1,3,6,1,4,1,20044,51,2,2,3,35,1),_PmoabphcAlmClientEdfaNr_Type())
pmoabphcAlmClientEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientEdfaNr.setStatus(_A)
_PmoabphcAlmClientEdfaTecFail_Type=EkiOnOff
_PmoabphcAlmClientEdfaTecFail_Object=MibScalar
pmoabphcAlmClientEdfaTecFail=_PmoabphcAlmClientEdfaTecFail_Object((1,3,6,1,4,1,20044,51,2,2,3,35,2),_PmoabphcAlmClientEdfaTecFail_Type())
pmoabphcAlmClientEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientEdfaTecFail.setStatus(_A)
_PmoabphcAlmClientEdfaLaserFail_Type=EkiOnOff
_PmoabphcAlmClientEdfaLaserFail_Object=MibScalar
pmoabphcAlmClientEdfaLaserFail=_PmoabphcAlmClientEdfaLaserFail_Object((1,3,6,1,4,1,20044,51,2,2,3,35,3),_PmoabphcAlmClientEdfaLaserFail_Type())
pmoabphcAlmClientEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientEdfaLaserFail.setStatus(_A)
_PmoabphcAlmClientEdfaLos_Type=EkiOnOff
_PmoabphcAlmClientEdfaLos_Object=MibScalar
pmoabphcAlmClientEdfaLos=_PmoabphcAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,51,2,2,3,35,4),_PmoabphcAlmClientEdfaLos_Type())
pmoabphcAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientEdfaLos.setStatus(_A)
_PmoabphcAlmClientExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoabphcAlmClientExtPumpEdfaLowCurrent_Object=MibScalar
pmoabphcAlmClientExtPumpEdfaLowCurrent=_PmoabphcAlmClientExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,51,2,2,3,35,5),_PmoabphcAlmClientExtPumpEdfaLowCurrent_Type())
pmoabphcAlmClientExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmClientExtPumpEdfaLowCurrent.setStatus(_A)
_PmoabphcAlmLine_ObjectIdentity=ObjectIdentity
pmoabphcAlmLine=_PmoabphcAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3))
_PmoabphcAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoabphcAlmLineNurg=_PmoabphcAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,1))
_PmoabphcAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoabphcAlmlineEdfaWarnings=_PmoabphcAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,1,41))
_PmoabphcAlmLineGainLowWarning_Type=EkiOnOff
_PmoabphcAlmLineGainLowWarning_Object=MibScalar
pmoabphcAlmLineGainLowWarning=_PmoabphcAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,1),_PmoabphcAlmLineGainLowWarning_Type())
pmoabphcAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineGainLowWarning.setStatus(_A)
_PmoabphcAlmLineGainHighWarning_Type=EkiOnOff
_PmoabphcAlmLineGainHighWarning_Object=MibScalar
pmoabphcAlmLineGainHighWarning=_PmoabphcAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,2),_PmoabphcAlmLineGainHighWarning_Type())
pmoabphcAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineGainHighWarning.setStatus(_A)
_PmoabphcAlmLineInputPwrLowWarning_Type=EkiOnOff
_PmoabphcAlmLineInputPwrLowWarning_Object=MibScalar
pmoabphcAlmLineInputPwrLowWarning=_PmoabphcAlmLineInputPwrLowWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,3),_PmoabphcAlmLineInputPwrLowWarning_Type())
pmoabphcAlmLineInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineInputPwrLowWarning.setStatus(_A)
_PmoabphcAlmLineInputPwrHighWarning_Type=EkiOnOff
_PmoabphcAlmLineInputPwrHighWarning_Object=MibScalar
pmoabphcAlmLineInputPwrHighWarning=_PmoabphcAlmLineInputPwrHighWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,4),_PmoabphcAlmLineInputPwrHighWarning_Type())
pmoabphcAlmLineInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineInputPwrHighWarning.setStatus(_A)
_PmoabphcAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoabphcAlmLineOutputPwrLowWarning_Object=MibScalar
pmoabphcAlmLineOutputPwrLowWarning=_PmoabphcAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,5),_PmoabphcAlmLineOutputPwrLowWarning_Type())
pmoabphcAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoabphcAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoabphcAlmLineOutputPwrHighWarning_Object=MibScalar
pmoabphcAlmLineOutputPwrHighWarning=_PmoabphcAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,6),_PmoabphcAlmLineOutputPwrHighWarning_Type())
pmoabphcAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoabphcAlmLineBiasLowWarning_Type=EkiOnOff
_PmoabphcAlmLineBiasLowWarning_Object=MibScalar
pmoabphcAlmLineBiasLowWarning=_PmoabphcAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,7),_PmoabphcAlmLineBiasLowWarning_Type())
pmoabphcAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineBiasLowWarning.setStatus(_A)
_PmoabphcAlmLineBiasHighWarning_Type=EkiOnOff
_PmoabphcAlmLineBiasHighWarning_Object=MibScalar
pmoabphcAlmLineBiasHighWarning=_PmoabphcAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,51,2,3,1,41,8),_PmoabphcAlmLineBiasHighWarning_Type())
pmoabphcAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineBiasHighWarning.setStatus(_A)
_PmoabphcAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoabphcAlmLineUrg=_PmoabphcAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,2))
_PmoabphcAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoabphcAlmlineEdfaAlarms1=_PmoabphcAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,2,40))
_PmoabphcAlmLineGainLowAlarm_Type=EkiOnOff
_PmoabphcAlmLineGainLowAlarm_Object=MibScalar
pmoabphcAlmLineGainLowAlarm=_PmoabphcAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,1),_PmoabphcAlmLineGainLowAlarm_Type())
pmoabphcAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineGainLowAlarm.setStatus(_A)
_PmoabphcAlmLineGainHighAlarm_Type=EkiOnOff
_PmoabphcAlmLineGainHighAlarm_Object=MibScalar
pmoabphcAlmLineGainHighAlarm=_PmoabphcAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,2),_PmoabphcAlmLineGainHighAlarm_Type())
pmoabphcAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineGainHighAlarm.setStatus(_A)
_PmoabphcAlmLineInputPwrLowAlarm_Type=EkiOnOff
_PmoabphcAlmLineInputPwrLowAlarm_Object=MibScalar
pmoabphcAlmLineInputPwrLowAlarm=_PmoabphcAlmLineInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,3),_PmoabphcAlmLineInputPwrLowAlarm_Type())
pmoabphcAlmLineInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineInputPwrLowAlarm.setStatus(_A)
_PmoabphcAlmLineInputPwrHighAlarm_Type=EkiOnOff
_PmoabphcAlmLineInputPwrHighAlarm_Object=MibScalar
pmoabphcAlmLineInputPwrHighAlarm=_PmoabphcAlmLineInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,4),_PmoabphcAlmLineInputPwrHighAlarm_Type())
pmoabphcAlmLineInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineInputPwrHighAlarm.setStatus(_A)
_PmoabphcAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoabphcAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoabphcAlmLineOutputPwrLowAlarm=_PmoabphcAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,5),_PmoabphcAlmLineOutputPwrLowAlarm_Type())
pmoabphcAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoabphcAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoabphcAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoabphcAlmLineOutputPwrHighAlarm=_PmoabphcAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,6),_PmoabphcAlmLineOutputPwrHighAlarm_Type())
pmoabphcAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoabphcAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoabphcAlmLineBiasLowAlarm_Object=MibScalar
pmoabphcAlmLineBiasLowAlarm=_PmoabphcAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,7),_PmoabphcAlmLineBiasLowAlarm_Type())
pmoabphcAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineBiasLowAlarm.setStatus(_A)
_PmoabphcAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoabphcAlmLineBiasHighAlarm_Object=MibScalar
pmoabphcAlmLineBiasHighAlarm=_PmoabphcAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,51,2,3,2,40,8),_PmoabphcAlmLineBiasHighAlarm_Type())
pmoabphcAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineBiasHighAlarm.setStatus(_A)
_PmoabphcAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoabphcAlmLineCrit=_PmoabphcAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,3))
_PmoabphcAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoabphcAlmsynthAlm7=_PmoabphcAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,3,7))
_PmoabphcAlmLineHwFail_Type=EkiOnOff
_PmoabphcAlmLineHwFail_Object=MibScalar
pmoabphcAlmLineHwFail=_PmoabphcAlmLineHwFail_Object((1,3,6,1,4,1,20044,51,2,3,3,7,4),_PmoabphcAlmLineHwFail_Type())
pmoabphcAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineHwFail.setStatus(_A)
_PmoabphcAlmLineTxOff_Type=EkiOnOff
_PmoabphcAlmLineTxOff_Object=MibScalar
pmoabphcAlmLineTxOff=_PmoabphcAlmLineTxOff_Object((1,3,6,1,4,1,20044,51,2,3,3,7,5),_PmoabphcAlmLineTxOff_Type())
pmoabphcAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineTxOff.setStatus(_A)
_PmoabphcAlmLineDdmWarning_Type=EkiOnOff
_PmoabphcAlmLineDdmWarning_Object=MibScalar
pmoabphcAlmLineDdmWarning=_PmoabphcAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,51,2,3,3,7,9),_PmoabphcAlmLineDdmWarning_Type())
pmoabphcAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineDdmWarning.setStatus(_A)
_PmoabphcAlmLineDdmAlm_Type=EkiOnOff
_PmoabphcAlmLineDdmAlm_Object=MibScalar
pmoabphcAlmLineDdmAlm=_PmoabphcAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,51,2,3,3,7,10),_PmoabphcAlmLineDdmAlm_Type())
pmoabphcAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineDdmAlm.setStatus(_A)
_PmoabphcAlmLineFail_Type=EkiOnOff
_PmoabphcAlmLineFail_Object=MibScalar
pmoabphcAlmLineFail=_PmoabphcAlmLineFail_Object((1,3,6,1,4,1,20044,51,2,3,3,7,12),_PmoabphcAlmLineFail_Type())
pmoabphcAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineFail.setStatus(_A)
_PmoabphcAlmLineExtPumpFail_Type=EkiOnOff
_PmoabphcAlmLineExtPumpFail_Object=MibScalar
pmoabphcAlmLineExtPumpFail=_PmoabphcAlmLineExtPumpFail_Object((1,3,6,1,4,1,20044,51,2,3,3,7,13),_PmoabphcAlmLineExtPumpFail_Type())
pmoabphcAlmLineExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineExtPumpFail.setStatus(_A)
_PmoabphcAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoabphcAlmlineEdfaAlarms2=_PmoabphcAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,51,2,3,3,43))
_PmoabphcAlmLineEdfaNr_Type=EkiOnOff
_PmoabphcAlmLineEdfaNr_Object=MibScalar
pmoabphcAlmLineEdfaNr=_PmoabphcAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,51,2,3,3,43,1),_PmoabphcAlmLineEdfaNr_Type())
pmoabphcAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineEdfaNr.setStatus(_A)
_PmoabphcAlmLineEdfaTecFail_Type=EkiOnOff
_PmoabphcAlmLineEdfaTecFail_Object=MibScalar
pmoabphcAlmLineEdfaTecFail=_PmoabphcAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,51,2,3,3,43,2),_PmoabphcAlmLineEdfaTecFail_Type())
pmoabphcAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineEdfaTecFail.setStatus(_A)
_PmoabphcAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoabphcAlmLineEdfaLaserFail_Object=MibScalar
pmoabphcAlmLineEdfaLaserFail=_PmoabphcAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,51,2,3,3,43,3),_PmoabphcAlmLineEdfaLaserFail_Type())
pmoabphcAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineEdfaLaserFail.setStatus(_A)
_PmoabphcAlmLineEdfaLos_Type=EkiOnOff
_PmoabphcAlmLineEdfaLos_Object=MibScalar
pmoabphcAlmLineEdfaLos=_PmoabphcAlmLineEdfaLos_Object((1,3,6,1,4,1,20044,51,2,3,3,43,4),_PmoabphcAlmLineEdfaLos_Type())
pmoabphcAlmLineEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineEdfaLos.setStatus(_A)
_PmoabphcAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoabphcAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoabphcAlmLineExtPumpEdfaLowCurrent=_PmoabphcAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,51,2,3,3,43,5),_PmoabphcAlmLineExtPumpEdfaLowCurrent_Type())
pmoabphcAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_Pmoabphcmeasures_ObjectIdentity=ObjectIdentity
pmoabphcmeasures=_Pmoabphcmeasures_ObjectIdentity((1,3,6,1,4,1,20044,51,3))
_PmoabphcMesrOther_ObjectIdentity=ObjectIdentity
pmoabphcMesrOther=_PmoabphcMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,51,3,1))
class _PmoabphcMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrtempMeas_Type.__name__=_E
_PmoabphcMesrtempMeas_Object=MibScalar
pmoabphcMesrtempMeas=_PmoabphcMesrtempMeas_Object((1,3,6,1,4,1,20044,51,3,1,72),_PmoabphcMesrtempMeas_Type())
pmoabphcMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrtempMeas.setStatus(_A)
_PmoabphcMesrClient_ObjectIdentity=ObjectIdentity
pmoabphcMesrClient=_PmoabphcMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,51,3,2))
class _PmoabphcMesrclientEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrclientEdfaBiasMeas_Type.__name__=_E
_PmoabphcMesrclientEdfaBiasMeas_Object=MibScalar
pmoabphcMesrclientEdfaBiasMeas=_PmoabphcMesrclientEdfaBiasMeas_Object((1,3,6,1,4,1,20044,51,3,2,32),_PmoabphcMesrclientEdfaBiasMeas_Type())
pmoabphcMesrclientEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrclientEdfaBiasMeas.setStatus(_A)
class _PmoabphcMesrclientEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrclientEdfaTxpwrMeas_Type.__name__=_E
_PmoabphcMesrclientEdfaTxpwrMeas_Object=MibScalar
pmoabphcMesrclientEdfaTxpwrMeas=_PmoabphcMesrclientEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,51,3,2,33),_PmoabphcMesrclientEdfaTxpwrMeas_Type())
pmoabphcMesrclientEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrclientEdfaTxpwrMeas.setStatus(_A)
class _PmoabphcMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrclientEdfaRxpwrMeas_Type.__name__=_E
_PmoabphcMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoabphcMesrclientEdfaRxpwrMeas=_PmoabphcMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,51,3,2,34),_PmoabphcMesrclientEdfaRxpwrMeas_Type())
pmoabphcMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrclientEdfaRxpwrMeas.setStatus(_A)
class _PmoabphcMesrclientEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrclientEdfaGainMeas_Type.__name__=_E
_PmoabphcMesrclientEdfaGainMeas_Object=MibScalar
pmoabphcMesrclientEdfaGainMeas=_PmoabphcMesrclientEdfaGainMeas_Object((1,3,6,1,4,1,20044,51,3,2,35),_PmoabphcMesrclientEdfaGainMeas_Type())
pmoabphcMesrclientEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrclientEdfaGainMeas.setStatus(_A)
class _PmoabphcMesrclientCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrclientCorrectedGain_Type.__name__=_E
_PmoabphcMesrclientCorrectedGain_Object=MibScalar
pmoabphcMesrclientCorrectedGain=_PmoabphcMesrclientCorrectedGain_Object((1,3,6,1,4,1,20044,51,3,2,38),_PmoabphcMesrclientCorrectedGain_Type())
pmoabphcMesrclientCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrclientCorrectedGain.setStatus(_A)
_PmoabphcMesrLine_ObjectIdentity=ObjectIdentity
pmoabphcMesrLine=_PmoabphcMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,51,3,3))
class _PmoabphcMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrlineEdfaBiasMeas_Type.__name__=_E
_PmoabphcMesrlineEdfaBiasMeas_Object=MibScalar
pmoabphcMesrlineEdfaBiasMeas=_PmoabphcMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,51,3,3,40),_PmoabphcMesrlineEdfaBiasMeas_Type())
pmoabphcMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoabphcMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrlineEdfaTxpwrMeas_Type.__name__=_E
_PmoabphcMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoabphcMesrlineEdfaTxpwrMeas=_PmoabphcMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,51,3,3,41),_PmoabphcMesrlineEdfaTxpwrMeas_Type())
pmoabphcMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoabphcMesrlineEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrlineEdfaRxpwrMeas_Type.__name__=_E
_PmoabphcMesrlineEdfaRxpwrMeas_Object=MibScalar
pmoabphcMesrlineEdfaRxpwrMeas=_PmoabphcMesrlineEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,51,3,3,42),_PmoabphcMesrlineEdfaRxpwrMeas_Type())
pmoabphcMesrlineEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrlineEdfaRxpwrMeas.setStatus(_A)
class _PmoabphcMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrlineEdfaGainMeas_Type.__name__=_E
_PmoabphcMesrlineEdfaGainMeas_Object=MibScalar
pmoabphcMesrlineEdfaGainMeas=_PmoabphcMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,51,3,3,43),_PmoabphcMesrlineEdfaGainMeas_Type())
pmoabphcMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrlineEdfaGainMeas.setStatus(_A)
class _PmoabphcMesrlineCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcMesrlineCorrectedGain_Type.__name__=_E
_PmoabphcMesrlineCorrectedGain_Object=MibScalar
pmoabphcMesrlineCorrectedGain=_PmoabphcMesrlineCorrectedGain_Object((1,3,6,1,4,1,20044,51,3,3,46),_PmoabphcMesrlineCorrectedGain_Type())
pmoabphcMesrlineCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcMesrlineCorrectedGain.setStatus(_A)
_PmoabphccontrolsWrite_ObjectIdentity=ObjectIdentity
pmoabphccontrolsWrite=_PmoabphccontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,51,6))
_PmoabphcCtrlOther_ObjectIdentity=ObjectIdentity
pmoabphcCtrlOther=_PmoabphcCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,51,6,1))
_PmoabphcCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoabphcCtrlsynth0=_PmoabphcCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,51,6,1,0))
_PmoabphcCtrlConfLoad_Type=EkiOnOff
_PmoabphcCtrlConfLoad_Object=MibScalar
pmoabphcCtrlConfLoad=_PmoabphcCtrlConfLoad_Object((1,3,6,1,4,1,20044,51,6,1,0,1),_PmoabphcCtrlConfLoad_Type())
pmoabphcCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlConfLoad.setStatus(_A)
_PmoabphcCtrlConfFlash_Type=EkiOnOff
_PmoabphcCtrlConfFlash_Object=MibScalar
pmoabphcCtrlConfFlash=_PmoabphcCtrlConfFlash_Object((1,3,6,1,4,1,20044,51,6,1,0,9),_PmoabphcCtrlConfFlash_Type())
pmoabphcCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlConfFlash.setStatus(_A)
_PmoabphcCtrlConfClear_Type=EkiOnOff
_PmoabphcCtrlConfClear_Object=MibScalar
pmoabphcCtrlConfClear=_PmoabphcCtrlConfClear_Object((1,3,6,1,4,1,20044,51,6,1,0,13),_PmoabphcCtrlConfClear_Type())
pmoabphcCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlConfClear.setStatus(_A)
_PmoabphcCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoabphcCtrlswMgnt=_PmoabphcCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,51,6,1,5))
_PmoabphcCtrlColdReset_Type=EkiOnOff
_PmoabphcCtrlColdReset_Object=MibScalar
pmoabphcCtrlColdReset=_PmoabphcCtrlColdReset_Object((1,3,6,1,4,1,20044,51,6,1,5,2),_PmoabphcCtrlColdReset_Type())
pmoabphcCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlColdReset.setStatus(_A)
_PmoabphcCtrlWarmReset_Type=EkiOnOff
_PmoabphcCtrlWarmReset_Object=MibScalar
pmoabphcCtrlWarmReset=_PmoabphcCtrlWarmReset_Object((1,3,6,1,4,1,20044,51,6,1,5,3),_PmoabphcCtrlWarmReset_Type())
pmoabphcCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlWarmReset.setStatus(_A)
_PmoabphcCtrlledTest_ObjectIdentity=ObjectIdentity
pmoabphcCtrlledTest=_PmoabphcCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,51,6,1,73))
_PmoabphcCtrlGreenLed_Type=EkiOnOff
_PmoabphcCtrlGreenLed_Object=MibScalar
pmoabphcCtrlGreenLed=_PmoabphcCtrlGreenLed_Object((1,3,6,1,4,1,20044,51,6,1,73,1),_PmoabphcCtrlGreenLed_Type())
pmoabphcCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlGreenLed.setStatus(_A)
_PmoabphcCtrlRedLed_Type=EkiOnOff
_PmoabphcCtrlRedLed_Object=MibScalar
pmoabphcCtrlRedLed=_PmoabphcCtrlRedLed_Object((1,3,6,1,4,1,20044,51,6,1,73,2),_PmoabphcCtrlRedLed_Type())
pmoabphcCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlRedLed.setStatus(_A)
_PmoabphcCtrlLedOff_Type=EkiOnOff
_PmoabphcCtrlLedOff_Object=MibScalar
pmoabphcCtrlLedOff=_PmoabphcCtrlLedOff_Object((1,3,6,1,4,1,20044,51,6,1,73,3),_PmoabphcCtrlLedOff_Type())
pmoabphcCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlLedOff.setStatus(_A)
_PmoabphcCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoabphcCtrlmaintMode=_PmoabphcCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,51,6,1,75))
_PmoabphcCtrlMaintenance_Type=EkiOnOff
_PmoabphcCtrlMaintenance_Object=MibScalar
pmoabphcCtrlMaintenance=_PmoabphcCtrlMaintenance_Object((1,3,6,1,4,1,20044,51,6,1,75,1),_PmoabphcCtrlMaintenance_Type())
pmoabphcCtrlMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlMaintenance.setStatus(_A)
_PmoabphcCtrlaprRestart_ObjectIdentity=ObjectIdentity
pmoabphcCtrlaprRestart=_PmoabphcCtrlaprRestart_ObjectIdentity((1,3,6,1,4,1,20044,51,6,1,76))
_PmoabphcCtrlAprManualRestart_Type=EkiOnOff
_PmoabphcCtrlAprManualRestart_Object=MibScalar
pmoabphcCtrlAprManualRestart=_PmoabphcCtrlAprManualRestart_Object((1,3,6,1,4,1,20044,51,6,1,76,1),_PmoabphcCtrlAprManualRestart_Type())
pmoabphcCtrlAprManualRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlAprManualRestart.setStatus(_A)
_PmoabphcCtrlClient_ObjectIdentity=ObjectIdentity
pmoabphcCtrlClient=_PmoabphcCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,51,6,2))
_PmoabphcCtrlclientEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoabphcCtrlclientEdfaLaserOff=_PmoabphcCtrlclientEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,51,6,2,32))
_PmoabphcCtrlClientEdfaLaserOff_Type=EkiOnOff
_PmoabphcCtrlClientEdfaLaserOff_Object=MibScalar
pmoabphcCtrlClientEdfaLaserOff=_PmoabphcCtrlClientEdfaLaserOff_Object((1,3,6,1,4,1,20044,51,6,2,32,1),_PmoabphcCtrlClientEdfaLaserOff_Type())
pmoabphcCtrlClientEdfaLaserOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlClientEdfaLaserOff.setStatus(_A)
class _PmoabphcCtrlclientGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrlclientGainCstMonitorValue_Type.__name__=_E
_PmoabphcCtrlclientGainCstMonitorValue_Object=MibScalar
pmoabphcCtrlclientGainCstMonitorValue=_PmoabphcCtrlclientGainCstMonitorValue_Object((1,3,6,1,4,1,20044,51,6,2,34),_PmoabphcCtrlclientGainCstMonitorValue_Type())
pmoabphcCtrlclientGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlclientGainCstMonitorValue.setStatus(_A)
class _PmoabphcCtrlclientGainCstPoutValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrlclientGainCstPoutValue_Type.__name__=_E
_PmoabphcCtrlclientGainCstPoutValue_Object=MibScalar
pmoabphcCtrlclientGainCstPoutValue=_PmoabphcCtrlclientGainCstPoutValue_Object((1,3,6,1,4,1,20044,51,6,2,35),_PmoabphcCtrlclientGainCstPoutValue_Type())
pmoabphcCtrlclientGainCstPoutValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlclientGainCstPoutValue.setStatus(_A)
class _PmoabphcCtrlclientGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrlclientGainSettingValue_Type.__name__=_E
_PmoabphcCtrlclientGainSettingValue_Object=MibScalar
pmoabphcCtrlclientGainSettingValue=_PmoabphcCtrlclientGainSettingValue_Object((1,3,6,1,4,1,20044,51,6,2,36),_PmoabphcCtrlclientGainSettingValue_Type())
pmoabphcCtrlclientGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlclientGainSettingValue.setStatus(_A)
_PmoabphcCtrlclientGainProcessing_ObjectIdentity=ObjectIdentity
pmoabphcCtrlclientGainProcessing=_PmoabphcCtrlclientGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,51,6,2,37))
_PmoabphcCtrlClientGainProc_Type=EkiOnOff
_PmoabphcCtrlClientGainProc_Object=MibScalar
pmoabphcCtrlClientGainProc=_PmoabphcCtrlClientGainProc_Object((1,3,6,1,4,1,20044,51,6,2,37,1),_PmoabphcCtrlClientGainProc_Type())
pmoabphcCtrlClientGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlClientGainProc.setStatus(_A)
class _PmoabphcCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrlclientGainCstFiberAgingMarginValue_Type.__name__=_E
_PmoabphcCtrlclientGainCstFiberAgingMarginValue_Object=MibScalar
pmoabphcCtrlclientGainCstFiberAgingMarginValue=_PmoabphcCtrlclientGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,51,6,2,38),_PmoabphcCtrlclientGainCstFiberAgingMarginValue_Type())
pmoabphcCtrlclientGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlclientGainCstFiberAgingMarginValue.setStatus(_A)
class _PmoabphcCtrlclientGainCstAdddropMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrlclientGainCstAdddropMarginValue_Type.__name__=_E
_PmoabphcCtrlclientGainCstAdddropMarginValue_Object=MibScalar
pmoabphcCtrlclientGainCstAdddropMarginValue=_PmoabphcCtrlclientGainCstAdddropMarginValue_Object((1,3,6,1,4,1,20044,51,6,2,39),_PmoabphcCtrlclientGainCstAdddropMarginValue_Type())
pmoabphcCtrlclientGainCstAdddropMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlclientGainCstAdddropMarginValue.setStatus(_A)
_PmoabphcCtrlLine_ObjectIdentity=ObjectIdentity
pmoabphcCtrlLine=_PmoabphcCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,51,6,3))
_PmoabphcCtrllineEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoabphcCtrllineEdfaLaserOff=_PmoabphcCtrllineEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,51,6,3,40))
_PmoabphcCtrlLineEdfaLaserOff_Type=EkiOnOff
_PmoabphcCtrlLineEdfaLaserOff_Object=MibScalar
pmoabphcCtrlLineEdfaLaserOff=_PmoabphcCtrlLineEdfaLaserOff_Object((1,3,6,1,4,1,20044,51,6,3,40,1),_PmoabphcCtrlLineEdfaLaserOff_Type())
pmoabphcCtrlLineEdfaLaserOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlLineEdfaLaserOff.setStatus(_A)
class _PmoabphcCtrllineGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrllineGainCstMonitorValue_Type.__name__=_E
_PmoabphcCtrllineGainCstMonitorValue_Object=MibScalar
pmoabphcCtrllineGainCstMonitorValue=_PmoabphcCtrllineGainCstMonitorValue_Object((1,3,6,1,4,1,20044,51,6,3,42),_PmoabphcCtrllineGainCstMonitorValue_Type())
pmoabphcCtrllineGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrllineGainCstMonitorValue.setStatus(_A)
class _PmoabphcCtrllineGainCstPoutValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrllineGainCstPoutValue_Type.__name__=_E
_PmoabphcCtrllineGainCstPoutValue_Object=MibScalar
pmoabphcCtrllineGainCstPoutValue=_PmoabphcCtrllineGainCstPoutValue_Object((1,3,6,1,4,1,20044,51,6,3,43),_PmoabphcCtrllineGainCstPoutValue_Type())
pmoabphcCtrllineGainCstPoutValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrllineGainCstPoutValue.setStatus(_A)
class _PmoabphcCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrllineGainSettingValue_Type.__name__=_E
_PmoabphcCtrllineGainSettingValue_Object=MibScalar
pmoabphcCtrllineGainSettingValue=_PmoabphcCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,51,6,3,44),_PmoabphcCtrllineGainSettingValue_Type())
pmoabphcCtrllineGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrllineGainSettingValue.setStatus(_A)
_PmoabphcCtrllineGainProcessing_ObjectIdentity=ObjectIdentity
pmoabphcCtrllineGainProcessing=_PmoabphcCtrllineGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,51,6,3,45))
_PmoabphcCtrlLineGainProc_Type=EkiOnOff
_PmoabphcCtrlLineGainProc_Object=MibScalar
pmoabphcCtrlLineGainProc=_PmoabphcCtrlLineGainProc_Object((1,3,6,1,4,1,20044,51,6,3,45,1),_PmoabphcCtrlLineGainProc_Type())
pmoabphcCtrlLineGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrlLineGainProc.setStatus(_A)
class _PmoabphcCtrllineGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrllineGainCstFiberAgingMarginValue_Type.__name__=_E
_PmoabphcCtrllineGainCstFiberAgingMarginValue_Object=MibScalar
pmoabphcCtrllineGainCstFiberAgingMarginValue=_PmoabphcCtrllineGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,51,6,3,46),_PmoabphcCtrllineGainCstFiberAgingMarginValue_Type())
pmoabphcCtrllineGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrllineGainCstFiberAgingMarginValue.setStatus(_A)
class _PmoabphcCtrllineGainCstAdddropMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcCtrllineGainCstAdddropMarginValue_Type.__name__=_E
_PmoabphcCtrllineGainCstAdddropMarginValue_Object=MibScalar
pmoabphcCtrllineGainCstAdddropMarginValue=_PmoabphcCtrllineGainCstAdddropMarginValue_Object((1,3,6,1,4,1,20044,51,6,3,47),_PmoabphcCtrllineGainCstAdddropMarginValue_Type())
pmoabphcCtrllineGainCstAdddropMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCtrllineGainCstAdddropMarginValue.setStatus(_A)
_Pmoabphcri_ObjectIdentity=ObjectIdentity
pmoabphcri=_Pmoabphcri_ObjectIdentity((1,3,6,1,4,1,20044,51,7))
_PmoabphcRinvReloadInventory_Type=EkiOnOff
_PmoabphcRinvReloadInventory_Object=MibScalar
pmoabphcRinvReloadInventory=_PmoabphcRinvReloadInventory_Object((1,3,6,1,4,1,20044,51,7,2),_PmoabphcRinvReloadInventory_Type())
pmoabphcRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcRinvReloadInventory.setStatus(_A)
_PmoabphcRinvModulePlatform_Type=DisplayString
_PmoabphcRinvModulePlatform_Object=MibScalar
pmoabphcRinvModulePlatform=_PmoabphcRinvModulePlatform_Object((1,3,6,1,4,1,20044,51,7,3),_PmoabphcRinvModulePlatform_Type())
pmoabphcRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvModulePlatform.setStatus(_A)
_PmoabphcRinvSwPlatform_Type=DisplayString
_PmoabphcRinvSwPlatform_Object=MibScalar
pmoabphcRinvSwPlatform=_PmoabphcRinvSwPlatform_Object((1,3,6,1,4,1,20044,51,7,4),_PmoabphcRinvSwPlatform_Type())
pmoabphcRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvSwPlatform.setStatus(_A)
_PmoabphcRinvSwFoa_Type=DisplayString
_PmoabphcRinvSwFoa_Object=MibScalar
pmoabphcRinvSwFoa=_PmoabphcRinvSwFoa_Object((1,3,6,1,4,1,20044,51,7,5),_PmoabphcRinvSwFoa_Type())
pmoabphcRinvSwFoa.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvSwFoa.setStatus(_A)
_PmoabphcRinvBoosterTable_Object=MibTable
pmoabphcRinvBoosterTable=_PmoabphcRinvBoosterTable_Object((1,3,6,1,4,1,20044,51,7,6))
if mibBuilder.loadTexts:pmoabphcRinvBoosterTable.setStatus(_A)
_PmoabphcRinvBoosterEntry_Object=MibTableRow
pmoabphcRinvBoosterEntry=_PmoabphcRinvBoosterEntry_Object((1,3,6,1,4,1,20044,51,7,6,1))
pmoabphcRinvBoosterEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:pmoabphcRinvBoosterEntry.setStatus(_A)
class _PmoabphcRinvBoosterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoabphcRinvBoosterIndex_Type.__name__=_E
_PmoabphcRinvBoosterIndex_Object=MibTableColumn
pmoabphcRinvBoosterIndex=_PmoabphcRinvBoosterIndex_Object((1,3,6,1,4,1,20044,51,7,6,1,1),_PmoabphcRinvBoosterIndex_Type())
pmoabphcRinvBoosterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvBoosterIndex.setStatus(_A)
_PmoabphcRinvBooster_Type=DisplayString
_PmoabphcRinvBooster_Object=MibTableColumn
pmoabphcRinvBooster=_PmoabphcRinvBooster_Object((1,3,6,1,4,1,20044,51,7,6,1,2),_PmoabphcRinvBooster_Type())
pmoabphcRinvBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvBooster.setStatus(_A)
_PmoabphcRinvPreAmpTable_Object=MibTable
pmoabphcRinvPreAmpTable=_PmoabphcRinvPreAmpTable_Object((1,3,6,1,4,1,20044,51,7,7))
if mibBuilder.loadTexts:pmoabphcRinvPreAmpTable.setStatus(_A)
_PmoabphcRinvPreAmpEntry_Object=MibTableRow
pmoabphcRinvPreAmpEntry=_PmoabphcRinvPreAmpEntry_Object((1,3,6,1,4,1,20044,51,7,7,1))
pmoabphcRinvPreAmpEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:pmoabphcRinvPreAmpEntry.setStatus(_A)
class _PmoabphcRinvPreAmpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoabphcRinvPreAmpIndex_Type.__name__=_E
_PmoabphcRinvPreAmpIndex_Object=MibTableColumn
pmoabphcRinvPreAmpIndex=_PmoabphcRinvPreAmpIndex_Object((1,3,6,1,4,1,20044,51,7,7,1,1),_PmoabphcRinvPreAmpIndex_Type())
pmoabphcRinvPreAmpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvPreAmpIndex.setStatus(_A)
_PmoabphcRinvPreAmp_Type=DisplayString
_PmoabphcRinvPreAmp_Object=MibTableColumn
pmoabphcRinvPreAmp=_PmoabphcRinvPreAmp_Object((1,3,6,1,4,1,20044,51,7,7,1,2),_PmoabphcRinvPreAmp_Type())
pmoabphcRinvPreAmp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcRinvPreAmp.setStatus(_A)
_PmoabphcConfig_ObjectIdentity=ObjectIdentity
pmoabphcConfig=_PmoabphcConfig_ObjectIdentity((1,3,6,1,4,1,20044,51,9))
_PmoabphcCfgNoValue_ObjectIdentity=ObjectIdentity
pmoabphcCfgNoValue=_PmoabphcCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,51,9,1))
_PmoabphctableclientStartup_ObjectIdentity=ObjectIdentity
pmoabphctableclientStartup=_PmoabphctableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,51,9,1,1))
class _PmoabphcCfgclientEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientEdfaLaserCtrl_Type.__name__=_F
_PmoabphcCfgclientEdfaLaserCtrl_Object=MibScalar
pmoabphcCfgclientEdfaLaserCtrl=_PmoabphcCfgclientEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,51,9,1,1,2),_PmoabphcCfgclientEdfaLaserCtrl_Type())
pmoabphcCfgclientEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientEdfaLaserCtrl.setStatus(_A)
class _PmoabphcCfgclientEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientEdfaLaserMode_Type.__name__=_F
_PmoabphcCfgclientEdfaLaserMode_Object=MibScalar
pmoabphcCfgclientEdfaLaserMode=_PmoabphcCfgclientEdfaLaserMode_Object((1,3,6,1,4,1,20044,51,9,1,1,3),_PmoabphcCfgclientEdfaLaserMode_Type())
pmoabphcCfgclientEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientEdfaLaserMode.setStatus(_A)
class _PmoabphcCfgclientGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientGainValue_Type.__name__=_F
_PmoabphcCfgclientGainValue_Object=MibScalar
pmoabphcCfgclientGainValue=_PmoabphcCfgclientGainValue_Object((1,3,6,1,4,1,20044,51,9,1,1,4),_PmoabphcCfgclientGainValue_Type())
pmoabphcCfgclientGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientGainValue.setStatus(_A)
class _PmoabphcCfgclientTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientTiltValue_Type.__name__=_F
_PmoabphcCfgclientTiltValue_Object=MibScalar
pmoabphcCfgclientTiltValue=_PmoabphcCfgclientTiltValue_Object((1,3,6,1,4,1,20044,51,9,1,1,5),_PmoabphcCfgclientTiltValue_Type())
pmoabphcCfgclientTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientTiltValue.setStatus(_A)
class _PmoabphcCfgclientMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientMsaLoss_Type.__name__=_F
_PmoabphcCfgclientMsaLoss_Object=MibScalar
pmoabphcCfgclientMsaLoss=_PmoabphcCfgclientMsaLoss_Object((1,3,6,1,4,1,20044,51,9,1,1,6),_PmoabphcCfgclientMsaLoss_Type())
pmoabphcCfgclientMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientMsaLoss.setStatus(_A)
class _PmoabphcCfgclientOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientOutputPowerValue_Type.__name__=_F
_PmoabphcCfgclientOutputPowerValue_Object=MibScalar
pmoabphcCfgclientOutputPowerValue=_PmoabphcCfgclientOutputPowerValue_Object((1,3,6,1,4,1,20044,51,9,1,1,7),_PmoabphcCfgclientOutputPowerValue_Type())
pmoabphcCfgclientOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientOutputPowerValue.setStatus(_A)
class _PmoabphcCfgclientAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgclientAseCompensation_Type.__name__=_F
_PmoabphcCfgclientAseCompensation_Object=MibScalar
pmoabphcCfgclientAseCompensation=_PmoabphcCfgclientAseCompensation_Object((1,3,6,1,4,1,20044,51,9,1,1,8),_PmoabphcCfgclientAseCompensation_Type())
pmoabphcCfgclientAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgclientAseCompensation.setStatus(_A)
_PmoabphcCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoabphcCfgLineStartUp=_PmoabphcCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,51,9,2))
_PmoabphctablelineStartup_ObjectIdentity=ObjectIdentity
pmoabphctablelineStartup=_PmoabphctablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,51,9,2,1))
class _PmoabphcCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineEdfaLaserCtrl_Type.__name__=_F
_PmoabphcCfglineEdfaLaserCtrl_Object=MibScalar
pmoabphcCfglineEdfaLaserCtrl=_PmoabphcCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,51,9,2,1,2),_PmoabphcCfglineEdfaLaserCtrl_Type())
pmoabphcCfglineEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoabphcCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineEdfaLaserMode_Type.__name__=_F
_PmoabphcCfglineEdfaLaserMode_Object=MibScalar
pmoabphcCfglineEdfaLaserMode=_PmoabphcCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,51,9,2,1,3),_PmoabphcCfglineEdfaLaserMode_Type())
pmoabphcCfglineEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineEdfaLaserMode.setStatus(_A)
class _PmoabphcCfglineGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineGainValue_Type.__name__=_F
_PmoabphcCfglineGainValue_Object=MibScalar
pmoabphcCfglineGainValue=_PmoabphcCfglineGainValue_Object((1,3,6,1,4,1,20044,51,9,2,1,4),_PmoabphcCfglineGainValue_Type())
pmoabphcCfglineGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineGainValue.setStatus(_A)
class _PmoabphcCfglineTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineTiltValue_Type.__name__=_F
_PmoabphcCfglineTiltValue_Object=MibScalar
pmoabphcCfglineTiltValue=_PmoabphcCfglineTiltValue_Object((1,3,6,1,4,1,20044,51,9,2,1,5),_PmoabphcCfglineTiltValue_Type())
pmoabphcCfglineTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineTiltValue.setStatus(_A)
class _PmoabphcCfglineMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineMsaLoss_Type.__name__=_F
_PmoabphcCfglineMsaLoss_Object=MibScalar
pmoabphcCfglineMsaLoss=_PmoabphcCfglineMsaLoss_Object((1,3,6,1,4,1,20044,51,9,2,1,6),_PmoabphcCfglineMsaLoss_Type())
pmoabphcCfglineMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineMsaLoss.setStatus(_A)
class _PmoabphcCfglineOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineOutputPowerValue_Type.__name__=_F
_PmoabphcCfglineOutputPowerValue_Object=MibScalar
pmoabphcCfglineOutputPowerValue=_PmoabphcCfglineOutputPowerValue_Object((1,3,6,1,4,1,20044,51,9,2,1,7),_PmoabphcCfglineOutputPowerValue_Type())
pmoabphcCfglineOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineOutputPowerValue.setStatus(_A)
class _PmoabphcCfglineAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfglineAseCompensation_Type.__name__=_F
_PmoabphcCfglineAseCompensation_Object=MibScalar
pmoabphcCfglineAseCompensation=_PmoabphcCfglineAseCompensation_Object((1,3,6,1,4,1,20044,51,9,2,1,8),_PmoabphcCfglineAseCompensation_Type())
pmoabphcCfglineAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfglineAseCompensation.setStatus(_A)
class _PmoabphcCfgaprMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcCfgaprMode_Type.__name__=_F
_PmoabphcCfgaprMode_Object=MibScalar
pmoabphcCfgaprMode=_PmoabphcCfgaprMode_Object((1,3,6,1,4,1,20044,51,9,2,1,11),_PmoabphcCfgaprMode_Type())
pmoabphcCfgaprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgaprMode.setStatus(_A)
_PmoabphcCfgLabels_ObjectIdentity=ObjectIdentity
pmoabphcCfgLabels=_PmoabphcCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,51,9,3))
_PmoabphcCfgLabelclientTable_Object=MibTable
pmoabphcCfgLabelclientTable=_PmoabphcCfgLabelclientTable_Object((1,3,6,1,4,1,20044,51,9,3,1))
if mibBuilder.loadTexts:pmoabphcCfgLabelclientTable.setStatus(_A)
_PmoabphcCfgLabelclientEntry_Object=MibTableRow
pmoabphcCfgLabelclientEntry=_PmoabphcCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,51,9,3,1,1))
pmoabphcCfgLabelclientEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:pmoabphcCfgLabelclientEntry.setStatus(_A)
class _PmoabphcCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcCfgLabelclientIndex_Type.__name__=_E
_PmoabphcCfgLabelclientIndex_Object=MibTableColumn
pmoabphcCfgLabelclientIndex=_PmoabphcCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,51,9,3,1,1,1),_PmoabphcCfgLabelclientIndex_Type())
pmoabphcCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcCfgLabelclientIndex.setStatus(_A)
class _PmoabphcCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoabphcCfgLabelclientPortn_Type.__name__=_H
_PmoabphcCfgLabelclientPortn_Object=MibTableColumn
pmoabphcCfgLabelclientPortn=_PmoabphcCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,51,9,3,1,1,3),_PmoabphcCfgLabelclientPortn_Type())
pmoabphcCfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgLabelclientPortn.setStatus(_A)
_PmoabphcCfgLabellineTable_Object=MibTable
pmoabphcCfgLabellineTable=_PmoabphcCfgLabellineTable_Object((1,3,6,1,4,1,20044,51,9,3,2))
if mibBuilder.loadTexts:pmoabphcCfgLabellineTable.setStatus(_A)
_PmoabphcCfgLabellineEntry_Object=MibTableRow
pmoabphcCfgLabellineEntry=_PmoabphcCfgLabellineEntry_Object((1,3,6,1,4,1,20044,51,9,3,2,1))
pmoabphcCfgLabellineEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:pmoabphcCfgLabellineEntry.setStatus(_A)
class _PmoabphcCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcCfgLabellineIndex_Type.__name__=_E
_PmoabphcCfgLabellineIndex_Object=MibTableColumn
pmoabphcCfgLabellineIndex=_PmoabphcCfgLabellineIndex_Object((1,3,6,1,4,1,20044,51,9,3,2,1,1),_PmoabphcCfgLabellineIndex_Type())
pmoabphcCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcCfgLabellineIndex.setStatus(_A)
class _PmoabphcCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoabphcCfgLabellinePortn_Type.__name__=_H
_PmoabphcCfgLabellinePortn_Object=MibTableColumn
pmoabphcCfgLabellinePortn=_PmoabphcCfgLabellinePortn_Object((1,3,6,1,4,1,20044,51,9,3,2,1,3),_PmoabphcCfgLabellinePortn_Type())
pmoabphcCfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgLabellinePortn.setStatus(_A)
_PmoabphcCfgWriteConfiguration_Type=EkiOnOff
_PmoabphcCfgWriteConfiguration_Object=MibScalar
pmoabphcCfgWriteConfiguration=_PmoabphcCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,51,9,257),_PmoabphcCfgWriteConfiguration_Type())
pmoabphcCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcCfgWriteConfiguration.setStatus(_A)
_Pmoabphctraps_ObjectIdentity=ObjectIdentity
pmoabphctraps=_Pmoabphctraps_ObjectIdentity((1,3,6,1,4,1,20044,51,10))
class _PmoabphctrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoabphctrapBoardNumber_Type.__name__=_E
_PmoabphctrapBoardNumber_Object=MibScalar
pmoabphctrapBoardNumber=_PmoabphctrapBoardNumber_Object((1,3,6,1,4,1,20044,51,10,4),_PmoabphctrapBoardNumber_Type())
pmoabphctrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphctrapBoardNumber.setStatus(_A)
pmoabphcLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,30))
pmoabphcLineTrapNotUrgentGoesOn.setObjects(*((_D,_I),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcLineTrapNotUrgentGoesOn.setStatus(_A)
pmoabphcLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,31))
pmoabphcLineTrapNotUrgentGoesOff.setObjects(*((_D,_I),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcLineTrapNotUrgentGoesOff.setStatus(_A)
pmoabphcLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,32))
pmoabphcLineTrapUrgentGoesOn.setObjects(*((_D,_J),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcLineTrapUrgentGoesOn.setStatus(_A)
pmoabphcLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,33))
pmoabphcLineTrapUrgentGoesOff.setObjects(*((_D,_J),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcLineTrapUrgentGoesOff.setStatus(_A)
pmoabphcLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,34))
pmoabphcLineTrapCritGoesOn.setObjects(*((_D,_K),(_D,_L),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcLineTrapCritGoesOn.setStatus(_A)
pmoabphcLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,35))
pmoabphcLineTrapCritGoesOff.setObjects(*((_D,_K),(_D,_L),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcLineTrapCritGoesOff.setStatus(_A)
pmoabphcClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,40))
pmoabphcClientTrapNotUrgentGoesOn.setObjects(*((_D,_M),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcClientTrapNotUrgentGoesOn.setStatus(_A)
pmoabphcClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,41))
pmoabphcClientTrapNotUrgentGoesOff.setObjects(*((_D,_M),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcClientTrapNotUrgentGoesOff.setStatus(_A)
pmoabphcClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,42))
pmoabphcClientTrapUrgentGoesOn.setObjects(*((_D,_N),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcClientTrapUrgentGoesOn.setStatus(_A)
pmoabphcClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,43))
pmoabphcClientTrapUrgentGoesOff.setObjects(*((_D,_N),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcClientTrapUrgentGoesOff.setStatus(_A)
pmoabphcClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,44))
pmoabphcClientTrapCritGoesOn.setObjects(*((_D,_O),(_D,_P),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcClientTrapCritGoesOn.setStatus(_A)
pmoabphcClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,45))
pmoabphcClientTrapCritGoesOff.setObjects(*((_D,_O),(_D,_P),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcClientTrapCritGoesOff.setStatus(_A)
pmoabphcPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,51,10,50))
pmoabphcPowerTrapUrgentGoesOn.setObjects(*((_D,_Q),(_D,_R),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcPowerTrapUrgentGoesOn.setStatus(_A)
pmoabphcPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,51,10,51))
pmoabphcPowerTrapUrgentGoesOff.setObjects(*((_D,_Q),(_D,_R),(_D,_G)))
if mibBuilder.loadTexts:pmoabphcPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PmoabphcpreampMode':PmoabphcpreampMode,'PmoabphcboosterMode':PmoabphcboosterMode,'PmoabphcaprMode':PmoabphcaprMode,'PmoabphcPreampGainAdjMode':PmoabphcPreampGainAdjMode,'PmoabphcBoosterGainAdjMode':PmoabphcBoosterGainAdjMode,'PmoabphcPreampCstGainAdjMode':PmoabphcPreampCstGainAdjMode,'PmoabphcBoosterCstGainAdjMode':PmoabphcBoosterCstGainAdjMode,'modulepmoabphc':modulepmoabphc,'pmoabphcalarms':pmoabphcalarms,'pmoabphcAlmOther':pmoabphcAlmOther,'pmoabphcAlmOtherNurg':pmoabphcAlmOtherNurg,'pmoabphcAlmsynthAlm2':pmoabphcAlmsynthAlm2,'pmoabphcAlmConfTableSave':pmoabphcAlmConfTableSave,'pmoabphcAlmInvUpload':pmoabphcAlmInvUpload,'pmoabphcAlmConfTableLoad':pmoabphcAlmConfTableLoad,'pmoabphcAlmfoaWarnings':pmoabphcAlmfoaWarnings,'pmoabphcAlmTermpLowWarning':pmoabphcAlmTermpLowWarning,'pmoabphcAlmTempHighWarning':pmoabphcAlmTempHighWarning,'pmoabphcAlmOtherUrg':pmoabphcAlmOtherUrg,'pmoabphcAlmfoaAlarms':pmoabphcAlmfoaAlarms,'pmoabphcAlmTermpLowAlarm':pmoabphcAlmTermpLowAlarm,'pmoabphcAlmTempHighAlarm':pmoabphcAlmTempHighAlarm,'pmoabphcAlmOtherCrit':pmoabphcAlmOtherCrit,'pmoabphcAlmsynthAlm0':pmoabphcAlmsynthAlm0,'pmoabphcAlmMaintenanceMode':pmoabphcAlmMaintenanceMode,'pmoabphcAlmAprOn':pmoabphcAlmAprOn,'pmoabphcAlmModGlobFail':pmoabphcAlmModGlobFail,'pmoabphcAlmUpEdfaInitNotCompl':pmoabphcAlmUpEdfaInitNotCompl,'pmoabphcAlmDwEdfaInitNotCompl':pmoabphcAlmDwEdfaInitNotCompl,'pmoabphcAlmExtPump1NotLocked':pmoabphcAlmExtPump1NotLocked,'pmoabphcAlmExtPump2NotLocked':pmoabphcAlmExtPump2NotLocked,_R:pmoabphcAlmDefFuseA,_Q:pmoabphcAlmDefFuseB,'pmoabphcAlmClient':pmoabphcAlmClient,'pmoabphcAlmClientNurg':pmoabphcAlmClientNurg,'pmoabphcAlmclientEdfaWarnings':pmoabphcAlmclientEdfaWarnings,'pmoabphcAlmClientGainLowWarning':pmoabphcAlmClientGainLowWarning,'pmoabphcAlmClientGainHighWarning':pmoabphcAlmClientGainHighWarning,'pmoabphcAlmClientInputPwrLowWarning':pmoabphcAlmClientInputPwrLowWarning,'pmoabphcAlmClientInputPwrHighWarning':pmoabphcAlmClientInputPwrHighWarning,'pmoabphcAlmClientOutputPwrLowWarning':pmoabphcAlmClientOutputPwrLowWarning,'pmoabphcAlmClientOutputPwrHighWarning':pmoabphcAlmClientOutputPwrHighWarning,'pmoabphcAlmClientBiasLowWarning':pmoabphcAlmClientBiasLowWarning,'pmoabphcAlmClientBiasHighWarning':pmoabphcAlmClientBiasHighWarning,'pmoabphcAlmClientUrg':pmoabphcAlmClientUrg,'pmoabphcAlmclientEdfaAlarms1':pmoabphcAlmclientEdfaAlarms1,'pmoabphcAlmClientGainLowAlarm':pmoabphcAlmClientGainLowAlarm,'pmoabphcAlmClientGainHighAlarm':pmoabphcAlmClientGainHighAlarm,'pmoabphcAlmClientInputPwrLowAlarm':pmoabphcAlmClientInputPwrLowAlarm,'pmoabphcAlmClientInputPwrHighAlarm':pmoabphcAlmClientInputPwrHighAlarm,'pmoabphcAlmClientOutputPwrLowAlarm':pmoabphcAlmClientOutputPwrLowAlarm,'pmoabphcAlmClientOutputPwrHighAlarm':pmoabphcAlmClientOutputPwrHighAlarm,'pmoabphcAlmClientBiasLowAlarm':pmoabphcAlmClientBiasLowAlarm,'pmoabphcAlmClientBiasHighAlarm':pmoabphcAlmClientBiasHighAlarm,'pmoabphcAlmClientCrit':pmoabphcAlmClientCrit,'pmoabphcAlmsynthAlm8':pmoabphcAlmsynthAlm8,_P:pmoabphcAlmClientHwFail,'pmoabphcAlmClientTxOff':pmoabphcAlmClientTxOff,_M:pmoabphcAlmClientDdmWarning,_N:pmoabphcAlmClientDdmAlm,_O:pmoabphcAlmClientFail,'pmoabphcAlmClientExtPumpFail':pmoabphcAlmClientExtPumpFail,'pmoabphcAlmclientEdfaAlarms2':pmoabphcAlmclientEdfaAlarms2,'pmoabphcAlmClientEdfaNr':pmoabphcAlmClientEdfaNr,'pmoabphcAlmClientEdfaTecFail':pmoabphcAlmClientEdfaTecFail,'pmoabphcAlmClientEdfaLaserFail':pmoabphcAlmClientEdfaLaserFail,'pmoabphcAlmClientEdfaLos':pmoabphcAlmClientEdfaLos,'pmoabphcAlmClientExtPumpEdfaLowCurrent':pmoabphcAlmClientExtPumpEdfaLowCurrent,'pmoabphcAlmLine':pmoabphcAlmLine,'pmoabphcAlmLineNurg':pmoabphcAlmLineNurg,'pmoabphcAlmlineEdfaWarnings':pmoabphcAlmlineEdfaWarnings,'pmoabphcAlmLineGainLowWarning':pmoabphcAlmLineGainLowWarning,'pmoabphcAlmLineGainHighWarning':pmoabphcAlmLineGainHighWarning,'pmoabphcAlmLineInputPwrLowWarning':pmoabphcAlmLineInputPwrLowWarning,'pmoabphcAlmLineInputPwrHighWarning':pmoabphcAlmLineInputPwrHighWarning,'pmoabphcAlmLineOutputPwrLowWarning':pmoabphcAlmLineOutputPwrLowWarning,'pmoabphcAlmLineOutputPwrHighWarning':pmoabphcAlmLineOutputPwrHighWarning,'pmoabphcAlmLineBiasLowWarning':pmoabphcAlmLineBiasLowWarning,'pmoabphcAlmLineBiasHighWarning':pmoabphcAlmLineBiasHighWarning,'pmoabphcAlmLineUrg':pmoabphcAlmLineUrg,'pmoabphcAlmlineEdfaAlarms1':pmoabphcAlmlineEdfaAlarms1,'pmoabphcAlmLineGainLowAlarm':pmoabphcAlmLineGainLowAlarm,'pmoabphcAlmLineGainHighAlarm':pmoabphcAlmLineGainHighAlarm,'pmoabphcAlmLineInputPwrLowAlarm':pmoabphcAlmLineInputPwrLowAlarm,'pmoabphcAlmLineInputPwrHighAlarm':pmoabphcAlmLineInputPwrHighAlarm,'pmoabphcAlmLineOutputPwrLowAlarm':pmoabphcAlmLineOutputPwrLowAlarm,'pmoabphcAlmLineOutputPwrHighAlarm':pmoabphcAlmLineOutputPwrHighAlarm,'pmoabphcAlmLineBiasLowAlarm':pmoabphcAlmLineBiasLowAlarm,'pmoabphcAlmLineBiasHighAlarm':pmoabphcAlmLineBiasHighAlarm,'pmoabphcAlmLineCrit':pmoabphcAlmLineCrit,'pmoabphcAlmsynthAlm7':pmoabphcAlmsynthAlm7,_L:pmoabphcAlmLineHwFail,'pmoabphcAlmLineTxOff':pmoabphcAlmLineTxOff,_I:pmoabphcAlmLineDdmWarning,_J:pmoabphcAlmLineDdmAlm,_K:pmoabphcAlmLineFail,'pmoabphcAlmLineExtPumpFail':pmoabphcAlmLineExtPumpFail,'pmoabphcAlmlineEdfaAlarms2':pmoabphcAlmlineEdfaAlarms2,'pmoabphcAlmLineEdfaNr':pmoabphcAlmLineEdfaNr,'pmoabphcAlmLineEdfaTecFail':pmoabphcAlmLineEdfaTecFail,'pmoabphcAlmLineEdfaLaserFail':pmoabphcAlmLineEdfaLaserFail,'pmoabphcAlmLineEdfaLos':pmoabphcAlmLineEdfaLos,'pmoabphcAlmLineExtPumpEdfaLowCurrent':pmoabphcAlmLineExtPumpEdfaLowCurrent,'pmoabphcmeasures':pmoabphcmeasures,'pmoabphcMesrOther':pmoabphcMesrOther,'pmoabphcMesrtempMeas':pmoabphcMesrtempMeas,'pmoabphcMesrClient':pmoabphcMesrClient,'pmoabphcMesrclientEdfaBiasMeas':pmoabphcMesrclientEdfaBiasMeas,'pmoabphcMesrclientEdfaTxpwrMeas':pmoabphcMesrclientEdfaTxpwrMeas,'pmoabphcMesrclientEdfaRxpwrMeas':pmoabphcMesrclientEdfaRxpwrMeas,'pmoabphcMesrclientEdfaGainMeas':pmoabphcMesrclientEdfaGainMeas,'pmoabphcMesrclientCorrectedGain':pmoabphcMesrclientCorrectedGain,'pmoabphcMesrLine':pmoabphcMesrLine,'pmoabphcMesrlineEdfaBiasMeas':pmoabphcMesrlineEdfaBiasMeas,'pmoabphcMesrlineEdfaTxpwrMeas':pmoabphcMesrlineEdfaTxpwrMeas,'pmoabphcMesrlineEdfaRxpwrMeas':pmoabphcMesrlineEdfaRxpwrMeas,'pmoabphcMesrlineEdfaGainMeas':pmoabphcMesrlineEdfaGainMeas,'pmoabphcMesrlineCorrectedGain':pmoabphcMesrlineCorrectedGain,'pmoabphccontrolsWrite':pmoabphccontrolsWrite,'pmoabphcCtrlOther':pmoabphcCtrlOther,'pmoabphcCtrlsynth0':pmoabphcCtrlsynth0,'pmoabphcCtrlConfLoad':pmoabphcCtrlConfLoad,'pmoabphcCtrlConfFlash':pmoabphcCtrlConfFlash,'pmoabphcCtrlConfClear':pmoabphcCtrlConfClear,'pmoabphcCtrlswMgnt':pmoabphcCtrlswMgnt,'pmoabphcCtrlColdReset':pmoabphcCtrlColdReset,'pmoabphcCtrlWarmReset':pmoabphcCtrlWarmReset,'pmoabphcCtrlledTest':pmoabphcCtrlledTest,'pmoabphcCtrlGreenLed':pmoabphcCtrlGreenLed,'pmoabphcCtrlRedLed':pmoabphcCtrlRedLed,'pmoabphcCtrlLedOff':pmoabphcCtrlLedOff,'pmoabphcCtrlmaintMode':pmoabphcCtrlmaintMode,'pmoabphcCtrlMaintenance':pmoabphcCtrlMaintenance,'pmoabphcCtrlaprRestart':pmoabphcCtrlaprRestart,'pmoabphcCtrlAprManualRestart':pmoabphcCtrlAprManualRestart,'pmoabphcCtrlClient':pmoabphcCtrlClient,'pmoabphcCtrlclientEdfaLaserOff':pmoabphcCtrlclientEdfaLaserOff,'pmoabphcCtrlClientEdfaLaserOff':pmoabphcCtrlClientEdfaLaserOff,'pmoabphcCtrlclientGainCstMonitorValue':pmoabphcCtrlclientGainCstMonitorValue,'pmoabphcCtrlclientGainCstPoutValue':pmoabphcCtrlclientGainCstPoutValue,'pmoabphcCtrlclientGainSettingValue':pmoabphcCtrlclientGainSettingValue,'pmoabphcCtrlclientGainProcessing':pmoabphcCtrlclientGainProcessing,'pmoabphcCtrlClientGainProc':pmoabphcCtrlClientGainProc,'pmoabphcCtrlclientGainCstFiberAgingMarginValue':pmoabphcCtrlclientGainCstFiberAgingMarginValue,'pmoabphcCtrlclientGainCstAdddropMarginValue':pmoabphcCtrlclientGainCstAdddropMarginValue,'pmoabphcCtrlLine':pmoabphcCtrlLine,'pmoabphcCtrllineEdfaLaserOff':pmoabphcCtrllineEdfaLaserOff,'pmoabphcCtrlLineEdfaLaserOff':pmoabphcCtrlLineEdfaLaserOff,'pmoabphcCtrllineGainCstMonitorValue':pmoabphcCtrllineGainCstMonitorValue,'pmoabphcCtrllineGainCstPoutValue':pmoabphcCtrllineGainCstPoutValue,'pmoabphcCtrllineGainSettingValue':pmoabphcCtrllineGainSettingValue,'pmoabphcCtrllineGainProcessing':pmoabphcCtrllineGainProcessing,'pmoabphcCtrlLineGainProc':pmoabphcCtrlLineGainProc,'pmoabphcCtrllineGainCstFiberAgingMarginValue':pmoabphcCtrllineGainCstFiberAgingMarginValue,'pmoabphcCtrllineGainCstAdddropMarginValue':pmoabphcCtrllineGainCstAdddropMarginValue,'pmoabphcri':pmoabphcri,'pmoabphcRinvReloadInventory':pmoabphcRinvReloadInventory,'pmoabphcRinvModulePlatform':pmoabphcRinvModulePlatform,'pmoabphcRinvSwPlatform':pmoabphcRinvSwPlatform,'pmoabphcRinvSwFoa':pmoabphcRinvSwFoa,'pmoabphcRinvBoosterTable':pmoabphcRinvBoosterTable,'pmoabphcRinvBoosterEntry':pmoabphcRinvBoosterEntry,_T:pmoabphcRinvBoosterIndex,'pmoabphcRinvBooster':pmoabphcRinvBooster,'pmoabphcRinvPreAmpTable':pmoabphcRinvPreAmpTable,'pmoabphcRinvPreAmpEntry':pmoabphcRinvPreAmpEntry,_U:pmoabphcRinvPreAmpIndex,'pmoabphcRinvPreAmp':pmoabphcRinvPreAmp,'pmoabphcConfig':pmoabphcConfig,'pmoabphcCfgNoValue':pmoabphcCfgNoValue,'pmoabphctableclientStartup':pmoabphctableclientStartup,'pmoabphcCfgclientEdfaLaserCtrl':pmoabphcCfgclientEdfaLaserCtrl,'pmoabphcCfgclientEdfaLaserMode':pmoabphcCfgclientEdfaLaserMode,'pmoabphcCfgclientGainValue':pmoabphcCfgclientGainValue,'pmoabphcCfgclientTiltValue':pmoabphcCfgclientTiltValue,'pmoabphcCfgclientMsaLoss':pmoabphcCfgclientMsaLoss,'pmoabphcCfgclientOutputPowerValue':pmoabphcCfgclientOutputPowerValue,'pmoabphcCfgclientAseCompensation':pmoabphcCfgclientAseCompensation,'pmoabphcCfgLineStartUp':pmoabphcCfgLineStartUp,'pmoabphctablelineStartup':pmoabphctablelineStartup,'pmoabphcCfglineEdfaLaserCtrl':pmoabphcCfglineEdfaLaserCtrl,'pmoabphcCfglineEdfaLaserMode':pmoabphcCfglineEdfaLaserMode,'pmoabphcCfglineGainValue':pmoabphcCfglineGainValue,'pmoabphcCfglineTiltValue':pmoabphcCfglineTiltValue,'pmoabphcCfglineMsaLoss':pmoabphcCfglineMsaLoss,'pmoabphcCfglineOutputPowerValue':pmoabphcCfglineOutputPowerValue,'pmoabphcCfglineAseCompensation':pmoabphcCfglineAseCompensation,'pmoabphcCfgaprMode':pmoabphcCfgaprMode,'pmoabphcCfgLabels':pmoabphcCfgLabels,'pmoabphcCfgLabelclientTable':pmoabphcCfgLabelclientTable,'pmoabphcCfgLabelclientEntry':pmoabphcCfgLabelclientEntry,_V:pmoabphcCfgLabelclientIndex,'pmoabphcCfgLabelclientPortn':pmoabphcCfgLabelclientPortn,'pmoabphcCfgLabellineTable':pmoabphcCfgLabellineTable,'pmoabphcCfgLabellineEntry':pmoabphcCfgLabellineEntry,_W:pmoabphcCfgLabellineIndex,'pmoabphcCfgLabellinePortn':pmoabphcCfgLabellinePortn,'pmoabphcCfgWriteConfiguration':pmoabphcCfgWriteConfiguration,'pmoabphctraps':pmoabphctraps,_G:pmoabphctrapBoardNumber,'pmoabphcLineTrapNotUrgentGoesOn':pmoabphcLineTrapNotUrgentGoesOn,'pmoabphcLineTrapNotUrgentGoesOff':pmoabphcLineTrapNotUrgentGoesOff,'pmoabphcLineTrapUrgentGoesOn':pmoabphcLineTrapUrgentGoesOn,'pmoabphcLineTrapUrgentGoesOff':pmoabphcLineTrapUrgentGoesOff,'pmoabphcLineTrapCritGoesOn':pmoabphcLineTrapCritGoesOn,'pmoabphcLineTrapCritGoesOff':pmoabphcLineTrapCritGoesOff,'pmoabphcClientTrapNotUrgentGoesOn':pmoabphcClientTrapNotUrgentGoesOn,'pmoabphcClientTrapNotUrgentGoesOff':pmoabphcClientTrapNotUrgentGoesOff,'pmoabphcClientTrapUrgentGoesOn':pmoabphcClientTrapUrgentGoesOn,'pmoabphcClientTrapUrgentGoesOff':pmoabphcClientTrapUrgentGoesOff,'pmoabphcClientTrapCritGoesOn':pmoabphcClientTrapCritGoesOn,'pmoabphcClientTrapCritGoesOff':pmoabphcClientTrapCritGoesOff,'pmoabphcPowerTrapUrgentGoesOn':pmoabphcPowerTrapUrgentGoesOn,'pmoabphcPowerTrapUrgentGoesOff':pmoabphcPowerTrapUrgentGoesOff})