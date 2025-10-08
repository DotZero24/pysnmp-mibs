#
# PySNMP MIB module ENTERASYS-MAU-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-MAU-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifMauIfIndex, = mibBuilder.importSymbols("MAU-MIB", "ifMauIfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysMauMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59))
etsysMauMibExtMIB.setRevisions(('2011-08-15 18:12', '2006-05-09 11:30', '2006-02-16 19:18', '2005-02-07 15:05',))
if mibBuilder.loadTexts: etsysMauMibExtMIB.setLastUpdated('201108151812Z')
if mibBuilder.loadTexts: etsysMauMibExtMIB.setOrganization('Enterasys Networks, Inc.')
etsysMauMibExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1))
etsysMauMibExtBasic = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1))
etsysIfMauExtMDIXTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1), )
if mibBuilder.loadTexts: etsysIfMauExtMDIXTable.setStatus('current')
etsysIfMauExtMDIXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"))
if mibBuilder.loadTexts: etsysIfMauExtMDIXEntry.setStatus('current')
etsysIfMauExtMDIXStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("mdix", 2), ("mdi", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfMauExtMDIXStatus.setStatus('current')
etsysIfMauExtMasterSlaveTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2), )
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveTable.setStatus('deprecated')
etsysIfMauExtMasterSlaveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"))
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveEntry.setStatus('deprecated')
etsysIfMauExtMasterSlaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("slave", 2))).clone('slave')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysIfMauExtMasterSlaveStatus.setStatus('deprecated')
etsysMauMibExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2))
etsysMauMibExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1))
etsysMauMibExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2))
etsysMauMibExtMDIXGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 1)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMDIXStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMDIXGroup = etsysMauMibExtMDIXGroup.setStatus('current')
etsysMauMibExtMasterSlaveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 1, 2)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysIfMauExtMasterSlaveStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMasterSlaveGroup = etsysMauMibExtMasterSlaveGroup.setStatus('deprecated')
etsysMauMibExtMDIXCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 1)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysMauMibExtMDIXGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMDIXCompliance = etsysMauMibExtMDIXCompliance.setStatus('current')
etsysMauMibExtMasterSlaveCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 59, 2, 2, 2)).setObjects(("ENTERASYS-MAU-MIB-EXT-MIB", "etsysMauMibExtMasterSlaveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMauMibExtMasterSlaveCompliance = etsysMauMibExtMasterSlaveCompliance.setStatus('deprecated')
mibBuilder.exportSymbols("ENTERASYS-MAU-MIB-EXT-MIB", etsysIfMauExtMDIXEntry=etsysIfMauExtMDIXEntry, etsysIfMauExtMasterSlaveStatus=etsysIfMauExtMasterSlaveStatus, PYSNMP_MODULE_ID=etsysMauMibExtMIB, etsysMauMibExtConformance=etsysMauMibExtConformance, etsysMauMibExtCompliances=etsysMauMibExtCompliances, etsysMauMibExtMDIXGroup=etsysMauMibExtMDIXGroup, etsysMauMibExtMIB=etsysMauMibExtMIB, etsysIfMauExtMDIXStatus=etsysIfMauExtMDIXStatus, etsysMauMibExtGroups=etsysMauMibExtGroups, etsysMauMibExtMasterSlaveCompliance=etsysMauMibExtMasterSlaveCompliance, etsysMauMibExtObjects=etsysMauMibExtObjects, etsysMauMibExtMDIXCompliance=etsysMauMibExtMDIXCompliance, etsysMauMibExtBasic=etsysMauMibExtBasic, etsysIfMauExtMDIXTable=etsysIfMauExtMDIXTable, etsysIfMauExtMasterSlaveTable=etsysIfMauExtMasterSlaveTable, etsysIfMauExtMasterSlaveEntry=etsysIfMauExtMasterSlaveEntry, etsysMauMibExtMasterSlaveGroup=etsysMauMibExtMasterSlaveGroup)
