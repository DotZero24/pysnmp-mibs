#
# PySNMP MIB module DMOS-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/datacom/DMOS-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
datacomDevicesMIBs, = mibBuilder.importSymbols("DATACOM-SMI", "datacomDevicesMIBs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
dmosNotificationsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3))
dmosNotificationsMIB.setRevisions(('2016-10-20 00:00',))
if mibBuilder.loadTexts: dmosNotificationsMIB.setLastUpdated('201610200000Z')
if mibBuilder.loadTexts: dmosNotificationsMIB.setOrganization('DATACOM')
notificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1))
notificationTime = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationTime.setStatus('current')
notificationName = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationName.setStatus('current')
notificationSourceType = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationSourceType.setStatus('current')
notificationSourceValue = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationSourceValue.setStatus('current')
notificationSeverity = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationSeverity.setStatus('current')
notificationInfo = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationInfo.setStatus('current')
notificationAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("clear", 1), ("set", 2), ("unstable", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: notificationAlarmState.setStatus('current')
notificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 2))
infoNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 2, 1)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    infoNotificationGroup = infoNotificationGroup.setStatus('current')
alarmNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 2, 2)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alarmNotificationGroup = alarmNotificationGroup.setStatus('current')
alarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3))
mibBuilder.exportSymbols("DMOS-NOTIFICATIONS-MIB", alarmNotificationGroup=alarmNotificationGroup, alarmNotifications=alarmNotifications, notificationName=notificationName, notificationInfo=notificationInfo, notificationAlarmState=notificationAlarmState, dmosNotificationsMIB=dmosNotificationsMIB, notificationSeverity=notificationSeverity, notificationSourceType=notificationSourceType, notificationTime=notificationTime, PYSNMP_MODULE_ID=dmosNotificationsMIB, infoNotificationGroup=infoNotificationGroup, notificationSourceValue=notificationSourceValue, notificationGroups=notificationGroups, notificationObjects=notificationObjects)
