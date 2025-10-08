#
# PySNMP MIB module ARISTA-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-REDUNDANCY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
aristaRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 8))
aristaRedundancyMIB.setRevisions(('2014-08-15 00:00', '2012-11-10 22:37',))
if mibBuilder.loadTexts: aristaRedundancyMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaRedundancyMIB.setOrganization('Arista Networks, Inc.')
class AristaRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("standby", 1), ("active", 2), ("disabled", 3))

class AristaRedundancyProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("simplex", 1), ("rpr", 2), ("sso", 3))

aristaRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0))
aristaRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1))
aristaRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2))
aristaRedundancyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0))
aristaRedundancyHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 1))
aristaRedundancyProtocolConfig = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 1), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolConfig.setStatus('current')
aristaRedundancyProtocolOper = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 2), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolOper.setStatus('current')
aristaRedundancyUnitStateTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3), )
if mibBuilder.loadTexts: aristaRedundancyUnitStateTable.setStatus('current')
aristaRedundancyUnitStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1), ).setIndexNames((0, "ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitId"))
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntry.setStatus('current')
aristaRedundancyUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaRedundancyUnitId.setStatus('current')
aristaRedundancyUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 2), AristaRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitState.setStatus('current')
aristaRedundancyUnitStateEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntryTime.setStatus('current')
aristaRedundancyLastSwOverReason = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyLastSwOverReason.setStatus('current')
aristaRedundancyNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0))
aristaRedundancySwitchOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
if mibBuilder.loadTexts: aristaRedundancySwitchOverNotif.setStatus('current')
aristaRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1))
aristaRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2))
aristaRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyStatusGroup"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyCompliance = aristaRedundancyCompliance.setStatus('current')
aristaRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolConfig"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolOper"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitState"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyStatusGroup = aristaRedundancyStatusGroup.setStatus('current')
aristaRedundancyNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 2)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancySwitchOverNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyNotificationsGroup = aristaRedundancyNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancyUnitState=aristaRedundancyUnitState, aristaRedundancyUnitStateEntry=aristaRedundancyUnitStateEntry, aristaRedundancyStatus=aristaRedundancyStatus, aristaRedundancyObjects=aristaRedundancyObjects, aristaRedundancySwitchOverNotif=aristaRedundancySwitchOverNotif, aristaRedundancyUnitId=aristaRedundancyUnitId, aristaRedundancyGroups=aristaRedundancyGroups, aristaRedundancyCompliance=aristaRedundancyCompliance, aristaRedundancyNotificationsGroup=aristaRedundancyNotificationsGroup, aristaRedundancyStatusGroup=aristaRedundancyStatusGroup, AristaRedundancyProtocol=AristaRedundancyProtocol, AristaRedundancyState=AristaRedundancyState, aristaRedundancyNotifications=aristaRedundancyNotifications, aristaRedundancyNotificationPrefix=aristaRedundancyNotificationPrefix, aristaRedundancyHistory=aristaRedundancyHistory, aristaRedundancyMIB=aristaRedundancyMIB, aristaRedundancyConformance=aristaRedundancyConformance, aristaRedundancyProtocolConfig=aristaRedundancyProtocolConfig, aristaRedundancyUnitStateEntryTime=aristaRedundancyUnitStateEntryTime, aristaRedundancyCompliances=aristaRedundancyCompliances, aristaRedundancyLastSwOverReason=aristaRedundancyLastSwOverReason, aristaRedundancyUnitStateTable=aristaRedundancyUnitStateTable, PYSNMP_MODULE_ID=aristaRedundancyMIB, aristaRedundancyProtocolOper=aristaRedundancyProtocolOper)
