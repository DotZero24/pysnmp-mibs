#
# PySNMP MIB module NORTEL-NMI-INFO-NOTI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NORTEL-NMI-INFO-NOTI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nortelNMInotificationGroups, = mibBuilder.importSymbols("NORTEL-NMI-GROUPS-MIB", "nortelNMInotificationGroups")
nortelNMInotifyNeType, nortelNMInotifyNeAdminState, nortelNMInotificationsMIB, nortelNMInotifyNeOperState, nortelNMInotifyNeName, nortelNMIcurrentTxNotificationSequenceNum, nortelNMInotifyNeUnknownStatus = mibBuilder.importSymbols("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeType", "nortelNMInotifyNeAdminState", "nortelNMInotificationsMIB", "nortelNMInotifyNeOperState", "nortelNMInotifyNeName", "nortelNMIcurrentTxNotificationSequenceNum", "nortelNMInotifyNeUnknownStatus")
NortelNMItimeStampDef, = mibBuilder.importSymbols("NORTEL-NMI-TC-MIB", "NortelNMItimeStampDef")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NORTEL-NMI-INFO-NOTI-MIB", PYSNMP_MODULE_ID=nortelNMIinfoNotiMIB, nortelNMIinfoNotiPrefix=nortelNMIinfoNotiPrefix, nortelNMIinfoNotification=nortelNMIinfoNotification, nortelNMIinfoNotiVarbinds=nortelNMIinfoNotiVarbinds, nortelNMInotifyLogComponentId=nortelNMInotifyLogComponentId, nortelNMInotifyLogText=nortelNMInotifyLogText, nortelNMInotifyLogTimeStamp=nortelNMInotifyLogTimeStamp, nortelNMIneLogNotificationsGroup=nortelNMIneLogNotificationsGroup, nortelNMIinfoNotiMIB=nortelNMIinfoNotiMIB)
