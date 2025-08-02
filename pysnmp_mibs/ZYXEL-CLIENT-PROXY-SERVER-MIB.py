_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelClientProxyServer=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,121))
_ZyxelClientProxyServerSetup_ObjectIdentity=ObjectIdentity
zyxelClientProxyServerSetup=_ZyxelClientProxyServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,121,1))
_ZyClientProxyServerHttpState_Type=EnabledStatus
_ZyClientProxyServerHttpState_Object=MibScalar
zyClientProxyServerHttpState=_ZyClientProxyServerHttpState_Object((1,3,6,1,4,1,890,1,15,3,121,1,1),_ZyClientProxyServerHttpState_Type())
zyClientProxyServerHttpState.setMaxAccess(_A)
if mibBuilder.loadTexts:zyClientProxyServerHttpState.setStatus(_B)
_ZyClientProxyServerHttpServer_Type=DisplayString
_ZyClientProxyServerHttpServer_Object=MibScalar
zyClientProxyServerHttpServer=_ZyClientProxyServerHttpServer_Object((1,3,6,1,4,1,890,1,15,3,121,1,2),_ZyClientProxyServerHttpServer_Type())
zyClientProxyServerHttpServer.setMaxAccess(_A)
if mibBuilder.loadTexts:zyClientProxyServerHttpServer.setStatus(_B)
_ZyClientProxyServerHttpPort_Type=Integer32
_ZyClientProxyServerHttpPort_Object=MibScalar
zyClientProxyServerHttpPort=_ZyClientProxyServerHttpPort_Object((1,3,6,1,4,1,890,1,15,3,121,1,3),_ZyClientProxyServerHttpPort_Type())
zyClientProxyServerHttpPort.setMaxAccess(_A)
if mibBuilder.loadTexts:zyClientProxyServerHttpPort.setStatus(_B)
_ZyClientProxyServerHttpAuthenticationState_Type=EnabledStatus
_ZyClientProxyServerHttpAuthenticationState_Object=MibScalar
zyClientProxyServerHttpAuthenticationState=_ZyClientProxyServerHttpAuthenticationState_Object((1,3,6,1,4,1,890,1,15,3,121,1,4),_ZyClientProxyServerHttpAuthenticationState_Type())
zyClientProxyServerHttpAuthenticationState.setMaxAccess(_A)
if mibBuilder.loadTexts:zyClientProxyServerHttpAuthenticationState.setStatus(_B)
_ZyClientProxyServerHttpUsername_Type=DisplayString
_ZyClientProxyServerHttpUsername_Object=MibScalar
zyClientProxyServerHttpUsername=_ZyClientProxyServerHttpUsername_Object((1,3,6,1,4,1,890,1,15,3,121,1,5),_ZyClientProxyServerHttpUsername_Type())
zyClientProxyServerHttpUsername.setMaxAccess(_A)
if mibBuilder.loadTexts:zyClientProxyServerHttpUsername.setStatus(_B)
_ZyClientProxyServerHttpPassword_Type=DisplayString
_ZyClientProxyServerHttpPassword_Object=MibScalar
zyClientProxyServerHttpPassword=_ZyClientProxyServerHttpPassword_Object((1,3,6,1,4,1,890,1,15,3,121,1,6),_ZyClientProxyServerHttpPassword_Type())
zyClientProxyServerHttpPassword.setMaxAccess(_A)
if mibBuilder.loadTexts:zyClientProxyServerHttpPassword.setStatus(_B)
mibBuilder.exportSymbols('ZYXEL-CLIENT-PROXY-SERVER-MIB',**{'zyxelClientProxyServer':zyxelClientProxyServer,'zyxelClientProxyServerSetup':zyxelClientProxyServerSetup,'zyClientProxyServerHttpState':zyClientProxyServerHttpState,'zyClientProxyServerHttpServer':zyClientProxyServerHttpServer,'zyClientProxyServerHttpPort':zyClientProxyServerHttpPort,'zyClientProxyServerHttpAuthenticationState':zyClientProxyServerHttpAuthenticationState,'zyClientProxyServerHttpUsername':zyClientProxyServerHttpUsername,'zyClientProxyServerHttpPassword':zyClientProxyServerHttpPassword})