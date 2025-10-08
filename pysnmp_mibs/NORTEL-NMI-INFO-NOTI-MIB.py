#
# PySNMP MIB module NORTEL-NMI-INFO-NOTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NORTEL-NMI-INFO-NOTI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nortelNMInotificationGroups, = mibBuilder.importSymbols("NORTEL-NMI-GROUPS-MIB", "nortelNMInotificationGroups")
nortelNMInotifyNeOperState, nortelNMInotifyNeType, nortelNMInotificationsMIB, nortelNMInotifyNeUnknownStatus, nortelNMInotifyNeAdminState, nortelNMInotifyNeName, nortelNMIcurrentTxNotificationSequenceNum = mibBuilder.importSymbols("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeOperState", "nortelNMInotifyNeType", "nortelNMInotificationsMIB", "nortelNMInotifyNeUnknownStatus", "nortelNMInotifyNeAdminState", "nortelNMInotifyNeName", "nortelNMIcurrentTxNotificationSequenceNum")
NortelNMItimeStampDef, = mibBuilder.importSymbols("NORTEL-NMI-TC-MIB", "NortelNMItimeStampDef")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortelNMIinfoNotiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5))
if mibBuilder.loadTexts: nortelNMIinfoNotiMIB.setLastUpdated('9907190000Z')
if mibBuilder.loadTexts: nortelNMIinfoNotiMIB.setOrganization('Nortel Networks')
nortelNMIinfoNotiPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 0))
if mibBuilder.loadTexts: nortelNMIinfoNotiPrefix.setStatus('current')
nortelNMIinfoNotiVarbinds = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1))
if mibBuilder.loadTexts: nortelNMIinfoNotiVarbinds.setStatus('current')
nortelNMInotifyLogComponentId = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyLogComponentId.setStatus('current')
nortelNMInotifyLogText = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyLogText.setStatus('current')
nortelNMInotifyLogTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1, 3), NortelNMItimeStampDef()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nortelNMInotifyLogTimeStamp.setStatus('current')
nortelNMIinfoNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 0, 301)).setObjects(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"), ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMInotifyLogComponentId"), ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMInotifyLogText"), ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMInotifyLogTimeStamp"))
if mibBuilder.loadTexts: nortelNMIinfoNotification.setStatus('current')
nortelNMIneLogNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 5)).setObjects(("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMIinfoNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nortelNMIneLogNotificationsGroup = nortelNMIneLogNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("NORTEL-NMI-INFO-NOTI-MIB", PYSNMP_MODULE_ID=nortelNMIinfoNotiMIB, nortelNMInotifyLogComponentId=nortelNMInotifyLogComponentId, nortelNMInotifyLogTimeStamp=nortelNMInotifyLogTimeStamp, nortelNMIinfoNotification=nortelNMIinfoNotification, nortelNMInotifyLogText=nortelNMInotifyLogText, nortelNMIinfoNotiMIB=nortelNMIinfoNotiMIB, nortelNMIneLogNotificationsGroup=nortelNMIneLogNotificationsGroup, nortelNMIinfoNotiPrefix=nortelNMIinfoNotiPrefix, nortelNMIinfoNotiVarbinds=nortelNMIinfoNotiVarbinds)
