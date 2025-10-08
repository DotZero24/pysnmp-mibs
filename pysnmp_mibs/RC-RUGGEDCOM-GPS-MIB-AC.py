#
# PySNMP MIB module RC-RUGGEDCOM-GPS-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-GPS-MIB-AC
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
ruggedcomRcGpsACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 42))
ruggedcomRcGpsACModule.setRevisions(('2015-10-30 17:00', '2014-12-05 17:00',))
if mibBuilder.loadTexts: ruggedcomRcGpsACModule.setLastUpdated('201510301700Z')
if mibBuilder.loadTexts: ruggedcomRcGpsACModule.setOrganization('Siemens Canada Limited')
ruggedcomRcGpsAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 42, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcGpsAC = ruggedcomRcGpsAC.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcGpsAC = ruggedcomRcGpsAC.setStatus('current')
ruggedcomRcGpsAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 42, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcGpsAC01 = ruggedcomRcGpsAC01.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcGpsAC01 = ruggedcomRcGpsAC01.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-GPS-MIB-AC", ruggedcomRcGpsAC=ruggedcomRcGpsAC, PYSNMP_MODULE_ID=ruggedcomRcGpsACModule, ruggedcomRcGpsAC01=ruggedcomRcGpsAC01, ruggedcomRcGpsACModule=ruggedcomRcGpsACModule)
