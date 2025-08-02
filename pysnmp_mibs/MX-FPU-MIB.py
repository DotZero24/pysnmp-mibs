_I='mfpInstalledInfoIndex'
_H='MX-FPU-MIB'
_G='Unsigned32'
_F='MxEnableState'
_E='OctetString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_F,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fpuMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1300))
_FpuMIBObjects_ObjectIdentity=ObjectIdentity
fpuMIBObjects=_FpuMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1300,1))
_MfpInstalledInfoTable_Object=MibTable
mfpInstalledInfoTable=_MfpInstalledInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100))
if mibBuilder.loadTexts:mfpInstalledInfoTable.setStatus(_A)
_MfpInstalledInfoEntry_Object=MibTableRow
mfpInstalledInfoEntry=_MfpInstalledInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100,1))
mfpInstalledInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mfpInstalledInfoEntry.setStatus(_A)
_MfpInstalledInfoIndex_Type=Unsigned32
_MfpInstalledInfoIndex_Object=MibTableColumn
mfpInstalledInfoIndex=_MfpInstalledInfoIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100,1,50),_MfpInstalledInfoIndex_Type())
mfpInstalledInfoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpInstalledInfoIndex.setStatus(_A)
_MfpInstalledInfoMfpName_Type=OctetString
_MfpInstalledInfoMfpName_Object=MibTableColumn
mfpInstalledInfoMfpName=_MfpInstalledInfoMfpName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100,1,100),_MfpInstalledInfoMfpName_Type())
mfpInstalledInfoMfpName.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpInstalledInfoMfpName.setStatus(_A)
_MfpInstalledInfoMfpVersion_Type=OctetString
_MfpInstalledInfoMfpVersion_Object=MibTableColumn
mfpInstalledInfoMfpVersion=_MfpInstalledInfoMfpVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100,1,200),_MfpInstalledInfoMfpVersion_Type())
mfpInstalledInfoMfpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpInstalledInfoMfpVersion.setStatus(_A)
class _MfpInstalledInfoMfpBank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('none',100),('main',200),('recovery',300),('mainInUse',400),('recoveryInUse',500)))
_MfpInstalledInfoMfpBank_Type.__name__=_B
_MfpInstalledInfoMfpBank_Object=MibTableColumn
mfpInstalledInfoMfpBank=_MfpInstalledInfoMfpBank_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100,1,300),_MfpInstalledInfoMfpBank_Type())
mfpInstalledInfoMfpBank.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpInstalledInfoMfpBank.setStatus(_A)
class _MfpInstalledInfoMfpProfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MfpInstalledInfoMfpProfileName_Type.__name__=_E
_MfpInstalledInfoMfpProfileName_Object=MibTableColumn
mfpInstalledInfoMfpProfileName=_MfpInstalledInfoMfpProfileName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,100,1,400),_MfpInstalledInfoMfpProfileName_Type())
mfpInstalledInfoMfpProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpInstalledInfoMfpProfileName.setStatus(_A)
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*(('waitingSystemReady',100),('idle',200),('updating',300),('waitingManualRestart',400),('rollbacking',500),('waitingForGracefulRestart',600)))
_Status_Type.__name__=_B
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,110),_Status_Type())
status.setMaxAccess(_D)
if mibBuilder.loadTexts:status.setStatus(_A)
class _MfpLastInstallationResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('none',100),('success',200),('fail',300)))
_MfpLastInstallationResult_Type.__name__=_B
_MfpLastInstallationResult_Object=MibScalar
mfpLastInstallationResult=_MfpLastInstallationResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,125),_MfpLastInstallationResult_Type())
mfpLastInstallationResult.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpLastInstallationResult.setStatus(_A)
class _MfpLastInstallationDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MfpLastInstallationDateTime_Type.__name__=_E
_MfpLastInstallationDateTime_Object=MibScalar
mfpLastInstallationDateTime=_MfpLastInstallationDateTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,150),_MfpLastInstallationDateTime_Type())
mfpLastInstallationDateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpLastInstallationDateTime.setStatus(_A)
class _MfpRollbackAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_MfpRollbackAvailable_Type.__name__=_B
_MfpRollbackAvailable_Object=MibScalar
mfpRollbackAvailable=_MfpRollbackAvailable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,175),_MfpRollbackAvailable_Type())
mfpRollbackAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:mfpRollbackAvailable.setStatus(_A)
_MfpRepositoryGroup_ObjectIdentity=ObjectIdentity
mfpRepositoryGroup=_MfpRepositoryGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400))
_MfpTransferGroup_ObjectIdentity=ObjectIdentity
mfpTransferGroup=_MfpTransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200))
class _MfpTransferUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MfpTransferUsername_Type.__name__=_E
_MfpTransferUsername_Object=MibScalar
mfpTransferUsername=_MfpTransferUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200,200),_MfpTransferUsername_Type())
mfpTransferUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpTransferUsername.setStatus(_A)
class _MfpTransferPassword_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MfpTransferPassword_Type.__name__=_E
_MfpTransferPassword_Object=MibScalar
mfpTransferPassword=_MfpTransferPassword_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200,300),_MfpTransferPassword_Type())
mfpTransferPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpTransferPassword.setStatus(_A)
class _MfpTransferCertificateValidation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('noValidation',100),('hostName',200)))
_MfpTransferCertificateValidation_Type.__name__=_B
_MfpTransferCertificateValidation_Object=MibScalar
mfpTransferCertificateValidation=_MfpTransferCertificateValidation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200,500),_MfpTransferCertificateValidation_Type())
mfpTransferCertificateValidation.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpTransferCertificateValidation.setStatus(_A)
class _MfpTransferCertificateTrustLevel_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('locallyTrusted',100),('ocspOptional',200),('ocspMandatory',300)))
_MfpTransferCertificateTrustLevel_Type.__name__=_B
_MfpTransferCertificateTrustLevel_Object=MibScalar
mfpTransferCertificateTrustLevel=_MfpTransferCertificateTrustLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200,600),_MfpTransferCertificateTrustLevel_Type())
mfpTransferCertificateTrustLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpTransferCertificateTrustLevel.setStatus(_A)
class _MfpTransferCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_MfpTransferCipherSuite_Type.__name__=_B
_MfpTransferCipherSuite_Object=MibScalar
mfpTransferCipherSuite=_MfpTransferCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200,700),_MfpTransferCipherSuite_Type())
mfpTransferCipherSuite.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpTransferCipherSuite.setStatus(_A)
class _MfpTransferTlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),('tLSv1-1',300),('tLSv1-2',400)))
_MfpTransferTlsVersion_Type.__name__=_B
_MfpTransferTlsVersion_Object=MibScalar
mfpTransferTlsVersion=_MfpTransferTlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,400,200,800),_MfpTransferTlsVersion_Type())
mfpTransferTlsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpTransferTlsVersion.setStatus(_A)
class _MfpUrl_Type(OctetString):defaultValue=OctetString('')
_MfpUrl_Type.__name__=_E
_MfpUrl_Object=MibScalar
mfpUrl=_MfpUrl_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,450),_MfpUrl_Type())
mfpUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:mfpUrl.setStatus(_A)
class _AutomaticRestartEnable_Type(MxEnableState):defaultValue=0
_AutomaticRestartEnable_Type.__name__=_F
_AutomaticRestartEnable_Object=MibScalar
automaticRestartEnable=_AutomaticRestartEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,500),_AutomaticRestartEnable_Type())
automaticRestartEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:automaticRestartEnable.setStatus(_A)
class _AutomaticRestartGraceDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10080))
_AutomaticRestartGraceDelay_Type.__name__=_G
_AutomaticRestartGraceDelay_Object=MibScalar
automaticRestartGraceDelay=_AutomaticRestartGraceDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,600),_AutomaticRestartGraceDelay_Type())
automaticRestartGraceDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:automaticRestartGraceDelay.setStatus(_A)
class _DefaultSettingsOnInstall_Type(MxEnableState):defaultValue=0
_DefaultSettingsOnInstall_Type.__name__=_F
_DefaultSettingsOnInstall_Object=MibScalar
defaultSettingsOnInstall=_DefaultSettingsOnInstall_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,700),_DefaultSettingsOnInstall_Type())
defaultSettingsOnInstall.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultSettingsOnInstall.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1300,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'fpuMIB':fpuMIB,'fpuMIBObjects':fpuMIBObjects,'mfpInstalledInfoTable':mfpInstalledInfoTable,'mfpInstalledInfoEntry':mfpInstalledInfoEntry,_I:mfpInstalledInfoIndex,'mfpInstalledInfoMfpName':mfpInstalledInfoMfpName,'mfpInstalledInfoMfpVersion':mfpInstalledInfoMfpVersion,'mfpInstalledInfoMfpBank':mfpInstalledInfoMfpBank,'mfpInstalledInfoMfpProfileName':mfpInstalledInfoMfpProfileName,'status':status,'mfpLastInstallationResult':mfpLastInstallationResult,'mfpLastInstallationDateTime':mfpLastInstallationDateTime,'mfpRollbackAvailable':mfpRollbackAvailable,'mfpRepositoryGroup':mfpRepositoryGroup,'mfpTransferGroup':mfpTransferGroup,'mfpTransferUsername':mfpTransferUsername,'mfpTransferPassword':mfpTransferPassword,'mfpTransferCertificateValidation':mfpTransferCertificateValidation,'mfpTransferCertificateTrustLevel':mfpTransferCertificateTrustLevel,'mfpTransferCipherSuite':mfpTransferCipherSuite,'mfpTransferTlsVersion':mfpTransferTlsVersion,'mfpUrl':mfpUrl,'automaticRestartEnable':automaticRestartEnable,'automaticRestartGraceDelay':automaticRestartGraceDelay,'defaultSettingsOnInstall':defaultSettingsOnInstall,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})