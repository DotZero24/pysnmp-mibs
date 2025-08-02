_s='radiusAuthClientExtMIBGroup'
_r='radiusAuthClientMIBGroup'
_q='radiusAuthClientCounterDiscontinuity'
_p='radiusAuthClientExtPacketsDropped'
_o='radiusAuthClientExtUnknownTypes'
_n='radiusAuthClientExtTimeouts'
_m='radiusAuthClientExtPendingRequests'
_l='radiusAuthClientExtBadAuthenticators'
_k='radiusAuthClientExtMalformedAccessResponses'
_j='radiusAuthClientExtAccessChallenges'
_i='radiusAuthClientExtAccessRejects'
_h='radiusAuthClientExtAccessAccepts'
_g='radiusAuthClientExtAccessRetransmissions'
_f='radiusAuthClientExtAccessRequests'
_e='radiusAuthClientExtRoundTripTime'
_d='radiusAuthClientServerInetPortNumber'
_c='radiusAuthServerInetAddress'
_b='radiusAuthServerInetAddressType'
_a='radiusAuthClientPacketsDropped'
_Z='radiusAuthClientUnknownTypes'
_Y='radiusAuthClientTimeouts'
_X='radiusAuthClientPendingRequests'
_W='radiusAuthClientBadAuthenticators'
_V='radiusAuthClientMalformedAccessResponses'
_U='radiusAuthClientAccessChallenges'
_T='radiusAuthClientAccessRejects'
_S='radiusAuthClientAccessAccepts'
_R='radiusAuthClientAccessRetransmissions'
_Q='radiusAuthClientAccessRequests'
_P='radiusAuthClientRoundTripTime'
_O='radiusAuthClientServerPortNumber'
_N='radiusAuthServerAddress'
_M='radiusAuthServerExtIndex'
_L='timeouts'
_K='not-accessible'
_J='radiusAuthServerIndex'
_I='InetPortNumber'
_H='radiusAuthClientInvalidServerAddresses'
_G='radiusAuthClientIdentifier'
_F='Integer32'
_E='deprecated'
_D='packets'
_C='current'
_B='read-only'
_A='RADIUS-AUTH-CLIENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
radiusAuthClientMIB=ModuleIdentity((1,3,6,1,2,1,67,1,2))
if mibBuilder.loadTexts:radiusAuthClientMIB.setRevisions(('2006-08-21 00:00','1999-06-11 00:00'))
_RadiusMIB_ObjectIdentity=ObjectIdentity
radiusMIB=_RadiusMIB_ObjectIdentity((1,3,6,1,2,1,67))
if mibBuilder.loadTexts:radiusMIB.setStatus(_C)
_RadiusAuthentication_ObjectIdentity=ObjectIdentity
radiusAuthentication=_RadiusAuthentication_ObjectIdentity((1,3,6,1,2,1,67,1))
_RadiusAuthClientMIBObjects_ObjectIdentity=ObjectIdentity
radiusAuthClientMIBObjects=_RadiusAuthClientMIBObjects_ObjectIdentity((1,3,6,1,2,1,67,1,2,1))
_RadiusAuthClient_ObjectIdentity=ObjectIdentity
radiusAuthClient=_RadiusAuthClient_ObjectIdentity((1,3,6,1,2,1,67,1,2,1,1))
_RadiusAuthClientInvalidServerAddresses_Type=Counter32
_RadiusAuthClientInvalidServerAddresses_Object=MibScalar
radiusAuthClientInvalidServerAddresses=_RadiusAuthClientInvalidServerAddresses_Object((1,3,6,1,2,1,67,1,2,1,1,1),_RadiusAuthClientInvalidServerAddresses_Type())
radiusAuthClientInvalidServerAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientInvalidServerAddresses.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientInvalidServerAddresses.setUnits(_D)
_RadiusAuthClientIdentifier_Type=SnmpAdminString
_RadiusAuthClientIdentifier_Object=MibScalar
radiusAuthClientIdentifier=_RadiusAuthClientIdentifier_Object((1,3,6,1,2,1,67,1,2,1,1,2),_RadiusAuthClientIdentifier_Type())
radiusAuthClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientIdentifier.setStatus(_C)
_RadiusAuthServerTable_Object=MibTable
radiusAuthServerTable=_RadiusAuthServerTable_Object((1,3,6,1,2,1,67,1,2,1,1,3))
if mibBuilder.loadTexts:radiusAuthServerTable.setStatus(_E)
_RadiusAuthServerEntry_Object=MibTableRow
radiusAuthServerEntry=_RadiusAuthServerEntry_Object((1,3,6,1,2,1,67,1,2,1,1,3,1))
radiusAuthServerEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:radiusAuthServerEntry.setStatus(_E)
class _RadiusAuthServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RadiusAuthServerIndex_Type.__name__=_F
_RadiusAuthServerIndex_Object=MibTableColumn
radiusAuthServerIndex=_RadiusAuthServerIndex_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,1),_RadiusAuthServerIndex_Type())
radiusAuthServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:radiusAuthServerIndex.setStatus(_E)
_RadiusAuthServerAddress_Type=IpAddress
_RadiusAuthServerAddress_Object=MibTableColumn
radiusAuthServerAddress=_RadiusAuthServerAddress_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,2),_RadiusAuthServerAddress_Type())
radiusAuthServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServerAddress.setStatus(_E)
class _RadiusAuthClientServerPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RadiusAuthClientServerPortNumber_Type.__name__=_F
_RadiusAuthClientServerPortNumber_Object=MibTableColumn
radiusAuthClientServerPortNumber=_RadiusAuthClientServerPortNumber_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,3),_RadiusAuthClientServerPortNumber_Type())
radiusAuthClientServerPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientServerPortNumber.setStatus(_E)
_RadiusAuthClientRoundTripTime_Type=TimeTicks
_RadiusAuthClientRoundTripTime_Object=MibTableColumn
radiusAuthClientRoundTripTime=_RadiusAuthClientRoundTripTime_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,4),_RadiusAuthClientRoundTripTime_Type())
radiusAuthClientRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientRoundTripTime.setStatus(_E)
_RadiusAuthClientAccessRequests_Type=Counter32
_RadiusAuthClientAccessRequests_Object=MibTableColumn
radiusAuthClientAccessRequests=_RadiusAuthClientAccessRequests_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,5),_RadiusAuthClientAccessRequests_Type())
radiusAuthClientAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientAccessRequests.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientAccessRequests.setUnits(_D)
_RadiusAuthClientAccessRetransmissions_Type=Counter32
_RadiusAuthClientAccessRetransmissions_Object=MibTableColumn
radiusAuthClientAccessRetransmissions=_RadiusAuthClientAccessRetransmissions_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,6),_RadiusAuthClientAccessRetransmissions_Type())
radiusAuthClientAccessRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientAccessRetransmissions.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientAccessRetransmissions.setUnits(_D)
_RadiusAuthClientAccessAccepts_Type=Counter32
_RadiusAuthClientAccessAccepts_Object=MibTableColumn
radiusAuthClientAccessAccepts=_RadiusAuthClientAccessAccepts_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,7),_RadiusAuthClientAccessAccepts_Type())
radiusAuthClientAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientAccessAccepts.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientAccessAccepts.setUnits(_D)
_RadiusAuthClientAccessRejects_Type=Counter32
_RadiusAuthClientAccessRejects_Object=MibTableColumn
radiusAuthClientAccessRejects=_RadiusAuthClientAccessRejects_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,8),_RadiusAuthClientAccessRejects_Type())
radiusAuthClientAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientAccessRejects.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientAccessRejects.setUnits(_D)
_RadiusAuthClientAccessChallenges_Type=Counter32
_RadiusAuthClientAccessChallenges_Object=MibTableColumn
radiusAuthClientAccessChallenges=_RadiusAuthClientAccessChallenges_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,9),_RadiusAuthClientAccessChallenges_Type())
radiusAuthClientAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientAccessChallenges.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientAccessChallenges.setUnits(_D)
_RadiusAuthClientMalformedAccessResponses_Type=Counter32
_RadiusAuthClientMalformedAccessResponses_Object=MibTableColumn
radiusAuthClientMalformedAccessResponses=_RadiusAuthClientMalformedAccessResponses_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,10),_RadiusAuthClientMalformedAccessResponses_Type())
radiusAuthClientMalformedAccessResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientMalformedAccessResponses.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientMalformedAccessResponses.setUnits(_D)
_RadiusAuthClientBadAuthenticators_Type=Counter32
_RadiusAuthClientBadAuthenticators_Object=MibTableColumn
radiusAuthClientBadAuthenticators=_RadiusAuthClientBadAuthenticators_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,11),_RadiusAuthClientBadAuthenticators_Type())
radiusAuthClientBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientBadAuthenticators.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientBadAuthenticators.setUnits(_D)
_RadiusAuthClientPendingRequests_Type=Gauge32
_RadiusAuthClientPendingRequests_Object=MibTableColumn
radiusAuthClientPendingRequests=_RadiusAuthClientPendingRequests_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,12),_RadiusAuthClientPendingRequests_Type())
radiusAuthClientPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientPendingRequests.setStatus(_E)
_RadiusAuthClientTimeouts_Type=Counter32
_RadiusAuthClientTimeouts_Object=MibTableColumn
radiusAuthClientTimeouts=_RadiusAuthClientTimeouts_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,13),_RadiusAuthClientTimeouts_Type())
radiusAuthClientTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientTimeouts.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientTimeouts.setUnits(_L)
_RadiusAuthClientUnknownTypes_Type=Counter32
_RadiusAuthClientUnknownTypes_Object=MibTableColumn
radiusAuthClientUnknownTypes=_RadiusAuthClientUnknownTypes_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,14),_RadiusAuthClientUnknownTypes_Type())
radiusAuthClientUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientUnknownTypes.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientUnknownTypes.setUnits(_D)
_RadiusAuthClientPacketsDropped_Type=Counter32
_RadiusAuthClientPacketsDropped_Object=MibTableColumn
radiusAuthClientPacketsDropped=_RadiusAuthClientPacketsDropped_Object((1,3,6,1,2,1,67,1,2,1,1,3,1,15),_RadiusAuthClientPacketsDropped_Type())
radiusAuthClientPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientPacketsDropped.setStatus(_E)
if mibBuilder.loadTexts:radiusAuthClientPacketsDropped.setUnits(_D)
_RadiusAuthServerExtTable_Object=MibTable
radiusAuthServerExtTable=_RadiusAuthServerExtTable_Object((1,3,6,1,2,1,67,1,2,1,1,4))
if mibBuilder.loadTexts:radiusAuthServerExtTable.setStatus(_C)
_RadiusAuthServerExtEntry_Object=MibTableRow
radiusAuthServerExtEntry=_RadiusAuthServerExtEntry_Object((1,3,6,1,2,1,67,1,2,1,1,4,1))
radiusAuthServerExtEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:radiusAuthServerExtEntry.setStatus(_C)
class _RadiusAuthServerExtIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RadiusAuthServerExtIndex_Type.__name__=_F
_RadiusAuthServerExtIndex_Object=MibTableColumn
radiusAuthServerExtIndex=_RadiusAuthServerExtIndex_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,1),_RadiusAuthServerExtIndex_Type())
radiusAuthServerExtIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:radiusAuthServerExtIndex.setStatus(_C)
_RadiusAuthServerInetAddressType_Type=InetAddressType
_RadiusAuthServerInetAddressType_Object=MibTableColumn
radiusAuthServerInetAddressType=_RadiusAuthServerInetAddressType_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,2),_RadiusAuthServerInetAddressType_Type())
radiusAuthServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServerInetAddressType.setStatus(_C)
_RadiusAuthServerInetAddress_Type=InetAddress
_RadiusAuthServerInetAddress_Object=MibTableColumn
radiusAuthServerInetAddress=_RadiusAuthServerInetAddress_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,3),_RadiusAuthServerInetAddress_Type())
radiusAuthServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthServerInetAddress.setStatus(_C)
class _RadiusAuthClientServerInetPortNumber_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RadiusAuthClientServerInetPortNumber_Type.__name__=_I
_RadiusAuthClientServerInetPortNumber_Object=MibTableColumn
radiusAuthClientServerInetPortNumber=_RadiusAuthClientServerInetPortNumber_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,4),_RadiusAuthClientServerInetPortNumber_Type())
radiusAuthClientServerInetPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientServerInetPortNumber.setStatus(_C)
_RadiusAuthClientExtRoundTripTime_Type=TimeTicks
_RadiusAuthClientExtRoundTripTime_Object=MibTableColumn
radiusAuthClientExtRoundTripTime=_RadiusAuthClientExtRoundTripTime_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,5),_RadiusAuthClientExtRoundTripTime_Type())
radiusAuthClientExtRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtRoundTripTime.setStatus(_C)
_RadiusAuthClientExtAccessRequests_Type=Counter32
_RadiusAuthClientExtAccessRequests_Object=MibTableColumn
radiusAuthClientExtAccessRequests=_RadiusAuthClientExtAccessRequests_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,6),_RadiusAuthClientExtAccessRequests_Type())
radiusAuthClientExtAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtAccessRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtAccessRequests.setUnits(_D)
_RadiusAuthClientExtAccessRetransmissions_Type=Counter32
_RadiusAuthClientExtAccessRetransmissions_Object=MibTableColumn
radiusAuthClientExtAccessRetransmissions=_RadiusAuthClientExtAccessRetransmissions_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,7),_RadiusAuthClientExtAccessRetransmissions_Type())
radiusAuthClientExtAccessRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtAccessRetransmissions.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtAccessRetransmissions.setUnits(_D)
_RadiusAuthClientExtAccessAccepts_Type=Counter32
_RadiusAuthClientExtAccessAccepts_Object=MibTableColumn
radiusAuthClientExtAccessAccepts=_RadiusAuthClientExtAccessAccepts_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,8),_RadiusAuthClientExtAccessAccepts_Type())
radiusAuthClientExtAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtAccessAccepts.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtAccessAccepts.setUnits(_D)
_RadiusAuthClientExtAccessRejects_Type=Counter32
_RadiusAuthClientExtAccessRejects_Object=MibTableColumn
radiusAuthClientExtAccessRejects=_RadiusAuthClientExtAccessRejects_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,9),_RadiusAuthClientExtAccessRejects_Type())
radiusAuthClientExtAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtAccessRejects.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtAccessRejects.setUnits(_D)
_RadiusAuthClientExtAccessChallenges_Type=Counter32
_RadiusAuthClientExtAccessChallenges_Object=MibTableColumn
radiusAuthClientExtAccessChallenges=_RadiusAuthClientExtAccessChallenges_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,10),_RadiusAuthClientExtAccessChallenges_Type())
radiusAuthClientExtAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtAccessChallenges.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtAccessChallenges.setUnits(_D)
_RadiusAuthClientExtMalformedAccessResponses_Type=Counter32
_RadiusAuthClientExtMalformedAccessResponses_Object=MibTableColumn
radiusAuthClientExtMalformedAccessResponses=_RadiusAuthClientExtMalformedAccessResponses_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,11),_RadiusAuthClientExtMalformedAccessResponses_Type())
radiusAuthClientExtMalformedAccessResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtMalformedAccessResponses.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtMalformedAccessResponses.setUnits(_D)
_RadiusAuthClientExtBadAuthenticators_Type=Counter32
_RadiusAuthClientExtBadAuthenticators_Object=MibTableColumn
radiusAuthClientExtBadAuthenticators=_RadiusAuthClientExtBadAuthenticators_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,12),_RadiusAuthClientExtBadAuthenticators_Type())
radiusAuthClientExtBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtBadAuthenticators.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtBadAuthenticators.setUnits(_D)
_RadiusAuthClientExtPendingRequests_Type=Gauge32
_RadiusAuthClientExtPendingRequests_Object=MibTableColumn
radiusAuthClientExtPendingRequests=_RadiusAuthClientExtPendingRequests_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,13),_RadiusAuthClientExtPendingRequests_Type())
radiusAuthClientExtPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtPendingRequests.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtPendingRequests.setUnits(_D)
_RadiusAuthClientExtTimeouts_Type=Counter32
_RadiusAuthClientExtTimeouts_Object=MibTableColumn
radiusAuthClientExtTimeouts=_RadiusAuthClientExtTimeouts_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,14),_RadiusAuthClientExtTimeouts_Type())
radiusAuthClientExtTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtTimeouts.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtTimeouts.setUnits(_L)
_RadiusAuthClientExtUnknownTypes_Type=Counter32
_RadiusAuthClientExtUnknownTypes_Object=MibTableColumn
radiusAuthClientExtUnknownTypes=_RadiusAuthClientExtUnknownTypes_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,15),_RadiusAuthClientExtUnknownTypes_Type())
radiusAuthClientExtUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtUnknownTypes.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtUnknownTypes.setUnits(_D)
_RadiusAuthClientExtPacketsDropped_Type=Counter32
_RadiusAuthClientExtPacketsDropped_Object=MibTableColumn
radiusAuthClientExtPacketsDropped=_RadiusAuthClientExtPacketsDropped_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,16),_RadiusAuthClientExtPacketsDropped_Type())
radiusAuthClientExtPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientExtPacketsDropped.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientExtPacketsDropped.setUnits(_D)
_RadiusAuthClientCounterDiscontinuity_Type=TimeTicks
_RadiusAuthClientCounterDiscontinuity_Object=MibTableColumn
radiusAuthClientCounterDiscontinuity=_RadiusAuthClientCounterDiscontinuity_Object((1,3,6,1,2,1,67,1,2,1,1,4,1,17),_RadiusAuthClientCounterDiscontinuity_Type())
radiusAuthClientCounterDiscontinuity.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAuthClientCounterDiscontinuity.setStatus(_C)
if mibBuilder.loadTexts:radiusAuthClientCounterDiscontinuity.setUnits('centiseconds')
_RadiusAuthClientMIBConformance_ObjectIdentity=ObjectIdentity
radiusAuthClientMIBConformance=_RadiusAuthClientMIBConformance_ObjectIdentity((1,3,6,1,2,1,67,1,2,2))
_RadiusAuthClientMIBCompliances_ObjectIdentity=ObjectIdentity
radiusAuthClientMIBCompliances=_RadiusAuthClientMIBCompliances_ObjectIdentity((1,3,6,1,2,1,67,1,2,2,1))
_RadiusAuthClientMIBGroups_ObjectIdentity=ObjectIdentity
radiusAuthClientMIBGroups=_RadiusAuthClientMIBGroups_ObjectIdentity((1,3,6,1,2,1,67,1,2,2,2))
radiusAuthClientMIBGroup=ObjectGroup((1,3,6,1,2,1,67,1,2,2,2,1))
radiusAuthClientMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:radiusAuthClientMIBGroup.setStatus(_E)
radiusAuthClientExtMIBGroup=ObjectGroup((1,3,6,1,2,1,67,1,2,2,2,2))
radiusAuthClientExtMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:radiusAuthClientExtMIBGroup.setStatus(_C)
radiusAuthClientMIBCompliance=ModuleCompliance((1,3,6,1,2,1,67,1,2,2,1,1))
radiusAuthClientMIBCompliance.setObjects((_A,_r))
if mibBuilder.loadTexts:radiusAuthClientMIBCompliance.setStatus(_E)
radiusAuthClientExtMIBCompliance=ModuleCompliance((1,3,6,1,2,1,67,1,2,2,1,2))
radiusAuthClientExtMIBCompliance.setObjects((_A,_s))
if mibBuilder.loadTexts:radiusAuthClientExtMIBCompliance.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'radiusMIB':radiusMIB,'radiusAuthentication':radiusAuthentication,'radiusAuthClientMIB':radiusAuthClientMIB,'radiusAuthClientMIBObjects':radiusAuthClientMIBObjects,'radiusAuthClient':radiusAuthClient,_H:radiusAuthClientInvalidServerAddresses,_G:radiusAuthClientIdentifier,'radiusAuthServerTable':radiusAuthServerTable,'radiusAuthServerEntry':radiusAuthServerEntry,_J:radiusAuthServerIndex,_N:radiusAuthServerAddress,_O:radiusAuthClientServerPortNumber,_P:radiusAuthClientRoundTripTime,_Q:radiusAuthClientAccessRequests,_R:radiusAuthClientAccessRetransmissions,_S:radiusAuthClientAccessAccepts,_T:radiusAuthClientAccessRejects,_U:radiusAuthClientAccessChallenges,_V:radiusAuthClientMalformedAccessResponses,_W:radiusAuthClientBadAuthenticators,_X:radiusAuthClientPendingRequests,_Y:radiusAuthClientTimeouts,_Z:radiusAuthClientUnknownTypes,_a:radiusAuthClientPacketsDropped,'radiusAuthServerExtTable':radiusAuthServerExtTable,'radiusAuthServerExtEntry':radiusAuthServerExtEntry,_M:radiusAuthServerExtIndex,_b:radiusAuthServerInetAddressType,_c:radiusAuthServerInetAddress,_d:radiusAuthClientServerInetPortNumber,_e:radiusAuthClientExtRoundTripTime,_f:radiusAuthClientExtAccessRequests,_g:radiusAuthClientExtAccessRetransmissions,_h:radiusAuthClientExtAccessAccepts,_i:radiusAuthClientExtAccessRejects,_j:radiusAuthClientExtAccessChallenges,_k:radiusAuthClientExtMalformedAccessResponses,_l:radiusAuthClientExtBadAuthenticators,_m:radiusAuthClientExtPendingRequests,_n:radiusAuthClientExtTimeouts,_o:radiusAuthClientExtUnknownTypes,_p:radiusAuthClientExtPacketsDropped,_q:radiusAuthClientCounterDiscontinuity,'radiusAuthClientMIBConformance':radiusAuthClientMIBConformance,'radiusAuthClientMIBCompliances':radiusAuthClientMIBCompliances,'radiusAuthClientMIBCompliance':radiusAuthClientMIBCompliance,'radiusAuthClientExtMIBCompliance':radiusAuthClientExtMIBCompliance,'radiusAuthClientMIBGroups':radiusAuthClientMIBGroups,_r:radiusAuthClientMIBGroup,_s:radiusAuthClientExtMIBGroup})