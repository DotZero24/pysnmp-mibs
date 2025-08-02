_E='MxIpHostNamePort'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap','MxEnableState','MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_E,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cdrMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4200))
_CdrMIBObjects_ObjectIdentity=ObjectIdentity
cdrMIBObjects=_CdrMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4200,1))
_SyslogGroup_ObjectIdentity=ObjectIdentity
syslogGroup=_SyslogGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,400))
class _SyslogRemoteHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_SyslogRemoteHost_Type.__name__=_E
_SyslogRemoteHost_Object=MibScalar
syslogRemoteHost=_SyslogRemoteHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,400,100),_SyslogRemoteHost_Type())
syslogRemoteHost.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogRemoteHost.setStatus(_A)
class _SyslogFormat_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SyslogFormat_Type.__name__=_D
_SyslogFormat_Object=MibScalar
syslogFormat=_SyslogFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,400,200),_SyslogFormat_Type())
syslogFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogFormat.setStatus(_A)
class _SyslogFacility_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800)));namedValues=NamedValues(*(('local0',100),('local1',200),('local2',300),('local3',400),('local4',500),('local5',600),('local6',700),('local7',800)))
_SyslogFacility_Type.__name__=_B
_SyslogFacility_Object=MibScalar
syslogFacility=_SyslogFacility_Object((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,400,300),_SyslogFacility_Type())
syslogFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogFacility.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4200,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess('read-only')
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols('MX-CDR-MIB',**{'cdrMIB':cdrMIB,'cdrMIBObjects':cdrMIBObjects,'syslogGroup':syslogGroup,'syslogRemoteHost':syslogRemoteHost,'syslogFormat':syslogFormat,'syslogFacility':syslogFacility,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})