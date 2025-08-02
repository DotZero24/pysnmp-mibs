_z='agentSntpClientBroadcastGroup'
_y='agentSntpClientUnicastGroup'
_x='agentSntpClientDeviceGroup'
_w='agentSntpClientBroadcastInterval'
_v='agentSntpClientBroadcastCount'
_u='agentSntpClientUcastServerRowStatus'
_t='agentSntpClientUcastServerNumFailedRequests'
_s='agentSntpClientUcastServerNumRequests'
_r='agentSntpClientUcastServerLastAttemptStatus'
_q='agentSntpClientUcastServerLastAttemptTime'
_p='agentSntpClientUcastServerLastUpdateTime'
_o='agentSntpClientUcastServerPrecedence'
_n='agentSntpClientUcastServerAddressType'
_m='agentSntpClientUcastServerAddress'
_l='agentSntpClientUcastServerCurrEntries'
_k='agentSntpClientUcastServerMaxEntries'
_j='agentSntpClientUnicastPollRetry'
_i='agentSntpClientUnicastPollTimeout'
_h='agentSntpClientUnicastPollInterval'
_g='agentSntpClientServerRefClkId'
_f='agentSntpClientServerStratum'
_e='agentSntpClientServerMode'
_d='agentSntpClientServerAddress'
_c='agentSntpClientServerAddressType'
_b='agentSntpClientLastAttemptStatus'
_a='agentSntpClientLastAttemptTime'
_Z='agentSntpClientLastUpdateTime'
_Y='agentSntpClientMode'
_X='agentSntpClientSupportedMode'
_W='agentSntpClientVersion'
_V='agentSntpClientUcastServerIndex'
_U='version4'
_T='version3'
_S='version2'
_R='version1'
_Q='multicast'
_P='broadcast'
_O='unicast'
_N='disabled'
_M='DisplayString'
_L='Gauge32'
_K='OctetString'
_J='SntpClientUpdateStatus'
_I='InetPortNumber'
_H='seconds'
_G='read-create'
_F='Integer32'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='SNTP-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_I)
quanta,switch=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','quanta','switch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_L,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'PhysAddress','RowStatus','TextualConvention')
agentSntpClientMIB=ModuleIdentity((1,3,6,1,4,1,7244,2,17))
class SntpClientAdminMode(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
class SntpClientUpdateStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('success',2),('requestTimedOut',3),('badDateEncoded',4),('versionNotSupported',5),('serverUnsychronized',6),('serverKissOfDeath',7)))
_AgentSntpClientObjects_ObjectIdentity=ObjectIdentity
agentSntpClientObjects=_AgentSntpClientObjects_ObjectIdentity((1,3,6,1,4,1,7244,2,17,1))
_AgentSntpClient_ObjectIdentity=ObjectIdentity
agentSntpClient=_AgentSntpClient_ObjectIdentity((1,3,6,1,4,1,7244,2,17,1,1))
class _AgentSntpClientVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4)))
_AgentSntpClientVersion_Type.__name__=_F
_AgentSntpClientVersion_Object=MibScalar
agentSntpClientVersion=_AgentSntpClientVersion_Object((1,3,6,1,4,1,7244,2,17,1,1,1),_AgentSntpClientVersion_Type())
agentSntpClientVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientVersion.setStatus(_A)
_AgentSntpClientSupportedMode_Type=SntpClientAdminMode
_AgentSntpClientSupportedMode_Object=MibScalar
agentSntpClientSupportedMode=_AgentSntpClientSupportedMode_Object((1,3,6,1,4,1,7244,2,17,1,1,2),_AgentSntpClientSupportedMode_Type())
agentSntpClientSupportedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientSupportedMode.setStatus(_A)
class _AgentSntpClientMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3)))
_AgentSntpClientMode_Type.__name__=_F
_AgentSntpClientMode_Object=MibScalar
agentSntpClientMode=_AgentSntpClientMode_Object((1,3,6,1,4,1,7244,2,17,1,1,3),_AgentSntpClientMode_Type())
agentSntpClientMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientMode.setStatus(_A)
class _AgentSntpClientPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentSntpClientPort_Type.__name__=_I
_AgentSntpClientPort_Object=MibScalar
agentSntpClientPort=_AgentSntpClientPort_Object((1,3,6,1,4,1,7244,2,17,1,1,4),_AgentSntpClientPort_Type())
agentSntpClientPort.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientPort.setStatus(_A)
_AgentSntpClientLastUpdateTime_Type=DateAndTime
_AgentSntpClientLastUpdateTime_Object=MibScalar
agentSntpClientLastUpdateTime=_AgentSntpClientLastUpdateTime_Object((1,3,6,1,4,1,7244,2,17,1,1,5),_AgentSntpClientLastUpdateTime_Type())
agentSntpClientLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientLastUpdateTime.setStatus(_A)
_AgentSntpClientLastAttemptTime_Type=DateAndTime
_AgentSntpClientLastAttemptTime_Object=MibScalar
agentSntpClientLastAttemptTime=_AgentSntpClientLastAttemptTime_Object((1,3,6,1,4,1,7244,2,17,1,1,6),_AgentSntpClientLastAttemptTime_Type())
agentSntpClientLastAttemptTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientLastAttemptTime.setStatus(_A)
class _AgentSntpClientLastAttemptStatus_Type(SntpClientUpdateStatus):defaultValue=1
_AgentSntpClientLastAttemptStatus_Type.__name__=_J
_AgentSntpClientLastAttemptStatus_Object=MibScalar
agentSntpClientLastAttemptStatus=_AgentSntpClientLastAttemptStatus_Object((1,3,6,1,4,1,7244,2,17,1,1,7),_AgentSntpClientLastAttemptStatus_Type())
agentSntpClientLastAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientLastAttemptStatus.setStatus(_A)
_AgentSntpClientServerAddressType_Type=InetAddressType
_AgentSntpClientServerAddressType_Object=MibScalar
agentSntpClientServerAddressType=_AgentSntpClientServerAddressType_Object((1,3,6,1,4,1,7244,2,17,1,1,8),_AgentSntpClientServerAddressType_Type())
agentSntpClientServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientServerAddressType.setStatus(_A)
_AgentSntpClientServerAddress_Type=InetAddress
_AgentSntpClientServerAddress_Object=MibScalar
agentSntpClientServerAddress=_AgentSntpClientServerAddress_Object((1,3,6,1,4,1,7244,2,17,1,1,9),_AgentSntpClientServerAddress_Type())
agentSntpClientServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientServerAddress.setStatus(_A)
class _AgentSntpClientServerMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentSntpClientServerMode_Type.__name__=_E
_AgentSntpClientServerMode_Object=MibScalar
agentSntpClientServerMode=_AgentSntpClientServerMode_Object((1,3,6,1,4,1,7244,2,17,1,1,10),_AgentSntpClientServerMode_Type())
agentSntpClientServerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientServerMode.setStatus(_A)
class _AgentSntpClientServerStratum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentSntpClientServerStratum_Type.__name__=_E
_AgentSntpClientServerStratum_Object=MibScalar
agentSntpClientServerStratum=_AgentSntpClientServerStratum_Object((1,3,6,1,4,1,7244,2,17,1,1,11),_AgentSntpClientServerStratum_Type())
agentSntpClientServerStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientServerStratum.setStatus(_A)
class _AgentSntpClientServerRefClkId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AgentSntpClientServerRefClkId_Type.__name__=_K
_AgentSntpClientServerRefClkId_Object=MibScalar
agentSntpClientServerRefClkId=_AgentSntpClientServerRefClkId_Object((1,3,6,1,4,1,7244,2,17,1,1,12),_AgentSntpClientServerRefClkId_Type())
agentSntpClientServerRefClkId.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientServerRefClkId.setStatus(_A)
class _AgentSntpClientPollInterval_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_AgentSntpClientPollInterval_Type.__name__=_E
_AgentSntpClientPollInterval_Object=MibScalar
agentSntpClientPollInterval=_AgentSntpClientPollInterval_Object((1,3,6,1,4,1,7244,2,17,1,1,13),_AgentSntpClientPollInterval_Type())
agentSntpClientPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientPollInterval.setStatus('obsolete')
if mibBuilder.loadTexts:agentSntpClientPollInterval.setUnits(_H)
_AgentSntpClientSourceInterface_Type=InterfaceIndexOrZero
_AgentSntpClientSourceInterface_Object=MibScalar
agentSntpClientSourceInterface=_AgentSntpClientSourceInterface_Object((1,3,6,1,4,1,7244,2,17,1,1,14),_AgentSntpClientSourceInterface_Type())
agentSntpClientSourceInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientSourceInterface.setStatus(_A)
_AgentSntpClientTimeZone_ObjectIdentity=ObjectIdentity
agentSntpClientTimeZone=_AgentSntpClientTimeZone_ObjectIdentity((1,3,6,1,4,1,7244,2,17,1,2))
class _AgentSNTPConfigTimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_AgentSNTPConfigTimeZoneName_Type.__name__=_M
_AgentSNTPConfigTimeZoneName_Object=MibScalar
agentSNTPConfigTimeZoneName=_AgentSNTPConfigTimeZoneName_Object((1,3,6,1,4,1,7244,2,17,1,2,1),_AgentSNTPConfigTimeZoneName_Type())
agentSNTPConfigTimeZoneName.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPConfigTimeZoneName.setStatus(_A)
class _AgentSNTPConfigTimeZoneTimeOffsetHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AgentSNTPConfigTimeZoneTimeOffsetHour_Type.__name__=_F
_AgentSNTPConfigTimeZoneTimeOffsetHour_Object=MibScalar
agentSNTPConfigTimeZoneTimeOffsetHour=_AgentSNTPConfigTimeZoneTimeOffsetHour_Object((1,3,6,1,4,1,7244,2,17,1,2,2),_AgentSNTPConfigTimeZoneTimeOffsetHour_Type())
agentSNTPConfigTimeZoneTimeOffsetHour.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPConfigTimeZoneTimeOffsetHour.setStatus(_A)
class _AgentSNTPConfigTimeZoneTimeOffsetMinute_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_AgentSNTPConfigTimeZoneTimeOffsetMinute_Type.__name__=_E
_AgentSNTPConfigTimeZoneTimeOffsetMinute_Object=MibScalar
agentSNTPConfigTimeZoneTimeOffsetMinute=_AgentSNTPConfigTimeZoneTimeOffsetMinute_Object((1,3,6,1,4,1,7244,2,17,1,2,3),_AgentSNTPConfigTimeZoneTimeOffsetMinute_Type())
agentSNTPConfigTimeZoneTimeOffsetMinute.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPConfigTimeZoneTimeOffsetMinute.setStatus(_A)
class _AgentSNTPConfigTimeZoneUTCArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('beforeutc',1),('afterutc',2)))
_AgentSNTPConfigTimeZoneUTCArea_Type.__name__=_F
_AgentSNTPConfigTimeZoneUTCArea_Object=MibScalar
agentSNTPConfigTimeZoneUTCArea=_AgentSNTPConfigTimeZoneUTCArea_Object((1,3,6,1,4,1,7244,2,17,1,2,4),_AgentSNTPConfigTimeZoneUTCArea_Type())
agentSNTPConfigTimeZoneUTCArea.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPConfigTimeZoneUTCArea.setStatus(_A)
_AgentSntpClientUnicast_ObjectIdentity=ObjectIdentity
agentSntpClientUnicast=_AgentSntpClientUnicast_ObjectIdentity((1,3,6,1,4,1,7244,2,17,1,3))
class _AgentSntpClientUnicastPollInterval_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_AgentSntpClientUnicastPollInterval_Type.__name__=_E
_AgentSntpClientUnicastPollInterval_Object=MibScalar
agentSntpClientUnicastPollInterval=_AgentSntpClientUnicastPollInterval_Object((1,3,6,1,4,1,7244,2,17,1,3,1),_AgentSntpClientUnicastPollInterval_Type())
agentSntpClientUnicastPollInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientUnicastPollInterval.setStatus(_A)
if mibBuilder.loadTexts:agentSntpClientUnicastPollInterval.setUnits(_H)
class _AgentSntpClientUnicastPollTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentSntpClientUnicastPollTimeout_Type.__name__=_E
_AgentSntpClientUnicastPollTimeout_Object=MibScalar
agentSntpClientUnicastPollTimeout=_AgentSntpClientUnicastPollTimeout_Object((1,3,6,1,4,1,7244,2,17,1,3,2),_AgentSntpClientUnicastPollTimeout_Type())
agentSntpClientUnicastPollTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientUnicastPollTimeout.setStatus(_A)
if mibBuilder.loadTexts:agentSntpClientUnicastPollTimeout.setUnits(_H)
class _AgentSntpClientUnicastPollRetry_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AgentSntpClientUnicastPollRetry_Type.__name__=_E
_AgentSntpClientUnicastPollRetry_Object=MibScalar
agentSntpClientUnicastPollRetry=_AgentSntpClientUnicastPollRetry_Object((1,3,6,1,4,1,7244,2,17,1,3,3),_AgentSntpClientUnicastPollRetry_Type())
agentSntpClientUnicastPollRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientUnicastPollRetry.setStatus(_A)
class _AgentSntpClientUcastServerMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AgentSntpClientUcastServerMaxEntries_Type.__name__=_E
_AgentSntpClientUcastServerMaxEntries_Object=MibScalar
agentSntpClientUcastServerMaxEntries=_AgentSntpClientUcastServerMaxEntries_Object((1,3,6,1,4,1,7244,2,17,1,3,4),_AgentSntpClientUcastServerMaxEntries_Type())
agentSntpClientUcastServerMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerMaxEntries.setStatus(_A)
class _AgentSntpClientUcastServerCurrEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AgentSntpClientUcastServerCurrEntries_Type.__name__=_L
_AgentSntpClientUcastServerCurrEntries_Object=MibScalar
agentSntpClientUcastServerCurrEntries=_AgentSntpClientUcastServerCurrEntries_Object((1,3,6,1,4,1,7244,2,17,1,3,5),_AgentSntpClientUcastServerCurrEntries_Type())
agentSntpClientUcastServerCurrEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerCurrEntries.setStatus(_A)
_AgentSntpClientUcastServerTable_Object=MibTable
agentSntpClientUcastServerTable=_AgentSntpClientUcastServerTable_Object((1,3,6,1,4,1,7244,2,17,1,3,6))
if mibBuilder.loadTexts:agentSntpClientUcastServerTable.setStatus(_A)
_AgentSntpClientUcastServerEntry_Object=MibTableRow
agentSntpClientUcastServerEntry=_AgentSntpClientUcastServerEntry_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1))
agentSntpClientUcastServerEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:agentSntpClientUcastServerEntry.setStatus(_A)
_AgentSntpClientUcastServerIndex_Type=Unsigned32
_AgentSntpClientUcastServerIndex_Object=MibTableColumn
agentSntpClientUcastServerIndex=_AgentSntpClientUcastServerIndex_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,1),_AgentSntpClientUcastServerIndex_Type())
agentSntpClientUcastServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentSntpClientUcastServerIndex.setStatus(_A)
_AgentSntpClientUcastServerAddressType_Type=InetAddressType
_AgentSntpClientUcastServerAddressType_Object=MibTableColumn
agentSntpClientUcastServerAddressType=_AgentSntpClientUcastServerAddressType_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,2),_AgentSntpClientUcastServerAddressType_Type())
agentSntpClientUcastServerAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSntpClientUcastServerAddressType.setStatus(_A)
_AgentSntpClientUcastServerAddress_Type=InetAddress
_AgentSntpClientUcastServerAddress_Object=MibTableColumn
agentSntpClientUcastServerAddress=_AgentSntpClientUcastServerAddress_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,3),_AgentSntpClientUcastServerAddress_Type())
agentSntpClientUcastServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSntpClientUcastServerAddress.setStatus(_A)
class _AgentSntpClientUcastServerPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentSntpClientUcastServerPort_Type.__name__=_I
_AgentSntpClientUcastServerPort_Object=MibTableColumn
agentSntpClientUcastServerPort=_AgentSntpClientUcastServerPort_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,4),_AgentSntpClientUcastServerPort_Type())
agentSntpClientUcastServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSntpClientUcastServerPort.setStatus(_A)
class _AgentSntpClientUcastServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4)))
_AgentSntpClientUcastServerVersion_Type.__name__=_F
_AgentSntpClientUcastServerVersion_Object=MibTableColumn
agentSntpClientUcastServerVersion=_AgentSntpClientUcastServerVersion_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,5),_AgentSntpClientUcastServerVersion_Type())
agentSntpClientUcastServerVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSntpClientUcastServerVersion.setStatus(_A)
class _AgentSntpClientUcastServerPrecedence_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AgentSntpClientUcastServerPrecedence_Type.__name__=_E
_AgentSntpClientUcastServerPrecedence_Object=MibTableColumn
agentSntpClientUcastServerPrecedence=_AgentSntpClientUcastServerPrecedence_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,6),_AgentSntpClientUcastServerPrecedence_Type())
agentSntpClientUcastServerPrecedence.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSntpClientUcastServerPrecedence.setStatus(_A)
_AgentSntpClientUcastServerLastUpdateTime_Type=DateAndTime
_AgentSntpClientUcastServerLastUpdateTime_Object=MibTableColumn
agentSntpClientUcastServerLastUpdateTime=_AgentSntpClientUcastServerLastUpdateTime_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,7),_AgentSntpClientUcastServerLastUpdateTime_Type())
agentSntpClientUcastServerLastUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerLastUpdateTime.setStatus(_A)
_AgentSntpClientUcastServerLastAttemptTime_Type=DateAndTime
_AgentSntpClientUcastServerLastAttemptTime_Object=MibTableColumn
agentSntpClientUcastServerLastAttemptTime=_AgentSntpClientUcastServerLastAttemptTime_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,8),_AgentSntpClientUcastServerLastAttemptTime_Type())
agentSntpClientUcastServerLastAttemptTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerLastAttemptTime.setStatus(_A)
class _AgentSntpClientUcastServerLastAttemptStatus_Type(SntpClientUpdateStatus):defaultValue=1
_AgentSntpClientUcastServerLastAttemptStatus_Type.__name__=_J
_AgentSntpClientUcastServerLastAttemptStatus_Object=MibTableColumn
agentSntpClientUcastServerLastAttemptStatus=_AgentSntpClientUcastServerLastAttemptStatus_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,9),_AgentSntpClientUcastServerLastAttemptStatus_Type())
agentSntpClientUcastServerLastAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerLastAttemptStatus.setStatus(_A)
_AgentSntpClientUcastServerNumRequests_Type=Counter32
_AgentSntpClientUcastServerNumRequests_Object=MibTableColumn
agentSntpClientUcastServerNumRequests=_AgentSntpClientUcastServerNumRequests_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,10),_AgentSntpClientUcastServerNumRequests_Type())
agentSntpClientUcastServerNumRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerNumRequests.setStatus(_A)
_AgentSntpClientUcastServerNumFailedRequests_Type=Counter32
_AgentSntpClientUcastServerNumFailedRequests_Object=MibTableColumn
agentSntpClientUcastServerNumFailedRequests=_AgentSntpClientUcastServerNumFailedRequests_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,11),_AgentSntpClientUcastServerNumFailedRequests_Type())
agentSntpClientUcastServerNumFailedRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientUcastServerNumFailedRequests.setStatus(_A)
_AgentSntpClientUcastServerRowStatus_Type=RowStatus
_AgentSntpClientUcastServerRowStatus_Object=MibTableColumn
agentSntpClientUcastServerRowStatus=_AgentSntpClientUcastServerRowStatus_Object((1,3,6,1,4,1,7244,2,17,1,3,6,1,12),_AgentSntpClientUcastServerRowStatus_Type())
agentSntpClientUcastServerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentSntpClientUcastServerRowStatus.setStatus(_A)
_AgentSntpClientBroadcast_ObjectIdentity=ObjectIdentity
agentSntpClientBroadcast=_AgentSntpClientBroadcast_ObjectIdentity((1,3,6,1,4,1,7244,2,17,1,4))
_AgentSntpClientBroadcastCount_Type=Counter32
_AgentSntpClientBroadcastCount_Object=MibScalar
agentSntpClientBroadcastCount=_AgentSntpClientBroadcastCount_Object((1,3,6,1,4,1,7244,2,17,1,4,1),_AgentSntpClientBroadcastCount_Type())
agentSntpClientBroadcastCount.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientBroadcastCount.setStatus(_A)
class _AgentSntpClientBroadcastInterval_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_AgentSntpClientBroadcastInterval_Type.__name__=_E
_AgentSntpClientBroadcastInterval_Object=MibScalar
agentSntpClientBroadcastInterval=_AgentSntpClientBroadcastInterval_Object((1,3,6,1,4,1,7244,2,17,1,4,2),_AgentSntpClientBroadcastInterval_Type())
agentSntpClientBroadcastInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientBroadcastInterval.setStatus(_A)
if mibBuilder.loadTexts:agentSntpClientBroadcastInterval.setUnits(_H)
_AgentSntpClientMulticast_ObjectIdentity=ObjectIdentity
agentSntpClientMulticast=_AgentSntpClientMulticast_ObjectIdentity((1,3,6,1,4,1,7244,2,17,1,5))
_AgentSntpClientMulticastCount_Type=Counter32
_AgentSntpClientMulticastCount_Object=MibScalar
agentSntpClientMulticastCount=_AgentSntpClientMulticastCount_Object((1,3,6,1,4,1,7244,2,17,1,5,1),_AgentSntpClientMulticastCount_Type())
agentSntpClientMulticastCount.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSntpClientMulticastCount.setStatus(_A)
class _AgentSntpClientMulticastInterval_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_AgentSntpClientMulticastInterval_Type.__name__=_E
_AgentSntpClientMulticastInterval_Object=MibScalar
agentSntpClientMulticastInterval=_AgentSntpClientMulticastInterval_Object((1,3,6,1,4,1,7244,2,17,1,5,2),_AgentSntpClientMulticastInterval_Type())
agentSntpClientMulticastInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSntpClientMulticastInterval.setStatus(_A)
if mibBuilder.loadTexts:agentSntpClientMulticastInterval.setUnits(_H)
_AgentSntpClientConformance_ObjectIdentity=ObjectIdentity
agentSntpClientConformance=_AgentSntpClientConformance_ObjectIdentity((1,3,6,1,4,1,7244,2,17,2))
_AgentSntpClientGroups_ObjectIdentity=ObjectIdentity
agentSntpClientGroups=_AgentSntpClientGroups_ObjectIdentity((1,3,6,1,4,1,7244,2,17,2,1))
_AgentSntpClientCompliances_ObjectIdentity=ObjectIdentity
agentSntpClientCompliances=_AgentSntpClientCompliances_ObjectIdentity((1,3,6,1,4,1,7244,2,17,2,2))
agentSntpClientDeviceGroup=ObjectGroup((1,3,6,1,4,1,7244,2,17,2,1,1))
agentSntpClientDeviceGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:agentSntpClientDeviceGroup.setStatus(_A)
agentSntpClientUnicastGroup=ObjectGroup((1,3,6,1,4,1,7244,2,17,2,1,2))
agentSntpClientUnicastGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:agentSntpClientUnicastGroup.setStatus(_A)
agentSntpClientBroadcastGroup=ObjectGroup((1,3,6,1,4,1,7244,2,17,2,1,3))
agentSntpClientBroadcastGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:agentSntpClientBroadcastGroup.setStatus(_A)
agentSntpClientCompliance=ModuleCompliance((1,3,6,1,4,1,7244,2,17,2,2,1))
agentSntpClientCompliance.setObjects(*((_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:agentSntpClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SntpClientAdminMode':SntpClientAdminMode,_J:SntpClientUpdateStatus,'agentSntpClientMIB':agentSntpClientMIB,'agentSntpClientObjects':agentSntpClientObjects,'agentSntpClient':agentSntpClient,_W:agentSntpClientVersion,_X:agentSntpClientSupportedMode,_Y:agentSntpClientMode,'agentSntpClientPort':agentSntpClientPort,_Z:agentSntpClientLastUpdateTime,_a:agentSntpClientLastAttemptTime,_b:agentSntpClientLastAttemptStatus,_c:agentSntpClientServerAddressType,_d:agentSntpClientServerAddress,_e:agentSntpClientServerMode,_f:agentSntpClientServerStratum,_g:agentSntpClientServerRefClkId,'agentSntpClientPollInterval':agentSntpClientPollInterval,'agentSntpClientSourceInterface':agentSntpClientSourceInterface,'agentSntpClientTimeZone':agentSntpClientTimeZone,'agentSNTPConfigTimeZoneName':agentSNTPConfigTimeZoneName,'agentSNTPConfigTimeZoneTimeOffsetHour':agentSNTPConfigTimeZoneTimeOffsetHour,'agentSNTPConfigTimeZoneTimeOffsetMinute':agentSNTPConfigTimeZoneTimeOffsetMinute,'agentSNTPConfigTimeZoneUTCArea':agentSNTPConfigTimeZoneUTCArea,'agentSntpClientUnicast':agentSntpClientUnicast,_h:agentSntpClientUnicastPollInterval,_i:agentSntpClientUnicastPollTimeout,_j:agentSntpClientUnicastPollRetry,_k:agentSntpClientUcastServerMaxEntries,_l:agentSntpClientUcastServerCurrEntries,'agentSntpClientUcastServerTable':agentSntpClientUcastServerTable,'agentSntpClientUcastServerEntry':agentSntpClientUcastServerEntry,_V:agentSntpClientUcastServerIndex,_n:agentSntpClientUcastServerAddressType,_m:agentSntpClientUcastServerAddress,'agentSntpClientUcastServerPort':agentSntpClientUcastServerPort,'agentSntpClientUcastServerVersion':agentSntpClientUcastServerVersion,_o:agentSntpClientUcastServerPrecedence,_p:agentSntpClientUcastServerLastUpdateTime,_q:agentSntpClientUcastServerLastAttemptTime,_r:agentSntpClientUcastServerLastAttemptStatus,_s:agentSntpClientUcastServerNumRequests,_t:agentSntpClientUcastServerNumFailedRequests,_u:agentSntpClientUcastServerRowStatus,'agentSntpClientBroadcast':agentSntpClientBroadcast,_v:agentSntpClientBroadcastCount,_w:agentSntpClientBroadcastInterval,'agentSntpClientMulticast':agentSntpClientMulticast,'agentSntpClientMulticastCount':agentSntpClientMulticastCount,'agentSntpClientMulticastInterval':agentSntpClientMulticastInterval,'agentSntpClientConformance':agentSntpClientConformance,'agentSntpClientGroups':agentSntpClientGroups,_x:agentSntpClientDeviceGroup,_y:agentSntpClientUnicastGroup,_z:agentSntpClientBroadcastGroup,'agentSntpClientCompliances':agentSntpClientCompliances,'agentSntpClientCompliance':agentSntpClientCompliance})