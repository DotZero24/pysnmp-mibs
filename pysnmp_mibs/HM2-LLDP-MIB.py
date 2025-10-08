#
# PySNMP MIB module HM2-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-LLDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2ConfigurationMibs, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs", "HmEnabledStatus")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HM2-LLDP-MIB", PYSNMP_MODULE_ID=hm2LLDPMib, hm2LLDPAdminStatus=hm2LLDPAdminStatus, hm2LLDPIfTable=hm2LLDPIfTable, hm2LLDPIfMaxNeighbors=hm2LLDPIfMaxNeighbors, hm2LLDPMib=hm2LLDPMib, hm2LLDPIfFDBMode=hm2LLDPIfFDBMode, hm2LLDPIfEntry=hm2LLDPIfEntry, hm2LLDPConfigGroup=hm2LLDPConfigGroup, hm2LLDPMibObjects=hm2LLDPMibObjects)
