#
# PySNMP MIB module BSUCLK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/BSUCLK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniBsuClock = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 4))
if mibBuilder.loadTexts: aniBsuClock.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniBsuClock.setOrganization('Aperto Networks')
aniBsuClkSntpTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuClkSntpTimeZone.setStatus('current')
aniBsuClkSntpDstEnable = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuClkSntpDstEnable.setStatus('current')
aniBsuClkSntpDstStart = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuClkSntpDstStart.setStatus('current')
aniBsuClkSntpDstEnd = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuClkSntpDstEnd.setStatus('current')
aniBsuClkSntpEnable = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuClkSntpEnable.setStatus('current')
aniBsuClkManualTime = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniBsuClkManualTime.setStatus('current')
aniBsuClkCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 4, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuClkCurrentTime.setStatus('current')
mibBuilder.exportSymbols("BSUCLK-MIB", PYSNMP_MODULE_ID=aniBsuClock, aniBsuClkManualTime=aniBsuClkManualTime, aniBsuClkCurrentTime=aniBsuClkCurrentTime, aniBsuClock=aniBsuClock, aniBsuClkSntpDstEnd=aniBsuClkSntpDstEnd, aniBsuClkSntpDstStart=aniBsuClkSntpDstStart, aniBsuClkSntpDstEnable=aniBsuClkSntpDstEnable, aniBsuClkSntpEnable=aniBsuClkSntpEnable, aniBsuClkSntpTimeZone=aniBsuClkSntpTimeZone)
