_J='fsRadExtAccServerIndex'
_I='fsRadExtAuthServerIndex'
_H='fsRadExtServerIndex'
_G='InetAddress'
_F='not-accessible'
_E='SUPERMICRO-RADIUS-EXT-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futureRADIUSEXTMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,30))
if mibBuilder.loadTexts:futureRADIUSEXTMIB.setRevisions(('2012-09-05 00:00',))
_FsRadExtClient_ObjectIdentity=ObjectIdentity
fsRadExtClient=_FsRadExtClient_ObjectIdentity((1,3,6,1,4,1,10876,101,2,30,1))
_FsRadExtServer_ObjectIdentity=ObjectIdentity
fsRadExtServer=_FsRadExtServer_ObjectIdentity((1,3,6,1,4,1,10876,101,2,30,1,1))
_FsRadExtDebugMask_Type=Integer32
_FsRadExtDebugMask_Object=MibScalar
fsRadExtDebugMask=_FsRadExtDebugMask_Object((1,3,6,1,4,1,10876,101,2,30,1,1,1),_FsRadExtDebugMask_Type())
fsRadExtDebugMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtDebugMask.setStatus(_A)
class _FsRadExtMaxNoOfUserEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsRadExtMaxNoOfUserEntries_Type.__name__=_D
_FsRadExtMaxNoOfUserEntries_Object=MibScalar
fsRadExtMaxNoOfUserEntries=_FsRadExtMaxNoOfUserEntries_Object((1,3,6,1,4,1,10876,101,2,30,1,1,2),_FsRadExtMaxNoOfUserEntries_Type())
fsRadExtMaxNoOfUserEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtMaxNoOfUserEntries.setStatus(_A)
_FsRadExtPrimaryServerAddressType_Type=InetAddressType
_FsRadExtPrimaryServerAddressType_Object=MibScalar
fsRadExtPrimaryServerAddressType=_FsRadExtPrimaryServerAddressType_Object((1,3,6,1,4,1,10876,101,2,30,1,1,3),_FsRadExtPrimaryServerAddressType_Type())
fsRadExtPrimaryServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtPrimaryServerAddressType.setStatus(_A)
class _FsRadExtPrimaryServer_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsRadExtPrimaryServer_Type.__name__=_G
_FsRadExtPrimaryServer_Object=MibScalar
fsRadExtPrimaryServer=_FsRadExtPrimaryServer_Object((1,3,6,1,4,1,10876,101,2,30,1,1,4),_FsRadExtPrimaryServer_Type())
fsRadExtPrimaryServer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtPrimaryServer.setStatus(_A)
_FsRadExtServerTable_Object=MibTable
fsRadExtServerTable=_FsRadExtServerTable_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5))
if mibBuilder.loadTexts:fsRadExtServerTable.setStatus(_A)
_FsRadExtServerEntry_Object=MibTableRow
fsRadExtServerEntry=_FsRadExtServerEntry_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1))
fsRadExtServerEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:fsRadExtServerEntry.setStatus(_A)
class _FsRadExtServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FsRadExtServerIndex_Type.__name__=_D
_FsRadExtServerIndex_Object=MibTableColumn
fsRadExtServerIndex=_FsRadExtServerIndex_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,1),_FsRadExtServerIndex_Type())
fsRadExtServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRadExtServerIndex.setStatus(_A)
_FsRadExtServerAddrType_Type=InetAddressType
_FsRadExtServerAddrType_Object=MibTableColumn
fsRadExtServerAddrType=_FsRadExtServerAddrType_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,2),_FsRadExtServerAddrType_Type())
fsRadExtServerAddrType.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsRadExtServerAddrType.setStatus(_A)
_FsRadExtServerAddress_Type=InetAddress
_FsRadExtServerAddress_Object=MibTableColumn
fsRadExtServerAddress=_FsRadExtServerAddress_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,3),_FsRadExtServerAddress_Type())
fsRadExtServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerAddress.setStatus(_A)
class _FsRadExtServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auth',1),('acct',2),('both',3)))
_FsRadExtServerType_Type.__name__=_D
_FsRadExtServerType_Object=MibTableColumn
fsRadExtServerType=_FsRadExtServerType_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,4),_FsRadExtServerType_Type())
fsRadExtServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerType.setStatus(_A)
_FsRadExtServerSharedSecret_Type=DisplayString
_FsRadExtServerSharedSecret_Object=MibTableColumn
fsRadExtServerSharedSecret=_FsRadExtServerSharedSecret_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,5),_FsRadExtServerSharedSecret_Type())
fsRadExtServerSharedSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerSharedSecret.setStatus(_A)
class _FsRadExtServerEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('destroy',3)))
_FsRadExtServerEnabled_Type.__name__=_D
_FsRadExtServerEnabled_Object=MibTableColumn
fsRadExtServerEnabled=_FsRadExtServerEnabled_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,6),_FsRadExtServerEnabled_Type())
fsRadExtServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerEnabled.setStatus(_A)
class _FsRadExtServerResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_FsRadExtServerResponseTime_Type.__name__=_D
_FsRadExtServerResponseTime_Object=MibTableColumn
fsRadExtServerResponseTime=_FsRadExtServerResponseTime_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,7),_FsRadExtServerResponseTime_Type())
fsRadExtServerResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerResponseTime.setStatus(_A)
class _FsRadExtServerMaximumRetransmission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_FsRadExtServerMaximumRetransmission_Type.__name__=_D
_FsRadExtServerMaximumRetransmission_Object=MibTableColumn
fsRadExtServerMaximumRetransmission=_FsRadExtServerMaximumRetransmission_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,8),_FsRadExtServerMaximumRetransmission_Type())
fsRadExtServerMaximumRetransmission.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerMaximumRetransmission.setStatus(_A)
_FsRadExtServerEntryStatus_Type=RowStatus
_FsRadExtServerEntryStatus_Object=MibTableColumn
fsRadExtServerEntryStatus=_FsRadExtServerEntryStatus_Object((1,3,6,1,4,1,10876,101,2,30,1,1,5,1,9),_FsRadExtServerEntryStatus_Type())
fsRadExtServerEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtServerEntryStatus.setStatus(_A)
_FsRadAuthClient_ObjectIdentity=ObjectIdentity
fsRadAuthClient=_FsRadAuthClient_ObjectIdentity((1,3,6,1,4,1,10876,101,2,30,1,2))
_FsRadExtAuthClientInvalidServerAddresses_Type=Counter32
_FsRadExtAuthClientInvalidServerAddresses_Object=MibScalar
fsRadExtAuthClientInvalidServerAddresses=_FsRadExtAuthClientInvalidServerAddresses_Object((1,3,6,1,4,1,10876,101,2,30,1,2,1),_FsRadExtAuthClientInvalidServerAddresses_Type())
fsRadExtAuthClientInvalidServerAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientInvalidServerAddresses.setStatus(_A)
_FsRadExtAuthClientIdentifier_Type=SnmpAdminString
_FsRadExtAuthClientIdentifier_Object=MibScalar
fsRadExtAuthClientIdentifier=_FsRadExtAuthClientIdentifier_Object((1,3,6,1,4,1,10876,101,2,30,1,2,2),_FsRadExtAuthClientIdentifier_Type())
fsRadExtAuthClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientIdentifier.setStatus(_A)
_FsRadExtAuthServerTable_Object=MibTable
fsRadExtAuthServerTable=_FsRadExtAuthServerTable_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3))
if mibBuilder.loadTexts:fsRadExtAuthServerTable.setStatus(_A)
_FsRadExtAuthServerEntry_Object=MibTableRow
fsRadExtAuthServerEntry=_FsRadExtAuthServerEntry_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1))
fsRadExtAuthServerEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:fsRadExtAuthServerEntry.setStatus(_A)
class _FsRadExtAuthServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsRadExtAuthServerIndex_Type.__name__=_D
_FsRadExtAuthServerIndex_Object=MibTableColumn
fsRadExtAuthServerIndex=_FsRadExtAuthServerIndex_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,1),_FsRadExtAuthServerIndex_Type())
fsRadExtAuthServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRadExtAuthServerIndex.setStatus(_A)
_FsRadExtAuthServerAddressType_Type=InetAddressType
_FsRadExtAuthServerAddressType_Object=MibTableColumn
fsRadExtAuthServerAddressType=_FsRadExtAuthServerAddressType_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,2),_FsRadExtAuthServerAddressType_Type())
fsRadExtAuthServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthServerAddressType.setStatus(_A)
_FsRadExtAuthServerAddress_Type=InetAddress
_FsRadExtAuthServerAddress_Object=MibTableColumn
fsRadExtAuthServerAddress=_FsRadExtAuthServerAddress_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,3),_FsRadExtAuthServerAddress_Type())
fsRadExtAuthServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthServerAddress.setStatus(_A)
class _FsRadExtAuthClientServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsRadExtAuthClientServerPortNumber_Type.__name__=_D
_FsRadExtAuthClientServerPortNumber_Object=MibTableColumn
fsRadExtAuthClientServerPortNumber=_FsRadExtAuthClientServerPortNumber_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,4),_FsRadExtAuthClientServerPortNumber_Type())
fsRadExtAuthClientServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtAuthClientServerPortNumber.setStatus(_A)
_FsRadExtAuthClientRoundTripTime_Type=TimeTicks
_FsRadExtAuthClientRoundTripTime_Object=MibTableColumn
fsRadExtAuthClientRoundTripTime=_FsRadExtAuthClientRoundTripTime_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,5),_FsRadExtAuthClientRoundTripTime_Type())
fsRadExtAuthClientRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientRoundTripTime.setStatus(_A)
_FsRadExtAuthClientAccessRequests_Type=Counter32
_FsRadExtAuthClientAccessRequests_Object=MibTableColumn
fsRadExtAuthClientAccessRequests=_FsRadExtAuthClientAccessRequests_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,6),_FsRadExtAuthClientAccessRequests_Type())
fsRadExtAuthClientAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientAccessRequests.setStatus(_A)
_FsRadExtAuthClientAccessRetransmissions_Type=Counter32
_FsRadExtAuthClientAccessRetransmissions_Object=MibTableColumn
fsRadExtAuthClientAccessRetransmissions=_FsRadExtAuthClientAccessRetransmissions_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,7),_FsRadExtAuthClientAccessRetransmissions_Type())
fsRadExtAuthClientAccessRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientAccessRetransmissions.setStatus(_A)
_FsRadExtAuthClientAccessAccepts_Type=Counter32
_FsRadExtAuthClientAccessAccepts_Object=MibTableColumn
fsRadExtAuthClientAccessAccepts=_FsRadExtAuthClientAccessAccepts_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,8),_FsRadExtAuthClientAccessAccepts_Type())
fsRadExtAuthClientAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientAccessAccepts.setStatus(_A)
_FsRadExtAuthClientAccessRejects_Type=Counter32
_FsRadExtAuthClientAccessRejects_Object=MibTableColumn
fsRadExtAuthClientAccessRejects=_FsRadExtAuthClientAccessRejects_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,9),_FsRadExtAuthClientAccessRejects_Type())
fsRadExtAuthClientAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientAccessRejects.setStatus(_A)
_FsRadExtAuthClientAccessChallenges_Type=Counter32
_FsRadExtAuthClientAccessChallenges_Object=MibTableColumn
fsRadExtAuthClientAccessChallenges=_FsRadExtAuthClientAccessChallenges_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,10),_FsRadExtAuthClientAccessChallenges_Type())
fsRadExtAuthClientAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientAccessChallenges.setStatus(_A)
_FsRadExtAuthClientMalformedAccessResponses_Type=Counter32
_FsRadExtAuthClientMalformedAccessResponses_Object=MibTableColumn
fsRadExtAuthClientMalformedAccessResponses=_FsRadExtAuthClientMalformedAccessResponses_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,11),_FsRadExtAuthClientMalformedAccessResponses_Type())
fsRadExtAuthClientMalformedAccessResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientMalformedAccessResponses.setStatus(_A)
_FsRadExtAuthClientBadAuthenticators_Type=Counter32
_FsRadExtAuthClientBadAuthenticators_Object=MibTableColumn
fsRadExtAuthClientBadAuthenticators=_FsRadExtAuthClientBadAuthenticators_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,12),_FsRadExtAuthClientBadAuthenticators_Type())
fsRadExtAuthClientBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientBadAuthenticators.setStatus(_A)
_FsRadExtAuthClientPendingRequests_Type=Gauge32
_FsRadExtAuthClientPendingRequests_Object=MibTableColumn
fsRadExtAuthClientPendingRequests=_FsRadExtAuthClientPendingRequests_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,13),_FsRadExtAuthClientPendingRequests_Type())
fsRadExtAuthClientPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientPendingRequests.setStatus(_A)
_FsRadExtAuthClientTimeouts_Type=Counter32
_FsRadExtAuthClientTimeouts_Object=MibTableColumn
fsRadExtAuthClientTimeouts=_FsRadExtAuthClientTimeouts_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,14),_FsRadExtAuthClientTimeouts_Type())
fsRadExtAuthClientTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientTimeouts.setStatus(_A)
_FsRadExtAuthClientUnknownTypes_Type=Counter32
_FsRadExtAuthClientUnknownTypes_Object=MibTableColumn
fsRadExtAuthClientUnknownTypes=_FsRadExtAuthClientUnknownTypes_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,15),_FsRadExtAuthClientUnknownTypes_Type())
fsRadExtAuthClientUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientUnknownTypes.setStatus(_A)
_FsRadExtAuthClientPacketsDropped_Type=Counter32
_FsRadExtAuthClientPacketsDropped_Object=MibTableColumn
fsRadExtAuthClientPacketsDropped=_FsRadExtAuthClientPacketsDropped_Object((1,3,6,1,4,1,10876,101,2,30,1,2,3,1,16),_FsRadExtAuthClientPacketsDropped_Type())
fsRadExtAuthClientPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAuthClientPacketsDropped.setStatus(_A)
_FsRadAccClient_ObjectIdentity=ObjectIdentity
fsRadAccClient=_FsRadAccClient_ObjectIdentity((1,3,6,1,4,1,10876,101,2,30,1,3))
_FsRadExtAccClientInvalidServerAddresses_Type=Counter32
_FsRadExtAccClientInvalidServerAddresses_Object=MibScalar
fsRadExtAccClientInvalidServerAddresses=_FsRadExtAccClientInvalidServerAddresses_Object((1,3,6,1,4,1,10876,101,2,30,1,3,1),_FsRadExtAccClientInvalidServerAddresses_Type())
fsRadExtAccClientInvalidServerAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientInvalidServerAddresses.setStatus(_A)
_FsRadExtAccClientIdentifier_Type=SnmpAdminString
_FsRadExtAccClientIdentifier_Object=MibScalar
fsRadExtAccClientIdentifier=_FsRadExtAccClientIdentifier_Object((1,3,6,1,4,1,10876,101,2,30,1,3,2),_FsRadExtAccClientIdentifier_Type())
fsRadExtAccClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientIdentifier.setStatus(_A)
_FsRadExtAccServerTable_Object=MibTable
fsRadExtAccServerTable=_FsRadExtAccServerTable_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3))
if mibBuilder.loadTexts:fsRadExtAccServerTable.setStatus(_A)
_FsRadExtAccServerEntry_Object=MibTableRow
fsRadExtAccServerEntry=_FsRadExtAccServerEntry_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1))
fsRadExtAccServerEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:fsRadExtAccServerEntry.setStatus(_A)
class _FsRadExtAccServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsRadExtAccServerIndex_Type.__name__=_D
_FsRadExtAccServerIndex_Object=MibTableColumn
fsRadExtAccServerIndex=_FsRadExtAccServerIndex_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,1),_FsRadExtAccServerIndex_Type())
fsRadExtAccServerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRadExtAccServerIndex.setStatus(_A)
_FsRadExtAccServerAddressType_Type=InetAddressType
_FsRadExtAccServerAddressType_Object=MibTableColumn
fsRadExtAccServerAddressType=_FsRadExtAccServerAddressType_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,2),_FsRadExtAccServerAddressType_Type())
fsRadExtAccServerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccServerAddressType.setStatus(_A)
_FsRadExtAccServerAddress_Type=InetAddress
_FsRadExtAccServerAddress_Object=MibTableColumn
fsRadExtAccServerAddress=_FsRadExtAccServerAddress_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,3),_FsRadExtAccServerAddress_Type())
fsRadExtAccServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccServerAddress.setStatus(_A)
class _FsRadExtAccClientServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsRadExtAccClientServerPortNumber_Type.__name__=_D
_FsRadExtAccClientServerPortNumber_Object=MibTableColumn
fsRadExtAccClientServerPortNumber=_FsRadExtAccClientServerPortNumber_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,4),_FsRadExtAccClientServerPortNumber_Type())
fsRadExtAccClientServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsRadExtAccClientServerPortNumber.setStatus(_A)
_FsRadExtAccClientRoundTripTime_Type=TimeTicks
_FsRadExtAccClientRoundTripTime_Object=MibTableColumn
fsRadExtAccClientRoundTripTime=_FsRadExtAccClientRoundTripTime_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,5),_FsRadExtAccClientRoundTripTime_Type())
fsRadExtAccClientRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientRoundTripTime.setStatus(_A)
_FsRadExtAccClientRequests_Type=Counter32
_FsRadExtAccClientRequests_Object=MibTableColumn
fsRadExtAccClientRequests=_FsRadExtAccClientRequests_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,6),_FsRadExtAccClientRequests_Type())
fsRadExtAccClientRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientRequests.setStatus(_A)
_FsRadExtAccClientRetransmissions_Type=Counter32
_FsRadExtAccClientRetransmissions_Object=MibTableColumn
fsRadExtAccClientRetransmissions=_FsRadExtAccClientRetransmissions_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,7),_FsRadExtAccClientRetransmissions_Type())
fsRadExtAccClientRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientRetransmissions.setStatus(_A)
_FsRadExtAccClientResponses_Type=Counter32
_FsRadExtAccClientResponses_Object=MibTableColumn
fsRadExtAccClientResponses=_FsRadExtAccClientResponses_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,8),_FsRadExtAccClientResponses_Type())
fsRadExtAccClientResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientResponses.setStatus(_A)
_FsRadExtAccClientMalformedResponses_Type=Counter32
_FsRadExtAccClientMalformedResponses_Object=MibTableColumn
fsRadExtAccClientMalformedResponses=_FsRadExtAccClientMalformedResponses_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,9),_FsRadExtAccClientMalformedResponses_Type())
fsRadExtAccClientMalformedResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientMalformedResponses.setStatus(_A)
_FsRadExtAccClientBadAuthenticators_Type=Counter32
_FsRadExtAccClientBadAuthenticators_Object=MibTableColumn
fsRadExtAccClientBadAuthenticators=_FsRadExtAccClientBadAuthenticators_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,10),_FsRadExtAccClientBadAuthenticators_Type())
fsRadExtAccClientBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientBadAuthenticators.setStatus(_A)
_FsRadExtAccClientPendingRequests_Type=Gauge32
_FsRadExtAccClientPendingRequests_Object=MibTableColumn
fsRadExtAccClientPendingRequests=_FsRadExtAccClientPendingRequests_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,11),_FsRadExtAccClientPendingRequests_Type())
fsRadExtAccClientPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientPendingRequests.setStatus(_A)
_FsRadExtAccClientTimeouts_Type=Counter32
_FsRadExtAccClientTimeouts_Object=MibTableColumn
fsRadExtAccClientTimeouts=_FsRadExtAccClientTimeouts_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,12),_FsRadExtAccClientTimeouts_Type())
fsRadExtAccClientTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientTimeouts.setStatus(_A)
_FsRadExtAccClientUnknownTypes_Type=Counter32
_FsRadExtAccClientUnknownTypes_Object=MibTableColumn
fsRadExtAccClientUnknownTypes=_FsRadExtAccClientUnknownTypes_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,13),_FsRadExtAccClientUnknownTypes_Type())
fsRadExtAccClientUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientUnknownTypes.setStatus(_A)
_FsRadExtAccClientPacketsDropped_Type=Counter32
_FsRadExtAccClientPacketsDropped_Object=MibTableColumn
fsRadExtAccClientPacketsDropped=_FsRadExtAccClientPacketsDropped_Object((1,3,6,1,4,1,10876,101,2,30,1,3,3,1,14),_FsRadExtAccClientPacketsDropped_Type())
fsRadExtAccClientPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadExtAccClientPacketsDropped.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'futureRADIUSEXTMIB':futureRADIUSEXTMIB,'fsRadExtClient':fsRadExtClient,'fsRadExtServer':fsRadExtServer,'fsRadExtDebugMask':fsRadExtDebugMask,'fsRadExtMaxNoOfUserEntries':fsRadExtMaxNoOfUserEntries,'fsRadExtPrimaryServerAddressType':fsRadExtPrimaryServerAddressType,'fsRadExtPrimaryServer':fsRadExtPrimaryServer,'fsRadExtServerTable':fsRadExtServerTable,'fsRadExtServerEntry':fsRadExtServerEntry,_H:fsRadExtServerIndex,'fsRadExtServerAddrType':fsRadExtServerAddrType,'fsRadExtServerAddress':fsRadExtServerAddress,'fsRadExtServerType':fsRadExtServerType,'fsRadExtServerSharedSecret':fsRadExtServerSharedSecret,'fsRadExtServerEnabled':fsRadExtServerEnabled,'fsRadExtServerResponseTime':fsRadExtServerResponseTime,'fsRadExtServerMaximumRetransmission':fsRadExtServerMaximumRetransmission,'fsRadExtServerEntryStatus':fsRadExtServerEntryStatus,'fsRadAuthClient':fsRadAuthClient,'fsRadExtAuthClientInvalidServerAddresses':fsRadExtAuthClientInvalidServerAddresses,'fsRadExtAuthClientIdentifier':fsRadExtAuthClientIdentifier,'fsRadExtAuthServerTable':fsRadExtAuthServerTable,'fsRadExtAuthServerEntry':fsRadExtAuthServerEntry,_I:fsRadExtAuthServerIndex,'fsRadExtAuthServerAddressType':fsRadExtAuthServerAddressType,'fsRadExtAuthServerAddress':fsRadExtAuthServerAddress,'fsRadExtAuthClientServerPortNumber':fsRadExtAuthClientServerPortNumber,'fsRadExtAuthClientRoundTripTime':fsRadExtAuthClientRoundTripTime,'fsRadExtAuthClientAccessRequests':fsRadExtAuthClientAccessRequests,'fsRadExtAuthClientAccessRetransmissions':fsRadExtAuthClientAccessRetransmissions,'fsRadExtAuthClientAccessAccepts':fsRadExtAuthClientAccessAccepts,'fsRadExtAuthClientAccessRejects':fsRadExtAuthClientAccessRejects,'fsRadExtAuthClientAccessChallenges':fsRadExtAuthClientAccessChallenges,'fsRadExtAuthClientMalformedAccessResponses':fsRadExtAuthClientMalformedAccessResponses,'fsRadExtAuthClientBadAuthenticators':fsRadExtAuthClientBadAuthenticators,'fsRadExtAuthClientPendingRequests':fsRadExtAuthClientPendingRequests,'fsRadExtAuthClientTimeouts':fsRadExtAuthClientTimeouts,'fsRadExtAuthClientUnknownTypes':fsRadExtAuthClientUnknownTypes,'fsRadExtAuthClientPacketsDropped':fsRadExtAuthClientPacketsDropped,'fsRadAccClient':fsRadAccClient,'fsRadExtAccClientInvalidServerAddresses':fsRadExtAccClientInvalidServerAddresses,'fsRadExtAccClientIdentifier':fsRadExtAccClientIdentifier,'fsRadExtAccServerTable':fsRadExtAccServerTable,'fsRadExtAccServerEntry':fsRadExtAccServerEntry,_J:fsRadExtAccServerIndex,'fsRadExtAccServerAddressType':fsRadExtAccServerAddressType,'fsRadExtAccServerAddress':fsRadExtAccServerAddress,'fsRadExtAccClientServerPortNumber':fsRadExtAccClientServerPortNumber,'fsRadExtAccClientRoundTripTime':fsRadExtAccClientRoundTripTime,'fsRadExtAccClientRequests':fsRadExtAccClientRequests,'fsRadExtAccClientRetransmissions':fsRadExtAccClientRetransmissions,'fsRadExtAccClientResponses':fsRadExtAccClientResponses,'fsRadExtAccClientMalformedResponses':fsRadExtAccClientMalformedResponses,'fsRadExtAccClientBadAuthenticators':fsRadExtAccClientBadAuthenticators,'fsRadExtAccClientPendingRequests':fsRadExtAccClientPendingRequests,'fsRadExtAccClientTimeouts':fsRadExtAccClientTimeouts,'fsRadExtAccClientUnknownTypes':fsRadExtAccClientUnknownTypes,'fsRadExtAccClientPacketsDropped':fsRadExtAccClientPacketsDropped})