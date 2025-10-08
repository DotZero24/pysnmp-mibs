#
# PySNMP MIB module Dlink-VLAN-TRUNKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/Dlink-VLAN-TRUNKING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlVlanTrunking = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136))
rlVlanTrunking.setRevisions(('2007-11-18 00:00',))
if mibBuilder.loadTexts: rlVlanTrunking.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlVlanTrunking.setOrganization('Dlink, Inc.')
rlVlanTrunkingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingEnabled.setStatus('current')
rlVlanTrunkingUplinkPorts = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 136, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlVlanTrunkingUplinkPorts.setStatus('current')
mibBuilder.exportSymbols("Dlink-VLAN-TRUNKING-MIB", rlVlanTrunkingUplinkPorts=rlVlanTrunkingUplinkPorts, rlVlanTrunkingEnabled=rlVlanTrunkingEnabled, rlVlanTrunking=rlVlanTrunking, PYSNMP_MODULE_ID=rlVlanTrunking)
