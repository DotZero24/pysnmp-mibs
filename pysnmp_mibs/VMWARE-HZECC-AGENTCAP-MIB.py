#
# PySNMP MIB module VMWARE-HZECC-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vmware/VMWARE-HZECC-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:28 2025
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
vmwHzeccAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 140))
vmwHzeccAgentCapabilityMIB.setRevisions(('2021-05-17 00:00',))
if mibBuilder.loadTexts: vmwHzeccAgentCapabilityMIB.setLastUpdated('202105170000Z')
if mibBuilder.loadTexts: vmwHzeccAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwHzeccCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 140, 1))
vmwHZECCAgent2021v200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 140, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHZECCAgent2021v200 = vmwHZECCAgent2021v200.setProductRelease('2.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHZECCAgent2021v200 = vmwHZECCAgent2021v200.setStatus('current')
mibBuilder.exportSymbols("VMWARE-HZECC-AGENTCAP-MIB", PYSNMP_MODULE_ID=vmwHzeccAgentCapabilityMIB, vmwHzeccCapability=vmwHzeccCapability, vmwHzeccAgentCapabilityMIB=vmwHzeccAgentCapabilityMIB, vmwHZECCAgent2021v200=vmwHZECCAgent2021v200)
