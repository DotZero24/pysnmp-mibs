_z='copsDeviceConfigGroup'
_y='copsDeviceStatusGroup'
_x='copsClientServerConfigRetryIntvl'
_w='copsClientServerConfigRetryCount'
_v='copsClientServerConfigRetryAlgrm'
_u='copsClientServerConfigRowStatus'
_t='copsClientServerConfigPriority'
_s='copsClientServerConfigTcpPort'
_r='copsClientErrAuthMissing'
_q='copsClientErrAuthFailures'
_p='copsClientKaTimedoutClients'
_o='copsClientErrWrongOpcode'
_n='copsClientErrWrongObjects'
_m='copsClientErrBadSends'
_l='copsClientErrBadCtype'
_k='copsClientErrUnknownCnum'
_j='copsClientErrUnknownOpcode'
_i='copsClientErrLengthMismatch'
_h='copsClientErrUnsupportedVersion'
_g='copsClientErrUnsupportClienttype'
_f='copsClientOpenFailures'
_e='copsClientOpenAttempts'
_d='copsClientTcpConnectFailures'
_c='copsClientTcpConnectAttempts'
_b='copsClientLastError'
_a='copsClientInErrs'
_Z='copsClientOutPkts'
_Y='copsClientInPkts'
_X='copsClientServerAccountingTime'
_W='copsClientServerKeepaliveTime'
_V='copsClientState'
_U='copsClientServerLastConnAttempt'
_T='copsClientServerAuthType'
_S='copsClientServerType'
_R='copsClientServerTcpPort'
_Q='copsClientCapabilities'
_P='copsClientServerConfigAuthType'
_O='copsClientServerConfigClientType'
_N='copsClientServerConfigAddress'
_M='copsClientServerConfigAddrType'
_L='copsClientServerClientType'
_K='copsClientServerAddress'
_J='copsClientServerAddressType'
_I='TimeInterval'
_H='Unsigned32'
_G='read-write'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='COPS-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I,'TimeStamp')
copsClientMIB=ModuleIdentity((1,3,6,1,2,1,89))
if mibBuilder.loadTexts:copsClientMIB.setRevisions(('2000-09-28 00:00',))
class CopsClientState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('copsClientInvalid',1),('copsClientTcpconnected',2),('copsClientAuthenticating',3),('copsClientSecAccepted',4),('copsClientAccepted',5),('copsClientTimingout',6)))
class CopsServerEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copsServerStatic',1),('copsServerRedirect',2)))
class CopsErrorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('errorOther',0),('errorBadHandle',1),('errorInvalidHandleReference',2),('errorBadMessageFormat',3),('errorUnableToProcess',4),('errorMandatoryClientSiMissing',5),('errorUnsupportedClientType',6),('errorMandatoryCopsObjectMissing',7),('errorClientFailure',8),('errorCommunicationFailure',9),('errorUnspecified',10),('errorShuttingDown',11),('errorRedirectToPreferredServer',12),('errorUnknownCopsObject',13),('errorAuthenticationFailure',14),('errorAuthenticationMissing',15)))
class CopsTcpPort(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class CopsAuthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('authNone',0),('authOther',1),('authIpSecAh',2),('authIpSecEsp',3),('authTls',4),('authCopsIntegrity',5)))
_CopsClientMIBObjects_ObjectIdentity=ObjectIdentity
copsClientMIBObjects=_CopsClientMIBObjects_ObjectIdentity((1,3,6,1,2,1,89,1))
_CopsClientCapabilitiesGroup_ObjectIdentity=ObjectIdentity
copsClientCapabilitiesGroup=_CopsClientCapabilitiesGroup_ObjectIdentity((1,3,6,1,2,1,89,1,1))
class _CopsClientCapabilities_Type(Bits):namedValues=NamedValues(*(('copsClientVersion1',0),('copsClientAuthIpSecAh',1),('copsClientAuthIpSecEsp',2),('copsClientAuthTls',3),('copsClientAuthInteg',4)))
_CopsClientCapabilities_Type.__name__='Bits'
_CopsClientCapabilities_Object=MibScalar
copsClientCapabilities=_CopsClientCapabilities_Object((1,3,6,1,2,1,89,1,1,1),_CopsClientCapabilities_Type())
copsClientCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientCapabilities.setStatus(_A)
_CopsClientStatusGroup_ObjectIdentity=ObjectIdentity
copsClientStatusGroup=_CopsClientStatusGroup_ObjectIdentity((1,3,6,1,2,1,89,1,2))
_CopsClientServerCurrentTable_Object=MibTable
copsClientServerCurrentTable=_CopsClientServerCurrentTable_Object((1,3,6,1,2,1,89,1,2,1))
if mibBuilder.loadTexts:copsClientServerCurrentTable.setStatus(_A)
_CopsClientServerCurrentEntry_Object=MibTableRow
copsClientServerCurrentEntry=_CopsClientServerCurrentEntry_Object((1,3,6,1,2,1,89,1,2,1,1))
copsClientServerCurrentEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:copsClientServerCurrentEntry.setStatus(_A)
_CopsClientServerAddressType_Type=InetAddressType
_CopsClientServerAddressType_Object=MibTableColumn
copsClientServerAddressType=_CopsClientServerAddressType_Object((1,3,6,1,2,1,89,1,2,1,1,1),_CopsClientServerAddressType_Type())
copsClientServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerAddressType.setStatus(_A)
_CopsClientServerAddress_Type=InetAddress
_CopsClientServerAddress_Object=MibTableColumn
copsClientServerAddress=_CopsClientServerAddress_Object((1,3,6,1,2,1,89,1,2,1,1,2),_CopsClientServerAddress_Type())
copsClientServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerAddress.setStatus(_A)
class _CopsClientServerClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CopsClientServerClientType_Type.__name__=_E
_CopsClientServerClientType_Object=MibTableColumn
copsClientServerClientType=_CopsClientServerClientType_Object((1,3,6,1,2,1,89,1,2,1,1,3),_CopsClientServerClientType_Type())
copsClientServerClientType.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerClientType.setStatus(_A)
_CopsClientServerTcpPort_Type=CopsTcpPort
_CopsClientServerTcpPort_Object=MibTableColumn
copsClientServerTcpPort=_CopsClientServerTcpPort_Object((1,3,6,1,2,1,89,1,2,1,1,4),_CopsClientServerTcpPort_Type())
copsClientServerTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientServerTcpPort.setStatus(_A)
_CopsClientServerType_Type=CopsServerEntryType
_CopsClientServerType_Object=MibTableColumn
copsClientServerType=_CopsClientServerType_Object((1,3,6,1,2,1,89,1,2,1,1,5),_CopsClientServerType_Type())
copsClientServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientServerType.setStatus(_A)
_CopsClientServerAuthType_Type=CopsAuthType
_CopsClientServerAuthType_Object=MibTableColumn
copsClientServerAuthType=_CopsClientServerAuthType_Object((1,3,6,1,2,1,89,1,2,1,1,6),_CopsClientServerAuthType_Type())
copsClientServerAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientServerAuthType.setStatus(_A)
_CopsClientServerLastConnAttempt_Type=TimeStamp
_CopsClientServerLastConnAttempt_Object=MibTableColumn
copsClientServerLastConnAttempt=_CopsClientServerLastConnAttempt_Object((1,3,6,1,2,1,89,1,2,1,1,7),_CopsClientServerLastConnAttempt_Type())
copsClientServerLastConnAttempt.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientServerLastConnAttempt.setStatus(_A)
_CopsClientState_Type=CopsClientState
_CopsClientState_Object=MibTableColumn
copsClientState=_CopsClientState_Object((1,3,6,1,2,1,89,1,2,1,1,8),_CopsClientState_Type())
copsClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientState.setStatus(_A)
_CopsClientServerKeepaliveTime_Type=TimeInterval
_CopsClientServerKeepaliveTime_Object=MibTableColumn
copsClientServerKeepaliveTime=_CopsClientServerKeepaliveTime_Object((1,3,6,1,2,1,89,1,2,1,1,9),_CopsClientServerKeepaliveTime_Type())
copsClientServerKeepaliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientServerKeepaliveTime.setStatus(_A)
_CopsClientServerAccountingTime_Type=TimeInterval
_CopsClientServerAccountingTime_Object=MibTableColumn
copsClientServerAccountingTime=_CopsClientServerAccountingTime_Object((1,3,6,1,2,1,89,1,2,1,1,10),_CopsClientServerAccountingTime_Type())
copsClientServerAccountingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientServerAccountingTime.setStatus(_A)
_CopsClientInPkts_Type=Counter32
_CopsClientInPkts_Object=MibTableColumn
copsClientInPkts=_CopsClientInPkts_Object((1,3,6,1,2,1,89,1,2,1,1,11),_CopsClientInPkts_Type())
copsClientInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientInPkts.setStatus(_A)
_CopsClientOutPkts_Type=Counter32
_CopsClientOutPkts_Object=MibTableColumn
copsClientOutPkts=_CopsClientOutPkts_Object((1,3,6,1,2,1,89,1,2,1,1,12),_CopsClientOutPkts_Type())
copsClientOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientOutPkts.setStatus(_A)
_CopsClientInErrs_Type=Counter32
_CopsClientInErrs_Object=MibTableColumn
copsClientInErrs=_CopsClientInErrs_Object((1,3,6,1,2,1,89,1,2,1,1,13),_CopsClientInErrs_Type())
copsClientInErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientInErrs.setStatus(_A)
_CopsClientLastError_Type=CopsErrorCode
_CopsClientLastError_Object=MibTableColumn
copsClientLastError=_CopsClientLastError_Object((1,3,6,1,2,1,89,1,2,1,1,14),_CopsClientLastError_Type())
copsClientLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientLastError.setStatus(_A)
_CopsClientTcpConnectAttempts_Type=Counter32
_CopsClientTcpConnectAttempts_Object=MibTableColumn
copsClientTcpConnectAttempts=_CopsClientTcpConnectAttempts_Object((1,3,6,1,2,1,89,1,2,1,1,15),_CopsClientTcpConnectAttempts_Type())
copsClientTcpConnectAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientTcpConnectAttempts.setStatus(_A)
_CopsClientTcpConnectFailures_Type=Counter32
_CopsClientTcpConnectFailures_Object=MibTableColumn
copsClientTcpConnectFailures=_CopsClientTcpConnectFailures_Object((1,3,6,1,2,1,89,1,2,1,1,16),_CopsClientTcpConnectFailures_Type())
copsClientTcpConnectFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientTcpConnectFailures.setStatus(_A)
_CopsClientOpenAttempts_Type=Counter32
_CopsClientOpenAttempts_Object=MibTableColumn
copsClientOpenAttempts=_CopsClientOpenAttempts_Object((1,3,6,1,2,1,89,1,2,1,1,17),_CopsClientOpenAttempts_Type())
copsClientOpenAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientOpenAttempts.setStatus(_A)
_CopsClientOpenFailures_Type=Counter32
_CopsClientOpenFailures_Object=MibTableColumn
copsClientOpenFailures=_CopsClientOpenFailures_Object((1,3,6,1,2,1,89,1,2,1,1,18),_CopsClientOpenFailures_Type())
copsClientOpenFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientOpenFailures.setStatus(_A)
_CopsClientErrUnsupportClienttype_Type=Counter32
_CopsClientErrUnsupportClienttype_Object=MibTableColumn
copsClientErrUnsupportClienttype=_CopsClientErrUnsupportClienttype_Object((1,3,6,1,2,1,89,1,2,1,1,19),_CopsClientErrUnsupportClienttype_Type())
copsClientErrUnsupportClienttype.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrUnsupportClienttype.setStatus(_A)
_CopsClientErrUnsupportedVersion_Type=Counter32
_CopsClientErrUnsupportedVersion_Object=MibTableColumn
copsClientErrUnsupportedVersion=_CopsClientErrUnsupportedVersion_Object((1,3,6,1,2,1,89,1,2,1,1,20),_CopsClientErrUnsupportedVersion_Type())
copsClientErrUnsupportedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrUnsupportedVersion.setStatus(_A)
_CopsClientErrLengthMismatch_Type=Counter32
_CopsClientErrLengthMismatch_Object=MibTableColumn
copsClientErrLengthMismatch=_CopsClientErrLengthMismatch_Object((1,3,6,1,2,1,89,1,2,1,1,21),_CopsClientErrLengthMismatch_Type())
copsClientErrLengthMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrLengthMismatch.setStatus(_A)
_CopsClientErrUnknownOpcode_Type=Counter32
_CopsClientErrUnknownOpcode_Object=MibTableColumn
copsClientErrUnknownOpcode=_CopsClientErrUnknownOpcode_Object((1,3,6,1,2,1,89,1,2,1,1,22),_CopsClientErrUnknownOpcode_Type())
copsClientErrUnknownOpcode.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrUnknownOpcode.setStatus(_A)
_CopsClientErrUnknownCnum_Type=Counter32
_CopsClientErrUnknownCnum_Object=MibTableColumn
copsClientErrUnknownCnum=_CopsClientErrUnknownCnum_Object((1,3,6,1,2,1,89,1,2,1,1,23),_CopsClientErrUnknownCnum_Type())
copsClientErrUnknownCnum.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrUnknownCnum.setStatus(_A)
_CopsClientErrBadCtype_Type=Counter32
_CopsClientErrBadCtype_Object=MibTableColumn
copsClientErrBadCtype=_CopsClientErrBadCtype_Object((1,3,6,1,2,1,89,1,2,1,1,24),_CopsClientErrBadCtype_Type())
copsClientErrBadCtype.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrBadCtype.setStatus(_A)
_CopsClientErrBadSends_Type=Counter32
_CopsClientErrBadSends_Object=MibTableColumn
copsClientErrBadSends=_CopsClientErrBadSends_Object((1,3,6,1,2,1,89,1,2,1,1,25),_CopsClientErrBadSends_Type())
copsClientErrBadSends.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrBadSends.setStatus(_A)
_CopsClientErrWrongObjects_Type=Counter32
_CopsClientErrWrongObjects_Object=MibTableColumn
copsClientErrWrongObjects=_CopsClientErrWrongObjects_Object((1,3,6,1,2,1,89,1,2,1,1,26),_CopsClientErrWrongObjects_Type())
copsClientErrWrongObjects.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrWrongObjects.setStatus(_A)
_CopsClientErrWrongOpcode_Type=Counter32
_CopsClientErrWrongOpcode_Object=MibTableColumn
copsClientErrWrongOpcode=_CopsClientErrWrongOpcode_Object((1,3,6,1,2,1,89,1,2,1,1,27),_CopsClientErrWrongOpcode_Type())
copsClientErrWrongOpcode.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrWrongOpcode.setStatus(_A)
_CopsClientKaTimedoutClients_Type=Counter32
_CopsClientKaTimedoutClients_Object=MibTableColumn
copsClientKaTimedoutClients=_CopsClientKaTimedoutClients_Object((1,3,6,1,2,1,89,1,2,1,1,28),_CopsClientKaTimedoutClients_Type())
copsClientKaTimedoutClients.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientKaTimedoutClients.setStatus(_A)
_CopsClientErrAuthFailures_Type=Counter32
_CopsClientErrAuthFailures_Object=MibTableColumn
copsClientErrAuthFailures=_CopsClientErrAuthFailures_Object((1,3,6,1,2,1,89,1,2,1,1,29),_CopsClientErrAuthFailures_Type())
copsClientErrAuthFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrAuthFailures.setStatus(_A)
_CopsClientErrAuthMissing_Type=Counter32
_CopsClientErrAuthMissing_Object=MibTableColumn
copsClientErrAuthMissing=_CopsClientErrAuthMissing_Object((1,3,6,1,2,1,89,1,2,1,1,30),_CopsClientErrAuthMissing_Type())
copsClientErrAuthMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:copsClientErrAuthMissing.setStatus(_A)
_CopsClientConfigGroup_ObjectIdentity=ObjectIdentity
copsClientConfigGroup=_CopsClientConfigGroup_ObjectIdentity((1,3,6,1,2,1,89,1,3))
_CopsClientServerConfigTable_Object=MibTable
copsClientServerConfigTable=_CopsClientServerConfigTable_Object((1,3,6,1,2,1,89,1,3,1))
if mibBuilder.loadTexts:copsClientServerConfigTable.setStatus(_A)
_CopsClientServerConfigEntry_Object=MibTableRow
copsClientServerConfigEntry=_CopsClientServerConfigEntry_Object((1,3,6,1,2,1,89,1,3,1,1))
copsClientServerConfigEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:copsClientServerConfigEntry.setStatus(_A)
_CopsClientServerConfigAddrType_Type=InetAddressType
_CopsClientServerConfigAddrType_Object=MibTableColumn
copsClientServerConfigAddrType=_CopsClientServerConfigAddrType_Object((1,3,6,1,2,1,89,1,3,1,1,1),_CopsClientServerConfigAddrType_Type())
copsClientServerConfigAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerConfigAddrType.setStatus(_A)
_CopsClientServerConfigAddress_Type=InetAddress
_CopsClientServerConfigAddress_Object=MibTableColumn
copsClientServerConfigAddress=_CopsClientServerConfigAddress_Object((1,3,6,1,2,1,89,1,3,1,1,2),_CopsClientServerConfigAddress_Type())
copsClientServerConfigAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerConfigAddress.setStatus(_A)
class _CopsClientServerConfigClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CopsClientServerConfigClientType_Type.__name__=_E
_CopsClientServerConfigClientType_Object=MibTableColumn
copsClientServerConfigClientType=_CopsClientServerConfigClientType_Object((1,3,6,1,2,1,89,1,3,1,1,3),_CopsClientServerConfigClientType_Type())
copsClientServerConfigClientType.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerConfigClientType.setStatus(_A)
_CopsClientServerConfigAuthType_Type=CopsAuthType
_CopsClientServerConfigAuthType_Object=MibTableColumn
copsClientServerConfigAuthType=_CopsClientServerConfigAuthType_Object((1,3,6,1,2,1,89,1,3,1,1,4),_CopsClientServerConfigAuthType_Type())
copsClientServerConfigAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:copsClientServerConfigAuthType.setStatus(_A)
_CopsClientServerConfigTcpPort_Type=CopsTcpPort
_CopsClientServerConfigTcpPort_Object=MibTableColumn
copsClientServerConfigTcpPort=_CopsClientServerConfigTcpPort_Object((1,3,6,1,2,1,89,1,3,1,1,5),_CopsClientServerConfigTcpPort_Type())
copsClientServerConfigTcpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:copsClientServerConfigTcpPort.setStatus(_A)
_CopsClientServerConfigPriority_Type=Integer32
_CopsClientServerConfigPriority_Object=MibTableColumn
copsClientServerConfigPriority=_CopsClientServerConfigPriority_Object((1,3,6,1,2,1,89,1,3,1,1,6),_CopsClientServerConfigPriority_Type())
copsClientServerConfigPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:copsClientServerConfigPriority.setStatus(_A)
_CopsClientServerConfigRowStatus_Type=RowStatus
_CopsClientServerConfigRowStatus_Object=MibTableColumn
copsClientServerConfigRowStatus=_CopsClientServerConfigRowStatus_Object((1,3,6,1,2,1,89,1,3,1,1,7),_CopsClientServerConfigRowStatus_Type())
copsClientServerConfigRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:copsClientServerConfigRowStatus.setStatus(_A)
class _CopsClientServerConfigRetryAlgrm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('sequential',2),('roundRobin',3)))
_CopsClientServerConfigRetryAlgrm_Type.__name__=_E
_CopsClientServerConfigRetryAlgrm_Object=MibScalar
copsClientServerConfigRetryAlgrm=_CopsClientServerConfigRetryAlgrm_Object((1,3,6,1,2,1,89,1,3,2),_CopsClientServerConfigRetryAlgrm_Type())
copsClientServerConfigRetryAlgrm.setMaxAccess(_G)
if mibBuilder.loadTexts:copsClientServerConfigRetryAlgrm.setStatus(_A)
class _CopsClientServerConfigRetryCount_Type(Unsigned32):defaultValue=1
_CopsClientServerConfigRetryCount_Type.__name__=_H
_CopsClientServerConfigRetryCount_Object=MibScalar
copsClientServerConfigRetryCount=_CopsClientServerConfigRetryCount_Object((1,3,6,1,2,1,89,1,3,3),_CopsClientServerConfigRetryCount_Type())
copsClientServerConfigRetryCount.setMaxAccess(_G)
if mibBuilder.loadTexts:copsClientServerConfigRetryCount.setStatus(_A)
class _CopsClientServerConfigRetryIntvl_Type(TimeInterval):defaultValue=1000
_CopsClientServerConfigRetryIntvl_Type.__name__=_I
_CopsClientServerConfigRetryIntvl_Object=MibScalar
copsClientServerConfigRetryIntvl=_CopsClientServerConfigRetryIntvl_Object((1,3,6,1,2,1,89,1,3,4),_CopsClientServerConfigRetryIntvl_Type())
copsClientServerConfigRetryIntvl.setMaxAccess(_G)
if mibBuilder.loadTexts:copsClientServerConfigRetryIntvl.setStatus(_A)
if mibBuilder.loadTexts:copsClientServerConfigRetryIntvl.setUnits('centi-seconds')
_CopsClientConformance_ObjectIdentity=ObjectIdentity
copsClientConformance=_CopsClientConformance_ObjectIdentity((1,3,6,1,2,1,89,2))
_CopsClientGroups_ObjectIdentity=ObjectIdentity
copsClientGroups=_CopsClientGroups_ObjectIdentity((1,3,6,1,2,1,89,2,1))
_CopsClientCompliances_ObjectIdentity=ObjectIdentity
copsClientCompliances=_CopsClientCompliances_ObjectIdentity((1,3,6,1,2,1,89,2,2))
copsDeviceStatusGroup=ObjectGroup((1,3,6,1,2,1,89,2,1,1))
copsDeviceStatusGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:copsDeviceStatusGroup.setStatus(_A)
copsDeviceConfigGroup=ObjectGroup((1,3,6,1,2,1,89,2,1,2))
copsDeviceConfigGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:copsDeviceConfigGroup.setStatus(_A)
copsClientCompliance=ModuleCompliance((1,3,6,1,2,1,89,2,2,1))
copsClientCompliance.setObjects(*((_B,_y),(_B,_z)))
if mibBuilder.loadTexts:copsClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CopsClientState':CopsClientState,'CopsServerEntryType':CopsServerEntryType,'CopsErrorCode':CopsErrorCode,'CopsTcpPort':CopsTcpPort,'CopsAuthType':CopsAuthType,'copsClientMIB':copsClientMIB,'copsClientMIBObjects':copsClientMIBObjects,'copsClientCapabilitiesGroup':copsClientCapabilitiesGroup,_Q:copsClientCapabilities,'copsClientStatusGroup':copsClientStatusGroup,'copsClientServerCurrentTable':copsClientServerCurrentTable,'copsClientServerCurrentEntry':copsClientServerCurrentEntry,_J:copsClientServerAddressType,_K:copsClientServerAddress,_L:copsClientServerClientType,_R:copsClientServerTcpPort,_S:copsClientServerType,_T:copsClientServerAuthType,_U:copsClientServerLastConnAttempt,_V:copsClientState,_W:copsClientServerKeepaliveTime,_X:copsClientServerAccountingTime,_Y:copsClientInPkts,_Z:copsClientOutPkts,_a:copsClientInErrs,_b:copsClientLastError,_c:copsClientTcpConnectAttempts,_d:copsClientTcpConnectFailures,_e:copsClientOpenAttempts,_f:copsClientOpenFailures,_g:copsClientErrUnsupportClienttype,_h:copsClientErrUnsupportedVersion,_i:copsClientErrLengthMismatch,_j:copsClientErrUnknownOpcode,_k:copsClientErrUnknownCnum,_l:copsClientErrBadCtype,_m:copsClientErrBadSends,_n:copsClientErrWrongObjects,_o:copsClientErrWrongOpcode,_p:copsClientKaTimedoutClients,_q:copsClientErrAuthFailures,_r:copsClientErrAuthMissing,'copsClientConfigGroup':copsClientConfigGroup,'copsClientServerConfigTable':copsClientServerConfigTable,'copsClientServerConfigEntry':copsClientServerConfigEntry,_M:copsClientServerConfigAddrType,_N:copsClientServerConfigAddress,_O:copsClientServerConfigClientType,_P:copsClientServerConfigAuthType,_s:copsClientServerConfigTcpPort,_t:copsClientServerConfigPriority,_u:copsClientServerConfigRowStatus,_v:copsClientServerConfigRetryAlgrm,_w:copsClientServerConfigRetryCount,_x:copsClientServerConfigRetryIntvl,'copsClientConformance':copsClientConformance,'copsClientGroups':copsClientGroups,_y:copsDeviceStatusGroup,_z:copsDeviceConfigGroup,'copsClientCompliances':copsClientCompliances,'copsClientCompliance':copsClientCompliance})