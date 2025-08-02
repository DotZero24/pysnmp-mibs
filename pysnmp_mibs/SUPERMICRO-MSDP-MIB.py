_e='fsMsdpRPOperStatus'
_d='fsMsdpPeerState'
_c='fsMsdpPeerFsmEstablishedTransitions'
_b='fsMsdpSARedistributionAddrType'
_a='fsMsdpPeerFilterAddrType'
_Z='fsMsdpRPAddrType'
_Y='fsMsdpMeshGroupPeerAddress'
_X='fsMsdpMeshGroupAddrType'
_W='fsMsdpMeshGroupName'
_V='fsMsdpSACacheOriginRP'
_U='fsMsdpSACacheSourceAddr'
_T='fsMsdpSACacheGroupAddr'
_S='fsMsdpSACacheAddrType'
_R='established'
_Q='fsMsdpPeerRemoteAddress'
_P='fsMsdpPeerAddrType'
_O='RowStatus'
_N='TimeTicks'
_M='seconds'
_L='fsMsdpRtrId'
_K='enabled'
_J='DisplayString'
_I='disabled'
_H='InetAddress'
_G='not-accessible'
_F='read-write'
_E='read-create'
_D='SUPERMICRO-MSDP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress',_O,'TextualConvention','TimeStamp')
fsMsdpMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,2,61))
if mibBuilder.loadTexts:fsMsdpMIB.setRevisions(('2012-09-05 00:00',))
_FsMsdp_ObjectIdentity=ObjectIdentity
fsMsdp=_FsMsdp_ObjectIdentity((1,3,6,1,4,1,10876,101,2,61,1))
_FsMsdpTraps_ObjectIdentity=ObjectIdentity
fsMsdpTraps=_FsMsdpTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,2,61,1,0))
class _FsMsdpTraceLevel_Type(Integer32):defaultValue=0
_FsMsdpTraceLevel_Type.__name__=_C
_FsMsdpTraceLevel_Object=MibScalar
fsMsdpTraceLevel=_FsMsdpTraceLevel_Object((1,3,6,1,4,1,10876,101,2,61,1,1),_FsMsdpTraceLevel_Type())
fsMsdpTraceLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpTraceLevel.setStatus(_A)
class _FsMsdpIPv4AdminStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_FsMsdpIPv4AdminStat_Type.__name__=_C
_FsMsdpIPv4AdminStat_Object=MibScalar
fsMsdpIPv4AdminStat=_FsMsdpIPv4AdminStat_Object((1,3,6,1,4,1,10876,101,2,61,1,2),_FsMsdpIPv4AdminStat_Type())
fsMsdpIPv4AdminStat.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpIPv4AdminStat.setStatus(_A)
class _FsMsdpIPv6AdminStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_FsMsdpIPv6AdminStat_Type.__name__=_C
_FsMsdpIPv6AdminStat_Object=MibScalar
fsMsdpIPv6AdminStat=_FsMsdpIPv6AdminStat_Object((1,3,6,1,4,1,10876,101,2,61,1,3),_FsMsdpIPv6AdminStat_Type())
fsMsdpIPv6AdminStat.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpIPv6AdminStat.setStatus(_A)
class _FsMsdpCacheLifetime_Type(TimeTicks):defaultValue=0
_FsMsdpCacheLifetime_Type.__name__=_N
_FsMsdpCacheLifetime_Object=MibScalar
fsMsdpCacheLifetime=_FsMsdpCacheLifetime_Object((1,3,6,1,4,1,10876,101,2,61,1,4),_FsMsdpCacheLifetime_Type())
fsMsdpCacheLifetime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpCacheLifetime.setStatus(_A)
_FsMsdpNumSACacheEntries_Type=Gauge32
_FsMsdpNumSACacheEntries_Object=MibScalar
fsMsdpNumSACacheEntries=_FsMsdpNumSACacheEntries_Object((1,3,6,1,4,1,10876,101,2,61,1,5),_FsMsdpNumSACacheEntries_Type())
fsMsdpNumSACacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpNumSACacheEntries.setStatus(_A)
class _FsMsdpMaxPeerSessions_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_FsMsdpMaxPeerSessions_Type.__name__=_C
_FsMsdpMaxPeerSessions_Object=MibScalar
fsMsdpMaxPeerSessions=_FsMsdpMaxPeerSessions_Object((1,3,6,1,4,1,10876,101,2,61,1,6),_FsMsdpMaxPeerSessions_Type())
fsMsdpMaxPeerSessions.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpMaxPeerSessions.setStatus(_A)
class _FsMsdpMappingComponentId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMsdpMappingComponentId_Type.__name__=_C
_FsMsdpMappingComponentId_Object=MibScalar
fsMsdpMappingComponentId=_FsMsdpMappingComponentId_Object((1,3,6,1,4,1,10876,101,2,61,1,7),_FsMsdpMappingComponentId_Type())
fsMsdpMappingComponentId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpMappingComponentId.setStatus(_A)
class _FsMsdpListenerPort_Type(Integer32):defaultValue=639;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(639,639),ValueRangeConstraint(1024,65535))
_FsMsdpListenerPort_Type.__name__=_C
_FsMsdpListenerPort_Object=MibScalar
fsMsdpListenerPort=_FsMsdpListenerPort_Object((1,3,6,1,4,1,10876,101,2,61,1,8),_FsMsdpListenerPort_Type())
fsMsdpListenerPort.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpListenerPort.setStatus(_A)
class _FsMsdpPeerFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('denyall',0),('acceptall',1)))
_FsMsdpPeerFilter_Type.__name__=_C
_FsMsdpPeerFilter_Object=MibScalar
fsMsdpPeerFilter=_FsMsdpPeerFilter_Object((1,3,6,1,4,1,10876,101,2,61,1,9),_FsMsdpPeerFilter_Type())
fsMsdpPeerFilter.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpPeerFilter.setStatus(_A)
_FsMsdpPeerCount_Type=Integer32
_FsMsdpPeerCount_Object=MibScalar
fsMsdpPeerCount=_FsMsdpPeerCount_Object((1,3,6,1,4,1,10876,101,2,61,1,10),_FsMsdpPeerCount_Type())
fsMsdpPeerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerCount.setStatus(_A)
_FsMsdpPeerTable_Object=MibTable
fsMsdpPeerTable=_FsMsdpPeerTable_Object((1,3,6,1,4,1,10876,101,2,61,1,11))
if mibBuilder.loadTexts:fsMsdpPeerTable.setStatus(_A)
_FsMsdpPeerEntry_Object=MibTableRow
fsMsdpPeerEntry=_FsMsdpPeerEntry_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1))
fsMsdpPeerEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:fsMsdpPeerEntry.setStatus(_A)
_FsMsdpPeerAddrType_Type=InetAddressType
_FsMsdpPeerAddrType_Object=MibTableColumn
fsMsdpPeerAddrType=_FsMsdpPeerAddrType_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,1),_FsMsdpPeerAddrType_Type())
fsMsdpPeerAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpPeerAddrType.setStatus(_A)
class _FsMsdpPeerRemoteAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpPeerRemoteAddress_Type.__name__=_H
_FsMsdpPeerRemoteAddress_Object=MibTableColumn
fsMsdpPeerRemoteAddress=_FsMsdpPeerRemoteAddress_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,2),_FsMsdpPeerRemoteAddress_Type())
fsMsdpPeerRemoteAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpPeerRemoteAddress.setStatus(_A)
class _FsMsdpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('listen',2),('connecting',3),(_R,4),(_I,5)))
_FsMsdpPeerState_Type.__name__=_C
_FsMsdpPeerState_Object=MibTableColumn
fsMsdpPeerState=_FsMsdpPeerState_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,3),_FsMsdpPeerState_Type())
fsMsdpPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerState.setStatus(_A)
_FsMsdpPeerRPFFailures_Type=Counter32
_FsMsdpPeerRPFFailures_Object=MibTableColumn
fsMsdpPeerRPFFailures=_FsMsdpPeerRPFFailures_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,4),_FsMsdpPeerRPFFailures_Type())
fsMsdpPeerRPFFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerRPFFailures.setStatus(_A)
_FsMsdpPeerInSAs_Type=Counter32
_FsMsdpPeerInSAs_Object=MibTableColumn
fsMsdpPeerInSAs=_FsMsdpPeerInSAs_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,5),_FsMsdpPeerInSAs_Type())
fsMsdpPeerInSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInSAs.setStatus(_A)
_FsMsdpPeerOutSAs_Type=Counter32
_FsMsdpPeerOutSAs_Object=MibTableColumn
fsMsdpPeerOutSAs=_FsMsdpPeerOutSAs_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,6),_FsMsdpPeerOutSAs_Type())
fsMsdpPeerOutSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerOutSAs.setStatus(_A)
_FsMsdpPeerInSARequests_Type=Counter32
_FsMsdpPeerInSARequests_Object=MibTableColumn
fsMsdpPeerInSARequests=_FsMsdpPeerInSARequests_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,7),_FsMsdpPeerInSARequests_Type())
fsMsdpPeerInSARequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInSARequests.setStatus(_A)
_FsMsdpPeerOutSARequests_Type=Counter32
_FsMsdpPeerOutSARequests_Object=MibTableColumn
fsMsdpPeerOutSARequests=_FsMsdpPeerOutSARequests_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,8),_FsMsdpPeerOutSARequests_Type())
fsMsdpPeerOutSARequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerOutSARequests.setStatus(_A)
_FsMsdpPeerInControlMessages_Type=Counter32
_FsMsdpPeerInControlMessages_Object=MibTableColumn
fsMsdpPeerInControlMessages=_FsMsdpPeerInControlMessages_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,9),_FsMsdpPeerInControlMessages_Type())
fsMsdpPeerInControlMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInControlMessages.setStatus(_A)
_FsMsdpPeerOutControlMessages_Type=Counter32
_FsMsdpPeerOutControlMessages_Object=MibTableColumn
fsMsdpPeerOutControlMessages=_FsMsdpPeerOutControlMessages_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,10),_FsMsdpPeerOutControlMessages_Type())
fsMsdpPeerOutControlMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerOutControlMessages.setStatus(_A)
_FsMsdpPeerInDataPackets_Type=Counter32
_FsMsdpPeerInDataPackets_Object=MibTableColumn
fsMsdpPeerInDataPackets=_FsMsdpPeerInDataPackets_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,11),_FsMsdpPeerInDataPackets_Type())
fsMsdpPeerInDataPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInDataPackets.setStatus(_A)
_FsMsdpPeerOutDataPackets_Type=Counter32
_FsMsdpPeerOutDataPackets_Object=MibTableColumn
fsMsdpPeerOutDataPackets=_FsMsdpPeerOutDataPackets_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,12),_FsMsdpPeerOutDataPackets_Type())
fsMsdpPeerOutDataPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerOutDataPackets.setStatus(_A)
_FsMsdpPeerFsmEstablishedTransitions_Type=Counter32
_FsMsdpPeerFsmEstablishedTransitions_Object=MibTableColumn
fsMsdpPeerFsmEstablishedTransitions=_FsMsdpPeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,13),_FsMsdpPeerFsmEstablishedTransitions_Type())
fsMsdpPeerFsmEstablishedTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerFsmEstablishedTransitions.setStatus(_A)
_FsMsdpPeerFsmEstablishedTime_Type=TimeStamp
_FsMsdpPeerFsmEstablishedTime_Object=MibTableColumn
fsMsdpPeerFsmEstablishedTime=_FsMsdpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,14),_FsMsdpPeerFsmEstablishedTime_Type())
fsMsdpPeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerFsmEstablishedTime.setStatus(_A)
_FsMsdpPeerInMessageTime_Type=TimeStamp
_FsMsdpPeerInMessageTime_Object=MibTableColumn
fsMsdpPeerInMessageTime=_FsMsdpPeerInMessageTime_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,15),_FsMsdpPeerInMessageTime_Type())
fsMsdpPeerInMessageTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInMessageTime.setStatus(_A)
class _FsMsdpPeerLocalAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpPeerLocalAddress_Type.__name__=_H
_FsMsdpPeerLocalAddress_Object=MibTableColumn
fsMsdpPeerLocalAddress=_FsMsdpPeerLocalAddress_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,16),_FsMsdpPeerLocalAddress_Type())
fsMsdpPeerLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerLocalAddress.setStatus(_A)
class _FsMsdpPeerConnectRetryInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMsdpPeerConnectRetryInterval_Type.__name__=_C
_FsMsdpPeerConnectRetryInterval_Object=MibTableColumn
fsMsdpPeerConnectRetryInterval=_FsMsdpPeerConnectRetryInterval_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,17),_FsMsdpPeerConnectRetryInterval_Type())
fsMsdpPeerConnectRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerConnectRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMsdpPeerConnectRetryInterval.setUnits(_M)
class _FsMsdpPeerHoldTimeConfigured_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_FsMsdpPeerHoldTimeConfigured_Type.__name__=_C
_FsMsdpPeerHoldTimeConfigured_Object=MibTableColumn
fsMsdpPeerHoldTimeConfigured=_FsMsdpPeerHoldTimeConfigured_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,18),_FsMsdpPeerHoldTimeConfigured_Type())
fsMsdpPeerHoldTimeConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerHoldTimeConfigured.setStatus(_A)
if mibBuilder.loadTexts:fsMsdpPeerHoldTimeConfigured.setUnits(_M)
class _FsMsdpPeerKeepAliveConfigured_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_FsMsdpPeerKeepAliveConfigured_Type.__name__=_C
_FsMsdpPeerKeepAliveConfigured_Object=MibTableColumn
fsMsdpPeerKeepAliveConfigured=_FsMsdpPeerKeepAliveConfigured_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,19),_FsMsdpPeerKeepAliveConfigured_Type())
fsMsdpPeerKeepAliveConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerKeepAliveConfigured.setStatus(_A)
if mibBuilder.loadTexts:fsMsdpPeerKeepAliveConfigured.setUnits(_M)
class _FsMsdpPeerDataTtl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMsdpPeerDataTtl_Type.__name__=_C
_FsMsdpPeerDataTtl_Object=MibTableColumn
fsMsdpPeerDataTtl=_FsMsdpPeerDataTtl_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,20),_FsMsdpPeerDataTtl_Type())
fsMsdpPeerDataTtl.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerDataTtl.setStatus(_A)
_FsMsdpPeerStatus_Type=RowStatus
_FsMsdpPeerStatus_Object=MibTableColumn
fsMsdpPeerStatus=_FsMsdpPeerStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,21),_FsMsdpPeerStatus_Type())
fsMsdpPeerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerStatus.setStatus(_A)
class _FsMsdpPeerRemotePort_Type(Integer32):defaultValue=639;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMsdpPeerRemotePort_Type.__name__=_C
_FsMsdpPeerRemotePort_Object=MibTableColumn
fsMsdpPeerRemotePort=_FsMsdpPeerRemotePort_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,22),_FsMsdpPeerRemotePort_Type())
fsMsdpPeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerRemotePort.setStatus(_A)
class _FsMsdpPeerLocalPort_Type(Integer32):defaultValue=639;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMsdpPeerLocalPort_Type.__name__=_C
_FsMsdpPeerLocalPort_Object=MibTableColumn
fsMsdpPeerLocalPort=_FsMsdpPeerLocalPort_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,23),_FsMsdpPeerLocalPort_Type())
fsMsdpPeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerLocalPort.setStatus(_A)
class _FsMsdpPeerEncapsulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('tcp',1)))
_FsMsdpPeerEncapsulationType_Type.__name__=_C
_FsMsdpPeerEncapsulationType_Object=MibTableColumn
fsMsdpPeerEncapsulationType=_FsMsdpPeerEncapsulationType_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,24),_FsMsdpPeerEncapsulationType_Type())
fsMsdpPeerEncapsulationType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerEncapsulationType.setStatus(_A)
_FsMsdpPeerConnectionAttempts_Type=Counter32
_FsMsdpPeerConnectionAttempts_Object=MibTableColumn
fsMsdpPeerConnectionAttempts=_FsMsdpPeerConnectionAttempts_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,25),_FsMsdpPeerConnectionAttempts_Type())
fsMsdpPeerConnectionAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerConnectionAttempts.setStatus(_A)
_FsMsdpPeerDiscontinuityTime_Type=TimeStamp
_FsMsdpPeerDiscontinuityTime_Object=MibTableColumn
fsMsdpPeerDiscontinuityTime=_FsMsdpPeerDiscontinuityTime_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,26),_FsMsdpPeerDiscontinuityTime_Type())
fsMsdpPeerDiscontinuityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerDiscontinuityTime.setStatus(_A)
class _FsMsdpPeerMD5AuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_FsMsdpPeerMD5AuthPassword_Type.__name__=_J
_FsMsdpPeerMD5AuthPassword_Object=MibTableColumn
fsMsdpPeerMD5AuthPassword=_FsMsdpPeerMD5AuthPassword_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,27),_FsMsdpPeerMD5AuthPassword_Type())
fsMsdpPeerMD5AuthPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpPeerMD5AuthPassword.setStatus(_A)
class _FsMsdpPeerMD5AuthPwdStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_FsMsdpPeerMD5AuthPwdStat_Type.__name__=_C
_FsMsdpPeerMD5AuthPwdStat_Object=MibTableColumn
fsMsdpPeerMD5AuthPwdStat=_FsMsdpPeerMD5AuthPwdStat_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,28),_FsMsdpPeerMD5AuthPwdStat_Type())
fsMsdpPeerMD5AuthPwdStat.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpPeerMD5AuthPwdStat.setStatus(_A)
_FsMsdpPeerMD5FailCount_Type=Integer32
_FsMsdpPeerMD5FailCount_Object=MibTableColumn
fsMsdpPeerMD5FailCount=_FsMsdpPeerMD5FailCount_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,29),_FsMsdpPeerMD5FailCount_Type())
fsMsdpPeerMD5FailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerMD5FailCount.setStatus(_A)
_FsMsdpPeerMD5SuccessCount_Type=Integer32
_FsMsdpPeerMD5SuccessCount_Object=MibTableColumn
fsMsdpPeerMD5SuccessCount=_FsMsdpPeerMD5SuccessCount_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,30),_FsMsdpPeerMD5SuccessCount_Type())
fsMsdpPeerMD5SuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerMD5SuccessCount.setStatus(_A)
_FsMsdpPeerInSAResponses_Type=Counter32
_FsMsdpPeerInSAResponses_Object=MibTableColumn
fsMsdpPeerInSAResponses=_FsMsdpPeerInSAResponses_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,31),_FsMsdpPeerInSAResponses_Type())
fsMsdpPeerInSAResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInSAResponses.setStatus(_A)
_FsMsdpPeerOutSAResponses_Type=Counter32
_FsMsdpPeerOutSAResponses_Object=MibTableColumn
fsMsdpPeerOutSAResponses=_FsMsdpPeerOutSAResponses_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,32),_FsMsdpPeerOutSAResponses_Type())
fsMsdpPeerOutSAResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerOutSAResponses.setStatus(_A)
_FsMsdpPeerUpTime_Type=TimeTicks
_FsMsdpPeerUpTime_Object=MibTableColumn
fsMsdpPeerUpTime=_FsMsdpPeerUpTime_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,33),_FsMsdpPeerUpTime_Type())
fsMsdpPeerUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerUpTime.setStatus(_A)
_FsMsdpPeerInKeepAliveCount_Type=Counter32
_FsMsdpPeerInKeepAliveCount_Object=MibTableColumn
fsMsdpPeerInKeepAliveCount=_FsMsdpPeerInKeepAliveCount_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,34),_FsMsdpPeerInKeepAliveCount_Type())
fsMsdpPeerInKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerInKeepAliveCount.setStatus(_A)
_FsMsdpPeerOutKeepAliveCount_Type=Counter32
_FsMsdpPeerOutKeepAliveCount_Object=MibTableColumn
fsMsdpPeerOutKeepAliveCount=_FsMsdpPeerOutKeepAliveCount_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,35),_FsMsdpPeerOutKeepAliveCount_Type())
fsMsdpPeerOutKeepAliveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerOutKeepAliveCount.setStatus(_A)
_FsMsdpPeerDataTtlErrorCount_Type=Counter32
_FsMsdpPeerDataTtlErrorCount_Object=MibTableColumn
fsMsdpPeerDataTtlErrorCount=_FsMsdpPeerDataTtlErrorCount_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,36),_FsMsdpPeerDataTtlErrorCount_Type())
fsMsdpPeerDataTtlErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpPeerDataTtlErrorCount.setStatus(_A)
class _FsMsdpPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_I,2)))
_FsMsdpPeerAdminStatus_Type.__name__=_C
_FsMsdpPeerAdminStatus_Object=MibTableColumn
fsMsdpPeerAdminStatus=_FsMsdpPeerAdminStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,11,1,37),_FsMsdpPeerAdminStatus_Type())
fsMsdpPeerAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpPeerAdminStatus.setStatus(_A)
_FsMsdpSACacheTable_Object=MibTable
fsMsdpSACacheTable=_FsMsdpSACacheTable_Object((1,3,6,1,4,1,10876,101,2,61,1,12))
if mibBuilder.loadTexts:fsMsdpSACacheTable.setStatus(_A)
_FsMsdpSACacheEntry_Object=MibTableRow
fsMsdpSACacheEntry=_FsMsdpSACacheEntry_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1))
fsMsdpSACacheEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:fsMsdpSACacheEntry.setStatus(_A)
_FsMsdpSACacheAddrType_Type=InetAddressType
_FsMsdpSACacheAddrType_Object=MibTableColumn
fsMsdpSACacheAddrType=_FsMsdpSACacheAddrType_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,1),_FsMsdpSACacheAddrType_Type())
fsMsdpSACacheAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpSACacheAddrType.setStatus(_A)
class _FsMsdpSACacheGroupAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpSACacheGroupAddr_Type.__name__=_H
_FsMsdpSACacheGroupAddr_Object=MibTableColumn
fsMsdpSACacheGroupAddr=_FsMsdpSACacheGroupAddr_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,2),_FsMsdpSACacheGroupAddr_Type())
fsMsdpSACacheGroupAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpSACacheGroupAddr.setStatus(_A)
class _FsMsdpSACacheSourceAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpSACacheSourceAddr_Type.__name__=_H
_FsMsdpSACacheSourceAddr_Object=MibTableColumn
fsMsdpSACacheSourceAddr=_FsMsdpSACacheSourceAddr_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,3),_FsMsdpSACacheSourceAddr_Type())
fsMsdpSACacheSourceAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpSACacheSourceAddr.setStatus(_A)
class _FsMsdpSACacheOriginRP_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpSACacheOriginRP_Type.__name__=_H
_FsMsdpSACacheOriginRP_Object=MibTableColumn
fsMsdpSACacheOriginRP=_FsMsdpSACacheOriginRP_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,4),_FsMsdpSACacheOriginRP_Type())
fsMsdpSACacheOriginRP.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpSACacheOriginRP.setStatus(_A)
class _FsMsdpSACachePeerLearnedFrom_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpSACachePeerLearnedFrom_Type.__name__=_H
_FsMsdpSACachePeerLearnedFrom_Object=MibTableColumn
fsMsdpSACachePeerLearnedFrom=_FsMsdpSACachePeerLearnedFrom_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,5),_FsMsdpSACachePeerLearnedFrom_Type())
fsMsdpSACachePeerLearnedFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpSACachePeerLearnedFrom.setStatus(_A)
class _FsMsdpSACacheRPFPeer_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpSACacheRPFPeer_Type.__name__=_H
_FsMsdpSACacheRPFPeer_Object=MibTableColumn
fsMsdpSACacheRPFPeer=_FsMsdpSACacheRPFPeer_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,6),_FsMsdpSACacheRPFPeer_Type())
fsMsdpSACacheRPFPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpSACacheRPFPeer.setStatus(_A)
_FsMsdpSACacheInSAs_Type=Counter32
_FsMsdpSACacheInSAs_Object=MibTableColumn
fsMsdpSACacheInSAs=_FsMsdpSACacheInSAs_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,7),_FsMsdpSACacheInSAs_Type())
fsMsdpSACacheInSAs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpSACacheInSAs.setStatus(_A)
_FsMsdpSACacheInDataPackets_Type=Counter32
_FsMsdpSACacheInDataPackets_Object=MibTableColumn
fsMsdpSACacheInDataPackets=_FsMsdpSACacheInDataPackets_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,8),_FsMsdpSACacheInDataPackets_Type())
fsMsdpSACacheInDataPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpSACacheInDataPackets.setStatus(_A)
_FsMsdpSACacheUpTime_Type=TimeTicks
_FsMsdpSACacheUpTime_Object=MibTableColumn
fsMsdpSACacheUpTime=_FsMsdpSACacheUpTime_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,9),_FsMsdpSACacheUpTime_Type())
fsMsdpSACacheUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpSACacheUpTime.setStatus(_A)
_FsMsdpSACacheExpiryTime_Type=TimeTicks
_FsMsdpSACacheExpiryTime_Object=MibTableColumn
fsMsdpSACacheExpiryTime=_FsMsdpSACacheExpiryTime_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,10),_FsMsdpSACacheExpiryTime_Type())
fsMsdpSACacheExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpSACacheExpiryTime.setStatus(_A)
class _FsMsdpSACacheStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*(('active',1),('destroy',6)))
_FsMsdpSACacheStatus_Type.__name__=_O
_FsMsdpSACacheStatus_Object=MibTableColumn
fsMsdpSACacheStatus=_FsMsdpSACacheStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,12,1,11),_FsMsdpSACacheStatus_Type())
fsMsdpSACacheStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMsdpSACacheStatus.setStatus(_A)
_FsMsdpMeshGroupTable_Object=MibTable
fsMsdpMeshGroupTable=_FsMsdpMeshGroupTable_Object((1,3,6,1,4,1,10876,101,2,61,1,13))
if mibBuilder.loadTexts:fsMsdpMeshGroupTable.setStatus(_A)
_FsMsdpMeshGroupEntry_Object=MibTableRow
fsMsdpMeshGroupEntry=_FsMsdpMeshGroupEntry_Object((1,3,6,1,4,1,10876,101,2,61,1,13,1))
fsMsdpMeshGroupEntry.setIndexNames((0,_D,_W),(0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:fsMsdpMeshGroupEntry.setStatus(_A)
class _FsMsdpMeshGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsMsdpMeshGroupName_Type.__name__=_J
_FsMsdpMeshGroupName_Object=MibTableColumn
fsMsdpMeshGroupName=_FsMsdpMeshGroupName_Object((1,3,6,1,4,1,10876,101,2,61,1,13,1,1),_FsMsdpMeshGroupName_Type())
fsMsdpMeshGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpMeshGroupName.setStatus(_A)
_FsMsdpMeshGroupAddrType_Type=InetAddressType
_FsMsdpMeshGroupAddrType_Object=MibTableColumn
fsMsdpMeshGroupAddrType=_FsMsdpMeshGroupAddrType_Object((1,3,6,1,4,1,10876,101,2,61,1,13,1,2),_FsMsdpMeshGroupAddrType_Type())
fsMsdpMeshGroupAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpMeshGroupAddrType.setStatus(_A)
class _FsMsdpMeshGroupPeerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpMeshGroupPeerAddress_Type.__name__=_H
_FsMsdpMeshGroupPeerAddress_Object=MibTableColumn
fsMsdpMeshGroupPeerAddress=_FsMsdpMeshGroupPeerAddress_Object((1,3,6,1,4,1,10876,101,2,61,1,13,1,3),_FsMsdpMeshGroupPeerAddress_Type())
fsMsdpMeshGroupPeerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpMeshGroupPeerAddress.setStatus(_A)
_FsMsdpMeshGroupStatus_Type=RowStatus
_FsMsdpMeshGroupStatus_Object=MibTableColumn
fsMsdpMeshGroupStatus=_FsMsdpMeshGroupStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,13,1,4),_FsMsdpMeshGroupStatus_Type())
fsMsdpMeshGroupStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpMeshGroupStatus.setStatus(_A)
_FsMsdpRPTable_Object=MibTable
fsMsdpRPTable=_FsMsdpRPTable_Object((1,3,6,1,4,1,10876,101,2,61,1,14))
if mibBuilder.loadTexts:fsMsdpRPTable.setStatus(_A)
_FsMsdpRPEntry_Object=MibTableRow
fsMsdpRPEntry=_FsMsdpRPEntry_Object((1,3,6,1,4,1,10876,101,2,61,1,14,1))
fsMsdpRPEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:fsMsdpRPEntry.setStatus(_A)
_FsMsdpRPAddrType_Type=InetAddressType
_FsMsdpRPAddrType_Object=MibTableColumn
fsMsdpRPAddrType=_FsMsdpRPAddrType_Object((1,3,6,1,4,1,10876,101,2,61,1,14,1,1),_FsMsdpRPAddrType_Type())
fsMsdpRPAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpRPAddrType.setStatus(_A)
class _FsMsdpRPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMsdpRPAddress_Type.__name__=_H
_FsMsdpRPAddress_Object=MibTableColumn
fsMsdpRPAddress=_FsMsdpRPAddress_Object((1,3,6,1,4,1,10876,101,2,61,1,14,1,2),_FsMsdpRPAddress_Type())
fsMsdpRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpRPAddress.setStatus(_A)
class _FsMsdpRPOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsMsdpRPOperStatus_Type.__name__=_C
_FsMsdpRPOperStatus_Object=MibTableColumn
fsMsdpRPOperStatus=_FsMsdpRPOperStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,14,1,3),_FsMsdpRPOperStatus_Type())
fsMsdpRPOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpRPOperStatus.setStatus(_A)
_FsMsdpRPStatus_Type=RowStatus
_FsMsdpRPStatus_Object=MibTableColumn
fsMsdpRPStatus=_FsMsdpRPStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,14,1,4),_FsMsdpRPStatus_Type())
fsMsdpRPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpRPStatus.setStatus(_A)
_FsMsdpPeerFilterTable_Object=MibTable
fsMsdpPeerFilterTable=_FsMsdpPeerFilterTable_Object((1,3,6,1,4,1,10876,101,2,61,1,15))
if mibBuilder.loadTexts:fsMsdpPeerFilterTable.setStatus(_A)
_FsMsdpPeerFilterEntry_Object=MibTableRow
fsMsdpPeerFilterEntry=_FsMsdpPeerFilterEntry_Object((1,3,6,1,4,1,10876,101,2,61,1,15,1))
fsMsdpPeerFilterEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:fsMsdpPeerFilterEntry.setStatus(_A)
_FsMsdpPeerFilterAddrType_Type=InetAddressType
_FsMsdpPeerFilterAddrType_Object=MibTableColumn
fsMsdpPeerFilterAddrType=_FsMsdpPeerFilterAddrType_Object((1,3,6,1,4,1,10876,101,2,61,1,15,1,1),_FsMsdpPeerFilterAddrType_Type())
fsMsdpPeerFilterAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpPeerFilterAddrType.setStatus(_A)
class _FsMsdpPeerFilterRouteMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsMsdpPeerFilterRouteMap_Type.__name__=_J
_FsMsdpPeerFilterRouteMap_Object=MibTableColumn
fsMsdpPeerFilterRouteMap=_FsMsdpPeerFilterRouteMap_Object((1,3,6,1,4,1,10876,101,2,61,1,15,1,2),_FsMsdpPeerFilterRouteMap_Type())
fsMsdpPeerFilterRouteMap.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerFilterRouteMap.setStatus(_A)
_FsMsdpPeerFilterStatus_Type=RowStatus
_FsMsdpPeerFilterStatus_Object=MibTableColumn
fsMsdpPeerFilterStatus=_FsMsdpPeerFilterStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,15,1,3),_FsMsdpPeerFilterStatus_Type())
fsMsdpPeerFilterStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpPeerFilterStatus.setStatus(_A)
_FsMsdpSARedistributionTable_Object=MibTable
fsMsdpSARedistributionTable=_FsMsdpSARedistributionTable_Object((1,3,6,1,4,1,10876,101,2,61,1,16))
if mibBuilder.loadTexts:fsMsdpSARedistributionTable.setStatus(_A)
_FsMsdpSARedistributionEntry_Object=MibTableRow
fsMsdpSARedistributionEntry=_FsMsdpSARedistributionEntry_Object((1,3,6,1,4,1,10876,101,2,61,1,16,1))
fsMsdpSARedistributionEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:fsMsdpSARedistributionEntry.setStatus(_A)
_FsMsdpSARedistributionAddrType_Type=InetAddressType
_FsMsdpSARedistributionAddrType_Object=MibTableColumn
fsMsdpSARedistributionAddrType=_FsMsdpSARedistributionAddrType_Object((1,3,6,1,4,1,10876,101,2,61,1,16,1,1),_FsMsdpSARedistributionAddrType_Type())
fsMsdpSARedistributionAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMsdpSARedistributionAddrType.setStatus(_A)
_FsMsdpSARedistributionStatus_Type=RowStatus
_FsMsdpSARedistributionStatus_Object=MibTableColumn
fsMsdpSARedistributionStatus=_FsMsdpSARedistributionStatus_Object((1,3,6,1,4,1,10876,101,2,61,1,16,1,2),_FsMsdpSARedistributionStatus_Type())
fsMsdpSARedistributionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpSARedistributionStatus.setStatus(_A)
class _FsMsdpSARedistributionRouteMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsMsdpSARedistributionRouteMap_Type.__name__=_J
_FsMsdpSARedistributionRouteMap_Object=MibTableColumn
fsMsdpSARedistributionRouteMap=_FsMsdpSARedistributionRouteMap_Object((1,3,6,1,4,1,10876,101,2,61,1,16,1,3),_FsMsdpSARedistributionRouteMap_Type())
fsMsdpSARedistributionRouteMap.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpSARedistributionRouteMap.setStatus(_A)
class _FsMsdpSARedistributionRouteMapStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_K,1)))
_FsMsdpSARedistributionRouteMapStat_Type.__name__=_C
_FsMsdpSARedistributionRouteMapStat_Object=MibTableColumn
fsMsdpSARedistributionRouteMapStat=_FsMsdpSARedistributionRouteMapStat_Object((1,3,6,1,4,1,10876,101,2,61,1,16,1,4),_FsMsdpSARedistributionRouteMapStat_Type())
fsMsdpSARedistributionRouteMapStat.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMsdpSARedistributionRouteMapStat.setStatus(_A)
_FsMsdpRtrId_Type=IpAddress
_FsMsdpRtrId_Object=MibScalar
fsMsdpRtrId=_FsMsdpRtrId_Object((1,3,6,1,4,1,10876,101,2,61,1,17),_FsMsdpRtrId_Type())
fsMsdpRtrId.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fsMsdpRtrId.setStatus(_A)
_FsMsdpStat_ObjectIdentity=ObjectIdentity
fsMsdpStat=_FsMsdpStat_ObjectIdentity((1,3,6,1,4,1,10876,101,2,61,2))
_FsMsdpStatEstPeerCount_Type=Integer32
_FsMsdpStatEstPeerCount_Object=MibScalar
fsMsdpStatEstPeerCount=_FsMsdpStatEstPeerCount_Object((1,3,6,1,4,1,10876,101,2,61,2,1),_FsMsdpStatEstPeerCount_Type())
fsMsdpStatEstPeerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMsdpStatEstPeerCount.setStatus(_A)
fsMsdpEstablished=NotificationType((1,3,6,1,4,1,10876,101,2,61,1,0,1))
fsMsdpEstablished.setObjects(*((_D,_L),(_D,_c)))
if mibBuilder.loadTexts:fsMsdpEstablished.setStatus(_A)
fsMsdpBackwardTransition=NotificationType((1,3,6,1,4,1,10876,101,2,61,1,0,2))
fsMsdpBackwardTransition.setObjects(*((_D,_L),(_D,_d)))
if mibBuilder.loadTexts:fsMsdpBackwardTransition.setStatus(_A)
fsMsdpRPOperStatusChange=NotificationType((1,3,6,1,4,1,10876,101,2,61,1,0,3))
fsMsdpRPOperStatusChange.setObjects(*((_D,_L),(_D,_e)))
if mibBuilder.loadTexts:fsMsdpRPOperStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsMsdpMIB':fsMsdpMIB,'fsMsdp':fsMsdp,'fsMsdpTraps':fsMsdpTraps,'fsMsdpEstablished':fsMsdpEstablished,'fsMsdpBackwardTransition':fsMsdpBackwardTransition,'fsMsdpRPOperStatusChange':fsMsdpRPOperStatusChange,'fsMsdpTraceLevel':fsMsdpTraceLevel,'fsMsdpIPv4AdminStat':fsMsdpIPv4AdminStat,'fsMsdpIPv6AdminStat':fsMsdpIPv6AdminStat,'fsMsdpCacheLifetime':fsMsdpCacheLifetime,'fsMsdpNumSACacheEntries':fsMsdpNumSACacheEntries,'fsMsdpMaxPeerSessions':fsMsdpMaxPeerSessions,'fsMsdpMappingComponentId':fsMsdpMappingComponentId,'fsMsdpListenerPort':fsMsdpListenerPort,'fsMsdpPeerFilter':fsMsdpPeerFilter,'fsMsdpPeerCount':fsMsdpPeerCount,'fsMsdpPeerTable':fsMsdpPeerTable,'fsMsdpPeerEntry':fsMsdpPeerEntry,_P:fsMsdpPeerAddrType,_Q:fsMsdpPeerRemoteAddress,_d:fsMsdpPeerState,'fsMsdpPeerRPFFailures':fsMsdpPeerRPFFailures,'fsMsdpPeerInSAs':fsMsdpPeerInSAs,'fsMsdpPeerOutSAs':fsMsdpPeerOutSAs,'fsMsdpPeerInSARequests':fsMsdpPeerInSARequests,'fsMsdpPeerOutSARequests':fsMsdpPeerOutSARequests,'fsMsdpPeerInControlMessages':fsMsdpPeerInControlMessages,'fsMsdpPeerOutControlMessages':fsMsdpPeerOutControlMessages,'fsMsdpPeerInDataPackets':fsMsdpPeerInDataPackets,'fsMsdpPeerOutDataPackets':fsMsdpPeerOutDataPackets,_c:fsMsdpPeerFsmEstablishedTransitions,'fsMsdpPeerFsmEstablishedTime':fsMsdpPeerFsmEstablishedTime,'fsMsdpPeerInMessageTime':fsMsdpPeerInMessageTime,'fsMsdpPeerLocalAddress':fsMsdpPeerLocalAddress,'fsMsdpPeerConnectRetryInterval':fsMsdpPeerConnectRetryInterval,'fsMsdpPeerHoldTimeConfigured':fsMsdpPeerHoldTimeConfigured,'fsMsdpPeerKeepAliveConfigured':fsMsdpPeerKeepAliveConfigured,'fsMsdpPeerDataTtl':fsMsdpPeerDataTtl,'fsMsdpPeerStatus':fsMsdpPeerStatus,'fsMsdpPeerRemotePort':fsMsdpPeerRemotePort,'fsMsdpPeerLocalPort':fsMsdpPeerLocalPort,'fsMsdpPeerEncapsulationType':fsMsdpPeerEncapsulationType,'fsMsdpPeerConnectionAttempts':fsMsdpPeerConnectionAttempts,'fsMsdpPeerDiscontinuityTime':fsMsdpPeerDiscontinuityTime,'fsMsdpPeerMD5AuthPassword':fsMsdpPeerMD5AuthPassword,'fsMsdpPeerMD5AuthPwdStat':fsMsdpPeerMD5AuthPwdStat,'fsMsdpPeerMD5FailCount':fsMsdpPeerMD5FailCount,'fsMsdpPeerMD5SuccessCount':fsMsdpPeerMD5SuccessCount,'fsMsdpPeerInSAResponses':fsMsdpPeerInSAResponses,'fsMsdpPeerOutSAResponses':fsMsdpPeerOutSAResponses,'fsMsdpPeerUpTime':fsMsdpPeerUpTime,'fsMsdpPeerInKeepAliveCount':fsMsdpPeerInKeepAliveCount,'fsMsdpPeerOutKeepAliveCount':fsMsdpPeerOutKeepAliveCount,'fsMsdpPeerDataTtlErrorCount':fsMsdpPeerDataTtlErrorCount,'fsMsdpPeerAdminStatus':fsMsdpPeerAdminStatus,'fsMsdpSACacheTable':fsMsdpSACacheTable,'fsMsdpSACacheEntry':fsMsdpSACacheEntry,_S:fsMsdpSACacheAddrType,_T:fsMsdpSACacheGroupAddr,_U:fsMsdpSACacheSourceAddr,_V:fsMsdpSACacheOriginRP,'fsMsdpSACachePeerLearnedFrom':fsMsdpSACachePeerLearnedFrom,'fsMsdpSACacheRPFPeer':fsMsdpSACacheRPFPeer,'fsMsdpSACacheInSAs':fsMsdpSACacheInSAs,'fsMsdpSACacheInDataPackets':fsMsdpSACacheInDataPackets,'fsMsdpSACacheUpTime':fsMsdpSACacheUpTime,'fsMsdpSACacheExpiryTime':fsMsdpSACacheExpiryTime,'fsMsdpSACacheStatus':fsMsdpSACacheStatus,'fsMsdpMeshGroupTable':fsMsdpMeshGroupTable,'fsMsdpMeshGroupEntry':fsMsdpMeshGroupEntry,_W:fsMsdpMeshGroupName,_X:fsMsdpMeshGroupAddrType,_Y:fsMsdpMeshGroupPeerAddress,'fsMsdpMeshGroupStatus':fsMsdpMeshGroupStatus,'fsMsdpRPTable':fsMsdpRPTable,'fsMsdpRPEntry':fsMsdpRPEntry,_Z:fsMsdpRPAddrType,'fsMsdpRPAddress':fsMsdpRPAddress,_e:fsMsdpRPOperStatus,'fsMsdpRPStatus':fsMsdpRPStatus,'fsMsdpPeerFilterTable':fsMsdpPeerFilterTable,'fsMsdpPeerFilterEntry':fsMsdpPeerFilterEntry,_a:fsMsdpPeerFilterAddrType,'fsMsdpPeerFilterRouteMap':fsMsdpPeerFilterRouteMap,'fsMsdpPeerFilterStatus':fsMsdpPeerFilterStatus,'fsMsdpSARedistributionTable':fsMsdpSARedistributionTable,'fsMsdpSARedistributionEntry':fsMsdpSARedistributionEntry,_b:fsMsdpSARedistributionAddrType,'fsMsdpSARedistributionStatus':fsMsdpSARedistributionStatus,'fsMsdpSARedistributionRouteMap':fsMsdpSARedistributionRouteMap,'fsMsdpSARedistributionRouteMapStat':fsMsdpSARedistributionRouteMapStat,_L:fsMsdpRtrId,'fsMsdpStat':fsMsdpStat,'fsMsdpStatEstPeerCount':fsMsdpStatEstPeerCount})