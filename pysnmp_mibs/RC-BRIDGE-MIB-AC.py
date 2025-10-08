#
# PySNMP MIB module RC-BRIDGE-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-BRIDGE-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:59 2025
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
ruggedcomBridgeACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 3))
ruggedcomBridgeACModule.setRevisions(('2014-02-22 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomBridgeACModule.setLastUpdated('201102221700Z')
if mibBuilder.loadTexts: ruggedcomBridgeACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomBridgeAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomBridgeAC = ruggedcomBridgeAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomBridgeAC = ruggedcomBridgeAC.setStatus('current')
ruggedcomBridgeAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomBridgeAC01 = ruggedcomBridgeAC01.setProductRelease('Ruggedcom ROX 2.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomBridgeAC01 = ruggedcomBridgeAC01.setStatus('current')
ruggedcomBridgeAC02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomBridgeAC02 = ruggedcomBridgeAC02.setProductRelease('ROS-MB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomBridgeAC02 = ruggedcomBridgeAC02.setStatus('current')
mibBuilder.exportSymbols("RC-BRIDGE-MIB-AC", ruggedcomBridgeACModule=ruggedcomBridgeACModule, PYSNMP_MODULE_ID=ruggedcomBridgeACModule, ruggedcomBridgeAC=ruggedcomBridgeAC, ruggedcomBridgeAC01=ruggedcomBridgeAC01, ruggedcomBridgeAC02=ruggedcomBridgeAC02)
