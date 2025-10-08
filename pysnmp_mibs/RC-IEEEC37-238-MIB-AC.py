#
# PySNMP MIB module RC-IEEEC37-238-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-IEEEC37-238-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:59 2025
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
ruggedcomIEEEC37238ACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 44))
ruggedcomIEEEC37238ACModule.setRevisions(('2022-08-03 15:00', '2022-03-08 13:16', '2023-07-07 16:00', '2023-07-17 14:00', '2023-08-02 12:00', '2015-09-09 15:00',))
if mibBuilder.loadTexts: ruggedcomIEEEC37238ACModule.setLastUpdated('202307071600Z')
if mibBuilder.loadTexts: ruggedcomIEEEC37238ACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomIEEEC37238AC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 44, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIEEEC37238AC = ruggedcomIEEEC37238AC.setProductRelease('ROS-MB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIEEEC37238AC = ruggedcomIEEEC37238AC.setStatus('current')
mibBuilder.exportSymbols("RC-IEEEC37-238-MIB-AC", PYSNMP_MODULE_ID=ruggedcomIEEEC37238ACModule, ruggedcomIEEEC37238ACModule=ruggedcomIEEEC37238ACModule, ruggedcomIEEEC37238AC=ruggedcomIEEEC37238AC)
