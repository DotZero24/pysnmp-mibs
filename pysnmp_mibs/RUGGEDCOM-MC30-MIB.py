#
# PySNMP MIB module RUGGEDCOM-MC30-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-MC30-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ruggedcomAgentCapabilities, ruggedcomProducts = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomAgentCapabilities", "ruggedcomProducts")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ruggedcomMC30Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 2, 3))
ruggedcomMC30Module.setRevisions(('2011-05-01 17:00', '2009-05-15 17:00', '2008-03-07 11:00', '2006-11-02 11:00', '2006-09-09 09:00', '2004-06-28 10:00',))
if mibBuilder.loadTexts: ruggedcomMC30Module.setLastUpdated('201105011700Z')
if mibBuilder.loadTexts: ruggedcomMC30Module.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomMC30Agents = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents = ruggedcomMC30Agents.setProductRelease('Rugged Media Converter RMC30 Agent capabilities version\r\n                     1.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents = ruggedcomMC30Agents.setStatus('obsolete')
ruggedcomMC30Agents03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents03 = ruggedcomMC30Agents03.setProductRelease('Rugged Media Converter RMC30 Agent capabilities version\r\n                     3.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents03 = ruggedcomMC30Agents03.setStatus('obsolete')
ruggedcomMC30Agents04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents04 = ruggedcomMC30Agents04.setProductRelease('Rugged Media Converter RMC30 Agent capabilities version\r\n                     4.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents04 = ruggedcomMC30Agents04.setStatus('obsolete')
ruggedcomMC30Agents041 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents041 = ruggedcomMC30Agents041.setProductRelease('Rugged Media Converter RMC30 Agent capabilities version\r\n                     4.1.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomMC30Agents041 = ruggedcomMC30Agents041.setStatus('obsolete')
mibBuilder.exportSymbols("RUGGEDCOM-MC30-MIB", ruggedcomMC30Module=ruggedcomMC30Module, ruggedcomMC30Agents=ruggedcomMC30Agents, PYSNMP_MODULE_ID=ruggedcomMC30Module, ruggedcomMC30Agents04=ruggedcomMC30Agents04, ruggedcomMC30Agents041=ruggedcomMC30Agents041, ruggedcomMC30Agents03=ruggedcomMC30Agents03)
