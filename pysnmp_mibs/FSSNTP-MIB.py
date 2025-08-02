_T='obsolete'
_S='microseconds'
_R='not-accessible'
_Q='fsSntpUnicastServerAddr'
_P='fsSntpUnicastServerAddrType'
_O='multicast'
_N='broadcast'
_M='version4'
_L='version3'
_K='OctetString'
_J='FSSNTP-MIB'
_I='enabled'
_H='disabled'
_G='DisplayString'
_F='seconds'
_E='Unsigned32'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
fsSntpMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,149))
if mibBuilder.loadTexts:fsSntpMIB.setRevisions(('2012-09-05 00:00',))
_FsSntp_ObjectIdentity=ObjectIdentity
fsSntp=_FsSntp_ObjectIdentity((1,3,6,1,4,1,10876,101,1,149,1))
_FsSntpScalars_ObjectIdentity=ObjectIdentity
fsSntpScalars=_FsSntpScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,149,1,1))
class _FsSntpGlobalTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSntpGlobalTrace_Type.__name__=_C
_FsSntpGlobalTrace_Object=MibScalar
fsSntpGlobalTrace=_FsSntpGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,149,1,1,1),_FsSntpGlobalTrace_Type())
fsSntpGlobalTrace.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpGlobalTrace.setStatus(_A)
class _FsSntpGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsSntpGlobalDebug_Type.__name__=_C
_FsSntpGlobalDebug_Object=MibScalar
fsSntpGlobalDebug=_FsSntpGlobalDebug_Object((1,3,6,1,4,1,10876,101,1,149,1,1,2),_FsSntpGlobalDebug_Type())
fsSntpGlobalDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpGlobalDebug.setStatus(_A)
class _FsSntpAdminStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_FsSntpAdminStatus_Type.__name__=_C
_FsSntpAdminStatus_Object=MibScalar
fsSntpAdminStatus=_FsSntpAdminStatus_Object((1,3,6,1,4,1,10876,101,1,149,1,1,3),_FsSntpAdminStatus_Type())
fsSntpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAdminStatus.setStatus(_A)
class _FsSntpClientVersion_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('version1',1),('version2',2),(_L,3),(_M,4)))
_FsSntpClientVersion_Type.__name__=_C
_FsSntpClientVersion_Object=MibScalar
fsSntpClientVersion=_FsSntpClientVersion_Object((1,3,6,1,4,1,10876,101,1,149,1,1,4),_FsSntpClientVersion_Type())
fsSntpClientVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpClientVersion.setStatus(_A)
class _FsSntpClientAddressingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unicast',1),(_N,2),(_O,3),('manycast',4)))
_FsSntpClientAddressingMode_Type.__name__=_C
_FsSntpClientAddressingMode_Object=MibScalar
fsSntpClientAddressingMode=_FsSntpClientAddressingMode_Object((1,3,6,1,4,1,10876,101,1,149,1,1,5),_FsSntpClientAddressingMode_Type())
fsSntpClientAddressingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpClientAddressingMode.setStatus(_A)
class _FsSntpClientPort_Type(Integer32):defaultValue=123;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(123,123),ValueRangeConstraint(1025,65535))
_FsSntpClientPort_Type.__name__=_C
_FsSntpClientPort_Object=MibScalar
fsSntpClientPort=_FsSntpClientPort_Object((1,3,6,1,4,1,10876,101,1,149,1,1,6),_FsSntpClientPort_Type())
fsSntpClientPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpClientPort.setStatus(_A)
class _FsSntpTimeDisplayFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hours',1),('ampm',2)))
_FsSntpTimeDisplayFormat_Type.__name__=_C
_FsSntpTimeDisplayFormat_Object=MibScalar
fsSntpTimeDisplayFormat=_FsSntpTimeDisplayFormat_Object((1,3,6,1,4,1,10876,101,1,149,1,1,7),_FsSntpTimeDisplayFormat_Type())
fsSntpTimeDisplayFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpTimeDisplayFormat.setStatus(_A)
_FsSntpAuthKeyId_Type=Integer32
_FsSntpAuthKeyId_Object=MibScalar
fsSntpAuthKeyId=_FsSntpAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,149,1,1,8),_FsSntpAuthKeyId_Type())
fsSntpAuthKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAuthKeyId.setStatus(_A)
class _FsSntpAuthAlgorithm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('md5',1),('des',2)))
_FsSntpAuthAlgorithm_Type.__name__=_C
_FsSntpAuthAlgorithm_Object=MibScalar
fsSntpAuthAlgorithm=_FsSntpAuthAlgorithm_Object((1,3,6,1,4,1,10876,101,1,149,1,1,9),_FsSntpAuthAlgorithm_Type())
fsSntpAuthAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAuthAlgorithm.setStatus(_A)
class _FsSntpAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsSntpAuthKey_Type.__name__=_K
_FsSntpAuthKey_Object=MibScalar
fsSntpAuthKey=_FsSntpAuthKey_Object((1,3,6,1,4,1,10876,101,1,149,1,1,10),_FsSntpAuthKey_Type())
fsSntpAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAuthKey.setStatus(_A)
class _FsSntpTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_FsSntpTimeZone_Type.__name__=_G
_FsSntpTimeZone_Object=MibScalar
fsSntpTimeZone=_FsSntpTimeZone_Object((1,3,6,1,4,1,10876,101,1,149,1,1,11),_FsSntpTimeZone_Type())
fsSntpTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpTimeZone.setStatus(_A)
class _FsSntpDSTStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_FsSntpDSTStartTime_Type.__name__=_G
_FsSntpDSTStartTime_Object=MibScalar
fsSntpDSTStartTime=_FsSntpDSTStartTime_Object((1,3,6,1,4,1,10876,101,1,149,1,1,12),_FsSntpDSTStartTime_Type())
fsSntpDSTStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpDSTStartTime.setStatus(_A)
class _FsSntpDSTEndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_FsSntpDSTEndTime_Type.__name__=_G
_FsSntpDSTEndTime_Object=MibScalar
fsSntpDSTEndTime=_FsSntpDSTEndTime_Object((1,3,6,1,4,1,10876,101,1,149,1,1,13),_FsSntpDSTEndTime_Type())
fsSntpDSTEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpDSTEndTime.setStatus(_A)
_FsSntpClientUptime_Type=Unsigned32
_FsSntpClientUptime_Object=MibScalar
fsSntpClientUptime=_FsSntpClientUptime_Object((1,3,6,1,4,1,10876,101,1,149,1,1,14),_FsSntpClientUptime_Type())
fsSntpClientUptime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpClientUptime.setStatus(_A)
class _FsSntpClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('notRunning',1),('notSynchronized',2),('noneConfigured',3),('syncToLocal',4),('syncToRemoteServer',5),('unknown',99)))
_FsSntpClientStatus_Type.__name__=_C
_FsSntpClientStatus_Object=MibScalar
fsSntpClientStatus=_FsSntpClientStatus_Object((1,3,6,1,4,1,10876,101,1,149,1,1,15),_FsSntpClientStatus_Type())
fsSntpClientStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpClientStatus.setStatus(_A)
_FsSntpServerReplyRxCount_Type=Counter32
_FsSntpServerReplyRxCount_Object=MibScalar
fsSntpServerReplyRxCount=_FsSntpServerReplyRxCount_Object((1,3,6,1,4,1,10876,101,1,149,1,1,16),_FsSntpServerReplyRxCount_Type())
fsSntpServerReplyRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpServerReplyRxCount.setStatus(_A)
_FsSntpClientReqTxCount_Type=Counter32
_FsSntpClientReqTxCount_Object=MibScalar
fsSntpClientReqTxCount=_FsSntpClientReqTxCount_Object((1,3,6,1,4,1,10876,101,1,149,1,1,17),_FsSntpClientReqTxCount_Type())
fsSntpClientReqTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpClientReqTxCount.setStatus(_A)
_FsSntpPktInDiscardCount_Type=Counter32
_FsSntpPktInDiscardCount_Object=MibScalar
fsSntpPktInDiscardCount=_FsSntpPktInDiscardCount_Object((1,3,6,1,4,1,10876,101,1,149,1,1,18),_FsSntpPktInDiscardCount_Type())
fsSntpPktInDiscardCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpPktInDiscardCount.setStatus(_A)
_FsSntpUnicast_ObjectIdentity=ObjectIdentity
fsSntpUnicast=_FsSntpUnicast_ObjectIdentity((1,3,6,1,4,1,10876,101,1,149,1,2))
class _FsSntpServerAutoDiscovery_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_FsSntpServerAutoDiscovery_Type.__name__=_C
_FsSntpServerAutoDiscovery_Object=MibScalar
fsSntpServerAutoDiscovery=_FsSntpServerAutoDiscovery_Object((1,3,6,1,4,1,10876,101,1,149,1,2,1),_FsSntpServerAutoDiscovery_Type())
fsSntpServerAutoDiscovery.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpServerAutoDiscovery.setStatus(_A)
class _FsSntpUnicastPollInterval_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16284))
_FsSntpUnicastPollInterval_Type.__name__=_E
_FsSntpUnicastPollInterval_Object=MibScalar
fsSntpUnicastPollInterval=_FsSntpUnicastPollInterval_Object((1,3,6,1,4,1,10876,101,1,149,1,2,2),_FsSntpUnicastPollInterval_Type())
fsSntpUnicastPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastPollInterval.setStatus(_A)
if mibBuilder.loadTexts:fsSntpUnicastPollInterval.setUnits(_F)
class _FsSntpUnicastPollTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_FsSntpUnicastPollTimeout_Type.__name__=_E
_FsSntpUnicastPollTimeout_Object=MibScalar
fsSntpUnicastPollTimeout=_FsSntpUnicastPollTimeout_Object((1,3,6,1,4,1,10876,101,1,149,1,2,3),_FsSntpUnicastPollTimeout_Type())
fsSntpUnicastPollTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastPollTimeout.setStatus(_A)
if mibBuilder.loadTexts:fsSntpUnicastPollTimeout.setUnits(_F)
class _FsSntpUnicastPollRetry_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsSntpUnicastPollRetry_Type.__name__=_E
_FsSntpUnicastPollRetry_Object=MibScalar
fsSntpUnicastPollRetry=_FsSntpUnicastPollRetry_Object((1,3,6,1,4,1,10876,101,1,149,1,2,4),_FsSntpUnicastPollRetry_Type())
fsSntpUnicastPollRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastPollRetry.setStatus(_A)
_FsSntpUnicastServerTable_Object=MibTable
fsSntpUnicastServerTable=_FsSntpUnicastServerTable_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5))
if mibBuilder.loadTexts:fsSntpUnicastServerTable.setStatus(_A)
_FsSntpUnicastServerEntry_Object=MibTableRow
fsSntpUnicastServerEntry=_FsSntpUnicastServerEntry_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1))
fsSntpUnicastServerEntry.setIndexNames((0,_J,_P),(0,_J,_Q))
if mibBuilder.loadTexts:fsSntpUnicastServerEntry.setStatus(_A)
_FsSntpUnicastServerAddrType_Type=InetAddressType
_FsSntpUnicastServerAddrType_Object=MibTableColumn
fsSntpUnicastServerAddrType=_FsSntpUnicastServerAddrType_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,1),_FsSntpUnicastServerAddrType_Type())
fsSntpUnicastServerAddrType.setMaxAccess(_R)
if mibBuilder.loadTexts:fsSntpUnicastServerAddrType.setStatus(_A)
_FsSntpUnicastServerAddr_Type=InetAddress
_FsSntpUnicastServerAddr_Object=MibTableColumn
fsSntpUnicastServerAddr=_FsSntpUnicastServerAddr_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,2),_FsSntpUnicastServerAddr_Type())
fsSntpUnicastServerAddr.setMaxAccess(_R)
if mibBuilder.loadTexts:fsSntpUnicastServerAddr.setStatus(_A)
class _FsSntpUnicastServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_L,3),(_M,4)))
_FsSntpUnicastServerVersion_Type.__name__=_C
_FsSntpUnicastServerVersion_Object=MibTableColumn
fsSntpUnicastServerVersion=_FsSntpUnicastServerVersion_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,3),_FsSntpUnicastServerVersion_Type())
fsSntpUnicastServerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastServerVersion.setStatus(_A)
class _FsSntpUnicastServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(123,123),ValueRangeConstraint(1025,65535))
_FsSntpUnicastServerPort_Type.__name__=_C
_FsSntpUnicastServerPort_Object=MibTableColumn
fsSntpUnicastServerPort=_FsSntpUnicastServerPort_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,4),_FsSntpUnicastServerPort_Type())
fsSntpUnicastServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastServerPort.setStatus(_A)
class _FsSntpUnicastServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_FsSntpUnicastServerType_Type.__name__=_C
_FsSntpUnicastServerType_Object=MibTableColumn
fsSntpUnicastServerType=_FsSntpUnicastServerType_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,5),_FsSntpUnicastServerType_Type())
fsSntpUnicastServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastServerType.setStatus(_A)
_FsSntpUnicastServerLastUpdateTime_Type=DisplayString
_FsSntpUnicastServerLastUpdateTime_Object=MibTableColumn
fsSntpUnicastServerLastUpdateTime=_FsSntpUnicastServerLastUpdateTime_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,6),_FsSntpUnicastServerLastUpdateTime_Type())
fsSntpUnicastServerLastUpdateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpUnicastServerLastUpdateTime.setStatus(_A)
_FsSntpUnicastServerTxRequests_Type=Counter32
_FsSntpUnicastServerTxRequests_Object=MibTableColumn
fsSntpUnicastServerTxRequests=_FsSntpUnicastServerTxRequests_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,7),_FsSntpUnicastServerTxRequests_Type())
fsSntpUnicastServerTxRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpUnicastServerTxRequests.setStatus(_A)
_FsSntpUnicastServerRowStatus_Type=RowStatus
_FsSntpUnicastServerRowStatus_Object=MibTableColumn
fsSntpUnicastServerRowStatus=_FsSntpUnicastServerRowStatus_Object((1,3,6,1,4,1,10876,101,1,149,1,2,5,1,8),_FsSntpUnicastServerRowStatus_Type())
fsSntpUnicastServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpUnicastServerRowStatus.setStatus(_A)
_FsSntpBroadcast_ObjectIdentity=ObjectIdentity
fsSntpBroadcast=_FsSntpBroadcast_ObjectIdentity((1,3,6,1,4,1,10876,101,1,149,1,3))
class _FsSntpSendRequestInBcastMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_FsSntpSendRequestInBcastMode_Type.__name__=_C
_FsSntpSendRequestInBcastMode_Object=MibScalar
fsSntpSendRequestInBcastMode=_FsSntpSendRequestInBcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,3,1),_FsSntpSendRequestInBcastMode_Type())
fsSntpSendRequestInBcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpSendRequestInBcastMode.setStatus(_A)
class _FsSntpPollTimeoutInBcastMode_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_FsSntpPollTimeoutInBcastMode_Type.__name__=_E
_FsSntpPollTimeoutInBcastMode_Object=MibScalar
fsSntpPollTimeoutInBcastMode=_FsSntpPollTimeoutInBcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,3,2),_FsSntpPollTimeoutInBcastMode_Type())
fsSntpPollTimeoutInBcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpPollTimeoutInBcastMode.setStatus(_A)
if mibBuilder.loadTexts:fsSntpPollTimeoutInBcastMode.setUnits(_F)
class _FsSntpDelayTimeInBcastMode_Type(Unsigned32):defaultValue=8000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,15000))
_FsSntpDelayTimeInBcastMode_Type.__name__=_E
_FsSntpDelayTimeInBcastMode_Object=MibScalar
fsSntpDelayTimeInBcastMode=_FsSntpDelayTimeInBcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,3,3),_FsSntpDelayTimeInBcastMode_Type())
fsSntpDelayTimeInBcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpDelayTimeInBcastMode.setStatus(_A)
if mibBuilder.loadTexts:fsSntpDelayTimeInBcastMode.setUnits(_S)
_FsSntpPrimaryServerAddrInBcastMode_Type=IpAddress
_FsSntpPrimaryServerAddrInBcastMode_Object=MibScalar
fsSntpPrimaryServerAddrInBcastMode=_FsSntpPrimaryServerAddrInBcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,3,4),_FsSntpPrimaryServerAddrInBcastMode_Type())
fsSntpPrimaryServerAddrInBcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpPrimaryServerAddrInBcastMode.setStatus(_A)
_FsSntpSecondaryServerAddrInBcastMode_Type=IpAddress
_FsSntpSecondaryServerAddrInBcastMode_Object=MibScalar
fsSntpSecondaryServerAddrInBcastMode=_FsSntpSecondaryServerAddrInBcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,3,5),_FsSntpSecondaryServerAddrInBcastMode_Type())
fsSntpSecondaryServerAddrInBcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpSecondaryServerAddrInBcastMode.setStatus(_A)
_FsSntpMulticast_ObjectIdentity=ObjectIdentity
fsSntpMulticast=_FsSntpMulticast_ObjectIdentity((1,3,6,1,4,1,10876,101,1,149,1,4))
class _FsSntpSendRequestInMcastMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_FsSntpSendRequestInMcastMode_Type.__name__=_C
_FsSntpSendRequestInMcastMode_Object=MibScalar
fsSntpSendRequestInMcastMode=_FsSntpSendRequestInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,1),_FsSntpSendRequestInMcastMode_Type())
fsSntpSendRequestInMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpSendRequestInMcastMode.setStatus(_A)
class _FsSntpPollTimeoutInMcastMode_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_FsSntpPollTimeoutInMcastMode_Type.__name__=_E
_FsSntpPollTimeoutInMcastMode_Object=MibScalar
fsSntpPollTimeoutInMcastMode=_FsSntpPollTimeoutInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,2),_FsSntpPollTimeoutInMcastMode_Type())
fsSntpPollTimeoutInMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpPollTimeoutInMcastMode.setStatus(_A)
if mibBuilder.loadTexts:fsSntpPollTimeoutInMcastMode.setUnits(_F)
class _FsSntpDelayTimeInMcastMode_Type(Unsigned32):defaultValue=8000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,15000))
_FsSntpDelayTimeInMcastMode_Type.__name__=_E
_FsSntpDelayTimeInMcastMode_Object=MibScalar
fsSntpDelayTimeInMcastMode=_FsSntpDelayTimeInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,3),_FsSntpDelayTimeInMcastMode_Type())
fsSntpDelayTimeInMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpDelayTimeInMcastMode.setStatus(_A)
if mibBuilder.loadTexts:fsSntpDelayTimeInMcastMode.setUnits(_S)
_FsSntpGrpAddrTypeInMcastMode_Type=InetAddressType
_FsSntpGrpAddrTypeInMcastMode_Object=MibScalar
fsSntpGrpAddrTypeInMcastMode=_FsSntpGrpAddrTypeInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,4),_FsSntpGrpAddrTypeInMcastMode_Type())
fsSntpGrpAddrTypeInMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpGrpAddrTypeInMcastMode.setStatus(_A)
_FsSntpGrpAddrInMcastMode_Type=InetAddress
_FsSntpGrpAddrInMcastMode_Object=MibScalar
fsSntpGrpAddrInMcastMode=_FsSntpGrpAddrInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,5),_FsSntpGrpAddrInMcastMode_Type())
fsSntpGrpAddrInMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpGrpAddrInMcastMode.setStatus(_A)
_FsSntpPrimaryServerAddrTypeInMcastMode_Type=InetAddressType
_FsSntpPrimaryServerAddrTypeInMcastMode_Object=MibScalar
fsSntpPrimaryServerAddrTypeInMcastMode=_FsSntpPrimaryServerAddrTypeInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,6),_FsSntpPrimaryServerAddrTypeInMcastMode_Type())
fsSntpPrimaryServerAddrTypeInMcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpPrimaryServerAddrTypeInMcastMode.setStatus(_A)
_FsSntpPrimaryServerAddrInMcastMode_Type=InetAddress
_FsSntpPrimaryServerAddrInMcastMode_Object=MibScalar
fsSntpPrimaryServerAddrInMcastMode=_FsSntpPrimaryServerAddrInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,7),_FsSntpPrimaryServerAddrInMcastMode_Type())
fsSntpPrimaryServerAddrInMcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpPrimaryServerAddrInMcastMode.setStatus(_A)
_FsSntpSecondaryServerAddrTypeInMcastMode_Type=InetAddressType
_FsSntpSecondaryServerAddrTypeInMcastMode_Object=MibScalar
fsSntpSecondaryServerAddrTypeInMcastMode=_FsSntpSecondaryServerAddrTypeInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,8),_FsSntpSecondaryServerAddrTypeInMcastMode_Type())
fsSntpSecondaryServerAddrTypeInMcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpSecondaryServerAddrTypeInMcastMode.setStatus(_A)
_FsSntpSecondaryServerAddrInMcastMode_Type=InetAddress
_FsSntpSecondaryServerAddrInMcastMode_Object=MibScalar
fsSntpSecondaryServerAddrInMcastMode=_FsSntpSecondaryServerAddrInMcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,4,9),_FsSntpSecondaryServerAddrInMcastMode_Type())
fsSntpSecondaryServerAddrInMcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpSecondaryServerAddrInMcastMode.setStatus(_A)
_FsSntpAnycast_ObjectIdentity=ObjectIdentity
fsSntpAnycast=_FsSntpAnycast_ObjectIdentity((1,3,6,1,4,1,10876,101,1,149,1,5))
class _FsSntpAnycastPollInterval_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,16284))
_FsSntpAnycastPollInterval_Type.__name__=_E
_FsSntpAnycastPollInterval_Object=MibScalar
fsSntpAnycastPollInterval=_FsSntpAnycastPollInterval_Object((1,3,6,1,4,1,10876,101,1,149,1,5,1),_FsSntpAnycastPollInterval_Type())
fsSntpAnycastPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAnycastPollInterval.setStatus(_A)
if mibBuilder.loadTexts:fsSntpAnycastPollInterval.setUnits(_F)
class _FsSntpAnycastPollTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_FsSntpAnycastPollTimeout_Type.__name__=_E
_FsSntpAnycastPollTimeout_Object=MibScalar
fsSntpAnycastPollTimeout=_FsSntpAnycastPollTimeout_Object((1,3,6,1,4,1,10876,101,1,149,1,5,2),_FsSntpAnycastPollTimeout_Type())
fsSntpAnycastPollTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAnycastPollTimeout.setStatus(_A)
if mibBuilder.loadTexts:fsSntpAnycastPollTimeout.setUnits(_F)
class _FsSntpAnycastPollRetry_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsSntpAnycastPollRetry_Type.__name__=_E
_FsSntpAnycastPollRetry_Object=MibScalar
fsSntpAnycastPollRetry=_FsSntpAnycastPollRetry_Object((1,3,6,1,4,1,10876,101,1,149,1,5,3),_FsSntpAnycastPollRetry_Type())
fsSntpAnycastPollRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpAnycastPollRetry.setStatus(_A)
class _FsSntpServerTypeInAcastMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_FsSntpServerTypeInAcastMode_Type.__name__=_C
_FsSntpServerTypeInAcastMode_Object=MibScalar
fsSntpServerTypeInAcastMode=_FsSntpServerTypeInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,4),_FsSntpServerTypeInAcastMode_Type())
fsSntpServerTypeInAcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpServerTypeInAcastMode.setStatus(_A)
_FsSntpGrpAddrTypeInAcastMode_Type=InetAddressType
_FsSntpGrpAddrTypeInAcastMode_Object=MibScalar
fsSntpGrpAddrTypeInAcastMode=_FsSntpGrpAddrTypeInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,5),_FsSntpGrpAddrTypeInAcastMode_Type())
fsSntpGrpAddrTypeInAcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpGrpAddrTypeInAcastMode.setStatus(_A)
_FsSntpGrpAddrInAcastMode_Type=InetAddress
_FsSntpGrpAddrInAcastMode_Object=MibScalar
fsSntpGrpAddrInAcastMode=_FsSntpGrpAddrInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,6),_FsSntpGrpAddrInAcastMode_Type())
fsSntpGrpAddrInAcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsSntpGrpAddrInAcastMode.setStatus(_A)
_FsSntpPrimaryServerAddrTypeInAcastMode_Type=InetAddressType
_FsSntpPrimaryServerAddrTypeInAcastMode_Object=MibScalar
fsSntpPrimaryServerAddrTypeInAcastMode=_FsSntpPrimaryServerAddrTypeInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,7),_FsSntpPrimaryServerAddrTypeInAcastMode_Type())
fsSntpPrimaryServerAddrTypeInAcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpPrimaryServerAddrTypeInAcastMode.setStatus(_A)
_FsSntpPrimaryServerAddrInAcastMode_Type=InetAddress
_FsSntpPrimaryServerAddrInAcastMode_Object=MibScalar
fsSntpPrimaryServerAddrInAcastMode=_FsSntpPrimaryServerAddrInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,8),_FsSntpPrimaryServerAddrInAcastMode_Type())
fsSntpPrimaryServerAddrInAcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpPrimaryServerAddrInAcastMode.setStatus(_A)
_FsSntpSecondaryServerAddrTypeInAcastMode_Type=InetAddressType
_FsSntpSecondaryServerAddrTypeInAcastMode_Object=MibScalar
fsSntpSecondaryServerAddrTypeInAcastMode=_FsSntpSecondaryServerAddrTypeInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,9),_FsSntpSecondaryServerAddrTypeInAcastMode_Type())
fsSntpSecondaryServerAddrTypeInAcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpSecondaryServerAddrTypeInAcastMode.setStatus(_T)
_FsSntpSecondaryServerAddrInAcastMode_Type=InetAddress
_FsSntpSecondaryServerAddrInAcastMode_Object=MibScalar
fsSntpSecondaryServerAddrInAcastMode=_FsSntpSecondaryServerAddrInAcastMode_Object((1,3,6,1,4,1,10876,101,1,149,1,5,10),_FsSntpSecondaryServerAddrInAcastMode_Type())
fsSntpSecondaryServerAddrInAcastMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSntpSecondaryServerAddrInAcastMode.setStatus(_T)
mibBuilder.exportSymbols(_J,**{'fsSntpMIB':fsSntpMIB,'fsSntp':fsSntp,'fsSntpScalars':fsSntpScalars,'fsSntpGlobalTrace':fsSntpGlobalTrace,'fsSntpGlobalDebug':fsSntpGlobalDebug,'fsSntpAdminStatus':fsSntpAdminStatus,'fsSntpClientVersion':fsSntpClientVersion,'fsSntpClientAddressingMode':fsSntpClientAddressingMode,'fsSntpClientPort':fsSntpClientPort,'fsSntpTimeDisplayFormat':fsSntpTimeDisplayFormat,'fsSntpAuthKeyId':fsSntpAuthKeyId,'fsSntpAuthAlgorithm':fsSntpAuthAlgorithm,'fsSntpAuthKey':fsSntpAuthKey,'fsSntpTimeZone':fsSntpTimeZone,'fsSntpDSTStartTime':fsSntpDSTStartTime,'fsSntpDSTEndTime':fsSntpDSTEndTime,'fsSntpClientUptime':fsSntpClientUptime,'fsSntpClientStatus':fsSntpClientStatus,'fsSntpServerReplyRxCount':fsSntpServerReplyRxCount,'fsSntpClientReqTxCount':fsSntpClientReqTxCount,'fsSntpPktInDiscardCount':fsSntpPktInDiscardCount,'fsSntpUnicast':fsSntpUnicast,'fsSntpServerAutoDiscovery':fsSntpServerAutoDiscovery,'fsSntpUnicastPollInterval':fsSntpUnicastPollInterval,'fsSntpUnicastPollTimeout':fsSntpUnicastPollTimeout,'fsSntpUnicastPollRetry':fsSntpUnicastPollRetry,'fsSntpUnicastServerTable':fsSntpUnicastServerTable,'fsSntpUnicastServerEntry':fsSntpUnicastServerEntry,_P:fsSntpUnicastServerAddrType,_Q:fsSntpUnicastServerAddr,'fsSntpUnicastServerVersion':fsSntpUnicastServerVersion,'fsSntpUnicastServerPort':fsSntpUnicastServerPort,'fsSntpUnicastServerType':fsSntpUnicastServerType,'fsSntpUnicastServerLastUpdateTime':fsSntpUnicastServerLastUpdateTime,'fsSntpUnicastServerTxRequests':fsSntpUnicastServerTxRequests,'fsSntpUnicastServerRowStatus':fsSntpUnicastServerRowStatus,'fsSntpBroadcast':fsSntpBroadcast,'fsSntpSendRequestInBcastMode':fsSntpSendRequestInBcastMode,'fsSntpPollTimeoutInBcastMode':fsSntpPollTimeoutInBcastMode,'fsSntpDelayTimeInBcastMode':fsSntpDelayTimeInBcastMode,'fsSntpPrimaryServerAddrInBcastMode':fsSntpPrimaryServerAddrInBcastMode,'fsSntpSecondaryServerAddrInBcastMode':fsSntpSecondaryServerAddrInBcastMode,'fsSntpMulticast':fsSntpMulticast,'fsSntpSendRequestInMcastMode':fsSntpSendRequestInMcastMode,'fsSntpPollTimeoutInMcastMode':fsSntpPollTimeoutInMcastMode,'fsSntpDelayTimeInMcastMode':fsSntpDelayTimeInMcastMode,'fsSntpGrpAddrTypeInMcastMode':fsSntpGrpAddrTypeInMcastMode,'fsSntpGrpAddrInMcastMode':fsSntpGrpAddrInMcastMode,'fsSntpPrimaryServerAddrTypeInMcastMode':fsSntpPrimaryServerAddrTypeInMcastMode,'fsSntpPrimaryServerAddrInMcastMode':fsSntpPrimaryServerAddrInMcastMode,'fsSntpSecondaryServerAddrTypeInMcastMode':fsSntpSecondaryServerAddrTypeInMcastMode,'fsSntpSecondaryServerAddrInMcastMode':fsSntpSecondaryServerAddrInMcastMode,'fsSntpAnycast':fsSntpAnycast,'fsSntpAnycastPollInterval':fsSntpAnycastPollInterval,'fsSntpAnycastPollTimeout':fsSntpAnycastPollTimeout,'fsSntpAnycastPollRetry':fsSntpAnycastPollRetry,'fsSntpServerTypeInAcastMode':fsSntpServerTypeInAcastMode,'fsSntpGrpAddrTypeInAcastMode':fsSntpGrpAddrTypeInAcastMode,'fsSntpGrpAddrInAcastMode':fsSntpGrpAddrInAcastMode,'fsSntpPrimaryServerAddrTypeInAcastMode':fsSntpPrimaryServerAddrTypeInAcastMode,'fsSntpPrimaryServerAddrInAcastMode':fsSntpPrimaryServerAddrInAcastMode,'fsSntpSecondaryServerAddrTypeInAcastMode':fsSntpSecondaryServerAddrTypeInAcastMode,'fsSntpSecondaryServerAddrInAcastMode':fsSntpSecondaryServerAddrInAcastMode})