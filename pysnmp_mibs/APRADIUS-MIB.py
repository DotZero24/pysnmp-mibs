_R='apRadiusServerAccessChallenges'
_Q='apRadiusServerUnknownPDUTypes'
_P='apRadiusServerAccessRejects'
_O='apRadiusServerTimeouts'
_N='apRadiusServerAccessAccepts'
_M='apRadiusServerAccessRetransmissions'
_L='apRadiusServerBadAuthenticators'
_K='apRadiusServerDisconnectNACks'
_J='apRadiusServerDisconnectACKs'
_I='apRadiusServerDisconnectRequests'
_H='apRadiusServerAccessRequests'
_G='apRadiusServerMalformedAccessResponse'
_F='apRadiusServerRoundTripTime'
_E='apRadiusServerAddress'
_D='apRadiusServerAddressType'
_C='read-only'
_B='APRADIUS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
apRadiusServerModule=ModuleIdentity((1,3,6,1,4,1,9148,3,18))
_ApRadiusServerMIBObjects_ObjectIdentity=ObjectIdentity
apRadiusServerMIBObjects=_ApRadiusServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,18,1))
_ApRadiusServerStatsTable_Object=MibTable
apRadiusServerStatsTable=_ApRadiusServerStatsTable_Object((1,3,6,1,4,1,9148,3,18,1,1))
if mibBuilder.loadTexts:apRadiusServerStatsTable.setStatus(_A)
_ApRadiusServerStatsEntry_Object=MibTableRow
apRadiusServerStatsEntry=_ApRadiusServerStatsEntry_Object((1,3,6,1,4,1,9148,3,18,1,1,1))
apRadiusServerStatsEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:apRadiusServerStatsEntry.setStatus(_A)
_ApRadiusServerAddressType_Type=InetAddressType
_ApRadiusServerAddressType_Object=MibTableColumn
apRadiusServerAddressType=_ApRadiusServerAddressType_Object((1,3,6,1,4,1,9148,3,18,1,1,1,1),_ApRadiusServerAddressType_Type())
apRadiusServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAddressType.setStatus(_A)
_ApRadiusServerAddress_Type=InetAddress
_ApRadiusServerAddress_Object=MibTableColumn
apRadiusServerAddress=_ApRadiusServerAddress_Object((1,3,6,1,4,1,9148,3,18,1,1,1,2),_ApRadiusServerAddress_Type())
apRadiusServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAddress.setStatus(_A)
_ApRadiusServerRoundTripTime_Type=Unsigned32
_ApRadiusServerRoundTripTime_Object=MibTableColumn
apRadiusServerRoundTripTime=_ApRadiusServerRoundTripTime_Object((1,3,6,1,4,1,9148,3,18,1,1,1,3),_ApRadiusServerRoundTripTime_Type())
apRadiusServerRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerRoundTripTime.setStatus(_A)
_ApRadiusServerMalformedAccessResponse_Type=Unsigned32
_ApRadiusServerMalformedAccessResponse_Object=MibTableColumn
apRadiusServerMalformedAccessResponse=_ApRadiusServerMalformedAccessResponse_Object((1,3,6,1,4,1,9148,3,18,1,1,1,4),_ApRadiusServerMalformedAccessResponse_Type())
apRadiusServerMalformedAccessResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerMalformedAccessResponse.setStatus(_A)
_ApRadiusServerAccessRequests_Type=Unsigned32
_ApRadiusServerAccessRequests_Object=MibTableColumn
apRadiusServerAccessRequests=_ApRadiusServerAccessRequests_Object((1,3,6,1,4,1,9148,3,18,1,1,1,5),_ApRadiusServerAccessRequests_Type())
apRadiusServerAccessRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAccessRequests.setStatus(_A)
_ApRadiusServerDisconnectRequests_Type=Unsigned32
_ApRadiusServerDisconnectRequests_Object=MibTableColumn
apRadiusServerDisconnectRequests=_ApRadiusServerDisconnectRequests_Object((1,3,6,1,4,1,9148,3,18,1,1,1,6),_ApRadiusServerDisconnectRequests_Type())
apRadiusServerDisconnectRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerDisconnectRequests.setStatus(_A)
_ApRadiusServerDisconnectACKs_Type=Unsigned32
_ApRadiusServerDisconnectACKs_Object=MibTableColumn
apRadiusServerDisconnectACKs=_ApRadiusServerDisconnectACKs_Object((1,3,6,1,4,1,9148,3,18,1,1,1,7),_ApRadiusServerDisconnectACKs_Type())
apRadiusServerDisconnectACKs.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerDisconnectACKs.setStatus(_A)
_ApRadiusServerDisconnectNACks_Type=Unsigned32
_ApRadiusServerDisconnectNACks_Object=MibTableColumn
apRadiusServerDisconnectNACks=_ApRadiusServerDisconnectNACks_Object((1,3,6,1,4,1,9148,3,18,1,1,1,8),_ApRadiusServerDisconnectNACks_Type())
apRadiusServerDisconnectNACks.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerDisconnectNACks.setStatus(_A)
_ApRadiusServerBadAuthenticators_Type=Unsigned32
_ApRadiusServerBadAuthenticators_Object=MibTableColumn
apRadiusServerBadAuthenticators=_ApRadiusServerBadAuthenticators_Object((1,3,6,1,4,1,9148,3,18,1,1,1,9),_ApRadiusServerBadAuthenticators_Type())
apRadiusServerBadAuthenticators.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerBadAuthenticators.setStatus(_A)
_ApRadiusServerAccessRetransmissions_Type=Unsigned32
_ApRadiusServerAccessRetransmissions_Object=MibTableColumn
apRadiusServerAccessRetransmissions=_ApRadiusServerAccessRetransmissions_Object((1,3,6,1,4,1,9148,3,18,1,1,1,10),_ApRadiusServerAccessRetransmissions_Type())
apRadiusServerAccessRetransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAccessRetransmissions.setStatus(_A)
_ApRadiusServerAccessAccepts_Type=Unsigned32
_ApRadiusServerAccessAccepts_Object=MibTableColumn
apRadiusServerAccessAccepts=_ApRadiusServerAccessAccepts_Object((1,3,6,1,4,1,9148,3,18,1,1,1,11),_ApRadiusServerAccessAccepts_Type())
apRadiusServerAccessAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAccessAccepts.setStatus(_A)
_ApRadiusServerTimeouts_Type=Unsigned32
_ApRadiusServerTimeouts_Object=MibTableColumn
apRadiusServerTimeouts=_ApRadiusServerTimeouts_Object((1,3,6,1,4,1,9148,3,18,1,1,1,12),_ApRadiusServerTimeouts_Type())
apRadiusServerTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerTimeouts.setStatus(_A)
_ApRadiusServerAccessRejects_Type=Unsigned32
_ApRadiusServerAccessRejects_Object=MibTableColumn
apRadiusServerAccessRejects=_ApRadiusServerAccessRejects_Object((1,3,6,1,4,1,9148,3,18,1,1,1,13),_ApRadiusServerAccessRejects_Type())
apRadiusServerAccessRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAccessRejects.setStatus(_A)
_ApRadiusServerUnknownPDUTypes_Type=Unsigned32
_ApRadiusServerUnknownPDUTypes_Object=MibTableColumn
apRadiusServerUnknownPDUTypes=_ApRadiusServerUnknownPDUTypes_Object((1,3,6,1,4,1,9148,3,18,1,1,1,14),_ApRadiusServerUnknownPDUTypes_Type())
apRadiusServerUnknownPDUTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerUnknownPDUTypes.setStatus(_A)
_ApRadiusServerAccessChallenges_Type=Unsigned32
_ApRadiusServerAccessChallenges_Object=MibTableColumn
apRadiusServerAccessChallenges=_ApRadiusServerAccessChallenges_Object((1,3,6,1,4,1,9148,3,18,1,1,1,15),_ApRadiusServerAccessChallenges_Type())
apRadiusServerAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:apRadiusServerAccessChallenges.setStatus(_A)
_ApRadiusServerConformance_ObjectIdentity=ObjectIdentity
apRadiusServerConformance=_ApRadiusServerConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,18,2))
_ApRadiusObjectGroups_ObjectIdentity=ObjectIdentity
apRadiusObjectGroups=_ApRadiusObjectGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,18,2,1))
apRadiusInterfaceStatsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,18,2,1,1))
apRadiusInterfaceStatsGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:apRadiusInterfaceStatsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'apRadiusServerModule':apRadiusServerModule,'apRadiusServerMIBObjects':apRadiusServerMIBObjects,'apRadiusServerStatsTable':apRadiusServerStatsTable,'apRadiusServerStatsEntry':apRadiusServerStatsEntry,_D:apRadiusServerAddressType,_E:apRadiusServerAddress,_F:apRadiusServerRoundTripTime,_G:apRadiusServerMalformedAccessResponse,_H:apRadiusServerAccessRequests,_I:apRadiusServerDisconnectRequests,_J:apRadiusServerDisconnectACKs,_K:apRadiusServerDisconnectNACks,_L:apRadiusServerBadAuthenticators,_M:apRadiusServerAccessRetransmissions,_N:apRadiusServerAccessAccepts,_O:apRadiusServerTimeouts,_P:apRadiusServerAccessRejects,_Q:apRadiusServerUnknownPDUTypes,_R:apRadiusServerAccessChallenges,'apRadiusServerConformance':apRadiusServerConformance,'apRadiusObjectGroups':apRadiusObjectGroups,'apRadiusInterfaceStatsGroup':apRadiusInterfaceStatsGroup})