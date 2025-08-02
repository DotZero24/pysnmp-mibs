_A2='interpretFirst'
_A1='behaviorOnT38InviteNotAcceptedSipErrorCode'
_A0='unsupportedMediaType'
_z='inactive'
_y='gwSpecificRtcpXrGatewayName'
_x='transparent'
_w='aocConfigGatewayName'
_v='gwEventHandlingGatewayName'
_u='gwSpecificConferenceGatewayName'
_t='mwiStatusIndex'
_s='gwSpecificMwiGatewayName'
_r='diversionConfigGatewayName'
_q='supported'
_p='gwKeepAliveAlternateDestinationGatewayName'
_o='errorMappingCauseToSipCause'
_n='errorMappingSipToCauseSipCode'
_m='gwSpecificFailoverGatewayName'
_l='5xxOnRegistration'
_k='tlsPersistentConnectionStatusIndex'
_j='transportConfigGatewayName'
_i='invalidResponse'
_h='configError'
_g='authFailed'
_f='unreachable'
_e='refreshing'
_d='registrationStatusIndex'
_c='unitRegistrationsIndex'
_b='gwSpecificRegistrationGatewayName'
_a='authenticationIndex'
_Z='gwSpecificProxyGatewayName'
_Y='noRouteHeader'
_X='strictRouter'
_W='looseRouter'
_V='userAgentEpId'
_U='gatewayStatusName'
_T='gatewayName'
_S='disable'
_R='192.168.0.10:0'
_Q='MxAdvancedIpPort'
_P='disabled'
_O='unsupported'
_N='rejected'
_M='192.168.10.10:0'
_L='delete'
_K='none'
_J='noOp'
_I='MxIpHostNamePort'
_H='MX-SIPEP-MIB'
_G='OctetString'
_F='Unsigned32'
_E='read-only'
_D='MxEnableState'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState',_Q,'MxDigitMap',_D,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_I,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sipEpMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400))
_SipEpMIBObjects_ObjectIdentity=ObjectIdentity
sipEpMIBObjects=_SipEpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1))
_GatewayTable_Object=MibTable
gatewayTable=_GatewayTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100))
if mibBuilder.loadTexts:gatewayTable.setStatus(_A)
_GatewayEntry_Object=MibTableRow
gatewayEntry=_GatewayEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1))
gatewayEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:gatewayEntry.setStatus(_A)
_GatewayName_Type=OctetString
_GatewayName_Object=MibTableColumn
gatewayName=_GatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,100),_GatewayName_Type())
gatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayName.setStatus(_A)
class _GatewayType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('trunkGateway',100),('endpointGateway',200)))
_GatewayType_Type.__name__=_C
_GatewayType_Object=MibTableColumn
gatewayType=_GatewayType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,150),_GatewayType_Type())
gatewayType.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayType.setStatus(_A)
class _GatewayNetworkInterface_Type(OctetString):defaultValue=OctetString('Lan1');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_GatewayNetworkInterface_Type.__name__=_G
_GatewayNetworkInterface_Object=MibTableColumn
gatewayNetworkInterface=_GatewayNetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,200),_GatewayNetworkInterface_Type())
gatewayNetworkInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayNetworkInterface.setStatus(_A)
class _GatewayMediaNetworks_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GatewayMediaNetworks_Type.__name__=_G
_GatewayMediaNetworks_Object=MibTableColumn
gatewayMediaNetworks=_GatewayMediaNetworks_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,250),_GatewayMediaNetworks_Type())
gatewayMediaNetworks.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayMediaNetworks.setStatus(_A)
class _GatewayPort_Type(MxAdvancedIpPort):defaultValue=0
_GatewayPort_Type.__name__=_Q
_GatewayPort_Object=MibTableColumn
gatewayPort=_GatewayPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,300),_GatewayPort_Type())
gatewayPort.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayPort.setStatus(_A)
class _GatewaySecurePort_Type(MxAdvancedIpPort):defaultValue=0
_GatewaySecurePort_Type.__name__=_Q
_GatewaySecurePort_Object=MibTableColumn
gatewaySecurePort=_GatewaySecurePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,325),_GatewaySecurePort_Type())
gatewaySecurePort.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewaySecurePort.setStatus(_A)
class _GatewayDomain_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GatewayDomain_Type.__name__=_G
_GatewayDomain_Object=MibTableColumn
gatewayDomain=_GatewayDomain_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,350),_GatewayDomain_Type())
gatewayDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayDomain.setStatus(_A)
class _GatewayDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_L,10)))
_GatewayDelete_Type.__name__=_C
_GatewayDelete_Object=MibTableColumn
gatewayDelete=_GatewayDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,100,1,400),_GatewayDelete_Type())
gatewayDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayDelete.setStatus(_A)
_GatewayStatusTable_Object=MibTable
gatewayStatusTable=_GatewayStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150))
if mibBuilder.loadTexts:gatewayStatusTable.setStatus(_A)
_GatewayStatusEntry_Object=MibTableRow
gatewayStatusEntry=_GatewayStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1))
gatewayStatusEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:gatewayStatusEntry.setStatus(_A)
_GatewayStatusName_Type=OctetString
_GatewayStatusName_Object=MibTableColumn
gatewayStatusName=_GatewayStatusName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,100),_GatewayStatusName_Type())
gatewayStatusName.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusName.setStatus(_A)
_GatewayStatusNetworkInterface_Type=OctetString
_GatewayStatusNetworkInterface_Object=MibTableColumn
gatewayStatusNetworkInterface=_GatewayStatusNetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,200),_GatewayStatusNetworkInterface_Type())
gatewayStatusNetworkInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusNetworkInterface.setStatus(_A)
_GatewayStatusMediaNetworks_Type=OctetString
_GatewayStatusMediaNetworks_Object=MibTableColumn
gatewayStatusMediaNetworks=_GatewayStatusMediaNetworks_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,250),_GatewayStatusMediaNetworks_Type())
gatewayStatusMediaNetworks.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusMediaNetworks.setStatus(_A)
_GatewayStatusPort_Type=MxAdvancedIpPort
_GatewayStatusPort_Object=MibTableColumn
gatewayStatusPort=_GatewayStatusPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,300),_GatewayStatusPort_Type())
gatewayStatusPort.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusPort.setStatus(_A)
_GatewayStatusSecurePort_Type=MxAdvancedIpPort
_GatewayStatusSecurePort_Object=MibTableColumn
gatewayStatusSecurePort=_GatewayStatusSecurePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,325),_GatewayStatusSecurePort_Type())
gatewayStatusSecurePort.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusSecurePort.setStatus(_A)
_GatewayStatusDomain_Type=OctetString
_GatewayStatusDomain_Object=MibTableColumn
gatewayStatusDomain=_GatewayStatusDomain_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,350),_GatewayStatusDomain_Type())
gatewayStatusDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusDomain.setStatus(_A)
_GatewayStatusState_Type=OctetString
_GatewayStatusState_Object=MibTableColumn
gatewayStatusState=_GatewayStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,150,1,400),_GatewayStatusState_Type())
gatewayStatusState.setMaxAccess(_E)
if mibBuilder.loadTexts:gatewayStatusState.setStatus(_A)
_UserAgentTable_Object=MibTable
userAgentTable=_UserAgentTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400))
if mibBuilder.loadTexts:userAgentTable.setStatus(_A)
_UserAgentEntry_Object=MibTableRow
userAgentEntry=_UserAgentEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1))
userAgentEntry.setIndexNames((0,_H,_V))
if mibBuilder.loadTexts:userAgentEntry.setStatus(_A)
_UserAgentEpId_Type=OctetString
_UserAgentEpId_Object=MibTableColumn
userAgentEpId=_UserAgentEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,100),_UserAgentEpId_Type())
userAgentEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:userAgentEpId.setStatus(_A)
class _UserAgentUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UserAgentUsername_Type.__name__=_G
_UserAgentUsername_Object=MibTableColumn
userAgentUsername=_UserAgentUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,200),_UserAgentUsername_Type())
userAgentUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentUsername.setStatus(_A)
class _UserAgentFriendlyName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UserAgentFriendlyName_Type.__name__=_G
_UserAgentFriendlyName_Object=MibTableColumn
userAgentFriendlyName=_UserAgentFriendlyName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,300),_UserAgentFriendlyName_Type())
userAgentFriendlyName.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentFriendlyName.setStatus(_A)
class _UserAgentRegister_Type(MxEnableState):defaultValue=0
_UserAgentRegister_Type.__name__=_D
_UserAgentRegister_Object=MibTableColumn
userAgentRegister=_UserAgentRegister_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,400),_UserAgentRegister_Type())
userAgentRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentRegister.setStatus(_A)
class _UserAgentGatewayName_Type(OctetString):defaultValue=OctetString('all')
_UserAgentGatewayName_Type.__name__=_G
_UserAgentGatewayName_Object=MibTableColumn
userAgentGatewayName=_UserAgentGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,500),_UserAgentGatewayName_Type())
userAgentGatewayName.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentGatewayName.setStatus(_A)
class _UserAgentMwiSubscribe_Type(MxEnableState):defaultValue=0
_UserAgentMwiSubscribe_Type.__name__=_D
_UserAgentMwiSubscribe_Object=MibTableColumn
userAgentMwiSubscribe=_UserAgentMwiSubscribe_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,700),_UserAgentMwiSubscribe_Type())
userAgentMwiSubscribe.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentMwiSubscribe.setStatus(_A)
class _UserAgentContactDomain_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UserAgentContactDomain_Type.__name__=_G
_UserAgentContactDomain_Object=MibTableColumn
userAgentContactDomain=_UserAgentContactDomain_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,800),_UserAgentContactDomain_Type())
userAgentContactDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentContactDomain.setStatus(_A)
class _UserAgentAcceptLanguage_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UserAgentAcceptLanguage_Type.__name__=_G
_UserAgentAcceptLanguage_Object=MibTableColumn
userAgentAcceptLanguage=_UserAgentAcceptLanguage_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,400,1,900),_UserAgentAcceptLanguage_Type())
userAgentAcceptLanguage.setMaxAccess(_B)
if mibBuilder.loadTexts:userAgentAcceptLanguage.setStatus(_A)
_ProxyGroup_ObjectIdentity=ObjectIdentity
proxyGroup=_ProxyGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500))
class _DefaultStaticProxyHomeDomainHost_Type(MxIpHostNamePort):defaultValue=OctetString(_M)
_DefaultStaticProxyHomeDomainHost_Type.__name__=_I
_DefaultStaticProxyHomeDomainHost_Object=MibScalar
defaultStaticProxyHomeDomainHost=_DefaultStaticProxyHomeDomainHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,100),_DefaultStaticProxyHomeDomainHost_Type())
defaultStaticProxyHomeDomainHost.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticProxyHomeDomainHost.setStatus(_A)
class _DefaultStaticProxyOutboundHost_Type(MxIpHostNamePort):defaultValue=OctetString('')
_DefaultStaticProxyOutboundHost_Type.__name__=_I
_DefaultStaticProxyOutboundHost_Object=MibScalar
defaultStaticProxyOutboundHost=_DefaultStaticProxyOutboundHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,200),_DefaultStaticProxyOutboundHost_Type())
defaultStaticProxyOutboundHost.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticProxyOutboundHost.setStatus(_A)
class _DefaultProxyOutboundType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_W,100),(_X,200),(_Y,300)))
_DefaultProxyOutboundType_Type.__name__=_C
_DefaultProxyOutboundType_Object=MibScalar
defaultProxyOutboundType=_DefaultProxyOutboundType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,300),_DefaultProxyOutboundType_Type())
defaultProxyOutboundType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultProxyOutboundType.setStatus(_A)
_GwSpecificProxyTable_Object=MibTable
gwSpecificProxyTable=_GwSpecificProxyTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400))
if mibBuilder.loadTexts:gwSpecificProxyTable.setStatus(_A)
_GwSpecificProxyEntry_Object=MibTableRow
gwSpecificProxyEntry=_GwSpecificProxyEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400,1))
gwSpecificProxyEntry.setIndexNames((0,_H,_Z))
if mibBuilder.loadTexts:gwSpecificProxyEntry.setStatus(_A)
_GwSpecificProxyGatewayName_Type=OctetString
_GwSpecificProxyGatewayName_Object=MibTableColumn
gwSpecificProxyGatewayName=_GwSpecificProxyGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400,1,100),_GwSpecificProxyGatewayName_Type())
gwSpecificProxyGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwSpecificProxyGatewayName.setStatus(_A)
class _GwSpecificProxyEnableConfig_Type(MxEnableState):defaultValue=0
_GwSpecificProxyEnableConfig_Type.__name__=_D
_GwSpecificProxyEnableConfig_Object=MibTableColumn
gwSpecificProxyEnableConfig=_GwSpecificProxyEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400,1,200),_GwSpecificProxyEnableConfig_Type())
gwSpecificProxyEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificProxyEnableConfig.setStatus(_A)
class _GwSpecificProxyHomeDomainHost_Type(MxIpHostNamePort):defaultValue=OctetString(_R)
_GwSpecificProxyHomeDomainHost_Type.__name__=_I
_GwSpecificProxyHomeDomainHost_Object=MibTableColumn
gwSpecificProxyHomeDomainHost=_GwSpecificProxyHomeDomainHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400,1,300),_GwSpecificProxyHomeDomainHost_Type())
gwSpecificProxyHomeDomainHost.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificProxyHomeDomainHost.setStatus(_A)
class _GwSpecificProxyOutboundHost_Type(MxIpHostNamePort):defaultValue=OctetString('0.0.0.0:0')
_GwSpecificProxyOutboundHost_Type.__name__=_I
_GwSpecificProxyOutboundHost_Object=MibTableColumn
gwSpecificProxyOutboundHost=_GwSpecificProxyOutboundHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400,1,400),_GwSpecificProxyOutboundHost_Type())
gwSpecificProxyOutboundHost.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificProxyOutboundHost.setStatus(_A)
class _GwSpecificProxyOutboundType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_W,100),(_X,200),(_Y,300)))
_GwSpecificProxyOutboundType_Type.__name__=_C
_GwSpecificProxyOutboundType_Object=MibTableColumn
gwSpecificProxyOutboundType=_GwSpecificProxyOutboundType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,500,400,1,500),_GwSpecificProxyOutboundType_Type())
gwSpecificProxyOutboundType.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificProxyOutboundType.setStatus(_A)
_SessionRefreshGroup_ObjectIdentity=ObjectIdentity
sessionRefreshGroup=_SessionRefreshGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,600))
class _DefaultSessionTimerEnable_Type(MxEnableState):defaultValue=1
_DefaultSessionTimerEnable_Type.__name__=_D
_DefaultSessionTimerEnable_Object=MibScalar
defaultSessionTimerEnable=_DefaultSessionTimerEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,600,100),_DefaultSessionTimerEnable_Type())
defaultSessionTimerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSessionTimerEnable.setStatus(_A)
class _DefaultSessionTimerMinimumExpirationDelay_Type(Unsigned32):defaultValue=1800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,86400))
_DefaultSessionTimerMinimumExpirationDelay_Type.__name__=_F
_DefaultSessionTimerMinimumExpirationDelay_Object=MibScalar
defaultSessionTimerMinimumExpirationDelay=_DefaultSessionTimerMinimumExpirationDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,600,200),_DefaultSessionTimerMinimumExpirationDelay_Type())
defaultSessionTimerMinimumExpirationDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSessionTimerMinimumExpirationDelay.setStatus(_A)
class _DefaultSessionTimerMaximumExpirationDelay_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,86400))
_DefaultSessionTimerMaximumExpirationDelay_Type.__name__=_F
_DefaultSessionTimerMaximumExpirationDelay_Object=MibScalar
defaultSessionTimerMaximumExpirationDelay=_DefaultSessionTimerMaximumExpirationDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,600,300),_DefaultSessionTimerMaximumExpirationDelay_Type())
defaultSessionTimerMaximumExpirationDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSessionTimerMaximumExpirationDelay.setStatus(_A)
class _SessionRefreshRequestMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('reInvite',100),('update',200)))
_SessionRefreshRequestMethod_Type.__name__=_C
_SessionRefreshRequestMethod_Object=MibScalar
sessionRefreshRequestMethod=_SessionRefreshRequestMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,600,400),_SessionRefreshRequestMethod_Type())
sessionRefreshRequestMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:sessionRefreshRequestMethod.setStatus(_A)
_AuthenticationGroup_ObjectIdentity=ObjectIdentity
authenticationGroup=_AuthenticationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700))
_AuthenticationTable_Object=MibTable
authenticationTable=_AuthenticationTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100))
if mibBuilder.loadTexts:authenticationTable.setStatus(_A)
_AuthenticationEntry_Object=MibTableRow
authenticationEntry=_AuthenticationEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1))
authenticationEntry.setIndexNames((0,_H,_a))
if mibBuilder.loadTexts:authenticationEntry.setStatus(_A)
_AuthenticationIndex_Type=Unsigned32
_AuthenticationIndex_Object=MibTableColumn
authenticationIndex=_AuthenticationIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,100),_AuthenticationIndex_Type())
authenticationIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:authenticationIndex.setStatus(_A)
class _AuthenticationCriteriaSelection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('unit',100),('endpoint',200),('gateway',300),('username',400)))
_AuthenticationCriteriaSelection_Type.__name__=_C
_AuthenticationCriteriaSelection_Object=MibTableColumn
authenticationCriteriaSelection=_AuthenticationCriteriaSelection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,200),_AuthenticationCriteriaSelection_Type())
authenticationCriteriaSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationCriteriaSelection.setStatus(_A)
class _AuthenticationEpId_Type(OctetString):defaultValue=OctetString('')
_AuthenticationEpId_Type.__name__=_G
_AuthenticationEpId_Object=MibTableColumn
authenticationEpId=_AuthenticationEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,300),_AuthenticationEpId_Type())
authenticationEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationEpId.setStatus(_A)
class _AuthenticationGatewayName_Type(OctetString):defaultValue=OctetString('')
_AuthenticationGatewayName_Type.__name__=_G
_AuthenticationGatewayName_Object=MibTableColumn
authenticationGatewayName=_AuthenticationGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,350),_AuthenticationGatewayName_Type())
authenticationGatewayName.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationGatewayName.setStatus(_A)
class _AuthenticationUsernameCriteria_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AuthenticationUsernameCriteria_Type.__name__=_G
_AuthenticationUsernameCriteria_Object=MibTableColumn
authenticationUsernameCriteria=_AuthenticationUsernameCriteria_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,360),_AuthenticationUsernameCriteria_Type())
authenticationUsernameCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationUsernameCriteria.setStatus(_A)
class _AuthenticationValidateRealm_Type(MxEnableState):defaultValue=1
_AuthenticationValidateRealm_Type.__name__=_D
_AuthenticationValidateRealm_Object=MibTableColumn
authenticationValidateRealm=_AuthenticationValidateRealm_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,375),_AuthenticationValidateRealm_Type())
authenticationValidateRealm.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationValidateRealm.setStatus(_A)
class _AuthenticationRealm_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AuthenticationRealm_Type.__name__=_G
_AuthenticationRealm_Object=MibTableColumn
authenticationRealm=_AuthenticationRealm_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,400),_AuthenticationRealm_Type())
authenticationRealm.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationRealm.setStatus(_A)
class _AuthenticationUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AuthenticationUsername_Type.__name__=_G
_AuthenticationUsername_Object=MibTableColumn
authenticationUsername=_AuthenticationUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,500),_AuthenticationUsername_Type())
authenticationUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationUsername.setStatus(_A)
class _AuthenticationPassword_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AuthenticationPassword_Type.__name__=_G
_AuthenticationPassword_Object=MibTableColumn
authenticationPassword=_AuthenticationPassword_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,600),_AuthenticationPassword_Type())
authenticationPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationPassword.setStatus(_A)
class _AuthenticationUp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),('up',10)))
_AuthenticationUp_Type.__name__=_C
_AuthenticationUp_Object=MibTableColumn
authenticationUp=_AuthenticationUp_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,700),_AuthenticationUp_Type())
authenticationUp.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationUp.setStatus(_A)
class _AuthenticationDown_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),('down',10)))
_AuthenticationDown_Type.__name__=_C
_AuthenticationDown_Object=MibTableColumn
authenticationDown=_AuthenticationDown_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,800),_AuthenticationDown_Type())
authenticationDown.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationDown.setStatus(_A)
class _AuthenticationInsert_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),('insert',10)))
_AuthenticationInsert_Type.__name__=_C
_AuthenticationInsert_Object=MibTableColumn
authenticationInsert=_AuthenticationInsert_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,900),_AuthenticationInsert_Type())
authenticationInsert.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationInsert.setStatus(_A)
class _AuthenticationDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_L,10)))
_AuthenticationDelete_Type.__name__=_C
_AuthenticationDelete_Object=MibTableColumn
authenticationDelete=_AuthenticationDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,700,100,1,1000),_AuthenticationDelete_Type())
authenticationDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:authenticationDelete.setStatus(_A)
_RegistrationGroup_ObjectIdentity=ObjectIdentity
registrationGroup=_RegistrationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800))
class _DefaultRegistrationRefreshTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_DefaultRegistrationRefreshTime_Type.__name__=_F
_DefaultRegistrationRefreshTime_Object=MibScalar
defaultRegistrationRefreshTime=_DefaultRegistrationRefreshTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,200),_DefaultRegistrationRefreshTime_Type())
defaultRegistrationRefreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRegistrationRefreshTime.setStatus(_A)
class _DefaultRegistrationExpirationValue_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_DefaultRegistrationExpirationValue_Type.__name__=_F
_DefaultRegistrationExpirationValue_Object=MibScalar
defaultRegistrationExpirationValue=_DefaultRegistrationExpirationValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,250),_DefaultRegistrationExpirationValue_Type())
defaultRegistrationExpirationValue.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRegistrationExpirationValue.setStatus(_A)
class _DefaultRegistrationProposedExpirationValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_DefaultRegistrationProposedExpirationValue_Type.__name__=_F
_DefaultRegistrationProposedExpirationValue_Object=MibScalar
defaultRegistrationProposedExpirationValue=_DefaultRegistrationProposedExpirationValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,300),_DefaultRegistrationProposedExpirationValue_Type())
defaultRegistrationProposedExpirationValue.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRegistrationProposedExpirationValue.setStatus(_A)
class _DefaultRegistrationRetryTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_DefaultRegistrationRetryTime_Type.__name__=_F
_DefaultRegistrationRetryTime_Object=MibScalar
defaultRegistrationRetryTime=_DefaultRegistrationRetryTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,350),_DefaultRegistrationRetryTime_Type())
defaultRegistrationRetryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRegistrationRetryTime.setStatus(_A)
class _DefaultRegistrationUnregisteredBehavior_Type(MxEnableState):defaultValue=0
_DefaultRegistrationUnregisteredBehavior_Type.__name__=_D
_DefaultRegistrationUnregisteredBehavior_Object=MibScalar
defaultRegistrationUnregisteredBehavior=_DefaultRegistrationUnregisteredBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,400),_DefaultRegistrationUnregisteredBehavior_Type())
defaultRegistrationUnregisteredBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRegistrationUnregisteredBehavior.setStatus(_A)
class _DefaultUnitRegistrationUnregisteredBehavior_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('noEffect',100),('disableGateway',200)))
_DefaultUnitRegistrationUnregisteredBehavior_Type.__name__=_C
_DefaultUnitRegistrationUnregisteredBehavior_Object=MibScalar
defaultUnitRegistrationUnregisteredBehavior=_DefaultUnitRegistrationUnregisteredBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,450),_DefaultUnitRegistrationUnregisteredBehavior_Type())
defaultUnitRegistrationUnregisteredBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultUnitRegistrationUnregisteredBehavior.setStatus(_A)
class _DefaultStaticRegistrarServerHost_Type(MxIpHostNamePort):defaultValue=OctetString(_M)
_DefaultStaticRegistrarServerHost_Type.__name__=_I
_DefaultStaticRegistrarServerHost_Object=MibScalar
defaultStaticRegistrarServerHost=_DefaultStaticRegistrarServerHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,500),_DefaultStaticRegistrarServerHost_Type())
defaultStaticRegistrarServerHost.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticRegistrarServerHost.setStatus(_A)
_GwSpecificRegistrationTable_Object=MibTable
gwSpecificRegistrationTable=_GwSpecificRegistrationTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600))
if mibBuilder.loadTexts:gwSpecificRegistrationTable.setStatus(_A)
_GwSpecificRegistrationEntry_Object=MibTableRow
gwSpecificRegistrationEntry=_GwSpecificRegistrationEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1))
gwSpecificRegistrationEntry.setIndexNames((0,_H,_b))
if mibBuilder.loadTexts:gwSpecificRegistrationEntry.setStatus(_A)
_GwSpecificRegistrationGatewayName_Type=OctetString
_GwSpecificRegistrationGatewayName_Object=MibTableColumn
gwSpecificRegistrationGatewayName=_GwSpecificRegistrationGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,100),_GwSpecificRegistrationGatewayName_Type())
gwSpecificRegistrationGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwSpecificRegistrationGatewayName.setStatus(_A)
class _GwSpecificRegistrationEnableConfig_Type(MxEnableState):defaultValue=0
_GwSpecificRegistrationEnableConfig_Type.__name__=_D
_GwSpecificRegistrationEnableConfig_Object=MibTableColumn
gwSpecificRegistrationEnableConfig=_GwSpecificRegistrationEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,200),_GwSpecificRegistrationEnableConfig_Type())
gwSpecificRegistrationEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationEnableConfig.setStatus(_A)
class _GwSpecificRegistrationRefreshTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_GwSpecificRegistrationRefreshTime_Type.__name__=_F
_GwSpecificRegistrationRefreshTime_Object=MibTableColumn
gwSpecificRegistrationRefreshTime=_GwSpecificRegistrationRefreshTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,300),_GwSpecificRegistrationRefreshTime_Type())
gwSpecificRegistrationRefreshTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationRefreshTime.setStatus(_A)
class _GwSpecificRegistrationExpirationValue_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_GwSpecificRegistrationExpirationValue_Type.__name__=_F
_GwSpecificRegistrationExpirationValue_Object=MibTableColumn
gwSpecificRegistrationExpirationValue=_GwSpecificRegistrationExpirationValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,350),_GwSpecificRegistrationExpirationValue_Type())
gwSpecificRegistrationExpirationValue.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationExpirationValue.setStatus(_A)
class _GwSpecificRegistrationProposedExpirationValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_GwSpecificRegistrationProposedExpirationValue_Type.__name__=_F
_GwSpecificRegistrationProposedExpirationValue_Object=MibTableColumn
gwSpecificRegistrationProposedExpirationValue=_GwSpecificRegistrationProposedExpirationValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,400),_GwSpecificRegistrationProposedExpirationValue_Type())
gwSpecificRegistrationProposedExpirationValue.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationProposedExpirationValue.setStatus(_A)
class _GwSpecificRegistrationRetryTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_GwSpecificRegistrationRetryTime_Type.__name__=_F
_GwSpecificRegistrationRetryTime_Object=MibTableColumn
gwSpecificRegistrationRetryTime=_GwSpecificRegistrationRetryTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,450),_GwSpecificRegistrationRetryTime_Type())
gwSpecificRegistrationRetryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationRetryTime.setStatus(_A)
class _GwSpecificRegistrationUnregisteredBehavior_Type(MxEnableState):defaultValue=0
_GwSpecificRegistrationUnregisteredBehavior_Type.__name__=_D
_GwSpecificRegistrationUnregisteredBehavior_Object=MibTableColumn
gwSpecificRegistrationUnregisteredBehavior=_GwSpecificRegistrationUnregisteredBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,500),_GwSpecificRegistrationUnregisteredBehavior_Type())
gwSpecificRegistrationUnregisteredBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationUnregisteredBehavior.setStatus(_A)
class _GwSpecificRegistrationServerHost_Type(MxIpHostNamePort):defaultValue=OctetString(_R)
_GwSpecificRegistrationServerHost_Type.__name__=_I
_GwSpecificRegistrationServerHost_Object=MibTableColumn
gwSpecificRegistrationServerHost=_GwSpecificRegistrationServerHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,600,1,600),_GwSpecificRegistrationServerHost_Type())
gwSpecificRegistrationServerHost.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRegistrationServerHost.setStatus(_A)
_UnitRegistrationsTable_Object=MibTable
unitRegistrationsTable=_UnitRegistrationsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,700))
if mibBuilder.loadTexts:unitRegistrationsTable.setStatus(_A)
_UnitRegistrationsEntry_Object=MibTableRow
unitRegistrationsEntry=_UnitRegistrationsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,700,1))
unitRegistrationsEntry.setIndexNames((0,_H,_c))
if mibBuilder.loadTexts:unitRegistrationsEntry.setStatus(_A)
_UnitRegistrationsIndex_Type=Unsigned32
_UnitRegistrationsIndex_Object=MibTableColumn
unitRegistrationsIndex=_UnitRegistrationsIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,700,1,100),_UnitRegistrationsIndex_Type())
unitRegistrationsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:unitRegistrationsIndex.setStatus(_A)
class _UnitRegistrationsUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UnitRegistrationsUsername_Type.__name__=_G
_UnitRegistrationsUsername_Object=MibTableColumn
unitRegistrationsUsername=_UnitRegistrationsUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,700,1,200),_UnitRegistrationsUsername_Type())
unitRegistrationsUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:unitRegistrationsUsername.setStatus(_A)
class _UnitRegistrationsGatewayName_Type(OctetString):defaultValue=OctetString('all')
_UnitRegistrationsGatewayName_Type.__name__=_G
_UnitRegistrationsGatewayName_Object=MibTableColumn
unitRegistrationsGatewayName=_UnitRegistrationsGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,700,1,250),_UnitRegistrationsGatewayName_Type())
unitRegistrationsGatewayName.setMaxAccess(_B)
if mibBuilder.loadTexts:unitRegistrationsGatewayName.setStatus(_A)
class _UnitRegistrationsDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_L,10)))
_UnitRegistrationsDelete_Type.__name__=_C
_UnitRegistrationsDelete_Object=MibTableColumn
unitRegistrationsDelete=_UnitRegistrationsDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,700,1,300),_UnitRegistrationsDelete_Type())
unitRegistrationsDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:unitRegistrationsDelete.setStatus(_A)
class _BehaviorOnInitialRegistrationReception_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('noRegistration',100),('endpointRegistration',200),('unitRegistration',300),('unitAndEndpointRegistration',400)))
_BehaviorOnInitialRegistrationReception_Type.__name__=_C
_BehaviorOnInitialRegistrationReception_Object=MibScalar
behaviorOnInitialRegistrationReception=_BehaviorOnInitialRegistrationReception_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,900),_BehaviorOnInitialRegistrationReception_Type())
behaviorOnInitialRegistrationReception.setMaxAccess(_B)
if mibBuilder.loadTexts:behaviorOnInitialRegistrationReception.setStatus(_A)
class _RegistrationDelayOnInitialRegistrationReception_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_RegistrationDelayOnInitialRegistrationReception_Type.__name__=_F
_RegistrationDelayOnInitialRegistrationReception_Object=MibScalar
registrationDelayOnInitialRegistrationReception=_RegistrationDelayOnInitialRegistrationReception_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,1000),_RegistrationDelayOnInitialRegistrationReception_Type())
registrationDelayOnInitialRegistrationReception.setMaxAccess(_B)
if mibBuilder.loadTexts:registrationDelayOnInitialRegistrationReception.setStatus(_A)
_RegistrationStatusTable_Object=MibTable
registrationStatusTable=_RegistrationStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000))
if mibBuilder.loadTexts:registrationStatusTable.setStatus(_A)
_RegistrationStatusEntry_Object=MibTableRow
registrationStatusEntry=_RegistrationStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1))
registrationStatusEntry.setIndexNames((0,_H,_d))
if mibBuilder.loadTexts:registrationStatusEntry.setStatus(_A)
_RegistrationStatusIndex_Type=Unsigned32
_RegistrationStatusIndex_Object=MibTableColumn
registrationStatusIndex=_RegistrationStatusIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1,100),_RegistrationStatusIndex_Type())
registrationStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:registrationStatusIndex.setStatus(_A)
_RegistrationStatusGateway_Type=OctetString
_RegistrationStatusGateway_Object=MibTableColumn
registrationStatusGateway=_RegistrationStatusGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1,200),_RegistrationStatusGateway_Type())
registrationStatusGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:registrationStatusGateway.setStatus(_A)
_RegistrationStatusEndpoint_Type=OctetString
_RegistrationStatusEndpoint_Object=MibTableColumn
registrationStatusEndpoint=_RegistrationStatusEndpoint_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1,300),_RegistrationStatusEndpoint_Type())
registrationStatusEndpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:registrationStatusEndpoint.setStatus(_A)
class _RegistrationStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000)));namedValues=NamedValues(*(('unregistered',100),('registering',200),('registered',300),(_e,400),('unregistering',500),(_f,600),(_g,700),(_N,800),(_h,900),(_i,1000)))
_RegistrationStatusState_Type.__name__=_C
_RegistrationStatusState_Object=MibTableColumn
registrationStatusState=_RegistrationStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1,400),_RegistrationStatusState_Type())
registrationStatusState.setMaxAccess(_E)
if mibBuilder.loadTexts:registrationStatusState.setStatus(_A)
_RegistrationStatusRegistrar_Type=OctetString
_RegistrationStatusRegistrar_Object=MibTableColumn
registrationStatusRegistrar=_RegistrationStatusRegistrar_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1,500),_RegistrationStatusRegistrar_Type())
registrationStatusRegistrar.setMaxAccess(_E)
if mibBuilder.loadTexts:registrationStatusRegistrar.setStatus(_A)
_RegistrationStatusUsername_Type=OctetString
_RegistrationStatusUsername_Object=MibTableColumn
registrationStatusUsername=_RegistrationStatusUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,800,10000,1,600),_RegistrationStatusUsername_Type())
registrationStatusUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:registrationStatusUsername.setStatus(_A)
_TransportGroup_ObjectIdentity=ObjectIdentity
transportGroup=_TransportGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900))
class _TransportPersistentBasePort_Type(Unsigned32):defaultValue=16000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,64535))
_TransportPersistentBasePort_Type.__name__=_F
_TransportPersistentBasePort_Object=MibScalar
transportPersistentBasePort=_TransportPersistentBasePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,50),_TransportPersistentBasePort_Type())
transportPersistentBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:transportPersistentBasePort.setStatus(_A)
class _TransportPersistentPortInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,1000))
_TransportPersistentPortInterval_Type.__name__=_F
_TransportPersistentPortInterval_Object=MibScalar
transportPersistentPortInterval=_TransportPersistentPortInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,55),_TransportPersistentPortInterval_Type())
transportPersistentPortInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:transportPersistentPortInterval.setStatus(_A)
class _TransportFailbackInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_TransportFailbackInterval_Type.__name__=_F
_TransportFailbackInterval_Object=MibScalar
transportFailbackInterval=_TransportFailbackInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,75),_TransportFailbackInterval_Type())
transportFailbackInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:transportFailbackInterval.setStatus(_A)
class _TransportTlsCertificateTrustLevel_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('locallyTrusted',100),('ocspOptional',200),('ocspMandatory',300)))
_TransportTlsCertificateTrustLevel_Type.__name__=_C
_TransportTlsCertificateTrustLevel_Object=MibScalar
transportTlsCertificateTrustLevel=_TransportTlsCertificateTrustLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,85),_TransportTlsCertificateTrustLevel_Type())
transportTlsCertificateTrustLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:transportTlsCertificateTrustLevel.setStatus(_A)
class _TransportTlsCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_TransportTlsCipherSuite_Type.__name__=_C
_TransportTlsCipherSuite_Object=MibScalar
transportTlsCipherSuite=_TransportTlsCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,90),_TransportTlsCipherSuite_Type())
transportTlsCipherSuite.setMaxAccess(_B)
if mibBuilder.loadTexts:transportTlsCipherSuite.setStatus(_A)
class _TransportTlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),('tLSv1-1',300),('tLSv1-2',400)))
_TransportTlsVersion_Type.__name__=_C
_TransportTlsVersion_Object=MibScalar
transportTlsVersion=_TransportTlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,95),_TransportTlsVersion_Type())
transportTlsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:transportTlsVersion.setStatus(_A)
_TransportConfigTable_Object=MibTable
transportConfigTable=_TransportConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100))
if mibBuilder.loadTexts:transportConfigTable.setStatus(_A)
_TransportConfigEntry_Object=MibTableRow
transportConfigEntry=_TransportConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1))
transportConfigEntry.setIndexNames((0,_H,_j))
if mibBuilder.loadTexts:transportConfigEntry.setStatus(_A)
_TransportConfigGatewayName_Type=OctetString
_TransportConfigGatewayName_Object=MibTableColumn
transportConfigGatewayName=_TransportConfigGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,100),_TransportConfigGatewayName_Type())
transportConfigGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:transportConfigGatewayName.setStatus(_A)
class _TransportConfigRegistrationEnable_Type(MxEnableState):defaultValue=0
_TransportConfigRegistrationEnable_Type.__name__=_D
_TransportConfigRegistrationEnable_Object=MibTableColumn
transportConfigRegistrationEnable=_TransportConfigRegistrationEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,200),_TransportConfigRegistrationEnable_Type())
transportConfigRegistrationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigRegistrationEnable.setStatus(_A)
class _TransportConfigContactEnable_Type(MxEnableState):defaultValue=0
_TransportConfigContactEnable_Type.__name__=_D
_TransportConfigContactEnable_Object=MibTableColumn
transportConfigContactEnable=_TransportConfigContactEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,300),_TransportConfigContactEnable_Type())
transportConfigContactEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigContactEnable.setStatus(_A)
class _TransportConfigUdpEnable_Type(MxEnableState):defaultValue=1
_TransportConfigUdpEnable_Type.__name__=_D
_TransportConfigUdpEnable_Object=MibTableColumn
transportConfigUdpEnable=_TransportConfigUdpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,400),_TransportConfigUdpEnable_Type())
transportConfigUdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigUdpEnable.setStatus(_A)
class _TransportConfigUdpQValue_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_TransportConfigUdpQValue_Type.__name__=_G
_TransportConfigUdpQValue_Object=MibTableColumn
transportConfigUdpQValue=_TransportConfigUdpQValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,500),_TransportConfigUdpQValue_Type())
transportConfigUdpQValue.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigUdpQValue.setStatus(_A)
class _TransportConfigTcpEnable_Type(MxEnableState):defaultValue=0
_TransportConfigTcpEnable_Type.__name__=_D
_TransportConfigTcpEnable_Object=MibTableColumn
transportConfigTcpEnable=_TransportConfigTcpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,600),_TransportConfigTcpEnable_Type())
transportConfigTcpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigTcpEnable.setStatus(_A)
class _TransportConfigTcpQValue_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_TransportConfigTcpQValue_Type.__name__=_G
_TransportConfigTcpQValue_Object=MibTableColumn
transportConfigTcpQValue=_TransportConfigTcpQValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,700),_TransportConfigTcpQValue_Type())
transportConfigTcpQValue.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigTcpQValue.setStatus(_A)
class _TransportConfigTlsEnable_Type(MxEnableState):defaultValue=0
_TransportConfigTlsEnable_Type.__name__=_D
_TransportConfigTlsEnable_Object=MibTableColumn
transportConfigTlsEnable=_TransportConfigTlsEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,800),_TransportConfigTlsEnable_Type())
transportConfigTlsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigTlsEnable.setStatus(_A)
class _TransportConfigTlsQValue_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_TransportConfigTlsQValue_Type.__name__=_G
_TransportConfigTlsQValue_Object=MibTableColumn
transportConfigTlsQValue=_TransportConfigTlsQValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,100,1,900),_TransportConfigTlsQValue_Type())
transportConfigTlsQValue.setMaxAccess(_B)
if mibBuilder.loadTexts:transportConfigTlsQValue.setStatus(_A)
_TlsPersistentConnectionStatusTable_Object=MibTable
tlsPersistentConnectionStatusTable=_TlsPersistentConnectionStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000))
if mibBuilder.loadTexts:tlsPersistentConnectionStatusTable.setStatus(_A)
_TlsPersistentConnectionStatusEntry_Object=MibTableRow
tlsPersistentConnectionStatusEntry=_TlsPersistentConnectionStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1))
tlsPersistentConnectionStatusEntry.setIndexNames((0,_H,_k))
if mibBuilder.loadTexts:tlsPersistentConnectionStatusEntry.setStatus(_A)
_TlsPersistentConnectionStatusIndex_Type=Unsigned32
_TlsPersistentConnectionStatusIndex_Object=MibTableColumn
tlsPersistentConnectionStatusIndex=_TlsPersistentConnectionStatusIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1,100),_TlsPersistentConnectionStatusIndex_Type())
tlsPersistentConnectionStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusIndex.setStatus(_A)
_TlsPersistentConnectionStatusGateway_Type=OctetString
_TlsPersistentConnectionStatusGateway_Object=MibTableColumn
tlsPersistentConnectionStatusGateway=_TlsPersistentConnectionStatusGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1,200),_TlsPersistentConnectionStatusGateway_Type())
tlsPersistentConnectionStatusGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusGateway.setStatus(_A)
_TlsPersistentConnectionStatusLocalPort_Type=MxAdvancedIpPort
_TlsPersistentConnectionStatusLocalPort_Object=MibTableColumn
tlsPersistentConnectionStatusLocalPort=_TlsPersistentConnectionStatusLocalPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1,300),_TlsPersistentConnectionStatusLocalPort_Type())
tlsPersistentConnectionStatusLocalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusLocalPort.setStatus(_A)
_TlsPersistentConnectionStatusRemoteHost_Type=OctetString
_TlsPersistentConnectionStatusRemoteHost_Object=MibTableColumn
tlsPersistentConnectionStatusRemoteHost=_TlsPersistentConnectionStatusRemoteHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1,400),_TlsPersistentConnectionStatusRemoteHost_Type())
tlsPersistentConnectionStatusRemoteHost.setMaxAccess(_E)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusRemoteHost.setStatus(_A)
_TlsPersistentConnectionStatusRemoteHostIpAddr_Type=OctetString
_TlsPersistentConnectionStatusRemoteHostIpAddr_Object=MibTableColumn
tlsPersistentConnectionStatusRemoteHostIpAddr=_TlsPersistentConnectionStatusRemoteHostIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1,450),_TlsPersistentConnectionStatusRemoteHostIpAddr_Type())
tlsPersistentConnectionStatusRemoteHostIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusRemoteHostIpAddr.setStatus(_A)
class _TlsPersistentConnectionStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('up',100),('down',200),('waitingShutdown',300),('waitingUp',400)))
_TlsPersistentConnectionStatusState_Type.__name__=_C
_TlsPersistentConnectionStatusState_Object=MibTableColumn
tlsPersistentConnectionStatusState=_TlsPersistentConnectionStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,900,10000,1,500),_TlsPersistentConnectionStatusState_Type())
tlsPersistentConnectionStatusState.setMaxAccess(_E)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusState.setStatus(_A)
_FailoverGroup_ObjectIdentity=ObjectIdentity
failoverGroup=_FailoverGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930))
class _DefaultSipFailoverConditions_Type(OctetString):defaultValue=OctetString(_l);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_DefaultSipFailoverConditions_Type.__name__=_G
_DefaultSipFailoverConditions_Object=MibScalar
defaultSipFailoverConditions=_DefaultSipFailoverConditions_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930,100),_DefaultSipFailoverConditions_Type())
defaultSipFailoverConditions.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSipFailoverConditions.setStatus(_A)
_GwSpecificFailoverTable_Object=MibTable
gwSpecificFailoverTable=_GwSpecificFailoverTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930,500))
if mibBuilder.loadTexts:gwSpecificFailoverTable.setStatus(_A)
_GwSpecificFailoverEntry_Object=MibTableRow
gwSpecificFailoverEntry=_GwSpecificFailoverEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930,500,1))
gwSpecificFailoverEntry.setIndexNames((0,_H,_m))
if mibBuilder.loadTexts:gwSpecificFailoverEntry.setStatus(_A)
_GwSpecificFailoverGatewayName_Type=OctetString
_GwSpecificFailoverGatewayName_Object=MibTableColumn
gwSpecificFailoverGatewayName=_GwSpecificFailoverGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930,500,1,100),_GwSpecificFailoverGatewayName_Type())
gwSpecificFailoverGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwSpecificFailoverGatewayName.setStatus(_A)
class _GwSpecificFailoverEnableConfig_Type(MxEnableState):defaultValue=0
_GwSpecificFailoverEnableConfig_Type.__name__=_D
_GwSpecificFailoverEnableConfig_Object=MibTableColumn
gwSpecificFailoverEnableConfig=_GwSpecificFailoverEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930,500,1,200),_GwSpecificFailoverEnableConfig_Type())
gwSpecificFailoverEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificFailoverEnableConfig.setStatus(_A)
class _GwSpecificFailoverSipFailoverConditions_Type(OctetString):defaultValue=OctetString(_l);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_GwSpecificFailoverSipFailoverConditions_Type.__name__=_G
_GwSpecificFailoverSipFailoverConditions_Object=MibTableColumn
gwSpecificFailoverSipFailoverConditions=_GwSpecificFailoverSipFailoverConditions_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,930,500,1,300),_GwSpecificFailoverSipFailoverConditions_Type())
gwSpecificFailoverSipFailoverConditions.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificFailoverSipFailoverConditions.setStatus(_A)
_PenaltyBoxGroup_ObjectIdentity=ObjectIdentity
penaltyBoxGroup=_PenaltyBoxGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1000))
class _PenaltyBoxEnable_Type(MxEnableState):defaultValue=0
_PenaltyBoxEnable_Type.__name__=_D
_PenaltyBoxEnable_Object=MibScalar
penaltyBoxEnable=_PenaltyBoxEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1000,100),_PenaltyBoxEnable_Type())
penaltyBoxEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:penaltyBoxEnable.setStatus(_A)
class _PenaltyBoxTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,7200))
_PenaltyBoxTime_Type.__name__=_F
_PenaltyBoxTime_Object=MibScalar
penaltyBoxTime=_PenaltyBoxTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1000,200),_PenaltyBoxTime_Type())
penaltyBoxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:penaltyBoxTime.setStatus(_A)
_ErrorMappingGroup_ObjectIdentity=ObjectIdentity
errorMappingGroup=_ErrorMappingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100))
_ErrorMappingSipToCauseTable_Object=MibTable
errorMappingSipToCauseTable=_ErrorMappingSipToCauseTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,100))
if mibBuilder.loadTexts:errorMappingSipToCauseTable.setStatus(_A)
_ErrorMappingSipToCauseEntry_Object=MibTableRow
errorMappingSipToCauseEntry=_ErrorMappingSipToCauseEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,100,1))
errorMappingSipToCauseEntry.setIndexNames((0,_H,_n))
if mibBuilder.loadTexts:errorMappingSipToCauseEntry.setStatus(_A)
class _ErrorMappingSipToCauseSipCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,699))
_ErrorMappingSipToCauseSipCode_Type.__name__=_F
_ErrorMappingSipToCauseSipCode_Object=MibTableColumn
errorMappingSipToCauseSipCode=_ErrorMappingSipToCauseSipCode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,100,1,100),_ErrorMappingSipToCauseSipCode_Type())
errorMappingSipToCauseSipCode.setMaxAccess(_E)
if mibBuilder.loadTexts:errorMappingSipToCauseSipCode.setStatus(_A)
class _ErrorMappingSipToCauseCause_Type(Unsigned32):defaultValue=127;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ErrorMappingSipToCauseCause_Type.__name__=_F
_ErrorMappingSipToCauseCause_Object=MibTableColumn
errorMappingSipToCauseCause=_ErrorMappingSipToCauseCause_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,100,1,200),_ErrorMappingSipToCauseCause_Type())
errorMappingSipToCauseCause.setMaxAccess(_B)
if mibBuilder.loadTexts:errorMappingSipToCauseCause.setStatus(_A)
class _ErrorMappingSipToCauseDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_L,10)))
_ErrorMappingSipToCauseDelete_Type.__name__=_C
_ErrorMappingSipToCauseDelete_Object=MibTableColumn
errorMappingSipToCauseDelete=_ErrorMappingSipToCauseDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,100,1,300),_ErrorMappingSipToCauseDelete_Type())
errorMappingSipToCauseDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:errorMappingSipToCauseDelete.setStatus(_A)
_ErrorMappingCauseToSipTable_Object=MibTable
errorMappingCauseToSipTable=_ErrorMappingCauseToSipTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,300))
if mibBuilder.loadTexts:errorMappingCauseToSipTable.setStatus(_A)
_ErrorMappingCauseToSipEntry_Object=MibTableRow
errorMappingCauseToSipEntry=_ErrorMappingCauseToSipEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,300,1))
errorMappingCauseToSipEntry.setIndexNames((0,_H,_o))
if mibBuilder.loadTexts:errorMappingCauseToSipEntry.setStatus(_A)
class _ErrorMappingCauseToSipCause_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_ErrorMappingCauseToSipCause_Type.__name__=_F
_ErrorMappingCauseToSipCause_Object=MibTableColumn
errorMappingCauseToSipCause=_ErrorMappingCauseToSipCause_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,300,1,100),_ErrorMappingCauseToSipCause_Type())
errorMappingCauseToSipCause.setMaxAccess(_E)
if mibBuilder.loadTexts:errorMappingCauseToSipCause.setStatus(_A)
class _ErrorMappingCauseToSipSipCode_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,699))
_ErrorMappingCauseToSipSipCode_Type.__name__=_F
_ErrorMappingCauseToSipSipCode_Object=MibTableColumn
errorMappingCauseToSipSipCode=_ErrorMappingCauseToSipSipCode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,300,1,200),_ErrorMappingCauseToSipSipCode_Type())
errorMappingCauseToSipSipCode.setMaxAccess(_B)
if mibBuilder.loadTexts:errorMappingCauseToSipSipCode.setStatus(_A)
class _ErrorMappingCauseToSipDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_J,0),(_L,10)))
_ErrorMappingCauseToSipDelete_Type.__name__=_C
_ErrorMappingCauseToSipDelete_Object=MibTableColumn
errorMappingCauseToSipDelete=_ErrorMappingCauseToSipDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,300,1,300),_ErrorMappingCauseToSipDelete_Type())
errorMappingCauseToSipDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:errorMappingCauseToSipDelete.setStatus(_A)
class _ReasonHeaderSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_K,100),('sendQ850',200),('receiveQ850',300),('sendReceiveQ850',400)))
_ReasonHeaderSupport_Type.__name__=_C
_ReasonHeaderSupport_Object=MibScalar
reasonHeaderSupport=_ReasonHeaderSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1100,500),_ReasonHeaderSupport_Type())
reasonHeaderSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:reasonHeaderSupport.setStatus(_A)
_SipKeepAliveGroup_ObjectIdentity=ObjectIdentity
sipKeepAliveGroup=_SipKeepAliveGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300))
class _SipKeepAliveMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_K,100),('sipOptions',200),('ping',300),('tcpKeepAlive',400)))
_SipKeepAliveMethod_Type.__name__=_C
_SipKeepAliveMethod_Object=MibScalar
sipKeepAliveMethod=_SipKeepAliveMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,100),_SipKeepAliveMethod_Type())
sipKeepAliveMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:sipKeepAliveMethod.setStatus(_A)
class _SipKeepAliveInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_SipKeepAliveInterval_Type.__name__=_F
_SipKeepAliveInterval_Object=MibScalar
sipKeepAliveInterval=_SipKeepAliveInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,200),_SipKeepAliveInterval_Type())
sipKeepAliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sipKeepAliveInterval.setStatus(_A)
class _SipKeepAliveRetry_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SipKeepAliveRetry_Type.__name__=_F
_SipKeepAliveRetry_Object=MibScalar
sipKeepAliveRetry=_SipKeepAliveRetry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,210),_SipKeepAliveRetry_Type())
sipKeepAliveRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:sipKeepAliveRetry.setStatus(_A)
class _SipKeepAliveDestination_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('firstSipDestination',100),('alternateDestination',200)))
_SipKeepAliveDestination_Type.__name__=_C
_SipKeepAliveDestination_Object=MibScalar
sipKeepAliveDestination=_SipKeepAliveDestination_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,300),_SipKeepAliveDestination_Type())
sipKeepAliveDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:sipKeepAliveDestination.setStatus(_A)
_GwKeepAliveAlternateDestinationTable_Object=MibTable
gwKeepAliveAlternateDestinationTable=_GwKeepAliveAlternateDestinationTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,400))
if mibBuilder.loadTexts:gwKeepAliveAlternateDestinationTable.setStatus(_A)
_GwKeepAliveAlternateDestinationEntry_Object=MibTableRow
gwKeepAliveAlternateDestinationEntry=_GwKeepAliveAlternateDestinationEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,400,1))
gwKeepAliveAlternateDestinationEntry.setIndexNames((0,_H,_p))
if mibBuilder.loadTexts:gwKeepAliveAlternateDestinationEntry.setStatus(_A)
_GwKeepAliveAlternateDestinationGatewayName_Type=OctetString
_GwKeepAliveAlternateDestinationGatewayName_Object=MibTableColumn
gwKeepAliveAlternateDestinationGatewayName=_GwKeepAliveAlternateDestinationGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,400,1,100),_GwKeepAliveAlternateDestinationGatewayName_Type())
gwKeepAliveAlternateDestinationGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwKeepAliveAlternateDestinationGatewayName.setStatus(_A)
class _GwKeepAliveAlternateDestinationAlternateDestination_Type(MxIpHostNamePort):defaultValue=OctetString(_R)
_GwKeepAliveAlternateDestinationAlternateDestination_Type.__name__=_I
_GwKeepAliveAlternateDestinationAlternateDestination_Object=MibTableColumn
gwKeepAliveAlternateDestinationAlternateDestination=_GwKeepAliveAlternateDestinationAlternateDestination_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1300,400,1,200),_GwKeepAliveAlternateDestinationAlternateDestination_Type())
gwKeepAliveAlternateDestinationAlternateDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:gwKeepAliveAlternateDestinationAlternateDestination.setStatus(_A)
_PrackGroup_ObjectIdentity=ObjectIdentity
prackGroup=_PrackGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1400))
class _UasPrackSupport_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300)));namedValues=NamedValues(*((_O,200),(_q,300)))
_UasPrackSupport_Type.__name__=_C
_UasPrackSupport_Object=MibScalar
uasPrackSupport=_UasPrackSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1400,100),_UasPrackSupport_Type())
uasPrackSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:uasPrackSupport.setStatus(_A)
class _UacPrackSupport_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300,400)));namedValues=NamedValues(*((_O,200),(_q,300),('required',400)))
_UacPrackSupport_Type.__name__=_C
_UacPrackSupport_Object=MibScalar
uacPrackSupport=_UacPrackSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1400,200),_UacPrackSupport_Type())
uacPrackSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:uacPrackSupport.setStatus(_A)
_OfferAnswerGroup_ObjectIdentity=ObjectIdentity
offerAnswerGroup=_OfferAnswerGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1500))
class _AnswerCodecNegotiation_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('allCommonLocalPriority',100),('firstCommonLocalPriority',200),('allCommonPeerPriority',300),('firstCommonPeerPriority',400)))
_AnswerCodecNegotiation_Type.__name__=_C
_AnswerCodecNegotiation_Object=MibScalar
answerCodecNegotiation=_AnswerCodecNegotiation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1500,100),_AnswerCodecNegotiation_Type())
answerCodecNegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:answerCodecNegotiation.setStatus(_A)
_DiversionGroup_ObjectIdentity=ObjectIdentity
diversionGroup=_DiversionGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1600))
_DiversionConfigTable_Object=MibTable
diversionConfigTable=_DiversionConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1600,100))
if mibBuilder.loadTexts:diversionConfigTable.setStatus(_A)
_DiversionConfigEntry_Object=MibTableRow
diversionConfigEntry=_DiversionConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1600,100,1))
diversionConfigEntry.setIndexNames((0,_H,_r))
if mibBuilder.loadTexts:diversionConfigEntry.setStatus(_A)
_DiversionConfigGatewayName_Type=OctetString
_DiversionConfigGatewayName_Object=MibTableColumn
diversionConfigGatewayName=_DiversionConfigGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1600,100,1,100),_DiversionConfigGatewayName_Type())
diversionConfigGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:diversionConfigGatewayName.setStatus(_A)
class _DiversionConfigMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),('diversionHeader',200)))
_DiversionConfigMethod_Type.__name__=_C
_DiversionConfigMethod_Object=MibTableColumn
diversionConfigMethod=_DiversionConfigMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1600,100,1,200),_DiversionConfigMethod_Type())
diversionConfigMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:diversionConfigMethod.setStatus(_A)
_DnsGroup_ObjectIdentity=ObjectIdentity
dnsGroup=_DnsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1700))
class _SupportedDnsQueries_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('address',100),('srv',200),('naptr',300)))
_SupportedDnsQueries_Type.__name__=_C
_SupportedDnsQueries_Object=MibScalar
supportedDnsQueries=_SupportedDnsQueries_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1700,100),_SupportedDnsQueries_Type())
supportedDnsQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:supportedDnsQueries.setStatus(_A)
class _DnsFailureConcealment_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,300)));namedValues=NamedValues(*((_K,100),('onNoResolution',300)))
_DnsFailureConcealment_Type.__name__=_C
_DnsFailureConcealment_Object=MibScalar
dnsFailureConcealment=_DnsFailureConcealment_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1700,200),_DnsFailureConcealment_Type())
dnsFailureConcealment.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsFailureConcealment.setStatus(_A)
class _DnsIpVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('ipV4Only',100),('ipV4Preferred',200)))
_DnsIpVersion_Type.__name__=_C
_DnsIpVersion_Object=MibScalar
dnsIpVersion=_DnsIpVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1700,300),_DnsIpVersion_Type())
dnsIpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsIpVersion.setStatus(_A)
_MessageWaitingIndication_ObjectIdentity=ObjectIdentity
messageWaitingIndication=_MessageWaitingIndication_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800))
class _DefaultStaticMessagingHost_Type(MxIpHostNamePort):defaultValue=OctetString(_M)
_DefaultStaticMessagingHost_Type.__name__=_I
_DefaultStaticMessagingHost_Object=MibScalar
defaultStaticMessagingHost=_DefaultStaticMessagingHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,100),_DefaultStaticMessagingHost_Type())
defaultStaticMessagingHost.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticMessagingHost.setStatus(_A)
class _DefaultUsernameInRequestUriEnable_Type(MxEnableState):defaultValue=0
_DefaultUsernameInRequestUriEnable_Type.__name__=_D
_DefaultUsernameInRequestUriEnable_Object=MibScalar
defaultUsernameInRequestUriEnable=_DefaultUsernameInRequestUriEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,110),_DefaultUsernameInRequestUriEnable_Type())
defaultUsernameInRequestUriEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultUsernameInRequestUriEnable.setStatus(_A)
_GwSpecificMwiTable_Object=MibTable
gwSpecificMwiTable=_GwSpecificMwiTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,200))
if mibBuilder.loadTexts:gwSpecificMwiTable.setStatus(_A)
_GwSpecificMwiEntry_Object=MibTableRow
gwSpecificMwiEntry=_GwSpecificMwiEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,200,1))
gwSpecificMwiEntry.setIndexNames((0,_H,_s))
if mibBuilder.loadTexts:gwSpecificMwiEntry.setStatus(_A)
_GwSpecificMwiGatewayName_Type=OctetString
_GwSpecificMwiGatewayName_Object=MibTableColumn
gwSpecificMwiGatewayName=_GwSpecificMwiGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,200,1,100),_GwSpecificMwiGatewayName_Type())
gwSpecificMwiGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwSpecificMwiGatewayName.setStatus(_A)
class _GwSpecificMwiEnableConfig_Type(MxEnableState):defaultValue=0
_GwSpecificMwiEnableConfig_Type.__name__=_D
_GwSpecificMwiEnableConfig_Object=MibTableColumn
gwSpecificMwiEnableConfig=_GwSpecificMwiEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,200,1,200),_GwSpecificMwiEnableConfig_Type())
gwSpecificMwiEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificMwiEnableConfig.setStatus(_A)
class _GwSpecificMwiMessagingHost_Type(MxIpHostNamePort):defaultValue=OctetString(_M)
_GwSpecificMwiMessagingHost_Type.__name__=_I
_GwSpecificMwiMessagingHost_Object=MibTableColumn
gwSpecificMwiMessagingHost=_GwSpecificMwiMessagingHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,200,1,300),_GwSpecificMwiMessagingHost_Type())
gwSpecificMwiMessagingHost.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificMwiMessagingHost.setStatus(_A)
class _GwSpecificMwiUsernameInRequestUriEnable_Type(MxEnableState):defaultValue=0
_GwSpecificMwiUsernameInRequestUriEnable_Type.__name__=_D
_GwSpecificMwiUsernameInRequestUriEnable_Object=MibTableColumn
gwSpecificMwiUsernameInRequestUriEnable=_GwSpecificMwiUsernameInRequestUriEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,200,1,400),_GwSpecificMwiUsernameInRequestUriEnable_Type())
gwSpecificMwiUsernameInRequestUriEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificMwiUsernameInRequestUriEnable.setStatus(_A)
_MwiStatusTable_Object=MibTable
mwiStatusTable=_MwiStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300))
if mibBuilder.loadTexts:mwiStatusTable.setStatus(_A)
_MwiStatusEntry_Object=MibTableRow
mwiStatusEntry=_MwiStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1))
mwiStatusEntry.setIndexNames((0,_H,_t))
if mibBuilder.loadTexts:mwiStatusEntry.setStatus(_A)
_MwiStatusIndex_Type=Unsigned32
_MwiStatusIndex_Object=MibTableColumn
mwiStatusIndex=_MwiStatusIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1,100),_MwiStatusIndex_Type())
mwiStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mwiStatusIndex.setStatus(_A)
_MwiStatusGatewayName_Type=OctetString
_MwiStatusGatewayName_Object=MibTableColumn
mwiStatusGatewayName=_MwiStatusGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1,200),_MwiStatusGatewayName_Type())
mwiStatusGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:mwiStatusGatewayName.setStatus(_A)
class _MwiStatusSubscriptionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100)));namedValues=NamedValues(*(('unsubscribed',100),('subscribing',200),('subscribed',300),(_e,400),('unsubscribing',500),(_f,600),(_g,700),(_N,800),(_h,900),(_i,1000),('error',1100)))
_MwiStatusSubscriptionState_Type.__name__=_C
_MwiStatusSubscriptionState_Object=MibTableColumn
mwiStatusSubscriptionState=_MwiStatusSubscriptionState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1,300),_MwiStatusSubscriptionState_Type())
mwiStatusSubscriptionState.setMaxAccess(_E)
if mibBuilder.loadTexts:mwiStatusSubscriptionState.setStatus(_A)
_MwiStatusEndpoint_Type=OctetString
_MwiStatusEndpoint_Object=MibTableColumn
mwiStatusEndpoint=_MwiStatusEndpoint_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1,400),_MwiStatusEndpoint_Type())
mwiStatusEndpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:mwiStatusEndpoint.setStatus(_A)
_MwiStatusMessagingHost_Type=OctetString
_MwiStatusMessagingHost_Object=MibTableColumn
mwiStatusMessagingHost=_MwiStatusMessagingHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1,500),_MwiStatusMessagingHost_Type())
mwiStatusMessagingHost.setMaxAccess(_E)
if mibBuilder.loadTexts:mwiStatusMessagingHost.setStatus(_A)
_MwiStatusUsername_Type=OctetString
_MwiStatusUsername_Object=MibTableColumn
mwiStatusUsername=_MwiStatusUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1800,300,1,600),_MwiStatusUsername_Type())
mwiStatusUsername.setMaxAccess(_E)
if mibBuilder.loadTexts:mwiStatusUsername.setStatus(_A)
_ConferenceGroup_ObjectIdentity=ObjectIdentity
conferenceGroup=_ConferenceGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900))
class _DefaultStaticConferenceServerUri_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DefaultStaticConferenceServerUri_Type.__name__=_G
_DefaultStaticConferenceServerUri_Object=MibScalar
defaultStaticConferenceServerUri=_DefaultStaticConferenceServerUri_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900,100),_DefaultStaticConferenceServerUri_Type())
defaultStaticConferenceServerUri.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticConferenceServerUri.setStatus(_A)
_GwSpecificConferenceTable_Object=MibTable
gwSpecificConferenceTable=_GwSpecificConferenceTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900,1000))
if mibBuilder.loadTexts:gwSpecificConferenceTable.setStatus(_A)
_GwSpecificConferenceEntry_Object=MibTableRow
gwSpecificConferenceEntry=_GwSpecificConferenceEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900,1000,1))
gwSpecificConferenceEntry.setIndexNames((0,_H,_u))
if mibBuilder.loadTexts:gwSpecificConferenceEntry.setStatus(_A)
_GwSpecificConferenceGatewayName_Type=OctetString
_GwSpecificConferenceGatewayName_Object=MibTableColumn
gwSpecificConferenceGatewayName=_GwSpecificConferenceGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900,1000,1,100),_GwSpecificConferenceGatewayName_Type())
gwSpecificConferenceGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwSpecificConferenceGatewayName.setStatus(_A)
class _GwSpecificConferenceEnableConfig_Type(MxEnableState):defaultValue=0
_GwSpecificConferenceEnableConfig_Type.__name__=_D
_GwSpecificConferenceEnableConfig_Object=MibTableColumn
gwSpecificConferenceEnableConfig=_GwSpecificConferenceEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900,1000,1,200),_GwSpecificConferenceEnableConfig_Type())
gwSpecificConferenceEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificConferenceEnableConfig.setStatus(_A)
class _GwSpecificConferenceServerUri_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GwSpecificConferenceServerUri_Type.__name__=_G
_GwSpecificConferenceServerUri_Object=MibTableColumn
gwSpecificConferenceServerUri=_GwSpecificConferenceServerUri_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,1900,1000,1,300),_GwSpecificConferenceServerUri_Type())
gwSpecificConferenceServerUri.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificConferenceServerUri.setStatus(_A)
_PriorityGroup_ObjectIdentity=ObjectIdentity
priorityGroup=_PriorityGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2000))
class _DefaultOutboundPriorityCallRouting_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('normal',100),('skipOutboundProxy',200)))
_DefaultOutboundPriorityCallRouting_Type.__name__=_C
_DefaultOutboundPriorityCallRouting_Object=MibScalar
defaultOutboundPriorityCallRouting=_DefaultOutboundPriorityCallRouting_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2000,100),_DefaultOutboundPriorityCallRouting_Type())
defaultOutboundPriorityCallRouting.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultOutboundPriorityCallRouting.setStatus(_A)
_EventHandlingGroup_ObjectIdentity=ObjectIdentity
eventHandlingGroup=_EventHandlingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100))
_GwEventHandlingTable_Object=MibTable
gwEventHandlingTable=_GwEventHandlingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100,100))
if mibBuilder.loadTexts:gwEventHandlingTable.setStatus(_A)
_GwEventHandlingEntry_Object=MibTableRow
gwEventHandlingEntry=_GwEventHandlingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100,100,1))
gwEventHandlingEntry.setIndexNames((0,_H,_v))
if mibBuilder.loadTexts:gwEventHandlingEntry.setStatus(_A)
_GwEventHandlingGatewayName_Type=OctetString
_GwEventHandlingGatewayName_Object=MibTableColumn
gwEventHandlingGatewayName=_GwEventHandlingGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100,100,1,100),_GwEventHandlingGatewayName_Type())
gwEventHandlingGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwEventHandlingGatewayName.setStatus(_A)
class _GwEventHandlingReboot_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_N,100),('restart',200)))
_GwEventHandlingReboot_Type.__name__=_C
_GwEventHandlingReboot_Object=MibTableColumn
gwEventHandlingReboot=_GwEventHandlingReboot_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100,100,1,200),_GwEventHandlingReboot_Type())
gwEventHandlingReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:gwEventHandlingReboot.setStatus(_A)
class _GwEventHandlingCheckSync_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_N,100),('transferScript',200),('cwmpInform',300)))
_GwEventHandlingCheckSync_Type.__name__=_C
_GwEventHandlingCheckSync_Object=MibTableColumn
gwEventHandlingCheckSync=_GwEventHandlingCheckSync_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100,100,1,300),_GwEventHandlingCheckSync_Type())
gwEventHandlingCheckSync.setMaxAccess(_B)
if mibBuilder.loadTexts:gwEventHandlingCheckSync.setStatus(_A)
class _SipMessageSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_P,100),('acceptPlainText',200)))
_SipMessageSupport_Type.__name__=_C
_SipMessageSupport_Object=MibScalar
sipMessageSupport=_SipMessageSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2100,200),_SipMessageSupport_Type())
sipMessageSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sipMessageSupport.setStatus(_A)
_TransferGroup_ObjectIdentity=ObjectIdentity
transferGroup=_TransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2200))
class _ReferredByHeader_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),('headerOnly',200)))
_ReferredByHeader_Type.__name__=_C
_ReferredByHeader_Object=MibScalar
referredByHeader=_ReferredByHeader_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2200,100),_ReferredByHeader_Type())
referredByHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:referredByHeader.setStatus(_A)
class _BlindTransferMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('semiAttended',100),('semiAttendedConfirmed',200),('semiAttendedCancelled',300)))
_BlindTransferMethod_Type.__name__=_C
_BlindTransferMethod_Object=MibScalar
blindTransferMethod=_BlindTransferMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2200,200),_BlindTransferMethod_Type())
blindTransferMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:blindTransferMethod.setStatus(_A)
class _ReferToHeaderUriSource_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('aor',100),('contactUri',200)))
_ReferToHeaderUriSource_Type.__name__=_C
_ReferToHeaderUriSource_Object=MibScalar
referToHeaderUriSource=_ReferToHeaderUriSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2200,300),_ReferToHeaderUriSource_Type())
referToHeaderUriSource.setMaxAccess(_B)
if mibBuilder.loadTexts:referToHeaderUriSource.setStatus(_A)
_AocGroup_ObjectIdentity=ObjectIdentity
aocGroup=_AocGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2300))
_AocConfigTable_Object=MibTable
aocConfigTable=_AocConfigTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2300,100))
if mibBuilder.loadTexts:aocConfigTable.setStatus(_A)
_AocConfigEntry_Object=MibTableRow
aocConfigEntry=_AocConfigEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2300,100,1))
aocConfigEntry.setIndexNames((0,_H,_w))
if mibBuilder.loadTexts:aocConfigEntry.setStatus(_A)
_AocConfigGatewayName_Type=OctetString
_AocConfigGatewayName_Object=MibTableColumn
aocConfigGatewayName=_AocConfigGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2300,100,1,100),_AocConfigGatewayName_Type())
aocConfigGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:aocConfigGatewayName.setStatus(_A)
class _AocConfigAocDSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_P,100),(_x,200)))
_AocConfigAocDSupport_Type.__name__=_C
_AocConfigAocDSupport_Object=MibTableColumn
aocConfigAocDSupport=_AocConfigAocDSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2300,100,1,200),_AocConfigAocDSupport_Type())
aocConfigAocDSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:aocConfigAocDSupport.setStatus(_A)
class _AocConfigAocESupport_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_P,100),(_x,200)))
_AocConfigAocESupport_Type.__name__=_C
_AocConfigAocESupport_Object=MibTableColumn
aocConfigAocESupport=_AocConfigAocESupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2300,100,1,300),_AocConfigAocESupport_Type())
aocConfigAocESupport.setMaxAccess(_B)
if mibBuilder.loadTexts:aocConfigAocESupport.setStatus(_A)
_KpmlGroup_ObjectIdentity=ObjectIdentity
kpmlGroup=_KpmlGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2400))
class _UasKpmlSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_O,100),('supportedInDialog',200)))
_UasKpmlSupport_Type.__name__=_C
_UasKpmlSupport_Object=MibScalar
uasKpmlSupport=_UasKpmlSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2400,100),_UasKpmlSupport_Type())
uasKpmlSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:uasKpmlSupport.setStatus(_A)
_SecurityAgreementGroup_ObjectIdentity=ObjectIdentity
securityAgreementGroup=_SecurityAgreementGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2500))
class _MediaSecurityAgreementEnable_Type(MxEnableState):defaultValue=0
_MediaSecurityAgreementEnable_Type.__name__=_D
_MediaSecurityAgreementEnable_Object=MibScalar
mediaSecurityAgreementEnable=_MediaSecurityAgreementEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2500,100),_MediaSecurityAgreementEnable_Type())
mediaSecurityAgreementEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaSecurityAgreementEnable.setStatus(_A)
_PrivacyHeadersGroup_ObjectIdentity=ObjectIdentity
privacyHeadersGroup=_PrivacyHeadersGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2600))
class _PrivacyHeadersInResponse_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_O,100),('supportedPAssertedIdentity',200)))
_PrivacyHeadersInResponse_Type.__name__=_C
_PrivacyHeadersInResponse_Object=MibScalar
privacyHeadersInResponse=_PrivacyHeadersInResponse_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2600,100),_PrivacyHeadersInResponse_Type())
privacyHeadersInResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:privacyHeadersInResponse.setStatus(_A)
_RtcpXrGroup_ObjectIdentity=ObjectIdentity
rtcpXrGroup=_RtcpXrGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700))
class _DefaultStaticRtcpXrCollectorUri_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DefaultStaticRtcpXrCollectorUri_Type.__name__=_G
_DefaultStaticRtcpXrCollectorUri_Object=MibScalar
defaultStaticRtcpXrCollectorUri=_DefaultStaticRtcpXrCollectorUri_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,100),_DefaultStaticRtcpXrCollectorUri_Type())
defaultStaticRtcpXrCollectorUri.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticRtcpXrCollectorUri.setStatus(_A)
class _DefaultRtcpXrPeriodicReportsInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_DefaultRtcpXrPeriodicReportsInterval_Type.__name__=_F
_DefaultRtcpXrPeriodicReportsInterval_Object=MibScalar
defaultRtcpXrPeriodicReportsInterval=_DefaultRtcpXrPeriodicReportsInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,200),_DefaultRtcpXrPeriodicReportsInterval_Type())
defaultRtcpXrPeriodicReportsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRtcpXrPeriodicReportsInterval.setStatus(_A)
_GwSpecificRtcpXrTable_Object=MibTable
gwSpecificRtcpXrTable=_GwSpecificRtcpXrTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,1000))
if mibBuilder.loadTexts:gwSpecificRtcpXrTable.setStatus(_A)
_GwSpecificRtcpXrEntry_Object=MibTableRow
gwSpecificRtcpXrEntry=_GwSpecificRtcpXrEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,1000,1))
gwSpecificRtcpXrEntry.setIndexNames((0,_H,_y))
if mibBuilder.loadTexts:gwSpecificRtcpXrEntry.setStatus(_A)
_GwSpecificRtcpXrGatewayName_Type=OctetString
_GwSpecificRtcpXrGatewayName_Object=MibTableColumn
gwSpecificRtcpXrGatewayName=_GwSpecificRtcpXrGatewayName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,1000,1,100),_GwSpecificRtcpXrGatewayName_Type())
gwSpecificRtcpXrGatewayName.setMaxAccess(_E)
if mibBuilder.loadTexts:gwSpecificRtcpXrGatewayName.setStatus(_A)
class _GwSpecificRtcpXrEnableConfig_Type(MxEnableState):defaultValue=0
_GwSpecificRtcpXrEnableConfig_Type.__name__=_D
_GwSpecificRtcpXrEnableConfig_Object=MibTableColumn
gwSpecificRtcpXrEnableConfig=_GwSpecificRtcpXrEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,1000,1,200),_GwSpecificRtcpXrEnableConfig_Type())
gwSpecificRtcpXrEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRtcpXrEnableConfig.setStatus(_A)
class _GwSpecificRtcpXrCollectorUri_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GwSpecificRtcpXrCollectorUri_Type.__name__=_G
_GwSpecificRtcpXrCollectorUri_Object=MibTableColumn
gwSpecificRtcpXrCollectorUri=_GwSpecificRtcpXrCollectorUri_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,1000,1,300),_GwSpecificRtcpXrCollectorUri_Type())
gwSpecificRtcpXrCollectorUri.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRtcpXrCollectorUri.setStatus(_A)
class _GwSpecificRtcpXrPeriodicReportsInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_GwSpecificRtcpXrPeriodicReportsInterval_Type.__name__=_F
_GwSpecificRtcpXrPeriodicReportsInterval_Object=MibTableColumn
gwSpecificRtcpXrPeriodicReportsInterval=_GwSpecificRtcpXrPeriodicReportsInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,2700,1000,1,400),_GwSpecificRtcpXrPeriodicReportsInterval_Type())
gwSpecificRtcpXrPeriodicReportsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:gwSpecificRtcpXrPeriodicReportsInterval.setStatus(_A)
_InteropGroup_ObjectIdentity=ObjectIdentity
interopGroup=_InteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000))
class _InteropTransmissionTimeout_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_InteropTransmissionTimeout_Type.__name__=_F
_InteropTransmissionTimeout_Object=MibScalar
interopTransmissionTimeout=_InteropTransmissionTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,400),_InteropTransmissionTimeout_Type())
interopTransmissionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:interopTransmissionTimeout.setStatus(_A)
class _InteropTcpConnectTimeout_Type(Unsigned32):defaultValue=127;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_InteropTcpConnectTimeout_Type.__name__=_F
_InteropTcpConnectTimeout_Object=MibScalar
interopTcpConnectTimeout=_InteropTcpConnectTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,450),_InteropTcpConnectTimeout_Type())
interopTcpConnectTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:interopTcpConnectTimeout.setStatus(_A)
class _InteropSymmetricUdpSourcePortEnable_Type(MxEnableState):defaultValue=1
_InteropSymmetricUdpSourcePortEnable_Type.__name__=_D
_InteropSymmetricUdpSourcePortEnable_Object=MibScalar
interopSymmetricUdpSourcePortEnable=_InteropSymmetricUdpSourcePortEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,600),_InteropSymmetricUdpSourcePortEnable_Type())
interopSymmetricUdpSourcePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSymmetricUdpSourcePortEnable.setStatus(_A)
class _InteropMaxForwardsValue_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_InteropMaxForwardsValue_Type.__name__=_C
_InteropMaxForwardsValue_Object=MibScalar
interopMaxForwardsValue=_InteropMaxForwardsValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,700),_InteropMaxForwardsValue_Type())
interopMaxForwardsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:interopMaxForwardsValue.setStatus(_A)
class _InteropSendUaHeaderEnable_Type(MxEnableState):defaultValue=1
_InteropSendUaHeaderEnable_Type.__name__=_D
_InteropSendUaHeaderEnable_Object=MibScalar
interopSendUaHeaderEnable=_InteropSendUaHeaderEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,800),_InteropSendUaHeaderEnable_Type())
interopSendUaHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSendUaHeaderEnable.setStatus(_A)
class _InteropSdpDirectionAttributeEnable_Type(MxEnableState):defaultValue=1
_InteropSdpDirectionAttributeEnable_Type.__name__=_D
_InteropSdpDirectionAttributeEnable_Object=MibScalar
interopSdpDirectionAttributeEnable=_InteropSdpDirectionAttributeEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,900),_InteropSdpDirectionAttributeEnable_Type())
interopSdpDirectionAttributeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpDirectionAttributeEnable.setStatus(_A)
class _InteropSdpDetectPeerDirectionAttributeSupportEnable_Type(MxEnableState):defaultValue=1
_InteropSdpDetectPeerDirectionAttributeSupportEnable_Type.__name__=_D
_InteropSdpDetectPeerDirectionAttributeSupportEnable_Object=MibScalar
interopSdpDetectPeerDirectionAttributeSupportEnable=_InteropSdpDetectPeerDirectionAttributeSupportEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,950),_InteropSdpDetectPeerDirectionAttributeSupportEnable_Type())
interopSdpDetectPeerDirectionAttributeSupportEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpDetectPeerDirectionAttributeSupportEnable.setStatus(_A)
class _InteropOnHoldSdpConnectionAddress_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('holdAddress',100),('mediaAddress',200)))
_InteropOnHoldSdpConnectionAddress_Type.__name__=_C
_InteropOnHoldSdpConnectionAddress_Object=MibScalar
interopOnHoldSdpConnectionAddress=_InteropOnHoldSdpConnectionAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,975),_InteropOnHoldSdpConnectionAddress_Type())
interopOnHoldSdpConnectionAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:interopOnHoldSdpConnectionAddress.setStatus(_A)
class _InteropOnHoldSdpStreamDirection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_z,100),('sendonly',200)))
_InteropOnHoldSdpStreamDirection_Type.__name__=_C
_InteropOnHoldSdpStreamDirection_Object=MibScalar
interopOnHoldSdpStreamDirection=_InteropOnHoldSdpStreamDirection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1000),_InteropOnHoldSdpStreamDirection_Type())
interopOnHoldSdpStreamDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:interopOnHoldSdpStreamDirection.setStatus(_A)
class _InteropOnHoldAnswerSdpStreamDirection_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_z,100),('recvonly',200)))
_InteropOnHoldAnswerSdpStreamDirection_Type.__name__=_C
_InteropOnHoldAnswerSdpStreamDirection_Object=MibScalar
interopOnHoldAnswerSdpStreamDirection=_InteropOnHoldAnswerSdpStreamDirection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1025),_InteropOnHoldAnswerSdpStreamDirection_Type())
interopOnHoldAnswerSdpStreamDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:interopOnHoldAnswerSdpStreamDirection.setStatus(_A)
class _InteropSdpDirectionAttributeLevel_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mediaOrSessionLevel',100),('mediaAndSessionLevel',200)))
_InteropSdpDirectionAttributeLevel_Type.__name__=_C
_InteropSdpDirectionAttributeLevel_Object=MibScalar
interopSdpDirectionAttributeLevel=_InteropSdpDirectionAttributeLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1050),_InteropSdpDirectionAttributeLevel_Type())
interopSdpDirectionAttributeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpDirectionAttributeLevel.setStatus(_A)
class _InteropLocalRingOnProvisionalResponse_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('localRingWhenNoEstablishedMediaStream',1),('localRingAlways',2)))
_InteropLocalRingOnProvisionalResponse_Type.__name__=_C
_InteropLocalRingOnProvisionalResponse_Object=MibScalar
interopLocalRingOnProvisionalResponse=_InteropLocalRingOnProvisionalResponse_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1100),_InteropLocalRingOnProvisionalResponse_Type())
interopLocalRingOnProvisionalResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:interopLocalRingOnProvisionalResponse.setStatus(_A)
class _InteropSdpOriginLineSessionIdAndVersionMaxLength_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('max32bits',100),('max64bits',200)))
_InteropSdpOriginLineSessionIdAndVersionMaxLength_Type.__name__=_C
_InteropSdpOriginLineSessionIdAndVersionMaxLength_Object=MibScalar
interopSdpOriginLineSessionIdAndVersionMaxLength=_InteropSdpOriginLineSessionIdAndVersionMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1200),_InteropSdpOriginLineSessionIdAndVersionMaxLength_Type())
interopSdpOriginLineSessionIdAndVersionMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpOriginLineSessionIdAndVersionMaxLength.setStatus(_A)
class _InteropLockDnsSrvRecordPerCallEnable_Type(MxEnableState):defaultValue=0
_InteropLockDnsSrvRecordPerCallEnable_Type.__name__=_D
_InteropLockDnsSrvRecordPerCallEnable_Object=MibScalar
interopLockDnsSrvRecordPerCallEnable=_InteropLockDnsSrvRecordPerCallEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1400),_InteropLockDnsSrvRecordPerCallEnable_Type())
interopLockDnsSrvRecordPerCallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopLockDnsSrvRecordPerCallEnable.setStatus(_A)
class _InteropRejectCodeForUnsupportedSdpOffer_Type(Integer32):defaultValue=415;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(415,488)));namedValues=NamedValues(*((_A0,415),('notAcceptableHere',488)))
_InteropRejectCodeForUnsupportedSdpOffer_Type.__name__=_C
_InteropRejectCodeForUnsupportedSdpOffer_Object=MibScalar
interopRejectCodeForUnsupportedSdpOffer=_InteropRejectCodeForUnsupportedSdpOffer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,1750),_InteropRejectCodeForUnsupportedSdpOffer_Type())
interopRejectCodeForUnsupportedSdpOffer.setMaxAccess(_B)
if mibBuilder.loadTexts:interopRejectCodeForUnsupportedSdpOffer.setStatus(_A)
class _InteropUseDtmfPayloadTypeFoundInAnswer_Type(MxEnableState):defaultValue=0
_InteropUseDtmfPayloadTypeFoundInAnswer_Type.__name__=_D
_InteropUseDtmfPayloadTypeFoundInAnswer_Object=MibScalar
interopUseDtmfPayloadTypeFoundInAnswer=_InteropUseDtmfPayloadTypeFoundInAnswer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,2200),_InteropUseDtmfPayloadTypeFoundInAnswer_Type())
interopUseDtmfPayloadTypeFoundInAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:interopUseDtmfPayloadTypeFoundInAnswer.setStatus(_A)
class _InteropRegisterHomeDomainOverride_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InteropRegisterHomeDomainOverride_Type.__name__=_G
_InteropRegisterHomeDomainOverride_Object=MibScalar
interopRegisterHomeDomainOverride=_InteropRegisterHomeDomainOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,2400),_InteropRegisterHomeDomainOverride_Type())
interopRegisterHomeDomainOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:interopRegisterHomeDomainOverride.setStatus(_A)
class _InteropEnforceOfferAnswerModel_Type(MxEnableState):defaultValue=1
_InteropEnforceOfferAnswerModel_Type.__name__=_D
_InteropEnforceOfferAnswerModel_Object=MibScalar
interopEnforceOfferAnswerModel=_InteropEnforceOfferAnswerModel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,2600),_InteropEnforceOfferAnswerModel_Type())
interopEnforceOfferAnswerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:interopEnforceOfferAnswerModel.setStatus(_A)
class _InteropMapPlusToTonInternational_Type(MxEnableState):defaultValue=1
_InteropMapPlusToTonInternational_Type.__name__=_D
_InteropMapPlusToTonInternational_Object=MibScalar
interopMapPlusToTonInternational=_InteropMapPlusToTonInternational_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,2700),_InteropMapPlusToTonInternational_Type())
interopMapPlusToTonInternational.setMaxAccess(_B)
if mibBuilder.loadTexts:interopMapPlusToTonInternational.setStatus(_A)
class _InteropAllowLessMediaInResponse_Type(MxEnableState):defaultValue=0
_InteropAllowLessMediaInResponse_Type.__name__=_D
_InteropAllowLessMediaInResponse_Object=MibScalar
interopAllowLessMediaInResponse=_InteropAllowLessMediaInResponse_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,2800),_InteropAllowLessMediaInResponse_Type())
interopAllowLessMediaInResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:interopAllowLessMediaInResponse.setStatus(_A)
class _InteropDefaultUsernameValue_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('anonymous',100),('host',200)))
_InteropDefaultUsernameValue_Type.__name__=_C
_InteropDefaultUsernameValue_Object=MibScalar
interopDefaultUsernameValue=_InteropDefaultUsernameValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3000),_InteropDefaultUsernameValue_Type())
interopDefaultUsernameValue.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDefaultUsernameValue.setStatus(_A)
class _InteropCallWaitingSipInfoPrivateNumberCriteria_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InteropCallWaitingSipInfoPrivateNumberCriteria_Type.__name__=_G
_InteropCallWaitingSipInfoPrivateNumberCriteria_Object=MibScalar
interopCallWaitingSipInfoPrivateNumberCriteria=_InteropCallWaitingSipInfoPrivateNumberCriteria_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3250),_InteropCallWaitingSipInfoPrivateNumberCriteria_Type())
interopCallWaitingSipInfoPrivateNumberCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:interopCallWaitingSipInfoPrivateNumberCriteria.setStatus(_A)
class _InteropSdpT38ParametersEncoding_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('ituT38AnnexD',100),('sippingRealTimeFax00InternetDraft',200)))
_InteropSdpT38ParametersEncoding_Type.__name__=_C
_InteropSdpT38ParametersEncoding_Object=MibScalar
interopSdpT38ParametersEncoding=_InteropSdpT38ParametersEncoding_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3300),_InteropSdpT38ParametersEncoding_Type())
interopSdpT38ParametersEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpT38ParametersEncoding.setStatus(_A)
class _InteropReInviteForVoiceOn606NotAcceptable_Type(MxEnableState):defaultValue=0
_InteropReInviteForVoiceOn606NotAcceptable_Type.__name__=_D
_InteropReInviteForVoiceOn606NotAcceptable_Object=MibScalar
interopReInviteForVoiceOn606NotAcceptable=_InteropReInviteForVoiceOn606NotAcceptable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3400),_InteropReInviteForVoiceOn606NotAcceptable_Type())
interopReInviteForVoiceOn606NotAcceptable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopReInviteForVoiceOn606NotAcceptable.setStatus(_A)
class _InteropAllowMultipleActiveMediaInAnswer_Type(MxEnableState):defaultValue=1
_InteropAllowMultipleActiveMediaInAnswer_Type.__name__=_D
_InteropAllowMultipleActiveMediaInAnswer_Object=MibScalar
interopAllowMultipleActiveMediaInAnswer=_InteropAllowMultipleActiveMediaInAnswer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3500),_InteropAllowMultipleActiveMediaInAnswer_Type())
interopAllowMultipleActiveMediaInAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:interopAllowMultipleActiveMediaInAnswer.setStatus(_A)
class _InteropIgnoreSipOptionsOnNoUsuableEndpoints_Type(MxEnableState):defaultValue=0
_InteropIgnoreSipOptionsOnNoUsuableEndpoints_Type.__name__=_D
_InteropIgnoreSipOptionsOnNoUsuableEndpoints_Object=MibScalar
interopIgnoreSipOptionsOnNoUsuableEndpoints=_InteropIgnoreSipOptionsOnNoUsuableEndpoints_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3550),_InteropIgnoreSipOptionsOnNoUsuableEndpoints_Type())
interopIgnoreSipOptionsOnNoUsuableEndpoints.setMaxAccess(_B)
if mibBuilder.loadTexts:interopIgnoreSipOptionsOnNoUsuableEndpoints.setStatus(_A)
class _InteropSipOptionsMethodSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),('alwaysOk',200)))
_InteropSipOptionsMethodSupport_Type.__name__=_C
_InteropSipOptionsMethodSupport_Object=MibScalar
interopSipOptionsMethodSupport=_InteropSipOptionsMethodSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3600),_InteropSipOptionsMethodSupport_Type())
interopSipOptionsMethodSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSipOptionsMethodSupport.setStatus(_A)
class _InteropAllowMediaReactivationInAnswer_Type(MxEnableState):defaultValue=0
_InteropAllowMediaReactivationInAnswer_Type.__name__=_D
_InteropAllowMediaReactivationInAnswer_Object=MibScalar
interopAllowMediaReactivationInAnswer=_InteropAllowMediaReactivationInAnswer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3700),_InteropAllowMediaReactivationInAnswer_Type())
interopAllowMediaReactivationInAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:interopAllowMediaReactivationInAnswer.setStatus(_A)
class _InteropAllowAudioAndImageNegotiation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('enable',100),('disableOffer',200),('disableAll',300)))
_InteropAllowAudioAndImageNegotiation_Type.__name__=_C
_InteropAllowAudioAndImageNegotiation_Object=MibScalar
interopAllowAudioAndImageNegotiation=_InteropAllowAudioAndImageNegotiation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,3800),_InteropAllowAudioAndImageNegotiation_Type())
interopAllowAudioAndImageNegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:interopAllowAudioAndImageNegotiation.setStatus(_A)
class _InteropEscapePoundInSipUriUsername_Type(MxEnableState):defaultValue=1
_InteropEscapePoundInSipUriUsername_Type.__name__=_D
_InteropEscapePoundInSipUriUsername_Object=MibScalar
interopEscapePoundInSipUriUsername=_InteropEscapePoundInSipUriUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4000),_InteropEscapePoundInSipUriUsername_Type())
interopEscapePoundInSipUriUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:interopEscapePoundInSipUriUsername.setStatus(_A)
class _InteropSiemensTransportHeaderEnable_Type(MxEnableState):defaultValue=0
_InteropSiemensTransportHeaderEnable_Type.__name__=_D
_InteropSiemensTransportHeaderEnable_Object=MibScalar
interopSiemensTransportHeaderEnable=_InteropSiemensTransportHeaderEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4100),_InteropSiemensTransportHeaderEnable_Type())
interopSiemensTransportHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSiemensTransportHeaderEnable.setStatus(_A)
class _InteropTlsClientAuthenticationEnable_Type(MxEnableState):defaultValue=0
_InteropTlsClientAuthenticationEnable_Type.__name__=_D
_InteropTlsClientAuthenticationEnable_Object=MibScalar
interopTlsClientAuthenticationEnable=_InteropTlsClientAuthenticationEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4200),_InteropTlsClientAuthenticationEnable_Type())
interopTlsClientAuthenticationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopTlsClientAuthenticationEnable.setStatus(_A)
class _InteropTlsCertificateValidation_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('noValidation',100),('trustedCertificate',200),('dnsSrvResponse',300),('hostName',400)))
_InteropTlsCertificateValidation_Type.__name__=_C
_InteropTlsCertificateValidation_Object=MibScalar
interopTlsCertificateValidation=_InteropTlsCertificateValidation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4250),_InteropTlsCertificateValidation_Type())
interopTlsCertificateValidation.setMaxAccess(_B)
if mibBuilder.loadTexts:interopTlsCertificateValidation.setStatus(_A)
class _InteropIgnorePlusInUsername_Type(MxEnableState):defaultValue=0
_InteropIgnorePlusInUsername_Type.__name__=_D
_InteropIgnorePlusInUsername_Object=MibScalar
interopIgnorePlusInUsername=_InteropIgnorePlusInUsername_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4300),_InteropIgnorePlusInUsername_Type())
interopIgnorePlusInUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:interopIgnorePlusInUsername.setStatus(_A)
_BehaviorOnT38InviteNotAcceptedTable_Object=MibTable
behaviorOnT38InviteNotAcceptedTable=_BehaviorOnT38InviteNotAcceptedTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4600))
if mibBuilder.loadTexts:behaviorOnT38InviteNotAcceptedTable.setStatus(_A)
_BehaviorOnT38InviteNotAcceptedEntry_Object=MibTableRow
behaviorOnT38InviteNotAcceptedEntry=_BehaviorOnT38InviteNotAcceptedEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4600,1))
behaviorOnT38InviteNotAcceptedEntry.setIndexNames((0,_H,_A1))
if mibBuilder.loadTexts:behaviorOnT38InviteNotAcceptedEntry.setStatus(_A)
class _BehaviorOnT38InviteNotAcceptedSipErrorCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(406,406),ValueRangeConstraint(415,415),ValueRangeConstraint(488,488),ValueRangeConstraint(606,606))
_BehaviorOnT38InviteNotAcceptedSipErrorCode_Type.__name__=_F
_BehaviorOnT38InviteNotAcceptedSipErrorCode_Object=MibTableColumn
behaviorOnT38InviteNotAcceptedSipErrorCode=_BehaviorOnT38InviteNotAcceptedSipErrorCode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4600,1,100),_BehaviorOnT38InviteNotAcceptedSipErrorCode_Type())
behaviorOnT38InviteNotAcceptedSipErrorCode.setMaxAccess(_E)
if mibBuilder.loadTexts:behaviorOnT38InviteNotAcceptedSipErrorCode.setStatus(_A)
class _BehaviorOnT38InviteNotAcceptedBehavior_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('dropCall',100),('reInviteForClearChannelOnly',200),('reEstablishAudio',300),('usePreviousMediaNegotiation',400)))
_BehaviorOnT38InviteNotAcceptedBehavior_Type.__name__=_C
_BehaviorOnT38InviteNotAcceptedBehavior_Object=MibTableColumn
behaviorOnT38InviteNotAcceptedBehavior=_BehaviorOnT38InviteNotAcceptedBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4600,1,200),_BehaviorOnT38InviteNotAcceptedBehavior_Type())
behaviorOnT38InviteNotAcceptedBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:behaviorOnT38InviteNotAcceptedBehavior.setStatus(_A)
class _InteropBehaviorOnMachineDetection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('reInviteOnFaxT38Only',100),('reInviteOnNoNegotiatedDataCodec',200),('reInviteUnconditional',300)))
_InteropBehaviorOnMachineDetection_Type.__name__=_C
_InteropBehaviorOnMachineDetection_Object=MibScalar
interopBehaviorOnMachineDetection=_InteropBehaviorOnMachineDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4650),_InteropBehaviorOnMachineDetection_Type())
interopBehaviorOnMachineDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:interopBehaviorOnMachineDetection.setStatus(_A)
class _InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('firstCodec',100),('prioritizeClearChannel',200)))
_InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Type.__name__=_C
_InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Object=MibScalar
interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice=_InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4700),_InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Type())
interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice.setMaxAccess(_B)
if mibBuilder.loadTexts:interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice.setStatus(_A)
class _InteropSipUriUserParameterValue_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_InteropSipUriUserParameterValue_Type.__name__=_G
_InteropSipUriUserParameterValue_Object=MibScalar
interopSipUriUserParameterValue=_InteropSipUriUserParameterValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4800),_InteropSipUriUserParameterValue_Type())
interopSipUriUserParameterValue.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSipUriUserParameterValue.setStatus(_A)
class _InteropListenForEarlyRtpEnable_Type(MxEnableState):defaultValue=0
_InteropListenForEarlyRtpEnable_Type.__name__=_D
_InteropListenForEarlyRtpEnable_Object=MibScalar
interopListenForEarlyRtpEnable=_InteropListenForEarlyRtpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,4900),_InteropListenForEarlyRtpEnable_Type())
interopListenForEarlyRtpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopListenForEarlyRtpEnable.setStatus(_A)
class _InteropRegistrationContactMatching_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('strict',100),('ignoreUriParams',200),('ignoreUriAndPortParams',300)))
_InteropRegistrationContactMatching_Type.__name__=_C
_InteropRegistrationContactMatching_Object=MibScalar
interopRegistrationContactMatching=_InteropRegistrationContactMatching_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5000),_InteropRegistrationContactMatching_Type())
interopRegistrationContactMatching.setMaxAccess(_B)
if mibBuilder.loadTexts:interopRegistrationContactMatching.setStatus(_A)
class _InteropResolveRouteHeaderEnable_Type(MxEnableState):defaultValue=0
_InteropResolveRouteHeaderEnable_Type.__name__=_D
_InteropResolveRouteHeaderEnable_Object=MibScalar
interopResolveRouteHeaderEnable=_InteropResolveRouteHeaderEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5100),_InteropResolveRouteHeaderEnable_Type())
interopResolveRouteHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopResolveRouteHeaderEnable.setStatus(_A)
class _InteropForceDnsNaptrInTls_Type(MxEnableState):defaultValue=0
_InteropForceDnsNaptrInTls_Type.__name__=_D
_InteropForceDnsNaptrInTls_Object=MibScalar
interopForceDnsNaptrInTls=_InteropForceDnsNaptrInTls_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5200),_InteropForceDnsNaptrInTls_Type())
interopForceDnsNaptrInTls.setMaxAccess(_B)
if mibBuilder.loadTexts:interopForceDnsNaptrInTls.setStatus(_A)
class _InteropAckBranchMatching_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('rfc3261',100),('rfc3261WithoutAck',200)))
_InteropAckBranchMatching_Type.__name__=_C
_InteropAckBranchMatching_Object=MibScalar
interopAckBranchMatching=_InteropAckBranchMatching_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5300),_InteropAckBranchMatching_Type())
interopAckBranchMatching.setMaxAccess(_B)
if mibBuilder.loadTexts:interopAckBranchMatching.setStatus(_A)
class _InteropIgnoreRequireHeaderEnable_Type(MxEnableState):defaultValue=1
_InteropIgnoreRequireHeaderEnable_Type.__name__=_D
_InteropIgnoreRequireHeaderEnable_Object=MibScalar
interopIgnoreRequireHeaderEnable=_InteropIgnoreRequireHeaderEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5400),_InteropIgnoreRequireHeaderEnable_Type())
interopIgnoreRequireHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopIgnoreRequireHeaderEnable.setStatus(_A)
class _InteropUaHeaderFormat_Type(OctetString):defaultValue=OctetString('%product%/v%version% %profile%')
_InteropUaHeaderFormat_Type.__name__=_G
_InteropUaHeaderFormat_Object=MibScalar
interopUaHeaderFormat=_InteropUaHeaderFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5500),_InteropUaHeaderFormat_Type())
interopUaHeaderFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:interopUaHeaderFormat.setStatus(_A)
class _InteropSipInfoWithoutContentAnswer_Type(Integer32):defaultValue=415;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,415)));namedValues=NamedValues(*(('ok',200),(_A0,415)))
_InteropSipInfoWithoutContentAnswer_Type.__name__=_C
_InteropSipInfoWithoutContentAnswer_Object=MibScalar
interopSipInfoWithoutContentAnswer=_InteropSipInfoWithoutContentAnswer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5600),_InteropSipInfoWithoutContentAnswer_Type())
interopSipInfoWithoutContentAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSipInfoWithoutContentAnswer.setStatus(_A)
class _InteropRegistrationDelayValue_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_InteropRegistrationDelayValue_Type.__name__=_F
_InteropRegistrationDelayValue_Object=MibScalar
interopRegistrationDelayValue=_InteropRegistrationDelayValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5700),_InteropRegistrationDelayValue_Type())
interopRegistrationDelayValue.setMaxAccess(_B)
if mibBuilder.loadTexts:interopRegistrationDelayValue.setStatus(_A)
class _InteropUnsupportedContentType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('reject',100),('allow',200),('ignore',300)))
_InteropUnsupportedContentType_Type.__name__=_C
_InteropUnsupportedContentType_Object=MibScalar
interopUnsupportedContentType=_InteropUnsupportedContentType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5800),_InteropUnsupportedContentType_Type())
interopUnsupportedContentType.setMaxAccess(_B)
if mibBuilder.loadTexts:interopUnsupportedContentType.setStatus(_A)
class _InteropWaitConfirmedDialogForBlindTransfer_Type(MxEnableState):defaultValue=0
_InteropWaitConfirmedDialogForBlindTransfer_Type.__name__=_D
_InteropWaitConfirmedDialogForBlindTransfer_Object=MibScalar
interopWaitConfirmedDialogForBlindTransfer=_InteropWaitConfirmedDialogForBlindTransfer_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,5900),_InteropWaitConfirmedDialogForBlindTransfer_Type())
interopWaitConfirmedDialogForBlindTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:interopWaitConfirmedDialogForBlindTransfer.setStatus('obsolete')
class _InteropPendingBlindTransferTimeout_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_InteropPendingBlindTransferTimeout_Type.__name__=_F
_InteropPendingBlindTransferTimeout_Object=MibScalar
interopPendingBlindTransferTimeout=_InteropPendingBlindTransferTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6000),_InteropPendingBlindTransferTimeout_Type())
interopPendingBlindTransferTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:interopPendingBlindTransferTimeout.setStatus(_A)
class _InteropForkedProvisionalResponsesBehavior_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_A2,100),('interpretAll',200)))
_InteropForkedProvisionalResponsesBehavior_Type.__name__=_C
_InteropForkedProvisionalResponsesBehavior_Object=MibScalar
interopForkedProvisionalResponsesBehavior=_InteropForkedProvisionalResponsesBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6100),_InteropForkedProvisionalResponsesBehavior_Type())
interopForkedProvisionalResponsesBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:interopForkedProvisionalResponsesBehavior.setStatus(_A)
class _InteropReliableForkedProvisionalResponsesBehavior_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_A2,100),('interpretFirstRemoteMedia',200)))
_InteropReliableForkedProvisionalResponsesBehavior_Type.__name__=_C
_InteropReliableForkedProvisionalResponsesBehavior_Object=MibScalar
interopReliableForkedProvisionalResponsesBehavior=_InteropReliableForkedProvisionalResponsesBehavior_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6110),_InteropReliableForkedProvisionalResponsesBehavior_Type())
interopReliableForkedProvisionalResponsesBehavior.setMaxAccess(_B)
if mibBuilder.loadTexts:interopReliableForkedProvisionalResponsesBehavior.setStatus(_A)
class _InteropSipContactDisplayNamePresence_Type(MxEnableState):defaultValue=1
_InteropSipContactDisplayNamePresence_Type.__name__=_D
_InteropSipContactDisplayNamePresence_Object=MibScalar
interopSipContactDisplayNamePresence=_InteropSipContactDisplayNamePresence_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6200),_InteropSipContactDisplayNamePresence_Type())
interopSipContactDisplayNamePresence.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSipContactDisplayNamePresence.setStatus(_A)
class _InteropEscapeFormat_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('lowercaseHex',100),('uppercaseHex',200)))
_InteropEscapeFormat_Type.__name__=_C
_InteropEscapeFormat_Object=MibScalar
interopEscapeFormat=_InteropEscapeFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6300),_InteropEscapeFormat_Type())
interopEscapeFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:interopEscapeFormat.setStatus(_A)
class _InteropKeepAliveOptionFormat_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('shortFrom',100),('fullFrom',200)))
_InteropKeepAliveOptionFormat_Type.__name__=_C
_InteropKeepAliveOptionFormat_Object=MibScalar
interopKeepAliveOptionFormat=_InteropKeepAliveOptionFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6400),_InteropKeepAliveOptionFormat_Type())
interopKeepAliveOptionFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:interopKeepAliveOptionFormat.setStatus(_A)
class _InteropInfoDtmfRelayFlashEvent_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_S,100),('evR',200),('ev16',300)))
_InteropInfoDtmfRelayFlashEvent_Type.__name__=_C
_InteropInfoDtmfRelayFlashEvent_Object=MibScalar
interopInfoDtmfRelayFlashEvent=_InteropInfoDtmfRelayFlashEvent_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6500),_InteropInfoDtmfRelayFlashEvent_Type())
interopInfoDtmfRelayFlashEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:interopInfoDtmfRelayFlashEvent.setStatus(_A)
class _InteropSdpPTimeAttribute_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_P,100),('declarativePreferredCodec',200),('declarativeConfigured',300)))
_InteropSdpPTimeAttribute_Type.__name__=_C
_InteropSdpPTimeAttribute_Object=MibScalar
interopSdpPTimeAttribute=_InteropSdpPTimeAttribute_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6600),_InteropSdpPTimeAttribute_Type())
interopSdpPTimeAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpPTimeAttribute.setStatus(_A)
class _InteropSdpPTimeAttributeValue_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,80))
_InteropSdpPTimeAttributeValue_Type.__name__=_F
_InteropSdpPTimeAttributeValue_Object=MibScalar
interopSdpPTimeAttributeValue=_InteropSdpPTimeAttributeValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6700),_InteropSdpPTimeAttributeValue_Type())
interopSdpPTimeAttributeValue.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSdpPTimeAttributeValue.setStatus(_A)
class _InteropIncrementSdpVersionWhenModified_Type(MxEnableState):defaultValue=1
_InteropIncrementSdpVersionWhenModified_Type.__name__=_D
_InteropIncrementSdpVersionWhenModified_Object=MibScalar
interopIncrementSdpVersionWhenModified=_InteropIncrementSdpVersionWhenModified_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,6800),_InteropIncrementSdpVersionWhenModified_Type())
interopIncrementSdpVersionWhenModified.setMaxAccess(_B)
if mibBuilder.loadTexts:interopIncrementSdpVersionWhenModified.setStatus(_A)
class _InteropActivateEarlyMediaOnProvisionalResponseAck_Type(MxEnableState):defaultValue=0
_InteropActivateEarlyMediaOnProvisionalResponseAck_Type.__name__=_D
_InteropActivateEarlyMediaOnProvisionalResponseAck_Object=MibScalar
interopActivateEarlyMediaOnProvisionalResponseAck=_InteropActivateEarlyMediaOnProvisionalResponseAck_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,7000),_InteropActivateEarlyMediaOnProvisionalResponseAck_Type())
interopActivateEarlyMediaOnProvisionalResponseAck.setMaxAccess(_B)
if mibBuilder.loadTexts:interopActivateEarlyMediaOnProvisionalResponseAck.setStatus(_A)
class _InteropSend183WithSdpBefore180WithoutSdp_Type(MxEnableState):defaultValue=0
_InteropSend183WithSdpBefore180WithoutSdp_Type.__name__=_D
_InteropSend183WithSdpBefore180WithoutSdp_Object=MibScalar
interopSend183WithSdpBefore180WithoutSdp=_InteropSend183WithSdpBefore180WithoutSdp_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,7100),_InteropSend183WithSdpBefore180WithoutSdp_Type())
interopSend183WithSdpBefore180WithoutSdp.setMaxAccess(_B)
if mibBuilder.loadTexts:interopSend183WithSdpBefore180WithoutSdp.setStatus(_A)
class _InteropCollectCallProprietaryHeader_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('ignore',100),('relay',200),('block',300)))
_InteropCollectCallProprietaryHeader_Type.__name__=_C
_InteropCollectCallProprietaryHeader_Object=MibScalar
interopCollectCallProprietaryHeader=_InteropCollectCallProprietaryHeader_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,7200),_InteropCollectCallProprietaryHeader_Type())
interopCollectCallProprietaryHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:interopCollectCallProprietaryHeader.setStatus(_A)
_InteropDtmfGroup_ObjectIdentity=ObjectIdentity
interopDtmfGroup=_InteropDtmfGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,50000))
class _InteropDtmfTransportMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('draftChoudhuriSipInfoDigit00',100),('infoDtmfRelay',200)))
_InteropDtmfTransportMethod_Type.__name__=_C
_InteropDtmfTransportMethod_Object=MibScalar
interopDtmfTransportMethod=_InteropDtmfTransportMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,50000,100),_InteropDtmfTransportMethod_Type())
interopDtmfTransportMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfTransportMethod.setStatus(_A)
class _InteropDtmfTransportDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,2000))
_InteropDtmfTransportDuration_Type.__name__=_C
_InteropDtmfTransportDuration_Object=MibScalar
interopDtmfTransportDuration=_InteropDtmfTransportDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50000,50000,200),_InteropDtmfTransportDuration_Type())
interopDtmfTransportDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfTransportDuration.setStatus(_A)
_MonitoringGroup_ObjectIdentity=ObjectIdentity
monitoringGroup=_MonitoringGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50500))
class _SipNotificationsGateway_Type(OctetString):defaultValue=OctetString('default')
_SipNotificationsGateway_Type.__name__=_G
_SipNotificationsGateway_Object=MibScalar
sipNotificationsGateway=_SipNotificationsGateway_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50500,100),_SipNotificationsGateway_Type())
sipNotificationsGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:sipNotificationsGateway.setStatus(_A)
class _MaxNotificationsPerNotify_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_MaxNotificationsPerNotify_Type.__name__=_F
_MaxNotificationsPerNotify_Object=MibScalar
maxNotificationsPerNotify=_MaxNotificationsPerNotify_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,50500,200),_MaxNotificationsPerNotify_Type())
maxNotificationsPerNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:maxNotificationsPerNotify.setStatus(_A)
_DebugGroup_ObjectIdentity=ObjectIdentity
debugGroup=_DebugGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,51000))
class _DebugSignalingLogEnable_Type(MxEnableState):defaultValue=0
_DebugSignalingLogEnable_Type.__name__=_D
_DebugSignalingLogEnable_Object=MibScalar
debugSignalingLogEnable=_DebugSignalingLogEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,51000,100),_DebugSignalingLogEnable_Type())
debugSignalingLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:debugSignalingLogEnable.setStatus(_A)
class _DebugSignalingLogHost_Type(MxIpHostNamePort):defaultValue=OctetString(_M)
_DebugSignalingLogHost_Type.__name__=_I
_DebugSignalingLogHost_Object=MibScalar
debugSignalingLogHost=_DebugSignalingLogHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,51000,200),_DebugSignalingLogHost_Type())
debugSignalingLogHost.setMaxAccess(_B)
if mibBuilder.loadTexts:debugSignalingLogHost.setStatus(_A)
class _DebugContextSnapshotTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10080))
_DebugContextSnapshotTime_Type.__name__=_F
_DebugContextSnapshotTime_Object=MibScalar
debugContextSnapshotTime=_DebugContextSnapshotTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,51000,300),_DebugContextSnapshotTime_Type())
debugContextSnapshotTime.setMaxAccess(_B)
if mibBuilder.loadTexts:debugContextSnapshotTime.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_S,0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1400,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'sipEpMIB':sipEpMIB,'sipEpMIBObjects':sipEpMIBObjects,'gatewayTable':gatewayTable,'gatewayEntry':gatewayEntry,_T:gatewayName,'gatewayType':gatewayType,'gatewayNetworkInterface':gatewayNetworkInterface,'gatewayMediaNetworks':gatewayMediaNetworks,'gatewayPort':gatewayPort,'gatewaySecurePort':gatewaySecurePort,'gatewayDomain':gatewayDomain,'gatewayDelete':gatewayDelete,'gatewayStatusTable':gatewayStatusTable,'gatewayStatusEntry':gatewayStatusEntry,_U:gatewayStatusName,'gatewayStatusNetworkInterface':gatewayStatusNetworkInterface,'gatewayStatusMediaNetworks':gatewayStatusMediaNetworks,'gatewayStatusPort':gatewayStatusPort,'gatewayStatusSecurePort':gatewayStatusSecurePort,'gatewayStatusDomain':gatewayStatusDomain,'gatewayStatusState':gatewayStatusState,'userAgentTable':userAgentTable,'userAgentEntry':userAgentEntry,_V:userAgentEpId,'userAgentUsername':userAgentUsername,'userAgentFriendlyName':userAgentFriendlyName,'userAgentRegister':userAgentRegister,'userAgentGatewayName':userAgentGatewayName,'userAgentMwiSubscribe':userAgentMwiSubscribe,'userAgentContactDomain':userAgentContactDomain,'userAgentAcceptLanguage':userAgentAcceptLanguage,'proxyGroup':proxyGroup,'defaultStaticProxyHomeDomainHost':defaultStaticProxyHomeDomainHost,'defaultStaticProxyOutboundHost':defaultStaticProxyOutboundHost,'defaultProxyOutboundType':defaultProxyOutboundType,'gwSpecificProxyTable':gwSpecificProxyTable,'gwSpecificProxyEntry':gwSpecificProxyEntry,_Z:gwSpecificProxyGatewayName,'gwSpecificProxyEnableConfig':gwSpecificProxyEnableConfig,'gwSpecificProxyHomeDomainHost':gwSpecificProxyHomeDomainHost,'gwSpecificProxyOutboundHost':gwSpecificProxyOutboundHost,'gwSpecificProxyOutboundType':gwSpecificProxyOutboundType,'sessionRefreshGroup':sessionRefreshGroup,'defaultSessionTimerEnable':defaultSessionTimerEnable,'defaultSessionTimerMinimumExpirationDelay':defaultSessionTimerMinimumExpirationDelay,'defaultSessionTimerMaximumExpirationDelay':defaultSessionTimerMaximumExpirationDelay,'sessionRefreshRequestMethod':sessionRefreshRequestMethod,'authenticationGroup':authenticationGroup,'authenticationTable':authenticationTable,'authenticationEntry':authenticationEntry,_a:authenticationIndex,'authenticationCriteriaSelection':authenticationCriteriaSelection,'authenticationEpId':authenticationEpId,'authenticationGatewayName':authenticationGatewayName,'authenticationUsernameCriteria':authenticationUsernameCriteria,'authenticationValidateRealm':authenticationValidateRealm,'authenticationRealm':authenticationRealm,'authenticationUsername':authenticationUsername,'authenticationPassword':authenticationPassword,'authenticationUp':authenticationUp,'authenticationDown':authenticationDown,'authenticationInsert':authenticationInsert,'authenticationDelete':authenticationDelete,'registrationGroup':registrationGroup,'defaultRegistrationRefreshTime':defaultRegistrationRefreshTime,'defaultRegistrationExpirationValue':defaultRegistrationExpirationValue,'defaultRegistrationProposedExpirationValue':defaultRegistrationProposedExpirationValue,'defaultRegistrationRetryTime':defaultRegistrationRetryTime,'defaultRegistrationUnregisteredBehavior':defaultRegistrationUnregisteredBehavior,'defaultUnitRegistrationUnregisteredBehavior':defaultUnitRegistrationUnregisteredBehavior,'defaultStaticRegistrarServerHost':defaultStaticRegistrarServerHost,'gwSpecificRegistrationTable':gwSpecificRegistrationTable,'gwSpecificRegistrationEntry':gwSpecificRegistrationEntry,_b:gwSpecificRegistrationGatewayName,'gwSpecificRegistrationEnableConfig':gwSpecificRegistrationEnableConfig,'gwSpecificRegistrationRefreshTime':gwSpecificRegistrationRefreshTime,'gwSpecificRegistrationExpirationValue':gwSpecificRegistrationExpirationValue,'gwSpecificRegistrationProposedExpirationValue':gwSpecificRegistrationProposedExpirationValue,'gwSpecificRegistrationRetryTime':gwSpecificRegistrationRetryTime,'gwSpecificRegistrationUnregisteredBehavior':gwSpecificRegistrationUnregisteredBehavior,'gwSpecificRegistrationServerHost':gwSpecificRegistrationServerHost,'unitRegistrationsTable':unitRegistrationsTable,'unitRegistrationsEntry':unitRegistrationsEntry,_c:unitRegistrationsIndex,'unitRegistrationsUsername':unitRegistrationsUsername,'unitRegistrationsGatewayName':unitRegistrationsGatewayName,'unitRegistrationsDelete':unitRegistrationsDelete,'behaviorOnInitialRegistrationReception':behaviorOnInitialRegistrationReception,'registrationDelayOnInitialRegistrationReception':registrationDelayOnInitialRegistrationReception,'registrationStatusTable':registrationStatusTable,'registrationStatusEntry':registrationStatusEntry,_d:registrationStatusIndex,'registrationStatusGateway':registrationStatusGateway,'registrationStatusEndpoint':registrationStatusEndpoint,'registrationStatusState':registrationStatusState,'registrationStatusRegistrar':registrationStatusRegistrar,'registrationStatusUsername':registrationStatusUsername,'transportGroup':transportGroup,'transportPersistentBasePort':transportPersistentBasePort,'transportPersistentPortInterval':transportPersistentPortInterval,'transportFailbackInterval':transportFailbackInterval,'transportTlsCertificateTrustLevel':transportTlsCertificateTrustLevel,'transportTlsCipherSuite':transportTlsCipherSuite,'transportTlsVersion':transportTlsVersion,'transportConfigTable':transportConfigTable,'transportConfigEntry':transportConfigEntry,_j:transportConfigGatewayName,'transportConfigRegistrationEnable':transportConfigRegistrationEnable,'transportConfigContactEnable':transportConfigContactEnable,'transportConfigUdpEnable':transportConfigUdpEnable,'transportConfigUdpQValue':transportConfigUdpQValue,'transportConfigTcpEnable':transportConfigTcpEnable,'transportConfigTcpQValue':transportConfigTcpQValue,'transportConfigTlsEnable':transportConfigTlsEnable,'transportConfigTlsQValue':transportConfigTlsQValue,'tlsPersistentConnectionStatusTable':tlsPersistentConnectionStatusTable,'tlsPersistentConnectionStatusEntry':tlsPersistentConnectionStatusEntry,_k:tlsPersistentConnectionStatusIndex,'tlsPersistentConnectionStatusGateway':tlsPersistentConnectionStatusGateway,'tlsPersistentConnectionStatusLocalPort':tlsPersistentConnectionStatusLocalPort,'tlsPersistentConnectionStatusRemoteHost':tlsPersistentConnectionStatusRemoteHost,'tlsPersistentConnectionStatusRemoteHostIpAddr':tlsPersistentConnectionStatusRemoteHostIpAddr,'tlsPersistentConnectionStatusState':tlsPersistentConnectionStatusState,'failoverGroup':failoverGroup,'defaultSipFailoverConditions':defaultSipFailoverConditions,'gwSpecificFailoverTable':gwSpecificFailoverTable,'gwSpecificFailoverEntry':gwSpecificFailoverEntry,_m:gwSpecificFailoverGatewayName,'gwSpecificFailoverEnableConfig':gwSpecificFailoverEnableConfig,'gwSpecificFailoverSipFailoverConditions':gwSpecificFailoverSipFailoverConditions,'penaltyBoxGroup':penaltyBoxGroup,'penaltyBoxEnable':penaltyBoxEnable,'penaltyBoxTime':penaltyBoxTime,'errorMappingGroup':errorMappingGroup,'errorMappingSipToCauseTable':errorMappingSipToCauseTable,'errorMappingSipToCauseEntry':errorMappingSipToCauseEntry,_n:errorMappingSipToCauseSipCode,'errorMappingSipToCauseCause':errorMappingSipToCauseCause,'errorMappingSipToCauseDelete':errorMappingSipToCauseDelete,'errorMappingCauseToSipTable':errorMappingCauseToSipTable,'errorMappingCauseToSipEntry':errorMappingCauseToSipEntry,_o:errorMappingCauseToSipCause,'errorMappingCauseToSipSipCode':errorMappingCauseToSipSipCode,'errorMappingCauseToSipDelete':errorMappingCauseToSipDelete,'reasonHeaderSupport':reasonHeaderSupport,'sipKeepAliveGroup':sipKeepAliveGroup,'sipKeepAliveMethod':sipKeepAliveMethod,'sipKeepAliveInterval':sipKeepAliveInterval,'sipKeepAliveRetry':sipKeepAliveRetry,'sipKeepAliveDestination':sipKeepAliveDestination,'gwKeepAliveAlternateDestinationTable':gwKeepAliveAlternateDestinationTable,'gwKeepAliveAlternateDestinationEntry':gwKeepAliveAlternateDestinationEntry,_p:gwKeepAliveAlternateDestinationGatewayName,'gwKeepAliveAlternateDestinationAlternateDestination':gwKeepAliveAlternateDestinationAlternateDestination,'prackGroup':prackGroup,'uasPrackSupport':uasPrackSupport,'uacPrackSupport':uacPrackSupport,'offerAnswerGroup':offerAnswerGroup,'answerCodecNegotiation':answerCodecNegotiation,'diversionGroup':diversionGroup,'diversionConfigTable':diversionConfigTable,'diversionConfigEntry':diversionConfigEntry,_r:diversionConfigGatewayName,'diversionConfigMethod':diversionConfigMethod,'dnsGroup':dnsGroup,'supportedDnsQueries':supportedDnsQueries,'dnsFailureConcealment':dnsFailureConcealment,'dnsIpVersion':dnsIpVersion,'messageWaitingIndication':messageWaitingIndication,'defaultStaticMessagingHost':defaultStaticMessagingHost,'defaultUsernameInRequestUriEnable':defaultUsernameInRequestUriEnable,'gwSpecificMwiTable':gwSpecificMwiTable,'gwSpecificMwiEntry':gwSpecificMwiEntry,_s:gwSpecificMwiGatewayName,'gwSpecificMwiEnableConfig':gwSpecificMwiEnableConfig,'gwSpecificMwiMessagingHost':gwSpecificMwiMessagingHost,'gwSpecificMwiUsernameInRequestUriEnable':gwSpecificMwiUsernameInRequestUriEnable,'mwiStatusTable':mwiStatusTable,'mwiStatusEntry':mwiStatusEntry,_t:mwiStatusIndex,'mwiStatusGatewayName':mwiStatusGatewayName,'mwiStatusSubscriptionState':mwiStatusSubscriptionState,'mwiStatusEndpoint':mwiStatusEndpoint,'mwiStatusMessagingHost':mwiStatusMessagingHost,'mwiStatusUsername':mwiStatusUsername,'conferenceGroup':conferenceGroup,'defaultStaticConferenceServerUri':defaultStaticConferenceServerUri,'gwSpecificConferenceTable':gwSpecificConferenceTable,'gwSpecificConferenceEntry':gwSpecificConferenceEntry,_u:gwSpecificConferenceGatewayName,'gwSpecificConferenceEnableConfig':gwSpecificConferenceEnableConfig,'gwSpecificConferenceServerUri':gwSpecificConferenceServerUri,'priorityGroup':priorityGroup,'defaultOutboundPriorityCallRouting':defaultOutboundPriorityCallRouting,'eventHandlingGroup':eventHandlingGroup,'gwEventHandlingTable':gwEventHandlingTable,'gwEventHandlingEntry':gwEventHandlingEntry,_v:gwEventHandlingGatewayName,'gwEventHandlingReboot':gwEventHandlingReboot,'gwEventHandlingCheckSync':gwEventHandlingCheckSync,'sipMessageSupport':sipMessageSupport,'transferGroup':transferGroup,'referredByHeader':referredByHeader,'blindTransferMethod':blindTransferMethod,'referToHeaderUriSource':referToHeaderUriSource,'aocGroup':aocGroup,'aocConfigTable':aocConfigTable,'aocConfigEntry':aocConfigEntry,_w:aocConfigGatewayName,'aocConfigAocDSupport':aocConfigAocDSupport,'aocConfigAocESupport':aocConfigAocESupport,'kpmlGroup':kpmlGroup,'uasKpmlSupport':uasKpmlSupport,'securityAgreementGroup':securityAgreementGroup,'mediaSecurityAgreementEnable':mediaSecurityAgreementEnable,'privacyHeadersGroup':privacyHeadersGroup,'privacyHeadersInResponse':privacyHeadersInResponse,'rtcpXrGroup':rtcpXrGroup,'defaultStaticRtcpXrCollectorUri':defaultStaticRtcpXrCollectorUri,'defaultRtcpXrPeriodicReportsInterval':defaultRtcpXrPeriodicReportsInterval,'gwSpecificRtcpXrTable':gwSpecificRtcpXrTable,'gwSpecificRtcpXrEntry':gwSpecificRtcpXrEntry,_y:gwSpecificRtcpXrGatewayName,'gwSpecificRtcpXrEnableConfig':gwSpecificRtcpXrEnableConfig,'gwSpecificRtcpXrCollectorUri':gwSpecificRtcpXrCollectorUri,'gwSpecificRtcpXrPeriodicReportsInterval':gwSpecificRtcpXrPeriodicReportsInterval,'interopGroup':interopGroup,'interopTransmissionTimeout':interopTransmissionTimeout,'interopTcpConnectTimeout':interopTcpConnectTimeout,'interopSymmetricUdpSourcePortEnable':interopSymmetricUdpSourcePortEnable,'interopMaxForwardsValue':interopMaxForwardsValue,'interopSendUaHeaderEnable':interopSendUaHeaderEnable,'interopSdpDirectionAttributeEnable':interopSdpDirectionAttributeEnable,'interopSdpDetectPeerDirectionAttributeSupportEnable':interopSdpDetectPeerDirectionAttributeSupportEnable,'interopOnHoldSdpConnectionAddress':interopOnHoldSdpConnectionAddress,'interopOnHoldSdpStreamDirection':interopOnHoldSdpStreamDirection,'interopOnHoldAnswerSdpStreamDirection':interopOnHoldAnswerSdpStreamDirection,'interopSdpDirectionAttributeLevel':interopSdpDirectionAttributeLevel,'interopLocalRingOnProvisionalResponse':interopLocalRingOnProvisionalResponse,'interopSdpOriginLineSessionIdAndVersionMaxLength':interopSdpOriginLineSessionIdAndVersionMaxLength,'interopLockDnsSrvRecordPerCallEnable':interopLockDnsSrvRecordPerCallEnable,'interopRejectCodeForUnsupportedSdpOffer':interopRejectCodeForUnsupportedSdpOffer,'interopUseDtmfPayloadTypeFoundInAnswer':interopUseDtmfPayloadTypeFoundInAnswer,'interopRegisterHomeDomainOverride':interopRegisterHomeDomainOverride,'interopEnforceOfferAnswerModel':interopEnforceOfferAnswerModel,'interopMapPlusToTonInternational':interopMapPlusToTonInternational,'interopAllowLessMediaInResponse':interopAllowLessMediaInResponse,'interopDefaultUsernameValue':interopDefaultUsernameValue,'interopCallWaitingSipInfoPrivateNumberCriteria':interopCallWaitingSipInfoPrivateNumberCriteria,'interopSdpT38ParametersEncoding':interopSdpT38ParametersEncoding,'interopReInviteForVoiceOn606NotAcceptable':interopReInviteForVoiceOn606NotAcceptable,'interopAllowMultipleActiveMediaInAnswer':interopAllowMultipleActiveMediaInAnswer,'interopIgnoreSipOptionsOnNoUsuableEndpoints':interopIgnoreSipOptionsOnNoUsuableEndpoints,'interopSipOptionsMethodSupport':interopSipOptionsMethodSupport,'interopAllowMediaReactivationInAnswer':interopAllowMediaReactivationInAnswer,'interopAllowAudioAndImageNegotiation':interopAllowAudioAndImageNegotiation,'interopEscapePoundInSipUriUsername':interopEscapePoundInSipUriUsername,'interopSiemensTransportHeaderEnable':interopSiemensTransportHeaderEnable,'interopTlsClientAuthenticationEnable':interopTlsClientAuthenticationEnable,'interopTlsCertificateValidation':interopTlsCertificateValidation,'interopIgnorePlusInUsername':interopIgnorePlusInUsername,'behaviorOnT38InviteNotAcceptedTable':behaviorOnT38InviteNotAcceptedTable,'behaviorOnT38InviteNotAcceptedEntry':behaviorOnT38InviteNotAcceptedEntry,_A1:behaviorOnT38InviteNotAcceptedSipErrorCode,'behaviorOnT38InviteNotAcceptedBehavior':behaviorOnT38InviteNotAcceptedBehavior,'interopBehaviorOnMachineDetection':interopBehaviorOnMachineDetection,'interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice':interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice,'interopSipUriUserParameterValue':interopSipUriUserParameterValue,'interopListenForEarlyRtpEnable':interopListenForEarlyRtpEnable,'interopRegistrationContactMatching':interopRegistrationContactMatching,'interopResolveRouteHeaderEnable':interopResolveRouteHeaderEnable,'interopForceDnsNaptrInTls':interopForceDnsNaptrInTls,'interopAckBranchMatching':interopAckBranchMatching,'interopIgnoreRequireHeaderEnable':interopIgnoreRequireHeaderEnable,'interopUaHeaderFormat':interopUaHeaderFormat,'interopSipInfoWithoutContentAnswer':interopSipInfoWithoutContentAnswer,'interopRegistrationDelayValue':interopRegistrationDelayValue,'interopUnsupportedContentType':interopUnsupportedContentType,'interopWaitConfirmedDialogForBlindTransfer':interopWaitConfirmedDialogForBlindTransfer,'interopPendingBlindTransferTimeout':interopPendingBlindTransferTimeout,'interopForkedProvisionalResponsesBehavior':interopForkedProvisionalResponsesBehavior,'interopReliableForkedProvisionalResponsesBehavior':interopReliableForkedProvisionalResponsesBehavior,'interopSipContactDisplayNamePresence':interopSipContactDisplayNamePresence,'interopEscapeFormat':interopEscapeFormat,'interopKeepAliveOptionFormat':interopKeepAliveOptionFormat,'interopInfoDtmfRelayFlashEvent':interopInfoDtmfRelayFlashEvent,'interopSdpPTimeAttribute':interopSdpPTimeAttribute,'interopSdpPTimeAttributeValue':interopSdpPTimeAttributeValue,'interopIncrementSdpVersionWhenModified':interopIncrementSdpVersionWhenModified,'interopActivateEarlyMediaOnProvisionalResponseAck':interopActivateEarlyMediaOnProvisionalResponseAck,'interopSend183WithSdpBefore180WithoutSdp':interopSend183WithSdpBefore180WithoutSdp,'interopCollectCallProprietaryHeader':interopCollectCallProprietaryHeader,'interopDtmfGroup':interopDtmfGroup,'interopDtmfTransportMethod':interopDtmfTransportMethod,'interopDtmfTransportDuration':interopDtmfTransportDuration,'monitoringGroup':monitoringGroup,'sipNotificationsGateway':sipNotificationsGateway,'maxNotificationsPerNotify':maxNotificationsPerNotify,'debugGroup':debugGroup,'debugSignalingLogEnable':debugSignalingLogEnable,'debugSignalingLogHost':debugSignalingLogHost,'debugContextSnapshotTime':debugContextSnapshotTime,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})