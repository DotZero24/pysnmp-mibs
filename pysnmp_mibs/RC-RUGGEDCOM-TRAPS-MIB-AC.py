#
# PySNMP MIB module RC-RUGGEDCOM-TRAPS-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-TRAPS-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:20 2025
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
mibBuilder.exportSymbols("RC-RUGGEDCOM-TRAPS-MIB-AC", PYSNMP_MODULE_ID=ruggedcomRcTrapsACModule, ruggedcomRcTrapsAC=ruggedcomRcTrapsAC, ruggedcomRcTrapsAC03=ruggedcomRcTrapsAC03, ruggedcomRcTrapsAC02=ruggedcomRcTrapsAC02, ruggedcomRcTrapsACModule=ruggedcomRcTrapsACModule, ruggedcomRcTrapsAC01=ruggedcomRcTrapsAC01)
