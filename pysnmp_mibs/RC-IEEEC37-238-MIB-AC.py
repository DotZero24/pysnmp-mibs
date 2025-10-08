#
# PySNMP MIB module RC-IEEEC37-238-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-IEEEC37-238-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:27 2025
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
ruggedcomIEEEC37238ACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 44))
ruggedcomIEEEC37238ACModule.setRevisions(('2022-08-03 15:00', '2022-03-08 13:16', '2023-07-07 16:00', '2023-07-17 14:00', '2023-08-02 12:00', '2015-09-09 15:00',))
if mibBuilder.loadTexts: ruggedcomIEEEC37238ACModule.setLastUpdated('202307071600Z')
if mibBuilder.loadTexts: ruggedcomIEEEC37238ACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomIEEEC37238AC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 44, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIEEEC37238AC = ruggedcomIEEEC37238AC.setProductRelease('ROS-MB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIEEEC37238AC = ruggedcomIEEEC37238AC.setStatus('current')
mibBuilder.exportSymbols("RC-IEEEC37-238-MIB-AC", ruggedcomIEEEC37238ACModule=ruggedcomIEEEC37238ACModule, PYSNMP_MODULE_ID=ruggedcomIEEEC37238ACModule, ruggedcomIEEEC37238AC=ruggedcomIEEEC37238AC)
