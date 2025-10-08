#
# PySNMP MIB module RBN-FAST-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-FAST-VRRP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
VrId, = mibBuilder.importSymbols("VRRP-MIB", "VrId")
rbnFastVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 45))
rbnFastVrrpMIB.setRevisions(('2008-05-21 00:00',))
if mibBuilder.loadTexts: rbnFastVrrpMIB.setLastUpdated('200805210000Z')
if mibBuilder.loadTexts: rbnFastVrrpMIB.setOrganization('Redback Networks, Inc.')
rbnFastVrrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1))
rbnFastVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2))
rbnFastVrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1), )
if mibBuilder.loadTexts: rbnFastVrrpOperTable.setStatus('current')
rbnFastVrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-FAST-VRRP-MIB", "rbnFastVrrpOperVrId"))
if mibBuilder.loadTexts: rbnFastVrrpOperEntry.setStatus('current')
rbnFastVrrpOperVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 1), VrId())
if mibBuilder.loadTexts: rbnFastVrrpOperVrId.setStatus('current')
rbnFastVrrpOperAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 45, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 999))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFastVrrpOperAdvertisementInterval.setStatus('current')
rbnFastVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1))
rbnFastVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2))
rbnFastVrrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 1, 1)).setObjects(("RBN-FAST-VRRP-MIB", "rbnFastVrrpObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFastVrrpCompliance = rbnFastVrrpCompliance.setStatus('current')
rbnFastVrrpObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 45, 2, 2, 1)).setObjects(("RBN-FAST-VRRP-MIB", "rbnFastVrrpOperAdvertisementInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnFastVrrpObjectGroup = rbnFastVrrpObjectGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-FAST-VRRP-MIB", rbnFastVrrpMIBObjects=rbnFastVrrpMIBObjects, rbnFastVrrpMIBGroups=rbnFastVrrpMIBGroups, PYSNMP_MODULE_ID=rbnFastVrrpMIB, rbnFastVrrpOperVrId=rbnFastVrrpOperVrId, rbnFastVrrpOperAdvertisementInterval=rbnFastVrrpOperAdvertisementInterval, rbnFastVrrpConformance=rbnFastVrrpConformance, rbnFastVrrpOperTable=rbnFastVrrpOperTable, rbnFastVrrpMIB=rbnFastVrrpMIB, rbnFastVrrpCompliance=rbnFastVrrpCompliance, rbnFastVrrpMIBCompliances=rbnFastVrrpMIBCompliances, rbnFastVrrpOperEntry=rbnFastVrrpOperEntry, rbnFastVrrpObjectGroup=rbnFastVrrpObjectGroup)
