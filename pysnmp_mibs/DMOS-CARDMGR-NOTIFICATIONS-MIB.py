#
# PySNMP MIB module DMOS-CARDMGR-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/datacom/DMOS-CARDMGR-NOTIFICATIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:41:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
notificationTime, notificationName, notificationSourceValue, notificationInfo, alarmNotifications, notificationSourceType, notificationSeverity, notificationAlarmState = mibBuilder.importSymbols("DMOS-NOTIFICATIONS-MIB", "notificationTime", "notificationName", "notificationSourceValue", "notificationInfo", "alarmNotifications", "notificationSourceType", "notificationSeverity", "notificationAlarmState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DMOS-CARDMGR-NOTIFICATIONS-MIB", PYSNMP_MODULE_ID=dmosCardmgrNotificationsMIB, cardNotProvisionedAlarmTrap=cardNotProvisionedAlarmTrap, dmosCardmgrNotificationsMIB=dmosCardmgrNotificationsMIB, cardRemovedAlarmTrap=cardRemovedAlarmTrap, cardRemovedTrap=cardRemovedTrap, cardNotPresentAlarmTrap=cardNotPresentAlarmTrap, cardInsertedTrap=cardInsertedTrap, dmosCardmgrAlarmTrapsGroup=dmosCardmgrAlarmTrapsGroup, dmosCardmgrNotificationGroups=dmosCardmgrNotificationGroups, cardMismatchAlarmTrap=cardMismatchAlarmTrap)
