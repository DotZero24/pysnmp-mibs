_M='critical'
_L='warning'
_K='localLogMessagesIndex'
_J='eventsIndex'
_I='MxIpHostNamePort'
_H='MX-NLM-MIB'
_G='MxEnableState'
_F='Unsigned32'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_G,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_I,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nlmMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100))
_NlmMIBObjects_ObjectIdentity=ObjectIdentity
nlmMIBObjects=_NlmMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1))
_SyslogGroup_ObjectIdentity=ObjectIdentity
syslogGroup=_SyslogGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,100))
class _SyslogRemoteHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_SyslogRemoteHost_Type.__name__=_I
_SyslogRemoteHost_Object=MibScalar
syslogRemoteHost=_SyslogRemoteHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,100,100),_SyslogRemoteHost_Type())
syslogRemoteHost.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogRemoteHost.setStatus(_A)
class _SyslogMessageFormat_Type(OctetString):defaultValue=OctetString('%servicetextkey: %serviceid-%servicename: %msgid-%message');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SyslogMessageFormat_Type.__name__=_E
_SyslogMessageFormat_Object=MibScalar
syslogMessageFormat=_SyslogMessageFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,100,200),_SyslogMessageFormat_Type())
syslogMessageFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogMessageFormat.setStatus(_A)
_EventsTable_Object=MibTable
eventsTable=_EventsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200))
if mibBuilder.loadTexts:eventsTable.setStatus(_A)
_EventsEntry_Object=MibTableRow
eventsEntry=_EventsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1))
eventsEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:eventsEntry.setStatus(_A)
_EventsIndex_Type=Unsigned32
_EventsIndex_Object=MibTableColumn
eventsIndex=_EventsIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,100),_EventsIndex_Type())
eventsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eventsIndex.setStatus(_A)
class _EventsActivation_Type(MxEnableState):defaultValue=1
_EventsActivation_Type.__name__=_G
_EventsActivation_Object=MibTableColumn
eventsActivation=_EventsActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,200),_EventsActivation_Type())
eventsActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:eventsActivation.setStatus(_A)
class _EventsType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(100));namedValues=NamedValues(('notification',100))
_EventsType_Type.__name__=_D
_EventsType_Object=MibTableColumn
eventsType=_EventsType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,300),_EventsType_Type())
eventsType.setMaxAccess(_B)
if mibBuilder.loadTexts:eventsType.setStatus(_A)
class _EventsCriteria_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_EventsCriteria_Type.__name__=_E
_EventsCriteria_Object=MibTableColumn
eventsCriteria=_EventsCriteria_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,400),_EventsCriteria_Type())
eventsCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:eventsCriteria.setStatus(_A)
class _EventsAction_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sendViaSyslog',100),('sendViaSip',200),('logLocally',300),('logToFile',400)))
_EventsAction_Type.__name__=_D
_EventsAction_Object=MibTableColumn
eventsAction=_EventsAction_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,500),_EventsAction_Type())
eventsAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eventsAction.setStatus(_A)
class _EventsConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('valid',100),('invalid',200),('notSupported',300)))
_EventsConfigStatus_Type.__name__=_D
_EventsConfigStatus_Object=MibTableColumn
eventsConfigStatus=_EventsConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,600),_EventsConfigStatus_Type())
eventsConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eventsConfigStatus.setStatus(_A)
class _EventsDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('delete',10)))
_EventsDelete_Type.__name__=_D
_EventsDelete_Object=MibTableColumn
eventsDelete=_EventsDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,200,1,10000),_EventsDelete_Type())
eventsDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:eventsDelete.setStatus(_A)
_LocalLogGroup_ObjectIdentity=ObjectIdentity
localLogGroup=_LocalLogGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300))
_LocalLogMaxNbEntries_Type=Unsigned32
_LocalLogMaxNbEntries_Object=MibScalar
localLogMaxNbEntries=_LocalLogMaxNbEntries_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,100),_LocalLogMaxNbEntries_Type())
localLogMaxNbEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMaxNbEntries.setStatus(_A)
_LocalLogNbErrorEntries_Type=Unsigned32
_LocalLogNbErrorEntries_Object=MibScalar
localLogNbErrorEntries=_LocalLogNbErrorEntries_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,200),_LocalLogNbErrorEntries_Type())
localLogNbErrorEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogNbErrorEntries.setStatus(_A)
_LocalLogNbCriticalEntries_Type=Unsigned32
_LocalLogNbCriticalEntries_Object=MibScalar
localLogNbCriticalEntries=_LocalLogNbCriticalEntries_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,300),_LocalLogNbCriticalEntries_Type())
localLogNbCriticalEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogNbCriticalEntries.setStatus(_A)
_LocalLogMessagesTable_Object=MibTable
localLogMessagesTable=_LocalLogMessagesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500))
if mibBuilder.loadTexts:localLogMessagesTable.setStatus(_A)
_LocalLogMessagesEntry_Object=MibTableRow
localLogMessagesEntry=_LocalLogMessagesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1))
localLogMessagesEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:localLogMessagesEntry.setStatus(_A)
_LocalLogMessagesIndex_Type=Unsigned32
_LocalLogMessagesIndex_Object=MibTableColumn
localLogMessagesIndex=_LocalLogMessagesIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,100),_LocalLogMessagesIndex_Type())
localLogMessagesIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesIndex.setStatus(_A)
_LocalLogMessagesLocalTime_Type=OctetString
_LocalLogMessagesLocalTime_Object=MibTableColumn
localLogMessagesLocalTime=_LocalLogMessagesLocalTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,200),_LocalLogMessagesLocalTime_Type())
localLogMessagesLocalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesLocalTime.setStatus(_A)
_LocalLogMessagesServiceNumkey_Type=Unsigned32
_LocalLogMessagesServiceNumkey_Object=MibTableColumn
localLogMessagesServiceNumkey=_LocalLogMessagesServiceNumkey_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,300),_LocalLogMessagesServiceNumkey_Type())
localLogMessagesServiceNumkey.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesServiceNumkey.setStatus(_A)
_LocalLogMessagesNotificationId_Type=Unsigned32
_LocalLogMessagesNotificationId_Object=MibTableColumn
localLogMessagesNotificationId=_LocalLogMessagesNotificationId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,400),_LocalLogMessagesNotificationId_Type())
localLogMessagesNotificationId.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesNotificationId.setStatus(_A)
class _LocalLogMessagesSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('debug',100),('information',200),(_L,300),('error',400),(_M,500)))
_LocalLogMessagesSeverity_Type.__name__=_D
_LocalLogMessagesSeverity_Object=MibTableColumn
localLogMessagesSeverity=_LocalLogMessagesSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,500),_LocalLogMessagesSeverity_Type())
localLogMessagesSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesSeverity.setStatus(_A)
_LocalLogMessagesServiceTextkey_Type=OctetString
_LocalLogMessagesServiceTextkey_Object=MibTableColumn
localLogMessagesServiceTextkey=_LocalLogMessagesServiceTextkey_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,600),_LocalLogMessagesServiceTextkey_Type())
localLogMessagesServiceTextkey.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesServiceTextkey.setStatus(_A)
_LocalLogMessagesMessage_Type=OctetString
_LocalLogMessagesMessage_Object=MibTableColumn
localLogMessagesMessage=_LocalLogMessagesMessage_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,300,500,1,700),_LocalLogMessagesMessage_Type())
localLogMessagesMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:localLogMessagesMessage.setStatus(_A)
_LogFileGroup_ObjectIdentity=ObjectIdentity
logFileGroup=_LogFileGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,400))
class _LogFileBaseName_Type(OctetString):defaultValue=OctetString('Notifications');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_LogFileBaseName_Type.__name__=_E
_LogFileBaseName_Object=MibScalar
logFileBaseName=_LogFileBaseName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,400,100),_LogFileBaseName_Type())
logFileBaseName.setMaxAccess(_B)
if mibBuilder.loadTexts:logFileBaseName.setStatus(_A)
class _LogFileMaxSize_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_LogFileMaxSize_Type.__name__=_F
_LogFileMaxSize_Object=MibScalar
logFileMaxSize=_LogFileMaxSize_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,400,200),_LogFileMaxSize_Type())
logFileMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:logFileMaxSize.setStatus(_A)
class _LogFileMaxNb_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LogFileMaxNb_Type.__name__=_F
_LogFileMaxNb_Object=MibScalar
logFileMaxNb=_LogFileMaxNb_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,400,300),_LogFileMaxNb_Type())
logFileMaxNb.setMaxAccess(_B)
if mibBuilder.loadTexts:logFileMaxNb.setStatus(_A)
_PCaptureGroup_ObjectIdentity=ObjectIdentity
pCaptureGroup=_PCaptureGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500))
class _PCaptureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100)));namedValues=NamedValues(*(('none',100),('requested',200),('completed',300),('undefinedFailure',400),('urlFailure',500),('filterFailure',600),('authenticationFailure',700),('hostUnreachableFailure',800),('tlsCertificateFailure',900),('sizeLimitFailure',1000),('linkFailure',1100)))
_PCaptureState_Type.__name__=_D
_PCaptureState_Object=MibScalar
pCaptureState=_PCaptureState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,100),_PCaptureState_Type())
pCaptureState.setMaxAccess(_C)
if mibBuilder.loadTexts:pCaptureState.setStatus(_A)
class _PCaptureNbFrames_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483648))
_PCaptureNbFrames_Type.__name__=_F
_PCaptureNbFrames_Object=MibScalar
pCaptureNbFrames=_PCaptureNbFrames_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,200),_PCaptureNbFrames_Type())
pCaptureNbFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureNbFrames.setStatus(_A)
class _PCaptureNbSecs_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2678400))
_PCaptureNbSecs_Type.__name__=_F
_PCaptureNbSecs_Object=MibScalar
pCaptureNbSecs=_PCaptureNbSecs_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,300),_PCaptureNbSecs_Type())
pCaptureNbSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureNbSecs.setStatus(_A)
class _PCaptureFilter_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_PCaptureFilter_Type.__name__=_E
_PCaptureFilter_Object=MibScalar
pCaptureFilter=_PCaptureFilter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,400),_PCaptureFilter_Type())
pCaptureFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureFilter.setStatus(_A)
class _PCaptureFileUrl_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_PCaptureFileUrl_Type.__name__=_E
_PCaptureFileUrl_Object=MibScalar
pCaptureFileUrl=_PCaptureFileUrl_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,500),_PCaptureFileUrl_Type())
pCaptureFileUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureFileUrl.setStatus(_A)
class _PCaptureLinkName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_PCaptureLinkName_Type.__name__=_E
_PCaptureLinkName_Object=MibScalar
pCaptureLinkName=_PCaptureLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,550),_PCaptureLinkName_Type())
pCaptureLinkName.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureLinkName.setStatus(_A)
_PCaptureTransferGroup_ObjectIdentity=ObjectIdentity
pCaptureTransferGroup=_PCaptureTransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,800))
class _PCaptureTransferCertificateValidation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('noValidation',100),('hostName',200)))
_PCaptureTransferCertificateValidation_Type.__name__=_D
_PCaptureTransferCertificateValidation_Object=MibScalar
pCaptureTransferCertificateValidation=_PCaptureTransferCertificateValidation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,800,100),_PCaptureTransferCertificateValidation_Type())
pCaptureTransferCertificateValidation.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureTransferCertificateValidation.setStatus(_A)
class _PCaptureTransferCertificateTrustLevel_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('locallyTrusted',100),('ocspOptional',200),('ocspMandatory',300)))
_PCaptureTransferCertificateTrustLevel_Type.__name__=_D
_PCaptureTransferCertificateTrustLevel_Object=MibScalar
pCaptureTransferCertificateTrustLevel=_PCaptureTransferCertificateTrustLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,800,200),_PCaptureTransferCertificateTrustLevel_Type())
pCaptureTransferCertificateTrustLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureTransferCertificateTrustLevel.setStatus(_A)
class _PCaptureTransferCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_PCaptureTransferCipherSuite_Type.__name__=_D
_PCaptureTransferCipherSuite_Object=MibScalar
pCaptureTransferCipherSuite=_PCaptureTransferCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,800,300),_PCaptureTransferCipherSuite_Type())
pCaptureTransferCipherSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureTransferCipherSuite.setStatus(_A)
class _PCaptureTransferTlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),('tLSv1-1',300),('tLSv1-2',400)))
_PCaptureTransferTlsVersion_Type.__name__=_D
_PCaptureTransferTlsVersion_Object=MibScalar
pCaptureTransferTlsVersion=_PCaptureTransferTlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,500,800,400),_PCaptureTransferTlsVersion_Type())
pCaptureTransferTlsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pCaptureTransferTlsVersion.setStatus(_A)
_DiagLogGroup_ObjectIdentity=ObjectIdentity
diagLogGroup=_DiagLogGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,600))
class _DiagLogAutomaticDump_Type(MxEnableState):defaultValue=1
_DiagLogAutomaticDump_Type.__name__=_G
_DiagLogAutomaticDump_Object=MibScalar
diagLogAutomaticDump=_DiagLogAutomaticDump_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,600,100),_DiagLogAutomaticDump_Type())
diagLogAutomaticDump.setMaxAccess(_B)
if mibBuilder.loadTexts:diagLogAutomaticDump.setStatus(_A)
_TacGroup_ObjectIdentity=ObjectIdentity
tacGroup=_TacGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,10000))
class _DiagnosticTracesEnable_Type(MxEnableState):defaultValue=0
_DiagnosticTracesEnable_Type.__name__=_G
_DiagnosticTracesEnable_Object=MibScalar
diagnosticTracesEnable=_DiagnosticTracesEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,10000,100),_DiagnosticTracesEnable_Type())
diagnosticTracesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:diagnosticTracesEnable.setStatus(_A)
class _DiagnosticTracesFilter_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_DiagnosticTracesFilter_Type.__name__=_E
_DiagnosticTracesFilter_Object=MibScalar
diagnosticTracesFilter=_DiagnosticTracesFilter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,10000,200),_DiagnosticTracesFilter_Type())
diagnosticTracesFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:diagnosticTracesFilter.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),(_L,300),('error',400),(_M,500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1100,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'nlmMIB':nlmMIB,'nlmMIBObjects':nlmMIBObjects,'syslogGroup':syslogGroup,'syslogRemoteHost':syslogRemoteHost,'syslogMessageFormat':syslogMessageFormat,'eventsTable':eventsTable,'eventsEntry':eventsEntry,_J:eventsIndex,'eventsActivation':eventsActivation,'eventsType':eventsType,'eventsCriteria':eventsCriteria,'eventsAction':eventsAction,'eventsConfigStatus':eventsConfigStatus,'eventsDelete':eventsDelete,'localLogGroup':localLogGroup,'localLogMaxNbEntries':localLogMaxNbEntries,'localLogNbErrorEntries':localLogNbErrorEntries,'localLogNbCriticalEntries':localLogNbCriticalEntries,'localLogMessagesTable':localLogMessagesTable,'localLogMessagesEntry':localLogMessagesEntry,_K:localLogMessagesIndex,'localLogMessagesLocalTime':localLogMessagesLocalTime,'localLogMessagesServiceNumkey':localLogMessagesServiceNumkey,'localLogMessagesNotificationId':localLogMessagesNotificationId,'localLogMessagesSeverity':localLogMessagesSeverity,'localLogMessagesServiceTextkey':localLogMessagesServiceTextkey,'localLogMessagesMessage':localLogMessagesMessage,'logFileGroup':logFileGroup,'logFileBaseName':logFileBaseName,'logFileMaxSize':logFileMaxSize,'logFileMaxNb':logFileMaxNb,'pCaptureGroup':pCaptureGroup,'pCaptureState':pCaptureState,'pCaptureNbFrames':pCaptureNbFrames,'pCaptureNbSecs':pCaptureNbSecs,'pCaptureFilter':pCaptureFilter,'pCaptureFileUrl':pCaptureFileUrl,'pCaptureLinkName':pCaptureLinkName,'pCaptureTransferGroup':pCaptureTransferGroup,'pCaptureTransferCertificateValidation':pCaptureTransferCertificateValidation,'pCaptureTransferCertificateTrustLevel':pCaptureTransferCertificateTrustLevel,'pCaptureTransferCipherSuite':pCaptureTransferCipherSuite,'pCaptureTransferTlsVersion':pCaptureTransferTlsVersion,'diagLogGroup':diagLogGroup,'diagLogAutomaticDump':diagLogAutomaticDump,'tacGroup':tacGroup,'diagnosticTracesEnable':diagnosticTracesEnable,'diagnosticTracesFilter':diagnosticTracesFilter,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})