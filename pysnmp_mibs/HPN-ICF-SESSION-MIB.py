#
# PySNMP MIB module HPN-ICF-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-SESSION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-SESSION-MIB", hpnicfSessionStatSlot=hpnicfSessionStatSlot, hpnicfSessionStatCreateRate=hpnicfSessionStatCreateRate, hpnicfSessionStatCount=hpnicfSessionStatCount, hpnicfSessionStatTable=hpnicfSessionStatTable, hpnicfSessionStatCPUID=hpnicfSessionStatCPUID, PYSNMP_MODULE_ID=hpnicfSession, hpnicfSessionTables=hpnicfSessionTables, hpnicfSessionStatChassis=hpnicfSessionStatChassis, hpnicfSessionStatEntry=hpnicfSessionStatEntry, hpnicfSession=hpnicfSession)
