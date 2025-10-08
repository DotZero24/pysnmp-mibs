#
# PySNMP MIB module RC-RUGGEDCOM-AAA-SERVER-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-AAA-SERVER-MIB-AC
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
ruggedcomRcAAAServerACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 48))
ruggedcomRcAAAServerACModule.setRevisions(('2017-09-20 11:00',))
if mibBuilder.loadTexts: ruggedcomRcAAAServerACModule.setLastUpdated('201709201100Z')
if mibBuilder.loadTexts: ruggedcomRcAAAServerACModule.setOrganization('Siemens Canada Ltd., Process Industries and Drives')
ruggedcomRcRadiusServerAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 48, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcRadiusServerAC = ruggedcomRcRadiusServerAC.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcRadiusServerAC = ruggedcomRcRadiusServerAC.setStatus('current')
ruggedcomRcTacacsServerAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 48, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTacacsServerAC = ruggedcomRcTacacsServerAC.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcTacacsServerAC = ruggedcomRcTacacsServerAC.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-AAA-SERVER-MIB-AC", ruggedcomRcRadiusServerAC=ruggedcomRcRadiusServerAC, ruggedcomRcAAAServerACModule=ruggedcomRcAAAServerACModule, ruggedcomRcTacacsServerAC=ruggedcomRcTacacsServerAC, PYSNMP_MODULE_ID=ruggedcomRcAAAServerACModule)
