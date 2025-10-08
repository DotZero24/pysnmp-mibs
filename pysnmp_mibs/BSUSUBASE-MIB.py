#
# PySNMP MIB module BSUSUBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/BSUSUBASE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aniBsuSuGroup, = mibBuilder.importSymbols("ANIROOT-MIB", "aniBsuSuGroup")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
aniBsuSuMacAddr, = mibBuilder.importSymbols("BSUSUINV-MIB", "aniBsuSuMacAddr")
aniBsuWirelessPort, = mibBuilder.importSymbols("BSUWIRELESSIF-MIB", "aniBsuWirelessPort")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuSuBase = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2))
if mibBuilder.loadTexts: aniBsuSuBase.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniBsuSuBase.setOrganization('Aperto Networks')
aniBsuSuBaseTable = MibTable((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1), )
if mibBuilder.loadTexts: aniBsuSuBaseTable.setStatus('current')
aniBsuSuBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1), ).setIndexNames((0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"), (0, "BSUSUINV-MIB", "aniBsuSuMacAddr"))
if mibBuilder.loadTexts: aniBsuSuBaseEntry.setStatus('current')
aniBsuSuNetworkAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuNetworkAccess.setStatus('current')
aniBsuSuMaxHostSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuMaxHostSupport.setStatus('current')
aniBsuSuTargetFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuTargetFreq.setStatus('current')
aniBsuSuFrequencyTable = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 7, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuSuFrequencyTable.setStatus('current')
mibBuilder.exportSymbols("BSUSUBASE-MIB", aniBsuSuBaseEntry=aniBsuSuBaseEntry, PYSNMP_MODULE_ID=aniBsuSuBase, aniBsuSuNetworkAccess=aniBsuSuNetworkAccess, aniBsuSuBaseTable=aniBsuSuBaseTable, aniBsuSuMaxHostSupport=aniBsuSuMaxHostSupport, aniBsuSuTargetFreq=aniBsuSuTargetFreq, aniBsuSuBase=aniBsuSuBase, aniBsuSuFrequencyTable=aniBsuSuFrequencyTable)
