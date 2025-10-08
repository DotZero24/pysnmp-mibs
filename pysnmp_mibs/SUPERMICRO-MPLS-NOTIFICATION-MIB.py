#
# PySNMP MIB module SUPERMICRO-MPLS-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-MPLS-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PwIndexType, = mibBuilder.importSymbols("PW-TC-STD-MIB", "PwIndexType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
fsMplsNotificationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10))
fsMplsNotificationMIB.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsMplsNotificationMIB.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsMplsNotificationMIB.setOrganization('Super Micro Computer Inc.')
fsMplsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 0))
fsMplsNotifConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 1))
fsMplsPwStatusNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMplsPwStatusNotifEnable.setStatus('current')
fsMplsPwOAMStatusNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMplsPwOAMStatusNotifEnable.setStatus('deprecated')
fsMplsPwNotifStatusStr = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 0, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fsMplsPwNotifStatusStr.setStatus('current')
fsMplsPwIndex = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 0, 2), PwIndexType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: fsMplsPwIndex.setStatus('current')
fsMplsPwOamStatus = NotificationType((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 0, 3)).setObjects(("SUPERMICRO-MPLS-NOTIFICATION-MIB", "fsMplsPwIndex"), ("SUPERMICRO-MPLS-NOTIFICATION-MIB", "fsMplsPwNotifStatusStr"))
if mibBuilder.loadTexts: fsMplsPwOamStatus.setStatus('deprecated')
fsMplsPwStatus = NotificationType((1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 10, 0, 4)).setObjects(("SUPERMICRO-MPLS-NOTIFICATION-MIB", "fsMplsPwIndex"), ("SUPERMICRO-MPLS-NOTIFICATION-MIB", "fsMplsPwNotifStatusStr"))
if mibBuilder.loadTexts: fsMplsPwStatus.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-MPLS-NOTIFICATION-MIB", fsMplsPwOamStatus=fsMplsPwOamStatus, fsMplsPwIndex=fsMplsPwIndex, PYSNMP_MODULE_ID=fsMplsNotificationMIB, fsMplsPwStatus=fsMplsPwStatus, fsMplsPwNotifStatusStr=fsMplsPwNotifStatusStr, fsMplsNotifConfig=fsMplsNotifConfig, fsMplsPwOAMStatusNotifEnable=fsMplsPwOAMStatusNotifEnable, fsMplsPwStatusNotifEnable=fsMplsPwStatusNotifEnable, fsMplsNotificationMIB=fsMplsNotificationMIB, fsMplsNotifications=fsMplsNotifications)
