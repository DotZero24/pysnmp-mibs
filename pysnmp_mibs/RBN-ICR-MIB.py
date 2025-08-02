_c='rbnIcrNotificationGroup'
_b='rbnIcrNotificationObjectGroup'
_a='rbnIcrGroup'
_Z='rbnIcrInconsistency'
_Y='rbnIcrNewPendingStandby'
_X='rbnIcrNewStandby'
_W='rbnIcrNewActive'
_V='rbnIcrRowStatus'
_U='rbnIcrAdminStatus'
_T='rbnIcrHoldTime'
_S='rbnIcrKeepAliveInterval'
_R='rbnIcrPriority'
_Q='seconds'
_P='rbnIcrId'
_O='rbnIcrInconsistencyError'
_N='InetPortNumber'
_M='InetAddressType'
_L='InetAddress'
_K='rbnIcrState'
_J='rbnIcrPeerPort'
_I='rbnIcrPeerAddress'
_H='rbnIcrPeerAddressType'
_G='rbnIcrLocalPort'
_F='rbnIcrLocalAddress'
_E='rbnIcrLocalAddressType'
_D='Integer32'
_C='read-create'
_B='current'
_A='RBN-ICR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,_M,_N)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rbnIcrMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,101))
if mibBuilder.loadTexts:rbnIcrMIB.setRevisions(('2011-01-10 00:00',))
_RbnIcrNotifications_ObjectIdentity=ObjectIdentity
rbnIcrNotifications=_RbnIcrNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,101,0))
_RbnIcrMIBObjects_ObjectIdentity=ObjectIdentity
rbnIcrMIBObjects=_RbnIcrMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,101,1))
_RbnIcrTable_Object=MibTable
rbnIcrTable=_RbnIcrTable_Object((1,3,6,1,4,1,2352,2,101,1,1))
if mibBuilder.loadTexts:rbnIcrTable.setStatus(_B)
_RbnIcrEntry_Object=MibTableRow
rbnIcrEntry=_RbnIcrEntry_Object((1,3,6,1,4,1,2352,2,101,1,1,1))
rbnIcrEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:rbnIcrEntry.setStatus(_B)
class _RbnIcrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RbnIcrId_Type.__name__=_D
_RbnIcrId_Object=MibTableColumn
rbnIcrId=_RbnIcrId_Object((1,3,6,1,4,1,2352,2,101,1,1,1,1),_RbnIcrId_Type())
rbnIcrId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnIcrId.setStatus(_B)
class _RbnIcrLocalAddressType_Type(InetAddressType):defaultValue=0
_RbnIcrLocalAddressType_Type.__name__=_M
_RbnIcrLocalAddressType_Object=MibTableColumn
rbnIcrLocalAddressType=_RbnIcrLocalAddressType_Object((1,3,6,1,4,1,2352,2,101,1,1,1,2),_RbnIcrLocalAddressType_Type())
rbnIcrLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrLocalAddressType.setStatus(_B)
class _RbnIcrLocalAddress_Type(InetAddress):defaultHexValue=''
_RbnIcrLocalAddress_Type.__name__=_L
_RbnIcrLocalAddress_Object=MibTableColumn
rbnIcrLocalAddress=_RbnIcrLocalAddress_Object((1,3,6,1,4,1,2352,2,101,1,1,1,3),_RbnIcrLocalAddress_Type())
rbnIcrLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrLocalAddress.setStatus(_B)
class _RbnIcrLocalPort_Type(InetPortNumber):defaultValue=0
_RbnIcrLocalPort_Type.__name__=_N
_RbnIcrLocalPort_Object=MibTableColumn
rbnIcrLocalPort=_RbnIcrLocalPort_Object((1,3,6,1,4,1,2352,2,101,1,1,1,4),_RbnIcrLocalPort_Type())
rbnIcrLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrLocalPort.setStatus(_B)
class _RbnIcrPeerAddressType_Type(InetAddressType):defaultValue=0
_RbnIcrPeerAddressType_Type.__name__=_M
_RbnIcrPeerAddressType_Object=MibTableColumn
rbnIcrPeerAddressType=_RbnIcrPeerAddressType_Object((1,3,6,1,4,1,2352,2,101,1,1,1,5),_RbnIcrPeerAddressType_Type())
rbnIcrPeerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrPeerAddressType.setStatus(_B)
class _RbnIcrPeerAddress_Type(InetAddress):defaultHexValue=''
_RbnIcrPeerAddress_Type.__name__=_L
_RbnIcrPeerAddress_Object=MibTableColumn
rbnIcrPeerAddress=_RbnIcrPeerAddress_Object((1,3,6,1,4,1,2352,2,101,1,1,1,6),_RbnIcrPeerAddress_Type())
rbnIcrPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrPeerAddress.setStatus(_B)
class _RbnIcrPeerPort_Type(InetPortNumber):defaultValue=0
_RbnIcrPeerPort_Type.__name__=_N
_RbnIcrPeerPort_Object=MibTableColumn
rbnIcrPeerPort=_RbnIcrPeerPort_Object((1,3,6,1,4,1,2352,2,101,1,1,1,7),_RbnIcrPeerPort_Type())
rbnIcrPeerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrPeerPort.setStatus(_B)
class _RbnIcrPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_RbnIcrPriority_Type.__name__=_D
_RbnIcrPriority_Object=MibTableColumn
rbnIcrPriority=_RbnIcrPriority_Object((1,3,6,1,4,1,2352,2,101,1,1,1,8),_RbnIcrPriority_Type())
rbnIcrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrPriority.setStatus(_B)
class _RbnIcrKeepAliveInterval_Type(Integer32):defaultValue=1
_RbnIcrKeepAliveInterval_Type.__name__=_D
_RbnIcrKeepAliveInterval_Object=MibTableColumn
rbnIcrKeepAliveInterval=_RbnIcrKeepAliveInterval_Object((1,3,6,1,4,1,2352,2,101,1,1,1,9),_RbnIcrKeepAliveInterval_Type())
rbnIcrKeepAliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrKeepAliveInterval.setStatus(_B)
if mibBuilder.loadTexts:rbnIcrKeepAliveInterval.setUnits(_Q)
class _RbnIcrHoldTime_Type(Integer32):defaultValue=10
_RbnIcrHoldTime_Type.__name__=_D
_RbnIcrHoldTime_Object=MibTableColumn
rbnIcrHoldTime=_RbnIcrHoldTime_Object((1,3,6,1,4,1,2352,2,101,1,1,1,10),_RbnIcrHoldTime_Type())
rbnIcrHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrHoldTime.setStatus(_B)
if mibBuilder.loadTexts:rbnIcrHoldTime.setUnits(_Q)
class _RbnIcrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initialize',1),('active',2),('standby',3),('pendingStandby',4)))
_RbnIcrState_Type.__name__=_D
_RbnIcrState_Object=MibTableColumn
rbnIcrState=_RbnIcrState_Object((1,3,6,1,4,1,2352,2,101,1,1,1,11),_RbnIcrState_Type())
rbnIcrState.setMaxAccess('read-only')
if mibBuilder.loadTexts:rbnIcrState.setStatus(_B)
class _RbnIcrAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RbnIcrAdminStatus_Type.__name__=_D
_RbnIcrAdminStatus_Object=MibTableColumn
rbnIcrAdminStatus=_RbnIcrAdminStatus_Object((1,3,6,1,4,1,2352,2,101,1,1,1,12),_RbnIcrAdminStatus_Type())
rbnIcrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrAdminStatus.setStatus(_B)
_RbnIcrRowStatus_Type=RowStatus
_RbnIcrRowStatus_Object=MibTableColumn
rbnIcrRowStatus=_RbnIcrRowStatus_Object((1,3,6,1,4,1,2352,2,101,1,1,1,13),_RbnIcrRowStatus_Type())
rbnIcrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIcrRowStatus.setStatus(_B)
class _RbnIcrInconsistencyError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('peerLoss',1))
_RbnIcrInconsistencyError_Type.__name__=_D
_RbnIcrInconsistencyError_Object=MibScalar
rbnIcrInconsistencyError=_RbnIcrInconsistencyError_Object((1,3,6,1,4,1,2352,2,101,1,2),_RbnIcrInconsistencyError_Type())
rbnIcrInconsistencyError.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:rbnIcrInconsistencyError.setStatus(_B)
_RbnIcrMIBConformance_ObjectIdentity=ObjectIdentity
rbnIcrMIBConformance=_RbnIcrMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,101,2))
_RbnIcrMIBCompliances_ObjectIdentity=ObjectIdentity
rbnIcrMIBCompliances=_RbnIcrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,101,2,1))
_RbnIcrMIBGroups_ObjectIdentity=ObjectIdentity
rbnIcrMIBGroups=_RbnIcrMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,101,2,2))
rbnIcrGroup=ObjectGroup((1,3,6,1,4,1,2352,2,101,2,2,1))
rbnIcrGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_R),(_A,_S),(_A,_T),(_A,_K),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:rbnIcrGroup.setStatus(_B)
rbnIcrNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,101,2,2,2))
rbnIcrNotificationObjectGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:rbnIcrNotificationObjectGroup.setStatus(_B)
rbnIcrNewActive=NotificationType((1,3,6,1,4,1,2352,2,101,0,1))
rbnIcrNewActive.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:rbnIcrNewActive.setStatus(_B)
rbnIcrNewStandby=NotificationType((1,3,6,1,4,1,2352,2,101,0,2))
rbnIcrNewStandby.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnIcrNewStandby.setStatus(_B)
rbnIcrNewPendingStandby=NotificationType((1,3,6,1,4,1,2352,2,101,0,3))
rbnIcrNewPendingStandby.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnIcrNewPendingStandby.setStatus(_B)
rbnIcrInconsistency=NotificationType((1,3,6,1,4,1,2352,2,101,0,4))
rbnIcrInconsistency.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_O)))
if mibBuilder.loadTexts:rbnIcrInconsistency.setStatus(_B)
rbnIcrNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,2,101,2,2,3))
rbnIcrNotificationGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:rbnIcrNotificationGroup.setStatus(_B)
rbnIcrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,101,2,1,1))
rbnIcrMIBCompliance.setObjects(*((_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:rbnIcrMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnIcrMIB':rbnIcrMIB,'rbnIcrNotifications':rbnIcrNotifications,_W:rbnIcrNewActive,_X:rbnIcrNewStandby,_Y:rbnIcrNewPendingStandby,_Z:rbnIcrInconsistency,'rbnIcrMIBObjects':rbnIcrMIBObjects,'rbnIcrTable':rbnIcrTable,'rbnIcrEntry':rbnIcrEntry,_P:rbnIcrId,_E:rbnIcrLocalAddressType,_F:rbnIcrLocalAddress,_G:rbnIcrLocalPort,_H:rbnIcrPeerAddressType,_I:rbnIcrPeerAddress,_J:rbnIcrPeerPort,_R:rbnIcrPriority,_S:rbnIcrKeepAliveInterval,_T:rbnIcrHoldTime,_K:rbnIcrState,_U:rbnIcrAdminStatus,_V:rbnIcrRowStatus,_O:rbnIcrInconsistencyError,'rbnIcrMIBConformance':rbnIcrMIBConformance,'rbnIcrMIBCompliances':rbnIcrMIBCompliances,'rbnIcrMIBCompliance':rbnIcrMIBCompliance,'rbnIcrMIBGroups':rbnIcrMIBGroups,_a:rbnIcrGroup,_b:rbnIcrNotificationObjectGroup,_c:rbnIcrNotificationGroup})