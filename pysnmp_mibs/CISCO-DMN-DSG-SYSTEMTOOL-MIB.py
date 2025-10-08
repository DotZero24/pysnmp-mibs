#
# PySNMP MIB module CISCO-DMN-DSG-SYSTEMTOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-SYSTEMTOOL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-DMN-DSG-SYSTEMTOOL-MIB", systemToolBanner=systemToolBanner, systemToolCleanUnusedTables=systemToolCleanUnusedTables, systemToolFactoryReset=systemToolFactoryReset, systemToolCAMode=systemToolCAMode, systemToolReboot=systemToolReboot, systemTool=systemTool, ciscoDSGSystemTool=ciscoDSGSystemTool, PYSNMP_MODULE_ID=ciscoDSGSystemTool, systemToolClearLogs=systemToolClearLogs)
