#
# PySNMP MIB module DMOS-MEM-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DMOS-MEM-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
notificationTime, notificationName, notificationSourceValue, notificationInfo, alarmNotifications, notificationSourceType, notificationSeverity, notificationAlarmState = mibBuilder.importSymbols("DMOS-NOTIFICATIONS-MIB", "notificationTime", "notificationName", "notificationSourceValue", "notificationInfo", "alarmNotifications", "notificationSourceType", "notificationSeverity", "notificationAlarmState")
UnsignedPercent, = mibBuilder.importSymbols("DMOS-TC-MIB", "UnsignedPercent")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DMOS-MEM-NOTIFICATIONS-MIB", dmosMemAlarmTrapsGroup=dmosMemAlarmTrapsGroup, dmosMemNotificationObjects=dmosMemNotificationObjects, memAvailableLowTrap=memAvailableLowTrap, PYSNMP_MODULE_ID=dmosMemNotificationsMIB, dmosMemNotificationThreshold=dmosMemNotificationThreshold, dmosMemNotificationsMIB=dmosMemNotificationsMIB, dmosMemNotificationGroups=dmosMemNotificationGroups, dmosMemAlarmInfoGroup=dmosMemAlarmInfoGroup, dmosMemNotificationInterval=dmosMemNotificationInterval)
