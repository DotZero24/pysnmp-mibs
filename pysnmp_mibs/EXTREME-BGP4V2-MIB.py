_Af='extremeBgp4V2StdMIBNotificationGroup'
_Ae='extremeBgp4V2GlobalsGroup'
_Ad='extremeBgp4V2StdMIBNlriGroup'
_Ac='extremeBgp4V2StdMIBPeerGroup'
_Ab='extremeBgp4V2StdMIBErrorsGroup'
_Aa='extremeBgp4V2StdMIBCountersGroup'
_AZ='extremeBgp4V2StdMIBTimersGroup'
_AY='extremeBgp4V2BackwardTransitionNotification'
_AX='extremeBgp4V2EstablishedNotification'
_AW='extremeBgp4V2NlriPathAttrUnknown'
_AV='extremeBgp4V2NlriAsPath'
_AU='extremeBgp4V2NlriOrigin'
_AT='extremeBgp4V2NlriLinkLocalNextHopAddr'
_AS='extremeBgp4V2NlriLinkLocalNextHopAddrType'
_AR='extremeBgp4V2NlriNextHopAddrType'
_AQ='extremeBgp4V2NlriNextHopAddr'
_AP='extremeBgp4V2NlriMedPresent'
_AO='extremeBgp4V2NlriMed'
_AN='extremeBgp4V2NlriLocalPrefPresent'
_AM='extremeBgp4V2NlriLocalPref'
_AL='extremeBgp4V2NlriAtomicAggregate'
_AK='extremeBgp4V2NlriAggregatorAddr'
_AJ='extremeBgp4V2NlriAggregatorAS'
_AI='extremeBgp4V2NlriAggregatorPresent'
_AH='extremeBgp4V2AdjRibsOutRoute'
_AG='extremeBgp4V2NlriCalcLocalPref'
_AF='extremeBgp4V2NlriBest'
_AE='extremeBgp4V2NlriAsPathString'
_AD='extremeBgp4V2NlriAsPathCalcLength'
_AC='extremeBgp4V2PeerDescription'
_AB='extremeBgp4V2PeerRemoteIdentifier'
_AA='extremeBgp4V2PeerLocalIdentifier'
_A9='extremeBgp4V2PeerRemoteAs'
_A8='extremeBgp4V2PeerLocalAs'
_A7='extremeBgp4V2PeerLocalAddr'
_A6='extremeBgp4V2PeerLocalAddrType'
_A5='extremeBgp4V2PeerAdminStatus'
_A4='extremeBgp4V2PeerLastErrorSentText'
_A3='extremeBgp4V2PeerLastErrorSentTime'
_A2='extremeBgp4V2PeerLastErrorSentData'
_A1='extremeBgp4V2PeerLastErrorSubCodeSent'
_A0='extremeBgp4V2PeerLastErrorCodeSent'
_z='extremeBgp4V2PeerLastErrorReceivedTime'
_y='extremeBgp4V2PeerLastErrorReceivedData'
_x='extremeBgp4V2PrefixOutPrefixes'
_w='extremeBgp4V2PrefixInPrefixesAccepted'
_v='extremeBgp4V2PrefixInPrefixes'
_u='extremeBgp4V2PeerFsmEstablishedTransitions'
_t='extremeBgp4V2PeerOutTotalMessages'
_s='extremeBgp4V2PeerInTotalMessages'
_r='extremeBgp4V2PeerOutUpdates'
_q='extremeBgp4V2PeerInUpdates'
_p='extremeBgp4V2PeerKeepAlive'
_o='extremeBgp4V2PeerHoldTime'
_n='extremeBgp4V2PeerMinRouteAdverInterval'
_m='extremeBgp4V2PeerMinASOrigInterval'
_l='extremeBgp4V2PeerKeepAliveConfigured'
_k='extremeBgp4V2PeerHoldTimeConfigured'
_j='extremeBgp4V2PeerConnectRetryInterval'
_i='extremeBgp4V2PeerInUpdatesElapsedTime'
_h='extremeBgp4V2PeerFsmEstablishedTime'
_g='extremeBgp4V2DiscontinuityTime'
_f='extremeBgp4V2PeerCountersEntry'
_e='extremeBgp4V2PeerNegotiatedTimersEntry'
_d='extremeBgp4V2PeerConfiguredTimersEntry'
_c='extremeBgp4V2PeerEventTimesEntry'
_b='extremeBgp4V2PeerErrorsEntry'
_a='extremeBgp4V2AdjRibsOutIndex'
_Z='extremeBgp4V2NlriIndex'
_Y='extremeBgp4V2PrefixGaugesSafi'
_X='extremeBgp4V2PrefixGaugesAfi'
_W='InetAddress'
_V='extremeBgp4V2PeerLastErrorReceivedText'
_U='extremeBgp4V2PeerLastErrorSubCodeReceived'
_T='extremeBgp4V2PeerLastErrorCodeReceived'
_S='extremeBgp4V2NlriPrefixLen'
_R='extremeBgp4V2NlriPrefix'
_Q='extremeBgp4V2NlriPrefixType'
_P='extremeBgp4V2NlriSafi'
_O='extremeBgp4V2NlriAfi'
_N='extremeBgp4V2PeerRemotePort'
_M='extremeBgp4V2PeerLocalPort'
_L='extremeBgp4V2PeerState'
_K='Integer32'
_J='extremeBgp4V2PeerRemoteAddr'
_I='extremeBgp4V2PeerRemoteAddrType'
_H='OctetString'
_G='extremeBgp4V2PeerInstance'
_F='seconds'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='EXTREME-BGP4V2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ExtremeBgp4V2AddressFamilyIdentifierTC,ExtremeBgp4V2IdentifierTC,ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC=mibBuilder.importSymbols('EXTREME-BGP4V2-TC-MIB','ExtremeBgp4V2AddressFamilyIdentifierTC','ExtremeBgp4V2IdentifierTC','ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_W,'InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
extremeBgp4V2=ModuleIdentity((1,3,6,1,4,1,1916,1,51))
if mibBuilder.loadTexts:extremeBgp4V2.setRevisions(('2018-11-02 00:00','2014-01-24 00:00'))
_ExtremeBgp4V2Notifications_ObjectIdentity=ObjectIdentity
extremeBgp4V2Notifications=_ExtremeBgp4V2Notifications_ObjectIdentity((1,3,6,1,4,1,1916,1,51,0))
_ExtremeBgp4V2Objects_ObjectIdentity=ObjectIdentity
extremeBgp4V2Objects=_ExtremeBgp4V2Objects_ObjectIdentity((1,3,6,1,4,1,1916,1,51,1))
_ExtremeBgp4V2DiscontinuityTable_Object=MibTable
extremeBgp4V2DiscontinuityTable=_ExtremeBgp4V2DiscontinuityTable_Object((1,3,6,1,4,1,1916,1,51,1,1))
if mibBuilder.loadTexts:extremeBgp4V2DiscontinuityTable.setStatus(_B)
_ExtremeBgp4V2DiscontinuityEntry_Object=MibTableRow
extremeBgp4V2DiscontinuityEntry=_ExtremeBgp4V2DiscontinuityEntry_Object((1,3,6,1,4,1,1916,1,51,1,1,1))
extremeBgp4V2DiscontinuityEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:extremeBgp4V2DiscontinuityEntry.setStatus(_B)
_ExtremeBgp4V2DiscontinuityTime_Type=TimeStamp
_ExtremeBgp4V2DiscontinuityTime_Object=MibTableColumn
extremeBgp4V2DiscontinuityTime=_ExtremeBgp4V2DiscontinuityTime_Object((1,3,6,1,4,1,1916,1,51,1,1,1,1),_ExtremeBgp4V2DiscontinuityTime_Type())
extremeBgp4V2DiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2DiscontinuityTime.setStatus(_B)
_ExtremeBgp4V2PeerTable_Object=MibTable
extremeBgp4V2PeerTable=_ExtremeBgp4V2PeerTable_Object((1,3,6,1,4,1,1916,1,51,1,2))
if mibBuilder.loadTexts:extremeBgp4V2PeerTable.setStatus(_B)
_ExtremeBgp4V2PeerEntry_Object=MibTableRow
extremeBgp4V2PeerEntry=_ExtremeBgp4V2PeerEntry_Object((1,3,6,1,4,1,1916,1,51,1,2,1))
extremeBgp4V2PeerEntry.setIndexNames((0,_A,_G),(0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:extremeBgp4V2PeerEntry.setStatus(_B)
class _ExtremeBgp4V2PeerInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ExtremeBgp4V2PeerInstance_Type.__name__=_D
_ExtremeBgp4V2PeerInstance_Object=MibTableColumn
extremeBgp4V2PeerInstance=_ExtremeBgp4V2PeerInstance_Object((1,3,6,1,4,1,1916,1,51,1,2,1,1),_ExtremeBgp4V2PeerInstance_Type())
extremeBgp4V2PeerInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2PeerInstance.setStatus(_B)
_ExtremeBgp4V2PeerLocalAddrType_Type=InetAddressType
_ExtremeBgp4V2PeerLocalAddrType_Object=MibTableColumn
extremeBgp4V2PeerLocalAddrType=_ExtremeBgp4V2PeerLocalAddrType_Object((1,3,6,1,4,1,1916,1,51,1,2,1,2),_ExtremeBgp4V2PeerLocalAddrType_Type())
extremeBgp4V2PeerLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLocalAddrType.setStatus(_B)
_ExtremeBgp4V2PeerLocalAddr_Type=InetAddress
_ExtremeBgp4V2PeerLocalAddr_Object=MibTableColumn
extremeBgp4V2PeerLocalAddr=_ExtremeBgp4V2PeerLocalAddr_Object((1,3,6,1,4,1,1916,1,51,1,2,1,3),_ExtremeBgp4V2PeerLocalAddr_Type())
extremeBgp4V2PeerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLocalAddr.setStatus(_B)
_ExtremeBgp4V2PeerRemoteAddrType_Type=InetAddressType
_ExtremeBgp4V2PeerRemoteAddrType_Object=MibTableColumn
extremeBgp4V2PeerRemoteAddrType=_ExtremeBgp4V2PeerRemoteAddrType_Object((1,3,6,1,4,1,1916,1,51,1,2,1,4),_ExtremeBgp4V2PeerRemoteAddrType_Type())
extremeBgp4V2PeerRemoteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2PeerRemoteAddrType.setStatus(_B)
_ExtremeBgp4V2PeerRemoteAddr_Type=InetAddress
_ExtremeBgp4V2PeerRemoteAddr_Object=MibTableColumn
extremeBgp4V2PeerRemoteAddr=_ExtremeBgp4V2PeerRemoteAddr_Object((1,3,6,1,4,1,1916,1,51,1,2,1,5),_ExtremeBgp4V2PeerRemoteAddr_Type())
extremeBgp4V2PeerRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2PeerRemoteAddr.setStatus(_B)
_ExtremeBgp4V2PeerLocalPort_Type=InetPortNumber
_ExtremeBgp4V2PeerLocalPort_Object=MibTableColumn
extremeBgp4V2PeerLocalPort=_ExtremeBgp4V2PeerLocalPort_Object((1,3,6,1,4,1,1916,1,51,1,2,1,6),_ExtremeBgp4V2PeerLocalPort_Type())
extremeBgp4V2PeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLocalPort.setStatus(_B)
_ExtremeBgp4V2PeerLocalAs_Type=InetAutonomousSystemNumber
_ExtremeBgp4V2PeerLocalAs_Object=MibTableColumn
extremeBgp4V2PeerLocalAs=_ExtremeBgp4V2PeerLocalAs_Object((1,3,6,1,4,1,1916,1,51,1,2,1,7),_ExtremeBgp4V2PeerLocalAs_Type())
extremeBgp4V2PeerLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLocalAs.setStatus(_B)
_ExtremeBgp4V2PeerLocalIdentifier_Type=ExtremeBgp4V2IdentifierTC
_ExtremeBgp4V2PeerLocalIdentifier_Object=MibTableColumn
extremeBgp4V2PeerLocalIdentifier=_ExtremeBgp4V2PeerLocalIdentifier_Object((1,3,6,1,4,1,1916,1,51,1,2,1,8),_ExtremeBgp4V2PeerLocalIdentifier_Type())
extremeBgp4V2PeerLocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLocalIdentifier.setStatus(_B)
_ExtremeBgp4V2PeerRemotePort_Type=InetPortNumber
_ExtremeBgp4V2PeerRemotePort_Object=MibTableColumn
extremeBgp4V2PeerRemotePort=_ExtremeBgp4V2PeerRemotePort_Object((1,3,6,1,4,1,1916,1,51,1,2,1,9),_ExtremeBgp4V2PeerRemotePort_Type())
extremeBgp4V2PeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerRemotePort.setStatus(_B)
_ExtremeBgp4V2PeerRemoteAs_Type=InetAutonomousSystemNumber
_ExtremeBgp4V2PeerRemoteAs_Object=MibTableColumn
extremeBgp4V2PeerRemoteAs=_ExtremeBgp4V2PeerRemoteAs_Object((1,3,6,1,4,1,1916,1,51,1,2,1,10),_ExtremeBgp4V2PeerRemoteAs_Type())
extremeBgp4V2PeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerRemoteAs.setStatus(_B)
_ExtremeBgp4V2PeerRemoteIdentifier_Type=ExtremeBgp4V2IdentifierTC
_ExtremeBgp4V2PeerRemoteIdentifier_Object=MibTableColumn
extremeBgp4V2PeerRemoteIdentifier=_ExtremeBgp4V2PeerRemoteIdentifier_Object((1,3,6,1,4,1,1916,1,51,1,2,1,11),_ExtremeBgp4V2PeerRemoteIdentifier_Type())
extremeBgp4V2PeerRemoteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerRemoteIdentifier.setStatus(_B)
class _ExtremeBgp4V2PeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halted',1),('running',2)))
_ExtremeBgp4V2PeerAdminStatus_Type.__name__=_K
_ExtremeBgp4V2PeerAdminStatus_Object=MibTableColumn
extremeBgp4V2PeerAdminStatus=_ExtremeBgp4V2PeerAdminStatus_Object((1,3,6,1,4,1,1916,1,51,1,2,1,12),_ExtremeBgp4V2PeerAdminStatus_Type())
extremeBgp4V2PeerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerAdminStatus.setStatus(_B)
class _ExtremeBgp4V2PeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_ExtremeBgp4V2PeerState_Type.__name__=_K
_ExtremeBgp4V2PeerState_Object=MibTableColumn
extremeBgp4V2PeerState=_ExtremeBgp4V2PeerState_Object((1,3,6,1,4,1,1916,1,51,1,2,1,13),_ExtremeBgp4V2PeerState_Type())
extremeBgp4V2PeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerState.setStatus(_B)
_ExtremeBgp4V2PeerDescription_Type=SnmpAdminString
_ExtremeBgp4V2PeerDescription_Object=MibTableColumn
extremeBgp4V2PeerDescription=_ExtremeBgp4V2PeerDescription_Object((1,3,6,1,4,1,1916,1,51,1,2,1,14),_ExtremeBgp4V2PeerDescription_Type())
extremeBgp4V2PeerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerDescription.setStatus(_B)
_ExtremeBgp4V2PeerErrorsTable_Object=MibTable
extremeBgp4V2PeerErrorsTable=_ExtremeBgp4V2PeerErrorsTable_Object((1,3,6,1,4,1,1916,1,51,1,3))
if mibBuilder.loadTexts:extremeBgp4V2PeerErrorsTable.setStatus(_B)
_ExtremeBgp4V2PeerErrorsEntry_Object=MibTableRow
extremeBgp4V2PeerErrorsEntry=_ExtremeBgp4V2PeerErrorsEntry_Object((1,3,6,1,4,1,1916,1,51,1,3,1))
if mibBuilder.loadTexts:extremeBgp4V2PeerErrorsEntry.setStatus(_B)
class _ExtremeBgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeBgp4V2PeerLastErrorCodeReceived_Type.__name__=_D
_ExtremeBgp4V2PeerLastErrorCodeReceived_Object=MibTableColumn
extremeBgp4V2PeerLastErrorCodeReceived=_ExtremeBgp4V2PeerLastErrorCodeReceived_Object((1,3,6,1,4,1,1916,1,51,1,3,1,1),_ExtremeBgp4V2PeerLastErrorCodeReceived_Type())
extremeBgp4V2PeerLastErrorCodeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorCodeReceived.setStatus(_B)
class _ExtremeBgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeBgp4V2PeerLastErrorSubCodeReceived_Type.__name__=_D
_ExtremeBgp4V2PeerLastErrorSubCodeReceived_Object=MibTableColumn
extremeBgp4V2PeerLastErrorSubCodeReceived=_ExtremeBgp4V2PeerLastErrorSubCodeReceived_Object((1,3,6,1,4,1,1916,1,51,1,3,1,2),_ExtremeBgp4V2PeerLastErrorSubCodeReceived_Type())
extremeBgp4V2PeerLastErrorSubCodeReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorSubCodeReceived.setStatus(_B)
_ExtremeBgp4V2PeerLastErrorReceivedTime_Type=TimeStamp
_ExtremeBgp4V2PeerLastErrorReceivedTime_Object=MibTableColumn
extremeBgp4V2PeerLastErrorReceivedTime=_ExtremeBgp4V2PeerLastErrorReceivedTime_Object((1,3,6,1,4,1,1916,1,51,1,3,1,3),_ExtremeBgp4V2PeerLastErrorReceivedTime_Type())
extremeBgp4V2PeerLastErrorReceivedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorReceivedTime.setStatus(_B)
_ExtremeBgp4V2PeerLastErrorReceivedText_Type=SnmpAdminString
_ExtremeBgp4V2PeerLastErrorReceivedText_Object=MibTableColumn
extremeBgp4V2PeerLastErrorReceivedText=_ExtremeBgp4V2PeerLastErrorReceivedText_Object((1,3,6,1,4,1,1916,1,51,1,3,1,4),_ExtremeBgp4V2PeerLastErrorReceivedText_Type())
extremeBgp4V2PeerLastErrorReceivedText.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorReceivedText.setStatus(_B)
class _ExtremeBgp4V2PeerLastErrorReceivedData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_ExtremeBgp4V2PeerLastErrorReceivedData_Type.__name__=_H
_ExtremeBgp4V2PeerLastErrorReceivedData_Object=MibTableColumn
extremeBgp4V2PeerLastErrorReceivedData=_ExtremeBgp4V2PeerLastErrorReceivedData_Object((1,3,6,1,4,1,1916,1,51,1,3,1,5),_ExtremeBgp4V2PeerLastErrorReceivedData_Type())
extremeBgp4V2PeerLastErrorReceivedData.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorReceivedData.setStatus(_B)
class _ExtremeBgp4V2PeerLastErrorCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeBgp4V2PeerLastErrorCodeSent_Type.__name__=_D
_ExtremeBgp4V2PeerLastErrorCodeSent_Object=MibTableColumn
extremeBgp4V2PeerLastErrorCodeSent=_ExtremeBgp4V2PeerLastErrorCodeSent_Object((1,3,6,1,4,1,1916,1,51,1,3,1,6),_ExtremeBgp4V2PeerLastErrorCodeSent_Type())
extremeBgp4V2PeerLastErrorCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorCodeSent.setStatus(_B)
class _ExtremeBgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ExtremeBgp4V2PeerLastErrorSubCodeSent_Type.__name__=_D
_ExtremeBgp4V2PeerLastErrorSubCodeSent_Object=MibTableColumn
extremeBgp4V2PeerLastErrorSubCodeSent=_ExtremeBgp4V2PeerLastErrorSubCodeSent_Object((1,3,6,1,4,1,1916,1,51,1,3,1,7),_ExtremeBgp4V2PeerLastErrorSubCodeSent_Type())
extremeBgp4V2PeerLastErrorSubCodeSent.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorSubCodeSent.setStatus(_B)
_ExtremeBgp4V2PeerLastErrorSentTime_Type=TimeStamp
_ExtremeBgp4V2PeerLastErrorSentTime_Object=MibTableColumn
extremeBgp4V2PeerLastErrorSentTime=_ExtremeBgp4V2PeerLastErrorSentTime_Object((1,3,6,1,4,1,1916,1,51,1,3,1,8),_ExtremeBgp4V2PeerLastErrorSentTime_Type())
extremeBgp4V2PeerLastErrorSentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorSentTime.setStatus(_B)
_ExtremeBgp4V2PeerLastErrorSentText_Type=SnmpAdminString
_ExtremeBgp4V2PeerLastErrorSentText_Object=MibTableColumn
extremeBgp4V2PeerLastErrorSentText=_ExtremeBgp4V2PeerLastErrorSentText_Object((1,3,6,1,4,1,1916,1,51,1,3,1,9),_ExtremeBgp4V2PeerLastErrorSentText_Type())
extremeBgp4V2PeerLastErrorSentText.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorSentText.setStatus(_B)
class _ExtremeBgp4V2PeerLastErrorSentData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_ExtremeBgp4V2PeerLastErrorSentData_Type.__name__=_H
_ExtremeBgp4V2PeerLastErrorSentData_Object=MibTableColumn
extremeBgp4V2PeerLastErrorSentData=_ExtremeBgp4V2PeerLastErrorSentData_Object((1,3,6,1,4,1,1916,1,51,1,3,1,10),_ExtremeBgp4V2PeerLastErrorSentData_Type())
extremeBgp4V2PeerLastErrorSentData.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerLastErrorSentData.setStatus(_B)
_ExtremeBgp4V2PeerEventTimesTable_Object=MibTable
extremeBgp4V2PeerEventTimesTable=_ExtremeBgp4V2PeerEventTimesTable_Object((1,3,6,1,4,1,1916,1,51,1,4))
if mibBuilder.loadTexts:extremeBgp4V2PeerEventTimesTable.setStatus(_B)
_ExtremeBgp4V2PeerEventTimesEntry_Object=MibTableRow
extremeBgp4V2PeerEventTimesEntry=_ExtremeBgp4V2PeerEventTimesEntry_Object((1,3,6,1,4,1,1916,1,51,1,4,1))
if mibBuilder.loadTexts:extremeBgp4V2PeerEventTimesEntry.setStatus(_B)
_ExtremeBgp4V2PeerFsmEstablishedTime_Type=Gauge32
_ExtremeBgp4V2PeerFsmEstablishedTime_Object=MibTableColumn
extremeBgp4V2PeerFsmEstablishedTime=_ExtremeBgp4V2PeerFsmEstablishedTime_Object((1,3,6,1,4,1,1916,1,51,1,4,1,1),_ExtremeBgp4V2PeerFsmEstablishedTime_Type())
extremeBgp4V2PeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerFsmEstablishedTime.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerFsmEstablishedTime.setUnits(_F)
_ExtremeBgp4V2PeerInUpdatesElapsedTime_Type=Gauge32
_ExtremeBgp4V2PeerInUpdatesElapsedTime_Object=MibTableColumn
extremeBgp4V2PeerInUpdatesElapsedTime=_ExtremeBgp4V2PeerInUpdatesElapsedTime_Object((1,3,6,1,4,1,1916,1,51,1,4,1,2),_ExtremeBgp4V2PeerInUpdatesElapsedTime_Type())
extremeBgp4V2PeerInUpdatesElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerInUpdatesElapsedTime.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerInUpdatesElapsedTime.setUnits(_F)
_ExtremeBgp4V2PeerConfiguredTimersTable_Object=MibTable
extremeBgp4V2PeerConfiguredTimersTable=_ExtremeBgp4V2PeerConfiguredTimersTable_Object((1,3,6,1,4,1,1916,1,51,1,5))
if mibBuilder.loadTexts:extremeBgp4V2PeerConfiguredTimersTable.setStatus(_B)
_ExtremeBgp4V2PeerConfiguredTimersEntry_Object=MibTableRow
extremeBgp4V2PeerConfiguredTimersEntry=_ExtremeBgp4V2PeerConfiguredTimersEntry_Object((1,3,6,1,4,1,1916,1,51,1,5,1))
if mibBuilder.loadTexts:extremeBgp4V2PeerConfiguredTimersEntry.setStatus(_B)
class _ExtremeBgp4V2PeerConnectRetryInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeBgp4V2PeerConnectRetryInterval_Type.__name__=_D
_ExtremeBgp4V2PeerConnectRetryInterval_Object=MibTableColumn
extremeBgp4V2PeerConnectRetryInterval=_ExtremeBgp4V2PeerConnectRetryInterval_Object((1,3,6,1,4,1,1916,1,51,1,5,1,1),_ExtremeBgp4V2PeerConnectRetryInterval_Type())
extremeBgp4V2PeerConnectRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerConnectRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerConnectRetryInterval.setUnits(_F)
class _ExtremeBgp4V2PeerHoldTimeConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_ExtremeBgp4V2PeerHoldTimeConfigured_Type.__name__=_D
_ExtremeBgp4V2PeerHoldTimeConfigured_Object=MibTableColumn
extremeBgp4V2PeerHoldTimeConfigured=_ExtremeBgp4V2PeerHoldTimeConfigured_Object((1,3,6,1,4,1,1916,1,51,1,5,1,2),_ExtremeBgp4V2PeerHoldTimeConfigured_Type())
extremeBgp4V2PeerHoldTimeConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerHoldTimeConfigured.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerHoldTimeConfigured.setUnits(_F)
class _ExtremeBgp4V2PeerKeepAliveConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_ExtremeBgp4V2PeerKeepAliveConfigured_Type.__name__=_D
_ExtremeBgp4V2PeerKeepAliveConfigured_Object=MibTableColumn
extremeBgp4V2PeerKeepAliveConfigured=_ExtremeBgp4V2PeerKeepAliveConfigured_Object((1,3,6,1,4,1,1916,1,51,1,5,1,3),_ExtremeBgp4V2PeerKeepAliveConfigured_Type())
extremeBgp4V2PeerKeepAliveConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerKeepAliveConfigured.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerKeepAliveConfigured.setUnits(_F)
class _ExtremeBgp4V2PeerMinASOrigInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeBgp4V2PeerMinASOrigInterval_Type.__name__=_D
_ExtremeBgp4V2PeerMinASOrigInterval_Object=MibTableColumn
extremeBgp4V2PeerMinASOrigInterval=_ExtremeBgp4V2PeerMinASOrigInterval_Object((1,3,6,1,4,1,1916,1,51,1,5,1,4),_ExtremeBgp4V2PeerMinASOrigInterval_Type())
extremeBgp4V2PeerMinASOrigInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerMinASOrigInterval.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerMinASOrigInterval.setUnits(_F)
class _ExtremeBgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeBgp4V2PeerMinRouteAdverInterval_Type.__name__=_D
_ExtremeBgp4V2PeerMinRouteAdverInterval_Object=MibTableColumn
extremeBgp4V2PeerMinRouteAdverInterval=_ExtremeBgp4V2PeerMinRouteAdverInterval_Object((1,3,6,1,4,1,1916,1,51,1,5,1,5),_ExtremeBgp4V2PeerMinRouteAdverInterval_Type())
extremeBgp4V2PeerMinRouteAdverInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerMinRouteAdverInterval.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerMinRouteAdverInterval.setUnits(_F)
_ExtremeBgp4V2PeerNegotiatedTimersTable_Object=MibTable
extremeBgp4V2PeerNegotiatedTimersTable=_ExtremeBgp4V2PeerNegotiatedTimersTable_Object((1,3,6,1,4,1,1916,1,51,1,6))
if mibBuilder.loadTexts:extremeBgp4V2PeerNegotiatedTimersTable.setStatus(_B)
_ExtremeBgp4V2PeerNegotiatedTimersEntry_Object=MibTableRow
extremeBgp4V2PeerNegotiatedTimersEntry=_ExtremeBgp4V2PeerNegotiatedTimersEntry_Object((1,3,6,1,4,1,1916,1,51,1,6,1))
if mibBuilder.loadTexts:extremeBgp4V2PeerNegotiatedTimersEntry.setStatus(_B)
class _ExtremeBgp4V2PeerHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_ExtremeBgp4V2PeerHoldTime_Type.__name__=_D
_ExtremeBgp4V2PeerHoldTime_Object=MibTableColumn
extremeBgp4V2PeerHoldTime=_ExtremeBgp4V2PeerHoldTime_Object((1,3,6,1,4,1,1916,1,51,1,6,1,1),_ExtremeBgp4V2PeerHoldTime_Type())
extremeBgp4V2PeerHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerHoldTime.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerHoldTime.setUnits(_F)
class _ExtremeBgp4V2PeerKeepAlive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_ExtremeBgp4V2PeerKeepAlive_Type.__name__=_D
_ExtremeBgp4V2PeerKeepAlive_Object=MibTableColumn
extremeBgp4V2PeerKeepAlive=_ExtremeBgp4V2PeerKeepAlive_Object((1,3,6,1,4,1,1916,1,51,1,6,1,2),_ExtremeBgp4V2PeerKeepAlive_Type())
extremeBgp4V2PeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:extremeBgp4V2PeerKeepAlive.setUnits(_F)
_ExtremeBgp4V2PeerCountersTable_Object=MibTable
extremeBgp4V2PeerCountersTable=_ExtremeBgp4V2PeerCountersTable_Object((1,3,6,1,4,1,1916,1,51,1,7))
if mibBuilder.loadTexts:extremeBgp4V2PeerCountersTable.setStatus(_B)
_ExtremeBgp4V2PeerCountersEntry_Object=MibTableRow
extremeBgp4V2PeerCountersEntry=_ExtremeBgp4V2PeerCountersEntry_Object((1,3,6,1,4,1,1916,1,51,1,7,1))
if mibBuilder.loadTexts:extremeBgp4V2PeerCountersEntry.setStatus(_B)
_ExtremeBgp4V2PeerInUpdates_Type=Counter32
_ExtremeBgp4V2PeerInUpdates_Object=MibTableColumn
extremeBgp4V2PeerInUpdates=_ExtremeBgp4V2PeerInUpdates_Object((1,3,6,1,4,1,1916,1,51,1,7,1,1),_ExtremeBgp4V2PeerInUpdates_Type())
extremeBgp4V2PeerInUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerInUpdates.setStatus(_B)
_ExtremeBgp4V2PeerOutUpdates_Type=Counter32
_ExtremeBgp4V2PeerOutUpdates_Object=MibTableColumn
extremeBgp4V2PeerOutUpdates=_ExtremeBgp4V2PeerOutUpdates_Object((1,3,6,1,4,1,1916,1,51,1,7,1,2),_ExtremeBgp4V2PeerOutUpdates_Type())
extremeBgp4V2PeerOutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerOutUpdates.setStatus(_B)
_ExtremeBgp4V2PeerInTotalMessages_Type=Counter32
_ExtremeBgp4V2PeerInTotalMessages_Object=MibTableColumn
extremeBgp4V2PeerInTotalMessages=_ExtremeBgp4V2PeerInTotalMessages_Object((1,3,6,1,4,1,1916,1,51,1,7,1,3),_ExtremeBgp4V2PeerInTotalMessages_Type())
extremeBgp4V2PeerInTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerInTotalMessages.setStatus(_B)
_ExtremeBgp4V2PeerOutTotalMessages_Type=Counter32
_ExtremeBgp4V2PeerOutTotalMessages_Object=MibTableColumn
extremeBgp4V2PeerOutTotalMessages=_ExtremeBgp4V2PeerOutTotalMessages_Object((1,3,6,1,4,1,1916,1,51,1,7,1,4),_ExtremeBgp4V2PeerOutTotalMessages_Type())
extremeBgp4V2PeerOutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerOutTotalMessages.setStatus(_B)
_ExtremeBgp4V2PeerFsmEstablishedTransitions_Type=Counter32
_ExtremeBgp4V2PeerFsmEstablishedTransitions_Object=MibTableColumn
extremeBgp4V2PeerFsmEstablishedTransitions=_ExtremeBgp4V2PeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,1916,1,51,1,7,1,5),_ExtremeBgp4V2PeerFsmEstablishedTransitions_Type())
extremeBgp4V2PeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PeerFsmEstablishedTransitions.setStatus(_B)
_ExtremeBgp4V2PrefixGaugesTable_Object=MibTable
extremeBgp4V2PrefixGaugesTable=_ExtremeBgp4V2PrefixGaugesTable_Object((1,3,6,1,4,1,1916,1,51,1,8))
if mibBuilder.loadTexts:extremeBgp4V2PrefixGaugesTable.setStatus(_B)
_ExtremeBgp4V2PrefixGaugesEntry_Object=MibTableRow
extremeBgp4V2PrefixGaugesEntry=_ExtremeBgp4V2PrefixGaugesEntry_Object((1,3,6,1,4,1,1916,1,51,1,8,1))
extremeBgp4V2PrefixGaugesEntry.setIndexNames((0,_A,_G),(0,_A,_I),(0,_A,_J),(0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:extremeBgp4V2PrefixGaugesEntry.setStatus(_B)
_ExtremeBgp4V2PrefixGaugesAfi_Type=ExtremeBgp4V2AddressFamilyIdentifierTC
_ExtremeBgp4V2PrefixGaugesAfi_Object=MibTableColumn
extremeBgp4V2PrefixGaugesAfi=_ExtremeBgp4V2PrefixGaugesAfi_Object((1,3,6,1,4,1,1916,1,51,1,8,1,1),_ExtremeBgp4V2PrefixGaugesAfi_Type())
extremeBgp4V2PrefixGaugesAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2PrefixGaugesAfi.setStatus(_B)
_ExtremeBgp4V2PrefixGaugesSafi_Type=ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC
_ExtremeBgp4V2PrefixGaugesSafi_Object=MibTableColumn
extremeBgp4V2PrefixGaugesSafi=_ExtremeBgp4V2PrefixGaugesSafi_Object((1,3,6,1,4,1,1916,1,51,1,8,1,2),_ExtremeBgp4V2PrefixGaugesSafi_Type())
extremeBgp4V2PrefixGaugesSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2PrefixGaugesSafi.setStatus(_B)
_ExtremeBgp4V2PrefixInPrefixes_Type=Gauge32
_ExtremeBgp4V2PrefixInPrefixes_Object=MibTableColumn
extremeBgp4V2PrefixInPrefixes=_ExtremeBgp4V2PrefixInPrefixes_Object((1,3,6,1,4,1,1916,1,51,1,8,1,3),_ExtremeBgp4V2PrefixInPrefixes_Type())
extremeBgp4V2PrefixInPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PrefixInPrefixes.setStatus(_B)
_ExtremeBgp4V2PrefixInPrefixesAccepted_Type=Gauge32
_ExtremeBgp4V2PrefixInPrefixesAccepted_Object=MibTableColumn
extremeBgp4V2PrefixInPrefixesAccepted=_ExtremeBgp4V2PrefixInPrefixesAccepted_Object((1,3,6,1,4,1,1916,1,51,1,8,1,4),_ExtremeBgp4V2PrefixInPrefixesAccepted_Type())
extremeBgp4V2PrefixInPrefixesAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PrefixInPrefixesAccepted.setStatus(_B)
_ExtremeBgp4V2PrefixOutPrefixes_Type=Gauge32
_ExtremeBgp4V2PrefixOutPrefixes_Object=MibTableColumn
extremeBgp4V2PrefixOutPrefixes=_ExtremeBgp4V2PrefixOutPrefixes_Object((1,3,6,1,4,1,1916,1,51,1,8,1,5),_ExtremeBgp4V2PrefixOutPrefixes_Type())
extremeBgp4V2PrefixOutPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2PrefixOutPrefixes.setStatus(_B)
_ExtremeBgp4V2NlriTable_Object=MibTable
extremeBgp4V2NlriTable=_ExtremeBgp4V2NlriTable_Object((1,3,6,1,4,1,1916,1,51,1,9))
if mibBuilder.loadTexts:extremeBgp4V2NlriTable.setStatus(_B)
_ExtremeBgp4V2NlriEntry_Object=MibTableRow
extremeBgp4V2NlriEntry=_ExtremeBgp4V2NlriEntry_Object((1,3,6,1,4,1,1916,1,51,1,9,1))
extremeBgp4V2NlriEntry.setIndexNames((0,_A,_G),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_I),(0,_A,_J),(0,_A,_Z))
if mibBuilder.loadTexts:extremeBgp4V2NlriEntry.setStatus(_B)
class _ExtremeBgp4V2NlriIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ExtremeBgp4V2NlriIndex_Type.__name__=_D
_ExtremeBgp4V2NlriIndex_Object=MibTableColumn
extremeBgp4V2NlriIndex=_ExtremeBgp4V2NlriIndex_Object((1,3,6,1,4,1,1916,1,51,1,9,1,1),_ExtremeBgp4V2NlriIndex_Type())
extremeBgp4V2NlriIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2NlriIndex.setStatus(_B)
_ExtremeBgp4V2NlriAfi_Type=ExtremeBgp4V2AddressFamilyIdentifierTC
_ExtremeBgp4V2NlriAfi_Object=MibTableColumn
extremeBgp4V2NlriAfi=_ExtremeBgp4V2NlriAfi_Object((1,3,6,1,4,1,1916,1,51,1,9,1,2),_ExtremeBgp4V2NlriAfi_Type())
extremeBgp4V2NlriAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2NlriAfi.setStatus(_B)
_ExtremeBgp4V2NlriSafi_Type=ExtremeBgp4V2SubsequentAddressFamilyIdentifierTC
_ExtremeBgp4V2NlriSafi_Object=MibTableColumn
extremeBgp4V2NlriSafi=_ExtremeBgp4V2NlriSafi_Object((1,3,6,1,4,1,1916,1,51,1,9,1,3),_ExtremeBgp4V2NlriSafi_Type())
extremeBgp4V2NlriSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2NlriSafi.setStatus(_B)
_ExtremeBgp4V2NlriPrefixType_Type=InetAddressType
_ExtremeBgp4V2NlriPrefixType_Object=MibTableColumn
extremeBgp4V2NlriPrefixType=_ExtremeBgp4V2NlriPrefixType_Object((1,3,6,1,4,1,1916,1,51,1,9,1,4),_ExtremeBgp4V2NlriPrefixType_Type())
extremeBgp4V2NlriPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2NlriPrefixType.setStatus(_B)
_ExtremeBgp4V2NlriPrefix_Type=InetAddress
_ExtremeBgp4V2NlriPrefix_Object=MibTableColumn
extremeBgp4V2NlriPrefix=_ExtremeBgp4V2NlriPrefix_Object((1,3,6,1,4,1,1916,1,51,1,9,1,5),_ExtremeBgp4V2NlriPrefix_Type())
extremeBgp4V2NlriPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2NlriPrefix.setStatus(_B)
_ExtremeBgp4V2NlriPrefixLen_Type=InetAddressPrefixLength
_ExtremeBgp4V2NlriPrefixLen_Object=MibTableColumn
extremeBgp4V2NlriPrefixLen=_ExtremeBgp4V2NlriPrefixLen_Object((1,3,6,1,4,1,1916,1,51,1,9,1,6),_ExtremeBgp4V2NlriPrefixLen_Type())
extremeBgp4V2NlriPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2NlriPrefixLen.setStatus(_B)
_ExtremeBgp4V2NlriBest_Type=TruthValue
_ExtremeBgp4V2NlriBest_Object=MibTableColumn
extremeBgp4V2NlriBest=_ExtremeBgp4V2NlriBest_Object((1,3,6,1,4,1,1916,1,51,1,9,1,7),_ExtremeBgp4V2NlriBest_Type())
extremeBgp4V2NlriBest.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriBest.setStatus(_B)
_ExtremeBgp4V2NlriCalcLocalPref_Type=Unsigned32
_ExtremeBgp4V2NlriCalcLocalPref_Object=MibTableColumn
extremeBgp4V2NlriCalcLocalPref=_ExtremeBgp4V2NlriCalcLocalPref_Object((1,3,6,1,4,1,1916,1,51,1,9,1,8),_ExtremeBgp4V2NlriCalcLocalPref_Type())
extremeBgp4V2NlriCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriCalcLocalPref.setStatus(_B)
class _ExtremeBgp4V2NlriOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_ExtremeBgp4V2NlriOrigin_Type.__name__=_K
_ExtremeBgp4V2NlriOrigin_Object=MibTableColumn
extremeBgp4V2NlriOrigin=_ExtremeBgp4V2NlriOrigin_Object((1,3,6,1,4,1,1916,1,51,1,9,1,9),_ExtremeBgp4V2NlriOrigin_Type())
extremeBgp4V2NlriOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriOrigin.setStatus(_B)
_ExtremeBgp4V2NlriNextHopAddrType_Type=InetAddressType
_ExtremeBgp4V2NlriNextHopAddrType_Object=MibTableColumn
extremeBgp4V2NlriNextHopAddrType=_ExtremeBgp4V2NlriNextHopAddrType_Object((1,3,6,1,4,1,1916,1,51,1,9,1,10),_ExtremeBgp4V2NlriNextHopAddrType_Type())
extremeBgp4V2NlriNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriNextHopAddrType.setStatus(_B)
class _ExtremeBgp4V2NlriNextHopAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_ExtremeBgp4V2NlriNextHopAddr_Type.__name__=_W
_ExtremeBgp4V2NlriNextHopAddr_Object=MibTableColumn
extremeBgp4V2NlriNextHopAddr=_ExtremeBgp4V2NlriNextHopAddr_Object((1,3,6,1,4,1,1916,1,51,1,9,1,11),_ExtremeBgp4V2NlriNextHopAddr_Type())
extremeBgp4V2NlriNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriNextHopAddr.setStatus(_B)
_ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Type=InetAddressType
_ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Object=MibTableColumn
extremeBgp4V2NlriLinkLocalNextHopAddrType=_ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Object((1,3,6,1,4,1,1916,1,51,1,9,1,12),_ExtremeBgp4V2NlriLinkLocalNextHopAddrType_Type())
extremeBgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriLinkLocalNextHopAddrType.setStatus(_B)
_ExtremeBgp4V2NlriLinkLocalNextHopAddr_Type=InetAddress
_ExtremeBgp4V2NlriLinkLocalNextHopAddr_Object=MibTableColumn
extremeBgp4V2NlriLinkLocalNextHopAddr=_ExtremeBgp4V2NlriLinkLocalNextHopAddr_Object((1,3,6,1,4,1,1916,1,51,1,9,1,13),_ExtremeBgp4V2NlriLinkLocalNextHopAddr_Type())
extremeBgp4V2NlriLinkLocalNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriLinkLocalNextHopAddr.setStatus(_B)
_ExtremeBgp4V2NlriLocalPrefPresent_Type=TruthValue
_ExtremeBgp4V2NlriLocalPrefPresent_Object=MibTableColumn
extremeBgp4V2NlriLocalPrefPresent=_ExtremeBgp4V2NlriLocalPrefPresent_Object((1,3,6,1,4,1,1916,1,51,1,9,1,14),_ExtremeBgp4V2NlriLocalPrefPresent_Type())
extremeBgp4V2NlriLocalPrefPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriLocalPrefPresent.setStatus(_B)
_ExtremeBgp4V2NlriLocalPref_Type=Unsigned32
_ExtremeBgp4V2NlriLocalPref_Object=MibTableColumn
extremeBgp4V2NlriLocalPref=_ExtremeBgp4V2NlriLocalPref_Object((1,3,6,1,4,1,1916,1,51,1,9,1,15),_ExtremeBgp4V2NlriLocalPref_Type())
extremeBgp4V2NlriLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriLocalPref.setStatus(_B)
_ExtremeBgp4V2NlriMedPresent_Type=TruthValue
_ExtremeBgp4V2NlriMedPresent_Object=MibTableColumn
extremeBgp4V2NlriMedPresent=_ExtremeBgp4V2NlriMedPresent_Object((1,3,6,1,4,1,1916,1,51,1,9,1,16),_ExtremeBgp4V2NlriMedPresent_Type())
extremeBgp4V2NlriMedPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriMedPresent.setStatus(_B)
_ExtremeBgp4V2NlriMed_Type=Unsigned32
_ExtremeBgp4V2NlriMed_Object=MibTableColumn
extremeBgp4V2NlriMed=_ExtremeBgp4V2NlriMed_Object((1,3,6,1,4,1,1916,1,51,1,9,1,17),_ExtremeBgp4V2NlriMed_Type())
extremeBgp4V2NlriMed.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriMed.setStatus(_B)
_ExtremeBgp4V2NlriAtomicAggregate_Type=TruthValue
_ExtremeBgp4V2NlriAtomicAggregate_Object=MibTableColumn
extremeBgp4V2NlriAtomicAggregate=_ExtremeBgp4V2NlriAtomicAggregate_Object((1,3,6,1,4,1,1916,1,51,1,9,1,18),_ExtremeBgp4V2NlriAtomicAggregate_Type())
extremeBgp4V2NlriAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAtomicAggregate.setStatus(_B)
_ExtremeBgp4V2NlriAggregatorPresent_Type=TruthValue
_ExtremeBgp4V2NlriAggregatorPresent_Object=MibTableColumn
extremeBgp4V2NlriAggregatorPresent=_ExtremeBgp4V2NlriAggregatorPresent_Object((1,3,6,1,4,1,1916,1,51,1,9,1,19),_ExtremeBgp4V2NlriAggregatorPresent_Type())
extremeBgp4V2NlriAggregatorPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAggregatorPresent.setStatus(_B)
_ExtremeBgp4V2NlriAggregatorAS_Type=InetAutonomousSystemNumber
_ExtremeBgp4V2NlriAggregatorAS_Object=MibTableColumn
extremeBgp4V2NlriAggregatorAS=_ExtremeBgp4V2NlriAggregatorAS_Object((1,3,6,1,4,1,1916,1,51,1,9,1,20),_ExtremeBgp4V2NlriAggregatorAS_Type())
extremeBgp4V2NlriAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAggregatorAS.setStatus(_B)
_ExtremeBgp4V2NlriAggregatorAddr_Type=ExtremeBgp4V2IdentifierTC
_ExtremeBgp4V2NlriAggregatorAddr_Object=MibTableColumn
extremeBgp4V2NlriAggregatorAddr=_ExtremeBgp4V2NlriAggregatorAddr_Object((1,3,6,1,4,1,1916,1,51,1,9,1,21),_ExtremeBgp4V2NlriAggregatorAddr_Type())
extremeBgp4V2NlriAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAggregatorAddr.setStatus(_B)
_ExtremeBgp4V2NlriAsPathCalcLength_Type=Unsigned32
_ExtremeBgp4V2NlriAsPathCalcLength_Object=MibTableColumn
extremeBgp4V2NlriAsPathCalcLength=_ExtremeBgp4V2NlriAsPathCalcLength_Object((1,3,6,1,4,1,1916,1,51,1,9,1,22),_ExtremeBgp4V2NlriAsPathCalcLength_Type())
extremeBgp4V2NlriAsPathCalcLength.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAsPathCalcLength.setStatus(_B)
_ExtremeBgp4V2NlriAsPathString_Type=SnmpAdminString
_ExtremeBgp4V2NlriAsPathString_Object=MibTableColumn
extremeBgp4V2NlriAsPathString=_ExtremeBgp4V2NlriAsPathString_Object((1,3,6,1,4,1,1916,1,51,1,9,1,23),_ExtremeBgp4V2NlriAsPathString_Type())
extremeBgp4V2NlriAsPathString.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAsPathString.setStatus(_B)
class _ExtremeBgp4V2NlriAsPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4072))
_ExtremeBgp4V2NlriAsPath_Type.__name__=_H
_ExtremeBgp4V2NlriAsPath_Object=MibTableColumn
extremeBgp4V2NlriAsPath=_ExtremeBgp4V2NlriAsPath_Object((1,3,6,1,4,1,1916,1,51,1,9,1,24),_ExtremeBgp4V2NlriAsPath_Type())
extremeBgp4V2NlriAsPath.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriAsPath.setStatus(_B)
class _ExtremeBgp4V2NlriPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4072))
_ExtremeBgp4V2NlriPathAttrUnknown_Type.__name__=_H
_ExtremeBgp4V2NlriPathAttrUnknown_Object=MibTableColumn
extremeBgp4V2NlriPathAttrUnknown=_ExtremeBgp4V2NlriPathAttrUnknown_Object((1,3,6,1,4,1,1916,1,51,1,9,1,25),_ExtremeBgp4V2NlriPathAttrUnknown_Type())
extremeBgp4V2NlriPathAttrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2NlriPathAttrUnknown.setStatus(_B)
_ExtremeBgp4V2AdjRibsOutTable_Object=MibTable
extremeBgp4V2AdjRibsOutTable=_ExtremeBgp4V2AdjRibsOutTable_Object((1,3,6,1,4,1,1916,1,51,1,10))
if mibBuilder.loadTexts:extremeBgp4V2AdjRibsOutTable.setStatus(_B)
_ExtremeBgp4V2AdjRibsOutEntry_Object=MibTableRow
extremeBgp4V2AdjRibsOutEntry=_ExtremeBgp4V2AdjRibsOutEntry_Object((1,3,6,1,4,1,1916,1,51,1,10,1))
extremeBgp4V2AdjRibsOutEntry.setIndexNames((0,_A,_G),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_I),(0,_A,_J),(0,_A,_a))
if mibBuilder.loadTexts:extremeBgp4V2AdjRibsOutEntry.setStatus(_B)
class _ExtremeBgp4V2AdjRibsOutIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ExtremeBgp4V2AdjRibsOutIndex_Type.__name__=_D
_ExtremeBgp4V2AdjRibsOutIndex_Object=MibTableColumn
extremeBgp4V2AdjRibsOutIndex=_ExtremeBgp4V2AdjRibsOutIndex_Object((1,3,6,1,4,1,1916,1,51,1,10,1,1),_ExtremeBgp4V2AdjRibsOutIndex_Type())
extremeBgp4V2AdjRibsOutIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeBgp4V2AdjRibsOutIndex.setStatus(_B)
_ExtremeBgp4V2AdjRibsOutRoute_Type=RowPointer
_ExtremeBgp4V2AdjRibsOutRoute_Object=MibTableColumn
extremeBgp4V2AdjRibsOutRoute=_ExtremeBgp4V2AdjRibsOutRoute_Object((1,3,6,1,4,1,1916,1,51,1,10,1,2),_ExtremeBgp4V2AdjRibsOutRoute_Type())
extremeBgp4V2AdjRibsOutRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeBgp4V2AdjRibsOutRoute.setStatus(_B)
_ExtremeBgp4V2Conformance_ObjectIdentity=ObjectIdentity
extremeBgp4V2Conformance=_ExtremeBgp4V2Conformance_ObjectIdentity((1,3,6,1,4,1,1916,1,51,2))
_ExtremeBgp4V2Compliances_ObjectIdentity=ObjectIdentity
extremeBgp4V2Compliances=_ExtremeBgp4V2Compliances_ObjectIdentity((1,3,6,1,4,1,1916,1,51,2,1))
_ExtremeBgp4V2Groups_ObjectIdentity=ObjectIdentity
extremeBgp4V2Groups=_ExtremeBgp4V2Groups_ObjectIdentity((1,3,6,1,4,1,1916,1,51,2,2))
extremeBgp4V2PeerEntry.registerAugmentions((_A,_b))
extremeBgp4V2PeerErrorsEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions((_A,_c))
extremeBgp4V2PeerEventTimesEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions((_A,_d))
extremeBgp4V2PeerConfiguredTimersEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions((_A,_e))
extremeBgp4V2PeerNegotiatedTimersEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2PeerEntry.registerAugmentions((_A,_f))
extremeBgp4V2PeerCountersEntry.setIndexNames(*extremeBgp4V2PeerEntry.getIndexNames())
extremeBgp4V2GlobalsGroup=ObjectGroup((1,3,6,1,4,1,1916,1,51,2,2,1))
extremeBgp4V2GlobalsGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:extremeBgp4V2GlobalsGroup.setStatus(_B)
extremeBgp4V2StdMIBTimersGroup=ObjectGroup((1,3,6,1,4,1,1916,1,51,2,2,2))
extremeBgp4V2StdMIBTimersGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:extremeBgp4V2StdMIBTimersGroup.setStatus(_B)
extremeBgp4V2StdMIBCountersGroup=ObjectGroup((1,3,6,1,4,1,1916,1,51,2,2,3))
extremeBgp4V2StdMIBCountersGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:extremeBgp4V2StdMIBCountersGroup.setStatus(_B)
extremeBgp4V2StdMIBErrorsGroup=ObjectGroup((1,3,6,1,4,1,1916,1,51,2,2,5))
extremeBgp4V2StdMIBErrorsGroup.setObjects(*((_A,_T),(_A,_U),(_A,_y),(_A,_z),(_A,_V),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:extremeBgp4V2StdMIBErrorsGroup.setStatus(_B)
extremeBgp4V2StdMIBPeerGroup=ObjectGroup((1,3,6,1,4,1,1916,1,51,2,2,6))
extremeBgp4V2StdMIBPeerGroup.setObjects(*((_A,_L),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_M),(_A,_A8),(_A,_N),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:extremeBgp4V2StdMIBPeerGroup.setStatus(_B)
extremeBgp4V2StdMIBNlriGroup=ObjectGroup((1,3,6,1,4,1,1916,1,51,2,2,7))
extremeBgp4V2StdMIBNlriGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:extremeBgp4V2StdMIBNlriGroup.setStatus(_B)
extremeBgp4V2EstablishedNotification=NotificationType((1,3,6,1,4,1,1916,1,51,0,1))
extremeBgp4V2EstablishedNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:extremeBgp4V2EstablishedNotification.setStatus(_B)
extremeBgp4V2BackwardTransitionNotification=NotificationType((1,3,6,1,4,1,1916,1,51,0,2))
extremeBgp4V2BackwardTransitionNotification.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:extremeBgp4V2BackwardTransitionNotification.setStatus(_B)
extremeBgp4V2StdMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,1916,1,51,2,2,8))
extremeBgp4V2StdMIBNotificationGroup.setObjects(*((_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:extremeBgp4V2StdMIBNotificationGroup.setStatus(_B)
extremeBgp4V2Compliance=ModuleCompliance((1,3,6,1,4,1,1916,1,51,2,1,4))
extremeBgp4V2Compliance.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:extremeBgp4V2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'extremeBgp4V2':extremeBgp4V2,'extremeBgp4V2Notifications':extremeBgp4V2Notifications,_AX:extremeBgp4V2EstablishedNotification,_AY:extremeBgp4V2BackwardTransitionNotification,'extremeBgp4V2Objects':extremeBgp4V2Objects,'extremeBgp4V2DiscontinuityTable':extremeBgp4V2DiscontinuityTable,'extremeBgp4V2DiscontinuityEntry':extremeBgp4V2DiscontinuityEntry,_g:extremeBgp4V2DiscontinuityTime,'extremeBgp4V2PeerTable':extremeBgp4V2PeerTable,'extremeBgp4V2PeerEntry':extremeBgp4V2PeerEntry,_G:extremeBgp4V2PeerInstance,_A6:extremeBgp4V2PeerLocalAddrType,_A7:extremeBgp4V2PeerLocalAddr,_I:extremeBgp4V2PeerRemoteAddrType,_J:extremeBgp4V2PeerRemoteAddr,_M:extremeBgp4V2PeerLocalPort,_A8:extremeBgp4V2PeerLocalAs,_AA:extremeBgp4V2PeerLocalIdentifier,_N:extremeBgp4V2PeerRemotePort,_A9:extremeBgp4V2PeerRemoteAs,_AB:extremeBgp4V2PeerRemoteIdentifier,_A5:extremeBgp4V2PeerAdminStatus,_L:extremeBgp4V2PeerState,_AC:extremeBgp4V2PeerDescription,'extremeBgp4V2PeerErrorsTable':extremeBgp4V2PeerErrorsTable,_b:extremeBgp4V2PeerErrorsEntry,_T:extremeBgp4V2PeerLastErrorCodeReceived,_U:extremeBgp4V2PeerLastErrorSubCodeReceived,_z:extremeBgp4V2PeerLastErrorReceivedTime,_V:extremeBgp4V2PeerLastErrorReceivedText,_y:extremeBgp4V2PeerLastErrorReceivedData,_A0:extremeBgp4V2PeerLastErrorCodeSent,_A1:extremeBgp4V2PeerLastErrorSubCodeSent,_A3:extremeBgp4V2PeerLastErrorSentTime,_A4:extremeBgp4V2PeerLastErrorSentText,_A2:extremeBgp4V2PeerLastErrorSentData,'extremeBgp4V2PeerEventTimesTable':extremeBgp4V2PeerEventTimesTable,_c:extremeBgp4V2PeerEventTimesEntry,_h:extremeBgp4V2PeerFsmEstablishedTime,_i:extremeBgp4V2PeerInUpdatesElapsedTime,'extremeBgp4V2PeerConfiguredTimersTable':extremeBgp4V2PeerConfiguredTimersTable,_d:extremeBgp4V2PeerConfiguredTimersEntry,_j:extremeBgp4V2PeerConnectRetryInterval,_k:extremeBgp4V2PeerHoldTimeConfigured,_l:extremeBgp4V2PeerKeepAliveConfigured,_m:extremeBgp4V2PeerMinASOrigInterval,_n:extremeBgp4V2PeerMinRouteAdverInterval,'extremeBgp4V2PeerNegotiatedTimersTable':extremeBgp4V2PeerNegotiatedTimersTable,_e:extremeBgp4V2PeerNegotiatedTimersEntry,_o:extremeBgp4V2PeerHoldTime,_p:extremeBgp4V2PeerKeepAlive,'extremeBgp4V2PeerCountersTable':extremeBgp4V2PeerCountersTable,_f:extremeBgp4V2PeerCountersEntry,_q:extremeBgp4V2PeerInUpdates,_r:extremeBgp4V2PeerOutUpdates,_s:extremeBgp4V2PeerInTotalMessages,_t:extremeBgp4V2PeerOutTotalMessages,_u:extremeBgp4V2PeerFsmEstablishedTransitions,'extremeBgp4V2PrefixGaugesTable':extremeBgp4V2PrefixGaugesTable,'extremeBgp4V2PrefixGaugesEntry':extremeBgp4V2PrefixGaugesEntry,_X:extremeBgp4V2PrefixGaugesAfi,_Y:extremeBgp4V2PrefixGaugesSafi,_v:extremeBgp4V2PrefixInPrefixes,_w:extremeBgp4V2PrefixInPrefixesAccepted,_x:extremeBgp4V2PrefixOutPrefixes,'extremeBgp4V2NlriTable':extremeBgp4V2NlriTable,'extremeBgp4V2NlriEntry':extremeBgp4V2NlriEntry,_Z:extremeBgp4V2NlriIndex,_O:extremeBgp4V2NlriAfi,_P:extremeBgp4V2NlriSafi,_Q:extremeBgp4V2NlriPrefixType,_R:extremeBgp4V2NlriPrefix,_S:extremeBgp4V2NlriPrefixLen,_AF:extremeBgp4V2NlriBest,_AG:extremeBgp4V2NlriCalcLocalPref,_AU:extremeBgp4V2NlriOrigin,_AR:extremeBgp4V2NlriNextHopAddrType,_AQ:extremeBgp4V2NlriNextHopAddr,_AS:extremeBgp4V2NlriLinkLocalNextHopAddrType,_AT:extremeBgp4V2NlriLinkLocalNextHopAddr,_AN:extremeBgp4V2NlriLocalPrefPresent,_AM:extremeBgp4V2NlriLocalPref,_AP:extremeBgp4V2NlriMedPresent,_AO:extremeBgp4V2NlriMed,_AL:extremeBgp4V2NlriAtomicAggregate,_AI:extremeBgp4V2NlriAggregatorPresent,_AJ:extremeBgp4V2NlriAggregatorAS,_AK:extremeBgp4V2NlriAggregatorAddr,_AD:extremeBgp4V2NlriAsPathCalcLength,_AE:extremeBgp4V2NlriAsPathString,_AV:extremeBgp4V2NlriAsPath,_AW:extremeBgp4V2NlriPathAttrUnknown,'extremeBgp4V2AdjRibsOutTable':extremeBgp4V2AdjRibsOutTable,'extremeBgp4V2AdjRibsOutEntry':extremeBgp4V2AdjRibsOutEntry,_a:extremeBgp4V2AdjRibsOutIndex,_AH:extremeBgp4V2AdjRibsOutRoute,'extremeBgp4V2Conformance':extremeBgp4V2Conformance,'extremeBgp4V2Compliances':extremeBgp4V2Compliances,'extremeBgp4V2Compliance':extremeBgp4V2Compliance,'extremeBgp4V2Groups':extremeBgp4V2Groups,_Ae:extremeBgp4V2GlobalsGroup,_AZ:extremeBgp4V2StdMIBTimersGroup,_Aa:extremeBgp4V2StdMIBCountersGroup,_Ab:extremeBgp4V2StdMIBErrorsGroup,_Ac:extremeBgp4V2StdMIBPeerGroup,_Ad:extremeBgp4V2StdMIBNlriGroup,_Af:extremeBgp4V2StdMIBNotificationGroup})