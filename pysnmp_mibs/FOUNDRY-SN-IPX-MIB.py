_j='snIpxPortCountersPort'
_i='snIpxPortAddrEncap'
_h='snIpxPortAddrPort'
_g='snIpxIfSapAccessDir'
_f='snIpxIfSapAccessPort'
_e='snIpxIfRipAccessDir'
_d='snIpxIfRipAccessPort'
_c='snIpxIfFwdAccessDir'
_b='snIpxIfFwdAccessPort'
_a='snIpxSapFilterId'
_Z='snIpxRipFilterId'
_Y='snIpxFwdFilterIdx'
_X='snIpxServerIndex'
_W='snIpxRouteIndex'
_V='ethernetSnap'
_U='ethernet8023'
_T='ethernet8022'
_S='ethernetII'
_R='snIpxCacheIndex'
_Q='addAllOutBound'
_P='addAllInBound'
_O='deleteAllOutBound'
_N='deleteAllInBound'
_M='PhysAddress'
_L='out'
_K='modify'
_J='create'
_I='delete'
_H='invalid'
_G='OctetString'
_F='valid'
_E='Integer32'
_D='FOUNDRY-SN-IPX-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
router,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','router')
PhysAddress,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_M,'TextualConvention')
snIpx=ModuleIdentity((1,3,6,1,4,1,1991,1,2,1))
if mibBuilder.loadTexts:snIpx.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
class RtrStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class ClearStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('clear',1)))
class PortIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3900))
class Action(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
class NetNumber(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SnIpxGen_ObjectIdentity=ObjectIdentity
snIpxGen=_SnIpxGen_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,1))
_SnIpxRoutingMode_Type=RtrStatus
_SnIpxRoutingMode_Object=MibScalar
snIpxRoutingMode=_SnIpxRoutingMode_Object((1,3,6,1,4,1,1991,1,2,1,1,1),_SnIpxRoutingMode_Type())
snIpxRoutingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRoutingMode.setStatus(_A)
_SnIpxNetBiosFilterMode_Type=RtrStatus
_SnIpxNetBiosFilterMode_Object=MibScalar
snIpxNetBiosFilterMode=_SnIpxNetBiosFilterMode_Object((1,3,6,1,4,1,1991,1,2,1,1,2),_SnIpxNetBiosFilterMode_Type())
snIpxNetBiosFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxNetBiosFilterMode.setStatus(_A)
_SnIpxClearCache_Type=ClearStatus
_SnIpxClearCache_Object=MibScalar
snIpxClearCache=_SnIpxClearCache_Object((1,3,6,1,4,1,1991,1,2,1,1,3),_SnIpxClearCache_Type())
snIpxClearCache.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxClearCache.setStatus(_A)
_SnIpxClearRoute_Type=ClearStatus
_SnIpxClearRoute_Object=MibScalar
snIpxClearRoute=_SnIpxClearRoute_Object((1,3,6,1,4,1,1991,1,2,1,1,4),_SnIpxClearRoute_Type())
snIpxClearRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxClearRoute.setStatus(_A)
_SnIpxClearTrafficCnts_Type=ClearStatus
_SnIpxClearTrafficCnts_Object=MibScalar
snIpxClearTrafficCnts=_SnIpxClearTrafficCnts_Object((1,3,6,1,4,1,1991,1,2,1,1,5),_SnIpxClearTrafficCnts_Type())
snIpxClearTrafficCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxClearTrafficCnts.setStatus(_A)
_SnIpxRcvPktsCnt_Type=Counter32
_SnIpxRcvPktsCnt_Object=MibScalar
snIpxRcvPktsCnt=_SnIpxRcvPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,6),_SnIpxRcvPktsCnt_Type())
snIpxRcvPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxRcvPktsCnt.setStatus(_A)
_SnIpxTxPktsCnt_Type=Counter32
_SnIpxTxPktsCnt_Object=MibScalar
snIpxTxPktsCnt=_SnIpxTxPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,7),_SnIpxTxPktsCnt_Type())
snIpxTxPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxTxPktsCnt.setStatus(_A)
_SnIpxFwdPktsCnt_Type=Counter32
_SnIpxFwdPktsCnt_Object=MibScalar
snIpxFwdPktsCnt=_SnIpxFwdPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,8),_SnIpxFwdPktsCnt_Type())
snIpxFwdPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxFwdPktsCnt.setStatus(_A)
_SnIpxRcvDropPktsCnt_Type=Counter32
_SnIpxRcvDropPktsCnt_Object=MibScalar
snIpxRcvDropPktsCnt=_SnIpxRcvDropPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,9),_SnIpxRcvDropPktsCnt_Type())
snIpxRcvDropPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxRcvDropPktsCnt.setStatus(_A)
_SnIpxRcvFiltPktsCnt_Type=Counter32
_SnIpxRcvFiltPktsCnt_Object=MibScalar
snIpxRcvFiltPktsCnt=_SnIpxRcvFiltPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,10),_SnIpxRcvFiltPktsCnt_Type())
snIpxRcvFiltPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxRcvFiltPktsCnt.setStatus(_A)
class _SnIpxRipGblFiltList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnIpxRipGblFiltList_Type.__name__=_G
_SnIpxRipGblFiltList_Object=MibScalar
snIpxRipGblFiltList=_SnIpxRipGblFiltList_Object((1,3,6,1,4,1,1991,1,2,1,1,11),_SnIpxRipGblFiltList_Type())
snIpxRipGblFiltList.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRipGblFiltList.setStatus(_A)
class _SnIpxRipFiltOnAllPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_SnIpxRipFiltOnAllPort_Type.__name__=_E
_SnIpxRipFiltOnAllPort_Object=MibScalar
snIpxRipFiltOnAllPort=_SnIpxRipFiltOnAllPort_Object((1,3,6,1,4,1,1991,1,2,1,1,12),_SnIpxRipFiltOnAllPort_Type())
snIpxRipFiltOnAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRipFiltOnAllPort.setStatus(_A)
class _SnIpxSapGblFiltList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnIpxSapGblFiltList_Type.__name__=_G
_SnIpxSapGblFiltList_Object=MibScalar
snIpxSapGblFiltList=_SnIpxSapGblFiltList_Object((1,3,6,1,4,1,1991,1,2,1,1,13),_SnIpxSapGblFiltList_Type())
snIpxSapGblFiltList.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxSapGblFiltList.setStatus(_A)
class _SnIpxSapFiltOnAllPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_SnIpxSapFiltOnAllPort_Type.__name__=_E
_SnIpxSapFiltOnAllPort_Object=MibScalar
snIpxSapFiltOnAllPort=_SnIpxSapFiltOnAllPort_Object((1,3,6,1,4,1,1991,1,2,1,1,14),_SnIpxSapFiltOnAllPort_Type())
snIpxSapFiltOnAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxSapFiltOnAllPort.setStatus(_A)
_SnIpxTxDropPktsCnt_Type=Counter32
_SnIpxTxDropPktsCnt_Object=MibScalar
snIpxTxDropPktsCnt=_SnIpxTxDropPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,15),_SnIpxTxDropPktsCnt_Type())
snIpxTxDropPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxTxDropPktsCnt.setStatus(_A)
_SnIpxTxFiltPktsCnt_Type=Counter32
_SnIpxTxFiltPktsCnt_Object=MibScalar
snIpxTxFiltPktsCnt=_SnIpxTxFiltPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,1,16),_SnIpxTxFiltPktsCnt_Type())
snIpxTxFiltPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxTxFiltPktsCnt.setStatus(_A)
_SnIpxCache_ObjectIdentity=ObjectIdentity
snIpxCache=_SnIpxCache_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,2))
_SnIpxCacheTable_Object=MibTable
snIpxCacheTable=_SnIpxCacheTable_Object((1,3,6,1,4,1,1991,1,2,1,2,1))
if mibBuilder.loadTexts:snIpxCacheTable.setStatus(_A)
_SnIpxCacheEntry_Object=MibTableRow
snIpxCacheEntry=_SnIpxCacheEntry_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1))
snIpxCacheEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:snIpxCacheEntry.setStatus(_A)
_SnIpxCacheIndex_Type=Integer32
_SnIpxCacheIndex_Object=MibTableColumn
snIpxCacheIndex=_SnIpxCacheIndex_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1,1),_SnIpxCacheIndex_Type())
snIpxCacheIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxCacheIndex.setStatus(_A)
_SnIpxCacheNetNum_Type=NetNumber
_SnIpxCacheNetNum_Object=MibTableColumn
snIpxCacheNetNum=_SnIpxCacheNetNum_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1,2),_SnIpxCacheNetNum_Type())
snIpxCacheNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxCacheNetNum.setStatus(_A)
_SnIpxCacheNode_Type=PhysAddress
_SnIpxCacheNode_Object=MibTableColumn
snIpxCacheNode=_SnIpxCacheNode_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1,3),_SnIpxCacheNode_Type())
snIpxCacheNode.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxCacheNode.setStatus(_A)
_SnIpxCacheOutFilter_Type=RtrStatus
_SnIpxCacheOutFilter_Object=MibTableColumn
snIpxCacheOutFilter=_SnIpxCacheOutFilter_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1,4),_SnIpxCacheOutFilter_Type())
snIpxCacheOutFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxCacheOutFilter.setStatus(_A)
class _SnIpxCacheEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4)))
_SnIpxCacheEncap_Type.__name__=_E
_SnIpxCacheEncap_Object=MibTableColumn
snIpxCacheEncap=_SnIpxCacheEncap_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1,5),_SnIpxCacheEncap_Type())
snIpxCacheEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxCacheEncap.setStatus(_A)
_SnIpxCachePort_Type=PortIndex
_SnIpxCachePort_Object=MibTableColumn
snIpxCachePort=_SnIpxCachePort_Object((1,3,6,1,4,1,1991,1,2,1,2,1,1,6),_SnIpxCachePort_Type())
snIpxCachePort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxCachePort.setStatus(_A)
_SnIpxRoute_ObjectIdentity=ObjectIdentity
snIpxRoute=_SnIpxRoute_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,3))
_SnIpxRouteTable_Object=MibTable
snIpxRouteTable=_SnIpxRouteTable_Object((1,3,6,1,4,1,1991,1,2,1,3,1))
if mibBuilder.loadTexts:snIpxRouteTable.setStatus(_A)
_SnIpxRouteEntry_Object=MibTableRow
snIpxRouteEntry=_SnIpxRouteEntry_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1))
snIpxRouteEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:snIpxRouteEntry.setStatus(_A)
_SnIpxRouteIndex_Type=Integer32
_SnIpxRouteIndex_Object=MibTableColumn
snIpxRouteIndex=_SnIpxRouteIndex_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1,1),_SnIpxRouteIndex_Type())
snIpxRouteIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxRouteIndex.setStatus(_A)
_SnIpxDestNetNum_Type=NetNumber
_SnIpxDestNetNum_Object=MibTableColumn
snIpxDestNetNum=_SnIpxDestNetNum_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1,2),_SnIpxDestNetNum_Type())
snIpxDestNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxDestNetNum.setStatus(_A)
_SnIpxFwdRouterNode_Type=PhysAddress
_SnIpxFwdRouterNode_Object=MibTableColumn
snIpxFwdRouterNode=_SnIpxFwdRouterNode_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1,3),_SnIpxFwdRouterNode_Type())
snIpxFwdRouterNode.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxFwdRouterNode.setStatus(_A)
_SnIpxDestHopCnts_Type=Integer32
_SnIpxDestHopCnts_Object=MibTableColumn
snIpxDestHopCnts=_SnIpxDestHopCnts_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1,4),_SnIpxDestHopCnts_Type())
snIpxDestHopCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxDestHopCnts.setStatus(_A)
_SnIpxRouteMetric_Type=Integer32
_SnIpxRouteMetric_Object=MibTableColumn
snIpxRouteMetric=_SnIpxRouteMetric_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1,5),_SnIpxRouteMetric_Type())
snIpxRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxRouteMetric.setStatus(_A)
_SnIpxDestPort_Type=Integer32
_SnIpxDestPort_Object=MibTableColumn
snIpxDestPort=_SnIpxDestPort_Object((1,3,6,1,4,1,1991,1,2,1,3,1,1,6),_SnIpxDestPort_Type())
snIpxDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxDestPort.setStatus(_A)
_SnIpxServer_ObjectIdentity=ObjectIdentity
snIpxServer=_SnIpxServer_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,4))
_SnIpxServerTable_Object=MibTable
snIpxServerTable=_SnIpxServerTable_Object((1,3,6,1,4,1,1991,1,2,1,4,1))
if mibBuilder.loadTexts:snIpxServerTable.setStatus(_A)
_SnIpxServerEntry_Object=MibTableRow
snIpxServerEntry=_SnIpxServerEntry_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1))
snIpxServerEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:snIpxServerEntry.setStatus(_A)
_SnIpxServerIndex_Type=Integer32
_SnIpxServerIndex_Object=MibTableColumn
snIpxServerIndex=_SnIpxServerIndex_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,1),_SnIpxServerIndex_Type())
snIpxServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerIndex.setStatus(_A)
_SnIpxServerType_Type=Integer32
_SnIpxServerType_Object=MibTableColumn
snIpxServerType=_SnIpxServerType_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,2),_SnIpxServerType_Type())
snIpxServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerType.setStatus(_A)
_SnIpxServerNetNum_Type=NetNumber
_SnIpxServerNetNum_Object=MibTableColumn
snIpxServerNetNum=_SnIpxServerNetNum_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,3),_SnIpxServerNetNum_Type())
snIpxServerNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerNetNum.setStatus(_A)
_SnIpxServerNode_Type=PhysAddress
_SnIpxServerNode_Object=MibTableColumn
snIpxServerNode=_SnIpxServerNode_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,4),_SnIpxServerNode_Type())
snIpxServerNode.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerNode.setStatus(_A)
_SnIpxServerSocket_Type=Integer32
_SnIpxServerSocket_Object=MibTableColumn
snIpxServerSocket=_SnIpxServerSocket_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,5),_SnIpxServerSocket_Type())
snIpxServerSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerSocket.setStatus(_A)
_SnIpxServerHopCnts_Type=Integer32
_SnIpxServerHopCnts_Object=MibTableColumn
snIpxServerHopCnts=_SnIpxServerHopCnts_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,6),_SnIpxServerHopCnts_Type())
snIpxServerHopCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerHopCnts.setStatus(_A)
class _SnIpxServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_SnIpxServerName_Type.__name__=_G
_SnIpxServerName_Object=MibTableColumn
snIpxServerName=_SnIpxServerName_Object((1,3,6,1,4,1,1991,1,2,1,4,1,1,7),_SnIpxServerName_Type())
snIpxServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxServerName.setStatus(_A)
_SnIpxFwdFilter_ObjectIdentity=ObjectIdentity
snIpxFwdFilter=_SnIpxFwdFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,5))
_SnIpxFwdFilterTable_Object=MibTable
snIpxFwdFilterTable=_SnIpxFwdFilterTable_Object((1,3,6,1,4,1,1991,1,2,1,5,1))
if mibBuilder.loadTexts:snIpxFwdFilterTable.setStatus(_A)
_SnIpxFwdFilterEntry_Object=MibTableRow
snIpxFwdFilterEntry=_SnIpxFwdFilterEntry_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1))
snIpxFwdFilterEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:snIpxFwdFilterEntry.setStatus(_A)
_SnIpxFwdFilterIdx_Type=Integer32
_SnIpxFwdFilterIdx_Object=MibTableColumn
snIpxFwdFilterIdx=_SnIpxFwdFilterIdx_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,1),_SnIpxFwdFilterIdx_Type())
snIpxFwdFilterIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxFwdFilterIdx.setStatus(_A)
_SnIpxFwdFilterAction_Type=Action
_SnIpxFwdFilterAction_Object=MibTableColumn
snIpxFwdFilterAction=_SnIpxFwdFilterAction_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,2),_SnIpxFwdFilterAction_Type())
snIpxFwdFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterAction.setStatus(_A)
_SnIpxFwdFilterSocket_Type=Integer32
_SnIpxFwdFilterSocket_Object=MibTableColumn
snIpxFwdFilterSocket=_SnIpxFwdFilterSocket_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,3),_SnIpxFwdFilterSocket_Type())
snIpxFwdFilterSocket.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterSocket.setStatus(_A)
_SnIpxFwdFilterSrcNet_Type=NetNumber
_SnIpxFwdFilterSrcNet_Object=MibTableColumn
snIpxFwdFilterSrcNet=_SnIpxFwdFilterSrcNet_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,4),_SnIpxFwdFilterSrcNet_Type())
snIpxFwdFilterSrcNet.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterSrcNet.setStatus(_A)
_SnIpxFwdFilterSrcNode_Type=PhysAddress
_SnIpxFwdFilterSrcNode_Object=MibTableColumn
snIpxFwdFilterSrcNode=_SnIpxFwdFilterSrcNode_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,5),_SnIpxFwdFilterSrcNode_Type())
snIpxFwdFilterSrcNode.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterSrcNode.setStatus(_A)
_SnIpxFwdFilterDestNet_Type=NetNumber
_SnIpxFwdFilterDestNet_Object=MibTableColumn
snIpxFwdFilterDestNet=_SnIpxFwdFilterDestNet_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,6),_SnIpxFwdFilterDestNet_Type())
snIpxFwdFilterDestNet.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterDestNet.setStatus(_A)
_SnIpxFwdFilterDestNode_Type=PhysAddress
_SnIpxFwdFilterDestNode_Object=MibTableColumn
snIpxFwdFilterDestNode=_SnIpxFwdFilterDestNode_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,7),_SnIpxFwdFilterDestNode_Type())
snIpxFwdFilterDestNode.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterDestNode.setStatus(_A)
class _SnIpxFwdFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxFwdFilterRowStatus_Type.__name__=_E
_SnIpxFwdFilterRowStatus_Object=MibTableColumn
snIpxFwdFilterRowStatus=_SnIpxFwdFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,5,1,1,8),_SnIpxFwdFilterRowStatus_Type())
snIpxFwdFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxFwdFilterRowStatus.setStatus(_A)
_SnIpxRipFilter_ObjectIdentity=ObjectIdentity
snIpxRipFilter=_SnIpxRipFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,6))
_SnIpxRipFilterTable_Object=MibTable
snIpxRipFilterTable=_SnIpxRipFilterTable_Object((1,3,6,1,4,1,1991,1,2,1,6,1))
if mibBuilder.loadTexts:snIpxRipFilterTable.setStatus(_A)
_SnIpxRipFilterEntry_Object=MibTableRow
snIpxRipFilterEntry=_SnIpxRipFilterEntry_Object((1,3,6,1,4,1,1991,1,2,1,6,1,1))
snIpxRipFilterEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:snIpxRipFilterEntry.setStatus(_A)
_SnIpxRipFilterId_Type=Integer32
_SnIpxRipFilterId_Object=MibTableColumn
snIpxRipFilterId=_SnIpxRipFilterId_Object((1,3,6,1,4,1,1991,1,2,1,6,1,1,1),_SnIpxRipFilterId_Type())
snIpxRipFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxRipFilterId.setStatus(_A)
_SnIpxRipFilterAction_Type=Action
_SnIpxRipFilterAction_Object=MibTableColumn
snIpxRipFilterAction=_SnIpxRipFilterAction_Object((1,3,6,1,4,1,1991,1,2,1,6,1,1,2),_SnIpxRipFilterAction_Type())
snIpxRipFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRipFilterAction.setStatus(_A)
_SnIpxRipFilterNet_Type=NetNumber
_SnIpxRipFilterNet_Object=MibTableColumn
snIpxRipFilterNet=_SnIpxRipFilterNet_Object((1,3,6,1,4,1,1991,1,2,1,6,1,1,3),_SnIpxRipFilterNet_Type())
snIpxRipFilterNet.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRipFilterNet.setStatus(_A)
_SnIpxRipFilterMask_Type=NetNumber
_SnIpxRipFilterMask_Object=MibTableColumn
snIpxRipFilterMask=_SnIpxRipFilterMask_Object((1,3,6,1,4,1,1991,1,2,1,6,1,1,4),_SnIpxRipFilterMask_Type())
snIpxRipFilterMask.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRipFilterMask.setStatus(_A)
class _SnIpxRipFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxRipFilterRowStatus_Type.__name__=_E
_SnIpxRipFilterRowStatus_Object=MibTableColumn
snIpxRipFilterRowStatus=_SnIpxRipFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,6,1,1,5),_SnIpxRipFilterRowStatus_Type())
snIpxRipFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxRipFilterRowStatus.setStatus(_A)
_SnIpxSapFilter_ObjectIdentity=ObjectIdentity
snIpxSapFilter=_SnIpxSapFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,7))
_SnIpxSapFilterTable_Object=MibTable
snIpxSapFilterTable=_SnIpxSapFilterTable_Object((1,3,6,1,4,1,1991,1,2,1,7,1))
if mibBuilder.loadTexts:snIpxSapFilterTable.setStatus(_A)
_SnIpxSapFilterEntry_Object=MibTableRow
snIpxSapFilterEntry=_SnIpxSapFilterEntry_Object((1,3,6,1,4,1,1991,1,2,1,7,1,1))
snIpxSapFilterEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:snIpxSapFilterEntry.setStatus(_A)
_SnIpxSapFilterId_Type=Integer32
_SnIpxSapFilterId_Object=MibTableColumn
snIpxSapFilterId=_SnIpxSapFilterId_Object((1,3,6,1,4,1,1991,1,2,1,7,1,1,1),_SnIpxSapFilterId_Type())
snIpxSapFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxSapFilterId.setStatus(_A)
_SnIpxSapFilterAction_Type=Action
_SnIpxSapFilterAction_Object=MibTableColumn
snIpxSapFilterAction=_SnIpxSapFilterAction_Object((1,3,6,1,4,1,1991,1,2,1,7,1,1,2),_SnIpxSapFilterAction_Type())
snIpxSapFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxSapFilterAction.setStatus(_A)
_SnIpxSapFilterType_Type=Integer32
_SnIpxSapFilterType_Object=MibTableColumn
snIpxSapFilterType=_SnIpxSapFilterType_Object((1,3,6,1,4,1,1991,1,2,1,7,1,1,3),_SnIpxSapFilterType_Type())
snIpxSapFilterType.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxSapFilterType.setStatus(_A)
class _SnIpxSapFilterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_SnIpxSapFilterName_Type.__name__=_G
_SnIpxSapFilterName_Object=MibTableColumn
snIpxSapFilterName=_SnIpxSapFilterName_Object((1,3,6,1,4,1,1991,1,2,1,7,1,1,4),_SnIpxSapFilterName_Type())
snIpxSapFilterName.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxSapFilterName.setStatus(_A)
class _SnIpxSapFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxSapFilterRowStatus_Type.__name__=_E
_SnIpxSapFilterRowStatus_Object=MibTableColumn
snIpxSapFilterRowStatus=_SnIpxSapFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,7,1,1,5),_SnIpxSapFilterRowStatus_Type())
snIpxSapFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxSapFilterRowStatus.setStatus(_A)
_SnIpxIfFwdAccess_ObjectIdentity=ObjectIdentity
snIpxIfFwdAccess=_SnIpxIfFwdAccess_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,8))
_SnIpxIfFwdAccessTable_Object=MibTable
snIpxIfFwdAccessTable=_SnIpxIfFwdAccessTable_Object((1,3,6,1,4,1,1991,1,2,1,8,1))
if mibBuilder.loadTexts:snIpxIfFwdAccessTable.setStatus(_A)
_SnIpxIfFwdAccessEntry_Object=MibTableRow
snIpxIfFwdAccessEntry=_SnIpxIfFwdAccessEntry_Object((1,3,6,1,4,1,1991,1,2,1,8,1,1))
snIpxIfFwdAccessEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:snIpxIfFwdAccessEntry.setStatus(_A)
_SnIpxIfFwdAccessPort_Type=Integer32
_SnIpxIfFwdAccessPort_Object=MibTableColumn
snIpxIfFwdAccessPort=_SnIpxIfFwdAccessPort_Object((1,3,6,1,4,1,1991,1,2,1,8,1,1,1),_SnIpxIfFwdAccessPort_Type())
snIpxIfFwdAccessPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxIfFwdAccessPort.setStatus(_A)
class _SnIpxIfFwdAccessDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),(_L,2)))
_SnIpxIfFwdAccessDir_Type.__name__=_E
_SnIpxIfFwdAccessDir_Object=MibTableColumn
snIpxIfFwdAccessDir=_SnIpxIfFwdAccessDir_Object((1,3,6,1,4,1,1991,1,2,1,8,1,1,2),_SnIpxIfFwdAccessDir_Type())
snIpxIfFwdAccessDir.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxIfFwdAccessDir.setStatus(_A)
class _SnIpxIfFwdAccessFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SnIpxIfFwdAccessFilterList_Type.__name__=_G
_SnIpxIfFwdAccessFilterList_Object=MibTableColumn
snIpxIfFwdAccessFilterList=_SnIpxIfFwdAccessFilterList_Object((1,3,6,1,4,1,1991,1,2,1,8,1,1,3),_SnIpxIfFwdAccessFilterList_Type())
snIpxIfFwdAccessFilterList.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxIfFwdAccessFilterList.setStatus(_A)
class _SnIpxIfFwdAccessRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxIfFwdAccessRowStatus_Type.__name__=_E
_SnIpxIfFwdAccessRowStatus_Object=MibTableColumn
snIpxIfFwdAccessRowStatus=_SnIpxIfFwdAccessRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,8,1,1,4),_SnIpxIfFwdAccessRowStatus_Type())
snIpxIfFwdAccessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxIfFwdAccessRowStatus.setStatus(_A)
_SnIpxIfRipAccess_ObjectIdentity=ObjectIdentity
snIpxIfRipAccess=_SnIpxIfRipAccess_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,9))
_SnIpxIfRipAccessTable_Object=MibTable
snIpxIfRipAccessTable=_SnIpxIfRipAccessTable_Object((1,3,6,1,4,1,1991,1,2,1,9,1))
if mibBuilder.loadTexts:snIpxIfRipAccessTable.setStatus(_A)
_SnIpxIfRipAccessEntry_Object=MibTableRow
snIpxIfRipAccessEntry=_SnIpxIfRipAccessEntry_Object((1,3,6,1,4,1,1991,1,2,1,9,1,1))
snIpxIfRipAccessEntry.setIndexNames((0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:snIpxIfRipAccessEntry.setStatus(_A)
_SnIpxIfRipAccessPort_Type=Integer32
_SnIpxIfRipAccessPort_Object=MibTableColumn
snIpxIfRipAccessPort=_SnIpxIfRipAccessPort_Object((1,3,6,1,4,1,1991,1,2,1,9,1,1,1),_SnIpxIfRipAccessPort_Type())
snIpxIfRipAccessPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxIfRipAccessPort.setStatus(_A)
class _SnIpxIfRipAccessDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),(_L,2)))
_SnIpxIfRipAccessDir_Type.__name__=_E
_SnIpxIfRipAccessDir_Object=MibTableColumn
snIpxIfRipAccessDir=_SnIpxIfRipAccessDir_Object((1,3,6,1,4,1,1991,1,2,1,9,1,1,2),_SnIpxIfRipAccessDir_Type())
snIpxIfRipAccessDir.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxIfRipAccessDir.setStatus(_A)
class _SnIpxIfRipAccessFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SnIpxIfRipAccessFilterList_Type.__name__=_G
_SnIpxIfRipAccessFilterList_Object=MibTableColumn
snIpxIfRipAccessFilterList=_SnIpxIfRipAccessFilterList_Object((1,3,6,1,4,1,1991,1,2,1,9,1,1,3),_SnIpxIfRipAccessFilterList_Type())
snIpxIfRipAccessFilterList.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxIfRipAccessFilterList.setStatus(_A)
class _SnIpxIfRipAccessRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxIfRipAccessRowStatus_Type.__name__=_E
_SnIpxIfRipAccessRowStatus_Object=MibTableColumn
snIpxIfRipAccessRowStatus=_SnIpxIfRipAccessRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,9,1,1,4),_SnIpxIfRipAccessRowStatus_Type())
snIpxIfRipAccessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxIfRipAccessRowStatus.setStatus(_A)
_SnIpxIfSapAccess_ObjectIdentity=ObjectIdentity
snIpxIfSapAccess=_SnIpxIfSapAccess_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,10))
_SnIpxIfSapAccessTable_Object=MibTable
snIpxIfSapAccessTable=_SnIpxIfSapAccessTable_Object((1,3,6,1,4,1,1991,1,2,1,10,1))
if mibBuilder.loadTexts:snIpxIfSapAccessTable.setStatus(_A)
_SnIpxIfSapAccessEntry_Object=MibTableRow
snIpxIfSapAccessEntry=_SnIpxIfSapAccessEntry_Object((1,3,6,1,4,1,1991,1,2,1,10,1,1))
snIpxIfSapAccessEntry.setIndexNames((0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:snIpxIfSapAccessEntry.setStatus(_A)
_SnIpxIfSapAccessPort_Type=Integer32
_SnIpxIfSapAccessPort_Object=MibTableColumn
snIpxIfSapAccessPort=_SnIpxIfSapAccessPort_Object((1,3,6,1,4,1,1991,1,2,1,10,1,1,1),_SnIpxIfSapAccessPort_Type())
snIpxIfSapAccessPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxIfSapAccessPort.setStatus(_A)
class _SnIpxIfSapAccessDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),(_L,2)))
_SnIpxIfSapAccessDir_Type.__name__=_E
_SnIpxIfSapAccessDir_Object=MibTableColumn
snIpxIfSapAccessDir=_SnIpxIfSapAccessDir_Object((1,3,6,1,4,1,1991,1,2,1,10,1,1,2),_SnIpxIfSapAccessDir_Type())
snIpxIfSapAccessDir.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxIfSapAccessDir.setStatus(_A)
class _SnIpxIfSapAccessFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SnIpxIfSapAccessFilterList_Type.__name__=_G
_SnIpxIfSapAccessFilterList_Object=MibTableColumn
snIpxIfSapAccessFilterList=_SnIpxIfSapAccessFilterList_Object((1,3,6,1,4,1,1991,1,2,1,10,1,1,3),_SnIpxIfSapAccessFilterList_Type())
snIpxIfSapAccessFilterList.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxIfSapAccessFilterList.setStatus(_A)
class _SnIpxIfSapAccessRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxIfSapAccessRowStatus_Type.__name__=_E
_SnIpxIfSapAccessRowStatus_Object=MibTableColumn
snIpxIfSapAccessRowStatus=_SnIpxIfSapAccessRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,10,1,1,4),_SnIpxIfSapAccessRowStatus_Type())
snIpxIfSapAccessRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxIfSapAccessRowStatus.setStatus(_A)
_SnIpxPortAddr_ObjectIdentity=ObjectIdentity
snIpxPortAddr=_SnIpxPortAddr_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,11))
_SnIpxPortAddrTable_Object=MibTable
snIpxPortAddrTable=_SnIpxPortAddrTable_Object((1,3,6,1,4,1,1991,1,2,1,11,1))
if mibBuilder.loadTexts:snIpxPortAddrTable.setStatus(_A)
_SnIpxPortAddrEntry_Object=MibTableRow
snIpxPortAddrEntry=_SnIpxPortAddrEntry_Object((1,3,6,1,4,1,1991,1,2,1,11,1,1))
snIpxPortAddrEntry.setIndexNames((0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:snIpxPortAddrEntry.setStatus(_A)
_SnIpxPortAddrPort_Type=PortIndex
_SnIpxPortAddrPort_Object=MibTableColumn
snIpxPortAddrPort=_SnIpxPortAddrPort_Object((1,3,6,1,4,1,1991,1,2,1,11,1,1,1),_SnIpxPortAddrPort_Type())
snIpxPortAddrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortAddrPort.setStatus(_A)
class _SnIpxPortAddrEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),(_U,2),(_S,3),(_V,4)))
_SnIpxPortAddrEncap_Type.__name__=_E
_SnIpxPortAddrEncap_Object=MibTableColumn
snIpxPortAddrEncap=_SnIpxPortAddrEncap_Object((1,3,6,1,4,1,1991,1,2,1,11,1,1,2),_SnIpxPortAddrEncap_Type())
snIpxPortAddrEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortAddrEncap.setStatus(_A)
_SnIpxPortAddrNetNum_Type=NetNumber
_SnIpxPortAddrNetNum_Object=MibTableColumn
snIpxPortAddrNetNum=_SnIpxPortAddrNetNum_Object((1,3,6,1,4,1,1991,1,2,1,11,1,1,3),_SnIpxPortAddrNetNum_Type())
snIpxPortAddrNetNum.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxPortAddrNetNum.setStatus(_A)
class _SnIpxPortAddrRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_F,2),(_I,3),(_J,4),(_K,5)))
_SnIpxPortAddrRowStatus_Type.__name__=_E
_SnIpxPortAddrRowStatus_Object=MibTableColumn
snIpxPortAddrRowStatus=_SnIpxPortAddrRowStatus_Object((1,3,6,1,4,1,1991,1,2,1,11,1,1,4),_SnIpxPortAddrRowStatus_Type())
snIpxPortAddrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxPortAddrRowStatus.setStatus(_A)
_SnIpxPortAddrNetBiosFilterMode_Type=RtrStatus
_SnIpxPortAddrNetBiosFilterMode_Object=MibTableColumn
snIpxPortAddrNetBiosFilterMode=_SnIpxPortAddrNetBiosFilterMode_Object((1,3,6,1,4,1,1991,1,2,1,11,1,1,5),_SnIpxPortAddrNetBiosFilterMode_Type())
snIpxPortAddrNetBiosFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snIpxPortAddrNetBiosFilterMode.setStatus(_A)
_SnIpxPortCounters_ObjectIdentity=ObjectIdentity
snIpxPortCounters=_SnIpxPortCounters_ObjectIdentity((1,3,6,1,4,1,1991,1,2,1,12))
_SnIpxPortCountersTable_Object=MibTable
snIpxPortCountersTable=_SnIpxPortCountersTable_Object((1,3,6,1,4,1,1991,1,2,1,12,1))
if mibBuilder.loadTexts:snIpxPortCountersTable.setStatus(_A)
_SnIpxPortCountersEntry_Object=MibTableRow
snIpxPortCountersEntry=_SnIpxPortCountersEntry_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1))
snIpxPortCountersEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:snIpxPortCountersEntry.setStatus(_A)
_SnIpxPortCountersPort_Type=PortIndex
_SnIpxPortCountersPort_Object=MibTableColumn
snIpxPortCountersPort=_SnIpxPortCountersPort_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,1),_SnIpxPortCountersPort_Type())
snIpxPortCountersPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersPort.setStatus(_A)
_SnIpxPortCountersRcvPktsCnt_Type=Counter32
_SnIpxPortCountersRcvPktsCnt_Object=MibTableColumn
snIpxPortCountersRcvPktsCnt=_SnIpxPortCountersRcvPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,2),_SnIpxPortCountersRcvPktsCnt_Type())
snIpxPortCountersRcvPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersRcvPktsCnt.setStatus(_A)
_SnIpxPortCountersTxPktsCnt_Type=Counter32
_SnIpxPortCountersTxPktsCnt_Object=MibTableColumn
snIpxPortCountersTxPktsCnt=_SnIpxPortCountersTxPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,3),_SnIpxPortCountersTxPktsCnt_Type())
snIpxPortCountersTxPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersTxPktsCnt.setStatus(_A)
_SnIpxPortCountersFwdPktsCnt_Type=Counter32
_SnIpxPortCountersFwdPktsCnt_Object=MibTableColumn
snIpxPortCountersFwdPktsCnt=_SnIpxPortCountersFwdPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,4),_SnIpxPortCountersFwdPktsCnt_Type())
snIpxPortCountersFwdPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersFwdPktsCnt.setStatus(_A)
_SnIpxPortCountersRcvDropPktsCnt_Type=Counter32
_SnIpxPortCountersRcvDropPktsCnt_Object=MibTableColumn
snIpxPortCountersRcvDropPktsCnt=_SnIpxPortCountersRcvDropPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,5),_SnIpxPortCountersRcvDropPktsCnt_Type())
snIpxPortCountersRcvDropPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersRcvDropPktsCnt.setStatus(_A)
_SnIpxPortCountersTxDropPktsCnt_Type=Counter32
_SnIpxPortCountersTxDropPktsCnt_Object=MibTableColumn
snIpxPortCountersTxDropPktsCnt=_SnIpxPortCountersTxDropPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,6),_SnIpxPortCountersTxDropPktsCnt_Type())
snIpxPortCountersTxDropPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersTxDropPktsCnt.setStatus(_A)
_SnIpxPortCountersRcvFiltPktsCnt_Type=Counter32
_SnIpxPortCountersRcvFiltPktsCnt_Object=MibTableColumn
snIpxPortCountersRcvFiltPktsCnt=_SnIpxPortCountersRcvFiltPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,7),_SnIpxPortCountersRcvFiltPktsCnt_Type())
snIpxPortCountersRcvFiltPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersRcvFiltPktsCnt.setStatus(_A)
_SnIpxPortCountersTxFiltPktsCnt_Type=Counter32
_SnIpxPortCountersTxFiltPktsCnt_Object=MibTableColumn
snIpxPortCountersTxFiltPktsCnt=_SnIpxPortCountersTxFiltPktsCnt_Object((1,3,6,1,4,1,1991,1,2,1,12,1,1,8),_SnIpxPortCountersTxFiltPktsCnt_Type())
snIpxPortCountersTxFiltPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:snIpxPortCountersTxFiltPktsCnt.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RtrStatus':RtrStatus,'ClearStatus':ClearStatus,'PortIndex':PortIndex,'Action':Action,'NetNumber':NetNumber,'snIpx':snIpx,'snIpxGen':snIpxGen,'snIpxRoutingMode':snIpxRoutingMode,'snIpxNetBiosFilterMode':snIpxNetBiosFilterMode,'snIpxClearCache':snIpxClearCache,'snIpxClearRoute':snIpxClearRoute,'snIpxClearTrafficCnts':snIpxClearTrafficCnts,'snIpxRcvPktsCnt':snIpxRcvPktsCnt,'snIpxTxPktsCnt':snIpxTxPktsCnt,'snIpxFwdPktsCnt':snIpxFwdPktsCnt,'snIpxRcvDropPktsCnt':snIpxRcvDropPktsCnt,'snIpxRcvFiltPktsCnt':snIpxRcvFiltPktsCnt,'snIpxRipGblFiltList':snIpxRipGblFiltList,'snIpxRipFiltOnAllPort':snIpxRipFiltOnAllPort,'snIpxSapGblFiltList':snIpxSapGblFiltList,'snIpxSapFiltOnAllPort':snIpxSapFiltOnAllPort,'snIpxTxDropPktsCnt':snIpxTxDropPktsCnt,'snIpxTxFiltPktsCnt':snIpxTxFiltPktsCnt,'snIpxCache':snIpxCache,'snIpxCacheTable':snIpxCacheTable,'snIpxCacheEntry':snIpxCacheEntry,_R:snIpxCacheIndex,'snIpxCacheNetNum':snIpxCacheNetNum,'snIpxCacheNode':snIpxCacheNode,'snIpxCacheOutFilter':snIpxCacheOutFilter,'snIpxCacheEncap':snIpxCacheEncap,'snIpxCachePort':snIpxCachePort,'snIpxRoute':snIpxRoute,'snIpxRouteTable':snIpxRouteTable,'snIpxRouteEntry':snIpxRouteEntry,_W:snIpxRouteIndex,'snIpxDestNetNum':snIpxDestNetNum,'snIpxFwdRouterNode':snIpxFwdRouterNode,'snIpxDestHopCnts':snIpxDestHopCnts,'snIpxRouteMetric':snIpxRouteMetric,'snIpxDestPort':snIpxDestPort,'snIpxServer':snIpxServer,'snIpxServerTable':snIpxServerTable,'snIpxServerEntry':snIpxServerEntry,_X:snIpxServerIndex,'snIpxServerType':snIpxServerType,'snIpxServerNetNum':snIpxServerNetNum,'snIpxServerNode':snIpxServerNode,'snIpxServerSocket':snIpxServerSocket,'snIpxServerHopCnts':snIpxServerHopCnts,'snIpxServerName':snIpxServerName,'snIpxFwdFilter':snIpxFwdFilter,'snIpxFwdFilterTable':snIpxFwdFilterTable,'snIpxFwdFilterEntry':snIpxFwdFilterEntry,_Y:snIpxFwdFilterIdx,'snIpxFwdFilterAction':snIpxFwdFilterAction,'snIpxFwdFilterSocket':snIpxFwdFilterSocket,'snIpxFwdFilterSrcNet':snIpxFwdFilterSrcNet,'snIpxFwdFilterSrcNode':snIpxFwdFilterSrcNode,'snIpxFwdFilterDestNet':snIpxFwdFilterDestNet,'snIpxFwdFilterDestNode':snIpxFwdFilterDestNode,'snIpxFwdFilterRowStatus':snIpxFwdFilterRowStatus,'snIpxRipFilter':snIpxRipFilter,'snIpxRipFilterTable':snIpxRipFilterTable,'snIpxRipFilterEntry':snIpxRipFilterEntry,_Z:snIpxRipFilterId,'snIpxRipFilterAction':snIpxRipFilterAction,'snIpxRipFilterNet':snIpxRipFilterNet,'snIpxRipFilterMask':snIpxRipFilterMask,'snIpxRipFilterRowStatus':snIpxRipFilterRowStatus,'snIpxSapFilter':snIpxSapFilter,'snIpxSapFilterTable':snIpxSapFilterTable,'snIpxSapFilterEntry':snIpxSapFilterEntry,_a:snIpxSapFilterId,'snIpxSapFilterAction':snIpxSapFilterAction,'snIpxSapFilterType':snIpxSapFilterType,'snIpxSapFilterName':snIpxSapFilterName,'snIpxSapFilterRowStatus':snIpxSapFilterRowStatus,'snIpxIfFwdAccess':snIpxIfFwdAccess,'snIpxIfFwdAccessTable':snIpxIfFwdAccessTable,'snIpxIfFwdAccessEntry':snIpxIfFwdAccessEntry,_b:snIpxIfFwdAccessPort,_c:snIpxIfFwdAccessDir,'snIpxIfFwdAccessFilterList':snIpxIfFwdAccessFilterList,'snIpxIfFwdAccessRowStatus':snIpxIfFwdAccessRowStatus,'snIpxIfRipAccess':snIpxIfRipAccess,'snIpxIfRipAccessTable':snIpxIfRipAccessTable,'snIpxIfRipAccessEntry':snIpxIfRipAccessEntry,_d:snIpxIfRipAccessPort,_e:snIpxIfRipAccessDir,'snIpxIfRipAccessFilterList':snIpxIfRipAccessFilterList,'snIpxIfRipAccessRowStatus':snIpxIfRipAccessRowStatus,'snIpxIfSapAccess':snIpxIfSapAccess,'snIpxIfSapAccessTable':snIpxIfSapAccessTable,'snIpxIfSapAccessEntry':snIpxIfSapAccessEntry,_f:snIpxIfSapAccessPort,_g:snIpxIfSapAccessDir,'snIpxIfSapAccessFilterList':snIpxIfSapAccessFilterList,'snIpxIfSapAccessRowStatus':snIpxIfSapAccessRowStatus,'snIpxPortAddr':snIpxPortAddr,'snIpxPortAddrTable':snIpxPortAddrTable,'snIpxPortAddrEntry':snIpxPortAddrEntry,_h:snIpxPortAddrPort,_i:snIpxPortAddrEncap,'snIpxPortAddrNetNum':snIpxPortAddrNetNum,'snIpxPortAddrRowStatus':snIpxPortAddrRowStatus,'snIpxPortAddrNetBiosFilterMode':snIpxPortAddrNetBiosFilterMode,'snIpxPortCounters':snIpxPortCounters,'snIpxPortCountersTable':snIpxPortCountersTable,'snIpxPortCountersEntry':snIpxPortCountersEntry,_j:snIpxPortCountersPort,'snIpxPortCountersRcvPktsCnt':snIpxPortCountersRcvPktsCnt,'snIpxPortCountersTxPktsCnt':snIpxPortCountersTxPktsCnt,'snIpxPortCountersFwdPktsCnt':snIpxPortCountersFwdPktsCnt,'snIpxPortCountersRcvDropPktsCnt':snIpxPortCountersRcvDropPktsCnt,'snIpxPortCountersTxDropPktsCnt':snIpxPortCountersTxDropPktsCnt,'snIpxPortCountersRcvFiltPktsCnt':snIpxPortCountersRcvFiltPktsCnt,'snIpxPortCountersTxFiltPktsCnt':snIpxPortCountersTxFiltPktsCnt})