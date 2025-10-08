#
# PySNMP MIB module LUM-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/LUM-INVENTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lumModules, lumInventoryMIB = mibBuilder.importSymbols("LUM-REG", "lumModules", "lumInventoryMIB")
MgmtNameString, = mibBuilder.importSymbols("LUM-TC", "MgmtNameString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, TestAndIncr, RowPointer, TruthValue, AutonomousType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TestAndIncr", "RowPointer", "TruthValue", "AutonomousType", "DisplayString")
lumInventoryMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8708, 1, 1, 5))
lumInventoryMIBModule.setRevisions(('2017-06-15 00:00', '2014-09-30 00:00', '2005-09-14 00:00', '2004-09-30 00:00', '2002-03-08 00:00', '2001-10-30 00:00', '2001-07-17 00:00', '2001-05-11 00:00', '2001-05-10 00:00',))
if mibBuilder.loadTexts: lumInventoryMIBModule.setLastUpdated('201706150000Z')
if mibBuilder.loadTexts: lumInventoryMIBModule.setOrganization('Infinera Corporation')
lumInventoryConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1))
lumInventoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1))
lumInventoryCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2))
lumInventoryMinimalGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 3))
lumInventoryMinimalCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4))
lumInventoryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2))
invPhysical = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1))
invGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2))
lumentisInvNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3))
invEntities = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4))
invRelations = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5))
invInsRemLog = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6))
class PhysicalClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11))

class EntityClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("undefined", 0), ("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("logical", 12))

class InsRemEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("insert", 0), ("remove", 1))

invPhysTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1), )
if mibBuilder.loadTexts: invPhysTable.setStatus('current')
invPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1), ).setIndexNames((0, "LUM-INVENTORY-MIB", "invPhysIndex"))
if mibBuilder.loadTexts: invPhysEntry.setStatus('current')
invPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysIndex.setStatus('current')
invPhysDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysDescr.setStatus('current')
invPhysVendorType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysVendorType.setStatus('deprecated')
invPhysContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysContainedIn.setStatus('current')
invPhysClass = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 5), PhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysClass.setStatus('current')
invPhysParentRelPos = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysParentRelPos.setStatus('current')
invPhysName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 7), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysName.setStatus('current')
invPhysHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysHardwareRev.setStatus('current')
invPhysFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysFirmwareRev.setStatus('current')
invPhysProductDataRev = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysProductDataRev.setStatus('current')
invPhysSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 11), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysSerialNum.setStatus('current')
invPhysMfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysMfgName.setStatus('current')
invPhysModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysModelName.setStatus('current')
invPhysIsFRU = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysIsFRU.setStatus('current')
invPhysSoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 15), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysSoftwareRev.setStatus('current')
invPhysSoftwareProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 16), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysSoftwareProduct.setStatus('current')
invPhysClei = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysClei.setStatus('current')
invPhysAid = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invPhysAid.setStatus('current')
invGeneralLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralLastChangeTime.setStatus('current')
invGeneralTestAndIncr = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: invGeneralTestAndIncr.setStatus('current')
invGeneralMibSpecVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: invGeneralMibSpecVersion.setStatus('current')
invGeneralMibImplVersion = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: invGeneralMibImplVersion.setStatus('current')
invGeneralConfigLastChangeTime = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralConfigLastChangeTime.setStatus('current')
invGeneralPhysTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralPhysTableSize.setStatus('current')
invGeneralEntityTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralEntityTableSize.setStatus('current')
invGeneralRelationTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralRelationTableSize.setStatus('current')
invGeneralInsRemTableSize = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralInsRemTableSize.setStatus('current')
invGeneralInsRemLastSeqNumber = MibScalar((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invGeneralInsRemLastSeqNumber.setStatus('current')
invNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3, 0))
invNotificationPhysAdded = NotificationType((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3, 0, 1)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysVendorType"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"))
if mibBuilder.loadTexts: invNotificationPhysAdded.setStatus('current')
invNotificationPhysRemoved = NotificationType((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3, 0, 2)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysVendorType"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"))
if mibBuilder.loadTexts: invNotificationPhysRemoved.setStatus('current')
invEntityTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1), )
if mibBuilder.loadTexts: invEntityTable.setStatus('current')
invEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1), ).setIndexNames((0, "LUM-INVENTORY-MIB", "invEntityIndex"))
if mibBuilder.loadTexts: invEntityEntry.setStatus('current')
invEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invEntityIndex.setStatus('current')
invEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invEntityName.setStatus('current')
invEntityObject = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 3), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invEntityObject.setStatus('current')
invEntityClass = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 4), EntityClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invEntityClass.setStatus('current')
invRelationTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1), )
if mibBuilder.loadTexts: invRelationTable.setStatus('current')
invRelationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1), ).setIndexNames((0, "LUM-INVENTORY-MIB", "invRelationIndex"))
if mibBuilder.loadTexts: invRelationEntry.setStatus('current')
invRelationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invRelationIndex.setStatus('current')
invRelationEntityIndex1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invRelationEntityIndex1.setStatus('current')
invRelationEntityName1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 3), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invRelationEntityName1.setStatus('current')
invRelationType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("containedIn", 1), ("dependsOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invRelationType.setStatus('current')
invRelationEntityIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invRelationEntityIndex2.setStatus('current')
invRelationEntityName2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 6), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invRelationEntityName2.setStatus('current')
invInsRemTable = MibTable((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1), )
if mibBuilder.loadTexts: invInsRemTable.setStatus('current')
invInsRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1), ).setIndexNames((0, "LUM-INVENTORY-MIB", "invInsRemIndex"))
if mibBuilder.loadTexts: invInsRemEntry.setStatus('current')
invInsRemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemIndex.setStatus('current')
invInsRemName = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 2), MgmtNameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemName.setStatus('current')
invInsRemEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 3), InsRemEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemEvent.setStatus('current')
invInsRemTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemTimestamp.setStatus('current')
invInsRemEquipmentType = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 5), PhysicalClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemEquipmentType.setStatus('current')
invInsRemPhysicalLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemPhysicalLocation.setStatus('current')
invInsRemClei = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemClei.setStatus('current')
invInsRemSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemSerialNumber.setStatus('current')
invInsRemPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemPartNumber.setStatus('current')
invInsRemSeqNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: invInsRemSeqNumber.setStatus('current')
invPhysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 1)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysVendorType"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invPhysGroup = invPhysGroup.setStatus('deprecated')
invGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 2)).setObjects(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralMibSpecVersion"), ("LUM-INVENTORY-MIB", "invGeneralMibImplVersion"), ("LUM-INVENTORY-MIB", "invGeneralTestAndIncr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invGeneralGroup = invGeneralGroup.setStatus('deprecated')
invEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 3)).setObjects(("LUM-INVENTORY-MIB", "invNotificationPhysAdded"), ("LUM-INVENTORY-MIB", "invNotificationPhysRemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invEventGroup = invEventGroup.setStatus('current')
invGeneralGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 4)).setObjects(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invGeneralGroupV2 = invGeneralGroupV2.setStatus('deprecated')
invPhysGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 5)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysVendorType"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"), ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invPhysGroupV2 = invPhysGroupV2.setStatus('deprecated')
invPhysGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 6)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysVendorType"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"), ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"), ("LUM-INVENTORY-MIB", "invPhysSoftwareProduct"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invPhysGroupV3 = invPhysGroupV3.setStatus('deprecated')
invEntityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 7)).setObjects(("LUM-INVENTORY-MIB", "invEntityIndex"), ("LUM-INVENTORY-MIB", "invEntityName"), ("LUM-INVENTORY-MIB", "invEntityObject"), ("LUM-INVENTORY-MIB", "invEntityClass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invEntityGroup = invEntityGroup.setStatus('current')
invRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 8)).setObjects(("LUM-INVENTORY-MIB", "invRelationIndex"), ("LUM-INVENTORY-MIB", "invRelationEntityIndex1"), ("LUM-INVENTORY-MIB", "invRelationEntityName1"), ("LUM-INVENTORY-MIB", "invRelationType"), ("LUM-INVENTORY-MIB", "invRelationEntityIndex2"), ("LUM-INVENTORY-MIB", "invRelationEntityName2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invRelationGroup = invRelationGroup.setStatus('current')
invGeneralGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 9)).setObjects(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invGeneralGroupV3 = invGeneralGroupV3.setStatus('deprecated')
invGeneralGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 10)).setObjects(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralPhysTableSize"), ("LUM-INVENTORY-MIB", "invGeneralEntityTableSize"), ("LUM-INVENTORY-MIB", "invGeneralRelationTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invGeneralGroupV4 = invGeneralGroupV4.setStatus('deprecated')
invPhysGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 11)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"), ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"), ("LUM-INVENTORY-MIB", "invPhysSoftwareProduct"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invPhysGroupV4 = invPhysGroupV4.setStatus('deprecated')
invPhysGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 12)).setObjects(("LUM-INVENTORY-MIB", "invPhysIndex"), ("LUM-INVENTORY-MIB", "invPhysDescr"), ("LUM-INVENTORY-MIB", "invPhysContainedIn"), ("LUM-INVENTORY-MIB", "invPhysClass"), ("LUM-INVENTORY-MIB", "invPhysParentRelPos"), ("LUM-INVENTORY-MIB", "invPhysName"), ("LUM-INVENTORY-MIB", "invPhysHardwareRev"), ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"), ("LUM-INVENTORY-MIB", "invPhysProductDataRev"), ("LUM-INVENTORY-MIB", "invPhysSerialNum"), ("LUM-INVENTORY-MIB", "invPhysMfgName"), ("LUM-INVENTORY-MIB", "invPhysModelName"), ("LUM-INVENTORY-MIB", "invPhysIsFRU"), ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"), ("LUM-INVENTORY-MIB", "invPhysSoftwareProduct"), ("LUM-INVENTORY-MIB", "invPhysClei"), ("LUM-INVENTORY-MIB", "invPhysAid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invPhysGroupV5 = invPhysGroupV5.setStatus('current')
invInsRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 13)).setObjects(("LUM-INVENTORY-MIB", "invInsRemIndex"), ("LUM-INVENTORY-MIB", "invInsRemName"), ("LUM-INVENTORY-MIB", "invInsRemEvent"), ("LUM-INVENTORY-MIB", "invInsRemTimestamp"), ("LUM-INVENTORY-MIB", "invInsRemEquipmentType"), ("LUM-INVENTORY-MIB", "invInsRemPhysicalLocation"), ("LUM-INVENTORY-MIB", "invInsRemClei"), ("LUM-INVENTORY-MIB", "invInsRemSerialNumber"), ("LUM-INVENTORY-MIB", "invInsRemPartNumber"), ("LUM-INVENTORY-MIB", "invInsRemSeqNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invInsRemGroup = invInsRemGroup.setStatus('current')
invGeneralGroupV5 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 14)).setObjects(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralPhysTableSize"), ("LUM-INVENTORY-MIB", "invGeneralEntityTableSize"), ("LUM-INVENTORY-MIB", "invGeneralRelationTableSize"), ("LUM-INVENTORY-MIB", "invGeneralInsRemTableSize"), ("LUM-INVENTORY-MIB", "invGeneralInsRemLastSeqNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    invGeneralGroupV5 = invGeneralGroupV5.setStatus('current')
lumInventoryBasicComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 1)).setObjects(("LUM-INVENTORY-MIB", "invPhysGroup"), ("LUM-INVENTORY-MIB", "invGeneralGroup"), ("LUM-INVENTORY-MIB", "invEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV1 = lumInventoryBasicComplV1.setStatus('deprecated')
lumInventoryBasicComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 2)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV2"), ("LUM-INVENTORY-MIB", "invPhysGroup"), ("LUM-INVENTORY-MIB", "invEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV2 = lumInventoryBasicComplV2.setStatus('deprecated')
lumInventoryBasicComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 3)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV2"), ("LUM-INVENTORY-MIB", "invPhysGroupV2"), ("LUM-INVENTORY-MIB", "invEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV3 = lumInventoryBasicComplV3.setStatus('deprecated')
lumInventoryBasicComplV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 4)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV2"), ("LUM-INVENTORY-MIB", "invPhysGroupV3"), ("LUM-INVENTORY-MIB", "invEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV4 = lumInventoryBasicComplV4.setStatus('deprecated')
lumInventoryBasicComplV5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 5)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV2"), ("LUM-INVENTORY-MIB", "invPhysGroupV3"), ("LUM-INVENTORY-MIB", "invEventGroup"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV5 = lumInventoryBasicComplV5.setStatus('deprecated')
lumInventoryBasicComplV6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 6)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV3"), ("LUM-INVENTORY-MIB", "invPhysGroupV3"), ("LUM-INVENTORY-MIB", "invEventGroup"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV6 = lumInventoryBasicComplV6.setStatus('deprecated')
lumInventoryBasicComplV7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 7)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV4"), ("LUM-INVENTORY-MIB", "invPhysGroupV3"), ("LUM-INVENTORY-MIB", "invEventGroup"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV7 = lumInventoryBasicComplV7.setStatus('deprecated')
lumInventoryBasicComplV8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 8)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV4"), ("LUM-INVENTORY-MIB", "invPhysGroupV4"), ("LUM-INVENTORY-MIB", "invEventGroup"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV8 = lumInventoryBasicComplV8.setStatus('deprecated')
lumInventoryBasicComplV9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 9)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV4"), ("LUM-INVENTORY-MIB", "invPhysGroupV5"), ("LUM-INVENTORY-MIB", "invEventGroup"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV9 = lumInventoryBasicComplV9.setStatus('deprecated')
lumInventoryBasicComplV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 10)).setObjects(("LUM-INVENTORY-MIB", "invGeneralGroupV5"), ("LUM-INVENTORY-MIB", "invPhysGroupV5"), ("LUM-INVENTORY-MIB", "invEventGroup"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"), ("LUM-INVENTORY-MIB", "invInsRemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryBasicComplV10 = lumInventoryBasicComplV10.setStatus('current')
inventoryGeneralMinimalGroupV1 = ObjectGroup((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 3, 1)).setObjects(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"), ("LUM-INVENTORY-MIB", "invGeneralPhysTableSize"), ("LUM-INVENTORY-MIB", "invGeneralEntityTableSize"), ("LUM-INVENTORY-MIB", "invGeneralRelationTableSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    inventoryGeneralMinimalGroupV1 = inventoryGeneralMinimalGroupV1.setStatus('current')
lumInventoryMinimalComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4, 1)).setObjects(("LUM-INVENTORY-MIB", "inventoryGeneralMinimalGroupV1"), ("LUM-INVENTORY-MIB", "invPhysGroupV3"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryMinimalComplV1 = lumInventoryMinimalComplV1.setStatus('deprecated')
lumInventoryMinimalComplV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4, 2)).setObjects(("LUM-INVENTORY-MIB", "inventoryGeneralMinimalGroupV1"), ("LUM-INVENTORY-MIB", "invPhysGroupV4"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryMinimalComplV2 = lumInventoryMinimalComplV2.setStatus('deprecated')
lumInventoryMinimalComplV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4, 3)).setObjects(("LUM-INVENTORY-MIB", "inventoryGeneralMinimalGroupV1"), ("LUM-INVENTORY-MIB", "invPhysGroupV5"), ("LUM-INVENTORY-MIB", "invEntityGroup"), ("LUM-INVENTORY-MIB", "invRelationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lumInventoryMinimalComplV3 = lumInventoryMinimalComplV3.setStatus('current')
mibBuilder.exportSymbols("LUM-INVENTORY-MIB", lumInventoryMIBModule=lumInventoryMIBModule, invPhysAid=invPhysAid, invGeneralGroupV2=invGeneralGroupV2, invInsRemName=invInsRemName, lumInventoryMinimalComplV1=lumInventoryMinimalComplV1, invPhysDescr=invPhysDescr, EntityClass=EntityClass, invPhysical=invPhysical, invInsRemSeqNumber=invInsRemSeqNumber, invPhysGroupV2=invPhysGroupV2, invRelationTable=invRelationTable, invPhysProductDataRev=invPhysProductDataRev, invGeneralTestAndIncr=invGeneralTestAndIncr, lumInventoryBasicComplV3=lumInventoryBasicComplV3, lumentisInvNotifications=lumentisInvNotifications, PYSNMP_MODULE_ID=lumInventoryMIBModule, invGeneralInsRemTableSize=invGeneralInsRemTableSize, invRelationEntry=invRelationEntry, lumInventoryBasicComplV5=lumInventoryBasicComplV5, invGeneralPhysTableSize=invGeneralPhysTableSize, invEntityEntry=invEntityEntry, lumInventoryBasicComplV6=lumInventoryBasicComplV6, lumInventoryBasicComplV9=lumInventoryBasicComplV9, invPhysClass=invPhysClass, invPhysSerialNum=invPhysSerialNum, invGeneralGroupV4=invGeneralGroupV4, lumInventoryMIBObjects=lumInventoryMIBObjects, invEventGroup=invEventGroup, invPhysFirmwareRev=invPhysFirmwareRev, invGeneralMibSpecVersion=invGeneralMibSpecVersion, lumInventoryCompl=lumInventoryCompl, invRelationIndex=invRelationIndex, invPhysTable=invPhysTable, inventoryGeneralMinimalGroupV1=inventoryGeneralMinimalGroupV1, invInsRemPartNumber=invInsRemPartNumber, invPhysParentRelPos=invPhysParentRelPos, invInsRemPhysicalLocation=invInsRemPhysicalLocation, invPhysGroupV5=invPhysGroupV5, invGeneralGroup=invGeneralGroup, invNotificationPhysRemoved=invNotificationPhysRemoved, PhysicalClass=PhysicalClass, invEntityGroup=invEntityGroup, invGeneralMibImplVersion=invGeneralMibImplVersion, invGeneralGroupV5=invGeneralGroupV5, InsRemEventType=InsRemEventType, lumInventoryBasicComplV2=lumInventoryBasicComplV2, invEntityName=invEntityName, invGeneralInsRemLastSeqNumber=invGeneralInsRemLastSeqNumber, invPhysGroup=invPhysGroup, invGeneral=invGeneral, invInsRemEvent=invInsRemEvent, invEntityClass=invEntityClass, invPhysIsFRU=invPhysIsFRU, lumInventoryBasicComplV10=lumInventoryBasicComplV10, invInsRemEntry=invInsRemEntry, invGeneralEntityTableSize=invGeneralEntityTableSize, lumInventoryBasicComplV7=lumInventoryBasicComplV7, invRelations=invRelations, invGeneralGroupV3=invGeneralGroupV3, invInsRemEquipmentType=invInsRemEquipmentType, invPhysHardwareRev=invPhysHardwareRev, lumInventoryMinimalComplV3=lumInventoryMinimalComplV3, invPhysClei=invPhysClei, invPhysVendorType=invPhysVendorType, invPhysModelName=invPhysModelName, invPhysContainedIn=invPhysContainedIn, lumInventoryConfs=lumInventoryConfs, invEntityTable=invEntityTable, lumInventoryBasicComplV1=lumInventoryBasicComplV1, invInsRemClei=invInsRemClei, invPhysSoftwareProduct=invPhysSoftwareProduct, invRelationEntityName1=invRelationEntityName1, invEntityIndex=invEntityIndex, invRelationEntityIndex1=invRelationEntityIndex1, lumInventoryBasicComplV8=lumInventoryBasicComplV8, invEntityObject=invEntityObject, invGeneralConfigLastChangeTime=invGeneralConfigLastChangeTime, invRelationEntityIndex2=invRelationEntityIndex2, lumInventoryMinimalCompl=lumInventoryMinimalCompl, invPhysGroupV4=invPhysGroupV4, invNotifyPrefix=invNotifyPrefix, lumInventoryGroups=lumInventoryGroups, invInsRemIndex=invInsRemIndex, invPhysEntry=invPhysEntry, invRelationType=invRelationType, lumInventoryMinimalComplV2=lumInventoryMinimalComplV2, lumInventoryBasicComplV4=lumInventoryBasicComplV4, invRelationGroup=invRelationGroup, invNotificationPhysAdded=invNotificationPhysAdded, invPhysIndex=invPhysIndex, invEntities=invEntities, invGeneralLastChangeTime=invGeneralLastChangeTime, invPhysGroupV3=invPhysGroupV3, invPhysMfgName=invPhysMfgName, invInsRemTimestamp=invInsRemTimestamp, lumInventoryMinimalGroups=lumInventoryMinimalGroups, invInsRemSerialNumber=invInsRemSerialNumber, invInsRemLog=invInsRemLog, invPhysName=invPhysName, invGeneralRelationTableSize=invGeneralRelationTableSize, invInsRemTable=invInsRemTable, invInsRemGroup=invInsRemGroup, invRelationEntityName2=invRelationEntityName2, invPhysSoftwareRev=invPhysSoftwareRev)
