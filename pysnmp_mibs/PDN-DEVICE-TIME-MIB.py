#
# PySNMP MIB module PDN-DEVICE-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-DEVICE-TIME-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pdn_time, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-time")
NTPMode, = mibBuilder.importSymbols("PDN-TC", "NTPMode")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
devTimeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1))
devTimeMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 2))
devTimeAndDate = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 1))
devNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2))
devDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 1, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDateAndTime.setStatus('mandatory')
devNTPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPServerIP.setStatus('mandatory')
devNTPMode = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 2), NTPMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPMode.setStatus('mandatory')
devNTPSynchronised = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPSynchronised.setStatus('mandatory')
devNTPEnable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPEnable.setStatus('mandatory')
devNTPOffsetFromUTC = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devNTPOffsetFromUTC.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-DEVICE-TIME-MIB", devNTPSynchronised=devNTPSynchronised, devTimeMIBTraps=devTimeMIBTraps, devNTPEnable=devNTPEnable, devNTPMode=devNTPMode, devNTPServerIP=devNTPServerIP, devDateAndTime=devDateAndTime, devNTP=devNTP, devTimeAndDate=devTimeAndDate, devTimeMIBObjects=devTimeMIBObjects, devNTPOffsetFromUTC=devNTPOffsetFromUTC)
