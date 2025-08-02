_U='cAuthorizationClientMIBGroup'
_T='cAuthorizServerGroupId'
_S='cAuthorizClientUnknownTypes'
_R='cAuthorizClientTimeouts'
_Q='cAuthorizClientPendingRequests'
_P='cAuthorizClientBadAuthenticates'
_O='cAuthorizClientMalAccessResps'
_N='cAuthorizClientAccessChallenges'
_M='cAuthorizClientAccessRejects'
_L='cAuthorizClientAccessAccepts'
_K='cAuthorizClientAccessRetrans'
_J='cAuthorizClientAccessRequests'
_I='cAuthorizClientRoundTripTime'
_H='cAuthorizClientServerPortNum'
_G='cAuthorizServerAddress'
_F='cAuthorizServerAddressType'
_E='cAuthorizServerIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-AUTHORIZATION-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,=mibBuilder.importSymbols('CISCO-TC','CiscoPort')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval')
ciscoAuthorizationStatsMibModule=ModuleIdentity((1,3,6,1,4,1,9,9,343))
if mibBuilder.loadTexts:ciscoAuthorizationStatsMibModule.setRevisions(('2006-11-08 00:00',))
_CStatsAuthorization_ObjectIdentity=ObjectIdentity
cStatsAuthorization=_CStatsAuthorization_ObjectIdentity((1,3,6,1,4,1,9,9,343,1))
_CAuthorizationGlobal_ObjectIdentity=ObjectIdentity
cAuthorizationGlobal=_CAuthorizationGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,343,1,1))
_CAuthorizationStatsTable_Object=MibTable
cAuthorizationStatsTable=_CAuthorizationStatsTable_Object((1,3,6,1,4,1,9,9,343,1,2))
if mibBuilder.loadTexts:cAuthorizationStatsTable.setStatus(_A)
_CAuthorizationStatsEntry_Object=MibTableRow
cAuthorizationStatsEntry=_CAuthorizationStatsEntry_Object((1,3,6,1,4,1,9,9,343,1,2,1))
cAuthorizationStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cAuthorizationStatsEntry.setStatus(_A)
class _CAuthorizServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CAuthorizServerIndex_Type.__name__=_D
_CAuthorizServerIndex_Object=MibTableColumn
cAuthorizServerIndex=_CAuthorizServerIndex_Object((1,3,6,1,4,1,9,9,343,1,2,1,1),_CAuthorizServerIndex_Type())
cAuthorizServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cAuthorizServerIndex.setStatus(_A)
_CAuthorizServerAddressType_Type=InetAddressType
_CAuthorizServerAddressType_Object=MibTableColumn
cAuthorizServerAddressType=_CAuthorizServerAddressType_Object((1,3,6,1,4,1,9,9,343,1,2,1,2),_CAuthorizServerAddressType_Type())
cAuthorizServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizServerAddressType.setStatus(_A)
_CAuthorizServerAddress_Type=InetAddress
_CAuthorizServerAddress_Object=MibTableColumn
cAuthorizServerAddress=_CAuthorizServerAddress_Object((1,3,6,1,4,1,9,9,343,1,2,1,3),_CAuthorizServerAddress_Type())
cAuthorizServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizServerAddress.setStatus(_A)
_CAuthorizClientServerPortNum_Type=CiscoPort
_CAuthorizClientServerPortNum_Object=MibTableColumn
cAuthorizClientServerPortNum=_CAuthorizClientServerPortNum_Object((1,3,6,1,4,1,9,9,343,1,2,1,4),_CAuthorizClientServerPortNum_Type())
cAuthorizClientServerPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientServerPortNum.setStatus(_A)
_CAuthorizClientRoundTripTime_Type=TimeInterval
_CAuthorizClientRoundTripTime_Object=MibTableColumn
cAuthorizClientRoundTripTime=_CAuthorizClientRoundTripTime_Object((1,3,6,1,4,1,9,9,343,1,2,1,5),_CAuthorizClientRoundTripTime_Type())
cAuthorizClientRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientRoundTripTime.setStatus(_A)
_CAuthorizClientAccessRequests_Type=Counter32
_CAuthorizClientAccessRequests_Object=MibTableColumn
cAuthorizClientAccessRequests=_CAuthorizClientAccessRequests_Object((1,3,6,1,4,1,9,9,343,1,2,1,6),_CAuthorizClientAccessRequests_Type())
cAuthorizClientAccessRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientAccessRequests.setStatus(_A)
_CAuthorizClientAccessRetrans_Type=Counter32
_CAuthorizClientAccessRetrans_Object=MibTableColumn
cAuthorizClientAccessRetrans=_CAuthorizClientAccessRetrans_Object((1,3,6,1,4,1,9,9,343,1,2,1,7),_CAuthorizClientAccessRetrans_Type())
cAuthorizClientAccessRetrans.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientAccessRetrans.setStatus(_A)
_CAuthorizClientAccessAccepts_Type=Counter32
_CAuthorizClientAccessAccepts_Object=MibTableColumn
cAuthorizClientAccessAccepts=_CAuthorizClientAccessAccepts_Object((1,3,6,1,4,1,9,9,343,1,2,1,8),_CAuthorizClientAccessAccepts_Type())
cAuthorizClientAccessAccepts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientAccessAccepts.setStatus(_A)
_CAuthorizClientAccessRejects_Type=Counter32
_CAuthorizClientAccessRejects_Object=MibTableColumn
cAuthorizClientAccessRejects=_CAuthorizClientAccessRejects_Object((1,3,6,1,4,1,9,9,343,1,2,1,9),_CAuthorizClientAccessRejects_Type())
cAuthorizClientAccessRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientAccessRejects.setStatus(_A)
_CAuthorizClientAccessChallenges_Type=Counter32
_CAuthorizClientAccessChallenges_Object=MibTableColumn
cAuthorizClientAccessChallenges=_CAuthorizClientAccessChallenges_Object((1,3,6,1,4,1,9,9,343,1,2,1,10),_CAuthorizClientAccessChallenges_Type())
cAuthorizClientAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientAccessChallenges.setStatus(_A)
_CAuthorizClientMalAccessResps_Type=Counter32
_CAuthorizClientMalAccessResps_Object=MibTableColumn
cAuthorizClientMalAccessResps=_CAuthorizClientMalAccessResps_Object((1,3,6,1,4,1,9,9,343,1,2,1,11),_CAuthorizClientMalAccessResps_Type())
cAuthorizClientMalAccessResps.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientMalAccessResps.setStatus(_A)
_CAuthorizClientBadAuthenticates_Type=Counter32
_CAuthorizClientBadAuthenticates_Object=MibTableColumn
cAuthorizClientBadAuthenticates=_CAuthorizClientBadAuthenticates_Object((1,3,6,1,4,1,9,9,343,1,2,1,12),_CAuthorizClientBadAuthenticates_Type())
cAuthorizClientBadAuthenticates.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientBadAuthenticates.setStatus(_A)
_CAuthorizClientPendingRequests_Type=Gauge32
_CAuthorizClientPendingRequests_Object=MibTableColumn
cAuthorizClientPendingRequests=_CAuthorizClientPendingRequests_Object((1,3,6,1,4,1,9,9,343,1,2,1,13),_CAuthorizClientPendingRequests_Type())
cAuthorizClientPendingRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientPendingRequests.setStatus(_A)
_CAuthorizClientTimeouts_Type=Counter32
_CAuthorizClientTimeouts_Object=MibTableColumn
cAuthorizClientTimeouts=_CAuthorizClientTimeouts_Object((1,3,6,1,4,1,9,9,343,1,2,1,14),_CAuthorizClientTimeouts_Type())
cAuthorizClientTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientTimeouts.setStatus(_A)
_CAuthorizClientUnknownTypes_Type=Counter32
_CAuthorizClientUnknownTypes_Object=MibTableColumn
cAuthorizClientUnknownTypes=_CAuthorizClientUnknownTypes_Object((1,3,6,1,4,1,9,9,343,1,2,1,15),_CAuthorizClientUnknownTypes_Type())
cAuthorizClientUnknownTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizClientUnknownTypes.setStatus(_A)
class _CAuthorizServerGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CAuthorizServerGroupId_Type.__name__=_D
_CAuthorizServerGroupId_Object=MibTableColumn
cAuthorizServerGroupId=_CAuthorizServerGroupId_Object((1,3,6,1,4,1,9,9,343,1,2,1,16),_CAuthorizServerGroupId_Type())
cAuthorizServerGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:cAuthorizServerGroupId.setStatus(_A)
_CAuthorizationMIBConformance_ObjectIdentity=ObjectIdentity
cAuthorizationMIBConformance=_CAuthorizationMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,343,2))
_CAuthorizationMIBCompliances_ObjectIdentity=ObjectIdentity
cAuthorizationMIBCompliances=_CAuthorizationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,343,2,1))
_CAuthorizationGroup_ObjectIdentity=ObjectIdentity
cAuthorizationGroup=_CAuthorizationGroup_ObjectIdentity((1,3,6,1,4,1,9,9,343,2,2))
cAuthorizationClientMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,343,2,2,1))
cAuthorizationClientMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cAuthorizationClientMIBGroup.setStatus(_A)
cAuthorizationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,343,2,1,1))
cAuthorizationMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:cAuthorizationMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAuthorizationStatsMibModule':ciscoAuthorizationStatsMibModule,'cStatsAuthorization':cStatsAuthorization,'cAuthorizationGlobal':cAuthorizationGlobal,'cAuthorizationStatsTable':cAuthorizationStatsTable,'cAuthorizationStatsEntry':cAuthorizationStatsEntry,_E:cAuthorizServerIndex,_F:cAuthorizServerAddressType,_G:cAuthorizServerAddress,_H:cAuthorizClientServerPortNum,_I:cAuthorizClientRoundTripTime,_J:cAuthorizClientAccessRequests,_K:cAuthorizClientAccessRetrans,_L:cAuthorizClientAccessAccepts,_M:cAuthorizClientAccessRejects,_N:cAuthorizClientAccessChallenges,_O:cAuthorizClientMalAccessResps,_P:cAuthorizClientBadAuthenticates,_Q:cAuthorizClientPendingRequests,_R:cAuthorizClientTimeouts,_S:cAuthorizClientUnknownTypes,_T:cAuthorizServerGroupId,'cAuthorizationMIBConformance':cAuthorizationMIBConformance,'cAuthorizationMIBCompliances':cAuthorizationMIBCompliances,'cAuthorizationMIBCompliance':cAuthorizationMIBCompliance,'cAuthorizationGroup':cAuthorizationGroup,_U:cAuthorizationClientMIBGroup})