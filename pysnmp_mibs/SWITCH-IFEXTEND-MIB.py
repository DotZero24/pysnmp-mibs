#
# PySNMP MIB module SWITCH-IFEXTEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/SWITCH-IFEXTEND-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SWITCH-IFEXTEND-MIB", rcIfDescription=rcIfDescription, rcIfindex=rcIfindex, rcIfExtendEntry=rcIfExtendEntry, rcIfExtendMib=rcIfExtendMib, rcIfExtend=rcIfExtend, rcIfExtendTable=rcIfExtendTable, PYSNMP_MODULE_ID=rcIfExtend)
