_G='fsTacClntServerAddress'
_F='ARICENT-TACACS-MIB'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futureTacacsClientMIB=ModuleIdentity((1,3,6,1,4,1,2076,77))
if mibBuilder.loadTexts:futureTacacsClientMIB.setRevisions(('2012-09-05 00:00',))
_FutureTacacsClientScalarGroup_ObjectIdentity=ObjectIdentity
futureTacacsClientScalarGroup=_FutureTacacsClientScalarGroup_ObjectIdentity((1,3,6,1,4,1,2076,77,1))
_FsTacClntActiveServer_Type=IpAddress
_FsTacClntActiveServer_Object=MibScalar
fsTacClntActiveServer=_FsTacClntActiveServer_Object((1,3,6,1,4,1,2076,77,1,1),_FsTacClntActiveServer_Type())
fsTacClntActiveServer.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTacClntActiveServer.setStatus(_A)
_FsTacClntTraceLevel_Type=Unsigned32
_FsTacClntTraceLevel_Object=MibScalar
fsTacClntTraceLevel=_FsTacClntTraceLevel_Object((1,3,6,1,4,1,2076,77,1,2),_FsTacClntTraceLevel_Type())
fsTacClntTraceLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTacClntTraceLevel.setStatus(_A)
class _FsTacClntRetransmit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsTacClntRetransmit_Type.__name__=_C
_FsTacClntRetransmit_Object=MibScalar
fsTacClntRetransmit=_FsTacClntRetransmit_Object((1,3,6,1,4,1,2076,77,1,3),_FsTacClntRetransmit_Type())
fsTacClntRetransmit.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTacClntRetransmit.setStatus(_A)
_FsTacClntStatisticsGroup_ObjectIdentity=ObjectIdentity
fsTacClntStatisticsGroup=_FsTacClntStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,2076,77,1,4))
_FsTacClntAuthenStartRequests_Type=Counter32
_FsTacClntAuthenStartRequests_Object=MibScalar
fsTacClntAuthenStartRequests=_FsTacClntAuthenStartRequests_Object((1,3,6,1,4,1,2076,77,1,4,1),_FsTacClntAuthenStartRequests_Type())
fsTacClntAuthenStartRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenStartRequests.setStatus(_A)
_FsTacClntAuthenContinueRequests_Type=Counter32
_FsTacClntAuthenContinueRequests_Object=MibScalar
fsTacClntAuthenContinueRequests=_FsTacClntAuthenContinueRequests_Object((1,3,6,1,4,1,2076,77,1,4,2),_FsTacClntAuthenContinueRequests_Type())
fsTacClntAuthenContinueRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenContinueRequests.setStatus(_A)
_FsTacClntAuthenEnableRequests_Type=Counter32
_FsTacClntAuthenEnableRequests_Object=MibScalar
fsTacClntAuthenEnableRequests=_FsTacClntAuthenEnableRequests_Object((1,3,6,1,4,1,2076,77,1,4,3),_FsTacClntAuthenEnableRequests_Type())
fsTacClntAuthenEnableRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenEnableRequests.setStatus(_A)
_FsTacClntAuthenAbortRequests_Type=Counter32
_FsTacClntAuthenAbortRequests_Object=MibScalar
fsTacClntAuthenAbortRequests=_FsTacClntAuthenAbortRequests_Object((1,3,6,1,4,1,2076,77,1,4,4),_FsTacClntAuthenAbortRequests_Type())
fsTacClntAuthenAbortRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenAbortRequests.setStatus(_A)
_FsTacClntAuthenPassReceived_Type=Counter32
_FsTacClntAuthenPassReceived_Object=MibScalar
fsTacClntAuthenPassReceived=_FsTacClntAuthenPassReceived_Object((1,3,6,1,4,1,2076,77,1,4,5),_FsTacClntAuthenPassReceived_Type())
fsTacClntAuthenPassReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenPassReceived.setStatus(_A)
_FsTacClntAuthenFailReceived_Type=Counter32
_FsTacClntAuthenFailReceived_Object=MibScalar
fsTacClntAuthenFailReceived=_FsTacClntAuthenFailReceived_Object((1,3,6,1,4,1,2076,77,1,4,6),_FsTacClntAuthenFailReceived_Type())
fsTacClntAuthenFailReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenFailReceived.setStatus(_A)
_FsTacClntAuthenGetUserReceived_Type=Counter32
_FsTacClntAuthenGetUserReceived_Object=MibScalar
fsTacClntAuthenGetUserReceived=_FsTacClntAuthenGetUserReceived_Object((1,3,6,1,4,1,2076,77,1,4,7),_FsTacClntAuthenGetUserReceived_Type())
fsTacClntAuthenGetUserReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenGetUserReceived.setStatus(_A)
_FsTacClntAuthenGetPassReceived_Type=Counter32
_FsTacClntAuthenGetPassReceived_Object=MibScalar
fsTacClntAuthenGetPassReceived=_FsTacClntAuthenGetPassReceived_Object((1,3,6,1,4,1,2076,77,1,4,8),_FsTacClntAuthenGetPassReceived_Type())
fsTacClntAuthenGetPassReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenGetPassReceived.setStatus(_A)
_FsTacClntAuthenGetDataReceived_Type=Counter32
_FsTacClntAuthenGetDataReceived_Object=MibScalar
fsTacClntAuthenGetDataReceived=_FsTacClntAuthenGetDataReceived_Object((1,3,6,1,4,1,2076,77,1,4,9),_FsTacClntAuthenGetDataReceived_Type())
fsTacClntAuthenGetDataReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenGetDataReceived.setStatus(_A)
_FsTacClntAuthenErrorReceived_Type=Counter32
_FsTacClntAuthenErrorReceived_Object=MibScalar
fsTacClntAuthenErrorReceived=_FsTacClntAuthenErrorReceived_Object((1,3,6,1,4,1,2076,77,1,4,10),_FsTacClntAuthenErrorReceived_Type())
fsTacClntAuthenErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenErrorReceived.setStatus(_A)
_FsTacClntAuthenFollowReceived_Type=Counter32
_FsTacClntAuthenFollowReceived_Object=MibScalar
fsTacClntAuthenFollowReceived=_FsTacClntAuthenFollowReceived_Object((1,3,6,1,4,1,2076,77,1,4,11),_FsTacClntAuthenFollowReceived_Type())
fsTacClntAuthenFollowReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenFollowReceived.setStatus(_A)
_FsTacClntAuthenRestartReceived_Type=Counter32
_FsTacClntAuthenRestartReceived_Object=MibScalar
fsTacClntAuthenRestartReceived=_FsTacClntAuthenRestartReceived_Object((1,3,6,1,4,1,2076,77,1,4,12),_FsTacClntAuthenRestartReceived_Type())
fsTacClntAuthenRestartReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenRestartReceived.setStatus(_A)
_FsTacClntAuthenSessionTimouts_Type=Counter32
_FsTacClntAuthenSessionTimouts_Object=MibScalar
fsTacClntAuthenSessionTimouts=_FsTacClntAuthenSessionTimouts_Object((1,3,6,1,4,1,2076,77,1,4,13),_FsTacClntAuthenSessionTimouts_Type())
fsTacClntAuthenSessionTimouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthenSessionTimouts.setStatus(_A)
_FsTacClntAuthorRequests_Type=Counter32
_FsTacClntAuthorRequests_Object=MibScalar
fsTacClntAuthorRequests=_FsTacClntAuthorRequests_Object((1,3,6,1,4,1,2076,77,1,4,14),_FsTacClntAuthorRequests_Type())
fsTacClntAuthorRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorRequests.setStatus(_A)
_FsTacClntAuthorPassAddReceived_Type=Counter32
_FsTacClntAuthorPassAddReceived_Object=MibScalar
fsTacClntAuthorPassAddReceived=_FsTacClntAuthorPassAddReceived_Object((1,3,6,1,4,1,2076,77,1,4,15),_FsTacClntAuthorPassAddReceived_Type())
fsTacClntAuthorPassAddReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorPassAddReceived.setStatus(_A)
_FsTacClntAuthorPassReplReceived_Type=Counter32
_FsTacClntAuthorPassReplReceived_Object=MibScalar
fsTacClntAuthorPassReplReceived=_FsTacClntAuthorPassReplReceived_Object((1,3,6,1,4,1,2076,77,1,4,16),_FsTacClntAuthorPassReplReceived_Type())
fsTacClntAuthorPassReplReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorPassReplReceived.setStatus(_A)
_FsTacClntAuthorFailReceived_Type=Counter32
_FsTacClntAuthorFailReceived_Object=MibScalar
fsTacClntAuthorFailReceived=_FsTacClntAuthorFailReceived_Object((1,3,6,1,4,1,2076,77,1,4,17),_FsTacClntAuthorFailReceived_Type())
fsTacClntAuthorFailReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorFailReceived.setStatus(_A)
_FsTacClntAuthorErrorReceived_Type=Counter32
_FsTacClntAuthorErrorReceived_Object=MibScalar
fsTacClntAuthorErrorReceived=_FsTacClntAuthorErrorReceived_Object((1,3,6,1,4,1,2076,77,1,4,18),_FsTacClntAuthorErrorReceived_Type())
fsTacClntAuthorErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorErrorReceived.setStatus(_A)
_FsTacClntAuthorFollowReceived_Type=Counter32
_FsTacClntAuthorFollowReceived_Object=MibScalar
fsTacClntAuthorFollowReceived=_FsTacClntAuthorFollowReceived_Object((1,3,6,1,4,1,2076,77,1,4,19),_FsTacClntAuthorFollowReceived_Type())
fsTacClntAuthorFollowReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorFollowReceived.setStatus(_A)
_FsTacClntAuthorSessionTimeouts_Type=Counter32
_FsTacClntAuthorSessionTimeouts_Object=MibScalar
fsTacClntAuthorSessionTimeouts=_FsTacClntAuthorSessionTimeouts_Object((1,3,6,1,4,1,2076,77,1,4,20),_FsTacClntAuthorSessionTimeouts_Type())
fsTacClntAuthorSessionTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAuthorSessionTimeouts.setStatus(_A)
_FsTacClntAcctStartRequests_Type=Counter32
_FsTacClntAcctStartRequests_Object=MibScalar
fsTacClntAcctStartRequests=_FsTacClntAcctStartRequests_Object((1,3,6,1,4,1,2076,77,1,4,21),_FsTacClntAcctStartRequests_Type())
fsTacClntAcctStartRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctStartRequests.setStatus(_A)
_FsTacClntAcctWdRequests_Type=Counter32
_FsTacClntAcctWdRequests_Object=MibScalar
fsTacClntAcctWdRequests=_FsTacClntAcctWdRequests_Object((1,3,6,1,4,1,2076,77,1,4,22),_FsTacClntAcctWdRequests_Type())
fsTacClntAcctWdRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctWdRequests.setStatus(_A)
_FsTacClntAcctStopRequests_Type=Counter32
_FsTacClntAcctStopRequests_Object=MibScalar
fsTacClntAcctStopRequests=_FsTacClntAcctStopRequests_Object((1,3,6,1,4,1,2076,77,1,4,23),_FsTacClntAcctStopRequests_Type())
fsTacClntAcctStopRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctStopRequests.setStatus(_A)
_FsTacClntAcctSuccessReceived_Type=Counter32
_FsTacClntAcctSuccessReceived_Object=MibScalar
fsTacClntAcctSuccessReceived=_FsTacClntAcctSuccessReceived_Object((1,3,6,1,4,1,2076,77,1,4,24),_FsTacClntAcctSuccessReceived_Type())
fsTacClntAcctSuccessReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctSuccessReceived.setStatus(_A)
_FsTacClntAcctErrorReceived_Type=Counter32
_FsTacClntAcctErrorReceived_Object=MibScalar
fsTacClntAcctErrorReceived=_FsTacClntAcctErrorReceived_Object((1,3,6,1,4,1,2076,77,1,4,25),_FsTacClntAcctErrorReceived_Type())
fsTacClntAcctErrorReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctErrorReceived.setStatus(_A)
_FsTacClntAcctFollowReceived_Type=Counter32
_FsTacClntAcctFollowReceived_Object=MibScalar
fsTacClntAcctFollowReceived=_FsTacClntAcctFollowReceived_Object((1,3,6,1,4,1,2076,77,1,4,26),_FsTacClntAcctFollowReceived_Type())
fsTacClntAcctFollowReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctFollowReceived.setStatus(_A)
_FsTacClntAcctSessionTimeouts_Type=Counter32
_FsTacClntAcctSessionTimeouts_Object=MibScalar
fsTacClntAcctSessionTimeouts=_FsTacClntAcctSessionTimeouts_Object((1,3,6,1,4,1,2076,77,1,4,27),_FsTacClntAcctSessionTimeouts_Type())
fsTacClntAcctSessionTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntAcctSessionTimeouts.setStatus(_A)
_FsTacClntMalformedPktsReceived_Type=Counter32
_FsTacClntMalformedPktsReceived_Object=MibScalar
fsTacClntMalformedPktsReceived=_FsTacClntMalformedPktsReceived_Object((1,3,6,1,4,1,2076,77,1,4,28),_FsTacClntMalformedPktsReceived_Type())
fsTacClntMalformedPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntMalformedPktsReceived.setStatus(_A)
_FsTacClntSocketFailures_Type=Counter32
_FsTacClntSocketFailures_Object=MibScalar
fsTacClntSocketFailures=_FsTacClntSocketFailures_Object((1,3,6,1,4,1,2076,77,1,4,29),_FsTacClntSocketFailures_Type())
fsTacClntSocketFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntSocketFailures.setStatus(_A)
_FsTacClntConnectionFailures_Type=Counter32
_FsTacClntConnectionFailures_Object=MibScalar
fsTacClntConnectionFailures=_FsTacClntConnectionFailures_Object((1,3,6,1,4,1,2076,77,1,4,30),_FsTacClntConnectionFailures_Type())
fsTacClntConnectionFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTacClntConnectionFailures.setStatus(_A)
_FutureTacacsClientTableGroup_ObjectIdentity=ObjectIdentity
futureTacacsClientTableGroup=_FutureTacacsClientTableGroup_ObjectIdentity((1,3,6,1,4,1,2076,77,2))
_FsTacClntServerTable_Object=MibTable
fsTacClntServerTable=_FsTacClntServerTable_Object((1,3,6,1,4,1,2076,77,2,1))
if mibBuilder.loadTexts:fsTacClntServerTable.setStatus(_A)
_FsTacClntServerEntry_Object=MibTableRow
fsTacClntServerEntry=_FsTacClntServerEntry_Object((1,3,6,1,4,1,2076,77,2,1,1))
fsTacClntServerEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fsTacClntServerEntry.setStatus(_A)
_FsTacClntServerAddress_Type=IpAddress
_FsTacClntServerAddress_Object=MibTableColumn
fsTacClntServerAddress=_FsTacClntServerAddress_Object((1,3,6,1,4,1,2076,77,2,1,1,1),_FsTacClntServerAddress_Type())
fsTacClntServerAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsTacClntServerAddress.setStatus(_A)
_FsTacClntServerStatus_Type=RowStatus
_FsTacClntServerStatus_Object=MibTableColumn
fsTacClntServerStatus=_FsTacClntServerStatus_Object((1,3,6,1,4,1,2076,77,2,1,1,2),_FsTacClntServerStatus_Type())
fsTacClntServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntServerStatus.setStatus(_A)
class _FsTacClntServerSingleConnect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_FsTacClntServerSingleConnect_Type.__name__=_C
_FsTacClntServerSingleConnect_Object=MibTableColumn
fsTacClntServerSingleConnect=_FsTacClntServerSingleConnect_Object((1,3,6,1,4,1,2076,77,2,1,1,3),_FsTacClntServerSingleConnect_Type())
fsTacClntServerSingleConnect.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntServerSingleConnect.setStatus(_A)
class _FsTacClntServerPort_Type(Integer32):defaultValue=49;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsTacClntServerPort_Type.__name__=_C
_FsTacClntServerPort_Object=MibTableColumn
fsTacClntServerPort=_FsTacClntServerPort_Object((1,3,6,1,4,1,2076,77,2,1,1,4),_FsTacClntServerPort_Type())
fsTacClntServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntServerPort.setStatus(_A)
class _FsTacClntServerTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsTacClntServerTimeout_Type.__name__=_C
_FsTacClntServerTimeout_Object=MibTableColumn
fsTacClntServerTimeout=_FsTacClntServerTimeout_Object((1,3,6,1,4,1,2076,77,2,1,1,5),_FsTacClntServerTimeout_Type())
fsTacClntServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntServerTimeout.setStatus(_A)
_FsTacClntServerKey_Type=DisplayString
_FsTacClntServerKey_Object=MibTableColumn
fsTacClntServerKey=_FsTacClntServerKey_Object((1,3,6,1,4,1,2076,77,2,1,1,6),_FsTacClntServerKey_Type())
fsTacClntServerKey.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacClntServerKey.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'futureTacacsClientMIB':futureTacacsClientMIB,'futureTacacsClientScalarGroup':futureTacacsClientScalarGroup,'fsTacClntActiveServer':fsTacClntActiveServer,'fsTacClntTraceLevel':fsTacClntTraceLevel,'fsTacClntRetransmit':fsTacClntRetransmit,'fsTacClntStatisticsGroup':fsTacClntStatisticsGroup,'fsTacClntAuthenStartRequests':fsTacClntAuthenStartRequests,'fsTacClntAuthenContinueRequests':fsTacClntAuthenContinueRequests,'fsTacClntAuthenEnableRequests':fsTacClntAuthenEnableRequests,'fsTacClntAuthenAbortRequests':fsTacClntAuthenAbortRequests,'fsTacClntAuthenPassReceived':fsTacClntAuthenPassReceived,'fsTacClntAuthenFailReceived':fsTacClntAuthenFailReceived,'fsTacClntAuthenGetUserReceived':fsTacClntAuthenGetUserReceived,'fsTacClntAuthenGetPassReceived':fsTacClntAuthenGetPassReceived,'fsTacClntAuthenGetDataReceived':fsTacClntAuthenGetDataReceived,'fsTacClntAuthenErrorReceived':fsTacClntAuthenErrorReceived,'fsTacClntAuthenFollowReceived':fsTacClntAuthenFollowReceived,'fsTacClntAuthenRestartReceived':fsTacClntAuthenRestartReceived,'fsTacClntAuthenSessionTimouts':fsTacClntAuthenSessionTimouts,'fsTacClntAuthorRequests':fsTacClntAuthorRequests,'fsTacClntAuthorPassAddReceived':fsTacClntAuthorPassAddReceived,'fsTacClntAuthorPassReplReceived':fsTacClntAuthorPassReplReceived,'fsTacClntAuthorFailReceived':fsTacClntAuthorFailReceived,'fsTacClntAuthorErrorReceived':fsTacClntAuthorErrorReceived,'fsTacClntAuthorFollowReceived':fsTacClntAuthorFollowReceived,'fsTacClntAuthorSessionTimeouts':fsTacClntAuthorSessionTimeouts,'fsTacClntAcctStartRequests':fsTacClntAcctStartRequests,'fsTacClntAcctWdRequests':fsTacClntAcctWdRequests,'fsTacClntAcctStopRequests':fsTacClntAcctStopRequests,'fsTacClntAcctSuccessReceived':fsTacClntAcctSuccessReceived,'fsTacClntAcctErrorReceived':fsTacClntAcctErrorReceived,'fsTacClntAcctFollowReceived':fsTacClntAcctFollowReceived,'fsTacClntAcctSessionTimeouts':fsTacClntAcctSessionTimeouts,'fsTacClntMalformedPktsReceived':fsTacClntMalformedPktsReceived,'fsTacClntSocketFailures':fsTacClntSocketFailures,'fsTacClntConnectionFailures':fsTacClntConnectionFailures,'futureTacacsClientTableGroup':futureTacacsClientTableGroup,'fsTacClntServerTable':fsTacClntServerTable,'fsTacClntServerEntry':fsTacClntServerEntry,_G:fsTacClntServerAddress,'fsTacClntServerStatus':fsTacClntServerStatus,'fsTacClntServerSingleConnect':fsTacClntServerSingleConnect,'fsTacClntServerPort':fsTacClntServerPort,'fsTacClntServerTimeout':fsTacClntServerTimeout,'fsTacClntServerKey':fsTacClntServerKey})