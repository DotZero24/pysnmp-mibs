_G='wwpRadiusServerId'
_F='WWP-RADIUS-CLIENT-MIB'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpRadiusClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,11))
if mibBuilder.loadTexts:wwpRadiusClientMIB.setRevisions(('2001-04-03 17:00',))
_WwpRadiusClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpRadiusClientMIBObjects=_WwpRadiusClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,11,1))
_WwpRadiusClient_ObjectIdentity=ObjectIdentity
wwpRadiusClient=_WwpRadiusClient_ObjectIdentity((1,3,6,1,4,1,6141,2,11,1,1))
class _WwpRadiusClientTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_WwpRadiusClientTimeout_Type.__name__=_C
_WwpRadiusClientTimeout_Object=MibScalar
wwpRadiusClientTimeout=_WwpRadiusClientTimeout_Object((1,3,6,1,4,1,6141,2,11,1,1,1),_WwpRadiusClientTimeout_Type())
wwpRadiusClientTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpRadiusClientTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpRadiusClientTimeout.setUnits('seconds')
class _WwpRadiusClientRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpRadiusClientRetries_Type.__name__=_C
_WwpRadiusClientRetries_Object=MibScalar
wwpRadiusClientRetries=_WwpRadiusClientRetries_Object((1,3,6,1,4,1,6141,2,11,1,1,2),_WwpRadiusClientRetries_Type())
wwpRadiusClientRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpRadiusClientRetries.setStatus(_A)
_WwpRadiusServerTable_Object=MibTable
wwpRadiusServerTable=_WwpRadiusServerTable_Object((1,3,6,1,4,1,6141,2,11,1,1,3))
if mibBuilder.loadTexts:wwpRadiusServerTable.setStatus(_A)
_WwpRadiusServerEntry_Object=MibTableRow
wwpRadiusServerEntry=_WwpRadiusServerEntry_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1))
wwpRadiusServerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wwpRadiusServerEntry.setStatus(_A)
class _WwpRadiusServerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpRadiusServerId_Type.__name__=_C
_WwpRadiusServerId_Object=MibTableColumn
wwpRadiusServerId=_WwpRadiusServerId_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,1),_WwpRadiusServerId_Type())
wwpRadiusServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusServerId.setStatus(_A)
_WwpRadiusServerIpAddr_Type=IpAddress
_WwpRadiusServerIpAddr_Object=MibTableColumn
wwpRadiusServerIpAddr=_WwpRadiusServerIpAddr_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,2),_WwpRadiusServerIpAddr_Type())
wwpRadiusServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpRadiusServerIpAddr.setStatus(_A)
class _WwpRadiusServerAuthPort_Type(Integer32):defaultValue=1812;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpRadiusServerAuthPort_Type.__name__=_C
_WwpRadiusServerAuthPort_Object=MibTableColumn
wwpRadiusServerAuthPort=_WwpRadiusServerAuthPort_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,3),_WwpRadiusServerAuthPort_Type())
wwpRadiusServerAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpRadiusServerAuthPort.setStatus(_A)
_WwpRadiusClientRoundTripTime_Type=TimeTicks
_WwpRadiusClientRoundTripTime_Object=MibTableColumn
wwpRadiusClientRoundTripTime=_WwpRadiusClientRoundTripTime_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,4),_WwpRadiusClientRoundTripTime_Type())
wwpRadiusClientRoundTripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientRoundTripTime.setStatus(_A)
_WwpRadiusClientAccessRequests_Type=Counter32
_WwpRadiusClientAccessRequests_Object=MibTableColumn
wwpRadiusClientAccessRequests=_WwpRadiusClientAccessRequests_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,5),_WwpRadiusClientAccessRequests_Type())
wwpRadiusClientAccessRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientAccessRequests.setStatus(_A)
_WwpRadiusClientAccessRetransmissions_Type=Counter32
_WwpRadiusClientAccessRetransmissions_Object=MibTableColumn
wwpRadiusClientAccessRetransmissions=_WwpRadiusClientAccessRetransmissions_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,6),_WwpRadiusClientAccessRetransmissions_Type())
wwpRadiusClientAccessRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientAccessRetransmissions.setStatus(_A)
_WwpRadiusClientAccessAccepts_Type=Counter32
_WwpRadiusClientAccessAccepts_Object=MibTableColumn
wwpRadiusClientAccessAccepts=_WwpRadiusClientAccessAccepts_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,7),_WwpRadiusClientAccessAccepts_Type())
wwpRadiusClientAccessAccepts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientAccessAccepts.setStatus(_A)
_WwpRadiusClientAccessRejects_Type=Counter32
_WwpRadiusClientAccessRejects_Object=MibTableColumn
wwpRadiusClientAccessRejects=_WwpRadiusClientAccessRejects_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,8),_WwpRadiusClientAccessRejects_Type())
wwpRadiusClientAccessRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientAccessRejects.setStatus(_A)
_WwpRadiusClientAccessChallenges_Type=Counter32
_WwpRadiusClientAccessChallenges_Object=MibTableColumn
wwpRadiusClientAccessChallenges=_WwpRadiusClientAccessChallenges_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,9),_WwpRadiusClientAccessChallenges_Type())
wwpRadiusClientAccessChallenges.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientAccessChallenges.setStatus(_A)
_WwpRadiusClientMalformedAccessResponses_Type=Counter32
_WwpRadiusClientMalformedAccessResponses_Object=MibTableColumn
wwpRadiusClientMalformedAccessResponses=_WwpRadiusClientMalformedAccessResponses_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,10),_WwpRadiusClientMalformedAccessResponses_Type())
wwpRadiusClientMalformedAccessResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientMalformedAccessResponses.setStatus(_A)
_WwpRadiusClientBadAuthenticators_Type=Counter32
_WwpRadiusClientBadAuthenticators_Object=MibTableColumn
wwpRadiusClientBadAuthenticators=_WwpRadiusClientBadAuthenticators_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,11),_WwpRadiusClientBadAuthenticators_Type())
wwpRadiusClientBadAuthenticators.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientBadAuthenticators.setStatus(_A)
_WwpRadiusClientPendingRequests_Type=Gauge32
_WwpRadiusClientPendingRequests_Object=MibTableColumn
wwpRadiusClientPendingRequests=_WwpRadiusClientPendingRequests_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,12),_WwpRadiusClientPendingRequests_Type())
wwpRadiusClientPendingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientPendingRequests.setStatus(_A)
_WwpRadiusClientTimeouts_Type=Counter32
_WwpRadiusClientTimeouts_Object=MibTableColumn
wwpRadiusClientTimeouts=_WwpRadiusClientTimeouts_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,13),_WwpRadiusClientTimeouts_Type())
wwpRadiusClientTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientTimeouts.setStatus(_A)
_WwpRadiusClientUnknownTypes_Type=Counter32
_WwpRadiusClientUnknownTypes_Object=MibTableColumn
wwpRadiusClientUnknownTypes=_WwpRadiusClientUnknownTypes_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,14),_WwpRadiusClientUnknownTypes_Type())
wwpRadiusClientUnknownTypes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientUnknownTypes.setStatus(_A)
_WwpRadiusClientPacketsDropped_Type=Counter32
_WwpRadiusClientPacketsDropped_Object=MibTableColumn
wwpRadiusClientPacketsDropped=_WwpRadiusClientPacketsDropped_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,15),_WwpRadiusClientPacketsDropped_Type())
wwpRadiusClientPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpRadiusClientPacketsDropped.setStatus(_A)
_WwpRadiusServerStatus_Type=RowStatus
_WwpRadiusServerStatus_Object=MibTableColumn
wwpRadiusServerStatus=_WwpRadiusServerStatus_Object((1,3,6,1,4,1,6141,2,11,1,1,3,1,16),_WwpRadiusServerStatus_Type())
wwpRadiusServerStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpRadiusServerStatus.setStatus(_A)
class _WwpRadiusClientAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,127))
_WwpRadiusClientAuthKey_Type.__name__=_E
_WwpRadiusClientAuthKey_Object=MibScalar
wwpRadiusClientAuthKey=_WwpRadiusClientAuthKey_Object((1,3,6,1,4,1,6141,2,11,1,1,4),_WwpRadiusClientAuthKey_Type())
wwpRadiusClientAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpRadiusClientAuthKey.setStatus(_A)
_WwpRadiusClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpRadiusClientMIBNotificationPrefix=_WwpRadiusClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,11,2))
_WwpRadiusClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpRadiusClientMIBNotifications=_WwpRadiusClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,11,2,0))
_WwpRadiusClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpRadiusClientMIBConformance=_WwpRadiusClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,11,3))
_WwpRadiusClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpRadiusClientMIBCompliances=_WwpRadiusClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,11,3,1))
_WwpRadiusClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpRadiusClientMIBGroups=_WwpRadiusClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,11,3,2))
mibBuilder.exportSymbols(_F,**{'wwpRadiusClientMIB':wwpRadiusClientMIB,'wwpRadiusClientMIBObjects':wwpRadiusClientMIBObjects,'wwpRadiusClient':wwpRadiusClient,'wwpRadiusClientTimeout':wwpRadiusClientTimeout,'wwpRadiusClientRetries':wwpRadiusClientRetries,'wwpRadiusServerTable':wwpRadiusServerTable,'wwpRadiusServerEntry':wwpRadiusServerEntry,_G:wwpRadiusServerId,'wwpRadiusServerIpAddr':wwpRadiusServerIpAddr,'wwpRadiusServerAuthPort':wwpRadiusServerAuthPort,'wwpRadiusClientRoundTripTime':wwpRadiusClientRoundTripTime,'wwpRadiusClientAccessRequests':wwpRadiusClientAccessRequests,'wwpRadiusClientAccessRetransmissions':wwpRadiusClientAccessRetransmissions,'wwpRadiusClientAccessAccepts':wwpRadiusClientAccessAccepts,'wwpRadiusClientAccessRejects':wwpRadiusClientAccessRejects,'wwpRadiusClientAccessChallenges':wwpRadiusClientAccessChallenges,'wwpRadiusClientMalformedAccessResponses':wwpRadiusClientMalformedAccessResponses,'wwpRadiusClientBadAuthenticators':wwpRadiusClientBadAuthenticators,'wwpRadiusClientPendingRequests':wwpRadiusClientPendingRequests,'wwpRadiusClientTimeouts':wwpRadiusClientTimeouts,'wwpRadiusClientUnknownTypes':wwpRadiusClientUnknownTypes,'wwpRadiusClientPacketsDropped':wwpRadiusClientPacketsDropped,'wwpRadiusServerStatus':wwpRadiusServerStatus,'wwpRadiusClientAuthKey':wwpRadiusClientAuthKey,'wwpRadiusClientMIBNotificationPrefix':wwpRadiusClientMIBNotificationPrefix,'wwpRadiusClientMIBNotifications':wwpRadiusClientMIBNotifications,'wwpRadiusClientMIBConformance':wwpRadiusClientMIBConformance,'wwpRadiusClientMIBCompliances':wwpRadiusClientMIBCompliances,'wwpRadiusClientMIBGroups':wwpRadiusClientMIBGroups})