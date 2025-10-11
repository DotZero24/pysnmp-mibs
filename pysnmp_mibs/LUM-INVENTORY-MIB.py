# SNMP MIB module (LUM-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:03 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(lumInventoryMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumInventoryMIB",
    "lumModules")

(MgmtNameString,) = mibBuilder.importSymbols(
    "LUM-TC",
    "MgmtNameString")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

lumInventoryMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lumInventoryMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2014-09-30 00:00",
         "2005-09-14 00:00",
         "2004-09-30 00:00",
         "2002-03-08 00:00",
         "2001-10-30 00:00",
         "2001-07-17 00:00",
         "2001-05-11 00:00",
         "2001-05-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PhysicalClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("port", 10),
          ("stack", 11))
    )



class EntityClass(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("other", 1),
          ("unknown", 2),
          ("chassis", 3),
          ("backplane", 4),
          ("container", 5),
          ("powerSupply", 6),
          ("fan", 7),
          ("sensor", 8),
          ("module", 9),
          ("port", 10),
          ("stack", 11),
          ("logical", 12))
    )



class InsRemEventType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 0),
          ("remove", 1))
    )



# MIB Managed Objects in the order of their OIDs

_LumInventoryConfs_ObjectIdentity = ObjectIdentity
lumInventoryConfs = _LumInventoryConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1)
)
_LumInventoryGroups_ObjectIdentity = ObjectIdentity
lumInventoryGroups = _LumInventoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1)
)
_LumInventoryCompl_ObjectIdentity = ObjectIdentity
lumInventoryCompl = _LumInventoryCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2)
)
_LumInventoryMinimalGroups_ObjectIdentity = ObjectIdentity
lumInventoryMinimalGroups = _LumInventoryMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 3)
)
_LumInventoryMinimalCompl_ObjectIdentity = ObjectIdentity
lumInventoryMinimalCompl = _LumInventoryMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4)
)
_LumInventoryMIBObjects_ObjectIdentity = ObjectIdentity
lumInventoryMIBObjects = _LumInventoryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2)
)
_InvPhysical_ObjectIdentity = ObjectIdentity
invPhysical = _InvPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1)
)
_InvPhysTable_Object = MibTable
invPhysTable = _InvPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    invPhysTable.setStatus("current")
_InvPhysEntry_Object = MibTableRow
invPhysEntry = _InvPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1)
)
invPhysEntry.setIndexNames(
    (0, "LUM-INVENTORY-MIB", "invPhysIndex"),
)
if mibBuilder.loadTexts:
    invPhysEntry.setStatus("current")


class _InvPhysIndex_Type(Unsigned32):
    """Custom type invPhysIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InvPhysIndex_Type.__name__ = "Unsigned32"
_InvPhysIndex_Object = MibTableColumn
invPhysIndex = _InvPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 1),
    _InvPhysIndex_Type()
)
invPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysIndex.setStatus("current")
_InvPhysDescr_Type = SnmpAdminString
_InvPhysDescr_Object = MibTableColumn
invPhysDescr = _InvPhysDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 2),
    _InvPhysDescr_Type()
)
invPhysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysDescr.setStatus("current")
_InvPhysVendorType_Type = AutonomousType
_InvPhysVendorType_Object = MibTableColumn
invPhysVendorType = _InvPhysVendorType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 3),
    _InvPhysVendorType_Type()
)
invPhysVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysVendorType.setStatus("deprecated")


class _InvPhysContainedIn_Type(Unsigned32):
    """Custom type invPhysContainedIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InvPhysContainedIn_Type.__name__ = "Unsigned32"
_InvPhysContainedIn_Object = MibTableColumn
invPhysContainedIn = _InvPhysContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 4),
    _InvPhysContainedIn_Type()
)
invPhysContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysContainedIn.setStatus("current")
_InvPhysClass_Type = PhysicalClass
_InvPhysClass_Object = MibTableColumn
invPhysClass = _InvPhysClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 5),
    _InvPhysClass_Type()
)
invPhysClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysClass.setStatus("current")


