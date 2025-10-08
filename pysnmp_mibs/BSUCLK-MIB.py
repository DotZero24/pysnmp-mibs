#
# PySNMP MIB module BSUCLK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/BSUCLK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BSUCLK-MIB", aniBsuClkSntpTimeZone=aniBsuClkSntpTimeZone, aniBsuClkManualTime=aniBsuClkManualTime, aniBsuClkCurrentTime=aniBsuClkCurrentTime, aniBsuClock=aniBsuClock, aniBsuClkSntpEnable=aniBsuClkSntpEnable, aniBsuClkSntpDstStart=aniBsuClkSntpDstStart, aniBsuClkSntpDstEnable=aniBsuClkSntpDstEnable, aniBsuClkSntpDstEnd=aniBsuClkSntpDstEnd, PYSNMP_MODULE_ID=aniBsuClock)
