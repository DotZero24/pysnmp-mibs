_V='agNewCfgTrapHostIndx'
_U='agCurCfgTrapHostIndx'
_T='image2'
_S='image1'
_R='notPresent'
_Q='ALTEON-TIGON-SWITCH-MIB'
_P='local7'
_O='local6'
_N='local5'
_M='local4'
_L='local3'
_K='local2'
_J='local1'
_I='local0'
_H='other'
_G='DisplayString'
_F='disabled'
_E='enabled'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch,=mibBuilder.importSymbols('ALTEON-ROOT-MIB','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,1872,2,1,1))
class _HwPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HwPartNumber_Type.__name__=_G
_HwPartNumber_Object=MibScalar
hwPartNumber=_HwPartNumber_Object((1,3,6,1,4,1,1872,2,1,1,1),_HwPartNumber_Type())
hwPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPartNumber.setStatus(_A)
class _HwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HwRevision_Type.__name__=_G
_HwRevision_Object=MibScalar
hwRevision=_HwRevision_Object((1,3,6,1,4,1,1872,2,1,1,2),_HwRevision_Type())
hwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRevision.setStatus(_A)
class _HwPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('bad',2)))
_HwPowerSupplyStatus_Type.__name__=_C
_HwPowerSupplyStatus_Object=MibScalar
hwPowerSupplyStatus=_HwPowerSupplyStatus_Object((1,3,6,1,4,1,1872,2,1,1,3),_HwPowerSupplyStatus_Type())
hwPowerSupplyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwPowerSupplyStatus.setStatus(_A)
class _HwRedundantPSPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_R,3),('present',4)))
_HwRedundantPSPresent_Type.__name__=_C
_HwRedundantPSPresent_Object=MibScalar
hwRedundantPSPresent=_HwRedundantPSPresent_Object((1,3,6,1,4,1,1872,2,1,1,4),_HwRedundantPSPresent_Type())
hwRedundantPSPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRedundantPSPresent.setStatus(_A)
class _HwRedundantPSStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('bad',2),(_R,3)))
_HwRedundantPSStatus_Type.__name__=_C
_HwRedundantPSStatus_Object=MibScalar
hwRedundantPSStatus=_HwRedundantPSStatus_Object((1,3,6,1,4,1,1872,2,1,1,5),_HwRedundantPSStatus_Type())
hwRedundantPSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRedundantPSStatus.setStatus(_A)
_HwSensor1Temp_Type=Integer32
_HwSensor1Temp_Object=MibScalar
hwSensor1Temp=_HwSensor1Temp_Object((1,3,6,1,4,1,1872,2,1,1,6),_HwSensor1Temp_Type())
hwSensor1Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:hwSensor1Temp.setStatus(_A)
_HwSensor2Temp_Type=Integer32
_HwSensor2Temp_Object=MibScalar
hwSensor2Temp=_HwSensor2Temp_Object((1,3,6,1,4,1,1872,2,1,1,7),_HwSensor2Temp_Type())
hwSensor2Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:hwSensor2Temp.setStatus(_A)
_HwSensor3Temp_Type=Integer32
_HwSensor3Temp_Object=MibScalar
hwSensor3Temp=_HwSensor3Temp_Object((1,3,6,1,4,1,1872,2,1,1,8),_HwSensor3Temp_Type())
hwSensor3Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:hwSensor3Temp.setStatus(_A)
_HwSensor4Temp_Type=Integer32
_HwSensor4Temp_Object=MibScalar
hwSensor4Temp=_HwSensor4Temp_Object((1,3,6,1,4,1,1872,2,1,1,9),_HwSensor4Temp_Type())
hwSensor4Temp.setMaxAccess(_B)
if mibBuilder.loadTexts:hwSensor4Temp.setStatus(_A)
_Agent_ObjectIdentity=ObjectIdentity
agent=_Agent_ObjectIdentity((1,3,6,1,4,1,1872,2,1,2))
_AgGeneral_ObjectIdentity=ObjectIdentity
agGeneral=_AgGeneral_ObjectIdentity((1,3,6,1,4,1,1872,2,1,2,1))
class _AgSaveConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('saveActive',2),('notSaveActive',3)))
_AgSaveConfiguration_Type.__name__=_C
_AgSaveConfiguration_Object=MibScalar
agSaveConfiguration=_AgSaveConfiguration_Object((1,3,6,1,4,1,1872,2,1,2,1,1),_AgSaveConfiguration_Type())
agSaveConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:agSaveConfiguration.setStatus(_A)
class _AgApplyConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('apply',2)))
_AgApplyConfiguration_Type.__name__=_C
_AgApplyConfiguration_Object=MibScalar
agApplyConfiguration=_AgApplyConfiguration_Object((1,3,6,1,4,1,1872,2,1,2,1,2),_AgApplyConfiguration_Type())
agApplyConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:agApplyConfiguration.setStatus(_A)
class _AgApplyPending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('applyNeeded',2),('noApplyNeeded',3)))
_AgApplyPending_Type.__name__=_C
_AgApplyPending_Object=MibScalar
agApplyPending=_AgApplyPending_Object((1,3,6,1,4,1,1872,2,1,2,1,3),_AgApplyPending_Type())
agApplyPending.setMaxAccess(_B)
if mibBuilder.loadTexts:agApplyPending.setStatus(_A)
class _AgReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('coldReset',2),('warmReset',3)))
_AgReset_Type.__name__=_C
_AgReset_Object=MibScalar
agReset=_AgReset_Object((1,3,6,1,4,1,1872,2,1,2,1,4),_AgReset_Type())
agReset.setMaxAccess(_D)
if mibBuilder.loadTexts:agReset.setStatus(_A)
class _AgConfigForNxtReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('active',2),('backup',3),('default',4)))
_AgConfigForNxtReset_Type.__name__=_C
_AgConfigForNxtReset_Object=MibScalar
agConfigForNxtReset=_AgConfigForNxtReset_Object((1,3,6,1,4,1,1872,2,1,2,1,5),_AgConfigForNxtReset_Type())
agConfigForNxtReset.setMaxAccess(_D)
if mibBuilder.loadTexts:agConfigForNxtReset.setStatus(_A)
class _AgImageForNxtReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_T,3)))
_AgImageForNxtReset_Type.__name__=_C
_AgImageForNxtReset_Object=MibScalar
agImageForNxtReset=_AgImageForNxtReset_Object((1,3,6,1,4,1,1872,2,1,2,1,6),_AgImageForNxtReset_Type())
agImageForNxtReset.setMaxAccess(_D)
if mibBuilder.loadTexts:agImageForNxtReset.setStatus(_A)
class _AgSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgSoftwareVersion_Type.__name__=_G
_AgSoftwareVersion_Object=MibScalar
agSoftwareVersion=_AgSoftwareVersion_Object((1,3,6,1,4,1,1872,2,1,2,1,7),_AgSoftwareVersion_Type())
agSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agSoftwareVersion.setStatus(_A)
class _AgBootVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgBootVer_Type.__name__=_G
_AgBootVer_Object=MibScalar
agBootVer=_AgBootVer_Object((1,3,6,1,4,1,1872,2,1,2,1,8),_AgBootVer_Type())
agBootVer.setMaxAccess(_B)
if mibBuilder.loadTexts:agBootVer.setStatus(_A)
class _AgImage1Ver_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgImage1Ver_Type.__name__=_G
_AgImage1Ver_Object=MibScalar
agImage1Ver=_AgImage1Ver_Object((1,3,6,1,4,1,1872,2,1,2,1,9),_AgImage1Ver_Type())
agImage1Ver.setMaxAccess(_B)
if mibBuilder.loadTexts:agImage1Ver.setStatus(_A)
class _AgImage2Ver_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgImage2Ver_Type.__name__=_G
_AgImage2Ver_Object=MibScalar
agImage2Ver=_AgImage2Ver_Object((1,3,6,1,4,1,1872,2,1,2,1,10),_AgImage2Ver_Type())
agImage2Ver.setMaxAccess(_B)
if mibBuilder.loadTexts:agImage2Ver.setStatus(_A)
class _AgRtcDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgRtcDate_Type.__name__=_G
_AgRtcDate_Object=MibScalar
agRtcDate=_AgRtcDate_Object((1,3,6,1,4,1,1872,2,1,2,1,11),_AgRtcDate_Type())
agRtcDate.setMaxAccess(_D)
if mibBuilder.loadTexts:agRtcDate.setStatus(_A)
class _AgRtcTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AgRtcTime_Type.__name__=_G
_AgRtcTime_Object=MibScalar
agRtcTime=_AgRtcTime_Object((1,3,6,1,4,1,1872,2,1,2,1,12),_AgRtcTime_Type())
agRtcTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agRtcTime.setStatus(_A)
_AgTftpServerIpAddr_Type=IpAddress
_AgTftpServerIpAddr_Object=MibScalar
agTftpServerIpAddr=_AgTftpServerIpAddr_Object((1,3,6,1,4,1,1872,2,1,2,1,13),_AgTftpServerIpAddr_Type())
agTftpServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpServerIpAddr.setStatus(_A)
class _AgTftpImageFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgTftpImageFileName_Type.__name__=_G
_AgTftpImageFileName_Object=MibScalar
agTftpImageFileName=_AgTftpImageFileName_Object((1,3,6,1,4,1,1872,2,1,2,1,14),_AgTftpImageFileName_Type())
agTftpImageFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpImageFileName.setStatus(_A)
class _AgTftpImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_S,2),(_T,3)))
_AgTftpImage_Type.__name__=_C
_AgTftpImage_Object=MibScalar
agTftpImage=_AgTftpImage_Object((1,3,6,1,4,1,1872,2,1,2,1,15),_AgTftpImage_Type())
agTftpImage.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpImage.setStatus(_A)
class _AgTftpDownload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('download',2)))
_AgTftpDownload_Type.__name__=_C
_AgTftpDownload_Object=MibScalar
agTftpDownload=_AgTftpDownload_Object((1,3,6,1,4,1,1872,2,1,2,1,16),_AgTftpDownload_Type())
agTftpDownload.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpDownload.setStatus(_A)
class _AgLastSetErrorReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AgLastSetErrorReason_Type.__name__=_G
_AgLastSetErrorReason_Object=MibScalar
agLastSetErrorReason=_AgLastSetErrorReason_Object((1,3,6,1,4,1,1872,2,1,2,1,17),_AgLastSetErrorReason_Type())
agLastSetErrorReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agLastSetErrorReason.setStatus(_A)
class _AgTftpServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgTftpServer_Type.__name__=_G
_AgTftpServer_Object=MibScalar
agTftpServer=_AgTftpServer_Object((1,3,6,1,4,1,1872,2,1,2,1,18),_AgTftpServer_Type())
agTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpServer.setStatus(_A)
class _AgTftpCfgFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgTftpCfgFileName_Type.__name__=_G
_AgTftpCfgFileName_Object=MibScalar
agTftpCfgFileName=_AgTftpCfgFileName_Object((1,3,6,1,4,1,1872,2,1,2,1,19),_AgTftpCfgFileName_Type())
agTftpCfgFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpCfgFileName.setStatus(_A)
class _AgTftpDumpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgTftpDumpFileName_Type.__name__=_G
_AgTftpDumpFileName_Object=MibScalar
agTftpDumpFileName=_AgTftpDumpFileName_Object((1,3,6,1,4,1,1872,2,1,2,1,20),_AgTftpDumpFileName_Type())
agTftpDumpFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpDumpFileName.setStatus(_A)
class _AgTftpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('img-get',2),('cfg-get',3),('cfg-put',4),('dump-put',5)))
_AgTftpAction_Type.__name__=_C
_AgTftpAction_Object=MibScalar
agTftpAction=_AgTftpAction_Object((1,3,6,1,4,1,1872,2,1,2,1,21),_AgTftpAction_Type())
agTftpAction.setMaxAccess(_D)
if mibBuilder.loadTexts:agTftpAction.setStatus(_A)
class _AgTftpLastActionStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgTftpLastActionStatus_Type.__name__=_G
_AgTftpLastActionStatus_Object=MibScalar
agTftpLastActionStatus=_AgTftpLastActionStatus_Object((1,3,6,1,4,1,1872,2,1,2,1,22),_AgTftpLastActionStatus_Type())
agTftpLastActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agTftpLastActionStatus.setStatus(_A)
class _AgRevert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('revert',2)))
_AgRevert_Type.__name__=_C
_AgRevert_Object=MibScalar
agRevert=_AgRevert_Object((1,3,6,1,4,1,1872,2,1,2,1,23),_AgRevert_Type())
agRevert.setMaxAccess(_D)
if mibBuilder.loadTexts:agRevert.setStatus(_A)
class _AgRevertApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('revertApply',2)))
_AgRevertApply_Type.__name__=_C
_AgRevertApply_Object=MibScalar
agRevertApply=_AgRevertApply_Object((1,3,6,1,4,1,1872,2,1,2,1,24),_AgRevertApply_Type())
agRevertApply.setMaxAccess(_D)
if mibBuilder.loadTexts:agRevertApply.setStatus(_A)
_AgEnabledSwFeatures_Type=DisplayString
_AgEnabledSwFeatures_Object=MibScalar
agEnabledSwFeatures=_AgEnabledSwFeatures_Object((1,3,6,1,4,1,1872,2,1,2,1,25),_AgEnabledSwFeatures_Type())
agEnabledSwFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:agEnabledSwFeatures.setStatus(_A)
class _AgClrSyslogMsgs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('reset',2)))
_AgClrSyslogMsgs_Type.__name__=_C
_AgClrSyslogMsgs_Object=MibScalar
agClrSyslogMsgs=_AgClrSyslogMsgs_Object((1,3,6,1,4,1,1872,2,1,2,1,26),_AgClrSyslogMsgs_Type())
agClrSyslogMsgs.setMaxAccess(_D)
if mibBuilder.loadTexts:agClrSyslogMsgs.setStatus(_A)
class _AgSavePending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saveNeeded',1),('noSaveNeeded',2)))
_AgSavePending_Type.__name__=_C
_AgSavePending_Object=MibScalar
agSavePending=_AgSavePending_Object((1,3,6,1,4,1,1872,2,1,2,1,27),_AgSavePending_Type())
agSavePending.setMaxAccess(_B)
if mibBuilder.loadTexts:agSavePending.setStatus(_A)
class _AgEnabledGslbKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgEnabledGslbKey_Type.__name__=_C
_AgEnabledGslbKey_Object=MibScalar
agEnabledGslbKey=_AgEnabledGslbKey_Object((1,3,6,1,4,1,1872,2,1,2,1,28),_AgEnabledGslbKey_Type())
agEnabledGslbKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agEnabledGslbKey.setStatus(_A)
class _AgEnabledBwmKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgEnabledBwmKey_Type.__name__=_C
_AgEnabledBwmKey_Object=MibScalar
agEnabledBwmKey=_AgEnabledBwmKey_Object((1,3,6,1,4,1,1872,2,1,2,1,29),_AgEnabledBwmKey_Type())
agEnabledBwmKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agEnabledBwmKey.setStatus(_A)
class _AgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AgSlotNumber_Type.__name__=_C
_AgSlotNumber_Object=MibScalar
agSlotNumber=_AgSlotNumber_Object((1,3,6,1,4,1,1872,2,1,2,1,30),_AgSlotNumber_Type())
agSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:agSlotNumber.setStatus(_A)
class _AgEnabledRurlKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgEnabledRurlKey_Type.__name__=_C
_AgEnabledRurlKey_Object=MibScalar
agEnabledRurlKey=_AgEnabledRurlKey_Object((1,3,6,1,4,1,1872,2,1,2,1,31),_AgEnabledRurlKey_Type())
agEnabledRurlKey.setMaxAccess(_B)
if mibBuilder.loadTexts:agEnabledRurlKey.setStatus(_A)
_AgGeneralConfig_ObjectIdentity=ObjectIdentity
agGeneralConfig=_AgGeneralConfig_ObjectIdentity((1,3,6,1,4,1,1872,2,1,2,2))
_AgNewCfgSyslogHost_Type=IpAddress
_AgNewCfgSyslogHost_Object=MibScalar
agNewCfgSyslogHost=_AgNewCfgSyslogHost_Object((1,3,6,1,4,1,1872,2,1,2,2,1),_AgNewCfgSyslogHost_Type())
agNewCfgSyslogHost.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogHost.setStatus(_A)
_AgCurCfgSyslogHost_Type=IpAddress
_AgCurCfgSyslogHost_Object=MibScalar
agCurCfgSyslogHost=_AgCurCfgSyslogHost_Object((1,3,6,1,4,1,1872,2,1,2,2,2),_AgCurCfgSyslogHost_Type())
agCurCfgSyslogHost.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogHost.setStatus(_A)
class _AgNewCfgBootp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_AgNewCfgBootp_Type.__name__=_C
_AgNewCfgBootp_Object=MibScalar
agNewCfgBootp=_AgNewCfgBootp_Object((1,3,6,1,4,1,1872,2,1,2,2,3),_AgNewCfgBootp_Type())
agNewCfgBootp.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgBootp.setStatus(_A)
class _AgCurCfgBootp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_AgCurCfgBootp_Type.__name__=_C
_AgCurCfgBootp_Object=MibScalar
agCurCfgBootp=_AgCurCfgBootp_Object((1,3,6,1,4,1,1872,2,1,2,2,4),_AgCurCfgBootp_Type())
agCurCfgBootp.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgBootp.setStatus(_A)
class _AgNewCfgSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('on',2),('off',3)))
_AgNewCfgSpanningTree_Type.__name__=_C
_AgNewCfgSpanningTree_Object=MibScalar
agNewCfgSpanningTree=_AgNewCfgSpanningTree_Object((1,3,6,1,4,1,1872,2,1,2,2,5),_AgNewCfgSpanningTree_Type())
agNewCfgSpanningTree.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSpanningTree.setStatus(_A)
class _AgCurCfgSpanningTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('on',2),('off',3)))
_AgCurCfgSpanningTree_Type.__name__=_C
_AgCurCfgSpanningTree_Object=MibScalar
agCurCfgSpanningTree=_AgCurCfgSpanningTree_Object((1,3,6,1,4,1,1872,2,1,2,2,6),_AgCurCfgSpanningTree_Type())
agCurCfgSpanningTree.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSpanningTree.setStatus(_A)
_AgTrapHostTableMaxEnt_Type=Integer32
_AgTrapHostTableMaxEnt_Object=MibScalar
agTrapHostTableMaxEnt=_AgTrapHostTableMaxEnt_Object((1,3,6,1,4,1,1872,2,1,2,2,7),_AgTrapHostTableMaxEnt_Type())
agTrapHostTableMaxEnt.setMaxAccess(_B)
if mibBuilder.loadTexts:agTrapHostTableMaxEnt.setStatus(_A)
_AgCurCfgTrapHostTable_Object=MibTable
agCurCfgTrapHostTable=_AgCurCfgTrapHostTable_Object((1,3,6,1,4,1,1872,2,1,2,2,8))
if mibBuilder.loadTexts:agCurCfgTrapHostTable.setStatus(_A)
_AgCurCfgTrapHostEntry_Object=MibTableRow
agCurCfgTrapHostEntry=_AgCurCfgTrapHostEntry_Object((1,3,6,1,4,1,1872,2,1,2,2,8,1))
agCurCfgTrapHostEntry.setIndexNames((0,_Q,_U))
if mibBuilder.loadTexts:agCurCfgTrapHostEntry.setStatus(_A)
class _AgCurCfgTrapHostIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgCurCfgTrapHostIndx_Type.__name__=_C
_AgCurCfgTrapHostIndx_Object=MibTableColumn
agCurCfgTrapHostIndx=_AgCurCfgTrapHostIndx_Object((1,3,6,1,4,1,1872,2,1,2,2,8,1,1),_AgCurCfgTrapHostIndx_Type())
agCurCfgTrapHostIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgTrapHostIndx.setStatus(_A)
_AgCurCfgTrapHostIpAddr_Type=IpAddress
_AgCurCfgTrapHostIpAddr_Object=MibTableColumn
agCurCfgTrapHostIpAddr=_AgCurCfgTrapHostIpAddr_Object((1,3,6,1,4,1,1872,2,1,2,2,8,1,2),_AgCurCfgTrapHostIpAddr_Type())
agCurCfgTrapHostIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgTrapHostIpAddr.setStatus(_A)
class _AgCurCfgTrapHostCommString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgCurCfgTrapHostCommString_Type.__name__=_G
_AgCurCfgTrapHostCommString_Object=MibTableColumn
agCurCfgTrapHostCommString=_AgCurCfgTrapHostCommString_Object((1,3,6,1,4,1,1872,2,1,2,2,8,1,3),_AgCurCfgTrapHostCommString_Type())
agCurCfgTrapHostCommString.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgTrapHostCommString.setStatus(_A)
_AgNewCfgTrapHostTable_Object=MibTable
agNewCfgTrapHostTable=_AgNewCfgTrapHostTable_Object((1,3,6,1,4,1,1872,2,1,2,2,9))
if mibBuilder.loadTexts:agNewCfgTrapHostTable.setStatus(_A)
_AgNewCfgTrapHostEntry_Object=MibTableRow
agNewCfgTrapHostEntry=_AgNewCfgTrapHostEntry_Object((1,3,6,1,4,1,1872,2,1,2,2,9,1))
agNewCfgTrapHostEntry.setIndexNames((0,_Q,_V))
if mibBuilder.loadTexts:agNewCfgTrapHostEntry.setStatus(_A)
class _AgNewCfgTrapHostIndx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgNewCfgTrapHostIndx_Type.__name__=_C
_AgNewCfgTrapHostIndx_Object=MibTableColumn
agNewCfgTrapHostIndx=_AgNewCfgTrapHostIndx_Object((1,3,6,1,4,1,1872,2,1,2,2,9,1,1),_AgNewCfgTrapHostIndx_Type())
agNewCfgTrapHostIndx.setMaxAccess(_B)
if mibBuilder.loadTexts:agNewCfgTrapHostIndx.setStatus(_A)
_AgNewCfgTrapHostIpAddr_Type=IpAddress
_AgNewCfgTrapHostIpAddr_Object=MibTableColumn
agNewCfgTrapHostIpAddr=_AgNewCfgTrapHostIpAddr_Object((1,3,6,1,4,1,1872,2,1,2,2,9,1,2),_AgNewCfgTrapHostIpAddr_Type())
agNewCfgTrapHostIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgTrapHostIpAddr.setStatus(_A)
class _AgNewCfgTrapHostCommString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgNewCfgTrapHostCommString_Type.__name__=_G
_AgNewCfgTrapHostCommString_Object=MibTableColumn
agNewCfgTrapHostCommString=_AgNewCfgTrapHostCommString_Object((1,3,6,1,4,1,1872,2,1,2,2,9,1,3),_AgNewCfgTrapHostCommString_Type())
agNewCfgTrapHostCommString.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgTrapHostCommString.setStatus(_A)
class _AgCurCfgHttpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgCurCfgHttpServerPort_Type.__name__=_C
_AgCurCfgHttpServerPort_Object=MibScalar
agCurCfgHttpServerPort=_AgCurCfgHttpServerPort_Object((1,3,6,1,4,1,1872,2,1,2,2,10),_AgCurCfgHttpServerPort_Type())
agCurCfgHttpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgHttpServerPort.setStatus(_A)
class _AgNewCfgHttpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgNewCfgHttpServerPort_Type.__name__=_C
_AgNewCfgHttpServerPort_Object=MibScalar
agNewCfgHttpServerPort=_AgNewCfgHttpServerPort_Object((1,3,6,1,4,1,1872,2,1,2,2,11),_AgNewCfgHttpServerPort_Type())
agNewCfgHttpServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgHttpServerPort.setStatus(_A)
class _AgCurCfgLoginBanner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_AgCurCfgLoginBanner_Type.__name__=_G
_AgCurCfgLoginBanner_Object=MibScalar
agCurCfgLoginBanner=_AgCurCfgLoginBanner_Object((1,3,6,1,4,1,1872,2,1,2,2,12),_AgCurCfgLoginBanner_Type())
agCurCfgLoginBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgLoginBanner.setStatus(_A)
class _AgNewCfgLoginBanner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_AgNewCfgLoginBanner_Type.__name__=_G
_AgNewCfgLoginBanner_Object=MibScalar
agNewCfgLoginBanner=_AgNewCfgLoginBanner_Object((1,3,6,1,4,1,1872,2,1,2,2,13),_AgNewCfgLoginBanner_Type())
agNewCfgLoginBanner.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgLoginBanner.setStatus(_A)
_AgNewCfgSyslog2Host_Type=IpAddress
_AgNewCfgSyslog2Host_Object=MibScalar
agNewCfgSyslog2Host=_AgNewCfgSyslog2Host_Object((1,3,6,1,4,1,1872,2,1,2,2,14),_AgNewCfgSyslog2Host_Type())
agNewCfgSyslog2Host.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslog2Host.setStatus(_A)
_AgCurCfgSyslog2Host_Type=IpAddress
_AgCurCfgSyslog2Host_Object=MibScalar
agCurCfgSyslog2Host=_AgCurCfgSyslog2Host_Object((1,3,6,1,4,1,1872,2,1,2,2,15),_AgCurCfgSyslog2Host_Type())
agCurCfgSyslog2Host.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslog2Host.setStatus(_A)
class _AgCurCfgSyslogFac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_AgCurCfgSyslogFac_Type.__name__=_C
_AgCurCfgSyslogFac_Object=MibScalar
agCurCfgSyslogFac=_AgCurCfgSyslogFac_Object((1,3,6,1,4,1,1872,2,1,2,2,16),_AgCurCfgSyslogFac_Type())
agCurCfgSyslogFac.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogFac.setStatus(_A)
class _AgNewCfgSyslogFac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_AgNewCfgSyslogFac_Type.__name__=_C
_AgNewCfgSyslogFac_Object=MibScalar
agNewCfgSyslogFac=_AgNewCfgSyslogFac_Object((1,3,6,1,4,1,1872,2,1,2,2,17),_AgNewCfgSyslogFac_Type())
agNewCfgSyslogFac.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogFac.setStatus(_A)
class _AgCurCfgSyslog2Fac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_AgCurCfgSyslog2Fac_Type.__name__=_C
_AgCurCfgSyslog2Fac_Object=MibScalar
agCurCfgSyslog2Fac=_AgCurCfgSyslog2Fac_Object((1,3,6,1,4,1,1872,2,1,2,2,18),_AgCurCfgSyslog2Fac_Type())
agCurCfgSyslog2Fac.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslog2Fac.setStatus(_A)
class _AgNewCfgSyslog2Fac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8)))
_AgNewCfgSyslog2Fac_Type.__name__=_C
_AgNewCfgSyslog2Fac_Object=MibScalar
agNewCfgSyslog2Fac=_AgNewCfgSyslog2Fac_Object((1,3,6,1,4,1,1872,2,1,2,2,19),_AgNewCfgSyslog2Fac_Type())
agNewCfgSyslog2Fac.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslog2Fac.setStatus(_A)
class _AgCurCfgSmtpHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AgCurCfgSmtpHost_Type.__name__=_G
_AgCurCfgSmtpHost_Object=MibScalar
agCurCfgSmtpHost=_AgCurCfgSmtpHost_Object((1,3,6,1,4,1,1872,2,1,2,2,20),_AgCurCfgSmtpHost_Type())
agCurCfgSmtpHost.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSmtpHost.setStatus(_A)
class _AgNewCfgSmtpHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AgNewCfgSmtpHost_Type.__name__=_G
_AgNewCfgSmtpHost_Object=MibScalar
agNewCfgSmtpHost=_AgNewCfgSmtpHost_Object((1,3,6,1,4,1,1872,2,1,2,2,21),_AgNewCfgSmtpHost_Type())
agNewCfgSmtpHost.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSmtpHost.setStatus(_A)
class _AgCurCfgConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgConsole_Type.__name__=_C
_AgCurCfgConsole_Object=MibScalar
agCurCfgConsole=_AgCurCfgConsole_Object((1,3,6,1,4,1,1872,2,1,2,2,22),_AgCurCfgConsole_Type())
agCurCfgConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgConsole.setStatus(_A)
class _AgNewCfgConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgConsole_Type.__name__=_C
_AgNewCfgConsole_Object=MibScalar
agNewCfgConsole=_AgNewCfgConsole_Object((1,3,6,1,4,1,1872,2,1,2,2,23),_AgNewCfgConsole_Type())
agNewCfgConsole.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgConsole.setStatus(_A)
_AgCurCfgMgmtNetwork_Type=IpAddress
_AgCurCfgMgmtNetwork_Object=MibScalar
agCurCfgMgmtNetwork=_AgCurCfgMgmtNetwork_Object((1,3,6,1,4,1,1872,2,1,2,2,24),_AgCurCfgMgmtNetwork_Type())
agCurCfgMgmtNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgMgmtNetwork.setStatus(_A)
_AgNewCfgMgmtNetwork_Type=IpAddress
_AgNewCfgMgmtNetwork_Object=MibScalar
agNewCfgMgmtNetwork=_AgNewCfgMgmtNetwork_Object((1,3,6,1,4,1,1872,2,1,2,2,25),_AgNewCfgMgmtNetwork_Type())
agNewCfgMgmtNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgMgmtNetwork.setStatus(_A)
_AgCurCfgMgmtMask_Type=IpAddress
_AgCurCfgMgmtMask_Object=MibScalar
agCurCfgMgmtMask=_AgCurCfgMgmtMask_Object((1,3,6,1,4,1,1872,2,1,2,2,26),_AgCurCfgMgmtMask_Type())
agCurCfgMgmtMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgMgmtMask.setStatus(_A)
_AgNewCfgMgmtMask_Type=IpAddress
_AgNewCfgMgmtMask_Object=MibScalar
agNewCfgMgmtMask=_AgNewCfgMgmtMask_Object((1,3,6,1,4,1,1872,2,1,2,2,27),_AgNewCfgMgmtMask_Type())
agNewCfgMgmtMask.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgMgmtMask.setStatus(_A)
_AgNTP_ObjectIdentity=ObjectIdentity
agNTP=_AgNTP_ObjectIdentity((1,3,6,1,4,1,1872,2,1,2,2,28))
_AgCurCfgNTPServer_Type=IpAddress
_AgCurCfgNTPServer_Object=MibScalar
agCurCfgNTPServer=_AgCurCfgNTPServer_Object((1,3,6,1,4,1,1872,2,1,2,2,28,1),_AgCurCfgNTPServer_Type())
agCurCfgNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgNTPServer.setStatus(_A)
_AgNewCfgNTPServer_Type=IpAddress
_AgNewCfgNTPServer_Object=MibScalar
agNewCfgNTPServer=_AgNewCfgNTPServer_Object((1,3,6,1,4,1,1872,2,1,2,2,28,2),_AgNewCfgNTPServer_Type())
agNewCfgNTPServer.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgNTPServer.setStatus(_A)
class _AgCurCfgNTPResyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2880))
_AgCurCfgNTPResyncInterval_Type.__name__=_C
_AgCurCfgNTPResyncInterval_Object=MibScalar
agCurCfgNTPResyncInterval=_AgCurCfgNTPResyncInterval_Object((1,3,6,1,4,1,1872,2,1,2,2,28,3),_AgCurCfgNTPResyncInterval_Type())
agCurCfgNTPResyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgNTPResyncInterval.setStatus(_A)
class _AgNewCfgNTPResyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2880))
_AgNewCfgNTPResyncInterval_Type.__name__=_C
_AgNewCfgNTPResyncInterval_Object=MibScalar
agNewCfgNTPResyncInterval=_AgNewCfgNTPResyncInterval_Object((1,3,6,1,4,1,1872,2,1,2,2,28,4),_AgNewCfgNTPResyncInterval_Type())
agNewCfgNTPResyncInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgNTPResyncInterval.setStatus(_A)
class _AgCurCfgNTPTzone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_AgCurCfgNTPTzone_Type.__name__=_G
_AgCurCfgNTPTzone_Object=MibScalar
agCurCfgNTPTzone=_AgCurCfgNTPTzone_Object((1,3,6,1,4,1,1872,2,1,2,2,28,5),_AgCurCfgNTPTzone_Type())
agCurCfgNTPTzone.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgNTPTzone.setStatus(_A)
class _AgNewCfgNTPTzone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_AgNewCfgNTPTzone_Type.__name__=_G
_AgNewCfgNTPTzone_Object=MibScalar
agNewCfgNTPTzone=_AgNewCfgNTPTzone_Object((1,3,6,1,4,1,1872,2,1,2,2,28,6),_AgNewCfgNTPTzone_Type())
agNewCfgNTPTzone.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgNTPTzone.setStatus(_A)
class _AgCurCfgNTPDlight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgNTPDlight_Type.__name__=_C
_AgCurCfgNTPDlight_Object=MibScalar
agCurCfgNTPDlight=_AgCurCfgNTPDlight_Object((1,3,6,1,4,1,1872,2,1,2,2,28,7),_AgCurCfgNTPDlight_Type())
agCurCfgNTPDlight.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgNTPDlight.setStatus(_A)
class _AgNewCfgNTPDlight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgNTPDlight_Type.__name__=_C
_AgNewCfgNTPDlight_Object=MibScalar
agNewCfgNTPDlight=_AgNewCfgNTPDlight_Object((1,3,6,1,4,1,1872,2,1,2,2,28,8),_AgNewCfgNTPDlight_Type())
agNewCfgNTPDlight.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgNTPDlight.setStatus(_A)
class _AgCurCfgNTPService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgNTPService_Type.__name__=_C
_AgCurCfgNTPService_Object=MibScalar
agCurCfgNTPService=_AgCurCfgNTPService_Object((1,3,6,1,4,1,1872,2,1,2,2,28,9),_AgCurCfgNTPService_Type())
agCurCfgNTPService.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgNTPService.setStatus(_A)
class _AgNewCfgNTPService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgNTPService_Type.__name__=_C
_AgNewCfgNTPService_Object=MibScalar
agNewCfgNTPService=_AgNewCfgNTPService_Object((1,3,6,1,4,1,1872,2,1,2,2,28,10),_AgNewCfgNTPService_Type())
agNewCfgNTPService.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgNTPService.setStatus(_A)
_AgLog_ObjectIdentity=ObjectIdentity
agLog=_AgLog_ObjectIdentity((1,3,6,1,4,1,1872,2,1,2,2,29))
class _AgNewCfgSyslogTrapConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapConsole_Type.__name__=_C
_AgNewCfgSyslogTrapConsole_Object=MibScalar
agNewCfgSyslogTrapConsole=_AgNewCfgSyslogTrapConsole_Object((1,3,6,1,4,1,1872,2,1,2,2,29,1),_AgNewCfgSyslogTrapConsole_Type())
agNewCfgSyslogTrapConsole.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapConsole.setStatus(_A)
class _AgCurCfgSyslogTrapConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapConsole_Type.__name__=_C
_AgCurCfgSyslogTrapConsole_Object=MibScalar
agCurCfgSyslogTrapConsole=_AgCurCfgSyslogTrapConsole_Object((1,3,6,1,4,1,1872,2,1,2,2,29,2),_AgCurCfgSyslogTrapConsole_Type())
agCurCfgSyslogTrapConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapConsole.setStatus(_A)
class _AgNewCfgSyslogTrapSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapSystem_Type.__name__=_C
_AgNewCfgSyslogTrapSystem_Object=MibScalar
agNewCfgSyslogTrapSystem=_AgNewCfgSyslogTrapSystem_Object((1,3,6,1,4,1,1872,2,1,2,2,29,3),_AgNewCfgSyslogTrapSystem_Type())
agNewCfgSyslogTrapSystem.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapSystem.setStatus(_A)
class _AgCurCfgSyslogTrapSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapSystem_Type.__name__=_C
_AgCurCfgSyslogTrapSystem_Object=MibScalar
agCurCfgSyslogTrapSystem=_AgCurCfgSyslogTrapSystem_Object((1,3,6,1,4,1,1872,2,1,2,2,29,4),_AgCurCfgSyslogTrapSystem_Type())
agCurCfgSyslogTrapSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapSystem.setStatus(_A)
class _AgNewCfgSyslogTrapMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapMgmt_Type.__name__=_C
_AgNewCfgSyslogTrapMgmt_Object=MibScalar
agNewCfgSyslogTrapMgmt=_AgNewCfgSyslogTrapMgmt_Object((1,3,6,1,4,1,1872,2,1,2,2,29,5),_AgNewCfgSyslogTrapMgmt_Type())
agNewCfgSyslogTrapMgmt.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapMgmt.setStatus(_A)
class _AgCurCfgSyslogTrapMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapMgmt_Type.__name__=_C
_AgCurCfgSyslogTrapMgmt_Object=MibScalar
agCurCfgSyslogTrapMgmt=_AgCurCfgSyslogTrapMgmt_Object((1,3,6,1,4,1,1872,2,1,2,2,29,6),_AgCurCfgSyslogTrapMgmt_Type())
agCurCfgSyslogTrapMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapMgmt.setStatus(_A)
class _AgNewCfgSyslogTrapCli_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapCli_Type.__name__=_C
_AgNewCfgSyslogTrapCli_Object=MibScalar
agNewCfgSyslogTrapCli=_AgNewCfgSyslogTrapCli_Object((1,3,6,1,4,1,1872,2,1,2,2,29,7),_AgNewCfgSyslogTrapCli_Type())
agNewCfgSyslogTrapCli.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapCli.setStatus(_A)
class _AgCurCfgSyslogTrapCli_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapCli_Type.__name__=_C
_AgCurCfgSyslogTrapCli_Object=MibScalar
agCurCfgSyslogTrapCli=_AgCurCfgSyslogTrapCli_Object((1,3,6,1,4,1,1872,2,1,2,2,29,8),_AgCurCfgSyslogTrapCli_Type())
agCurCfgSyslogTrapCli.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapCli.setStatus(_A)
class _AgNewCfgSyslogTrapStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapStp_Type.__name__=_C
_AgNewCfgSyslogTrapStp_Object=MibScalar
agNewCfgSyslogTrapStp=_AgNewCfgSyslogTrapStp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,9),_AgNewCfgSyslogTrapStp_Type())
agNewCfgSyslogTrapStp.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapStp.setStatus(_A)
class _AgCurCfgSyslogTrapStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapStp_Type.__name__=_C
_AgCurCfgSyslogTrapStp_Object=MibScalar
agCurCfgSyslogTrapStp=_AgCurCfgSyslogTrapStp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,10),_AgCurCfgSyslogTrapStp_Type())
agCurCfgSyslogTrapStp.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapStp.setStatus(_A)
class _AgNewCfgSyslogTrapVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapVlan_Type.__name__=_C
_AgNewCfgSyslogTrapVlan_Object=MibScalar
agNewCfgSyslogTrapVlan=_AgNewCfgSyslogTrapVlan_Object((1,3,6,1,4,1,1872,2,1,2,2,29,11),_AgNewCfgSyslogTrapVlan_Type())
agNewCfgSyslogTrapVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapVlan.setStatus(_A)
class _AgCurCfgSyslogTrapVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapVlan_Type.__name__=_C
_AgCurCfgSyslogTrapVlan_Object=MibScalar
agCurCfgSyslogTrapVlan=_AgCurCfgSyslogTrapVlan_Object((1,3,6,1,4,1,1872,2,1,2,2,29,12),_AgCurCfgSyslogTrapVlan_Type())
agCurCfgSyslogTrapVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapVlan.setStatus(_A)
class _AgNewCfgSyslogTrapSlb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapSlb_Type.__name__=_C
_AgNewCfgSyslogTrapSlb_Object=MibScalar
agNewCfgSyslogTrapSlb=_AgNewCfgSyslogTrapSlb_Object((1,3,6,1,4,1,1872,2,1,2,2,29,13),_AgNewCfgSyslogTrapSlb_Type())
agNewCfgSyslogTrapSlb.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapSlb.setStatus(_A)
class _AgCurCfgSyslogTrapSlb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapSlb_Type.__name__=_C
_AgCurCfgSyslogTrapSlb_Object=MibScalar
agCurCfgSyslogTrapSlb=_AgCurCfgSyslogTrapSlb_Object((1,3,6,1,4,1,1872,2,1,2,2,29,14),_AgCurCfgSyslogTrapSlb_Type())
agCurCfgSyslogTrapSlb.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapSlb.setStatus(_A)
class _AgNewCfgSyslogTrapGslb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapGslb_Type.__name__=_C
_AgNewCfgSyslogTrapGslb_Object=MibScalar
agNewCfgSyslogTrapGslb=_AgNewCfgSyslogTrapGslb_Object((1,3,6,1,4,1,1872,2,1,2,2,29,15),_AgNewCfgSyslogTrapGslb_Type())
agNewCfgSyslogTrapGslb.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapGslb.setStatus(_A)
class _AgCurCfgSyslogTrapGslb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapGslb_Type.__name__=_C
_AgCurCfgSyslogTrapGslb_Object=MibScalar
agCurCfgSyslogTrapGslb=_AgCurCfgSyslogTrapGslb_Object((1,3,6,1,4,1,1872,2,1,2,2,29,16),_AgCurCfgSyslogTrapGslb_Type())
agCurCfgSyslogTrapGslb.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapGslb.setStatus(_A)
class _AgNewCfgSyslogTrapFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapFilter_Type.__name__=_C
_AgNewCfgSyslogTrapFilter_Object=MibScalar
agNewCfgSyslogTrapFilter=_AgNewCfgSyslogTrapFilter_Object((1,3,6,1,4,1,1872,2,1,2,2,29,17),_AgNewCfgSyslogTrapFilter_Type())
agNewCfgSyslogTrapFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapFilter.setStatus(_A)
class _AgCurCfgSyslogTrapFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapFilter_Type.__name__=_C
_AgCurCfgSyslogTrapFilter_Object=MibScalar
agCurCfgSyslogTrapFilter=_AgCurCfgSyslogTrapFilter_Object((1,3,6,1,4,1,1872,2,1,2,2,29,18),_AgCurCfgSyslogTrapFilter_Type())
agCurCfgSyslogTrapFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapFilter.setStatus(_A)
class _AgNewCfgSyslogTrapSsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapSsh_Type.__name__=_C
_AgNewCfgSyslogTrapSsh_Object=MibScalar
agNewCfgSyslogTrapSsh=_AgNewCfgSyslogTrapSsh_Object((1,3,6,1,4,1,1872,2,1,2,2,29,19),_AgNewCfgSyslogTrapSsh_Type())
agNewCfgSyslogTrapSsh.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapSsh.setStatus(_A)
class _AgCurCfgSyslogTrapSsh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapSsh_Type.__name__=_C
_AgCurCfgSyslogTrapSsh_Object=MibScalar
agCurCfgSyslogTrapSsh=_AgCurCfgSyslogTrapSsh_Object((1,3,6,1,4,1,1872,2,1,2,2,29,20),_AgCurCfgSyslogTrapSsh_Type())
agCurCfgSyslogTrapSsh.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapSsh.setStatus(_A)
class _AgNewCfgSyslogTrapVrrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapVrrp_Type.__name__=_C
_AgNewCfgSyslogTrapVrrp_Object=MibScalar
agNewCfgSyslogTrapVrrp=_AgNewCfgSyslogTrapVrrp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,21),_AgNewCfgSyslogTrapVrrp_Type())
agNewCfgSyslogTrapVrrp.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapVrrp.setStatus(_A)
class _AgCurCfgSyslogTrapVrrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapVrrp_Type.__name__=_C
_AgCurCfgSyslogTrapVrrp_Object=MibScalar
agCurCfgSyslogTrapVrrp=_AgCurCfgSyslogTrapVrrp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,22),_AgCurCfgSyslogTrapVrrp_Type())
agCurCfgSyslogTrapVrrp.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapVrrp.setStatus(_A)
class _AgNewCfgSyslogTrapBgp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapBgp_Type.__name__=_C
_AgNewCfgSyslogTrapBgp_Object=MibScalar
agNewCfgSyslogTrapBgp=_AgNewCfgSyslogTrapBgp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,23),_AgNewCfgSyslogTrapBgp_Type())
agNewCfgSyslogTrapBgp.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapBgp.setStatus(_A)
class _AgCurCfgSyslogTrapBgp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapBgp_Type.__name__=_C
_AgCurCfgSyslogTrapBgp_Object=MibScalar
agCurCfgSyslogTrapBgp=_AgCurCfgSyslogTrapBgp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,24),_AgCurCfgSyslogTrapBgp_Type())
agCurCfgSyslogTrapBgp.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapBgp.setStatus(_A)
class _AgNewCfgSyslogTrapNtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapNtp_Type.__name__=_C
_AgNewCfgSyslogTrapNtp_Object=MibScalar
agNewCfgSyslogTrapNtp=_AgNewCfgSyslogTrapNtp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,25),_AgNewCfgSyslogTrapNtp_Type())
agNewCfgSyslogTrapNtp.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapNtp.setStatus(_A)
class _AgCurCfgSyslogTrapNtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapNtp_Type.__name__=_C
_AgCurCfgSyslogTrapNtp_Object=MibScalar
agCurCfgSyslogTrapNtp=_AgCurCfgSyslogTrapNtp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,26),_AgCurCfgSyslogTrapNtp_Type())
agCurCfgSyslogTrapNtp.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapNtp.setStatus(_A)
class _AgNewCfgSyslogTrapIsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapIsd_Type.__name__=_C
_AgNewCfgSyslogTrapIsd_Object=MibScalar
agNewCfgSyslogTrapIsd=_AgNewCfgSyslogTrapIsd_Object((1,3,6,1,4,1,1872,2,1,2,2,29,27),_AgNewCfgSyslogTrapIsd_Type())
agNewCfgSyslogTrapIsd.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapIsd.setStatus(_A)
class _AgCurCfgSyslogTrapIsd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapIsd_Type.__name__=_C
_AgCurCfgSyslogTrapIsd_Object=MibScalar
agCurCfgSyslogTrapIsd=_AgCurCfgSyslogTrapIsd_Object((1,3,6,1,4,1,1872,2,1,2,2,29,28),_AgCurCfgSyslogTrapIsd_Type())
agCurCfgSyslogTrapIsd.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapIsd.setStatus(_A)
class _AgNewCfgSyslogTrapIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapIp_Type.__name__=_C
_AgNewCfgSyslogTrapIp_Object=MibScalar
agNewCfgSyslogTrapIp=_AgNewCfgSyslogTrapIp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,31),_AgNewCfgSyslogTrapIp_Type())
agNewCfgSyslogTrapIp.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapIp.setStatus(_A)
class _AgCurCfgSyslogTrapIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapIp_Type.__name__=_C
_AgCurCfgSyslogTrapIp_Object=MibScalar
agCurCfgSyslogTrapIp=_AgCurCfgSyslogTrapIp_Object((1,3,6,1,4,1,1872,2,1,2,2,29,32),_AgCurCfgSyslogTrapIp_Type())
agCurCfgSyslogTrapIp.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapIp.setStatus(_A)
class _AgNewCfgSyslogTrapWeb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapWeb_Type.__name__=_C
_AgNewCfgSyslogTrapWeb_Object=MibScalar
agNewCfgSyslogTrapWeb=_AgNewCfgSyslogTrapWeb_Object((1,3,6,1,4,1,1872,2,1,2,2,29,35),_AgNewCfgSyslogTrapWeb_Type())
agNewCfgSyslogTrapWeb.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapWeb.setStatus(_A)
class _AgCurCfgSyslogTrapWeb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapWeb_Type.__name__=_C
_AgCurCfgSyslogTrapWeb_Object=MibScalar
agCurCfgSyslogTrapWeb=_AgCurCfgSyslogTrapWeb_Object((1,3,6,1,4,1,1872,2,1,2,2,29,36),_AgCurCfgSyslogTrapWeb_Type())
agCurCfgSyslogTrapWeb.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapWeb.setStatus(_A)
class _AgNewCfgSyslogTrapSynAtk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapSynAtk_Type.__name__=_C
_AgNewCfgSyslogTrapSynAtk_Object=MibScalar
agNewCfgSyslogTrapSynAtk=_AgNewCfgSyslogTrapSynAtk_Object((1,3,6,1,4,1,1872,2,1,2,2,29,37),_AgNewCfgSyslogTrapSynAtk_Type())
agNewCfgSyslogTrapSynAtk.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapSynAtk.setStatus(_A)
class _AgCurCfgSyslogTrapSynAtk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapSynAtk_Type.__name__=_C
_AgCurCfgSyslogTrapSynAtk_Object=MibScalar
agCurCfgSyslogTrapSynAtk=_AgCurCfgSyslogTrapSynAtk_Object((1,3,6,1,4,1,1872,2,1,2,2,29,38),_AgCurCfgSyslogTrapSynAtk_Type())
agCurCfgSyslogTrapSynAtk.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapSynAtk.setStatus(_A)
class _AgNewCfgSyslogTrapTcpLim_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgNewCfgSyslogTrapTcpLim_Type.__name__=_C
_AgNewCfgSyslogTrapTcpLim_Object=MibScalar
agNewCfgSyslogTrapTcpLim=_AgNewCfgSyslogTrapTcpLim_Object((1,3,6,1,4,1,1872,2,1,2,2,29,39),_AgNewCfgSyslogTrapTcpLim_Type())
agNewCfgSyslogTrapTcpLim.setMaxAccess(_D)
if mibBuilder.loadTexts:agNewCfgSyslogTrapTcpLim.setStatus(_A)
class _AgCurCfgSyslogTrapTcpLim_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgCurCfgSyslogTrapTcpLim_Type.__name__=_C
_AgCurCfgSyslogTrapTcpLim_Object=MibScalar
agCurCfgSyslogTrapTcpLim=_AgCurCfgSyslogTrapTcpLim_Object((1,3,6,1,4,1,1872,2,1,2,2,29,40),_AgCurCfgSyslogTrapTcpLim_Type())
agCurCfgSyslogTrapTcpLim.setMaxAccess(_B)
if mibBuilder.loadTexts:agCurCfgSyslogTrapTcpLim.setStatus(_A)
_Stats_ObjectIdentity=ObjectIdentity
stats=_Stats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8))
_MemStats_ObjectIdentity=ObjectIdentity
memStats=_MemStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,12))
_MemStatsAllocs_Type=Counter32
_MemStatsAllocs_Object=MibScalar
memStatsAllocs=_MemStatsAllocs_Object((1,3,6,1,4,1,1872,2,1,8,12,1),_MemStatsAllocs_Type())
memStatsAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsAllocs.setStatus(_A)
_MemStatsFrees_Type=Counter32
_MemStatsFrees_Object=MibScalar
memStatsFrees=_MemStatsFrees_Object((1,3,6,1,4,1,1872,2,1,8,12,2),_MemStatsFrees_Type())
memStatsFrees.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsFrees.setStatus(_A)
_MemStatsAllocFails_Type=Counter32
_MemStatsAllocFails_Object=MibScalar
memStatsAllocFails=_MemStatsAllocFails_Object((1,3,6,1,4,1,1872,2,1,8,12,3),_MemStatsAllocFails_Type())
memStatsAllocFails.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsAllocFails.setStatus(_A)
_MemStatsBytesCurr_Type=Gauge32
_MemStatsBytesCurr_Object=MibScalar
memStatsBytesCurr=_MemStatsBytesCurr_Object((1,3,6,1,4,1,1872,2,1,8,12,4),_MemStatsBytesCurr_Type())
memStatsBytesCurr.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsBytesCurr.setStatus(_A)
_MemStatsBytesHiwat_Type=Gauge32
_MemStatsBytesHiwat_Object=MibScalar
memStatsBytesHiwat=_MemStatsBytesHiwat_Object((1,3,6,1,4,1,1872,2,1,8,12,5),_MemStatsBytesHiwat_Type())
memStatsBytesHiwat.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsBytesHiwat.setStatus(_A)
_MemStatsPoolBytes_Type=Gauge32
_MemStatsPoolBytes_Object=MibScalar
memStatsPoolBytes=_MemStatsPoolBytes_Object((1,3,6,1,4,1,1872,2,1,8,12,6),_MemStatsPoolBytes_Type())
memStatsPoolBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsPoolBytes.setStatus(_A)
_MemStatsLargest_Type=Gauge32
_MemStatsLargest_Object=MibScalar
memStatsLargest=_MemStatsLargest_Object((1,3,6,1,4,1,1872,2,1,8,12,7),_MemStatsLargest_Type())
memStatsLargest.setMaxAccess(_B)
if mibBuilder.loadTexts:memStatsLargest.setStatus(_A)
_PktStats_ObjectIdentity=ObjectIdentity
pktStats=_PktStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,13))
_PktStatsAllocs_Type=Counter32
_PktStatsAllocs_Object=MibScalar
pktStatsAllocs=_PktStatsAllocs_Object((1,3,6,1,4,1,1872,2,1,8,13,1),_PktStatsAllocs_Type())
pktStatsAllocs.setMaxAccess(_B)
if mibBuilder.loadTexts:pktStatsAllocs.setStatus(_A)
_PktStatsFrees_Type=Counter32
_PktStatsFrees_Object=MibScalar
pktStatsFrees=_PktStatsFrees_Object((1,3,6,1,4,1,1872,2,1,8,13,2),_PktStatsFrees_Type())
pktStatsFrees.setMaxAccess(_B)
if mibBuilder.loadTexts:pktStatsFrees.setStatus(_A)
_PktStatsAllocFails_Type=Counter32
_PktStatsAllocFails_Object=MibScalar
pktStatsAllocFails=_PktStatsAllocFails_Object((1,3,6,1,4,1,1872,2,1,8,13,3),_PktStatsAllocFails_Type())
pktStatsAllocFails.setMaxAccess(_B)
if mibBuilder.loadTexts:pktStatsAllocFails.setStatus(_A)
_PktStatsMediums_Type=Counter32
_PktStatsMediums_Object=MibScalar
pktStatsMediums=_PktStatsMediums_Object((1,3,6,1,4,1,1872,2,1,8,13,4),_PktStatsMediums_Type())
pktStatsMediums.setMaxAccess(_B)
if mibBuilder.loadTexts:pktStatsMediums.setStatus(_A)
_PktStatsJumbos_Type=Counter32
_PktStatsJumbos_Object=MibScalar
pktStatsJumbos=_PktStatsJumbos_Object((1,3,6,1,4,1,1872,2,1,8,13,5),_PktStatsJumbos_Type())
pktStatsJumbos.setMaxAccess(_B)
if mibBuilder.loadTexts:pktStatsJumbos.setStatus(_A)
_PktStatsSmalls_Type=Counter32
_PktStatsSmalls_Object=MibScalar
pktStatsSmalls=_PktStatsSmalls_Object((1,3,6,1,4,1,1872,2,1,8,13,6),_PktStatsSmalls_Type())
pktStatsSmalls.setMaxAccess(_B)
if mibBuilder.loadTexts:pktStatsSmalls.setStatus(_A)
_MpCpuStats_ObjectIdentity=ObjectIdentity
mpCpuStats=_MpCpuStats_ObjectIdentity((1,3,6,1,4,1,1872,2,1,8,16))
_MpCpuAStatsUtil1Second_Type=Integer32
_MpCpuAStatsUtil1Second_Object=MibScalar
mpCpuAStatsUtil1Second=_MpCpuAStatsUtil1Second_Object((1,3,6,1,4,1,1872,2,1,8,16,1),_MpCpuAStatsUtil1Second_Type())
mpCpuAStatsUtil1Second.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCpuAStatsUtil1Second.setStatus(_A)
_MpCpuBStatsUtil1Second_Type=Integer32
_MpCpuBStatsUtil1Second_Object=MibScalar
mpCpuBStatsUtil1Second=_MpCpuBStatsUtil1Second_Object((1,3,6,1,4,1,1872,2,1,8,16,2),_MpCpuBStatsUtil1Second_Type())
mpCpuBStatsUtil1Second.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCpuBStatsUtil1Second.setStatus(_A)
_MpCpuAStatsUtil4Seconds_Type=Integer32
_MpCpuAStatsUtil4Seconds_Object=MibScalar
mpCpuAStatsUtil4Seconds=_MpCpuAStatsUtil4Seconds_Object((1,3,6,1,4,1,1872,2,1,8,16,3),_MpCpuAStatsUtil4Seconds_Type())
mpCpuAStatsUtil4Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCpuAStatsUtil4Seconds.setStatus(_A)
_MpCpuBStatsUtil4Seconds_Type=Integer32
_MpCpuBStatsUtil4Seconds_Object=MibScalar
mpCpuBStatsUtil4Seconds=_MpCpuBStatsUtil4Seconds_Object((1,3,6,1,4,1,1872,2,1,8,16,4),_MpCpuBStatsUtil4Seconds_Type())
mpCpuBStatsUtil4Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCpuBStatsUtil4Seconds.setStatus(_A)
_MpCpuAStatsUtil64Seconds_Type=Integer32
_MpCpuAStatsUtil64Seconds_Object=MibScalar
mpCpuAStatsUtil64Seconds=_MpCpuAStatsUtil64Seconds_Object((1,3,6,1,4,1,1872,2,1,8,16,5),_MpCpuAStatsUtil64Seconds_Type())
mpCpuAStatsUtil64Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCpuAStatsUtil64Seconds.setStatus(_A)
_MpCpuBStatsUtil64Seconds_Type=Integer32
_MpCpuBStatsUtil64Seconds_Object=MibScalar
mpCpuBStatsUtil64Seconds=_MpCpuBStatsUtil64Seconds_Object((1,3,6,1,4,1,1872,2,1,8,16,6),_MpCpuBStatsUtil64Seconds_Type())
mpCpuBStatsUtil64Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:mpCpuBStatsUtil64Seconds.setStatus(_A)
_Information_ObjectIdentity=ObjectIdentity
information=_Information_ObjectIdentity((1,3,6,1,4,1,1872,2,1,9))
_AltswitchTraps_ObjectIdentity=ObjectIdentity
altswitchTraps=_AltswitchTraps_ObjectIdentity((1,3,6,1,4,1,1872,2,1,13))
_OperCmds_ObjectIdentity=ObjectIdentity
operCmds=_OperCmds_ObjectIdentity((1,3,6,1,4,1,1872,2,1,14))
_Radius_ObjectIdentity=ObjectIdentity
radius=_Radius_ObjectIdentity((1,3,6,1,4,1,1872,2,1,16))
_RadCurCfgPrimaryIpAddr_Type=IpAddress
_RadCurCfgPrimaryIpAddr_Object=MibScalar
radCurCfgPrimaryIpAddr=_RadCurCfgPrimaryIpAddr_Object((1,3,6,1,4,1,1872,2,1,16,1),_RadCurCfgPrimaryIpAddr_Type())
radCurCfgPrimaryIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgPrimaryIpAddr.setStatus(_A)
_RadNewCfgPrimaryIpAddr_Type=IpAddress
_RadNewCfgPrimaryIpAddr_Object=MibScalar
radNewCfgPrimaryIpAddr=_RadNewCfgPrimaryIpAddr_Object((1,3,6,1,4,1,1872,2,1,16,2),_RadNewCfgPrimaryIpAddr_Type())
radNewCfgPrimaryIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgPrimaryIpAddr.setStatus(_A)
_RadCurCfgSecondaryIpAddr_Type=IpAddress
_RadCurCfgSecondaryIpAddr_Object=MibScalar
radCurCfgSecondaryIpAddr=_RadCurCfgSecondaryIpAddr_Object((1,3,6,1,4,1,1872,2,1,16,3),_RadCurCfgSecondaryIpAddr_Type())
radCurCfgSecondaryIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgSecondaryIpAddr.setStatus(_A)
_RadNewCfgSecondaryIpAddr_Type=IpAddress
_RadNewCfgSecondaryIpAddr_Object=MibScalar
radNewCfgSecondaryIpAddr=_RadNewCfgSecondaryIpAddr_Object((1,3,6,1,4,1,1872,2,1,16,4),_RadNewCfgSecondaryIpAddr_Type())
radNewCfgSecondaryIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgSecondaryIpAddr.setStatus(_A)
class _RadCurCfgPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,3000))
_RadCurCfgPort_Type.__name__=_C
_RadCurCfgPort_Object=MibScalar
radCurCfgPort=_RadCurCfgPort_Object((1,3,6,1,4,1,1872,2,1,16,5),_RadCurCfgPort_Type())
radCurCfgPort.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgPort.setStatus(_A)
class _RadNewCfgPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,3000))
_RadNewCfgPort_Type.__name__=_C
_RadNewCfgPort_Object=MibScalar
radNewCfgPort=_RadNewCfgPort_Object((1,3,6,1,4,1,1872,2,1,16,6),_RadNewCfgPort_Type())
radNewCfgPort.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgPort.setStatus(_A)
class _RadCurCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RadCurCfgTimeout_Type.__name__=_C
_RadCurCfgTimeout_Object=MibScalar
radCurCfgTimeout=_RadCurCfgTimeout_Object((1,3,6,1,4,1,1872,2,1,16,7),_RadCurCfgTimeout_Type())
radCurCfgTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgTimeout.setStatus(_A)
class _RadNewCfgTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RadNewCfgTimeout_Type.__name__=_C
_RadNewCfgTimeout_Object=MibScalar
radNewCfgTimeout=_RadNewCfgTimeout_Object((1,3,6,1,4,1,1872,2,1,16,8),_RadNewCfgTimeout_Type())
radNewCfgTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgTimeout.setStatus(_A)
class _RadCurCfgRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_RadCurCfgRetries_Type.__name__=_C
_RadCurCfgRetries_Object=MibScalar
radCurCfgRetries=_RadCurCfgRetries_Object((1,3,6,1,4,1,1872,2,1,16,9),_RadCurCfgRetries_Type())
radCurCfgRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgRetries.setStatus(_A)
class _RadNewCfgRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_RadNewCfgRetries_Type.__name__=_C
_RadNewCfgRetries_Object=MibScalar
radNewCfgRetries=_RadNewCfgRetries_Object((1,3,6,1,4,1,1872,2,1,16,10),_RadNewCfgRetries_Type())
radNewCfgRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgRetries.setStatus(_A)
class _RadCurCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RadCurCfgState_Type.__name__=_C
_RadCurCfgState_Object=MibScalar
radCurCfgState=_RadCurCfgState_Object((1,3,6,1,4,1,1872,2,1,16,11),_RadCurCfgState_Type())
radCurCfgState.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgState.setStatus(_A)
class _RadNewCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_E,2),(_F,3)))
_RadNewCfgState_Type.__name__=_C
_RadNewCfgState_Object=MibScalar
radNewCfgState=_RadNewCfgState_Object((1,3,6,1,4,1,1872,2,1,16,12),_RadNewCfgState_Type())
radNewCfgState.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgState.setStatus(_A)
class _RadCurCfgAuthenString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RadCurCfgAuthenString_Type.__name__=_G
_RadCurCfgAuthenString_Object=MibScalar
radCurCfgAuthenString=_RadCurCfgAuthenString_Object((1,3,6,1,4,1,1872,2,1,16,13),_RadCurCfgAuthenString_Type())
radCurCfgAuthenString.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgAuthenString.setStatus(_A)
class _RadNewCfgAuthenString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RadNewCfgAuthenString_Type.__name__=_G
_RadNewCfgAuthenString_Object=MibScalar
radNewCfgAuthenString=_RadNewCfgAuthenString_Object((1,3,6,1,4,1,1872,2,1,16,14),_RadNewCfgAuthenString_Type())
radNewCfgAuthenString.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgAuthenString.setStatus(_A)
class _RadCurCfgTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RadCurCfgTelnet_Type.__name__=_C
_RadCurCfgTelnet_Object=MibScalar
radCurCfgTelnet=_RadCurCfgTelnet_Object((1,3,6,1,4,1,1872,2,1,16,15),_RadCurCfgTelnet_Type())
radCurCfgTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:radCurCfgTelnet.setStatus(_A)
class _RadNewCfgTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_RadNewCfgTelnet_Type.__name__=_C
_RadNewCfgTelnet_Object=MibScalar
radNewCfgTelnet=_RadNewCfgTelnet_Object((1,3,6,1,4,1,1872,2,1,16,16),_RadNewCfgTelnet_Type())
radNewCfgTelnet.setMaxAccess(_D)
if mibBuilder.loadTexts:radNewCfgTelnet.setStatus(_A)
mibBuilder.exportSymbols(_Q,**{'hardware':hardware,'hwPartNumber':hwPartNumber,'hwRevision':hwRevision,'hwPowerSupplyStatus':hwPowerSupplyStatus,'hwRedundantPSPresent':hwRedundantPSPresent,'hwRedundantPSStatus':hwRedundantPSStatus,'hwSensor1Temp':hwSensor1Temp,'hwSensor2Temp':hwSensor2Temp,'hwSensor3Temp':hwSensor3Temp,'hwSensor4Temp':hwSensor4Temp,'agent':agent,'agGeneral':agGeneral,'agSaveConfiguration':agSaveConfiguration,'agApplyConfiguration':agApplyConfiguration,'agApplyPending':agApplyPending,'agReset':agReset,'agConfigForNxtReset':agConfigForNxtReset,'agImageForNxtReset':agImageForNxtReset,'agSoftwareVersion':agSoftwareVersion,'agBootVer':agBootVer,'agImage1Ver':agImage1Ver,'agImage2Ver':agImage2Ver,'agRtcDate':agRtcDate,'agRtcTime':agRtcTime,'agTftpServerIpAddr':agTftpServerIpAddr,'agTftpImageFileName':agTftpImageFileName,'agTftpImage':agTftpImage,'agTftpDownload':agTftpDownload,'agLastSetErrorReason':agLastSetErrorReason,'agTftpServer':agTftpServer,'agTftpCfgFileName':agTftpCfgFileName,'agTftpDumpFileName':agTftpDumpFileName,'agTftpAction':agTftpAction,'agTftpLastActionStatus':agTftpLastActionStatus,'agRevert':agRevert,'agRevertApply':agRevertApply,'agEnabledSwFeatures':agEnabledSwFeatures,'agClrSyslogMsgs':agClrSyslogMsgs,'agSavePending':agSavePending,'agEnabledGslbKey':agEnabledGslbKey,'agEnabledBwmKey':agEnabledBwmKey,'agSlotNumber':agSlotNumber,'agEnabledRurlKey':agEnabledRurlKey,'agGeneralConfig':agGeneralConfig,'agNewCfgSyslogHost':agNewCfgSyslogHost,'agCurCfgSyslogHost':agCurCfgSyslogHost,'agNewCfgBootp':agNewCfgBootp,'agCurCfgBootp':agCurCfgBootp,'agNewCfgSpanningTree':agNewCfgSpanningTree,'agCurCfgSpanningTree':agCurCfgSpanningTree,'agTrapHostTableMaxEnt':agTrapHostTableMaxEnt,'agCurCfgTrapHostTable':agCurCfgTrapHostTable,'agCurCfgTrapHostEntry':agCurCfgTrapHostEntry,_U:agCurCfgTrapHostIndx,'agCurCfgTrapHostIpAddr':agCurCfgTrapHostIpAddr,'agCurCfgTrapHostCommString':agCurCfgTrapHostCommString,'agNewCfgTrapHostTable':agNewCfgTrapHostTable,'agNewCfgTrapHostEntry':agNewCfgTrapHostEntry,_V:agNewCfgTrapHostIndx,'agNewCfgTrapHostIpAddr':agNewCfgTrapHostIpAddr,'agNewCfgTrapHostCommString':agNewCfgTrapHostCommString,'agCurCfgHttpServerPort':agCurCfgHttpServerPort,'agNewCfgHttpServerPort':agNewCfgHttpServerPort,'agCurCfgLoginBanner':agCurCfgLoginBanner,'agNewCfgLoginBanner':agNewCfgLoginBanner,'agNewCfgSyslog2Host':agNewCfgSyslog2Host,'agCurCfgSyslog2Host':agCurCfgSyslog2Host,'agCurCfgSyslogFac':agCurCfgSyslogFac,'agNewCfgSyslogFac':agNewCfgSyslogFac,'agCurCfgSyslog2Fac':agCurCfgSyslog2Fac,'agNewCfgSyslog2Fac':agNewCfgSyslog2Fac,'agCurCfgSmtpHost':agCurCfgSmtpHost,'agNewCfgSmtpHost':agNewCfgSmtpHost,'agCurCfgConsole':agCurCfgConsole,'agNewCfgConsole':agNewCfgConsole,'agCurCfgMgmtNetwork':agCurCfgMgmtNetwork,'agNewCfgMgmtNetwork':agNewCfgMgmtNetwork,'agCurCfgMgmtMask':agCurCfgMgmtMask,'agNewCfgMgmtMask':agNewCfgMgmtMask,'agNTP':agNTP,'agCurCfgNTPServer':agCurCfgNTPServer,'agNewCfgNTPServer':agNewCfgNTPServer,'agCurCfgNTPResyncInterval':agCurCfgNTPResyncInterval,'agNewCfgNTPResyncInterval':agNewCfgNTPResyncInterval,'agCurCfgNTPTzone':agCurCfgNTPTzone,'agNewCfgNTPTzone':agNewCfgNTPTzone,'agCurCfgNTPDlight':agCurCfgNTPDlight,'agNewCfgNTPDlight':agNewCfgNTPDlight,'agCurCfgNTPService':agCurCfgNTPService,'agNewCfgNTPService':agNewCfgNTPService,'agLog':agLog,'agNewCfgSyslogTrapConsole':agNewCfgSyslogTrapConsole,'agCurCfgSyslogTrapConsole':agCurCfgSyslogTrapConsole,'agNewCfgSyslogTrapSystem':agNewCfgSyslogTrapSystem,'agCurCfgSyslogTrapSystem':agCurCfgSyslogTrapSystem,'agNewCfgSyslogTrapMgmt':agNewCfgSyslogTrapMgmt,'agCurCfgSyslogTrapMgmt':agCurCfgSyslogTrapMgmt,'agNewCfgSyslogTrapCli':agNewCfgSyslogTrapCli,'agCurCfgSyslogTrapCli':agCurCfgSyslogTrapCli,'agNewCfgSyslogTrapStp':agNewCfgSyslogTrapStp,'agCurCfgSyslogTrapStp':agCurCfgSyslogTrapStp,'agNewCfgSyslogTrapVlan':agNewCfgSyslogTrapVlan,'agCurCfgSyslogTrapVlan':agCurCfgSyslogTrapVlan,'agNewCfgSyslogTrapSlb':agNewCfgSyslogTrapSlb,'agCurCfgSyslogTrapSlb':agCurCfgSyslogTrapSlb,'agNewCfgSyslogTrapGslb':agNewCfgSyslogTrapGslb,'agCurCfgSyslogTrapGslb':agCurCfgSyslogTrapGslb,'agNewCfgSyslogTrapFilter':agNewCfgSyslogTrapFilter,'agCurCfgSyslogTrapFilter':agCurCfgSyslogTrapFilter,'agNewCfgSyslogTrapSsh':agNewCfgSyslogTrapSsh,'agCurCfgSyslogTrapSsh':agCurCfgSyslogTrapSsh,'agNewCfgSyslogTrapVrrp':agNewCfgSyslogTrapVrrp,'agCurCfgSyslogTrapVrrp':agCurCfgSyslogTrapVrrp,'agNewCfgSyslogTrapBgp':agNewCfgSyslogTrapBgp,'agCurCfgSyslogTrapBgp':agCurCfgSyslogTrapBgp,'agNewCfgSyslogTrapNtp':agNewCfgSyslogTrapNtp,'agCurCfgSyslogTrapNtp':agCurCfgSyslogTrapNtp,'agNewCfgSyslogTrapIsd':agNewCfgSyslogTrapIsd,'agCurCfgSyslogTrapIsd':agCurCfgSyslogTrapIsd,'agNewCfgSyslogTrapIp':agNewCfgSyslogTrapIp,'agCurCfgSyslogTrapIp':agCurCfgSyslogTrapIp,'agNewCfgSyslogTrapWeb':agNewCfgSyslogTrapWeb,'agCurCfgSyslogTrapWeb':agCurCfgSyslogTrapWeb,'agNewCfgSyslogTrapSynAtk':agNewCfgSyslogTrapSynAtk,'agCurCfgSyslogTrapSynAtk':agCurCfgSyslogTrapSynAtk,'agNewCfgSyslogTrapTcpLim':agNewCfgSyslogTrapTcpLim,'agCurCfgSyslogTrapTcpLim':agCurCfgSyslogTrapTcpLim,'stats':stats,'memStats':memStats,'memStatsAllocs':memStatsAllocs,'memStatsFrees':memStatsFrees,'memStatsAllocFails':memStatsAllocFails,'memStatsBytesCurr':memStatsBytesCurr,'memStatsBytesHiwat':memStatsBytesHiwat,'memStatsPoolBytes':memStatsPoolBytes,'memStatsLargest':memStatsLargest,'pktStats':pktStats,'pktStatsAllocs':pktStatsAllocs,'pktStatsFrees':pktStatsFrees,'pktStatsAllocFails':pktStatsAllocFails,'pktStatsMediums':pktStatsMediums,'pktStatsJumbos':pktStatsJumbos,'pktStatsSmalls':pktStatsSmalls,'mpCpuStats':mpCpuStats,'mpCpuAStatsUtil1Second':mpCpuAStatsUtil1Second,'mpCpuBStatsUtil1Second':mpCpuBStatsUtil1Second,'mpCpuAStatsUtil4Seconds':mpCpuAStatsUtil4Seconds,'mpCpuBStatsUtil4Seconds':mpCpuBStatsUtil4Seconds,'mpCpuAStatsUtil64Seconds':mpCpuAStatsUtil64Seconds,'mpCpuBStatsUtil64Seconds':mpCpuBStatsUtil64Seconds,'information':information,'altswitchTraps':altswitchTraps,'operCmds':operCmds,'radius':radius,'radCurCfgPrimaryIpAddr':radCurCfgPrimaryIpAddr,'radNewCfgPrimaryIpAddr':radNewCfgPrimaryIpAddr,'radCurCfgSecondaryIpAddr':radCurCfgSecondaryIpAddr,'radNewCfgSecondaryIpAddr':radNewCfgSecondaryIpAddr,'radCurCfgPort':radCurCfgPort,'radNewCfgPort':radNewCfgPort,'radCurCfgTimeout':radCurCfgTimeout,'radNewCfgTimeout':radNewCfgTimeout,'radCurCfgRetries':radCurCfgRetries,'radNewCfgRetries':radNewCfgRetries,'radCurCfgState':radCurCfgState,'radNewCfgState':radNewCfgState,'radCurCfgAuthenString':radCurCfgAuthenString,'radNewCfgAuthenString':radNewCfgAuthenString,'radCurCfgTelnet':radCurCfgTelnet,'radNewCfgTelnet':radNewCfgTelnet})