class _InvPhysParentRelPos_Type(Integer32):
    """Custom type invPhysParentRelPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_InvPhysParentRelPos_Type.__name__ = "Integer32"
_InvPhysParentRelPos_Object = MibTableColumn
invPhysParentRelPos = _InvPhysParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 6),
    _InvPhysParentRelPos_Type()
)
invPhysParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysParentRelPos.setStatus("current")
_InvPhysName_Type = MgmtNameString
_InvPhysName_Object = MibTableColumn
invPhysName = _InvPhysName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 7),
    _InvPhysName_Type()
)
invPhysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysName.setStatus("current")
_InvPhysHardwareRev_Type = SnmpAdminString
_InvPhysHardwareRev_Object = MibTableColumn
invPhysHardwareRev = _InvPhysHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 8),
    _InvPhysHardwareRev_Type()
)
invPhysHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysHardwareRev.setStatus("current")
_InvPhysFirmwareRev_Type = SnmpAdminString
_InvPhysFirmwareRev_Object = MibTableColumn
invPhysFirmwareRev = _InvPhysFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 9),
    _InvPhysFirmwareRev_Type()
)
invPhysFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysFirmwareRev.setStatus("current")
_InvPhysProductDataRev_Type = SnmpAdminString
_InvPhysProductDataRev_Object = MibTableColumn
invPhysProductDataRev = _InvPhysProductDataRev_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 10),
    _InvPhysProductDataRev_Type()
)
invPhysProductDataRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysProductDataRev.setStatus("current")


class _InvPhysSerialNum_Type(SnmpAdminString):
    """Custom type invPhysSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InvPhysSerialNum_Type.__name__ = "SnmpAdminString"
_InvPhysSerialNum_Object = MibTableColumn
invPhysSerialNum = _InvPhysSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 11),
    _InvPhysSerialNum_Type()
)
invPhysSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysSerialNum.setStatus("current")
_InvPhysMfgName_Type = SnmpAdminString
_InvPhysMfgName_Object = MibTableColumn
invPhysMfgName = _InvPhysMfgName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 12),
    _InvPhysMfgName_Type()
)
invPhysMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysMfgName.setStatus("current")
_InvPhysModelName_Type = SnmpAdminString
_InvPhysModelName_Object = MibTableColumn
invPhysModelName = _InvPhysModelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 13),
    _InvPhysModelName_Type()
)
invPhysModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysModelName.setStatus("current")
_InvPhysIsFRU_Type = TruthValue
_InvPhysIsFRU_Object = MibTableColumn
invPhysIsFRU = _InvPhysIsFRU_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 14),
    _InvPhysIsFRU_Type()
)
invPhysIsFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysIsFRU.setStatus("current")
_InvPhysSoftwareRev_Type = SnmpAdminString
_InvPhysSoftwareRev_Object = MibTableColumn
invPhysSoftwareRev = _InvPhysSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 15),
    _InvPhysSoftwareRev_Type()
)
invPhysSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysSoftwareRev.setStatus("current")
_InvPhysSoftwareProduct_Type = SnmpAdminString
_InvPhysSoftwareProduct_Object = MibTableColumn
invPhysSoftwareProduct = _InvPhysSoftwareProduct_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 16),
    _InvPhysSoftwareProduct_Type()
)
invPhysSoftwareProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysSoftwareProduct.setStatus("current")


class _InvPhysClei_Type(DisplayString):
    """Custom type invPhysClei based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InvPhysClei_Type.__name__ = "DisplayString"
_InvPhysClei_Object = MibTableColumn
invPhysClei = _InvPhysClei_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 17),
    _InvPhysClei_Type()
)
invPhysClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysClei.setStatus("current")
_InvPhysAid_Type = DisplayString
_InvPhysAid_Object = MibTableColumn
invPhysAid = _InvPhysAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 1, 1, 1, 18),
    _InvPhysAid_Type()
)
invPhysAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invPhysAid.setStatus("current")
_InvGeneral_ObjectIdentity = ObjectIdentity
invGeneral = _InvGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2)
)
_InvGeneralLastChangeTime_Type = DateAndTime
_InvGeneralLastChangeTime_Object = MibScalar
invGeneralLastChangeTime = _InvGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 1),
    _InvGeneralLastChangeTime_Type()
)
invGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralLastChangeTime.setStatus("current")
_InvGeneralTestAndIncr_Type = TestAndIncr
_InvGeneralTestAndIncr_Object = MibScalar
invGeneralTestAndIncr = _InvGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 2),
    _InvGeneralTestAndIncr_Type()
)
invGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invGeneralTestAndIncr.setStatus("current")


class _InvGeneralMibSpecVersion_Type(DisplayString):
    """Custom type invGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_InvGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_InvGeneralMibSpecVersion_Object = MibScalar
