_K='Integer32'
_J='pmfanAlmFansFailure'
_I='pmfanAlmDefFuseA'
_H='pmfanAlmDefFuseB'
_G='pmfanAlmDefPowerB'
_F='pmfanAlmDefPowerA'
_E='Unsigned32'
_D='EKINOPS-Pmfan-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
modulepmfan=ModuleIdentity((1,3,6,1,4,1,20044,59))
if mibBuilder.loadTexts:modulepmfan.setRevisions(('2013-10-23 00:00','2014-03-27 00:00','2014-12-16 00:00','2016-05-23 00:00'))
_Pmfanalarms_ObjectIdentity=ObjectIdentity
pmfanalarms=_Pmfanalarms_ObjectIdentity((1,3,6,1,4,1,20044,59,2))
_PmfanAlmOther_ObjectIdentity=ObjectIdentity
pmfanAlmOther=_PmfanAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1))
_PmfanAlmOtherNurg_ObjectIdentity=ObjectIdentity
pmfanAlmOtherNurg=_PmfanAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,1))
_PmfanAlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmfanAlmsynthAlm2=_PmfanAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,1,2))
_PmfanAlmConfTableSave_Type=EkiOnOff
_PmfanAlmConfTableSave_Object=MibScalar
pmfanAlmConfTableSave=_PmfanAlmConfTableSave_Object((1,3,6,1,4,1,20044,59,2,1,1,2,1),_PmfanAlmConfTableSave_Type())
pmfanAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmConfTableSave.setStatus(_A)
_PmfanAlmInvUpload_Type=EkiOnOff
_PmfanAlmInvUpload_Object=MibScalar
pmfanAlmInvUpload=_PmfanAlmInvUpload_Object((1,3,6,1,4,1,20044,59,2,1,1,2,2),_PmfanAlmInvUpload_Type())
pmfanAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmInvUpload.setStatus(_A)
_PmfanAlmConfTableLoad_Type=EkiOnOff
_PmfanAlmConfTableLoad_Object=MibScalar
pmfanAlmConfTableLoad=_PmfanAlmConfTableLoad_Object((1,3,6,1,4,1,20044,59,2,1,1,2,3),_PmfanAlmConfTableLoad_Type())
pmfanAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmConfTableLoad.setStatus(_A)
_PmfanAlmCorrelatOff_Type=EkiOnOff
_PmfanAlmCorrelatOff_Object=MibScalar
pmfanAlmCorrelatOff=_PmfanAlmCorrelatOff_Object((1,3,6,1,4,1,20044,59,2,1,1,2,4),_PmfanAlmCorrelatOff_Type())
pmfanAlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmCorrelatOff.setStatus(_A)
_PmfanAlmOtherUrg_ObjectIdentity=ObjectIdentity
pmfanAlmOtherUrg=_PmfanAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,2))
_PmfanAlmfilterAlm_ObjectIdentity=ObjectIdentity
pmfanAlmfilterAlm=_PmfanAlmfilterAlm_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,2,16))
_PmfanAlmFilterNotPresent_Type=EkiOnOff
_PmfanAlmFilterNotPresent_Object=MibScalar
pmfanAlmFilterNotPresent=_PmfanAlmFilterNotPresent_Object((1,3,6,1,4,1,20044,59,2,1,2,16,15),_PmfanAlmFilterNotPresent_Type())
pmfanAlmFilterNotPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFilterNotPresent.setStatus(_A)
_PmfanAlmfansMgnt_ObjectIdentity=ObjectIdentity
pmfanAlmfansMgnt=_PmfanAlmfansMgnt_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,2,20))
_PmfanAlmFan1Fail_Type=EkiOnOff
_PmfanAlmFan1Fail_Object=MibScalar
pmfanAlmFan1Fail=_PmfanAlmFan1Fail_Object((1,3,6,1,4,1,20044,59,2,1,2,20,2),_PmfanAlmFan1Fail_Type())
pmfanAlmFan1Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFan1Fail.setStatus(_A)
_PmfanAlmFan2Fail_Type=EkiOnOff
_PmfanAlmFan2Fail_Object=MibScalar
pmfanAlmFan2Fail=_PmfanAlmFan2Fail_Object((1,3,6,1,4,1,20044,59,2,1,2,20,3),_PmfanAlmFan2Fail_Type())
pmfanAlmFan2Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFan2Fail.setStatus(_A)
_PmfanAlmFan3Fail_Type=EkiOnOff
_PmfanAlmFan3Fail_Object=MibScalar
pmfanAlmFan3Fail=_PmfanAlmFan3Fail_Object((1,3,6,1,4,1,20044,59,2,1,2,20,4),_PmfanAlmFan3Fail_Type())
pmfanAlmFan3Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFan3Fail.setStatus(_A)
_PmfanAlmFan4Fail_Type=EkiOnOff
_PmfanAlmFan4Fail_Object=MibScalar
pmfanAlmFan4Fail=_PmfanAlmFan4Fail_Object((1,3,6,1,4,1,20044,59,2,1,2,20,5),_PmfanAlmFan4Fail_Type())
pmfanAlmFan4Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFan4Fail.setStatus(_A)
_PmfanAlmFan5Fail_Type=EkiOnOff
_PmfanAlmFan5Fail_Object=MibScalar
pmfanAlmFan5Fail=_PmfanAlmFan5Fail_Object((1,3,6,1,4,1,20044,59,2,1,2,20,6),_PmfanAlmFan5Fail_Type())
pmfanAlmFan5Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFan5Fail.setStatus(_A)
_PmfanAlmFan6Fail_Type=EkiOnOff
_PmfanAlmFan6Fail_Object=MibScalar
pmfanAlmFan6Fail=_PmfanAlmFan6Fail_Object((1,3,6,1,4,1,20044,59,2,1,2,20,7),_PmfanAlmFan6Fail_Type())
pmfanAlmFan6Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFan6Fail.setStatus(_A)
_PmfanAlmFansOff_Type=EkiOnOff
_PmfanAlmFansOff_Object=MibScalar
pmfanAlmFansOff=_PmfanAlmFansOff_Object((1,3,6,1,4,1,20044,59,2,1,2,20,13),_PmfanAlmFansOff_Type())
pmfanAlmFansOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFansOff.setStatus(_A)
_PmfanAlmFanLowSpeed_Type=EkiOnOff
_PmfanAlmFanLowSpeed_Object=MibScalar
pmfanAlmFanLowSpeed=_PmfanAlmFanLowSpeed_Object((1,3,6,1,4,1,20044,59,2,1,2,20,14),_PmfanAlmFanLowSpeed_Type())
pmfanAlmFanLowSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFanLowSpeed.setStatus(_A)
_PmfanAlmchassisTempAlarms_ObjectIdentity=ObjectIdentity
pmfanAlmchassisTempAlarms=_PmfanAlmchassisTempAlarms_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,2,21))
_PmfanAlmChassisTempLowAlarm_Type=EkiOnOff
_PmfanAlmChassisTempLowAlarm_Object=MibScalar
pmfanAlmChassisTempLowAlarm=_PmfanAlmChassisTempLowAlarm_Object((1,3,6,1,4,1,20044,59,2,1,2,21,1),_PmfanAlmChassisTempLowAlarm_Type())
pmfanAlmChassisTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmChassisTempLowAlarm.setStatus(_A)
_PmfanAlmChassisTempHighAlarm_Type=EkiOnOff
_PmfanAlmChassisTempHighAlarm_Object=MibScalar
pmfanAlmChassisTempHighAlarm=_PmfanAlmChassisTempHighAlarm_Object((1,3,6,1,4,1,20044,59,2,1,2,21,2),_PmfanAlmChassisTempHighAlarm_Type())
pmfanAlmChassisTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmChassisTempHighAlarm.setStatus(_A)
_PmfanAlmchassisTempWarnings_ObjectIdentity=ObjectIdentity
pmfanAlmchassisTempWarnings=_PmfanAlmchassisTempWarnings_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,2,22))
_PmfanAlmChassisTempLowWarning_Type=EkiOnOff
_PmfanAlmChassisTempLowWarning_Object=MibScalar
pmfanAlmChassisTempLowWarning=_PmfanAlmChassisTempLowWarning_Object((1,3,6,1,4,1,20044,59,2,1,2,22,1),_PmfanAlmChassisTempLowWarning_Type())
pmfanAlmChassisTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmChassisTempLowWarning.setStatus(_A)
_PmfanAlmChassisTempHighWarning_Type=EkiOnOff
_PmfanAlmChassisTempHighWarning_Object=MibScalar
pmfanAlmChassisTempHighWarning=_PmfanAlmChassisTempHighWarning_Object((1,3,6,1,4,1,20044,59,2,1,2,22,2),_PmfanAlmChassisTempHighWarning_Type())
pmfanAlmChassisTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmChassisTempHighWarning.setStatus(_A)
_PmfanAlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
pmfanAlmmodInitFailLevel2=_PmfanAlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,2,70))
_PmfanAlmRegReadFail_Type=EkiOnOff
_PmfanAlmRegReadFail_Object=MibScalar
pmfanAlmRegReadFail=_PmfanAlmRegReadFail_Object((1,3,6,1,4,1,20044,59,2,1,2,70,1),_PmfanAlmRegReadFail_Type())
pmfanAlmRegReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmRegReadFail.setStatus(_A)
_PmfanAlmResetHwInitFail_Type=EkiOnOff
_PmfanAlmResetHwInitFail_Object=MibScalar
pmfanAlmResetHwInitFail=_PmfanAlmResetHwInitFail_Object((1,3,6,1,4,1,20044,59,2,1,2,70,2),_PmfanAlmResetHwInitFail_Type())
pmfanAlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmResetHwInitFail.setStatus(_A)
_PmfanAlmConfReadFail_Type=EkiOnOff
_PmfanAlmConfReadFail_Object=MibScalar
pmfanAlmConfReadFail=_PmfanAlmConfReadFail_Object((1,3,6,1,4,1,20044,59,2,1,2,70,3),_PmfanAlmConfReadFail_Type())
pmfanAlmConfReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmConfReadFail.setStatus(_A)
_PmfanAlmInvReadFail_Type=EkiOnOff
_PmfanAlmInvReadFail_Object=MibScalar
pmfanAlmInvReadFail=_PmfanAlmInvReadFail_Object((1,3,6,1,4,1,20044,59,2,1,2,70,4),_PmfanAlmInvReadFail_Type())
pmfanAlmInvReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmInvReadFail.setStatus(_A)
_PmfanAlmOtherCrit_ObjectIdentity=ObjectIdentity
pmfanAlmOtherCrit=_PmfanAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,3))
_PmfanAlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmfanAlmsynthAlm0=_PmfanAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,3,0))
_PmfanAlmModuleGlobFailure_Type=EkiOnOff
_PmfanAlmModuleGlobFailure_Object=MibScalar
pmfanAlmModuleGlobFailure=_PmfanAlmModuleGlobFailure_Object((1,3,6,1,4,1,20044,59,2,1,3,0,9),_PmfanAlmModuleGlobFailure_Type())
pmfanAlmModuleGlobFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmModuleGlobFailure.setStatus(_A)
_PmfanAlmDefPowerA_Type=EkiOnOff
_PmfanAlmDefPowerA_Object=MibScalar
pmfanAlmDefPowerA=_PmfanAlmDefPowerA_Object((1,3,6,1,4,1,20044,59,2,1,3,0,11),_PmfanAlmDefPowerA_Type())
pmfanAlmDefPowerA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmDefPowerA.setStatus(_A)
_PmfanAlmDefPowerB_Type=EkiOnOff
_PmfanAlmDefPowerB_Object=MibScalar
pmfanAlmDefPowerB=_PmfanAlmDefPowerB_Object((1,3,6,1,4,1,20044,59,2,1,3,0,12),_PmfanAlmDefPowerB_Type())
pmfanAlmDefPowerB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmDefPowerB.setStatus(_A)
_PmfanAlmAcknowledge_Type=EkiOnOff
_PmfanAlmAcknowledge_Object=MibScalar
pmfanAlmAcknowledge=_PmfanAlmAcknowledge_Object((1,3,6,1,4,1,20044,59,2,1,3,0,13),_PmfanAlmAcknowledge_Type())
pmfanAlmAcknowledge.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmAcknowledge.setStatus(_A)
_PmfanAlmDefFuseA_Type=EkiOnOff
_PmfanAlmDefFuseA_Object=MibScalar
pmfanAlmDefFuseA=_PmfanAlmDefFuseA_Object((1,3,6,1,4,1,20044,59,2,1,3,0,15),_PmfanAlmDefFuseA_Type())
pmfanAlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmDefFuseA.setStatus(_A)
_PmfanAlmDefFuseB_Type=EkiOnOff
_PmfanAlmDefFuseB_Object=MibScalar
pmfanAlmDefFuseB=_PmfanAlmDefFuseB_Object((1,3,6,1,4,1,20044,59,2,1,3,0,16),_PmfanAlmDefFuseB_Type())
pmfanAlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmDefFuseB.setStatus(_A)
_PmfanAlmsynthAlm1_ObjectIdentity=ObjectIdentity
pmfanAlmsynthAlm1=_PmfanAlmsynthAlm1_ObjectIdentity((1,3,6,1,4,1,20044,59,2,1,3,1))
_PmfanAlmFansFailure_Type=EkiOnOff
_PmfanAlmFansFailure_Object=MibScalar
pmfanAlmFansFailure=_PmfanAlmFansFailure_Object((1,3,6,1,4,1,20044,59,2,1,3,1,10),_PmfanAlmFansFailure_Type())
pmfanAlmFansFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanAlmFansFailure.setStatus(_A)
_Pmfanmeasures_ObjectIdentity=ObjectIdentity
pmfanmeasures=_Pmfanmeasures_ObjectIdentity((1,3,6,1,4,1,20044,59,3))
_PmfanMesrOther_ObjectIdentity=ObjectIdentity
pmfanMesrOther=_PmfanMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,59,3,1))
class _PmfanMesrtempChassis_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmfanMesrtempChassis_Type.__name__=_E
_PmfanMesrtempChassis_Object=MibScalar
pmfanMesrtempChassis=_PmfanMesrtempChassis_Object((1,3,6,1,4,1,20044,59,3,1,64),_PmfanMesrtempChassis_Type())
pmfanMesrtempChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanMesrtempChassis.setStatus(_A)
class _PmfanMesrtempModule_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PmfanMesrtempModule_Type.__name__=_E
_PmfanMesrtempModule_Object=MibScalar
pmfanMesrtempModule=_PmfanMesrtempModule_Object((1,3,6,1,4,1,20044,59,3,1,65),_PmfanMesrtempModule_Type())
pmfanMesrtempModule.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanMesrtempModule.setStatus(_A)
_PmfancontrolsWrite_ObjectIdentity=ObjectIdentity
pmfancontrolsWrite=_PmfancontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,59,6))
_PmfanCtrlOther_ObjectIdentity=ObjectIdentity
pmfanCtrlOther=_PmfanCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1))
_PmfanCtrlsynth0_ObjectIdentity=ObjectIdentity
pmfanCtrlsynth0=_PmfanCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,0))
_PmfanCtrlConfLoad_Type=EkiOnOff
_PmfanCtrlConfLoad_Object=MibScalar
pmfanCtrlConfLoad=_PmfanCtrlConfLoad_Object((1,3,6,1,4,1,20044,59,6,1,0,1),_PmfanCtrlConfLoad_Type())
pmfanCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlConfLoad.setStatus(_A)
_PmfanCtrlConfFlash_Type=EkiOnOff
_PmfanCtrlConfFlash_Object=MibScalar
pmfanCtrlConfFlash=_PmfanCtrlConfFlash_Object((1,3,6,1,4,1,20044,59,6,1,0,9),_PmfanCtrlConfFlash_Type())
pmfanCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlConfFlash.setStatus(_A)
_PmfanCtrlConfClear_Type=EkiOnOff
_PmfanCtrlConfClear_Object=MibScalar
pmfanCtrlConfClear=_PmfanCtrlConfClear_Object((1,3,6,1,4,1,20044,59,6,1,0,13),_PmfanCtrlConfClear_Type())
pmfanCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlConfClear.setStatus(_A)
_PmfanCtrlsynth4_ObjectIdentity=ObjectIdentity
pmfanCtrlsynth4=_PmfanCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,4))
_PmfanCtrlCorrelatOn_Type=EkiOnOff
_PmfanCtrlCorrelatOn_Object=MibScalar
pmfanCtrlCorrelatOn=_PmfanCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,59,6,1,4,1),_PmfanCtrlCorrelatOn_Type())
pmfanCtrlCorrelatOn.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlCorrelatOn.setStatus(_A)
_PmfanCtrlCorrelatOff_Type=EkiOnOff
_PmfanCtrlCorrelatOff_Object=MibScalar
pmfanCtrlCorrelatOff=_PmfanCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,59,6,1,4,2),_PmfanCtrlCorrelatOff_Type())
pmfanCtrlCorrelatOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlCorrelatOff.setStatus(_A)
_PmfanCtrlswMgnt_ObjectIdentity=ObjectIdentity
pmfanCtrlswMgnt=_PmfanCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,5))
_PmfanCtrlColdReset_Type=EkiOnOff
_PmfanCtrlColdReset_Object=MibScalar
pmfanCtrlColdReset=_PmfanCtrlColdReset_Object((1,3,6,1,4,1,20044,59,6,1,5,2),_PmfanCtrlColdReset_Type())
pmfanCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlColdReset.setStatus(_A)
_PmfanCtrlWarmReset_Type=EkiOnOff
_PmfanCtrlWarmReset_Object=MibScalar
pmfanCtrlWarmReset=_PmfanCtrlWarmReset_Object((1,3,6,1,4,1,20044,59,6,1,5,3),_PmfanCtrlWarmReset_Type())
pmfanCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlWarmReset.setStatus(_A)
_PmfanCtrlpoweraLed_ObjectIdentity=ObjectIdentity
pmfanCtrlpoweraLed=_PmfanCtrlpoweraLed_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,43))
_PmfanCtrlLedPowerA_Type=EkiOnOff
_PmfanCtrlLedPowerA_Object=MibScalar
pmfanCtrlLedPowerA=_PmfanCtrlLedPowerA_Object((1,3,6,1,4,1,20044,59,6,1,43,1),_PmfanCtrlLedPowerA_Type())
pmfanCtrlLedPowerA.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlLedPowerA.setStatus(_A)
_PmfanCtrlpowerbLed_ObjectIdentity=ObjectIdentity
pmfanCtrlpowerbLed=_PmfanCtrlpowerbLed_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,44))
_PmfanCtrlLedPowerB_Type=EkiOnOff
_PmfanCtrlLedPowerB_Object=MibScalar
pmfanCtrlLedPowerB=_PmfanCtrlLedPowerB_Object((1,3,6,1,4,1,20044,59,6,1,44,1),_PmfanCtrlLedPowerB_Type())
pmfanCtrlLedPowerB.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlLedPowerB.setStatus(_A)
_PmfanCtrlledTest_ObjectIdentity=ObjectIdentity
pmfanCtrlledTest=_PmfanCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,64))
_PmfanCtrlGreenLed_Type=EkiOnOff
_PmfanCtrlGreenLed_Object=MibScalar
pmfanCtrlGreenLed=_PmfanCtrlGreenLed_Object((1,3,6,1,4,1,20044,59,6,1,64,1),_PmfanCtrlGreenLed_Type())
pmfanCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlGreenLed.setStatus(_A)
_PmfanCtrlRedLed_Type=EkiOnOff
_PmfanCtrlRedLed_Object=MibScalar
pmfanCtrlRedLed=_PmfanCtrlRedLed_Object((1,3,6,1,4,1,20044,59,6,1,64,2),_PmfanCtrlRedLed_Type())
pmfanCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlRedLed.setStatus(_A)
_PmfanCtrlLedOff_Type=EkiOnOff
_PmfanCtrlLedOff_Object=MibScalar
pmfanCtrlLedOff=_PmfanCtrlLedOff_Object((1,3,6,1,4,1,20044,59,6,1,64,3),_PmfanCtrlLedOff_Type())
pmfanCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlLedOff.setStatus(_A)
_PmfanCtrlacknowledgeActiv_ObjectIdentity=ObjectIdentity
pmfanCtrlacknowledgeActiv=_PmfanCtrlacknowledgeActiv_ObjectIdentity((1,3,6,1,4,1,20044,59,6,1,65))
_PmfanCtrlAckActiv_Type=EkiOnOff
_PmfanCtrlAckActiv_Object=MibScalar
pmfanCtrlAckActiv=_PmfanCtrlAckActiv_Object((1,3,6,1,4,1,20044,59,6,1,65,1),_PmfanCtrlAckActiv_Type())
pmfanCtrlAckActiv.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCtrlAckActiv.setStatus(_A)
_Pmfanri_ObjectIdentity=ObjectIdentity
pmfanri=_Pmfanri_ObjectIdentity((1,3,6,1,4,1,20044,59,7))
_PmfanriTable_ObjectIdentity=ObjectIdentity
pmfanriTable=_PmfanriTable_ObjectIdentity((1,3,6,1,4,1,20044,59,7,1))
_PmfanRinvReloadInventory_Type=EkiOnOff
_PmfanRinvReloadInventory_Object=MibScalar
pmfanRinvReloadInventory=_PmfanRinvReloadInventory_Object((1,3,6,1,4,1,20044,59,7,2),_PmfanRinvReloadInventory_Type())
pmfanRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanRinvReloadInventory.setStatus(_A)
_PmfanRinvHwPlatform_Type=DisplayString
_PmfanRinvHwPlatform_Object=MibScalar
pmfanRinvHwPlatform=_PmfanRinvHwPlatform_Object((1,3,6,1,4,1,20044,59,7,3),_PmfanRinvHwPlatform_Type())
pmfanRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanRinvHwPlatform.setStatus(_A)
_PmfanRinvModulePlatform_Type=DisplayString
_PmfanRinvModulePlatform_Object=MibScalar
pmfanRinvModulePlatform=_PmfanRinvModulePlatform_Object((1,3,6,1,4,1,20044,59,7,4),_PmfanRinvModulePlatform_Type())
pmfanRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanRinvModulePlatform.setStatus(_A)
_PmfanRinvSwPlatform_Type=DisplayString
_PmfanRinvSwPlatform_Object=MibScalar
pmfanRinvSwPlatform=_PmfanRinvSwPlatform_Object((1,3,6,1,4,1,20044,59,7,5),_PmfanRinvSwPlatform_Type())
pmfanRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfanRinvSwPlatform.setStatus(_A)
_PmfanConfig_ObjectIdentity=ObjectIdentity
pmfanConfig=_PmfanConfig_ObjectIdentity((1,3,6,1,4,1,20044,59,9))
_PmfanCfgLsd_ObjectIdentity=ObjectIdentity
pmfanCfgLsd=_PmfanCfgLsd_ObjectIdentity((1,3,6,1,4,1,20044,59,9,1))
_PmfanCfgStartUp_ObjectIdentity=ObjectIdentity
pmfanCfgStartUp=_PmfanCfgStartUp_ObjectIdentity((1,3,6,1,4,1,20044,59,9,2))
_Pmfantableother_ObjectIdentity=ObjectIdentity
pmfantableother=_Pmfantableother_ObjectIdentity((1,3,6,1,4,1,20044,59,9,2,1))
class _PmfanCfglowspeedThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmfanCfglowspeedThresh_Type.__name__=_E
_PmfanCfglowspeedThresh_Object=MibScalar
pmfanCfglowspeedThresh=_PmfanCfglowspeedThresh_Object((1,3,6,1,4,1,20044,59,9,2,1,2),_PmfanCfglowspeedThresh_Type())
pmfanCfglowspeedThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCfglowspeedThresh.setStatus(_A)
class _PmfanCfghighspeedThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmfanCfghighspeedThresh_Type.__name__=_E
_PmfanCfghighspeedThresh_Object=MibScalar
pmfanCfghighspeedThresh=_PmfanCfghighspeedThresh_Object((1,3,6,1,4,1,20044,59,9,2,1,3),_PmfanCfghighspeedThresh_Type())
pmfanCfghighspeedThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCfghighspeedThresh.setStatus(_A)
class _PmfanCfgpmfanMgnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_PmfanCfgpmfanMgnt_Type.__name__=_E
_PmfanCfgpmfanMgnt_Object=MibScalar
pmfanCfgpmfanMgnt=_PmfanCfgpmfanMgnt_Object((1,3,6,1,4,1,20044,59,9,2,1,10),_PmfanCfgpmfanMgnt_Type())
pmfanCfgpmfanMgnt.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCfgpmfanMgnt.setStatus(_A)
_PmfanCfgLabels_ObjectIdentity=ObjectIdentity
pmfanCfgLabels=_PmfanCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,59,9,3))
_PmfanCfgWriteConfiguration_Type=EkiOnOff
_PmfanCfgWriteConfiguration_Object=MibScalar
pmfanCfgWriteConfiguration=_PmfanCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,59,9,257),_PmfanCfgWriteConfiguration_Type())
pmfanCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:pmfanCfgWriteConfiguration.setStatus(_A)
_Pmfantraps_ObjectIdentity=ObjectIdentity
pmfantraps=_Pmfantraps_ObjectIdentity((1,3,6,1,4,1,20044,59,10))
class _PmfantrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PmfantrapBoardNumber_Type.__name__=_K
_PmfantrapBoardNumber_Object=MibScalar
pmfantrapBoardNumber=_PmfantrapBoardNumber_Object((1,3,6,1,4,1,20044,59,10,2),_PmfantrapBoardNumber_Type())
pmfantrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmfantrapBoardNumber.setStatus(_A)
pmfanPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,59,10,32))
pmfanPowerTrapUrgentGoesOn.setObjects(*((_D,_F),(_D,_G)))
if mibBuilder.loadTexts:pmfanPowerTrapUrgentGoesOn.setStatus(_A)
pmfanPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,59,10,33))
pmfanPowerTrapUrgentGoesOff.setObjects(*((_D,_F),(_D,_G)))
if mibBuilder.loadTexts:pmfanPowerTrapUrgentGoesOff.setStatus(_A)
pmfanPowerTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,59,10,34))
pmfanPowerTrapCritGoesOn.setObjects(*((_D,_H),(_D,_I)))
if mibBuilder.loadTexts:pmfanPowerTrapCritGoesOn.setStatus(_A)
pmfanPowerTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,59,10,35))
pmfanPowerTrapCritGoesOff.setObjects(*((_D,_H),(_D,_I)))
if mibBuilder.loadTexts:pmfanPowerTrapCritGoesOff.setStatus(_A)
pmfanFanTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,59,10,44))
pmfanFanTrapCritGoesOn.setObjects((_D,_J))
if mibBuilder.loadTexts:pmfanFanTrapCritGoesOn.setStatus(_A)
pmfanFanTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,59,10,45))
pmfanFanTrapCritGoesOff.setObjects((_D,_J))
if mibBuilder.loadTexts:pmfanFanTrapCritGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'modulepmfan':modulepmfan,'pmfanalarms':pmfanalarms,'pmfanAlmOther':pmfanAlmOther,'pmfanAlmOtherNurg':pmfanAlmOtherNurg,'pmfanAlmsynthAlm2':pmfanAlmsynthAlm2,'pmfanAlmConfTableSave':pmfanAlmConfTableSave,'pmfanAlmInvUpload':pmfanAlmInvUpload,'pmfanAlmConfTableLoad':pmfanAlmConfTableLoad,'pmfanAlmCorrelatOff':pmfanAlmCorrelatOff,'pmfanAlmOtherUrg':pmfanAlmOtherUrg,'pmfanAlmfilterAlm':pmfanAlmfilterAlm,'pmfanAlmFilterNotPresent':pmfanAlmFilterNotPresent,'pmfanAlmfansMgnt':pmfanAlmfansMgnt,'pmfanAlmFan1Fail':pmfanAlmFan1Fail,'pmfanAlmFan2Fail':pmfanAlmFan2Fail,'pmfanAlmFan3Fail':pmfanAlmFan3Fail,'pmfanAlmFan4Fail':pmfanAlmFan4Fail,'pmfanAlmFan5Fail':pmfanAlmFan5Fail,'pmfanAlmFan6Fail':pmfanAlmFan6Fail,'pmfanAlmFansOff':pmfanAlmFansOff,'pmfanAlmFanLowSpeed':pmfanAlmFanLowSpeed,'pmfanAlmchassisTempAlarms':pmfanAlmchassisTempAlarms,'pmfanAlmChassisTempLowAlarm':pmfanAlmChassisTempLowAlarm,'pmfanAlmChassisTempHighAlarm':pmfanAlmChassisTempHighAlarm,'pmfanAlmchassisTempWarnings':pmfanAlmchassisTempWarnings,'pmfanAlmChassisTempLowWarning':pmfanAlmChassisTempLowWarning,'pmfanAlmChassisTempHighWarning':pmfanAlmChassisTempHighWarning,'pmfanAlmmodInitFailLevel2':pmfanAlmmodInitFailLevel2,'pmfanAlmRegReadFail':pmfanAlmRegReadFail,'pmfanAlmResetHwInitFail':pmfanAlmResetHwInitFail,'pmfanAlmConfReadFail':pmfanAlmConfReadFail,'pmfanAlmInvReadFail':pmfanAlmInvReadFail,'pmfanAlmOtherCrit':pmfanAlmOtherCrit,'pmfanAlmsynthAlm0':pmfanAlmsynthAlm0,'pmfanAlmModuleGlobFailure':pmfanAlmModuleGlobFailure,_F:pmfanAlmDefPowerA,_G:pmfanAlmDefPowerB,'pmfanAlmAcknowledge':pmfanAlmAcknowledge,_I:pmfanAlmDefFuseA,_H:pmfanAlmDefFuseB,'pmfanAlmsynthAlm1':pmfanAlmsynthAlm1,_J:pmfanAlmFansFailure,'pmfanmeasures':pmfanmeasures,'pmfanMesrOther':pmfanMesrOther,'pmfanMesrtempChassis':pmfanMesrtempChassis,'pmfanMesrtempModule':pmfanMesrtempModule,'pmfancontrolsWrite':pmfancontrolsWrite,'pmfanCtrlOther':pmfanCtrlOther,'pmfanCtrlsynth0':pmfanCtrlsynth0,'pmfanCtrlConfLoad':pmfanCtrlConfLoad,'pmfanCtrlConfFlash':pmfanCtrlConfFlash,'pmfanCtrlConfClear':pmfanCtrlConfClear,'pmfanCtrlsynth4':pmfanCtrlsynth4,'pmfanCtrlCorrelatOn':pmfanCtrlCorrelatOn,'pmfanCtrlCorrelatOff':pmfanCtrlCorrelatOff,'pmfanCtrlswMgnt':pmfanCtrlswMgnt,'pmfanCtrlColdReset':pmfanCtrlColdReset,'pmfanCtrlWarmReset':pmfanCtrlWarmReset,'pmfanCtrlpoweraLed':pmfanCtrlpoweraLed,'pmfanCtrlLedPowerA':pmfanCtrlLedPowerA,'pmfanCtrlpowerbLed':pmfanCtrlpowerbLed,'pmfanCtrlLedPowerB':pmfanCtrlLedPowerB,'pmfanCtrlledTest':pmfanCtrlledTest,'pmfanCtrlGreenLed':pmfanCtrlGreenLed,'pmfanCtrlRedLed':pmfanCtrlRedLed,'pmfanCtrlLedOff':pmfanCtrlLedOff,'pmfanCtrlacknowledgeActiv':pmfanCtrlacknowledgeActiv,'pmfanCtrlAckActiv':pmfanCtrlAckActiv,'pmfanri':pmfanri,'pmfanriTable':pmfanriTable,'pmfanRinvReloadInventory':pmfanRinvReloadInventory,'pmfanRinvHwPlatform':pmfanRinvHwPlatform,'pmfanRinvModulePlatform':pmfanRinvModulePlatform,'pmfanRinvSwPlatform':pmfanRinvSwPlatform,'pmfanConfig':pmfanConfig,'pmfanCfgLsd':pmfanCfgLsd,'pmfanCfgStartUp':pmfanCfgStartUp,'pmfantableother':pmfantableother,'pmfanCfglowspeedThresh':pmfanCfglowspeedThresh,'pmfanCfghighspeedThresh':pmfanCfghighspeedThresh,'pmfanCfgpmfanMgnt':pmfanCfgpmfanMgnt,'pmfanCfgLabels':pmfanCfgLabels,'pmfanCfgWriteConfiguration':pmfanCfgWriteConfiguration,'pmfantraps':pmfantraps,'pmfantrapBoardNumber':pmfantrapBoardNumber,'pmfanPowerTrapUrgentGoesOn':pmfanPowerTrapUrgentGoesOn,'pmfanPowerTrapUrgentGoesOff':pmfanPowerTrapUrgentGoesOff,'pmfanPowerTrapCritGoesOn':pmfanPowerTrapCritGoesOn,'pmfanPowerTrapCritGoesOff':pmfanPowerTrapCritGoesOff,'pmfanFanTrapCritGoesOn':pmfanFanTrapCritGoesOn,'pmfanFanTrapCritGoesOff':pmfanFanTrapCritGoesOff})