#
# PySNMP MIB module HM2-PLATFORM-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HM2-PLATFORM-SFLOW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PlatformSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 59))
hm2PlatformSflow.setRevisions(('2011-10-12 00:00',))
if mibBuilder.loadTexts: hm2PlatformSflow.setLastUpdated('201110120000Z')
if mibBuilder.loadTexts: hm2PlatformSflow.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 59, 1))
hm2AgentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-SFLOW-MIB", hm2PlatformSflow=hm2PlatformSflow, PYSNMP_MODULE_ID=hm2PlatformSflow, hm2AgentFastPathSflowObjects=hm2AgentFastPathSflowObjects, hm2AgentSflowSourceInterface=hm2AgentSflowSourceInterface)
