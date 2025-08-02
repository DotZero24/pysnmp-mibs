_Y='groupAB'
_X='not-accessible'
_W='wwpLeosVlanTranslationFrameVid'
_V='wwpLeosVlanTranslationPgId'
_U='wwpLeosVlanTotalStatsVlanId'
_T='wwpLeosVlanStatsVlanId'
_S='wwpLeosPortId'
_R='disabled'
_Q='enabled'
_P='groupB'
_O='groupA'
_N='wwpLeosVlanl2ProtocolNum'
_M='wwpLeosVlanMemberTagId'
_L='wwpLeosVlanMemberPortId'
_K='TruthValue'
_J='OctetString'
_I='wwpLeosCircuitIndex'
_H='wwpLeosVlanId'
_G='read-create'
_F='read-write'
_E='WWP-LEOS-VLAN-TAG-MIB'
_D='Integer32'
_C='deprecated'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_K)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosVlanMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,5))
if mibBuilder.loadTexts:wwpLeosVlanMIB.setRevisions(('2007-09-29 17:00','2003-01-15 17:00'))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
class VlanTag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosVlanMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosVlanMIBObjects=_WwpLeosVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,1))
_WwpLeosVlan_ObjectIdentity=ObjectIdentity
wwpLeosVlan=_WwpLeosVlan_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,1,1))
_WwpLeosMaxVlans_Type=Unsigned32
_WwpLeosMaxVlans_Object=MibScalar
wwpLeosMaxVlans=_WwpLeosMaxVlans_Object((1,3,6,1,4,1,6141,2,60,5,1,1,1),_WwpLeosMaxVlans_Type())
wwpLeosMaxVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMaxVlans.setStatus(_A)
_WwpLeosMaxSupportedVlanTagId_Type=Unsigned32
_WwpLeosMaxSupportedVlanTagId_Object=MibScalar
wwpLeosMaxSupportedVlanTagId=_WwpLeosMaxSupportedVlanTagId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,2),_WwpLeosMaxSupportedVlanTagId_Type())
wwpLeosMaxSupportedVlanTagId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMaxSupportedVlanTagId.setStatus(_A)
_WwpLeosNumVlans_Type=Unsigned32
_WwpLeosNumVlans_Object=MibScalar
wwpLeosNumVlans=_WwpLeosNumVlans_Object((1,3,6,1,4,1,6141,2,60,5,1,1,3),_WwpLeosNumVlans_Type())
wwpLeosNumVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosNumVlans.setStatus(_A)
_WwpLeosVlanTable_Object=MibTable
wwpLeosVlanTable=_WwpLeosVlanTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4))
if mibBuilder.loadTexts:wwpLeosVlanTable.setStatus(_A)
_WwpLeosVlanEntry_Object=MibTableRow
wwpLeosVlanEntry=_WwpLeosVlanEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1))
wwpLeosVlanEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosVlanEntry.setStatus(_A)
_WwpLeosVlanId_Type=VlanId
_WwpLeosVlanId_Object=MibTableColumn
wwpLeosVlanId=_WwpLeosVlanId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,1),_WwpLeosVlanId_Type())
wwpLeosVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanId.setStatus(_A)
class _WwpLeosVlanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosVlanName_Type.__name__=_J
_WwpLeosVlanName_Object=MibTableColumn
wwpLeosVlanName=_WwpLeosVlanName_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,2),_WwpLeosVlanName_Type())
wwpLeosVlanName.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanName.setStatus(_A)
_WwpLeosVlanStatus_Type=RowStatus
_WwpLeosVlanStatus_Object=MibTableColumn
wwpLeosVlanStatus=_WwpLeosVlanStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,4),_WwpLeosVlanStatus_Type())
wwpLeosVlanStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanStatus.setStatus(_A)
class _WwpLeosVlanMacLrnState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_WwpLeosVlanMacLrnState_Type.__name__=_D
_WwpLeosVlanMacLrnState_Object=MibTableColumn
wwpLeosVlanMacLrnState=_WwpLeosVlanMacLrnState_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,5),_WwpLeosVlanMacLrnState_Type())
wwpLeosVlanMacLrnState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanMacLrnState.setStatus(_A)
class _WwpLeosVlanMacLrnOperState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),('vsOverride',3)))
_WwpLeosVlanMacLrnOperState_Type.__name__=_D
_WwpLeosVlanMacLrnOperState_Object=MibTableColumn
wwpLeosVlanMacLrnOperState=_WwpLeosVlanMacLrnOperState_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,6),_WwpLeosVlanMacLrnOperState_Type())
wwpLeosVlanMacLrnOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanMacLrnOperState.setStatus(_A)
class _WwpLeosVlanTranslationVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosVlanTranslationVlan_Type.__name__=_D
_WwpLeosVlanTranslationVlan_Object=MibTableColumn
wwpLeosVlanTranslationVlan=_WwpLeosVlanTranslationVlan_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,7),_WwpLeosVlanTranslationVlan_Type())
wwpLeosVlanTranslationVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanTranslationVlan.setStatus(_A)
class _WwpLeosVlanEgressTpid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tpid8100',1),('tpid9100',2),('tpid88A8',3)))
_WwpLeosVlanEgressTpid_Type.__name__=_D
_WwpLeosVlanEgressTpid_Object=MibTableColumn
wwpLeosVlanEgressTpid=_WwpLeosVlanEgressTpid_Object((1,3,6,1,4,1,6141,2,60,5,1,1,4,1,8),_WwpLeosVlanEgressTpid_Type())
wwpLeosVlanEgressTpid.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanEgressTpid.setStatus(_A)
_WwpLeosVlanTagMemberTable_Object=MibTable
wwpLeosVlanTagMemberTable=_WwpLeosVlanTagMemberTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,5))
if mibBuilder.loadTexts:wwpLeosVlanTagMemberTable.setStatus(_A)
_WwpLeosVlanTagMemberEntry_Object=MibTableRow
wwpLeosVlanTagMemberEntry=_WwpLeosVlanTagMemberEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,5,1))
wwpLeosVlanTagMemberEntry.setIndexNames((0,_E,_H),(0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:wwpLeosVlanTagMemberEntry.setStatus(_A)
class _WwpLeosVlanMemberPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVlanMemberPortId_Type.__name__=_D
_WwpLeosVlanMemberPortId_Object=MibTableColumn
wwpLeosVlanMemberPortId=_WwpLeosVlanMemberPortId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,5,1,1),_WwpLeosVlanMemberPortId_Type())
wwpLeosVlanMemberPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanMemberPortId.setStatus(_A)
_WwpLeosVlanMemberTagId_Type=VlanTag
_WwpLeosVlanMemberTagId_Object=MibTableColumn
wwpLeosVlanMemberTagId=_WwpLeosVlanMemberTagId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,5,1,2),_WwpLeosVlanMemberTagId_Type())
wwpLeosVlanMemberTagId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanMemberTagId.setStatus(_A)
_WwpLeosVlanMemberStatus_Type=RowStatus
_WwpLeosVlanMemberStatus_Object=MibTableColumn
wwpLeosVlanMemberStatus=_WwpLeosVlanMemberStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,5,1,4),_WwpLeosVlanMemberStatus_Type())
wwpLeosVlanMemberStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanMemberStatus.setStatus(_A)
_WwpLeosVlanCircuitTable_Object=MibTable
wwpLeosVlanCircuitTable=_WwpLeosVlanCircuitTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6))
if mibBuilder.loadTexts:wwpLeosVlanCircuitTable.setStatus(_C)
_WwpLeosVlanCircuitEntry_Object=MibTableRow
wwpLeosVlanCircuitEntry=_WwpLeosVlanCircuitEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1))
wwpLeosVlanCircuitEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wwpLeosVlanCircuitEntry.setStatus(_C)
class _WwpLeosCircuitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosCircuitIndex_Type.__name__=_D
_WwpLeosCircuitIndex_Object=MibTableColumn
wwpLeosCircuitIndex=_WwpLeosCircuitIndex_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,1),_WwpLeosCircuitIndex_Type())
wwpLeosCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosCircuitIndex.setStatus(_C)
_WwpLeosCircuitVlanId_Type=VlanId
_WwpLeosCircuitVlanId_Object=MibTableColumn
wwpLeosCircuitVlanId=_WwpLeosCircuitVlanId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,2),_WwpLeosCircuitVlanId_Type())
wwpLeosCircuitVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosCircuitVlanId.setStatus(_C)
class _WwpLeosCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('mpls',2)))
_WwpLeosCircuitType_Type.__name__=_D
_WwpLeosCircuitType_Object=MibTableColumn
wwpLeosCircuitType=_WwpLeosCircuitType_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,3),_WwpLeosCircuitType_Type())
wwpLeosCircuitType.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosCircuitType.setStatus(_C)
class _WwpLeosCircuitName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_WwpLeosCircuitName_Type.__name__=_J
_WwpLeosCircuitName_Object=MibTableColumn
wwpLeosCircuitName=_WwpLeosCircuitName_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,4),_WwpLeosCircuitName_Type())
wwpLeosCircuitName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosCircuitName.setStatus(_C)
class _WwpLeosCircuitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosCircuitPriority_Type.__name__=_D
_WwpLeosCircuitPriority_Object=MibTableColumn
wwpLeosCircuitPriority=_WwpLeosCircuitPriority_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,5),_WwpLeosCircuitPriority_Type())
wwpLeosCircuitPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosCircuitPriority.setStatus(_C)
class _WwpLeosCircuitDataTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosCircuitDataTunnelState_Type.__name__=_D
_WwpLeosCircuitDataTunnelState_Object=MibTableColumn
wwpLeosCircuitDataTunnelState=_WwpLeosCircuitDataTunnelState_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,6),_WwpLeosCircuitDataTunnelState_Type())
wwpLeosCircuitDataTunnelState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosCircuitDataTunnelState.setStatus(_C)
class _WwpLeosCircuitCtrlProtocolTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosCircuitCtrlProtocolTunnelState_Type.__name__=_D
_WwpLeosCircuitCtrlProtocolTunnelState_Object=MibTableColumn
wwpLeosCircuitCtrlProtocolTunnelState=_WwpLeosCircuitCtrlProtocolTunnelState_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,7),_WwpLeosCircuitCtrlProtocolTunnelState_Type())
wwpLeosCircuitCtrlProtocolTunnelState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosCircuitCtrlProtocolTunnelState.setStatus(_C)
class _WwpLeosCircuitNumEndPoints_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosCircuitNumEndPoints_Type.__name__=_D
_WwpLeosCircuitNumEndPoints_Object=MibTableColumn
wwpLeosCircuitNumEndPoints=_WwpLeosCircuitNumEndPoints_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,8),_WwpLeosCircuitNumEndPoints_Type())
wwpLeosCircuitNumEndPoints.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosCircuitNumEndPoints.setStatus(_C)
_WwpLeosCircuitStatus_Type=RowStatus
_WwpLeosCircuitStatus_Object=MibTableColumn
wwpLeosCircuitStatus=_WwpLeosCircuitStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,6,1,9),_WwpLeosCircuitStatus_Type())
wwpLeosCircuitStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosCircuitStatus.setStatus(_C)
_WwpLeosVlanCircuitPortExclusiveTable_Object=MibTable
wwpLeosVlanCircuitPortExclusiveTable=_WwpLeosVlanCircuitPortExclusiveTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,7))
if mibBuilder.loadTexts:wwpLeosVlanCircuitPortExclusiveTable.setStatus(_C)
_WwpLeosVlanCircuitPortExclusiveEntry_Object=MibTableRow
wwpLeosVlanCircuitPortExclusiveEntry=_WwpLeosVlanCircuitPortExclusiveEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,7,1))
wwpLeosVlanCircuitPortExclusiveEntry.setIndexNames((0,_E,_I),(0,_E,_S))
if mibBuilder.loadTexts:wwpLeosVlanCircuitPortExclusiveEntry.setStatus(_C)
class _WwpLeosPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortId_Type.__name__=_D
_WwpLeosPortId_Object=MibTableColumn
wwpLeosPortId=_WwpLeosPortId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,7,1,1),_WwpLeosPortId_Type())
wwpLeosPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortId.setStatus(_C)
_WwpLeosPortExclusiveStatus_Type=RowStatus
_WwpLeosPortExclusiveStatus_Object=MibTableColumn
wwpLeosPortExclusiveStatus=_WwpLeosPortExclusiveStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,7,1,2),_WwpLeosPortExclusiveStatus_Type())
wwpLeosPortExclusiveStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosPortExclusiveStatus.setStatus(_C)
_WwpLeosVlanCircuitCtrlProtocolTable_Object=MibTable
wwpLeosVlanCircuitCtrlProtocolTable=_WwpLeosVlanCircuitCtrlProtocolTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,8))
if mibBuilder.loadTexts:wwpLeosVlanCircuitCtrlProtocolTable.setStatus(_C)
_WwpLeosVlanCircuitCtrlProtocolEntry_Object=MibTableRow
wwpLeosVlanCircuitCtrlProtocolEntry=_WwpLeosVlanCircuitCtrlProtocolEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,8,1))
wwpLeosVlanCircuitCtrlProtocolEntry.setIndexNames((0,_E,_I),(0,_E,_N))
if mibBuilder.loadTexts:wwpLeosVlanCircuitCtrlProtocolEntry.setStatus(_C)
class _WwpLeosVlanl2ProtocolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('l28021x',1),('rstp',2),('ciscoCdp',3),('ciscoDtp',4),('ciscoPagp',5),('ciscoPvst',6),('ciscoUplinkFast',7),('ciscoUdlp',8),('ciscoVtp',9),('gvrp',10),('lacp',11),('lacpMarker',12),('lldp',13),('oam',14),('vlanBridge',15)))
_WwpLeosVlanl2ProtocolNum_Type.__name__=_D
_WwpLeosVlanl2ProtocolNum_Object=MibTableColumn
wwpLeosVlanl2ProtocolNum=_WwpLeosVlanl2ProtocolNum_Object((1,3,6,1,4,1,6141,2,60,5,1,1,8,1,1),_WwpLeosVlanl2ProtocolNum_Type())
wwpLeosVlanl2ProtocolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2ProtocolNum.setStatus(_C)
class _WwpLeosVlanl2Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discard',1),('peer',2),('tunnel',3)))
_WwpLeosVlanl2Type_Type.__name__=_D
_WwpLeosVlanl2Type_Object=MibTableColumn
wwpLeosVlanl2Type=_WwpLeosVlanl2Type_Object((1,3,6,1,4,1,6141,2,60,5,1,1,8,1,2),_WwpLeosVlanl2Type_Type())
wwpLeosVlanl2Type.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanl2Type.setStatus(_C)
_WwpLeosVlanCircuitStats_ObjectIdentity=ObjectIdentity
wwpLeosVlanCircuitStats=_WwpLeosVlanCircuitStats_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,1,1,9))
_WwpLeosVlanl2AllRxPkts_Type=Counter32
_WwpLeosVlanl2AllRxPkts_Object=MibScalar
wwpLeosVlanl2AllRxPkts=_WwpLeosVlanl2AllRxPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,1),_WwpLeosVlanl2AllRxPkts_Type())
wwpLeosVlanl2AllRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllRxPkts.setStatus(_C)
_WwpLeosVlanl2AllTunneledPkts_Type=Counter32
_WwpLeosVlanl2AllTunneledPkts_Object=MibScalar
wwpLeosVlanl2AllTunneledPkts=_WwpLeosVlanl2AllTunneledPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,2),_WwpLeosVlanl2AllTunneledPkts_Type())
wwpLeosVlanl2AllTunneledPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllTunneledPkts.setStatus(_C)
_WwpLeosVlanl2AllPeerPkts_Type=Counter32
_WwpLeosVlanl2AllPeerPkts_Object=MibScalar
wwpLeosVlanl2AllPeerPkts=_WwpLeosVlanl2AllPeerPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,3),_WwpLeosVlanl2AllPeerPkts_Type())
wwpLeosVlanl2AllPeerPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllPeerPkts.setStatus(_C)
_WwpLeosVlanl2AllDiscardedPkts_Type=Counter32
_WwpLeosVlanl2AllDiscardedPkts_Object=MibScalar
wwpLeosVlanl2AllDiscardedPkts=_WwpLeosVlanl2AllDiscardedPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,4),_WwpLeosVlanl2AllDiscardedPkts_Type())
wwpLeosVlanl2AllDiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllDiscardedPkts.setStatus(_C)
_WwpLeosVlanl2AllDecodedPkts_Type=Counter32
_WwpLeosVlanl2AllDecodedPkts_Object=MibScalar
wwpLeosVlanl2AllDecodedPkts=_WwpLeosVlanl2AllDecodedPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,5),_WwpLeosVlanl2AllDecodedPkts_Type())
wwpLeosVlanl2AllDecodedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllDecodedPkts.setStatus(_C)
_WwpLeosVlanl2AllDecodedFailures_Type=Counter32
_WwpLeosVlanl2AllDecodedFailures_Object=MibScalar
wwpLeosVlanl2AllDecodedFailures=_WwpLeosVlanl2AllDecodedFailures_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,6),_WwpLeosVlanl2AllDecodedFailures_Type())
wwpLeosVlanl2AllDecodedFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllDecodedFailures.setStatus(_C)
_WwpLeosVlanl2AllTunneledSubcriberPortPkts_Type=Counter32
_WwpLeosVlanl2AllTunneledSubcriberPortPkts_Object=MibScalar
wwpLeosVlanl2AllTunneledSubcriberPortPkts=_WwpLeosVlanl2AllTunneledSubcriberPortPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,9,7),_WwpLeosVlanl2AllTunneledSubcriberPortPkts_Type())
wwpLeosVlanl2AllTunneledSubcriberPortPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2AllTunneledSubcriberPortPkts.setStatus(_C)
_WwpLeosVlanCircuitProtocolStatsTable_Object=MibTable
wwpLeosVlanCircuitProtocolStatsTable=_WwpLeosVlanCircuitProtocolStatsTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10))
if mibBuilder.loadTexts:wwpLeosVlanCircuitProtocolStatsTable.setStatus(_C)
_WwpLeosVlanCircuitProtocolStatsEntry_Object=MibTableRow
wwpLeosVlanCircuitProtocolStatsEntry=_WwpLeosVlanCircuitProtocolStatsEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1))
wwpLeosVlanCircuitProtocolStatsEntry.setIndexNames((0,_E,_I),(0,_E,_N))
if mibBuilder.loadTexts:wwpLeosVlanCircuitProtocolStatsEntry.setStatus(_C)
_WwpLeosVlanl2RxPkts_Type=Counter32
_WwpLeosVlanl2RxPkts_Object=MibTableColumn
wwpLeosVlanl2RxPkts=_WwpLeosVlanl2RxPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,1),_WwpLeosVlanl2RxPkts_Type())
wwpLeosVlanl2RxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2RxPkts.setStatus(_C)
_WwpLeosVlanl2TunneledPkts_Type=Counter32
_WwpLeosVlanl2TunneledPkts_Object=MibTableColumn
wwpLeosVlanl2TunneledPkts=_WwpLeosVlanl2TunneledPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,2),_WwpLeosVlanl2TunneledPkts_Type())
wwpLeosVlanl2TunneledPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2TunneledPkts.setStatus(_C)
_WwpLeosVlanl2PeerPkts_Type=Counter32
_WwpLeosVlanl2PeerPkts_Object=MibTableColumn
wwpLeosVlanl2PeerPkts=_WwpLeosVlanl2PeerPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,3),_WwpLeosVlanl2PeerPkts_Type())
wwpLeosVlanl2PeerPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2PeerPkts.setStatus(_C)
_WwpLeosVlanl2DiscardedPkts_Type=Counter32
_WwpLeosVlanl2DiscardedPkts_Object=MibTableColumn
wwpLeosVlanl2DiscardedPkts=_WwpLeosVlanl2DiscardedPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,4),_WwpLeosVlanl2DiscardedPkts_Type())
wwpLeosVlanl2DiscardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2DiscardedPkts.setStatus(_C)
_WwpLeosVlanl2DecodedPkts_Type=Counter32
_WwpLeosVlanl2DecodedPkts_Object=MibTableColumn
wwpLeosVlanl2DecodedPkts=_WwpLeosVlanl2DecodedPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,5),_WwpLeosVlanl2DecodedPkts_Type())
wwpLeosVlanl2DecodedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2DecodedPkts.setStatus(_C)
_WwpLeosVlanl2DecodedFailures_Type=Counter32
_WwpLeosVlanl2DecodedFailures_Object=MibTableColumn
wwpLeosVlanl2DecodedFailures=_WwpLeosVlanl2DecodedFailures_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,6),_WwpLeosVlanl2DecodedFailures_Type())
wwpLeosVlanl2DecodedFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2DecodedFailures.setStatus(_C)
_WwpLeosVlanl2TunneledSubcriberPortPkts_Type=Counter32
_WwpLeosVlanl2TunneledSubcriberPortPkts_Object=MibTableColumn
wwpLeosVlanl2TunneledSubcriberPortPkts=_WwpLeosVlanl2TunneledSubcriberPortPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,10,1,7),_WwpLeosVlanl2TunneledSubcriberPortPkts_Type())
wwpLeosVlanl2TunneledSubcriberPortPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanl2TunneledSubcriberPortPkts.setStatus(_C)
_WwpLeosVlanStatsTable_Object=MibTable
wwpLeosVlanStatsTable=_WwpLeosVlanStatsTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11))
if mibBuilder.loadTexts:wwpLeosVlanStatsTable.setStatus(_A)
_WwpLeosVlanStatsEntry_Object=MibTableRow
wwpLeosVlanStatsEntry=_WwpLeosVlanStatsEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1))
wwpLeosVlanStatsEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:wwpLeosVlanStatsEntry.setStatus(_A)
_WwpLeosVlanStatsVlanId_Type=VlanTag
_WwpLeosVlanStatsVlanId_Object=MibTableColumn
wwpLeosVlanStatsVlanId=_WwpLeosVlanStatsVlanId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,1),_WwpLeosVlanStatsVlanId_Type())
wwpLeosVlanStatsVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanStatsVlanId.setStatus(_A)
_WwpLeosVlanStatsCreateTime_Type=TimeStamp
_WwpLeosVlanStatsCreateTime_Object=MibTableColumn
wwpLeosVlanStatsCreateTime=_WwpLeosVlanStatsCreateTime_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,2),_WwpLeosVlanStatsCreateTime_Type())
wwpLeosVlanStatsCreateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanStatsCreateTime.setStatus(_A)
_WwpLeosVlanStatsUniOctets_Type=Counter64
_WwpLeosVlanStatsUniOctets_Object=MibTableColumn
wwpLeosVlanStatsUniOctets=_WwpLeosVlanStatsUniOctets_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,3),_WwpLeosVlanStatsUniOctets_Type())
wwpLeosVlanStatsUniOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanStatsUniOctets.setStatus(_A)
_WwpLeosVlanStatsUniPkts_Type=Counter32
_WwpLeosVlanStatsUniPkts_Object=MibTableColumn
wwpLeosVlanStatsUniPkts=_WwpLeosVlanStatsUniPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,4),_WwpLeosVlanStatsUniPkts_Type())
wwpLeosVlanStatsUniPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanStatsUniPkts.setStatus(_A)
_WwpLeosVlanStatsNonUniOctets_Type=Counter64
_WwpLeosVlanStatsNonUniOctets_Object=MibTableColumn
wwpLeosVlanStatsNonUniOctets=_WwpLeosVlanStatsNonUniOctets_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,5),_WwpLeosVlanStatsNonUniOctets_Type())
wwpLeosVlanStatsNonUniOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanStatsNonUniOctets.setStatus(_A)
_WwpLeosVlanStatsNonUniPkts_Type=Counter32
_WwpLeosVlanStatsNonUniPkts_Object=MibTableColumn
wwpLeosVlanStatsNonUniPkts=_WwpLeosVlanStatsNonUniPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,6),_WwpLeosVlanStatsNonUniPkts_Type())
wwpLeosVlanStatsNonUniPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanStatsNonUniPkts.setStatus(_A)
_WwpLeosVlanStatsStatus_Type=RowStatus
_WwpLeosVlanStatsStatus_Object=MibTableColumn
wwpLeosVlanStatsStatus=_WwpLeosVlanStatsStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,7),_WwpLeosVlanStatsStatus_Type())
wwpLeosVlanStatsStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanStatsStatus.setStatus(_A)
class _WwpLeosVlanStatsClear_Type(TruthValue):defaultValue=2
_WwpLeosVlanStatsClear_Type.__name__=_K
_WwpLeosVlanStatsClear_Object=MibTableColumn
wwpLeosVlanStatsClear=_WwpLeosVlanStatsClear_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,8),_WwpLeosVlanStatsClear_Type())
wwpLeosVlanStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanStatsClear.setStatus(_A)
class _WwpLeosVlanStatsPortId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVlanStatsPortId_Type.__name__=_D
_WwpLeosVlanStatsPortId_Object=MibTableColumn
wwpLeosVlanStatsPortId=_WwpLeosVlanStatsPortId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,11,1,9),_WwpLeosVlanStatsPortId_Type())
wwpLeosVlanStatsPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanStatsPortId.setStatus(_A)
_WwpLeosVlanTotalStatsTable_Object=MibTable
wwpLeosVlanTotalStatsTable=_WwpLeosVlanTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12))
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsTable.setStatus(_A)
_WwpLeosVlanTotalStatsEntry_Object=MibTableRow
wwpLeosVlanTotalStatsEntry=_WwpLeosVlanTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1))
wwpLeosVlanTotalStatsEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsEntry.setStatus(_A)
_WwpLeosVlanTotalStatsVlanId_Type=VlanTag
_WwpLeosVlanTotalStatsVlanId_Object=MibTableColumn
wwpLeosVlanTotalStatsVlanId=_WwpLeosVlanTotalStatsVlanId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,1),_WwpLeosVlanTotalStatsVlanId_Type())
wwpLeosVlanTotalStatsVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsVlanId.setStatus(_A)
_WwpLeosVlanTotalStatsCreateTime_Type=TimeStamp
_WwpLeosVlanTotalStatsCreateTime_Object=MibTableColumn
wwpLeosVlanTotalStatsCreateTime=_WwpLeosVlanTotalStatsCreateTime_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,2),_WwpLeosVlanTotalStatsCreateTime_Type())
wwpLeosVlanTotalStatsCreateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsCreateTime.setStatus(_A)
_WwpLeosVlanTotalStatsUniOctets_Type=Counter64
_WwpLeosVlanTotalStatsUniOctets_Object=MibTableColumn
wwpLeosVlanTotalStatsUniOctets=_WwpLeosVlanTotalStatsUniOctets_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,3),_WwpLeosVlanTotalStatsUniOctets_Type())
wwpLeosVlanTotalStatsUniOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsUniOctets.setStatus(_A)
_WwpLeosVlanTotalStatsUniPkts_Type=Counter32
_WwpLeosVlanTotalStatsUniPkts_Object=MibTableColumn
wwpLeosVlanTotalStatsUniPkts=_WwpLeosVlanTotalStatsUniPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,4),_WwpLeosVlanTotalStatsUniPkts_Type())
wwpLeosVlanTotalStatsUniPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsUniPkts.setStatus(_A)
_WwpLeosVlanTotalStatsNonUniOctets_Type=Counter64
_WwpLeosVlanTotalStatsNonUniOctets_Object=MibTableColumn
wwpLeosVlanTotalStatsNonUniOctets=_WwpLeosVlanTotalStatsNonUniOctets_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,5),_WwpLeosVlanTotalStatsNonUniOctets_Type())
wwpLeosVlanTotalStatsNonUniOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsNonUniOctets.setStatus(_A)
_WwpLeosVlanTotalStatsNonUniPkts_Type=Counter32
_WwpLeosVlanTotalStatsNonUniPkts_Object=MibTableColumn
wwpLeosVlanTotalStatsNonUniPkts=_WwpLeosVlanTotalStatsNonUniPkts_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,6),_WwpLeosVlanTotalStatsNonUniPkts_Type())
wwpLeosVlanTotalStatsNonUniPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsNonUniPkts.setStatus(_A)
_WwpLeosVlanTotalStatsStatus_Type=RowStatus
_WwpLeosVlanTotalStatsStatus_Object=MibTableColumn
wwpLeosVlanTotalStatsStatus=_WwpLeosVlanTotalStatsStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,7),_WwpLeosVlanTotalStatsStatus_Type())
wwpLeosVlanTotalStatsStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsStatus.setStatus(_A)
class _WwpLeosVlanTotalStatsClear_Type(TruthValue):defaultValue=2
_WwpLeosVlanTotalStatsClear_Type.__name__=_K
_WwpLeosVlanTotalStatsClear_Object=MibTableColumn
wwpLeosVlanTotalStatsClear=_WwpLeosVlanTotalStatsClear_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,8),_WwpLeosVlanTotalStatsClear_Type())
wwpLeosVlanTotalStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsClear.setStatus(_A)
class _WwpLeosVlanTotalStatsPortId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosVlanTotalStatsPortId_Type.__name__=_D
_WwpLeosVlanTotalStatsPortId_Object=MibTableColumn
wwpLeosVlanTotalStatsPortId=_WwpLeosVlanTotalStatsPortId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,12,1,9),_WwpLeosVlanTotalStatsPortId_Type())
wwpLeosVlanTotalStatsPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanTotalStatsPortId.setStatus(_A)
_WwpLeosVlanTranslationTable_Object=MibTable
wwpLeosVlanTranslationTable=_WwpLeosVlanTranslationTable_Object((1,3,6,1,4,1,6141,2,60,5,1,1,13))
if mibBuilder.loadTexts:wwpLeosVlanTranslationTable.setStatus(_A)
_WwpLeosVlanTranslationEntry_Object=MibTableRow
wwpLeosVlanTranslationEntry=_WwpLeosVlanTranslationEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,1,13,1))
wwpLeosVlanTranslationEntry.setIndexNames((0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:wwpLeosVlanTranslationEntry.setStatus(_A)
class _WwpLeosVlanTranslationPgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosVlanTranslationPgId_Type.__name__=_D
_WwpLeosVlanTranslationPgId_Object=MibTableColumn
wwpLeosVlanTranslationPgId=_WwpLeosVlanTranslationPgId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,13,1,1),_WwpLeosVlanTranslationPgId_Type())
wwpLeosVlanTranslationPgId.setMaxAccess(_X)
if mibBuilder.loadTexts:wwpLeosVlanTranslationPgId.setStatus(_A)
_WwpLeosVlanTranslationFrameVid_Type=VlanTag
_WwpLeosVlanTranslationFrameVid_Object=MibTableColumn
wwpLeosVlanTranslationFrameVid=_WwpLeosVlanTranslationFrameVid_Object((1,3,6,1,4,1,6141,2,60,5,1,1,13,1,2),_WwpLeosVlanTranslationFrameVid_Type())
wwpLeosVlanTranslationFrameVid.setMaxAccess(_X)
if mibBuilder.loadTexts:wwpLeosVlanTranslationFrameVid.setStatus(_A)
_WwpLeosVlanTranslationVlanId_Type=VlanTag
_WwpLeosVlanTranslationVlanId_Object=MibTableColumn
wwpLeosVlanTranslationVlanId=_WwpLeosVlanTranslationVlanId_Object((1,3,6,1,4,1,6141,2,60,5,1,1,13,1,3),_WwpLeosVlanTranslationVlanId_Type())
wwpLeosVlanTranslationVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanTranslationVlanId.setStatus(_A)
_WwpLeosVlanTranslationStatus_Type=RowStatus
_WwpLeosVlanTranslationStatus_Object=MibTableColumn
wwpLeosVlanTranslationStatus=_WwpLeosVlanTranslationStatus_Object((1,3,6,1,4,1,6141,2,60,5,1,1,13,1,4),_WwpLeosVlanTranslationStatus_Type())
wwpLeosVlanTranslationStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosVlanTranslationStatus.setStatus(_A)
_WwpLeosVlanEPR_ObjectIdentity=ObjectIdentity
wwpLeosVlanEPR=_WwpLeosVlanEPR_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,1,2))
_WwpLeosVlanEPRTable_Object=MibTable
wwpLeosVlanEPRTable=_WwpLeosVlanEPRTable_Object((1,3,6,1,4,1,6141,2,60,5,1,2,1))
if mibBuilder.loadTexts:wwpLeosVlanEPRTable.setStatus(_A)
_WwpLeosVlanEPREntry_Object=MibTableRow
wwpLeosVlanEPREntry=_WwpLeosVlanEPREntry_Object((1,3,6,1,4,1,6141,2,60,5,1,2,1,1))
wwpLeosVlanEPREntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosVlanEPREntry.setStatus(_A)
class _WwpLeosVlanEPRState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpLeosVlanEPRState_Type.__name__=_D
_WwpLeosVlanEPRState_Object=MibTableColumn
wwpLeosVlanEPRState=_WwpLeosVlanEPRState_Object((1,3,6,1,4,1,6141,2,60,5,1,2,1,1,1),_WwpLeosVlanEPRState_Type())
wwpLeosVlanEPRState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanEPRState.setStatus(_A)
_WwpLeosVlanEPRGrpMemTable_Object=MibTable
wwpLeosVlanEPRGrpMemTable=_WwpLeosVlanEPRGrpMemTable_Object((1,3,6,1,4,1,6141,2,60,5,1,2,2))
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpMemTable.setStatus(_A)
_WwpLeosVlanEPRGrpMemEntry_Object=MibTableRow
wwpLeosVlanEPRGrpMemEntry=_WwpLeosVlanEPRGrpMemEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,2,2,1))
wwpLeosVlanEPRGrpMemEntry.setIndexNames((0,_E,_H),(0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpMemEntry.setStatus(_A)
class _WwpLeosVlanEPRGrpName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_WwpLeosVlanEPRGrpName_Type.__name__=_D
_WwpLeosVlanEPRGrpName_Object=MibTableColumn
wwpLeosVlanEPRGrpName=_WwpLeosVlanEPRGrpName_Object((1,3,6,1,4,1,6141,2,60,5,1,2,2,1,1),_WwpLeosVlanEPRGrpName_Type())
wwpLeosVlanEPRGrpName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpName.setStatus(_A)
_WwpLeosVlanEPRGrpAccessTable_Object=MibTable
wwpLeosVlanEPRGrpAccessTable=_WwpLeosVlanEPRGrpAccessTable_Object((1,3,6,1,4,1,6141,2,60,5,1,2,3))
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpAccessTable.setStatus(_A)
_WwpLeosVlanEPRGrpAccessEntry_Object=MibTableRow
wwpLeosVlanEPRGrpAccessEntry=_WwpLeosVlanEPRGrpAccessEntry_Object((1,3,6,1,4,1,6141,2,60,5,1,2,3,1))
wwpLeosVlanEPRGrpAccessEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpAccessEntry.setStatus(_A)
class _WwpLeosVlanEPRGrpAAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_Y,3)))
_WwpLeosVlanEPRGrpAAccess_Type.__name__=_D
_WwpLeosVlanEPRGrpAAccess_Object=MibTableColumn
wwpLeosVlanEPRGrpAAccess=_WwpLeosVlanEPRGrpAAccess_Object((1,3,6,1,4,1,6141,2,60,5,1,2,3,1,1),_WwpLeosVlanEPRGrpAAccess_Type())
wwpLeosVlanEPRGrpAAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpAAccess.setStatus(_A)
class _WwpLeosVlanEPRGrpBAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_Y,3)))
_WwpLeosVlanEPRGrpBAccess_Type.__name__=_D
_WwpLeosVlanEPRGrpBAccess_Object=MibTableColumn
wwpLeosVlanEPRGrpBAccess=_WwpLeosVlanEPRGrpBAccess_Object((1,3,6,1,4,1,6141,2,60,5,1,2,3,1,2),_WwpLeosVlanEPRGrpBAccess_Type())
wwpLeosVlanEPRGrpBAccess.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosVlanEPRGrpBAccess.setStatus(_A)
_WwpLeosVlanMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosVlanMIBNotificationPrefix=_WwpLeosVlanMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,2))
_WwpLeosVlanMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosVlanMIBNotifications=_WwpLeosVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,2,0))
_WwpLeosVlanMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosVlanMIBConformance=_WwpLeosVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,3))
_WwpLeosVlanMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosVlanMIBCompliances=_WwpLeosVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,3,1))
_WwpLeosVlanMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosVlanMIBGroups=_WwpLeosVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,5,3,2))
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'VlanTag':VlanTag,'wwpLeosVlanMIB':wwpLeosVlanMIB,'wwpLeosVlanMIBObjects':wwpLeosVlanMIBObjects,'wwpLeosVlan':wwpLeosVlan,'wwpLeosMaxVlans':wwpLeosMaxVlans,'wwpLeosMaxSupportedVlanTagId':wwpLeosMaxSupportedVlanTagId,'wwpLeosNumVlans':wwpLeosNumVlans,'wwpLeosVlanTable':wwpLeosVlanTable,'wwpLeosVlanEntry':wwpLeosVlanEntry,_H:wwpLeosVlanId,'wwpLeosVlanName':wwpLeosVlanName,'wwpLeosVlanStatus':wwpLeosVlanStatus,'wwpLeosVlanMacLrnState':wwpLeosVlanMacLrnState,'wwpLeosVlanMacLrnOperState':wwpLeosVlanMacLrnOperState,'wwpLeosVlanTranslationVlan':wwpLeosVlanTranslationVlan,'wwpLeosVlanEgressTpid':wwpLeosVlanEgressTpid,'wwpLeosVlanTagMemberTable':wwpLeosVlanTagMemberTable,'wwpLeosVlanTagMemberEntry':wwpLeosVlanTagMemberEntry,_L:wwpLeosVlanMemberPortId,_M:wwpLeosVlanMemberTagId,'wwpLeosVlanMemberStatus':wwpLeosVlanMemberStatus,'wwpLeosVlanCircuitTable':wwpLeosVlanCircuitTable,'wwpLeosVlanCircuitEntry':wwpLeosVlanCircuitEntry,_I:wwpLeosCircuitIndex,'wwpLeosCircuitVlanId':wwpLeosCircuitVlanId,'wwpLeosCircuitType':wwpLeosCircuitType,'wwpLeosCircuitName':wwpLeosCircuitName,'wwpLeosCircuitPriority':wwpLeosCircuitPriority,'wwpLeosCircuitDataTunnelState':wwpLeosCircuitDataTunnelState,'wwpLeosCircuitCtrlProtocolTunnelState':wwpLeosCircuitCtrlProtocolTunnelState,'wwpLeosCircuitNumEndPoints':wwpLeosCircuitNumEndPoints,'wwpLeosCircuitStatus':wwpLeosCircuitStatus,'wwpLeosVlanCircuitPortExclusiveTable':wwpLeosVlanCircuitPortExclusiveTable,'wwpLeosVlanCircuitPortExclusiveEntry':wwpLeosVlanCircuitPortExclusiveEntry,_S:wwpLeosPortId,'wwpLeosPortExclusiveStatus':wwpLeosPortExclusiveStatus,'wwpLeosVlanCircuitCtrlProtocolTable':wwpLeosVlanCircuitCtrlProtocolTable,'wwpLeosVlanCircuitCtrlProtocolEntry':wwpLeosVlanCircuitCtrlProtocolEntry,_N:wwpLeosVlanl2ProtocolNum,'wwpLeosVlanl2Type':wwpLeosVlanl2Type,'wwpLeosVlanCircuitStats':wwpLeosVlanCircuitStats,'wwpLeosVlanl2AllRxPkts':wwpLeosVlanl2AllRxPkts,'wwpLeosVlanl2AllTunneledPkts':wwpLeosVlanl2AllTunneledPkts,'wwpLeosVlanl2AllPeerPkts':wwpLeosVlanl2AllPeerPkts,'wwpLeosVlanl2AllDiscardedPkts':wwpLeosVlanl2AllDiscardedPkts,'wwpLeosVlanl2AllDecodedPkts':wwpLeosVlanl2AllDecodedPkts,'wwpLeosVlanl2AllDecodedFailures':wwpLeosVlanl2AllDecodedFailures,'wwpLeosVlanl2AllTunneledSubcriberPortPkts':wwpLeosVlanl2AllTunneledSubcriberPortPkts,'wwpLeosVlanCircuitProtocolStatsTable':wwpLeosVlanCircuitProtocolStatsTable,'wwpLeosVlanCircuitProtocolStatsEntry':wwpLeosVlanCircuitProtocolStatsEntry,'wwpLeosVlanl2RxPkts':wwpLeosVlanl2RxPkts,'wwpLeosVlanl2TunneledPkts':wwpLeosVlanl2TunneledPkts,'wwpLeosVlanl2PeerPkts':wwpLeosVlanl2PeerPkts,'wwpLeosVlanl2DiscardedPkts':wwpLeosVlanl2DiscardedPkts,'wwpLeosVlanl2DecodedPkts':wwpLeosVlanl2DecodedPkts,'wwpLeosVlanl2DecodedFailures':wwpLeosVlanl2DecodedFailures,'wwpLeosVlanl2TunneledSubcriberPortPkts':wwpLeosVlanl2TunneledSubcriberPortPkts,'wwpLeosVlanStatsTable':wwpLeosVlanStatsTable,'wwpLeosVlanStatsEntry':wwpLeosVlanStatsEntry,_T:wwpLeosVlanStatsVlanId,'wwpLeosVlanStatsCreateTime':wwpLeosVlanStatsCreateTime,'wwpLeosVlanStatsUniOctets':wwpLeosVlanStatsUniOctets,'wwpLeosVlanStatsUniPkts':wwpLeosVlanStatsUniPkts,'wwpLeosVlanStatsNonUniOctets':wwpLeosVlanStatsNonUniOctets,'wwpLeosVlanStatsNonUniPkts':wwpLeosVlanStatsNonUniPkts,'wwpLeosVlanStatsStatus':wwpLeosVlanStatsStatus,'wwpLeosVlanStatsClear':wwpLeosVlanStatsClear,'wwpLeosVlanStatsPortId':wwpLeosVlanStatsPortId,'wwpLeosVlanTotalStatsTable':wwpLeosVlanTotalStatsTable,'wwpLeosVlanTotalStatsEntry':wwpLeosVlanTotalStatsEntry,_U:wwpLeosVlanTotalStatsVlanId,'wwpLeosVlanTotalStatsCreateTime':wwpLeosVlanTotalStatsCreateTime,'wwpLeosVlanTotalStatsUniOctets':wwpLeosVlanTotalStatsUniOctets,'wwpLeosVlanTotalStatsUniPkts':wwpLeosVlanTotalStatsUniPkts,'wwpLeosVlanTotalStatsNonUniOctets':wwpLeosVlanTotalStatsNonUniOctets,'wwpLeosVlanTotalStatsNonUniPkts':wwpLeosVlanTotalStatsNonUniPkts,'wwpLeosVlanTotalStatsStatus':wwpLeosVlanTotalStatsStatus,'wwpLeosVlanTotalStatsClear':wwpLeosVlanTotalStatsClear,'wwpLeosVlanTotalStatsPortId':wwpLeosVlanTotalStatsPortId,'wwpLeosVlanTranslationTable':wwpLeosVlanTranslationTable,'wwpLeosVlanTranslationEntry':wwpLeosVlanTranslationEntry,_V:wwpLeosVlanTranslationPgId,_W:wwpLeosVlanTranslationFrameVid,'wwpLeosVlanTranslationVlanId':wwpLeosVlanTranslationVlanId,'wwpLeosVlanTranslationStatus':wwpLeosVlanTranslationStatus,'wwpLeosVlanEPR':wwpLeosVlanEPR,'wwpLeosVlanEPRTable':wwpLeosVlanEPRTable,'wwpLeosVlanEPREntry':wwpLeosVlanEPREntry,'wwpLeosVlanEPRState':wwpLeosVlanEPRState,'wwpLeosVlanEPRGrpMemTable':wwpLeosVlanEPRGrpMemTable,'wwpLeosVlanEPRGrpMemEntry':wwpLeosVlanEPRGrpMemEntry,'wwpLeosVlanEPRGrpName':wwpLeosVlanEPRGrpName,'wwpLeosVlanEPRGrpAccessTable':wwpLeosVlanEPRGrpAccessTable,'wwpLeosVlanEPRGrpAccessEntry':wwpLeosVlanEPRGrpAccessEntry,'wwpLeosVlanEPRGrpAAccess':wwpLeosVlanEPRGrpAAccess,'wwpLeosVlanEPRGrpBAccess':wwpLeosVlanEPRGrpBAccess,'wwpLeosVlanMIBNotificationPrefix':wwpLeosVlanMIBNotificationPrefix,'wwpLeosVlanMIBNotifications':wwpLeosVlanMIBNotifications,'wwpLeosVlanMIBConformance':wwpLeosVlanMIBConformance,'wwpLeosVlanMIBCompliances':wwpLeosVlanMIBCompliances,'wwpLeosVlanMIBGroups':wwpLeosVlanMIBGroups})