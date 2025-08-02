_AB='etsysSntpClientUnicastAuthenticationGroup'
_AA='etsysSntpClientAnycastGroup'
_A9='etsysSntpClientBroadcastGroup'
_A8='etsysSntpClientMulticastGroup'
_A7='etsysSntpClientUnicastGroup'
_A6='etsysSntpClientDeviceGroup'
_A5='etsysSntpClientUAuthKeyStatus'
_A4='etsysSntpClientUKeyTrusted'
_A3='etsysSntpClientUAuthValue'
_A2='etsysSntpClientUAuthType'
_A1='etsysSntpClientUServerAuthKey'
_A0='etsysSntpClientMaxAuthenticationKeys'
_z='etsysSntpClientAuthenticationEnable'
_y='etsysSntpClientAnycastNumPollRequests'
_x='etsysSntpClientAnycastNumRequests'
_w='etsysSntpClientAnycastServerAddr'
_v='etsysSntpClientAnycastServerAddrType'
_u='etsysSntpClientAnycastPollRetry'
_t='etsysSntpClientAnycastPollTimeout'
_s='etsysSntpClientAnycastPollInterval'
_r='etsysSntpClientAnycastBindRequestInterval'
_q='etsysSntpClientBroadcastCount'
_p='etsysSntpClientBroadcastDelay'
_o='etsysSntpClientMulticastCount'
_n='etsysSntpClientMulticastDelay'
_m='etsysSntpClientUServerStatus'
_l='etsysSntpClientUServerNumFailedRequests'
_k='etsysSntpClientUServerNumRequests'
_j='etsysSntpClientUServerLastAttemptStatus'
_i='etsysSntpClientUServerLastAttemptTime'
_h='etsysSntpClientUServerLastUpdateTime'
_g='etsysSntpClientUServerPrecedence'
_f='etsysSntpClientUServerCurrEntries'
_e='etsysSntpClientUServerMaxEntries'
_d='etsysSntpClientUnicastPollRetry'
_c='etsysSntpClientUnicastPollTimeout'
_b='etsysSntpClientUnicastPollInterval'
_a='etsysSntpClientLastAttemptStatus'
_Z='etsysSntpClientLastAttemptTime'
_Y='etsysSntpClientLastUpdateTime'
_X='etsysSntpClientMode'
_W='etsysSntpClientSupportedMode'
_V='etsysSntpClientVersion'
_U='microseconds'
_T='etsysSntpClientUServerAddr'
_S='etsysSntpClientUServerAddrType'
_R='SntpClientOperModes'
_Q='RowStatus'
_P='Gauge32'
_O='OctetString'
_N='etsysSntpClientUAuthKey'
_M='not-accessible'
_L='SntpClientUpdateStatus'
_K='TruthValue'
_J='Integer32'
_I='InetAddress'
_H='seconds'
_G='DateAndTime'
_F='read-create'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='ENTERASYS-SNTP-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_P,_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'DisplayString','PhysAddress',_Q,'TextualConvention',_K)
etsysSntpClientMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,38))
if mibBuilder.loadTexts:etsysSntpClientMIB.setRevisions(('2011-03-09 15:56','2003-06-13 18:09'))
class SntpClientOperModes(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('disabled',0),('unicast',1),('multicast',2),('broadcast',3),('anycast',4)))
class SntpClientUpdateStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('success',2),('requestTimedOut',3),('badDateEncoded',4),('versionNotSupported',5),('serverUnsychronized',6)))
_EtsysSntpClientObjects_ObjectIdentity=ObjectIdentity
etsysSntpClientObjects=_EtsysSntpClientObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,1))
_EtsysSntpClientDevice_ObjectIdentity=ObjectIdentity
etsysSntpClientDevice=_EtsysSntpClientDevice_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,1,1))
class _EtsysSntpClientVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('version1',1),('version2',2),('version3',3),('version4',4)))
_EtsysSntpClientVersion_Type.__name__=_J
_EtsysSntpClientVersion_Object=MibScalar
etsysSntpClientVersion=_EtsysSntpClientVersion_Object((1,3,6,1,4,1,5624,1,2,38,1,1,1),_EtsysSntpClientVersion_Type())
etsysSntpClientVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientVersion.setStatus(_A)
_EtsysSntpClientSupportedMode_Type=SntpClientOperModes
_EtsysSntpClientSupportedMode_Object=MibScalar
etsysSntpClientSupportedMode=_EtsysSntpClientSupportedMode_Object((1,3,6,1,4,1,5624,1,2,38,1,1,2),_EtsysSntpClientSupportedMode_Type())
etsysSntpClientSupportedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientSupportedMode.setStatus(_A)
class _EtsysSntpClientMode_Type(SntpClientOperModes):defaultBinValue='1'
_EtsysSntpClientMode_Type.__name__=_R
_EtsysSntpClientMode_Object=MibScalar
etsysSntpClientMode=_EtsysSntpClientMode_Object((1,3,6,1,4,1,5624,1,2,38,1,1,3),_EtsysSntpClientMode_Type())
etsysSntpClientMode.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientMode.setStatus(_A)
class _EtsysSntpClientLastUpdateTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtsysSntpClientLastUpdateTime_Type.__name__=_G
_EtsysSntpClientLastUpdateTime_Object=MibScalar
etsysSntpClientLastUpdateTime=_EtsysSntpClientLastUpdateTime_Object((1,3,6,1,4,1,5624,1,2,38,1,1,4),_EtsysSntpClientLastUpdateTime_Type())
etsysSntpClientLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientLastUpdateTime.setStatus(_A)
class _EtsysSntpClientLastAttemptTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtsysSntpClientLastAttemptTime_Type.__name__=_G
_EtsysSntpClientLastAttemptTime_Object=MibScalar
etsysSntpClientLastAttemptTime=_EtsysSntpClientLastAttemptTime_Object((1,3,6,1,4,1,5624,1,2,38,1,1,5),_EtsysSntpClientLastAttemptTime_Type())
etsysSntpClientLastAttemptTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientLastAttemptTime.setStatus(_A)
class _EtsysSntpClientLastAttemptStatus_Type(SntpClientUpdateStatus):defaultValue=1
_EtsysSntpClientLastAttemptStatus_Type.__name__=_L
_EtsysSntpClientLastAttemptStatus_Object=MibScalar
etsysSntpClientLastAttemptStatus=_EtsysSntpClientLastAttemptStatus_Object((1,3,6,1,4,1,5624,1,2,38,1,1,6),_EtsysSntpClientLastAttemptStatus_Type())
etsysSntpClientLastAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientLastAttemptStatus.setStatus(_A)
class _EtsysSntpClientAuthenticationEnable_Type(TruthValue):defaultValue=2
_EtsysSntpClientAuthenticationEnable_Type.__name__=_K
_EtsysSntpClientAuthenticationEnable_Object=MibScalar
etsysSntpClientAuthenticationEnable=_EtsysSntpClientAuthenticationEnable_Object((1,3,6,1,4,1,5624,1,2,38,1,1,7),_EtsysSntpClientAuthenticationEnable_Type())
etsysSntpClientAuthenticationEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientAuthenticationEnable.setStatus(_A)
_EtsysSntpClientMaxAuthenticationKeys_Type=Unsigned32
_EtsysSntpClientMaxAuthenticationKeys_Object=MibScalar
etsysSntpClientMaxAuthenticationKeys=_EtsysSntpClientMaxAuthenticationKeys_Object((1,3,6,1,4,1,5624,1,2,38,1,1,8),_EtsysSntpClientMaxAuthenticationKeys_Type())
etsysSntpClientMaxAuthenticationKeys.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientMaxAuthenticationKeys.setStatus(_A)
_EtsysSntpClientUnicast_ObjectIdentity=ObjectIdentity
etsysSntpClientUnicast=_EtsysSntpClientUnicast_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,1,2))
class _EtsysSntpClientUnicastPollInterval_Type(Unsigned32):defaultValue=512;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16284))
_EtsysSntpClientUnicastPollInterval_Type.__name__=_D
_EtsysSntpClientUnicastPollInterval_Object=MibScalar
etsysSntpClientUnicastPollInterval=_EtsysSntpClientUnicastPollInterval_Object((1,3,6,1,4,1,5624,1,2,38,1,2,1),_EtsysSntpClientUnicastPollInterval_Type())
etsysSntpClientUnicastPollInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientUnicastPollInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientUnicastPollInterval.setUnits(_H)
class _EtsysSntpClientUnicastPollTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_EtsysSntpClientUnicastPollTimeout_Type.__name__=_D
_EtsysSntpClientUnicastPollTimeout_Object=MibScalar
etsysSntpClientUnicastPollTimeout=_EtsysSntpClientUnicastPollTimeout_Object((1,3,6,1,4,1,5624,1,2,38,1,2,2),_EtsysSntpClientUnicastPollTimeout_Type())
etsysSntpClientUnicastPollTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientUnicastPollTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientUnicastPollTimeout.setUnits(_H)
class _EtsysSntpClientUnicastPollRetry_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EtsysSntpClientUnicastPollRetry_Type.__name__=_D
_EtsysSntpClientUnicastPollRetry_Object=MibScalar
etsysSntpClientUnicastPollRetry=_EtsysSntpClientUnicastPollRetry_Object((1,3,6,1,4,1,5624,1,2,38,1,2,3),_EtsysSntpClientUnicastPollRetry_Type())
etsysSntpClientUnicastPollRetry.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientUnicastPollRetry.setStatus(_A)
class _EtsysSntpClientUServerMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EtsysSntpClientUServerMaxEntries_Type.__name__=_D
_EtsysSntpClientUServerMaxEntries_Object=MibScalar
etsysSntpClientUServerMaxEntries=_EtsysSntpClientUServerMaxEntries_Object((1,3,6,1,4,1,5624,1,2,38,1,2,4),_EtsysSntpClientUServerMaxEntries_Type())
etsysSntpClientUServerMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerMaxEntries.setStatus(_A)
class _EtsysSntpClientUServerCurrEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EtsysSntpClientUServerCurrEntries_Type.__name__=_P
_EtsysSntpClientUServerCurrEntries_Object=MibScalar
etsysSntpClientUServerCurrEntries=_EtsysSntpClientUServerCurrEntries_Object((1,3,6,1,4,1,5624,1,2,38,1,2,5),_EtsysSntpClientUServerCurrEntries_Type())
etsysSntpClientUServerCurrEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerCurrEntries.setStatus(_A)
_EtsysSntpClientUServerTable_Object=MibTable
etsysSntpClientUServerTable=_EtsysSntpClientUServerTable_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6))
if mibBuilder.loadTexts:etsysSntpClientUServerTable.setStatus(_A)
_EtsysSntpClientUServerEntry_Object=MibTableRow
etsysSntpClientUServerEntry=_EtsysSntpClientUServerEntry_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1))
etsysSntpClientUServerEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:etsysSntpClientUServerEntry.setStatus(_A)
_EtsysSntpClientUServerAddrType_Type=InetAddressType
_EtsysSntpClientUServerAddrType_Object=MibTableColumn
etsysSntpClientUServerAddrType=_EtsysSntpClientUServerAddrType_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,1),_EtsysSntpClientUServerAddrType_Type())
etsysSntpClientUServerAddrType.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysSntpClientUServerAddrType.setStatus(_A)
class _EtsysSntpClientUServerAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysSntpClientUServerAddr_Type.__name__=_I
_EtsysSntpClientUServerAddr_Object=MibTableColumn
etsysSntpClientUServerAddr=_EtsysSntpClientUServerAddr_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,2),_EtsysSntpClientUServerAddr_Type())
etsysSntpClientUServerAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysSntpClientUServerAddr.setStatus(_A)
class _EtsysSntpClientUServerPrecedence_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EtsysSntpClientUServerPrecedence_Type.__name__=_D
_EtsysSntpClientUServerPrecedence_Object=MibTableColumn
etsysSntpClientUServerPrecedence=_EtsysSntpClientUServerPrecedence_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,3),_EtsysSntpClientUServerPrecedence_Type())
etsysSntpClientUServerPrecedence.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUServerPrecedence.setStatus(_A)
class _EtsysSntpClientUServerLastUpdateTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtsysSntpClientUServerLastUpdateTime_Type.__name__=_G
_EtsysSntpClientUServerLastUpdateTime_Object=MibTableColumn
etsysSntpClientUServerLastUpdateTime=_EtsysSntpClientUServerLastUpdateTime_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,4),_EtsysSntpClientUServerLastUpdateTime_Type())
etsysSntpClientUServerLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerLastUpdateTime.setStatus(_A)
class _EtsysSntpClientUServerLastAttemptTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtsysSntpClientUServerLastAttemptTime_Type.__name__=_G
_EtsysSntpClientUServerLastAttemptTime_Object=MibTableColumn
etsysSntpClientUServerLastAttemptTime=_EtsysSntpClientUServerLastAttemptTime_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,5),_EtsysSntpClientUServerLastAttemptTime_Type())
etsysSntpClientUServerLastAttemptTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerLastAttemptTime.setStatus(_A)
class _EtsysSntpClientUServerLastAttemptStatus_Type(SntpClientUpdateStatus):defaultValue=1
_EtsysSntpClientUServerLastAttemptStatus_Type.__name__=_L
_EtsysSntpClientUServerLastAttemptStatus_Object=MibTableColumn
etsysSntpClientUServerLastAttemptStatus=_EtsysSntpClientUServerLastAttemptStatus_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,6),_EtsysSntpClientUServerLastAttemptStatus_Type())
etsysSntpClientUServerLastAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerLastAttemptStatus.setStatus(_A)
_EtsysSntpClientUServerNumRequests_Type=Counter32
_EtsysSntpClientUServerNumRequests_Object=MibTableColumn
etsysSntpClientUServerNumRequests=_EtsysSntpClientUServerNumRequests_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,7),_EtsysSntpClientUServerNumRequests_Type())
etsysSntpClientUServerNumRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerNumRequests.setStatus(_A)
_EtsysSntpClientUServerNumFailedRequests_Type=Counter32
_EtsysSntpClientUServerNumFailedRequests_Object=MibTableColumn
etsysSntpClientUServerNumFailedRequests=_EtsysSntpClientUServerNumFailedRequests_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,8),_EtsysSntpClientUServerNumFailedRequests_Type())
etsysSntpClientUServerNumFailedRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientUServerNumFailedRequests.setStatus(_A)
_EtsysSntpClientUServerStatus_Type=RowStatus
_EtsysSntpClientUServerStatus_Object=MibTableColumn
etsysSntpClientUServerStatus=_EtsysSntpClientUServerStatus_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,9),_EtsysSntpClientUServerStatus_Type())
etsysSntpClientUServerStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUServerStatus.setStatus(_A)
class _EtsysSntpClientUServerAuthKey_Type(Unsigned32):defaultValue=0
_EtsysSntpClientUServerAuthKey_Type.__name__=_D
_EtsysSntpClientUServerAuthKey_Object=MibTableColumn
etsysSntpClientUServerAuthKey=_EtsysSntpClientUServerAuthKey_Object((1,3,6,1,4,1,5624,1,2,38,1,2,6,1,10),_EtsysSntpClientUServerAuthKey_Type())
etsysSntpClientUServerAuthKey.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUServerAuthKey.setStatus(_A)
_EtsysSntpClientUAuthKeyTable_Object=MibTable
etsysSntpClientUAuthKeyTable=_EtsysSntpClientUAuthKeyTable_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7))
if mibBuilder.loadTexts:etsysSntpClientUAuthKeyTable.setStatus(_A)
_EtsysSntpClientUAuthKeyEntry_Object=MibTableRow
etsysSntpClientUAuthKeyEntry=_EtsysSntpClientUAuthKeyEntry_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7,1))
etsysSntpClientUAuthKeyEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:etsysSntpClientUAuthKeyEntry.setStatus(_A)
_EtsysSntpClientUAuthKey_Type=Unsigned32
_EtsysSntpClientUAuthKey_Object=MibTableColumn
etsysSntpClientUAuthKey=_EtsysSntpClientUAuthKey_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7,1,1),_EtsysSntpClientUAuthKey_Type())
etsysSntpClientUAuthKey.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysSntpClientUAuthKey.setStatus(_A)
class _EtsysSntpClientUAuthType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('md5',1),('sha-1',2)))
_EtsysSntpClientUAuthType_Type.__name__=_J
_EtsysSntpClientUAuthType_Object=MibTableColumn
etsysSntpClientUAuthType=_EtsysSntpClientUAuthType_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7,1,2),_EtsysSntpClientUAuthType_Type())
etsysSntpClientUAuthType.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUAuthType.setStatus(_A)
class _EtsysSntpClientUAuthValue_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysSntpClientUAuthValue_Type.__name__=_O
_EtsysSntpClientUAuthValue_Object=MibTableColumn
etsysSntpClientUAuthValue=_EtsysSntpClientUAuthValue_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7,1,3),_EtsysSntpClientUAuthValue_Type())
etsysSntpClientUAuthValue.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUAuthValue.setStatus(_A)
class _EtsysSntpClientUKeyTrusted_Type(TruthValue):defaultValue=2
_EtsysSntpClientUKeyTrusted_Type.__name__=_K
_EtsysSntpClientUKeyTrusted_Object=MibTableColumn
etsysSntpClientUKeyTrusted=_EtsysSntpClientUKeyTrusted_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7,1,4),_EtsysSntpClientUKeyTrusted_Type())
etsysSntpClientUKeyTrusted.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUKeyTrusted.setStatus(_A)
class _EtsysSntpClientUAuthKeyStatus_Type(RowStatus):defaultValue=4
_EtsysSntpClientUAuthKeyStatus_Type.__name__=_Q
_EtsysSntpClientUAuthKeyStatus_Object=MibTableColumn
etsysSntpClientUAuthKeyStatus=_EtsysSntpClientUAuthKeyStatus_Object((1,3,6,1,4,1,5624,1,2,38,1,2,7,1,5),_EtsysSntpClientUAuthKeyStatus_Type())
etsysSntpClientUAuthKeyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysSntpClientUAuthKeyStatus.setStatus(_A)
_EtsysSntpClientMulticast_ObjectIdentity=ObjectIdentity
etsysSntpClientMulticast=_EtsysSntpClientMulticast_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,1,3))
class _EtsysSntpClientMulticastDelay_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999))
_EtsysSntpClientMulticastDelay_Type.__name__=_D
_EtsysSntpClientMulticastDelay_Object=MibScalar
etsysSntpClientMulticastDelay=_EtsysSntpClientMulticastDelay_Object((1,3,6,1,4,1,5624,1,2,38,1,3,1),_EtsysSntpClientMulticastDelay_Type())
etsysSntpClientMulticastDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientMulticastDelay.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientMulticastDelay.setUnits(_U)
_EtsysSntpClientMulticastCount_Type=Counter32
_EtsysSntpClientMulticastCount_Object=MibScalar
etsysSntpClientMulticastCount=_EtsysSntpClientMulticastCount_Object((1,3,6,1,4,1,5624,1,2,38,1,3,2),_EtsysSntpClientMulticastCount_Type())
etsysSntpClientMulticastCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientMulticastCount.setStatus(_A)
_EtsysSntpClientBroadcast_ObjectIdentity=ObjectIdentity
etsysSntpClientBroadcast=_EtsysSntpClientBroadcast_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,1,4))
class _EtsysSntpClientBroadcastDelay_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999))
_EtsysSntpClientBroadcastDelay_Type.__name__=_D
_EtsysSntpClientBroadcastDelay_Object=MibScalar
etsysSntpClientBroadcastDelay=_EtsysSntpClientBroadcastDelay_Object((1,3,6,1,4,1,5624,1,2,38,1,4,1),_EtsysSntpClientBroadcastDelay_Type())
etsysSntpClientBroadcastDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientBroadcastDelay.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientBroadcastDelay.setUnits(_U)
_EtsysSntpClientBroadcastCount_Type=Counter32
_EtsysSntpClientBroadcastCount_Object=MibScalar
etsysSntpClientBroadcastCount=_EtsysSntpClientBroadcastCount_Object((1,3,6,1,4,1,5624,1,2,38,1,4,2),_EtsysSntpClientBroadcastCount_Type())
etsysSntpClientBroadcastCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientBroadcastCount.setStatus(_A)
_EtsysSntpClientAnycast_ObjectIdentity=ObjectIdentity
etsysSntpClientAnycast=_EtsysSntpClientAnycast_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,1,5))
class _EtsysSntpClientAnycastBindRequestInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16284))
_EtsysSntpClientAnycastBindRequestInterval_Type.__name__=_D
_EtsysSntpClientAnycastBindRequestInterval_Object=MibScalar
etsysSntpClientAnycastBindRequestInterval=_EtsysSntpClientAnycastBindRequestInterval_Object((1,3,6,1,4,1,5624,1,2,38,1,5,1),_EtsysSntpClientAnycastBindRequestInterval_Type())
etsysSntpClientAnycastBindRequestInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientAnycastBindRequestInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientAnycastBindRequestInterval.setUnits(_H)
class _EtsysSntpClientAnycastPollInterval_Type(Unsigned32):defaultValue=512;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,16284))
_EtsysSntpClientAnycastPollInterval_Type.__name__=_D
_EtsysSntpClientAnycastPollInterval_Object=MibScalar
etsysSntpClientAnycastPollInterval=_EtsysSntpClientAnycastPollInterval_Object((1,3,6,1,4,1,5624,1,2,38,1,5,2),_EtsysSntpClientAnycastPollInterval_Type())
etsysSntpClientAnycastPollInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientAnycastPollInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientAnycastPollInterval.setUnits(_H)
class _EtsysSntpClientAnycastPollTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_EtsysSntpClientAnycastPollTimeout_Type.__name__=_D
_EtsysSntpClientAnycastPollTimeout_Object=MibScalar
etsysSntpClientAnycastPollTimeout=_EtsysSntpClientAnycastPollTimeout_Object((1,3,6,1,4,1,5624,1,2,38,1,5,3),_EtsysSntpClientAnycastPollTimeout_Type())
etsysSntpClientAnycastPollTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientAnycastPollTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysSntpClientAnycastPollTimeout.setUnits(_H)
class _EtsysSntpClientAnycastPollRetry_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EtsysSntpClientAnycastPollRetry_Type.__name__=_D
_EtsysSntpClientAnycastPollRetry_Object=MibScalar
etsysSntpClientAnycastPollRetry=_EtsysSntpClientAnycastPollRetry_Object((1,3,6,1,4,1,5624,1,2,38,1,5,4),_EtsysSntpClientAnycastPollRetry_Type())
etsysSntpClientAnycastPollRetry.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSntpClientAnycastPollRetry.setStatus(_A)
_EtsysSntpClientAnycastServerAddrType_Type=InetAddressType
_EtsysSntpClientAnycastServerAddrType_Object=MibScalar
etsysSntpClientAnycastServerAddrType=_EtsysSntpClientAnycastServerAddrType_Object((1,3,6,1,4,1,5624,1,2,38,1,5,5),_EtsysSntpClientAnycastServerAddrType_Type())
etsysSntpClientAnycastServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientAnycastServerAddrType.setStatus(_A)
class _EtsysSntpClientAnycastServerAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EtsysSntpClientAnycastServerAddr_Type.__name__=_I
_EtsysSntpClientAnycastServerAddr_Object=MibScalar
etsysSntpClientAnycastServerAddr=_EtsysSntpClientAnycastServerAddr_Object((1,3,6,1,4,1,5624,1,2,38,1,5,6),_EtsysSntpClientAnycastServerAddr_Type())
etsysSntpClientAnycastServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientAnycastServerAddr.setStatus(_A)
_EtsysSntpClientAnycastNumRequests_Type=Counter32
_EtsysSntpClientAnycastNumRequests_Object=MibScalar
etsysSntpClientAnycastNumRequests=_EtsysSntpClientAnycastNumRequests_Object((1,3,6,1,4,1,5624,1,2,38,1,5,7),_EtsysSntpClientAnycastNumRequests_Type())
etsysSntpClientAnycastNumRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientAnycastNumRequests.setStatus(_A)
_EtsysSntpClientAnycastNumPollRequests_Type=Counter32
_EtsysSntpClientAnycastNumPollRequests_Object=MibScalar
etsysSntpClientAnycastNumPollRequests=_EtsysSntpClientAnycastNumPollRequests_Object((1,3,6,1,4,1,5624,1,2,38,1,5,8),_EtsysSntpClientAnycastNumPollRequests_Type())
etsysSntpClientAnycastNumPollRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSntpClientAnycastNumPollRequests.setStatus(_A)
_EtsysSntpClientConformance_ObjectIdentity=ObjectIdentity
etsysSntpClientConformance=_EtsysSntpClientConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,2))
_EtsysSntpClientGroups_ObjectIdentity=ObjectIdentity
etsysSntpClientGroups=_EtsysSntpClientGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,2,1))
_EtsysSntpClientCompliances_ObjectIdentity=ObjectIdentity
etsysSntpClientCompliances=_EtsysSntpClientCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,38,2,2))
etsysSntpClientDeviceGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,38,2,1,1))
etsysSntpClientDeviceGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:etsysSntpClientDeviceGroup.setStatus(_A)
etsysSntpClientUnicastGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,38,2,1,2))
etsysSntpClientUnicastGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:etsysSntpClientUnicastGroup.setStatus(_A)
etsysSntpClientMulticastGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,38,2,1,3))
etsysSntpClientMulticastGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:etsysSntpClientMulticastGroup.setStatus(_A)
etsysSntpClientBroadcastGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,38,2,1,4))
etsysSntpClientBroadcastGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:etsysSntpClientBroadcastGroup.setStatus(_A)
etsysSntpClientAnycastGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,38,2,1,5))
etsysSntpClientAnycastGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:etsysSntpClientAnycastGroup.setStatus(_A)
etsysSntpClientUnicastAuthenticationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,38,2,1,6))
etsysSntpClientUnicastAuthenticationGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_N),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:etsysSntpClientUnicastAuthenticationGroup.setStatus(_A)
etsysSntpClientCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,38,2,2,1))
etsysSntpClientCompliance.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:etsysSntpClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_R:SntpClientOperModes,_L:SntpClientUpdateStatus,'etsysSntpClientMIB':etsysSntpClientMIB,'etsysSntpClientObjects':etsysSntpClientObjects,'etsysSntpClientDevice':etsysSntpClientDevice,_V:etsysSntpClientVersion,_W:etsysSntpClientSupportedMode,_X:etsysSntpClientMode,_Y:etsysSntpClientLastUpdateTime,_Z:etsysSntpClientLastAttemptTime,_a:etsysSntpClientLastAttemptStatus,_z:etsysSntpClientAuthenticationEnable,_A0:etsysSntpClientMaxAuthenticationKeys,'etsysSntpClientUnicast':etsysSntpClientUnicast,_b:etsysSntpClientUnicastPollInterval,_c:etsysSntpClientUnicastPollTimeout,_d:etsysSntpClientUnicastPollRetry,_e:etsysSntpClientUServerMaxEntries,_f:etsysSntpClientUServerCurrEntries,'etsysSntpClientUServerTable':etsysSntpClientUServerTable,'etsysSntpClientUServerEntry':etsysSntpClientUServerEntry,_S:etsysSntpClientUServerAddrType,_T:etsysSntpClientUServerAddr,_g:etsysSntpClientUServerPrecedence,_h:etsysSntpClientUServerLastUpdateTime,_i:etsysSntpClientUServerLastAttemptTime,_j:etsysSntpClientUServerLastAttemptStatus,_k:etsysSntpClientUServerNumRequests,_l:etsysSntpClientUServerNumFailedRequests,_m:etsysSntpClientUServerStatus,_A1:etsysSntpClientUServerAuthKey,'etsysSntpClientUAuthKeyTable':etsysSntpClientUAuthKeyTable,'etsysSntpClientUAuthKeyEntry':etsysSntpClientUAuthKeyEntry,_N:etsysSntpClientUAuthKey,_A2:etsysSntpClientUAuthType,_A3:etsysSntpClientUAuthValue,_A4:etsysSntpClientUKeyTrusted,_A5:etsysSntpClientUAuthKeyStatus,'etsysSntpClientMulticast':etsysSntpClientMulticast,_n:etsysSntpClientMulticastDelay,_o:etsysSntpClientMulticastCount,'etsysSntpClientBroadcast':etsysSntpClientBroadcast,_p:etsysSntpClientBroadcastDelay,_q:etsysSntpClientBroadcastCount,'etsysSntpClientAnycast':etsysSntpClientAnycast,_r:etsysSntpClientAnycastBindRequestInterval,_s:etsysSntpClientAnycastPollInterval,_t:etsysSntpClientAnycastPollTimeout,_u:etsysSntpClientAnycastPollRetry,_v:etsysSntpClientAnycastServerAddrType,_w:etsysSntpClientAnycastServerAddr,_x:etsysSntpClientAnycastNumRequests,_y:etsysSntpClientAnycastNumPollRequests,'etsysSntpClientConformance':etsysSntpClientConformance,'etsysSntpClientGroups':etsysSntpClientGroups,_A6:etsysSntpClientDeviceGroup,_A7:etsysSntpClientUnicastGroup,_A8:etsysSntpClientMulticastGroup,_A9:etsysSntpClientBroadcastGroup,_AA:etsysSntpClientAnycastGroup,_AB:etsysSntpClientUnicastAuthenticationGroup,'etsysSntpClientCompliances':etsysSntpClientCompliances,'etsysSntpClientCompliance':etsysSntpClientCompliance})