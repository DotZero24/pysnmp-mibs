#
# PySNMP MIB module DMOS-CARDMGR-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/datacom/DMOS-CARDMGR-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
notificationSourceType, notificationSeverity, notificationTime, notificationSourceValue, notificationAlarmState, notificationInfo, alarmNotifications, notificationName = mibBuilder.importSymbols("DMOS-NOTIFICATIONS-MIB", "notificationSourceType", "notificationSeverity", "notificationTime", "notificationSourceValue", "notificationAlarmState", "notificationInfo", "alarmNotifications", "notificationName")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dmosCardmgrNotificationsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3))
dmosCardmgrNotificationsMIB.setRevisions(('2017-11-27 00:00',))
if mibBuilder.loadTexts: dmosCardmgrNotificationsMIB.setLastUpdated('201711270000Z')
if mibBuilder.loadTexts: dmosCardmgrNotificationsMIB.setOrganization('DATACOM')
dmosCardmgrNotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 1))
dmosCardmgrAlarmTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 1, 1)).setObjects(("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardNotProvisionedAlarmTrap"), ("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardNotPresentAlarmTrap"), ("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardRemovedAlarmTrap"), ("DMOS-CARDMGR-NOTIFICATIONS-MIB", "cardMismatchAlarmTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dmosCardmgrAlarmTrapsGroup = dmosCardmgrAlarmTrapsGroup.setStatus('current')
cardNotProvisionedAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 2)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
if mibBuilder.loadTexts: cardNotProvisionedAlarmTrap.setStatus('current')
cardNotPresentAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 3)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
if mibBuilder.loadTexts: cardNotPresentAlarmTrap.setStatus('current')
cardRemovedAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 4)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
if mibBuilder.loadTexts: cardRemovedAlarmTrap.setStatus('current')
cardMismatchAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 5)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationSeverity"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"), ("DMOS-NOTIFICATIONS-MIB", "notificationAlarmState"))
if mibBuilder.loadTexts: cardMismatchAlarmTrap.setStatus('current')
cardInsertedTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 6)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"))
if mibBuilder.loadTexts: cardInsertedTrap.setStatus('current')
cardRemovedTrap = NotificationType((1, 3, 6, 1, 4, 1, 3709, 3, 6, 3, 3, 3, 7)).setObjects(("DMOS-NOTIFICATIONS-MIB", "notificationTime"), ("DMOS-NOTIFICATIONS-MIB", "notificationName"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceType"), ("DMOS-NOTIFICATIONS-MIB", "notificationSourceValue"), ("DMOS-NOTIFICATIONS-MIB", "notificationInfo"))
if mibBuilder.loadTexts: cardRemovedTrap.setStatus('current')
mibBuilder.exportSymbols("DMOS-CARDMGR-NOTIFICATIONS-MIB", PYSNMP_MODULE_ID=dmosCardmgrNotificationsMIB, cardMismatchAlarmTrap=cardMismatchAlarmTrap, cardRemovedTrap=cardRemovedTrap, cardRemovedAlarmTrap=cardRemovedAlarmTrap, dmosCardmgrAlarmTrapsGroup=dmosCardmgrAlarmTrapsGroup, cardNotPresentAlarmTrap=cardNotPresentAlarmTrap, dmosCardmgrNotificationGroups=dmosCardmgrNotificationGroups, cardNotProvisionedAlarmTrap=cardNotProvisionedAlarmTrap, cardInsertedTrap=cardInsertedTrap, dmosCardmgrNotificationsMIB=dmosCardmgrNotificationsMIB)
