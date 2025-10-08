#
# PySNMP MIB module DMOS-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DMOS-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
datacomDevicesMIBs, = mibBuilder.importSymbols("DATACOM-SMI", "datacomDevicesMIBs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DMOS-NOTIFICATIONS-MIB", alarmNotificationGroup=alarmNotificationGroup, infoNotificationGroup=infoNotificationGroup, notificationName=notificationName, notificationInfo=notificationInfo, dmosNotificationsMIB=dmosNotificationsMIB, notificationSourceType=notificationSourceType, alarmNotifications=alarmNotifications, notificationObjects=notificationObjects, notificationSourceValue=notificationSourceValue, PYSNMP_MODULE_ID=dmosNotificationsMIB, notificationSeverity=notificationSeverity, notificationTime=notificationTime, notificationGroups=notificationGroups, notificationAlarmState=notificationAlarmState)
