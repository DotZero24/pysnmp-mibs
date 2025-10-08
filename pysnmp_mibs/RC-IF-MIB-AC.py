#
# PySNMP MIB module RC-IF-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-IF-MIB-AC
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
ruggedcomIfACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 2))
ruggedcomIfACModule.setRevisions(('2013-11-14 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomIfACModule.setLastUpdated('201311141700Z')
if mibBuilder.loadTexts: ruggedcomIfACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomIfAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIfAC = ruggedcomIfAC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIfAC = ruggedcomIfAC.setStatus('current')
ruggedcomIfAC01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 2, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIfAC01 = ruggedcomIfAC01.setProductRelease('Ruggedcom ROX 2.4.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIfAC01 = ruggedcomIfAC01.setStatus('current')
mibBuilder.exportSymbols("RC-IF-MIB-AC", ruggedcomIfACModule=ruggedcomIfACModule, ruggedcomIfAC01=ruggedcomIfAC01, ruggedcomIfAC=ruggedcomIfAC, PYSNMP_MODULE_ID=ruggedcomIfACModule)