invGeneralMibSpecVersion = _InvGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 3),
    _InvGeneralMibSpecVersion_Type()
)
invGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invGeneralMibSpecVersion.setStatus("current")


class _InvGeneralMibImplVersion_Type(DisplayString):
    """Custom type invGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_InvGeneralMibImplVersion_Type.__name__ = "DisplayString"
_InvGeneralMibImplVersion_Object = MibScalar
invGeneralMibImplVersion = _InvGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 4),
    _InvGeneralMibImplVersion_Type()
)
invGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invGeneralMibImplVersion.setStatus("current")
_InvGeneralConfigLastChangeTime_Type = DateAndTime
_InvGeneralConfigLastChangeTime_Object = MibScalar
invGeneralConfigLastChangeTime = _InvGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 5),
    _InvGeneralConfigLastChangeTime_Type()
)
invGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralConfigLastChangeTime.setStatus("current")
_InvGeneralPhysTableSize_Type = Unsigned32
_InvGeneralPhysTableSize_Object = MibScalar
invGeneralPhysTableSize = _InvGeneralPhysTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 6),
    _InvGeneralPhysTableSize_Type()
)
invGeneralPhysTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralPhysTableSize.setStatus("current")
_InvGeneralEntityTableSize_Type = Unsigned32
_InvGeneralEntityTableSize_Object = MibScalar
invGeneralEntityTableSize = _InvGeneralEntityTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 7),
    _InvGeneralEntityTableSize_Type()
)
invGeneralEntityTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralEntityTableSize.setStatus("current")
_InvGeneralRelationTableSize_Type = Unsigned32
_InvGeneralRelationTableSize_Object = MibScalar
invGeneralRelationTableSize = _InvGeneralRelationTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 8),
    _InvGeneralRelationTableSize_Type()
)
invGeneralRelationTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralRelationTableSize.setStatus("current")
_InvGeneralInsRemTableSize_Type = Unsigned32
_InvGeneralInsRemTableSize_Object = MibScalar
invGeneralInsRemTableSize = _InvGeneralInsRemTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 9),
    _InvGeneralInsRemTableSize_Type()
)
invGeneralInsRemTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralInsRemTableSize.setStatus("current")
_InvGeneralInsRemLastSeqNumber_Type = Counter32
_InvGeneralInsRemLastSeqNumber_Object = MibScalar
invGeneralInsRemLastSeqNumber = _InvGeneralInsRemLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 2, 10),
    _InvGeneralInsRemLastSeqNumber_Type()
)
invGeneralInsRemLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invGeneralInsRemLastSeqNumber.setStatus("current")
_LumentisInvNotifications_ObjectIdentity = ObjectIdentity
lumentisInvNotifications = _LumentisInvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3)
)
_InvNotifyPrefix_ObjectIdentity = ObjectIdentity
invNotifyPrefix = _InvNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3, 0)
)
_InvEntities_ObjectIdentity = ObjectIdentity
invEntities = _InvEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4)
)
_InvEntityTable_Object = MibTable
invEntityTable = _InvEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    invEntityTable.setStatus("current")
_InvEntityEntry_Object = MibTableRow
invEntityEntry = _InvEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1)
)
invEntityEntry.setIndexNames(
    (0, "LUM-INVENTORY-MIB", "invEntityIndex"),
)
if mibBuilder.loadTexts:
    invEntityEntry.setStatus("current")


class _InvEntityIndex_Type(Unsigned32):
    """Custom type invEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InvEntityIndex_Type.__name__ = "Unsigned32"
_InvEntityIndex_Object = MibTableColumn
invEntityIndex = _InvEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 1),
    _InvEntityIndex_Type()
)
invEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invEntityIndex.setStatus("current")
_InvEntityName_Type = MgmtNameString
_InvEntityName_Object = MibTableColumn
invEntityName = _InvEntityName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 2),
    _InvEntityName_Type()
)
invEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invEntityName.setStatus("current")
_InvEntityObject_Type = RowPointer
_InvEntityObject_Object = MibTableColumn
invEntityObject = _InvEntityObject_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 3),
    _InvEntityObject_Type()
)
invEntityObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invEntityObject.setStatus("current")
_InvEntityClass_Type = EntityClass
_InvEntityClass_Object = MibTableColumn
invEntityClass = _InvEntityClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 4, 1, 1, 4),
    _InvEntityClass_Type()
)
invEntityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invEntityClass.setStatus("current")
_InvRelations_ObjectIdentity = ObjectIdentity
invRelations = _InvRelations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5)
)
_InvRelationTable_Object = MibTable
invRelationTable = _InvRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    invRelationTable.setStatus("current")
_InvRelationEntry_Object = MibTableRow
invRelationEntry = _InvRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1)
)
invRelationEntry.setIndexNames(
    (0, "LUM-INVENTORY-MIB", "invRelationIndex"),
)
if mibBuilder.loadTexts:
    invRelationEntry.setStatus("current")


