#
# PySNMP MIB module RC-RUGGEDCOM-SFP-DDM-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-SFP-DDM-MIB-AC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:00 2025
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
ruggedcomRcSfpDdmACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 50))
if mibBuilder.loadTexts: ruggedcomRcSfpDdmACModule.setLastUpdated('202107211609Z')
if mibBuilder.loadTexts: ruggedcomRcSfpDdmACModule.setOrganization('Siemens Canada Ltd., Process Industries and Drives')
ruggedcomRcSfpDdmAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 50, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSfpDdmAC = ruggedcomRcSfpDdmAC.setProductRelease('ROS')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcSfpDdmAC = ruggedcomRcSfpDdmAC.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-SFP-DDM-MIB-AC", PYSNMP_MODULE_ID=ruggedcomRcSfpDdmACModule, ruggedcomRcSfpDdmACModule=ruggedcomRcSfpDdmACModule, ruggedcomRcSfpDdmAC=ruggedcomRcSfpDdmAC)
