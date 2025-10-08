#
# PySNMP MIB module ENTERASYS-MAC-LOCKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-MAC-LOCKING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
etsysMACLockingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21))
etsysMACLockingMIB.setRevisions(('2014-07-07 13:31', '2014-06-02 11:21', '2011-08-03 18:25', '2011-06-08 12:38', '2011-03-08 19:47', '2007-05-21 13:04', '2007-05-17 12:55', '2007-05-09 19:24', '2007-04-16 15:26', '2003-07-30 15:45', '2003-01-17 21:14', '2002-08-05 20:30', '2002-08-01 14:45',))
if mibBuilder.loadTexts: etsysMACLockingMIB.setLastUpdated('201407071331Z')
if mibBuilder.loadTexts: etsysMACLockingMIB.setOrganization('Extreme Networks, Inc.')
etsysMACLockingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1))
etsysMACLockingSystemBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 1))
etsysMACLockingPortConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2))
etsysMACLockingStaticStationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3))
etsysMACLockingStationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4))
etsysMACLockingTrapBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0))
etsysMACLockingSystemEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingSystemEnable.setStatus('current')
etsysMACLockingPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1), )
if mibBuilder.loadTexts: etsysMACLockingPortTable.setStatus('current')
etsysMACLockingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1), ).setIndexNames((0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"))
if mibBuilder.loadTexts: etsysMACLockingPortEntry.setStatus('current')
etsysMACLockingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: etsysMACLockingPort.setStatus('current')
etsysMACLockingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingEnable.setStatus('current')
etsysMACLockingViolationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingViolationEnable.setStatus('current')
etsysMACLockingLastViolationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingLastViolationAddress.setStatus('current')
etsysMACLockingFirstArrivalStationsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalStationsAllowed.setStatus('current')
etsysMACLockingFirstArrivalStationsAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalStationsAllocated.setStatus('current')
etsysMACLockingStaticStationsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingStaticStationsAllowed.setStatus('current')
etsysMACLockingStaticStationsAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingStaticStationsAllocated.setStatus('current')
etsysMACLockingMoveFirstArrivalToStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingMoveFirstArrivalToStatic.setStatus('current')
etsysMACLockingStaticStationsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingStaticStationsCount.setStatus('current')
etsysMACLockingClearStaticStations = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingClearStaticStations.setStatus('current')
etsysMACLockingFirstArrivalAging = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalAging.setStatus('current')
etsysMACLockingViolationSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 13), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingViolationSyslogEnable.setStatus('current')
etsysMACLockingThresholdEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 14), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingThresholdEnable.setStatus('current')
etsysMACLockingThresholdSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 15), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingThresholdSyslogEnable.setStatus('current')
etsysMACLockingThresholdShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 16), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingThresholdShutdown.setStatus('current')
etsysMACLockingShutdownState = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingShutdownState.setStatus('current')
etsysMACLockingClearOnLink = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 18), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingClearOnLink.setStatus('current')
etsysMACLockingStaticStationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1), )
if mibBuilder.loadTexts: etsysMACLockingStaticStationTable.setStatus('current')
etsysMACLockingStaticStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1), ).setIndexNames((0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"), (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedAddress"))
if mibBuilder.loadTexts: etsysMACLockingStaticStationEntry.setStatus('current')
etsysMACLockingLockedAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: etsysMACLockingLockedAddress.setStatus('current')
etsysMACLockingStaticEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysMACLockingStaticEntryRowStatus.setStatus('current')
etsysMACLockingStationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1), )
if mibBuilder.loadTexts: etsysMACLockingStationTable.setStatus('current')
etsysMACLockingStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1), ).setIndexNames((0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"), (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedAddress"))
if mibBuilder.loadTexts: etsysMACLockingStationEntry.setStatus('current')
etsysMACLockingLockedEntryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("firstArrival", 2), ("agingFirstArrival", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingLockedEntryCause.setStatus('current')
etsysMACLockingRemoveStation = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingRemoveStation.setStatus('current')
etsysMACLockingMACViolation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0, 1)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLastViolationAddress"))
if mibBuilder.loadTexts: etsysMACLockingMACViolation.setStatus('current')
etsysMACLockingMACThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0, 2)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllocated"))
if mibBuilder.loadTexts: etsysMACLockingMACThreshold.setStatus('current')
etsysMACLockingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2))
etsysMACLockingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1))
etsysMACLockingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2))
etsysMACLockingSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 1)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingSystemGroup = etsysMACLockingSystemGroup.setStatus('current')
etsysMACLockingPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 2)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingViolationEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLastViolationAddress"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllowed"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllocated"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsAllowed"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsAllocated"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMoveFirstArrivalToStatic"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsCount"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingClearStaticStations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortGroup = etsysMACLockingPortGroup.setStatus('current')
etsysMACLockingStationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 3)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedEntryCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStationGroup = etsysMACLockingStationGroup.setStatus('deprecated')
etsysMACLockingStaticStationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 4)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStaticStationGroup = etsysMACLockingStaticStationGroup.setStatus('current')
etsysMACLockingPortFirstArrivalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 5)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalAging"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortFirstArrivalGroup = etsysMACLockingPortFirstArrivalGroup.setStatus('current')
etsysMACLockingStationGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 6)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedEntryCause"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingRemoveStation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStationGroup2 = etsysMACLockingStationGroup2.setStatus('current')
etsysMACLockingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 7)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMACViolation"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMACThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingNotificationGroup = etsysMACLockingNotificationGroup.setStatus('current')
etsysMACLockingPortMessageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 8)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingViolationSyslogEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortMessageGroup = etsysMACLockingPortMessageGroup.setStatus('current')
etsysMACLockingShutdownGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 9)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdShutdown"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingShutdownState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingShutdownGroup = etsysMACLockingShutdownGroup.setStatus('current')
etsysMACLockingLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 10)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingClearOnLink"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingLinkGroup = etsysMACLockingLinkGroup.setStatus('current')
etsysMACLockingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 1)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingCompliance = etsysMACLockingCompliance.setStatus('deprecated')
etsysMACLockingPortFirstArrivalCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 2)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortFirstArrivalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortFirstArrivalCompliance = etsysMACLockingPortFirstArrivalCompliance.setStatus('current')
etsysMACLockingCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 3)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStationGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingCompliance2 = etsysMACLockingCompliance2.setStatus('current')
etsysMACLockingNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 4)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingNotificationGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortMessageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingNotificationCompliance = etsysMACLockingNotificationCompliance.setStatus('current')
etsysMACLockingShutdownCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 5)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingShutdownGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingShutdownCompliance = etsysMACLockingShutdownCompliance.setStatus('current')
etsysMACLockingLinkCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 6)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingLinkCompliance = etsysMACLockingLinkCompliance.setStatus('current')
etsysMACLockingStaticStationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 7)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStaticStationCompliance = etsysMACLockingStaticStationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-MAC-LOCKING-MIB", etsysMACLockingStationTable=etsysMACLockingStationTable, etsysMACLockingFirstArrivalAging=etsysMACLockingFirstArrivalAging, etsysMACLockingTrapBranch=etsysMACLockingTrapBranch, etsysMACLockingNotificationCompliance=etsysMACLockingNotificationCompliance, etsysMACLockingViolationSyslogEnable=etsysMACLockingViolationSyslogEnable, etsysMACLockingPort=etsysMACLockingPort, etsysMACLockingGroups=etsysMACLockingGroups, etsysMACLockingMACThreshold=etsysMACLockingMACThreshold, etsysMACLockingClearStaticStations=etsysMACLockingClearStaticStations, etsysMACLockingCompliance2=etsysMACLockingCompliance2, etsysMACLockingNotificationGroup=etsysMACLockingNotificationGroup, etsysMACLockingLockedAddress=etsysMACLockingLockedAddress, etsysMACLockingPortMessageGroup=etsysMACLockingPortMessageGroup, etsysMACLockingCompliances=etsysMACLockingCompliances, etsysMACLockingMIB=etsysMACLockingMIB, etsysMACLockingStaticStationBranch=etsysMACLockingStaticStationBranch, etsysMACLockingClearOnLink=etsysMACLockingClearOnLink, etsysMACLockingShutdownCompliance=etsysMACLockingShutdownCompliance, etsysMACLockingFirstArrivalStationsAllocated=etsysMACLockingFirstArrivalStationsAllocated, etsysMACLockingStationEntry=etsysMACLockingStationEntry, etsysMACLockingSystemGroup=etsysMACLockingSystemGroup, etsysMACLockingConformance=etsysMACLockingConformance, etsysMACLockingPortFirstArrivalCompliance=etsysMACLockingPortFirstArrivalCompliance, etsysMACLockingLinkCompliance=etsysMACLockingLinkCompliance, etsysMACLockingLastViolationAddress=etsysMACLockingLastViolationAddress, etsysMACLockingStaticStationsAllocated=etsysMACLockingStaticStationsAllocated, etsysMACLockingPortEntry=etsysMACLockingPortEntry, etsysMACLockingThresholdShutdown=etsysMACLockingThresholdShutdown, etsysMACLockingMoveFirstArrivalToStatic=etsysMACLockingMoveFirstArrivalToStatic, etsysMACLockingThresholdEnable=etsysMACLockingThresholdEnable, etsysMACLockingPortTable=etsysMACLockingPortTable, etsysMACLockingSystemEnable=etsysMACLockingSystemEnable, etsysMACLockingFirstArrivalStationsAllowed=etsysMACLockingFirstArrivalStationsAllowed, etsysMACLockingStaticEntryRowStatus=etsysMACLockingStaticEntryRowStatus, etsysMACLockingStaticStationGroup=etsysMACLockingStaticStationGroup, etsysMACLockingObjects=etsysMACLockingObjects, PYSNMP_MODULE_ID=etsysMACLockingMIB, etsysMACLockingPortGroup=etsysMACLockingPortGroup, etsysMACLockingPortFirstArrivalGroup=etsysMACLockingPortFirstArrivalGroup, etsysMACLockingStationGroup2=etsysMACLockingStationGroup2, etsysMACLockingLinkGroup=etsysMACLockingLinkGroup, etsysMACLockingCompliance=etsysMACLockingCompliance, etsysMACLockingStaticStationCompliance=etsysMACLockingStaticStationCompliance, etsysMACLockingPortConfigBranch=etsysMACLockingPortConfigBranch, etsysMACLockingStaticStationsCount=etsysMACLockingStaticStationsCount, etsysMACLockingShutdownGroup=etsysMACLockingShutdownGroup, etsysMACLockingStaticStationTable=etsysMACLockingStaticStationTable, etsysMACLockingStaticStationEntry=etsysMACLockingStaticStationEntry, etsysMACLockingEnable=etsysMACLockingEnable, etsysMACLockingViolationEnable=etsysMACLockingViolationEnable, etsysMACLockingShutdownState=etsysMACLockingShutdownState, etsysMACLockingThresholdSyslogEnable=etsysMACLockingThresholdSyslogEnable, etsysMACLockingRemoveStation=etsysMACLockingRemoveStation, etsysMACLockingStationGroup=etsysMACLockingStationGroup, etsysMACLockingStationBranch=etsysMACLockingStationBranch, etsysMACLockingSystemBranch=etsysMACLockingSystemBranch, etsysMACLockingLockedEntryCause=etsysMACLockingLockedEntryCause, etsysMACLockingMACViolation=etsysMACLockingMACViolation, etsysMACLockingStaticStationsAllowed=etsysMACLockingStaticStationsAllowed)
