#
# PySNMP MIB module RADLAN-DhcpSpoofing-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/RADLAN-DhcpSpoofing-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PortList, dot1qVlanIndex = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qVlanIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("RADLAN-DhcpSpoofing-MIB", rlDhcpSpoofing=rlDhcpSpoofing, PYSNMP_MODULE_ID=rlDhcpSpoofing, rlDhcpSpoofingEnabled=rlDhcpSpoofingEnabled, rlDhcpSpoofingVlanTable=rlDhcpSpoofingVlanTable, rlDhcpSpoofingVlanEntry=rlDhcpSpoofingVlanEntry, rlDhcpSpoofingServerPorts=rlDhcpSpoofingServerPorts)
