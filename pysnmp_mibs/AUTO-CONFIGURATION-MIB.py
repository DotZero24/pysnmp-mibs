_L='rcAutoConfigResult'
_K='rcAutoConfigCurrentFileType'
_J='success'
_I='Unsigned32'
_H='AUTO-CONFIGURATION-MIB'
_G='none'
_F='read-only'
_E='EnableVar'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_E)
rcAutoConfig=ModuleIdentity((1,3,6,1,4,1,8886,6,1,28))
_RcAutoConfigTftpServerAddress_Type=IpAddress
_RcAutoConfigTftpServerAddress_Object=MibScalar
rcAutoConfigTftpServerAddress=_RcAutoConfigTftpServerAddress_Object((1,3,6,1,4,1,8886,6,1,28,1),_RcAutoConfigTftpServerAddress_Type())
rcAutoConfigTftpServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigTftpServerAddress.setStatus(_A)
class _RcAutoConfigFileName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RcAutoConfigFileName_Type.__name__=_C
_RcAutoConfigFileName_Object=MibScalar
rcAutoConfigFileName=_RcAutoConfigFileName_Object((1,3,6,1,4,1,8886,6,1,28,2),_RcAutoConfigFileName_Type())
rcAutoConfigFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigFileName.setStatus(_A)
class _RcAutoConfigStartupEnable_Type(EnableVar):defaultValue=2
_RcAutoConfigStartupEnable_Type.__name__=_E
_RcAutoConfigStartupEnable_Object=MibScalar
rcAutoConfigStartupEnable=_RcAutoConfigStartupEnable_Object((1,3,6,1,4,1,8886,6,1,28,3),_RcAutoConfigStartupEnable_Type())
rcAutoConfigStartupEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigStartupEnable.setStatus(_A)
class _RcAutoConfigOverwriteEnable_Type(EnableVar):defaultValue=2
_RcAutoConfigOverwriteEnable_Type.__name__=_E
_RcAutoConfigOverwriteEnable_Object=MibScalar
rcAutoConfigOverwriteEnable=_RcAutoConfigOverwriteEnable_Object((1,3,6,1,4,1,8886,6,1,28,4),_RcAutoConfigOverwriteEnable_Type())
rcAutoConfigOverwriteEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigOverwriteEnable.setStatus(_A)
class _RcAutoConfigTrapEnable_Type(EnableVar):defaultValue=2
_RcAutoConfigTrapEnable_Type.__name__=_E
_RcAutoConfigTrapEnable_Object=MibScalar
rcAutoConfigTrapEnable=_RcAutoConfigTrapEnable_Object((1,3,6,1,4,1,8886,6,1,28,5),_RcAutoConfigTrapEnable_Type())
rcAutoConfigTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigTrapEnable.setStatus(_A)
class _RcAutoConfigCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_RcAutoConfigCommand_Type.__name__=_D
_RcAutoConfigCommand_Object=MibScalar
rcAutoConfigCommand=_RcAutoConfigCommand_Object((1,3,6,1,4,1,8886,6,1,28,6),_RcAutoConfigCommand_Type())
rcAutoConfigCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigCommand.setStatus('deprecated')
class _RcAutoConfigOperationStates_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('waiting',1),('getting',2),('loading',3),('writing',4),('done',5)))
_RcAutoConfigOperationStates_Type.__name__=_D
_RcAutoConfigOperationStates_Object=MibScalar
rcAutoConfigOperationStates=_RcAutoConfigOperationStates_Object((1,3,6,1,4,1,8886,6,1,28,7),_RcAutoConfigOperationStates_Type())
rcAutoConfigOperationStates.setMaxAccess(_F)
if mibBuilder.loadTexts:rcAutoConfigOperationStates.setStatus(_A)
class _RcAutoConfigResult_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),('succeeded',2),('ipAddressUnavailable',3),('acquireFailed',4),('getFailed',5),('writeFailed',6),('notEnoughMemory',7),('other',8),('stopped',9)))
_RcAutoConfigResult_Type.__name__=_D
_RcAutoConfigResult_Object=MibScalar
rcAutoConfigResult=_RcAutoConfigResult_Object((1,3,6,1,4,1,8886,6,1,28,8),_RcAutoConfigResult_Type())
rcAutoConfigResult.setMaxAccess(_F)
if mibBuilder.loadTexts:rcAutoConfigResult.setStatus(_A)
_RcAutoConfigTraps_ObjectIdentity=ObjectIdentity
rcAutoConfigTraps=_RcAutoConfigTraps_ObjectIdentity((1,3,6,1,4,1,8886,6,1,28,9))
class _RcAutoConfigFilenameRule_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(80000,89999))
_RcAutoConfigFilenameRule_Type.__name__=_I
_RcAutoConfigFilenameRule_Object=MibScalar
rcAutoConfigFilenameRule=_RcAutoConfigFilenameRule_Object((1,3,6,1,4,1,8886,6,1,28,10),_RcAutoConfigFilenameRule_Type())
rcAutoConfigFilenameRule.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigFilenameRule.setStatus(_A)
class _RcAutoConfigSystemBootVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_RcAutoConfigSystemBootVersion_Type.__name__=_C
_RcAutoConfigSystemBootVersion_Object=MibScalar
rcAutoConfigSystemBootVersion=_RcAutoConfigSystemBootVersion_Object((1,3,6,1,4,1,8886,6,1,28,11),_RcAutoConfigSystemBootVersion_Type())
rcAutoConfigSystemBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigSystemBootVersion.setStatus(_A)
class _RcAutoConfigBootstrapVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_RcAutoConfigBootstrapVersion_Type.__name__=_C
_RcAutoConfigBootstrapVersion_Object=MibScalar
rcAutoConfigBootstrapVersion=_RcAutoConfigBootstrapVersion_Object((1,3,6,1,4,1,8886,6,1,28,12),_RcAutoConfigBootstrapVersion_Type())
rcAutoConfigBootstrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigBootstrapVersion.setStatus(_A)
class _RcAutoConfigStartupConfigVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_RcAutoConfigStartupConfigVersion_Type.__name__=_C
_RcAutoConfigStartupConfigVersion_Object=MibScalar
rcAutoConfigStartupConfigVersion=_RcAutoConfigStartupConfigVersion_Object((1,3,6,1,4,1,8886,6,1,28,13),_RcAutoConfigStartupConfigVersion_Type())
rcAutoConfigStartupConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigStartupConfigVersion.setStatus(_A)
class _RcAutoConfigEnable_Type(EnableVar):defaultValue=1
_RcAutoConfigEnable_Type.__name__=_E
_RcAutoConfigEnable_Object=MibScalar
rcAutoConfigEnable=_RcAutoConfigEnable_Object((1,3,6,1,4,1,8886,6,1,28,14),_RcAutoConfigEnable_Type())
rcAutoConfigEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigEnable.setStatus(_A)
class _RcAutoConfigCurrentFileType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('startup-config',2),('system-boot',3),('bootstrap',4)))
_RcAutoConfigCurrentFileType_Type.__name__=_D
_RcAutoConfigCurrentFileType_Object=MibScalar
rcAutoConfigCurrentFileType=_RcAutoConfigCurrentFileType_Object((1,3,6,1,4,1,8886,6,1,28,15),_RcAutoConfigCurrentFileType_Type())
rcAutoConfigCurrentFileType.setMaxAccess(_F)
if mibBuilder.loadTexts:rcAutoConfigCurrentFileType.setStatus(_A)
class _RcAutoConfigFilenamePrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RcAutoConfigFilenamePrefix_Type.__name__=_C
_RcAutoConfigFilenamePrefix_Object=MibScalar
rcAutoConfigFilenamePrefix=_RcAutoConfigFilenamePrefix_Object((1,3,6,1,4,1,8886,6,1,28,16),_RcAutoConfigFilenamePrefix_Type())
rcAutoConfigFilenamePrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigFilenamePrefix.setStatus(_A)
class _RcAutoConfigFilenamePostfix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RcAutoConfigFilenamePostfix_Type.__name__=_C
_RcAutoConfigFilenamePostfix_Object=MibScalar
rcAutoConfigFilenamePostfix=_RcAutoConfigFilenamePostfix_Object((1,3,6,1,4,1,8886,6,1,28,17),_RcAutoConfigFilenamePostfix_Type())
rcAutoConfigFilenamePostfix.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigFilenamePostfix.setStatus(_A)
class _RcAutoConfigAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('DHCPC',2),('Auto-provision',3)))
_RcAutoConfigAccessType_Type.__name__=_D
_RcAutoConfigAccessType_Object=MibScalar
rcAutoConfigAccessType=_RcAutoConfigAccessType_Object((1,3,6,1,4,1,8886,6,1,28,18),_RcAutoConfigAccessType_Type())
rcAutoConfigAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigAccessType.setStatus(_A)
class _RcAutoConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('management-access',2),(_J,3),('fail',4)))
_RcAutoConfigStatus_Type.__name__=_D
_RcAutoConfigStatus_Object=MibScalar
rcAutoConfigStatus=_RcAutoConfigStatus_Object((1,3,6,1,4,1,8886,6,1,28,19),_RcAutoConfigStatus_Type())
rcAutoConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigStatus.setStatus(_A)
class _RcAutoConfigLoadConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('tftp-fail',2),('load-fail',3),('config-conflict',4),('write-fail',5),('format-fail',6)))
_RcAutoConfigLoadConfigStatus_Type.__name__=_D
_RcAutoConfigLoadConfigStatus_Object=MibScalar
rcAutoConfigLoadConfigStatus=_RcAutoConfigLoadConfigStatus_Object((1,3,6,1,4,1,8886,6,1,28,20),_RcAutoConfigLoadConfigStatus_Type())
rcAutoConfigLoadConfigStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rcAutoConfigLoadConfigStatus.setStatus(_A)
_RcAutoConfigDhcpTftpAddress_Type=IpAddress
_RcAutoConfigDhcpTftpAddress_Object=MibScalar
rcAutoConfigDhcpTftpAddress=_RcAutoConfigDhcpTftpAddress_Object((1,3,6,1,4,1,8886,6,1,28,21),_RcAutoConfigDhcpTftpAddress_Type())
rcAutoConfigDhcpTftpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:rcAutoConfigDhcpTftpAddress.setStatus(_A)
class _RcAutoConfigErrorLineNum_Type(OctetString):defaultValue=OctetString('The configuration file line numbers which load failed.');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RcAutoConfigErrorLineNum_Type.__name__=_C
_RcAutoConfigErrorLineNum_Object=MibScalar
rcAutoConfigErrorLineNum=_RcAutoConfigErrorLineNum_Object((1,3,6,1,4,1,8886,6,1,28,22),_RcAutoConfigErrorLineNum_Type())
rcAutoConfigErrorLineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcAutoConfigErrorLineNum.setStatus(_A)
rcAutoConfigCompletionTrap=NotificationType((1,3,6,1,4,1,8886,6,1,28,9,1))
rcAutoConfigCompletionTrap.setObjects(*((_H,_K),(_H,_L)))
if mibBuilder.loadTexts:rcAutoConfigCompletionTrap.setStatus(_A)
rcAutoConfigLoadFailTrap=NotificationType((1,3,6,1,4,1,8886,6,1,28,9,2))
if mibBuilder.loadTexts:rcAutoConfigLoadFailTrap.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'rcAutoConfig':rcAutoConfig,'rcAutoConfigTftpServerAddress':rcAutoConfigTftpServerAddress,'rcAutoConfigFileName':rcAutoConfigFileName,'rcAutoConfigStartupEnable':rcAutoConfigStartupEnable,'rcAutoConfigOverwriteEnable':rcAutoConfigOverwriteEnable,'rcAutoConfigTrapEnable':rcAutoConfigTrapEnable,'rcAutoConfigCommand':rcAutoConfigCommand,'rcAutoConfigOperationStates':rcAutoConfigOperationStates,_L:rcAutoConfigResult,'rcAutoConfigTraps':rcAutoConfigTraps,'rcAutoConfigCompletionTrap':rcAutoConfigCompletionTrap,'rcAutoConfigLoadFailTrap':rcAutoConfigLoadFailTrap,'rcAutoConfigFilenameRule':rcAutoConfigFilenameRule,'rcAutoConfigSystemBootVersion':rcAutoConfigSystemBootVersion,'rcAutoConfigBootstrapVersion':rcAutoConfigBootstrapVersion,'rcAutoConfigStartupConfigVersion':rcAutoConfigStartupConfigVersion,'rcAutoConfigEnable':rcAutoConfigEnable,_K:rcAutoConfigCurrentFileType,'rcAutoConfigFilenamePrefix':rcAutoConfigFilenamePrefix,'rcAutoConfigFilenamePostfix':rcAutoConfigFilenamePostfix,'rcAutoConfigAccessType':rcAutoConfigAccessType,'rcAutoConfigStatus':rcAutoConfigStatus,'rcAutoConfigLoadConfigStatus':rcAutoConfigLoadConfigStatus,'rcAutoConfigDhcpTftpAddress':rcAutoConfigDhcpTftpAddress,'rcAutoConfigErrorLineNum':rcAutoConfigErrorLineNum})