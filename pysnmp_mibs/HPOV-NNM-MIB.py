_H='openViewSeverity'
_G='openViewData'
_F='openViewSourceName'
_E='openViewSourceId'
_D='OctetString'
_C='HPOV-NNM-MIB'
_B='accessible-for-notify'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpOpenView=ModuleIdentity((1,3,6,1,4,1,11,2,17,1))
if mibBuilder.loadTexts:hpOpenView.setRevisions(('2005-09-28 00:00','1996-07-08 00:00'))
class OVTextString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_OpenView_ObjectIdentity=ObjectIdentity
openView=_OpenView_ObjectIdentity((1,3,6,1,4,1,11,2,17))
_HpOVNNMTraps_ObjectIdentity=ObjectIdentity
hpOVNNMTraps=_HpOVNNMTraps_ObjectIdentity((1,3,6,1,4,1,11,2,17,1,0))
_OpenViewTrapVars_ObjectIdentity=ObjectIdentity
openViewTrapVars=_OpenViewTrapVars_ObjectIdentity((1,3,6,1,4,1,11,2,17,2))
_OpenViewSourceId_Type=Integer32
_OpenViewSourceId_Object=MibScalar
openViewSourceId=_OpenViewSourceId_Object((1,3,6,1,4,1,11,2,17,2,1),_OpenViewSourceId_Type())
openViewSourceId.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewSourceId.setStatus(_A)
_OpenViewSourceName_Type=OVTextString
_OpenViewSourceName_Object=MibScalar
openViewSourceName=_OpenViewSourceName_Object((1,3,6,1,4,1,11,2,17,2,2),_OpenViewSourceName_Type())
openViewSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewSourceName.setStatus(_A)
_OpenViewObjectId_Type=DisplayString
_OpenViewObjectId_Object=MibScalar
openViewObjectId=_OpenViewObjectId_Object((1,3,6,1,4,1,11,2,17,2,3),_OpenViewObjectId_Type())
openViewObjectId.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewObjectId.setStatus(_A)
_OpenViewData_Type=OctetString
_OpenViewData_Object=MibScalar
openViewData=_OpenViewData_Object((1,3,6,1,4,1,11,2,17,2,4),_OpenViewData_Type())
openViewData.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewData.setStatus(_A)
_OpenViewSeverity_Type=OVTextString
_OpenViewSeverity_Object=MibScalar
openViewSeverity=_OpenViewSeverity_Object((1,3,6,1,4,1,11,2,17,2,5),_OpenViewSeverity_Type())
openViewSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewSeverity.setStatus(_A)
_OpenViewCategory_Type=OVTextString
_OpenViewCategory_Object=MibScalar
openViewCategory=_OpenViewCategory_Object((1,3,6,1,4,1,11,2,17,2,6),_OpenViewCategory_Type())
openViewCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewCategory.setStatus(_A)
_OpenViewFilter_Type=DisplayString
_OpenViewFilter_Object=MibScalar
openViewFilter=_OpenViewFilter_Object((1,3,6,1,4,1,11,2,17,2,7),_OpenViewFilter_Type())
openViewFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewFilter.setStatus(_A)
_OpenViewEntity_Type=OVTextString
_OpenViewEntity_Object=MibScalar
openViewEntity=_OpenViewEntity_Object((1,3,6,1,4,1,11,2,17,2,8),_OpenViewEntity_Type())
openViewEntity.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewEntity.setStatus(_A)
_OpenViewAddress_Type=DisplayString
_OpenViewAddress_Object=MibScalar
openViewAddress=_OpenViewAddress_Object((1,3,6,1,4,1,11,2,17,2,9),_OpenViewAddress_Type())
openViewAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewAddress.setStatus(_A)
_OpenViewPid_Type=DisplayString
_OpenViewPid_Object=MibScalar
openViewPid=_OpenViewPid_Object((1,3,6,1,4,1,11,2,17,2,10),_OpenViewPid_Type())
openViewPid.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewPid.setStatus(_A)
_OpenViewCmipManagedObjectClass_Type=DisplayString
_OpenViewCmipManagedObjectClass_Object=MibScalar
openViewCmipManagedObjectClass=_OpenViewCmipManagedObjectClass_Object((1,3,6,1,4,1,11,2,17,2,11),_OpenViewCmipManagedObjectClass_Type())
openViewCmipManagedObjectClass.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewCmipManagedObjectClass.setStatus(_A)
_OpenViewCmipEventTime_Type=DisplayString
_OpenViewCmipEventTime_Object=MibScalar
openViewCmipEventTime=_OpenViewCmipEventTime_Object((1,3,6,1,4,1,11,2,17,2,12),_OpenViewCmipEventTime_Type())
openViewCmipEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewCmipEventTime.setStatus(_A)
_OpenViewCmipEventType_Type=DisplayString
_OpenViewCmipEventType_Object=MibScalar
openViewCmipEventType=_OpenViewCmipEventType_Object((1,3,6,1,4,1,11,2,17,2,13),_OpenViewCmipEventType_Type())
openViewCmipEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewCmipEventType.setStatus(_A)
_OpenViewCmipEventInfo_Type=DisplayString
_OpenViewCmipEventInfo_Object=MibScalar
openViewCmipEventInfo=_OpenViewCmipEventInfo_Object((1,3,6,1,4,1,11,2,17,2,14),_OpenViewCmipEventInfo_Type())
openViewCmipEventInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewCmipEventInfo.setStatus(_A)
_OpenViewCmipManagedObjectInstanceId_Type=DisplayString
_OpenViewCmipManagedObjectInstanceId_Object=MibScalar
openViewCmipManagedObjectInstanceId=_OpenViewCmipManagedObjectInstanceId_Object((1,3,6,1,4,1,11,2,17,2,15),_OpenViewCmipManagedObjectInstanceId_Type())
openViewCmipManagedObjectInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewCmipManagedObjectInstanceId.setStatus(_A)
class _OpenViewEventUUID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_OpenViewEventUUID_Type.__name__=_D
_OpenViewEventUUID_Object=MibScalar
openViewEventUUID=_OpenViewEventUUID_Object((1,3,6,1,4,1,11,2,17,2,16),_OpenViewEventUUID_Type())
openViewEventUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewEventUUID.setStatus(_A)
_OpenViewEcsCorrelateEvUUID_Type=DisplayString
_OpenViewEcsCorrelateEvUUID_Object=MibScalar
openViewEcsCorrelateEvUUID=_OpenViewEcsCorrelateEvUUID_Object((1,3,6,1,4,1,11,2,17,2,17),_OpenViewEcsCorrelateEvUUID_Type())
openViewEcsCorrelateEvUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewEcsCorrelateEvUUID.setStatus(_A)
_OpenViewEcsNodeImportance_Type=DisplayString
_OpenViewEcsNodeImportance_Object=MibScalar
openViewEcsNodeImportance=_OpenViewEcsNodeImportance_Object((1,3,6,1,4,1,11,2,17,2,18),_OpenViewEcsNodeImportance_Type())
openViewEcsNodeImportance.setMaxAccess(_B)
if mibBuilder.loadTexts:openViewEcsNodeImportance.setStatus(_A)
hpOVMessageTrap=NotificationType((1,3,6,1,4,1,11,2,17,1,0,58916872))
hpOVMessageTrap.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:hpOVMessageTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'OVTextString':OVTextString,'hp':hp,'nm':nm,'openView':openView,'hpOpenView':hpOpenView,'hpOVNNMTraps':hpOVNNMTraps,'hpOVMessageTrap':hpOVMessageTrap,'openViewTrapVars':openViewTrapVars,_E:openViewSourceId,_F:openViewSourceName,'openViewObjectId':openViewObjectId,_G:openViewData,_H:openViewSeverity,'openViewCategory':openViewCategory,'openViewFilter':openViewFilter,'openViewEntity':openViewEntity,'openViewAddress':openViewAddress,'openViewPid':openViewPid,'openViewCmipManagedObjectClass':openViewCmipManagedObjectClass,'openViewCmipEventTime':openViewCmipEventTime,'openViewCmipEventType':openViewCmipEventType,'openViewCmipEventInfo':openViewCmipEventInfo,'openViewCmipManagedObjectInstanceId':openViewCmipManagedObjectInstanceId,'openViewEventUUID':openViewEventUUID,'openViewEcsCorrelateEvUUID':openViewEcsCorrelateEvUUID,'openViewEcsNodeImportance':openViewEcsNodeImportance})