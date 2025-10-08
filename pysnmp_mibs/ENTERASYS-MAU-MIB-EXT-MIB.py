#
# PySNMP MIB module ENTERASYS-MAU-MIB-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-MAU-MIB-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifMauIfIndex, = mibBuilder.importSymbols("MAU-MIB", "ifMauIfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-MAU-MIB-EXT-MIB", etsysIfMauExtMDIXStatus=etsysIfMauExtMDIXStatus, etsysIfMauExtMasterSlaveStatus=etsysIfMauExtMasterSlaveStatus, etsysMauMibExtObjects=etsysMauMibExtObjects, etsysMauMibExtBasic=etsysMauMibExtBasic, etsysMauMibExtMasterSlaveCompliance=etsysMauMibExtMasterSlaveCompliance, etsysIfMauExtMDIXTable=etsysIfMauExtMDIXTable, etsysMauMibExtMDIXGroup=etsysMauMibExtMDIXGroup, etsysMauMibExtMDIXCompliance=etsysMauMibExtMDIXCompliance, etsysMauMibExtConformance=etsysMauMibExtConformance, etsysMauMibExtMasterSlaveGroup=etsysMauMibExtMasterSlaveGroup, PYSNMP_MODULE_ID=etsysMauMibExtMIB, etsysIfMauExtMasterSlaveTable=etsysIfMauExtMasterSlaveTable, etsysIfMauExtMasterSlaveEntry=etsysIfMauExtMasterSlaveEntry, etsysMauMibExtGroups=etsysMauMibExtGroups, etsysIfMauExtMDIXEntry=etsysIfMauExtMDIXEntry, etsysMauMibExtCompliances=etsysMauMibExtCompliances, etsysMauMibExtMIB=etsysMauMibExtMIB)
