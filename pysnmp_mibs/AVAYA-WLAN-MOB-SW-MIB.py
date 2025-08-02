_g='avWlanMobSwFdbMacAddress'
_f='avWlanMobSwFdbVlanId'
_e='avWlanMobSwControllerId'
_d='avWlanMobTunnelStatsDeviceId'
_c='avWlanMobVlanPeerAdvertiserId'
_b='avWlanMobVlanPeerAdvertiserVlanName'
_a='avWlanMobVlanServerVlanName'
_Z='avWlanMobPeerVlansAdvertisedVlanName'
_Y='avWlanMobPeerVlansAdvertisedId'
_X='resPeerAccessTunnel'
_W='accessTunnel'
_V='mobTunnel'
_U='failure'
_T='success'
_S='inProgress'
_R='notStarted'
_Q='avWlanMobAgentVlanName'
_P='avWlanMobSwDeviceId'
_O='avWlanMobSwDeviceType'
_N='reset'
_M='bits/seconds'
_L='SnmpAdminString'
_K='InetAddress'
_J='none'
_I='read-create'
_H='Unsigned32'
_G='read-write'
_F='not-accessible'
_E='AVAYA-WLAN-MOB-SW-MIB'
_D='Integer32'
_C='deprecated'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,'InetAddressType','InetPortNumber')
PortList,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIdOrNone')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
avayaWlanMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','avayaWlanMibs')
avayaWlanMobSwMib=ModuleIdentity((1,3,6,1,4,1,45,7,10))
if mibBuilder.loadTexts:avayaWlanMobSwMib.setRevisions(('2010-03-30 00:00',))
_AvWlanMobSwObjects_ObjectIdentity=ObjectIdentity
avWlanMobSwObjects=_AvWlanMobSwObjects_ObjectIdentity((1,3,6,1,4,1,45,7,10,1))
_AvWlanMobAgentObjects_ObjectIdentity=ObjectIdentity
avWlanMobAgentObjects=_AvWlanMobAgentObjects_ObjectIdentity((1,3,6,1,4,1,45,7,10,1,1))
_AvWlanMobAgentVlanTable_Object=MibTable
avWlanMobAgentVlanTable=_AvWlanMobAgentVlanTable_Object((1,3,6,1,4,1,45,7,10,1,1,1))
if mibBuilder.loadTexts:avWlanMobAgentVlanTable.setStatus(_A)
_AvWlanMobAgentVlanEntry_Object=MibTableRow
avWlanMobAgentVlanEntry=_AvWlanMobAgentVlanEntry_Object((1,3,6,1,4,1,45,7,10,1,1,1,1))
avWlanMobAgentVlanEntry.setIndexNames((1,_E,_Q))
if mibBuilder.loadTexts:avWlanMobAgentVlanEntry.setStatus(_A)
class _AvWlanMobAgentVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AvWlanMobAgentVlanName_Type.__name__=_L
_AvWlanMobAgentVlanName_Object=MibTableColumn
avWlanMobAgentVlanName=_AvWlanMobAgentVlanName_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,1),_AvWlanMobAgentVlanName_Type())
avWlanMobAgentVlanName.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobAgentVlanName.setStatus(_A)
_AvWlanMobAgentVlanLVID_Type=VlanIdOrNone
_AvWlanMobAgentVlanLVID_Object=MibTableColumn
avWlanMobAgentVlanLVID=_AvWlanMobAgentVlanLVID_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,2),_AvWlanMobAgentVlanLVID_Type())
avWlanMobAgentVlanLVID.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobAgentVlanLVID.setStatus(_A)
class _AvWlanMobAgentVlanL3Mobility_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('server',2),('client',3)))
_AvWlanMobAgentVlanL3Mobility_Type.__name__=_D
_AvWlanMobAgentVlanL3Mobility_Object=MibTableColumn
avWlanMobAgentVlanL3Mobility=_AvWlanMobAgentVlanL3Mobility_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,3),_AvWlanMobAgentVlanL3Mobility_Type())
avWlanMobAgentVlanL3Mobility.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobAgentVlanL3Mobility.setStatus(_A)
class _AvWlanMobAgentVlanWeight_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AvWlanMobAgentVlanWeight_Type.__name__=_H
_AvWlanMobAgentVlanWeight_Object=MibTableColumn
avWlanMobAgentVlanWeight=_AvWlanMobAgentVlanWeight_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,4),_AvWlanMobAgentVlanWeight_Type())
avWlanMobAgentVlanWeight.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobAgentVlanWeight.setStatus(_A)
_AvWlanMobAgentVlanTrack_Type=PortList
_AvWlanMobAgentVlanTrack_Object=MibTableColumn
avWlanMobAgentVlanTrack=_AvWlanMobAgentVlanTrack_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,5),_AvWlanMobAgentVlanTrack_Type())
avWlanMobAgentVlanTrack.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobAgentVlanTrack.setStatus(_A)
class _AvWlanMobAgentVlanScope_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('domain',1),('enterprise',2)))
_AvWlanMobAgentVlanScope_Type.__name__=_D
_AvWlanMobAgentVlanScope_Object=MibTableColumn
avWlanMobAgentVlanScope=_AvWlanMobAgentVlanScope_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,6),_AvWlanMobAgentVlanScope_Type())
avWlanMobAgentVlanScope.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobAgentVlanScope.setStatus(_A)
_AvWlanMobAgentVlanWcValidated_Type=TruthValue
_AvWlanMobAgentVlanWcValidated_Object=MibTableColumn
avWlanMobAgentVlanWcValidated=_AvWlanMobAgentVlanWcValidated_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,7),_AvWlanMobAgentVlanWcValidated_Type())
avWlanMobAgentVlanWcValidated.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobAgentVlanWcValidated.setStatus(_A)
_AvWlanMobAgentVlanAdminMapped_Type=TruthValue
_AvWlanMobAgentVlanAdminMapped_Object=MibTableColumn
avWlanMobAgentVlanAdminMapped=_AvWlanMobAgentVlanAdminMapped_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,8),_AvWlanMobAgentVlanAdminMapped_Type())
avWlanMobAgentVlanAdminMapped.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobAgentVlanAdminMapped.setStatus(_A)
_AvWlanMobAgentVlanActive_Type=TruthValue
_AvWlanMobAgentVlanActive_Object=MibTableColumn
avWlanMobAgentVlanActive=_AvWlanMobAgentVlanActive_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,9),_AvWlanMobAgentVlanActive_Type())
avWlanMobAgentVlanActive.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobAgentVlanActive.setStatus(_A)
_AvWlanMobAgentVlanRowStatus_Type=RowStatus
_AvWlanMobAgentVlanRowStatus_Object=MibTableColumn
avWlanMobAgentVlanRowStatus=_AvWlanMobAgentVlanRowStatus_Object((1,3,6,1,4,1,45,7,10,1,1,1,1,10),_AvWlanMobAgentVlanRowStatus_Type())
avWlanMobAgentVlanRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobAgentVlanRowStatus.setStatus(_A)
_AvWlanMobSwScalars_ObjectIdentity=ObjectIdentity
avWlanMobSwScalars=_AvWlanMobSwScalars_ObjectIdentity((1,3,6,1,4,1,45,7,10,1,2))
class _AvWlanMobSwVLANPeriodicAdvInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AvWlanMobSwVLANPeriodicAdvInterval_Type.__name__=_H
_AvWlanMobSwVLANPeriodicAdvInterval_Object=MibScalar
avWlanMobSwVLANPeriodicAdvInterval=_AvWlanMobSwVLANPeriodicAdvInterval_Object((1,3,6,1,4,1,45,7,10,1,2,1),_AvWlanMobSwVLANPeriodicAdvInterval_Type())
avWlanMobSwVLANPeriodicAdvInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwVLANPeriodicAdvInterval.setStatus(_A)
if mibBuilder.loadTexts:avWlanMobSwVLANPeriodicAdvInterval.setUnits('seconds')
class _AvWlanMobSwVMMMaxRetransmits_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobSwVMMMaxRetransmits_Type.__name__=_H
_AvWlanMobSwVMMMaxRetransmits_Object=MibScalar
avWlanMobSwVMMMaxRetransmits=_AvWlanMobSwVMMMaxRetransmits_Object((1,3,6,1,4,1,45,7,10,1,2,2),_AvWlanMobSwVMMMaxRetransmits_Type())
avWlanMobSwVMMMaxRetransmits.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwVMMMaxRetransmits.setStatus(_A)
class _AvWlanMobSwKeepAliveInterval_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobSwKeepAliveInterval_Type.__name__=_H
_AvWlanMobSwKeepAliveInterval_Object=MibScalar
avWlanMobSwKeepAliveInterval=_AvWlanMobSwKeepAliveInterval_Object((1,3,6,1,4,1,45,7,10,1,2,3),_AvWlanMobSwKeepAliveInterval_Type())
avWlanMobSwKeepAliveInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:avWlanMobSwKeepAliveInterval.setUnits('milliseconds')
class _AvWlanMobSwKeepAliveNumRetries_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobSwKeepAliveNumRetries_Type.__name__=_H
_AvWlanMobSwKeepAliveNumRetries_Object=MibScalar
avWlanMobSwKeepAliveNumRetries=_AvWlanMobSwKeepAliveNumRetries_Object((1,3,6,1,4,1,45,7,10,1,2,4),_AvWlanMobSwKeepAliveNumRetries_Type())
avWlanMobSwKeepAliveNumRetries.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwKeepAliveNumRetries.setStatus(_A)
class _AvWlanMobSwTransMaxRetransmits_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobSwTransMaxRetransmits_Type.__name__=_H
_AvWlanMobSwTransMaxRetransmits_Object=MibScalar
avWlanMobSwTransMaxRetransmits=_AvWlanMobSwTransMaxRetransmits_Object((1,3,6,1,4,1,45,7,10,1,2,5),_AvWlanMobSwTransMaxRetransmits_Type())
avWlanMobSwTransMaxRetransmits.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwTransMaxRetransmits.setStatus(_A)
_AvWlanMobSwLocalDeviceId_Type=MacAddress
_AvWlanMobSwLocalDeviceId_Object=MibScalar
avWlanMobSwLocalDeviceId=_AvWlanMobSwLocalDeviceId_Object((1,3,6,1,4,1,45,7,10,1,2,6),_AvWlanMobSwLocalDeviceId_Type())
avWlanMobSwLocalDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwLocalDeviceId.setStatus(_A)
class _AvWlanMobSwAllStatisticsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_N,2)))
_AvWlanMobSwAllStatisticsReset_Type.__name__=_D
_AvWlanMobSwAllStatisticsReset_Object=MibScalar
avWlanMobSwAllStatisticsReset=_AvWlanMobSwAllStatisticsReset_Object((1,3,6,1,4,1,45,7,10,1,2,7),_AvWlanMobSwAllStatisticsReset_Type())
avWlanMobSwAllStatisticsReset.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwAllStatisticsReset.setStatus(_A)
class _AvWlanMobSwAllStatisticsResetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('requested',2),(_S,3),(_T,4),('partialSuccess',5),(_U,6)))
_AvWlanMobSwAllStatisticsResetStatus_Type.__name__=_D
_AvWlanMobSwAllStatisticsResetStatus_Object=MibScalar
avWlanMobSwAllStatisticsResetStatus=_AvWlanMobSwAllStatisticsResetStatus_Object((1,3,6,1,4,1,45,7,10,1,2,8),_AvWlanMobSwAllStatisticsResetStatus_Type())
avWlanMobSwAllStatisticsResetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwAllStatisticsResetStatus.setStatus(_A)
_AvWlanMobSwCtrlAddrType_Type=InetAddressType
_AvWlanMobSwCtrlAddrType_Object=MibScalar
avWlanMobSwCtrlAddrType=_AvWlanMobSwCtrlAddrType_Object((1,3,6,1,4,1,45,7,10,1,2,9),_AvWlanMobSwCtrlAddrType_Type())
avWlanMobSwCtrlAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwCtrlAddrType.setStatus(_A)
class _AvWlanMobSwCtrlAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AvWlanMobSwCtrlAddr_Type.__name__=_K
_AvWlanMobSwCtrlAddr_Object=MibScalar
avWlanMobSwCtrlAddr=_AvWlanMobSwCtrlAddr_Object((1,3,6,1,4,1,45,7,10,1,2,10),_AvWlanMobSwCtrlAddr_Type())
avWlanMobSwCtrlAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwCtrlAddr.setStatus(_A)
_AvWlanMobSwNumMobilityTunnels_Type=Counter32
_AvWlanMobSwNumMobilityTunnels_Object=MibScalar
avWlanMobSwNumMobilityTunnels=_AvWlanMobSwNumMobilityTunnels_Object((1,3,6,1,4,1,45,7,10,1,2,11),_AvWlanMobSwNumMobilityTunnels_Type())
avWlanMobSwNumMobilityTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwNumMobilityTunnels.setStatus(_A)
_AvWlanMobSwNumAccessTunnels_Type=Counter32
_AvWlanMobSwNumAccessTunnels_Object=MibScalar
avWlanMobSwNumAccessTunnels=_AvWlanMobSwNumAccessTunnels_Object((1,3,6,1,4,1,45,7,10,1,2,12),_AvWlanMobSwNumAccessTunnels_Type())
avWlanMobSwNumAccessTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwNumAccessTunnels.setStatus(_A)
_AvWlanMobSwNumResPeerAccessTunnels_Type=Counter32
_AvWlanMobSwNumResPeerAccessTunnels_Object=MibScalar
avWlanMobSwNumResPeerAccessTunnels=_AvWlanMobSwNumResPeerAccessTunnels_Object((1,3,6,1,4,1,45,7,10,1,2,13),_AvWlanMobSwNumResPeerAccessTunnels_Type())
avWlanMobSwNumResPeerAccessTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwNumResPeerAccessTunnels.setStatus(_A)
class _AvWlanMobSwFdbGlobalFlushAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('flushAll',2)))
_AvWlanMobSwFdbGlobalFlushAction_Type.__name__=_D
_AvWlanMobSwFdbGlobalFlushAction_Object=MibScalar
avWlanMobSwFdbGlobalFlushAction=_AvWlanMobSwFdbGlobalFlushAction_Object((1,3,6,1,4,1,45,7,10,1,2,14),_AvWlanMobSwFdbGlobalFlushAction_Type())
avWlanMobSwFdbGlobalFlushAction.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwFdbGlobalFlushAction.setStatus(_A)
class _AvWlanMobSwFdbGlobalFlushActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),('partialFailure',4),(_U,5)))
_AvWlanMobSwFdbGlobalFlushActionStatus_Type.__name__=_D
_AvWlanMobSwFdbGlobalFlushActionStatus_Object=MibScalar
avWlanMobSwFdbGlobalFlushActionStatus=_AvWlanMobSwFdbGlobalFlushActionStatus_Object((1,3,6,1,4,1,45,7,10,1,2,15),_AvWlanMobSwFdbGlobalFlushActionStatus_Type())
avWlanMobSwFdbGlobalFlushActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbGlobalFlushActionStatus.setStatus(_A)
class _AvWlanMobSwPurgeInactiveMaps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('purge',2)))
_AvWlanMobSwPurgeInactiveMaps_Type.__name__=_D
_AvWlanMobSwPurgeInactiveMaps_Object=MibScalar
avWlanMobSwPurgeInactiveMaps=_AvWlanMobSwPurgeInactiveMaps_Object((1,3,6,1,4,1,45,7,10,1,2,16),_AvWlanMobSwPurgeInactiveMaps_Type())
avWlanMobSwPurgeInactiveMaps.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwPurgeInactiveMaps.setStatus(_A)
_AvWlanMobSwDeviceTable_Object=MibTable
avWlanMobSwDeviceTable=_AvWlanMobSwDeviceTable_Object((1,3,6,1,4,1,45,7,10,1,3))
if mibBuilder.loadTexts:avWlanMobSwDeviceTable.setStatus(_A)
_AvWlanMobSwDeviceEntry_Object=MibTableRow
avWlanMobSwDeviceEntry=_AvWlanMobSwDeviceEntry_Object((1,3,6,1,4,1,45,7,10,1,3,1))
avWlanMobSwDeviceEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:avWlanMobSwDeviceEntry.setStatus(_A)
class _AvWlanMobSwDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3)))
_AvWlanMobSwDeviceType_Type.__name__=_D
_AvWlanMobSwDeviceType_Object=MibTableColumn
avWlanMobSwDeviceType=_AvWlanMobSwDeviceType_Object((1,3,6,1,4,1,45,7,10,1,3,1,1),_AvWlanMobSwDeviceType_Type())
avWlanMobSwDeviceType.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobSwDeviceType.setStatus(_A)
_AvWlanMobSwDeviceId_Type=MacAddress
_AvWlanMobSwDeviceId_Object=MibTableColumn
avWlanMobSwDeviceId=_AvWlanMobSwDeviceId_Object((1,3,6,1,4,1,45,7,10,1,3,1,2),_AvWlanMobSwDeviceId_Type())
avWlanMobSwDeviceId.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobSwDeviceId.setStatus(_A)
_AvWlanMobSwDeviceAddrType_Type=InetAddressType
_AvWlanMobSwDeviceAddrType_Object=MibTableColumn
avWlanMobSwDeviceAddrType=_AvWlanMobSwDeviceAddrType_Object((1,3,6,1,4,1,45,7,10,1,3,1,3),_AvWlanMobSwDeviceAddrType_Type())
avWlanMobSwDeviceAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwDeviceAddrType.setStatus(_A)
class _AvWlanMobSwDeviceAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AvWlanMobSwDeviceAddr_Type.__name__=_K
_AvWlanMobSwDeviceAddr_Object=MibTableColumn
avWlanMobSwDeviceAddr=_AvWlanMobSwDeviceAddr_Object((1,3,6,1,4,1,45,7,10,1,3,1,4),_AvWlanMobSwDeviceAddr_Type())
avWlanMobSwDeviceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwDeviceAddr.setStatus(_A)
_AvWlanMobSwDeviceUdpPort_Type=InetPortNumber
_AvWlanMobSwDeviceUdpPort_Object=MibTableColumn
avWlanMobSwDeviceUdpPort=_AvWlanMobSwDeviceUdpPort_Object((1,3,6,1,4,1,45,7,10,1,3,1,5),_AvWlanMobSwDeviceUdpPort_Type())
avWlanMobSwDeviceUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwDeviceUdpPort.setStatus(_A)
class _AvWlanMobSwDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AvWlanMobSwDeviceStatus_Type.__name__=_D
_AvWlanMobSwDeviceStatus_Object=MibTableColumn
avWlanMobSwDeviceStatus=_AvWlanMobSwDeviceStatus_Object((1,3,6,1,4,1,45,7,10,1,3,1,6),_AvWlanMobSwDeviceStatus_Type())
avWlanMobSwDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwDeviceStatus.setStatus(_A)
_AvWlanMobSwDeviceLocalUdpPort_Type=InetPortNumber
_AvWlanMobSwDeviceLocalUdpPort_Object=MibTableColumn
avWlanMobSwDeviceLocalUdpPort=_AvWlanMobSwDeviceLocalUdpPort_Object((1,3,6,1,4,1,45,7,10,1,3,1,7),_AvWlanMobSwDeviceLocalUdpPort_Type())
avWlanMobSwDeviceLocalUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwDeviceLocalUdpPort.setStatus(_A)
_AvWlanMobSwDeviceInterfaceId_Type=Integer32
_AvWlanMobSwDeviceInterfaceId_Object=MibTableColumn
avWlanMobSwDeviceInterfaceId=_AvWlanMobSwDeviceInterfaceId_Object((1,3,6,1,4,1,45,7,10,1,3,1,8),_AvWlanMobSwDeviceInterfaceId_Type())
avWlanMobSwDeviceInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwDeviceInterfaceId.setStatus(_A)
_AvWlanMobPeerVlansAdvertisedTable_Object=MibTable
avWlanMobPeerVlansAdvertisedTable=_AvWlanMobPeerVlansAdvertisedTable_Object((1,3,6,1,4,1,45,7,10,1,4))
if mibBuilder.loadTexts:avWlanMobPeerVlansAdvertisedTable.setStatus(_A)
_AvWlanMobPeerVlansAdvertisedEntry_Object=MibTableRow
avWlanMobPeerVlansAdvertisedEntry=_AvWlanMobPeerVlansAdvertisedEntry_Object((1,3,6,1,4,1,45,7,10,1,4,1))
avWlanMobPeerVlansAdvertisedEntry.setIndexNames((0,_E,_Y),(1,_E,_Z))
if mibBuilder.loadTexts:avWlanMobPeerVlansAdvertisedEntry.setStatus(_A)
_AvWlanMobPeerVlansAdvertisedId_Type=MacAddress
_AvWlanMobPeerVlansAdvertisedId_Object=MibTableColumn
avWlanMobPeerVlansAdvertisedId=_AvWlanMobPeerVlansAdvertisedId_Object((1,3,6,1,4,1,45,7,10,1,4,1,1),_AvWlanMobPeerVlansAdvertisedId_Type())
avWlanMobPeerVlansAdvertisedId.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobPeerVlansAdvertisedId.setStatus(_A)
class _AvWlanMobPeerVlansAdvertisedVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AvWlanMobPeerVlansAdvertisedVlanName_Type.__name__=_L
_AvWlanMobPeerVlansAdvertisedVlanName_Object=MibTableColumn
avWlanMobPeerVlansAdvertisedVlanName=_AvWlanMobPeerVlansAdvertisedVlanName_Object((1,3,6,1,4,1,45,7,10,1,4,1,2),_AvWlanMobPeerVlansAdvertisedVlanName_Type())
avWlanMobPeerVlansAdvertisedVlanName.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobPeerVlansAdvertisedVlanName.setStatus(_A)
class _AvWlanMobPeerVlansAdvertisedPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobPeerVlansAdvertisedPriority_Type.__name__=_H
_AvWlanMobPeerVlansAdvertisedPriority_Object=MibTableColumn
avWlanMobPeerVlansAdvertisedPriority=_AvWlanMobPeerVlansAdvertisedPriority_Object((1,3,6,1,4,1,45,7,10,1,4,1,3),_AvWlanMobPeerVlansAdvertisedPriority_Type())
avWlanMobPeerVlansAdvertisedPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobPeerVlansAdvertisedPriority.setStatus(_A)
_AvWlanMobVlanServerTable_Object=MibTable
avWlanMobVlanServerTable=_AvWlanMobVlanServerTable_Object((1,3,6,1,4,1,45,7,10,1,5))
if mibBuilder.loadTexts:avWlanMobVlanServerTable.setStatus(_A)
_AvWlanMobVlanServerEntry_Object=MibTableRow
avWlanMobVlanServerEntry=_AvWlanMobVlanServerEntry_Object((1,3,6,1,4,1,45,7,10,1,5,1))
avWlanMobVlanServerEntry.setIndexNames((1,_E,_a))
if mibBuilder.loadTexts:avWlanMobVlanServerEntry.setStatus(_A)
class _AvWlanMobVlanServerVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AvWlanMobVlanServerVlanName_Type.__name__=_L
_AvWlanMobVlanServerVlanName_Object=MibTableColumn
avWlanMobVlanServerVlanName=_AvWlanMobVlanServerVlanName_Object((1,3,6,1,4,1,45,7,10,1,5,1,1),_AvWlanMobVlanServerVlanName_Type())
avWlanMobVlanServerVlanName.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobVlanServerVlanName.setStatus(_A)
_AvWlanMobVlanServerId_Type=MacAddress
_AvWlanMobVlanServerId_Object=MibTableColumn
avWlanMobVlanServerId=_AvWlanMobVlanServerId_Object((1,3,6,1,4,1,45,7,10,1,5,1,2),_AvWlanMobVlanServerId_Type())
avWlanMobVlanServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobVlanServerId.setStatus(_A)
class _AvWlanMobVlanServerPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobVlanServerPriority_Type.__name__=_H
_AvWlanMobVlanServerPriority_Object=MibTableColumn
avWlanMobVlanServerPriority=_AvWlanMobVlanServerPriority_Object((1,3,6,1,4,1,45,7,10,1,5,1,3),_AvWlanMobVlanServerPriority_Type())
avWlanMobVlanServerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobVlanServerPriority.setStatus(_A)
_AvWlanMobVlanPeerAdvertiserTable_Object=MibTable
avWlanMobVlanPeerAdvertiserTable=_AvWlanMobVlanPeerAdvertiserTable_Object((1,3,6,1,4,1,45,7,10,1,6))
if mibBuilder.loadTexts:avWlanMobVlanPeerAdvertiserTable.setStatus(_A)
_AvWlanMobVlanPeerAdvertiserEntry_Object=MibTableRow
avWlanMobVlanPeerAdvertiserEntry=_AvWlanMobVlanPeerAdvertiserEntry_Object((1,3,6,1,4,1,45,7,10,1,6,1))
avWlanMobVlanPeerAdvertiserEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:avWlanMobVlanPeerAdvertiserEntry.setStatus(_A)
class _AvWlanMobVlanPeerAdvertiserVlanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AvWlanMobVlanPeerAdvertiserVlanName_Type.__name__=_L
_AvWlanMobVlanPeerAdvertiserVlanName_Object=MibTableColumn
avWlanMobVlanPeerAdvertiserVlanName=_AvWlanMobVlanPeerAdvertiserVlanName_Object((1,3,6,1,4,1,45,7,10,1,6,1,1),_AvWlanMobVlanPeerAdvertiserVlanName_Type())
avWlanMobVlanPeerAdvertiserVlanName.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobVlanPeerAdvertiserVlanName.setStatus(_A)
_AvWlanMobVlanPeerAdvertiserId_Type=MacAddress
_AvWlanMobVlanPeerAdvertiserId_Object=MibTableColumn
avWlanMobVlanPeerAdvertiserId=_AvWlanMobVlanPeerAdvertiserId_Object((1,3,6,1,4,1,45,7,10,1,6,1,2),_AvWlanMobVlanPeerAdvertiserId_Type())
avWlanMobVlanPeerAdvertiserId.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobVlanPeerAdvertiserId.setStatus(_A)
class _AvWlanMobVlanPeerAdvertiserPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvWlanMobVlanPeerAdvertiserPriority_Type.__name__=_H
_AvWlanMobVlanPeerAdvertiserPriority_Object=MibTableColumn
avWlanMobVlanPeerAdvertiserPriority=_AvWlanMobVlanPeerAdvertiserPriority_Object((1,3,6,1,4,1,45,7,10,1,6,1,3),_AvWlanMobVlanPeerAdvertiserPriority_Type())
avWlanMobVlanPeerAdvertiserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobVlanPeerAdvertiserPriority.setStatus(_A)
_AvWlanMobTunnelStatsTable_Object=MibTable
avWlanMobTunnelStatsTable=_AvWlanMobTunnelStatsTable_Object((1,3,6,1,4,1,45,7,10,1,7))
if mibBuilder.loadTexts:avWlanMobTunnelStatsTable.setStatus(_C)
_AvWlanMobTunnelStatsEntry_Object=MibTableRow
avWlanMobTunnelStatsEntry=_AvWlanMobTunnelStatsEntry_Object((1,3,6,1,4,1,45,7,10,1,7,1))
avWlanMobTunnelStatsEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:avWlanMobTunnelStatsEntry.setStatus(_C)
_AvWlanMobTunnelStatsDeviceId_Type=MacAddress
_AvWlanMobTunnelStatsDeviceId_Object=MibTableColumn
avWlanMobTunnelStatsDeviceId=_AvWlanMobTunnelStatsDeviceId_Object((1,3,6,1,4,1,45,7,10,1,7,1,1),_AvWlanMobTunnelStatsDeviceId_Type())
avWlanMobTunnelStatsDeviceId.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobTunnelStatsDeviceId.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts=_AvWlanMobTunnelStatsIngressPkts_Object((1,3,6,1,4,1,45,7,10,1,7,1,2),_AvWlanMobTunnelStatsIngressPkts_Type())
avWlanMobTunnelStatsIngressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts.setStatus(_C)
_AvWlanMobTunnelStatsIngressMcast_Type=Counter64
_AvWlanMobTunnelStatsIngressMcast_Object=MibTableColumn
avWlanMobTunnelStatsIngressMcast=_AvWlanMobTunnelStatsIngressMcast_Object((1,3,6,1,4,1,45,7,10,1,7,1,3),_AvWlanMobTunnelStatsIngressMcast_Type())
avWlanMobTunnelStatsIngressMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressMcast.setStatus(_C)
_AvWlanMobTunnelStatsIngressBcast_Type=Counter64
_AvWlanMobTunnelStatsIngressBcast_Object=MibTableColumn
avWlanMobTunnelStatsIngressBcast=_AvWlanMobTunnelStatsIngressBcast_Object((1,3,6,1,4,1,45,7,10,1,7,1,4),_AvWlanMobTunnelStatsIngressBcast_Type())
avWlanMobTunnelStatsIngressBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressBcast.setStatus(_C)
_AvWlanMobTunnelStatsIngressOctets_Type=Counter64
_AvWlanMobTunnelStatsIngressOctets_Object=MibTableColumn
avWlanMobTunnelStatsIngressOctets=_AvWlanMobTunnelStatsIngressOctets_Object((1,3,6,1,4,1,45,7,10,1,7,1,5),_AvWlanMobTunnelStatsIngressOctets_Type())
avWlanMobTunnelStatsIngressOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressOctets.setStatus(_C)
_AvWlanMobTunnelStatsIngressError_Type=Counter64
_AvWlanMobTunnelStatsIngressError_Object=MibTableColumn
avWlanMobTunnelStatsIngressError=_AvWlanMobTunnelStatsIngressError_Object((1,3,6,1,4,1,45,7,10,1,7,1,6),_AvWlanMobTunnelStatsIngressError_Type())
avWlanMobTunnelStatsIngressError.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressError.setStatus(_C)
_AvWlanMobTunnelStatsIngressDropped_Type=Counter64
_AvWlanMobTunnelStatsIngressDropped_Object=MibTableColumn
avWlanMobTunnelStatsIngressDropped=_AvWlanMobTunnelStatsIngressDropped_Object((1,3,6,1,4,1,45,7,10,1,7,1,7),_AvWlanMobTunnelStatsIngressDropped_Type())
avWlanMobTunnelStatsIngressDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressDropped.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts64_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts64_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts64=_AvWlanMobTunnelStatsIngressPkts64_Object((1,3,6,1,4,1,45,7,10,1,7,1,8),_AvWlanMobTunnelStatsIngressPkts64_Type())
avWlanMobTunnelStatsIngressPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts64.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts65to127_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts65to127_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts65to127=_AvWlanMobTunnelStatsIngressPkts65to127_Object((1,3,6,1,4,1,45,7,10,1,7,1,9),_AvWlanMobTunnelStatsIngressPkts65to127_Type())
avWlanMobTunnelStatsIngressPkts65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts65to127.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts128to255_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts128to255_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts128to255=_AvWlanMobTunnelStatsIngressPkts128to255_Object((1,3,6,1,4,1,45,7,10,1,7,1,10),_AvWlanMobTunnelStatsIngressPkts128to255_Type())
avWlanMobTunnelStatsIngressPkts128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts128to255.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts256to511_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts256to511_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts256to511=_AvWlanMobTunnelStatsIngressPkts256to511_Object((1,3,6,1,4,1,45,7,10,1,7,1,11),_AvWlanMobTunnelStatsIngressPkts256to511_Type())
avWlanMobTunnelStatsIngressPkts256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts256to511.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts512to1023_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts512to1023_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts512to1023=_AvWlanMobTunnelStatsIngressPkts512to1023_Object((1,3,6,1,4,1,45,7,10,1,7,1,12),_AvWlanMobTunnelStatsIngressPkts512to1023_Type())
avWlanMobTunnelStatsIngressPkts512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts512to1023.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts1024to1518_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts1024to1518_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts1024to1518=_AvWlanMobTunnelStatsIngressPkts1024to1518_Object((1,3,6,1,4,1,45,7,10,1,7,1,13),_AvWlanMobTunnelStatsIngressPkts1024to1518_Type())
avWlanMobTunnelStatsIngressPkts1024to1518.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts1024to1518.setStatus(_C)
_AvWlanMobTunnelStatsIngressPkts1522to9216_Type=Counter64
_AvWlanMobTunnelStatsIngressPkts1522to9216_Object=MibTableColumn
avWlanMobTunnelStatsIngressPkts1522to9216=_AvWlanMobTunnelStatsIngressPkts1522to9216_Object((1,3,6,1,4,1,45,7,10,1,7,1,14),_AvWlanMobTunnelStatsIngressPkts1522to9216_Type())
avWlanMobTunnelStatsIngressPkts1522to9216.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressPkts1522to9216.setStatus(_C)
_AvWlanMobTunnelStatsIngressFragments_Type=Counter64
_AvWlanMobTunnelStatsIngressFragments_Object=MibTableColumn
avWlanMobTunnelStatsIngressFragments=_AvWlanMobTunnelStatsIngressFragments_Object((1,3,6,1,4,1,45,7,10,1,7,1,15),_AvWlanMobTunnelStatsIngressFragments_Type())
avWlanMobTunnelStatsIngressFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressFragments.setStatus(_C)
_AvWlanMobTunnelStatsIngressFragmentsDrop_Type=Counter64
_AvWlanMobTunnelStatsIngressFragmentsDrop_Object=MibTableColumn
avWlanMobTunnelStatsIngressFragmentsDrop=_AvWlanMobTunnelStatsIngressFragmentsDrop_Object((1,3,6,1,4,1,45,7,10,1,7,1,16),_AvWlanMobTunnelStatsIngressFragmentsDrop_Type())
avWlanMobTunnelStatsIngressFragmentsDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressFragmentsDrop.setStatus(_C)
_AvWlanMobTunnelStatsIngressKeepAliveReq_Type=Counter64
_AvWlanMobTunnelStatsIngressKeepAliveReq_Object=MibTableColumn
avWlanMobTunnelStatsIngressKeepAliveReq=_AvWlanMobTunnelStatsIngressKeepAliveReq_Object((1,3,6,1,4,1,45,7,10,1,7,1,17),_AvWlanMobTunnelStatsIngressKeepAliveReq_Type())
avWlanMobTunnelStatsIngressKeepAliveReq.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressKeepAliveReq.setStatus(_C)
_AvWlanMobTunnelStatsIngressKeepAliveRsp_Type=Counter64
_AvWlanMobTunnelStatsIngressKeepAliveRsp_Object=MibTableColumn
avWlanMobTunnelStatsIngressKeepAliveRsp=_AvWlanMobTunnelStatsIngressKeepAliveRsp_Object((1,3,6,1,4,1,45,7,10,1,7,1,18),_AvWlanMobTunnelStatsIngressKeepAliveRsp_Type())
avWlanMobTunnelStatsIngressKeepAliveRsp.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressKeepAliveRsp.setStatus(_C)
_AvWlanMobTunnelStatsIngressDataRate_Type=CounterBasedGauge64
_AvWlanMobTunnelStatsIngressDataRate_Object=MibTableColumn
avWlanMobTunnelStatsIngressDataRate=_AvWlanMobTunnelStatsIngressDataRate_Object((1,3,6,1,4,1,45,7,10,1,7,1,19),_AvWlanMobTunnelStatsIngressDataRate_Type())
avWlanMobTunnelStatsIngressDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressDataRate.setStatus(_C)
if mibBuilder.loadTexts:avWlanMobTunnelStatsIngressDataRate.setUnits(_M)
_AvWlanMobTunnelStatsEgressPkts_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts=_AvWlanMobTunnelStatsEgressPkts_Object((1,3,6,1,4,1,45,7,10,1,7,1,20),_AvWlanMobTunnelStatsEgressPkts_Type())
avWlanMobTunnelStatsEgressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts.setStatus(_C)
_AvWlanMobTunnelStatsEgressMcast_Type=Counter64
_AvWlanMobTunnelStatsEgressMcast_Object=MibTableColumn
avWlanMobTunnelStatsEgressMcast=_AvWlanMobTunnelStatsEgressMcast_Object((1,3,6,1,4,1,45,7,10,1,7,1,21),_AvWlanMobTunnelStatsEgressMcast_Type())
avWlanMobTunnelStatsEgressMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressMcast.setStatus(_C)
_AvWlanMobTunnelStatsEgressBcast_Type=Counter64
_AvWlanMobTunnelStatsEgressBcast_Object=MibTableColumn
avWlanMobTunnelStatsEgressBcast=_AvWlanMobTunnelStatsEgressBcast_Object((1,3,6,1,4,1,45,7,10,1,7,1,22),_AvWlanMobTunnelStatsEgressBcast_Type())
avWlanMobTunnelStatsEgressBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressBcast.setStatus(_C)
_AvWlanMobTunnelStatsEgressOctets_Type=Counter64
_AvWlanMobTunnelStatsEgressOctets_Object=MibTableColumn
avWlanMobTunnelStatsEgressOctets=_AvWlanMobTunnelStatsEgressOctets_Object((1,3,6,1,4,1,45,7,10,1,7,1,23),_AvWlanMobTunnelStatsEgressOctets_Type())
avWlanMobTunnelStatsEgressOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressOctets.setStatus(_C)
_AvWlanMobTunnelStatsEgressError_Type=Counter64
_AvWlanMobTunnelStatsEgressError_Object=MibTableColumn
avWlanMobTunnelStatsEgressError=_AvWlanMobTunnelStatsEgressError_Object((1,3,6,1,4,1,45,7,10,1,7,1,24),_AvWlanMobTunnelStatsEgressError_Type())
avWlanMobTunnelStatsEgressError.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressError.setStatus(_C)
_AvWlanMobTunnelStatsEgressDropped_Type=Counter64
_AvWlanMobTunnelStatsEgressDropped_Object=MibTableColumn
avWlanMobTunnelStatsEgressDropped=_AvWlanMobTunnelStatsEgressDropped_Object((1,3,6,1,4,1,45,7,10,1,7,1,25),_AvWlanMobTunnelStatsEgressDropped_Type())
avWlanMobTunnelStatsEgressDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressDropped.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts64_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts64_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts64=_AvWlanMobTunnelStatsEgressPkts64_Object((1,3,6,1,4,1,45,7,10,1,7,1,26),_AvWlanMobTunnelStatsEgressPkts64_Type())
avWlanMobTunnelStatsEgressPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts64.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts65to127_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts65to127_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts65to127=_AvWlanMobTunnelStatsEgressPkts65to127_Object((1,3,6,1,4,1,45,7,10,1,7,1,27),_AvWlanMobTunnelStatsEgressPkts65to127_Type())
avWlanMobTunnelStatsEgressPkts65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts65to127.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts128to255_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts128to255_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts128to255=_AvWlanMobTunnelStatsEgressPkts128to255_Object((1,3,6,1,4,1,45,7,10,1,7,1,28),_AvWlanMobTunnelStatsEgressPkts128to255_Type())
avWlanMobTunnelStatsEgressPkts128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts128to255.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts256to511_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts256to511_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts256to511=_AvWlanMobTunnelStatsEgressPkts256to511_Object((1,3,6,1,4,1,45,7,10,1,7,1,29),_AvWlanMobTunnelStatsEgressPkts256to511_Type())
avWlanMobTunnelStatsEgressPkts256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts256to511.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts512to1023_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts512to1023_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts512to1023=_AvWlanMobTunnelStatsEgressPkts512to1023_Object((1,3,6,1,4,1,45,7,10,1,7,1,30),_AvWlanMobTunnelStatsEgressPkts512to1023_Type())
avWlanMobTunnelStatsEgressPkts512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts512to1023.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts1024to1518_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts1024to1518_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts1024to1518=_AvWlanMobTunnelStatsEgressPkts1024to1518_Object((1,3,6,1,4,1,45,7,10,1,7,1,31),_AvWlanMobTunnelStatsEgressPkts1024to1518_Type())
avWlanMobTunnelStatsEgressPkts1024to1518.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts1024to1518.setStatus(_C)
_AvWlanMobTunnelStatsEgressPkts1522to9216_Type=Counter64
_AvWlanMobTunnelStatsEgressPkts1522to9216_Object=MibTableColumn
avWlanMobTunnelStatsEgressPkts1522to9216=_AvWlanMobTunnelStatsEgressPkts1522to9216_Object((1,3,6,1,4,1,45,7,10,1,7,1,32),_AvWlanMobTunnelStatsEgressPkts1522to9216_Type())
avWlanMobTunnelStatsEgressPkts1522to9216.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressPkts1522to9216.setStatus(_C)
_AvWlanMobTunnelStatsEgressFragments_Type=Counter64
_AvWlanMobTunnelStatsEgressFragments_Object=MibTableColumn
avWlanMobTunnelStatsEgressFragments=_AvWlanMobTunnelStatsEgressFragments_Object((1,3,6,1,4,1,45,7,10,1,7,1,33),_AvWlanMobTunnelStatsEgressFragments_Type())
avWlanMobTunnelStatsEgressFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressFragments.setStatus(_C)
_AvWlanMobTunnelStatsEgressKeepAliveReq_Type=Counter64
_AvWlanMobTunnelStatsEgressKeepAliveReq_Object=MibTableColumn
avWlanMobTunnelStatsEgressKeepAliveReq=_AvWlanMobTunnelStatsEgressKeepAliveReq_Object((1,3,6,1,4,1,45,7,10,1,7,1,34),_AvWlanMobTunnelStatsEgressKeepAliveReq_Type())
avWlanMobTunnelStatsEgressKeepAliveReq.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressKeepAliveReq.setStatus(_C)
_AvWlanMobTunnelStatsEgressKeepAliveRsp_Type=Counter64
_AvWlanMobTunnelStatsEgressKeepAliveRsp_Object=MibTableColumn
avWlanMobTunnelStatsEgressKeepAliveRsp=_AvWlanMobTunnelStatsEgressKeepAliveRsp_Object((1,3,6,1,4,1,45,7,10,1,7,1,35),_AvWlanMobTunnelStatsEgressKeepAliveRsp_Type())
avWlanMobTunnelStatsEgressKeepAliveRsp.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressKeepAliveRsp.setStatus(_C)
_AvWlanMobTunnelStatsEgressDataRate_Type=CounterBasedGauge64
_AvWlanMobTunnelStatsEgressDataRate_Object=MibTableColumn
avWlanMobTunnelStatsEgressDataRate=_AvWlanMobTunnelStatsEgressDataRate_Object((1,3,6,1,4,1,45,7,10,1,7,1,36),_AvWlanMobTunnelStatsEgressDataRate_Type())
avWlanMobTunnelStatsEgressDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressDataRate.setStatus(_C)
if mibBuilder.loadTexts:avWlanMobTunnelStatsEgressDataRate.setUnits(_M)
class _AvWlanMobTunnelStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_N,2)))
_AvWlanMobTunnelStatsReset_Type.__name__=_D
_AvWlanMobTunnelStatsReset_Object=MibTableColumn
avWlanMobTunnelStatsReset=_AvWlanMobTunnelStatsReset_Object((1,3,6,1,4,1,45,7,10,1,7,1,37),_AvWlanMobTunnelStatsReset_Type())
avWlanMobTunnelStatsReset.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobTunnelStatsReset.setStatus(_C)
_AvWlanMobSwTunnelStatisticsTable_Object=MibTable
avWlanMobSwTunnelStatisticsTable=_AvWlanMobSwTunnelStatisticsTable_Object((1,3,6,1,4,1,45,7,10,1,8))
if mibBuilder.loadTexts:avWlanMobSwTunnelStatisticsTable.setStatus(_A)
_AvWlanMobSwTunnelStatisticsEntry_Object=MibTableRow
avWlanMobSwTunnelStatisticsEntry=_AvWlanMobSwTunnelStatisticsEntry_Object((1,3,6,1,4,1,45,7,10,1,8,1))
avWlanMobSwTunnelStatisticsEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:avWlanMobSwTunnelStatisticsEntry.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts_Type=Counter64
_AvWlanMobSwTunnelIngressPkts_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts=_AvWlanMobSwTunnelIngressPkts_Object((1,3,6,1,4,1,45,7,10,1,8,1,1),_AvWlanMobSwTunnelIngressPkts_Type())
avWlanMobSwTunnelIngressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts.setStatus(_A)
_AvWlanMobSwTunnelIngressMcast_Type=Counter64
_AvWlanMobSwTunnelIngressMcast_Object=MibTableColumn
avWlanMobSwTunnelIngressMcast=_AvWlanMobSwTunnelIngressMcast_Object((1,3,6,1,4,1,45,7,10,1,8,1,2),_AvWlanMobSwTunnelIngressMcast_Type())
avWlanMobSwTunnelIngressMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressMcast.setStatus(_A)
_AvWlanMobSwTunnelIngressBcast_Type=Counter64
_AvWlanMobSwTunnelIngressBcast_Object=MibTableColumn
avWlanMobSwTunnelIngressBcast=_AvWlanMobSwTunnelIngressBcast_Object((1,3,6,1,4,1,45,7,10,1,8,1,3),_AvWlanMobSwTunnelIngressBcast_Type())
avWlanMobSwTunnelIngressBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressBcast.setStatus(_A)
_AvWlanMobSwTunnelIngressOctets_Type=Counter64
_AvWlanMobSwTunnelIngressOctets_Object=MibTableColumn
avWlanMobSwTunnelIngressOctets=_AvWlanMobSwTunnelIngressOctets_Object((1,3,6,1,4,1,45,7,10,1,8,1,4),_AvWlanMobSwTunnelIngressOctets_Type())
avWlanMobSwTunnelIngressOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressOctets.setStatus(_A)
_AvWlanMobSwTunnelIngressError_Type=Counter64
_AvWlanMobSwTunnelIngressError_Object=MibTableColumn
avWlanMobSwTunnelIngressError=_AvWlanMobSwTunnelIngressError_Object((1,3,6,1,4,1,45,7,10,1,8,1,5),_AvWlanMobSwTunnelIngressError_Type())
avWlanMobSwTunnelIngressError.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressError.setStatus(_A)
_AvWlanMobSwTunnelIngressDropped_Type=Counter64
_AvWlanMobSwTunnelIngressDropped_Object=MibTableColumn
avWlanMobSwTunnelIngressDropped=_AvWlanMobSwTunnelIngressDropped_Object((1,3,6,1,4,1,45,7,10,1,8,1,6),_AvWlanMobSwTunnelIngressDropped_Type())
avWlanMobSwTunnelIngressDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressDropped.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts64_Type=Counter64
_AvWlanMobSwTunnelIngressPkts64_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts64=_AvWlanMobSwTunnelIngressPkts64_Object((1,3,6,1,4,1,45,7,10,1,8,1,7),_AvWlanMobSwTunnelIngressPkts64_Type())
avWlanMobSwTunnelIngressPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts64.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts65to127_Type=Counter64
_AvWlanMobSwTunnelIngressPkts65to127_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts65to127=_AvWlanMobSwTunnelIngressPkts65to127_Object((1,3,6,1,4,1,45,7,10,1,8,1,8),_AvWlanMobSwTunnelIngressPkts65to127_Type())
avWlanMobSwTunnelIngressPkts65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts65to127.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts128to255_Type=Counter64
_AvWlanMobSwTunnelIngressPkts128to255_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts128to255=_AvWlanMobSwTunnelIngressPkts128to255_Object((1,3,6,1,4,1,45,7,10,1,8,1,9),_AvWlanMobSwTunnelIngressPkts128to255_Type())
avWlanMobSwTunnelIngressPkts128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts128to255.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts256to511_Type=Counter64
_AvWlanMobSwTunnelIngressPkts256to511_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts256to511=_AvWlanMobSwTunnelIngressPkts256to511_Object((1,3,6,1,4,1,45,7,10,1,8,1,10),_AvWlanMobSwTunnelIngressPkts256to511_Type())
avWlanMobSwTunnelIngressPkts256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts256to511.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts512to1023_Type=Counter64
_AvWlanMobSwTunnelIngressPkts512to1023_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts512to1023=_AvWlanMobSwTunnelIngressPkts512to1023_Object((1,3,6,1,4,1,45,7,10,1,8,1,11),_AvWlanMobSwTunnelIngressPkts512to1023_Type())
avWlanMobSwTunnelIngressPkts512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts512to1023.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts1024to1518_Type=Counter64
_AvWlanMobSwTunnelIngressPkts1024to1518_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts1024to1518=_AvWlanMobSwTunnelIngressPkts1024to1518_Object((1,3,6,1,4,1,45,7,10,1,8,1,12),_AvWlanMobSwTunnelIngressPkts1024to1518_Type())
avWlanMobSwTunnelIngressPkts1024to1518.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts1024to1518.setStatus(_A)
_AvWlanMobSwTunnelIngressPkts1522to9216_Type=Counter64
_AvWlanMobSwTunnelIngressPkts1522to9216_Object=MibTableColumn
avWlanMobSwTunnelIngressPkts1522to9216=_AvWlanMobSwTunnelIngressPkts1522to9216_Object((1,3,6,1,4,1,45,7,10,1,8,1,13),_AvWlanMobSwTunnelIngressPkts1522to9216_Type())
avWlanMobSwTunnelIngressPkts1522to9216.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressPkts1522to9216.setStatus(_A)
_AvWlanMobSwTunnelIngressFragments_Type=Counter64
_AvWlanMobSwTunnelIngressFragments_Object=MibTableColumn
avWlanMobSwTunnelIngressFragments=_AvWlanMobSwTunnelIngressFragments_Object((1,3,6,1,4,1,45,7,10,1,8,1,14),_AvWlanMobSwTunnelIngressFragments_Type())
avWlanMobSwTunnelIngressFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressFragments.setStatus(_A)
_AvWlanMobSwTunnelIngressFragmentsDrop_Type=Counter64
_AvWlanMobSwTunnelIngressFragmentsDrop_Object=MibTableColumn
avWlanMobSwTunnelIngressFragmentsDrop=_AvWlanMobSwTunnelIngressFragmentsDrop_Object((1,3,6,1,4,1,45,7,10,1,8,1,15),_AvWlanMobSwTunnelIngressFragmentsDrop_Type())
avWlanMobSwTunnelIngressFragmentsDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressFragmentsDrop.setStatus(_A)
_AvWlanMobSwTunnelIngressKeepAliveReq_Type=Counter64
_AvWlanMobSwTunnelIngressKeepAliveReq_Object=MibTableColumn
avWlanMobSwTunnelIngressKeepAliveReq=_AvWlanMobSwTunnelIngressKeepAliveReq_Object((1,3,6,1,4,1,45,7,10,1,8,1,16),_AvWlanMobSwTunnelIngressKeepAliveReq_Type())
avWlanMobSwTunnelIngressKeepAliveReq.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressKeepAliveReq.setStatus(_A)
_AvWlanMobSwTunnelIngressKeepAliveRsp_Type=Counter64
_AvWlanMobSwTunnelIngressKeepAliveRsp_Object=MibTableColumn
avWlanMobSwTunnelIngressKeepAliveRsp=_AvWlanMobSwTunnelIngressKeepAliveRsp_Object((1,3,6,1,4,1,45,7,10,1,8,1,17),_AvWlanMobSwTunnelIngressKeepAliveRsp_Type())
avWlanMobSwTunnelIngressKeepAliveRsp.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressKeepAliveRsp.setStatus(_A)
_AvWlanMobSwTunnelIngressDataRate_Type=CounterBasedGauge64
_AvWlanMobSwTunnelIngressDataRate_Object=MibTableColumn
avWlanMobSwTunnelIngressDataRate=_AvWlanMobSwTunnelIngressDataRate_Object((1,3,6,1,4,1,45,7,10,1,8,1,18),_AvWlanMobSwTunnelIngressDataRate_Type())
avWlanMobSwTunnelIngressDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressDataRate.setStatus(_A)
if mibBuilder.loadTexts:avWlanMobSwTunnelIngressDataRate.setUnits(_M)
_AvWlanMobSwTunnelEgressPkts_Type=Counter64
_AvWlanMobSwTunnelEgressPkts_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts=_AvWlanMobSwTunnelEgressPkts_Object((1,3,6,1,4,1,45,7,10,1,8,1,19),_AvWlanMobSwTunnelEgressPkts_Type())
avWlanMobSwTunnelEgressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts.setStatus(_A)
_AvWlanMobSwTunnelEgressMcast_Type=Counter64
_AvWlanMobSwTunnelEgressMcast_Object=MibTableColumn
avWlanMobSwTunnelEgressMcast=_AvWlanMobSwTunnelEgressMcast_Object((1,3,6,1,4,1,45,7,10,1,8,1,20),_AvWlanMobSwTunnelEgressMcast_Type())
avWlanMobSwTunnelEgressMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressMcast.setStatus(_A)
_AvWlanMobSwTunnelEgressBcast_Type=Counter64
_AvWlanMobSwTunnelEgressBcast_Object=MibTableColumn
avWlanMobSwTunnelEgressBcast=_AvWlanMobSwTunnelEgressBcast_Object((1,3,6,1,4,1,45,7,10,1,8,1,21),_AvWlanMobSwTunnelEgressBcast_Type())
avWlanMobSwTunnelEgressBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressBcast.setStatus(_A)
_AvWlanMobSwTunnelEgressOctets_Type=Counter64
_AvWlanMobSwTunnelEgressOctets_Object=MibTableColumn
avWlanMobSwTunnelEgressOctets=_AvWlanMobSwTunnelEgressOctets_Object((1,3,6,1,4,1,45,7,10,1,8,1,22),_AvWlanMobSwTunnelEgressOctets_Type())
avWlanMobSwTunnelEgressOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressOctets.setStatus(_A)
_AvWlanMobSwTunnelEgressError_Type=Counter64
_AvWlanMobSwTunnelEgressError_Object=MibTableColumn
avWlanMobSwTunnelEgressError=_AvWlanMobSwTunnelEgressError_Object((1,3,6,1,4,1,45,7,10,1,8,1,23),_AvWlanMobSwTunnelEgressError_Type())
avWlanMobSwTunnelEgressError.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressError.setStatus(_A)
_AvWlanMobSwTunnelEgressDropped_Type=Counter64
_AvWlanMobSwTunnelEgressDropped_Object=MibTableColumn
avWlanMobSwTunnelEgressDropped=_AvWlanMobSwTunnelEgressDropped_Object((1,3,6,1,4,1,45,7,10,1,8,1,24),_AvWlanMobSwTunnelEgressDropped_Type())
avWlanMobSwTunnelEgressDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressDropped.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts64_Type=Counter64
_AvWlanMobSwTunnelEgressPkts64_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts64=_AvWlanMobSwTunnelEgressPkts64_Object((1,3,6,1,4,1,45,7,10,1,8,1,25),_AvWlanMobSwTunnelEgressPkts64_Type())
avWlanMobSwTunnelEgressPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts64.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts65to127_Type=Counter64
_AvWlanMobSwTunnelEgressPkts65to127_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts65to127=_AvWlanMobSwTunnelEgressPkts65to127_Object((1,3,6,1,4,1,45,7,10,1,8,1,26),_AvWlanMobSwTunnelEgressPkts65to127_Type())
avWlanMobSwTunnelEgressPkts65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts65to127.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts128to255_Type=Counter64
_AvWlanMobSwTunnelEgressPkts128to255_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts128to255=_AvWlanMobSwTunnelEgressPkts128to255_Object((1,3,6,1,4,1,45,7,10,1,8,1,27),_AvWlanMobSwTunnelEgressPkts128to255_Type())
avWlanMobSwTunnelEgressPkts128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts128to255.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts256to511_Type=Counter64
_AvWlanMobSwTunnelEgressPkts256to511_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts256to511=_AvWlanMobSwTunnelEgressPkts256to511_Object((1,3,6,1,4,1,45,7,10,1,8,1,28),_AvWlanMobSwTunnelEgressPkts256to511_Type())
avWlanMobSwTunnelEgressPkts256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts256to511.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts512to1023_Type=Counter64
_AvWlanMobSwTunnelEgressPkts512to1023_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts512to1023=_AvWlanMobSwTunnelEgressPkts512to1023_Object((1,3,6,1,4,1,45,7,10,1,8,1,29),_AvWlanMobSwTunnelEgressPkts512to1023_Type())
avWlanMobSwTunnelEgressPkts512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts512to1023.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts1024to1518_Type=Counter64
_AvWlanMobSwTunnelEgressPkts1024to1518_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts1024to1518=_AvWlanMobSwTunnelEgressPkts1024to1518_Object((1,3,6,1,4,1,45,7,10,1,8,1,30),_AvWlanMobSwTunnelEgressPkts1024to1518_Type())
avWlanMobSwTunnelEgressPkts1024to1518.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts1024to1518.setStatus(_A)
_AvWlanMobSwTunnelEgressPkts1522to9216_Type=Counter64
_AvWlanMobSwTunnelEgressPkts1522to9216_Object=MibTableColumn
avWlanMobSwTunnelEgressPkts1522to9216=_AvWlanMobSwTunnelEgressPkts1522to9216_Object((1,3,6,1,4,1,45,7,10,1,8,1,31),_AvWlanMobSwTunnelEgressPkts1522to9216_Type())
avWlanMobSwTunnelEgressPkts1522to9216.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressPkts1522to9216.setStatus(_A)
_AvWlanMobSwTunnelEgressFragments_Type=Counter64
_AvWlanMobSwTunnelEgressFragments_Object=MibTableColumn
avWlanMobSwTunnelEgressFragments=_AvWlanMobSwTunnelEgressFragments_Object((1,3,6,1,4,1,45,7,10,1,8,1,32),_AvWlanMobSwTunnelEgressFragments_Type())
avWlanMobSwTunnelEgressFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressFragments.setStatus(_A)
_AvWlanMobSwTunnelEgressKeepAliveReq_Type=Counter64
_AvWlanMobSwTunnelEgressKeepAliveReq_Object=MibTableColumn
avWlanMobSwTunnelEgressKeepAliveReq=_AvWlanMobSwTunnelEgressKeepAliveReq_Object((1,3,6,1,4,1,45,7,10,1,8,1,33),_AvWlanMobSwTunnelEgressKeepAliveReq_Type())
avWlanMobSwTunnelEgressKeepAliveReq.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressKeepAliveReq.setStatus(_A)
_AvWlanMobSwTunnelEgressKeepAliveRsp_Type=Counter64
_AvWlanMobSwTunnelEgressKeepAliveRsp_Object=MibTableColumn
avWlanMobSwTunnelEgressKeepAliveRsp=_AvWlanMobSwTunnelEgressKeepAliveRsp_Object((1,3,6,1,4,1,45,7,10,1,8,1,34),_AvWlanMobSwTunnelEgressKeepAliveRsp_Type())
avWlanMobSwTunnelEgressKeepAliveRsp.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressKeepAliveRsp.setStatus(_A)
_AvWlanMobSwTunnelEgressDataRate_Type=CounterBasedGauge64
_AvWlanMobSwTunnelEgressDataRate_Object=MibTableColumn
avWlanMobSwTunnelEgressDataRate=_AvWlanMobSwTunnelEgressDataRate_Object((1,3,6,1,4,1,45,7,10,1,8,1,35),_AvWlanMobSwTunnelEgressDataRate_Type())
avWlanMobSwTunnelEgressDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressDataRate.setStatus(_A)
if mibBuilder.loadTexts:avWlanMobSwTunnelEgressDataRate.setUnits(_M)
class _AvWlanMobSwTunnelResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_N,2)))
_AvWlanMobSwTunnelResetStats_Type.__name__=_D
_AvWlanMobSwTunnelResetStats_Object=MibTableColumn
avWlanMobSwTunnelResetStats=_AvWlanMobSwTunnelResetStats_Object((1,3,6,1,4,1,45,7,10,1,8,1,36),_AvWlanMobSwTunnelResetStats_Type())
avWlanMobSwTunnelResetStats.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwTunnelResetStats.setStatus(_A)
_AvWlanMobSwTunnelIpAddressType_Type=InetAddressType
_AvWlanMobSwTunnelIpAddressType_Object=MibTableColumn
avWlanMobSwTunnelIpAddressType=_AvWlanMobSwTunnelIpAddressType_Object((1,3,6,1,4,1,45,7,10,1,8,1,37),_AvWlanMobSwTunnelIpAddressType_Type())
avWlanMobSwTunnelIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIpAddressType.setStatus(_A)
class _AvWlanMobSwTunnelIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AvWlanMobSwTunnelIpAddress_Type.__name__=_K
_AvWlanMobSwTunnelIpAddress_Object=MibTableColumn
avWlanMobSwTunnelIpAddress=_AvWlanMobSwTunnelIpAddress_Object((1,3,6,1,4,1,45,7,10,1,8,1,38),_AvWlanMobSwTunnelIpAddress_Type())
avWlanMobSwTunnelIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelIpAddress.setStatus(_A)
_AvWlanMobSwTunnelInterfaceId_Type=Integer32
_AvWlanMobSwTunnelInterfaceId_Object=MibTableColumn
avWlanMobSwTunnelInterfaceId=_AvWlanMobSwTunnelInterfaceId_Object((1,3,6,1,4,1,45,7,10,1,8,1,39),_AvWlanMobSwTunnelInterfaceId_Type())
avWlanMobSwTunnelInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwTunnelInterfaceId.setStatus(_A)
_AvWlanMobSwControllerTable_Object=MibTable
avWlanMobSwControllerTable=_AvWlanMobSwControllerTable_Object((1,3,6,1,4,1,45,7,10,1,9))
if mibBuilder.loadTexts:avWlanMobSwControllerTable.setStatus(_A)
_AvWlanMobSwControllerEntry_Object=MibTableRow
avWlanMobSwControllerEntry=_AvWlanMobSwControllerEntry_Object((1,3,6,1,4,1,45,7,10,1,9,1))
avWlanMobSwControllerEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:avWlanMobSwControllerEntry.setStatus(_A)
class _AvWlanMobSwControllerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AvWlanMobSwControllerId_Type.__name__=_D
_AvWlanMobSwControllerId_Object=MibTableColumn
avWlanMobSwControllerId=_AvWlanMobSwControllerId_Object((1,3,6,1,4,1,45,7,10,1,9,1,1),_AvWlanMobSwControllerId_Type())
avWlanMobSwControllerId.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobSwControllerId.setStatus(_A)
_AvWlanMobSwControllerAddrType_Type=InetAddressType
_AvWlanMobSwControllerAddrType_Object=MibTableColumn
avWlanMobSwControllerAddrType=_AvWlanMobSwControllerAddrType_Object((1,3,6,1,4,1,45,7,10,1,9,1,2),_AvWlanMobSwControllerAddrType_Type())
avWlanMobSwControllerAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobSwControllerAddrType.setStatus(_A)
class _AvWlanMobSwControllerAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AvWlanMobSwControllerAddr_Type.__name__=_K
_AvWlanMobSwControllerAddr_Object=MibTableColumn
avWlanMobSwControllerAddr=_AvWlanMobSwControllerAddr_Object((1,3,6,1,4,1,45,7,10,1,9,1,3),_AvWlanMobSwControllerAddr_Type())
avWlanMobSwControllerAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobSwControllerAddr.setStatus(_A)
_AvWlanMobSwControllerRowStatus_Type=RowStatus
_AvWlanMobSwControllerRowStatus_Object=MibTableColumn
avWlanMobSwControllerRowStatus=_AvWlanMobSwControllerRowStatus_Object((1,3,6,1,4,1,45,7,10,1,9,1,4),_AvWlanMobSwControllerRowStatus_Type())
avWlanMobSwControllerRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:avWlanMobSwControllerRowStatus.setStatus(_A)
_AvWlanMobSwFdbTable_Object=MibTable
avWlanMobSwFdbTable=_AvWlanMobSwFdbTable_Object((1,3,6,1,4,1,45,7,10,1,10))
if mibBuilder.loadTexts:avWlanMobSwFdbTable.setStatus(_A)
_AvWlanMobSwFdbEntry_Object=MibTableRow
avWlanMobSwFdbEntry=_AvWlanMobSwFdbEntry_Object((1,3,6,1,4,1,45,7,10,1,10,1))
avWlanMobSwFdbEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:avWlanMobSwFdbEntry.setStatus(_A)
_AvWlanMobSwFdbVlanId_Type=VlanIdOrNone
_AvWlanMobSwFdbVlanId_Object=MibTableColumn
avWlanMobSwFdbVlanId=_AvWlanMobSwFdbVlanId_Object((1,3,6,1,4,1,45,7,10,1,10,1,1),_AvWlanMobSwFdbVlanId_Type())
avWlanMobSwFdbVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobSwFdbVlanId.setStatus(_A)
_AvWlanMobSwFdbMacAddress_Type=MacAddress
_AvWlanMobSwFdbMacAddress_Object=MibTableColumn
avWlanMobSwFdbMacAddress=_AvWlanMobSwFdbMacAddress_Object((1,3,6,1,4,1,45,7,10,1,10,1,2),_AvWlanMobSwFdbMacAddress_Type())
avWlanMobSwFdbMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:avWlanMobSwFdbMacAddress.setStatus(_A)
class _AvWlanMobSwFdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('static',5)))
_AvWlanMobSwFdbType_Type.__name__=_D
_AvWlanMobSwFdbType_Object=MibTableColumn
avWlanMobSwFdbType=_AvWlanMobSwFdbType_Object((1,3,6,1,4,1,45,7,10,1,10,1,3),_AvWlanMobSwFdbType_Type())
avWlanMobSwFdbType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbType.setStatus(_A)
class _AvWlanMobSwFdbTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3)))
_AvWlanMobSwFdbTunnelType_Type.__name__=_D
_AvWlanMobSwFdbTunnelType_Object=MibTableColumn
avWlanMobSwFdbTunnelType=_AvWlanMobSwFdbTunnelType_Object((1,3,6,1,4,1,45,7,10,1,10,1,4),_AvWlanMobSwFdbTunnelType_Type())
avWlanMobSwFdbTunnelType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbTunnelType.setStatus(_A)
_AvWlanMobSwFdbRemoteEndpointId_Type=MacAddress
_AvWlanMobSwFdbRemoteEndpointId_Object=MibTableColumn
avWlanMobSwFdbRemoteEndpointId=_AvWlanMobSwFdbRemoteEndpointId_Object((1,3,6,1,4,1,45,7,10,1,10,1,5),_AvWlanMobSwFdbRemoteEndpointId_Type())
avWlanMobSwFdbRemoteEndpointId.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbRemoteEndpointId.setStatus(_A)
_AvWlanMobSwFdbRemoteEndpointAddrType_Type=InetAddressType
_AvWlanMobSwFdbRemoteEndpointAddrType_Object=MibTableColumn
avWlanMobSwFdbRemoteEndpointAddrType=_AvWlanMobSwFdbRemoteEndpointAddrType_Object((1,3,6,1,4,1,45,7,10,1,10,1,6),_AvWlanMobSwFdbRemoteEndpointAddrType_Type())
avWlanMobSwFdbRemoteEndpointAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbRemoteEndpointAddrType.setStatus(_A)
class _AvWlanMobSwFdbRemoteEndpointAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AvWlanMobSwFdbRemoteEndpointAddr_Type.__name__=_K
_AvWlanMobSwFdbRemoteEndpointAddr_Object=MibTableColumn
avWlanMobSwFdbRemoteEndpointAddr=_AvWlanMobSwFdbRemoteEndpointAddr_Object((1,3,6,1,4,1,45,7,10,1,10,1,7),_AvWlanMobSwFdbRemoteEndpointAddr_Type())
avWlanMobSwFdbRemoteEndpointAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbRemoteEndpointAddr.setStatus(_A)
_AvWlanMobSwFdbRemoteEndpointUdpPort_Type=InetPortNumber
_AvWlanMobSwFdbRemoteEndpointUdpPort_Object=MibTableColumn
avWlanMobSwFdbRemoteEndpointUdpPort=_AvWlanMobSwFdbRemoteEndpointUdpPort_Object((1,3,6,1,4,1,45,7,10,1,10,1,8),_AvWlanMobSwFdbRemoteEndpointUdpPort_Type())
avWlanMobSwFdbRemoteEndpointUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbRemoteEndpointUdpPort.setStatus(_A)
_AvWlanMobSwFdbLocalEndpointUdpPort_Type=InetPortNumber
_AvWlanMobSwFdbLocalEndpointUdpPort_Object=MibTableColumn
avWlanMobSwFdbLocalEndpointUdpPort=_AvWlanMobSwFdbLocalEndpointUdpPort_Object((1,3,6,1,4,1,45,7,10,1,10,1,9),_AvWlanMobSwFdbLocalEndpointUdpPort_Type())
avWlanMobSwFdbLocalEndpointUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbLocalEndpointUdpPort.setStatus(_A)
_AvWlanMobSwFdbInterfaceId_Type=Integer32
_AvWlanMobSwFdbInterfaceId_Object=MibTableColumn
avWlanMobSwFdbInterfaceId=_AvWlanMobSwFdbInterfaceId_Object((1,3,6,1,4,1,45,7,10,1,10,1,10),_AvWlanMobSwFdbInterfaceId_Type())
avWlanMobSwFdbInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:avWlanMobSwFdbInterfaceId.setStatus(_A)
class _AvWlanMobSwFdbFlushAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('flush',2)))
_AvWlanMobSwFdbFlushAction_Type.__name__=_D
_AvWlanMobSwFdbFlushAction_Object=MibTableColumn
avWlanMobSwFdbFlushAction=_AvWlanMobSwFdbFlushAction_Object((1,3,6,1,4,1,45,7,10,1,10,1,11),_AvWlanMobSwFdbFlushAction_Type())
avWlanMobSwFdbFlushAction.setMaxAccess(_G)
if mibBuilder.loadTexts:avWlanMobSwFdbFlushAction.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'avayaWlanMobSwMib':avayaWlanMobSwMib,'avWlanMobSwObjects':avWlanMobSwObjects,'avWlanMobAgentObjects':avWlanMobAgentObjects,'avWlanMobAgentVlanTable':avWlanMobAgentVlanTable,'avWlanMobAgentVlanEntry':avWlanMobAgentVlanEntry,_Q:avWlanMobAgentVlanName,'avWlanMobAgentVlanLVID':avWlanMobAgentVlanLVID,'avWlanMobAgentVlanL3Mobility':avWlanMobAgentVlanL3Mobility,'avWlanMobAgentVlanWeight':avWlanMobAgentVlanWeight,'avWlanMobAgentVlanTrack':avWlanMobAgentVlanTrack,'avWlanMobAgentVlanScope':avWlanMobAgentVlanScope,'avWlanMobAgentVlanWcValidated':avWlanMobAgentVlanWcValidated,'avWlanMobAgentVlanAdminMapped':avWlanMobAgentVlanAdminMapped,'avWlanMobAgentVlanActive':avWlanMobAgentVlanActive,'avWlanMobAgentVlanRowStatus':avWlanMobAgentVlanRowStatus,'avWlanMobSwScalars':avWlanMobSwScalars,'avWlanMobSwVLANPeriodicAdvInterval':avWlanMobSwVLANPeriodicAdvInterval,'avWlanMobSwVMMMaxRetransmits':avWlanMobSwVMMMaxRetransmits,'avWlanMobSwKeepAliveInterval':avWlanMobSwKeepAliveInterval,'avWlanMobSwKeepAliveNumRetries':avWlanMobSwKeepAliveNumRetries,'avWlanMobSwTransMaxRetransmits':avWlanMobSwTransMaxRetransmits,'avWlanMobSwLocalDeviceId':avWlanMobSwLocalDeviceId,'avWlanMobSwAllStatisticsReset':avWlanMobSwAllStatisticsReset,'avWlanMobSwAllStatisticsResetStatus':avWlanMobSwAllStatisticsResetStatus,'avWlanMobSwCtrlAddrType':avWlanMobSwCtrlAddrType,'avWlanMobSwCtrlAddr':avWlanMobSwCtrlAddr,'avWlanMobSwNumMobilityTunnels':avWlanMobSwNumMobilityTunnels,'avWlanMobSwNumAccessTunnels':avWlanMobSwNumAccessTunnels,'avWlanMobSwNumResPeerAccessTunnels':avWlanMobSwNumResPeerAccessTunnels,'avWlanMobSwFdbGlobalFlushAction':avWlanMobSwFdbGlobalFlushAction,'avWlanMobSwFdbGlobalFlushActionStatus':avWlanMobSwFdbGlobalFlushActionStatus,'avWlanMobSwPurgeInactiveMaps':avWlanMobSwPurgeInactiveMaps,'avWlanMobSwDeviceTable':avWlanMobSwDeviceTable,'avWlanMobSwDeviceEntry':avWlanMobSwDeviceEntry,_O:avWlanMobSwDeviceType,_P:avWlanMobSwDeviceId,'avWlanMobSwDeviceAddrType':avWlanMobSwDeviceAddrType,'avWlanMobSwDeviceAddr':avWlanMobSwDeviceAddr,'avWlanMobSwDeviceUdpPort':avWlanMobSwDeviceUdpPort,'avWlanMobSwDeviceStatus':avWlanMobSwDeviceStatus,'avWlanMobSwDeviceLocalUdpPort':avWlanMobSwDeviceLocalUdpPort,'avWlanMobSwDeviceInterfaceId':avWlanMobSwDeviceInterfaceId,'avWlanMobPeerVlansAdvertisedTable':avWlanMobPeerVlansAdvertisedTable,'avWlanMobPeerVlansAdvertisedEntry':avWlanMobPeerVlansAdvertisedEntry,_Y:avWlanMobPeerVlansAdvertisedId,_Z:avWlanMobPeerVlansAdvertisedVlanName,'avWlanMobPeerVlansAdvertisedPriority':avWlanMobPeerVlansAdvertisedPriority,'avWlanMobVlanServerTable':avWlanMobVlanServerTable,'avWlanMobVlanServerEntry':avWlanMobVlanServerEntry,_a:avWlanMobVlanServerVlanName,'avWlanMobVlanServerId':avWlanMobVlanServerId,'avWlanMobVlanServerPriority':avWlanMobVlanServerPriority,'avWlanMobVlanPeerAdvertiserTable':avWlanMobVlanPeerAdvertiserTable,'avWlanMobVlanPeerAdvertiserEntry':avWlanMobVlanPeerAdvertiserEntry,_b:avWlanMobVlanPeerAdvertiserVlanName,_c:avWlanMobVlanPeerAdvertiserId,'avWlanMobVlanPeerAdvertiserPriority':avWlanMobVlanPeerAdvertiserPriority,'avWlanMobTunnelStatsTable':avWlanMobTunnelStatsTable,'avWlanMobTunnelStatsEntry':avWlanMobTunnelStatsEntry,_d:avWlanMobTunnelStatsDeviceId,'avWlanMobTunnelStatsIngressPkts':avWlanMobTunnelStatsIngressPkts,'avWlanMobTunnelStatsIngressMcast':avWlanMobTunnelStatsIngressMcast,'avWlanMobTunnelStatsIngressBcast':avWlanMobTunnelStatsIngressBcast,'avWlanMobTunnelStatsIngressOctets':avWlanMobTunnelStatsIngressOctets,'avWlanMobTunnelStatsIngressError':avWlanMobTunnelStatsIngressError,'avWlanMobTunnelStatsIngressDropped':avWlanMobTunnelStatsIngressDropped,'avWlanMobTunnelStatsIngressPkts64':avWlanMobTunnelStatsIngressPkts64,'avWlanMobTunnelStatsIngressPkts65to127':avWlanMobTunnelStatsIngressPkts65to127,'avWlanMobTunnelStatsIngressPkts128to255':avWlanMobTunnelStatsIngressPkts128to255,'avWlanMobTunnelStatsIngressPkts256to511':avWlanMobTunnelStatsIngressPkts256to511,'avWlanMobTunnelStatsIngressPkts512to1023':avWlanMobTunnelStatsIngressPkts512to1023,'avWlanMobTunnelStatsIngressPkts1024to1518':avWlanMobTunnelStatsIngressPkts1024to1518,'avWlanMobTunnelStatsIngressPkts1522to9216':avWlanMobTunnelStatsIngressPkts1522to9216,'avWlanMobTunnelStatsIngressFragments':avWlanMobTunnelStatsIngressFragments,'avWlanMobTunnelStatsIngressFragmentsDrop':avWlanMobTunnelStatsIngressFragmentsDrop,'avWlanMobTunnelStatsIngressKeepAliveReq':avWlanMobTunnelStatsIngressKeepAliveReq,'avWlanMobTunnelStatsIngressKeepAliveRsp':avWlanMobTunnelStatsIngressKeepAliveRsp,'avWlanMobTunnelStatsIngressDataRate':avWlanMobTunnelStatsIngressDataRate,'avWlanMobTunnelStatsEgressPkts':avWlanMobTunnelStatsEgressPkts,'avWlanMobTunnelStatsEgressMcast':avWlanMobTunnelStatsEgressMcast,'avWlanMobTunnelStatsEgressBcast':avWlanMobTunnelStatsEgressBcast,'avWlanMobTunnelStatsEgressOctets':avWlanMobTunnelStatsEgressOctets,'avWlanMobTunnelStatsEgressError':avWlanMobTunnelStatsEgressError,'avWlanMobTunnelStatsEgressDropped':avWlanMobTunnelStatsEgressDropped,'avWlanMobTunnelStatsEgressPkts64':avWlanMobTunnelStatsEgressPkts64,'avWlanMobTunnelStatsEgressPkts65to127':avWlanMobTunnelStatsEgressPkts65to127,'avWlanMobTunnelStatsEgressPkts128to255':avWlanMobTunnelStatsEgressPkts128to255,'avWlanMobTunnelStatsEgressPkts256to511':avWlanMobTunnelStatsEgressPkts256to511,'avWlanMobTunnelStatsEgressPkts512to1023':avWlanMobTunnelStatsEgressPkts512to1023,'avWlanMobTunnelStatsEgressPkts1024to1518':avWlanMobTunnelStatsEgressPkts1024to1518,'avWlanMobTunnelStatsEgressPkts1522to9216':avWlanMobTunnelStatsEgressPkts1522to9216,'avWlanMobTunnelStatsEgressFragments':avWlanMobTunnelStatsEgressFragments,'avWlanMobTunnelStatsEgressKeepAliveReq':avWlanMobTunnelStatsEgressKeepAliveReq,'avWlanMobTunnelStatsEgressKeepAliveRsp':avWlanMobTunnelStatsEgressKeepAliveRsp,'avWlanMobTunnelStatsEgressDataRate':avWlanMobTunnelStatsEgressDataRate,'avWlanMobTunnelStatsReset':avWlanMobTunnelStatsReset,'avWlanMobSwTunnelStatisticsTable':avWlanMobSwTunnelStatisticsTable,'avWlanMobSwTunnelStatisticsEntry':avWlanMobSwTunnelStatisticsEntry,'avWlanMobSwTunnelIngressPkts':avWlanMobSwTunnelIngressPkts,'avWlanMobSwTunnelIngressMcast':avWlanMobSwTunnelIngressMcast,'avWlanMobSwTunnelIngressBcast':avWlanMobSwTunnelIngressBcast,'avWlanMobSwTunnelIngressOctets':avWlanMobSwTunnelIngressOctets,'avWlanMobSwTunnelIngressError':avWlanMobSwTunnelIngressError,'avWlanMobSwTunnelIngressDropped':avWlanMobSwTunnelIngressDropped,'avWlanMobSwTunnelIngressPkts64':avWlanMobSwTunnelIngressPkts64,'avWlanMobSwTunnelIngressPkts65to127':avWlanMobSwTunnelIngressPkts65to127,'avWlanMobSwTunnelIngressPkts128to255':avWlanMobSwTunnelIngressPkts128to255,'avWlanMobSwTunnelIngressPkts256to511':avWlanMobSwTunnelIngressPkts256to511,'avWlanMobSwTunnelIngressPkts512to1023':avWlanMobSwTunnelIngressPkts512to1023,'avWlanMobSwTunnelIngressPkts1024to1518':avWlanMobSwTunnelIngressPkts1024to1518,'avWlanMobSwTunnelIngressPkts1522to9216':avWlanMobSwTunnelIngressPkts1522to9216,'avWlanMobSwTunnelIngressFragments':avWlanMobSwTunnelIngressFragments,'avWlanMobSwTunnelIngressFragmentsDrop':avWlanMobSwTunnelIngressFragmentsDrop,'avWlanMobSwTunnelIngressKeepAliveReq':avWlanMobSwTunnelIngressKeepAliveReq,'avWlanMobSwTunnelIngressKeepAliveRsp':avWlanMobSwTunnelIngressKeepAliveRsp,'avWlanMobSwTunnelIngressDataRate':avWlanMobSwTunnelIngressDataRate,'avWlanMobSwTunnelEgressPkts':avWlanMobSwTunnelEgressPkts,'avWlanMobSwTunnelEgressMcast':avWlanMobSwTunnelEgressMcast,'avWlanMobSwTunnelEgressBcast':avWlanMobSwTunnelEgressBcast,'avWlanMobSwTunnelEgressOctets':avWlanMobSwTunnelEgressOctets,'avWlanMobSwTunnelEgressError':avWlanMobSwTunnelEgressError,'avWlanMobSwTunnelEgressDropped':avWlanMobSwTunnelEgressDropped,'avWlanMobSwTunnelEgressPkts64':avWlanMobSwTunnelEgressPkts64,'avWlanMobSwTunnelEgressPkts65to127':avWlanMobSwTunnelEgressPkts65to127,'avWlanMobSwTunnelEgressPkts128to255':avWlanMobSwTunnelEgressPkts128to255,'avWlanMobSwTunnelEgressPkts256to511':avWlanMobSwTunnelEgressPkts256to511,'avWlanMobSwTunnelEgressPkts512to1023':avWlanMobSwTunnelEgressPkts512to1023,'avWlanMobSwTunnelEgressPkts1024to1518':avWlanMobSwTunnelEgressPkts1024to1518,'avWlanMobSwTunnelEgressPkts1522to9216':avWlanMobSwTunnelEgressPkts1522to9216,'avWlanMobSwTunnelEgressFragments':avWlanMobSwTunnelEgressFragments,'avWlanMobSwTunnelEgressKeepAliveReq':avWlanMobSwTunnelEgressKeepAliveReq,'avWlanMobSwTunnelEgressKeepAliveRsp':avWlanMobSwTunnelEgressKeepAliveRsp,'avWlanMobSwTunnelEgressDataRate':avWlanMobSwTunnelEgressDataRate,'avWlanMobSwTunnelResetStats':avWlanMobSwTunnelResetStats,'avWlanMobSwTunnelIpAddressType':avWlanMobSwTunnelIpAddressType,'avWlanMobSwTunnelIpAddress':avWlanMobSwTunnelIpAddress,'avWlanMobSwTunnelInterfaceId':avWlanMobSwTunnelInterfaceId,'avWlanMobSwControllerTable':avWlanMobSwControllerTable,'avWlanMobSwControllerEntry':avWlanMobSwControllerEntry,_e:avWlanMobSwControllerId,'avWlanMobSwControllerAddrType':avWlanMobSwControllerAddrType,'avWlanMobSwControllerAddr':avWlanMobSwControllerAddr,'avWlanMobSwControllerRowStatus':avWlanMobSwControllerRowStatus,'avWlanMobSwFdbTable':avWlanMobSwFdbTable,'avWlanMobSwFdbEntry':avWlanMobSwFdbEntry,_f:avWlanMobSwFdbVlanId,_g:avWlanMobSwFdbMacAddress,'avWlanMobSwFdbType':avWlanMobSwFdbType,'avWlanMobSwFdbTunnelType':avWlanMobSwFdbTunnelType,'avWlanMobSwFdbRemoteEndpointId':avWlanMobSwFdbRemoteEndpointId,'avWlanMobSwFdbRemoteEndpointAddrType':avWlanMobSwFdbRemoteEndpointAddrType,'avWlanMobSwFdbRemoteEndpointAddr':avWlanMobSwFdbRemoteEndpointAddr,'avWlanMobSwFdbRemoteEndpointUdpPort':avWlanMobSwFdbRemoteEndpointUdpPort,'avWlanMobSwFdbLocalEndpointUdpPort':avWlanMobSwFdbLocalEndpointUdpPort,'avWlanMobSwFdbInterfaceId':avWlanMobSwFdbInterfaceId,'avWlanMobSwFdbFlushAction':avWlanMobSwFdbFlushAction})