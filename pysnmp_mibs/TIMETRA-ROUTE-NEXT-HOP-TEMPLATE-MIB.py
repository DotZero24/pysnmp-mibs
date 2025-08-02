_c='tmnxRouteNextHopTemplateGroup'
_b='tmnxRouteNHTemplAdminGrpPref'
_a='tmnxRouteNHTemplAdmGrpRowLstCh'
_Z='tmnxRouteNHTemplAdmGrpRowStatus'
_Y='tmnxRouteNHTemplAdminGrpTblLstCh'
_X='tmnxRouteNHTemplateNextHopType'
_W='tmnxRouteNHTemplProtectionType'
_V='tmnxRouteNHTemplateSrlgEnable'
_U='tmnxRouteNHTemplateDescription'
_T='tmnxRouteNHTemplateRowLstChng'
_S='tmnxRouteNHTemplateRowStatus'
_R='tmnxRouteNHTemplateTblLastCh'
_Q='tmnxRouteNHAdminControlApply'
_P='tmnxRouteNHAdminOwner'
_O='tmnxRouteNHAdminLastChangeTime'
_N='tmnxRouteNHTemplAdminGrpName'
_M='tmnxRouteNHTemplAdminGrpType'
_L='read-write'
_K='TNamedItemOrEmpty'
_J='TItemDescription'
_I='TruthValue'
_H='tmnxRouteNHTemplateName'
_G='tmnxRouteNHTemplateVersion'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_I)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TNamedItem,TNamedItemOrEmpty=mibBuilder.importSymbols('TIMETRA-TC-MIB',_J,'TNamedItem',_K)
timetraRouteNextHopTemplateMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,90))
if mibBuilder.loadTexts:timetraRouteNextHopTemplateMIBModule.setRevisions(('2014-01-01 00:00',))
class TmnxRouteNHVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('admin',0),('oper',1)))
_TmnxRouteNHConformance_ObjectIdentity=ObjectIdentity
tmnxRouteNHConformance=_TmnxRouteNHConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,90))
_TmnxRouteNHCompliances_ObjectIdentity=ObjectIdentity
tmnxRouteNHCompliances=_TmnxRouteNHCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,90,1))
_TmnxRouteNHGroups_ObjectIdentity=ObjectIdentity
tmnxRouteNHGroups=_TmnxRouteNHGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,90,2))
_TmnxRouteNHNotifGroups_ObjectIdentity=ObjectIdentity
tmnxRouteNHNotifGroups=_TmnxRouteNHNotifGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,90,3))
_TmnxRouteNextHop_ObjectIdentity=ObjectIdentity
tmnxRouteNextHop=_TmnxRouteNextHop_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,90))
_TmnxRouteNextHopObjs_ObjectIdentity=ObjectIdentity
tmnxRouteNextHopObjs=_TmnxRouteNextHopObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,90,1))
_TmnxRouteNHAdminControl_ObjectIdentity=ObjectIdentity
tmnxRouteNHAdminControl=_TmnxRouteNHAdminControl_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,90,1,1))
_TmnxRouteNHAdminLastChangeTime_Type=TimeStamp
_TmnxRouteNHAdminLastChangeTime_Object=MibScalar
tmnxRouteNHAdminLastChangeTime=_TmnxRouteNHAdminLastChangeTime_Object((1,3,6,1,4,1,6527,3,1,2,90,1,1,1),_TmnxRouteNHAdminLastChangeTime_Type())
tmnxRouteNHAdminLastChangeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxRouteNHAdminLastChangeTime.setStatus(_A)
class _TmnxRouteNHAdminOwner_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TmnxRouteNHAdminOwner_Type.__name__=_K
_TmnxRouteNHAdminOwner_Object=MibScalar
tmnxRouteNHAdminOwner=_TmnxRouteNHAdminOwner_Object((1,3,6,1,4,1,6527,3,1,2,90,1,1,2),_TmnxRouteNHAdminOwner_Type())
tmnxRouteNHAdminOwner.setMaxAccess(_L)
if mibBuilder.loadTexts:tmnxRouteNHAdminOwner.setStatus(_A)
class _TmnxRouteNHAdminControlApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('initialize',2),('commit',3)))
_TmnxRouteNHAdminControlApply_Type.__name__=_D
_TmnxRouteNHAdminControlApply_Object=MibScalar
tmnxRouteNHAdminControlApply=_TmnxRouteNHAdminControlApply_Object((1,3,6,1,4,1,6527,3,1,2,90,1,1,3),_TmnxRouteNHAdminControlApply_Type())
tmnxRouteNHAdminControlApply.setMaxAccess(_L)
if mibBuilder.loadTexts:tmnxRouteNHAdminControlApply.setStatus(_A)
_TmnxRouteNHTemplateTblLastCh_Type=TimeStamp
_TmnxRouteNHTemplateTblLastCh_Object=MibScalar
tmnxRouteNHTemplateTblLastCh=_TmnxRouteNHTemplateTblLastCh_Object((1,3,6,1,4,1,6527,3,1,2,90,1,3),_TmnxRouteNHTemplateTblLastCh_Type())
tmnxRouteNHTemplateTblLastCh.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxRouteNHTemplateTblLastCh.setStatus(_A)
_TmnxRouteNHTemplateTable_Object=MibTable
tmnxRouteNHTemplateTable=_TmnxRouteNHTemplateTable_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4))
if mibBuilder.loadTexts:tmnxRouteNHTemplateTable.setStatus(_A)
_TmnxRouteNHTemplateEntry_Object=MibTableRow
tmnxRouteNHTemplateEntry=_TmnxRouteNHTemplateEntry_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1))
tmnxRouteNHTemplateEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:tmnxRouteNHTemplateEntry.setStatus(_A)
_TmnxRouteNHTemplateVersion_Type=TmnxRouteNHVersion
_TmnxRouteNHTemplateVersion_Object=MibTableColumn
tmnxRouteNHTemplateVersion=_TmnxRouteNHTemplateVersion_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,1),_TmnxRouteNHTemplateVersion_Type())
tmnxRouteNHTemplateVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxRouteNHTemplateVersion.setStatus(_A)
_TmnxRouteNHTemplateName_Type=TNamedItem
_TmnxRouteNHTemplateName_Object=MibTableColumn
tmnxRouteNHTemplateName=_TmnxRouteNHTemplateName_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,2),_TmnxRouteNHTemplateName_Type())
tmnxRouteNHTemplateName.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxRouteNHTemplateName.setStatus(_A)
_TmnxRouteNHTemplateRowStatus_Type=RowStatus
_TmnxRouteNHTemplateRowStatus_Object=MibTableColumn
tmnxRouteNHTemplateRowStatus=_TmnxRouteNHTemplateRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,3),_TmnxRouteNHTemplateRowStatus_Type())
tmnxRouteNHTemplateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplateRowStatus.setStatus(_A)
_TmnxRouteNHTemplateRowLstChng_Type=TimeStamp
_TmnxRouteNHTemplateRowLstChng_Object=MibTableColumn
tmnxRouteNHTemplateRowLstChng=_TmnxRouteNHTemplateRowLstChng_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,4),_TmnxRouteNHTemplateRowLstChng_Type())
tmnxRouteNHTemplateRowLstChng.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxRouteNHTemplateRowLstChng.setStatus(_A)
class _TmnxRouteNHTemplateDescription_Type(TItemDescription):defaultValue=OctetString('')
_TmnxRouteNHTemplateDescription_Type.__name__=_J
_TmnxRouteNHTemplateDescription_Object=MibTableColumn
tmnxRouteNHTemplateDescription=_TmnxRouteNHTemplateDescription_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,5),_TmnxRouteNHTemplateDescription_Type())
tmnxRouteNHTemplateDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplateDescription.setStatus(_A)
class _TmnxRouteNHTemplateSrlgEnable_Type(TruthValue):defaultValue=2
_TmnxRouteNHTemplateSrlgEnable_Type.__name__=_I
_TmnxRouteNHTemplateSrlgEnable_Object=MibTableColumn
tmnxRouteNHTemplateSrlgEnable=_TmnxRouteNHTemplateSrlgEnable_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,6),_TmnxRouteNHTemplateSrlgEnable_Type())
tmnxRouteNHTemplateSrlgEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplateSrlgEnable.setStatus(_A)
class _TmnxRouteNHTemplProtectionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link',1),('node',2)))
_TmnxRouteNHTemplProtectionType_Type.__name__=_D
_TmnxRouteNHTemplProtectionType_Object=MibTableColumn
tmnxRouteNHTemplProtectionType=_TmnxRouteNHTemplProtectionType_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,7),_TmnxRouteNHTemplProtectionType_Type())
tmnxRouteNHTemplProtectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplProtectionType.setStatus(_A)
class _TmnxRouteNHTemplateNextHopType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('tunnel',2)))
_TmnxRouteNHTemplateNextHopType_Type.__name__=_D
_TmnxRouteNHTemplateNextHopType_Object=MibTableColumn
tmnxRouteNHTemplateNextHopType=_TmnxRouteNHTemplateNextHopType_Object((1,3,6,1,4,1,6527,3,1,2,90,1,4,1,8),_TmnxRouteNHTemplateNextHopType_Type())
tmnxRouteNHTemplateNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplateNextHopType.setStatus(_A)
_TmnxRouteNHTemplAdminGrpTblLstCh_Type=TimeStamp
_TmnxRouteNHTemplAdminGrpTblLstCh_Object=MibScalar
tmnxRouteNHTemplAdminGrpTblLstCh=_TmnxRouteNHTemplAdminGrpTblLstCh_Object((1,3,6,1,4,1,6527,3,1,2,90,1,5),_TmnxRouteNHTemplAdminGrpTblLstCh_Type())
tmnxRouteNHTemplAdminGrpTblLstCh.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxRouteNHTemplAdminGrpTblLstCh.setStatus(_A)
_TmnxRouteNHTemplAdminGrpTable_Object=MibTable
tmnxRouteNHTemplAdminGrpTable=_TmnxRouteNHTemplAdminGrpTable_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6))
if mibBuilder.loadTexts:tmnxRouteNHTemplAdminGrpTable.setStatus(_A)
_TmnxRouteNHTemplAdminGrpEntry_Object=MibTableRow
tmnxRouteNHTemplAdminGrpEntry=_TmnxRouteNHTemplAdminGrpEntry_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6,1))
tmnxRouteNHTemplAdminGrpEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:tmnxRouteNHTemplAdminGrpEntry.setStatus(_A)
class _TmnxRouteNHTemplAdminGrpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_TmnxRouteNHTemplAdminGrpType_Type.__name__=_D
_TmnxRouteNHTemplAdminGrpType_Object=MibTableColumn
tmnxRouteNHTemplAdminGrpType=_TmnxRouteNHTemplAdminGrpType_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6,1,1),_TmnxRouteNHTemplAdminGrpType_Type())
tmnxRouteNHTemplAdminGrpType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxRouteNHTemplAdminGrpType.setStatus(_A)
_TmnxRouteNHTemplAdminGrpName_Type=TNamedItem
_TmnxRouteNHTemplAdminGrpName_Object=MibTableColumn
tmnxRouteNHTemplAdminGrpName=_TmnxRouteNHTemplAdminGrpName_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6,1,2),_TmnxRouteNHTemplAdminGrpName_Type())
tmnxRouteNHTemplAdminGrpName.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxRouteNHTemplAdminGrpName.setStatus(_A)
_TmnxRouteNHTemplAdmGrpRowStatus_Type=RowStatus
_TmnxRouteNHTemplAdmGrpRowStatus_Object=MibTableColumn
tmnxRouteNHTemplAdmGrpRowStatus=_TmnxRouteNHTemplAdmGrpRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6,1,3),_TmnxRouteNHTemplAdmGrpRowStatus_Type())
tmnxRouteNHTemplAdmGrpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplAdmGrpRowStatus.setStatus(_A)
_TmnxRouteNHTemplAdmGrpRowLstCh_Type=TimeStamp
_TmnxRouteNHTemplAdmGrpRowLstCh_Object=MibTableColumn
tmnxRouteNHTemplAdmGrpRowLstCh=_TmnxRouteNHTemplAdmGrpRowLstCh_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6,1,4),_TmnxRouteNHTemplAdmGrpRowLstCh_Type())
tmnxRouteNHTemplAdmGrpRowLstCh.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxRouteNHTemplAdmGrpRowLstCh.setStatus(_A)
class _TmnxRouteNHTemplAdminGrpPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TmnxRouteNHTemplAdminGrpPref_Type.__name__=_D
_TmnxRouteNHTemplAdminGrpPref_Object=MibTableColumn
tmnxRouteNHTemplAdminGrpPref=_TmnxRouteNHTemplAdminGrpPref_Object((1,3,6,1,4,1,6527,3,1,2,90,1,6,1,5),_TmnxRouteNHTemplAdminGrpPref_Type())
tmnxRouteNHTemplAdminGrpPref.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxRouteNHTemplAdminGrpPref.setStatus(_A)
_TmnxRouteNHNotificationObjs_ObjectIdentity=ObjectIdentity
tmnxRouteNHNotificationObjs=_TmnxRouteNHNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,90,2))
_TmnxRouteNHNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxRouteNHNotifyPrefix=_TmnxRouteNHNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,90))
_TmnxRouteNHNotifications_ObjectIdentity=ObjectIdentity
tmnxRouteNHNotifications=_TmnxRouteNHNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,90,0))
tmnxRouteNextHopTemplateGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,90,2,1))
tmnxRouteNextHopTemplateGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:tmnxRouteNextHopTemplateGroup.setStatus(_A)
tmnxRouteNextHopCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,90,1,1))
tmnxRouteNextHopCompliance.setObjects((_B,_c))
if mibBuilder.loadTexts:tmnxRouteNextHopCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TmnxRouteNHVersion':TmnxRouteNHVersion,'timetraRouteNextHopTemplateMIBModule':timetraRouteNextHopTemplateMIBModule,'tmnxRouteNHConformance':tmnxRouteNHConformance,'tmnxRouteNHCompliances':tmnxRouteNHCompliances,'tmnxRouteNextHopCompliance':tmnxRouteNextHopCompliance,'tmnxRouteNHGroups':tmnxRouteNHGroups,_c:tmnxRouteNextHopTemplateGroup,'tmnxRouteNHNotifGroups':tmnxRouteNHNotifGroups,'tmnxRouteNextHop':tmnxRouteNextHop,'tmnxRouteNextHopObjs':tmnxRouteNextHopObjs,'tmnxRouteNHAdminControl':tmnxRouteNHAdminControl,_O:tmnxRouteNHAdminLastChangeTime,_P:tmnxRouteNHAdminOwner,_Q:tmnxRouteNHAdminControlApply,_R:tmnxRouteNHTemplateTblLastCh,'tmnxRouteNHTemplateTable':tmnxRouteNHTemplateTable,'tmnxRouteNHTemplateEntry':tmnxRouteNHTemplateEntry,_G:tmnxRouteNHTemplateVersion,_H:tmnxRouteNHTemplateName,_S:tmnxRouteNHTemplateRowStatus,_T:tmnxRouteNHTemplateRowLstChng,_U:tmnxRouteNHTemplateDescription,_V:tmnxRouteNHTemplateSrlgEnable,_W:tmnxRouteNHTemplProtectionType,_X:tmnxRouteNHTemplateNextHopType,_Y:tmnxRouteNHTemplAdminGrpTblLstCh,'tmnxRouteNHTemplAdminGrpTable':tmnxRouteNHTemplAdminGrpTable,'tmnxRouteNHTemplAdminGrpEntry':tmnxRouteNHTemplAdminGrpEntry,_M:tmnxRouteNHTemplAdminGrpType,_N:tmnxRouteNHTemplAdminGrpName,_Z:tmnxRouteNHTemplAdmGrpRowStatus,_a:tmnxRouteNHTemplAdmGrpRowLstCh,_b:tmnxRouteNHTemplAdminGrpPref,'tmnxRouteNHNotificationObjs':tmnxRouteNHNotificationObjs,'tmnxRouteNHNotifyPrefix':tmnxRouteNHNotifyPrefix,'tmnxRouteNHNotifications':tmnxRouteNHNotifications})