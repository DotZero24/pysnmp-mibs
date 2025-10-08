#
# PySNMP MIB module VMW-TUNNEL-SERVER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/vmware/VMW-TUNNEL-SERVER-AGENTCAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:31 2025
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
vmwTunnelServerAgentCapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 70, 28))
vmwTunnelServerAgentCapMIB.setRevisions(('2022-10-28 00:00', '2020-07-21 00:00', '2019-10-30 00:00', '2018-09-04 00:00',))
if mibBuilder.loadTexts: vmwTunnelServerAgentCapMIB.setLastUpdated('202210280000Z')
if mibBuilder.loadTexts: vmwTunnelServerAgentCapMIB.setOrganization('VMware, Inc.')
vmwTunnelServerCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 70, 28, 1))
vmwTunnelServer2022_221200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 4)).setLabel("vmwTunnelServer2022-221200")
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2022_221200 = vmwTunnelServer2022_221200.setProductRelease('22.12.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2022_221200 = vmwTunnelServer2022_221200.setStatus('current')
vmwTunnelServer2020_200900 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 3)).setLabel("vmwTunnelServer2020-200900")
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2020_200900 = vmwTunnelServer2020_200900.setProductRelease('20.09.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2020_200900 = vmwTunnelServer2020_200900.setStatus('current')
vmwTunnelServer2019_420 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 2)).setLabel("vmwTunnelServer2019-420")
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2019_420 = vmwTunnelServer2019_420.setProductRelease('4.2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2019_420 = vmwTunnelServer2019_420.setStatus('current')
vmwTunnelServer2018_400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 6876, 70, 28, 1, 1)).setLabel("vmwTunnelServer2018-400")
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2018_400 = vmwTunnelServer2018_400.setProductRelease('4.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwTunnelServer2018_400 = vmwTunnelServer2018_400.setStatus('current')
mibBuilder.exportSymbols("VMW-TUNNEL-SERVER-AGENTCAP-MIB", vmwTunnelServer2020_200900=vmwTunnelServer2020_200900, vmwTunnelServer2019_420=vmwTunnelServer2019_420, vmwTunnelServerCapability=vmwTunnelServerCapability, vmwTunnelServerAgentCapMIB=vmwTunnelServerAgentCapMIB, vmwTunnelServer2022_221200=vmwTunnelServer2022_221200, PYSNMP_MODULE_ID=vmwTunnelServerAgentCapMIB, vmwTunnelServer2018_400=vmwTunnelServer2018_400)
