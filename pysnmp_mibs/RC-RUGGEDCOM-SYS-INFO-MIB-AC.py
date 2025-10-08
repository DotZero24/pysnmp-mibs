#
# PySNMP MIB module RC-RUGGEDCOM-SYS-INFO-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-SYS-INFO-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:22 2025
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
mibBuilder.exportSymbols("RC-RUGGEDCOM-SYS-INFO-MIB-AC", ruggedcomRcSysinfoAC03=ruggedcomRcSysinfoAC03, ruggedcomRcSysinfoAC=ruggedcomRcSysinfoAC, ruggedcomRcSysinfoACModule=ruggedcomRcSysinfoACModule, ruggedcomRcSysinfoAC02=ruggedcomRcSysinfoAC02, PYSNMP_MODULE_ID=ruggedcomRcSysinfoACModule, ruggedcomRcSysinfoAC01=ruggedcomRcSysinfoAC01, ruggedcomRcSysinfoAC05=ruggedcomRcSysinfoAC05, ruggedcomRcSysinfoAC04=ruggedcomRcSysinfoAC04)
