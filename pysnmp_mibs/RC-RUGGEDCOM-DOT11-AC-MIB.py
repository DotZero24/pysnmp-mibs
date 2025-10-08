#
# PySNMP MIB module RC-RUGGEDCOM-DOT11-AC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-DOT11-AC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:22 2025
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
ruggedcomRcDot11ACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 16))
ruggedcomRcDot11ACModule.setRevisions(('2012-06-01 17:00', '2011-02-22 17:00',))
if mibBuilder.loadTexts: ruggedcomRcDot11ACModule.setLastUpdated('201206011700Z')
if mibBuilder.loadTexts: ruggedcomRcDot11ACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomRcDot11AC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 16, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcDot11AC = ruggedcomRcDot11AC.setProductRelease('ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcDot11AC = ruggedcomRcDot11AC.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-DOT11-AC-MIB", PYSNMP_MODULE_ID=ruggedcomRcDot11ACModule, ruggedcomRcDot11AC=ruggedcomRcDot11AC, ruggedcomRcDot11ACModule=ruggedcomRcDot11ACModule)
