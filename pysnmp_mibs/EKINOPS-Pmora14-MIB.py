_O='pmora14CfgLabellineIndex'
_N='pmora14CfgLabelclientIndex'
_M='pmora14RinvLineIndex'
_L='pmora14AlmDefFuseA'
_K='pmora14AlmDefFuseB'
_J='pmora14AlmLineHwFail'
_I='pmora14AlmLineFail'
_H='DisplayString'
_G='pmora14trapBoardNumber'
_F='Unsigned32'
_E='EKINOPS-Pmora14-MIB'
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
modulepmora14=ModuleIdentity((1,3,6,1,4,1,20044,72))
if mibBuilder.loadTexts:modulepmora14.setRevisions(('2015-08-31 00:00','2016-05-23 00:00'))
class Pmora14PumpsMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ora14maxpowermode',0),('ora14gaincontrolmode',1),('ora14manualcontrolmode',2)))
class Pmora14AprMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ora14aproffmode',0),('ora14aproscmode',1),('ora14aprbrratiomode',2),('ora14aprsbandmode',3),('ora14aprfullmode',4)))
class Pmora14LineFiberTypeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ora14g652mode',0),('ora14g655leafmode',1),('ora14g655truewavemode',2),('ora14g654mode',3),('ora14g653mode',4)))
_Pmora14alarms_ObjectIdentity=ObjectIdentity
pmora14alarms=_Pmora14alarms_ObjectIdentity((1,3,6,1,4,1,20044,72,2))
_Pmora14AlmOther_ObjectIdentity=ObjectIdentity
pmora14AlmOther=_Pmora14AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1))
_Pmora14AlmOtherNurg_ObjectIdentity=ObjectIdentity
pmora14AlmOtherNurg=_Pmora14AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,1))
_Pmora14AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmora14AlmsynthAlm2=_Pmora14AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,1,2))
_Pmora14AlmConfTableSave_Type=EkiOnOff
_Pmora14AlmConfTableSave_Object=MibScalar
pmora14AlmConfTableSave=_Pmora14AlmConfTableSave_Object((1,3,6,1,4,1,20044,72,2,1,1,2,1),_Pmora14AlmConfTableSave_Type())
pmora14AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmConfTableSave.setStatus(_A)
_Pmora14AlmInvUpload_Type=EkiOnOff
_Pmora14AlmInvUpload_Object=MibScalar
pmora14AlmInvUpload=_Pmora14AlmInvUpload_Object((1,3,6,1,4,1,20044,72,2,1,1,2,2),_Pmora14AlmInvUpload_Type())
pmora14AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmInvUpload.setStatus(_A)
_Pmora14AlmConfTableLoad_Type=EkiOnOff
_Pmora14AlmConfTableLoad_Object=MibScalar
pmora14AlmConfTableLoad=_Pmora14AlmConfTableLoad_Object((1,3,6,1,4,1,20044,72,2,1,1,2,3),_Pmora14AlmConfTableLoad_Type())
pmora14AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmConfTableLoad.setStatus(_A)
_Pmora14AlmmoduleWarnings_ObjectIdentity=ObjectIdentity
pmora14AlmmoduleWarnings=_Pmora14AlmmoduleWarnings_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,1,75))
_Pmora14AlmModuleTempLowWarning_Type=EkiOnOff
_Pmora14AlmModuleTempLowWarning_Object=MibScalar
pmora14AlmModuleTempLowWarning=_Pmora14AlmModuleTempLowWarning_Object((1,3,6,1,4,1,20044,72,2,1,1,75,1),_Pmora14AlmModuleTempLowWarning_Type())
pmora14AlmModuleTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmModuleTempLowWarning.setStatus(_A)
_Pmora14AlmModuleTempHighWarning_Type=EkiOnOff
_Pmora14AlmModuleTempHighWarning_Object=MibScalar
pmora14AlmModuleTempHighWarning=_Pmora14AlmModuleTempHighWarning_Object((1,3,6,1,4,1,20044,72,2,1,1,75,2),_Pmora14AlmModuleTempHighWarning_Type())
pmora14AlmModuleTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmModuleTempHighWarning.setStatus(_A)
_Pmora14AlmOtherUrg_ObjectIdentity=ObjectIdentity
pmora14AlmOtherUrg=_Pmora14AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,2))
_Pmora14AlmmoduleAlarms_ObjectIdentity=ObjectIdentity
pmora14AlmmoduleAlarms=_Pmora14AlmmoduleAlarms_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,2,74))
_Pmora14AlmModuleTempLowAlarm_Type=EkiOnOff
_Pmora14AlmModuleTempLowAlarm_Object=MibScalar
pmora14AlmModuleTempLowAlarm=_Pmora14AlmModuleTempLowAlarm_Object((1,3,6,1,4,1,20044,72,2,1,2,74,1),_Pmora14AlmModuleTempLowAlarm_Type())
pmora14AlmModuleTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmModuleTempLowAlarm.setStatus(_A)
_Pmora14AlmModuleTempHighAlarm_Type=EkiOnOff
_Pmora14AlmModuleTempHighAlarm_Object=MibScalar
pmora14AlmModuleTempHighAlarm=_Pmora14AlmModuleTempHighAlarm_Object((1,3,6,1,4,1,20044,72,2,1,2,74,2),_Pmora14AlmModuleTempHighAlarm_Type())
pmora14AlmModuleTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmModuleTempHighAlarm.setStatus(_A)
_Pmora14AlmOtherCrit_ObjectIdentity=ObjectIdentity
pmora14AlmOtherCrit=_Pmora14AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,3))
_Pmora14AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmora14AlmsynthAlm0=_Pmora14AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,72,2,1,3,0))
_Pmora14AlmMaintenanceMode_Type=EkiOnOff
_Pmora14AlmMaintenanceMode_Object=MibScalar
pmora14AlmMaintenanceMode=_Pmora14AlmMaintenanceMode_Object((1,3,6,1,4,1,20044,72,2,1,3,0,1),_Pmora14AlmMaintenanceMode_Type())
pmora14AlmMaintenanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmMaintenanceMode.setStatus(_A)
_Pmora14AlmAprOn_Type=EkiOnOff
_Pmora14AlmAprOn_Object=MibScalar
pmora14AlmAprOn=_Pmora14AlmAprOn_Object((1,3,6,1,4,1,20044,72,2,1,3,0,2),_Pmora14AlmAprOn_Type())
pmora14AlmAprOn.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmAprOn.setStatus(_A)
_Pmora14AlmModGlobFail_Type=EkiOnOff
_Pmora14AlmModGlobFail_Object=MibScalar
pmora14AlmModGlobFail=_Pmora14AlmModGlobFail_Object((1,3,6,1,4,1,20044,72,2,1,3,0,9),_Pmora14AlmModGlobFail_Type())
pmora14AlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmModGlobFail.setStatus(_A)
_Pmora14AlmInitNotCompl_Type=EkiOnOff
_Pmora14AlmInitNotCompl_Object=MibScalar
pmora14AlmInitNotCompl=_Pmora14AlmInitNotCompl_Object((1,3,6,1,4,1,20044,72,2,1,3,0,10),_Pmora14AlmInitNotCompl_Type())
pmora14AlmInitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmInitNotCompl.setStatus(_A)
_Pmora14AlmDefFuseA_Type=EkiOnOff
_Pmora14AlmDefFuseA_Object=MibScalar
pmora14AlmDefFuseA=_Pmora14AlmDefFuseA_Object((1,3,6,1,4,1,20044,72,2,1,3,0,15),_Pmora14AlmDefFuseA_Type())
pmora14AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmDefFuseA.setStatus(_A)
_Pmora14AlmDefFuseB_Type=EkiOnOff
_Pmora14AlmDefFuseB_Object=MibScalar
pmora14AlmDefFuseB=_Pmora14AlmDefFuseB_Object((1,3,6,1,4,1,20044,72,2,1,3,0,16),_Pmora14AlmDefFuseB_Type())
pmora14AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmDefFuseB.setStatus(_A)
_Pmora14AlmClient_ObjectIdentity=ObjectIdentity
pmora14AlmClient=_Pmora14AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,72,2,2))
_Pmora14AlmClientNurg_ObjectIdentity=ObjectIdentity
pmora14AlmClientNurg=_Pmora14AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,72,2,2,1))
_Pmora14AlmClientUrg_ObjectIdentity=ObjectIdentity
pmora14AlmClientUrg=_Pmora14AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,72,2,2,2))
_Pmora14AlmClientCrit_ObjectIdentity=ObjectIdentity
pmora14AlmClientCrit=_Pmora14AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,72,2,2,3))
_Pmora14AlmLine_ObjectIdentity=ObjectIdentity
pmora14AlmLine=_Pmora14AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3))
_Pmora14AlmLineNurg_ObjectIdentity=ObjectIdentity
pmora14AlmLineNurg=_Pmora14AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,1))
_Pmora14AlmclientOraaWarnings_ObjectIdentity=ObjectIdentity
pmora14AlmclientOraaWarnings=_Pmora14AlmclientOraaWarnings_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,1,33))
_Pmora14AlmPump1CurrentHighWarning_Type=EkiOnOff
_Pmora14AlmPump1CurrentHighWarning_Object=MibScalar
pmora14AlmPump1CurrentHighWarning=_Pmora14AlmPump1CurrentHighWarning_Object((1,3,6,1,4,1,20044,72,2,3,1,33,1),_Pmora14AlmPump1CurrentHighWarning_Type())
pmora14AlmPump1CurrentHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump1CurrentHighWarning.setStatus(_A)
_Pmora14AlmPump2CurrentHighWarning_Type=EkiOnOff
_Pmora14AlmPump2CurrentHighWarning_Object=MibScalar
pmora14AlmPump2CurrentHighWarning=_Pmora14AlmPump2CurrentHighWarning_Object((1,3,6,1,4,1,20044,72,2,3,1,33,2),_Pmora14AlmPump2CurrentHighWarning_Type())
pmora14AlmPump2CurrentHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump2CurrentHighWarning.setStatus(_A)
_Pmora14AlmPump1TecWarning_Type=EkiOnOff
_Pmora14AlmPump1TecWarning_Object=MibScalar
pmora14AlmPump1TecWarning=_Pmora14AlmPump1TecWarning_Object((1,3,6,1,4,1,20044,72,2,3,1,33,3),_Pmora14AlmPump1TecWarning_Type())
pmora14AlmPump1TecWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump1TecWarning.setStatus(_A)
_Pmora14AlmPump2TecWarning_Type=EkiOnOff
_Pmora14AlmPump2TecWarning_Object=MibScalar
pmora14AlmPump2TecWarning=_Pmora14AlmPump2TecWarning_Object((1,3,6,1,4,1,20044,72,2,3,1,33,4),_Pmora14AlmPump2TecWarning_Type())
pmora14AlmPump2TecWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump2TecWarning.setStatus(_A)
_Pmora14AlmLineUrg_ObjectIdentity=ObjectIdentity
pmora14AlmLineUrg=_Pmora14AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,2))
_Pmora14AlmsynthAlm7_ObjectIdentity=ObjectIdentity
pmora14AlmsynthAlm7=_Pmora14AlmsynthAlm7_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,2,7))
_Pmora14AlmLineHwFail_Type=EkiOnOff
_Pmora14AlmLineHwFail_Object=MibScalar
pmora14AlmLineHwFail=_Pmora14AlmLineHwFail_Object((1,3,6,1,4,1,20044,72,2,3,2,7,4),_Pmora14AlmLineHwFail_Type())
pmora14AlmLineHwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmLineHwFail.setStatus(_A)
_Pmora14AlmPumpsTxOff_Type=EkiOnOff
_Pmora14AlmPumpsTxOff_Object=MibScalar
pmora14AlmPumpsTxOff=_Pmora14AlmPumpsTxOff_Object((1,3,6,1,4,1,20044,72,2,3,2,7,5),_Pmora14AlmPumpsTxOff_Type())
pmora14AlmPumpsTxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPumpsTxOff.setStatus(_A)
_Pmora14AlmLineFail_Type=EkiOnOff
_Pmora14AlmLineFail_Object=MibScalar
pmora14AlmLineFail=_Pmora14AlmLineFail_Object((1,3,6,1,4,1,20044,72,2,3,2,7,12),_Pmora14AlmLineFail_Type())
pmora14AlmLineFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmLineFail.setStatus(_A)
_Pmora14AlmclientOraAlarms1_ObjectIdentity=ObjectIdentity
pmora14AlmclientOraAlarms1=_Pmora14AlmclientOraAlarms1_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,2,32))
_Pmora14AlmPump1CurrentHighAlarm_Type=EkiOnOff
_Pmora14AlmPump1CurrentHighAlarm_Object=MibScalar
pmora14AlmPump1CurrentHighAlarm=_Pmora14AlmPump1CurrentHighAlarm_Object((1,3,6,1,4,1,20044,72,2,3,2,32,1),_Pmora14AlmPump1CurrentHighAlarm_Type())
pmora14AlmPump1CurrentHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump1CurrentHighAlarm.setStatus(_A)
_Pmora14AlmPump2CurrentHighAlarm_Type=EkiOnOff
_Pmora14AlmPump2CurrentHighAlarm_Object=MibScalar
pmora14AlmPump2CurrentHighAlarm=_Pmora14AlmPump2CurrentHighAlarm_Object((1,3,6,1,4,1,20044,72,2,3,2,32,2),_Pmora14AlmPump2CurrentHighAlarm_Type())
pmora14AlmPump2CurrentHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump2CurrentHighAlarm.setStatus(_A)
_Pmora14AlmPump1TecAlarm_Type=EkiOnOff
_Pmora14AlmPump1TecAlarm_Object=MibScalar
pmora14AlmPump1TecAlarm=_Pmora14AlmPump1TecAlarm_Object((1,3,6,1,4,1,20044,72,2,3,2,32,3),_Pmora14AlmPump1TecAlarm_Type())
pmora14AlmPump1TecAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump1TecAlarm.setStatus(_A)
_Pmora14AlmPump2TecAlarm_Type=EkiOnOff
_Pmora14AlmPump2TecAlarm_Object=MibScalar
pmora14AlmPump2TecAlarm=_Pmora14AlmPump2TecAlarm_Object((1,3,6,1,4,1,20044,72,2,3,2,32,4),_Pmora14AlmPump2TecAlarm_Type())
pmora14AlmPump2TecAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump2TecAlarm.setStatus(_A)
_Pmora14AlmfiberAlarms_ObjectIdentity=ObjectIdentity
pmora14AlmfiberAlarms=_Pmora14AlmfiberAlarms_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,2,72))
_Pmora14AlmSBandLossOfSignal_Type=EkiOnOff
_Pmora14AlmSBandLossOfSignal_Object=MibScalar
pmora14AlmSBandLossOfSignal=_Pmora14AlmSBandLossOfSignal_Object((1,3,6,1,4,1,20044,72,2,3,2,72,1),_Pmora14AlmSBandLossOfSignal_Type())
pmora14AlmSBandLossOfSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmSBandLossOfSignal.setStatus(_A)
_Pmora14AlmLowSBand_Type=EkiOnOff
_Pmora14AlmLowSBand_Object=MibScalar
pmora14AlmLowSBand=_Pmora14AlmLowSBand_Object((1,3,6,1,4,1,20044,72,2,3,2,72,2),_Pmora14AlmLowSBand_Type())
pmora14AlmLowSBand.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmLowSBand.setStatus(_A)
_Pmora14AlmCBandLossOfSignal_Type=EkiOnOff
_Pmora14AlmCBandLossOfSignal_Object=MibScalar
pmora14AlmCBandLossOfSignal=_Pmora14AlmCBandLossOfSignal_Object((1,3,6,1,4,1,20044,72,2,3,2,72,3),_Pmora14AlmCBandLossOfSignal_Type())
pmora14AlmCBandLossOfSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmCBandLossOfSignal.setStatus(_A)
_Pmora14AlmHighBackReflection_Type=EkiOnOff
_Pmora14AlmHighBackReflection_Object=MibScalar
pmora14AlmHighBackReflection=_Pmora14AlmHighBackReflection_Object((1,3,6,1,4,1,20044,72,2,3,2,72,4),_Pmora14AlmHighBackReflection_Type())
pmora14AlmHighBackReflection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmHighBackReflection.setStatus(_A)
_Pmora14AlmLineConnectorUnlocked_Type=EkiOnOff
_Pmora14AlmLineConnectorUnlocked_Object=MibScalar
pmora14AlmLineConnectorUnlocked=_Pmora14AlmLineConnectorUnlocked_Object((1,3,6,1,4,1,20044,72,2,3,2,72,5),_Pmora14AlmLineConnectorUnlocked_Type())
pmora14AlmLineConnectorUnlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmLineConnectorUnlocked.setStatus(_A)
_Pmora14AlmOscFailed_Type=EkiOnOff
_Pmora14AlmOscFailed_Object=MibScalar
pmora14AlmOscFailed=_Pmora14AlmOscFailed_Object((1,3,6,1,4,1,20044,72,2,3,2,72,6),_Pmora14AlmOscFailed_Type())
pmora14AlmOscFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmOscFailed.setStatus(_A)
_Pmora14AlmPartialAprSecurity_Type=EkiOnOff
_Pmora14AlmPartialAprSecurity_Object=MibScalar
pmora14AlmPartialAprSecurity=_Pmora14AlmPartialAprSecurity_Object((1,3,6,1,4,1,20044,72,2,3,2,72,7),_Pmora14AlmPartialAprSecurity_Type())
pmora14AlmPartialAprSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPartialAprSecurity.setStatus(_A)
_Pmora14AlmStartupLowSBand_Type=EkiOnOff
_Pmora14AlmStartupLowSBand_Object=MibScalar
pmora14AlmStartupLowSBand=_Pmora14AlmStartupLowSBand_Object((1,3,6,1,4,1,20044,72,2,3,2,72,8),_Pmora14AlmStartupLowSBand_Type())
pmora14AlmStartupLowSBand.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmStartupLowSBand.setStatus(_A)
_Pmora14AlmStartupHighBackReflection_Type=EkiOnOff
_Pmora14AlmStartupHighBackReflection_Object=MibScalar
pmora14AlmStartupHighBackReflection=_Pmora14AlmStartupHighBackReflection_Object((1,3,6,1,4,1,20044,72,2,3,2,72,9),_Pmora14AlmStartupHighBackReflection_Type())
pmora14AlmStartupHighBackReflection.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmStartupHighBackReflection.setStatus(_A)
_Pmora14AlmLineCrit_ObjectIdentity=ObjectIdentity
pmora14AlmLineCrit=_Pmora14AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,3))
_Pmora14Almpump1Alarms_ObjectIdentity=ObjectIdentity
pmora14Almpump1Alarms=_Pmora14Almpump1Alarms_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,3,35))
_Pmora14AlmPump1Shutdown_Type=EkiOnOff
_Pmora14AlmPump1Shutdown_Object=MibScalar
pmora14AlmPump1Shutdown=_Pmora14AlmPump1Shutdown_Object((1,3,6,1,4,1,20044,72,2,3,3,35,1),_Pmora14AlmPump1Shutdown_Type())
pmora14AlmPump1Shutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump1Shutdown.setStatus(_A)
_Pmora14AlmPump1TecFail_Type=EkiOnOff
_Pmora14AlmPump1TecFail_Object=MibScalar
pmora14AlmPump1TecFail=_Pmora14AlmPump1TecFail_Object((1,3,6,1,4,1,20044,72,2,3,3,35,2),_Pmora14AlmPump1TecFail_Type())
pmora14AlmPump1TecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump1TecFail.setStatus(_A)
_Pmora14Almpump2Alarms_ObjectIdentity=ObjectIdentity
pmora14Almpump2Alarms=_Pmora14Almpump2Alarms_ObjectIdentity((1,3,6,1,4,1,20044,72,2,3,3,36))
_Pmora14AlmPump2Shutdown_Type=EkiOnOff
_Pmora14AlmPump2Shutdown_Object=MibScalar
pmora14AlmPump2Shutdown=_Pmora14AlmPump2Shutdown_Object((1,3,6,1,4,1,20044,72,2,3,3,36,1),_Pmora14AlmPump2Shutdown_Type())
pmora14AlmPump2Shutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump2Shutdown.setStatus(_A)
_Pmora14AlmPump2TecFail_Type=EkiOnOff
_Pmora14AlmPump2TecFail_Object=MibScalar
pmora14AlmPump2TecFail=_Pmora14AlmPump2TecFail_Object((1,3,6,1,4,1,20044,72,2,3,3,36,2),_Pmora14AlmPump2TecFail_Type())
pmora14AlmPump2TecFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14AlmPump2TecFail.setStatus(_A)
_Pmora14measures_ObjectIdentity=ObjectIdentity
pmora14measures=_Pmora14measures_ObjectIdentity((1,3,6,1,4,1,20044,72,3))
_Pmora14MesrOther_ObjectIdentity=ObjectIdentity
pmora14MesrOther=_Pmora14MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,72,3,1))
class _Pmora14MesrpmTempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14MesrpmTempMeas_Type.__name__=_D
_Pmora14MesrpmTempMeas_Object=MibScalar
pmora14MesrpmTempMeas=_Pmora14MesrpmTempMeas_Object((1,3,6,1,4,1,20044,72,3,1,80),_Pmora14MesrpmTempMeas_Type())
pmora14MesrpmTempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14MesrpmTempMeas.setStatus(_A)
_Pmora14MesrClient_ObjectIdentity=ObjectIdentity
pmora14MesrClient=_Pmora14MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,72,3,2))
_Pmora14MesrLine_ObjectIdentity=ObjectIdentity
pmora14MesrLine=_Pmora14MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,72,3,3))
class _Pmora14Mesrpump1CurrentMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump1CurrentMeas_Type.__name__=_D
_Pmora14Mesrpump1CurrentMeas_Object=MibScalar
pmora14Mesrpump1CurrentMeas=_Pmora14Mesrpump1CurrentMeas_Object((1,3,6,1,4,1,20044,72,3,3,64),_Pmora14Mesrpump1CurrentMeas_Type())
pmora14Mesrpump1CurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump1CurrentMeas.setStatus(_A)
class _Pmora14Mesrpump1PowerMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump1PowerMeas_Type.__name__=_D
_Pmora14Mesrpump1PowerMeas_Object=MibScalar
pmora14Mesrpump1PowerMeas=_Pmora14Mesrpump1PowerMeas_Object((1,3,6,1,4,1,20044,72,3,3,65),_Pmora14Mesrpump1PowerMeas_Type())
pmora14Mesrpump1PowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump1PowerMeas.setStatus(_A)
class _Pmora14Mesrpump1TempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump1TempMeas_Type.__name__=_D
_Pmora14Mesrpump1TempMeas_Object=MibScalar
pmora14Mesrpump1TempMeas=_Pmora14Mesrpump1TempMeas_Object((1,3,6,1,4,1,20044,72,3,3,66),_Pmora14Mesrpump1TempMeas_Type())
pmora14Mesrpump1TempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump1TempMeas.setStatus(_A)
class _Pmora14Mesrpump1TecCurrentMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump1TecCurrentMeas_Type.__name__=_D
_Pmora14Mesrpump1TecCurrentMeas_Object=MibScalar
pmora14Mesrpump1TecCurrentMeas=_Pmora14Mesrpump1TecCurrentMeas_Object((1,3,6,1,4,1,20044,72,3,3,67),_Pmora14Mesrpump1TecCurrentMeas_Type())
pmora14Mesrpump1TecCurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump1TecCurrentMeas.setStatus(_A)
class _Pmora14Mesrpump2CurrentMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump2CurrentMeas_Type.__name__=_D
_Pmora14Mesrpump2CurrentMeas_Object=MibScalar
pmora14Mesrpump2CurrentMeas=_Pmora14Mesrpump2CurrentMeas_Object((1,3,6,1,4,1,20044,72,3,3,68),_Pmora14Mesrpump2CurrentMeas_Type())
pmora14Mesrpump2CurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump2CurrentMeas.setStatus(_A)
class _Pmora14Mesrpump2PowerMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump2PowerMeas_Type.__name__=_D
_Pmora14Mesrpump2PowerMeas_Object=MibScalar
pmora14Mesrpump2PowerMeas=_Pmora14Mesrpump2PowerMeas_Object((1,3,6,1,4,1,20044,72,3,3,69),_Pmora14Mesrpump2PowerMeas_Type())
pmora14Mesrpump2PowerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump2PowerMeas.setStatus(_A)
class _Pmora14Mesrpump2TempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump2TempMeas_Type.__name__=_D
_Pmora14Mesrpump2TempMeas_Object=MibScalar
pmora14Mesrpump2TempMeas=_Pmora14Mesrpump2TempMeas_Object((1,3,6,1,4,1,20044,72,3,3,70),_Pmora14Mesrpump2TempMeas_Type())
pmora14Mesrpump2TempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump2TempMeas.setStatus(_A)
class _Pmora14Mesrpump2TecCurrentMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14Mesrpump2TecCurrentMeas_Type.__name__=_D
_Pmora14Mesrpump2TecCurrentMeas_Object=MibScalar
pmora14Mesrpump2TecCurrentMeas=_Pmora14Mesrpump2TecCurrentMeas_Object((1,3,6,1,4,1,20044,72,3,3,71),_Pmora14Mesrpump2TecCurrentMeas_Type())
pmora14Mesrpump2TecCurrentMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14Mesrpump2TecCurrentMeas.setStatus(_A)
class _Pmora14MesrtotalPumpsPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14MesrtotalPumpsPower_Type.__name__=_D
_Pmora14MesrtotalPumpsPower_Object=MibScalar
pmora14MesrtotalPumpsPower=_Pmora14MesrtotalPumpsPower_Object((1,3,6,1,4,1,20044,72,3,3,72),_Pmora14MesrtotalPumpsPower_Type())
pmora14MesrtotalPumpsPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14MesrtotalPumpsPower.setStatus(_A)
class _Pmora14MesrinputCBandPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14MesrinputCBandPower_Type.__name__=_D
_Pmora14MesrinputCBandPower_Object=MibScalar
pmora14MesrinputCBandPower=_Pmora14MesrinputCBandPower_Object((1,3,6,1,4,1,20044,72,3,3,73),_Pmora14MesrinputCBandPower_Type())
pmora14MesrinputCBandPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14MesrinputCBandPower.setStatus(_A)
class _Pmora14MesrsBandPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14MesrsBandPower_Type.__name__=_D
_Pmora14MesrsBandPower_Object=MibScalar
pmora14MesrsBandPower=_Pmora14MesrsBandPower_Object((1,3,6,1,4,1,20044,72,3,3,74),_Pmora14MesrsBandPower_Type())
pmora14MesrsBandPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14MesrsBandPower.setStatus(_A)
class _Pmora14MesrbackReflectionPumpPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14MesrbackReflectionPumpPower_Type.__name__=_D
_Pmora14MesrbackReflectionPumpPower_Object=MibScalar
pmora14MesrbackReflectionPumpPower=_Pmora14MesrbackReflectionPumpPower_Object((1,3,6,1,4,1,20044,72,3,3,75),_Pmora14MesrbackReflectionPumpPower_Type())
pmora14MesrbackReflectionPumpPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14MesrbackReflectionPumpPower.setStatus(_A)
class _Pmora14MesrbackReflectionPumpRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmora14MesrbackReflectionPumpRatio_Type.__name__=_D
_Pmora14MesrbackReflectionPumpRatio_Object=MibScalar
pmora14MesrbackReflectionPumpRatio=_Pmora14MesrbackReflectionPumpRatio_Object((1,3,6,1,4,1,20044,72,3,3,76),_Pmora14MesrbackReflectionPumpRatio_Type())
pmora14MesrbackReflectionPumpRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14MesrbackReflectionPumpRatio.setStatus(_A)
_Pmora14counters_ObjectIdentity=ObjectIdentity
pmora14counters=_Pmora14counters_ObjectIdentity((1,3,6,1,4,1,20044,72,4))
_Pmora14CntOther_ObjectIdentity=ObjectIdentity
pmora14CntOther=_Pmora14CntOther_ObjectIdentity((1,3,6,1,4,1,20044,72,4,1))
_Pmora14CntClient_ObjectIdentity=ObjectIdentity
pmora14CntClient=_Pmora14CntClient_ObjectIdentity((1,3,6,1,4,1,20044,72,4,2))
_Pmora14CntLine_ObjectIdentity=ObjectIdentity
pmora14CntLine=_Pmora14CntLine_ObjectIdentity((1,3,6,1,4,1,20044,72,4,3))
_Pmora14CntCountersReset_Type=EkiOnOff
_Pmora14CntCountersReset_Object=MibScalar
pmora14CntCountersReset=_Pmora14CntCountersReset_Object((1,3,6,1,4,1,20044,72,4,259),_Pmora14CntCountersReset_Type())
pmora14CntCountersReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CntCountersReset.setStatus(_A)
_Pmora14CntCountersStop_Type=EkiOnOff
_Pmora14CntCountersStop_Object=MibScalar
pmora14CntCountersStop=_Pmora14CntCountersStop_Object((1,3,6,1,4,1,20044,72,4,260),_Pmora14CntCountersStop_Type())
pmora14CntCountersStop.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CntCountersStop.setStatus(_A)
_Pmora14controlsWrite_ObjectIdentity=ObjectIdentity
pmora14controlsWrite=_Pmora14controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,72,6))
_Pmora14CtrlOther_ObjectIdentity=ObjectIdentity
pmora14CtrlOther=_Pmora14CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,72,6,1))
_Pmora14Ctrlsynth0_ObjectIdentity=ObjectIdentity
pmora14Ctrlsynth0=_Pmora14Ctrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,72,6,1,0))
_Pmora14CtrlConfLoad_Type=EkiOnOff
_Pmora14CtrlConfLoad_Object=MibScalar
pmora14CtrlConfLoad=_Pmora14CtrlConfLoad_Object((1,3,6,1,4,1,20044,72,6,1,0,1),_Pmora14CtrlConfLoad_Type())
pmora14CtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlConfLoad.setStatus(_A)
_Pmora14CtrlConfFlash_Type=EkiOnOff
_Pmora14CtrlConfFlash_Object=MibScalar
pmora14CtrlConfFlash=_Pmora14CtrlConfFlash_Object((1,3,6,1,4,1,20044,72,6,1,0,9),_Pmora14CtrlConfFlash_Type())
pmora14CtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlConfFlash.setStatus(_A)
_Pmora14CtrlConfClear_Type=EkiOnOff
_Pmora14CtrlConfClear_Object=MibScalar
pmora14CtrlConfClear=_Pmora14CtrlConfClear_Object((1,3,6,1,4,1,20044,72,6,1,0,13),_Pmora14CtrlConfClear_Type())
pmora14CtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlConfClear.setStatus(_A)
_Pmora14CtrlswMgnt_ObjectIdentity=ObjectIdentity
pmora14CtrlswMgnt=_Pmora14CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,72,6,1,5))
_Pmora14CtrlColdReset_Type=EkiOnOff
_Pmora14CtrlColdReset_Object=MibScalar
pmora14CtrlColdReset=_Pmora14CtrlColdReset_Object((1,3,6,1,4,1,20044,72,6,1,5,2),_Pmora14CtrlColdReset_Type())
pmora14CtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlColdReset.setStatus(_A)
_Pmora14CtrlWarmReset_Type=EkiOnOff
_Pmora14CtrlWarmReset_Object=MibScalar
pmora14CtrlWarmReset=_Pmora14CtrlWarmReset_Object((1,3,6,1,4,1,20044,72,6,1,5,3),_Pmora14CtrlWarmReset_Type())
pmora14CtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlWarmReset.setStatus(_A)
_Pmora14CtrlaprMode_Type=Pmora14AprMode
_Pmora14CtrlaprMode_Object=MibScalar
pmora14CtrlaprMode=_Pmora14CtrlaprMode_Object((1,3,6,1,4,1,20044,72,6,1,16),_Pmora14CtrlaprMode_Type())
pmora14CtrlaprMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlaprMode.setStatus(_A)
_Pmora14CtrlledTest_ObjectIdentity=ObjectIdentity
pmora14CtrlledTest=_Pmora14CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,72,6,1,73))
_Pmora14CtrlGreenLed_Type=EkiOnOff
_Pmora14CtrlGreenLed_Object=MibScalar
pmora14CtrlGreenLed=_Pmora14CtrlGreenLed_Object((1,3,6,1,4,1,20044,72,6,1,73,1),_Pmora14CtrlGreenLed_Type())
pmora14CtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlGreenLed.setStatus(_A)
_Pmora14CtrlRedLed_Type=EkiOnOff
_Pmora14CtrlRedLed_Object=MibScalar
pmora14CtrlRedLed=_Pmora14CtrlRedLed_Object((1,3,6,1,4,1,20044,72,6,1,73,2),_Pmora14CtrlRedLed_Type())
pmora14CtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlRedLed.setStatus(_A)
_Pmora14CtrlLedOff_Type=EkiOnOff
_Pmora14CtrlLedOff_Object=MibScalar
pmora14CtrlLedOff=_Pmora14CtrlLedOff_Object((1,3,6,1,4,1,20044,72,6,1,73,3),_Pmora14CtrlLedOff_Type())
pmora14CtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlLedOff.setStatus(_A)
_Pmora14CtrlmaintMode_ObjectIdentity=ObjectIdentity
pmora14CtrlmaintMode=_Pmora14CtrlmaintMode_ObjectIdentity((1,3,6,1,4,1,20044,72,6,1,74))
_Pmora14CtrlMaintenance_Type=EkiOnOff
_Pmora14CtrlMaintenance_Object=MibScalar
pmora14CtrlMaintenance=_Pmora14CtrlMaintenance_Object((1,3,6,1,4,1,20044,72,6,1,74,1),_Pmora14CtrlMaintenance_Type())
pmora14CtrlMaintenance.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlMaintenance.setStatus(_A)
_Pmora14CtrlClient_ObjectIdentity=ObjectIdentity
pmora14CtrlClient=_Pmora14CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,72,6,2))
_Pmora14CtrlLine_ObjectIdentity=ObjectIdentity
pmora14CtrlLine=_Pmora14CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,72,6,3))
_Pmora14CtrlaprManualRestart_ObjectIdentity=ObjectIdentity
pmora14CtrlaprManualRestart=_Pmora14CtrlaprManualRestart_ObjectIdentity((1,3,6,1,4,1,20044,72,6,3,75))
_Pmora14CtrlAprManualRestart_Type=EkiOnOff
_Pmora14CtrlAprManualRestart_Object=MibScalar
pmora14CtrlAprManualRestart=_Pmora14CtrlAprManualRestart_Object((1,3,6,1,4,1,20044,72,6,3,75,1),_Pmora14CtrlAprManualRestart_Type())
pmora14CtrlAprManualRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CtrlAprManualRestart.setStatus(_A)
_Pmora14ri_ObjectIdentity=ObjectIdentity
pmora14ri=_Pmora14ri_ObjectIdentity((1,3,6,1,4,1,20044,72,7))
_Pmora14riTable_ObjectIdentity=ObjectIdentity
pmora14riTable=_Pmora14riTable_ObjectIdentity((1,3,6,1,4,1,20044,72,7,1))
_Pmora14RinvLineTable_Object=MibTable
pmora14RinvLineTable=_Pmora14RinvLineTable_Object((1,3,6,1,4,1,20044,72,7,1,2))
if mibBuilder.loadTexts:pmora14RinvLineTable.setStatus(_A)
_Pmora14RinvLineEntry_Object=MibTableRow
pmora14RinvLineEntry=_Pmora14RinvLineEntry_Object((1,3,6,1,4,1,20044,72,7,1,2,1))
pmora14RinvLineEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:pmora14RinvLineEntry.setStatus(_A)
class _Pmora14RinvLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pmora14RinvLineIndex_Type.__name__=_D
_Pmora14RinvLineIndex_Object=MibTableColumn
pmora14RinvLineIndex=_Pmora14RinvLineIndex_Object((1,3,6,1,4,1,20044,72,7,1,2,1,1),_Pmora14RinvLineIndex_Type())
pmora14RinvLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14RinvLineIndex.setStatus(_A)
_Pmora14RinvportLine_Type=DisplayString
_Pmora14RinvportLine_Object=MibTableColumn
pmora14RinvportLine=_Pmora14RinvportLine_Object((1,3,6,1,4,1,20044,72,7,1,2,1,2),_Pmora14RinvportLine_Type())
pmora14RinvportLine.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14RinvportLine.setStatus(_A)
_Pmora14RinvReloadInventory_Type=EkiOnOff
_Pmora14RinvReloadInventory_Object=MibScalar
pmora14RinvReloadInventory=_Pmora14RinvReloadInventory_Object((1,3,6,1,4,1,20044,72,7,2),_Pmora14RinvReloadInventory_Type())
pmora14RinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14RinvReloadInventory.setStatus(_A)
_Pmora14RinvHwPlatform_Type=DisplayString
_Pmora14RinvHwPlatform_Object=MibScalar
pmora14RinvHwPlatform=_Pmora14RinvHwPlatform_Object((1,3,6,1,4,1,20044,72,7,3),_Pmora14RinvHwPlatform_Type())
pmora14RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14RinvHwPlatform.setStatus(_A)
_Pmora14RinvModulePlatform_Type=DisplayString
_Pmora14RinvModulePlatform_Object=MibScalar
pmora14RinvModulePlatform=_Pmora14RinvModulePlatform_Object((1,3,6,1,4,1,20044,72,7,4),_Pmora14RinvModulePlatform_Type())
pmora14RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14RinvModulePlatform.setStatus(_A)
_Pmora14RinvSwPlatform_Type=DisplayString
_Pmora14RinvSwPlatform_Object=MibScalar
pmora14RinvSwPlatform=_Pmora14RinvSwPlatform_Object((1,3,6,1,4,1,20044,72,7,5),_Pmora14RinvSwPlatform_Type())
pmora14RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14RinvSwPlatform.setStatus(_A)
_Pmora14RinvGwPlatform_Type=DisplayString
_Pmora14RinvGwPlatform_Object=MibScalar
pmora14RinvGwPlatform=_Pmora14RinvGwPlatform_Object((1,3,6,1,4,1,20044,72,7,6),_Pmora14RinvGwPlatform_Type())
pmora14RinvGwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14RinvGwPlatform.setStatus(_A)
_Pmora14Config_ObjectIdentity=ObjectIdentity
pmora14Config=_Pmora14Config_ObjectIdentity((1,3,6,1,4,1,20044,72,9))
_Pmora14CfgNoValue_ObjectIdentity=ObjectIdentity
pmora14CfgNoValue=_Pmora14CfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,72,9,1))
_Pmora14tablelineStartup_ObjectIdentity=ObjectIdentity
pmora14tablelineStartup=_Pmora14tablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,72,9,1,1))
class _Pmora14CfgoraModuleCtrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfgoraModuleCtrl_Type.__name__=_F
_Pmora14CfgoraModuleCtrl_Object=MibScalar
pmora14CfgoraModuleCtrl=_Pmora14CfgoraModuleCtrl_Object((1,3,6,1,4,1,20044,72,9,1,1,2),_Pmora14CfgoraModuleCtrl_Type())
pmora14CfgoraModuleCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgoraModuleCtrl.setStatus(_A)
class _Pmora14CfgautoRestartDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfgautoRestartDelay_Type.__name__=_F
_Pmora14CfgautoRestartDelay_Object=MibScalar
pmora14CfgautoRestartDelay=_Pmora14CfgautoRestartDelay_Object((1,3,6,1,4,1,20044,72,9,1,1,3),_Pmora14CfgautoRestartDelay_Type())
pmora14CfgautoRestartDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgautoRestartDelay.setStatus(_A)
class _Pmora14CfgramanGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfgramanGain_Type.__name__=_F
_Pmora14CfgramanGain_Object=MibScalar
pmora14CfgramanGain=_Pmora14CfgramanGain_Object((1,3,6,1,4,1,20044,72,9,1,1,4),_Pmora14CfgramanGain_Type())
pmora14CfgramanGain.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgramanGain.setStatus(_A)
class _Pmora14CfgramanMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfgramanMode_Type.__name__=_F
_Pmora14CfgramanMode_Object=MibScalar
pmora14CfgramanMode=_Pmora14CfgramanMode_Object((1,3,6,1,4,1,20044,72,9,1,1,5),_Pmora14CfgramanMode_Type())
pmora14CfgramanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgramanMode.setStatus(_A)
class _Pmora14CfgtiltValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfgtiltValue_Type.__name__=_F
_Pmora14CfgtiltValue_Object=MibScalar
pmora14CfgtiltValue=_Pmora14CfgtiltValue_Object((1,3,6,1,4,1,20044,72,9,1,1,6),_Pmora14CfgtiltValue_Type())
pmora14CfgtiltValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgtiltValue.setStatus(_A)
class _Pmora14CfghighBackreflectionThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfghighBackreflectionThreshold_Type.__name__=_F
_Pmora14CfghighBackreflectionThreshold_Object=MibScalar
pmora14CfghighBackreflectionThreshold=_Pmora14CfghighBackreflectionThreshold_Object((1,3,6,1,4,1,20044,72,9,1,1,7),_Pmora14CfghighBackreflectionThreshold_Type())
pmora14CfghighBackreflectionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfghighBackreflectionThreshold.setStatus(_A)
class _Pmora14CfgsBandThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14CfgsBandThreshold_Type.__name__=_F
_Pmora14CfgsBandThreshold_Object=MibScalar
pmora14CfgsBandThreshold=_Pmora14CfgsBandThreshold_Object((1,3,6,1,4,1,20044,72,9,1,1,8),_Pmora14CfgsBandThreshold_Type())
pmora14CfgsBandThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgsBandThreshold.setStatus(_A)
class _Pmora14Cfgpump1ManualPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14Cfgpump1ManualPower_Type.__name__=_F
_Pmora14Cfgpump1ManualPower_Object=MibScalar
pmora14Cfgpump1ManualPower=_Pmora14Cfgpump1ManualPower_Object((1,3,6,1,4,1,20044,72,9,1,1,9),_Pmora14Cfgpump1ManualPower_Type())
pmora14Cfgpump1ManualPower.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14Cfgpump1ManualPower.setStatus(_A)
class _Pmora14Cfgpump2ManualPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmora14Cfgpump2ManualPower_Type.__name__=_F
_Pmora14Cfgpump2ManualPower_Object=MibScalar
pmora14Cfgpump2ManualPower=_Pmora14Cfgpump2ManualPower_Object((1,3,6,1,4,1,20044,72,9,1,1,10),_Pmora14Cfgpump2ManualPower_Type())
pmora14Cfgpump2ManualPower.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14Cfgpump2ManualPower.setStatus(_A)
_Pmora14CfgLabels_ObjectIdentity=ObjectIdentity
pmora14CfgLabels=_Pmora14CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,72,9,2))
_Pmora14CfgLabelclientTable_Object=MibTable
pmora14CfgLabelclientTable=_Pmora14CfgLabelclientTable_Object((1,3,6,1,4,1,20044,72,9,2,1))
if mibBuilder.loadTexts:pmora14CfgLabelclientTable.setStatus(_A)
_Pmora14CfgLabelclientEntry_Object=MibTableRow
pmora14CfgLabelclientEntry=_Pmora14CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,72,9,2,1,1))
pmora14CfgLabelclientEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:pmora14CfgLabelclientEntry.setStatus(_A)
class _Pmora14CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmora14CfgLabelclientIndex_Type.__name__=_D
_Pmora14CfgLabelclientIndex_Object=MibTableColumn
pmora14CfgLabelclientIndex=_Pmora14CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,72,9,2,1,1,1),_Pmora14CfgLabelclientIndex_Type())
pmora14CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14CfgLabelclientIndex.setStatus(_A)
class _Pmora14CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmora14CfgLabelclientPortn_Type.__name__=_H
_Pmora14CfgLabelclientPortn_Object=MibTableColumn
pmora14CfgLabelclientPortn=_Pmora14CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,72,9,2,1,1,3),_Pmora14CfgLabelclientPortn_Type())
pmora14CfgLabelclientPortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgLabelclientPortn.setStatus(_A)
_Pmora14CfgLabellineTable_Object=MibTable
pmora14CfgLabellineTable=_Pmora14CfgLabellineTable_Object((1,3,6,1,4,1,20044,72,9,2,2))
if mibBuilder.loadTexts:pmora14CfgLabellineTable.setStatus(_A)
_Pmora14CfgLabellineEntry_Object=MibTableRow
pmora14CfgLabellineEntry=_Pmora14CfgLabellineEntry_Object((1,3,6,1,4,1,20044,72,9,2,2,1))
pmora14CfgLabellineEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:pmora14CfgLabellineEntry.setStatus(_A)
class _Pmora14CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmora14CfgLabellineIndex_Type.__name__=_D
_Pmora14CfgLabellineIndex_Object=MibTableColumn
pmora14CfgLabellineIndex=_Pmora14CfgLabellineIndex_Object((1,3,6,1,4,1,20044,72,9,2,2,1,1),_Pmora14CfgLabellineIndex_Type())
pmora14CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14CfgLabellineIndex.setStatus(_A)
class _Pmora14CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmora14CfgLabellinePortn_Type.__name__=_H
_Pmora14CfgLabellinePortn_Object=MibTableColumn
pmora14CfgLabellinePortn=_Pmora14CfgLabellinePortn_Object((1,3,6,1,4,1,20044,72,9,2,2,1,3),_Pmora14CfgLabellinePortn_Type())
pmora14CfgLabellinePortn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgLabellinePortn.setStatus(_A)
_Pmora14CfgWriteConfiguration_Type=EkiOnOff
_Pmora14CfgWriteConfiguration_Object=MibScalar
pmora14CfgWriteConfiguration=_Pmora14CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,72,9,257),_Pmora14CfgWriteConfiguration_Type())
pmora14CfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmora14CfgWriteConfiguration.setStatus(_A)
_Pmora14traps_ObjectIdentity=ObjectIdentity
pmora14traps=_Pmora14traps_ObjectIdentity((1,3,6,1,4,1,20044,72,10))
class _Pmora14trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pmora14trapBoardNumber_Type.__name__=_D
_Pmora14trapBoardNumber_Object=MibScalar
pmora14trapBoardNumber=_Pmora14trapBoardNumber_Object((1,3,6,1,4,1,20044,72,10,4),_Pmora14trapBoardNumber_Type())
pmora14trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmora14trapBoardNumber.setStatus(_A)
pmora14LineTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,72,10,34))
pmora14LineTrapCritGoesOn.setObjects(*((_E,_I),(_E,_J),(_E,_G)))
if mibBuilder.loadTexts:pmora14LineTrapCritGoesOn.setStatus(_A)
pmora14LineTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,72,10,35))
pmora14LineTrapCritGoesOff.setObjects(*((_E,_I),(_E,_J),(_E,_G)))
if mibBuilder.loadTexts:pmora14LineTrapCritGoesOff.setStatus(_A)
pmora14PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,72,10,50))
pmora14PowerTrapUrgentGoesOn.setObjects(*((_E,_K),(_E,_L),(_E,_G)))
if mibBuilder.loadTexts:pmora14PowerTrapUrgentGoesOn.setStatus(_A)
pmora14PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,72,10,51))
pmora14PowerTrapUrgentGoesOff.setObjects(*((_E,_K),(_E,_L),(_E,_G)))
if mibBuilder.loadTexts:pmora14PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Pmora14PumpsMode':Pmora14PumpsMode,'Pmora14AprMode':Pmora14AprMode,'Pmora14LineFiberTypeMode':Pmora14LineFiberTypeMode,'modulepmora14':modulepmora14,'pmora14alarms':pmora14alarms,'pmora14AlmOther':pmora14AlmOther,'pmora14AlmOtherNurg':pmora14AlmOtherNurg,'pmora14AlmsynthAlm2':pmora14AlmsynthAlm2,'pmora14AlmConfTableSave':pmora14AlmConfTableSave,'pmora14AlmInvUpload':pmora14AlmInvUpload,'pmora14AlmConfTableLoad':pmora14AlmConfTableLoad,'pmora14AlmmoduleWarnings':pmora14AlmmoduleWarnings,'pmora14AlmModuleTempLowWarning':pmora14AlmModuleTempLowWarning,'pmora14AlmModuleTempHighWarning':pmora14AlmModuleTempHighWarning,'pmora14AlmOtherUrg':pmora14AlmOtherUrg,'pmora14AlmmoduleAlarms':pmora14AlmmoduleAlarms,'pmora14AlmModuleTempLowAlarm':pmora14AlmModuleTempLowAlarm,'pmora14AlmModuleTempHighAlarm':pmora14AlmModuleTempHighAlarm,'pmora14AlmOtherCrit':pmora14AlmOtherCrit,'pmora14AlmsynthAlm0':pmora14AlmsynthAlm0,'pmora14AlmMaintenanceMode':pmora14AlmMaintenanceMode,'pmora14AlmAprOn':pmora14AlmAprOn,'pmora14AlmModGlobFail':pmora14AlmModGlobFail,'pmora14AlmInitNotCompl':pmora14AlmInitNotCompl,_L:pmora14AlmDefFuseA,_K:pmora14AlmDefFuseB,'pmora14AlmClient':pmora14AlmClient,'pmora14AlmClientNurg':pmora14AlmClientNurg,'pmora14AlmClientUrg':pmora14AlmClientUrg,'pmora14AlmClientCrit':pmora14AlmClientCrit,'pmora14AlmLine':pmora14AlmLine,'pmora14AlmLineNurg':pmora14AlmLineNurg,'pmora14AlmclientOraaWarnings':pmora14AlmclientOraaWarnings,'pmora14AlmPump1CurrentHighWarning':pmora14AlmPump1CurrentHighWarning,'pmora14AlmPump2CurrentHighWarning':pmora14AlmPump2CurrentHighWarning,'pmora14AlmPump1TecWarning':pmora14AlmPump1TecWarning,'pmora14AlmPump2TecWarning':pmora14AlmPump2TecWarning,'pmora14AlmLineUrg':pmora14AlmLineUrg,'pmora14AlmsynthAlm7':pmora14AlmsynthAlm7,_J:pmora14AlmLineHwFail,'pmora14AlmPumpsTxOff':pmora14AlmPumpsTxOff,_I:pmora14AlmLineFail,'pmora14AlmclientOraAlarms1':pmora14AlmclientOraAlarms1,'pmora14AlmPump1CurrentHighAlarm':pmora14AlmPump1CurrentHighAlarm,'pmora14AlmPump2CurrentHighAlarm':pmora14AlmPump2CurrentHighAlarm,'pmora14AlmPump1TecAlarm':pmora14AlmPump1TecAlarm,'pmora14AlmPump2TecAlarm':pmora14AlmPump2TecAlarm,'pmora14AlmfiberAlarms':pmora14AlmfiberAlarms,'pmora14AlmSBandLossOfSignal':pmora14AlmSBandLossOfSignal,'pmora14AlmLowSBand':pmora14AlmLowSBand,'pmora14AlmCBandLossOfSignal':pmora14AlmCBandLossOfSignal,'pmora14AlmHighBackReflection':pmora14AlmHighBackReflection,'pmora14AlmLineConnectorUnlocked':pmora14AlmLineConnectorUnlocked,'pmora14AlmOscFailed':pmora14AlmOscFailed,'pmora14AlmPartialAprSecurity':pmora14AlmPartialAprSecurity,'pmora14AlmStartupLowSBand':pmora14AlmStartupLowSBand,'pmora14AlmStartupHighBackReflection':pmora14AlmStartupHighBackReflection,'pmora14AlmLineCrit':pmora14AlmLineCrit,'pmora14Almpump1Alarms':pmora14Almpump1Alarms,'pmora14AlmPump1Shutdown':pmora14AlmPump1Shutdown,'pmora14AlmPump1TecFail':pmora14AlmPump1TecFail,'pmora14Almpump2Alarms':pmora14Almpump2Alarms,'pmora14AlmPump2Shutdown':pmora14AlmPump2Shutdown,'pmora14AlmPump2TecFail':pmora14AlmPump2TecFail,'pmora14measures':pmora14measures,'pmora14MesrOther':pmora14MesrOther,'pmora14MesrpmTempMeas':pmora14MesrpmTempMeas,'pmora14MesrClient':pmora14MesrClient,'pmora14MesrLine':pmora14MesrLine,'pmora14Mesrpump1CurrentMeas':pmora14Mesrpump1CurrentMeas,'pmora14Mesrpump1PowerMeas':pmora14Mesrpump1PowerMeas,'pmora14Mesrpump1TempMeas':pmora14Mesrpump1TempMeas,'pmora14Mesrpump1TecCurrentMeas':pmora14Mesrpump1TecCurrentMeas,'pmora14Mesrpump2CurrentMeas':pmora14Mesrpump2CurrentMeas,'pmora14Mesrpump2PowerMeas':pmora14Mesrpump2PowerMeas,'pmora14Mesrpump2TempMeas':pmora14Mesrpump2TempMeas,'pmora14Mesrpump2TecCurrentMeas':pmora14Mesrpump2TecCurrentMeas,'pmora14MesrtotalPumpsPower':pmora14MesrtotalPumpsPower,'pmora14MesrinputCBandPower':pmora14MesrinputCBandPower,'pmora14MesrsBandPower':pmora14MesrsBandPower,'pmora14MesrbackReflectionPumpPower':pmora14MesrbackReflectionPumpPower,'pmora14MesrbackReflectionPumpRatio':pmora14MesrbackReflectionPumpRatio,'pmora14counters':pmora14counters,'pmora14CntOther':pmora14CntOther,'pmora14CntClient':pmora14CntClient,'pmora14CntLine':pmora14CntLine,'pmora14CntCountersReset':pmora14CntCountersReset,'pmora14CntCountersStop':pmora14CntCountersStop,'pmora14controlsWrite':pmora14controlsWrite,'pmora14CtrlOther':pmora14CtrlOther,'pmora14Ctrlsynth0':pmora14Ctrlsynth0,'pmora14CtrlConfLoad':pmora14CtrlConfLoad,'pmora14CtrlConfFlash':pmora14CtrlConfFlash,'pmora14CtrlConfClear':pmora14CtrlConfClear,'pmora14CtrlswMgnt':pmora14CtrlswMgnt,'pmora14CtrlColdReset':pmora14CtrlColdReset,'pmora14CtrlWarmReset':pmora14CtrlWarmReset,'pmora14CtrlaprMode':pmora14CtrlaprMode,'pmora14CtrlledTest':pmora14CtrlledTest,'pmora14CtrlGreenLed':pmora14CtrlGreenLed,'pmora14CtrlRedLed':pmora14CtrlRedLed,'pmora14CtrlLedOff':pmora14CtrlLedOff,'pmora14CtrlmaintMode':pmora14CtrlmaintMode,'pmora14CtrlMaintenance':pmora14CtrlMaintenance,'pmora14CtrlClient':pmora14CtrlClient,'pmora14CtrlLine':pmora14CtrlLine,'pmora14CtrlaprManualRestart':pmora14CtrlaprManualRestart,'pmora14CtrlAprManualRestart':pmora14CtrlAprManualRestart,'pmora14ri':pmora14ri,'pmora14riTable':pmora14riTable,'pmora14RinvLineTable':pmora14RinvLineTable,'pmora14RinvLineEntry':pmora14RinvLineEntry,_M:pmora14RinvLineIndex,'pmora14RinvportLine':pmora14RinvportLine,'pmora14RinvReloadInventory':pmora14RinvReloadInventory,'pmora14RinvHwPlatform':pmora14RinvHwPlatform,'pmora14RinvModulePlatform':pmora14RinvModulePlatform,'pmora14RinvSwPlatform':pmora14RinvSwPlatform,'pmora14RinvGwPlatform':pmora14RinvGwPlatform,'pmora14Config':pmora14Config,'pmora14CfgNoValue':pmora14CfgNoValue,'pmora14tablelineStartup':pmora14tablelineStartup,'pmora14CfgoraModuleCtrl':pmora14CfgoraModuleCtrl,'pmora14CfgautoRestartDelay':pmora14CfgautoRestartDelay,'pmora14CfgramanGain':pmora14CfgramanGain,'pmora14CfgramanMode':pmora14CfgramanMode,'pmora14CfgtiltValue':pmora14CfgtiltValue,'pmora14CfghighBackreflectionThreshold':pmora14CfghighBackreflectionThreshold,'pmora14CfgsBandThreshold':pmora14CfgsBandThreshold,'pmora14Cfgpump1ManualPower':pmora14Cfgpump1ManualPower,'pmora14Cfgpump2ManualPower':pmora14Cfgpump2ManualPower,'pmora14CfgLabels':pmora14CfgLabels,'pmora14CfgLabelclientTable':pmora14CfgLabelclientTable,'pmora14CfgLabelclientEntry':pmora14CfgLabelclientEntry,_N:pmora14CfgLabelclientIndex,'pmora14CfgLabelclientPortn':pmora14CfgLabelclientPortn,'pmora14CfgLabellineTable':pmora14CfgLabellineTable,'pmora14CfgLabellineEntry':pmora14CfgLabellineEntry,_O:pmora14CfgLabellineIndex,'pmora14CfgLabellinePortn':pmora14CfgLabellinePortn,'pmora14CfgWriteConfiguration':pmora14CfgWriteConfiguration,'pmora14traps':pmora14traps,_G:pmora14trapBoardNumber,'pmora14LineTrapCritGoesOn':pmora14LineTrapCritGoesOn,'pmora14LineTrapCritGoesOff':pmora14LineTrapCritGoesOff,'pmora14PowerTrapUrgentGoesOn':pmora14PowerTrapUrgentGoesOn,'pmora14PowerTrapUrgentGoesOff':pmora14PowerTrapUrgentGoesOff})