class _InvRelationIndex_Type(Unsigned32):
    """Custom type invRelationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InvRelationIndex_Type.__name__ = "Unsigned32"
_InvRelationIndex_Object = MibTableColumn
invRelationIndex = _InvRelationIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 1),
    _InvRelationIndex_Type()
)
invRelationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invRelationIndex.setStatus("current")


class _InvRelationEntityIndex1_Type(Unsigned32):
    """Custom type invRelationEntityIndex1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InvRelationEntityIndex1_Type.__name__ = "Unsigned32"
_InvRelationEntityIndex1_Object = MibTableColumn
invRelationEntityIndex1 = _InvRelationEntityIndex1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 2),
    _InvRelationEntityIndex1_Type()
)
invRelationEntityIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invRelationEntityIndex1.setStatus("current")
_InvRelationEntityName1_Type = MgmtNameString
_InvRelationEntityName1_Object = MibTableColumn
invRelationEntityName1 = _InvRelationEntityName1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 3),
    _InvRelationEntityName1_Type()
)
invRelationEntityName1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invRelationEntityName1.setStatus("current")


class _InvRelationType_Type(Integer32):
    """Custom type invRelationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("containedIn", 1),
          ("dependsOn", 2))
    )


_InvRelationType_Type.__name__ = "Integer32"
_InvRelationType_Object = MibTableColumn
invRelationType = _InvRelationType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 4),
    _InvRelationType_Type()
)
invRelationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invRelationType.setStatus("current")


class _InvRelationEntityIndex2_Type(Unsigned32):
    """Custom type invRelationEntityIndex2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InvRelationEntityIndex2_Type.__name__ = "Unsigned32"
_InvRelationEntityIndex2_Object = MibTableColumn
invRelationEntityIndex2 = _InvRelationEntityIndex2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 5),
    _InvRelationEntityIndex2_Type()
)
invRelationEntityIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invRelationEntityIndex2.setStatus("current")
_InvRelationEntityName2_Type = MgmtNameString
_InvRelationEntityName2_Object = MibTableColumn
invRelationEntityName2 = _InvRelationEntityName2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 5, 1, 1, 6),
    _InvRelationEntityName2_Type()
)
invRelationEntityName2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invRelationEntityName2.setStatus("current")
_InvInsRemLog_ObjectIdentity = ObjectIdentity
invInsRemLog = _InvInsRemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6)
)
_InvInsRemTable_Object = MibTable
invInsRemTable = _InvInsRemTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    invInsRemTable.setStatus("current")
_InvInsRemEntry_Object = MibTableRow
invInsRemEntry = _InvInsRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1)
)
invInsRemEntry.setIndexNames(
    (0, "LUM-INVENTORY-MIB", "invInsRemIndex"),
)
if mibBuilder.loadTexts:
    invInsRemEntry.setStatus("current")


class _InvInsRemIndex_Type(Unsigned32):
    """Custom type invInsRemIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InvInsRemIndex_Type.__name__ = "Unsigned32"
_InvInsRemIndex_Object = MibTableColumn
invInsRemIndex = _InvInsRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 1),
    _InvInsRemIndex_Type()
)
invInsRemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemIndex.setStatus("current")
_InvInsRemName_Type = MgmtNameString
_InvInsRemName_Object = MibTableColumn
invInsRemName = _InvInsRemName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 2),
    _InvInsRemName_Type()
)
invInsRemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemName.setStatus("current")
_InvInsRemEvent_Type = InsRemEventType
_InvInsRemEvent_Object = MibTableColumn
invInsRemEvent = _InvInsRemEvent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 3),
    _InvInsRemEvent_Type()
)
invInsRemEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemEvent.setStatus("current")
_InvInsRemTimestamp_Type = DateAndTime
_InvInsRemTimestamp_Object = MibTableColumn
invInsRemTimestamp = _InvInsRemTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 4),
    _InvInsRemTimestamp_Type()
)
invInsRemTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemTimestamp.setStatus("current")
_InvInsRemEquipmentType_Type = PhysicalClass
_InvInsRemEquipmentType_Object = MibTableColumn
invInsRemEquipmentType = _InvInsRemEquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 5),
    _InvInsRemEquipmentType_Type()
)
invInsRemEquipmentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemEquipmentType.setStatus("current")


class _InvInsRemPhysicalLocation_Type(DisplayString):
    """Custom type invInsRemPhysicalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InvInsRemPhysicalLocation_Type.__name__ = "DisplayString"
