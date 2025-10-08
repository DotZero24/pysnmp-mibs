#
# PySNMP MIB module SWITCH-L3FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/SWITCH-L3FILTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("SWITCH-L3FILTER-MIB", rcL3Filter=rcL3Filter, rcL3IpSubnetFilter=rcL3IpSubnetFilter, rcL3IpSubnetFilterIPAclNumber=rcL3IpSubnetFilterIPAclNumber, rcL3IpSubnetFilterIfIndex=rcL3IpSubnetFilterIfIndex, rcL3IpSubnetFilterTable=rcL3IpSubnetFilterTable, rcL3IpSubnetFilterStatus=rcL3IpSubnetFilterStatus, rcL3IpSubnetFilterEntry=rcL3IpSubnetFilterEntry, rcL3IpSubnetFilterPorts=rcL3IpSubnetFilterPorts, PYSNMP_MODULE_ID=rcL3Filter)
