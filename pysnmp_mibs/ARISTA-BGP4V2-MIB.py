_Ao='aristaBgp4V2StdMIBNotificationGroup'
_An='aristaBgp4V2GlobalsGroup'
_Am='aristaBgp4V2StdMIBNlriGroup'
_Al='aristaBgp4V2StdMIBPeerGroup'
_Ak='aristaBgp4V2StdMIBErrorsGroup'
_Aj='aristaBgp4V2StdMIBCountersGroup'
_Ai='aristaBgp4V2StdMIBTimersGroup'
_Ah='aristaBgp4V2BackwardTransitionNotification'
_Ag='aristaBgp4V2EstablishedNotification'
_Af='aristaBgp4V2NlriPathAttrUnknown'
_Ae='aristaBgp4V2NlriAsPath'
_Ad='aristaBgp4V2NlriOrigin'
_Ac='aristaBgp4V2NlriLinkLocalNextHopAddr'
_Ab='aristaBgp4V2NlriLinkLocalNextHopAddrType'
_Aa='aristaBgp4V2NlriNextHopAddrType'
_AZ='aristaBgp4V2NlriNextHopAddr'
_AY='aristaBgp4V2NlriMedPresent'
_AX='aristaBgp4V2NlriMed'
_AW='aristaBgp4V2NlriLocalPrefPresent'
_AV='aristaBgp4V2NlriLocalPref'
_AU='aristaBgp4V2NlriAtomicAggregate'
_AT='aristaBgp4V2NlriAggregatorAddr'
_AS='aristaBgp4V2NlriAggregatorAS'
_AR='aristaBgp4V2NlriAggregatorPresent'
_AQ='aristaBgp4V2AdjRibsOutRoute'
_AP='aristaBgp4V2NlriCalcLocalPref'
_AO='aristaBgp4V2NlriBest'
_AN='aristaBgp4V2NlriAsPathString'
_AM='aristaBgp4V2NlriAsPathCalcLength'
_AL='aristaBgp4V2PeerPrevState'
_AK='aristaBgp4V2PeerDescription'
_AJ='aristaBgp4V2PeerRemoteIdentifier'
_AI='aristaBgp4V2PeerLocalIdentifier'
_AH='aristaBgp4V2PeerRemoteAs'
_AG='aristaBgp4V2PeerLocalAs'
_AF='aristaBgp4V2PeerLocalAddr'
_AE='aristaBgp4V2PeerLocalAddrType'
_AD='aristaBgp4V2PeerAdminStatus'
_AC='aristaBgp4V2PeerLastErrorSentText'
_AB='aristaBgp4V2PeerLastErrorSentTime'
_AA='aristaBgp4V2PeerLastErrorSentData'
_A9='aristaBgp4V2PeerLastErrorSubCodeSent'
_A8='aristaBgp4V2PeerLastErrorCodeSent'
_A7='aristaBgp4V2PeerLastErrorReceivedTime'
_A6='aristaBgp4V2PeerLastErrorReceivedData'
_A5='aristaBgp4V2PrefixNlriInPrefixesAccepted'
_A4='aristaBgp4V2PrefixNlriInPrefixes'
_A3='aristaBgp4V2PrefixOutPrefixes'
_A2='aristaBgp4V2PrefixInPrefixesAccepted'
_A1='aristaBgp4V2PrefixInPrefixes'
_A0='aristaBgp4V2PeerFsmEstablishedTransitions'
_z='aristaBgp4V2PeerOutTotalMessages'
_y='aristaBgp4V2PeerInTotalMessages'
_x='aristaBgp4V2PeerOutUpdates'
_w='aristaBgp4V2PeerInUpdates'
_v='aristaBgp4V2PeerKeepAlive'
_u='aristaBgp4V2PeerHoldTime'
_t='aristaBgp4V2PeerMinRouteAdverInterval'
_s='aristaBgp4V2PeerMinASOrigInterval'
_r='aristaBgp4V2PeerKeepAliveConfigured'
_q='aristaBgp4V2PeerHoldTimeConfigured'
_p='aristaBgp4V2PeerConnectRetryInterval'
_o='aristaBgp4V2PeerInUpdatesElapsedTime'
_n='aristaBgp4V2PeerFsmEstablishedTime'
_m='aristaBgp4V2DiscontinuityTime'
_l='aristaBgp4V2PeerCountersEntry'
_k='aristaBgp4V2PeerNegotiatedTimersEntry'
_j='aristaBgp4V2PeerConfiguredTimersEntry'
_i='aristaBgp4V2PeerEventTimesEntry'
_h='aristaBgp4V2PeerErrorsEntry'
_g='aristaBgp4V2PrefixGaugesNlri'
_f='aristaBgp4V2AdjRibsOutIndex'
_e='aristaBgp4V2NlriIndex'
_d='aristaBgp4V2PrefixGaugesSafi'
_c='aristaBgp4V2PrefixGaugesAfi'
_b='established'
_a='openconfirm'
_Z='opensent'
_Y='active'
_X='connect'
_W='InetAddress'
_V='aristaBgp4V2PeerLastErrorReceivedText'
_U='aristaBgp4V2PeerLastErrorSubCodeReceived'
_T='aristaBgp4V2PeerLastErrorCodeReceived'
_S='aristaBgp4V2NlriPrefixLen'
_R='aristaBgp4V2NlriPrefix'
_Q='aristaBgp4V2NlriPrefixType'
_P='aristaBgp4V2NlriSafi'
_O='aristaBgp4V2NlriAfi'
_N='aristaBgp4V2PeerRemotePort'
_M='aristaBgp4V2PeerLocalPort'
_L='aristaBgp4V2PeerState'
_K='Integer32'
_J='OctetString'
_I='aristaBgp4V2PeerRemoteAddr'
_H='aristaBgp4V2PeerRemoteAddrType'
_G='aristaBgp4V2PeerInstance'
_F='seconds'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='ARISTA-BGP4V2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AristaBgp4V2AddressFamilyIdentifierTC,AristaBgp4V2EvpnNlriTC,AristaBgp4V2IdentifierTC,AristaBgp4V2SubsequentAddressFamilyIdentifierTC=mibBuilder.importSymbols('ARISTA-BGP4V2-TC-MIB','AristaBgp4V2AddressFamilyIdentifierTC','AristaBgp4V2EvpnNlriTC','AristaBgp4V2IdentifierTC','AristaBgp4V2SubsequentAddressFamilyIdentifierTC')
aristaExperiment,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaExperiment')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,'InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
aristaBgp4V2=ModuleIdentity((1,3,6,1,4,1,30065,4,1))
if mibBuilder.loadTexts:aristaBgp4V2.setRevisions(('2021-02-10 00:00','2020-12-29 00:00','2014-08-15 00:00','2012-10-19 00:00','2012-03-11 00:00'))
_AristaBgp4V2Notifications_ObjectIdentity=ObjectIdentity
aristaBgp4V2Notifications=_AristaBgp4V2Notifications_ObjectIdentity((1,3,6,1,4,1,30065,4,1,0))
_AristaBgp4V2Objects_ObjectIdentity=ObjectIdentity
aristaBgp4V2Objects=_AristaBgp4V2Objects_ObjectIdentity((1,3,6,1,4,1,30065,4,1,1))
_AristaBgp4V2DiscontinuityTable_Object=MibTable
aristaBgp4V2DiscontinuityTable=_AristaBgp4V2DiscontinuityTable_Object((1,3,6,1,4,1,30065,4,1,1,1))
if mibBuilder.loadTexts:aristaBgp4V2DiscontinuityTable.setStatus(_B)
_AristaBgp4V2DiscontinuityEntry_Object=MibTableRow
aristaBgp4V2DiscontinuityEntry=_AristaBgp4V2DiscontinuityEntry_Object((1,3,6,1,4,1,30065,4,1,1,1,1))
aristaBgp4V2DiscontinuityEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:aristaBgp4V2DiscontinuityEntry.setStatus(_B)
_AristaBgp4V2DiscontinuityTime_Type=TimeStamp
_AristaBgp4V2DiscontinuityTime_Object=MibTableColumn
aristaBgp4V2DiscontinuityTime=_AristaBgp4V2DiscontinuityTime_Object((1,3,6,1,4,1,30065,4,1,1,1,1,1),_AristaBgp4V2DiscontinuityTime_Type())
aristaBgp4V2DiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2DiscontinuityTime.setStatus(_B)
_AristaBgp4V2PeerTable_Object=MibTable
aristaBgp4V2PeerTable=_AristaBgp4V2PeerTable_Object((1,3,6,1,4,1,30065,4,1,1,2))
if mibBuilder.loadTexts:aristaBgp4V2PeerTable.setStatus(_B)
_AristaBgp4V2PeerEntry_Object=MibTableRow
aristaBgp4V2PeerEntry=_AristaBgp4V2PeerEntry_Object((1,3,6,1,4,1,30065,4,1,1,2,1))
aristaBgp4V2PeerEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:aristaBgp4V2PeerEntry.setStatus(_B)
class _AristaBgp4V2PeerInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AristaBgp4V2PeerInstance_Type.__name__=_D
_AristaBgp4V2PeerInstance_Object=MibTableColumn
aristaBgp4V2PeerInstance=_AristaBgp4V2PeerInstance_Object((1,3,6,1,4,1,30065,4,1,1,2,1,1),_AristaBgp4V2PeerInstance_Type())
aristaBgp4V2PeerInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2PeerInstance.setStatus(_B)
_AristaBgp4V2PeerLocalAddrType_Type=InetAddressType
_AristaBgp4V2PeerLocalAddrType_Object=MibTableColumn
aristaBgp4V2PeerLocalAddrType=_AristaBgp4V2PeerLocalAddrType_Object((1,3,6,1,4,1,30065,4,1,1,2,1,2),_AristaBgp4V2PeerLocalAddrType_Type())
aristaBgp4V2PeerLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLocalAddrType.setStatus(_B)
_AristaBgp4V2PeerLocalAddr_Type=InetAddress
_AristaBgp4V2PeerLocalAddr_Object=MibTableColumn
aristaBgp4V2PeerLocalAddr=_AristaBgp4V2PeerLocalAddr_Object((1,3,6,1,4,1,30065,4,1,1,2,1,3),_AristaBgp4V2PeerLocalAddr_Type())
aristaBgp4V2PeerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLocalAddr.setStatus(_B)
_AristaBgp4V2PeerRemoteAddrType_Type=InetAddressType
_AristaBgp4V2PeerRemoteAddrType_Object=MibTableColumn
aristaBgp4V2PeerRemoteAddrType=_AristaBgp4V2PeerRemoteAddrType_Object((1,3,6,1,4,1,30065,4,1,1,2,1,4),_AristaBgp4V2PeerRemoteAddrType_Type())
aristaBgp4V2PeerRemoteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2PeerRemoteAddrType.setStatus(_B)
_AristaBgp4V2PeerRemoteAddr_Type=InetAddress
_AristaBgp4V2PeerRemoteAddr_Object=MibTableColumn
aristaBgp4V2PeerRemoteAddr=_AristaBgp4V2PeerRemoteAddr_Object((1,3,6,1,4,1,30065,4,1,1,2,1,5),_AristaBgp4V2PeerRemoteAddr_Type())
aristaBgp4V2PeerRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2PeerRemoteAddr.setStatus(_B)
_AristaBgp4V2PeerLocalPort_Type=InetPortNumber
_AristaBgp4V2PeerLocalPort_Object=MibTableColumn
aristaBgp4V2PeerLocalPort=_AristaBgp4V2PeerLocalPort_Object((1,3,6,1,4,1,30065,4,1,1,2,1,6),_AristaBgp4V2PeerLocalPort_Type())
aristaBgp4V2PeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLocalPort.setStatus(_B)
_AristaBgp4V2PeerLocalAs_Type=InetAutonomousSystemNumber
_AristaBgp4V2PeerLocalAs_Object=MibTableColumn
aristaBgp4V2PeerLocalAs=_AristaBgp4V2PeerLocalAs_Object((1,3,6,1,4,1,30065,4,1,1,2,1,7),_AristaBgp4V2PeerLocalAs_Type())
aristaBgp4V2PeerLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLocalAs.setStatus(_B)
_AristaBgp4V2PeerLocalIdentifier_Type=AristaBgp4V2IdentifierTC
_AristaBgp4V2PeerLocalIdentifier_Object=MibTableColumn
aristaBgp4V2PeerLocalIdentifier=_AristaBgp4V2PeerLocalIdentifier_Object((1,3,6,1,4,1,30065,4,1,1,2,1,8),_AristaBgp4V2PeerLocalIdentifier_Type())
aristaBgp4V2PeerLocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLocalIdentifier.setStatus(_B)
_AristaBgp4V2PeerRemotePort_Type=InetPortNumber
_AristaBgp4V2PeerRemotePort_Object=MibTableColumn
aristaBgp4V2PeerRemotePort=_AristaBgp4V2PeerRemotePort_Object((1,3,6,1,4,1,30065,4,1,1,2,1,9),_AristaBgp4V2PeerRemotePort_Type())
aristaBgp4V2PeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerRemotePort.setStatus(_B)
_AristaBgp4V2PeerRemoteAs_Type=InetAutonomousSystemNumber
_AristaBgp4V2PeerRemoteAs_Object=MibTableColumn
aristaBgp4V2PeerRemoteAs=_AristaBgp4V2PeerRemoteAs_Object((1,3,6,1,4,1,30065,4,1,1,2,1,10),_AristaBgp4V2PeerRemoteAs_Type())
aristaBgp4V2PeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerRemoteAs.setStatus(_B)
_AristaBgp4V2PeerRemoteIdentifier_Type=AristaBgp4V2IdentifierTC
_AristaBgp4V2PeerRemoteIdentifier_Object=MibTableColumn
aristaBgp4V2PeerRemoteIdentifier=_AristaBgp4V2PeerRemoteIdentifier_Object((1,3,6,1,4,1,30065,4,1,1,2,1,11),_AristaBgp4V2PeerRemoteIdentifier_Type())
aristaBgp4V2PeerRemoteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerRemoteIdentifier.setStatus(_B)
class _AristaBgp4V2PeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halted',1),('running',2)))
_AristaBgp4V2PeerAdminStatus_Type.__name__=_K
_AristaBgp4V2PeerAdminStatus_Object=MibTableColumn
aristaBgp4V2PeerAdminStatus=_AristaBgp4V2PeerAdminStatus_Object((1,3,6,1,4,1,30065,4,1,1,2,1,12),_AristaBgp4V2PeerAdminStatus_Type())
aristaBgp4V2PeerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerAdminStatus.setStatus(_B)
class _AristaBgp4V2PeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_AristaBgp4V2PeerState_Type.__name__=_K
_AristaBgp4V2PeerState_Object=MibTableColumn
aristaBgp4V2PeerState=_AristaBgp4V2PeerState_Object((1,3,6,1,4,1,30065,4,1,1,2,1,13),_AristaBgp4V2PeerState_Type())
aristaBgp4V2PeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerState.setStatus(_B)
_AristaBgp4V2PeerDescription_Type=SnmpAdminString
_AristaBgp4V2PeerDescription_Object=MibTableColumn
aristaBgp4V2PeerDescription=_AristaBgp4V2PeerDescription_Object((1,3,6,1,4,1,30065,4,1,1,2,1,14),_AristaBgp4V2PeerDescription_Type())
aristaBgp4V2PeerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerDescription.setStatus(_B)
class _AristaBgp4V2PeerPrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_AristaBgp4V2PeerPrevState_Type.__name__=_K
_AristaBgp4V2PeerPrevState_Object=MibTableColumn
aristaBgp4V2PeerPrevState=_AristaBgp4V2PeerPrevState_Object((1,3,6,1,4,1,30065,4,1,1,2,1,15),_AristaBgp4V2PeerPrevState_Type())
aristaBgp4V2PeerPrevState.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerPrevState.setStatus(_B)
_AristaBgp4V2PeerErrorsTable_Object=MibTable
aristaBgp4V2PeerErrorsTable=_AristaBgp4V2PeerErrorsTable_Object((1,3,6,1,4,1,30065,4,1,1,3))
if mibBuilder.loadTexts:aristaBgp4V2PeerErrorsTable.setStatus(_B)
_AristaBgp4V2PeerErrorsEntry_Object=MibTableRow
aristaBgp4V2PeerErrorsEntry=_AristaBgp4V2PeerErrorsEntry_Object((1,3,6,1,4,1,30065,4,1,1,3,1))
if mibBuilder.loadTexts:aristaBgp4V2PeerErrorsEntry.setStatus(_B)
class _AristaBgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AristaBgp4V2PeerLastErrorCodeReceived_Type.__name__=_D
_AristaBgp4V2PeerLastErrorCodeReceived_Object=MibTableColumn
aristaBgp4V2PeerLastErrorCodeReceived=_AristaBgp4V2PeerLastErrorCodeReceived_Object((1,3,6,1,4,1,30065,4,1,1,3,1,1),_AristaBgp4V2PeerLastErrorCodeReceived_Type())
aristaBgp4V2PeerLastErrorCodeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorCodeReceived.setStatus(_B)
class _AristaBgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AristaBgp4V2PeerLastErrorSubCodeReceived_Type.__name__=_D
_AristaBgp4V2PeerLastErrorSubCodeReceived_Object=MibTableColumn
aristaBgp4V2PeerLastErrorSubCodeReceived=_AristaBgp4V2PeerLastErrorSubCodeReceived_Object((1,3,6,1,4,1,30065,4,1,1,3,1,2),_AristaBgp4V2PeerLastErrorSubCodeReceived_Type())
aristaBgp4V2PeerLastErrorSubCodeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorSubCodeReceived.setStatus(_B)
_AristaBgp4V2PeerLastErrorReceivedTime_Type=TimeStamp
_AristaBgp4V2PeerLastErrorReceivedTime_Object=MibTableColumn
aristaBgp4V2PeerLastErrorReceivedTime=_AristaBgp4V2PeerLastErrorReceivedTime_Object((1,3,6,1,4,1,30065,4,1,1,3,1,3),_AristaBgp4V2PeerLastErrorReceivedTime_Type())
aristaBgp4V2PeerLastErrorReceivedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorReceivedTime.setStatus(_B)
_AristaBgp4V2PeerLastErrorReceivedText_Type=SnmpAdminString
_AristaBgp4V2PeerLastErrorReceivedText_Object=MibTableColumn
aristaBgp4V2PeerLastErrorReceivedText=_AristaBgp4V2PeerLastErrorReceivedText_Object((1,3,6,1,4,1,30065,4,1,1,3,1,4),_AristaBgp4V2PeerLastErrorReceivedText_Type())
aristaBgp4V2PeerLastErrorReceivedText.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorReceivedText.setStatus(_B)
class _AristaBgp4V2PeerLastErrorReceivedData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_AristaBgp4V2PeerLastErrorReceivedData_Type.__name__=_J
_AristaBgp4V2PeerLastErrorReceivedData_Object=MibTableColumn
aristaBgp4V2PeerLastErrorReceivedData=_AristaBgp4V2PeerLastErrorReceivedData_Object((1,3,6,1,4,1,30065,4,1,1,3,1,5),_AristaBgp4V2PeerLastErrorReceivedData_Type())
aristaBgp4V2PeerLastErrorReceivedData.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorReceivedData.setStatus(_B)
class _AristaBgp4V2PeerLastErrorCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AristaBgp4V2PeerLastErrorCodeSent_Type.__name__=_D
_AristaBgp4V2PeerLastErrorCodeSent_Object=MibTableColumn
aristaBgp4V2PeerLastErrorCodeSent=_AristaBgp4V2PeerLastErrorCodeSent_Object((1,3,6,1,4,1,30065,4,1,1,3,1,6),_AristaBgp4V2PeerLastErrorCodeSent_Type())
aristaBgp4V2PeerLastErrorCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorCodeSent.setStatus(_B)
class _AristaBgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AristaBgp4V2PeerLastErrorSubCodeSent_Type.__name__=_D
_AristaBgp4V2PeerLastErrorSubCodeSent_Object=MibTableColumn
aristaBgp4V2PeerLastErrorSubCodeSent=_AristaBgp4V2PeerLastErrorSubCodeSent_Object((1,3,6,1,4,1,30065,4,1,1,3,1,7),_AristaBgp4V2PeerLastErrorSubCodeSent_Type())
aristaBgp4V2PeerLastErrorSubCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorSubCodeSent.setStatus(_B)
_AristaBgp4V2PeerLastErrorSentTime_Type=TimeStamp
_AristaBgp4V2PeerLastErrorSentTime_Object=MibTableColumn
aristaBgp4V2PeerLastErrorSentTime=_AristaBgp4V2PeerLastErrorSentTime_Object((1,3,6,1,4,1,30065,4,1,1,3,1,8),_AristaBgp4V2PeerLastErrorSentTime_Type())
aristaBgp4V2PeerLastErrorSentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorSentTime.setStatus(_B)
_AristaBgp4V2PeerLastErrorSentText_Type=SnmpAdminString
_AristaBgp4V2PeerLastErrorSentText_Object=MibTableColumn
aristaBgp4V2PeerLastErrorSentText=_AristaBgp4V2PeerLastErrorSentText_Object((1,3,6,1,4,1,30065,4,1,1,3,1,9),_AristaBgp4V2PeerLastErrorSentText_Type())
aristaBgp4V2PeerLastErrorSentText.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorSentText.setStatus(_B)
class _AristaBgp4V2PeerLastErrorSentData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_AristaBgp4V2PeerLastErrorSentData_Type.__name__=_J
_AristaBgp4V2PeerLastErrorSentData_Object=MibTableColumn
aristaBgp4V2PeerLastErrorSentData=_AristaBgp4V2PeerLastErrorSentData_Object((1,3,6,1,4,1,30065,4,1,1,3,1,10),_AristaBgp4V2PeerLastErrorSentData_Type())
aristaBgp4V2PeerLastErrorSentData.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerLastErrorSentData.setStatus(_B)
_AristaBgp4V2PeerEventTimesTable_Object=MibTable
aristaBgp4V2PeerEventTimesTable=_AristaBgp4V2PeerEventTimesTable_Object((1,3,6,1,4,1,30065,4,1,1,4))
if mibBuilder.loadTexts:aristaBgp4V2PeerEventTimesTable.setStatus(_B)
_AristaBgp4V2PeerEventTimesEntry_Object=MibTableRow
aristaBgp4V2PeerEventTimesEntry=_AristaBgp4V2PeerEventTimesEntry_Object((1,3,6,1,4,1,30065,4,1,1,4,1))
if mibBuilder.loadTexts:aristaBgp4V2PeerEventTimesEntry.setStatus(_B)
_AristaBgp4V2PeerFsmEstablishedTime_Type=Gauge32
_AristaBgp4V2PeerFsmEstablishedTime_Object=MibTableColumn
aristaBgp4V2PeerFsmEstablishedTime=_AristaBgp4V2PeerFsmEstablishedTime_Object((1,3,6,1,4,1,30065,4,1,1,4,1,1),_AristaBgp4V2PeerFsmEstablishedTime_Type())
aristaBgp4V2PeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerFsmEstablishedTime.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerFsmEstablishedTime.setUnits(_F)
_AristaBgp4V2PeerInUpdatesElapsedTime_Type=Gauge32
_AristaBgp4V2PeerInUpdatesElapsedTime_Object=MibTableColumn
aristaBgp4V2PeerInUpdatesElapsedTime=_AristaBgp4V2PeerInUpdatesElapsedTime_Object((1,3,6,1,4,1,30065,4,1,1,4,1,2),_AristaBgp4V2PeerInUpdatesElapsedTime_Type())
aristaBgp4V2PeerInUpdatesElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerInUpdatesElapsedTime.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerInUpdatesElapsedTime.setUnits(_F)
_AristaBgp4V2PeerConfiguredTimersTable_Object=MibTable
aristaBgp4V2PeerConfiguredTimersTable=_AristaBgp4V2PeerConfiguredTimersTable_Object((1,3,6,1,4,1,30065,4,1,1,5))
if mibBuilder.loadTexts:aristaBgp4V2PeerConfiguredTimersTable.setStatus(_B)
_AristaBgp4V2PeerConfiguredTimersEntry_Object=MibTableRow
aristaBgp4V2PeerConfiguredTimersEntry=_AristaBgp4V2PeerConfiguredTimersEntry_Object((1,3,6,1,4,1,30065,4,1,1,5,1))
if mibBuilder.loadTexts:aristaBgp4V2PeerConfiguredTimersEntry.setStatus(_B)
class _AristaBgp4V2PeerConnectRetryInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AristaBgp4V2PeerConnectRetryInterval_Type.__name__=_D
_AristaBgp4V2PeerConnectRetryInterval_Object=MibTableColumn
aristaBgp4V2PeerConnectRetryInterval=_AristaBgp4V2PeerConnectRetryInterval_Object((1,3,6,1,4,1,30065,4,1,1,5,1,1),_AristaBgp4V2PeerConnectRetryInterval_Type())
aristaBgp4V2PeerConnectRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerConnectRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerConnectRetryInterval.setUnits(_F)
class _AristaBgp4V2PeerHoldTimeConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_AristaBgp4V2PeerHoldTimeConfigured_Type.__name__=_D
_AristaBgp4V2PeerHoldTimeConfigured_Object=MibTableColumn
aristaBgp4V2PeerHoldTimeConfigured=_AristaBgp4V2PeerHoldTimeConfigured_Object((1,3,6,1,4,1,30065,4,1,1,5,1,2),_AristaBgp4V2PeerHoldTimeConfigured_Type())
aristaBgp4V2PeerHoldTimeConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerHoldTimeConfigured.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerHoldTimeConfigured.setUnits(_F)
class _AristaBgp4V2PeerKeepAliveConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_AristaBgp4V2PeerKeepAliveConfigured_Type.__name__=_D
_AristaBgp4V2PeerKeepAliveConfigured_Object=MibTableColumn
aristaBgp4V2PeerKeepAliveConfigured=_AristaBgp4V2PeerKeepAliveConfigured_Object((1,3,6,1,4,1,30065,4,1,1,5,1,3),_AristaBgp4V2PeerKeepAliveConfigured_Type())
aristaBgp4V2PeerKeepAliveConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerKeepAliveConfigured.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerKeepAliveConfigured.setUnits(_F)
class _AristaBgp4V2PeerMinASOrigInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AristaBgp4V2PeerMinASOrigInterval_Type.__name__=_D
_AristaBgp4V2PeerMinASOrigInterval_Object=MibTableColumn
aristaBgp4V2PeerMinASOrigInterval=_AristaBgp4V2PeerMinASOrigInterval_Object((1,3,6,1,4,1,30065,4,1,1,5,1,4),_AristaBgp4V2PeerMinASOrigInterval_Type())
aristaBgp4V2PeerMinASOrigInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerMinASOrigInterval.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerMinASOrigInterval.setUnits(_F)
class _AristaBgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AristaBgp4V2PeerMinRouteAdverInterval_Type.__name__=_D
_AristaBgp4V2PeerMinRouteAdverInterval_Object=MibTableColumn
aristaBgp4V2PeerMinRouteAdverInterval=_AristaBgp4V2PeerMinRouteAdverInterval_Object((1,3,6,1,4,1,30065,4,1,1,5,1,5),_AristaBgp4V2PeerMinRouteAdverInterval_Type())
aristaBgp4V2PeerMinRouteAdverInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerMinRouteAdverInterval.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerMinRouteAdverInterval.setUnits(_F)
_AristaBgp4V2PeerNegotiatedTimersTable_Object=MibTable
aristaBgp4V2PeerNegotiatedTimersTable=_AristaBgp4V2PeerNegotiatedTimersTable_Object((1,3,6,1,4,1,30065,4,1,1,6))
if mibBuilder.loadTexts:aristaBgp4V2PeerNegotiatedTimersTable.setStatus(_B)
_AristaBgp4V2PeerNegotiatedTimersEntry_Object=MibTableRow
aristaBgp4V2PeerNegotiatedTimersEntry=_AristaBgp4V2PeerNegotiatedTimersEntry_Object((1,3,6,1,4,1,30065,4,1,1,6,1))
if mibBuilder.loadTexts:aristaBgp4V2PeerNegotiatedTimersEntry.setStatus(_B)
class _AristaBgp4V2PeerHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_AristaBgp4V2PeerHoldTime_Type.__name__=_D
_AristaBgp4V2PeerHoldTime_Object=MibTableColumn
aristaBgp4V2PeerHoldTime=_AristaBgp4V2PeerHoldTime_Object((1,3,6,1,4,1,30065,4,1,1,6,1,1),_AristaBgp4V2PeerHoldTime_Type())
aristaBgp4V2PeerHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerHoldTime.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerHoldTime.setUnits(_F)
class _AristaBgp4V2PeerKeepAlive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_AristaBgp4V2PeerKeepAlive_Type.__name__=_D
_AristaBgp4V2PeerKeepAlive_Object=MibTableColumn
aristaBgp4V2PeerKeepAlive=_AristaBgp4V2PeerKeepAlive_Object((1,3,6,1,4,1,30065,4,1,1,6,1,2),_AristaBgp4V2PeerKeepAlive_Type())
aristaBgp4V2PeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:aristaBgp4V2PeerKeepAlive.setUnits(_F)
_AristaBgp4V2PeerCountersTable_Object=MibTable
aristaBgp4V2PeerCountersTable=_AristaBgp4V2PeerCountersTable_Object((1,3,6,1,4,1,30065,4,1,1,7))
if mibBuilder.loadTexts:aristaBgp4V2PeerCountersTable.setStatus(_B)
_AristaBgp4V2PeerCountersEntry_Object=MibTableRow
aristaBgp4V2PeerCountersEntry=_AristaBgp4V2PeerCountersEntry_Object((1,3,6,1,4,1,30065,4,1,1,7,1))
if mibBuilder.loadTexts:aristaBgp4V2PeerCountersEntry.setStatus(_B)
_AristaBgp4V2PeerInUpdates_Type=Counter32
_AristaBgp4V2PeerInUpdates_Object=MibTableColumn
aristaBgp4V2PeerInUpdates=_AristaBgp4V2PeerInUpdates_Object((1,3,6,1,4,1,30065,4,1,1,7,1,1),_AristaBgp4V2PeerInUpdates_Type())
aristaBgp4V2PeerInUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerInUpdates.setStatus(_B)
_AristaBgp4V2PeerOutUpdates_Type=Counter32
_AristaBgp4V2PeerOutUpdates_Object=MibTableColumn
aristaBgp4V2PeerOutUpdates=_AristaBgp4V2PeerOutUpdates_Object((1,3,6,1,4,1,30065,4,1,1,7,1,2),_AristaBgp4V2PeerOutUpdates_Type())
aristaBgp4V2PeerOutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerOutUpdates.setStatus(_B)
_AristaBgp4V2PeerInTotalMessages_Type=Counter32
_AristaBgp4V2PeerInTotalMessages_Object=MibTableColumn
aristaBgp4V2PeerInTotalMessages=_AristaBgp4V2PeerInTotalMessages_Object((1,3,6,1,4,1,30065,4,1,1,7,1,3),_AristaBgp4V2PeerInTotalMessages_Type())
aristaBgp4V2PeerInTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerInTotalMessages.setStatus(_B)
_AristaBgp4V2PeerOutTotalMessages_Type=Counter32
_AristaBgp4V2PeerOutTotalMessages_Object=MibTableColumn
aristaBgp4V2PeerOutTotalMessages=_AristaBgp4V2PeerOutTotalMessages_Object((1,3,6,1,4,1,30065,4,1,1,7,1,4),_AristaBgp4V2PeerOutTotalMessages_Type())
aristaBgp4V2PeerOutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerOutTotalMessages.setStatus(_B)
_AristaBgp4V2PeerFsmEstablishedTransitions_Type=Counter32
_AristaBgp4V2PeerFsmEstablishedTransitions_Object=MibTableColumn
aristaBgp4V2PeerFsmEstablishedTransitions=_AristaBgp4V2PeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,30065,4,1,1,7,1,5),_AristaBgp4V2PeerFsmEstablishedTransitions_Type())
aristaBgp4V2PeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PeerFsmEstablishedTransitions.setStatus(_B)
_AristaBgp4V2PrefixGaugesTable_Object=MibTable
aristaBgp4V2PrefixGaugesTable=_AristaBgp4V2PrefixGaugesTable_Object((1,3,6,1,4,1,30065,4,1,1,8))
if mibBuilder.loadTexts:aristaBgp4V2PrefixGaugesTable.setStatus(_B)
_AristaBgp4V2PrefixGaugesEntry_Object=MibTableRow
aristaBgp4V2PrefixGaugesEntry=_AristaBgp4V2PrefixGaugesEntry_Object((1,3,6,1,4,1,30065,4,1,1,8,1))
aristaBgp4V2PrefixGaugesEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:aristaBgp4V2PrefixGaugesEntry.setStatus(_B)
_AristaBgp4V2PrefixGaugesAfi_Type=AristaBgp4V2AddressFamilyIdentifierTC
_AristaBgp4V2PrefixGaugesAfi_Object=MibTableColumn
aristaBgp4V2PrefixGaugesAfi=_AristaBgp4V2PrefixGaugesAfi_Object((1,3,6,1,4,1,30065,4,1,1,8,1,1),_AristaBgp4V2PrefixGaugesAfi_Type())
aristaBgp4V2PrefixGaugesAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2PrefixGaugesAfi.setStatus(_B)
_AristaBgp4V2PrefixGaugesSafi_Type=AristaBgp4V2SubsequentAddressFamilyIdentifierTC
_AristaBgp4V2PrefixGaugesSafi_Object=MibTableColumn
aristaBgp4V2PrefixGaugesSafi=_AristaBgp4V2PrefixGaugesSafi_Object((1,3,6,1,4,1,30065,4,1,1,8,1,2),_AristaBgp4V2PrefixGaugesSafi_Type())
aristaBgp4V2PrefixGaugesSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2PrefixGaugesSafi.setStatus(_B)
_AristaBgp4V2PrefixInPrefixes_Type=Gauge32
_AristaBgp4V2PrefixInPrefixes_Object=MibTableColumn
aristaBgp4V2PrefixInPrefixes=_AristaBgp4V2PrefixInPrefixes_Object((1,3,6,1,4,1,30065,4,1,1,8,1,3),_AristaBgp4V2PrefixInPrefixes_Type())
aristaBgp4V2PrefixInPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PrefixInPrefixes.setStatus(_B)
_AristaBgp4V2PrefixInPrefixesAccepted_Type=Gauge32
_AristaBgp4V2PrefixInPrefixesAccepted_Object=MibTableColumn
aristaBgp4V2PrefixInPrefixesAccepted=_AristaBgp4V2PrefixInPrefixesAccepted_Object((1,3,6,1,4,1,30065,4,1,1,8,1,4),_AristaBgp4V2PrefixInPrefixesAccepted_Type())
aristaBgp4V2PrefixInPrefixesAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PrefixInPrefixesAccepted.setStatus(_B)
_AristaBgp4V2PrefixOutPrefixes_Type=Gauge32
_AristaBgp4V2PrefixOutPrefixes_Object=MibTableColumn
aristaBgp4V2PrefixOutPrefixes=_AristaBgp4V2PrefixOutPrefixes_Object((1,3,6,1,4,1,30065,4,1,1,8,1,5),_AristaBgp4V2PrefixOutPrefixes_Type())
aristaBgp4V2PrefixOutPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PrefixOutPrefixes.setStatus(_B)
_AristaBgp4V2NlriTable_Object=MibTable
aristaBgp4V2NlriTable=_AristaBgp4V2NlriTable_Object((1,3,6,1,4,1,30065,4,1,1,9))
if mibBuilder.loadTexts:aristaBgp4V2NlriTable.setStatus(_B)
_AristaBgp4V2NlriEntry_Object=MibTableRow
aristaBgp4V2NlriEntry=_AristaBgp4V2NlriEntry_Object((1,3,6,1,4,1,30065,4,1,1,9,1))
aristaBgp4V2NlriEntry.setIndexNames((0,_A,_G),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_H),(0,_A,_I),(0,_A,_e))
if mibBuilder.loadTexts:aristaBgp4V2NlriEntry.setStatus(_B)
class _AristaBgp4V2NlriIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AristaBgp4V2NlriIndex_Type.__name__=_D
_AristaBgp4V2NlriIndex_Object=MibTableColumn
aristaBgp4V2NlriIndex=_AristaBgp4V2NlriIndex_Object((1,3,6,1,4,1,30065,4,1,1,9,1,1),_AristaBgp4V2NlriIndex_Type())
aristaBgp4V2NlriIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2NlriIndex.setStatus(_B)
_AristaBgp4V2NlriAfi_Type=AristaBgp4V2AddressFamilyIdentifierTC
_AristaBgp4V2NlriAfi_Object=MibTableColumn
aristaBgp4V2NlriAfi=_AristaBgp4V2NlriAfi_Object((1,3,6,1,4,1,30065,4,1,1,9,1,2),_AristaBgp4V2NlriAfi_Type())
aristaBgp4V2NlriAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2NlriAfi.setStatus(_B)
_AristaBgp4V2NlriSafi_Type=AristaBgp4V2SubsequentAddressFamilyIdentifierTC
_AristaBgp4V2NlriSafi_Object=MibTableColumn
aristaBgp4V2NlriSafi=_AristaBgp4V2NlriSafi_Object((1,3,6,1,4,1,30065,4,1,1,9,1,3),_AristaBgp4V2NlriSafi_Type())
aristaBgp4V2NlriSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2NlriSafi.setStatus(_B)
_AristaBgp4V2NlriPrefixType_Type=InetAddressType
_AristaBgp4V2NlriPrefixType_Object=MibTableColumn
aristaBgp4V2NlriPrefixType=_AristaBgp4V2NlriPrefixType_Object((1,3,6,1,4,1,30065,4,1,1,9,1,4),_AristaBgp4V2NlriPrefixType_Type())
aristaBgp4V2NlriPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2NlriPrefixType.setStatus(_B)
_AristaBgp4V2NlriPrefix_Type=InetAddress
_AristaBgp4V2NlriPrefix_Object=MibTableColumn
aristaBgp4V2NlriPrefix=_AristaBgp4V2NlriPrefix_Object((1,3,6,1,4,1,30065,4,1,1,9,1,5),_AristaBgp4V2NlriPrefix_Type())
aristaBgp4V2NlriPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2NlriPrefix.setStatus(_B)
_AristaBgp4V2NlriPrefixLen_Type=InetAddressPrefixLength
_AristaBgp4V2NlriPrefixLen_Object=MibTableColumn
aristaBgp4V2NlriPrefixLen=_AristaBgp4V2NlriPrefixLen_Object((1,3,6,1,4,1,30065,4,1,1,9,1,6),_AristaBgp4V2NlriPrefixLen_Type())
aristaBgp4V2NlriPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2NlriPrefixLen.setStatus(_B)
_AristaBgp4V2NlriBest_Type=TruthValue
_AristaBgp4V2NlriBest_Object=MibTableColumn
aristaBgp4V2NlriBest=_AristaBgp4V2NlriBest_Object((1,3,6,1,4,1,30065,4,1,1,9,1,7),_AristaBgp4V2NlriBest_Type())
aristaBgp4V2NlriBest.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriBest.setStatus(_B)
_AristaBgp4V2NlriCalcLocalPref_Type=Unsigned32
_AristaBgp4V2NlriCalcLocalPref_Object=MibTableColumn
aristaBgp4V2NlriCalcLocalPref=_AristaBgp4V2NlriCalcLocalPref_Object((1,3,6,1,4,1,30065,4,1,1,9,1,8),_AristaBgp4V2NlriCalcLocalPref_Type())
aristaBgp4V2NlriCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriCalcLocalPref.setStatus(_B)
class _AristaBgp4V2NlriOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_AristaBgp4V2NlriOrigin_Type.__name__=_K
_AristaBgp4V2NlriOrigin_Object=MibTableColumn
aristaBgp4V2NlriOrigin=_AristaBgp4V2NlriOrigin_Object((1,3,6,1,4,1,30065,4,1,1,9,1,9),_AristaBgp4V2NlriOrigin_Type())
aristaBgp4V2NlriOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriOrigin.setStatus(_B)
_AristaBgp4V2NlriNextHopAddrType_Type=InetAddressType
_AristaBgp4V2NlriNextHopAddrType_Object=MibTableColumn
aristaBgp4V2NlriNextHopAddrType=_AristaBgp4V2NlriNextHopAddrType_Object((1,3,6,1,4,1,30065,4,1,1,9,1,10),_AristaBgp4V2NlriNextHopAddrType_Type())
aristaBgp4V2NlriNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriNextHopAddrType.setStatus(_B)
class _AristaBgp4V2NlriNextHopAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_AristaBgp4V2NlriNextHopAddr_Type.__name__=_W
_AristaBgp4V2NlriNextHopAddr_Object=MibTableColumn
aristaBgp4V2NlriNextHopAddr=_AristaBgp4V2NlriNextHopAddr_Object((1,3,6,1,4,1,30065,4,1,1,9,1,11),_AristaBgp4V2NlriNextHopAddr_Type())
aristaBgp4V2NlriNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriNextHopAddr.setStatus(_B)
_AristaBgp4V2NlriLinkLocalNextHopAddrType_Type=InetAddressType
_AristaBgp4V2NlriLinkLocalNextHopAddrType_Object=MibTableColumn
aristaBgp4V2NlriLinkLocalNextHopAddrType=_AristaBgp4V2NlriLinkLocalNextHopAddrType_Object((1,3,6,1,4,1,30065,4,1,1,9,1,12),_AristaBgp4V2NlriLinkLocalNextHopAddrType_Type())
aristaBgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriLinkLocalNextHopAddrType.setStatus(_B)
_AristaBgp4V2NlriLinkLocalNextHopAddr_Type=InetAddress
_AristaBgp4V2NlriLinkLocalNextHopAddr_Object=MibTableColumn
aristaBgp4V2NlriLinkLocalNextHopAddr=_AristaBgp4V2NlriLinkLocalNextHopAddr_Object((1,3,6,1,4,1,30065,4,1,1,9,1,13),_AristaBgp4V2NlriLinkLocalNextHopAddr_Type())
aristaBgp4V2NlriLinkLocalNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriLinkLocalNextHopAddr.setStatus(_B)
_AristaBgp4V2NlriLocalPrefPresent_Type=TruthValue
_AristaBgp4V2NlriLocalPrefPresent_Object=MibTableColumn
aristaBgp4V2NlriLocalPrefPresent=_AristaBgp4V2NlriLocalPrefPresent_Object((1,3,6,1,4,1,30065,4,1,1,9,1,14),_AristaBgp4V2NlriLocalPrefPresent_Type())
aristaBgp4V2NlriLocalPrefPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriLocalPrefPresent.setStatus(_B)
_AristaBgp4V2NlriLocalPref_Type=Unsigned32
_AristaBgp4V2NlriLocalPref_Object=MibTableColumn
aristaBgp4V2NlriLocalPref=_AristaBgp4V2NlriLocalPref_Object((1,3,6,1,4,1,30065,4,1,1,9,1,15),_AristaBgp4V2NlriLocalPref_Type())
aristaBgp4V2NlriLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriLocalPref.setStatus(_B)
_AristaBgp4V2NlriMedPresent_Type=TruthValue
_AristaBgp4V2NlriMedPresent_Object=MibTableColumn
aristaBgp4V2NlriMedPresent=_AristaBgp4V2NlriMedPresent_Object((1,3,6,1,4,1,30065,4,1,1,9,1,16),_AristaBgp4V2NlriMedPresent_Type())
aristaBgp4V2NlriMedPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriMedPresent.setStatus(_B)
_AristaBgp4V2NlriMed_Type=Unsigned32
_AristaBgp4V2NlriMed_Object=MibTableColumn
aristaBgp4V2NlriMed=_AristaBgp4V2NlriMed_Object((1,3,6,1,4,1,30065,4,1,1,9,1,17),_AristaBgp4V2NlriMed_Type())
aristaBgp4V2NlriMed.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriMed.setStatus(_B)
_AristaBgp4V2NlriAtomicAggregate_Type=TruthValue
_AristaBgp4V2NlriAtomicAggregate_Object=MibTableColumn
aristaBgp4V2NlriAtomicAggregate=_AristaBgp4V2NlriAtomicAggregate_Object((1,3,6,1,4,1,30065,4,1,1,9,1,18),_AristaBgp4V2NlriAtomicAggregate_Type())
aristaBgp4V2NlriAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAtomicAggregate.setStatus(_B)
_AristaBgp4V2NlriAggregatorPresent_Type=TruthValue
_AristaBgp4V2NlriAggregatorPresent_Object=MibTableColumn
aristaBgp4V2NlriAggregatorPresent=_AristaBgp4V2NlriAggregatorPresent_Object((1,3,6,1,4,1,30065,4,1,1,9,1,19),_AristaBgp4V2NlriAggregatorPresent_Type())
aristaBgp4V2NlriAggregatorPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAggregatorPresent.setStatus(_B)
_AristaBgp4V2NlriAggregatorAS_Type=InetAutonomousSystemNumber
_AristaBgp4V2NlriAggregatorAS_Object=MibTableColumn
aristaBgp4V2NlriAggregatorAS=_AristaBgp4V2NlriAggregatorAS_Object((1,3,6,1,4,1,30065,4,1,1,9,1,20),_AristaBgp4V2NlriAggregatorAS_Type())
aristaBgp4V2NlriAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAggregatorAS.setStatus(_B)
_AristaBgp4V2NlriAggregatorAddr_Type=AristaBgp4V2IdentifierTC
_AristaBgp4V2NlriAggregatorAddr_Object=MibTableColumn
aristaBgp4V2NlriAggregatorAddr=_AristaBgp4V2NlriAggregatorAddr_Object((1,3,6,1,4,1,30065,4,1,1,9,1,21),_AristaBgp4V2NlriAggregatorAddr_Type())
aristaBgp4V2NlriAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAggregatorAddr.setStatus(_B)
_AristaBgp4V2NlriAsPathCalcLength_Type=Unsigned32
_AristaBgp4V2NlriAsPathCalcLength_Object=MibTableColumn
aristaBgp4V2NlriAsPathCalcLength=_AristaBgp4V2NlriAsPathCalcLength_Object((1,3,6,1,4,1,30065,4,1,1,9,1,22),_AristaBgp4V2NlriAsPathCalcLength_Type())
aristaBgp4V2NlriAsPathCalcLength.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAsPathCalcLength.setStatus(_B)
_AristaBgp4V2NlriAsPathString_Type=SnmpAdminString
_AristaBgp4V2NlriAsPathString_Object=MibTableColumn
aristaBgp4V2NlriAsPathString=_AristaBgp4V2NlriAsPathString_Object((1,3,6,1,4,1,30065,4,1,1,9,1,23),_AristaBgp4V2NlriAsPathString_Type())
aristaBgp4V2NlriAsPathString.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAsPathString.setStatus(_B)
class _AristaBgp4V2NlriAsPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4072))
_AristaBgp4V2NlriAsPath_Type.__name__=_J
_AristaBgp4V2NlriAsPath_Object=MibTableColumn
aristaBgp4V2NlriAsPath=_AristaBgp4V2NlriAsPath_Object((1,3,6,1,4,1,30065,4,1,1,9,1,24),_AristaBgp4V2NlriAsPath_Type())
aristaBgp4V2NlriAsPath.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriAsPath.setStatus(_B)
class _AristaBgp4V2NlriPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4072))
_AristaBgp4V2NlriPathAttrUnknown_Type.__name__=_J
_AristaBgp4V2NlriPathAttrUnknown_Object=MibTableColumn
aristaBgp4V2NlriPathAttrUnknown=_AristaBgp4V2NlriPathAttrUnknown_Object((1,3,6,1,4,1,30065,4,1,1,9,1,25),_AristaBgp4V2NlriPathAttrUnknown_Type())
aristaBgp4V2NlriPathAttrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2NlriPathAttrUnknown.setStatus(_B)
_AristaBgp4V2AdjRibsOutTable_Object=MibTable
aristaBgp4V2AdjRibsOutTable=_AristaBgp4V2AdjRibsOutTable_Object((1,3,6,1,4,1,30065,4,1,1,10))
if mibBuilder.loadTexts:aristaBgp4V2AdjRibsOutTable.setStatus(_B)
_AristaBgp4V2AdjRibsOutEntry_Object=MibTableRow
aristaBgp4V2AdjRibsOutEntry=_AristaBgp4V2AdjRibsOutEntry_Object((1,3,6,1,4,1,30065,4,1,1,10,1))
aristaBgp4V2AdjRibsOutEntry.setIndexNames((0,_A,_G),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_H),(0,_A,_I),(0,_A,_f))
if mibBuilder.loadTexts:aristaBgp4V2AdjRibsOutEntry.setStatus(_B)
class _AristaBgp4V2AdjRibsOutIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AristaBgp4V2AdjRibsOutIndex_Type.__name__=_D
_AristaBgp4V2AdjRibsOutIndex_Object=MibTableColumn
aristaBgp4V2AdjRibsOutIndex=_AristaBgp4V2AdjRibsOutIndex_Object((1,3,6,1,4,1,30065,4,1,1,10,1,1),_AristaBgp4V2AdjRibsOutIndex_Type())
aristaBgp4V2AdjRibsOutIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2AdjRibsOutIndex.setStatus(_B)
_AristaBgp4V2AdjRibsOutRoute_Type=RowPointer
_AristaBgp4V2AdjRibsOutRoute_Object=MibTableColumn
aristaBgp4V2AdjRibsOutRoute=_AristaBgp4V2AdjRibsOutRoute_Object((1,3,6,1,4,1,30065,4,1,1,10,1,2),_AristaBgp4V2AdjRibsOutRoute_Type())
aristaBgp4V2AdjRibsOutRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2AdjRibsOutRoute.setStatus(_B)
_AristaBgp4V2PrefixEvpnNlriGaugesTable_Object=MibTable
aristaBgp4V2PrefixEvpnNlriGaugesTable=_AristaBgp4V2PrefixEvpnNlriGaugesTable_Object((1,3,6,1,4,1,30065,4,1,1,11))
if mibBuilder.loadTexts:aristaBgp4V2PrefixEvpnNlriGaugesTable.setStatus(_B)
_AristaBgp4V2PrefixEvpnNlriGaugesEntry_Object=MibTableRow
aristaBgp4V2PrefixEvpnNlriGaugesEntry=_AristaBgp4V2PrefixEvpnNlriGaugesEntry_Object((1,3,6,1,4,1,30065,4,1,1,11,1))
aristaBgp4V2PrefixEvpnNlriGaugesEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_g))
if mibBuilder.loadTexts:aristaBgp4V2PrefixEvpnNlriGaugesEntry.setStatus(_B)
_AristaBgp4V2PrefixGaugesNlri_Type=AristaBgp4V2EvpnNlriTC
_AristaBgp4V2PrefixGaugesNlri_Object=MibTableColumn
aristaBgp4V2PrefixGaugesNlri=_AristaBgp4V2PrefixGaugesNlri_Object((1,3,6,1,4,1,30065,4,1,1,11,1,1),_AristaBgp4V2PrefixGaugesNlri_Type())
aristaBgp4V2PrefixGaugesNlri.setMaxAccess(_E)
if mibBuilder.loadTexts:aristaBgp4V2PrefixGaugesNlri.setStatus(_B)
_AristaBgp4V2PrefixNlriInPrefixes_Type=Gauge32
_AristaBgp4V2PrefixNlriInPrefixes_Object=MibTableColumn
aristaBgp4V2PrefixNlriInPrefixes=_AristaBgp4V2PrefixNlriInPrefixes_Object((1,3,6,1,4,1,30065,4,1,1,11,1,2),_AristaBgp4V2PrefixNlriInPrefixes_Type())
aristaBgp4V2PrefixNlriInPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PrefixNlriInPrefixes.setStatus(_B)
_AristaBgp4V2PrefixNlriInPrefixesAccepted_Type=Gauge32
_AristaBgp4V2PrefixNlriInPrefixesAccepted_Object=MibTableColumn
aristaBgp4V2PrefixNlriInPrefixesAccepted=_AristaBgp4V2PrefixNlriInPrefixesAccepted_Object((1,3,6,1,4,1,30065,4,1,1,11,1,3),_AristaBgp4V2PrefixNlriInPrefixesAccepted_Type())
aristaBgp4V2PrefixNlriInPrefixesAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaBgp4V2PrefixNlriInPrefixesAccepted.setStatus(_B)
_AristaBgp4V2Conformance_ObjectIdentity=ObjectIdentity
aristaBgp4V2Conformance=_AristaBgp4V2Conformance_ObjectIdentity((1,3,6,1,4,1,30065,4,1,2))
_AristaBgp4V2Compliances_ObjectIdentity=ObjectIdentity
aristaBgp4V2Compliances=_AristaBgp4V2Compliances_ObjectIdentity((1,3,6,1,4,1,30065,4,1,2,1))
_AristaBgp4V2Groups_ObjectIdentity=ObjectIdentity
aristaBgp4V2Groups=_AristaBgp4V2Groups_ObjectIdentity((1,3,6,1,4,1,30065,4,1,2,2))
aristaBgp4V2PeerEntry.registerAugmentions((_A,_h))
aristaBgp4V2PeerErrorsEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions((_A,_i))
aristaBgp4V2PeerEventTimesEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions((_A,_j))
aristaBgp4V2PeerConfiguredTimersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions((_A,_k))
aristaBgp4V2PeerNegotiatedTimersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2PeerEntry.registerAugmentions((_A,_l))
aristaBgp4V2PeerCountersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
aristaBgp4V2GlobalsGroup=ObjectGroup((1,3,6,1,4,1,30065,4,1,2,2,1))
aristaBgp4V2GlobalsGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:aristaBgp4V2GlobalsGroup.setStatus(_B)
aristaBgp4V2StdMIBTimersGroup=ObjectGroup((1,3,6,1,4,1,30065,4,1,2,2,2))
aristaBgp4V2StdMIBTimersGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:aristaBgp4V2StdMIBTimersGroup.setStatus(_B)
aristaBgp4V2StdMIBCountersGroup=ObjectGroup((1,3,6,1,4,1,30065,4,1,2,2,3))
aristaBgp4V2StdMIBCountersGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:aristaBgp4V2StdMIBCountersGroup.setStatus(_B)
aristaBgp4V2StdMIBErrorsGroup=ObjectGroup((1,3,6,1,4,1,30065,4,1,2,2,5))
aristaBgp4V2StdMIBErrorsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_A6),(_A,_A7),(_A,_V),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:aristaBgp4V2StdMIBErrorsGroup.setStatus(_B)
aristaBgp4V2StdMIBPeerGroup=ObjectGroup((1,3,6,1,4,1,30065,4,1,2,2,6))
aristaBgp4V2StdMIBPeerGroup.setObjects(*((_A,_L),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_M),(_A,_AG),(_A,_N),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:aristaBgp4V2StdMIBPeerGroup.setStatus(_B)
aristaBgp4V2StdMIBNlriGroup=ObjectGroup((1,3,6,1,4,1,30065,4,1,2,2,7))
aristaBgp4V2StdMIBNlriGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:aristaBgp4V2StdMIBNlriGroup.setStatus(_B)
aristaBgp4V2EstablishedNotification=NotificationType((1,3,6,1,4,1,30065,4,1,0,1))
aristaBgp4V2EstablishedNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:aristaBgp4V2EstablishedNotification.setStatus(_B)
aristaBgp4V2BackwardTransitionNotification=NotificationType((1,3,6,1,4,1,30065,4,1,0,2))
aristaBgp4V2BackwardTransitionNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:aristaBgp4V2BackwardTransitionNotification.setStatus(_B)
aristaBgp4V2StdMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,30065,4,1,2,2,8))
aristaBgp4V2StdMIBNotificationGroup.setObjects(*((_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:aristaBgp4V2StdMIBNotificationGroup.setStatus(_B)
aristaBgp4V2Compliance=ModuleCompliance((1,3,6,1,4,1,30065,4,1,2,1,4))
aristaBgp4V2Compliance.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:aristaBgp4V2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'aristaBgp4V2':aristaBgp4V2,'aristaBgp4V2Notifications':aristaBgp4V2Notifications,_Ag:aristaBgp4V2EstablishedNotification,_Ah:aristaBgp4V2BackwardTransitionNotification,'aristaBgp4V2Objects':aristaBgp4V2Objects,'aristaBgp4V2DiscontinuityTable':aristaBgp4V2DiscontinuityTable,'aristaBgp4V2DiscontinuityEntry':aristaBgp4V2DiscontinuityEntry,_m:aristaBgp4V2DiscontinuityTime,'aristaBgp4V2PeerTable':aristaBgp4V2PeerTable,'aristaBgp4V2PeerEntry':aristaBgp4V2PeerEntry,_G:aristaBgp4V2PeerInstance,_AE:aristaBgp4V2PeerLocalAddrType,_AF:aristaBgp4V2PeerLocalAddr,_H:aristaBgp4V2PeerRemoteAddrType,_I:aristaBgp4V2PeerRemoteAddr,_M:aristaBgp4V2PeerLocalPort,_AG:aristaBgp4V2PeerLocalAs,_AI:aristaBgp4V2PeerLocalIdentifier,_N:aristaBgp4V2PeerRemotePort,_AH:aristaBgp4V2PeerRemoteAs,_AJ:aristaBgp4V2PeerRemoteIdentifier,_AD:aristaBgp4V2PeerAdminStatus,_L:aristaBgp4V2PeerState,_AK:aristaBgp4V2PeerDescription,_AL:aristaBgp4V2PeerPrevState,'aristaBgp4V2PeerErrorsTable':aristaBgp4V2PeerErrorsTable,_h:aristaBgp4V2PeerErrorsEntry,_T:aristaBgp4V2PeerLastErrorCodeReceived,_U:aristaBgp4V2PeerLastErrorSubCodeReceived,_A7:aristaBgp4V2PeerLastErrorReceivedTime,_V:aristaBgp4V2PeerLastErrorReceivedText,_A6:aristaBgp4V2PeerLastErrorReceivedData,_A8:aristaBgp4V2PeerLastErrorCodeSent,_A9:aristaBgp4V2PeerLastErrorSubCodeSent,_AB:aristaBgp4V2PeerLastErrorSentTime,_AC:aristaBgp4V2PeerLastErrorSentText,_AA:aristaBgp4V2PeerLastErrorSentData,'aristaBgp4V2PeerEventTimesTable':aristaBgp4V2PeerEventTimesTable,_i:aristaBgp4V2PeerEventTimesEntry,_n:aristaBgp4V2PeerFsmEstablishedTime,_o:aristaBgp4V2PeerInUpdatesElapsedTime,'aristaBgp4V2PeerConfiguredTimersTable':aristaBgp4V2PeerConfiguredTimersTable,_j:aristaBgp4V2PeerConfiguredTimersEntry,_p:aristaBgp4V2PeerConnectRetryInterval,_q:aristaBgp4V2PeerHoldTimeConfigured,_r:aristaBgp4V2PeerKeepAliveConfigured,_s:aristaBgp4V2PeerMinASOrigInterval,_t:aristaBgp4V2PeerMinRouteAdverInterval,'aristaBgp4V2PeerNegotiatedTimersTable':aristaBgp4V2PeerNegotiatedTimersTable,_k:aristaBgp4V2PeerNegotiatedTimersEntry,_u:aristaBgp4V2PeerHoldTime,_v:aristaBgp4V2PeerKeepAlive,'aristaBgp4V2PeerCountersTable':aristaBgp4V2PeerCountersTable,_l:aristaBgp4V2PeerCountersEntry,_w:aristaBgp4V2PeerInUpdates,_x:aristaBgp4V2PeerOutUpdates,_y:aristaBgp4V2PeerInTotalMessages,_z:aristaBgp4V2PeerOutTotalMessages,_A0:aristaBgp4V2PeerFsmEstablishedTransitions,'aristaBgp4V2PrefixGaugesTable':aristaBgp4V2PrefixGaugesTable,'aristaBgp4V2PrefixGaugesEntry':aristaBgp4V2PrefixGaugesEntry,_c:aristaBgp4V2PrefixGaugesAfi,_d:aristaBgp4V2PrefixGaugesSafi,_A1:aristaBgp4V2PrefixInPrefixes,_A2:aristaBgp4V2PrefixInPrefixesAccepted,_A3:aristaBgp4V2PrefixOutPrefixes,'aristaBgp4V2NlriTable':aristaBgp4V2NlriTable,'aristaBgp4V2NlriEntry':aristaBgp4V2NlriEntry,_e:aristaBgp4V2NlriIndex,_O:aristaBgp4V2NlriAfi,_P:aristaBgp4V2NlriSafi,_Q:aristaBgp4V2NlriPrefixType,_R:aristaBgp4V2NlriPrefix,_S:aristaBgp4V2NlriPrefixLen,_AO:aristaBgp4V2NlriBest,_AP:aristaBgp4V2NlriCalcLocalPref,_Ad:aristaBgp4V2NlriOrigin,_Aa:aristaBgp4V2NlriNextHopAddrType,_AZ:aristaBgp4V2NlriNextHopAddr,_Ab:aristaBgp4V2NlriLinkLocalNextHopAddrType,_Ac:aristaBgp4V2NlriLinkLocalNextHopAddr,_AW:aristaBgp4V2NlriLocalPrefPresent,_AV:aristaBgp4V2NlriLocalPref,_AY:aristaBgp4V2NlriMedPresent,_AX:aristaBgp4V2NlriMed,_AU:aristaBgp4V2NlriAtomicAggregate,_AR:aristaBgp4V2NlriAggregatorPresent,_AS:aristaBgp4V2NlriAggregatorAS,_AT:aristaBgp4V2NlriAggregatorAddr,_AM:aristaBgp4V2NlriAsPathCalcLength,_AN:aristaBgp4V2NlriAsPathString,_Ae:aristaBgp4V2NlriAsPath,_Af:aristaBgp4V2NlriPathAttrUnknown,'aristaBgp4V2AdjRibsOutTable':aristaBgp4V2AdjRibsOutTable,'aristaBgp4V2AdjRibsOutEntry':aristaBgp4V2AdjRibsOutEntry,_f:aristaBgp4V2AdjRibsOutIndex,_AQ:aristaBgp4V2AdjRibsOutRoute,'aristaBgp4V2PrefixEvpnNlriGaugesTable':aristaBgp4V2PrefixEvpnNlriGaugesTable,'aristaBgp4V2PrefixEvpnNlriGaugesEntry':aristaBgp4V2PrefixEvpnNlriGaugesEntry,_g:aristaBgp4V2PrefixGaugesNlri,_A4:aristaBgp4V2PrefixNlriInPrefixes,_A5:aristaBgp4V2PrefixNlriInPrefixesAccepted,'aristaBgp4V2Conformance':aristaBgp4V2Conformance,'aristaBgp4V2Compliances':aristaBgp4V2Compliances,'aristaBgp4V2Compliance':aristaBgp4V2Compliance,'aristaBgp4V2Groups':aristaBgp4V2Groups,_An:aristaBgp4V2GlobalsGroup,_Ai:aristaBgp4V2StdMIBTimersGroup,_Aj:aristaBgp4V2StdMIBCountersGroup,_Ak:aristaBgp4V2StdMIBErrorsGroup,_Al:aristaBgp4V2StdMIBPeerGroup,_Am:aristaBgp4V2StdMIBNlriGroup,_Ao:aristaBgp4V2StdMIBNotificationGroup})