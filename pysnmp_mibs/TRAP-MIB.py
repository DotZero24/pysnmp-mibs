#
# PySNMP MIB module TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ctTrapTable, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTrapTable")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1))
trapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1), )
if mibBuilder.loadTexts: trapTable.setStatus('mandatory')
trapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1), ).setIndexNames((0, "TRAP-MIB", "trapIndex"))
if mibBuilder.loadTexts: trapEntry.setStatus('mandatory')
trapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIndex.setStatus('mandatory')
trapCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapCommunityName.setStatus('mandatory')
trapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trapsDisabled", 1), ("trapsEnabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapStatus.setStatus('mandatory')
trapIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapIPAddr.setStatus('mandatory')
trapSrcParty = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSrcParty.setStatus('mandatory')
trapDstParty = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7, 1, 1, 1, 6), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDstParty.setStatus('mandatory')
mibBuilder.exportSymbols("TRAP-MIB", trapIPAddr=trapIPAddr, trap=trap, trapEntry=trapEntry, trapSrcParty=trapSrcParty, trapStatus=trapStatus, trapTable=trapTable, trapDstParty=trapDstParty, trapCommunityName=trapCommunityName, trapIndex=trapIndex)
