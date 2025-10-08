#
# PySNMP MIB module SWITCH-IFEXTEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/SWITCH-IFEXTEND-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rcIfExtend = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 20))
if mibBuilder.loadTexts: rcIfExtend.setLastUpdated('200502200000Z')
if mibBuilder.loadTexts: rcIfExtend.setOrganization('Raisecom, Inc.')
rcIfExtendMib = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1))
rcIfExtendTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1), )
if mibBuilder.loadTexts: rcIfExtendTable.setStatus('current')
rcIfExtendEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1, 1), ).setIndexNames((0, "SWITCH-IFEXTEND-MIB", "rcIfindex"))
if mibBuilder.loadTexts: rcIfExtendEntry.setStatus('current')
rcIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rcIfindex.setStatus('current')
rcIfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 20, 1, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcIfDescription.setStatus('current')
mibBuilder.exportSymbols("SWITCH-IFEXTEND-MIB", rcIfExtendEntry=rcIfExtendEntry, rcIfExtendTable=rcIfExtendTable, PYSNMP_MODULE_ID=rcIfExtend, rcIfindex=rcIfindex, rcIfExtendMib=rcIfExtendMib, rcIfDescription=rcIfDescription, rcIfExtend=rcIfExtend)
