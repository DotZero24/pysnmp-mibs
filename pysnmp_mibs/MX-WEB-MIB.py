_E='MxIpPort'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap','MxEnableState','MxIpAddress','MxIpHostName',_E,'MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
webMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1200))
_WebMIBObjects_ObjectIdentity=ObjectIdentity
webMIBObjects=_WebMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1200,1))
_ServerGroup_ObjectIdentity=ObjectIdentity
serverGroup=_ServerGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,100))
class _HttpMode_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('secure',100),('unsecure',200),('both',300)))
_HttpMode_Type.__name__=_B
_HttpMode_Object=MibScalar
httpMode=_HttpMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,100,50),_HttpMode_Type())
httpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:httpMode.setStatus(_A)
class _ServerPort_Type(MxIpPort):defaultValue=80
_ServerPort_Type.__name__=_E
_ServerPort_Object=MibScalar
serverPort=_ServerPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,100,100),_ServerPort_Type())
serverPort.setMaxAccess(_C)
if mibBuilder.loadTexts:serverPort.setStatus(_A)
class _SecureServerPort_Type(MxIpPort):defaultValue=443
_SecureServerPort_Type.__name__=_E
_SecureServerPort_Object=MibScalar
secureServerPort=_SecureServerPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,100,200),_SecureServerPort_Type())
secureServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:secureServerPort.setStatus(_A)
class _HttpsCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_HttpsCipherSuite_Type.__name__=_B
_HttpsCipherSuite_Object=MibScalar
httpsCipherSuite=_HttpsCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,100,300),_HttpsCipherSuite_Type())
httpsCipherSuite.setMaxAccess(_C)
if mibBuilder.loadTexts:httpsCipherSuite.setStatus(_A)
class _TlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),('tLSv1-1',300),('tLSv1-2',400)))
_TlsVersion_Type.__name__=_B
_TlsVersion_Object=MibScalar
tlsVersion=_TlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,100,400),_TlsVersion_Type())
tlsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tlsVersion.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,10000))
_StatsRequest_Type=Unsigned32
_StatsRequest_Object=MibScalar
statsRequest=_StatsRequest_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,10000,100),_StatsRequest_Type())
statsRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:statsRequest.setStatus(_A)
_StatsRedirect_Type=Unsigned32
_StatsRedirect_Object=MibScalar
statsRedirect=_StatsRedirect_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,10000,200),_StatsRedirect_Type())
statsRedirect.setMaxAccess(_D)
if mibBuilder.loadTexts:statsRedirect.setStatus(_A)
_StatsError_Type=Unsigned32
_StatsError_Object=MibScalar
statsError=_StatsError_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,10000,300),_StatsError_Type())
statsError.setMaxAccess(_D)
if mibBuilder.loadTexts:statsError.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1200,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols('MX-WEB-MIB',**{'webMIB':webMIB,'webMIBObjects':webMIBObjects,'serverGroup':serverGroup,'httpMode':httpMode,'serverPort':serverPort,'secureServerPort':secureServerPort,'httpsCipherSuite':httpsCipherSuite,'tlsVersion':tlsVersion,'statisticsGroup':statisticsGroup,'statsRequest':statsRequest,'statsRedirect':statsRedirect,'statsError':statsError,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})