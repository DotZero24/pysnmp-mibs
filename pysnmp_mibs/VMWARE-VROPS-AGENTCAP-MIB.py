#
# PySNMP MIB module VMWARE-VROPS-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/vmware/VMWARE-VROPS-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwareAgentCapabilities, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwareAgentCapabilities")
vmwVropsAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 27))
vmwVropsAgentCapabilityMIB.setRevisions(('2018-06-27 00:00',))
if mibBuilder.loadTexts: vmwVropsAgentCapabilityMIB.setLastUpdated('201806270000Z')
if mibBuilder.loadTexts: vmwVropsAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwVropsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 27, 1))
vmwVrops2018_70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 27, 1, 1)).setLabel("vmwVrops2018-70")
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVrops2018_70 = vmwVrops2018_70.setProductRelease('7.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVrops2018_70 = vmwVrops2018_70.setStatus('current')
mibBuilder.exportSymbols("VMWARE-VROPS-AGENTCAP-MIB", vmwVropsAgentCapabilityMIB=vmwVropsAgentCapabilityMIB, PYSNMP_MODULE_ID=vmwVropsAgentCapabilityMIB, vmwVrops2018_70=vmwVrops2018_70, vmwVropsCapability=vmwVropsCapability)
