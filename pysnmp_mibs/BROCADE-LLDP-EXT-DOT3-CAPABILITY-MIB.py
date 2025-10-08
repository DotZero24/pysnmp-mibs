#
# PySNMP MIB module BROCADE-LLDP-EXT-DOT3-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-LLDP-EXT-DOT3-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
brocadeAgentCapability, = mibBuilder.importSymbols("Brocade-REG-MIB", "brocadeAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brocadeLLDP_EXT_DOT3Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 2, 2)).setLabel("brocadeLLDP-EXT-DOT3Capability")
brocadeLLDP_EXT_DOT3Capability.setRevisions(('2012-06-06 00:00',))
if mibBuilder.loadTexts: brocadeLLDP_EXT_DOT3Capability.setLastUpdated('201206060000Z')
if mibBuilder.loadTexts: brocadeLLDP_EXT_DOT3Capability.setOrganization('Brocade Communications Systems, Inc.,')
brocadeLLDP_EXT_DOT3Vdx300R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 1588, 3, 2, 2, 1)).setLabel("brocadeLLDP-EXT-DOT3Vdx300R1")
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeLLDP_EXT_DOT3Vdx300R1 = brocadeLLDP_EXT_DOT3Vdx300R1.setProductRelease('NOS3.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeLLDP_EXT_DOT3Vdx300R1 = brocadeLLDP_EXT_DOT3Vdx300R1.setStatus('current')
mibBuilder.exportSymbols("BROCADE-LLDP-EXT-DOT3-CAPABILITY-MIB", PYSNMP_MODULE_ID=brocadeLLDP_EXT_DOT3Capability, brocadeLLDP_EXT_DOT3Vdx300R1=brocadeLLDP_EXT_DOT3Vdx300R1, brocadeLLDP_EXT_DOT3Capability=brocadeLLDP_EXT_DOT3Capability)
