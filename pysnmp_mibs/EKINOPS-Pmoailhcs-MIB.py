_Z='pmoailhcsCfgLabellineIndex'
_Y='pmoailhcsCfgLabelclientIndex'
_X='pmoailhcsCfgLineStartupIndex'
_W='pmoailhcsRinvPreAmpIndex'
_V='pmoailhcsRinvBoosterIndex'
_U='pmoailhcsCntlineOscErrIndex'
_T='pmoailhcsMesrlineOscRxPowerIndex'
_S='pmoailhcsMesrlineOscTxPowerIndex'
_R='pmoailhcsAlmlineOscThresholdsWarningsIndex'
_Q='pmoailhcsAlmlineOscThresholdAlarmsIndex'
_P='pmoailhcsAlmlineOscAlarmsIndex'
_O='2014-06-20 00:00'
_N='pmoailhcsAlmDefFuseA'
_M='pmoailhcsAlmDefFuseB'
_L='pmoailhcsAlmClientHwFail'
_K='pmoailhcsAlmClientFail'
_J='pmoailhcsAlmLineHwFail'
_I='pmoailhcsAlmLineFail'
_H='DisplayString'
_G='pmoailhcstrapBoardNumber'
_F='Unsigned32'
_E='EKINOPS-Pmoailhcs-MIB'
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
modulepmoailhcs=ModuleIdentity((1,3,6,1,4,1,20044,62))
if mibBuilder.loadTexts:modulepmoailhcs.setRevisions((_O,_O,'2015-01-27 00:00','2016-05-23 00:00'))
class PmoailhcspreampMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oailhcspreampdefaultmode',0),('oailhcspreampconstantcurrentmode',1),('oailhcspreampconstantpowermode',2),('oailhcspreampconstantgainmode',3),('oailhcspreamppoutpinmode',4),('oailhcspreampmanualmode',5),('oailhcspreampfeedforwardmode',6),('oailhcspreamptransientsupmode',7)))
class PmoailhcsboosterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('oailhcsboosterdefaultmode',0),('oailhcsboosterconstantcurrentmode',1),('oailhcsboosterconstantpowermode',2),('oailhcsboosterconstantgainmode',3),('oailhcsboosterpoutpinmode',4),('oailhcsboostermanualmode',5),('oailhcsboosterfeedforwardmode',6),('oailhcsboostertransientsupmode',7)))
class PmoailhcsaprMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('oailhcsaproffmode',0),('oailhcsaprsemiautomode',1),('oailhcsaprautomode',2),('oailhcsaprlossforwardingmode',3),('oailhcsaprrepeatmode',4)))
class PmoailhcsPreampGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oailhcspreampgainadjmanualmode',0),('oailhcspreampgainadjsemiautomode',1),('oailhcspreampgainadjautomode',2)))
class PmoailhcsBoosterGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('oailhcsboostergainadjmanualmode',0),('oailhcsboostergainadjsemiautomode',1),('oailhcsboostergainadjautomode',2)))
class PmoailhcsPreampCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oailhcspreampcstgainadjsemiautomode',1),('oailhcspreampcstgainadjautomode',2)))
class PmoailhcsBoosterCstGainAdjMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oailhcsboostercstgainadjsemiautomode',1),('oailhcsboostercstgainadjautomode',2)))
_Pmoailhcsalarms_ObjectIdentity=ObjectIdentity
pmoailhcsalarms=_Pmoailhcsalarms_ObjectIdentity((1,3,6,1,4,1,20044,62,2))
_PmoailhcsAlmOther_ObjectIdentity=ObjectIdentity
pmoailhcsAlmOther=_PmoailhcsAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1))
_PmoailhcsAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmoailhcsAlmOtherNurg=_PmoailhcsAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,1))
_PmoailhcsAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmoailhcsAlmsynthAlm2=_PmoailhcsAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,1,2))
_PmoailhcsAlmConfTableSave_Type=EkiOnOff
_PmoailhcsAlmConfTableSave_Object=MibScalar
pmoailhcsAlmConfTableSave=_PmoailhcsAlmConfTableSave_Object((1,3,6,1,4,1,20044,62,2,1,1,2,1),_PmoailhcsAlmConfTableSave_Type())
pmoailhcsAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmConfTableSave.setStatus(_A)
_PmoailhcsAlmInvUpload_Type=EkiOnOff
_PmoailhcsAlmInvUpload_Object=MibScalar
pmoailhcsAlmInvUpload=_PmoailhcsAlmInvUpload_Object((1,3,6,1,4,1,20044,62,2,1,1,2,2),_PmoailhcsAlmInvUpload_Type())
pmoailhcsAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmInvUpload.setStatus(_A)
_PmoailhcsAlmConfTableLoad_Type=EkiOnOff
_PmoailhcsAlmConfTableLoad_Object=MibScalar
pmoailhcsAlmConfTableLoad=_PmoailhcsAlmConfTableLoad_Object((1,3,6,1,4,1,20044,62,2,1,1,2,3),_PmoailhcsAlmConfTableLoad_Type())
pmoailhcsAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmConfTableLoad.setStatus(_A)
_PmoailhcsAlmfoaWarnings_ObjectIdentity=ObjectIdentity
pmoailhcsAlmfoaWarnings=_PmoailhcsAlmfoaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,1,75))
_PmoailhcsAlmTermpLowWarning_Type=EkiOnOff
_PmoailhcsAlmTermpLowWarning_Object=MibScalar
pmoailhcsAlmTermpLowWarning=_PmoailhcsAlmTermpLowWarning_Object((1,3,6,1,4,1,20044,62,2,1,1,75,7),_PmoailhcsAlmTermpLowWarning_Type())
pmoailhcsAlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmTermpLowWarning.setStatus(_A)
_PmoailhcsAlmTempHighWarning_Type=EkiOnOff
_PmoailhcsAlmTempHighWarning_Object=MibScalar
pmoailhcsAlmTempHighWarning=_PmoailhcsAlmTempHighWarning_Object((1,3,6,1,4,1,20044,62,2,1,1,75,8),_PmoailhcsAlmTempHighWarning_Type())
pmoailhcsAlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmTempHighWarning.setStatus(_A)
_PmoailhcsAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmoailhcsAlmOtherUrg=_PmoailhcsAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,2))
_PmoailhcsAlmfoaAlarms_ObjectIdentity=ObjectIdentity
pmoailhcsAlmfoaAlarms=_PmoailhcsAlmfoaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,2,74))
_PmoailhcsAlmTermpLowAlarm_Type=EkiOnOff
_PmoailhcsAlmTermpLowAlarm_Object=MibScalar
pmoailhcsAlmTermpLowAlarm=_PmoailhcsAlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,62,2,1,2,74,7),_PmoailhcsAlmTermpLowAlarm_Type())
pmoailhcsAlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmTermpLowAlarm.setStatus(_A)
_PmoailhcsAlmTempHighAlarm_Type=EkiOnOff
_PmoailhcsAlmTempHighAlarm_Object=MibScalar
pmoailhcsAlmTempHighAlarm=_PmoailhcsAlmTempHighAlarm_Object((1,3,6,1,4,1,20044,62,2,1,2,74,8),_PmoailhcsAlmTempHighAlarm_Type())
pmoailhcsAlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmTempHighAlarm.setStatus(_A)
_PmoailhcsAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmoailhcsAlmOtherCrit=_PmoailhcsAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,3))
_PmoailhcsAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmoailhcsAlmsynthAlm0=_PmoailhcsAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,62,2,1,3,0))
_PmoailhcsAlmMaintenanceMode_Type=EkiOnOff
_PmoailhcsAlmMaintenanceMode_Object=MibScalar
pmoailhcsAlmMaintenanceMode=_PmoailhcsAlmMaintenanceMode_Object((1,3,6,1,4,1,20044,62,2,1,3,0,1),_PmoailhcsAlmMaintenanceMode_Type())
pmoailhcsAlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmMaintenanceMode.setStatus(_A)
_PmoailhcsAlmAprOn_Type=EkiOnOff
_PmoailhcsAlmAprOn_Object=MibScalar
pmoailhcsAlmAprOn=_PmoailhcsAlmAprOn_Object((1,3,6,1,4,1,20044,62,2,1,3,0,2),_PmoailhcsAlmAprOn_Type())
pmoailhcsAlmAprOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmAprOn.setStatus(_A)
_PmoailhcsAlmModGlobFail_Type=EkiOnOff
_PmoailhcsAlmModGlobFail_Object=MibScalar
pmoailhcsAlmModGlobFail=_PmoailhcsAlmModGlobFail_Object((1,3,6,1,4,1,20044,62,2,1,3,0,9),_PmoailhcsAlmModGlobFail_Type())
pmoailhcsAlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmModGlobFail.setStatus(_A)
_PmoailhcsAlmUpEdfaInitNotCompl_Type=EkiOnOff
_PmoailhcsAlmUpEdfaInitNotCompl_Object=MibScalar
pmoailhcsAlmUpEdfaInitNotCompl=_PmoailhcsAlmUpEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,62,2,1,3,0,10),_PmoailhcsAlmUpEdfaInitNotCompl_Type())
pmoailhcsAlmUpEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmUpEdfaInitNotCompl.setStatus(_A)
_PmoailhcsAlmDwEdfaInitNotCompl_Type=EkiOnOff
_PmoailhcsAlmDwEdfaInitNotCompl_Object=MibScalar
pmoailhcsAlmDwEdfaInitNotCompl=_PmoailhcsAlmDwEdfaInitNotCompl_Object((1,3,6,1,4,1,20044,62,2,1,3,0,11),_PmoailhcsAlmDwEdfaInitNotCompl_Type())
pmoailhcsAlmDwEdfaInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmDwEdfaInitNotCompl.setStatus(_A)
_PmoailhcsAlmExtPump1NotLocked_Type=EkiOnOff
_PmoailhcsAlmExtPump1NotLocked_Object=MibScalar
pmoailhcsAlmExtPump1NotLocked=_PmoailhcsAlmExtPump1NotLocked_Object((1,3,6,1,4,1,20044,62,2,1,3,0,12),_PmoailhcsAlmExtPump1NotLocked_Type())
pmoailhcsAlmExtPump1NotLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmExtPump1NotLocked.setStatus(_A)
_PmoailhcsAlmDefFuseA_Type=EkiOnOff
_PmoailhcsAlmDefFuseA_Object=MibScalar
pmoailhcsAlmDefFuseA=_PmoailhcsAlmDefFuseA_Object((1,3,6,1,4,1,20044,62,2,1,3,0,15),_PmoailhcsAlmDefFuseA_Type())
pmoailhcsAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmDefFuseA.setStatus(_A)
_PmoailhcsAlmDefFuseB_Type=EkiOnOff
_PmoailhcsAlmDefFuseB_Object=MibScalar
pmoailhcsAlmDefFuseB=_PmoailhcsAlmDefFuseB_Object((1,3,6,1,4,1,20044,62,2,1,3,0,16),_PmoailhcsAlmDefFuseB_Type())
pmoailhcsAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmDefFuseB.setStatus(_A)
_PmoailhcsAlmClient_ObjectIdentity=ObjectIdentity
pmoailhcsAlmClient=_PmoailhcsAlmClient_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2))
_PmoailhcsAlmClientNurg_ObjectIdentity=ObjectIdentity
pmoailhcsAlmClientNurg=_PmoailhcsAlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,1))
_PmoailhcsAlmclientEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoailhcsAlmclientEdfaWarnings=_PmoailhcsAlmclientEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,1,33))
_PmoailhcsAlmClientGainLowWarning_Type=EkiOnOff
_PmoailhcsAlmClientGainLowWarning_Object=MibScalar
pmoailhcsAlmClientGainLowWarning=_PmoailhcsAlmClientGainLowWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,1),_PmoailhcsAlmClientGainLowWarning_Type())
pmoailhcsAlmClientGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientGainLowWarning.setStatus(_A)
_PmoailhcsAlmClientGainHighWarning_Type=EkiOnOff
_PmoailhcsAlmClientGainHighWarning_Object=MibScalar
pmoailhcsAlmClientGainHighWarning=_PmoailhcsAlmClientGainHighWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,2),_PmoailhcsAlmClientGainHighWarning_Type())
pmoailhcsAlmClientGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientGainHighWarning.setStatus(_A)
_PmoailhcsAlmClientInputPwrLowWarning_Type=EkiOnOff
_PmoailhcsAlmClientInputPwrLowWarning_Object=MibScalar
pmoailhcsAlmClientInputPwrLowWarning=_PmoailhcsAlmClientInputPwrLowWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,3),_PmoailhcsAlmClientInputPwrLowWarning_Type())
pmoailhcsAlmClientInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientInputPwrLowWarning.setStatus(_A)
_PmoailhcsAlmClientInputPwrHighWarning_Type=EkiOnOff
_PmoailhcsAlmClientInputPwrHighWarning_Object=MibScalar
pmoailhcsAlmClientInputPwrHighWarning=_PmoailhcsAlmClientInputPwrHighWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,4),_PmoailhcsAlmClientInputPwrHighWarning_Type())
pmoailhcsAlmClientInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientInputPwrHighWarning.setStatus(_A)
_PmoailhcsAlmClientOutputPwrLowWarning_Type=EkiOnOff
_PmoailhcsAlmClientOutputPwrLowWarning_Object=MibScalar
pmoailhcsAlmClientOutputPwrLowWarning=_PmoailhcsAlmClientOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,5),_PmoailhcsAlmClientOutputPwrLowWarning_Type())
pmoailhcsAlmClientOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientOutputPwrLowWarning.setStatus(_A)
_PmoailhcsAlmClientOutputPwrHighWarning_Type=EkiOnOff
_PmoailhcsAlmClientOutputPwrHighWarning_Object=MibScalar
pmoailhcsAlmClientOutputPwrHighWarning=_PmoailhcsAlmClientOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,6),_PmoailhcsAlmClientOutputPwrHighWarning_Type())
pmoailhcsAlmClientOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientOutputPwrHighWarning.setStatus(_A)
_PmoailhcsAlmClientBiasLowWarning_Type=EkiOnOff
_PmoailhcsAlmClientBiasLowWarning_Object=MibScalar
pmoailhcsAlmClientBiasLowWarning=_PmoailhcsAlmClientBiasLowWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,7),_PmoailhcsAlmClientBiasLowWarning_Type())
pmoailhcsAlmClientBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientBiasLowWarning.setStatus(_A)
_PmoailhcsAlmClientBiasHighWarning_Type=EkiOnOff
_PmoailhcsAlmClientBiasHighWarning_Object=MibScalar
pmoailhcsAlmClientBiasHighWarning=_PmoailhcsAlmClientBiasHighWarning_Object((1,3,6,1,4,1,20044,62,2,2,1,33,8),_PmoailhcsAlmClientBiasHighWarning_Type())
pmoailhcsAlmClientBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientBiasHighWarning.setStatus(_A)
_PmoailhcsAlmClientUrg_ObjectIdentity=ObjectIdentity
pmoailhcsAlmClientUrg=_PmoailhcsAlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,2))
_PmoailhcsAlmclientEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoailhcsAlmclientEdfaAlarms1=_PmoailhcsAlmclientEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,2,32))
_PmoailhcsAlmClientGainLowAlarm_Type=EkiOnOff
_PmoailhcsAlmClientGainLowAlarm_Object=MibScalar
pmoailhcsAlmClientGainLowAlarm=_PmoailhcsAlmClientGainLowAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,1),_PmoailhcsAlmClientGainLowAlarm_Type())
pmoailhcsAlmClientGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientGainLowAlarm.setStatus(_A)
_PmoailhcsAlmClientGainHighAlarm_Type=EkiOnOff
_PmoailhcsAlmClientGainHighAlarm_Object=MibScalar
pmoailhcsAlmClientGainHighAlarm=_PmoailhcsAlmClientGainHighAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,2),_PmoailhcsAlmClientGainHighAlarm_Type())
pmoailhcsAlmClientGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientGainHighAlarm.setStatus(_A)
_PmoailhcsAlmClientInputPwrLowAlarm_Type=EkiOnOff
_PmoailhcsAlmClientInputPwrLowAlarm_Object=MibScalar
pmoailhcsAlmClientInputPwrLowAlarm=_PmoailhcsAlmClientInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,3),_PmoailhcsAlmClientInputPwrLowAlarm_Type())
pmoailhcsAlmClientInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientInputPwrLowAlarm.setStatus(_A)
_PmoailhcsAlmClientInputPwrHighAlarm_Type=EkiOnOff
_PmoailhcsAlmClientInputPwrHighAlarm_Object=MibScalar
pmoailhcsAlmClientInputPwrHighAlarm=_PmoailhcsAlmClientInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,4),_PmoailhcsAlmClientInputPwrHighAlarm_Type())
pmoailhcsAlmClientInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientInputPwrHighAlarm.setStatus(_A)
_PmoailhcsAlmClientOutputPwrLowAlarm_Type=EkiOnOff
_PmoailhcsAlmClientOutputPwrLowAlarm_Object=MibScalar
pmoailhcsAlmClientOutputPwrLowAlarm=_PmoailhcsAlmClientOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,5),_PmoailhcsAlmClientOutputPwrLowAlarm_Type())
pmoailhcsAlmClientOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientOutputPwrLowAlarm.setStatus(_A)
_PmoailhcsAlmClientOutputPwrHighAlarm_Type=EkiOnOff
_PmoailhcsAlmClientOutputPwrHighAlarm_Object=MibScalar
pmoailhcsAlmClientOutputPwrHighAlarm=_PmoailhcsAlmClientOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,6),_PmoailhcsAlmClientOutputPwrHighAlarm_Type())
pmoailhcsAlmClientOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientOutputPwrHighAlarm.setStatus(_A)
_PmoailhcsAlmClientBiasLowAlarm_Type=EkiOnOff
_PmoailhcsAlmClientBiasLowAlarm_Object=MibScalar
pmoailhcsAlmClientBiasLowAlarm=_PmoailhcsAlmClientBiasLowAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,7),_PmoailhcsAlmClientBiasLowAlarm_Type())
pmoailhcsAlmClientBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientBiasLowAlarm.setStatus(_A)
_PmoailhcsAlmClientBiasHighAlarm_Type=EkiOnOff
_PmoailhcsAlmClientBiasHighAlarm_Object=MibScalar
pmoailhcsAlmClientBiasHighAlarm=_PmoailhcsAlmClientBiasHighAlarm_Object((1,3,6,1,4,1,20044,62,2,2,2,32,8),_PmoailhcsAlmClientBiasHighAlarm_Type())
pmoailhcsAlmClientBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientBiasHighAlarm.setStatus(_A)
_PmoailhcsAlmClientCrit_ObjectIdentity=ObjectIdentity
pmoailhcsAlmClientCrit=_PmoailhcsAlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,3))
_PmoailhcsAlmsynthAlm8_ObjectIdentity=ObjectIdentity
pmoailhcsAlmsynthAlm8=_PmoailhcsAlmsynthAlm8_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,3,8))
_PmoailhcsAlmClientHwFail_Type=EkiOnOff
_PmoailhcsAlmClientHwFail_Object=MibScalar
pmoailhcsAlmClientHwFail=_PmoailhcsAlmClientHwFail_Object((1,3,6,1,4,1,20044,62,2,2,3,8,4),_PmoailhcsAlmClientHwFail_Type())
pmoailhcsAlmClientHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientHwFail.setStatus(_A)
_PmoailhcsAlmClientTxOff_Type=EkiOnOff
_PmoailhcsAlmClientTxOff_Object=MibScalar
pmoailhcsAlmClientTxOff=_PmoailhcsAlmClientTxOff_Object((1,3,6,1,4,1,20044,62,2,2,3,8,5),_PmoailhcsAlmClientTxOff_Type())
pmoailhcsAlmClientTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientTxOff.setStatus(_A)
_PmoailhcsAlmClientFail_Type=EkiOnOff
_PmoailhcsAlmClientFail_Object=MibScalar
pmoailhcsAlmClientFail=_PmoailhcsAlmClientFail_Object((1,3,6,1,4,1,20044,62,2,2,3,8,12),_PmoailhcsAlmClientFail_Type())
pmoailhcsAlmClientFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientFail.setStatus(_A)
_PmoailhcsAlmClientExtPumpFail_Type=EkiOnOff
_PmoailhcsAlmClientExtPumpFail_Object=MibScalar
pmoailhcsAlmClientExtPumpFail=_PmoailhcsAlmClientExtPumpFail_Object((1,3,6,1,4,1,20044,62,2,2,3,8,13),_PmoailhcsAlmClientExtPumpFail_Type())
pmoailhcsAlmClientExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientExtPumpFail.setStatus(_A)
_PmoailhcsAlmSupvbFail_Type=EkiOnOff
_PmoailhcsAlmSupvbFail_Object=MibScalar
pmoailhcsAlmSupvbFail=_PmoailhcsAlmSupvbFail_Object((1,3,6,1,4,1,20044,62,2,2,3,8,14),_PmoailhcsAlmSupvbFail_Type())
pmoailhcsAlmSupvbFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmSupvbFail.setStatus(_A)
_PmoailhcsAlmclientEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoailhcsAlmclientEdfaAlarms2=_PmoailhcsAlmclientEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,3,35))
_PmoailhcsAlmClientEdfaNr_Type=EkiOnOff
_PmoailhcsAlmClientEdfaNr_Object=MibScalar
pmoailhcsAlmClientEdfaNr=_PmoailhcsAlmClientEdfaNr_Object((1,3,6,1,4,1,20044,62,2,2,3,35,1),_PmoailhcsAlmClientEdfaNr_Type())
pmoailhcsAlmClientEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientEdfaNr.setStatus(_A)
_PmoailhcsAlmClientEdfaTecFail_Type=EkiOnOff
_PmoailhcsAlmClientEdfaTecFail_Object=MibScalar
pmoailhcsAlmClientEdfaTecFail=_PmoailhcsAlmClientEdfaTecFail_Object((1,3,6,1,4,1,20044,62,2,2,3,35,2),_PmoailhcsAlmClientEdfaTecFail_Type())
pmoailhcsAlmClientEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientEdfaTecFail.setStatus(_A)
_PmoailhcsAlmClientEdfaLaserFail_Type=EkiOnOff
_PmoailhcsAlmClientEdfaLaserFail_Object=MibScalar
pmoailhcsAlmClientEdfaLaserFail=_PmoailhcsAlmClientEdfaLaserFail_Object((1,3,6,1,4,1,20044,62,2,2,3,35,3),_PmoailhcsAlmClientEdfaLaserFail_Type())
pmoailhcsAlmClientEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientEdfaLaserFail.setStatus(_A)
_PmoailhcsAlmClientEdfaLos_Type=EkiOnOff
_PmoailhcsAlmClientEdfaLos_Object=MibScalar
pmoailhcsAlmClientEdfaLos=_PmoailhcsAlmClientEdfaLos_Object((1,3,6,1,4,1,20044,62,2,2,3,35,4),_PmoailhcsAlmClientEdfaLos_Type())
pmoailhcsAlmClientEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientEdfaLos.setStatus(_A)
_PmoailhcsAlmClientExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoailhcsAlmClientExtPumpEdfaLowCurrent_Object=MibScalar
pmoailhcsAlmClientExtPumpEdfaLowCurrent=_PmoailhcsAlmClientExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,62,2,2,3,35,5),_PmoailhcsAlmClientExtPumpEdfaLowCurrent_Type())
pmoailhcsAlmClientExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientExtPumpEdfaLowCurrent.setStatus(_A)
_PmoailhcsAlmClientGainOutOfRange_Type=EkiOnOff
_PmoailhcsAlmClientGainOutOfRange_Object=MibScalar
pmoailhcsAlmClientGainOutOfRange=_PmoailhcsAlmClientGainOutOfRange_Object((1,3,6,1,4,1,20044,62,2,2,3,35,6),_PmoailhcsAlmClientGainOutOfRange_Type())
pmoailhcsAlmClientGainOutOfRange.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientGainOutOfRange.setStatus(_A)
_PmoailhcsAlmclientMsaAlarms_ObjectIdentity=ObjectIdentity
pmoailhcsAlmclientMsaAlarms=_PmoailhcsAlmclientMsaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,62,2,2,3,37))
_PmoailhcsAlmClientMsaLos_Type=EkiOnOff
_PmoailhcsAlmClientMsaLos_Object=MibScalar
pmoailhcsAlmClientMsaLos=_PmoailhcsAlmClientMsaLos_Object((1,3,6,1,4,1,20044,62,2,2,3,37,1),_PmoailhcsAlmClientMsaLos_Type())
pmoailhcsAlmClientMsaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientMsaLos.setStatus(_A)
_PmoailhcsAlmClientMsaAttenuation_Type=EkiOnOff
_PmoailhcsAlmClientMsaAttenuation_Object=MibScalar
pmoailhcsAlmClientMsaAttenuation=_PmoailhcsAlmClientMsaAttenuation_Object((1,3,6,1,4,1,20044,62,2,2,3,37,2),_PmoailhcsAlmClientMsaAttenuation_Type())
pmoailhcsAlmClientMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmClientMsaAttenuation.setStatus(_A)
_PmoailhcsAlmLine_ObjectIdentity=ObjectIdentity
pmoailhcsAlmLine=_PmoailhcsAlmLine_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3))
_PmoailhcsAlmLineNurg_ObjectIdentity=ObjectIdentity
pmoailhcsAlmLineNurg=_PmoailhcsAlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,1))
_PmoailhcsAlmlineEdfaWarnings_ObjectIdentity=ObjectIdentity
pmoailhcsAlmlineEdfaWarnings=_PmoailhcsAlmlineEdfaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,1,41))
_PmoailhcsAlmLineGainLowWarning_Type=EkiOnOff
_PmoailhcsAlmLineGainLowWarning_Object=MibScalar
pmoailhcsAlmLineGainLowWarning=_PmoailhcsAlmLineGainLowWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,1),_PmoailhcsAlmLineGainLowWarning_Type())
pmoailhcsAlmLineGainLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineGainLowWarning.setStatus(_A)
_PmoailhcsAlmLineGainHighWarning_Type=EkiOnOff
_PmoailhcsAlmLineGainHighWarning_Object=MibScalar
pmoailhcsAlmLineGainHighWarning=_PmoailhcsAlmLineGainHighWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,2),_PmoailhcsAlmLineGainHighWarning_Type())
pmoailhcsAlmLineGainHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineGainHighWarning.setStatus(_A)
_PmoailhcsAlmLineInputPwrLowWarning_Type=EkiOnOff
_PmoailhcsAlmLineInputPwrLowWarning_Object=MibScalar
pmoailhcsAlmLineInputPwrLowWarning=_PmoailhcsAlmLineInputPwrLowWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,3),_PmoailhcsAlmLineInputPwrLowWarning_Type())
pmoailhcsAlmLineInputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineInputPwrLowWarning.setStatus(_A)
_PmoailhcsAlmLineInputPwrHighWarning_Type=EkiOnOff
_PmoailhcsAlmLineInputPwrHighWarning_Object=MibScalar
pmoailhcsAlmLineInputPwrHighWarning=_PmoailhcsAlmLineInputPwrHighWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,4),_PmoailhcsAlmLineInputPwrHighWarning_Type())
pmoailhcsAlmLineInputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineInputPwrHighWarning.setStatus(_A)
_PmoailhcsAlmLineOutputPwrLowWarning_Type=EkiOnOff
_PmoailhcsAlmLineOutputPwrLowWarning_Object=MibScalar
pmoailhcsAlmLineOutputPwrLowWarning=_PmoailhcsAlmLineOutputPwrLowWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,5),_PmoailhcsAlmLineOutputPwrLowWarning_Type())
pmoailhcsAlmLineOutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOutputPwrLowWarning.setStatus(_A)
_PmoailhcsAlmLineOutputPwrHighWarning_Type=EkiOnOff
_PmoailhcsAlmLineOutputPwrHighWarning_Object=MibScalar
pmoailhcsAlmLineOutputPwrHighWarning=_PmoailhcsAlmLineOutputPwrHighWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,6),_PmoailhcsAlmLineOutputPwrHighWarning_Type())
pmoailhcsAlmLineOutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOutputPwrHighWarning.setStatus(_A)
_PmoailhcsAlmLineBiasLowWarning_Type=EkiOnOff
_PmoailhcsAlmLineBiasLowWarning_Object=MibScalar
pmoailhcsAlmLineBiasLowWarning=_PmoailhcsAlmLineBiasLowWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,7),_PmoailhcsAlmLineBiasLowWarning_Type())
pmoailhcsAlmLineBiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineBiasLowWarning.setStatus(_A)
_PmoailhcsAlmLineBiasHighWarning_Type=EkiOnOff
_PmoailhcsAlmLineBiasHighWarning_Object=MibScalar
pmoailhcsAlmLineBiasHighWarning=_PmoailhcsAlmLineBiasHighWarning_Object((1,3,6,1,4,1,20044,62,2,3,1,41,8),_PmoailhcsAlmLineBiasHighWarning_Type())
pmoailhcsAlmLineBiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineBiasHighWarning.setStatus(_A)
_PmoailhcsAlmLineUrg_ObjectIdentity=ObjectIdentity
pmoailhcsAlmLineUrg=_PmoailhcsAlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,2))
_PmoailhcsAlmlineEdfaAlarms1_ObjectIdentity=ObjectIdentity
pmoailhcsAlmlineEdfaAlarms1=_PmoailhcsAlmlineEdfaAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,2,40))
_PmoailhcsAlmLineGainLowAlarm_Type=EkiOnOff
_PmoailhcsAlmLineGainLowAlarm_Object=MibScalar
pmoailhcsAlmLineGainLowAlarm=_PmoailhcsAlmLineGainLowAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,1),_PmoailhcsAlmLineGainLowAlarm_Type())
pmoailhcsAlmLineGainLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineGainLowAlarm.setStatus(_A)
_PmoailhcsAlmLineGainHighAlarm_Type=EkiOnOff
_PmoailhcsAlmLineGainHighAlarm_Object=MibScalar
pmoailhcsAlmLineGainHighAlarm=_PmoailhcsAlmLineGainHighAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,2),_PmoailhcsAlmLineGainHighAlarm_Type())
pmoailhcsAlmLineGainHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineGainHighAlarm.setStatus(_A)
_PmoailhcsAlmLineInputPwrLowAlarm_Type=EkiOnOff
_PmoailhcsAlmLineInputPwrLowAlarm_Object=MibScalar
pmoailhcsAlmLineInputPwrLowAlarm=_PmoailhcsAlmLineInputPwrLowAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,3),_PmoailhcsAlmLineInputPwrLowAlarm_Type())
pmoailhcsAlmLineInputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineInputPwrLowAlarm.setStatus(_A)
_PmoailhcsAlmLineInputPwrHighAlarm_Type=EkiOnOff
_PmoailhcsAlmLineInputPwrHighAlarm_Object=MibScalar
pmoailhcsAlmLineInputPwrHighAlarm=_PmoailhcsAlmLineInputPwrHighAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,4),_PmoailhcsAlmLineInputPwrHighAlarm_Type())
pmoailhcsAlmLineInputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineInputPwrHighAlarm.setStatus(_A)
_PmoailhcsAlmLineOutputPwrLowAlarm_Type=EkiOnOff
_PmoailhcsAlmLineOutputPwrLowAlarm_Object=MibScalar
pmoailhcsAlmLineOutputPwrLowAlarm=_PmoailhcsAlmLineOutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,5),_PmoailhcsAlmLineOutputPwrLowAlarm_Type())
pmoailhcsAlmLineOutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOutputPwrLowAlarm.setStatus(_A)
_PmoailhcsAlmLineOutputPwrHighAlarm_Type=EkiOnOff
_PmoailhcsAlmLineOutputPwrHighAlarm_Object=MibScalar
pmoailhcsAlmLineOutputPwrHighAlarm=_PmoailhcsAlmLineOutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,6),_PmoailhcsAlmLineOutputPwrHighAlarm_Type())
pmoailhcsAlmLineOutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOutputPwrHighAlarm.setStatus(_A)
_PmoailhcsAlmLineBiasLowAlarm_Type=EkiOnOff
_PmoailhcsAlmLineBiasLowAlarm_Object=MibScalar
pmoailhcsAlmLineBiasLowAlarm=_PmoailhcsAlmLineBiasLowAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,7),_PmoailhcsAlmLineBiasLowAlarm_Type())
pmoailhcsAlmLineBiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineBiasLowAlarm.setStatus(_A)
_PmoailhcsAlmLineBiasHighAlarm_Type=EkiOnOff
_PmoailhcsAlmLineBiasHighAlarm_Object=MibScalar
pmoailhcsAlmLineBiasHighAlarm=_PmoailhcsAlmLineBiasHighAlarm_Object((1,3,6,1,4,1,20044,62,2,3,2,40,8),_PmoailhcsAlmLineBiasHighAlarm_Type())
pmoailhcsAlmLineBiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineBiasHighAlarm.setStatus(_A)
_PmoailhcsAlmLineCrit_ObjectIdentity=ObjectIdentity
pmoailhcsAlmLineCrit=_PmoailhcsAlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,3))
_PmoailhcsAlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmoailhcsAlmsynthAlm7=_PmoailhcsAlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,3,7))
_PmoailhcsAlmLineHwFail_Type=EkiOnOff
_PmoailhcsAlmLineHwFail_Object=MibScalar
pmoailhcsAlmLineHwFail=_PmoailhcsAlmLineHwFail_Object((1,3,6,1,4,1,20044,62,2,3,3,7,4),_PmoailhcsAlmLineHwFail_Type())
pmoailhcsAlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineHwFail.setStatus(_A)
_PmoailhcsAlmLineTxOff_Type=EkiOnOff
_PmoailhcsAlmLineTxOff_Object=MibScalar
pmoailhcsAlmLineTxOff=_PmoailhcsAlmLineTxOff_Object((1,3,6,1,4,1,20044,62,2,3,3,7,5),_PmoailhcsAlmLineTxOff_Type())
pmoailhcsAlmLineTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxOff.setStatus(_A)
_PmoailhcsAlmLineFail_Type=EkiOnOff
_PmoailhcsAlmLineFail_Object=MibScalar
pmoailhcsAlmLineFail=_PmoailhcsAlmLineFail_Object((1,3,6,1,4,1,20044,62,2,3,3,7,12),_PmoailhcsAlmLineFail_Type())
pmoailhcsAlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineFail.setStatus(_A)
_PmoailhcsAlmLineExtPumpFail_Type=EkiOnOff
_PmoailhcsAlmLineExtPumpFail_Object=MibScalar
pmoailhcsAlmLineExtPumpFail=_PmoailhcsAlmLineExtPumpFail_Object((1,3,6,1,4,1,20044,62,2,3,3,7,13),_PmoailhcsAlmLineExtPumpFail_Type())
pmoailhcsAlmLineExtPumpFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineExtPumpFail.setStatus(_A)
_PmoailhcsAlmSupvaFail_Type=EkiOnOff
_PmoailhcsAlmSupvaFail_Object=MibScalar
pmoailhcsAlmSupvaFail=_PmoailhcsAlmSupvaFail_Object((1,3,6,1,4,1,20044,62,2,3,3,7,14),_PmoailhcsAlmSupvaFail_Type())
pmoailhcsAlmSupvaFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmSupvaFail.setStatus(_A)
_PmoailhcsAlmlineEdfaAlarms2_ObjectIdentity=ObjectIdentity
pmoailhcsAlmlineEdfaAlarms2=_PmoailhcsAlmlineEdfaAlarms2_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,3,43))
_PmoailhcsAlmLineEdfaNr_Type=EkiOnOff
_PmoailhcsAlmLineEdfaNr_Object=MibScalar
pmoailhcsAlmLineEdfaNr=_PmoailhcsAlmLineEdfaNr_Object((1,3,6,1,4,1,20044,62,2,3,3,43,1),_PmoailhcsAlmLineEdfaNr_Type())
pmoailhcsAlmLineEdfaNr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineEdfaNr.setStatus(_A)
_PmoailhcsAlmLineEdfaTecFail_Type=EkiOnOff
_PmoailhcsAlmLineEdfaTecFail_Object=MibScalar
pmoailhcsAlmLineEdfaTecFail=_PmoailhcsAlmLineEdfaTecFail_Object((1,3,6,1,4,1,20044,62,2,3,3,43,2),_PmoailhcsAlmLineEdfaTecFail_Type())
pmoailhcsAlmLineEdfaTecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineEdfaTecFail.setStatus(_A)
_PmoailhcsAlmLineEdfaLaserFail_Type=EkiOnOff
_PmoailhcsAlmLineEdfaLaserFail_Object=MibScalar
pmoailhcsAlmLineEdfaLaserFail=_PmoailhcsAlmLineEdfaLaserFail_Object((1,3,6,1,4,1,20044,62,2,3,3,43,3),_PmoailhcsAlmLineEdfaLaserFail_Type())
pmoailhcsAlmLineEdfaLaserFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineEdfaLaserFail.setStatus(_A)
_PmoailhcsAlmLineEdfaLos_Type=EkiOnOff
_PmoailhcsAlmLineEdfaLos_Object=MibScalar
pmoailhcsAlmLineEdfaLos=_PmoailhcsAlmLineEdfaLos_Object((1,3,6,1,4,1,20044,62,2,3,3,43,4),_PmoailhcsAlmLineEdfaLos_Type())
pmoailhcsAlmLineEdfaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineEdfaLos.setStatus(_A)
_PmoailhcsAlmLineExtPumpEdfaLowCurrent_Type=EkiOnOff
_PmoailhcsAlmLineExtPumpEdfaLowCurrent_Object=MibScalar
pmoailhcsAlmLineExtPumpEdfaLowCurrent=_PmoailhcsAlmLineExtPumpEdfaLowCurrent_Object((1,3,6,1,4,1,20044,62,2,3,3,43,5),_PmoailhcsAlmLineExtPumpEdfaLowCurrent_Type())
pmoailhcsAlmLineExtPumpEdfaLowCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineExtPumpEdfaLowCurrent.setStatus(_A)
_PmoailhcsAlmLineGainOutOfRange_Type=EkiOnOff
_PmoailhcsAlmLineGainOutOfRange_Object=MibScalar
pmoailhcsAlmLineGainOutOfRange=_PmoailhcsAlmLineGainOutOfRange_Object((1,3,6,1,4,1,20044,62,2,3,3,43,6),_PmoailhcsAlmLineGainOutOfRange_Type())
pmoailhcsAlmLineGainOutOfRange.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineGainOutOfRange.setStatus(_A)
_PmoailhcsAlmlineMsaAlarms_ObjectIdentity=ObjectIdentity
pmoailhcsAlmlineMsaAlarms=_PmoailhcsAlmlineMsaAlarms_ObjectIdentity((1,3,6,1,4,1,20044,62,2,3,3,45))
_PmoailhcsAlmLineMsaLos_Type=EkiOnOff
_PmoailhcsAlmLineMsaLos_Object=MibScalar
pmoailhcsAlmLineMsaLos=_PmoailhcsAlmLineMsaLos_Object((1,3,6,1,4,1,20044,62,2,3,3,45,1),_PmoailhcsAlmLineMsaLos_Type())
pmoailhcsAlmLineMsaLos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineMsaLos.setStatus(_A)
_PmoailhcsAlmLineMsaAttenuation_Type=EkiOnOff
_PmoailhcsAlmLineMsaAttenuation_Object=MibScalar
pmoailhcsAlmLineMsaAttenuation=_PmoailhcsAlmLineMsaAttenuation_Object((1,3,6,1,4,1,20044,62,2,3,3,45,2),_PmoailhcsAlmLineMsaAttenuation_Type())
pmoailhcsAlmLineMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineMsaAttenuation.setStatus(_A)
_PmoailhcsAlmlineOscAlarmsTable_Object=MibTable
pmoailhcsAlmlineOscAlarmsTable=_PmoailhcsAlmlineOscAlarmsTable_Object((1,3,6,1,4,1,20044,62,2,3,3,48))
if mibBuilder.loadTexts:pmoailhcsAlmlineOscAlarmsTable.setStatus(_A)
_PmoailhcsAlmlineOscAlarmsEntry_Object=MibTableRow
pmoailhcsAlmlineOscAlarmsEntry=_PmoailhcsAlmlineOscAlarmsEntry_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1))
pmoailhcsAlmlineOscAlarmsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:pmoailhcsAlmlineOscAlarmsEntry.setStatus(_A)
class _PmoailhcsAlmlineOscAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsAlmlineOscAlarmsIndex_Type.__name__=_D
_PmoailhcsAlmlineOscAlarmsIndex_Object=MibTableColumn
pmoailhcsAlmlineOscAlarmsIndex=_PmoailhcsAlmlineOscAlarmsIndex_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,1),_PmoailhcsAlmlineOscAlarmsIndex_Type())
pmoailhcsAlmlineOscAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmlineOscAlarmsIndex.setStatus(_A)
_PmoailhcsAlmLineLosPortn_Type=EkiOnOff
_PmoailhcsAlmLineLosPortn_Object=MibTableColumn
pmoailhcsAlmLineLosPortn=_PmoailhcsAlmLineLosPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,2),_PmoailhcsAlmLineLosPortn_Type())
pmoailhcsAlmLineLosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineLosPortn.setStatus(_A)
_PmoailhcsAlmLineTxOffPortn_Type=EkiOnOff
_PmoailhcsAlmLineTxOffPortn_Object=MibTableColumn
pmoailhcsAlmLineTxOffPortn=_PmoailhcsAlmLineTxOffPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,3),_PmoailhcsAlmLineTxOffPortn_Type())
pmoailhcsAlmLineTxOffPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxOffPortn.setStatus(_A)
_PmoailhcsAlmLineTxFailPortn_Type=EkiOnOff
_PmoailhcsAlmLineTxFailPortn_Object=MibTableColumn
pmoailhcsAlmLineTxFailPortn=_PmoailhcsAlmLineTxFailPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,4),_PmoailhcsAlmLineTxFailPortn_Type())
pmoailhcsAlmLineTxFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxFailPortn.setStatus(_A)
_PmoailhcsAlmLineFecFailPortn_Type=EkiOnOff
_PmoailhcsAlmLineFecFailPortn_Object=MibTableColumn
pmoailhcsAlmLineFecFailPortn=_PmoailhcsAlmLineFecFailPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,5),_PmoailhcsAlmLineFecFailPortn_Type())
pmoailhcsAlmLineFecFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineFecFailPortn.setStatus(_A)
_PmoailhcsAlmLineOosPortn_Type=EkiOnOff
_PmoailhcsAlmLineOosPortn_Object=MibTableColumn
pmoailhcsAlmLineOosPortn=_PmoailhcsAlmLineOosPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,6),_PmoailhcsAlmLineOosPortn_Type())
pmoailhcsAlmLineOosPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOosPortn.setStatus(_A)
_PmoailhcsAlmLineLofPortn_Type=EkiOnOff
_PmoailhcsAlmLineLofPortn_Object=MibTableColumn
pmoailhcsAlmLineLofPortn=_PmoailhcsAlmLineLofPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,7),_PmoailhcsAlmLineLofPortn_Type())
pmoailhcsAlmLineLofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineLofPortn.setStatus(_A)
_PmoailhcsAlmLineOofPortn_Type=EkiOnOff
_PmoailhcsAlmLineOofPortn_Object=MibTableColumn
pmoailhcsAlmLineOofPortn=_PmoailhcsAlmLineOofPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,8),_PmoailhcsAlmLineOofPortn_Type())
pmoailhcsAlmLineOofPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOofPortn.setStatus(_A)
_PmoailhcsAlmLineRemoteTxFailPortn_Type=EkiOnOff
_PmoailhcsAlmLineRemoteTxFailPortn_Object=MibTableColumn
pmoailhcsAlmLineRemoteTxFailPortn=_PmoailhcsAlmLineRemoteTxFailPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,9),_PmoailhcsAlmLineRemoteTxFailPortn_Type())
pmoailhcsAlmLineRemoteTxFailPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineRemoteTxFailPortn.setStatus(_A)
_PmoailhcsAlmLineWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineWarningPortn=_PmoailhcsAlmLineWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,10),_PmoailhcsAlmLineWarningPortn_Type())
pmoailhcsAlmLineWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineWarningPortn.setStatus(_A)
_PmoailhcsAlmLineAlmPortn_Type=EkiOnOff
_PmoailhcsAlmLineAlmPortn_Object=MibTableColumn
pmoailhcsAlmLineAlmPortn=_PmoailhcsAlmLineAlmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,48,1,11),_PmoailhcsAlmLineAlmPortn_Type())
pmoailhcsAlmLineAlmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineAlmPortn.setStatus(_A)
_PmoailhcsAlmlineOscThresholdAlarmsTable_Object=MibTable
pmoailhcsAlmlineOscThresholdAlarmsTable=_PmoailhcsAlmlineOscThresholdAlarmsTable_Object((1,3,6,1,4,1,20044,62,2,3,3,49))
if mibBuilder.loadTexts:pmoailhcsAlmlineOscThresholdAlarmsTable.setStatus(_A)
_PmoailhcsAlmlineOscThresholdAlarmsEntry_Object=MibTableRow
pmoailhcsAlmlineOscThresholdAlarmsEntry=_PmoailhcsAlmlineOscThresholdAlarmsEntry_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1))
pmoailhcsAlmlineOscThresholdAlarmsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:pmoailhcsAlmlineOscThresholdAlarmsEntry.setStatus(_A)
class _PmoailhcsAlmlineOscThresholdAlarmsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsAlmlineOscThresholdAlarmsIndex_Type.__name__=_D
_PmoailhcsAlmlineOscThresholdAlarmsIndex_Object=MibTableColumn
pmoailhcsAlmlineOscThresholdAlarmsIndex=_PmoailhcsAlmlineOscThresholdAlarmsIndex_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,1),_PmoailhcsAlmlineOscThresholdAlarmsIndex_Type())
pmoailhcsAlmlineOscThresholdAlarmsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmlineOscThresholdAlarmsIndex.setStatus(_A)
_PmoailhcsAlmLineTxPwrLowAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineTxPwrLowAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineTxPwrLowAlarmPortn=_PmoailhcsAlmLineTxPwrLowAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,2),_PmoailhcsAlmLineTxPwrLowAlarmPortn_Type())
pmoailhcsAlmLineTxPwrLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxPwrLowAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineTxPwrHighAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineTxPwrHighAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineTxPwrHighAlarmPortn=_PmoailhcsAlmLineTxPwrHighAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,3),_PmoailhcsAlmLineTxPwrHighAlarmPortn_Type())
pmoailhcsAlmLineTxPwrHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxPwrHighAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineRxPwrLowAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineRxPwrLowAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineRxPwrLowAlarmPortn=_PmoailhcsAlmLineRxPwrLowAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,4),_PmoailhcsAlmLineRxPwrLowAlarmPortn_Type())
pmoailhcsAlmLineRxPwrLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineRxPwrLowAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineRxPwrHighAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineRxPwrHighAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineRxPwrHighAlarmPortn=_PmoailhcsAlmLineRxPwrHighAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,5),_PmoailhcsAlmLineRxPwrHighAlarmPortn_Type())
pmoailhcsAlmLineRxPwrHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineRxPwrHighAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineSpanlossLowAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineSpanlossLowAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineSpanlossLowAlarmPortn=_PmoailhcsAlmLineSpanlossLowAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,6),_PmoailhcsAlmLineSpanlossLowAlarmPortn_Type())
pmoailhcsAlmLineSpanlossLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineSpanlossLowAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineSpanlossHighAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineSpanlossHighAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineSpanlossHighAlarmPortn=_PmoailhcsAlmLineSpanlossHighAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,7),_PmoailhcsAlmLineSpanlossHighAlarmPortn_Type())
pmoailhcsAlmLineSpanlossHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineSpanlossHighAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineOscBiasLowAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineOscBiasLowAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineOscBiasLowAlarmPortn=_PmoailhcsAlmLineOscBiasLowAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,8),_PmoailhcsAlmLineOscBiasLowAlarmPortn_Type())
pmoailhcsAlmLineOscBiasLowAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOscBiasLowAlarmPortn.setStatus(_A)
_PmoailhcsAlmLineOscBiasHighAlarmPortn_Type=EkiOnOff
_PmoailhcsAlmLineOscBiasHighAlarmPortn_Object=MibTableColumn
pmoailhcsAlmLineOscBiasHighAlarmPortn=_PmoailhcsAlmLineOscBiasHighAlarmPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,49,1,9),_PmoailhcsAlmLineOscBiasHighAlarmPortn_Type())
pmoailhcsAlmLineOscBiasHighAlarmPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOscBiasHighAlarmPortn.setStatus(_A)
_PmoailhcsAlmlineOscThresholdsWarningsTable_Object=MibTable
pmoailhcsAlmlineOscThresholdsWarningsTable=_PmoailhcsAlmlineOscThresholdsWarningsTable_Object((1,3,6,1,4,1,20044,62,2,3,3,50))
if mibBuilder.loadTexts:pmoailhcsAlmlineOscThresholdsWarningsTable.setStatus(_A)
_PmoailhcsAlmlineOscThresholdsWarningsEntry_Object=MibTableRow
pmoailhcsAlmlineOscThresholdsWarningsEntry=_PmoailhcsAlmlineOscThresholdsWarningsEntry_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1))
pmoailhcsAlmlineOscThresholdsWarningsEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:pmoailhcsAlmlineOscThresholdsWarningsEntry.setStatus(_A)
class _PmoailhcsAlmlineOscThresholdsWarningsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsAlmlineOscThresholdsWarningsIndex_Type.__name__=_D
_PmoailhcsAlmlineOscThresholdsWarningsIndex_Object=MibTableColumn
pmoailhcsAlmlineOscThresholdsWarningsIndex=_PmoailhcsAlmlineOscThresholdsWarningsIndex_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,1),_PmoailhcsAlmlineOscThresholdsWarningsIndex_Type())
pmoailhcsAlmlineOscThresholdsWarningsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmlineOscThresholdsWarningsIndex.setStatus(_A)
_PmoailhcsAlmLineTxPwrLowWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineTxPwrLowWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineTxPwrLowWarningPortn=_PmoailhcsAlmLineTxPwrLowWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,2),_PmoailhcsAlmLineTxPwrLowWarningPortn_Type())
pmoailhcsAlmLineTxPwrLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxPwrLowWarningPortn.setStatus(_A)
_PmoailhcsAlmLineTxPwrHighWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineTxPwrHighWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineTxPwrHighWarningPortn=_PmoailhcsAlmLineTxPwrHighWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,3),_PmoailhcsAlmLineTxPwrHighWarningPortn_Type())
pmoailhcsAlmLineTxPwrHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineTxPwrHighWarningPortn.setStatus(_A)
_PmoailhcsAlmLineRxPwrLowWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineRxPwrLowWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineRxPwrLowWarningPortn=_PmoailhcsAlmLineRxPwrLowWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,4),_PmoailhcsAlmLineRxPwrLowWarningPortn_Type())
pmoailhcsAlmLineRxPwrLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineRxPwrLowWarningPortn.setStatus(_A)
_PmoailhcsAlmLineRxPwrHighWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineRxPwrHighWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineRxPwrHighWarningPortn=_PmoailhcsAlmLineRxPwrHighWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,5),_PmoailhcsAlmLineRxPwrHighWarningPortn_Type())
pmoailhcsAlmLineRxPwrHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineRxPwrHighWarningPortn.setStatus(_A)
_PmoailhcsAlmLineSpanlossLowWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineSpanlossLowWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineSpanlossLowWarningPortn=_PmoailhcsAlmLineSpanlossLowWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,6),_PmoailhcsAlmLineSpanlossLowWarningPortn_Type())
pmoailhcsAlmLineSpanlossLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineSpanlossLowWarningPortn.setStatus(_A)
_PmoailhcsAlmLineSpanlossHighWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineSpanlossHighWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineSpanlossHighWarningPortn=_PmoailhcsAlmLineSpanlossHighWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,7),_PmoailhcsAlmLineSpanlossHighWarningPortn_Type())
pmoailhcsAlmLineSpanlossHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineSpanlossHighWarningPortn.setStatus(_A)
_PmoailhcsAlmLineOscBiasLowWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineOscBiasLowWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineOscBiasLowWarningPortn=_PmoailhcsAlmLineOscBiasLowWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,8),_PmoailhcsAlmLineOscBiasLowWarningPortn_Type())
pmoailhcsAlmLineOscBiasLowWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOscBiasLowWarningPortn.setStatus(_A)
_PmoailhcsAlmLineOscBiasHighWarningPortn_Type=EkiOnOff
_PmoailhcsAlmLineOscBiasHighWarningPortn_Object=MibTableColumn
pmoailhcsAlmLineOscBiasHighWarningPortn=_PmoailhcsAlmLineOscBiasHighWarningPortn_Object((1,3,6,1,4,1,20044,62,2,3,3,50,1,9),_PmoailhcsAlmLineOscBiasHighWarningPortn_Type())
pmoailhcsAlmLineOscBiasHighWarningPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsAlmLineOscBiasHighWarningPortn.setStatus(_A)
_Pmoailhcsmeasures_ObjectIdentity=ObjectIdentity
pmoailhcsmeasures=_Pmoailhcsmeasures_ObjectIdentity((1,3,6,1,4,1,20044,62,3))
_PmoailhcsMesrOther_ObjectIdentity=ObjectIdentity
pmoailhcsMesrOther=_PmoailhcsMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,62,3,1))
class _PmoailhcsMesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrtempMeas_Type.__name__=_D
_PmoailhcsMesrtempMeas_Object=MibScalar
pmoailhcsMesrtempMeas=_PmoailhcsMesrtempMeas_Object((1,3,6,1,4,1,20044,62,3,1,80),_PmoailhcsMesrtempMeas_Type())
pmoailhcsMesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrtempMeas.setStatus(_A)
_PmoailhcsMesrClient_ObjectIdentity=ObjectIdentity
pmoailhcsMesrClient=_PmoailhcsMesrClient_ObjectIdentity((1,3,6,1,4,1,20044,62,3,2))
class _PmoailhcsMesrclientEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientEdfaBiasMeas_Type.__name__=_D
_PmoailhcsMesrclientEdfaBiasMeas_Object=MibScalar
pmoailhcsMesrclientEdfaBiasMeas=_PmoailhcsMesrclientEdfaBiasMeas_Object((1,3,6,1,4,1,20044,62,3,2,32),_PmoailhcsMesrclientEdfaBiasMeas_Type())
pmoailhcsMesrclientEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientEdfaBiasMeas.setStatus(_A)
class _PmoailhcsMesrclientEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientEdfaTxpwrMeas_Type.__name__=_D
_PmoailhcsMesrclientEdfaTxpwrMeas_Object=MibScalar
pmoailhcsMesrclientEdfaTxpwrMeas=_PmoailhcsMesrclientEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,62,3,2,33),_PmoailhcsMesrclientEdfaTxpwrMeas_Type())
pmoailhcsMesrclientEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientEdfaTxpwrMeas.setStatus(_A)
class _PmoailhcsMesrclientEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientEdfaRxpwrMeas_Type.__name__=_D
_PmoailhcsMesrclientEdfaRxpwrMeas_Object=MibScalar
pmoailhcsMesrclientEdfaRxpwrMeas=_PmoailhcsMesrclientEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,62,3,2,34),_PmoailhcsMesrclientEdfaRxpwrMeas_Type())
pmoailhcsMesrclientEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientEdfaRxpwrMeas.setStatus(_A)
class _PmoailhcsMesrclientEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientEdfaGainMeas_Type.__name__=_D
_PmoailhcsMesrclientEdfaGainMeas_Object=MibScalar
pmoailhcsMesrclientEdfaGainMeas=_PmoailhcsMesrclientEdfaGainMeas_Object((1,3,6,1,4,1,20044,62,3,2,35),_PmoailhcsMesrclientEdfaGainMeas_Type())
pmoailhcsMesrclientEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientEdfaGainMeas.setStatus(_A)
class _PmoailhcsMesrclientOscSpanLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientOscSpanLoss_Type.__name__=_D
_PmoailhcsMesrclientOscSpanLoss_Object=MibScalar
pmoailhcsMesrclientOscSpanLoss=_PmoailhcsMesrclientOscSpanLoss_Object((1,3,6,1,4,1,20044,62,3,2,36),_PmoailhcsMesrclientOscSpanLoss_Type())
pmoailhcsMesrclientOscSpanLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientOscSpanLoss.setStatus(_A)
class _PmoailhcsMesrclientOscSpanLossRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientOscSpanLossRef_Type.__name__=_D
_PmoailhcsMesrclientOscSpanLossRef_Object=MibScalar
pmoailhcsMesrclientOscSpanLossRef=_PmoailhcsMesrclientOscSpanLossRef_Object((1,3,6,1,4,1,20044,62,3,2,37),_PmoailhcsMesrclientOscSpanLossRef_Type())
pmoailhcsMesrclientOscSpanLossRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientOscSpanLossRef.setStatus(_A)
class _PmoailhcsMesrclientCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientCorrectedGain_Type.__name__=_D
_PmoailhcsMesrclientCorrectedGain_Object=MibScalar
pmoailhcsMesrclientCorrectedGain=_PmoailhcsMesrclientCorrectedGain_Object((1,3,6,1,4,1,20044,62,3,2,38),_PmoailhcsMesrclientCorrectedGain_Type())
pmoailhcsMesrclientCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientCorrectedGain.setStatus(_A)
class _PmoailhcsMesrclientMsaInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientMsaInputPower_Type.__name__=_D
_PmoailhcsMesrclientMsaInputPower_Object=MibScalar
pmoailhcsMesrclientMsaInputPower=_PmoailhcsMesrclientMsaInputPower_Object((1,3,6,1,4,1,20044,62,3,2,39),_PmoailhcsMesrclientMsaInputPower_Type())
pmoailhcsMesrclientMsaInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientMsaInputPower.setStatus(_A)
class _PmoailhcsMesrclientMsaOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientMsaOutputPower_Type.__name__=_D
_PmoailhcsMesrclientMsaOutputPower_Object=MibScalar
pmoailhcsMesrclientMsaOutputPower=_PmoailhcsMesrclientMsaOutputPower_Object((1,3,6,1,4,1,20044,62,3,2,40),_PmoailhcsMesrclientMsaOutputPower_Type())
pmoailhcsMesrclientMsaOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientMsaOutputPower.setStatus(_A)
class _PmoailhcsMesrclientMsaAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientMsaAttenuation_Type.__name__=_D
_PmoailhcsMesrclientMsaAttenuation_Object=MibScalar
pmoailhcsMesrclientMsaAttenuation=_PmoailhcsMesrclientMsaAttenuation_Object((1,3,6,1,4,1,20044,62,3,2,41),_PmoailhcsMesrclientMsaAttenuation_Type())
pmoailhcsMesrclientMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientMsaAttenuation.setStatus(_A)
class _PmoailhcsMesrclientMsaAttenuationRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrclientMsaAttenuationRef_Type.__name__=_D
_PmoailhcsMesrclientMsaAttenuationRef_Object=MibScalar
pmoailhcsMesrclientMsaAttenuationRef=_PmoailhcsMesrclientMsaAttenuationRef_Object((1,3,6,1,4,1,20044,62,3,2,42),_PmoailhcsMesrclientMsaAttenuationRef_Type())
pmoailhcsMesrclientMsaAttenuationRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrclientMsaAttenuationRef.setStatus(_A)
_PmoailhcsMesrLine_ObjectIdentity=ObjectIdentity
pmoailhcsMesrLine=_PmoailhcsMesrLine_ObjectIdentity((1,3,6,1,4,1,20044,62,3,3))
class _PmoailhcsMesrlineEdfaBiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineEdfaBiasMeas_Type.__name__=_D
_PmoailhcsMesrlineEdfaBiasMeas_Object=MibScalar
pmoailhcsMesrlineEdfaBiasMeas=_PmoailhcsMesrlineEdfaBiasMeas_Object((1,3,6,1,4,1,20044,62,3,3,48),_PmoailhcsMesrlineEdfaBiasMeas_Type())
pmoailhcsMesrlineEdfaBiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineEdfaBiasMeas.setStatus(_A)
class _PmoailhcsMesrlineEdfaTxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineEdfaTxpwrMeas_Type.__name__=_D
_PmoailhcsMesrlineEdfaTxpwrMeas_Object=MibScalar
pmoailhcsMesrlineEdfaTxpwrMeas=_PmoailhcsMesrlineEdfaTxpwrMeas_Object((1,3,6,1,4,1,20044,62,3,3,49),_PmoailhcsMesrlineEdfaTxpwrMeas_Type())
pmoailhcsMesrlineEdfaTxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineEdfaTxpwrMeas.setStatus(_A)
class _PmoailhcsMesrlineEdfaRxpwrMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineEdfaRxpwrMeas_Type.__name__=_D
_PmoailhcsMesrlineEdfaRxpwrMeas_Object=MibScalar
pmoailhcsMesrlineEdfaRxpwrMeas=_PmoailhcsMesrlineEdfaRxpwrMeas_Object((1,3,6,1,4,1,20044,62,3,3,50),_PmoailhcsMesrlineEdfaRxpwrMeas_Type())
pmoailhcsMesrlineEdfaRxpwrMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineEdfaRxpwrMeas.setStatus(_A)
class _PmoailhcsMesrlineEdfaGainMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineEdfaGainMeas_Type.__name__=_D
_PmoailhcsMesrlineEdfaGainMeas_Object=MibScalar
pmoailhcsMesrlineEdfaGainMeas=_PmoailhcsMesrlineEdfaGainMeas_Object((1,3,6,1,4,1,20044,62,3,3,51),_PmoailhcsMesrlineEdfaGainMeas_Type())
pmoailhcsMesrlineEdfaGainMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineEdfaGainMeas.setStatus(_A)
class _PmoailhcsMesrlineOscSpanLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineOscSpanLoss_Type.__name__=_D
_PmoailhcsMesrlineOscSpanLoss_Object=MibScalar
pmoailhcsMesrlineOscSpanLoss=_PmoailhcsMesrlineOscSpanLoss_Object((1,3,6,1,4,1,20044,62,3,3,52),_PmoailhcsMesrlineOscSpanLoss_Type())
pmoailhcsMesrlineOscSpanLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineOscSpanLoss.setStatus(_A)
class _PmoailhcsMesrlineOscSpanLossRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineOscSpanLossRef_Type.__name__=_D
_PmoailhcsMesrlineOscSpanLossRef_Object=MibScalar
pmoailhcsMesrlineOscSpanLossRef=_PmoailhcsMesrlineOscSpanLossRef_Object((1,3,6,1,4,1,20044,62,3,3,53),_PmoailhcsMesrlineOscSpanLossRef_Type())
pmoailhcsMesrlineOscSpanLossRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineOscSpanLossRef.setStatus(_A)
class _PmoailhcsMesrlineCorrectedGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineCorrectedGain_Type.__name__=_D
_PmoailhcsMesrlineCorrectedGain_Object=MibScalar
pmoailhcsMesrlineCorrectedGain=_PmoailhcsMesrlineCorrectedGain_Object((1,3,6,1,4,1,20044,62,3,3,54),_PmoailhcsMesrlineCorrectedGain_Type())
pmoailhcsMesrlineCorrectedGain.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineCorrectedGain.setStatus(_A)
class _PmoailhcsMesrlineMsaInputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineMsaInputPower_Type.__name__=_D
_PmoailhcsMesrlineMsaInputPower_Object=MibScalar
pmoailhcsMesrlineMsaInputPower=_PmoailhcsMesrlineMsaInputPower_Object((1,3,6,1,4,1,20044,62,3,3,55),_PmoailhcsMesrlineMsaInputPower_Type())
pmoailhcsMesrlineMsaInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineMsaInputPower.setStatus(_A)
class _PmoailhcsMesrlineMsaOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineMsaOutputPower_Type.__name__=_D
_PmoailhcsMesrlineMsaOutputPower_Object=MibScalar
pmoailhcsMesrlineMsaOutputPower=_PmoailhcsMesrlineMsaOutputPower_Object((1,3,6,1,4,1,20044,62,3,3,56),_PmoailhcsMesrlineMsaOutputPower_Type())
pmoailhcsMesrlineMsaOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineMsaOutputPower.setStatus(_A)
class _PmoailhcsMesrlineMsaAttenuation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineMsaAttenuation_Type.__name__=_D
_PmoailhcsMesrlineMsaAttenuation_Object=MibScalar
pmoailhcsMesrlineMsaAttenuation=_PmoailhcsMesrlineMsaAttenuation_Object((1,3,6,1,4,1,20044,62,3,3,57),_PmoailhcsMesrlineMsaAttenuation_Type())
pmoailhcsMesrlineMsaAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineMsaAttenuation.setStatus(_A)
class _PmoailhcsMesrlineMsaAttenuationRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineMsaAttenuationRef_Type.__name__=_D
_PmoailhcsMesrlineMsaAttenuationRef_Object=MibScalar
pmoailhcsMesrlineMsaAttenuationRef=_PmoailhcsMesrlineMsaAttenuationRef_Object((1,3,6,1,4,1,20044,62,3,3,58),_PmoailhcsMesrlineMsaAttenuationRef_Type())
pmoailhcsMesrlineMsaAttenuationRef.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineMsaAttenuationRef.setStatus(_A)
_PmoailhcsMesrlineOscTxPowerTable_Object=MibTable
pmoailhcsMesrlineOscTxPowerTable=_PmoailhcsMesrlineOscTxPowerTable_Object((1,3,6,1,4,1,20044,62,3,3,64))
if mibBuilder.loadTexts:pmoailhcsMesrlineOscTxPowerTable.setStatus(_A)
_PmoailhcsMesrlineOscTxPowerEntry_Object=MibTableRow
pmoailhcsMesrlineOscTxPowerEntry=_PmoailhcsMesrlineOscTxPowerEntry_Object((1,3,6,1,4,1,20044,62,3,3,64,1))
pmoailhcsMesrlineOscTxPowerEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:pmoailhcsMesrlineOscTxPowerEntry.setStatus(_A)
class _PmoailhcsMesrlineOscTxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsMesrlineOscTxPowerIndex_Type.__name__=_D
_PmoailhcsMesrlineOscTxPowerIndex_Object=MibTableColumn
pmoailhcsMesrlineOscTxPowerIndex=_PmoailhcsMesrlineOscTxPowerIndex_Object((1,3,6,1,4,1,20044,62,3,3,64,1,1),_PmoailhcsMesrlineOscTxPowerIndex_Type())
pmoailhcsMesrlineOscTxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineOscTxPowerIndex.setStatus(_A)
class _PmoailhcsMesrlineOscTxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineOscTxPowerPortn_Type.__name__=_D
_PmoailhcsMesrlineOscTxPowerPortn_Object=MibTableColumn
pmoailhcsMesrlineOscTxPowerPortn=_PmoailhcsMesrlineOscTxPowerPortn_Object((1,3,6,1,4,1,20044,62,3,3,64,1,2),_PmoailhcsMesrlineOscTxPowerPortn_Type())
pmoailhcsMesrlineOscTxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineOscTxPowerPortn.setStatus(_A)
_PmoailhcsMesrlineOscRxPowerTable_Object=MibTable
pmoailhcsMesrlineOscRxPowerTable=_PmoailhcsMesrlineOscRxPowerTable_Object((1,3,6,1,4,1,20044,62,3,3,65))
if mibBuilder.loadTexts:pmoailhcsMesrlineOscRxPowerTable.setStatus(_A)
_PmoailhcsMesrlineOscRxPowerEntry_Object=MibTableRow
pmoailhcsMesrlineOscRxPowerEntry=_PmoailhcsMesrlineOscRxPowerEntry_Object((1,3,6,1,4,1,20044,62,3,3,65,1))
pmoailhcsMesrlineOscRxPowerEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:pmoailhcsMesrlineOscRxPowerEntry.setStatus(_A)
class _PmoailhcsMesrlineOscRxPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsMesrlineOscRxPowerIndex_Type.__name__=_D
_PmoailhcsMesrlineOscRxPowerIndex_Object=MibTableColumn
pmoailhcsMesrlineOscRxPowerIndex=_PmoailhcsMesrlineOscRxPowerIndex_Object((1,3,6,1,4,1,20044,62,3,3,65,1,1),_PmoailhcsMesrlineOscRxPowerIndex_Type())
pmoailhcsMesrlineOscRxPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineOscRxPowerIndex.setStatus(_A)
class _PmoailhcsMesrlineOscRxPowerPortn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsMesrlineOscRxPowerPortn_Type.__name__=_D
_PmoailhcsMesrlineOscRxPowerPortn_Object=MibTableColumn
pmoailhcsMesrlineOscRxPowerPortn=_PmoailhcsMesrlineOscRxPowerPortn_Object((1,3,6,1,4,1,20044,62,3,3,65,1,2),_PmoailhcsMesrlineOscRxPowerPortn_Type())
pmoailhcsMesrlineOscRxPowerPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsMesrlineOscRxPowerPortn.setStatus(_A)
_Pmoailhcscounters_ObjectIdentity=ObjectIdentity
pmoailhcscounters=_Pmoailhcscounters_ObjectIdentity((1,3,6,1,4,1,20044,62,4))
_PmoailhcsCntOther_ObjectIdentity=ObjectIdentity
pmoailhcsCntOther=_PmoailhcsCntOther_ObjectIdentity((1,3,6,1,4,1,20044,62,4,1))
_PmoailhcsCntClient_ObjectIdentity=ObjectIdentity
pmoailhcsCntClient=_PmoailhcsCntClient_ObjectIdentity((1,3,6,1,4,1,20044,62,4,2))
_PmoailhcsCntLine_ObjectIdentity=ObjectIdentity
pmoailhcsCntLine=_PmoailhcsCntLine_ObjectIdentity((1,3,6,1,4,1,20044,62,4,3))
_PmoailhcsCntlineOscErrTable_Object=MibTable
pmoailhcsCntlineOscErrTable=_PmoailhcsCntlineOscErrTable_Object((1,3,6,1,4,1,20044,62,4,3,16))
if mibBuilder.loadTexts:pmoailhcsCntlineOscErrTable.setStatus(_A)
_PmoailhcsCntlineOscErrEntry_Object=MibTableRow
pmoailhcsCntlineOscErrEntry=_PmoailhcsCntlineOscErrEntry_Object((1,3,6,1,4,1,20044,62,4,3,16,1))
pmoailhcsCntlineOscErrEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:pmoailhcsCntlineOscErrEntry.setStatus(_A)
class _PmoailhcsCntlineOscErrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsCntlineOscErrIndex_Type.__name__=_D
_PmoailhcsCntlineOscErrIndex_Object=MibTableColumn
pmoailhcsCntlineOscErrIndex=_PmoailhcsCntlineOscErrIndex_Object((1,3,6,1,4,1,20044,62,4,3,16,1,1),_PmoailhcsCntlineOscErrIndex_Type())
pmoailhcsCntlineOscErrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCntlineOscErrIndex.setStatus(_A)
_PmoailhcsCntlineOscErrValuePortn_Type=Counter32
_PmoailhcsCntlineOscErrValuePortn_Object=MibTableColumn
pmoailhcsCntlineOscErrValuePortn=_PmoailhcsCntlineOscErrValuePortn_Object((1,3,6,1,4,1,20044,62,4,3,16,1,2),_PmoailhcsCntlineOscErrValuePortn_Type())
pmoailhcsCntlineOscErrValuePortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCntlineOscErrValuePortn.setStatus(_A)
_PmoailhcsCntlineOscErrErrorPortn_Type=EkiOnOff
_PmoailhcsCntlineOscErrErrorPortn_Object=MibTableColumn
pmoailhcsCntlineOscErrErrorPortn=_PmoailhcsCntlineOscErrErrorPortn_Object((1,3,6,1,4,1,20044,62,4,3,16,1,3),_PmoailhcsCntlineOscErrErrorPortn_Type())
pmoailhcsCntlineOscErrErrorPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCntlineOscErrErrorPortn.setStatus(_A)
_PmoailhcsCntlineOscErrOverloadPortn_Type=EkiOnOff
_PmoailhcsCntlineOscErrOverloadPortn_Object=MibTableColumn
pmoailhcsCntlineOscErrOverloadPortn=_PmoailhcsCntlineOscErrOverloadPortn_Object((1,3,6,1,4,1,20044,62,4,3,16,1,4),_PmoailhcsCntlineOscErrOverloadPortn_Type())
pmoailhcsCntlineOscErrOverloadPortn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCntlineOscErrOverloadPortn.setStatus(_A)
_PmoailhcsCntCountersReset_Type=EkiOnOff
_PmoailhcsCntCountersReset_Object=MibScalar
pmoailhcsCntCountersReset=_PmoailhcsCntCountersReset_Object((1,3,6,1,4,1,20044,62,4,259),_PmoailhcsCntCountersReset_Type())
pmoailhcsCntCountersReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCntCountersReset.setStatus(_A)
_PmoailhcsCntCountersStop_Type=EkiOnOff
_PmoailhcsCntCountersStop_Object=MibScalar
pmoailhcsCntCountersStop=_PmoailhcsCntCountersStop_Object((1,3,6,1,4,1,20044,62,4,260),_PmoailhcsCntCountersStop_Type())
pmoailhcsCntCountersStop.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCntCountersStop.setStatus(_A)
_PmoailhcscontrolsWrite_ObjectIdentity=ObjectIdentity
pmoailhcscontrolsWrite=_PmoailhcscontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,62,6))
_PmoailhcsCtrlOther_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlOther=_PmoailhcsCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,62,6,1))
_PmoailhcsCtrlsynth0_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlsynth0=_PmoailhcsCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,62,6,1,0))
_PmoailhcsCtrlConfLoad_Type=EkiOnOff
_PmoailhcsCtrlConfLoad_Object=MibScalar
pmoailhcsCtrlConfLoad=_PmoailhcsCtrlConfLoad_Object((1,3,6,1,4,1,20044,62,6,1,0,1),_PmoailhcsCtrlConfLoad_Type())
pmoailhcsCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlConfLoad.setStatus(_A)
_PmoailhcsCtrlConfFlash_Type=EkiOnOff
_PmoailhcsCtrlConfFlash_Object=MibScalar
pmoailhcsCtrlConfFlash=_PmoailhcsCtrlConfFlash_Object((1,3,6,1,4,1,20044,62,6,1,0,9),_PmoailhcsCtrlConfFlash_Type())
pmoailhcsCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlConfFlash.setStatus(_A)
_PmoailhcsCtrlConfClear_Type=EkiOnOff
_PmoailhcsCtrlConfClear_Object=MibScalar
pmoailhcsCtrlConfClear=_PmoailhcsCtrlConfClear_Object((1,3,6,1,4,1,20044,62,6,1,0,13),_PmoailhcsCtrlConfClear_Type())
pmoailhcsCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlConfClear.setStatus(_A)
_PmoailhcsCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlswMgnt=_PmoailhcsCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,62,6,1,5))
_PmoailhcsCtrlColdReset_Type=EkiOnOff
_PmoailhcsCtrlColdReset_Object=MibScalar
pmoailhcsCtrlColdReset=_PmoailhcsCtrlColdReset_Object((1,3,6,1,4,1,20044,62,6,1,5,2),_PmoailhcsCtrlColdReset_Type())
pmoailhcsCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlColdReset.setStatus(_A)
_PmoailhcsCtrlWarmReset_Type=EkiOnOff
_PmoailhcsCtrlWarmReset_Object=MibScalar
pmoailhcsCtrlWarmReset=_PmoailhcsCtrlWarmReset_Object((1,3,6,1,4,1,20044,62,6,1,5,3),_PmoailhcsCtrlWarmReset_Type())
pmoailhcsCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlWarmReset.setStatus(_A)
_PmoailhcsCtrlledTest_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlledTest=_PmoailhcsCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,62,6,1,73))
_PmoailhcsCtrlGreenLed_Type=EkiOnOff
_PmoailhcsCtrlGreenLed_Object=MibScalar
pmoailhcsCtrlGreenLed=_PmoailhcsCtrlGreenLed_Object((1,3,6,1,4,1,20044,62,6,1,73,1),_PmoailhcsCtrlGreenLed_Type())
pmoailhcsCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlGreenLed.setStatus(_A)
_PmoailhcsCtrlRedLed_Type=EkiOnOff
_PmoailhcsCtrlRedLed_Object=MibScalar
pmoailhcsCtrlRedLed=_PmoailhcsCtrlRedLed_Object((1,3,6,1,4,1,20044,62,6,1,73,2),_PmoailhcsCtrlRedLed_Type())
pmoailhcsCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlRedLed.setStatus(_A)
_PmoailhcsCtrlLedOff_Type=EkiOnOff
_PmoailhcsCtrlLedOff_Object=MibScalar
pmoailhcsCtrlLedOff=_PmoailhcsCtrlLedOff_Object((1,3,6,1,4,1,20044,62,6,1,73,3),_PmoailhcsCtrlLedOff_Type())
pmoailhcsCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlLedOff.setStatus(_A)
_PmoailhcsCtrlmaintMode_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlmaintMode=_PmoailhcsCtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,62,6,1,75))
_PmoailhcsCtrlMaintenance_Type=EkiOnOff
_PmoailhcsCtrlMaintenance_Object=MibScalar
pmoailhcsCtrlMaintenance=_PmoailhcsCtrlMaintenance_Object((1,3,6,1,4,1,20044,62,6,1,75,1),_PmoailhcsCtrlMaintenance_Type())
pmoailhcsCtrlMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlMaintenance.setStatus(_A)
_PmoailhcsCtrlaprRestart_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlaprRestart=_PmoailhcsCtrlaprRestart_ObjectIdentity((1,3,6,1,4,1,20044,62,6,1,76))
_PmoailhcsCtrlAprManualRestart_Type=EkiOnOff
_PmoailhcsCtrlAprManualRestart_Object=MibScalar
pmoailhcsCtrlAprManualRestart=_PmoailhcsCtrlAprManualRestart_Object((1,3,6,1,4,1,20044,62,6,1,76,1),_PmoailhcsCtrlAprManualRestart_Type())
pmoailhcsCtrlAprManualRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlAprManualRestart.setStatus(_A)
_PmoailhcsCtrlClient_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlClient=_PmoailhcsCtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,62,6,2))
_PmoailhcsCtrlclientOscInputSpanLoss_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlclientOscInputSpanLoss=_PmoailhcsCtrlclientOscInputSpanLoss_ObjectIdentity((1,3,6,1,4,1,20044,62,6,2,33))
_PmoailhcsCtrlClientSpanLoss_Type=EkiOnOff
_PmoailhcsCtrlClientSpanLoss_Object=MibScalar
pmoailhcsCtrlClientSpanLoss=_PmoailhcsCtrlClientSpanLoss_Object((1,3,6,1,4,1,20044,62,6,2,33,1),_PmoailhcsCtrlClientSpanLoss_Type())
pmoailhcsCtrlClientSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlClientSpanLoss.setStatus(_A)
class _PmoailhcsCtrlclientGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsCtrlclientGainCstMonitorValue_Type.__name__=_D
_PmoailhcsCtrlclientGainCstMonitorValue_Object=MibScalar
pmoailhcsCtrlclientGainCstMonitorValue=_PmoailhcsCtrlclientGainCstMonitorValue_Object((1,3,6,1,4,1,20044,62,6,2,34),_PmoailhcsCtrlclientGainCstMonitorValue_Type())
pmoailhcsCtrlclientGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlclientGainCstMonitorValue.setStatus(_A)
class _PmoailhcsCtrlclientGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsCtrlclientGainSettingValue_Type.__name__=_D
_PmoailhcsCtrlclientGainSettingValue_Object=MibScalar
pmoailhcsCtrlclientGainSettingValue=_PmoailhcsCtrlclientGainSettingValue_Object((1,3,6,1,4,1,20044,62,6,2,36),_PmoailhcsCtrlclientGainSettingValue_Type())
pmoailhcsCtrlclientGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlclientGainSettingValue.setStatus(_A)
_PmoailhcsCtrlclientGainProcessing_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlclientGainProcessing=_PmoailhcsCtrlclientGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,62,6,2,37))
_PmoailhcsCtrlClientGainProc_Type=EkiOnOff
_PmoailhcsCtrlClientGainProc_Object=MibScalar
pmoailhcsCtrlClientGainProc=_PmoailhcsCtrlClientGainProc_Object((1,3,6,1,4,1,20044,62,6,2,37,1),_PmoailhcsCtrlClientGainProc_Type())
pmoailhcsCtrlClientGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlClientGainProc.setStatus(_A)
class _PmoailhcsCtrlclientGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsCtrlclientGainCstFiberAgingMarginValue_Type.__name__=_D
_PmoailhcsCtrlclientGainCstFiberAgingMarginValue_Object=MibScalar
pmoailhcsCtrlclientGainCstFiberAgingMarginValue=_PmoailhcsCtrlclientGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,62,6,2,38),_PmoailhcsCtrlclientGainCstFiberAgingMarginValue_Type())
pmoailhcsCtrlclientGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlclientGainCstFiberAgingMarginValue.setStatus(_A)
_PmoailhcsCtrlclientMsaAttenuationValue_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlclientMsaAttenuationValue=_PmoailhcsCtrlclientMsaAttenuationValue_ObjectIdentity((1,3,6,1,4,1,20044,62,6,2,40))
_PmoailhcsCtrlClientAttenuation_Type=EkiOnOff
_PmoailhcsCtrlClientAttenuation_Object=MibScalar
pmoailhcsCtrlClientAttenuation=_PmoailhcsCtrlClientAttenuation_Object((1,3,6,1,4,1,20044,62,6,2,40,1),_PmoailhcsCtrlClientAttenuation_Type())
pmoailhcsCtrlClientAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlClientAttenuation.setStatus(_A)
_PmoailhcsCtrlLine_ObjectIdentity=ObjectIdentity
pmoailhcsCtrlLine=_PmoailhcsCtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,62,6,3))
_PmoailhcsCtrllineOscInputSpanLoss_ObjectIdentity=ObjectIdentity
pmoailhcsCtrllineOscInputSpanLoss=_PmoailhcsCtrllineOscInputSpanLoss_ObjectIdentity((1,3,6,1,4,1,20044,62,6,3,49))
_PmoailhcsCtrlLineSpanLoss_Type=EkiOnOff
_PmoailhcsCtrlLineSpanLoss_Object=MibScalar
pmoailhcsCtrlLineSpanLoss=_PmoailhcsCtrlLineSpanLoss_Object((1,3,6,1,4,1,20044,62,6,3,49,1),_PmoailhcsCtrlLineSpanLoss_Type())
pmoailhcsCtrlLineSpanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlLineSpanLoss.setStatus(_A)
class _PmoailhcsCtrllineGainCstMonitorValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsCtrllineGainCstMonitorValue_Type.__name__=_D
_PmoailhcsCtrllineGainCstMonitorValue_Object=MibScalar
pmoailhcsCtrllineGainCstMonitorValue=_PmoailhcsCtrllineGainCstMonitorValue_Object((1,3,6,1,4,1,20044,62,6,3,50),_PmoailhcsCtrllineGainCstMonitorValue_Type())
pmoailhcsCtrllineGainCstMonitorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrllineGainCstMonitorValue.setStatus(_A)
class _PmoailhcsCtrllineGainSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsCtrllineGainSettingValue_Type.__name__=_D
_PmoailhcsCtrllineGainSettingValue_Object=MibScalar
pmoailhcsCtrllineGainSettingValue=_PmoailhcsCtrllineGainSettingValue_Object((1,3,6,1,4,1,20044,62,6,3,52),_PmoailhcsCtrllineGainSettingValue_Type())
pmoailhcsCtrllineGainSettingValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrllineGainSettingValue.setStatus(_A)
_PmoailhcsCtrllineGainProcessing_ObjectIdentity=ObjectIdentity
pmoailhcsCtrllineGainProcessing=_PmoailhcsCtrllineGainProcessing_ObjectIdentity((1,3,6,1,4,1,20044,62,6,3,53))
_PmoailhcsCtrlLineGainProc_Type=EkiOnOff
_PmoailhcsCtrlLineGainProc_Object=MibScalar
pmoailhcsCtrlLineGainProc=_PmoailhcsCtrlLineGainProc_Object((1,3,6,1,4,1,20044,62,6,3,53,1),_PmoailhcsCtrlLineGainProc_Type())
pmoailhcsCtrlLineGainProc.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlLineGainProc.setStatus(_A)
class _PmoailhcsCtrllineGainCstFiberAgingMarginValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmoailhcsCtrllineGainCstFiberAgingMarginValue_Type.__name__=_D
_PmoailhcsCtrllineGainCstFiberAgingMarginValue_Object=MibScalar
pmoailhcsCtrllineGainCstFiberAgingMarginValue=_PmoailhcsCtrllineGainCstFiberAgingMarginValue_Object((1,3,6,1,4,1,20044,62,6,3,54),_PmoailhcsCtrllineGainCstFiberAgingMarginValue_Type())
pmoailhcsCtrllineGainCstFiberAgingMarginValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrllineGainCstFiberAgingMarginValue.setStatus(_A)
_PmoailhcsCtrllineMsaAttenuationValue_ObjectIdentity=ObjectIdentity
pmoailhcsCtrllineMsaAttenuationValue=_PmoailhcsCtrllineMsaAttenuationValue_ObjectIdentity((1,3,6,1,4,1,20044,62,6,3,56))
_PmoailhcsCtrlLineAttenuation_Type=EkiOnOff
_PmoailhcsCtrlLineAttenuation_Object=MibScalar
pmoailhcsCtrlLineAttenuation=_PmoailhcsCtrlLineAttenuation_Object((1,3,6,1,4,1,20044,62,6,3,56,1),_PmoailhcsCtrlLineAttenuation_Type())
pmoailhcsCtrlLineAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCtrlLineAttenuation.setStatus(_A)
_Pmoailhcsri_ObjectIdentity=ObjectIdentity
pmoailhcsri=_Pmoailhcsri_ObjectIdentity((1,3,6,1,4,1,20044,62,7))
_PmoailhcsRinvReloadInventory_Type=EkiOnOff
_PmoailhcsRinvReloadInventory_Object=MibScalar
pmoailhcsRinvReloadInventory=_PmoailhcsRinvReloadInventory_Object((1,3,6,1,4,1,20044,62,7,2),_PmoailhcsRinvReloadInventory_Type())
pmoailhcsRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsRinvReloadInventory.setStatus(_A)
_PmoailhcsRinvHwPlatform_Type=DisplayString
_PmoailhcsRinvHwPlatform_Object=MibScalar
pmoailhcsRinvHwPlatform=_PmoailhcsRinvHwPlatform_Object((1,3,6,1,4,1,20044,62,7,3),_PmoailhcsRinvHwPlatform_Type())
pmoailhcsRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvHwPlatform.setStatus(_A)
_PmoailhcsRinvModulePlatform_Type=DisplayString
_PmoailhcsRinvModulePlatform_Object=MibScalar
pmoailhcsRinvModulePlatform=_PmoailhcsRinvModulePlatform_Object((1,3,6,1,4,1,20044,62,7,4),_PmoailhcsRinvModulePlatform_Type())
pmoailhcsRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvModulePlatform.setStatus(_A)
_PmoailhcsRinvSwPlatform_Type=DisplayString
_PmoailhcsRinvSwPlatform_Object=MibScalar
pmoailhcsRinvSwPlatform=_PmoailhcsRinvSwPlatform_Object((1,3,6,1,4,1,20044,62,7,5),_PmoailhcsRinvSwPlatform_Type())
pmoailhcsRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvSwPlatform.setStatus(_A)
_PmoailhcsRinvGwPlatform_Type=DisplayString
_PmoailhcsRinvGwPlatform_Object=MibScalar
pmoailhcsRinvGwPlatform=_PmoailhcsRinvGwPlatform_Object((1,3,6,1,4,1,20044,62,7,6),_PmoailhcsRinvGwPlatform_Type())
pmoailhcsRinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvGwPlatform.setStatus(_A)
_PmoailhcsRinvBoosterTable_Object=MibTable
pmoailhcsRinvBoosterTable=_PmoailhcsRinvBoosterTable_Object((1,3,6,1,4,1,20044,62,7,7))
if mibBuilder.loadTexts:pmoailhcsRinvBoosterTable.setStatus(_A)
_PmoailhcsRinvBoosterEntry_Object=MibTableRow
pmoailhcsRinvBoosterEntry=_PmoailhcsRinvBoosterEntry_Object((1,3,6,1,4,1,20044,62,7,7,1))
pmoailhcsRinvBoosterEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:pmoailhcsRinvBoosterEntry.setStatus(_A)
class _PmoailhcsRinvBoosterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoailhcsRinvBoosterIndex_Type.__name__=_D
_PmoailhcsRinvBoosterIndex_Object=MibTableColumn
pmoailhcsRinvBoosterIndex=_PmoailhcsRinvBoosterIndex_Object((1,3,6,1,4,1,20044,62,7,7,1,1),_PmoailhcsRinvBoosterIndex_Type())
pmoailhcsRinvBoosterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvBoosterIndex.setStatus(_A)
_PmoailhcsRinvBooster_Type=DisplayString
_PmoailhcsRinvBooster_Object=MibTableColumn
pmoailhcsRinvBooster=_PmoailhcsRinvBooster_Object((1,3,6,1,4,1,20044,62,7,7,1,2),_PmoailhcsRinvBooster_Type())
pmoailhcsRinvBooster.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvBooster.setStatus(_A)
_PmoailhcsRinvPreAmpTable_Object=MibTable
pmoailhcsRinvPreAmpTable=_PmoailhcsRinvPreAmpTable_Object((1,3,6,1,4,1,20044,62,7,8))
if mibBuilder.loadTexts:pmoailhcsRinvPreAmpTable.setStatus(_A)
_PmoailhcsRinvPreAmpEntry_Object=MibTableRow
pmoailhcsRinvPreAmpEntry=_PmoailhcsRinvPreAmpEntry_Object((1,3,6,1,4,1,20044,62,7,8,1))
pmoailhcsRinvPreAmpEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:pmoailhcsRinvPreAmpEntry.setStatus(_A)
class _PmoailhcsRinvPreAmpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PmoailhcsRinvPreAmpIndex_Type.__name__=_D
_PmoailhcsRinvPreAmpIndex_Object=MibTableColumn
pmoailhcsRinvPreAmpIndex=_PmoailhcsRinvPreAmpIndex_Object((1,3,6,1,4,1,20044,62,7,8,1,1),_PmoailhcsRinvPreAmpIndex_Type())
pmoailhcsRinvPreAmpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvPreAmpIndex.setStatus(_A)
_PmoailhcsRinvPreAmp_Type=DisplayString
_PmoailhcsRinvPreAmp_Object=MibTableColumn
pmoailhcsRinvPreAmp=_PmoailhcsRinvPreAmp_Object((1,3,6,1,4,1,20044,62,7,8,1,2),_PmoailhcsRinvPreAmp_Type())
pmoailhcsRinvPreAmp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsRinvPreAmp.setStatus(_A)
_PmoailhcsConfig_ObjectIdentity=ObjectIdentity
pmoailhcsConfig=_PmoailhcsConfig_ObjectIdentity((1,3,6,1,4,1,20044,62,9))
_PmoailhcsCfgNoValue_ObjectIdentity=ObjectIdentity
pmoailhcsCfgNoValue=_PmoailhcsCfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,62,9,1))
_PmoailhcstableclientStartup_ObjectIdentity=ObjectIdentity
pmoailhcstableclientStartup=_PmoailhcstableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,62,9,1,1))
class _PmoailhcsCfgclientEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientEdfaLaserCtrl_Type.__name__=_F
_PmoailhcsCfgclientEdfaLaserCtrl_Object=MibScalar
pmoailhcsCfgclientEdfaLaserCtrl=_PmoailhcsCfgclientEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,62,9,1,1,2),_PmoailhcsCfgclientEdfaLaserCtrl_Type())
pmoailhcsCfgclientEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientEdfaLaserCtrl.setStatus(_A)
class _PmoailhcsCfgclientEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientEdfaLaserMode_Type.__name__=_F
_PmoailhcsCfgclientEdfaLaserMode_Object=MibScalar
pmoailhcsCfgclientEdfaLaserMode=_PmoailhcsCfgclientEdfaLaserMode_Object((1,3,6,1,4,1,20044,62,9,1,1,3),_PmoailhcsCfgclientEdfaLaserMode_Type())
pmoailhcsCfgclientEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientEdfaLaserMode.setStatus(_A)
class _PmoailhcsCfgclientGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientGainValue_Type.__name__=_F
_PmoailhcsCfgclientGainValue_Object=MibScalar
pmoailhcsCfgclientGainValue=_PmoailhcsCfgclientGainValue_Object((1,3,6,1,4,1,20044,62,9,1,1,4),_PmoailhcsCfgclientGainValue_Type())
pmoailhcsCfgclientGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientGainValue.setStatus(_A)
class _PmoailhcsCfgclientTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientTiltValue_Type.__name__=_F
_PmoailhcsCfgclientTiltValue_Object=MibScalar
pmoailhcsCfgclientTiltValue=_PmoailhcsCfgclientTiltValue_Object((1,3,6,1,4,1,20044,62,9,1,1,5),_PmoailhcsCfgclientTiltValue_Type())
pmoailhcsCfgclientTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientTiltValue.setStatus(_A)
class _PmoailhcsCfgclientMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientMsaLoss_Type.__name__=_F
_PmoailhcsCfgclientMsaLoss_Object=MibScalar
pmoailhcsCfgclientMsaLoss=_PmoailhcsCfgclientMsaLoss_Object((1,3,6,1,4,1,20044,62,9,1,1,6),_PmoailhcsCfgclientMsaLoss_Type())
pmoailhcsCfgclientMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientMsaLoss.setStatus(_A)
class _PmoailhcsCfgclientOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientOutputPowerValue_Type.__name__=_F
_PmoailhcsCfgclientOutputPowerValue_Object=MibScalar
pmoailhcsCfgclientOutputPowerValue=_PmoailhcsCfgclientOutputPowerValue_Object((1,3,6,1,4,1,20044,62,9,1,1,7),_PmoailhcsCfgclientOutputPowerValue_Type())
pmoailhcsCfgclientOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientOutputPowerValue.setStatus(_A)
class _PmoailhcsCfgclientAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgclientAseCompensation_Type.__name__=_F
_PmoailhcsCfgclientAseCompensation_Object=MibScalar
pmoailhcsCfgclientAseCompensation=_PmoailhcsCfgclientAseCompensation_Object((1,3,6,1,4,1,20044,62,9,1,1,8),_PmoailhcsCfgclientAseCompensation_Type())
pmoailhcsCfgclientAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgclientAseCompensation.setStatus(_A)
_PmoailhcsCfgLineStartUp_ObjectIdentity=ObjectIdentity
pmoailhcsCfgLineStartUp=_PmoailhcsCfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,62,9,2))
_PmoailhcstablelineStartup_ObjectIdentity=ObjectIdentity
pmoailhcstablelineStartup=_PmoailhcstablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,62,9,2,1))
class _PmoailhcsCfglineEdfaLaserCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineEdfaLaserCtrl_Type.__name__=_F
_PmoailhcsCfglineEdfaLaserCtrl_Object=MibScalar
pmoailhcsCfglineEdfaLaserCtrl=_PmoailhcsCfglineEdfaLaserCtrl_Object((1,3,6,1,4,1,20044,62,9,2,1,2),_PmoailhcsCfglineEdfaLaserCtrl_Type())
pmoailhcsCfglineEdfaLaserCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineEdfaLaserCtrl.setStatus(_A)
class _PmoailhcsCfglineEdfaLaserMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineEdfaLaserMode_Type.__name__=_F
_PmoailhcsCfglineEdfaLaserMode_Object=MibScalar
pmoailhcsCfglineEdfaLaserMode=_PmoailhcsCfglineEdfaLaserMode_Object((1,3,6,1,4,1,20044,62,9,2,1,3),_PmoailhcsCfglineEdfaLaserMode_Type())
pmoailhcsCfglineEdfaLaserMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineEdfaLaserMode.setStatus(_A)
class _PmoailhcsCfglineGainValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineGainValue_Type.__name__=_F
_PmoailhcsCfglineGainValue_Object=MibScalar
pmoailhcsCfglineGainValue=_PmoailhcsCfglineGainValue_Object((1,3,6,1,4,1,20044,62,9,2,1,4),_PmoailhcsCfglineGainValue_Type())
pmoailhcsCfglineGainValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineGainValue.setStatus(_A)
class _PmoailhcsCfglineTiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineTiltValue_Type.__name__=_F
_PmoailhcsCfglineTiltValue_Object=MibScalar
pmoailhcsCfglineTiltValue=_PmoailhcsCfglineTiltValue_Object((1,3,6,1,4,1,20044,62,9,2,1,5),_PmoailhcsCfglineTiltValue_Type())
pmoailhcsCfglineTiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineTiltValue.setStatus(_A)
class _PmoailhcsCfglineMsaLoss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineMsaLoss_Type.__name__=_F
_PmoailhcsCfglineMsaLoss_Object=MibScalar
pmoailhcsCfglineMsaLoss=_PmoailhcsCfglineMsaLoss_Object((1,3,6,1,4,1,20044,62,9,2,1,6),_PmoailhcsCfglineMsaLoss_Type())
pmoailhcsCfglineMsaLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineMsaLoss.setStatus(_A)
class _PmoailhcsCfglineOutputPowerValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineOutputPowerValue_Type.__name__=_F
_PmoailhcsCfglineOutputPowerValue_Object=MibScalar
pmoailhcsCfglineOutputPowerValue=_PmoailhcsCfglineOutputPowerValue_Object((1,3,6,1,4,1,20044,62,9,2,1,7),_PmoailhcsCfglineOutputPowerValue_Type())
pmoailhcsCfglineOutputPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineOutputPowerValue.setStatus(_A)
class _PmoailhcsCfglineAseCompensation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfglineAseCompensation_Type.__name__=_F
_PmoailhcsCfglineAseCompensation_Object=MibScalar
pmoailhcsCfglineAseCompensation=_PmoailhcsCfglineAseCompensation_Object((1,3,6,1,4,1,20044,62,9,2,1,8),_PmoailhcsCfglineAseCompensation_Type())
pmoailhcsCfglineAseCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfglineAseCompensation.setStatus(_A)
class _PmoailhcsCfgaprMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgaprMode_Type.__name__=_F
_PmoailhcsCfgaprMode_Object=MibScalar
pmoailhcsCfgaprMode=_PmoailhcsCfgaprMode_Object((1,3,6,1,4,1,20044,62,9,2,1,11),_PmoailhcsCfgaprMode_Type())
pmoailhcsCfgaprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgaprMode.setStatus(_A)
_PmoailhcsCfgClientSupvStartUp_ObjectIdentity=ObjectIdentity
pmoailhcsCfgClientSupvStartUp=_PmoailhcsCfgClientSupvStartUp_ObjectIdentity((1,3,6,1,4,1,20044,62,9,3))
_PmoailhcsCfgLineStartupTable_Object=MibTable
pmoailhcsCfgLineStartupTable=_PmoailhcsCfgLineStartupTable_Object((1,3,6,1,4,1,20044,62,9,3,1))
if mibBuilder.loadTexts:pmoailhcsCfgLineStartupTable.setStatus(_A)
_PmoailhcsCfgLineStartupEntry_Object=MibTableRow
pmoailhcsCfgLineStartupEntry=_PmoailhcsCfgLineStartupEntry_Object((1,3,6,1,4,1,20044,62,9,3,1,1))
pmoailhcsCfgLineStartupEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:pmoailhcsCfgLineStartupEntry.setStatus(_A)
class _PmoailhcsCfgLineStartupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsCfgLineStartupIndex_Type.__name__=_D
_PmoailhcsCfgLineStartupIndex_Object=MibTableColumn
pmoailhcsCfgLineStartupIndex=_PmoailhcsCfgLineStartupIndex_Object((1,3,6,1,4,1,20044,62,9,3,1,1,1),_PmoailhcsCfgLineStartupIndex_Type())
pmoailhcsCfgLineStartupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCfgLineStartupIndex.setStatus(_A)
class _PmoailhcsCfgLineOscLaserCtrlPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgLineOscLaserCtrlPortn_Type.__name__=_F
_PmoailhcsCfgLineOscLaserCtrlPortn_Object=MibTableColumn
pmoailhcsCfgLineOscLaserCtrlPortn=_PmoailhcsCfgLineOscLaserCtrlPortn_Object((1,3,6,1,4,1,20044,62,9,3,1,1,3),_PmoailhcsCfgLineOscLaserCtrlPortn_Type())
pmoailhcsCfgLineOscLaserCtrlPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgLineOscLaserCtrlPortn.setStatus(_A)
class _PmoailhcsCfgLineOscOosPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgLineOscOosPortn_Type.__name__=_F
_PmoailhcsCfgLineOscOosPortn_Object=MibTableColumn
pmoailhcsCfgLineOscOosPortn=_PmoailhcsCfgLineOscOosPortn_Object((1,3,6,1,4,1,20044,62,9,3,1,1,4),_PmoailhcsCfgLineOscOosPortn_Type())
pmoailhcsCfgLineOscOosPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgLineOscOosPortn.setStatus(_A)
class _PmoailhcsCfgLineOscSpanLengthPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgLineOscSpanLengthPortn_Type.__name__=_F
_PmoailhcsCfgLineOscSpanLengthPortn_Object=MibTableColumn
pmoailhcsCfgLineOscSpanLengthPortn=_PmoailhcsCfgLineOscSpanLengthPortn_Object((1,3,6,1,4,1,20044,62,9,3,1,1,5),_PmoailhcsCfgLineOscSpanLengthPortn_Type())
pmoailhcsCfgLineOscSpanLengthPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgLineOscSpanLengthPortn.setStatus(_A)
class _PmoailhcsCfgLineOscCorrectionFactorPortn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmoailhcsCfgLineOscCorrectionFactorPortn_Type.__name__=_F
_PmoailhcsCfgLineOscCorrectionFactorPortn_Object=MibTableColumn
pmoailhcsCfgLineOscCorrectionFactorPortn=_PmoailhcsCfgLineOscCorrectionFactorPortn_Object((1,3,6,1,4,1,20044,62,9,3,1,1,6),_PmoailhcsCfgLineOscCorrectionFactorPortn_Type())
pmoailhcsCfgLineOscCorrectionFactorPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgLineOscCorrectionFactorPortn.setStatus(_A)
_PmoailhcsCfgLabels_ObjectIdentity=ObjectIdentity
pmoailhcsCfgLabels=_PmoailhcsCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,62,9,4))
_PmoailhcsCfgLabelclientTable_Object=MibTable
pmoailhcsCfgLabelclientTable=_PmoailhcsCfgLabelclientTable_Object((1,3,6,1,4,1,20044,62,9,4,1))
if mibBuilder.loadTexts:pmoailhcsCfgLabelclientTable.setStatus(_A)
_PmoailhcsCfgLabelclientEntry_Object=MibTableRow
pmoailhcsCfgLabelclientEntry=_PmoailhcsCfgLabelclientEntry_Object((1,3,6,1,4,1,20044,62,9,4,1,1))
pmoailhcsCfgLabelclientEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:pmoailhcsCfgLabelclientEntry.setStatus(_A)
class _PmoailhcsCfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsCfgLabelclientIndex_Type.__name__=_D
_PmoailhcsCfgLabelclientIndex_Object=MibTableColumn
pmoailhcsCfgLabelclientIndex=_PmoailhcsCfgLabelclientIndex_Object((1,3,6,1,4,1,20044,62,9,4,1,1,1),_PmoailhcsCfgLabelclientIndex_Type())
pmoailhcsCfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCfgLabelclientIndex.setStatus(_A)
class _PmoailhcsCfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoailhcsCfgLabelclientPortn_Type.__name__=_H
_PmoailhcsCfgLabelclientPortn_Object=MibTableColumn
pmoailhcsCfgLabelclientPortn=_PmoailhcsCfgLabelclientPortn_Object((1,3,6,1,4,1,20044,62,9,4,1,1,3),_PmoailhcsCfgLabelclientPortn_Type())
pmoailhcsCfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgLabelclientPortn.setStatus(_A)
_PmoailhcsCfgLabellineTable_Object=MibTable
pmoailhcsCfgLabellineTable=_PmoailhcsCfgLabellineTable_Object((1,3,6,1,4,1,20044,62,9,4,2))
if mibBuilder.loadTexts:pmoailhcsCfgLabellineTable.setStatus(_A)
_PmoailhcsCfgLabellineEntry_Object=MibTableRow
pmoailhcsCfgLabellineEntry=_PmoailhcsCfgLabellineEntry_Object((1,3,6,1,4,1,20044,62,9,4,2,1))
pmoailhcsCfgLabellineEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:pmoailhcsCfgLabellineEntry.setStatus(_A)
class _PmoailhcsCfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_PmoailhcsCfgLabellineIndex_Type.__name__=_D
_PmoailhcsCfgLabellineIndex_Object=MibTableColumn
pmoailhcsCfgLabellineIndex=_PmoailhcsCfgLabellineIndex_Object((1,3,6,1,4,1,20044,62,9,4,2,1,1),_PmoailhcsCfgLabellineIndex_Type())
pmoailhcsCfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcsCfgLabellineIndex.setStatus(_A)
class _PmoailhcsCfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_PmoailhcsCfgLabellinePortn_Type.__name__=_H
_PmoailhcsCfgLabellinePortn_Object=MibTableColumn
pmoailhcsCfgLabellinePortn=_PmoailhcsCfgLabellinePortn_Object((1,3,6,1,4,1,20044,62,9,4,2,1,3),_PmoailhcsCfgLabellinePortn_Type())
pmoailhcsCfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgLabellinePortn.setStatus(_A)
_PmoailhcsCfgWriteConfiguration_Type=EkiOnOff
_PmoailhcsCfgWriteConfiguration_Object=MibScalar
pmoailhcsCfgWriteConfiguration=_PmoailhcsCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,62,9,257),_PmoailhcsCfgWriteConfiguration_Type())
pmoailhcsCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmoailhcsCfgWriteConfiguration.setStatus(_A)
_Pmoailhcstraps_ObjectIdentity=ObjectIdentity
pmoailhcstraps=_Pmoailhcstraps_ObjectIdentity((1,3,6,1,4,1,20044,62,10))
class _PmoailhcstrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmoailhcstrapBoardNumber_Type.__name__=_D
_PmoailhcstrapBoardNumber_Object=MibScalar
pmoailhcstrapBoardNumber=_PmoailhcstrapBoardNumber_Object((1,3,6,1,4,1,20044,62,10,4),_PmoailhcstrapBoardNumber_Type())
pmoailhcstrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmoailhcstrapBoardNumber.setStatus(_A)
pmoailhcsLineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,62,10,34))
pmoailhcsLineTrapCritGoesOn.setObjects(*((_E,_I),(_E,_J),(_E,_G)))
if mibBuilder.loadTexts:pmoailhcsLineTrapCritGoesOn.setStatus(_A)
pmoailhcsLineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,62,10,35))
pmoailhcsLineTrapCritGoesOff.setObjects(*((_E,_I),(_E,_J),(_E,_G)))
if mibBuilder.loadTexts:pmoailhcsLineTrapCritGoesOff.setStatus(_A)
pmoailhcsClientTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,62,10,44))
pmoailhcsClientTrapCritGoesOn.setObjects(*((_E,_K),(_E,_L),(_E,_G)))
if mibBuilder.loadTexts:pmoailhcsClientTrapCritGoesOn.setStatus(_A)
pmoailhcsClientTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,62,10,45))
pmoailhcsClientTrapCritGoesOff.setObjects(*((_E,_K),(_E,_L),(_E,_G)))
if mibBuilder.loadTexts:pmoailhcsClientTrapCritGoesOff.setStatus(_A)
pmoailhcsPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,62,10,50))
pmoailhcsPowerTrapUrgentGoesOn.setObjects(*((_E,_M),(_E,_N),(_E,_G)))
if mibBuilder.loadTexts:pmoailhcsPowerTrapUrgentGoesOn.setStatus(_A)
pmoailhcsPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,62,10,51))
pmoailhcsPowerTrapUrgentGoesOff.setObjects(*((_E,_M),(_E,_N),(_E,_G)))
if mibBuilder.loadTexts:pmoailhcsPowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PmoailhcspreampMode':PmoailhcspreampMode,'PmoailhcsboosterMode':PmoailhcsboosterMode,'PmoailhcsaprMode':PmoailhcsaprMode,'PmoailhcsPreampGainAdjMode':PmoailhcsPreampGainAdjMode,'PmoailhcsBoosterGainAdjMode':PmoailhcsBoosterGainAdjMode,'PmoailhcsPreampCstGainAdjMode':PmoailhcsPreampCstGainAdjMode,'PmoailhcsBoosterCstGainAdjMode':PmoailhcsBoosterCstGainAdjMode,'modulepmoailhcs':modulepmoailhcs,'pmoailhcsalarms':pmoailhcsalarms,'pmoailhcsAlmOther':pmoailhcsAlmOther,'pmoailhcsAlmOtherNurg':pmoailhcsAlmOtherNurg,'pmoailhcsAlmsynthAlm2':pmoailhcsAlmsynthAlm2,'pmoailhcsAlmConfTableSave':pmoailhcsAlmConfTableSave,'pmoailhcsAlmInvUpload':pmoailhcsAlmInvUpload,'pmoailhcsAlmConfTableLoad':pmoailhcsAlmConfTableLoad,'pmoailhcsAlmfoaWarnings':pmoailhcsAlmfoaWarnings,'pmoailhcsAlmTermpLowWarning':pmoailhcsAlmTermpLowWarning,'pmoailhcsAlmTempHighWarning':pmoailhcsAlmTempHighWarning,'pmoailhcsAlmOtherUrg':pmoailhcsAlmOtherUrg,'pmoailhcsAlmfoaAlarms':pmoailhcsAlmfoaAlarms,'pmoailhcsAlmTermpLowAlarm':pmoailhcsAlmTermpLowAlarm,'pmoailhcsAlmTempHighAlarm':pmoailhcsAlmTempHighAlarm,'pmoailhcsAlmOtherCrit':pmoailhcsAlmOtherCrit,'pmoailhcsAlmsynthAlm0':pmoailhcsAlmsynthAlm0,'pmoailhcsAlmMaintenanceMode':pmoailhcsAlmMaintenanceMode,'pmoailhcsAlmAprOn':pmoailhcsAlmAprOn,'pmoailhcsAlmModGlobFail':pmoailhcsAlmModGlobFail,'pmoailhcsAlmUpEdfaInitNotCompl':pmoailhcsAlmUpEdfaInitNotCompl,'pmoailhcsAlmDwEdfaInitNotCompl':pmoailhcsAlmDwEdfaInitNotCompl,'pmoailhcsAlmExtPump1NotLocked':pmoailhcsAlmExtPump1NotLocked,_N:pmoailhcsAlmDefFuseA,_M:pmoailhcsAlmDefFuseB,'pmoailhcsAlmClient':pmoailhcsAlmClient,'pmoailhcsAlmClientNurg':pmoailhcsAlmClientNurg,'pmoailhcsAlmclientEdfaWarnings':pmoailhcsAlmclientEdfaWarnings,'pmoailhcsAlmClientGainLowWarning':pmoailhcsAlmClientGainLowWarning,'pmoailhcsAlmClientGainHighWarning':pmoailhcsAlmClientGainHighWarning,'pmoailhcsAlmClientInputPwrLowWarning':pmoailhcsAlmClientInputPwrLowWarning,'pmoailhcsAlmClientInputPwrHighWarning':pmoailhcsAlmClientInputPwrHighWarning,'pmoailhcsAlmClientOutputPwrLowWarning':pmoailhcsAlmClientOutputPwrLowWarning,'pmoailhcsAlmClientOutputPwrHighWarning':pmoailhcsAlmClientOutputPwrHighWarning,'pmoailhcsAlmClientBiasLowWarning':pmoailhcsAlmClientBiasLowWarning,'pmoailhcsAlmClientBiasHighWarning':pmoailhcsAlmClientBiasHighWarning,'pmoailhcsAlmClientUrg':pmoailhcsAlmClientUrg,'pmoailhcsAlmclientEdfaAlarms1':pmoailhcsAlmclientEdfaAlarms1,'pmoailhcsAlmClientGainLowAlarm':pmoailhcsAlmClientGainLowAlarm,'pmoailhcsAlmClientGainHighAlarm':pmoailhcsAlmClientGainHighAlarm,'pmoailhcsAlmClientInputPwrLowAlarm':pmoailhcsAlmClientInputPwrLowAlarm,'pmoailhcsAlmClientInputPwrHighAlarm':pmoailhcsAlmClientInputPwrHighAlarm,'pmoailhcsAlmClientOutputPwrLowAlarm':pmoailhcsAlmClientOutputPwrLowAlarm,'pmoailhcsAlmClientOutputPwrHighAlarm':pmoailhcsAlmClientOutputPwrHighAlarm,'pmoailhcsAlmClientBiasLowAlarm':pmoailhcsAlmClientBiasLowAlarm,'pmoailhcsAlmClientBiasHighAlarm':pmoailhcsAlmClientBiasHighAlarm,'pmoailhcsAlmClientCrit':pmoailhcsAlmClientCrit,'pmoailhcsAlmsynthAlm8':pmoailhcsAlmsynthAlm8,_L:pmoailhcsAlmClientHwFail,'pmoailhcsAlmClientTxOff':pmoailhcsAlmClientTxOff,_K:pmoailhcsAlmClientFail,'pmoailhcsAlmClientExtPumpFail':pmoailhcsAlmClientExtPumpFail,'pmoailhcsAlmSupvbFail':pmoailhcsAlmSupvbFail,'pmoailhcsAlmclientEdfaAlarms2':pmoailhcsAlmclientEdfaAlarms2,'pmoailhcsAlmClientEdfaNr':pmoailhcsAlmClientEdfaNr,'pmoailhcsAlmClientEdfaTecFail':pmoailhcsAlmClientEdfaTecFail,'pmoailhcsAlmClientEdfaLaserFail':pmoailhcsAlmClientEdfaLaserFail,'pmoailhcsAlmClientEdfaLos':pmoailhcsAlmClientEdfaLos,'pmoailhcsAlmClientExtPumpEdfaLowCurrent':pmoailhcsAlmClientExtPumpEdfaLowCurrent,'pmoailhcsAlmClientGainOutOfRange':pmoailhcsAlmClientGainOutOfRange,'pmoailhcsAlmclientMsaAlarms':pmoailhcsAlmclientMsaAlarms,'pmoailhcsAlmClientMsaLos':pmoailhcsAlmClientMsaLos,'pmoailhcsAlmClientMsaAttenuation':pmoailhcsAlmClientMsaAttenuation,'pmoailhcsAlmLine':pmoailhcsAlmLine,'pmoailhcsAlmLineNurg':pmoailhcsAlmLineNurg,'pmoailhcsAlmlineEdfaWarnings':pmoailhcsAlmlineEdfaWarnings,'pmoailhcsAlmLineGainLowWarning':pmoailhcsAlmLineGainLowWarning,'pmoailhcsAlmLineGainHighWarning':pmoailhcsAlmLineGainHighWarning,'pmoailhcsAlmLineInputPwrLowWarning':pmoailhcsAlmLineInputPwrLowWarning,'pmoailhcsAlmLineInputPwrHighWarning':pmoailhcsAlmLineInputPwrHighWarning,'pmoailhcsAlmLineOutputPwrLowWarning':pmoailhcsAlmLineOutputPwrLowWarning,'pmoailhcsAlmLineOutputPwrHighWarning':pmoailhcsAlmLineOutputPwrHighWarning,'pmoailhcsAlmLineBiasLowWarning':pmoailhcsAlmLineBiasLowWarning,'pmoailhcsAlmLineBiasHighWarning':pmoailhcsAlmLineBiasHighWarning,'pmoailhcsAlmLineUrg':pmoailhcsAlmLineUrg,'pmoailhcsAlmlineEdfaAlarms1':pmoailhcsAlmlineEdfaAlarms1,'pmoailhcsAlmLineGainLowAlarm':pmoailhcsAlmLineGainLowAlarm,'pmoailhcsAlmLineGainHighAlarm':pmoailhcsAlmLineGainHighAlarm,'pmoailhcsAlmLineInputPwrLowAlarm':pmoailhcsAlmLineInputPwrLowAlarm,'pmoailhcsAlmLineInputPwrHighAlarm':pmoailhcsAlmLineInputPwrHighAlarm,'pmoailhcsAlmLineOutputPwrLowAlarm':pmoailhcsAlmLineOutputPwrLowAlarm,'pmoailhcsAlmLineOutputPwrHighAlarm':pmoailhcsAlmLineOutputPwrHighAlarm,'pmoailhcsAlmLineBiasLowAlarm':pmoailhcsAlmLineBiasLowAlarm,'pmoailhcsAlmLineBiasHighAlarm':pmoailhcsAlmLineBiasHighAlarm,'pmoailhcsAlmLineCrit':pmoailhcsAlmLineCrit,'pmoailhcsAlmsynthAlm7':pmoailhcsAlmsynthAlm7,_J:pmoailhcsAlmLineHwFail,'pmoailhcsAlmLineTxOff':pmoailhcsAlmLineTxOff,_I:pmoailhcsAlmLineFail,'pmoailhcsAlmLineExtPumpFail':pmoailhcsAlmLineExtPumpFail,'pmoailhcsAlmSupvaFail':pmoailhcsAlmSupvaFail,'pmoailhcsAlmlineEdfaAlarms2':pmoailhcsAlmlineEdfaAlarms2,'pmoailhcsAlmLineEdfaNr':pmoailhcsAlmLineEdfaNr,'pmoailhcsAlmLineEdfaTecFail':pmoailhcsAlmLineEdfaTecFail,'pmoailhcsAlmLineEdfaLaserFail':pmoailhcsAlmLineEdfaLaserFail,'pmoailhcsAlmLineEdfaLos':pmoailhcsAlmLineEdfaLos,'pmoailhcsAlmLineExtPumpEdfaLowCurrent':pmoailhcsAlmLineExtPumpEdfaLowCurrent,'pmoailhcsAlmLineGainOutOfRange':pmoailhcsAlmLineGainOutOfRange,'pmoailhcsAlmlineMsaAlarms':pmoailhcsAlmlineMsaAlarms,'pmoailhcsAlmLineMsaLos':pmoailhcsAlmLineMsaLos,'pmoailhcsAlmLineMsaAttenuation':pmoailhcsAlmLineMsaAttenuation,'pmoailhcsAlmlineOscAlarmsTable':pmoailhcsAlmlineOscAlarmsTable,'pmoailhcsAlmlineOscAlarmsEntry':pmoailhcsAlmlineOscAlarmsEntry,_P:pmoailhcsAlmlineOscAlarmsIndex,'pmoailhcsAlmLineLosPortn':pmoailhcsAlmLineLosPortn,'pmoailhcsAlmLineTxOffPortn':pmoailhcsAlmLineTxOffPortn,'pmoailhcsAlmLineTxFailPortn':pmoailhcsAlmLineTxFailPortn,'pmoailhcsAlmLineFecFailPortn':pmoailhcsAlmLineFecFailPortn,'pmoailhcsAlmLineOosPortn':pmoailhcsAlmLineOosPortn,'pmoailhcsAlmLineLofPortn':pmoailhcsAlmLineLofPortn,'pmoailhcsAlmLineOofPortn':pmoailhcsAlmLineOofPortn,'pmoailhcsAlmLineRemoteTxFailPortn':pmoailhcsAlmLineRemoteTxFailPortn,'pmoailhcsAlmLineWarningPortn':pmoailhcsAlmLineWarningPortn,'pmoailhcsAlmLineAlmPortn':pmoailhcsAlmLineAlmPortn,'pmoailhcsAlmlineOscThresholdAlarmsTable':pmoailhcsAlmlineOscThresholdAlarmsTable,'pmoailhcsAlmlineOscThresholdAlarmsEntry':pmoailhcsAlmlineOscThresholdAlarmsEntry,_Q:pmoailhcsAlmlineOscThresholdAlarmsIndex,'pmoailhcsAlmLineTxPwrLowAlarmPortn':pmoailhcsAlmLineTxPwrLowAlarmPortn,'pmoailhcsAlmLineTxPwrHighAlarmPortn':pmoailhcsAlmLineTxPwrHighAlarmPortn,'pmoailhcsAlmLineRxPwrLowAlarmPortn':pmoailhcsAlmLineRxPwrLowAlarmPortn,'pmoailhcsAlmLineRxPwrHighAlarmPortn':pmoailhcsAlmLineRxPwrHighAlarmPortn,'pmoailhcsAlmLineSpanlossLowAlarmPortn':pmoailhcsAlmLineSpanlossLowAlarmPortn,'pmoailhcsAlmLineSpanlossHighAlarmPortn':pmoailhcsAlmLineSpanlossHighAlarmPortn,'pmoailhcsAlmLineOscBiasLowAlarmPortn':pmoailhcsAlmLineOscBiasLowAlarmPortn,'pmoailhcsAlmLineOscBiasHighAlarmPortn':pmoailhcsAlmLineOscBiasHighAlarmPortn,'pmoailhcsAlmlineOscThresholdsWarningsTable':pmoailhcsAlmlineOscThresholdsWarningsTable,'pmoailhcsAlmlineOscThresholdsWarningsEntry':pmoailhcsAlmlineOscThresholdsWarningsEntry,_R:pmoailhcsAlmlineOscThresholdsWarningsIndex,'pmoailhcsAlmLineTxPwrLowWarningPortn':pmoailhcsAlmLineTxPwrLowWarningPortn,'pmoailhcsAlmLineTxPwrHighWarningPortn':pmoailhcsAlmLineTxPwrHighWarningPortn,'pmoailhcsAlmLineRxPwrLowWarningPortn':pmoailhcsAlmLineRxPwrLowWarningPortn,'pmoailhcsAlmLineRxPwrHighWarningPortn':pmoailhcsAlmLineRxPwrHighWarningPortn,'pmoailhcsAlmLineSpanlossLowWarningPortn':pmoailhcsAlmLineSpanlossLowWarningPortn,'pmoailhcsAlmLineSpanlossHighWarningPortn':pmoailhcsAlmLineSpanlossHighWarningPortn,'pmoailhcsAlmLineOscBiasLowWarningPortn':pmoailhcsAlmLineOscBiasLowWarningPortn,'pmoailhcsAlmLineOscBiasHighWarningPortn':pmoailhcsAlmLineOscBiasHighWarningPortn,'pmoailhcsmeasures':pmoailhcsmeasures,'pmoailhcsMesrOther':pmoailhcsMesrOther,'pmoailhcsMesrtempMeas':pmoailhcsMesrtempMeas,'pmoailhcsMesrClient':pmoailhcsMesrClient,'pmoailhcsMesrclientEdfaBiasMeas':pmoailhcsMesrclientEdfaBiasMeas,'pmoailhcsMesrclientEdfaTxpwrMeas':pmoailhcsMesrclientEdfaTxpwrMeas,'pmoailhcsMesrclientEdfaRxpwrMeas':pmoailhcsMesrclientEdfaRxpwrMeas,'pmoailhcsMesrclientEdfaGainMeas':pmoailhcsMesrclientEdfaGainMeas,'pmoailhcsMesrclientOscSpanLoss':pmoailhcsMesrclientOscSpanLoss,'pmoailhcsMesrclientOscSpanLossRef':pmoailhcsMesrclientOscSpanLossRef,'pmoailhcsMesrclientCorrectedGain':pmoailhcsMesrclientCorrectedGain,'pmoailhcsMesrclientMsaInputPower':pmoailhcsMesrclientMsaInputPower,'pmoailhcsMesrclientMsaOutputPower':pmoailhcsMesrclientMsaOutputPower,'pmoailhcsMesrclientMsaAttenuation':pmoailhcsMesrclientMsaAttenuation,'pmoailhcsMesrclientMsaAttenuationRef':pmoailhcsMesrclientMsaAttenuationRef,'pmoailhcsMesrLine':pmoailhcsMesrLine,'pmoailhcsMesrlineEdfaBiasMeas':pmoailhcsMesrlineEdfaBiasMeas,'pmoailhcsMesrlineEdfaTxpwrMeas':pmoailhcsMesrlineEdfaTxpwrMeas,'pmoailhcsMesrlineEdfaRxpwrMeas':pmoailhcsMesrlineEdfaRxpwrMeas,'pmoailhcsMesrlineEdfaGainMeas':pmoailhcsMesrlineEdfaGainMeas,'pmoailhcsMesrlineOscSpanLoss':pmoailhcsMesrlineOscSpanLoss,'pmoailhcsMesrlineOscSpanLossRef':pmoailhcsMesrlineOscSpanLossRef,'pmoailhcsMesrlineCorrectedGain':pmoailhcsMesrlineCorrectedGain,'pmoailhcsMesrlineMsaInputPower':pmoailhcsMesrlineMsaInputPower,'pmoailhcsMesrlineMsaOutputPower':pmoailhcsMesrlineMsaOutputPower,'pmoailhcsMesrlineMsaAttenuation':pmoailhcsMesrlineMsaAttenuation,'pmoailhcsMesrlineMsaAttenuationRef':pmoailhcsMesrlineMsaAttenuationRef,'pmoailhcsMesrlineOscTxPowerTable':pmoailhcsMesrlineOscTxPowerTable,'pmoailhcsMesrlineOscTxPowerEntry':pmoailhcsMesrlineOscTxPowerEntry,_S:pmoailhcsMesrlineOscTxPowerIndex,'pmoailhcsMesrlineOscTxPowerPortn':pmoailhcsMesrlineOscTxPowerPortn,'pmoailhcsMesrlineOscRxPowerTable':pmoailhcsMesrlineOscRxPowerTable,'pmoailhcsMesrlineOscRxPowerEntry':pmoailhcsMesrlineOscRxPowerEntry,_T:pmoailhcsMesrlineOscRxPowerIndex,'pmoailhcsMesrlineOscRxPowerPortn':pmoailhcsMesrlineOscRxPowerPortn,'pmoailhcscounters':pmoailhcscounters,'pmoailhcsCntOther':pmoailhcsCntOther,'pmoailhcsCntClient':pmoailhcsCntClient,'pmoailhcsCntLine':pmoailhcsCntLine,'pmoailhcsCntlineOscErrTable':pmoailhcsCntlineOscErrTable,'pmoailhcsCntlineOscErrEntry':pmoailhcsCntlineOscErrEntry,_U:pmoailhcsCntlineOscErrIndex,'pmoailhcsCntlineOscErrValuePortn':pmoailhcsCntlineOscErrValuePortn,'pmoailhcsCntlineOscErrErrorPortn':pmoailhcsCntlineOscErrErrorPortn,'pmoailhcsCntlineOscErrOverloadPortn':pmoailhcsCntlineOscErrOverloadPortn,'pmoailhcsCntCountersReset':pmoailhcsCntCountersReset,'pmoailhcsCntCountersStop':pmoailhcsCntCountersStop,'pmoailhcscontrolsWrite':pmoailhcscontrolsWrite,'pmoailhcsCtrlOther':pmoailhcsCtrlOther,'pmoailhcsCtrlsynth0':pmoailhcsCtrlsynth0,'pmoailhcsCtrlConfLoad':pmoailhcsCtrlConfLoad,'pmoailhcsCtrlConfFlash':pmoailhcsCtrlConfFlash,'pmoailhcsCtrlConfClear':pmoailhcsCtrlConfClear,'pmoailhcsCtrlswMgnt':pmoailhcsCtrlswMgnt,'pmoailhcsCtrlColdReset':pmoailhcsCtrlColdReset,'pmoailhcsCtrlWarmReset':pmoailhcsCtrlWarmReset,'pmoailhcsCtrlledTest':pmoailhcsCtrlledTest,'pmoailhcsCtrlGreenLed':pmoailhcsCtrlGreenLed,'pmoailhcsCtrlRedLed':pmoailhcsCtrlRedLed,'pmoailhcsCtrlLedOff':pmoailhcsCtrlLedOff,'pmoailhcsCtrlmaintMode':pmoailhcsCtrlmaintMode,'pmoailhcsCtrlMaintenance':pmoailhcsCtrlMaintenance,'pmoailhcsCtrlaprRestart':pmoailhcsCtrlaprRestart,'pmoailhcsCtrlAprManualRestart':pmoailhcsCtrlAprManualRestart,'pmoailhcsCtrlClient':pmoailhcsCtrlClient,'pmoailhcsCtrlclientOscInputSpanLoss':pmoailhcsCtrlclientOscInputSpanLoss,'pmoailhcsCtrlClientSpanLoss':pmoailhcsCtrlClientSpanLoss,'pmoailhcsCtrlclientGainCstMonitorValue':pmoailhcsCtrlclientGainCstMonitorValue,'pmoailhcsCtrlclientGainSettingValue':pmoailhcsCtrlclientGainSettingValue,'pmoailhcsCtrlclientGainProcessing':pmoailhcsCtrlclientGainProcessing,'pmoailhcsCtrlClientGainProc':pmoailhcsCtrlClientGainProc,'pmoailhcsCtrlclientGainCstFiberAgingMarginValue':pmoailhcsCtrlclientGainCstFiberAgingMarginValue,'pmoailhcsCtrlclientMsaAttenuationValue':pmoailhcsCtrlclientMsaAttenuationValue,'pmoailhcsCtrlClientAttenuation':pmoailhcsCtrlClientAttenuation,'pmoailhcsCtrlLine':pmoailhcsCtrlLine,'pmoailhcsCtrllineOscInputSpanLoss':pmoailhcsCtrllineOscInputSpanLoss,'pmoailhcsCtrlLineSpanLoss':pmoailhcsCtrlLineSpanLoss,'pmoailhcsCtrllineGainCstMonitorValue':pmoailhcsCtrllineGainCstMonitorValue,'pmoailhcsCtrllineGainSettingValue':pmoailhcsCtrllineGainSettingValue,'pmoailhcsCtrllineGainProcessing':pmoailhcsCtrllineGainProcessing,'pmoailhcsCtrlLineGainProc':pmoailhcsCtrlLineGainProc,'pmoailhcsCtrllineGainCstFiberAgingMarginValue':pmoailhcsCtrllineGainCstFiberAgingMarginValue,'pmoailhcsCtrllineMsaAttenuationValue':pmoailhcsCtrllineMsaAttenuationValue,'pmoailhcsCtrlLineAttenuation':pmoailhcsCtrlLineAttenuation,'pmoailhcsri':pmoailhcsri,'pmoailhcsRinvReloadInventory':pmoailhcsRinvReloadInventory,'pmoailhcsRinvHwPlatform':pmoailhcsRinvHwPlatform,'pmoailhcsRinvModulePlatform':pmoailhcsRinvModulePlatform,'pmoailhcsRinvSwPlatform':pmoailhcsRinvSwPlatform,'pmoailhcsRinvGwPlatform':pmoailhcsRinvGwPlatform,'pmoailhcsRinvBoosterTable':pmoailhcsRinvBoosterTable,'pmoailhcsRinvBoosterEntry':pmoailhcsRinvBoosterEntry,_V:pmoailhcsRinvBoosterIndex,'pmoailhcsRinvBooster':pmoailhcsRinvBooster,'pmoailhcsRinvPreAmpTable':pmoailhcsRinvPreAmpTable,'pmoailhcsRinvPreAmpEntry':pmoailhcsRinvPreAmpEntry,_W:pmoailhcsRinvPreAmpIndex,'pmoailhcsRinvPreAmp':pmoailhcsRinvPreAmp,'pmoailhcsConfig':pmoailhcsConfig,'pmoailhcsCfgNoValue':pmoailhcsCfgNoValue,'pmoailhcstableclientStartup':pmoailhcstableclientStartup,'pmoailhcsCfgclientEdfaLaserCtrl':pmoailhcsCfgclientEdfaLaserCtrl,'pmoailhcsCfgclientEdfaLaserMode':pmoailhcsCfgclientEdfaLaserMode,'pmoailhcsCfgclientGainValue':pmoailhcsCfgclientGainValue,'pmoailhcsCfgclientTiltValue':pmoailhcsCfgclientTiltValue,'pmoailhcsCfgclientMsaLoss':pmoailhcsCfgclientMsaLoss,'pmoailhcsCfgclientOutputPowerValue':pmoailhcsCfgclientOutputPowerValue,'pmoailhcsCfgclientAseCompensation':pmoailhcsCfgclientAseCompensation,'pmoailhcsCfgLineStartUp':pmoailhcsCfgLineStartUp,'pmoailhcstablelineStartup':pmoailhcstablelineStartup,'pmoailhcsCfglineEdfaLaserCtrl':pmoailhcsCfglineEdfaLaserCtrl,'pmoailhcsCfglineEdfaLaserMode':pmoailhcsCfglineEdfaLaserMode,'pmoailhcsCfglineGainValue':pmoailhcsCfglineGainValue,'pmoailhcsCfglineTiltValue':pmoailhcsCfglineTiltValue,'pmoailhcsCfglineMsaLoss':pmoailhcsCfglineMsaLoss,'pmoailhcsCfglineOutputPowerValue':pmoailhcsCfglineOutputPowerValue,'pmoailhcsCfglineAseCompensation':pmoailhcsCfglineAseCompensation,'pmoailhcsCfgaprMode':pmoailhcsCfgaprMode,'pmoailhcsCfgClientSupvStartUp':pmoailhcsCfgClientSupvStartUp,'pmoailhcsCfgLineStartupTable':pmoailhcsCfgLineStartupTable,'pmoailhcsCfgLineStartupEntry':pmoailhcsCfgLineStartupEntry,_X:pmoailhcsCfgLineStartupIndex,'pmoailhcsCfgLineOscLaserCtrlPortn':pmoailhcsCfgLineOscLaserCtrlPortn,'pmoailhcsCfgLineOscOosPortn':pmoailhcsCfgLineOscOosPortn,'pmoailhcsCfgLineOscSpanLengthPortn':pmoailhcsCfgLineOscSpanLengthPortn,'pmoailhcsCfgLineOscCorrectionFactorPortn':pmoailhcsCfgLineOscCorrectionFactorPortn,'pmoailhcsCfgLabels':pmoailhcsCfgLabels,'pmoailhcsCfgLabelclientTable':pmoailhcsCfgLabelclientTable,'pmoailhcsCfgLabelclientEntry':pmoailhcsCfgLabelclientEntry,_Y:pmoailhcsCfgLabelclientIndex,'pmoailhcsCfgLabelclientPortn':pmoailhcsCfgLabelclientPortn,'pmoailhcsCfgLabellineTable':pmoailhcsCfgLabellineTable,'pmoailhcsCfgLabellineEntry':pmoailhcsCfgLabellineEntry,_Z:pmoailhcsCfgLabellineIndex,'pmoailhcsCfgLabellinePortn':pmoailhcsCfgLabellinePortn,'pmoailhcsCfgWriteConfiguration':pmoailhcsCfgWriteConfiguration,'pmoailhcstraps':pmoailhcstraps,_G:pmoailhcstrapBoardNumber,'pmoailhcsLineTrapCritGoesOn':pmoailhcsLineTrapCritGoesOn,'pmoailhcsLineTrapCritGoesOff':pmoailhcsLineTrapCritGoesOff,'pmoailhcsClientTrapCritGoesOn':pmoailhcsClientTrapCritGoesOn,'pmoailhcsClientTrapCritGoesOff':pmoailhcsClientTrapCritGoesOff,'pmoailhcsPowerTrapUrgentGoesOn':pmoailhcsPowerTrapUrgentGoesOn,'pmoailhcsPowerTrapUrgentGoesOff':pmoailhcsPowerTrapUrgentGoesOff})