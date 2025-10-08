#
# PySNMP MIB module RC-RUGGEDCOM-SYS-INFO-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-SYS-INFO-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:57 2025
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
ruggedcomRcSysinfoACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12))
ruggedcomRcSysinfoACModule.setRevisions(('2017-11-02 11:00', '2017-02-15 10:00', '2013-11-13 17:00', '2012-08-30 17:00', '2012-06-01 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomRcSysinfoACModule.setLastUpdated('201711021100Z')
if mibBuilder.loadTexts: ruggedcomRcSysinfoACModule.setOrganization('Siemens Canada Ltd., Process Industries and Drives')
ruggedcomRcSysinfoAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC = ruggedcomRcSysinfoAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC = ruggedcomRcSysinfoAC.setStatus('obsolete')
ruggedcomRcSysinfoAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC01 = ruggedcomRcSysinfoAC01.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC01 = ruggedcomRcSysinfoAC01.setStatus('obsolete')
ruggedcomRcSysinfoAC02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC02 = ruggedcomRcSysinfoAC02.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC02 = ruggedcomRcSysinfoAC02.setStatus('obsolete')
ruggedcomRcSysinfoAC03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC03 = ruggedcomRcSysinfoAC03.setProductRelease('Ruggedcom ROX 2.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC03 = ruggedcomRcSysinfoAC03.setStatus('current')
ruggedcomRcSysinfoAC04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC04 = ruggedcomRcSysinfoAC04.setProductRelease('Ruggedcom ROX II')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC04 = ruggedcomRcSysinfoAC04.setStatus('current')
ruggedcomRcSysinfoAC05 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC05 = ruggedcomRcSysinfoAC05.setProductRelease('ROS-CF52 and ROS-MPC83')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSysinfoAC05 = ruggedcomRcSysinfoAC05.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-SYS-INFO-MIB-AC", ruggedcomRcSysinfoACModule=ruggedcomRcSysinfoACModule, ruggedcomRcSysinfoAC05=ruggedcomRcSysinfoAC05, PYSNMP_MODULE_ID=ruggedcomRcSysinfoACModule, ruggedcomRcSysinfoAC=ruggedcomRcSysinfoAC, ruggedcomRcSysinfoAC03=ruggedcomRcSysinfoAC03, ruggedcomRcSysinfoAC04=ruggedcomRcSysinfoAC04, ruggedcomRcSysinfoAC02=ruggedcomRcSysinfoAC02, ruggedcomRcSysinfoAC01=ruggedcomRcSysinfoAC01)
