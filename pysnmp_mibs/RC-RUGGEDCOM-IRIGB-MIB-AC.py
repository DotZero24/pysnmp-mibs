#
# PySNMP MIB module RC-RUGGEDCOM-IRIGB-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-IRIGB-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:00 2025
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
mibBuilder.exportSymbols("RC-RUGGEDCOM-IRIGB-MIB-AC", ruggedcomRcIrigbAC04=ruggedcomRcIrigbAC04, ruggedcomRcIrigbAC=ruggedcomRcIrigbAC, PYSNMP_MODULE_ID=ruggedcomRcIrigbACModule, ruggedcomRcIrigbACModule=ruggedcomRcIrigbACModule, ruggedcomRcIrigbAC03=ruggedcomRcIrigbAC03, ruggedcomRcIrigbAC06=ruggedcomRcIrigbAC06, ruggedcomRcIrigbAC02=ruggedcomRcIrigbAC02, ruggedcomRcIrigbAC01=ruggedcomRcIrigbAC01, ruggedcomRcIrigbAC05=ruggedcomRcIrigbAC05)
