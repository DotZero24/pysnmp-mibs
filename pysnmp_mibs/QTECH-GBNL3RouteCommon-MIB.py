#
# PySNMP MIB module QTECH-GBNL3RouteCommon-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-GBNL3RouteCommon-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
gbnL3, = mibBuilder.importSymbols("QTECH-MASTER-MIB", "gbnL3")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
gbnL3RouteCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2))
gbnL3RouteCommon.setRevisions(('1901-05-10 20:04',))
if mibBuilder.loadTexts: gbnL3RouteCommon.setLastUpdated('0105102004Z')
if mibBuilder.loadTexts: gbnL3RouteCommon.setOrganization('QTECH LLC')
routerId = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2, 1))
routerIdConfig = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: routerIdConfig.setStatus('current')
routerIdValue = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: routerIdValue.setStatus('current')
mibBuilder.exportSymbols("QTECH-GBNL3RouteCommon-MIB", routerId=routerId, routerIdConfig=routerIdConfig, routerIdValue=routerIdValue, gbnL3RouteCommon=gbnL3RouteCommon, PYSNMP_MODULE_ID=gbnL3RouteCommon)
