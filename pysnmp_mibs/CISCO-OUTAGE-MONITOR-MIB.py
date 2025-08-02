_y='ciscoLntMappingGroup'
_x='ciscoObjectOutageGroupRev'
_w='ciscoObjectOutageGroup'
_v='ciscoOutageEvent'
_u='cOutageLogicalObjDescrText'
_t='cOutageRecordingStartTime'
_s='cOutageRemoteObjDescrText'
_r='cOutageRemoteObjID'
_q='cOutageRemoteObjIDType'
_p='cOutageCpmProcessPID'
_o='cOutageCpmCPUTotalIndex'
_n='deprecated'
_m='cOutageEventTypeDescrText'
_l='cOutageEventTypeName'
_k='cOutageHistMsgsFlushed'
_j='cOutageHistTableSize'
_i='cOutageFilteredEvents'
_h='cOutageNotificationFilterEnabled'
_g='cOutageNotificationsEnabled'
_f='cOutageNotificationsSent'
_e='cOutageApplVersion'
_d='cOutageLogicalObjMapIndex'
_c='cOutageRemoteObjMapIndex'
_b='cOutageCpmMapIndex'
_a='cOutageMonitoredObjectIndex'
_Z='cOutageObjectType'
_Y='cOutageEventTypeMapIndex'
_X='cOutageEventIndex'
_W='Unsigned32'
_V='Integer32'
_U='SnmpAdminString'
_T='ciscoOutageNotificationsGroup'
_S='ciscoRmtMappingGroup'
_R='ciscoCpmMappingGroup'
_Q='ciscoEventDescrGroup'
_P='ciscoEventHistoryGroup'
_O='ciscoOutageBasicGroup'
_N='cOutageNAFSinceMeasureStarted'
_M='cOutageAOTSinceMeasureStarted'
_L='cOutageCurrentStatus'
_K='cOutageEventInterval'
_J='cOutageEventTime'
_I='cOutageEventTypeIndex'
_H='cOutageEventMonObjectIndex'
_G='cOutageEventObjectType'
_F='read-write'
_E='TruthValue'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-OUTAGE-MONITOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_V,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_E)
ciscoOutageMIB=ModuleIdentity((1,3,6,1,4,1,9,9,280))
if mibBuilder.loadTexts:ciscoOutageMIB.setRevisions(('2005-08-22 00:00','2002-09-09 00:00'))
class OutageMonObjectType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('interface',1),('physicalEntity',2),('swProcess',3),('remoteObject',4),('logicalEntity',5)))
_CiscoOutageMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOutageMIBObjects=_CiscoOutageMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,280,1))
_COutageBasicInfo_ObjectIdentity=ObjectIdentity
cOutageBasicInfo=_COutageBasicInfo_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,1))
_COutageApplVersion_Type=SnmpAdminString
_COutageApplVersion_Object=MibScalar
cOutageApplVersion=_COutageApplVersion_Object((1,3,6,1,4,1,9,9,280,1,1,1),_COutageApplVersion_Type())
cOutageApplVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageApplVersion.setStatus(_B)
_COutageNotificationsSent_Type=Counter32
_COutageNotificationsSent_Object=MibScalar
cOutageNotificationsSent=_COutageNotificationsSent_Object((1,3,6,1,4,1,9,9,280,1,1,2),_COutageNotificationsSent_Type())
cOutageNotificationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageNotificationsSent.setStatus(_B)
if mibBuilder.loadTexts:cOutageNotificationsSent.setUnits('notifications')
class _COutageNotificationsEnabled_Type(TruthValue):defaultValue=2
_COutageNotificationsEnabled_Type.__name__=_E
_COutageNotificationsEnabled_Object=MibScalar
cOutageNotificationsEnabled=_COutageNotificationsEnabled_Object((1,3,6,1,4,1,9,9,280,1,1,3),_COutageNotificationsEnabled_Type())
cOutageNotificationsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cOutageNotificationsEnabled.setStatus(_B)
class _COutageNotificationFilterEnabled_Type(TruthValue):defaultValue=2
_COutageNotificationFilterEnabled_Type.__name__=_E
_COutageNotificationFilterEnabled_Object=MibScalar
cOutageNotificationFilterEnabled=_COutageNotificationFilterEnabled_Object((1,3,6,1,4,1,9,9,280,1,1,4),_COutageNotificationFilterEnabled_Type())
cOutageNotificationFilterEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cOutageNotificationFilterEnabled.setStatus(_B)
_COutageFilteredEvents_Type=Counter32
_COutageFilteredEvents_Object=MibScalar
cOutageFilteredEvents=_COutageFilteredEvents_Object((1,3,6,1,4,1,9,9,280,1,1,5),_COutageFilteredEvents_Type())
cOutageFilteredEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageFilteredEvents.setStatus(_B)
_COutageHistory_ObjectIdentity=ObjectIdentity
cOutageHistory=_COutageHistory_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,2))
class _COutageHistTableSize_Type(Unsigned32):defaultValue=100
_COutageHistTableSize_Type.__name__=_W
_COutageHistTableSize_Object=MibScalar
cOutageHistTableSize=_COutageHistTableSize_Object((1,3,6,1,4,1,9,9,280,1,2,1),_COutageHistTableSize_Type())
cOutageHistTableSize.setMaxAccess(_F)
if mibBuilder.loadTexts:cOutageHistTableSize.setStatus(_B)
if mibBuilder.loadTexts:cOutageHistTableSize.setUnits('entries')
_COutageHistMsgsFlushed_Type=Counter32
_COutageHistMsgsFlushed_Object=MibScalar
cOutageHistMsgsFlushed=_COutageHistMsgsFlushed_Object((1,3,6,1,4,1,9,9,280,1,2,2),_COutageHistMsgsFlushed_Type())
cOutageHistMsgsFlushed.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageHistMsgsFlushed.setStatus(_B)
if mibBuilder.loadTexts:cOutageHistMsgsFlushed.setUnits('messages')
_COutageHistoryTable_Object=MibTable
cOutageHistoryTable=_COutageHistoryTable_Object((1,3,6,1,4,1,9,9,280,1,2,3))
if mibBuilder.loadTexts:cOutageHistoryTable.setStatus(_B)
_COutageHistoryEntry_Object=MibTableRow
cOutageHistoryEntry=_COutageHistoryEntry_Object((1,3,6,1,4,1,9,9,280,1,2,3,1))
cOutageHistoryEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:cOutageHistoryEntry.setStatus(_B)
_COutageEventIndex_Type=Unsigned32
_COutageEventIndex_Object=MibTableColumn
cOutageEventIndex=_COutageEventIndex_Object((1,3,6,1,4,1,9,9,280,1,2,3,1,1),_COutageEventIndex_Type())
cOutageEventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageEventIndex.setStatus(_B)
_COutageEventObjectType_Type=OutageMonObjectType
_COutageEventObjectType_Object=MibTableColumn
cOutageEventObjectType=_COutageEventObjectType_Object((1,3,6,1,4,1,9,9,280,1,2,3,1,2),_COutageEventObjectType_Type())
cOutageEventObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventObjectType.setStatus(_B)
_COutageEventMonObjectIndex_Type=Unsigned32
_COutageEventMonObjectIndex_Object=MibTableColumn
cOutageEventMonObjectIndex=_COutageEventMonObjectIndex_Object((1,3,6,1,4,1,9,9,280,1,2,3,1,3),_COutageEventMonObjectIndex_Type())
cOutageEventMonObjectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventMonObjectIndex.setStatus(_B)
_COutageEventTypeIndex_Type=Unsigned32
_COutageEventTypeIndex_Object=MibTableColumn
cOutageEventTypeIndex=_COutageEventTypeIndex_Object((1,3,6,1,4,1,9,9,280,1,2,3,1,4),_COutageEventTypeIndex_Type())
cOutageEventTypeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventTypeIndex.setStatus(_B)
_COutageEventTime_Type=DateAndTime
_COutageEventTime_Object=MibTableColumn
cOutageEventTime=_COutageEventTime_Object((1,3,6,1,4,1,9,9,280,1,2,3,1,5),_COutageEventTime_Type())
cOutageEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventTime.setStatus(_B)
_COutageEventInterval_Type=Unsigned32
_COutageEventInterval_Object=MibTableColumn
cOutageEventInterval=_COutageEventInterval_Object((1,3,6,1,4,1,9,9,280,1,2,3,1,6),_COutageEventInterval_Type())
cOutageEventInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventInterval.setStatus(_B)
_COutageDescription_ObjectIdentity=ObjectIdentity
cOutageDescription=_COutageDescription_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,3))
_COutageEventTypeMapTable_Object=MibTable
cOutageEventTypeMapTable=_COutageEventTypeMapTable_Object((1,3,6,1,4,1,9,9,280,1,3,1))
if mibBuilder.loadTexts:cOutageEventTypeMapTable.setStatus(_B)
_COutageEventTypeMapEntry_Object=MibTableRow
cOutageEventTypeMapEntry=_COutageEventTypeMapEntry_Object((1,3,6,1,4,1,9,9,280,1,3,1,1))
cOutageEventTypeMapEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:cOutageEventTypeMapEntry.setStatus(_B)
_COutageEventTypeMapIndex_Type=Unsigned32
_COutageEventTypeMapIndex_Object=MibTableColumn
cOutageEventTypeMapIndex=_COutageEventTypeMapIndex_Object((1,3,6,1,4,1,9,9,280,1,3,1,1,1),_COutageEventTypeMapIndex_Type())
cOutageEventTypeMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageEventTypeMapIndex.setStatus(_B)
class _COutageEventTypeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_COutageEventTypeName_Type.__name__=_U
_COutageEventTypeName_Object=MibTableColumn
cOutageEventTypeName=_COutageEventTypeName_Object((1,3,6,1,4,1,9,9,280,1,3,1,1,2),_COutageEventTypeName_Type())
cOutageEventTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventTypeName.setStatus(_B)
_COutageEventTypeDescrText_Type=SnmpAdminString
_COutageEventTypeDescrText_Object=MibTableColumn
cOutageEventTypeDescrText=_COutageEventTypeDescrText_Object((1,3,6,1,4,1,9,9,280,1,3,1,1,3),_COutageEventTypeDescrText_Type())
cOutageEventTypeDescrText.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageEventTypeDescrText.setStatus(_B)
_COutageMonObject_ObjectIdentity=ObjectIdentity
cOutageMonObject=_COutageMonObject_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,4))
_COutageObjectTable_Object=MibTable
cOutageObjectTable=_COutageObjectTable_Object((1,3,6,1,4,1,9,9,280,1,4,1))
if mibBuilder.loadTexts:cOutageObjectTable.setStatus(_B)
_COutageObjectEntry_Object=MibTableRow
cOutageObjectEntry=_COutageObjectEntry_Object((1,3,6,1,4,1,9,9,280,1,4,1,1))
cOutageObjectEntry.setIndexNames((0,_A,_Z),(0,_A,_a))
if mibBuilder.loadTexts:cOutageObjectEntry.setStatus(_B)
_COutageObjectType_Type=OutageMonObjectType
_COutageObjectType_Object=MibTableColumn
cOutageObjectType=_COutageObjectType_Object((1,3,6,1,4,1,9,9,280,1,4,1,1,1),_COutageObjectType_Type())
cOutageObjectType.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageObjectType.setStatus(_B)
_COutageMonitoredObjectIndex_Type=Unsigned32
_COutageMonitoredObjectIndex_Object=MibTableColumn
cOutageMonitoredObjectIndex=_COutageMonitoredObjectIndex_Object((1,3,6,1,4,1,9,9,280,1,4,1,1,2),_COutageMonitoredObjectIndex_Type())
cOutageMonitoredObjectIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageMonitoredObjectIndex.setStatus(_B)
class _COutageCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_COutageCurrentStatus_Type.__name__=_V
_COutageCurrentStatus_Object=MibTableColumn
cOutageCurrentStatus=_COutageCurrentStatus_Object((1,3,6,1,4,1,9,9,280,1,4,1,1,3),_COutageCurrentStatus_Type())
cOutageCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageCurrentStatus.setStatus(_B)
_COutageAOTSinceMeasureStarted_Type=Unsigned32
_COutageAOTSinceMeasureStarted_Object=MibTableColumn
cOutageAOTSinceMeasureStarted=_COutageAOTSinceMeasureStarted_Object((1,3,6,1,4,1,9,9,280,1,4,1,1,4),_COutageAOTSinceMeasureStarted_Type())
cOutageAOTSinceMeasureStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageAOTSinceMeasureStarted.setStatus(_B)
_COutageNAFSinceMeasureStarted_Type=Unsigned32
_COutageNAFSinceMeasureStarted_Object=MibTableColumn
cOutageNAFSinceMeasureStarted=_COutageNAFSinceMeasureStarted_Object((1,3,6,1,4,1,9,9,280,1,4,1,1,5),_COutageNAFSinceMeasureStarted_Type())
cOutageNAFSinceMeasureStarted.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageNAFSinceMeasureStarted.setStatus(_B)
_COutageRecordingStartTime_Type=DateAndTime
_COutageRecordingStartTime_Object=MibTableColumn
cOutageRecordingStartTime=_COutageRecordingStartTime_Object((1,3,6,1,4,1,9,9,280,1,4,1,1,6),_COutageRecordingStartTime_Type())
cOutageRecordingStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageRecordingStartTime.setStatus(_B)
_COutageCpmMapping_ObjectIdentity=ObjectIdentity
cOutageCpmMapping=_COutageCpmMapping_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,5))
_COutageCpmMapTable_Object=MibTable
cOutageCpmMapTable=_COutageCpmMapTable_Object((1,3,6,1,4,1,9,9,280,1,5,1))
if mibBuilder.loadTexts:cOutageCpmMapTable.setStatus(_B)
_COutageCpmMapEntry_Object=MibTableRow
cOutageCpmMapEntry=_COutageCpmMapEntry_Object((1,3,6,1,4,1,9,9,280,1,5,1,1))
cOutageCpmMapEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:cOutageCpmMapEntry.setStatus(_B)
_COutageCpmMapIndex_Type=Unsigned32
_COutageCpmMapIndex_Object=MibTableColumn
cOutageCpmMapIndex=_COutageCpmMapIndex_Object((1,3,6,1,4,1,9,9,280,1,5,1,1,1),_COutageCpmMapIndex_Type())
cOutageCpmMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageCpmMapIndex.setStatus(_B)
_COutageCpmCPUTotalIndex_Type=Unsigned32
_COutageCpmCPUTotalIndex_Object=MibTableColumn
cOutageCpmCPUTotalIndex=_COutageCpmCPUTotalIndex_Object((1,3,6,1,4,1,9,9,280,1,5,1,1,2),_COutageCpmCPUTotalIndex_Type())
cOutageCpmCPUTotalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageCpmCPUTotalIndex.setStatus(_B)
_COutageCpmProcessPID_Type=Unsigned32
_COutageCpmProcessPID_Object=MibTableColumn
cOutageCpmProcessPID=_COutageCpmProcessPID_Object((1,3,6,1,4,1,9,9,280,1,5,1,1,3),_COutageCpmProcessPID_Type())
cOutageCpmProcessPID.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageCpmProcessPID.setStatus(_B)
_COutageRmtMapping_ObjectIdentity=ObjectIdentity
cOutageRmtMapping=_COutageRmtMapping_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,6))
_COutageRemoteObjMapTable_Object=MibTable
cOutageRemoteObjMapTable=_COutageRemoteObjMapTable_Object((1,3,6,1,4,1,9,9,280,1,6,1))
if mibBuilder.loadTexts:cOutageRemoteObjMapTable.setStatus(_B)
_COutageRemoteObjMapEntry_Object=MibTableRow
cOutageRemoteObjMapEntry=_COutageRemoteObjMapEntry_Object((1,3,6,1,4,1,9,9,280,1,6,1,1))
cOutageRemoteObjMapEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:cOutageRemoteObjMapEntry.setStatus(_B)
_COutageRemoteObjMapIndex_Type=Unsigned32
_COutageRemoteObjMapIndex_Object=MibTableColumn
cOutageRemoteObjMapIndex=_COutageRemoteObjMapIndex_Object((1,3,6,1,4,1,9,9,280,1,6,1,1,1),_COutageRemoteObjMapIndex_Type())
cOutageRemoteObjMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageRemoteObjMapIndex.setStatus(_B)
_COutageRemoteObjIDType_Type=InetAddressType
_COutageRemoteObjIDType_Object=MibTableColumn
cOutageRemoteObjIDType=_COutageRemoteObjIDType_Object((1,3,6,1,4,1,9,9,280,1,6,1,1,2),_COutageRemoteObjIDType_Type())
cOutageRemoteObjIDType.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageRemoteObjIDType.setStatus(_B)
_COutageRemoteObjID_Type=InetAddress
_COutageRemoteObjID_Object=MibTableColumn
cOutageRemoteObjID=_COutageRemoteObjID_Object((1,3,6,1,4,1,9,9,280,1,6,1,1,3),_COutageRemoteObjID_Type())
cOutageRemoteObjID.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageRemoteObjID.setStatus(_B)
_COutageRemoteObjDescrText_Type=SnmpAdminString
_COutageRemoteObjDescrText_Object=MibTableColumn
cOutageRemoteObjDescrText=_COutageRemoteObjDescrText_Object((1,3,6,1,4,1,9,9,280,1,6,1,1,4),_COutageRemoteObjDescrText_Type())
cOutageRemoteObjDescrText.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageRemoteObjDescrText.setStatus(_B)
_COutageLntMapping_ObjectIdentity=ObjectIdentity
cOutageLntMapping=_COutageLntMapping_ObjectIdentity((1,3,6,1,4,1,9,9,280,1,7))
_COutageLogicalObjMapTable_Object=MibTable
cOutageLogicalObjMapTable=_COutageLogicalObjMapTable_Object((1,3,6,1,4,1,9,9,280,1,7,1))
if mibBuilder.loadTexts:cOutageLogicalObjMapTable.setStatus(_B)
_COutageLogicalObjMapEntry_Object=MibTableRow
cOutageLogicalObjMapEntry=_COutageLogicalObjMapEntry_Object((1,3,6,1,4,1,9,9,280,1,7,1,1))
cOutageLogicalObjMapEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:cOutageLogicalObjMapEntry.setStatus(_B)
_COutageLogicalObjMapIndex_Type=Unsigned32
_COutageLogicalObjMapIndex_Object=MibTableColumn
cOutageLogicalObjMapIndex=_COutageLogicalObjMapIndex_Object((1,3,6,1,4,1,9,9,280,1,7,1,1,1),_COutageLogicalObjMapIndex_Type())
cOutageLogicalObjMapIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cOutageLogicalObjMapIndex.setStatus(_B)
_COutageLogicalObjDescrText_Type=SnmpAdminString
_COutageLogicalObjDescrText_Object=MibTableColumn
cOutageLogicalObjDescrText=_COutageLogicalObjDescrText_Object((1,3,6,1,4,1,9,9,280,1,7,1,1,2),_COutageLogicalObjDescrText_Type())
cOutageLogicalObjDescrText.setMaxAccess(_C)
if mibBuilder.loadTexts:cOutageLogicalObjDescrText.setStatus(_B)
_CiscoOutageMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoOutageMIBNotificationPrefix=_CiscoOutageMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,280,2))
_CiscoOutageMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoOutageMIBNotifications=_CiscoOutageMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,280,2,0))
_CiscoOutageMIBConformance_ObjectIdentity=ObjectIdentity
ciscoOutageMIBConformance=_CiscoOutageMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,280,3))
_CiscoOutageMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOutageMIBCompliances=_CiscoOutageMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,280,3,1))
_CiscoOutageMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOutageMIBGroups=_CiscoOutageMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,280,3,2))
ciscoOutageBasicGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,1))
ciscoOutageBasicGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoOutageBasicGroup.setStatus(_B)
ciscoEventHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,2))
ciscoEventHistoryGroup.setObjects(*((_A,_j),(_A,_k),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoEventHistoryGroup.setStatus(_B)
ciscoEventDescrGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,3))
ciscoEventDescrGroup.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ciscoEventDescrGroup.setStatus(_B)
ciscoObjectOutageGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,4))
ciscoObjectOutageGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoObjectOutageGroup.setStatus(_n)
ciscoCpmMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,5))
ciscoCpmMappingGroup.setObjects(*((_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ciscoCpmMappingGroup.setStatus(_B)
ciscoRmtMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,6))
ciscoRmtMappingGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoRmtMappingGroup.setStatus(_B)
ciscoObjectOutageGroupRev=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,8))
ciscoObjectOutageGroupRev.setObjects(*((_A,_L),(_A,_t),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:ciscoObjectOutageGroupRev.setStatus(_B)
ciscoLntMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,280,3,2,9))
ciscoLntMappingGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:ciscoLntMappingGroup.setStatus(_B)
ciscoOutageEvent=NotificationType((1,3,6,1,4,1,9,9,280,2,0,1))
ciscoOutageEvent.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoOutageEvent.setStatus(_B)
ciscoOutageNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,280,3,2,7))
ciscoOutageNotificationsGroup.setObjects((_A,_v))
if mibBuilder.loadTexts:ciscoOutageNotificationsGroup.setStatus(_B)
ciscoOutageMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,280,3,1,1))
ciscoOutageMIBCompliance.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_w),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoOutageMIBCompliance.setStatus(_n)
ciscoOutageMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,280,3,1,2))
ciscoOutageMIBComplianceRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_x),(_A,_R),(_A,_S),(_A,_y),(_A,_T)))
if mibBuilder.loadTexts:ciscoOutageMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'OutageMonObjectType':OutageMonObjectType,'ciscoOutageMIB':ciscoOutageMIB,'ciscoOutageMIBObjects':ciscoOutageMIBObjects,'cOutageBasicInfo':cOutageBasicInfo,_e:cOutageApplVersion,_f:cOutageNotificationsSent,_g:cOutageNotificationsEnabled,_h:cOutageNotificationFilterEnabled,_i:cOutageFilteredEvents,'cOutageHistory':cOutageHistory,_j:cOutageHistTableSize,_k:cOutageHistMsgsFlushed,'cOutageHistoryTable':cOutageHistoryTable,'cOutageHistoryEntry':cOutageHistoryEntry,_X:cOutageEventIndex,_G:cOutageEventObjectType,_H:cOutageEventMonObjectIndex,_I:cOutageEventTypeIndex,_J:cOutageEventTime,_K:cOutageEventInterval,'cOutageDescription':cOutageDescription,'cOutageEventTypeMapTable':cOutageEventTypeMapTable,'cOutageEventTypeMapEntry':cOutageEventTypeMapEntry,_Y:cOutageEventTypeMapIndex,_l:cOutageEventTypeName,_m:cOutageEventTypeDescrText,'cOutageMonObject':cOutageMonObject,'cOutageObjectTable':cOutageObjectTable,'cOutageObjectEntry':cOutageObjectEntry,_Z:cOutageObjectType,_a:cOutageMonitoredObjectIndex,_L:cOutageCurrentStatus,_M:cOutageAOTSinceMeasureStarted,_N:cOutageNAFSinceMeasureStarted,_t:cOutageRecordingStartTime,'cOutageCpmMapping':cOutageCpmMapping,'cOutageCpmMapTable':cOutageCpmMapTable,'cOutageCpmMapEntry':cOutageCpmMapEntry,_b:cOutageCpmMapIndex,_o:cOutageCpmCPUTotalIndex,_p:cOutageCpmProcessPID,'cOutageRmtMapping':cOutageRmtMapping,'cOutageRemoteObjMapTable':cOutageRemoteObjMapTable,'cOutageRemoteObjMapEntry':cOutageRemoteObjMapEntry,_c:cOutageRemoteObjMapIndex,_q:cOutageRemoteObjIDType,_r:cOutageRemoteObjID,_s:cOutageRemoteObjDescrText,'cOutageLntMapping':cOutageLntMapping,'cOutageLogicalObjMapTable':cOutageLogicalObjMapTable,'cOutageLogicalObjMapEntry':cOutageLogicalObjMapEntry,_d:cOutageLogicalObjMapIndex,_u:cOutageLogicalObjDescrText,'ciscoOutageMIBNotificationPrefix':ciscoOutageMIBNotificationPrefix,'ciscoOutageMIBNotifications':ciscoOutageMIBNotifications,_v:ciscoOutageEvent,'ciscoOutageMIBConformance':ciscoOutageMIBConformance,'ciscoOutageMIBCompliances':ciscoOutageMIBCompliances,'ciscoOutageMIBCompliance':ciscoOutageMIBCompliance,'ciscoOutageMIBComplianceRev1':ciscoOutageMIBComplianceRev1,'ciscoOutageMIBGroups':ciscoOutageMIBGroups,_O:ciscoOutageBasicGroup,_P:ciscoEventHistoryGroup,_Q:ciscoEventDescrGroup,_w:ciscoObjectOutageGroup,_R:ciscoCpmMappingGroup,_S:ciscoRmtMappingGroup,_T:ciscoOutageNotificationsGroup,_x:ciscoObjectOutageGroupRev,_y:ciscoLntMappingGroup})