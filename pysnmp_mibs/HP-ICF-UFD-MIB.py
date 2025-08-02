_d='hpicfUfdConfigGroup2'
_c='hpicfUfdLtDAutoEnabled'
_b='hpicfUfdLtDAutoDisabled'
_a='hpicfUfdLinksTransitionDelay'
_Z='hpicfUfdLinkRole'
_Y='hpicfUfdAdminStatus'
_X='hpicfUfdIfIndex'
_W='not-accessible'
_V='hpicfUfdConfigGroup1'
_U='hpicfUfdConfigGroup'
_T='deprecated'
_S='hpicfUfdLinksToTransitionType'
_R='hpicfUfdLinksToMonitorType'
_Q='hpicfUfdTrackEntityRowStatus'
_P='hpicfUfdTrackEntityState'
_O='hpicfUfdLinksToTransitionState'
_N='hpicfUfdLinksToMonitorState'
_M='hpicfUfdLinksToMonitor'
_L='hpicfUfdTrackEntityType'
_K='hpicfUfdTrackId'
_J='OctetString'
_I='hpicfUfdNotificationGroup'
_H='hpicfUfdBaseGroup'
_G='hpicfUfdNotifyTrackId'
_F='read-only'
_E='hpicfUfdLinksToTransition'
_D='read-write'
_C='Integer32'
_B='current'
_A='HP-ICF-UFD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpicfUfdMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74))
if mibBuilder.loadTexts:hpicfUfdMIB.setRevisions(('2018-05-23 00:00','2012-04-30 00:00','2011-05-12 00:00','2010-02-06 15:39'))
class HpUfdTrackEntityType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ufd',1))
class HpUfdTrackLinksSubtype(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('portMap',1),('lacpKey',2)))
_HpicfUfdNotifications_ObjectIdentity=ObjectIdentity
hpicfUfdNotifications=_HpicfUfdNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,0))
_HpicfUfdNotificationPrefix_ObjectIdentity=ObjectIdentity
hpicfUfdNotificationPrefix=_HpicfUfdNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,0,0))
_HpicfUfdConfigObjects_ObjectIdentity=ObjectIdentity
hpicfUfdConfigObjects=_HpicfUfdConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,1))
_HpicfUfdScalars_ObjectIdentity=ObjectIdentity
hpicfUfdScalars=_HpicfUfdScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,1,1))
class _HpicfUfdAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfUfdAdminStatus_Type.__name__=_C
_HpicfUfdAdminStatus_Object=MibScalar
hpicfUfdAdminStatus=_HpicfUfdAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,1,1),_HpicfUfdAdminStatus_Type())
hpicfUfdAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdAdminStatus.setStatus(_B)
class _HpicfUfdNotifyTrackId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_HpicfUfdNotifyTrackId_Type.__name__=_C
_HpicfUfdNotifyTrackId_Object=MibScalar
hpicfUfdNotifyTrackId=_HpicfUfdNotifyTrackId_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,1,2),_HpicfUfdNotifyTrackId_Type())
hpicfUfdNotifyTrackId.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpicfUfdNotifyTrackId.setStatus(_B)
_HpicfUfdTrackEntities_ObjectIdentity=ObjectIdentity
hpicfUfdTrackEntities=_HpicfUfdTrackEntities_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2))
_HpicfUfdTrackTable_Object=MibTable
hpicfUfdTrackTable=_HpicfUfdTrackTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1))
if mibBuilder.loadTexts:hpicfUfdTrackTable.setStatus(_B)
_HpicfUfdTrackEntry_Object=MibTableRow
hpicfUfdTrackEntry=_HpicfUfdTrackEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1))
hpicfUfdTrackEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:hpicfUfdTrackEntry.setStatus(_B)
class _HpicfUfdTrackId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_HpicfUfdTrackId_Type.__name__=_C
_HpicfUfdTrackId_Object=MibTableColumn
hpicfUfdTrackId=_HpicfUfdTrackId_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,1),_HpicfUfdTrackId_Type())
hpicfUfdTrackId.setMaxAccess(_W)
if mibBuilder.loadTexts:hpicfUfdTrackId.setStatus(_B)
_HpicfUfdTrackEntityType_Type=HpUfdTrackEntityType
_HpicfUfdTrackEntityType_Object=MibTableColumn
hpicfUfdTrackEntityType=_HpicfUfdTrackEntityType_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,2),_HpicfUfdTrackEntityType_Type())
hpicfUfdTrackEntityType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdTrackEntityType.setStatus(_B)
class _HpicfUfdLinksToMonitor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_HpicfUfdLinksToMonitor_Type.__name__=_J
_HpicfUfdLinksToMonitor_Object=MibTableColumn
hpicfUfdLinksToMonitor=_HpicfUfdLinksToMonitor_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,3),_HpicfUfdLinksToMonitor_Type())
hpicfUfdLinksToMonitor.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdLinksToMonitor.setStatus(_B)
class _HpicfUfdLinksToTransition_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_HpicfUfdLinksToTransition_Type.__name__=_J
_HpicfUfdLinksToTransition_Object=MibTableColumn
hpicfUfdLinksToTransition=_HpicfUfdLinksToTransition_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,4),_HpicfUfdLinksToTransition_Type())
hpicfUfdLinksToTransition.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdLinksToTransition.setStatus(_B)
class _HpicfUfdLinksToMonitorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpicfUfdLinksToMonitorState_Type.__name__=_C
_HpicfUfdLinksToMonitorState_Object=MibTableColumn
hpicfUfdLinksToMonitorState=_HpicfUfdLinksToMonitorState_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,5),_HpicfUfdLinksToMonitorState_Type())
hpicfUfdLinksToMonitorState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfUfdLinksToMonitorState.setStatus(_B)
class _HpicfUfdLinksToTransitionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('autoDisabled',2)))
_HpicfUfdLinksToTransitionState_Type.__name__=_C
_HpicfUfdLinksToTransitionState_Object=MibTableColumn
hpicfUfdLinksToTransitionState=_HpicfUfdLinksToTransitionState_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,6),_HpicfUfdLinksToTransitionState_Type())
hpicfUfdLinksToTransitionState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfUfdLinksToTransitionState.setStatus(_B)
class _HpicfUfdTrackEntityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('ok',1),('failed',2)))
_HpicfUfdTrackEntityState_Type.__name__=_C
_HpicfUfdTrackEntityState_Object=MibTableColumn
hpicfUfdTrackEntityState=_HpicfUfdTrackEntityState_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,7),_HpicfUfdTrackEntityState_Type())
hpicfUfdTrackEntityState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfUfdTrackEntityState.setStatus(_B)
_HpicfUfdTrackEntityRowStatus_Type=RowStatus
_HpicfUfdTrackEntityRowStatus_Object=MibTableColumn
hpicfUfdTrackEntityRowStatus=_HpicfUfdTrackEntityRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,8),_HpicfUfdTrackEntityRowStatus_Type())
hpicfUfdTrackEntityRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpicfUfdTrackEntityRowStatus.setStatus(_B)
_HpicfUfdLinksToMonitorType_Type=HpUfdTrackLinksSubtype
_HpicfUfdLinksToMonitorType_Object=MibTableColumn
hpicfUfdLinksToMonitorType=_HpicfUfdLinksToMonitorType_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,9),_HpicfUfdLinksToMonitorType_Type())
hpicfUfdLinksToMonitorType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdLinksToMonitorType.setStatus(_B)
_HpicfUfdLinksToTransitionType_Type=HpUfdTrackLinksSubtype
_HpicfUfdLinksToTransitionType_Object=MibTableColumn
hpicfUfdLinksToTransitionType=_HpicfUfdLinksToTransitionType_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,10),_HpicfUfdLinksToTransitionType_Type())
hpicfUfdLinksToTransitionType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdLinksToTransitionType.setStatus(_B)
class _HpicfUfdLinksTransitionDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HpicfUfdLinksTransitionDelay_Type.__name__=_C
_HpicfUfdLinksTransitionDelay_Object=MibTableColumn
hpicfUfdLinksTransitionDelay=_HpicfUfdLinksTransitionDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,1,1,13),_HpicfUfdLinksTransitionDelay_Type())
hpicfUfdLinksTransitionDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfUfdLinksTransitionDelay.setStatus(_B)
_HpicfUfdTrackedLinkTable_Object=MibTable
hpicfUfdTrackedLinkTable=_HpicfUfdTrackedLinkTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,2))
if mibBuilder.loadTexts:hpicfUfdTrackedLinkTable.setStatus(_B)
_HpicfUfdTrackedLinkEntry_Object=MibTableRow
hpicfUfdTrackedLinkEntry=_HpicfUfdTrackedLinkEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,2,1))
hpicfUfdTrackedLinkEntry.setIndexNames((0,_A,_K),(0,_A,_X))
if mibBuilder.loadTexts:hpicfUfdTrackedLinkEntry.setStatus(_B)
_HpicfUfdIfIndex_Type=InterfaceIndex
_HpicfUfdIfIndex_Object=MibTableColumn
hpicfUfdIfIndex=_HpicfUfdIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,2,1,1),_HpicfUfdIfIndex_Type())
hpicfUfdIfIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:hpicfUfdIfIndex.setStatus(_B)
class _HpicfUfdLinkRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uplink',1),('downlink',2)))
_HpicfUfdLinkRole_Type.__name__=_C
_HpicfUfdLinkRole_Object=MibTableColumn
hpicfUfdLinkRole=_HpicfUfdLinkRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,74,1,2,2,1,2),_HpicfUfdLinkRole_Type())
hpicfUfdLinkRole.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfUfdLinkRole.setStatus(_B)
_HpicfUfdConformance_ObjectIdentity=ObjectIdentity
hpicfUfdConformance=_HpicfUfdConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,3))
_HpicfUfdCompliances_ObjectIdentity=ObjectIdentity
hpicfUfdCompliances=_HpicfUfdCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,3,1))
_HpicfUfdGroups_ObjectIdentity=ObjectIdentity
hpicfUfdGroups=_HpicfUfdGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,74,3,2))
hpicfUfdBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,74,3,2,1))
hpicfUfdBaseGroup.setObjects(*((_A,_Y),(_A,_G)))
if mibBuilder.loadTexts:hpicfUfdBaseGroup.setStatus(_B)
hpicfUfdConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,74,3,2,2))
hpicfUfdConfigGroup.setObjects(*((_A,_L),(_A,_M),(_A,_E),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:hpicfUfdConfigGroup.setStatus(_T)
hpicfUfdConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,74,3,2,4))
hpicfUfdConfigGroup1.setObjects((_A,_Z))
if mibBuilder.loadTexts:hpicfUfdConfigGroup1.setStatus(_B)
hpicfUfdConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,74,3,2,5))
hpicfUfdConfigGroup2.setObjects(*((_A,_L),(_A,_M),(_A,_E),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_a)))
if mibBuilder.loadTexts:hpicfUfdConfigGroup2.setStatus(_B)
hpicfUfdLtDAutoDisabled=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,74,0,0,3))
hpicfUfdLtDAutoDisabled.setObjects(*((_A,_G),(_A,_E)))
if mibBuilder.loadTexts:hpicfUfdLtDAutoDisabled.setStatus(_B)
hpicfUfdLtDAutoEnabled=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,74,0,0,4))
hpicfUfdLtDAutoEnabled.setObjects(*((_A,_G),(_A,_E)))
if mibBuilder.loadTexts:hpicfUfdLtDAutoEnabled.setStatus(_B)
hpicfUfdNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,74,3,2,3))
hpicfUfdNotificationGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hpicfUfdNotificationGroup.setStatus(_B)
hpicfUfdCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,74,3,1,1))
hpicfUfdCompliance.setObjects(*((_A,_H),(_A,_U),(_A,_I)))
if mibBuilder.loadTexts:hpicfUfdCompliance.setStatus(_T)
hpicfUfdCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,74,3,1,2))
hpicfUfdCompliance1.setObjects(*((_A,_H),(_A,_U),(_A,_I),(_A,_V)))
if mibBuilder.loadTexts:hpicfUfdCompliance1.setStatus(_T)
hpicfUfdCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,74,3,1,3))
hpicfUfdCompliance2.setObjects(*((_A,_H),(_A,_d),(_A,_I),(_A,_V)))
if mibBuilder.loadTexts:hpicfUfdCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpUfdTrackEntityType':HpUfdTrackEntityType,'HpUfdTrackLinksSubtype':HpUfdTrackLinksSubtype,'hpicfUfdMIB':hpicfUfdMIB,'hpicfUfdNotifications':hpicfUfdNotifications,'hpicfUfdNotificationPrefix':hpicfUfdNotificationPrefix,_b:hpicfUfdLtDAutoDisabled,_c:hpicfUfdLtDAutoEnabled,'hpicfUfdConfigObjects':hpicfUfdConfigObjects,'hpicfUfdScalars':hpicfUfdScalars,_Y:hpicfUfdAdminStatus,_G:hpicfUfdNotifyTrackId,'hpicfUfdTrackEntities':hpicfUfdTrackEntities,'hpicfUfdTrackTable':hpicfUfdTrackTable,'hpicfUfdTrackEntry':hpicfUfdTrackEntry,_K:hpicfUfdTrackId,_L:hpicfUfdTrackEntityType,_M:hpicfUfdLinksToMonitor,_E:hpicfUfdLinksToTransition,_N:hpicfUfdLinksToMonitorState,_O:hpicfUfdLinksToTransitionState,_P:hpicfUfdTrackEntityState,_Q:hpicfUfdTrackEntityRowStatus,_R:hpicfUfdLinksToMonitorType,_S:hpicfUfdLinksToTransitionType,_a:hpicfUfdLinksTransitionDelay,'hpicfUfdTrackedLinkTable':hpicfUfdTrackedLinkTable,'hpicfUfdTrackedLinkEntry':hpicfUfdTrackedLinkEntry,_X:hpicfUfdIfIndex,_Z:hpicfUfdLinkRole,'hpicfUfdConformance':hpicfUfdConformance,'hpicfUfdCompliances':hpicfUfdCompliances,'hpicfUfdCompliance':hpicfUfdCompliance,'hpicfUfdCompliance1':hpicfUfdCompliance1,'hpicfUfdCompliance2':hpicfUfdCompliance2,'hpicfUfdGroups':hpicfUfdGroups,_H:hpicfUfdBaseGroup,_U:hpicfUfdConfigGroup,_I:hpicfUfdNotificationGroup,_V:hpicfUfdConfigGroup1,_d:hpicfUfdConfigGroup2})