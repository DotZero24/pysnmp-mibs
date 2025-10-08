#
# PySNMP MIB module RUGGEDCOM-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ruggedcomAgentCapabilities, ruggedcomProducts = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomAgentCapabilities", "ruggedcomProducts")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ruggedcomServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 2, 2))
ruggedcomServerModule.setRevisions(('2011-05-01 17:00', '2009-05-15 17:00', '2008-12-17 13:00', '2008-11-11 13:00', '2008-09-08 15:00', '2008-03-07 11:00', '2006-11-02 11:00', '2006-09-06 16:30', '2004-06-28 10:00',))
if mibBuilder.loadTexts: ruggedcomServerModule.setLastUpdated('201105011700Z')
if mibBuilder.loadTexts: ruggedcomServerModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomServerAgents = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents = ruggedcomServerAgents.setProductRelease('Rugged Server Agent capabilities version 2.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents = ruggedcomServerAgents.setStatus('obsolete')
ruggedcomServerAgents03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents03 = ruggedcomServerAgents03.setProductRelease('Rugged Server Agent capabilities version 3.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents03 = ruggedcomServerAgents03.setStatus('obsolete')
ruggedcomServerAgents04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents04 = ruggedcomServerAgents04.setProductRelease('Rugged Server Agent capabilities version 4.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents04 = ruggedcomServerAgents04.setStatus('obsolete')
ruggedcomServerAgents05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents05 = ruggedcomServerAgents05.setProductRelease('Rugged Server Agent capabilities version 5.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents05 = ruggedcomServerAgents05.setStatus('obsolete')
ruggedcomServerAgents051 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents051 = ruggedcomServerAgents051.setProductRelease('Rugged Server Agent capabilities version 5.1.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomServerAgents051 = ruggedcomServerAgents051.setStatus('obsolete')
mibBuilder.exportSymbols("RUGGEDCOM-SERVER-MIB", ruggedcomServerAgents051=ruggedcomServerAgents051, ruggedcomServerModule=ruggedcomServerModule, PYSNMP_MODULE_ID=ruggedcomServerModule, ruggedcomServerAgents04=ruggedcomServerAgents04, ruggedcomServerAgents05=ruggedcomServerAgents05, ruggedcomServerAgents=ruggedcomServerAgents, ruggedcomServerAgents03=ruggedcomServerAgents03)
