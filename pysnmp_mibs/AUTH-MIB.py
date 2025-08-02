_A7='swGuestVlanId'
_A6='swCompoundAuthPortIndex'
_A5='swAuthMacAddress'
_A4='swAuthPortNumber'
_A3='swMacBasedPaeMac'
_A2='swMacBasedPaePort'
_A1='reauthenticate'
_A0='swMacBasedPaePortNumber'
_z='swAuthenticatedPortNumber'
_y='unauthorized'
_x='authorized'
_w='notTerminatedYet'
_v='portAdminDisabled'
_u='portReInit'
_t='authControlForceUnauth'
_s='reauthFailed'
_r='supplicantRestart'
_q='portFailure'
_p='supplicantLogoff'
_o='localAuthServer'
_n='remoteAuthServer'
_m='swRadiusAcctServiceIndex'
_l='swRadiusAuthServerIndex'
_k='swRadiusServerIndex'
_j='DisplayString'
_i='InetAddressType'
_h='dot1xPaePortNumber'
_g='IEEE8021-PAE-MIB'
_f='none'
_e='idle'
_d='timeout'
_c='fail'
_b='success'
_a='response'
_Z='request'
_Y='forceUnauth'
_X='forceAuth'
_W='held'
_V='aborting'
_U='authenticated'
_T='connecting'
_S='disconnected'
_R='OctetString'
_Q='swDot1xAuthMACAddress'
_P='swDot1xAuthVID'
_O='swDot1xAuthPortNumber'
_N='authenticating'
_M='swPaePortNumber'
_L='swPaeMacAddr'
_K='disabled'
_J='enabled'
_I='initialize'
_H='Unsigned32'
_G='not-accessible'
_F='obsolete'
_E='read-write'
_D='AUTH-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PaeControlledPortStatus,dot1xPaePortNumber=mibBuilder.importSymbols(_g,'PaeControlledPortStatus',_h)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_i)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_j,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
swAuthCtrl=ModuleIdentity((1,3,6,1,4,1,171,12,3))
class PortList(TextualConvention,OctetString):status=_A
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwAuthenCtrl_ObjectIdentity=ObjectIdentity
swAuthenCtrl=_SwAuthenCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,3,1))
class _AuthProtocol_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('authProtocolNone',1),('authProtocolLocal',2),('authProtocolRadius',3),('authProtocolRadiusEap',4),('authProtocolRadiusChap',5),('authProtocolTacacs',6)))
_AuthProtocol_Type.__name__=_C
_AuthProtocol_Object=MibScalar
authProtocol=_AuthProtocol_Object((1,3,6,1,4,1,171,12,3,1,1),_AuthProtocol_Type())
authProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:authProtocol.setStatus(_A)
class _SwAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portBase',1),('macBase',2)))
_SwAuthMode_Type.__name__=_C
_SwAuthMode_Object=MibScalar
swAuthMode=_SwAuthMode_Object((1,3,6,1,4,1,171,12,3,1,2),_SwAuthMode_Type())
swAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthMode.setStatus(_A)
class _SwAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwAuthorizationState_Type.__name__=_C
_SwAuthorizationState_Object=MibScalar
swAuthorizationState=_SwAuthorizationState_Object((1,3,6,1,4,1,171,12,3,1,3),_SwAuthorizationState_Type())
swAuthorizationState.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthorizationState.setStatus(_A)
class _SwAuthFailOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwAuthFailOver_Type.__name__=_C
_SwAuthFailOver_Object=MibScalar
swAuthFailOver=_SwAuthFailOver_Object((1,3,6,1,4,1,171,12,3,1,4),_SwAuthFailOver_Type())
swAuthFailOver.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthFailOver.setStatus(_A)
_SwRadiusCtrl_ObjectIdentity=ObjectIdentity
swRadiusCtrl=_SwRadiusCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,3,2))
class _SwRadiusDeadTime_Type(Unsigned32):defaultValue=1
_SwRadiusDeadTime_Type.__name__=_H
_SwRadiusDeadTime_Object=MibScalar
swRadiusDeadTime=_SwRadiusDeadTime_Object((1,3,6,1,4,1,171,12,3,2,1),_SwRadiusDeadTime_Type())
swRadiusDeadTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusDeadTime.setStatus(_A)
class _SwRadiusTimeout_Type(Unsigned32):defaultValue=10
_SwRadiusTimeout_Type.__name__=_H
_SwRadiusTimeout_Object=MibScalar
swRadiusTimeout=_SwRadiusTimeout_Object((1,3,6,1,4,1,171,12,3,2,2),_SwRadiusTimeout_Type())
swRadiusTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusTimeout.setStatus(_A)
class _SwRadiusRetransmitAttempts_Type(Unsigned32):defaultValue=2
_SwRadiusRetransmitAttempts_Type.__name__=_H
_SwRadiusRetransmitAttempts_Object=MibScalar
swRadiusRetransmitAttempts=_SwRadiusRetransmitAttempts_Object((1,3,6,1,4,1,171,12,3,2,3),_SwRadiusRetransmitAttempts_Type())
swRadiusRetransmitAttempts.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusRetransmitAttempts.setStatus(_A)
_SwRadiusServerTable_Object=MibTable
swRadiusServerTable=_SwRadiusServerTable_Object((1,3,6,1,4,1,171,12,3,2,4))
if mibBuilder.loadTexts:swRadiusServerTable.setStatus(_A)
_SwRadiusServerEntry_Object=MibTableRow
swRadiusServerEntry=_SwRadiusServerEntry_Object((1,3,6,1,4,1,171,12,3,2,4,1))
swRadiusServerEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:swRadiusServerEntry.setStatus(_A)
class _SwRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('swRadiusServerIndex-first',1),('swRadiusServerIndex-second',2),('swRadiusServerIndex-third',3)))
_SwRadiusServerIndex_Type.__name__=_C
_SwRadiusServerIndex_Object=MibTableColumn
swRadiusServerIndex=_SwRadiusServerIndex_Object((1,3,6,1,4,1,171,12,3,2,4,1,1),_SwRadiusServerIndex_Type())
swRadiusServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerIndex.setStatus(_A)
_SwRadiusServerIpAddr_Type=IpAddress
_SwRadiusServerIpAddr_Object=MibTableColumn
swRadiusServerIpAddr=_SwRadiusServerIpAddr_Object((1,3,6,1,4,1,171,12,3,2,4,1,2),_SwRadiusServerIpAddr_Type())
swRadiusServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerIpAddr.setStatus(_F)
class _SwRadiusServerKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwRadiusServerKey_Type.__name__=_R
_SwRadiusServerKey_Object=MibTableColumn
swRadiusServerKey=_SwRadiusServerKey_Object((1,3,6,1,4,1,171,12,3,2,4,1,3),_SwRadiusServerKey_Type())
swRadiusServerKey.setMaxAccess(_G)
if mibBuilder.loadTexts:swRadiusServerKey.setStatus(_A)
class _SwRadiusAuthPortNumber_Type(Unsigned32):defaultValue=1812
_SwRadiusAuthPortNumber_Type.__name__=_H
_SwRadiusAuthPortNumber_Object=MibTableColumn
swRadiusAuthPortNumber=_SwRadiusAuthPortNumber_Object((1,3,6,1,4,1,171,12,3,2,4,1,4),_SwRadiusAuthPortNumber_Type())
swRadiusAuthPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthPortNumber.setStatus(_A)
class _SwRadiusAcctPortNumber_Type(Unsigned32):defaultValue=1813
_SwRadiusAcctPortNumber_Type.__name__=_H
_SwRadiusAcctPortNumber_Object=MibTableColumn
swRadiusAcctPortNumber=_SwRadiusAcctPortNumber_Object((1,3,6,1,4,1,171,12,3,2,4,1,5),_SwRadiusAcctPortNumber_Type())
swRadiusAcctPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAcctPortNumber.setStatus(_A)
_SwRadiusServerStatus_Type=RowStatus
_SwRadiusServerStatus_Object=MibTableColumn
swRadiusServerStatus=_SwRadiusServerStatus_Object((1,3,6,1,4,1,171,12,3,2,4,1,6),_SwRadiusServerStatus_Type())
swRadiusServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerStatus.setStatus(_A)
class _SwRadiusServerTimeout_Type(Unsigned32):defaultValue=5
_SwRadiusServerTimeout_Type.__name__=_H
_SwRadiusServerTimeout_Object=MibTableColumn
swRadiusServerTimeout=_SwRadiusServerTimeout_Object((1,3,6,1,4,1,171,12,3,2,4,1,7),_SwRadiusServerTimeout_Type())
swRadiusServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerTimeout.setStatus(_A)
class _SwRadiusServerRetransmit_Type(Unsigned32):defaultValue=2
_SwRadiusServerRetransmit_Type.__name__=_H
_SwRadiusServerRetransmit_Object=MibTableColumn
swRadiusServerRetransmit=_SwRadiusServerRetransmit_Object((1,3,6,1,4,1,171,12,3,2,4,1,8),_SwRadiusServerRetransmit_Type())
swRadiusServerRetransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerRetransmit.setStatus(_A)
class _SwRadiusServerAddrType_Type(InetAddressType):defaultValue=1
_SwRadiusServerAddrType_Type.__name__=_i
_SwRadiusServerAddrType_Object=MibTableColumn
swRadiusServerAddrType=_SwRadiusServerAddrType_Object((1,3,6,1,4,1,171,12,3,2,4,1,9),_SwRadiusServerAddrType_Type())
swRadiusServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerAddrType.setStatus(_A)
_SwRadiusServerAddr_Type=InetAddress
_SwRadiusServerAddr_Object=MibTableColumn
swRadiusServerAddr=_SwRadiusServerAddr_Object((1,3,6,1,4,1,171,12,3,2,4,1,10),_SwRadiusServerAddr_Type())
swRadiusServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusServerAddr.setStatus(_A)
class _SwRadiusVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwRadiusVrfName_Type.__name__=_j
_SwRadiusVrfName_Object=MibScalar
swRadiusVrfName=_SwRadiusVrfName_Object((1,3,6,1,4,1,171,12,3,2,5),_SwRadiusVrfName_Type())
swRadiusVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusVrfName.setStatus(_A)
_SwRadiusAuthInfo_ObjectIdentity=ObjectIdentity
swRadiusAuthInfo=_SwRadiusAuthInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,3))
class _SwRadiusAuthClientIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SwRadiusAuthClientIdentifier_Type.__name__=_R
_SwRadiusAuthClientIdentifier_Object=MibScalar
swRadiusAuthClientIdentifier=_SwRadiusAuthClientIdentifier_Object((1,3,6,1,4,1,171,12,3,3,1),_SwRadiusAuthClientIdentifier_Type())
swRadiusAuthClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientIdentifier.setStatus(_F)
_SwRadiusAuthClientInvalidServerAddresses_Type=Counter32
_SwRadiusAuthClientInvalidServerAddresses_Object=MibScalar
swRadiusAuthClientInvalidServerAddresses=_SwRadiusAuthClientInvalidServerAddresses_Object((1,3,6,1,4,1,171,12,3,3,2),_SwRadiusAuthClientInvalidServerAddresses_Type())
swRadiusAuthClientInvalidServerAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientInvalidServerAddresses.setStatus(_F)
_SwRadiusAuthServerTable_Object=MibTable
swRadiusAuthServerTable=_SwRadiusAuthServerTable_Object((1,3,6,1,4,1,171,12,3,3,3))
if mibBuilder.loadTexts:swRadiusAuthServerTable.setStatus(_A)
_SwRadiusAuthServerEntry_Object=MibTableRow
swRadiusAuthServerEntry=_SwRadiusAuthServerEntry_Object((1,3,6,1,4,1,171,12,3,3,3,1))
swRadiusAuthServerEntry.setIndexNames((0,_D,_l))
if mibBuilder.loadTexts:swRadiusAuthServerEntry.setStatus(_F)
_SwRadiusAuthServerIndex_Type=Integer32
_SwRadiusAuthServerIndex_Object=MibTableColumn
swRadiusAuthServerIndex=_SwRadiusAuthServerIndex_Object((1,3,6,1,4,1,171,12,3,3,3,1,1),_SwRadiusAuthServerIndex_Type())
swRadiusAuthServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthServerIndex.setStatus(_F)
_SwRadiusAuthServerAddress_Type=IpAddress
_SwRadiusAuthServerAddress_Object=MibTableColumn
swRadiusAuthServerAddress=_SwRadiusAuthServerAddress_Object((1,3,6,1,4,1,171,12,3,3,3,1,2),_SwRadiusAuthServerAddress_Type())
swRadiusAuthServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthServerAddress.setStatus(_F)
class _SwRadiusAuthClientServerPortNumber_Type(Unsigned32):defaultValue=1812
_SwRadiusAuthClientServerPortNumber_Type.__name__=_H
_SwRadiusAuthClientServerPortNumber_Object=MibTableColumn
swRadiusAuthClientServerPortNumber=_SwRadiusAuthClientServerPortNumber_Object((1,3,6,1,4,1,171,12,3,3,3,1,3),_SwRadiusAuthClientServerPortNumber_Type())
swRadiusAuthClientServerPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientServerPortNumber.setStatus(_F)
_SwRadiusAuthClientRoundTripTime_Type=Counter32
_SwRadiusAuthClientRoundTripTime_Object=MibTableColumn
swRadiusAuthClientRoundTripTime=_SwRadiusAuthClientRoundTripTime_Object((1,3,6,1,4,1,171,12,3,3,3,1,4),_SwRadiusAuthClientRoundTripTime_Type())
swRadiusAuthClientRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientRoundTripTime.setStatus(_F)
_SwRadiusAuthClientAccessRequests_Type=Counter32
_SwRadiusAuthClientAccessRequests_Object=MibTableColumn
swRadiusAuthClientAccessRequests=_SwRadiusAuthClientAccessRequests_Object((1,3,6,1,4,1,171,12,3,3,3,1,5),_SwRadiusAuthClientAccessRequests_Type())
swRadiusAuthClientAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientAccessRequests.setStatus(_F)
_SwRadiusAuthClientAccessRetransmissions_Type=Counter32
_SwRadiusAuthClientAccessRetransmissions_Object=MibTableColumn
swRadiusAuthClientAccessRetransmissions=_SwRadiusAuthClientAccessRetransmissions_Object((1,3,6,1,4,1,171,12,3,3,3,1,6),_SwRadiusAuthClientAccessRetransmissions_Type())
swRadiusAuthClientAccessRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientAccessRetransmissions.setStatus(_F)
_SwRadiusAuthClientAccessAccepts_Type=Counter32
_SwRadiusAuthClientAccessAccepts_Object=MibTableColumn
swRadiusAuthClientAccessAccepts=_SwRadiusAuthClientAccessAccepts_Object((1,3,6,1,4,1,171,12,3,3,3,1,7),_SwRadiusAuthClientAccessAccepts_Type())
swRadiusAuthClientAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientAccessAccepts.setStatus(_F)
_SwRadiusAuthClientAccessRejects_Type=Counter32
_SwRadiusAuthClientAccessRejects_Object=MibTableColumn
swRadiusAuthClientAccessRejects=_SwRadiusAuthClientAccessRejects_Object((1,3,6,1,4,1,171,12,3,3,3,1,8),_SwRadiusAuthClientAccessRejects_Type())
swRadiusAuthClientAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientAccessRejects.setStatus(_F)
_SwRadiusAuthClientAccessChallenges_Type=Counter32
_SwRadiusAuthClientAccessChallenges_Object=MibTableColumn
swRadiusAuthClientAccessChallenges=_SwRadiusAuthClientAccessChallenges_Object((1,3,6,1,4,1,171,12,3,3,3,1,9),_SwRadiusAuthClientAccessChallenges_Type())
swRadiusAuthClientAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientAccessChallenges.setStatus(_F)
_SwRadiusAuthClientMalformedAccessResponses_Type=Counter32
_SwRadiusAuthClientMalformedAccessResponses_Object=MibTableColumn
swRadiusAuthClientMalformedAccessResponses=_SwRadiusAuthClientMalformedAccessResponses_Object((1,3,6,1,4,1,171,12,3,3,3,1,10),_SwRadiusAuthClientMalformedAccessResponses_Type())
swRadiusAuthClientMalformedAccessResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientMalformedAccessResponses.setStatus(_F)
_SwRadiusAuthClientBadAuthenticators_Type=Counter32
_SwRadiusAuthClientBadAuthenticators_Object=MibTableColumn
swRadiusAuthClientBadAuthenticators=_SwRadiusAuthClientBadAuthenticators_Object((1,3,6,1,4,1,171,12,3,3,3,1,11),_SwRadiusAuthClientBadAuthenticators_Type())
swRadiusAuthClientBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientBadAuthenticators.setStatus(_F)
_SwRadiusAuthClientPendingRequests_Type=Counter32
_SwRadiusAuthClientPendingRequests_Object=MibTableColumn
swRadiusAuthClientPendingRequests=_SwRadiusAuthClientPendingRequests_Object((1,3,6,1,4,1,171,12,3,3,3,1,12),_SwRadiusAuthClientPendingRequests_Type())
swRadiusAuthClientPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientPendingRequests.setStatus(_F)
_SwRadiusAuthClientTimeouts_Type=Counter32
_SwRadiusAuthClientTimeouts_Object=MibTableColumn
swRadiusAuthClientTimeouts=_SwRadiusAuthClientTimeouts_Object((1,3,6,1,4,1,171,12,3,3,3,1,13),_SwRadiusAuthClientTimeouts_Type())
swRadiusAuthClientTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientTimeouts.setStatus(_F)
_SwRadiusAuthClientUnknownTypes_Type=Counter32
_SwRadiusAuthClientUnknownTypes_Object=MibTableColumn
swRadiusAuthClientUnknownTypes=_SwRadiusAuthClientUnknownTypes_Object((1,3,6,1,4,1,171,12,3,3,3,1,14),_SwRadiusAuthClientUnknownTypes_Type())
swRadiusAuthClientUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientUnknownTypes.setStatus(_F)
_SwRadiusAuthClientPacketsDropped_Type=Counter32
_SwRadiusAuthClientPacketsDropped_Object=MibTableColumn
swRadiusAuthClientPacketsDropped=_SwRadiusAuthClientPacketsDropped_Object((1,3,6,1,4,1,171,12,3,3,3,1,15),_SwRadiusAuthClientPacketsDropped_Type())
swRadiusAuthClientPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAuthClientPacketsDropped.setStatus(_F)
_SwRadiusAccountingCtrl_ObjectIdentity=ObjectIdentity
swRadiusAccountingCtrl=_SwRadiusAccountingCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,3,4))
_SwRadiusAcctUpdateInterval_Type=Unsigned32
_SwRadiusAcctUpdateInterval_Object=MibScalar
swRadiusAcctUpdateInterval=_SwRadiusAcctUpdateInterval_Object((1,3,6,1,4,1,171,12,3,4,1),_SwRadiusAcctUpdateInterval_Type())
swRadiusAcctUpdateInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusAcctUpdateInterval.setStatus(_A)
_SwRadiusAcctSuppressNullUserName_Type=TruthValue
_SwRadiusAcctSuppressNullUserName_Object=MibScalar
swRadiusAcctSuppressNullUserName=_SwRadiusAcctSuppressNullUserName_Object((1,3,6,1,4,1,171,12,3,4,2),_SwRadiusAcctSuppressNullUserName_Type())
swRadiusAcctSuppressNullUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusAcctSuppressNullUserName.setStatus(_A)
_SwRadiusAcctServiceTable_Object=MibTable
swRadiusAcctServiceTable=_SwRadiusAcctServiceTable_Object((1,3,6,1,4,1,171,12,3,4,3))
if mibBuilder.loadTexts:swRadiusAcctServiceTable.setStatus(_A)
_SwRadiusAcctServiceEntry_Object=MibTableRow
swRadiusAcctServiceEntry=_SwRadiusAcctServiceEntry_Object((1,3,6,1,4,1,171,12,3,4,3,1))
swRadiusAcctServiceEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:swRadiusAcctServiceEntry.setStatus(_A)
class _SwRadiusAcctServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acctServiceIndex-network',1),('acctServiceIndex-exec',2),('acctServiceIndex-system',3)))
_SwRadiusAcctServiceIndex_Type.__name__=_C
_SwRadiusAcctServiceIndex_Object=MibTableColumn
swRadiusAcctServiceIndex=_SwRadiusAcctServiceIndex_Object((1,3,6,1,4,1,171,12,3,4,3,1,1),_SwRadiusAcctServiceIndex_Type())
swRadiusAcctServiceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swRadiusAcctServiceIndex.setStatus(_A)
class _SwRadiusAcctServiceMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('swRadiusAcctServiceMethodNone',1),('swRadiusAcctServiceMethodRadius',2)))
_SwRadiusAcctServiceMethod_Type.__name__=_C
_SwRadiusAcctServiceMethod_Object=MibTableColumn
swRadiusAcctServiceMethod=_SwRadiusAcctServiceMethod_Object((1,3,6,1,4,1,171,12,3,4,3,1,2),_SwRadiusAcctServiceMethod_Type())
swRadiusAcctServiceMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusAcctServiceMethod.setStatus(_A)
class _SwRadiusAcctServiceMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('radiusAcctServiceModeNone',1),('radiusAcctServiceModeStartStop',2),('radiusAcctServiceModeStopOnly',3)))
_SwRadiusAcctServiceMode_Type.__name__=_C
_SwRadiusAcctServiceMode_Object=MibTableColumn
swRadiusAcctServiceMode=_SwRadiusAcctServiceMode_Object((1,3,6,1,4,1,171,12,3,4,3,1,3),_SwRadiusAcctServiceMode_Type())
swRadiusAcctServiceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusAcctServiceMode.setStatus(_A)
_SwRadiusAccountingInfo_ObjectIdentity=ObjectIdentity
swRadiusAccountingInfo=_SwRadiusAccountingInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,5))
_SwMacAuthBaseStatsInfo_ObjectIdentity=ObjectIdentity
swMacAuthBaseStatsInfo=_SwMacAuthBaseStatsInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,6))
_SwMacAuthStateTable_Object=MibTable
swMacAuthStateTable=_SwMacAuthStateTable_Object((1,3,6,1,4,1,171,12,3,6,1))
if mibBuilder.loadTexts:swMacAuthStateTable.setStatus(_F)
_SwMacAuthStateEntry_Object=MibTableRow
swMacAuthStateEntry=_SwMacAuthStateEntry_Object((1,3,6,1,4,1,171,12,3,6,1,1))
swMacAuthStateEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swMacAuthStateEntry.setStatus(_F)
_SwPaeMacAddr_Type=MacAddress
_SwPaeMacAddr_Object=MibTableColumn
swPaeMacAddr=_SwPaeMacAddr_Object((1,3,6,1,4,1,171,12,3,6,1,1,1),_SwPaeMacAddr_Type())
swPaeMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:swPaeMacAddr.setStatus(_F)
_SwPaePortNumber_Type=InterfaceIndex
_SwPaePortNumber_Object=MibTableColumn
swPaePortNumber=_SwPaePortNumber_Object((1,3,6,1,4,1,171,12,3,6,1,1,2),_SwPaePortNumber_Type())
swPaePortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swPaePortNumber.setStatus(_F)
class _SwAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,1),(_S,2),(_T,3),(_N,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9)))
_SwAuthPaeState_Type.__name__=_C
_SwAuthPaeState_Object=MibTableColumn
swAuthPaeState=_SwAuthPaeState_Object((1,3,6,1,4,1,171,12,3,6,1,1,3),_SwAuthPaeState_Type())
swAuthPaeState.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthPaeState.setStatus(_F)
class _SwAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_I,7)))
_SwAuthBackendAuthState_Type.__name__=_C
_SwAuthBackendAuthState_Object=MibTableColumn
swAuthBackendAuthState=_SwAuthBackendAuthState_Object((1,3,6,1,4,1,171,12,3,6,1,1,4),_SwAuthBackendAuthState_Type())
swAuthBackendAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendAuthState.setStatus(_F)
_SwAuthAuthControlledPortStatus_Type=PaeControlledPortStatus
_SwAuthAuthControlledPortStatus_Object=MibTableColumn
swAuthAuthControlledPortStatus=_SwAuthAuthControlledPortStatus_Object((1,3,6,1,4,1,171,12,3,6,1,1,5),_SwAuthAuthControlledPortStatus_Type())
swAuthAuthControlledPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthControlledPortStatus.setStatus(_F)
_SwMacAuthStatsTable_Object=MibTable
swMacAuthStatsTable=_SwMacAuthStatsTable_Object((1,3,6,1,4,1,171,12,3,6,2))
if mibBuilder.loadTexts:swMacAuthStatsTable.setStatus(_A)
_SwMacAuthStatsEntry_Object=MibTableRow
swMacAuthStatsEntry=_SwMacAuthStatsEntry_Object((1,3,6,1,4,1,171,12,3,6,2,1))
swMacAuthStatsEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swMacAuthStatsEntry.setStatus(_A)
_SwAuthEapolFramesRx_Type=Counter32
_SwAuthEapolFramesRx_Object=MibTableColumn
swAuthEapolFramesRx=_SwAuthEapolFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,1),_SwAuthEapolFramesRx_Type())
swAuthEapolFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolFramesRx.setStatus(_A)
_SwAuthEapolFramesTx_Type=Counter32
_SwAuthEapolFramesTx_Object=MibTableColumn
swAuthEapolFramesTx=_SwAuthEapolFramesTx_Object((1,3,6,1,4,1,171,12,3,6,2,1,2),_SwAuthEapolFramesTx_Type())
swAuthEapolFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolFramesTx.setStatus(_A)
_SwAuthEapolStartFramesRx_Type=Counter32
_SwAuthEapolStartFramesRx_Object=MibTableColumn
swAuthEapolStartFramesRx=_SwAuthEapolStartFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,3),_SwAuthEapolStartFramesRx_Type())
swAuthEapolStartFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolStartFramesRx.setStatus(_A)
_SwAuthEapolLogoffFramesRx_Type=Counter32
_SwAuthEapolLogoffFramesRx_Object=MibTableColumn
swAuthEapolLogoffFramesRx=_SwAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,4),_SwAuthEapolLogoffFramesRx_Type())
swAuthEapolLogoffFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolLogoffFramesRx.setStatus(_A)
_SwAuthEapolRespIdFramesRx_Type=Counter32
_SwAuthEapolRespIdFramesRx_Object=MibTableColumn
swAuthEapolRespIdFramesRx=_SwAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,5),_SwAuthEapolRespIdFramesRx_Type())
swAuthEapolRespIdFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolRespIdFramesRx.setStatus(_A)
_SwAuthEapolRespFramesRx_Type=Counter32
_SwAuthEapolRespFramesRx_Object=MibTableColumn
swAuthEapolRespFramesRx=_SwAuthEapolRespFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,6),_SwAuthEapolRespFramesRx_Type())
swAuthEapolRespFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolRespFramesRx.setStatus(_A)
_SwAuthEapolReqIdFramesTx_Type=Counter32
_SwAuthEapolReqIdFramesTx_Object=MibTableColumn
swAuthEapolReqIdFramesTx=_SwAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,171,12,3,6,2,1,7),_SwAuthEapolReqIdFramesTx_Type())
swAuthEapolReqIdFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolReqIdFramesTx.setStatus(_A)
_SwAuthEapolReqFramesTx_Type=Counter32
_SwAuthEapolReqFramesTx_Object=MibTableColumn
swAuthEapolReqFramesTx=_SwAuthEapolReqFramesTx_Object((1,3,6,1,4,1,171,12,3,6,2,1,8),_SwAuthEapolReqFramesTx_Type())
swAuthEapolReqFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapolReqFramesTx.setStatus(_A)
_SwAuthInvalidEapolFramesRx_Type=Counter32
_SwAuthInvalidEapolFramesRx_Object=MibTableColumn
swAuthInvalidEapolFramesRx=_SwAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,9),_SwAuthInvalidEapolFramesRx_Type())
swAuthInvalidEapolFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthInvalidEapolFramesRx.setStatus(_A)
_SwAuthEapLengthErrorFramesRx_Type=Counter32
_SwAuthEapLengthErrorFramesRx_Object=MibTableColumn
swAuthEapLengthErrorFramesRx=_SwAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,10),_SwAuthEapLengthErrorFramesRx_Type())
swAuthEapLengthErrorFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapLengthErrorFramesRx.setStatus(_A)
_SwAuthLastEapolFrameVersion_Type=Unsigned32
_SwAuthLastEapolFrameVersion_Object=MibTableColumn
swAuthLastEapolFrameVersion=_SwAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,171,12,3,6,2,1,11),_SwAuthLastEapolFrameVersion_Type())
swAuthLastEapolFrameVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthLastEapolFrameVersion.setStatus(_A)
_SwAuthLastEapolFrameSource_Type=MacAddress
_SwAuthLastEapolFrameSource_Object=MibTableColumn
swAuthLastEapolFrameSource=_SwAuthLastEapolFrameSource_Object((1,3,6,1,4,1,171,12,3,6,2,1,12),_SwAuthLastEapolFrameSource_Type())
swAuthLastEapolFrameSource.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthLastEapolFrameSource.setStatus(_A)
_SwMacAuthDiagTable_Object=MibTable
swMacAuthDiagTable=_SwMacAuthDiagTable_Object((1,3,6,1,4,1,171,12,3,6,3))
if mibBuilder.loadTexts:swMacAuthDiagTable.setStatus(_A)
_SwMacAuthDiagEntry_Object=MibTableRow
swMacAuthDiagEntry=_SwMacAuthDiagEntry_Object((1,3,6,1,4,1,171,12,3,6,3,1))
swMacAuthDiagEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swMacAuthDiagEntry.setStatus(_A)
_SwAuthEntersConnecting_Type=Counter32
_SwAuthEntersConnecting_Object=MibTableColumn
swAuthEntersConnecting=_SwAuthEntersConnecting_Object((1,3,6,1,4,1,171,12,3,6,3,1,1),_SwAuthEntersConnecting_Type())
swAuthEntersConnecting.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEntersConnecting.setStatus(_A)
_SwAuthEapLogoffsWhileConnecting_Type=Counter32
_SwAuthEapLogoffsWhileConnecting_Object=MibTableColumn
swAuthEapLogoffsWhileConnecting=_SwAuthEapLogoffsWhileConnecting_Object((1,3,6,1,4,1,171,12,3,6,3,1,2),_SwAuthEapLogoffsWhileConnecting_Type())
swAuthEapLogoffsWhileConnecting.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEapLogoffsWhileConnecting.setStatus(_A)
_SwAuthEntersAuthenticating_Type=Counter32
_SwAuthEntersAuthenticating_Object=MibTableColumn
swAuthEntersAuthenticating=_SwAuthEntersAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,3),_SwAuthEntersAuthenticating_Type())
swAuthEntersAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthEntersAuthenticating.setStatus(_A)
_SwAuthAuthSuccessWhileAuthenticating_Type=Counter32
_SwAuthAuthSuccessWhileAuthenticating_Object=MibTableColumn
swAuthAuthSuccessWhileAuthenticating=_SwAuthAuthSuccessWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,4),_SwAuthAuthSuccessWhileAuthenticating_Type())
swAuthAuthSuccessWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthSuccessWhileAuthenticating.setStatus(_A)
_SwAuthAuthTimeoutsWhileAuthenticating_Type=Counter32
_SwAuthAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
swAuthAuthTimeoutsWhileAuthenticating=_SwAuthAuthTimeoutsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,5),_SwAuthAuthTimeoutsWhileAuthenticating_Type())
swAuthAuthTimeoutsWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthTimeoutsWhileAuthenticating.setStatus(_A)
_SwAuthAuthFailWhileAuthenticating_Type=Counter32
_SwAuthAuthFailWhileAuthenticating_Object=MibTableColumn
swAuthAuthFailWhileAuthenticating=_SwAuthAuthFailWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,6),_SwAuthAuthFailWhileAuthenticating_Type())
swAuthAuthFailWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthFailWhileAuthenticating.setStatus(_A)
_SwAuthAuthReauthsWhileAuthenticating_Type=Counter32
_SwAuthAuthReauthsWhileAuthenticating_Object=MibTableColumn
swAuthAuthReauthsWhileAuthenticating=_SwAuthAuthReauthsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,7),_SwAuthAuthReauthsWhileAuthenticating_Type())
swAuthAuthReauthsWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthReauthsWhileAuthenticating.setStatus(_A)
_SwAuthAuthEapStartsWhileAuthenticating_Type=Counter32
_SwAuthAuthEapStartsWhileAuthenticating_Object=MibTableColumn
swAuthAuthEapStartsWhileAuthenticating=_SwAuthAuthEapStartsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,8),_SwAuthAuthEapStartsWhileAuthenticating_Type())
swAuthAuthEapStartsWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthEapStartsWhileAuthenticating.setStatus(_A)
_SwAuthAuthEapLogoffWhileAuthenticating_Type=Counter32
_SwAuthAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
swAuthAuthEapLogoffWhileAuthenticating=_SwAuthAuthEapLogoffWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,9),_SwAuthAuthEapLogoffWhileAuthenticating_Type())
swAuthAuthEapLogoffWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthEapLogoffWhileAuthenticating.setStatus(_A)
_SwAuthAuthReauthsWhileAuthenticated_Type=Counter32
_SwAuthAuthReauthsWhileAuthenticated_Object=MibTableColumn
swAuthAuthReauthsWhileAuthenticated=_SwAuthAuthReauthsWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,3,1,10),_SwAuthAuthReauthsWhileAuthenticated_Type())
swAuthAuthReauthsWhileAuthenticated.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthReauthsWhileAuthenticated.setStatus(_A)
_SwAuthAuthEapStartsWhileAuthenticated_Type=Counter32
_SwAuthAuthEapStartsWhileAuthenticated_Object=MibTableColumn
swAuthAuthEapStartsWhileAuthenticated=_SwAuthAuthEapStartsWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,3,1,11),_SwAuthAuthEapStartsWhileAuthenticated_Type())
swAuthAuthEapStartsWhileAuthenticated.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthEapStartsWhileAuthenticated.setStatus(_A)
_SwAuthAuthEapLogoffWhileAuthenticated_Type=Counter32
_SwAuthAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
swAuthAuthEapLogoffWhileAuthenticated=_SwAuthAuthEapLogoffWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,3,1,12),_SwAuthAuthEapLogoffWhileAuthenticated_Type())
swAuthAuthEapLogoffWhileAuthenticated.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthEapLogoffWhileAuthenticated.setStatus(_A)
_SwAuthBackendResponses_Type=Counter32
_SwAuthBackendResponses_Object=MibTableColumn
swAuthBackendResponses=_SwAuthBackendResponses_Object((1,3,6,1,4,1,171,12,3,6,3,1,13),_SwAuthBackendResponses_Type())
swAuthBackendResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendResponses.setStatus(_A)
_SwAuthBackendAccessChallenges_Type=Counter32
_SwAuthBackendAccessChallenges_Object=MibTableColumn
swAuthBackendAccessChallenges=_SwAuthBackendAccessChallenges_Object((1,3,6,1,4,1,171,12,3,6,3,1,14),_SwAuthBackendAccessChallenges_Type())
swAuthBackendAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendAccessChallenges.setStatus(_A)
_SwAuthBackendOtherRequestsToSupplicant_Type=Counter32
_SwAuthBackendOtherRequestsToSupplicant_Object=MibTableColumn
swAuthBackendOtherRequestsToSupplicant=_SwAuthBackendOtherRequestsToSupplicant_Object((1,3,6,1,4,1,171,12,3,6,3,1,15),_SwAuthBackendOtherRequestsToSupplicant_Type())
swAuthBackendOtherRequestsToSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendOtherRequestsToSupplicant.setStatus(_A)
_SwAuthBackendNonNakResponsesFromSupplicant_Type=Counter32
_SwAuthBackendNonNakResponsesFromSupplicant_Object=MibTableColumn
swAuthBackendNonNakResponsesFromSupplicant=_SwAuthBackendNonNakResponsesFromSupplicant_Object((1,3,6,1,4,1,171,12,3,6,3,1,16),_SwAuthBackendNonNakResponsesFromSupplicant_Type())
swAuthBackendNonNakResponsesFromSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendNonNakResponsesFromSupplicant.setStatus(_A)
_SwAuthBackendAuthSuccesses_Type=Counter32
_SwAuthBackendAuthSuccesses_Object=MibTableColumn
swAuthBackendAuthSuccesses=_SwAuthBackendAuthSuccesses_Object((1,3,6,1,4,1,171,12,3,6,3,1,17),_SwAuthBackendAuthSuccesses_Type())
swAuthBackendAuthSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendAuthSuccesses.setStatus(_A)
_SwAuthBackendAuthFails_Type=Counter32
_SwAuthBackendAuthFails_Object=MibTableColumn
swAuthBackendAuthFails=_SwAuthBackendAuthFails_Object((1,3,6,1,4,1,171,12,3,6,3,1,18),_SwAuthBackendAuthFails_Type())
swAuthBackendAuthFails.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBackendAuthFails.setStatus(_A)
_SwMacAuthSessionStatsTable_Object=MibTable
swMacAuthSessionStatsTable=_SwMacAuthSessionStatsTable_Object((1,3,6,1,4,1,171,12,3,6,4))
if mibBuilder.loadTexts:swMacAuthSessionStatsTable.setStatus(_A)
_SwMacAuthSessionStatsEntry_Object=MibTableRow
swMacAuthSessionStatsEntry=_SwMacAuthSessionStatsEntry_Object((1,3,6,1,4,1,171,12,3,6,4,1))
swMacAuthSessionStatsEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:swMacAuthSessionStatsEntry.setStatus(_A)
_SwAuthSessionOctetsRx_Type=Counter64
_SwAuthSessionOctetsRx_Object=MibTableColumn
swAuthSessionOctetsRx=_SwAuthSessionOctetsRx_Object((1,3,6,1,4,1,171,12,3,6,4,1,1),_SwAuthSessionOctetsRx_Type())
swAuthSessionOctetsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionOctetsRx.setStatus(_A)
_SwAuthSessionOctetsTx_Type=Counter64
_SwAuthSessionOctetsTx_Object=MibTableColumn
swAuthSessionOctetsTx=_SwAuthSessionOctetsTx_Object((1,3,6,1,4,1,171,12,3,6,4,1,2),_SwAuthSessionOctetsTx_Type())
swAuthSessionOctetsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionOctetsTx.setStatus(_A)
_SwAuthSessionFramesRx_Type=Counter32
_SwAuthSessionFramesRx_Object=MibTableColumn
swAuthSessionFramesRx=_SwAuthSessionFramesRx_Object((1,3,6,1,4,1,171,12,3,6,4,1,3),_SwAuthSessionFramesRx_Type())
swAuthSessionFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionFramesRx.setStatus(_A)
_SwAuthSessionFramesTx_Type=Counter32
_SwAuthSessionFramesTx_Object=MibTableColumn
swAuthSessionFramesTx=_SwAuthSessionFramesTx_Object((1,3,6,1,4,1,171,12,3,6,4,1,4),_SwAuthSessionFramesTx_Type())
swAuthSessionFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionFramesTx.setStatus(_A)
_SwAuthSessionId_Type=SnmpAdminString
_SwAuthSessionId_Object=MibTableColumn
swAuthSessionId=_SwAuthSessionId_Object((1,3,6,1,4,1,171,12,3,6,4,1,5),_SwAuthSessionId_Type())
swAuthSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionId.setStatus(_A)
class _SwAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_SwAuthSessionAuthenticMethod_Type.__name__=_C
_SwAuthSessionAuthenticMethod_Object=MibTableColumn
swAuthSessionAuthenticMethod=_SwAuthSessionAuthenticMethod_Object((1,3,6,1,4,1,171,12,3,6,4,1,6),_SwAuthSessionAuthenticMethod_Type())
swAuthSessionAuthenticMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionAuthenticMethod.setStatus(_A)
_SwAuthSessionTime_Type=TimeTicks
_SwAuthSessionTime_Object=MibTableColumn
swAuthSessionTime=_SwAuthSessionTime_Object((1,3,6,1,4,1,171,12,3,6,4,1,7),_SwAuthSessionTime_Type())
swAuthSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionTime.setStatus(_A)
class _SwAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7),(_w,999)))
_SwAuthSessionTerminateCause_Type.__name__=_C
_SwAuthSessionTerminateCause_Object=MibTableColumn
swAuthSessionTerminateCause=_SwAuthSessionTerminateCause_Object((1,3,6,1,4,1,171,12,3,6,4,1,8),_SwAuthSessionTerminateCause_Type())
swAuthSessionTerminateCause.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionTerminateCause.setStatus(_A)
_SwAuthSessionUserName_Type=SnmpAdminString
_SwAuthSessionUserName_Object=MibTableColumn
swAuthSessionUserName=_SwAuthSessionUserName_Object((1,3,6,1,4,1,171,12,3,6,4,1,9),_SwAuthSessionUserName_Type())
swAuthSessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthSessionUserName.setStatus(_A)
_SwDot1xAuthStateTable_Object=MibTable
swDot1xAuthStateTable=_SwDot1xAuthStateTable_Object((1,3,6,1,4,1,171,12,3,6,5))
if mibBuilder.loadTexts:swDot1xAuthStateTable.setStatus(_A)
_SwDot1xAuthStateEntry_Object=MibTableRow
swDot1xAuthStateEntry=_SwDot1xAuthStateEntry_Object((1,3,6,1,4,1,171,12,3,6,5,1))
swDot1xAuthStateEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:swDot1xAuthStateEntry.setStatus(_A)
_SwDot1xAuthPortNumber_Type=InterfaceIndex
_SwDot1xAuthPortNumber_Object=MibTableColumn
swDot1xAuthPortNumber=_SwDot1xAuthPortNumber_Object((1,3,6,1,4,1,171,12,3,6,5,1,1),_SwDot1xAuthPortNumber_Type())
swDot1xAuthPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swDot1xAuthPortNumber.setStatus(_A)
_SwDot1xAuthVID_Type=Integer32
_SwDot1xAuthVID_Object=MibTableColumn
swDot1xAuthVID=_SwDot1xAuthVID_Object((1,3,6,1,4,1,171,12,3,6,5,1,2),_SwDot1xAuthVID_Type())
swDot1xAuthVID.setMaxAccess(_G)
if mibBuilder.loadTexts:swDot1xAuthVID.setStatus(_A)
_SwDot1xAuthMACAddress_Type=MacAddress
_SwDot1xAuthMACAddress_Object=MibTableColumn
swDot1xAuthMACAddress=_SwDot1xAuthMACAddress_Object((1,3,6,1,4,1,171,12,3,6,5,1,3),_SwDot1xAuthMACAddress_Type())
swDot1xAuthMACAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:swDot1xAuthMACAddress.setStatus(_A)
class _SwDot1xAuthenticatorPAEState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,1),(_S,2),(_T,3),(_N,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9)))
_SwDot1xAuthenticatorPAEState_Type.__name__=_C
_SwDot1xAuthenticatorPAEState_Object=MibTableColumn
swDot1xAuthenticatorPAEState=_SwDot1xAuthenticatorPAEState_Object((1,3,6,1,4,1,171,12,3,6,5,1,4),_SwDot1xAuthenticatorPAEState_Type())
swDot1xAuthenticatorPAEState.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthenticatorPAEState.setStatus(_A)
class _SwDot1xAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_I,7)))
_SwDot1xAuthBackendAuthState_Type.__name__=_C
_SwDot1xAuthBackendAuthState_Object=MibTableColumn
swDot1xAuthBackendAuthState=_SwDot1xAuthBackendAuthState_Object((1,3,6,1,4,1,171,12,3,6,5,1,5),_SwDot1xAuthBackendAuthState_Type())
swDot1xAuthBackendAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendAuthState.setStatus(_A)
class _SwDot1xAuthAuthControlledStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_x,2),(_y,3)))
_SwDot1xAuthAuthControlledStatus_Type.__name__=_C
_SwDot1xAuthAuthControlledStatus_Object=MibTableColumn
swDot1xAuthAuthControlledStatus=_SwDot1xAuthAuthControlledStatus_Object((1,3,6,1,4,1,171,12,3,6,5,1,6),_SwDot1xAuthAuthControlledStatus_Type())
swDot1xAuthAuthControlledStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthControlledStatus.setStatus(_A)
_SwDot1xAuthAssignVID_Type=Integer32
_SwDot1xAuthAssignVID_Object=MibTableColumn
swDot1xAuthAssignVID=_SwDot1xAuthAssignVID_Object((1,3,6,1,4,1,171,12,3,6,5,1,7),_SwDot1xAuthAssignVID_Type())
swDot1xAuthAssignVID.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAssignVID.setStatus(_A)
_SwDot1xAuthAssignPriority_Type=Integer32
_SwDot1xAuthAssignPriority_Object=MibTableColumn
swDot1xAuthAssignPriority=_SwDot1xAuthAssignPriority_Object((1,3,6,1,4,1,171,12,3,6,5,1,8),_SwDot1xAuthAssignPriority_Type())
swDot1xAuthAssignPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAssignPriority.setStatus(_A)
_SwDot1xAuthStatsTable_Object=MibTable
swDot1xAuthStatsTable=_SwDot1xAuthStatsTable_Object((1,3,6,1,4,1,171,12,3,6,6))
if mibBuilder.loadTexts:swDot1xAuthStatsTable.setStatus(_A)
_SwDot1xAuthStatsEntry_Object=MibTableRow
swDot1xAuthStatsEntry=_SwDot1xAuthStatsEntry_Object((1,3,6,1,4,1,171,12,3,6,6,1))
swDot1xAuthStatsEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:swDot1xAuthStatsEntry.setStatus(_A)
_SwDot1xAuthEapolFramesRx_Type=Counter32
_SwDot1xAuthEapolFramesRx_Object=MibTableColumn
swDot1xAuthEapolFramesRx=_SwDot1xAuthEapolFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,1),_SwDot1xAuthEapolFramesRx_Type())
swDot1xAuthEapolFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolFramesRx.setStatus(_A)
_SwDot1xAuthEapolFramesTx_Type=Counter32
_SwDot1xAuthEapolFramesTx_Object=MibTableColumn
swDot1xAuthEapolFramesTx=_SwDot1xAuthEapolFramesTx_Object((1,3,6,1,4,1,171,12,3,6,6,1,2),_SwDot1xAuthEapolFramesTx_Type())
swDot1xAuthEapolFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolFramesTx.setStatus(_A)
_SwDot1xAuthEapolStartFramesRx_Type=Counter32
_SwDot1xAuthEapolStartFramesRx_Object=MibTableColumn
swDot1xAuthEapolStartFramesRx=_SwDot1xAuthEapolStartFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,3),_SwDot1xAuthEapolStartFramesRx_Type())
swDot1xAuthEapolStartFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolStartFramesRx.setStatus(_A)
_SwDot1xAuthEapolLogoffFramesRx_Type=Counter32
_SwDot1xAuthEapolLogoffFramesRx_Object=MibTableColumn
swDot1xAuthEapolLogoffFramesRx=_SwDot1xAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,4),_SwDot1xAuthEapolLogoffFramesRx_Type())
swDot1xAuthEapolLogoffFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolLogoffFramesRx.setStatus(_A)
_SwDot1xAuthEapolRespIdFramesRx_Type=Counter32
_SwDot1xAuthEapolRespIdFramesRx_Object=MibTableColumn
swDot1xAuthEapolRespIdFramesRx=_SwDot1xAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,5),_SwDot1xAuthEapolRespIdFramesRx_Type())
swDot1xAuthEapolRespIdFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolRespIdFramesRx.setStatus(_A)
_SwDot1xAuthEapolRespFramesRx_Type=Counter32
_SwDot1xAuthEapolRespFramesRx_Object=MibTableColumn
swDot1xAuthEapolRespFramesRx=_SwDot1xAuthEapolRespFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,6),_SwDot1xAuthEapolRespFramesRx_Type())
swDot1xAuthEapolRespFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolRespFramesRx.setStatus(_A)
_SwDot1xAuthEapolReqIdFramesTx_Type=Counter32
_SwDot1xAuthEapolReqIdFramesTx_Object=MibTableColumn
swDot1xAuthEapolReqIdFramesTx=_SwDot1xAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,171,12,3,6,6,1,7),_SwDot1xAuthEapolReqIdFramesTx_Type())
swDot1xAuthEapolReqIdFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolReqIdFramesTx.setStatus(_A)
_SwDot1xAuthEapolReqFramesTx_Type=Counter32
_SwDot1xAuthEapolReqFramesTx_Object=MibTableColumn
swDot1xAuthEapolReqFramesTx=_SwDot1xAuthEapolReqFramesTx_Object((1,3,6,1,4,1,171,12,3,6,6,1,8),_SwDot1xAuthEapolReqFramesTx_Type())
swDot1xAuthEapolReqFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapolReqFramesTx.setStatus(_A)
_SwDot1xAuthInvalidEapolFramesRx_Type=Counter32
_SwDot1xAuthInvalidEapolFramesRx_Object=MibTableColumn
swDot1xAuthInvalidEapolFramesRx=_SwDot1xAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,9),_SwDot1xAuthInvalidEapolFramesRx_Type())
swDot1xAuthInvalidEapolFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthInvalidEapolFramesRx.setStatus(_A)
_SwDot1xAuthEapLengthErrorFramesRx_Type=Counter32
_SwDot1xAuthEapLengthErrorFramesRx_Object=MibTableColumn
swDot1xAuthEapLengthErrorFramesRx=_SwDot1xAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,171,12,3,6,6,1,10),_SwDot1xAuthEapLengthErrorFramesRx_Type())
swDot1xAuthEapLengthErrorFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapLengthErrorFramesRx.setStatus(_A)
_SwDot1xAuthLastEapolFrameVersion_Type=Unsigned32
_SwDot1xAuthLastEapolFrameVersion_Object=MibTableColumn
swDot1xAuthLastEapolFrameVersion=_SwDot1xAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,171,12,3,6,6,1,11),_SwDot1xAuthLastEapolFrameVersion_Type())
swDot1xAuthLastEapolFrameVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthLastEapolFrameVersion.setStatus(_A)
_SwDot1xAuthLastEapolFrameSource_Type=MacAddress
_SwDot1xAuthLastEapolFrameSource_Object=MibTableColumn
swDot1xAuthLastEapolFrameSource=_SwDot1xAuthLastEapolFrameSource_Object((1,3,6,1,4,1,171,12,3,6,6,1,12),_SwDot1xAuthLastEapolFrameSource_Type())
swDot1xAuthLastEapolFrameSource.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthLastEapolFrameSource.setStatus(_A)
_SwDot1xAuthDiagTable_Object=MibTable
swDot1xAuthDiagTable=_SwDot1xAuthDiagTable_Object((1,3,6,1,4,1,171,12,3,6,7))
if mibBuilder.loadTexts:swDot1xAuthDiagTable.setStatus(_A)
_SwDot1xAuthDiagEntry_Object=MibTableRow
swDot1xAuthDiagEntry=_SwDot1xAuthDiagEntry_Object((1,3,6,1,4,1,171,12,3,6,7,1))
swDot1xAuthDiagEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:swDot1xAuthDiagEntry.setStatus(_A)
_SwDot1xAuthEntersConnecting_Type=Counter32
_SwDot1xAuthEntersConnecting_Object=MibTableColumn
swDot1xAuthEntersConnecting=_SwDot1xAuthEntersConnecting_Object((1,3,6,1,4,1,171,12,3,6,7,1,1),_SwDot1xAuthEntersConnecting_Type())
swDot1xAuthEntersConnecting.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEntersConnecting.setStatus(_A)
_SwDot1xAuthEapLogoffsWhileConnecting_Type=Counter32
_SwDot1xAuthEapLogoffsWhileConnecting_Object=MibTableColumn
swDot1xAuthEapLogoffsWhileConnecting=_SwDot1xAuthEapLogoffsWhileConnecting_Object((1,3,6,1,4,1,171,12,3,6,7,1,2),_SwDot1xAuthEapLogoffsWhileConnecting_Type())
swDot1xAuthEapLogoffsWhileConnecting.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEapLogoffsWhileConnecting.setStatus(_A)
_SwDot1xAuthEntersAuthenticating_Type=Counter32
_SwDot1xAuthEntersAuthenticating_Object=MibTableColumn
swDot1xAuthEntersAuthenticating=_SwDot1xAuthEntersAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,3),_SwDot1xAuthEntersAuthenticating_Type())
swDot1xAuthEntersAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthEntersAuthenticating.setStatus(_A)
_SwDot1xAuthAuthSuccessWhileAuthenticating_Type=Counter32
_SwDot1xAuthAuthSuccessWhileAuthenticating_Object=MibTableColumn
swDot1xAuthAuthSuccessWhileAuthenticating=_SwDot1xAuthAuthSuccessWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,4),_SwDot1xAuthAuthSuccessWhileAuthenticating_Type())
swDot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthSuccessWhileAuthenticating.setStatus(_A)
_SwDot1xAuthAuthTimeoutsWhileAuthenticating_Type=Counter32
_SwDot1xAuthAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
swDot1xAuthAuthTimeoutsWhileAuthenticating=_SwDot1xAuthAuthTimeoutsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,5),_SwDot1xAuthAuthTimeoutsWhileAuthenticating_Type())
swDot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthTimeoutsWhileAuthenticating.setStatus(_A)
_SwDot1xAuthAuthFailWhileAuthenticating_Type=Counter32
_SwDot1xAuthAuthFailWhileAuthenticating_Object=MibTableColumn
swDot1xAuthAuthFailWhileAuthenticating=_SwDot1xAuthAuthFailWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,6),_SwDot1xAuthAuthFailWhileAuthenticating_Type())
swDot1xAuthAuthFailWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthFailWhileAuthenticating.setStatus(_A)
_SwDot1xAuthAuthReauthsWhileAuthenticating_Type=Counter32
_SwDot1xAuthAuthReauthsWhileAuthenticating_Object=MibTableColumn
swDot1xAuthAuthReauthsWhileAuthenticating=_SwDot1xAuthAuthReauthsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,7),_SwDot1xAuthAuthReauthsWhileAuthenticating_Type())
swDot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthReauthsWhileAuthenticating.setStatus(_A)
_SwDot1xAuthAuthEapStartsWhileAuthenticating_Type=Counter32
_SwDot1xAuthAuthEapStartsWhileAuthenticating_Object=MibTableColumn
swDot1xAuthAuthEapStartsWhileAuthenticating=_SwDot1xAuthAuthEapStartsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,8),_SwDot1xAuthAuthEapStartsWhileAuthenticating_Type())
swDot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthEapStartsWhileAuthenticating.setStatus(_A)
_SwDot1xAuthAuthEapLogoffWhileAuthenticating_Type=Counter32
_SwDot1xAuthAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
swDot1xAuthAuthEapLogoffWhileAuthenticating=_SwDot1xAuthAuthEapLogoffWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,7,1,9),_SwDot1xAuthAuthEapLogoffWhileAuthenticating_Type())
swDot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthEapLogoffWhileAuthenticating.setStatus(_A)
_SwDot1xAuthAuthReauthsWhileAuthenticated_Type=Counter32
_SwDot1xAuthAuthReauthsWhileAuthenticated_Object=MibTableColumn
swDot1xAuthAuthReauthsWhileAuthenticated=_SwDot1xAuthAuthReauthsWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,7,1,10),_SwDot1xAuthAuthReauthsWhileAuthenticated_Type())
swDot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthReauthsWhileAuthenticated.setStatus(_A)
_SwDot1xAuthAuthEapStartsWhileAuthenticated_Type=Counter32
_SwDot1xAuthAuthEapStartsWhileAuthenticated_Object=MibTableColumn
swDot1xAuthAuthEapStartsWhileAuthenticated=_SwDot1xAuthAuthEapStartsWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,7,1,11),_SwDot1xAuthAuthEapStartsWhileAuthenticated_Type())
swDot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthEapStartsWhileAuthenticated.setStatus(_A)
_SwDot1xAuthAuthEapLogoffWhileAuthenticated_Type=Counter32
_SwDot1xAuthAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
swDot1xAuthAuthEapLogoffWhileAuthenticated=_SwDot1xAuthAuthEapLogoffWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,7,1,12),_SwDot1xAuthAuthEapLogoffWhileAuthenticated_Type())
swDot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthAuthEapLogoffWhileAuthenticated.setStatus(_A)
_SwDot1xAuthBackendResponses_Type=Counter32
_SwDot1xAuthBackendResponses_Object=MibTableColumn
swDot1xAuthBackendResponses=_SwDot1xAuthBackendResponses_Object((1,3,6,1,4,1,171,12,3,6,7,1,13),_SwDot1xAuthBackendResponses_Type())
swDot1xAuthBackendResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendResponses.setStatus(_A)
_SwDot1xAuthBackendAccessChallenges_Type=Counter32
_SwDot1xAuthBackendAccessChallenges_Object=MibTableColumn
swDot1xAuthBackendAccessChallenges=_SwDot1xAuthBackendAccessChallenges_Object((1,3,6,1,4,1,171,12,3,6,7,1,14),_SwDot1xAuthBackendAccessChallenges_Type())
swDot1xAuthBackendAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendAccessChallenges.setStatus(_A)
_SwDot1xAuthBackendOtherRequestsToSupplicant_Type=Counter32
_SwDot1xAuthBackendOtherRequestsToSupplicant_Object=MibTableColumn
swDot1xAuthBackendOtherRequestsToSupplicant=_SwDot1xAuthBackendOtherRequestsToSupplicant_Object((1,3,6,1,4,1,171,12,3,6,7,1,15),_SwDot1xAuthBackendOtherRequestsToSupplicant_Type())
swDot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendOtherRequestsToSupplicant.setStatus(_A)
_SwDot1xAuthBackendNonNakResponsesFromSupplicant_Type=Counter32
_SwDot1xAuthBackendNonNakResponsesFromSupplicant_Object=MibTableColumn
swDot1xAuthBackendNonNakResponsesFromSupplicant=_SwDot1xAuthBackendNonNakResponsesFromSupplicant_Object((1,3,6,1,4,1,171,12,3,6,7,1,16),_SwDot1xAuthBackendNonNakResponsesFromSupplicant_Type())
swDot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendNonNakResponsesFromSupplicant.setStatus(_A)
_SwDot1xAuthBackendAuthSuccesses_Type=Counter32
_SwDot1xAuthBackendAuthSuccesses_Object=MibTableColumn
swDot1xAuthBackendAuthSuccesses=_SwDot1xAuthBackendAuthSuccesses_Object((1,3,6,1,4,1,171,12,3,6,7,1,17),_SwDot1xAuthBackendAuthSuccesses_Type())
swDot1xAuthBackendAuthSuccesses.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendAuthSuccesses.setStatus(_A)
_SwDot1xAuthBackendAuthFails_Type=Counter32
_SwDot1xAuthBackendAuthFails_Object=MibTableColumn
swDot1xAuthBackendAuthFails=_SwDot1xAuthBackendAuthFails_Object((1,3,6,1,4,1,171,12,3,6,7,1,18),_SwDot1xAuthBackendAuthFails_Type())
swDot1xAuthBackendAuthFails.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthBackendAuthFails.setStatus(_A)
_SwDot1xAuthSessionStatsTable_Object=MibTable
swDot1xAuthSessionStatsTable=_SwDot1xAuthSessionStatsTable_Object((1,3,6,1,4,1,171,12,3,6,8))
if mibBuilder.loadTexts:swDot1xAuthSessionStatsTable.setStatus(_A)
_SwDot1xAuthSessionStatsEntry_Object=MibTableRow
swDot1xAuthSessionStatsEntry=_SwDot1xAuthSessionStatsEntry_Object((1,3,6,1,4,1,171,12,3,6,8,1))
swDot1xAuthSessionStatsEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:swDot1xAuthSessionStatsEntry.setStatus(_A)
_SwDot1xAuthSessionOctetsRx_Type=Counter64
_SwDot1xAuthSessionOctetsRx_Object=MibTableColumn
swDot1xAuthSessionOctetsRx=_SwDot1xAuthSessionOctetsRx_Object((1,3,6,1,4,1,171,12,3,6,8,1,1),_SwDot1xAuthSessionOctetsRx_Type())
swDot1xAuthSessionOctetsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionOctetsRx.setStatus(_A)
_SwDot1xAuthSessionOctetsTx_Type=Counter64
_SwDot1xAuthSessionOctetsTx_Object=MibTableColumn
swDot1xAuthSessionOctetsTx=_SwDot1xAuthSessionOctetsTx_Object((1,3,6,1,4,1,171,12,3,6,8,1,2),_SwDot1xAuthSessionOctetsTx_Type())
swDot1xAuthSessionOctetsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionOctetsTx.setStatus(_A)
_SwDot1xAuthSessionFramesRx_Type=Counter32
_SwDot1xAuthSessionFramesRx_Object=MibTableColumn
swDot1xAuthSessionFramesRx=_SwDot1xAuthSessionFramesRx_Object((1,3,6,1,4,1,171,12,3,6,8,1,3),_SwDot1xAuthSessionFramesRx_Type())
swDot1xAuthSessionFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionFramesRx.setStatus(_A)
_SwDot1xAuthSessionFramesTx_Type=Counter32
_SwDot1xAuthSessionFramesTx_Object=MibTableColumn
swDot1xAuthSessionFramesTx=_SwDot1xAuthSessionFramesTx_Object((1,3,6,1,4,1,171,12,3,6,8,1,4),_SwDot1xAuthSessionFramesTx_Type())
swDot1xAuthSessionFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionFramesTx.setStatus(_A)
_SwDot1xAuthSessionId_Type=SnmpAdminString
_SwDot1xAuthSessionId_Object=MibTableColumn
swDot1xAuthSessionId=_SwDot1xAuthSessionId_Object((1,3,6,1,4,1,171,12,3,6,8,1,5),_SwDot1xAuthSessionId_Type())
swDot1xAuthSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionId.setStatus(_A)
class _SwDot1xAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),(_o,2)))
_SwDot1xAuthSessionAuthenticMethod_Type.__name__=_C
_SwDot1xAuthSessionAuthenticMethod_Object=MibTableColumn
swDot1xAuthSessionAuthenticMethod=_SwDot1xAuthSessionAuthenticMethod_Object((1,3,6,1,4,1,171,12,3,6,8,1,6),_SwDot1xAuthSessionAuthenticMethod_Type())
swDot1xAuthSessionAuthenticMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionAuthenticMethod.setStatus(_A)
_SwDot1xAuthSessionTime_Type=TimeTicks
_SwDot1xAuthSessionTime_Object=MibTableColumn
swDot1xAuthSessionTime=_SwDot1xAuthSessionTime_Object((1,3,6,1,4,1,171,12,3,6,8,1,7),_SwDot1xAuthSessionTime_Type())
swDot1xAuthSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionTime.setStatus(_A)
class _SwDot1xAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7),(_w,999)))
_SwDot1xAuthSessionTerminateCause_Type.__name__=_C
_SwDot1xAuthSessionTerminateCause_Object=MibTableColumn
swDot1xAuthSessionTerminateCause=_SwDot1xAuthSessionTerminateCause_Object((1,3,6,1,4,1,171,12,3,6,8,1,8),_SwDot1xAuthSessionTerminateCause_Type())
swDot1xAuthSessionTerminateCause.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionTerminateCause.setStatus(_A)
_SwDot1xAuthSessionUserName_Type=SnmpAdminString
_SwDot1xAuthSessionUserName_Object=MibTableColumn
swDot1xAuthSessionUserName=_SwDot1xAuthSessionUserName_Object((1,3,6,1,4,1,171,12,3,6,8,1,9),_SwDot1xAuthSessionUserName_Type())
swDot1xAuthSessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swDot1xAuthSessionUserName.setStatus(_A)
_SwRadiusCommand_ObjectIdentity=ObjectIdentity
swRadiusCommand=_SwRadiusCommand_ObjectIdentity((1,3,6,1,4,1,171,12,3,7))
_SwRadiusForceDownPortNumber_Type=Unsigned32
_SwRadiusForceDownPortNumber_Object=MibScalar
swRadiusForceDownPortNumber=_SwRadiusForceDownPortNumber_Object((1,3,6,1,4,1,171,12,3,7,1),_SwRadiusForceDownPortNumber_Type())
swRadiusForceDownPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusForceDownPortNumber.setStatus(_A)
_SwRadiusForceDownMacAddr_Type=MacAddress
_SwRadiusForceDownMacAddr_Object=MibScalar
swRadiusForceDownMacAddr=_SwRadiusForceDownMacAddr_Object((1,3,6,1,4,1,171,12,3,7,2),_SwRadiusForceDownMacAddr_Type())
swRadiusForceDownMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swRadiusForceDownMacAddr.setStatus(_A)
_SwAuthenticatedPortInfo_ObjectIdentity=ObjectIdentity
swAuthenticatedPortInfo=_SwAuthenticatedPortInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,8))
_SwAuthenticatedPortCtrlTable_Object=MibTable
swAuthenticatedPortCtrlTable=_SwAuthenticatedPortCtrlTable_Object((1,3,6,1,4,1,171,12,3,8,1))
if mibBuilder.loadTexts:swAuthenticatedPortCtrlTable.setStatus(_A)
_SwAuthenticatedPortCtrlEntry_Object=MibTableRow
swAuthenticatedPortCtrlEntry=_SwAuthenticatedPortCtrlEntry_Object((1,3,6,1,4,1,171,12,3,8,1,1))
swAuthenticatedPortCtrlEntry.setIndexNames((0,_D,_z))
if mibBuilder.loadTexts:swAuthenticatedPortCtrlEntry.setStatus(_A)
_SwAuthenticatedPortNumber_Type=Integer32
_SwAuthenticatedPortNumber_Object=MibTableColumn
swAuthenticatedPortNumber=_SwAuthenticatedPortNumber_Object((1,3,6,1,4,1,171,12,3,8,1,1,1),_SwAuthenticatedPortNumber_Type())
swAuthenticatedPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swAuthenticatedPortNumber.setStatus(_A)
class _SwAuthenticatedPortCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),('authenticator',2)))
_SwAuthenticatedPortCapabilities_Type.__name__=_C
_SwAuthenticatedPortCapabilities_Object=MibTableColumn
swAuthenticatedPortCapabilities=_SwAuthenticatedPortCapabilities_Object((1,3,6,1,4,1,171,12,3,8,1,1,2),_SwAuthenticatedPortCapabilities_Type())
swAuthenticatedPortCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthenticatedPortCapabilities.setStatus(_A)
_SwMacBasedPaePortInfo_ObjectIdentity=ObjectIdentity
swMacBasedPaePortInfo=_SwMacBasedPaePortInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,9))
_SwMacBasedPaePortTable_Object=MibTable
swMacBasedPaePortTable=_SwMacBasedPaePortTable_Object((1,3,6,1,4,1,171,12,3,9,1))
if mibBuilder.loadTexts:swMacBasedPaePortTable.setStatus(_A)
_SwMacBasedPaePortEntry_Object=MibTableRow
swMacBasedPaePortEntry=_SwMacBasedPaePortEntry_Object((1,3,6,1,4,1,171,12,3,9,1,1))
swMacBasedPaePortEntry.setIndexNames((0,_D,_A0))
if mibBuilder.loadTexts:swMacBasedPaePortEntry.setStatus(_A)
_SwMacBasedPaePortNumber_Type=InterfaceIndex
_SwMacBasedPaePortNumber_Object=MibTableColumn
swMacBasedPaePortNumber=_SwMacBasedPaePortNumber_Object((1,3,6,1,4,1,171,12,3,9,1,1,1),_SwMacBasedPaePortNumber_Type())
swMacBasedPaePortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swMacBasedPaePortNumber.setStatus(_A)
_SwMacBasedPaeMacAddress_Type=MacAddress
_SwMacBasedPaeMacAddress_Object=MibTableColumn
swMacBasedPaeMacAddress=_SwMacBasedPaeMacAddress_Object((1,3,6,1,4,1,171,12,3,9,1,1,2),_SwMacBasedPaeMacAddress_Type())
swMacBasedPaeMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedPaeMacAddress.setStatus(_A)
class _SwMacBasedPaePortInitializeOrReauthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_I,2),(_A1,3)))
_SwMacBasedPaePortInitializeOrReauthStatus_Type.__name__=_C
_SwMacBasedPaePortInitializeOrReauthStatus_Object=MibTableColumn
swMacBasedPaePortInitializeOrReauthStatus=_SwMacBasedPaePortInitializeOrReauthStatus_Object((1,3,6,1,4,1,171,12,3,9,1,1,3),_SwMacBasedPaePortInitializeOrReauthStatus_Type())
swMacBasedPaePortInitializeOrReauthStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedPaePortInitializeOrReauthStatus.setStatus(_A)
_SwMacBasedPaeTable_Object=MibTable
swMacBasedPaeTable=_SwMacBasedPaeTable_Object((1,3,6,1,4,1,171,12,3,9,2))
if mibBuilder.loadTexts:swMacBasedPaeTable.setStatus(_A)
_SwMacBasedPaeEntry_Object=MibTableRow
swMacBasedPaeEntry=_SwMacBasedPaeEntry_Object((1,3,6,1,4,1,171,12,3,9,2,1))
swMacBasedPaeEntry.setIndexNames((0,_D,_A2),(0,_D,_A3))
if mibBuilder.loadTexts:swMacBasedPaeEntry.setStatus(_A)
_SwMacBasedPaePort_Type=InterfaceIndex
_SwMacBasedPaePort_Object=MibTableColumn
swMacBasedPaePort=_SwMacBasedPaePort_Object((1,3,6,1,4,1,171,12,3,9,2,1,1),_SwMacBasedPaePort_Type())
swMacBasedPaePort.setMaxAccess(_G)
if mibBuilder.loadTexts:swMacBasedPaePort.setStatus(_A)
_SwMacBasedPaeMac_Type=MacAddress
_SwMacBasedPaeMac_Object=MibTableColumn
swMacBasedPaeMac=_SwMacBasedPaeMac_Object((1,3,6,1,4,1,171,12,3,9,2,1,2),_SwMacBasedPaeMac_Type())
swMacBasedPaeMac.setMaxAccess(_G)
if mibBuilder.loadTexts:swMacBasedPaeMac.setStatus(_A)
class _SwMacBasedPaeInitOrReauthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_I,2),(_A1,3)))
_SwMacBasedPaeInitOrReauthStatus_Type.__name__=_C
_SwMacBasedPaeInitOrReauthStatus_Object=MibTableColumn
swMacBasedPaeInitOrReauthStatus=_SwMacBasedPaeInitOrReauthStatus_Object((1,3,6,1,4,1,171,12,3,9,2,1,3),_SwMacBasedPaeInitOrReauthStatus_Type())
swMacBasedPaeInitOrReauthStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedPaeInitOrReauthStatus.setStatus(_A)
_SwPaeAuthenticator_ObjectIdentity=ObjectIdentity
swPaeAuthenticator=_SwPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,171,12,3,10))
class _SwPaeAuthSysFwdPdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwPaeAuthSysFwdPdu_Type.__name__=_C
_SwPaeAuthSysFwdPdu_Object=MibScalar
swPaeAuthSysFwdPdu=_SwPaeAuthSysFwdPdu_Object((1,3,6,1,4,1,171,12,3,10,1),_SwPaeAuthSysFwdPdu_Type())
swPaeAuthSysFwdPdu.setMaxAccess(_E)
if mibBuilder.loadTexts:swPaeAuthSysFwdPdu.setStatus(_A)
_SwPaeAuthSysMaxUser_Type=Integer32
_SwPaeAuthSysMaxUser_Object=MibScalar
swPaeAuthSysMaxUser=_SwPaeAuthSysMaxUser_Object((1,3,6,1,4,1,171,12,3,10,2),_SwPaeAuthSysMaxUser_Type())
swPaeAuthSysMaxUser.setMaxAccess(_E)
if mibBuilder.loadTexts:swPaeAuthSysMaxUser.setStatus(_A)
_SwPaeAuthConfigTable_Object=MibTable
swPaeAuthConfigTable=_SwPaeAuthConfigTable_Object((1,3,6,1,4,1,171,12,3,10,3))
if mibBuilder.loadTexts:swPaeAuthConfigTable.setStatus(_A)
_SwPaeAuthConfigEntry_Object=MibTableRow
swPaeAuthConfigEntry=_SwPaeAuthConfigEntry_Object((1,3,6,1,4,1,171,12,3,10,3,1))
swPaeAuthConfigEntry.setIndexNames((0,_g,_h))
if mibBuilder.loadTexts:swPaeAuthConfigEntry.setStatus(_A)
class _SwPaeAuthFwdPdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwPaeAuthFwdPdu_Type.__name__=_C
_SwPaeAuthFwdPdu_Object=MibTableColumn
swPaeAuthFwdPdu=_SwPaeAuthFwdPdu_Object((1,3,6,1,4,1,171,12,3,10,3,1,1),_SwPaeAuthFwdPdu_Type())
swPaeAuthFwdPdu.setMaxAccess(_E)
if mibBuilder.loadTexts:swPaeAuthFwdPdu.setStatus(_A)
_SwPaeAuthMaxUser_Type=Integer32
_SwPaeAuthMaxUser_Object=MibTableColumn
swPaeAuthMaxUser=_SwPaeAuthMaxUser_Object((1,3,6,1,4,1,171,12,3,10,3,1,2),_SwPaeAuthMaxUser_Type())
swPaeAuthMaxUser.setMaxAccess(_E)
if mibBuilder.loadTexts:swPaeAuthMaxUser.setStatus(_A)
_SwAuthStateTable_Object=MibTable
swAuthStateTable=_SwAuthStateTable_Object((1,3,6,1,4,1,171,12,3,10,4))
if mibBuilder.loadTexts:swAuthStateTable.setStatus(_A)
_SwAuthStateEntry_Object=MibTableRow
swAuthStateEntry=_SwAuthStateEntry_Object((1,3,6,1,4,1,171,12,3,10,4,1))
swAuthStateEntry.setIndexNames((0,_D,_A4),(0,_D,_A5))
if mibBuilder.loadTexts:swAuthStateEntry.setStatus(_A)
_SwAuthPortNumber_Type=InterfaceIndex
_SwAuthPortNumber_Object=MibTableColumn
swAuthPortNumber=_SwAuthPortNumber_Object((1,3,6,1,4,1,171,12,3,10,4,1,1),_SwAuthPortNumber_Type())
swAuthPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:swAuthPortNumber.setStatus(_A)
_SwAuthMacAddress_Type=MacAddress
_SwAuthMacAddress_Object=MibTableColumn
swAuthMacAddress=_SwAuthMacAddress_Object((1,3,6,1,4,1,171,12,3,10,4,1,2),_SwAuthMacAddress_Type())
swAuthMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:swAuthMacAddress.setStatus(_A)
class _SwAuthAuthControlledStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_x,2),(_y,3)))
_SwAuthAuthControlledStatus_Type.__name__=_C
_SwAuthAuthControlledStatus_Object=MibTableColumn
swAuthAuthControlledStatus=_SwAuthAuthControlledStatus_Object((1,3,6,1,4,1,171,12,3,10,4,1,3),_SwAuthAuthControlledStatus_Type())
swAuthAuthControlledStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAuthControlledStatus.setStatus(_A)
_SwAuthAssignVid_Type=Integer32
_SwAuthAssignVid_Object=MibTableColumn
swAuthAssignVid=_SwAuthAssignVid_Object((1,3,6,1,4,1,171,12,3,10,4,1,4),_SwAuthAssignVid_Type())
swAuthAssignVid.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAssignVid.setStatus(_A)
_SwAuthAssignPriority_Type=Integer32
_SwAuthAssignPriority_Object=MibTableColumn
swAuthAssignPriority=_SwAuthAssignPriority_Object((1,3,6,1,4,1,171,12,3,10,4,1,5),_SwAuthAssignPriority_Type())
swAuthAssignPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthAssignPriority.setStatus(_A)
class _SwAuthenticatorPAEState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,1),(_S,2),(_T,3),(_N,4),(_U,5),(_V,6),(_W,7),(_X,8),(_Y,9)))
_SwAuthenticatorPAEState_Type.__name__=_C
_SwAuthenticatorPAEState_Object=MibTableColumn
swAuthenticatorPAEState=_SwAuthenticatorPAEState_Object((1,3,6,1,4,1,171,12,3,10,4,1,6),_SwAuthenticatorPAEState_Type())
swAuthenticatorPAEState.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthenticatorPAEState.setStatus(_A)
class _SwAuthBKdAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),(_I,7)))
_SwAuthBKdAuthState_Type.__name__=_C
_SwAuthBKdAuthState_Object=MibTableColumn
swAuthBKdAuthState=_SwAuthBKdAuthState_Object((1,3,6,1,4,1,171,12,3,10,4,1,7),_SwAuthBKdAuthState_Type())
swAuthBKdAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:swAuthBKdAuthState.setStatus(_A)
_SwCompoundAuthMgmt_ObjectIdentity=ObjectIdentity
swCompoundAuthMgmt=_SwCompoundAuthMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,3,11))
_SwCompoundAuthPortTable_Object=MibTable
swCompoundAuthPortTable=_SwCompoundAuthPortTable_Object((1,3,6,1,4,1,171,12,3,11,1))
if mibBuilder.loadTexts:swCompoundAuthPortTable.setStatus(_A)
_SwCompoundAuthPortEntry_Object=MibTableRow
swCompoundAuthPortEntry=_SwCompoundAuthPortEntry_Object((1,3,6,1,4,1,171,12,3,11,1,1))
swCompoundAuthPortEntry.setIndexNames((0,_D,_A6))
if mibBuilder.loadTexts:swCompoundAuthPortEntry.setStatus(_A)
class _SwCompoundAuthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwCompoundAuthPortIndex_Type.__name__=_C
_SwCompoundAuthPortIndex_Object=MibTableColumn
swCompoundAuthPortIndex=_SwCompoundAuthPortIndex_Object((1,3,6,1,4,1,171,12,3,11,1,1,1),_SwCompoundAuthPortIndex_Type())
swCompoundAuthPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swCompoundAuthPortIndex.setStatus(_A)
class _SwCompoundAuthPortAuthMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hostbased',1),('portbased',2)))
_SwCompoundAuthPortAuthMode_Type.__name__=_C
_SwCompoundAuthPortAuthMode_Object=MibTableColumn
swCompoundAuthPortAuthMode=_SwCompoundAuthPortAuthMode_Object((1,3,6,1,4,1,171,12,3,11,1,1,2),_SwCompoundAuthPortAuthMode_Type())
swCompoundAuthPortAuthMode.setMaxAccess(_E)
if mibBuilder.loadTexts:swCompoundAuthPortAuthMode.setStatus(_A)
class _SwCompoundAuthPortMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_f,1),('any',2),('dot1xImpb',3),('impbJwac',4),('impbWac',5),('macImpb',6),('macJwac',7)))
_SwCompoundAuthPortMethod_Type.__name__=_C
_SwCompoundAuthPortMethod_Object=MibTableColumn
swCompoundAuthPortMethod=_SwCompoundAuthPortMethod_Object((1,3,6,1,4,1,171,12,3,11,1,1,3),_SwCompoundAuthPortMethod_Type())
swCompoundAuthPortMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:swCompoundAuthPortMethod.setStatus(_A)
_SwCompoundAuthPortAuthVLANs_Type=DisplayString
_SwCompoundAuthPortAuthVLANs_Object=MibTableColumn
swCompoundAuthPortAuthVLANs=_SwCompoundAuthPortAuthVLANs_Object((1,3,6,1,4,1,171,12,3,11,1,1,4),_SwCompoundAuthPortAuthVLANs_Type())
swCompoundAuthPortAuthVLANs.setMaxAccess(_E)
if mibBuilder.loadTexts:swCompoundAuthPortAuthVLANs.setStatus(_A)
_SwGuestVlanTable_Object=MibTable
swGuestVlanTable=_SwGuestVlanTable_Object((1,3,6,1,4,1,171,12,3,11,2))
if mibBuilder.loadTexts:swGuestVlanTable.setStatus(_A)
_SwGuestVlanEntry_Object=MibTableRow
swGuestVlanEntry=_SwGuestVlanEntry_Object((1,3,6,1,4,1,171,12,3,11,2,1))
swGuestVlanEntry.setIndexNames((0,_D,_A7))
if mibBuilder.loadTexts:swGuestVlanEntry.setStatus(_A)
_SwGuestVlanId_Type=VlanId
_SwGuestVlanId_Object=MibTableColumn
swGuestVlanId=_SwGuestVlanId_Object((1,3,6,1,4,1,171,12,3,11,2,1,1),_SwGuestVlanId_Type())
swGuestVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:swGuestVlanId.setStatus(_A)
_SwGuestVlanPorts_Type=PortList
_SwGuestVlanPorts_Object=MibTableColumn
swGuestVlanPorts=_SwGuestVlanPorts_Object((1,3,6,1,4,1,171,12,3,11,2,1,2),_SwGuestVlanPorts_Type())
swGuestVlanPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:swGuestVlanPorts.setStatus(_A)
_SwGuestVlanRowStatus_Type=RowStatus
_SwGuestVlanRowStatus_Object=MibTableColumn
swGuestVlanRowStatus=_SwGuestVlanRowStatus_Object((1,3,6,1,4,1,171,12,3,11,2,1,3),_SwGuestVlanRowStatus_Type())
swGuestVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:swGuestVlanRowStatus.setStatus(_A)
class _SwAuthorizationAttributes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SwAuthorizationAttributes_Type.__name__=_C
_SwAuthorizationAttributes_Object=MibScalar
swAuthorizationAttributes=_SwAuthorizationAttributes_Object((1,3,6,1,4,1,171,12,3,11,3),_SwAuthorizationAttributes_Type())
swAuthorizationAttributes.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthorizationAttributes.setStatus(_A)
class _SwAuthServerFailoverState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('block',1),('local',2),('permit',3)))
_SwAuthServerFailoverState_Type.__name__=_C
_SwAuthServerFailoverState_Object=MibScalar
swAuthServerFailoverState=_SwAuthServerFailoverState_Object((1,3,6,1,4,1,171,12,3,11,4),_SwAuthServerFailoverState_Type())
swAuthServerFailoverState.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthServerFailoverState.setStatus(_A)
class _SwAuthMACFormatCase_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uppercase',1),('lowercase',2)))
_SwAuthMACFormatCase_Type.__name__=_C
_SwAuthMACFormatCase_Object=MibScalar
swAuthMACFormatCase=_SwAuthMACFormatCase_Object((1,3,6,1,4,1,171,12,3,11,5),_SwAuthMACFormatCase_Type())
swAuthMACFormatCase.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthMACFormatCase.setStatus(_A)
class _SwAuthMACFormatDelimiter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_f,1),('hyphen',2),('colon',3),('dot',4)))
_SwAuthMACFormatDelimiter_Type.__name__=_C
_SwAuthMACFormatDelimiter_Object=MibScalar
swAuthMACFormatDelimiter=_SwAuthMACFormatDelimiter_Object((1,3,6,1,4,1,171,12,3,11,6),_SwAuthMACFormatDelimiter_Type())
swAuthMACFormatDelimiter.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthMACFormatDelimiter.setStatus(_A)
class _SwAuthMACFormatDelimiterNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('delimiter-number-1',1),('delimiter-number-2',2),('delimiter-number-5',3)))
_SwAuthMACFormatDelimiterNumber_Type.__name__=_C
_SwAuthMACFormatDelimiterNumber_Object=MibScalar
swAuthMACFormatDelimiterNumber=_SwAuthMACFormatDelimiterNumber_Object((1,3,6,1,4,1,171,12,3,11,7),_SwAuthMACFormatDelimiterNumber_Type())
swAuthMACFormatDelimiterNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:swAuthMACFormatDelimiterNumber.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'VlanId':VlanId,'swAuthCtrl':swAuthCtrl,'swAuthenCtrl':swAuthenCtrl,'authProtocol':authProtocol,'swAuthMode':swAuthMode,'swAuthorizationState':swAuthorizationState,'swAuthFailOver':swAuthFailOver,'swRadiusCtrl':swRadiusCtrl,'swRadiusDeadTime':swRadiusDeadTime,'swRadiusTimeout':swRadiusTimeout,'swRadiusRetransmitAttempts':swRadiusRetransmitAttempts,'swRadiusServerTable':swRadiusServerTable,'swRadiusServerEntry':swRadiusServerEntry,_k:swRadiusServerIndex,'swRadiusServerIpAddr':swRadiusServerIpAddr,'swRadiusServerKey':swRadiusServerKey,'swRadiusAuthPortNumber':swRadiusAuthPortNumber,'swRadiusAcctPortNumber':swRadiusAcctPortNumber,'swRadiusServerStatus':swRadiusServerStatus,'swRadiusServerTimeout':swRadiusServerTimeout,'swRadiusServerRetransmit':swRadiusServerRetransmit,'swRadiusServerAddrType':swRadiusServerAddrType,'swRadiusServerAddr':swRadiusServerAddr,'swRadiusVrfName':swRadiusVrfName,'swRadiusAuthInfo':swRadiusAuthInfo,'swRadiusAuthClientIdentifier':swRadiusAuthClientIdentifier,'swRadiusAuthClientInvalidServerAddresses':swRadiusAuthClientInvalidServerAddresses,'swRadiusAuthServerTable':swRadiusAuthServerTable,'swRadiusAuthServerEntry':swRadiusAuthServerEntry,_l:swRadiusAuthServerIndex,'swRadiusAuthServerAddress':swRadiusAuthServerAddress,'swRadiusAuthClientServerPortNumber':swRadiusAuthClientServerPortNumber,'swRadiusAuthClientRoundTripTime':swRadiusAuthClientRoundTripTime,'swRadiusAuthClientAccessRequests':swRadiusAuthClientAccessRequests,'swRadiusAuthClientAccessRetransmissions':swRadiusAuthClientAccessRetransmissions,'swRadiusAuthClientAccessAccepts':swRadiusAuthClientAccessAccepts,'swRadiusAuthClientAccessRejects':swRadiusAuthClientAccessRejects,'swRadiusAuthClientAccessChallenges':swRadiusAuthClientAccessChallenges,'swRadiusAuthClientMalformedAccessResponses':swRadiusAuthClientMalformedAccessResponses,'swRadiusAuthClientBadAuthenticators':swRadiusAuthClientBadAuthenticators,'swRadiusAuthClientPendingRequests':swRadiusAuthClientPendingRequests,'swRadiusAuthClientTimeouts':swRadiusAuthClientTimeouts,'swRadiusAuthClientUnknownTypes':swRadiusAuthClientUnknownTypes,'swRadiusAuthClientPacketsDropped':swRadiusAuthClientPacketsDropped,'swRadiusAccountingCtrl':swRadiusAccountingCtrl,'swRadiusAcctUpdateInterval':swRadiusAcctUpdateInterval,'swRadiusAcctSuppressNullUserName':swRadiusAcctSuppressNullUserName,'swRadiusAcctServiceTable':swRadiusAcctServiceTable,'swRadiusAcctServiceEntry':swRadiusAcctServiceEntry,_m:swRadiusAcctServiceIndex,'swRadiusAcctServiceMethod':swRadiusAcctServiceMethod,'swRadiusAcctServiceMode':swRadiusAcctServiceMode,'swRadiusAccountingInfo':swRadiusAccountingInfo,'swMacAuthBaseStatsInfo':swMacAuthBaseStatsInfo,'swMacAuthStateTable':swMacAuthStateTable,'swMacAuthStateEntry':swMacAuthStateEntry,_L:swPaeMacAddr,_M:swPaePortNumber,'swAuthPaeState':swAuthPaeState,'swAuthBackendAuthState':swAuthBackendAuthState,'swAuthAuthControlledPortStatus':swAuthAuthControlledPortStatus,'swMacAuthStatsTable':swMacAuthStatsTable,'swMacAuthStatsEntry':swMacAuthStatsEntry,'swAuthEapolFramesRx':swAuthEapolFramesRx,'swAuthEapolFramesTx':swAuthEapolFramesTx,'swAuthEapolStartFramesRx':swAuthEapolStartFramesRx,'swAuthEapolLogoffFramesRx':swAuthEapolLogoffFramesRx,'swAuthEapolRespIdFramesRx':swAuthEapolRespIdFramesRx,'swAuthEapolRespFramesRx':swAuthEapolRespFramesRx,'swAuthEapolReqIdFramesTx':swAuthEapolReqIdFramesTx,'swAuthEapolReqFramesTx':swAuthEapolReqFramesTx,'swAuthInvalidEapolFramesRx':swAuthInvalidEapolFramesRx,'swAuthEapLengthErrorFramesRx':swAuthEapLengthErrorFramesRx,'swAuthLastEapolFrameVersion':swAuthLastEapolFrameVersion,'swAuthLastEapolFrameSource':swAuthLastEapolFrameSource,'swMacAuthDiagTable':swMacAuthDiagTable,'swMacAuthDiagEntry':swMacAuthDiagEntry,'swAuthEntersConnecting':swAuthEntersConnecting,'swAuthEapLogoffsWhileConnecting':swAuthEapLogoffsWhileConnecting,'swAuthEntersAuthenticating':swAuthEntersAuthenticating,'swAuthAuthSuccessWhileAuthenticating':swAuthAuthSuccessWhileAuthenticating,'swAuthAuthTimeoutsWhileAuthenticating':swAuthAuthTimeoutsWhileAuthenticating,'swAuthAuthFailWhileAuthenticating':swAuthAuthFailWhileAuthenticating,'swAuthAuthReauthsWhileAuthenticating':swAuthAuthReauthsWhileAuthenticating,'swAuthAuthEapStartsWhileAuthenticating':swAuthAuthEapStartsWhileAuthenticating,'swAuthAuthEapLogoffWhileAuthenticating':swAuthAuthEapLogoffWhileAuthenticating,'swAuthAuthReauthsWhileAuthenticated':swAuthAuthReauthsWhileAuthenticated,'swAuthAuthEapStartsWhileAuthenticated':swAuthAuthEapStartsWhileAuthenticated,'swAuthAuthEapLogoffWhileAuthenticated':swAuthAuthEapLogoffWhileAuthenticated,'swAuthBackendResponses':swAuthBackendResponses,'swAuthBackendAccessChallenges':swAuthBackendAccessChallenges,'swAuthBackendOtherRequestsToSupplicant':swAuthBackendOtherRequestsToSupplicant,'swAuthBackendNonNakResponsesFromSupplicant':swAuthBackendNonNakResponsesFromSupplicant,'swAuthBackendAuthSuccesses':swAuthBackendAuthSuccesses,'swAuthBackendAuthFails':swAuthBackendAuthFails,'swMacAuthSessionStatsTable':swMacAuthSessionStatsTable,'swMacAuthSessionStatsEntry':swMacAuthSessionStatsEntry,'swAuthSessionOctetsRx':swAuthSessionOctetsRx,'swAuthSessionOctetsTx':swAuthSessionOctetsTx,'swAuthSessionFramesRx':swAuthSessionFramesRx,'swAuthSessionFramesTx':swAuthSessionFramesTx,'swAuthSessionId':swAuthSessionId,'swAuthSessionAuthenticMethod':swAuthSessionAuthenticMethod,'swAuthSessionTime':swAuthSessionTime,'swAuthSessionTerminateCause':swAuthSessionTerminateCause,'swAuthSessionUserName':swAuthSessionUserName,'swDot1xAuthStateTable':swDot1xAuthStateTable,'swDot1xAuthStateEntry':swDot1xAuthStateEntry,_O:swDot1xAuthPortNumber,_P:swDot1xAuthVID,_Q:swDot1xAuthMACAddress,'swDot1xAuthenticatorPAEState':swDot1xAuthenticatorPAEState,'swDot1xAuthBackendAuthState':swDot1xAuthBackendAuthState,'swDot1xAuthAuthControlledStatus':swDot1xAuthAuthControlledStatus,'swDot1xAuthAssignVID':swDot1xAuthAssignVID,'swDot1xAuthAssignPriority':swDot1xAuthAssignPriority,'swDot1xAuthStatsTable':swDot1xAuthStatsTable,'swDot1xAuthStatsEntry':swDot1xAuthStatsEntry,'swDot1xAuthEapolFramesRx':swDot1xAuthEapolFramesRx,'swDot1xAuthEapolFramesTx':swDot1xAuthEapolFramesTx,'swDot1xAuthEapolStartFramesRx':swDot1xAuthEapolStartFramesRx,'swDot1xAuthEapolLogoffFramesRx':swDot1xAuthEapolLogoffFramesRx,'swDot1xAuthEapolRespIdFramesRx':swDot1xAuthEapolRespIdFramesRx,'swDot1xAuthEapolRespFramesRx':swDot1xAuthEapolRespFramesRx,'swDot1xAuthEapolReqIdFramesTx':swDot1xAuthEapolReqIdFramesTx,'swDot1xAuthEapolReqFramesTx':swDot1xAuthEapolReqFramesTx,'swDot1xAuthInvalidEapolFramesRx':swDot1xAuthInvalidEapolFramesRx,'swDot1xAuthEapLengthErrorFramesRx':swDot1xAuthEapLengthErrorFramesRx,'swDot1xAuthLastEapolFrameVersion':swDot1xAuthLastEapolFrameVersion,'swDot1xAuthLastEapolFrameSource':swDot1xAuthLastEapolFrameSource,'swDot1xAuthDiagTable':swDot1xAuthDiagTable,'swDot1xAuthDiagEntry':swDot1xAuthDiagEntry,'swDot1xAuthEntersConnecting':swDot1xAuthEntersConnecting,'swDot1xAuthEapLogoffsWhileConnecting':swDot1xAuthEapLogoffsWhileConnecting,'swDot1xAuthEntersAuthenticating':swDot1xAuthEntersAuthenticating,'swDot1xAuthAuthSuccessWhileAuthenticating':swDot1xAuthAuthSuccessWhileAuthenticating,'swDot1xAuthAuthTimeoutsWhileAuthenticating':swDot1xAuthAuthTimeoutsWhileAuthenticating,'swDot1xAuthAuthFailWhileAuthenticating':swDot1xAuthAuthFailWhileAuthenticating,'swDot1xAuthAuthReauthsWhileAuthenticating':swDot1xAuthAuthReauthsWhileAuthenticating,'swDot1xAuthAuthEapStartsWhileAuthenticating':swDot1xAuthAuthEapStartsWhileAuthenticating,'swDot1xAuthAuthEapLogoffWhileAuthenticating':swDot1xAuthAuthEapLogoffWhileAuthenticating,'swDot1xAuthAuthReauthsWhileAuthenticated':swDot1xAuthAuthReauthsWhileAuthenticated,'swDot1xAuthAuthEapStartsWhileAuthenticated':swDot1xAuthAuthEapStartsWhileAuthenticated,'swDot1xAuthAuthEapLogoffWhileAuthenticated':swDot1xAuthAuthEapLogoffWhileAuthenticated,'swDot1xAuthBackendResponses':swDot1xAuthBackendResponses,'swDot1xAuthBackendAccessChallenges':swDot1xAuthBackendAccessChallenges,'swDot1xAuthBackendOtherRequestsToSupplicant':swDot1xAuthBackendOtherRequestsToSupplicant,'swDot1xAuthBackendNonNakResponsesFromSupplicant':swDot1xAuthBackendNonNakResponsesFromSupplicant,'swDot1xAuthBackendAuthSuccesses':swDot1xAuthBackendAuthSuccesses,'swDot1xAuthBackendAuthFails':swDot1xAuthBackendAuthFails,'swDot1xAuthSessionStatsTable':swDot1xAuthSessionStatsTable,'swDot1xAuthSessionStatsEntry':swDot1xAuthSessionStatsEntry,'swDot1xAuthSessionOctetsRx':swDot1xAuthSessionOctetsRx,'swDot1xAuthSessionOctetsTx':swDot1xAuthSessionOctetsTx,'swDot1xAuthSessionFramesRx':swDot1xAuthSessionFramesRx,'swDot1xAuthSessionFramesTx':swDot1xAuthSessionFramesTx,'swDot1xAuthSessionId':swDot1xAuthSessionId,'swDot1xAuthSessionAuthenticMethod':swDot1xAuthSessionAuthenticMethod,'swDot1xAuthSessionTime':swDot1xAuthSessionTime,'swDot1xAuthSessionTerminateCause':swDot1xAuthSessionTerminateCause,'swDot1xAuthSessionUserName':swDot1xAuthSessionUserName,'swRadiusCommand':swRadiusCommand,'swRadiusForceDownPortNumber':swRadiusForceDownPortNumber,'swRadiusForceDownMacAddr':swRadiusForceDownMacAddr,'swAuthenticatedPortInfo':swAuthenticatedPortInfo,'swAuthenticatedPortCtrlTable':swAuthenticatedPortCtrlTable,'swAuthenticatedPortCtrlEntry':swAuthenticatedPortCtrlEntry,_z:swAuthenticatedPortNumber,'swAuthenticatedPortCapabilities':swAuthenticatedPortCapabilities,'swMacBasedPaePortInfo':swMacBasedPaePortInfo,'swMacBasedPaePortTable':swMacBasedPaePortTable,'swMacBasedPaePortEntry':swMacBasedPaePortEntry,_A0:swMacBasedPaePortNumber,'swMacBasedPaeMacAddress':swMacBasedPaeMacAddress,'swMacBasedPaePortInitializeOrReauthStatus':swMacBasedPaePortInitializeOrReauthStatus,'swMacBasedPaeTable':swMacBasedPaeTable,'swMacBasedPaeEntry':swMacBasedPaeEntry,_A2:swMacBasedPaePort,_A3:swMacBasedPaeMac,'swMacBasedPaeInitOrReauthStatus':swMacBasedPaeInitOrReauthStatus,'swPaeAuthenticator':swPaeAuthenticator,'swPaeAuthSysFwdPdu':swPaeAuthSysFwdPdu,'swPaeAuthSysMaxUser':swPaeAuthSysMaxUser,'swPaeAuthConfigTable':swPaeAuthConfigTable,'swPaeAuthConfigEntry':swPaeAuthConfigEntry,'swPaeAuthFwdPdu':swPaeAuthFwdPdu,'swPaeAuthMaxUser':swPaeAuthMaxUser,'swAuthStateTable':swAuthStateTable,'swAuthStateEntry':swAuthStateEntry,_A4:swAuthPortNumber,_A5:swAuthMacAddress,'swAuthAuthControlledStatus':swAuthAuthControlledStatus,'swAuthAssignVid':swAuthAssignVid,'swAuthAssignPriority':swAuthAssignPriority,'swAuthenticatorPAEState':swAuthenticatorPAEState,'swAuthBKdAuthState':swAuthBKdAuthState,'swCompoundAuthMgmt':swCompoundAuthMgmt,'swCompoundAuthPortTable':swCompoundAuthPortTable,'swCompoundAuthPortEntry':swCompoundAuthPortEntry,_A6:swCompoundAuthPortIndex,'swCompoundAuthPortAuthMode':swCompoundAuthPortAuthMode,'swCompoundAuthPortMethod':swCompoundAuthPortMethod,'swCompoundAuthPortAuthVLANs':swCompoundAuthPortAuthVLANs,'swGuestVlanTable':swGuestVlanTable,'swGuestVlanEntry':swGuestVlanEntry,_A7:swGuestVlanId,'swGuestVlanPorts':swGuestVlanPorts,'swGuestVlanRowStatus':swGuestVlanRowStatus,'swAuthorizationAttributes':swAuthorizationAttributes,'swAuthServerFailoverState':swAuthServerFailoverState,'swAuthMACFormatCase':swAuthMACFormatCase,'swAuthMACFormatDelimiter':swAuthMACFormatDelimiter,'swAuthMACFormatDelimiterNumber':swAuthMACFormatDelimiterNumber})