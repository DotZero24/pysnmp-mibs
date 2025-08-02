_Z='os10bgp4V2PeerCountersEntry'
_Y='os10bgp4V2PeerNegotiatedTimersEntry'
_X='os10bgp4V2PeerConfiguredTimersEntry'
_W='os10bgp4V2PeerEventTimesEntry'
_V='os10bgp4V2PeerErrorsEntry'
_U='os10bgp4V2AdjRibsOutIndex'
_T='os10bgp4V2NlriIndex'
_S='os10bgp4V2PrefixGaugesSafi'
_R='os10bgp4V2PrefixGaugesAfi'
_Q='InetAddress'
_P='os10bgp4V2NlriPrefixLen'
_O='os10bgp4V2NlriPrefix'
_N='os10bgp4V2NlriPrefixType'
_M='os10bgp4V2NlriSafi'
_L='os10bgp4V2NlriAfi'
_K='Integer32'
_J='os10bgp4V2PeerRemoteAddr'
_I='os10bgp4V2PeerRemoteAddrType'
_H='OctetString'
_G='os10bgp4V2PeerInstance'
_F='seconds'
_E='not-accessible'
_D='Unsigned32'
_C='DELLEMC-OS10-BGP4V2-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
os10Experiment,=mibBuilder.importSymbols('DELLEMC-OS10-SMI-MIB','os10Experiment')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_Q,'InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
os10Bgp4V2Mib=ModuleIdentity((1,3,6,1,4,1,674,11000,5000,200,1))
if mibBuilder.loadTexts:os10Bgp4V2Mib.setRevisions(('2020-02-25 12:00','2018-07-04 12:00','2014-01-24 00:00'))
class Os10Bgp4V2IdentifierTC(TextualConvention,OctetString):status=_A;displayHint='1d.';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class Os10Bgp4V2AddressFamilyIdentifierTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
class Os10Bgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('mpls',4)))
_Os10bgp4V2Notifications_ObjectIdentity=ObjectIdentity
os10bgp4V2Notifications=_Os10bgp4V2Notifications_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,200,1,0))
_Os10bgp4V2Objects_ObjectIdentity=ObjectIdentity
os10bgp4V2Objects=_Os10bgp4V2Objects_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,200,1,1))
_Os10bgp4V2DiscontinuityTable_Object=MibTable
os10bgp4V2DiscontinuityTable=_Os10bgp4V2DiscontinuityTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,1))
if mibBuilder.loadTexts:os10bgp4V2DiscontinuityTable.setStatus(_A)
_Os10bgp4V2DiscontinuityEntry_Object=MibTableRow
os10bgp4V2DiscontinuityEntry=_Os10bgp4V2DiscontinuityEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,1,1))
os10bgp4V2DiscontinuityEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:os10bgp4V2DiscontinuityEntry.setStatus(_A)
_Os10bgp4V2DiscontinuityTime_Type=TimeStamp
_Os10bgp4V2DiscontinuityTime_Object=MibTableColumn
os10bgp4V2DiscontinuityTime=_Os10bgp4V2DiscontinuityTime_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,1,1,1),_Os10bgp4V2DiscontinuityTime_Type())
os10bgp4V2DiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2DiscontinuityTime.setStatus(_A)
_Os10bgp4V2PeerTable_Object=MibTable
os10bgp4V2PeerTable=_Os10bgp4V2PeerTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2))
if mibBuilder.loadTexts:os10bgp4V2PeerTable.setStatus(_A)
_Os10bgp4V2PeerEntry_Object=MibTableRow
os10bgp4V2PeerEntry=_Os10bgp4V2PeerEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1))
os10bgp4V2PeerEntry.setIndexNames((0,_C,_G),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:os10bgp4V2PeerEntry.setStatus(_A)
class _Os10bgp4V2PeerInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Os10bgp4V2PeerInstance_Type.__name__=_D
_Os10bgp4V2PeerInstance_Object=MibTableColumn
os10bgp4V2PeerInstance=_Os10bgp4V2PeerInstance_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,1),_Os10bgp4V2PeerInstance_Type())
os10bgp4V2PeerInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2PeerInstance.setStatus(_A)
_Os10bgp4V2PeerLocalAddrType_Type=InetAddressType
_Os10bgp4V2PeerLocalAddrType_Object=MibTableColumn
os10bgp4V2PeerLocalAddrType=_Os10bgp4V2PeerLocalAddrType_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,2),_Os10bgp4V2PeerLocalAddrType_Type())
os10bgp4V2PeerLocalAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLocalAddrType.setStatus(_A)
_Os10bgp4V2PeerLocalAddr_Type=InetAddress
_Os10bgp4V2PeerLocalAddr_Object=MibTableColumn
os10bgp4V2PeerLocalAddr=_Os10bgp4V2PeerLocalAddr_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,3),_Os10bgp4V2PeerLocalAddr_Type())
os10bgp4V2PeerLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLocalAddr.setStatus(_A)
_Os10bgp4V2PeerRemoteAddrType_Type=InetAddressType
_Os10bgp4V2PeerRemoteAddrType_Object=MibTableColumn
os10bgp4V2PeerRemoteAddrType=_Os10bgp4V2PeerRemoteAddrType_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,4),_Os10bgp4V2PeerRemoteAddrType_Type())
os10bgp4V2PeerRemoteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2PeerRemoteAddrType.setStatus(_A)
_Os10bgp4V2PeerRemoteAddr_Type=InetAddress
_Os10bgp4V2PeerRemoteAddr_Object=MibTableColumn
os10bgp4V2PeerRemoteAddr=_Os10bgp4V2PeerRemoteAddr_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,5),_Os10bgp4V2PeerRemoteAddr_Type())
os10bgp4V2PeerRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2PeerRemoteAddr.setStatus(_A)
_Os10bgp4V2PeerLocalPort_Type=InetPortNumber
_Os10bgp4V2PeerLocalPort_Object=MibTableColumn
os10bgp4V2PeerLocalPort=_Os10bgp4V2PeerLocalPort_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,6),_Os10bgp4V2PeerLocalPort_Type())
os10bgp4V2PeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLocalPort.setStatus(_A)
_Os10bgp4V2PeerLocalAs_Type=InetAutonomousSystemNumber
_Os10bgp4V2PeerLocalAs_Object=MibTableColumn
os10bgp4V2PeerLocalAs=_Os10bgp4V2PeerLocalAs_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,7),_Os10bgp4V2PeerLocalAs_Type())
os10bgp4V2PeerLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLocalAs.setStatus(_A)
_Os10bgp4V2PeerLocalIdentifier_Type=Os10Bgp4V2IdentifierTC
_Os10bgp4V2PeerLocalIdentifier_Object=MibTableColumn
os10bgp4V2PeerLocalIdentifier=_Os10bgp4V2PeerLocalIdentifier_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,8),_Os10bgp4V2PeerLocalIdentifier_Type())
os10bgp4V2PeerLocalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLocalIdentifier.setStatus(_A)
_Os10bgp4V2PeerRemotePort_Type=InetPortNumber
_Os10bgp4V2PeerRemotePort_Object=MibTableColumn
os10bgp4V2PeerRemotePort=_Os10bgp4V2PeerRemotePort_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,9),_Os10bgp4V2PeerRemotePort_Type())
os10bgp4V2PeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerRemotePort.setStatus(_A)
_Os10bgp4V2PeerRemoteAs_Type=InetAutonomousSystemNumber
_Os10bgp4V2PeerRemoteAs_Object=MibTableColumn
os10bgp4V2PeerRemoteAs=_Os10bgp4V2PeerRemoteAs_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,10),_Os10bgp4V2PeerRemoteAs_Type())
os10bgp4V2PeerRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerRemoteAs.setStatus(_A)
_Os10bgp4V2PeerRemoteIdentifier_Type=Os10Bgp4V2IdentifierTC
_Os10bgp4V2PeerRemoteIdentifier_Object=MibTableColumn
os10bgp4V2PeerRemoteIdentifier=_Os10bgp4V2PeerRemoteIdentifier_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,11),_Os10bgp4V2PeerRemoteIdentifier_Type())
os10bgp4V2PeerRemoteIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerRemoteIdentifier.setStatus(_A)
class _Os10bgp4V2PeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halted',1),('running',2)))
_Os10bgp4V2PeerAdminStatus_Type.__name__=_K
_Os10bgp4V2PeerAdminStatus_Object=MibTableColumn
os10bgp4V2PeerAdminStatus=_Os10bgp4V2PeerAdminStatus_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,12),_Os10bgp4V2PeerAdminStatus_Type())
os10bgp4V2PeerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerAdminStatus.setStatus(_A)
class _Os10bgp4V2PeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_Os10bgp4V2PeerState_Type.__name__=_K
_Os10bgp4V2PeerState_Object=MibTableColumn
os10bgp4V2PeerState=_Os10bgp4V2PeerState_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,13),_Os10bgp4V2PeerState_Type())
os10bgp4V2PeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerState.setStatus(_A)
_Os10bgp4V2PeerDescription_Type=SnmpAdminString
_Os10bgp4V2PeerDescription_Object=MibTableColumn
os10bgp4V2PeerDescription=_Os10bgp4V2PeerDescription_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,2,1,14),_Os10bgp4V2PeerDescription_Type())
os10bgp4V2PeerDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerDescription.setStatus(_A)
_Os10bgp4V2PeerErrorsTable_Object=MibTable
os10bgp4V2PeerErrorsTable=_Os10bgp4V2PeerErrorsTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3))
if mibBuilder.loadTexts:os10bgp4V2PeerErrorsTable.setStatus(_A)
_Os10bgp4V2PeerErrorsEntry_Object=MibTableRow
os10bgp4V2PeerErrorsEntry=_Os10bgp4V2PeerErrorsEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1))
if mibBuilder.loadTexts:os10bgp4V2PeerErrorsEntry.setStatus(_A)
class _Os10bgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Os10bgp4V2PeerLastErrorCodeReceived_Type.__name__=_D
_Os10bgp4V2PeerLastErrorCodeReceived_Object=MibTableColumn
os10bgp4V2PeerLastErrorCodeReceived=_Os10bgp4V2PeerLastErrorCodeReceived_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,1),_Os10bgp4V2PeerLastErrorCodeReceived_Type())
os10bgp4V2PeerLastErrorCodeReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorCodeReceived.setStatus(_A)
class _Os10bgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Os10bgp4V2PeerLastErrorSubCodeReceived_Type.__name__=_D
_Os10bgp4V2PeerLastErrorSubCodeReceived_Object=MibTableColumn
os10bgp4V2PeerLastErrorSubCodeReceived=_Os10bgp4V2PeerLastErrorSubCodeReceived_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,2),_Os10bgp4V2PeerLastErrorSubCodeReceived_Type())
os10bgp4V2PeerLastErrorSubCodeReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorSubCodeReceived.setStatus(_A)
_Os10bgp4V2PeerLastErrorReceivedTime_Type=TimeStamp
_Os10bgp4V2PeerLastErrorReceivedTime_Object=MibTableColumn
os10bgp4V2PeerLastErrorReceivedTime=_Os10bgp4V2PeerLastErrorReceivedTime_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,3),_Os10bgp4V2PeerLastErrorReceivedTime_Type())
os10bgp4V2PeerLastErrorReceivedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorReceivedTime.setStatus(_A)
_Os10bgp4V2PeerLastErrorReceivedText_Type=SnmpAdminString
_Os10bgp4V2PeerLastErrorReceivedText_Object=MibTableColumn
os10bgp4V2PeerLastErrorReceivedText=_Os10bgp4V2PeerLastErrorReceivedText_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,4),_Os10bgp4V2PeerLastErrorReceivedText_Type())
os10bgp4V2PeerLastErrorReceivedText.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorReceivedText.setStatus(_A)
class _Os10bgp4V2PeerLastErrorReceivedData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_Os10bgp4V2PeerLastErrorReceivedData_Type.__name__=_H
_Os10bgp4V2PeerLastErrorReceivedData_Object=MibTableColumn
os10bgp4V2PeerLastErrorReceivedData=_Os10bgp4V2PeerLastErrorReceivedData_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,5),_Os10bgp4V2PeerLastErrorReceivedData_Type())
os10bgp4V2PeerLastErrorReceivedData.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorReceivedData.setStatus(_A)
class _Os10bgp4V2PeerLastErrorCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Os10bgp4V2PeerLastErrorCodeSent_Type.__name__=_D
_Os10bgp4V2PeerLastErrorCodeSent_Object=MibTableColumn
os10bgp4V2PeerLastErrorCodeSent=_Os10bgp4V2PeerLastErrorCodeSent_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,6),_Os10bgp4V2PeerLastErrorCodeSent_Type())
os10bgp4V2PeerLastErrorCodeSent.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorCodeSent.setStatus(_A)
class _Os10bgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Os10bgp4V2PeerLastErrorSubCodeSent_Type.__name__=_D
_Os10bgp4V2PeerLastErrorSubCodeSent_Object=MibTableColumn
os10bgp4V2PeerLastErrorSubCodeSent=_Os10bgp4V2PeerLastErrorSubCodeSent_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,7),_Os10bgp4V2PeerLastErrorSubCodeSent_Type())
os10bgp4V2PeerLastErrorSubCodeSent.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorSubCodeSent.setStatus(_A)
_Os10bgp4V2PeerLastErrorSentTime_Type=TimeStamp
_Os10bgp4V2PeerLastErrorSentTime_Object=MibTableColumn
os10bgp4V2PeerLastErrorSentTime=_Os10bgp4V2PeerLastErrorSentTime_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,8),_Os10bgp4V2PeerLastErrorSentTime_Type())
os10bgp4V2PeerLastErrorSentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorSentTime.setStatus(_A)
_Os10bgp4V2PeerLastErrorSentText_Type=SnmpAdminString
_Os10bgp4V2PeerLastErrorSentText_Object=MibTableColumn
os10bgp4V2PeerLastErrorSentText=_Os10bgp4V2PeerLastErrorSentText_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,9),_Os10bgp4V2PeerLastErrorSentText_Type())
os10bgp4V2PeerLastErrorSentText.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorSentText.setStatus(_A)
class _Os10bgp4V2PeerLastErrorSentData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_Os10bgp4V2PeerLastErrorSentData_Type.__name__=_H
_Os10bgp4V2PeerLastErrorSentData_Object=MibTableColumn
os10bgp4V2PeerLastErrorSentData=_Os10bgp4V2PeerLastErrorSentData_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,3,1,10),_Os10bgp4V2PeerLastErrorSentData_Type())
os10bgp4V2PeerLastErrorSentData.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerLastErrorSentData.setStatus(_A)
_Os10bgp4V2PeerEventTimesTable_Object=MibTable
os10bgp4V2PeerEventTimesTable=_Os10bgp4V2PeerEventTimesTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,4))
if mibBuilder.loadTexts:os10bgp4V2PeerEventTimesTable.setStatus(_A)
_Os10bgp4V2PeerEventTimesEntry_Object=MibTableRow
os10bgp4V2PeerEventTimesEntry=_Os10bgp4V2PeerEventTimesEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,4,1))
if mibBuilder.loadTexts:os10bgp4V2PeerEventTimesEntry.setStatus(_A)
_Os10bgp4V2PeerFsmEstablishedTime_Type=Gauge32
_Os10bgp4V2PeerFsmEstablishedTime_Object=MibTableColumn
os10bgp4V2PeerFsmEstablishedTime=_Os10bgp4V2PeerFsmEstablishedTime_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,4,1,1),_Os10bgp4V2PeerFsmEstablishedTime_Type())
os10bgp4V2PeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerFsmEstablishedTime.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerFsmEstablishedTime.setUnits(_F)
_Os10bgp4V2PeerInUpdatesElapsedTime_Type=Gauge32
_Os10bgp4V2PeerInUpdatesElapsedTime_Object=MibTableColumn
os10bgp4V2PeerInUpdatesElapsedTime=_Os10bgp4V2PeerInUpdatesElapsedTime_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,4,1,2),_Os10bgp4V2PeerInUpdatesElapsedTime_Type())
os10bgp4V2PeerInUpdatesElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerInUpdatesElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerInUpdatesElapsedTime.setUnits(_F)
_Os10bgp4V2PeerConfiguredTimersTable_Object=MibTable
os10bgp4V2PeerConfiguredTimersTable=_Os10bgp4V2PeerConfiguredTimersTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5))
if mibBuilder.loadTexts:os10bgp4V2PeerConfiguredTimersTable.setStatus(_A)
_Os10bgp4V2PeerConfiguredTimersEntry_Object=MibTableRow
os10bgp4V2PeerConfiguredTimersEntry=_Os10bgp4V2PeerConfiguredTimersEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5,1))
if mibBuilder.loadTexts:os10bgp4V2PeerConfiguredTimersEntry.setStatus(_A)
class _Os10bgp4V2PeerConnectRetryInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Os10bgp4V2PeerConnectRetryInterval_Type.__name__=_D
_Os10bgp4V2PeerConnectRetryInterval_Object=MibTableColumn
os10bgp4V2PeerConnectRetryInterval=_Os10bgp4V2PeerConnectRetryInterval_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5,1,1),_Os10bgp4V2PeerConnectRetryInterval_Type())
os10bgp4V2PeerConnectRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerConnectRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerConnectRetryInterval.setUnits(_F)
class _Os10bgp4V2PeerHoldTimeConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_Os10bgp4V2PeerHoldTimeConfigured_Type.__name__=_D
_Os10bgp4V2PeerHoldTimeConfigured_Object=MibTableColumn
os10bgp4V2PeerHoldTimeConfigured=_Os10bgp4V2PeerHoldTimeConfigured_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5,1,2),_Os10bgp4V2PeerHoldTimeConfigured_Type())
os10bgp4V2PeerHoldTimeConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerHoldTimeConfigured.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerHoldTimeConfigured.setUnits(_F)
class _Os10bgp4V2PeerKeepAliveConfigured_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_Os10bgp4V2PeerKeepAliveConfigured_Type.__name__=_D
_Os10bgp4V2PeerKeepAliveConfigured_Object=MibTableColumn
os10bgp4V2PeerKeepAliveConfigured=_Os10bgp4V2PeerKeepAliveConfigured_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5,1,3),_Os10bgp4V2PeerKeepAliveConfigured_Type())
os10bgp4V2PeerKeepAliveConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerKeepAliveConfigured.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerKeepAliveConfigured.setUnits(_F)
class _Os10bgp4V2PeerMinASOrigInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Os10bgp4V2PeerMinASOrigInterval_Type.__name__=_D
_Os10bgp4V2PeerMinASOrigInterval_Object=MibTableColumn
os10bgp4V2PeerMinASOrigInterval=_Os10bgp4V2PeerMinASOrigInterval_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5,1,4),_Os10bgp4V2PeerMinASOrigInterval_Type())
os10bgp4V2PeerMinASOrigInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerMinASOrigInterval.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerMinASOrigInterval.setUnits(_F)
class _Os10bgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Os10bgp4V2PeerMinRouteAdverInterval_Type.__name__=_D
_Os10bgp4V2PeerMinRouteAdverInterval_Object=MibTableColumn
os10bgp4V2PeerMinRouteAdverInterval=_Os10bgp4V2PeerMinRouteAdverInterval_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,5,1,5),_Os10bgp4V2PeerMinRouteAdverInterval_Type())
os10bgp4V2PeerMinRouteAdverInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerMinRouteAdverInterval.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerMinRouteAdverInterval.setUnits(_F)
_Os10bgp4V2PeerNegotiatedTimersTable_Object=MibTable
os10bgp4V2PeerNegotiatedTimersTable=_Os10bgp4V2PeerNegotiatedTimersTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,6))
if mibBuilder.loadTexts:os10bgp4V2PeerNegotiatedTimersTable.setStatus(_A)
_Os10bgp4V2PeerNegotiatedTimersEntry_Object=MibTableRow
os10bgp4V2PeerNegotiatedTimersEntry=_Os10bgp4V2PeerNegotiatedTimersEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,6,1))
if mibBuilder.loadTexts:os10bgp4V2PeerNegotiatedTimersEntry.setStatus(_A)
class _Os10bgp4V2PeerHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_Os10bgp4V2PeerHoldTime_Type.__name__=_D
_Os10bgp4V2PeerHoldTime_Object=MibTableColumn
os10bgp4V2PeerHoldTime=_Os10bgp4V2PeerHoldTime_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,6,1,1),_Os10bgp4V2PeerHoldTime_Type())
os10bgp4V2PeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerHoldTime.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerHoldTime.setUnits(_F)
class _Os10bgp4V2PeerKeepAlive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_Os10bgp4V2PeerKeepAlive_Type.__name__=_D
_Os10bgp4V2PeerKeepAlive_Object=MibTableColumn
os10bgp4V2PeerKeepAlive=_Os10bgp4V2PeerKeepAlive_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,6,1,2),_Os10bgp4V2PeerKeepAlive_Type())
os10bgp4V2PeerKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:os10bgp4V2PeerKeepAlive.setUnits(_F)
_Os10bgp4V2PeerCountersTable_Object=MibTable
os10bgp4V2PeerCountersTable=_Os10bgp4V2PeerCountersTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7))
if mibBuilder.loadTexts:os10bgp4V2PeerCountersTable.setStatus(_A)
_Os10bgp4V2PeerCountersEntry_Object=MibTableRow
os10bgp4V2PeerCountersEntry=_Os10bgp4V2PeerCountersEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7,1))
if mibBuilder.loadTexts:os10bgp4V2PeerCountersEntry.setStatus(_A)
_Os10bgp4V2PeerInUpdates_Type=Counter32
_Os10bgp4V2PeerInUpdates_Object=MibTableColumn
os10bgp4V2PeerInUpdates=_Os10bgp4V2PeerInUpdates_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7,1,1),_Os10bgp4V2PeerInUpdates_Type())
os10bgp4V2PeerInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerInUpdates.setStatus(_A)
_Os10bgp4V2PeerOutUpdates_Type=Counter32
_Os10bgp4V2PeerOutUpdates_Object=MibTableColumn
os10bgp4V2PeerOutUpdates=_Os10bgp4V2PeerOutUpdates_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7,1,2),_Os10bgp4V2PeerOutUpdates_Type())
os10bgp4V2PeerOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerOutUpdates.setStatus(_A)
_Os10bgp4V2PeerInTotalMessages_Type=Counter32
_Os10bgp4V2PeerInTotalMessages_Object=MibTableColumn
os10bgp4V2PeerInTotalMessages=_Os10bgp4V2PeerInTotalMessages_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7,1,3),_Os10bgp4V2PeerInTotalMessages_Type())
os10bgp4V2PeerInTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerInTotalMessages.setStatus(_A)
_Os10bgp4V2PeerOutTotalMessages_Type=Counter32
_Os10bgp4V2PeerOutTotalMessages_Object=MibTableColumn
os10bgp4V2PeerOutTotalMessages=_Os10bgp4V2PeerOutTotalMessages_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7,1,4),_Os10bgp4V2PeerOutTotalMessages_Type())
os10bgp4V2PeerOutTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerOutTotalMessages.setStatus(_A)
_Os10bgp4V2PeerFsmEstablishedTransitions_Type=Counter32
_Os10bgp4V2PeerFsmEstablishedTransitions_Object=MibTableColumn
os10bgp4V2PeerFsmEstablishedTransitions=_Os10bgp4V2PeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,7,1,5),_Os10bgp4V2PeerFsmEstablishedTransitions_Type())
os10bgp4V2PeerFsmEstablishedTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PeerFsmEstablishedTransitions.setStatus(_A)
_Os10bgp4V2PrefixGaugesTable_Object=MibTable
os10bgp4V2PrefixGaugesTable=_Os10bgp4V2PrefixGaugesTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8))
if mibBuilder.loadTexts:os10bgp4V2PrefixGaugesTable.setStatus(_A)
_Os10bgp4V2PrefixGaugesEntry_Object=MibTableRow
os10bgp4V2PrefixGaugesEntry=_Os10bgp4V2PrefixGaugesEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8,1))
os10bgp4V2PrefixGaugesEntry.setIndexNames((0,_C,_G),(0,_C,_I),(0,_C,_J),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:os10bgp4V2PrefixGaugesEntry.setStatus(_A)
_Os10bgp4V2PrefixGaugesAfi_Type=Os10Bgp4V2AddressFamilyIdentifierTC
_Os10bgp4V2PrefixGaugesAfi_Object=MibTableColumn
os10bgp4V2PrefixGaugesAfi=_Os10bgp4V2PrefixGaugesAfi_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8,1,1),_Os10bgp4V2PrefixGaugesAfi_Type())
os10bgp4V2PrefixGaugesAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2PrefixGaugesAfi.setStatus(_A)
_Os10bgp4V2PrefixGaugesSafi_Type=Os10Bgp4V2SubsequentAddressFamilyIdentifierTC
_Os10bgp4V2PrefixGaugesSafi_Object=MibTableColumn
os10bgp4V2PrefixGaugesSafi=_Os10bgp4V2PrefixGaugesSafi_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8,1,2),_Os10bgp4V2PrefixGaugesSafi_Type())
os10bgp4V2PrefixGaugesSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2PrefixGaugesSafi.setStatus(_A)
_Os10bgp4V2PrefixInPrefixes_Type=Gauge32
_Os10bgp4V2PrefixInPrefixes_Object=MibTableColumn
os10bgp4V2PrefixInPrefixes=_Os10bgp4V2PrefixInPrefixes_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8,1,3),_Os10bgp4V2PrefixInPrefixes_Type())
os10bgp4V2PrefixInPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PrefixInPrefixes.setStatus(_A)
_Os10bgp4V2PrefixInPrefixesAccepted_Type=Gauge32
_Os10bgp4V2PrefixInPrefixesAccepted_Object=MibTableColumn
os10bgp4V2PrefixInPrefixesAccepted=_Os10bgp4V2PrefixInPrefixesAccepted_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8,1,4),_Os10bgp4V2PrefixInPrefixesAccepted_Type())
os10bgp4V2PrefixInPrefixesAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PrefixInPrefixesAccepted.setStatus(_A)
_Os10bgp4V2PrefixOutPrefixes_Type=Gauge32
_Os10bgp4V2PrefixOutPrefixes_Object=MibTableColumn
os10bgp4V2PrefixOutPrefixes=_Os10bgp4V2PrefixOutPrefixes_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,8,1,5),_Os10bgp4V2PrefixOutPrefixes_Type())
os10bgp4V2PrefixOutPrefixes.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2PrefixOutPrefixes.setStatus(_A)
_Os10bgp4V2NlriTable_Object=MibTable
os10bgp4V2NlriTable=_Os10bgp4V2NlriTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9))
if mibBuilder.loadTexts:os10bgp4V2NlriTable.setStatus(_A)
_Os10bgp4V2NlriEntry_Object=MibTableRow
os10bgp4V2NlriEntry=_Os10bgp4V2NlriEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1))
os10bgp4V2NlriEntry.setIndexNames((0,_C,_G),(0,_C,_L),(0,_C,_M),(0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_I),(0,_C,_J),(0,_C,_T))
if mibBuilder.loadTexts:os10bgp4V2NlriEntry.setStatus(_A)
class _Os10bgp4V2NlriIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Os10bgp4V2NlriIndex_Type.__name__=_D
_Os10bgp4V2NlriIndex_Object=MibTableColumn
os10bgp4V2NlriIndex=_Os10bgp4V2NlriIndex_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,1),_Os10bgp4V2NlriIndex_Type())
os10bgp4V2NlriIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2NlriIndex.setStatus(_A)
_Os10bgp4V2NlriAfi_Type=Os10Bgp4V2AddressFamilyIdentifierTC
_Os10bgp4V2NlriAfi_Object=MibTableColumn
os10bgp4V2NlriAfi=_Os10bgp4V2NlriAfi_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,2),_Os10bgp4V2NlriAfi_Type())
os10bgp4V2NlriAfi.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2NlriAfi.setStatus(_A)
_Os10bgp4V2NlriSafi_Type=Os10Bgp4V2SubsequentAddressFamilyIdentifierTC
_Os10bgp4V2NlriSafi_Object=MibTableColumn
os10bgp4V2NlriSafi=_Os10bgp4V2NlriSafi_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,3),_Os10bgp4V2NlriSafi_Type())
os10bgp4V2NlriSafi.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2NlriSafi.setStatus(_A)
_Os10bgp4V2NlriPrefixType_Type=InetAddressType
_Os10bgp4V2NlriPrefixType_Object=MibTableColumn
os10bgp4V2NlriPrefixType=_Os10bgp4V2NlriPrefixType_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,4),_Os10bgp4V2NlriPrefixType_Type())
os10bgp4V2NlriPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2NlriPrefixType.setStatus(_A)
_Os10bgp4V2NlriPrefix_Type=InetAddress
_Os10bgp4V2NlriPrefix_Object=MibTableColumn
os10bgp4V2NlriPrefix=_Os10bgp4V2NlriPrefix_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,5),_Os10bgp4V2NlriPrefix_Type())
os10bgp4V2NlriPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2NlriPrefix.setStatus(_A)
_Os10bgp4V2NlriPrefixLen_Type=InetAddressPrefixLength
_Os10bgp4V2NlriPrefixLen_Object=MibTableColumn
os10bgp4V2NlriPrefixLen=_Os10bgp4V2NlriPrefixLen_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,6),_Os10bgp4V2NlriPrefixLen_Type())
os10bgp4V2NlriPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2NlriPrefixLen.setStatus(_A)
_Os10bgp4V2NlriBest_Type=TruthValue
_Os10bgp4V2NlriBest_Object=MibTableColumn
os10bgp4V2NlriBest=_Os10bgp4V2NlriBest_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,7),_Os10bgp4V2NlriBest_Type())
os10bgp4V2NlriBest.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriBest.setStatus(_A)
_Os10bgp4V2NlriCalcLocalPref_Type=Unsigned32
_Os10bgp4V2NlriCalcLocalPref_Object=MibTableColumn
os10bgp4V2NlriCalcLocalPref=_Os10bgp4V2NlriCalcLocalPref_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,8),_Os10bgp4V2NlriCalcLocalPref_Type())
os10bgp4V2NlriCalcLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriCalcLocalPref.setStatus(_A)
class _Os10bgp4V2NlriOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_Os10bgp4V2NlriOrigin_Type.__name__=_K
_Os10bgp4V2NlriOrigin_Object=MibTableColumn
os10bgp4V2NlriOrigin=_Os10bgp4V2NlriOrigin_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,9),_Os10bgp4V2NlriOrigin_Type())
os10bgp4V2NlriOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriOrigin.setStatus(_A)
_Os10bgp4V2NlriNextHopAddrType_Type=InetAddressType
_Os10bgp4V2NlriNextHopAddrType_Object=MibTableColumn
os10bgp4V2NlriNextHopAddrType=_Os10bgp4V2NlriNextHopAddrType_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,10),_Os10bgp4V2NlriNextHopAddrType_Type())
os10bgp4V2NlriNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriNextHopAddrType.setStatus(_A)
class _Os10bgp4V2NlriNextHopAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_Os10bgp4V2NlriNextHopAddr_Type.__name__=_Q
_Os10bgp4V2NlriNextHopAddr_Object=MibTableColumn
os10bgp4V2NlriNextHopAddr=_Os10bgp4V2NlriNextHopAddr_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,11),_Os10bgp4V2NlriNextHopAddr_Type())
os10bgp4V2NlriNextHopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriNextHopAddr.setStatus(_A)
_Os10bgp4V2NlriLinkLocalNextHopAddrType_Type=InetAddressType
_Os10bgp4V2NlriLinkLocalNextHopAddrType_Object=MibTableColumn
os10bgp4V2NlriLinkLocalNextHopAddrType=_Os10bgp4V2NlriLinkLocalNextHopAddrType_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,12),_Os10bgp4V2NlriLinkLocalNextHopAddrType_Type())
os10bgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriLinkLocalNextHopAddrType.setStatus(_A)
_Os10bgp4V2NlriLinkLocalNextHopAddr_Type=InetAddress
_Os10bgp4V2NlriLinkLocalNextHopAddr_Object=MibTableColumn
os10bgp4V2NlriLinkLocalNextHopAddr=_Os10bgp4V2NlriLinkLocalNextHopAddr_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,13),_Os10bgp4V2NlriLinkLocalNextHopAddr_Type())
os10bgp4V2NlriLinkLocalNextHopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriLinkLocalNextHopAddr.setStatus(_A)
_Os10bgp4V2NlriLocalPrefPresent_Type=TruthValue
_Os10bgp4V2NlriLocalPrefPresent_Object=MibTableColumn
os10bgp4V2NlriLocalPrefPresent=_Os10bgp4V2NlriLocalPrefPresent_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,14),_Os10bgp4V2NlriLocalPrefPresent_Type())
os10bgp4V2NlriLocalPrefPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriLocalPrefPresent.setStatus(_A)
_Os10bgp4V2NlriLocalPref_Type=Unsigned32
_Os10bgp4V2NlriLocalPref_Object=MibTableColumn
os10bgp4V2NlriLocalPref=_Os10bgp4V2NlriLocalPref_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,15),_Os10bgp4V2NlriLocalPref_Type())
os10bgp4V2NlriLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriLocalPref.setStatus(_A)
_Os10bgp4V2NlriMedPresent_Type=TruthValue
_Os10bgp4V2NlriMedPresent_Object=MibTableColumn
os10bgp4V2NlriMedPresent=_Os10bgp4V2NlriMedPresent_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,16),_Os10bgp4V2NlriMedPresent_Type())
os10bgp4V2NlriMedPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriMedPresent.setStatus(_A)
_Os10bgp4V2NlriMed_Type=Unsigned32
_Os10bgp4V2NlriMed_Object=MibTableColumn
os10bgp4V2NlriMed=_Os10bgp4V2NlriMed_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,17),_Os10bgp4V2NlriMed_Type())
os10bgp4V2NlriMed.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriMed.setStatus(_A)
_Os10bgp4V2NlriAtomicAggregate_Type=TruthValue
_Os10bgp4V2NlriAtomicAggregate_Object=MibTableColumn
os10bgp4V2NlriAtomicAggregate=_Os10bgp4V2NlriAtomicAggregate_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,18),_Os10bgp4V2NlriAtomicAggregate_Type())
os10bgp4V2NlriAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAtomicAggregate.setStatus(_A)
_Os10bgp4V2NlriAggregatorPresent_Type=TruthValue
_Os10bgp4V2NlriAggregatorPresent_Object=MibTableColumn
os10bgp4V2NlriAggregatorPresent=_Os10bgp4V2NlriAggregatorPresent_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,19),_Os10bgp4V2NlriAggregatorPresent_Type())
os10bgp4V2NlriAggregatorPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAggregatorPresent.setStatus(_A)
_Os10bgp4V2NlriAggregatorAS_Type=InetAutonomousSystemNumber
_Os10bgp4V2NlriAggregatorAS_Object=MibTableColumn
os10bgp4V2NlriAggregatorAS=_Os10bgp4V2NlriAggregatorAS_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,20),_Os10bgp4V2NlriAggregatorAS_Type())
os10bgp4V2NlriAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAggregatorAS.setStatus(_A)
_Os10bgp4V2NlriAggregatorAddr_Type=Os10Bgp4V2IdentifierTC
_Os10bgp4V2NlriAggregatorAddr_Object=MibTableColumn
os10bgp4V2NlriAggregatorAddr=_Os10bgp4V2NlriAggregatorAddr_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,21),_Os10bgp4V2NlriAggregatorAddr_Type())
os10bgp4V2NlriAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAggregatorAddr.setStatus(_A)
_Os10bgp4V2NlriAsPathCalcLength_Type=Unsigned32
_Os10bgp4V2NlriAsPathCalcLength_Object=MibTableColumn
os10bgp4V2NlriAsPathCalcLength=_Os10bgp4V2NlriAsPathCalcLength_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,22),_Os10bgp4V2NlriAsPathCalcLength_Type())
os10bgp4V2NlriAsPathCalcLength.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAsPathCalcLength.setStatus(_A)
_Os10bgp4V2NlriAsPathString_Type=SnmpAdminString
_Os10bgp4V2NlriAsPathString_Object=MibTableColumn
os10bgp4V2NlriAsPathString=_Os10bgp4V2NlriAsPathString_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,23),_Os10bgp4V2NlriAsPathString_Type())
os10bgp4V2NlriAsPathString.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAsPathString.setStatus(_A)
class _Os10bgp4V2NlriAsPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4072))
_Os10bgp4V2NlriAsPath_Type.__name__=_H
_Os10bgp4V2NlriAsPath_Object=MibTableColumn
os10bgp4V2NlriAsPath=_Os10bgp4V2NlriAsPath_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,24),_Os10bgp4V2NlriAsPath_Type())
os10bgp4V2NlriAsPath.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriAsPath.setStatus(_A)
class _Os10bgp4V2NlriPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4072))
_Os10bgp4V2NlriPathAttrUnknown_Type.__name__=_H
_Os10bgp4V2NlriPathAttrUnknown_Object=MibTableColumn
os10bgp4V2NlriPathAttrUnknown=_Os10bgp4V2NlriPathAttrUnknown_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,9,1,25),_Os10bgp4V2NlriPathAttrUnknown_Type())
os10bgp4V2NlriPathAttrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2NlriPathAttrUnknown.setStatus(_A)
_Os10bgp4V2AdjRibsOutTable_Object=MibTable
os10bgp4V2AdjRibsOutTable=_Os10bgp4V2AdjRibsOutTable_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,10))
if mibBuilder.loadTexts:os10bgp4V2AdjRibsOutTable.setStatus(_A)
_Os10bgp4V2AdjRibsOutEntry_Object=MibTableRow
os10bgp4V2AdjRibsOutEntry=_Os10bgp4V2AdjRibsOutEntry_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,10,1))
os10bgp4V2AdjRibsOutEntry.setIndexNames((0,_C,_G),(0,_C,_L),(0,_C,_M),(0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_I),(0,_C,_J),(0,_C,_U))
if mibBuilder.loadTexts:os10bgp4V2AdjRibsOutEntry.setStatus(_A)
class _Os10bgp4V2AdjRibsOutIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Os10bgp4V2AdjRibsOutIndex_Type.__name__=_D
_Os10bgp4V2AdjRibsOutIndex_Object=MibTableColumn
os10bgp4V2AdjRibsOutIndex=_Os10bgp4V2AdjRibsOutIndex_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,10,1,1),_Os10bgp4V2AdjRibsOutIndex_Type())
os10bgp4V2AdjRibsOutIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:os10bgp4V2AdjRibsOutIndex.setStatus(_A)
_Os10bgp4V2AdjRibsOutRoute_Type=RowPointer
_Os10bgp4V2AdjRibsOutRoute_Object=MibTableColumn
os10bgp4V2AdjRibsOutRoute=_Os10bgp4V2AdjRibsOutRoute_Object((1,3,6,1,4,1,674,11000,5000,200,1,1,10,1,2),_Os10bgp4V2AdjRibsOutRoute_Type())
os10bgp4V2AdjRibsOutRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:os10bgp4V2AdjRibsOutRoute.setStatus(_A)
_Os10bgp4V2Conformance_ObjectIdentity=ObjectIdentity
os10bgp4V2Conformance=_Os10bgp4V2Conformance_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,200,1,2))
os10bgp4V2PeerEntry.registerAugmentions((_C,_V))
os10bgp4V2PeerErrorsEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions((_C,_W))
os10bgp4V2PeerEventTimesEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions((_C,_X))
os10bgp4V2PeerConfiguredTimersEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions((_C,_Y))
os10bgp4V2PeerNegotiatedTimersEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions((_C,_Z))
os10bgp4V2PeerCountersEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'Os10Bgp4V2IdentifierTC':Os10Bgp4V2IdentifierTC,'Os10Bgp4V2AddressFamilyIdentifierTC':Os10Bgp4V2AddressFamilyIdentifierTC,'Os10Bgp4V2SubsequentAddressFamilyIdentifierTC':Os10Bgp4V2SubsequentAddressFamilyIdentifierTC,'os10Bgp4V2Mib':os10Bgp4V2Mib,'os10bgp4V2Notifications':os10bgp4V2Notifications,'os10bgp4V2Objects':os10bgp4V2Objects,'os10bgp4V2DiscontinuityTable':os10bgp4V2DiscontinuityTable,'os10bgp4V2DiscontinuityEntry':os10bgp4V2DiscontinuityEntry,'os10bgp4V2DiscontinuityTime':os10bgp4V2DiscontinuityTime,'os10bgp4V2PeerTable':os10bgp4V2PeerTable,'os10bgp4V2PeerEntry':os10bgp4V2PeerEntry,_G:os10bgp4V2PeerInstance,'os10bgp4V2PeerLocalAddrType':os10bgp4V2PeerLocalAddrType,'os10bgp4V2PeerLocalAddr':os10bgp4V2PeerLocalAddr,_I:os10bgp4V2PeerRemoteAddrType,_J:os10bgp4V2PeerRemoteAddr,'os10bgp4V2PeerLocalPort':os10bgp4V2PeerLocalPort,'os10bgp4V2PeerLocalAs':os10bgp4V2PeerLocalAs,'os10bgp4V2PeerLocalIdentifier':os10bgp4V2PeerLocalIdentifier,'os10bgp4V2PeerRemotePort':os10bgp4V2PeerRemotePort,'os10bgp4V2PeerRemoteAs':os10bgp4V2PeerRemoteAs,'os10bgp4V2PeerRemoteIdentifier':os10bgp4V2PeerRemoteIdentifier,'os10bgp4V2PeerAdminStatus':os10bgp4V2PeerAdminStatus,'os10bgp4V2PeerState':os10bgp4V2PeerState,'os10bgp4V2PeerDescription':os10bgp4V2PeerDescription,'os10bgp4V2PeerErrorsTable':os10bgp4V2PeerErrorsTable,_V:os10bgp4V2PeerErrorsEntry,'os10bgp4V2PeerLastErrorCodeReceived':os10bgp4V2PeerLastErrorCodeReceived,'os10bgp4V2PeerLastErrorSubCodeReceived':os10bgp4V2PeerLastErrorSubCodeReceived,'os10bgp4V2PeerLastErrorReceivedTime':os10bgp4V2PeerLastErrorReceivedTime,'os10bgp4V2PeerLastErrorReceivedText':os10bgp4V2PeerLastErrorReceivedText,'os10bgp4V2PeerLastErrorReceivedData':os10bgp4V2PeerLastErrorReceivedData,'os10bgp4V2PeerLastErrorCodeSent':os10bgp4V2PeerLastErrorCodeSent,'os10bgp4V2PeerLastErrorSubCodeSent':os10bgp4V2PeerLastErrorSubCodeSent,'os10bgp4V2PeerLastErrorSentTime':os10bgp4V2PeerLastErrorSentTime,'os10bgp4V2PeerLastErrorSentText':os10bgp4V2PeerLastErrorSentText,'os10bgp4V2PeerLastErrorSentData':os10bgp4V2PeerLastErrorSentData,'os10bgp4V2PeerEventTimesTable':os10bgp4V2PeerEventTimesTable,_W:os10bgp4V2PeerEventTimesEntry,'os10bgp4V2PeerFsmEstablishedTime':os10bgp4V2PeerFsmEstablishedTime,'os10bgp4V2PeerInUpdatesElapsedTime':os10bgp4V2PeerInUpdatesElapsedTime,'os10bgp4V2PeerConfiguredTimersTable':os10bgp4V2PeerConfiguredTimersTable,_X:os10bgp4V2PeerConfiguredTimersEntry,'os10bgp4V2PeerConnectRetryInterval':os10bgp4V2PeerConnectRetryInterval,'os10bgp4V2PeerHoldTimeConfigured':os10bgp4V2PeerHoldTimeConfigured,'os10bgp4V2PeerKeepAliveConfigured':os10bgp4V2PeerKeepAliveConfigured,'os10bgp4V2PeerMinASOrigInterval':os10bgp4V2PeerMinASOrigInterval,'os10bgp4V2PeerMinRouteAdverInterval':os10bgp4V2PeerMinRouteAdverInterval,'os10bgp4V2PeerNegotiatedTimersTable':os10bgp4V2PeerNegotiatedTimersTable,_Y:os10bgp4V2PeerNegotiatedTimersEntry,'os10bgp4V2PeerHoldTime':os10bgp4V2PeerHoldTime,'os10bgp4V2PeerKeepAlive':os10bgp4V2PeerKeepAlive,'os10bgp4V2PeerCountersTable':os10bgp4V2PeerCountersTable,_Z:os10bgp4V2PeerCountersEntry,'os10bgp4V2PeerInUpdates':os10bgp4V2PeerInUpdates,'os10bgp4V2PeerOutUpdates':os10bgp4V2PeerOutUpdates,'os10bgp4V2PeerInTotalMessages':os10bgp4V2PeerInTotalMessages,'os10bgp4V2PeerOutTotalMessages':os10bgp4V2PeerOutTotalMessages,'os10bgp4V2PeerFsmEstablishedTransitions':os10bgp4V2PeerFsmEstablishedTransitions,'os10bgp4V2PrefixGaugesTable':os10bgp4V2PrefixGaugesTable,'os10bgp4V2PrefixGaugesEntry':os10bgp4V2PrefixGaugesEntry,_R:os10bgp4V2PrefixGaugesAfi,_S:os10bgp4V2PrefixGaugesSafi,'os10bgp4V2PrefixInPrefixes':os10bgp4V2PrefixInPrefixes,'os10bgp4V2PrefixInPrefixesAccepted':os10bgp4V2PrefixInPrefixesAccepted,'os10bgp4V2PrefixOutPrefixes':os10bgp4V2PrefixOutPrefixes,'os10bgp4V2NlriTable':os10bgp4V2NlriTable,'os10bgp4V2NlriEntry':os10bgp4V2NlriEntry,_T:os10bgp4V2NlriIndex,_L:os10bgp4V2NlriAfi,_M:os10bgp4V2NlriSafi,_N:os10bgp4V2NlriPrefixType,_O:os10bgp4V2NlriPrefix,_P:os10bgp4V2NlriPrefixLen,'os10bgp4V2NlriBest':os10bgp4V2NlriBest,'os10bgp4V2NlriCalcLocalPref':os10bgp4V2NlriCalcLocalPref,'os10bgp4V2NlriOrigin':os10bgp4V2NlriOrigin,'os10bgp4V2NlriNextHopAddrType':os10bgp4V2NlriNextHopAddrType,'os10bgp4V2NlriNextHopAddr':os10bgp4V2NlriNextHopAddr,'os10bgp4V2NlriLinkLocalNextHopAddrType':os10bgp4V2NlriLinkLocalNextHopAddrType,'os10bgp4V2NlriLinkLocalNextHopAddr':os10bgp4V2NlriLinkLocalNextHopAddr,'os10bgp4V2NlriLocalPrefPresent':os10bgp4V2NlriLocalPrefPresent,'os10bgp4V2NlriLocalPref':os10bgp4V2NlriLocalPref,'os10bgp4V2NlriMedPresent':os10bgp4V2NlriMedPresent,'os10bgp4V2NlriMed':os10bgp4V2NlriMed,'os10bgp4V2NlriAtomicAggregate':os10bgp4V2NlriAtomicAggregate,'os10bgp4V2NlriAggregatorPresent':os10bgp4V2NlriAggregatorPresent,'os10bgp4V2NlriAggregatorAS':os10bgp4V2NlriAggregatorAS,'os10bgp4V2NlriAggregatorAddr':os10bgp4V2NlriAggregatorAddr,'os10bgp4V2NlriAsPathCalcLength':os10bgp4V2NlriAsPathCalcLength,'os10bgp4V2NlriAsPathString':os10bgp4V2NlriAsPathString,'os10bgp4V2NlriAsPath':os10bgp4V2NlriAsPath,'os10bgp4V2NlriPathAttrUnknown':os10bgp4V2NlriPathAttrUnknown,'os10bgp4V2AdjRibsOutTable':os10bgp4V2AdjRibsOutTable,'os10bgp4V2AdjRibsOutEntry':os10bgp4V2AdjRibsOutEntry,_U:os10bgp4V2AdjRibsOutIndex,'os10bgp4V2AdjRibsOutRoute':os10bgp4V2AdjRibsOutRoute,'os10bgp4V2Conformance':os10bgp4V2Conformance})