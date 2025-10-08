#
# PySNMP MIB module RUGGEDCOM-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-SWITCH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:58 2025
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
ruggedcomSwitchModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 2, 1))
ruggedcomSwitchModule.setRevisions(('2011-05-01 17:00', '2009-05-15 17:00', '2008-11-11 13:00', '2008-09-08 15:00', '2008-03-07 11:00', '2006-11-02 11:00', '2006-09-09 09:00', '2003-07-22 14:00',))
if mibBuilder.loadTexts: ruggedcomSwitchModule.setLastUpdated('201105011700Z')
if mibBuilder.loadTexts: ruggedcomSwitchModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomSwitchAgents = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents = ruggedcomSwitchAgents.setProductRelease('Rugged Switch Agent capabilities version 1.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents = ruggedcomSwitchAgents.setStatus('obsolete')
ruggedcomSwitchAgents03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents03 = ruggedcomSwitchAgents03.setProductRelease('Rugged Switch Agent capabilities version 3.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents03 = ruggedcomSwitchAgents03.setStatus('obsolete')
ruggedcomSwitchAgents04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents04 = ruggedcomSwitchAgents04.setProductRelease('Rugged Switch Agent capabilities version 4.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents04 = ruggedcomSwitchAgents04.setStatus('obsolete')
ruggedcomSwitchAgents05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents05 = ruggedcomSwitchAgents05.setProductRelease('Rugged Switch Agent capabilities version 4.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents05 = ruggedcomSwitchAgents05.setStatus('obsolete')
ruggedcomSwitchAgents06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents06 = ruggedcomSwitchAgents06.setProductRelease('Rugged Switch Agent capabilities version 5.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents06 = ruggedcomSwitchAgents06.setStatus('obsolete')
ruggedcomSwitchAgents07 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents07 = ruggedcomSwitchAgents07.setProductRelease('Rugged Switch Agent capabilities version 6.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents07 = ruggedcomSwitchAgents07.setStatus('obsolete')
ruggedcomSwitchAgents071 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 13, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents071 = ruggedcomSwitchAgents071.setProductRelease('Rugged Switch Agent capabilities version 6.1.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents071 = ruggedcomSwitchAgents071.setStatus('obsolete')
ruggedcomSwitchAgents08 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents08 = ruggedcomSwitchAgents08.setProductRelease('Rugged Switch Agent capabilities version 7.0.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents08 = ruggedcomSwitchAgents08.setStatus('obsolete')
ruggedcomSwitchAgents081 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents081 = ruggedcomSwitchAgents081.setProductRelease('Rugged Switch Agent capabilities version 7.1.0. ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomSwitchAgents081 = ruggedcomSwitchAgents081.setStatus('obsolete')
mibBuilder.exportSymbols("RUGGEDCOM-SWITCH-MIB", ruggedcomSwitchAgents06=ruggedcomSwitchAgents06, ruggedcomSwitchAgents03=ruggedcomSwitchAgents03, ruggedcomSwitchAgents=ruggedcomSwitchAgents, ruggedcomSwitchAgents04=ruggedcomSwitchAgents04, ruggedcomSwitchAgents071=ruggedcomSwitchAgents071, ruggedcomSwitchModule=ruggedcomSwitchModule, ruggedcomSwitchAgents07=ruggedcomSwitchAgents07, ruggedcomSwitchAgents08=ruggedcomSwitchAgents08, PYSNMP_MODULE_ID=ruggedcomSwitchModule, ruggedcomSwitchAgents081=ruggedcomSwitchAgents081, ruggedcomSwitchAgents05=ruggedcomSwitchAgents05)
