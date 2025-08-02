_Z='pmoabphcsCfgLabellineIndex'
_Y='pmoabphcsCfgLabelclientIndex'
_X='pmoabphcsCfgLineStartupIndex'
_W='pmoabphcsRinvPreAmpIndex'
_V='pmoabphcsRinvBoosterIndex'
_U='pmoabphcsCntlineOscErrIndex'
_T='pmoabphcsMesrlineOscRxPowerIndex'
_S='pmoabphcsMesrlineOscTxPowerIndex'
_R='pmoabphcsAlmlineOscThresholdsWarningsIndex'
_Q='pmoabphcsAlmlineOscThresholdAlarmsIndex'
_P='pmoabphcsAlmlineOscAlarmsIndex'
_O='2014-03-10 00:00'
_N='pmoabphcsAlmDefFuseA'
_M='pmoabphcsAlmDefFuseB'
_L='pmoabphcsAlmClientHwFail'
_K='pmoabphcsAlmClientFail'
_J='pmoabphcsAlmLineHwFail'
_I='pmoabphcsAlmLineFail'
_H='DisplayString'
_G='pmoabphcstrapBoardNumber'
_F='Unsigned32'
_E='EKINOPS-Pmoabphcs-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,EkiSynchroMode,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','EkiSynchroMode','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
modulepmoabphcs=ModuleIdentity((1,3,6,1,4,1,20044,61))
if mibBuilder.loadTexts:modulepmoabphcs.setRevisions((_O,_O,'2015-01-27 00:00','2016-05-23 00:00'))
class PmoabphcspreampMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oabphcspreampdefaultmode',0),('oabphcspreampconstantcurrentmode',1),('oabphcspreampconstantpowermode',2),('oabphcspreampconstantgainmode',3),('oabphcspreamppoutpinmode',4),('oabphcspreampmanualmode',5),('oabphcspreampfeedforwardmode',6),('oabphcspreamptransientsupmode',7)))
class PmoabphcsboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oabphcsboosterdefaultmode',0),('oabphcsboosterconstantcurrentmode',1),('oabphcsboosterconstantpowermode',2),('oabphcsboosterconstantgainmode',3),('oabphcsboosterpoutpinmode',4),('oabphcsboostermanualmode',5),('oabphcsboosterfeedforwardmode',6),('oabphcsboostertransientsupmode',7)))
class PmoabphcsaprMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('oabphcsaproffmode',0),('oabphcsaprsemiautomode',1),('oabphcsaprautomode',2),('oabphcsaprlossforwardingmode',3),('oabphcsaprrepeatmode',4)))
class PmoabphcsPreampGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oabphcspreampgainadjmanualmode',0),('oabphcspreampgainadjsemiautomode',1),('oabphcspreampgainadjautomode',2)))
class PmoabphcsBoosterGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oabphcsboostergainadjmanualmode',0),('oabphcsboostergainadjsemiautomode',1),('oabphcsboostergainadjautomode',2)))
class PmoabphcsPreampCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oabphcspreampcstgainadjsemiautomode',1),('oabphcspreampcstgainadjautomode',2)))
class PmoabphcsBoosterCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oabphcsboostercstgainadjsemiautomode',1),('oabphcsboostercstgainadjautomode',2)))
_Pmoabphcsalarms_ObjectIdentity=ObjectIdentity
pmoabphcsalarms=_Pmoabphcsalarms_ObjectIdentity((1,3,6,1,4,1,20044,61,2))
_PmoabphcsAlmOther_ObjectIdentity=ObjectIdentity
pmoabphcsAlmOther=_PmoabphcsAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1))
_PmoabphcsAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoabphcsAlmOtherNurg=_PmoabphcsAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,1))
_PmoabphcsAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoabphcsAlmsynthAlm2=_PmoabphcsAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,1,2))
_PmoabphcsAlmConfTableSave_Type=EkiOnOff
_PmoabphcsAlmConfTableSave_Object=MibScalar
pmoabphcsAlmConfTableSave=_PmoabphcsAlmConfTableSave_Object((1,3,6,1,4,1,20044,61,2,1,1,2,1),_PmoabphcsAlmConfTableSave_Type())
pmoabphcsAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmConfTableSave.setStatus(_A)
_PmoabphcsAlmInvUpload_Type=EkiOnOff
_PmoabphcsAlmInvUpload_Object=MibScalar
pmoabphcsAlmInvUpload=_PmoabphcsAlmInvUpload_Object((1,3,6,1,4,1,20044,61,2,1,1,2,2),_PmoabphcsAlmInvUpload_Type())
pmoabphcsAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmInvUpload.setStatus(_A)
_PmoabphcsAlmConfTableLoad_Type=EkiOnOff
_PmoabphcsAlmConfTableLoad_Object=MibScalar
pmoabphcsAlmConfTableLoad=_PmoabphcsAlmConfTableLoad_Object((1,3,6,1,4,1,20044,61,2,1,1,2,3),_PmoabphcsAlmConfTableLoad_Type())
pmoabphcsAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmConfTableLoad.setStatus(_A)
_PmoabphcsAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoabphcsAlmfoaWarnings=_PmoabphcsAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,1,75))
_PmoabphcsAlmTermpLowWarning_Type=EkiOnOff
_PmoabphcsAlmTermpLowWarning_Object=MibScalar
pmoabphcsAlmTermpLowWarning=_PmoabphcsAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,61,2,1,1,75,7),_PmoabphcsAlmTermpLowWarning_Type())
pmoabphcsAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmTermpLowWarning.setStatus(_A)
_PmoabphcsAlmTempHighWarning_Type=EkiOnOff
_PmoabphcsAlmTempHighWarning_Object=MibScalar
pmoabphcsAlmTempHighWarning=_PmoabphcsAlmTempHighWarning_Object((1,3,6,1,4,1,20044,61,2,1,1,75,8),_PmoabphcsAlmTempHighWarning_Type())
pmoabphcsAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmTempHighWarning.setStatus(_A)
_PmoabphcsAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoabphcsAlmOtherUrg=_PmoabphcsAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,2))
_PmoabphcsAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoabphcsAlmfoaAlarms=_PmoabphcsAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,2,74))
_PmoabphcsAlmTermpLowAlarm_Type=EkiOnOff
_PmoabphcsAlmTermpLowAlarm_Object=MibScalar
pmoabphcsAlmTermpLowAlarm=_PmoabphcsAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,61,2,1,2,74,7),_PmoabphcsAlmTermpLowAlarm_Type())
pmoabphcsAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmTermpLowAlarm.setStatus(_A)
_PmoabphcsAlmTempHighAlarm_Type=EkiOnOff
_PmoabphcsAlmTempHighAlarm_Object=MibScalar
pmoabphcsAlmTempHighAlarm=_PmoabphcsAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,61,2,1,2,74,8),_PmoabphcsAlmTempHighAlarm_Type())
pmoabphcsAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmTempHighAlarm.setStatus(_A)
_PmoabphcsAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoabphcsAlmOtherCrit=_PmoabphcsAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,3))
_PmoabphcsAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoabphcsAlmsynthAlm0=_PmoabphcsAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,61,2,1,3,0))
_PmoabphcsAlmMaintenanceMode_Type=EkiOnOff
_PmoabphcsAlmMaintenanceMode_Object=MibScalar
pmoabphcsAlmMaintenanceMode=_PmoabphcsAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,61,2,1,3,0,1),_PmoabphcsAlmMaintenanceMode_Type())
pmoabphcsAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmMaintenanceMode.setStatus(_A)
_PmoabphcsAlmAprOn_Type=EkiOnOff
_PmoabphcsAlmAprOn_Object=MibScalar
pmoabphcsAlmAprOn=_PmoabphcsAlmAprOn_Object((1,3,6,1,4,1,20044,61,2,1,3,0,2),_PmoabphcsAlmAprOn_Type())
pmoabphcsAlmAprOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmAprOn.setStatus(_A)
_PmoabphcsAlmModGlobFail_Type=EkiOnOff
_PmoabphcsAlmModGlobFail_Object=MibScalar
pmoabphcsAlmModGlobFail=_PmoabphcsAlmModGlobFail_Object((1,3,6,1,4,1,20044,61,2,1,3,0,9),_PmoabphcsAlmModGlobFail_Type())
pmoabphcsAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmModGlobFail.setStatus(_A)
_PmoabphcsAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoabphcsAlmUpEdfaInitNotCompl_Object=MibScalar
pmoabphcsAlmUpEdfaInitNotCompl=_PmoabphcsAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,61,2,1,3,0,10),_PmoabphcsAlmUpEdfaInitNotCompl_Type())
pmoabphcsAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoabphcsAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoabphcsAlmDwEdfaInitNotCompl_Object=MibScalar
pmoabphcsAlmDwEdfaInitNotCompl=_PmoabphcsAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,61,2,1,3,0,11),_PmoabphcsAlmDwEdfaInitNotCompl_Type())
pmoabphcsAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoabphcsAlmExtPump1NotLocked_Type=EkiOnOff
_PmoabphcsAlmExtPump1NotLocked_Object=MibScalar
pmoabphcsAlmExtPump1NotLocked=_PmoabphcsAlmExtPump1NotLocked_Object((1,3,6,1,4,1,20044,61,2,1,3,0,12),_PmoabphcsAlmExtPump1NotLocked_Type())
pmoabphcsAlmExtPump1NotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmExtPump1NotLocked.setStatus(_A)
_PmoabphcsAlmDefFuseA_Type=EkiOnOff
_PmoabphcsAlmDefFuseA_Object=MibScalar
pmoabphcsAlmDefFuseA=_PmoabphcsAlmDefFuseA_Object((1,3,6,1,4,1,20044,61,2,1,3,0,15),_PmoabphcsAlmDefFuseA_Type())
pmoabphcsAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmDefFuseA.setStatus(_A)
_PmoabphcsAlmDefFuseB_Type=EkiOnOff
_PmoabphcsAlmDefFuseB_Object=MibScalar
pmoabphcsAlmDefFuseB=_PmoabphcsAlmDefFuseB_Object((1,3,6,1,4,1,20044,61,2,1,3,0,16),_PmoabphcsAlmDefFuseB_Type())
pmoabphcsAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmDefFuseB.setStatus(_A)
_PmoabphcsAlmClient_ObjectIdentity=ObjectIdentity
pmoabphcsAlmClient=_PmoabphcsAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2))
_PmoabphcsAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoabphcsAlmClientNurg=_PmoabphcsAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,1))
_PmoabphcsAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoabphcsAlmclientEdfaWarnings=_PmoabphcsAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,1,33))
_PmoabphcsAlmClientGainLowWarning_Type=EkiOnOff
_PmoabphcsAlmClientGainLowWarning_Object=MibScalar
pmoabphcsAlmClientGainLowWarning=_PmoabphcsAlmClientGainLowWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,1),_PmoabphcsAlmClientGainLowWarning_Type())
pmoabphcsAlmClientGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientGainLowWarning.setStatus(_A)
_PmoabphcsAlmClientGainHighWarning_Type=EkiOnOff
_PmoabphcsAlmClientGainHighWarning_Object=MibScalar
pmoabphcsAlmClientGainHighWarning=_PmoabphcsAlmClientGainHighWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,2),_PmoabphcsAlmClientGainHighWarning_Type())
pmoabphcsAlmClientGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientGainHighWarning.setStatus(_A)
_PmoabphcsAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoabphcsAlmClientInputPwrLowWarning_Object=MibScalar
pmoabphcsAlmClientInputPwrLowWarning=_PmoabphcsAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,3),_PmoabphcsAlmClientInputPwrLowWarning_Type())
pmoabphcsAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientInputPwrLowWarning.setStatus(_A)
_PmoabphcsAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoabphcsAlmClientInputPwrHighWarning_Object=MibScalar
pmoabphcsAlmClientInputPwrHighWarning=_PmoabphcsAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,4),_PmoabphcsAlmClientInputPwrHighWarning_Type())
pmoabphcsAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientInputPwrHighWarning.setStatus(_A)
_PmoabphcsAlmClientOutputPwrLowWarning_Type=EkiOnOff
_PmoabphcsAlmClientOutputPwrLowWarning_Object=MibScalar
pmoabphcsAlmClientOutputPwrLowWarning=_PmoabphcsAlmClientOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,5),_PmoabphcsAlmClientOutputPwrLowWarning_Type())
pmoabphcsAlmClientOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientOutputPwrLowWarning.setStatus(_A)
_PmoabphcsAlmClientOutputPwrHighWarning_Type=EkiOnOff
_PmoabphcsAlmClientOutputPwrHighWarning_Object=MibScalar
pmoabphcsAlmClientOutputPwrHighWarning=_PmoabphcsAlmClientOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,6),_PmoabphcsAlmClientOutputPwrHighWarning_Type())
pmoabphcsAlmClientOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientOutputPwrHighWarning.setStatus(_A)
_PmoabphcsAlmClientBiasLowWarning_Type=EkiOnOff
_PmoabphcsAlmClientBiasLowWarning_Object=MibScalar
pmoabphcsAlmClientBiasLowWarning=_PmoabphcsAlmClientBiasLowWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,7),_PmoabphcsAlmClientBiasLowWarning_Type())
pmoabphcsAlmClientBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientBiasLowWarning.setStatus(_A)
_PmoabphcsAlmClientBiasHighWarning_Type=EkiOnOff
_PmoabphcsAlmClientBiasHighWarning_Object=MibScalar
pmoabphcsAlmClientBiasHighWarning=_PmoabphcsAlmClientBiasHighWarning_Object((1,3,6,1,4,1,20044,61,2,2,1,33,8),_PmoabphcsAlmClientBiasHighWarning_Type())
pmoabphcsAlmClientBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientBiasHighWarning.setStatus(_A)
_PmoabphcsAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoabphcsAlmClientUrg=_PmoabphcsAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,2))
_PmoabphcsAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoabphcsAlmclientEdfaAlarms1=_PmoabphcsAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,2,32))
_PmoabphcsAlmClientGainLowAlarm_Type=EkiOnOff
_PmoabphcsAlmClientGainLowAlarm_Object=MibScalar
pmoabphcsAlmClientGainLowAlarm=_PmoabphcsAlmClientGainLowAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,1),_PmoabphcsAlmClientGainLowAlarm_Type())
pmoabphcsAlmClientGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientGainLowAlarm.setStatus(_A)
_PmoabphcsAlmClientGainHighAlarm_Type=EkiOnOff
_PmoabphcsAlmClientGainHighAlarm_Object=MibScalar
pmoabphcsAlmClientGainHighAlarm=_PmoabphcsAlmClientGainHighAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,2),_PmoabphcsAlmClientGainHighAlarm_Type())
pmoabphcsAlmClientGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientGainHighAlarm.setStatus(_A)
_PmoabphcsAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoabphcsAlmClientInputPwrLowAlarm_Object=MibScalar
pmoabphcsAlmClientInputPwrLowAlarm=_PmoabphcsAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,3),_PmoabphcsAlmClientInputPwrLowAlarm_Type())
pmoabphcsAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoabphcsAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoabphcsAlmClientInputPwrHighAlarm_Object=MibScalar
pmoabphcsAlmClientInputPwrHighAlarm=_PmoabphcsAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,4),_PmoabphcsAlmClientInputPwrHighAlarm_Type())
pmoabphcsAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoabphcsAlmClientOutputPwrLowAlarm_Type=EkiOnOff
_PmoabphcsAlmClientOutputPwrLowAlarm_Object=MibScalar
pmoabphcsAlmClientOutputPwrLowAlarm=_PmoabphcsAlmClientOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,5),_PmoabphcsAlmClientOutputPwrLowAlarm_Type())
pmoabphcsAlmClientOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientOutputPwrLowAlarm.setStatus(_A)
_PmoabphcsAlmClientOutputPwrHighAlarm_Type=EkiOnOff
_PmoabphcsAlmClientOutputPwrHighAlarm_Object=MibScalar
pmoabphcsAlmClientOutputPwrHighAlarm=_PmoabphcsAlmClientOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,6),_PmoabphcsAlmClientOutputPwrHighAlarm_Type())
pmoabphcsAlmClientOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientOutputPwrHighAlarm.setStatus(_A)
_PmoabphcsAlmClientBiasLowAlarm_Type=EkiOnOff
_PmoabphcsAlmClientBiasLowAlarm_Object=MibScalar
pmoabphcsAlmClientBiasLowAlarm=_PmoabphcsAlmClientBiasLowAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,7),_PmoabphcsAlmClientBiasLowAlarm_Type())
pmoabphcsAlmClientBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientBiasLowAlarm.setStatus(_A)
_PmoabphcsAlmClientBiasHighAlarm_Type=EkiOnOff
_PmoabphcsAlmClientBiasHighAlarm_Object=MibScalar
pmoabphcsAlmClientBiasHighAlarm=_PmoabphcsAlmClientBiasHighAlarm_Object((1,3,6,1,4,1,20044,61,2,2,2,32,8),_PmoabphcsAlmClientBiasHighAlarm_Type())
pmoabphcsAlmClientBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientBiasHighAlarm.setStatus(_A)
_PmoabphcsAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoabphcsAlmClientCrit=_PmoabphcsAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,3))
_PmoabphcsAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoabphcsAlmsynthAlm8=_PmoabphcsAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,3,8))
_PmoabphcsAlmClientHwFail_Type=EkiOnOff
_PmoabphcsAlmClientHwFail_Object=MibScalar
pmoabphcsAlmClientHwFail=_PmoabphcsAlmClientHwFail_Object((1,3,6,1,4,1,20044,61,2,2,3,8,4),_PmoabphcsAlmClientHwFail_Type())
pmoabphcsAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientHwFail.setStatus(_A)
_PmoabphcsAlmClientTxOff_Type=EkiOnOff
_PmoabphcsAlmClientTxOff_Object=MibScalar
pmoabphcsAlmClientTxOff=_PmoabphcsAlmClientTxOff_Object((1,3,6,1,4,1,20044,61,2,2,3,8,5),_PmoabphcsAlmClientTxOff_Type())
pmoabphcsAlmClientTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientTxOff.setStatus(_A)
_PmoabphcsAlmClientFail_Type=EkiOnOff
_PmoabphcsAlmClientFail_Object=MibScalar
pmoabphcsAlmClientFail=_PmoabphcsAlmClientFail_Object((1,3,6,1,4,1,20044,61,2,2,3,8,12),_PmoabphcsAlmClientFail_Type())
pmoabphcsAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientFail.setStatus(_A)
_PmoabphcsAlmClientExtPumpFail_Type=EkiOnOff
_PmoabphcsAlmClientExtPumpFail_Object=MibScalar
pmoabphcsAlmClientExtPumpFail=_PmoabphcsAlmClientExtPumpFail_Object((1,3,6,1,4,1,20044,61,2,2,3,8,13),_PmoabphcsAlmClientExtPumpFail_Type())
pmoabphcsAlmClientExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientExtPumpFail.setStatus(_A)
_PmoabphcsAlmSupvbFail_Type=EkiOnOff
_PmoabphcsAlmSupvbFail_Object=MibScalar
pmoabphcsAlmSupvbFail=_PmoabphcsAlmSupvbFail_Object((1,3,6,1,4,1,20044,61,2,2,3,8,14),_PmoabphcsAlmSupvbFail_Type())
pmoabphcsAlmSupvbFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmSupvbFail.setStatus(_A)
_PmoabphcsAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoabphcsAlmclientEdfaAlarms2=_PmoabphcsAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,3,35))
_PmoabphcsAlmClientEdfaNr_Type=EkiOnOff
_PmoabphcsAlmClientEdfaNr_Object=MibScalar
pmoabphcsAlmClientEdfaNr=_PmoabphcsAlmClientEdfaNr_Object((1,3,6,1,4,1,20044,61,2,2,3,35,1),_PmoabphcsAlmClientEdfaNr_Type())
pmoabphcsAlmClientEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientEdfaNr.setStatus(_A)
_PmoabphcsAlmClientEdfaTecFail_Type=EkiOnOff
_PmoabphcsAlmClientEdfaTecFail_Object=MibScalar
pmoabphcsAlmClientEdfaTecFail=_PmoabphcsAlmClientEdfaTecFail_Object((1,3,6,1,4,1,20044,61,2,2,3,35,2),_PmoabphcsAlmClientEdfaTecFail_Type())
pmoabphcsAlmClientEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientEdfaTecFail.setStatus(_A)
_PmoabphcsAlmClientEdfaLaserFail_Type=EkiOnOff
_PmoabphcsAlmClientEdfaLaserFail_Object=MibScalar
pmoabphcsAlmClientEdfaLaserFail=_PmoabphcsAlmClientEdfaLaserFail_Object((1,3,6,1,4,1,20044,61,2,2,3,35,3),_PmoabphcsAlmClientEdfaLaserFail_Type())
pmoabphcsAlmClientEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientEdfaLaserFail.setStatus(_A)
_PmoabphcsAlmClientEdfaLos_Type=EkiOnOff
_PmoabphcsAlmClientEdfaLos_Object=MibScalar
pmoabphcsAlmClientEdfaLos=_PmoabphcsAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,61,2,2,3,35,4),_PmoabphcsAlmClientEdfaLos_Type())
pmoabphcsAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientEdfaLos.setStatus(_A)
_PmoabphcsAlmClientExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoabphcsAlmClientExtPumpEdfaLowCurrent_Object=MibScalar
pmoabphcsAlmClientExtPumpEdfaLowCurrent=_PmoabphcsAlmClientExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,61,2,2,3,35,5),_PmoabphcsAlmClientExtPumpEdfaLowCurrent_Type())
pmoabphcsAlmClientExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientExtPumpEdfaLowCurrent.setStatus(_A)
_PmoabphcsAlmClientGainOutOfRange_Type=EkiOnOff
_PmoabphcsAlmClientGainOutOfRange_Object=MibScalar
pmoabphcsAlmClientGainOutOfRange=_PmoabphcsAlmClientGainOutOfRange_Object((1,3,6,1,4,1,20044,61,2,2,3,35,6),_PmoabphcsAlmClientGainOutOfRange_Type())
pmoabphcsAlmClientGainOutOfRange.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientGainOutOfRange.setStatus(_A)
_PmoabphcsAlmclientMsaAlarms_ObjectIdentity=ObjectIdentity
pmoabphcsAlmclientMsaAlarms=_PmoabphcsAlmclientMsaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,61,2,2,3,37))
_PmoabphcsAlmClientMsaLos_Type=EkiOnOff
_PmoabphcsAlmClientMsaLos_Object=MibScalar
pmoabphcsAlmClientMsaLos=_PmoabphcsAlmClientMsaLos_Object((1,3,6,1,4,1,20044,61,2,2,3,37,1),_PmoabphcsAlmClientMsaLos_Type())
pmoabphcsAlmClientMsaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientMsaLos.setStatus(_A)
_PmoabphcsAlmClientMsaAttenuation_Type=EkiOnOff
_PmoabphcsAlmClientMsaAttenuation_Object=MibScalar
pmoabphcsAlmClientMsaAttenuation=_PmoabphcsAlmClientMsaAttenuation_Object((1,3,6,1,4,1,20044,61,2,2,3,37,2),_PmoabphcsAlmClientMsaAttenuation_Type())
pmoabphcsAlmClientMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmClientMsaAttenuation.setStatus(_A)
_PmoabphcsAlmLine_ObjectIdentity=ObjectIdentity
pmoabphcsAlmLine=_PmoabphcsAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3))
_PmoabphcsAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoabphcsAlmLineNurg=_PmoabphcsAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,1))
_PmoabphcsAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoabphcsAlmlineEdfaWarnings=_PmoabphcsAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,1,41))
_PmoabphcsAlmLineGainLowWarning_Type=EkiOnOff
_PmoabphcsAlmLineGainLowWarning_Object=MibScalar
pmoabphcsAlmLineGainLowWarning=_PmoabphcsAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,1),_PmoabphcsAlmLineGainLowWarning_Type())
pmoabphcsAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineGainLowWarning.setStatus(_A)
_PmoabphcsAlmLineGainHighWarning_Type=EkiOnOff
_PmoabphcsAlmLineGainHighWarning_Object=MibScalar
pmoabphcsAlmLineGainHighWarning=_PmoabphcsAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,2),_PmoabphcsAlmLineGainHighWarning_Type())
pmoabphcsAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineGainHighWarning.setStatus(_A)
_PmoabphcsAlmLineInputPwrLowWarning_Type=EkiOnOff
_PmoabphcsAlmLineInputPwrLowWarning_Object=MibScalar
pmoabphcsAlmLineInputPwrLowWarning=_PmoabphcsAlmLineInputPwrLowWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,3),_PmoabphcsAlmLineInputPwrLowWarning_Type())
pmoabphcsAlmLineInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineInputPwrLowWarning.setStatus(_A)
_PmoabphcsAlmLineInputPwrHighWarning_Type=EkiOnOff
_PmoabphcsAlmLineInputPwrHighWarning_Object=MibScalar
pmoabphcsAlmLineInputPwrHighWarning=_PmoabphcsAlmLineInputPwrHighWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,4),_PmoabphcsAlmLineInputPwrHighWarning_Type())
pmoabphcsAlmLineInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineInputPwrHighWarning.setStatus(_A)
_PmoabphcsAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoabphcsAlmLineOutputPwrLowWarning_Object=MibScalar
pmoabphcsAlmLineOutputPwrLowWarning=_PmoabphcsAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,5),_PmoabphcsAlmLineOutputPwrLowWarning_Type())
pmoabphcsAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoabphcsAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoabphcsAlmLineOutputPwrHighWarning_Object=MibScalar
pmoabphcsAlmLineOutputPwrHighWarning=_PmoabphcsAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,6),_PmoabphcsAlmLineOutputPwrHighWarning_Type())
pmoabphcsAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoabphcsAlmLineBiasLowWarning_Type=EkiOnOff
_PmoabphcsAlmLineBiasLowWarning_Object=MibScalar
pmoabphcsAlmLineBiasLowWarning=_PmoabphcsAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,7),_PmoabphcsAlmLineBiasLowWarning_Type())
pmoabphcsAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineBiasLowWarning.setStatus(_A)
_PmoabphcsAlmLineBiasHighWarning_Type=EkiOnOff
_PmoabphcsAlmLineBiasHighWarning_Object=MibScalar
pmoabphcsAlmLineBiasHighWarning=_PmoabphcsAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,61,2,3,1,41,8),_PmoabphcsAlmLineBiasHighWarning_Type())
pmoabphcsAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineBiasHighWarning.setStatus(_A)
_PmoabphcsAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoabphcsAlmLineUrg=_PmoabphcsAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,2))
_PmoabphcsAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoabphcsAlmlineEdfaAlarms1=_PmoabphcsAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,2,40))
_PmoabphcsAlmLineGainLowAlarm_Type=EkiOnOff
_PmoabphcsAlmLineGainLowAlarm_Object=MibScalar
pmoabphcsAlmLineGainLowAlarm=_PmoabphcsAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,1),_PmoabphcsAlmLineGainLowAlarm_Type())
pmoabphcsAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineGainLowAlarm.setStatus(_A)
_PmoabphcsAlmLineGainHighAlarm_Type=EkiOnOff
_PmoabphcsAlmLineGainHighAlarm_Object=MibScalar
pmoabphcsAlmLineGainHighAlarm=_PmoabphcsAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,2),_PmoabphcsAlmLineGainHighAlarm_Type())
pmoabphcsAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineGainHighAlarm.setStatus(_A)
_PmoabphcsAlmLineInputPwrLowAlarm_Type=EkiOnOff
_PmoabphcsAlmLineInputPwrLowAlarm_Object=MibScalar
pmoabphcsAlmLineInputPwrLowAlarm=_PmoabphcsAlmLineInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,3),_PmoabphcsAlmLineInputPwrLowAlarm_Type())
pmoabphcsAlmLineInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineInputPwrLowAlarm.setStatus(_A)
_PmoabphcsAlmLineInputPwrHighAlarm_Type=EkiOnOff
_PmoabphcsAlmLineInputPwrHighAlarm_Object=MibScalar
pmoabphcsAlmLineInputPwrHighAlarm=_PmoabphcsAlmLineInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,4),_PmoabphcsAlmLineInputPwrHighAlarm_Type())
pmoabphcsAlmLineInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineInputPwrHighAlarm.setStatus(_A)
_PmoabphcsAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoabphcsAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoabphcsAlmLineOutputPwrLowAlarm=_PmoabphcsAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,5),_PmoabphcsAlmLineOutputPwrLowAlarm_Type())
pmoabphcsAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoabphcsAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoabphcsAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoabphcsAlmLineOutputPwrHighAlarm=_PmoabphcsAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,6),_PmoabphcsAlmLineOutputPwrHighAlarm_Type())
pmoabphcsAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoabphcsAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoabphcsAlmLineBiasLowAlarm_Object=MibScalar
pmoabphcsAlmLineBiasLowAlarm=_PmoabphcsAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,7),_PmoabphcsAlmLineBiasLowAlarm_Type())
pmoabphcsAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineBiasLowAlarm.setStatus(_A)
_PmoabphcsAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoabphcsAlmLineBiasHighAlarm_Object=MibScalar
pmoabphcsAlmLineBiasHighAlarm=_PmoabphcsAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,61,2,3,2,40,8),_PmoabphcsAlmLineBiasHighAlarm_Type())
pmoabphcsAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineBiasHighAlarm.setStatus(_A)
_PmoabphcsAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoabphcsAlmLineCrit=_PmoabphcsAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,3))
_PmoabphcsAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoabphcsAlmsynthAlm7=_PmoabphcsAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,3,7))
_PmoabphcsAlmLineHwFail_Type=EkiOnOff
_PmoabphcsAlmLineHwFail_Object=MibScalar
pmoabphcsAlmLineHwFail=_PmoabphcsAlmLineHwFail_Object((1,3,6,1,4,1,20044,61,2,3,3,7,4),_PmoabphcsAlmLineHwFail_Type())
pmoabphcsAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineHwFail.setStatus(_A)
_PmoabphcsAlmLineTxOff_Type=EkiOnOff
_PmoabphcsAlmLineTxOff_Object=MibScalar
pmoabphcsAlmLineTxOff=_PmoabphcsAlmLineTxOff_Object((1,3,6,1,4,1,20044,61,2,3,3,7,5),_PmoabphcsAlmLineTxOff_Type())
pmoabphcsAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxOff.setStatus(_A)
_PmoabphcsAlmLineFail_Type=EkiOnOff
_PmoabphcsAlmLineFail_Object=MibScalar
pmoabphcsAlmLineFail=_PmoabphcsAlmLineFail_Object((1,3,6,1,4,1,20044,61,2,3,3,7,12),_PmoabphcsAlmLineFail_Type())
pmoabphcsAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineFail.setStatus(_A)
_PmoabphcsAlmLineExtPumpFail_Type=EkiOnOff
_PmoabphcsAlmLineExtPumpFail_Object=MibScalar
pmoabphcsAlmLineExtPumpFail=_PmoabphcsAlmLineExtPumpFail_Object((1,3,6,1,4,1,20044,61,2,3,3,7,13),_PmoabphcsAlmLineExtPumpFail_Type())
pmoabphcsAlmLineExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineExtPumpFail.setStatus(_A)
_PmoabphcsAlmSupvaFail_Type=EkiOnOff
_PmoabphcsAlmSupvaFail_Object=MibScalar
pmoabphcsAlmSupvaFail=_PmoabphcsAlmSupvaFail_Object((1,3,6,1,4,1,20044,61,2,3,3,7,14),_PmoabphcsAlmSupvaFail_Type())
pmoabphcsAlmSupvaFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmSupvaFail.setStatus(_A)
_PmoabphcsAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoabphcsAlmlineEdfaAlarms2=_PmoabphcsAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,3,43))
_PmoabphcsAlmLineEdfaNr_Type=EkiOnOff
_PmoabphcsAlmLineEdfaNr_Object=MibScalar
pmoabphcsAlmLineEdfaNr=_PmoabphcsAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,61,2,3,3,43,1),_PmoabphcsAlmLineEdfaNr_Type())
pmoabphcsAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineEdfaNr.setStatus(_A)
_PmoabphcsAlmLineEdfaTecFail_Type=EkiOnOff
_PmoabphcsAlmLineEdfaTecFail_Object=MibScalar
pmoabphcsAlmLineEdfaTecFail=_PmoabphcsAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,61,2,3,3,43,2),_PmoabphcsAlmLineEdfaTecFail_Type())
pmoabphcsAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineEdfaTecFail.setStatus(_A)
_PmoabphcsAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoabphcsAlmLineEdfaLaserFail_Object=MibScalar
pmoabphcsAlmLineEdfaLaserFail=_PmoabphcsAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,61,2,3,3,43,3),_PmoabphcsAlmLineEdfaLaserFail_Type())
pmoabphcsAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineEdfaLaserFail.setStatus(_A)
_PmoabphcsAlmLineEdfaLos_Type=EkiOnOff
_PmoabphcsAlmLineEdfaLos_Object=MibScalar
pmoabphcsAlmLineEdfaLos=_PmoabphcsAlmLineEdfaLos_Object((1,3,6,1,4,1,20044,61,2,3,3,43,4),_PmoabphcsAlmLineEdfaLos_Type())
pmoabphcsAlmLineEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineEdfaLos.setStatus(_A)
_PmoabphcsAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoabphcsAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoabphcsAlmLineExtPumpEdfaLowCurrent=_PmoabphcsAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,61,2,3,3,43,5),_PmoabphcsAlmLineExtPumpEdfaLowCurrent_Type())
pmoabphcsAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_PmoabphcsAlmLineGainOutOfRange_Type=EkiOnOff
_PmoabphcsAlmLineGainOutOfRange_Object=MibScalar
pmoabphcsAlmLineGainOutOfRange=_PmoabphcsAlmLineGainOutOfRange_Object((1,3,6,1,4,1,20044,61,2,3,3,43,6),_PmoabphcsAlmLineGainOutOfRange_Type())
pmoabphcsAlmLineGainOutOfRange.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineGainOutOfRange.setStatus(_A)
_PmoabphcsAlmlineMsaAlarms_ObjectIdentity=ObjectIdentity
pmoabphcsAlmlineMsaAlarms=_PmoabphcsAlmlineMsaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,61,2,3,3,45))
_PmoabphcsAlmLineMsaLos_Type=EkiOnOff
_PmoabphcsAlmLineMsaLos_Object=MibScalar
pmoabphcsAlmLineMsaLos=_PmoabphcsAlmLineMsaLos_Object((1,3,6,1,4,1,20044,61,2,3,3,45,1),_PmoabphcsAlmLineMsaLos_Type())
pmoabphcsAlmLineMsaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineMsaLos.setStatus(_A)
_PmoabphcsAlmLineMsaAttenuation_Type=EkiOnOff
_PmoabphcsAlmLineMsaAttenuation_Object=MibScalar
pmoabphcsAlmLineMsaAttenuation=_PmoabphcsAlmLineMsaAttenuation_Object((1,3,6,1,4,1,20044,61,2,3,3,45,2),_PmoabphcsAlmLineMsaAttenuation_Type())
pmoabphcsAlmLineMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineMsaAttenuation.setStatus(_A)
_PmoabphcsAlmlineOscAlarmsTable_Object=MibTable
pmoabphcsAlmlineOscAlarmsTable=_PmoabphcsAlmlineOscAlarmsTable_Object((1,3,6,1,4,1,20044,61,2,3,3,48))
if mibBuilder.loadTexts:pmoabphcsAlmlineOscAlarmsTable.setStatus(_A)
_PmoabphcsAlmlineOscAlarmsEntry_Object=MibTableRow
pmoabphcsAlmlineOscAlarmsEntry=_PmoabphcsAlmlineOscAlarmsEntry_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1))
pmoabphcsAlmlineOscAlarmsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:pmoabphcsAlmlineOscAlarmsEntry.setStatus(_A)
class _PmoabphcsAlmlineOscAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsAlmlineOscAlarmsIndex_Type.__name__=_D
_PmoabphcsAlmlineOscAlarmsIndex_Object=MibTableColumn
pmoabphcsAlmlineOscAlarmsIndex=_PmoabphcsAlmlineOscAlarmsIndex_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,1),_PmoabphcsAlmlineOscAlarmsIndex_Type())
pmoabphcsAlmlineOscAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmlineOscAlarmsIndex.setStatus(_A)
_PmoabphcsAlmLineLosPortn_Type=EkiOnOff
_PmoabphcsAlmLineLosPortn_Object=MibTableColumn
pmoabphcsAlmLineLosPortn=_PmoabphcsAlmLineLosPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,2),_PmoabphcsAlmLineLosPortn_Type())
pmoabphcsAlmLineLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineLosPortn.setStatus(_A)
_PmoabphcsAlmLineTxOffPortn_Type=EkiOnOff
_PmoabphcsAlmLineTxOffPortn_Object=MibTableColumn
pmoabphcsAlmLineTxOffPortn=_PmoabphcsAlmLineTxOffPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,3),_PmoabphcsAlmLineTxOffPortn_Type())
pmoabphcsAlmLineTxOffPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxOffPortn.setStatus(_A)
_PmoabphcsAlmLineTxFailPortn_Type=EkiOnOff
_PmoabphcsAlmLineTxFailPortn_Object=MibTableColumn
pmoabphcsAlmLineTxFailPortn=_PmoabphcsAlmLineTxFailPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,4),_PmoabphcsAlmLineTxFailPortn_Type())
pmoabphcsAlmLineTxFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxFailPortn.setStatus(_A)
_PmoabphcsAlmLineFecFailPortn_Type=EkiOnOff
_PmoabphcsAlmLineFecFailPortn_Object=MibTableColumn
pmoabphcsAlmLineFecFailPortn=_PmoabphcsAlmLineFecFailPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,5),_PmoabphcsAlmLineFecFailPortn_Type())
pmoabphcsAlmLineFecFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineFecFailPortn.setStatus(_A)
_PmoabphcsAlmLineOosPortn_Type=EkiOnOff
_PmoabphcsAlmLineOosPortn_Object=MibTableColumn
pmoabphcsAlmLineOosPortn=_PmoabphcsAlmLineOosPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,6),_PmoabphcsAlmLineOosPortn_Type())
pmoabphcsAlmLineOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOosPortn.setStatus(_A)
_PmoabphcsAlmLineLofPortn_Type=EkiOnOff
_PmoabphcsAlmLineLofPortn_Object=MibTableColumn
pmoabphcsAlmLineLofPortn=_PmoabphcsAlmLineLofPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,7),_PmoabphcsAlmLineLofPortn_Type())
pmoabphcsAlmLineLofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineLofPortn.setStatus(_A)
_PmoabphcsAlmLineOofPortn_Type=EkiOnOff
_PmoabphcsAlmLineOofPortn_Object=MibTableColumn
pmoabphcsAlmLineOofPortn=_PmoabphcsAlmLineOofPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,8),_PmoabphcsAlmLineOofPortn_Type())
pmoabphcsAlmLineOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOofPortn.setStatus(_A)
_PmoabphcsAlmLineRemoteTxFailPortn_Type=EkiOnOff
_PmoabphcsAlmLineRemoteTxFailPortn_Object=MibTableColumn
pmoabphcsAlmLineRemoteTxFailPortn=_PmoabphcsAlmLineRemoteTxFailPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,9),_PmoabphcsAlmLineRemoteTxFailPortn_Type())
pmoabphcsAlmLineRemoteTxFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineRemoteTxFailPortn.setStatus(_A)
_PmoabphcsAlmLineWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineWarningPortn=_PmoabphcsAlmLineWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,10),_PmoabphcsAlmLineWarningPortn_Type())
pmoabphcsAlmLineWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineWarningPortn.setStatus(_A)
_PmoabphcsAlmLineAlmPortn_Type=EkiOnOff
_PmoabphcsAlmLineAlmPortn_Object=MibTableColumn
pmoabphcsAlmLineAlmPortn=_PmoabphcsAlmLineAlmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,48,1,11),_PmoabphcsAlmLineAlmPortn_Type())
pmoabphcsAlmLineAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineAlmPortn.setStatus(_A)
_PmoabphcsAlmlineOscThresholdAlarmsTable_Object=MibTable
pmoabphcsAlmlineOscThresholdAlarmsTable=_PmoabphcsAlmlineOscThresholdAlarmsTable_Object((1,3,6,1,4,1,20044,61,2,3,3,49))
if mibBuilder.loadTexts:pmoabphcsAlmlineOscThresholdAlarmsTable.setStatus(_A)
_PmoabphcsAlmlineOscThresholdAlarmsEntry_Object=MibTableRow
pmoabphcsAlmlineOscThresholdAlarmsEntry=_PmoabphcsAlmlineOscThresholdAlarmsEntry_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1))
pmoabphcsAlmlineOscThresholdAlarmsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:pmoabphcsAlmlineOscThresholdAlarmsEntry.setStatus(_A)
class _PmoabphcsAlmlineOscThresholdAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsAlmlineOscThresholdAlarmsIndex_Type.__name__=_D
_PmoabphcsAlmlineOscThresholdAlarmsIndex_Object=MibTableColumn
pmoabphcsAlmlineOscThresholdAlarmsIndex=_PmoabphcsAlmlineOscThresholdAlarmsIndex_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,1),_PmoabphcsAlmlineOscThresholdAlarmsIndex_Type())
pmoabphcsAlmlineOscThresholdAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmlineOscThresholdAlarmsIndex.setStatus(_A)
_PmoabphcsAlmLineTxPwrLowAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineTxPwrLowAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineTxPwrLowAlarmPortn=_PmoabphcsAlmLineTxPwrLowAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,2),_PmoabphcsAlmLineTxPwrLowAlarmPortn_Type())
pmoabphcsAlmLineTxPwrLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxPwrLowAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineTxPwrHighAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineTxPwrHighAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineTxPwrHighAlarmPortn=_PmoabphcsAlmLineTxPwrHighAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,3),_PmoabphcsAlmLineTxPwrHighAlarmPortn_Type())
pmoabphcsAlmLineTxPwrHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxPwrHighAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineRxPwrLowAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineRxPwrLowAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineRxPwrLowAlarmPortn=_PmoabphcsAlmLineRxPwrLowAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,4),_PmoabphcsAlmLineRxPwrLowAlarmPortn_Type())
pmoabphcsAlmLineRxPwrLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineRxPwrLowAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineRxPwrHighAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineRxPwrHighAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineRxPwrHighAlarmPortn=_PmoabphcsAlmLineRxPwrHighAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,5),_PmoabphcsAlmLineRxPwrHighAlarmPortn_Type())
pmoabphcsAlmLineRxPwrHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineRxPwrHighAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineSpanlossLowAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineSpanlossLowAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineSpanlossLowAlarmPortn=_PmoabphcsAlmLineSpanlossLowAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,6),_PmoabphcsAlmLineSpanlossLowAlarmPortn_Type())
pmoabphcsAlmLineSpanlossLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineSpanlossLowAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineSpanlossHighAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineSpanlossHighAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineSpanlossHighAlarmPortn=_PmoabphcsAlmLineSpanlossHighAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,7),_PmoabphcsAlmLineSpanlossHighAlarmPortn_Type())
pmoabphcsAlmLineSpanlossHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineSpanlossHighAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineOscBiasLowAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineOscBiasLowAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineOscBiasLowAlarmPortn=_PmoabphcsAlmLineOscBiasLowAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,8),_PmoabphcsAlmLineOscBiasLowAlarmPortn_Type())
pmoabphcsAlmLineOscBiasLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOscBiasLowAlarmPortn.setStatus(_A)
_PmoabphcsAlmLineOscBiasHighAlarmPortn_Type=EkiOnOff
_PmoabphcsAlmLineOscBiasHighAlarmPortn_Object=MibTableColumn
pmoabphcsAlmLineOscBiasHighAlarmPortn=_PmoabphcsAlmLineOscBiasHighAlarmPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,49,1,9),_PmoabphcsAlmLineOscBiasHighAlarmPortn_Type())
pmoabphcsAlmLineOscBiasHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOscBiasHighAlarmPortn.setStatus(_A)
_PmoabphcsAlmlineOscThresholdsWarningsTable_Object=MibTable
pmoabphcsAlmlineOscThresholdsWarningsTable=_PmoabphcsAlmlineOscThresholdsWarningsTable_Object((1,3,6,1,4,1,20044,61,2,3,3,50))
if mibBuilder.loadTexts:pmoabphcsAlmlineOscThresholdsWarningsTable.setStatus(_A)
_PmoabphcsAlmlineOscThresholdsWarningsEntry_Object=MibTableRow
pmoabphcsAlmlineOscThresholdsWarningsEntry=_PmoabphcsAlmlineOscThresholdsWarningsEntry_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1))
pmoabphcsAlmlineOscThresholdsWarningsEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:pmoabphcsAlmlineOscThresholdsWarningsEntry.setStatus(_A)
class _PmoabphcsAlmlineOscThresholdsWarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsAlmlineOscThresholdsWarningsIndex_Type.__name__=_D
_PmoabphcsAlmlineOscThresholdsWarningsIndex_Object=MibTableColumn
pmoabphcsAlmlineOscThresholdsWarningsIndex=_PmoabphcsAlmlineOscThresholdsWarningsIndex_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,1),_PmoabphcsAlmlineOscThresholdsWarningsIndex_Type())
pmoabphcsAlmlineOscThresholdsWarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmlineOscThresholdsWarningsIndex.setStatus(_A)
_PmoabphcsAlmLineTxPwrLowWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineTxPwrLowWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineTxPwrLowWarningPortn=_PmoabphcsAlmLineTxPwrLowWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,2),_PmoabphcsAlmLineTxPwrLowWarningPortn_Type())
pmoabphcsAlmLineTxPwrLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxPwrLowWarningPortn.setStatus(_A)
_PmoabphcsAlmLineTxPwrHighWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineTxPwrHighWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineTxPwrHighWarningPortn=_PmoabphcsAlmLineTxPwrHighWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,3),_PmoabphcsAlmLineTxPwrHighWarningPortn_Type())
pmoabphcsAlmLineTxPwrHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineTxPwrHighWarningPortn.setStatus(_A)
_PmoabphcsAlmLineRxPwrLowWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineRxPwrLowWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineRxPwrLowWarningPortn=_PmoabphcsAlmLineRxPwrLowWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,4),_PmoabphcsAlmLineRxPwrLowWarningPortn_Type())
pmoabphcsAlmLineRxPwrLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineRxPwrLowWarningPortn.setStatus(_A)
_PmoabphcsAlmLineRxPwrHighWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineRxPwrHighWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineRxPwrHighWarningPortn=_PmoabphcsAlmLineRxPwrHighWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,5),_PmoabphcsAlmLineRxPwrHighWarningPortn_Type())
pmoabphcsAlmLineRxPwrHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineRxPwrHighWarningPortn.setStatus(_A)
_PmoabphcsAlmLineSpanlossLowWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineSpanlossLowWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineSpanlossLowWarningPortn=_PmoabphcsAlmLineSpanlossLowWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,6),_PmoabphcsAlmLineSpanlossLowWarningPortn_Type())
pmoabphcsAlmLineSpanlossLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineSpanlossLowWarningPortn.setStatus(_A)
_PmoabphcsAlmLineSpanlossHighWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineSpanlossHighWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineSpanlossHighWarningPortn=_PmoabphcsAlmLineSpanlossHighWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,7),_PmoabphcsAlmLineSpanlossHighWarningPortn_Type())
pmoabphcsAlmLineSpanlossHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineSpanlossHighWarningPortn.setStatus(_A)
_PmoabphcsAlmLineOscBiasLowWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineOscBiasLowWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineOscBiasLowWarningPortn=_PmoabphcsAlmLineOscBiasLowWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,8),_PmoabphcsAlmLineOscBiasLowWarningPortn_Type())
pmoabphcsAlmLineOscBiasLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOscBiasLowWarningPortn.setStatus(_A)
_PmoabphcsAlmLineOscBiasHighWarningPortn_Type=EkiOnOff
_PmoabphcsAlmLineOscBiasHighWarningPortn_Object=MibTableColumn
pmoabphcsAlmLineOscBiasHighWarningPortn=_PmoabphcsAlmLineOscBiasHighWarningPortn_Object((1,3,6,1,4,1,20044,61,2,3,3,50,1,9),_PmoabphcsAlmLineOscBiasHighWarningPortn_Type())
pmoabphcsAlmLineOscBiasHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsAlmLineOscBiasHighWarningPortn.setStatus(_A)
_Pmoabphcsmeasures_ObjectIdentity=ObjectIdentity
pmoabphcsmeasures=_Pmoabphcsmeasures_ObjectIdentity((1,3,6,1,4,1,20044,61,3))
_PmoabphcsMesrOther_ObjectIdentity=ObjectIdentity
pmoabphcsMesrOther=_PmoabphcsMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,61,3,1))
class _PmoabphcsMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrtempMeas_Type.__name__=_D
_PmoabphcsMesrtempMeas_Object=MibScalar
pmoabphcsMesrtempMeas=_PmoabphcsMesrtempMeas_Object((1,3,6,1,4,1,20044,61,3,1,80),_PmoabphcsMesrtempMeas_Type())
pmoabphcsMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrtempMeas.setStatus(_A)
_PmoabphcsMesrClient_ObjectIdentity=ObjectIdentity
pmoabphcsMesrClient=_PmoabphcsMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,61,3,2))
class _PmoabphcsMesrclientEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientEdfaBiasMeas_Type.__name__=_D
_PmoabphcsMesrclientEdfaBiasMeas_Object=MibScalar
pmoabphcsMesrclientEdfaBiasMeas=_PmoabphcsMesrclientEdfaBiasMeas_Object((1,3,6,1,4,1,20044,61,3,2,32),_PmoabphcsMesrclientEdfaBiasMeas_Type())
pmoabphcsMesrclientEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientEdfaBiasMeas.setStatus(_A)
class _PmoabphcsMesrclientEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientEdfaTxpwrMeas_Type.__name__=_D
_PmoabphcsMesrclientEdfaTxpwrMeas_Object=MibScalar
pmoabphcsMesrclientEdfaTxpwrMeas=_PmoabphcsMesrclientEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,61,3,2,33),_PmoabphcsMesrclientEdfaTxpwrMeas_Type())
pmoabphcsMesrclientEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientEdfaTxpwrMeas.setStatus(_A)
class _PmoabphcsMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientEdfaRxpwrMeas_Type.__name__=_D
_PmoabphcsMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoabphcsMesrclientEdfaRxpwrMeas=_PmoabphcsMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,61,3,2,34),_PmoabphcsMesrclientEdfaRxpwrMeas_Type())
pmoabphcsMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientEdfaRxpwrMeas.setStatus(_A)
class _PmoabphcsMesrclientEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientEdfaGainMeas_Type.__name__=_D
_PmoabphcsMesrclientEdfaGainMeas_Object=MibScalar
pmoabphcsMesrclientEdfaGainMeas=_PmoabphcsMesrclientEdfaGainMeas_Object((1,3,6,1,4,1,20044,61,3,2,35),_PmoabphcsMesrclientEdfaGainMeas_Type())
pmoabphcsMesrclientEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientEdfaGainMeas.setStatus(_A)
class _PmoabphcsMesrclientOscSpanLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientOscSpanLoss_Type.__name__=_D
_PmoabphcsMesrclientOscSpanLoss_Object=MibScalar
pmoabphcsMesrclientOscSpanLoss=_PmoabphcsMesrclientOscSpanLoss_Object((1,3,6,1,4,1,20044,61,3,2,36),_PmoabphcsMesrclientOscSpanLoss_Type())
pmoabphcsMesrclientOscSpanLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientOscSpanLoss.setStatus(_A)
class _PmoabphcsMesrclientOscSpanLossRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientOscSpanLossRef_Type.__name__=_D
_PmoabphcsMesrclientOscSpanLossRef_Object=MibScalar
pmoabphcsMesrclientOscSpanLossRef=_PmoabphcsMesrclientOscSpanLossRef_Object((1,3,6,1,4,1,20044,61,3,2,37),_PmoabphcsMesrclientOscSpanLossRef_Type())
pmoabphcsMesrclientOscSpanLossRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientOscSpanLossRef.setStatus(_A)
class _PmoabphcsMesrclientCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientCorrectedGain_Type.__name__=_D
_PmoabphcsMesrclientCorrectedGain_Object=MibScalar
pmoabphcsMesrclientCorrectedGain=_PmoabphcsMesrclientCorrectedGain_Object((1,3,6,1,4,1,20044,61,3,2,38),_PmoabphcsMesrclientCorrectedGain_Type())
pmoabphcsMesrclientCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientCorrectedGain.setStatus(_A)
class _PmoabphcsMesrclientMsaInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientMsaInputPower_Type.__name__=_D
_PmoabphcsMesrclientMsaInputPower_Object=MibScalar
pmoabphcsMesrclientMsaInputPower=_PmoabphcsMesrclientMsaInputPower_Object((1,3,6,1,4,1,20044,61,3,2,39),_PmoabphcsMesrclientMsaInputPower_Type())
pmoabphcsMesrclientMsaInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientMsaInputPower.setStatus(_A)
class _PmoabphcsMesrclientMsaOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientMsaOutputPower_Type.__name__=_D
_PmoabphcsMesrclientMsaOutputPower_Object=MibScalar
pmoabphcsMesrclientMsaOutputPower=_PmoabphcsMesrclientMsaOutputPower_Object((1,3,6,1,4,1,20044,61,3,2,40),_PmoabphcsMesrclientMsaOutputPower_Type())
pmoabphcsMesrclientMsaOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientMsaOutputPower.setStatus(_A)
class _PmoabphcsMesrclientMsaAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientMsaAttenuation_Type.__name__=_D
_PmoabphcsMesrclientMsaAttenuation_Object=MibScalar
pmoabphcsMesrclientMsaAttenuation=_PmoabphcsMesrclientMsaAttenuation_Object((1,3,6,1,4,1,20044,61,3,2,41),_PmoabphcsMesrclientMsaAttenuation_Type())
pmoabphcsMesrclientMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientMsaAttenuation.setStatus(_A)
class _PmoabphcsMesrclientMsaAttenuationRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrclientMsaAttenuationRef_Type.__name__=_D
_PmoabphcsMesrclientMsaAttenuationRef_Object=MibScalar
pmoabphcsMesrclientMsaAttenuationRef=_PmoabphcsMesrclientMsaAttenuationRef_Object((1,3,6,1,4,1,20044,61,3,2,42),_PmoabphcsMesrclientMsaAttenuationRef_Type())
pmoabphcsMesrclientMsaAttenuationRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrclientMsaAttenuationRef.setStatus(_A)
_PmoabphcsMesrLine_ObjectIdentity=ObjectIdentity
pmoabphcsMesrLine=_PmoabphcsMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,61,3,3))
class _PmoabphcsMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineEdfaBiasMeas_Type.__name__=_D
_PmoabphcsMesrlineEdfaBiasMeas_Object=MibScalar
pmoabphcsMesrlineEdfaBiasMeas=_PmoabphcsMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,61,3,3,48),_PmoabphcsMesrlineEdfaBiasMeas_Type())
pmoabphcsMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoabphcsMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineEdfaTxpwrMeas_Type.__name__=_D
_PmoabphcsMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoabphcsMesrlineEdfaTxpwrMeas=_PmoabphcsMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,61,3,3,49),_PmoabphcsMesrlineEdfaTxpwrMeas_Type())
pmoabphcsMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoabphcsMesrlineEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineEdfaRxpwrMeas_Type.__name__=_D
_PmoabphcsMesrlineEdfaRxpwrMeas_Object=MibScalar
pmoabphcsMesrlineEdfaRxpwrMeas=_PmoabphcsMesrlineEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,61,3,3,50),_PmoabphcsMesrlineEdfaRxpwrMeas_Type())
pmoabphcsMesrlineEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineEdfaRxpwrMeas.setStatus(_A)
class _PmoabphcsMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineEdfaGainMeas_Type.__name__=_D
_PmoabphcsMesrlineEdfaGainMeas_Object=MibScalar
pmoabphcsMesrlineEdfaGainMeas=_PmoabphcsMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,61,3,3,51),_PmoabphcsMesrlineEdfaGainMeas_Type())
pmoabphcsMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineEdfaGainMeas.setStatus(_A)
class _PmoabphcsMesrlineOscSpanLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineOscSpanLoss_Type.__name__=_D
_PmoabphcsMesrlineOscSpanLoss_Object=MibScalar
pmoabphcsMesrlineOscSpanLoss=_PmoabphcsMesrlineOscSpanLoss_Object((1,3,6,1,4,1,20044,61,3,3,52),_PmoabphcsMesrlineOscSpanLoss_Type())
pmoabphcsMesrlineOscSpanLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineOscSpanLoss.setStatus(_A)
class _PmoabphcsMesrlineOscSpanLossRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineOscSpanLossRef_Type.__name__=_D
_PmoabphcsMesrlineOscSpanLossRef_Object=MibScalar
pmoabphcsMesrlineOscSpanLossRef=_PmoabphcsMesrlineOscSpanLossRef_Object((1,3,6,1,4,1,20044,61,3,3,53),_PmoabphcsMesrlineOscSpanLossRef_Type())
pmoabphcsMesrlineOscSpanLossRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineOscSpanLossRef.setStatus(_A)
class _PmoabphcsMesrlineCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineCorrectedGain_Type.__name__=_D
_PmoabphcsMesrlineCorrectedGain_Object=MibScalar
pmoabphcsMesrlineCorrectedGain=_PmoabphcsMesrlineCorrectedGain_Object((1,3,6,1,4,1,20044,61,3,3,54),_PmoabphcsMesrlineCorrectedGain_Type())
pmoabphcsMesrlineCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineCorrectedGain.setStatus(_A)
class _PmoabphcsMesrlineMsaInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineMsaInputPower_Type.__name__=_D
_PmoabphcsMesrlineMsaInputPower_Object=MibScalar
pmoabphcsMesrlineMsaInputPower=_PmoabphcsMesrlineMsaInputPower_Object((1,3,6,1,4,1,20044,61,3,3,55),_PmoabphcsMesrlineMsaInputPower_Type())
pmoabphcsMesrlineMsaInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineMsaInputPower.setStatus(_A)
class _PmoabphcsMesrlineMsaOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineMsaOutputPower_Type.__name__=_D
_PmoabphcsMesrlineMsaOutputPower_Object=MibScalar
pmoabphcsMesrlineMsaOutputPower=_PmoabphcsMesrlineMsaOutputPower_Object((1,3,6,1,4,1,20044,61,3,3,56),_PmoabphcsMesrlineMsaOutputPower_Type())
pmoabphcsMesrlineMsaOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineMsaOutputPower.setStatus(_A)
class _PmoabphcsMesrlineMsaAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineMsaAttenuation_Type.__name__=_D
_PmoabphcsMesrlineMsaAttenuation_Object=MibScalar
pmoabphcsMesrlineMsaAttenuation=_PmoabphcsMesrlineMsaAttenuation_Object((1,3,6,1,4,1,20044,61,3,3,57),_PmoabphcsMesrlineMsaAttenuation_Type())
pmoabphcsMesrlineMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineMsaAttenuation.setStatus(_A)
class _PmoabphcsMesrlineMsaAttenuationRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineMsaAttenuationRef_Type.__name__=_D
_PmoabphcsMesrlineMsaAttenuationRef_Object=MibScalar
pmoabphcsMesrlineMsaAttenuationRef=_PmoabphcsMesrlineMsaAttenuationRef_Object((1,3,6,1,4,1,20044,61,3,3,58),_PmoabphcsMesrlineMsaAttenuationRef_Type())
pmoabphcsMesrlineMsaAttenuationRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineMsaAttenuationRef.setStatus(_A)
_PmoabphcsMesrlineOscTxPowerTable_Object=MibTable
pmoabphcsMesrlineOscTxPowerTable=_PmoabphcsMesrlineOscTxPowerTable_Object((1,3,6,1,4,1,20044,61,3,3,64))
if mibBuilder.loadTexts:pmoabphcsMesrlineOscTxPowerTable.setStatus(_A)
_PmoabphcsMesrlineOscTxPowerEntry_Object=MibTableRow
pmoabphcsMesrlineOscTxPowerEntry=_PmoabphcsMesrlineOscTxPowerEntry_Object((1,3,6,1,4,1,20044,61,3,3,64,1))
pmoabphcsMesrlineOscTxPowerEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:pmoabphcsMesrlineOscTxPowerEntry.setStatus(_A)
class _PmoabphcsMesrlineOscTxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsMesrlineOscTxPowerIndex_Type.__name__=_D
_PmoabphcsMesrlineOscTxPowerIndex_Object=MibTableColumn
pmoabphcsMesrlineOscTxPowerIndex=_PmoabphcsMesrlineOscTxPowerIndex_Object((1,3,6,1,4,1,20044,61,3,3,64,1,1),_PmoabphcsMesrlineOscTxPowerIndex_Type())
pmoabphcsMesrlineOscTxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineOscTxPowerIndex.setStatus(_A)
class _PmoabphcsMesrlineOscTxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineOscTxPowerPortn_Type.__name__=_D
_PmoabphcsMesrlineOscTxPowerPortn_Object=MibTableColumn
pmoabphcsMesrlineOscTxPowerPortn=_PmoabphcsMesrlineOscTxPowerPortn_Object((1,3,6,1,4,1,20044,61,3,3,64,1,2),_PmoabphcsMesrlineOscTxPowerPortn_Type())
pmoabphcsMesrlineOscTxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineOscTxPowerPortn.setStatus(_A)
_PmoabphcsMesrlineOscRxPowerTable_Object=MibTable
pmoabphcsMesrlineOscRxPowerTable=_PmoabphcsMesrlineOscRxPowerTable_Object((1,3,6,1,4,1,20044,61,3,3,65))
if mibBuilder.loadTexts:pmoabphcsMesrlineOscRxPowerTable.setStatus(_A)
_PmoabphcsMesrlineOscRxPowerEntry_Object=MibTableRow
pmoabphcsMesrlineOscRxPowerEntry=_PmoabphcsMesrlineOscRxPowerEntry_Object((1,3,6,1,4,1,20044,61,3,3,65,1))
pmoabphcsMesrlineOscRxPowerEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:pmoabphcsMesrlineOscRxPowerEntry.setStatus(_A)
class _PmoabphcsMesrlineOscRxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsMesrlineOscRxPowerIndex_Type.__name__=_D
_PmoabphcsMesrlineOscRxPowerIndex_Object=MibTableColumn
pmoabphcsMesrlineOscRxPowerIndex=_PmoabphcsMesrlineOscRxPowerIndex_Object((1,3,6,1,4,1,20044,61,3,3,65,1,1),_PmoabphcsMesrlineOscRxPowerIndex_Type())
pmoabphcsMesrlineOscRxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineOscRxPowerIndex.setStatus(_A)
class _PmoabphcsMesrlineOscRxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsMesrlineOscRxPowerPortn_Type.__name__=_D
_PmoabphcsMesrlineOscRxPowerPortn_Object=MibTableColumn
pmoabphcsMesrlineOscRxPowerPortn=_PmoabphcsMesrlineOscRxPowerPortn_Object((1,3,6,1,4,1,20044,61,3,3,65,1,2),_PmoabphcsMesrlineOscRxPowerPortn_Type())
pmoabphcsMesrlineOscRxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsMesrlineOscRxPowerPortn.setStatus(_A)
_Pmoabphcscounters_ObjectIdentity=ObjectIdentity
pmoabphcscounters=_Pmoabphcscounters_ObjectIdentity((1,3,6,1,4,1,20044,61,4))
_PmoabphcsCntOther_ObjectIdentity=ObjectIdentity
pmoabphcsCntOther=_PmoabphcsCntOther_ObjectIdentity((1,3,6,1,4,1,20044,61,4,1))
_PmoabphcsCntClient_ObjectIdentity=ObjectIdentity
pmoabphcsCntClient=_PmoabphcsCntClient_ObjectIdentity((1,3,6,1,4,1,20044,61,4,2))
_PmoabphcsCntLine_ObjectIdentity=ObjectIdentity
pmoabphcsCntLine=_PmoabphcsCntLine_ObjectIdentity((1,3,6,1,4,1,20044,61,4,3))
_PmoabphcsCntlineOscErrTable_Object=MibTable
pmoabphcsCntlineOscErrTable=_PmoabphcsCntlineOscErrTable_Object((1,3,6,1,4,1,20044,61,4,3,16))
if mibBuilder.loadTexts:pmoabphcsCntlineOscErrTable.setStatus(_A)
_PmoabphcsCntlineOscErrEntry_Object=MibTableRow
pmoabphcsCntlineOscErrEntry=_PmoabphcsCntlineOscErrEntry_Object((1,3,6,1,4,1,20044,61,4,3,16,1))
pmoabphcsCntlineOscErrEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:pmoabphcsCntlineOscErrEntry.setStatus(_A)
class _PmoabphcsCntlineOscErrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsCntlineOscErrIndex_Type.__name__=_D
_PmoabphcsCntlineOscErrIndex_Object=MibTableColumn
pmoabphcsCntlineOscErrIndex=_PmoabphcsCntlineOscErrIndex_Object((1,3,6,1,4,1,20044,61,4,3,16,1,1),_PmoabphcsCntlineOscErrIndex_Type())
pmoabphcsCntlineOscErrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCntlineOscErrIndex.setStatus(_A)
_PmoabphcsCntlineOscErrValuePortn_Type=Counter32
_PmoabphcsCntlineOscErrValuePortn_Object=MibTableColumn
pmoabphcsCntlineOscErrValuePortn=_PmoabphcsCntlineOscErrValuePortn_Object((1,3,6,1,4,1,20044,61,4,3,16,1,2),_PmoabphcsCntlineOscErrValuePortn_Type())
pmoabphcsCntlineOscErrValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCntlineOscErrValuePortn.setStatus(_A)
_PmoabphcsCntlineOscErrErrorPortn_Type=EkiOnOff
_PmoabphcsCntlineOscErrErrorPortn_Object=MibTableColumn
pmoabphcsCntlineOscErrErrorPortn=_PmoabphcsCntlineOscErrErrorPortn_Object((1,3,6,1,4,1,20044,61,4,3,16,1,3),_PmoabphcsCntlineOscErrErrorPortn_Type())
pmoabphcsCntlineOscErrErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCntlineOscErrErrorPortn.setStatus(_A)
_PmoabphcsCntlineOscErrOverloadPortn_Type=EkiOnOff
_PmoabphcsCntlineOscErrOverloadPortn_Object=MibTableColumn
pmoabphcsCntlineOscErrOverloadPortn=_PmoabphcsCntlineOscErrOverloadPortn_Object((1,3,6,1,4,1,20044,61,4,3,16,1,4),_PmoabphcsCntlineOscErrOverloadPortn_Type())
pmoabphcsCntlineOscErrOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCntlineOscErrOverloadPortn.setStatus(_A)
_PmoabphcsCntCountersReset_Type=EkiOnOff
_PmoabphcsCntCountersReset_Object=MibScalar
pmoabphcsCntCountersReset=_PmoabphcsCntCountersReset_Object((1,3,6,1,4,1,20044,61,4,259),_PmoabphcsCntCountersReset_Type())
pmoabphcsCntCountersReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCntCountersReset.setStatus(_A)
_PmoabphcsCntCountersStop_Type=EkiOnOff
_PmoabphcsCntCountersStop_Object=MibScalar
pmoabphcsCntCountersStop=_PmoabphcsCntCountersStop_Object((1,3,6,1,4,1,20044,61,4,260),_PmoabphcsCntCountersStop_Type())
pmoabphcsCntCountersStop.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCntCountersStop.setStatus(_A)
_PmoabphcscontrolsWrite_ObjectIdentity=ObjectIdentity
pmoabphcscontrolsWrite=_PmoabphcscontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,61,6))
_PmoabphcsCtrlOther_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlOther=_PmoabphcsCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,61,6,1))
_PmoabphcsCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlsynth0=_PmoabphcsCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,61,6,1,0))
_PmoabphcsCtrlConfLoad_Type=EkiOnOff
_PmoabphcsCtrlConfLoad_Object=MibScalar
pmoabphcsCtrlConfLoad=_PmoabphcsCtrlConfLoad_Object((1,3,6,1,4,1,20044,61,6,1,0,1),_PmoabphcsCtrlConfLoad_Type())
pmoabphcsCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlConfLoad.setStatus(_A)
_PmoabphcsCtrlConfFlash_Type=EkiOnOff
_PmoabphcsCtrlConfFlash_Object=MibScalar
pmoabphcsCtrlConfFlash=_PmoabphcsCtrlConfFlash_Object((1,3,6,1,4,1,20044,61,6,1,0,9),_PmoabphcsCtrlConfFlash_Type())
pmoabphcsCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlConfFlash.setStatus(_A)
_PmoabphcsCtrlConfClear_Type=EkiOnOff
_PmoabphcsCtrlConfClear_Object=MibScalar
pmoabphcsCtrlConfClear=_PmoabphcsCtrlConfClear_Object((1,3,6,1,4,1,20044,61,6,1,0,13),_PmoabphcsCtrlConfClear_Type())
pmoabphcsCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlConfClear.setStatus(_A)
_PmoabphcsCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlswMgnt=_PmoabphcsCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,61,6,1,5))
_PmoabphcsCtrlColdReset_Type=EkiOnOff
_PmoabphcsCtrlColdReset_Object=MibScalar
pmoabphcsCtrlColdReset=_PmoabphcsCtrlColdReset_Object((1,3,6,1,4,1,20044,61,6,1,5,2),_PmoabphcsCtrlColdReset_Type())
pmoabphcsCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlColdReset.setStatus(_A)
_PmoabphcsCtrlWarmReset_Type=EkiOnOff
_PmoabphcsCtrlWarmReset_Object=MibScalar
pmoabphcsCtrlWarmReset=_PmoabphcsCtrlWarmReset_Object((1,3,6,1,4,1,20044,61,6,1,5,3),_PmoabphcsCtrlWarmReset_Type())
pmoabphcsCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlWarmReset.setStatus(_A)
_PmoabphcsCtrlledTest_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlledTest=_PmoabphcsCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,61,6,1,73))
_PmoabphcsCtrlGreenLed_Type=EkiOnOff
_PmoabphcsCtrlGreenLed_Object=MibScalar
pmoabphcsCtrlGreenLed=_PmoabphcsCtrlGreenLed_Object((1,3,6,1,4,1,20044,61,6,1,73,1),_PmoabphcsCtrlGreenLed_Type())
pmoabphcsCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlGreenLed.setStatus(_A)
_PmoabphcsCtrlRedLed_Type=EkiOnOff
_PmoabphcsCtrlRedLed_Object=MibScalar
pmoabphcsCtrlRedLed=_PmoabphcsCtrlRedLed_Object((1,3,6,1,4,1,20044,61,6,1,73,2),_PmoabphcsCtrlRedLed_Type())
pmoabphcsCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlRedLed.setStatus(_A)
_PmoabphcsCtrlLedOff_Type=EkiOnOff
_PmoabphcsCtrlLedOff_Object=MibScalar
pmoabphcsCtrlLedOff=_PmoabphcsCtrlLedOff_Object((1,3,6,1,4,1,20044,61,6,1,73,3),_PmoabphcsCtrlLedOff_Type())
pmoabphcsCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlLedOff.setStatus(_A)
_PmoabphcsCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlmaintMode=_PmoabphcsCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,61,6,1,75))
_PmoabphcsCtrlMaintenance_Type=EkiOnOff
_PmoabphcsCtrlMaintenance_Object=MibScalar
pmoabphcsCtrlMaintenance=_PmoabphcsCtrlMaintenance_Object((1,3,6,1,4,1,20044,61,6,1,75,1),_PmoabphcsCtrlMaintenance_Type())
pmoabphcsCtrlMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlMaintenance.setStatus(_A)
_PmoabphcsCtrlaprRestart_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlaprRestart=_PmoabphcsCtrlaprRestart_ObjectIdentity((1,3,6,1,4,1,20044,61,6,1,76))
_PmoabphcsCtrlAprManualRestart_Type=EkiOnOff
_PmoabphcsCtrlAprManualRestart_Object=MibScalar
pmoabphcsCtrlAprManualRestart=_PmoabphcsCtrlAprManualRestart_Object((1,3,6,1,4,1,20044,61,6,1,76,1),_PmoabphcsCtrlAprManualRestart_Type())
pmoabphcsCtrlAprManualRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlAprManualRestart.setStatus(_A)
_PmoabphcsCtrlClient_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlClient=_PmoabphcsCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,61,6,2))
_PmoabphcsCtrlclientOscInputSpanLoss_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlclientOscInputSpanLoss=_PmoabphcsCtrlclientOscInputSpanLoss_ObjectIdentity((1,3,6,1,4,1,20044,61,6,2,33))
_PmoabphcsCtrlClientSpanLoss_Type=EkiOnOff
_PmoabphcsCtrlClientSpanLoss_Object=MibScalar
pmoabphcsCtrlClientSpanLoss=_PmoabphcsCtrlClientSpanLoss_Object((1,3,6,1,4,1,20044,61,6,2,33,1),_PmoabphcsCtrlClientSpanLoss_Type())
pmoabphcsCtrlClientSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlClientSpanLoss.setStatus(_A)
class _PmoabphcsCtrlclientGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsCtrlclientGainCstMonitorValue_Type.__name__=_D
_PmoabphcsCtrlclientGainCstMonitorValue_Object=MibScalar
pmoabphcsCtrlclientGainCstMonitorValue=_PmoabphcsCtrlclientGainCstMonitorValue_Object((1,3,6,1,4,1,20044,61,6,2,34),_PmoabphcsCtrlclientGainCstMonitorValue_Type())
pmoabphcsCtrlclientGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlclientGainCstMonitorValue.setStatus(_A)
class _PmoabphcsCtrlclientGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsCtrlclientGainSettingValue_Type.__name__=_D
_PmoabphcsCtrlclientGainSettingValue_Object=MibScalar
pmoabphcsCtrlclientGainSettingValue=_PmoabphcsCtrlclientGainSettingValue_Object((1,3,6,1,4,1,20044,61,6,2,36),_PmoabphcsCtrlclientGainSettingValue_Type())
pmoabphcsCtrlclientGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlclientGainSettingValue.setStatus(_A)
_PmoabphcsCtrlclientGainProcessing_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlclientGainProcessing=_PmoabphcsCtrlclientGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,61,6,2,37))
_PmoabphcsCtrlClientGainProc_Type=EkiOnOff
_PmoabphcsCtrlClientGainProc_Object=MibScalar
pmoabphcsCtrlClientGainProc=_PmoabphcsCtrlClientGainProc_Object((1,3,6,1,4,1,20044,61,6,2,37,1),_PmoabphcsCtrlClientGainProc_Type())
pmoabphcsCtrlClientGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlClientGainProc.setStatus(_A)
class _PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Type.__name__=_D
_PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Object=MibScalar
pmoabphcsCtrlclientGainCstFiberAgingMarginValue=_PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,61,6,2,38),_PmoabphcsCtrlclientGainCstFiberAgingMarginValue_Type())
pmoabphcsCtrlclientGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlclientGainCstFiberAgingMarginValue.setStatus(_A)
_PmoabphcsCtrlclientMsaAttenuationValue_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlclientMsaAttenuationValue=_PmoabphcsCtrlclientMsaAttenuationValue_ObjectIdentity((1,3,6,1,4,1,20044,61,6,2,40))
_PmoabphcsCtrlClientAttenuation_Type=EkiOnOff
_PmoabphcsCtrlClientAttenuation_Object=MibScalar
pmoabphcsCtrlClientAttenuation=_PmoabphcsCtrlClientAttenuation_Object((1,3,6,1,4,1,20044,61,6,2,40,1),_PmoabphcsCtrlClientAttenuation_Type())
pmoabphcsCtrlClientAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlClientAttenuation.setStatus(_A)
_PmoabphcsCtrlLine_ObjectIdentity=ObjectIdentity
pmoabphcsCtrlLine=_PmoabphcsCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,61,6,3))
_PmoabphcsCtrllineOscInputSpanLoss_ObjectIdentity=ObjectIdentity
pmoabphcsCtrllineOscInputSpanLoss=_PmoabphcsCtrllineOscInputSpanLoss_ObjectIdentity((1,3,6,1,4,1,20044,61,6,3,49))
_PmoabphcsCtrlLineSpanLoss_Type=EkiOnOff
_PmoabphcsCtrlLineSpanLoss_Object=MibScalar
pmoabphcsCtrlLineSpanLoss=_PmoabphcsCtrlLineSpanLoss_Object((1,3,6,1,4,1,20044,61,6,3,49,1),_PmoabphcsCtrlLineSpanLoss_Type())
pmoabphcsCtrlLineSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlLineSpanLoss.setStatus(_A)
class _PmoabphcsCtrllineGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsCtrllineGainCstMonitorValue_Type.__name__=_D
_PmoabphcsCtrllineGainCstMonitorValue_Object=MibScalar
pmoabphcsCtrllineGainCstMonitorValue=_PmoabphcsCtrllineGainCstMonitorValue_Object((1,3,6,1,4,1,20044,61,6,3,50),_PmoabphcsCtrllineGainCstMonitorValue_Type())
pmoabphcsCtrllineGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrllineGainCstMonitorValue.setStatus(_A)
class _PmoabphcsCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsCtrllineGainSettingValue_Type.__name__=_D
_PmoabphcsCtrllineGainSettingValue_Object=MibScalar
pmoabphcsCtrllineGainSettingValue=_PmoabphcsCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,61,6,3,52),_PmoabphcsCtrllineGainSettingValue_Type())
pmoabphcsCtrllineGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrllineGainSettingValue.setStatus(_A)
_PmoabphcsCtrllineGainProcessing_ObjectIdentity=ObjectIdentity
pmoabphcsCtrllineGainProcessing=_PmoabphcsCtrllineGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,61,6,3,53))
_PmoabphcsCtrlLineGainProc_Type=EkiOnOff
_PmoabphcsCtrlLineGainProc_Object=MibScalar
pmoabphcsCtrlLineGainProc=_PmoabphcsCtrlLineGainProc_Object((1,3,6,1,4,1,20044,61,6,3,53,1),_PmoabphcsCtrlLineGainProc_Type())
pmoabphcsCtrlLineGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlLineGainProc.setStatus(_A)
class _PmoabphcsCtrllineGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoabphcsCtrllineGainCstFiberAgingMarginValue_Type.__name__=_D
_PmoabphcsCtrllineGainCstFiberAgingMarginValue_Object=MibScalar
pmoabphcsCtrllineGainCstFiberAgingMarginValue=_PmoabphcsCtrllineGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,61,6,3,54),_PmoabphcsCtrllineGainCstFiberAgingMarginValue_Type())
pmoabphcsCtrllineGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrllineGainCstFiberAgingMarginValue.setStatus(_A)
_PmoabphcsCtrllineMsaAttenuationValue_ObjectIdentity=ObjectIdentity
pmoabphcsCtrllineMsaAttenuationValue=_PmoabphcsCtrllineMsaAttenuationValue_ObjectIdentity((1,3,6,1,4,1,20044,61,6,3,56))
_PmoabphcsCtrlLineAttenuation_Type=EkiOnOff
_PmoabphcsCtrlLineAttenuation_Object=MibScalar
pmoabphcsCtrlLineAttenuation=_PmoabphcsCtrlLineAttenuation_Object((1,3,6,1,4,1,20044,61,6,3,56,1),_PmoabphcsCtrlLineAttenuation_Type())
pmoabphcsCtrlLineAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCtrlLineAttenuation.setStatus(_A)
_Pmoabphcsri_ObjectIdentity=ObjectIdentity
pmoabphcsri=_Pmoabphcsri_ObjectIdentity((1,3,6,1,4,1,20044,61,7))
_PmoabphcsRinvReloadInventory_Type=EkiOnOff
_PmoabphcsRinvReloadInventory_Object=MibScalar
pmoabphcsRinvReloadInventory=_PmoabphcsRinvReloadInventory_Object((1,3,6,1,4,1,20044,61,7,2),_PmoabphcsRinvReloadInventory_Type())
pmoabphcsRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsRinvReloadInventory.setStatus(_A)
_PmoabphcsRinvHwPlatform_Type=DisplayString
_PmoabphcsRinvHwPlatform_Object=MibScalar
pmoabphcsRinvHwPlatform=_PmoabphcsRinvHwPlatform_Object((1,3,6,1,4,1,20044,61,7,3),_PmoabphcsRinvHwPlatform_Type())
pmoabphcsRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvHwPlatform.setStatus(_A)
_PmoabphcsRinvModulePlatform_Type=DisplayString
_PmoabphcsRinvModulePlatform_Object=MibScalar
pmoabphcsRinvModulePlatform=_PmoabphcsRinvModulePlatform_Object((1,3,6,1,4,1,20044,61,7,4),_PmoabphcsRinvModulePlatform_Type())
pmoabphcsRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvModulePlatform.setStatus(_A)
_PmoabphcsRinvSwPlatform_Type=DisplayString
_PmoabphcsRinvSwPlatform_Object=MibScalar
pmoabphcsRinvSwPlatform=_PmoabphcsRinvSwPlatform_Object((1,3,6,1,4,1,20044,61,7,5),_PmoabphcsRinvSwPlatform_Type())
pmoabphcsRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvSwPlatform.setStatus(_A)
_PmoabphcsRinvGwPlatform_Type=DisplayString
_PmoabphcsRinvGwPlatform_Object=MibScalar
pmoabphcsRinvGwPlatform=_PmoabphcsRinvGwPlatform_Object((1,3,6,1,4,1,20044,61,7,6),_PmoabphcsRinvGwPlatform_Type())
pmoabphcsRinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvGwPlatform.setStatus(_A)
_PmoabphcsRinvBoosterTable_Object=MibTable
pmoabphcsRinvBoosterTable=_PmoabphcsRinvBoosterTable_Object((1,3,6,1,4,1,20044,61,7,7))
if mibBuilder.loadTexts:pmoabphcsRinvBoosterTable.setStatus(_A)
_PmoabphcsRinvBoosterEntry_Object=MibTableRow
pmoabphcsRinvBoosterEntry=_PmoabphcsRinvBoosterEntry_Object((1,3,6,1,4,1,20044,61,7,7,1))
pmoabphcsRinvBoosterEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:pmoabphcsRinvBoosterEntry.setStatus(_A)
class _PmoabphcsRinvBoosterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoabphcsRinvBoosterIndex_Type.__name__=_D
_PmoabphcsRinvBoosterIndex_Object=MibTableColumn
pmoabphcsRinvBoosterIndex=_PmoabphcsRinvBoosterIndex_Object((1,3,6,1,4,1,20044,61,7,7,1,1),_PmoabphcsRinvBoosterIndex_Type())
pmoabphcsRinvBoosterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvBoosterIndex.setStatus(_A)
_PmoabphcsRinvBooster_Type=DisplayString
_PmoabphcsRinvBooster_Object=MibTableColumn
pmoabphcsRinvBooster=_PmoabphcsRinvBooster_Object((1,3,6,1,4,1,20044,61,7,7,1,2),_PmoabphcsRinvBooster_Type())
pmoabphcsRinvBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvBooster.setStatus(_A)
_PmoabphcsRinvPreAmpTable_Object=MibTable
pmoabphcsRinvPreAmpTable=_PmoabphcsRinvPreAmpTable_Object((1,3,6,1,4,1,20044,61,7,8))
if mibBuilder.loadTexts:pmoabphcsRinvPreAmpTable.setStatus(_A)
_PmoabphcsRinvPreAmpEntry_Object=MibTableRow
pmoabphcsRinvPreAmpEntry=_PmoabphcsRinvPreAmpEntry_Object((1,3,6,1,4,1,20044,61,7,8,1))
pmoabphcsRinvPreAmpEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:pmoabphcsRinvPreAmpEntry.setStatus(_A)
class _PmoabphcsRinvPreAmpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoabphcsRinvPreAmpIndex_Type.__name__=_D
_PmoabphcsRinvPreAmpIndex_Object=MibTableColumn
pmoabphcsRinvPreAmpIndex=_PmoabphcsRinvPreAmpIndex_Object((1,3,6,1,4,1,20044,61,7,8,1,1),_PmoabphcsRinvPreAmpIndex_Type())
pmoabphcsRinvPreAmpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvPreAmpIndex.setStatus(_A)
_PmoabphcsRinvPreAmp_Type=DisplayString
_PmoabphcsRinvPreAmp_Object=MibTableColumn
pmoabphcsRinvPreAmp=_PmoabphcsRinvPreAmp_Object((1,3,6,1,4,1,20044,61,7,8,1,2),_PmoabphcsRinvPreAmp_Type())
pmoabphcsRinvPreAmp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsRinvPreAmp.setStatus(_A)
_PmoabphcsConfig_ObjectIdentity=ObjectIdentity
pmoabphcsConfig=_PmoabphcsConfig_ObjectIdentity((1,3,6,1,4,1,20044,61,9))
_PmoabphcsCfgNoValue_ObjectIdentity=ObjectIdentity
pmoabphcsCfgNoValue=_PmoabphcsCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,61,9,1))
_PmoabphcstableclientStartup_ObjectIdentity=ObjectIdentity
pmoabphcstableclientStartup=_PmoabphcstableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,61,9,1,1))
class _PmoabphcsCfgclientEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientEdfaLaserCtrl_Type.__name__=_F
_PmoabphcsCfgclientEdfaLaserCtrl_Object=MibScalar
pmoabphcsCfgclientEdfaLaserCtrl=_PmoabphcsCfgclientEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,61,9,1,1,2),_PmoabphcsCfgclientEdfaLaserCtrl_Type())
pmoabphcsCfgclientEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientEdfaLaserCtrl.setStatus(_A)
class _PmoabphcsCfgclientEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientEdfaLaserMode_Type.__name__=_F
_PmoabphcsCfgclientEdfaLaserMode_Object=MibScalar
pmoabphcsCfgclientEdfaLaserMode=_PmoabphcsCfgclientEdfaLaserMode_Object((1,3,6,1,4,1,20044,61,9,1,1,3),_PmoabphcsCfgclientEdfaLaserMode_Type())
pmoabphcsCfgclientEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientEdfaLaserMode.setStatus(_A)
class _PmoabphcsCfgclientGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientGainValue_Type.__name__=_F
_PmoabphcsCfgclientGainValue_Object=MibScalar
pmoabphcsCfgclientGainValue=_PmoabphcsCfgclientGainValue_Object((1,3,6,1,4,1,20044,61,9,1,1,4),_PmoabphcsCfgclientGainValue_Type())
pmoabphcsCfgclientGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientGainValue.setStatus(_A)
class _PmoabphcsCfgclientTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientTiltValue_Type.__name__=_F
_PmoabphcsCfgclientTiltValue_Object=MibScalar
pmoabphcsCfgclientTiltValue=_PmoabphcsCfgclientTiltValue_Object((1,3,6,1,4,1,20044,61,9,1,1,5),_PmoabphcsCfgclientTiltValue_Type())
pmoabphcsCfgclientTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientTiltValue.setStatus(_A)
class _PmoabphcsCfgclientMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientMsaLoss_Type.__name__=_F
_PmoabphcsCfgclientMsaLoss_Object=MibScalar
pmoabphcsCfgclientMsaLoss=_PmoabphcsCfgclientMsaLoss_Object((1,3,6,1,4,1,20044,61,9,1,1,6),_PmoabphcsCfgclientMsaLoss_Type())
pmoabphcsCfgclientMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientMsaLoss.setStatus(_A)
class _PmoabphcsCfgclientOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientOutputPowerValue_Type.__name__=_F
_PmoabphcsCfgclientOutputPowerValue_Object=MibScalar
pmoabphcsCfgclientOutputPowerValue=_PmoabphcsCfgclientOutputPowerValue_Object((1,3,6,1,4,1,20044,61,9,1,1,7),_PmoabphcsCfgclientOutputPowerValue_Type())
pmoabphcsCfgclientOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientOutputPowerValue.setStatus(_A)
class _PmoabphcsCfgclientAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgclientAseCompensation_Type.__name__=_F
_PmoabphcsCfgclientAseCompensation_Object=MibScalar
pmoabphcsCfgclientAseCompensation=_PmoabphcsCfgclientAseCompensation_Object((1,3,6,1,4,1,20044,61,9,1,1,8),_PmoabphcsCfgclientAseCompensation_Type())
pmoabphcsCfgclientAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgclientAseCompensation.setStatus(_A)
_PmoabphcsCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoabphcsCfgLineStartUp=_PmoabphcsCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,61,9,2))
_PmoabphcstablelineStartup_ObjectIdentity=ObjectIdentity
pmoabphcstablelineStartup=_PmoabphcstablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,61,9,2,1))
class _PmoabphcsCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineEdfaLaserCtrl_Type.__name__=_F
_PmoabphcsCfglineEdfaLaserCtrl_Object=MibScalar
pmoabphcsCfglineEdfaLaserCtrl=_PmoabphcsCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,61,9,2,1,2),_PmoabphcsCfglineEdfaLaserCtrl_Type())
pmoabphcsCfglineEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoabphcsCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineEdfaLaserMode_Type.__name__=_F
_PmoabphcsCfglineEdfaLaserMode_Object=MibScalar
pmoabphcsCfglineEdfaLaserMode=_PmoabphcsCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,61,9,2,1,3),_PmoabphcsCfglineEdfaLaserMode_Type())
pmoabphcsCfglineEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineEdfaLaserMode.setStatus(_A)
class _PmoabphcsCfglineGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineGainValue_Type.__name__=_F
_PmoabphcsCfglineGainValue_Object=MibScalar
pmoabphcsCfglineGainValue=_PmoabphcsCfglineGainValue_Object((1,3,6,1,4,1,20044,61,9,2,1,4),_PmoabphcsCfglineGainValue_Type())
pmoabphcsCfglineGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineGainValue.setStatus(_A)
class _PmoabphcsCfglineTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineTiltValue_Type.__name__=_F
_PmoabphcsCfglineTiltValue_Object=MibScalar
pmoabphcsCfglineTiltValue=_PmoabphcsCfglineTiltValue_Object((1,3,6,1,4,1,20044,61,9,2,1,5),_PmoabphcsCfglineTiltValue_Type())
pmoabphcsCfglineTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineTiltValue.setStatus(_A)
class _PmoabphcsCfglineMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineMsaLoss_Type.__name__=_F
_PmoabphcsCfglineMsaLoss_Object=MibScalar
pmoabphcsCfglineMsaLoss=_PmoabphcsCfglineMsaLoss_Object((1,3,6,1,4,1,20044,61,9,2,1,6),_PmoabphcsCfglineMsaLoss_Type())
pmoabphcsCfglineMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineMsaLoss.setStatus(_A)
class _PmoabphcsCfglineOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineOutputPowerValue_Type.__name__=_F
_PmoabphcsCfglineOutputPowerValue_Object=MibScalar
pmoabphcsCfglineOutputPowerValue=_PmoabphcsCfglineOutputPowerValue_Object((1,3,6,1,4,1,20044,61,9,2,1,7),_PmoabphcsCfglineOutputPowerValue_Type())
pmoabphcsCfglineOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineOutputPowerValue.setStatus(_A)
class _PmoabphcsCfglineAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfglineAseCompensation_Type.__name__=_F
_PmoabphcsCfglineAseCompensation_Object=MibScalar
pmoabphcsCfglineAseCompensation=_PmoabphcsCfglineAseCompensation_Object((1,3,6,1,4,1,20044,61,9,2,1,8),_PmoabphcsCfglineAseCompensation_Type())
pmoabphcsCfglineAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfglineAseCompensation.setStatus(_A)
class _PmoabphcsCfgaprMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgaprMode_Type.__name__=_F
_PmoabphcsCfgaprMode_Object=MibScalar
pmoabphcsCfgaprMode=_PmoabphcsCfgaprMode_Object((1,3,6,1,4,1,20044,61,9,2,1,11),_PmoabphcsCfgaprMode_Type())
pmoabphcsCfgaprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgaprMode.setStatus(_A)
_PmoabphcsCfgClientSupvStartUp_ObjectIdentity=ObjectIdentity
pmoabphcsCfgClientSupvStartUp=_PmoabphcsCfgClientSupvStartUp_ObjectIdentity((1,3,6,1,4,1,20044,61,9,3))
_PmoabphcsCfgLineStartupTable_Object=MibTable
pmoabphcsCfgLineStartupTable=_PmoabphcsCfgLineStartupTable_Object((1,3,6,1,4,1,20044,61,9,3,1))
if mibBuilder.loadTexts:pmoabphcsCfgLineStartupTable.setStatus(_A)
_PmoabphcsCfgLineStartupEntry_Object=MibTableRow
pmoabphcsCfgLineStartupEntry=_PmoabphcsCfgLineStartupEntry_Object((1,3,6,1,4,1,20044,61,9,3,1,1))
pmoabphcsCfgLineStartupEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:pmoabphcsCfgLineStartupEntry.setStatus(_A)
class _PmoabphcsCfgLineStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsCfgLineStartupIndex_Type.__name__=_D
_PmoabphcsCfgLineStartupIndex_Object=MibTableColumn
pmoabphcsCfgLineStartupIndex=_PmoabphcsCfgLineStartupIndex_Object((1,3,6,1,4,1,20044,61,9,3,1,1,1),_PmoabphcsCfgLineStartupIndex_Type())
pmoabphcsCfgLineStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCfgLineStartupIndex.setStatus(_A)
class _PmoabphcsCfgLineOscLaserCtrlPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgLineOscLaserCtrlPortn_Type.__name__=_F
_PmoabphcsCfgLineOscLaserCtrlPortn_Object=MibTableColumn
pmoabphcsCfgLineOscLaserCtrlPortn=_PmoabphcsCfgLineOscLaserCtrlPortn_Object((1,3,6,1,4,1,20044,61,9,3,1,1,3),_PmoabphcsCfgLineOscLaserCtrlPortn_Type())
pmoabphcsCfgLineOscLaserCtrlPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgLineOscLaserCtrlPortn.setStatus(_A)
class _PmoabphcsCfgLineOscOosPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgLineOscOosPortn_Type.__name__=_F
_PmoabphcsCfgLineOscOosPortn_Object=MibTableColumn
pmoabphcsCfgLineOscOosPortn=_PmoabphcsCfgLineOscOosPortn_Object((1,3,6,1,4,1,20044,61,9,3,1,1,4),_PmoabphcsCfgLineOscOosPortn_Type())
pmoabphcsCfgLineOscOosPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgLineOscOosPortn.setStatus(_A)
class _PmoabphcsCfgLineOscSpanLengthPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgLineOscSpanLengthPortn_Type.__name__=_F
_PmoabphcsCfgLineOscSpanLengthPortn_Object=MibTableColumn
pmoabphcsCfgLineOscSpanLengthPortn=_PmoabphcsCfgLineOscSpanLengthPortn_Object((1,3,6,1,4,1,20044,61,9,3,1,1,5),_PmoabphcsCfgLineOscSpanLengthPortn_Type())
pmoabphcsCfgLineOscSpanLengthPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgLineOscSpanLengthPortn.setStatus(_A)
class _PmoabphcsCfgLineOscCorrectionFactorPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoabphcsCfgLineOscCorrectionFactorPortn_Type.__name__=_F
_PmoabphcsCfgLineOscCorrectionFactorPortn_Object=MibTableColumn
pmoabphcsCfgLineOscCorrectionFactorPortn=_PmoabphcsCfgLineOscCorrectionFactorPortn_Object((1,3,6,1,4,1,20044,61,9,3,1,1,6),_PmoabphcsCfgLineOscCorrectionFactorPortn_Type())
pmoabphcsCfgLineOscCorrectionFactorPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgLineOscCorrectionFactorPortn.setStatus(_A)
_PmoabphcsCfgLabels_ObjectIdentity=ObjectIdentity
pmoabphcsCfgLabels=_PmoabphcsCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,61,9,4))
_PmoabphcsCfgLabelclientTable_Object=MibTable
pmoabphcsCfgLabelclientTable=_PmoabphcsCfgLabelclientTable_Object((1,3,6,1,4,1,20044,61,9,4,1))
if mibBuilder.loadTexts:pmoabphcsCfgLabelclientTable.setStatus(_A)
_PmoabphcsCfgLabelclientEntry_Object=MibTableRow
pmoabphcsCfgLabelclientEntry=_PmoabphcsCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,61,9,4,1,1))
pmoabphcsCfgLabelclientEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:pmoabphcsCfgLabelclientEntry.setStatus(_A)
class _PmoabphcsCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsCfgLabelclientIndex_Type.__name__=_D
_PmoabphcsCfgLabelclientIndex_Object=MibTableColumn
pmoabphcsCfgLabelclientIndex=_PmoabphcsCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,61,9,4,1,1,1),_PmoabphcsCfgLabelclientIndex_Type())
pmoabphcsCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCfgLabelclientIndex.setStatus(_A)
class _PmoabphcsCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoabphcsCfgLabelclientPortn_Type.__name__=_H
_PmoabphcsCfgLabelclientPortn_Object=MibTableColumn
pmoabphcsCfgLabelclientPortn=_PmoabphcsCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,61,9,4,1,1,3),_PmoabphcsCfgLabelclientPortn_Type())
pmoabphcsCfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgLabelclientPortn.setStatus(_A)
_PmoabphcsCfgLabellineTable_Object=MibTable
pmoabphcsCfgLabellineTable=_PmoabphcsCfgLabellineTable_Object((1,3,6,1,4,1,20044,61,9,4,2))
if mibBuilder.loadTexts:pmoabphcsCfgLabellineTable.setStatus(_A)
_PmoabphcsCfgLabellineEntry_Object=MibTableRow
pmoabphcsCfgLabellineEntry=_PmoabphcsCfgLabellineEntry_Object((1,3,6,1,4,1,20044,61,9,4,2,1))
pmoabphcsCfgLabellineEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:pmoabphcsCfgLabellineEntry.setStatus(_A)
class _PmoabphcsCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoabphcsCfgLabellineIndex_Type.__name__=_D
_PmoabphcsCfgLabellineIndex_Object=MibTableColumn
pmoabphcsCfgLabellineIndex=_PmoabphcsCfgLabellineIndex_Object((1,3,6,1,4,1,20044,61,9,4,2,1,1),_PmoabphcsCfgLabellineIndex_Type())
pmoabphcsCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcsCfgLabellineIndex.setStatus(_A)
class _PmoabphcsCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoabphcsCfgLabellinePortn_Type.__name__=_H
_PmoabphcsCfgLabellinePortn_Object=MibTableColumn
pmoabphcsCfgLabellinePortn=_PmoabphcsCfgLabellinePortn_Object((1,3,6,1,4,1,20044,61,9,4,2,1,3),_PmoabphcsCfgLabellinePortn_Type())
pmoabphcsCfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgLabellinePortn.setStatus(_A)
_PmoabphcsCfgWriteConfiguration_Type=EkiOnOff
_PmoabphcsCfgWriteConfiguration_Object=MibScalar
pmoabphcsCfgWriteConfiguration=_PmoabphcsCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,61,9,257),_PmoabphcsCfgWriteConfiguration_Type())
pmoabphcsCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoabphcsCfgWriteConfiguration.setStatus(_A)
_Pmoabphcstraps_ObjectIdentity=ObjectIdentity
pmoabphcstraps=_Pmoabphcstraps_ObjectIdentity((1,3,6,1,4,1,20044,61,10))
class _PmoabphcstrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoabphcstrapBoardNumber_Type.__name__=_D
_PmoabphcstrapBoardNumber_Object=MibScalar
pmoabphcstrapBoardNumber=_PmoabphcstrapBoardNumber_Object((1,3,6,1,4,1,20044,61,10,4),_PmoabphcstrapBoardNumber_Type())
pmoabphcstrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoabphcstrapBoardNumber.setStatus(_A)
pmoabphcsLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,61,10,34))
pmoabphcsLineTrapCritGoesOn.setObjects(*((_E,_I),(_E,_J),(_E,_G)))
if mibBuilder.loadTexts:pmoabphcsLineTrapCritGoesOn.setStatus(_A)
pmoabphcsLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,61,10,35))
pmoabphcsLineTrapCritGoesOff.setObjects(*((_E,_I),(_E,_J),(_E,_G)))
if mibBuilder.loadTexts:pmoabphcsLineTrapCritGoesOff.setStatus(_A)
pmoabphcsClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,61,10,44))
pmoabphcsClientTrapCritGoesOn.setObjects(*((_E,_K),(_E,_L),(_E,_G)))
if mibBuilder.loadTexts:pmoabphcsClientTrapCritGoesOn.setStatus(_A)
pmoabphcsClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,61,10,45))
pmoabphcsClientTrapCritGoesOff.setObjects(*((_E,_K),(_E,_L),(_E,_G)))
if mibBuilder.loadTexts:pmoabphcsClientTrapCritGoesOff.setStatus(_A)
pmoabphcsPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,61,10,50))
pmoabphcsPowerTrapUrgentGoesOn.setObjects(*((_E,_M),(_E,_N),(_E,_G)))
if mibBuilder.loadTexts:pmoabphcsPowerTrapUrgentGoesOn.setStatus(_A)
pmoabphcsPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,61,10,51))
pmoabphcsPowerTrapUrgentGoesOff.setObjects(*((_E,_M),(_E,_N),(_E,_G)))
if mibBuilder.loadTexts:pmoabphcsPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PmoabphcspreampMode':PmoabphcspreampMode,'PmoabphcsboosterMode':PmoabphcsboosterMode,'PmoabphcsaprMode':PmoabphcsaprMode,'PmoabphcsPreampGainAdjMode':PmoabphcsPreampGainAdjMode,'PmoabphcsBoosterGainAdjMode':PmoabphcsBoosterGainAdjMode,'PmoabphcsPreampCstGainAdjMode':PmoabphcsPreampCstGainAdjMode,'PmoabphcsBoosterCstGainAdjMode':PmoabphcsBoosterCstGainAdjMode,'modulepmoabphcs':modulepmoabphcs,'pmoabphcsalarms':pmoabphcsalarms,'pmoabphcsAlmOther':pmoabphcsAlmOther,'pmoabphcsAlmOtherNurg':pmoabphcsAlmOtherNurg,'pmoabphcsAlmsynthAlm2':pmoabphcsAlmsynthAlm2,'pmoabphcsAlmConfTableSave':pmoabphcsAlmConfTableSave,'pmoabphcsAlmInvUpload':pmoabphcsAlmInvUpload,'pmoabphcsAlmConfTableLoad':pmoabphcsAlmConfTableLoad,'pmoabphcsAlmfoaWarnings':pmoabphcsAlmfoaWarnings,'pmoabphcsAlmTermpLowWarning':pmoabphcsAlmTermpLowWarning,'pmoabphcsAlmTempHighWarning':pmoabphcsAlmTempHighWarning,'pmoabphcsAlmOtherUrg':pmoabphcsAlmOtherUrg,'pmoabphcsAlmfoaAlarms':pmoabphcsAlmfoaAlarms,'pmoabphcsAlmTermpLowAlarm':pmoabphcsAlmTermpLowAlarm,'pmoabphcsAlmTempHighAlarm':pmoabphcsAlmTempHighAlarm,'pmoabphcsAlmOtherCrit':pmoabphcsAlmOtherCrit,'pmoabphcsAlmsynthAlm0':pmoabphcsAlmsynthAlm0,'pmoabphcsAlmMaintenanceMode':pmoabphcsAlmMaintenanceMode,'pmoabphcsAlmAprOn':pmoabphcsAlmAprOn,'pmoabphcsAlmModGlobFail':pmoabphcsAlmModGlobFail,'pmoabphcsAlmUpEdfaInitNotCompl':pmoabphcsAlmUpEdfaInitNotCompl,'pmoabphcsAlmDwEdfaInitNotCompl':pmoabphcsAlmDwEdfaInitNotCompl,'pmoabphcsAlmExtPump1NotLocked':pmoabphcsAlmExtPump1NotLocked,_N:pmoabphcsAlmDefFuseA,_M:pmoabphcsAlmDefFuseB,'pmoabphcsAlmClient':pmoabphcsAlmClient,'pmoabphcsAlmClientNurg':pmoabphcsAlmClientNurg,'pmoabphcsAlmclientEdfaWarnings':pmoabphcsAlmclientEdfaWarnings,'pmoabphcsAlmClientGainLowWarning':pmoabphcsAlmClientGainLowWarning,'pmoabphcsAlmClientGainHighWarning':pmoabphcsAlmClientGainHighWarning,'pmoabphcsAlmClientInputPwrLowWarning':pmoabphcsAlmClientInputPwrLowWarning,'pmoabphcsAlmClientInputPwrHighWarning':pmoabphcsAlmClientInputPwrHighWarning,'pmoabphcsAlmClientOutputPwrLowWarning':pmoabphcsAlmClientOutputPwrLowWarning,'pmoabphcsAlmClientOutputPwrHighWarning':pmoabphcsAlmClientOutputPwrHighWarning,'pmoabphcsAlmClientBiasLowWarning':pmoabphcsAlmClientBiasLowWarning,'pmoabphcsAlmClientBiasHighWarning':pmoabphcsAlmClientBiasHighWarning,'pmoabphcsAlmClientUrg':pmoabphcsAlmClientUrg,'pmoabphcsAlmclientEdfaAlarms1':pmoabphcsAlmclientEdfaAlarms1,'pmoabphcsAlmClientGainLowAlarm':pmoabphcsAlmClientGainLowAlarm,'pmoabphcsAlmClientGainHighAlarm':pmoabphcsAlmClientGainHighAlarm,'pmoabphcsAlmClientInputPwrLowAlarm':pmoabphcsAlmClientInputPwrLowAlarm,'pmoabphcsAlmClientInputPwrHighAlarm':pmoabphcsAlmClientInputPwrHighAlarm,'pmoabphcsAlmClientOutputPwrLowAlarm':pmoabphcsAlmClientOutputPwrLowAlarm,'pmoabphcsAlmClientOutputPwrHighAlarm':pmoabphcsAlmClientOutputPwrHighAlarm,'pmoabphcsAlmClientBiasLowAlarm':pmoabphcsAlmClientBiasLowAlarm,'pmoabphcsAlmClientBiasHighAlarm':pmoabphcsAlmClientBiasHighAlarm,'pmoabphcsAlmClientCrit':pmoabphcsAlmClientCrit,'pmoabphcsAlmsynthAlm8':pmoabphcsAlmsynthAlm8,_L:pmoabphcsAlmClientHwFail,'pmoabphcsAlmClientTxOff':pmoabphcsAlmClientTxOff,_K:pmoabphcsAlmClientFail,'pmoabphcsAlmClientExtPumpFail':pmoabphcsAlmClientExtPumpFail,'pmoabphcsAlmSupvbFail':pmoabphcsAlmSupvbFail,'pmoabphcsAlmclientEdfaAlarms2':pmoabphcsAlmclientEdfaAlarms2,'pmoabphcsAlmClientEdfaNr':pmoabphcsAlmClientEdfaNr,'pmoabphcsAlmClientEdfaTecFail':pmoabphcsAlmClientEdfaTecFail,'pmoabphcsAlmClientEdfaLaserFail':pmoabphcsAlmClientEdfaLaserFail,'pmoabphcsAlmClientEdfaLos':pmoabphcsAlmClientEdfaLos,'pmoabphcsAlmClientExtPumpEdfaLowCurrent':pmoabphcsAlmClientExtPumpEdfaLowCurrent,'pmoabphcsAlmClientGainOutOfRange':pmoabphcsAlmClientGainOutOfRange,'pmoabphcsAlmclientMsaAlarms':pmoabphcsAlmclientMsaAlarms,'pmoabphcsAlmClientMsaLos':pmoabphcsAlmClientMsaLos,'pmoabphcsAlmClientMsaAttenuation':pmoabphcsAlmClientMsaAttenuation,'pmoabphcsAlmLine':pmoabphcsAlmLine,'pmoabphcsAlmLineNurg':pmoabphcsAlmLineNurg,'pmoabphcsAlmlineEdfaWarnings':pmoabphcsAlmlineEdfaWarnings,'pmoabphcsAlmLineGainLowWarning':pmoabphcsAlmLineGainLowWarning,'pmoabphcsAlmLineGainHighWarning':pmoabphcsAlmLineGainHighWarning,'pmoabphcsAlmLineInputPwrLowWarning':pmoabphcsAlmLineInputPwrLowWarning,'pmoabphcsAlmLineInputPwrHighWarning':pmoabphcsAlmLineInputPwrHighWarning,'pmoabphcsAlmLineOutputPwrLowWarning':pmoabphcsAlmLineOutputPwrLowWarning,'pmoabphcsAlmLineOutputPwrHighWarning':pmoabphcsAlmLineOutputPwrHighWarning,'pmoabphcsAlmLineBiasLowWarning':pmoabphcsAlmLineBiasLowWarning,'pmoabphcsAlmLineBiasHighWarning':pmoabphcsAlmLineBiasHighWarning,'pmoabphcsAlmLineUrg':pmoabphcsAlmLineUrg,'pmoabphcsAlmlineEdfaAlarms1':pmoabphcsAlmlineEdfaAlarms1,'pmoabphcsAlmLineGainLowAlarm':pmoabphcsAlmLineGainLowAlarm,'pmoabphcsAlmLineGainHighAlarm':pmoabphcsAlmLineGainHighAlarm,'pmoabphcsAlmLineInputPwrLowAlarm':pmoabphcsAlmLineInputPwrLowAlarm,'pmoabphcsAlmLineInputPwrHighAlarm':pmoabphcsAlmLineInputPwrHighAlarm,'pmoabphcsAlmLineOutputPwrLowAlarm':pmoabphcsAlmLineOutputPwrLowAlarm,'pmoabphcsAlmLineOutputPwrHighAlarm':pmoabphcsAlmLineOutputPwrHighAlarm,'pmoabphcsAlmLineBiasLowAlarm':pmoabphcsAlmLineBiasLowAlarm,'pmoabphcsAlmLineBiasHighAlarm':pmoabphcsAlmLineBiasHighAlarm,'pmoabphcsAlmLineCrit':pmoabphcsAlmLineCrit,'pmoabphcsAlmsynthAlm7':pmoabphcsAlmsynthAlm7,_J:pmoabphcsAlmLineHwFail,'pmoabphcsAlmLineTxOff':pmoabphcsAlmLineTxOff,_I:pmoabphcsAlmLineFail,'pmoabphcsAlmLineExtPumpFail':pmoabphcsAlmLineExtPumpFail,'pmoabphcsAlmSupvaFail':pmoabphcsAlmSupvaFail,'pmoabphcsAlmlineEdfaAlarms2':pmoabphcsAlmlineEdfaAlarms2,'pmoabphcsAlmLineEdfaNr':pmoabphcsAlmLineEdfaNr,'pmoabphcsAlmLineEdfaTecFail':pmoabphcsAlmLineEdfaTecFail,'pmoabphcsAlmLineEdfaLaserFail':pmoabphcsAlmLineEdfaLaserFail,'pmoabphcsAlmLineEdfaLos':pmoabphcsAlmLineEdfaLos,'pmoabphcsAlmLineExtPumpEdfaLowCurrent':pmoabphcsAlmLineExtPumpEdfaLowCurrent,'pmoabphcsAlmLineGainOutOfRange':pmoabphcsAlmLineGainOutOfRange,'pmoabphcsAlmlineMsaAlarms':pmoabphcsAlmlineMsaAlarms,'pmoabphcsAlmLineMsaLos':pmoabphcsAlmLineMsaLos,'pmoabphcsAlmLineMsaAttenuation':pmoabphcsAlmLineMsaAttenuation,'pmoabphcsAlmlineOscAlarmsTable':pmoabphcsAlmlineOscAlarmsTable,'pmoabphcsAlmlineOscAlarmsEntry':pmoabphcsAlmlineOscAlarmsEntry,_P:pmoabphcsAlmlineOscAlarmsIndex,'pmoabphcsAlmLineLosPortn':pmoabphcsAlmLineLosPortn,'pmoabphcsAlmLineTxOffPortn':pmoabphcsAlmLineTxOffPortn,'pmoabphcsAlmLineTxFailPortn':pmoabphcsAlmLineTxFailPortn,'pmoabphcsAlmLineFecFailPortn':pmoabphcsAlmLineFecFailPortn,'pmoabphcsAlmLineOosPortn':pmoabphcsAlmLineOosPortn,'pmoabphcsAlmLineLofPortn':pmoabphcsAlmLineLofPortn,'pmoabphcsAlmLineOofPortn':pmoabphcsAlmLineOofPortn,'pmoabphcsAlmLineRemoteTxFailPortn':pmoabphcsAlmLineRemoteTxFailPortn,'pmoabphcsAlmLineWarningPortn':pmoabphcsAlmLineWarningPortn,'pmoabphcsAlmLineAlmPortn':pmoabphcsAlmLineAlmPortn,'pmoabphcsAlmlineOscThresholdAlarmsTable':pmoabphcsAlmlineOscThresholdAlarmsTable,'pmoabphcsAlmlineOscThresholdAlarmsEntry':pmoabphcsAlmlineOscThresholdAlarmsEntry,_Q:pmoabphcsAlmlineOscThresholdAlarmsIndex,'pmoabphcsAlmLineTxPwrLowAlarmPortn':pmoabphcsAlmLineTxPwrLowAlarmPortn,'pmoabphcsAlmLineTxPwrHighAlarmPortn':pmoabphcsAlmLineTxPwrHighAlarmPortn,'pmoabphcsAlmLineRxPwrLowAlarmPortn':pmoabphcsAlmLineRxPwrLowAlarmPortn,'pmoabphcsAlmLineRxPwrHighAlarmPortn':pmoabphcsAlmLineRxPwrHighAlarmPortn,'pmoabphcsAlmLineSpanlossLowAlarmPortn':pmoabphcsAlmLineSpanlossLowAlarmPortn,'pmoabphcsAlmLineSpanlossHighAlarmPortn':pmoabphcsAlmLineSpanlossHighAlarmPortn,'pmoabphcsAlmLineOscBiasLowAlarmPortn':pmoabphcsAlmLineOscBiasLowAlarmPortn,'pmoabphcsAlmLineOscBiasHighAlarmPortn':pmoabphcsAlmLineOscBiasHighAlarmPortn,'pmoabphcsAlmlineOscThresholdsWarningsTable':pmoabphcsAlmlineOscThresholdsWarningsTable,'pmoabphcsAlmlineOscThresholdsWarningsEntry':pmoabphcsAlmlineOscThresholdsWarningsEntry,_R:pmoabphcsAlmlineOscThresholdsWarningsIndex,'pmoabphcsAlmLineTxPwrLowWarningPortn':pmoabphcsAlmLineTxPwrLowWarningPortn,'pmoabphcsAlmLineTxPwrHighWarningPortn':pmoabphcsAlmLineTxPwrHighWarningPortn,'pmoabphcsAlmLineRxPwrLowWarningPortn':pmoabphcsAlmLineRxPwrLowWarningPortn,'pmoabphcsAlmLineRxPwrHighWarningPortn':pmoabphcsAlmLineRxPwrHighWarningPortn,'pmoabphcsAlmLineSpanlossLowWarningPortn':pmoabphcsAlmLineSpanlossLowWarningPortn,'pmoabphcsAlmLineSpanlossHighWarningPortn':pmoabphcsAlmLineSpanlossHighWarningPortn,'pmoabphcsAlmLineOscBiasLowWarningPortn':pmoabphcsAlmLineOscBiasLowWarningPortn,'pmoabphcsAlmLineOscBiasHighWarningPortn':pmoabphcsAlmLineOscBiasHighWarningPortn,'pmoabphcsmeasures':pmoabphcsmeasures,'pmoabphcsMesrOther':pmoabphcsMesrOther,'pmoabphcsMesrtempMeas':pmoabphcsMesrtempMeas,'pmoabphcsMesrClient':pmoabphcsMesrClient,'pmoabphcsMesrclientEdfaBiasMeas':pmoabphcsMesrclientEdfaBiasMeas,'pmoabphcsMesrclientEdfaTxpwrMeas':pmoabphcsMesrclientEdfaTxpwrMeas,'pmoabphcsMesrclientEdfaRxpwrMeas':pmoabphcsMesrclientEdfaRxpwrMeas,'pmoabphcsMesrclientEdfaGainMeas':pmoabphcsMesrclientEdfaGainMeas,'pmoabphcsMesrclientOscSpanLoss':pmoabphcsMesrclientOscSpanLoss,'pmoabphcsMesrclientOscSpanLossRef':pmoabphcsMesrclientOscSpanLossRef,'pmoabphcsMesrclientCorrectedGain':pmoabphcsMesrclientCorrectedGain,'pmoabphcsMesrclientMsaInputPower':pmoabphcsMesrclientMsaInputPower,'pmoabphcsMesrclientMsaOutputPower':pmoabphcsMesrclientMsaOutputPower,'pmoabphcsMesrclientMsaAttenuation':pmoabphcsMesrclientMsaAttenuation,'pmoabphcsMesrclientMsaAttenuationRef':pmoabphcsMesrclientMsaAttenuationRef,'pmoabphcsMesrLine':pmoabphcsMesrLine,'pmoabphcsMesrlineEdfaBiasMeas':pmoabphcsMesrlineEdfaBiasMeas,'pmoabphcsMesrlineEdfaTxpwrMeas':pmoabphcsMesrlineEdfaTxpwrMeas,'pmoabphcsMesrlineEdfaRxpwrMeas':pmoabphcsMesrlineEdfaRxpwrMeas,'pmoabphcsMesrlineEdfaGainMeas':pmoabphcsMesrlineEdfaGainMeas,'pmoabphcsMesrlineOscSpanLoss':pmoabphcsMesrlineOscSpanLoss,'pmoabphcsMesrlineOscSpanLossRef':pmoabphcsMesrlineOscSpanLossRef,'pmoabphcsMesrlineCorrectedGain':pmoabphcsMesrlineCorrectedGain,'pmoabphcsMesrlineMsaInputPower':pmoabphcsMesrlineMsaInputPower,'pmoabphcsMesrlineMsaOutputPower':pmoabphcsMesrlineMsaOutputPower,'pmoabphcsMesrlineMsaAttenuation':pmoabphcsMesrlineMsaAttenuation,'pmoabphcsMesrlineMsaAttenuationRef':pmoabphcsMesrlineMsaAttenuationRef,'pmoabphcsMesrlineOscTxPowerTable':pmoabphcsMesrlineOscTxPowerTable,'pmoabphcsMesrlineOscTxPowerEntry':pmoabphcsMesrlineOscTxPowerEntry,_S:pmoabphcsMesrlineOscTxPowerIndex,'pmoabphcsMesrlineOscTxPowerPortn':pmoabphcsMesrlineOscTxPowerPortn,'pmoabphcsMesrlineOscRxPowerTable':pmoabphcsMesrlineOscRxPowerTable,'pmoabphcsMesrlineOscRxPowerEntry':pmoabphcsMesrlineOscRxPowerEntry,_T:pmoabphcsMesrlineOscRxPowerIndex,'pmoabphcsMesrlineOscRxPowerPortn':pmoabphcsMesrlineOscRxPowerPortn,'pmoabphcscounters':pmoabphcscounters,'pmoabphcsCntOther':pmoabphcsCntOther,'pmoabphcsCntClient':pmoabphcsCntClient,'pmoabphcsCntLine':pmoabphcsCntLine,'pmoabphcsCntlineOscErrTable':pmoabphcsCntlineOscErrTable,'pmoabphcsCntlineOscErrEntry':pmoabphcsCntlineOscErrEntry,_U:pmoabphcsCntlineOscErrIndex,'pmoabphcsCntlineOscErrValuePortn':pmoabphcsCntlineOscErrValuePortn,'pmoabphcsCntlineOscErrErrorPortn':pmoabphcsCntlineOscErrErrorPortn,'pmoabphcsCntlineOscErrOverloadPortn':pmoabphcsCntlineOscErrOverloadPortn,'pmoabphcsCntCountersReset':pmoabphcsCntCountersReset,'pmoabphcsCntCountersStop':pmoabphcsCntCountersStop,'pmoabphcscontrolsWrite':pmoabphcscontrolsWrite,'pmoabphcsCtrlOther':pmoabphcsCtrlOther,'pmoabphcsCtrlsynth0':pmoabphcsCtrlsynth0,'pmoabphcsCtrlConfLoad':pmoabphcsCtrlConfLoad,'pmoabphcsCtrlConfFlash':pmoabphcsCtrlConfFlash,'pmoabphcsCtrlConfClear':pmoabphcsCtrlConfClear,'pmoabphcsCtrlswMgnt':pmoabphcsCtrlswMgnt,'pmoabphcsCtrlColdReset':pmoabphcsCtrlColdReset,'pmoabphcsCtrlWarmReset':pmoabphcsCtrlWarmReset,'pmoabphcsCtrlledTest':pmoabphcsCtrlledTest,'pmoabphcsCtrlGreenLed':pmoabphcsCtrlGreenLed,'pmoabphcsCtrlRedLed':pmoabphcsCtrlRedLed,'pmoabphcsCtrlLedOff':pmoabphcsCtrlLedOff,'pmoabphcsCtrlmaintMode':pmoabphcsCtrlmaintMode,'pmoabphcsCtrlMaintenance':pmoabphcsCtrlMaintenance,'pmoabphcsCtrlaprRestart':pmoabphcsCtrlaprRestart,'pmoabphcsCtrlAprManualRestart':pmoabphcsCtrlAprManualRestart,'pmoabphcsCtrlClient':pmoabphcsCtrlClient,'pmoabphcsCtrlclientOscInputSpanLoss':pmoabphcsCtrlclientOscInputSpanLoss,'pmoabphcsCtrlClientSpanLoss':pmoabphcsCtrlClientSpanLoss,'pmoabphcsCtrlclientGainCstMonitorValue':pmoabphcsCtrlclientGainCstMonitorValue,'pmoabphcsCtrlclientGainSettingValue':pmoabphcsCtrlclientGainSettingValue,'pmoabphcsCtrlclientGainProcessing':pmoabphcsCtrlclientGainProcessing,'pmoabphcsCtrlClientGainProc':pmoabphcsCtrlClientGainProc,'pmoabphcsCtrlclientGainCstFiberAgingMarginValue':pmoabphcsCtrlclientGainCstFiberAgingMarginValue,'pmoabphcsCtrlclientMsaAttenuationValue':pmoabphcsCtrlclientMsaAttenuationValue,'pmoabphcsCtrlClientAttenuation':pmoabphcsCtrlClientAttenuation,'pmoabphcsCtrlLine':pmoabphcsCtrlLine,'pmoabphcsCtrllineOscInputSpanLoss':pmoabphcsCtrllineOscInputSpanLoss,'pmoabphcsCtrlLineSpanLoss':pmoabphcsCtrlLineSpanLoss,'pmoabphcsCtrllineGainCstMonitorValue':pmoabphcsCtrllineGainCstMonitorValue,'pmoabphcsCtrllineGainSettingValue':pmoabphcsCtrllineGainSettingValue,'pmoabphcsCtrllineGainProcessing':pmoabphcsCtrllineGainProcessing,'pmoabphcsCtrlLineGainProc':pmoabphcsCtrlLineGainProc,'pmoabphcsCtrllineGainCstFiberAgingMarginValue':pmoabphcsCtrllineGainCstFiberAgingMarginValue,'pmoabphcsCtrllineMsaAttenuationValue':pmoabphcsCtrllineMsaAttenuationValue,'pmoabphcsCtrlLineAttenuation':pmoabphcsCtrlLineAttenuation,'pmoabphcsri':pmoabphcsri,'pmoabphcsRinvReloadInventory':pmoabphcsRinvReloadInventory,'pmoabphcsRinvHwPlatform':pmoabphcsRinvHwPlatform,'pmoabphcsRinvModulePlatform':pmoabphcsRinvModulePlatform,'pmoabphcsRinvSwPlatform':pmoabphcsRinvSwPlatform,'pmoabphcsRinvGwPlatform':pmoabphcsRinvGwPlatform,'pmoabphcsRinvBoosterTable':pmoabphcsRinvBoosterTable,'pmoabphcsRinvBoosterEntry':pmoabphcsRinvBoosterEntry,_V:pmoabphcsRinvBoosterIndex,'pmoabphcsRinvBooster':pmoabphcsRinvBooster,'pmoabphcsRinvPreAmpTable':pmoabphcsRinvPreAmpTable,'pmoabphcsRinvPreAmpEntry':pmoabphcsRinvPreAmpEntry,_W:pmoabphcsRinvPreAmpIndex,'pmoabphcsRinvPreAmp':pmoabphcsRinvPreAmp,'pmoabphcsConfig':pmoabphcsConfig,'pmoabphcsCfgNoValue':pmoabphcsCfgNoValue,'pmoabphcstableclientStartup':pmoabphcstableclientStartup,'pmoabphcsCfgclientEdfaLaserCtrl':pmoabphcsCfgclientEdfaLaserCtrl,'pmoabphcsCfgclientEdfaLaserMode':pmoabphcsCfgclientEdfaLaserMode,'pmoabphcsCfgclientGainValue':pmoabphcsCfgclientGainValue,'pmoabphcsCfgclientTiltValue':pmoabphcsCfgclientTiltValue,'pmoabphcsCfgclientMsaLoss':pmoabphcsCfgclientMsaLoss,'pmoabphcsCfgclientOutputPowerValue':pmoabphcsCfgclientOutputPowerValue,'pmoabphcsCfgclientAseCompensation':pmoabphcsCfgclientAseCompensation,'pmoabphcsCfgLineStartUp':pmoabphcsCfgLineStartUp,'pmoabphcstablelineStartup':pmoabphcstablelineStartup,'pmoabphcsCfglineEdfaLaserCtrl':pmoabphcsCfglineEdfaLaserCtrl,'pmoabphcsCfglineEdfaLaserMode':pmoabphcsCfglineEdfaLaserMode,'pmoabphcsCfglineGainValue':pmoabphcsCfglineGainValue,'pmoabphcsCfglineTiltValue':pmoabphcsCfglineTiltValue,'pmoabphcsCfglineMsaLoss':pmoabphcsCfglineMsaLoss,'pmoabphcsCfglineOutputPowerValue':pmoabphcsCfglineOutputPowerValue,'pmoabphcsCfglineAseCompensation':pmoabphcsCfglineAseCompensation,'pmoabphcsCfgaprMode':pmoabphcsCfgaprMode,'pmoabphcsCfgClientSupvStartUp':pmoabphcsCfgClientSupvStartUp,'pmoabphcsCfgLineStartupTable':pmoabphcsCfgLineStartupTable,'pmoabphcsCfgLineStartupEntry':pmoabphcsCfgLineStartupEntry,_X:pmoabphcsCfgLineStartupIndex,'pmoabphcsCfgLineOscLaserCtrlPortn':pmoabphcsCfgLineOscLaserCtrlPortn,'pmoabphcsCfgLineOscOosPortn':pmoabphcsCfgLineOscOosPortn,'pmoabphcsCfgLineOscSpanLengthPortn':pmoabphcsCfgLineOscSpanLengthPortn,'pmoabphcsCfgLineOscCorrectionFactorPortn':pmoabphcsCfgLineOscCorrectionFactorPortn,'pmoabphcsCfgLabels':pmoabphcsCfgLabels,'pmoabphcsCfgLabelclientTable':pmoabphcsCfgLabelclientTable,'pmoabphcsCfgLabelclientEntry':pmoabphcsCfgLabelclientEntry,_Y:pmoabphcsCfgLabelclientIndex,'pmoabphcsCfgLabelclientPortn':pmoabphcsCfgLabelclientPortn,'pmoabphcsCfgLabellineTable':pmoabphcsCfgLabellineTable,'pmoabphcsCfgLabellineEntry':pmoabphcsCfgLabellineEntry,_Z:pmoabphcsCfgLabellineIndex,'pmoabphcsCfgLabellinePortn':pmoabphcsCfgLabellinePortn,'pmoabphcsCfgWriteConfiguration':pmoabphcsCfgWriteConfiguration,'pmoabphcstraps':pmoabphcstraps,_G:pmoabphcstrapBoardNumber,'pmoabphcsLineTrapCritGoesOn':pmoabphcsLineTrapCritGoesOn,'pmoabphcsLineTrapCritGoesOff':pmoabphcsLineTrapCritGoesOff,'pmoabphcsClientTrapCritGoesOn':pmoabphcsClientTrapCritGoesOn,'pmoabphcsClientTrapCritGoesOff':pmoabphcsClientTrapCritGoesOff,'pmoabphcsPowerTrapUrgentGoesOn':pmoabphcsPowerTrapUrgentGoesOn,'pmoabphcsPowerTrapUrgentGoesOff':pmoabphcsPowerTrapUrgentGoesOff})