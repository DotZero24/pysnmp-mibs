_An='nhdpStateGroup2'
_Am='nhdpStateGroup'
_Al='nhdpIfStateChange'
_Ak='nhdp2HopNbrStateChange'
_Aj='nhdpNbrStateChange'
_Ai='nhdpIib2HopSetN2Lost'
_Ah='nhdp2HopNbrStateChangeWindow'
_Ag='nhdp2HopNbrStateChangeThreshold'
_Af='nhdpNbrStateChangeWindow'
_Ae='nhdpNbrStateChangeThreshold'
_Ad='nhdpIib2HopSetPerfUpTime'
_Ac='nhdpIib2HopSetPerfChanges'
_Ab='nhdpDiscNeighborNibNeighborSetReachableLinkChanges'
_Aa='nhdpDiscNeighborNibNeighborSetUpTime'
_AZ='nhdpDiscNeighborNibNeighborSetChanges'
_AY='nhdpNibNeighborSetChanges'
_AX='nhdpDiscIfExpectedPackets'
_AW='nhdpDiscIfRecvdPackets'
_AV='nhdpIfPerfCounterDiscontinuityTime'
_AU='nhdpIfHelloMessageXmitAccumulatedLostNeighborCount'
_AT='nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount'
_AS='nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount'
_AR='nhdpIfHelloMessagePeriodicXmits'
_AQ='nhdpIfHelloMessageTriggeredXmits'
_AP='nhdpIfHelloMessageRecvdAccumulatedSize'
_AO='nhdpIfHelloMessageXmitAccumulatedSize'
_AN='nhdpIfHelloMessageRecvd'
_AM='nhdpIfHelloMessageXmits'
_AL='deprecated'
_AK='nhdpLibRemovedIfAddrSetIRTime'
_AJ='nhdpLibRemovedIfAddrSetIfIndex'
_AI='nhdpLibRemovedIfAddrSetIpAddrPrefixLen'
_AH='nhdpLibRemovedIfAddrSetIpAddr'
_AG='nhdpLibRemovedIfAddrSetIpAddrType'
_AF='nhdpLibLocalIfSetRowStatus'
_AE='nhdpLibLocalIfSetIpAddrPrefixLen'
_AD='nhdpLibLocalIfSetIpAddr'
_AC='nhdpLibLocalIfSetIpAddrType'
_AB='nhdpLibLocalIfSetIfIndex'
_AA='nhdpIfRowStatus'
_A9='nhdpIHoldTime'
_A8='nhdpNHoldTime'
_A7='nhdpHtMaxJitter'
_A6='nhdpHpMaxJitter'
_A5='nhdpInitialPending'
_A4='nhdpInitialQuality'
_A3='nhdpHystRejectQuality'
_A2='nhdpHystAcceptQuality'
_A1='nhdpHHoldTime'
_A0='nhdpLHoldTime'
_z='nhdpRefreshInterval'
_y='nhdpHelloMinInterval'
_x='nhdpHelloInterval'
_w='packets'
_v='octets'
_u='nhdpIib2HopSetIpAddress'
_t='nhdpIib2HopSetIpAddressType'
_s='nhdpDiscIfSetIndex'
_r='nhdpLibRemovedIfAddrSetIndex'
_q='nhdpLibLocalIfSetIndex'
_p='nhdpPerformanceGroup'
_o='nhdpNotificationGroup'
_n='nhdpNotificationObjectGroup'
_m='nhdp2HopNbrState'
_l='nhdpNbrState'
_k='nhdpNibLostNeighborSetNLTime'
_j='nhdpNibNeighborSetNSymmetric'
_i='nhdpIib2HopSetN2Time'
_h='nhdpIib2HopSet1HopIfIndex'
_g='nhdpIib2HopSetIpAddrPrefixLen'
_f='nhdpIibLinkSetLTime'
_e='nhdpIibLinkSetLLost'
_d='nhdpIibLinkSetLPending'
_c='nhdpIibLinkSetLSymTime'
_b='nhdpIibLinkSetLHeardTime'
_a='nhdpDiscIfSetIpAddrPrefixLen'
_Z='nhdpDiscIfSetIpAddr'
_Y='nhdpDiscIfSetIpAddrType'
_X='nhdpIfStateUpTime'
_W='nhdpUpTime'
_V='nhdpIfStatus'
_U='neighbors'
_T='TruthValue'
_S='RowStatus'
_R='TimeTicks'
_Q='nhdpConfigurationGroup'
_P='messages'
_O='nhdpIfName'
_N='InetAddress'
_M='nhdpDiscIfIndex'
_L='not-accessible'
_K='nhdpIfIndex'
_J='changes'
_I='read-write'
_H='nhdpDiscRouterIndex'
_G='Integer32'
_F='milliseconds'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='NHDP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB','Float32TC')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressPrefixLength','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_R,_E,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_S,'TextualConvention','TimeStamp',_T)
nhdpMIB=ModuleIdentity((1,3,6,1,2,1,213))
if mibBuilder.loadTexts:nhdpMIB.setRevisions(('2016-07-12 00:00','2012-10-22 10:00'))
class NeighborIfIndex(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NeighborRouterIndex(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NhdpNotifications_ObjectIdentity=ObjectIdentity
nhdpNotifications=_NhdpNotifications_ObjectIdentity((1,3,6,1,2,1,213,0))
_NhdpNotificationsObjects_ObjectIdentity=ObjectIdentity
nhdpNotificationsObjects=_NhdpNotificationsObjects_ObjectIdentity((1,3,6,1,2,1,213,0,0))
_NhdpNotificationsControl_ObjectIdentity=ObjectIdentity
nhdpNotificationsControl=_NhdpNotificationsControl_ObjectIdentity((1,3,6,1,2,1,213,0,1))
class _NhdpNbrStateChangeThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NhdpNbrStateChangeThreshold_Type.__name__=_G
_NhdpNbrStateChangeThreshold_Object=MibScalar
nhdpNbrStateChangeThreshold=_NhdpNbrStateChangeThreshold_Object((1,3,6,1,2,1,213,0,1,1),_NhdpNbrStateChangeThreshold_Type())
nhdpNbrStateChangeThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:nhdpNbrStateChangeThreshold.setStatus(_B)
if mibBuilder.loadTexts:nhdpNbrStateChangeThreshold.setUnits(_J)
class _NhdpNbrStateChangeWindow_Type(TimeTicks):defaultValue=1000
_NhdpNbrStateChangeWindow_Type.__name__=_R
_NhdpNbrStateChangeWindow_Object=MibScalar
nhdpNbrStateChangeWindow=_NhdpNbrStateChangeWindow_Object((1,3,6,1,2,1,213,0,1,2),_NhdpNbrStateChangeWindow_Type())
nhdpNbrStateChangeWindow.setMaxAccess(_I)
if mibBuilder.loadTexts:nhdpNbrStateChangeWindow.setStatus(_B)
class _Nhdp2HopNbrStateChangeThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Nhdp2HopNbrStateChangeThreshold_Type.__name__=_G
_Nhdp2HopNbrStateChangeThreshold_Object=MibScalar
nhdp2HopNbrStateChangeThreshold=_Nhdp2HopNbrStateChangeThreshold_Object((1,3,6,1,2,1,213,0,1,3),_Nhdp2HopNbrStateChangeThreshold_Type())
nhdp2HopNbrStateChangeThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:nhdp2HopNbrStateChangeThreshold.setStatus(_B)
if mibBuilder.loadTexts:nhdp2HopNbrStateChangeThreshold.setUnits(_J)
class _Nhdp2HopNbrStateChangeWindow_Type(TimeTicks):defaultValue=1000
_Nhdp2HopNbrStateChangeWindow_Type.__name__=_R
_Nhdp2HopNbrStateChangeWindow_Object=MibScalar
nhdp2HopNbrStateChangeWindow=_Nhdp2HopNbrStateChangeWindow_Object((1,3,6,1,2,1,213,0,1,4),_Nhdp2HopNbrStateChangeWindow_Type())
nhdp2HopNbrStateChangeWindow.setMaxAccess(_I)
if mibBuilder.loadTexts:nhdp2HopNbrStateChangeWindow.setStatus(_B)
_NhdpNotificationsStates_ObjectIdentity=ObjectIdentity
nhdpNotificationsStates=_NhdpNotificationsStates_ObjectIdentity((1,3,6,1,2,1,213,0,2))
class _NhdpNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('down',0),('asymmetric',1),('symmetric',2)))
_NhdpNbrState_Type.__name__=_G
_NhdpNbrState_Object=MibScalar
nhdpNbrState=_NhdpNbrState_Object((1,3,6,1,2,1,213,0,2,1),_NhdpNbrState_Type())
nhdpNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpNbrState.setStatus(_B)
class _Nhdp2HopNbrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('down',0),('up',1),('notconsidered',2)))
_Nhdp2HopNbrState_Type.__name__=_G
_Nhdp2HopNbrState_Object=MibScalar
nhdp2HopNbrState=_Nhdp2HopNbrState_Object((1,3,6,1,2,1,213,0,2,2),_Nhdp2HopNbrState_Type())
nhdp2HopNbrState.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdp2HopNbrState.setStatus(_B)
_NhdpObjects_ObjectIdentity=ObjectIdentity
nhdpObjects=_NhdpObjects_ObjectIdentity((1,3,6,1,2,1,213,1))
_NhdpConfigurationObjGrp_ObjectIdentity=ObjectIdentity
nhdpConfigurationObjGrp=_NhdpConfigurationObjGrp_ObjectIdentity((1,3,6,1,2,1,213,1,1))
_NhdpInterfaceTable_Object=MibTable
nhdpInterfaceTable=_NhdpInterfaceTable_Object((1,3,6,1,2,1,213,1,1,1))
if mibBuilder.loadTexts:nhdpInterfaceTable.setStatus(_B)
_NhdpInterfaceEntry_Object=MibTableRow
nhdpInterfaceEntry=_NhdpInterfaceEntry_Object((1,3,6,1,2,1,213,1,1,1,1))
nhdpInterfaceEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:nhdpInterfaceEntry.setStatus(_B)
_NhdpIfIndex_Type=InterfaceIndex
_NhdpIfIndex_Object=MibTableColumn
nhdpIfIndex=_NhdpIfIndex_Object((1,3,6,1,2,1,213,1,1,1,1,1),_NhdpIfIndex_Type())
nhdpIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:nhdpIfIndex.setStatus(_B)
_NhdpIfName_Type=SnmpAdminString
_NhdpIfName_Object=MibTableColumn
nhdpIfName=_NhdpIfName_Object((1,3,6,1,2,1,213,1,1,1,1,2),_NhdpIfName_Type())
nhdpIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfName.setStatus(_B)
class _NhdpIfStatus_Type(TruthValue):defaultValue=2
_NhdpIfStatus_Type.__name__=_T
_NhdpIfStatus_Object=MibTableColumn
nhdpIfStatus=_NhdpIfStatus_Object((1,3,6,1,2,1,213,1,1,1,1,3),_NhdpIfStatus_Type())
nhdpIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpIfStatus.setStatus(_B)
class _NhdpHelloInterval_Type(Unsigned32):defaultValue=2000
_NhdpHelloInterval_Type.__name__=_E
_NhdpHelloInterval_Object=MibTableColumn
nhdpHelloInterval=_NhdpHelloInterval_Object((1,3,6,1,2,1,213,1,1,1,1,4),_NhdpHelloInterval_Type())
nhdpHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:nhdpHelloInterval.setUnits(_F)
class _NhdpHelloMinInterval_Type(Unsigned32):defaultValue=500
_NhdpHelloMinInterval_Type.__name__=_E
_NhdpHelloMinInterval_Object=MibTableColumn
nhdpHelloMinInterval=_NhdpHelloMinInterval_Object((1,3,6,1,2,1,213,1,1,1,1,5),_NhdpHelloMinInterval_Type())
nhdpHelloMinInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHelloMinInterval.setStatus(_B)
if mibBuilder.loadTexts:nhdpHelloMinInterval.setUnits(_F)
class _NhdpRefreshInterval_Type(Unsigned32):defaultValue=2000
_NhdpRefreshInterval_Type.__name__=_E
_NhdpRefreshInterval_Object=MibTableColumn
nhdpRefreshInterval=_NhdpRefreshInterval_Object((1,3,6,1,2,1,213,1,1,1,1,6),_NhdpRefreshInterval_Type())
nhdpRefreshInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpRefreshInterval.setStatus(_B)
if mibBuilder.loadTexts:nhdpRefreshInterval.setUnits(_F)
class _NhdpLHoldTime_Type(Unsigned32):defaultValue=6000
_NhdpLHoldTime_Type.__name__=_E
_NhdpLHoldTime_Object=MibTableColumn
nhdpLHoldTime=_NhdpLHoldTime_Object((1,3,6,1,2,1,213,1,1,1,1,7),_NhdpLHoldTime_Type())
nhdpLHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpLHoldTime.setStatus(_B)
if mibBuilder.loadTexts:nhdpLHoldTime.setUnits(_F)
class _NhdpHHoldTime_Type(Unsigned32):defaultValue=6000
_NhdpHHoldTime_Type.__name__=_E
_NhdpHHoldTime_Object=MibTableColumn
nhdpHHoldTime=_NhdpHHoldTime_Object((1,3,6,1,2,1,213,1,1,1,1,8),_NhdpHHoldTime_Type())
nhdpHHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHHoldTime.setStatus(_B)
if mibBuilder.loadTexts:nhdpHHoldTime.setUnits(_F)
_NhdpHystAcceptQuality_Type=Float32TC
_NhdpHystAcceptQuality_Object=MibTableColumn
nhdpHystAcceptQuality=_NhdpHystAcceptQuality_Object((1,3,6,1,2,1,213,1,1,1,1,9),_NhdpHystAcceptQuality_Type())
nhdpHystAcceptQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHystAcceptQuality.setStatus(_B)
_NhdpHystRejectQuality_Type=Float32TC
_NhdpHystRejectQuality_Object=MibTableColumn
nhdpHystRejectQuality=_NhdpHystRejectQuality_Object((1,3,6,1,2,1,213,1,1,1,1,10),_NhdpHystRejectQuality_Type())
nhdpHystRejectQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHystRejectQuality.setStatus(_B)
_NhdpInitialQuality_Type=Float32TC
_NhdpInitialQuality_Object=MibTableColumn
nhdpInitialQuality=_NhdpInitialQuality_Object((1,3,6,1,2,1,213,1,1,1,1,11),_NhdpInitialQuality_Type())
nhdpInitialQuality.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpInitialQuality.setStatus(_B)
class _NhdpInitialPending_Type(TruthValue):defaultValue=2
_NhdpInitialPending_Type.__name__=_T
_NhdpInitialPending_Object=MibTableColumn
nhdpInitialPending=_NhdpInitialPending_Object((1,3,6,1,2,1,213,1,1,1,1,12),_NhdpInitialPending_Type())
nhdpInitialPending.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpInitialPending.setStatus(_B)
class _NhdpHpMaxJitter_Type(Unsigned32):defaultValue=500
_NhdpHpMaxJitter_Type.__name__=_E
_NhdpHpMaxJitter_Object=MibTableColumn
nhdpHpMaxJitter=_NhdpHpMaxJitter_Object((1,3,6,1,2,1,213,1,1,1,1,13),_NhdpHpMaxJitter_Type())
nhdpHpMaxJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHpMaxJitter.setStatus(_B)
if mibBuilder.loadTexts:nhdpHpMaxJitter.setUnits(_F)
class _NhdpHtMaxJitter_Type(Unsigned32):defaultValue=500
_NhdpHtMaxJitter_Type.__name__=_E
_NhdpHtMaxJitter_Object=MibTableColumn
nhdpHtMaxJitter=_NhdpHtMaxJitter_Object((1,3,6,1,2,1,213,1,1,1,1,14),_NhdpHtMaxJitter_Type())
nhdpHtMaxJitter.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpHtMaxJitter.setStatus(_B)
if mibBuilder.loadTexts:nhdpHtMaxJitter.setUnits(_F)
class _NhdpIfRowStatus_Type(RowStatus):defaultValue=1
_NhdpIfRowStatus_Type.__name__=_S
_NhdpIfRowStatus_Object=MibTableColumn
nhdpIfRowStatus=_NhdpIfRowStatus_Object((1,3,6,1,2,1,213,1,1,1,1,15),_NhdpIfRowStatus_Type())
nhdpIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpIfRowStatus.setStatus(_B)
class _NhdpNHoldTime_Type(Unsigned32):defaultValue=6000
_NhdpNHoldTime_Type.__name__=_E
_NhdpNHoldTime_Object=MibScalar
nhdpNHoldTime=_NhdpNHoldTime_Object((1,3,6,1,2,1,213,1,1,2),_NhdpNHoldTime_Type())
nhdpNHoldTime.setMaxAccess(_I)
if mibBuilder.loadTexts:nhdpNHoldTime.setStatus(_B)
if mibBuilder.loadTexts:nhdpNHoldTime.setUnits(_F)
class _NhdpIHoldTime_Type(Unsigned32):defaultValue=6000
_NhdpIHoldTime_Type.__name__=_E
_NhdpIHoldTime_Object=MibScalar
nhdpIHoldTime=_NhdpIHoldTime_Object((1,3,6,1,2,1,213,1,1,3),_NhdpIHoldTime_Type())
nhdpIHoldTime.setMaxAccess(_I)
if mibBuilder.loadTexts:nhdpIHoldTime.setStatus(_B)
if mibBuilder.loadTexts:nhdpIHoldTime.setUnits(_F)
_NhdpLibLocalIfSetTable_Object=MibTable
nhdpLibLocalIfSetTable=_NhdpLibLocalIfSetTable_Object((1,3,6,1,2,1,213,1,1,4))
if mibBuilder.loadTexts:nhdpLibLocalIfSetTable.setStatus(_B)
_NhdpLibLocalIfSetEntry_Object=MibTableRow
nhdpLibLocalIfSetEntry=_NhdpLibLocalIfSetEntry_Object((1,3,6,1,2,1,213,1,1,4,1))
nhdpLibLocalIfSetEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:nhdpLibLocalIfSetEntry.setStatus(_B)
class _NhdpLibLocalIfSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NhdpLibLocalIfSetIndex_Type.__name__=_G
_NhdpLibLocalIfSetIndex_Object=MibTableColumn
nhdpLibLocalIfSetIndex=_NhdpLibLocalIfSetIndex_Object((1,3,6,1,2,1,213,1,1,4,1,1),_NhdpLibLocalIfSetIndex_Type())
nhdpLibLocalIfSetIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:nhdpLibLocalIfSetIndex.setStatus(_B)
_NhdpLibLocalIfSetIfIndex_Type=InterfaceIndex
_NhdpLibLocalIfSetIfIndex_Object=MibTableColumn
nhdpLibLocalIfSetIfIndex=_NhdpLibLocalIfSetIfIndex_Object((1,3,6,1,2,1,213,1,1,4,1,2),_NhdpLibLocalIfSetIfIndex_Type())
nhdpLibLocalIfSetIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpLibLocalIfSetIfIndex.setStatus(_B)
_NhdpLibLocalIfSetIpAddrType_Type=InetAddressType
_NhdpLibLocalIfSetIpAddrType_Object=MibTableColumn
nhdpLibLocalIfSetIpAddrType=_NhdpLibLocalIfSetIpAddrType_Object((1,3,6,1,2,1,213,1,1,4,1,3),_NhdpLibLocalIfSetIpAddrType_Type())
nhdpLibLocalIfSetIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpLibLocalIfSetIpAddrType.setStatus(_B)
class _NhdpLibLocalIfSetIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_NhdpLibLocalIfSetIpAddr_Type.__name__=_N
_NhdpLibLocalIfSetIpAddr_Object=MibTableColumn
nhdpLibLocalIfSetIpAddr=_NhdpLibLocalIfSetIpAddr_Object((1,3,6,1,2,1,213,1,1,4,1,4),_NhdpLibLocalIfSetIpAddr_Type())
nhdpLibLocalIfSetIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpLibLocalIfSetIpAddr.setStatus(_B)
_NhdpLibLocalIfSetIpAddrPrefixLen_Type=InetAddressPrefixLength
_NhdpLibLocalIfSetIpAddrPrefixLen_Object=MibTableColumn
nhdpLibLocalIfSetIpAddrPrefixLen=_NhdpLibLocalIfSetIpAddrPrefixLen_Object((1,3,6,1,2,1,213,1,1,4,1,5),_NhdpLibLocalIfSetIpAddrPrefixLen_Type())
nhdpLibLocalIfSetIpAddrPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpLibLocalIfSetIpAddrPrefixLen.setStatus(_B)
class _NhdpLibLocalIfSetRowStatus_Type(RowStatus):defaultValue=3
_NhdpLibLocalIfSetRowStatus_Type.__name__=_S
_NhdpLibLocalIfSetRowStatus_Object=MibTableColumn
nhdpLibLocalIfSetRowStatus=_NhdpLibLocalIfSetRowStatus_Object((1,3,6,1,2,1,213,1,1,4,1,6),_NhdpLibLocalIfSetRowStatus_Type())
nhdpLibLocalIfSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nhdpLibLocalIfSetRowStatus.setStatus(_B)
_NhdpLibRemovedIfAddrSetTable_Object=MibTable
nhdpLibRemovedIfAddrSetTable=_NhdpLibRemovedIfAddrSetTable_Object((1,3,6,1,2,1,213,1,1,5))
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetTable.setStatus(_B)
_NhdpLibRemovedIfAddrSetEntry_Object=MibTableRow
nhdpLibRemovedIfAddrSetEntry=_NhdpLibRemovedIfAddrSetEntry_Object((1,3,6,1,2,1,213,1,1,5,1))
nhdpLibRemovedIfAddrSetEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetEntry.setStatus(_B)
class _NhdpLibRemovedIfAddrSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NhdpLibRemovedIfAddrSetIndex_Type.__name__=_G
_NhdpLibRemovedIfAddrSetIndex_Object=MibTableColumn
nhdpLibRemovedIfAddrSetIndex=_NhdpLibRemovedIfAddrSetIndex_Object((1,3,6,1,2,1,213,1,1,5,1,1),_NhdpLibRemovedIfAddrSetIndex_Type())
nhdpLibRemovedIfAddrSetIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetIndex.setStatus(_B)
_NhdpLibRemovedIfAddrSetIpAddrType_Type=InetAddressType
_NhdpLibRemovedIfAddrSetIpAddrType_Object=MibTableColumn
nhdpLibRemovedIfAddrSetIpAddrType=_NhdpLibRemovedIfAddrSetIpAddrType_Object((1,3,6,1,2,1,213,1,1,5,1,2),_NhdpLibRemovedIfAddrSetIpAddrType_Type())
nhdpLibRemovedIfAddrSetIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetIpAddrType.setStatus(_B)
class _NhdpLibRemovedIfAddrSetIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_NhdpLibRemovedIfAddrSetIpAddr_Type.__name__=_N
_NhdpLibRemovedIfAddrSetIpAddr_Object=MibTableColumn
nhdpLibRemovedIfAddrSetIpAddr=_NhdpLibRemovedIfAddrSetIpAddr_Object((1,3,6,1,2,1,213,1,1,5,1,3),_NhdpLibRemovedIfAddrSetIpAddr_Type())
nhdpLibRemovedIfAddrSetIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetIpAddr.setStatus(_B)
_NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Type=InetAddressPrefixLength
_NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Object=MibTableColumn
nhdpLibRemovedIfAddrSetIpAddrPrefixLen=_NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Object((1,3,6,1,2,1,213,1,1,5,1,4),_NhdpLibRemovedIfAddrSetIpAddrPrefixLen_Type())
nhdpLibRemovedIfAddrSetIpAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetIpAddrPrefixLen.setStatus(_B)
_NhdpLibRemovedIfAddrSetIfIndex_Type=InterfaceIndex
_NhdpLibRemovedIfAddrSetIfIndex_Object=MibTableColumn
nhdpLibRemovedIfAddrSetIfIndex=_NhdpLibRemovedIfAddrSetIfIndex_Object((1,3,6,1,2,1,213,1,1,5,1,5),_NhdpLibRemovedIfAddrSetIfIndex_Type())
nhdpLibRemovedIfAddrSetIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetIfIndex.setStatus(_B)
_NhdpLibRemovedIfAddrSetIRTime_Type=TimeStamp
_NhdpLibRemovedIfAddrSetIRTime_Object=MibTableColumn
nhdpLibRemovedIfAddrSetIRTime=_NhdpLibRemovedIfAddrSetIRTime_Object((1,3,6,1,2,1,213,1,1,5,1,6),_NhdpLibRemovedIfAddrSetIRTime_Type())
nhdpLibRemovedIfAddrSetIRTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpLibRemovedIfAddrSetIRTime.setStatus(_B)
_NhdpStateObjGrp_ObjectIdentity=ObjectIdentity
nhdpStateObjGrp=_NhdpStateObjGrp_ObjectIdentity((1,3,6,1,2,1,213,1,2))
_NhdpUpTime_Type=TimeStamp
_NhdpUpTime_Object=MibScalar
nhdpUpTime=_NhdpUpTime_Object((1,3,6,1,2,1,213,1,2,1),_NhdpUpTime_Type())
nhdpUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpUpTime.setStatus(_B)
_NhdpInterfaceStateTable_Object=MibTable
nhdpInterfaceStateTable=_NhdpInterfaceStateTable_Object((1,3,6,1,2,1,213,1,2,2))
if mibBuilder.loadTexts:nhdpInterfaceStateTable.setStatus(_B)
_NhdpInterfaceStateEntry_Object=MibTableRow
nhdpInterfaceStateEntry=_NhdpInterfaceStateEntry_Object((1,3,6,1,2,1,213,1,2,2,1))
nhdpInterfaceStateEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:nhdpInterfaceStateEntry.setStatus(_B)
_NhdpIfStateUpTime_Type=TimeStamp
_NhdpIfStateUpTime_Object=MibTableColumn
nhdpIfStateUpTime=_NhdpIfStateUpTime_Object((1,3,6,1,2,1,213,1,2,2,1,1),_NhdpIfStateUpTime_Type())
nhdpIfStateUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfStateUpTime.setStatus(_B)
_NhdpDiscIfSetTable_Object=MibTable
nhdpDiscIfSetTable=_NhdpDiscIfSetTable_Object((1,3,6,1,2,1,213,1,2,3))
if mibBuilder.loadTexts:nhdpDiscIfSetTable.setStatus(_B)
_NhdpDiscIfSetEntry_Object=MibTableRow
nhdpDiscIfSetEntry=_NhdpDiscIfSetEntry_Object((1,3,6,1,2,1,213,1,2,3,1))
nhdpDiscIfSetEntry.setIndexNames((0,_A,_s))
if mibBuilder.loadTexts:nhdpDiscIfSetEntry.setStatus(_B)
class _NhdpDiscIfSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NhdpDiscIfSetIndex_Type.__name__=_G
_NhdpDiscIfSetIndex_Object=MibTableColumn
nhdpDiscIfSetIndex=_NhdpDiscIfSetIndex_Object((1,3,6,1,2,1,213,1,2,3,1,1),_NhdpDiscIfSetIndex_Type())
nhdpDiscIfSetIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:nhdpDiscIfSetIndex.setStatus(_B)
_NhdpDiscIfIndex_Type=NeighborIfIndex
_NhdpDiscIfIndex_Object=MibTableColumn
nhdpDiscIfIndex=_NhdpDiscIfIndex_Object((1,3,6,1,2,1,213,1,2,3,1,2),_NhdpDiscIfIndex_Type())
nhdpDiscIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscIfIndex.setStatus(_B)
_NhdpDiscRouterIndex_Type=NeighborRouterIndex
_NhdpDiscRouterIndex_Object=MibTableColumn
nhdpDiscRouterIndex=_NhdpDiscRouterIndex_Object((1,3,6,1,2,1,213,1,2,3,1,3),_NhdpDiscRouterIndex_Type())
nhdpDiscRouterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscRouterIndex.setStatus(_B)
_NhdpDiscIfSetIpAddrType_Type=InetAddressType
_NhdpDiscIfSetIpAddrType_Object=MibTableColumn
nhdpDiscIfSetIpAddrType=_NhdpDiscIfSetIpAddrType_Object((1,3,6,1,2,1,213,1,2,3,1,4),_NhdpDiscIfSetIpAddrType_Type())
nhdpDiscIfSetIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscIfSetIpAddrType.setStatus(_B)
class _NhdpDiscIfSetIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_NhdpDiscIfSetIpAddr_Type.__name__=_N
_NhdpDiscIfSetIpAddr_Object=MibTableColumn
nhdpDiscIfSetIpAddr=_NhdpDiscIfSetIpAddr_Object((1,3,6,1,2,1,213,1,2,3,1,5),_NhdpDiscIfSetIpAddr_Type())
nhdpDiscIfSetIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscIfSetIpAddr.setStatus(_B)
_NhdpDiscIfSetIpAddrPrefixLen_Type=InetAddressPrefixLength
_NhdpDiscIfSetIpAddrPrefixLen_Object=MibTableColumn
nhdpDiscIfSetIpAddrPrefixLen=_NhdpDiscIfSetIpAddrPrefixLen_Object((1,3,6,1,2,1,213,1,2,3,1,6),_NhdpDiscIfSetIpAddrPrefixLen_Type())
nhdpDiscIfSetIpAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscIfSetIpAddrPrefixLen.setStatus(_B)
_NhdpIibLinkSetTable_Object=MibTable
nhdpIibLinkSetTable=_NhdpIibLinkSetTable_Object((1,3,6,1,2,1,213,1,2,4))
if mibBuilder.loadTexts:nhdpIibLinkSetTable.setStatus(_B)
_NhdpIibLinkSetEntry_Object=MibTableRow
nhdpIibLinkSetEntry=_NhdpIibLinkSetEntry_Object((1,3,6,1,2,1,213,1,2,4,1))
nhdpIibLinkSetEntry.setIndexNames((0,_A,_K),(0,_A,_M))
if mibBuilder.loadTexts:nhdpIibLinkSetEntry.setStatus(_B)
_NhdpIibLinkSetLHeardTime_Type=TimeStamp
_NhdpIibLinkSetLHeardTime_Object=MibTableColumn
nhdpIibLinkSetLHeardTime=_NhdpIibLinkSetLHeardTime_Object((1,3,6,1,2,1,213,1,2,4,1,1),_NhdpIibLinkSetLHeardTime_Type())
nhdpIibLinkSetLHeardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIibLinkSetLHeardTime.setStatus(_B)
_NhdpIibLinkSetLSymTime_Type=TimeStamp
_NhdpIibLinkSetLSymTime_Object=MibTableColumn
nhdpIibLinkSetLSymTime=_NhdpIibLinkSetLSymTime_Object((1,3,6,1,2,1,213,1,2,4,1,2),_NhdpIibLinkSetLSymTime_Type())
nhdpIibLinkSetLSymTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIibLinkSetLSymTime.setStatus(_B)
_NhdpIibLinkSetLPending_Type=TruthValue
_NhdpIibLinkSetLPending_Object=MibTableColumn
nhdpIibLinkSetLPending=_NhdpIibLinkSetLPending_Object((1,3,6,1,2,1,213,1,2,4,1,3),_NhdpIibLinkSetLPending_Type())
nhdpIibLinkSetLPending.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIibLinkSetLPending.setStatus(_B)
_NhdpIibLinkSetLLost_Type=TruthValue
_NhdpIibLinkSetLLost_Object=MibTableColumn
nhdpIibLinkSetLLost=_NhdpIibLinkSetLLost_Object((1,3,6,1,2,1,213,1,2,4,1,4),_NhdpIibLinkSetLLost_Type())
nhdpIibLinkSetLLost.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIibLinkSetLLost.setStatus(_B)
_NhdpIibLinkSetLTime_Type=TimeStamp
_NhdpIibLinkSetLTime_Object=MibTableColumn
nhdpIibLinkSetLTime=_NhdpIibLinkSetLTime_Object((1,3,6,1,2,1,213,1,2,4,1,5),_NhdpIibLinkSetLTime_Type())
nhdpIibLinkSetLTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIibLinkSetLTime.setStatus(_B)
_NhdpIib2HopSetTable_Object=MibTable
nhdpIib2HopSetTable=_NhdpIib2HopSetTable_Object((1,3,6,1,2,1,213,1,2,5))
if mibBuilder.loadTexts:nhdpIib2HopSetTable.setStatus(_B)
_NhdpIib2HopSetEntry_Object=MibTableRow
nhdpIib2HopSetEntry=_NhdpIib2HopSetEntry_Object((1,3,6,1,2,1,213,1,2,5,1))
nhdpIib2HopSetEntry.setIndexNames((0,_A,_K),(0,_A,_M),(0,_A,_t),(0,_A,_u))
if mibBuilder.loadTexts:nhdpIib2HopSetEntry.setStatus(_B)
_NhdpIib2HopSetIpAddressType_Type=InetAddressType
_NhdpIib2HopSetIpAddressType_Object=MibTableColumn
nhdpIib2HopSetIpAddressType=_NhdpIib2HopSetIpAddressType_Object((1,3,6,1,2,1,213,1,2,5,1,1),_NhdpIib2HopSetIpAddressType_Type())
nhdpIib2HopSetIpAddressType.setMaxAccess(_L)
if mibBuilder.loadTexts:nhdpIib2HopSetIpAddressType.setStatus(_B)
class _NhdpIib2HopSetIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_NhdpIib2HopSetIpAddress_Type.__name__=_N
_NhdpIib2HopSetIpAddress_Object=MibTableColumn
nhdpIib2HopSetIpAddress=_NhdpIib2HopSetIpAddress_Object((1,3,6,1,2,1,213,1,2,5,1,2),_NhdpIib2HopSetIpAddress_Type())
nhdpIib2HopSetIpAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:nhdpIib2HopSetIpAddress.setStatus(_B)
_NhdpIib2HopSetIpAddrPrefixLen_Type=InetAddressPrefixLength
_NhdpIib2HopSetIpAddrPrefixLen_Object=MibTableColumn
nhdpIib2HopSetIpAddrPrefixLen=_NhdpIib2HopSetIpAddrPrefixLen_Object((1,3,6,1,2,1,213,1,2,5,1,3),_NhdpIib2HopSetIpAddrPrefixLen_Type())
nhdpIib2HopSetIpAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIib2HopSetIpAddrPrefixLen.setStatus(_B)
_NhdpIib2HopSet1HopIfIndex_Type=NeighborIfIndex
_NhdpIib2HopSet1HopIfIndex_Object=MibTableColumn
nhdpIib2HopSet1HopIfIndex=_NhdpIib2HopSet1HopIfIndex_Object((1,3,6,1,2,1,213,1,2,5,1,4),_NhdpIib2HopSet1HopIfIndex_Type())
nhdpIib2HopSet1HopIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIib2HopSet1HopIfIndex.setStatus(_B)
_NhdpIib2HopSetN2Time_Type=TimeStamp
_NhdpIib2HopSetN2Time_Object=MibTableColumn
nhdpIib2HopSetN2Time=_NhdpIib2HopSetN2Time_Object((1,3,6,1,2,1,213,1,2,5,1,5),_NhdpIib2HopSetN2Time_Type())
nhdpIib2HopSetN2Time.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIib2HopSetN2Time.setStatus(_B)
_NhdpIib2HopSetN2Lost_Type=TruthValue
_NhdpIib2HopSetN2Lost_Object=MibTableColumn
nhdpIib2HopSetN2Lost=_NhdpIib2HopSetN2Lost_Object((1,3,6,1,2,1,213,1,2,5,1,6),_NhdpIib2HopSetN2Lost_Type())
nhdpIib2HopSetN2Lost.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIib2HopSetN2Lost.setStatus(_B)
_NhdpNibNeighborSetTable_Object=MibTable
nhdpNibNeighborSetTable=_NhdpNibNeighborSetTable_Object((1,3,6,1,2,1,213,1,2,6))
if mibBuilder.loadTexts:nhdpNibNeighborSetTable.setStatus(_B)
_NhdpNibNeighborSetEntry_Object=MibTableRow
nhdpNibNeighborSetEntry=_NhdpNibNeighborSetEntry_Object((1,3,6,1,2,1,213,1,2,6,1))
nhdpNibNeighborSetEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:nhdpNibNeighborSetEntry.setStatus(_B)
_NhdpNibNeighborSetNSymmetric_Type=TruthValue
_NhdpNibNeighborSetNSymmetric_Object=MibTableColumn
nhdpNibNeighborSetNSymmetric=_NhdpNibNeighborSetNSymmetric_Object((1,3,6,1,2,1,213,1,2,6,1,1),_NhdpNibNeighborSetNSymmetric_Type())
nhdpNibNeighborSetNSymmetric.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpNibNeighborSetNSymmetric.setStatus(_B)
_NhdpNibLostNeighborSetTable_Object=MibTable
nhdpNibLostNeighborSetTable=_NhdpNibLostNeighborSetTable_Object((1,3,6,1,2,1,213,1,2,7))
if mibBuilder.loadTexts:nhdpNibLostNeighborSetTable.setStatus(_B)
_NhdpNibLostNeighborSetEntry_Object=MibTableRow
nhdpNibLostNeighborSetEntry=_NhdpNibLostNeighborSetEntry_Object((1,3,6,1,2,1,213,1,2,7,1))
nhdpNibLostNeighborSetEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:nhdpNibLostNeighborSetEntry.setStatus(_B)
_NhdpNibLostNeighborSetNLTime_Type=TimeStamp
_NhdpNibLostNeighborSetNLTime_Object=MibTableColumn
nhdpNibLostNeighborSetNLTime=_NhdpNibLostNeighborSetNLTime_Object((1,3,6,1,2,1,213,1,2,7,1,1),_NhdpNibLostNeighborSetNLTime_Type())
nhdpNibLostNeighborSetNLTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpNibLostNeighborSetNLTime.setStatus(_B)
_NhdpPerformanceObjGrp_ObjectIdentity=ObjectIdentity
nhdpPerformanceObjGrp=_NhdpPerformanceObjGrp_ObjectIdentity((1,3,6,1,2,1,213,1,3))
_NhdpInterfacePerfTable_Object=MibTable
nhdpInterfacePerfTable=_NhdpInterfacePerfTable_Object((1,3,6,1,2,1,213,1,3,1))
if mibBuilder.loadTexts:nhdpInterfacePerfTable.setStatus(_B)
_NhdpInterfacePerfEntry_Object=MibTableRow
nhdpInterfacePerfEntry=_NhdpInterfacePerfEntry_Object((1,3,6,1,2,1,213,1,3,1,1))
nhdpInterfacePerfEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:nhdpInterfacePerfEntry.setStatus(_B)
_NhdpIfHelloMessageXmits_Type=Counter32
_NhdpIfHelloMessageXmits_Object=MibTableColumn
nhdpIfHelloMessageXmits=_NhdpIfHelloMessageXmits_Object((1,3,6,1,2,1,213,1,3,1,1,1),_NhdpIfHelloMessageXmits_Type())
nhdpIfHelloMessageXmits.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmits.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmits.setUnits(_P)
_NhdpIfHelloMessageRecvd_Type=Counter32
_NhdpIfHelloMessageRecvd_Object=MibTableColumn
nhdpIfHelloMessageRecvd=_NhdpIfHelloMessageRecvd_Object((1,3,6,1,2,1,213,1,3,1,1,2),_NhdpIfHelloMessageRecvd_Type())
nhdpIfHelloMessageRecvd.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageRecvd.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageRecvd.setUnits(_P)
_NhdpIfHelloMessageXmitAccumulatedSize_Type=Counter64
_NhdpIfHelloMessageXmitAccumulatedSize_Object=MibTableColumn
nhdpIfHelloMessageXmitAccumulatedSize=_NhdpIfHelloMessageXmitAccumulatedSize_Object((1,3,6,1,2,1,213,1,3,1,1,3),_NhdpIfHelloMessageXmitAccumulatedSize_Type())
nhdpIfHelloMessageXmitAccumulatedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedSize.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedSize.setUnits(_v)
_NhdpIfHelloMessageRecvdAccumulatedSize_Type=Counter64
_NhdpIfHelloMessageRecvdAccumulatedSize_Object=MibTableColumn
nhdpIfHelloMessageRecvdAccumulatedSize=_NhdpIfHelloMessageRecvdAccumulatedSize_Object((1,3,6,1,2,1,213,1,3,1,1,4),_NhdpIfHelloMessageRecvdAccumulatedSize_Type())
nhdpIfHelloMessageRecvdAccumulatedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageRecvdAccumulatedSize.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageRecvdAccumulatedSize.setUnits(_v)
_NhdpIfHelloMessageTriggeredXmits_Type=Counter32
_NhdpIfHelloMessageTriggeredXmits_Object=MibTableColumn
nhdpIfHelloMessageTriggeredXmits=_NhdpIfHelloMessageTriggeredXmits_Object((1,3,6,1,2,1,213,1,3,1,1,5),_NhdpIfHelloMessageTriggeredXmits_Type())
nhdpIfHelloMessageTriggeredXmits.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageTriggeredXmits.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageTriggeredXmits.setUnits(_P)
_NhdpIfHelloMessagePeriodicXmits_Type=Counter32
_NhdpIfHelloMessagePeriodicXmits_Object=MibTableColumn
nhdpIfHelloMessagePeriodicXmits=_NhdpIfHelloMessagePeriodicXmits_Object((1,3,6,1,2,1,213,1,3,1,1,6),_NhdpIfHelloMessagePeriodicXmits_Type())
nhdpIfHelloMessagePeriodicXmits.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessagePeriodicXmits.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessagePeriodicXmits.setUnits(_P)
_NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Type=Counter32
_NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Object=MibTableColumn
nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount=_NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Object((1,3,6,1,2,1,213,1,3,1,1,7),_NhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount_Type())
nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount.setUnits(_U)
_NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Type=Counter32
_NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Object=MibTableColumn
nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount=_NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Object((1,3,6,1,2,1,213,1,3,1,1,8),_NhdpIfHelloMessageXmitAccumulatedHeardNeighborCount_Type())
nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount.setUnits(_U)
_NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Type=Counter32
_NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Object=MibTableColumn
nhdpIfHelloMessageXmitAccumulatedLostNeighborCount=_NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Object((1,3,6,1,2,1,213,1,3,1,1,9),_NhdpIfHelloMessageXmitAccumulatedLostNeighborCount_Type())
nhdpIfHelloMessageXmitAccumulatedLostNeighborCount.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedLostNeighborCount.setStatus(_B)
if mibBuilder.loadTexts:nhdpIfHelloMessageXmitAccumulatedLostNeighborCount.setUnits(_U)
_NhdpIfPerfCounterDiscontinuityTime_Type=TimeStamp
_NhdpIfPerfCounterDiscontinuityTime_Object=MibTableColumn
nhdpIfPerfCounterDiscontinuityTime=_NhdpIfPerfCounterDiscontinuityTime_Object((1,3,6,1,2,1,213,1,3,1,1,10),_NhdpIfPerfCounterDiscontinuityTime_Type())
nhdpIfPerfCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIfPerfCounterDiscontinuityTime.setStatus(_B)
_NhdpDiscIfSetPerfTable_Object=MibTable
nhdpDiscIfSetPerfTable=_NhdpDiscIfSetPerfTable_Object((1,3,6,1,2,1,213,1,3,2))
if mibBuilder.loadTexts:nhdpDiscIfSetPerfTable.setStatus(_B)
_NhdpDiscIfSetPerfEntry_Object=MibTableRow
nhdpDiscIfSetPerfEntry=_NhdpDiscIfSetPerfEntry_Object((1,3,6,1,2,1,213,1,3,2,1))
nhdpDiscIfSetPerfEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:nhdpDiscIfSetPerfEntry.setStatus(_B)
_NhdpDiscIfRecvdPackets_Type=Counter32
_NhdpDiscIfRecvdPackets_Object=MibTableColumn
nhdpDiscIfRecvdPackets=_NhdpDiscIfRecvdPackets_Object((1,3,6,1,2,1,213,1,3,2,1,1),_NhdpDiscIfRecvdPackets_Type())
nhdpDiscIfRecvdPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscIfRecvdPackets.setStatus(_B)
if mibBuilder.loadTexts:nhdpDiscIfRecvdPackets.setUnits(_w)
_NhdpDiscIfExpectedPackets_Type=Counter32
_NhdpDiscIfExpectedPackets_Object=MibTableColumn
nhdpDiscIfExpectedPackets=_NhdpDiscIfExpectedPackets_Object((1,3,6,1,2,1,213,1,3,2,1,2),_NhdpDiscIfExpectedPackets_Type())
nhdpDiscIfExpectedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscIfExpectedPackets.setStatus(_B)
if mibBuilder.loadTexts:nhdpDiscIfExpectedPackets.setUnits(_w)
_NhdpNibNeighborSetChanges_Type=Counter32
_NhdpNibNeighborSetChanges_Object=MibScalar
nhdpNibNeighborSetChanges=_NhdpNibNeighborSetChanges_Object((1,3,6,1,2,1,213,1,3,3),_NhdpNibNeighborSetChanges_Type())
nhdpNibNeighborSetChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpNibNeighborSetChanges.setStatus(_B)
if mibBuilder.loadTexts:nhdpNibNeighborSetChanges.setUnits(_J)
_NhdpDiscNeighborSetPerfTable_Object=MibTable
nhdpDiscNeighborSetPerfTable=_NhdpDiscNeighborSetPerfTable_Object((1,3,6,1,2,1,213,1,3,4))
if mibBuilder.loadTexts:nhdpDiscNeighborSetPerfTable.setStatus(_B)
_NhdpDiscNeighborSetPerfEntry_Object=MibTableRow
nhdpDiscNeighborSetPerfEntry=_NhdpDiscNeighborSetPerfEntry_Object((1,3,6,1,2,1,213,1,3,4,1))
nhdpDiscNeighborSetPerfEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:nhdpDiscNeighborSetPerfEntry.setStatus(_B)
_NhdpDiscNeighborNibNeighborSetChanges_Type=Counter32
_NhdpDiscNeighborNibNeighborSetChanges_Object=MibTableColumn
nhdpDiscNeighborNibNeighborSetChanges=_NhdpDiscNeighborNibNeighborSetChanges_Object((1,3,6,1,2,1,213,1,3,4,1,1),_NhdpDiscNeighborNibNeighborSetChanges_Type())
nhdpDiscNeighborNibNeighborSetChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscNeighborNibNeighborSetChanges.setStatus(_B)
if mibBuilder.loadTexts:nhdpDiscNeighborNibNeighborSetChanges.setUnits(_J)
_NhdpDiscNeighborNibNeighborSetUpTime_Type=TimeStamp
_NhdpDiscNeighborNibNeighborSetUpTime_Object=MibTableColumn
nhdpDiscNeighborNibNeighborSetUpTime=_NhdpDiscNeighborNibNeighborSetUpTime_Object((1,3,6,1,2,1,213,1,3,4,1,2),_NhdpDiscNeighborNibNeighborSetUpTime_Type())
nhdpDiscNeighborNibNeighborSetUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscNeighborNibNeighborSetUpTime.setStatus(_B)
_NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Type=Counter32
_NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Object=MibTableColumn
nhdpDiscNeighborNibNeighborSetReachableLinkChanges=_NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Object((1,3,6,1,2,1,213,1,3,4,1,3),_NhdpDiscNeighborNibNeighborSetReachableLinkChanges_Type())
nhdpDiscNeighborNibNeighborSetReachableLinkChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpDiscNeighborNibNeighborSetReachableLinkChanges.setStatus(_B)
if mibBuilder.loadTexts:nhdpDiscNeighborNibNeighborSetReachableLinkChanges.setUnits(_J)
_NhdpIib2HopSetPerfTable_Object=MibTable
nhdpIib2HopSetPerfTable=_NhdpIib2HopSetPerfTable_Object((1,3,6,1,2,1,213,1,3,5))
if mibBuilder.loadTexts:nhdpIib2HopSetPerfTable.setStatus(_B)
_NhdpIib2HopSetPerfEntry_Object=MibTableRow
nhdpIib2HopSetPerfEntry=_NhdpIib2HopSetPerfEntry_Object((1,3,6,1,2,1,213,1,3,5,1))
nhdpIib2HopSetPerfEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:nhdpIib2HopSetPerfEntry.setStatus(_B)
_NhdpIib2HopSetPerfChanges_Type=Counter32
_NhdpIib2HopSetPerfChanges_Object=MibTableColumn
nhdpIib2HopSetPerfChanges=_NhdpIib2HopSetPerfChanges_Object((1,3,6,1,2,1,213,1,3,5,1,1),_NhdpIib2HopSetPerfChanges_Type())
nhdpIib2HopSetPerfChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIib2HopSetPerfChanges.setStatus(_B)
if mibBuilder.loadTexts:nhdpIib2HopSetPerfChanges.setUnits(_J)
_NhdpIib2HopSetPerfUpTime_Type=TimeStamp
_NhdpIib2HopSetPerfUpTime_Object=MibTableColumn
nhdpIib2HopSetPerfUpTime=_NhdpIib2HopSetPerfUpTime_Object((1,3,6,1,2,1,213,1,3,5,1,2),_NhdpIib2HopSetPerfUpTime_Type())
nhdpIib2HopSetPerfUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nhdpIib2HopSetPerfUpTime.setStatus(_B)
_NhdpConformance_ObjectIdentity=ObjectIdentity
nhdpConformance=_NhdpConformance_ObjectIdentity((1,3,6,1,2,1,213,2))
_NhdpCompliances_ObjectIdentity=ObjectIdentity
nhdpCompliances=_NhdpCompliances_ObjectIdentity((1,3,6,1,2,1,213,2,1))
_NhdpMIBGroups_ObjectIdentity=ObjectIdentity
nhdpMIBGroups=_NhdpMIBGroups_ObjectIdentity((1,3,6,1,2,1,213,2,2))
nhdpConfigurationGroup=ObjectGroup((1,3,6,1,2,1,213,2,2,2))
nhdpConfigurationGroup.setObjects(*((_A,_O),(_A,_V),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:nhdpConfigurationGroup.setStatus(_B)
nhdpStateGroup=ObjectGroup((1,3,6,1,2,1,213,2,2,3))
nhdpStateGroup.setObjects(*((_A,_W),(_A,_X),(_A,_H),(_A,_M),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:nhdpStateGroup.setStatus(_AL)
nhdpPerformanceGroup=ObjectGroup((1,3,6,1,2,1,213,2,2,4))
nhdpPerformanceGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:nhdpPerformanceGroup.setStatus(_B)
nhdpNotificationObjectGroup=ObjectGroup((1,3,6,1,2,1,213,2,2,5))
nhdpNotificationObjectGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:nhdpNotificationObjectGroup.setStatus(_B)
nhdpStateGroup2=ObjectGroup((1,3,6,1,2,1,213,2,2,7))
nhdpStateGroup2.setObjects(*((_A,_W),(_A,_X),(_A,_H),(_A,_M),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_Ai),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:nhdpStateGroup2.setStatus(_B)
nhdpNbrStateChange=NotificationType((1,3,6,1,2,1,213,0,0,1))
nhdpNbrStateChange.setObjects(*((_A,_O),(_A,_l)))
if mibBuilder.loadTexts:nhdpNbrStateChange.setStatus(_B)
nhdp2HopNbrStateChange=NotificationType((1,3,6,1,2,1,213,0,0,2))
nhdp2HopNbrStateChange.setObjects(*((_A,_O),(_A,_m)))
if mibBuilder.loadTexts:nhdp2HopNbrStateChange.setStatus(_B)
nhdpIfStateChange=NotificationType((1,3,6,1,2,1,213,0,0,3))
nhdpIfStateChange.setObjects(*((_A,_O),(_A,_V)))
if mibBuilder.loadTexts:nhdpIfStateChange.setStatus(_B)
nhdpNotificationGroup=NotificationGroup((1,3,6,1,2,1,213,2,2,6))
nhdpNotificationGroup.setObjects(*((_A,_Aj),(_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:nhdpNotificationGroup.setStatus(_B)
nhdpBasicCompliance=ModuleCompliance((1,3,6,1,2,1,213,2,1,1))
nhdpBasicCompliance.setObjects((_A,_Q))
if mibBuilder.loadTexts:nhdpBasicCompliance.setStatus(_B)
nhdpFullCompliance=ModuleCompliance((1,3,6,1,2,1,213,2,1,2))
nhdpFullCompliance.setObjects(*((_A,_Q),(_A,_Am),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:nhdpFullCompliance.setStatus(_AL)
nhdpFullCompliance2=ModuleCompliance((1,3,6,1,2,1,213,2,1,3))
nhdpFullCompliance2.setObjects(*((_A,_Q),(_A,_An),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:nhdpFullCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NeighborIfIndex':NeighborIfIndex,'NeighborRouterIndex':NeighborRouterIndex,'nhdpMIB':nhdpMIB,'nhdpNotifications':nhdpNotifications,'nhdpNotificationsObjects':nhdpNotificationsObjects,_Aj:nhdpNbrStateChange,_Ak:nhdp2HopNbrStateChange,_Al:nhdpIfStateChange,'nhdpNotificationsControl':nhdpNotificationsControl,_Ae:nhdpNbrStateChangeThreshold,_Af:nhdpNbrStateChangeWindow,_Ag:nhdp2HopNbrStateChangeThreshold,_Ah:nhdp2HopNbrStateChangeWindow,'nhdpNotificationsStates':nhdpNotificationsStates,_l:nhdpNbrState,_m:nhdp2HopNbrState,'nhdpObjects':nhdpObjects,'nhdpConfigurationObjGrp':nhdpConfigurationObjGrp,'nhdpInterfaceTable':nhdpInterfaceTable,'nhdpInterfaceEntry':nhdpInterfaceEntry,_K:nhdpIfIndex,_O:nhdpIfName,_V:nhdpIfStatus,_x:nhdpHelloInterval,_y:nhdpHelloMinInterval,_z:nhdpRefreshInterval,_A0:nhdpLHoldTime,_A1:nhdpHHoldTime,_A2:nhdpHystAcceptQuality,_A3:nhdpHystRejectQuality,_A4:nhdpInitialQuality,_A5:nhdpInitialPending,_A6:nhdpHpMaxJitter,_A7:nhdpHtMaxJitter,_AA:nhdpIfRowStatus,_A8:nhdpNHoldTime,_A9:nhdpIHoldTime,'nhdpLibLocalIfSetTable':nhdpLibLocalIfSetTable,'nhdpLibLocalIfSetEntry':nhdpLibLocalIfSetEntry,_q:nhdpLibLocalIfSetIndex,_AB:nhdpLibLocalIfSetIfIndex,_AC:nhdpLibLocalIfSetIpAddrType,_AD:nhdpLibLocalIfSetIpAddr,_AE:nhdpLibLocalIfSetIpAddrPrefixLen,_AF:nhdpLibLocalIfSetRowStatus,'nhdpLibRemovedIfAddrSetTable':nhdpLibRemovedIfAddrSetTable,'nhdpLibRemovedIfAddrSetEntry':nhdpLibRemovedIfAddrSetEntry,_r:nhdpLibRemovedIfAddrSetIndex,_AG:nhdpLibRemovedIfAddrSetIpAddrType,_AH:nhdpLibRemovedIfAddrSetIpAddr,_AI:nhdpLibRemovedIfAddrSetIpAddrPrefixLen,_AJ:nhdpLibRemovedIfAddrSetIfIndex,_AK:nhdpLibRemovedIfAddrSetIRTime,'nhdpStateObjGrp':nhdpStateObjGrp,_W:nhdpUpTime,'nhdpInterfaceStateTable':nhdpInterfaceStateTable,'nhdpInterfaceStateEntry':nhdpInterfaceStateEntry,_X:nhdpIfStateUpTime,'nhdpDiscIfSetTable':nhdpDiscIfSetTable,'nhdpDiscIfSetEntry':nhdpDiscIfSetEntry,_s:nhdpDiscIfSetIndex,_M:nhdpDiscIfIndex,_H:nhdpDiscRouterIndex,_Y:nhdpDiscIfSetIpAddrType,_Z:nhdpDiscIfSetIpAddr,_a:nhdpDiscIfSetIpAddrPrefixLen,'nhdpIibLinkSetTable':nhdpIibLinkSetTable,'nhdpIibLinkSetEntry':nhdpIibLinkSetEntry,_b:nhdpIibLinkSetLHeardTime,_c:nhdpIibLinkSetLSymTime,_d:nhdpIibLinkSetLPending,_e:nhdpIibLinkSetLLost,_f:nhdpIibLinkSetLTime,'nhdpIib2HopSetTable':nhdpIib2HopSetTable,'nhdpIib2HopSetEntry':nhdpIib2HopSetEntry,_t:nhdpIib2HopSetIpAddressType,_u:nhdpIib2HopSetIpAddress,_g:nhdpIib2HopSetIpAddrPrefixLen,_h:nhdpIib2HopSet1HopIfIndex,_i:nhdpIib2HopSetN2Time,_Ai:nhdpIib2HopSetN2Lost,'nhdpNibNeighborSetTable':nhdpNibNeighborSetTable,'nhdpNibNeighborSetEntry':nhdpNibNeighborSetEntry,_j:nhdpNibNeighborSetNSymmetric,'nhdpNibLostNeighborSetTable':nhdpNibLostNeighborSetTable,'nhdpNibLostNeighborSetEntry':nhdpNibLostNeighborSetEntry,_k:nhdpNibLostNeighborSetNLTime,'nhdpPerformanceObjGrp':nhdpPerformanceObjGrp,'nhdpInterfacePerfTable':nhdpInterfacePerfTable,'nhdpInterfacePerfEntry':nhdpInterfacePerfEntry,_AM:nhdpIfHelloMessageXmits,_AN:nhdpIfHelloMessageRecvd,_AO:nhdpIfHelloMessageXmitAccumulatedSize,_AP:nhdpIfHelloMessageRecvdAccumulatedSize,_AQ:nhdpIfHelloMessageTriggeredXmits,_AR:nhdpIfHelloMessagePeriodicXmits,_AS:nhdpIfHelloMessageXmitAccumulatedSymmetricNeighborCount,_AT:nhdpIfHelloMessageXmitAccumulatedHeardNeighborCount,_AU:nhdpIfHelloMessageXmitAccumulatedLostNeighborCount,_AV:nhdpIfPerfCounterDiscontinuityTime,'nhdpDiscIfSetPerfTable':nhdpDiscIfSetPerfTable,'nhdpDiscIfSetPerfEntry':nhdpDiscIfSetPerfEntry,_AW:nhdpDiscIfRecvdPackets,_AX:nhdpDiscIfExpectedPackets,_AY:nhdpNibNeighborSetChanges,'nhdpDiscNeighborSetPerfTable':nhdpDiscNeighborSetPerfTable,'nhdpDiscNeighborSetPerfEntry':nhdpDiscNeighborSetPerfEntry,_AZ:nhdpDiscNeighborNibNeighborSetChanges,_Aa:nhdpDiscNeighborNibNeighborSetUpTime,_Ab:nhdpDiscNeighborNibNeighborSetReachableLinkChanges,'nhdpIib2HopSetPerfTable':nhdpIib2HopSetPerfTable,'nhdpIib2HopSetPerfEntry':nhdpIib2HopSetPerfEntry,_Ac:nhdpIib2HopSetPerfChanges,_Ad:nhdpIib2HopSetPerfUpTime,'nhdpConformance':nhdpConformance,'nhdpCompliances':nhdpCompliances,'nhdpBasicCompliance':nhdpBasicCompliance,'nhdpFullCompliance':nhdpFullCompliance,'nhdpFullCompliance2':nhdpFullCompliance2,'nhdpMIBGroups':nhdpMIBGroups,_Q:nhdpConfigurationGroup,_Am:nhdpStateGroup,_p:nhdpPerformanceGroup,_n:nhdpNotificationObjectGroup,_o:nhdpNotificationGroup,_An:nhdpStateGroup2})