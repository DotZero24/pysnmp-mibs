#
# PySNMP MIB module RC-RUGGEDCOM-POE-AC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-POE-AC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:55 2025
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
ruggedcomRcPoeACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 14))
ruggedcomRcPoeACModule.setRevisions(('2012-06-01 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomRcPoeACModule.setLastUpdated('201206011700Z')
if mibBuilder.loadTexts: ruggedcomRcPoeACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomRcPoeAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 14, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcPoeAC = ruggedcomRcPoeAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcPoeAC = ruggedcomRcPoeAC.setStatus('current')
ruggedcomRcPoe2AC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 14, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcPoe2AC = ruggedcomRcPoe2AC.setProductRelease('ROS-CF52 based RuggedCom devices that support\r\n    \t\t\t\t RUGGEDCOM-POE-MIB.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcPoe2AC = ruggedcomRcPoe2AC.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-POE-AC-MIB", ruggedcomRcPoeAC=ruggedcomRcPoeAC, PYSNMP_MODULE_ID=ruggedcomRcPoeACModule, ruggedcomRcPoe2AC=ruggedcomRcPoe2AC, ruggedcomRcPoeACModule=ruggedcomRcPoeACModule)
