#
# PySNMP MIB module EdgeSwitch-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ubiquiti/EdgeSwitch-SFLOW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fastPathSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59))
if mibBuilder.loadTexts: fastPathSflow.setLastUpdated('201201120000Z')
if mibBuilder.loadTexts: fastPathSflow.setOrganization('Broadcom Inc')
agentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1))
agentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-SFLOW-MIB", PYSNMP_MODULE_ID=fastPathSflow, agentFastPathSflowObjects=agentFastPathSflowObjects, agentSflowSourceInterface=agentSflowSourceInterface, fastPathSflow=fastPathSflow)
