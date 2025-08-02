_AD='hm2Dot1asIsSynchronized'
_AC='hm2SntpClientStatus'
_AB='hm2PtpIsSynchronized'
_AA='halfDuplex'
_A9='asymmCorrection'
_A8='ptp2UdpIpv6'
_A7='ptp2UdpIpv4'
_A6='ptp2Ieee8023'
_A5='p2p-delay'
_A4='e2e-delay'
_A3='Hm2Ptp2LogSyncIntervalTc'
_A2='beyond10s'
_A1='within250ms'
_A0='within25ms'
_z='within2500us'
_y='within1000us'
_x='within250us'
_w='within25us'
_v='within2500ns'
_u='within1000ns'
_t='within250ns'
_s='within25ns'
_r='hm2NtpClientListenAddrIndex'
_q='genericError'
_p='synchronized'
_o='synchronizing'
_n='notResponding'
_m='protocolError'
_l='hm2NtpClientServerIndex'
_k='hm2SntpClientServerIndex'
_j='broadcast'
_i='unicast'
_h='hm2SntpServerBroadcastVlan'
_g='syncToRemoteServer'
_f='syncToRefclock'
_e='syncToLocal'
_d='sec-16'
_c='Hm2Ptp2LogPdelayReqIntervalTc'
_b='within10s'
_a='within1s'
_Z='within100ms'
_Y='within10ms'
_X='within100us'
_W='within10us'
_V='within100ns'
_U='not-accessible'
_T='sec-2'
_S='sec-1'
_R='Bits'
_Q='ifIndex'
_P='InterfaceIndexOrZero'
_O='IF-MIB'
_N='00000000'
_M='notSynchronized'
_L='InetAddressType'
_K='InetAddress'
_J='InetPortNumber'
_I='TruthValue'
_H='HM2-TIMESYNC-MIB'
_G='disabled'
_F='HmEnabledStatus'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_F,'HmTimeSeconds1970','hm2ConfigurationMibs')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_O,_P,_Q)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,_L,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_R,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
hm2TimeSyncMib=ModuleIdentity((1,3,6,1,4,1,248,11,50))
if mibBuilder.loadTexts:hm2TimeSyncMib.setRevisions(('2018-09-07 00:00',))
class HmSntpClientServerStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('success',2),('requestTimedOut',3),('badDateEncoded',4),('versionNotSupported',5),('serverUnsychronized',6),('serverKissOfDeath',7)))
class Hm2Ptp2LogSyncIntervalTc(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-3,-2,-1,0,1)));namedValues=NamedValues(*(('msec-125',-3),('msec-250',-2),('msec-500',-1),(_S,0),(_T,1)))
class Hm2Ptp2LogPdelayReqIntervalTc(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_S,0),(_T,1),('sec-4',2),('sec-8',3),(_d,4),('sec-32',5)))
class PtpTimeInterval(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class PtpTimeStamp(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
class PtpPortIdentity(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
class PtpClockIdentity(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class PtpClockQuality(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Hm2TimeSyncMibNotifications_ObjectIdentity=ObjectIdentity
hm2TimeSyncMibNotifications=_Hm2TimeSyncMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,50,0))
_Hm2TimeSyncMibObjects_ObjectIdentity=ObjectIdentity
hm2TimeSyncMibObjects=_Hm2TimeSyncMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,50,1))
_Hm2SystemTimeGroup_ObjectIdentity=ObjectIdentity
hm2SystemTimeGroup=_Hm2SystemTimeGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,1))
_Hm2SystemUtcTime_Type=HmTimeSeconds1970
_Hm2SystemUtcTime_Object=MibScalar
hm2SystemUtcTime=_Hm2SystemUtcTime_Object((1,3,6,1,4,1,248,11,50,1,1,1),_Hm2SystemUtcTime_Type())
hm2SystemUtcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SystemUtcTime.setStatus(_A)
class _Hm2SystemTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('local',1),('sntp',2),('ntp',3),('ptp',4),('gps',5)))
_Hm2SystemTimeSource_Type.__name__=_C
_Hm2SystemTimeSource_Object=MibScalar
hm2SystemTimeSource=_Hm2SystemTimeSource_Object((1,3,6,1,4,1,248,11,50,1,1,2),_Hm2SystemTimeSource_Type())
hm2SystemTimeSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2SystemTimeSource.setStatus(_A)
_Hm2SystemLocalTime_Type=HmTimeSeconds1970
_Hm2SystemLocalTime_Object=MibScalar
hm2SystemLocalTime=_Hm2SystemLocalTime_Object((1,3,6,1,4,1,248,11,50,1,1,3),_Hm2SystemLocalTime_Type())
hm2SystemLocalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SystemLocalTime.setStatus(_A)
class _Hm2SystemLocalOffset_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-780,840))
_Hm2SystemLocalOffset_Type.__name__=_C
_Hm2SystemLocalOffset_Object=MibScalar
hm2SystemLocalOffset=_Hm2SystemLocalOffset_Object((1,3,6,1,4,1,248,11,50,1,1,4),_Hm2SystemLocalOffset_Type())
hm2SystemLocalOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SystemLocalOffset.setStatus(_A)
_Hm2SntpGroup_ObjectIdentity=ObjectIdentity
hm2SntpGroup=_Hm2SntpGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,2))
_Hm2SntpServerGroup_ObjectIdentity=ObjectIdentity
hm2SntpServerGroup=_Hm2SntpServerGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,2,1))
class _Hm2SntpServerAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2SntpServerAdminState_Type.__name__=_F
_Hm2SntpServerAdminState_Object=MibScalar
hm2SntpServerAdminState=_Hm2SntpServerAdminState_Object((1,3,6,1,4,1,248,11,50,1,2,1,1),_Hm2SntpServerAdminState_Type())
hm2SntpServerAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerAdminState.setStatus(_A)
class _Hm2SntpServerPort_Type(InetPortNumber):defaultValue=123;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2SntpServerPort_Type.__name__=_J
_Hm2SntpServerPort_Object=MibScalar
hm2SntpServerPort=_Hm2SntpServerPort_Object((1,3,6,1,4,1,248,11,50,1,2,1,2),_Hm2SntpServerPort_Type())
hm2SntpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerPort.setStatus(_A)
class _Hm2SntpServerOnlyIfSync_Type(HmEnabledStatus):defaultValue=2
_Hm2SntpServerOnlyIfSync_Type.__name__=_F
_Hm2SntpServerOnlyIfSync_Object=MibScalar
hm2SntpServerOnlyIfSync=_Hm2SntpServerOnlyIfSync_Object((1,3,6,1,4,1,248,11,50,1,2,1,3),_Hm2SntpServerOnlyIfSync_Type())
hm2SntpServerOnlyIfSync.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerOnlyIfSync.setStatus(_A)
class _Hm2SntpServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_M,2),(_e,3),(_f,4),(_g,5)))
_Hm2SntpServerStatus_Type.__name__=_C
_Hm2SntpServerStatus_Object=MibScalar
hm2SntpServerStatus=_Hm2SntpServerStatus_Object((1,3,6,1,4,1,248,11,50,1,2,1,4),_Hm2SntpServerStatus_Type())
hm2SntpServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2SntpServerStatus.setStatus(_A)
class _Hm2SntpServerInterface_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2SntpServerInterface_Type.__name__=_P
_Hm2SntpServerInterface_Object=MibScalar
hm2SntpServerInterface=_Hm2SntpServerInterface_Object((1,3,6,1,4,1,248,11,50,1,2,1,5),_Hm2SntpServerInterface_Type())
hm2SntpServerInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerInterface.setStatus(_A)
_Hm2SntpServerBroadcastGroup_ObjectIdentity=ObjectIdentity
hm2SntpServerBroadcastGroup=_Hm2SntpServerBroadcastGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,2,2))
class _Hm2SntpServerBroadcastAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2SntpServerBroadcastAdminState_Type.__name__=_F
_Hm2SntpServerBroadcastAdminState_Object=MibScalar
hm2SntpServerBroadcastAdminState=_Hm2SntpServerBroadcastAdminState_Object((1,3,6,1,4,1,248,11,50,1,2,2,1),_Hm2SntpServerBroadcastAdminState_Type())
hm2SntpServerBroadcastAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerBroadcastAdminState.setStatus(_A)
class _Hm2SntpServerBroadcastAddrType_Type(InetAddressType):defaultValue=1
_Hm2SntpServerBroadcastAddrType_Type.__name__=_L
_Hm2SntpServerBroadcastAddrType_Object=MibScalar
hm2SntpServerBroadcastAddrType=_Hm2SntpServerBroadcastAddrType_Object((1,3,6,1,4,1,248,11,50,1,2,2,2),_Hm2SntpServerBroadcastAddrType_Type())
hm2SntpServerBroadcastAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerBroadcastAddrType.setStatus(_A)
class _Hm2SntpServerBroadcastAddr_Type(InetAddress):defaultHexValue=_N
_Hm2SntpServerBroadcastAddr_Type.__name__=_K
_Hm2SntpServerBroadcastAddr_Object=MibScalar
hm2SntpServerBroadcastAddr=_Hm2SntpServerBroadcastAddr_Object((1,3,6,1,4,1,248,11,50,1,2,2,3),_Hm2SntpServerBroadcastAddr_Type())
hm2SntpServerBroadcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerBroadcastAddr.setStatus(_A)
class _Hm2SntpServerBroadcastPort_Type(InetPortNumber):defaultValue=123;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2SntpServerBroadcastPort_Type.__name__=_J
_Hm2SntpServerBroadcastPort_Object=MibScalar
hm2SntpServerBroadcastPort=_Hm2SntpServerBroadcastPort_Object((1,3,6,1,4,1,248,11,50,1,2,2,4),_Hm2SntpServerBroadcastPort_Type())
hm2SntpServerBroadcastPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerBroadcastPort.setStatus(_A)
class _Hm2SntpServerBroadcastInterval_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024))
_Hm2SntpServerBroadcastInterval_Type.__name__=_C
_Hm2SntpServerBroadcastInterval_Object=MibScalar
hm2SntpServerBroadcastInterval=_Hm2SntpServerBroadcastInterval_Object((1,3,6,1,4,1,248,11,50,1,2,2,5),_Hm2SntpServerBroadcastInterval_Type())
hm2SntpServerBroadcastInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpServerBroadcastInterval.setStatus(_A)
_Hm2SntpServerBroadcastVlanTable_Object=MibTable
hm2SntpServerBroadcastVlanTable=_Hm2SntpServerBroadcastVlanTable_Object((1,3,6,1,4,1,248,11,50,1,2,2,10))
if mibBuilder.loadTexts:hm2SntpServerBroadcastVlanTable.setStatus(_A)
_Hm2SntpServerBroadcastVlanEntry_Object=MibTableRow
hm2SntpServerBroadcastVlanEntry=_Hm2SntpServerBroadcastVlanEntry_Object((1,3,6,1,4,1,248,11,50,1,2,2,10,1))
hm2SntpServerBroadcastVlanEntry.setIndexNames((0,_H,_h))
if mibBuilder.loadTexts:hm2SntpServerBroadcastVlanEntry.setStatus(_A)
class _Hm2SntpServerBroadcastVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4042))
_Hm2SntpServerBroadcastVlan_Type.__name__=_C
_Hm2SntpServerBroadcastVlan_Object=MibTableColumn
hm2SntpServerBroadcastVlan=_Hm2SntpServerBroadcastVlan_Object((1,3,6,1,4,1,248,11,50,1,2,2,10,1,1),_Hm2SntpServerBroadcastVlan_Type())
hm2SntpServerBroadcastVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2SntpServerBroadcastVlan.setStatus(_A)
_Hm2SntpServerBroadcastVlanRowStatus_Type=RowStatus
_Hm2SntpServerBroadcastVlanRowStatus_Object=MibTableColumn
hm2SntpServerBroadcastVlanRowStatus=_Hm2SntpServerBroadcastVlanRowStatus_Object((1,3,6,1,4,1,248,11,50,1,2,2,10,1,2),_Hm2SntpServerBroadcastVlanRowStatus_Type())
hm2SntpServerBroadcastVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SntpServerBroadcastVlanRowStatus.setStatus(_A)
_Hm2SntpClientGroup_ObjectIdentity=ObjectIdentity
hm2SntpClientGroup=_Hm2SntpClientGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,2,3))
class _Hm2SntpClientAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2SntpClientAdminState_Type.__name__=_F
_Hm2SntpClientAdminState_Object=MibScalar
hm2SntpClientAdminState=_Hm2SntpClientAdminState_Object((1,3,6,1,4,1,248,11,50,1,2,3,1),_Hm2SntpClientAdminState_Type())
hm2SntpClientAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpClientAdminState.setStatus(_A)
class _Hm2SntpClientOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_Hm2SntpClientOperatingMode_Type.__name__=_C
_Hm2SntpClientOperatingMode_Object=MibScalar
hm2SntpClientOperatingMode=_Hm2SntpClientOperatingMode_Object((1,3,6,1,4,1,248,11,50,1,2,3,2),_Hm2SntpClientOperatingMode_Type())
hm2SntpClientOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpClientOperatingMode.setStatus(_A)
class _Hm2SntpClientDisableAfterSync_Type(HmEnabledStatus):defaultValue=2
_Hm2SntpClientDisableAfterSync_Type.__name__=_F
_Hm2SntpClientDisableAfterSync_Object=MibScalar
hm2SntpClientDisableAfterSync=_Hm2SntpClientDisableAfterSync_Object((1,3,6,1,4,1,248,11,50,1,2,3,3),_Hm2SntpClientDisableAfterSync_Type())
hm2SntpClientDisableAfterSync.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpClientDisableAfterSync.setStatus(_A)
class _Hm2SntpClientRequestInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_Hm2SntpClientRequestInterval_Type.__name__=_C
_Hm2SntpClientRequestInterval_Object=MibScalar
hm2SntpClientRequestInterval=_Hm2SntpClientRequestInterval_Object((1,3,6,1,4,1,248,11,50,1,2,3,4),_Hm2SntpClientRequestInterval_Type())
hm2SntpClientRequestInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpClientRequestInterval.setStatus(_A)
class _Hm2SntpClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*((_G,1),(_M,2),('synchronizedToRemoteServer',5)))
_Hm2SntpClientStatus_Type.__name__=_C
_Hm2SntpClientStatus_Object=MibScalar
hm2SntpClientStatus=_Hm2SntpClientStatus_Object((1,3,6,1,4,1,248,11,50,1,2,3,5),_Hm2SntpClientStatus_Type())
hm2SntpClientStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2SntpClientStatus.setStatus(_A)
class _Hm2SntpClientBroadcastRecvTimeout_Type(Integer32):defaultValue=320;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,2048))
_Hm2SntpClientBroadcastRecvTimeout_Type.__name__=_C
_Hm2SntpClientBroadcastRecvTimeout_Object=MibScalar
hm2SntpClientBroadcastRecvTimeout=_Hm2SntpClientBroadcastRecvTimeout_Object((1,3,6,1,4,1,248,11,50,1,2,3,6),_Hm2SntpClientBroadcastRecvTimeout_Type())
hm2SntpClientBroadcastRecvTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpClientBroadcastRecvTimeout.setStatus(_A)
class _Hm2SntpClientInterface_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2SntpClientInterface_Type.__name__=_P
_Hm2SntpClientInterface_Object=MibScalar
hm2SntpClientInterface=_Hm2SntpClientInterface_Object((1,3,6,1,4,1,248,11,50,1,2,3,7),_Hm2SntpClientInterface_Type())
hm2SntpClientInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SntpClientInterface.setStatus(_A)
_Hm2SntpClientServerAddrTable_Object=MibTable
hm2SntpClientServerAddrTable=_Hm2SntpClientServerAddrTable_Object((1,3,6,1,4,1,248,11,50,1,2,3,10))
if mibBuilder.loadTexts:hm2SntpClientServerAddrTable.setStatus(_A)
_Hm2SntpClientServerAddrEntry_Object=MibTableRow
hm2SntpClientServerAddrEntry=_Hm2SntpClientServerAddrEntry_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1))
hm2SntpClientServerAddrEntry.setIndexNames((0,_H,_k))
if mibBuilder.loadTexts:hm2SntpClientServerAddrEntry.setStatus(_A)
class _Hm2SntpClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2SntpClientServerIndex_Type.__name__=_C
_Hm2SntpClientServerIndex_Object=MibTableColumn
hm2SntpClientServerIndex=_Hm2SntpClientServerIndex_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,1),_Hm2SntpClientServerIndex_Type())
hm2SntpClientServerIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:hm2SntpClientServerIndex.setStatus(_A)
class _Hm2SntpClientServerAddrType_Type(InetAddressType):defaultValue=1
_Hm2SntpClientServerAddrType_Type.__name__=_L
_Hm2SntpClientServerAddrType_Object=MibTableColumn
hm2SntpClientServerAddrType=_Hm2SntpClientServerAddrType_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,2),_Hm2SntpClientServerAddrType_Type())
hm2SntpClientServerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SntpClientServerAddrType.setStatus(_A)
class _Hm2SntpClientServerAddr_Type(InetAddress):defaultHexValue=_N
_Hm2SntpClientServerAddr_Type.__name__=_K
_Hm2SntpClientServerAddr_Object=MibTableColumn
hm2SntpClientServerAddr=_Hm2SntpClientServerAddr_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,3),_Hm2SntpClientServerAddr_Type())
hm2SntpClientServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SntpClientServerAddr.setStatus(_A)
class _Hm2SntpClientServerPort_Type(InetPortNumber):defaultValue=123;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2SntpClientServerPort_Type.__name__=_J
_Hm2SntpClientServerPort_Object=MibTableColumn
hm2SntpClientServerPort=_Hm2SntpClientServerPort_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,4),_Hm2SntpClientServerPort_Type())
hm2SntpClientServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SntpClientServerPort.setStatus(_A)
_Hm2SntpClientServerDescr_Type=DisplayString
_Hm2SntpClientServerDescr_Object=MibTableColumn
hm2SntpClientServerDescr=_Hm2SntpClientServerDescr_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,5),_Hm2SntpClientServerDescr_Type())
hm2SntpClientServerDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SntpClientServerDescr.setStatus(_A)
_Hm2SntpClientServerStatus_Type=HmSntpClientServerStatus
_Hm2SntpClientServerStatus_Object=MibTableColumn
hm2SntpClientServerStatus=_Hm2SntpClientServerStatus_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,6),_Hm2SntpClientServerStatus_Type())
hm2SntpClientServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2SntpClientServerStatus.setStatus(_A)
_Hm2SntpClientServerRowStatus_Type=RowStatus
_Hm2SntpClientServerRowStatus_Object=MibTableColumn
hm2SntpClientServerRowStatus=_Hm2SntpClientServerRowStatus_Object((1,3,6,1,4,1,248,11,50,1,2,3,10,1,7),_Hm2SntpClientServerRowStatus_Type())
hm2SntpClientServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SntpClientServerRowStatus.setStatus(_A)
_Hm2NtpGroup_ObjectIdentity=ObjectIdentity
hm2NtpGroup=_Hm2NtpGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,3))
_Hm2NtpGeneralGroup_ObjectIdentity=ObjectIdentity
hm2NtpGeneralGroup=_Hm2NtpGeneralGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,3,1))
class _Hm2NtpOperatingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_M,2),(_e,3),(_f,4),(_g,5)))
_Hm2NtpOperatingState_Type.__name__=_C
_Hm2NtpOperatingState_Object=MibScalar
hm2NtpOperatingState=_Hm2NtpOperatingState_Object((1,3,6,1,4,1,248,11,50,1,3,1,1),_Hm2NtpOperatingState_Type())
hm2NtpOperatingState.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NtpOperatingState.setStatus(_A)
_Hm2NtpServerGroup_ObjectIdentity=ObjectIdentity
hm2NtpServerGroup=_Hm2NtpServerGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,3,2))
_Hm2NtpServerConfigGroup_ObjectIdentity=ObjectIdentity
hm2NtpServerConfigGroup=_Hm2NtpServerConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,3,2,1))
class _Hm2NtpServerAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2NtpServerAdminState_Type.__name__=_F
_Hm2NtpServerAdminState_Object=MibScalar
hm2NtpServerAdminState=_Hm2NtpServerAdminState_Object((1,3,6,1,4,1,248,11,50,1,3,2,1,1),_Hm2NtpServerAdminState_Type())
hm2NtpServerAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2NtpServerAdminState.setStatus(_A)
class _Hm2NtpServerOperatingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('symmetric',1),('client-server',2)))
_Hm2NtpServerOperatingMode_Type.__name__=_C
_Hm2NtpServerOperatingMode_Object=MibScalar
hm2NtpServerOperatingMode=_Hm2NtpServerOperatingMode_Object((1,3,6,1,4,1,248,11,50,1,3,2,1,2),_Hm2NtpServerOperatingMode_Type())
hm2NtpServerOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2NtpServerOperatingMode.setStatus(_A)
class _Hm2NtpServerLocalClockStratum_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Hm2NtpServerLocalClockStratum_Type.__name__=_C
_Hm2NtpServerLocalClockStratum_Object=MibScalar
hm2NtpServerLocalClockStratum=_Hm2NtpServerLocalClockStratum_Object((1,3,6,1,4,1,248,11,50,1,3,2,1,3),_Hm2NtpServerLocalClockStratum_Type())
hm2NtpServerLocalClockStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2NtpServerLocalClockStratum.setStatus(_A)
_Hm2NtpClientGroup_ObjectIdentity=ObjectIdentity
hm2NtpClientGroup=_Hm2NtpClientGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,3,3))
_Hm2NtpClientConfigGroup_ObjectIdentity=ObjectIdentity
hm2NtpClientConfigGroup=_Hm2NtpClientConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,3,3,1))
class _Hm2NtpClientAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2NtpClientAdminState_Type.__name__=_F
_Hm2NtpClientAdminState_Object=MibScalar
hm2NtpClientAdminState=_Hm2NtpClientAdminState_Object((1,3,6,1,4,1,248,11,50,1,3,3,1,1),_Hm2NtpClientAdminState_Type())
hm2NtpClientAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2NtpClientAdminState.setStatus(_A)
class _Hm2NtpClientOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_j,2)))
_Hm2NtpClientOperatingMode_Type.__name__=_C
_Hm2NtpClientOperatingMode_Object=MibScalar
hm2NtpClientOperatingMode=_Hm2NtpClientOperatingMode_Object((1,3,6,1,4,1,248,11,50,1,3,3,1,2),_Hm2NtpClientOperatingMode_Type())
hm2NtpClientOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2NtpClientOperatingMode.setStatus(_A)
_Hm2NtpClientServerAddrTable_Object=MibTable
hm2NtpClientServerAddrTable=_Hm2NtpClientServerAddrTable_Object((1,3,6,1,4,1,248,11,50,1,3,3,4))
if mibBuilder.loadTexts:hm2NtpClientServerAddrTable.setStatus(_A)
_Hm2NtpClientServerAddrEntry_Object=MibTableRow
hm2NtpClientServerAddrEntry=_Hm2NtpClientServerAddrEntry_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1))
hm2NtpClientServerAddrEntry.setIndexNames((0,_H,_l))
if mibBuilder.loadTexts:hm2NtpClientServerAddrEntry.setStatus(_A)
class _Hm2NtpClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2NtpClientServerIndex_Type.__name__=_C
_Hm2NtpClientServerIndex_Object=MibTableColumn
hm2NtpClientServerIndex=_Hm2NtpClientServerIndex_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,1),_Hm2NtpClientServerIndex_Type())
hm2NtpClientServerIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:hm2NtpClientServerIndex.setStatus(_A)
class _Hm2NtpClientServerAddressType_Type(InetAddressType):defaultValue=1
_Hm2NtpClientServerAddressType_Type.__name__=_L
_Hm2NtpClientServerAddressType_Object=MibTableColumn
hm2NtpClientServerAddressType=_Hm2NtpClientServerAddressType_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,2),_Hm2NtpClientServerAddressType_Type())
hm2NtpClientServerAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerAddressType.setStatus(_A)
class _Hm2NtpClientServerAddress_Type(InetAddress):defaultHexValue=_N
_Hm2NtpClientServerAddress_Type.__name__=_K
_Hm2NtpClientServerAddress_Object=MibTableColumn
hm2NtpClientServerAddress=_Hm2NtpClientServerAddress_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,3),_Hm2NtpClientServerAddress_Type())
hm2NtpClientServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerAddress.setStatus(_A)
class _Hm2NtpClientServerPort_Type(InetPortNumber):defaultValue=123
_Hm2NtpClientServerPort_Type.__name__=_J
_Hm2NtpClientServerPort_Object=MibTableColumn
hm2NtpClientServerPort=_Hm2NtpClientServerPort_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,4),_Hm2NtpClientServerPort_Type())
hm2NtpClientServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerPort.setStatus(_A)
class _Hm2NtpClientServerInitialBurst_Type(HmEnabledStatus):defaultValue=2
_Hm2NtpClientServerInitialBurst_Type.__name__=_F
_Hm2NtpClientServerInitialBurst_Object=MibTableColumn
hm2NtpClientServerInitialBurst=_Hm2NtpClientServerInitialBurst_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,5),_Hm2NtpClientServerInitialBurst_Type())
hm2NtpClientServerInitialBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerInitialBurst.setStatus(_A)
class _Hm2NtpClientServerBurst_Type(HmEnabledStatus):defaultValue=2
_Hm2NtpClientServerBurst_Type.__name__=_F
_Hm2NtpClientServerBurst_Object=MibTableColumn
hm2NtpClientServerBurst=_Hm2NtpClientServerBurst_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,6),_Hm2NtpClientServerBurst_Type())
hm2NtpClientServerBurst.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerBurst.setStatus(_A)
class _Hm2NtpClientServerPrefer_Type(TruthValue):defaultValue=2
_Hm2NtpClientServerPrefer_Type.__name__=_I
_Hm2NtpClientServerPrefer_Object=MibTableColumn
hm2NtpClientServerPrefer=_Hm2NtpClientServerPrefer_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,7),_Hm2NtpClientServerPrefer_Type())
hm2NtpClientServerPrefer.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerPrefer.setStatus(_A)
class _Hm2NtpClientServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_m,2),(_M,3),(_n,4),(_o,5),(_p,6),(_q,7)))
_Hm2NtpClientServerStatus_Type.__name__=_C
_Hm2NtpClientServerStatus_Object=MibTableColumn
hm2NtpClientServerStatus=_Hm2NtpClientServerStatus_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,10),_Hm2NtpClientServerStatus_Type())
hm2NtpClientServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NtpClientServerStatus.setStatus(_A)
_Hm2NtpClientServerRowStatus_Type=RowStatus
_Hm2NtpClientServerRowStatus_Object=MibTableColumn
hm2NtpClientServerRowStatus=_Hm2NtpClientServerRowStatus_Object((1,3,6,1,4,1,248,11,50,1,3,3,4,1,11),_Hm2NtpClientServerRowStatus_Type())
hm2NtpClientServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientServerRowStatus.setStatus(_A)
_Hm2NtpClientListenAddrTable_Object=MibTable
hm2NtpClientListenAddrTable=_Hm2NtpClientListenAddrTable_Object((1,3,6,1,4,1,248,11,50,1,3,3,5))
if mibBuilder.loadTexts:hm2NtpClientListenAddrTable.setStatus(_A)
_Hm2NtpClientListenAddrEntry_Object=MibTableRow
hm2NtpClientListenAddrEntry=_Hm2NtpClientListenAddrEntry_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1))
hm2NtpClientListenAddrEntry.setIndexNames((0,_H,_r))
if mibBuilder.loadTexts:hm2NtpClientListenAddrEntry.setStatus(_A)
class _Hm2NtpClientListenAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Hm2NtpClientListenAddrIndex_Type.__name__=_C
_Hm2NtpClientListenAddrIndex_Object=MibTableColumn
hm2NtpClientListenAddrIndex=_Hm2NtpClientListenAddrIndex_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1,1),_Hm2NtpClientListenAddrIndex_Type())
hm2NtpClientListenAddrIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:hm2NtpClientListenAddrIndex.setStatus(_A)
class _Hm2NtpClientListenAddrAddressType_Type(InetAddressType):defaultValue=1
_Hm2NtpClientListenAddrAddressType_Type.__name__=_L
_Hm2NtpClientListenAddrAddressType_Object=MibTableColumn
hm2NtpClientListenAddrAddressType=_Hm2NtpClientListenAddrAddressType_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1,2),_Hm2NtpClientListenAddrAddressType_Type())
hm2NtpClientListenAddrAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientListenAddrAddressType.setStatus(_A)
class _Hm2NtpClientListenAddrAddress_Type(InetAddress):defaultHexValue=_N
_Hm2NtpClientListenAddrAddress_Type.__name__=_K
_Hm2NtpClientListenAddrAddress_Object=MibTableColumn
hm2NtpClientListenAddrAddress=_Hm2NtpClientListenAddrAddress_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1,3),_Hm2NtpClientListenAddrAddress_Type())
hm2NtpClientListenAddrAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientListenAddrAddress.setStatus(_A)
class _Hm2NtpClientListenAddrPort_Type(InetPortNumber):defaultValue=123
_Hm2NtpClientListenAddrPort_Type.__name__=_J
_Hm2NtpClientListenAddrPort_Object=MibTableColumn
hm2NtpClientListenAddrPort=_Hm2NtpClientListenAddrPort_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1,4),_Hm2NtpClientListenAddrPort_Type())
hm2NtpClientListenAddrPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientListenAddrPort.setStatus(_A)
class _Hm2NtpClientListenAddrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),(_m,2),(_M,3),(_n,4),(_o,5),(_p,6),(_q,7)))
_Hm2NtpClientListenAddrStatus_Type.__name__=_C
_Hm2NtpClientListenAddrStatus_Object=MibTableColumn
hm2NtpClientListenAddrStatus=_Hm2NtpClientListenAddrStatus_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1,10),_Hm2NtpClientListenAddrStatus_Type())
hm2NtpClientListenAddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2NtpClientListenAddrStatus.setStatus(_A)
_Hm2NtpClientListenAddrRowStatus_Type=RowStatus
_Hm2NtpClientListenAddrRowStatus_Object=MibTableColumn
hm2NtpClientListenAddrRowStatus=_Hm2NtpClientListenAddrRowStatus_Object((1,3,6,1,4,1,248,11,50,1,3,3,5,1,11),_Hm2NtpClientListenAddrRowStatus_Type())
hm2NtpClientListenAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2NtpClientListenAddrRowStatus.setStatus(_A)
_Hm2PtpGroup_ObjectIdentity=ObjectIdentity
hm2PtpGroup=_Hm2PtpGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,4))
_Hm2PtpGlobal_ObjectIdentity=ObjectIdentity
hm2PtpGlobal=_Hm2PtpGlobal_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,4,1))
class _Hm2PtpEnable_Type(HmEnabledStatus):defaultValue=2
_Hm2PtpEnable_Type.__name__=_F
_Hm2PtpEnable_Object=MibScalar
hm2PtpEnable=_Hm2PtpEnable_Object((1,3,6,1,4,1,248,11,50,1,4,1,1),_Hm2PtpEnable_Type())
hm2PtpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PtpEnable.setStatus(_A)
class _Hm2PtpClockMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('v2-boundary-clock',2),('v2-transparent-clock',3)))
_Hm2PtpClockMode_Type.__name__=_C
_Hm2PtpClockMode_Object=MibScalar
hm2PtpClockMode=_Hm2PtpClockMode_Object((1,3,6,1,4,1,248,11,50,1,4,1,2),_Hm2PtpClockMode_Type())
hm2PtpClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PtpClockMode.setStatus(_A)
class _Hm2PtpProfile_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user-defined',1),('default-e2e',2),('default-p2p',3)))
_Hm2PtpProfile_Type.__name__=_C
_Hm2PtpProfile_Object=MibScalar
hm2PtpProfile=_Hm2PtpProfile_Object((1,3,6,1,4,1,248,11,50,1,4,1,3),_Hm2PtpProfile_Type())
hm2PtpProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PtpProfile.setStatus(_A)
class _Hm2PtpIsSynchronized_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hm2PtpIsSynchronized_Type.__name__=_C
_Hm2PtpIsSynchronized_Object=MibScalar
hm2PtpIsSynchronized=_Hm2PtpIsSynchronized_Object((1,3,6,1,4,1,248,11,50,1,4,1,4),_Hm2PtpIsSynchronized_Type())
hm2PtpIsSynchronized.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2PtpIsSynchronized.setStatus(_A)
class _Hm2PtpSyncLowerBound_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999999))
_Hm2PtpSyncLowerBound_Type.__name__=_C
_Hm2PtpSyncLowerBound_Object=MibScalar
hm2PtpSyncLowerBound=_Hm2PtpSyncLowerBound_Object((1,3,6,1,4,1,248,11,50,1,4,1,5),_Hm2PtpSyncLowerBound_Type())
hm2PtpSyncLowerBound.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PtpSyncLowerBound.setStatus(_A)
class _Hm2PtpSyncUpperBound_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(31,1000000000))
_Hm2PtpSyncUpperBound_Type.__name__=_C
_Hm2PtpSyncUpperBound_Object=MibScalar
hm2PtpSyncUpperBound=_Hm2PtpSyncUpperBound_Object((1,3,6,1,4,1,248,11,50,1,4,1,6),_Hm2PtpSyncUpperBound_Type())
hm2PtpSyncUpperBound.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PtpSyncUpperBound.setStatus(_A)
_Hm2PtpAbsMaxOffset_Type=Integer32
_Hm2PtpAbsMaxOffset_Object=MibScalar
hm2PtpAbsMaxOffset=_Hm2PtpAbsMaxOffset_Object((1,3,6,1,4,1,248,11,50,1,4,1,7),_Hm2PtpAbsMaxOffset_Type())
hm2PtpAbsMaxOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2PtpAbsMaxOffset.setStatus(_A)
_Hm2PtpTimeSeconds_Type=PtpTimeStamp
_Hm2PtpTimeSeconds_Object=MibScalar
hm2PtpTimeSeconds=_Hm2PtpTimeSeconds_Object((1,3,6,1,4,1,248,11,50,1,4,1,8),_Hm2PtpTimeSeconds_Type())
hm2PtpTimeSeconds.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2PtpTimeSeconds.setStatus(_A)
class _Hm2PtpManagement_Type(TruthValue):defaultValue=2
_Hm2PtpManagement_Type.__name__=_I
_Hm2PtpManagement_Object=MibScalar
hm2PtpManagement=_Hm2PtpManagement_Object((1,3,6,1,4,1,248,11,50,1,4,1,9),_Hm2PtpManagement_Type())
hm2PtpManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PtpManagement.setStatus(_A)
_Hm2Ptp2Objects_ObjectIdentity=ObjectIdentity
hm2Ptp2Objects=_Hm2Ptp2Objects_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,4,2))
_Hm2Ptp2Configuration_ObjectIdentity=ObjectIdentity
hm2Ptp2Configuration=_Hm2Ptp2Configuration_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,4,2,1))
_Hm2Ptp2TwoStepClock_Type=TruthValue
_Hm2Ptp2TwoStepClock_Object=MibScalar
hm2Ptp2TwoStepClock=_Hm2Ptp2TwoStepClock_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,1),_Hm2Ptp2TwoStepClock_Type())
hm2Ptp2TwoStepClock.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TwoStepClock.setStatus(_A)
_Hm2Ptp2ClockIdentity_Type=PtpClockIdentity
_Hm2Ptp2ClockIdentity_Object=MibScalar
hm2Ptp2ClockIdentity=_Hm2Ptp2ClockIdentity_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,2),_Hm2Ptp2ClockIdentity_Type())
hm2Ptp2ClockIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ClockIdentity.setStatus(_A)
_Hm2Ptp2ClockQuality_Type=PtpClockQuality
_Hm2Ptp2ClockQuality_Object=MibScalar
hm2Ptp2ClockQuality=_Hm2Ptp2ClockQuality_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,3),_Hm2Ptp2ClockQuality_Type())
hm2Ptp2ClockQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ClockQuality.setStatus(_A)
class _Hm2Ptp2ClockClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2Ptp2ClockClass_Type.__name__=_C
_Hm2Ptp2ClockClass_Object=MibScalar
hm2Ptp2ClockClass=_Hm2Ptp2ClockClass_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,4),_Hm2Ptp2ClockClass_Type())
hm2Ptp2ClockClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ClockClass.setStatus(_A)
class _Hm2Ptp2ClockAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,254)));namedValues=NamedValues(*((_s,32),(_V,33),(_t,34),(_u,35),(_v,36),(_W,37),(_w,38),(_X,39),(_x,40),(_y,41),(_z,42),(_Y,43),(_A0,44),(_Z,45),(_A1,46),(_a,47),(_b,48),(_A2,49),('unknown',254)))
_Hm2Ptp2ClockAccuracy_Type.__name__=_C
_Hm2Ptp2ClockAccuracy_Object=MibScalar
hm2Ptp2ClockAccuracy=_Hm2Ptp2ClockAccuracy_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,5),_Hm2Ptp2ClockAccuracy_Type())
hm2Ptp2ClockAccuracy.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ClockAccuracy.setStatus(_A)
_Hm2Ptp2ClockVariance_Type=Integer32
_Hm2Ptp2ClockVariance_Object=MibScalar
hm2Ptp2ClockVariance=_Hm2Ptp2ClockVariance_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,6),_Hm2Ptp2ClockVariance_Type())
hm2Ptp2ClockVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ClockVariance.setStatus(_A)
class _Hm2Ptp2Priority1_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2Ptp2Priority1_Type.__name__=_C
_Hm2Ptp2Priority1_Object=MibScalar
hm2Ptp2Priority1=_Hm2Ptp2Priority1_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,7),_Hm2Ptp2Priority1_Type())
hm2Ptp2Priority1.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2Priority1.setStatus(_A)
class _Hm2Ptp2Priority2_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2Ptp2Priority2_Type.__name__=_C
_Hm2Ptp2Priority2_Object=MibScalar
hm2Ptp2Priority2=_Hm2Ptp2Priority2_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,8),_Hm2Ptp2Priority2_Type())
hm2Ptp2Priority2.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2Priority2.setStatus(_A)
class _Hm2Ptp2DomainNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2Ptp2DomainNumber_Type.__name__=_C
_Hm2Ptp2DomainNumber_Object=MibScalar
hm2Ptp2DomainNumber=_Hm2Ptp2DomainNumber_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,9),_Hm2Ptp2DomainNumber_Type())
hm2Ptp2DomainNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2DomainNumber.setStatus(_A)
_Hm2Ptp2StepsRemoved_Type=Integer32
_Hm2Ptp2StepsRemoved_Object=MibScalar
hm2Ptp2StepsRemoved=_Hm2Ptp2StepsRemoved_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,10),_Hm2Ptp2StepsRemoved_Type())
hm2Ptp2StepsRemoved.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2StepsRemoved.setStatus(_A)
_Hm2Ptp2OffsetFromMaster_Type=PtpTimeInterval
_Hm2Ptp2OffsetFromMaster_Object=MibScalar
hm2Ptp2OffsetFromMaster=_Hm2Ptp2OffsetFromMaster_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,11),_Hm2Ptp2OffsetFromMaster_Type())
hm2Ptp2OffsetFromMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2OffsetFromMaster.setStatus(_A)
_Hm2Ptp2MeanPathDelay_Type=PtpTimeInterval
_Hm2Ptp2MeanPathDelay_Object=MibScalar
hm2Ptp2MeanPathDelay=_Hm2Ptp2MeanPathDelay_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,12),_Hm2Ptp2MeanPathDelay_Type())
hm2Ptp2MeanPathDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2MeanPathDelay.setStatus(_A)
_Hm2Ptp2ParentPortIdentity_Type=PtpPortIdentity
_Hm2Ptp2ParentPortIdentity_Object=MibScalar
hm2Ptp2ParentPortIdentity=_Hm2Ptp2ParentPortIdentity_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,13),_Hm2Ptp2ParentPortIdentity_Type())
hm2Ptp2ParentPortIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ParentPortIdentity.setStatus(_A)
_Hm2Ptp2ParentStats_Type=TruthValue
_Hm2Ptp2ParentStats_Object=MibScalar
hm2Ptp2ParentStats=_Hm2Ptp2ParentStats_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,14),_Hm2Ptp2ParentStats_Type())
hm2Ptp2ParentStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ParentStats.setStatus(_A)
_Hm2Ptp2ObservedParentOffsetScaledLogVariance_Type=Integer32
_Hm2Ptp2ObservedParentOffsetScaledLogVariance_Object=MibScalar
hm2Ptp2ObservedParentOffsetScaledLogVariance=_Hm2Ptp2ObservedParentOffsetScaledLogVariance_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,15),_Hm2Ptp2ObservedParentOffsetScaledLogVariance_Type())
hm2Ptp2ObservedParentOffsetScaledLogVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ObservedParentOffsetScaledLogVariance.setStatus(_A)
_Hm2Ptp2ObservedParentClockPhaseChangeRate_Type=Integer32
_Hm2Ptp2ObservedParentClockPhaseChangeRate_Object=MibScalar
hm2Ptp2ObservedParentClockPhaseChangeRate=_Hm2Ptp2ObservedParentClockPhaseChangeRate_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,16),_Hm2Ptp2ObservedParentClockPhaseChangeRate_Type())
hm2Ptp2ObservedParentClockPhaseChangeRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2ObservedParentClockPhaseChangeRate.setStatus(_A)
_Hm2Ptp2GrandmasterIdentity_Type=PtpClockIdentity
_Hm2Ptp2GrandmasterIdentity_Object=MibScalar
hm2Ptp2GrandmasterIdentity=_Hm2Ptp2GrandmasterIdentity_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,17),_Hm2Ptp2GrandmasterIdentity_Type())
hm2Ptp2GrandmasterIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterIdentity.setStatus(_A)
_Hm2Ptp2GrandmasterClockQuality_Type=PtpClockQuality
_Hm2Ptp2GrandmasterClockQuality_Object=MibScalar
hm2Ptp2GrandmasterClockQuality=_Hm2Ptp2GrandmasterClockQuality_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,18),_Hm2Ptp2GrandmasterClockQuality_Type())
hm2Ptp2GrandmasterClockQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterClockQuality.setStatus(_A)
class _Hm2Ptp2GrandmasterClockClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2Ptp2GrandmasterClockClass_Type.__name__=_C
_Hm2Ptp2GrandmasterClockClass_Object=MibScalar
hm2Ptp2GrandmasterClockClass=_Hm2Ptp2GrandmasterClockClass_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,19),_Hm2Ptp2GrandmasterClockClass_Type())
hm2Ptp2GrandmasterClockClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterClockClass.setStatus(_A)
class _Hm2Ptp2GrandmasterClockAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,254)));namedValues=NamedValues(*((_s,32),(_V,33),(_t,34),(_u,35),(_v,36),(_W,37),(_w,38),(_X,39),(_x,40),(_y,41),(_z,42),(_Y,43),(_A0,44),(_Z,45),(_A1,46),(_a,47),(_b,48),(_A2,49),('unknown',254)))
_Hm2Ptp2GrandmasterClockAccuracy_Type.__name__=_C
_Hm2Ptp2GrandmasterClockAccuracy_Object=MibScalar
hm2Ptp2GrandmasterClockAccuracy=_Hm2Ptp2GrandmasterClockAccuracy_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,20),_Hm2Ptp2GrandmasterClockAccuracy_Type())
hm2Ptp2GrandmasterClockAccuracy.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterClockAccuracy.setStatus(_A)
_Hm2Ptp2GrandmasterClockVariance_Type=Integer32
_Hm2Ptp2GrandmasterClockVariance_Object=MibScalar
hm2Ptp2GrandmasterClockVariance=_Hm2Ptp2GrandmasterClockVariance_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,21),_Hm2Ptp2GrandmasterClockVariance_Type())
hm2Ptp2GrandmasterClockVariance.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterClockVariance.setStatus(_A)
_Hm2Ptp2GrandmasterPriority1_Type=Integer32
_Hm2Ptp2GrandmasterPriority1_Object=MibScalar
hm2Ptp2GrandmasterPriority1=_Hm2Ptp2GrandmasterPriority1_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,22),_Hm2Ptp2GrandmasterPriority1_Type())
hm2Ptp2GrandmasterPriority1.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterPriority1.setStatus(_A)
_Hm2Ptp2GrandmasterPriority2_Type=Integer32
_Hm2Ptp2GrandmasterPriority2_Object=MibScalar
hm2Ptp2GrandmasterPriority2=_Hm2Ptp2GrandmasterPriority2_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,23),_Hm2Ptp2GrandmasterPriority2_Type())
hm2Ptp2GrandmasterPriority2.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2GrandmasterPriority2.setStatus(_A)
class _Hm2Ptp2CurrentUtcOffset_Type(Integer32):defaultValue=37;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
_Hm2Ptp2CurrentUtcOffset_Type.__name__=_C
_Hm2Ptp2CurrentUtcOffset_Object=MibScalar
hm2Ptp2CurrentUtcOffset=_Hm2Ptp2CurrentUtcOffset_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,24),_Hm2Ptp2CurrentUtcOffset_Type())
hm2Ptp2CurrentUtcOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2CurrentUtcOffset.setStatus(_A)
class _Hm2Ptp2CurrentUtcOffsetValid_Type(TruthValue):defaultValue=2
_Hm2Ptp2CurrentUtcOffsetValid_Type.__name__=_I
_Hm2Ptp2CurrentUtcOffsetValid_Object=MibScalar
hm2Ptp2CurrentUtcOffsetValid=_Hm2Ptp2CurrentUtcOffsetValid_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,25),_Hm2Ptp2CurrentUtcOffsetValid_Type())
hm2Ptp2CurrentUtcOffsetValid.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2CurrentUtcOffsetValid.setStatus(_A)
_Hm2Ptp2Leap59_Type=TruthValue
_Hm2Ptp2Leap59_Object=MibScalar
hm2Ptp2Leap59=_Hm2Ptp2Leap59_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,26),_Hm2Ptp2Leap59_Type())
hm2Ptp2Leap59.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2Leap59.setStatus(_A)
_Hm2Ptp2Leap61_Type=TruthValue
_Hm2Ptp2Leap61_Object=MibScalar
hm2Ptp2Leap61=_Hm2Ptp2Leap61_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,27),_Hm2Ptp2Leap61_Type())
hm2Ptp2Leap61.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2Leap61.setStatus(_A)
_Hm2Ptp2TimeTraceable_Type=TruthValue
_Hm2Ptp2TimeTraceable_Object=MibScalar
hm2Ptp2TimeTraceable=_Hm2Ptp2TimeTraceable_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,28),_Hm2Ptp2TimeTraceable_Type())
hm2Ptp2TimeTraceable.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TimeTraceable.setStatus(_A)
_Hm2Ptp2FrequencyTraceable_Type=TruthValue
_Hm2Ptp2FrequencyTraceable_Object=MibScalar
hm2Ptp2FrequencyTraceable=_Hm2Ptp2FrequencyTraceable_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,29),_Hm2Ptp2FrequencyTraceable_Type())
hm2Ptp2FrequencyTraceable.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2FrequencyTraceable.setStatus(_A)
_Hm2Ptp2PtpTimescale_Type=TruthValue
_Hm2Ptp2PtpTimescale_Object=MibScalar
hm2Ptp2PtpTimescale=_Hm2Ptp2PtpTimescale_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,30),_Hm2Ptp2PtpTimescale_Type())
hm2Ptp2PtpTimescale.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2PtpTimescale.setStatus(_A)
class _Hm2Ptp2TimeSource_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,48,64,80,96,144,160)));namedValues=NamedValues(*(('atomicClock',16),('gps',32),('terrestrialRadio',48),('ptp',64),('ntp',80),('handSet',96),('other',144),('internalOscillator',160)))
_Hm2Ptp2TimeSource_Type.__name__=_C
_Hm2Ptp2TimeSource_Object=MibScalar
hm2Ptp2TimeSource=_Hm2Ptp2TimeSource_Object((1,3,6,1,4,1,248,11,50,1,4,2,1,31),_Hm2Ptp2TimeSource_Type())
hm2Ptp2TimeSource.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TimeSource.setStatus(_A)
_Hm2Ptp2PortTable_Object=MibTable
hm2Ptp2PortTable=_Hm2Ptp2PortTable_Object((1,3,6,1,4,1,248,11,50,1,4,2,2))
if mibBuilder.loadTexts:hm2Ptp2PortTable.setStatus(_A)
_Hm2Ptp2PortEntry_Object=MibTableRow
hm2Ptp2PortEntry=_Hm2Ptp2PortEntry_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1))
hm2Ptp2PortEntry.setIndexNames((0,_O,_Q))
if mibBuilder.loadTexts:hm2Ptp2PortEntry.setStatus(_A)
class _Hm2Ptp2PortEnable_Type(HmEnabledStatus):defaultValue=1
_Hm2Ptp2PortEnable_Type.__name__=_F
_Hm2Ptp2PortEnable_Object=MibTableColumn
hm2Ptp2PortEnable=_Hm2Ptp2PortEnable_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,1),_Hm2Ptp2PortEnable_Type())
hm2Ptp2PortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2PortEnable.setStatus(_A)
class _Hm2Ptp2PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('initializing',1),('faulty',2),(_G,3),('listening',4),('pre-master',5),('master',6),('passive',7),('uncalibrated',8),('slave',9)))
_Hm2Ptp2PortState_Type.__name__=_C
_Hm2Ptp2PortState_Object=MibTableColumn
hm2Ptp2PortState=_Hm2Ptp2PortState_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,2),_Hm2Ptp2PortState_Type())
hm2Ptp2PortState.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2PortState.setStatus(_A)
_Hm2Ptp2LogDelayReqInterval_Type=Integer32
_Hm2Ptp2LogDelayReqInterval_Object=MibTableColumn
hm2Ptp2LogDelayReqInterval=_Hm2Ptp2LogDelayReqInterval_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,3),_Hm2Ptp2LogDelayReqInterval_Type())
hm2Ptp2LogDelayReqInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2LogDelayReqInterval.setStatus(_A)
_Hm2Ptp2PeerMeanPathDelay_Type=PtpTimeInterval
_Hm2Ptp2PeerMeanPathDelay_Object=MibTableColumn
hm2Ptp2PeerMeanPathDelay=_Hm2Ptp2PeerMeanPathDelay_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,4),_Hm2Ptp2PeerMeanPathDelay_Type())
hm2Ptp2PeerMeanPathDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2PeerMeanPathDelay.setStatus(_A)
class _Hm2Ptp2LogAnnounceInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_S,0),(_T,1),('sec-4',2),('sec-8',3),(_d,4)))
_Hm2Ptp2LogAnnounceInterval_Type.__name__=_C
_Hm2Ptp2LogAnnounceInterval_Object=MibTableColumn
hm2Ptp2LogAnnounceInterval=_Hm2Ptp2LogAnnounceInterval_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,5),_Hm2Ptp2LogAnnounceInterval_Type())
hm2Ptp2LogAnnounceInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2LogAnnounceInterval.setStatus(_A)
class _Hm2Ptp2AnnounceReceiptTimeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_Hm2Ptp2AnnounceReceiptTimeout_Type.__name__=_C
_Hm2Ptp2AnnounceReceiptTimeout_Object=MibTableColumn
hm2Ptp2AnnounceReceiptTimeout=_Hm2Ptp2AnnounceReceiptTimeout_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,6),_Hm2Ptp2AnnounceReceiptTimeout_Type())
hm2Ptp2AnnounceReceiptTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2AnnounceReceiptTimeout.setStatus(_A)
class _Hm2Ptp2LogSyncInterval_Type(Hm2Ptp2LogSyncIntervalTc):defaultValue=0
_Hm2Ptp2LogSyncInterval_Type.__name__=_A3
_Hm2Ptp2LogSyncInterval_Object=MibTableColumn
hm2Ptp2LogSyncInterval=_Hm2Ptp2LogSyncInterval_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,7),_Hm2Ptp2LogSyncInterval_Type())
hm2Ptp2LogSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2LogSyncInterval.setStatus(_A)
class _Hm2Ptp2DelayMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254)));namedValues=NamedValues(*(('e2e',1),('p2p',2),(_G,254)))
_Hm2Ptp2DelayMechanism_Type.__name__=_C
_Hm2Ptp2DelayMechanism_Object=MibTableColumn
hm2Ptp2DelayMechanism=_Hm2Ptp2DelayMechanism_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,8),_Hm2Ptp2DelayMechanism_Type())
hm2Ptp2DelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2DelayMechanism.setStatus(_A)
class _Hm2Ptp2LogPdelayReqInterval_Type(Hm2Ptp2LogPdelayReqIntervalTc):defaultValue=0
_Hm2Ptp2LogPdelayReqInterval_Type.__name__=_c
_Hm2Ptp2LogPdelayReqInterval_Object=MibTableColumn
hm2Ptp2LogPdelayReqInterval=_Hm2Ptp2LogPdelayReqInterval_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,9),_Hm2Ptp2LogPdelayReqInterval_Type())
hm2Ptp2LogPdelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2LogPdelayReqInterval.setStatus(_A)
class _Hm2Ptp2VersionNumber_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ptpVersion1',1),('ptpVersion2',2)))
_Hm2Ptp2VersionNumber_Type.__name__=_C
_Hm2Ptp2VersionNumber_Object=MibTableColumn
hm2Ptp2VersionNumber=_Hm2Ptp2VersionNumber_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,10),_Hm2Ptp2VersionNumber_Type())
hm2Ptp2VersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2VersionNumber.setStatus(_A)
class _Hm2Ptp2NetworkProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('udpIpv4',1),('ieee8023',3)))
_Hm2Ptp2NetworkProtocol_Type.__name__=_C
_Hm2Ptp2NetworkProtocol_Object=MibTableColumn
hm2Ptp2NetworkProtocol=_Hm2Ptp2NetworkProtocol_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,11),_Hm2Ptp2NetworkProtocol_Type())
hm2Ptp2NetworkProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2NetworkProtocol.setStatus(_A)
class _Hm2Ptp2V1Compatibility_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('auto',3)))
_Hm2Ptp2V1Compatibility_Type.__name__=_C
_Hm2Ptp2V1Compatibility_Object=MibTableColumn
hm2Ptp2V1Compatibility=_Hm2Ptp2V1Compatibility_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,12),_Hm2Ptp2V1Compatibility_Type())
hm2Ptp2V1Compatibility.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2V1Compatibility.setStatus(_A)
class _Hm2Ptp2DelayAsymmetry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000000000,2000000000))
_Hm2Ptp2DelayAsymmetry_Type.__name__=_C
_Hm2Ptp2DelayAsymmetry_Object=MibTableColumn
hm2Ptp2DelayAsymmetry=_Hm2Ptp2DelayAsymmetry_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,13),_Hm2Ptp2DelayAsymmetry_Type())
hm2Ptp2DelayAsymmetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2DelayAsymmetry.setStatus(_A)
class _Hm2Ptp2PortCapability_Type(Bits):namedValues=NamedValues(*(('reserved',0),('one-step',1),(_A4,2),(_A5,3),(_A6,4),(_A7,5),(_A8,6),(_A9,7),(_AA,8),('ptp2UdpE2EGlobal',9)))
_Hm2Ptp2PortCapability_Type.__name__=_R
_Hm2Ptp2PortCapability_Object=MibTableColumn
hm2Ptp2PortCapability=_Hm2Ptp2PortCapability_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,14),_Hm2Ptp2PortCapability_Type())
hm2Ptp2PortCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2PortCapability.setStatus(_A)
class _Hm2Ptp2VlanID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4042))
_Hm2Ptp2VlanID_Type.__name__=_C
_Hm2Ptp2VlanID_Object=MibTableColumn
hm2Ptp2VlanID=_Hm2Ptp2VlanID_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,15),_Hm2Ptp2VlanID_Type())
hm2Ptp2VlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2VlanID.setStatus(_A)
class _Hm2Ptp2VlanPriority_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2Ptp2VlanPriority_Type.__name__=_C
_Hm2Ptp2VlanPriority_Object=MibTableColumn
hm2Ptp2VlanPriority=_Hm2Ptp2VlanPriority_Object((1,3,6,1,4,1,248,11,50,1,4,2,2,1,16),_Hm2Ptp2VlanPriority_Type())
hm2Ptp2VlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2VlanPriority.setStatus(_A)
_Hm2Ptp2TCObjects_ObjectIdentity=ObjectIdentity
hm2Ptp2TCObjects=_Hm2Ptp2TCObjects_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,4,3))
_Hm2Ptp2TCConfiguration_ObjectIdentity=ObjectIdentity
hm2Ptp2TCConfiguration=_Hm2Ptp2TCConfiguration_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,4,3,1))
_Hm2Ptp2TCClockIdentity_Type=PtpClockIdentity
_Hm2Ptp2TCClockIdentity_Object=MibScalar
hm2Ptp2TCClockIdentity=_Hm2Ptp2TCClockIdentity_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,1),_Hm2Ptp2TCClockIdentity_Type())
hm2Ptp2TCClockIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCClockIdentity.setStatus(_A)
class _Hm2Ptp2TCDelayMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,254)));namedValues=NamedValues(*(('e2e',1),('p2p',2),('e2e-optimized',3),(_G,254)))
_Hm2Ptp2TCDelayMechanism_Type.__name__=_C
_Hm2Ptp2TCDelayMechanism_Object=MibScalar
hm2Ptp2TCDelayMechanism=_Hm2Ptp2TCDelayMechanism_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,2),_Hm2Ptp2TCDelayMechanism_Type())
hm2Ptp2TCDelayMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCDelayMechanism.setStatus(_A)
class _Hm2Ptp2TCPrimaryDomain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Hm2Ptp2TCPrimaryDomain_Type.__name__=_C
_Hm2Ptp2TCPrimaryDomain_Object=MibScalar
hm2Ptp2TCPrimaryDomain=_Hm2Ptp2TCPrimaryDomain_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,3),_Hm2Ptp2TCPrimaryDomain_Type())
hm2Ptp2TCPrimaryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCPrimaryDomain.setStatus(_A)
class _Hm2Ptp2TCSyntonized_Type(TruthValue):defaultValue=1
_Hm2Ptp2TCSyntonized_Type.__name__=_I
_Hm2Ptp2TCSyntonized_Object=MibScalar
hm2Ptp2TCSyntonized=_Hm2Ptp2TCSyntonized_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,4),_Hm2Ptp2TCSyntonized_Type())
hm2Ptp2TCSyntonized.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCSyntonized.setStatus(_A)
class _Hm2Ptp2TCNetworkProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('udpIpv4',1),('ieee8023',3)))
_Hm2Ptp2TCNetworkProtocol_Type.__name__=_C
_Hm2Ptp2TCNetworkProtocol_Object=MibScalar
hm2Ptp2TCNetworkProtocol=_Hm2Ptp2TCNetworkProtocol_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,5),_Hm2Ptp2TCNetworkProtocol_Type())
hm2Ptp2TCNetworkProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCNetworkProtocol.setStatus(_A)
_Hm2Ptp2TCCurrentMaster_Type=PtpPortIdentity
_Hm2Ptp2TCCurrentMaster_Object=MibScalar
hm2Ptp2TCCurrentMaster=_Hm2Ptp2TCCurrentMaster_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,6),_Hm2Ptp2TCCurrentMaster_Type())
hm2Ptp2TCCurrentMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCCurrentMaster.setStatus(_A)
class _Hm2Ptp2TCMultiDomainMode_Type(TruthValue):defaultValue=2
_Hm2Ptp2TCMultiDomainMode_Type.__name__=_I
_Hm2Ptp2TCMultiDomainMode_Object=MibScalar
hm2Ptp2TCMultiDomainMode=_Hm2Ptp2TCMultiDomainMode_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,7),_Hm2Ptp2TCMultiDomainMode_Type())
hm2Ptp2TCMultiDomainMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCMultiDomainMode.setStatus(_A)
class _Hm2Ptp2TCSyncLocalClock_Type(TruthValue):defaultValue=2
_Hm2Ptp2TCSyncLocalClock_Type.__name__=_I
_Hm2Ptp2TCSyncLocalClock_Object=MibScalar
hm2Ptp2TCSyncLocalClock=_Hm2Ptp2TCSyncLocalClock_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,8),_Hm2Ptp2TCSyncLocalClock_Type())
hm2Ptp2TCSyncLocalClock.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCSyncLocalClock.setStatus(_A)
_Hm2Ptp2TCOffsetFromMaster_Type=PtpTimeInterval
_Hm2Ptp2TCOffsetFromMaster_Object=MibScalar
hm2Ptp2TCOffsetFromMaster=_Hm2Ptp2TCOffsetFromMaster_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,9),_Hm2Ptp2TCOffsetFromMaster_Type())
hm2Ptp2TCOffsetFromMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCOffsetFromMaster.setStatus(_A)
_Hm2Ptp2TCMeanPathDelay_Type=PtpTimeInterval
_Hm2Ptp2TCMeanPathDelay_Object=MibScalar
hm2Ptp2TCMeanPathDelay=_Hm2Ptp2TCMeanPathDelay_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,10),_Hm2Ptp2TCMeanPathDelay_Type())
hm2Ptp2TCMeanPathDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCMeanPathDelay.setStatus(_A)
class _Hm2Ptp2TCVlanID_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_Hm2Ptp2TCVlanID_Type.__name__=_C
_Hm2Ptp2TCVlanID_Object=MibScalar
hm2Ptp2TCVlanID=_Hm2Ptp2TCVlanID_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,11),_Hm2Ptp2TCVlanID_Type())
hm2Ptp2TCVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCVlanID.setStatus(_A)
class _Hm2Ptp2TCVlanPriority_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2Ptp2TCVlanPriority_Type.__name__=_C
_Hm2Ptp2TCVlanPriority_Object=MibScalar
hm2Ptp2TCVlanPriority=_Hm2Ptp2TCVlanPriority_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,12),_Hm2Ptp2TCVlanPriority_Type())
hm2Ptp2TCVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCVlanPriority.setStatus(_A)
class _Hm2Ptp2TCCapability_Type(Bits):namedValues=NamedValues(*(('reserved',0),('one-step',1),(_A4,2),(_A5,3),(_A6,4),(_A7,5),(_A8,6),(_A9,7),(_AA,8)))
_Hm2Ptp2TCCapability_Type.__name__=_R
_Hm2Ptp2TCCapability_Object=MibScalar
hm2Ptp2TCCapability=_Hm2Ptp2TCCapability_Object((1,3,6,1,4,1,248,11,50,1,4,3,1,13),_Hm2Ptp2TCCapability_Type())
hm2Ptp2TCCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCCapability.setStatus(_A)
_Hm2Ptp2TCPortTable_Object=MibTable
hm2Ptp2TCPortTable=_Hm2Ptp2TCPortTable_Object((1,3,6,1,4,1,248,11,50,1,4,3,2))
if mibBuilder.loadTexts:hm2Ptp2TCPortTable.setStatus(_A)
_Hm2Ptp2TCPortEntry_Object=MibTableRow
hm2Ptp2TCPortEntry=_Hm2Ptp2TCPortEntry_Object((1,3,6,1,4,1,248,11,50,1,4,3,2,1))
hm2Ptp2TCPortEntry.setIndexNames((0,_O,_Q))
if mibBuilder.loadTexts:hm2Ptp2TCPortEntry.setStatus(_A)
class _Hm2Ptp2TCPortEnable_Type(HmEnabledStatus):defaultValue=1
_Hm2Ptp2TCPortEnable_Type.__name__=_F
_Hm2Ptp2TCPortEnable_Object=MibTableColumn
hm2Ptp2TCPortEnable=_Hm2Ptp2TCPortEnable_Object((1,3,6,1,4,1,248,11,50,1,4,3,2,1,1),_Hm2Ptp2TCPortEnable_Type())
hm2Ptp2TCPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCPortEnable.setStatus(_A)
class _Hm2Ptp2TCLogPdelayReqInterval_Type(Hm2Ptp2LogPdelayReqIntervalTc):defaultValue=0
_Hm2Ptp2TCLogPdelayReqInterval_Type.__name__=_c
_Hm2Ptp2TCLogPdelayReqInterval_Object=MibTableColumn
hm2Ptp2TCLogPdelayReqInterval=_Hm2Ptp2TCLogPdelayReqInterval_Object((1,3,6,1,4,1,248,11,50,1,4,3,2,1,2),_Hm2Ptp2TCLogPdelayReqInterval_Type())
hm2Ptp2TCLogPdelayReqInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCLogPdelayReqInterval.setStatus(_A)
_Hm2Ptp2TCFaulty_Type=TruthValue
_Hm2Ptp2TCFaulty_Object=MibTableColumn
hm2Ptp2TCFaulty=_Hm2Ptp2TCFaulty_Object((1,3,6,1,4,1,248,11,50,1,4,3,2,1,3),_Hm2Ptp2TCFaulty_Type())
hm2Ptp2TCFaulty.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCFaulty.setStatus(_A)
_Hm2Ptp2TCPeerMeanPathDelay_Type=PtpTimeInterval
_Hm2Ptp2TCPeerMeanPathDelay_Object=MibTableColumn
hm2Ptp2TCPeerMeanPathDelay=_Hm2Ptp2TCPeerMeanPathDelay_Object((1,3,6,1,4,1,248,11,50,1,4,3,2,1,4),_Hm2Ptp2TCPeerMeanPathDelay_Type())
hm2Ptp2TCPeerMeanPathDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Ptp2TCPeerMeanPathDelay.setStatus(_A)
class _Hm2Ptp2TCDelayAsymmetry_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2000000000,2000000000))
_Hm2Ptp2TCDelayAsymmetry_Type.__name__=_C
_Hm2Ptp2TCDelayAsymmetry_Object=MibTableColumn
hm2Ptp2TCDelayAsymmetry=_Hm2Ptp2TCDelayAsymmetry_Object((1,3,6,1,4,1,248,11,50,1,4,3,2,1,5),_Hm2Ptp2TCDelayAsymmetry_Type())
hm2Ptp2TCDelayAsymmetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Ptp2TCDelayAsymmetry.setStatus(_A)
_Hm2IrigGroup_ObjectIdentity=ObjectIdentity
hm2IrigGroup=_Hm2IrigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,5))
class _Hm2IrigAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2IrigAdminStatus_Type.__name__=_F
_Hm2IrigAdminStatus_Object=MibScalar
hm2IrigAdminStatus=_Hm2IrigAdminStatus_Object((1,3,6,1,4,1,248,11,50,1,5,1),_Hm2IrigAdminStatus_Type())
hm2IrigAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IrigAdminStatus.setStatus(_A)
class _Hm2IrigMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('irig-b000',0),('irig-b001',1),('irig-b002',2),('irig-b003',3),('irig-b004',4),('irig-b005',5),('irig-b006',6),('irig-b007',7)))
_Hm2IrigMode_Type.__name__=_C
_Hm2IrigMode_Object=MibScalar
hm2IrigMode=_Hm2IrigMode_Object((1,3,6,1,4,1,248,11,50,1,5,2),_Hm2IrigMode_Type())
hm2IrigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IrigMode.setStatus(_A)
class _Hm2IrigPpsAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2IrigPpsAdminStatus_Type.__name__=_F
_Hm2IrigPpsAdminStatus_Object=MibScalar
hm2IrigPpsAdminStatus=_Hm2IrigPpsAdminStatus_Object((1,3,6,1,4,1,248,11,50,1,5,3),_Hm2IrigPpsAdminStatus_Type())
hm2IrigPpsAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IrigPpsAdminStatus.setStatus(_A)
class _Hm2IrigTimeMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('utc',1),('local',2)))
_Hm2IrigTimeMode_Type.__name__=_C
_Hm2IrigTimeMode_Object=MibScalar
hm2IrigTimeMode=_Hm2IrigTimeMode_Object((1,3,6,1,4,1,248,11,50,1,5,4),_Hm2IrigTimeMode_Type())
hm2IrigTimeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2IrigTimeMode.setStatus(_A)
_Hm2IrigOperStatus_Type=HmEnabledStatus
_Hm2IrigOperStatus_Object=MibScalar
hm2IrigOperStatus=_Hm2IrigOperStatus_Object((1,3,6,1,4,1,248,11,50,1,5,5),_Hm2IrigOperStatus_Type())
hm2IrigOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2IrigOperStatus.setStatus(_A)
class _Hm2IrigTimeQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('locked',0),('within1ns',1),('within10ns',2),(_V,3),('within1us',4),(_W,5),(_X,6),('within1ms',7),(_Y,8),(_Z,9),(_a,10),(_b,11),('within100s',12),('within1000s',13),('within10000s',14),('failure',15)))
_Hm2IrigTimeQuality_Type.__name__=_C
_Hm2IrigTimeQuality_Object=MibScalar
hm2IrigTimeQuality=_Hm2IrigTimeQuality_Object((1,3,6,1,4,1,248,11,50,1,5,6),_Hm2IrigTimeQuality_Type())
hm2IrigTimeQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2IrigTimeQuality.setStatus(_A)
_Hm2Dot1asGroup_ObjectIdentity=ObjectIdentity
hm2Dot1asGroup=_Hm2Dot1asGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,6))
_Hm2Dot1asGlobal_ObjectIdentity=ObjectIdentity
hm2Dot1asGlobal=_Hm2Dot1asGlobal_ObjectIdentity((1,3,6,1,4,1,248,11,50,1,6,1))
class _Hm2Dot1asEnable_Type(HmEnabledStatus):defaultValue=2
_Hm2Dot1asEnable_Type.__name__=_F
_Hm2Dot1asEnable_Object=MibScalar
hm2Dot1asEnable=_Hm2Dot1asEnable_Object((1,3,6,1,4,1,248,11,50,1,6,1,1),_Hm2Dot1asEnable_Type())
hm2Dot1asEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Dot1asEnable.setStatus(_A)
class _Hm2Dot1asIsSynchronized_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hm2Dot1asIsSynchronized_Type.__name__=_C
_Hm2Dot1asIsSynchronized_Object=MibScalar
hm2Dot1asIsSynchronized=_Hm2Dot1asIsSynchronized_Object((1,3,6,1,4,1,248,11,50,1,6,1,2),_Hm2Dot1asIsSynchronized_Type())
hm2Dot1asIsSynchronized.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Dot1asIsSynchronized.setStatus(_A)
class _Hm2Dot1asSyncLowerBound_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999999))
_Hm2Dot1asSyncLowerBound_Type.__name__=_C
_Hm2Dot1asSyncLowerBound_Object=MibScalar
hm2Dot1asSyncLowerBound=_Hm2Dot1asSyncLowerBound_Object((1,3,6,1,4,1,248,11,50,1,6,1,3),_Hm2Dot1asSyncLowerBound_Type())
hm2Dot1asSyncLowerBound.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Dot1asSyncLowerBound.setStatus(_A)
class _Hm2Dot1asSyncUpperBound_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(31,1000000000))
_Hm2Dot1asSyncUpperBound_Type.__name__=_C
_Hm2Dot1asSyncUpperBound_Object=MibScalar
hm2Dot1asSyncUpperBound=_Hm2Dot1asSyncUpperBound_Object((1,3,6,1,4,1,248,11,50,1,6,1,4),_Hm2Dot1asSyncUpperBound_Type())
hm2Dot1asSyncUpperBound.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2Dot1asSyncUpperBound.setStatus(_A)
_Hm2Dot1asAbsMaxOffset_Type=Integer32
_Hm2Dot1asAbsMaxOffset_Object=MibScalar
hm2Dot1asAbsMaxOffset=_Hm2Dot1asAbsMaxOffset_Object((1,3,6,1,4,1,248,11,50,1,6,1,5),_Hm2Dot1asAbsMaxOffset_Type())
hm2Dot1asAbsMaxOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2Dot1asAbsMaxOffset.setStatus(_A)
_Hm2TimeSyncMibSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncMibSNMPExtensionGroup=_Hm2TimeSyncMibSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3))
_Hm2TimeSyncSystemTimeSESGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncSystemTimeSESGroup=_Hm2TimeSyncSystemTimeSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,1))
_Hm2TimeSyncSntpSESGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncSntpSESGroup=_Hm2TimeSyncSntpSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,2))
_Hm2TimeSyncSntpSESIpv4PortNumberPairInUse_ObjectIdentity=ObjectIdentity
hm2TimeSyncSntpSESIpv4PortNumberPairInUse=_Hm2TimeSyncSntpSESIpv4PortNumberPairInUse_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,2,1))
if mibBuilder.loadTexts:hm2TimeSyncSntpSESIpv4PortNumberPairInUse.setStatus(_A)
_Hm2TimeSyncSntpSESDnsPortNumberPairInUse_ObjectIdentity=ObjectIdentity
hm2TimeSyncSntpSESDnsPortNumberPairInUse=_Hm2TimeSyncSntpSESDnsPortNumberPairInUse_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,2,2))
if mibBuilder.loadTexts:hm2TimeSyncSntpSESDnsPortNumberPairInUse.setStatus(_A)
_Hm2TimeSyncSntpSESIpv6PortNumberPairInUse_ObjectIdentity=ObjectIdentity
hm2TimeSyncSntpSESIpv6PortNumberPairInUse=_Hm2TimeSyncSntpSESIpv6PortNumberPairInUse_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,2,3))
if mibBuilder.loadTexts:hm2TimeSyncSntpSESIpv6PortNumberPairInUse.setStatus(_A)
_Hm2TimeSyncNtpSESGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncNtpSESGroup=_Hm2TimeSyncNtpSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,3))
_Hm2TimeSyncPtpSESGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncPtpSESGroup=_Hm2TimeSyncPtpSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,4))
_Hm2TimeSyncPtpSESPortIsNotCapable_ObjectIdentity=ObjectIdentity
hm2TimeSyncPtpSESPortIsNotCapable=_Hm2TimeSyncPtpSESPortIsNotCapable_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,4,1))
if mibBuilder.loadTexts:hm2TimeSyncPtpSESPortIsNotCapable.setStatus(_A)
_Hm2TimeSyncIrigSESGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncIrigSESGroup=_Hm2TimeSyncIrigSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,5))
_Hm2TimeSyncDot1asSESGroup_ObjectIdentity=ObjectIdentity
hm2TimeSyncDot1asSESGroup=_Hm2TimeSyncDot1asSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,50,3,6))
hm2Ptp2SynchronizationChange=NotificationType((1,3,6,1,4,1,248,11,50,0,1))
hm2Ptp2SynchronizationChange.setObjects((_H,_AB))
if mibBuilder.loadTexts:hm2Ptp2SynchronizationChange.setStatus(_A)
hm2SntpClientSynchronizationChangeTrap=NotificationType((1,3,6,1,4,1,248,11,50,0,10))
hm2SntpClientSynchronizationChangeTrap.setObjects((_H,_AC))
if mibBuilder.loadTexts:hm2SntpClientSynchronizationChangeTrap.setStatus(_A)
hm2Dot1asSynchronizationChange=NotificationType((1,3,6,1,4,1,248,11,50,0,20))
hm2Dot1asSynchronizationChange.setObjects((_H,_AD))
if mibBuilder.loadTexts:hm2Dot1asSynchronizationChange.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'HmSntpClientServerStatus':HmSntpClientServerStatus,_A3:Hm2Ptp2LogSyncIntervalTc,_c:Hm2Ptp2LogPdelayReqIntervalTc,'PtpTimeInterval':PtpTimeInterval,'PtpTimeStamp':PtpTimeStamp,'PtpPortIdentity':PtpPortIdentity,'PtpClockIdentity':PtpClockIdentity,'PtpClockQuality':PtpClockQuality,'hm2TimeSyncMib':hm2TimeSyncMib,'hm2TimeSyncMibNotifications':hm2TimeSyncMibNotifications,'hm2Ptp2SynchronizationChange':hm2Ptp2SynchronizationChange,'hm2SntpClientSynchronizationChangeTrap':hm2SntpClientSynchronizationChangeTrap,'hm2Dot1asSynchronizationChange':hm2Dot1asSynchronizationChange,'hm2TimeSyncMibObjects':hm2TimeSyncMibObjects,'hm2SystemTimeGroup':hm2SystemTimeGroup,'hm2SystemUtcTime':hm2SystemUtcTime,'hm2SystemTimeSource':hm2SystemTimeSource,'hm2SystemLocalTime':hm2SystemLocalTime,'hm2SystemLocalOffset':hm2SystemLocalOffset,'hm2SntpGroup':hm2SntpGroup,'hm2SntpServerGroup':hm2SntpServerGroup,'hm2SntpServerAdminState':hm2SntpServerAdminState,'hm2SntpServerPort':hm2SntpServerPort,'hm2SntpServerOnlyIfSync':hm2SntpServerOnlyIfSync,'hm2SntpServerStatus':hm2SntpServerStatus,'hm2SntpServerInterface':hm2SntpServerInterface,'hm2SntpServerBroadcastGroup':hm2SntpServerBroadcastGroup,'hm2SntpServerBroadcastAdminState':hm2SntpServerBroadcastAdminState,'hm2SntpServerBroadcastAddrType':hm2SntpServerBroadcastAddrType,'hm2SntpServerBroadcastAddr':hm2SntpServerBroadcastAddr,'hm2SntpServerBroadcastPort':hm2SntpServerBroadcastPort,'hm2SntpServerBroadcastInterval':hm2SntpServerBroadcastInterval,'hm2SntpServerBroadcastVlanTable':hm2SntpServerBroadcastVlanTable,'hm2SntpServerBroadcastVlanEntry':hm2SntpServerBroadcastVlanEntry,_h:hm2SntpServerBroadcastVlan,'hm2SntpServerBroadcastVlanRowStatus':hm2SntpServerBroadcastVlanRowStatus,'hm2SntpClientGroup':hm2SntpClientGroup,'hm2SntpClientAdminState':hm2SntpClientAdminState,'hm2SntpClientOperatingMode':hm2SntpClientOperatingMode,'hm2SntpClientDisableAfterSync':hm2SntpClientDisableAfterSync,'hm2SntpClientRequestInterval':hm2SntpClientRequestInterval,_AC:hm2SntpClientStatus,'hm2SntpClientBroadcastRecvTimeout':hm2SntpClientBroadcastRecvTimeout,'hm2SntpClientInterface':hm2SntpClientInterface,'hm2SntpClientServerAddrTable':hm2SntpClientServerAddrTable,'hm2SntpClientServerAddrEntry':hm2SntpClientServerAddrEntry,_k:hm2SntpClientServerIndex,'hm2SntpClientServerAddrType':hm2SntpClientServerAddrType,'hm2SntpClientServerAddr':hm2SntpClientServerAddr,'hm2SntpClientServerPort':hm2SntpClientServerPort,'hm2SntpClientServerDescr':hm2SntpClientServerDescr,'hm2SntpClientServerStatus':hm2SntpClientServerStatus,'hm2SntpClientServerRowStatus':hm2SntpClientServerRowStatus,'hm2NtpGroup':hm2NtpGroup,'hm2NtpGeneralGroup':hm2NtpGeneralGroup,'hm2NtpOperatingState':hm2NtpOperatingState,'hm2NtpServerGroup':hm2NtpServerGroup,'hm2NtpServerConfigGroup':hm2NtpServerConfigGroup,'hm2NtpServerAdminState':hm2NtpServerAdminState,'hm2NtpServerOperatingMode':hm2NtpServerOperatingMode,'hm2NtpServerLocalClockStratum':hm2NtpServerLocalClockStratum,'hm2NtpClientGroup':hm2NtpClientGroup,'hm2NtpClientConfigGroup':hm2NtpClientConfigGroup,'hm2NtpClientAdminState':hm2NtpClientAdminState,'hm2NtpClientOperatingMode':hm2NtpClientOperatingMode,'hm2NtpClientServerAddrTable':hm2NtpClientServerAddrTable,'hm2NtpClientServerAddrEntry':hm2NtpClientServerAddrEntry,_l:hm2NtpClientServerIndex,'hm2NtpClientServerAddressType':hm2NtpClientServerAddressType,'hm2NtpClientServerAddress':hm2NtpClientServerAddress,'hm2NtpClientServerPort':hm2NtpClientServerPort,'hm2NtpClientServerInitialBurst':hm2NtpClientServerInitialBurst,'hm2NtpClientServerBurst':hm2NtpClientServerBurst,'hm2NtpClientServerPrefer':hm2NtpClientServerPrefer,'hm2NtpClientServerStatus':hm2NtpClientServerStatus,'hm2NtpClientServerRowStatus':hm2NtpClientServerRowStatus,'hm2NtpClientListenAddrTable':hm2NtpClientListenAddrTable,'hm2NtpClientListenAddrEntry':hm2NtpClientListenAddrEntry,_r:hm2NtpClientListenAddrIndex,'hm2NtpClientListenAddrAddressType':hm2NtpClientListenAddrAddressType,'hm2NtpClientListenAddrAddress':hm2NtpClientListenAddrAddress,'hm2NtpClientListenAddrPort':hm2NtpClientListenAddrPort,'hm2NtpClientListenAddrStatus':hm2NtpClientListenAddrStatus,'hm2NtpClientListenAddrRowStatus':hm2NtpClientListenAddrRowStatus,'hm2PtpGroup':hm2PtpGroup,'hm2PtpGlobal':hm2PtpGlobal,'hm2PtpEnable':hm2PtpEnable,'hm2PtpClockMode':hm2PtpClockMode,'hm2PtpProfile':hm2PtpProfile,_AB:hm2PtpIsSynchronized,'hm2PtpSyncLowerBound':hm2PtpSyncLowerBound,'hm2PtpSyncUpperBound':hm2PtpSyncUpperBound,'hm2PtpAbsMaxOffset':hm2PtpAbsMaxOffset,'hm2PtpTimeSeconds':hm2PtpTimeSeconds,'hm2PtpManagement':hm2PtpManagement,'hm2Ptp2Objects':hm2Ptp2Objects,'hm2Ptp2Configuration':hm2Ptp2Configuration,'hm2Ptp2TwoStepClock':hm2Ptp2TwoStepClock,'hm2Ptp2ClockIdentity':hm2Ptp2ClockIdentity,'hm2Ptp2ClockQuality':hm2Ptp2ClockQuality,'hm2Ptp2ClockClass':hm2Ptp2ClockClass,'hm2Ptp2ClockAccuracy':hm2Ptp2ClockAccuracy,'hm2Ptp2ClockVariance':hm2Ptp2ClockVariance,'hm2Ptp2Priority1':hm2Ptp2Priority1,'hm2Ptp2Priority2':hm2Ptp2Priority2,'hm2Ptp2DomainNumber':hm2Ptp2DomainNumber,'hm2Ptp2StepsRemoved':hm2Ptp2StepsRemoved,'hm2Ptp2OffsetFromMaster':hm2Ptp2OffsetFromMaster,'hm2Ptp2MeanPathDelay':hm2Ptp2MeanPathDelay,'hm2Ptp2ParentPortIdentity':hm2Ptp2ParentPortIdentity,'hm2Ptp2ParentStats':hm2Ptp2ParentStats,'hm2Ptp2ObservedParentOffsetScaledLogVariance':hm2Ptp2ObservedParentOffsetScaledLogVariance,'hm2Ptp2ObservedParentClockPhaseChangeRate':hm2Ptp2ObservedParentClockPhaseChangeRate,'hm2Ptp2GrandmasterIdentity':hm2Ptp2GrandmasterIdentity,'hm2Ptp2GrandmasterClockQuality':hm2Ptp2GrandmasterClockQuality,'hm2Ptp2GrandmasterClockClass':hm2Ptp2GrandmasterClockClass,'hm2Ptp2GrandmasterClockAccuracy':hm2Ptp2GrandmasterClockAccuracy,'hm2Ptp2GrandmasterClockVariance':hm2Ptp2GrandmasterClockVariance,'hm2Ptp2GrandmasterPriority1':hm2Ptp2GrandmasterPriority1,'hm2Ptp2GrandmasterPriority2':hm2Ptp2GrandmasterPriority2,'hm2Ptp2CurrentUtcOffset':hm2Ptp2CurrentUtcOffset,'hm2Ptp2CurrentUtcOffsetValid':hm2Ptp2CurrentUtcOffsetValid,'hm2Ptp2Leap59':hm2Ptp2Leap59,'hm2Ptp2Leap61':hm2Ptp2Leap61,'hm2Ptp2TimeTraceable':hm2Ptp2TimeTraceable,'hm2Ptp2FrequencyTraceable':hm2Ptp2FrequencyTraceable,'hm2Ptp2PtpTimescale':hm2Ptp2PtpTimescale,'hm2Ptp2TimeSource':hm2Ptp2TimeSource,'hm2Ptp2PortTable':hm2Ptp2PortTable,'hm2Ptp2PortEntry':hm2Ptp2PortEntry,'hm2Ptp2PortEnable':hm2Ptp2PortEnable,'hm2Ptp2PortState':hm2Ptp2PortState,'hm2Ptp2LogDelayReqInterval':hm2Ptp2LogDelayReqInterval,'hm2Ptp2PeerMeanPathDelay':hm2Ptp2PeerMeanPathDelay,'hm2Ptp2LogAnnounceInterval':hm2Ptp2LogAnnounceInterval,'hm2Ptp2AnnounceReceiptTimeout':hm2Ptp2AnnounceReceiptTimeout,'hm2Ptp2LogSyncInterval':hm2Ptp2LogSyncInterval,'hm2Ptp2DelayMechanism':hm2Ptp2DelayMechanism,'hm2Ptp2LogPdelayReqInterval':hm2Ptp2LogPdelayReqInterval,'hm2Ptp2VersionNumber':hm2Ptp2VersionNumber,'hm2Ptp2NetworkProtocol':hm2Ptp2NetworkProtocol,'hm2Ptp2V1Compatibility':hm2Ptp2V1Compatibility,'hm2Ptp2DelayAsymmetry':hm2Ptp2DelayAsymmetry,'hm2Ptp2PortCapability':hm2Ptp2PortCapability,'hm2Ptp2VlanID':hm2Ptp2VlanID,'hm2Ptp2VlanPriority':hm2Ptp2VlanPriority,'hm2Ptp2TCObjects':hm2Ptp2TCObjects,'hm2Ptp2TCConfiguration':hm2Ptp2TCConfiguration,'hm2Ptp2TCClockIdentity':hm2Ptp2TCClockIdentity,'hm2Ptp2TCDelayMechanism':hm2Ptp2TCDelayMechanism,'hm2Ptp2TCPrimaryDomain':hm2Ptp2TCPrimaryDomain,'hm2Ptp2TCSyntonized':hm2Ptp2TCSyntonized,'hm2Ptp2TCNetworkProtocol':hm2Ptp2TCNetworkProtocol,'hm2Ptp2TCCurrentMaster':hm2Ptp2TCCurrentMaster,'hm2Ptp2TCMultiDomainMode':hm2Ptp2TCMultiDomainMode,'hm2Ptp2TCSyncLocalClock':hm2Ptp2TCSyncLocalClock,'hm2Ptp2TCOffsetFromMaster':hm2Ptp2TCOffsetFromMaster,'hm2Ptp2TCMeanPathDelay':hm2Ptp2TCMeanPathDelay,'hm2Ptp2TCVlanID':hm2Ptp2TCVlanID,'hm2Ptp2TCVlanPriority':hm2Ptp2TCVlanPriority,'hm2Ptp2TCCapability':hm2Ptp2TCCapability,'hm2Ptp2TCPortTable':hm2Ptp2TCPortTable,'hm2Ptp2TCPortEntry':hm2Ptp2TCPortEntry,'hm2Ptp2TCPortEnable':hm2Ptp2TCPortEnable,'hm2Ptp2TCLogPdelayReqInterval':hm2Ptp2TCLogPdelayReqInterval,'hm2Ptp2TCFaulty':hm2Ptp2TCFaulty,'hm2Ptp2TCPeerMeanPathDelay':hm2Ptp2TCPeerMeanPathDelay,'hm2Ptp2TCDelayAsymmetry':hm2Ptp2TCDelayAsymmetry,'hm2IrigGroup':hm2IrigGroup,'hm2IrigAdminStatus':hm2IrigAdminStatus,'hm2IrigMode':hm2IrigMode,'hm2IrigPpsAdminStatus':hm2IrigPpsAdminStatus,'hm2IrigTimeMode':hm2IrigTimeMode,'hm2IrigOperStatus':hm2IrigOperStatus,'hm2IrigTimeQuality':hm2IrigTimeQuality,'hm2Dot1asGroup':hm2Dot1asGroup,'hm2Dot1asGlobal':hm2Dot1asGlobal,'hm2Dot1asEnable':hm2Dot1asEnable,_AD:hm2Dot1asIsSynchronized,'hm2Dot1asSyncLowerBound':hm2Dot1asSyncLowerBound,'hm2Dot1asSyncUpperBound':hm2Dot1asSyncUpperBound,'hm2Dot1asAbsMaxOffset':hm2Dot1asAbsMaxOffset,'hm2TimeSyncMibSNMPExtensionGroup':hm2TimeSyncMibSNMPExtensionGroup,'hm2TimeSyncSystemTimeSESGroup':hm2TimeSyncSystemTimeSESGroup,'hm2TimeSyncSntpSESGroup':hm2TimeSyncSntpSESGroup,'hm2TimeSyncSntpSESIpv4PortNumberPairInUse':hm2TimeSyncSntpSESIpv4PortNumberPairInUse,'hm2TimeSyncSntpSESDnsPortNumberPairInUse':hm2TimeSyncSntpSESDnsPortNumberPairInUse,'hm2TimeSyncSntpSESIpv6PortNumberPairInUse':hm2TimeSyncSntpSESIpv6PortNumberPairInUse,'hm2TimeSyncNtpSESGroup':hm2TimeSyncNtpSESGroup,'hm2TimeSyncPtpSESGroup':hm2TimeSyncPtpSESGroup,'hm2TimeSyncPtpSESPortIsNotCapable':hm2TimeSyncPtpSESPortIsNotCapable,'hm2TimeSyncIrigSESGroup':hm2TimeSyncIrigSESGroup,'hm2TimeSyncDot1asSESGroup':hm2TimeSyncDot1asSESGroup})