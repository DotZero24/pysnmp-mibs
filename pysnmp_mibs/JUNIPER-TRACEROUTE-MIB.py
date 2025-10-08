#
# PySNMP MIB module JUNIPER-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-TRACEROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("JUNIPER-TRACEROUTE-MIB", jnxTraceRouteCtlTable=jnxTraceRouteCtlTable, PYSNMP_MODULE_ID=jnxTraceRouteMIB, jnxTRCtlTestName=jnxTRCtlTestName, jnxTraceRouteMIB=jnxTraceRouteMIB, jnxTraceRouteCtlEntry=jnxTraceRouteCtlEntry, jnxTRCtlRoutingInstanceName=jnxTRCtlRoutingInstanceName, jnxTRCtlIfName=jnxTRCtlIfName, jnxTRCtlOwnerIndex=jnxTRCtlOwnerIndex, jnxTraceRouteObjects=jnxTraceRouteObjects)
