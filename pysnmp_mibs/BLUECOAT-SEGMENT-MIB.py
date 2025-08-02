_O='segmentMIBGroup'
_N='segmentStateTrap'
_M='segmentStatusIndex'
_L='Integer32'
_K='segmentStatusComment'
_J='segmentStatusState'
_I='segmentStatusCopyIfList'
_H='segmentStatusDownIfList'
_G='segmentStatusIfList'
_F='segmentStatusMode'
_E='segmentStatusIdentifier'
_D='PortList'
_C='read-only'
_B='current'
_A='BLUECOAT-SEGMENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
segmentMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,17))
if mibBuilder.loadTexts:segmentMIB.setRevisions(('2016-02-24 03:00','2015-01-13 03:00'))
class SegmentMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('invalid',0),('activeInlineFailToAppliance',1),('asymActiveInlineFailToAppliance',2),('activeInlineFailToNetwork',3),('asymActiveInlineFailToNetwork',4),('passiveInline',5),('asymPassiveInline',6),('passiveTap',7),('asymPassiveTap',8),('passiveTap2xAggrInputs',9),('passiveTap3xAggrInputs',10)))
class SegmentState(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('softwareFailure',0),('manualFailure',1),('linkFailure',2),('activationFailure',3)))
_SegmentMIBObjects_ObjectIdentity=ObjectIdentity
segmentMIBObjects=_SegmentMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,17,1))
_Segments_ObjectIdentity=ObjectIdentity
segments=_Segments_ObjectIdentity((1,3,6,1,4,1,3417,2,17,1,1))
_SegmentStatusTable_Object=MibTable
segmentStatusTable=_SegmentStatusTable_Object((1,3,6,1,4,1,3417,2,17,1,1,1))
if mibBuilder.loadTexts:segmentStatusTable.setStatus(_B)
_SegmentStatusEntry_Object=MibTableRow
segmentStatusEntry=_SegmentStatusEntry_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1))
segmentStatusEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:segmentStatusEntry.setStatus(_B)
class _SegmentStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SegmentStatusIndex_Type.__name__=_L
_SegmentStatusIndex_Object=MibTableColumn
segmentStatusIndex=_SegmentStatusIndex_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,1),_SegmentStatusIndex_Type())
segmentStatusIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:segmentStatusIndex.setStatus(_B)
_SegmentStatusIdentifier_Type=DisplayString
_SegmentStatusIdentifier_Object=MibTableColumn
segmentStatusIdentifier=_SegmentStatusIdentifier_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,2),_SegmentStatusIdentifier_Type())
segmentStatusIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusIdentifier.setStatus(_B)
_SegmentStatusMode_Type=SegmentMode
_SegmentStatusMode_Object=MibTableColumn
segmentStatusMode=_SegmentStatusMode_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,3),_SegmentStatusMode_Type())
segmentStatusMode.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusMode.setStatus(_B)
class _SegmentStatusIfList_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SegmentStatusIfList_Type.__name__=_D
_SegmentStatusIfList_Object=MibTableColumn
segmentStatusIfList=_SegmentStatusIfList_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,4),_SegmentStatusIfList_Type())
segmentStatusIfList.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusIfList.setStatus(_B)
class _SegmentStatusDownIfList_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SegmentStatusDownIfList_Type.__name__=_D
_SegmentStatusDownIfList_Object=MibTableColumn
segmentStatusDownIfList=_SegmentStatusDownIfList_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,5),_SegmentStatusDownIfList_Type())
segmentStatusDownIfList.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusDownIfList.setStatus(_B)
class _SegmentStatusCopyIfList_Type(PortList):subtypeSpec=PortList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SegmentStatusCopyIfList_Type.__name__=_D
_SegmentStatusCopyIfList_Object=MibTableColumn
segmentStatusCopyIfList=_SegmentStatusCopyIfList_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,6),_SegmentStatusCopyIfList_Type())
segmentStatusCopyIfList.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusCopyIfList.setStatus(_B)
_SegmentStatusState_Type=SegmentState
_SegmentStatusState_Object=MibTableColumn
segmentStatusState=_SegmentStatusState_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,7),_SegmentStatusState_Type())
segmentStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusState.setStatus(_B)
_SegmentStatusComment_Type=DisplayString
_SegmentStatusComment_Object=MibTableColumn
segmentStatusComment=_SegmentStatusComment_Object((1,3,6,1,4,1,3417,2,17,1,1,1,1,8),_SegmentStatusComment_Type())
segmentStatusComment.setMaxAccess(_C)
if mibBuilder.loadTexts:segmentStatusComment.setStatus(_B)
_SegmentMIBNotifications_ObjectIdentity=ObjectIdentity
segmentMIBNotifications=_SegmentMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,17,2))
_SegmentMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
segmentMIBNotificationsPrefix=_SegmentMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,17,2,0))
_SegmentMIBConformance_ObjectIdentity=ObjectIdentity
segmentMIBConformance=_SegmentMIBConformance_ObjectIdentity((1,3,6,1,4,1,3417,2,17,3))
_SegmentMIBCompliances_ObjectIdentity=ObjectIdentity
segmentMIBCompliances=_SegmentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3417,2,17,3,1))
_SegmentMIBGroups_ObjectIdentity=ObjectIdentity
segmentMIBGroups=_SegmentMIBGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,17,3,2))
_SegmentMIBNotifGroups_ObjectIdentity=ObjectIdentity
segmentMIBNotifGroups=_SegmentMIBNotifGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,17,3,3))
segmentMIBGroup=ObjectGroup((1,3,6,1,4,1,3417,2,17,3,2,1))
segmentMIBGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:segmentMIBGroup.setStatus(_B)
segmentStateTrap=NotificationType((1,3,6,1,4,1,3417,2,17,2,0,1))
segmentStateTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:segmentStateTrap.setStatus(_B)
segmentMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,3417,2,17,3,3,1))
segmentMIBNotifGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:segmentMIBNotifGroup.setStatus(_B)
segmentMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3417,2,17,3,1,1))
segmentMIBCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:segmentMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SegmentMode':SegmentMode,'SegmentState':SegmentState,'segmentMIB':segmentMIB,'segmentMIBObjects':segmentMIBObjects,'segments':segments,'segmentStatusTable':segmentStatusTable,'segmentStatusEntry':segmentStatusEntry,_M:segmentStatusIndex,_E:segmentStatusIdentifier,_F:segmentStatusMode,_G:segmentStatusIfList,_H:segmentStatusDownIfList,_I:segmentStatusCopyIfList,_J:segmentStatusState,_K:segmentStatusComment,'segmentMIBNotifications':segmentMIBNotifications,'segmentMIBNotificationsPrefix':segmentMIBNotificationsPrefix,_N:segmentStateTrap,'segmentMIBConformance':segmentMIBConformance,'segmentMIBCompliances':segmentMIBCompliances,'segmentMIBCompliance':segmentMIBCompliance,'segmentMIBGroups':segmentMIBGroups,_O:segmentMIBGroup,'segmentMIBNotifGroups':segmentMIBNotifGroups,'segmentMIBNotifGroup':segmentMIBNotifGroup})