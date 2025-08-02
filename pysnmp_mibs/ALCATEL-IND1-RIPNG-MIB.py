_Ae='alaRipngRouteGroup'
_Ad='alaRipngPeerGroup'
_Ac='alaRipngRouteFilterGroup'
_Ab='alaRipngSummarizationGroup'
_Aa='alaRipngNexthopFilterGroup'
_AZ='alaRipngInterfaceGroup'
_AY='alaRipngDebugGroup'
_AX='alaRipngGlobalGroup'
_AW='ripngRouteMaxLimitReached'
_AV='alaRipngDebugSummary'
_AU='alaRipngDebugRouteFilter'
_AT='alaRipngDebugNexthopFilter'
_AS='alaRipngRouteIndex'
_AR='alaRipngRouteFlags'
_AQ='alaRipngRouteStatus'
_AP='alaRipngRouteMetric'
_AO='alaRipngRouteTag'
_AN='alaRipngRouteAge'
_AM='alaRipngRouteType'
_AL='alaRipngPeerBadRoutes'
_AK='alaRipngPeerBadPackets'
_AJ='alaRipngPeerNumRoutes'
_AI='alaRipngPeerNumUpdates'
_AH='alaRipngPeerLastUpdate'
_AG='alaRipngRouteFilterSubnets'
_AF='alaRipngRouteFilterStatus'
_AE='alaRipngSummarizationSubnets'
_AD='alaRipngSummarizationStatus'
_AC='alaRipngNexthopFilterStatus'
_AB='alaRipngInterfaceJitter'
_AA='alaRipngInterfaceNextUpdate'
_A9='alaRipngInterfaceMTU'
_A8='alaRipngInterfacePacketsRcvd'
_A7='alaRipngInterfacePacketsSent'
_A6='alaRipngInterfaceHorizon'
_A5='alaRipngInterfaceSendStatus'
_A4='alaRipngInterfaceRecvStatus'
_A3='alaRipngInterfaceMetric'
_A2='alaRipngInterfaceStatus'
_A1='alaRipngDebugAll'
_A0='alaRipngDebugTm'
_z='alaRipngDebugTime'
_y='alaRipngDebugSetup'
_x='alaRipngDebugInfo'
_w='alaRipngDebugMip'
_v='alaRipngDebugAge'
_u='alaRipngDebugRdb'
_t='alaRipngDebugSend'
_s='alaRipngDebugRecv'
_r='alaRipngDebugWarn'
_q='alaRipngDebugError'
_p='alaRipngDebugLevel'
_o='alaRipngPort'
_n='alaRipngJitter'
_m='alaRipngTriggeredSends'
_l='alaRipngGlobalRouteTag'
_k='alaRipngRouteCount'
_j='alaRipngGarbageTimer'
_i='alaRipngHolddownTimer'
_h='alaRipngInvalidTimer'
_g='alaRipngUpdateInterval'
_f='alaRipngProtoStatus'
_e='unknown'
_d='alaRipngRouteNextHop'
_c='alaRipngRoutePrefixLen'
_b='alaRipngRoutePrefix'
_a='alaRipngPeerIndex'
_Z='alaRipngPeerAddress'
_Y='donotinclude'
_X='include'
_W='disabled'
_V='enabled'
_U='alaRipngInterfaceIndex'
_T='alaRipngRouteFilterDirection'
_S='alaRipngRouteFilterPrefixLen'
_R='alaRipngRouteFilterPrefix'
_Q='alaRipngSummarizationPrefixLen'
_P='alaRipngSummarizationPrefix'
_O='alaRipngSummarizationSourcePrefixLen'
_N='alaRipngSummarizationSourcePrefix'
_M='alaRipngNexthopFilterAddress'
_L='seconds'
_K='RowStatus'
_J='not-accessible'
_I='read-create'
_H='disable'
_G='enable'
_F='read-only'
_E='read-write'
_D='deprecated'
_C='Integer32'
_B='current'
_A='ALCATEL-IND1-RIPNG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ripng,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','routingIND1Ripng')
Ipv6Address,Ipv6AddressPrefix=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressPrefix')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_K,'TextualConvention')
alcatelIND1RIPNGMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1RIPNGMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBObjects=_AlcatelIND1RIPNGMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBObjects.setStatus(_B)
_AlaProtocolRipng_ObjectIdentity=ObjectIdentity
alaProtocolRipng=_AlaProtocolRipng_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1))
class _AlaRipngProtoStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngProtoStatus_Type.__name__=_C
_AlaRipngProtoStatus_Object=MibScalar
alaRipngProtoStatus=_AlaRipngProtoStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,1),_AlaRipngProtoStatus_Type())
alaRipngProtoStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngProtoStatus.setStatus(_B)
class _AlaRipngUpdateInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_AlaRipngUpdateInterval_Type.__name__=_C
_AlaRipngUpdateInterval_Object=MibScalar
alaRipngUpdateInterval=_AlaRipngUpdateInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,2),_AlaRipngUpdateInterval_Type())
alaRipngUpdateInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngUpdateInterval.setStatus(_B)
if mibBuilder.loadTexts:alaRipngUpdateInterval.setUnits(_L)
class _AlaRipngInvalidTimer_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,360))
_AlaRipngInvalidTimer_Type.__name__=_C
_AlaRipngInvalidTimer_Object=MibScalar
alaRipngInvalidTimer=_AlaRipngInvalidTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,3),_AlaRipngInvalidTimer_Type())
alaRipngInvalidTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngInvalidTimer.setStatus(_B)
if mibBuilder.loadTexts:alaRipngInvalidTimer.setUnits(_L)
class _AlaRipngHolddownTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_AlaRipngHolddownTimer_Type.__name__=_C
_AlaRipngHolddownTimer_Object=MibScalar
alaRipngHolddownTimer=_AlaRipngHolddownTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,4),_AlaRipngHolddownTimer_Type())
alaRipngHolddownTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngHolddownTimer.setStatus(_B)
class _AlaRipngGarbageTimer_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_AlaRipngGarbageTimer_Type.__name__=_C
_AlaRipngGarbageTimer_Object=MibScalar
alaRipngGarbageTimer=_AlaRipngGarbageTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,5),_AlaRipngGarbageTimer_Type())
alaRipngGarbageTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngGarbageTimer.setStatus(_B)
class _AlaRipngRouteCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaRipngRouteCount_Type.__name__=_C
_AlaRipngRouteCount_Object=MibScalar
alaRipngRouteCount=_AlaRipngRouteCount_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,6),_AlaRipngRouteCount_Type())
alaRipngRouteCount.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteCount.setStatus(_B)
class _AlaRipngGlobalRouteTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaRipngGlobalRouteTag_Type.__name__=_C
_AlaRipngGlobalRouteTag_Object=MibScalar
alaRipngGlobalRouteTag=_AlaRipngGlobalRouteTag_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,7),_AlaRipngGlobalRouteTag_Type())
alaRipngGlobalRouteTag.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngGlobalRouteTag.setStatus(_B)
class _AlaRipngTriggeredSends_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('onlyupdated',2),('off',3)))
_AlaRipngTriggeredSends_Type.__name__=_C
_AlaRipngTriggeredSends_Object=MibScalar
alaRipngTriggeredSends=_AlaRipngTriggeredSends_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,8),_AlaRipngTriggeredSends_Type())
alaRipngTriggeredSends.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngTriggeredSends.setStatus(_B)
class _AlaRipngJitter_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AlaRipngJitter_Type.__name__=_C
_AlaRipngJitter_Object=MibScalar
alaRipngJitter=_AlaRipngJitter_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,9),_AlaRipngJitter_Type())
alaRipngJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngJitter.setStatus(_B)
if mibBuilder.loadTexts:alaRipngJitter.setUnits(_L)
class _AlaRipngPort_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaRipngPort_Type.__name__=_C
_AlaRipngPort_Object=MibScalar
alaRipngPort=_AlaRipngPort_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,10),_AlaRipngPort_Type())
alaRipngPort.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngPort.setStatus(_B)
_AlaRipngInterfaceTable_Object=MibTable
alaRipngInterfaceTable=_AlaRipngInterfaceTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11))
if mibBuilder.loadTexts:alaRipngInterfaceTable.setStatus(_B)
_AlaRipngInterfaceEntry_Object=MibTableRow
alaRipngInterfaceEntry=_AlaRipngInterfaceEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1))
alaRipngInterfaceEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:alaRipngInterfaceEntry.setStatus(_B)
class _AlaRipngInterfaceStatus_Type(RowStatus):defaultValue=2
_AlaRipngInterfaceStatus_Type.__name__=_K
_AlaRipngInterfaceStatus_Object=MibTableColumn
alaRipngInterfaceStatus=_AlaRipngInterfaceStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,1),_AlaRipngInterfaceStatus_Type())
alaRipngInterfaceStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngInterfaceStatus.setStatus(_B)
class _AlaRipngInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaRipngInterfaceIndex_Type.__name__=_C
_AlaRipngInterfaceIndex_Object=MibTableColumn
alaRipngInterfaceIndex=_AlaRipngInterfaceIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,2),_AlaRipngInterfaceIndex_Type())
alaRipngInterfaceIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:alaRipngInterfaceIndex.setStatus(_B)
class _AlaRipngInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AlaRipngInterfaceMetric_Type.__name__=_C
_AlaRipngInterfaceMetric_Object=MibTableColumn
alaRipngInterfaceMetric=_AlaRipngInterfaceMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,3),_AlaRipngInterfaceMetric_Type())
alaRipngInterfaceMetric.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngInterfaceMetric.setStatus(_B)
class _AlaRipngInterfaceRecvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_AlaRipngInterfaceRecvStatus_Type.__name__=_C
_AlaRipngInterfaceRecvStatus_Object=MibTableColumn
alaRipngInterfaceRecvStatus=_AlaRipngInterfaceRecvStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,4),_AlaRipngInterfaceRecvStatus_Type())
alaRipngInterfaceRecvStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngInterfaceRecvStatus.setStatus(_B)
class _AlaRipngInterfaceSendStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_AlaRipngInterfaceSendStatus_Type.__name__=_C
_AlaRipngInterfaceSendStatus_Object=MibTableColumn
alaRipngInterfaceSendStatus=_AlaRipngInterfaceSendStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,5),_AlaRipngInterfaceSendStatus_Type())
alaRipngInterfaceSendStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngInterfaceSendStatus.setStatus(_B)
class _AlaRipngInterfaceHorizon_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('onlysplit',2),('poison',3)))
_AlaRipngInterfaceHorizon_Type.__name__=_C
_AlaRipngInterfaceHorizon_Object=MibTableColumn
alaRipngInterfaceHorizon=_AlaRipngInterfaceHorizon_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,6),_AlaRipngInterfaceHorizon_Type())
alaRipngInterfaceHorizon.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngInterfaceHorizon.setStatus(_B)
_AlaRipngInterfacePacketsSent_Type=Integer32
_AlaRipngInterfacePacketsSent_Object=MibTableColumn
alaRipngInterfacePacketsSent=_AlaRipngInterfacePacketsSent_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,7),_AlaRipngInterfacePacketsSent_Type())
alaRipngInterfacePacketsSent.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngInterfacePacketsSent.setStatus(_B)
_AlaRipngInterfacePacketsRcvd_Type=Integer32
_AlaRipngInterfacePacketsRcvd_Object=MibTableColumn
alaRipngInterfacePacketsRcvd=_AlaRipngInterfacePacketsRcvd_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,8),_AlaRipngInterfacePacketsRcvd_Type())
alaRipngInterfacePacketsRcvd.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngInterfacePacketsRcvd.setStatus(_B)
_AlaRipngInterfaceMTU_Type=Counter32
_AlaRipngInterfaceMTU_Object=MibTableColumn
alaRipngInterfaceMTU=_AlaRipngInterfaceMTU_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,9),_AlaRipngInterfaceMTU_Type())
alaRipngInterfaceMTU.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngInterfaceMTU.setStatus(_B)
_AlaRipngInterfaceNextUpdate_Type=TimeTicks
_AlaRipngInterfaceNextUpdate_Object=MibTableColumn
alaRipngInterfaceNextUpdate=_AlaRipngInterfaceNextUpdate_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,10),_AlaRipngInterfaceNextUpdate_Type())
alaRipngInterfaceNextUpdate.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngInterfaceNextUpdate.setStatus(_B)
class _AlaRipngInterfaceJitter_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AlaRipngInterfaceJitter_Type.__name__=_C
_AlaRipngInterfaceJitter_Object=MibTableColumn
alaRipngInterfaceJitter=_AlaRipngInterfaceJitter_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,11,1,11),_AlaRipngInterfaceJitter_Type())
alaRipngInterfaceJitter.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngInterfaceJitter.setStatus(_D)
_AlaRipngNexthopFilterTable_Object=MibTable
alaRipngNexthopFilterTable=_AlaRipngNexthopFilterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,12))
if mibBuilder.loadTexts:alaRipngNexthopFilterTable.setStatus(_D)
_AlaRipngNexthopFilterEntry_Object=MibTableRow
alaRipngNexthopFilterEntry=_AlaRipngNexthopFilterEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,12,1))
alaRipngNexthopFilterEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:alaRipngNexthopFilterEntry.setStatus(_D)
class _AlaRipngNexthopFilterStatus_Type(RowStatus):defaultValue=2
_AlaRipngNexthopFilterStatus_Type.__name__=_K
_AlaRipngNexthopFilterStatus_Object=MibTableColumn
alaRipngNexthopFilterStatus=_AlaRipngNexthopFilterStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,12,1,1),_AlaRipngNexthopFilterStatus_Type())
alaRipngNexthopFilterStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngNexthopFilterStatus.setStatus(_D)
_AlaRipngNexthopFilterAddress_Type=Ipv6Address
_AlaRipngNexthopFilterAddress_Object=MibTableColumn
alaRipngNexthopFilterAddress=_AlaRipngNexthopFilterAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,12,1,2),_AlaRipngNexthopFilterAddress_Type())
alaRipngNexthopFilterAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngNexthopFilterAddress.setStatus(_D)
_AlaRipngSummarizationTable_Object=MibTable
alaRipngSummarizationTable=_AlaRipngSummarizationTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13))
if mibBuilder.loadTexts:alaRipngSummarizationTable.setStatus(_D)
_AlaRipngSummarizationEntry_Object=MibTableRow
alaRipngSummarizationEntry=_AlaRipngSummarizationEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1))
alaRipngSummarizationEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_A,_P),(0,_A,_Q))
if mibBuilder.loadTexts:alaRipngSummarizationEntry.setStatus(_D)
class _AlaRipngSummarizationStatus_Type(RowStatus):defaultValue=2
_AlaRipngSummarizationStatus_Type.__name__=_K
_AlaRipngSummarizationStatus_Object=MibTableColumn
alaRipngSummarizationStatus=_AlaRipngSummarizationStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1,1),_AlaRipngSummarizationStatus_Type())
alaRipngSummarizationStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngSummarizationStatus.setStatus(_D)
_AlaRipngSummarizationSourcePrefix_Type=Ipv6AddressPrefix
_AlaRipngSummarizationSourcePrefix_Object=MibTableColumn
alaRipngSummarizationSourcePrefix=_AlaRipngSummarizationSourcePrefix_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1,2),_AlaRipngSummarizationSourcePrefix_Type())
alaRipngSummarizationSourcePrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngSummarizationSourcePrefix.setStatus(_D)
class _AlaRipngSummarizationSourcePrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaRipngSummarizationSourcePrefixLen_Type.__name__=_C
_AlaRipngSummarizationSourcePrefixLen_Object=MibTableColumn
alaRipngSummarizationSourcePrefixLen=_AlaRipngSummarizationSourcePrefixLen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1,3),_AlaRipngSummarizationSourcePrefixLen_Type())
alaRipngSummarizationSourcePrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngSummarizationSourcePrefixLen.setStatus(_D)
_AlaRipngSummarizationPrefix_Type=Ipv6AddressPrefix
_AlaRipngSummarizationPrefix_Object=MibTableColumn
alaRipngSummarizationPrefix=_AlaRipngSummarizationPrefix_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1,4),_AlaRipngSummarizationPrefix_Type())
alaRipngSummarizationPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngSummarizationPrefix.setStatus(_D)
class _AlaRipngSummarizationPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaRipngSummarizationPrefixLen_Type.__name__=_C
_AlaRipngSummarizationPrefixLen_Object=MibTableColumn
alaRipngSummarizationPrefixLen=_AlaRipngSummarizationPrefixLen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1,5),_AlaRipngSummarizationPrefixLen_Type())
alaRipngSummarizationPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngSummarizationPrefixLen.setStatus(_D)
class _AlaRipngSummarizationSubnets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_AlaRipngSummarizationSubnets_Type.__name__=_C
_AlaRipngSummarizationSubnets_Object=MibTableColumn
alaRipngSummarizationSubnets=_AlaRipngSummarizationSubnets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,13,1,6),_AlaRipngSummarizationSubnets_Type())
alaRipngSummarizationSubnets.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngSummarizationSubnets.setStatus(_D)
_AlaRipngRouteFilterTable_Object=MibTable
alaRipngRouteFilterTable=_AlaRipngRouteFilterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14))
if mibBuilder.loadTexts:alaRipngRouteFilterTable.setStatus(_D)
_AlaRipngRouteFilterEntry_Object=MibTableRow
alaRipngRouteFilterEntry=_AlaRipngRouteFilterEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14,1))
alaRipngRouteFilterEntry.setIndexNames((0,_A,_R),(0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:alaRipngRouteFilterEntry.setStatus(_D)
class _AlaRipngRouteFilterStatus_Type(RowStatus):defaultValue=2
_AlaRipngRouteFilterStatus_Type.__name__=_K
_AlaRipngRouteFilterStatus_Object=MibTableColumn
alaRipngRouteFilterStatus=_AlaRipngRouteFilterStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14,1,1),_AlaRipngRouteFilterStatus_Type())
alaRipngRouteFilterStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngRouteFilterStatus.setStatus(_D)
_AlaRipngRouteFilterPrefix_Type=Ipv6AddressPrefix
_AlaRipngRouteFilterPrefix_Object=MibTableColumn
alaRipngRouteFilterPrefix=_AlaRipngRouteFilterPrefix_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14,1,2),_AlaRipngRouteFilterPrefix_Type())
alaRipngRouteFilterPrefix.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngRouteFilterPrefix.setStatus(_D)
class _AlaRipngRouteFilterPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AlaRipngRouteFilterPrefixLen_Type.__name__=_C
_AlaRipngRouteFilterPrefixLen_Object=MibTableColumn
alaRipngRouteFilterPrefixLen=_AlaRipngRouteFilterPrefixLen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14,1,3),_AlaRipngRouteFilterPrefixLen_Type())
alaRipngRouteFilterPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngRouteFilterPrefixLen.setStatus(_D)
class _AlaRipngRouteFilterDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_AlaRipngRouteFilterDirection_Type.__name__=_C
_AlaRipngRouteFilterDirection_Object=MibTableColumn
alaRipngRouteFilterDirection=_AlaRipngRouteFilterDirection_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14,1,4),_AlaRipngRouteFilterDirection_Type())
alaRipngRouteFilterDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngRouteFilterDirection.setStatus(_D)
class _AlaRipngRouteFilterSubnets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_AlaRipngRouteFilterSubnets_Type.__name__=_C
_AlaRipngRouteFilterSubnets_Object=MibTableColumn
alaRipngRouteFilterSubnets=_AlaRipngRouteFilterSubnets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,14,1,5),_AlaRipngRouteFilterSubnets_Type())
alaRipngRouteFilterSubnets.setMaxAccess(_I)
if mibBuilder.loadTexts:alaRipngRouteFilterSubnets.setStatus(_D)
_AlaRipngPeerTable_Object=MibTable
alaRipngPeerTable=_AlaRipngPeerTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15))
if mibBuilder.loadTexts:alaRipngPeerTable.setStatus(_B)
_AlaRipngPeerEntry_Object=MibTableRow
alaRipngPeerEntry=_AlaRipngPeerEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1))
alaRipngPeerEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:alaRipngPeerEntry.setStatus(_B)
_AlaRipngPeerAddress_Type=Ipv6Address
_AlaRipngPeerAddress_Object=MibTableColumn
alaRipngPeerAddress=_AlaRipngPeerAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,1),_AlaRipngPeerAddress_Type())
alaRipngPeerAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:alaRipngPeerAddress.setStatus(_B)
_AlaRipngPeerLastUpdate_Type=TimeTicks
_AlaRipngPeerLastUpdate_Object=MibTableColumn
alaRipngPeerLastUpdate=_AlaRipngPeerLastUpdate_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,2),_AlaRipngPeerLastUpdate_Type())
alaRipngPeerLastUpdate.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerLastUpdate.setStatus(_B)
_AlaRipngPeerNumUpdates_Type=Counter32
_AlaRipngPeerNumUpdates_Object=MibTableColumn
alaRipngPeerNumUpdates=_AlaRipngPeerNumUpdates_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,3),_AlaRipngPeerNumUpdates_Type())
alaRipngPeerNumUpdates.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerNumUpdates.setStatus(_B)
_AlaRipngPeerNumRoutes_Type=Counter32
_AlaRipngPeerNumRoutes_Object=MibTableColumn
alaRipngPeerNumRoutes=_AlaRipngPeerNumRoutes_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,4),_AlaRipngPeerNumRoutes_Type())
alaRipngPeerNumRoutes.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerNumRoutes.setStatus(_B)
_AlaRipngPeerBadPackets_Type=Counter32
_AlaRipngPeerBadPackets_Object=MibTableColumn
alaRipngPeerBadPackets=_AlaRipngPeerBadPackets_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,5),_AlaRipngPeerBadPackets_Type())
alaRipngPeerBadPackets.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerBadPackets.setStatus(_B)
_AlaRipngPeerBadRoutes_Type=Counter32
_AlaRipngPeerBadRoutes_Object=MibTableColumn
alaRipngPeerBadRoutes=_AlaRipngPeerBadRoutes_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,6),_AlaRipngPeerBadRoutes_Type())
alaRipngPeerBadRoutes.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerBadRoutes.setStatus(_B)
class _AlaRipngPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaRipngPeerIndex_Type.__name__=_C
_AlaRipngPeerIndex_Object=MibTableColumn
alaRipngPeerIndex=_AlaRipngPeerIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,15,1,7),_AlaRipngPeerIndex_Type())
alaRipngPeerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:alaRipngPeerIndex.setStatus(_B)
_AlaRipngRouteTable_Object=MibTable
alaRipngRouteTable=_AlaRipngRouteTable_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16))
if mibBuilder.loadTexts:alaRipngRouteTable.setStatus(_B)
_AlaRipngRouteEntry_Object=MibTableRow
alaRipngRouteEntry=_AlaRipngRouteEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1))
alaRipngRouteEntry.setIndexNames((0,_A,_b),(0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:alaRipngRouteEntry.setStatus(_B)
_AlaRipngRoutePrefix_Type=Ipv6AddressPrefix
_AlaRipngRoutePrefix_Object=MibTableColumn
alaRipngRoutePrefix=_AlaRipngRoutePrefix_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,1),_AlaRipngRoutePrefix_Type())
alaRipngRoutePrefix.setMaxAccess(_J)
if mibBuilder.loadTexts:alaRipngRoutePrefix.setStatus(_B)
class _AlaRipngRoutePrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaRipngRoutePrefixLen_Type.__name__=_C
_AlaRipngRoutePrefixLen_Object=MibTableColumn
alaRipngRoutePrefixLen=_AlaRipngRoutePrefixLen_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,2),_AlaRipngRoutePrefixLen_Type())
alaRipngRoutePrefixLen.setMaxAccess(_J)
if mibBuilder.loadTexts:alaRipngRoutePrefixLen.setStatus(_B)
_AlaRipngRouteNextHop_Type=Ipv6Address
_AlaRipngRouteNextHop_Object=MibTableColumn
alaRipngRouteNextHop=_AlaRipngRouteNextHop_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,3),_AlaRipngRouteNextHop_Type())
alaRipngRouteNextHop.setMaxAccess(_J)
if mibBuilder.loadTexts:alaRipngRouteNextHop.setStatus(_B)
class _AlaRipngRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('rip',2),('redist',3),(_e,4)))
_AlaRipngRouteType_Type.__name__=_C
_AlaRipngRouteType_Object=MibTableColumn
alaRipngRouteType=_AlaRipngRouteType_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,4),_AlaRipngRouteType_Type())
alaRipngRouteType.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteType.setStatus(_B)
_AlaRipngRouteAge_Type=TimeTicks
_AlaRipngRouteAge_Object=MibTableColumn
alaRipngRouteAge=_AlaRipngRouteAge_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,5),_AlaRipngRouteAge_Type())
alaRipngRouteAge.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteAge.setStatus(_B)
class _AlaRipngRouteTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaRipngRouteTag_Type.__name__=_C
_AlaRipngRouteTag_Object=MibTableColumn
alaRipngRouteTag=_AlaRipngRouteTag_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,6),_AlaRipngRouteTag_Type())
alaRipngRouteTag.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteTag.setStatus(_B)
class _AlaRipngRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AlaRipngRouteMetric_Type.__name__=_C
_AlaRipngRouteMetric_Object=MibTableColumn
alaRipngRouteMetric=_AlaRipngRouteMetric_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,7),_AlaRipngRouteMetric_Type())
alaRipngRouteMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteMetric.setStatus(_B)
_AlaRipngRouteStatus_Type=RowStatus
_AlaRipngRouteStatus_Object=MibTableColumn
alaRipngRouteStatus=_AlaRipngRouteStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,8),_AlaRipngRouteStatus_Type())
alaRipngRouteStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteStatus.setStatus(_B)
class _AlaRipngRouteFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('garbage',2),('holddown',3),(_e,4)))
_AlaRipngRouteFlags_Type.__name__=_C
_AlaRipngRouteFlags_Object=MibTableColumn
alaRipngRouteFlags=_AlaRipngRouteFlags_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,9),_AlaRipngRouteFlags_Type())
alaRipngRouteFlags.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteFlags.setStatus(_B)
_AlaRipngRouteIndex_Type=Integer32
_AlaRipngRouteIndex_Object=MibTableColumn
alaRipngRouteIndex=_AlaRipngRouteIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,1,16,1,10),_AlaRipngRouteIndex_Type())
alaRipngRouteIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteIndex.setStatus(_B)
_AlaRipngDebug_ObjectIdentity=ObjectIdentity
alaRipngDebug=_AlaRipngDebug_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2))
class _AlaRipngDebugLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaRipngDebugLevel_Type.__name__=_C
_AlaRipngDebugLevel_Object=MibScalar
alaRipngDebugLevel=_AlaRipngDebugLevel_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,1),_AlaRipngDebugLevel_Type())
alaRipngDebugLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugLevel.setStatus(_D)
class _AlaRipngDebugError_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugError_Type.__name__=_C
_AlaRipngDebugError_Object=MibScalar
alaRipngDebugError=_AlaRipngDebugError_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,2),_AlaRipngDebugError_Type())
alaRipngDebugError.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugError.setStatus(_D)
class _AlaRipngDebugWarn_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugWarn_Type.__name__=_C
_AlaRipngDebugWarn_Object=MibScalar
alaRipngDebugWarn=_AlaRipngDebugWarn_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,3),_AlaRipngDebugWarn_Type())
alaRipngDebugWarn.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugWarn.setStatus(_D)
class _AlaRipngDebugRecv_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugRecv_Type.__name__=_C
_AlaRipngDebugRecv_Object=MibScalar
alaRipngDebugRecv=_AlaRipngDebugRecv_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,4),_AlaRipngDebugRecv_Type())
alaRipngDebugRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugRecv.setStatus(_D)
class _AlaRipngDebugSend_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugSend_Type.__name__=_C
_AlaRipngDebugSend_Object=MibScalar
alaRipngDebugSend=_AlaRipngDebugSend_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,5),_AlaRipngDebugSend_Type())
alaRipngDebugSend.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugSend.setStatus(_D)
class _AlaRipngDebugRdb_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugRdb_Type.__name__=_C
_AlaRipngDebugRdb_Object=MibScalar
alaRipngDebugRdb=_AlaRipngDebugRdb_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,6),_AlaRipngDebugRdb_Type())
alaRipngDebugRdb.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugRdb.setStatus(_D)
class _AlaRipngDebugAge_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugAge_Type.__name__=_C
_AlaRipngDebugAge_Object=MibScalar
alaRipngDebugAge=_AlaRipngDebugAge_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,7),_AlaRipngDebugAge_Type())
alaRipngDebugAge.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugAge.setStatus(_D)
class _AlaRipngDebugMip_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugMip_Type.__name__=_C
_AlaRipngDebugMip_Object=MibScalar
alaRipngDebugMip=_AlaRipngDebugMip_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,8),_AlaRipngDebugMip_Type())
alaRipngDebugMip.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugMip.setStatus(_D)
class _AlaRipngDebugInfo_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugInfo_Type.__name__=_C
_AlaRipngDebugInfo_Object=MibScalar
alaRipngDebugInfo=_AlaRipngDebugInfo_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,9),_AlaRipngDebugInfo_Type())
alaRipngDebugInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugInfo.setStatus(_D)
class _AlaRipngDebugSetup_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugSetup_Type.__name__=_C
_AlaRipngDebugSetup_Object=MibScalar
alaRipngDebugSetup=_AlaRipngDebugSetup_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,10),_AlaRipngDebugSetup_Type())
alaRipngDebugSetup.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugSetup.setStatus(_D)
class _AlaRipngDebugTime_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugTime_Type.__name__=_C
_AlaRipngDebugTime_Object=MibScalar
alaRipngDebugTime=_AlaRipngDebugTime_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,11),_AlaRipngDebugTime_Type())
alaRipngDebugTime.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugTime.setStatus(_D)
class _AlaRipngDebugTm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugTm_Type.__name__=_C
_AlaRipngDebugTm_Object=MibScalar
alaRipngDebugTm=_AlaRipngDebugTm_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,12),_AlaRipngDebugTm_Type())
alaRipngDebugTm.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugTm.setStatus(_D)
class _AlaRipngDebugRouteFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugRouteFilter_Type.__name__=_C
_AlaRipngDebugRouteFilter_Object=MibScalar
alaRipngDebugRouteFilter=_AlaRipngDebugRouteFilter_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,13),_AlaRipngDebugRouteFilter_Type())
alaRipngDebugRouteFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugRouteFilter.setStatus(_D)
class _AlaRipngDebugNexthopFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugNexthopFilter_Type.__name__=_C
_AlaRipngDebugNexthopFilter_Object=MibScalar
alaRipngDebugNexthopFilter=_AlaRipngDebugNexthopFilter_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,14),_AlaRipngDebugNexthopFilter_Type())
alaRipngDebugNexthopFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugNexthopFilter.setStatus(_D)
class _AlaRipngDebugSummary_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugSummary_Type.__name__=_C
_AlaRipngDebugSummary_Object=MibScalar
alaRipngDebugSummary=_AlaRipngDebugSummary_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,15),_AlaRipngDebugSummary_Type())
alaRipngDebugSummary.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugSummary.setStatus(_D)
class _AlaRipngDebugAll_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlaRipngDebugAll_Type.__name__=_C
_AlaRipngDebugAll_Object=MibScalar
alaRipngDebugAll=_AlaRipngDebugAll_Object((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,1,2,16),_AlaRipngDebugAll_Type())
alaRipngDebugAll.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngDebugAll.setStatus(_D)
_AlcatelIND1RIPNGMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBConformance=_AlcatelIND1RIPNGMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBConformance.setStatus(_B)
_AlcatelIND1RIPNGMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBGroups=_AlcatelIND1RIPNGMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBGroups.setStatus(_B)
_AlcatelIND1RIPNGMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBCompliances=_AlcatelIND1RIPNGMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,2))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBCompliances.setStatus(_B)
_AlcatelIND1RIPNGTraps_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGTraps=_AlcatelIND1RIPNGTraps_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,3))
_AlcatelIND1RIPNGTrapsRoot_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGTrapsRoot=_AlcatelIND1RIPNGTrapsRoot_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,3,0))
alaRipngGlobalGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,1))
alaRipngGlobalGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:alaRipngGlobalGroup.setStatus(_B)
alaRipngDebugGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,2))
alaRipngDebugGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:alaRipngDebugGroup.setStatus(_B)
alaRipngInterfaceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,3))
alaRipngInterfaceGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:alaRipngInterfaceGroup.setStatus(_B)
alaRipngNexthopFilterGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,4))
alaRipngNexthopFilterGroup.setObjects(*((_A,_AC),(_A,_M)))
if mibBuilder.loadTexts:alaRipngNexthopFilterGroup.setStatus(_B)
alaRipngSummarizationGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,5))
alaRipngSummarizationGroup.setObjects(*((_A,_AD),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_AE)))
if mibBuilder.loadTexts:alaRipngSummarizationGroup.setStatus(_B)
alaRipngRouteFilterGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,6))
alaRipngRouteFilterGroup.setObjects(*((_A,_AF),(_A,_R),(_A,_S),(_A,_T),(_A,_AG)))
if mibBuilder.loadTexts:alaRipngRouteFilterGroup.setStatus(_B)
alaRipngPeerGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,7))
alaRipngPeerGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:alaRipngPeerGroup.setStatus(_B)
alaRipngRouteGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,8))
alaRipngRouteGroup.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:alaRipngRouteGroup.setStatus(_B)
ripngRouteMaxLimitReached=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,3,0,1))
if mibBuilder.loadTexts:ripngRouteMaxLimitReached.setStatus(_B)
alaRipngNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,1,9))
alaRipngNotificationGroup.setObjects((_A,_AW))
if mibBuilder.loadTexts:alaRipngNotificationGroup.setStatus(_B)
alcatelIND1RIPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,10,12,1,2,2,1))
alcatelIND1RIPMIBCompliance.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:alcatelIND1RIPMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1RIPNGMIB':alcatelIND1RIPNGMIB,'alcatelIND1RIPNGMIBObjects':alcatelIND1RIPNGMIBObjects,'alaProtocolRipng':alaProtocolRipng,_f:alaRipngProtoStatus,_g:alaRipngUpdateInterval,_h:alaRipngInvalidTimer,_i:alaRipngHolddownTimer,_j:alaRipngGarbageTimer,_k:alaRipngRouteCount,_l:alaRipngGlobalRouteTag,_m:alaRipngTriggeredSends,_n:alaRipngJitter,_o:alaRipngPort,'alaRipngInterfaceTable':alaRipngInterfaceTable,'alaRipngInterfaceEntry':alaRipngInterfaceEntry,_A2:alaRipngInterfaceStatus,_U:alaRipngInterfaceIndex,_A3:alaRipngInterfaceMetric,_A4:alaRipngInterfaceRecvStatus,_A5:alaRipngInterfaceSendStatus,_A6:alaRipngInterfaceHorizon,_A7:alaRipngInterfacePacketsSent,_A8:alaRipngInterfacePacketsRcvd,_A9:alaRipngInterfaceMTU,_AA:alaRipngInterfaceNextUpdate,_AB:alaRipngInterfaceJitter,'alaRipngNexthopFilterTable':alaRipngNexthopFilterTable,'alaRipngNexthopFilterEntry':alaRipngNexthopFilterEntry,_AC:alaRipngNexthopFilterStatus,_M:alaRipngNexthopFilterAddress,'alaRipngSummarizationTable':alaRipngSummarizationTable,'alaRipngSummarizationEntry':alaRipngSummarizationEntry,_AD:alaRipngSummarizationStatus,_N:alaRipngSummarizationSourcePrefix,_O:alaRipngSummarizationSourcePrefixLen,_P:alaRipngSummarizationPrefix,_Q:alaRipngSummarizationPrefixLen,_AE:alaRipngSummarizationSubnets,'alaRipngRouteFilterTable':alaRipngRouteFilterTable,'alaRipngRouteFilterEntry':alaRipngRouteFilterEntry,_AF:alaRipngRouteFilterStatus,_R:alaRipngRouteFilterPrefix,_S:alaRipngRouteFilterPrefixLen,_T:alaRipngRouteFilterDirection,_AG:alaRipngRouteFilterSubnets,'alaRipngPeerTable':alaRipngPeerTable,'alaRipngPeerEntry':alaRipngPeerEntry,_Z:alaRipngPeerAddress,_AH:alaRipngPeerLastUpdate,_AI:alaRipngPeerNumUpdates,_AJ:alaRipngPeerNumRoutes,_AK:alaRipngPeerBadPackets,_AL:alaRipngPeerBadRoutes,_a:alaRipngPeerIndex,'alaRipngRouteTable':alaRipngRouteTable,'alaRipngRouteEntry':alaRipngRouteEntry,_b:alaRipngRoutePrefix,_c:alaRipngRoutePrefixLen,_d:alaRipngRouteNextHop,_AM:alaRipngRouteType,_AN:alaRipngRouteAge,_AO:alaRipngRouteTag,_AP:alaRipngRouteMetric,_AQ:alaRipngRouteStatus,_AR:alaRipngRouteFlags,_AS:alaRipngRouteIndex,'alaRipngDebug':alaRipngDebug,_p:alaRipngDebugLevel,_q:alaRipngDebugError,_r:alaRipngDebugWarn,_s:alaRipngDebugRecv,_t:alaRipngDebugSend,_u:alaRipngDebugRdb,_v:alaRipngDebugAge,_w:alaRipngDebugMip,_x:alaRipngDebugInfo,_y:alaRipngDebugSetup,_z:alaRipngDebugTime,_A0:alaRipngDebugTm,_AU:alaRipngDebugRouteFilter,_AT:alaRipngDebugNexthopFilter,_AV:alaRipngDebugSummary,_A1:alaRipngDebugAll,'alcatelIND1RIPNGMIBConformance':alcatelIND1RIPNGMIBConformance,'alcatelIND1RIPNGMIBGroups':alcatelIND1RIPNGMIBGroups,_AX:alaRipngGlobalGroup,_AY:alaRipngDebugGroup,_AZ:alaRipngInterfaceGroup,_Aa:alaRipngNexthopFilterGroup,_Ab:alaRipngSummarizationGroup,_Ac:alaRipngRouteFilterGroup,_Ad:alaRipngPeerGroup,_Ae:alaRipngRouteGroup,'alaRipngNotificationGroup':alaRipngNotificationGroup,'alcatelIND1RIPNGMIBCompliances':alcatelIND1RIPNGMIBCompliances,'alcatelIND1RIPMIBCompliance':alcatelIND1RIPMIBCompliance,'alcatelIND1RIPNGTraps':alcatelIND1RIPNGTraps,'alcatelIND1RIPNGTrapsRoot':alcatelIND1RIPNGTrapsRoot,_AW:ripngRouteMaxLimitReached})