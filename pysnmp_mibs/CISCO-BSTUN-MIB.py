_A7='bstunRouteApipGroup'
_A6='bstunRoutePortsGroup'
_A5='bstunRouteBipGroup'
_A4='bstunRouteGroupRev2'
_A3='bstunRouteGroup'
_A2='bstunGlobalGroup'
_A1='bstunCUStatusChangeNotification'
_A0='bstunPeerStateChangeNotification2'
_z='bstunPeerStateChangeNotification'
_y='bstunRouteAPIPHeaderVersion'
_x='bstunPeerKeepaliveLimit'
_w='bstunPeerKeepaliveInterval'
_v='bstunLisnSap'
_u='bstunPortDefaultPeerSerial'
_t='bstunPortDefaultPeerIP'
_s='bstunPortDefaultPeerType'
_r='bstunPortGroupNumber'
_q='bstunGroupUnroutableReceive'
_p='bstunGroupUnroutableTransmit'
_o='bstunLocalAck'
_n='bstunProtocolType'
_m='bstunRouteStationAddress'
_l='bstunRouteGroupIndex'
_k='serialLLC2'
_j='serialFrameRelay'
_i='serialDirect'
_h='serial'
_g='bstunGroupIndex'
_f='TruthValue'
_e='ifIndex'
_d='IF-MIB'
_c='bstunNotificationGroupRev1'
_b='bstunRouteGroupRev1'
_a='bstunRouteBIPPassive'
_Z='bstunLLC2Priority'
_Y='bstunRouteRSAP'
_X='bstunRouteDLCI'
_W='bstunIPAddr'
_V='not-accessible'
_U='bstunGlobalGroupRev1'
_T='deprecated'
_S='bstunRouteBIPDeviceStatus'
_R='bstunRouteBIPForeignPort'
_Q='bstunRouteBIPLocalPort'
_P='bstunRouteTxBytes'
_O='bstunRouteRxBytes'
_N='bstunRoutePriority'
_M='bstunRouteSerial'
_L='obsolete'
_K='bstunPortGroup'
_J='bstunGroupGroup'
_I='bstunRouteTxPackets'
_H='bstunRouteRxPackets'
_G='bstunRouteIP'
_F='bstunRouteType'
_E='bstunRoutePeerState'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-BSTUN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_d,'InterfaceIndex',_e)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_f)
ciscoBstunMIB=ModuleIdentity((1,3,6,1,4,1,9,9,35))
if mibBuilder.loadTexts:ciscoBstunMIB.setRevisions(('2003-02-10 00:00','2001-06-19 00:00','1997-01-22 00:00','1995-08-21 00:00'))
_BstunObjects_ObjectIdentity=ObjectIdentity
bstunObjects=_BstunObjects_ObjectIdentity((1,3,6,1,4,1,9,9,35,1))
_BstunGlobal_ObjectIdentity=ObjectIdentity
bstunGlobal=_BstunGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,35,1,1))
_BstunIPAddr_Type=IpAddress
_BstunIPAddr_Object=MibScalar
bstunIPAddr=_BstunIPAddr_Object((1,3,6,1,4,1,9,9,35,1,1,1),_BstunIPAddr_Type())
bstunIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunIPAddr.setStatus(_B)
class _BstunLisnSap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BstunLisnSap_Type.__name__=_D
_BstunLisnSap_Object=MibScalar
bstunLisnSap=_BstunLisnSap_Object((1,3,6,1,4,1,9,9,35,1,1,2),_BstunLisnSap_Type())
bstunLisnSap.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunLisnSap.setStatus(_B)
class _BstunPeerKeepaliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_BstunPeerKeepaliveInterval_Type.__name__=_D
_BstunPeerKeepaliveInterval_Object=MibScalar
bstunPeerKeepaliveInterval=_BstunPeerKeepaliveInterval_Object((1,3,6,1,4,1,9,9,35,1,1,3),_BstunPeerKeepaliveInterval_Type())
bstunPeerKeepaliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunPeerKeepaliveInterval.setStatus(_B)
if mibBuilder.loadTexts:bstunPeerKeepaliveInterval.setUnits('deciseconds')
class _BstunPeerKeepaliveLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_BstunPeerKeepaliveLimit_Type.__name__=_D
_BstunPeerKeepaliveLimit_Object=MibScalar
bstunPeerKeepaliveLimit=_BstunPeerKeepaliveLimit_Object((1,3,6,1,4,1,9,9,35,1,1,4),_BstunPeerKeepaliveLimit_Type())
bstunPeerKeepaliveLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunPeerKeepaliveLimit.setStatus(_B)
_BstunGroups_ObjectIdentity=ObjectIdentity
bstunGroups=_BstunGroups_ObjectIdentity((1,3,6,1,4,1,9,9,35,1,2))
_BstunGroupTable_Object=MibTable
bstunGroupTable=_BstunGroupTable_Object((1,3,6,1,4,1,9,9,35,1,2,1))
if mibBuilder.loadTexts:bstunGroupTable.setStatus(_B)
_BstunGroupEntry_Object=MibTableRow
bstunGroupEntry=_BstunGroupEntry_Object((1,3,6,1,4,1,9,9,35,1,2,1,1))
bstunGroupEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:bstunGroupEntry.setStatus(_B)
class _BstunGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BstunGroupIndex_Type.__name__=_D
_BstunGroupIndex_Object=MibTableColumn
bstunGroupIndex=_BstunGroupIndex_Object((1,3,6,1,4,1,9,9,35,1,2,1,1,1),_BstunGroupIndex_Type())
bstunGroupIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:bstunGroupIndex.setStatus(_B)
class _BstunProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('bsc',1),('adtVariPoll',2),('adtPollSelect',3),('adplex',4),('diebold',5),('asyncGeneric',6),('mdi',7),('mosec',8),('gddb',9),('apos',10)))
_BstunProtocolType_Type.__name__=_D
_BstunProtocolType_Object=MibTableColumn
bstunProtocolType=_BstunProtocolType_Object((1,3,6,1,4,1,9,9,35,1,2,1,1,2),_BstunProtocolType_Type())
bstunProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunProtocolType.setStatus(_B)
_BstunLocalAck_Type=TruthValue
_BstunLocalAck_Object=MibTableColumn
bstunLocalAck=_BstunLocalAck_Object((1,3,6,1,4,1,9,9,35,1,2,1,1,3),_BstunLocalAck_Type())
bstunLocalAck.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunLocalAck.setStatus(_B)
_BstunGroupUnroutableTransmit_Type=Counter32
_BstunGroupUnroutableTransmit_Object=MibTableColumn
bstunGroupUnroutableTransmit=_BstunGroupUnroutableTransmit_Object((1,3,6,1,4,1,9,9,35,1,2,1,1,4),_BstunGroupUnroutableTransmit_Type())
bstunGroupUnroutableTransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunGroupUnroutableTransmit.setStatus(_B)
_BstunGroupUnroutableReceive_Type=Counter32
_BstunGroupUnroutableReceive_Object=MibTableColumn
bstunGroupUnroutableReceive=_BstunGroupUnroutableReceive_Object((1,3,6,1,4,1,9,9,35,1,2,1,1,5),_BstunGroupUnroutableReceive_Type())
bstunGroupUnroutableReceive.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunGroupUnroutableReceive.setStatus(_B)
_BstunPorts_ObjectIdentity=ObjectIdentity
bstunPorts=_BstunPorts_ObjectIdentity((1,3,6,1,4,1,9,9,35,1,3))
_BstunPortTable_Object=MibTable
bstunPortTable=_BstunPortTable_Object((1,3,6,1,4,1,9,9,35,1,3,1))
if mibBuilder.loadTexts:bstunPortTable.setStatus(_B)
_BstunPortEntry_Object=MibTableRow
bstunPortEntry=_BstunPortEntry_Object((1,3,6,1,4,1,9,9,35,1,3,1,1))
bstunPortEntry.setIndexNames((0,_d,_e))
if mibBuilder.loadTexts:bstunPortEntry.setStatus(_B)
class _BstunPortGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BstunPortGroupNumber_Type.__name__=_D
_BstunPortGroupNumber_Object=MibTableColumn
bstunPortGroupNumber=_BstunPortGroupNumber_Object((1,3,6,1,4,1,9,9,35,1,3,1,1,1),_BstunPortGroupNumber_Type())
bstunPortGroupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunPortGroupNumber.setStatus(_B)
class _BstunPortDefaultPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('ip',2),(_h,3),(_i,4),(_j,5),(_k,6)))
_BstunPortDefaultPeerType_Type.__name__=_D
_BstunPortDefaultPeerType_Object=MibTableColumn
bstunPortDefaultPeerType=_BstunPortDefaultPeerType_Object((1,3,6,1,4,1,9,9,35,1,3,1,1,2),_BstunPortDefaultPeerType_Type())
bstunPortDefaultPeerType.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunPortDefaultPeerType.setStatus(_B)
_BstunPortDefaultPeerIP_Type=IpAddress
_BstunPortDefaultPeerIP_Object=MibTableColumn
bstunPortDefaultPeerIP=_BstunPortDefaultPeerIP_Object((1,3,6,1,4,1,9,9,35,1,3,1,1,3),_BstunPortDefaultPeerIP_Type())
bstunPortDefaultPeerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunPortDefaultPeerIP.setStatus(_B)
_BstunPortDefaultPeerSerial_Type=InterfaceIndex
_BstunPortDefaultPeerSerial_Object=MibTableColumn
bstunPortDefaultPeerSerial=_BstunPortDefaultPeerSerial_Object((1,3,6,1,4,1,9,9,35,1,3,1,1,4),_BstunPortDefaultPeerSerial_Type())
bstunPortDefaultPeerSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunPortDefaultPeerSerial.setStatus(_B)
_BstunRoutes_ObjectIdentity=ObjectIdentity
bstunRoutes=_BstunRoutes_ObjectIdentity((1,3,6,1,4,1,9,9,35,1,4))
_BstunRouteTable_Object=MibTable
bstunRouteTable=_BstunRouteTable_Object((1,3,6,1,4,1,9,9,35,1,4,1))
if mibBuilder.loadTexts:bstunRouteTable.setStatus(_B)
_BstunRouteEntry_Object=MibTableRow
bstunRouteEntry=_BstunRouteEntry_Object((1,3,6,1,4,1,9,9,35,1,4,1,1))
bstunRouteEntry.setIndexNames((0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:bstunRouteEntry.setStatus(_B)
class _BstunRouteGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BstunRouteGroupIndex_Type.__name__=_D
_BstunRouteGroupIndex_Object=MibTableColumn
bstunRouteGroupIndex=_BstunRouteGroupIndex_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,1),_BstunRouteGroupIndex_Type())
bstunRouteGroupIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:bstunRouteGroupIndex.setStatus(_B)
class _BstunRouteStationAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_BstunRouteStationAddress_Type.__name__=_D
_BstunRouteStationAddress_Object=MibTableColumn
bstunRouteStationAddress=_BstunRouteStationAddress_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,2),_BstunRouteStationAddress_Type())
bstunRouteStationAddress.setMaxAccess(_V)
if mibBuilder.loadTexts:bstunRouteStationAddress.setStatus(_B)
class _BstunRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),('ip',2),(_h,3),(_i,4),(_j,5),(_k,6),('bip',7),('apip',8)))
_BstunRouteType_Type.__name__=_D
_BstunRouteType_Object=MibTableColumn
bstunRouteType=_BstunRouteType_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,3),_BstunRouteType_Type())
bstunRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteType.setStatus(_B)
_BstunRouteIP_Type=IpAddress
_BstunRouteIP_Object=MibTableColumn
bstunRouteIP=_BstunRouteIP_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,4),_BstunRouteIP_Type())
bstunRouteIP.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteIP.setStatus(_B)
_BstunRouteSerial_Type=InterfaceIndex
_BstunRouteSerial_Object=MibTableColumn
bstunRouteSerial=_BstunRouteSerial_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,5),_BstunRouteSerial_Type())
bstunRouteSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteSerial.setStatus(_B)
class _BstunRoutePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('normal',2),('medium',3),('high',4)))
_BstunRoutePriority_Type.__name__=_D
_BstunRoutePriority_Object=MibTableColumn
bstunRoutePriority=_BstunRoutePriority_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,6),_BstunRoutePriority_Type())
bstunRoutePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRoutePriority.setStatus(_B)
class _BstunRoutePeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dead',1),('closed',2),('opening',3),('openWait',4),('connected',5),('direct',6)))
_BstunRoutePeerState_Type.__name__=_D
_BstunRoutePeerState_Object=MibTableColumn
bstunRoutePeerState=_BstunRoutePeerState_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,7),_BstunRoutePeerState_Type())
bstunRoutePeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRoutePeerState.setStatus(_B)
_BstunRouteRxPackets_Type=Counter32
_BstunRouteRxPackets_Object=MibTableColumn
bstunRouteRxPackets=_BstunRouteRxPackets_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,8),_BstunRouteRxPackets_Type())
bstunRouteRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteRxPackets.setStatus(_B)
_BstunRouteTxPackets_Type=Counter32
_BstunRouteTxPackets_Object=MibTableColumn
bstunRouteTxPackets=_BstunRouteTxPackets_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,9),_BstunRouteTxPackets_Type())
bstunRouteTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteTxPackets.setStatus(_B)
_BstunRouteRxBytes_Type=Counter32
_BstunRouteRxBytes_Object=MibTableColumn
bstunRouteRxBytes=_BstunRouteRxBytes_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,10),_BstunRouteRxBytes_Type())
bstunRouteRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteRxBytes.setStatus(_B)
_BstunRouteTxBytes_Type=Counter32
_BstunRouteTxBytes_Object=MibTableColumn
bstunRouteTxBytes=_BstunRouteTxBytes_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,11),_BstunRouteTxBytes_Type())
bstunRouteTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteTxBytes.setStatus(_B)
class _BstunRouteDLCI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_BstunRouteDLCI_Type.__name__=_D
_BstunRouteDLCI_Object=MibTableColumn
bstunRouteDLCI=_BstunRouteDLCI_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,12),_BstunRouteDLCI_Type())
bstunRouteDLCI.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteDLCI.setStatus(_B)
class _BstunRouteRSAP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BstunRouteRSAP_Type.__name__=_D
_BstunRouteRSAP_Object=MibTableColumn
bstunRouteRSAP=_BstunRouteRSAP_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,13),_BstunRouteRSAP_Type())
bstunRouteRSAP.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteRSAP.setStatus(_B)
class _BstunLLC2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_BstunLLC2Priority_Type.__name__=_D
_BstunLLC2Priority_Object=MibTableColumn
bstunLLC2Priority=_BstunLLC2Priority_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,14),_BstunLLC2Priority_Type())
bstunLLC2Priority.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunLLC2Priority.setStatus(_B)
class _BstunRouteBIPPassive_Type(TruthValue):defaultValue=2
_BstunRouteBIPPassive_Type.__name__=_f
_BstunRouteBIPPassive_Object=MibTableColumn
bstunRouteBIPPassive=_BstunRouteBIPPassive_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,15),_BstunRouteBIPPassive_Type())
bstunRouteBIPPassive.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteBIPPassive.setStatus(_B)
class _BstunRouteBIPLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,32000))
_BstunRouteBIPLocalPort_Type.__name__=_D
_BstunRouteBIPLocalPort_Object=MibTableColumn
bstunRouteBIPLocalPort=_BstunRouteBIPLocalPort_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,16),_BstunRouteBIPLocalPort_Type())
bstunRouteBIPLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteBIPLocalPort.setStatus(_B)
class _BstunRouteBIPForeignPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,32000))
_BstunRouteBIPForeignPort_Type.__name__=_D
_BstunRouteBIPForeignPort_Object=MibTableColumn
bstunRouteBIPForeignPort=_BstunRouteBIPForeignPort_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,17),_BstunRouteBIPForeignPort_Type())
bstunRouteBIPForeignPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteBIPForeignPort.setStatus(_B)
class _BstunRouteBIPDeviceStatus_Type(Bits):namedValues=NamedValues(*(('operationcheck',0),('reservedBit1',1),('datacheck',2),('equipmentcheck',3),('interventionrequired',4),('commandreject',5),('deviceinactive',6),('deviceactive',7),('reservedBit8',8),('deviceend',9),('unitspecify',10),('devicebusy',11)))
_BstunRouteBIPDeviceStatus_Type.__name__='Bits'
_BstunRouteBIPDeviceStatus_Object=MibTableColumn
bstunRouteBIPDeviceStatus=_BstunRouteBIPDeviceStatus_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,18),_BstunRouteBIPDeviceStatus_Type())
bstunRouteBIPDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteBIPDeviceStatus.setStatus(_B)
class _BstunRouteAPIPHeaderVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v0',1),('v1',2),('v2',3)))
_BstunRouteAPIPHeaderVersion_Type.__name__=_D
_BstunRouteAPIPHeaderVersion_Object=MibTableColumn
bstunRouteAPIPHeaderVersion=_BstunRouteAPIPHeaderVersion_Object((1,3,6,1,4,1,9,9,35,1,4,1,1,19),_BstunRouteAPIPHeaderVersion_Type())
bstunRouteAPIPHeaderVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:bstunRouteAPIPHeaderVersion.setStatus(_B)
_BstunNotificationPrefix_ObjectIdentity=ObjectIdentity
bstunNotificationPrefix=_BstunNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,35,2))
_BstunNotifications_ObjectIdentity=ObjectIdentity
bstunNotifications=_BstunNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,35,2,0))
_BstunMibConformance_ObjectIdentity=ObjectIdentity
bstunMibConformance=_BstunMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,35,3))
_BstunMibCompliances_ObjectIdentity=ObjectIdentity
bstunMibCompliances=_BstunMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,35,3,1))
_BstunMibGroups_ObjectIdentity=ObjectIdentity
bstunMibGroups=_BstunMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,35,3,2))
bstunGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,1))
bstunGlobalGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:bstunGlobalGroup.setStatus(_L)
bstunGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,2))
bstunGroupGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:bstunGroupGroup.setStatus(_B)
bstunPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,3))
bstunPortGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:bstunPortGroup.setStatus(_B)
bstunRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,4))
bstunRouteGroup.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_E),(_A,_H),(_A,_I),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:bstunRouteGroup.setStatus(_L)
bstunGlobalGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,5))
bstunGlobalGroupRev1.setObjects(*((_A,_W),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:bstunGlobalGroupRev1.setStatus(_B)
bstunRouteGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,6))
bstunRouteGroupRev1.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_E),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:bstunRouteGroupRev1.setStatus(_B)
bstunRouteGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,7))
bstunRouteGroupRev2.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_E),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:bstunRouteGroupRev2.setStatus(_T)
bstunRouteBipGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,10))
bstunRouteBipGroup.setObjects(*((_A,_a),(_A,_S)))
if mibBuilder.loadTexts:bstunRouteBipGroup.setStatus(_B)
bstunRoutePortsGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,11))
bstunRoutePortsGroup.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:bstunRoutePortsGroup.setStatus(_B)
bstunRouteApipGroup=ObjectGroup((1,3,6,1,4,1,9,9,35,3,2,12))
bstunRouteApipGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:bstunRouteApipGroup.setStatus(_B)
bstunPeerStateChangeNotification=NotificationType((1,3,6,1,4,1,9,9,35,2,0,1))
bstunPeerStateChangeNotification.setObjects((_A,_E))
if mibBuilder.loadTexts:bstunPeerStateChangeNotification.setStatus(_T)
bstunPeerStateChangeNotification2=NotificationType((1,3,6,1,4,1,9,9,35,2,0,2))
bstunPeerStateChangeNotification2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:bstunPeerStateChangeNotification2.setStatus(_B)
bstunCUStatusChangeNotification=NotificationType((1,3,6,1,4,1,9,9,35,2,0,3))
bstunCUStatusChangeNotification.setObjects(*((_A,_G),(_A,_R),(_A,_Q),(_A,_S)))
if mibBuilder.loadTexts:bstunCUStatusChangeNotification.setStatus(_B)
bstunNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,35,3,2,8))
bstunNotificationGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:bstunNotificationGroup.setStatus(_T)
bstunNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,35,3,2,9))
bstunNotificationGroupRev1.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:bstunNotificationGroupRev1.setStatus(_B)
bstunMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,35,3,1,1))
bstunMibCompliance.setObjects(*((_A,_A2),(_A,_J),(_A,_K),(_A,_A3)))
if mibBuilder.loadTexts:bstunMibCompliance.setStatus(_L)
bstunMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,35,3,1,2))
bstunMibComplianceRev1.setObjects(*((_A,_U),(_A,_J),(_A,_K),(_A,_b)))
if mibBuilder.loadTexts:bstunMibComplianceRev1.setStatus(_L)
bstunMibComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,35,3,1,3))
bstunMibComplianceRev2.setObjects(*((_A,_U),(_A,_J),(_A,_K),(_A,_A4),(_A,_c)))
if mibBuilder.loadTexts:bstunMibComplianceRev2.setStatus(_T)
bstunMibComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,35,3,1,4))
bstunMibComplianceRev3.setObjects(*((_A,_U),(_A,_J),(_A,_K),(_A,_b),(_A,_c),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:bstunMibComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoBstunMIB':ciscoBstunMIB,'bstunObjects':bstunObjects,'bstunGlobal':bstunGlobal,_W:bstunIPAddr,_v:bstunLisnSap,_w:bstunPeerKeepaliveInterval,_x:bstunPeerKeepaliveLimit,'bstunGroups':bstunGroups,'bstunGroupTable':bstunGroupTable,'bstunGroupEntry':bstunGroupEntry,_g:bstunGroupIndex,_n:bstunProtocolType,_o:bstunLocalAck,_p:bstunGroupUnroutableTransmit,_q:bstunGroupUnroutableReceive,'bstunPorts':bstunPorts,'bstunPortTable':bstunPortTable,'bstunPortEntry':bstunPortEntry,_r:bstunPortGroupNumber,_s:bstunPortDefaultPeerType,_t:bstunPortDefaultPeerIP,_u:bstunPortDefaultPeerSerial,'bstunRoutes':bstunRoutes,'bstunRouteTable':bstunRouteTable,'bstunRouteEntry':bstunRouteEntry,_l:bstunRouteGroupIndex,_m:bstunRouteStationAddress,_F:bstunRouteType,_G:bstunRouteIP,_M:bstunRouteSerial,_N:bstunRoutePriority,_E:bstunRoutePeerState,_H:bstunRouteRxPackets,_I:bstunRouteTxPackets,_O:bstunRouteRxBytes,_P:bstunRouteTxBytes,_X:bstunRouteDLCI,_Y:bstunRouteRSAP,_Z:bstunLLC2Priority,_a:bstunRouteBIPPassive,_Q:bstunRouteBIPLocalPort,_R:bstunRouteBIPForeignPort,_S:bstunRouteBIPDeviceStatus,_y:bstunRouteAPIPHeaderVersion,'bstunNotificationPrefix':bstunNotificationPrefix,'bstunNotifications':bstunNotifications,_z:bstunPeerStateChangeNotification,_A0:bstunPeerStateChangeNotification2,_A1:bstunCUStatusChangeNotification,'bstunMibConformance':bstunMibConformance,'bstunMibCompliances':bstunMibCompliances,'bstunMibCompliance':bstunMibCompliance,'bstunMibComplianceRev1':bstunMibComplianceRev1,'bstunMibComplianceRev2':bstunMibComplianceRev2,'bstunMibComplianceRev3':bstunMibComplianceRev3,'bstunMibGroups':bstunMibGroups,_A2:bstunGlobalGroup,_J:bstunGroupGroup,_K:bstunPortGroup,_A3:bstunRouteGroup,_U:bstunGlobalGroupRev1,_b:bstunRouteGroupRev1,_A4:bstunRouteGroupRev2,'bstunNotificationGroup':bstunNotificationGroup,_c:bstunNotificationGroupRev1,_A5:bstunRouteBipGroup,_A6:bstunRoutePortsGroup,_A7:bstunRouteApipGroup})