_InvInsRemPhysicalLocation_Object = MibTableColumn
invInsRemPhysicalLocation = _InvInsRemPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 6),
    _InvInsRemPhysicalLocation_Type()
)
invInsRemPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemPhysicalLocation.setStatus("current")


class _InvInsRemClei_Type(DisplayString):
    """Custom type invInsRemClei based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InvInsRemClei_Type.__name__ = "DisplayString"
_InvInsRemClei_Object = MibTableColumn
invInsRemClei = _InvInsRemClei_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 7),
    _InvInsRemClei_Type()
)
invInsRemClei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemClei.setStatus("current")


class _InvInsRemSerialNumber_Type(DisplayString):
    """Custom type invInsRemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InvInsRemSerialNumber_Type.__name__ = "DisplayString"
_InvInsRemSerialNumber_Object = MibTableColumn
invInsRemSerialNumber = _InvInsRemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 8),
    _InvInsRemSerialNumber_Type()
)
invInsRemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemSerialNumber.setStatus("current")
_InvInsRemPartNumber_Type = DisplayString
_InvInsRemPartNumber_Object = MibTableColumn
invInsRemPartNumber = _InvInsRemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 9),
    _InvInsRemPartNumber_Type()
)
invInsRemPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemPartNumber.setStatus("current")
_InvInsRemSeqNumber_Type = Counter32
_InvInsRemSeqNumber_Object = MibTableColumn
invInsRemSeqNumber = _InvInsRemSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 6, 1, 1, 10),
    _InvInsRemSeqNumber_Type()
)
invInsRemSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invInsRemSeqNumber.setStatus("current")

# Managed Objects groups

invPhysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 1)
)
invPhysGroup.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysVendorType"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"))
)
if mibBuilder.loadTexts:
    invPhysGroup.setStatus("deprecated")

invGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 2)
)
invGeneralGroup.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralMibSpecVersion"),
        ("LUM-INVENTORY-MIB", "invGeneralMibImplVersion"),
        ("LUM-INVENTORY-MIB", "invGeneralTestAndIncr"))
)
if mibBuilder.loadTexts:
    invGeneralGroup.setStatus("deprecated")

invGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 4)
)
invGeneralGroupV2.setObjects(
    ("LUM-INVENTORY-MIB", "invGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    invGeneralGroupV2.setStatus("deprecated")

invPhysGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 5)
)
invPhysGroupV2.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysVendorType"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"))
)
if mibBuilder.loadTexts:
    invPhysGroupV2.setStatus("deprecated")

invPhysGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 6)
)
invPhysGroupV3.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysVendorType"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareProduct"))
)
if mibBuilder.loadTexts:
    invPhysGroupV3.setStatus("deprecated")

invEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 7)
)
invEntityGroup.setObjects(
      *(("LUM-INVENTORY-MIB", "invEntityIndex"),
        ("LUM-INVENTORY-MIB", "invEntityName"),
        ("LUM-INVENTORY-MIB", "invEntityObject"),
        ("LUM-INVENTORY-MIB", "invEntityClass"))
)
if mibBuilder.loadTexts:
    invEntityGroup.setStatus("current")

invRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 8)
)
invRelationGroup.setObjects(
      *(("LUM-INVENTORY-MIB", "invRelationIndex"),
        ("LUM-INVENTORY-MIB", "invRelationEntityIndex1"),
        ("LUM-INVENTORY-MIB", "invRelationEntityName1"),
        ("LUM-INVENTORY-MIB", "invRelationType"),
        ("LUM-INVENTORY-MIB", "invRelationEntityIndex2"),
        ("LUM-INVENTORY-MIB", "invRelationEntityName2"))
)
if mibBuilder.loadTexts:
    invRelationGroup.setStatus("current")

invGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 9)
)
invGeneralGroupV3.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    invGeneralGroupV3.setStatus("deprecated")

invGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 10)
)
invGeneralGroupV4.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralPhysTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralEntityTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralRelationTableSize"))
)
if mibBuilder.loadTexts:
    invGeneralGroupV4.setStatus("deprecated")

invPhysGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 11)
)
invPhysGroupV4.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareProduct"))
)
if mibBuilder.loadTexts:
    invPhysGroupV4.setStatus("deprecated")

invPhysGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 12)
)
invPhysGroupV5.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysSoftwareProduct"),
        ("LUM-INVENTORY-MIB", "invPhysClei"),
        ("LUM-INVENTORY-MIB", "invPhysAid"))
)
if mibBuilder.loadTexts:
    invPhysGroupV5.setStatus("current")

invInsRemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 13)
)
invInsRemGroup.setObjects(
      *(("LUM-INVENTORY-MIB", "invInsRemIndex"),
        ("LUM-INVENTORY-MIB", "invInsRemName"),
        ("LUM-INVENTORY-MIB", "invInsRemEvent"),
        ("LUM-INVENTORY-MIB", "invInsRemTimestamp"),
        ("LUM-INVENTORY-MIB", "invInsRemEquipmentType"),
        ("LUM-INVENTORY-MIB", "invInsRemPhysicalLocation"),
        ("LUM-INVENTORY-MIB", "invInsRemClei"),
        ("LUM-INVENTORY-MIB", "invInsRemSerialNumber"),
        ("LUM-INVENTORY-MIB", "invInsRemPartNumber"),
        ("LUM-INVENTORY-MIB", "invInsRemSeqNumber"))
)
if mibBuilder.loadTexts:
    invInsRemGroup.setStatus("current")

invGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 14)
)
invGeneralGroupV5.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralPhysTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralEntityTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralRelationTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralInsRemTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralInsRemLastSeqNumber"))
)
if mibBuilder.loadTexts:
    invGeneralGroupV5.setStatus("current")

inventoryGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 3, 1)
)
inventoryGeneralMinimalGroupV1.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralConfigLastChangeTime"),
        ("LUM-INVENTORY-MIB", "invGeneralPhysTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralEntityTableSize"),
        ("LUM-INVENTORY-MIB", "invGeneralRelationTableSize"))
)
if mibBuilder.loadTexts:
    inventoryGeneralMinimalGroupV1.setStatus("current")


# Notification objects

invNotificationPhysAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3, 0, 1)
)
invNotificationPhysAdded.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysVendorType"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"))
)
if mibBuilder.loadTexts:
    invNotificationPhysAdded.setStatus(
        "current"
    )

invNotificationPhysRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 2, 3, 0, 2)
)
invNotificationPhysRemoved.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysIndex"),
        ("LUM-INVENTORY-MIB", "invPhysDescr"),
        ("LUM-INVENTORY-MIB", "invPhysVendorType"),
        ("LUM-INVENTORY-MIB", "invPhysContainedIn"),
        ("LUM-INVENTORY-MIB", "invPhysClass"),
        ("LUM-INVENTORY-MIB", "invPhysParentRelPos"),
        ("LUM-INVENTORY-MIB", "invPhysName"),
        ("LUM-INVENTORY-MIB", "invPhysHardwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysFirmwareRev"),
        ("LUM-INVENTORY-MIB", "invPhysProductDataRev"),
        ("LUM-INVENTORY-MIB", "invPhysSerialNum"),
        ("LUM-INVENTORY-MIB", "invPhysMfgName"),
        ("LUM-INVENTORY-MIB", "invPhysModelName"),
        ("LUM-INVENTORY-MIB", "invPhysIsFRU"))
)
if mibBuilder.loadTexts:
    invNotificationPhysRemoved.setStatus(
        "current"
    )


# Notifications groups

invEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 1, 3)
)
invEventGroup.setObjects(
      *(("LUM-INVENTORY-MIB", "invNotificationPhysAdded"),
        ("LUM-INVENTORY-MIB", "invNotificationPhysRemoved"))
)
if mibBuilder.loadTexts:
    invEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumInventoryBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 1)
)
lumInventoryBasicComplV1.setObjects(
      *(("LUM-INVENTORY-MIB", "invPhysGroup"),
        ("LUM-INVENTORY-MIB", "invGeneralGroup"),
        ("LUM-INVENTORY-MIB", "invEventGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV1.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 2)
)
lumInventoryBasicComplV2.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV2"),
        ("LUM-INVENTORY-MIB", "invPhysGroup"),
        ("LUM-INVENTORY-MIB", "invEventGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV2.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 3)
)
lumInventoryBasicComplV3.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV2"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV2"),
        ("LUM-INVENTORY-MIB", "invEventGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV3.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 4)
)
lumInventoryBasicComplV4.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV2"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV3"),
        ("LUM-INVENTORY-MIB", "invEventGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV4.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 5)
)
lumInventoryBasicComplV5.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV2"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV3"),
        ("LUM-INVENTORY-MIB", "invEventGroup"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV5.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 6)
)
lumInventoryBasicComplV6.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV3"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV3"),
        ("LUM-INVENTORY-MIB", "invEventGroup"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV6.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 7)
)
lumInventoryBasicComplV7.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV4"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV3"),
        ("LUM-INVENTORY-MIB", "invEventGroup"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV7.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 8)
)
lumInventoryBasicComplV8.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV4"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV4"),
        ("LUM-INVENTORY-MIB", "invEventGroup"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV8.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 9)
)
lumInventoryBasicComplV9.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV4"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV5"),
        ("LUM-INVENTORY-MIB", "invEventGroup"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV9.setStatus(
        "deprecated"
    )

lumInventoryBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 2, 10)
)
lumInventoryBasicComplV10.setObjects(
      *(("LUM-INVENTORY-MIB", "invGeneralGroupV5"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV5"),
        ("LUM-INVENTORY-MIB", "invEventGroup"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"),
        ("LUM-INVENTORY-MIB", "invInsRemGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryBasicComplV10.setStatus(
        "current"
    )

lumInventoryMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4, 1)
)
lumInventoryMinimalComplV1.setObjects(
      *(("LUM-INVENTORY-MIB", "inventoryGeneralMinimalGroupV1"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV3"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryMinimalComplV1.setStatus(
        "deprecated"
    )

lumInventoryMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4, 2)
)
lumInventoryMinimalComplV2.setObjects(
      *(("LUM-INVENTORY-MIB", "inventoryGeneralMinimalGroupV1"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV4"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryMinimalComplV2.setStatus(
        "deprecated"
    )

lumInventoryMinimalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 3, 1, 4, 3)
)
lumInventoryMinimalComplV3.setObjects(
      *(("LUM-INVENTORY-MIB", "inventoryGeneralMinimalGroupV1"),
        ("LUM-INVENTORY-MIB", "invPhysGroupV5"),
        ("LUM-INVENTORY-MIB", "invEntityGroup"),
        ("LUM-INVENTORY-MIB", "invRelationGroup"))
)
if mibBuilder.loadTexts:
    lumInventoryMinimalComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-INVENTORY-MIB",
    **{"PhysicalClass": PhysicalClass,
       "EntityClass": EntityClass,
       "InsRemEventType": InsRemEventType,
       "lumInventoryMIBModule": lumInventoryMIBModule,
       "lumInventoryConfs": lumInventoryConfs,
       "lumInventoryGroups": lumInventoryGroups,
       "invPhysGroup": invPhysGroup,
       "invGeneralGroup": invGeneralGroup,
       "invEventGroup": invEventGroup,
       "invGeneralGroupV2": invGeneralGroupV2,
       "invPhysGroupV2": invPhysGroupV2,
       "invPhysGroupV3": invPhysGroupV3,
       "invEntityGroup": invEntityGroup,
       "invRelationGroup": invRelationGroup,
       "invGeneralGroupV3": invGeneralGroupV3,
       "invGeneralGroupV4": invGeneralGroupV4,
       "invPhysGroupV4": invPhysGroupV4,
       "invPhysGroupV5": invPhysGroupV5,
       "invInsRemGroup": invInsRemGroup,
       "invGeneralGroupV5": invGeneralGroupV5,
       "lumInventoryCompl": lumInventoryCompl,
       "lumInventoryBasicComplV1": lumInventoryBasicComplV1,
       "lumInventoryBasicComplV2": lumInventoryBasicComplV2,
       "lumInventoryBasicComplV3": lumInventoryBasicComplV3,
       "lumInventoryBasicComplV4": lumInventoryBasicComplV4,
       "lumInventoryBasicComplV5": lumInventoryBasicComplV5,
       "lumInventoryBasicComplV6": lumInventoryBasicComplV6,
       "lumInventoryBasicComplV7": lumInventoryBasicComplV7,
       "lumInventoryBasicComplV8": lumInventoryBasicComplV8,
       "lumInventoryBasicComplV9": lumInventoryBasicComplV9,
       "lumInventoryBasicComplV10": lumInventoryBasicComplV10,
       "lumInventoryMinimalGroups": lumInventoryMinimalGroups,
       "inventoryGeneralMinimalGroupV1": inventoryGeneralMinimalGroupV1,
       "lumInventoryMinimalCompl": lumInventoryMinimalCompl,
       "lumInventoryMinimalComplV1": lumInventoryMinimalComplV1,
       "lumInventoryMinimalComplV2": lumInventoryMinimalComplV2,
       "lumInventoryMinimalComplV3": lumInventoryMinimalComplV3,
       "lumInventoryMIBObjects": lumInventoryMIBObjects,
       "invPhysical": invPhysical,
       "invPhysTable": invPhysTable,
       "invPhysEntry": invPhysEntry,
       "invPhysIndex": invPhysIndex,
       "invPhysDescr": invPhysDescr,
       "invPhysVendorType": invPhysVendorType,
       "invPhysContainedIn": invPhysContainedIn,
       "invPhysClass": invPhysClass,
       "invPhysParentRelPos": invPhysParentRelPos,
       "invPhysName": invPhysName,
       "invPhysHardwareRev": invPhysHardwareRev,
       "invPhysFirmwareRev": invPhysFirmwareRev,
       "invPhysProductDataRev": invPhysProductDataRev,
       "invPhysSerialNum": invPhysSerialNum,
       "invPhysMfgName": invPhysMfgName,
       "invPhysModelName": invPhysModelName,
       "invPhysIsFRU": invPhysIsFRU,
       "invPhysSoftwareRev": invPhysSoftwareRev,
       "invPhysSoftwareProduct": invPhysSoftwareProduct,
       "invPhysClei": invPhysClei,
       "invPhysAid": invPhysAid,
       "invGeneral": invGeneral,
       "invGeneralLastChangeTime": invGeneralLastChangeTime,
       "invGeneralTestAndIncr": invGeneralTestAndIncr,
       "invGeneralMibSpecVersion": invGeneralMibSpecVersion,
       "invGeneralMibImplVersion": invGeneralMibImplVersion,
       "invGeneralConfigLastChangeTime": invGeneralConfigLastChangeTime,
       "invGeneralPhysTableSize": invGeneralPhysTableSize,
       "invGeneralEntityTableSize": invGeneralEntityTableSize,
       "invGeneralRelationTableSize": invGeneralRelationTableSize,
       "invGeneralInsRemTableSize": invGeneralInsRemTableSize,
       "invGeneralInsRemLastSeqNumber": invGeneralInsRemLastSeqNumber,
       "lumentisInvNotifications": lumentisInvNotifications,
       "invNotifyPrefix": invNotifyPrefix,
       "invNotificationPhysAdded": invNotificationPhysAdded,
       "invNotificationPhysRemoved": invNotificationPhysRemoved,
       "invEntities": invEntities,
       "invEntityTable": invEntityTable,
       "invEntityEntry": invEntityEntry,
       "invEntityIndex": invEntityIndex,
       "invEntityName": invEntityName,
       "invEntityObject": invEntityObject,
       "invEntityClass": invEntityClass,
       "invRelations": invRelations,
       "invRelationTable": invRelationTable,
       "invRelationEntry": invRelationEntry,
       "invRelationIndex": invRelationIndex,
       "invRelationEntityIndex1": invRelationEntityIndex1,
       "invRelationEntityName1": invRelationEntityName1,
       "invRelationType": invRelationType,
       "invRelationEntityIndex2": invRelationEntityIndex2,
       "invRelationEntityName2": invRelationEntityName2,
       "invInsRemLog": invInsRemLog,
       "invInsRemTable": invInsRemTable,
       "invInsRemEntry": invInsRemEntry,
       "invInsRemIndex": invInsRemIndex,
       "invInsRemName": invInsRemName,
       "invInsRemEvent": invInsRemEvent,
       "invInsRemTimestamp": invInsRemTimestamp,
       "invInsRemEquipmentType": invInsRemEquipmentType,
       "invInsRemPhysicalLocation": invInsRemPhysicalLocation,
       "invInsRemClei": invInsRemClei,
       "invInsRemSerialNumber": invInsRemSerialNumber,
       "invInsRemPartNumber": invInsRemPartNumber,
       "invInsRemSeqNumber": invInsRemSeqNumber}
)
