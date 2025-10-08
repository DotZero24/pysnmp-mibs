#
# PySNMP MIB module DMOS-CPU-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DMOS-CPU-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:58 2025
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
mibBuilder.exportSymbols("DMOS-CPU-NOTIFICATIONS-MIB", dmosCpuNotificationThreshold=dmosCpuNotificationThreshold, dmosCpuNotificationGroups=dmosCpuNotificationGroups, cpuCoreHighTrap=cpuCoreHighTrap, dmosCpuNotificationsMIB=dmosCpuNotificationsMIB, dmosCpuNotificationValue=dmosCpuNotificationValue, PYSNMP_MODULE_ID=dmosCpuNotificationsMIB, dmosCpuAlarmInfoGroup=dmosCpuAlarmInfoGroup, dmosCpuAlarmTrapsGroup=dmosCpuAlarmTrapsGroup, cpuLoadHighTrap=cpuLoadHighTrap, dmosCpuNotificationInterval=dmosCpuNotificationInterval, dmosCpuNotificationObjects=dmosCpuNotificationObjects, dmosCpuNotificationCoreId=dmosCpuNotificationCoreId)
