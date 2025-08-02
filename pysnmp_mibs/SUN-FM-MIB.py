_i='sunFmProblemTrap'
_h='sunFmResourceDiagnosisUUID'
_g='sunFmResourceStatus'
_f='sunFmResourceFMRI'
_e='sunFmResourceCount'
_d='sunFmModuleDescription'
_c='sunFmModuleStatus'
_b='sunFmModuleVersion'
_a='sunFmModuleName'
_Z='sunFmFaultEventLocation'
_Y='sunFmFaultEventStatus'
_X='sunFmFaultEventResource'
_W='sunFmFaultEventFRU'
_V='sunFmFaultEventASRU'
_U='sunFmFaultEventCertainty'
_T='sunFmFaultEventClass'
_S='sunFmFaultEventProblemUUID'
_R='sunFmProblemSuspectCount'
_Q='sunFmProblemDiagTime'
_P='sunFmProblemDiagEngine'
_O='sunFmResourceIndex'
_N='sunFmModuleIndex'
_M='sunFmFaultEventIndex'
_L='sunFmFaultEventUUIDIndex'
_K='sunFmProblemUUIDIndex'
_J='Gauge32'
_I='sunFmProblemURL'
_H='sunFmProblemCode'
_G='sunFmProblemUUID'
_F='other'
_E='DisplayString'
_D='not-accessible'
_C='read-only'
_B='SUN-FM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
URLString,=mibBuilder.importSymbols('NETWORK-SERVICES-MIB','URLString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_J,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','TextualConvention')
products,=mibBuilder.importSymbols('SUN-MIB','products')
sunFmMIB=ModuleIdentity((1,3,6,1,4,1,42,2,195,1))
if mibBuilder.loadTexts:sunFmMIB.setRevisions(('2008-08-04 00:00',))
class SunFmUuidString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class SunFmModuleState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('active',2),('failed',3)))
class SunFmResourceState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('ok',2),('degraded',3),('unknown',4),('faulted',5)))
class SunFmEventState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('faulty',2),('removed',3),('replaced',4),('repaired',5),('acquitted',6)))
_Fm_ObjectIdentity=ObjectIdentity
fm=_Fm_ObjectIdentity((1,3,6,1,4,1,42,2,195))
_SunFmProblemTable_Object=MibTable
sunFmProblemTable=_SunFmProblemTable_Object((1,3,6,1,4,1,42,2,195,1,1))
if mibBuilder.loadTexts:sunFmProblemTable.setStatus(_A)
_SunFmProblemEntry_Object=MibTableRow
sunFmProblemEntry=_SunFmProblemEntry_Object((1,3,6,1,4,1,42,2,195,1,1,1))
sunFmProblemEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:sunFmProblemEntry.setStatus(_A)
_SunFmProblemUUIDIndex_Type=SunFmUuidString
_SunFmProblemUUIDIndex_Object=MibTableColumn
sunFmProblemUUIDIndex=_SunFmProblemUUIDIndex_Object((1,3,6,1,4,1,42,2,195,1,1,1,1),_SunFmProblemUUIDIndex_Type())
sunFmProblemUUIDIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sunFmProblemUUIDIndex.setStatus(_A)
_SunFmProblemUUID_Type=SunFmUuidString
_SunFmProblemUUID_Object=MibTableColumn
sunFmProblemUUID=_SunFmProblemUUID_Object((1,3,6,1,4,1,42,2,195,1,1,1,2),_SunFmProblemUUID_Type())
sunFmProblemUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmProblemUUID.setStatus(_A)
_SunFmProblemCode_Type=DisplayString
_SunFmProblemCode_Object=MibTableColumn
sunFmProblemCode=_SunFmProblemCode_Object((1,3,6,1,4,1,42,2,195,1,1,1,3),_SunFmProblemCode_Type())
sunFmProblemCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmProblemCode.setStatus(_A)
_SunFmProblemURL_Type=URLString
_SunFmProblemURL_Object=MibTableColumn
sunFmProblemURL=_SunFmProblemURL_Object((1,3,6,1,4,1,42,2,195,1,1,1,4),_SunFmProblemURL_Type())
sunFmProblemURL.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmProblemURL.setStatus(_A)
_SunFmProblemDiagEngine_Type=URLString
_SunFmProblemDiagEngine_Object=MibTableColumn
sunFmProblemDiagEngine=_SunFmProblemDiagEngine_Object((1,3,6,1,4,1,42,2,195,1,1,1,5),_SunFmProblemDiagEngine_Type())
sunFmProblemDiagEngine.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmProblemDiagEngine.setStatus(_A)
_SunFmProblemDiagTime_Type=DateAndTime
_SunFmProblemDiagTime_Object=MibTableColumn
sunFmProblemDiagTime=_SunFmProblemDiagTime_Object((1,3,6,1,4,1,42,2,195,1,1,1,6),_SunFmProblemDiagTime_Type())
sunFmProblemDiagTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmProblemDiagTime.setStatus(_A)
_SunFmProblemSuspectCount_Type=Gauge32
_SunFmProblemSuspectCount_Object=MibTableColumn
sunFmProblemSuspectCount=_SunFmProblemSuspectCount_Object((1,3,6,1,4,1,42,2,195,1,1,1,7),_SunFmProblemSuspectCount_Type())
sunFmProblemSuspectCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmProblemSuspectCount.setStatus(_A)
_SunFmFaultEventTable_Object=MibTable
sunFmFaultEventTable=_SunFmFaultEventTable_Object((1,3,6,1,4,1,42,2,195,1,2))
if mibBuilder.loadTexts:sunFmFaultEventTable.setStatus(_A)
_SunFmFaultEventEntry_Object=MibTableRow
sunFmFaultEventEntry=_SunFmFaultEventEntry_Object((1,3,6,1,4,1,42,2,195,1,2,1))
sunFmFaultEventEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:sunFmFaultEventEntry.setStatus(_A)
_SunFmFaultEventUUIDIndex_Type=SunFmUuidString
_SunFmFaultEventUUIDIndex_Object=MibTableColumn
sunFmFaultEventUUIDIndex=_SunFmFaultEventUUIDIndex_Object((1,3,6,1,4,1,42,2,195,1,2,1,1),_SunFmFaultEventUUIDIndex_Type())
sunFmFaultEventUUIDIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sunFmFaultEventUUIDIndex.setStatus(_A)
_SunFmFaultEventIndex_Type=Unsigned32
_SunFmFaultEventIndex_Object=MibTableColumn
sunFmFaultEventIndex=_SunFmFaultEventIndex_Object((1,3,6,1,4,1,42,2,195,1,2,1,2),_SunFmFaultEventIndex_Type())
sunFmFaultEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sunFmFaultEventIndex.setStatus(_A)
_SunFmFaultEventProblemUUID_Type=SunFmUuidString
_SunFmFaultEventProblemUUID_Object=MibTableColumn
sunFmFaultEventProblemUUID=_SunFmFaultEventProblemUUID_Object((1,3,6,1,4,1,42,2,195,1,2,1,3),_SunFmFaultEventProblemUUID_Type())
sunFmFaultEventProblemUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventProblemUUID.setStatus(_A)
_SunFmFaultEventClass_Type=DisplayString
_SunFmFaultEventClass_Object=MibTableColumn
sunFmFaultEventClass=_SunFmFaultEventClass_Object((1,3,6,1,4,1,42,2,195,1,2,1,4),_SunFmFaultEventClass_Type())
sunFmFaultEventClass.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventClass.setStatus(_A)
class _SunFmFaultEventCertainty_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SunFmFaultEventCertainty_Type.__name__=_J
_SunFmFaultEventCertainty_Object=MibTableColumn
sunFmFaultEventCertainty=_SunFmFaultEventCertainty_Object((1,3,6,1,4,1,42,2,195,1,2,1,5),_SunFmFaultEventCertainty_Type())
sunFmFaultEventCertainty.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventCertainty.setStatus(_A)
_SunFmFaultEventASRU_Type=URLString
_SunFmFaultEventASRU_Object=MibTableColumn
sunFmFaultEventASRU=_SunFmFaultEventASRU_Object((1,3,6,1,4,1,42,2,195,1,2,1,6),_SunFmFaultEventASRU_Type())
sunFmFaultEventASRU.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventASRU.setStatus(_A)
_SunFmFaultEventFRU_Type=URLString
_SunFmFaultEventFRU_Object=MibTableColumn
sunFmFaultEventFRU=_SunFmFaultEventFRU_Object((1,3,6,1,4,1,42,2,195,1,2,1,7),_SunFmFaultEventFRU_Type())
sunFmFaultEventFRU.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventFRU.setStatus(_A)
_SunFmFaultEventResource_Type=URLString
_SunFmFaultEventResource_Object=MibTableColumn
sunFmFaultEventResource=_SunFmFaultEventResource_Object((1,3,6,1,4,1,42,2,195,1,2,1,8),_SunFmFaultEventResource_Type())
sunFmFaultEventResource.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventResource.setStatus(_A)
_SunFmFaultEventStatus_Type=SunFmEventState
_SunFmFaultEventStatus_Object=MibTableColumn
sunFmFaultEventStatus=_SunFmFaultEventStatus_Object((1,3,6,1,4,1,42,2,195,1,2,1,9),_SunFmFaultEventStatus_Type())
sunFmFaultEventStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventStatus.setStatus(_A)
_SunFmFaultEventLocation_Type=URLString
_SunFmFaultEventLocation_Object=MibTableColumn
sunFmFaultEventLocation=_SunFmFaultEventLocation_Object((1,3,6,1,4,1,42,2,195,1,2,1,10),_SunFmFaultEventLocation_Type())
sunFmFaultEventLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmFaultEventLocation.setStatus(_A)
_SunFmModuleTable_Object=MibTable
sunFmModuleTable=_SunFmModuleTable_Object((1,3,6,1,4,1,42,2,195,1,3))
if mibBuilder.loadTexts:sunFmModuleTable.setStatus(_A)
_SunFmModuleEntry_Object=MibTableRow
sunFmModuleEntry=_SunFmModuleEntry_Object((1,3,6,1,4,1,42,2,195,1,3,1))
sunFmModuleEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:sunFmModuleEntry.setStatus(_A)
_SunFmModuleIndex_Type=Unsigned32
_SunFmModuleIndex_Object=MibTableColumn
sunFmModuleIndex=_SunFmModuleIndex_Object((1,3,6,1,4,1,42,2,195,1,3,1,1),_SunFmModuleIndex_Type())
sunFmModuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sunFmModuleIndex.setStatus(_A)
class _SunFmModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SunFmModuleName_Type.__name__=_E
_SunFmModuleName_Object=MibTableColumn
sunFmModuleName=_SunFmModuleName_Object((1,3,6,1,4,1,42,2,195,1,3,1,2),_SunFmModuleName_Type())
sunFmModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmModuleName.setStatus(_A)
_SunFmModuleVersion_Type=DisplayString
_SunFmModuleVersion_Object=MibTableColumn
sunFmModuleVersion=_SunFmModuleVersion_Object((1,3,6,1,4,1,42,2,195,1,3,1,3),_SunFmModuleVersion_Type())
sunFmModuleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmModuleVersion.setStatus(_A)
_SunFmModuleStatus_Type=SunFmModuleState
_SunFmModuleStatus_Object=MibTableColumn
sunFmModuleStatus=_SunFmModuleStatus_Object((1,3,6,1,4,1,42,2,195,1,3,1,4),_SunFmModuleStatus_Type())
sunFmModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmModuleStatus.setStatus(_A)
_SunFmModuleDescription_Type=DisplayString
_SunFmModuleDescription_Object=MibTableColumn
sunFmModuleDescription=_SunFmModuleDescription_Object((1,3,6,1,4,1,42,2,195,1,3,1,5),_SunFmModuleDescription_Type())
sunFmModuleDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmModuleDescription.setStatus(_A)
_SunFmResourceCount_Type=Gauge32
_SunFmResourceCount_Object=MibScalar
sunFmResourceCount=_SunFmResourceCount_Object((1,3,6,1,4,1,42,2,195,1,4),_SunFmResourceCount_Type())
sunFmResourceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmResourceCount.setStatus(_A)
_SunFmResourceTable_Object=MibTable
sunFmResourceTable=_SunFmResourceTable_Object((1,3,6,1,4,1,42,2,195,1,5))
if mibBuilder.loadTexts:sunFmResourceTable.setStatus(_A)
_SunFmResourceEntry_Object=MibTableRow
sunFmResourceEntry=_SunFmResourceEntry_Object((1,3,6,1,4,1,42,2,195,1,5,1))
sunFmResourceEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:sunFmResourceEntry.setStatus(_A)
_SunFmResourceIndex_Type=Unsigned32
_SunFmResourceIndex_Object=MibTableColumn
sunFmResourceIndex=_SunFmResourceIndex_Object((1,3,6,1,4,1,42,2,195,1,5,1,1),_SunFmResourceIndex_Type())
sunFmResourceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sunFmResourceIndex.setStatus(_A)
class _SunFmResourceFMRI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SunFmResourceFMRI_Type.__name__=_E
_SunFmResourceFMRI_Object=MibTableColumn
sunFmResourceFMRI=_SunFmResourceFMRI_Object((1,3,6,1,4,1,42,2,195,1,5,1,2),_SunFmResourceFMRI_Type())
sunFmResourceFMRI.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmResourceFMRI.setStatus(_A)
_SunFmResourceStatus_Type=SunFmResourceState
_SunFmResourceStatus_Object=MibTableColumn
sunFmResourceStatus=_SunFmResourceStatus_Object((1,3,6,1,4,1,42,2,195,1,5,1,3),_SunFmResourceStatus_Type())
sunFmResourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmResourceStatus.setStatus(_A)
_SunFmResourceDiagnosisUUID_Type=SunFmUuidString
_SunFmResourceDiagnosisUUID_Object=MibTableColumn
sunFmResourceDiagnosisUUID=_SunFmResourceDiagnosisUUID_Object((1,3,6,1,4,1,42,2,195,1,5,1,4),_SunFmResourceDiagnosisUUID_Type())
sunFmResourceDiagnosisUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:sunFmResourceDiagnosisUUID.setStatus(_A)
_SunFmObjectGroups_ObjectIdentity=ObjectIdentity
sunFmObjectGroups=_SunFmObjectGroups_ObjectIdentity((1,3,6,1,4,1,42,2,195,1,6))
_SunFmTraps_ObjectIdentity=ObjectIdentity
sunFmTraps=_SunFmTraps_ObjectIdentity((1,3,6,1,4,1,42,2,195,1,7,0))
sunFmObjectGroup=ObjectGroup((1,3,6,1,4,1,42,2,195,1,6,1))
sunFmObjectGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:sunFmObjectGroup.setStatus(_A)
sunFmProblemTrap=NotificationType((1,3,6,1,4,1,42,2,195,1,7,0,1))
sunFmProblemTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:sunFmProblemTrap.setStatus(_A)
sunFmNotificationGroup=NotificationGroup((1,3,6,1,4,1,42,2,195,1,6,2))
sunFmNotificationGroup.setObjects((_B,_i))
if mibBuilder.loadTexts:sunFmNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SunFmUuidString':SunFmUuidString,'SunFmModuleState':SunFmModuleState,'SunFmResourceState':SunFmResourceState,'SunFmEventState':SunFmEventState,'fm':fm,'sunFmMIB':sunFmMIB,'sunFmProblemTable':sunFmProblemTable,'sunFmProblemEntry':sunFmProblemEntry,_K:sunFmProblemUUIDIndex,_G:sunFmProblemUUID,_H:sunFmProblemCode,_I:sunFmProblemURL,_P:sunFmProblemDiagEngine,_Q:sunFmProblemDiagTime,_R:sunFmProblemSuspectCount,'sunFmFaultEventTable':sunFmFaultEventTable,'sunFmFaultEventEntry':sunFmFaultEventEntry,_L:sunFmFaultEventUUIDIndex,_M:sunFmFaultEventIndex,_S:sunFmFaultEventProblemUUID,_T:sunFmFaultEventClass,_U:sunFmFaultEventCertainty,_V:sunFmFaultEventASRU,_W:sunFmFaultEventFRU,_X:sunFmFaultEventResource,_Y:sunFmFaultEventStatus,_Z:sunFmFaultEventLocation,'sunFmModuleTable':sunFmModuleTable,'sunFmModuleEntry':sunFmModuleEntry,_N:sunFmModuleIndex,_a:sunFmModuleName,_b:sunFmModuleVersion,_c:sunFmModuleStatus,_d:sunFmModuleDescription,_e:sunFmResourceCount,'sunFmResourceTable':sunFmResourceTable,'sunFmResourceEntry':sunFmResourceEntry,_O:sunFmResourceIndex,_f:sunFmResourceFMRI,_g:sunFmResourceStatus,_h:sunFmResourceDiagnosisUUID,'sunFmObjectGroups':sunFmObjectGroups,'sunFmObjectGroup':sunFmObjectGroup,'sunFmNotificationGroup':sunFmNotificationGroup,'sunFmTraps':sunFmTraps,_i:sunFmProblemTrap})