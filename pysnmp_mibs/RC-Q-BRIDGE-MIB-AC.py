#
# PySNMP MIB module RC-Q-BRIDGE-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-Q-BRIDGE-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:58 2025
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
ruggedcomqBridgeACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 10))
ruggedcomqBridgeACModule.setRevisions(('2012-06-01 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomqBridgeACModule.setLastUpdated('201206011700Z')
if mibBuilder.loadTexts: ruggedcomqBridgeACModule.setOrganization('RuggedCom - Industrial Strength Networks')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

ruggedcomqBridgeAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 10, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomqBridgeAC = ruggedcomqBridgeAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomqBridgeAC = ruggedcomqBridgeAC.setStatus('current')
ruggedcomqBridgeAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 10, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomqBridgeAC01 = ruggedcomqBridgeAC01.setProductRelease('Ruggedcom ROX 2.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomqBridgeAC01 = ruggedcomqBridgeAC01.setStatus('current')
mibBuilder.exportSymbols("RC-Q-BRIDGE-MIB-AC", ruggedcomqBridgeAC01=ruggedcomqBridgeAC01, EnabledStatus=EnabledStatus, ruggedcomqBridgeACModule=ruggedcomqBridgeACModule, ruggedcomqBridgeAC=ruggedcomqBridgeAC, PYSNMP_MODULE_ID=ruggedcomqBridgeACModule)
