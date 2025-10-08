#
# PySNMP MIB module RC-IEC-62439-3-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-IEC-62439-3-MIB-AC
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
ruggedcomIEC624393ACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 40))
ruggedcomIEC624393ACModule.setRevisions(('2013-10-04 17:00',))
if mibBuilder.loadTexts: ruggedcomIEC624393ACModule.setLastUpdated('201310041700Z')
if mibBuilder.loadTexts: ruggedcomIEC624393ACModule.setOrganization('RuggedCom - Industrial Strength Networks')
ruggedcomIEC624393AC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 40, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIEC624393AC = ruggedcomIEC624393AC.setProductRelease('ROS-MB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomIEC624393AC = ruggedcomIEC624393AC.setStatus('current')
mibBuilder.exportSymbols("RC-IEC-62439-3-MIB-AC", ruggedcomIEC624393AC=ruggedcomIEC624393AC, ruggedcomIEC624393ACModule=ruggedcomIEC624393ACModule, PYSNMP_MODULE_ID=ruggedcomIEC624393ACModule)
