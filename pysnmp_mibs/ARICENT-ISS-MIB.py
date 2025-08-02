_AT='issLogTrapFileName'
_AS='issLogTrapEventTime'
_AR='issLogTrapEvent'
_AQ='issSwitchFanStatus'
_AP='issSwitchCurrentFlashUsage'
_AO='issSwitchMaxFlashUsage'
_AN='issSwitchCurrentRAMUsage'
_AM='issSwitchMaxRAMUsage'
_AL='issSwitchCurrentPowerSupply'
_AK='issSwitchPowerFailure'
_AJ='issSwitchPowerSurge'
_AI='issSwitchCurrentCPUThreshold'
_AH='issSwitchMaxCPUThreshold'
_AG='issSwitchCurrentTemperature'
_AF='issSwitchMaxThresholdTemperature'
_AE='issSwitchMinThresholdTemperature'
_AD='issAuditTrapFileName'
_AC='issAuditTrapEventTime'
_AB='issAuditTrapEvent'
_AA='issMsrFailedValue'
_A9='issMsrFailedOid'
_A8='issConfigRestoreStatus'
_A7='issModuleId'
_A6='sizeThresholdHit'
_A5='sizeExceeded'
_A4='writeFailed'
_A3='openFailed'
_A2='issL4SwitchingFilterNo'
_A1='issIpAuthMgrIpMask'
_A0='issIpAuthMgrIpAddr'
_z='FFFFFFFF'
_y='00000000'
_x='issL3FilterNo'
_w='issL2FilterNo'
_v='issRateCtrlIndex'
_u='issMirrorCtrlExtnDestination'
_t='issMirrorCtrlExtnSrcVlanId'
_s='issMirrorCtrlExtnSrcVlanContext'
_r='issMirrorCtrlExtnSrcId'
_q='issMirrorCtrlIndex'
_p='issPortIsolationEgressPort'
_o='issPortIsolationInVlanId'
_n='issPortIsolationIngressPort'
_m='issPortCtrlIndex'
_l='issConfigCtrlIndex'
_k='config.txt'
_j='iss.log'
_i='console'
_h='iss.conf'
_g='MacAddress'
_f='issSwitchFanIndex'
_e='both'
_d='egress'
_c='ingress'
_b='delete'
_a='add'
_Z='drop'
_Y='invalid'
_X='failed'
_W='successful'
_V='inprogress'
_U='sftp'
_T='tftp'
_S='issMirrorCtrlExtnSessionIndex'
_R='enable'
_Q='notInitiated'
_P='IpAddress'
_O='accessible-for-notify'
_N='disable'
_M='read-create'
_L='Unsigned32'
_K='enabled'
_J='disabled'
_I='TruthValue'
_H='not-accessible'
_G='read-only'
_F='DisplayString'
_E='ARICENT-ISS-MIB'
_D='deprecated'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_P,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,_g,'PhysAddress','RowStatus','StorageType','TextualConvention',_I)
iss=ModuleIdentity((1,3,6,1,4,1,2076,81))
if mibBuilder.loadTexts:iss.setRevisions(('2022-03-14 00:00','2012-09-05 00:00'))
class PortList(TextualConvention,OctetString):status=_A
_IssNotifications_ObjectIdentity=ObjectIdentity
issNotifications=_IssNotifications_ObjectIdentity((1,3,6,1,4,1,2076,81,0))
_IssSystem_ObjectIdentity=ObjectIdentity
issSystem=_IssSystem_ObjectIdentity((1,3,6,1,4,1,2076,81,1))
class _IssSwitchName_Type(DisplayString):defaultValue=OctetString('ISS');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssSwitchName_Type.__name__=_F
_IssSwitchName_Object=MibScalar
issSwitchName=_IssSwitchName_Object((1,3,6,1,4,1,2076,81,1,1),_IssSwitchName_Type())
issSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchName.setStatus(_A)
class _IssHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_IssHardwareVersion_Type.__name__=_F
_IssHardwareVersion_Object=MibScalar
issHardwareVersion=_IssHardwareVersion_Object((1,3,6,1,4,1,2076,81,1,2),_IssHardwareVersion_Type())
issHardwareVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:issHardwareVersion.setStatus(_A)
class _IssFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_IssFirmwareVersion_Type.__name__=_F
_IssFirmwareVersion_Object=MibScalar
issFirmwareVersion=_IssFirmwareVersion_Object((1,3,6,1,4,1,2076,81,1,3),_IssFirmwareVersion_Type())
issFirmwareVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:issFirmwareVersion.setStatus(_A)
class _IssDefaultIpAddrCfgMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('dynamic',2)))
_IssDefaultIpAddrCfgMode_Type.__name__=_C
_IssDefaultIpAddrCfgMode_Object=MibScalar
issDefaultIpAddrCfgMode=_IssDefaultIpAddrCfgMode_Object((1,3,6,1,4,1,2076,81,1,4),_IssDefaultIpAddrCfgMode_Type())
issDefaultIpAddrCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultIpAddrCfgMode.setStatus(_A)
_IssDefaultIpAddr_Type=IpAddress
_IssDefaultIpAddr_Object=MibScalar
issDefaultIpAddr=_IssDefaultIpAddr_Object((1,3,6,1,4,1,2076,81,1,5),_IssDefaultIpAddr_Type())
issDefaultIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultIpAddr.setStatus(_A)
_IssDefaultIpSubnetMask_Type=IpAddress
_IssDefaultIpSubnetMask_Object=MibScalar
issDefaultIpSubnetMask=_IssDefaultIpSubnetMask_Object((1,3,6,1,4,1,2076,81,1,6),_IssDefaultIpSubnetMask_Type())
issDefaultIpSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultIpSubnetMask.setStatus(_A)
_IssEffectiveIpAddr_Type=IpAddress
_IssEffectiveIpAddr_Object=MibScalar
issEffectiveIpAddr=_IssEffectiveIpAddr_Object((1,3,6,1,4,1,2076,81,1,7),_IssEffectiveIpAddr_Type())
issEffectiveIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:issEffectiveIpAddr.setStatus(_D)
class _IssDefaultInterface_Type(DisplayString):defaultValue=OctetString('eth0');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_IssDefaultInterface_Type.__name__=_F
_IssDefaultInterface_Object=MibScalar
issDefaultInterface=_IssDefaultInterface_Object((1,3,6,1,4,1,2076,81,1,8),_IssDefaultInterface_Type())
issDefaultInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultInterface.setStatus(_A)
class _IssRestart_Type(TruthValue):defaultValue=2
_IssRestart_Type.__name__=_I
_IssRestart_Object=MibScalar
issRestart=_IssRestart_Object((1,3,6,1,4,1,2076,81,1,9),_IssRestart_Type())
issRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:issRestart.setStatus(_A)
class _IssConfigSaveOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noSave',1),('flashSave',2),('remoteSave',3),('startupConfig',4)))
_IssConfigSaveOption_Type.__name__=_C
_IssConfigSaveOption_Object=MibScalar
issConfigSaveOption=_IssConfigSaveOption_Object((1,3,6,1,4,1,2076,81,1,10),_IssConfigSaveOption_Type())
issConfigSaveOption.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveOption.setStatus(_A)
_IssConfigSaveIpAddr_Type=IpAddress
_IssConfigSaveIpAddr_Object=MibScalar
issConfigSaveIpAddr=_IssConfigSaveIpAddr_Object((1,3,6,1,4,1,2076,81,1,11),_IssConfigSaveIpAddr_Type())
issConfigSaveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveIpAddr.setStatus(_D)
class _IssConfigSaveFileName_Type(DisplayString):defaultValue=OctetString(_h);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssConfigSaveFileName_Type.__name__=_F
_IssConfigSaveFileName_Object=MibScalar
issConfigSaveFileName=_IssConfigSaveFileName_Object((1,3,6,1,4,1,2076,81,1,12),_IssConfigSaveFileName_Type())
issConfigSaveFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveFileName.setStatus(_A)
class _IssInitiateConfigSave_Type(TruthValue):defaultValue=2
_IssInitiateConfigSave_Type.__name__=_I
_IssInitiateConfigSave_Object=MibScalar
issInitiateConfigSave=_IssInitiateConfigSave_Object((1,3,6,1,4,1,2076,81,1,13),_IssInitiateConfigSave_Type())
issInitiateConfigSave.setMaxAccess(_B)
if mibBuilder.loadTexts:issInitiateConfigSave.setStatus(_A)
class _IssConfigSaveStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('saveInProgress',1),('saveSuccessful',2),('saveFailed',3),(_Q,4)))
_IssConfigSaveStatus_Type.__name__=_C
_IssConfigSaveStatus_Object=MibScalar
issConfigSaveStatus=_IssConfigSaveStatus_Object((1,3,6,1,4,1,2076,81,1,14),_IssConfigSaveStatus_Type())
issConfigSaveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issConfigSaveStatus.setStatus(_A)
class _IssConfigRestoreOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noRestore',1),('restore',2)))
_IssConfigRestoreOption_Type.__name__=_C
_IssConfigRestoreOption_Object=MibScalar
issConfigRestoreOption=_IssConfigRestoreOption_Object((1,3,6,1,4,1,2076,81,1,15),_IssConfigRestoreOption_Type())
issConfigRestoreOption.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigRestoreOption.setStatus(_A)
_IssConfigRestoreIpAddr_Type=IpAddress
_IssConfigRestoreIpAddr_Object=MibScalar
issConfigRestoreIpAddr=_IssConfigRestoreIpAddr_Object((1,3,6,1,4,1,2076,81,1,16),_IssConfigRestoreIpAddr_Type())
issConfigRestoreIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigRestoreIpAddr.setStatus(_D)
class _IssConfigRestoreFileName_Type(DisplayString):defaultValue=OctetString(_h);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssConfigRestoreFileName_Type.__name__=_F
_IssConfigRestoreFileName_Object=MibScalar
issConfigRestoreFileName=_IssConfigRestoreFileName_Object((1,3,6,1,4,1,2076,81,1,17),_IssConfigRestoreFileName_Type())
issConfigRestoreFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigRestoreFileName.setStatus(_A)
class _IssInitiateConfigRestore_Type(TruthValue):defaultValue=2
_IssInitiateConfigRestore_Type.__name__=_I
_IssInitiateConfigRestore_Object=MibScalar
issInitiateConfigRestore=_IssInitiateConfigRestore_Object((1,3,6,1,4,1,2076,81,1,18),_IssInitiateConfigRestore_Type())
issInitiateConfigRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:issInitiateConfigRestore.setStatus(_A)
class _IssConfigRestoreStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('restoreInprogress',1),('restoreSuccessful',2),('restoreFailed',3),(_Q,4)))
_IssConfigRestoreStatus_Type.__name__=_C
_IssConfigRestoreStatus_Object=MibScalar
issConfigRestoreStatus=_IssConfigRestoreStatus_Object((1,3,6,1,4,1,2076,81,1,19),_IssConfigRestoreStatus_Type())
issConfigRestoreStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issConfigRestoreStatus.setStatus(_A)
_IssDlImageFromIp_Type=IpAddress
_IssDlImageFromIp_Object=MibScalar
issDlImageFromIp=_IssDlImageFromIp_Object((1,3,6,1,4,1,2076,81,1,20),_IssDlImageFromIp_Type())
issDlImageFromIp.setMaxAccess(_B)
if mibBuilder.loadTexts:issDlImageFromIp.setStatus(_D)
class _IssDlImageName_Type(DisplayString):defaultValue=OctetString('iss.exe');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssDlImageName_Type.__name__=_F
_IssDlImageName_Object=MibScalar
issDlImageName=_IssDlImageName_Object((1,3,6,1,4,1,2076,81,1,21),_IssDlImageName_Type())
issDlImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:issDlImageName.setStatus(_A)
_IssInitiateDlImage_Type=TruthValue
_IssInitiateDlImage_Object=MibScalar
issInitiateDlImage=_IssInitiateDlImage_Object((1,3,6,1,4,1,2076,81,1,22),_IssInitiateDlImage_Type())
issInitiateDlImage.setMaxAccess(_B)
if mibBuilder.loadTexts:issInitiateDlImage.setStatus(_A)
class _IssLoggingOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),('file',2),('flash',3)))
_IssLoggingOption_Type.__name__=_C
_IssLoggingOption_Object=MibScalar
issLoggingOption=_IssLoggingOption_Object((1,3,6,1,4,1,2076,81,1,23),_IssLoggingOption_Type())
issLoggingOption.setMaxAccess(_B)
if mibBuilder.loadTexts:issLoggingOption.setStatus(_A)
_IssUploadLogFileToIp_Type=IpAddress
_IssUploadLogFileToIp_Object=MibScalar
issUploadLogFileToIp=_IssUploadLogFileToIp_Object((1,3,6,1,4,1,2076,81,1,24),_IssUploadLogFileToIp_Type())
issUploadLogFileToIp.setMaxAccess(_B)
if mibBuilder.loadTexts:issUploadLogFileToIp.setStatus(_D)
class _IssLogFileName_Type(DisplayString):defaultValue=OctetString(_j);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssLogFileName_Type.__name__=_F
_IssLogFileName_Object=MibScalar
issLogFileName=_IssLogFileName_Object((1,3,6,1,4,1,2076,81,1,25),_IssLogFileName_Type())
issLogFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issLogFileName.setStatus(_A)
_IssInitiateUlLogFile_Type=TruthValue
_IssInitiateUlLogFile_Object=MibScalar
issInitiateUlLogFile=_IssInitiateUlLogFile_Object((1,3,6,1,4,1,2076,81,1,26),_IssInitiateUlLogFile_Type())
issInitiateUlLogFile.setMaxAccess(_B)
if mibBuilder.loadTexts:issInitiateUlLogFile.setStatus(_A)
class _IssRemoteSaveStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Q,4)))
_IssRemoteSaveStatus_Type.__name__=_C
_IssRemoteSaveStatus_Object=MibScalar
issRemoteSaveStatus=_IssRemoteSaveStatus_Object((1,3,6,1,4,1,2076,81,1,27),_IssRemoteSaveStatus_Type())
issRemoteSaveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issRemoteSaveStatus.setStatus(_A)
class _IssDownloadStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Q,4)))
_IssDownloadStatus_Type.__name__=_C
_IssDownloadStatus_Object=MibScalar
issDownloadStatus=_IssDownloadStatus_Object((1,3,6,1,4,1,2076,81,1,28),_IssDownloadStatus_Type())
issDownloadStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issDownloadStatus.setStatus(_A)
class _IssSysContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_IssSysContact_Type.__name__=_F
_IssSysContact_Object=MibScalar
issSysContact=_IssSysContact_Object((1,3,6,1,4,1,2076,81,1,29),_IssSysContact_Type())
issSysContact.setMaxAccess(_B)
if mibBuilder.loadTexts:issSysContact.setStatus(_D)
class _IssSysLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_IssSysLocation_Type.__name__=_F
_IssSysLocation_Object=MibScalar
issSysLocation=_IssSysLocation_Object((1,3,6,1,4,1,2076,81,1,30),_IssSysLocation_Type())
issSysLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:issSysLocation.setStatus(_D)
class _IssLoginAuthentication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('local',1),('remoteRadius',2),('remoteTacacs',3),('radiusFallbackToLocal',4),('tacacsFallbackToLocal',5)))
_IssLoginAuthentication_Type.__name__=_C
_IssLoginAuthentication_Object=MibScalar
issLoginAuthentication=_IssLoginAuthentication_Object((1,3,6,1,4,1,2076,81,1,31),_IssLoginAuthentication_Type())
issLoginAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:issLoginAuthentication.setStatus(_D)
class _IssSwitchBaseMacAddress_Type(MacAddress):defaultHexValue='000102030405'
_IssSwitchBaseMacAddress_Type.__name__=_g
_IssSwitchBaseMacAddress_Object=MibScalar
issSwitchBaseMacAddress=_IssSwitchBaseMacAddress_Object((1,3,6,1,4,1,2076,81,1,32),_IssSwitchBaseMacAddress_Type())
issSwitchBaseMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchBaseMacAddress.setStatus(_A)
_IssOOBInterface_Type=TruthValue
_IssOOBInterface_Object=MibScalar
issOOBInterface=_IssOOBInterface_Object((1,3,6,1,4,1,2076,81,1,33),_IssOOBInterface_Type())
issOOBInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:issOOBInterface.setStatus(_A)
class _IssSwitchDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_IssSwitchDate_Type.__name__=_F
_IssSwitchDate_Object=MibScalar
issSwitchDate=_IssSwitchDate_Object((1,3,6,1,4,1,2076,81,1,34),_IssSwitchDate_Type())
issSwitchDate.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchDate.setStatus(_A)
_IssNoCliConsole_Type=TruthValue
_IssNoCliConsole_Object=MibScalar
issNoCliConsole=_IssNoCliConsole_Object((1,3,6,1,4,1,2076,81,1,35),_IssNoCliConsole_Type())
issNoCliConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:issNoCliConsole.setStatus(_A)
class _IssDefaultIpAddrAllocProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rarp',1),('dhcp',2),('bootp',3)))
_IssDefaultIpAddrAllocProtocol_Type.__name__=_C
_IssDefaultIpAddrAllocProtocol_Object=MibScalar
issDefaultIpAddrAllocProtocol=_IssDefaultIpAddrAllocProtocol_Object((1,3,6,1,4,1,2076,81,1,36),_IssDefaultIpAddrAllocProtocol_Type())
issDefaultIpAddrAllocProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultIpAddrAllocProtocol.setStatus(_A)
class _IssHttpPort_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssHttpPort_Type.__name__=_C
_IssHttpPort_Object=MibScalar
issHttpPort=_IssHttpPort_Object((1,3,6,1,4,1,2076,81,1,37),_IssHttpPort_Type())
issHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issHttpPort.setStatus(_A)
class _IssHttpStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_N,2)))
_IssHttpStatus_Type.__name__=_C
_IssHttpStatus_Object=MibScalar
issHttpStatus=_IssHttpStatus_Object((1,3,6,1,4,1,2076,81,1,38),_IssHttpStatus_Type())
issHttpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issHttpStatus.setStatus(_A)
class _IssConfigRestoreFileVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_IssConfigRestoreFileVersion_Type.__name__=_F
_IssConfigRestoreFileVersion_Object=MibScalar
issConfigRestoreFileVersion=_IssConfigRestoreFileVersion_Object((1,3,6,1,4,1,2076,81,1,39),_IssConfigRestoreFileVersion_Type())
issConfigRestoreFileVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:issConfigRestoreFileVersion.setStatus(_A)
class _IssDefaultRmIfName_Type(DisplayString):defaultValue=OctetString('NONE');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_IssDefaultRmIfName_Type.__name__=_F
_IssDefaultRmIfName_Object=MibScalar
issDefaultRmIfName=_IssDefaultRmIfName_Object((1,3,6,1,4,1,2076,81,1,40),_IssDefaultRmIfName_Type())
issDefaultRmIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultRmIfName.setStatus(_A)
class _IssDefaultVlanId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IssDefaultVlanId_Type.__name__=_C
_IssDefaultVlanId_Object=MibScalar
issDefaultVlanId=_IssDefaultVlanId_Object((1,3,6,1,4,1,2076,81,1,41),_IssDefaultVlanId_Type())
issDefaultVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultVlanId.setStatus(_A)
class _IssNpapiMode_Type(DisplayString):defaultValue=OctetString('Synchronous');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_IssNpapiMode_Type.__name__=_F
_IssNpapiMode_Object=MibScalar
issNpapiMode=_IssNpapiMode_Object((1,3,6,1,4,1,2076,81,1,42),_IssNpapiMode_Type())
issNpapiMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issNpapiMode.setStatus(_A)
class _IssConfigAutoSaveTrigger_Type(TruthValue):defaultValue=2
_IssConfigAutoSaveTrigger_Type.__name__=_I
_IssConfigAutoSaveTrigger_Object=MibScalar
issConfigAutoSaveTrigger=_IssConfigAutoSaveTrigger_Object((1,3,6,1,4,1,2076,81,1,43),_IssConfigAutoSaveTrigger_Type())
issConfigAutoSaveTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigAutoSaveTrigger.setStatus(_A)
class _IssConfigIncrSaveFlag_Type(TruthValue):defaultValue=2
_IssConfigIncrSaveFlag_Type.__name__=_I
_IssConfigIncrSaveFlag_Object=MibScalar
issConfigIncrSaveFlag=_IssConfigIncrSaveFlag_Object((1,3,6,1,4,1,2076,81,1,44),_IssConfigIncrSaveFlag_Type())
issConfigIncrSaveFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigIncrSaveFlag.setStatus(_A)
class _IssConfigRollbackFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IssConfigRollbackFlag_Type.__name__=_C
_IssConfigRollbackFlag_Object=MibScalar
issConfigRollbackFlag=_IssConfigRollbackFlag_Object((1,3,6,1,4,1,2076,81,1,45),_IssConfigRollbackFlag_Type())
issConfigRollbackFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigRollbackFlag.setStatus(_A)
class _IssConfigSyncUpOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('syncup',1))
_IssConfigSyncUpOperation_Type.__name__=_C
_IssConfigSyncUpOperation_Object=MibScalar
issConfigSyncUpOperation=_IssConfigSyncUpOperation_Object((1,3,6,1,4,1,2076,81,1,46),_IssConfigSyncUpOperation_Type())
issConfigSyncUpOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSyncUpOperation.setStatus(_A)
_IssFrontPanelPortCount_Type=Integer32
_IssFrontPanelPortCount_Object=MibScalar
issFrontPanelPortCount=_IssFrontPanelPortCount_Object((1,3,6,1,4,1,2076,81,1,47),_IssFrontPanelPortCount_Type())
issFrontPanelPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:issFrontPanelPortCount.setStatus(_A)
class _IssAuditLogStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_N,2)))
_IssAuditLogStatus_Type.__name__=_C
_IssAuditLogStatus_Object=MibScalar
issAuditLogStatus=_IssAuditLogStatus_Object((1,3,6,1,4,1,2076,81,1,48),_IssAuditLogStatus_Type())
issAuditLogStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogStatus.setStatus(_A)
class _IssAuditLogFileName_Type(DisplayString):defaultValue=OctetString(_k);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssAuditLogFileName_Type.__name__=_F
_IssAuditLogFileName_Object=MibScalar
issAuditLogFileName=_IssAuditLogFileName_Object((1,3,6,1,4,1,2076,81,1,49),_IssAuditLogFileName_Type())
issAuditLogFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogFileName.setStatus(_A)
class _IssAuditLogFileSize_Type(Unsigned32):defaultValue=1048576;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,1048576))
_IssAuditLogFileSize_Type.__name__=_L
_IssAuditLogFileSize_Object=MibScalar
issAuditLogFileSize=_IssAuditLogFileSize_Object((1,3,6,1,4,1,2076,81,1,50),_IssAuditLogFileSize_Type())
issAuditLogFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogFileSize.setStatus(_A)
class _IssAuditLogReset_Type(TruthValue):defaultValue=2
_IssAuditLogReset_Type.__name__=_I
_IssAuditLogReset_Object=MibScalar
issAuditLogReset=_IssAuditLogReset_Object((1,3,6,1,4,1,2076,81,1,51),_IssAuditLogReset_Type())
issAuditLogReset.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogReset.setStatus(_A)
_IssAuditLogRemoteIpAddr_Type=IpAddress
_IssAuditLogRemoteIpAddr_Object=MibScalar
issAuditLogRemoteIpAddr=_IssAuditLogRemoteIpAddr_Object((1,3,6,1,4,1,2076,81,1,52),_IssAuditLogRemoteIpAddr_Type())
issAuditLogRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogRemoteIpAddr.setStatus(_D)
class _IssAuditLogInitiateTransfer_Type(TruthValue):defaultValue=2
_IssAuditLogInitiateTransfer_Type.__name__=_I
_IssAuditLogInitiateTransfer_Object=MibScalar
issAuditLogInitiateTransfer=_IssAuditLogInitiateTransfer_Object((1,3,6,1,4,1,2076,81,1,53),_IssAuditLogInitiateTransfer_Type())
issAuditLogInitiateTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogInitiateTransfer.setStatus(_A)
class _IssAuditTransferFileName_Type(DisplayString):defaultValue=OctetString(_k);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_IssAuditTransferFileName_Type.__name__=_F
_IssAuditTransferFileName_Object=MibScalar
issAuditTransferFileName=_IssAuditTransferFileName_Object((1,3,6,1,4,1,2076,81,1,54),_IssAuditTransferFileName_Type())
issAuditTransferFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditTransferFileName.setStatus(_A)
class _IssDownLoadTransferMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_IssDownLoadTransferMode_Type.__name__=_C
_IssDownLoadTransferMode_Object=MibScalar
issDownLoadTransferMode=_IssDownLoadTransferMode_Object((1,3,6,1,4,1,2076,81,1,55),_IssDownLoadTransferMode_Type())
issDownLoadTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issDownLoadTransferMode.setStatus(_A)
class _IssDownLoadUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssDownLoadUserName_Type.__name__=_F
_IssDownLoadUserName_Object=MibScalar
issDownLoadUserName=_IssDownLoadUserName_Object((1,3,6,1,4,1,2076,81,1,56),_IssDownLoadUserName_Type())
issDownLoadUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:issDownLoadUserName.setStatus(_A)
class _IssDownLoadPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssDownLoadPassword_Type.__name__=_F
_IssDownLoadPassword_Object=MibScalar
issDownLoadPassword=_IssDownLoadPassword_Object((1,3,6,1,4,1,2076,81,1,57),_IssDownLoadPassword_Type())
issDownLoadPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:issDownLoadPassword.setStatus(_A)
class _IssUploadLogTransferMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_IssUploadLogTransferMode_Type.__name__=_C
_IssUploadLogTransferMode_Object=MibScalar
issUploadLogTransferMode=_IssUploadLogTransferMode_Object((1,3,6,1,4,1,2076,81,1,58),_IssUploadLogTransferMode_Type())
issUploadLogTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issUploadLogTransferMode.setStatus(_A)
class _IssUploadLogUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssUploadLogUserName_Type.__name__=_F
_IssUploadLogUserName_Object=MibScalar
issUploadLogUserName=_IssUploadLogUserName_Object((1,3,6,1,4,1,2076,81,1,59),_IssUploadLogUserName_Type())
issUploadLogUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:issUploadLogUserName.setStatus(_A)
class _IssUploadLogPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssUploadLogPasswd_Type.__name__=_F
_IssUploadLogPasswd_Object=MibScalar
issUploadLogPasswd=_IssUploadLogPasswd_Object((1,3,6,1,4,1,2076,81,1,60),_IssUploadLogPasswd_Type())
issUploadLogPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:issUploadLogPasswd.setStatus(_A)
class _IssConfigSaveTransferMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_IssConfigSaveTransferMode_Type.__name__=_C
_IssConfigSaveTransferMode_Object=MibScalar
issConfigSaveTransferMode=_IssConfigSaveTransferMode_Object((1,3,6,1,4,1,2076,81,1,61),_IssConfigSaveTransferMode_Type())
issConfigSaveTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveTransferMode.setStatus(_A)
class _IssConfigSaveUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssConfigSaveUserName_Type.__name__=_F
_IssConfigSaveUserName_Object=MibScalar
issConfigSaveUserName=_IssConfigSaveUserName_Object((1,3,6,1,4,1,2076,81,1,62),_IssConfigSaveUserName_Type())
issConfigSaveUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveUserName.setStatus(_A)
class _IssConfigSavePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssConfigSavePassword_Type.__name__=_F
_IssConfigSavePassword_Object=MibScalar
issConfigSavePassword=_IssConfigSavePassword_Object((1,3,6,1,4,1,2076,81,1,63),_IssConfigSavePassword_Type())
issConfigSavePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSavePassword.setStatus(_A)
class _IssSwitchMinThresholdTemperature_Type(Integer32):defaultValue=-5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-35,30))
_IssSwitchMinThresholdTemperature_Type.__name__=_C
_IssSwitchMinThresholdTemperature_Object=MibScalar
issSwitchMinThresholdTemperature=_IssSwitchMinThresholdTemperature_Object((1,3,6,1,4,1,2076,81,1,64),_IssSwitchMinThresholdTemperature_Type())
issSwitchMinThresholdTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchMinThresholdTemperature.setStatus(_A)
class _IssSwitchMaxThresholdTemperature_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(35,90))
_IssSwitchMaxThresholdTemperature_Type.__name__=_C
_IssSwitchMaxThresholdTemperature_Object=MibScalar
issSwitchMaxThresholdTemperature=_IssSwitchMaxThresholdTemperature_Object((1,3,6,1,4,1,2076,81,1,65),_IssSwitchMaxThresholdTemperature_Type())
issSwitchMaxThresholdTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchMaxThresholdTemperature.setStatus(_A)
_IssSwitchCurrentTemperature_Type=Integer32
_IssSwitchCurrentTemperature_Object=MibScalar
issSwitchCurrentTemperature=_IssSwitchCurrentTemperature_Object((1,3,6,1,4,1,2076,81,1,66),_IssSwitchCurrentTemperature_Type())
issSwitchCurrentTemperature.setMaxAccess(_G)
if mibBuilder.loadTexts:issSwitchCurrentTemperature.setStatus(_A)
class _IssSwitchMaxCPUThreshold_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IssSwitchMaxCPUThreshold_Type.__name__=_C
_IssSwitchMaxCPUThreshold_Object=MibScalar
issSwitchMaxCPUThreshold=_IssSwitchMaxCPUThreshold_Object((1,3,6,1,4,1,2076,81,1,67),_IssSwitchMaxCPUThreshold_Type())
issSwitchMaxCPUThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchMaxCPUThreshold.setStatus(_A)
_IssSwitchCurrentCPUThreshold_Type=Integer32
_IssSwitchCurrentCPUThreshold_Object=MibScalar
issSwitchCurrentCPUThreshold=_IssSwitchCurrentCPUThreshold_Object((1,3,6,1,4,1,2076,81,1,68),_IssSwitchCurrentCPUThreshold_Type())
issSwitchCurrentCPUThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:issSwitchCurrentCPUThreshold.setStatus(_A)
class _IssSwitchPowerSurge_Type(Integer32):defaultValue=230;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IssSwitchPowerSurge_Type.__name__=_C
_IssSwitchPowerSurge_Object=MibScalar
issSwitchPowerSurge=_IssSwitchPowerSurge_Object((1,3,6,1,4,1,2076,81,1,69),_IssSwitchPowerSurge_Type())
issSwitchPowerSurge.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchPowerSurge.setStatus(_A)
class _IssSwitchPowerFailure_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IssSwitchPowerFailure_Type.__name__=_C
_IssSwitchPowerFailure_Object=MibScalar
issSwitchPowerFailure=_IssSwitchPowerFailure_Object((1,3,6,1,4,1,2076,81,1,70),_IssSwitchPowerFailure_Type())
issSwitchPowerFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchPowerFailure.setStatus(_A)
_IssSwitchCurrentPowerSupply_Type=Integer32
_IssSwitchCurrentPowerSupply_Object=MibScalar
issSwitchCurrentPowerSupply=_IssSwitchCurrentPowerSupply_Object((1,3,6,1,4,1,2076,81,1,71),_IssSwitchCurrentPowerSupply_Type())
issSwitchCurrentPowerSupply.setMaxAccess(_G)
if mibBuilder.loadTexts:issSwitchCurrentPowerSupply.setStatus(_A)
class _IssSwitchMaxRAMUsage_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IssSwitchMaxRAMUsage_Type.__name__=_C
_IssSwitchMaxRAMUsage_Object=MibScalar
issSwitchMaxRAMUsage=_IssSwitchMaxRAMUsage_Object((1,3,6,1,4,1,2076,81,1,72),_IssSwitchMaxRAMUsage_Type())
issSwitchMaxRAMUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchMaxRAMUsage.setStatus(_A)
_IssSwitchCurrentRAMUsage_Type=Integer32
_IssSwitchCurrentRAMUsage_Object=MibScalar
issSwitchCurrentRAMUsage=_IssSwitchCurrentRAMUsage_Object((1,3,6,1,4,1,2076,81,1,73),_IssSwitchCurrentRAMUsage_Type())
issSwitchCurrentRAMUsage.setMaxAccess(_G)
if mibBuilder.loadTexts:issSwitchCurrentRAMUsage.setStatus(_A)
class _IssSwitchMaxFlashUsage_Type(Integer32):defaultValue=95;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_IssSwitchMaxFlashUsage_Type.__name__=_C
_IssSwitchMaxFlashUsage_Object=MibScalar
issSwitchMaxFlashUsage=_IssSwitchMaxFlashUsage_Object((1,3,6,1,4,1,2076,81,1,74),_IssSwitchMaxFlashUsage_Type())
issSwitchMaxFlashUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchMaxFlashUsage.setStatus(_A)
_IssSwitchCurrentFlashUsage_Type=Integer32
_IssSwitchCurrentFlashUsage_Object=MibScalar
issSwitchCurrentFlashUsage=_IssSwitchCurrentFlashUsage_Object((1,3,6,1,4,1,2076,81,1,75),_IssSwitchCurrentFlashUsage_Type())
issSwitchCurrentFlashUsage.setMaxAccess(_G)
if mibBuilder.loadTexts:issSwitchCurrentFlashUsage.setStatus(_A)
class _IssConfigRestoreFileFormatVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_IssConfigRestoreFileFormatVersion_Type.__name__=_F
_IssConfigRestoreFileFormatVersion_Object=MibScalar
issConfigRestoreFileFormatVersion=_IssConfigRestoreFileFormatVersion_Object((1,3,6,1,4,1,2076,81,1,76),_IssConfigRestoreFileFormatVersion_Type())
issConfigRestoreFileFormatVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:issConfigRestoreFileFormatVersion.setStatus(_A)
class _IssDebugOption_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,288))
_IssDebugOption_Type.__name__=_F
_IssDebugOption_Object=MibScalar
issDebugOption=_IssDebugOption_Object((1,3,6,1,4,1,2076,81,1,77),_IssDebugOption_Type())
issDebugOption.setMaxAccess(_B)
if mibBuilder.loadTexts:issDebugOption.setStatus(_A)
class _IssConfigDefaultValueSaveOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssConfigDefaultValueSaveOption_Type.__name__=_C
_IssConfigDefaultValueSaveOption_Object=MibScalar
issConfigDefaultValueSaveOption=_IssConfigDefaultValueSaveOption_Object((1,3,6,1,4,1,2076,81,1,78),_IssConfigDefaultValueSaveOption_Type())
issConfigDefaultValueSaveOption.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigDefaultValueSaveOption.setStatus(_A)
_IssConfigSaveIpAddrType_Type=InetAddressType
_IssConfigSaveIpAddrType_Object=MibScalar
issConfigSaveIpAddrType=_IssConfigSaveIpAddrType_Object((1,3,6,1,4,1,2076,81,1,79),_IssConfigSaveIpAddrType_Type())
issConfigSaveIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveIpAddrType.setStatus(_A)
_IssConfigSaveIpvxAddr_Type=InetAddress
_IssConfigSaveIpvxAddr_Object=MibScalar
issConfigSaveIpvxAddr=_IssConfigSaveIpvxAddr_Object((1,3,6,1,4,1,2076,81,1,80),_IssConfigSaveIpvxAddr_Type())
issConfigSaveIpvxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigSaveIpvxAddr.setStatus(_A)
_IssConfigRestoreIpAddrType_Type=InetAddressType
_IssConfigRestoreIpAddrType_Object=MibScalar
issConfigRestoreIpAddrType=_IssConfigRestoreIpAddrType_Object((1,3,6,1,4,1,2076,81,1,81),_IssConfigRestoreIpAddrType_Type())
issConfigRestoreIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigRestoreIpAddrType.setStatus(_A)
_IssConfigRestoreIpvxAddr_Type=InetAddress
_IssConfigRestoreIpvxAddr_Object=MibScalar
issConfigRestoreIpvxAddr=_IssConfigRestoreIpvxAddr_Object((1,3,6,1,4,1,2076,81,1,82),_IssConfigRestoreIpvxAddr_Type())
issConfigRestoreIpvxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigRestoreIpvxAddr.setStatus(_A)
_IssDlImageFromIpAddrType_Type=InetAddressType
_IssDlImageFromIpAddrType_Object=MibScalar
issDlImageFromIpAddrType=_IssDlImageFromIpAddrType_Object((1,3,6,1,4,1,2076,81,1,83),_IssDlImageFromIpAddrType_Type())
issDlImageFromIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issDlImageFromIpAddrType.setStatus(_A)
_IssDlImageFromIpvx_Type=InetAddress
_IssDlImageFromIpvx_Object=MibScalar
issDlImageFromIpvx=_IssDlImageFromIpvx_Object((1,3,6,1,4,1,2076,81,1,84),_IssDlImageFromIpvx_Type())
issDlImageFromIpvx.setMaxAccess(_B)
if mibBuilder.loadTexts:issDlImageFromIpvx.setStatus(_A)
_IssUploadLogFileToIpAddrType_Type=InetAddressType
_IssUploadLogFileToIpAddrType_Object=MibScalar
issUploadLogFileToIpAddrType=_IssUploadLogFileToIpAddrType_Object((1,3,6,1,4,1,2076,81,1,85),_IssUploadLogFileToIpAddrType_Type())
issUploadLogFileToIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issUploadLogFileToIpAddrType.setStatus(_A)
_IssUploadLogFileToIpvx_Type=InetAddress
_IssUploadLogFileToIpvx_Object=MibScalar
issUploadLogFileToIpvx=_IssUploadLogFileToIpvx_Object((1,3,6,1,4,1,2076,81,1,86),_IssUploadLogFileToIpvx_Type())
issUploadLogFileToIpvx.setMaxAccess(_B)
if mibBuilder.loadTexts:issUploadLogFileToIpvx.setStatus(_A)
_IssAuditLogRemoteIpAddrType_Type=InetAddressType
_IssAuditLogRemoteIpAddrType_Object=MibScalar
issAuditLogRemoteIpAddrType=_IssAuditLogRemoteIpAddrType_Object((1,3,6,1,4,1,2076,81,1,87),_IssAuditLogRemoteIpAddrType_Type())
issAuditLogRemoteIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogRemoteIpAddrType.setStatus(_A)
_IssAuditLogRemoteIpvxAddr_Type=InetAddress
_IssAuditLogRemoteIpvxAddr_Object=MibScalar
issAuditLogRemoteIpvxAddr=_IssAuditLogRemoteIpvxAddr_Object((1,3,6,1,4,1,2076,81,1,88),_IssAuditLogRemoteIpvxAddr_Type())
issAuditLogRemoteIpvxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogRemoteIpvxAddr.setStatus(_A)
class _IssSystemTimerSpeed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_IssSystemTimerSpeed_Type.__name__=_L
_IssSystemTimerSpeed_Object=MibScalar
issSystemTimerSpeed=_IssSystemTimerSpeed_Object((1,3,6,1,4,1,2076,81,1,89),_IssSystemTimerSpeed_Type())
issSystemTimerSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:issSystemTimerSpeed.setStatus(_A)
class _IssMgmtInterfaceRouting_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssMgmtInterfaceRouting_Type.__name__=_C
_IssMgmtInterfaceRouting_Object=MibScalar
issMgmtInterfaceRouting=_IssMgmtInterfaceRouting_Object((1,3,6,1,4,1,2076,81,1,90),_IssMgmtInterfaceRouting_Type())
issMgmtInterfaceRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:issMgmtInterfaceRouting.setStatus(_A)
class _IssMacLearnRateLimit_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IssMacLearnRateLimit_Type.__name__=_C
_IssMacLearnRateLimit_Object=MibScalar
issMacLearnRateLimit=_IssMacLearnRateLimit_Object((1,3,6,1,4,1,2076,81,1,91),_IssMacLearnRateLimit_Type())
issMacLearnRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:issMacLearnRateLimit.setStatus(_A)
class _IssMacLearnRateLimitInterval_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_IssMacLearnRateLimitInterval_Type.__name__=_L
_IssMacLearnRateLimitInterval_Object=MibScalar
issMacLearnRateLimitInterval=_IssMacLearnRateLimitInterval_Object((1,3,6,1,4,1,2076,81,1,92),_IssMacLearnRateLimitInterval_Type())
issMacLearnRateLimitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:issMacLearnRateLimitInterval.setStatus(_A)
if mibBuilder.loadTexts:issMacLearnRateLimitInterval.setUnits('milliseconds')
class _IssVrfUnqMacFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_R,1)))
_IssVrfUnqMacFlag_Type.__name__=_C
_IssVrfUnqMacFlag_Object=MibScalar
issVrfUnqMacFlag=_IssVrfUnqMacFlag_Object((1,3,6,1,4,1,2076,81,1,93),_IssVrfUnqMacFlag_Type())
issVrfUnqMacFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:issVrfUnqMacFlag.setStatus(_A)
class _IssLoginAttempts_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IssLoginAttempts_Type.__name__=_C
_IssLoginAttempts_Object=MibScalar
issLoginAttempts=_IssLoginAttempts_Object((1,3,6,1,4,1,2076,81,1,94),_IssLoginAttempts_Type())
issLoginAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:issLoginAttempts.setStatus(_A)
class _IssLoginLockTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_IssLoginLockTime_Type.__name__=_C
_IssLoginLockTime_Object=MibScalar
issLoginLockTime=_IssLoginLockTime_Object((1,3,6,1,4,1,2076,81,1,95),_IssLoginLockTime_Type())
issLoginLockTime.setMaxAccess(_B)
if mibBuilder.loadTexts:issLoginLockTime.setStatus(_A)
class _IssAuditLogSizeThreshold_Type(Unsigned32):defaultValue=70;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_IssAuditLogSizeThreshold_Type.__name__=_L
_IssAuditLogSizeThreshold_Object=MibScalar
issAuditLogSizeThreshold=_IssAuditLogSizeThreshold_Object((1,3,6,1,4,1,2076,81,1,96),_IssAuditLogSizeThreshold_Type())
issAuditLogSizeThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:issAuditLogSizeThreshold.setStatus(_A)
class _IssTelnetStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_N,2),('enableInProgress',3),('disableInProgress',4)))
_IssTelnetStatus_Type.__name__=_C
_IssTelnetStatus_Object=MibScalar
issTelnetStatus=_IssTelnetStatus_Object((1,3,6,1,4,1,2076,81,1,97),_IssTelnetStatus_Type())
issTelnetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issTelnetStatus.setStatus(_A)
class _IssWebSessionTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_IssWebSessionTimeOut_Type.__name__=_C
_IssWebSessionTimeOut_Object=MibScalar
issWebSessionTimeOut=_IssWebSessionTimeOut_Object((1,3,6,1,4,1,2076,81,1,98),_IssWebSessionTimeOut_Type())
issWebSessionTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:issWebSessionTimeOut.setStatus(_A)
class _IssWebSessionMaxUsers_Type(Integer32):defaultValue=7
_IssWebSessionMaxUsers_Type.__name__=_C
_IssWebSessionMaxUsers_Object=MibScalar
issWebSessionMaxUsers=_IssWebSessionMaxUsers_Object((1,3,6,1,4,1,2076,81,1,99),_IssWebSessionMaxUsers_Type())
issWebSessionMaxUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:issWebSessionMaxUsers.setStatus(_A)
class _IssHeartBeatMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_IssHeartBeatMode_Type.__name__=_C
_IssHeartBeatMode_Object=MibScalar
issHeartBeatMode=_IssHeartBeatMode_Object((1,3,6,1,4,1,2076,81,1,100),_IssHeartBeatMode_Type())
issHeartBeatMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issHeartBeatMode.setStatus(_A)
class _IssRmRType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hot',1),('cold',2)))
_IssRmRType_Type.__name__=_C
_IssRmRType_Object=MibScalar
issRmRType=_IssRmRType_Object((1,3,6,1,4,1,2076,81,1,101),_IssRmRType_Type())
issRmRType.setMaxAccess(_B)
if mibBuilder.loadTexts:issRmRType.setStatus(_A)
class _IssRmDType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shared',1),('separate',2)))
_IssRmDType_Type.__name__=_C
_IssRmDType_Object=MibScalar
issRmDType=_IssRmDType_Object((1,3,6,1,4,1,2076,81,1,102),_IssRmDType_Type())
issRmDType.setMaxAccess(_B)
if mibBuilder.loadTexts:issRmDType.setStatus(_A)
class _IssClearConfig_Type(TruthValue):defaultValue=2
_IssClearConfig_Type.__name__=_I
_IssClearConfig_Object=MibScalar
issClearConfig=_IssClearConfig_Object((1,3,6,1,4,1,2076,81,1,103),_IssClearConfig_Type())
issClearConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:issClearConfig.setStatus(_A)
class _IssClearConfigFileName_Type(DisplayString):defaultValue=OctetString('clear.conf');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssClearConfigFileName_Type.__name__=_F
_IssClearConfigFileName_Object=MibScalar
issClearConfigFileName=_IssClearConfigFileName_Object((1,3,6,1,4,1,2076,81,1,104),_IssClearConfigFileName_Type())
issClearConfigFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issClearConfigFileName.setStatus(_A)
class _IssTelnetClientStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_IssTelnetClientStatus_Type.__name__=_C
_IssTelnetClientStatus_Object=MibScalar
issTelnetClientStatus=_IssTelnetClientStatus_Object((1,3,6,1,4,1,2076,81,1,105),_IssTelnetClientStatus_Type())
issTelnetClientStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issTelnetClientStatus.setStatus(_A)
class _IssSshClientStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_IssSshClientStatus_Type.__name__=_C
_IssSshClientStatus_Object=MibScalar
issSshClientStatus=_IssSshClientStatus_Object((1,3,6,1,4,1,2076,81,1,106),_IssSshClientStatus_Type())
issSshClientStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issSshClientStatus.setStatus(_A)
_IssActiveTelnetClientSessions_Type=Integer32
_IssActiveTelnetClientSessions_Object=MibScalar
issActiveTelnetClientSessions=_IssActiveTelnetClientSessions_Object((1,3,6,1,4,1,2076,81,1,107),_IssActiveTelnetClientSessions_Type())
issActiveTelnetClientSessions.setMaxAccess(_G)
if mibBuilder.loadTexts:issActiveTelnetClientSessions.setStatus(_A)
_IssActiveSshClientSessions_Type=Integer32
_IssActiveSshClientSessions_Object=MibScalar
issActiveSshClientSessions=_IssActiveSshClientSessions_Object((1,3,6,1,4,1,2076,81,1,108),_IssActiveSshClientSessions_Type())
issActiveSshClientSessions.setMaxAccess(_G)
if mibBuilder.loadTexts:issActiveSshClientSessions.setStatus(_A)
class _IssLogFileSize_Type(Unsigned32):defaultValue=1048576
_IssLogFileSize_Type.__name__=_L
_IssLogFileSize_Object=MibScalar
issLogFileSize=_IssLogFileSize_Object((1,3,6,1,4,1,2076,81,1,109),_IssLogFileSize_Type())
issLogFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:issLogFileSize.setStatus(_A)
class _IssLogReset_Type(TruthValue):defaultValue=2
_IssLogReset_Type.__name__=_I
_IssLogReset_Object=MibScalar
issLogReset=_IssLogReset_Object((1,3,6,1,4,1,2076,81,1,110),_IssLogReset_Type())
issLogReset.setMaxAccess(_B)
if mibBuilder.loadTexts:issLogReset.setStatus(_A)
class _IssLogSizeThreshold_Type(Unsigned32):defaultValue=70;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_IssLogSizeThreshold_Type.__name__=_L
_IssLogSizeThreshold_Object=MibScalar
issLogSizeThreshold=_IssLogSizeThreshold_Object((1,3,6,1,4,1,2076,81,1,111),_IssLogSizeThreshold_Type())
issLogSizeThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:issLogSizeThreshold.setStatus(_A)
class _IssAutomaticPortCreate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssAutomaticPortCreate_Type.__name__=_C
_IssAutomaticPortCreate_Object=MibScalar
issAutomaticPortCreate=_IssAutomaticPortCreate_Object((1,3,6,1,4,1,2076,81,1,112),_IssAutomaticPortCreate_Type())
issAutomaticPortCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:issAutomaticPortCreate.setStatus(_A)
class _IssUlRemoteLogFileName_Type(DisplayString):defaultValue=OctetString(_j);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssUlRemoteLogFileName_Type.__name__=_F
_IssUlRemoteLogFileName_Object=MibScalar
issUlRemoteLogFileName=_IssUlRemoteLogFileName_Object((1,3,6,1,4,1,2076,81,1,113),_IssUlRemoteLogFileName_Type())
issUlRemoteLogFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issUlRemoteLogFileName.setStatus(_A)
_IssDefaultExecTimeOut_Type=Unsigned32
_IssDefaultExecTimeOut_Object=MibScalar
issDefaultExecTimeOut=_IssDefaultExecTimeOut_Object((1,3,6,1,4,1,2076,81,1,114),_IssDefaultExecTimeOut_Type())
issDefaultExecTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:issDefaultExecTimeOut.setStatus(_A)
class _IssRmStackingInterfaceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oob',1),('inband',2)))
_IssRmStackingInterfaceType_Type.__name__=_C
_IssRmStackingInterfaceType_Object=MibScalar
issRmStackingInterfaceType=_IssRmStackingInterfaceType_Object((1,3,6,1,4,1,2076,81,1,115),_IssRmStackingInterfaceType_Type())
issRmStackingInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:issRmStackingInterfaceType.setStatus(_A)
class _IssPeerLoggingOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),('file',2),('flash',3)))
_IssPeerLoggingOption_Type.__name__=_C
_IssPeerLoggingOption_Object=MibScalar
issPeerLoggingOption=_IssPeerLoggingOption_Object((1,3,6,1,4,1,2076,81,1,116),_IssPeerLoggingOption_Type())
issPeerLoggingOption.setMaxAccess(_B)
if mibBuilder.loadTexts:issPeerLoggingOption.setStatus(_A)
class _IssStandbyRestart_Type(TruthValue):defaultValue=2
_IssStandbyRestart_Type.__name__=_I
_IssStandbyRestart_Object=MibScalar
issStandbyRestart=_IssStandbyRestart_Object((1,3,6,1,4,1,2076,81,1,117),_IssStandbyRestart_Type())
issStandbyRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:issStandbyRestart.setStatus(_A)
class _IssRestoreType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('msr',1),('csr',2)))
_IssRestoreType_Type.__name__=_C
_IssRestoreType_Object=MibScalar
issRestoreType=_IssRestoreType_Object((1,3,6,1,4,1,2076,81,1,118),_IssRestoreType_Type())
issRestoreType.setMaxAccess(_B)
if mibBuilder.loadTexts:issRestoreType.setStatus(_A)
class _IssSwitchModeType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cutThrough',1),('storeForward',2)))
_IssSwitchModeType_Type.__name__=_C
_IssSwitchModeType_Object=MibScalar
issSwitchModeType=_IssSwitchModeType_Object((1,3,6,1,4,1,2076,81,1,119),_IssSwitchModeType_Type())
issSwitchModeType.setMaxAccess(_B)
if mibBuilder.loadTexts:issSwitchModeType.setStatus(_A)
class _IssHardwareSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_IssHardwareSerialNumber_Type.__name__=_F
_IssHardwareSerialNumber_Object=MibScalar
issHardwareSerialNumber=_IssHardwareSerialNumber_Object((1,3,6,1,4,1,2076,81,1,120),_IssHardwareSerialNumber_Type())
issHardwareSerialNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:issHardwareSerialNumber.setStatus(_A)
class _IssDlImageType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('firmware',1),('bootloader',2)))
_IssDlImageType_Type.__name__=_C
_IssDlImageType_Object=MibScalar
issDlImageType=_IssDlImageType_Object((1,3,6,1,4,1,2076,81,1,121),_IssDlImageType_Type())
issDlImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:issDlImageType.setStatus(_A)
_IssConfigControl_ObjectIdentity=ObjectIdentity
issConfigControl=_IssConfigControl_ObjectIdentity((1,3,6,1,4,1,2076,81,2))
_IssConfigCtrlTable_Object=MibTable
issConfigCtrlTable=_IssConfigCtrlTable_Object((1,3,6,1,4,1,2076,81,2,1))
if mibBuilder.loadTexts:issConfigCtrlTable.setStatus(_A)
_IssConfigCtrlEntry_Object=MibTableRow
issConfigCtrlEntry=_IssConfigCtrlEntry_Object((1,3,6,1,4,1,2076,81,2,1,1))
issConfigCtrlEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:issConfigCtrlEntry.setStatus(_A)
class _IssConfigCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssConfigCtrlIndex_Type.__name__=_C
_IssConfigCtrlIndex_Object=MibTableColumn
issConfigCtrlIndex=_IssConfigCtrlIndex_Object((1,3,6,1,4,1,2076,81,2,1,1,1),_IssConfigCtrlIndex_Type())
issConfigCtrlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:issConfigCtrlIndex.setStatus(_A)
class _IssConfigCtrlEgressStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssConfigCtrlEgressStatus_Type.__name__=_C
_IssConfigCtrlEgressStatus_Object=MibTableColumn
issConfigCtrlEgressStatus=_IssConfigCtrlEgressStatus_Object((1,3,6,1,4,1,2076,81,2,1,1,2),_IssConfigCtrlEgressStatus_Type())
issConfigCtrlEgressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigCtrlEgressStatus.setStatus(_A)
class _IssConfigCtrlStatsCollection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssConfigCtrlStatsCollection_Type.__name__=_C
_IssConfigCtrlStatsCollection_Object=MibTableColumn
issConfigCtrlStatsCollection=_IssConfigCtrlStatsCollection_Object((1,3,6,1,4,1,2076,81,2,1,1,3),_IssConfigCtrlStatsCollection_Type())
issConfigCtrlStatsCollection.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigCtrlStatsCollection.setStatus(_A)
class _IssConfigCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_Y,2)))
_IssConfigCtrlStatus_Type.__name__=_C
_IssConfigCtrlStatus_Object=MibTableColumn
issConfigCtrlStatus=_IssConfigCtrlStatus_Object((1,3,6,1,4,1,2076,81,2,1,1,4),_IssConfigCtrlStatus_Type())
issConfigCtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issConfigCtrlStatus.setStatus(_A)
_IssPortCtrlTable_Object=MibTable
issPortCtrlTable=_IssPortCtrlTable_Object((1,3,6,1,4,1,2076,81,2,2))
if mibBuilder.loadTexts:issPortCtrlTable.setStatus(_A)
_IssPortCtrlEntry_Object=MibTableRow
issPortCtrlEntry=_IssPortCtrlEntry_Object((1,3,6,1,4,1,2076,81,2,2,1))
issPortCtrlEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:issPortCtrlEntry.setStatus(_A)
class _IssPortCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssPortCtrlIndex_Type.__name__=_C
_IssPortCtrlIndex_Object=MibTableColumn
issPortCtrlIndex=_IssPortCtrlIndex_Object((1,3,6,1,4,1,2076,81,2,2,1,1),_IssPortCtrlIndex_Type())
issPortCtrlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:issPortCtrlIndex.setStatus(_A)
class _IssPortCtrlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('noNegotiation',2)))
_IssPortCtrlMode_Type.__name__=_C
_IssPortCtrlMode_Object=MibTableColumn
issPortCtrlMode=_IssPortCtrlMode_Object((1,3,6,1,4,1,2076,81,2,2,1,2),_IssPortCtrlMode_Type())
issPortCtrlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlMode.setStatus(_A)
class _IssPortCtrlDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('half',2)))
_IssPortCtrlDuplex_Type.__name__=_C
_IssPortCtrlDuplex_Object=MibTableColumn
issPortCtrlDuplex=_IssPortCtrlDuplex_Object((1,3,6,1,4,1,2076,81,2,2,1,3),_IssPortCtrlDuplex_Type())
issPortCtrlDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlDuplex.setStatus(_A)
class _IssPortCtrlSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('tenMBPS',1),('hundredMBPS',2),('oneGB',3),('tenGB',4),('fortyGB',5),('fiftyGB',6),('twothousandfivehundredMBPS',7),('twentyfiveGB',8),('onehundredGB',9)))
_IssPortCtrlSpeed_Type.__name__=_C
_IssPortCtrlSpeed_Object=MibTableColumn
issPortCtrlSpeed=_IssPortCtrlSpeed_Object((1,3,6,1,4,1,2076,81,2,2,1,4),_IssPortCtrlSpeed_Type())
issPortCtrlSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlSpeed.setStatus(_A)
class _IssPortCtrlFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_N,2)))
_IssPortCtrlFlowControl_Type.__name__=_C
_IssPortCtrlFlowControl_Object=MibTableColumn
issPortCtrlFlowControl=_IssPortCtrlFlowControl_Object((1,3,6,1,4,1,2076,81,2,2,1,5),_IssPortCtrlFlowControl_Type())
issPortCtrlFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlFlowControl.setStatus(_D)
class _IssPortCtrlRenegotiate_Type(TruthValue):defaultValue=2
_IssPortCtrlRenegotiate_Type.__name__=_I
_IssPortCtrlRenegotiate_Object=MibTableColumn
issPortCtrlRenegotiate=_IssPortCtrlRenegotiate_Object((1,3,6,1,4,1,2076,81,2,2,1,6),_IssPortCtrlRenegotiate_Type())
issPortCtrlRenegotiate.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlRenegotiate.setStatus(_A)
_IssPortCtrlMaxMacAddr_Type=Integer32
_IssPortCtrlMaxMacAddr_Object=MibTableColumn
issPortCtrlMaxMacAddr=_IssPortCtrlMaxMacAddr_Object((1,3,6,1,4,1,2076,81,2,2,1,7),_IssPortCtrlMaxMacAddr_Type())
issPortCtrlMaxMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlMaxMacAddr.setStatus(_A)
class _IssPortCtrlMaxMacAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),('purgeLRU',2)))
_IssPortCtrlMaxMacAction_Type.__name__=_C
_IssPortCtrlMaxMacAction_Object=MibTableColumn
issPortCtrlMaxMacAction=_IssPortCtrlMaxMacAction_Object((1,3,6,1,4,1,2076,81,2,2,1,8),_IssPortCtrlMaxMacAction_Type())
issPortCtrlMaxMacAction.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlMaxMacAction.setStatus(_A)
class _IssPortHOLBlockPrevention_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IssPortHOLBlockPrevention_Type.__name__=_C
_IssPortHOLBlockPrevention_Object=MibTableColumn
issPortHOLBlockPrevention=_IssPortHOLBlockPrevention_Object((1,3,6,1,4,1,2076,81,2,2,1,9),_IssPortHOLBlockPrevention_Type())
issPortHOLBlockPrevention.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortHOLBlockPrevention.setStatus(_A)
_IssPortAutoNegAdvtCapBits_Type=OctetString
_IssPortAutoNegAdvtCapBits_Object=MibTableColumn
issPortAutoNegAdvtCapBits=_IssPortAutoNegAdvtCapBits_Object((1,3,6,1,4,1,2076,81,2,2,1,10),_IssPortAutoNegAdvtCapBits_Type())
issPortAutoNegAdvtCapBits.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortAutoNegAdvtCapBits.setStatus(_A)
class _IssPortCpuControlledLearning_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IssPortCpuControlledLearning_Type.__name__=_C
_IssPortCpuControlledLearning_Object=MibTableColumn
issPortCpuControlledLearning=_IssPortCpuControlledLearning_Object((1,3,6,1,4,1,2076,81,2,2,1,11),_IssPortCpuControlledLearning_Type())
issPortCpuControlledLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCpuControlledLearning.setStatus(_A)
class _IssPortMdiOrMdixCap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('mdi',2),('mdix',3)))
_IssPortMdiOrMdixCap_Type.__name__=_C
_IssPortMdiOrMdixCap_Object=MibTableColumn
issPortMdiOrMdixCap=_IssPortMdiOrMdixCap_Object((1,3,6,1,4,1,2076,81,2,2,1,12),_IssPortMdiOrMdixCap_Type())
issPortMdiOrMdixCap.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortMdiOrMdixCap.setStatus(_A)
class _IssPortCtrlFlowControlMaxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80000000))
_IssPortCtrlFlowControlMaxRate_Type.__name__=_C
_IssPortCtrlFlowControlMaxRate_Object=MibTableColumn
issPortCtrlFlowControlMaxRate=_IssPortCtrlFlowControlMaxRate_Object((1,3,6,1,4,1,2076,81,2,2,1,13),_IssPortCtrlFlowControlMaxRate_Type())
issPortCtrlFlowControlMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlFlowControlMaxRate.setStatus(_A)
class _IssPortCtrlFlowControlMinRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80000000))
_IssPortCtrlFlowControlMinRate_Type.__name__=_C
_IssPortCtrlFlowControlMinRate_Object=MibTableColumn
issPortCtrlFlowControlMinRate=_IssPortCtrlFlowControlMinRate_Object((1,3,6,1,4,1,2076,81,2,2,1,14),_IssPortCtrlFlowControlMinRate_Type())
issPortCtrlFlowControlMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:issPortCtrlFlowControlMinRate.setStatus(_A)
_IssPortIsolationTable_Object=MibTable
issPortIsolationTable=_IssPortIsolationTable_Object((1,3,6,1,4,1,2076,81,2,3))
if mibBuilder.loadTexts:issPortIsolationTable.setStatus(_A)
_IssPortIsolationEntry_Object=MibTableRow
issPortIsolationEntry=_IssPortIsolationEntry_Object((1,3,6,1,4,1,2076,81,2,3,1))
issPortIsolationEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:issPortIsolationEntry.setStatus(_A)
_IssPortIsolationIngressPort_Type=InterfaceIndex
_IssPortIsolationIngressPort_Object=MibTableColumn
issPortIsolationIngressPort=_IssPortIsolationIngressPort_Object((1,3,6,1,4,1,2076,81,2,3,1,1),_IssPortIsolationIngressPort_Type())
issPortIsolationIngressPort.setMaxAccess(_H)
if mibBuilder.loadTexts:issPortIsolationIngressPort.setStatus(_A)
class _IssPortIsolationInVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IssPortIsolationInVlanId_Type.__name__=_C
_IssPortIsolationInVlanId_Object=MibTableColumn
issPortIsolationInVlanId=_IssPortIsolationInVlanId_Object((1,3,6,1,4,1,2076,81,2,3,1,2),_IssPortIsolationInVlanId_Type())
issPortIsolationInVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:issPortIsolationInVlanId.setStatus(_A)
_IssPortIsolationEgressPort_Type=InterfaceIndex
_IssPortIsolationEgressPort_Object=MibTableColumn
issPortIsolationEgressPort=_IssPortIsolationEgressPort_Object((1,3,6,1,4,1,2076,81,2,3,1,3),_IssPortIsolationEgressPort_Type())
issPortIsolationEgressPort.setMaxAccess(_H)
if mibBuilder.loadTexts:issPortIsolationEgressPort.setStatus(_A)
_IssPortIsolationStorageType_Type=StorageType
_IssPortIsolationStorageType_Object=MibTableColumn
issPortIsolationStorageType=_IssPortIsolationStorageType_Object((1,3,6,1,4,1,2076,81,2,3,1,4),_IssPortIsolationStorageType_Type())
issPortIsolationStorageType.setMaxAccess(_G)
if mibBuilder.loadTexts:issPortIsolationStorageType.setStatus(_A)
_IssPortIsolationRowStatus_Type=RowStatus
_IssPortIsolationRowStatus_Object=MibTableColumn
issPortIsolationRowStatus=_IssPortIsolationRowStatus_Object((1,3,6,1,4,1,2076,81,2,3,1,5),_IssPortIsolationRowStatus_Type())
issPortIsolationRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:issPortIsolationRowStatus.setStatus(_A)
_IssMirror_ObjectIdentity=ObjectIdentity
issMirror=_IssMirror_ObjectIdentity((1,3,6,1,4,1,2076,81,3))
class _IssMirrorStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_IssMirrorStatus_Type.__name__=_C
_IssMirrorStatus_Object=MibScalar
issMirrorStatus=_IssMirrorStatus_Object((1,3,6,1,4,1,2076,81,3,1),_IssMirrorStatus_Type())
issMirrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorStatus.setStatus(_A)
_IssMirrorToPort_Type=Integer32
_IssMirrorToPort_Object=MibScalar
issMirrorToPort=_IssMirrorToPort_Object((1,3,6,1,4,1,2076,81,3,2),_IssMirrorToPort_Type())
issMirrorToPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorToPort.setStatus(_A)
_IssMirrorCtrlTable_Object=MibTable
issMirrorCtrlTable=_IssMirrorCtrlTable_Object((1,3,6,1,4,1,2076,81,3,3))
if mibBuilder.loadTexts:issMirrorCtrlTable.setStatus(_A)
_IssMirrorCtrlEntry_Object=MibTableRow
issMirrorCtrlEntry=_IssMirrorCtrlEntry_Object((1,3,6,1,4,1,2076,81,3,3,1))
issMirrorCtrlEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:issMirrorCtrlEntry.setStatus(_A)
class _IssMirrorCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssMirrorCtrlIndex_Type.__name__=_C
_IssMirrorCtrlIndex_Object=MibTableColumn
issMirrorCtrlIndex=_IssMirrorCtrlIndex_Object((1,3,6,1,4,1,2076,81,3,3,1,1),_IssMirrorCtrlIndex_Type())
issMirrorCtrlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:issMirrorCtrlIndex.setStatus(_A)
class _IssMirrorCtrlIngressMirroring_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssMirrorCtrlIngressMirroring_Type.__name__=_C
_IssMirrorCtrlIngressMirroring_Object=MibTableColumn
issMirrorCtrlIngressMirroring=_IssMirrorCtrlIngressMirroring_Object((1,3,6,1,4,1,2076,81,3,3,1,2),_IssMirrorCtrlIngressMirroring_Type())
issMirrorCtrlIngressMirroring.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlIngressMirroring.setStatus(_A)
class _IssMirrorCtrlEgressMirroring_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssMirrorCtrlEgressMirroring_Type.__name__=_C
_IssMirrorCtrlEgressMirroring_Object=MibTableColumn
issMirrorCtrlEgressMirroring=_IssMirrorCtrlEgressMirroring_Object((1,3,6,1,4,1,2076,81,3,3,1,3),_IssMirrorCtrlEgressMirroring_Type())
issMirrorCtrlEgressMirroring.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlEgressMirroring.setStatus(_A)
class _IssMirrorCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_Y,2)))
_IssMirrorCtrlStatus_Type.__name__=_C
_IssMirrorCtrlStatus_Object=MibTableColumn
issMirrorCtrlStatus=_IssMirrorCtrlStatus_Object((1,3,6,1,4,1,2076,81,3,3,1,4),_IssMirrorCtrlStatus_Type())
issMirrorCtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlStatus.setStatus(_A)
_IssMirrorCtrlRemainingSrcRcrds_Type=Integer32
_IssMirrorCtrlRemainingSrcRcrds_Object=MibScalar
issMirrorCtrlRemainingSrcRcrds=_IssMirrorCtrlRemainingSrcRcrds_Object((1,3,6,1,4,1,2076,81,3,4),_IssMirrorCtrlRemainingSrcRcrds_Type())
issMirrorCtrlRemainingSrcRcrds.setMaxAccess(_G)
if mibBuilder.loadTexts:issMirrorCtrlRemainingSrcRcrds.setStatus(_A)
_IssMirrorCtrlRemainingDestRcrds_Type=Integer32
_IssMirrorCtrlRemainingDestRcrds_Object=MibScalar
issMirrorCtrlRemainingDestRcrds=_IssMirrorCtrlRemainingDestRcrds_Object((1,3,6,1,4,1,2076,81,3,5),_IssMirrorCtrlRemainingDestRcrds_Type())
issMirrorCtrlRemainingDestRcrds.setMaxAccess(_G)
if mibBuilder.loadTexts:issMirrorCtrlRemainingDestRcrds.setStatus(_A)
_IssMirrorCtrlExtnTable_Object=MibTable
issMirrorCtrlExtnTable=_IssMirrorCtrlExtnTable_Object((1,3,6,1,4,1,2076,81,3,6))
if mibBuilder.loadTexts:issMirrorCtrlExtnTable.setStatus(_A)
_IssMirrorCtrlExtnEntry_Object=MibTableRow
issMirrorCtrlExtnEntry=_IssMirrorCtrlExtnEntry_Object((1,3,6,1,4,1,2076,81,3,6,1))
issMirrorCtrlExtnEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:issMirrorCtrlExtnEntry.setStatus(_A)
class _IssMirrorCtrlExtnSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_IssMirrorCtrlExtnSessionIndex_Type.__name__=_C
_IssMirrorCtrlExtnSessionIndex_Object=MibTableColumn
issMirrorCtrlExtnSessionIndex=_IssMirrorCtrlExtnSessionIndex_Object((1,3,6,1,4,1,2076,81,3,6,1,1),_IssMirrorCtrlExtnSessionIndex_Type())
issMirrorCtrlExtnSessionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:issMirrorCtrlExtnSessionIndex.setStatus(_A)
class _IssMirrorCtrlExtnMirrType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('portBased',1),('mac-flowBased',2),('vlanBased',3),(_Y,4),('ip-flowBased',5)))
_IssMirrorCtrlExtnMirrType_Type.__name__=_C
_IssMirrorCtrlExtnMirrType_Object=MibTableColumn
issMirrorCtrlExtnMirrType=_IssMirrorCtrlExtnMirrType_Object((1,3,6,1,4,1,2076,81,3,6,1,2),_IssMirrorCtrlExtnMirrType_Type())
issMirrorCtrlExtnMirrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnMirrType.setStatus(_A)
class _IssMirrorCtrlExtnRSpanStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sourceRSpanVlan',1),('destinationRSpanVlan',2),(_J,3)))
_IssMirrorCtrlExtnRSpanStatus_Type.__name__=_C
_IssMirrorCtrlExtnRSpanStatus_Object=MibTableColumn
issMirrorCtrlExtnRSpanStatus=_IssMirrorCtrlExtnRSpanStatus_Object((1,3,6,1,4,1,2076,81,3,6,1,3),_IssMirrorCtrlExtnRSpanStatus_Type())
issMirrorCtrlExtnRSpanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnRSpanStatus.setStatus(_A)
class _IssMirrorCtrlExtnRSpanVlanId_Type(Integer32):defaultValue=0
_IssMirrorCtrlExtnRSpanVlanId_Type.__name__=_C
_IssMirrorCtrlExtnRSpanVlanId_Object=MibTableColumn
issMirrorCtrlExtnRSpanVlanId=_IssMirrorCtrlExtnRSpanVlanId_Object((1,3,6,1,4,1,2076,81,3,6,1,4),_IssMirrorCtrlExtnRSpanVlanId_Type())
issMirrorCtrlExtnRSpanVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnRSpanVlanId.setStatus(_A)
class _IssMirrorCtrlExtnRSpanContext_Type(Integer32):defaultValue=0
_IssMirrorCtrlExtnRSpanContext_Type.__name__=_C
_IssMirrorCtrlExtnRSpanContext_Object=MibTableColumn
issMirrorCtrlExtnRSpanContext=_IssMirrorCtrlExtnRSpanContext_Object((1,3,6,1,4,1,2076,81,3,6,1,5),_IssMirrorCtrlExtnRSpanContext_Type())
issMirrorCtrlExtnRSpanContext.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnRSpanContext.setStatus(_A)
_IssMirrorCtrlExtnStatus_Type=RowStatus
_IssMirrorCtrlExtnStatus_Object=MibTableColumn
issMirrorCtrlExtnStatus=_IssMirrorCtrlExtnStatus_Object((1,3,6,1,4,1,2076,81,3,6,1,6),_IssMirrorCtrlExtnStatus_Type())
issMirrorCtrlExtnStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:issMirrorCtrlExtnStatus.setStatus(_A)
_IssMirrorCtrlExtnSrcTable_Object=MibTable
issMirrorCtrlExtnSrcTable=_IssMirrorCtrlExtnSrcTable_Object((1,3,6,1,4,1,2076,81,3,7))
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcTable.setStatus(_A)
_IssMirrorCtrlExtnSrcEntry_Object=MibTableRow
issMirrorCtrlExtnSrcEntry=_IssMirrorCtrlExtnSrcEntry_Object((1,3,6,1,4,1,2076,81,3,7,1))
issMirrorCtrlExtnSrcEntry.setIndexNames((0,_E,_S),(0,_E,_r))
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcEntry.setStatus(_A)
class _IssMirrorCtrlExtnSrcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssMirrorCtrlExtnSrcId_Type.__name__=_C
_IssMirrorCtrlExtnSrcId_Object=MibTableColumn
issMirrorCtrlExtnSrcId=_IssMirrorCtrlExtnSrcId_Object((1,3,6,1,4,1,2076,81,3,7,1,1),_IssMirrorCtrlExtnSrcId_Type())
issMirrorCtrlExtnSrcId.setMaxAccess(_H)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcId.setStatus(_A)
class _IssMirrorCtrlExtnSrcCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IssMirrorCtrlExtnSrcCfg_Type.__name__=_C
_IssMirrorCtrlExtnSrcCfg_Object=MibTableColumn
issMirrorCtrlExtnSrcCfg=_IssMirrorCtrlExtnSrcCfg_Object((1,3,6,1,4,1,2076,81,3,7,1,2),_IssMirrorCtrlExtnSrcCfg_Type())
issMirrorCtrlExtnSrcCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcCfg.setStatus(_A)
class _IssMirrorCtrlExtnSrcMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_N,4)))
_IssMirrorCtrlExtnSrcMode_Type.__name__=_C
_IssMirrorCtrlExtnSrcMode_Object=MibTableColumn
issMirrorCtrlExtnSrcMode=_IssMirrorCtrlExtnSrcMode_Object((1,3,6,1,4,1,2076,81,3,7,1,3),_IssMirrorCtrlExtnSrcMode_Type())
issMirrorCtrlExtnSrcMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcMode.setStatus(_A)
_IssMirrorCtrlExtnSrcVlanTable_Object=MibTable
issMirrorCtrlExtnSrcVlanTable=_IssMirrorCtrlExtnSrcVlanTable_Object((1,3,6,1,4,1,2076,81,3,8))
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcVlanTable.setStatus(_A)
_IssMirrorCtrlExtnSrcVlanEntry_Object=MibTableRow
issMirrorCtrlExtnSrcVlanEntry=_IssMirrorCtrlExtnSrcVlanEntry_Object((1,3,6,1,4,1,2076,81,3,8,1))
issMirrorCtrlExtnSrcVlanEntry.setIndexNames((0,_E,_S),(0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcVlanEntry.setStatus(_A)
class _IssMirrorCtrlExtnSrcVlanContext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_IssMirrorCtrlExtnSrcVlanContext_Type.__name__=_C
_IssMirrorCtrlExtnSrcVlanContext_Object=MibTableColumn
issMirrorCtrlExtnSrcVlanContext=_IssMirrorCtrlExtnSrcVlanContext_Object((1,3,6,1,4,1,2076,81,3,8,1,1),_IssMirrorCtrlExtnSrcVlanContext_Type())
issMirrorCtrlExtnSrcVlanContext.setMaxAccess(_H)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcVlanContext.setStatus(_A)
class _IssMirrorCtrlExtnSrcVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_IssMirrorCtrlExtnSrcVlanId_Type.__name__=_C
_IssMirrorCtrlExtnSrcVlanId_Object=MibTableColumn
issMirrorCtrlExtnSrcVlanId=_IssMirrorCtrlExtnSrcVlanId_Object((1,3,6,1,4,1,2076,81,3,8,1,2),_IssMirrorCtrlExtnSrcVlanId_Type())
issMirrorCtrlExtnSrcVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcVlanId.setStatus(_A)
class _IssMirrorCtrlExtnSrcVlanCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IssMirrorCtrlExtnSrcVlanCfg_Type.__name__=_C
_IssMirrorCtrlExtnSrcVlanCfg_Object=MibTableColumn
issMirrorCtrlExtnSrcVlanCfg=_IssMirrorCtrlExtnSrcVlanCfg_Object((1,3,6,1,4,1,2076,81,3,8,1,3),_IssMirrorCtrlExtnSrcVlanCfg_Type())
issMirrorCtrlExtnSrcVlanCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcVlanCfg.setStatus(_A)
class _IssMirrorCtrlExtnSrcVlanMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3)))
_IssMirrorCtrlExtnSrcVlanMode_Type.__name__=_C
_IssMirrorCtrlExtnSrcVlanMode_Object=MibTableColumn
issMirrorCtrlExtnSrcVlanMode=_IssMirrorCtrlExtnSrcVlanMode_Object((1,3,6,1,4,1,2076,81,3,8,1,4),_IssMirrorCtrlExtnSrcVlanMode_Type())
issMirrorCtrlExtnSrcVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnSrcVlanMode.setStatus(_A)
_IssMirrorCtrlExtnDestinationTable_Object=MibTable
issMirrorCtrlExtnDestinationTable=_IssMirrorCtrlExtnDestinationTable_Object((1,3,6,1,4,1,2076,81,3,9))
if mibBuilder.loadTexts:issMirrorCtrlExtnDestinationTable.setStatus(_A)
_IssMirrorCtrlExtnDestinationEntry_Object=MibTableRow
issMirrorCtrlExtnDestinationEntry=_IssMirrorCtrlExtnDestinationEntry_Object((1,3,6,1,4,1,2076,81,3,9,1))
issMirrorCtrlExtnDestinationEntry.setIndexNames((0,_E,_S),(0,_E,_u))
if mibBuilder.loadTexts:issMirrorCtrlExtnDestinationEntry.setStatus(_A)
class _IssMirrorCtrlExtnDestination_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssMirrorCtrlExtnDestination_Type.__name__=_C
_IssMirrorCtrlExtnDestination_Object=MibTableColumn
issMirrorCtrlExtnDestination=_IssMirrorCtrlExtnDestination_Object((1,3,6,1,4,1,2076,81,3,9,1,1),_IssMirrorCtrlExtnDestination_Type())
issMirrorCtrlExtnDestination.setMaxAccess(_H)
if mibBuilder.loadTexts:issMirrorCtrlExtnDestination.setStatus(_A)
class _IssMirrorCtrlExtnDestCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_IssMirrorCtrlExtnDestCfg_Type.__name__=_C
_IssMirrorCtrlExtnDestCfg_Object=MibTableColumn
issMirrorCtrlExtnDestCfg=_IssMirrorCtrlExtnDestCfg_Object((1,3,6,1,4,1,2076,81,3,9,1,2),_IssMirrorCtrlExtnDestCfg_Type())
issMirrorCtrlExtnDestCfg.setMaxAccess(_B)
if mibBuilder.loadTexts:issMirrorCtrlExtnDestCfg.setStatus(_A)
class _IssCpuMirrorType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_N,4)))
_IssCpuMirrorType_Type.__name__=_C
_IssCpuMirrorType_Object=MibScalar
issCpuMirrorType=_IssCpuMirrorType_Object((1,3,6,1,4,1,2076,81,3,10),_IssCpuMirrorType_Type())
issCpuMirrorType.setMaxAccess(_B)
if mibBuilder.loadTexts:issCpuMirrorType.setStatus(_A)
class _IssCpuMirrorToPort_Type(Integer32):defaultValue=0
_IssCpuMirrorToPort_Type.__name__=_C
_IssCpuMirrorToPort_Object=MibScalar
issCpuMirrorToPort=_IssCpuMirrorToPort_Object((1,3,6,1,4,1,2076,81,3,11),_IssCpuMirrorToPort_Type())
issCpuMirrorToPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issCpuMirrorToPort.setStatus(_A)
_IssRateControl_ObjectIdentity=ObjectIdentity
issRateControl=_IssRateControl_ObjectIdentity((1,3,6,1,4,1,2076,81,4))
_IssRateCtrlTable_Object=MibTable
issRateCtrlTable=_IssRateCtrlTable_Object((1,3,6,1,4,1,2076,81,4,1))
if mibBuilder.loadTexts:issRateCtrlTable.setStatus(_D)
_IssRateCtrlEntry_Object=MibTableRow
issRateCtrlEntry=_IssRateCtrlEntry_Object((1,3,6,1,4,1,2076,81,4,1,1))
issRateCtrlEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:issRateCtrlEntry.setStatus(_D)
class _IssRateCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssRateCtrlIndex_Type.__name__=_C
_IssRateCtrlIndex_Object=MibTableColumn
issRateCtrlIndex=_IssRateCtrlIndex_Object((1,3,6,1,4,1,2076,81,4,1,1,1),_IssRateCtrlIndex_Type())
issRateCtrlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:issRateCtrlIndex.setStatus(_D)
class _IssRateCtrlDLFLimitValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IssRateCtrlDLFLimitValue_Type.__name__=_C
_IssRateCtrlDLFLimitValue_Object=MibTableColumn
issRateCtrlDLFLimitValue=_IssRateCtrlDLFLimitValue_Object((1,3,6,1,4,1,2076,81,4,1,1,2),_IssRateCtrlDLFLimitValue_Type())
issRateCtrlDLFLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:issRateCtrlDLFLimitValue.setStatus(_D)
class _IssRateCtrlBCASTLimitValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IssRateCtrlBCASTLimitValue_Type.__name__=_C
_IssRateCtrlBCASTLimitValue_Object=MibTableColumn
issRateCtrlBCASTLimitValue=_IssRateCtrlBCASTLimitValue_Object((1,3,6,1,4,1,2076,81,4,1,1,3),_IssRateCtrlBCASTLimitValue_Type())
issRateCtrlBCASTLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:issRateCtrlBCASTLimitValue.setStatus(_D)
class _IssRateCtrlMCASTLimitValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IssRateCtrlMCASTLimitValue_Type.__name__=_C
_IssRateCtrlMCASTLimitValue_Object=MibTableColumn
issRateCtrlMCASTLimitValue=_IssRateCtrlMCASTLimitValue_Object((1,3,6,1,4,1,2076,81,4,1,1,4),_IssRateCtrlMCASTLimitValue_Type())
issRateCtrlMCASTLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:issRateCtrlMCASTLimitValue.setStatus(_D)
class _IssRateCtrlPortRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80000000))
_IssRateCtrlPortRateLimit_Type.__name__=_C
_IssRateCtrlPortRateLimit_Object=MibTableColumn
issRateCtrlPortRateLimit=_IssRateCtrlPortRateLimit_Object((1,3,6,1,4,1,2076,81,4,1,1,5),_IssRateCtrlPortRateLimit_Type())
issRateCtrlPortRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:issRateCtrlPortRateLimit.setStatus(_D)
class _IssRateCtrlPortBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80000000))
_IssRateCtrlPortBurstSize_Type.__name__=_C
_IssRateCtrlPortBurstSize_Object=MibTableColumn
issRateCtrlPortBurstSize=_IssRateCtrlPortBurstSize_Object((1,3,6,1,4,1,2076,81,4,1,1,6),_IssRateCtrlPortBurstSize_Type())
issRateCtrlPortBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:issRateCtrlPortBurstSize.setStatus(_D)
_IssL2Filter_ObjectIdentity=ObjectIdentity
issL2Filter=_IssL2Filter_ObjectIdentity((1,3,6,1,4,1,2076,81,5))
_IssL2FilterTable_Object=MibTable
issL2FilterTable=_IssL2FilterTable_Object((1,3,6,1,4,1,2076,81,5,1))
if mibBuilder.loadTexts:issL2FilterTable.setStatus(_D)
_IssL2FilterEntry_Object=MibTableRow
issL2FilterEntry=_IssL2FilterEntry_Object((1,3,6,1,4,1,2076,81,5,1,1))
issL2FilterEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:issL2FilterEntry.setStatus(_D)
class _IssL2FilterNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssL2FilterNo_Type.__name__=_C
_IssL2FilterNo_Object=MibTableColumn
issL2FilterNo=_IssL2FilterNo_Object((1,3,6,1,4,1,2076,81,5,1,1,1),_IssL2FilterNo_Type())
issL2FilterNo.setMaxAccess(_H)
if mibBuilder.loadTexts:issL2FilterNo.setStatus(_A)
class _IssL2FilterPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IssL2FilterPriority_Type.__name__=_C
_IssL2FilterPriority_Object=MibTableColumn
issL2FilterPriority=_IssL2FilterPriority_Object((1,3,6,1,4,1,2076,81,5,1,1,2),_IssL2FilterPriority_Type())
issL2FilterPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterPriority.setStatus(_A)
class _IssL2FilterEtherType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssL2FilterEtherType_Type.__name__=_C
_IssL2FilterEtherType_Object=MibTableColumn
issL2FilterEtherType=_IssL2FilterEtherType_Object((1,3,6,1,4,1,2076,81,5,1,1,3),_IssL2FilterEtherType_Type())
issL2FilterEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterEtherType.setStatus(_D)
class _IssL2FilterProtocolType_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssL2FilterProtocolType_Type.__name__=_L
_IssL2FilterProtocolType_Object=MibTableColumn
issL2FilterProtocolType=_IssL2FilterProtocolType_Object((1,3,6,1,4,1,2076,81,5,1,1,4),_IssL2FilterProtocolType_Type())
issL2FilterProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterProtocolType.setStatus(_D)
_IssL2FilterDstMacAddr_Type=MacAddress
_IssL2FilterDstMacAddr_Object=MibTableColumn
issL2FilterDstMacAddr=_IssL2FilterDstMacAddr_Object((1,3,6,1,4,1,2076,81,5,1,1,5),_IssL2FilterDstMacAddr_Type())
issL2FilterDstMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterDstMacAddr.setStatus(_D)
_IssL2FilterSrcMacAddr_Type=MacAddress
_IssL2FilterSrcMacAddr_Object=MibTableColumn
issL2FilterSrcMacAddr=_IssL2FilterSrcMacAddr_Object((1,3,6,1,4,1,2076,81,5,1,1,6),_IssL2FilterSrcMacAddr_Type())
issL2FilterSrcMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterSrcMacAddr.setStatus(_D)
class _IssL2FilterVlanId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_IssL2FilterVlanId_Type.__name__=_C
_IssL2FilterVlanId_Object=MibTableColumn
issL2FilterVlanId=_IssL2FilterVlanId_Object((1,3,6,1,4,1,2076,81,5,1,1,7),_IssL2FilterVlanId_Type())
issL2FilterVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterVlanId.setStatus(_D)
_IssL2FilterInPortList_Type=PortList
_IssL2FilterInPortList_Object=MibTableColumn
issL2FilterInPortList=_IssL2FilterInPortList_Object((1,3,6,1,4,1,2076,81,5,1,1,8),_IssL2FilterInPortList_Type())
issL2FilterInPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterInPortList.setStatus(_D)
class _IssL2FilterAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),(_Z,2)))
_IssL2FilterAction_Type.__name__=_C
_IssL2FilterAction_Object=MibTableColumn
issL2FilterAction=_IssL2FilterAction_Object((1,3,6,1,4,1,2076,81,5,1,1,9),_IssL2FilterAction_Type())
issL2FilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterAction.setStatus(_D)
_IssL2FilterMatchCount_Type=Counter32
_IssL2FilterMatchCount_Object=MibTableColumn
issL2FilterMatchCount=_IssL2FilterMatchCount_Object((1,3,6,1,4,1,2076,81,5,1,1,10),_IssL2FilterMatchCount_Type())
issL2FilterMatchCount.setMaxAccess(_G)
if mibBuilder.loadTexts:issL2FilterMatchCount.setStatus(_D)
_IssL2FilterStatus_Type=RowStatus
_IssL2FilterStatus_Object=MibTableColumn
issL2FilterStatus=_IssL2FilterStatus_Object((1,3,6,1,4,1,2076,81,5,1,1,11),_IssL2FilterStatus_Type())
issL2FilterStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:issL2FilterStatus.setStatus(_D)
_IssL2FilterOutPortList_Type=PortList
_IssL2FilterOutPortList_Object=MibTableColumn
issL2FilterOutPortList=_IssL2FilterOutPortList_Object((1,3,6,1,4,1,2076,81,5,1,1,12),_IssL2FilterOutPortList_Type())
issL2FilterOutPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterOutPortList.setStatus(_D)
class _IssL2FilterDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_IssL2FilterDirection_Type.__name__=_C
_IssL2FilterDirection_Object=MibTableColumn
issL2FilterDirection=_IssL2FilterDirection_Object((1,3,6,1,4,1,2076,81,5,1,1,13),_IssL2FilterDirection_Type())
issL2FilterDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:issL2FilterDirection.setStatus(_D)
_IssL3Filter_ObjectIdentity=ObjectIdentity
issL3Filter=_IssL3Filter_ObjectIdentity((1,3,6,1,4,1,2076,81,6))
_IssL3FilterTable_Object=MibTable
issL3FilterTable=_IssL3FilterTable_Object((1,3,6,1,4,1,2076,81,6,1))
if mibBuilder.loadTexts:issL3FilterTable.setStatus(_D)
_IssL3FilterEntry_Object=MibTableRow
issL3FilterEntry=_IssL3FilterEntry_Object((1,3,6,1,4,1,2076,81,6,1,1))
issL3FilterEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:issL3FilterEntry.setStatus(_D)
class _IssL3FilterNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssL3FilterNo_Type.__name__=_C
_IssL3FilterNo_Object=MibTableColumn
issL3FilterNo=_IssL3FilterNo_Object((1,3,6,1,4,1,2076,81,6,1,1,1),_IssL3FilterNo_Type())
issL3FilterNo.setMaxAccess(_H)
if mibBuilder.loadTexts:issL3FilterNo.setStatus(_D)
class _IssL3FilterPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IssL3FilterPriority_Type.__name__=_C
_IssL3FilterPriority_Object=MibTableColumn
issL3FilterPriority=_IssL3FilterPriority_Object((1,3,6,1,4,1,2076,81,6,1,1,2),_IssL3FilterPriority_Type())
issL3FilterPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterPriority.setStatus(_D)
class _IssL3FilterProtocol_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IssL3FilterProtocol_Type.__name__=_C
_IssL3FilterProtocol_Object=MibTableColumn
issL3FilterProtocol=_IssL3FilterProtocol_Object((1,3,6,1,4,1,2076,81,6,1,1,3),_IssL3FilterProtocol_Type())
issL3FilterProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterProtocol.setStatus(_D)
class _IssL3FilterMessageType_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssL3FilterMessageType_Type.__name__=_C
_IssL3FilterMessageType_Object=MibTableColumn
issL3FilterMessageType=_IssL3FilterMessageType_Object((1,3,6,1,4,1,2076,81,6,1,1,4),_IssL3FilterMessageType_Type())
issL3FilterMessageType.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterMessageType.setStatus(_D)
class _IssL3FilterMessageCode_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssL3FilterMessageCode_Type.__name__=_C
_IssL3FilterMessageCode_Object=MibTableColumn
issL3FilterMessageCode=_IssL3FilterMessageCode_Object((1,3,6,1,4,1,2076,81,6,1,1,5),_IssL3FilterMessageCode_Type())
issL3FilterMessageCode.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterMessageCode.setStatus(_D)
class _IssL3FilterDstIpAddr_Type(IpAddress):defaultHexValue=_y
_IssL3FilterDstIpAddr_Type.__name__=_P
_IssL3FilterDstIpAddr_Object=MibTableColumn
issL3FilterDstIpAddr=_IssL3FilterDstIpAddr_Object((1,3,6,1,4,1,2076,81,6,1,1,6),_IssL3FilterDstIpAddr_Type())
issL3FilterDstIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterDstIpAddr.setStatus(_D)
class _IssL3FilterSrcIpAddr_Type(IpAddress):defaultHexValue=_y
_IssL3FilterSrcIpAddr_Type.__name__=_P
_IssL3FilterSrcIpAddr_Object=MibTableColumn
issL3FilterSrcIpAddr=_IssL3FilterSrcIpAddr_Object((1,3,6,1,4,1,2076,81,6,1,1,7),_IssL3FilterSrcIpAddr_Type())
issL3FilterSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterSrcIpAddr.setStatus(_D)
class _IssL3FilterDstIpAddrMask_Type(IpAddress):defaultHexValue=_z
_IssL3FilterDstIpAddrMask_Type.__name__=_P
_IssL3FilterDstIpAddrMask_Object=MibTableColumn
issL3FilterDstIpAddrMask=_IssL3FilterDstIpAddrMask_Object((1,3,6,1,4,1,2076,81,6,1,1,8),_IssL3FilterDstIpAddrMask_Type())
issL3FilterDstIpAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterDstIpAddrMask.setStatus(_D)
class _IssL3FilterSrcIpAddrMask_Type(IpAddress):defaultHexValue=_z
_IssL3FilterSrcIpAddrMask_Type.__name__=_P
_IssL3FilterSrcIpAddrMask_Object=MibTableColumn
issL3FilterSrcIpAddrMask=_IssL3FilterSrcIpAddrMask_Object((1,3,6,1,4,1,2076,81,6,1,1,9),_IssL3FilterSrcIpAddrMask_Type())
issL3FilterSrcIpAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterSrcIpAddrMask.setStatus(_D)
class _IssL3FilterMinDstProtPort_Type(Unsigned32):defaultValue=0
_IssL3FilterMinDstProtPort_Type.__name__=_L
_IssL3FilterMinDstProtPort_Object=MibTableColumn
issL3FilterMinDstProtPort=_IssL3FilterMinDstProtPort_Object((1,3,6,1,4,1,2076,81,6,1,1,10),_IssL3FilterMinDstProtPort_Type())
issL3FilterMinDstProtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterMinDstProtPort.setStatus(_D)
class _IssL3FilterMaxDstProtPort_Type(Unsigned32):defaultValue=65535
_IssL3FilterMaxDstProtPort_Type.__name__=_L
_IssL3FilterMaxDstProtPort_Object=MibTableColumn
issL3FilterMaxDstProtPort=_IssL3FilterMaxDstProtPort_Object((1,3,6,1,4,1,2076,81,6,1,1,11),_IssL3FilterMaxDstProtPort_Type())
issL3FilterMaxDstProtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterMaxDstProtPort.setStatus(_D)
class _IssL3FilterMinSrcProtPort_Type(Unsigned32):defaultValue=0
_IssL3FilterMinSrcProtPort_Type.__name__=_L
_IssL3FilterMinSrcProtPort_Object=MibTableColumn
issL3FilterMinSrcProtPort=_IssL3FilterMinSrcProtPort_Object((1,3,6,1,4,1,2076,81,6,1,1,12),_IssL3FilterMinSrcProtPort_Type())
issL3FilterMinSrcProtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterMinSrcProtPort.setStatus(_D)
class _IssL3FilterMaxSrcProtPort_Type(Unsigned32):defaultValue=65535
_IssL3FilterMaxSrcProtPort_Type.__name__=_L
_IssL3FilterMaxSrcProtPort_Object=MibTableColumn
issL3FilterMaxSrcProtPort=_IssL3FilterMaxSrcProtPort_Object((1,3,6,1,4,1,2076,81,6,1,1,13),_IssL3FilterMaxSrcProtPort_Type())
issL3FilterMaxSrcProtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterMaxSrcProtPort.setStatus(_D)
_IssL3FilterInPortList_Type=PortList
_IssL3FilterInPortList_Object=MibTableColumn
issL3FilterInPortList=_IssL3FilterInPortList_Object((1,3,6,1,4,1,2076,81,6,1,1,14),_IssL3FilterInPortList_Type())
issL3FilterInPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterInPortList.setStatus(_D)
_IssL3FilterOutPortList_Type=PortList
_IssL3FilterOutPortList_Object=MibTableColumn
issL3FilterOutPortList=_IssL3FilterOutPortList_Object((1,3,6,1,4,1,2076,81,6,1,1,15),_IssL3FilterOutPortList_Type())
issL3FilterOutPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterOutPortList.setStatus(_D)
class _IssL3FilterAckBit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('establish',1),('notEstablish',2),('any',3)))
_IssL3FilterAckBit_Type.__name__=_C
_IssL3FilterAckBit_Object=MibTableColumn
issL3FilterAckBit=_IssL3FilterAckBit_Object((1,3,6,1,4,1,2076,81,6,1,1,16),_IssL3FilterAckBit_Type())
issL3FilterAckBit.setMaxAccess(_M)
if mibBuilder.loadTexts:issL3FilterAckBit.setStatus(_D)
class _IssL3FilterRstBit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('set',1),('notSet',2),('any',3)))
_IssL3FilterRstBit_Type.__name__=_C
_IssL3FilterRstBit_Object=MibTableColumn
issL3FilterRstBit=_IssL3FilterRstBit_Object((1,3,6,1,4,1,2076,81,6,1,1,17),_IssL3FilterRstBit_Type())
issL3FilterRstBit.setMaxAccess(_M)
if mibBuilder.loadTexts:issL3FilterRstBit.setStatus(_D)
class _IssL3FilterTos_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_IssL3FilterTos_Type.__name__=_C
_IssL3FilterTos_Object=MibTableColumn
issL3FilterTos=_IssL3FilterTos_Object((1,3,6,1,4,1,2076,81,6,1,1,18),_IssL3FilterTos_Type())
issL3FilterTos.setMaxAccess(_M)
if mibBuilder.loadTexts:issL3FilterTos.setStatus(_D)
class _IssL3FilterDscp_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,63))
_IssL3FilterDscp_Type.__name__=_C
_IssL3FilterDscp_Object=MibTableColumn
issL3FilterDscp=_IssL3FilterDscp_Object((1,3,6,1,4,1,2076,81,6,1,1,19),_IssL3FilterDscp_Type())
issL3FilterDscp.setMaxAccess(_M)
if mibBuilder.loadTexts:issL3FilterDscp.setStatus(_D)
class _IssL3FilterDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_IssL3FilterDirection_Type.__name__=_C
_IssL3FilterDirection_Object=MibTableColumn
issL3FilterDirection=_IssL3FilterDirection_Object((1,3,6,1,4,1,2076,81,6,1,1,20),_IssL3FilterDirection_Type())
issL3FilterDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterDirection.setStatus(_D)
class _IssL3FilterAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),(_Z,2)))
_IssL3FilterAction_Type.__name__=_C
_IssL3FilterAction_Object=MibTableColumn
issL3FilterAction=_IssL3FilterAction_Object((1,3,6,1,4,1,2076,81,6,1,1,21),_IssL3FilterAction_Type())
issL3FilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:issL3FilterAction.setStatus(_D)
_IssL3FilterMatchCount_Type=Counter32
_IssL3FilterMatchCount_Object=MibTableColumn
issL3FilterMatchCount=_IssL3FilterMatchCount_Object((1,3,6,1,4,1,2076,81,6,1,1,22),_IssL3FilterMatchCount_Type())
issL3FilterMatchCount.setMaxAccess(_G)
if mibBuilder.loadTexts:issL3FilterMatchCount.setStatus(_D)
_IssL3FilterStatus_Type=RowStatus
_IssL3FilterStatus_Object=MibTableColumn
issL3FilterStatus=_IssL3FilterStatus_Object((1,3,6,1,4,1,2076,81,6,1,1,23),_IssL3FilterStatus_Type())
issL3FilterStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:issL3FilterStatus.setStatus(_D)
_IssIpAuthMgr_ObjectIdentity=ObjectIdentity
issIpAuthMgr=_IssIpAuthMgr_ObjectIdentity((1,3,6,1,4,1,2076,81,7))
_IssIpAuthMgrTable_Object=MibTable
issIpAuthMgrTable=_IssIpAuthMgrTable_Object((1,3,6,1,4,1,2076,81,7,1))
if mibBuilder.loadTexts:issIpAuthMgrTable.setStatus(_A)
_IssIpAuthMgrEntry_Object=MibTableRow
issIpAuthMgrEntry=_IssIpAuthMgrEntry_Object((1,3,6,1,4,1,2076,81,7,1,1))
issIpAuthMgrEntry.setIndexNames((0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:issIpAuthMgrEntry.setStatus(_A)
_IssIpAuthMgrIpAddr_Type=IpAddress
_IssIpAuthMgrIpAddr_Object=MibTableColumn
issIpAuthMgrIpAddr=_IssIpAuthMgrIpAddr_Object((1,3,6,1,4,1,2076,81,7,1,1,1),_IssIpAuthMgrIpAddr_Type())
issIpAuthMgrIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:issIpAuthMgrIpAddr.setStatus(_A)
_IssIpAuthMgrIpMask_Type=IpAddress
_IssIpAuthMgrIpMask_Object=MibTableColumn
issIpAuthMgrIpMask=_IssIpAuthMgrIpMask_Object((1,3,6,1,4,1,2076,81,7,1,1,2),_IssIpAuthMgrIpMask_Type())
issIpAuthMgrIpMask.setMaxAccess(_H)
if mibBuilder.loadTexts:issIpAuthMgrIpMask.setStatus(_A)
_IssIpAuthMgrPortList_Type=PortList
_IssIpAuthMgrPortList_Object=MibTableColumn
issIpAuthMgrPortList=_IssIpAuthMgrPortList_Object((1,3,6,1,4,1,2076,81,7,1,1,3),_IssIpAuthMgrPortList_Type())
issIpAuthMgrPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:issIpAuthMgrPortList.setStatus(_A)
_IssIpAuthMgrVlanList_Type=OctetString
_IssIpAuthMgrVlanList_Object=MibTableColumn
issIpAuthMgrVlanList=_IssIpAuthMgrVlanList_Object((1,3,6,1,4,1,2076,81,7,1,1,4),_IssIpAuthMgrVlanList_Type())
issIpAuthMgrVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:issIpAuthMgrVlanList.setStatus(_A)
class _IssIpAuthMgrOOBPort_Type(TruthValue):defaultValue=2
_IssIpAuthMgrOOBPort_Type.__name__=_I
_IssIpAuthMgrOOBPort_Object=MibTableColumn
issIpAuthMgrOOBPort=_IssIpAuthMgrOOBPort_Object((1,3,6,1,4,1,2076,81,7,1,1,5),_IssIpAuthMgrOOBPort_Type())
issIpAuthMgrOOBPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issIpAuthMgrOOBPort.setStatus(_A)
class _IssIpAuthMgrAllowedServices_Type(Integer32):defaultValue=31
_IssIpAuthMgrAllowedServices_Type.__name__=_C
_IssIpAuthMgrAllowedServices_Object=MibTableColumn
issIpAuthMgrAllowedServices=_IssIpAuthMgrAllowedServices_Object((1,3,6,1,4,1,2076,81,7,1,1,6),_IssIpAuthMgrAllowedServices_Type())
issIpAuthMgrAllowedServices.setMaxAccess(_B)
if mibBuilder.loadTexts:issIpAuthMgrAllowedServices.setStatus(_A)
_IssIpAuthMgrRowStatus_Type=RowStatus
_IssIpAuthMgrRowStatus_Object=MibTableColumn
issIpAuthMgrRowStatus=_IssIpAuthMgrRowStatus_Object((1,3,6,1,4,1,2076,81,7,1,1,7),_IssIpAuthMgrRowStatus_Type())
issIpAuthMgrRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:issIpAuthMgrRowStatus.setStatus(_A)
_IssExt_ObjectIdentity=ObjectIdentity
issExt=_IssExt_ObjectIdentity((1,3,6,1,4,1,2076,81,8))
_IssL4Switching_ObjectIdentity=ObjectIdentity
issL4Switching=_IssL4Switching_ObjectIdentity((1,3,6,1,4,1,2076,81,9))
_IssL4SwitchingFilterTable_Object=MibTable
issL4SwitchingFilterTable=_IssL4SwitchingFilterTable_Object((1,3,6,1,4,1,2076,81,9,1))
if mibBuilder.loadTexts:issL4SwitchingFilterTable.setStatus(_A)
_IssL4SwitchingFilterEntry_Object=MibTableRow
issL4SwitchingFilterEntry=_IssL4SwitchingFilterEntry_Object((1,3,6,1,4,1,2076,81,9,1,1))
issL4SwitchingFilterEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:issL4SwitchingFilterEntry.setStatus(_A)
class _IssL4SwitchingFilterNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssL4SwitchingFilterNo_Type.__name__=_C
_IssL4SwitchingFilterNo_Object=MibTableColumn
issL4SwitchingFilterNo=_IssL4SwitchingFilterNo_Object((1,3,6,1,4,1,2076,81,9,1,1,1),_IssL4SwitchingFilterNo_Type())
issL4SwitchingFilterNo.setMaxAccess(_H)
if mibBuilder.loadTexts:issL4SwitchingFilterNo.setStatus(_A)
class _IssL4SwitchingProtocol_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IssL4SwitchingProtocol_Type.__name__=_C
_IssL4SwitchingProtocol_Object=MibTableColumn
issL4SwitchingProtocol=_IssL4SwitchingProtocol_Object((1,3,6,1,4,1,2076,81,9,1,1,2),_IssL4SwitchingProtocol_Type())
issL4SwitchingProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:issL4SwitchingProtocol.setStatus(_A)
class _IssL4SwitchingPortNo_Type(Unsigned32):defaultValue=0
_IssL4SwitchingPortNo_Type.__name__=_L
_IssL4SwitchingPortNo_Object=MibTableColumn
issL4SwitchingPortNo=_IssL4SwitchingPortNo_Object((1,3,6,1,4,1,2076,81,9,1,1,3),_IssL4SwitchingPortNo_Type())
issL4SwitchingPortNo.setMaxAccess(_B)
if mibBuilder.loadTexts:issL4SwitchingPortNo.setStatus(_A)
class _IssL4SwitchingCopyToPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IssL4SwitchingCopyToPort_Type.__name__=_C
_IssL4SwitchingCopyToPort_Object=MibTableColumn
issL4SwitchingCopyToPort=_IssL4SwitchingCopyToPort_Object((1,3,6,1,4,1,2076,81,9,1,1,4),_IssL4SwitchingCopyToPort_Type())
issL4SwitchingCopyToPort.setMaxAccess(_B)
if mibBuilder.loadTexts:issL4SwitchingCopyToPort.setStatus(_A)
_IssL4SwitchingFilterStatus_Type=RowStatus
_IssL4SwitchingFilterStatus_Object=MibTableColumn
issL4SwitchingFilterStatus=_IssL4SwitchingFilterStatus_Object((1,3,6,1,4,1,2076,81,9,1,1,5),_IssL4SwitchingFilterStatus_Type())
issL4SwitchingFilterStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:issL4SwitchingFilterStatus.setStatus(_A)
_IssSystemTrap_ObjectIdentity=ObjectIdentity
issSystemTrap=_IssSystemTrap_ObjectIdentity((1,3,6,1,4,1,2076,81,10))
_IssMsrFailedOid_Type=ObjectIdentifier
_IssMsrFailedOid_Object=MibScalar
issMsrFailedOid=_IssMsrFailedOid_Object((1,3,6,1,4,1,2076,81,10,1),_IssMsrFailedOid_Type())
issMsrFailedOid.setMaxAccess(_O)
if mibBuilder.loadTexts:issMsrFailedOid.setStatus(_A)
_IssMsrFailedValue_Type=DisplayString
_IssMsrFailedValue_Object=MibScalar
issMsrFailedValue=_IssMsrFailedValue_Object((1,3,6,1,4,1,2076,81,10,2),_IssMsrFailedValue_Type())
issMsrFailedValue.setMaxAccess(_O)
if mibBuilder.loadTexts:issMsrFailedValue.setStatus(_A)
_IssAuditTrap_ObjectIdentity=ObjectIdentity
issAuditTrap=_IssAuditTrap_ObjectIdentity((1,3,6,1,4,1,2076,81,11))
class _IssAuditTrapEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A3,1),(_A4,2),(_A5,3),(_A6,4)))
_IssAuditTrapEvent_Type.__name__=_C
_IssAuditTrapEvent_Object=MibScalar
issAuditTrapEvent=_IssAuditTrapEvent_Object((1,3,6,1,4,1,2076,81,11,1),_IssAuditTrapEvent_Type())
issAuditTrapEvent.setMaxAccess(_O)
if mibBuilder.loadTexts:issAuditTrapEvent.setStatus(_A)
class _IssAuditTrapEventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_IssAuditTrapEventTime_Type.__name__=_F
_IssAuditTrapEventTime_Object=MibScalar
issAuditTrapEventTime=_IssAuditTrapEventTime_Object((1,3,6,1,4,1,2076,81,11,2),_IssAuditTrapEventTime_Type())
issAuditTrapEventTime.setMaxAccess(_O)
if mibBuilder.loadTexts:issAuditTrapEventTime.setStatus(_A)
class _IssAuditTrapFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssAuditTrapFileName_Type.__name__=_F
_IssAuditTrapFileName_Object=MibScalar
issAuditTrapFileName=_IssAuditTrapFileName_Object((1,3,6,1,4,1,2076,81,11,3),_IssAuditTrapFileName_Type())
issAuditTrapFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:issAuditTrapFileName.setStatus(_A)
_IssModule_ObjectIdentity=ObjectIdentity
issModule=_IssModule_ObjectIdentity((1,3,6,1,4,1,2076,81,12))
_IssModuleTable_Object=MibTable
issModuleTable=_IssModuleTable_Object((1,3,6,1,4,1,2076,81,12,1))
if mibBuilder.loadTexts:issModuleTable.setStatus(_A)
_IssModuleEntry_Object=MibTableRow
issModuleEntry=_IssModuleEntry_Object((1,3,6,1,4,1,2076,81,12,1,1))
issModuleEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:issModuleEntry.setStatus(_A)
class _IssModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IssModuleId_Type.__name__=_C
_IssModuleId_Object=MibTableColumn
issModuleId=_IssModuleId_Object((1,3,6,1,4,1,2076,81,12,1,1,1),_IssModuleId_Type())
issModuleId.setMaxAccess(_H)
if mibBuilder.loadTexts:issModuleId.setStatus(_A)
class _IssModuleSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('idle',0),('shutdown',1),('start',2)))
_IssModuleSystemControl_Type.__name__=_C
_IssModuleSystemControl_Object=MibTableColumn
issModuleSystemControl=_IssModuleSystemControl_Object((1,3,6,1,4,1,2076,81,12,1,1,2),_IssModuleSystemControl_Type())
issModuleSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:issModuleSystemControl.setStatus(_A)
_IssSwitchFan_ObjectIdentity=ObjectIdentity
issSwitchFan=_IssSwitchFan_ObjectIdentity((1,3,6,1,4,1,2076,81,13))
_IssSwitchFanTable_Object=MibTable
issSwitchFanTable=_IssSwitchFanTable_Object((1,3,6,1,4,1,2076,81,13,1))
if mibBuilder.loadTexts:issSwitchFanTable.setStatus(_A)
_IssSwitchFanEntry_Object=MibTableRow
issSwitchFanEntry=_IssSwitchFanEntry_Object((1,3,6,1,4,1,2076,81,13,1,1))
issSwitchFanEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:issSwitchFanEntry.setStatus(_A)
class _IssSwitchFanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_IssSwitchFanIndex_Type.__name__=_C
_IssSwitchFanIndex_Object=MibTableColumn
issSwitchFanIndex=_IssSwitchFanIndex_Object((1,3,6,1,4,1,2076,81,13,1,1,1),_IssSwitchFanIndex_Type())
issSwitchFanIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:issSwitchFanIndex.setStatus(_A)
class _IssSwitchFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('faulty',2),('critical',3),('not-present',4)))
_IssSwitchFanStatus_Type.__name__=_C
_IssSwitchFanStatus_Object=MibTableColumn
issSwitchFanStatus=_IssSwitchFanStatus_Object((1,3,6,1,4,1,2076,81,13,1,1,2),_IssSwitchFanStatus_Type())
issSwitchFanStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issSwitchFanStatus.setStatus(_A)
_IssAclNp_ObjectIdentity=ObjectIdentity
issAclNp=_IssAclNp_ObjectIdentity((1,3,6,1,4,1,2076,81,14))
class _IssAclProvisionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('immediate',1),('consolidated',2)))
_IssAclProvisionMode_Type.__name__=_C
_IssAclProvisionMode_Object=MibScalar
issAclProvisionMode=_IssAclProvisionMode_Object((1,3,6,1,4,1,2076,81,14,1),_IssAclProvisionMode_Type())
issAclProvisionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issAclProvisionMode.setStatus(_A)
class _IssAclTriggerCommit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_IssAclTriggerCommit_Type.__name__=_C
_IssAclTriggerCommit_Object=MibScalar
issAclTriggerCommit=_IssAclTriggerCommit_Object((1,3,6,1,4,1,2076,81,14,2),_IssAclTriggerCommit_Type())
issAclTriggerCommit.setMaxAccess(_B)
if mibBuilder.loadTexts:issAclTriggerCommit.setStatus(_A)
_IssAclTrafficControl_ObjectIdentity=ObjectIdentity
issAclTrafficControl=_IssAclTrafficControl_ObjectIdentity((1,3,6,1,4,1,2076,81,15))
class _IssAclTrafficSeperationCtrl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('systemdefault',1),('userconfig',2),('none',3)))
_IssAclTrafficSeperationCtrl_Type.__name__=_C
_IssAclTrafficSeperationCtrl_Object=MibScalar
issAclTrafficSeperationCtrl=_IssAclTrafficSeperationCtrl_Object((1,3,6,1,4,1,2076,81,15,1),_IssAclTrafficSeperationCtrl_Type())
issAclTrafficSeperationCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:issAclTrafficSeperationCtrl.setStatus(_A)
_IssLogTrap_ObjectIdentity=ObjectIdentity
issLogTrap=_IssLogTrap_ObjectIdentity((1,3,6,1,4,1,2076,81,16))
class _IssLogTrapEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A3,1),(_A4,2),(_A5,3),(_A6,4)))
_IssLogTrapEvent_Type.__name__=_C
_IssLogTrapEvent_Object=MibScalar
issLogTrapEvent=_IssLogTrapEvent_Object((1,3,6,1,4,1,2076,81,16,1),_IssLogTrapEvent_Type())
issLogTrapEvent.setMaxAccess(_O)
if mibBuilder.loadTexts:issLogTrapEvent.setStatus(_A)
class _IssLogTrapEventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_IssLogTrapEventTime_Type.__name__=_F
_IssLogTrapEventTime_Object=MibScalar
issLogTrapEventTime=_IssLogTrapEventTime_Object((1,3,6,1,4,1,2076,81,16,2),_IssLogTrapEventTime_Type())
issLogTrapEventTime.setMaxAccess(_O)
if mibBuilder.loadTexts:issLogTrapEventTime.setStatus(_A)
class _IssLogTrapFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssLogTrapFileName_Type.__name__=_F
_IssLogTrapFileName_Object=MibScalar
issLogTrapFileName=_IssLogTrapFileName_Object((1,3,6,1,4,1,2076,81,16,3),_IssLogTrapFileName_Type())
issLogTrapFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:issLogTrapFileName.setStatus(_A)
_IssHealthCheckGroup_ObjectIdentity=ObjectIdentity
issHealthCheckGroup=_IssHealthCheckGroup_ObjectIdentity((1,3,6,1,4,1,2076,81,17))
class _IssHealthChkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('upAndRunning',1),('downNonRecoverableErr',2),('upRecoverableRuntimeErr',3)))
_IssHealthChkStatus_Type.__name__=_C
_IssHealthChkStatus_Object=MibScalar
issHealthChkStatus=_IssHealthChkStatus_Object((1,3,6,1,4,1,2076,81,17,1),_IssHealthChkStatus_Type())
issHealthChkStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issHealthChkStatus.setStatus(_A)
class _IssHealthChkErrorReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonRecovTaskInitializationFailure',1),('nonRecovInsufficientStartupMemory',2),('recovCruBuffExhausted',3),('recovConfigRestoreFailed',4),('recovProtocolMemPoolExhausted',5)))
_IssHealthChkErrorReason_Type.__name__=_C
_IssHealthChkErrorReason_Object=MibScalar
issHealthChkErrorReason=_IssHealthChkErrorReason_Object((1,3,6,1,4,1,2076,81,17,2),_IssHealthChkErrorReason_Type())
issHealthChkErrorReason.setMaxAccess(_G)
if mibBuilder.loadTexts:issHealthChkErrorReason.setStatus(_A)
_IssHealthChkMemAllocErrPoolId_Type=Integer32
_IssHealthChkMemAllocErrPoolId_Object=MibScalar
issHealthChkMemAllocErrPoolId=_IssHealthChkMemAllocErrPoolId_Object((1,3,6,1,4,1,2076,81,17,3),_IssHealthChkMemAllocErrPoolId_Type())
issHealthChkMemAllocErrPoolId.setMaxAccess(_G)
if mibBuilder.loadTexts:issHealthChkMemAllocErrPoolId.setStatus(_A)
class _IssHealthChkConfigRestoreStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('configRestoreSuccess',1),('configRestoreFailed',2),('configRestoreInProgress',3),('configRestoreDefault',4)))
_IssHealthChkConfigRestoreStatus_Type.__name__=_C
_IssHealthChkConfigRestoreStatus_Object=MibScalar
issHealthChkConfigRestoreStatus=_IssHealthChkConfigRestoreStatus_Object((1,3,6,1,4,1,2076,81,17,4),_IssHealthChkConfigRestoreStatus_Type())
issHealthChkConfigRestoreStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issHealthChkConfigRestoreStatus.setStatus(_A)
class _IssHealthChkClearCtr_Type(Bits):namedValues=NamedValues(*(('bgp',1),('ospf',2),('rip',3),('rip6',4),('ospf3',5),('ipv4',6),('ipv6',7)))
_IssHealthChkClearCtr_Type.__name__='Bits'
_IssHealthChkClearCtr_Object=MibScalar
issHealthChkClearCtr=_IssHealthChkClearCtr_Object((1,3,6,1,4,1,2076,81,17,5),_IssHealthChkClearCtr_Type())
issHealthChkClearCtr.setMaxAccess(_B)
if mibBuilder.loadTexts:issHealthChkClearCtr.setStatus(_A)
_IssZtp_ObjectIdentity=ObjectIdentity
issZtp=_IssZtp_ObjectIdentity((1,3,6,1,4,1,2076,81,18))
class _IssZtpConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_IssZtpConfigStatus_Type.__name__=_C
_IssZtpConfigStatus_Object=MibScalar
issZtpConfigStatus=_IssZtpConfigStatus_Object((1,3,6,1,4,1,2076,81,18,1),_IssZtpConfigStatus_Type())
issZtpConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:issZtpConfigStatus.setStatus(_A)
class _IssZtpCurrentStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('shutdown',1),('waiting',2),('download',3),('install',4),('reload',5),('complete',6),('error',7)))
_IssZtpCurrentStatus_Type.__name__=_C
_IssZtpCurrentStatus_Object=MibScalar
issZtpCurrentStatus=_IssZtpCurrentStatus_Object((1,3,6,1,4,1,2076,81,18,2),_IssZtpCurrentStatus_Type())
issZtpCurrentStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issZtpCurrentStatus.setStatus(_A)
_IssRunConfig_ObjectIdentity=ObjectIdentity
issRunConfig=_IssRunConfig_ObjectIdentity((1,3,6,1,4,1,2076,81,19))
class _IssRunConfigFileTransferMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_IssRunConfigFileTransferMode_Type.__name__=_C
_IssRunConfigFileTransferMode_Object=MibScalar
issRunConfigFileTransferMode=_IssRunConfigFileTransferMode_Object((1,3,6,1,4,1,2076,81,19,1),_IssRunConfigFileTransferMode_Type())
issRunConfigFileTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:issRunConfigFileTransferMode.setStatus(_A)
_IssRunConfigIpAddrType_Type=InetAddressType
_IssRunConfigIpAddrType_Object=MibScalar
issRunConfigIpAddrType=_IssRunConfigIpAddrType_Object((1,3,6,1,4,1,2076,81,19,2),_IssRunConfigIpAddrType_Type())
issRunConfigIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:issRunConfigIpAddrType.setStatus(_A)
_IssRunConfigIpAddr_Type=InetAddress
_IssRunConfigIpAddr_Object=MibScalar
issRunConfigIpAddr=_IssRunConfigIpAddr_Object((1,3,6,1,4,1,2076,81,19,3),_IssRunConfigIpAddr_Type())
issRunConfigIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:issRunConfigIpAddr.setStatus(_A)
class _IssRunConfigUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssRunConfigUserName_Type.__name__=_F
_IssRunConfigUserName_Object=MibScalar
issRunConfigUserName=_IssRunConfigUserName_Object((1,3,6,1,4,1,2076,81,19,4),_IssRunConfigUserName_Type())
issRunConfigUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:issRunConfigUserName.setStatus(_A)
class _IssRunConfigPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_IssRunConfigPassword_Type.__name__=_F
_IssRunConfigPassword_Object=MibScalar
issRunConfigPassword=_IssRunConfigPassword_Object((1,3,6,1,4,1,2076,81,19,5),_IssRunConfigPassword_Type())
issRunConfigPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:issRunConfigPassword.setStatus(_A)
class _IssRunConfigFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_IssRunConfigFileName_Type.__name__=_F
_IssRunConfigFileName_Object=MibScalar
issRunConfigFileName=_IssRunConfigFileName_Object((1,3,6,1,4,1,2076,81,19,6),_IssRunConfigFileName_Type())
issRunConfigFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:issRunConfigFileName.setStatus(_A)
class _IssApplyConfigToRunningConfig_Type(TruthValue):defaultValue=2
_IssApplyConfigToRunningConfig_Type.__name__=_I
_IssApplyConfigToRunningConfig_Object=MibScalar
issApplyConfigToRunningConfig=_IssApplyConfigToRunningConfig_Object((1,3,6,1,4,1,2076,81,19,7),_IssApplyConfigToRunningConfig_Type())
issApplyConfigToRunningConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:issApplyConfigToRunningConfig.setStatus(_A)
class _IssConfigToRunningConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Q,4)))
_IssConfigToRunningConfigStatus_Type.__name__=_C
_IssConfigToRunningConfigStatus_Object=MibScalar
issConfigToRunningConfigStatus=_IssConfigToRunningConfigStatus_Object((1,3,6,1,4,1,2076,81,19,8),_IssConfigToRunningConfigStatus_Type())
issConfigToRunningConfigStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:issConfigToRunningConfigStatus.setStatus(_A)
class _IssInitiateRunningConfig_Type(TruthValue):defaultValue=2
_IssInitiateRunningConfig_Type.__name__=_I
_IssInitiateRunningConfig_Object=MibScalar
issInitiateRunningConfig=_IssInitiateRunningConfig_Object((1,3,6,1,4,1,2076,81,19,9),_IssInitiateRunningConfig_Type())
issInitiateRunningConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:issInitiateRunningConfig.setStatus(_A)
class _IssCopyStartupConfig_Type(TruthValue):defaultValue=2
_IssCopyStartupConfig_Type.__name__=_I
_IssCopyStartupConfig_Object=MibScalar
issCopyStartupConfig=_IssCopyStartupConfig_Object((1,3,6,1,4,1,2076,81,19,10),_IssCopyStartupConfig_Type())
issCopyStartupConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:issCopyStartupConfig.setStatus(_A)
class _IssStartupToRunningConfig_Type(TruthValue):defaultValue=2
_IssStartupToRunningConfig_Type.__name__=_I
_IssStartupToRunningConfig_Object=MibScalar
issStartupToRunningConfig=_IssStartupToRunningConfig_Object((1,3,6,1,4,1,2076,81,19,11),_IssStartupToRunningConfig_Type())
issStartupToRunningConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:issStartupToRunningConfig.setStatus(_A)
issTrapConfigRestore=NotificationType((1,3,6,1,4,1,2076,81,0,1))
issTrapConfigRestore.setObjects((_E,_A8))
if mibBuilder.loadTexts:issTrapConfigRestore.setStatus(_A)
issMsrUpdateEventFail=NotificationType((1,3,6,1,4,1,2076,81,0,2))
issMsrUpdateEventFail.setObjects(*((_E,_A9),(_E,_AA)))
if mibBuilder.loadTexts:issMsrUpdateEventFail.setStatus(_A)
issAuditTrapMessage=NotificationType((1,3,6,1,4,1,2076,81,0,3))
issAuditTrapMessage.setObjects(*((_E,_AB),(_E,_AC),(_E,_AD)))
if mibBuilder.loadTexts:issAuditTrapMessage.setStatus(_A)
issTrapTemperature=NotificationType((1,3,6,1,4,1,2076,81,0,4))
issTrapTemperature.setObjects(*((_E,_AE),(_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:issTrapTemperature.setStatus(_A)
issTrapCPUThreshold=NotificationType((1,3,6,1,4,1,2076,81,0,5))
issTrapCPUThreshold.setObjects(*((_E,_AH),(_E,_AI)))
if mibBuilder.loadTexts:issTrapCPUThreshold.setStatus(_A)
issTrapPowerSupply=NotificationType((1,3,6,1,4,1,2076,81,0,6))
issTrapPowerSupply.setObjects(*((_E,_AJ),(_E,_AK),(_E,_AL)))
if mibBuilder.loadTexts:issTrapPowerSupply.setStatus(_A)
issTrapRAMUsage=NotificationType((1,3,6,1,4,1,2076,81,0,7))
issTrapRAMUsage.setObjects(*((_E,_AM),(_E,_AN)))
if mibBuilder.loadTexts:issTrapRAMUsage.setStatus(_A)
issTrapFlashUsage=NotificationType((1,3,6,1,4,1,2076,81,0,8))
issTrapFlashUsage.setObjects(*((_E,_AO),(_E,_AP)))
if mibBuilder.loadTexts:issTrapFlashUsage.setStatus(_A)
issTrapFanStatus=NotificationType((1,3,6,1,4,1,2076,81,0,9))
issTrapFanStatus.setObjects(*((_E,_f),(_E,_AQ)))
if mibBuilder.loadTexts:issTrapFanStatus.setStatus(_A)
issLogTrapMessage=NotificationType((1,3,6,1,4,1,2076,81,0,10))
issLogTrapMessage.setObjects(*((_E,_AR),(_E,_AS),(_E,_AT)))
if mibBuilder.loadTexts:issLogTrapMessage.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortList':PortList,'iss':iss,'issNotifications':issNotifications,'issTrapConfigRestore':issTrapConfigRestore,'issMsrUpdateEventFail':issMsrUpdateEventFail,'issAuditTrapMessage':issAuditTrapMessage,'issTrapTemperature':issTrapTemperature,'issTrapCPUThreshold':issTrapCPUThreshold,'issTrapPowerSupply':issTrapPowerSupply,'issTrapRAMUsage':issTrapRAMUsage,'issTrapFlashUsage':issTrapFlashUsage,'issTrapFanStatus':issTrapFanStatus,'issLogTrapMessage':issLogTrapMessage,'issSystem':issSystem,'issSwitchName':issSwitchName,'issHardwareVersion':issHardwareVersion,'issFirmwareVersion':issFirmwareVersion,'issDefaultIpAddrCfgMode':issDefaultIpAddrCfgMode,'issDefaultIpAddr':issDefaultIpAddr,'issDefaultIpSubnetMask':issDefaultIpSubnetMask,'issEffectiveIpAddr':issEffectiveIpAddr,'issDefaultInterface':issDefaultInterface,'issRestart':issRestart,'issConfigSaveOption':issConfigSaveOption,'issConfigSaveIpAddr':issConfigSaveIpAddr,'issConfigSaveFileName':issConfigSaveFileName,'issInitiateConfigSave':issInitiateConfigSave,'issConfigSaveStatus':issConfigSaveStatus,'issConfigRestoreOption':issConfigRestoreOption,'issConfigRestoreIpAddr':issConfigRestoreIpAddr,'issConfigRestoreFileName':issConfigRestoreFileName,'issInitiateConfigRestore':issInitiateConfigRestore,_A8:issConfigRestoreStatus,'issDlImageFromIp':issDlImageFromIp,'issDlImageName':issDlImageName,'issInitiateDlImage':issInitiateDlImage,'issLoggingOption':issLoggingOption,'issUploadLogFileToIp':issUploadLogFileToIp,'issLogFileName':issLogFileName,'issInitiateUlLogFile':issInitiateUlLogFile,'issRemoteSaveStatus':issRemoteSaveStatus,'issDownloadStatus':issDownloadStatus,'issSysContact':issSysContact,'issSysLocation':issSysLocation,'issLoginAuthentication':issLoginAuthentication,'issSwitchBaseMacAddress':issSwitchBaseMacAddress,'issOOBInterface':issOOBInterface,'issSwitchDate':issSwitchDate,'issNoCliConsole':issNoCliConsole,'issDefaultIpAddrAllocProtocol':issDefaultIpAddrAllocProtocol,'issHttpPort':issHttpPort,'issHttpStatus':issHttpStatus,'issConfigRestoreFileVersion':issConfigRestoreFileVersion,'issDefaultRmIfName':issDefaultRmIfName,'issDefaultVlanId':issDefaultVlanId,'issNpapiMode':issNpapiMode,'issConfigAutoSaveTrigger':issConfigAutoSaveTrigger,'issConfigIncrSaveFlag':issConfigIncrSaveFlag,'issConfigRollbackFlag':issConfigRollbackFlag,'issConfigSyncUpOperation':issConfigSyncUpOperation,'issFrontPanelPortCount':issFrontPanelPortCount,'issAuditLogStatus':issAuditLogStatus,'issAuditLogFileName':issAuditLogFileName,'issAuditLogFileSize':issAuditLogFileSize,'issAuditLogReset':issAuditLogReset,'issAuditLogRemoteIpAddr':issAuditLogRemoteIpAddr,'issAuditLogInitiateTransfer':issAuditLogInitiateTransfer,'issAuditTransferFileName':issAuditTransferFileName,'issDownLoadTransferMode':issDownLoadTransferMode,'issDownLoadUserName':issDownLoadUserName,'issDownLoadPassword':issDownLoadPassword,'issUploadLogTransferMode':issUploadLogTransferMode,'issUploadLogUserName':issUploadLogUserName,'issUploadLogPasswd':issUploadLogPasswd,'issConfigSaveTransferMode':issConfigSaveTransferMode,'issConfigSaveUserName':issConfigSaveUserName,'issConfigSavePassword':issConfigSavePassword,_AE:issSwitchMinThresholdTemperature,_AF:issSwitchMaxThresholdTemperature,_AG:issSwitchCurrentTemperature,_AH:issSwitchMaxCPUThreshold,_AI:issSwitchCurrentCPUThreshold,_AJ:issSwitchPowerSurge,_AK:issSwitchPowerFailure,_AL:issSwitchCurrentPowerSupply,_AM:issSwitchMaxRAMUsage,_AN:issSwitchCurrentRAMUsage,_AO:issSwitchMaxFlashUsage,_AP:issSwitchCurrentFlashUsage,'issConfigRestoreFileFormatVersion':issConfigRestoreFileFormatVersion,'issDebugOption':issDebugOption,'issConfigDefaultValueSaveOption':issConfigDefaultValueSaveOption,'issConfigSaveIpAddrType':issConfigSaveIpAddrType,'issConfigSaveIpvxAddr':issConfigSaveIpvxAddr,'issConfigRestoreIpAddrType':issConfigRestoreIpAddrType,'issConfigRestoreIpvxAddr':issConfigRestoreIpvxAddr,'issDlImageFromIpAddrType':issDlImageFromIpAddrType,'issDlImageFromIpvx':issDlImageFromIpvx,'issUploadLogFileToIpAddrType':issUploadLogFileToIpAddrType,'issUploadLogFileToIpvx':issUploadLogFileToIpvx,'issAuditLogRemoteIpAddrType':issAuditLogRemoteIpAddrType,'issAuditLogRemoteIpvxAddr':issAuditLogRemoteIpvxAddr,'issSystemTimerSpeed':issSystemTimerSpeed,'issMgmtInterfaceRouting':issMgmtInterfaceRouting,'issMacLearnRateLimit':issMacLearnRateLimit,'issMacLearnRateLimitInterval':issMacLearnRateLimitInterval,'issVrfUnqMacFlag':issVrfUnqMacFlag,'issLoginAttempts':issLoginAttempts,'issLoginLockTime':issLoginLockTime,'issAuditLogSizeThreshold':issAuditLogSizeThreshold,'issTelnetStatus':issTelnetStatus,'issWebSessionTimeOut':issWebSessionTimeOut,'issWebSessionMaxUsers':issWebSessionMaxUsers,'issHeartBeatMode':issHeartBeatMode,'issRmRType':issRmRType,'issRmDType':issRmDType,'issClearConfig':issClearConfig,'issClearConfigFileName':issClearConfigFileName,'issTelnetClientStatus':issTelnetClientStatus,'issSshClientStatus':issSshClientStatus,'issActiveTelnetClientSessions':issActiveTelnetClientSessions,'issActiveSshClientSessions':issActiveSshClientSessions,'issLogFileSize':issLogFileSize,'issLogReset':issLogReset,'issLogSizeThreshold':issLogSizeThreshold,'issAutomaticPortCreate':issAutomaticPortCreate,'issUlRemoteLogFileName':issUlRemoteLogFileName,'issDefaultExecTimeOut':issDefaultExecTimeOut,'issRmStackingInterfaceType':issRmStackingInterfaceType,'issPeerLoggingOption':issPeerLoggingOption,'issStandbyRestart':issStandbyRestart,'issRestoreType':issRestoreType,'issSwitchModeType':issSwitchModeType,'issHardwareSerialNumber':issHardwareSerialNumber,'issDlImageType':issDlImageType,'issConfigControl':issConfigControl,'issConfigCtrlTable':issConfigCtrlTable,'issConfigCtrlEntry':issConfigCtrlEntry,_l:issConfigCtrlIndex,'issConfigCtrlEgressStatus':issConfigCtrlEgressStatus,'issConfigCtrlStatsCollection':issConfigCtrlStatsCollection,'issConfigCtrlStatus':issConfigCtrlStatus,'issPortCtrlTable':issPortCtrlTable,'issPortCtrlEntry':issPortCtrlEntry,_m:issPortCtrlIndex,'issPortCtrlMode':issPortCtrlMode,'issPortCtrlDuplex':issPortCtrlDuplex,'issPortCtrlSpeed':issPortCtrlSpeed,'issPortCtrlFlowControl':issPortCtrlFlowControl,'issPortCtrlRenegotiate':issPortCtrlRenegotiate,'issPortCtrlMaxMacAddr':issPortCtrlMaxMacAddr,'issPortCtrlMaxMacAction':issPortCtrlMaxMacAction,'issPortHOLBlockPrevention':issPortHOLBlockPrevention,'issPortAutoNegAdvtCapBits':issPortAutoNegAdvtCapBits,'issPortCpuControlledLearning':issPortCpuControlledLearning,'issPortMdiOrMdixCap':issPortMdiOrMdixCap,'issPortCtrlFlowControlMaxRate':issPortCtrlFlowControlMaxRate,'issPortCtrlFlowControlMinRate':issPortCtrlFlowControlMinRate,'issPortIsolationTable':issPortIsolationTable,'issPortIsolationEntry':issPortIsolationEntry,_n:issPortIsolationIngressPort,_o:issPortIsolationInVlanId,_p:issPortIsolationEgressPort,'issPortIsolationStorageType':issPortIsolationStorageType,'issPortIsolationRowStatus':issPortIsolationRowStatus,'issMirror':issMirror,'issMirrorStatus':issMirrorStatus,'issMirrorToPort':issMirrorToPort,'issMirrorCtrlTable':issMirrorCtrlTable,'issMirrorCtrlEntry':issMirrorCtrlEntry,_q:issMirrorCtrlIndex,'issMirrorCtrlIngressMirroring':issMirrorCtrlIngressMirroring,'issMirrorCtrlEgressMirroring':issMirrorCtrlEgressMirroring,'issMirrorCtrlStatus':issMirrorCtrlStatus,'issMirrorCtrlRemainingSrcRcrds':issMirrorCtrlRemainingSrcRcrds,'issMirrorCtrlRemainingDestRcrds':issMirrorCtrlRemainingDestRcrds,'issMirrorCtrlExtnTable':issMirrorCtrlExtnTable,'issMirrorCtrlExtnEntry':issMirrorCtrlExtnEntry,_S:issMirrorCtrlExtnSessionIndex,'issMirrorCtrlExtnMirrType':issMirrorCtrlExtnMirrType,'issMirrorCtrlExtnRSpanStatus':issMirrorCtrlExtnRSpanStatus,'issMirrorCtrlExtnRSpanVlanId':issMirrorCtrlExtnRSpanVlanId,'issMirrorCtrlExtnRSpanContext':issMirrorCtrlExtnRSpanContext,'issMirrorCtrlExtnStatus':issMirrorCtrlExtnStatus,'issMirrorCtrlExtnSrcTable':issMirrorCtrlExtnSrcTable,'issMirrorCtrlExtnSrcEntry':issMirrorCtrlExtnSrcEntry,_r:issMirrorCtrlExtnSrcId,'issMirrorCtrlExtnSrcCfg':issMirrorCtrlExtnSrcCfg,'issMirrorCtrlExtnSrcMode':issMirrorCtrlExtnSrcMode,'issMirrorCtrlExtnSrcVlanTable':issMirrorCtrlExtnSrcVlanTable,'issMirrorCtrlExtnSrcVlanEntry':issMirrorCtrlExtnSrcVlanEntry,_s:issMirrorCtrlExtnSrcVlanContext,_t:issMirrorCtrlExtnSrcVlanId,'issMirrorCtrlExtnSrcVlanCfg':issMirrorCtrlExtnSrcVlanCfg,'issMirrorCtrlExtnSrcVlanMode':issMirrorCtrlExtnSrcVlanMode,'issMirrorCtrlExtnDestinationTable':issMirrorCtrlExtnDestinationTable,'issMirrorCtrlExtnDestinationEntry':issMirrorCtrlExtnDestinationEntry,_u:issMirrorCtrlExtnDestination,'issMirrorCtrlExtnDestCfg':issMirrorCtrlExtnDestCfg,'issCpuMirrorType':issCpuMirrorType,'issCpuMirrorToPort':issCpuMirrorToPort,'issRateControl':issRateControl,'issRateCtrlTable':issRateCtrlTable,'issRateCtrlEntry':issRateCtrlEntry,_v:issRateCtrlIndex,'issRateCtrlDLFLimitValue':issRateCtrlDLFLimitValue,'issRateCtrlBCASTLimitValue':issRateCtrlBCASTLimitValue,'issRateCtrlMCASTLimitValue':issRateCtrlMCASTLimitValue,'issRateCtrlPortRateLimit':issRateCtrlPortRateLimit,'issRateCtrlPortBurstSize':issRateCtrlPortBurstSize,'issL2Filter':issL2Filter,'issL2FilterTable':issL2FilterTable,'issL2FilterEntry':issL2FilterEntry,_w:issL2FilterNo,'issL2FilterPriority':issL2FilterPriority,'issL2FilterEtherType':issL2FilterEtherType,'issL2FilterProtocolType':issL2FilterProtocolType,'issL2FilterDstMacAddr':issL2FilterDstMacAddr,'issL2FilterSrcMacAddr':issL2FilterSrcMacAddr,'issL2FilterVlanId':issL2FilterVlanId,'issL2FilterInPortList':issL2FilterInPortList,'issL2FilterAction':issL2FilterAction,'issL2FilterMatchCount':issL2FilterMatchCount,'issL2FilterStatus':issL2FilterStatus,'issL2FilterOutPortList':issL2FilterOutPortList,'issL2FilterDirection':issL2FilterDirection,'issL3Filter':issL3Filter,'issL3FilterTable':issL3FilterTable,'issL3FilterEntry':issL3FilterEntry,_x:issL3FilterNo,'issL3FilterPriority':issL3FilterPriority,'issL3FilterProtocol':issL3FilterProtocol,'issL3FilterMessageType':issL3FilterMessageType,'issL3FilterMessageCode':issL3FilterMessageCode,'issL3FilterDstIpAddr':issL3FilterDstIpAddr,'issL3FilterSrcIpAddr':issL3FilterSrcIpAddr,'issL3FilterDstIpAddrMask':issL3FilterDstIpAddrMask,'issL3FilterSrcIpAddrMask':issL3FilterSrcIpAddrMask,'issL3FilterMinDstProtPort':issL3FilterMinDstProtPort,'issL3FilterMaxDstProtPort':issL3FilterMaxDstProtPort,'issL3FilterMinSrcProtPort':issL3FilterMinSrcProtPort,'issL3FilterMaxSrcProtPort':issL3FilterMaxSrcProtPort,'issL3FilterInPortList':issL3FilterInPortList,'issL3FilterOutPortList':issL3FilterOutPortList,'issL3FilterAckBit':issL3FilterAckBit,'issL3FilterRstBit':issL3FilterRstBit,'issL3FilterTos':issL3FilterTos,'issL3FilterDscp':issL3FilterDscp,'issL3FilterDirection':issL3FilterDirection,'issL3FilterAction':issL3FilterAction,'issL3FilterMatchCount':issL3FilterMatchCount,'issL3FilterStatus':issL3FilterStatus,'issIpAuthMgr':issIpAuthMgr,'issIpAuthMgrTable':issIpAuthMgrTable,'issIpAuthMgrEntry':issIpAuthMgrEntry,_A0:issIpAuthMgrIpAddr,_A1:issIpAuthMgrIpMask,'issIpAuthMgrPortList':issIpAuthMgrPortList,'issIpAuthMgrVlanList':issIpAuthMgrVlanList,'issIpAuthMgrOOBPort':issIpAuthMgrOOBPort,'issIpAuthMgrAllowedServices':issIpAuthMgrAllowedServices,'issIpAuthMgrRowStatus':issIpAuthMgrRowStatus,'issExt':issExt,'issL4Switching':issL4Switching,'issL4SwitchingFilterTable':issL4SwitchingFilterTable,'issL4SwitchingFilterEntry':issL4SwitchingFilterEntry,_A2:issL4SwitchingFilterNo,'issL4SwitchingProtocol':issL4SwitchingProtocol,'issL4SwitchingPortNo':issL4SwitchingPortNo,'issL4SwitchingCopyToPort':issL4SwitchingCopyToPort,'issL4SwitchingFilterStatus':issL4SwitchingFilterStatus,'issSystemTrap':issSystemTrap,_A9:issMsrFailedOid,_AA:issMsrFailedValue,'issAuditTrap':issAuditTrap,_AB:issAuditTrapEvent,_AC:issAuditTrapEventTime,_AD:issAuditTrapFileName,'issModule':issModule,'issModuleTable':issModuleTable,'issModuleEntry':issModuleEntry,_A7:issModuleId,'issModuleSystemControl':issModuleSystemControl,'issSwitchFan':issSwitchFan,'issSwitchFanTable':issSwitchFanTable,'issSwitchFanEntry':issSwitchFanEntry,_f:issSwitchFanIndex,_AQ:issSwitchFanStatus,'issAclNp':issAclNp,'issAclProvisionMode':issAclProvisionMode,'issAclTriggerCommit':issAclTriggerCommit,'issAclTrafficControl':issAclTrafficControl,'issAclTrafficSeperationCtrl':issAclTrafficSeperationCtrl,'issLogTrap':issLogTrap,_AR:issLogTrapEvent,_AS:issLogTrapEventTime,_AT:issLogTrapFileName,'issHealthCheckGroup':issHealthCheckGroup,'issHealthChkStatus':issHealthChkStatus,'issHealthChkErrorReason':issHealthChkErrorReason,'issHealthChkMemAllocErrPoolId':issHealthChkMemAllocErrPoolId,'issHealthChkConfigRestoreStatus':issHealthChkConfigRestoreStatus,'issHealthChkClearCtr':issHealthChkClearCtr,'issZtp':issZtp,'issZtpConfigStatus':issZtpConfigStatus,'issZtpCurrentStatus':issZtpCurrentStatus,'issRunConfig':issRunConfig,'issRunConfigFileTransferMode':issRunConfigFileTransferMode,'issRunConfigIpAddrType':issRunConfigIpAddrType,'issRunConfigIpAddr':issRunConfigIpAddr,'issRunConfigUserName':issRunConfigUserName,'issRunConfigPassword':issRunConfigPassword,'issRunConfigFileName':issRunConfigFileName,'issApplyConfigToRunningConfig':issApplyConfigToRunningConfig,'issConfigToRunningConfigStatus':issConfigToRunningConfigStatus,'issInitiateRunningConfig':issInitiateRunningConfig,'issCopyStartupConfig':issCopyStartupConfig,'issStartupToRunningConfig':issStartupToRunningConfig})