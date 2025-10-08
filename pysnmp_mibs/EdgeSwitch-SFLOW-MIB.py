#
# PySNMP MIB module EdgeSwitch-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ubiquiti/EdgeSwitch-SFLOW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fastPathSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59))
if mibBuilder.loadTexts: fastPathSflow.setLastUpdated('201201120000Z')
if mibBuilder.loadTexts: fastPathSflow.setOrganization('Broadcom Inc')
agentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1))
agentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-SFLOW-MIB", PYSNMP_MODULE_ID=fastPathSflow, agentSflowSourceInterface=agentSflowSourceInterface, fastPathSflow=fastPathSflow, agentFastPathSflowObjects=agentFastPathSflowObjects)
