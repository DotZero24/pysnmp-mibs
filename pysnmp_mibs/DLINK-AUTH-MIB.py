_O='initialize'
_N='swRadiusAcctServerIndex'
_M='swRadiusAcctServiceIndex'
_L='swRadiusAuthServerIndex'
_K='swRadiusServerIndex'
_J='OctetString'
_I='swPaePortNumber'
_H='swPaeMacAddr'
_G='Unsigned32'
_F='read-write'
_E='Integer32'
_D='DLINK-AUTH-MIB'
_C='obsolete'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PaeControlledPortStatus,=mibBuilder.importSymbols('IEEE8021-PAE-MIB','PaeControlledPortStatus')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
swDlinkAuthCtrl=ModuleIdentity((1,3,6,1,4,1,171,12,3))
_SwAuthCtrl_ObjectIdentity=ObjectIdentity
swAuthCtrl=_SwAuthCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,3,1))
class _AuthProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authProtocolRadiusEap',1),('authProtocolRadiusPap',2)))
_AuthProtocol_Type.__name__=_E
_AuthProtocol_Object=MibScalar
authProtocol=_AuthProtocol_Object((1,3,6,1,4,1,171,12,3,1,1),_AuthProtocol_Type())
authProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:authProtocol.setStatus(_B)
class _SwAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('portBase',1),('macBase',2),('none',3)))
_SwAuthMode_Type.__name__=_E
_SwAuthMode_Object=MibScalar
swAuthMode=_SwAuthMode_Object((1,3,6,1,4,1,171,12,3,1,2),_SwAuthMode_Type())
swAuthMode.setMaxAccess(_F)
if mibBuilder.loadTexts:swAuthMode.setStatus(_B)
class _SwFakeAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_SwFakeAuthentication_Type.__name__=_E
_SwFakeAuthentication_Object=MibScalar
swFakeAuthentication=_SwFakeAuthentication_Object((1,3,6,1,4,1,171,12,3,1,3),_SwFakeAuthentication_Type())
swFakeAuthentication.setMaxAccess(_F)
if mibBuilder.loadTexts:swFakeAuthentication.setStatus(_B)
_SwRadiusCtrl_ObjectIdentity=ObjectIdentity
swRadiusCtrl=_SwRadiusCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,3,2))
_SwRadiusServerTable_Object=MibTable
swRadiusServerTable=_SwRadiusServerTable_Object((1,3,6,1,4,1,171,12,3,2,4))
if mibBuilder.loadTexts:swRadiusServerTable.setStatus(_B)
_SwRadiusServerEntry_Object=MibTableRow
swRadiusServerEntry=_SwRadiusServerEntry_Object((1,3,6,1,4,1,171,12,3,2,4,1))
swRadiusServerEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:swRadiusServerEntry.setStatus(_B)
class _SwRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('swRadiusServerIndex-first',1),('swRadiusServerIndex-second',2),('swRadiusServerIndex-third',3)))
_SwRadiusServerIndex_Type.__name__=_E
_SwRadiusServerIndex_Object=MibTableColumn
swRadiusServerIndex=_SwRadiusServerIndex_Object((1,3,6,1,4,1,171,12,3,2,4,1,1),_SwRadiusServerIndex_Type())
swRadiusServerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusServerIndex.setStatus(_B)
_SwRadiusServerIpAddr_Type=IpAddress
_SwRadiusServerIpAddr_Object=MibTableColumn
swRadiusServerIpAddr=_SwRadiusServerIpAddr_Object((1,3,6,1,4,1,171,12,3,2,4,1,2),_SwRadiusServerIpAddr_Type())
swRadiusServerIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusServerIpAddr.setStatus(_B)
class _SwRadiusServerKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwRadiusServerKey_Type.__name__=_J
_SwRadiusServerKey_Object=MibTableColumn
swRadiusServerKey=_SwRadiusServerKey_Object((1,3,6,1,4,1,171,12,3,2,4,1,3),_SwRadiusServerKey_Type())
swRadiusServerKey.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swRadiusServerKey.setStatus(_B)
class _SwRadiusAuthPortNumber_Type(Unsigned32):defaultValue=1812
_SwRadiusAuthPortNumber_Type.__name__=_G
_SwRadiusAuthPortNumber_Object=MibTableColumn
swRadiusAuthPortNumber=_SwRadiusAuthPortNumber_Object((1,3,6,1,4,1,171,12,3,2,4,1,4),_SwRadiusAuthPortNumber_Type())
swRadiusAuthPortNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthPortNumber.setStatus(_B)
class _SwRadiusAcctPortNumber_Type(Unsigned32):defaultValue=1813
_SwRadiusAcctPortNumber_Type.__name__=_G
_SwRadiusAcctPortNumber_Object=MibTableColumn
swRadiusAcctPortNumber=_SwRadiusAcctPortNumber_Object((1,3,6,1,4,1,171,12,3,2,4,1,5),_SwRadiusAcctPortNumber_Type())
swRadiusAcctPortNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctPortNumber.setStatus(_B)
_SwRadiusServerStatus_Type=RowStatus
_SwRadiusServerStatus_Object=MibTableColumn
swRadiusServerStatus=_SwRadiusServerStatus_Object((1,3,6,1,4,1,171,12,3,2,4,1,6),_SwRadiusServerStatus_Type())
swRadiusServerStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusServerStatus.setStatus(_B)
_SwRadiusAuthInfo_ObjectIdentity=ObjectIdentity
swRadiusAuthInfo=_SwRadiusAuthInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,3))
class _SwRadiusAuthClientIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SwRadiusAuthClientIdentifier_Type.__name__=_J
_SwRadiusAuthClientIdentifier_Object=MibScalar
swRadiusAuthClientIdentifier=_SwRadiusAuthClientIdentifier_Object((1,3,6,1,4,1,171,12,3,3,1),_SwRadiusAuthClientIdentifier_Type())
swRadiusAuthClientIdentifier.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientIdentifier.setStatus(_C)
_SwRadiusAuthClientInvalidServerAddresses_Type=Counter32
_SwRadiusAuthClientInvalidServerAddresses_Object=MibScalar
swRadiusAuthClientInvalidServerAddresses=_SwRadiusAuthClientInvalidServerAddresses_Object((1,3,6,1,4,1,171,12,3,3,2),_SwRadiusAuthClientInvalidServerAddresses_Type())
swRadiusAuthClientInvalidServerAddresses.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientInvalidServerAddresses.setStatus(_C)
_SwRadiusAuthServerTable_Object=MibTable
swRadiusAuthServerTable=_SwRadiusAuthServerTable_Object((1,3,6,1,4,1,171,12,3,3,3))
if mibBuilder.loadTexts:swRadiusAuthServerTable.setStatus(_C)
_SwRadiusAuthServerEntry_Object=MibTableRow
swRadiusAuthServerEntry=_SwRadiusAuthServerEntry_Object((1,3,6,1,4,1,171,12,3,3,3,1))
swRadiusAuthServerEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:swRadiusAuthServerEntry.setStatus(_C)
_SwRadiusAuthServerIndex_Type=Integer32
_SwRadiusAuthServerIndex_Object=MibTableColumn
swRadiusAuthServerIndex=_SwRadiusAuthServerIndex_Object((1,3,6,1,4,1,171,12,3,3,3,1,1),_SwRadiusAuthServerIndex_Type())
swRadiusAuthServerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthServerIndex.setStatus(_C)
_SwRadiusAuthServerAddress_Type=IpAddress
_SwRadiusAuthServerAddress_Object=MibTableColumn
swRadiusAuthServerAddress=_SwRadiusAuthServerAddress_Object((1,3,6,1,4,1,171,12,3,3,3,1,2),_SwRadiusAuthServerAddress_Type())
swRadiusAuthServerAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthServerAddress.setStatus(_C)
class _SwRadiusAuthClientServerPortNumber_Type(Unsigned32):defaultValue=1812
_SwRadiusAuthClientServerPortNumber_Type.__name__=_G
_SwRadiusAuthClientServerPortNumber_Object=MibTableColumn
swRadiusAuthClientServerPortNumber=_SwRadiusAuthClientServerPortNumber_Object((1,3,6,1,4,1,171,12,3,3,3,1,3),_SwRadiusAuthClientServerPortNumber_Type())
swRadiusAuthClientServerPortNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientServerPortNumber.setStatus(_C)
_SwRadiusAuthClientRoundTripTime_Type=Counter32
_SwRadiusAuthClientRoundTripTime_Object=MibTableColumn
swRadiusAuthClientRoundTripTime=_SwRadiusAuthClientRoundTripTime_Object((1,3,6,1,4,1,171,12,3,3,3,1,4),_SwRadiusAuthClientRoundTripTime_Type())
swRadiusAuthClientRoundTripTime.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientRoundTripTime.setStatus(_C)
_SwRadiusAuthClientAccessRequests_Type=Counter32
_SwRadiusAuthClientAccessRequests_Object=MibTableColumn
swRadiusAuthClientAccessRequests=_SwRadiusAuthClientAccessRequests_Object((1,3,6,1,4,1,171,12,3,3,3,1,5),_SwRadiusAuthClientAccessRequests_Type())
swRadiusAuthClientAccessRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientAccessRequests.setStatus(_C)
_SwRadiusAuthClientAccessRetransmissions_Type=Counter32
_SwRadiusAuthClientAccessRetransmissions_Object=MibTableColumn
swRadiusAuthClientAccessRetransmissions=_SwRadiusAuthClientAccessRetransmissions_Object((1,3,6,1,4,1,171,12,3,3,3,1,6),_SwRadiusAuthClientAccessRetransmissions_Type())
swRadiusAuthClientAccessRetransmissions.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientAccessRetransmissions.setStatus(_C)
_SwRadiusAuthClientAccessAccepts_Type=Counter32
_SwRadiusAuthClientAccessAccepts_Object=MibTableColumn
swRadiusAuthClientAccessAccepts=_SwRadiusAuthClientAccessAccepts_Object((1,3,6,1,4,1,171,12,3,3,3,1,7),_SwRadiusAuthClientAccessAccepts_Type())
swRadiusAuthClientAccessAccepts.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientAccessAccepts.setStatus(_C)
_SwRadiusAuthClientAccessRejects_Type=Counter32
_SwRadiusAuthClientAccessRejects_Object=MibTableColumn
swRadiusAuthClientAccessRejects=_SwRadiusAuthClientAccessRejects_Object((1,3,6,1,4,1,171,12,3,3,3,1,8),_SwRadiusAuthClientAccessRejects_Type())
swRadiusAuthClientAccessRejects.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientAccessRejects.setStatus(_C)
_SwRadiusAuthClientAccessChallenges_Type=Counter32
_SwRadiusAuthClientAccessChallenges_Object=MibTableColumn
swRadiusAuthClientAccessChallenges=_SwRadiusAuthClientAccessChallenges_Object((1,3,6,1,4,1,171,12,3,3,3,1,9),_SwRadiusAuthClientAccessChallenges_Type())
swRadiusAuthClientAccessChallenges.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientAccessChallenges.setStatus(_C)
_SwRadiusAuthClientMalformedAccessResponses_Type=Counter32
_SwRadiusAuthClientMalformedAccessResponses_Object=MibTableColumn
swRadiusAuthClientMalformedAccessResponses=_SwRadiusAuthClientMalformedAccessResponses_Object((1,3,6,1,4,1,171,12,3,3,3,1,10),_SwRadiusAuthClientMalformedAccessResponses_Type())
swRadiusAuthClientMalformedAccessResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientMalformedAccessResponses.setStatus(_C)
_SwRadiusAuthClientBadAuthenticators_Type=Counter32
_SwRadiusAuthClientBadAuthenticators_Object=MibTableColumn
swRadiusAuthClientBadAuthenticators=_SwRadiusAuthClientBadAuthenticators_Object((1,3,6,1,4,1,171,12,3,3,3,1,11),_SwRadiusAuthClientBadAuthenticators_Type())
swRadiusAuthClientBadAuthenticators.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientBadAuthenticators.setStatus(_C)
_SwRadiusAuthClientPendingRequests_Type=Counter32
_SwRadiusAuthClientPendingRequests_Object=MibTableColumn
swRadiusAuthClientPendingRequests=_SwRadiusAuthClientPendingRequests_Object((1,3,6,1,4,1,171,12,3,3,3,1,12),_SwRadiusAuthClientPendingRequests_Type())
swRadiusAuthClientPendingRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientPendingRequests.setStatus(_C)
_SwRadiusAuthClientTimeouts_Type=Counter32
_SwRadiusAuthClientTimeouts_Object=MibTableColumn
swRadiusAuthClientTimeouts=_SwRadiusAuthClientTimeouts_Object((1,3,6,1,4,1,171,12,3,3,3,1,13),_SwRadiusAuthClientTimeouts_Type())
swRadiusAuthClientTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientTimeouts.setStatus(_C)
_SwRadiusAuthClientUnknownTypes_Type=Counter32
_SwRadiusAuthClientUnknownTypes_Object=MibTableColumn
swRadiusAuthClientUnknownTypes=_SwRadiusAuthClientUnknownTypes_Object((1,3,6,1,4,1,171,12,3,3,3,1,14),_SwRadiusAuthClientUnknownTypes_Type())
swRadiusAuthClientUnknownTypes.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientUnknownTypes.setStatus(_C)
_SwRadiusAuthClientPacketsDropped_Type=Counter32
_SwRadiusAuthClientPacketsDropped_Object=MibTableColumn
swRadiusAuthClientPacketsDropped=_SwRadiusAuthClientPacketsDropped_Object((1,3,6,1,4,1,171,12,3,3,3,1,15),_SwRadiusAuthClientPacketsDropped_Type())
swRadiusAuthClientPacketsDropped.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAuthClientPacketsDropped.setStatus(_C)
_SwRadiusAccountingCtrl_ObjectIdentity=ObjectIdentity
swRadiusAccountingCtrl=_SwRadiusAccountingCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,3,4))
class _SwRadiusAcctUpdateInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwRadiusAcctUpdateInterval_Type.__name__=_G
_SwRadiusAcctUpdateInterval_Object=MibScalar
swRadiusAcctUpdateInterval=_SwRadiusAcctUpdateInterval_Object((1,3,6,1,4,1,171,12,3,4,1),_SwRadiusAcctUpdateInterval_Type())
swRadiusAcctUpdateInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:swRadiusAcctUpdateInterval.setStatus(_B)
_SwRadiusAcctSuppressNullUserName_Type=TruthValue
_SwRadiusAcctSuppressNullUserName_Object=MibScalar
swRadiusAcctSuppressNullUserName=_SwRadiusAcctSuppressNullUserName_Object((1,3,6,1,4,1,171,12,3,4,2),_SwRadiusAcctSuppressNullUserName_Type())
swRadiusAcctSuppressNullUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:swRadiusAcctSuppressNullUserName.setStatus(_B)
_SwRadiusAcctServiceTable_Object=MibTable
swRadiusAcctServiceTable=_SwRadiusAcctServiceTable_Object((1,3,6,1,4,1,171,12,3,4,3))
if mibBuilder.loadTexts:swRadiusAcctServiceTable.setStatus(_B)
_SwRadiusAcctServiceEntry_Object=MibTableRow
swRadiusAcctServiceEntry=_SwRadiusAcctServiceEntry_Object((1,3,6,1,4,1,171,12,3,4,3,1))
swRadiusAcctServiceEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:swRadiusAcctServiceEntry.setStatus(_B)
class _SwRadiusAcctServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acctServiceIndex-network',1),('acctServiceIndex-exec',2),('acctServiceIndex-system',3)))
_SwRadiusAcctServiceIndex_Type.__name__=_E
_SwRadiusAcctServiceIndex_Object=MibTableColumn
swRadiusAcctServiceIndex=_SwRadiusAcctServiceIndex_Object((1,3,6,1,4,1,171,12,3,4,3,1,1),_SwRadiusAcctServiceIndex_Type())
swRadiusAcctServiceIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctServiceIndex.setStatus(_B)
class _SwRadiusAcctServiceMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('swRadiusAcctServiceMethodNone',1),('swRadiusAcctServiceMethodRadius',2)))
_SwRadiusAcctServiceMethod_Type.__name__=_E
_SwRadiusAcctServiceMethod_Object=MibTableColumn
swRadiusAcctServiceMethod=_SwRadiusAcctServiceMethod_Object((1,3,6,1,4,1,171,12,3,4,3,1,2),_SwRadiusAcctServiceMethod_Type())
swRadiusAcctServiceMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:swRadiusAcctServiceMethod.setStatus(_B)
class _SwRadiusAcctServiceMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('radiusAcctServiceModeNone',1),('radiusAcctServiceModeStartStop',2),('radiusAcctServiceModeStopOnly',3)))
_SwRadiusAcctServiceMode_Type.__name__=_E
_SwRadiusAcctServiceMode_Object=MibTableColumn
swRadiusAcctServiceMode=_SwRadiusAcctServiceMode_Object((1,3,6,1,4,1,171,12,3,4,3,1,3),_SwRadiusAcctServiceMode_Type())
swRadiusAcctServiceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:swRadiusAcctServiceMode.setStatus(_B)
_SwRadiusAccountingInfo_ObjectIdentity=ObjectIdentity
swRadiusAccountingInfo=_SwRadiusAccountingInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,5))
class _SwRadiusAcctClientIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SwRadiusAcctClientIdentifier_Type.__name__=_J
_SwRadiusAcctClientIdentifier_Object=MibScalar
swRadiusAcctClientIdentifier=_SwRadiusAcctClientIdentifier_Object((1,3,6,1,4,1,171,12,3,5,1),_SwRadiusAcctClientIdentifier_Type())
swRadiusAcctClientIdentifier.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientIdentifier.setStatus(_C)
_SwRadiusAcctClientInvalidServerAddresses_Type=IpAddress
_SwRadiusAcctClientInvalidServerAddresses_Object=MibScalar
swRadiusAcctClientInvalidServerAddresses=_SwRadiusAcctClientInvalidServerAddresses_Object((1,3,6,1,4,1,171,12,3,5,2),_SwRadiusAcctClientInvalidServerAddresses_Type())
swRadiusAcctClientInvalidServerAddresses.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientInvalidServerAddresses.setStatus(_C)
_SwRadiusAcctServerTable_Object=MibTable
swRadiusAcctServerTable=_SwRadiusAcctServerTable_Object((1,3,6,1,4,1,171,12,3,5,3))
if mibBuilder.loadTexts:swRadiusAcctServerTable.setStatus(_C)
_SwRadiusAcctServerEntry_Object=MibTableRow
swRadiusAcctServerEntry=_SwRadiusAcctServerEntry_Object((1,3,6,1,4,1,171,12,3,5,3,1))
swRadiusAcctServerEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:swRadiusAcctServerEntry.setStatus(_C)
_SwRadiusAcctServerIndex_Type=Integer32
_SwRadiusAcctServerIndex_Object=MibTableColumn
swRadiusAcctServerIndex=_SwRadiusAcctServerIndex_Object((1,3,6,1,4,1,171,12,3,5,3,1,1),_SwRadiusAcctServerIndex_Type())
swRadiusAcctServerIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctServerIndex.setStatus(_C)
_SwRadiusAcctServerAddress_Type=IpAddress
_SwRadiusAcctServerAddress_Object=MibTableColumn
swRadiusAcctServerAddress=_SwRadiusAcctServerAddress_Object((1,3,6,1,4,1,171,12,3,5,3,1,2),_SwRadiusAcctServerAddress_Type())
swRadiusAcctServerAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctServerAddress.setStatus(_C)
class _SwRadiusAcctClientServerPortNumber_Type(Unsigned32):defaultValue=1813
_SwRadiusAcctClientServerPortNumber_Type.__name__=_G
_SwRadiusAcctClientServerPortNumber_Object=MibTableColumn
swRadiusAcctClientServerPortNumber=_SwRadiusAcctClientServerPortNumber_Object((1,3,6,1,4,1,171,12,3,5,3,1,3),_SwRadiusAcctClientServerPortNumber_Type())
swRadiusAcctClientServerPortNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientServerPortNumber.setStatus(_C)
_SwRadiusAcctClientRoundTripTime_Type=Counter32
_SwRadiusAcctClientRoundTripTime_Object=MibTableColumn
swRadiusAcctClientRoundTripTime=_SwRadiusAcctClientRoundTripTime_Object((1,3,6,1,4,1,171,12,3,5,3,1,4),_SwRadiusAcctClientRoundTripTime_Type())
swRadiusAcctClientRoundTripTime.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientRoundTripTime.setStatus(_C)
_SwRadiusAcctClientRequests_Type=Counter32
_SwRadiusAcctClientRequests_Object=MibTableColumn
swRadiusAcctClientRequests=_SwRadiusAcctClientRequests_Object((1,3,6,1,4,1,171,12,3,5,3,1,5),_SwRadiusAcctClientRequests_Type())
swRadiusAcctClientRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientRequests.setStatus(_C)
_SwRadiusAcctClientRetransmissions_Type=Counter32
_SwRadiusAcctClientRetransmissions_Object=MibTableColumn
swRadiusAcctClientRetransmissions=_SwRadiusAcctClientRetransmissions_Object((1,3,6,1,4,1,171,12,3,5,3,1,6),_SwRadiusAcctClientRetransmissions_Type())
swRadiusAcctClientRetransmissions.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientRetransmissions.setStatus(_C)
_SwRadiusAcctClientResponses_Type=Counter32
_SwRadiusAcctClientResponses_Object=MibTableColumn
swRadiusAcctClientResponses=_SwRadiusAcctClientResponses_Object((1,3,6,1,4,1,171,12,3,5,3,1,7),_SwRadiusAcctClientResponses_Type())
swRadiusAcctClientResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientResponses.setStatus(_C)
_SwRadiusAcctClientMalformedResponses_Type=Counter32
_SwRadiusAcctClientMalformedResponses_Object=MibTableColumn
swRadiusAcctClientMalformedResponses=_SwRadiusAcctClientMalformedResponses_Object((1,3,6,1,4,1,171,12,3,5,3,1,8),_SwRadiusAcctClientMalformedResponses_Type())
swRadiusAcctClientMalformedResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientMalformedResponses.setStatus(_C)
_SwRadiusAcctClientBadAuthenticators_Type=Counter32
_SwRadiusAcctClientBadAuthenticators_Object=MibTableColumn
swRadiusAcctClientBadAuthenticators=_SwRadiusAcctClientBadAuthenticators_Object((1,3,6,1,4,1,171,12,3,5,3,1,9),_SwRadiusAcctClientBadAuthenticators_Type())
swRadiusAcctClientBadAuthenticators.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientBadAuthenticators.setStatus(_C)
_SwRadiusAcctClientPendingRequests_Type=Counter32
_SwRadiusAcctClientPendingRequests_Object=MibTableColumn
swRadiusAcctClientPendingRequests=_SwRadiusAcctClientPendingRequests_Object((1,3,6,1,4,1,171,12,3,5,3,1,10),_SwRadiusAcctClientPendingRequests_Type())
swRadiusAcctClientPendingRequests.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientPendingRequests.setStatus(_C)
_SwRadiusAcctClientTimeouts_Type=Counter32
_SwRadiusAcctClientTimeouts_Object=MibTableColumn
swRadiusAcctClientTimeouts=_SwRadiusAcctClientTimeouts_Object((1,3,6,1,4,1,171,12,3,5,3,1,11),_SwRadiusAcctClientTimeouts_Type())
swRadiusAcctClientTimeouts.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientTimeouts.setStatus(_C)
_SwRadiusAcctClientUnknownTypes_Type=Counter32
_SwRadiusAcctClientUnknownTypes_Object=MibTableColumn
swRadiusAcctClientUnknownTypes=_SwRadiusAcctClientUnknownTypes_Object((1,3,6,1,4,1,171,12,3,5,3,1,12),_SwRadiusAcctClientUnknownTypes_Type())
swRadiusAcctClientUnknownTypes.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientUnknownTypes.setStatus(_C)
_SwRadiusAcctClientPacketsDropped_Type=Counter32
_SwRadiusAcctClientPacketsDropped_Object=MibTableColumn
swRadiusAcctClientPacketsDropped=_SwRadiusAcctClientPacketsDropped_Object((1,3,6,1,4,1,171,12,3,5,3,1,13),_SwRadiusAcctClientPacketsDropped_Type())
swRadiusAcctClientPacketsDropped.setMaxAccess(_A)
if mibBuilder.loadTexts:swRadiusAcctClientPacketsDropped.setStatus(_C)
_SwMacAuthBaseStatsInfo_ObjectIdentity=ObjectIdentity
swMacAuthBaseStatsInfo=_SwMacAuthBaseStatsInfo_ObjectIdentity((1,3,6,1,4,1,171,12,3,6))
_SwMacAuthStateTable_Object=MibTable
swMacAuthStateTable=_SwMacAuthStateTable_Object((1,3,6,1,4,1,171,12,3,6,1))
if mibBuilder.loadTexts:swMacAuthStateTable.setStatus(_B)
_SwMacAuthStateEntry_Object=MibTableRow
swMacAuthStateEntry=_SwMacAuthStateEntry_Object((1,3,6,1,4,1,171,12,3,6,1,1))
swMacAuthStateEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:swMacAuthStateEntry.setStatus(_B)
_SwPaeMacAddr_Type=MacAddress
_SwPaeMacAddr_Object=MibTableColumn
swPaeMacAddr=_SwPaeMacAddr_Object((1,3,6,1,4,1,171,12,3,6,1,1,1),_SwPaeMacAddr_Type())
swPaeMacAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:swPaeMacAddr.setStatus(_B)
_SwPaePortNumber_Type=InterfaceIndex
_SwPaePortNumber_Object=MibTableColumn
swPaePortNumber=_SwPaePortNumber_Object((1,3,6,1,4,1,171,12,3,6,1,1,2),_SwPaePortNumber_Type())
swPaePortNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:swPaePortNumber.setStatus(_B)
class _SwAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_O,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_SwAuthPaeState_Type.__name__=_E
_SwAuthPaeState_Object=MibTableColumn
swAuthPaeState=_SwAuthPaeState_Object((1,3,6,1,4,1,171,12,3,6,1,1,3),_SwAuthPaeState_Type())
swAuthPaeState.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthPaeState.setStatus(_B)
class _SwAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_O,7)))
_SwAuthBackendAuthState_Type.__name__=_E
_SwAuthBackendAuthState_Object=MibTableColumn
swAuthBackendAuthState=_SwAuthBackendAuthState_Object((1,3,6,1,4,1,171,12,3,6,1,1,4),_SwAuthBackendAuthState_Type())
swAuthBackendAuthState.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendAuthState.setStatus(_B)
_SwAuthAuthControlledPortStatus_Type=PaeControlledPortStatus
_SwAuthAuthControlledPortStatus_Object=MibTableColumn
swAuthAuthControlledPortStatus=_SwAuthAuthControlledPortStatus_Object((1,3,6,1,4,1,171,12,3,6,1,1,5),_SwAuthAuthControlledPortStatus_Type())
swAuthAuthControlledPortStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthControlledPortStatus.setStatus(_B)
_SwMacAuthStatsTable_Object=MibTable
swMacAuthStatsTable=_SwMacAuthStatsTable_Object((1,3,6,1,4,1,171,12,3,6,2))
if mibBuilder.loadTexts:swMacAuthStatsTable.setStatus(_B)
_SwMacAuthStatsEntry_Object=MibTableRow
swMacAuthStatsEntry=_SwMacAuthStatsEntry_Object((1,3,6,1,4,1,171,12,3,6,2,1))
swMacAuthStatsEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:swMacAuthStatsEntry.setStatus(_B)
_SwAuthEapolFramesRx_Type=Counter32
_SwAuthEapolFramesRx_Object=MibTableColumn
swAuthEapolFramesRx=_SwAuthEapolFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,1),_SwAuthEapolFramesRx_Type())
swAuthEapolFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolFramesRx.setStatus(_B)
_SwAuthEapolFramesTx_Type=Counter32
_SwAuthEapolFramesTx_Object=MibTableColumn
swAuthEapolFramesTx=_SwAuthEapolFramesTx_Object((1,3,6,1,4,1,171,12,3,6,2,1,2),_SwAuthEapolFramesTx_Type())
swAuthEapolFramesTx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolFramesTx.setStatus(_B)
_SwAuthEapolStartFramesRx_Type=Counter32
_SwAuthEapolStartFramesRx_Object=MibTableColumn
swAuthEapolStartFramesRx=_SwAuthEapolStartFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,3),_SwAuthEapolStartFramesRx_Type())
swAuthEapolStartFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolStartFramesRx.setStatus(_B)
_SwAuthEapolLogoffFramesRx_Type=Counter32
_SwAuthEapolLogoffFramesRx_Object=MibTableColumn
swAuthEapolLogoffFramesRx=_SwAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,4),_SwAuthEapolLogoffFramesRx_Type())
swAuthEapolLogoffFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolLogoffFramesRx.setStatus(_B)
_SwAuthEapolRespIdFramesRx_Type=Counter32
_SwAuthEapolRespIdFramesRx_Object=MibTableColumn
swAuthEapolRespIdFramesRx=_SwAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,5),_SwAuthEapolRespIdFramesRx_Type())
swAuthEapolRespIdFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolRespIdFramesRx.setStatus(_B)
_SwAuthEapolRespFramesRx_Type=Counter32
_SwAuthEapolRespFramesRx_Object=MibTableColumn
swAuthEapolRespFramesRx=_SwAuthEapolRespFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,6),_SwAuthEapolRespFramesRx_Type())
swAuthEapolRespFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolRespFramesRx.setStatus(_B)
_SwAuthEapolReqIdFramesTx_Type=Counter32
_SwAuthEapolReqIdFramesTx_Object=MibTableColumn
swAuthEapolReqIdFramesTx=_SwAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,171,12,3,6,2,1,7),_SwAuthEapolReqIdFramesTx_Type())
swAuthEapolReqIdFramesTx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolReqIdFramesTx.setStatus(_B)
_SwAuthEapolReqFramesTx_Type=Counter32
_SwAuthEapolReqFramesTx_Object=MibTableColumn
swAuthEapolReqFramesTx=_SwAuthEapolReqFramesTx_Object((1,3,6,1,4,1,171,12,3,6,2,1,8),_SwAuthEapolReqFramesTx_Type())
swAuthEapolReqFramesTx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapolReqFramesTx.setStatus(_B)
_SwAuthInvalidEapolFramesRx_Type=Counter32
_SwAuthInvalidEapolFramesRx_Object=MibTableColumn
swAuthInvalidEapolFramesRx=_SwAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,9),_SwAuthInvalidEapolFramesRx_Type())
swAuthInvalidEapolFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthInvalidEapolFramesRx.setStatus(_B)
_SwAuthEapLengthErrorFramesRx_Type=Counter32
_SwAuthEapLengthErrorFramesRx_Object=MibTableColumn
swAuthEapLengthErrorFramesRx=_SwAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,171,12,3,6,2,1,10),_SwAuthEapLengthErrorFramesRx_Type())
swAuthEapLengthErrorFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapLengthErrorFramesRx.setStatus(_B)
_SwAuthLastEapolFrameVersion_Type=Unsigned32
_SwAuthLastEapolFrameVersion_Object=MibTableColumn
swAuthLastEapolFrameVersion=_SwAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,171,12,3,6,2,1,11),_SwAuthLastEapolFrameVersion_Type())
swAuthLastEapolFrameVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthLastEapolFrameVersion.setStatus(_B)
_SwAuthLastEapolFrameSource_Type=MacAddress
_SwAuthLastEapolFrameSource_Object=MibTableColumn
swAuthLastEapolFrameSource=_SwAuthLastEapolFrameSource_Object((1,3,6,1,4,1,171,12,3,6,2,1,12),_SwAuthLastEapolFrameSource_Type())
swAuthLastEapolFrameSource.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthLastEapolFrameSource.setStatus(_B)
_SwMacAuthDiagTable_Object=MibTable
swMacAuthDiagTable=_SwMacAuthDiagTable_Object((1,3,6,1,4,1,171,12,3,6,3))
if mibBuilder.loadTexts:swMacAuthDiagTable.setStatus(_B)
_SwMacAuthDiagEntry_Object=MibTableRow
swMacAuthDiagEntry=_SwMacAuthDiagEntry_Object((1,3,6,1,4,1,171,12,3,6,3,1))
swMacAuthDiagEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:swMacAuthDiagEntry.setStatus(_B)
_SwAuthEntersConnecting_Type=Counter32
_SwAuthEntersConnecting_Object=MibTableColumn
swAuthEntersConnecting=_SwAuthEntersConnecting_Object((1,3,6,1,4,1,171,12,3,6,3,1,1),_SwAuthEntersConnecting_Type())
swAuthEntersConnecting.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEntersConnecting.setStatus(_B)
_SwAuthEapLogoffsWhileConnecting_Type=Counter32
_SwAuthEapLogoffsWhileConnecting_Object=MibTableColumn
swAuthEapLogoffsWhileConnecting=_SwAuthEapLogoffsWhileConnecting_Object((1,3,6,1,4,1,171,12,3,6,3,1,2),_SwAuthEapLogoffsWhileConnecting_Type())
swAuthEapLogoffsWhileConnecting.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEapLogoffsWhileConnecting.setStatus(_B)
_SwAuthEntersAuthenticating_Type=Counter32
_SwAuthEntersAuthenticating_Object=MibTableColumn
swAuthEntersAuthenticating=_SwAuthEntersAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,3),_SwAuthEntersAuthenticating_Type())
swAuthEntersAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthEntersAuthenticating.setStatus(_B)
_SwAuthAuthSuccessWhileAuthenticating_Type=Counter32
_SwAuthAuthSuccessWhileAuthenticating_Object=MibTableColumn
swAuthAuthSuccessWhileAuthenticating=_SwAuthAuthSuccessWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,4),_SwAuthAuthSuccessWhileAuthenticating_Type())
swAuthAuthSuccessWhileAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthSuccessWhileAuthenticating.setStatus(_B)
_SwAuthAuthTimeoutsWhileAuthenticating_Type=Counter32
_SwAuthAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
swAuthAuthTimeoutsWhileAuthenticating=_SwAuthAuthTimeoutsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,5),_SwAuthAuthTimeoutsWhileAuthenticating_Type())
swAuthAuthTimeoutsWhileAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthTimeoutsWhileAuthenticating.setStatus(_B)
_SwAuthAuthFailWhileAuthenticating_Type=Counter32
_SwAuthAuthFailWhileAuthenticating_Object=MibTableColumn
swAuthAuthFailWhileAuthenticating=_SwAuthAuthFailWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,6),_SwAuthAuthFailWhileAuthenticating_Type())
swAuthAuthFailWhileAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthFailWhileAuthenticating.setStatus(_B)
_SwAuthAuthReauthsWhileAuthenticating_Type=Counter32
_SwAuthAuthReauthsWhileAuthenticating_Object=MibTableColumn
swAuthAuthReauthsWhileAuthenticating=_SwAuthAuthReauthsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,7),_SwAuthAuthReauthsWhileAuthenticating_Type())
swAuthAuthReauthsWhileAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthReauthsWhileAuthenticating.setStatus(_B)
_SwAuthAuthEapStartsWhileAuthenticating_Type=Counter32
_SwAuthAuthEapStartsWhileAuthenticating_Object=MibTableColumn
swAuthAuthEapStartsWhileAuthenticating=_SwAuthAuthEapStartsWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,8),_SwAuthAuthEapStartsWhileAuthenticating_Type())
swAuthAuthEapStartsWhileAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthEapStartsWhileAuthenticating.setStatus(_B)
_SwAuthAuthEapLogoffWhileAuthenticating_Type=Counter32
_SwAuthAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
swAuthAuthEapLogoffWhileAuthenticating=_SwAuthAuthEapLogoffWhileAuthenticating_Object((1,3,6,1,4,1,171,12,3,6,3,1,9),_SwAuthAuthEapLogoffWhileAuthenticating_Type())
swAuthAuthEapLogoffWhileAuthenticating.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthEapLogoffWhileAuthenticating.setStatus(_B)
_SwAuthAuthReauthsWhileAuthenticated_Type=Counter32
_SwAuthAuthReauthsWhileAuthenticated_Object=MibTableColumn
swAuthAuthReauthsWhileAuthenticated=_SwAuthAuthReauthsWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,3,1,10),_SwAuthAuthReauthsWhileAuthenticated_Type())
swAuthAuthReauthsWhileAuthenticated.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthReauthsWhileAuthenticated.setStatus(_B)
_SwAuthAuthEapStartsWhileAuthenticated_Type=Counter32
_SwAuthAuthEapStartsWhileAuthenticated_Object=MibTableColumn
swAuthAuthEapStartsWhileAuthenticated=_SwAuthAuthEapStartsWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,3,1,11),_SwAuthAuthEapStartsWhileAuthenticated_Type())
swAuthAuthEapStartsWhileAuthenticated.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthEapStartsWhileAuthenticated.setStatus(_B)
_SwAuthAuthEapLogoffWhileAuthenticated_Type=Counter32
_SwAuthAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
swAuthAuthEapLogoffWhileAuthenticated=_SwAuthAuthEapLogoffWhileAuthenticated_Object((1,3,6,1,4,1,171,12,3,6,3,1,12),_SwAuthAuthEapLogoffWhileAuthenticated_Type())
swAuthAuthEapLogoffWhileAuthenticated.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthAuthEapLogoffWhileAuthenticated.setStatus(_B)
_SwAuthBackendResponses_Type=Counter32
_SwAuthBackendResponses_Object=MibTableColumn
swAuthBackendResponses=_SwAuthBackendResponses_Object((1,3,6,1,4,1,171,12,3,6,3,1,13),_SwAuthBackendResponses_Type())
swAuthBackendResponses.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendResponses.setStatus(_B)
_SwAuthBackendAccessChallenges_Type=Counter32
_SwAuthBackendAccessChallenges_Object=MibTableColumn
swAuthBackendAccessChallenges=_SwAuthBackendAccessChallenges_Object((1,3,6,1,4,1,171,12,3,6,3,1,14),_SwAuthBackendAccessChallenges_Type())
swAuthBackendAccessChallenges.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendAccessChallenges.setStatus(_B)
_SwAuthBackendOtherRequestsToSupplicant_Type=Counter32
_SwAuthBackendOtherRequestsToSupplicant_Object=MibTableColumn
swAuthBackendOtherRequestsToSupplicant=_SwAuthBackendOtherRequestsToSupplicant_Object((1,3,6,1,4,1,171,12,3,6,3,1,15),_SwAuthBackendOtherRequestsToSupplicant_Type())
swAuthBackendOtherRequestsToSupplicant.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendOtherRequestsToSupplicant.setStatus(_B)
_SwAuthBackendNonNakResponsesFromSupplicant_Type=Counter32
_SwAuthBackendNonNakResponsesFromSupplicant_Object=MibTableColumn
swAuthBackendNonNakResponsesFromSupplicant=_SwAuthBackendNonNakResponsesFromSupplicant_Object((1,3,6,1,4,1,171,12,3,6,3,1,16),_SwAuthBackendNonNakResponsesFromSupplicant_Type())
swAuthBackendNonNakResponsesFromSupplicant.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendNonNakResponsesFromSupplicant.setStatus(_B)
_SwAuthBackendAuthSuccesses_Type=Counter32
_SwAuthBackendAuthSuccesses_Object=MibTableColumn
swAuthBackendAuthSuccesses=_SwAuthBackendAuthSuccesses_Object((1,3,6,1,4,1,171,12,3,6,3,1,17),_SwAuthBackendAuthSuccesses_Type())
swAuthBackendAuthSuccesses.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendAuthSuccesses.setStatus(_B)
_SwAuthBackendAuthFails_Type=Counter32
_SwAuthBackendAuthFails_Object=MibTableColumn
swAuthBackendAuthFails=_SwAuthBackendAuthFails_Object((1,3,6,1,4,1,171,12,3,6,3,1,18),_SwAuthBackendAuthFails_Type())
swAuthBackendAuthFails.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthBackendAuthFails.setStatus(_B)
_SwMacAuthSessionStatsTable_Object=MibTable
swMacAuthSessionStatsTable=_SwMacAuthSessionStatsTable_Object((1,3,6,1,4,1,171,12,3,6,4))
if mibBuilder.loadTexts:swMacAuthSessionStatsTable.setStatus(_B)
_SwMacAuthSessionStatsEntry_Object=MibTableRow
swMacAuthSessionStatsEntry=_SwMacAuthSessionStatsEntry_Object((1,3,6,1,4,1,171,12,3,6,4,1))
swMacAuthSessionStatsEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:swMacAuthSessionStatsEntry.setStatus(_B)
_SwAuthSessionOctetsRx_Type=Counter64
_SwAuthSessionOctetsRx_Object=MibTableColumn
swAuthSessionOctetsRx=_SwAuthSessionOctetsRx_Object((1,3,6,1,4,1,171,12,3,6,4,1,1),_SwAuthSessionOctetsRx_Type())
swAuthSessionOctetsRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionOctetsRx.setStatus(_B)
_SwAuthSessionOctetsTx_Type=Counter64
_SwAuthSessionOctetsTx_Object=MibTableColumn
swAuthSessionOctetsTx=_SwAuthSessionOctetsTx_Object((1,3,6,1,4,1,171,12,3,6,4,1,2),_SwAuthSessionOctetsTx_Type())
swAuthSessionOctetsTx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionOctetsTx.setStatus(_B)
_SwAuthSessionFramesRx_Type=Counter32
_SwAuthSessionFramesRx_Object=MibTableColumn
swAuthSessionFramesRx=_SwAuthSessionFramesRx_Object((1,3,6,1,4,1,171,12,3,6,4,1,3),_SwAuthSessionFramesRx_Type())
swAuthSessionFramesRx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionFramesRx.setStatus(_B)
_SwAuthSessionFramesTx_Type=Counter32
_SwAuthSessionFramesTx_Object=MibTableColumn
swAuthSessionFramesTx=_SwAuthSessionFramesTx_Object((1,3,6,1,4,1,171,12,3,6,4,1,4),_SwAuthSessionFramesTx_Type())
swAuthSessionFramesTx.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionFramesTx.setStatus(_B)
_SwAuthSessionId_Type=SnmpAdminString
_SwAuthSessionId_Object=MibTableColumn
swAuthSessionId=_SwAuthSessionId_Object((1,3,6,1,4,1,171,12,3,6,4,1,5),_SwAuthSessionId_Type())
swAuthSessionId.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionId.setStatus(_B)
class _SwAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remoteAuthServer',1),('localAuthServer',2)))
_SwAuthSessionAuthenticMethod_Type.__name__=_E
_SwAuthSessionAuthenticMethod_Object=MibTableColumn
swAuthSessionAuthenticMethod=_SwAuthSessionAuthenticMethod_Object((1,3,6,1,4,1,171,12,3,6,4,1,6),_SwAuthSessionAuthenticMethod_Type())
swAuthSessionAuthenticMethod.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionAuthenticMethod.setStatus(_B)
_SwAuthSessionTime_Type=TimeTicks
_SwAuthSessionTime_Object=MibTableColumn
swAuthSessionTime=_SwAuthSessionTime_Object((1,3,6,1,4,1,171,12,3,6,4,1,7),_SwAuthSessionTime_Type())
swAuthSessionTime.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionTime.setStatus(_B)
class _SwAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_SwAuthSessionTerminateCause_Type.__name__=_E
_SwAuthSessionTerminateCause_Object=MibTableColumn
swAuthSessionTerminateCause=_SwAuthSessionTerminateCause_Object((1,3,6,1,4,1,171,12,3,6,4,1,8),_SwAuthSessionTerminateCause_Type())
swAuthSessionTerminateCause.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionTerminateCause.setStatus(_B)
_SwAuthSessionUserName_Type=SnmpAdminString
_SwAuthSessionUserName_Object=MibTableColumn
swAuthSessionUserName=_SwAuthSessionUserName_Object((1,3,6,1,4,1,171,12,3,6,4,1,9),_SwAuthSessionUserName_Type())
swAuthSessionUserName.setMaxAccess(_A)
if mibBuilder.loadTexts:swAuthSessionUserName.setStatus(_B)
_SwRadiusCommand_ObjectIdentity=ObjectIdentity
swRadiusCommand=_SwRadiusCommand_ObjectIdentity((1,3,6,1,4,1,171,12,3,7))
_SwRadiusForceDownPortNumber_Type=Unsigned32
_SwRadiusForceDownPortNumber_Object=MibScalar
swRadiusForceDownPortNumber=_SwRadiusForceDownPortNumber_Object((1,3,6,1,4,1,171,12,3,7,1),_SwRadiusForceDownPortNumber_Type())
swRadiusForceDownPortNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:swRadiusForceDownPortNumber.setStatus(_B)
_SwRadiusForceDownMacAddr_Type=MacAddress
_SwRadiusForceDownMacAddr_Object=MibScalar
swRadiusForceDownMacAddr=_SwRadiusForceDownMacAddr_Object((1,3,6,1,4,1,171,12,3,7,2),_SwRadiusForceDownMacAddr_Type())
swRadiusForceDownMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:swRadiusForceDownMacAddr.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'swDlinkAuthCtrl':swDlinkAuthCtrl,'swAuthCtrl':swAuthCtrl,'authProtocol':authProtocol,'swAuthMode':swAuthMode,'swFakeAuthentication':swFakeAuthentication,'swRadiusCtrl':swRadiusCtrl,'swRadiusServerTable':swRadiusServerTable,'swRadiusServerEntry':swRadiusServerEntry,_K:swRadiusServerIndex,'swRadiusServerIpAddr':swRadiusServerIpAddr,'swRadiusServerKey':swRadiusServerKey,'swRadiusAuthPortNumber':swRadiusAuthPortNumber,'swRadiusAcctPortNumber':swRadiusAcctPortNumber,'swRadiusServerStatus':swRadiusServerStatus,'swRadiusAuthInfo':swRadiusAuthInfo,'swRadiusAuthClientIdentifier':swRadiusAuthClientIdentifier,'swRadiusAuthClientInvalidServerAddresses':swRadiusAuthClientInvalidServerAddresses,'swRadiusAuthServerTable':swRadiusAuthServerTable,'swRadiusAuthServerEntry':swRadiusAuthServerEntry,_L:swRadiusAuthServerIndex,'swRadiusAuthServerAddress':swRadiusAuthServerAddress,'swRadiusAuthClientServerPortNumber':swRadiusAuthClientServerPortNumber,'swRadiusAuthClientRoundTripTime':swRadiusAuthClientRoundTripTime,'swRadiusAuthClientAccessRequests':swRadiusAuthClientAccessRequests,'swRadiusAuthClientAccessRetransmissions':swRadiusAuthClientAccessRetransmissions,'swRadiusAuthClientAccessAccepts':swRadiusAuthClientAccessAccepts,'swRadiusAuthClientAccessRejects':swRadiusAuthClientAccessRejects,'swRadiusAuthClientAccessChallenges':swRadiusAuthClientAccessChallenges,'swRadiusAuthClientMalformedAccessResponses':swRadiusAuthClientMalformedAccessResponses,'swRadiusAuthClientBadAuthenticators':swRadiusAuthClientBadAuthenticators,'swRadiusAuthClientPendingRequests':swRadiusAuthClientPendingRequests,'swRadiusAuthClientTimeouts':swRadiusAuthClientTimeouts,'swRadiusAuthClientUnknownTypes':swRadiusAuthClientUnknownTypes,'swRadiusAuthClientPacketsDropped':swRadiusAuthClientPacketsDropped,'swRadiusAccountingCtrl':swRadiusAccountingCtrl,'swRadiusAcctUpdateInterval':swRadiusAcctUpdateInterval,'swRadiusAcctSuppressNullUserName':swRadiusAcctSuppressNullUserName,'swRadiusAcctServiceTable':swRadiusAcctServiceTable,'swRadiusAcctServiceEntry':swRadiusAcctServiceEntry,_M:swRadiusAcctServiceIndex,'swRadiusAcctServiceMethod':swRadiusAcctServiceMethod,'swRadiusAcctServiceMode':swRadiusAcctServiceMode,'swRadiusAccountingInfo':swRadiusAccountingInfo,'swRadiusAcctClientIdentifier':swRadiusAcctClientIdentifier,'swRadiusAcctClientInvalidServerAddresses':swRadiusAcctClientInvalidServerAddresses,'swRadiusAcctServerTable':swRadiusAcctServerTable,'swRadiusAcctServerEntry':swRadiusAcctServerEntry,_N:swRadiusAcctServerIndex,'swRadiusAcctServerAddress':swRadiusAcctServerAddress,'swRadiusAcctClientServerPortNumber':swRadiusAcctClientServerPortNumber,'swRadiusAcctClientRoundTripTime':swRadiusAcctClientRoundTripTime,'swRadiusAcctClientRequests':swRadiusAcctClientRequests,'swRadiusAcctClientRetransmissions':swRadiusAcctClientRetransmissions,'swRadiusAcctClientResponses':swRadiusAcctClientResponses,'swRadiusAcctClientMalformedResponses':swRadiusAcctClientMalformedResponses,'swRadiusAcctClientBadAuthenticators':swRadiusAcctClientBadAuthenticators,'swRadiusAcctClientPendingRequests':swRadiusAcctClientPendingRequests,'swRadiusAcctClientTimeouts':swRadiusAcctClientTimeouts,'swRadiusAcctClientUnknownTypes':swRadiusAcctClientUnknownTypes,'swRadiusAcctClientPacketsDropped':swRadiusAcctClientPacketsDropped,'swMacAuthBaseStatsInfo':swMacAuthBaseStatsInfo,'swMacAuthStateTable':swMacAuthStateTable,'swMacAuthStateEntry':swMacAuthStateEntry,_H:swPaeMacAddr,_I:swPaePortNumber,'swAuthPaeState':swAuthPaeState,'swAuthBackendAuthState':swAuthBackendAuthState,'swAuthAuthControlledPortStatus':swAuthAuthControlledPortStatus,'swMacAuthStatsTable':swMacAuthStatsTable,'swMacAuthStatsEntry':swMacAuthStatsEntry,'swAuthEapolFramesRx':swAuthEapolFramesRx,'swAuthEapolFramesTx':swAuthEapolFramesTx,'swAuthEapolStartFramesRx':swAuthEapolStartFramesRx,'swAuthEapolLogoffFramesRx':swAuthEapolLogoffFramesRx,'swAuthEapolRespIdFramesRx':swAuthEapolRespIdFramesRx,'swAuthEapolRespFramesRx':swAuthEapolRespFramesRx,'swAuthEapolReqIdFramesTx':swAuthEapolReqIdFramesTx,'swAuthEapolReqFramesTx':swAuthEapolReqFramesTx,'swAuthInvalidEapolFramesRx':swAuthInvalidEapolFramesRx,'swAuthEapLengthErrorFramesRx':swAuthEapLengthErrorFramesRx,'swAuthLastEapolFrameVersion':swAuthLastEapolFrameVersion,'swAuthLastEapolFrameSource':swAuthLastEapolFrameSource,'swMacAuthDiagTable':swMacAuthDiagTable,'swMacAuthDiagEntry':swMacAuthDiagEntry,'swAuthEntersConnecting':swAuthEntersConnecting,'swAuthEapLogoffsWhileConnecting':swAuthEapLogoffsWhileConnecting,'swAuthEntersAuthenticating':swAuthEntersAuthenticating,'swAuthAuthSuccessWhileAuthenticating':swAuthAuthSuccessWhileAuthenticating,'swAuthAuthTimeoutsWhileAuthenticating':swAuthAuthTimeoutsWhileAuthenticating,'swAuthAuthFailWhileAuthenticating':swAuthAuthFailWhileAuthenticating,'swAuthAuthReauthsWhileAuthenticating':swAuthAuthReauthsWhileAuthenticating,'swAuthAuthEapStartsWhileAuthenticating':swAuthAuthEapStartsWhileAuthenticating,'swAuthAuthEapLogoffWhileAuthenticating':swAuthAuthEapLogoffWhileAuthenticating,'swAuthAuthReauthsWhileAuthenticated':swAuthAuthReauthsWhileAuthenticated,'swAuthAuthEapStartsWhileAuthenticated':swAuthAuthEapStartsWhileAuthenticated,'swAuthAuthEapLogoffWhileAuthenticated':swAuthAuthEapLogoffWhileAuthenticated,'swAuthBackendResponses':swAuthBackendResponses,'swAuthBackendAccessChallenges':swAuthBackendAccessChallenges,'swAuthBackendOtherRequestsToSupplicant':swAuthBackendOtherRequestsToSupplicant,'swAuthBackendNonNakResponsesFromSupplicant':swAuthBackendNonNakResponsesFromSupplicant,'swAuthBackendAuthSuccesses':swAuthBackendAuthSuccesses,'swAuthBackendAuthFails':swAuthBackendAuthFails,'swMacAuthSessionStatsTable':swMacAuthSessionStatsTable,'swMacAuthSessionStatsEntry':swMacAuthSessionStatsEntry,'swAuthSessionOctetsRx':swAuthSessionOctetsRx,'swAuthSessionOctetsTx':swAuthSessionOctetsTx,'swAuthSessionFramesRx':swAuthSessionFramesRx,'swAuthSessionFramesTx':swAuthSessionFramesTx,'swAuthSessionId':swAuthSessionId,'swAuthSessionAuthenticMethod':swAuthSessionAuthenticMethod,'swAuthSessionTime':swAuthSessionTime,'swAuthSessionTerminateCause':swAuthSessionTerminateCause,'swAuthSessionUserName':swAuthSessionUserName,'swRadiusCommand':swRadiusCommand,'swRadiusForceDownPortNumber':swRadiusForceDownPortNumber,'swRadiusForceDownMacAddr':swRadiusForceDownMacAddr})