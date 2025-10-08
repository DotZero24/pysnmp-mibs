#
# PySNMP MIB module SUN-CLUSTER-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oracle/SUN-CLUSTER-EVENTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sunClusterEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 80, 2))
sunClusterEventsMIB.setRevisions(('1902-11-30 00:00',))
if mibBuilder.loadTexts: sunClusterEventsMIB.setLastUpdated('0211300000Z')
if mibBuilder.loadTexts: sunClusterEventsMIB.setOrganization('Sun Microsystems')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
suncluster = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80))
scEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1))
scEventsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2))
class ScEventTableCount(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(20, 32767)

class ScEventIndex(TextualConvention, Integer32):
    status = 'current'

class ScClusterId(DisplayString):
    status = 'current'

class ScClusterName(DisplayString):
    status = 'current'

class ScNodeName(DisplayString):
    status = 'current'

class ScEventVersion(TextualConvention, Integer32):
    status = 'current'

class ScEventClassName(DisplayString):
    status = 'current'

class ScEventSubclassName(DisplayString):
    status = 'current'

class ScEventSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("clEventSevInfo", 0), ("clEventSevWarning", 1), ("clEventSevError", 2), ("clEventSevCritical", 3), ("clEventSevFatal", 4))

class ScEventInitiator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("clEventInitUnknown", 0), ("clEventInitSystem", 1), ("clEventInitOperator", 2), ("clEventInitAgent", 3))

class ScEventPublisher(DisplayString):
    status = 'current'

class ScEventPid(TextualConvention, Counter64):
    status = 'current'

class ScTimeStamp(TextualConvention, Counter64):
    status = 'current'

class ScEventData(DisplayString):
    status = 'current'

class ScEventAttributeName(DisplayString):
    status = 'current'

class ScEventAttributeValue(DisplayString):
    status = 'current'

escEventTableCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 1), ScEventTableCount()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: escEventTableCount.setStatus('current')
escEventsTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2), )
if mibBuilder.loadTexts: escEventsTable.setStatus('current')
escEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1), ).setIndexNames((0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"))
if mibBuilder.loadTexts: escEventsEntry.setStatus('current')
eventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 1), ScEventIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIndex.setStatus('current')
eventClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 2), ScClusterId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClusterId.setStatus('current')
eventClusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 3), ScClusterName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClusterName.setStatus('current')
eventNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 4), ScNodeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventNodeName.setStatus('current')
eventVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 5), ScEventVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventVersion.setStatus('current')
eventClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 6), ScEventClassName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClassName.setStatus('current')
eventSubclassName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 7), ScEventSubclassName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSubclassName.setStatus('current')
eventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 8), ScEventSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
eventInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 9), ScEventInitiator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventInitiator.setStatus('current')
eventPublisher = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 10), ScEventPublisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPublisher.setStatus('current')
eventSeqNo = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeqNo.setStatus('current')
eventPid = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 12), ScEventPid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPid.setStatus('current')
eventTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 13), ScTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
eventData = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 14), ScEventData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventData.setStatus('current')
escEventsAttributesTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3), )
if mibBuilder.loadTexts: escEventsAttributesTable.setStatus('current')
escEventsAttributesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1), ).setIndexNames((0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"), (0, "SUN-CLUSTER-EVENTS-MIB", "attributeName"))
if mibBuilder.loadTexts: escEventsAttributesEntry.setStatus('current')
attributeName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 1), ScEventAttributeName())
if mibBuilder.loadTexts: attributeName.setStatus('current')
attributeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 2), ScEventAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attributeValue.setStatus('current')
escNewEvents = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2, 1)).setObjects(("SUN-CLUSTER-EVENTS-MIB", "eventIndex"), ("SUN-CLUSTER-EVENTS-MIB", "eventClusterId"), ("SUN-CLUSTER-EVENTS-MIB", "eventClusterName"), ("SUN-CLUSTER-EVENTS-MIB", "eventNodeName"), ("SUN-CLUSTER-EVENTS-MIB", "eventVersion"), ("SUN-CLUSTER-EVENTS-MIB", "eventClassName"), ("SUN-CLUSTER-EVENTS-MIB", "eventSubclassName"), ("SUN-CLUSTER-EVENTS-MIB", "eventSeverity"), ("SUN-CLUSTER-EVENTS-MIB", "eventInitiator"), ("SUN-CLUSTER-EVENTS-MIB", "eventPublisher"), ("SUN-CLUSTER-EVENTS-MIB", "eventSeqNo"), ("SUN-CLUSTER-EVENTS-MIB", "eventPid"), ("SUN-CLUSTER-EVENTS-MIB", "eventTimeStamp"), ("SUN-CLUSTER-EVENTS-MIB", "eventData"))
if mibBuilder.loadTexts: escNewEvents.setStatus('current')
mibBuilder.exportSymbols("SUN-CLUSTER-EVENTS-MIB", ScEventAttributeValue=ScEventAttributeValue, eventVersion=eventVersion, escEventsTable=escEventsTable, eventClusterId=eventClusterId, attributeValue=attributeValue, escEventTableCount=escEventTableCount, eventPid=eventPid, sunClusterEventsMIB=sunClusterEventsMIB, ScEventAttributeName=ScEventAttributeName, scEventsMIBNotifications=scEventsMIBNotifications, ScClusterId=ScClusterId, eventClusterName=eventClusterName, ScEventPublisher=ScEventPublisher, eventPublisher=eventPublisher, eventSubclassName=eventSubclassName, ScEventIndex=ScEventIndex, ScTimeStamp=ScTimeStamp, attributeName=attributeName, ScEventClassName=ScEventClassName, ScEventPid=ScEventPid, sun=sun, escEventsEntry=escEventsEntry, ScEventData=ScEventData, suncluster=suncluster, escEventsAttributesTable=escEventsAttributesTable, eventTimeStamp=eventTimeStamp, scEventsMIBObjects=scEventsMIBObjects, ScEventSeverity=ScEventSeverity, escEventsAttributesEntry=escEventsAttributesEntry, escNewEvents=escNewEvents, ScEventInitiator=ScEventInitiator, eventInitiator=eventInitiator, ScEventSubclassName=ScEventSubclassName, ScNodeName=ScNodeName, ScClusterName=ScClusterName, eventIndex=eventIndex, eventData=eventData, PYSNMP_MODULE_ID=sunClusterEventsMIB, eventSeqNo=eventSeqNo, eventSeverity=eventSeverity, ScEventVersion=ScEventVersion, ScEventTableCount=ScEventTableCount, eventClassName=eventClassName, prod=prod, eventNodeName=eventNodeName)
