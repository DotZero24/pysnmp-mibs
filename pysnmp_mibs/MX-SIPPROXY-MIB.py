_R='userTransformationsId'
_Q='delete'
_P='invalid'
_O='priorityDuplicate'
_N='routeId'
_M='registrationCacheSearchResultId'
_L='tlsPersistentConnectionStatusId'
_K='MxEnableState'
_J='yes'
_I='MxIpHostNamePort'
_H='MxAdvancedIpPort'
_G='MX-SIPPROXY-MIB'
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
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState',_H,'MxDigitMap',_K,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort',_I,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sipProxyMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600))
_SipProxyMIBObjects_ObjectIdentity=ObjectIdentity
sipProxyMIBObjects=_SipProxyMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1))
_StatusGroup_ObjectIdentity=ObjectIdentity
statusGroup=_StatusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100))
class _MonitoringState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('destinationIsUp',100),('destinationIsDown',200),('inactive',300),('unknown',400)))
_MonitoringState_Type.__name__=_D
_MonitoringState_Object=MibScalar
monitoringState=_MonitoringState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,100),_MonitoringState_Type())
monitoringState.setMaxAccess(_C)
if mibBuilder.loadTexts:monitoringState.setStatus(_A)
class _ProxyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700)));namedValues=NamedValues(*(('starting',100),('running',200),('runningInSurvivability',300),('stopping',400),('errorPortAlreadyInUse',500),('errorWaitingForTimeSynchronization',600),('errorInternal',700)))
_ProxyStatus_Type.__name__=_D
_ProxyStatus_Object=MibScalar
proxyStatus=_ProxyStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,200),_ProxyStatus_Type())
proxyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:proxyStatus.setStatus(_A)
_NbActiveCalls_Type=Unsigned32
_NbActiveCalls_Object=MibScalar
nbActiveCalls=_NbActiveCalls_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,250),_NbActiveCalls_Type())
nbActiveCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:nbActiveCalls.setStatus(_A)
_TlsPersistentConnectionStatusTable_Object=MibTable
tlsPersistentConnectionStatusTable=_TlsPersistentConnectionStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300))
if mibBuilder.loadTexts:tlsPersistentConnectionStatusTable.setStatus(_A)
_TlsPersistentConnectionStatusEntry_Object=MibTableRow
tlsPersistentConnectionStatusEntry=_TlsPersistentConnectionStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300,1))
tlsPersistentConnectionStatusEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:tlsPersistentConnectionStatusEntry.setStatus(_A)
_TlsPersistentConnectionStatusId_Type=Unsigned32
_TlsPersistentConnectionStatusId_Object=MibTableColumn
tlsPersistentConnectionStatusId=_TlsPersistentConnectionStatusId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300,1,100),_TlsPersistentConnectionStatusId_Type())
tlsPersistentConnectionStatusId.setMaxAccess(_C)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusId.setStatus(_A)
_TlsPersistentConnectionStatusLocalPort_Type=MxAdvancedIpPort
_TlsPersistentConnectionStatusLocalPort_Object=MibTableColumn
tlsPersistentConnectionStatusLocalPort=_TlsPersistentConnectionStatusLocalPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300,1,300),_TlsPersistentConnectionStatusLocalPort_Type())
tlsPersistentConnectionStatusLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusLocalPort.setStatus(_A)
_TlsPersistentConnectionStatusRemoteHost_Type=OctetString
_TlsPersistentConnectionStatusRemoteHost_Object=MibTableColumn
tlsPersistentConnectionStatusRemoteHost=_TlsPersistentConnectionStatusRemoteHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300,1,400),_TlsPersistentConnectionStatusRemoteHost_Type())
tlsPersistentConnectionStatusRemoteHost.setMaxAccess(_C)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusRemoteHost.setStatus(_A)
_TlsPersistentConnectionStatusRemoteHostIpAddr_Type=OctetString
_TlsPersistentConnectionStatusRemoteHostIpAddr_Object=MibTableColumn
tlsPersistentConnectionStatusRemoteHostIpAddr=_TlsPersistentConnectionStatusRemoteHostIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300,1,450),_TlsPersistentConnectionStatusRemoteHostIpAddr_Type())
tlsPersistentConnectionStatusRemoteHostIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusRemoteHostIpAddr.setStatus(_A)
class _TlsPersistentConnectionStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('up',100),('down',200),('waitingShutdown',300),('waitingUp',400)))
_TlsPersistentConnectionStatusState_Type.__name__=_D
_TlsPersistentConnectionStatusState_Object=MibTableColumn
tlsPersistentConnectionStatusState=_TlsPersistentConnectionStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,100,300,1,500),_TlsPersistentConnectionStatusState_Type())
tlsPersistentConnectionStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:tlsPersistentConnectionStatusState.setStatus(_A)
_ProxyGroup_ObjectIdentity=ObjectIdentity
proxyGroup=_ProxyGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,200))
class _SurvivabilityMode_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('automatic',100),('alwaysOn',200),('disabled',300)))
_SurvivabilityMode_Type.__name__=_D
_SurvivabilityMode_Object=MibScalar
survivabilityMode=_SurvivabilityMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,200,100),_SurvivabilityMode_Type())
survivabilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:survivabilityMode.setStatus(_A)
class _ConfigModifiedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_J,100),('no',200)))
_ConfigModifiedStatus_Type.__name__=_D
_ConfigModifiedStatus_Object=MibScalar
configModifiedStatus=_ConfigModifiedStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,200,300),_ConfigModifiedStatus_Type())
configModifiedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:configModifiedStatus.setStatus(_A)
class _ConfigAppliedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_J,100),('no',200)))
_ConfigAppliedStatus_Type.__name__=_D
_ConfigAppliedStatus_Object=MibScalar
configAppliedStatus=_ConfigAppliedStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,200,400),_ConfigAppliedStatus_Type())
configAppliedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:configAppliedStatus.setStatus(_A)
_NetworkGroup_ObjectIdentity=ObjectIdentity
networkGroup=_NetworkGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,300))
class _NetworkInterface_Type(OctetString):defaultValue=OctetString('Uplink');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_NetworkInterface_Type.__name__=_E
_NetworkInterface_Object=MibScalar
networkInterface=_NetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,300,100),_NetworkInterface_Type())
networkInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterface.setStatus(_A)
class _Port_Type(MxAdvancedIpPort):defaultValue=0
_Port_Type.__name__=_H
_Port_Object=MibScalar
port=_Port_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,300,200),_Port_Type())
port.setMaxAccess(_B)
if mibBuilder.loadTexts:port.setStatus(_A)
class _SecurePort_Type(MxAdvancedIpPort):defaultValue=0
_SecurePort_Type.__name__=_H
_SecurePort_Object=MibScalar
securePort=_SecurePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,300,300),_SecurePort_Type())
securePort.setMaxAccess(_B)
if mibBuilder.loadTexts:securePort.setStatus(_A)
_RegisterGroup_ObjectIdentity=ObjectIdentity
registerGroup=_RegisterGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400))
class _ContactOverrideEnable_Type(MxEnableState):defaultValue=1
_ContactOverrideEnable_Type.__name__=_K
_ContactOverrideEnable_Object=MibScalar
contactOverrideEnable=_ContactOverrideEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,50),_ContactOverrideEnable_Type())
contactOverrideEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:contactOverrideEnable.setStatus(_A)
class _EndpointSurvivabilityExpiration_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_EndpointSurvivabilityExpiration_Type.__name__=_F
_EndpointSurvivabilityExpiration_Object=MibScalar
endpointSurvivabilityExpiration=_EndpointSurvivabilityExpiration_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,100),_EndpointSurvivabilityExpiration_Type())
endpointSurvivabilityExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:endpointSurvivabilityExpiration.setStatus(_A)
class _RelayedThrottlingExpiration_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,86400))
_RelayedThrottlingExpiration_Type.__name__=_F
_RelayedThrottlingExpiration_Object=MibScalar
relayedThrottlingExpiration=_RelayedThrottlingExpiration_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,200),_RelayedThrottlingExpiration_Type())
relayedThrottlingExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:relayedThrottlingExpiration.setStatus(_A)
class _EndpointThrottlingExpiration_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,3600))
_EndpointThrottlingExpiration_Type.__name__=_F
_EndpointThrottlingExpiration_Object=MibScalar
endpointThrottlingExpiration=_EndpointThrottlingExpiration_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,300),_EndpointThrottlingExpiration_Type())
endpointThrottlingExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:endpointThrottlingExpiration.setStatus(_A)
_RegistrationCacheGroup_ObjectIdentity=ObjectIdentity
registrationCacheGroup=_RegistrationCacheGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400))
_RegistrationCacheSearchName_Type=OctetString
_RegistrationCacheSearchName_Object=MibScalar
registrationCacheSearchName=_RegistrationCacheSearchName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,100),_RegistrationCacheSearchName_Type())
registrationCacheSearchName.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchName.setStatus(_A)
class _RegistrationCacheSearchSort_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,1000)));namedValues=NamedValues(*(('aor',100),('contact',200),('receivedTime',300),('endpointExpiration',400),('registrarExpiration',500),('unsorted',1000)))
_RegistrationCacheSearchSort_Type.__name__=_D
_RegistrationCacheSearchSort_Object=MibScalar
registrationCacheSearchSort=_RegistrationCacheSearchSort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,200),_RegistrationCacheSearchSort_Type())
registrationCacheSearchSort.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchSort.setStatus(_A)
_RegistrationCacheSearchResultTable_Object=MibTable
registrationCacheSearchResultTable=_RegistrationCacheSearchResultTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300))
if mibBuilder.loadTexts:registrationCacheSearchResultTable.setStatus(_A)
_RegistrationCacheSearchResultEntry_Object=MibTableRow
registrationCacheSearchResultEntry=_RegistrationCacheSearchResultEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1))
registrationCacheSearchResultEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:registrationCacheSearchResultEntry.setStatus(_A)
_RegistrationCacheSearchResultId_Type=Unsigned32
_RegistrationCacheSearchResultId_Object=MibTableColumn
registrationCacheSearchResultId=_RegistrationCacheSearchResultId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,100),_RegistrationCacheSearchResultId_Type())
registrationCacheSearchResultId.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultId.setStatus(_A)
_RegistrationCacheSearchResultAor_Type=OctetString
_RegistrationCacheSearchResultAor_Object=MibTableColumn
registrationCacheSearchResultAor=_RegistrationCacheSearchResultAor_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,200),_RegistrationCacheSearchResultAor_Type())
registrationCacheSearchResultAor.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultAor.setStatus(_A)
_RegistrationCacheSearchResultContact_Type=OctetString
_RegistrationCacheSearchResultContact_Object=MibTableColumn
registrationCacheSearchResultContact=_RegistrationCacheSearchResultContact_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,300),_RegistrationCacheSearchResultContact_Type())
registrationCacheSearchResultContact.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultContact.setStatus(_A)
_RegistrationCacheSearchResultReceivedTime_Type=OctetString
_RegistrationCacheSearchResultReceivedTime_Object=MibTableColumn
registrationCacheSearchResultReceivedTime=_RegistrationCacheSearchResultReceivedTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,400),_RegistrationCacheSearchResultReceivedTime_Type())
registrationCacheSearchResultReceivedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultReceivedTime.setStatus(_A)
_RegistrationCacheSearchResultEndpointExpiration_Type=OctetString
_RegistrationCacheSearchResultEndpointExpiration_Object=MibTableColumn
registrationCacheSearchResultEndpointExpiration=_RegistrationCacheSearchResultEndpointExpiration_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,500),_RegistrationCacheSearchResultEndpointExpiration_Type())
registrationCacheSearchResultEndpointExpiration.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultEndpointExpiration.setStatus(_A)
_RegistrationCacheSearchResultRegistrarExpiration_Type=OctetString
_RegistrationCacheSearchResultRegistrarExpiration_Object=MibTableColumn
registrationCacheSearchResultRegistrarExpiration=_RegistrationCacheSearchResultRegistrarExpiration_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,550),_RegistrationCacheSearchResultRegistrarExpiration_Type())
registrationCacheSearchResultRegistrarExpiration.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultRegistrarExpiration.setStatus(_A)
class _RegistrationCacheSearchResultRegisteredTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('normal',100),('local',200)))
_RegistrationCacheSearchResultRegisteredTo_Type.__name__=_D
_RegistrationCacheSearchResultRegisteredTo_Object=MibTableColumn
registrationCacheSearchResultRegisteredTo=_RegistrationCacheSearchResultRegisteredTo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,300,1,600),_RegistrationCacheSearchResultRegisteredTo_Type())
registrationCacheSearchResultRegisteredTo.setMaxAccess(_C)
if mibBuilder.loadTexts:registrationCacheSearchResultRegisteredTo.setStatus(_A)
_TotalRegistrationCacheCount_Type=Unsigned32
_TotalRegistrationCacheCount_Object=MibScalar
totalRegistrationCacheCount=_TotalRegistrationCacheCount_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,400,400,400),_TotalRegistrationCacheCount_Type())
totalRegistrationCacheCount.setMaxAccess(_C)
if mibBuilder.loadTexts:totalRegistrationCacheCount.setStatus(_A)
_MonitoringGroup_ObjectIdentity=ObjectIdentity
monitoringGroup=_MonitoringGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,500))
class _MonitoringInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MonitoringInterval_Type.__name__=_F
_MonitoringInterval_Object=MibScalar
monitoringInterval=_MonitoringInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,500,100),_MonitoringInterval_Type())
monitoringInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:monitoringInterval.setStatus(_A)
class _MonitoringToggleDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_MonitoringToggleDelay_Type.__name__=_F
_MonitoringToggleDelay_Object=MibScalar
monitoringToggleDelay=_MonitoringToggleDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,500,200),_MonitoringToggleDelay_Type())
monitoringToggleDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:monitoringToggleDelay.setStatus(_A)
class _MonitoringDestination_Type(MxIpHostNamePort):defaultValue=OctetString('')
_MonitoringDestination_Type.__name__=_I
_MonitoringDestination_Object=MibScalar
monitoringDestination=_MonitoringDestination_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,500,300),_MonitoringDestination_Type())
monitoringDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:monitoringDestination.setStatus(_A)
class _KeepAliveOptionErrorCodes_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_KeepAliveOptionErrorCodes_Type.__name__=_E
_KeepAliveOptionErrorCodes_Object=MibScalar
keepAliveOptionErrorCodes=_KeepAliveOptionErrorCodes_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,500,400),_KeepAliveOptionErrorCodes_Type())
keepAliveOptionErrorCodes.setMaxAccess(_B)
if mibBuilder.loadTexts:keepAliveOptionErrorCodes.setStatus(_A)
_OptionGroup_ObjectIdentity=ObjectIdentity
optionGroup=_OptionGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,600))
class _SipOptionsMethodSupport_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('default',100),('acceptAll',200),('rejectAll',300)))
_SipOptionsMethodSupport_Type.__name__=_D
_SipOptionsMethodSupport_Object=MibScalar
sipOptionsMethodSupport=_SipOptionsMethodSupport_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,600,100),_SipOptionsMethodSupport_Type())
sipOptionsMethodSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:sipOptionsMethodSupport.setStatus(_A)
_RoutingGroup_ObjectIdentity=ObjectIdentity
routingGroup=_RoutingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700))
_RouteTable_Object=MibTable
routeTable=_RouteTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100))
if mibBuilder.loadTexts:routeTable.setStatus(_A)
_RouteEntry_Object=MibTableRow
routeEntry=_RouteEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1))
routeEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:routeEntry.setStatus(_A)
_RouteId_Type=Unsigned32
_RouteId_Object=MibTableColumn
routeId=_RouteId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,100),_RouteId_Type())
routeId.setMaxAccess(_C)
if mibBuilder.loadTexts:routeId.setStatus(_A)
class _RoutePriority_Type(Unsigned32):defaultValue=1
_RoutePriority_Type.__name__=_F
_RoutePriority_Object=MibTableColumn
routePriority=_RoutePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,200),_RoutePriority_Type())
routePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:routePriority.setStatus(_A)
class _RouteCriteriaType_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*(('toUri',100),('toUser',200),('toHost',300),('contactUri',400),('contactUser',500),('contactHost',600)))
_RouteCriteriaType_Type.__name__=_D
_RouteCriteriaType_Object=MibTableColumn
routeCriteriaType=_RouteCriteriaType_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,300),_RouteCriteriaType_Type())
routeCriteriaType.setMaxAccess(_B)
if mibBuilder.loadTexts:routeCriteriaType.setStatus(_A)
class _RouteCriteriaExpression_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RouteCriteriaExpression_Type.__name__=_E
_RouteCriteriaExpression_Object=MibTableColumn
routeCriteriaExpression=_RouteCriteriaExpression_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,400),_RouteCriteriaExpression_Type())
routeCriteriaExpression.setMaxAccess(_B)
if mibBuilder.loadTexts:routeCriteriaExpression.setStatus(_A)
class _RouteTargetType_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('registeredAor',100),('registeredAorUser',200),('hardcodedHost',300)))
_RouteTargetType_Type.__name__=_D
_RouteTargetType_Object=MibTableColumn
routeTargetType=_RouteTargetType_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,500),_RouteTargetType_Type())
routeTargetType.setMaxAccess(_B)
if mibBuilder.loadTexts:routeTargetType.setStatus(_A)
class _RouteTargetUserTransformationName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RouteTargetUserTransformationName_Type.__name__=_E
_RouteTargetUserTransformationName_Object=MibTableColumn
routeTargetUserTransformationName=_RouteTargetUserTransformationName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,600),_RouteTargetUserTransformationName_Type())
routeTargetUserTransformationName.setMaxAccess(_B)
if mibBuilder.loadTexts:routeTargetUserTransformationName.setStatus(_A)
class _RouteRegisteredUserTransformationName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RouteRegisteredUserTransformationName_Type.__name__=_E
_RouteRegisteredUserTransformationName_Object=MibTableColumn
routeRegisteredUserTransformationName=_RouteRegisteredUserTransformationName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,700),_RouteRegisteredUserTransformationName_Type())
routeRegisteredUserTransformationName.setMaxAccess(_B)
if mibBuilder.loadTexts:routeRegisteredUserTransformationName.setStatus(_A)
class _RouteHardcodedHostPort_Type(MxIpHostNamePort):defaultValue=OctetString('')
_RouteHardcodedHostPort_Type.__name__=_I
_RouteHardcodedHostPort_Object=MibTableColumn
routeHardcodedHostPort=_RouteHardcodedHostPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,800),_RouteHardcodedHostPort_Type())
routeHardcodedHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:routeHardcodedHostPort.setStatus(_A)
class _RouteConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*(('valid',100),(_O,200),('missingHardcodedHostport',300),('inexistentTargetUserTransformation',400),('inexistentRegisteredUserTransformation',500),(_P,600)))
_RouteConfigStatus_Type.__name__=_D
_RouteConfigStatus_Object=MibTableColumn
routeConfigStatus=_RouteConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,2000),_RouteConfigStatus_Type())
routeConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:routeConfigStatus.setStatus(_A)
class _RouteDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),(_Q,10)))
_RouteDelete_Type.__name__=_D
_RouteDelete_Object=MibTableColumn
routeDelete=_RouteDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,100,1,2100),_RouteDelete_Type())
routeDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:routeDelete.setStatus(_A)
_UserTransformationsTable_Object=MibTable
userTransformationsTable=_UserTransformationsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300))
if mibBuilder.loadTexts:userTransformationsTable.setStatus(_A)
_UserTransformationsEntry_Object=MibTableRow
userTransformationsEntry=_UserTransformationsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1))
userTransformationsEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:userTransformationsEntry.setStatus(_A)
_UserTransformationsId_Type=Unsigned32
_UserTransformationsId_Object=MibTableColumn
userTransformationsId=_UserTransformationsId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,100),_UserTransformationsId_Type())
userTransformationsId.setMaxAccess(_C)
if mibBuilder.loadTexts:userTransformationsId.setStatus(_A)
class _UserTransformationsPriority_Type(Unsigned32):defaultValue=1
_UserTransformationsPriority_Type.__name__=_F
_UserTransformationsPriority_Object=MibTableColumn
userTransformationsPriority=_UserTransformationsPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,200),_UserTransformationsPriority_Type())
userTransformationsPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:userTransformationsPriority.setStatus(_A)
class _UserTransformationsName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_UserTransformationsName_Type.__name__=_E
_UserTransformationsName_Object=MibTableColumn
userTransformationsName=_UserTransformationsName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,300),_UserTransformationsName_Type())
userTransformationsName.setMaxAccess(_B)
if mibBuilder.loadTexts:userTransformationsName.setStatus(_A)
class _UserTransformationsCriteria_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_UserTransformationsCriteria_Type.__name__=_E
_UserTransformationsCriteria_Object=MibTableColumn
userTransformationsCriteria=_UserTransformationsCriteria_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,400),_UserTransformationsCriteria_Type())
userTransformationsCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:userTransformationsCriteria.setStatus(_A)
class _UserTransformationsPattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,250))
_UserTransformationsPattern_Type.__name__=_E
_UserTransformationsPattern_Object=MibTableColumn
userTransformationsPattern=_UserTransformationsPattern_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,500),_UserTransformationsPattern_Type())
userTransformationsPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:userTransformationsPattern.setStatus(_A)
class _UserTransformationsConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('valid',100),(_O,200),('missingName',300),(_P,400)))
_UserTransformationsConfigStatus_Type.__name__=_D
_UserTransformationsConfigStatus_Object=MibTableColumn
userTransformationsConfigStatus=_UserTransformationsConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,2000),_UserTransformationsConfigStatus_Type())
userTransformationsConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:userTransformationsConfigStatus.setStatus(_A)
class _UserTransformationsDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),(_Q,10)))
_UserTransformationsDelete_Type.__name__=_D
_UserTransformationsDelete_Object=MibTableColumn
userTransformationsDelete=_UserTransformationsDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,700,300,1,2100),_UserTransformationsDelete_Type())
userTransformationsDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:userTransformationsDelete.setStatus(_A)
_InteropGroup_ObjectIdentity=ObjectIdentity
interopGroup=_InteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,800))
class _InteropRequestTransactionTimeout_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_InteropRequestTransactionTimeout_Type.__name__=_F
_InteropRequestTransactionTimeout_Object=MibScalar
interopRequestTransactionTimeout=_InteropRequestTransactionTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,800,100),_InteropRequestTransactionTimeout_Type())
interopRequestTransactionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:interopRequestTransactionTimeout.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),(_J,100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4600,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'sipProxyMIB':sipProxyMIB,'sipProxyMIBObjects':sipProxyMIBObjects,'statusGroup':statusGroup,'monitoringState':monitoringState,'proxyStatus':proxyStatus,'nbActiveCalls':nbActiveCalls,'tlsPersistentConnectionStatusTable':tlsPersistentConnectionStatusTable,'tlsPersistentConnectionStatusEntry':tlsPersistentConnectionStatusEntry,_L:tlsPersistentConnectionStatusId,'tlsPersistentConnectionStatusLocalPort':tlsPersistentConnectionStatusLocalPort,'tlsPersistentConnectionStatusRemoteHost':tlsPersistentConnectionStatusRemoteHost,'tlsPersistentConnectionStatusRemoteHostIpAddr':tlsPersistentConnectionStatusRemoteHostIpAddr,'tlsPersistentConnectionStatusState':tlsPersistentConnectionStatusState,'proxyGroup':proxyGroup,'survivabilityMode':survivabilityMode,'configModifiedStatus':configModifiedStatus,'configAppliedStatus':configAppliedStatus,'networkGroup':networkGroup,'networkInterface':networkInterface,'port':port,'securePort':securePort,'registerGroup':registerGroup,'contactOverrideEnable':contactOverrideEnable,'endpointSurvivabilityExpiration':endpointSurvivabilityExpiration,'relayedThrottlingExpiration':relayedThrottlingExpiration,'endpointThrottlingExpiration':endpointThrottlingExpiration,'registrationCacheGroup':registrationCacheGroup,'registrationCacheSearchName':registrationCacheSearchName,'registrationCacheSearchSort':registrationCacheSearchSort,'registrationCacheSearchResultTable':registrationCacheSearchResultTable,'registrationCacheSearchResultEntry':registrationCacheSearchResultEntry,_M:registrationCacheSearchResultId,'registrationCacheSearchResultAor':registrationCacheSearchResultAor,'registrationCacheSearchResultContact':registrationCacheSearchResultContact,'registrationCacheSearchResultReceivedTime':registrationCacheSearchResultReceivedTime,'registrationCacheSearchResultEndpointExpiration':registrationCacheSearchResultEndpointExpiration,'registrationCacheSearchResultRegistrarExpiration':registrationCacheSearchResultRegistrarExpiration,'registrationCacheSearchResultRegisteredTo':registrationCacheSearchResultRegisteredTo,'totalRegistrationCacheCount':totalRegistrationCacheCount,'monitoringGroup':monitoringGroup,'monitoringInterval':monitoringInterval,'monitoringToggleDelay':monitoringToggleDelay,'monitoringDestination':monitoringDestination,'keepAliveOptionErrorCodes':keepAliveOptionErrorCodes,'optionGroup':optionGroup,'sipOptionsMethodSupport':sipOptionsMethodSupport,'routingGroup':routingGroup,'routeTable':routeTable,'routeEntry':routeEntry,_N:routeId,'routePriority':routePriority,'routeCriteriaType':routeCriteriaType,'routeCriteriaExpression':routeCriteriaExpression,'routeTargetType':routeTargetType,'routeTargetUserTransformationName':routeTargetUserTransformationName,'routeRegisteredUserTransformationName':routeRegisteredUserTransformationName,'routeHardcodedHostPort':routeHardcodedHostPort,'routeConfigStatus':routeConfigStatus,'routeDelete':routeDelete,'userTransformationsTable':userTransformationsTable,'userTransformationsEntry':userTransformationsEntry,_R:userTransformationsId,'userTransformationsPriority':userTransformationsPriority,'userTransformationsName':userTransformationsName,'userTransformationsCriteria':userTransformationsCriteria,'userTransformationsPattern':userTransformationsPattern,'userTransformationsConfigStatus':userTransformationsConfigStatus,'userTransformationsDelete':userTransformationsDelete,'interopGroup':interopGroup,'interopRequestTransactionTimeout':interopRequestTransactionTimeout,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})