_U='bsRadiusExtDynAuthClientEntry'
_T='bsRadiusDynAuthClientAddress'
_S='bsRadiusDynAuthClientAddressType'
_R='bsRadiusServerIndex'
_Q='Unsigned32'
_P='InetAddress'
_O='bsRadiusServerAddress'
_N='bsRadiusServerAddressType'
_M='not-accessible'
_L='DisplayString'
_K='InetPortNumber'
_J='OctetString'
_I='seconds'
_H='BAY-STACK-RADIUS-MIB'
_G='TruthValue'
_F='requests'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_P,'InetAddressType',_K)
radiusDynAuthClientEntry,=mibBuilder.importSymbols('RADIUS-DYNAUTH-SERVER-MIB','radiusDynAuthClientEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention',_G)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackRadiusMib=ModuleIdentity((1,3,6,1,4,1,45,5,21))
if mibBuilder.loadTexts:bayStackRadiusMib.setRevisions(('2021-03-02 00:00','2015-07-23 00:00','2014-10-20 00:00','2012-03-15 00:00','2010-10-15 00:00','2010-10-14 00:00','2010-09-07 00:00','2010-02-10 00:00','2009-10-13 00:00','2009-05-28 00:00','2009-04-16 00:00','2009-03-30 00:00','2008-10-30 00:00','2008-05-29 00:00','2008-03-25 00:00','2007-04-03 00:00'))
_BsRadiusNotifications_ObjectIdentity=ObjectIdentity
bsRadiusNotifications=_BsRadiusNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,21,0))
_BsRadiusObjects_ObjectIdentity=ObjectIdentity
bsRadiusObjects=_BsRadiusObjects_ObjectIdentity((1,3,6,1,4,1,45,5,21,1))
_BsRadiusScalars_ObjectIdentity=ObjectIdentity
bsRadiusScalars=_BsRadiusScalars_ObjectIdentity((1,3,6,1,4,1,45,5,21,1,1))
class _BsRadiusUseMgmtIp_Type(TruthValue):defaultValue=1
_BsRadiusUseMgmtIp_Type.__name__=_G
_BsRadiusUseMgmtIp_Object=MibScalar
bsRadiusUseMgmtIp=_BsRadiusUseMgmtIp_Object((1,3,6,1,4,1,45,5,21,1,1,1),_BsRadiusUseMgmtIp_Type())
bsRadiusUseMgmtIp.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusUseMgmtIp.setStatus(_A)
class _BsRadiusAccountingEnabled_Type(TruthValue):defaultValue=2
_BsRadiusAccountingEnabled_Type.__name__=_G
_BsRadiusAccountingEnabled_Object=MibScalar
bsRadiusAccountingEnabled=_BsRadiusAccountingEnabled_Object((1,3,6,1,4,1,45,5,21,1,1,2),_BsRadiusAccountingEnabled_Type())
bsRadiusAccountingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusAccountingEnabled.setStatus(_A)
class _BsRadiusPasswordFallbackEnabled_Type(TruthValue):defaultValue=2
_BsRadiusPasswordFallbackEnabled_Type.__name__=_G
_BsRadiusPasswordFallbackEnabled_Object=MibScalar
bsRadiusPasswordFallbackEnabled=_BsRadiusPasswordFallbackEnabled_Object((1,3,6,1,4,1,45,5,21,1,1,3),_BsRadiusPasswordFallbackEnabled_Type())
bsRadiusPasswordFallbackEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusPasswordFallbackEnabled.setStatus(_A)
class _BsRadiusAccountingPort_Type(InetPortNumber):defaultValue=1813
_BsRadiusAccountingPort_Type.__name__=_K
_BsRadiusAccountingPort_Object=MibScalar
bsRadiusAccountingPort=_BsRadiusAccountingPort_Object((1,3,6,1,4,1,45,5,21,1,1,4),_BsRadiusAccountingPort_Type())
bsRadiusAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusAccountingPort.setStatus(_A)
class _BsRadiusAccountingInterimUpdates_Type(TruthValue):defaultValue=2
_BsRadiusAccountingInterimUpdates_Type.__name__=_G
_BsRadiusAccountingInterimUpdates_Object=MibScalar
bsRadiusAccountingInterimUpdates=_BsRadiusAccountingInterimUpdates_Object((1,3,6,1,4,1,45,5,21,1,1,5),_BsRadiusAccountingInterimUpdates_Type())
bsRadiusAccountingInterimUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusAccountingInterimUpdates.setStatus(_A)
class _BsRadiusAccountingInterimUpdatesInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,3600))
_BsRadiusAccountingInterimUpdatesInterval_Type.__name__=_Q
_BsRadiusAccountingInterimUpdatesInterval_Object=MibScalar
bsRadiusAccountingInterimUpdatesInterval=_BsRadiusAccountingInterimUpdatesInterval_Object((1,3,6,1,4,1,45,5,21,1,1,6),_BsRadiusAccountingInterimUpdatesInterval_Type())
bsRadiusAccountingInterimUpdatesInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusAccountingInterimUpdatesInterval.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusAccountingInterimUpdatesInterval.setUnits(_I)
class _BsRadiusAccountingInterimUpdatesIntervalSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configuredValue',1),('radiusServer',2)))
_BsRadiusAccountingInterimUpdatesIntervalSource_Type.__name__=_D
_BsRadiusAccountingInterimUpdatesIntervalSource_Object=MibScalar
bsRadiusAccountingInterimUpdatesIntervalSource=_BsRadiusAccountingInterimUpdatesIntervalSource_Object((1,3,6,1,4,1,45,5,21,1,1,7),_BsRadiusAccountingInterimUpdatesIntervalSource_Type())
bsRadiusAccountingInterimUpdatesIntervalSource.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusAccountingInterimUpdatesIntervalSource.setStatus(_A)
_BsRadiusDynAuthReplayProtection_Type=TruthValue
_BsRadiusDynAuthReplayProtection_Object=MibScalar
bsRadiusDynAuthReplayProtection=_BsRadiusDynAuthReplayProtection_Object((1,3,6,1,4,1,45,5,21,1,1,8),_BsRadiusDynAuthReplayProtection_Type())
bsRadiusDynAuthReplayProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusDynAuthReplayProtection.setStatus(_A)
class _BsRadiusReachability_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('useRadius',1),('useIcmp',2),('useStatusServer',3)))
_BsRadiusReachability_Type.__name__=_D
_BsRadiusReachability_Object=MibScalar
bsRadiusReachability=_BsRadiusReachability_Object((1,3,6,1,4,1,45,5,21,1,1,9),_BsRadiusReachability_Type())
bsRadiusReachability.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachability.setStatus(_A)
class _BsRadiusReachabilityUserName_Type(DisplayString):defaultValue=OctetString('avaya');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_BsRadiusReachabilityUserName_Type.__name__=_L
_BsRadiusReachabilityUserName_Object=MibScalar
bsRadiusReachabilityUserName=_BsRadiusReachabilityUserName_Object((1,3,6,1,4,1,45,5,21,1,1,10),_BsRadiusReachabilityUserName_Type())
bsRadiusReachabilityUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachabilityUserName.setStatus(_A)
class _BsRadiusReachabilityPassword_Type(DisplayString):defaultValue=OctetString('avaya');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_BsRadiusReachabilityPassword_Type.__name__=_L
_BsRadiusReachabilityPassword_Object=MibScalar
bsRadiusReachabilityPassword=_BsRadiusReachabilityPassword_Object((1,3,6,1,4,1,45,5,21,1,1,11),_BsRadiusReachabilityPassword_Type())
bsRadiusReachabilityPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachabilityPassword.setStatus(_A)
class _BsRadiusEncapsulationProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pap',1),('ms-chap-v2',2)))
_BsRadiusEncapsulationProtocol_Type.__name__=_D
_BsRadiusEncapsulationProtocol_Object=MibScalar
bsRadiusEncapsulationProtocol=_BsRadiusEncapsulationProtocol_Object((1,3,6,1,4,1,45,5,21,1,1,12),_BsRadiusEncapsulationProtocol_Type())
bsRadiusEncapsulationProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusEncapsulationProtocol.setStatus(_A)
class _BsRadiusReachabilityTimeout_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_BsRadiusReachabilityTimeout_Type.__name__=_D
_BsRadiusReachabilityTimeout_Object=MibScalar
bsRadiusReachabilityTimeout=_BsRadiusReachabilityTimeout_Object((1,3,6,1,4,1,45,5,21,1,1,13),_BsRadiusReachabilityTimeout_Type())
bsRadiusReachabilityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachabilityTimeout.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusReachabilityTimeout.setUnits(_I)
class _BsRadiusReachabilityRetry_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_BsRadiusReachabilityRetry_Type.__name__=_D
_BsRadiusReachabilityRetry_Object=MibScalar
bsRadiusReachabilityRetry=_BsRadiusReachabilityRetry_Object((1,3,6,1,4,1,45,5,21,1,1,14),_BsRadiusReachabilityRetry_Type())
bsRadiusReachabilityRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachabilityRetry.setStatus(_A)
class _BsRadiusReachabilityBadTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_BsRadiusReachabilityBadTimer_Type.__name__=_D
_BsRadiusReachabilityBadTimer_Object=MibScalar
bsRadiusReachabilityBadTimer=_BsRadiusReachabilityBadTimer_Object((1,3,6,1,4,1,45,5,21,1,1,15),_BsRadiusReachabilityBadTimer_Type())
bsRadiusReachabilityBadTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachabilityBadTimer.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusReachabilityBadTimer.setUnits(_I)
class _BsRadiusReachabilityGoodTimer_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_BsRadiusReachabilityGoodTimer_Type.__name__=_D
_BsRadiusReachabilityGoodTimer_Object=MibScalar
bsRadiusReachabilityGoodTimer=_BsRadiusReachabilityGoodTimer_Object((1,3,6,1,4,1,45,5,21,1,1,16),_BsRadiusReachabilityGoodTimer_Type())
bsRadiusReachabilityGoodTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusReachabilityGoodTimer.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusReachabilityGoodTimer.setUnits(_I)
_BsRadiusServerTable_Object=MibTable
bsRadiusServerTable=_BsRadiusServerTable_Object((1,3,6,1,4,1,45,5,21,1,2))
if mibBuilder.loadTexts:bsRadiusServerTable.setStatus(_A)
_BsRadiusServerEntry_Object=MibTableRow
bsRadiusServerEntry=_BsRadiusServerEntry_Object((1,3,6,1,4,1,45,5,21,1,2,1))
bsRadiusServerEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:bsRadiusServerEntry.setStatus(_A)
class _BsRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_BsRadiusServerIndex_Type.__name__=_D
_BsRadiusServerIndex_Object=MibTableColumn
bsRadiusServerIndex=_BsRadiusServerIndex_Object((1,3,6,1,4,1,45,5,21,1,2,1,1),_BsRadiusServerIndex_Type())
bsRadiusServerIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:bsRadiusServerIndex.setStatus(_A)
class _BsRadiusServerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BsRadiusServerPriority_Type.__name__=_D
_BsRadiusServerPriority_Object=MibTableColumn
bsRadiusServerPriority=_BsRadiusServerPriority_Object((1,3,6,1,4,1,45,5,21,1,2,1,2),_BsRadiusServerPriority_Type())
bsRadiusServerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerPriority.setStatus(_A)
_BsRadiusServerAddressType_Type=InetAddressType
_BsRadiusServerAddressType_Object=MibTableColumn
bsRadiusServerAddressType=_BsRadiusServerAddressType_Object((1,3,6,1,4,1,45,5,21,1,2,1,3),_BsRadiusServerAddressType_Type())
bsRadiusServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerAddressType.setStatus(_A)
_BsRadiusServerAddress_Type=InetAddress
_BsRadiusServerAddress_Object=MibTableColumn
bsRadiusServerAddress=_BsRadiusServerAddress_Object((1,3,6,1,4,1,45,5,21,1,2,1,4),_BsRadiusServerAddress_Type())
bsRadiusServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerAddress.setStatus(_A)
_BsRadiusServerUdpPort_Type=InetPortNumber
_BsRadiusServerUdpPort_Object=MibTableColumn
bsRadiusServerUdpPort=_BsRadiusServerUdpPort_Object((1,3,6,1,4,1,45,5,21,1,2,1,5),_BsRadiusServerUdpPort_Type())
bsRadiusServerUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerUdpPort.setStatus(_A)
_BsRadiusServerTimeout_Type=Integer32
_BsRadiusServerTimeout_Object=MibTableColumn
bsRadiusServerTimeout=_BsRadiusServerTimeout_Object((1,3,6,1,4,1,45,5,21,1,2,1,6),_BsRadiusServerTimeout_Type())
bsRadiusServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerTimeout.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusServerTimeout.setUnits(_I)
class _BsRadiusServerSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BsRadiusServerSecret_Type.__name__=_J
_BsRadiusServerSecret_Object=MibTableColumn
bsRadiusServerSecret=_BsRadiusServerSecret_Object((1,3,6,1,4,1,45,5,21,1,2,1,7),_BsRadiusServerSecret_Type())
bsRadiusServerSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerSecret.setStatus(_A)
_BsRadiusServerRowStatus_Type=RowStatus
_BsRadiusServerRowStatus_Object=MibTableColumn
bsRadiusServerRowStatus=_BsRadiusServerRowStatus_Object((1,3,6,1,4,1,45,5,21,1,2,1,8),_BsRadiusServerRowStatus_Type())
bsRadiusServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusServerRowStatus.setStatus(_A)
_BsRadiusServerAccountingPort_Type=InetPortNumber
_BsRadiusServerAccountingPort_Object=MibTableColumn
bsRadiusServerAccountingPort=_BsRadiusServerAccountingPort_Object((1,3,6,1,4,1,45,5,21,1,2,1,9),_BsRadiusServerAccountingPort_Type())
bsRadiusServerAccountingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusServerAccountingPort.setStatus(_A)
class _BsRadiusServerAccountingEnabled_Type(TruthValue):defaultValue=2
_BsRadiusServerAccountingEnabled_Type.__name__=_G
_BsRadiusServerAccountingEnabled_Object=MibTableColumn
bsRadiusServerAccountingEnabled=_BsRadiusServerAccountingEnabled_Object((1,3,6,1,4,1,45,5,21,1,2,1,10),_BsRadiusServerAccountingEnabled_Type())
bsRadiusServerAccountingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusServerAccountingEnabled.setStatus(_A)
class _BsRadiusServerRetryLimit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_BsRadiusServerRetryLimit_Type.__name__=_D
_BsRadiusServerRetryLimit_Object=MibTableColumn
bsRadiusServerRetryLimit=_BsRadiusServerRetryLimit_Object((1,3,6,1,4,1,45,5,21,1,2,1,11),_BsRadiusServerRetryLimit_Type())
bsRadiusServerRetryLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bsRadiusServerRetryLimit.setStatus(_A)
_BsRadiusDynAuthClientTable_Object=MibTable
bsRadiusDynAuthClientTable=_BsRadiusDynAuthClientTable_Object((1,3,6,1,4,1,45,5,21,1,3))
if mibBuilder.loadTexts:bsRadiusDynAuthClientTable.setStatus(_A)
_BsRadiusDynAuthClientEntry_Object=MibTableRow
bsRadiusDynAuthClientEntry=_BsRadiusDynAuthClientEntry_Object((1,3,6,1,4,1,45,5,21,1,3,1))
bsRadiusDynAuthClientEntry.setIndexNames((0,_H,_S),(0,_H,_T))
if mibBuilder.loadTexts:bsRadiusDynAuthClientEntry.setStatus(_A)
_BsRadiusDynAuthClientAddressType_Type=InetAddressType
_BsRadiusDynAuthClientAddressType_Object=MibTableColumn
bsRadiusDynAuthClientAddressType=_BsRadiusDynAuthClientAddressType_Object((1,3,6,1,4,1,45,5,21,1,3,1,1),_BsRadiusDynAuthClientAddressType_Type())
bsRadiusDynAuthClientAddressType.setMaxAccess(_M)
if mibBuilder.loadTexts:bsRadiusDynAuthClientAddressType.setStatus(_A)
class _BsRadiusDynAuthClientAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,113))
_BsRadiusDynAuthClientAddress_Type.__name__=_P
_BsRadiusDynAuthClientAddress_Object=MibTableColumn
bsRadiusDynAuthClientAddress=_BsRadiusDynAuthClientAddress_Object((1,3,6,1,4,1,45,5,21,1,3,1,2),_BsRadiusDynAuthClientAddress_Type())
bsRadiusDynAuthClientAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:bsRadiusDynAuthClientAddress.setStatus(_A)
class _BsRadiusDynAuthClientUdpPort_Type(InetPortNumber):defaultValue=3799
_BsRadiusDynAuthClientUdpPort_Type.__name__=_K
_BsRadiusDynAuthClientUdpPort_Object=MibTableColumn
bsRadiusDynAuthClientUdpPort=_BsRadiusDynAuthClientUdpPort_Object((1,3,6,1,4,1,45,5,21,1,3,1,3),_BsRadiusDynAuthClientUdpPort_Type())
bsRadiusDynAuthClientUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientUdpPort.setStatus(_A)
class _BsRadiusDynAuthClientSecret_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_BsRadiusDynAuthClientSecret_Type.__name__=_J
_BsRadiusDynAuthClientSecret_Object=MibTableColumn
bsRadiusDynAuthClientSecret=_BsRadiusDynAuthClientSecret_Object((1,3,6,1,4,1,45,5,21,1,3,1,4),_BsRadiusDynAuthClientSecret_Type())
bsRadiusDynAuthClientSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientSecret.setStatus(_A)
class _BsRadiusDynAuthClientEnabled_Type(TruthValue):defaultValue=2
_BsRadiusDynAuthClientEnabled_Type.__name__=_G
_BsRadiusDynAuthClientEnabled_Object=MibTableColumn
bsRadiusDynAuthClientEnabled=_BsRadiusDynAuthClientEnabled_Object((1,3,6,1,4,1,45,5,21,1,3,1,5),_BsRadiusDynAuthClientEnabled_Type())
bsRadiusDynAuthClientEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientEnabled.setStatus(_A)
class _BsRadiusDynAuthClientProcessDisconnectRequests_Type(TruthValue):defaultValue=2
_BsRadiusDynAuthClientProcessDisconnectRequests_Type.__name__=_G
_BsRadiusDynAuthClientProcessDisconnectRequests_Object=MibTableColumn
bsRadiusDynAuthClientProcessDisconnectRequests=_BsRadiusDynAuthClientProcessDisconnectRequests_Object((1,3,6,1,4,1,45,5,21,1,3,1,6),_BsRadiusDynAuthClientProcessDisconnectRequests_Type())
bsRadiusDynAuthClientProcessDisconnectRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientProcessDisconnectRequests.setStatus(_A)
class _BsRadiusDynAuthClientProcessCoARequests_Type(TruthValue):defaultValue=2
_BsRadiusDynAuthClientProcessCoARequests_Type.__name__=_G
_BsRadiusDynAuthClientProcessCoARequests_Object=MibTableColumn
bsRadiusDynAuthClientProcessCoARequests=_BsRadiusDynAuthClientProcessCoARequests_Object((1,3,6,1,4,1,45,5,21,1,3,1,7),_BsRadiusDynAuthClientProcessCoARequests_Type())
bsRadiusDynAuthClientProcessCoARequests.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientProcessCoARequests.setStatus(_A)
_BsRadiusDynAuthClientRowStatus_Type=RowStatus
_BsRadiusDynAuthClientRowStatus_Object=MibTableColumn
bsRadiusDynAuthClientRowStatus=_BsRadiusDynAuthClientRowStatus_Object((1,3,6,1,4,1,45,5,21,1,3,1,8),_BsRadiusDynAuthClientRowStatus_Type())
bsRadiusDynAuthClientRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientRowStatus.setStatus(_A)
_BsRadiusDynAuthClientReplayProtection_Type=TruthValue
_BsRadiusDynAuthClientReplayProtection_Object=MibTableColumn
bsRadiusDynAuthClientReplayProtection=_BsRadiusDynAuthClientReplayProtection_Object((1,3,6,1,4,1,45,5,21,1,3,1,9),_BsRadiusDynAuthClientReplayProtection_Type())
bsRadiusDynAuthClientReplayProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientReplayProtection.setStatus(_A)
class _BsRadiusDynAuthClientProcessReAuthRequests_Type(TruthValue):defaultValue=2
_BsRadiusDynAuthClientProcessReAuthRequests_Type.__name__=_G
_BsRadiusDynAuthClientProcessReAuthRequests_Object=MibTableColumn
bsRadiusDynAuthClientProcessReAuthRequests=_BsRadiusDynAuthClientProcessReAuthRequests_Object((1,3,6,1,4,1,45,5,21,1,3,1,10),_BsRadiusDynAuthClientProcessReAuthRequests_Type())
bsRadiusDynAuthClientProcessReAuthRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:bsRadiusDynAuthClientProcessReAuthRequests.setStatus(_A)
_BsRadiusExtDynAuthClientTable_Object=MibTable
bsRadiusExtDynAuthClientTable=_BsRadiusExtDynAuthClientTable_Object((1,3,6,1,4,1,45,5,21,1,4))
if mibBuilder.loadTexts:bsRadiusExtDynAuthClientTable.setStatus(_A)
_BsRadiusExtDynAuthClientEntry_Object=MibTableRow
bsRadiusExtDynAuthClientEntry=_BsRadiusExtDynAuthClientEntry_Object((1,3,6,1,4,1,45,5,21,1,4,1))
if mibBuilder.loadTexts:bsRadiusExtDynAuthClientEntry.setStatus(_A)
_BsRadiusExtDynAuthServRcRequests_Type=Counter32
_BsRadiusExtDynAuthServRcRequests_Object=MibTableColumn
bsRadiusExtDynAuthServRcRequests=_BsRadiusExtDynAuthServRcRequests_Object((1,3,6,1,4,1,45,5,21,1,4,1,1),_BsRadiusExtDynAuthServRcRequests_Type())
bsRadiusExtDynAuthServRcRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcRequests.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcRequests.setUnits(_F)
_BsRadiusExtDynAuthServRcAuthOnlyRequests_Type=Counter32
_BsRadiusExtDynAuthServRcAuthOnlyRequests_Object=MibTableColumn
bsRadiusExtDynAuthServRcAuthOnlyRequests=_BsRadiusExtDynAuthServRcAuthOnlyRequests_Object((1,3,6,1,4,1,45,5,21,1,4,1,2),_BsRadiusExtDynAuthServRcAuthOnlyRequests_Type())
bsRadiusExtDynAuthServRcAuthOnlyRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcAuthOnlyRequests.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcAuthOnlyRequests.setUnits(_F)
_BsRadiusExtDynAuthServRcDupRequests_Type=Counter32
_BsRadiusExtDynAuthServRcDupRequests_Object=MibTableColumn
bsRadiusExtDynAuthServRcDupRequests=_BsRadiusExtDynAuthServRcDupRequests_Object((1,3,6,1,4,1,45,5,21,1,4,1,3),_BsRadiusExtDynAuthServRcDupRequests_Type())
bsRadiusExtDynAuthServRcDupRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcDupRequests.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcDupRequests.setUnits(_F)
_BsRadiusExtDynAuthServRcAcks_Type=Counter32
_BsRadiusExtDynAuthServRcAcks_Object=MibTableColumn
bsRadiusExtDynAuthServRcAcks=_BsRadiusExtDynAuthServRcAcks_Object((1,3,6,1,4,1,45,5,21,1,4,1,4),_BsRadiusExtDynAuthServRcAcks_Type())
bsRadiusExtDynAuthServRcAcks.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcAcks.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcAcks.setUnits(_F)
_BsRadiusExtDynAuthServRcNacks_Type=Counter32
_BsRadiusExtDynAuthServRcNacks_Object=MibTableColumn
bsRadiusExtDynAuthServRcNacks=_BsRadiusExtDynAuthServRcNacks_Object((1,3,6,1,4,1,45,5,21,1,4,1,5),_BsRadiusExtDynAuthServRcNacks_Type())
bsRadiusExtDynAuthServRcNacks.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcNacks.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcNacks.setUnits(_F)
_BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Type=Counter32
_BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Object=MibTableColumn
bsRadiusExtDynAuthServRcNacksAuthOnlyRequests=_BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Object((1,3,6,1,4,1,45,5,21,1,4,1,6),_BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Type())
bsRadiusExtDynAuthServRcNacksAuthOnlyRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcNacksAuthOnlyRequests.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcNacksAuthOnlyRequests.setUnits(_F)
_BsRadiusExtDynAuthServRcNacksNoSess_Type=Counter32
_BsRadiusExtDynAuthServRcNacksNoSess_Object=MibTableColumn
bsRadiusExtDynAuthServRcNacksNoSess=_BsRadiusExtDynAuthServRcNacksNoSess_Object((1,3,6,1,4,1,45,5,21,1,4,1,7),_BsRadiusExtDynAuthServRcNacksNoSess_Type())
bsRadiusExtDynAuthServRcNacksNoSess.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcNacksNoSess.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcNacksNoSess.setUnits(_F)
_BsRadiusExtDynAuthServRcSessReauthenticated_Type=Counter32
_BsRadiusExtDynAuthServRcSessReauthenticated_Object=MibTableColumn
bsRadiusExtDynAuthServRcSessReauthenticated=_BsRadiusExtDynAuthServRcSessReauthenticated_Object((1,3,6,1,4,1,45,5,21,1,4,1,8),_BsRadiusExtDynAuthServRcSessReauthenticated_Type())
bsRadiusExtDynAuthServRcSessReauthenticated.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcSessReauthenticated.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcSessReauthenticated.setUnits(_F)
_BsRadiusExtDynAuthServRcMalformed_Type=Counter32
_BsRadiusExtDynAuthServRcMalformed_Object=MibTableColumn
bsRadiusExtDynAuthServRcMalformed=_BsRadiusExtDynAuthServRcMalformed_Object((1,3,6,1,4,1,45,5,21,1,4,1,9),_BsRadiusExtDynAuthServRcMalformed_Type())
bsRadiusExtDynAuthServRcMalformed.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcMalformed.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcMalformed.setUnits(_F)
_BsRadiusExtDynAuthServRcDropped_Type=Counter32
_BsRadiusExtDynAuthServRcDropped_Object=MibTableColumn
bsRadiusExtDynAuthServRcDropped=_BsRadiusExtDynAuthServRcDropped_Object((1,3,6,1,4,1,45,5,21,1,4,1,10),_BsRadiusExtDynAuthServRcDropped_Type())
bsRadiusExtDynAuthServRcDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcDropped.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcDropped.setUnits(_F)
_BsRadiusExtDynAuthServRcBadAuths_Type=Counter32
_BsRadiusExtDynAuthServRcBadAuths_Object=MibTableColumn
bsRadiusExtDynAuthServRcBadAuths=_BsRadiusExtDynAuthServRcBadAuths_Object((1,3,6,1,4,1,45,5,21,1,4,1,11),_BsRadiusExtDynAuthServRcBadAuths_Type())
bsRadiusExtDynAuthServRcBadAuths.setMaxAccess(_E)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcBadAuths.setStatus(_A)
if mibBuilder.loadTexts:bsRadiusExtDynAuthServRcBadAuths.setUnits(_F)
radiusDynAuthClientEntry.registerAugmentions((_H,_U))
bsRadiusExtDynAuthClientEntry.setIndexNames(*radiusDynAuthClientEntry.getIndexNames())
bsRadiusReachabilityServerDown=NotificationType((1,3,6,1,4,1,45,5,21,0,1))
bsRadiusReachabilityServerDown.setObjects(*((_H,_N),(_H,_O)))
if mibBuilder.loadTexts:bsRadiusReachabilityServerDown.setStatus(_A)
bsRadiusReachabilityServerUp=NotificationType((1,3,6,1,4,1,45,5,21,0,2))
bsRadiusReachabilityServerUp.setObjects(*((_H,_N),(_H,_O)))
if mibBuilder.loadTexts:bsRadiusReachabilityServerUp.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'bayStackRadiusMib':bayStackRadiusMib,'bsRadiusNotifications':bsRadiusNotifications,'bsRadiusReachabilityServerDown':bsRadiusReachabilityServerDown,'bsRadiusReachabilityServerUp':bsRadiusReachabilityServerUp,'bsRadiusObjects':bsRadiusObjects,'bsRadiusScalars':bsRadiusScalars,'bsRadiusUseMgmtIp':bsRadiusUseMgmtIp,'bsRadiusAccountingEnabled':bsRadiusAccountingEnabled,'bsRadiusPasswordFallbackEnabled':bsRadiusPasswordFallbackEnabled,'bsRadiusAccountingPort':bsRadiusAccountingPort,'bsRadiusAccountingInterimUpdates':bsRadiusAccountingInterimUpdates,'bsRadiusAccountingInterimUpdatesInterval':bsRadiusAccountingInterimUpdatesInterval,'bsRadiusAccountingInterimUpdatesIntervalSource':bsRadiusAccountingInterimUpdatesIntervalSource,'bsRadiusDynAuthReplayProtection':bsRadiusDynAuthReplayProtection,'bsRadiusReachability':bsRadiusReachability,'bsRadiusReachabilityUserName':bsRadiusReachabilityUserName,'bsRadiusReachabilityPassword':bsRadiusReachabilityPassword,'bsRadiusEncapsulationProtocol':bsRadiusEncapsulationProtocol,'bsRadiusReachabilityTimeout':bsRadiusReachabilityTimeout,'bsRadiusReachabilityRetry':bsRadiusReachabilityRetry,'bsRadiusReachabilityBadTimer':bsRadiusReachabilityBadTimer,'bsRadiusReachabilityGoodTimer':bsRadiusReachabilityGoodTimer,'bsRadiusServerTable':bsRadiusServerTable,'bsRadiusServerEntry':bsRadiusServerEntry,_R:bsRadiusServerIndex,'bsRadiusServerPriority':bsRadiusServerPriority,_N:bsRadiusServerAddressType,_O:bsRadiusServerAddress,'bsRadiusServerUdpPort':bsRadiusServerUdpPort,'bsRadiusServerTimeout':bsRadiusServerTimeout,'bsRadiusServerSecret':bsRadiusServerSecret,'bsRadiusServerRowStatus':bsRadiusServerRowStatus,'bsRadiusServerAccountingPort':bsRadiusServerAccountingPort,'bsRadiusServerAccountingEnabled':bsRadiusServerAccountingEnabled,'bsRadiusServerRetryLimit':bsRadiusServerRetryLimit,'bsRadiusDynAuthClientTable':bsRadiusDynAuthClientTable,'bsRadiusDynAuthClientEntry':bsRadiusDynAuthClientEntry,_S:bsRadiusDynAuthClientAddressType,_T:bsRadiusDynAuthClientAddress,'bsRadiusDynAuthClientUdpPort':bsRadiusDynAuthClientUdpPort,'bsRadiusDynAuthClientSecret':bsRadiusDynAuthClientSecret,'bsRadiusDynAuthClientEnabled':bsRadiusDynAuthClientEnabled,'bsRadiusDynAuthClientProcessDisconnectRequests':bsRadiusDynAuthClientProcessDisconnectRequests,'bsRadiusDynAuthClientProcessCoARequests':bsRadiusDynAuthClientProcessCoARequests,'bsRadiusDynAuthClientRowStatus':bsRadiusDynAuthClientRowStatus,'bsRadiusDynAuthClientReplayProtection':bsRadiusDynAuthClientReplayProtection,'bsRadiusDynAuthClientProcessReAuthRequests':bsRadiusDynAuthClientProcessReAuthRequests,'bsRadiusExtDynAuthClientTable':bsRadiusExtDynAuthClientTable,_U:bsRadiusExtDynAuthClientEntry,'bsRadiusExtDynAuthServRcRequests':bsRadiusExtDynAuthServRcRequests,'bsRadiusExtDynAuthServRcAuthOnlyRequests':bsRadiusExtDynAuthServRcAuthOnlyRequests,'bsRadiusExtDynAuthServRcDupRequests':bsRadiusExtDynAuthServRcDupRequests,'bsRadiusExtDynAuthServRcAcks':bsRadiusExtDynAuthServRcAcks,'bsRadiusExtDynAuthServRcNacks':bsRadiusExtDynAuthServRcNacks,'bsRadiusExtDynAuthServRcNacksAuthOnlyRequests':bsRadiusExtDynAuthServRcNacksAuthOnlyRequests,'bsRadiusExtDynAuthServRcNacksNoSess':bsRadiusExtDynAuthServRcNacksNoSess,'bsRadiusExtDynAuthServRcSessReauthenticated':bsRadiusExtDynAuthServRcSessReauthenticated,'bsRadiusExtDynAuthServRcMalformed':bsRadiusExtDynAuthServRcMalformed,'bsRadiusExtDynAuthServRcDropped':bsRadiusExtDynAuthServRcDropped,'bsRadiusExtDynAuthServRcBadAuths':bsRadiusExtDynAuthServRcBadAuths})