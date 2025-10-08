#
# PySNMP MIB module HPN-ICF-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-SESSION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfSession = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149))
hpnicfSession.setRevisions(('2013-12-20 00:00',))
if mibBuilder.loadTexts: hpnicfSession.setLastUpdated('201312200000Z')
if mibBuilder.loadTexts: hpnicfSession.setOrganization('')
hpnicfSessionTables = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1))
hpnicfSessionStatTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1), )
if mibBuilder.loadTexts: hpnicfSessionStatTable.setStatus('current')
hpnicfSessionStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatChassis"), (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatSlot"), (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatCPUID"))
if mibBuilder.loadTexts: hpnicfSessionStatEntry.setStatus('current')
hpnicfSessionStatChassis = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hpnicfSessionStatChassis.setStatus('current')
hpnicfSessionStatSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65534)))
if mibBuilder.loadTexts: hpnicfSessionStatSlot.setStatus('current')
hpnicfSessionStatCPUID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: hpnicfSessionStatCPUID.setStatus('current')
hpnicfSessionStatCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSessionStatCount.setStatus('current')
hpnicfSessionStatCreateRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSessionStatCreateRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-SESSION-MIB", hpnicfSessionStatCount=hpnicfSessionStatCount, hpnicfSessionStatEntry=hpnicfSessionStatEntry, hpnicfSessionStatCPUID=hpnicfSessionStatCPUID, hpnicfSessionStatCreateRate=hpnicfSessionStatCreateRate, hpnicfSessionStatSlot=hpnicfSessionStatSlot, hpnicfSessionStatTable=hpnicfSessionStatTable, PYSNMP_MODULE_ID=hpnicfSession, hpnicfSession=hpnicfSession, hpnicfSessionStatChassis=hpnicfSessionStatChassis, hpnicfSessionTables=hpnicfSessionTables)
