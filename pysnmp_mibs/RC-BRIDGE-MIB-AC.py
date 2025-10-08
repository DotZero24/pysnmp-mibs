#
# PySNMP MIB module RC-BRIDGE-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-BRIDGE-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ruggedcomAgentCapability, = mibBuilder.importSymbols("RUGGEDCOM-MIB", "ruggedcomAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RC-BRIDGE-MIB-AC", ruggedcomBridgeAC01=ruggedcomBridgeAC01, ruggedcomBridgeAC=ruggedcomBridgeAC, PYSNMP_MODULE_ID=ruggedcomBridgeACModule, ruggedcomBridgeACModule=ruggedcomBridgeACModule, ruggedcomBridgeAC02=ruggedcomBridgeAC02)
