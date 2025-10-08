#
# PySNMP MIB module QTECH-GBNL3RouteCommon-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-GBNL3RouteCommon-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
gbnL3, = mibBuilder.importSymbols("QTECH-MASTER-MIB", "gbnL3")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
gbnL3RouteCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2))
gbnL3RouteCommon.setRevisions(('1901-05-10 20:04',))
if mibBuilder.loadTexts: gbnL3RouteCommon.setLastUpdated('0105102004Z')
if mibBuilder.loadTexts: gbnL3RouteCommon.setOrganization('QTECH LLC')
routerId = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2, 1))
routerIdConfig = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: routerIdConfig.setStatus('current')
routerIdValue = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: routerIdValue.setStatus('current')
mibBuilder.exportSymbols("QTECH-GBNL3RouteCommon-MIB", routerId=routerId, routerIdValue=routerIdValue, gbnL3RouteCommon=gbnL3RouteCommon, PYSNMP_MODULE_ID=gbnL3RouteCommon, routerIdConfig=routerIdConfig)
