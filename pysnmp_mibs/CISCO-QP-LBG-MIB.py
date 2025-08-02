_AO='cqlciscoQpLbgNotifsControlGroup1'
_AN='cqlciscoQpObjectGroup1'
_AM='cqlciscoQpNotifsGroup1'
_AL='cqlciscoQpLbgNotifsControlGroup'
_AK='cqlciscoQpObjectGroup'
_AJ='cqlciscoQpNotifsGroup'
_AI='cqlQamOverSubscribedAlert'
_AH='cqlLbgRouteDelete'
_AG='cqlLbgRouteAdd'
_AF='cqlQamOverSubscribedEnable'
_AE='cqlqpServerIpList'
_AD='cqllbgDstIpAddrType'
_AC='cqllbgNumFlows'
_AB='cqllbgRsvBandwidth'
_AA='cqllbgAllocatedBandwidth'
_A9='cqllbgGqiIngressPort'
_A8='cqllbgUdpPortRangeMax'
_A7='cqllbgUdpPortRangeMin'
_A6='cqllbgDstIpAddr'
_A5='cqllbgQpId'
_A4='cqllbgAvailableBandwidth'
_A3='cqllbgIpRsvBandwidth'
_A2='cqllbgQamRsvBandwidth'
_A1='cqllbgTotalBandwidth'
_A0='cqllbgRouteIndex'
_z='cqllbgIndex'
_y='cqlqpIndex'
_x='cqlciscoLbgObjectGroup'
_w='cqlciscoLbgNotifsGroup'
_v='cqlciscoLbgRouteObjectGroup'
_u='cqlQamDelete'
_t='cqlQamAdd'
_s='cqlQpStateChange'
_r='cqlqpQamOversubscribedStatus'
_q='cqlRouteNotifyEnable'
_p='cqlQamNotifyEnable'
_o='cqlQpNotifyEnable'
_n='cqlqpServerIpAddrType'
_m='cqlqpMgmtIpAddrType'
_l='cqlqpErmiRtspSessionTimeout'
_k='cqlqpErmiRtspKeepAliveTime'
_j='cqlqpErmiRtspConnectTime'
_i='cqlqpErmiRtspConnectRetry'
_h='cqlqpErmiErrpHoldTime'
_g='cqlqpErmiErrpConnnectTime'
_f='cqlqpErmiErrpConnectRetry'
_e='cqlqpErmiErrpStreamingZone'
_d='cqlqpErmiErrpComponentName'
_c='cqlqpNumRoutes'
_b='cqlqpQamCarrrierList'
_a='cqlqpNumQams'
_Z='cqlqpGqiMacAddr'
_Y='cqlqpServerState'
_X='cqlqpServerIp'
_W='cqlqpGqiResetInterval'
_V='cqlqpKeepAliveTime'
_U='cqlqpProtocol'
_T='cqlqpMgmtIp'
_S='not-accessible'
_R='InetAddressType'
_Q='entPhysicalIndex'
_P='ENTITY-MIB'
_O='deprecated'
_N='cqlqpState'
_M='read-write'
_L='Integer32'
_K='ifDescr'
_J='IF-MIB'
_I='cqlqpRouteDetails'
_H='cqlqpId'
_G='Kbps'
_F='TruthValue'
_E='Unsigned32'
_D='seconds'
_C='read-only'
_B='current'
_A='CISCO-QP-LBG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_P,_Q)
ifDescr,=mibBuilder.importSymbols(_J,_K)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_F)
ciscoQpLbgMIB=ModuleIdentity((1,3,6,1,4,1,9,9,824))
if mibBuilder.loadTexts:ciscoQpLbgMIB.setRevisions(('2015-09-21 00:00','2014-08-27 00:00'))
_CiscoQpLbgNotifs_ObjectIdentity=ObjectIdentity
ciscoQpLbgNotifs=_CiscoQpLbgNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,824,0))
_CiscoQpLbgObjects_ObjectIdentity=ObjectIdentity
ciscoQpLbgObjects=_CiscoQpLbgObjects_ObjectIdentity((1,3,6,1,4,1,9,9,824,1))
_CqlqamPartitionTable_Object=MibTable
cqlqamPartitionTable=_CqlqamPartitionTable_Object((1,3,6,1,4,1,9,9,824,1,1))
if mibBuilder.loadTexts:cqlqamPartitionTable.setStatus(_B)
_CqlqamPartitionEntry_Object=MibTableRow
cqlqamPartitionEntry=_CqlqamPartitionEntry_Object((1,3,6,1,4,1,9,9,824,1,1,1))
cqlqamPartitionEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:cqlqamPartitionEntry.setStatus(_B)
_CqlqpIndex_Type=Unsigned32
_CqlqpIndex_Object=MibTableColumn
cqlqpIndex=_CqlqpIndex_Object((1,3,6,1,4,1,9,9,824,1,1,1,1),_CqlqpIndex_Type())
cqlqpIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cqlqpIndex.setStatus(_B)
_CqlqpId_Type=Unsigned32
_CqlqpId_Object=MibTableColumn
cqlqpId=_CqlqpId_Object((1,3,6,1,4,1,9,9,824,1,1,1,2),_CqlqpId_Type())
cqlqpId.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpId.setStatus(_B)
class _CqlqpMgmtIpAddrType_Type(InetAddressType):defaultValue=1
_CqlqpMgmtIpAddrType_Type.__name__=_R
_CqlqpMgmtIpAddrType_Object=MibTableColumn
cqlqpMgmtIpAddrType=_CqlqpMgmtIpAddrType_Object((1,3,6,1,4,1,9,9,824,1,1,1,3),_CqlqpMgmtIpAddrType_Type())
cqlqpMgmtIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpMgmtIpAddrType.setStatus(_B)
_CqlqpMgmtIp_Type=InetAddress
_CqlqpMgmtIp_Object=MibTableColumn
cqlqpMgmtIp=_CqlqpMgmtIp_Object((1,3,6,1,4,1,9,9,824,1,1,1,4),_CqlqpMgmtIp_Type())
cqlqpMgmtIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpMgmtIp.setStatus(_B)
_CqlqpServerIpAddrType_Type=InetAddressType
_CqlqpServerIpAddrType_Object=MibTableColumn
cqlqpServerIpAddrType=_CqlqpServerIpAddrType_Object((1,3,6,1,4,1,9,9,824,1,1,1,5),_CqlqpServerIpAddrType_Type())
cqlqpServerIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpServerIpAddrType.setStatus(_B)
_CqlqpServerIp_Type=InetAddress
_CqlqpServerIp_Object=MibTableColumn
cqlqpServerIp=_CqlqpServerIp_Object((1,3,6,1,4,1,9,9,824,1,1,1,6),_CqlqpServerIp_Type())
cqlqpServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpServerIp.setStatus(_B)
class _CqlqpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('init',2),('active',3)))
_CqlqpState_Type.__name__=_L
_CqlqpState_Object=MibTableColumn
cqlqpState=_CqlqpState_Object((1,3,6,1,4,1,9,9,824,1,1,1,7),_CqlqpState_Type())
cqlqpState.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpState.setStatus(_B)
class _CqlqpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gqi',1),('ermi',2)))
_CqlqpProtocol_Type.__name__=_L
_CqlqpProtocol_Object=MibTableColumn
cqlqpProtocol=_CqlqpProtocol_Object((1,3,6,1,4,1,9,9,824,1,1,1,8),_CqlqpProtocol_Type())
cqlqpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpProtocol.setStatus(_B)
_CqlqpKeepAliveTime_Type=Unsigned32
_CqlqpKeepAliveTime_Object=MibTableColumn
cqlqpKeepAliveTime=_CqlqpKeepAliveTime_Object((1,3,6,1,4,1,9,9,824,1,1,1,9),_CqlqpKeepAliveTime_Type())
cqlqpKeepAliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpKeepAliveTime.setStatus(_B)
if mibBuilder.loadTexts:cqlqpKeepAliveTime.setUnits(_D)
class _CqlqpServerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disconnected',1),('connected',2)))
_CqlqpServerState_Type.__name__=_L
_CqlqpServerState_Object=MibTableColumn
cqlqpServerState=_CqlqpServerState_Object((1,3,6,1,4,1,9,9,824,1,1,1,10),_CqlqpServerState_Type())
cqlqpServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpServerState.setStatus(_B)
_CqlqpGqiMacAddr_Type=MacAddress
_CqlqpGqiMacAddr_Object=MibTableColumn
cqlqpGqiMacAddr=_CqlqpGqiMacAddr_Object((1,3,6,1,4,1,9,9,824,1,1,1,11),_CqlqpGqiMacAddr_Type())
cqlqpGqiMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpGqiMacAddr.setStatus(_B)
_CqlqpGqiResetInterval_Type=Unsigned32
_CqlqpGqiResetInterval_Object=MibTableColumn
cqlqpGqiResetInterval=_CqlqpGqiResetInterval_Object((1,3,6,1,4,1,9,9,824,1,1,1,12),_CqlqpGqiResetInterval_Type())
cqlqpGqiResetInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpGqiResetInterval.setStatus(_B)
if mibBuilder.loadTexts:cqlqpGqiResetInterval.setUnits(_D)
_CqlqpNumQams_Type=Unsigned32
_CqlqpNumQams_Object=MibTableColumn
cqlqpNumQams=_CqlqpNumQams_Object((1,3,6,1,4,1,9,9,824,1,1,1,13),_CqlqpNumQams_Type())
cqlqpNumQams.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpNumQams.setStatus(_B)
_CqlqpQamCarrrierList_Type=OctetString
_CqlqpQamCarrrierList_Object=MibTableColumn
cqlqpQamCarrrierList=_CqlqpQamCarrrierList_Object((1,3,6,1,4,1,9,9,824,1,1,1,14),_CqlqpQamCarrrierList_Type())
cqlqpQamCarrrierList.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpQamCarrrierList.setStatus(_B)
_CqlqpNumRoutes_Type=Unsigned32
_CqlqpNumRoutes_Object=MibTableColumn
cqlqpNumRoutes=_CqlqpNumRoutes_Object((1,3,6,1,4,1,9,9,824,1,1,1,15),_CqlqpNumRoutes_Type())
cqlqpNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpNumRoutes.setStatus(_B)
_CqlqpRouteDetails_Type=OctetString
_CqlqpRouteDetails_Object=MibTableColumn
cqlqpRouteDetails=_CqlqpRouteDetails_Object((1,3,6,1,4,1,9,9,824,1,1,1,16),_CqlqpRouteDetails_Type())
cqlqpRouteDetails.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpRouteDetails.setStatus(_B)
_CqlqpErmiErrpComponentName_Type=OctetString
_CqlqpErmiErrpComponentName_Object=MibTableColumn
cqlqpErmiErrpComponentName=_CqlqpErmiErrpComponentName_Object((1,3,6,1,4,1,9,9,824,1,1,1,17),_CqlqpErmiErrpComponentName_Type())
cqlqpErmiErrpComponentName.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiErrpComponentName.setStatus(_B)
_CqlqpErmiErrpStreamingZone_Type=OctetString
_CqlqpErmiErrpStreamingZone_Object=MibTableColumn
cqlqpErmiErrpStreamingZone=_CqlqpErmiErrpStreamingZone_Object((1,3,6,1,4,1,9,9,824,1,1,1,18),_CqlqpErmiErrpStreamingZone_Type())
cqlqpErmiErrpStreamingZone.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiErrpStreamingZone.setStatus(_B)
class _CqlqpErmiErrpHoldTime_Type(Unsigned32):defaultValue=90
_CqlqpErmiErrpHoldTime_Type.__name__=_E
_CqlqpErmiErrpHoldTime_Object=MibTableColumn
cqlqpErmiErrpHoldTime=_CqlqpErmiErrpHoldTime_Object((1,3,6,1,4,1,9,9,824,1,1,1,19),_CqlqpErmiErrpHoldTime_Type())
cqlqpErmiErrpHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiErrpHoldTime.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiErrpHoldTime.setUnits(_D)
class _CqlqpErmiErrpConnnectTime_Type(Unsigned32):defaultValue=10
_CqlqpErmiErrpConnnectTime_Type.__name__=_E
_CqlqpErmiErrpConnnectTime_Object=MibTableColumn
cqlqpErmiErrpConnnectTime=_CqlqpErmiErrpConnnectTime_Object((1,3,6,1,4,1,9,9,824,1,1,1,20),_CqlqpErmiErrpConnnectTime_Type())
cqlqpErmiErrpConnnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiErrpConnnectTime.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiErrpConnnectTime.setUnits(_D)
class _CqlqpErmiErrpConnectRetry_Type(Unsigned32):defaultValue=0
_CqlqpErmiErrpConnectRetry_Type.__name__=_E
_CqlqpErmiErrpConnectRetry_Object=MibTableColumn
cqlqpErmiErrpConnectRetry=_CqlqpErmiErrpConnectRetry_Object((1,3,6,1,4,1,9,9,824,1,1,1,21),_CqlqpErmiErrpConnectRetry_Type())
cqlqpErmiErrpConnectRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiErrpConnectRetry.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiErrpConnectRetry.setUnits(_D)
class _CqlqpErmiRtspConnectTime_Type(Unsigned32):defaultValue=200
_CqlqpErmiRtspConnectTime_Type.__name__=_E
_CqlqpErmiRtspConnectTime_Object=MibTableColumn
cqlqpErmiRtspConnectTime=_CqlqpErmiRtspConnectTime_Object((1,3,6,1,4,1,9,9,824,1,1,1,22),_CqlqpErmiRtspConnectTime_Type())
cqlqpErmiRtspConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiRtspConnectTime.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiRtspConnectTime.setUnits(_D)
class _CqlqpErmiRtspConnectRetry_Type(Unsigned32):defaultValue=0
_CqlqpErmiRtspConnectRetry_Type.__name__=_E
_CqlqpErmiRtspConnectRetry_Object=MibTableColumn
cqlqpErmiRtspConnectRetry=_CqlqpErmiRtspConnectRetry_Object((1,3,6,1,4,1,9,9,824,1,1,1,23),_CqlqpErmiRtspConnectRetry_Type())
cqlqpErmiRtspConnectRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiRtspConnectRetry.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiRtspConnectRetry.setUnits(_D)
class _CqlqpErmiRtspKeepAliveTime_Type(Unsigned32):defaultValue=300
_CqlqpErmiRtspKeepAliveTime_Type.__name__=_E
_CqlqpErmiRtspKeepAliveTime_Object=MibTableColumn
cqlqpErmiRtspKeepAliveTime=_CqlqpErmiRtspKeepAliveTime_Object((1,3,6,1,4,1,9,9,824,1,1,1,24),_CqlqpErmiRtspKeepAliveTime_Type())
cqlqpErmiRtspKeepAliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiRtspKeepAliveTime.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiRtspKeepAliveTime.setUnits(_D)
class _CqlqpErmiRtspSessionTimeout_Type(Unsigned32):defaultValue=10800
_CqlqpErmiRtspSessionTimeout_Type.__name__=_E
_CqlqpErmiRtspSessionTimeout_Object=MibTableColumn
cqlqpErmiRtspSessionTimeout=_CqlqpErmiRtspSessionTimeout_Object((1,3,6,1,4,1,9,9,824,1,1,1,25),_CqlqpErmiRtspSessionTimeout_Type())
cqlqpErmiRtspSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpErmiRtspSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:cqlqpErmiRtspSessionTimeout.setUnits(_D)
class _CqlqpQamOversubscribedStatus_Type(TruthValue):defaultValue=2
_CqlqpQamOversubscribedStatus_Type.__name__=_F
_CqlqpQamOversubscribedStatus_Object=MibTableColumn
cqlqpQamOversubscribedStatus=_CqlqpQamOversubscribedStatus_Object((1,3,6,1,4,1,9,9,824,1,1,1,26),_CqlqpQamOversubscribedStatus_Type())
cqlqpQamOversubscribedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpQamOversubscribedStatus.setStatus(_B)
_CqlqpServerIpList_Type=OctetString
_CqlqpServerIpList_Object=MibTableColumn
cqlqpServerIpList=_CqlqpServerIpList_Object((1,3,6,1,4,1,9,9,824,1,1,1,27),_CqlqpServerIpList_Type())
cqlqpServerIpList.setMaxAccess(_C)
if mibBuilder.loadTexts:cqlqpServerIpList.setStatus(_B)
_CqlloadBalanceGroupTable_Object=MibTable
cqlloadBalanceGroupTable=_CqlloadBalanceGroupTable_Object((1,3,6,1,4,1,9,9,824,1,2))
if mibBuilder.loadTexts:cqlloadBalanceGroupTable.setStatus(_B)
_CqlloadBalanceGroupEntry_Object=MibTableRow
cqlloadBalanceGroupEntry=_CqlloadBalanceGroupEntry_Object((1,3,6,1,4,1,9,9,824,1,2,1))
cqlloadBalanceGroupEntry.setIndexNames((0,_P,_Q),(0,_A,_z))
if mibBuilder.loadTexts:cqlloadBalanceGroupEntry.setStatus(_B)
_CqllbgIndex_Type=Unsigned32
_CqllbgIndex_Object=MibTableColumn
cqllbgIndex=_CqllbgIndex_Object((1,3,6,1,4,1,9,9,824,1,2,1,1),_CqllbgIndex_Type())
cqllbgIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cqllbgIndex.setStatus(_B)
_CqllbgTotalBandwidth_Type=Unsigned32
_CqllbgTotalBandwidth_Object=MibTableColumn
cqllbgTotalBandwidth=_CqllbgTotalBandwidth_Object((1,3,6,1,4,1,9,9,824,1,2,1,2),_CqllbgTotalBandwidth_Type())
cqllbgTotalBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgTotalBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cqllbgTotalBandwidth.setUnits(_G)
_CqllbgQamRsvBandwidth_Type=Unsigned32
_CqllbgQamRsvBandwidth_Object=MibTableColumn
cqllbgQamRsvBandwidth=_CqllbgQamRsvBandwidth_Object((1,3,6,1,4,1,9,9,824,1,2,1,3),_CqllbgQamRsvBandwidth_Type())
cqllbgQamRsvBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgQamRsvBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cqllbgQamRsvBandwidth.setUnits(_G)
_CqllbgIpRsvBandwidth_Type=Unsigned32
_CqllbgIpRsvBandwidth_Object=MibTableColumn
cqllbgIpRsvBandwidth=_CqllbgIpRsvBandwidth_Object((1,3,6,1,4,1,9,9,824,1,2,1,4),_CqllbgIpRsvBandwidth_Type())
cqllbgIpRsvBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgIpRsvBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cqllbgIpRsvBandwidth.setUnits(_G)
_CqllbgAvailableBandwidth_Type=Unsigned32
_CqllbgAvailableBandwidth_Object=MibTableColumn
cqllbgAvailableBandwidth=_CqllbgAvailableBandwidth_Object((1,3,6,1,4,1,9,9,824,1,2,1,5),_CqllbgAvailableBandwidth_Type())
cqllbgAvailableBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgAvailableBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cqllbgAvailableBandwidth.setUnits(_G)
_CqllbgrouteTable_Object=MibTable
cqllbgrouteTable=_CqllbgrouteTable_Object((1,3,6,1,4,1,9,9,824,1,3))
if mibBuilder.loadTexts:cqllbgrouteTable.setStatus(_B)
_CqllbgrouteEntry_Object=MibTableRow
cqllbgrouteEntry=_CqllbgrouteEntry_Object((1,3,6,1,4,1,9,9,824,1,3,1))
cqllbgrouteEntry.setIndexNames((0,_P,_Q),(0,_A,_A0))
if mibBuilder.loadTexts:cqllbgrouteEntry.setStatus(_B)
_CqllbgRouteIndex_Type=Unsigned32
_CqllbgRouteIndex_Object=MibTableColumn
cqllbgRouteIndex=_CqllbgRouteIndex_Object((1,3,6,1,4,1,9,9,824,1,3,1,1),_CqllbgRouteIndex_Type())
cqllbgRouteIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:cqllbgRouteIndex.setStatus(_B)
_CqllbgQpId_Type=Unsigned32
_CqllbgQpId_Object=MibTableColumn
cqllbgQpId=_CqllbgQpId_Object((1,3,6,1,4,1,9,9,824,1,3,1,2),_CqllbgQpId_Type())
cqllbgQpId.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgQpId.setStatus(_B)
class _CqllbgDstIpAddrType_Type(InetAddressType):defaultValue=1
_CqllbgDstIpAddrType_Type.__name__=_R
_CqllbgDstIpAddrType_Object=MibTableColumn
cqllbgDstIpAddrType=_CqllbgDstIpAddrType_Object((1,3,6,1,4,1,9,9,824,1,3,1,3),_CqllbgDstIpAddrType_Type())
cqllbgDstIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgDstIpAddrType.setStatus(_B)
_CqllbgDstIpAddr_Type=InetAddress
_CqllbgDstIpAddr_Object=MibTableColumn
cqllbgDstIpAddr=_CqllbgDstIpAddr_Object((1,3,6,1,4,1,9,9,824,1,3,1,4),_CqllbgDstIpAddr_Type())
cqllbgDstIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgDstIpAddr.setStatus(_B)
_CqllbgUdpPortRangeMin_Type=Unsigned32
_CqllbgUdpPortRangeMin_Object=MibTableColumn
cqllbgUdpPortRangeMin=_CqllbgUdpPortRangeMin_Object((1,3,6,1,4,1,9,9,824,1,3,1,5),_CqllbgUdpPortRangeMin_Type())
cqllbgUdpPortRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgUdpPortRangeMin.setStatus(_B)
_CqllbgUdpPortRangeMax_Type=Unsigned32
_CqllbgUdpPortRangeMax_Object=MibTableColumn
cqllbgUdpPortRangeMax=_CqllbgUdpPortRangeMax_Object((1,3,6,1,4,1,9,9,824,1,3,1,6),_CqllbgUdpPortRangeMax_Type())
cqllbgUdpPortRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgUdpPortRangeMax.setStatus(_B)
_CqllbgGqiIngressPort_Type=Unsigned32
_CqllbgGqiIngressPort_Object=MibTableColumn
cqllbgGqiIngressPort=_CqllbgGqiIngressPort_Object((1,3,6,1,4,1,9,9,824,1,3,1,7),_CqllbgGqiIngressPort_Type())
cqllbgGqiIngressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgGqiIngressPort.setStatus(_B)
_CqllbgRsvBandwidth_Type=Unsigned32
_CqllbgRsvBandwidth_Object=MibTableColumn
cqllbgRsvBandwidth=_CqllbgRsvBandwidth_Object((1,3,6,1,4,1,9,9,824,1,3,1,8),_CqllbgRsvBandwidth_Type())
cqllbgRsvBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgRsvBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cqllbgRsvBandwidth.setUnits(_G)
_CqllbgAllocatedBandwidth_Type=Unsigned32
_CqllbgAllocatedBandwidth_Object=MibTableColumn
cqllbgAllocatedBandwidth=_CqllbgAllocatedBandwidth_Object((1,3,6,1,4,1,9,9,824,1,3,1,9),_CqllbgAllocatedBandwidth_Type())
cqllbgAllocatedBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgAllocatedBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cqllbgAllocatedBandwidth.setUnits(_G)
_CqllbgNumFlows_Type=Unsigned32
_CqllbgNumFlows_Object=MibTableColumn
cqllbgNumFlows=_CqllbgNumFlows_Object((1,3,6,1,4,1,9,9,824,1,3,1,10),_CqllbgNumFlows_Type())
cqllbgNumFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cqllbgNumFlows.setStatus(_B)
class _CqlQpNotifyEnable_Type(TruthValue):defaultValue=2
_CqlQpNotifyEnable_Type.__name__=_F
_CqlQpNotifyEnable_Object=MibScalar
cqlQpNotifyEnable=_CqlQpNotifyEnable_Object((1,3,6,1,4,1,9,9,824,1,4),_CqlQpNotifyEnable_Type())
cqlQpNotifyEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cqlQpNotifyEnable.setStatus(_B)
class _CqlQamNotifyEnable_Type(TruthValue):defaultValue=2
_CqlQamNotifyEnable_Type.__name__=_F
_CqlQamNotifyEnable_Object=MibScalar
cqlQamNotifyEnable=_CqlQamNotifyEnable_Object((1,3,6,1,4,1,9,9,824,1,5),_CqlQamNotifyEnable_Type())
cqlQamNotifyEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cqlQamNotifyEnable.setStatus(_B)
class _CqlRouteNotifyEnable_Type(TruthValue):defaultValue=2
_CqlRouteNotifyEnable_Type.__name__=_F
_CqlRouteNotifyEnable_Object=MibScalar
cqlRouteNotifyEnable=_CqlRouteNotifyEnable_Object((1,3,6,1,4,1,9,9,824,1,6),_CqlRouteNotifyEnable_Type())
cqlRouteNotifyEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cqlRouteNotifyEnable.setStatus(_B)
class _CqlQamOverSubscribedEnable_Type(TruthValue):defaultValue=2
_CqlQamOverSubscribedEnable_Type.__name__=_F
_CqlQamOverSubscribedEnable_Object=MibScalar
cqlQamOverSubscribedEnable=_CqlQamOverSubscribedEnable_Object((1,3,6,1,4,1,9,9,824,1,7),_CqlQamOverSubscribedEnable_Type())
cqlQamOverSubscribedEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:cqlQamOverSubscribedEnable.setStatus(_B)
_CiscoQpLbgConform_ObjectIdentity=ObjectIdentity
ciscoQpLbgConform=_CiscoQpLbgConform_ObjectIdentity((1,3,6,1,4,1,9,9,824,2))
_CiscoQpLbgCompliances_ObjectIdentity=ObjectIdentity
ciscoQpLbgCompliances=_CiscoQpLbgCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,824,2,1))
_CiscoQpLbgGroups_ObjectIdentity=ObjectIdentity
ciscoQpLbgGroups=_CiscoQpLbgGroups_ObjectIdentity((1,3,6,1,4,1,9,9,824,2,2))
cqlciscoQpObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,824,2,2,3))
cqlciscoQpObjectGroup.setObjects(*((_A,_H),(_A,_T),(_A,_N),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_I),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cqlciscoQpObjectGroup.setStatus(_O)
cqlciscoLbgObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,824,2,2,4))
cqlciscoLbgObjectGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cqlciscoLbgObjectGroup.setStatus(_B)
cqlciscoLbgRouteObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,824,2,2,5))
cqlciscoLbgRouteObjectGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:cqlciscoLbgRouteObjectGroup.setStatus(_B)
cqlciscoQpLbgNotifsControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,824,2,2,6))
cqlciscoQpLbgNotifsControlGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cqlciscoQpLbgNotifsControlGroup.setStatus(_O)
cqlciscoQpObjectGroup1=ObjectGroup((1,3,6,1,4,1,9,9,824,2,2,8))
cqlciscoQpObjectGroup1.setObjects(*((_A,_H),(_A,_m),(_A,_T),(_A,_n),(_A,_X),(_A,_N),(_A,_U),(_A,_V),(_A,_Y),(_A,_Z),(_A,_W),(_A,_a),(_A,_b),(_A,_c),(_A,_I),(_A,_d),(_A,_e),(_A,_h),(_A,_g),(_A,_f),(_A,_j),(_A,_i),(_A,_k),(_A,_l),(_A,_r),(_A,_AE)))
if mibBuilder.loadTexts:cqlciscoQpObjectGroup1.setStatus(_B)
cqlciscoQpLbgNotifsControlGroup1=ObjectGroup((1,3,6,1,4,1,9,9,824,2,2,9))
cqlciscoQpLbgNotifsControlGroup1.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_AF)))
if mibBuilder.loadTexts:cqlciscoQpLbgNotifsControlGroup1.setStatus(_B)
cqlQpStateChange=NotificationType((1,3,6,1,4,1,9,9,824,0,1))
cqlQpStateChange.setObjects((_A,_N))
if mibBuilder.loadTexts:cqlQpStateChange.setStatus(_B)
cqlQamAdd=NotificationType((1,3,6,1,4,1,9,9,824,0,2))
cqlQamAdd.setObjects(*((_A,_H),(_J,_K)))
if mibBuilder.loadTexts:cqlQamAdd.setStatus(_B)
cqlQamDelete=NotificationType((1,3,6,1,4,1,9,9,824,0,3))
cqlQamDelete.setObjects(*((_A,_H),(_J,_K)))
if mibBuilder.loadTexts:cqlQamDelete.setStatus(_B)
cqlLbgRouteAdd=NotificationType((1,3,6,1,4,1,9,9,824,0,4))
cqlLbgRouteAdd.setObjects((_A,_I))
if mibBuilder.loadTexts:cqlLbgRouteAdd.setStatus(_B)
cqlLbgRouteDelete=NotificationType((1,3,6,1,4,1,9,9,824,0,5))
cqlLbgRouteDelete.setObjects((_A,_I))
if mibBuilder.loadTexts:cqlLbgRouteDelete.setStatus(_B)
cqlQamOverSubscribedAlert=NotificationType((1,3,6,1,4,1,9,9,824,0,6))
cqlQamOverSubscribedAlert.setObjects(*((_J,_K),(_A,_r)))
if mibBuilder.loadTexts:cqlQamOverSubscribedAlert.setStatus(_B)
cqlciscoQpNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,824,2,2,1))
cqlciscoQpNotifsGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cqlciscoQpNotifsGroup.setStatus(_O)
cqlciscoLbgNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,824,2,2,2))
cqlciscoLbgNotifsGroup.setObjects(*((_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:cqlciscoLbgNotifsGroup.setStatus(_B)
cqlciscoQpNotifsGroup1=NotificationGroup((1,3,6,1,4,1,9,9,824,2,2,7))
cqlciscoQpNotifsGroup1.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_AI)))
if mibBuilder.loadTexts:cqlciscoQpNotifsGroup1.setStatus(_B)
cqlciscoQpLbgCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,824,2,1,1))
cqlciscoQpLbgCompliance.setObjects(*((_A,_v),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:cqlciscoQpLbgCompliance.setStatus(_O)
cqlciscoQpLbgCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,824,2,1,2))
cqlciscoQpLbgCompliance1.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cqlciscoQpLbgCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoQpLbgMIB':ciscoQpLbgMIB,'ciscoQpLbgNotifs':ciscoQpLbgNotifs,_s:cqlQpStateChange,_t:cqlQamAdd,_u:cqlQamDelete,_AG:cqlLbgRouteAdd,_AH:cqlLbgRouteDelete,_AI:cqlQamOverSubscribedAlert,'ciscoQpLbgObjects':ciscoQpLbgObjects,'cqlqamPartitionTable':cqlqamPartitionTable,'cqlqamPartitionEntry':cqlqamPartitionEntry,_y:cqlqpIndex,_H:cqlqpId,_m:cqlqpMgmtIpAddrType,_T:cqlqpMgmtIp,_n:cqlqpServerIpAddrType,_X:cqlqpServerIp,_N:cqlqpState,_U:cqlqpProtocol,_V:cqlqpKeepAliveTime,_Y:cqlqpServerState,_Z:cqlqpGqiMacAddr,_W:cqlqpGqiResetInterval,_a:cqlqpNumQams,_b:cqlqpQamCarrrierList,_c:cqlqpNumRoutes,_I:cqlqpRouteDetails,_d:cqlqpErmiErrpComponentName,_e:cqlqpErmiErrpStreamingZone,_h:cqlqpErmiErrpHoldTime,_g:cqlqpErmiErrpConnnectTime,_f:cqlqpErmiErrpConnectRetry,_j:cqlqpErmiRtspConnectTime,_i:cqlqpErmiRtspConnectRetry,_k:cqlqpErmiRtspKeepAliveTime,_l:cqlqpErmiRtspSessionTimeout,_r:cqlqpQamOversubscribedStatus,_AE:cqlqpServerIpList,'cqlloadBalanceGroupTable':cqlloadBalanceGroupTable,'cqlloadBalanceGroupEntry':cqlloadBalanceGroupEntry,_z:cqllbgIndex,_A1:cqllbgTotalBandwidth,_A2:cqllbgQamRsvBandwidth,_A3:cqllbgIpRsvBandwidth,_A4:cqllbgAvailableBandwidth,'cqllbgrouteTable':cqllbgrouteTable,'cqllbgrouteEntry':cqllbgrouteEntry,_A0:cqllbgRouteIndex,_A5:cqllbgQpId,_AD:cqllbgDstIpAddrType,_A6:cqllbgDstIpAddr,_A7:cqllbgUdpPortRangeMin,_A8:cqllbgUdpPortRangeMax,_A9:cqllbgGqiIngressPort,_AB:cqllbgRsvBandwidth,_AA:cqllbgAllocatedBandwidth,_AC:cqllbgNumFlows,_o:cqlQpNotifyEnable,_p:cqlQamNotifyEnable,_q:cqlRouteNotifyEnable,_AF:cqlQamOverSubscribedEnable,'ciscoQpLbgConform':ciscoQpLbgConform,'ciscoQpLbgCompliances':ciscoQpLbgCompliances,'cqlciscoQpLbgCompliance':cqlciscoQpLbgCompliance,'cqlciscoQpLbgCompliance1':cqlciscoQpLbgCompliance1,'ciscoQpLbgGroups':ciscoQpLbgGroups,_AJ:cqlciscoQpNotifsGroup,_w:cqlciscoLbgNotifsGroup,_AK:cqlciscoQpObjectGroup,_x:cqlciscoLbgObjectGroup,_v:cqlciscoLbgRouteObjectGroup,_AL:cqlciscoQpLbgNotifsControlGroup,_AM:cqlciscoQpNotifsGroup1,_AN:cqlciscoQpObjectGroup1,_AO:cqlciscoQpLbgNotifsControlGroup1})