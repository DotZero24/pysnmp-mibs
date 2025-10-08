#
# PySNMP MIB module TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ctTrapTable, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTrapTable")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TRAP-MIB", trapStatus=trapStatus, trapTable=trapTable, trapIndex=trapIndex, trapEntry=trapEntry, trapSrcParty=trapSrcParty, trapCommunityName=trapCommunityName, trapIPAddr=trapIPAddr, trapDstParty=trapDstParty, trap=trap)
