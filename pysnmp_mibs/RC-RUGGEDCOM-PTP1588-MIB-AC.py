#
# PySNMP MIB module RC-RUGGEDCOM-PTP1588-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-PTP1588-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:28 2025
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
ruggedcomRcPTP1588ACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 46))
ruggedcomRcPTP1588ACModule.setRevisions(('2022-02-08 13:50', '2015-09-23 13:00', '2022-02-08 13:50', '2022-08-03 15:00',))
if mibBuilder.loadTexts: ruggedcomRcPTP1588ACModule.setLastUpdated('202202081350Z')
if mibBuilder.loadTexts: ruggedcomRcPTP1588ACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomRcPTP1588AC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 46, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcPTP1588AC = ruggedcomRcPTP1588AC.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcPTP1588AC = ruggedcomRcPTP1588AC.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-PTP1588-MIB-AC", ruggedcomRcPTP1588AC=ruggedcomRcPTP1588AC, ruggedcomRcPTP1588ACModule=ruggedcomRcPTP1588ACModule, PYSNMP_MODULE_ID=ruggedcomRcPTP1588ACModule)
