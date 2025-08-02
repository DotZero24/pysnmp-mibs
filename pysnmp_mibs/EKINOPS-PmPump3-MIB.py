_V='pmpump3CfgLabellineIndex'
_U='pmpump3CfgLabelclientIndex'
_T='pmpump3RinvLaser2Index'
_S='pmpump3RinvLaser1Index'
_R='pmpump3AlmDefFuseA'
_Q='pmpump3AlmDefFuseB'
_P='pmpump3AlmLaser1HwFail'
_O='pmpump3AlmLaser1Fail'
_N='pmpump3AlmLaser1Alm'
_M='pmpump3AlmLaser1Warning'
_L='pmpump3AlmLaser2HwFail'
_K='pmpump3AlmLaser2Fail'
_J='pmpump3AlmLaser2Alm'
_I='pmpump3AlmLaser2Warning'
_H='DisplayString'
_G='Unsigned32'
_F='pmpump3trapBoardNumber'
_E='Integer32'
_D='read-write'
_C='EKINOPS-PmPump3-MIB'
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
modulepmpump3=ModuleIdentity((1,3,6,1,4,1,20044,49))
if mibBuilder.loadTexts:modulepmpump3.setRevisions(('2010-09-01 00:00','2010-12-15 00:00','2011-09-20 00:00','2012-07-04 00:00','2014-03-26 00:00','2014-11-25 00:00','2016-05-23 00:00'))
_Pmpump3alarms_ObjectIdentity=ObjectIdentity
pmpump3alarms=_Pmpump3alarms_ObjectIdentity((1,3,6,1,4,1,20044,49,2))
_Pmpump3AlmOther_ObjectIdentity=ObjectIdentity
pmpump3AlmOther=_Pmpump3AlmOther_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1))
_Pmpump3AlmOtherNurg_ObjectIdentity=ObjectIdentity
pmpump3AlmOtherNurg=_Pmpump3AlmOtherNurg_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,1))
_Pmpump3AlmsynthAlm2_ObjectIdentity=ObjectIdentity
pmpump3AlmsynthAlm2=_Pmpump3AlmsynthAlm2_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,1,2))
_Pmpump3AlmConfTableSave_Type=EkiOnOff
_Pmpump3AlmConfTableSave_Object=MibScalar
pmpump3AlmConfTableSave=_Pmpump3AlmConfTableSave_Object((1,3,6,1,4,1,20044,49,2,1,1,2,1),_Pmpump3AlmConfTableSave_Type())
pmpump3AlmConfTableSave.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmConfTableSave.setStatus(_A)
_Pmpump3AlmInvUpload_Type=EkiOnOff
_Pmpump3AlmInvUpload_Object=MibScalar
pmpump3AlmInvUpload=_Pmpump3AlmInvUpload_Object((1,3,6,1,4,1,20044,49,2,1,1,2,2),_Pmpump3AlmInvUpload_Type())
pmpump3AlmInvUpload.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmInvUpload.setStatus(_A)
_Pmpump3AlmConfTableLoad_Type=EkiOnOff
_Pmpump3AlmConfTableLoad_Object=MibScalar
pmpump3AlmConfTableLoad=_Pmpump3AlmConfTableLoad_Object((1,3,6,1,4,1,20044,49,2,1,1,2,3),_Pmpump3AlmConfTableLoad_Type())
pmpump3AlmConfTableLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmConfTableLoad.setStatus(_A)
_Pmpump3AlmpmWarnings_ObjectIdentity=ObjectIdentity
pmpump3AlmpmWarnings=_Pmpump3AlmpmWarnings_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,1,75))
_Pmpump3AlmTermpLowWarning_Type=EkiOnOff
_Pmpump3AlmTermpLowWarning_Object=MibScalar
pmpump3AlmTermpLowWarning=_Pmpump3AlmTermpLowWarning_Object((1,3,6,1,4,1,20044,49,2,1,1,75,1),_Pmpump3AlmTermpLowWarning_Type())
pmpump3AlmTermpLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmTermpLowWarning.setStatus(_A)
_Pmpump3AlmTempHighWarning_Type=EkiOnOff
_Pmpump3AlmTempHighWarning_Object=MibScalar
pmpump3AlmTempHighWarning=_Pmpump3AlmTempHighWarning_Object((1,3,6,1,4,1,20044,49,2,1,1,75,2),_Pmpump3AlmTempHighWarning_Type())
pmpump3AlmTempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmTempHighWarning.setStatus(_A)
_Pmpump3AlmOtherUrg_ObjectIdentity=ObjectIdentity
pmpump3AlmOtherUrg=_Pmpump3AlmOtherUrg_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,2))
_Pmpump3AlmpmAlarms_ObjectIdentity=ObjectIdentity
pmpump3AlmpmAlarms=_Pmpump3AlmpmAlarms_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,2,74))
_Pmpump3AlmTermpLowAlarm_Type=EkiOnOff
_Pmpump3AlmTermpLowAlarm_Object=MibScalar
pmpump3AlmTermpLowAlarm=_Pmpump3AlmTermpLowAlarm_Object((1,3,6,1,4,1,20044,49,2,1,2,74,1),_Pmpump3AlmTermpLowAlarm_Type())
pmpump3AlmTermpLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmTermpLowAlarm.setStatus(_A)
_Pmpump3AlmTempHighAlarm_Type=EkiOnOff
_Pmpump3AlmTempHighAlarm_Object=MibScalar
pmpump3AlmTempHighAlarm=_Pmpump3AlmTempHighAlarm_Object((1,3,6,1,4,1,20044,49,2,1,2,74,2),_Pmpump3AlmTempHighAlarm_Type())
pmpump3AlmTempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmTempHighAlarm.setStatus(_A)
_Pmpump3AlmOtherCrit_ObjectIdentity=ObjectIdentity
pmpump3AlmOtherCrit=_Pmpump3AlmOtherCrit_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,3))
_Pmpump3AlmsynthAlm0_ObjectIdentity=ObjectIdentity
pmpump3AlmsynthAlm0=_Pmpump3AlmsynthAlm0_ObjectIdentity((1,3,6,1,4,1,20044,49,2,1,3,0))
_Pmpump3AlmModGlobFail_Type=EkiOnOff
_Pmpump3AlmModGlobFail_Object=MibScalar
pmpump3AlmModGlobFail=_Pmpump3AlmModGlobFail_Object((1,3,6,1,4,1,20044,49,2,1,3,0,9),_Pmpump3AlmModGlobFail_Type())
pmpump3AlmModGlobFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmModGlobFail.setStatus(_A)
_Pmpump3AlmDefFuseA_Type=EkiOnOff
_Pmpump3AlmDefFuseA_Object=MibScalar
pmpump3AlmDefFuseA=_Pmpump3AlmDefFuseA_Object((1,3,6,1,4,1,20044,49,2,1,3,0,15),_Pmpump3AlmDefFuseA_Type())
pmpump3AlmDefFuseA.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmDefFuseA.setStatus(_A)
_Pmpump3AlmDefFuseB_Type=EkiOnOff
_Pmpump3AlmDefFuseB_Object=MibScalar
pmpump3AlmDefFuseB=_Pmpump3AlmDefFuseB_Object((1,3,6,1,4,1,20044,49,2,1,3,0,16),_Pmpump3AlmDefFuseB_Type())
pmpump3AlmDefFuseB.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmDefFuseB.setStatus(_A)
_Pmpump3AlmClient_ObjectIdentity=ObjectIdentity
pmpump3AlmClient=_Pmpump3AlmClient_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2))
_Pmpump3AlmClientNurg_ObjectIdentity=ObjectIdentity
pmpump3AlmClientNurg=_Pmpump3AlmClientNurg_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,1))
_Pmpump3Almlaser1Warnings_ObjectIdentity=ObjectIdentity
pmpump3Almlaser1Warnings=_Pmpump3Almlaser1Warnings_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,1,17))
_Pmpump3AlmLaser1TempLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser1TempLowWarning_Object=MibScalar
pmpump3AlmLaser1TempLowWarning=_Pmpump3AlmLaser1TempLowWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,1),_Pmpump3AlmLaser1TempLowWarning_Type())
pmpump3AlmLaser1TempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1TempLowWarning.setStatus(_A)
_Pmpump3AlmLaser1TempHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser1TempHighWarning_Object=MibScalar
pmpump3AlmLaser1TempHighWarning=_Pmpump3AlmLaser1TempHighWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,2),_Pmpump3AlmLaser1TempHighWarning_Type())
pmpump3AlmLaser1TempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1TempHighWarning.setStatus(_A)
_Pmpump3AlmLaser1VthLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser1VthLowWarning_Object=MibScalar
pmpump3AlmLaser1VthLowWarning=_Pmpump3AlmLaser1VthLowWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,3),_Pmpump3AlmLaser1VthLowWarning_Type())
pmpump3AlmLaser1VthLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1VthLowWarning.setStatus(_A)
_Pmpump3AlmLaser1VthHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser1VthHighWarning_Object=MibScalar
pmpump3AlmLaser1VthHighWarning=_Pmpump3AlmLaser1VthHighWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,4),_Pmpump3AlmLaser1VthHighWarning_Type())
pmpump3AlmLaser1VthHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1VthHighWarning.setStatus(_A)
_Pmpump3AlmLaser1OutputPwrLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser1OutputPwrLowWarning_Object=MibScalar
pmpump3AlmLaser1OutputPwrLowWarning=_Pmpump3AlmLaser1OutputPwrLowWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,5),_Pmpump3AlmLaser1OutputPwrLowWarning_Type())
pmpump3AlmLaser1OutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1OutputPwrLowWarning.setStatus(_A)
_Pmpump3AlmLaser1OutputPwrHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser1OutputPwrHighWarning_Object=MibScalar
pmpump3AlmLaser1OutputPwrHighWarning=_Pmpump3AlmLaser1OutputPwrHighWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,6),_Pmpump3AlmLaser1OutputPwrHighWarning_Type())
pmpump3AlmLaser1OutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1OutputPwrHighWarning.setStatus(_A)
_Pmpump3AlmLaser1BiasLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser1BiasLowWarning_Object=MibScalar
pmpump3AlmLaser1BiasLowWarning=_Pmpump3AlmLaser1BiasLowWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,7),_Pmpump3AlmLaser1BiasLowWarning_Type())
pmpump3AlmLaser1BiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1BiasLowWarning.setStatus(_A)
_Pmpump3AlmLaser1BiasHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser1BiasHighWarning_Object=MibScalar
pmpump3AlmLaser1BiasHighWarning=_Pmpump3AlmLaser1BiasHighWarning_Object((1,3,6,1,4,1,20044,49,2,2,1,17,8),_Pmpump3AlmLaser1BiasHighWarning_Type())
pmpump3AlmLaser1BiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1BiasHighWarning.setStatus(_A)
_Pmpump3AlmClientUrg_ObjectIdentity=ObjectIdentity
pmpump3AlmClientUrg=_Pmpump3AlmClientUrg_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,2))
_Pmpump3Almlaser1Alarms1_ObjectIdentity=ObjectIdentity
pmpump3Almlaser1Alarms1=_Pmpump3Almlaser1Alarms1_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,2,16))
_Pmpump3AlmLaser1TempLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1TempLowAlarm_Object=MibScalar
pmpump3AlmLaser1TempLowAlarm=_Pmpump3AlmLaser1TempLowAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,1),_Pmpump3AlmLaser1TempLowAlarm_Type())
pmpump3AlmLaser1TempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1TempLowAlarm.setStatus(_A)
_Pmpump3AlmLaser1TempHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1TempHighAlarm_Object=MibScalar
pmpump3AlmLaser1TempHighAlarm=_Pmpump3AlmLaser1TempHighAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,2),_Pmpump3AlmLaser1TempHighAlarm_Type())
pmpump3AlmLaser1TempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1TempHighAlarm.setStatus(_A)
_Pmpump3AlmLaser1VthLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1VthLowAlarm_Object=MibScalar
pmpump3AlmLaser1VthLowAlarm=_Pmpump3AlmLaser1VthLowAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,3),_Pmpump3AlmLaser1VthLowAlarm_Type())
pmpump3AlmLaser1VthLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1VthLowAlarm.setStatus(_A)
_Pmpump3AlmLaser1VthHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1VthHighAlarm_Object=MibScalar
pmpump3AlmLaser1VthHighAlarm=_Pmpump3AlmLaser1VthHighAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,4),_Pmpump3AlmLaser1VthHighAlarm_Type())
pmpump3AlmLaser1VthHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1VthHighAlarm.setStatus(_A)
_Pmpump3AlmLaser1OutputPwrLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1OutputPwrLowAlarm_Object=MibScalar
pmpump3AlmLaser1OutputPwrLowAlarm=_Pmpump3AlmLaser1OutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,5),_Pmpump3AlmLaser1OutputPwrLowAlarm_Type())
pmpump3AlmLaser1OutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1OutputPwrLowAlarm.setStatus(_A)
_Pmpump3AlmLaser1OutputPwrHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1OutputPwrHighAlarm_Object=MibScalar
pmpump3AlmLaser1OutputPwrHighAlarm=_Pmpump3AlmLaser1OutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,6),_Pmpump3AlmLaser1OutputPwrHighAlarm_Type())
pmpump3AlmLaser1OutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1OutputPwrHighAlarm.setStatus(_A)
_Pmpump3AlmLaser1BiasLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1BiasLowAlarm_Object=MibScalar
pmpump3AlmLaser1BiasLowAlarm=_Pmpump3AlmLaser1BiasLowAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,7),_Pmpump3AlmLaser1BiasLowAlarm_Type())
pmpump3AlmLaser1BiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1BiasLowAlarm.setStatus(_A)
_Pmpump3AlmLaser1BiasHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser1BiasHighAlarm_Object=MibScalar
pmpump3AlmLaser1BiasHighAlarm=_Pmpump3AlmLaser1BiasHighAlarm_Object((1,3,6,1,4,1,20044,49,2,2,2,16,8),_Pmpump3AlmLaser1BiasHighAlarm_Type())
pmpump3AlmLaser1BiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1BiasHighAlarm.setStatus(_A)
_Pmpump3AlmClientCrit_ObjectIdentity=ObjectIdentity
pmpump3AlmClientCrit=_Pmpump3AlmClientCrit_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,3))
_Pmpump3AlmsynthAlmLaser1_ObjectIdentity=ObjectIdentity
pmpump3AlmsynthAlmLaser1=_Pmpump3AlmsynthAlmLaser1_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,3,8))
_Pmpump3AlmLaser1InitNotCompl_Type=EkiOnOff
_Pmpump3AlmLaser1InitNotCompl_Object=MibScalar
pmpump3AlmLaser1InitNotCompl=_Pmpump3AlmLaser1InitNotCompl_Object((1,3,6,1,4,1,20044,49,2,2,3,8,2),_Pmpump3AlmLaser1InitNotCompl_Type())
pmpump3AlmLaser1InitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1InitNotCompl.setStatus(_A)
_Pmpump3AlmLaser1HwFail_Type=EkiOnOff
_Pmpump3AlmLaser1HwFail_Object=MibScalar
pmpump3AlmLaser1HwFail=_Pmpump3AlmLaser1HwFail_Object((1,3,6,1,4,1,20044,49,2,2,3,8,4),_Pmpump3AlmLaser1HwFail_Type())
pmpump3AlmLaser1HwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1HwFail.setStatus(_A)
_Pmpump3AlmLaser1TxOff_Type=EkiOnOff
_Pmpump3AlmLaser1TxOff_Object=MibScalar
pmpump3AlmLaser1TxOff=_Pmpump3AlmLaser1TxOff_Object((1,3,6,1,4,1,20044,49,2,2,3,8,5),_Pmpump3AlmLaser1TxOff_Type())
pmpump3AlmLaser1TxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1TxOff.setStatus(_A)
_Pmpump3AlmLaser1Oos_Type=EkiOnOff
_Pmpump3AlmLaser1Oos_Object=MibScalar
pmpump3AlmLaser1Oos=_Pmpump3AlmLaser1Oos_Object((1,3,6,1,4,1,20044,49,2,2,3,8,6),_Pmpump3AlmLaser1Oos_Type())
pmpump3AlmLaser1Oos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1Oos.setStatus(_A)
_Pmpump3AlmLaser1Warning_Type=EkiOnOff
_Pmpump3AlmLaser1Warning_Object=MibScalar
pmpump3AlmLaser1Warning=_Pmpump3AlmLaser1Warning_Object((1,3,6,1,4,1,20044,49,2,2,3,8,9),_Pmpump3AlmLaser1Warning_Type())
pmpump3AlmLaser1Warning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1Warning.setStatus(_A)
_Pmpump3AlmLaser1Alm_Type=EkiOnOff
_Pmpump3AlmLaser1Alm_Object=MibScalar
pmpump3AlmLaser1Alm=_Pmpump3AlmLaser1Alm_Object((1,3,6,1,4,1,20044,49,2,2,3,8,10),_Pmpump3AlmLaser1Alm_Type())
pmpump3AlmLaser1Alm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1Alm.setStatus(_A)
_Pmpump3AlmLaser1Fail_Type=EkiOnOff
_Pmpump3AlmLaser1Fail_Object=MibScalar
pmpump3AlmLaser1Fail=_Pmpump3AlmLaser1Fail_Object((1,3,6,1,4,1,20044,49,2,2,3,8,12),_Pmpump3AlmLaser1Fail_Type())
pmpump3AlmLaser1Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1Fail.setStatus(_A)
_Pmpump3AlmsynthAlmLaser2_ObjectIdentity=ObjectIdentity
pmpump3AlmsynthAlmLaser2=_Pmpump3AlmsynthAlmLaser2_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,3,9))
_Pmpump3AlmLaser2InitNotCompl_Type=EkiOnOff
_Pmpump3AlmLaser2InitNotCompl_Object=MibScalar
pmpump3AlmLaser2InitNotCompl=_Pmpump3AlmLaser2InitNotCompl_Object((1,3,6,1,4,1,20044,49,2,2,3,9,2),_Pmpump3AlmLaser2InitNotCompl_Type())
pmpump3AlmLaser2InitNotCompl.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2InitNotCompl.setStatus(_A)
_Pmpump3AlmLaser2HwFail_Type=EkiOnOff
_Pmpump3AlmLaser2HwFail_Object=MibScalar
pmpump3AlmLaser2HwFail=_Pmpump3AlmLaser2HwFail_Object((1,3,6,1,4,1,20044,49,2,2,3,9,4),_Pmpump3AlmLaser2HwFail_Type())
pmpump3AlmLaser2HwFail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2HwFail.setStatus(_A)
_Pmpump3AlmLaser2TxOff_Type=EkiOnOff
_Pmpump3AlmLaser2TxOff_Object=MibScalar
pmpump3AlmLaser2TxOff=_Pmpump3AlmLaser2TxOff_Object((1,3,6,1,4,1,20044,49,2,2,3,9,5),_Pmpump3AlmLaser2TxOff_Type())
pmpump3AlmLaser2TxOff.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2TxOff.setStatus(_A)
_Pmpump3AlmLaser2Oos_Type=EkiOnOff
_Pmpump3AlmLaser2Oos_Object=MibScalar
pmpump3AlmLaser2Oos=_Pmpump3AlmLaser2Oos_Object((1,3,6,1,4,1,20044,49,2,2,3,9,6),_Pmpump3AlmLaser2Oos_Type())
pmpump3AlmLaser2Oos.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2Oos.setStatus(_A)
_Pmpump3AlmLaser2Warning_Type=EkiOnOff
_Pmpump3AlmLaser2Warning_Object=MibScalar
pmpump3AlmLaser2Warning=_Pmpump3AlmLaser2Warning_Object((1,3,6,1,4,1,20044,49,2,2,3,9,9),_Pmpump3AlmLaser2Warning_Type())
pmpump3AlmLaser2Warning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2Warning.setStatus(_A)
_Pmpump3AlmLaser2Alm_Type=EkiOnOff
_Pmpump3AlmLaser2Alm_Object=MibScalar
pmpump3AlmLaser2Alm=_Pmpump3AlmLaser2Alm_Object((1,3,6,1,4,1,20044,49,2,2,3,9,10),_Pmpump3AlmLaser2Alm_Type())
pmpump3AlmLaser2Alm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2Alm.setStatus(_A)
_Pmpump3AlmLaser2Fail_Type=EkiOnOff
_Pmpump3AlmLaser2Fail_Object=MibScalar
pmpump3AlmLaser2Fail=_Pmpump3AlmLaser2Fail_Object((1,3,6,1,4,1,20044,49,2,2,3,9,12),_Pmpump3AlmLaser2Fail_Type())
pmpump3AlmLaser2Fail.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2Fail.setStatus(_A)
_Pmpump3Almlaser1Alarms2_ObjectIdentity=ObjectIdentity
pmpump3Almlaser1Alarms2=_Pmpump3Almlaser1Alarms2_ObjectIdentity((1,3,6,1,4,1,20044,49,2,2,3,19))
_Pmpump3AlmLaser1AlmCurrent_Type=EkiOnOff
_Pmpump3AlmLaser1AlmCurrent_Object=MibScalar
pmpump3AlmLaser1AlmCurrent=_Pmpump3AlmLaser1AlmCurrent_Object((1,3,6,1,4,1,20044,49,2,2,3,19,1),_Pmpump3AlmLaser1AlmCurrent_Type())
pmpump3AlmLaser1AlmCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1AlmCurrent.setStatus(_A)
_Pmpump3AlmLaser1AlmTemp_Type=EkiOnOff
_Pmpump3AlmLaser1AlmTemp_Object=MibScalar
pmpump3AlmLaser1AlmTemp=_Pmpump3AlmLaser1AlmTemp_Object((1,3,6,1,4,1,20044,49,2,2,3,19,2),_Pmpump3AlmLaser1AlmTemp_Type())
pmpump3AlmLaser1AlmTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1AlmTemp.setStatus(_A)
_Pmpump3AlmLaser1AlmTecPower_Type=EkiOnOff
_Pmpump3AlmLaser1AlmTecPower_Object=MibScalar
pmpump3AlmLaser1AlmTecPower=_Pmpump3AlmLaser1AlmTecPower_Object((1,3,6,1,4,1,20044,49,2,2,3,19,3),_Pmpump3AlmLaser1AlmTecPower_Type())
pmpump3AlmLaser1AlmTecPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1AlmTecPower.setStatus(_A)
_Pmpump3AlmLaser1AlmTecDev_Type=EkiOnOff
_Pmpump3AlmLaser1AlmTecDev_Object=MibScalar
pmpump3AlmLaser1AlmTecDev=_Pmpump3AlmLaser1AlmTecDev_Object((1,3,6,1,4,1,20044,49,2,2,3,19,4),_Pmpump3AlmLaser1AlmTecDev_Type())
pmpump3AlmLaser1AlmTecDev.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1AlmTecDev.setStatus(_A)
_Pmpump3AlmLaser1OaDisconnectedLsd_Type=EkiOnOff
_Pmpump3AlmLaser1OaDisconnectedLsd_Object=MibScalar
pmpump3AlmLaser1OaDisconnectedLsd=_Pmpump3AlmLaser1OaDisconnectedLsd_Object((1,3,6,1,4,1,20044,49,2,2,3,19,5),_Pmpump3AlmLaser1OaDisconnectedLsd_Type())
pmpump3AlmLaser1OaDisconnectedLsd.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1OaDisconnectedLsd.setStatus(_A)
_Pmpump3AlmLaser1ExtLsd_Type=EkiOnOff
_Pmpump3AlmLaser1ExtLsd_Object=MibScalar
pmpump3AlmLaser1ExtLsd=_Pmpump3AlmLaser1ExtLsd_Object((1,3,6,1,4,1,20044,49,2,2,3,19,6),_Pmpump3AlmLaser1ExtLsd_Type())
pmpump3AlmLaser1ExtLsd.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser1ExtLsd.setStatus(_A)
_Pmpump3AlmLine_ObjectIdentity=ObjectIdentity
pmpump3AlmLine=_Pmpump3AlmLine_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3))
_Pmpump3AlmLineNurg_ObjectIdentity=ObjectIdentity
pmpump3AlmLineNurg=_Pmpump3AlmLineNurg_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3,1))
_Pmpump3Almlaser2Warnings_ObjectIdentity=ObjectIdentity
pmpump3Almlaser2Warnings=_Pmpump3Almlaser2Warnings_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3,1,25))
_Pmpump3AlmLaser2TempLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser2TempLowWarning_Object=MibScalar
pmpump3AlmLaser2TempLowWarning=_Pmpump3AlmLaser2TempLowWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,1),_Pmpump3AlmLaser2TempLowWarning_Type())
pmpump3AlmLaser2TempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2TempLowWarning.setStatus(_A)
_Pmpump3AlmLaser2TempHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser2TempHighWarning_Object=MibScalar
pmpump3AlmLaser2TempHighWarning=_Pmpump3AlmLaser2TempHighWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,2),_Pmpump3AlmLaser2TempHighWarning_Type())
pmpump3AlmLaser2TempHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2TempHighWarning.setStatus(_A)
_Pmpump3AlmLaser2VthLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser2VthLowWarning_Object=MibScalar
pmpump3AlmLaser2VthLowWarning=_Pmpump3AlmLaser2VthLowWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,3),_Pmpump3AlmLaser2VthLowWarning_Type())
pmpump3AlmLaser2VthLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2VthLowWarning.setStatus(_A)
_Pmpump3AlmLaser2VthHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser2VthHighWarning_Object=MibScalar
pmpump3AlmLaser2VthHighWarning=_Pmpump3AlmLaser2VthHighWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,4),_Pmpump3AlmLaser2VthHighWarning_Type())
pmpump3AlmLaser2VthHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2VthHighWarning.setStatus(_A)
_Pmpump3AlmLaser2OutputPwrLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser2OutputPwrLowWarning_Object=MibScalar
pmpump3AlmLaser2OutputPwrLowWarning=_Pmpump3AlmLaser2OutputPwrLowWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,5),_Pmpump3AlmLaser2OutputPwrLowWarning_Type())
pmpump3AlmLaser2OutputPwrLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2OutputPwrLowWarning.setStatus(_A)
_Pmpump3AlmLaser2OutputPwrHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser2OutputPwrHighWarning_Object=MibScalar
pmpump3AlmLaser2OutputPwrHighWarning=_Pmpump3AlmLaser2OutputPwrHighWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,6),_Pmpump3AlmLaser2OutputPwrHighWarning_Type())
pmpump3AlmLaser2OutputPwrHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2OutputPwrHighWarning.setStatus(_A)
_Pmpump3AlmLaser2BiasLowWarning_Type=EkiOnOff
_Pmpump3AlmLaser2BiasLowWarning_Object=MibScalar
pmpump3AlmLaser2BiasLowWarning=_Pmpump3AlmLaser2BiasLowWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,7),_Pmpump3AlmLaser2BiasLowWarning_Type())
pmpump3AlmLaser2BiasLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2BiasLowWarning.setStatus(_A)
_Pmpump3AlmLaser2BiasHighWarning_Type=EkiOnOff
_Pmpump3AlmLaser2BiasHighWarning_Object=MibScalar
pmpump3AlmLaser2BiasHighWarning=_Pmpump3AlmLaser2BiasHighWarning_Object((1,3,6,1,4,1,20044,49,2,3,1,25,8),_Pmpump3AlmLaser2BiasHighWarning_Type())
pmpump3AlmLaser2BiasHighWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2BiasHighWarning.setStatus(_A)
_Pmpump3AlmLineUrg_ObjectIdentity=ObjectIdentity
pmpump3AlmLineUrg=_Pmpump3AlmLineUrg_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3,2))
_Pmpump3Almlaser2Alarms1_ObjectIdentity=ObjectIdentity
pmpump3Almlaser2Alarms1=_Pmpump3Almlaser2Alarms1_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3,2,24))
_Pmpump3AlmLaser2TempLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2TempLowAlarm_Object=MibScalar
pmpump3AlmLaser2TempLowAlarm=_Pmpump3AlmLaser2TempLowAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,1),_Pmpump3AlmLaser2TempLowAlarm_Type())
pmpump3AlmLaser2TempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2TempLowAlarm.setStatus(_A)
_Pmpump3AlmLaser2TempHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2TempHighAlarm_Object=MibScalar
pmpump3AlmLaser2TempHighAlarm=_Pmpump3AlmLaser2TempHighAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,2),_Pmpump3AlmLaser2TempHighAlarm_Type())
pmpump3AlmLaser2TempHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2TempHighAlarm.setStatus(_A)
_Pmpump3AlmLaser2VthLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2VthLowAlarm_Object=MibScalar
pmpump3AlmLaser2VthLowAlarm=_Pmpump3AlmLaser2VthLowAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,3),_Pmpump3AlmLaser2VthLowAlarm_Type())
pmpump3AlmLaser2VthLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2VthLowAlarm.setStatus(_A)
_Pmpump3AlmLaser2VthHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2VthHighAlarm_Object=MibScalar
pmpump3AlmLaser2VthHighAlarm=_Pmpump3AlmLaser2VthHighAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,4),_Pmpump3AlmLaser2VthHighAlarm_Type())
pmpump3AlmLaser2VthHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2VthHighAlarm.setStatus(_A)
_Pmpump3AlmLaser2OutputPwrLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2OutputPwrLowAlarm_Object=MibScalar
pmpump3AlmLaser2OutputPwrLowAlarm=_Pmpump3AlmLaser2OutputPwrLowAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,5),_Pmpump3AlmLaser2OutputPwrLowAlarm_Type())
pmpump3AlmLaser2OutputPwrLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2OutputPwrLowAlarm.setStatus(_A)
_Pmpump3AlmLaser2OutputPwrHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2OutputPwrHighAlarm_Object=MibScalar
pmpump3AlmLaser2OutputPwrHighAlarm=_Pmpump3AlmLaser2OutputPwrHighAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,6),_Pmpump3AlmLaser2OutputPwrHighAlarm_Type())
pmpump3AlmLaser2OutputPwrHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2OutputPwrHighAlarm.setStatus(_A)
_Pmpump3AlmLaser2BiasLowAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2BiasLowAlarm_Object=MibScalar
pmpump3AlmLaser2BiasLowAlarm=_Pmpump3AlmLaser2BiasLowAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,7),_Pmpump3AlmLaser2BiasLowAlarm_Type())
pmpump3AlmLaser2BiasLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2BiasLowAlarm.setStatus(_A)
_Pmpump3AlmLaser2BiasHighAlarm_Type=EkiOnOff
_Pmpump3AlmLaser2BiasHighAlarm_Object=MibScalar
pmpump3AlmLaser2BiasHighAlarm=_Pmpump3AlmLaser2BiasHighAlarm_Object((1,3,6,1,4,1,20044,49,2,3,2,24,8),_Pmpump3AlmLaser2BiasHighAlarm_Type())
pmpump3AlmLaser2BiasHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2BiasHighAlarm.setStatus(_A)
_Pmpump3AlmLineCrit_ObjectIdentity=ObjectIdentity
pmpump3AlmLineCrit=_Pmpump3AlmLineCrit_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3,3))
_Pmpump3Almlaser2Alarms2_ObjectIdentity=ObjectIdentity
pmpump3Almlaser2Alarms2=_Pmpump3Almlaser2Alarms2_ObjectIdentity((1,3,6,1,4,1,20044,49,2,3,3,27))
_Pmpump3AlmLaser2AlmCurrent_Type=EkiOnOff
_Pmpump3AlmLaser2AlmCurrent_Object=MibScalar
pmpump3AlmLaser2AlmCurrent=_Pmpump3AlmLaser2AlmCurrent_Object((1,3,6,1,4,1,20044,49,2,3,3,27,1),_Pmpump3AlmLaser2AlmCurrent_Type())
pmpump3AlmLaser2AlmCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2AlmCurrent.setStatus(_A)
_Pmpump3AlmLaser2AlmTemp_Type=EkiOnOff
_Pmpump3AlmLaser2AlmTemp_Object=MibScalar
pmpump3AlmLaser2AlmTemp=_Pmpump3AlmLaser2AlmTemp_Object((1,3,6,1,4,1,20044,49,2,3,3,27,2),_Pmpump3AlmLaser2AlmTemp_Type())
pmpump3AlmLaser2AlmTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2AlmTemp.setStatus(_A)
_Pmpump3AlmLaser2AlmTecPower_Type=EkiOnOff
_Pmpump3AlmLaser2AlmTecPower_Object=MibScalar
pmpump3AlmLaser2AlmTecPower=_Pmpump3AlmLaser2AlmTecPower_Object((1,3,6,1,4,1,20044,49,2,3,3,27,3),_Pmpump3AlmLaser2AlmTecPower_Type())
pmpump3AlmLaser2AlmTecPower.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2AlmTecPower.setStatus(_A)
_Pmpump3AlmLaser2AlmTecDev_Type=EkiOnOff
_Pmpump3AlmLaser2AlmTecDev_Object=MibScalar
pmpump3AlmLaser2AlmTecDev=_Pmpump3AlmLaser2AlmTecDev_Object((1,3,6,1,4,1,20044,49,2,3,3,27,4),_Pmpump3AlmLaser2AlmTecDev_Type())
pmpump3AlmLaser2AlmTecDev.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2AlmTecDev.setStatus(_A)
_Pmpump3AlmLaser2OaDisconnectedLsd_Type=EkiOnOff
_Pmpump3AlmLaser2OaDisconnectedLsd_Object=MibScalar
pmpump3AlmLaser2OaDisconnectedLsd=_Pmpump3AlmLaser2OaDisconnectedLsd_Object((1,3,6,1,4,1,20044,49,2,3,3,27,5),_Pmpump3AlmLaser2OaDisconnectedLsd_Type())
pmpump3AlmLaser2OaDisconnectedLsd.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2OaDisconnectedLsd.setStatus(_A)
_Pmpump3AlmLaser2ExtLsd_Type=EkiOnOff
_Pmpump3AlmLaser2ExtLsd_Object=MibScalar
pmpump3AlmLaser2ExtLsd=_Pmpump3AlmLaser2ExtLsd_Object((1,3,6,1,4,1,20044,49,2,3,3,27,6),_Pmpump3AlmLaser2ExtLsd_Type())
pmpump3AlmLaser2ExtLsd.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3AlmLaser2ExtLsd.setStatus(_A)
_Pmpump3measures_ObjectIdentity=ObjectIdentity
pmpump3measures=_Pmpump3measures_ObjectIdentity((1,3,6,1,4,1,20044,49,3))
_Pmpump3MesrOther_ObjectIdentity=ObjectIdentity
pmpump3MesrOther=_Pmpump3MesrOther_ObjectIdentity((1,3,6,1,4,1,20044,49,3,1))
class _Pmpump3MesrtempMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3MesrtempMeas_Type.__name__=_E
_Pmpump3MesrtempMeas_Object=MibScalar
pmpump3MesrtempMeas=_Pmpump3MesrtempMeas_Object((1,3,6,1,4,1,20044,49,3,1,74),_Pmpump3MesrtempMeas_Type())
pmpump3MesrtempMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3MesrtempMeas.setStatus(_A)
_Pmpump3MesrClient_ObjectIdentity=ObjectIdentity
pmpump3MesrClient=_Pmpump3MesrClient_ObjectIdentity((1,3,6,1,4,1,20044,49,3,2))
class _Pmpump3Mesrlaser1BiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser1BiasMeas_Type.__name__=_E
_Pmpump3Mesrlaser1BiasMeas_Object=MibScalar
pmpump3Mesrlaser1BiasMeas=_Pmpump3Mesrlaser1BiasMeas_Object((1,3,6,1,4,1,20044,49,3,2,16),_Pmpump3Mesrlaser1BiasMeas_Type())
pmpump3Mesrlaser1BiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser1BiasMeas.setStatus(_A)
class _Pmpump3Mesrlaser1VthMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser1VthMeas_Type.__name__=_E
_Pmpump3Mesrlaser1VthMeas_Object=MibScalar
pmpump3Mesrlaser1VthMeas=_Pmpump3Mesrlaser1VthMeas_Object((1,3,6,1,4,1,20044,49,3,2,17),_Pmpump3Mesrlaser1VthMeas_Type())
pmpump3Mesrlaser1VthMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser1VthMeas.setStatus(_A)
class _Pmpump3Mesrlaser1Pwr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser1Pwr_Type.__name__=_E
_Pmpump3Mesrlaser1Pwr_Object=MibScalar
pmpump3Mesrlaser1Pwr=_Pmpump3Mesrlaser1Pwr_Object((1,3,6,1,4,1,20044,49,3,2,36),_Pmpump3Mesrlaser1Pwr_Type())
pmpump3Mesrlaser1Pwr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser1Pwr.setStatus(_A)
class _Pmpump3Mesrlaser1Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser1Temp_Type.__name__=_E
_Pmpump3Mesrlaser1Temp_Object=MibScalar
pmpump3Mesrlaser1Temp=_Pmpump3Mesrlaser1Temp_Object((1,3,6,1,4,1,20044,49,3,2,37),_Pmpump3Mesrlaser1Temp_Type())
pmpump3Mesrlaser1Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser1Temp.setStatus(_A)
_Pmpump3MesrLine_ObjectIdentity=ObjectIdentity
pmpump3MesrLine=_Pmpump3MesrLine_ObjectIdentity((1,3,6,1,4,1,20044,49,3,3))
class _Pmpump3Mesrlaser2BiasMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser2BiasMeas_Type.__name__=_E
_Pmpump3Mesrlaser2BiasMeas_Object=MibScalar
pmpump3Mesrlaser2BiasMeas=_Pmpump3Mesrlaser2BiasMeas_Object((1,3,6,1,4,1,20044,49,3,3,24),_Pmpump3Mesrlaser2BiasMeas_Type())
pmpump3Mesrlaser2BiasMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser2BiasMeas.setStatus(_A)
class _Pmpump3Mesrlaser2VthMeas_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser2VthMeas_Type.__name__=_E
_Pmpump3Mesrlaser2VthMeas_Object=MibScalar
pmpump3Mesrlaser2VthMeas=_Pmpump3Mesrlaser2VthMeas_Object((1,3,6,1,4,1,20044,49,3,3,25),_Pmpump3Mesrlaser2VthMeas_Type())
pmpump3Mesrlaser2VthMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser2VthMeas.setStatus(_A)
class _Pmpump3Mesrlaser2Pwr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser2Pwr_Type.__name__=_E
_Pmpump3Mesrlaser2Pwr_Object=MibScalar
pmpump3Mesrlaser2Pwr=_Pmpump3Mesrlaser2Pwr_Object((1,3,6,1,4,1,20044,49,3,3,44),_Pmpump3Mesrlaser2Pwr_Type())
pmpump3Mesrlaser2Pwr.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser2Pwr.setStatus(_A)
class _Pmpump3Mesrlaser2Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Mesrlaser2Temp_Type.__name__=_E
_Pmpump3Mesrlaser2Temp_Object=MibScalar
pmpump3Mesrlaser2Temp=_Pmpump3Mesrlaser2Temp_Object((1,3,6,1,4,1,20044,49,3,3,45),_Pmpump3Mesrlaser2Temp_Type())
pmpump3Mesrlaser2Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3Mesrlaser2Temp.setStatus(_A)
_Pmpump3controlsWrite_ObjectIdentity=ObjectIdentity
pmpump3controlsWrite=_Pmpump3controlsWrite_ObjectIdentity((1,3,6,1,4,1,20044,49,6))
_Pmpump3CtrlOther_ObjectIdentity=ObjectIdentity
pmpump3CtrlOther=_Pmpump3CtrlOther_ObjectIdentity((1,3,6,1,4,1,20044,49,6,1))
_Pmpump3Ctrlsynth0_ObjectIdentity=ObjectIdentity
pmpump3Ctrlsynth0=_Pmpump3Ctrlsynth0_ObjectIdentity((1,3,6,1,4,1,20044,49,6,1,0))
_Pmpump3CtrlConfLoad_Type=EkiOnOff
_Pmpump3CtrlConfLoad_Object=MibScalar
pmpump3CtrlConfLoad=_Pmpump3CtrlConfLoad_Object((1,3,6,1,4,1,20044,49,6,1,0,1),_Pmpump3CtrlConfLoad_Type())
pmpump3CtrlConfLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlConfLoad.setStatus(_A)
_Pmpump3CtrlConfFlash_Type=EkiOnOff
_Pmpump3CtrlConfFlash_Object=MibScalar
pmpump3CtrlConfFlash=_Pmpump3CtrlConfFlash_Object((1,3,6,1,4,1,20044,49,6,1,0,9),_Pmpump3CtrlConfFlash_Type())
pmpump3CtrlConfFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlConfFlash.setStatus(_A)
_Pmpump3CtrlConfClear_Type=EkiOnOff
_Pmpump3CtrlConfClear_Object=MibScalar
pmpump3CtrlConfClear=_Pmpump3CtrlConfClear_Object((1,3,6,1,4,1,20044,49,6,1,0,13),_Pmpump3CtrlConfClear_Type())
pmpump3CtrlConfClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlConfClear.setStatus(_A)
_Pmpump3CtrlswMgnt_ObjectIdentity=ObjectIdentity
pmpump3CtrlswMgnt=_Pmpump3CtrlswMgnt_ObjectIdentity((1,3,6,1,4,1,20044,49,6,1,5))
_Pmpump3CtrlColdReset_Type=EkiOnOff
_Pmpump3CtrlColdReset_Object=MibScalar
pmpump3CtrlColdReset=_Pmpump3CtrlColdReset_Object((1,3,6,1,4,1,20044,49,6,1,5,2),_Pmpump3CtrlColdReset_Type())
pmpump3CtrlColdReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlColdReset.setStatus(_A)
_Pmpump3CtrlWarmReset_Type=EkiOnOff
_Pmpump3CtrlWarmReset_Object=MibScalar
pmpump3CtrlWarmReset=_Pmpump3CtrlWarmReset_Object((1,3,6,1,4,1,20044,49,6,1,5,3),_Pmpump3CtrlWarmReset_Type())
pmpump3CtrlWarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlWarmReset.setStatus(_A)
_Pmpump3CtrlledTest_ObjectIdentity=ObjectIdentity
pmpump3CtrlledTest=_Pmpump3CtrlledTest_ObjectIdentity((1,3,6,1,4,1,20044,49,6,1,73))
_Pmpump3CtrlGreenLed_Type=EkiOnOff
_Pmpump3CtrlGreenLed_Object=MibScalar
pmpump3CtrlGreenLed=_Pmpump3CtrlGreenLed_Object((1,3,6,1,4,1,20044,49,6,1,73,1),_Pmpump3CtrlGreenLed_Type())
pmpump3CtrlGreenLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlGreenLed.setStatus(_A)
_Pmpump3CtrlRedLed_Type=EkiOnOff
_Pmpump3CtrlRedLed_Object=MibScalar
pmpump3CtrlRedLed=_Pmpump3CtrlRedLed_Object((1,3,6,1,4,1,20044,49,6,1,73,2),_Pmpump3CtrlRedLed_Type())
pmpump3CtrlRedLed.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlRedLed.setStatus(_A)
_Pmpump3CtrlLedOff_Type=EkiOnOff
_Pmpump3CtrlLedOff_Object=MibScalar
pmpump3CtrlLedOff=_Pmpump3CtrlLedOff_Object((1,3,6,1,4,1,20044,49,6,1,73,3),_Pmpump3CtrlLedOff_Type())
pmpump3CtrlLedOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlLedOff.setStatus(_A)
_Pmpump3CtrlClient_ObjectIdentity=ObjectIdentity
pmpump3CtrlClient=_Pmpump3CtrlClient_ObjectIdentity((1,3,6,1,4,1,20044,49,6,2))
_Pmpump3Ctrllaser1LaserOff_ObjectIdentity=ObjectIdentity
pmpump3Ctrllaser1LaserOff=_Pmpump3Ctrllaser1LaserOff_ObjectIdentity((1,3,6,1,4,1,20044,49,6,2,32))
_Pmpump3CtrlLaser1LaserOff_Type=EkiOnOff
_Pmpump3CtrlLaser1LaserOff_Object=MibScalar
pmpump3CtrlLaser1LaserOff=_Pmpump3CtrlLaser1LaserOff_Object((1,3,6,1,4,1,20044,49,6,2,32,1),_Pmpump3CtrlLaser1LaserOff_Type())
pmpump3CtrlLaser1LaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlLaser1LaserOff.setStatus(_A)
class _Pmpump3Ctrllaser1EffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Ctrllaser1EffPwrOutSettingValue_Type.__name__=_E
_Pmpump3Ctrllaser1EffPwrOutSettingValue_Object=MibScalar
pmpump3Ctrllaser1EffPwrOutSettingValue=_Pmpump3Ctrllaser1EffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,49,6,2,37),_Pmpump3Ctrllaser1EffPwrOutSettingValue_Type())
pmpump3Ctrllaser1EffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3Ctrllaser1EffPwrOutSettingValue.setStatus(_A)
_Pmpump3CtrlLine_ObjectIdentity=ObjectIdentity
pmpump3CtrlLine=_Pmpump3CtrlLine_ObjectIdentity((1,3,6,1,4,1,20044,49,6,3))
_Pmpump3Ctrllaser2LaserOff_ObjectIdentity=ObjectIdentity
pmpump3Ctrllaser2LaserOff=_Pmpump3Ctrllaser2LaserOff_ObjectIdentity((1,3,6,1,4,1,20044,49,6,3,40))
_Pmpump3CtrlLaser2LaserOff_Type=EkiOnOff
_Pmpump3CtrlLaser2LaserOff_Object=MibScalar
pmpump3CtrlLaser2LaserOff=_Pmpump3CtrlLaser2LaserOff_Object((1,3,6,1,4,1,20044,49,6,3,40,1),_Pmpump3CtrlLaser2LaserOff_Type())
pmpump3CtrlLaser2LaserOff.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CtrlLaser2LaserOff.setStatus(_A)
class _Pmpump3Ctrllaser2EffPwrOutSettingValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Pmpump3Ctrllaser2EffPwrOutSettingValue_Type.__name__=_E
_Pmpump3Ctrllaser2EffPwrOutSettingValue_Object=MibScalar
pmpump3Ctrllaser2EffPwrOutSettingValue=_Pmpump3Ctrllaser2EffPwrOutSettingValue_Object((1,3,6,1,4,1,20044,49,6,3,45),_Pmpump3Ctrllaser2EffPwrOutSettingValue_Type())
pmpump3Ctrllaser2EffPwrOutSettingValue.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3Ctrllaser2EffPwrOutSettingValue.setStatus(_A)
_Pmpump3ri_ObjectIdentity=ObjectIdentity
pmpump3ri=_Pmpump3ri_ObjectIdentity((1,3,6,1,4,1,20044,49,7))
_Pmpump3riTable_ObjectIdentity=ObjectIdentity
pmpump3riTable=_Pmpump3riTable_ObjectIdentity((1,3,6,1,4,1,20044,49,7,1))
_Pmpump3RinvLaser1Table_Object=MibTable
pmpump3RinvLaser1Table=_Pmpump3RinvLaser1Table_Object((1,3,6,1,4,1,20044,49,7,1,1))
if mibBuilder.loadTexts:pmpump3RinvLaser1Table.setStatus(_A)
_Pmpump3RinvLaser1Entry_Object=MibTableRow
pmpump3RinvLaser1Entry=_Pmpump3RinvLaser1Entry_Object((1,3,6,1,4,1,20044,49,7,1,1,1))
pmpump3RinvLaser1Entry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:pmpump3RinvLaser1Entry.setStatus(_A)
class _Pmpump3RinvLaser1Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pmpump3RinvLaser1Index_Type.__name__=_E
_Pmpump3RinvLaser1Index_Object=MibTableColumn
pmpump3RinvLaser1Index=_Pmpump3RinvLaser1Index_Object((1,3,6,1,4,1,20044,49,7,1,1,1,1),_Pmpump3RinvLaser1Index_Type())
pmpump3RinvLaser1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvLaser1Index.setStatus(_A)
_Pmpump3RinvLaser1_Type=DisplayString
_Pmpump3RinvLaser1_Object=MibTableColumn
pmpump3RinvLaser1=_Pmpump3RinvLaser1_Object((1,3,6,1,4,1,20044,49,7,1,1,1,2),_Pmpump3RinvLaser1_Type())
pmpump3RinvLaser1.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvLaser1.setStatus(_A)
_Pmpump3RinvLaser2Table_Object=MibTable
pmpump3RinvLaser2Table=_Pmpump3RinvLaser2Table_Object((1,3,6,1,4,1,20044,49,7,1,2))
if mibBuilder.loadTexts:pmpump3RinvLaser2Table.setStatus(_A)
_Pmpump3RinvLaser2Entry_Object=MibTableRow
pmpump3RinvLaser2Entry=_Pmpump3RinvLaser2Entry_Object((1,3,6,1,4,1,20044,49,7,1,2,1))
pmpump3RinvLaser2Entry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:pmpump3RinvLaser2Entry.setStatus(_A)
class _Pmpump3RinvLaser2Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Pmpump3RinvLaser2Index_Type.__name__=_E
_Pmpump3RinvLaser2Index_Object=MibTableColumn
pmpump3RinvLaser2Index=_Pmpump3RinvLaser2Index_Object((1,3,6,1,4,1,20044,49,7,1,2,1,1),_Pmpump3RinvLaser2Index_Type())
pmpump3RinvLaser2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvLaser2Index.setStatus(_A)
_Pmpump3RinvLaser2_Type=DisplayString
_Pmpump3RinvLaser2_Object=MibTableColumn
pmpump3RinvLaser2=_Pmpump3RinvLaser2_Object((1,3,6,1,4,1,20044,49,7,1,2,1,2),_Pmpump3RinvLaser2_Type())
pmpump3RinvLaser2.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvLaser2.setStatus(_A)
_Pmpump3RinvReloadInventory_Type=EkiOnOff
_Pmpump3RinvReloadInventory_Object=MibScalar
pmpump3RinvReloadInventory=_Pmpump3RinvReloadInventory_Object((1,3,6,1,4,1,20044,49,7,2),_Pmpump3RinvReloadInventory_Type())
pmpump3RinvReloadInventory.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3RinvReloadInventory.setStatus(_A)
_Pmpump3RinvHwPlatform_Type=DisplayString
_Pmpump3RinvHwPlatform_Object=MibScalar
pmpump3RinvHwPlatform=_Pmpump3RinvHwPlatform_Object((1,3,6,1,4,1,20044,49,7,3),_Pmpump3RinvHwPlatform_Type())
pmpump3RinvHwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvHwPlatform.setStatus(_A)
_Pmpump3RinvModulePlatform_Type=DisplayString
_Pmpump3RinvModulePlatform_Object=MibScalar
pmpump3RinvModulePlatform=_Pmpump3RinvModulePlatform_Object((1,3,6,1,4,1,20044,49,7,4),_Pmpump3RinvModulePlatform_Type())
pmpump3RinvModulePlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvModulePlatform.setStatus(_A)
_Pmpump3RinvSwPlatform_Type=DisplayString
_Pmpump3RinvSwPlatform_Object=MibScalar
pmpump3RinvSwPlatform=_Pmpump3RinvSwPlatform_Object((1,3,6,1,4,1,20044,49,7,5),_Pmpump3RinvSwPlatform_Type())
pmpump3RinvSwPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3RinvSwPlatform.setStatus(_A)
_Pmpump3Config_ObjectIdentity=ObjectIdentity
pmpump3Config=_Pmpump3Config_ObjectIdentity((1,3,6,1,4,1,20044,49,9))
_Pmpump3CfgNoValue_ObjectIdentity=ObjectIdentity
pmpump3CfgNoValue=_Pmpump3CfgNoValue_ObjectIdentity((1,3,6,1,4,1,20044,49,9,1))
_Pmpump3tableclientStartup_ObjectIdentity=ObjectIdentity
pmpump3tableclientStartup=_Pmpump3tableclientStartup_ObjectIdentity((1,3,6,1,4,1,20044,49,9,1,1))
class _Pmpump3Cfglaser1Ctrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmpump3Cfglaser1Ctrl_Type.__name__=_G
_Pmpump3Cfglaser1Ctrl_Object=MibScalar
pmpump3Cfglaser1Ctrl=_Pmpump3Cfglaser1Ctrl_Object((1,3,6,1,4,1,20044,49,9,1,1,2),_Pmpump3Cfglaser1Ctrl_Type())
pmpump3Cfglaser1Ctrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3Cfglaser1Ctrl.setStatus(_A)
_Pmpump3CfgLineStartUp_ObjectIdentity=ObjectIdentity
pmpump3CfgLineStartUp=_Pmpump3CfgLineStartUp_ObjectIdentity((1,3,6,1,4,1,20044,49,9,2))
_Pmpump3tablelineStartup_ObjectIdentity=ObjectIdentity
pmpump3tablelineStartup=_Pmpump3tablelineStartup_ObjectIdentity((1,3,6,1,4,1,20044,49,9,2,1))
class _Pmpump3Cfglaser2Ctrl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_Pmpump3Cfglaser2Ctrl_Type.__name__=_G
_Pmpump3Cfglaser2Ctrl_Object=MibScalar
pmpump3Cfglaser2Ctrl=_Pmpump3Cfglaser2Ctrl_Object((1,3,6,1,4,1,20044,49,9,2,1,2),_Pmpump3Cfglaser2Ctrl_Type())
pmpump3Cfglaser2Ctrl.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3Cfglaser2Ctrl.setStatus(_A)
_Pmpump3CfgLabels_ObjectIdentity=ObjectIdentity
pmpump3CfgLabels=_Pmpump3CfgLabels_ObjectIdentity((1,3,6,1,4,1,20044,49,9,3))
_Pmpump3CfgLabelclientTable_Object=MibTable
pmpump3CfgLabelclientTable=_Pmpump3CfgLabelclientTable_Object((1,3,6,1,4,1,20044,49,9,3,1))
if mibBuilder.loadTexts:pmpump3CfgLabelclientTable.setStatus(_A)
_Pmpump3CfgLabelclientEntry_Object=MibTableRow
pmpump3CfgLabelclientEntry=_Pmpump3CfgLabelclientEntry_Object((1,3,6,1,4,1,20044,49,9,3,1,1))
pmpump3CfgLabelclientEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:pmpump3CfgLabelclientEntry.setStatus(_A)
class _Pmpump3CfgLabelclientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmpump3CfgLabelclientIndex_Type.__name__=_E
_Pmpump3CfgLabelclientIndex_Object=MibTableColumn
pmpump3CfgLabelclientIndex=_Pmpump3CfgLabelclientIndex_Object((1,3,6,1,4,1,20044,49,9,3,1,1,1),_Pmpump3CfgLabelclientIndex_Type())
pmpump3CfgLabelclientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3CfgLabelclientIndex.setStatus(_A)
class _Pmpump3CfgLabelclientPortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmpump3CfgLabelclientPortn_Type.__name__=_H
_Pmpump3CfgLabelclientPortn_Object=MibTableColumn
pmpump3CfgLabelclientPortn=_Pmpump3CfgLabelclientPortn_Object((1,3,6,1,4,1,20044,49,9,3,1,1,3),_Pmpump3CfgLabelclientPortn_Type())
pmpump3CfgLabelclientPortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CfgLabelclientPortn.setStatus(_A)
_Pmpump3CfgLabellineTable_Object=MibTable
pmpump3CfgLabellineTable=_Pmpump3CfgLabellineTable_Object((1,3,6,1,4,1,20044,49,9,3,2))
if mibBuilder.loadTexts:pmpump3CfgLabellineTable.setStatus(_A)
_Pmpump3CfgLabellineEntry_Object=MibTableRow
pmpump3CfgLabellineEntry=_Pmpump3CfgLabellineEntry_Object((1,3,6,1,4,1,20044,49,9,3,2,1))
pmpump3CfgLabellineEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:pmpump3CfgLabellineEntry.setStatus(_A)
class _Pmpump3CfgLabellineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_Pmpump3CfgLabellineIndex_Type.__name__=_E
_Pmpump3CfgLabellineIndex_Object=MibTableColumn
pmpump3CfgLabellineIndex=_Pmpump3CfgLabellineIndex_Object((1,3,6,1,4,1,20044,49,9,3,2,1,1),_Pmpump3CfgLabellineIndex_Type())
pmpump3CfgLabellineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3CfgLabellineIndex.setStatus(_A)
class _Pmpump3CfgLabellinePortn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Pmpump3CfgLabellinePortn_Type.__name__=_H
_Pmpump3CfgLabellinePortn_Object=MibTableColumn
pmpump3CfgLabellinePortn=_Pmpump3CfgLabellinePortn_Object((1,3,6,1,4,1,20044,49,9,3,2,1,3),_Pmpump3CfgLabellinePortn_Type())
pmpump3CfgLabellinePortn.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CfgLabellinePortn.setStatus(_A)
_Pmpump3CfgWriteConfiguration_Type=EkiOnOff
_Pmpump3CfgWriteConfiguration_Object=MibScalar
pmpump3CfgWriteConfiguration=_Pmpump3CfgWriteConfiguration_Object((1,3,6,1,4,1,20044,49,9,257),_Pmpump3CfgWriteConfiguration_Type())
pmpump3CfgWriteConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:pmpump3CfgWriteConfiguration.setStatus(_A)
_Pmpump3traps_ObjectIdentity=ObjectIdentity
pmpump3traps=_Pmpump3traps_ObjectIdentity((1,3,6,1,4,1,20044,49,10))
class _Pmpump3trapBoardNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Pmpump3trapBoardNumber_Type.__name__=_E
_Pmpump3trapBoardNumber_Object=MibScalar
pmpump3trapBoardNumber=_Pmpump3trapBoardNumber_Object((1,3,6,1,4,1,20044,49,10,4),_Pmpump3trapBoardNumber_Type())
pmpump3trapBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pmpump3trapBoardNumber.setStatus(_A)
pmpump3Laser2TrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,30))
pmpump3Laser2TrapNotUrgentGoesOn.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser2TrapNotUrgentGoesOn.setStatus(_A)
pmpump3Laser2TrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,31))
pmpump3Laser2TrapNotUrgentGoesOff.setObjects(*((_C,_I),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser2TrapNotUrgentGoesOff.setStatus(_A)
pmpump3Laser2TrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,32))
pmpump3Laser2TrapUrgentGoesOn.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser2TrapUrgentGoesOn.setStatus(_A)
pmpump3Laser2TrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,33))
pmpump3Laser2TrapUrgentGoesOff.setObjects(*((_C,_J),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser2TrapUrgentGoesOff.setStatus(_A)
pmpump3Laser2TrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,34))
pmpump3Laser2TrapCritGoesOn.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser2TrapCritGoesOn.setStatus(_A)
pmpump3Laser2TrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,35))
pmpump3Laser2TrapCritGoesOff.setObjects(*((_C,_K),(_C,_L),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser2TrapCritGoesOff.setStatus(_A)
pmpump3Laser1TrapNotUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,40))
pmpump3Laser1TrapNotUrgentGoesOn.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser1TrapNotUrgentGoesOn.setStatus(_A)
pmpump3Laser1TrapNotUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,41))
pmpump3Laser1TrapNotUrgentGoesOff.setObjects(*((_C,_M),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser1TrapNotUrgentGoesOff.setStatus(_A)
pmpump3Laser1TrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,42))
pmpump3Laser1TrapUrgentGoesOn.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser1TrapUrgentGoesOn.setStatus(_A)
pmpump3Laser1TrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,43))
pmpump3Laser1TrapUrgentGoesOff.setObjects(*((_C,_N),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser1TrapUrgentGoesOff.setStatus(_A)
pmpump3Laser1TrapCritGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,44))
pmpump3Laser1TrapCritGoesOn.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser1TrapCritGoesOn.setStatus(_A)
pmpump3Laser1TrapCritGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,45))
pmpump3Laser1TrapCritGoesOff.setObjects(*((_C,_O),(_C,_P),(_C,_F)))
if mibBuilder.loadTexts:pmpump3Laser1TrapCritGoesOff.setStatus(_A)
pmpump3PowerTrapUrgentGoesOn=NotificationType((1,3,6,1,4,1,20044,49,10,50))
pmpump3PowerTrapUrgentGoesOn.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmpump3PowerTrapUrgentGoesOn.setStatus(_A)
pmpump3PowerTrapUrgentGoesOff=NotificationType((1,3,6,1,4,1,20044,49,10,51))
pmpump3PowerTrapUrgentGoesOff.setObjects(*((_C,_Q),(_C,_R),(_C,_F)))
if mibBuilder.loadTexts:pmpump3PowerTrapUrgentGoesOff.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'modulepmpump3':modulepmpump3,'pmpump3alarms':pmpump3alarms,'pmpump3AlmOther':pmpump3AlmOther,'pmpump3AlmOtherNurg':pmpump3AlmOtherNurg,'pmpump3AlmsynthAlm2':pmpump3AlmsynthAlm2,'pmpump3AlmConfTableSave':pmpump3AlmConfTableSave,'pmpump3AlmInvUpload':pmpump3AlmInvUpload,'pmpump3AlmConfTableLoad':pmpump3AlmConfTableLoad,'pmpump3AlmpmWarnings':pmpump3AlmpmWarnings,'pmpump3AlmTermpLowWarning':pmpump3AlmTermpLowWarning,'pmpump3AlmTempHighWarning':pmpump3AlmTempHighWarning,'pmpump3AlmOtherUrg':pmpump3AlmOtherUrg,'pmpump3AlmpmAlarms':pmpump3AlmpmAlarms,'pmpump3AlmTermpLowAlarm':pmpump3AlmTermpLowAlarm,'pmpump3AlmTempHighAlarm':pmpump3AlmTempHighAlarm,'pmpump3AlmOtherCrit':pmpump3AlmOtherCrit,'pmpump3AlmsynthAlm0':pmpump3AlmsynthAlm0,'pmpump3AlmModGlobFail':pmpump3AlmModGlobFail,_R:pmpump3AlmDefFuseA,_Q:pmpump3AlmDefFuseB,'pmpump3AlmClient':pmpump3AlmClient,'pmpump3AlmClientNurg':pmpump3AlmClientNurg,'pmpump3Almlaser1Warnings':pmpump3Almlaser1Warnings,'pmpump3AlmLaser1TempLowWarning':pmpump3AlmLaser1TempLowWarning,'pmpump3AlmLaser1TempHighWarning':pmpump3AlmLaser1TempHighWarning,'pmpump3AlmLaser1VthLowWarning':pmpump3AlmLaser1VthLowWarning,'pmpump3AlmLaser1VthHighWarning':pmpump3AlmLaser1VthHighWarning,'pmpump3AlmLaser1OutputPwrLowWarning':pmpump3AlmLaser1OutputPwrLowWarning,'pmpump3AlmLaser1OutputPwrHighWarning':pmpump3AlmLaser1OutputPwrHighWarning,'pmpump3AlmLaser1BiasLowWarning':pmpump3AlmLaser1BiasLowWarning,'pmpump3AlmLaser1BiasHighWarning':pmpump3AlmLaser1BiasHighWarning,'pmpump3AlmClientUrg':pmpump3AlmClientUrg,'pmpump3Almlaser1Alarms1':pmpump3Almlaser1Alarms1,'pmpump3AlmLaser1TempLowAlarm':pmpump3AlmLaser1TempLowAlarm,'pmpump3AlmLaser1TempHighAlarm':pmpump3AlmLaser1TempHighAlarm,'pmpump3AlmLaser1VthLowAlarm':pmpump3AlmLaser1VthLowAlarm,'pmpump3AlmLaser1VthHighAlarm':pmpump3AlmLaser1VthHighAlarm,'pmpump3AlmLaser1OutputPwrLowAlarm':pmpump3AlmLaser1OutputPwrLowAlarm,'pmpump3AlmLaser1OutputPwrHighAlarm':pmpump3AlmLaser1OutputPwrHighAlarm,'pmpump3AlmLaser1BiasLowAlarm':pmpump3AlmLaser1BiasLowAlarm,'pmpump3AlmLaser1BiasHighAlarm':pmpump3AlmLaser1BiasHighAlarm,'pmpump3AlmClientCrit':pmpump3AlmClientCrit,'pmpump3AlmsynthAlmLaser1':pmpump3AlmsynthAlmLaser1,'pmpump3AlmLaser1InitNotCompl':pmpump3AlmLaser1InitNotCompl,_P:pmpump3AlmLaser1HwFail,'pmpump3AlmLaser1TxOff':pmpump3AlmLaser1TxOff,'pmpump3AlmLaser1Oos':pmpump3AlmLaser1Oos,_M:pmpump3AlmLaser1Warning,_N:pmpump3AlmLaser1Alm,_O:pmpump3AlmLaser1Fail,'pmpump3AlmsynthAlmLaser2':pmpump3AlmsynthAlmLaser2,'pmpump3AlmLaser2InitNotCompl':pmpump3AlmLaser2InitNotCompl,_L:pmpump3AlmLaser2HwFail,'pmpump3AlmLaser2TxOff':pmpump3AlmLaser2TxOff,'pmpump3AlmLaser2Oos':pmpump3AlmLaser2Oos,_I:pmpump3AlmLaser2Warning,_J:pmpump3AlmLaser2Alm,_K:pmpump3AlmLaser2Fail,'pmpump3Almlaser1Alarms2':pmpump3Almlaser1Alarms2,'pmpump3AlmLaser1AlmCurrent':pmpump3AlmLaser1AlmCurrent,'pmpump3AlmLaser1AlmTemp':pmpump3AlmLaser1AlmTemp,'pmpump3AlmLaser1AlmTecPower':pmpump3AlmLaser1AlmTecPower,'pmpump3AlmLaser1AlmTecDev':pmpump3AlmLaser1AlmTecDev,'pmpump3AlmLaser1OaDisconnectedLsd':pmpump3AlmLaser1OaDisconnectedLsd,'pmpump3AlmLaser1ExtLsd':pmpump3AlmLaser1ExtLsd,'pmpump3AlmLine':pmpump3AlmLine,'pmpump3AlmLineNurg':pmpump3AlmLineNurg,'pmpump3Almlaser2Warnings':pmpump3Almlaser2Warnings,'pmpump3AlmLaser2TempLowWarning':pmpump3AlmLaser2TempLowWarning,'pmpump3AlmLaser2TempHighWarning':pmpump3AlmLaser2TempHighWarning,'pmpump3AlmLaser2VthLowWarning':pmpump3AlmLaser2VthLowWarning,'pmpump3AlmLaser2VthHighWarning':pmpump3AlmLaser2VthHighWarning,'pmpump3AlmLaser2OutputPwrLowWarning':pmpump3AlmLaser2OutputPwrLowWarning,'pmpump3AlmLaser2OutputPwrHighWarning':pmpump3AlmLaser2OutputPwrHighWarning,'pmpump3AlmLaser2BiasLowWarning':pmpump3AlmLaser2BiasLowWarning,'pmpump3AlmLaser2BiasHighWarning':pmpump3AlmLaser2BiasHighWarning,'pmpump3AlmLineUrg':pmpump3AlmLineUrg,'pmpump3Almlaser2Alarms1':pmpump3Almlaser2Alarms1,'pmpump3AlmLaser2TempLowAlarm':pmpump3AlmLaser2TempLowAlarm,'pmpump3AlmLaser2TempHighAlarm':pmpump3AlmLaser2TempHighAlarm,'pmpump3AlmLaser2VthLowAlarm':pmpump3AlmLaser2VthLowAlarm,'pmpump3AlmLaser2VthHighAlarm':pmpump3AlmLaser2VthHighAlarm,'pmpump3AlmLaser2OutputPwrLowAlarm':pmpump3AlmLaser2OutputPwrLowAlarm,'pmpump3AlmLaser2OutputPwrHighAlarm':pmpump3AlmLaser2OutputPwrHighAlarm,'pmpump3AlmLaser2BiasLowAlarm':pmpump3AlmLaser2BiasLowAlarm,'pmpump3AlmLaser2BiasHighAlarm':pmpump3AlmLaser2BiasHighAlarm,'pmpump3AlmLineCrit':pmpump3AlmLineCrit,'pmpump3Almlaser2Alarms2':pmpump3Almlaser2Alarms2,'pmpump3AlmLaser2AlmCurrent':pmpump3AlmLaser2AlmCurrent,'pmpump3AlmLaser2AlmTemp':pmpump3AlmLaser2AlmTemp,'pmpump3AlmLaser2AlmTecPower':pmpump3AlmLaser2AlmTecPower,'pmpump3AlmLaser2AlmTecDev':pmpump3AlmLaser2AlmTecDev,'pmpump3AlmLaser2OaDisconnectedLsd':pmpump3AlmLaser2OaDisconnectedLsd,'pmpump3AlmLaser2ExtLsd':pmpump3AlmLaser2ExtLsd,'pmpump3measures':pmpump3measures,'pmpump3MesrOther':pmpump3MesrOther,'pmpump3MesrtempMeas':pmpump3MesrtempMeas,'pmpump3MesrClient':pmpump3MesrClient,'pmpump3Mesrlaser1BiasMeas':pmpump3Mesrlaser1BiasMeas,'pmpump3Mesrlaser1VthMeas':pmpump3Mesrlaser1VthMeas,'pmpump3Mesrlaser1Pwr':pmpump3Mesrlaser1Pwr,'pmpump3Mesrlaser1Temp':pmpump3Mesrlaser1Temp,'pmpump3MesrLine':pmpump3MesrLine,'pmpump3Mesrlaser2BiasMeas':pmpump3Mesrlaser2BiasMeas,'pmpump3Mesrlaser2VthMeas':pmpump3Mesrlaser2VthMeas,'pmpump3Mesrlaser2Pwr':pmpump3Mesrlaser2Pwr,'pmpump3Mesrlaser2Temp':pmpump3Mesrlaser2Temp,'pmpump3controlsWrite':pmpump3controlsWrite,'pmpump3CtrlOther':pmpump3CtrlOther,'pmpump3Ctrlsynth0':pmpump3Ctrlsynth0,'pmpump3CtrlConfLoad':pmpump3CtrlConfLoad,'pmpump3CtrlConfFlash':pmpump3CtrlConfFlash,'pmpump3CtrlConfClear':pmpump3CtrlConfClear,'pmpump3CtrlswMgnt':pmpump3CtrlswMgnt,'pmpump3CtrlColdReset':pmpump3CtrlColdReset,'pmpump3CtrlWarmReset':pmpump3CtrlWarmReset,'pmpump3CtrlledTest':pmpump3CtrlledTest,'pmpump3CtrlGreenLed':pmpump3CtrlGreenLed,'pmpump3CtrlRedLed':pmpump3CtrlRedLed,'pmpump3CtrlLedOff':pmpump3CtrlLedOff,'pmpump3CtrlClient':pmpump3CtrlClient,'pmpump3Ctrllaser1LaserOff':pmpump3Ctrllaser1LaserOff,'pmpump3CtrlLaser1LaserOff':pmpump3CtrlLaser1LaserOff,'pmpump3Ctrllaser1EffPwrOutSettingValue':pmpump3Ctrllaser1EffPwrOutSettingValue,'pmpump3CtrlLine':pmpump3CtrlLine,'pmpump3Ctrllaser2LaserOff':pmpump3Ctrllaser2LaserOff,'pmpump3CtrlLaser2LaserOff':pmpump3CtrlLaser2LaserOff,'pmpump3Ctrllaser2EffPwrOutSettingValue':pmpump3Ctrllaser2EffPwrOutSettingValue,'pmpump3ri':pmpump3ri,'pmpump3riTable':pmpump3riTable,'pmpump3RinvLaser1Table':pmpump3RinvLaser1Table,'pmpump3RinvLaser1Entry':pmpump3RinvLaser1Entry,_S:pmpump3RinvLaser1Index,'pmpump3RinvLaser1':pmpump3RinvLaser1,'pmpump3RinvLaser2Table':pmpump3RinvLaser2Table,'pmpump3RinvLaser2Entry':pmpump3RinvLaser2Entry,_T:pmpump3RinvLaser2Index,'pmpump3RinvLaser2':pmpump3RinvLaser2,'pmpump3RinvReloadInventory':pmpump3RinvReloadInventory,'pmpump3RinvHwPlatform':pmpump3RinvHwPlatform,'pmpump3RinvModulePlatform':pmpump3RinvModulePlatform,'pmpump3RinvSwPlatform':pmpump3RinvSwPlatform,'pmpump3Config':pmpump3Config,'pmpump3CfgNoValue':pmpump3CfgNoValue,'pmpump3tableclientStartup':pmpump3tableclientStartup,'pmpump3Cfglaser1Ctrl':pmpump3Cfglaser1Ctrl,'pmpump3CfgLineStartUp':pmpump3CfgLineStartUp,'pmpump3tablelineStartup':pmpump3tablelineStartup,'pmpump3Cfglaser2Ctrl':pmpump3Cfglaser2Ctrl,'pmpump3CfgLabels':pmpump3CfgLabels,'pmpump3CfgLabelclientTable':pmpump3CfgLabelclientTable,'pmpump3CfgLabelclientEntry':pmpump3CfgLabelclientEntry,_U:pmpump3CfgLabelclientIndex,'pmpump3CfgLabelclientPortn':pmpump3CfgLabelclientPortn,'pmpump3CfgLabellineTable':pmpump3CfgLabellineTable,'pmpump3CfgLabellineEntry':pmpump3CfgLabellineEntry,_V:pmpump3CfgLabellineIndex,'pmpump3CfgLabellinePortn':pmpump3CfgLabellinePortn,'pmpump3CfgWriteConfiguration':pmpump3CfgWriteConfiguration,'pmpump3traps':pmpump3traps,_F:pmpump3trapBoardNumber,'pmpump3Laser2TrapNotUrgentGoesOn':pmpump3Laser2TrapNotUrgentGoesOn,'pmpump3Laser2TrapNotUrgentGoesOff':pmpump3Laser2TrapNotUrgentGoesOff,'pmpump3Laser2TrapUrgentGoesOn':pmpump3Laser2TrapUrgentGoesOn,'pmpump3Laser2TrapUrgentGoesOff':pmpump3Laser2TrapUrgentGoesOff,'pmpump3Laser2TrapCritGoesOn':pmpump3Laser2TrapCritGoesOn,'pmpump3Laser2TrapCritGoesOff':pmpump3Laser2TrapCritGoesOff,'pmpump3Laser1TrapNotUrgentGoesOn':pmpump3Laser1TrapNotUrgentGoesOn,'pmpump3Laser1TrapNotUrgentGoesOff':pmpump3Laser1TrapNotUrgentGoesOff,'pmpump3Laser1TrapUrgentGoesOn':pmpump3Laser1TrapUrgentGoesOn,'pmpump3Laser1TrapUrgentGoesOff':pmpump3Laser1TrapUrgentGoesOff,'pmpump3Laser1TrapCritGoesOn':pmpump3Laser1TrapCritGoesOn,'pmpump3Laser1TrapCritGoesOff':pmpump3Laser1TrapCritGoesOff,'pmpump3PowerTrapUrgentGoesOn':pmpump3PowerTrapUrgentGoesOn,'pmpump3PowerTrapUrgentGoesOff':pmpump3PowerTrapUrgentGoesOff})