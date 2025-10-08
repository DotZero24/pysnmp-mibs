#
# PySNMP MIB module VMWARE-NSX-MANAGER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vmware/VMWARE-NSX-MANAGER-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:23 2025
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
vmwNSXAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 25))
vmwNSXAgentCapabilityMIB.setRevisions(('2020-06-03 00:00', '2016-10-24 00:01', '2016-10-24 00:00', '2016-06-02 00:00',))
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setLastUpdated('202006030000Z')
if mibBuilder.loadTexts: vmwNSXAgentCapabilityMIB.setOrganization('VMware, Inc')
vmwNSXMCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1))
vmwNSXManager2020x647 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2020x647 = vmwNSXManager2020x647.setProductRelease('6.4.7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2020x647 = vmwNSXManager2020x647.setStatus('current')
vmwNSXManager2019x646 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x646 = vmwNSXManager2019x646.setProductRelease('6.4.6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x646 = vmwNSXManager2019x646.setStatus('current')
vmwNSXManager2019x645 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x645 = vmwNSXManager2019x645.setProductRelease('6.4.5')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2019x645 = vmwNSXManager2019x645.setStatus('current')
vmwNSXManager2018x642 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x642 = vmwNSXManager2018x642.setProductRelease('6.4.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x642 = vmwNSXManager2018x642.setStatus('current')
vmwNSXManager2018x637 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x637 = vmwNSXManager2018x637.setProductRelease('6.3.7')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x637 = vmwNSXManager2018x637.setStatus('current')
vmwNSXManager2018x641 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x641 = vmwNSXManager2018x641.setProductRelease('6.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x641 = vmwNSXManager2018x641.setStatus('current')
vmwNSXManager2018x636 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x636 = vmwNSXManager2018x636.setProductRelease('6.3.6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2018x636 = vmwNSXManager2018x636.setStatus('current')
vmwNSXManager2017x640 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x640 = vmwNSXManager2017x640.setProductRelease('6.4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x640 = vmwNSXManager2017x640.setStatus('current')
vmwNSXManager2017x630 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x630 = vmwNSXManager2017x630.setProductRelease('6.3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2017x630 = vmwNSXManager2017x630.setStatus('current')
vmwNSXManager2016x = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 25, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setProductRelease('6.2.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwNSXManager2016x = vmwNSXManager2016x.setStatus('current')
mibBuilder.exportSymbols("VMWARE-NSX-MANAGER-AGENTCAP-MIB", vmwNSXManager2018x642=vmwNSXManager2018x642, vmwNSXManager2017x630=vmwNSXManager2017x630, PYSNMP_MODULE_ID=vmwNSXAgentCapabilityMIB, vmwNSXManager2018x636=vmwNSXManager2018x636, vmwNSXMCapability=vmwNSXMCapability, vmwNSXAgentCapabilityMIB=vmwNSXAgentCapabilityMIB, vmwNSXManager2020x647=vmwNSXManager2020x647, vmwNSXManager2018x641=vmwNSXManager2018x641, vmwNSXManager2016x=vmwNSXManager2016x, vmwNSXManager2019x646=vmwNSXManager2019x646, vmwNSXManager2018x637=vmwNSXManager2018x637, vmwNSXManager2019x645=vmwNSXManager2019x645, vmwNSXManager2017x640=vmwNSXManager2017x640)
