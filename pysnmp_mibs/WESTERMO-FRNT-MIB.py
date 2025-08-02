_c='frntNotificationsGroup'
_b='frntPortStatusGroup'
_a='frntStatusGroup'
_Z='frntRingBroken'
_Y='frntRingOK'
_X='frntPortStatusLinkState'
_W='frntPortStatusOperState'
_V='frntPortStatusAdminState'
_U='frntStatusTimeSinceLastChange'
_T='frntStatusTopologyChangeCount'
_S='frntStatusVid2'
_R='frntStatusVid1'
_Q='frntStatusBlockingPort'
_P='disabled'
_O='frntPortStatusRefIndex'
_N='frntPortStatusFrntRingId'
_M='frntStatusInstance'
_L='frntStatusVersion'
_K='unknown'
_J='frntStatusPort2'
_I='frntStatusPort1'
_H='frntStatusRingStatus'
_G='frntStatusDeviceMode'
_F='frntStatusRingId'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='current'
_A='WESTERMO-FRNT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
IfaceRefIndex,=mibBuilder.importSymbols('WESTERMO-INTERFACE-MIB','IfaceRefIndex')
common,=mibBuilder.importSymbols('WESTERMO-OID-MIB','common')
frnt=ModuleIdentity((1,3,6,1,4,1,16177,2,5))
if mibBuilder.loadTexts:frnt.setRevisions(('2019-08-30 00:00','2019-12-11 00:00'))
_FrntObjects_ObjectIdentity=ObjectIdentity
frntObjects=_FrntObjects_ObjectIdentity((1,3,6,1,4,1,16177,2,5,1))
_FrntStatusTable_Object=MibTable
frntStatusTable=_FrntStatusTable_Object((1,3,6,1,4,1,16177,2,5,1,1))
if mibBuilder.loadTexts:frntStatusTable.setStatus(_B)
_FrntStatusEntry_Object=MibTableRow
frntStatusEntry=_FrntStatusEntry_Object((1,3,6,1,4,1,16177,2,5,1,1,1))
frntStatusEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:frntStatusEntry.setStatus(_B)
class _FrntStatusVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('v0',0),('v2',2)))
_FrntStatusVersion_Type.__name__=_D
_FrntStatusVersion_Object=MibTableColumn
frntStatusVersion=_FrntStatusVersion_Object((1,3,6,1,4,1,16177,2,5,1,1,1,1),_FrntStatusVersion_Type())
frntStatusVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:frntStatusVersion.setStatus(_B)
class _FrntStatusInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FrntStatusInstance_Type.__name__=_D
_FrntStatusInstance_Object=MibTableColumn
frntStatusInstance=_FrntStatusInstance_Object((1,3,6,1,4,1,16177,2,5,1,1,1,2),_FrntStatusInstance_Type())
frntStatusInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:frntStatusInstance.setStatus(_B)
_FrntStatusRingId_Type=Integer32
_FrntStatusRingId_Object=MibTableColumn
frntStatusRingId=_FrntStatusRingId_Object((1,3,6,1,4,1,16177,2,5,1,1,1,3),_FrntStatusRingId_Type())
frntStatusRingId.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusRingId.setStatus(_B)
class _FrntStatusDeviceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('member',1),('focalPoint',2)))
_FrntStatusDeviceMode_Type.__name__=_D
_FrntStatusDeviceMode_Object=MibTableColumn
frntStatusDeviceMode=_FrntStatusDeviceMode_Object((1,3,6,1,4,1,16177,2,5,1,1,1,4),_FrntStatusDeviceMode_Type())
frntStatusDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusDeviceMode.setStatus(_B)
class _FrntStatusRingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('broken',0),('ok',1)))
_FrntStatusRingStatus_Type.__name__=_D
_FrntStatusRingStatus_Object=MibTableColumn
frntStatusRingStatus=_FrntStatusRingStatus_Object((1,3,6,1,4,1,16177,2,5,1,1,1,5),_FrntStatusRingStatus_Type())
frntStatusRingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusRingStatus.setStatus(_B)
_FrntStatusPort1_Type=IfaceRefIndex
_FrntStatusPort1_Object=MibTableColumn
frntStatusPort1=_FrntStatusPort1_Object((1,3,6,1,4,1,16177,2,5,1,1,1,6),_FrntStatusPort1_Type())
frntStatusPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusPort1.setStatus(_B)
_FrntStatusPort2_Type=IfaceRefIndex
_FrntStatusPort2_Object=MibTableColumn
frntStatusPort2=_FrntStatusPort2_Object((1,3,6,1,4,1,16177,2,5,1,1,1,7),_FrntStatusPort2_Type())
frntStatusPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusPort2.setStatus(_B)
_FrntStatusBlockingPort_Type=IfaceRefIndex
_FrntStatusBlockingPort_Object=MibTableColumn
frntStatusBlockingPort=_FrntStatusBlockingPort_Object((1,3,6,1,4,1,16177,2,5,1,1,1,8),_FrntStatusBlockingPort_Type())
frntStatusBlockingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusBlockingPort.setStatus(_B)
_FrntStatusVid1_Type=Integer32
_FrntStatusVid1_Object=MibTableColumn
frntStatusVid1=_FrntStatusVid1_Object((1,3,6,1,4,1,16177,2,5,1,1,1,9),_FrntStatusVid1_Type())
frntStatusVid1.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusVid1.setStatus(_B)
_FrntStatusVid2_Type=Integer32
_FrntStatusVid2_Object=MibTableColumn
frntStatusVid2=_FrntStatusVid2_Object((1,3,6,1,4,1,16177,2,5,1,1,1,10),_FrntStatusVid2_Type())
frntStatusVid2.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusVid2.setStatus(_B)
_FrntStatusTopologyChangeCount_Type=Integer32
_FrntStatusTopologyChangeCount_Object=MibTableColumn
frntStatusTopologyChangeCount=_FrntStatusTopologyChangeCount_Object((1,3,6,1,4,1,16177,2,5,1,1,1,11),_FrntStatusTopologyChangeCount_Type())
frntStatusTopologyChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusTopologyChangeCount.setStatus(_B)
_FrntStatusTimeSinceLastChange_Type=TimeTicks
_FrntStatusTimeSinceLastChange_Object=MibTableColumn
frntStatusTimeSinceLastChange=_FrntStatusTimeSinceLastChange_Object((1,3,6,1,4,1,16177,2,5,1,1,1,12),_FrntStatusTimeSinceLastChange_Type())
frntStatusTimeSinceLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:frntStatusTimeSinceLastChange.setStatus(_B)
_FrntPortStatusTable_Object=MibTable
frntPortStatusTable=_FrntPortStatusTable_Object((1,3,6,1,4,1,16177,2,5,1,2))
if mibBuilder.loadTexts:frntPortStatusTable.setStatus(_B)
_FrntPortStatusEntry_Object=MibTableRow
frntPortStatusEntry=_FrntPortStatusEntry_Object((1,3,6,1,4,1,16177,2,5,1,2,1))
frntPortStatusEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:frntPortStatusEntry.setStatus(_B)
class _FrntPortStatusFrntRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_FrntPortStatusFrntRingId_Type.__name__=_D
_FrntPortStatusFrntRingId_Object=MibTableColumn
frntPortStatusFrntRingId=_FrntPortStatusFrntRingId_Object((1,3,6,1,4,1,16177,2,5,1,2,1,1),_FrntPortStatusFrntRingId_Type())
frntPortStatusFrntRingId.setMaxAccess(_E)
if mibBuilder.loadTexts:frntPortStatusFrntRingId.setStatus(_B)
_FrntPortStatusRefIndex_Type=IfaceRefIndex
_FrntPortStatusRefIndex_Object=MibTableColumn
frntPortStatusRefIndex=_FrntPortStatusRefIndex_Object((1,3,6,1,4,1,16177,2,5,1,2,1,2),_FrntPortStatusRefIndex_Type())
frntPortStatusRefIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:frntPortStatusRefIndex.setStatus(_B)
class _FrntPortStatusAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('enabled',1),(_P,2)))
_FrntPortStatusAdminState_Type.__name__=_D
_FrntPortStatusAdminState_Object=MibTableColumn
frntPortStatusAdminState=_FrntPortStatusAdminState_Object((1,3,6,1,4,1,16177,2,5,1,2,1,3),_FrntPortStatusAdminState_Type())
frntPortStatusAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:frntPortStatusAdminState.setStatus(_B)
class _FrntPortStatusOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_K,0),(_P,1),('down',2),('notQualified',3),('qualified',4),('forwarding',5)))
_FrntPortStatusOperState_Type.__name__=_D
_FrntPortStatusOperState_Object=MibTableColumn
frntPortStatusOperState=_FrntPortStatusOperState_Object((1,3,6,1,4,1,16177,2,5,1,2,1,4),_FrntPortStatusOperState_Type())
frntPortStatusOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:frntPortStatusOperState.setStatus(_B)
class _FrntPortStatusLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('up',1),('down',2)))
_FrntPortStatusLinkState_Type.__name__=_D
_FrntPortStatusLinkState_Object=MibTableColumn
frntPortStatusLinkState=_FrntPortStatusLinkState_Object((1,3,6,1,4,1,16177,2,5,1,2,1,5),_FrntPortStatusLinkState_Type())
frntPortStatusLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:frntPortStatusLinkState.setStatus(_B)
_FrntConformance_ObjectIdentity=ObjectIdentity
frntConformance=_FrntConformance_ObjectIdentity((1,3,6,1,4,1,16177,2,5,2))
_FrntGroups_ObjectIdentity=ObjectIdentity
frntGroups=_FrntGroups_ObjectIdentity((1,3,6,1,4,1,16177,2,5,2,1))
_FrntCompliances_ObjectIdentity=ObjectIdentity
frntCompliances=_FrntCompliances_ObjectIdentity((1,3,6,1,4,1,16177,2,5,2,2))
_FrntNotifications_ObjectIdentity=ObjectIdentity
frntNotifications=_FrntNotifications_ObjectIdentity((1,3,6,1,4,1,16177,2,5,3))
_FrntNotificationPrefix_ObjectIdentity=ObjectIdentity
frntNotificationPrefix=_FrntNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,16177,2,5,3,0))
frntStatusGroup=ObjectGroup((1,3,6,1,4,1,16177,2,5,2,1,1))
frntStatusGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:frntStatusGroup.setStatus(_B)
frntPortStatusGroup=ObjectGroup((1,3,6,1,4,1,16177,2,5,2,1,2))
frntPortStatusGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:frntPortStatusGroup.setStatus(_B)
frntRingOK=NotificationType((1,3,6,1,4,1,16177,2,5,3,0,1))
frntRingOK.setObjects(*((_A,_F),(_A,_H),(_A,_G),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:frntRingOK.setStatus(_B)
frntRingBroken=NotificationType((1,3,6,1,4,1,16177,2,5,3,0,2))
frntRingBroken.setObjects(*((_A,_F),(_A,_H),(_A,_G),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:frntRingBroken.setStatus(_B)
frntNotificationsGroup=NotificationGroup((1,3,6,1,4,1,16177,2,5,2,1,3))
frntNotificationsGroup.setObjects(*((_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:frntNotificationsGroup.setStatus(_B)
frntCompliance=ModuleCompliance((1,3,6,1,4,1,16177,2,5,2,2,1))
frntCompliance.setObjects(*((_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:frntCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'frnt':frnt,'frntObjects':frntObjects,'frntStatusTable':frntStatusTable,'frntStatusEntry':frntStatusEntry,_L:frntStatusVersion,_M:frntStatusInstance,_F:frntStatusRingId,_G:frntStatusDeviceMode,_H:frntStatusRingStatus,_I:frntStatusPort1,_J:frntStatusPort2,_Q:frntStatusBlockingPort,_R:frntStatusVid1,_S:frntStatusVid2,_T:frntStatusTopologyChangeCount,_U:frntStatusTimeSinceLastChange,'frntPortStatusTable':frntPortStatusTable,'frntPortStatusEntry':frntPortStatusEntry,_N:frntPortStatusFrntRingId,_O:frntPortStatusRefIndex,_V:frntPortStatusAdminState,_W:frntPortStatusOperState,_X:frntPortStatusLinkState,'frntConformance':frntConformance,'frntGroups':frntGroups,_a:frntStatusGroup,_b:frntPortStatusGroup,_c:frntNotificationsGroup,'frntCompliances':frntCompliances,'frntCompliance':frntCompliance,'frntNotifications':frntNotifications,'frntNotificationPrefix':frntNotificationPrefix,_Y:frntRingOK,_Z:frntRingBroken})