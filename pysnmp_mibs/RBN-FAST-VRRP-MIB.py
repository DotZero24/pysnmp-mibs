#
# PySNMP MIB module RBN-FAST-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-FAST-VRRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RBN-FAST-VRRP-MIB", rbnFastVrrpOperTable=rbnFastVrrpOperTable, rbnFastVrrpMIB=rbnFastVrrpMIB, PYSNMP_MODULE_ID=rbnFastVrrpMIB, rbnFastVrrpMIBCompliances=rbnFastVrrpMIBCompliances, rbnFastVrrpObjectGroup=rbnFastVrrpObjectGroup, rbnFastVrrpCompliance=rbnFastVrrpCompliance, rbnFastVrrpOperVrId=rbnFastVrrpOperVrId, rbnFastVrrpOperAdvertisementInterval=rbnFastVrrpOperAdvertisementInterval, rbnFastVrrpMIBObjects=rbnFastVrrpMIBObjects, rbnFastVrrpOperEntry=rbnFastVrrpOperEntry, rbnFastVrrpMIBGroups=rbnFastVrrpMIBGroups, rbnFastVrrpConformance=rbnFastVrrpConformance)
