#
# PySNMP MIB module PDN-DEVICE-TIME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/paradyne/PDN-DEVICE-TIME-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdn_time, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-time")
NTPMode, = mibBuilder.importSymbols("PDN-TC", "NTPMode")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PDN-DEVICE-TIME-MIB", devNTPOffsetFromUTC=devNTPOffsetFromUTC, devNTPEnable=devNTPEnable, devDateAndTime=devDateAndTime, devTimeMIBObjects=devTimeMIBObjects, devTimeMIBTraps=devTimeMIBTraps, devNTPServerIP=devNTPServerIP, devNTPMode=devNTPMode, devTimeAndDate=devTimeAndDate, devNTP=devNTP, devNTPSynchronised=devNTPSynchronised)
