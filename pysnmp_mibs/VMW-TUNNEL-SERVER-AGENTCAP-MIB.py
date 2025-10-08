#
# PySNMP MIB module VMW-TUNNEL-SERVER-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vmware/VMW-TUNNEL-SERVER-AGENTCAP-MIB
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
mibBuilder.exportSymbols("VMW-TUNNEL-SERVER-AGENTCAP-MIB", vmwTunnelServer2022_221200=vmwTunnelServer2022_221200, vmwTunnelServerAgentCapMIB=vmwTunnelServerAgentCapMIB, vmwTunnelServerCapability=vmwTunnelServerCapability, vmwTunnelServer2018_400=vmwTunnelServer2018_400, vmwTunnelServer2019_420=vmwTunnelServer2019_420, PYSNMP_MODULE_ID=vmwTunnelServerAgentCapMIB, vmwTunnelServer2020_200900=vmwTunnelServer2020_200900)
