#
# PySNMP MIB module RC-RUGGEDCOM-GPS-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-GPS-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:24 2025
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
mibBuilder.exportSymbols("RC-RUGGEDCOM-GPS-MIB-AC", ruggedcomRcGpsACModule=ruggedcomRcGpsACModule, ruggedcomRcGpsAC=ruggedcomRcGpsAC, ruggedcomRcGpsAC01=ruggedcomRcGpsAC01, PYSNMP_MODULE_ID=ruggedcomRcGpsACModule)
