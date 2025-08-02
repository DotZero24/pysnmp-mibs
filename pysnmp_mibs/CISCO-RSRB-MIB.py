_g='rsrbRingGroup'
_f='rsrbRemotePeerGroup'
_e='rsrbVirtRingGroup'
_d='rsrbRingNbrPacketsFwd'
_c='rsrbRingRemoteIpAddress'
_b='rsrbRingLocalIfIndex'
_a='rsrbRingMacAddr'
_Z='rsrbRingType'
_Y='rsrbRingLocal'
_X='rsrbRingBridge'
_W='rsrbRemotePeerVersion'
_V='rsrbRemotePeerLocalAck'
_U='rsrbRemotePeerDrops'
_T='rsrbRemotePeerTcpQueue'
_S='rsrbRemotePeerExplorersRx'
_R='rsrbRemotePeerBytesTx'
_Q='rsrbRemotePeerBytesRx'
_P='rsrbRemotePeerPacketsTx'
_O='rsrbRemotePeerPacketsRx'
_N='rsrbRemotePeerLocalIfIndex'
_M='rsrbRemotePeerIPAddr'
_L='rsrbRemotePeerEncapsulation'
_K='rsrbVirtRingMaxTcpQSize'
_J='rsrbVirtRingIPAddr'
_I='rsrbRingIndex'
_H='rsrbRemotePeerIndex'
_G='rsrbRemotePeerState'
_F='not-accessible'
_E='rsrbVirtRingIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-RSRB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ciscoRsrbMIB=ModuleIdentity((1,3,6,1,4,1,9,9,29))
if mibBuilder.loadTexts:ciscoRsrbMIB.setRevisions(('1995-08-21 00:00',))
_RsrbObjects_ObjectIdentity=ObjectIdentity
rsrbObjects=_RsrbObjects_ObjectIdentity((1,3,6,1,4,1,9,9,29,1))
_RsrbVirtualRings_ObjectIdentity=ObjectIdentity
rsrbVirtualRings=_RsrbVirtualRings_ObjectIdentity((1,3,6,1,4,1,9,9,29,1,1))
_RsrbVirtRingTable_Object=MibTable
rsrbVirtRingTable=_RsrbVirtRingTable_Object((1,3,6,1,4,1,9,9,29,1,1,1))
if mibBuilder.loadTexts:rsrbVirtRingTable.setStatus(_A)
_RsrbVirtRingEntry_Object=MibTableRow
rsrbVirtRingEntry=_RsrbVirtRingEntry_Object((1,3,6,1,4,1,9,9,29,1,1,1,1))
rsrbVirtRingEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:rsrbVirtRingEntry.setStatus(_A)
class _RsrbVirtRingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RsrbVirtRingIndex_Type.__name__=_D
_RsrbVirtRingIndex_Object=MibTableColumn
rsrbVirtRingIndex=_RsrbVirtRingIndex_Object((1,3,6,1,4,1,9,9,29,1,1,1,1,1),_RsrbVirtRingIndex_Type())
rsrbVirtRingIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rsrbVirtRingIndex.setStatus(_A)
_RsrbVirtRingIPAddr_Type=IpAddress
_RsrbVirtRingIPAddr_Object=MibTableColumn
rsrbVirtRingIPAddr=_RsrbVirtRingIPAddr_Object((1,3,6,1,4,1,9,9,29,1,1,1,1,2),_RsrbVirtRingIPAddr_Type())
rsrbVirtRingIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbVirtRingIPAddr.setStatus(_A)
_RsrbVirtRingMaxTcpQSize_Type=Integer32
_RsrbVirtRingMaxTcpQSize_Object=MibTableColumn
rsrbVirtRingMaxTcpQSize=_RsrbVirtRingMaxTcpQSize_Object((1,3,6,1,4,1,9,9,29,1,1,1,1,3),_RsrbVirtRingMaxTcpQSize_Type())
rsrbVirtRingMaxTcpQSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbVirtRingMaxTcpQSize.setStatus(_A)
_RsrbRemotePeers_ObjectIdentity=ObjectIdentity
rsrbRemotePeers=_RsrbRemotePeers_ObjectIdentity((1,3,6,1,4,1,9,9,29,1,2))
_RsrbRemotePeerTable_Object=MibTable
rsrbRemotePeerTable=_RsrbRemotePeerTable_Object((1,3,6,1,4,1,9,9,29,1,2,1))
if mibBuilder.loadTexts:rsrbRemotePeerTable.setStatus(_A)
_RsrbRemotePeerEntry_Object=MibTableRow
rsrbRemotePeerEntry=_RsrbRemotePeerEntry_Object((1,3,6,1,4,1,9,9,29,1,2,1,1))
rsrbRemotePeerEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:rsrbRemotePeerEntry.setStatus(_A)
class _RsrbRemotePeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RsrbRemotePeerIndex_Type.__name__=_D
_RsrbRemotePeerIndex_Object=MibTableColumn
rsrbRemotePeerIndex=_RsrbRemotePeerIndex_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,1),_RsrbRemotePeerIndex_Type())
rsrbRemotePeerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rsrbRemotePeerIndex.setStatus(_A)
class _RsrbRemotePeerEncapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tcp',1),('serial',2),('lan',3),('fst',4),('frameRelay',5)))
_RsrbRemotePeerEncapsulation_Type.__name__=_D
_RsrbRemotePeerEncapsulation_Object=MibTableColumn
rsrbRemotePeerEncapsulation=_RsrbRemotePeerEncapsulation_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,2),_RsrbRemotePeerEncapsulation_Type())
rsrbRemotePeerEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerEncapsulation.setStatus(_A)
_RsrbRemotePeerIPAddr_Type=IpAddress
_RsrbRemotePeerIPAddr_Object=MibTableColumn
rsrbRemotePeerIPAddr=_RsrbRemotePeerIPAddr_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,3),_RsrbRemotePeerIPAddr_Type())
rsrbRemotePeerIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerIPAddr.setStatus(_A)
_RsrbRemotePeerLocalIfIndex_Type=InterfaceIndex
_RsrbRemotePeerLocalIfIndex_Object=MibTableColumn
rsrbRemotePeerLocalIfIndex=_RsrbRemotePeerLocalIfIndex_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,4),_RsrbRemotePeerLocalIfIndex_Type())
rsrbRemotePeerLocalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerLocalIfIndex.setStatus(_A)
class _RsrbRemotePeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dead',1),('closed',2),('opening',3),('openWaitXport',4),('waitRemoteRsp',5),('remoteResponded',6),('remoteOpened',7),('draining',8),('connected',9)))
_RsrbRemotePeerState_Type.__name__=_D
_RsrbRemotePeerState_Object=MibTableColumn
rsrbRemotePeerState=_RsrbRemotePeerState_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,5),_RsrbRemotePeerState_Type())
rsrbRemotePeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerState.setStatus(_A)
_RsrbRemotePeerPacketsRx_Type=Counter32
_RsrbRemotePeerPacketsRx_Object=MibTableColumn
rsrbRemotePeerPacketsRx=_RsrbRemotePeerPacketsRx_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,6),_RsrbRemotePeerPacketsRx_Type())
rsrbRemotePeerPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerPacketsRx.setStatus(_A)
_RsrbRemotePeerPacketsTx_Type=Counter32
_RsrbRemotePeerPacketsTx_Object=MibTableColumn
rsrbRemotePeerPacketsTx=_RsrbRemotePeerPacketsTx_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,7),_RsrbRemotePeerPacketsTx_Type())
rsrbRemotePeerPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerPacketsTx.setStatus(_A)
_RsrbRemotePeerBytesRx_Type=Counter32
_RsrbRemotePeerBytesRx_Object=MibTableColumn
rsrbRemotePeerBytesRx=_RsrbRemotePeerBytesRx_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,8),_RsrbRemotePeerBytesRx_Type())
rsrbRemotePeerBytesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerBytesRx.setStatus(_A)
_RsrbRemotePeerBytesTx_Type=Counter32
_RsrbRemotePeerBytesTx_Object=MibTableColumn
rsrbRemotePeerBytesTx=_RsrbRemotePeerBytesTx_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,9),_RsrbRemotePeerBytesTx_Type())
rsrbRemotePeerBytesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerBytesTx.setStatus(_A)
_RsrbRemotePeerExplorersRx_Type=Counter32
_RsrbRemotePeerExplorersRx_Object=MibTableColumn
rsrbRemotePeerExplorersRx=_RsrbRemotePeerExplorersRx_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,10),_RsrbRemotePeerExplorersRx_Type())
rsrbRemotePeerExplorersRx.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerExplorersRx.setStatus(_A)
_RsrbRemotePeerTcpQueue_Type=Gauge32
_RsrbRemotePeerTcpQueue_Object=MibTableColumn
rsrbRemotePeerTcpQueue=_RsrbRemotePeerTcpQueue_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,11),_RsrbRemotePeerTcpQueue_Type())
rsrbRemotePeerTcpQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerTcpQueue.setStatus(_A)
_RsrbRemotePeerDrops_Type=Counter32
_RsrbRemotePeerDrops_Object=MibTableColumn
rsrbRemotePeerDrops=_RsrbRemotePeerDrops_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,12),_RsrbRemotePeerDrops_Type())
rsrbRemotePeerDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerDrops.setStatus(_A)
_RsrbRemotePeerLocalAck_Type=TruthValue
_RsrbRemotePeerLocalAck_Object=MibTableColumn
rsrbRemotePeerLocalAck=_RsrbRemotePeerLocalAck_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,13),_RsrbRemotePeerLocalAck_Type())
rsrbRemotePeerLocalAck.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerLocalAck.setStatus(_A)
_RsrbRemotePeerVersion_Type=Integer32
_RsrbRemotePeerVersion_Object=MibTableColumn
rsrbRemotePeerVersion=_RsrbRemotePeerVersion_Object((1,3,6,1,4,1,9,9,29,1,2,1,1,14),_RsrbRemotePeerVersion_Type())
rsrbRemotePeerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRemotePeerVersion.setStatus(_A)
_RsrbPhysicalRings_ObjectIdentity=ObjectIdentity
rsrbPhysicalRings=_RsrbPhysicalRings_ObjectIdentity((1,3,6,1,4,1,9,9,29,1,3))
_RsrbRingTable_Object=MibTable
rsrbRingTable=_RsrbRingTable_Object((1,3,6,1,4,1,9,9,29,1,3,1))
if mibBuilder.loadTexts:rsrbRingTable.setStatus(_A)
_RsrbRingEntry_Object=MibTableRow
rsrbRingEntry=_RsrbRingEntry_Object((1,3,6,1,4,1,9,9,29,1,3,1,1))
rsrbRingEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:rsrbRingEntry.setStatus(_A)
class _RsrbRingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RsrbRingIndex_Type.__name__=_D
_RsrbRingIndex_Object=MibTableColumn
rsrbRingIndex=_RsrbRingIndex_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,1),_RsrbRingIndex_Type())
rsrbRingIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rsrbRingIndex.setStatus(_A)
_RsrbRingBridge_Type=Integer32
_RsrbRingBridge_Object=MibTableColumn
rsrbRingBridge=_RsrbRingBridge_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,2),_RsrbRingBridge_Type())
rsrbRingBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingBridge.setStatus(_A)
_RsrbRingLocal_Type=TruthValue
_RsrbRingLocal_Object=MibTableColumn
rsrbRingLocal=_RsrbRingLocal_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,3),_RsrbRingLocal_Type())
rsrbRingLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingLocal.setStatus(_A)
class _RsrbRingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('dynamic',2),('sdllc',3),('qllc',4),('virtual',5)))
_RsrbRingType_Type.__name__=_D
_RsrbRingType_Object=MibTableColumn
rsrbRingType=_RsrbRingType_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,4),_RsrbRingType_Type())
rsrbRingType.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingType.setStatus(_A)
_RsrbRingMacAddr_Type=MacAddress
_RsrbRingMacAddr_Object=MibTableColumn
rsrbRingMacAddr=_RsrbRingMacAddr_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,5),_RsrbRingMacAddr_Type())
rsrbRingMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingMacAddr.setStatus(_A)
_RsrbRingLocalIfIndex_Type=InterfaceIndex
_RsrbRingLocalIfIndex_Object=MibTableColumn
rsrbRingLocalIfIndex=_RsrbRingLocalIfIndex_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,6),_RsrbRingLocalIfIndex_Type())
rsrbRingLocalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingLocalIfIndex.setStatus(_A)
_RsrbRingRemoteIpAddress_Type=IpAddress
_RsrbRingRemoteIpAddress_Object=MibTableColumn
rsrbRingRemoteIpAddress=_RsrbRingRemoteIpAddress_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,7),_RsrbRingRemoteIpAddress_Type())
rsrbRingRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingRemoteIpAddress.setStatus(_A)
_RsrbRingNbrPacketsFwd_Type=Counter32
_RsrbRingNbrPacketsFwd_Object=MibTableColumn
rsrbRingNbrPacketsFwd=_RsrbRingNbrPacketsFwd_Object((1,3,6,1,4,1,9,9,29,1,3,1,1,8),_RsrbRingNbrPacketsFwd_Type())
rsrbRingNbrPacketsFwd.setMaxAccess(_C)
if mibBuilder.loadTexts:rsrbRingNbrPacketsFwd.setStatus(_A)
_RsrbNotificationPrefix_ObjectIdentity=ObjectIdentity
rsrbNotificationPrefix=_RsrbNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,29,2))
_RsrbNotifications_ObjectIdentity=ObjectIdentity
rsrbNotifications=_RsrbNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,29,2,0))
_RsrbMibConformance_ObjectIdentity=ObjectIdentity
rsrbMibConformance=_RsrbMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,29,3))
_RsrbMibCompliances_ObjectIdentity=ObjectIdentity
rsrbMibCompliances=_RsrbMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,29,3,1))
_RsrbMibGroups_ObjectIdentity=ObjectIdentity
rsrbMibGroups=_RsrbMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,29,3,2))
rsrbVirtRingGroup=ObjectGroup((1,3,6,1,4,1,9,9,29,3,2,1))
rsrbVirtRingGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:rsrbVirtRingGroup.setStatus(_A)
rsrbRemotePeerGroup=ObjectGroup((1,3,6,1,4,1,9,9,29,3,2,2))
rsrbRemotePeerGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_G),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:rsrbRemotePeerGroup.setStatus(_A)
rsrbRingGroup=ObjectGroup((1,3,6,1,4,1,9,9,29,3,2,3))
rsrbRingGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:rsrbRingGroup.setStatus(_A)
rsrbPeerStateChangeNotification=NotificationType((1,3,6,1,4,1,9,9,29,2,0,1))
rsrbPeerStateChangeNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:rsrbPeerStateChangeNotification.setStatus(_A)
rsrbMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,29,3,1,1))
rsrbMibCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:rsrbMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoRsrbMIB':ciscoRsrbMIB,'rsrbObjects':rsrbObjects,'rsrbVirtualRings':rsrbVirtualRings,'rsrbVirtRingTable':rsrbVirtRingTable,'rsrbVirtRingEntry':rsrbVirtRingEntry,_E:rsrbVirtRingIndex,_J:rsrbVirtRingIPAddr,_K:rsrbVirtRingMaxTcpQSize,'rsrbRemotePeers':rsrbRemotePeers,'rsrbRemotePeerTable':rsrbRemotePeerTable,'rsrbRemotePeerEntry':rsrbRemotePeerEntry,_H:rsrbRemotePeerIndex,_L:rsrbRemotePeerEncapsulation,_M:rsrbRemotePeerIPAddr,_N:rsrbRemotePeerLocalIfIndex,_G:rsrbRemotePeerState,_O:rsrbRemotePeerPacketsRx,_P:rsrbRemotePeerPacketsTx,_Q:rsrbRemotePeerBytesRx,_R:rsrbRemotePeerBytesTx,_S:rsrbRemotePeerExplorersRx,_T:rsrbRemotePeerTcpQueue,_U:rsrbRemotePeerDrops,_V:rsrbRemotePeerLocalAck,_W:rsrbRemotePeerVersion,'rsrbPhysicalRings':rsrbPhysicalRings,'rsrbRingTable':rsrbRingTable,'rsrbRingEntry':rsrbRingEntry,_I:rsrbRingIndex,_X:rsrbRingBridge,_Y:rsrbRingLocal,_Z:rsrbRingType,_a:rsrbRingMacAddr,_b:rsrbRingLocalIfIndex,_c:rsrbRingRemoteIpAddress,_d:rsrbRingNbrPacketsFwd,'rsrbNotificationPrefix':rsrbNotificationPrefix,'rsrbNotifications':rsrbNotifications,'rsrbPeerStateChangeNotification':rsrbPeerStateChangeNotification,'rsrbMibConformance':rsrbMibConformance,'rsrbMibCompliances':rsrbMibCompliances,'rsrbMibCompliance':rsrbMibCompliance,'rsrbMibGroups':rsrbMibGroups,_e:rsrbVirtRingGroup,_f:rsrbRemotePeerGroup,_g:rsrbRingGroup})