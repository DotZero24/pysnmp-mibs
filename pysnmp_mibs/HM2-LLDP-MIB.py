#
# PySNMP MIB module HM2-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HM2-LLDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
HmEnabledStatus, hm2ConfigurationMibs = mibBuilder.importSymbols("HM2-TC-MIB", "HmEnabledStatus", "hm2ConfigurationMibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2LLDPMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 34))
hm2LLDPMib.setRevisions(('2011-04-11 00:00',))
if mibBuilder.loadTexts: hm2LLDPMib.setLastUpdated('201104110000Z')
if mibBuilder.loadTexts: hm2LLDPMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2LLDPMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 34, 1))
hm2LLDPConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1))
hm2LLDPAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 1), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LLDPAdminStatus.setStatus('current')
hm2LLDPIfTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2), )
if mibBuilder.loadTexts: hm2LLDPIfTable.setStatus('current')
hm2LLDPIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hm2LLDPIfEntry.setStatus('current')
hm2LLDPIfMaxNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LLDPIfMaxNeighbors.setStatus('current')
hm2LLDPIfFDBMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("lldpOnly", 1), ("macOnly", 2), ("both", 3), ("autoDetect", 4))).clone('autoDetect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2LLDPIfFDBMode.setStatus('current')
mibBuilder.exportSymbols("HM2-LLDP-MIB", hm2LLDPMib=hm2LLDPMib, PYSNMP_MODULE_ID=hm2LLDPMib, hm2LLDPAdminStatus=hm2LLDPAdminStatus, hm2LLDPIfEntry=hm2LLDPIfEntry, hm2LLDPIfTable=hm2LLDPIfTable, hm2LLDPMibObjects=hm2LLDPMibObjects, hm2LLDPIfMaxNeighbors=hm2LLDPIfMaxNeighbors, hm2LLDPConfigGroup=hm2LLDPConfigGroup, hm2LLDPIfFDBMode=hm2LLDPIfFDBMode)
