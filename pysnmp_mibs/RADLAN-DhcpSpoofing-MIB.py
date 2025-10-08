#
# PySNMP MIB module RADLAN-DhcpSpoofing-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/RADLAN-DhcpSpoofing-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, dot1qVlanIndex = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qVlanIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlDhcpSpoofing = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 113))
rlDhcpSpoofing.setRevisions(('2006-05-15 00:00',))
if mibBuilder.loadTexts: rlDhcpSpoofing.setLastUpdated('200605150000Z')
if mibBuilder.loadTexts: rlDhcpSpoofing.setOrganization('Radlan Computer Communications Ltd.')
rlDhcpSpoofingServerPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 113, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSpoofingServerPorts.setStatus('current')
rlDhcpSpoofingVlanTable = MibTable((1, 3, 6, 1, 4, 1, 89, 113, 2), )
if mibBuilder.loadTexts: rlDhcpSpoofingVlanTable.setStatus('current')
rlDhcpSpoofingVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 113, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: rlDhcpSpoofingVlanEntry.setStatus('current')
rlDhcpSpoofingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 113, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDhcpSpoofingEnabled.setStatus('current')
mibBuilder.exportSymbols("RADLAN-DhcpSpoofing-MIB", rlDhcpSpoofingServerPorts=rlDhcpSpoofingServerPorts, rlDhcpSpoofingEnabled=rlDhcpSpoofingEnabled, rlDhcpSpoofingVlanEntry=rlDhcpSpoofingVlanEntry, rlDhcpSpoofing=rlDhcpSpoofing, rlDhcpSpoofingVlanTable=rlDhcpSpoofingVlanTable, PYSNMP_MODULE_ID=rlDhcpSpoofing)
