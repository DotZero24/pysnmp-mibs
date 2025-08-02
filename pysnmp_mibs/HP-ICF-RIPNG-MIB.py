_t='hpicfRipngNotificationGroup'
_s='hpicfRipngNotificationObjectGroup'
_r='hpicfRipngIfRxBadPacket'
_q='hpicfRipngIfConfigError'
_p='hpicfRipngIfStateChange'
_o='hpicfRipngPacketSrcType'
_n='hpicfRipngPeerRcvBadPackets'
_m='hpicfRipngPeerLastUpdate'
_l='hpicfRipngIfConfDoPoisonReverse'
_k='hpicfRipngIfConfSrcAddressType'
_j='hpicfRipngIfConfStatus'
_i='hpicfRipngIfConfMetric'
_h='hpicfRipngNotificationEnable'
_g='hpicfRipngGarbageCollectTime'
_f='hpicfRipngTimeoutTime'
_e='hpicfRipngUpdateTime'
_d='hpicfRipngDistance'
_c='hpicfRipngDefaultMetric'
_b='hpicfRipngAdminStatus'
_a='hpicfRipngGlobalQueries'
_Z='hpicfRipngGlobalRouteChanges'
_Y='hpicfRipngPeerAddress'
_X='hpicfRipngPeerAddressType'
_W='hpicfRipngIfConfInstId'
_V='hpicfRipngIfConfIndex'
_U='TruthValue'
_T='OctetString'
_S='hpicfRipngPeerGroup'
_R='hpicfRipngIfConfGroup'
_Q='hpicfRipngBaseScalarsGroup'
_P='hpicfRipngConfigErrorType'
_O='read-create'
_N='seconds'
_M='hpicfRipngPacketSrc'
_L='hpicfRipngPacketType'
_K='not-accessible'
_J='Unsigned32'
_I='InetAddress'
_H='hpicfRipngIfState'
_G='hpicfRipngIfConfSrcAddress'
_F='accessible-for-notify'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='HP-ICF-RIPNG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_U)
hpicfRipng=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113))
if mibBuilder.loadTexts:hpicfRipng.setRevisions(('2015-05-11 00:00',))
_HpicfRipngNotifications_ObjectIdentity=ObjectIdentity
hpicfRipngNotifications=_HpicfRipngNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,0))
_HpicfRipngObjects_ObjectIdentity=ObjectIdentity
hpicfRipngObjects=_HpicfRipngObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,1))
_HpicfRipngBaseScalars_ObjectIdentity=ObjectIdentity
hpicfRipngBaseScalars=_HpicfRipngBaseScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1))
_HpicfRipngGlobalRouteChanges_Type=Counter32
_HpicfRipngGlobalRouteChanges_Object=MibScalar
hpicfRipngGlobalRouteChanges=_HpicfRipngGlobalRouteChanges_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,1),_HpicfRipngGlobalRouteChanges_Type())
hpicfRipngGlobalRouteChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfRipngGlobalRouteChanges.setStatus(_B)
_HpicfRipngGlobalQueries_Type=Counter32
_HpicfRipngGlobalQueries_Object=MibScalar
hpicfRipngGlobalQueries=_HpicfRipngGlobalQueries_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,2),_HpicfRipngGlobalQueries_Type())
hpicfRipngGlobalQueries.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfRipngGlobalQueries.setStatus(_B)
class _HpicfRipngAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfRipngAdminStatus_Type.__name__=_C
_HpicfRipngAdminStatus_Object=MibScalar
hpicfRipngAdminStatus=_HpicfRipngAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,3),_HpicfRipngAdminStatus_Type())
hpicfRipngAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngAdminStatus.setStatus(_B)
class _HpicfRipngDefaultMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpicfRipngDefaultMetric_Type.__name__=_C
_HpicfRipngDefaultMetric_Object=MibScalar
hpicfRipngDefaultMetric=_HpicfRipngDefaultMetric_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,4),_HpicfRipngDefaultMetric_Type())
hpicfRipngDefaultMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngDefaultMetric.setStatus(_B)
class _HpicfRipngDistance_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpicfRipngDistance_Type.__name__=_C
_HpicfRipngDistance_Object=MibScalar
hpicfRipngDistance=_HpicfRipngDistance_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,5),_HpicfRipngDistance_Type())
hpicfRipngDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngDistance.setStatus(_B)
class _HpicfRipngUpdateTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,65535))
_HpicfRipngUpdateTime_Type.__name__=_J
_HpicfRipngUpdateTime_Object=MibScalar
hpicfRipngUpdateTime=_HpicfRipngUpdateTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,6),_HpicfRipngUpdateTime_Type())
hpicfRipngUpdateTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngUpdateTime.setStatus(_B)
if mibBuilder.loadTexts:hpicfRipngUpdateTime.setUnits(_N)
class _HpicfRipngTimeoutTime_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,65535))
_HpicfRipngTimeoutTime_Type.__name__=_J
_HpicfRipngTimeoutTime_Object=MibScalar
hpicfRipngTimeoutTime=_HpicfRipngTimeoutTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,7),_HpicfRipngTimeoutTime_Type())
hpicfRipngTimeoutTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngTimeoutTime.setStatus(_B)
if mibBuilder.loadTexts:hpicfRipngTimeoutTime.setUnits(_N)
class _HpicfRipngGarbageCollectTime_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,65535))
_HpicfRipngGarbageCollectTime_Type.__name__=_J
_HpicfRipngGarbageCollectTime_Object=MibScalar
hpicfRipngGarbageCollectTime=_HpicfRipngGarbageCollectTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,8),_HpicfRipngGarbageCollectTime_Type())
hpicfRipngGarbageCollectTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngGarbageCollectTime.setStatus(_B)
if mibBuilder.loadTexts:hpicfRipngGarbageCollectTime.setUnits(_N)
class _HpicfRipngNotificationEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpicfRipngNotificationEnable_Type.__name__=_T
_HpicfRipngNotificationEnable_Object=MibScalar
hpicfRipngNotificationEnable=_HpicfRipngNotificationEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,1,9),_HpicfRipngNotificationEnable_Type())
hpicfRipngNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfRipngNotificationEnable.setStatus(_B)
_HpicfRipngIfConfTable_Object=MibTable
hpicfRipngIfConfTable=_HpicfRipngIfConfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2))
if mibBuilder.loadTexts:hpicfRipngIfConfTable.setStatus(_B)
_HpicfRipngIfConfEntry_Object=MibTableRow
hpicfRipngIfConfEntry=_HpicfRipngIfConfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1))
hpicfRipngIfConfEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:hpicfRipngIfConfEntry.setStatus(_B)
_HpicfRipngIfConfIndex_Type=InterfaceIndex
_HpicfRipngIfConfIndex_Object=MibTableColumn
hpicfRipngIfConfIndex=_HpicfRipngIfConfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,1),_HpicfRipngIfConfIndex_Type())
hpicfRipngIfConfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfRipngIfConfIndex.setStatus(_B)
class _HpicfRipngIfConfInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpicfRipngIfConfInstId_Type.__name__=_C
_HpicfRipngIfConfInstId_Object=MibTableColumn
hpicfRipngIfConfInstId=_HpicfRipngIfConfInstId_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,2),_HpicfRipngIfConfInstId_Type())
hpicfRipngIfConfInstId.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfRipngIfConfInstId.setStatus(_B)
class _HpicfRipngIfConfMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpicfRipngIfConfMetric_Type.__name__=_C
_HpicfRipngIfConfMetric_Object=MibTableColumn
hpicfRipngIfConfMetric=_HpicfRipngIfConfMetric_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,3),_HpicfRipngIfConfMetric_Type())
hpicfRipngIfConfMetric.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfRipngIfConfMetric.setStatus(_B)
_HpicfRipngIfConfStatus_Type=RowStatus
_HpicfRipngIfConfStatus_Object=MibTableColumn
hpicfRipngIfConfStatus=_HpicfRipngIfConfStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,4),_HpicfRipngIfConfStatus_Type())
hpicfRipngIfConfStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfRipngIfConfStatus.setStatus(_B)
_HpicfRipngIfConfSrcAddressType_Type=InetAddressType
_HpicfRipngIfConfSrcAddressType_Object=MibTableColumn
hpicfRipngIfConfSrcAddressType=_HpicfRipngIfConfSrcAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,5),_HpicfRipngIfConfSrcAddressType_Type())
hpicfRipngIfConfSrcAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfRipngIfConfSrcAddressType.setStatus(_B)
class _HpicfRipngIfConfSrcAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_HpicfRipngIfConfSrcAddress_Type.__name__=_I
_HpicfRipngIfConfSrcAddress_Object=MibTableColumn
hpicfRipngIfConfSrcAddress=_HpicfRipngIfConfSrcAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,6),_HpicfRipngIfConfSrcAddress_Type())
hpicfRipngIfConfSrcAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfRipngIfConfSrcAddress.setStatus(_B)
class _HpicfRipngIfConfDoPoisonReverse_Type(TruthValue):defaultValue=1
_HpicfRipngIfConfDoPoisonReverse_Type.__name__=_U
_HpicfRipngIfConfDoPoisonReverse_Object=MibTableColumn
hpicfRipngIfConfDoPoisonReverse=_HpicfRipngIfConfDoPoisonReverse_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,2,1,7),_HpicfRipngIfConfDoPoisonReverse_Type())
hpicfRipngIfConfDoPoisonReverse.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfRipngIfConfDoPoisonReverse.setStatus(_B)
_HpicfRipngPeerTable_Object=MibTable
hpicfRipngPeerTable=_HpicfRipngPeerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,3))
if mibBuilder.loadTexts:hpicfRipngPeerTable.setStatus(_B)
_HpicfRipngPeerEntry_Object=MibTableRow
hpicfRipngPeerEntry=_HpicfRipngPeerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,3,1))
hpicfRipngPeerEntry.setIndexNames((0,_A,_X),(0,_A,_Y))
if mibBuilder.loadTexts:hpicfRipngPeerEntry.setStatus(_B)
_HpicfRipngPeerAddressType_Type=InetAddressType
_HpicfRipngPeerAddressType_Object=MibTableColumn
hpicfRipngPeerAddressType=_HpicfRipngPeerAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,3,1,1),_HpicfRipngPeerAddressType_Type())
hpicfRipngPeerAddressType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfRipngPeerAddressType.setStatus(_B)
class _HpicfRipngPeerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_HpicfRipngPeerAddress_Type.__name__=_I
_HpicfRipngPeerAddress_Object=MibTableColumn
hpicfRipngPeerAddress=_HpicfRipngPeerAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,3,1,2),_HpicfRipngPeerAddress_Type())
hpicfRipngPeerAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hpicfRipngPeerAddress.setStatus(_B)
_HpicfRipngPeerLastUpdate_Type=Unsigned32
_HpicfRipngPeerLastUpdate_Object=MibTableColumn
hpicfRipngPeerLastUpdate=_HpicfRipngPeerLastUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,3,1,3),_HpicfRipngPeerLastUpdate_Type())
hpicfRipngPeerLastUpdate.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfRipngPeerLastUpdate.setStatus(_B)
_HpicfRipngPeerRcvBadPackets_Type=Counter32
_HpicfRipngPeerRcvBadPackets_Object=MibTableColumn
hpicfRipngPeerRcvBadPackets=_HpicfRipngPeerRcvBadPackets_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,3,1,4),_HpicfRipngPeerRcvBadPackets_Type())
hpicfRipngPeerRcvBadPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfRipngPeerRcvBadPackets.setStatus(_B)
_HpicfRipngNotificationEntry_ObjectIdentity=ObjectIdentity
hpicfRipngNotificationEntry=_HpicfRipngNotificationEntry_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,1,4))
class _HpicfRipngConfigErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('badVersion',1),('badIPtype',2),('badHop',3),('badField',4),('ownPkt',5),('noError',6)))
_HpicfRipngConfigErrorType_Type.__name__=_C
_HpicfRipngConfigErrorType_Object=MibScalar
hpicfRipngConfigErrorType=_HpicfRipngConfigErrorType_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,4,1),_HpicfRipngConfigErrorType_Type())
hpicfRipngConfigErrorType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfRipngConfigErrorType.setStatus(_B)
class _HpicfRipngPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('request',1),('response',2),('nullPacket',3)))
_HpicfRipngPacketType_Type.__name__=_C
_HpicfRipngPacketType_Object=MibScalar
hpicfRipngPacketType=_HpicfRipngPacketType_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,4,2),_HpicfRipngPacketType_Type())
hpicfRipngPacketType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfRipngPacketType.setStatus(_B)
_HpicfRipngPacketSrcType_Type=InetAddressType
_HpicfRipngPacketSrcType_Object=MibScalar
hpicfRipngPacketSrcType=_HpicfRipngPacketSrcType_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,4,3),_HpicfRipngPacketSrcType_Type())
hpicfRipngPacketSrcType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfRipngPacketSrcType.setStatus(_B)
class _HpicfRipngPacketSrc_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16))
_HpicfRipngPacketSrc_Type.__name__=_I
_HpicfRipngPacketSrc_Object=MibScalar
hpicfRipngPacketSrc=_HpicfRipngPacketSrc_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,4,4),_HpicfRipngPacketSrc_Type())
hpicfRipngPacketSrc.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfRipngPacketSrc.setStatus(_B)
class _HpicfRipngIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpicfRipngIfState_Type.__name__=_C
_HpicfRipngIfState_Object=MibScalar
hpicfRipngIfState=_HpicfRipngIfState_Object((1,3,6,1,4,1,11,2,14,11,5,1,113,1,4,5),_HpicfRipngIfState_Type())
hpicfRipngIfState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfRipngIfState.setStatus(_B)
_HpicfRipngConformance_ObjectIdentity=ObjectIdentity
hpicfRipngConformance=_HpicfRipngConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,2))
_HpicfRipngCompliances_ObjectIdentity=ObjectIdentity
hpicfRipngCompliances=_HpicfRipngCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,2,1))
_HpicfRipngGroups_ObjectIdentity=ObjectIdentity
hpicfRipngGroups=_HpicfRipngGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,113,2,2))
hpicfRipngBaseScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,113,2,2,1))
hpicfRipngBaseScalarsGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpicfRipngBaseScalarsGroup.setStatus(_B)
hpicfRipngIfConfGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,113,2,2,2))
hpicfRipngIfConfGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_G),(_A,_l)))
if mibBuilder.loadTexts:hpicfRipngIfConfGroup.setStatus(_B)
hpicfRipngPeerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,113,2,2,3))
hpicfRipngPeerGroup.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:hpicfRipngPeerGroup.setStatus(_B)
hpicfRipngNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,113,2,2,4))
hpicfRipngNotificationObjectGroup.setObjects(*((_A,_P),(_A,_L),(_A,_o),(_A,_M),(_A,_H)))
if mibBuilder.loadTexts:hpicfRipngNotificationObjectGroup.setStatus(_B)
hpicfRipngIfStateChange=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,113,0,1))
hpicfRipngIfStateChange.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpicfRipngIfStateChange.setStatus(_B)
hpicfRipngIfConfigError=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,113,0,2))
hpicfRipngIfConfigError.setObjects(*((_A,_G),(_A,_H),(_A,_M),(_A,_P),(_A,_L)))
if mibBuilder.loadTexts:hpicfRipngIfConfigError.setStatus(_B)
hpicfRipngIfRxBadPacket=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,113,0,3))
hpicfRipngIfRxBadPacket.setObjects(*((_A,_G),(_A,_H),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:hpicfRipngIfRxBadPacket.setStatus(_B)
hpicfRipngNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,113,2,2,5))
hpicfRipngNotificationGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:hpicfRipngNotificationGroup.setStatus(_B)
hpicfRipngCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,113,2,1,1))
hpicfRipngCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_Q),(_A,_R),(_A,_S),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:hpicfRipngCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfRipng':hpicfRipng,'hpicfRipngNotifications':hpicfRipngNotifications,_p:hpicfRipngIfStateChange,_q:hpicfRipngIfConfigError,_r:hpicfRipngIfRxBadPacket,'hpicfRipngObjects':hpicfRipngObjects,'hpicfRipngBaseScalars':hpicfRipngBaseScalars,_Z:hpicfRipngGlobalRouteChanges,_a:hpicfRipngGlobalQueries,_b:hpicfRipngAdminStatus,_c:hpicfRipngDefaultMetric,_d:hpicfRipngDistance,_e:hpicfRipngUpdateTime,_f:hpicfRipngTimeoutTime,_g:hpicfRipngGarbageCollectTime,_h:hpicfRipngNotificationEnable,'hpicfRipngIfConfTable':hpicfRipngIfConfTable,'hpicfRipngIfConfEntry':hpicfRipngIfConfEntry,_V:hpicfRipngIfConfIndex,_W:hpicfRipngIfConfInstId,_i:hpicfRipngIfConfMetric,_j:hpicfRipngIfConfStatus,_k:hpicfRipngIfConfSrcAddressType,_G:hpicfRipngIfConfSrcAddress,_l:hpicfRipngIfConfDoPoisonReverse,'hpicfRipngPeerTable':hpicfRipngPeerTable,'hpicfRipngPeerEntry':hpicfRipngPeerEntry,_X:hpicfRipngPeerAddressType,_Y:hpicfRipngPeerAddress,_m:hpicfRipngPeerLastUpdate,_n:hpicfRipngPeerRcvBadPackets,'hpicfRipngNotificationEntry':hpicfRipngNotificationEntry,_P:hpicfRipngConfigErrorType,_L:hpicfRipngPacketType,_o:hpicfRipngPacketSrcType,_M:hpicfRipngPacketSrc,_H:hpicfRipngIfState,'hpicfRipngConformance':hpicfRipngConformance,'hpicfRipngCompliances':hpicfRipngCompliances,'hpicfRipngCompliance':hpicfRipngCompliance,'hpicfRipngGroups':hpicfRipngGroups,_Q:hpicfRipngBaseScalarsGroup,_R:hpicfRipngIfConfGroup,_S:hpicfRipngPeerGroup,_s:hpicfRipngNotificationObjectGroup,_t:hpicfRipngNotificationGroup})