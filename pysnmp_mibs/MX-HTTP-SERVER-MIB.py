_a='httpServerCustomisationGroupVer1'
_Z='httpServerServerGroupVer1'
_Y='httpServerBasicGroupVer1'
_X='httpServerBandwidthControlSectionEnable'
_W='httpServerSipAuthenticationEnable'
_V='httpServerPort'
_U='httpServerUserRealm'
_T='httpServerAdminRealm'
_S='httpServerResetToDefaultAdminPwd'
_R='httpServerDefaultAdminPassword'
_Q='httpServerAdminUsername'
_P='httpServerAdminAccess'
_O='httpServerResetToDefaultPwd'
_N='httpServerDefaultPassword'
_M='httpServerUsername'
_L='httpServerAccess'
_K='httpServerEnable'
_J='default'
_I='wanOnly'
_H='lanOnly'
_G='MxIpPort'
_F='MxEnableState'
_E='Integer32'
_D='OctetString'
_C='read-write'
_B='MX-HTTP-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,mediatrixConfig=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','mediatrixConfig')
MxEnableState,MxIpAddress,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC',_F,'MxIpAddress',_G,'MxIpSubnetMask')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
httpServerMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,120))
if mibBuilder.loadTexts:httpServerMIB.setRevisions(('2009-05-20 00:00','2005-10-07 00:00','2005-04-25 00:00','2004-09-29 00:00','2004-08-31 00:00','2004-02-23 00:00','2004-02-09 00:00','2003-11-13 00:00','2003-11-03 00:00'))
_IpAddressConfigHttpServer_ObjectIdentity=ObjectIdentity
ipAddressConfigHttpServer=_IpAddressConfigHttpServer_ObjectIdentity((1,3,6,1,4,1,4935,15,1,110))
class _HttpServerPort_Type(MxIpPort):defaultValue=80
_HttpServerPort_Type.__name__=_G
_HttpServerPort_Object=MibScalar
httpServerPort=_HttpServerPort_Object((1,3,6,1,4,1,4935,15,1,110,5),_HttpServerPort_Type())
httpServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerPort.setStatus(_A)
class _HttpServerAdminPort_Type(MxIpPort):defaultValue=8080
_HttpServerAdminPort_Type.__name__=_G
_HttpServerAdminPort_Object=MibScalar
httpServerAdminPort=_HttpServerAdminPort_Object((1,3,6,1,4,1,4935,15,1,110,10),_HttpServerAdminPort_Type())
httpServerAdminPort.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerAdminPort.setStatus(_A)
_HttpServerMIBObjects_ObjectIdentity=ObjectIdentity
httpServerMIBObjects=_HttpServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,120,1))
class _HttpServerEnable_Type(MxEnableState):defaultValue=1
_HttpServerEnable_Type.__name__=_F
_HttpServerEnable_Object=MibScalar
httpServerEnable=_HttpServerEnable_Object((1,3,6,1,4,1,4935,15,120,1,5),_HttpServerEnable_Type())
httpServerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerEnable.setStatus(_A)
class _HttpServerAccess_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_I,1),('all',2)))
_HttpServerAccess_Type.__name__=_E
_HttpServerAccess_Object=MibScalar
httpServerAccess=_HttpServerAccess_Object((1,3,6,1,4,1,4935,15,120,1,50),_HttpServerAccess_Type())
httpServerAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerAccess.setStatus(_A)
class _HttpServerUsername_Type(OctetString):defaultValue=OctetString('admin');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HttpServerUsername_Type.__name__=_D
_HttpServerUsername_Object=MibScalar
httpServerUsername=_HttpServerUsername_Object((1,3,6,1,4,1,4935,15,120,1,100),_HttpServerUsername_Type())
httpServerUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerUsername.setStatus(_A)
class _HttpServerDefaultPassword_Type(OctetString):defaultValue=OctetString('1234');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HttpServerDefaultPassword_Type.__name__=_D
_HttpServerDefaultPassword_Object=MibScalar
httpServerDefaultPassword=_HttpServerDefaultPassword_Object((1,3,6,1,4,1,4935,15,120,1,150),_HttpServerDefaultPassword_Type())
httpServerDefaultPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerDefaultPassword.setStatus(_A)
class _HttpServerResetToDefaultPwd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noOp',0),('reset',1)))
_HttpServerResetToDefaultPwd_Type.__name__=_E
_HttpServerResetToDefaultPwd_Object=MibScalar
httpServerResetToDefaultPwd=_HttpServerResetToDefaultPwd_Object((1,3,6,1,4,1,4935,15,120,1,200),_HttpServerResetToDefaultPwd_Type())
httpServerResetToDefaultPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerResetToDefaultPwd.setStatus(_A)
class _HttpServerAdminAccess_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_I,1),('all',2)))
_HttpServerAdminAccess_Type.__name__=_E
_HttpServerAdminAccess_Object=MibScalar
httpServerAdminAccess=_HttpServerAdminAccess_Object((1,3,6,1,4,1,4935,15,120,1,205),_HttpServerAdminAccess_Type())
httpServerAdminAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerAdminAccess.setStatus(_A)
class _HttpServerAdminUsername_Type(OctetString):defaultValue=OctetString('root');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HttpServerAdminUsername_Type.__name__=_D
_HttpServerAdminUsername_Object=MibScalar
httpServerAdminUsername=_HttpServerAdminUsername_Object((1,3,6,1,4,1,4935,15,120,1,210),_HttpServerAdminUsername_Type())
httpServerAdminUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerAdminUsername.setStatus(_A)
class _HttpServerDefaultAdminPassword_Type(OctetString):defaultValue=OctetString('5678');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HttpServerDefaultAdminPassword_Type.__name__=_D
_HttpServerDefaultAdminPassword_Object=MibScalar
httpServerDefaultAdminPassword=_HttpServerDefaultAdminPassword_Object((1,3,6,1,4,1,4935,15,120,1,215),_HttpServerDefaultAdminPassword_Type())
httpServerDefaultAdminPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerDefaultAdminPassword.setStatus(_A)
class _HttpServerResetToDefaultAdminPwd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noOp',0),('reset',1)))
_HttpServerResetToDefaultAdminPwd_Type.__name__=_E
_HttpServerResetToDefaultAdminPwd_Object=MibScalar
httpServerResetToDefaultAdminPwd=_HttpServerResetToDefaultAdminPwd_Object((1,3,6,1,4,1,4935,15,120,1,220),_HttpServerResetToDefaultAdminPwd_Type())
httpServerResetToDefaultAdminPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerResetToDefaultAdminPwd.setStatus(_A)
class _HttpServerAdminRealm_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HttpServerAdminRealm_Type.__name__=_D
_HttpServerAdminRealm_Object=MibScalar
httpServerAdminRealm=_HttpServerAdminRealm_Object((1,3,6,1,4,1,4935,15,120,1,225),_HttpServerAdminRealm_Type())
httpServerAdminRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerAdminRealm.setStatus(_A)
class _HttpServerUserRealm_Type(OctetString):defaultValue=OctetString(_J);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HttpServerUserRealm_Type.__name__=_D
_HttpServerUserRealm_Object=MibScalar
httpServerUserRealm=_HttpServerUserRealm_Object((1,3,6,1,4,1,4935,15,120,1,230),_HttpServerUserRealm_Type())
httpServerUserRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerUserRealm.setStatus(_A)
_HttpServerMIBCustomisation_ObjectIdentity=ObjectIdentity
httpServerMIBCustomisation=_HttpServerMIBCustomisation_ObjectIdentity((1,3,6,1,4,1,4935,15,120,1,250))
class _HttpServerSipAuthenticationEnable_Type(MxEnableState):defaultValue=0
_HttpServerSipAuthenticationEnable_Type.__name__=_F
_HttpServerSipAuthenticationEnable_Object=MibScalar
httpServerSipAuthenticationEnable=_HttpServerSipAuthenticationEnable_Object((1,3,6,1,4,1,4935,15,120,1,250,20),_HttpServerSipAuthenticationEnable_Type())
httpServerSipAuthenticationEnable.setMaxAccess('read-only')
if mibBuilder.loadTexts:httpServerSipAuthenticationEnable.setStatus(_A)
class _HttpServerBandwidthControlSectionEnable_Type(MxEnableState):defaultValue=0
_HttpServerBandwidthControlSectionEnable_Type.__name__=_F
_HttpServerBandwidthControlSectionEnable_Object=MibScalar
httpServerBandwidthControlSectionEnable=_HttpServerBandwidthControlSectionEnable_Object((1,3,6,1,4,1,4935,15,120,1,250,30),_HttpServerBandwidthControlSectionEnable_Type())
httpServerBandwidthControlSectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:httpServerBandwidthControlSectionEnable.setStatus(_A)
_HttpServerConformance_ObjectIdentity=ObjectIdentity
httpServerConformance=_HttpServerConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,120,2))
_HttpServerCompliances_ObjectIdentity=ObjectIdentity
httpServerCompliances=_HttpServerCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,120,2,1))
_HttpServerGroups_ObjectIdentity=ObjectIdentity
httpServerGroups=_HttpServerGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,120,2,5))
httpServerBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,120,2,5,5))
httpServerBasicGroupVer1.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:httpServerBasicGroupVer1.setStatus(_A)
httpServerServerGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,120,2,5,10))
httpServerServerGroupVer1.setObjects((_B,_V))
if mibBuilder.loadTexts:httpServerServerGroupVer1.setStatus(_A)
httpServerCustomisationGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,120,2,5,15))
httpServerCustomisationGroupVer1.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:httpServerCustomisationGroupVer1.setStatus(_A)
httpServerComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,120,2,1,1))
httpServerComplVer1.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:httpServerComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressConfigHttpServer':ipAddressConfigHttpServer,_V:httpServerPort,'httpServerAdminPort':httpServerAdminPort,'httpServerMIB':httpServerMIB,'httpServerMIBObjects':httpServerMIBObjects,_K:httpServerEnable,_L:httpServerAccess,_M:httpServerUsername,_N:httpServerDefaultPassword,_O:httpServerResetToDefaultPwd,_P:httpServerAdminAccess,_Q:httpServerAdminUsername,_R:httpServerDefaultAdminPassword,_S:httpServerResetToDefaultAdminPwd,_T:httpServerAdminRealm,_U:httpServerUserRealm,'httpServerMIBCustomisation':httpServerMIBCustomisation,_W:httpServerSipAuthenticationEnable,_X:httpServerBandwidthControlSectionEnable,'httpServerConformance':httpServerConformance,'httpServerCompliances':httpServerCompliances,'httpServerComplVer1':httpServerComplVer1,'httpServerGroups':httpServerGroups,_Y:httpServerBasicGroupVer1,_Z:httpServerServerGroupVer1,_a:httpServerCustomisationGroupVer1})