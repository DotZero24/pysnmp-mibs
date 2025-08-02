_W='pmoailhcCfgLabellineIndex'
_V='pmoailhcCfgLabelclientIndex'
_U='pmoailhcRinvInLine2Index'
_T='pmoailhcRinvInLine1Index'
_S='2012-09-10 00:00'
_R='pmoailhcAlmDefFuseA'
_Q='pmoailhcAlmDefFuseB'
_P='pmoailhcAlmClientHwFail'
_O='pmoailhcAlmClientFail'
_N='pmoailhcAlmClientDdmAlm'
_M='pmoailhcAlmClientDdmWarning'
_L='pmoailhcAlmLineHwFail'
_K='pmoailhcAlmLineFail'
_J='pmoailhcAlmLineDdmAlm'
_I='pmoailhcAlmLineDdmWarning'
_H='DisplayString'
_G='pmoailhctrapBoardNumber'
_F='Unsigned32'
_E='Integer32'
_D='EKINOPS-PmOailhc-MIB'
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
modulepmoailhc=ModuleIdentity((1,3,6,1,4,1,20044,55))
if mibBuilder.loadTexts:modulepmoailhc.setRevisions((_S,_S,'2013-02-08 00:00','2013-07-02 00:00','2013-09-16 00:00','2013-12-02 00:00','2014-03-26 00:00','2014-12-10 00:00','2016-05-23 00:00'))
class PmoailhcpreampMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oailhcpreampdefaultmode',0),('oailhcpreampconstantcurrentmode',1),('oailhcpreampconstantpowermode',2),('oailhcpreampconstantgainmode',3),('oailhcpreamppoutpinmode',4),('oailhcpreampmanualmode',5),('oailhcpreampfeedforwardmode',6),('oailhcpreamptransientsupmode',7)))
class PmoailhcboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oailhcboosterdefaultmode',0),('oailhcboosterconstantcurrentmode',1),('oailhcboosterconstantpowermode',2),('oailhcboosterconstantgainmode',3),('oailhcboosterpoutpinmode',4),('oailhcboostermanualmode',5),('oailhcboosterfeedforwardmode',6),('oailhcboostertransientsupmode',7)))
class PmoailhcaprMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('oailhcaproffmode',0),('oailhcaprsemiautomode',1),('oailhcaprautomode',2),('oailhcaprlossforwardingmode',3),('oailhcaprrepeatmode',4)))
class PmoailhcPreampGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oailhcpreampgainadjmanualmode',0),('oailhcpreampgainadjsemiautomode',1),('oailhcpreampgainadjautomode',2)))
class PmoailhcBoosterGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oailhcboostergainadjmanualmode',0),('oailhcboostergainadjsemiautomode',1),('oailhcboostergainadjautomode',2)))
class PmoailhcPreampCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oailhcpreampcstgainadjsemiautomode',1),('oailhcpreampcstgainadjautomode',2)))
class PmoailhcBoosterCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oailhcboostercstgainadjsemiautomode',1),('oailhcboostercstgainadjautomode',2)))
_Pmoailhcalarms_ObjectIdentity=ObjectIdentity
pmoailhcalarms=_Pmoailhcalarms_ObjectIdentity((1,3,6,1,4,1,20044,55,2))
_PmoailhcAlmOther_ObjectIdentity=ObjectIdentity
pmoailhcAlmOther=_PmoailhcAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1))
_PmoailhcAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoailhcAlmOtherNurg=_PmoailhcAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,1))
_PmoailhcAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoailhcAlmsynthAlm2=_PmoailhcAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,1,2))
_PmoailhcAlmConfTableSave_Type=EkiOnOff
_PmoailhcAlmConfTableSave_Object=MibScalar
pmoailhcAlmConfTableSave=_PmoailhcAlmConfTableSave_Object((1,3,6,1,4,1,20044,55,2,1,1,2,1),_PmoailhcAlmConfTableSave_Type())
pmoailhcAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmConfTableSave.setStatus(_A)
_PmoailhcAlmInvUpload_Type=EkiOnOff
_PmoailhcAlmInvUpload_Object=MibScalar
pmoailhcAlmInvUpload=_PmoailhcAlmInvUpload_Object((1,3,6,1,4,1,20044,55,2,1,1,2,2),_PmoailhcAlmInvUpload_Type())
pmoailhcAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmInvUpload.setStatus(_A)
_PmoailhcAlmConfTableLoad_Type=EkiOnOff
_PmoailhcAlmConfTableLoad_Object=MibScalar
pmoailhcAlmConfTableLoad=_PmoailhcAlmConfTableLoad_Object((1,3,6,1,4,1,20044,55,2,1,1,2,3),_PmoailhcAlmConfTableLoad_Type())
pmoailhcAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmConfTableLoad.setStatus(_A)
_PmoailhcAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoailhcAlmfoaWarnings=_PmoailhcAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,1,75))
_PmoailhcAlmTermpLowWarning_Type=EkiOnOff
_PmoailhcAlmTermpLowWarning_Object=MibScalar
pmoailhcAlmTermpLowWarning=_PmoailhcAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,55,2,1,1,75,7),_PmoailhcAlmTermpLowWarning_Type())
pmoailhcAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmTermpLowWarning.setStatus(_A)
_PmoailhcAlmTempHighWarning_Type=EkiOnOff
_PmoailhcAlmTempHighWarning_Object=MibScalar
pmoailhcAlmTempHighWarning=_PmoailhcAlmTempHighWarning_Object((1,3,6,1,4,1,20044,55,2,1,1,75,8),_PmoailhcAlmTempHighWarning_Type())
pmoailhcAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmTempHighWarning.setStatus(_A)
_PmoailhcAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoailhcAlmOtherUrg=_PmoailhcAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,2))
_PmoailhcAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoailhcAlmfoaAlarms=_PmoailhcAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,2,74))
_PmoailhcAlmTermpLowAlarm_Type=EkiOnOff
_PmoailhcAlmTermpLowAlarm_Object=MibScalar
pmoailhcAlmTermpLowAlarm=_PmoailhcAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,55,2,1,2,74,7),_PmoailhcAlmTermpLowAlarm_Type())
pmoailhcAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmTermpLowAlarm.setStatus(_A)
_PmoailhcAlmTempHighAlarm_Type=EkiOnOff
_PmoailhcAlmTempHighAlarm_Object=MibScalar
pmoailhcAlmTempHighAlarm=_PmoailhcAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,55,2,1,2,74,8),_PmoailhcAlmTempHighAlarm_Type())
pmoailhcAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmTempHighAlarm.setStatus(_A)
_PmoailhcAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoailhcAlmOtherCrit=_PmoailhcAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,3))
_PmoailhcAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoailhcAlmsynthAlm0=_PmoailhcAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,55,2,1,3,0))
_PmoailhcAlmMaintenanceMode_Type=EkiOnOff
_PmoailhcAlmMaintenanceMode_Object=MibScalar
pmoailhcAlmMaintenanceMode=_PmoailhcAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,55,2,1,3,0,1),_PmoailhcAlmMaintenanceMode_Type())
pmoailhcAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmMaintenanceMode.setStatus(_A)
_PmoailhcAlmAprOn_Type=EkiOnOff
_PmoailhcAlmAprOn_Object=MibScalar
pmoailhcAlmAprOn=_PmoailhcAlmAprOn_Object((1,3,6,1,4,1,20044,55,2,1,3,0,2),_PmoailhcAlmAprOn_Type())
pmoailhcAlmAprOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmAprOn.setStatus(_A)
_PmoailhcAlmModGlobFail_Type=EkiOnOff
_PmoailhcAlmModGlobFail_Object=MibScalar
pmoailhcAlmModGlobFail=_PmoailhcAlmModGlobFail_Object((1,3,6,1,4,1,20044,55,2,1,3,0,9),_PmoailhcAlmModGlobFail_Type())
pmoailhcAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmModGlobFail.setStatus(_A)
_PmoailhcAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoailhcAlmUpEdfaInitNotCompl_Object=MibScalar
pmoailhcAlmUpEdfaInitNotCompl=_PmoailhcAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,55,2,1,3,0,10),_PmoailhcAlmUpEdfaInitNotCompl_Type())
pmoailhcAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoailhcAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoailhcAlmDwEdfaInitNotCompl_Object=MibScalar
pmoailhcAlmDwEdfaInitNotCompl=_PmoailhcAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,55,2,1,3,0,11),_PmoailhcAlmDwEdfaInitNotCompl_Type())
pmoailhcAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoailhcAlmExtPump1NotLocked_Type=EkiOnOff
_PmoailhcAlmExtPump1NotLocked_Object=MibScalar
pmoailhcAlmExtPump1NotLocked=_PmoailhcAlmExtPump1NotLocked_Object((1,3,6,1,4,1,20044,55,2,1,3,0,12),_PmoailhcAlmExtPump1NotLocked_Type())
pmoailhcAlmExtPump1NotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmExtPump1NotLocked.setStatus(_A)
_PmoailhcAlmExtPump2NotLocked_Type=EkiOnOff
_PmoailhcAlmExtPump2NotLocked_Object=MibScalar
pmoailhcAlmExtPump2NotLocked=_PmoailhcAlmExtPump2NotLocked_Object((1,3,6,1,4,1,20044,55,2,1,3,0,13),_PmoailhcAlmExtPump2NotLocked_Type())
pmoailhcAlmExtPump2NotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmExtPump2NotLocked.setStatus(_A)
_PmoailhcAlmDefFuseA_Type=EkiOnOff
_PmoailhcAlmDefFuseA_Object=MibScalar
pmoailhcAlmDefFuseA=_PmoailhcAlmDefFuseA_Object((1,3,6,1,4,1,20044,55,2,1,3,0,15),_PmoailhcAlmDefFuseA_Type())
pmoailhcAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmDefFuseA.setStatus(_A)
_PmoailhcAlmDefFuseB_Type=EkiOnOff
_PmoailhcAlmDefFuseB_Object=MibScalar
pmoailhcAlmDefFuseB=_PmoailhcAlmDefFuseB_Object((1,3,6,1,4,1,20044,55,2,1,3,0,16),_PmoailhcAlmDefFuseB_Type())
pmoailhcAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmDefFuseB.setStatus(_A)
_PmoailhcAlmClient_ObjectIdentity=ObjectIdentity
pmoailhcAlmClient=_PmoailhcAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2))
_PmoailhcAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoailhcAlmClientNurg=_PmoailhcAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,1))
_PmoailhcAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoailhcAlmclientEdfaWarnings=_PmoailhcAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,1,33))
_PmoailhcAlmClientGainLowWarning_Type=EkiOnOff
_PmoailhcAlmClientGainLowWarning_Object=MibScalar
pmoailhcAlmClientGainLowWarning=_PmoailhcAlmClientGainLowWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,1),_PmoailhcAlmClientGainLowWarning_Type())
pmoailhcAlmClientGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientGainLowWarning.setStatus(_A)
_PmoailhcAlmClientGainHighWarning_Type=EkiOnOff
_PmoailhcAlmClientGainHighWarning_Object=MibScalar
pmoailhcAlmClientGainHighWarning=_PmoailhcAlmClientGainHighWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,2),_PmoailhcAlmClientGainHighWarning_Type())
pmoailhcAlmClientGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientGainHighWarning.setStatus(_A)
_PmoailhcAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoailhcAlmClientInputPwrLowWarning_Object=MibScalar
pmoailhcAlmClientInputPwrLowWarning=_PmoailhcAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,3),_PmoailhcAlmClientInputPwrLowWarning_Type())
pmoailhcAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientInputPwrLowWarning.setStatus(_A)
_PmoailhcAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoailhcAlmClientInputPwrHighWarning_Object=MibScalar
pmoailhcAlmClientInputPwrHighWarning=_PmoailhcAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,4),_PmoailhcAlmClientInputPwrHighWarning_Type())
pmoailhcAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientInputPwrHighWarning.setStatus(_A)
_PmoailhcAlmClientOutputPwrLowWarning_Type=EkiOnOff
_PmoailhcAlmClientOutputPwrLowWarning_Object=MibScalar
pmoailhcAlmClientOutputPwrLowWarning=_PmoailhcAlmClientOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,5),_PmoailhcAlmClientOutputPwrLowWarning_Type())
pmoailhcAlmClientOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientOutputPwrLowWarning.setStatus(_A)
_PmoailhcAlmClientOutputPwrHighWarning_Type=EkiOnOff
_PmoailhcAlmClientOutputPwrHighWarning_Object=MibScalar
pmoailhcAlmClientOutputPwrHighWarning=_PmoailhcAlmClientOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,6),_PmoailhcAlmClientOutputPwrHighWarning_Type())
pmoailhcAlmClientOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientOutputPwrHighWarning.setStatus(_A)
_PmoailhcAlmClientBiasLowWarning_Type=EkiOnOff
_PmoailhcAlmClientBiasLowWarning_Object=MibScalar
pmoailhcAlmClientBiasLowWarning=_PmoailhcAlmClientBiasLowWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,7),_PmoailhcAlmClientBiasLowWarning_Type())
pmoailhcAlmClientBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientBiasLowWarning.setStatus(_A)
_PmoailhcAlmClientBiasHighWarning_Type=EkiOnOff
_PmoailhcAlmClientBiasHighWarning_Object=MibScalar
pmoailhcAlmClientBiasHighWarning=_PmoailhcAlmClientBiasHighWarning_Object((1,3,6,1,4,1,20044,55,2,2,1,33,8),_PmoailhcAlmClientBiasHighWarning_Type())
pmoailhcAlmClientBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientBiasHighWarning.setStatus(_A)
_PmoailhcAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoailhcAlmClientUrg=_PmoailhcAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,2))
_PmoailhcAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoailhcAlmclientEdfaAlarms1=_PmoailhcAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,2,32))
_PmoailhcAlmClientGainLowAlarm_Type=EkiOnOff
_PmoailhcAlmClientGainLowAlarm_Object=MibScalar
pmoailhcAlmClientGainLowAlarm=_PmoailhcAlmClientGainLowAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,1),_PmoailhcAlmClientGainLowAlarm_Type())
pmoailhcAlmClientGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientGainLowAlarm.setStatus(_A)
_PmoailhcAlmClientGainHighAlarm_Type=EkiOnOff
_PmoailhcAlmClientGainHighAlarm_Object=MibScalar
pmoailhcAlmClientGainHighAlarm=_PmoailhcAlmClientGainHighAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,2),_PmoailhcAlmClientGainHighAlarm_Type())
pmoailhcAlmClientGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientGainHighAlarm.setStatus(_A)
_PmoailhcAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoailhcAlmClientInputPwrLowAlarm_Object=MibScalar
pmoailhcAlmClientInputPwrLowAlarm=_PmoailhcAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,3),_PmoailhcAlmClientInputPwrLowAlarm_Type())
pmoailhcAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoailhcAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoailhcAlmClientInputPwrHighAlarm_Object=MibScalar
pmoailhcAlmClientInputPwrHighAlarm=_PmoailhcAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,4),_PmoailhcAlmClientInputPwrHighAlarm_Type())
pmoailhcAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoailhcAlmClientOutputPwrLowAlarm_Type=EkiOnOff
_PmoailhcAlmClientOutputPwrLowAlarm_Object=MibScalar
pmoailhcAlmClientOutputPwrLowAlarm=_PmoailhcAlmClientOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,5),_PmoailhcAlmClientOutputPwrLowAlarm_Type())
pmoailhcAlmClientOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientOutputPwrLowAlarm.setStatus(_A)
_PmoailhcAlmClientOutputPwrHighAlarm_Type=EkiOnOff
_PmoailhcAlmClientOutputPwrHighAlarm_Object=MibScalar
pmoailhcAlmClientOutputPwrHighAlarm=_PmoailhcAlmClientOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,6),_PmoailhcAlmClientOutputPwrHighAlarm_Type())
pmoailhcAlmClientOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientOutputPwrHighAlarm.setStatus(_A)
_PmoailhcAlmClientBiasLowAlarm_Type=EkiOnOff
_PmoailhcAlmClientBiasLowAlarm_Object=MibScalar
pmoailhcAlmClientBiasLowAlarm=_PmoailhcAlmClientBiasLowAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,7),_PmoailhcAlmClientBiasLowAlarm_Type())
pmoailhcAlmClientBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientBiasLowAlarm.setStatus(_A)
_PmoailhcAlmClientBiasHighAlarm_Type=EkiOnOff
_PmoailhcAlmClientBiasHighAlarm_Object=MibScalar
pmoailhcAlmClientBiasHighAlarm=_PmoailhcAlmClientBiasHighAlarm_Object((1,3,6,1,4,1,20044,55,2,2,2,32,8),_PmoailhcAlmClientBiasHighAlarm_Type())
pmoailhcAlmClientBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientBiasHighAlarm.setStatus(_A)
_PmoailhcAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoailhcAlmClientCrit=_PmoailhcAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,3))
_PmoailhcAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoailhcAlmsynthAlm8=_PmoailhcAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,3,8))
_PmoailhcAlmClientHwFail_Type=EkiOnOff
_PmoailhcAlmClientHwFail_Object=MibScalar
pmoailhcAlmClientHwFail=_PmoailhcAlmClientHwFail_Object((1,3,6,1,4,1,20044,55,2,2,3,8,4),_PmoailhcAlmClientHwFail_Type())
pmoailhcAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientHwFail.setStatus(_A)
_PmoailhcAlmClientTxOff_Type=EkiOnOff
_PmoailhcAlmClientTxOff_Object=MibScalar
pmoailhcAlmClientTxOff=_PmoailhcAlmClientTxOff_Object((1,3,6,1,4,1,20044,55,2,2,3,8,5),_PmoailhcAlmClientTxOff_Type())
pmoailhcAlmClientTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientTxOff.setStatus(_A)
_PmoailhcAlmClientDdmWarning_Type=EkiOnOff
_PmoailhcAlmClientDdmWarning_Object=MibScalar
pmoailhcAlmClientDdmWarning=_PmoailhcAlmClientDdmWarning_Object((1,3,6,1,4,1,20044,55,2,2,3,8,9),_PmoailhcAlmClientDdmWarning_Type())
pmoailhcAlmClientDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientDdmWarning.setStatus(_A)
_PmoailhcAlmClientDdmAlm_Type=EkiOnOff
_PmoailhcAlmClientDdmAlm_Object=MibScalar
pmoailhcAlmClientDdmAlm=_PmoailhcAlmClientDdmAlm_Object((1,3,6,1,4,1,20044,55,2,2,3,8,10),_PmoailhcAlmClientDdmAlm_Type())
pmoailhcAlmClientDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientDdmAlm.setStatus(_A)
_PmoailhcAlmClientFail_Type=EkiOnOff
_PmoailhcAlmClientFail_Object=MibScalar
pmoailhcAlmClientFail=_PmoailhcAlmClientFail_Object((1,3,6,1,4,1,20044,55,2,2,3,8,12),_PmoailhcAlmClientFail_Type())
pmoailhcAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientFail.setStatus(_A)
_PmoailhcAlmClientExtPumpFail_Type=EkiOnOff
_PmoailhcAlmClientExtPumpFail_Object=MibScalar
pmoailhcAlmClientExtPumpFail=_PmoailhcAlmClientExtPumpFail_Object((1,3,6,1,4,1,20044,55,2,2,3,8,13),_PmoailhcAlmClientExtPumpFail_Type())
pmoailhcAlmClientExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientExtPumpFail.setStatus(_A)
_PmoailhcAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoailhcAlmclientEdfaAlarms2=_PmoailhcAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,55,2,2,3,35))
_PmoailhcAlmClientEdfaNr_Type=EkiOnOff
_PmoailhcAlmClientEdfaNr_Object=MibScalar
pmoailhcAlmClientEdfaNr=_PmoailhcAlmClientEdfaNr_Object((1,3,6,1,4,1,20044,55,2,2,3,35,1),_PmoailhcAlmClientEdfaNr_Type())
pmoailhcAlmClientEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientEdfaNr.setStatus(_A)
_PmoailhcAlmClientEdfaTecFail_Type=EkiOnOff
_PmoailhcAlmClientEdfaTecFail_Object=MibScalar
pmoailhcAlmClientEdfaTecFail=_PmoailhcAlmClientEdfaTecFail_Object((1,3,6,1,4,1,20044,55,2,2,3,35,2),_PmoailhcAlmClientEdfaTecFail_Type())
pmoailhcAlmClientEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientEdfaTecFail.setStatus(_A)
_PmoailhcAlmClientEdfaLaserFail_Type=EkiOnOff
_PmoailhcAlmClientEdfaLaserFail_Object=MibScalar
pmoailhcAlmClientEdfaLaserFail=_PmoailhcAlmClientEdfaLaserFail_Object((1,3,6,1,4,1,20044,55,2,2,3,35,3),_PmoailhcAlmClientEdfaLaserFail_Type())
pmoailhcAlmClientEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientEdfaLaserFail.setStatus(_A)
_PmoailhcAlmClientEdfaLos_Type=EkiOnOff
_PmoailhcAlmClientEdfaLos_Object=MibScalar
pmoailhcAlmClientEdfaLos=_PmoailhcAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,55,2,2,3,35,4),_PmoailhcAlmClientEdfaLos_Type())
pmoailhcAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientEdfaLos.setStatus(_A)
_PmoailhcAlmClientExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoailhcAlmClientExtPumpEdfaLowCurrent_Object=MibScalar
pmoailhcAlmClientExtPumpEdfaLowCurrent=_PmoailhcAlmClientExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,55,2,2,3,35,5),_PmoailhcAlmClientExtPumpEdfaLowCurrent_Type())
pmoailhcAlmClientExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmClientExtPumpEdfaLowCurrent.setStatus(_A)
_PmoailhcAlmLine_ObjectIdentity=ObjectIdentity
pmoailhcAlmLine=_PmoailhcAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3))
_PmoailhcAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoailhcAlmLineNurg=_PmoailhcAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,1))
_PmoailhcAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoailhcAlmlineEdfaWarnings=_PmoailhcAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,1,41))
_PmoailhcAlmLineGainLowWarning_Type=EkiOnOff
_PmoailhcAlmLineGainLowWarning_Object=MibScalar
pmoailhcAlmLineGainLowWarning=_PmoailhcAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,1),_PmoailhcAlmLineGainLowWarning_Type())
pmoailhcAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineGainLowWarning.setStatus(_A)
_PmoailhcAlmLineGainHighWarning_Type=EkiOnOff
_PmoailhcAlmLineGainHighWarning_Object=MibScalar
pmoailhcAlmLineGainHighWarning=_PmoailhcAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,2),_PmoailhcAlmLineGainHighWarning_Type())
pmoailhcAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineGainHighWarning.setStatus(_A)
_PmoailhcAlmLineInputPwrLowWarning_Type=EkiOnOff
_PmoailhcAlmLineInputPwrLowWarning_Object=MibScalar
pmoailhcAlmLineInputPwrLowWarning=_PmoailhcAlmLineInputPwrLowWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,3),_PmoailhcAlmLineInputPwrLowWarning_Type())
pmoailhcAlmLineInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineInputPwrLowWarning.setStatus(_A)
_PmoailhcAlmLineInputPwrHighWarning_Type=EkiOnOff
_PmoailhcAlmLineInputPwrHighWarning_Object=MibScalar
pmoailhcAlmLineInputPwrHighWarning=_PmoailhcAlmLineInputPwrHighWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,4),_PmoailhcAlmLineInputPwrHighWarning_Type())
pmoailhcAlmLineInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineInputPwrHighWarning.setStatus(_A)
_PmoailhcAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoailhcAlmLineOutputPwrLowWarning_Object=MibScalar
pmoailhcAlmLineOutputPwrLowWarning=_PmoailhcAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,5),_PmoailhcAlmLineOutputPwrLowWarning_Type())
pmoailhcAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoailhcAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoailhcAlmLineOutputPwrHighWarning_Object=MibScalar
pmoailhcAlmLineOutputPwrHighWarning=_PmoailhcAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,6),_PmoailhcAlmLineOutputPwrHighWarning_Type())
pmoailhcAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoailhcAlmLineBiasLowWarning_Type=EkiOnOff
_PmoailhcAlmLineBiasLowWarning_Object=MibScalar
pmoailhcAlmLineBiasLowWarning=_PmoailhcAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,7),_PmoailhcAlmLineBiasLowWarning_Type())
pmoailhcAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineBiasLowWarning.setStatus(_A)
_PmoailhcAlmLineBiasHighWarning_Type=EkiOnOff
_PmoailhcAlmLineBiasHighWarning_Object=MibScalar
pmoailhcAlmLineBiasHighWarning=_PmoailhcAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,55,2,3,1,41,8),_PmoailhcAlmLineBiasHighWarning_Type())
pmoailhcAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineBiasHighWarning.setStatus(_A)
_PmoailhcAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoailhcAlmLineUrg=_PmoailhcAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,2))
_PmoailhcAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoailhcAlmlineEdfaAlarms1=_PmoailhcAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,2,40))
_PmoailhcAlmLineGainLowAlarm_Type=EkiOnOff
_PmoailhcAlmLineGainLowAlarm_Object=MibScalar
pmoailhcAlmLineGainLowAlarm=_PmoailhcAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,1),_PmoailhcAlmLineGainLowAlarm_Type())
pmoailhcAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineGainLowAlarm.setStatus(_A)
_PmoailhcAlmLineGainHighAlarm_Type=EkiOnOff
_PmoailhcAlmLineGainHighAlarm_Object=MibScalar
pmoailhcAlmLineGainHighAlarm=_PmoailhcAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,2),_PmoailhcAlmLineGainHighAlarm_Type())
pmoailhcAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineGainHighAlarm.setStatus(_A)
_PmoailhcAlmLineInputPwrLowAlarm_Type=EkiOnOff
_PmoailhcAlmLineInputPwrLowAlarm_Object=MibScalar
pmoailhcAlmLineInputPwrLowAlarm=_PmoailhcAlmLineInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,3),_PmoailhcAlmLineInputPwrLowAlarm_Type())
pmoailhcAlmLineInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineInputPwrLowAlarm.setStatus(_A)
_PmoailhcAlmLineInputPwrHighAlarm_Type=EkiOnOff
_PmoailhcAlmLineInputPwrHighAlarm_Object=MibScalar
pmoailhcAlmLineInputPwrHighAlarm=_PmoailhcAlmLineInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,4),_PmoailhcAlmLineInputPwrHighAlarm_Type())
pmoailhcAlmLineInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineInputPwrHighAlarm.setStatus(_A)
_PmoailhcAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoailhcAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoailhcAlmLineOutputPwrLowAlarm=_PmoailhcAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,5),_PmoailhcAlmLineOutputPwrLowAlarm_Type())
pmoailhcAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoailhcAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoailhcAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoailhcAlmLineOutputPwrHighAlarm=_PmoailhcAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,6),_PmoailhcAlmLineOutputPwrHighAlarm_Type())
pmoailhcAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoailhcAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoailhcAlmLineBiasLowAlarm_Object=MibScalar
pmoailhcAlmLineBiasLowAlarm=_PmoailhcAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,7),_PmoailhcAlmLineBiasLowAlarm_Type())
pmoailhcAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineBiasLowAlarm.setStatus(_A)
_PmoailhcAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoailhcAlmLineBiasHighAlarm_Object=MibScalar
pmoailhcAlmLineBiasHighAlarm=_PmoailhcAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,55,2,3,2,40,8),_PmoailhcAlmLineBiasHighAlarm_Type())
pmoailhcAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineBiasHighAlarm.setStatus(_A)
_PmoailhcAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoailhcAlmLineCrit=_PmoailhcAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,3))
_PmoailhcAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoailhcAlmsynthAlm7=_PmoailhcAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,3,7))
_PmoailhcAlmLineHwFail_Type=EkiOnOff
_PmoailhcAlmLineHwFail_Object=MibScalar
pmoailhcAlmLineHwFail=_PmoailhcAlmLineHwFail_Object((1,3,6,1,4,1,20044,55,2,3,3,7,4),_PmoailhcAlmLineHwFail_Type())
pmoailhcAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineHwFail.setStatus(_A)
_PmoailhcAlmLineTxOff_Type=EkiOnOff
_PmoailhcAlmLineTxOff_Object=MibScalar
pmoailhcAlmLineTxOff=_PmoailhcAlmLineTxOff_Object((1,3,6,1,4,1,20044,55,2,3,3,7,5),_PmoailhcAlmLineTxOff_Type())
pmoailhcAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineTxOff.setStatus(_A)
_PmoailhcAlmLineDdmWarning_Type=EkiOnOff
_PmoailhcAlmLineDdmWarning_Object=MibScalar
pmoailhcAlmLineDdmWarning=_PmoailhcAlmLineDdmWarning_Object((1,3,6,1,4,1,20044,55,2,3,3,7,9),_PmoailhcAlmLineDdmWarning_Type())
pmoailhcAlmLineDdmWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineDdmWarning.setStatus(_A)
_PmoailhcAlmLineDdmAlm_Type=EkiOnOff
_PmoailhcAlmLineDdmAlm_Object=MibScalar
pmoailhcAlmLineDdmAlm=_PmoailhcAlmLineDdmAlm_Object((1,3,6,1,4,1,20044,55,2,3,3,7,10),_PmoailhcAlmLineDdmAlm_Type())
pmoailhcAlmLineDdmAlm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineDdmAlm.setStatus(_A)
_PmoailhcAlmLineFail_Type=EkiOnOff
_PmoailhcAlmLineFail_Object=MibScalar
pmoailhcAlmLineFail=_PmoailhcAlmLineFail_Object((1,3,6,1,4,1,20044,55,2,3,3,7,12),_PmoailhcAlmLineFail_Type())
pmoailhcAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineFail.setStatus(_A)
_PmoailhcAlmLineExtPumpFail_Type=EkiOnOff
_PmoailhcAlmLineExtPumpFail_Object=MibScalar
pmoailhcAlmLineExtPumpFail=_PmoailhcAlmLineExtPumpFail_Object((1,3,6,1,4,1,20044,55,2,3,3,7,13),_PmoailhcAlmLineExtPumpFail_Type())
pmoailhcAlmLineExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineExtPumpFail.setStatus(_A)
_PmoailhcAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoailhcAlmlineEdfaAlarms2=_PmoailhcAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,55,2,3,3,43))
_PmoailhcAlmLineEdfaNr_Type=EkiOnOff
_PmoailhcAlmLineEdfaNr_Object=MibScalar
pmoailhcAlmLineEdfaNr=_PmoailhcAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,55,2,3,3,43,1),_PmoailhcAlmLineEdfaNr_Type())
pmoailhcAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineEdfaNr.setStatus(_A)
_PmoailhcAlmLineEdfaTecFail_Type=EkiOnOff
_PmoailhcAlmLineEdfaTecFail_Object=MibScalar
pmoailhcAlmLineEdfaTecFail=_PmoailhcAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,55,2,3,3,43,2),_PmoailhcAlmLineEdfaTecFail_Type())
pmoailhcAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineEdfaTecFail.setStatus(_A)
_PmoailhcAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoailhcAlmLineEdfaLaserFail_Object=MibScalar
pmoailhcAlmLineEdfaLaserFail=_PmoailhcAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,55,2,3,3,43,3),_PmoailhcAlmLineEdfaLaserFail_Type())
pmoailhcAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineEdfaLaserFail.setStatus(_A)
_PmoailhcAlmLineEdfaLos_Type=EkiOnOff
_PmoailhcAlmLineEdfaLos_Object=MibScalar
pmoailhcAlmLineEdfaLos=_PmoailhcAlmLineEdfaLos_Object((1,3,6,1,4,1,20044,55,2,3,3,43,4),_PmoailhcAlmLineEdfaLos_Type())
pmoailhcAlmLineEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineEdfaLos.setStatus(_A)
_PmoailhcAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoailhcAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoailhcAlmLineExtPumpEdfaLowCurrent=_PmoailhcAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,55,2,3,3,43,5),_PmoailhcAlmLineExtPumpEdfaLowCurrent_Type())
pmoailhcAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_Pmoailhcmeasures_ObjectIdentity=ObjectIdentity
pmoailhcmeasures=_Pmoailhcmeasures_ObjectIdentity((1,3,6,1,4,1,20044,55,3))
_PmoailhcMesrOther_ObjectIdentity=ObjectIdentity
pmoailhcMesrOther=_PmoailhcMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,55,3,1))
class _PmoailhcMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrtempMeas_Type.__name__=_E
_PmoailhcMesrtempMeas_Object=MibScalar
pmoailhcMesrtempMeas=_PmoailhcMesrtempMeas_Object((1,3,6,1,4,1,20044,55,3,1,72),_PmoailhcMesrtempMeas_Type())
pmoailhcMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrtempMeas.setStatus(_A)
_PmoailhcMesrClient_ObjectIdentity=ObjectIdentity
pmoailhcMesrClient=_PmoailhcMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,55,3,2))
class _PmoailhcMesrclientEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrclientEdfaBiasMeas_Type.__name__=_E
_PmoailhcMesrclientEdfaBiasMeas_Object=MibScalar
pmoailhcMesrclientEdfaBiasMeas=_PmoailhcMesrclientEdfaBiasMeas_Object((1,3,6,1,4,1,20044,55,3,2,32),_PmoailhcMesrclientEdfaBiasMeas_Type())
pmoailhcMesrclientEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrclientEdfaBiasMeas.setStatus(_A)
class _PmoailhcMesrclientEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrclientEdfaTxpwrMeas_Type.__name__=_E
_PmoailhcMesrclientEdfaTxpwrMeas_Object=MibScalar
pmoailhcMesrclientEdfaTxpwrMeas=_PmoailhcMesrclientEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,55,3,2,33),_PmoailhcMesrclientEdfaTxpwrMeas_Type())
pmoailhcMesrclientEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrclientEdfaTxpwrMeas.setStatus(_A)
class _PmoailhcMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrclientEdfaRxpwrMeas_Type.__name__=_E
_PmoailhcMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoailhcMesrclientEdfaRxpwrMeas=_PmoailhcMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,55,3,2,34),_PmoailhcMesrclientEdfaRxpwrMeas_Type())
pmoailhcMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrclientEdfaRxpwrMeas.setStatus(_A)
class _PmoailhcMesrclientEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrclientEdfaGainMeas_Type.__name__=_E
_PmoailhcMesrclientEdfaGainMeas_Object=MibScalar
pmoailhcMesrclientEdfaGainMeas=_PmoailhcMesrclientEdfaGainMeas_Object((1,3,6,1,4,1,20044,55,3,2,35),_PmoailhcMesrclientEdfaGainMeas_Type())
pmoailhcMesrclientEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrclientEdfaGainMeas.setStatus(_A)
class _PmoailhcMesrclientCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrclientCorrectedGain_Type.__name__=_E
_PmoailhcMesrclientCorrectedGain_Object=MibScalar
pmoailhcMesrclientCorrectedGain=_PmoailhcMesrclientCorrectedGain_Object((1,3,6,1,4,1,20044,55,3,2,38),_PmoailhcMesrclientCorrectedGain_Type())
pmoailhcMesrclientCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrclientCorrectedGain.setStatus(_A)
_PmoailhcMesrLine_ObjectIdentity=ObjectIdentity
pmoailhcMesrLine=_PmoailhcMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,55,3,3))
class _PmoailhcMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrlineEdfaBiasMeas_Type.__name__=_E
_PmoailhcMesrlineEdfaBiasMeas_Object=MibScalar
pmoailhcMesrlineEdfaBiasMeas=_PmoailhcMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,55,3,3,40),_PmoailhcMesrlineEdfaBiasMeas_Type())
pmoailhcMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoailhcMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrlineEdfaTxpwrMeas_Type.__name__=_E
_PmoailhcMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoailhcMesrlineEdfaTxpwrMeas=_PmoailhcMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,55,3,3,41),_PmoailhcMesrlineEdfaTxpwrMeas_Type())
pmoailhcMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoailhcMesrlineEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrlineEdfaRxpwrMeas_Type.__name__=_E
_PmoailhcMesrlineEdfaRxpwrMeas_Object=MibScalar
pmoailhcMesrlineEdfaRxpwrMeas=_PmoailhcMesrlineEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,55,3,3,42),_PmoailhcMesrlineEdfaRxpwrMeas_Type())
pmoailhcMesrlineEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrlineEdfaRxpwrMeas.setStatus(_A)
class _PmoailhcMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrlineEdfaGainMeas_Type.__name__=_E
_PmoailhcMesrlineEdfaGainMeas_Object=MibScalar
pmoailhcMesrlineEdfaGainMeas=_PmoailhcMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,55,3,3,43),_PmoailhcMesrlineEdfaGainMeas_Type())
pmoailhcMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrlineEdfaGainMeas.setStatus(_A)
class _PmoailhcMesrlineCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcMesrlineCorrectedGain_Type.__name__=_E
_PmoailhcMesrlineCorrectedGain_Object=MibScalar
pmoailhcMesrlineCorrectedGain=_PmoailhcMesrlineCorrectedGain_Object((1,3,6,1,4,1,20044,55,3,3,46),_PmoailhcMesrlineCorrectedGain_Type())
pmoailhcMesrlineCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcMesrlineCorrectedGain.setStatus(_A)
_PmoailhccontrolsWrite_ObjectIdentity=ObjectIdentity
pmoailhccontrolsWrite=_PmoailhccontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,55,6))
_PmoailhcCtrlOther_ObjectIdentity=ObjectIdentity
pmoailhcCtrlOther=_PmoailhcCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,55,6,1))
_PmoailhcCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoailhcCtrlsynth0=_PmoailhcCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,55,6,1,0))
_PmoailhcCtrlConfLoad_Type=EkiOnOff
_PmoailhcCtrlConfLoad_Object=MibScalar
pmoailhcCtrlConfLoad=_PmoailhcCtrlConfLoad_Object((1,3,6,1,4,1,20044,55,6,1,0,1),_PmoailhcCtrlConfLoad_Type())
pmoailhcCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlConfLoad.setStatus(_A)
_PmoailhcCtrlConfFlash_Type=EkiOnOff
_PmoailhcCtrlConfFlash_Object=MibScalar
pmoailhcCtrlConfFlash=_PmoailhcCtrlConfFlash_Object((1,3,6,1,4,1,20044,55,6,1,0,9),_PmoailhcCtrlConfFlash_Type())
pmoailhcCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlConfFlash.setStatus(_A)
_PmoailhcCtrlConfClear_Type=EkiOnOff
_PmoailhcCtrlConfClear_Object=MibScalar
pmoailhcCtrlConfClear=_PmoailhcCtrlConfClear_Object((1,3,6,1,4,1,20044,55,6,1,0,13),_PmoailhcCtrlConfClear_Type())
pmoailhcCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlConfClear.setStatus(_A)
_PmoailhcCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoailhcCtrlswMgnt=_PmoailhcCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,55,6,1,5))
_PmoailhcCtrlColdReset_Type=EkiOnOff
_PmoailhcCtrlColdReset_Object=MibScalar
pmoailhcCtrlColdReset=_PmoailhcCtrlColdReset_Object((1,3,6,1,4,1,20044,55,6,1,5,2),_PmoailhcCtrlColdReset_Type())
pmoailhcCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlColdReset.setStatus(_A)
_PmoailhcCtrlWarmReset_Type=EkiOnOff
_PmoailhcCtrlWarmReset_Object=MibScalar
pmoailhcCtrlWarmReset=_PmoailhcCtrlWarmReset_Object((1,3,6,1,4,1,20044,55,6,1,5,3),_PmoailhcCtrlWarmReset_Type())
pmoailhcCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlWarmReset.setStatus(_A)
_PmoailhcCtrlledTest_ObjectIdentity=ObjectIdentity
pmoailhcCtrlledTest=_PmoailhcCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,55,6,1,73))
_PmoailhcCtrlGreenLed_Type=EkiOnOff
_PmoailhcCtrlGreenLed_Object=MibScalar
pmoailhcCtrlGreenLed=_PmoailhcCtrlGreenLed_Object((1,3,6,1,4,1,20044,55,6,1,73,1),_PmoailhcCtrlGreenLed_Type())
pmoailhcCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlGreenLed.setStatus(_A)
_PmoailhcCtrlRedLed_Type=EkiOnOff
_PmoailhcCtrlRedLed_Object=MibScalar
pmoailhcCtrlRedLed=_PmoailhcCtrlRedLed_Object((1,3,6,1,4,1,20044,55,6,1,73,2),_PmoailhcCtrlRedLed_Type())
pmoailhcCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlRedLed.setStatus(_A)
_PmoailhcCtrlLedOff_Type=EkiOnOff
_PmoailhcCtrlLedOff_Object=MibScalar
pmoailhcCtrlLedOff=_PmoailhcCtrlLedOff_Object((1,3,6,1,4,1,20044,55,6,1,73,3),_PmoailhcCtrlLedOff_Type())
pmoailhcCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlLedOff.setStatus(_A)
_PmoailhcCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoailhcCtrlmaintMode=_PmoailhcCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,55,6,1,75))
_PmoailhcCtrlMaintenance_Type=EkiOnOff
_PmoailhcCtrlMaintenance_Object=MibScalar
pmoailhcCtrlMaintenance=_PmoailhcCtrlMaintenance_Object((1,3,6,1,4,1,20044,55,6,1,75,1),_PmoailhcCtrlMaintenance_Type())
pmoailhcCtrlMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlMaintenance.setStatus(_A)
_PmoailhcCtrlaprRestart_ObjectIdentity=ObjectIdentity
pmoailhcCtrlaprRestart=_PmoailhcCtrlaprRestart_ObjectIdentity((1,3,6,1,4,1,20044,55,6,1,76))
_PmoailhcCtrlAprManualRestart_Type=EkiOnOff
_PmoailhcCtrlAprManualRestart_Object=MibScalar
pmoailhcCtrlAprManualRestart=_PmoailhcCtrlAprManualRestart_Object((1,3,6,1,4,1,20044,55,6,1,76,1),_PmoailhcCtrlAprManualRestart_Type())
pmoailhcCtrlAprManualRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlAprManualRestart.setStatus(_A)
_PmoailhcCtrlClient_ObjectIdentity=ObjectIdentity
pmoailhcCtrlClient=_PmoailhcCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,55,6,2))
_PmoailhcCtrlclientEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoailhcCtrlclientEdfaLaserOff=_PmoailhcCtrlclientEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,55,6,2,32))
_PmoailhcCtrlClientEdfaLaserOff_Type=EkiOnOff
_PmoailhcCtrlClientEdfaLaserOff_Object=MibScalar
pmoailhcCtrlClientEdfaLaserOff=_PmoailhcCtrlClientEdfaLaserOff_Object((1,3,6,1,4,1,20044,55,6,2,32,1),_PmoailhcCtrlClientEdfaLaserOff_Type())
pmoailhcCtrlClientEdfaLaserOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlClientEdfaLaserOff.setStatus(_A)
class _PmoailhcCtrlclientGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrlclientGainCstMonitorValue_Type.__name__=_E
_PmoailhcCtrlclientGainCstMonitorValue_Object=MibScalar
pmoailhcCtrlclientGainCstMonitorValue=_PmoailhcCtrlclientGainCstMonitorValue_Object((1,3,6,1,4,1,20044,55,6,2,34),_PmoailhcCtrlclientGainCstMonitorValue_Type())
pmoailhcCtrlclientGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlclientGainCstMonitorValue.setStatus(_A)
class _PmoailhcCtrlclientGainCstPoutValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrlclientGainCstPoutValue_Type.__name__=_E
_PmoailhcCtrlclientGainCstPoutValue_Object=MibScalar
pmoailhcCtrlclientGainCstPoutValue=_PmoailhcCtrlclientGainCstPoutValue_Object((1,3,6,1,4,1,20044,55,6,2,35),_PmoailhcCtrlclientGainCstPoutValue_Type())
pmoailhcCtrlclientGainCstPoutValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlclientGainCstPoutValue.setStatus(_A)
class _PmoailhcCtrlclientGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrlclientGainSettingValue_Type.__name__=_E
_PmoailhcCtrlclientGainSettingValue_Object=MibScalar
pmoailhcCtrlclientGainSettingValue=_PmoailhcCtrlclientGainSettingValue_Object((1,3,6,1,4,1,20044,55,6,2,36),_PmoailhcCtrlclientGainSettingValue_Type())
pmoailhcCtrlclientGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlclientGainSettingValue.setStatus(_A)
_PmoailhcCtrlclientGainProcessing_ObjectIdentity=ObjectIdentity
pmoailhcCtrlclientGainProcessing=_PmoailhcCtrlclientGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,55,6,2,37))
_PmoailhcCtrlClientGainProc_Type=EkiOnOff
_PmoailhcCtrlClientGainProc_Object=MibScalar
pmoailhcCtrlClientGainProc=_PmoailhcCtrlClientGainProc_Object((1,3,6,1,4,1,20044,55,6,2,37,1),_PmoailhcCtrlClientGainProc_Type())
pmoailhcCtrlClientGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlClientGainProc.setStatus(_A)
class _PmoailhcCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrlclientGainCstFiberAgingMarginValue_Type.__name__=_E
_PmoailhcCtrlclientGainCstFiberAgingMarginValue_Object=MibScalar
pmoailhcCtrlclientGainCstFiberAgingMarginValue=_PmoailhcCtrlclientGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,55,6,2,38),_PmoailhcCtrlclientGainCstFiberAgingMarginValue_Type())
pmoailhcCtrlclientGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlclientGainCstFiberAgingMarginValue.setStatus(_A)
class _PmoailhcCtrlclientGainCstAdddropMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrlclientGainCstAdddropMarginValue_Type.__name__=_E
_PmoailhcCtrlclientGainCstAdddropMarginValue_Object=MibScalar
pmoailhcCtrlclientGainCstAdddropMarginValue=_PmoailhcCtrlclientGainCstAdddropMarginValue_Object((1,3,6,1,4,1,20044,55,6,2,39),_PmoailhcCtrlclientGainCstAdddropMarginValue_Type())
pmoailhcCtrlclientGainCstAdddropMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlclientGainCstAdddropMarginValue.setStatus(_A)
_PmoailhcCtrlLine_ObjectIdentity=ObjectIdentity
pmoailhcCtrlLine=_PmoailhcCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,55,6,3))
_PmoailhcCtrllineEdfaLaserOff_ObjectIdentity=ObjectIdentity
pmoailhcCtrllineEdfaLaserOff=_PmoailhcCtrllineEdfaLaserOff_ObjectIdentity((1,3,6,1,4,1,20044,55,6,3,40))
_PmoailhcCtrlLineEdfaLaserOff_Type=EkiOnOff
_PmoailhcCtrlLineEdfaLaserOff_Object=MibScalar
pmoailhcCtrlLineEdfaLaserOff=_PmoailhcCtrlLineEdfaLaserOff_Object((1,3,6,1,4,1,20044,55,6,3,40,1),_PmoailhcCtrlLineEdfaLaserOff_Type())
pmoailhcCtrlLineEdfaLaserOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlLineEdfaLaserOff.setStatus(_A)
class _PmoailhcCtrllineGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrllineGainCstMonitorValue_Type.__name__=_E
_PmoailhcCtrllineGainCstMonitorValue_Object=MibScalar
pmoailhcCtrllineGainCstMonitorValue=_PmoailhcCtrllineGainCstMonitorValue_Object((1,3,6,1,4,1,20044,55,6,3,42),_PmoailhcCtrllineGainCstMonitorValue_Type())
pmoailhcCtrllineGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrllineGainCstMonitorValue.setStatus(_A)
class _PmoailhcCtrllineGainCstPoutValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrllineGainCstPoutValue_Type.__name__=_E
_PmoailhcCtrllineGainCstPoutValue_Object=MibScalar
pmoailhcCtrllineGainCstPoutValue=_PmoailhcCtrllineGainCstPoutValue_Object((1,3,6,1,4,1,20044,55,6,3,43),_PmoailhcCtrllineGainCstPoutValue_Type())
pmoailhcCtrllineGainCstPoutValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrllineGainCstPoutValue.setStatus(_A)
class _PmoailhcCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrllineGainSettingValue_Type.__name__=_E
_PmoailhcCtrllineGainSettingValue_Object=MibScalar
pmoailhcCtrllineGainSettingValue=_PmoailhcCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,55,6,3,44),_PmoailhcCtrllineGainSettingValue_Type())
pmoailhcCtrllineGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrllineGainSettingValue.setStatus(_A)
_PmoailhcCtrllineGainProcessing_ObjectIdentity=ObjectIdentity
pmoailhcCtrllineGainProcessing=_PmoailhcCtrllineGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,55,6,3,45))
_PmoailhcCtrlLineGainProc_Type=EkiOnOff
_PmoailhcCtrlLineGainProc_Object=MibScalar
pmoailhcCtrlLineGainProc=_PmoailhcCtrlLineGainProc_Object((1,3,6,1,4,1,20044,55,6,3,45,1),_PmoailhcCtrlLineGainProc_Type())
pmoailhcCtrlLineGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrlLineGainProc.setStatus(_A)
class _PmoailhcCtrllineGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrllineGainCstFiberAgingMarginValue_Type.__name__=_E
_PmoailhcCtrllineGainCstFiberAgingMarginValue_Object=MibScalar
pmoailhcCtrllineGainCstFiberAgingMarginValue=_PmoailhcCtrllineGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,55,6,3,46),_PmoailhcCtrllineGainCstFiberAgingMarginValue_Type())
pmoailhcCtrllineGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrllineGainCstFiberAgingMarginValue.setStatus(_A)
class _PmoailhcCtrllineGainCstAdddropMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcCtrllineGainCstAdddropMarginValue_Type.__name__=_E
_PmoailhcCtrllineGainCstAdddropMarginValue_Object=MibScalar
pmoailhcCtrllineGainCstAdddropMarginValue=_PmoailhcCtrllineGainCstAdddropMarginValue_Object((1,3,6,1,4,1,20044,55,6,3,47),_PmoailhcCtrllineGainCstAdddropMarginValue_Type())
pmoailhcCtrllineGainCstAdddropMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCtrllineGainCstAdddropMarginValue.setStatus(_A)
_Pmoailhcri_ObjectIdentity=ObjectIdentity
pmoailhcri=_Pmoailhcri_ObjectIdentity((1,3,6,1,4,1,20044,55,7))
_PmoailhcRinvReloadInventory_Type=EkiOnOff
_PmoailhcRinvReloadInventory_Object=MibScalar
pmoailhcRinvReloadInventory=_PmoailhcRinvReloadInventory_Object((1,3,6,1,4,1,20044,55,7,2),_PmoailhcRinvReloadInventory_Type())
pmoailhcRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcRinvReloadInventory.setStatus(_A)
_PmoailhcRinvModulePlatform_Type=DisplayString
_PmoailhcRinvModulePlatform_Object=MibScalar
pmoailhcRinvModulePlatform=_PmoailhcRinvModulePlatform_Object((1,3,6,1,4,1,20044,55,7,3),_PmoailhcRinvModulePlatform_Type())
pmoailhcRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvModulePlatform.setStatus(_A)
_PmoailhcRinvSwPlatform_Type=DisplayString
_PmoailhcRinvSwPlatform_Object=MibScalar
pmoailhcRinvSwPlatform=_PmoailhcRinvSwPlatform_Object((1,3,6,1,4,1,20044,55,7,4),_PmoailhcRinvSwPlatform_Type())
pmoailhcRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvSwPlatform.setStatus(_A)
_PmoailhcRinvSwFoa_Type=DisplayString
_PmoailhcRinvSwFoa_Object=MibScalar
pmoailhcRinvSwFoa=_PmoailhcRinvSwFoa_Object((1,3,6,1,4,1,20044,55,7,5),_PmoailhcRinvSwFoa_Type())
pmoailhcRinvSwFoa.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvSwFoa.setStatus(_A)
_PmoailhcRinvInLine1Table_Object=MibTable
pmoailhcRinvInLine1Table=_PmoailhcRinvInLine1Table_Object((1,3,6,1,4,1,20044,55,7,6))
if mibBuilder.loadTexts:pmoailhcRinvInLine1Table.setStatus(_A)
_PmoailhcRinvInLine1Entry_Object=MibTableRow
pmoailhcRinvInLine1Entry=_PmoailhcRinvInLine1Entry_Object((1,3,6,1,4,1,20044,55,7,6,1))
pmoailhcRinvInLine1Entry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:pmoailhcRinvInLine1Entry.setStatus(_A)
class _PmoailhcRinvInLine1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoailhcRinvInLine1Index_Type.__name__=_E
_PmoailhcRinvInLine1Index_Object=MibTableColumn
pmoailhcRinvInLine1Index=_PmoailhcRinvInLine1Index_Object((1,3,6,1,4,1,20044,55,7,6,1,1),_PmoailhcRinvInLine1Index_Type())
pmoailhcRinvInLine1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvInLine1Index.setStatus(_A)
_PmoailhcRinvInLine1_Type=DisplayString
_PmoailhcRinvInLine1_Object=MibTableColumn
pmoailhcRinvInLine1=_PmoailhcRinvInLine1_Object((1,3,6,1,4,1,20044,55,7,6,1,2),_PmoailhcRinvInLine1_Type())
pmoailhcRinvInLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvInLine1.setStatus(_A)
_PmoailhcRinvInLine2Table_Object=MibTable
pmoailhcRinvInLine2Table=_PmoailhcRinvInLine2Table_Object((1,3,6,1,4,1,20044,55,7,7))
if mibBuilder.loadTexts:pmoailhcRinvInLine2Table.setStatus(_A)
_PmoailhcRinvInLine2Entry_Object=MibTableRow
pmoailhcRinvInLine2Entry=_PmoailhcRinvInLine2Entry_Object((1,3,6,1,4,1,20044,55,7,7,1))
pmoailhcRinvInLine2Entry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:pmoailhcRinvInLine2Entry.setStatus(_A)
class _PmoailhcRinvInLine2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoailhcRinvInLine2Index_Type.__name__=_E
_PmoailhcRinvInLine2Index_Object=MibTableColumn
pmoailhcRinvInLine2Index=_PmoailhcRinvInLine2Index_Object((1,3,6,1,4,1,20044,55,7,7,1,1),_PmoailhcRinvInLine2Index_Type())
pmoailhcRinvInLine2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvInLine2Index.setStatus(_A)
_PmoailhcRinvInLine2_Type=DisplayString
_PmoailhcRinvInLine2_Object=MibTableColumn
pmoailhcRinvInLine2=_PmoailhcRinvInLine2_Object((1,3,6,1,4,1,20044,55,7,7,1,2),_PmoailhcRinvInLine2_Type())
pmoailhcRinvInLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcRinvInLine2.setStatus(_A)
_PmoailhcConfig_ObjectIdentity=ObjectIdentity
pmoailhcConfig=_PmoailhcConfig_ObjectIdentity((1,3,6,1,4,1,20044,55,9))
_PmoailhcCfgNoValue_ObjectIdentity=ObjectIdentity
pmoailhcCfgNoValue=_PmoailhcCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,55,9,1))
_PmoailhctableclientStartup_ObjectIdentity=ObjectIdentity
pmoailhctableclientStartup=_PmoailhctableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,55,9,1,1))
class _PmoailhcCfgclientEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientEdfaLaserCtrl_Type.__name__=_F
_PmoailhcCfgclientEdfaLaserCtrl_Object=MibScalar
pmoailhcCfgclientEdfaLaserCtrl=_PmoailhcCfgclientEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,55,9,1,1,2),_PmoailhcCfgclientEdfaLaserCtrl_Type())
pmoailhcCfgclientEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientEdfaLaserCtrl.setStatus(_A)
class _PmoailhcCfgclientEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientEdfaLaserMode_Type.__name__=_F
_PmoailhcCfgclientEdfaLaserMode_Object=MibScalar
pmoailhcCfgclientEdfaLaserMode=_PmoailhcCfgclientEdfaLaserMode_Object((1,3,6,1,4,1,20044,55,9,1,1,3),_PmoailhcCfgclientEdfaLaserMode_Type())
pmoailhcCfgclientEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientEdfaLaserMode.setStatus(_A)
class _PmoailhcCfgclientGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientGainValue_Type.__name__=_F
_PmoailhcCfgclientGainValue_Object=MibScalar
pmoailhcCfgclientGainValue=_PmoailhcCfgclientGainValue_Object((1,3,6,1,4,1,20044,55,9,1,1,4),_PmoailhcCfgclientGainValue_Type())
pmoailhcCfgclientGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientGainValue.setStatus(_A)
class _PmoailhcCfgclientTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientTiltValue_Type.__name__=_F
_PmoailhcCfgclientTiltValue_Object=MibScalar
pmoailhcCfgclientTiltValue=_PmoailhcCfgclientTiltValue_Object((1,3,6,1,4,1,20044,55,9,1,1,5),_PmoailhcCfgclientTiltValue_Type())
pmoailhcCfgclientTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientTiltValue.setStatus(_A)
class _PmoailhcCfgclientMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientMsaLoss_Type.__name__=_F
_PmoailhcCfgclientMsaLoss_Object=MibScalar
pmoailhcCfgclientMsaLoss=_PmoailhcCfgclientMsaLoss_Object((1,3,6,1,4,1,20044,55,9,1,1,6),_PmoailhcCfgclientMsaLoss_Type())
pmoailhcCfgclientMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientMsaLoss.setStatus(_A)
class _PmoailhcCfgclientOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientOutputPowerValue_Type.__name__=_F
_PmoailhcCfgclientOutputPowerValue_Object=MibScalar
pmoailhcCfgclientOutputPowerValue=_PmoailhcCfgclientOutputPowerValue_Object((1,3,6,1,4,1,20044,55,9,1,1,7),_PmoailhcCfgclientOutputPowerValue_Type())
pmoailhcCfgclientOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientOutputPowerValue.setStatus(_A)
class _PmoailhcCfgclientAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgclientAseCompensation_Type.__name__=_F
_PmoailhcCfgclientAseCompensation_Object=MibScalar
pmoailhcCfgclientAseCompensation=_PmoailhcCfgclientAseCompensation_Object((1,3,6,1,4,1,20044,55,9,1,1,8),_PmoailhcCfgclientAseCompensation_Type())
pmoailhcCfgclientAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgclientAseCompensation.setStatus(_A)
_PmoailhcCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoailhcCfgLineStartUp=_PmoailhcCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,55,9,2))
_PmoailhctablelineStartup_ObjectIdentity=ObjectIdentity
pmoailhctablelineStartup=_PmoailhctablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,55,9,2,1))
class _PmoailhcCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineEdfaLaserCtrl_Type.__name__=_F
_PmoailhcCfglineEdfaLaserCtrl_Object=MibScalar
pmoailhcCfglineEdfaLaserCtrl=_PmoailhcCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,55,9,2,1,2),_PmoailhcCfglineEdfaLaserCtrl_Type())
pmoailhcCfglineEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoailhcCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineEdfaLaserMode_Type.__name__=_F
_PmoailhcCfglineEdfaLaserMode_Object=MibScalar
pmoailhcCfglineEdfaLaserMode=_PmoailhcCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,55,9,2,1,3),_PmoailhcCfglineEdfaLaserMode_Type())
pmoailhcCfglineEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineEdfaLaserMode.setStatus(_A)
class _PmoailhcCfglineGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineGainValue_Type.__name__=_F
_PmoailhcCfglineGainValue_Object=MibScalar
pmoailhcCfglineGainValue=_PmoailhcCfglineGainValue_Object((1,3,6,1,4,1,20044,55,9,2,1,4),_PmoailhcCfglineGainValue_Type())
pmoailhcCfglineGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineGainValue.setStatus(_A)
class _PmoailhcCfglineTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineTiltValue_Type.__name__=_F
_PmoailhcCfglineTiltValue_Object=MibScalar
pmoailhcCfglineTiltValue=_PmoailhcCfglineTiltValue_Object((1,3,6,1,4,1,20044,55,9,2,1,5),_PmoailhcCfglineTiltValue_Type())
pmoailhcCfglineTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineTiltValue.setStatus(_A)
class _PmoailhcCfglineMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineMsaLoss_Type.__name__=_F
_PmoailhcCfglineMsaLoss_Object=MibScalar
pmoailhcCfglineMsaLoss=_PmoailhcCfglineMsaLoss_Object((1,3,6,1,4,1,20044,55,9,2,1,6),_PmoailhcCfglineMsaLoss_Type())
pmoailhcCfglineMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineMsaLoss.setStatus(_A)
class _PmoailhcCfglineOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineOutputPowerValue_Type.__name__=_F
_PmoailhcCfglineOutputPowerValue_Object=MibScalar
pmoailhcCfglineOutputPowerValue=_PmoailhcCfglineOutputPowerValue_Object((1,3,6,1,4,1,20044,55,9,2,1,7),_PmoailhcCfglineOutputPowerValue_Type())
pmoailhcCfglineOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineOutputPowerValue.setStatus(_A)
class _PmoailhcCfglineAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfglineAseCompensation_Type.__name__=_F
_PmoailhcCfglineAseCompensation_Object=MibScalar
pmoailhcCfglineAseCompensation=_PmoailhcCfglineAseCompensation_Object((1,3,6,1,4,1,20044,55,9,2,1,8),_PmoailhcCfglineAseCompensation_Type())
pmoailhcCfglineAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfglineAseCompensation.setStatus(_A)
class _PmoailhcCfgaprMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcCfgaprMode_Type.__name__=_F
_PmoailhcCfgaprMode_Object=MibScalar
pmoailhcCfgaprMode=_PmoailhcCfgaprMode_Object((1,3,6,1,4,1,20044,55,9,2,1,11),_PmoailhcCfgaprMode_Type())
pmoailhcCfgaprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgaprMode.setStatus(_A)
_PmoailhcCfgLabels_ObjectIdentity=ObjectIdentity
pmoailhcCfgLabels=_PmoailhcCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,55,9,3))
_PmoailhcCfgLabelclientTable_Object=MibTable
pmoailhcCfgLabelclientTable=_PmoailhcCfgLabelclientTable_Object((1,3,6,1,4,1,20044,55,9,3,1))
if mibBuilder.loadTexts:pmoailhcCfgLabelclientTable.setStatus(_A)
_PmoailhcCfgLabelclientEntry_Object=MibTableRow
pmoailhcCfgLabelclientEntry=_PmoailhcCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,55,9,3,1,1))
pmoailhcCfgLabelclientEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:pmoailhcCfgLabelclientEntry.setStatus(_A)
class _PmoailhcCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcCfgLabelclientIndex_Type.__name__=_E
_PmoailhcCfgLabelclientIndex_Object=MibTableColumn
pmoailhcCfgLabelclientIndex=_PmoailhcCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,55,9,3,1,1,1),_PmoailhcCfgLabelclientIndex_Type())
pmoailhcCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcCfgLabelclientIndex.setStatus(_A)
class _PmoailhcCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoailhcCfgLabelclientPortn_Type.__name__=_H
_PmoailhcCfgLabelclientPortn_Object=MibTableColumn
pmoailhcCfgLabelclientPortn=_PmoailhcCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,55,9,3,1,1,3),_PmoailhcCfgLabelclientPortn_Type())
pmoailhcCfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgLabelclientPortn.setStatus(_A)
_PmoailhcCfgLabellineTable_Object=MibTable
pmoailhcCfgLabellineTable=_PmoailhcCfgLabellineTable_Object((1,3,6,1,4,1,20044,55,9,3,2))
if mibBuilder.loadTexts:pmoailhcCfgLabellineTable.setStatus(_A)
_PmoailhcCfgLabellineEntry_Object=MibTableRow
pmoailhcCfgLabellineEntry=_PmoailhcCfgLabellineEntry_Object((1,3,6,1,4,1,20044,55,9,3,2,1))
pmoailhcCfgLabellineEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:pmoailhcCfgLabellineEntry.setStatus(_A)
class _PmoailhcCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcCfgLabellineIndex_Type.__name__=_E
_PmoailhcCfgLabellineIndex_Object=MibTableColumn
pmoailhcCfgLabellineIndex=_PmoailhcCfgLabellineIndex_Object((1,3,6,1,4,1,20044,55,9,3,2,1,1),_PmoailhcCfgLabellineIndex_Type())
pmoailhcCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcCfgLabellineIndex.setStatus(_A)
class _PmoailhcCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoailhcCfgLabellinePortn_Type.__name__=_H
_PmoailhcCfgLabellinePortn_Object=MibTableColumn
pmoailhcCfgLabellinePortn=_PmoailhcCfgLabellinePortn_Object((1,3,6,1,4,1,20044,55,9,3,2,1,3),_PmoailhcCfgLabellinePortn_Type())
pmoailhcCfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgLabellinePortn.setStatus(_A)
_PmoailhcCfgWriteConfiguration_Type=EkiOnOff
_PmoailhcCfgWriteConfiguration_Object=MibScalar
pmoailhcCfgWriteConfiguration=_PmoailhcCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,55,9,257),_PmoailhcCfgWriteConfiguration_Type())
pmoailhcCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcCfgWriteConfiguration.setStatus(_A)
_Pmoailhctraps_ObjectIdentity=ObjectIdentity
pmoailhctraps=_Pmoailhctraps_ObjectIdentity((1,3,6,1,4,1,20044,55,10))
class _PmoailhctrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoailhctrapBoardNumber_Type.__name__=_E
_PmoailhctrapBoardNumber_Object=MibScalar
pmoailhctrapBoardNumber=_PmoailhctrapBoardNumber_Object((1,3,6,1,4,1,20044,55,10,4),_PmoailhctrapBoardNumber_Type())
pmoailhctrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhctrapBoardNumber.setStatus(_A)
pmoailhcLineTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,30))
pmoailhcLineTrapNotUrgentGoesOn.setObjects(*((_D,_I),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcLineTrapNotUrgentGoesOn.setStatus(_A)
pmoailhcLineTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,31))
pmoailhcLineTrapNotUrgentGoesOff.setObjects(*((_D,_I),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcLineTrapNotUrgentGoesOff.setStatus(_A)
pmoailhcLineTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,32))
pmoailhcLineTrapUrgentGoesOn.setObjects(*((_D,_J),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcLineTrapUrgentGoesOn.setStatus(_A)
pmoailhcLineTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,33))
pmoailhcLineTrapUrgentGoesOff.setObjects(*((_D,_J),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcLineTrapUrgentGoesOff.setStatus(_A)
pmoailhcLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,34))
pmoailhcLineTrapCritGoesOn.setObjects(*((_D,_K),(_D,_L),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcLineTrapCritGoesOn.setStatus(_A)
pmoailhcLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,35))
pmoailhcLineTrapCritGoesOff.setObjects(*((_D,_K),(_D,_L),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcLineTrapCritGoesOff.setStatus(_A)
pmoailhcClientTrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,40))
pmoailhcClientTrapNotUrgentGoesOn.setObjects(*((_D,_M),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcClientTrapNotUrgentGoesOn.setStatus(_A)
pmoailhcClientTrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,41))
pmoailhcClientTrapNotUrgentGoesOff.setObjects(*((_D,_M),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcClientTrapNotUrgentGoesOff.setStatus(_A)
pmoailhcClientTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,42))
pmoailhcClientTrapUrgentGoesOn.setObjects(*((_D,_N),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcClientTrapUrgentGoesOn.setStatus(_A)
pmoailhcClientTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,43))
pmoailhcClientTrapUrgentGoesOff.setObjects(*((_D,_N),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcClientTrapUrgentGoesOff.setStatus(_A)
pmoailhcClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,44))
pmoailhcClientTrapCritGoesOn.setObjects(*((_D,_O),(_D,_P),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcClientTrapCritGoesOn.setStatus(_A)
pmoailhcClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,45))
pmoailhcClientTrapCritGoesOff.setObjects(*((_D,_O),(_D,_P),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcClientTrapCritGoesOff.setStatus(_A)
pmoailhcPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,55,10,50))
pmoailhcPowerTrapUrgentGoesOn.setObjects(*((_D,_Q),(_D,_R),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcPowerTrapUrgentGoesOn.setStatus(_A)
pmoailhcPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,55,10,51))
pmoailhcPowerTrapUrgentGoesOff.setObjects(*((_D,_Q),(_D,_R),(_D,_G)))
if mibBuilder.loadTexts:pmoailhcPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PmoailhcpreampMode':PmoailhcpreampMode,'PmoailhcboosterMode':PmoailhcboosterMode,'PmoailhcaprMode':PmoailhcaprMode,'PmoailhcPreampGainAdjMode':PmoailhcPreampGainAdjMode,'PmoailhcBoosterGainAdjMode':PmoailhcBoosterGainAdjMode,'PmoailhcPreampCstGainAdjMode':PmoailhcPreampCstGainAdjMode,'PmoailhcBoosterCstGainAdjMode':PmoailhcBoosterCstGainAdjMode,'modulepmoailhc':modulepmoailhc,'pmoailhcalarms':pmoailhcalarms,'pmoailhcAlmOther':pmoailhcAlmOther,'pmoailhcAlmOtherNurg':pmoailhcAlmOtherNurg,'pmoailhcAlmsynthAlm2':pmoailhcAlmsynthAlm2,'pmoailhcAlmConfTableSave':pmoailhcAlmConfTableSave,'pmoailhcAlmInvUpload':pmoailhcAlmInvUpload,'pmoailhcAlmConfTableLoad':pmoailhcAlmConfTableLoad,'pmoailhcAlmfoaWarnings':pmoailhcAlmfoaWarnings,'pmoailhcAlmTermpLowWarning':pmoailhcAlmTermpLowWarning,'pmoailhcAlmTempHighWarning':pmoailhcAlmTempHighWarning,'pmoailhcAlmOtherUrg':pmoailhcAlmOtherUrg,'pmoailhcAlmfoaAlarms':pmoailhcAlmfoaAlarms,'pmoailhcAlmTermpLowAlarm':pmoailhcAlmTermpLowAlarm,'pmoailhcAlmTempHighAlarm':pmoailhcAlmTempHighAlarm,'pmoailhcAlmOtherCrit':pmoailhcAlmOtherCrit,'pmoailhcAlmsynthAlm0':pmoailhcAlmsynthAlm0,'pmoailhcAlmMaintenanceMode':pmoailhcAlmMaintenanceMode,'pmoailhcAlmAprOn':pmoailhcAlmAprOn,'pmoailhcAlmModGlobFail':pmoailhcAlmModGlobFail,'pmoailhcAlmUpEdfaInitNotCompl':pmoailhcAlmUpEdfaInitNotCompl,'pmoailhcAlmDwEdfaInitNotCompl':pmoailhcAlmDwEdfaInitNotCompl,'pmoailhcAlmExtPump1NotLocked':pmoailhcAlmExtPump1NotLocked,'pmoailhcAlmExtPump2NotLocked':pmoailhcAlmExtPump2NotLocked,_R:pmoailhcAlmDefFuseA,_Q:pmoailhcAlmDefFuseB,'pmoailhcAlmClient':pmoailhcAlmClient,'pmoailhcAlmClientNurg':pmoailhcAlmClientNurg,'pmoailhcAlmclientEdfaWarnings':pmoailhcAlmclientEdfaWarnings,'pmoailhcAlmClientGainLowWarning':pmoailhcAlmClientGainLowWarning,'pmoailhcAlmClientGainHighWarning':pmoailhcAlmClientGainHighWarning,'pmoailhcAlmClientInputPwrLowWarning':pmoailhcAlmClientInputPwrLowWarning,'pmoailhcAlmClientInputPwrHighWarning':pmoailhcAlmClientInputPwrHighWarning,'pmoailhcAlmClientOutputPwrLowWarning':pmoailhcAlmClientOutputPwrLowWarning,'pmoailhcAlmClientOutputPwrHighWarning':pmoailhcAlmClientOutputPwrHighWarning,'pmoailhcAlmClientBiasLowWarning':pmoailhcAlmClientBiasLowWarning,'pmoailhcAlmClientBiasHighWarning':pmoailhcAlmClientBiasHighWarning,'pmoailhcAlmClientUrg':pmoailhcAlmClientUrg,'pmoailhcAlmclientEdfaAlarms1':pmoailhcAlmclientEdfaAlarms1,'pmoailhcAlmClientGainLowAlarm':pmoailhcAlmClientGainLowAlarm,'pmoailhcAlmClientGainHighAlarm':pmoailhcAlmClientGainHighAlarm,'pmoailhcAlmClientInputPwrLowAlarm':pmoailhcAlmClientInputPwrLowAlarm,'pmoailhcAlmClientInputPwrHighAlarm':pmoailhcAlmClientInputPwrHighAlarm,'pmoailhcAlmClientOutputPwrLowAlarm':pmoailhcAlmClientOutputPwrLowAlarm,'pmoailhcAlmClientOutputPwrHighAlarm':pmoailhcAlmClientOutputPwrHighAlarm,'pmoailhcAlmClientBiasLowAlarm':pmoailhcAlmClientBiasLowAlarm,'pmoailhcAlmClientBiasHighAlarm':pmoailhcAlmClientBiasHighAlarm,'pmoailhcAlmClientCrit':pmoailhcAlmClientCrit,'pmoailhcAlmsynthAlm8':pmoailhcAlmsynthAlm8,_P:pmoailhcAlmClientHwFail,'pmoailhcAlmClientTxOff':pmoailhcAlmClientTxOff,_M:pmoailhcAlmClientDdmWarning,_N:pmoailhcAlmClientDdmAlm,_O:pmoailhcAlmClientFail,'pmoailhcAlmClientExtPumpFail':pmoailhcAlmClientExtPumpFail,'pmoailhcAlmclientEdfaAlarms2':pmoailhcAlmclientEdfaAlarms2,'pmoailhcAlmClientEdfaNr':pmoailhcAlmClientEdfaNr,'pmoailhcAlmClientEdfaTecFail':pmoailhcAlmClientEdfaTecFail,'pmoailhcAlmClientEdfaLaserFail':pmoailhcAlmClientEdfaLaserFail,'pmoailhcAlmClientEdfaLos':pmoailhcAlmClientEdfaLos,'pmoailhcAlmClientExtPumpEdfaLowCurrent':pmoailhcAlmClientExtPumpEdfaLowCurrent,'pmoailhcAlmLine':pmoailhcAlmLine,'pmoailhcAlmLineNurg':pmoailhcAlmLineNurg,'pmoailhcAlmlineEdfaWarnings':pmoailhcAlmlineEdfaWarnings,'pmoailhcAlmLineGainLowWarning':pmoailhcAlmLineGainLowWarning,'pmoailhcAlmLineGainHighWarning':pmoailhcAlmLineGainHighWarning,'pmoailhcAlmLineInputPwrLowWarning':pmoailhcAlmLineInputPwrLowWarning,'pmoailhcAlmLineInputPwrHighWarning':pmoailhcAlmLineInputPwrHighWarning,'pmoailhcAlmLineOutputPwrLowWarning':pmoailhcAlmLineOutputPwrLowWarning,'pmoailhcAlmLineOutputPwrHighWarning':pmoailhcAlmLineOutputPwrHighWarning,'pmoailhcAlmLineBiasLowWarning':pmoailhcAlmLineBiasLowWarning,'pmoailhcAlmLineBiasHighWarning':pmoailhcAlmLineBiasHighWarning,'pmoailhcAlmLineUrg':pmoailhcAlmLineUrg,'pmoailhcAlmlineEdfaAlarms1':pmoailhcAlmlineEdfaAlarms1,'pmoailhcAlmLineGainLowAlarm':pmoailhcAlmLineGainLowAlarm,'pmoailhcAlmLineGainHighAlarm':pmoailhcAlmLineGainHighAlarm,'pmoailhcAlmLineInputPwrLowAlarm':pmoailhcAlmLineInputPwrLowAlarm,'pmoailhcAlmLineInputPwrHighAlarm':pmoailhcAlmLineInputPwrHighAlarm,'pmoailhcAlmLineOutputPwrLowAlarm':pmoailhcAlmLineOutputPwrLowAlarm,'pmoailhcAlmLineOutputPwrHighAlarm':pmoailhcAlmLineOutputPwrHighAlarm,'pmoailhcAlmLineBiasLowAlarm':pmoailhcAlmLineBiasLowAlarm,'pmoailhcAlmLineBiasHighAlarm':pmoailhcAlmLineBiasHighAlarm,'pmoailhcAlmLineCrit':pmoailhcAlmLineCrit,'pmoailhcAlmsynthAlm7':pmoailhcAlmsynthAlm7,_L:pmoailhcAlmLineHwFail,'pmoailhcAlmLineTxOff':pmoailhcAlmLineTxOff,_I:pmoailhcAlmLineDdmWarning,_J:pmoailhcAlmLineDdmAlm,_K:pmoailhcAlmLineFail,'pmoailhcAlmLineExtPumpFail':pmoailhcAlmLineExtPumpFail,'pmoailhcAlmlineEdfaAlarms2':pmoailhcAlmlineEdfaAlarms2,'pmoailhcAlmLineEdfaNr':pmoailhcAlmLineEdfaNr,'pmoailhcAlmLineEdfaTecFail':pmoailhcAlmLineEdfaTecFail,'pmoailhcAlmLineEdfaLaserFail':pmoailhcAlmLineEdfaLaserFail,'pmoailhcAlmLineEdfaLos':pmoailhcAlmLineEdfaLos,'pmoailhcAlmLineExtPumpEdfaLowCurrent':pmoailhcAlmLineExtPumpEdfaLowCurrent,'pmoailhcmeasures':pmoailhcmeasures,'pmoailhcMesrOther':pmoailhcMesrOther,'pmoailhcMesrtempMeas':pmoailhcMesrtempMeas,'pmoailhcMesrClient':pmoailhcMesrClient,'pmoailhcMesrclientEdfaBiasMeas':pmoailhcMesrclientEdfaBiasMeas,'pmoailhcMesrclientEdfaTxpwrMeas':pmoailhcMesrclientEdfaTxpwrMeas,'pmoailhcMesrclientEdfaRxpwrMeas':pmoailhcMesrclientEdfaRxpwrMeas,'pmoailhcMesrclientEdfaGainMeas':pmoailhcMesrclientEdfaGainMeas,'pmoailhcMesrclientCorrectedGain':pmoailhcMesrclientCorrectedGain,'pmoailhcMesrLine':pmoailhcMesrLine,'pmoailhcMesrlineEdfaBiasMeas':pmoailhcMesrlineEdfaBiasMeas,'pmoailhcMesrlineEdfaTxpwrMeas':pmoailhcMesrlineEdfaTxpwrMeas,'pmoailhcMesrlineEdfaRxpwrMeas':pmoailhcMesrlineEdfaRxpwrMeas,'pmoailhcMesrlineEdfaGainMeas':pmoailhcMesrlineEdfaGainMeas,'pmoailhcMesrlineCorrectedGain':pmoailhcMesrlineCorrectedGain,'pmoailhccontrolsWrite':pmoailhccontrolsWrite,'pmoailhcCtrlOther':pmoailhcCtrlOther,'pmoailhcCtrlsynth0':pmoailhcCtrlsynth0,'pmoailhcCtrlConfLoad':pmoailhcCtrlConfLoad,'pmoailhcCtrlConfFlash':pmoailhcCtrlConfFlash,'pmoailhcCtrlConfClear':pmoailhcCtrlConfClear,'pmoailhcCtrlswMgnt':pmoailhcCtrlswMgnt,'pmoailhcCtrlColdReset':pmoailhcCtrlColdReset,'pmoailhcCtrlWarmReset':pmoailhcCtrlWarmReset,'pmoailhcCtrlledTest':pmoailhcCtrlledTest,'pmoailhcCtrlGreenLed':pmoailhcCtrlGreenLed,'pmoailhcCtrlRedLed':pmoailhcCtrlRedLed,'pmoailhcCtrlLedOff':pmoailhcCtrlLedOff,'pmoailhcCtrlmaintMode':pmoailhcCtrlmaintMode,'pmoailhcCtrlMaintenance':pmoailhcCtrlMaintenance,'pmoailhcCtrlaprRestart':pmoailhcCtrlaprRestart,'pmoailhcCtrlAprManualRestart':pmoailhcCtrlAprManualRestart,'pmoailhcCtrlClient':pmoailhcCtrlClient,'pmoailhcCtrlclientEdfaLaserOff':pmoailhcCtrlclientEdfaLaserOff,'pmoailhcCtrlClientEdfaLaserOff':pmoailhcCtrlClientEdfaLaserOff,'pmoailhcCtrlclientGainCstMonitorValue':pmoailhcCtrlclientGainCstMonitorValue,'pmoailhcCtrlclientGainCstPoutValue':pmoailhcCtrlclientGainCstPoutValue,'pmoailhcCtrlclientGainSettingValue':pmoailhcCtrlclientGainSettingValue,'pmoailhcCtrlclientGainProcessing':pmoailhcCtrlclientGainProcessing,'pmoailhcCtrlClientGainProc':pmoailhcCtrlClientGainProc,'pmoailhcCtrlclientGainCstFiberAgingMarginValue':pmoailhcCtrlclientGainCstFiberAgingMarginValue,'pmoailhcCtrlclientGainCstAdddropMarginValue':pmoailhcCtrlclientGainCstAdddropMarginValue,'pmoailhcCtrlLine':pmoailhcCtrlLine,'pmoailhcCtrllineEdfaLaserOff':pmoailhcCtrllineEdfaLaserOff,'pmoailhcCtrlLineEdfaLaserOff':pmoailhcCtrlLineEdfaLaserOff,'pmoailhcCtrllineGainCstMonitorValue':pmoailhcCtrllineGainCstMonitorValue,'pmoailhcCtrllineGainCstPoutValue':pmoailhcCtrllineGainCstPoutValue,'pmoailhcCtrllineGainSettingValue':pmoailhcCtrllineGainSettingValue,'pmoailhcCtrllineGainProcessing':pmoailhcCtrllineGainProcessing,'pmoailhcCtrlLineGainProc':pmoailhcCtrlLineGainProc,'pmoailhcCtrllineGainCstFiberAgingMarginValue':pmoailhcCtrllineGainCstFiberAgingMarginValue,'pmoailhcCtrllineGainCstAdddropMarginValue':pmoailhcCtrllineGainCstAdddropMarginValue,'pmoailhcri':pmoailhcri,'pmoailhcRinvReloadInventory':pmoailhcRinvReloadInventory,'pmoailhcRinvModulePlatform':pmoailhcRinvModulePlatform,'pmoailhcRinvSwPlatform':pmoailhcRinvSwPlatform,'pmoailhcRinvSwFoa':pmoailhcRinvSwFoa,'pmoailhcRinvInLine1Table':pmoailhcRinvInLine1Table,'pmoailhcRinvInLine1Entry':pmoailhcRinvInLine1Entry,_T:pmoailhcRinvInLine1Index,'pmoailhcRinvInLine1':pmoailhcRinvInLine1,'pmoailhcRinvInLine2Table':pmoailhcRinvInLine2Table,'pmoailhcRinvInLine2Entry':pmoailhcRinvInLine2Entry,_U:pmoailhcRinvInLine2Index,'pmoailhcRinvInLine2':pmoailhcRinvInLine2,'pmoailhcConfig':pmoailhcConfig,'pmoailhcCfgNoValue':pmoailhcCfgNoValue,'pmoailhctableclientStartup':pmoailhctableclientStartup,'pmoailhcCfgclientEdfaLaserCtrl':pmoailhcCfgclientEdfaLaserCtrl,'pmoailhcCfgclientEdfaLaserMode':pmoailhcCfgclientEdfaLaserMode,'pmoailhcCfgclientGainValue':pmoailhcCfgclientGainValue,'pmoailhcCfgclientTiltValue':pmoailhcCfgclientTiltValue,'pmoailhcCfgclientMsaLoss':pmoailhcCfgclientMsaLoss,'pmoailhcCfgclientOutputPowerValue':pmoailhcCfgclientOutputPowerValue,'pmoailhcCfgclientAseCompensation':pmoailhcCfgclientAseCompensation,'pmoailhcCfgLineStartUp':pmoailhcCfgLineStartUp,'pmoailhctablelineStartup':pmoailhctablelineStartup,'pmoailhcCfglineEdfaLaserCtrl':pmoailhcCfglineEdfaLaserCtrl,'pmoailhcCfglineEdfaLaserMode':pmoailhcCfglineEdfaLaserMode,'pmoailhcCfglineGainValue':pmoailhcCfglineGainValue,'pmoailhcCfglineTiltValue':pmoailhcCfglineTiltValue,'pmoailhcCfglineMsaLoss':pmoailhcCfglineMsaLoss,'pmoailhcCfglineOutputPowerValue':pmoailhcCfglineOutputPowerValue,'pmoailhcCfglineAseCompensation':pmoailhcCfglineAseCompensation,'pmoailhcCfgaprMode':pmoailhcCfgaprMode,'pmoailhcCfgLabels':pmoailhcCfgLabels,'pmoailhcCfgLabelclientTable':pmoailhcCfgLabelclientTable,'pmoailhcCfgLabelclientEntry':pmoailhcCfgLabelclientEntry,_V:pmoailhcCfgLabelclientIndex,'pmoailhcCfgLabelclientPortn':pmoailhcCfgLabelclientPortn,'pmoailhcCfgLabellineTable':pmoailhcCfgLabellineTable,'pmoailhcCfgLabellineEntry':pmoailhcCfgLabellineEntry,_W:pmoailhcCfgLabellineIndex,'pmoailhcCfgLabellinePortn':pmoailhcCfgLabellinePortn,'pmoailhcCfgWriteConfiguration':pmoailhcCfgWriteConfiguration,'pmoailhctraps':pmoailhctraps,_G:pmoailhctrapBoardNumber,'pmoailhcLineTrapNotUrgentGoesOn':pmoailhcLineTrapNotUrgentGoesOn,'pmoailhcLineTrapNotUrgentGoesOff':pmoailhcLineTrapNotUrgentGoesOff,'pmoailhcLineTrapUrgentGoesOn':pmoailhcLineTrapUrgentGoesOn,'pmoailhcLineTrapUrgentGoesOff':pmoailhcLineTrapUrgentGoesOff,'pmoailhcLineTrapCritGoesOn':pmoailhcLineTrapCritGoesOn,'pmoailhcLineTrapCritGoesOff':pmoailhcLineTrapCritGoesOff,'pmoailhcClientTrapNotUrgentGoesOn':pmoailhcClientTrapNotUrgentGoesOn,'pmoailhcClientTrapNotUrgentGoesOff':pmoailhcClientTrapNotUrgentGoesOff,'pmoailhcClientTrapUrgentGoesOn':pmoailhcClientTrapUrgentGoesOn,'pmoailhcClientTrapUrgentGoesOff':pmoailhcClientTrapUrgentGoesOff,'pmoailhcClientTrapCritGoesOn':pmoailhcClientTrapCritGoesOn,'pmoailhcClientTrapCritGoesOff':pmoailhcClientTrapCritGoesOff,'pmoailhcPowerTrapUrgentGoesOn':pmoailhcPowerTrapUrgentGoesOn,'pmoailhcPowerTrapUrgentGoesOff':pmoailhcPowerTrapUrgentGoesOff})