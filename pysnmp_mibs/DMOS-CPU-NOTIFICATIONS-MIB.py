#
# PySNMP MIB module DMOS-CPU-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/datacom/DMOS-CPU-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:43 2025
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
dmosCpuNotificationsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0))
dmosCpuNotificationsMIB.setRevisions(('2016-10-20 00:00',))
if mibBuilder.loadTexts: dmosCpuNotificationsMIB.setLastUpdated('201610200000Z')
if mibBuilder.loadTexts: dmosCpuNotificationsMIB.setOrganization('DATACOM')
dmosCpuNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1))
dmosCpuNotificationThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 1), UnsignedPercent()).setUnits('%').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dmosCpuNotificationThreshold.setStatus('current')
dmosCpuNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 2), Gauge32()).setUnits('seconds').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dmosCpuNotificationInterval.setStatus('current')
dmosCpuNotificationValue = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 3), UnsignedPercent()).setUnits('%').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dmosCpuNotificationValue.setStatus('current')
dmosCpuNotificationCoreId = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 1, 4), Gauge32()).setUnits('ID').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dmosCpuNotificationCoreId.setStatus('current')
dmosCpuNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 2))
dmosCpuAlarmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 2, 1)).setObjects(("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationThreshold"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationInterval"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationCoreId"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmosCpuAlarmInfoGroup = dmosCpuAlarmInfoGroup.setStatus('current')
dmosCpuAlarmTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 2, 2)).setObjects(("DMOS-CPU-NOTIFICATIONS-MIB", "cpuLoadHighTrap"), ("DMOS-CPU-NOTIFICATIONS-MIB", "cpuCoreHighTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmosCpuAlarmTrapsGroup = dmosCpuAlarmTrapsGroup.setStatus('current')
cpuLoadHighTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 3)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationThreshold"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationInterval"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationValue"))
if mibBuilder.loadTexts: cpuLoadHighTrap.setStatus('current')
cpuCoreHighTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 0, 4)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationThreshold"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationInterval"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationCoreId"), ("DMOS-CPU-NOTIFICATIONS-MIB", "dmosCpuNotificationValue"))
if mibBuilder.loadTexts: cpuCoreHighTrap.setStatus('current')
mibBuilder.exportSymbols("DMOS-CPU-NOTIFICATIONS-MIB", dmosCpuNotificationGroups=dmosCpuNotificationGroups, dmosCpuNotificationsMIB=dmosCpuNotificationsMIB, dmosCpuAlarmInfoGroup=dmosCpuAlarmInfoGroup, dmosCpuNotificationValue=dmosCpuNotificationValue, cpuCoreHighTrap=cpuCoreHighTrap, dmosCpuNotificationCoreId=dmosCpuNotificationCoreId, dmosCpuNotificationObjects=dmosCpuNotificationObjects, dmosCpuNotificationThreshold=dmosCpuNotificationThreshold, PYSNMP_MODULE_ID=dmosCpuNotificationsMIB, cpuLoadHighTrap=cpuLoadHighTrap, dmosCpuAlarmTrapsGroup=dmosCpuAlarmTrapsGroup, dmosCpuNotificationInterval=dmosCpuNotificationInterval)
