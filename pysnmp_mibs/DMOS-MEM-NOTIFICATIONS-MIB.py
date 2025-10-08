#
# PySNMP MIB module DMOS-MEM-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/datacom/DMOS-MEM-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
notificationSourceType, notificationSeverity, notificationTime, notificationSourceValue, notificationAlarmState, notificationInfo, alarmNotifications, notificationName = mibBuilder.importSymbols("DMOS-NOTIFICATIONS-MIB", "notificationSourceType", "notificationSeverity", "notificationTime", "notificationSourceValue", "notificationAlarmState", "notificationInfo", "alarmNotifications", "notificationName")
UnsignedPercent, = mibBuilder.importSymbols("DMOS-TC-MIB", "UnsignedPercent")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dmosMemNotificationsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1))
dmosMemNotificationsMIB.setRevisions(('2016-10-20 00:00',))
if mibBuilder.loadTexts: dmosMemNotificationsMIB.setLastUpdated('201610200000Z')
if mibBuilder.loadTexts: dmosMemNotificationsMIB.setOrganization('DATACOM')
dmosMemNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 1))
dmosMemNotificationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 1, 1), Gauge32()).setUnits('Bytes').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dmosMemNotificationThreshold.setStatus('current')
dmosMemNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 1, 2), Gauge32()).setUnits('seconds').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dmosMemNotificationInterval.setStatus('current')
dmosMemNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 2))
dmosMemAlarmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 2, 1)).setObjects(("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationThreshold"), ("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmosMemAlarmInfoGroup = dmosMemAlarmInfoGroup.setStatus('current')
dmosMemAlarmTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 2, 2)).setObjects(("DMOS-MEM-NOTIFICATIONS-MIB", "memAvailableLowTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmosMemAlarmTrapsGroup = dmosMemAlarmTrapsGroup.setStatus('current')
memAvailableLowTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 1, 3)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"), ("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationThreshold"), ("DMOS-MEM-NOTIFICATIONS-MIB", "dmosMemNotificationInterval"))
if mibBuilder.loadTexts: memAvailableLowTrap.setStatus('current')
mibBuilder.exportSymbols("DMOS-MEM-NOTIFICATIONS-MIB", dmosMemAlarmTrapsGroup=dmosMemAlarmTrapsGroup, dmosMemNotificationsMIB=dmosMemNotificationsMIB, dmosMemNotificationGroups=dmosMemNotificationGroups, dmosMemAlarmInfoGroup=dmosMemAlarmInfoGroup, memAvailableLowTrap=memAvailableLowTrap, dmosMemNotificationThreshold=dmosMemNotificationThreshold, dmosMemNotificationObjects=dmosMemNotificationObjects, PYSNMP_MODULE_ID=dmosMemNotificationsMIB, dmosMemNotificationInterval=dmosMemNotificationInterval)
