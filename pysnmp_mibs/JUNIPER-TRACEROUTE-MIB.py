#
# PySNMP MIB module JUNIPER-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-TRACEROUTE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxTraceRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 8))
if mibBuilder.loadTexts: jnxTraceRouteMIB.setLastUpdated('200307182154Z')
if mibBuilder.loadTexts: jnxTraceRouteMIB.setOrganization('Juniper Networks, Inc.')
jnxTraceRouteObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1))
jnxTraceRouteCtlTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2), )
if mibBuilder.loadTexts: jnxTraceRouteCtlTable.setStatus('current')
jnxTraceRouteCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1), ).setIndexNames((0, "JUNIPER-TRACEROUTE-MIB", "jnxTRCtlOwnerIndex"), (0, "JUNIPER-TRACEROUTE-MIB", "jnxTRCtlTestName"))
if mibBuilder.loadTexts: jnxTraceRouteCtlEntry.setStatus('current')
jnxTRCtlOwnerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: jnxTRCtlOwnerIndex.setStatus('current')
jnxTRCtlTestName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: jnxTRCtlTestName.setStatus('current')
jnxTRCtlIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: jnxTRCtlIfName.setStatus('current')
jnxTRCtlRoutingInstanceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 8, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: jnxTRCtlRoutingInstanceName.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-TRACEROUTE-MIB", jnxTRCtlOwnerIndex=jnxTRCtlOwnerIndex, jnxTraceRouteCtlEntry=jnxTraceRouteCtlEntry, jnxTRCtlIfName=jnxTRCtlIfName, jnxTRCtlRoutingInstanceName=jnxTRCtlRoutingInstanceName, PYSNMP_MODULE_ID=jnxTraceRouteMIB, jnxTRCtlTestName=jnxTRCtlTestName, jnxTraceRouteObjects=jnxTraceRouteObjects, jnxTraceRouteMIB=jnxTraceRouteMIB, jnxTraceRouteCtlTable=jnxTraceRouteCtlTable)
