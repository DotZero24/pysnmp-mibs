_R='eventData'
_Q='eventTimeStamp'
_P='eventPid'
_O='eventSeqNo'
_N='eventPublisher'
_M='eventInitiator'
_L='eventSeverity'
_K='eventSubclassName'
_J='eventClassName'
_I='eventVersion'
_H='eventNodeName'
_G='eventClusterName'
_F='eventClusterId'
_E='attributeName'
_D='eventIndex'
_C='read-only'
_B='SUN-CLUSTER-EVENTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sunClusterEventsMIB=ModuleIdentity((1,3,6,1,4,1,42,2,80,2))
if mibBuilder.loadTexts:sunClusterEventsMIB.setRevisions(('1902-11-30 00:00',))
class ScEventTableCount(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,32767))
class ScEventIndex(TextualConvention,Integer32):status=_A
class ScClusterId(DisplayString):status=_A
class ScClusterName(DisplayString):status=_A
class ScNodeName(DisplayString):status=_A
class ScEventVersion(TextualConvention,Integer32):status=_A
class ScEventClassName(DisplayString):status=_A
class ScEventSubclassName(DisplayString):status=_A
class ScEventSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('clEventSevInfo',0),('clEventSevWarning',1),('clEventSevError',2),('clEventSevCritical',3),('clEventSevFatal',4)))
class ScEventInitiator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('clEventInitUnknown',0),('clEventInitSystem',1),('clEventInitOperator',2),('clEventInitAgent',3)))
class ScEventPublisher(DisplayString):status=_A
class ScEventPid(TextualConvention,Counter64):status=_A
class ScTimeStamp(TextualConvention,Counter64):status=_A
class ScEventData(DisplayString):status=_A
class ScEventAttributeName(DisplayString):status=_A
class ScEventAttributeValue(DisplayString):status=_A
_Sun_ObjectIdentity=ObjectIdentity
sun=_Sun_ObjectIdentity((1,3,6,1,4,1,42))
_Prod_ObjectIdentity=ObjectIdentity
prod=_Prod_ObjectIdentity((1,3,6,1,4,1,42,2))
_Suncluster_ObjectIdentity=ObjectIdentity
suncluster=_Suncluster_ObjectIdentity((1,3,6,1,4,1,42,2,80))
_ScEventsMIBObjects_ObjectIdentity=ObjectIdentity
scEventsMIBObjects=_ScEventsMIBObjects_ObjectIdentity((1,3,6,1,4,1,42,2,80,2,1))
_EscEventTableCount_Type=ScEventTableCount
_EscEventTableCount_Object=MibScalar
escEventTableCount=_EscEventTableCount_Object((1,3,6,1,4,1,42,2,80,2,1,1),_EscEventTableCount_Type())
escEventTableCount.setMaxAccess('read-write')
if mibBuilder.loadTexts:escEventTableCount.setStatus(_A)
_EscEventsTable_Object=MibTable
escEventsTable=_EscEventsTable_Object((1,3,6,1,4,1,42,2,80,2,1,2))
if mibBuilder.loadTexts:escEventsTable.setStatus(_A)
_EscEventsEntry_Object=MibTableRow
escEventsEntry=_EscEventsEntry_Object((1,3,6,1,4,1,42,2,80,2,1,2,1))
escEventsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:escEventsEntry.setStatus(_A)
_EventIndex_Type=ScEventIndex
_EventIndex_Object=MibTableColumn
eventIndex=_EventIndex_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,1),_EventIndex_Type())
eventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eventIndex.setStatus(_A)
_EventClusterId_Type=ScClusterId
_EventClusterId_Object=MibTableColumn
eventClusterId=_EventClusterId_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,2),_EventClusterId_Type())
eventClusterId.setMaxAccess(_C)
if mibBuilder.loadTexts:eventClusterId.setStatus(_A)
_EventClusterName_Type=ScClusterName
_EventClusterName_Object=MibTableColumn
eventClusterName=_EventClusterName_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,3),_EventClusterName_Type())
eventClusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventClusterName.setStatus(_A)
_EventNodeName_Type=ScNodeName
_EventNodeName_Object=MibTableColumn
eventNodeName=_EventNodeName_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,4),_EventNodeName_Type())
eventNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventNodeName.setStatus(_A)
_EventVersion_Type=ScEventVersion
_EventVersion_Object=MibTableColumn
eventVersion=_EventVersion_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,5),_EventVersion_Type())
eventVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eventVersion.setStatus(_A)
_EventClassName_Type=ScEventClassName
_EventClassName_Object=MibTableColumn
eventClassName=_EventClassName_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,6),_EventClassName_Type())
eventClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventClassName.setStatus(_A)
_EventSubclassName_Type=ScEventSubclassName
_EventSubclassName_Object=MibTableColumn
eventSubclassName=_EventSubclassName_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,7),_EventSubclassName_Type())
eventSubclassName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventSubclassName.setStatus(_A)
_EventSeverity_Type=ScEventSeverity
_EventSeverity_Object=MibTableColumn
eventSeverity=_EventSeverity_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,8),_EventSeverity_Type())
eventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eventSeverity.setStatus(_A)
_EventInitiator_Type=ScEventInitiator
_EventInitiator_Object=MibTableColumn
eventInitiator=_EventInitiator_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,9),_EventInitiator_Type())
eventInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:eventInitiator.setStatus(_A)
_EventPublisher_Type=ScEventPublisher
_EventPublisher_Object=MibTableColumn
eventPublisher=_EventPublisher_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,10),_EventPublisher_Type())
eventPublisher.setMaxAccess(_C)
if mibBuilder.loadTexts:eventPublisher.setStatus(_A)
_EventSeqNo_Type=Counter64
_EventSeqNo_Object=MibTableColumn
eventSeqNo=_EventSeqNo_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,11),_EventSeqNo_Type())
eventSeqNo.setMaxAccess(_C)
if mibBuilder.loadTexts:eventSeqNo.setStatus(_A)
_EventPid_Type=ScEventPid
_EventPid_Object=MibTableColumn
eventPid=_EventPid_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,12),_EventPid_Type())
eventPid.setMaxAccess(_C)
if mibBuilder.loadTexts:eventPid.setStatus(_A)
_EventTimeStamp_Type=ScTimeStamp
_EventTimeStamp_Object=MibTableColumn
eventTimeStamp=_EventTimeStamp_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,13),_EventTimeStamp_Type())
eventTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:eventTimeStamp.setStatus(_A)
_EventData_Type=ScEventData
_EventData_Object=MibTableColumn
eventData=_EventData_Object((1,3,6,1,4,1,42,2,80,2,1,2,1,14),_EventData_Type())
eventData.setMaxAccess(_C)
if mibBuilder.loadTexts:eventData.setStatus(_A)
_EscEventsAttributesTable_Object=MibTable
escEventsAttributesTable=_EscEventsAttributesTable_Object((1,3,6,1,4,1,42,2,80,2,1,3))
if mibBuilder.loadTexts:escEventsAttributesTable.setStatus(_A)
_EscEventsAttributesEntry_Object=MibTableRow
escEventsAttributesEntry=_EscEventsAttributesEntry_Object((1,3,6,1,4,1,42,2,80,2,1,3,1))
escEventsAttributesEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:escEventsAttributesEntry.setStatus(_A)
_AttributeName_Type=ScEventAttributeName
_AttributeName_Object=MibTableColumn
attributeName=_AttributeName_Object((1,3,6,1,4,1,42,2,80,2,1,3,1,1),_AttributeName_Type())
attributeName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:attributeName.setStatus(_A)
_AttributeValue_Type=ScEventAttributeValue
_AttributeValue_Object=MibTableColumn
attributeValue=_AttributeValue_Object((1,3,6,1,4,1,42,2,80,2,1,3,1,2),_AttributeValue_Type())
attributeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:attributeValue.setStatus(_A)
_ScEventsMIBNotifications_ObjectIdentity=ObjectIdentity
scEventsMIBNotifications=_ScEventsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,42,2,80,2,2))
escNewEvents=NotificationType((1,3,6,1,4,1,42,2,80,2,2,1))
escNewEvents.setObjects(*((_B,_D),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:escNewEvents.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ScEventTableCount':ScEventTableCount,'ScEventIndex':ScEventIndex,'ScClusterId':ScClusterId,'ScClusterName':ScClusterName,'ScNodeName':ScNodeName,'ScEventVersion':ScEventVersion,'ScEventClassName':ScEventClassName,'ScEventSubclassName':ScEventSubclassName,'ScEventSeverity':ScEventSeverity,'ScEventInitiator':ScEventInitiator,'ScEventPublisher':ScEventPublisher,'ScEventPid':ScEventPid,'ScTimeStamp':ScTimeStamp,'ScEventData':ScEventData,'ScEventAttributeName':ScEventAttributeName,'ScEventAttributeValue':ScEventAttributeValue,'sun':sun,'prod':prod,'suncluster':suncluster,'sunClusterEventsMIB':sunClusterEventsMIB,'scEventsMIBObjects':scEventsMIBObjects,'escEventTableCount':escEventTableCount,'escEventsTable':escEventsTable,'escEventsEntry':escEventsEntry,_D:eventIndex,_F:eventClusterId,_G:eventClusterName,_H:eventNodeName,_I:eventVersion,_J:eventClassName,_K:eventSubclassName,_L:eventSeverity,_M:eventInitiator,_N:eventPublisher,_O:eventSeqNo,_P:eventPid,_Q:eventTimeStamp,_R:eventData,'escEventsAttributesTable':escEventsAttributesTable,'escEventsAttributesEntry':escEventsAttributesEntry,_E:attributeName,'attributeValue':attributeValue,'scEventsMIBNotifications':scEventsMIBNotifications,'escNewEvents':escNewEvents})