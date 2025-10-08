#
# PySNMP MIB module Dell-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/Dell-TRACEROUTE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlTraceRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 81))
rlTraceRoute.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('Dell')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
mibBuilder.exportSymbols("Dell-TRACEROUTE-MIB", rlTraceRouteMibVersion=rlTraceRouteMibVersion, rlTraceRoute=rlTraceRoute, PYSNMP_MODULE_ID=rlTraceRoute)
