_Af='bgp4V2StdMIBNotificationGroup'
_Ae='bgp4V2GlobalsGroup'
_Ad='bgp4V2StdMIBNlriGroup'
_Ac='bgp4V2StdMIBPeerGroup'
_Ab='bgp4V2StdMIBErrorsGroup'
_Aa='bgp4V2StdMIBCountersGroup'
_AZ='bgp4V2StdMIBTimersGroup'
_AY='bgp4V2BackwardTransitionNotification'
_AX='bgp4V2EstablishedNotification'
_AW='bgp4V2NlriPathAttrUnknown'
_AV='bgp4V2NlriAsPath'
_AU='bgp4V2NlriOrigin'
_AT='bgp4V2NlriLinkLocalNextHopAddr'
_AS='bgp4V2NlriLinkLocalNextHopAddrType'
_AR='bgp4V2NlriNextHopAddrType'
_AQ='bgp4V2NlriNextHopAddr'
_AP='bgp4V2NlriMedPresent'
_AO='bgp4V2NlriMed'
_AN='bgp4V2NlriLocalPrefPresent'
_AM='bgp4V2NlriLocalPref'
_AL='bgp4V2NlriAtomicAggregate'
_AK='bgp4V2NlriAggregatorAddr'
_AJ='bgp4V2NlriAggregatorAS'
_AI='bgp4V2NlriAggregatorPresent'
_AH='bgp4V2AdjRibsOutRoute'
_AG='bgp4V2NlriCalcLocalPref'
_AF='bgp4V2NlriBest'
_AE='bgp4V2NlriAsPathString'
_AD='bgp4V2NlriAsPathCalcLength'
_AC='bgp4V2PeerDescription'
_AB='bgp4V2PeerRemoteIdentifier'
_AA='bgp4V2PeerLocalIdentifier'
_A9='bgp4V2PeerRemoteAs'
_A8='bgp4V2PeerLocalAs'
_A7='bgp4V2PeerLocalAddr'
_A6='bgp4V2PeerLocalAddrType'
_A5='bgp4V2PeerAdminStatus'
_A4='bgp4V2PeerLastErrorSentText'
_A3='bgp4V2PeerLastErrorSentTime'
_A2='bgp4V2PeerLastErrorSentData'
_A1='bgp4V2PeerLastErrorSubCodeSent'
_A0='bgp4V2PeerLastErrorCodeSent'
_z='bgp4V2PeerLastErrorReceivedTime'
_y='bgp4V2PeerLastErrorReceivedData'
_x='bgp4V2PrefixOutPrefixes'
_w='bgp4V2PrefixInPrefixesAccepted'
_v='bgp4V2PrefixInPrefixes'
_u='bgp4V2PeerFsmEstablishedTransitions'
_t='bgp4V2PeerOutTotalMessages'
_s='bgp4V2PeerInTotalMessages'
_r='bgp4V2PeerOutUpdates'
_q='bgp4V2PeerInUpdates'
_p='bgp4V2PeerKeepAlive'
_o='bgp4V2PeerHoldTime'
_n='bgp4V2PeerMinRouteAdverInterval'
_m='bgp4V2PeerMinASOrigInterval'
_l='bgp4V2PeerKeepAliveConfigured'
_k='bgp4V2PeerHoldTimeConfigured'
_j='bgp4V2PeerConnectRetryInterval'
_i='bgp4V2PeerInUpdatesElapsedTime'
_h='bgp4V2PeerFsmEstablishedTime'
_g='bgp4V2DiscontinuityTime'
_f='bgp4V2PeerCountersEntry'
_e='bgp4V2PeerNegotiatedTimersEntry'
_d='bgp4V2PeerConfiguredTimersEntry'
_c='bgp4V2PeerEventTimesEntry'
_b='bgp4V2PeerErrorsEntry'
_a='bgp4V2AdjRibsOutIndex'
_Z='bgp4V2NlriIndex'
_Y='bgp4V2PrefixGaugesSafi'
_X='bgp4V2PrefixGaugesAfi'
_W='InetAddress'
_V='bgp4V2PeerLastErrorReceivedText'
_U='bgp4V2PeerLastErrorSubCodeReceived'
_T='bgp4V2PeerLastErrorCodeReceived'
_S='bgp4V2NlriPrefixLen'
_R='bgp4V2NlriPrefix'
_Q='bgp4V2NlriPrefixType'
_P='bgp4V2NlriSafi'
_O='bgp4V2NlriAfi'
_N='bgp4V2PeerRemotePort'
_M='bgp4V2PeerLocalPort'
_L='bgp4V2PeerState'
_K='Integer32'
_J='bgp4V2PeerRemoteAddr'
_I='bgp4V2PeerRemoteAddrType'
_H='OctetString'
_G='bgp4V2PeerInstance'
_F='seconds'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='BGP4V2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Bgp4V2AddressFamilyIdentifierTC,Bgp4V2IdentifierTC,Bgp4V2SubsequentAddressFamilyIdentifierTC,frr=mibBuilder.importSymbols('BGP4V2-TC-MIB','Bgp4V2AddressFamilyIdentifierTC','Bgp4V2IdentifierTC','Bgp4V2SubsequentAddressFamilyIdentifierTC','frr')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,'InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
bgp4V2=ModuleIdentity((1,3,6,1,3,5,1))
if mibBuilder.loadTexts:bgp4V2.setRevisions(('2014-01-24 00:00',))
_Bgp4V2Notifications_ObjectIdentity=ObjectIdentity
bgp4V2Notifications=_Bgp4V2Notifications_ObjectIdentity((1,3,6,1,3,5,1,0))
_Bgp4V2Objects_ObjectIdentity=ObjectIdentity
bgp4V2Objects=_Bgp4V2Objects_ObjectIdentity((1,3,6,1,3,5,1,1))
_Bgp4V2DiscontinuityTable_Object=MibTable
bgp4V2DiscontinuityTable=_Bgp4V2DiscontinuityTable_Object((1,3,6,1,3,5,1,1,1))
if mibBuilder.loadTexts:bgp4V2DiscontinuityTable.setStatus(_B)
_Bgp4V2DiscontinuityEntry_Object=MibTableRow
bgp4V2DiscontinuityEntry=_Bgp4V2DiscontinuityEntry_Object((1,3,6,1,3,5,1,1,1,1))
bgp4V2DiscontinuityEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:bgp4V2DiscontinuityEntry.setStatus(_B)
_Bgp4V2DiscontinuityTime_Type=TimeStamp
_Bgp4V2DiscontinuityTime_Object=MibTableColumn
bgp4V2DiscontinuityTime=_Bgp4V2DiscontinuityTime_Object((1,3,6,1,3,5,1,1,1,1,1),_Bgp4V2DiscontinuityTime_Type())
bgp4V2DiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2DiscontinuityTime.setStatus(_B)
_Bgp4V2PeerTable_Object=MibTable
bgp4V2PeerTable=_Bgp4V2PeerTable_Object((1,3,6,1,3,5,1,1,2))
if mibBuilder.loadTexts:bgp4V2PeerTable.setStatus(_B)
_Bgp4V2PeerEntry_Object=MibTableRow
bgp4V2PeerEntry=_Bgp4V2PeerEntry_Object((1,3,6,1,3,5,1,1,2,1))
bgp4V2PeerEntry.setIndexNames((0,_A,_G),(0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:bgp4V2PeerEntry.setStatus(_B)
class _Bgp4V2PeerInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Bgp4V2PeerInstance_Type.__name__=_D
_Bgp4V2PeerInstance_Object=MibTableColumn
bgp4V2PeerInstance=_Bgp4V2PeerInstance_Object((1,3,6,1,3,5,1,1,2,1,1),_Bgp4V2PeerInstance_Type())
bgp4V2PeerInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2PeerInstance.setStatus(_B)
_Bgp4V2PeerLocalAddrType_Type=InetAddressType
_Bgp4V2PeerLocalAddrType_Object=MibTableColumn
bgp4V2PeerLocalAddrType=_Bgp4V2PeerLocalAddrType_Object((1,3,6,1,3,5,1,1,2,1,2),_Bgp4V2PeerLocalAddrType_Type())
bgp4V2PeerLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLocalAddrType.setStatus(_B)
_Bgp4V2PeerLocalAddr_Type=InetAddress
_Bgp4V2PeerLocalAddr_Object=MibTableColumn
bgp4V2PeerLocalAddr=_Bgp4V2PeerLocalAddr_Object((1,3,6,1,3,5,1,1,2,1,3),_Bgp4V2PeerLocalAddr_Type())
bgp4V2PeerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLocalAddr.setStatus(_B)
_Bgp4V2PeerRemoteAddrType_Type=InetAddressType
_Bgp4V2PeerRemoteAddrType_Object=MibTableColumn
bgp4V2PeerRemoteAddrType=_Bgp4V2PeerRemoteAddrType_Object((1,3,6,1,3,5,1,1,2,1,4),_Bgp4V2PeerRemoteAddrType_Type())
bgp4V2PeerRemoteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2PeerRemoteAddrType.setStatus(_B)
_Bgp4V2PeerRemoteAddr_Type=InetAddress
_Bgp4V2PeerRemoteAddr_Object=MibTableColumn
bgp4V2PeerRemoteAddr=_Bgp4V2PeerRemoteAddr_Object((1,3,6,1,3,5,1,1,2,1,5),_Bgp4V2PeerRemoteAddr_Type())
bgp4V2PeerRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2PeerRemoteAddr.setStatus(_B)
_Bgp4V2PeerLocalPort_Type=InetPortNumber
_Bgp4V2PeerLocalPort_Object=MibTableColumn
bgp4V2PeerLocalPort=_Bgp4V2PeerLocalPort_Object((1,3,6,1,3,5,1,1,2,1,6),_Bgp4V2PeerLocalPort_Type())
bgp4V2PeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLocalPort.setStatus(_B)
_Bgp4V2PeerLocalAs_Type=InetAutonomousSystemNumber
_Bgp4V2PeerLocalAs_Object=MibTableColumn
bgp4V2PeerLocalAs=_Bgp4V2PeerLocalAs_Object((1,3,6,1,3,5,1,1,2,1,7),_Bgp4V2PeerLocalAs_Type())
bgp4V2PeerLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLocalAs.setStatus(_B)
_Bgp4V2PeerLocalIdentifier_Type=Bgp4V2IdentifierTC
_Bgp4V2PeerLocalIdentifier_Object=MibTableColumn
bgp4V2PeerLocalIdentifier=_Bgp4V2PeerLocalIdentifier_Object((1,3,6,1,3,5,1,1,2,1,8),_Bgp4V2PeerLocalIdentifier_Type())
bgp4V2PeerLocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLocalIdentifier.setStatus(_B)
_Bgp4V2PeerRemotePort_Type=InetPortNumber
_Bgp4V2PeerRemotePort_Object=MibTableColumn
bgp4V2PeerRemotePort=_Bgp4V2PeerRemotePort_Object((1,3,6,1,3,5,1,1,2,1,9),_Bgp4V2PeerRemotePort_Type())
bgp4V2PeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerRemotePort.setStatus(_B)
_Bgp4V2PeerRemoteAs_Type=InetAutonomousSystemNumber
_Bgp4V2PeerRemoteAs_Object=MibTableColumn
bgp4V2PeerRemoteAs=_Bgp4V2PeerRemoteAs_Object((1,3,6,1,3,5,1,1,2,1,10),_Bgp4V2PeerRemoteAs_Type())
bgp4V2PeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerRemoteAs.setStatus(_B)
_Bgp4V2PeerRemoteIdentifier_Type=Bgp4V2IdentifierTC
_Bgp4V2PeerRemoteIdentifier_Object=MibTableColumn
bgp4V2PeerRemoteIdentifier=_Bgp4V2PeerRemoteIdentifier_Object((1,3,6,1,3,5,1,1,2,1,11),_Bgp4V2PeerRemoteIdentifier_Type())
bgp4V2PeerRemoteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerRemoteIdentifier.setStatus(_B)
class _Bgp4V2PeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halted',1),('running',2)))
_Bgp4V2PeerAdminStatus_Type.__name__=_K
_Bgp4V2PeerAdminStatus_Object=MibTableColumn
bgp4V2PeerAdminStatus=_Bgp4V2PeerAdminStatus_Object((1,3,6,1,3,5,1,1,2,1,12),_Bgp4V2PeerAdminStatus_Type())
bgp4V2PeerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerAdminStatus.setStatus(_B)
class _Bgp4V2PeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_Bgp4V2PeerState_Type.__name__=_K
_Bgp4V2PeerState_Object=MibTableColumn
bgp4V2PeerState=_Bgp4V2PeerState_Object((1,3,6,1,3,5,1,1,2,1,13),_Bgp4V2PeerState_Type())
bgp4V2PeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerState.setStatus(_B)
_Bgp4V2PeerDescription_Type=SnmpAdminString
_Bgp4V2PeerDescription_Object=MibTableColumn
bgp4V2PeerDescription=_Bgp4V2PeerDescription_Object((1,3,6,1,3,5,1,1,2,1,14),_Bgp4V2PeerDescription_Type())
bgp4V2PeerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerDescription.setStatus(_B)
_Bgp4V2PeerErrorsTable_Object=MibTable
bgp4V2PeerErrorsTable=_Bgp4V2PeerErrorsTable_Object((1,3,6,1,3,5,1,1,3))
if mibBuilder.loadTexts:bgp4V2PeerErrorsTable.setStatus(_B)
_Bgp4V2PeerErrorsEntry_Object=MibTableRow
bgp4V2PeerErrorsEntry=_Bgp4V2PeerErrorsEntry_Object((1,3,6,1,3,5,1,1,3,1))
if mibBuilder.loadTexts:bgp4V2PeerErrorsEntry.setStatus(_B)
class _Bgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorCodeReceived_Type.__name__=_D
_Bgp4V2PeerLastErrorCodeReceived_Object=MibTableColumn
bgp4V2PeerLastErrorCodeReceived=_Bgp4V2PeerLastErrorCodeReceived_Object((1,3,6,1,3,5,1,1,3,1,1),_Bgp4V2PeerLastErrorCodeReceived_Type())
bgp4V2PeerLastErrorCodeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorCodeReceived.setStatus(_B)
class _Bgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorSubCodeReceived_Type.__name__=_D
_Bgp4V2PeerLastErrorSubCodeReceived_Object=MibTableColumn
bgp4V2PeerLastErrorSubCodeReceived=_Bgp4V2PeerLastErrorSubCodeReceived_Object((1,3,6,1,3,5,1,1,3,1,2),_Bgp4V2PeerLastErrorSubCodeReceived_Type())
bgp4V2PeerLastErrorSubCodeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSubCodeReceived.setStatus(_B)
_Bgp4V2PeerLastErrorReceivedTime_Type=TimeStamp
_Bgp4V2PeerLastErrorReceivedTime_Object=MibTableColumn
bgp4V2PeerLastErrorReceivedTime=_Bgp4V2PeerLastErrorReceivedTime_Object((1,3,6,1,3,5,1,1,3,1,3),_Bgp4V2PeerLastErrorReceivedTime_Type())
bgp4V2PeerLastErrorReceivedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorReceivedTime.setStatus(_B)
_Bgp4V2PeerLastErrorReceivedText_Type=SnmpAdminString
_Bgp4V2PeerLastErrorReceivedText_Object=MibTableColumn
bgp4V2PeerLastErrorReceivedText=_Bgp4V2PeerLastErrorReceivedText_Object((1,3,6,1,3,5,1,1,3,1,4),_Bgp4V2PeerLastErrorReceivedText_Type())
bgp4V2PeerLastErrorReceivedText.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorReceivedText.setStatus(_B)
class _Bgp4V2PeerLastErrorReceivedData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_Bgp4V2PeerLastErrorReceivedData_Type.__name__=_H
_Bgp4V2PeerLastErrorReceivedData_Object=MibTableColumn
bgp4V2PeerLastErrorReceivedData=_Bgp4V2PeerLastErrorReceivedData_Object((1,3,6,1,3,5,1,1,3,1,5),_Bgp4V2PeerLastErrorReceivedData_Type())
bgp4V2PeerLastErrorReceivedData.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorReceivedData.setStatus(_B)
class _Bgp4V2PeerLastErrorCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorCodeSent_Type.__name__=_D
_Bgp4V2PeerLastErrorCodeSent_Object=MibTableColumn
bgp4V2PeerLastErrorCodeSent=_Bgp4V2PeerLastErrorCodeSent_Object((1,3,6,1,3,5,1,1,3,1,6),_Bgp4V2PeerLastErrorCodeSent_Type())
bgp4V2PeerLastErrorCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorCodeSent.setStatus(_B)
class _Bgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorSubCodeSent_Type.__name__=_D
_Bgp4V2PeerLastErrorSubCodeSent_Object=MibTableColumn
bgp4V2PeerLastErrorSubCodeSent=_Bgp4V2PeerLastErrorSubCodeSent_Object((1,3,6,1,3,5,1,1,3,1,7),_Bgp4V2PeerLastErrorSubCodeSent_Type())
bgp4V2PeerLastErrorSubCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSubCodeSent.setStatus(_B)
_Bgp4V2PeerLastErrorSentTime_Type=TimeStamp
_Bgp4V2PeerLastErrorSentTime_Object=MibTableColumn
bgp4V2PeerLastErrorSentTime=_Bgp4V2PeerLastErrorSentTime_Object((1,3,6,1,3,5,1,1,3,1,8),_Bgp4V2PeerLastErrorSentTime_Type())
bgp4V2PeerLastErrorSentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSentTime.setStatus(_B)
_Bgp4V2PeerLastErrorSentText_Type=SnmpAdminString
_Bgp4V2PeerLastErrorSentText_Object=MibTableColumn
bgp4V2PeerLastErrorSentText=_Bgp4V2PeerLastErrorSentText_Object((1,3,6,1,3,5,1,1,3,1,9),_Bgp4V2PeerLastErrorSentText_Type())
bgp4V2PeerLastErrorSentText.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSentText.setStatus(_B)
class _Bgp4V2PeerLastErrorSentData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_Bgp4V2PeerLastErrorSentData_Type.__name__=_H
_Bgp4V2PeerLastErrorSentData_Object=MibTableColumn
bgp4V2PeerLastErrorSentData=_Bgp4V2PeerLastErrorSentData_Object((1,3,6,1,3,5,1,1,3,1,10),_Bgp4V2PeerLastErrorSentData_Type())
bgp4V2PeerLastErrorSentData.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSentData.setStatus(_B)
_Bgp4V2PeerEventTimesTable_Object=MibTable
bgp4V2PeerEventTimesTable=_Bgp4V2PeerEventTimesTable_Object((1,3,6,1,3,5,1,1,4))
if mibBuilder.loadTexts:bgp4V2PeerEventTimesTable.setStatus(_B)
_Bgp4V2PeerEventTimesEntry_Object=MibTableRow
bgp4V2PeerEventTimesEntry=_Bgp4V2PeerEventTimesEntry_Object((1,3,6,1,3,5,1,1,4,1))
if mibBuilder.loadTexts:bgp4V2PeerEventTimesEntry.setStatus(_B)
_Bgp4V2PeerFsmEstablishedTime_Type=Gauge32
_Bgp4V2PeerFsmEstablishedTime_Object=MibTableColumn
bgp4V2PeerFsmEstablishedTime=_Bgp4V2PeerFsmEstablishedTime_Object((1,3,6,1,3,5,1,1,4,1,1),_Bgp4V2PeerFsmEstablishedTime_Type())
bgp4V2PeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerFsmEstablishedTime.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerFsmEstablishedTime.setUnits(_F)
_Bgp4V2PeerInUpdatesElapsedTime_Type=Gauge32
_Bgp4V2PeerInUpdatesElapsedTime_Object=MibTableColumn
bgp4V2PeerInUpdatesElapsedTime=_Bgp4V2PeerInUpdatesElapsedTime_Object((1,3,6,1,3,5,1,1,4,1,2),_Bgp4V2PeerInUpdatesElapsedTime_Type())
bgp4V2PeerInUpdatesElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerInUpdatesElapsedTime.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerInUpdatesElapsedTime.setUnits(_F)
_Bgp4V2PeerConfiguredTimersTable_Object=MibTable
bgp4V2PeerConfiguredTimersTable=_Bgp4V2PeerConfiguredTimersTable_Object((1,3,6,1,3,5,1,1,5))
if mibBuilder.loadTexts:bgp4V2PeerConfiguredTimersTable.setStatus(_B)
_Bgp4V2PeerConfiguredTimersEntry_Object=MibTableRow
bgp4V2PeerConfiguredTimersEntry=_Bgp4V2PeerConfiguredTimersEntry_Object((1,3,6,1,3,5,1,1,5,1))
if mibBuilder.loadTexts:bgp4V2PeerConfiguredTimersEntry.setStatus(_B)
class _Bgp4V2PeerConnectRetryInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Bgp4V2PeerConnectRetryInterval_Type.__name__=_D
_Bgp4V2PeerConnectRetryInterval_Object=MibTableColumn
bgp4V2PeerConnectRetryInterval=_Bgp4V2PeerConnectRetryInterval_Object((1,3,6,1,3,5,1,1,5,1,1),_Bgp4V2PeerConnectRetryInterval_Type())
bgp4V2PeerConnectRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerConnectRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerConnectRetryInterval.setUnits(_F)
class _Bgp4V2PeerHoldTimeConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_Bgp4V2PeerHoldTimeConfigured_Type.__name__=_D
_Bgp4V2PeerHoldTimeConfigured_Object=MibTableColumn
bgp4V2PeerHoldTimeConfigured=_Bgp4V2PeerHoldTimeConfigured_Object((1,3,6,1,3,5,1,1,5,1,2),_Bgp4V2PeerHoldTimeConfigured_Type())
bgp4V2PeerHoldTimeConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerHoldTimeConfigured.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerHoldTimeConfigured.setUnits(_F)
class _Bgp4V2PeerKeepAliveConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_Bgp4V2PeerKeepAliveConfigured_Type.__name__=_D
_Bgp4V2PeerKeepAliveConfigured_Object=MibTableColumn
bgp4V2PeerKeepAliveConfigured=_Bgp4V2PeerKeepAliveConfigured_Object((1,3,6,1,3,5,1,1,5,1,3),_Bgp4V2PeerKeepAliveConfigured_Type())
bgp4V2PeerKeepAliveConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerKeepAliveConfigured.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerKeepAliveConfigured.setUnits(_F)
class _Bgp4V2PeerMinASOrigInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Bgp4V2PeerMinASOrigInterval_Type.__name__=_D
_Bgp4V2PeerMinASOrigInterval_Object=MibTableColumn
bgp4V2PeerMinASOrigInterval=_Bgp4V2PeerMinASOrigInterval_Object((1,3,6,1,3,5,1,1,5,1,4),_Bgp4V2PeerMinASOrigInterval_Type())
bgp4V2PeerMinASOrigInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerMinASOrigInterval.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerMinASOrigInterval.setUnits(_F)
class _Bgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Bgp4V2PeerMinRouteAdverInterval_Type.__name__=_D
_Bgp4V2PeerMinRouteAdverInterval_Object=MibTableColumn
bgp4V2PeerMinRouteAdverInterval=_Bgp4V2PeerMinRouteAdverInterval_Object((1,3,6,1,3,5,1,1,5,1,5),_Bgp4V2PeerMinRouteAdverInterval_Type())
bgp4V2PeerMinRouteAdverInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerMinRouteAdverInterval.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerMinRouteAdverInterval.setUnits(_F)
_Bgp4V2PeerNegotiatedTimersTable_Object=MibTable
bgp4V2PeerNegotiatedTimersTable=_Bgp4V2PeerNegotiatedTimersTable_Object((1,3,6,1,3,5,1,1,6))
if mibBuilder.loadTexts:bgp4V2PeerNegotiatedTimersTable.setStatus(_B)
_Bgp4V2PeerNegotiatedTimersEntry_Object=MibTableRow
bgp4V2PeerNegotiatedTimersEntry=_Bgp4V2PeerNegotiatedTimersEntry_Object((1,3,6,1,3,5,1,1,6,1))
if mibBuilder.loadTexts:bgp4V2PeerNegotiatedTimersEntry.setStatus(_B)
class _Bgp4V2PeerHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_Bgp4V2PeerHoldTime_Type.__name__=_D
_Bgp4V2PeerHoldTime_Object=MibTableColumn
bgp4V2PeerHoldTime=_Bgp4V2PeerHoldTime_Object((1,3,6,1,3,5,1,1,6,1,1),_Bgp4V2PeerHoldTime_Type())
bgp4V2PeerHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerHoldTime.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerHoldTime.setUnits(_F)
class _Bgp4V2PeerKeepAlive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_Bgp4V2PeerKeepAlive_Type.__name__=_D
_Bgp4V2PeerKeepAlive_Object=MibTableColumn
bgp4V2PeerKeepAlive=_Bgp4V2PeerKeepAlive_Object((1,3,6,1,3,5,1,1,6,1,2),_Bgp4V2PeerKeepAlive_Type())
bgp4V2PeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:bgp4V2PeerKeepAlive.setUnits(_F)
_Bgp4V2PeerCountersTable_Object=MibTable
bgp4V2PeerCountersTable=_Bgp4V2PeerCountersTable_Object((1,3,6,1,3,5,1,1,7))
if mibBuilder.loadTexts:bgp4V2PeerCountersTable.setStatus(_B)
_Bgp4V2PeerCountersEntry_Object=MibTableRow
bgp4V2PeerCountersEntry=_Bgp4V2PeerCountersEntry_Object((1,3,6,1,3,5,1,1,7,1))
if mibBuilder.loadTexts:bgp4V2PeerCountersEntry.setStatus(_B)
_Bgp4V2PeerInUpdates_Type=Counter32
_Bgp4V2PeerInUpdates_Object=MibTableColumn
bgp4V2PeerInUpdates=_Bgp4V2PeerInUpdates_Object((1,3,6,1,3,5,1,1,7,1,1),_Bgp4V2PeerInUpdates_Type())
bgp4V2PeerInUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerInUpdates.setStatus(_B)
_Bgp4V2PeerOutUpdates_Type=Counter32
_Bgp4V2PeerOutUpdates_Object=MibTableColumn
bgp4V2PeerOutUpdates=_Bgp4V2PeerOutUpdates_Object((1,3,6,1,3,5,1,1,7,1,2),_Bgp4V2PeerOutUpdates_Type())
bgp4V2PeerOutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerOutUpdates.setStatus(_B)
_Bgp4V2PeerInTotalMessages_Type=Counter32
_Bgp4V2PeerInTotalMessages_Object=MibTableColumn
bgp4V2PeerInTotalMessages=_Bgp4V2PeerInTotalMessages_Object((1,3,6,1,3,5,1,1,7,1,3),_Bgp4V2PeerInTotalMessages_Type())
bgp4V2PeerInTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerInTotalMessages.setStatus(_B)
_Bgp4V2PeerOutTotalMessages_Type=Counter32
_Bgp4V2PeerOutTotalMessages_Object=MibTableColumn
bgp4V2PeerOutTotalMessages=_Bgp4V2PeerOutTotalMessages_Object((1,3,6,1,3,5,1,1,7,1,4),_Bgp4V2PeerOutTotalMessages_Type())
bgp4V2PeerOutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerOutTotalMessages.setStatus(_B)
_Bgp4V2PeerFsmEstablishedTransitions_Type=Counter32
_Bgp4V2PeerFsmEstablishedTransitions_Object=MibTableColumn
bgp4V2PeerFsmEstablishedTransitions=_Bgp4V2PeerFsmEstablishedTransitions_Object((1,3,6,1,3,5,1,1,7,1,5),_Bgp4V2PeerFsmEstablishedTransitions_Type())
bgp4V2PeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PeerFsmEstablishedTransitions.setStatus(_B)
_Bgp4V2PrefixGaugesTable_Object=MibTable
bgp4V2PrefixGaugesTable=_Bgp4V2PrefixGaugesTable_Object((1,3,6,1,3,5,1,1,8))
if mibBuilder.loadTexts:bgp4V2PrefixGaugesTable.setStatus(_B)
_Bgp4V2PrefixGaugesEntry_Object=MibTableRow
bgp4V2PrefixGaugesEntry=_Bgp4V2PrefixGaugesEntry_Object((1,3,6,1,3,5,1,1,8,1))
bgp4V2PrefixGaugesEntry.setIndexNames((0,_A,_G),(0,_A,_I),(0,_A,_J),(0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:bgp4V2PrefixGaugesEntry.setStatus(_B)
_Bgp4V2PrefixGaugesAfi_Type=Bgp4V2AddressFamilyIdentifierTC
_Bgp4V2PrefixGaugesAfi_Object=MibTableColumn
bgp4V2PrefixGaugesAfi=_Bgp4V2PrefixGaugesAfi_Object((1,3,6,1,3,5,1,1,8,1,1),_Bgp4V2PrefixGaugesAfi_Type())
bgp4V2PrefixGaugesAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2PrefixGaugesAfi.setStatus(_B)
_Bgp4V2PrefixGaugesSafi_Type=Bgp4V2SubsequentAddressFamilyIdentifierTC
_Bgp4V2PrefixGaugesSafi_Object=MibTableColumn
bgp4V2PrefixGaugesSafi=_Bgp4V2PrefixGaugesSafi_Object((1,3,6,1,3,5,1,1,8,1,2),_Bgp4V2PrefixGaugesSafi_Type())
bgp4V2PrefixGaugesSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2PrefixGaugesSafi.setStatus(_B)
_Bgp4V2PrefixInPrefixes_Type=Gauge32
_Bgp4V2PrefixInPrefixes_Object=MibTableColumn
bgp4V2PrefixInPrefixes=_Bgp4V2PrefixInPrefixes_Object((1,3,6,1,3,5,1,1,8,1,3),_Bgp4V2PrefixInPrefixes_Type())
bgp4V2PrefixInPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PrefixInPrefixes.setStatus(_B)
_Bgp4V2PrefixInPrefixesAccepted_Type=Gauge32
_Bgp4V2PrefixInPrefixesAccepted_Object=MibTableColumn
bgp4V2PrefixInPrefixesAccepted=_Bgp4V2PrefixInPrefixesAccepted_Object((1,3,6,1,3,5,1,1,8,1,4),_Bgp4V2PrefixInPrefixesAccepted_Type())
bgp4V2PrefixInPrefixesAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PrefixInPrefixesAccepted.setStatus(_B)
_Bgp4V2PrefixOutPrefixes_Type=Gauge32
_Bgp4V2PrefixOutPrefixes_Object=MibTableColumn
bgp4V2PrefixOutPrefixes=_Bgp4V2PrefixOutPrefixes_Object((1,3,6,1,3,5,1,1,8,1,5),_Bgp4V2PrefixOutPrefixes_Type())
bgp4V2PrefixOutPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2PrefixOutPrefixes.setStatus(_B)
_Bgp4V2NlriTable_Object=MibTable
bgp4V2NlriTable=_Bgp4V2NlriTable_Object((1,3,6,1,3,5,1,1,9))
if mibBuilder.loadTexts:bgp4V2NlriTable.setStatus(_B)
_Bgp4V2NlriEntry_Object=MibTableRow
bgp4V2NlriEntry=_Bgp4V2NlriEntry_Object((1,3,6,1,3,5,1,1,9,1))
bgp4V2NlriEntry.setIndexNames((0,_A,_G),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_I),(0,_A,_J),(0,_A,_Z))
if mibBuilder.loadTexts:bgp4V2NlriEntry.setStatus(_B)
class _Bgp4V2NlriIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Bgp4V2NlriIndex_Type.__name__=_D
_Bgp4V2NlriIndex_Object=MibTableColumn
bgp4V2NlriIndex=_Bgp4V2NlriIndex_Object((1,3,6,1,3,5,1,1,9,1,1),_Bgp4V2NlriIndex_Type())
bgp4V2NlriIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2NlriIndex.setStatus(_B)
_Bgp4V2NlriAfi_Type=Bgp4V2AddressFamilyIdentifierTC
_Bgp4V2NlriAfi_Object=MibTableColumn
bgp4V2NlriAfi=_Bgp4V2NlriAfi_Object((1,3,6,1,3,5,1,1,9,1,2),_Bgp4V2NlriAfi_Type())
bgp4V2NlriAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2NlriAfi.setStatus(_B)
_Bgp4V2NlriSafi_Type=Bgp4V2SubsequentAddressFamilyIdentifierTC
_Bgp4V2NlriSafi_Object=MibTableColumn
bgp4V2NlriSafi=_Bgp4V2NlriSafi_Object((1,3,6,1,3,5,1,1,9,1,3),_Bgp4V2NlriSafi_Type())
bgp4V2NlriSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2NlriSafi.setStatus(_B)
_Bgp4V2NlriPrefixType_Type=InetAddressType
_Bgp4V2NlriPrefixType_Object=MibTableColumn
bgp4V2NlriPrefixType=_Bgp4V2NlriPrefixType_Object((1,3,6,1,3,5,1,1,9,1,4),_Bgp4V2NlriPrefixType_Type())
bgp4V2NlriPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2NlriPrefixType.setStatus(_B)
_Bgp4V2NlriPrefix_Type=InetAddress
_Bgp4V2NlriPrefix_Object=MibTableColumn
bgp4V2NlriPrefix=_Bgp4V2NlriPrefix_Object((1,3,6,1,3,5,1,1,9,1,5),_Bgp4V2NlriPrefix_Type())
bgp4V2NlriPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2NlriPrefix.setStatus(_B)
_Bgp4V2NlriPrefixLen_Type=InetAddressPrefixLength
_Bgp4V2NlriPrefixLen_Object=MibTableColumn
bgp4V2NlriPrefixLen=_Bgp4V2NlriPrefixLen_Object((1,3,6,1,3,5,1,1,9,1,6),_Bgp4V2NlriPrefixLen_Type())
bgp4V2NlriPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2NlriPrefixLen.setStatus(_B)
_Bgp4V2NlriBest_Type=TruthValue
_Bgp4V2NlriBest_Object=MibTableColumn
bgp4V2NlriBest=_Bgp4V2NlriBest_Object((1,3,6,1,3,5,1,1,9,1,7),_Bgp4V2NlriBest_Type())
bgp4V2NlriBest.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriBest.setStatus(_B)
_Bgp4V2NlriCalcLocalPref_Type=Unsigned32
_Bgp4V2NlriCalcLocalPref_Object=MibTableColumn
bgp4V2NlriCalcLocalPref=_Bgp4V2NlriCalcLocalPref_Object((1,3,6,1,3,5,1,1,9,1,8),_Bgp4V2NlriCalcLocalPref_Type())
bgp4V2NlriCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriCalcLocalPref.setStatus(_B)
class _Bgp4V2NlriOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_Bgp4V2NlriOrigin_Type.__name__=_K
_Bgp4V2NlriOrigin_Object=MibTableColumn
bgp4V2NlriOrigin=_Bgp4V2NlriOrigin_Object((1,3,6,1,3,5,1,1,9,1,9),_Bgp4V2NlriOrigin_Type())
bgp4V2NlriOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriOrigin.setStatus(_B)
_Bgp4V2NlriNextHopAddrType_Type=InetAddressType
_Bgp4V2NlriNextHopAddrType_Object=MibTableColumn
bgp4V2NlriNextHopAddrType=_Bgp4V2NlriNextHopAddrType_Object((1,3,6,1,3,5,1,1,9,1,10),_Bgp4V2NlriNextHopAddrType_Type())
bgp4V2NlriNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriNextHopAddrType.setStatus(_B)
class _Bgp4V2NlriNextHopAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_Bgp4V2NlriNextHopAddr_Type.__name__=_W
_Bgp4V2NlriNextHopAddr_Object=MibTableColumn
bgp4V2NlriNextHopAddr=_Bgp4V2NlriNextHopAddr_Object((1,3,6,1,3,5,1,1,9,1,11),_Bgp4V2NlriNextHopAddr_Type())
bgp4V2NlriNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriNextHopAddr.setStatus(_B)
_Bgp4V2NlriLinkLocalNextHopAddrType_Type=InetAddressType
_Bgp4V2NlriLinkLocalNextHopAddrType_Object=MibTableColumn
bgp4V2NlriLinkLocalNextHopAddrType=_Bgp4V2NlriLinkLocalNextHopAddrType_Object((1,3,6,1,3,5,1,1,9,1,12),_Bgp4V2NlriLinkLocalNextHopAddrType_Type())
bgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriLinkLocalNextHopAddrType.setStatus(_B)
_Bgp4V2NlriLinkLocalNextHopAddr_Type=InetAddress
_Bgp4V2NlriLinkLocalNextHopAddr_Object=MibTableColumn
bgp4V2NlriLinkLocalNextHopAddr=_Bgp4V2NlriLinkLocalNextHopAddr_Object((1,3,6,1,3,5,1,1,9,1,13),_Bgp4V2NlriLinkLocalNextHopAddr_Type())
bgp4V2NlriLinkLocalNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriLinkLocalNextHopAddr.setStatus(_B)
_Bgp4V2NlriLocalPrefPresent_Type=TruthValue
_Bgp4V2NlriLocalPrefPresent_Object=MibTableColumn
bgp4V2NlriLocalPrefPresent=_Bgp4V2NlriLocalPrefPresent_Object((1,3,6,1,3,5,1,1,9,1,14),_Bgp4V2NlriLocalPrefPresent_Type())
bgp4V2NlriLocalPrefPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriLocalPrefPresent.setStatus(_B)
_Bgp4V2NlriLocalPref_Type=Unsigned32
_Bgp4V2NlriLocalPref_Object=MibTableColumn
bgp4V2NlriLocalPref=_Bgp4V2NlriLocalPref_Object((1,3,6,1,3,5,1,1,9,1,15),_Bgp4V2NlriLocalPref_Type())
bgp4V2NlriLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriLocalPref.setStatus(_B)
_Bgp4V2NlriMedPresent_Type=TruthValue
_Bgp4V2NlriMedPresent_Object=MibTableColumn
bgp4V2NlriMedPresent=_Bgp4V2NlriMedPresent_Object((1,3,6,1,3,5,1,1,9,1,16),_Bgp4V2NlriMedPresent_Type())
bgp4V2NlriMedPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriMedPresent.setStatus(_B)
_Bgp4V2NlriMed_Type=Unsigned32
_Bgp4V2NlriMed_Object=MibTableColumn
bgp4V2NlriMed=_Bgp4V2NlriMed_Object((1,3,6,1,3,5,1,1,9,1,17),_Bgp4V2NlriMed_Type())
bgp4V2NlriMed.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriMed.setStatus(_B)
_Bgp4V2NlriAtomicAggregate_Type=TruthValue
_Bgp4V2NlriAtomicAggregate_Object=MibTableColumn
bgp4V2NlriAtomicAggregate=_Bgp4V2NlriAtomicAggregate_Object((1,3,6,1,3,5,1,1,9,1,18),_Bgp4V2NlriAtomicAggregate_Type())
bgp4V2NlriAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAtomicAggregate.setStatus(_B)
_Bgp4V2NlriAggregatorPresent_Type=TruthValue
_Bgp4V2NlriAggregatorPresent_Object=MibTableColumn
bgp4V2NlriAggregatorPresent=_Bgp4V2NlriAggregatorPresent_Object((1,3,6,1,3,5,1,1,9,1,19),_Bgp4V2NlriAggregatorPresent_Type())
bgp4V2NlriAggregatorPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAggregatorPresent.setStatus(_B)
_Bgp4V2NlriAggregatorAS_Type=InetAutonomousSystemNumber
_Bgp4V2NlriAggregatorAS_Object=MibTableColumn
bgp4V2NlriAggregatorAS=_Bgp4V2NlriAggregatorAS_Object((1,3,6,1,3,5,1,1,9,1,20),_Bgp4V2NlriAggregatorAS_Type())
bgp4V2NlriAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAggregatorAS.setStatus(_B)
_Bgp4V2NlriAggregatorAddr_Type=Bgp4V2IdentifierTC
_Bgp4V2NlriAggregatorAddr_Object=MibTableColumn
bgp4V2NlriAggregatorAddr=_Bgp4V2NlriAggregatorAddr_Object((1,3,6,1,3,5,1,1,9,1,21),_Bgp4V2NlriAggregatorAddr_Type())
bgp4V2NlriAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAggregatorAddr.setStatus(_B)
_Bgp4V2NlriAsPathCalcLength_Type=Unsigned32
_Bgp4V2NlriAsPathCalcLength_Object=MibTableColumn
bgp4V2NlriAsPathCalcLength=_Bgp4V2NlriAsPathCalcLength_Object((1,3,6,1,3,5,1,1,9,1,22),_Bgp4V2NlriAsPathCalcLength_Type())
bgp4V2NlriAsPathCalcLength.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAsPathCalcLength.setStatus(_B)
_Bgp4V2NlriAsPathString_Type=SnmpAdminString
_Bgp4V2NlriAsPathString_Object=MibTableColumn
bgp4V2NlriAsPathString=_Bgp4V2NlriAsPathString_Object((1,3,6,1,3,5,1,1,9,1,23),_Bgp4V2NlriAsPathString_Type())
bgp4V2NlriAsPathString.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAsPathString.setStatus(_B)
class _Bgp4V2NlriAsPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4072))
_Bgp4V2NlriAsPath_Type.__name__=_H
_Bgp4V2NlriAsPath_Object=MibTableColumn
bgp4V2NlriAsPath=_Bgp4V2NlriAsPath_Object((1,3,6,1,3,5,1,1,9,1,24),_Bgp4V2NlriAsPath_Type())
bgp4V2NlriAsPath.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriAsPath.setStatus(_B)
class _Bgp4V2NlriPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4072))
_Bgp4V2NlriPathAttrUnknown_Type.__name__=_H
_Bgp4V2NlriPathAttrUnknown_Object=MibTableColumn
bgp4V2NlriPathAttrUnknown=_Bgp4V2NlriPathAttrUnknown_Object((1,3,6,1,3,5,1,1,9,1,25),_Bgp4V2NlriPathAttrUnknown_Type())
bgp4V2NlriPathAttrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2NlriPathAttrUnknown.setStatus(_B)
_Bgp4V2AdjRibsOutTable_Object=MibTable
bgp4V2AdjRibsOutTable=_Bgp4V2AdjRibsOutTable_Object((1,3,6,1,3,5,1,1,10))
if mibBuilder.loadTexts:bgp4V2AdjRibsOutTable.setStatus(_B)
_Bgp4V2AdjRibsOutEntry_Object=MibTableRow
bgp4V2AdjRibsOutEntry=_Bgp4V2AdjRibsOutEntry_Object((1,3,6,1,3,5,1,1,10,1))
bgp4V2AdjRibsOutEntry.setIndexNames((0,_A,_G),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_I),(0,_A,_J),(0,_A,_a))
if mibBuilder.loadTexts:bgp4V2AdjRibsOutEntry.setStatus(_B)
class _Bgp4V2AdjRibsOutIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Bgp4V2AdjRibsOutIndex_Type.__name__=_D
_Bgp4V2AdjRibsOutIndex_Object=MibTableColumn
bgp4V2AdjRibsOutIndex=_Bgp4V2AdjRibsOutIndex_Object((1,3,6,1,3,5,1,1,10,1,1),_Bgp4V2AdjRibsOutIndex_Type())
bgp4V2AdjRibsOutIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bgp4V2AdjRibsOutIndex.setStatus(_B)
_Bgp4V2AdjRibsOutRoute_Type=RowPointer
_Bgp4V2AdjRibsOutRoute_Object=MibTableColumn
bgp4V2AdjRibsOutRoute=_Bgp4V2AdjRibsOutRoute_Object((1,3,6,1,3,5,1,1,10,1,2),_Bgp4V2AdjRibsOutRoute_Type())
bgp4V2AdjRibsOutRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4V2AdjRibsOutRoute.setStatus(_B)
_Bgp4V2Conformance_ObjectIdentity=ObjectIdentity
bgp4V2Conformance=_Bgp4V2Conformance_ObjectIdentity((1,3,6,1,3,5,1,2))
_Bgp4V2Compliances_ObjectIdentity=ObjectIdentity
bgp4V2Compliances=_Bgp4V2Compliances_ObjectIdentity((1,3,6,1,3,5,1,2,1))
_Bgp4V2Groups_ObjectIdentity=ObjectIdentity
bgp4V2Groups=_Bgp4V2Groups_ObjectIdentity((1,3,6,1,3,5,1,2,2))
bgp4V2PeerEntry.registerAugmentions((_A,_b))
bgp4V2PeerErrorsEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions((_A,_c))
bgp4V2PeerEventTimesEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions((_A,_d))
bgp4V2PeerConfiguredTimersEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions((_A,_e))
bgp4V2PeerNegotiatedTimersEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions((_A,_f))
bgp4V2PeerCountersEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2GlobalsGroup=ObjectGroup((1,3,6,1,3,5,1,2,2,1))
bgp4V2GlobalsGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:bgp4V2GlobalsGroup.setStatus(_B)
bgp4V2StdMIBTimersGroup=ObjectGroup((1,3,6,1,3,5,1,2,2,2))
bgp4V2StdMIBTimersGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:bgp4V2StdMIBTimersGroup.setStatus(_B)
bgp4V2StdMIBCountersGroup=ObjectGroup((1,3,6,1,3,5,1,2,2,3))
bgp4V2StdMIBCountersGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:bgp4V2StdMIBCountersGroup.setStatus(_B)
bgp4V2StdMIBErrorsGroup=ObjectGroup((1,3,6,1,3,5,1,2,2,5))
bgp4V2StdMIBErrorsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_y),(_A,_z),(_A,_V),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:bgp4V2StdMIBErrorsGroup.setStatus(_B)
bgp4V2StdMIBPeerGroup=ObjectGroup((1,3,6,1,3,5,1,2,2,6))
bgp4V2StdMIBPeerGroup.setObjects(*((_A,_L),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_M),(_A,_A8),(_A,_N),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:bgp4V2StdMIBPeerGroup.setStatus(_B)
bgp4V2StdMIBNlriGroup=ObjectGroup((1,3,6,1,3,5,1,2,2,7))
bgp4V2StdMIBNlriGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:bgp4V2StdMIBNlriGroup.setStatus(_B)
bgp4V2EstablishedNotification=NotificationType((1,3,6,1,3,5,1,0,1))
bgp4V2EstablishedNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:bgp4V2EstablishedNotification.setStatus(_B)
bgp4V2BackwardTransitionNotification=NotificationType((1,3,6,1,3,5,1,0,2))
bgp4V2BackwardTransitionNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:bgp4V2BackwardTransitionNotification.setStatus(_B)
bgp4V2StdMIBNotificationGroup=NotificationGroup((1,3,6,1,3,5,1,2,2,8))
bgp4V2StdMIBNotificationGroup.setObjects(*((_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:bgp4V2StdMIBNotificationGroup.setStatus(_B)
bgp4V2Compliance=ModuleCompliance((1,3,6,1,3,5,1,2,1,4))
bgp4V2Compliance.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:bgp4V2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'bgp4V2':bgp4V2,'bgp4V2Notifications':bgp4V2Notifications,_AX:bgp4V2EstablishedNotification,_AY:bgp4V2BackwardTransitionNotification,'bgp4V2Objects':bgp4V2Objects,'bgp4V2DiscontinuityTable':bgp4V2DiscontinuityTable,'bgp4V2DiscontinuityEntry':bgp4V2DiscontinuityEntry,_g:bgp4V2DiscontinuityTime,'bgp4V2PeerTable':bgp4V2PeerTable,'bgp4V2PeerEntry':bgp4V2PeerEntry,_G:bgp4V2PeerInstance,_A6:bgp4V2PeerLocalAddrType,_A7:bgp4V2PeerLocalAddr,_I:bgp4V2PeerRemoteAddrType,_J:bgp4V2PeerRemoteAddr,_M:bgp4V2PeerLocalPort,_A8:bgp4V2PeerLocalAs,_AA:bgp4V2PeerLocalIdentifier,_N:bgp4V2PeerRemotePort,_A9:bgp4V2PeerRemoteAs,_AB:bgp4V2PeerRemoteIdentifier,_A5:bgp4V2PeerAdminStatus,_L:bgp4V2PeerState,_AC:bgp4V2PeerDescription,'bgp4V2PeerErrorsTable':bgp4V2PeerErrorsTable,_b:bgp4V2PeerErrorsEntry,_T:bgp4V2PeerLastErrorCodeReceived,_U:bgp4V2PeerLastErrorSubCodeReceived,_z:bgp4V2PeerLastErrorReceivedTime,_V:bgp4V2PeerLastErrorReceivedText,_y:bgp4V2PeerLastErrorReceivedData,_A0:bgp4V2PeerLastErrorCodeSent,_A1:bgp4V2PeerLastErrorSubCodeSent,_A3:bgp4V2PeerLastErrorSentTime,_A4:bgp4V2PeerLastErrorSentText,_A2:bgp4V2PeerLastErrorSentData,'bgp4V2PeerEventTimesTable':bgp4V2PeerEventTimesTable,_c:bgp4V2PeerEventTimesEntry,_h:bgp4V2PeerFsmEstablishedTime,_i:bgp4V2PeerInUpdatesElapsedTime,'bgp4V2PeerConfiguredTimersTable':bgp4V2PeerConfiguredTimersTable,_d:bgp4V2PeerConfiguredTimersEntry,_j:bgp4V2PeerConnectRetryInterval,_k:bgp4V2PeerHoldTimeConfigured,_l:bgp4V2PeerKeepAliveConfigured,_m:bgp4V2PeerMinASOrigInterval,_n:bgp4V2PeerMinRouteAdverInterval,'bgp4V2PeerNegotiatedTimersTable':bgp4V2PeerNegotiatedTimersTable,_e:bgp4V2PeerNegotiatedTimersEntry,_o:bgp4V2PeerHoldTime,_p:bgp4V2PeerKeepAlive,'bgp4V2PeerCountersTable':bgp4V2PeerCountersTable,_f:bgp4V2PeerCountersEntry,_q:bgp4V2PeerInUpdates,_r:bgp4V2PeerOutUpdates,_s:bgp4V2PeerInTotalMessages,_t:bgp4V2PeerOutTotalMessages,_u:bgp4V2PeerFsmEstablishedTransitions,'bgp4V2PrefixGaugesTable':bgp4V2PrefixGaugesTable,'bgp4V2PrefixGaugesEntry':bgp4V2PrefixGaugesEntry,_X:bgp4V2PrefixGaugesAfi,_Y:bgp4V2PrefixGaugesSafi,_v:bgp4V2PrefixInPrefixes,_w:bgp4V2PrefixInPrefixesAccepted,_x:bgp4V2PrefixOutPrefixes,'bgp4V2NlriTable':bgp4V2NlriTable,'bgp4V2NlriEntry':bgp4V2NlriEntry,_Z:bgp4V2NlriIndex,_O:bgp4V2NlriAfi,_P:bgp4V2NlriSafi,_Q:bgp4V2NlriPrefixType,_R:bgp4V2NlriPrefix,_S:bgp4V2NlriPrefixLen,_AF:bgp4V2NlriBest,_AG:bgp4V2NlriCalcLocalPref,_AU:bgp4V2NlriOrigin,_AR:bgp4V2NlriNextHopAddrType,_AQ:bgp4V2NlriNextHopAddr,_AS:bgp4V2NlriLinkLocalNextHopAddrType,_AT:bgp4V2NlriLinkLocalNextHopAddr,_AN:bgp4V2NlriLocalPrefPresent,_AM:bgp4V2NlriLocalPref,_AP:bgp4V2NlriMedPresent,_AO:bgp4V2NlriMed,_AL:bgp4V2NlriAtomicAggregate,_AI:bgp4V2NlriAggregatorPresent,_AJ:bgp4V2NlriAggregatorAS,_AK:bgp4V2NlriAggregatorAddr,_AD:bgp4V2NlriAsPathCalcLength,_AE:bgp4V2NlriAsPathString,_AV:bgp4V2NlriAsPath,_AW:bgp4V2NlriPathAttrUnknown,'bgp4V2AdjRibsOutTable':bgp4V2AdjRibsOutTable,'bgp4V2AdjRibsOutEntry':bgp4V2AdjRibsOutEntry,_a:bgp4V2AdjRibsOutIndex,_AH:bgp4V2AdjRibsOutRoute,'bgp4V2Conformance':bgp4V2Conformance,'bgp4V2Compliances':bgp4V2Compliances,'bgp4V2Compliance':bgp4V2Compliance,'bgp4V2Groups':bgp4V2Groups,_Ae:bgp4V2GlobalsGroup,_AZ:bgp4V2StdMIBTimersGroup,_Aa:bgp4V2StdMIBCountersGroup,_Ab:bgp4V2StdMIBErrorsGroup,_Ac:bgp4V2StdMIBPeerGroup,_Ad:bgp4V2StdMIBNlriGroup,_Af:bgp4V2StdMIBNotificationGroup})