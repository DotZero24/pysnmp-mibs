#
# PySNMP MIB module Dlink-VLAN-TRUNKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/Dlink-VLAN-TRUNKING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlVlanTrunking = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136))
rlVlanTrunking.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlVlanTrunking.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlVlanTrunking.setOrganization('Dlink, Inc.')
rlVlanTrunkingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingEnabled.setStatus('current')
rlVlanTrunkingUplinkPorts = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingUplinkPorts.setStatus('current')
mibBuilder.exportSymbols("Dlink-VLAN-TRUNKING-MIB", PYSNMP_MODULE_ID=rlVlanTrunking, rlVlanTrunkingEnabled=rlVlanTrunkingEnabled, rlVlanTrunking=rlVlanTrunking, rlVlanTrunkingUplinkPorts=rlVlanTrunkingUplinkPorts)
