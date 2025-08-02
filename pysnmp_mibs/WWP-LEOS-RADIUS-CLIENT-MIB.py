_I='read-create'
_H='wwpLeosRadiusClientServerIndex'
_G='WWP-LEOS-RADIUS-CLIENT-MIB'
_F='enabled'
_E='disabled'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosRadiusClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,20))
if mibBuilder.loadTexts:wwpLeosRadiusClientMIB.setRevisions(('2012-04-26 00:00','2012-04-05 00:00','2001-04-03 17:00'))
class RadiusString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_WwpLeosRadiusClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClientMIBObjects=_WwpLeosRadiusClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,1))
_WwpLeosRadiusClient_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClient=_WwpLeosRadiusClient_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,1,1))
class _WwpLeosRadiusAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_WwpLeosRadiusAdminState_Type.__name__=_C
_WwpLeosRadiusAdminState_Object=MibScalar
wwpLeosRadiusAdminState=_WwpLeosRadiusAdminState_Object((1,3,6,1,4,1,6141,2,60,20,1,1,1),_WwpLeosRadiusAdminState_Type())
wwpLeosRadiusAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusAdminState.setStatus(_A)
class _WwpLeosRadiusOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_WwpLeosRadiusOperState_Type.__name__=_C
_WwpLeosRadiusOperState_Object=MibScalar
wwpLeosRadiusOperState=_WwpLeosRadiusOperState_Object((1,3,6,1,4,1,6141,2,60,20,1,1,2),_WwpLeosRadiusOperState_Type())
wwpLeosRadiusOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusOperState.setStatus(_A)
class _WwpLeosRadiusClientTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_WwpLeosRadiusClientTimeout_Type.__name__=_C
_WwpLeosRadiusClientTimeout_Object=MibScalar
wwpLeosRadiusClientTimeout=_WwpLeosRadiusClientTimeout_Object((1,3,6,1,4,1,6141,2,60,20,1,1,3),_WwpLeosRadiusClientTimeout_Type())
wwpLeosRadiusClientTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRadiusClientTimeout.setUnits('seconds')
class _WwpLeosRadiusClientRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosRadiusClientRetries_Type.__name__=_C
_WwpLeosRadiusClientRetries_Object=MibScalar
wwpLeosRadiusClientRetries=_WwpLeosRadiusClientRetries_Object((1,3,6,1,4,1,6141,2,60,20,1,1,4),_WwpLeosRadiusClientRetries_Type())
wwpLeosRadiusClientRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientRetries.setStatus(_A)
_WwpLeosRadiusClientAuthKey_Type=RadiusString
_WwpLeosRadiusClientAuthKey_Object=MibScalar
wwpLeosRadiusClientAuthKey=_WwpLeosRadiusClientAuthKey_Object((1,3,6,1,4,1,6141,2,60,20,1,1,5),_WwpLeosRadiusClientAuthKey_Type())
wwpLeosRadiusClientAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientAuthKey.setStatus(_A)
_WwpLeosRadiusClientServerTable_Object=MibTable
wwpLeosRadiusClientServerTable=_WwpLeosRadiusClientServerTable_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6))
if mibBuilder.loadTexts:wwpLeosRadiusClientServerTable.setStatus(_A)
_WwpLeosRadiusClientServerEntry_Object=MibTableRow
wwpLeosRadiusClientServerEntry=_WwpLeosRadiusClientServerEntry_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1))
wwpLeosRadiusClientServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:wwpLeosRadiusClientServerEntry.setStatus(_A)
class _WwpLeosRadiusClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WwpLeosRadiusClientServerIndex_Type.__name__=_C
_WwpLeosRadiusClientServerIndex_Object=MibTableColumn
wwpLeosRadiusClientServerIndex=_WwpLeosRadiusClientServerIndex_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,1),_WwpLeosRadiusClientServerIndex_Type())
wwpLeosRadiusClientServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wwpLeosRadiusClientServerIndex.setStatus(_A)
_WwpLeosRadiusClientServerAddr_Type=DisplayString
_WwpLeosRadiusClientServerAddr_Object=MibTableColumn
wwpLeosRadiusClientServerAddr=_WwpLeosRadiusClientServerAddr_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,2),_WwpLeosRadiusClientServerAddr_Type())
wwpLeosRadiusClientServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAddr.setStatus(_A)
_WwpLeosRadiusClientServerResolvedAddr_Type=IpAddress
_WwpLeosRadiusClientServerResolvedAddr_Object=MibTableColumn
wwpLeosRadiusClientServerResolvedAddr=_WwpLeosRadiusClientServerResolvedAddr_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,3),_WwpLeosRadiusClientServerResolvedAddr_Type())
wwpLeosRadiusClientServerResolvedAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerResolvedAddr.setStatus(_A)
class _WwpLeosRadiusClientServerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WwpLeosRadiusClientServerPriority_Type.__name__=_C
_WwpLeosRadiusClientServerPriority_Object=MibTableColumn
wwpLeosRadiusClientServerPriority=_WwpLeosRadiusClientServerPriority_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,4),_WwpLeosRadiusClientServerPriority_Type())
wwpLeosRadiusClientServerPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerPriority.setStatus(_A)
class _WwpLeosRadiusClientServerAuthPort_Type(Integer32):defaultValue=1812;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRadiusClientServerAuthPort_Type.__name__=_C
_WwpLeosRadiusClientServerAuthPort_Object=MibTableColumn
wwpLeosRadiusClientServerAuthPort=_WwpLeosRadiusClientServerAuthPort_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,5),_WwpLeosRadiusClientServerAuthPort_Type())
wwpLeosRadiusClientServerAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAuthPort.setStatus(_A)
_WwpLeosRadiusClientServerRoundTripTime_Type=TimeTicks
_WwpLeosRadiusClientServerRoundTripTime_Object=MibTableColumn
wwpLeosRadiusClientServerRoundTripTime=_WwpLeosRadiusClientServerRoundTripTime_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,6),_WwpLeosRadiusClientServerRoundTripTime_Type())
wwpLeosRadiusClientServerRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerRoundTripTime.setStatus(_A)
_WwpLeosRadiusClientServerAccessRequests_Type=Counter32
_WwpLeosRadiusClientServerAccessRequests_Object=MibTableColumn
wwpLeosRadiusClientServerAccessRequests=_WwpLeosRadiusClientServerAccessRequests_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,7),_WwpLeosRadiusClientServerAccessRequests_Type())
wwpLeosRadiusClientServerAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAccessRequests.setStatus(_A)
_WwpLeosRadiusClientServerAccessRetransmissions_Type=Counter32
_WwpLeosRadiusClientServerAccessRetransmissions_Object=MibTableColumn
wwpLeosRadiusClientServerAccessRetransmissions=_WwpLeosRadiusClientServerAccessRetransmissions_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,8),_WwpLeosRadiusClientServerAccessRetransmissions_Type())
wwpLeosRadiusClientServerAccessRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAccessRetransmissions.setStatus(_A)
_WwpLeosRadiusClientServerAccessAccepts_Type=Counter32
_WwpLeosRadiusClientServerAccessAccepts_Object=MibTableColumn
wwpLeosRadiusClientServerAccessAccepts=_WwpLeosRadiusClientServerAccessAccepts_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,9),_WwpLeosRadiusClientServerAccessAccepts_Type())
wwpLeosRadiusClientServerAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAccessAccepts.setStatus(_A)
_WwpLeosRadiusClientServerAccessRejects_Type=Counter32
_WwpLeosRadiusClientServerAccessRejects_Object=MibTableColumn
wwpLeosRadiusClientServerAccessRejects=_WwpLeosRadiusClientServerAccessRejects_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,10),_WwpLeosRadiusClientServerAccessRejects_Type())
wwpLeosRadiusClientServerAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAccessRejects.setStatus(_A)
_WwpLeosRadiusClientServerAccessChallenges_Type=Counter32
_WwpLeosRadiusClientServerAccessChallenges_Object=MibTableColumn
wwpLeosRadiusClientServerAccessChallenges=_WwpLeosRadiusClientServerAccessChallenges_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,11),_WwpLeosRadiusClientServerAccessChallenges_Type())
wwpLeosRadiusClientServerAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerAccessChallenges.setStatus(_A)
_WwpLeosRadiusClientServerMalformedAccessResponses_Type=Counter32
_WwpLeosRadiusClientServerMalformedAccessResponses_Object=MibTableColumn
wwpLeosRadiusClientServerMalformedAccessResponses=_WwpLeosRadiusClientServerMalformedAccessResponses_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,12),_WwpLeosRadiusClientServerMalformedAccessResponses_Type())
wwpLeosRadiusClientServerMalformedAccessResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerMalformedAccessResponses.setStatus(_A)
_WwpLeosRadiusClientServerBadAuthenticators_Type=Counter32
_WwpLeosRadiusClientServerBadAuthenticators_Object=MibTableColumn
wwpLeosRadiusClientServerBadAuthenticators=_WwpLeosRadiusClientServerBadAuthenticators_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,13),_WwpLeosRadiusClientServerBadAuthenticators_Type())
wwpLeosRadiusClientServerBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerBadAuthenticators.setStatus(_A)
_WwpLeosRadiusClientServerPendingRequests_Type=Gauge32
_WwpLeosRadiusClientServerPendingRequests_Object=MibTableColumn
wwpLeosRadiusClientServerPendingRequests=_WwpLeosRadiusClientServerPendingRequests_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,14),_WwpLeosRadiusClientServerPendingRequests_Type())
wwpLeosRadiusClientServerPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerPendingRequests.setStatus(_A)
_WwpLeosRadiusClientServerTimeouts_Type=Counter32
_WwpLeosRadiusClientServerTimeouts_Object=MibTableColumn
wwpLeosRadiusClientServerTimeouts=_WwpLeosRadiusClientServerTimeouts_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,15),_WwpLeosRadiusClientServerTimeouts_Type())
wwpLeosRadiusClientServerTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerTimeouts.setStatus(_A)
_WwpLeosRadiusClientServerUnknownTypes_Type=Counter32
_WwpLeosRadiusClientServerUnknownTypes_Object=MibTableColumn
wwpLeosRadiusClientServerUnknownTypes=_WwpLeosRadiusClientServerUnknownTypes_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,16),_WwpLeosRadiusClientServerUnknownTypes_Type())
wwpLeosRadiusClientServerUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerUnknownTypes.setStatus(_A)
_WwpLeosRadiusClientServerPacketsDropped_Type=Counter32
_WwpLeosRadiusClientServerPacketsDropped_Object=MibTableColumn
wwpLeosRadiusClientServerPacketsDropped=_WwpLeosRadiusClientServerPacketsDropped_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,17),_WwpLeosRadiusClientServerPacketsDropped_Type())
wwpLeosRadiusClientServerPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerPacketsDropped.setStatus(_A)
_WwpLeosRadiusClientServerStatus_Type=RowStatus
_WwpLeosRadiusClientServerStatus_Object=MibTableColumn
wwpLeosRadiusClientServerStatus=_WwpLeosRadiusClientServerStatus_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,18),_WwpLeosRadiusClientServerStatus_Type())
wwpLeosRadiusClientServerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerStatus.setStatus(_A)
class _WwpLeosRadiusClientServerApplication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('userLogin',1),('dot1x',2),('all',3)))
_WwpLeosRadiusClientServerApplication_Type.__name__=_C
_WwpLeosRadiusClientServerApplication_Object=MibTableColumn
wwpLeosRadiusClientServerApplication=_WwpLeosRadiusClientServerApplication_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,19),_WwpLeosRadiusClientServerApplication_Type())
wwpLeosRadiusClientServerApplication.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerApplication.setStatus(_A)
_WwpLeosRadiusClientServerResolvedInetAddrType_Type=InetAddressType
_WwpLeosRadiusClientServerResolvedInetAddrType_Object=MibTableColumn
wwpLeosRadiusClientServerResolvedInetAddrType=_WwpLeosRadiusClientServerResolvedInetAddrType_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,20),_WwpLeosRadiusClientServerResolvedInetAddrType_Type())
wwpLeosRadiusClientServerResolvedInetAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerResolvedInetAddrType.setStatus(_A)
_WwpLeosRadiusClientServerResolvedInetAddress_Type=InetAddress
_WwpLeosRadiusClientServerResolvedInetAddress_Object=MibTableColumn
wwpLeosRadiusClientServerResolvedInetAddress=_WwpLeosRadiusClientServerResolvedInetAddress_Object((1,3,6,1,4,1,6141,2,60,20,1,1,6,1,21),_WwpLeosRadiusClientServerResolvedInetAddress_Type())
wwpLeosRadiusClientServerResolvedInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRadiusClientServerResolvedInetAddress.setStatus(_A)
_WwpLeosRadiusClientAuthKeyUnset_Type=TruthValue
_WwpLeosRadiusClientAuthKeyUnset_Object=MibScalar
wwpLeosRadiusClientAuthKeyUnset=_WwpLeosRadiusClientAuthKeyUnset_Object((1,3,6,1,4,1,6141,2,60,20,1,1,7),_WwpLeosRadiusClientAuthKeyUnset_Type())
wwpLeosRadiusClientAuthKeyUnset.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientAuthKeyUnset.setStatus(_A)
_WwpLeosRadiusClientAuthSecretUnset_Type=TruthValue
_WwpLeosRadiusClientAuthSecretUnset_Object=MibScalar
wwpLeosRadiusClientAuthSecretUnset=_WwpLeosRadiusClientAuthSecretUnset_Object((1,3,6,1,4,1,6141,2,60,20,1,1,8),_WwpLeosRadiusClientAuthSecretUnset_Type())
wwpLeosRadiusClientAuthSecretUnset.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientAuthSecretUnset.setStatus(_A)
class _WwpLeosRadiusClientSearchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cached',1),('priority',2)))
_WwpLeosRadiusClientSearchType_Type.__name__=_C
_WwpLeosRadiusClientSearchType_Object=MibScalar
wwpLeosRadiusClientSearchType=_WwpLeosRadiusClientSearchType_Object((1,3,6,1,4,1,6141,2,60,20,1,1,10),_WwpLeosRadiusClientSearchType_Type())
wwpLeosRadiusClientSearchType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosRadiusClientSearchType.setStatus(_A)
_WwpLeosRadiusClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClientMIBNotificationPrefix=_WwpLeosRadiusClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,2))
_WwpLeosRadiusClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClientMIBNotifications=_WwpLeosRadiusClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,2,0))
_WwpLeosRadiusClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClientMIBConformance=_WwpLeosRadiusClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,3))
_WwpLeosRadiusClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClientMIBCompliances=_WwpLeosRadiusClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,3,1))
_WwpLeosRadiusClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosRadiusClientMIBGroups=_WwpLeosRadiusClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,20,3,2))
mibBuilder.exportSymbols(_G,**{'RadiusString':RadiusString,'wwpLeosRadiusClientMIB':wwpLeosRadiusClientMIB,'wwpLeosRadiusClientMIBObjects':wwpLeosRadiusClientMIBObjects,'wwpLeosRadiusClient':wwpLeosRadiusClient,'wwpLeosRadiusAdminState':wwpLeosRadiusAdminState,'wwpLeosRadiusOperState':wwpLeosRadiusOperState,'wwpLeosRadiusClientTimeout':wwpLeosRadiusClientTimeout,'wwpLeosRadiusClientRetries':wwpLeosRadiusClientRetries,'wwpLeosRadiusClientAuthKey':wwpLeosRadiusClientAuthKey,'wwpLeosRadiusClientServerTable':wwpLeosRadiusClientServerTable,'wwpLeosRadiusClientServerEntry':wwpLeosRadiusClientServerEntry,_H:wwpLeosRadiusClientServerIndex,'wwpLeosRadiusClientServerAddr':wwpLeosRadiusClientServerAddr,'wwpLeosRadiusClientServerResolvedAddr':wwpLeosRadiusClientServerResolvedAddr,'wwpLeosRadiusClientServerPriority':wwpLeosRadiusClientServerPriority,'wwpLeosRadiusClientServerAuthPort':wwpLeosRadiusClientServerAuthPort,'wwpLeosRadiusClientServerRoundTripTime':wwpLeosRadiusClientServerRoundTripTime,'wwpLeosRadiusClientServerAccessRequests':wwpLeosRadiusClientServerAccessRequests,'wwpLeosRadiusClientServerAccessRetransmissions':wwpLeosRadiusClientServerAccessRetransmissions,'wwpLeosRadiusClientServerAccessAccepts':wwpLeosRadiusClientServerAccessAccepts,'wwpLeosRadiusClientServerAccessRejects':wwpLeosRadiusClientServerAccessRejects,'wwpLeosRadiusClientServerAccessChallenges':wwpLeosRadiusClientServerAccessChallenges,'wwpLeosRadiusClientServerMalformedAccessResponses':wwpLeosRadiusClientServerMalformedAccessResponses,'wwpLeosRadiusClientServerBadAuthenticators':wwpLeosRadiusClientServerBadAuthenticators,'wwpLeosRadiusClientServerPendingRequests':wwpLeosRadiusClientServerPendingRequests,'wwpLeosRadiusClientServerTimeouts':wwpLeosRadiusClientServerTimeouts,'wwpLeosRadiusClientServerUnknownTypes':wwpLeosRadiusClientServerUnknownTypes,'wwpLeosRadiusClientServerPacketsDropped':wwpLeosRadiusClientServerPacketsDropped,'wwpLeosRadiusClientServerStatus':wwpLeosRadiusClientServerStatus,'wwpLeosRadiusClientServerApplication':wwpLeosRadiusClientServerApplication,'wwpLeosRadiusClientServerResolvedInetAddrType':wwpLeosRadiusClientServerResolvedInetAddrType,'wwpLeosRadiusClientServerResolvedInetAddress':wwpLeosRadiusClientServerResolvedInetAddress,'wwpLeosRadiusClientAuthKeyUnset':wwpLeosRadiusClientAuthKeyUnset,'wwpLeosRadiusClientAuthSecretUnset':wwpLeosRadiusClientAuthSecretUnset,'wwpLeosRadiusClientSearchType':wwpLeosRadiusClientSearchType,'wwpLeosRadiusClientMIBNotificationPrefix':wwpLeosRadiusClientMIBNotificationPrefix,'wwpLeosRadiusClientMIBNotifications':wwpLeosRadiusClientMIBNotifications,'wwpLeosRadiusClientMIBConformance':wwpLeosRadiusClientMIBConformance,'wwpLeosRadiusClientMIBCompliances':wwpLeosRadiusClientMIBCompliances,'wwpLeosRadiusClientMIBGroups':wwpLeosRadiusClientMIBGroups})