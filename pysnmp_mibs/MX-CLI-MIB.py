_G='Unsigned32'
_F='OctetString'
_E='MxIpPort'
_D='MxEnableState'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_D,'MxIpAddress','MxIpHostName',_E,'MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cliMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2700))
_CliMIBObjects_ObjectIdentity=ObjectIdentity
cliMIBObjects=_CliMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2700,1))
class _InactivityTimeOut_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,90))
_InactivityTimeOut_Type.__name__=_G
_InactivityTimeOut_Object=MibScalar
inactivityTimeOut=_InactivityTimeOut_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,100),_InactivityTimeOut_Type())
inactivityTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:inactivityTimeOut.setStatus(_A)
class _WelcomeMessage_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_WelcomeMessage_Type.__name__=_F
_WelcomeMessage_Object=MibScalar
welcomeMessage=_WelcomeMessage_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,200),_WelcomeMessage_Type())
welcomeMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:welcomeMessage.setStatus(_A)
_TelnetGroup_ObjectIdentity=ObjectIdentity
telnetGroup=_TelnetGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1000))
class _EnableTelnet_Type(MxEnableState):defaultValue=0
_EnableTelnet_Type.__name__=_D
_EnableTelnet_Object=MibScalar
enableTelnet=_EnableTelnet_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1000,100),_EnableTelnet_Type())
enableTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:enableTelnet.setStatus(_A)
class _TelnetPort_Type(MxIpPort):defaultValue=23
_TelnetPort_Type.__name__=_E
_TelnetPort_Object=MibScalar
telnetPort=_TelnetPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1000,200),_TelnetPort_Type())
telnetPort.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetPort.setStatus(_A)
_SshGroup_ObjectIdentity=ObjectIdentity
sshGroup=_SshGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1100))
class _EnableSsh_Type(MxEnableState):defaultValue=1
_EnableSsh_Type.__name__=_D
_EnableSsh_Object=MibScalar
enableSsh=_EnableSsh_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1100,100),_EnableSsh_Type())
enableSsh.setMaxAccess(_B)
if mibBuilder.loadTexts:enableSsh.setStatus(_A)
class _SshPort_Type(MxIpPort):defaultValue=22
_SshPort_Type.__name__=_E
_SshPort_Object=MibScalar
sshPort=_SshPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1100,200),_SshPort_Type())
sshPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sshPort.setStatus(_A)
class _SshSecurityLevel_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('permissive',100),('standard',200),('mostSecure',300)))
_SshSecurityLevel_Type.__name__=_C
_SshSecurityLevel_Object=MibScalar
sshSecurityLevel=_SshSecurityLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,1100,300),_SshSecurityLevel_Type())
sshSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:sshSecurityLevel.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,2700,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess('read-only')
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols('MX-CLI-MIB',**{'cliMIB':cliMIB,'cliMIBObjects':cliMIBObjects,'inactivityTimeOut':inactivityTimeOut,'welcomeMessage':welcomeMessage,'telnetGroup':telnetGroup,'enableTelnet':enableTelnet,'telnetPort':telnetPort,'sshGroup':sshGroup,'enableSsh':enableSsh,'sshPort':sshPort,'sshSecurityLevel':sshSecurityLevel,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})