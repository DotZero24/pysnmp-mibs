#
# PySNMP MIB module HM2-PLATFORM-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-PLATFORM-SFLOW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2PlatformSflow = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 59))
hm2PlatformSflow.setRevisions(('2011-10-12 00:00',))
if mibBuilder.loadTexts: hm2PlatformSflow.setLastUpdated('201110120000Z')
if mibBuilder.loadTexts: hm2PlatformSflow.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentFastPathSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 59, 1))
hm2AgentSflowSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 59, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentSflowSourceInterface.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-SFLOW-MIB", hm2AgentFastPathSflowObjects=hm2AgentFastPathSflowObjects, hm2AgentSflowSourceInterface=hm2AgentSflowSourceInterface, hm2PlatformSflow=hm2PlatformSflow, PYSNMP_MODULE_ID=hm2PlatformSflow)
