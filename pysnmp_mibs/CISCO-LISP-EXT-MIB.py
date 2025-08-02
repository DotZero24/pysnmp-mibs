_AM='clispExtEidRegRlocMembershipGroup'
_AL='clispExtRlocMembershipGroup'
_AK='clispExtFeaturesMapCacheWarningThresholdReached'
_AJ='clispExtFeaturesMapCacheLimitReached'
_AI='clispExtFeaturesEidRegMoreSpecificWarningThresholdReached'
_AH='clispExtFeaturesEidRegMoreSpecificLimitReached'
_AG='clispExtEidRegMapRequestDropped'
_AF='clispExtEidRegMoreSpecificWarningThresholdReached'
_AE='clispExtEidRegMoreSpecificLimitReached'
_AD='clispExtEidRegFailure'
_AC='clispExtEidRegSiteAllRegistrationsExpired'
_AB='clispExtUseProxyEtrStateChange'
_AA='clispExtUseMapServerStateChange'
_A9='clispExtMappingDatabaseEidRegFailure'
_A8='clispExtReliableTransportStateChange'
_A7='clispExtUseMapResolverStateChange'
_A6='clispExtEidRegMoreSpecificCount'
_A5='clispExtGlobalStatsEidRegMoreSpecificEntryCount'
_A4='clispExtReliableTransportSessionBytesOut'
_A3='clispExtReliableTransportSessionBytesIn'
_A2='clispExtReliableTransportSessionMessagesOut'
_A1='clispExtReliableTransportSessionMessagesIn'
_A0='clispExtReliableTransportSessionEstablishmentRole'
_z='clispExtReliableTransportSessionLastStateChangeTime'
_y='clispExtRlocMembershipConfigured'
_x='clispExtRlocMembershipDiscovered'
_w='clispExtRlocMembershipMemberSince'
_v='clispExtEidRegRlocMembershipConfigured'
_u='clispExtEidRegRlocMembershipGleaned'
_t='clispExtEidRegRlocMembershipMemberSince'
_s='clispExtFeaturesEntry'
_r='clispExtGlobalStatsEntry'
_q='accessible-for-notify'
_p='clispExtReliableTransportSessionLocalPort'
_o='clispExtReliableTransportSessionLocalAddress'
_n='clispExtReliableTransportSessionLocalAddressLength'
_m='clispExtReliableTransportSessionPeerPort'
_l='clispExtReliableTransportSessionPeerAddress'
_k='clispExtReliableTransportSessionPeerAddressLength'
_j='clispExtRlocMembershipRloc'
_i='clispExtRlocMembershipRlocLength'
_h='clispExtRlocMembershipEidAfi'
_g='clispExtRlocMembershipInstanceID'
_f='clispExtEidRegRlocMembershipRloc'
_e='clispExtEidRegRlocMembershipRlocLength'
_d='clispExtEidRegRlocMembershipEidAfi'
_c='clispExtEidRegRlocMembershipInstanceID'
_b='lispUseProxyEtrState'
_a='lispUseMapResolverState'
_Z='lispMappingDatabaseTimeStamp'
_Y='lispFeaturesMapCacheLimit'
_X='clispExtEidRegMoreSpecificValuesGroup'
_W='clispExtNotificationSupportGroup'
_V='clispExtFeaturesGroup'
_U='clispExtGlobalStatsGroup'
_T='clispExtNotificationsGroup'
_S='clispExtReliableTransportSessionGroup'
_R='clispExtEidRegMapRequestDroppedCause'
_Q='clispExtEidRegFailureCause'
_P='clispExtFeaturesMapCacheWarningThreshold'
_O='clispExtFeaturesEidRegMoreSpecificLimit'
_N='clispExtFeaturesEidRegMoreSpecificWarningThreshold'
_M='clispExtReliableTransportSessionState'
_L='Unsigned32'
_K='lispUseMapServerState'
_J='clispExtEidRegMoreSpecificLimit'
_I='clispExtEidRegMoreSpecificWarningThreshold'
_H='TimeStamp'
_G='lispEidRegistrationSiteName'
_F='Integer32'
_E='LISP-MIB'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-LISP-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
LispAddressType,lispEidRegistrationSiteName,lispFeaturesEntry,lispFeaturesMapCacheLimit,lispGlobalStatsEntry,lispMappingDatabaseTimeStamp,lispUseMapResolverState,lispUseMapServerState,lispUseProxyEtrState=mibBuilder.importSymbols(_E,'LispAddressType',_G,'lispFeaturesEntry',_Y,'lispGlobalStatsEntry',_Z,_a,_K,_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H,'TruthValue')
ciscoLispExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,825))
if mibBuilder.loadTexts:ciscoLispExtMIB.setRevisions(('2015-05-13 00:00',))
_CiscoLispExtNotifications_ObjectIdentity=ObjectIdentity
ciscoLispExtNotifications=_CiscoLispExtNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,825,0))
_CiscoLispExtObjects_ObjectIdentity=ObjectIdentity
ciscoLispExtObjects=_CiscoLispExtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,825,1))
_ClispExtEidRegRlocMembershipTable_Object=MibTable
clispExtEidRegRlocMembershipTable=_ClispExtEidRegRlocMembershipTable_Object((1,3,6,1,4,1,9,9,825,1,1))
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipTable.setStatus(_B)
_ClispExtEidRegRlocMembershipEntry_Object=MibTableRow
clispExtEidRegRlocMembershipEntry=_ClispExtEidRegRlocMembershipEntry_Object((1,3,6,1,4,1,9,9,825,1,1,1))
clispExtEidRegRlocMembershipEntry.setIndexNames((0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipEntry.setStatus(_B)
class _ClispExtEidRegRlocMembershipInstanceID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_ClispExtEidRegRlocMembershipInstanceID_Type.__name__=_L
_ClispExtEidRegRlocMembershipInstanceID_Object=MibTableColumn
clispExtEidRegRlocMembershipInstanceID=_ClispExtEidRegRlocMembershipInstanceID_Object((1,3,6,1,4,1,9,9,825,1,1,1,1),_ClispExtEidRegRlocMembershipInstanceID_Type())
clispExtEidRegRlocMembershipInstanceID.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipInstanceID.setStatus(_B)
_ClispExtEidRegRlocMembershipEidAfi_Type=AddressFamilyNumbers
_ClispExtEidRegRlocMembershipEidAfi_Object=MibTableColumn
clispExtEidRegRlocMembershipEidAfi=_ClispExtEidRegRlocMembershipEidAfi_Object((1,3,6,1,4,1,9,9,825,1,1,1,2),_ClispExtEidRegRlocMembershipEidAfi_Type())
clispExtEidRegRlocMembershipEidAfi.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipEidAfi.setStatus(_B)
class _ClispExtEidRegRlocMembershipRlocLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,39))
_ClispExtEidRegRlocMembershipRlocLength_Type.__name__=_F
_ClispExtEidRegRlocMembershipRlocLength_Object=MibTableColumn
clispExtEidRegRlocMembershipRlocLength=_ClispExtEidRegRlocMembershipRlocLength_Object((1,3,6,1,4,1,9,9,825,1,1,1,3),_ClispExtEidRegRlocMembershipRlocLength_Type())
clispExtEidRegRlocMembershipRlocLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipRlocLength.setStatus(_B)
_ClispExtEidRegRlocMembershipRloc_Type=LispAddressType
_ClispExtEidRegRlocMembershipRloc_Object=MibTableColumn
clispExtEidRegRlocMembershipRloc=_ClispExtEidRegRlocMembershipRloc_Object((1,3,6,1,4,1,9,9,825,1,1,1,4),_ClispExtEidRegRlocMembershipRloc_Type())
clispExtEidRegRlocMembershipRloc.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipRloc.setStatus(_B)
class _ClispExtEidRegRlocMembershipMemberSince_Type(TimeStamp):defaultValue=0
_ClispExtEidRegRlocMembershipMemberSince_Type.__name__=_H
_ClispExtEidRegRlocMembershipMemberSince_Object=MibTableColumn
clispExtEidRegRlocMembershipMemberSince=_ClispExtEidRegRlocMembershipMemberSince_Object((1,3,6,1,4,1,9,9,825,1,1,1,5),_ClispExtEidRegRlocMembershipMemberSince_Type())
clispExtEidRegRlocMembershipMemberSince.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipMemberSince.setStatus(_B)
_ClispExtEidRegRlocMembershipGleaned_Type=TruthValue
_ClispExtEidRegRlocMembershipGleaned_Object=MibTableColumn
clispExtEidRegRlocMembershipGleaned=_ClispExtEidRegRlocMembershipGleaned_Object((1,3,6,1,4,1,9,9,825,1,1,1,6),_ClispExtEidRegRlocMembershipGleaned_Type())
clispExtEidRegRlocMembershipGleaned.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipGleaned.setStatus(_B)
_ClispExtEidRegRlocMembershipConfigured_Type=TruthValue
_ClispExtEidRegRlocMembershipConfigured_Object=MibTableColumn
clispExtEidRegRlocMembershipConfigured=_ClispExtEidRegRlocMembershipConfigured_Object((1,3,6,1,4,1,9,9,825,1,1,1,7),_ClispExtEidRegRlocMembershipConfigured_Type())
clispExtEidRegRlocMembershipConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipConfigured.setStatus(_B)
_ClispExtRlocMembershipTable_Object=MibTable
clispExtRlocMembershipTable=_ClispExtRlocMembershipTable_Object((1,3,6,1,4,1,9,9,825,1,2))
if mibBuilder.loadTexts:clispExtRlocMembershipTable.setStatus(_B)
_ClispExtRlocMembershipEntry_Object=MibTableRow
clispExtRlocMembershipEntry=_ClispExtRlocMembershipEntry_Object((1,3,6,1,4,1,9,9,825,1,2,1))
clispExtRlocMembershipEntry.setIndexNames((0,_A,_g),(0,_A,_h),(0,_A,_i),(0,_A,_j))
if mibBuilder.loadTexts:clispExtRlocMembershipEntry.setStatus(_B)
class _ClispExtRlocMembershipInstanceID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_ClispExtRlocMembershipInstanceID_Type.__name__=_L
_ClispExtRlocMembershipInstanceID_Object=MibTableColumn
clispExtRlocMembershipInstanceID=_ClispExtRlocMembershipInstanceID_Object((1,3,6,1,4,1,9,9,825,1,2,1,1),_ClispExtRlocMembershipInstanceID_Type())
clispExtRlocMembershipInstanceID.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtRlocMembershipInstanceID.setStatus(_B)
_ClispExtRlocMembershipEidAfi_Type=AddressFamilyNumbers
_ClispExtRlocMembershipEidAfi_Object=MibTableColumn
clispExtRlocMembershipEidAfi=_ClispExtRlocMembershipEidAfi_Object((1,3,6,1,4,1,9,9,825,1,2,1,2),_ClispExtRlocMembershipEidAfi_Type())
clispExtRlocMembershipEidAfi.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtRlocMembershipEidAfi.setStatus(_B)
class _ClispExtRlocMembershipRlocLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,39))
_ClispExtRlocMembershipRlocLength_Type.__name__=_F
_ClispExtRlocMembershipRlocLength_Object=MibTableColumn
clispExtRlocMembershipRlocLength=_ClispExtRlocMembershipRlocLength_Object((1,3,6,1,4,1,9,9,825,1,2,1,3),_ClispExtRlocMembershipRlocLength_Type())
clispExtRlocMembershipRlocLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtRlocMembershipRlocLength.setStatus(_B)
_ClispExtRlocMembershipRloc_Type=LispAddressType
_ClispExtRlocMembershipRloc_Object=MibTableColumn
clispExtRlocMembershipRloc=_ClispExtRlocMembershipRloc_Object((1,3,6,1,4,1,9,9,825,1,2,1,4),_ClispExtRlocMembershipRloc_Type())
clispExtRlocMembershipRloc.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtRlocMembershipRloc.setStatus(_B)
class _ClispExtRlocMembershipMemberSince_Type(TimeStamp):defaultValue=0
_ClispExtRlocMembershipMemberSince_Type.__name__=_H
_ClispExtRlocMembershipMemberSince_Object=MibTableColumn
clispExtRlocMembershipMemberSince=_ClispExtRlocMembershipMemberSince_Object((1,3,6,1,4,1,9,9,825,1,2,1,5),_ClispExtRlocMembershipMemberSince_Type())
clispExtRlocMembershipMemberSince.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtRlocMembershipMemberSince.setStatus(_B)
_ClispExtRlocMembershipDiscovered_Type=TruthValue
_ClispExtRlocMembershipDiscovered_Object=MibTableColumn
clispExtRlocMembershipDiscovered=_ClispExtRlocMembershipDiscovered_Object((1,3,6,1,4,1,9,9,825,1,2,1,6),_ClispExtRlocMembershipDiscovered_Type())
clispExtRlocMembershipDiscovered.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtRlocMembershipDiscovered.setStatus(_B)
_ClispExtRlocMembershipConfigured_Type=TruthValue
_ClispExtRlocMembershipConfigured_Object=MibTableColumn
clispExtRlocMembershipConfigured=_ClispExtRlocMembershipConfigured_Object((1,3,6,1,4,1,9,9,825,1,2,1,7),_ClispExtRlocMembershipConfigured_Type())
clispExtRlocMembershipConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtRlocMembershipConfigured.setStatus(_B)
_ClispExtReliableTransportSessionTable_Object=MibTable
clispExtReliableTransportSessionTable=_ClispExtReliableTransportSessionTable_Object((1,3,6,1,4,1,9,9,825,1,3))
if mibBuilder.loadTexts:clispExtReliableTransportSessionTable.setStatus(_B)
_ClispExtReliableTransportSessionEntry_Object=MibTableRow
clispExtReliableTransportSessionEntry=_ClispExtReliableTransportSessionEntry_Object((1,3,6,1,4,1,9,9,825,1,3,1))
clispExtReliableTransportSessionEntry.setIndexNames((0,_A,_k),(0,_A,_l),(0,_A,_m),(0,_A,_n),(0,_A,_o),(0,_A,_p))
if mibBuilder.loadTexts:clispExtReliableTransportSessionEntry.setStatus(_B)
class _ClispExtReliableTransportSessionPeerAddressLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,39))
_ClispExtReliableTransportSessionPeerAddressLength_Type.__name__=_F
_ClispExtReliableTransportSessionPeerAddressLength_Object=MibTableColumn
clispExtReliableTransportSessionPeerAddressLength=_ClispExtReliableTransportSessionPeerAddressLength_Object((1,3,6,1,4,1,9,9,825,1,3,1,1),_ClispExtReliableTransportSessionPeerAddressLength_Type())
clispExtReliableTransportSessionPeerAddressLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtReliableTransportSessionPeerAddressLength.setStatus(_B)
_ClispExtReliableTransportSessionPeerAddress_Type=LispAddressType
_ClispExtReliableTransportSessionPeerAddress_Object=MibTableColumn
clispExtReliableTransportSessionPeerAddress=_ClispExtReliableTransportSessionPeerAddress_Object((1,3,6,1,4,1,9,9,825,1,3,1,2),_ClispExtReliableTransportSessionPeerAddress_Type())
clispExtReliableTransportSessionPeerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtReliableTransportSessionPeerAddress.setStatus(_B)
_ClispExtReliableTransportSessionPeerPort_Type=InetPortNumber
_ClispExtReliableTransportSessionPeerPort_Object=MibTableColumn
clispExtReliableTransportSessionPeerPort=_ClispExtReliableTransportSessionPeerPort_Object((1,3,6,1,4,1,9,9,825,1,3,1,3),_ClispExtReliableTransportSessionPeerPort_Type())
clispExtReliableTransportSessionPeerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtReliableTransportSessionPeerPort.setStatus(_B)
class _ClispExtReliableTransportSessionLocalAddressLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,39))
_ClispExtReliableTransportSessionLocalAddressLength_Type.__name__=_F
_ClispExtReliableTransportSessionLocalAddressLength_Object=MibTableColumn
clispExtReliableTransportSessionLocalAddressLength=_ClispExtReliableTransportSessionLocalAddressLength_Object((1,3,6,1,4,1,9,9,825,1,3,1,4),_ClispExtReliableTransportSessionLocalAddressLength_Type())
clispExtReliableTransportSessionLocalAddressLength.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtReliableTransportSessionLocalAddressLength.setStatus(_B)
_ClispExtReliableTransportSessionLocalAddress_Type=LispAddressType
_ClispExtReliableTransportSessionLocalAddress_Object=MibTableColumn
clispExtReliableTransportSessionLocalAddress=_ClispExtReliableTransportSessionLocalAddress_Object((1,3,6,1,4,1,9,9,825,1,3,1,5),_ClispExtReliableTransportSessionLocalAddress_Type())
clispExtReliableTransportSessionLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtReliableTransportSessionLocalAddress.setStatus(_B)
_ClispExtReliableTransportSessionLocalPort_Type=InetPortNumber
_ClispExtReliableTransportSessionLocalPort_Object=MibTableColumn
clispExtReliableTransportSessionLocalPort=_ClispExtReliableTransportSessionLocalPort_Object((1,3,6,1,4,1,9,9,825,1,3,1,6),_ClispExtReliableTransportSessionLocalPort_Type())
clispExtReliableTransportSessionLocalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:clispExtReliableTransportSessionLocalPort.setStatus(_B)
class _ClispExtReliableTransportSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ClispExtReliableTransportSessionState_Type.__name__=_F
_ClispExtReliableTransportSessionState_Object=MibTableColumn
clispExtReliableTransportSessionState=_ClispExtReliableTransportSessionState_Object((1,3,6,1,4,1,9,9,825,1,3,1,7),_ClispExtReliableTransportSessionState_Type())
clispExtReliableTransportSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionState.setStatus(_B)
class _ClispExtReliableTransportSessionLastStateChangeTime_Type(TimeStamp):defaultValue=0
_ClispExtReliableTransportSessionLastStateChangeTime_Type.__name__=_H
_ClispExtReliableTransportSessionLastStateChangeTime_Object=MibTableColumn
clispExtReliableTransportSessionLastStateChangeTime=_ClispExtReliableTransportSessionLastStateChangeTime_Object((1,3,6,1,4,1,9,9,825,1,3,1,8),_ClispExtReliableTransportSessionLastStateChangeTime_Type())
clispExtReliableTransportSessionLastStateChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionLastStateChangeTime.setStatus(_B)
class _ClispExtReliableTransportSessionEstablishmentRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passive',1),('active',2)))
_ClispExtReliableTransportSessionEstablishmentRole_Type.__name__=_F
_ClispExtReliableTransportSessionEstablishmentRole_Object=MibTableColumn
clispExtReliableTransportSessionEstablishmentRole=_ClispExtReliableTransportSessionEstablishmentRole_Object((1,3,6,1,4,1,9,9,825,1,3,1,9),_ClispExtReliableTransportSessionEstablishmentRole_Type())
clispExtReliableTransportSessionEstablishmentRole.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionEstablishmentRole.setStatus(_B)
_ClispExtReliableTransportSessionMessagesIn_Type=Counter64
_ClispExtReliableTransportSessionMessagesIn_Object=MibTableColumn
clispExtReliableTransportSessionMessagesIn=_ClispExtReliableTransportSessionMessagesIn_Object((1,3,6,1,4,1,9,9,825,1,3,1,10),_ClispExtReliableTransportSessionMessagesIn_Type())
clispExtReliableTransportSessionMessagesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionMessagesIn.setStatus(_B)
_ClispExtReliableTransportSessionMessagesOut_Type=Counter64
_ClispExtReliableTransportSessionMessagesOut_Object=MibTableColumn
clispExtReliableTransportSessionMessagesOut=_ClispExtReliableTransportSessionMessagesOut_Object((1,3,6,1,4,1,9,9,825,1,3,1,11),_ClispExtReliableTransportSessionMessagesOut_Type())
clispExtReliableTransportSessionMessagesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionMessagesOut.setStatus(_B)
_ClispExtReliableTransportSessionBytesIn_Type=Counter64
_ClispExtReliableTransportSessionBytesIn_Object=MibTableColumn
clispExtReliableTransportSessionBytesIn=_ClispExtReliableTransportSessionBytesIn_Object((1,3,6,1,4,1,9,9,825,1,3,1,12),_ClispExtReliableTransportSessionBytesIn_Type())
clispExtReliableTransportSessionBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionBytesIn.setStatus(_B)
_ClispExtReliableTransportSessionBytesOut_Type=Counter64
_ClispExtReliableTransportSessionBytesOut_Object=MibTableColumn
clispExtReliableTransportSessionBytesOut=_ClispExtReliableTransportSessionBytesOut_Object((1,3,6,1,4,1,9,9,825,1,3,1,13),_ClispExtReliableTransportSessionBytesOut_Type())
clispExtReliableTransportSessionBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtReliableTransportSessionBytesOut.setStatus(_B)
_ClispExtGlobalStatsTable_Object=MibTable
clispExtGlobalStatsTable=_ClispExtGlobalStatsTable_Object((1,3,6,1,4,1,9,9,825,1,4))
if mibBuilder.loadTexts:clispExtGlobalStatsTable.setStatus(_B)
_ClispExtGlobalStatsEntry_Object=MibTableRow
clispExtGlobalStatsEntry=_ClispExtGlobalStatsEntry_Object((1,3,6,1,4,1,9,9,825,1,4,1))
if mibBuilder.loadTexts:clispExtGlobalStatsEntry.setStatus(_B)
_ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Type=Unsigned32
_ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Object=MibTableColumn
clispExtGlobalStatsEidRegMoreSpecificEntryCount=_ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Object((1,3,6,1,4,1,9,9,825,1,4,1,1),_ClispExtGlobalStatsEidRegMoreSpecificEntryCount_Type())
clispExtGlobalStatsEidRegMoreSpecificEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtGlobalStatsEidRegMoreSpecificEntryCount.setStatus(_B)
_ClispExtFeaturesTable_Object=MibTable
clispExtFeaturesTable=_ClispExtFeaturesTable_Object((1,3,6,1,4,1,9,9,825,1,5))
if mibBuilder.loadTexts:clispExtFeaturesTable.setStatus(_B)
_ClispExtFeaturesEntry_Object=MibTableRow
clispExtFeaturesEntry=_ClispExtFeaturesEntry_Object((1,3,6,1,4,1,9,9,825,1,5,1))
if mibBuilder.loadTexts:clispExtFeaturesEntry.setStatus(_B)
_ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Type=Unsigned32
_ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Object=MibTableColumn
clispExtFeaturesEidRegMoreSpecificWarningThreshold=_ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Object((1,3,6,1,4,1,9,9,825,1,5,1,1),_ClispExtFeaturesEidRegMoreSpecificWarningThreshold_Type())
clispExtFeaturesEidRegMoreSpecificWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtFeaturesEidRegMoreSpecificWarningThreshold.setStatus(_B)
_ClispExtFeaturesEidRegMoreSpecificLimit_Type=Unsigned32
_ClispExtFeaturesEidRegMoreSpecificLimit_Object=MibTableColumn
clispExtFeaturesEidRegMoreSpecificLimit=_ClispExtFeaturesEidRegMoreSpecificLimit_Object((1,3,6,1,4,1,9,9,825,1,5,1,2),_ClispExtFeaturesEidRegMoreSpecificLimit_Type())
clispExtFeaturesEidRegMoreSpecificLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtFeaturesEidRegMoreSpecificLimit.setStatus(_B)
_ClispExtFeaturesMapCacheWarningThreshold_Type=Unsigned32
_ClispExtFeaturesMapCacheWarningThreshold_Object=MibTableColumn
clispExtFeaturesMapCacheWarningThreshold=_ClispExtFeaturesMapCacheWarningThreshold_Object((1,3,6,1,4,1,9,9,825,1,5,1,3),_ClispExtFeaturesMapCacheWarningThreshold_Type())
clispExtFeaturesMapCacheWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtFeaturesMapCacheWarningThreshold.setStatus(_B)
_ClispExtNotificationObjects_ObjectIdentity=ObjectIdentity
clispExtNotificationObjects=_ClispExtNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9,9,825,1,6))
class _ClispExtEidRegFailureCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noEidPrefixConfiguration',1),('authenticationFailure',2),('allowedLocatorMismatch',3)))
_ClispExtEidRegFailureCause_Type.__name__=_F
_ClispExtEidRegFailureCause_Object=MibScalar
clispExtEidRegFailureCause=_ClispExtEidRegFailureCause_Object((1,3,6,1,4,1,9,9,825,1,6,1),_ClispExtEidRegFailureCause_Type())
clispExtEidRegFailureCause.setMaxAccess(_q)
if mibBuilder.loadTexts:clispExtEidRegFailureCause.setStatus(_B)
class _ClispExtEidRegMapRequestDroppedCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('malformedRequest',1),('noMatchingEidRegistration',2),('allowedLocatorPolicyViolation',3)))
_ClispExtEidRegMapRequestDroppedCause_Type.__name__=_F
_ClispExtEidRegMapRequestDroppedCause_Object=MibScalar
clispExtEidRegMapRequestDroppedCause=_ClispExtEidRegMapRequestDroppedCause_Object((1,3,6,1,4,1,9,9,825,1,6,2),_ClispExtEidRegMapRequestDroppedCause_Type())
clispExtEidRegMapRequestDroppedCause.setMaxAccess(_q)
if mibBuilder.loadTexts:clispExtEidRegMapRequestDroppedCause.setStatus(_B)
_ClispExtGlobalObjects_ObjectIdentity=ObjectIdentity
clispExtGlobalObjects=_ClispExtGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,825,1,7))
_ClispExtEidRegMoreSpecificWarningThreshold_Type=Unsigned32
_ClispExtEidRegMoreSpecificWarningThreshold_Object=MibScalar
clispExtEidRegMoreSpecificWarningThreshold=_ClispExtEidRegMoreSpecificWarningThreshold_Object((1,3,6,1,4,1,9,9,825,1,7,1),_ClispExtEidRegMoreSpecificWarningThreshold_Type())
clispExtEidRegMoreSpecificWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtEidRegMoreSpecificWarningThreshold.setStatus(_B)
_ClispExtEidRegMoreSpecificLimit_Type=Unsigned32
_ClispExtEidRegMoreSpecificLimit_Object=MibScalar
clispExtEidRegMoreSpecificLimit=_ClispExtEidRegMoreSpecificLimit_Object((1,3,6,1,4,1,9,9,825,1,7,2),_ClispExtEidRegMoreSpecificLimit_Type())
clispExtEidRegMoreSpecificLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtEidRegMoreSpecificLimit.setStatus(_B)
_ClispExtEidRegMoreSpecificCount_Type=Unsigned32
_ClispExtEidRegMoreSpecificCount_Object=MibScalar
clispExtEidRegMoreSpecificCount=_ClispExtEidRegMoreSpecificCount_Object((1,3,6,1,4,1,9,9,825,1,7,3),_ClispExtEidRegMoreSpecificCount_Type())
clispExtEidRegMoreSpecificCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clispExtEidRegMoreSpecificCount.setStatus(_B)
_CiscoLispExtConformance_ObjectIdentity=ObjectIdentity
ciscoLispExtConformance=_CiscoLispExtConformance_ObjectIdentity((1,3,6,1,4,1,9,9,825,2))
_CiscoLispExtCompliances_ObjectIdentity=ObjectIdentity
ciscoLispExtCompliances=_CiscoLispExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,825,2,1))
_CiscoLispExtGroups_ObjectIdentity=ObjectIdentity
ciscoLispExtGroups=_CiscoLispExtGroups_ObjectIdentity((1,3,6,1,4,1,9,9,825,2,2))
lispGlobalStatsEntry.registerAugmentions((_A,_r))
clispExtGlobalStatsEntry.setIndexNames(*lispGlobalStatsEntry.getIndexNames())
lispFeaturesEntry.registerAugmentions((_A,_s))
clispExtFeaturesEntry.setIndexNames(*lispFeaturesEntry.getIndexNames())
clispExtEidRegRlocMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,2))
clispExtEidRegRlocMembershipGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:clispExtEidRegRlocMembershipGroup.setStatus(_B)
clispExtRlocMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,3))
clispExtRlocMembershipGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:clispExtRlocMembershipGroup.setStatus(_B)
clispExtReliableTransportSessionGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,4))
clispExtReliableTransportSessionGroup.setObjects(*((_A,_M),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:clispExtReliableTransportSessionGroup.setStatus(_B)
clispExtGlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,5))
clispExtGlobalStatsGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:clispExtGlobalStatsGroup.setStatus(_B)
clispExtFeaturesGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,6))
clispExtFeaturesGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:clispExtFeaturesGroup.setStatus(_B)
clispExtNotificationSupportGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,7))
clispExtNotificationSupportGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:clispExtNotificationSupportGroup.setStatus(_B)
clispExtEidRegMoreSpecificValuesGroup=ObjectGroup((1,3,6,1,4,1,9,9,825,2,2,8))
clispExtEidRegMoreSpecificValuesGroup.setObjects(*((_A,_I),(_A,_J),(_A,_A6)))
if mibBuilder.loadTexts:clispExtEidRegMoreSpecificValuesGroup.setStatus(_B)
clispExtUseMapResolverStateChange=NotificationType((1,3,6,1,4,1,9,9,825,0,1))
clispExtUseMapResolverStateChange.setObjects((_E,_a))
if mibBuilder.loadTexts:clispExtUseMapResolverStateChange.setStatus(_B)
clispExtReliableTransportStateChange=NotificationType((1,3,6,1,4,1,9,9,825,0,2))
clispExtReliableTransportStateChange.setObjects((_A,_M))
if mibBuilder.loadTexts:clispExtReliableTransportStateChange.setStatus(_B)
clispExtMappingDatabaseEidRegFailure=NotificationType((1,3,6,1,4,1,9,9,825,0,3))
clispExtMappingDatabaseEidRegFailure.setObjects(*((_E,_Z),(_E,_K)))
if mibBuilder.loadTexts:clispExtMappingDatabaseEidRegFailure.setStatus(_B)
clispExtUseMapServerStateChange=NotificationType((1,3,6,1,4,1,9,9,825,0,4))
clispExtUseMapServerStateChange.setObjects((_E,_K))
if mibBuilder.loadTexts:clispExtUseMapServerStateChange.setStatus(_B)
clispExtUseProxyEtrStateChange=NotificationType((1,3,6,1,4,1,9,9,825,0,5))
clispExtUseProxyEtrStateChange.setObjects((_E,_b))
if mibBuilder.loadTexts:clispExtUseProxyEtrStateChange.setStatus(_B)
clispExtEidRegSiteAllRegistrationsExpired=NotificationType((1,3,6,1,4,1,9,9,825,0,6))
clispExtEidRegSiteAllRegistrationsExpired.setObjects((_E,_G))
if mibBuilder.loadTexts:clispExtEidRegSiteAllRegistrationsExpired.setStatus(_B)
clispExtEidRegFailure=NotificationType((1,3,6,1,4,1,9,9,825,0,7))
clispExtEidRegFailure.setObjects(*((_E,_G),(_A,_Q)))
if mibBuilder.loadTexts:clispExtEidRegFailure.setStatus(_B)
clispExtFeaturesEidRegMoreSpecificLimitReached=NotificationType((1,3,6,1,4,1,9,9,825,0,8))
clispExtFeaturesEidRegMoreSpecificLimitReached.setObjects((_A,_O))
if mibBuilder.loadTexts:clispExtFeaturesEidRegMoreSpecificLimitReached.setStatus(_B)
clispExtFeaturesEidRegMoreSpecificWarningThresholdReached=NotificationType((1,3,6,1,4,1,9,9,825,0,9))
clispExtFeaturesEidRegMoreSpecificWarningThresholdReached.setObjects((_A,_N))
if mibBuilder.loadTexts:clispExtFeaturesEidRegMoreSpecificWarningThresholdReached.setStatus(_B)
clispExtEidRegMapRequestDropped=NotificationType((1,3,6,1,4,1,9,9,825,0,10))
clispExtEidRegMapRequestDropped.setObjects(*((_E,_G),(_A,_R)))
if mibBuilder.loadTexts:clispExtEidRegMapRequestDropped.setStatus(_B)
clispExtEidRegMoreSpecificLimitReached=NotificationType((1,3,6,1,4,1,9,9,825,0,11))
clispExtEidRegMoreSpecificLimitReached.setObjects((_A,_J))
if mibBuilder.loadTexts:clispExtEidRegMoreSpecificLimitReached.setStatus(_B)
clispExtEidRegMoreSpecificWarningThresholdReached=NotificationType((1,3,6,1,4,1,9,9,825,0,12))
clispExtEidRegMoreSpecificWarningThresholdReached.setObjects((_A,_I))
if mibBuilder.loadTexts:clispExtEidRegMoreSpecificWarningThresholdReached.setStatus(_B)
clispExtFeaturesMapCacheLimitReached=NotificationType((1,3,6,1,4,1,9,9,825,0,13))
clispExtFeaturesMapCacheLimitReached.setObjects((_E,_Y))
if mibBuilder.loadTexts:clispExtFeaturesMapCacheLimitReached.setStatus(_B)
clispExtFeaturesMapCacheWarningThresholdReached=NotificationType((1,3,6,1,4,1,9,9,825,0,14))
clispExtFeaturesMapCacheWarningThresholdReached.setObjects((_A,_P))
if mibBuilder.loadTexts:clispExtFeaturesMapCacheWarningThresholdReached.setStatus(_B)
clispExtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,825,2,2,1))
clispExtNotificationsGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:clispExtNotificationsGroup.setStatus(_B)
ciscoLispExtMIBComplianceAll=ModuleCompliance((1,3,6,1,4,1,9,9,825,2,1,1))
ciscoLispExtMIBComplianceAll.setObjects(*((_A,_AL),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoLispExtMIBComplianceAll.setStatus(_B)
ciscoLispExtMIBComplianceMapServer=ModuleCompliance((1,3,6,1,4,1,9,9,825,2,1,2))
ciscoLispExtMIBComplianceMapServer.setObjects(*((_A,_AM),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoLispExtMIBComplianceMapServer.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoLispExtMIB':ciscoLispExtMIB,'ciscoLispExtNotifications':ciscoLispExtNotifications,_A7:clispExtUseMapResolverStateChange,_A8:clispExtReliableTransportStateChange,_A9:clispExtMappingDatabaseEidRegFailure,_AA:clispExtUseMapServerStateChange,_AB:clispExtUseProxyEtrStateChange,_AC:clispExtEidRegSiteAllRegistrationsExpired,_AD:clispExtEidRegFailure,_AH:clispExtFeaturesEidRegMoreSpecificLimitReached,_AI:clispExtFeaturesEidRegMoreSpecificWarningThresholdReached,_AG:clispExtEidRegMapRequestDropped,_AE:clispExtEidRegMoreSpecificLimitReached,_AF:clispExtEidRegMoreSpecificWarningThresholdReached,_AJ:clispExtFeaturesMapCacheLimitReached,_AK:clispExtFeaturesMapCacheWarningThresholdReached,'ciscoLispExtObjects':ciscoLispExtObjects,'clispExtEidRegRlocMembershipTable':clispExtEidRegRlocMembershipTable,'clispExtEidRegRlocMembershipEntry':clispExtEidRegRlocMembershipEntry,_c:clispExtEidRegRlocMembershipInstanceID,_d:clispExtEidRegRlocMembershipEidAfi,_e:clispExtEidRegRlocMembershipRlocLength,_f:clispExtEidRegRlocMembershipRloc,_t:clispExtEidRegRlocMembershipMemberSince,_u:clispExtEidRegRlocMembershipGleaned,_v:clispExtEidRegRlocMembershipConfigured,'clispExtRlocMembershipTable':clispExtRlocMembershipTable,'clispExtRlocMembershipEntry':clispExtRlocMembershipEntry,_g:clispExtRlocMembershipInstanceID,_h:clispExtRlocMembershipEidAfi,_i:clispExtRlocMembershipRlocLength,_j:clispExtRlocMembershipRloc,_w:clispExtRlocMembershipMemberSince,_x:clispExtRlocMembershipDiscovered,_y:clispExtRlocMembershipConfigured,'clispExtReliableTransportSessionTable':clispExtReliableTransportSessionTable,'clispExtReliableTransportSessionEntry':clispExtReliableTransportSessionEntry,_k:clispExtReliableTransportSessionPeerAddressLength,_l:clispExtReliableTransportSessionPeerAddress,_m:clispExtReliableTransportSessionPeerPort,_n:clispExtReliableTransportSessionLocalAddressLength,_o:clispExtReliableTransportSessionLocalAddress,_p:clispExtReliableTransportSessionLocalPort,_M:clispExtReliableTransportSessionState,_z:clispExtReliableTransportSessionLastStateChangeTime,_A0:clispExtReliableTransportSessionEstablishmentRole,_A1:clispExtReliableTransportSessionMessagesIn,_A2:clispExtReliableTransportSessionMessagesOut,_A3:clispExtReliableTransportSessionBytesIn,_A4:clispExtReliableTransportSessionBytesOut,'clispExtGlobalStatsTable':clispExtGlobalStatsTable,_r:clispExtGlobalStatsEntry,_A5:clispExtGlobalStatsEidRegMoreSpecificEntryCount,'clispExtFeaturesTable':clispExtFeaturesTable,_s:clispExtFeaturesEntry,_N:clispExtFeaturesEidRegMoreSpecificWarningThreshold,_O:clispExtFeaturesEidRegMoreSpecificLimit,_P:clispExtFeaturesMapCacheWarningThreshold,'clispExtNotificationObjects':clispExtNotificationObjects,_Q:clispExtEidRegFailureCause,_R:clispExtEidRegMapRequestDroppedCause,'clispExtGlobalObjects':clispExtGlobalObjects,_I:clispExtEidRegMoreSpecificWarningThreshold,_J:clispExtEidRegMoreSpecificLimit,_A6:clispExtEidRegMoreSpecificCount,'ciscoLispExtConformance':ciscoLispExtConformance,'ciscoLispExtCompliances':ciscoLispExtCompliances,'ciscoLispExtMIBComplianceAll':ciscoLispExtMIBComplianceAll,'ciscoLispExtMIBComplianceMapServer':ciscoLispExtMIBComplianceMapServer,'ciscoLispExtGroups':ciscoLispExtGroups,_T:clispExtNotificationsGroup,_AM:clispExtEidRegRlocMembershipGroup,_AL:clispExtRlocMembershipGroup,_S:clispExtReliableTransportSessionGroup,_U:clispExtGlobalStatsGroup,_V:clispExtFeaturesGroup,_W:clispExtNotificationSupportGroup,_X:clispExtEidRegMoreSpecificValuesGroup})