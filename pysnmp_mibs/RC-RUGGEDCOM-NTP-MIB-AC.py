#
# PySNMP MIB module RC-RUGGEDCOM-NTP-MIB-AC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/siemens/RC-RUGGEDCOM-NTP-MIB-AC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:25 2025
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
ruggedcomRcNTPACModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 15004, 6, 30, 47))
ruggedcomRcNTPACModule.setRevisions(('2017-02-15 10:00', '2015-09-23 13:00',))
if mibBuilder.loadTexts: ruggedcomRcNTPACModule.setLastUpdated('201702151000Z')
if mibBuilder.loadTexts: ruggedcomRcNTPACModule.setOrganization('Siemens Canada Ltd., Process Industries and Drives')
ruggedcomRcNTPAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 47, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcNTPAC = ruggedcomRcNTPAC.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcNTPAC = ruggedcomRcNTPAC.setStatus('obsolete')
ruggedcomRcNTPAC02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 15004, 6, 30, 47, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcNTPAC02 = ruggedcomRcNTPAC02.setProductRelease('ROS-MPC83 and ROS-CF52')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ruggedcomRcNTPAC02 = ruggedcomRcNTPAC02.setStatus('current')
mibBuilder.exportSymbols("RC-RUGGEDCOM-NTP-MIB-AC", ruggedcomRcNTPAC02=ruggedcomRcNTPAC02, ruggedcomRcNTPAC=ruggedcomRcNTPAC, PYSNMP_MODULE_ID=ruggedcomRcNTPACModule, ruggedcomRcNTPACModule=ruggedcomRcNTPACModule)
