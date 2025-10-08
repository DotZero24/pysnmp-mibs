#
# PySNMP MIB module ARICENT-MPLS-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aricent/ARICENT-MPLS-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PwIndexType, = mibBuilder.importSymbols("PW-TC-STD-MIB", "PwIndexType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
fsMplsNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2076, 13, 10))
fsMplsNotificationMIB.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsMplsNotificationMIB.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsMplsNotificationMIB.setOrganization('ARICENT COMMUNICATIONS SOFTWARE')
fsMplsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 13, 10, 0))
fsMplsNotifConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 13, 10, 1))
fsMplsPwStatusNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 2076, 13, 10, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMplsPwStatusNotifEnable.setStatus('current')
fsMplsPwOAMStatusNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 2076, 13, 10, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMplsPwOAMStatusNotifEnable.setStatus('deprecated')
fsMplsPwNotifStatusStr = MibScalar((1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fsMplsPwNotifStatusStr.setStatus('current')
fsMplsPwIndex = MibScalar((1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 2), PwIndexType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fsMplsPwIndex.setStatus('current')
fsMplsPwOamStatus = NotificationType((1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 3)).setObjects(("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwIndex"), ("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwNotifStatusStr"))
if mibBuilder.loadTexts: fsMplsPwOamStatus.setStatus('deprecated')
fsMplsPwStatus = NotificationType((1, 3, 6, 1, 4, 1, 2076, 13, 10, 0, 4)).setObjects(("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwIndex"), ("ARICENT-MPLS-NOTIFICATION-MIB", "fsMplsPwNotifStatusStr"))
if mibBuilder.loadTexts: fsMplsPwStatus.setStatus('current')
mibBuilder.exportSymbols("ARICENT-MPLS-NOTIFICATION-MIB", fsMplsPwNotifStatusStr=fsMplsPwNotifStatusStr, fsMplsPwStatus=fsMplsPwStatus, fsMplsNotifications=fsMplsNotifications, fsMplsPwIndex=fsMplsPwIndex, fsMplsNotificationMIB=fsMplsNotificationMIB, fsMplsPwOamStatus=fsMplsPwOamStatus, PYSNMP_MODULE_ID=fsMplsNotificationMIB, fsMplsPwOAMStatusNotifEnable=fsMplsPwOAMStatusNotifEnable, fsMplsPwStatusNotifEnable=fsMplsPwStatusNotifEnable, fsMplsNotifConfig=fsMplsNotifConfig)
