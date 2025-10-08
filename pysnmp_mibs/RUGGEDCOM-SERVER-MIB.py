#
# PySNMP MIB module RUGGEDCOM-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ruggedcomProducts, ruggedcomAgentCapabilities = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomProducts", "ruggedcomAgentCapabilities")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RUGGEDCOM-SERVER-MIB", ruggedcomServerAgents05=ruggedcomServerAgents05, ruggedcomServerAgents03=ruggedcomServerAgents03, PYSNMP_MODULE_ID=ruggedcomServerModule, ruggedcomServerAgents051=ruggedcomServerAgents051, ruggedcomServerAgents04=ruggedcomServerAgents04, ruggedcomServerAgents=ruggedcomServerAgents, ruggedcomServerModule=ruggedcomServerModule)
