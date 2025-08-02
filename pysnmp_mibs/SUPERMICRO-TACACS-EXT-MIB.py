_M='fsTacClntExtServerGroupServerAddress'
_L='fsTacClntExtServerGroupServerAddressType'
_K='fsTacClntExtServerGroupMibName'
_J='fsTacClntExtServerAddress'
_I='fsTacClntExtServerAddressType'
_H='DisplayString'
_G='read-write'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='SUPERMICRO-TACACS-EXT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
futureTacacsClientExtMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,29))
if mibBuilder.loadTexts:futureTacacsClientExtMIB.setRevisions(('2012-09-05 00:00',))
_FutureTacacsClientExtScalarGroup_ObjectIdentity=ObjectIdentity
futureTacacsClientExtScalarGroup=_FutureTacacsClientExtScalarGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,29,1))
_FsTacClntExtActiveServerAddressType_Type=InetAddressType
_FsTacClntExtActiveServerAddressType_Object=MibScalar
fsTacClntExtActiveServerAddressType=_FsTacClntExtActiveServerAddressType_Object((1,3,6,1,4,1,10876,101,2,29,1,1),_FsTacClntExtActiveServerAddressType_Type())
fsTacClntExtActiveServerAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTacClntExtActiveServerAddressType.setStatus(_A)
_FsTacClntExtActiveServer_Type=InetAddress
_FsTacClntExtActiveServer_Object=MibScalar
fsTacClntExtActiveServer=_FsTacClntExtActiveServer_Object((1,3,6,1,4,1,10876,101,2,29,1,2),_FsTacClntExtActiveServer_Type())
fsTacClntExtActiveServer.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTacClntExtActiveServer.setStatus(_A)
_FsTacClntExtTraceLevel_Type=Unsigned32
_FsTacClntExtTraceLevel_Object=MibScalar
fsTacClntExtTraceLevel=_FsTacClntExtTraceLevel_Object((1,3,6,1,4,1,10876,101,2,29,1,3),_FsTacClntExtTraceLevel_Type())
fsTacClntExtTraceLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTacClntExtTraceLevel.setStatus(_A)
class _FsTacClntExtRetransmit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsTacClntExtRetransmit_Type.__name__=_E
_FsTacClntExtRetransmit_Object=MibScalar
fsTacClntExtRetransmit=_FsTacClntExtRetransmit_Object((1,3,6,1,4,1,10876,101,2,29,1,4),_FsTacClntExtRetransmit_Type())
fsTacClntExtRetransmit.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTacClntExtRetransmit.setStatus(_A)
_FsTacClntExtStatisticsGroup_ObjectIdentity=ObjectIdentity
fsTacClntExtStatisticsGroup=_FsTacClntExtStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,29,1,5))
_FsTacClntExtAuthenStartRequests_Type=Counter32
_FsTacClntExtAuthenStartRequests_Object=MibScalar
fsTacClntExtAuthenStartRequests=_FsTacClntExtAuthenStartRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,1),_FsTacClntExtAuthenStartRequests_Type())
fsTacClntExtAuthenStartRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenStartRequests.setStatus(_A)
_FsTacClntExtAuthenContinueRequests_Type=Counter32
_FsTacClntExtAuthenContinueRequests_Object=MibScalar
fsTacClntExtAuthenContinueRequests=_FsTacClntExtAuthenContinueRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,2),_FsTacClntExtAuthenContinueRequests_Type())
fsTacClntExtAuthenContinueRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenContinueRequests.setStatus(_A)
_FsTacClntExtAuthenEnableRequests_Type=Counter32
_FsTacClntExtAuthenEnableRequests_Object=MibScalar
fsTacClntExtAuthenEnableRequests=_FsTacClntExtAuthenEnableRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,3),_FsTacClntExtAuthenEnableRequests_Type())
fsTacClntExtAuthenEnableRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenEnableRequests.setStatus(_A)
_FsTacClntExtAuthenAbortRequests_Type=Counter32
_FsTacClntExtAuthenAbortRequests_Object=MibScalar
fsTacClntExtAuthenAbortRequests=_FsTacClntExtAuthenAbortRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,4),_FsTacClntExtAuthenAbortRequests_Type())
fsTacClntExtAuthenAbortRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenAbortRequests.setStatus(_A)
_FsTacClntExtAuthenPassReceived_Type=Counter32
_FsTacClntExtAuthenPassReceived_Object=MibScalar
fsTacClntExtAuthenPassReceived=_FsTacClntExtAuthenPassReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,5),_FsTacClntExtAuthenPassReceived_Type())
fsTacClntExtAuthenPassReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenPassReceived.setStatus(_A)
_FsTacClntExtAuthenFailReceived_Type=Counter32
_FsTacClntExtAuthenFailReceived_Object=MibScalar
fsTacClntExtAuthenFailReceived=_FsTacClntExtAuthenFailReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,6),_FsTacClntExtAuthenFailReceived_Type())
fsTacClntExtAuthenFailReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenFailReceived.setStatus(_A)
_FsTacClntExtAuthenGetUserReceived_Type=Counter32
_FsTacClntExtAuthenGetUserReceived_Object=MibScalar
fsTacClntExtAuthenGetUserReceived=_FsTacClntExtAuthenGetUserReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,7),_FsTacClntExtAuthenGetUserReceived_Type())
fsTacClntExtAuthenGetUserReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenGetUserReceived.setStatus(_A)
_FsTacClntExtAuthenGetPassReceived_Type=Counter32
_FsTacClntExtAuthenGetPassReceived_Object=MibScalar
fsTacClntExtAuthenGetPassReceived=_FsTacClntExtAuthenGetPassReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,8),_FsTacClntExtAuthenGetPassReceived_Type())
fsTacClntExtAuthenGetPassReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenGetPassReceived.setStatus(_A)
_FsTacClntExtAuthenGetDataReceived_Type=Counter32
_FsTacClntExtAuthenGetDataReceived_Object=MibScalar
fsTacClntExtAuthenGetDataReceived=_FsTacClntExtAuthenGetDataReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,9),_FsTacClntExtAuthenGetDataReceived_Type())
fsTacClntExtAuthenGetDataReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenGetDataReceived.setStatus(_A)
_FsTacClntExtAuthenErrorReceived_Type=Counter32
_FsTacClntExtAuthenErrorReceived_Object=MibScalar
fsTacClntExtAuthenErrorReceived=_FsTacClntExtAuthenErrorReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,10),_FsTacClntExtAuthenErrorReceived_Type())
fsTacClntExtAuthenErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenErrorReceived.setStatus(_A)
_FsTacClntExtAuthenFollowReceived_Type=Counter32
_FsTacClntExtAuthenFollowReceived_Object=MibScalar
fsTacClntExtAuthenFollowReceived=_FsTacClntExtAuthenFollowReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,11),_FsTacClntExtAuthenFollowReceived_Type())
fsTacClntExtAuthenFollowReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenFollowReceived.setStatus(_A)
_FsTacClntExtAuthenRestartReceived_Type=Counter32
_FsTacClntExtAuthenRestartReceived_Object=MibScalar
fsTacClntExtAuthenRestartReceived=_FsTacClntExtAuthenRestartReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,12),_FsTacClntExtAuthenRestartReceived_Type())
fsTacClntExtAuthenRestartReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenRestartReceived.setStatus(_A)
_FsTacClntExtAuthenSessionTimouts_Type=Counter32
_FsTacClntExtAuthenSessionTimouts_Object=MibScalar
fsTacClntExtAuthenSessionTimouts=_FsTacClntExtAuthenSessionTimouts_Object((1,3,6,1,4,1,10876,101,2,29,1,5,13),_FsTacClntExtAuthenSessionTimouts_Type())
fsTacClntExtAuthenSessionTimouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthenSessionTimouts.setStatus(_A)
_FsTacClntExtAuthorRequests_Type=Counter32
_FsTacClntExtAuthorRequests_Object=MibScalar
fsTacClntExtAuthorRequests=_FsTacClntExtAuthorRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,14),_FsTacClntExtAuthorRequests_Type())
fsTacClntExtAuthorRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorRequests.setStatus(_A)
_FsTacClntExtAuthorPassAddReceived_Type=Counter32
_FsTacClntExtAuthorPassAddReceived_Object=MibScalar
fsTacClntExtAuthorPassAddReceived=_FsTacClntExtAuthorPassAddReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,15),_FsTacClntExtAuthorPassAddReceived_Type())
fsTacClntExtAuthorPassAddReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorPassAddReceived.setStatus(_A)
_FsTacClntExtAuthorPassReplReceived_Type=Counter32
_FsTacClntExtAuthorPassReplReceived_Object=MibScalar
fsTacClntExtAuthorPassReplReceived=_FsTacClntExtAuthorPassReplReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,16),_FsTacClntExtAuthorPassReplReceived_Type())
fsTacClntExtAuthorPassReplReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorPassReplReceived.setStatus(_A)
_FsTacClntExtAuthorFailReceived_Type=Counter32
_FsTacClntExtAuthorFailReceived_Object=MibScalar
fsTacClntExtAuthorFailReceived=_FsTacClntExtAuthorFailReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,17),_FsTacClntExtAuthorFailReceived_Type())
fsTacClntExtAuthorFailReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorFailReceived.setStatus(_A)
_FsTacClntExtAuthorErrorReceived_Type=Counter32
_FsTacClntExtAuthorErrorReceived_Object=MibScalar
fsTacClntExtAuthorErrorReceived=_FsTacClntExtAuthorErrorReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,18),_FsTacClntExtAuthorErrorReceived_Type())
fsTacClntExtAuthorErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorErrorReceived.setStatus(_A)
_FsTacClntExtAuthorFollowReceived_Type=Counter32
_FsTacClntExtAuthorFollowReceived_Object=MibScalar
fsTacClntExtAuthorFollowReceived=_FsTacClntExtAuthorFollowReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,19),_FsTacClntExtAuthorFollowReceived_Type())
fsTacClntExtAuthorFollowReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorFollowReceived.setStatus(_A)
_FsTacClntExtAuthorSessionTimeouts_Type=Counter32
_FsTacClntExtAuthorSessionTimeouts_Object=MibScalar
fsTacClntExtAuthorSessionTimeouts=_FsTacClntExtAuthorSessionTimeouts_Object((1,3,6,1,4,1,10876,101,2,29,1,5,20),_FsTacClntExtAuthorSessionTimeouts_Type())
fsTacClntExtAuthorSessionTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAuthorSessionTimeouts.setStatus(_A)
_FsTacClntExtAcctStartRequests_Type=Counter32
_FsTacClntExtAcctStartRequests_Object=MibScalar
fsTacClntExtAcctStartRequests=_FsTacClntExtAcctStartRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,21),_FsTacClntExtAcctStartRequests_Type())
fsTacClntExtAcctStartRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctStartRequests.setStatus(_A)
_FsTacClntExtAcctWdRequests_Type=Counter32
_FsTacClntExtAcctWdRequests_Object=MibScalar
fsTacClntExtAcctWdRequests=_FsTacClntExtAcctWdRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,22),_FsTacClntExtAcctWdRequests_Type())
fsTacClntExtAcctWdRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctWdRequests.setStatus(_A)
_FsTacClntExtAcctStopRequests_Type=Counter32
_FsTacClntExtAcctStopRequests_Object=MibScalar
fsTacClntExtAcctStopRequests=_FsTacClntExtAcctStopRequests_Object((1,3,6,1,4,1,10876,101,2,29,1,5,23),_FsTacClntExtAcctStopRequests_Type())
fsTacClntExtAcctStopRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctStopRequests.setStatus(_A)
_FsTacClntExtAcctSuccessReceived_Type=Counter32
_FsTacClntExtAcctSuccessReceived_Object=MibScalar
fsTacClntExtAcctSuccessReceived=_FsTacClntExtAcctSuccessReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,24),_FsTacClntExtAcctSuccessReceived_Type())
fsTacClntExtAcctSuccessReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctSuccessReceived.setStatus(_A)
_FsTacClntExtAcctErrorReceived_Type=Counter32
_FsTacClntExtAcctErrorReceived_Object=MibScalar
fsTacClntExtAcctErrorReceived=_FsTacClntExtAcctErrorReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,25),_FsTacClntExtAcctErrorReceived_Type())
fsTacClntExtAcctErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctErrorReceived.setStatus(_A)
_FsTacClntExtAcctFollowReceived_Type=Counter32
_FsTacClntExtAcctFollowReceived_Object=MibScalar
fsTacClntExtAcctFollowReceived=_FsTacClntExtAcctFollowReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,26),_FsTacClntExtAcctFollowReceived_Type())
fsTacClntExtAcctFollowReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctFollowReceived.setStatus(_A)
_FsTacClntExtAcctSessionTimeouts_Type=Counter32
_FsTacClntExtAcctSessionTimeouts_Object=MibScalar
fsTacClntExtAcctSessionTimeouts=_FsTacClntExtAcctSessionTimeouts_Object((1,3,6,1,4,1,10876,101,2,29,1,5,27),_FsTacClntExtAcctSessionTimeouts_Type())
fsTacClntExtAcctSessionTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtAcctSessionTimeouts.setStatus(_A)
_FsTacClntExtMalformedPktsReceived_Type=Counter32
_FsTacClntExtMalformedPktsReceived_Object=MibScalar
fsTacClntExtMalformedPktsReceived=_FsTacClntExtMalformedPktsReceived_Object((1,3,6,1,4,1,10876,101,2,29,1,5,28),_FsTacClntExtMalformedPktsReceived_Type())
fsTacClntExtMalformedPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtMalformedPktsReceived.setStatus(_A)
_FsTacClntExtSocketFailures_Type=Counter32
_FsTacClntExtSocketFailures_Object=MibScalar
fsTacClntExtSocketFailures=_FsTacClntExtSocketFailures_Object((1,3,6,1,4,1,10876,101,2,29,1,5,29),_FsTacClntExtSocketFailures_Type())
fsTacClntExtSocketFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtSocketFailures.setStatus(_A)
_FsTacClntExtConnectionFailures_Type=Counter32
_FsTacClntExtConnectionFailures_Object=MibScalar
fsTacClntExtConnectionFailures=_FsTacClntExtConnectionFailures_Object((1,3,6,1,4,1,10876,101,2,29,1,5,30),_FsTacClntExtConnectionFailures_Type())
fsTacClntExtConnectionFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntExtConnectionFailures.setStatus(_A)
_FutureTacacsClientExtTableGroup_ObjectIdentity=ObjectIdentity
futureTacacsClientExtTableGroup=_FutureTacacsClientExtTableGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,29,2))
_FsTacClntExtServerTable_Object=MibTable
fsTacClntExtServerTable=_FsTacClntExtServerTable_Object((1,3,6,1,4,1,10876,101,2,29,2,1))
if mibBuilder.loadTexts:fsTacClntExtServerTable.setStatus(_A)
_FsTacClntExtServerEntry_Object=MibTableRow
fsTacClntExtServerEntry=_FsTacClntExtServerEntry_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1))
fsTacClntExtServerEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fsTacClntExtServerEntry.setStatus(_A)
_FsTacClntExtServerAddressType_Type=InetAddressType
_FsTacClntExtServerAddressType_Object=MibTableColumn
fsTacClntExtServerAddressType=_FsTacClntExtServerAddressType_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,1),_FsTacClntExtServerAddressType_Type())
fsTacClntExtServerAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTacClntExtServerAddressType.setStatus(_A)
_FsTacClntExtServerAddress_Type=InetAddress
_FsTacClntExtServerAddress_Object=MibTableColumn
fsTacClntExtServerAddress=_FsTacClntExtServerAddress_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,2),_FsTacClntExtServerAddress_Type())
fsTacClntExtServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTacClntExtServerAddress.setStatus(_A)
_FsTacClntExtServerStatus_Type=RowStatus
_FsTacClntExtServerStatus_Object=MibTableColumn
fsTacClntExtServerStatus=_FsTacClntExtServerStatus_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,3),_FsTacClntExtServerStatus_Type())
fsTacClntExtServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntExtServerStatus.setStatus(_A)
class _FsTacClntExtServerSingleConnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsTacClntExtServerSingleConnect_Type.__name__=_E
_FsTacClntExtServerSingleConnect_Object=MibTableColumn
fsTacClntExtServerSingleConnect=_FsTacClntExtServerSingleConnect_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,4),_FsTacClntExtServerSingleConnect_Type())
fsTacClntExtServerSingleConnect.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntExtServerSingleConnect.setStatus(_A)
class _FsTacClntExtServerPort_Type(Integer32):defaultValue=49;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsTacClntExtServerPort_Type.__name__=_E
_FsTacClntExtServerPort_Object=MibTableColumn
fsTacClntExtServerPort=_FsTacClntExtServerPort_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,5),_FsTacClntExtServerPort_Type())
fsTacClntExtServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntExtServerPort.setStatus(_A)
class _FsTacClntExtServerTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsTacClntExtServerTimeout_Type.__name__=_E
_FsTacClntExtServerTimeout_Object=MibTableColumn
fsTacClntExtServerTimeout=_FsTacClntExtServerTimeout_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,6),_FsTacClntExtServerTimeout_Type())
fsTacClntExtServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntExtServerTimeout.setStatus(_A)
_FsTacClntExtServerKey_Type=DisplayString
_FsTacClntExtServerKey_Object=MibTableColumn
fsTacClntExtServerKey=_FsTacClntExtServerKey_Object((1,3,6,1,4,1,10876,101,2,29,2,1,1,7),_FsTacClntExtServerKey_Type())
fsTacClntExtServerKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntExtServerKey.setStatus(_A)
_FsTacClntExtServerGroupMibTable_Object=MibTable
fsTacClntExtServerGroupMibTable=_FsTacClntExtServerGroupMibTable_Object((1,3,6,1,4,1,10876,101,2,29,2,2))
if mibBuilder.loadTexts:fsTacClntExtServerGroupMibTable.setStatus(_A)
_FsTacClntExtServerGroupMibEntry_Object=MibTableRow
fsTacClntExtServerGroupMibEntry=_FsTacClntExtServerGroupMibEntry_Object((1,3,6,1,4,1,10876,101,2,29,2,2,1))
fsTacClntExtServerGroupMibEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsTacClntExtServerGroupMibEntry.setStatus(_A)
_FsTacClntExtServerGroupMibStatus_Type=RowStatus
_FsTacClntExtServerGroupMibStatus_Object=MibTableColumn
fsTacClntExtServerGroupMibStatus=_FsTacClntExtServerGroupMibStatus_Object((1,3,6,1,4,1,10876,101,2,29,2,2,1,1),_FsTacClntExtServerGroupMibStatus_Type())
fsTacClntExtServerGroupMibStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntExtServerGroupMibStatus.setStatus(_A)
class _FsTacClntExtServerGroupMibName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_FsTacClntExtServerGroupMibName_Type.__name__=_H
_FsTacClntExtServerGroupMibName_Object=MibTableColumn
fsTacClntExtServerGroupMibName=_FsTacClntExtServerGroupMibName_Object((1,3,6,1,4,1,10876,101,2,29,2,2,1,2),_FsTacClntExtServerGroupMibName_Type())
fsTacClntExtServerGroupMibName.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTacClntExtServerGroupMibName.setStatus(_A)
_FsTacClntExtServerGroupServerAddressType_Type=InetAddressType
_FsTacClntExtServerGroupServerAddressType_Object=MibTableColumn
fsTacClntExtServerGroupServerAddressType=_FsTacClntExtServerGroupServerAddressType_Object((1,3,6,1,4,1,10876,101,2,29,2,2,1,3),_FsTacClntExtServerGroupServerAddressType_Type())
fsTacClntExtServerGroupServerAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTacClntExtServerGroupServerAddressType.setStatus(_A)
_FsTacClntExtServerGroupServerAddress_Type=InetAddress
_FsTacClntExtServerGroupServerAddress_Object=MibTableColumn
fsTacClntExtServerGroupServerAddress=_FsTacClntExtServerGroupServerAddress_Object((1,3,6,1,4,1,10876,101,2,29,2,2,1,4),_FsTacClntExtServerGroupServerAddress_Type())
fsTacClntExtServerGroupServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsTacClntExtServerGroupServerAddress.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'futureTacacsClientExtMIB':futureTacacsClientExtMIB,'futureTacacsClientExtScalarGroup':futureTacacsClientExtScalarGroup,'fsTacClntExtActiveServerAddressType':fsTacClntExtActiveServerAddressType,'fsTacClntExtActiveServer':fsTacClntExtActiveServer,'fsTacClntExtTraceLevel':fsTacClntExtTraceLevel,'fsTacClntExtRetransmit':fsTacClntExtRetransmit,'fsTacClntExtStatisticsGroup':fsTacClntExtStatisticsGroup,'fsTacClntExtAuthenStartRequests':fsTacClntExtAuthenStartRequests,'fsTacClntExtAuthenContinueRequests':fsTacClntExtAuthenContinueRequests,'fsTacClntExtAuthenEnableRequests':fsTacClntExtAuthenEnableRequests,'fsTacClntExtAuthenAbortRequests':fsTacClntExtAuthenAbortRequests,'fsTacClntExtAuthenPassReceived':fsTacClntExtAuthenPassReceived,'fsTacClntExtAuthenFailReceived':fsTacClntExtAuthenFailReceived,'fsTacClntExtAuthenGetUserReceived':fsTacClntExtAuthenGetUserReceived,'fsTacClntExtAuthenGetPassReceived':fsTacClntExtAuthenGetPassReceived,'fsTacClntExtAuthenGetDataReceived':fsTacClntExtAuthenGetDataReceived,'fsTacClntExtAuthenErrorReceived':fsTacClntExtAuthenErrorReceived,'fsTacClntExtAuthenFollowReceived':fsTacClntExtAuthenFollowReceived,'fsTacClntExtAuthenRestartReceived':fsTacClntExtAuthenRestartReceived,'fsTacClntExtAuthenSessionTimouts':fsTacClntExtAuthenSessionTimouts,'fsTacClntExtAuthorRequests':fsTacClntExtAuthorRequests,'fsTacClntExtAuthorPassAddReceived':fsTacClntExtAuthorPassAddReceived,'fsTacClntExtAuthorPassReplReceived':fsTacClntExtAuthorPassReplReceived,'fsTacClntExtAuthorFailReceived':fsTacClntExtAuthorFailReceived,'fsTacClntExtAuthorErrorReceived':fsTacClntExtAuthorErrorReceived,'fsTacClntExtAuthorFollowReceived':fsTacClntExtAuthorFollowReceived,'fsTacClntExtAuthorSessionTimeouts':fsTacClntExtAuthorSessionTimeouts,'fsTacClntExtAcctStartRequests':fsTacClntExtAcctStartRequests,'fsTacClntExtAcctWdRequests':fsTacClntExtAcctWdRequests,'fsTacClntExtAcctStopRequests':fsTacClntExtAcctStopRequests,'fsTacClntExtAcctSuccessReceived':fsTacClntExtAcctSuccessReceived,'fsTacClntExtAcctErrorReceived':fsTacClntExtAcctErrorReceived,'fsTacClntExtAcctFollowReceived':fsTacClntExtAcctFollowReceived,'fsTacClntExtAcctSessionTimeouts':fsTacClntExtAcctSessionTimeouts,'fsTacClntExtMalformedPktsReceived':fsTacClntExtMalformedPktsReceived,'fsTacClntExtSocketFailures':fsTacClntExtSocketFailures,'fsTacClntExtConnectionFailures':fsTacClntExtConnectionFailures,'futureTacacsClientExtTableGroup':futureTacacsClientExtTableGroup,'fsTacClntExtServerTable':fsTacClntExtServerTable,'fsTacClntExtServerEntry':fsTacClntExtServerEntry,_I:fsTacClntExtServerAddressType,_J:fsTacClntExtServerAddress,'fsTacClntExtServerStatus':fsTacClntExtServerStatus,'fsTacClntExtServerSingleConnect':fsTacClntExtServerSingleConnect,'fsTacClntExtServerPort':fsTacClntExtServerPort,'fsTacClntExtServerTimeout':fsTacClntExtServerTimeout,'fsTacClntExtServerKey':fsTacClntExtServerKey,'fsTacClntExtServerGroupMibTable':fsTacClntExtServerGroupMibTable,'fsTacClntExtServerGroupMibEntry':fsTacClntExtServerGroupMibEntry,'fsTacClntExtServerGroupMibStatus':fsTacClntExtServerGroupMibStatus,_K:fsTacClntExtServerGroupMibName,_L:fsTacClntExtServerGroupServerAddressType,_M:fsTacClntExtServerGroupServerAddress})