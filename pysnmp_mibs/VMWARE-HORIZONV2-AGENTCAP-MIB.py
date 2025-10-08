#
# PySNMP MIB module VMWARE-HORIZONV2-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vmware/VMWARE-HORIZONV2-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwHorizonv2AgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 150))
vmwHorizonv2AgentCapabilityMIB.setRevisions(('2023-07-28 00:00',))
if mibBuilder.loadTexts: vmwHorizonv2AgentCapabilityMIB.setLastUpdated('202307280000Z')
if mibBuilder.loadTexts: vmwHorizonv2AgentCapabilityMIB.setOrganization('VMware, Inc')
vmwHorizonv2Capability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 150, 0))
vmwHorizonv2Agent2021v200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 150, 0, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHorizonv2Agent2021v200 = vmwHorizonv2Agent2021v200.setProductRelease('2.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHorizonv2Agent2021v200 = vmwHorizonv2Agent2021v200.setStatus('current')
mibBuilder.exportSymbols("VMWARE-HORIZONV2-AGENTCAP-MIB", vmwHorizonv2AgentCapabilityMIB=vmwHorizonv2AgentCapabilityMIB, PYSNMP_MODULE_ID=vmwHorizonv2AgentCapabilityMIB, vmwHorizonv2Agent2021v200=vmwHorizonv2Agent2021v200, vmwHorizonv2Capability=vmwHorizonv2Capability)
