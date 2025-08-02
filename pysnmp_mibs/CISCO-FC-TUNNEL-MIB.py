_Aw='cftTcpTunnelConfigGroup'
_Av='cftIfTcpHdrPredictOkForDataPkts'
_Au='cftIfTcpHdrPredictOkForAcks'
_At='cftIfTcpRetxSackFackTimeouts'
_As='cftIfTcpSackFackConnClosed'
_Ar='cftIfTcpRetxSackFackDataOctets'
_Aq='cftIfTcpRetxSackFackDataPkts'
_Ap='cftIfTcpTxSackFackDataOctets'
_Ao='cftIfTcpTxSackFackDataPkts'
_An='cftIfTcpSegDropByPAWS'
_Am='cftIfTcpRxWindowUpdatePkts'
_Al='cftIfTcpOctetAckedByRxAcks'
_Ak='cftIfTcpRxAcksPkts'
_Aj='cftIfTcpRxAcksForUnsentData'
_Ai='cftIfTcpRxDupAcks'
_Ah='cftIfTcpRxWindowProbesPkts'
_Ag='cftIfTcpRxPktsAfterConnClose'
_Af='cftIfTcpRxDataAfterWindowOctets'
_Ae='cftIfTcpRxDataAfterWindowPkts'
_Ad='cftIfTcpRxDupOctetsInPartDupPkts'
_Ac='cftIfTcpRxDupDataPkts'
_Ab='cftIfTcpRxDupOnlyOctets'
_Aa='cftIfTcpRxDupOnlyPkts'
_AZ='cftIfTcpRxTooShort'
_AY='cftIfTcpRxDroppedByNoMemory'
_AX='cftIfTcpTxControlPkts'
_AW='cftIfTcpTxWindowUpdateOnlyPkts'
_AV='cftIfTcpTxURGPkts'
_AU='cftIfTcpTxWindowProbes'
_AT='cftIfTcpAckOnlyPkts'
_AS='cftIfTcpConnDrainedByNoMemory'
_AR='cftIfTcpConnDroppedInPersist'
_AQ='cftIfTcpConnDroppedInKeepalive'
_AP='cftIfTcpKeepaliveProbesSent'
_AO='cftIfTcpKeepaliveTimeout'
_AN='cftIfTcpPersistTimeout'
_AM='cftIfTcpRetransmitTimeout'
_AL='cftIfTcpConnDroppedRxTimeout'
_AK='cftIfTcpDelayedAcksSent'
_AJ='cftIfTcpSegsSucceedToGetRTT'
_AI='cftIfTcpSegsTryToGetRTT'
_AH='cftIfTcpEmbryonicConnDrops'
_AG='cftIfTcpRxOutOfOrderOctets'
_AF='cftIfTcpRxOutOfOrderPkts'
_AE='cftIfTcpRxBadOffsetPkts'
_AD='cftIfTcpRxCcksumErrPkts'
_AC='cftIfTcpRxInSequenceOctets'
_AB='cftIfTcpRxInSequencePkts'
_AA='cftIfTcpRxPkts'
_A9='cftIfTcpRetxDataOctets'
_A8='cftIfTcpRetxDataPkts'
_A7='cftIfTcpTxDataOctets'
_A6='cftIfTcpTxDataPkts'
_A5='cftIfTcpTxPkts'
_A4='cftIfTcpConnClosed'
_A3='cftIfTcpConnDrops'
_A2='cftIfTcpConnEstablished'
_A1='cftIfTcpConnAccepted'
_A0='cftIfTcpConnInit'
_z='cftTcpTunnelDataTxDrops'
_y='cftTcpTunnelCmdTxDrops'
_x='cftTcpTunnelDataTxPkts'
_w='cftTcpTunnelCmdTxPkts'
_v='cftTcpTunnelDataTxOctets'
_u='cftTcpTunnelCmdTxOctets'
_t='cftTcpTunnelDataRxPoststufOctets'
_s='cftTcpTunnelCmdRxPoststufOctets'
_r='cftTcpTunnelDataRxPrestufOctets'
_q='cftTcpTunnelCmdRxPrestufOctets'
_p='cftTcpTunnelDataRxSegmentOctets'
_o='cftTcpTunnelCmdRxSegmentOctets'
_n='cftTcpTunnelStatus'
_m='cftTcpTunnelOperStatus'
_l='cftTcpTunnelDataConnectStatus'
_k='cftTcpTunnelCmdConnectStatus'
_j='cftTcpTunnelDataSelectiveAck'
_i='cftTcpTunnelCmdSelectiveAck'
_h='cftTcpTunnelDataKeepAliveTime'
_g='cftTcpTunnelCmdKeepAliveTime'
_f='cftTcpTunnelDataMWS'
_e='cftTcpTunnelCmdMWS'
_d='cftTcpTunnelDataDestPort'
_c='cftTcpTunnelDataSrcPort'
_b='cftTcpTunnelCmdDestPort'
_a='cftTcpTunnelCmdSrcPort'
_Z='cftTcpTunnelDestIp'
_Y='cftTcpTunnelDestIpType'
_X='cftTcpTunnelSrcIp'
_W='cftTcpTunnelSrcIpType'
_V='cftMaxTcpTunnels'
_U='notConnected'
_T='connected'
_S='seconds'
_R='ws512kbytes'
_Q='ws256kbytes'
_P='ws128kbytes'
_O='ws32kbytes'
_N='SnmpAdminString'
_M='cftIfTcpIndex'
_L='not-accessible'
_K='cftTcpTunnelName'
_J='cftFiberChannelIf'
_I='TruthValue'
_H='packets'
_G='Integer32'
_F='Unsigned32'
_E='bytes'
_D='read-create'
_C='read-only'
_B='CISCO-FC-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
ciscoFiberChannelTunnelMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9999))
if mibBuilder.loadTexts:ciscoFiberChannelTunnelMIB.setRevisions(('2002-03-08 17:00',))
_CiscoFCTunnelMIBNotifi_ObjectIdentity=ObjectIdentity
ciscoFCTunnelMIBNotifi=_CiscoFCTunnelMIBNotifi_ObjectIdentity((1,3,6,1,4,1,9,9,9999,0))
_CiscoFCTunnelMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFCTunnelMIBObjects=_CiscoFCTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1))
_CftTcpTunnelObjects_ObjectIdentity=ObjectIdentity
cftTcpTunnelObjects=_CftTcpTunnelObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1))
_CftMaxTcpTunnels_Type=Unsigned32
_CftMaxTcpTunnels_Object=MibScalar
cftMaxTcpTunnels=_CftMaxTcpTunnels_Object((1,3,6,1,4,1,9,9,9999,1,1,1),_CftMaxTcpTunnels_Type())
cftMaxTcpTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:cftMaxTcpTunnels.setStatus(_A)
_CftTcpTunnelTable_Object=MibTable
cftTcpTunnelTable=_CftTcpTunnelTable_Object((1,3,6,1,4,1,9,9,9999,1,1,2))
if mibBuilder.loadTexts:cftTcpTunnelTable.setStatus(_A)
_CftTcpTunnelEntry_Object=MibTableRow
cftTcpTunnelEntry=_CftTcpTunnelEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1))
cftTcpTunnelEntry.setIndexNames((0,_B,_J),(1,_B,_K))
if mibBuilder.loadTexts:cftTcpTunnelEntry.setStatus(_A)
_CftFiberChannelIf_Type=InterfaceIndex
_CftFiberChannelIf_Object=MibTableColumn
cftFiberChannelIf=_CftFiberChannelIf_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,1),_CftFiberChannelIf_Type())
cftFiberChannelIf.setMaxAccess(_L)
if mibBuilder.loadTexts:cftFiberChannelIf.setStatus(_A)
class _CftTcpTunnelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CftTcpTunnelName_Type.__name__=_N
_CftTcpTunnelName_Object=MibTableColumn
cftTcpTunnelName=_CftTcpTunnelName_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,2),_CftTcpTunnelName_Type())
cftTcpTunnelName.setMaxAccess(_L)
if mibBuilder.loadTexts:cftTcpTunnelName.setStatus(_A)
_CftTcpTunnelSrcIpType_Type=InetAddressType
_CftTcpTunnelSrcIpType_Object=MibTableColumn
cftTcpTunnelSrcIpType=_CftTcpTunnelSrcIpType_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,3),_CftTcpTunnelSrcIpType_Type())
cftTcpTunnelSrcIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelSrcIpType.setStatus(_A)
_CftTcpTunnelSrcIp_Type=InetAddress
_CftTcpTunnelSrcIp_Object=MibTableColumn
cftTcpTunnelSrcIp=_CftTcpTunnelSrcIp_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,4),_CftTcpTunnelSrcIp_Type())
cftTcpTunnelSrcIp.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelSrcIp.setStatus(_A)
_CftTcpTunnelDestIpType_Type=InetAddressType
_CftTcpTunnelDestIpType_Object=MibTableColumn
cftTcpTunnelDestIpType=_CftTcpTunnelDestIpType_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,5),_CftTcpTunnelDestIpType_Type())
cftTcpTunnelDestIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDestIpType.setStatus(_A)
_CftTcpTunnelDestIp_Type=InetAddress
_CftTcpTunnelDestIp_Object=MibTableColumn
cftTcpTunnelDestIp=_CftTcpTunnelDestIp_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,6),_CftTcpTunnelDestIp_Type())
cftTcpTunnelDestIp.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDestIp.setStatus(_A)
class _CftTcpTunnelCmdSrcPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_CftTcpTunnelCmdSrcPort_Type.__name__=_F
_CftTcpTunnelCmdSrcPort_Object=MibTableColumn
cftTcpTunnelCmdSrcPort=_CftTcpTunnelCmdSrcPort_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,7),_CftTcpTunnelCmdSrcPort_Type())
cftTcpTunnelCmdSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelCmdSrcPort.setStatus(_A)
class _CftTcpTunnelCmdDestPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_CftTcpTunnelCmdDestPort_Type.__name__=_F
_CftTcpTunnelCmdDestPort_Object=MibTableColumn
cftTcpTunnelCmdDestPort=_CftTcpTunnelCmdDestPort_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,8),_CftTcpTunnelCmdDestPort_Type())
cftTcpTunnelCmdDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelCmdDestPort.setStatus(_A)
class _CftTcpTunnelDataSrcPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_CftTcpTunnelDataSrcPort_Type.__name__=_F
_CftTcpTunnelDataSrcPort_Object=MibTableColumn
cftTcpTunnelDataSrcPort=_CftTcpTunnelDataSrcPort_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,9),_CftTcpTunnelDataSrcPort_Type())
cftTcpTunnelDataSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDataSrcPort.setStatus(_A)
class _CftTcpTunnelDataDestPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_CftTcpTunnelDataDestPort_Type.__name__=_F
_CftTcpTunnelDataDestPort_Object=MibTableColumn
cftTcpTunnelDataDestPort=_CftTcpTunnelDataDestPort_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,10),_CftTcpTunnelDataDestPort_Type())
cftTcpTunnelDataDestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDataDestPort.setStatus(_A)
class _CftTcpTunnelCmdMWS_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_CftTcpTunnelCmdMWS_Type.__name__=_G
_CftTcpTunnelCmdMWS_Object=MibTableColumn
cftTcpTunnelCmdMWS=_CftTcpTunnelCmdMWS_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,11),_CftTcpTunnelCmdMWS_Type())
cftTcpTunnelCmdMWS.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelCmdMWS.setStatus(_A)
class _CftTcpTunnelDataMWS_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_CftTcpTunnelDataMWS_Type.__name__=_G
_CftTcpTunnelDataMWS_Object=MibTableColumn
cftTcpTunnelDataMWS=_CftTcpTunnelDataMWS_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,12),_CftTcpTunnelDataMWS_Type())
cftTcpTunnelDataMWS.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDataMWS.setStatus(_A)
class _CftTcpTunnelCmdKeepAliveTime_Type(Unsigned32):defaultValue=7200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,10800))
_CftTcpTunnelCmdKeepAliveTime_Type.__name__=_F
_CftTcpTunnelCmdKeepAliveTime_Object=MibTableColumn
cftTcpTunnelCmdKeepAliveTime=_CftTcpTunnelCmdKeepAliveTime_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,13),_CftTcpTunnelCmdKeepAliveTime_Type())
cftTcpTunnelCmdKeepAliveTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelCmdKeepAliveTime.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdKeepAliveTime.setUnits(_S)
class _CftTcpTunnelDataKeepAliveTime_Type(Unsigned32):defaultValue=7200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,10800))
_CftTcpTunnelDataKeepAliveTime_Type.__name__=_F
_CftTcpTunnelDataKeepAliveTime_Object=MibTableColumn
cftTcpTunnelDataKeepAliveTime=_CftTcpTunnelDataKeepAliveTime_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,14),_CftTcpTunnelDataKeepAliveTime_Type())
cftTcpTunnelDataKeepAliveTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDataKeepAliveTime.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataKeepAliveTime.setUnits(_S)
class _CftTcpTunnelCmdSelectiveAck_Type(TruthValue):defaultValue=2
_CftTcpTunnelCmdSelectiveAck_Type.__name__=_I
_CftTcpTunnelCmdSelectiveAck_Object=MibTableColumn
cftTcpTunnelCmdSelectiveAck=_CftTcpTunnelCmdSelectiveAck_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,15),_CftTcpTunnelCmdSelectiveAck_Type())
cftTcpTunnelCmdSelectiveAck.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelCmdSelectiveAck.setStatus(_A)
class _CftTcpTunnelDataSelectiveAck_Type(TruthValue):defaultValue=1
_CftTcpTunnelDataSelectiveAck_Type.__name__=_I
_CftTcpTunnelDataSelectiveAck_Object=MibTableColumn
cftTcpTunnelDataSelectiveAck=_CftTcpTunnelDataSelectiveAck_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,16),_CftTcpTunnelDataSelectiveAck_Type())
cftTcpTunnelDataSelectiveAck.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelDataSelectiveAck.setStatus(_A)
class _CftTcpTunnelCmdConnectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CftTcpTunnelCmdConnectStatus_Type.__name__=_G
_CftTcpTunnelCmdConnectStatus_Object=MibTableColumn
cftTcpTunnelCmdConnectStatus=_CftTcpTunnelCmdConnectStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,17),_CftTcpTunnelCmdConnectStatus_Type())
cftTcpTunnelCmdConnectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdConnectStatus.setStatus(_A)
class _CftTcpTunnelDataConnectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CftTcpTunnelDataConnectStatus_Type.__name__=_G
_CftTcpTunnelDataConnectStatus_Object=MibTableColumn
cftTcpTunnelDataConnectStatus=_CftTcpTunnelDataConnectStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,18),_CftTcpTunnelDataConnectStatus_Type())
cftTcpTunnelDataConnectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataConnectStatus.setStatus(_A)
class _CftTcpTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CftTcpTunnelOperStatus_Type.__name__=_G
_CftTcpTunnelOperStatus_Object=MibTableColumn
cftTcpTunnelOperStatus=_CftTcpTunnelOperStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,19),_CftTcpTunnelOperStatus_Type())
cftTcpTunnelOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelOperStatus.setStatus(_A)
_CftTcpTunnelStatus_Type=RowStatus
_CftTcpTunnelStatus_Object=MibTableColumn
cftTcpTunnelStatus=_CftTcpTunnelStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,20),_CftTcpTunnelStatus_Type())
cftTcpTunnelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cftTcpTunnelStatus.setStatus(_A)
_CftTcpTunnelStatsTable_Object=MibTable
cftTcpTunnelStatsTable=_CftTcpTunnelStatsTable_Object((1,3,6,1,4,1,9,9,9999,1,1,3))
if mibBuilder.loadTexts:cftTcpTunnelStatsTable.setStatus(_A)
_CftTcpTunnelStatsEntry_Object=MibTableRow
cftTcpTunnelStatsEntry=_CftTcpTunnelStatsEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1))
cftTcpTunnelStatsEntry.setIndexNames((0,_B,_J),(1,_B,_K))
if mibBuilder.loadTexts:cftTcpTunnelStatsEntry.setStatus(_A)
_CftTcpTunnelCmdRxSegmentOctets_Type=Counter64
_CftTcpTunnelCmdRxSegmentOctets_Object=MibTableColumn
cftTcpTunnelCmdRxSegmentOctets=_CftTcpTunnelCmdRxSegmentOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,1),_CftTcpTunnelCmdRxSegmentOctets_Type())
cftTcpTunnelCmdRxSegmentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdRxSegmentOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdRxSegmentOctets.setUnits(_E)
_CftTcpTunnelDataRxSegmentOctets_Type=Counter64
_CftTcpTunnelDataRxSegmentOctets_Object=MibTableColumn
cftTcpTunnelDataRxSegmentOctets=_CftTcpTunnelDataRxSegmentOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,2),_CftTcpTunnelDataRxSegmentOctets_Type())
cftTcpTunnelDataRxSegmentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataRxSegmentOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataRxSegmentOctets.setUnits(_E)
_CftTcpTunnelCmdRxPrestufOctets_Type=Counter64
_CftTcpTunnelCmdRxPrestufOctets_Object=MibTableColumn
cftTcpTunnelCmdRxPrestufOctets=_CftTcpTunnelCmdRxPrestufOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,3),_CftTcpTunnelCmdRxPrestufOctets_Type())
cftTcpTunnelCmdRxPrestufOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdRxPrestufOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdRxPrestufOctets.setUnits(_E)
_CftTcpTunnelDataRxPrestufOctets_Type=Counter64
_CftTcpTunnelDataRxPrestufOctets_Object=MibTableColumn
cftTcpTunnelDataRxPrestufOctets=_CftTcpTunnelDataRxPrestufOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,4),_CftTcpTunnelDataRxPrestufOctets_Type())
cftTcpTunnelDataRxPrestufOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataRxPrestufOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataRxPrestufOctets.setUnits(_E)
_CftTcpTunnelCmdRxPoststufOctets_Type=Counter64
_CftTcpTunnelCmdRxPoststufOctets_Object=MibTableColumn
cftTcpTunnelCmdRxPoststufOctets=_CftTcpTunnelCmdRxPoststufOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,5),_CftTcpTunnelCmdRxPoststufOctets_Type())
cftTcpTunnelCmdRxPoststufOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdRxPoststufOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdRxPoststufOctets.setUnits(_E)
_CftTcpTunnelDataRxPoststufOctets_Type=Counter64
_CftTcpTunnelDataRxPoststufOctets_Object=MibTableColumn
cftTcpTunnelDataRxPoststufOctets=_CftTcpTunnelDataRxPoststufOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,6),_CftTcpTunnelDataRxPoststufOctets_Type())
cftTcpTunnelDataRxPoststufOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataRxPoststufOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataRxPoststufOctets.setUnits(_E)
_CftTcpTunnelCmdTxOctets_Type=Counter64
_CftTcpTunnelCmdTxOctets_Object=MibTableColumn
cftTcpTunnelCmdTxOctets=_CftTcpTunnelCmdTxOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,7),_CftTcpTunnelCmdTxOctets_Type())
cftTcpTunnelCmdTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdTxOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdTxOctets.setUnits(_E)
_CftTcpTunnelDataTxOctets_Type=Counter64
_CftTcpTunnelDataTxOctets_Object=MibTableColumn
cftTcpTunnelDataTxOctets=_CftTcpTunnelDataTxOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,8),_CftTcpTunnelDataTxOctets_Type())
cftTcpTunnelDataTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataTxOctets.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataTxOctets.setUnits(_E)
_CftTcpTunnelCmdTxPkts_Type=Counter32
_CftTcpTunnelCmdTxPkts_Object=MibTableColumn
cftTcpTunnelCmdTxPkts=_CftTcpTunnelCmdTxPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,9),_CftTcpTunnelCmdTxPkts_Type())
cftTcpTunnelCmdTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdTxPkts.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdTxPkts.setUnits(_H)
_CftTcpTunnelDataTxPkts_Type=Counter32
_CftTcpTunnelDataTxPkts_Object=MibTableColumn
cftTcpTunnelDataTxPkts=_CftTcpTunnelDataTxPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,10),_CftTcpTunnelDataTxPkts_Type())
cftTcpTunnelDataTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataTxPkts.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataTxPkts.setUnits(_H)
_CftTcpTunnelCmdTxDrops_Type=Counter32
_CftTcpTunnelCmdTxDrops_Object=MibTableColumn
cftTcpTunnelCmdTxDrops=_CftTcpTunnelCmdTxDrops_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,11),_CftTcpTunnelCmdTxDrops_Type())
cftTcpTunnelCmdTxDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelCmdTxDrops.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelCmdTxDrops.setUnits(_H)
_CftTcpTunnelDataTxDrops_Type=Counter32
_CftTcpTunnelDataTxDrops_Object=MibTableColumn
cftTcpTunnelDataTxDrops=_CftTcpTunnelDataTxDrops_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,12),_CftTcpTunnelDataTxDrops_Type())
cftTcpTunnelDataTxDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cftTcpTunnelDataTxDrops.setStatus(_A)
if mibBuilder.loadTexts:cftTcpTunnelDataTxDrops.setUnits(_H)
_CftIfTcpTable_Object=MibTable
cftIfTcpTable=_CftIfTcpTable_Object((1,3,6,1,4,1,9,9,9999,1,1,4))
if mibBuilder.loadTexts:cftIfTcpTable.setStatus(_A)
_CftIfTcpEntry_Object=MibTableRow
cftIfTcpEntry=_CftIfTcpEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1))
cftIfTcpEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cftIfTcpEntry.setStatus(_A)
_CftIfTcpIndex_Type=InterfaceIndex
_CftIfTcpIndex_Object=MibTableColumn
cftIfTcpIndex=_CftIfTcpIndex_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,1),_CftIfTcpIndex_Type())
cftIfTcpIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cftIfTcpIndex.setStatus(_A)
_CftIfTcpConnInit_Type=Counter32
_CftIfTcpConnInit_Object=MibTableColumn
cftIfTcpConnInit=_CftIfTcpConnInit_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,2),_CftIfTcpConnInit_Type())
cftIfTcpConnInit.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnInit.setStatus(_A)
_CftIfTcpConnAccepted_Type=Counter32
_CftIfTcpConnAccepted_Object=MibTableColumn
cftIfTcpConnAccepted=_CftIfTcpConnAccepted_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,3),_CftIfTcpConnAccepted_Type())
cftIfTcpConnAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnAccepted.setStatus(_A)
_CftIfTcpConnEstablished_Type=Counter32
_CftIfTcpConnEstablished_Object=MibTableColumn
cftIfTcpConnEstablished=_CftIfTcpConnEstablished_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,4),_CftIfTcpConnEstablished_Type())
cftIfTcpConnEstablished.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnEstablished.setStatus(_A)
_CftIfTcpConnDrops_Type=Counter32
_CftIfTcpConnDrops_Object=MibTableColumn
cftIfTcpConnDrops=_CftIfTcpConnDrops_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,5),_CftIfTcpConnDrops_Type())
cftIfTcpConnDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnDrops.setStatus(_A)
_CftIfTcpConnClosed_Type=Counter32
_CftIfTcpConnClosed_Object=MibTableColumn
cftIfTcpConnClosed=_CftIfTcpConnClosed_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,6),_CftIfTcpConnClosed_Type())
cftIfTcpConnClosed.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnClosed.setStatus(_A)
_CftIfTcpTxPkts_Type=Counter32
_CftIfTcpTxPkts_Object=MibTableColumn
cftIfTcpTxPkts=_CftIfTcpTxPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,7),_CftIfTcpTxPkts_Type())
cftIfTcpTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxPkts.setStatus(_A)
_CftIfTcpTxDataPkts_Type=Counter32
_CftIfTcpTxDataPkts_Object=MibTableColumn
cftIfTcpTxDataPkts=_CftIfTcpTxDataPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,8),_CftIfTcpTxDataPkts_Type())
cftIfTcpTxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxDataPkts.setStatus(_A)
_CftIfTcpTxDataOctets_Type=Counter32
_CftIfTcpTxDataOctets_Object=MibTableColumn
cftIfTcpTxDataOctets=_CftIfTcpTxDataOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,9),_CftIfTcpTxDataOctets_Type())
cftIfTcpTxDataOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxDataOctets.setStatus(_A)
_CftIfTcpRetxDataPkts_Type=Counter32
_CftIfTcpRetxDataPkts_Object=MibTableColumn
cftIfTcpRetxDataPkts=_CftIfTcpRetxDataPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,10),_CftIfTcpRetxDataPkts_Type())
cftIfTcpRetxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRetxDataPkts.setStatus(_A)
_CftIfTcpRetxDataOctets_Type=Counter32
_CftIfTcpRetxDataOctets_Object=MibTableColumn
cftIfTcpRetxDataOctets=_CftIfTcpRetxDataOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,11),_CftIfTcpRetxDataOctets_Type())
cftIfTcpRetxDataOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRetxDataOctets.setStatus(_A)
_CftIfTcpRxPkts_Type=Counter32
_CftIfTcpRxPkts_Object=MibTableColumn
cftIfTcpRxPkts=_CftIfTcpRxPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,12),_CftIfTcpRxPkts_Type())
cftIfTcpRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxPkts.setStatus(_A)
_CftIfTcpRxInSequencePkts_Type=Counter32
_CftIfTcpRxInSequencePkts_Object=MibTableColumn
cftIfTcpRxInSequencePkts=_CftIfTcpRxInSequencePkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,13),_CftIfTcpRxInSequencePkts_Type())
cftIfTcpRxInSequencePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxInSequencePkts.setStatus(_A)
_CftIfTcpRxInSequenceOctets_Type=Counter32
_CftIfTcpRxInSequenceOctets_Object=MibTableColumn
cftIfTcpRxInSequenceOctets=_CftIfTcpRxInSequenceOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,14),_CftIfTcpRxInSequenceOctets_Type())
cftIfTcpRxInSequenceOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxInSequenceOctets.setStatus(_A)
_CftIfTcpRxCcksumErrPkts_Type=Counter32
_CftIfTcpRxCcksumErrPkts_Object=MibTableColumn
cftIfTcpRxCcksumErrPkts=_CftIfTcpRxCcksumErrPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,15),_CftIfTcpRxCcksumErrPkts_Type())
cftIfTcpRxCcksumErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxCcksumErrPkts.setStatus(_A)
_CftIfTcpRxBadOffsetPkts_Type=Counter32
_CftIfTcpRxBadOffsetPkts_Object=MibTableColumn
cftIfTcpRxBadOffsetPkts=_CftIfTcpRxBadOffsetPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,16),_CftIfTcpRxBadOffsetPkts_Type())
cftIfTcpRxBadOffsetPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxBadOffsetPkts.setStatus(_A)
_CftIfTcpRxOutOfOrderPkts_Type=Counter32
_CftIfTcpRxOutOfOrderPkts_Object=MibTableColumn
cftIfTcpRxOutOfOrderPkts=_CftIfTcpRxOutOfOrderPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,17),_CftIfTcpRxOutOfOrderPkts_Type())
cftIfTcpRxOutOfOrderPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxOutOfOrderPkts.setStatus(_A)
_CftIfTcpRxOutOfOrderOctets_Type=Counter32
_CftIfTcpRxOutOfOrderOctets_Object=MibTableColumn
cftIfTcpRxOutOfOrderOctets=_CftIfTcpRxOutOfOrderOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,18),_CftIfTcpRxOutOfOrderOctets_Type())
cftIfTcpRxOutOfOrderOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxOutOfOrderOctets.setStatus(_A)
_CftIfTcpExtTable_Object=MibTable
cftIfTcpExtTable=_CftIfTcpExtTable_Object((1,3,6,1,4,1,9,9,9999,1,1,5))
if mibBuilder.loadTexts:cftIfTcpExtTable.setStatus(_A)
_CftIfTcpExtEntry_Object=MibTableRow
cftIfTcpExtEntry=_CftIfTcpExtEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1))
cftIfTcpExtEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cftIfTcpExtEntry.setStatus(_A)
_CftIfTcpEmbryonicConnDrops_Type=Counter32
_CftIfTcpEmbryonicConnDrops_Object=MibTableColumn
cftIfTcpEmbryonicConnDrops=_CftIfTcpEmbryonicConnDrops_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,1),_CftIfTcpEmbryonicConnDrops_Type())
cftIfTcpEmbryonicConnDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpEmbryonicConnDrops.setStatus(_A)
_CftIfTcpSegsTryToGetRTT_Type=Counter32
_CftIfTcpSegsTryToGetRTT_Object=MibTableColumn
cftIfTcpSegsTryToGetRTT=_CftIfTcpSegsTryToGetRTT_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,2),_CftIfTcpSegsTryToGetRTT_Type())
cftIfTcpSegsTryToGetRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpSegsTryToGetRTT.setStatus(_A)
_CftIfTcpSegsSucceedToGetRTT_Type=Counter32
_CftIfTcpSegsSucceedToGetRTT_Object=MibTableColumn
cftIfTcpSegsSucceedToGetRTT=_CftIfTcpSegsSucceedToGetRTT_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,3),_CftIfTcpSegsSucceedToGetRTT_Type())
cftIfTcpSegsSucceedToGetRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpSegsSucceedToGetRTT.setStatus(_A)
_CftIfTcpDelayedAcksSent_Type=Counter32
_CftIfTcpDelayedAcksSent_Object=MibTableColumn
cftIfTcpDelayedAcksSent=_CftIfTcpDelayedAcksSent_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,4),_CftIfTcpDelayedAcksSent_Type())
cftIfTcpDelayedAcksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpDelayedAcksSent.setStatus(_A)
_CftIfTcpConnDroppedRxTimeout_Type=Counter32
_CftIfTcpConnDroppedRxTimeout_Object=MibTableColumn
cftIfTcpConnDroppedRxTimeout=_CftIfTcpConnDroppedRxTimeout_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,5),_CftIfTcpConnDroppedRxTimeout_Type())
cftIfTcpConnDroppedRxTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnDroppedRxTimeout.setStatus(_A)
_CftIfTcpRetransmitTimeout_Type=Counter32
_CftIfTcpRetransmitTimeout_Object=MibTableColumn
cftIfTcpRetransmitTimeout=_CftIfTcpRetransmitTimeout_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,6),_CftIfTcpRetransmitTimeout_Type())
cftIfTcpRetransmitTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRetransmitTimeout.setStatus(_A)
_CftIfTcpPersistTimeout_Type=Counter32
_CftIfTcpPersistTimeout_Object=MibTableColumn
cftIfTcpPersistTimeout=_CftIfTcpPersistTimeout_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,7),_CftIfTcpPersistTimeout_Type())
cftIfTcpPersistTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpPersistTimeout.setStatus(_A)
_CftIfTcpKeepaliveTimeout_Type=Counter32
_CftIfTcpKeepaliveTimeout_Object=MibTableColumn
cftIfTcpKeepaliveTimeout=_CftIfTcpKeepaliveTimeout_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,8),_CftIfTcpKeepaliveTimeout_Type())
cftIfTcpKeepaliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpKeepaliveTimeout.setStatus(_A)
_CftIfTcpKeepaliveProbesSent_Type=Counter32
_CftIfTcpKeepaliveProbesSent_Object=MibTableColumn
cftIfTcpKeepaliveProbesSent=_CftIfTcpKeepaliveProbesSent_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,9),_CftIfTcpKeepaliveProbesSent_Type())
cftIfTcpKeepaliveProbesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpKeepaliveProbesSent.setStatus(_A)
_CftIfTcpConnDroppedInKeepalive_Type=Counter32
_CftIfTcpConnDroppedInKeepalive_Object=MibTableColumn
cftIfTcpConnDroppedInKeepalive=_CftIfTcpConnDroppedInKeepalive_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,10),_CftIfTcpConnDroppedInKeepalive_Type())
cftIfTcpConnDroppedInKeepalive.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnDroppedInKeepalive.setStatus(_A)
_CftIfTcpConnDroppedInPersist_Type=Counter32
_CftIfTcpConnDroppedInPersist_Object=MibTableColumn
cftIfTcpConnDroppedInPersist=_CftIfTcpConnDroppedInPersist_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,11),_CftIfTcpConnDroppedInPersist_Type())
cftIfTcpConnDroppedInPersist.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnDroppedInPersist.setStatus(_A)
_CftIfTcpConnDrainedByNoMemory_Type=Counter32
_CftIfTcpConnDrainedByNoMemory_Object=MibTableColumn
cftIfTcpConnDrainedByNoMemory=_CftIfTcpConnDrainedByNoMemory_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,12),_CftIfTcpConnDrainedByNoMemory_Type())
cftIfTcpConnDrainedByNoMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpConnDrainedByNoMemory.setStatus(_A)
_CftIfTcpAckOnlyPkts_Type=Counter32
_CftIfTcpAckOnlyPkts_Object=MibTableColumn
cftIfTcpAckOnlyPkts=_CftIfTcpAckOnlyPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,13),_CftIfTcpAckOnlyPkts_Type())
cftIfTcpAckOnlyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpAckOnlyPkts.setStatus(_A)
_CftIfTcpTxWindowProbes_Type=Counter32
_CftIfTcpTxWindowProbes_Object=MibTableColumn
cftIfTcpTxWindowProbes=_CftIfTcpTxWindowProbes_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,14),_CftIfTcpTxWindowProbes_Type())
cftIfTcpTxWindowProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxWindowProbes.setStatus(_A)
_CftIfTcpTxURGPkts_Type=Counter32
_CftIfTcpTxURGPkts_Object=MibTableColumn
cftIfTcpTxURGPkts=_CftIfTcpTxURGPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,15),_CftIfTcpTxURGPkts_Type())
cftIfTcpTxURGPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxURGPkts.setStatus(_A)
_CftIfTcpTxWindowUpdateOnlyPkts_Type=Counter32
_CftIfTcpTxWindowUpdateOnlyPkts_Object=MibTableColumn
cftIfTcpTxWindowUpdateOnlyPkts=_CftIfTcpTxWindowUpdateOnlyPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,16),_CftIfTcpTxWindowUpdateOnlyPkts_Type())
cftIfTcpTxWindowUpdateOnlyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxWindowUpdateOnlyPkts.setStatus(_A)
_CftIfTcpTxControlPkts_Type=Counter32
_CftIfTcpTxControlPkts_Object=MibTableColumn
cftIfTcpTxControlPkts=_CftIfTcpTxControlPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,17),_CftIfTcpTxControlPkts_Type())
cftIfTcpTxControlPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxControlPkts.setStatus(_A)
_CftIfTcpRxDroppedByNoMemory_Type=Counter32
_CftIfTcpRxDroppedByNoMemory_Object=MibTableColumn
cftIfTcpRxDroppedByNoMemory=_CftIfTcpRxDroppedByNoMemory_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,18),_CftIfTcpRxDroppedByNoMemory_Type())
cftIfTcpRxDroppedByNoMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDroppedByNoMemory.setStatus(_A)
_CftIfTcpRxTooShort_Type=Counter32
_CftIfTcpRxTooShort_Object=MibTableColumn
cftIfTcpRxTooShort=_CftIfTcpRxTooShort_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,19),_CftIfTcpRxTooShort_Type())
cftIfTcpRxTooShort.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxTooShort.setStatus(_A)
_CftIfTcpRxDupOnlyPkts_Type=Counter32
_CftIfTcpRxDupOnlyPkts_Object=MibTableColumn
cftIfTcpRxDupOnlyPkts=_CftIfTcpRxDupOnlyPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,20),_CftIfTcpRxDupOnlyPkts_Type())
cftIfTcpRxDupOnlyPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDupOnlyPkts.setStatus(_A)
_CftIfTcpRxDupOnlyOctets_Type=Counter32
_CftIfTcpRxDupOnlyOctets_Object=MibTableColumn
cftIfTcpRxDupOnlyOctets=_CftIfTcpRxDupOnlyOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,21),_CftIfTcpRxDupOnlyOctets_Type())
cftIfTcpRxDupOnlyOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDupOnlyOctets.setStatus(_A)
_CftIfTcpRxDupDataPkts_Type=Counter32
_CftIfTcpRxDupDataPkts_Object=MibTableColumn
cftIfTcpRxDupDataPkts=_CftIfTcpRxDupDataPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,22),_CftIfTcpRxDupDataPkts_Type())
cftIfTcpRxDupDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDupDataPkts.setStatus(_A)
_CftIfTcpRxDupOctetsInPartDupPkts_Type=Counter32
_CftIfTcpRxDupOctetsInPartDupPkts_Object=MibTableColumn
cftIfTcpRxDupOctetsInPartDupPkts=_CftIfTcpRxDupOctetsInPartDupPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,23),_CftIfTcpRxDupOctetsInPartDupPkts_Type())
cftIfTcpRxDupOctetsInPartDupPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDupOctetsInPartDupPkts.setStatus(_A)
_CftIfTcpRxDataAfterWindowPkts_Type=Counter32
_CftIfTcpRxDataAfterWindowPkts_Object=MibTableColumn
cftIfTcpRxDataAfterWindowPkts=_CftIfTcpRxDataAfterWindowPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,24),_CftIfTcpRxDataAfterWindowPkts_Type())
cftIfTcpRxDataAfterWindowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDataAfterWindowPkts.setStatus(_A)
_CftIfTcpRxDataAfterWindowOctets_Type=Counter32
_CftIfTcpRxDataAfterWindowOctets_Object=MibTableColumn
cftIfTcpRxDataAfterWindowOctets=_CftIfTcpRxDataAfterWindowOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,25),_CftIfTcpRxDataAfterWindowOctets_Type())
cftIfTcpRxDataAfterWindowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDataAfterWindowOctets.setStatus(_A)
_CftIfTcpRxPktsAfterConnClose_Type=Counter32
_CftIfTcpRxPktsAfterConnClose_Object=MibTableColumn
cftIfTcpRxPktsAfterConnClose=_CftIfTcpRxPktsAfterConnClose_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,26),_CftIfTcpRxPktsAfterConnClose_Type())
cftIfTcpRxPktsAfterConnClose.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxPktsAfterConnClose.setStatus(_A)
_CftIfTcpRxWindowProbesPkts_Type=Counter32
_CftIfTcpRxWindowProbesPkts_Object=MibTableColumn
cftIfTcpRxWindowProbesPkts=_CftIfTcpRxWindowProbesPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,27),_CftIfTcpRxWindowProbesPkts_Type())
cftIfTcpRxWindowProbesPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxWindowProbesPkts.setStatus(_A)
_CftIfTcpRxDupAcks_Type=Counter32
_CftIfTcpRxDupAcks_Object=MibTableColumn
cftIfTcpRxDupAcks=_CftIfTcpRxDupAcks_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,28),_CftIfTcpRxDupAcks_Type())
cftIfTcpRxDupAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxDupAcks.setStatus(_A)
_CftIfTcpRxAcksForUnsentData_Type=Counter32
_CftIfTcpRxAcksForUnsentData_Object=MibTableColumn
cftIfTcpRxAcksForUnsentData=_CftIfTcpRxAcksForUnsentData_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,29),_CftIfTcpRxAcksForUnsentData_Type())
cftIfTcpRxAcksForUnsentData.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxAcksForUnsentData.setStatus(_A)
_CftIfTcpRxAcksPkts_Type=Counter32
_CftIfTcpRxAcksPkts_Object=MibTableColumn
cftIfTcpRxAcksPkts=_CftIfTcpRxAcksPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,30),_CftIfTcpRxAcksPkts_Type())
cftIfTcpRxAcksPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxAcksPkts.setStatus(_A)
_CftIfTcpOctetAckedByRxAcks_Type=Counter32
_CftIfTcpOctetAckedByRxAcks_Object=MibTableColumn
cftIfTcpOctetAckedByRxAcks=_CftIfTcpOctetAckedByRxAcks_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,31),_CftIfTcpOctetAckedByRxAcks_Type())
cftIfTcpOctetAckedByRxAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpOctetAckedByRxAcks.setStatus(_A)
_CftIfTcpRxWindowUpdatePkts_Type=Counter32
_CftIfTcpRxWindowUpdatePkts_Object=MibTableColumn
cftIfTcpRxWindowUpdatePkts=_CftIfTcpRxWindowUpdatePkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,32),_CftIfTcpRxWindowUpdatePkts_Type())
cftIfTcpRxWindowUpdatePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRxWindowUpdatePkts.setStatus(_A)
_CftIfTcpSegDropByPAWS_Type=Counter32
_CftIfTcpSegDropByPAWS_Object=MibTableColumn
cftIfTcpSegDropByPAWS=_CftIfTcpSegDropByPAWS_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,33),_CftIfTcpSegDropByPAWS_Type())
cftIfTcpSegDropByPAWS.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpSegDropByPAWS.setStatus(_A)
_CftIfTcpTxSackFackDataPkts_Type=Counter32
_CftIfTcpTxSackFackDataPkts_Object=MibTableColumn
cftIfTcpTxSackFackDataPkts=_CftIfTcpTxSackFackDataPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,34),_CftIfTcpTxSackFackDataPkts_Type())
cftIfTcpTxSackFackDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxSackFackDataPkts.setStatus(_A)
_CftIfTcpTxSackFackDataOctets_Type=Counter32
_CftIfTcpTxSackFackDataOctets_Object=MibTableColumn
cftIfTcpTxSackFackDataOctets=_CftIfTcpTxSackFackDataOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,35),_CftIfTcpTxSackFackDataOctets_Type())
cftIfTcpTxSackFackDataOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpTxSackFackDataOctets.setStatus(_A)
_CftIfTcpRetxSackFackDataPkts_Type=Counter32
_CftIfTcpRetxSackFackDataPkts_Object=MibTableColumn
cftIfTcpRetxSackFackDataPkts=_CftIfTcpRetxSackFackDataPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,36),_CftIfTcpRetxSackFackDataPkts_Type())
cftIfTcpRetxSackFackDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRetxSackFackDataPkts.setStatus(_A)
_CftIfTcpRetxSackFackDataOctets_Type=Counter32
_CftIfTcpRetxSackFackDataOctets_Object=MibTableColumn
cftIfTcpRetxSackFackDataOctets=_CftIfTcpRetxSackFackDataOctets_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,37),_CftIfTcpRetxSackFackDataOctets_Type())
cftIfTcpRetxSackFackDataOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRetxSackFackDataOctets.setStatus(_A)
_CftIfTcpSackFackConnClosed_Type=Counter32
_CftIfTcpSackFackConnClosed_Object=MibTableColumn
cftIfTcpSackFackConnClosed=_CftIfTcpSackFackConnClosed_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,38),_CftIfTcpSackFackConnClosed_Type())
cftIfTcpSackFackConnClosed.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpSackFackConnClosed.setStatus(_A)
_CftIfTcpRetxSackFackTimeouts_Type=Counter32
_CftIfTcpRetxSackFackTimeouts_Object=MibTableColumn
cftIfTcpRetxSackFackTimeouts=_CftIfTcpRetxSackFackTimeouts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,39),_CftIfTcpRetxSackFackTimeouts_Type())
cftIfTcpRetxSackFackTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpRetxSackFackTimeouts.setStatus(_A)
_CftIfTcpHdrPredictOkForAcks_Type=Counter32
_CftIfTcpHdrPredictOkForAcks_Object=MibTableColumn
cftIfTcpHdrPredictOkForAcks=_CftIfTcpHdrPredictOkForAcks_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,40),_CftIfTcpHdrPredictOkForAcks_Type())
cftIfTcpHdrPredictOkForAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpHdrPredictOkForAcks.setStatus(_A)
_CftIfTcpHdrPredictOkForDataPkts_Type=Counter32
_CftIfTcpHdrPredictOkForDataPkts_Object=MibTableColumn
cftIfTcpHdrPredictOkForDataPkts=_CftIfTcpHdrPredictOkForDataPkts_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,41),_CftIfTcpHdrPredictOkForDataPkts_Type())
cftIfTcpHdrPredictOkForDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cftIfTcpHdrPredictOkForDataPkts.setStatus(_A)
_CiscoFCTunnelMIBConform_ObjectIdentity=ObjectIdentity
ciscoFCTunnelMIBConform=_CiscoFCTunnelMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2))
_CftTunnelMIBCompliances_ObjectIdentity=ObjectIdentity
cftTunnelMIBCompliances=_CftTunnelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,1))
_CftTunnelMIBGroups_ObjectIdentity=ObjectIdentity
cftTunnelMIBGroups=_CftTunnelMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,2))
cftTcpTunnelConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,1))
cftTcpTunnelConfigGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cftTcpTunnelConfigGroup.setStatus(_A)
cftTcpTunnelStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,2))
cftTcpTunnelStatGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:cftTcpTunnelStatGroup.setStatus(_A)
cftIfTcpGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,3))
cftIfTcpGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:cftIfTcpGroup.setStatus(_A)
cftIfTcpExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,4))
cftIfTcpExtGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:cftIfTcpExtGroup.setStatus(_A)
cftTunnelMIBComplianceV01=ModuleCompliance((1,3,6,1,4,1,9,9,9999,2,1,1))
cftTunnelMIBComplianceV01.setObjects((_B,_Aw))
if mibBuilder.loadTexts:cftTunnelMIBComplianceV01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFiberChannelTunnelMIB':ciscoFiberChannelTunnelMIB,'ciscoFCTunnelMIBNotifi':ciscoFCTunnelMIBNotifi,'ciscoFCTunnelMIBObjects':ciscoFCTunnelMIBObjects,'cftTcpTunnelObjects':cftTcpTunnelObjects,_V:cftMaxTcpTunnels,'cftTcpTunnelTable':cftTcpTunnelTable,'cftTcpTunnelEntry':cftTcpTunnelEntry,_J:cftFiberChannelIf,_K:cftTcpTunnelName,_W:cftTcpTunnelSrcIpType,_X:cftTcpTunnelSrcIp,_Y:cftTcpTunnelDestIpType,_Z:cftTcpTunnelDestIp,_a:cftTcpTunnelCmdSrcPort,_b:cftTcpTunnelCmdDestPort,_c:cftTcpTunnelDataSrcPort,_d:cftTcpTunnelDataDestPort,_e:cftTcpTunnelCmdMWS,_f:cftTcpTunnelDataMWS,_g:cftTcpTunnelCmdKeepAliveTime,_h:cftTcpTunnelDataKeepAliveTime,_i:cftTcpTunnelCmdSelectiveAck,_j:cftTcpTunnelDataSelectiveAck,_k:cftTcpTunnelCmdConnectStatus,_l:cftTcpTunnelDataConnectStatus,_m:cftTcpTunnelOperStatus,_n:cftTcpTunnelStatus,'cftTcpTunnelStatsTable':cftTcpTunnelStatsTable,'cftTcpTunnelStatsEntry':cftTcpTunnelStatsEntry,_o:cftTcpTunnelCmdRxSegmentOctets,_p:cftTcpTunnelDataRxSegmentOctets,_q:cftTcpTunnelCmdRxPrestufOctets,_r:cftTcpTunnelDataRxPrestufOctets,_s:cftTcpTunnelCmdRxPoststufOctets,_t:cftTcpTunnelDataRxPoststufOctets,_u:cftTcpTunnelCmdTxOctets,_v:cftTcpTunnelDataTxOctets,_w:cftTcpTunnelCmdTxPkts,_x:cftTcpTunnelDataTxPkts,_y:cftTcpTunnelCmdTxDrops,_z:cftTcpTunnelDataTxDrops,'cftIfTcpTable':cftIfTcpTable,'cftIfTcpEntry':cftIfTcpEntry,_M:cftIfTcpIndex,_A0:cftIfTcpConnInit,_A1:cftIfTcpConnAccepted,_A2:cftIfTcpConnEstablished,_A3:cftIfTcpConnDrops,_A4:cftIfTcpConnClosed,_A5:cftIfTcpTxPkts,_A6:cftIfTcpTxDataPkts,_A7:cftIfTcpTxDataOctets,_A8:cftIfTcpRetxDataPkts,_A9:cftIfTcpRetxDataOctets,_AA:cftIfTcpRxPkts,_AB:cftIfTcpRxInSequencePkts,_AC:cftIfTcpRxInSequenceOctets,_AD:cftIfTcpRxCcksumErrPkts,_AE:cftIfTcpRxBadOffsetPkts,_AF:cftIfTcpRxOutOfOrderPkts,_AG:cftIfTcpRxOutOfOrderOctets,'cftIfTcpExtTable':cftIfTcpExtTable,'cftIfTcpExtEntry':cftIfTcpExtEntry,_AH:cftIfTcpEmbryonicConnDrops,_AI:cftIfTcpSegsTryToGetRTT,_AJ:cftIfTcpSegsSucceedToGetRTT,_AK:cftIfTcpDelayedAcksSent,_AL:cftIfTcpConnDroppedRxTimeout,_AM:cftIfTcpRetransmitTimeout,_AN:cftIfTcpPersistTimeout,_AO:cftIfTcpKeepaliveTimeout,_AP:cftIfTcpKeepaliveProbesSent,_AQ:cftIfTcpConnDroppedInKeepalive,_AR:cftIfTcpConnDroppedInPersist,_AS:cftIfTcpConnDrainedByNoMemory,_AT:cftIfTcpAckOnlyPkts,_AU:cftIfTcpTxWindowProbes,_AV:cftIfTcpTxURGPkts,_AW:cftIfTcpTxWindowUpdateOnlyPkts,_AX:cftIfTcpTxControlPkts,_AY:cftIfTcpRxDroppedByNoMemory,_AZ:cftIfTcpRxTooShort,_Aa:cftIfTcpRxDupOnlyPkts,_Ab:cftIfTcpRxDupOnlyOctets,_Ac:cftIfTcpRxDupDataPkts,_Ad:cftIfTcpRxDupOctetsInPartDupPkts,_Ae:cftIfTcpRxDataAfterWindowPkts,_Af:cftIfTcpRxDataAfterWindowOctets,_Ag:cftIfTcpRxPktsAfterConnClose,_Ah:cftIfTcpRxWindowProbesPkts,_Ai:cftIfTcpRxDupAcks,_Aj:cftIfTcpRxAcksForUnsentData,_Ak:cftIfTcpRxAcksPkts,_Al:cftIfTcpOctetAckedByRxAcks,_Am:cftIfTcpRxWindowUpdatePkts,_An:cftIfTcpSegDropByPAWS,_Ao:cftIfTcpTxSackFackDataPkts,_Ap:cftIfTcpTxSackFackDataOctets,_Aq:cftIfTcpRetxSackFackDataPkts,_Ar:cftIfTcpRetxSackFackDataOctets,_As:cftIfTcpSackFackConnClosed,_At:cftIfTcpRetxSackFackTimeouts,_Au:cftIfTcpHdrPredictOkForAcks,_Av:cftIfTcpHdrPredictOkForDataPkts,'ciscoFCTunnelMIBConform':ciscoFCTunnelMIBConform,'cftTunnelMIBCompliances':cftTunnelMIBCompliances,'cftTunnelMIBComplianceV01':cftTunnelMIBComplianceV01,'cftTunnelMIBGroups':cftTunnelMIBGroups,_Aw:cftTcpTunnelConfigGroup,'cftTcpTunnelStatGroup':cftTcpTunnelStatGroup,'cftIfTcpGroup':cftIfTcpGroup,'cftIfTcpExtGroup':cftIfTcpExtGroup})