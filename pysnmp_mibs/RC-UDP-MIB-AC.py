#
# PySNMP MIB module RC-UDP-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-UDP-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ruggedcomAgentCapability, = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruggedcomUdpACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 6))
ruggedcomUdpACModule.setRevisions(('2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomUdpACModule.setLastUpdated('201102221700Z')
if mibBuilder.loadTexts: ruggedcomUdpACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomUdpAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomUdpAC = ruggedcomUdpAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomUdpAC = ruggedcomUdpAC.setStatus('current')
ruggedcomUdpAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 6, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomUdpAC01 = ruggedcomUdpAC01.setProductRelease('Ruggedcom ROX 2.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomUdpAC01 = ruggedcomUdpAC01.setStatus('current')
mibBuilder.exportSymbols("RC-UDP-MIB-AC", ruggedcomUdpAC01=ruggedcomUdpAC01, PYSNMP_MODULE_ID=ruggedcomUdpACModule, ruggedcomUdpAC=ruggedcomUdpAC, ruggedcomUdpACModule=ruggedcomUdpACModule)
