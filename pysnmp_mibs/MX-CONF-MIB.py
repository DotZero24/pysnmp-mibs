_R='aliasName'
_Q='macrosName'
_P='transferFailed'
_O='transfering'
_N='tLSv1-2'
_M='tLSv1-1'
_L='0.0.0.0:0'
_K='MX-CONF-MIB'
_J='Unsigned32'
_I='MxIpHostNamePort'
_H='success'
_G='none'
_F='MxEnableState'
_E='read-only'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_F,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_I,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
confMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800))
_ConfMIBObjects_ObjectIdentity=ObjectIdentity
confMIBObjects=_ConfMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1))
_ScriptsGroup_ObjectIdentity=ObjectIdentity
scriptsGroup=_ScriptsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100))
class _ScriptGenericFileName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_ScriptGenericFileName_Type.__name__=_D
_ScriptGenericFileName_Object=MibScalar
scriptGenericFileName=_ScriptGenericFileName_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,100),_ScriptGenericFileName_Type())
scriptGenericFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptGenericFileName.setStatus(_A)
class _ScriptSpecificFileName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_ScriptSpecificFileName_Type.__name__=_D
_ScriptSpecificFileName_Object=MibScalar
scriptSpecificFileName=_ScriptSpecificFileName_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,200),_ScriptSpecificFileName_Type())
scriptSpecificFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptSpecificFileName.setStatus(_A)
class _ScriptsLocation_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ScriptsLocation_Type.__name__=_D
_ScriptsLocation_Object=MibScalar
scriptsLocation=_ScriptsLocation_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,300),_ScriptsLocation_Type())
scriptsLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsLocation.setStatus(_A)
_ScriptsTransferGroup_ObjectIdentity=ObjectIdentity
scriptsTransferGroup=_ScriptsTransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400))
class _ScriptsTransferProtocol_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('http',100),('https',200),('tftp',300),('ftp',400),('file',500)))
_ScriptsTransferProtocol_Type.__name__=_C
_ScriptsTransferProtocol_Object=MibScalar
scriptsTransferProtocol=_ScriptsTransferProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,100),_ScriptsTransferProtocol_Type())
scriptsTransferProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferProtocol.setStatus(_A)
class _ScriptsTransferUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ScriptsTransferUsername_Type.__name__=_D
_ScriptsTransferUsername_Object=MibScalar
scriptsTransferUsername=_ScriptsTransferUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,200),_ScriptsTransferUsername_Type())
scriptsTransferUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferUsername.setStatus(_A)
class _ScriptsTransferPassword_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ScriptsTransferPassword_Type.__name__=_D
_ScriptsTransferPassword_Object=MibScalar
scriptsTransferPassword=_ScriptsTransferPassword_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,300),_ScriptsTransferPassword_Type())
scriptsTransferPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferPassword.setStatus(_A)
class _ScriptsTransferSrvHostname_Type(MxIpHostNamePort):defaultValue=OctetString(_L)
_ScriptsTransferSrvHostname_Type.__name__=_I
_ScriptsTransferSrvHostname_Object=MibScalar
scriptsTransferSrvHostname=_ScriptsTransferSrvHostname_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,400),_ScriptsTransferSrvHostname_Type())
scriptsTransferSrvHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferSrvHostname.setStatus(_A)
class _ScriptsTransferCertificateValidation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('noValidation',100),('hostName',200)))
_ScriptsTransferCertificateValidation_Type.__name__=_C
_ScriptsTransferCertificateValidation_Object=MibScalar
scriptsTransferCertificateValidation=_ScriptsTransferCertificateValidation_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,500),_ScriptsTransferCertificateValidation_Type())
scriptsTransferCertificateValidation.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferCertificateValidation.setStatus(_A)
class _ScriptsTransferCertificateTrustLevel_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('locallyTrusted',100),('ocspOptional',200),('ocspMandatory',300)))
_ScriptsTransferCertificateTrustLevel_Type.__name__=_C
_ScriptsTransferCertificateTrustLevel_Object=MibScalar
scriptsTransferCertificateTrustLevel=_ScriptsTransferCertificateTrustLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,600),_ScriptsTransferCertificateTrustLevel_Type())
scriptsTransferCertificateTrustLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferCertificateTrustLevel.setStatus(_A)
class _ScriptsTransferCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_ScriptsTransferCipherSuite_Type.__name__=_C
_ScriptsTransferCipherSuite_Object=MibScalar
scriptsTransferCipherSuite=_ScriptsTransferCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,700),_ScriptsTransferCipherSuite_Type())
scriptsTransferCipherSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferCipherSuite.setStatus(_A)
class _ScriptsTransferTlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),(_M,300),(_N,400)))
_ScriptsTransferTlsVersion_Type.__name__=_C
_ScriptsTransferTlsVersion_Object=MibScalar
scriptsTransferTlsVersion=_ScriptsTransferTlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,800),_ScriptsTransferTlsVersion_Type())
scriptsTransferTlsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferTlsVersion.setStatus(_A)
class _ScriptsTransferHttpAuthenticationMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('normal',100),('proprietaryV1',200)))
_ScriptsTransferHttpAuthenticationMethod_Type.__name__=_C
_ScriptsTransferHttpAuthenticationMethod_Object=MibScalar
scriptsTransferHttpAuthenticationMethod=_ScriptsTransferHttpAuthenticationMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,400,900),_ScriptsTransferHttpAuthenticationMethod_Type())
scriptsTransferHttpAuthenticationMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferHttpAuthenticationMethod.setStatus(_A)
_AutomaticScriptsTransferGroup_ObjectIdentity=ObjectIdentity
automaticScriptsTransferGroup=_AutomaticScriptsTransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500))
class _ScriptsTransferOnRestartEnable_Type(MxEnableState):defaultValue=0
_ScriptsTransferOnRestartEnable_Type.__name__=_F
_ScriptsTransferOnRestartEnable_Object=MibScalar
scriptsTransferOnRestartEnable=_ScriptsTransferOnRestartEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,100),_ScriptsTransferOnRestartEnable_Type())
scriptsTransferOnRestartEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferOnRestartEnable.setStatus(_A)
class _ScriptsTransferRetriesNumber_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_ScriptsTransferRetriesNumber_Type.__name__=_C
_ScriptsTransferRetriesNumber_Object=MibScalar
scriptsTransferRetriesNumber=_ScriptsTransferRetriesNumber_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,150),_ScriptsTransferRetriesNumber_Type())
scriptsTransferRetriesNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferRetriesNumber.setStatus(_A)
class _ScriptsTransferPeriodicEnable_Type(MxEnableState):defaultValue=0
_ScriptsTransferPeriodicEnable_Type.__name__=_F
_ScriptsTransferPeriodicEnable_Object=MibScalar
scriptsTransferPeriodicEnable=_ScriptsTransferPeriodicEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,200),_ScriptsTransferPeriodicEnable_Type())
scriptsTransferPeriodicEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferPeriodicEnable.setStatus(_A)
class _ScriptsTransferPeriodicTimeUnit_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('minutes',100),('hours',200),('days',300)))
_ScriptsTransferPeriodicTimeUnit_Type.__name__=_C
_ScriptsTransferPeriodicTimeUnit_Object=MibScalar
scriptsTransferPeriodicTimeUnit=_ScriptsTransferPeriodicTimeUnit_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,300),_ScriptsTransferPeriodicTimeUnit_Type())
scriptsTransferPeriodicTimeUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferPeriodicTimeUnit.setStatus(_A)
class _ScriptsTransferInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ScriptsTransferInterval_Type.__name__=_J
_ScriptsTransferInterval_Object=MibScalar
scriptsTransferInterval=_ScriptsTransferInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,400),_ScriptsTransferInterval_Type())
scriptsTransferInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferInterval.setStatus(_A)
class _ScriptsTransferTimeOfDay_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,23))
_ScriptsTransferTimeOfDay_Type.__name__=_C
_ScriptsTransferTimeOfDay_Object=MibScalar
scriptsTransferTimeOfDay=_ScriptsTransferTimeOfDay_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,500),_ScriptsTransferTimeOfDay_Type())
scriptsTransferTimeOfDay.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferTimeOfDay.setStatus('obsolete')
class _ScriptsDhcpDownloadEnable_Type(MxEnableState):defaultValue=1
_ScriptsDhcpDownloadEnable_Type.__name__=_F
_ScriptsDhcpDownloadEnable_Object=MibScalar
scriptsDhcpDownloadEnable=_ScriptsDhcpDownloadEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,600),_ScriptsDhcpDownloadEnable_Type())
scriptsDhcpDownloadEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsDhcpDownloadEnable.setStatus(_A)
class _ScriptsDhcpOptionsFormat_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('fullyQualified',100),('url',200),('serverHost',300),('autoDetect',400)))
_ScriptsDhcpOptionsFormat_Type.__name__=_C
_ScriptsDhcpOptionsFormat_Object=MibScalar
scriptsDhcpOptionsFormat=_ScriptsDhcpOptionsFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,650),_ScriptsDhcpOptionsFormat_Type())
scriptsDhcpOptionsFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsDhcpOptionsFormat.setStatus(_A)
class _ScriptsTransferOnRestartDhcpScriptMaxDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,360))
_ScriptsTransferOnRestartDhcpScriptMaxDelay_Type.__name__=_J
_ScriptsTransferOnRestartDhcpScriptMaxDelay_Object=MibScalar
scriptsTransferOnRestartDhcpScriptMaxDelay=_ScriptsTransferOnRestartDhcpScriptMaxDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,660),_ScriptsTransferOnRestartDhcpScriptMaxDelay_Type())
scriptsTransferOnRestartDhcpScriptMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferOnRestartDhcpScriptMaxDelay.setStatus(_A)
class _ScriptsTransferTimeRange_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ScriptsTransferTimeRange_Type.__name__=_D
_ScriptsTransferTimeRange_Object=MibScalar
scriptsTransferTimeRange=_ScriptsTransferTimeRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,500,700),_ScriptsTransferTimeRange_Type())
scriptsTransferTimeRange.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsTransferTimeRange.setStatus(_A)
class _ScriptsSecretKey_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,112))
_ScriptsSecretKey_Type.__name__=_D
_ScriptsSecretKey_Object=MibScalar
scriptsSecretKey=_ScriptsSecretKey_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,600),_ScriptsSecretKey_Type())
scriptsSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsSecretKey.setStatus(_A)
class _ScriptsAllowRepeatedExecution_Type(MxEnableState):defaultValue=1
_ScriptsAllowRepeatedExecution_Type.__name__=_F
_ScriptsAllowRepeatedExecution_Object=MibScalar
scriptsAllowRepeatedExecution=_ScriptsAllowRepeatedExecution_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,650),_ScriptsAllowRepeatedExecution_Type())
scriptsAllowRepeatedExecution.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptsAllowRepeatedExecution.setStatus(_A)
_ScriptExportGroup_ObjectIdentity=ObjectIdentity
scriptExportGroup=_ScriptExportGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,1000))
class _ScriptExportContent_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('allConfig',100),('modifiedConfig',200)))
_ScriptExportContent_Type.__name__=_C
_ScriptExportContent_Object=MibScalar
scriptExportContent=_ScriptExportContent_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,1000,100),_ScriptExportContent_Type())
scriptExportContent.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptExportContent.setStatus(_A)
class _ScriptExportServiceName_Type(OctetString):defaultValue=OctetString('All');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ScriptExportServiceName_Type.__name__=_D
_ScriptExportServiceName_Object=MibScalar
scriptExportServiceName=_ScriptExportServiceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,1000,150),_ScriptExportServiceName_Type())
scriptExportServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptExportServiceName.setStatus(_A)
class _ScriptExportUrl_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_ScriptExportUrl_Type.__name__=_D
_ScriptExportUrl_Object=MibScalar
scriptExportUrl=_ScriptExportUrl_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,1000,200),_ScriptExportUrl_Type())
scriptExportUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptExportUrl.setStatus(_A)
class _ScriptExportSecretKey_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ScriptExportSecretKey_Type.__name__=_D
_ScriptExportSecretKey_Object=MibScalar
scriptExportSecretKey=_ScriptExportSecretKey_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,1000,300),_ScriptExportSecretKey_Type())
scriptExportSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:scriptExportSecretKey.setStatus(_A)
_ScriptsStatsGroup_ObjectIdentity=ObjectIdentity
scriptsStatsGroup=_ScriptsStatsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000))
class _ScriptsStatsCurrentTransferState_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('idle',100),(_O,200),('running',300)))
_ScriptsStatsCurrentTransferState_Type.__name__=_C
_ScriptsStatsCurrentTransferState_Object=MibScalar
scriptsStatsCurrentTransferState=_ScriptsStatsCurrentTransferState_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000,700),_ScriptsStatsCurrentTransferState_Type())
scriptsStatsCurrentTransferState.setMaxAccess(_E)
if mibBuilder.loadTexts:scriptsStatsCurrentTransferState.setStatus(_A)
class _ScriptsStatsLastTransferResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_G,100),(_H,200),('executionFailed',300),(_P,400)))
_ScriptsStatsLastTransferResult_Type.__name__=_C
_ScriptsStatsLastTransferResult_Object=MibScalar
scriptsStatsLastTransferResult=_ScriptsStatsLastTransferResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000,800),_ScriptsStatsLastTransferResult_Type())
scriptsStatsLastTransferResult.setMaxAccess(_E)
if mibBuilder.loadTexts:scriptsStatsLastTransferResult.setStatus(_A)
class _ScriptsStatsLastTransferDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ScriptsStatsLastTransferDateTime_Type.__name__=_D
_ScriptsStatsLastTransferDateTime_Object=MibScalar
scriptsStatsLastTransferDateTime=_ScriptsStatsLastTransferDateTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000,900),_ScriptsStatsLastTransferDateTime_Type())
scriptsStatsLastTransferDateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:scriptsStatsLastTransferDateTime.setStatus(_A)
class _ScriptsStatsCurrentExportState_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('idle',100),(_O,200),('exporting',300)))
_ScriptsStatsCurrentExportState_Type.__name__=_C
_ScriptsStatsCurrentExportState_Object=MibScalar
scriptsStatsCurrentExportState=_ScriptsStatsCurrentExportState_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000,1000),_ScriptsStatsCurrentExportState_Type())
scriptsStatsCurrentExportState.setMaxAccess(_E)
if mibBuilder.loadTexts:scriptsStatsCurrentExportState.setStatus(_A)
class _ScriptsStatsLastExportResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_G,100),(_H,200),('exportationFailed',300),(_P,400)))
_ScriptsStatsLastExportResult_Type.__name__=_C
_ScriptsStatsLastExportResult_Object=MibScalar
scriptsStatsLastExportResult=_ScriptsStatsLastExportResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000,1100),_ScriptsStatsLastExportResult_Type())
scriptsStatsLastExportResult.setMaxAccess(_E)
if mibBuilder.loadTexts:scriptsStatsLastExportResult.setStatus(_A)
class _ScriptsStatsLastExportDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ScriptsStatsLastExportDateTime_Type.__name__=_D
_ScriptsStatsLastExportDateTime_Object=MibScalar
scriptsStatsLastExportDateTime=_ScriptsStatsLastExportDateTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,100,10000,1200),_ScriptsStatsLastExportDateTime_Type())
scriptsStatsLastExportDateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:scriptsStatsLastExportDateTime.setStatus(_A)
_ImageGroup_ObjectIdentity=ObjectIdentity
imageGroup=_ImageGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200))
class _ImageFileName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_ImageFileName_Type.__name__=_D
_ImageFileName_Object=MibScalar
imageFileName=_ImageFileName_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,100),_ImageFileName_Type())
imageFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:imageFileName.setStatus(_A)
class _ImageLocation_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ImageLocation_Type.__name__=_D
_ImageLocation_Object=MibScalar
imageLocation=_ImageLocation_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,200),_ImageLocation_Type())
imageLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:imageLocation.setStatus(_A)
class _ImageBackupContent_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('config',100),('configAndCertificates',200)))
_ImageBackupContent_Type.__name__=_C
_ImageBackupContent_Object=MibScalar
imageBackupContent=_ImageBackupContent_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,250),_ImageBackupContent_Type())
imageBackupContent.setMaxAccess(_B)
if mibBuilder.loadTexts:imageBackupContent.setStatus(_A)
_ImageTransferGroup_ObjectIdentity=ObjectIdentity
imageTransferGroup=_ImageTransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300))
class _ImageTransferProtocol_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('http',100),('https',200),('tftp',300),('ftp',400),('file',500)))
_ImageTransferProtocol_Type.__name__=_C
_ImageTransferProtocol_Object=MibScalar
imageTransferProtocol=_ImageTransferProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300,100),_ImageTransferProtocol_Type())
imageTransferProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:imageTransferProtocol.setStatus(_A)
class _ImageTransferUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageTransferUsername_Type.__name__=_D
_ImageTransferUsername_Object=MibScalar
imageTransferUsername=_ImageTransferUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300,200),_ImageTransferUsername_Type())
imageTransferUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:imageTransferUsername.setStatus(_A)
class _ImageTransferPassword_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageTransferPassword_Type.__name__=_D
_ImageTransferPassword_Object=MibScalar
imageTransferPassword=_ImageTransferPassword_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300,300),_ImageTransferPassword_Type())
imageTransferPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:imageTransferPassword.setStatus(_A)
class _ImageTransferSrvHostname_Type(MxIpHostNamePort):defaultValue=OctetString(_L)
_ImageTransferSrvHostname_Type.__name__=_I
_ImageTransferSrvHostname_Object=MibScalar
imageTransferSrvHostname=_ImageTransferSrvHostname_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300,400),_ImageTransferSrvHostname_Type())
imageTransferSrvHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:imageTransferSrvHostname.setStatus(_A)
class _ImageTransferCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_ImageTransferCipherSuite_Type.__name__=_C
_ImageTransferCipherSuite_Object=MibScalar
imageTransferCipherSuite=_ImageTransferCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300,500),_ImageTransferCipherSuite_Type())
imageTransferCipherSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:imageTransferCipherSuite.setStatus(_A)
class _ImageTransferTlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),(_M,300),(_N,400)))
_ImageTransferTlsVersion_Type.__name__=_C
_ImageTransferTlsVersion_Object=MibScalar
imageTransferTlsVersion=_ImageTransferTlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,300,600),_ImageTransferTlsVersion_Type())
imageTransferTlsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:imageTransferTlsVersion.setStatus(_A)
_ImagePrivacyGroup_ObjectIdentity=ObjectIdentity
imagePrivacyGroup=_ImagePrivacyGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,400))
class _ImagePrivacyAlgo_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_G,100),('defaultAlgo',200)))
_ImagePrivacyAlgo_Type.__name__=_C
_ImagePrivacyAlgo_Object=MibScalar
imagePrivacyAlgo=_ImagePrivacyAlgo_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,400,100),_ImagePrivacyAlgo_Type())
imagePrivacyAlgo.setMaxAccess(_B)
if mibBuilder.loadTexts:imagePrivacyAlgo.setStatus(_A)
class _ImageSecretKey_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ImageSecretKey_Type.__name__=_D
_ImageSecretKey_Object=MibScalar
imageSecretKey=_ImageSecretKey_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,400,200),_ImageSecretKey_Type())
imageSecretKey.setMaxAccess(_B)
if mibBuilder.loadTexts:imageSecretKey.setStatus(_A)
class _ImageBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_G,100),(_H,200),('failed',300)))
_ImageBackupStatus_Type.__name__=_C
_ImageBackupStatus_Object=MibScalar
imageBackupStatus=_ImageBackupStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,600),_ImageBackupStatus_Type())
imageBackupStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:imageBackupStatus.setStatus(_A)
class _ImageRestoreStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_G,100),(_H,200),('applyFailed',300),('loadFailed',400)))
_ImageRestoreStatus_Type.__name__=_C
_ImageRestoreStatus_Object=MibScalar
imageRestoreStatus=_ImageRestoreStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,200,800),_ImageRestoreStatus_Type())
imageRestoreStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:imageRestoreStatus.setStatus(_A)
_AliasGroup_ObjectIdentity=ObjectIdentity
aliasGroup=_AliasGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300))
_MacrosTable_Object=MibTable
macrosTable=_MacrosTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,100))
if mibBuilder.loadTexts:macrosTable.setStatus(_A)
_MacrosEntry_Object=MibTableRow
macrosEntry=_MacrosEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,100,1))
macrosEntry.setIndexNames((0,_K,_Q))
if mibBuilder.loadTexts:macrosEntry.setStatus(_A)
class _MacrosName_Type(OctetString):defaultValue=OctetString('')
_MacrosName_Type.__name__=_D
_MacrosName_Object=MibTableColumn
macrosName=_MacrosName_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,100,1,100),_MacrosName_Type())
macrosName.setMaxAccess(_E)
if mibBuilder.loadTexts:macrosName.setStatus(_A)
class _MacrosDescription_Type(OctetString):defaultValue=OctetString('')
_MacrosDescription_Type.__name__=_D
_MacrosDescription_Object=MibTableColumn
macrosDescription=_MacrosDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,100,1,200),_MacrosDescription_Type())
macrosDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:macrosDescription.setStatus(_A)
_AliasTable_Object=MibTable
aliasTable=_AliasTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,200))
if mibBuilder.loadTexts:aliasTable.setStatus(_A)
_AliasEntry_Object=MibTableRow
aliasEntry=_AliasEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,200,1))
aliasEntry.setIndexNames((0,_K,_R))
if mibBuilder.loadTexts:aliasEntry.setStatus(_A)
class _AliasName_Type(OctetString):defaultValue=OctetString('')
_AliasName_Type.__name__=_D
_AliasName_Object=MibTableColumn
aliasName=_AliasName_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,200,1,100),_AliasName_Type())
aliasName.setMaxAccess(_E)
if mibBuilder.loadTexts:aliasName.setStatus(_A)
_AliasEntity_Type=OctetString
_AliasEntity_Object=MibTableColumn
aliasEntity=_AliasEntity_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,200,1,200),_AliasEntity_Type())
aliasEntity.setMaxAccess(_E)
if mibBuilder.loadTexts:aliasEntity.setStatus(_A)
class _AliasType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('module',100),('object',200),('columnar',300)))
_AliasType_Type.__name__=_C
_AliasType_Object=MibTableColumn
aliasType=_AliasType_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,200,1,300),_AliasType_Type())
aliasType.setMaxAccess(_E)
if mibBuilder.loadTexts:aliasType.setStatus(_A)
_AliasContext_Type=OctetString
_AliasContext_Object=MibTableColumn
aliasContext=_AliasContext_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,300,200,1,400),_AliasContext_Type())
aliasContext.setMaxAccess(_E)
if mibBuilder.loadTexts:aliasContext.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,800,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,800,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'confMIB':confMIB,'confMIBObjects':confMIBObjects,'scriptsGroup':scriptsGroup,'scriptGenericFileName':scriptGenericFileName,'scriptSpecificFileName':scriptSpecificFileName,'scriptsLocation':scriptsLocation,'scriptsTransferGroup':scriptsTransferGroup,'scriptsTransferProtocol':scriptsTransferProtocol,'scriptsTransferUsername':scriptsTransferUsername,'scriptsTransferPassword':scriptsTransferPassword,'scriptsTransferSrvHostname':scriptsTransferSrvHostname,'scriptsTransferCertificateValidation':scriptsTransferCertificateValidation,'scriptsTransferCertificateTrustLevel':scriptsTransferCertificateTrustLevel,'scriptsTransferCipherSuite':scriptsTransferCipherSuite,'scriptsTransferTlsVersion':scriptsTransferTlsVersion,'scriptsTransferHttpAuthenticationMethod':scriptsTransferHttpAuthenticationMethod,'automaticScriptsTransferGroup':automaticScriptsTransferGroup,'scriptsTransferOnRestartEnable':scriptsTransferOnRestartEnable,'scriptsTransferRetriesNumber':scriptsTransferRetriesNumber,'scriptsTransferPeriodicEnable':scriptsTransferPeriodicEnable,'scriptsTransferPeriodicTimeUnit':scriptsTransferPeriodicTimeUnit,'scriptsTransferInterval':scriptsTransferInterval,'scriptsTransferTimeOfDay':scriptsTransferTimeOfDay,'scriptsDhcpDownloadEnable':scriptsDhcpDownloadEnable,'scriptsDhcpOptionsFormat':scriptsDhcpOptionsFormat,'scriptsTransferOnRestartDhcpScriptMaxDelay':scriptsTransferOnRestartDhcpScriptMaxDelay,'scriptsTransferTimeRange':scriptsTransferTimeRange,'scriptsSecretKey':scriptsSecretKey,'scriptsAllowRepeatedExecution':scriptsAllowRepeatedExecution,'scriptExportGroup':scriptExportGroup,'scriptExportContent':scriptExportContent,'scriptExportServiceName':scriptExportServiceName,'scriptExportUrl':scriptExportUrl,'scriptExportSecretKey':scriptExportSecretKey,'scriptsStatsGroup':scriptsStatsGroup,'scriptsStatsCurrentTransferState':scriptsStatsCurrentTransferState,'scriptsStatsLastTransferResult':scriptsStatsLastTransferResult,'scriptsStatsLastTransferDateTime':scriptsStatsLastTransferDateTime,'scriptsStatsCurrentExportState':scriptsStatsCurrentExportState,'scriptsStatsLastExportResult':scriptsStatsLastExportResult,'scriptsStatsLastExportDateTime':scriptsStatsLastExportDateTime,'imageGroup':imageGroup,'imageFileName':imageFileName,'imageLocation':imageLocation,'imageBackupContent':imageBackupContent,'imageTransferGroup':imageTransferGroup,'imageTransferProtocol':imageTransferProtocol,'imageTransferUsername':imageTransferUsername,'imageTransferPassword':imageTransferPassword,'imageTransferSrvHostname':imageTransferSrvHostname,'imageTransferCipherSuite':imageTransferCipherSuite,'imageTransferTlsVersion':imageTransferTlsVersion,'imagePrivacyGroup':imagePrivacyGroup,'imagePrivacyAlgo':imagePrivacyAlgo,'imageSecretKey':imageSecretKey,'imageBackupStatus':imageBackupStatus,'imageRestoreStatus':imageRestoreStatus,'aliasGroup':aliasGroup,'macrosTable':macrosTable,'macrosEntry':macrosEntry,_Q:macrosName,'macrosDescription':macrosDescription,'aliasTable':aliasTable,'aliasEntry':aliasEntry,_R:aliasName,'aliasEntity':aliasEntity,'aliasType':aliasType,'aliasContext':aliasContext,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})