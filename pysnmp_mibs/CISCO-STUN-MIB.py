_e='stunRouteGroup'
_d='stunPortGroup'
_c='stunGroupGroup'
_b='stunGlobalGroup'
_a='stunRouteTxBytes'
_Z='stunRouteRxBytes'
_Y='stunRouteTxPackets'
_X='stunRouteRxPackets'
_W='stunRouteLocalAck'
_V='stunRoutePriority'
_U='stunRouteSerialInterface'
_T='stunRouteRemoteIP'
_S='stunRouteType'
_R='stunPortDefaultPeerSerialInterface'
_Q='stunPortDefaultPeerIP'
_P='stunPortDefaultPeerType'
_O='stunPortGroupIndex'
_N='stunProtocolType'
_M='stunIPAddr'
_L='stunRouteStationAddress'
_K='frameRelay'
_J='not-accessible'
_I='ifIndex'
_H='IF-MIB'
_G='stunRoutePeerState'
_F='direct'
_E='stunGroupIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-STUN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoStunMIB=ModuleIdentity((1,3,6,1,4,1,9,9,30))
if mibBuilder.loadTexts:ciscoStunMIB.setRevisions(('1995-08-21 00:00','1995-03-17 00:00'))
_StunObjects_ObjectIdentity=ObjectIdentity
stunObjects=_StunObjects_ObjectIdentity((1,3,6,1,4,1,9,9,30,1))
_StunGlobal_ObjectIdentity=ObjectIdentity
stunGlobal=_StunGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,30,1,1))
_StunIPAddr_Type=IpAddress
_StunIPAddr_Object=MibScalar
stunIPAddr=_StunIPAddr_Object((1,3,6,1,4,1,9,9,30,1,1,1),_StunIPAddr_Type())
stunIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:stunIPAddr.setStatus(_A)
_StunGroups_ObjectIdentity=ObjectIdentity
stunGroups=_StunGroups_ObjectIdentity((1,3,6,1,4,1,9,9,30,1,2))
_StunGroupTable_Object=MibTable
stunGroupTable=_StunGroupTable_Object((1,3,6,1,4,1,9,9,30,1,2,1))
if mibBuilder.loadTexts:stunGroupTable.setStatus(_A)
_StunGroupEntry_Object=MibTableRow
stunGroupEntry=_StunGroupEntry_Object((1,3,6,1,4,1,9,9,30,1,2,1,1))
stunGroupEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:stunGroupEntry.setStatus(_A)
class _StunGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_StunGroupIndex_Type.__name__=_D
_StunGroupIndex_Object=MibTableColumn
stunGroupIndex=_StunGroupIndex_Object((1,3,6,1,4,1,9,9,30,1,2,1,1,1),_StunGroupIndex_Type())
stunGroupIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:stunGroupIndex.setStatus(_A)
class _StunProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('basic',1),('sdlc',2),('sdlctg',3),('custom',4)))
_StunProtocolType_Type.__name__=_D
_StunProtocolType_Object=MibTableColumn
stunProtocolType=_StunProtocolType_Object((1,3,6,1,4,1,9,9,30,1,2,1,1,2),_StunProtocolType_Type())
stunProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:stunProtocolType.setStatus(_A)
_StunPorts_ObjectIdentity=ObjectIdentity
stunPorts=_StunPorts_ObjectIdentity((1,3,6,1,4,1,9,9,30,1,3))
_StunPortTable_Object=MibTable
stunPortTable=_StunPortTable_Object((1,3,6,1,4,1,9,9,30,1,3,1))
if mibBuilder.loadTexts:stunPortTable.setStatus(_A)
_StunPortEntry_Object=MibTableRow
stunPortEntry=_StunPortEntry_Object((1,3,6,1,4,1,9,9,30,1,3,1,1))
stunPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:stunPortEntry.setStatus(_A)
class _StunPortGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_StunPortGroupIndex_Type.__name__=_D
_StunPortGroupIndex_Object=MibTableColumn
stunPortGroupIndex=_StunPortGroupIndex_Object((1,3,6,1,4,1,9,9,30,1,3,1,1,1),_StunPortGroupIndex_Type())
stunPortGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:stunPortGroupIndex.setStatus(_A)
class _StunPortDefaultPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ip',2),(_F,3),(_K,4)))
_StunPortDefaultPeerType_Type.__name__=_D
_StunPortDefaultPeerType_Object=MibTableColumn
stunPortDefaultPeerType=_StunPortDefaultPeerType_Object((1,3,6,1,4,1,9,9,30,1,3,1,1,2),_StunPortDefaultPeerType_Type())
stunPortDefaultPeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:stunPortDefaultPeerType.setStatus(_A)
_StunPortDefaultPeerIP_Type=IpAddress
_StunPortDefaultPeerIP_Object=MibTableColumn
stunPortDefaultPeerIP=_StunPortDefaultPeerIP_Object((1,3,6,1,4,1,9,9,30,1,3,1,1,3),_StunPortDefaultPeerIP_Type())
stunPortDefaultPeerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:stunPortDefaultPeerIP.setStatus(_A)
_StunPortDefaultPeerSerialInterface_Type=InterfaceIndex
_StunPortDefaultPeerSerialInterface_Object=MibTableColumn
stunPortDefaultPeerSerialInterface=_StunPortDefaultPeerSerialInterface_Object((1,3,6,1,4,1,9,9,30,1,3,1,1,4),_StunPortDefaultPeerSerialInterface_Type())
stunPortDefaultPeerSerialInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:stunPortDefaultPeerSerialInterface.setStatus(_A)
_StunRoutes_ObjectIdentity=ObjectIdentity
stunRoutes=_StunRoutes_ObjectIdentity((1,3,6,1,4,1,9,9,30,1,4))
_StunRouteTable_Object=MibTable
stunRouteTable=_StunRouteTable_Object((1,3,6,1,4,1,9,9,30,1,4,1))
if mibBuilder.loadTexts:stunRouteTable.setStatus(_A)
_StunRouteEntry_Object=MibTableRow
stunRouteEntry=_StunRouteEntry_Object((1,3,6,1,4,1,9,9,30,1,4,1,1))
stunRouteEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:stunRouteEntry.setStatus(_A)
class _StunRouteStationAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_StunRouteStationAddress_Type.__name__=_D
_StunRouteStationAddress_Object=MibTableColumn
stunRouteStationAddress=_StunRouteStationAddress_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,1),_StunRouteStationAddress_Type())
stunRouteStationAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:stunRouteStationAddress.setStatus(_A)
class _StunRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ip',2),(_F,3),(_K,4)))
_StunRouteType_Type.__name__=_D
_StunRouteType_Object=MibTableColumn
stunRouteType=_StunRouteType_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,2),_StunRouteType_Type())
stunRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteType.setStatus(_A)
_StunRouteRemoteIP_Type=IpAddress
_StunRouteRemoteIP_Object=MibTableColumn
stunRouteRemoteIP=_StunRouteRemoteIP_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,3),_StunRouteRemoteIP_Type())
stunRouteRemoteIP.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteRemoteIP.setStatus(_A)
_StunRouteSerialInterface_Type=InterfaceIndex
_StunRouteSerialInterface_Object=MibTableColumn
stunRouteSerialInterface=_StunRouteSerialInterface_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,4),_StunRouteSerialInterface_Type())
stunRouteSerialInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteSerialInterface.setStatus(_A)
class _StunRoutePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('normal',2),('medium',3),('high',4)))
_StunRoutePriority_Type.__name__=_D
_StunRoutePriority_Object=MibTableColumn
stunRoutePriority=_StunRoutePriority_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,5),_StunRoutePriority_Type())
stunRoutePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRoutePriority.setStatus(_A)
class _StunRoutePeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dead',1),('closed',2),('opening',3),('openWait',4),('connected',5),(_F,6)))
_StunRoutePeerState_Type.__name__=_D
_StunRoutePeerState_Object=MibTableColumn
stunRoutePeerState=_StunRoutePeerState_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,6),_StunRoutePeerState_Type())
stunRoutePeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRoutePeerState.setStatus(_A)
_StunRouteLocalAck_Type=TruthValue
_StunRouteLocalAck_Object=MibTableColumn
stunRouteLocalAck=_StunRouteLocalAck_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,7),_StunRouteLocalAck_Type())
stunRouteLocalAck.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteLocalAck.setStatus(_A)
_StunRouteRxPackets_Type=Counter32
_StunRouteRxPackets_Object=MibTableColumn
stunRouteRxPackets=_StunRouteRxPackets_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,8),_StunRouteRxPackets_Type())
stunRouteRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteRxPackets.setStatus(_A)
_StunRouteTxPackets_Type=Counter32
_StunRouteTxPackets_Object=MibTableColumn
stunRouteTxPackets=_StunRouteTxPackets_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,9),_StunRouteTxPackets_Type())
stunRouteTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteTxPackets.setStatus(_A)
_StunRouteRxBytes_Type=Counter32
_StunRouteRxBytes_Object=MibTableColumn
stunRouteRxBytes=_StunRouteRxBytes_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,10),_StunRouteRxBytes_Type())
stunRouteRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteRxBytes.setStatus(_A)
_StunRouteTxBytes_Type=Counter32
_StunRouteTxBytes_Object=MibTableColumn
stunRouteTxBytes=_StunRouteTxBytes_Object((1,3,6,1,4,1,9,9,30,1,4,1,1,11),_StunRouteTxBytes_Type())
stunRouteTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:stunRouteTxBytes.setStatus(_A)
_StunNotificationPrefix_ObjectIdentity=ObjectIdentity
stunNotificationPrefix=_StunNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,30,2))
_StunNotifications_ObjectIdentity=ObjectIdentity
stunNotifications=_StunNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,30,2,0))
_StunMibConformance_ObjectIdentity=ObjectIdentity
stunMibConformance=_StunMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,30,3))
_StunMibCompliances_ObjectIdentity=ObjectIdentity
stunMibCompliances=_StunMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,30,3,1))
_StunMibGroups_ObjectIdentity=ObjectIdentity
stunMibGroups=_StunMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,30,3,2))
stunGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,30,3,2,1))
stunGlobalGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:stunGlobalGroup.setStatus(_A)
stunGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,30,3,2,2))
stunGroupGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:stunGroupGroup.setStatus(_A)
stunPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,30,3,2,3))
stunPortGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:stunPortGroup.setStatus(_A)
stunRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,30,3,2,4))
stunRouteGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_G),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:stunRouteGroup.setStatus(_A)
stunPeerStateChangeNotification=NotificationType((1,3,6,1,4,1,9,9,30,2,0,1))
stunPeerStateChangeNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:stunPeerStateChangeNotification.setStatus(_A)
stunMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,30,3,1,1))
stunMibCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:stunMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoStunMIB':ciscoStunMIB,'stunObjects':stunObjects,'stunGlobal':stunGlobal,_M:stunIPAddr,'stunGroups':stunGroups,'stunGroupTable':stunGroupTable,'stunGroupEntry':stunGroupEntry,_E:stunGroupIndex,_N:stunProtocolType,'stunPorts':stunPorts,'stunPortTable':stunPortTable,'stunPortEntry':stunPortEntry,_O:stunPortGroupIndex,_P:stunPortDefaultPeerType,_Q:stunPortDefaultPeerIP,_R:stunPortDefaultPeerSerialInterface,'stunRoutes':stunRoutes,'stunRouteTable':stunRouteTable,'stunRouteEntry':stunRouteEntry,_L:stunRouteStationAddress,_S:stunRouteType,_T:stunRouteRemoteIP,_U:stunRouteSerialInterface,_V:stunRoutePriority,_G:stunRoutePeerState,_W:stunRouteLocalAck,_X:stunRouteRxPackets,_Y:stunRouteTxPackets,_Z:stunRouteRxBytes,_a:stunRouteTxBytes,'stunNotificationPrefix':stunNotificationPrefix,'stunNotifications':stunNotifications,'stunPeerStateChangeNotification':stunPeerStateChangeNotification,'stunMibConformance':stunMibConformance,'stunMibCompliances':stunMibCompliances,'stunMibCompliance':stunMibCompliance,'stunMibGroups':stunMibGroups,_b:stunGlobalGroup,_c:stunGroupGroup,_d:stunPortGroup,_e:stunRouteGroup})