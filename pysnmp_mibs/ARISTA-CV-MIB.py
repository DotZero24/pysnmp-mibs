#
# PySNMP MIB module ARISTA-CV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-CV-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
aristaCvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 33))
aristaCvMIB.setRevisions(('2022-07-27 00:00',))
if mibBuilder.loadTexts: aristaCvMIB.setLastUpdated('202207270000Z')
if mibBuilder.loadTexts: aristaCvMIB.setOrganization('Arista Networks, Inc.')
class CvString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '65535t'

aristaCvNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 33, 0))
aristaCvObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1))
aristaCvConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 33, 2))
aristaCvAlertEventType = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 1), CvString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aristaCvAlertEventType.setStatus('current')
aristaCvAlertDescription = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 2), CvString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aristaCvAlertDescription.setStatus('current')
aristaCvAlertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("info", 1), ("warning", 2), ("error", 3), ("critical", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aristaCvAlertSeverity.setStatus('current')
aristaCvAlertTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 4), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aristaCvAlertTimestamp.setStatus('current')
aristaCvAlertKey = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 5), CvString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aristaCvAlertKey.setStatus('current')
aristaCvAlertSource = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 33, 1, 6), CvString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aristaCvAlertSource.setStatus('current')
aristaCvAlertFiringNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 33, 0, 1)).setObjects(("ARISTA-CV-MIB", "aristaCvAlertEventType"), ("ARISTA-CV-MIB", "aristaCvAlertDescription"), ("ARISTA-CV-MIB", "aristaCvAlertSeverity"), ("ARISTA-CV-MIB", "aristaCvAlertTimestamp"), ("ARISTA-CV-MIB", "aristaCvAlertKey"), ("ARISTA-CV-MIB", "aristaCvAlertSource"))
if mibBuilder.loadTexts: aristaCvAlertFiringNotification.setStatus('current')
aristaCvAlertResolvedNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 33, 0, 2)).setObjects(("ARISTA-CV-MIB", "aristaCvAlertEventType"), ("ARISTA-CV-MIB", "aristaCvAlertDescription"), ("ARISTA-CV-MIB", "aristaCvAlertSeverity"), ("ARISTA-CV-MIB", "aristaCvAlertTimestamp"), ("ARISTA-CV-MIB", "aristaCvAlertKey"), ("ARISTA-CV-MIB", "aristaCvAlertSource"))
if mibBuilder.loadTexts: aristaCvAlertResolvedNotification.setStatus('current')
aristaCvCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 1))
aristaCvGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 2))
aristaCvCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 1, 1)).setObjects(("ARISTA-CV-MIB", "aristaCvObjectsGroup"), ("ARISTA-CV-MIB", "aristaCvNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaCvCompliance = aristaCvCompliance.setStatus('current')
aristaCvObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 2, 1)).setObjects(("ARISTA-CV-MIB", "aristaCvAlertEventType"), ("ARISTA-CV-MIB", "aristaCvAlertDescription"), ("ARISTA-CV-MIB", "aristaCvAlertSeverity"), ("ARISTA-CV-MIB", "aristaCvAlertTimestamp"), ("ARISTA-CV-MIB", "aristaCvAlertKey"), ("ARISTA-CV-MIB", "aristaCvAlertSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaCvObjectsGroup = aristaCvObjectsGroup.setStatus('current')
aristaCvNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 33, 2, 2, 2)).setObjects(("ARISTA-CV-MIB", "aristaCvAlertFiringNotification"), ("ARISTA-CV-MIB", "aristaCvAlertResolvedNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaCvNotificationsGroup = aristaCvNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-CV-MIB", aristaCvAlertResolvedNotification=aristaCvAlertResolvedNotification, aristaCvNotifications=aristaCvNotifications, aristaCvNotificationsGroup=aristaCvNotificationsGroup, CvString=CvString, aristaCvMIB=aristaCvMIB, aristaCvGroups=aristaCvGroups, aristaCvObjects=aristaCvObjects, aristaCvAlertDescription=aristaCvAlertDescription, aristaCvConformance=aristaCvConformance, aristaCvAlertTimestamp=aristaCvAlertTimestamp, aristaCvAlertFiringNotification=aristaCvAlertFiringNotification, aristaCvCompliance=aristaCvCompliance, aristaCvObjectsGroup=aristaCvObjectsGroup, aristaCvAlertKey=aristaCvAlertKey, aristaCvAlertEventType=aristaCvAlertEventType, PYSNMP_MODULE_ID=aristaCvMIB, aristaCvAlertSeverity=aristaCvAlertSeverity, aristaCvCompliances=aristaCvCompliances, aristaCvAlertSource=aristaCvAlertSource)
