#
# PySNMP MIB module SWITCH-L3FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/SWITCH-L3FILTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
PortList, = mibBuilder.importSymbols("SWITCH-TC", "PortList")
rcL3Filter = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15))
if mibBuilder.loadTexts: rcL3Filter.setLastUpdated('200504120000Z')
if mibBuilder.loadTexts: rcL3Filter.setOrganization('Raisecom, Inc.')
rcL3IpSubnetFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1))
rcL3IpSubnetFilterTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1), )
if mibBuilder.loadTexts: rcL3IpSubnetFilterTable.setStatus('current')
rcL3IpSubnetFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1), ).setIndexNames((0, "SWITCH-L3FILTER-MIB", "rcL3IpSubnetFilterIfIndex"), (0, "SWITCH-L3FILTER-MIB", "rcL3IpSubnetFilterIPAclNumber"))
if mibBuilder.loadTexts: rcL3IpSubnetFilterEntry.setStatus('current')
rcL3IpSubnetFilterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rcL3IpSubnetFilterIfIndex.setStatus('current')
rcL3IpSubnetFilterIPAclNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: rcL3IpSubnetFilterIPAclNumber.setStatus('current')
rcL3IpSubnetFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcL3IpSubnetFilterStatus.setStatus('current')
rcL3IpSubnetFilterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 15, 1, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rcL3IpSubnetFilterPorts.setStatus('current')
mibBuilder.exportSymbols("SWITCH-L3FILTER-MIB", rcL3IpSubnetFilterIPAclNumber=rcL3IpSubnetFilterIPAclNumber, PYSNMP_MODULE_ID=rcL3Filter, rcL3IpSubnetFilterStatus=rcL3IpSubnetFilterStatus, rcL3IpSubnetFilterIfIndex=rcL3IpSubnetFilterIfIndex, rcL3IpSubnetFilterEntry=rcL3IpSubnetFilterEntry, rcL3Filter=rcL3Filter, rcL3IpSubnetFilterPorts=rcL3IpSubnetFilterPorts, rcL3IpSubnetFilter=rcL3IpSubnetFilter, rcL3IpSubnetFilterTable=rcL3IpSubnetFilterTable)
