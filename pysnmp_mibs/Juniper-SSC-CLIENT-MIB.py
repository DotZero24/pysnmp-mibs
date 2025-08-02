_A5='juniSscClientGroup4'
_A4='juniSscClientGroup3'
_A3='juniSscClientGroup2'
_A2='juniSscClientGroup'
_A1='juniSscClientDeleteDiscoversSent'
_A0='juniSscClientCreateDiscoversSent'
_z='juniSscClientDiscoverTransitions'
_y='juniSscClientActiveDiscovers'
_x='juniSscClientDiscoversSeen'
_w='DisplayString'
_v='juniSscClientVersion'
_u='juniSscClientTransportRouterName'
_t='juniSscClientLocalAddress'
_s='juniSscClientAuthenticationFailures'
_r='juniSscClientAuthenticationSuccesses'
_q='juniSscClientDeleteTokensSent'
_p='juniSscClientCreateTokensSent'
_o='juniSscClientTokenTransitions'
_n='juniSscClientActiveTokens'
_m='juniSscClientTokensSeen'
_l='juniSscClientDeleteAddressesSent'
_k='juniSscClientCreateAddressesSent'
_j='juniSscClientAddressTransitions'
_i='juniSscClientActiveAddresses'
_h='juniSscClientCommunicationErrors'
_g='juniSscClientInternalErrors'
_f='juniSscClientSynchronizeCompletesSent'
_e='juniSscClientSynchronizesReceived'
_d='juniSscClientIpInterfaceTransitions'
_c='juniSscClientActiveIpInterfaces'
_b='juniSscClientDeleteInterfacesSent'
_a='juniSscClientCreateInterfacesSent'
_Z='juniSscClientConnectionClosedRemotely'
_Y='juniSscClientConnectionClosedSent'
_X='juniSscClientConnectionOpenCompletes'
_W='juniSscClientConnectionOpenRequests'
_V='juniSscClientPolicyReportsSent'
_U='juniSscClientErrorPolicyCommandsReceived'
_T='juniSscClientBadPolicyCommandsReceived'
_S='juniSscClientPolicyCommandsAcctReceived'
_R='juniSscClientPolicyCommandsListReceived'
_Q='juniSscClientPolicyCommandsReceived'
_P='juniSscClientActivePort'
_O='juniSscClientConnectionState'
_N='juniSscClientActiveAddress'
_M='juniSscClientTertiaryPort'
_L='juniSscClientTertiaryAddress'
_K='juniSscClientSecondaryPort'
_J='juniSscClientSecondaryAddress'
_I='juniSscClientPrimaryPort'
_H='juniSscClientPrimaryAddress'
_G='juniSscClientServerSwitchoverTimeout'
_F='Integer32'
_E='read-write'
_D='obsolete'
_C='read-only'
_B='current'
_A='Juniper-SSC-CLIENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniName,=mibBuilder.importSymbols('Juniper-TC','JuniName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_w,'PhysAddress','TextualConvention')
juniSscClientMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,36))
if mibBuilder.loadTexts:juniSscClientMIB.setRevisions(('2003-12-18 16:29','2002-09-16 21:44','2002-01-14 20:15','2001-01-23 21:30','2000-02-17 23:10'))
_JuniSscClientObjects_ObjectIdentity=ObjectIdentity
juniSscClientObjects=_JuniSscClientObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1))
_JuniSscClientCfg_ObjectIdentity=ObjectIdentity
juniSscClientCfg=_JuniSscClientCfg_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1,1))
_JuniSscClientCfgScalars_ObjectIdentity=ObjectIdentity
juniSscClientCfgScalars=_JuniSscClientCfgScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1,1,1))
class _JuniSscClientServerSwitchoverTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_JuniSscClientServerSwitchoverTimeout_Type.__name__=_F
_JuniSscClientServerSwitchoverTimeout_Object=MibScalar
juniSscClientServerSwitchoverTimeout=_JuniSscClientServerSwitchoverTimeout_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,1),_JuniSscClientServerSwitchoverTimeout_Type())
juniSscClientServerSwitchoverTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientServerSwitchoverTimeout.setStatus(_B)
if mibBuilder.loadTexts:juniSscClientServerSwitchoverTimeout.setUnits('seconds')
_JuniSscClientPrimaryAddress_Type=IpAddress
_JuniSscClientPrimaryAddress_Object=MibScalar
juniSscClientPrimaryAddress=_JuniSscClientPrimaryAddress_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,2),_JuniSscClientPrimaryAddress_Type())
juniSscClientPrimaryAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientPrimaryAddress.setStatus(_B)
class _JuniSscClientPrimaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniSscClientPrimaryPort_Type.__name__=_F
_JuniSscClientPrimaryPort_Object=MibScalar
juniSscClientPrimaryPort=_JuniSscClientPrimaryPort_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,3),_JuniSscClientPrimaryPort_Type())
juniSscClientPrimaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientPrimaryPort.setStatus(_B)
_JuniSscClientSecondaryAddress_Type=IpAddress
_JuniSscClientSecondaryAddress_Object=MibScalar
juniSscClientSecondaryAddress=_JuniSscClientSecondaryAddress_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,4),_JuniSscClientSecondaryAddress_Type())
juniSscClientSecondaryAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientSecondaryAddress.setStatus(_B)
class _JuniSscClientSecondaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniSscClientSecondaryPort_Type.__name__=_F
_JuniSscClientSecondaryPort_Object=MibScalar
juniSscClientSecondaryPort=_JuniSscClientSecondaryPort_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,5),_JuniSscClientSecondaryPort_Type())
juniSscClientSecondaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientSecondaryPort.setStatus(_B)
_JuniSscClientTertiaryAddress_Type=IpAddress
_JuniSscClientTertiaryAddress_Object=MibScalar
juniSscClientTertiaryAddress=_JuniSscClientTertiaryAddress_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,6),_JuniSscClientTertiaryAddress_Type())
juniSscClientTertiaryAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientTertiaryAddress.setStatus(_B)
class _JuniSscClientTertiaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniSscClientTertiaryPort_Type.__name__=_F
_JuniSscClientTertiaryPort_Object=MibScalar
juniSscClientTertiaryPort=_JuniSscClientTertiaryPort_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,7),_JuniSscClientTertiaryPort_Type())
juniSscClientTertiaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientTertiaryPort.setStatus(_B)
_JuniSscClientLocalAddress_Type=IpAddress
_JuniSscClientLocalAddress_Object=MibScalar
juniSscClientLocalAddress=_JuniSscClientLocalAddress_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,8),_JuniSscClientLocalAddress_Type())
juniSscClientLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientLocalAddress.setStatus(_B)
_JuniSscClientTransportRouterName_Type=JuniName
_JuniSscClientTransportRouterName_Object=MibScalar
juniSscClientTransportRouterName=_JuniSscClientTransportRouterName_Object((1,3,6,1,4,1,4874,2,2,36,1,1,1,9),_JuniSscClientTransportRouterName_Type())
juniSscClientTransportRouterName.setMaxAccess(_E)
if mibBuilder.loadTexts:juniSscClientTransportRouterName.setStatus(_B)
_JuniSscClientStatus_ObjectIdentity=ObjectIdentity
juniSscClientStatus=_JuniSscClientStatus_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1,2))
_JuniSscClientStatusScalars_ObjectIdentity=ObjectIdentity
juniSscClientStatusScalars=_JuniSscClientStatusScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1,2,1))
class _JuniSscClientConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disconnected',0),('trying',1),('connected',2)))
_JuniSscClientConnectionState_Type.__name__=_F
_JuniSscClientConnectionState_Object=MibScalar
juniSscClientConnectionState=_JuniSscClientConnectionState_Object((1,3,6,1,4,1,4874,2,2,36,1,2,1,1),_JuniSscClientConnectionState_Type())
juniSscClientConnectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientConnectionState.setStatus(_B)
_JuniSscClientActiveAddress_Type=IpAddress
_JuniSscClientActiveAddress_Object=MibScalar
juniSscClientActiveAddress=_JuniSscClientActiveAddress_Object((1,3,6,1,4,1,4874,2,2,36,1,2,1,2),_JuniSscClientActiveAddress_Type())
juniSscClientActiveAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientActiveAddress.setStatus(_B)
class _JuniSscClientActivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniSscClientActivePort_Type.__name__=_F
_JuniSscClientActivePort_Object=MibScalar
juniSscClientActivePort=_JuniSscClientActivePort_Object((1,3,6,1,4,1,4874,2,2,36,1,2,1,3),_JuniSscClientActivePort_Type())
juniSscClientActivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientActivePort.setStatus(_B)
class _JuniSscClientVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_JuniSscClientVersion_Type.__name__=_w
_JuniSscClientVersion_Object=MibScalar
juniSscClientVersion=_JuniSscClientVersion_Object((1,3,6,1,4,1,4874,2,2,36,1,2,1,4),_JuniSscClientVersion_Type())
juniSscClientVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientVersion.setStatus(_B)
_JuniSscClientStatistics_ObjectIdentity=ObjectIdentity
juniSscClientStatistics=_JuniSscClientStatistics_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1,3))
_JuniSscClientStatisticsScalars_ObjectIdentity=ObjectIdentity
juniSscClientStatisticsScalars=_JuniSscClientStatisticsScalars_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,1,3,1))
_JuniSscClientPolicyCommandsReceived_Type=Counter32
_JuniSscClientPolicyCommandsReceived_Object=MibScalar
juniSscClientPolicyCommandsReceived=_JuniSscClientPolicyCommandsReceived_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,1),_JuniSscClientPolicyCommandsReceived_Type())
juniSscClientPolicyCommandsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientPolicyCommandsReceived.setStatus(_B)
_JuniSscClientPolicyCommandsListReceived_Type=Counter32
_JuniSscClientPolicyCommandsListReceived_Object=MibScalar
juniSscClientPolicyCommandsListReceived=_JuniSscClientPolicyCommandsListReceived_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,2),_JuniSscClientPolicyCommandsListReceived_Type())
juniSscClientPolicyCommandsListReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientPolicyCommandsListReceived.setStatus(_B)
_JuniSscClientPolicyCommandsAcctReceived_Type=Counter32
_JuniSscClientPolicyCommandsAcctReceived_Object=MibScalar
juniSscClientPolicyCommandsAcctReceived=_JuniSscClientPolicyCommandsAcctReceived_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,3),_JuniSscClientPolicyCommandsAcctReceived_Type())
juniSscClientPolicyCommandsAcctReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientPolicyCommandsAcctReceived.setStatus(_B)
_JuniSscClientBadPolicyCommandsReceived_Type=Counter32
_JuniSscClientBadPolicyCommandsReceived_Object=MibScalar
juniSscClientBadPolicyCommandsReceived=_JuniSscClientBadPolicyCommandsReceived_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,4),_JuniSscClientBadPolicyCommandsReceived_Type())
juniSscClientBadPolicyCommandsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientBadPolicyCommandsReceived.setStatus(_B)
_JuniSscClientErrorPolicyCommandsReceived_Type=Counter32
_JuniSscClientErrorPolicyCommandsReceived_Object=MibScalar
juniSscClientErrorPolicyCommandsReceived=_JuniSscClientErrorPolicyCommandsReceived_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,5),_JuniSscClientErrorPolicyCommandsReceived_Type())
juniSscClientErrorPolicyCommandsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientErrorPolicyCommandsReceived.setStatus(_B)
_JuniSscClientPolicyReportsSent_Type=Counter32
_JuniSscClientPolicyReportsSent_Object=MibScalar
juniSscClientPolicyReportsSent=_JuniSscClientPolicyReportsSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,6),_JuniSscClientPolicyReportsSent_Type())
juniSscClientPolicyReportsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientPolicyReportsSent.setStatus(_B)
_JuniSscClientConnectionOpenRequests_Type=Counter32
_JuniSscClientConnectionOpenRequests_Object=MibScalar
juniSscClientConnectionOpenRequests=_JuniSscClientConnectionOpenRequests_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,7),_JuniSscClientConnectionOpenRequests_Type())
juniSscClientConnectionOpenRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientConnectionOpenRequests.setStatus(_B)
_JuniSscClientConnectionOpenCompletes_Type=Counter32
_JuniSscClientConnectionOpenCompletes_Object=MibScalar
juniSscClientConnectionOpenCompletes=_JuniSscClientConnectionOpenCompletes_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,8),_JuniSscClientConnectionOpenCompletes_Type())
juniSscClientConnectionOpenCompletes.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientConnectionOpenCompletes.setStatus(_B)
_JuniSscClientConnectionClosedSent_Type=Counter32
_JuniSscClientConnectionClosedSent_Object=MibScalar
juniSscClientConnectionClosedSent=_JuniSscClientConnectionClosedSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,9),_JuniSscClientConnectionClosedSent_Type())
juniSscClientConnectionClosedSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientConnectionClosedSent.setStatus(_B)
_JuniSscClientConnectionClosedRemotely_Type=Counter32
_JuniSscClientConnectionClosedRemotely_Object=MibScalar
juniSscClientConnectionClosedRemotely=_JuniSscClientConnectionClosedRemotely_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,10),_JuniSscClientConnectionClosedRemotely_Type())
juniSscClientConnectionClosedRemotely.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientConnectionClosedRemotely.setStatus(_B)
_JuniSscClientCreateInterfacesSent_Type=Counter32
_JuniSscClientCreateInterfacesSent_Object=MibScalar
juniSscClientCreateInterfacesSent=_JuniSscClientCreateInterfacesSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,11),_JuniSscClientCreateInterfacesSent_Type())
juniSscClientCreateInterfacesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientCreateInterfacesSent.setStatus(_B)
_JuniSscClientDeleteInterfacesSent_Type=Counter32
_JuniSscClientDeleteInterfacesSent_Object=MibScalar
juniSscClientDeleteInterfacesSent=_JuniSscClientDeleteInterfacesSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,12),_JuniSscClientDeleteInterfacesSent_Type())
juniSscClientDeleteInterfacesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientDeleteInterfacesSent.setStatus(_B)
_JuniSscClientActiveIpInterfaces_Type=Counter32
_JuniSscClientActiveIpInterfaces_Object=MibScalar
juniSscClientActiveIpInterfaces=_JuniSscClientActiveIpInterfaces_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,13),_JuniSscClientActiveIpInterfaces_Type())
juniSscClientActiveIpInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientActiveIpInterfaces.setStatus(_B)
_JuniSscClientIpInterfaceTransitions_Type=Counter32
_JuniSscClientIpInterfaceTransitions_Object=MibScalar
juniSscClientIpInterfaceTransitions=_JuniSscClientIpInterfaceTransitions_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,14),_JuniSscClientIpInterfaceTransitions_Type())
juniSscClientIpInterfaceTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientIpInterfaceTransitions.setStatus(_B)
_JuniSscClientSynchronizesReceived_Type=Counter32
_JuniSscClientSynchronizesReceived_Object=MibScalar
juniSscClientSynchronizesReceived=_JuniSscClientSynchronizesReceived_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,15),_JuniSscClientSynchronizesReceived_Type())
juniSscClientSynchronizesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientSynchronizesReceived.setStatus(_B)
_JuniSscClientSynchronizeCompletesSent_Type=Counter32
_JuniSscClientSynchronizeCompletesSent_Object=MibScalar
juniSscClientSynchronizeCompletesSent=_JuniSscClientSynchronizeCompletesSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,16),_JuniSscClientSynchronizeCompletesSent_Type())
juniSscClientSynchronizeCompletesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientSynchronizeCompletesSent.setStatus(_B)
_JuniSscClientInternalErrors_Type=Counter32
_JuniSscClientInternalErrors_Object=MibScalar
juniSscClientInternalErrors=_JuniSscClientInternalErrors_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,17),_JuniSscClientInternalErrors_Type())
juniSscClientInternalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientInternalErrors.setStatus(_B)
_JuniSscClientCommunicationErrors_Type=Counter32
_JuniSscClientCommunicationErrors_Object=MibScalar
juniSscClientCommunicationErrors=_JuniSscClientCommunicationErrors_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,18),_JuniSscClientCommunicationErrors_Type())
juniSscClientCommunicationErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientCommunicationErrors.setStatus(_B)
_JuniSscClientTokensSeen_Type=Counter32
_JuniSscClientTokensSeen_Object=MibScalar
juniSscClientTokensSeen=_JuniSscClientTokensSeen_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,19),_JuniSscClientTokensSeen_Type())
juniSscClientTokensSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientTokensSeen.setStatus(_D)
_JuniSscClientActiveTokens_Type=Counter32
_JuniSscClientActiveTokens_Object=MibScalar
juniSscClientActiveTokens=_JuniSscClientActiveTokens_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,20),_JuniSscClientActiveTokens_Type())
juniSscClientActiveTokens.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientActiveTokens.setStatus(_D)
_JuniSscClientTokenTransitions_Type=Counter32
_JuniSscClientTokenTransitions_Object=MibScalar
juniSscClientTokenTransitions=_JuniSscClientTokenTransitions_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,21),_JuniSscClientTokenTransitions_Type())
juniSscClientTokenTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientTokenTransitions.setStatus(_D)
_JuniSscClientCreateTokensSent_Type=Counter32
_JuniSscClientCreateTokensSent_Object=MibScalar
juniSscClientCreateTokensSent=_JuniSscClientCreateTokensSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,22),_JuniSscClientCreateTokensSent_Type())
juniSscClientCreateTokensSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientCreateTokensSent.setStatus(_D)
_JuniSscClientDeleteTokensSent_Type=Counter32
_JuniSscClientDeleteTokensSent_Object=MibScalar
juniSscClientDeleteTokensSent=_JuniSscClientDeleteTokensSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,23),_JuniSscClientDeleteTokensSent_Type())
juniSscClientDeleteTokensSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientDeleteTokensSent.setStatus(_D)
_JuniSscClientActiveAddresses_Type=Counter32
_JuniSscClientActiveAddresses_Object=MibScalar
juniSscClientActiveAddresses=_JuniSscClientActiveAddresses_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,24),_JuniSscClientActiveAddresses_Type())
juniSscClientActiveAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientActiveAddresses.setStatus(_B)
_JuniSscClientAddressTransitions_Type=Counter32
_JuniSscClientAddressTransitions_Object=MibScalar
juniSscClientAddressTransitions=_JuniSscClientAddressTransitions_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,25),_JuniSscClientAddressTransitions_Type())
juniSscClientAddressTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientAddressTransitions.setStatus(_B)
_JuniSscClientCreateAddressesSent_Type=Counter32
_JuniSscClientCreateAddressesSent_Object=MibScalar
juniSscClientCreateAddressesSent=_JuniSscClientCreateAddressesSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,26),_JuniSscClientCreateAddressesSent_Type())
juniSscClientCreateAddressesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientCreateAddressesSent.setStatus(_B)
_JuniSscClientDeleteAddressesSent_Type=Counter32
_JuniSscClientDeleteAddressesSent_Object=MibScalar
juniSscClientDeleteAddressesSent=_JuniSscClientDeleteAddressesSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,27),_JuniSscClientDeleteAddressesSent_Type())
juniSscClientDeleteAddressesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientDeleteAddressesSent.setStatus(_B)
_JuniSscClientAuthenticationSuccesses_Type=Counter32
_JuniSscClientAuthenticationSuccesses_Object=MibScalar
juniSscClientAuthenticationSuccesses=_JuniSscClientAuthenticationSuccesses_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,28),_JuniSscClientAuthenticationSuccesses_Type())
juniSscClientAuthenticationSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientAuthenticationSuccesses.setStatus(_D)
_JuniSscClientAuthenticationFailures_Type=Counter32
_JuniSscClientAuthenticationFailures_Object=MibScalar
juniSscClientAuthenticationFailures=_JuniSscClientAuthenticationFailures_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,29),_JuniSscClientAuthenticationFailures_Type())
juniSscClientAuthenticationFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientAuthenticationFailures.setStatus(_D)
_JuniSscClientDiscoversSeen_Type=Counter32
_JuniSscClientDiscoversSeen_Object=MibScalar
juniSscClientDiscoversSeen=_JuniSscClientDiscoversSeen_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,30),_JuniSscClientDiscoversSeen_Type())
juniSscClientDiscoversSeen.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientDiscoversSeen.setStatus(_B)
_JuniSscClientActiveDiscovers_Type=Counter32
_JuniSscClientActiveDiscovers_Object=MibScalar
juniSscClientActiveDiscovers=_JuniSscClientActiveDiscovers_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,31),_JuniSscClientActiveDiscovers_Type())
juniSscClientActiveDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientActiveDiscovers.setStatus(_B)
_JuniSscClientDiscoverTransitions_Type=Counter32
_JuniSscClientDiscoverTransitions_Object=MibScalar
juniSscClientDiscoverTransitions=_JuniSscClientDiscoverTransitions_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,32),_JuniSscClientDiscoverTransitions_Type())
juniSscClientDiscoverTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientDiscoverTransitions.setStatus(_B)
_JuniSscClientCreateDiscoversSent_Type=Counter32
_JuniSscClientCreateDiscoversSent_Object=MibScalar
juniSscClientCreateDiscoversSent=_JuniSscClientCreateDiscoversSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,33),_JuniSscClientCreateDiscoversSent_Type())
juniSscClientCreateDiscoversSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientCreateDiscoversSent.setStatus(_B)
_JuniSscClientDeleteDiscoversSent_Type=Counter32
_JuniSscClientDeleteDiscoversSent_Object=MibScalar
juniSscClientDeleteDiscoversSent=_JuniSscClientDeleteDiscoversSent_Object((1,3,6,1,4,1,4874,2,2,36,1,3,1,34),_JuniSscClientDeleteDiscoversSent_Type())
juniSscClientDeleteDiscoversSent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniSscClientDeleteDiscoversSent.setStatus(_B)
_JuniSscClientMIBConformance_ObjectIdentity=ObjectIdentity
juniSscClientMIBConformance=_JuniSscClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,4))
_JuniSscClientMIBCompliances_ObjectIdentity=ObjectIdentity
juniSscClientMIBCompliances=_JuniSscClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,4,1))
_JuniSscClientMIBGroups_ObjectIdentity=ObjectIdentity
juniSscClientMIBGroups=_JuniSscClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,36,4,2))
juniSscClientGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,36,4,2,1))
juniSscClientGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:juniSscClientGroup.setStatus(_D)
juniSscClientGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,36,4,2,2))
juniSscClientGroup2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:juniSscClientGroup2.setStatus(_D)
juniSscClientGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,36,4,2,3))
juniSscClientGroup3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_t),(_A,_u),(_A,_N),(_A,_O),(_A,_P),(_A,_v),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:juniSscClientGroup3.setStatus(_D)
juniSscClientGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,36,4,2,4))
juniSscClientGroup4.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_t),(_A,_u),(_A,_N),(_A,_O),(_A,_P),(_A,_v),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:juniSscClientGroup4.setStatus(_B)
juniSscClientAuthCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,36,4,1,1))
juniSscClientAuthCompliance.setObjects((_A,_A2))
if mibBuilder.loadTexts:juniSscClientAuthCompliance.setStatus(_D)
juniSscClientAuthCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,36,4,1,2))
juniSscClientAuthCompliance2.setObjects((_A,_A3))
if mibBuilder.loadTexts:juniSscClientAuthCompliance2.setStatus(_D)
juniSscClientAuthCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,36,4,1,3))
juniSscClientAuthCompliance3.setObjects((_A,_A4))
if mibBuilder.loadTexts:juniSscClientAuthCompliance3.setStatus(_D)
juniSscClientAuthCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,36,4,1,4))
juniSscClientAuthCompliance4.setObjects((_A,_A5))
if mibBuilder.loadTexts:juniSscClientAuthCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniSscClientMIB':juniSscClientMIB,'juniSscClientObjects':juniSscClientObjects,'juniSscClientCfg':juniSscClientCfg,'juniSscClientCfgScalars':juniSscClientCfgScalars,_G:juniSscClientServerSwitchoverTimeout,_H:juniSscClientPrimaryAddress,_I:juniSscClientPrimaryPort,_J:juniSscClientSecondaryAddress,_K:juniSscClientSecondaryPort,_L:juniSscClientTertiaryAddress,_M:juniSscClientTertiaryPort,_t:juniSscClientLocalAddress,_u:juniSscClientTransportRouterName,'juniSscClientStatus':juniSscClientStatus,'juniSscClientStatusScalars':juniSscClientStatusScalars,_O:juniSscClientConnectionState,_N:juniSscClientActiveAddress,_P:juniSscClientActivePort,_v:juniSscClientVersion,'juniSscClientStatistics':juniSscClientStatistics,'juniSscClientStatisticsScalars':juniSscClientStatisticsScalars,_Q:juniSscClientPolicyCommandsReceived,_R:juniSscClientPolicyCommandsListReceived,_S:juniSscClientPolicyCommandsAcctReceived,_T:juniSscClientBadPolicyCommandsReceived,_U:juniSscClientErrorPolicyCommandsReceived,_V:juniSscClientPolicyReportsSent,_W:juniSscClientConnectionOpenRequests,_X:juniSscClientConnectionOpenCompletes,_Y:juniSscClientConnectionClosedSent,_Z:juniSscClientConnectionClosedRemotely,_a:juniSscClientCreateInterfacesSent,_b:juniSscClientDeleteInterfacesSent,_c:juniSscClientActiveIpInterfaces,_d:juniSscClientIpInterfaceTransitions,_e:juniSscClientSynchronizesReceived,_f:juniSscClientSynchronizeCompletesSent,_g:juniSscClientInternalErrors,_h:juniSscClientCommunicationErrors,_m:juniSscClientTokensSeen,_n:juniSscClientActiveTokens,_o:juniSscClientTokenTransitions,_p:juniSscClientCreateTokensSent,_q:juniSscClientDeleteTokensSent,_i:juniSscClientActiveAddresses,_j:juniSscClientAddressTransitions,_k:juniSscClientCreateAddressesSent,_l:juniSscClientDeleteAddressesSent,_r:juniSscClientAuthenticationSuccesses,_s:juniSscClientAuthenticationFailures,_x:juniSscClientDiscoversSeen,_y:juniSscClientActiveDiscovers,_z:juniSscClientDiscoverTransitions,_A0:juniSscClientCreateDiscoversSent,_A1:juniSscClientDeleteDiscoversSent,'juniSscClientMIBConformance':juniSscClientMIBConformance,'juniSscClientMIBCompliances':juniSscClientMIBCompliances,'juniSscClientAuthCompliance':juniSscClientAuthCompliance,'juniSscClientAuthCompliance2':juniSscClientAuthCompliance2,'juniSscClientAuthCompliance3':juniSscClientAuthCompliance3,'juniSscClientAuthCompliance4':juniSscClientAuthCompliance4,'juniSscClientMIBGroups':juniSscClientMIBGroups,_A2:juniSscClientGroup,_A3:juniSscClientGroup2,_A4:juniSscClientGroup3,_A5:juniSscClientGroup4})