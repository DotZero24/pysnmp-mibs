#
# PySNMP MIB module RC-RUGGEDCOM-TRAPS-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-TRAPS-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:56 2025
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
ruggedcomRcTrapsACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 11))
ruggedcomRcTrapsACModule.setRevisions(('2012-08-30 17:00', '2012-06-01 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomRcTrapsACModule.setLastUpdated('201208301700Z')
if mibBuilder.loadTexts: ruggedcomRcTrapsACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomRcTrapsAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC = ruggedcomRcTrapsAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC = ruggedcomRcTrapsAC.setStatus('current')
ruggedcomRcTrapsAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC01 = ruggedcomRcTrapsAC01.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC01 = ruggedcomRcTrapsAC01.setStatus('current')
ruggedcomRcTrapsAC02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC02 = ruggedcomRcTrapsAC02.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC02 = ruggedcomRcTrapsAC02.setStatus('current')
ruggedcomRcTrapsAC03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 11, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC03 = ruggedcomRcTrapsAC03.setProductRelease('Ruggedcom ROX 2.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTrapsAC03 = ruggedcomRcTrapsAC03.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-TRAPS-MIB-AC", ruggedcomRcTrapsACModule=ruggedcomRcTrapsACModule, ruggedcomRcTrapsAC03=ruggedcomRcTrapsAC03, ruggedcomRcTrapsAC01=ruggedcomRcTrapsAC01, ruggedcomRcTrapsAC=ruggedcomRcTrapsAC, ruggedcomRcTrapsAC02=ruggedcomRcTrapsAC02, PYSNMP_MODULE_ID=ruggedcomRcTrapsACModule)
