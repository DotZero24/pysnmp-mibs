_L='Integer32'
_K='trfanAlmFansFailure'
_J='trfanAlmDefFuse'
_I='trfanAlmPwr12v2Fail'
_H='trfanAlmPwr12v1Fail'
_G='trfanAlmDefPowerB'
_F='trfanAlmDefPowerA'
_E='Unsigned32'
_D='EKINOPS-Trfan-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EkiApiState,EkiMeasureType,EkiMode,EkiOnOff,EkiProtocol,EkiState,ekinops=mibBuilder.importSymbols('EKINOPS-MIB','EkiApiState','EkiMeasureType','EkiMode','EkiOnOff','EkiProtocol','EkiState','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
moduletrfan=ModuleIdentity((1,3,6,1,4,1,20044,45))
if mibBuilder.loadTexts:moduletrfan.setRevisions(('2010-01-04 00:00','2010-10-28 00:00','2012-07-04 00:00','2013-09-02 00:00','2014-03-26 00:00','2014-11-25 00:00','2016-05-23 00:00','2017-06-09 00:00'))
_Trfanalarms_ObjectIdentity=ObjectIdentity
trfanalarms=_Trfanalarms_ObjectIdentity((1,3,6,1,4,1,20044,45,2))
_TrfanAlmOther_ObjectIdentity=ObjectIdentity
trfanAlmOther=_TrfanAlmOther_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1))
_TrfanAlmOtherNurg_ObjectIdentity=ObjectIdentity
trfanAlmOtherNurg=_TrfanAlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,1))
_TrfanAlmsynthAlm2_ObjectIdentity=ObjectIdentity
trfanAlmsynthAlm2=_TrfanAlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,1,2))
_TrfanAlmConfTableSave_Type=EkiOnOff
_TrfanAlmConfTableSave_Object=MibScalar
trfanAlmConfTableSave=_TrfanAlmConfTableSave_Object((1,3,6,1,4,1,20044,45,2,1,1,2,1),_TrfanAlmConfTableSave_Type())
trfanAlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmConfTableSave.setStatus(_A)
_TrfanAlmInvUpload_Type=EkiOnOff
_TrfanAlmInvUpload_Object=MibScalar
trfanAlmInvUpload=_TrfanAlmInvUpload_Object((1,3,6,1,4,1,20044,45,2,1,1,2,2),_TrfanAlmInvUpload_Type())
trfanAlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmInvUpload.setStatus(_A)
_TrfanAlmConfTableLoad_Type=EkiOnOff
_TrfanAlmConfTableLoad_Object=MibScalar
trfanAlmConfTableLoad=_TrfanAlmConfTableLoad_Object((1,3,6,1,4,1,20044,45,2,1,1,2,3),_TrfanAlmConfTableLoad_Type())
trfanAlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmConfTableLoad.setStatus(_A)
_TrfanAlmCorrelatOff_Type=EkiOnOff
_TrfanAlmCorrelatOff_Object=MibScalar
trfanAlmCorrelatOff=_TrfanAlmCorrelatOff_Object((1,3,6,1,4,1,20044,45,2,1,1,2,4),_TrfanAlmCorrelatOff_Type())
trfanAlmCorrelatOff.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmCorrelatOff.setStatus(_A)
_TrfanAlmOtherUrg_ObjectIdentity=ObjectIdentity
trfanAlmOtherUrg=_TrfanAlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,2))
_TrfanAlmfilterAlm_ObjectIdentity=ObjectIdentity
trfanAlmfilterAlm=_TrfanAlmfilterAlm_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,2,16))
_TrfanAlmFilterNotPresent_Type=EkiOnOff
_TrfanAlmFilterNotPresent_Object=MibScalar
trfanAlmFilterNotPresent=_TrfanAlmFilterNotPresent_Object((1,3,6,1,4,1,20044,45,2,1,2,16,15),_TrfanAlmFilterNotPresent_Type())
trfanAlmFilterNotPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFilterNotPresent.setStatus(_A)
_TrfanAlmfansMgnt_ObjectIdentity=ObjectIdentity
trfanAlmfansMgnt=_TrfanAlmfansMgnt_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,2,20))
_TrfanAlmFan1Fail_Type=EkiOnOff
_TrfanAlmFan1Fail_Object=MibScalar
trfanAlmFan1Fail=_TrfanAlmFan1Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,20,2),_TrfanAlmFan1Fail_Type())
trfanAlmFan1Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFan1Fail.setStatus(_A)
_TrfanAlmFan2Fail_Type=EkiOnOff
_TrfanAlmFan2Fail_Object=MibScalar
trfanAlmFan2Fail=_TrfanAlmFan2Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,20,3),_TrfanAlmFan2Fail_Type())
trfanAlmFan2Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFan2Fail.setStatus(_A)
_TrfanAlmFan3Fail_Type=EkiOnOff
_TrfanAlmFan3Fail_Object=MibScalar
trfanAlmFan3Fail=_TrfanAlmFan3Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,20,4),_TrfanAlmFan3Fail_Type())
trfanAlmFan3Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFan3Fail.setStatus(_A)
_TrfanAlmFan4Fail_Type=EkiOnOff
_TrfanAlmFan4Fail_Object=MibScalar
trfanAlmFan4Fail=_TrfanAlmFan4Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,20,5),_TrfanAlmFan4Fail_Type())
trfanAlmFan4Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFan4Fail.setStatus(_A)
_TrfanAlmFan5Fail_Type=EkiOnOff
_TrfanAlmFan5Fail_Object=MibScalar
trfanAlmFan5Fail=_TrfanAlmFan5Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,20,6),_TrfanAlmFan5Fail_Type())
trfanAlmFan5Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFan5Fail.setStatus(_A)
_TrfanAlmFan6Fail_Type=EkiOnOff
_TrfanAlmFan6Fail_Object=MibScalar
trfanAlmFan6Fail=_TrfanAlmFan6Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,20,7),_TrfanAlmFan6Fail_Type())
trfanAlmFan6Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFan6Fail.setStatus(_A)
_TrfanAlmFansOff_Type=EkiOnOff
_TrfanAlmFansOff_Object=MibScalar
trfanAlmFansOff=_TrfanAlmFansOff_Object((1,3,6,1,4,1,20044,45,2,1,2,20,13),_TrfanAlmFansOff_Type())
trfanAlmFansOff.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFansOff.setStatus(_A)
_TrfanAlmFanLowSpeed_Type=EkiOnOff
_TrfanAlmFanLowSpeed_Object=MibScalar
trfanAlmFanLowSpeed=_TrfanAlmFanLowSpeed_Object((1,3,6,1,4,1,20044,45,2,1,2,20,14),_TrfanAlmFanLowSpeed_Type())
trfanAlmFanLowSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFanLowSpeed.setStatus(_A)
_TrfanAlmpwrMgnt_ObjectIdentity=ObjectIdentity
trfanAlmpwrMgnt=_TrfanAlmpwrMgnt_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,2,24))
_TrfanAlmPwr12v1Fail_Type=EkiOnOff
_TrfanAlmPwr12v1Fail_Object=MibScalar
trfanAlmPwr12v1Fail=_TrfanAlmPwr12v1Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,24,13),_TrfanAlmPwr12v1Fail_Type())
trfanAlmPwr12v1Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmPwr12v1Fail.setStatus(_A)
_TrfanAlmPwr12v2Fail_Type=EkiOnOff
_TrfanAlmPwr12v2Fail_Object=MibScalar
trfanAlmPwr12v2Fail=_TrfanAlmPwr12v2Fail_Object((1,3,6,1,4,1,20044,45,2,1,2,24,14),_TrfanAlmPwr12v2Fail_Type())
trfanAlmPwr12v2Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmPwr12v2Fail.setStatus(_A)
_TrfanAlmmodInitFailLevel2_ObjectIdentity=ObjectIdentity
trfanAlmmodInitFailLevel2=_TrfanAlmmodInitFailLevel2_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,2,70))
_TrfanAlmRegReadFail_Type=EkiOnOff
_TrfanAlmRegReadFail_Object=MibScalar
trfanAlmRegReadFail=_TrfanAlmRegReadFail_Object((1,3,6,1,4,1,20044,45,2,1,2,70,1),_TrfanAlmRegReadFail_Type())
trfanAlmRegReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmRegReadFail.setStatus(_A)
_TrfanAlmResetHwInitFail_Type=EkiOnOff
_TrfanAlmResetHwInitFail_Object=MibScalar
trfanAlmResetHwInitFail=_TrfanAlmResetHwInitFail_Object((1,3,6,1,4,1,20044,45,2,1,2,70,2),_TrfanAlmResetHwInitFail_Type())
trfanAlmResetHwInitFail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmResetHwInitFail.setStatus(_A)
_TrfanAlmConfReadFail_Type=EkiOnOff
_TrfanAlmConfReadFail_Object=MibScalar
trfanAlmConfReadFail=_TrfanAlmConfReadFail_Object((1,3,6,1,4,1,20044,45,2,1,2,70,3),_TrfanAlmConfReadFail_Type())
trfanAlmConfReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmConfReadFail.setStatus(_A)
_TrfanAlmInvReadFail_Type=EkiOnOff
_TrfanAlmInvReadFail_Object=MibScalar
trfanAlmInvReadFail=_TrfanAlmInvReadFail_Object((1,3,6,1,4,1,20044,45,2,1,2,70,4),_TrfanAlmInvReadFail_Type())
trfanAlmInvReadFail.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmInvReadFail.setStatus(_A)
_TrfanAlmOtherCrit_ObjectIdentity=ObjectIdentity
trfanAlmOtherCrit=_TrfanAlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,3))
_TrfanAlmsynthAlm0_ObjectIdentity=ObjectIdentity
trfanAlmsynthAlm0=_TrfanAlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,3,0))
_TrfanAlmModuleGlobFailure_Type=EkiOnOff
_TrfanAlmModuleGlobFailure_Object=MibScalar
trfanAlmModuleGlobFailure=_TrfanAlmModuleGlobFailure_Object((1,3,6,1,4,1,20044,45,2,1,3,0,9),_TrfanAlmModuleGlobFailure_Type())
trfanAlmModuleGlobFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmModuleGlobFailure.setStatus(_A)
_TrfanAlmDefPowerA_Type=EkiOnOff
_TrfanAlmDefPowerA_Object=MibScalar
trfanAlmDefPowerA=_TrfanAlmDefPowerA_Object((1,3,6,1,4,1,20044,45,2,1,3,0,11),_TrfanAlmDefPowerA_Type())
trfanAlmDefPowerA.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmDefPowerA.setStatus(_A)
_TrfanAlmDefPowerB_Type=EkiOnOff
_TrfanAlmDefPowerB_Object=MibScalar
trfanAlmDefPowerB=_TrfanAlmDefPowerB_Object((1,3,6,1,4,1,20044,45,2,1,3,0,12),_TrfanAlmDefPowerB_Type())
trfanAlmDefPowerB.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmDefPowerB.setStatus(_A)
_TrfanAlmAcknowledge_Type=EkiOnOff
_TrfanAlmAcknowledge_Object=MibScalar
trfanAlmAcknowledge=_TrfanAlmAcknowledge_Object((1,3,6,1,4,1,20044,45,2,1,3,0,13),_TrfanAlmAcknowledge_Type())
trfanAlmAcknowledge.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmAcknowledge.setStatus(_A)
_TrfanAlmDefFuse_Type=EkiOnOff
_TrfanAlmDefFuse_Object=MibScalar
trfanAlmDefFuse=_TrfanAlmDefFuse_Object((1,3,6,1,4,1,20044,45,2,1,3,0,15),_TrfanAlmDefFuse_Type())
trfanAlmDefFuse.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmDefFuse.setStatus(_A)
_TrfanAlmsynthAlm1_ObjectIdentity=ObjectIdentity
trfanAlmsynthAlm1=_TrfanAlmsynthAlm1_ObjectIdentity((1,3,6,1,4,1,20044,45,2,1,3,1))
_TrfanAlmFansFailure_Type=EkiOnOff
_TrfanAlmFansFailure_Object=MibScalar
trfanAlmFansFailure=_TrfanAlmFansFailure_Object((1,3,6,1,4,1,20044,45,2,1,3,1,10),_TrfanAlmFansFailure_Type())
trfanAlmFansFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanAlmFansFailure.setStatus(_A)
_Trfanmeasures_ObjectIdentity=ObjectIdentity
trfanmeasures=_Trfanmeasures_ObjectIdentity((1,3,6,1,4,1,20044,45,3))
_TrfanMesrOther_ObjectIdentity=ObjectIdentity
trfanMesrOther=_TrfanMesrOther_ObjectIdentity((1,3,6,1,4,1,20044,45,3,1))
class _TrfanMesrvoltMeas12v1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TrfanMesrvoltMeas12v1_Type.__name__=_E
_TrfanMesrvoltMeas12v1_Object=MibScalar
trfanMesrvoltMeas12v1=_TrfanMesrvoltMeas12v1_Object((1,3,6,1,4,1,20044,45,3,1,16),_TrfanMesrvoltMeas12v1_Type())
trfanMesrvoltMeas12v1.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanMesrvoltMeas12v1.setStatus(_A)
class _TrfanMesrvoltMeas12v2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TrfanMesrvoltMeas12v2_Type.__name__=_E
_TrfanMesrvoltMeas12v2_Object=MibScalar
trfanMesrvoltMeas12v2=_TrfanMesrvoltMeas12v2_Object((1,3,6,1,4,1,20044,45,3,1,17),_TrfanMesrvoltMeas12v2_Type())
trfanMesrvoltMeas12v2.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanMesrvoltMeas12v2.setStatus(_A)
class _TrfanMesrtempChassis_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TrfanMesrtempChassis_Type.__name__=_E
_TrfanMesrtempChassis_Object=MibScalar
trfanMesrtempChassis=_TrfanMesrtempChassis_Object((1,3,6,1,4,1,20044,45,3,1,64),_TrfanMesrtempChassis_Type())
trfanMesrtempChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanMesrtempChassis.setStatus(_A)
_TrfancontrolsWrite_ObjectIdentity=ObjectIdentity
trfancontrolsWrite=_TrfancontrolsWrite_ObjectIdentity((1,3,6,1,4,1,20044,45,6))
_TrfanCtrlOther_ObjectIdentity=ObjectIdentity
trfanCtrlOther=_TrfanCtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,45,6,1))
_TrfanCtrlsynth0_ObjectIdentity=ObjectIdentity
trfanCtrlsynth0=_TrfanCtrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,45,6,1,0))
_TrfanCtrlConfLoad_Type=EkiOnOff
_TrfanCtrlConfLoad_Object=MibScalar
trfanCtrlConfLoad=_TrfanCtrlConfLoad_Object((1,3,6,1,4,1,20044,45,6,1,0,1),_TrfanCtrlConfLoad_Type())
trfanCtrlConfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlConfLoad.setStatus(_A)
_TrfanCtrlConfFlash_Type=EkiOnOff
_TrfanCtrlConfFlash_Object=MibScalar
trfanCtrlConfFlash=_TrfanCtrlConfFlash_Object((1,3,6,1,4,1,20044,45,6,1,0,9),_TrfanCtrlConfFlash_Type())
trfanCtrlConfFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlConfFlash.setStatus(_A)
_TrfanCtrlConfClear_Type=EkiOnOff
_TrfanCtrlConfClear_Object=MibScalar
trfanCtrlConfClear=_TrfanCtrlConfClear_Object((1,3,6,1,4,1,20044,45,6,1,0,13),_TrfanCtrlConfClear_Type())
trfanCtrlConfClear.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlConfClear.setStatus(_A)
_TrfanCtrlsynth4_ObjectIdentity=ObjectIdentity
trfanCtrlsynth4=_TrfanCtrlsynth4_ObjectIdentity((1,3,6,1,4,1,20044,45,6,1,4))
_TrfanCtrlCorrelatOn_Type=EkiOnOff
_TrfanCtrlCorrelatOn_Object=MibScalar
trfanCtrlCorrelatOn=_TrfanCtrlCorrelatOn_Object((1,3,6,1,4,1,20044,45,6,1,4,1),_TrfanCtrlCorrelatOn_Type())
trfanCtrlCorrelatOn.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlCorrelatOn.setStatus(_A)
_TrfanCtrlCorrelatOff_Type=EkiOnOff
_TrfanCtrlCorrelatOff_Object=MibScalar
trfanCtrlCorrelatOff=_TrfanCtrlCorrelatOff_Object((1,3,6,1,4,1,20044,45,6,1,4,2),_TrfanCtrlCorrelatOff_Type())
trfanCtrlCorrelatOff.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlCorrelatOff.setStatus(_A)
_TrfanCtrlswMgnt_ObjectIdentity=ObjectIdentity
trfanCtrlswMgnt=_TrfanCtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,45,6,1,5))
_TrfanCtrlColdReset_Type=EkiOnOff
_TrfanCtrlColdReset_Object=MibScalar
trfanCtrlColdReset=_TrfanCtrlColdReset_Object((1,3,6,1,4,1,20044,45,6,1,5,2),_TrfanCtrlColdReset_Type())
trfanCtrlColdReset.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlColdReset.setStatus(_A)
_TrfanCtrlWarmReset_Type=EkiOnOff
_TrfanCtrlWarmReset_Object=MibScalar
trfanCtrlWarmReset=_TrfanCtrlWarmReset_Object((1,3,6,1,4,1,20044,45,6,1,5,3),_TrfanCtrlWarmReset_Type())
trfanCtrlWarmReset.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlWarmReset.setStatus(_A)
_TrfanCtrlledTest_ObjectIdentity=ObjectIdentity
trfanCtrlledTest=_TrfanCtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,45,6,1,64))
_TrfanCtrlGreenLed_Type=EkiOnOff
_TrfanCtrlGreenLed_Object=MibScalar
trfanCtrlGreenLed=_TrfanCtrlGreenLed_Object((1,3,6,1,4,1,20044,45,6,1,64,1),_TrfanCtrlGreenLed_Type())
trfanCtrlGreenLed.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlGreenLed.setStatus(_A)
_TrfanCtrlRedLed_Type=EkiOnOff
_TrfanCtrlRedLed_Object=MibScalar
trfanCtrlRedLed=_TrfanCtrlRedLed_Object((1,3,6,1,4,1,20044,45,6,1,64,2),_TrfanCtrlRedLed_Type())
trfanCtrlRedLed.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlRedLed.setStatus(_A)
_TrfanCtrlLedOff_Type=EkiOnOff
_TrfanCtrlLedOff_Object=MibScalar
trfanCtrlLedOff=_TrfanCtrlLedOff_Object((1,3,6,1,4,1,20044,45,6,1,64,3),_TrfanCtrlLedOff_Type())
trfanCtrlLedOff.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlLedOff.setStatus(_A)
_TrfanCtrlacknowledgeActiv_ObjectIdentity=ObjectIdentity
trfanCtrlacknowledgeActiv=_TrfanCtrlacknowledgeActiv_ObjectIdentity((1,3,6,1,4,1,20044,45,6,1,65))
_TrfanCtrlAckActiv_Type=EkiOnOff
_TrfanCtrlAckActiv_Object=MibScalar
trfanCtrlAckActiv=_TrfanCtrlAckActiv_Object((1,3,6,1,4,1,20044,45,6,1,65,1),_TrfanCtrlAckActiv_Type())
trfanCtrlAckActiv.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCtrlAckActiv.setStatus(_A)
_Trfanri_ObjectIdentity=ObjectIdentity
trfanri=_Trfanri_ObjectIdentity((1,3,6,1,4,1,20044,45,7))
_TrfanriTable_ObjectIdentity=ObjectIdentity
trfanriTable=_TrfanriTable_ObjectIdentity((1,3,6,1,4,1,20044,45,7,1))
_TrfanRinvReloadInventory_Type=EkiOnOff
_TrfanRinvReloadInventory_Object=MibScalar
trfanRinvReloadInventory=_TrfanRinvReloadInventory_Object((1,3,6,1,4,1,20044,45,7,2),_TrfanRinvReloadInventory_Type())
trfanRinvReloadInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanRinvReloadInventory.setStatus(_A)
_TrfanRinvHwPlatform_Type=DisplayString
_TrfanRinvHwPlatform_Object=MibScalar
trfanRinvHwPlatform=_TrfanRinvHwPlatform_Object((1,3,6,1,4,1,20044,45,7,3),_TrfanRinvHwPlatform_Type())
trfanRinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanRinvHwPlatform.setStatus(_A)
_TrfanRinvModulePlatform_Type=DisplayString
_TrfanRinvModulePlatform_Object=MibScalar
trfanRinvModulePlatform=_TrfanRinvModulePlatform_Object((1,3,6,1,4,1,20044,45,7,4),_TrfanRinvModulePlatform_Type())
trfanRinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanRinvModulePlatform.setStatus(_A)
_TrfanRinvSwPlatform_Type=DisplayString
_TrfanRinvSwPlatform_Object=MibScalar
trfanRinvSwPlatform=_TrfanRinvSwPlatform_Object((1,3,6,1,4,1,20044,45,7,5),_TrfanRinvSwPlatform_Type())
trfanRinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:trfanRinvSwPlatform.setStatus(_A)
_TrfanConfig_ObjectIdentity=ObjectIdentity
trfanConfig=_TrfanConfig_ObjectIdentity((1,3,6,1,4,1,20044,45,9))
_TrfanCfgLsd_ObjectIdentity=ObjectIdentity
trfanCfgLsd=_TrfanCfgLsd_ObjectIdentity((1,3,6,1,4,1,20044,45,9,1))
_TrfanCfgStartUp_ObjectIdentity=ObjectIdentity
trfanCfgStartUp=_TrfanCfgStartUp_ObjectIdentity((1,3,6,1,4,1,20044,45,9,2))
_Trfantableother_ObjectIdentity=ObjectIdentity
trfantableother=_Trfantableother_ObjectIdentity((1,3,6,1,4,1,20044,45,9,2,1))
class _TrfanCfglowspeedThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_TrfanCfglowspeedThresh_Type.__name__=_E
_TrfanCfglowspeedThresh_Object=MibScalar
trfanCfglowspeedThresh=_TrfanCfglowspeedThresh_Object((1,3,6,1,4,1,20044,45,9,2,1,2),_TrfanCfglowspeedThresh_Type())
trfanCfglowspeedThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCfglowspeedThresh.setStatus(_A)
class _TrfanCfghighspeedThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_TrfanCfghighspeedThresh_Type.__name__=_E
_TrfanCfghighspeedThresh_Object=MibScalar
trfanCfghighspeedThresh=_TrfanCfghighspeedThresh_Object((1,3,6,1,4,1,20044,45,9,2,1,3),_TrfanCfghighspeedThresh_Type())
trfanCfghighspeedThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCfghighspeedThresh.setStatus(_A)
class _TrfanCfgtrfanMgnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_TrfanCfgtrfanMgnt_Type.__name__=_E
_TrfanCfgtrfanMgnt_Object=MibScalar
trfanCfgtrfanMgnt=_TrfanCfgtrfanMgnt_Object((1,3,6,1,4,1,20044,45,9,2,1,10),_TrfanCfgtrfanMgnt_Type())
trfanCfgtrfanMgnt.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCfgtrfanMgnt.setStatus(_A)
_TrfanCfgLabels_ObjectIdentity=ObjectIdentity
trfanCfgLabels=_TrfanCfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,45,9,3))
_TrfanCfgWriteConfiguration_Type=EkiOnOff
_TrfanCfgWriteConfiguration_Object=MibScalar
trfanCfgWriteConfiguration=_TrfanCfgWriteConfiguration_Object((1,3,6,1,4,1,20044,45,9,257),_TrfanCfgWriteConfiguration_Type())
trfanCfgWriteConfiguration.setMaxAccess(_C)
if mibBuilder.loadTexts:trfanCfgWriteConfiguration.setStatus(_A)
_Trfantraps_ObjectIdentity=ObjectIdentity
trfantraps=_Trfantraps_ObjectIdentity((1,3,6,1,4,1,20044,45,10))
class _TrfantrapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_TrfantrapBoardNumber_Type.__name__=_L
_TrfantrapBoardNumber_Object=MibScalar
trfantrapBoardNumber=_TrfantrapBoardNumber_Object((1,3,6,1,4,1,20044,45,10,2),_TrfantrapBoardNumber_Type())
trfantrapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:trfantrapBoardNumber.setStatus(_A)
trfanPowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,45,10,32))
trfanPowerTrapUrgentGoesOn.setObjects(*((_D,_F),(_D,_G),(_D,_H),(_D,_I)))
if mibBuilder.loadTexts:trfanPowerTrapUrgentGoesOn.setStatus(_A)
trfanPowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,45,10,33))
trfanPowerTrapUrgentGoesOff.setObjects(*((_D,_F),(_D,_G),(_D,_H),(_D,_I)))
if mibBuilder.loadTexts:trfanPowerTrapUrgentGoesOff.setStatus(_A)
trfanPowerTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,45,10,34))
trfanPowerTrapCritGoesOn.setObjects((_D,_J))
if mibBuilder.loadTexts:trfanPowerTrapCritGoesOn.setStatus(_A)
trfanPowerTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,45,10,35))
trfanPowerTrapCritGoesOff.setObjects((_D,_J))
if mibBuilder.loadTexts:trfanPowerTrapCritGoesOff.setStatus(_A)
trfanFanTrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,45,10,44))
trfanFanTrapCritGoesOn.setObjects((_D,_K))
if mibBuilder.loadTexts:trfanFanTrapCritGoesOn.setStatus(_A)
trfanFanTrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,45,10,45))
trfanFanTrapCritGoesOff.setObjects((_D,_K))
if mibBuilder.loadTexts:trfanFanTrapCritGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'moduletrfan':moduletrfan,'trfanalarms':trfanalarms,'trfanAlmOther':trfanAlmOther,'trfanAlmOtherNurg':trfanAlmOtherNurg,'trfanAlmsynthAlm2':trfanAlmsynthAlm2,'trfanAlmConfTableSave':trfanAlmConfTableSave,'trfanAlmInvUpload':trfanAlmInvUpload,'trfanAlmConfTableLoad':trfanAlmConfTableLoad,'trfanAlmCorrelatOff':trfanAlmCorrelatOff,'trfanAlmOtherUrg':trfanAlmOtherUrg,'trfanAlmfilterAlm':trfanAlmfilterAlm,'trfanAlmFilterNotPresent':trfanAlmFilterNotPresent,'trfanAlmfansMgnt':trfanAlmfansMgnt,'trfanAlmFan1Fail':trfanAlmFan1Fail,'trfanAlmFan2Fail':trfanAlmFan2Fail,'trfanAlmFan3Fail':trfanAlmFan3Fail,'trfanAlmFan4Fail':trfanAlmFan4Fail,'trfanAlmFan5Fail':trfanAlmFan5Fail,'trfanAlmFan6Fail':trfanAlmFan6Fail,'trfanAlmFansOff':trfanAlmFansOff,'trfanAlmFanLowSpeed':trfanAlmFanLowSpeed,'trfanAlmpwrMgnt':trfanAlmpwrMgnt,_H:trfanAlmPwr12v1Fail,_I:trfanAlmPwr12v2Fail,'trfanAlmmodInitFailLevel2':trfanAlmmodInitFailLevel2,'trfanAlmRegReadFail':trfanAlmRegReadFail,'trfanAlmResetHwInitFail':trfanAlmResetHwInitFail,'trfanAlmConfReadFail':trfanAlmConfReadFail,'trfanAlmInvReadFail':trfanAlmInvReadFail,'trfanAlmOtherCrit':trfanAlmOtherCrit,'trfanAlmsynthAlm0':trfanAlmsynthAlm0,'trfanAlmModuleGlobFailure':trfanAlmModuleGlobFailure,_F:trfanAlmDefPowerA,_G:trfanAlmDefPowerB,'trfanAlmAcknowledge':trfanAlmAcknowledge,_J:trfanAlmDefFuse,'trfanAlmsynthAlm1':trfanAlmsynthAlm1,_K:trfanAlmFansFailure,'trfanmeasures':trfanmeasures,'trfanMesrOther':trfanMesrOther,'trfanMesrvoltMeas12v1':trfanMesrvoltMeas12v1,'trfanMesrvoltMeas12v2':trfanMesrvoltMeas12v2,'trfanMesrtempChassis':trfanMesrtempChassis,'trfancontrolsWrite':trfancontrolsWrite,'trfanCtrlOther':trfanCtrlOther,'trfanCtrlsynth0':trfanCtrlsynth0,'trfanCtrlConfLoad':trfanCtrlConfLoad,'trfanCtrlConfFlash':trfanCtrlConfFlash,'trfanCtrlConfClear':trfanCtrlConfClear,'trfanCtrlsynth4':trfanCtrlsynth4,'trfanCtrlCorrelatOn':trfanCtrlCorrelatOn,'trfanCtrlCorrelatOff':trfanCtrlCorrelatOff,'trfanCtrlswMgnt':trfanCtrlswMgnt,'trfanCtrlColdReset':trfanCtrlColdReset,'trfanCtrlWarmReset':trfanCtrlWarmReset,'trfanCtrlledTest':trfanCtrlledTest,'trfanCtrlGreenLed':trfanCtrlGreenLed,'trfanCtrlRedLed':trfanCtrlRedLed,'trfanCtrlLedOff':trfanCtrlLedOff,'trfanCtrlacknowledgeActiv':trfanCtrlacknowledgeActiv,'trfanCtrlAckActiv':trfanCtrlAckActiv,'trfanri':trfanri,'trfanriTable':trfanriTable,'trfanRinvReloadInventory':trfanRinvReloadInventory,'trfanRinvHwPlatform':trfanRinvHwPlatform,'trfanRinvModulePlatform':trfanRinvModulePlatform,'trfanRinvSwPlatform':trfanRinvSwPlatform,'trfanConfig':trfanConfig,'trfanCfgLsd':trfanCfgLsd,'trfanCfgStartUp':trfanCfgStartUp,'trfantableother':trfantableother,'trfanCfglowspeedThresh':trfanCfglowspeedThresh,'trfanCfghighspeedThresh':trfanCfghighspeedThresh,'trfanCfgtrfanMgnt':trfanCfgtrfanMgnt,'trfanCfgLabels':trfanCfgLabels,'trfanCfgWriteConfiguration':trfanCfgWriteConfiguration,'trfantraps':trfantraps,'trfantrapBoardNumber':trfantrapBoardNumber,'trfanPowerTrapUrgentGoesOn':trfanPowerTrapUrgentGoesOn,'trfanPowerTrapUrgentGoesOff':trfanPowerTrapUrgentGoesOff,'trfanPowerTrapCritGoesOn':trfanPowerTrapCritGoesOn,'trfanPowerTrapCritGoesOff':trfanPowerTrapCritGoesOff,'trfanFanTrapCritGoesOn':trfanFanTrapCritGoesOn,'trfanFanTrapCritGoesOff':trfanFanTrapCritGoesOff})