#
# PySNMP MIB module ARISTA-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arista/ARISTA-REDUNDANCY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
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
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancyGroups=aristaRedundancyGroups, aristaRedundancyCompliances=aristaRedundancyCompliances, aristaRedundancyNotificationsGroup=aristaRedundancyNotificationsGroup, aristaRedundancyStatusGroup=aristaRedundancyStatusGroup, PYSNMP_MODULE_ID=aristaRedundancyMIB, aristaRedundancyLastSwOverReason=aristaRedundancyLastSwOverReason, aristaRedundancyMIB=aristaRedundancyMIB, aristaRedundancyNotificationPrefix=aristaRedundancyNotificationPrefix, aristaRedundancyNotifications=aristaRedundancyNotifications, aristaRedundancyUnitStateEntryTime=aristaRedundancyUnitStateEntryTime, aristaRedundancyUnitState=aristaRedundancyUnitState, AristaRedundancyProtocol=AristaRedundancyProtocol, aristaRedundancyObjects=aristaRedundancyObjects, aristaRedundancyUnitStateEntry=aristaRedundancyUnitStateEntry, aristaRedundancyUnitId=aristaRedundancyUnitId, aristaRedundancyHistory=aristaRedundancyHistory, AristaRedundancyState=AristaRedundancyState, aristaRedundancyConformance=aristaRedundancyConformance, aristaRedundancyProtocolConfig=aristaRedundancyProtocolConfig, aristaRedundancySwitchOverNotif=aristaRedundancySwitchOverNotif, aristaRedundancyCompliance=aristaRedundancyCompliance, aristaRedundancyStatus=aristaRedundancyStatus, aristaRedundancyUnitStateTable=aristaRedundancyUnitStateTable, aristaRedundancyProtocolOper=aristaRedundancyProtocolOper)
