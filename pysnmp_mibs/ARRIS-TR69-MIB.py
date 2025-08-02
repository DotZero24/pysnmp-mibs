_T='arrisTR181DeviceInfoProcessStatusProcessIndex'
_S='not-accessible'
_R='arrisTR69RootCertIndex'
_Q='cwmp13'
_P='cwmp12'
_O='cwmp11'
_N='cwmp10'
_M='ARRIS-TR69-MIB'
_L='true'
_K='false'
_J='Unsigned32'
_I='enable'
_H='disable'
_G='DisplayString'
_F='read-create'
_E='read-only'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arrisProdIdCM,=mibBuilder.importSymbols('ARRIS-MIB','arrisProdIdCM')
InetVersion,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetVersion')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
arrisTR69Mib=ModuleIdentity((1,3,6,1,4,1,4115,1,3,7))
if mibBuilder.loadTexts:arrisTR69Mib.setRevisions(('1915-07-07 00:00','1915-02-12 00:00','1913-11-04 00:00','1913-04-30 00:00','1913-02-05 00:00','1913-04-11 00:00','1913-03-04 00:00','1912-08-01 00:00','1912-01-19 00:00','1911-07-18 00:00'))
_ArrisTR69MibObjects_ObjectIdentity=ObjectIdentity
arrisTR69MibObjects=_ArrisTR69MibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,1))
_ArrisTR69Base_ObjectIdentity=ObjectIdentity
arrisTR69Base=_ArrisTR69Base_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,1,1))
class _ArrisTR69EnableCWMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ArrisTR69EnableCWMP_Type.__name__=_D
_ArrisTR69EnableCWMP_Object=MibScalar
arrisTR69EnableCWMP=_ArrisTR69EnableCWMP_Object((1,3,6,1,4,1,4115,1,3,7,1,1,1),_ArrisTR69EnableCWMP_Type())
arrisTR69EnableCWMP.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69EnableCWMP.setStatus(_A)
class _ArrisTR69AcsUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69AcsUrl_Type.__name__=_C
_ArrisTR69AcsUrl_Object=MibScalar
arrisTR69AcsUrl=_ArrisTR69AcsUrl_Object((1,3,6,1,4,1,4115,1,3,7,1,1,2),_ArrisTR69AcsUrl_Type())
arrisTR69AcsUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsUrl.setStatus(_A)
class _ArrisTR69AcsUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69AcsUserName_Type.__name__=_C
_ArrisTR69AcsUserName_Object=MibScalar
arrisTR69AcsUserName=_ArrisTR69AcsUserName_Object((1,3,6,1,4,1,4115,1,3,7,1,1,3),_ArrisTR69AcsUserName_Type())
arrisTR69AcsUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsUserName.setStatus(_A)
class _ArrisTR69AcsPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69AcsPassword_Type.__name__=_C
_ArrisTR69AcsPassword_Object=MibScalar
arrisTR69AcsPassword=_ArrisTR69AcsPassword_Object((1,3,6,1,4,1,4115,1,3,7,1,1,4),_ArrisTR69AcsPassword_Type())
arrisTR69AcsPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsPassword.setStatus(_A)
class _ArrisTR69PeriodicInformEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ArrisTR69PeriodicInformEnable_Type.__name__=_D
_ArrisTR69PeriodicInformEnable_Object=MibScalar
arrisTR69PeriodicInformEnable=_ArrisTR69PeriodicInformEnable_Object((1,3,6,1,4,1,4115,1,3,7,1,1,5),_ArrisTR69PeriodicInformEnable_Type())
arrisTR69PeriodicInformEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69PeriodicInformEnable.setStatus(_A)
_ArrisTR69PeriodicInformInterval_Type=Unsigned32
_ArrisTR69PeriodicInformInterval_Object=MibScalar
arrisTR69PeriodicInformInterval=_ArrisTR69PeriodicInformInterval_Object((1,3,6,1,4,1,4115,1,3,7,1,1,6),_ArrisTR69PeriodicInformInterval_Type())
arrisTR69PeriodicInformInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69PeriodicInformInterval.setStatus(_A)
class _ArrisTR69PeriodicInformTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_ArrisTR69PeriodicInformTime_Type.__name__=_G
_ArrisTR69PeriodicInformTime_Object=MibScalar
arrisTR69PeriodicInformTime=_ArrisTR69PeriodicInformTime_Object((1,3,6,1,4,1,4115,1,3,7,1,1,7),_ArrisTR69PeriodicInformTime_Type())
arrisTR69PeriodicInformTime.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69PeriodicInformTime.setStatus(_A)
class _ArrisTR69ParameterKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArrisTR69ParameterKey_Type.__name__=_C
_ArrisTR69ParameterKey_Object=MibScalar
arrisTR69ParameterKey=_ArrisTR69ParameterKey_Object((1,3,6,1,4,1,4115,1,3,7,1,1,8),_ArrisTR69ParameterKey_Type())
arrisTR69ParameterKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ParameterKey.setStatus(_A)
class _ArrisTR69ConnectionRequestUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69ConnectionRequestUrl_Type.__name__=_C
_ArrisTR69ConnectionRequestUrl_Object=MibScalar
arrisTR69ConnectionRequestUrl=_ArrisTR69ConnectionRequestUrl_Object((1,3,6,1,4,1,4115,1,3,7,1,1,9),_ArrisTR69ConnectionRequestUrl_Type())
arrisTR69ConnectionRequestUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ConnectionRequestUrl.setStatus(_A)
class _ArrisTR69ConnectionRequestUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69ConnectionRequestUserName_Type.__name__=_C
_ArrisTR69ConnectionRequestUserName_Object=MibScalar
arrisTR69ConnectionRequestUserName=_ArrisTR69ConnectionRequestUserName_Object((1,3,6,1,4,1,4115,1,3,7,1,1,10),_ArrisTR69ConnectionRequestUserName_Type())
arrisTR69ConnectionRequestUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ConnectionRequestUserName.setStatus(_A)
class _ArrisTR69ConnectionRequestPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69ConnectionRequestPassword_Type.__name__=_C
_ArrisTR69ConnectionRequestPassword_Object=MibScalar
arrisTR69ConnectionRequestPassword=_ArrisTR69ConnectionRequestPassword_Object((1,3,6,1,4,1,4115,1,3,7,1,1,11),_ArrisTR69ConnectionRequestPassword_Type())
arrisTR69ConnectionRequestPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ConnectionRequestPassword.setStatus(_A)
class _ArrisTR69TransportInterface_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gwInterface',1),('cmInterface',2)))
_ArrisTR69TransportInterface_Type.__name__=_D
_ArrisTR69TransportInterface_Object=MibScalar
arrisTR69TransportInterface=_ArrisTR69TransportInterface_Object((1,3,6,1,4,1,4115,1,3,7,1,1,12),_ArrisTR69TransportInterface_Type())
arrisTR69TransportInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69TransportInterface.setStatus(_A)
_ArrisTR69CwmpPort_Type=Unsigned32
_ArrisTR69CwmpPort_Object=MibScalar
arrisTR69CwmpPort=_ArrisTR69CwmpPort_Object((1,3,6,1,4,1,4115,1,3,7,1,1,13),_ArrisTR69CwmpPort_Type())
arrisTR69CwmpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69CwmpPort.setStatus(_A)
class _ArrisTR69NameSpacePriOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('default',1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_ArrisTR69NameSpacePriOverride_Type.__name__=_D
_ArrisTR69NameSpacePriOverride_Object=MibScalar
arrisTR69NameSpacePriOverride=_ArrisTR69NameSpacePriOverride_Object((1,3,6,1,4,1,4115,1,3,7,1,1,14),_ArrisTR69NameSpacePriOverride_Type())
arrisTR69NameSpacePriOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69NameSpacePriOverride.setStatus(_A)
class _ArrisTR69NameSpaceSecOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('null',1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_ArrisTR69NameSpaceSecOverride_Type.__name__=_D
_ArrisTR69NameSpaceSecOverride_Object=MibScalar
arrisTR69NameSpaceSecOverride=_ArrisTR69NameSpaceSecOverride_Object((1,3,6,1,4,1,4115,1,3,7,1,1,15),_ArrisTR69NameSpaceSecOverride_Type())
arrisTR69NameSpaceSecOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69NameSpaceSecOverride.setStatus(_A)
class _ArrisTR69DataModelSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tr098',0),('tr181',1)))
_ArrisTR69DataModelSelect_Type.__name__=_D
_ArrisTR69DataModelSelect_Object=MibScalar
arrisTR69DataModelSelect=_ArrisTR69DataModelSelect_Object((1,3,6,1,4,1,4115,1,3,7,1,1,16),_ArrisTR69DataModelSelect_Type())
arrisTR69DataModelSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69DataModelSelect.setStatus(_A)
_ArrisTR69RetryMinimumWaitInterval_Type=Unsigned32
_ArrisTR69RetryMinimumWaitInterval_Object=MibScalar
arrisTR69RetryMinimumWaitInterval=_ArrisTR69RetryMinimumWaitInterval_Object((1,3,6,1,4,1,4115,1,3,7,1,1,17),_ArrisTR69RetryMinimumWaitInterval_Type())
arrisTR69RetryMinimumWaitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69RetryMinimumWaitInterval.setStatus(_A)
_ArrisTR69RetryIntervalMultiplier_Type=Unsigned32
_ArrisTR69RetryIntervalMultiplier_Object=MibScalar
arrisTR69RetryIntervalMultiplier=_ArrisTR69RetryIntervalMultiplier_Object((1,3,6,1,4,1,4115,1,3,7,1,1,18),_ArrisTR69RetryIntervalMultiplier_Type())
arrisTR69RetryIntervalMultiplier.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69RetryIntervalMultiplier.setStatus(_A)
class _ArrisTR69ConnectRequestRealm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisTR69ConnectRequestRealm_Type.__name__=_G
_ArrisTR69ConnectRequestRealm_Object=MibScalar
arrisTR69ConnectRequestRealm=_ArrisTR69ConnectRequestRealm_Object((1,3,6,1,4,1,4115,1,3,7,1,1,19),_ArrisTR69ConnectRequestRealm_Type())
arrisTR69ConnectRequestRealm.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ConnectRequestRealm.setStatus(_A)
class _ArrisTR69AcsPwdAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hmac-sha1',1),('hmac-sha256',2)))
_ArrisTR69AcsPwdAlgorithm_Type.__name__=_D
_ArrisTR69AcsPwdAlgorithm_Object=MibScalar
arrisTR69AcsPwdAlgorithm=_ArrisTR69AcsPwdAlgorithm_Object((1,3,6,1,4,1,4115,1,3,7,1,1,20),_ArrisTR69AcsPwdAlgorithm_Type())
arrisTR69AcsPwdAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsPwdAlgorithm.setStatus(_A)
class _ArrisTR69AcsPwdAlgorithmText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisTR69AcsPwdAlgorithmText_Type.__name__=_G
_ArrisTR69AcsPwdAlgorithmText_Object=MibScalar
arrisTR69AcsPwdAlgorithmText=_ArrisTR69AcsPwdAlgorithmText_Object((1,3,6,1,4,1,4115,1,3,7,1,1,21),_ArrisTR69AcsPwdAlgorithmText_Type())
arrisTR69AcsPwdAlgorithmText.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsPwdAlgorithmText.setStatus(_A)
class _ArrisTR69AcsPwdAlgorithmKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArrisTR69AcsPwdAlgorithmKey_Type.__name__=_G
_ArrisTR69AcsPwdAlgorithmKey_Object=MibScalar
arrisTR69AcsPwdAlgorithmKey=_ArrisTR69AcsPwdAlgorithmKey_Object((1,3,6,1,4,1,4115,1,3,7,1,1,22),_ArrisTR69AcsPwdAlgorithmKey_Type())
arrisTR69AcsPwdAlgorithmKey.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsPwdAlgorithmKey.setStatus(_A)
_ArrisTR69TransportIPVersion_Type=InetVersion
_ArrisTR69TransportIPVersion_Object=MibScalar
arrisTR69TransportIPVersion=_ArrisTR69TransportIPVersion_Object((1,3,6,1,4,1,4115,1,3,7,1,1,23),_ArrisTR69TransportIPVersion_Type())
arrisTR69TransportIPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69TransportIPVersion.setStatus(_A)
class _ArrisTR69ProvisioningCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR69ProvisioningCode_Type.__name__=_C
_ArrisTR69ProvisioningCode_Object=MibScalar
arrisTR69ProvisioningCode=_ArrisTR69ProvisioningCode_Object((1,3,6,1,4,1,4115,1,3,7,1,1,24),_ArrisTR69ProvisioningCode_Type())
arrisTR69ProvisioningCode.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ProvisioningCode.setStatus(_A)
_ArrisTR69DefaultActiveNotificationThrottle_Type=Unsigned32
_ArrisTR69DefaultActiveNotificationThrottle_Object=MibScalar
arrisTR69DefaultActiveNotificationThrottle=_ArrisTR69DefaultActiveNotificationThrottle_Object((1,3,6,1,4,1,4115,1,3,7,1,1,25),_ArrisTR69DefaultActiveNotificationThrottle_Type())
arrisTR69DefaultActiveNotificationThrottle.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69DefaultActiveNotificationThrottle.setStatus(_A)
class _ArrisTR69DataModelSelectIgnoreNonPuma5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ArrisTR69DataModelSelectIgnoreNonPuma5_Type.__name__=_D
_ArrisTR69DataModelSelectIgnoreNonPuma5_Object=MibScalar
arrisTR69DataModelSelectIgnoreNonPuma5=_ArrisTR69DataModelSelectIgnoreNonPuma5_Object((1,3,6,1,4,1,4115,1,3,7,1,1,26),_ArrisTR69DataModelSelectIgnoreNonPuma5_Type())
arrisTR69DataModelSelectIgnoreNonPuma5.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69DataModelSelectIgnoreNonPuma5.setStatus(_A)
class _ArrisTR69AcsDiscoveryDhcpOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('option60',1),('option124',2)))
_ArrisTR69AcsDiscoveryDhcpOption_Type.__name__=_D
_ArrisTR69AcsDiscoveryDhcpOption_Object=MibScalar
arrisTR69AcsDiscoveryDhcpOption=_ArrisTR69AcsDiscoveryDhcpOption_Object((1,3,6,1,4,1,4115,1,3,7,1,1,27),_ArrisTR69AcsDiscoveryDhcpOption_Type())
arrisTR69AcsDiscoveryDhcpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69AcsDiscoveryDhcpOption.setStatus(_A)
_ArrisTR69Setup_ObjectIdentity=ObjectIdentity
arrisTR69Setup=_ArrisTR69Setup_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,1,2))
class _ArrisTR69PersistEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_ArrisTR69PersistEnable_Type.__name__=_D
_ArrisTR69PersistEnable_Object=MibScalar
arrisTR69PersistEnable=_ArrisTR69PersistEnable_Object((1,3,6,1,4,1,4115,1,3,7,1,2,1),_ArrisTR69PersistEnable_Type())
arrisTR69PersistEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69PersistEnable.setStatus(_A)
_ArrisTR69Authentication_ObjectIdentity=ObjectIdentity
arrisTR69Authentication=_ArrisTR69Authentication_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,1,3))
class _ArrisTR69ValidateManagementServerCertificate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ArrisTR69ValidateManagementServerCertificate_Type.__name__=_D
_ArrisTR69ValidateManagementServerCertificate_Object=MibScalar
arrisTR69ValidateManagementServerCertificate=_ArrisTR69ValidateManagementServerCertificate_Object((1,3,6,1,4,1,4115,1,3,7,1,3,1),_ArrisTR69ValidateManagementServerCertificate_Type())
arrisTR69ValidateManagementServerCertificate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ValidateManagementServerCertificate.setStatus(_A)
class _ArrisTR69ValidateDownloadServerCertificate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ArrisTR69ValidateDownloadServerCertificate_Type.__name__=_D
_ArrisTR69ValidateDownloadServerCertificate_Object=MibScalar
arrisTR69ValidateDownloadServerCertificate=_ArrisTR69ValidateDownloadServerCertificate_Object((1,3,6,1,4,1,4115,1,3,7,1,3,2),_ArrisTR69ValidateDownloadServerCertificate_Type())
arrisTR69ValidateDownloadServerCertificate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69ValidateDownloadServerCertificate.setStatus(_A)
_ArrisTR69RootCertificateNumberOfEntries_Type=Unsigned32
_ArrisTR69RootCertificateNumberOfEntries_Object=MibScalar
arrisTR69RootCertificateNumberOfEntries=_ArrisTR69RootCertificateNumberOfEntries_Object((1,3,6,1,4,1,4115,1,3,7,1,3,3),_ArrisTR69RootCertificateNumberOfEntries_Type())
arrisTR69RootCertificateNumberOfEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR69RootCertificateNumberOfEntries.setStatus(_A)
_ArrisTR69RootCertificateTable_Object=MibTable
arrisTR69RootCertificateTable=_ArrisTR69RootCertificateTable_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4))
if mibBuilder.loadTexts:arrisTR69RootCertificateTable.setStatus(_A)
_ArrisTR69RootCertificateEntry_Object=MibTableRow
arrisTR69RootCertificateEntry=_ArrisTR69RootCertificateEntry_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1))
arrisTR69RootCertificateEntry.setIndexNames((0,_M,_R))
if mibBuilder.loadTexts:arrisTR69RootCertificateEntry.setStatus(_A)
_ArrisTR69RootCertIndex_Type=Unsigned32
_ArrisTR69RootCertIndex_Object=MibTableColumn
arrisTR69RootCertIndex=_ArrisTR69RootCertIndex_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,1),_ArrisTR69RootCertIndex_Type())
arrisTR69RootCertIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:arrisTR69RootCertIndex.setStatus(_A)
class _ArrisTR69RootCertEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ArrisTR69RootCertEnabled_Type.__name__=_D
_ArrisTR69RootCertEnabled_Object=MibTableColumn
arrisTR69RootCertEnabled=_ArrisTR69RootCertEnabled_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,2),_ArrisTR69RootCertEnabled_Type())
arrisTR69RootCertEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69RootCertEnabled.setStatus(_A)
class _ArrisTR69RootCertCertificate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4096))
_ArrisTR69RootCertCertificate_Type.__name__=_C
_ArrisTR69RootCertCertificate_Object=MibTableColumn
arrisTR69RootCertCertificate=_ArrisTR69RootCertCertificate_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,3),_ArrisTR69RootCertCertificate_Type())
arrisTR69RootCertCertificate.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69RootCertCertificate.setStatus(_A)
_ArrisTR69RootCertLastModif_Type=TimeStamp
_ArrisTR69RootCertLastModif_Object=MibTableColumn
arrisTR69RootCertLastModif=_ArrisTR69RootCertLastModif_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,4),_ArrisTR69RootCertLastModif_Type())
arrisTR69RootCertLastModif.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertLastModif.setStatus(_A)
class _ArrisTR69RootCertSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArrisTR69RootCertSerialNumber_Type.__name__=_G
_ArrisTR69RootCertSerialNumber_Object=MibTableColumn
arrisTR69RootCertSerialNumber=_ArrisTR69RootCertSerialNumber_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,5),_ArrisTR69RootCertSerialNumber_Type())
arrisTR69RootCertSerialNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertSerialNumber.setStatus(_A)
class _ArrisTR69RootCertIssuer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ArrisTR69RootCertIssuer_Type.__name__=_C
_ArrisTR69RootCertIssuer_Object=MibTableColumn
arrisTR69RootCertIssuer=_ArrisTR69RootCertIssuer_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,6),_ArrisTR69RootCertIssuer_Type())
arrisTR69RootCertIssuer.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertIssuer.setStatus(_A)
class _ArrisTR69RootCertNotBefore_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ArrisTR69RootCertNotBefore_Type.__name__=_C
_ArrisTR69RootCertNotBefore_Object=MibTableColumn
arrisTR69RootCertNotBefore=_ArrisTR69RootCertNotBefore_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,7),_ArrisTR69RootCertNotBefore_Type())
arrisTR69RootCertNotBefore.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertNotBefore.setStatus(_A)
class _ArrisTR69RootCertNotAfter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ArrisTR69RootCertNotAfter_Type.__name__=_C
_ArrisTR69RootCertNotAfter_Object=MibTableColumn
arrisTR69RootCertNotAfter=_ArrisTR69RootCertNotAfter_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,8),_ArrisTR69RootCertNotAfter_Type())
arrisTR69RootCertNotAfter.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertNotAfter.setStatus(_A)
class _ArrisTR69RootCertSubject_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ArrisTR69RootCertSubject_Type.__name__=_C
_ArrisTR69RootCertSubject_Object=MibTableColumn
arrisTR69RootCertSubject=_ArrisTR69RootCertSubject_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,9),_ArrisTR69RootCertSubject_Type())
arrisTR69RootCertSubject.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertSubject.setStatus(_A)
class _ArrisTR69RootCertSubjectAlt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ArrisTR69RootCertSubjectAlt_Type.__name__=_C
_ArrisTR69RootCertSubjectAlt_Object=MibTableColumn
arrisTR69RootCertSubjectAlt=_ArrisTR69RootCertSubjectAlt_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,10),_ArrisTR69RootCertSubjectAlt_Type())
arrisTR69RootCertSubjectAlt.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertSubjectAlt.setStatus(_A)
class _ArrisTR69RootCertSignatureAlgorithm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ArrisTR69RootCertSignatureAlgorithm_Type.__name__=_C
_ArrisTR69RootCertSignatureAlgorithm_Object=MibTableColumn
arrisTR69RootCertSignatureAlgorithm=_ArrisTR69RootCertSignatureAlgorithm_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,11),_ArrisTR69RootCertSignatureAlgorithm_Type())
arrisTR69RootCertSignatureAlgorithm.setMaxAccess(_F)
if mibBuilder.loadTexts:arrisTR69RootCertSignatureAlgorithm.setStatus(_A)
_ArrisTR69RootCertObjInstance_Type=Unsigned32
_ArrisTR69RootCertObjInstance_Object=MibTableColumn
arrisTR69RootCertObjInstance=_ArrisTR69RootCertObjInstance_Object((1,3,6,1,4,1,4115,1,3,7,1,3,4,1,12),_ArrisTR69RootCertObjInstance_Type())
arrisTR69RootCertObjInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:arrisTR69RootCertObjInstance.setStatus(_A)
_ArrisTR181MibObjects_ObjectIdentity=ObjectIdentity
arrisTR181MibObjects=_ArrisTR181MibObjects_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,2))
_ArrisTR181DeviceInfo_ObjectIdentity=ObjectIdentity
arrisTR181DeviceInfo=_ArrisTR181DeviceInfo_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,2,1))
_ArrisTR181DeviceInfoFirstUseDate_Type=DateAndTime
_ArrisTR181DeviceInfoFirstUseDate_Object=MibScalar
arrisTR181DeviceInfoFirstUseDate=_ArrisTR181DeviceInfoFirstUseDate_Object((1,3,6,1,4,1,4115,1,3,7,2,1,1),_ArrisTR181DeviceInfoFirstUseDate_Type())
arrisTR181DeviceInfoFirstUseDate.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoFirstUseDate.setStatus(_A)
_ArrisTR181DeviceInfoMemoryStatus_ObjectIdentity=ObjectIdentity
arrisTR181DeviceInfoMemoryStatus=_ArrisTR181DeviceInfoMemoryStatus_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,2,1,2))
_ArrisTR181DeviceInfoMemoryStatusTotal_Type=Unsigned32
_ArrisTR181DeviceInfoMemoryStatusTotal_Object=MibScalar
arrisTR181DeviceInfoMemoryStatusTotal=_ArrisTR181DeviceInfoMemoryStatusTotal_Object((1,3,6,1,4,1,4115,1,3,7,2,1,2,1),_ArrisTR181DeviceInfoMemoryStatusTotal_Type())
arrisTR181DeviceInfoMemoryStatusTotal.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoMemoryStatusTotal.setStatus(_A)
_ArrisTR181DeviceInfoMemoryStatusFree_Type=Unsigned32
_ArrisTR181DeviceInfoMemoryStatusFree_Object=MibScalar
arrisTR181DeviceInfoMemoryStatusFree=_ArrisTR181DeviceInfoMemoryStatusFree_Object((1,3,6,1,4,1,4115,1,3,7,2,1,2,2),_ArrisTR181DeviceInfoMemoryStatusFree_Type())
arrisTR181DeviceInfoMemoryStatusFree.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoMemoryStatusFree.setStatus(_A)
_ArrisTR181DeviceInfoProcessStatus_ObjectIdentity=ObjectIdentity
arrisTR181DeviceInfoProcessStatus=_ArrisTR181DeviceInfoProcessStatus_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,2,1,3))
class _ArrisTR181DeviceInfoProcessStatusCPUUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ArrisTR181DeviceInfoProcessStatusCPUUsage_Type.__name__=_J
_ArrisTR181DeviceInfoProcessStatusCPUUsage_Object=MibScalar
arrisTR181DeviceInfoProcessStatusCPUUsage=_ArrisTR181DeviceInfoProcessStatusCPUUsage_Object((1,3,6,1,4,1,4115,1,3,7,2,1,3,1),_ArrisTR181DeviceInfoProcessStatusCPUUsage_Type())
arrisTR181DeviceInfoProcessStatusCPUUsage.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusCPUUsage.setStatus(_A)
_ArrisTR181DeviceInfoProcessStatusProcess_ObjectIdentity=ObjectIdentity
arrisTR181DeviceInfoProcessStatusProcess=_ArrisTR181DeviceInfoProcessStatusProcess_ObjectIdentity((1,3,6,1,4,1,4115,1,3,7,2,1,4))
_ArrisTR181DeviceInfoProcessStatusProcessTable_Object=MibTable
arrisTR181DeviceInfoProcessStatusProcessTable=_ArrisTR181DeviceInfoProcessStatusProcessTable_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1))
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessTable.setStatus(_A)
_ArrisTR181DeviceInfoProcessStatusProcessEntry_Object=MibTableRow
arrisTR181DeviceInfoProcessStatusProcessEntry=_ArrisTR181DeviceInfoProcessStatusProcessEntry_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1))
arrisTR181DeviceInfoProcessStatusProcessEntry.setIndexNames((0,_M,_T))
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessEntry.setStatus(_A)
class _ArrisTR181DeviceInfoProcessStatusProcessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,150))
_ArrisTR181DeviceInfoProcessStatusProcessIndex_Type.__name__=_D
_ArrisTR181DeviceInfoProcessStatusProcessIndex_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessIndex=_ArrisTR181DeviceInfoProcessStatusProcessIndex_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,1),_ArrisTR181DeviceInfoProcessStatusProcessIndex_Type())
arrisTR181DeviceInfoProcessStatusProcessIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessIndex.setStatus(_A)
_ArrisTR181DeviceInfoProcessStatusProcessPID_Type=Unsigned32
_ArrisTR181DeviceInfoProcessStatusProcessPID_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessPID=_ArrisTR181DeviceInfoProcessStatusProcessPID_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,2),_ArrisTR181DeviceInfoProcessStatusProcessPID_Type())
arrisTR181DeviceInfoProcessStatusProcessPID.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessPID.setStatus(_A)
class _ArrisTR181DeviceInfoProcessStatusProcessCommand_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ArrisTR181DeviceInfoProcessStatusProcessCommand_Type.__name__=_C
_ArrisTR181DeviceInfoProcessStatusProcessCommand_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessCommand=_ArrisTR181DeviceInfoProcessStatusProcessCommand_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,3),_ArrisTR181DeviceInfoProcessStatusProcessCommand_Type())
arrisTR181DeviceInfoProcessStatusProcessCommand.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessCommand.setStatus(_A)
_ArrisTR181DeviceInfoProcessStatusProcessSize_Type=Unsigned32
_ArrisTR181DeviceInfoProcessStatusProcessSize_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessSize=_ArrisTR181DeviceInfoProcessStatusProcessSize_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,4),_ArrisTR181DeviceInfoProcessStatusProcessSize_Type())
arrisTR181DeviceInfoProcessStatusProcessSize.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessSize.setStatus(_A)
class _ArrisTR181DeviceInfoProcessStatusProcessPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_ArrisTR181DeviceInfoProcessStatusProcessPriority_Type.__name__=_J
_ArrisTR181DeviceInfoProcessStatusProcessPriority_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessPriority=_ArrisTR181DeviceInfoProcessStatusProcessPriority_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,5),_ArrisTR181DeviceInfoProcessStatusProcessPriority_Type())
arrisTR181DeviceInfoProcessStatusProcessPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessPriority.setStatus(_A)
_ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Type=Unsigned32
_ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessCPUTime=_ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,6),_ArrisTR181DeviceInfoProcessStatusProcessCPUTime_Type())
arrisTR181DeviceInfoProcessStatusProcessCPUTime.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessCPUTime.setStatus(_A)
class _ArrisTR181DeviceInfoProcessStatusProcessState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ArrisTR181DeviceInfoProcessStatusProcessState_Type.__name__=_C
_ArrisTR181DeviceInfoProcessStatusProcessState_Object=MibTableColumn
arrisTR181DeviceInfoProcessStatusProcessState=_ArrisTR181DeviceInfoProcessStatusProcessState_Object((1,3,6,1,4,1,4115,1,3,7,2,1,4,1,1,7),_ArrisTR181DeviceInfoProcessStatusProcessState_Type())
arrisTR181DeviceInfoProcessStatusProcessState.setMaxAccess(_E)
if mibBuilder.loadTexts:arrisTR181DeviceInfoProcessStatusProcessState.setStatus(_A)
mibBuilder.exportSymbols(_M,**{'arrisTR69Mib':arrisTR69Mib,'arrisTR69MibObjects':arrisTR69MibObjects,'arrisTR69Base':arrisTR69Base,'arrisTR69EnableCWMP':arrisTR69EnableCWMP,'arrisTR69AcsUrl':arrisTR69AcsUrl,'arrisTR69AcsUserName':arrisTR69AcsUserName,'arrisTR69AcsPassword':arrisTR69AcsPassword,'arrisTR69PeriodicInformEnable':arrisTR69PeriodicInformEnable,'arrisTR69PeriodicInformInterval':arrisTR69PeriodicInformInterval,'arrisTR69PeriodicInformTime':arrisTR69PeriodicInformTime,'arrisTR69ParameterKey':arrisTR69ParameterKey,'arrisTR69ConnectionRequestUrl':arrisTR69ConnectionRequestUrl,'arrisTR69ConnectionRequestUserName':arrisTR69ConnectionRequestUserName,'arrisTR69ConnectionRequestPassword':arrisTR69ConnectionRequestPassword,'arrisTR69TransportInterface':arrisTR69TransportInterface,'arrisTR69CwmpPort':arrisTR69CwmpPort,'arrisTR69NameSpacePriOverride':arrisTR69NameSpacePriOverride,'arrisTR69NameSpaceSecOverride':arrisTR69NameSpaceSecOverride,'arrisTR69DataModelSelect':arrisTR69DataModelSelect,'arrisTR69RetryMinimumWaitInterval':arrisTR69RetryMinimumWaitInterval,'arrisTR69RetryIntervalMultiplier':arrisTR69RetryIntervalMultiplier,'arrisTR69ConnectRequestRealm':arrisTR69ConnectRequestRealm,'arrisTR69AcsPwdAlgorithm':arrisTR69AcsPwdAlgorithm,'arrisTR69AcsPwdAlgorithmText':arrisTR69AcsPwdAlgorithmText,'arrisTR69AcsPwdAlgorithmKey':arrisTR69AcsPwdAlgorithmKey,'arrisTR69TransportIPVersion':arrisTR69TransportIPVersion,'arrisTR69ProvisioningCode':arrisTR69ProvisioningCode,'arrisTR69DefaultActiveNotificationThrottle':arrisTR69DefaultActiveNotificationThrottle,'arrisTR69DataModelSelectIgnoreNonPuma5':arrisTR69DataModelSelectIgnoreNonPuma5,'arrisTR69AcsDiscoveryDhcpOption':arrisTR69AcsDiscoveryDhcpOption,'arrisTR69Setup':arrisTR69Setup,'arrisTR69PersistEnable':arrisTR69PersistEnable,'arrisTR69Authentication':arrisTR69Authentication,'arrisTR69ValidateManagementServerCertificate':arrisTR69ValidateManagementServerCertificate,'arrisTR69ValidateDownloadServerCertificate':arrisTR69ValidateDownloadServerCertificate,'arrisTR69RootCertificateNumberOfEntries':arrisTR69RootCertificateNumberOfEntries,'arrisTR69RootCertificateTable':arrisTR69RootCertificateTable,'arrisTR69RootCertificateEntry':arrisTR69RootCertificateEntry,_R:arrisTR69RootCertIndex,'arrisTR69RootCertEnabled':arrisTR69RootCertEnabled,'arrisTR69RootCertCertificate':arrisTR69RootCertCertificate,'arrisTR69RootCertLastModif':arrisTR69RootCertLastModif,'arrisTR69RootCertSerialNumber':arrisTR69RootCertSerialNumber,'arrisTR69RootCertIssuer':arrisTR69RootCertIssuer,'arrisTR69RootCertNotBefore':arrisTR69RootCertNotBefore,'arrisTR69RootCertNotAfter':arrisTR69RootCertNotAfter,'arrisTR69RootCertSubject':arrisTR69RootCertSubject,'arrisTR69RootCertSubjectAlt':arrisTR69RootCertSubjectAlt,'arrisTR69RootCertSignatureAlgorithm':arrisTR69RootCertSignatureAlgorithm,'arrisTR69RootCertObjInstance':arrisTR69RootCertObjInstance,'arrisTR181MibObjects':arrisTR181MibObjects,'arrisTR181DeviceInfo':arrisTR181DeviceInfo,'arrisTR181DeviceInfoFirstUseDate':arrisTR181DeviceInfoFirstUseDate,'arrisTR181DeviceInfoMemoryStatus':arrisTR181DeviceInfoMemoryStatus,'arrisTR181DeviceInfoMemoryStatusTotal':arrisTR181DeviceInfoMemoryStatusTotal,'arrisTR181DeviceInfoMemoryStatusFree':arrisTR181DeviceInfoMemoryStatusFree,'arrisTR181DeviceInfoProcessStatus':arrisTR181DeviceInfoProcessStatus,'arrisTR181DeviceInfoProcessStatusCPUUsage':arrisTR181DeviceInfoProcessStatusCPUUsage,'arrisTR181DeviceInfoProcessStatusProcess':arrisTR181DeviceInfoProcessStatusProcess,'arrisTR181DeviceInfoProcessStatusProcessTable':arrisTR181DeviceInfoProcessStatusProcessTable,'arrisTR181DeviceInfoProcessStatusProcessEntry':arrisTR181DeviceInfoProcessStatusProcessEntry,_T:arrisTR181DeviceInfoProcessStatusProcessIndex,'arrisTR181DeviceInfoProcessStatusProcessPID':arrisTR181DeviceInfoProcessStatusProcessPID,'arrisTR181DeviceInfoProcessStatusProcessCommand':arrisTR181DeviceInfoProcessStatusProcessCommand,'arrisTR181DeviceInfoProcessStatusProcessSize':arrisTR181DeviceInfoProcessStatusProcessSize,'arrisTR181DeviceInfoProcessStatusProcessPriority':arrisTR181DeviceInfoProcessStatusProcessPriority,'arrisTR181DeviceInfoProcessStatusProcessCPUTime':arrisTR181DeviceInfoProcessStatusProcessCPUTime,'arrisTR181DeviceInfoProcessStatusProcessState':arrisTR181DeviceInfoProcessStatusProcessState})