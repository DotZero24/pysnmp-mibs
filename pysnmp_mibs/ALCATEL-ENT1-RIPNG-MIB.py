_A2='alaRipngRouteGroup'
_A1='alaRipngPeerGroup'
_A0='alaRipngInterfaceGroup'
_z='alaRipngGlobalGroup'
_y='ripngRouteMaxLimitReached'
_x='alaRipngRouteIndex'
_w='alaRipngRouteFlags'
_v='alaRipngRouteStatus'
_u='alaRipngRouteMetric'
_t='alaRipngRouteTag'
_s='alaRipngRouteAge'
_r='alaRipngRouteType'
_q='alaRipngPeerBadRoutes'
_p='alaRipngPeerBadPackets'
_o='alaRipngPeerNumRoutes'
_n='alaRipngPeerNumUpdates'
_m='alaRipngPeerLastUpdate'
_l='alaRipngInterfaceNextUpdate'
_k='alaRipngInterfaceMTU'
_j='alaRipngInterfacePacketsRcvd'
_i='alaRipngInterfacePacketsSent'
_h='alaRipngInterfaceHorizon'
_g='alaRipngInterfaceSendStatus'
_f='alaRipngInterfaceRecvStatus'
_e='alaRipngInterfaceMetric'
_d='alaRipngInterfaceStatus'
_c='alaRipngPort'
_b='alaRipngJitter'
_a='alaRipngTriggeredSends'
_Z='alaRipngGlobalRouteTag'
_Y='alaRipngRouteCount'
_X='alaRipngGarbageTimer'
_W='alaRipngHolddownTimer'
_V='alaRipngInvalidTimer'
_U='alaRipngUpdateInterval'
_T='alaRipngProtoStatus'
_S='active'
_R='unknown'
_Q='alaRipngRouteNextHop'
_P='alaRipngRoutePrefixLen'
_O='alaRipngRoutePrefix'
_N='alaRipngPeerIndex'
_M='alaRipngPeerAddress'
_L='disabled'
_K='enabled'
_J='alaRipngInterfaceIndex'
_I='RowStatus'
_H='seconds'
_G='read-create'
_F='not-accessible'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALCATEL-ENT1-RIPNG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Ripng,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Ripng')
Ipv6Address,Ipv6AddressPrefix=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressPrefix')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_I,'TextualConvention')
alcatelIND1RIPNGMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1RIPNGMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBObjects=_AlcatelIND1RIPNGMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBObjects.setStatus(_A)
_AlaProtocolRipng_ObjectIdentity=ObjectIdentity
alaProtocolRipng=_AlaProtocolRipng_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1))
class _AlaRipngProtoStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaRipngProtoStatus_Type.__name__=_C
_AlaRipngProtoStatus_Object=MibScalar
alaRipngProtoStatus=_AlaRipngProtoStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,1),_AlaRipngProtoStatus_Type())
alaRipngProtoStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngProtoStatus.setStatus(_A)
class _AlaRipngUpdateInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_AlaRipngUpdateInterval_Type.__name__=_C
_AlaRipngUpdateInterval_Object=MibScalar
alaRipngUpdateInterval=_AlaRipngUpdateInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,2),_AlaRipngUpdateInterval_Type())
alaRipngUpdateInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngUpdateInterval.setStatus(_A)
if mibBuilder.loadTexts:alaRipngUpdateInterval.setUnits(_H)
class _AlaRipngInvalidTimer_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,360))
_AlaRipngInvalidTimer_Type.__name__=_C
_AlaRipngInvalidTimer_Object=MibScalar
alaRipngInvalidTimer=_AlaRipngInvalidTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,3),_AlaRipngInvalidTimer_Type())
alaRipngInvalidTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngInvalidTimer.setStatus(_A)
if mibBuilder.loadTexts:alaRipngInvalidTimer.setUnits(_H)
class _AlaRipngHolddownTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_AlaRipngHolddownTimer_Type.__name__=_C
_AlaRipngHolddownTimer_Object=MibScalar
alaRipngHolddownTimer=_AlaRipngHolddownTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,4),_AlaRipngHolddownTimer_Type())
alaRipngHolddownTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngHolddownTimer.setStatus(_A)
class _AlaRipngGarbageTimer_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_AlaRipngGarbageTimer_Type.__name__=_C
_AlaRipngGarbageTimer_Object=MibScalar
alaRipngGarbageTimer=_AlaRipngGarbageTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,5),_AlaRipngGarbageTimer_Type())
alaRipngGarbageTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngGarbageTimer.setStatus(_A)
class _AlaRipngRouteCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaRipngRouteCount_Type.__name__=_C
_AlaRipngRouteCount_Object=MibScalar
alaRipngRouteCount=_AlaRipngRouteCount_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,6),_AlaRipngRouteCount_Type())
alaRipngRouteCount.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteCount.setStatus(_A)
class _AlaRipngGlobalRouteTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaRipngGlobalRouteTag_Type.__name__=_C
_AlaRipngGlobalRouteTag_Object=MibScalar
alaRipngGlobalRouteTag=_AlaRipngGlobalRouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,7),_AlaRipngGlobalRouteTag_Type())
alaRipngGlobalRouteTag.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngGlobalRouteTag.setStatus(_A)
class _AlaRipngTriggeredSends_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('onlyupdated',2),('off',3)))
_AlaRipngTriggeredSends_Type.__name__=_C
_AlaRipngTriggeredSends_Object=MibScalar
alaRipngTriggeredSends=_AlaRipngTriggeredSends_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,8),_AlaRipngTriggeredSends_Type())
alaRipngTriggeredSends.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngTriggeredSends.setStatus(_A)
class _AlaRipngJitter_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AlaRipngJitter_Type.__name__=_C
_AlaRipngJitter_Object=MibScalar
alaRipngJitter=_AlaRipngJitter_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,9),_AlaRipngJitter_Type())
alaRipngJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngJitter.setStatus(_A)
if mibBuilder.loadTexts:alaRipngJitter.setUnits(_H)
class _AlaRipngPort_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AlaRipngPort_Type.__name__=_C
_AlaRipngPort_Object=MibScalar
alaRipngPort=_AlaRipngPort_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,10),_AlaRipngPort_Type())
alaRipngPort.setMaxAccess(_E)
if mibBuilder.loadTexts:alaRipngPort.setStatus(_A)
_AlaRipngInterfaceTable_Object=MibTable
alaRipngInterfaceTable=_AlaRipngInterfaceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11))
if mibBuilder.loadTexts:alaRipngInterfaceTable.setStatus(_A)
_AlaRipngInterfaceEntry_Object=MibTableRow
alaRipngInterfaceEntry=_AlaRipngInterfaceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1))
alaRipngInterfaceEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:alaRipngInterfaceEntry.setStatus(_A)
class _AlaRipngInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaRipngInterfaceIndex_Type.__name__=_C
_AlaRipngInterfaceIndex_Object=MibTableColumn
alaRipngInterfaceIndex=_AlaRipngInterfaceIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,1),_AlaRipngInterfaceIndex_Type())
alaRipngInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngInterfaceIndex.setStatus(_A)
class _AlaRipngInterfaceStatus_Type(RowStatus):defaultValue=2
_AlaRipngInterfaceStatus_Type.__name__=_I
_AlaRipngInterfaceStatus_Object=MibTableColumn
alaRipngInterfaceStatus=_AlaRipngInterfaceStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,2),_AlaRipngInterfaceStatus_Type())
alaRipngInterfaceStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:alaRipngInterfaceStatus.setStatus(_A)
class _AlaRipngInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AlaRipngInterfaceMetric_Type.__name__=_C
_AlaRipngInterfaceMetric_Object=MibTableColumn
alaRipngInterfaceMetric=_AlaRipngInterfaceMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,3),_AlaRipngInterfaceMetric_Type())
alaRipngInterfaceMetric.setMaxAccess(_G)
if mibBuilder.loadTexts:alaRipngInterfaceMetric.setStatus(_A)
class _AlaRipngInterfaceRecvStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaRipngInterfaceRecvStatus_Type.__name__=_C
_AlaRipngInterfaceRecvStatus_Object=MibTableColumn
alaRipngInterfaceRecvStatus=_AlaRipngInterfaceRecvStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,4),_AlaRipngInterfaceRecvStatus_Type())
alaRipngInterfaceRecvStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:alaRipngInterfaceRecvStatus.setStatus(_A)
class _AlaRipngInterfaceSendStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaRipngInterfaceSendStatus_Type.__name__=_C
_AlaRipngInterfaceSendStatus_Object=MibTableColumn
alaRipngInterfaceSendStatus=_AlaRipngInterfaceSendStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,5),_AlaRipngInterfaceSendStatus_Type())
alaRipngInterfaceSendStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:alaRipngInterfaceSendStatus.setStatus(_A)
class _AlaRipngInterfaceHorizon_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('onlysplit',2),('poison',3)))
_AlaRipngInterfaceHorizon_Type.__name__=_C
_AlaRipngInterfaceHorizon_Object=MibTableColumn
alaRipngInterfaceHorizon=_AlaRipngInterfaceHorizon_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,6),_AlaRipngInterfaceHorizon_Type())
alaRipngInterfaceHorizon.setMaxAccess(_G)
if mibBuilder.loadTexts:alaRipngInterfaceHorizon.setStatus(_A)
_AlaRipngInterfacePacketsSent_Type=Integer32
_AlaRipngInterfacePacketsSent_Object=MibTableColumn
alaRipngInterfacePacketsSent=_AlaRipngInterfacePacketsSent_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,7),_AlaRipngInterfacePacketsSent_Type())
alaRipngInterfacePacketsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngInterfacePacketsSent.setStatus(_A)
_AlaRipngInterfacePacketsRcvd_Type=Integer32
_AlaRipngInterfacePacketsRcvd_Object=MibTableColumn
alaRipngInterfacePacketsRcvd=_AlaRipngInterfacePacketsRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,8),_AlaRipngInterfacePacketsRcvd_Type())
alaRipngInterfacePacketsRcvd.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngInterfacePacketsRcvd.setStatus(_A)
_AlaRipngInterfaceMTU_Type=Counter32
_AlaRipngInterfaceMTU_Object=MibTableColumn
alaRipngInterfaceMTU=_AlaRipngInterfaceMTU_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,9),_AlaRipngInterfaceMTU_Type())
alaRipngInterfaceMTU.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngInterfaceMTU.setStatus(_A)
_AlaRipngInterfaceNextUpdate_Type=TimeTicks
_AlaRipngInterfaceNextUpdate_Object=MibTableColumn
alaRipngInterfaceNextUpdate=_AlaRipngInterfaceNextUpdate_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,11,1,10),_AlaRipngInterfaceNextUpdate_Type())
alaRipngInterfaceNextUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngInterfaceNextUpdate.setStatus(_A)
_AlaRipngPeerTable_Object=MibTable
alaRipngPeerTable=_AlaRipngPeerTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15))
if mibBuilder.loadTexts:alaRipngPeerTable.setStatus(_A)
_AlaRipngPeerEntry_Object=MibTableRow
alaRipngPeerEntry=_AlaRipngPeerEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1))
alaRipngPeerEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:alaRipngPeerEntry.setStatus(_A)
_AlaRipngPeerAddress_Type=Ipv6Address
_AlaRipngPeerAddress_Object=MibTableColumn
alaRipngPeerAddress=_AlaRipngPeerAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,1),_AlaRipngPeerAddress_Type())
alaRipngPeerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerAddress.setStatus(_A)
class _AlaRipngPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaRipngPeerIndex_Type.__name__=_C
_AlaRipngPeerIndex_Object=MibTableColumn
alaRipngPeerIndex=_AlaRipngPeerIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,2),_AlaRipngPeerIndex_Type())
alaRipngPeerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngPeerIndex.setStatus(_A)
_AlaRipngPeerLastUpdate_Type=TimeTicks
_AlaRipngPeerLastUpdate_Object=MibTableColumn
alaRipngPeerLastUpdate=_AlaRipngPeerLastUpdate_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,3),_AlaRipngPeerLastUpdate_Type())
alaRipngPeerLastUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngPeerLastUpdate.setStatus(_A)
_AlaRipngPeerNumUpdates_Type=Counter32
_AlaRipngPeerNumUpdates_Object=MibTableColumn
alaRipngPeerNumUpdates=_AlaRipngPeerNumUpdates_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,4),_AlaRipngPeerNumUpdates_Type())
alaRipngPeerNumUpdates.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngPeerNumUpdates.setStatus(_A)
_AlaRipngPeerNumRoutes_Type=Counter32
_AlaRipngPeerNumRoutes_Object=MibTableColumn
alaRipngPeerNumRoutes=_AlaRipngPeerNumRoutes_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,5),_AlaRipngPeerNumRoutes_Type())
alaRipngPeerNumRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngPeerNumRoutes.setStatus(_A)
_AlaRipngPeerBadPackets_Type=Counter32
_AlaRipngPeerBadPackets_Object=MibTableColumn
alaRipngPeerBadPackets=_AlaRipngPeerBadPackets_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,6),_AlaRipngPeerBadPackets_Type())
alaRipngPeerBadPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngPeerBadPackets.setStatus(_A)
_AlaRipngPeerBadRoutes_Type=Counter32
_AlaRipngPeerBadRoutes_Object=MibTableColumn
alaRipngPeerBadRoutes=_AlaRipngPeerBadRoutes_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,15,1,7),_AlaRipngPeerBadRoutes_Type())
alaRipngPeerBadRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngPeerBadRoutes.setStatus(_A)
_AlaRipngRouteTable_Object=MibTable
alaRipngRouteTable=_AlaRipngRouteTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16))
if mibBuilder.loadTexts:alaRipngRouteTable.setStatus(_A)
_AlaRipngRouteEntry_Object=MibTableRow
alaRipngRouteEntry=_AlaRipngRouteEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1))
alaRipngRouteEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:alaRipngRouteEntry.setStatus(_A)
_AlaRipngRoutePrefix_Type=Ipv6AddressPrefix
_AlaRipngRoutePrefix_Object=MibTableColumn
alaRipngRoutePrefix=_AlaRipngRoutePrefix_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,1),_AlaRipngRoutePrefix_Type())
alaRipngRoutePrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRoutePrefix.setStatus(_A)
class _AlaRipngRoutePrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaRipngRoutePrefixLen_Type.__name__=_C
_AlaRipngRoutePrefixLen_Object=MibTableColumn
alaRipngRoutePrefixLen=_AlaRipngRoutePrefixLen_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,2),_AlaRipngRoutePrefixLen_Type())
alaRipngRoutePrefixLen.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRoutePrefixLen.setStatus(_A)
_AlaRipngRouteNextHop_Type=Ipv6Address
_AlaRipngRouteNextHop_Object=MibTableColumn
alaRipngRouteNextHop=_AlaRipngRouteNextHop_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,3),_AlaRipngRouteNextHop_Type())
alaRipngRouteNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:alaRipngRouteNextHop.setStatus(_A)
class _AlaRipngRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('rip',2),('redist',3),(_R,4)))
_AlaRipngRouteType_Type.__name__=_C
_AlaRipngRouteType_Object=MibTableColumn
alaRipngRouteType=_AlaRipngRouteType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,4),_AlaRipngRouteType_Type())
alaRipngRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteType.setStatus(_A)
_AlaRipngRouteAge_Type=TimeTicks
_AlaRipngRouteAge_Object=MibTableColumn
alaRipngRouteAge=_AlaRipngRouteAge_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,5),_AlaRipngRouteAge_Type())
alaRipngRouteAge.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteAge.setStatus(_A)
class _AlaRipngRouteTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaRipngRouteTag_Type.__name__=_C
_AlaRipngRouteTag_Object=MibTableColumn
alaRipngRouteTag=_AlaRipngRouteTag_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,6),_AlaRipngRouteTag_Type())
alaRipngRouteTag.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteTag.setStatus(_A)
class _AlaRipngRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AlaRipngRouteMetric_Type.__name__=_C
_AlaRipngRouteMetric_Object=MibTableColumn
alaRipngRouteMetric=_AlaRipngRouteMetric_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,7),_AlaRipngRouteMetric_Type())
alaRipngRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteMetric.setStatus(_A)
class _AlaRipngRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),(_S,1)))
_AlaRipngRouteStatus_Type.__name__=_C
_AlaRipngRouteStatus_Object=MibTableColumn
alaRipngRouteStatus=_AlaRipngRouteStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,8),_AlaRipngRouteStatus_Type())
alaRipngRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteStatus.setStatus(_A)
class _AlaRipngRouteFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('garbage',2),('holddown',3),(_R,4)))
_AlaRipngRouteFlags_Type.__name__=_C
_AlaRipngRouteFlags_Object=MibTableColumn
alaRipngRouteFlags=_AlaRipngRouteFlags_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,9),_AlaRipngRouteFlags_Type())
alaRipngRouteFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteFlags.setStatus(_A)
_AlaRipngRouteIndex_Type=Integer32
_AlaRipngRouteIndex_Object=MibTableColumn
alaRipngRouteIndex=_AlaRipngRouteIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,1,1,16,1,10),_AlaRipngRouteIndex_Type())
alaRipngRouteIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:alaRipngRouteIndex.setStatus(_A)
_AlcatelIND1RIPNGMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBConformance=_AlcatelIND1RIPNGMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBConformance.setStatus(_A)
_AlcatelIND1RIPNGMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBGroups=_AlcatelIND1RIPNGMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,1))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBGroups.setStatus(_A)
_AlcatelIND1RIPNGMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGMIBCompliances=_AlcatelIND1RIPNGMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,2))
if mibBuilder.loadTexts:alcatelIND1RIPNGMIBCompliances.setStatus(_A)
_AlcatelIND1RIPNGTraps_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGTraps=_AlcatelIND1RIPNGTraps_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,3))
_AlcatelIND1RIPNGTrapsRoot_ObjectIdentity=ObjectIdentity
alcatelIND1RIPNGTrapsRoot=_AlcatelIND1RIPNGTrapsRoot_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,3,0))
alaRipngGlobalGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,1,1))
alaRipngGlobalGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:alaRipngGlobalGroup.setStatus(_A)
alaRipngInterfaceGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,1,3))
alaRipngInterfaceGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaRipngInterfaceGroup.setStatus(_A)
alaRipngPeerGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,1,7))
alaRipngPeerGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alaRipngPeerGroup.setStatus(_A)
alaRipngRouteGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,1,8))
alaRipngRouteGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:alaRipngRouteGroup.setStatus(_A)
ripngRouteMaxLimitReached=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,3,0,1))
if mibBuilder.loadTexts:ripngRouteMaxLimitReached.setStatus(_A)
alcatelIND1RIPNGTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,1,9))
alcatelIND1RIPNGTrapsGroup.setObjects((_B,_y))
if mibBuilder.loadTexts:alcatelIND1RIPNGTrapsGroup.setStatus(_A)
alcatelIND1RIPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,12,1,2,2,1))
alcatelIND1RIPMIBCompliance.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:alcatelIND1RIPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1RIPNGMIB':alcatelIND1RIPNGMIB,'alcatelIND1RIPNGMIBObjects':alcatelIND1RIPNGMIBObjects,'alaProtocolRipng':alaProtocolRipng,_T:alaRipngProtoStatus,_U:alaRipngUpdateInterval,_V:alaRipngInvalidTimer,_W:alaRipngHolddownTimer,_X:alaRipngGarbageTimer,_Y:alaRipngRouteCount,_Z:alaRipngGlobalRouteTag,_a:alaRipngTriggeredSends,_b:alaRipngJitter,_c:alaRipngPort,'alaRipngInterfaceTable':alaRipngInterfaceTable,'alaRipngInterfaceEntry':alaRipngInterfaceEntry,_J:alaRipngInterfaceIndex,_d:alaRipngInterfaceStatus,_e:alaRipngInterfaceMetric,_f:alaRipngInterfaceRecvStatus,_g:alaRipngInterfaceSendStatus,_h:alaRipngInterfaceHorizon,_i:alaRipngInterfacePacketsSent,_j:alaRipngInterfacePacketsRcvd,_k:alaRipngInterfaceMTU,_l:alaRipngInterfaceNextUpdate,'alaRipngPeerTable':alaRipngPeerTable,'alaRipngPeerEntry':alaRipngPeerEntry,_M:alaRipngPeerAddress,_N:alaRipngPeerIndex,_m:alaRipngPeerLastUpdate,_n:alaRipngPeerNumUpdates,_o:alaRipngPeerNumRoutes,_p:alaRipngPeerBadPackets,_q:alaRipngPeerBadRoutes,'alaRipngRouteTable':alaRipngRouteTable,'alaRipngRouteEntry':alaRipngRouteEntry,_O:alaRipngRoutePrefix,_P:alaRipngRoutePrefixLen,_Q:alaRipngRouteNextHop,_r:alaRipngRouteType,_s:alaRipngRouteAge,_t:alaRipngRouteTag,_u:alaRipngRouteMetric,_v:alaRipngRouteStatus,_w:alaRipngRouteFlags,_x:alaRipngRouteIndex,'alcatelIND1RIPNGMIBConformance':alcatelIND1RIPNGMIBConformance,'alcatelIND1RIPNGMIBGroups':alcatelIND1RIPNGMIBGroups,_z:alaRipngGlobalGroup,_A0:alaRipngInterfaceGroup,_A1:alaRipngPeerGroup,_A2:alaRipngRouteGroup,'alcatelIND1RIPNGTrapsGroup':alcatelIND1RIPNGTrapsGroup,'alcatelIND1RIPNGMIBCompliances':alcatelIND1RIPNGMIBCompliances,'alcatelIND1RIPMIBCompliance':alcatelIND1RIPMIBCompliance,'alcatelIND1RIPNGTraps':alcatelIND1RIPNGTraps,'alcatelIND1RIPNGTrapsRoot':alcatelIND1RIPNGTrapsRoot,_y:ripngRouteMaxLimitReached})