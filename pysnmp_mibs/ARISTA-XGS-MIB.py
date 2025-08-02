_AQ='aristaXgsCpuQueueStatsGroup'
_AP='aristaXgsIfGroup'
_AO='aristaXgsWatermarkGroup'
_AN='aristaXgsNexthopGroup'
_AM='aristaXgsMibGroup'
_AL='aristaXgsCpuQueueStatsRxPacketsDropped'
_AK='aristaXgsCpuQueueStatsRxBytesDropped'
_AJ='aristaXgsCpuQueueStatsRxPackets'
_AI='aristaXgsCpuQueueStatsRxBytes'
_AH='aristaXgsNexthopEcmpInUseSets'
_AG='aristaXgsNexthopEcmpInUseEntries'
_AF='aristaXgsNexthopEcmpMaxSets'
_AE='aristaXgsNexthopEcmpMaxEntries'
_AD='aristaXgsNexthopEcmpOverlayInUseSets'
_AC='aristaXgsNexthopEcmpUnderlayInUseSets'
_AB='aristaXgsNexthopEcmpOverlayMaxSets'
_AA='aristaXgsNexthopEcmpUnderlayMaxSets'
_A9='aristaXgsNexthopEcmpOverlayInUseEntries'
_A8='aristaXgsNexthopEcmpUnderlayInUseEntries'
_A7='aristaXgsNexthopEcmpOverlayMaxEntries'
_A6='aristaXgsNexthopEcmpUnderlayMaxEntries'
_A5='aristaXgsIfWredDropPktCounter'
_A4='deprecated'
_A3='aristaXgsCpuQueueStatsQueueIdentifier'
_A2='aristaXgsCpuQueueStatsForwardingElementIdentifier'
_A1='aristaXgsQueueWatermarkQueueId'
_A0='aristaXgsQueueWatermarkQueueType'
_z='Integer32'
_y='aristaXgsIfTxSplitHorizonDrop'
_x='aristaXgsIfWredNonEctDropPktCounter'
_w='aristaXgsIfWredEctDropPktCounter'
_v='aristaXgsIfEcnMarkedPackets'
_u='aristaXgsIfTxNetworkPortNonTrillDiscard'
_t='aristaXgsIfTxAccessPortTrillDiscard'
_s='aristaXgsIfRxNetworkPortNonTrillDiscard'
_r='aristaXgsIfRxAccessPortTrillDiscard'
_q='aristaXgsIfTxFcsError'
_p='aristaXgsIfRxIngressNfDrop'
_o='aristaXgsIfRxUc'
_n='aristaXgsIfIpV6L3Mcast'
_m='aristaXgsIfIpV6L3HeaderError'
_l='aristaXgsIfIpV6L3Ok'
_k='aristaXgsIfIpV6L3Discard'
_j='aristaXgsIfIpV4L3Mcast'
_i='aristaXgsIfIpV4L3HeaderError'
_h='aristaXgsIfIpV4L3Ok'
_g='aristaXgsIfIpV4L3Discard'
_f='aristaXgsIfTxPCError'
_e='aristaXgsIfTxMacError'
_d='aristaXgsIfRxL2MtuError'
_c='aristaXgsIfRxFpDrop'
_b='aristaXgsIfRxVlanDrop'
_a='aristaXgsIfRxUrpfDrop'
_Z='aristaXgsIfRxPolicyDiscard'
_Y='aristaXgsIfRxBufferPoolDiscard'
_X='aristaXgsIfRxTunnelError'
_W='aristaXgsIfRxMcDrop'
_V='aristaXgsIfNonCongestionDiscard'
_U='aristaXgsIfTxUnknownDrop'
_T='aristaXgsIfTxL2McDrop'
_S='aristaXgsIfTxVxltMiss'
_R='aristaXgsIfTxInvalidVlan'
_Q='aristaXgsIfTxTtlDrop'
_P='aristaXgsIfTxL3UcAgedDrop'
_O='aristaXgsIfTxL2MtuError'
_N='aristaXgsIfTxIpV6L3McOk'
_M='aristaXgsIfTxIpV4L3McOk'
_L='aristaXgsIfTxIpV6L3UcOk'
_K='aristaXgsIfTxIpV4L3UcOk'
_J='aristaXgsQueueWatermarkLastResetTime'
_I='aristaXgsQueueWatermarkCellSize'
_H='aristaXgsQueueWatermarkMaxCellsUsed'
_G='DisplayString'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='read-only'
_B='current'
_A='ARISTA-XGS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_z,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
aristaXgsMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,26))
if mibBuilder.loadTexts:aristaXgsMIB.setRevisions(('2020-08-10 00:00','2019-09-27 00:00','2019-01-03 00:00','2018-05-16 00:00'))
_AristaXgsMibConformance_ObjectIdentity=ObjectIdentity
aristaXgsMibConformance=_AristaXgsMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,26,1))
_AristaXgsMibCompliances_ObjectIdentity=ObjectIdentity
aristaXgsMibCompliances=_AristaXgsMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,26,1,1))
_AristaXgsMibGroups_ObjectIdentity=ObjectIdentity
aristaXgsMibGroups=_AristaXgsMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,26,1,2))
_AristaXgsQueueWatermarkTable_Object=MibTable
aristaXgsQueueWatermarkTable=_AristaXgsQueueWatermarkTable_Object((1,3,6,1,4,1,30065,3,26,2))
if mibBuilder.loadTexts:aristaXgsQueueWatermarkTable.setStatus(_B)
_AristaXgsQueueWatermarkEntry_Object=MibTableRow
aristaXgsQueueWatermarkEntry=_AristaXgsQueueWatermarkEntry_Object((1,3,6,1,4,1,30065,3,26,2,1))
aristaXgsQueueWatermarkEntry.setIndexNames((0,_E,_F),(0,_A,_A0),(0,_A,_A1))
if mibBuilder.loadTexts:aristaXgsQueueWatermarkEntry.setStatus(_B)
class _AristaXgsQueueWatermarkQueueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ingressHeadroomCells',1),('ingressSharedCells',2),('egressUnicastSharedCells',3),('egressMulticastSharedCells',4)))
_AristaXgsQueueWatermarkQueueType_Type.__name__=_z
_AristaXgsQueueWatermarkQueueType_Object=MibTableColumn
aristaXgsQueueWatermarkQueueType=_AristaXgsQueueWatermarkQueueType_Object((1,3,6,1,4,1,30065,3,26,2,1,1),_AristaXgsQueueWatermarkQueueType_Type())
aristaXgsQueueWatermarkQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXgsQueueWatermarkQueueType.setStatus(_B)
_AristaXgsQueueWatermarkQueueId_Type=Unsigned32
_AristaXgsQueueWatermarkQueueId_Object=MibTableColumn
aristaXgsQueueWatermarkQueueId=_AristaXgsQueueWatermarkQueueId_Object((1,3,6,1,4,1,30065,3,26,2,1,2),_AristaXgsQueueWatermarkQueueId_Type())
aristaXgsQueueWatermarkQueueId.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXgsQueueWatermarkQueueId.setStatus(_B)
_AristaXgsQueueWatermarkMaxCellsUsed_Type=Unsigned32
_AristaXgsQueueWatermarkMaxCellsUsed_Object=MibTableColumn
aristaXgsQueueWatermarkMaxCellsUsed=_AristaXgsQueueWatermarkMaxCellsUsed_Object((1,3,6,1,4,1,30065,3,26,2,1,3),_AristaXgsQueueWatermarkMaxCellsUsed_Type())
aristaXgsQueueWatermarkMaxCellsUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsQueueWatermarkMaxCellsUsed.setStatus(_B)
_AristaXgsQueueWatermarkCellSize_Type=Unsigned32
_AristaXgsQueueWatermarkCellSize_Object=MibTableColumn
aristaXgsQueueWatermarkCellSize=_AristaXgsQueueWatermarkCellSize_Object((1,3,6,1,4,1,30065,3,26,2,1,4),_AristaXgsQueueWatermarkCellSize_Type())
aristaXgsQueueWatermarkCellSize.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsQueueWatermarkCellSize.setStatus(_B)
_AristaXgsQueueWatermarkLastResetTime_Type=TimeTicks
_AristaXgsQueueWatermarkLastResetTime_Object=MibTableColumn
aristaXgsQueueWatermarkLastResetTime=_AristaXgsQueueWatermarkLastResetTime_Object((1,3,6,1,4,1,30065,3,26,2,1,5),_AristaXgsQueueWatermarkLastResetTime_Type())
aristaXgsQueueWatermarkLastResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsQueueWatermarkLastResetTime.setStatus(_B)
_AristaXgsIfTable_Object=MibTable
aristaXgsIfTable=_AristaXgsIfTable_Object((1,3,6,1,4,1,30065,3,26,3))
if mibBuilder.loadTexts:aristaXgsIfTable.setStatus(_B)
_AristaXgsIfEntry_Object=MibTableRow
aristaXgsIfEntry=_AristaXgsIfEntry_Object((1,3,6,1,4,1,30065,3,26,3,1))
aristaXgsIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aristaXgsIfEntry.setStatus(_B)
_AristaXgsIfTxIpV4L3UcOk_Type=Counter64
_AristaXgsIfTxIpV4L3UcOk_Object=MibTableColumn
aristaXgsIfTxIpV4L3UcOk=_AristaXgsIfTxIpV4L3UcOk_Object((1,3,6,1,4,1,30065,3,26,3,1,1),_AristaXgsIfTxIpV4L3UcOk_Type())
aristaXgsIfTxIpV4L3UcOk.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxIpV4L3UcOk.setStatus(_B)
_AristaXgsIfTxIpV6L3UcOk_Type=Counter64
_AristaXgsIfTxIpV6L3UcOk_Object=MibTableColumn
aristaXgsIfTxIpV6L3UcOk=_AristaXgsIfTxIpV6L3UcOk_Object((1,3,6,1,4,1,30065,3,26,3,1,2),_AristaXgsIfTxIpV6L3UcOk_Type())
aristaXgsIfTxIpV6L3UcOk.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxIpV6L3UcOk.setStatus(_B)
_AristaXgsIfTxIpV4L3McOk_Type=Counter64
_AristaXgsIfTxIpV4L3McOk_Object=MibTableColumn
aristaXgsIfTxIpV4L3McOk=_AristaXgsIfTxIpV4L3McOk_Object((1,3,6,1,4,1,30065,3,26,3,1,3),_AristaXgsIfTxIpV4L3McOk_Type())
aristaXgsIfTxIpV4L3McOk.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxIpV4L3McOk.setStatus(_B)
_AristaXgsIfTxIpV6L3McOk_Type=Counter64
_AristaXgsIfTxIpV6L3McOk_Object=MibTableColumn
aristaXgsIfTxIpV6L3McOk=_AristaXgsIfTxIpV6L3McOk_Object((1,3,6,1,4,1,30065,3,26,3,1,4),_AristaXgsIfTxIpV6L3McOk_Type())
aristaXgsIfTxIpV6L3McOk.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxIpV6L3McOk.setStatus(_B)
_AristaXgsIfTxL2MtuError_Type=Counter64
_AristaXgsIfTxL2MtuError_Object=MibTableColumn
aristaXgsIfTxL2MtuError=_AristaXgsIfTxL2MtuError_Object((1,3,6,1,4,1,30065,3,26,3,1,5),_AristaXgsIfTxL2MtuError_Type())
aristaXgsIfTxL2MtuError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxL2MtuError.setStatus(_B)
_AristaXgsIfTxL3UcAgedDrop_Type=Counter64
_AristaXgsIfTxL3UcAgedDrop_Object=MibTableColumn
aristaXgsIfTxL3UcAgedDrop=_AristaXgsIfTxL3UcAgedDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,6),_AristaXgsIfTxL3UcAgedDrop_Type())
aristaXgsIfTxL3UcAgedDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxL3UcAgedDrop.setStatus(_B)
_AristaXgsIfTxTtlDrop_Type=Counter64
_AristaXgsIfTxTtlDrop_Object=MibTableColumn
aristaXgsIfTxTtlDrop=_AristaXgsIfTxTtlDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,7),_AristaXgsIfTxTtlDrop_Type())
aristaXgsIfTxTtlDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxTtlDrop.setStatus(_B)
_AristaXgsIfTxInvalidVlan_Type=Counter64
_AristaXgsIfTxInvalidVlan_Object=MibTableColumn
aristaXgsIfTxInvalidVlan=_AristaXgsIfTxInvalidVlan_Object((1,3,6,1,4,1,30065,3,26,3,1,8),_AristaXgsIfTxInvalidVlan_Type())
aristaXgsIfTxInvalidVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxInvalidVlan.setStatus(_B)
_AristaXgsIfTxVxltMiss_Type=Counter64
_AristaXgsIfTxVxltMiss_Object=MibTableColumn
aristaXgsIfTxVxltMiss=_AristaXgsIfTxVxltMiss_Object((1,3,6,1,4,1,30065,3,26,3,1,9),_AristaXgsIfTxVxltMiss_Type())
aristaXgsIfTxVxltMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxVxltMiss.setStatus(_B)
_AristaXgsIfTxL2McDrop_Type=Counter64
_AristaXgsIfTxL2McDrop_Object=MibTableColumn
aristaXgsIfTxL2McDrop=_AristaXgsIfTxL2McDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,10),_AristaXgsIfTxL2McDrop_Type())
aristaXgsIfTxL2McDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxL2McDrop.setStatus(_B)
_AristaXgsIfTxUnknownDrop_Type=Counter64
_AristaXgsIfTxUnknownDrop_Object=MibTableColumn
aristaXgsIfTxUnknownDrop=_AristaXgsIfTxUnknownDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,11),_AristaXgsIfTxUnknownDrop_Type())
aristaXgsIfTxUnknownDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxUnknownDrop.setStatus(_B)
_AristaXgsIfNonCongestionDiscard_Type=Counter64
_AristaXgsIfNonCongestionDiscard_Object=MibTableColumn
aristaXgsIfNonCongestionDiscard=_AristaXgsIfNonCongestionDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,12),_AristaXgsIfNonCongestionDiscard_Type())
aristaXgsIfNonCongestionDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfNonCongestionDiscard.setStatus(_B)
_AristaXgsIfRxMcDrop_Type=Counter64
_AristaXgsIfRxMcDrop_Object=MibTableColumn
aristaXgsIfRxMcDrop=_AristaXgsIfRxMcDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,13),_AristaXgsIfRxMcDrop_Type())
aristaXgsIfRxMcDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxMcDrop.setStatus(_B)
_AristaXgsIfRxTunnelError_Type=Counter64
_AristaXgsIfRxTunnelError_Object=MibTableColumn
aristaXgsIfRxTunnelError=_AristaXgsIfRxTunnelError_Object((1,3,6,1,4,1,30065,3,26,3,1,14),_AristaXgsIfRxTunnelError_Type())
aristaXgsIfRxTunnelError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxTunnelError.setStatus(_B)
_AristaXgsIfRxBufferPoolDiscard_Type=Counter64
_AristaXgsIfRxBufferPoolDiscard_Object=MibTableColumn
aristaXgsIfRxBufferPoolDiscard=_AristaXgsIfRxBufferPoolDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,15),_AristaXgsIfRxBufferPoolDiscard_Type())
aristaXgsIfRxBufferPoolDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxBufferPoolDiscard.setStatus(_B)
_AristaXgsIfRxPolicyDiscard_Type=Counter64
_AristaXgsIfRxPolicyDiscard_Object=MibTableColumn
aristaXgsIfRxPolicyDiscard=_AristaXgsIfRxPolicyDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,16),_AristaXgsIfRxPolicyDiscard_Type())
aristaXgsIfRxPolicyDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxPolicyDiscard.setStatus(_B)
_AristaXgsIfRxUrpfDrop_Type=Counter64
_AristaXgsIfRxUrpfDrop_Object=MibTableColumn
aristaXgsIfRxUrpfDrop=_AristaXgsIfRxUrpfDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,17),_AristaXgsIfRxUrpfDrop_Type())
aristaXgsIfRxUrpfDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxUrpfDrop.setStatus(_B)
_AristaXgsIfRxVlanDrop_Type=Counter64
_AristaXgsIfRxVlanDrop_Object=MibTableColumn
aristaXgsIfRxVlanDrop=_AristaXgsIfRxVlanDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,18),_AristaXgsIfRxVlanDrop_Type())
aristaXgsIfRxVlanDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxVlanDrop.setStatus(_B)
_AristaXgsIfRxFpDrop_Type=Counter64
_AristaXgsIfRxFpDrop_Object=MibTableColumn
aristaXgsIfRxFpDrop=_AristaXgsIfRxFpDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,19),_AristaXgsIfRxFpDrop_Type())
aristaXgsIfRxFpDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxFpDrop.setStatus(_B)
_AristaXgsIfRxL2MtuError_Type=Counter64
_AristaXgsIfRxL2MtuError_Object=MibTableColumn
aristaXgsIfRxL2MtuError=_AristaXgsIfRxL2MtuError_Object((1,3,6,1,4,1,30065,3,26,3,1,20),_AristaXgsIfRxL2MtuError_Type())
aristaXgsIfRxL2MtuError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxL2MtuError.setStatus(_B)
_AristaXgsIfTxMacError_Type=Counter64
_AristaXgsIfTxMacError_Object=MibTableColumn
aristaXgsIfTxMacError=_AristaXgsIfTxMacError_Object((1,3,6,1,4,1,30065,3,26,3,1,21),_AristaXgsIfTxMacError_Type())
aristaXgsIfTxMacError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxMacError.setStatus(_B)
_AristaXgsIfTxPCError_Type=Counter64
_AristaXgsIfTxPCError_Object=MibTableColumn
aristaXgsIfTxPCError=_AristaXgsIfTxPCError_Object((1,3,6,1,4,1,30065,3,26,3,1,22),_AristaXgsIfTxPCError_Type())
aristaXgsIfTxPCError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxPCError.setStatus(_B)
_AristaXgsIfIpV4L3Discard_Type=Counter64
_AristaXgsIfIpV4L3Discard_Object=MibTableColumn
aristaXgsIfIpV4L3Discard=_AristaXgsIfIpV4L3Discard_Object((1,3,6,1,4,1,30065,3,26,3,1,23),_AristaXgsIfIpV4L3Discard_Type())
aristaXgsIfIpV4L3Discard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV4L3Discard.setStatus(_B)
_AristaXgsIfIpV4L3Ok_Type=Counter64
_AristaXgsIfIpV4L3Ok_Object=MibTableColumn
aristaXgsIfIpV4L3Ok=_AristaXgsIfIpV4L3Ok_Object((1,3,6,1,4,1,30065,3,26,3,1,24),_AristaXgsIfIpV4L3Ok_Type())
aristaXgsIfIpV4L3Ok.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV4L3Ok.setStatus(_B)
_AristaXgsIfIpV4L3HeaderError_Type=Counter64
_AristaXgsIfIpV4L3HeaderError_Object=MibTableColumn
aristaXgsIfIpV4L3HeaderError=_AristaXgsIfIpV4L3HeaderError_Object((1,3,6,1,4,1,30065,3,26,3,1,25),_AristaXgsIfIpV4L3HeaderError_Type())
aristaXgsIfIpV4L3HeaderError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV4L3HeaderError.setStatus(_B)
_AristaXgsIfIpV4L3Mcast_Type=Counter64
_AristaXgsIfIpV4L3Mcast_Object=MibTableColumn
aristaXgsIfIpV4L3Mcast=_AristaXgsIfIpV4L3Mcast_Object((1,3,6,1,4,1,30065,3,26,3,1,26),_AristaXgsIfIpV4L3Mcast_Type())
aristaXgsIfIpV4L3Mcast.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV4L3Mcast.setStatus(_B)
_AristaXgsIfIpV6L3Discard_Type=Counter64
_AristaXgsIfIpV6L3Discard_Object=MibTableColumn
aristaXgsIfIpV6L3Discard=_AristaXgsIfIpV6L3Discard_Object((1,3,6,1,4,1,30065,3,26,3,1,27),_AristaXgsIfIpV6L3Discard_Type())
aristaXgsIfIpV6L3Discard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV6L3Discard.setStatus(_B)
_AristaXgsIfIpV6L3Ok_Type=Counter64
_AristaXgsIfIpV6L3Ok_Object=MibTableColumn
aristaXgsIfIpV6L3Ok=_AristaXgsIfIpV6L3Ok_Object((1,3,6,1,4,1,30065,3,26,3,1,28),_AristaXgsIfIpV6L3Ok_Type())
aristaXgsIfIpV6L3Ok.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV6L3Ok.setStatus(_B)
_AristaXgsIfIpV6L3HeaderError_Type=Counter64
_AristaXgsIfIpV6L3HeaderError_Object=MibTableColumn
aristaXgsIfIpV6L3HeaderError=_AristaXgsIfIpV6L3HeaderError_Object((1,3,6,1,4,1,30065,3,26,3,1,29),_AristaXgsIfIpV6L3HeaderError_Type())
aristaXgsIfIpV6L3HeaderError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV6L3HeaderError.setStatus(_B)
_AristaXgsIfIpV6L3Mcast_Type=Counter64
_AristaXgsIfIpV6L3Mcast_Object=MibTableColumn
aristaXgsIfIpV6L3Mcast=_AristaXgsIfIpV6L3Mcast_Object((1,3,6,1,4,1,30065,3,26,3,1,30),_AristaXgsIfIpV6L3Mcast_Type())
aristaXgsIfIpV6L3Mcast.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfIpV6L3Mcast.setStatus(_B)
_AristaXgsIfRxUc_Type=Counter64
_AristaXgsIfRxUc_Object=MibTableColumn
aristaXgsIfRxUc=_AristaXgsIfRxUc_Object((1,3,6,1,4,1,30065,3,26,3,1,31),_AristaXgsIfRxUc_Type())
aristaXgsIfRxUc.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxUc.setStatus(_B)
_AristaXgsIfRxIngressNfDrop_Type=Counter64
_AristaXgsIfRxIngressNfDrop_Object=MibTableColumn
aristaXgsIfRxIngressNfDrop=_AristaXgsIfRxIngressNfDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,32),_AristaXgsIfRxIngressNfDrop_Type())
aristaXgsIfRxIngressNfDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxIngressNfDrop.setStatus(_B)
_AristaXgsIfTxFcsError_Type=Counter64
_AristaXgsIfTxFcsError_Object=MibTableColumn
aristaXgsIfTxFcsError=_AristaXgsIfTxFcsError_Object((1,3,6,1,4,1,30065,3,26,3,1,33),_AristaXgsIfTxFcsError_Type())
aristaXgsIfTxFcsError.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxFcsError.setStatus(_B)
_AristaXgsIfRxAccessPortTrillDiscard_Type=Counter64
_AristaXgsIfRxAccessPortTrillDiscard_Object=MibTableColumn
aristaXgsIfRxAccessPortTrillDiscard=_AristaXgsIfRxAccessPortTrillDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,34),_AristaXgsIfRxAccessPortTrillDiscard_Type())
aristaXgsIfRxAccessPortTrillDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxAccessPortTrillDiscard.setStatus(_B)
_AristaXgsIfRxNetworkPortNonTrillDiscard_Type=Counter64
_AristaXgsIfRxNetworkPortNonTrillDiscard_Object=MibTableColumn
aristaXgsIfRxNetworkPortNonTrillDiscard=_AristaXgsIfRxNetworkPortNonTrillDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,35),_AristaXgsIfRxNetworkPortNonTrillDiscard_Type())
aristaXgsIfRxNetworkPortNonTrillDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfRxNetworkPortNonTrillDiscard.setStatus(_B)
_AristaXgsIfTxAccessPortTrillDiscard_Type=Counter64
_AristaXgsIfTxAccessPortTrillDiscard_Object=MibTableColumn
aristaXgsIfTxAccessPortTrillDiscard=_AristaXgsIfTxAccessPortTrillDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,36),_AristaXgsIfTxAccessPortTrillDiscard_Type())
aristaXgsIfTxAccessPortTrillDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxAccessPortTrillDiscard.setStatus(_B)
_AristaXgsIfTxNetworkPortNonTrillDiscard_Type=Counter64
_AristaXgsIfTxNetworkPortNonTrillDiscard_Object=MibTableColumn
aristaXgsIfTxNetworkPortNonTrillDiscard=_AristaXgsIfTxNetworkPortNonTrillDiscard_Object((1,3,6,1,4,1,30065,3,26,3,1,37),_AristaXgsIfTxNetworkPortNonTrillDiscard_Type())
aristaXgsIfTxNetworkPortNonTrillDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxNetworkPortNonTrillDiscard.setStatus(_B)
_AristaXgsIfEcnMarkedPackets_Type=Counter64
_AristaXgsIfEcnMarkedPackets_Object=MibTableColumn
aristaXgsIfEcnMarkedPackets=_AristaXgsIfEcnMarkedPackets_Object((1,3,6,1,4,1,30065,3,26,3,1,38),_AristaXgsIfEcnMarkedPackets_Type())
aristaXgsIfEcnMarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfEcnMarkedPackets.setStatus(_B)
_AristaXgsIfWredEctDropPktCounter_Type=Counter64
_AristaXgsIfWredEctDropPktCounter_Object=MibTableColumn
aristaXgsIfWredEctDropPktCounter=_AristaXgsIfWredEctDropPktCounter_Object((1,3,6,1,4,1,30065,3,26,3,1,39),_AristaXgsIfWredEctDropPktCounter_Type())
aristaXgsIfWredEctDropPktCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfWredEctDropPktCounter.setStatus(_B)
_AristaXgsIfWredNonEctDropPktCounter_Type=Counter64
_AristaXgsIfWredNonEctDropPktCounter_Object=MibTableColumn
aristaXgsIfWredNonEctDropPktCounter=_AristaXgsIfWredNonEctDropPktCounter_Object((1,3,6,1,4,1,30065,3,26,3,1,40),_AristaXgsIfWredNonEctDropPktCounter_Type())
aristaXgsIfWredNonEctDropPktCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfWredNonEctDropPktCounter.setStatus(_B)
_AristaXgsIfTxSplitHorizonDrop_Type=Counter64
_AristaXgsIfTxSplitHorizonDrop_Object=MibTableColumn
aristaXgsIfTxSplitHorizonDrop=_AristaXgsIfTxSplitHorizonDrop_Object((1,3,6,1,4,1,30065,3,26,3,1,41),_AristaXgsIfTxSplitHorizonDrop_Type())
aristaXgsIfTxSplitHorizonDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfTxSplitHorizonDrop.setStatus(_B)
_AristaXgsIfWredDropPktCounter_Type=Counter64
_AristaXgsIfWredDropPktCounter_Object=MibTableColumn
aristaXgsIfWredDropPktCounter=_AristaXgsIfWredDropPktCounter_Object((1,3,6,1,4,1,30065,3,26,3,1,42),_AristaXgsIfWredDropPktCounter_Type())
aristaXgsIfWredDropPktCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsIfWredDropPktCounter.setStatus(_B)
_AristaXgsNexthopEcmpUnderlayMaxEntries_Type=Unsigned32
_AristaXgsNexthopEcmpUnderlayMaxEntries_Object=MibScalar
aristaXgsNexthopEcmpUnderlayMaxEntries=_AristaXgsNexthopEcmpUnderlayMaxEntries_Object((1,3,6,1,4,1,30065,3,26,4),_AristaXgsNexthopEcmpUnderlayMaxEntries_Type())
aristaXgsNexthopEcmpUnderlayMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpUnderlayMaxEntries.setStatus(_B)
_AristaXgsNexthopEcmpOverlayMaxEntries_Type=Unsigned32
_AristaXgsNexthopEcmpOverlayMaxEntries_Object=MibScalar
aristaXgsNexthopEcmpOverlayMaxEntries=_AristaXgsNexthopEcmpOverlayMaxEntries_Object((1,3,6,1,4,1,30065,3,26,5),_AristaXgsNexthopEcmpOverlayMaxEntries_Type())
aristaXgsNexthopEcmpOverlayMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpOverlayMaxEntries.setStatus(_B)
_AristaXgsNexthopEcmpUnderlayInUseEntries_Type=Unsigned32
_AristaXgsNexthopEcmpUnderlayInUseEntries_Object=MibScalar
aristaXgsNexthopEcmpUnderlayInUseEntries=_AristaXgsNexthopEcmpUnderlayInUseEntries_Object((1,3,6,1,4,1,30065,3,26,6),_AristaXgsNexthopEcmpUnderlayInUseEntries_Type())
aristaXgsNexthopEcmpUnderlayInUseEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpUnderlayInUseEntries.setStatus(_B)
_AristaXgsNexthopEcmpOverlayInUseEntries_Type=Unsigned32
_AristaXgsNexthopEcmpOverlayInUseEntries_Object=MibScalar
aristaXgsNexthopEcmpOverlayInUseEntries=_AristaXgsNexthopEcmpOverlayInUseEntries_Object((1,3,6,1,4,1,30065,3,26,7),_AristaXgsNexthopEcmpOverlayInUseEntries_Type())
aristaXgsNexthopEcmpOverlayInUseEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpOverlayInUseEntries.setStatus(_B)
_AristaXgsNexthopEcmpUnderlayMaxSets_Type=Unsigned32
_AristaXgsNexthopEcmpUnderlayMaxSets_Object=MibScalar
aristaXgsNexthopEcmpUnderlayMaxSets=_AristaXgsNexthopEcmpUnderlayMaxSets_Object((1,3,6,1,4,1,30065,3,26,8),_AristaXgsNexthopEcmpUnderlayMaxSets_Type())
aristaXgsNexthopEcmpUnderlayMaxSets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpUnderlayMaxSets.setStatus(_B)
_AristaXgsNexthopEcmpOverlayMaxSets_Type=Unsigned32
_AristaXgsNexthopEcmpOverlayMaxSets_Object=MibScalar
aristaXgsNexthopEcmpOverlayMaxSets=_AristaXgsNexthopEcmpOverlayMaxSets_Object((1,3,6,1,4,1,30065,3,26,9),_AristaXgsNexthopEcmpOverlayMaxSets_Type())
aristaXgsNexthopEcmpOverlayMaxSets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpOverlayMaxSets.setStatus(_B)
_AristaXgsNexthopEcmpUnderlayInUseSets_Type=Unsigned32
_AristaXgsNexthopEcmpUnderlayInUseSets_Object=MibScalar
aristaXgsNexthopEcmpUnderlayInUseSets=_AristaXgsNexthopEcmpUnderlayInUseSets_Object((1,3,6,1,4,1,30065,3,26,10),_AristaXgsNexthopEcmpUnderlayInUseSets_Type())
aristaXgsNexthopEcmpUnderlayInUseSets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpUnderlayInUseSets.setStatus(_B)
_AristaXgsNexthopEcmpOverlayInUseSets_Type=Unsigned32
_AristaXgsNexthopEcmpOverlayInUseSets_Object=MibScalar
aristaXgsNexthopEcmpOverlayInUseSets=_AristaXgsNexthopEcmpOverlayInUseSets_Object((1,3,6,1,4,1,30065,3,26,11),_AristaXgsNexthopEcmpOverlayInUseSets_Type())
aristaXgsNexthopEcmpOverlayInUseSets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpOverlayInUseSets.setStatus(_B)
_AristaXgsNexthopEcmpMaxEntries_Type=Unsigned32
_AristaXgsNexthopEcmpMaxEntries_Object=MibScalar
aristaXgsNexthopEcmpMaxEntries=_AristaXgsNexthopEcmpMaxEntries_Object((1,3,6,1,4,1,30065,3,26,12),_AristaXgsNexthopEcmpMaxEntries_Type())
aristaXgsNexthopEcmpMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpMaxEntries.setStatus(_B)
_AristaXgsNexthopEcmpMaxSets_Type=Unsigned32
_AristaXgsNexthopEcmpMaxSets_Object=MibScalar
aristaXgsNexthopEcmpMaxSets=_AristaXgsNexthopEcmpMaxSets_Object((1,3,6,1,4,1,30065,3,26,13),_AristaXgsNexthopEcmpMaxSets_Type())
aristaXgsNexthopEcmpMaxSets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpMaxSets.setStatus(_B)
_AristaXgsNexthopEcmpInUseEntries_Type=Unsigned32
_AristaXgsNexthopEcmpInUseEntries_Object=MibScalar
aristaXgsNexthopEcmpInUseEntries=_AristaXgsNexthopEcmpInUseEntries_Object((1,3,6,1,4,1,30065,3,26,14),_AristaXgsNexthopEcmpInUseEntries_Type())
aristaXgsNexthopEcmpInUseEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpInUseEntries.setStatus(_B)
_AristaXgsNexthopEcmpInUseSets_Type=Unsigned32
_AristaXgsNexthopEcmpInUseSets_Object=MibScalar
aristaXgsNexthopEcmpInUseSets=_AristaXgsNexthopEcmpInUseSets_Object((1,3,6,1,4,1,30065,3,26,15),_AristaXgsNexthopEcmpInUseSets_Type())
aristaXgsNexthopEcmpInUseSets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsNexthopEcmpInUseSets.setStatus(_B)
_AristaXgsCpuQueueStatsTable_Object=MibTable
aristaXgsCpuQueueStatsTable=_AristaXgsCpuQueueStatsTable_Object((1,3,6,1,4,1,30065,3,26,16))
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsTable.setStatus(_B)
_AristaXgsCpuQueueStatsEntry_Object=MibTableRow
aristaXgsCpuQueueStatsEntry=_AristaXgsCpuQueueStatsEntry_Object((1,3,6,1,4,1,30065,3,26,16,1))
aristaXgsCpuQueueStatsEntry.setIndexNames((0,_A,_A2),(0,_A,_A3))
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsEntry.setStatus(_B)
class _AristaXgsCpuQueueStatsForwardingElementIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AristaXgsCpuQueueStatsForwardingElementIdentifier_Type.__name__=_G
_AristaXgsCpuQueueStatsForwardingElementIdentifier_Object=MibTableColumn
aristaXgsCpuQueueStatsForwardingElementIdentifier=_AristaXgsCpuQueueStatsForwardingElementIdentifier_Object((1,3,6,1,4,1,30065,3,26,16,1,1),_AristaXgsCpuQueueStatsForwardingElementIdentifier_Type())
aristaXgsCpuQueueStatsForwardingElementIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsForwardingElementIdentifier.setStatus(_B)
class _AristaXgsCpuQueueStatsQueueIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AristaXgsCpuQueueStatsQueueIdentifier_Type.__name__=_G
_AristaXgsCpuQueueStatsQueueIdentifier_Object=MibTableColumn
aristaXgsCpuQueueStatsQueueIdentifier=_AristaXgsCpuQueueStatsQueueIdentifier_Object((1,3,6,1,4,1,30065,3,26,16,1,2),_AristaXgsCpuQueueStatsQueueIdentifier_Type())
aristaXgsCpuQueueStatsQueueIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsQueueIdentifier.setStatus(_B)
_AristaXgsCpuQueueStatsRxBytes_Type=Counter64
_AristaXgsCpuQueueStatsRxBytes_Object=MibTableColumn
aristaXgsCpuQueueStatsRxBytes=_AristaXgsCpuQueueStatsRxBytes_Object((1,3,6,1,4,1,30065,3,26,16,1,3),_AristaXgsCpuQueueStatsRxBytes_Type())
aristaXgsCpuQueueStatsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsRxBytes.setStatus(_B)
_AristaXgsCpuQueueStatsRxPackets_Type=Counter64
_AristaXgsCpuQueueStatsRxPackets_Object=MibTableColumn
aristaXgsCpuQueueStatsRxPackets=_AristaXgsCpuQueueStatsRxPackets_Object((1,3,6,1,4,1,30065,3,26,16,1,4),_AristaXgsCpuQueueStatsRxPackets_Type())
aristaXgsCpuQueueStatsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsRxPackets.setStatus(_B)
_AristaXgsCpuQueueStatsRxBytesDropped_Type=Counter64
_AristaXgsCpuQueueStatsRxBytesDropped_Object=MibTableColumn
aristaXgsCpuQueueStatsRxBytesDropped=_AristaXgsCpuQueueStatsRxBytesDropped_Object((1,3,6,1,4,1,30065,3,26,16,1,5),_AristaXgsCpuQueueStatsRxBytesDropped_Type())
aristaXgsCpuQueueStatsRxBytesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsRxBytesDropped.setStatus(_B)
_AristaXgsCpuQueueStatsRxPacketsDropped_Type=Counter64
_AristaXgsCpuQueueStatsRxPacketsDropped_Object=MibTableColumn
aristaXgsCpuQueueStatsRxPacketsDropped=_AristaXgsCpuQueueStatsRxPacketsDropped_Object((1,3,6,1,4,1,30065,3,26,16,1,6),_AristaXgsCpuQueueStatsRxPacketsDropped_Type())
aristaXgsCpuQueueStatsRxPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsRxPacketsDropped.setStatus(_B)
aristaXgsMibGroup=ObjectGroup((1,3,6,1,4,1,30065,3,26,1,2,1))
aristaXgsMibGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:aristaXgsMibGroup.setStatus(_A4)
aristaXgsWatermarkGroup=ObjectGroup((1,3,6,1,4,1,30065,3,26,1,2,2))
aristaXgsWatermarkGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:aristaXgsWatermarkGroup.setStatus(_B)
aristaXgsIfGroup=ObjectGroup((1,3,6,1,4,1,30065,3,26,1,2,3))
aristaXgsIfGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_A5)))
if mibBuilder.loadTexts:aristaXgsIfGroup.setStatus(_B)
aristaXgsNexthopGroup=ObjectGroup((1,3,6,1,4,1,30065,3,26,1,2,4))
aristaXgsNexthopGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:aristaXgsNexthopGroup.setStatus(_B)
aristaXgsCpuQueueStatsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,26,1,2,5))
aristaXgsCpuQueueStatsGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:aristaXgsCpuQueueStatsGroup.setStatus(_B)
aristaXgsMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,26,1,1,1))
aristaXgsMibCompliance.setObjects((_A,_AM))
if mibBuilder.loadTexts:aristaXgsMibCompliance.setStatus(_A4)
aristaXgsMibCompliance2=ModuleCompliance((1,3,6,1,4,1,30065,3,26,1,1,2))
aristaXgsMibCompliance2.setObjects(*((_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:aristaXgsMibCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'aristaXgsMIB':aristaXgsMIB,'aristaXgsMibConformance':aristaXgsMibConformance,'aristaXgsMibCompliances':aristaXgsMibCompliances,'aristaXgsMibCompliance':aristaXgsMibCompliance,'aristaXgsMibCompliance2':aristaXgsMibCompliance2,'aristaXgsMibGroups':aristaXgsMibGroups,_AM:aristaXgsMibGroup,_AO:aristaXgsWatermarkGroup,_AP:aristaXgsIfGroup,_AN:aristaXgsNexthopGroup,_AQ:aristaXgsCpuQueueStatsGroup,'aristaXgsQueueWatermarkTable':aristaXgsQueueWatermarkTable,'aristaXgsQueueWatermarkEntry':aristaXgsQueueWatermarkEntry,_A0:aristaXgsQueueWatermarkQueueType,_A1:aristaXgsQueueWatermarkQueueId,_H:aristaXgsQueueWatermarkMaxCellsUsed,_I:aristaXgsQueueWatermarkCellSize,_J:aristaXgsQueueWatermarkLastResetTime,'aristaXgsIfTable':aristaXgsIfTable,'aristaXgsIfEntry':aristaXgsIfEntry,_K:aristaXgsIfTxIpV4L3UcOk,_L:aristaXgsIfTxIpV6L3UcOk,_M:aristaXgsIfTxIpV4L3McOk,_N:aristaXgsIfTxIpV6L3McOk,_O:aristaXgsIfTxL2MtuError,_P:aristaXgsIfTxL3UcAgedDrop,_Q:aristaXgsIfTxTtlDrop,_R:aristaXgsIfTxInvalidVlan,_S:aristaXgsIfTxVxltMiss,_T:aristaXgsIfTxL2McDrop,_U:aristaXgsIfTxUnknownDrop,_V:aristaXgsIfNonCongestionDiscard,_W:aristaXgsIfRxMcDrop,_X:aristaXgsIfRxTunnelError,_Y:aristaXgsIfRxBufferPoolDiscard,_Z:aristaXgsIfRxPolicyDiscard,_a:aristaXgsIfRxUrpfDrop,_b:aristaXgsIfRxVlanDrop,_c:aristaXgsIfRxFpDrop,_d:aristaXgsIfRxL2MtuError,_e:aristaXgsIfTxMacError,_f:aristaXgsIfTxPCError,_g:aristaXgsIfIpV4L3Discard,_h:aristaXgsIfIpV4L3Ok,_i:aristaXgsIfIpV4L3HeaderError,_j:aristaXgsIfIpV4L3Mcast,_k:aristaXgsIfIpV6L3Discard,_l:aristaXgsIfIpV6L3Ok,_m:aristaXgsIfIpV6L3HeaderError,_n:aristaXgsIfIpV6L3Mcast,_o:aristaXgsIfRxUc,_p:aristaXgsIfRxIngressNfDrop,_q:aristaXgsIfTxFcsError,_r:aristaXgsIfRxAccessPortTrillDiscard,_s:aristaXgsIfRxNetworkPortNonTrillDiscard,_t:aristaXgsIfTxAccessPortTrillDiscard,_u:aristaXgsIfTxNetworkPortNonTrillDiscard,_v:aristaXgsIfEcnMarkedPackets,_w:aristaXgsIfWredEctDropPktCounter,_x:aristaXgsIfWredNonEctDropPktCounter,_y:aristaXgsIfTxSplitHorizonDrop,_A5:aristaXgsIfWredDropPktCounter,_A6:aristaXgsNexthopEcmpUnderlayMaxEntries,_A7:aristaXgsNexthopEcmpOverlayMaxEntries,_A8:aristaXgsNexthopEcmpUnderlayInUseEntries,_A9:aristaXgsNexthopEcmpOverlayInUseEntries,_AA:aristaXgsNexthopEcmpUnderlayMaxSets,_AB:aristaXgsNexthopEcmpOverlayMaxSets,_AC:aristaXgsNexthopEcmpUnderlayInUseSets,_AD:aristaXgsNexthopEcmpOverlayInUseSets,_AE:aristaXgsNexthopEcmpMaxEntries,_AF:aristaXgsNexthopEcmpMaxSets,_AG:aristaXgsNexthopEcmpInUseEntries,_AH:aristaXgsNexthopEcmpInUseSets,'aristaXgsCpuQueueStatsTable':aristaXgsCpuQueueStatsTable,'aristaXgsCpuQueueStatsEntry':aristaXgsCpuQueueStatsEntry,_A2:aristaXgsCpuQueueStatsForwardingElementIdentifier,_A3:aristaXgsCpuQueueStatsQueueIdentifier,_AI:aristaXgsCpuQueueStatsRxBytes,_AJ:aristaXgsCpuQueueStatsRxPackets,_AK:aristaXgsCpuQueueStatsRxBytesDropped,_AL:aristaXgsCpuQueueStatsRxPacketsDropped})