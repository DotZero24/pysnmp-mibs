#
# PySNMP MIB module RC-RUGGEDCOM-IRIGB-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-IRIGB-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:29 2025
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
ruggedcomRcIrigbACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43))
ruggedcomRcIrigbACModule.setRevisions(('2015-10-30 17:00', '2014-12-05 17:00',))
if mibBuilder.loadTexts: ruggedcomRcIrigbACModule.setLastUpdated('201510301700Z')
if mibBuilder.loadTexts: ruggedcomRcIrigbACModule.setOrganization('Siemens Canada Limited')
ruggedcomRcIrigbAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC = ruggedcomRcIrigbAC.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC = ruggedcomRcIrigbAC.setStatus('current')
ruggedcomRcIrigbAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC01 = ruggedcomRcIrigbAC01.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC01 = ruggedcomRcIrigbAC01.setStatus('current')
ruggedcomRcIrigbAC02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC02 = ruggedcomRcIrigbAC02.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC02 = ruggedcomRcIrigbAC02.setStatus('current')
ruggedcomRcIrigbAC03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC03 = ruggedcomRcIrigbAC03.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC03 = ruggedcomRcIrigbAC03.setStatus('current')
ruggedcomRcIrigbAC04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC04 = ruggedcomRcIrigbAC04.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC04 = ruggedcomRcIrigbAC04.setStatus('current')
ruggedcomRcIrigbAC05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC05 = ruggedcomRcIrigbAC05.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC05 = ruggedcomRcIrigbAC05.setStatus('current')
ruggedcomRcIrigbAC06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC06 = ruggedcomRcIrigbAC06.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcIrigbAC06 = ruggedcomRcIrigbAC06.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-IRIGB-MIB-AC", ruggedcomRcIrigbACModule=ruggedcomRcIrigbACModule, ruggedcomRcIrigbAC01=ruggedcomRcIrigbAC01, ruggedcomRcIrigbAC05=ruggedcomRcIrigbAC05, ruggedcomRcIrigbAC03=ruggedcomRcIrigbAC03, ruggedcomRcIrigbAC04=ruggedcomRcIrigbAC04, ruggedcomRcIrigbAC06=ruggedcomRcIrigbAC06, ruggedcomRcIrigbAC=ruggedcomRcIrigbAC, ruggedcomRcIrigbAC02=ruggedcomRcIrigbAC02, PYSNMP_MODULE_ID=ruggedcomRcIrigbACModule)
