_O='mergeConfig'
_N='restoreConfig'
_M='backupConfig'
_L='disable'
_K='enable'
_J='success'
_I='resetToDefault'
_H='none'
_G='config2'
_F='config1'
_E='read-only'
_D='nothing'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelManagement=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,49))
_ZyxelSysMgmt_ObjectIdentity=ObjectIdentity
zyxelSysMgmt=_ZyxelSysMgmt_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1))
class _ZySysMgmtConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZySysMgmtConfigSave_Type.__name__=_C
_ZySysMgmtConfigSave_Object=MibScalar
zySysMgmtConfigSave=_ZySysMgmtConfigSave_Object((1,3,6,1,4,1,890,1,15,3,49,1,1),_ZySysMgmtConfigSave_Type())
zySysMgmtConfigSave.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtConfigSave.setStatus(_A)
class _ZySysMgmtBootupConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZySysMgmtBootupConfig_Type.__name__=_C
_ZySysMgmtBootupConfig_Object=MibScalar
zySysMgmtBootupConfig=_ZySysMgmtBootupConfig_Object((1,3,6,1,4,1,890,1,15,3,49,1,2),_ZySysMgmtBootupConfig_Type())
zySysMgmtBootupConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtBootupConfig.setStatus(_A)
class _ZySysMgmtReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('reboot',1)))
_ZySysMgmtReboot_Type.__name__=_C
_ZySysMgmtReboot_Object=MibScalar
zySysMgmtReboot=_ZySysMgmtReboot_Object((1,3,6,1,4,1,890,1,15,3,49,1,3),_ZySysMgmtReboot_Type())
zySysMgmtReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtReboot.setStatus(_A)
class _ZySysMgmtDefaultConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_I,1)))
_ZySysMgmtDefaultConfig_Type.__name__=_C
_ZySysMgmtDefaultConfig_Object=MibScalar
zySysMgmtDefaultConfig=_ZySysMgmtDefaultConfig_Object((1,3,6,1,4,1,890,1,15,3,49,1,4),_ZySysMgmtDefaultConfig_Type())
zySysMgmtDefaultConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtDefaultConfig.setStatus(_A)
class _ZySysMgmtLastActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_J,1),('fail',2)))
_ZySysMgmtLastActionStatus_Type.__name__=_C
_ZySysMgmtLastActionStatus_Object=MibScalar
zySysMgmtLastActionStatus=_ZySysMgmtLastActionStatus_Object((1,3,6,1,4,1,890,1,15,3,49,1,5),_ZySysMgmtLastActionStatus_Type())
zySysMgmtLastActionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtLastActionStatus.setStatus(_A)
class _ZySysMgmtSysStatus_Type(Bits):namedValues=NamedValues(*(('sysAlarmDetected',0),('sysTemperatureError',1),('sysFanRPMError',2),('sysVoltageRangeError',3),('sysNoDefect',4)))
_ZySysMgmtSysStatus_Type.__name__='Bits'
_ZySysMgmtSysStatus_Object=MibScalar
zySysMgmtSysStatus=_ZySysMgmtSysStatus_Object((1,3,6,1,4,1,890,1,15,3,49,1,6),_ZySysMgmtSysStatus_Type())
zySysMgmtSysStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtSysStatus.setStatus(_A)
_ZySysMgmtCPUUsage_Type=Integer32
_ZySysMgmtCPUUsage_Object=MibScalar
zySysMgmtCPUUsage=_ZySysMgmtCPUUsage_Object((1,3,6,1,4,1,890,1,15,3,49,1,7),_ZySysMgmtCPUUsage_Type())
zySysMgmtCPUUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtCPUUsage.setStatus(_A)
class _ZySysMgmtBootupImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('image1',1),('image2',2)))
_ZySysMgmtBootupImage_Type.__name__=_C
_ZySysMgmtBootupImage_Object=MibScalar
zySysMgmtBootupImage=_ZySysMgmtBootupImage_Object((1,3,6,1,4,1,890,1,15,3,49,1,8),_ZySysMgmtBootupImage_Type())
zySysMgmtBootupImage.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtBootupImage.setStatus(_A)
class _ZySysMgmtCounterReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZySysMgmtCounterReset_Type.__name__=_C
_ZySysMgmtCounterReset_Object=MibScalar
zySysMgmtCounterReset=_ZySysMgmtCounterReset_Object((1,3,6,1,4,1,890,1,15,3,49,1,9),_ZySysMgmtCounterReset_Type())
zySysMgmtCounterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtCounterReset.setStatus(_A)
_ZyxelSysMgmtTftpServiceSetup_ObjectIdentity=ObjectIdentity
zyxelSysMgmtTftpServiceSetup=_ZyxelSysMgmtTftpServiceSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1,10))
_ZySysMgmtTftpServiceServerIpAddress_Type=IpAddress
_ZySysMgmtTftpServiceServerIpAddress_Object=MibScalar
zySysMgmtTftpServiceServerIpAddress=_ZySysMgmtTftpServiceServerIpAddress_Object((1,3,6,1,4,1,890,1,15,3,49,1,10,1),_ZySysMgmtTftpServiceServerIpAddress_Type())
zySysMgmtTftpServiceServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtTftpServiceServerIpAddress.setStatus(_A)
_ZySysMgmtTftpRemoteFileName_Type=DisplayString
_ZySysMgmtTftpRemoteFileName_Object=MibScalar
zySysMgmtTftpRemoteFileName=_ZySysMgmtTftpRemoteFileName_Object((1,3,6,1,4,1,890,1,15,3,49,1,10,2),_ZySysMgmtTftpRemoteFileName_Type())
zySysMgmtTftpRemoteFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtTftpRemoteFileName.setStatus(_A)
class _ZySysMgmtTftpConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZySysMgmtTftpConfigIndex_Type.__name__=_C
_ZySysMgmtTftpConfigIndex_Object=MibScalar
zySysMgmtTftpConfigIndex=_ZySysMgmtTftpConfigIndex_Object((1,3,6,1,4,1,890,1,15,3,49,1,10,3),_ZySysMgmtTftpConfigIndex_Type())
zySysMgmtTftpConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtTftpConfigIndex.setStatus(_A)
class _ZySysMgmtTftpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_M,1),(_N,2),(_O,3)))
_ZySysMgmtTftpAction_Type.__name__=_C
_ZySysMgmtTftpAction_Object=MibScalar
zySysMgmtTftpAction=_ZySysMgmtTftpAction_Object((1,3,6,1,4,1,890,1,15,3,49,1,10,4),_ZySysMgmtTftpAction_Type())
zySysMgmtTftpAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtTftpAction.setStatus(_A)
class _ZySysMgmtTftpActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_J,1),('fail',2),('underAction',3)))
_ZySysMgmtTftpActionStatus_Type.__name__=_C
_ZySysMgmtTftpActionStatus_Object=MibScalar
zySysMgmtTftpActionStatus=_ZySysMgmtTftpActionStatus_Object((1,3,6,1,4,1,890,1,15,3,49,1,10,5),_ZySysMgmtTftpActionStatus_Type())
zySysMgmtTftpActionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtTftpActionStatus.setStatus(_A)
class _ZySysMgmtTftpActionPrivilege13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),(_M,1),(_N,2),(_O,3)))
_ZySysMgmtTftpActionPrivilege13_Type.__name__=_C
_ZySysMgmtTftpActionPrivilege13_Object=MibScalar
zySysMgmtTftpActionPrivilege13=_ZySysMgmtTftpActionPrivilege13_Object((1,3,6,1,4,1,890,1,15,3,49,1,10,113),_ZySysMgmtTftpActionPrivilege13_Type())
zySysMgmtTftpActionPrivilege13.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtTftpActionPrivilege13.setStatus(_A)
class _ZySysMgmtReloadFactoryDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('reloadFactoryDefault',1)))
_ZySysMgmtReloadFactoryDefault_Type.__name__=_C
_ZySysMgmtReloadFactoryDefault_Object=MibScalar
zySysMgmtReloadFactoryDefault=_ZySysMgmtReloadFactoryDefault_Object((1,3,6,1,4,1,890,1,15,3,49,1,11),_ZySysMgmtReloadFactoryDefault_Type())
zySysMgmtReloadFactoryDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtReloadFactoryDefault.setStatus(_A)
class _ZySysMgmtReloadStackingDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('reloadStackingDefault',1)))
_ZySysMgmtReloadStackingDefault_Type.__name__=_C
_ZySysMgmtReloadStackingDefault_Object=MibScalar
zySysMgmtReloadStackingDefault=_ZySysMgmtReloadStackingDefault_Object((1,3,6,1,4,1,890,1,15,3,49,1,12),_ZySysMgmtReloadStackingDefault_Type())
zySysMgmtReloadStackingDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtReloadStackingDefault.setStatus(_A)
class _ZySysMgmtConfigSaveCustomDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('configSaveCustomDefault',1)))
_ZySysMgmtConfigSaveCustomDefault_Type.__name__=_C
_ZySysMgmtConfigSaveCustomDefault_Object=MibScalar
zySysMgmtConfigSaveCustomDefault=_ZySysMgmtConfigSaveCustomDefault_Object((1,3,6,1,4,1,890,1,15,3,49,1,13),_ZySysMgmtConfigSaveCustomDefault_Type())
zySysMgmtConfigSaveCustomDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtConfigSaveCustomDefault.setStatus(_A)
class _ZySysMgmtReloadCustomDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),('reloadCustomDefault',1)))
_ZySysMgmtReloadCustomDefault_Type.__name__=_C
_ZySysMgmtReloadCustomDefault_Object=MibScalar
zySysMgmtReloadCustomDefault=_ZySysMgmtReloadCustomDefault_Object((1,3,6,1,4,1,890,1,15,3,49,1,14),_ZySysMgmtReloadCustomDefault_Type())
zySysMgmtReloadCustomDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtReloadCustomDefault.setStatus(_A)
_ZyxelSysMgmtAutoConfiguration_ObjectIdentity=ObjectIdentity
zyxelSysMgmtAutoConfiguration=_ZyxelSysMgmtAutoConfiguration_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1,15))
_ZyxelSysMgmtAutoConfigurationSetup_ObjectIdentity=ObjectIdentity
zyxelSysMgmtAutoConfigurationSetup=_ZyxelSysMgmtAutoConfigurationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1,15,1))
_ZySysMgmtAutoConfigurationState_Type=EnabledStatus
_ZySysMgmtAutoConfigurationState_Object=MibScalar
zySysMgmtAutoConfigurationState=_ZySysMgmtAutoConfigurationState_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,1,1),_ZySysMgmtAutoConfigurationState_Type())
zySysMgmtAutoConfigurationState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationState.setStatus(_A)
_ZySysMgmtAutoConfigurationMode_Type=Integer32
_ZySysMgmtAutoConfigurationMode_Object=MibScalar
zySysMgmtAutoConfigurationMode=_ZySysMgmtAutoConfigurationMode_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,1,2),_ZySysMgmtAutoConfigurationMode_Type())
zySysMgmtAutoConfigurationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationMode.setStatus(_A)
_ZySysMgmtAutoConfigurationVlanId_Type=Integer32
_ZySysMgmtAutoConfigurationVlanId_Object=MibScalar
zySysMgmtAutoConfigurationVlanId=_ZySysMgmtAutoConfigurationVlanId_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,1,3),_ZySysMgmtAutoConfigurationVlanId_Type())
zySysMgmtAutoConfigurationVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationVlanId.setStatus(_A)
_ZySysMgmtAutoConfigurationUrl_Type=DisplayString
_ZySysMgmtAutoConfigurationUrl_Object=MibScalar
zySysMgmtAutoConfigurationUrl=_ZySysMgmtAutoConfigurationUrl_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,1,4),_ZySysMgmtAutoConfigurationUrl_Type())
zySysMgmtAutoConfigurationUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationUrl.setStatus(_A)
_ZyxelSysMgmtAutoConfigurationStatus_ObjectIdentity=ObjectIdentity
zyxelSysMgmtAutoConfigurationStatus=_ZyxelSysMgmtAutoConfigurationStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1,15,2))
_ZyxelSysMgmtAutoConfigurationResult_ObjectIdentity=ObjectIdentity
zyxelSysMgmtAutoConfigurationResult=_ZyxelSysMgmtAutoConfigurationResult_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1,15,2,1))
_ZySysMgmtAutoConfigurationResultMode_Type=Integer32
_ZySysMgmtAutoConfigurationResultMode_Object=MibScalar
zySysMgmtAutoConfigurationResultMode=_ZySysMgmtAutoConfigurationResultMode_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,2,1,1),_ZySysMgmtAutoConfigurationResultMode_Type())
zySysMgmtAutoConfigurationResultMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationResultMode.setStatus(_A)
_ZySysMgmtAutoConfigurationResultState_Type=Integer32
_ZySysMgmtAutoConfigurationResultState_Object=MibScalar
zySysMgmtAutoConfigurationResultState=_ZySysMgmtAutoConfigurationResultState_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,2,1,2),_ZySysMgmtAutoConfigurationResultState_Type())
zySysMgmtAutoConfigurationResultState.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationResultState.setStatus(_A)
_ZySysMgmtAutoConfigurationResultFilename_Type=DisplayString
_ZySysMgmtAutoConfigurationResultFilename_Object=MibScalar
zySysMgmtAutoConfigurationResultFilename=_ZySysMgmtAutoConfigurationResultFilename_Object((1,3,6,1,4,1,890,1,15,3,49,1,15,2,1,3),_ZySysMgmtAutoConfigurationResultFilename_Type())
zySysMgmtAutoConfigurationResultFilename.setMaxAccess(_E)
if mibBuilder.loadTexts:zySysMgmtAutoConfigurationResultFilename.setStatus(_A)
_ZyxelSysMgmtCustomDefaultSetup_ObjectIdentity=ObjectIdentity
zyxelSysMgmtCustomDefaultSetup=_ZyxelSysMgmtCustomDefaultSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,1,16))
class _ZySysMgmtCustomDefaultState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZySysMgmtCustomDefaultState_Type.__name__=_C
_ZySysMgmtCustomDefaultState_Object=MibScalar
zySysMgmtCustomDefaultState=_ZySysMgmtCustomDefaultState_Object((1,3,6,1,4,1,890,1,15,3,49,1,16,1),_ZySysMgmtCustomDefaultState_Type())
zySysMgmtCustomDefaultState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtCustomDefaultState.setStatus(_A)
class _ZySysMgmtConfigSavePrivilege13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZySysMgmtConfigSavePrivilege13_Type.__name__=_C
_ZySysMgmtConfigSavePrivilege13_Object=MibScalar
zySysMgmtConfigSavePrivilege13=_ZySysMgmtConfigSavePrivilege13_Object((1,3,6,1,4,1,890,1,15,3,49,1,113),_ZySysMgmtConfigSavePrivilege13_Type())
zySysMgmtConfigSavePrivilege13.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtConfigSavePrivilege13.setStatus(_A)
class _ZySysMgmtDefaultConfigPrivilege13_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_I,1)))
_ZySysMgmtDefaultConfigPrivilege13_Type.__name__=_C
_ZySysMgmtDefaultConfigPrivilege13_Object=MibScalar
zySysMgmtDefaultConfigPrivilege13=_ZySysMgmtDefaultConfigPrivilege13_Object((1,3,6,1,4,1,890,1,15,3,49,1,213),_ZySysMgmtDefaultConfigPrivilege13_Type())
zySysMgmtDefaultConfigPrivilege13.setMaxAccess(_B)
if mibBuilder.loadTexts:zySysMgmtDefaultConfigPrivilege13.setStatus(_A)
_ZyxelSysMgmtNotifications_ObjectIdentity=ObjectIdentity
zyxelSysMgmtNotifications=_ZyxelSysMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,49,2))
zySysMgmtUncontrolledSystemReset=NotificationType((1,3,6,1,4,1,890,1,15,3,49,2,1))
if mibBuilder.loadTexts:zySysMgmtUncontrolledSystemReset.setStatus(_A)
zySysMgmtControlledSystemReset=NotificationType((1,3,6,1,4,1,890,1,15,3,49,2,2))
if mibBuilder.loadTexts:zySysMgmtControlledSystemReset.setStatus(_A)
zySysMgmtBootImageInconsistence=NotificationType((1,3,6,1,4,1,890,1,15,3,49,2,3))
if mibBuilder.loadTexts:zySysMgmtBootImageInconsistence.setStatus(_A)
zySysMgmtReloadCustomCAFail=NotificationType((1,3,6,1,4,1,890,1,15,3,49,2,4))
if mibBuilder.loadTexts:zySysMgmtReloadCustomCAFail.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-SYSTEM-MGMT-MIB',**{'zyxelManagement':zyxelManagement,'zyxelSysMgmt':zyxelSysMgmt,'zySysMgmtConfigSave':zySysMgmtConfigSave,'zySysMgmtBootupConfig':zySysMgmtBootupConfig,'zySysMgmtReboot':zySysMgmtReboot,'zySysMgmtDefaultConfig':zySysMgmtDefaultConfig,'zySysMgmtLastActionStatus':zySysMgmtLastActionStatus,'zySysMgmtSysStatus':zySysMgmtSysStatus,'zySysMgmtCPUUsage':zySysMgmtCPUUsage,'zySysMgmtBootupImage':zySysMgmtBootupImage,'zySysMgmtCounterReset':zySysMgmtCounterReset,'zyxelSysMgmtTftpServiceSetup':zyxelSysMgmtTftpServiceSetup,'zySysMgmtTftpServiceServerIpAddress':zySysMgmtTftpServiceServerIpAddress,'zySysMgmtTftpRemoteFileName':zySysMgmtTftpRemoteFileName,'zySysMgmtTftpConfigIndex':zySysMgmtTftpConfigIndex,'zySysMgmtTftpAction':zySysMgmtTftpAction,'zySysMgmtTftpActionStatus':zySysMgmtTftpActionStatus,'zySysMgmtTftpActionPrivilege13':zySysMgmtTftpActionPrivilege13,'zySysMgmtReloadFactoryDefault':zySysMgmtReloadFactoryDefault,'zySysMgmtReloadStackingDefault':zySysMgmtReloadStackingDefault,'zySysMgmtConfigSaveCustomDefault':zySysMgmtConfigSaveCustomDefault,'zySysMgmtReloadCustomDefault':zySysMgmtReloadCustomDefault,'zyxelSysMgmtAutoConfiguration':zyxelSysMgmtAutoConfiguration,'zyxelSysMgmtAutoConfigurationSetup':zyxelSysMgmtAutoConfigurationSetup,'zySysMgmtAutoConfigurationState':zySysMgmtAutoConfigurationState,'zySysMgmtAutoConfigurationMode':zySysMgmtAutoConfigurationMode,'zySysMgmtAutoConfigurationVlanId':zySysMgmtAutoConfigurationVlanId,'zySysMgmtAutoConfigurationUrl':zySysMgmtAutoConfigurationUrl,'zyxelSysMgmtAutoConfigurationStatus':zyxelSysMgmtAutoConfigurationStatus,'zyxelSysMgmtAutoConfigurationResult':zyxelSysMgmtAutoConfigurationResult,'zySysMgmtAutoConfigurationResultMode':zySysMgmtAutoConfigurationResultMode,'zySysMgmtAutoConfigurationResultState':zySysMgmtAutoConfigurationResultState,'zySysMgmtAutoConfigurationResultFilename':zySysMgmtAutoConfigurationResultFilename,'zyxelSysMgmtCustomDefaultSetup':zyxelSysMgmtCustomDefaultSetup,'zySysMgmtCustomDefaultState':zySysMgmtCustomDefaultState,'zySysMgmtConfigSavePrivilege13':zySysMgmtConfigSavePrivilege13,'zySysMgmtDefaultConfigPrivilege13':zySysMgmtDefaultConfigPrivilege13,'zyxelSysMgmtNotifications':zyxelSysMgmtNotifications,'zySysMgmtUncontrolledSystemReset':zySysMgmtUncontrolledSystemReset,'zySysMgmtControlledSystemReset':zySysMgmtControlledSystemReset,'zySysMgmtBootImageInconsistence':zySysMgmtBootImageInconsistence,'zySysMgmtReloadCustomCAFail':zySysMgmtReloadCustomCAFail})