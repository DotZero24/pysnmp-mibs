#
# PySNMP MIB module RUGGEDCOM-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RUGGEDCOM-SWITCH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:24 2025
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
mibBuilder.exportSymbols("RUGGEDCOM-SWITCH-MIB", ruggedcomSwitchModule=ruggedcomSwitchModule, ruggedcomSwitchAgents06=ruggedcomSwitchAgents06, ruggedcomSwitchAgents081=ruggedcomSwitchAgents081, ruggedcomSwitchAgents05=ruggedcomSwitchAgents05, ruggedcomSwitchAgents03=ruggedcomSwitchAgents03, ruggedcomSwitchAgents07=ruggedcomSwitchAgents07, ruggedcomSwitchAgents08=ruggedcomSwitchAgents08, ruggedcomSwitchAgents071=ruggedcomSwitchAgents071, ruggedcomSwitchAgents04=ruggedcomSwitchAgents04, ruggedcomSwitchAgents=ruggedcomSwitchAgents, PYSNMP_MODULE_ID=ruggedcomSwitchModule)
