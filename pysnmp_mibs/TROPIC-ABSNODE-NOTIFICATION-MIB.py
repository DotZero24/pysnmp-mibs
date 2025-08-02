_K='tnTrapServiceAffecting'
_J='current'
_I='tnTrapTime'
_H='tnTrapObjectIDType'
_G='tnTrapObjectID'
_F='tnTrapEntityType'
_E='tnTrapDescr'
_D='tnTrapData'
_C='tnTrapCondition'
_B='tnTrapCategory'
_A='TROPIC-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnAbsNodeMIBModules,=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnAbsNodeMIBModules')
tnNotificationObjs,tnTrapCategory,tnTrapCondition,tnTrapData,tnTrapDescr,tnTrapEntityType,tnTrapObjectID,tnTrapObjectIDType,tnTrapServiceAffecting,tnTrapTime=mibBuilder.importSymbols(_A,'tnNotificationObjs',_B,_C,_D,_E,_F,_G,_H,_K,_I)
tnAbsNodeNotificationMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,7,2))
if mibBuilder.loadTexts:tnAbsNodeNotificationMIBModule.setRevisions(('2018-02-23 12:00','2016-11-16 12:00','2016-10-18 12:00','2016-08-03 12:00','2016-02-26 12:00'))
_TnNotificationsAbsNode_ObjectIdentity=ObjectIdentity
tnNotificationsAbsNode=_TnNotificationsAbsNode_ObjectIdentity((1,3,6,1,4,1,7483,2,1,2,2,9))
_TnAlarmNotificationsAbsNode_ObjectIdentity=ObjectIdentity
tnAlarmNotificationsAbsNode=_TnAlarmNotificationsAbsNode_ObjectIdentity((1,3,6,1,4,1,7483,2,1,2,2,9,1))
_TnEventNotificationsAbsNode_ObjectIdentity=ObjectIdentity
tnEventNotificationsAbsNode=_TnEventNotificationsAbsNode_ObjectIdentity((1,3,6,1,4,1,7483,2,1,2,2,9,2))
tnAbsNodeRaisedNotif=NotificationType((1,3,6,1,4,1,7483,2,1,2,2,9,1,1))
tnAbsNodeRaisedNotif.setObjects(*((_A,_I),(_A,_H),(_A,_G),(_A,_B),(_A,_E),(_A,_D),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:tnAbsNodeRaisedNotif.setStatus(_J)
tnAbsNodeClearedNotif=NotificationType((1,3,6,1,4,1,7483,2,1,2,2,9,1,2))
tnAbsNodeClearedNotif.setObjects(*((_A,_I),(_A,_H),(_A,_G),(_A,_B),(_A,_E),(_A,_D),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:tnAbsNodeClearedNotif.setStatus(_J)
tnAbsNodeDegradedRaisedNotif=NotificationType((1,3,6,1,4,1,7483,2,1,2,2,9,1,3))
tnAbsNodeDegradedRaisedNotif.setObjects(*((_A,_I),(_A,_H),(_A,_G),(_A,_B),(_A,_E),(_A,_D),(_A,_K),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:tnAbsNodeDegradedRaisedNotif.setStatus(_J)
tnAbsNodeDegradedClearedNotif=NotificationType((1,3,6,1,4,1,7483,2,1,2,2,9,1,4))
tnAbsNodeDegradedClearedNotif.setObjects(*((_A,_I),(_A,_H),(_A,_G),(_A,_B),(_A,_E),(_A,_D),(_A,_K),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:tnAbsNodeDegradedClearedNotif.setStatus(_J)
tnAbsNodeFailedRaisedNotif=NotificationType((1,3,6,1,4,1,7483,2,1,2,2,9,1,5))
tnAbsNodeFailedRaisedNotif.setObjects(*((_A,_I),(_A,_H),(_A,_G),(_A,_B),(_A,_E),(_A,_D),(_A,_K),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:tnAbsNodeFailedRaisedNotif.setStatus(_J)
tnAbsNodeFailedClearedNotif=NotificationType((1,3,6,1,4,1,7483,2,1,2,2,9,1,6))
tnAbsNodeFailedClearedNotif.setObjects(*((_A,_I),(_A,_H),(_A,_G),(_A,_B),(_A,_E),(_A,_D),(_A,_K),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:tnAbsNodeFailedClearedNotif.setStatus(_J)
mibBuilder.exportSymbols('TROPIC-ABSNODE-NOTIFICATION-MIB',**{'tnAbsNodeNotificationMIBModule':tnAbsNodeNotificationMIBModule,'tnNotificationsAbsNode':tnNotificationsAbsNode,'tnAlarmNotificationsAbsNode':tnAlarmNotificationsAbsNode,'tnAbsNodeRaisedNotif':tnAbsNodeRaisedNotif,'tnAbsNodeClearedNotif':tnAbsNodeClearedNotif,'tnAbsNodeDegradedRaisedNotif':tnAbsNodeDegradedRaisedNotif,'tnAbsNodeDegradedClearedNotif':tnAbsNodeDegradedClearedNotif,'tnAbsNodeFailedRaisedNotif':tnAbsNodeFailedRaisedNotif,'tnAbsNodeFailedClearedNotif':tnAbsNodeFailedClearedNotif,'tnEventNotificationsAbsNode':tnEventNotificationsAbsNode})