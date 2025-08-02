_Z='bgp4V2PeerLastErrorReceivedText'
_Y='bgp4V2PeerLastErrorSubCodeReceived'
_X='bgp4V2PeerLastErrorCodeReceived'
_W='bgp4V2PeerEventTimesEntry'
_V='bgp4V2PeerErrorsEntry'
_U='bgp4V2NlriIndex'
_T='bgp4V2NlriPrefixLen'
_S='bgp4V2NlriPrefix'
_R='bgp4V2NlriPrefixType'
_Q='bgp4V2NlriSafi'
_P='bgp4V2NlriAfi'
_O='seconds'
_N='InetAddress'
_M='bgp4V2PeerRemotePort'
_L='bgp4V2PeerLocalPort'
_K='bgp4V2PeerState'
_J='bgp4V2PeerRemoteAddr'
_I='bgp4V2PeerRemoteAddrType'
_H='bgp4V2PeerInstance'
_G='Integer32'
_F='OctetString'
_E='Unsigned32'
_D='not-accessible'
_C='FOUNDRY-BGP4V2-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Bgp4V2AddressFamilyIdentifierTC,Bgp4V2IdentifierTC,Bgp4V2SubsequentAddressFamilyIdentifierTC=mibBuilder.importSymbols('FOUNDRY-BGP4V2-TC-MIB','Bgp4V2AddressFamilyIdentifierTC','Bgp4V2IdentifierTC','Bgp4V2SubsequentAddressFamilyIdentifierTC')
bgp4V2Root,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','bgp4V2Root')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
bgp4V2=ModuleIdentity((1,3,6,1,4,1,1991,3,5,1))
if mibBuilder.loadTexts:bgp4V2.setRevisions(('2011-01-17 00:00',))
_Bgp4V2Notifications_ObjectIdentity=ObjectIdentity
bgp4V2Notifications=_Bgp4V2Notifications_ObjectIdentity((1,3,6,1,4,1,1991,3,5,1,0))
_Bgp4V2Objects_ObjectIdentity=ObjectIdentity
bgp4V2Objects=_Bgp4V2Objects_ObjectIdentity((1,3,6,1,4,1,1991,3,5,1,1))
_Bgp4V2PeerTable_Object=MibTable
bgp4V2PeerTable=_Bgp4V2PeerTable_Object((1,3,6,1,4,1,1991,3,5,1,1,2))
if mibBuilder.loadTexts:bgp4V2PeerTable.setStatus(_A)
_Bgp4V2PeerEntry_Object=MibTableRow
bgp4V2PeerEntry=_Bgp4V2PeerEntry_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1))
bgp4V2PeerEntry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:bgp4V2PeerEntry.setStatus(_A)
class _Bgp4V2PeerInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Bgp4V2PeerInstance_Type.__name__=_E
_Bgp4V2PeerInstance_Object=MibTableColumn
bgp4V2PeerInstance=_Bgp4V2PeerInstance_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,1),_Bgp4V2PeerInstance_Type())
bgp4V2PeerInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2PeerInstance.setStatus(_A)
_Bgp4V2PeerLocalAddrType_Type=InetAddressType
_Bgp4V2PeerLocalAddrType_Object=MibTableColumn
bgp4V2PeerLocalAddrType=_Bgp4V2PeerLocalAddrType_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,2),_Bgp4V2PeerLocalAddrType_Type())
bgp4V2PeerLocalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2PeerLocalAddrType.setStatus(_A)
_Bgp4V2PeerLocalAddr_Type=InetAddress
_Bgp4V2PeerLocalAddr_Object=MibTableColumn
bgp4V2PeerLocalAddr=_Bgp4V2PeerLocalAddr_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,3),_Bgp4V2PeerLocalAddr_Type())
bgp4V2PeerLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2PeerLocalAddr.setStatus(_A)
_Bgp4V2PeerRemoteAddrType_Type=InetAddressType
_Bgp4V2PeerRemoteAddrType_Object=MibTableColumn
bgp4V2PeerRemoteAddrType=_Bgp4V2PeerRemoteAddrType_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,4),_Bgp4V2PeerRemoteAddrType_Type())
bgp4V2PeerRemoteAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2PeerRemoteAddrType.setStatus(_A)
_Bgp4V2PeerRemoteAddr_Type=InetAddress
_Bgp4V2PeerRemoteAddr_Object=MibTableColumn
bgp4V2PeerRemoteAddr=_Bgp4V2PeerRemoteAddr_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,5),_Bgp4V2PeerRemoteAddr_Type())
bgp4V2PeerRemoteAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2PeerRemoteAddr.setStatus(_A)
_Bgp4V2PeerLocalPort_Type=InetPortNumber
_Bgp4V2PeerLocalPort_Object=MibTableColumn
bgp4V2PeerLocalPort=_Bgp4V2PeerLocalPort_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,6),_Bgp4V2PeerLocalPort_Type())
bgp4V2PeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLocalPort.setStatus(_A)
_Bgp4V2PeerLocalAs_Type=InetAutonomousSystemNumber
_Bgp4V2PeerLocalAs_Object=MibTableColumn
bgp4V2PeerLocalAs=_Bgp4V2PeerLocalAs_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,7),_Bgp4V2PeerLocalAs_Type())
bgp4V2PeerLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLocalAs.setStatus(_A)
_Bgp4V2PeerLocalIdentifier_Type=Bgp4V2IdentifierTC
_Bgp4V2PeerLocalIdentifier_Object=MibTableColumn
bgp4V2PeerLocalIdentifier=_Bgp4V2PeerLocalIdentifier_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,8),_Bgp4V2PeerLocalIdentifier_Type())
bgp4V2PeerLocalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLocalIdentifier.setStatus(_A)
_Bgp4V2PeerRemotePort_Type=InetPortNumber
_Bgp4V2PeerRemotePort_Object=MibTableColumn
bgp4V2PeerRemotePort=_Bgp4V2PeerRemotePort_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,9),_Bgp4V2PeerRemotePort_Type())
bgp4V2PeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerRemotePort.setStatus(_A)
_Bgp4V2PeerRemoteAs_Type=InetAutonomousSystemNumber
_Bgp4V2PeerRemoteAs_Object=MibTableColumn
bgp4V2PeerRemoteAs=_Bgp4V2PeerRemoteAs_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,10),_Bgp4V2PeerRemoteAs_Type())
bgp4V2PeerRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerRemoteAs.setStatus(_A)
_Bgp4V2PeerRemoteIdentifier_Type=Bgp4V2IdentifierTC
_Bgp4V2PeerRemoteIdentifier_Object=MibTableColumn
bgp4V2PeerRemoteIdentifier=_Bgp4V2PeerRemoteIdentifier_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,11),_Bgp4V2PeerRemoteIdentifier_Type())
bgp4V2PeerRemoteIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerRemoteIdentifier.setStatus(_A)
class _Bgp4V2PeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('halted',1),('running',2)))
_Bgp4V2PeerAdminStatus_Type.__name__=_G
_Bgp4V2PeerAdminStatus_Object=MibTableColumn
bgp4V2PeerAdminStatus=_Bgp4V2PeerAdminStatus_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,12),_Bgp4V2PeerAdminStatus_Type())
bgp4V2PeerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerAdminStatus.setStatus(_A)
class _Bgp4V2PeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_Bgp4V2PeerState_Type.__name__=_G
_Bgp4V2PeerState_Object=MibTableColumn
bgp4V2PeerState=_Bgp4V2PeerState_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,13),_Bgp4V2PeerState_Type())
bgp4V2PeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerState.setStatus(_A)
_Bgp4V2PeerDescription_Type=SnmpAdminString
_Bgp4V2PeerDescription_Object=MibTableColumn
bgp4V2PeerDescription=_Bgp4V2PeerDescription_Object((1,3,6,1,4,1,1991,3,5,1,1,2,1,14),_Bgp4V2PeerDescription_Type())
bgp4V2PeerDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerDescription.setStatus(_A)
_Bgp4V2PeerErrorsTable_Object=MibTable
bgp4V2PeerErrorsTable=_Bgp4V2PeerErrorsTable_Object((1,3,6,1,4,1,1991,3,5,1,1,3))
if mibBuilder.loadTexts:bgp4V2PeerErrorsTable.setStatus(_A)
_Bgp4V2PeerErrorsEntry_Object=MibTableRow
bgp4V2PeerErrorsEntry=_Bgp4V2PeerErrorsEntry_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1))
if mibBuilder.loadTexts:bgp4V2PeerErrorsEntry.setStatus(_A)
class _Bgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorCodeReceived_Type.__name__=_E
_Bgp4V2PeerLastErrorCodeReceived_Object=MibTableColumn
bgp4V2PeerLastErrorCodeReceived=_Bgp4V2PeerLastErrorCodeReceived_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,1),_Bgp4V2PeerLastErrorCodeReceived_Type())
bgp4V2PeerLastErrorCodeReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorCodeReceived.setStatus(_A)
class _Bgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorSubCodeReceived_Type.__name__=_E
_Bgp4V2PeerLastErrorSubCodeReceived_Object=MibTableColumn
bgp4V2PeerLastErrorSubCodeReceived=_Bgp4V2PeerLastErrorSubCodeReceived_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,2),_Bgp4V2PeerLastErrorSubCodeReceived_Type())
bgp4V2PeerLastErrorSubCodeReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSubCodeReceived.setStatus(_A)
_Bgp4V2PeerLastErrorReceivedTime_Type=TimeStamp
_Bgp4V2PeerLastErrorReceivedTime_Object=MibTableColumn
bgp4V2PeerLastErrorReceivedTime=_Bgp4V2PeerLastErrorReceivedTime_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,3),_Bgp4V2PeerLastErrorReceivedTime_Type())
bgp4V2PeerLastErrorReceivedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorReceivedTime.setStatus(_A)
_Bgp4V2PeerLastErrorReceivedText_Type=SnmpAdminString
_Bgp4V2PeerLastErrorReceivedText_Object=MibTableColumn
bgp4V2PeerLastErrorReceivedText=_Bgp4V2PeerLastErrorReceivedText_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,4),_Bgp4V2PeerLastErrorReceivedText_Type())
bgp4V2PeerLastErrorReceivedText.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorReceivedText.setStatus(_A)
class _Bgp4V2PeerLastErrorReceivedData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_Bgp4V2PeerLastErrorReceivedData_Type.__name__=_F
_Bgp4V2PeerLastErrorReceivedData_Object=MibTableColumn
bgp4V2PeerLastErrorReceivedData=_Bgp4V2PeerLastErrorReceivedData_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,5),_Bgp4V2PeerLastErrorReceivedData_Type())
bgp4V2PeerLastErrorReceivedData.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorReceivedData.setStatus(_A)
class _Bgp4V2PeerLastErrorCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorCodeSent_Type.__name__=_E
_Bgp4V2PeerLastErrorCodeSent_Object=MibTableColumn
bgp4V2PeerLastErrorCodeSent=_Bgp4V2PeerLastErrorCodeSent_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,6),_Bgp4V2PeerLastErrorCodeSent_Type())
bgp4V2PeerLastErrorCodeSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorCodeSent.setStatus(_A)
class _Bgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Bgp4V2PeerLastErrorSubCodeSent_Type.__name__=_E
_Bgp4V2PeerLastErrorSubCodeSent_Object=MibTableColumn
bgp4V2PeerLastErrorSubCodeSent=_Bgp4V2PeerLastErrorSubCodeSent_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,7),_Bgp4V2PeerLastErrorSubCodeSent_Type())
bgp4V2PeerLastErrorSubCodeSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSubCodeSent.setStatus(_A)
_Bgp4V2PeerLastErrorSentTime_Type=TimeStamp
_Bgp4V2PeerLastErrorSentTime_Object=MibTableColumn
bgp4V2PeerLastErrorSentTime=_Bgp4V2PeerLastErrorSentTime_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,8),_Bgp4V2PeerLastErrorSentTime_Type())
bgp4V2PeerLastErrorSentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSentTime.setStatus(_A)
_Bgp4V2PeerLastErrorSentText_Type=SnmpAdminString
_Bgp4V2PeerLastErrorSentText_Object=MibTableColumn
bgp4V2PeerLastErrorSentText=_Bgp4V2PeerLastErrorSentText_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,9),_Bgp4V2PeerLastErrorSentText_Type())
bgp4V2PeerLastErrorSentText.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSentText.setStatus(_A)
class _Bgp4V2PeerLastErrorSentData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4075))
_Bgp4V2PeerLastErrorSentData_Type.__name__=_F
_Bgp4V2PeerLastErrorSentData_Object=MibTableColumn
bgp4V2PeerLastErrorSentData=_Bgp4V2PeerLastErrorSentData_Object((1,3,6,1,4,1,1991,3,5,1,1,3,1,10),_Bgp4V2PeerLastErrorSentData_Type())
bgp4V2PeerLastErrorSentData.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerLastErrorSentData.setStatus(_A)
_Bgp4V2PeerEventTimesTable_Object=MibTable
bgp4V2PeerEventTimesTable=_Bgp4V2PeerEventTimesTable_Object((1,3,6,1,4,1,1991,3,5,1,1,4))
if mibBuilder.loadTexts:bgp4V2PeerEventTimesTable.setStatus(_A)
_Bgp4V2PeerEventTimesEntry_Object=MibTableRow
bgp4V2PeerEventTimesEntry=_Bgp4V2PeerEventTimesEntry_Object((1,3,6,1,4,1,1991,3,5,1,1,4,1))
if mibBuilder.loadTexts:bgp4V2PeerEventTimesEntry.setStatus(_A)
_Bgp4V2PeerFsmEstablishedTime_Type=Gauge32
_Bgp4V2PeerFsmEstablishedTime_Object=MibTableColumn
bgp4V2PeerFsmEstablishedTime=_Bgp4V2PeerFsmEstablishedTime_Object((1,3,6,1,4,1,1991,3,5,1,1,4,1,1),_Bgp4V2PeerFsmEstablishedTime_Type())
bgp4V2PeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerFsmEstablishedTime.setStatus(_A)
if mibBuilder.loadTexts:bgp4V2PeerFsmEstablishedTime.setUnits(_O)
_Bgp4V2PeerInUpdatesElapsedTime_Type=Gauge32
_Bgp4V2PeerInUpdatesElapsedTime_Object=MibTableColumn
bgp4V2PeerInUpdatesElapsedTime=_Bgp4V2PeerInUpdatesElapsedTime_Object((1,3,6,1,4,1,1991,3,5,1,1,4,1,2),_Bgp4V2PeerInUpdatesElapsedTime_Type())
bgp4V2PeerInUpdatesElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2PeerInUpdatesElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:bgp4V2PeerInUpdatesElapsedTime.setUnits(_O)
_Bgp4V2NlriTable_Object=MibTable
bgp4V2NlriTable=_Bgp4V2NlriTable_Object((1,3,6,1,4,1,1991,3,5,1,1,9))
if mibBuilder.loadTexts:bgp4V2NlriTable.setStatus(_A)
_Bgp4V2NlriEntry_Object=MibTableRow
bgp4V2NlriEntry=_Bgp4V2NlriEntry_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1))
bgp4V2NlriEntry.setIndexNames((0,_C,_H),(0,_C,_P),(0,_C,_Q),(0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_I),(0,_C,_J),(0,_C,_U))
if mibBuilder.loadTexts:bgp4V2NlriEntry.setStatus(_A)
_Bgp4V2NlriIndex_Type=Unsigned32
_Bgp4V2NlriIndex_Object=MibTableColumn
bgp4V2NlriIndex=_Bgp4V2NlriIndex_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,1),_Bgp4V2NlriIndex_Type())
bgp4V2NlriIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2NlriIndex.setStatus(_A)
_Bgp4V2NlriAfi_Type=Bgp4V2AddressFamilyIdentifierTC
_Bgp4V2NlriAfi_Object=MibTableColumn
bgp4V2NlriAfi=_Bgp4V2NlriAfi_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,2),_Bgp4V2NlriAfi_Type())
bgp4V2NlriAfi.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2NlriAfi.setStatus(_A)
_Bgp4V2NlriSafi_Type=Bgp4V2SubsequentAddressFamilyIdentifierTC
_Bgp4V2NlriSafi_Object=MibTableColumn
bgp4V2NlriSafi=_Bgp4V2NlriSafi_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,3),_Bgp4V2NlriSafi_Type())
bgp4V2NlriSafi.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2NlriSafi.setStatus(_A)
_Bgp4V2NlriPrefixType_Type=InetAddressType
_Bgp4V2NlriPrefixType_Object=MibTableColumn
bgp4V2NlriPrefixType=_Bgp4V2NlriPrefixType_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,4),_Bgp4V2NlriPrefixType_Type())
bgp4V2NlriPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2NlriPrefixType.setStatus(_A)
_Bgp4V2NlriPrefix_Type=InetAddress
_Bgp4V2NlriPrefix_Object=MibTableColumn
bgp4V2NlriPrefix=_Bgp4V2NlriPrefix_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,5),_Bgp4V2NlriPrefix_Type())
bgp4V2NlriPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2NlriPrefix.setStatus(_A)
_Bgp4V2NlriPrefixLen_Type=InetAddressPrefixLength
_Bgp4V2NlriPrefixLen_Object=MibTableColumn
bgp4V2NlriPrefixLen=_Bgp4V2NlriPrefixLen_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,6),_Bgp4V2NlriPrefixLen_Type())
bgp4V2NlriPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:bgp4V2NlriPrefixLen.setStatus(_A)
_Bgp4V2NlriBest_Type=TruthValue
_Bgp4V2NlriBest_Object=MibTableColumn
bgp4V2NlriBest=_Bgp4V2NlriBest_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,7),_Bgp4V2NlriBest_Type())
bgp4V2NlriBest.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriBest.setStatus(_A)
_Bgp4V2NlriCalcLocalPref_Type=Unsigned32
_Bgp4V2NlriCalcLocalPref_Object=MibTableColumn
bgp4V2NlriCalcLocalPref=_Bgp4V2NlriCalcLocalPref_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,8),_Bgp4V2NlriCalcLocalPref_Type())
bgp4V2NlriCalcLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriCalcLocalPref.setStatus(_A)
class _Bgp4V2NlriOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_Bgp4V2NlriOrigin_Type.__name__=_G
_Bgp4V2NlriOrigin_Object=MibTableColumn
bgp4V2NlriOrigin=_Bgp4V2NlriOrigin_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,9),_Bgp4V2NlriOrigin_Type())
bgp4V2NlriOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriOrigin.setStatus(_A)
_Bgp4V2NlriNextHopAddrType_Type=InetAddressType
_Bgp4V2NlriNextHopAddrType_Object=MibTableColumn
bgp4V2NlriNextHopAddrType=_Bgp4V2NlriNextHopAddrType_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,10),_Bgp4V2NlriNextHopAddrType_Type())
bgp4V2NlriNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriNextHopAddrType.setStatus(_A)
class _Bgp4V2NlriNextHopAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_Bgp4V2NlriNextHopAddr_Type.__name__=_N
_Bgp4V2NlriNextHopAddr_Object=MibTableColumn
bgp4V2NlriNextHopAddr=_Bgp4V2NlriNextHopAddr_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,11),_Bgp4V2NlriNextHopAddr_Type())
bgp4V2NlriNextHopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriNextHopAddr.setStatus(_A)
_Bgp4V2NlriLinkLocalNextHopAddrType_Type=InetAddressType
_Bgp4V2NlriLinkLocalNextHopAddrType_Object=MibTableColumn
bgp4V2NlriLinkLocalNextHopAddrType=_Bgp4V2NlriLinkLocalNextHopAddrType_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,12),_Bgp4V2NlriLinkLocalNextHopAddrType_Type())
bgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriLinkLocalNextHopAddrType.setStatus(_A)
_Bgp4V2NlriLinkLocalNextHopAddr_Type=InetAddress
_Bgp4V2NlriLinkLocalNextHopAddr_Object=MibTableColumn
bgp4V2NlriLinkLocalNextHopAddr=_Bgp4V2NlriLinkLocalNextHopAddr_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,13),_Bgp4V2NlriLinkLocalNextHopAddr_Type())
bgp4V2NlriLinkLocalNextHopAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriLinkLocalNextHopAddr.setStatus(_A)
_Bgp4V2NlriLocalPrefPresent_Type=TruthValue
_Bgp4V2NlriLocalPrefPresent_Object=MibTableColumn
bgp4V2NlriLocalPrefPresent=_Bgp4V2NlriLocalPrefPresent_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,14),_Bgp4V2NlriLocalPrefPresent_Type())
bgp4V2NlriLocalPrefPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriLocalPrefPresent.setStatus(_A)
_Bgp4V2NlriLocalPref_Type=Unsigned32
_Bgp4V2NlriLocalPref_Object=MibTableColumn
bgp4V2NlriLocalPref=_Bgp4V2NlriLocalPref_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,15),_Bgp4V2NlriLocalPref_Type())
bgp4V2NlriLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriLocalPref.setStatus(_A)
_Bgp4V2NlriMedPresent_Type=TruthValue
_Bgp4V2NlriMedPresent_Object=MibTableColumn
bgp4V2NlriMedPresent=_Bgp4V2NlriMedPresent_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,16),_Bgp4V2NlriMedPresent_Type())
bgp4V2NlriMedPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriMedPresent.setStatus(_A)
_Bgp4V2NlriMed_Type=Unsigned32
_Bgp4V2NlriMed_Object=MibTableColumn
bgp4V2NlriMed=_Bgp4V2NlriMed_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,17),_Bgp4V2NlriMed_Type())
bgp4V2NlriMed.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriMed.setStatus(_A)
_Bgp4V2NlriAtomicAggregate_Type=TruthValue
_Bgp4V2NlriAtomicAggregate_Object=MibTableColumn
bgp4V2NlriAtomicAggregate=_Bgp4V2NlriAtomicAggregate_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,18),_Bgp4V2NlriAtomicAggregate_Type())
bgp4V2NlriAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAtomicAggregate.setStatus(_A)
_Bgp4V2NlriAggregatorPresent_Type=TruthValue
_Bgp4V2NlriAggregatorPresent_Object=MibTableColumn
bgp4V2NlriAggregatorPresent=_Bgp4V2NlriAggregatorPresent_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,19),_Bgp4V2NlriAggregatorPresent_Type())
bgp4V2NlriAggregatorPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAggregatorPresent.setStatus(_A)
_Bgp4V2NlriAggregatorAS_Type=InetAutonomousSystemNumber
_Bgp4V2NlriAggregatorAS_Object=MibTableColumn
bgp4V2NlriAggregatorAS=_Bgp4V2NlriAggregatorAS_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,20),_Bgp4V2NlriAggregatorAS_Type())
bgp4V2NlriAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAggregatorAS.setStatus(_A)
_Bgp4V2NlriAggregatorAddr_Type=Bgp4V2IdentifierTC
_Bgp4V2NlriAggregatorAddr_Object=MibTableColumn
bgp4V2NlriAggregatorAddr=_Bgp4V2NlriAggregatorAddr_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,21),_Bgp4V2NlriAggregatorAddr_Type())
bgp4V2NlriAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAggregatorAddr.setStatus(_A)
_Bgp4V2NlriAsPathCalcLength_Type=Unsigned32
_Bgp4V2NlriAsPathCalcLength_Object=MibTableColumn
bgp4V2NlriAsPathCalcLength=_Bgp4V2NlriAsPathCalcLength_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,22),_Bgp4V2NlriAsPathCalcLength_Type())
bgp4V2NlriAsPathCalcLength.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAsPathCalcLength.setStatus(_A)
_Bgp4V2NlriAsPathString_Type=SnmpAdminString
_Bgp4V2NlriAsPathString_Object=MibTableColumn
bgp4V2NlriAsPathString=_Bgp4V2NlriAsPathString_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,23),_Bgp4V2NlriAsPathString_Type())
bgp4V2NlriAsPathString.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAsPathString.setStatus(_A)
class _Bgp4V2NlriAsPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,4072))
_Bgp4V2NlriAsPath_Type.__name__=_F
_Bgp4V2NlriAsPath_Object=MibTableColumn
bgp4V2NlriAsPath=_Bgp4V2NlriAsPath_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,24),_Bgp4V2NlriAsPath_Type())
bgp4V2NlriAsPath.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriAsPath.setStatus(_A)
class _Bgp4V2NlriPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4072))
_Bgp4V2NlriPathAttrUnknown_Type.__name__=_F
_Bgp4V2NlriPathAttrUnknown_Object=MibTableColumn
bgp4V2NlriPathAttrUnknown=_Bgp4V2NlriPathAttrUnknown_Object((1,3,6,1,4,1,1991,3,5,1,1,9,1,25),_Bgp4V2NlriPathAttrUnknown_Type())
bgp4V2NlriPathAttrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4V2NlriPathAttrUnknown.setStatus(_A)
bgp4V2PeerEntry.registerAugmentions((_C,_V))
bgp4V2PeerErrorsEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2PeerEntry.registerAugmentions((_C,_W))
bgp4V2PeerEventTimesEntry.setIndexNames(*bgp4V2PeerEntry.getIndexNames())
bgp4V2EstablishedNotification=NotificationType((1,3,6,1,4,1,1991,3,5,1,0,1))
bgp4V2EstablishedNotification.setObjects(*((_C,_K),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:bgp4V2EstablishedNotification.setStatus(_A)
bgp4V2BackwardTransitionNotification=NotificationType((1,3,6,1,4,1,1991,3,5,1,0,2))
bgp4V2BackwardTransitionNotification.setObjects(*((_C,_K),(_C,_L),(_C,_M),(_C,_X),(_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:bgp4V2BackwardTransitionNotification.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bgp4V2':bgp4V2,'bgp4V2Notifications':bgp4V2Notifications,'bgp4V2EstablishedNotification':bgp4V2EstablishedNotification,'bgp4V2BackwardTransitionNotification':bgp4V2BackwardTransitionNotification,'bgp4V2Objects':bgp4V2Objects,'bgp4V2PeerTable':bgp4V2PeerTable,'bgp4V2PeerEntry':bgp4V2PeerEntry,_H:bgp4V2PeerInstance,'bgp4V2PeerLocalAddrType':bgp4V2PeerLocalAddrType,'bgp4V2PeerLocalAddr':bgp4V2PeerLocalAddr,_I:bgp4V2PeerRemoteAddrType,_J:bgp4V2PeerRemoteAddr,_L:bgp4V2PeerLocalPort,'bgp4V2PeerLocalAs':bgp4V2PeerLocalAs,'bgp4V2PeerLocalIdentifier':bgp4V2PeerLocalIdentifier,_M:bgp4V2PeerRemotePort,'bgp4V2PeerRemoteAs':bgp4V2PeerRemoteAs,'bgp4V2PeerRemoteIdentifier':bgp4V2PeerRemoteIdentifier,'bgp4V2PeerAdminStatus':bgp4V2PeerAdminStatus,_K:bgp4V2PeerState,'bgp4V2PeerDescription':bgp4V2PeerDescription,'bgp4V2PeerErrorsTable':bgp4V2PeerErrorsTable,_V:bgp4V2PeerErrorsEntry,_X:bgp4V2PeerLastErrorCodeReceived,_Y:bgp4V2PeerLastErrorSubCodeReceived,'bgp4V2PeerLastErrorReceivedTime':bgp4V2PeerLastErrorReceivedTime,_Z:bgp4V2PeerLastErrorReceivedText,'bgp4V2PeerLastErrorReceivedData':bgp4V2PeerLastErrorReceivedData,'bgp4V2PeerLastErrorCodeSent':bgp4V2PeerLastErrorCodeSent,'bgp4V2PeerLastErrorSubCodeSent':bgp4V2PeerLastErrorSubCodeSent,'bgp4V2PeerLastErrorSentTime':bgp4V2PeerLastErrorSentTime,'bgp4V2PeerLastErrorSentText':bgp4V2PeerLastErrorSentText,'bgp4V2PeerLastErrorSentData':bgp4V2PeerLastErrorSentData,'bgp4V2PeerEventTimesTable':bgp4V2PeerEventTimesTable,_W:bgp4V2PeerEventTimesEntry,'bgp4V2PeerFsmEstablishedTime':bgp4V2PeerFsmEstablishedTime,'bgp4V2PeerInUpdatesElapsedTime':bgp4V2PeerInUpdatesElapsedTime,'bgp4V2NlriTable':bgp4V2NlriTable,'bgp4V2NlriEntry':bgp4V2NlriEntry,_U:bgp4V2NlriIndex,_P:bgp4V2NlriAfi,_Q:bgp4V2NlriSafi,_R:bgp4V2NlriPrefixType,_S:bgp4V2NlriPrefix,_T:bgp4V2NlriPrefixLen,'bgp4V2NlriBest':bgp4V2NlriBest,'bgp4V2NlriCalcLocalPref':bgp4V2NlriCalcLocalPref,'bgp4V2NlriOrigin':bgp4V2NlriOrigin,'bgp4V2NlriNextHopAddrType':bgp4V2NlriNextHopAddrType,'bgp4V2NlriNextHopAddr':bgp4V2NlriNextHopAddr,'bgp4V2NlriLinkLocalNextHopAddrType':bgp4V2NlriLinkLocalNextHopAddrType,'bgp4V2NlriLinkLocalNextHopAddr':bgp4V2NlriLinkLocalNextHopAddr,'bgp4V2NlriLocalPrefPresent':bgp4V2NlriLocalPrefPresent,'bgp4V2NlriLocalPref':bgp4V2NlriLocalPref,'bgp4V2NlriMedPresent':bgp4V2NlriMedPresent,'bgp4V2NlriMed':bgp4V2NlriMed,'bgp4V2NlriAtomicAggregate':bgp4V2NlriAtomicAggregate,'bgp4V2NlriAggregatorPresent':bgp4V2NlriAggregatorPresent,'bgp4V2NlriAggregatorAS':bgp4V2NlriAggregatorAS,'bgp4V2NlriAggregatorAddr':bgp4V2NlriAggregatorAddr,'bgp4V2NlriAsPathCalcLength':bgp4V2NlriAsPathCalcLength,'bgp4V2NlriAsPathString':bgp4V2NlriAsPathString,'bgp4V2NlriAsPath':bgp4V2NlriAsPath,'bgp4V2NlriPathAttrUnknown':bgp4V2NlriPathAttrUnknown})