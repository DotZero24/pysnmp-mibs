#
# PySNMP MIB module ENTERASYS-RIPv2-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-RIPv2-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysRip2ExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66))
etsysRip2ExtMIB.setRevisions(('2009-02-06 17:11',))
if mibBuilder.loadTexts: etsysRip2ExtMIB.setLastUpdated('200902061711Z')
if mibBuilder.loadTexts: etsysRip2ExtMIB.setOrganization('Enterasys Networks, Inc.')
etsysRip2ExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1))
etsysRip2ExtGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1))
etsysRip2ExtAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))).clone('adminStatusDown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtAdminStatus.setStatus('current')
etsysRip2ExtOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysRip2ExtOperStatus.setStatus('current')
etsysRip2ExtMaxEcmpHops = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtMaxEcmpHops.setStatus('current')
etsysRip2ExtRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtRefreshInterval.setStatus('current')
etsysRip2ExtTriggeredDelayMin = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 5), Unsigned32().clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtTriggeredDelayMin.setStatus('current')
etsysRip2ExtTriggeredDelayMax = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 6), Unsigned32().clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtTriggeredDelayMax.setStatus('current')
etsysRip2ExtRouteCheckInterval = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtRouteCheckInterval.setStatus('current')
etsysRip2ExtRouteExpiryInterval = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtRouteExpiryInterval.setStatus('current')
etsysRip2ExtRouteFlushInterval = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRip2ExtRouteFlushInterval.setStatus('current')
etsysRip2ExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2))
etsysRip2ExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 1))
etsysRip2ExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 2))
etsysRip2ExtGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 1, 1)).setObjects(("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtAdminStatus"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtOperStatus"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtMaxEcmpHops"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRefreshInterval"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtTriggeredDelayMin"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtTriggeredDelayMax"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRouteCheckInterval"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRouteExpiryInterval"), ("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtRouteFlushInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRip2ExtGlobalGroup = etsysRip2ExtGlobalGroup.setStatus('current')
etsysRip2ExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 66, 2, 2, 1)).setObjects(("ENTERASYS-RIPv2-EXT-MIB", "etsysRip2ExtGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRip2ExtCompliance = etsysRip2ExtCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RIPv2-EXT-MIB", etsysRip2ExtRouteExpiryInterval=etsysRip2ExtRouteExpiryInterval, etsysRip2ExtGlobalGroup=etsysRip2ExtGlobalGroup, etsysRip2ExtMIB=etsysRip2ExtMIB, etsysRip2ExtRouteCheckInterval=etsysRip2ExtRouteCheckInterval, etsysRip2ExtGlobals=etsysRip2ExtGlobals, PYSNMP_MODULE_ID=etsysRip2ExtMIB, etsysRip2ExtOperStatus=etsysRip2ExtOperStatus, etsysRip2ExtAdminStatus=etsysRip2ExtAdminStatus, etsysRip2ExtRefreshInterval=etsysRip2ExtRefreshInterval, etsysRip2ExtConformance=etsysRip2ExtConformance, etsysRip2ExtRouteFlushInterval=etsysRip2ExtRouteFlushInterval, etsysRip2ExtTriggeredDelayMin=etsysRip2ExtTriggeredDelayMin, etsysRip2ExtTriggeredDelayMax=etsysRip2ExtTriggeredDelayMax, etsysRip2ExtGroups=etsysRip2ExtGroups, etsysRip2ExtCompliance=etsysRip2ExtCompliance, etsysRip2ExtObjects=etsysRip2ExtObjects, etsysRip2ExtMaxEcmpHops=etsysRip2ExtMaxEcmpHops, etsysRip2ExtCompliances=etsysRip2ExtCompliances)
