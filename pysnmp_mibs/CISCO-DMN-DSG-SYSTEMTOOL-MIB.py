#
# PySNMP MIB module CISCO-DMN-DSG-SYSTEMTOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-SYSTEMTOOL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGSystemTool = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8))
ciscoDSGSystemTool.setRevisions(('2010-08-03 09:00', '2009-12-20 15:00',))
if mibBuilder.loadTexts: ciscoDSGSystemTool.setLastUpdated('201008030900Z')
if mibBuilder.loadTexts: ciscoDSGSystemTool.setOrganization('Cisco Systems, Inc.')
systemTool = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1))
systemToolBanner = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolBanner.setStatus('current')
systemToolReboot = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolReboot.setStatus('current')
systemToolFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolFactoryReset.setStatus('current')
systemToolCleanUnusedTables = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolCleanUnusedTables.setStatus('current')
systemToolCAMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("open", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolCAMode.setStatus('current')
systemToolClearLogs = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolClearLogs.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SYSTEMTOOL-MIB", systemToolBanner=systemToolBanner, systemToolFactoryReset=systemToolFactoryReset, systemToolCleanUnusedTables=systemToolCleanUnusedTables, systemTool=systemTool, systemToolReboot=systemToolReboot, ciscoDSGSystemTool=ciscoDSGSystemTool, systemToolCAMode=systemToolCAMode, PYSNMP_MODULE_ID=ciscoDSGSystemTool, systemToolClearLogs=systemToolClearLogs)
