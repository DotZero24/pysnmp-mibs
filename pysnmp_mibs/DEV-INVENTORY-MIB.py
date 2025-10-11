# SNMP MIB module (DEV-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DEV-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:13 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nbInvId = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19)
)
if mibBuilder.loadTexts:
    nbInvId.setRevisions(
        ("2009-01-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InvIndexType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("shelf", 1),
          ("slot", 2),
          ("entity", 3),
          ("port", 4),
          ("cpuSlot", 5),
          ("fanSlot", 6),
          ("psSlot", 7))
    )



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbInvGenInfo_ObjectIdentity = ObjectIdentity
nbInvGenInfo = _NbInvGenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1)
)
_NbInvDevIndexInfo_ObjectIdentity = ObjectIdentity
nbInvDevIndexInfo = _NbInvDevIndexInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1)
)
_NbInvIndexesMaxNumber_Type = Integer32
_NbInvIndexesMaxNumber_Object = MibScalar
nbInvIndexesMaxNumber = _NbInvIndexesMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 1),
    _NbInvIndexesMaxNumber_Type()
)
nbInvIndexesMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvIndexesMaxNumber.setStatus("current")
_NbInvIndexesTable_Object = MibTable
nbInvIndexesTable = _NbInvIndexesTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5)
)
if mibBuilder.loadTexts:
    nbInvIndexesTable.setStatus("current")
_NbInvIndexesEntry_Object = MibTableRow
nbInvIndexesEntry = _NbInvIndexesEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1)
)
nbInvIndexesEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvIndexId"),
)
if mibBuilder.loadTexts:
    nbInvIndexesEntry.setStatus("current")


class _NbInvIndexId_Type(Integer32):
    """Custom type nbInvIndexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvIndexId_Type.__name__ = "Integer32"
_NbInvIndexId_Object = MibTableColumn
nbInvIndexId = _NbInvIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1, 1),
    _NbInvIndexId_Type()
)
nbInvIndexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvIndexId.setStatus("current")
_NbInvIndexType_Type = InvIndexType
_NbInvIndexType_Object = MibTableColumn
nbInvIndexType = _NbInvIndexType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1, 2),
    _NbInvIndexType_Type()
)
nbInvIndexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvIndexType.setStatus("current")


class _NbInvIndexVal_Type(Integer32):
    """Custom type nbInvIndexVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvIndexVal_Type.__name__ = "Integer32"
_NbInvIndexVal_Object = MibTableColumn
nbInvIndexVal = _NbInvIndexVal_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1, 3),
    _NbInvIndexVal_Type()
)
nbInvIndexVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvIndexVal.setStatus("current")
_NbInvIndexDesc_Type = DisplayString
_NbInvIndexDesc_Object = MibTableColumn
nbInvIndexDesc = _NbInvIndexDesc_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1, 4),
    _NbInvIndexDesc_Type()
)
nbInvIndexDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvIndexDesc.setStatus("current")


class _NbInvParentIndexId_Type(Integer32):
    """Custom type nbInvParentIndexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvParentIndexId_Type.__name__ = "Integer32"
_NbInvParentIndexId_Object = MibTableColumn
nbInvParentIndexId = _NbInvParentIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1, 5),
    _NbInvParentIndexId_Type()
)
nbInvParentIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvParentIndexId.setStatus("current")


class _NbInvOffsetVal_Type(Integer32):
    """Custom type nbInvOffsetVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvOffsetVal_Type.__name__ = "Integer32"
_NbInvOffsetVal_Object = MibTableColumn
nbInvOffsetVal = _NbInvOffsetVal_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 1, 5, 1, 6),
    _NbInvOffsetVal_Type()
)
nbInvOffsetVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvOffsetVal.setStatus("current")
_NbInvDevDetails_ObjectIdentity = ObjectIdentity
nbInvDevDetails = _NbInvDevDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2)
)
_NbInvShelfInfo_ObjectIdentity = ObjectIdentity
nbInvShelfInfo = _NbInvShelfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1)
)
_NbInvShelfIndexTableNum_Type = Integer32
_NbInvShelfIndexTableNum_Object = MibScalar
nbInvShelfIndexTableNum = _NbInvShelfIndexTableNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 1),
    _NbInvShelfIndexTableNum_Type()
)
nbInvShelfIndexTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfIndexTableNum.setStatus("current")
_NbInvShelfIndexId_Type = Integer32
_NbInvShelfIndexId_Object = MibScalar
nbInvShelfIndexId = _NbInvShelfIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 2),
    _NbInvShelfIndexId_Type()
)
nbInvShelfIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfIndexId.setStatus("current")
_NbInvShelfTable_Object = MibTable
nbInvShelfTable = _NbInvShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    nbInvShelfTable.setStatus("current")
_NbInvShelfEntry_Object = MibTableRow
nbInvShelfEntry = _NbInvShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1)
)
nbInvShelfEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvShelfIndex"),
)
if mibBuilder.loadTexts:
    nbInvShelfEntry.setStatus("current")


class _NbInvShelfIndex_Type(Integer32):
    """Custom type nbInvShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvShelfIndex_Type.__name__ = "Integer32"
_NbInvShelfIndex_Object = MibTableColumn
nbInvShelfIndex = _NbInvShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 1),
    _NbInvShelfIndex_Type()
)
nbInvShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvShelfIndex.setStatus("current")


class _NbInvShelfHwVer_Type(Integer32):
    """Custom type nbInvShelfHwVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvShelfHwVer_Type.__name__ = "Integer32"
_NbInvShelfHwVer_Object = MibTableColumn
nbInvShelfHwVer = _NbInvShelfHwVer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 2),
    _NbInvShelfHwVer_Type()
)
nbInvShelfHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfHwVer.setStatus("current")
_NbInvShelfHwSerialUnit_Type = DisplayString
_NbInvShelfHwSerialUnit_Object = MibTableColumn
nbInvShelfHwSerialUnit = _NbInvShelfHwSerialUnit_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 3),
    _NbInvShelfHwSerialUnit_Type()
)
nbInvShelfHwSerialUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfHwSerialUnit.setStatus("current")
_NbInvShelfHwBackPlaneSN_Type = DisplayString
_NbInvShelfHwBackPlaneSN_Object = MibTableColumn
nbInvShelfHwBackPlaneSN = _NbInvShelfHwBackPlaneSN_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 4),
    _NbInvShelfHwBackPlaneSN_Type()
)
nbInvShelfHwBackPlaneSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfHwBackPlaneSN.setStatus("current")


class _NbInvShelfHwCpuNumber_Type(Integer32):
    """Custom type nbInvShelfHwCpuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvShelfHwCpuNumber_Type.__name__ = "Integer32"
_NbInvShelfHwCpuNumber_Object = MibTableColumn
nbInvShelfHwCpuNumber = _NbInvShelfHwCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 6),
    _NbInvShelfHwCpuNumber_Type()
)
nbInvShelfHwCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfHwCpuNumber.setStatus("current")


class _NbInvShelfHwFanNumber_Type(Integer32):
    """Custom type nbInvShelfHwFanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvShelfHwFanNumber_Type.__name__ = "Integer32"
_NbInvShelfHwFanNumber_Object = MibTableColumn
nbInvShelfHwFanNumber = _NbInvShelfHwFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 7),
    _NbInvShelfHwFanNumber_Type()
)
nbInvShelfHwFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfHwFanNumber.setStatus("current")


class _NbInvShelfHwPSNumber_Type(Integer32):
    """Custom type nbInvShelfHwPSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvShelfHwPSNumber_Type.__name__ = "Integer32"
_NbInvShelfHwPSNumber_Object = MibTableColumn
nbInvShelfHwPSNumber = _NbInvShelfHwPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 8),
    _NbInvShelfHwPSNumber_Type()
)
nbInvShelfHwPSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfHwPSNumber.setStatus("current")
_NbInvShelfSwRev_Type = DisplayString
_NbInvShelfSwRev_Object = MibTableColumn
nbInvShelfSwRev = _NbInvShelfSwRev_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 9),
    _NbInvShelfSwRev_Type()
)
nbInvShelfSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfSwRev.setStatus("current")
_NbInvShelfSwBuildTime_Type = DisplayString
_NbInvShelfSwBuildTime_Object = MibTableColumn
nbInvShelfSwBuildTime = _NbInvShelfSwBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 1, 5, 1, 10),
    _NbInvShelfSwBuildTime_Type()
)
nbInvShelfSwBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvShelfSwBuildTime.setStatus("current")
_NbInvSlotInfo_ObjectIdentity = ObjectIdentity
nbInvSlotInfo = _NbInvSlotInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2)
)
_NbInvSlotIndexTableNum_Type = Integer32
_NbInvSlotIndexTableNum_Object = MibScalar
nbInvSlotIndexTableNum = _NbInvSlotIndexTableNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 1),
    _NbInvSlotIndexTableNum_Type()
)
nbInvSlotIndexTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvSlotIndexTableNum.setStatus("current")
_NbInvSlotIndexId_Type = Integer32
_NbInvSlotIndexId_Object = MibScalar
nbInvSlotIndexId = _NbInvSlotIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 2),
    _NbInvSlotIndexId_Type()
)
nbInvSlotIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvSlotIndexId.setStatus("current")
_NbInvSlotTable_Object = MibTable
nbInvSlotTable = _NbInvSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    nbInvSlotTable.setStatus("current")
_NbInvSlotEntry_Object = MibTableRow
nbInvSlotEntry = _NbInvSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5, 1)
)
nbInvSlotEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvSlotIndex"),
)
if mibBuilder.loadTexts:
    nbInvSlotEntry.setStatus("current")


class _NbInvSlotIndex_Type(Integer32):
    """Custom type nbInvSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvSlotIndex_Type.__name__ = "Integer32"
_NbInvSlotIndex_Object = MibTableColumn
nbInvSlotIndex = _NbInvSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5, 1, 1),
    _NbInvSlotIndex_Type()
)
nbInvSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvSlotIndex.setStatus("current")


class _NbInvSlotHardwareVer_Type(Integer32):
    """Custom type nbInvSlotHardwareVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvSlotHardwareVer_Type.__name__ = "Integer32"
_NbInvSlotHardwareVer_Object = MibTableColumn
nbInvSlotHardwareVer = _NbInvSlotHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5, 1, 2),
    _NbInvSlotHardwareVer_Type()
)
nbInvSlotHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvSlotHardwareVer.setStatus("current")
_NbInvSlotHwSerialUnit_Type = DisplayString
_NbInvSlotHwSerialUnit_Object = MibTableColumn
nbInvSlotHwSerialUnit = _NbInvSlotHwSerialUnit_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5, 1, 3),
    _NbInvSlotHwSerialUnit_Type()
)
nbInvSlotHwSerialUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvSlotHwSerialUnit.setStatus("current")
_NbInvSlotHwPartNumber_Type = DisplayString
_NbInvSlotHwPartNumber_Object = MibTableColumn
nbInvSlotHwPartNumber = _NbInvSlotHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5, 1, 4),
    _NbInvSlotHwPartNumber_Type()
)
nbInvSlotHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvSlotHwPartNumber.setStatus("current")
_NbInvSlotSwFpgaRevision_Type = DisplayString
_NbInvSlotSwFpgaRevision_Object = MibTableColumn
nbInvSlotSwFpgaRevision = _NbInvSlotSwFpgaRevision_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 2, 5, 1, 5),
    _NbInvSlotSwFpgaRevision_Type()
)
nbInvSlotSwFpgaRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvSlotSwFpgaRevision.setStatus("current")
_NbInvPortInfo_ObjectIdentity = ObjectIdentity
nbInvPortInfo = _NbInvPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4)
)
_NbInvPortIndexTableNum_Type = Integer32
_NbInvPortIndexTableNum_Object = MibScalar
nbInvPortIndexTableNum = _NbInvPortIndexTableNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 1),
    _NbInvPortIndexTableNum_Type()
)
nbInvPortIndexTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortIndexTableNum.setStatus("current")
_NbInvPortIndexId_Type = Integer32
_NbInvPortIndexId_Object = MibScalar
nbInvPortIndexId = _NbInvPortIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 2),
    _NbInvPortIndexId_Type()
)
nbInvPortIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortIndexId.setStatus("current")
_NbInvPortTable_Object = MibTable
nbInvPortTable = _NbInvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    nbInvPortTable.setStatus("current")
_NbInvPortEntry_Object = MibTableRow
nbInvPortEntry = _NbInvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1)
)
nbInvPortEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvPortIndex"),
)
if mibBuilder.loadTexts:
    nbInvPortEntry.setStatus("current")


class _NbInvPortIndex_Type(Integer32):
    """Custom type nbInvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvPortIndex_Type.__name__ = "Integer32"
_NbInvPortIndex_Object = MibTableColumn
nbInvPortIndex = _NbInvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 1),
    _NbInvPortIndex_Type()
)
nbInvPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvPortIndex.setStatus("current")


class _NbInvPortIdentifier_Type(Integer32):
    """Custom type nbInvPortIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("combo", 2),
          ("gbic", 3),
          ("fixed", 4),
          ("sfp", 5),
          ("xbi300pin", 6),
          ("xenpak", 7),
          ("xfp", 8),
          ("xff", 9),
          ("xfpE", 10),
          ("xpak", 11),
          ("x2", 12),
          ("dsfp", 13))
    )


_NbInvPortIdentifier_Type.__name__ = "Integer32"
_NbInvPortIdentifier_Object = MibTableColumn
nbInvPortIdentifier = _NbInvPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 2),
    _NbInvPortIdentifier_Type()
)
nbInvPortIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortIdentifier.setStatus("current")


class _NbInvPortConnector_Type(Integer32):
    """Custom type nbInvPortConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("sc", 3),
          ("fcs1cc", 4),
          ("fcs2cc", 5),
          ("bnctnc", 6),
          ("fcch", 7),
          ("fiberJack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalPigtail", 13),
          ("hssdcii", 34),
          ("copperPigtail", 35))
    )


_NbInvPortConnector_Type.__name__ = "Integer32"
_NbInvPortConnector_Object = MibTableColumn
nbInvPortConnector = _NbInvPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 3),
    _NbInvPortConnector_Type()
)
nbInvPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortConnector.setStatus("current")


class _NbInvPortVendorName_Type(DisplayString):
    """Custom type nbInvPortVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbInvPortVendorName_Type.__name__ = "DisplayString"
_NbInvPortVendorName_Object = MibTableColumn
nbInvPortVendorName = _NbInvPortVendorName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 4),
    _NbInvPortVendorName_Type()
)
nbInvPortVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorName.setStatus("current")


class _NbInvPortVendorOUI_Type(DisplayString):
    """Custom type nbInvPortVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_NbInvPortVendorOUI_Type.__name__ = "DisplayString"
_NbInvPortVendorOUI_Object = MibTableColumn
nbInvPortVendorOUI = _NbInvPortVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 5),
    _NbInvPortVendorOUI_Type()
)
nbInvPortVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorOUI.setStatus("current")


class _NbInvPortVendorPN_Type(DisplayString):
    """Custom type nbInvPortVendorPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbInvPortVendorPN_Type.__name__ = "DisplayString"
_NbInvPortVendorPN_Object = MibTableColumn
nbInvPortVendorPN = _NbInvPortVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 6),
    _NbInvPortVendorPN_Type()
)
nbInvPortVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorPN.setStatus("current")


class _NbInvPortVendorRev_Type(DisplayString):
    """Custom type nbInvPortVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_NbInvPortVendorRev_Type.__name__ = "DisplayString"
_NbInvPortVendorRev_Object = MibTableColumn
nbInvPortVendorRev = _NbInvPortVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 7),
    _NbInvPortVendorRev_Type()
)
nbInvPortVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorRev.setStatus("current")


class _NbInvPortVendorSN_Type(DisplayString):
    """Custom type nbInvPortVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbInvPortVendorSN_Type.__name__ = "DisplayString"
_NbInvPortVendorSN_Object = MibTableColumn
nbInvPortVendorSN = _NbInvPortVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 8),
    _NbInvPortVendorSN_Type()
)
nbInvPortVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorSN.setStatus("current")


class _NbInvPortVendorDate_Type(DisplayString):
    """Custom type nbInvPortVendorDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbInvPortVendorDate_Type.__name__ = "DisplayString"
_NbInvPortVendorDate_Object = MibTableColumn
nbInvPortVendorDate = _NbInvPortVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 9),
    _NbInvPortVendorDate_Type()
)
nbInvPortVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorDate.setStatus("current")


class _NbInvPortVendorLotCode_Type(DisplayString):
    """Custom type nbInvPortVendorLotCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_NbInvPortVendorLotCode_Type.__name__ = "DisplayString"
_NbInvPortVendorLotCode_Object = MibTableColumn
nbInvPortVendorLotCode = _NbInvPortVendorLotCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 10),
    _NbInvPortVendorLotCode_Type()
)
nbInvPortVendorLotCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortVendorLotCode.setStatus("current")


class _NbInvPortAlias_Type(DisplayString):
    """Custom type nbInvPortAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_NbInvPortAlias_Type.__name__ = "DisplayString"
_NbInvPortAlias_Object = MibTableColumn
nbInvPortAlias = _NbInvPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 11),
    _NbInvPortAlias_Type()
)
nbInvPortAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortAlias.setStatus("current")
_NbInvPortWavelength_Type = Integer32
_NbInvPortWavelength_Object = MibTableColumn
nbInvPortWavelength = _NbInvPortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 4, 5, 1, 12),
    _NbInvPortWavelength_Type()
)
nbInvPortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPortWavelength.setStatus("current")
if mibBuilder.loadTexts:
    nbInvPortWavelength.setUnits("0.01 Nano Meter(nm)")
_NbInvCpuInfo_ObjectIdentity = ObjectIdentity
nbInvCpuInfo = _NbInvCpuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5)
)
_NbInvCpuIndexTableNum_Type = Integer32
_NbInvCpuIndexTableNum_Object = MibScalar
nbInvCpuIndexTableNum = _NbInvCpuIndexTableNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 1),
    _NbInvCpuIndexTableNum_Type()
)
nbInvCpuIndexTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvCpuIndexTableNum.setStatus("current")
_NbInvCpuIndexId_Type = Integer32
_NbInvCpuIndexId_Object = MibScalar
nbInvCpuIndexId = _NbInvCpuIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 2),
    _NbInvCpuIndexId_Type()
)
nbInvCpuIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvCpuIndexId.setStatus("current")
_NbInvCpuTable_Object = MibTable
nbInvCpuTable = _NbInvCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    nbInvCpuTable.setStatus("current")
_NbInvCpuEntry_Object = MibTableRow
nbInvCpuEntry = _NbInvCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 5, 1)
)
nbInvCpuEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvCpuIndex"),
)
if mibBuilder.loadTexts:
    nbInvCpuEntry.setStatus("current")


class _NbInvCpuIndex_Type(Integer32):
    """Custom type nbInvCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvCpuIndex_Type.__name__ = "Integer32"
_NbInvCpuIndex_Object = MibTableColumn
nbInvCpuIndex = _NbInvCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 5, 1, 1),
    _NbInvCpuIndex_Type()
)
nbInvCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvCpuIndex.setStatus("current")
_NbInvCpuSerial_Type = DisplayString
_NbInvCpuSerial_Object = MibTableColumn
nbInvCpuSerial = _NbInvCpuSerial_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 5, 1, 4),
    _NbInvCpuSerial_Type()
)
nbInvCpuSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvCpuSerial.setStatus("current")
_NbInvCpuDescr_Type = DisplayString
_NbInvCpuDescr_Object = MibTableColumn
nbInvCpuDescr = _NbInvCpuDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 5, 5, 1, 9),
    _NbInvCpuDescr_Type()
)
nbInvCpuDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvCpuDescr.setStatus("current")
_NbInvFanInfo_ObjectIdentity = ObjectIdentity
nbInvFanInfo = _NbInvFanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6)
)
_NbInvFanIndexTableNum_Type = Integer32
_NbInvFanIndexTableNum_Object = MibScalar
nbInvFanIndexTableNum = _NbInvFanIndexTableNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6, 1),
    _NbInvFanIndexTableNum_Type()
)
nbInvFanIndexTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvFanIndexTableNum.setStatus("current")
_NbInvFanIndexId_Type = Integer32
_NbInvFanIndexId_Object = MibScalar
nbInvFanIndexId = _NbInvFanIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6, 2),
    _NbInvFanIndexId_Type()
)
nbInvFanIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvFanIndexId.setStatus("current")
_NbInvFanTable_Object = MibTable
nbInvFanTable = _NbInvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    nbInvFanTable.setStatus("current")
_NbInvFanEntry_Object = MibTableRow
nbInvFanEntry = _NbInvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6, 5, 1)
)
nbInvFanEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvFanIndex"),
)
if mibBuilder.loadTexts:
    nbInvFanEntry.setStatus("current")


class _NbInvFanIndex_Type(Integer32):
    """Custom type nbInvFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvFanIndex_Type.__name__ = "Integer32"
_NbInvFanIndex_Object = MibTableColumn
nbInvFanIndex = _NbInvFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6, 5, 1, 1),
    _NbInvFanIndex_Type()
)
nbInvFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvFanIndex.setStatus("current")
_NbInvFanDescr_Type = DisplayString
_NbInvFanDescr_Object = MibTableColumn
nbInvFanDescr = _NbInvFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 6, 5, 1, 2),
    _NbInvFanDescr_Type()
)
nbInvFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvFanDescr.setStatus("current")
_NbInvPsInfo_ObjectIdentity = ObjectIdentity
nbInvPsInfo = _NbInvPsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7)
)
_NbInvPsIndexTableNum_Type = Integer32
_NbInvPsIndexTableNum_Object = MibScalar
nbInvPsIndexTableNum = _NbInvPsIndexTableNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 1),
    _NbInvPsIndexTableNum_Type()
)
nbInvPsIndexTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPsIndexTableNum.setStatus("current")
_NbInvPsIndexId_Type = Integer32
_NbInvPsIndexId_Object = MibScalar
nbInvPsIndexId = _NbInvPsIndexId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 2),
    _NbInvPsIndexId_Type()
)
nbInvPsIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPsIndexId.setStatus("current")
_NbInvPsTable_Object = MibTable
nbInvPsTable = _NbInvPsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5)
)
if mibBuilder.loadTexts:
    nbInvPsTable.setStatus("current")
_NbInvPsEntry_Object = MibTableRow
nbInvPsEntry = _NbInvPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5, 1)
)
nbInvPsEntry.setIndexNames(
    (0, "DEV-INVENTORY-MIB", "nbInvPsIndex"),
)
if mibBuilder.loadTexts:
    nbInvPsEntry.setStatus("current")


class _NbInvPsIndex_Type(Integer32):
    """Custom type nbInvPsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbInvPsIndex_Type.__name__ = "Integer32"
_NbInvPsIndex_Object = MibTableColumn
nbInvPsIndex = _NbInvPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5, 1, 1),
    _NbInvPsIndex_Type()
)
nbInvPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbInvPsIndex.setStatus("current")


class _NbInvPsType_Type(Integer32):
    """Custom type nbInvPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dcType", 2),
          ("acType", 3))
    )


_NbInvPsType_Type.__name__ = "Integer32"
_NbInvPsType_Object = MibTableColumn
nbInvPsType = _NbInvPsType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5, 1, 2),
    _NbInvPsType_Type()
)
nbInvPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPsType.setStatus("current")
_NbInvPsSerialNumber_Type = DisplayString
_NbInvPsSerialNumber_Object = MibTableColumn
nbInvPsSerialNumber = _NbInvPsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5, 1, 3),
    _NbInvPsSerialNumber_Type()
)
nbInvPsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPsSerialNumber.setStatus("current")
_NbInvPsPartNumber_Type = DisplayString
_NbInvPsPartNumber_Object = MibTableColumn
nbInvPsPartNumber = _NbInvPsPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5, 1, 4),
    _NbInvPsPartNumber_Type()
)
nbInvPsPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPsPartNumber.setStatus("current")
_NbInvPsDescr_Type = DisplayString
_NbInvPsDescr_Object = MibTableColumn
nbInvPsDescr = _NbInvPsDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 1, 2, 7, 5, 1, 5),
    _NbInvPsDescr_Type()
)
nbInvPsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbInvPsDescr.setStatus("current")
_NbInvConformance_ObjectIdentity = ObjectIdentity
nbInvConformance = _NbInvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101)
)
_NbInvMIBCompliances_ObjectIdentity = ObjectIdentity
nbInvMIBCompliances = _NbInvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 1)
)
_NbInvMIBGroups_ObjectIdentity = ObjectIdentity
nbInvMIBGroups = _NbInvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2)
)

# Managed Objects groups

nbInvIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 1)
)
nbInvIndexGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvIndexesMaxNumber"),
        ("DEV-INVENTORY-MIB", "nbInvIndexType"),
        ("DEV-INVENTORY-MIB", "nbInvIndexVal"),
        ("DEV-INVENTORY-MIB", "nbInvIndexDesc"),
        ("DEV-INVENTORY-MIB", "nbInvParentIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvOffsetVal"))
)
if mibBuilder.loadTexts:
    nbInvIndexGroup.setStatus("current")

nbInvShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 2)
)
nbInvShelfGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvShelfIndexTableNum"),
        ("DEV-INVENTORY-MIB", "nbInvShelfIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvShelfHwVer"),
        ("DEV-INVENTORY-MIB", "nbInvShelfHwSerialUnit"),
        ("DEV-INVENTORY-MIB", "nbInvShelfHwBackPlaneSN"),
        ("DEV-INVENTORY-MIB", "nbInvShelfHwCpuNumber"),
        ("DEV-INVENTORY-MIB", "nbInvShelfHwFanNumber"),
        ("DEV-INVENTORY-MIB", "nbInvShelfHwPSNumber"),
        ("DEV-INVENTORY-MIB", "nbInvShelfSwRev"),
        ("DEV-INVENTORY-MIB", "nbInvShelfSwBuildTime"))
)
if mibBuilder.loadTexts:
    nbInvShelfGroup.setStatus("current")

nbInvSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 3)
)
nbInvSlotGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvSlotIndexTableNum"),
        ("DEV-INVENTORY-MIB", "nbInvSlotIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvSlotHardwareVer"),
        ("DEV-INVENTORY-MIB", "nbInvSlotHwSerialUnit"),
        ("DEV-INVENTORY-MIB", "nbInvSlotHwPartNumber"),
        ("DEV-INVENTORY-MIB", "nbInvSlotSwFpgaRevision"))
)
if mibBuilder.loadTexts:
    nbInvSlotGroup.setStatus("current")

nbInvPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 5)
)
nbInvPortGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvPortIndexTableNum"),
        ("DEV-INVENTORY-MIB", "nbInvPortIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvPortIdentifier"),
        ("DEV-INVENTORY-MIB", "nbInvPortConnector"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorName"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorOUI"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorPN"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorRev"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorSN"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorDate"),
        ("DEV-INVENTORY-MIB", "nbInvPortVendorLotCode"),
        ("DEV-INVENTORY-MIB", "nbInvPortAlias"),
        ("DEV-INVENTORY-MIB", "nbInvPortWavelength"))
)
if mibBuilder.loadTexts:
    nbInvPortGroup.setStatus("current")

nbInvCPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 6)
)
nbInvCPUGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvCpuIndexTableNum"),
        ("DEV-INVENTORY-MIB", "nbInvCpuIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvCpuSerial"),
        ("DEV-INVENTORY-MIB", "nbInvCpuDescr"))
)
if mibBuilder.loadTexts:
    nbInvCPUGroup.setStatus("current")

nbInvFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 7)
)
nbInvFanGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvFanIndexTableNum"),
        ("DEV-INVENTORY-MIB", "nbInvFanIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvFanDescr"))
)
if mibBuilder.loadTexts:
    nbInvFanGroup.setStatus("current")

nbInvPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 2, 8)
)
nbInvPSGroup.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvPsIndexTableNum"),
        ("DEV-INVENTORY-MIB", "nbInvPsIndexId"),
        ("DEV-INVENTORY-MIB", "nbInvPsType"),
        ("DEV-INVENTORY-MIB", "nbInvPsSerialNumber"),
        ("DEV-INVENTORY-MIB", "nbInvPsPartNumber"),
        ("DEV-INVENTORY-MIB", "nbInvPsDescr"))
)
if mibBuilder.loadTexts:
    nbInvPSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nbInvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 19, 101, 1, 1)
)
nbInvMIBCompliance.setObjects(
      *(("DEV-INVENTORY-MIB", "nbInvIndexGroup"),
        ("DEV-INVENTORY-MIB", "nbInvShelfGroup"),
        ("DEV-INVENTORY-MIB", "nbInvSlotGroup"),
        ("DEV-INVENTORY-MIB", "nbInvPortGroup"),
        ("DEV-INVENTORY-MIB", "nbInvCPUGroup"),
        ("DEV-INVENTORY-MIB", "nbInvFanGroup"),
        ("DEV-INVENTORY-MIB", "nbInvPSGroup"))
)
if mibBuilder.loadTexts:
    nbInvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEV-INVENTORY-MIB",
    **{"InvIndexType": InvIndexType,
       "nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbInvId": nbInvId,
       "nbInvGenInfo": nbInvGenInfo,
       "nbInvDevIndexInfo": nbInvDevIndexInfo,
       "nbInvIndexesMaxNumber": nbInvIndexesMaxNumber,
       "nbInvIndexesTable": nbInvIndexesTable,
       "nbInvIndexesEntry": nbInvIndexesEntry,
       "nbInvIndexId": nbInvIndexId,
       "nbInvIndexType": nbInvIndexType,
       "nbInvIndexVal": nbInvIndexVal,
       "nbInvIndexDesc": nbInvIndexDesc,
       "nbInvParentIndexId": nbInvParentIndexId,
       "nbInvOffsetVal": nbInvOffsetVal,
       "nbInvDevDetails": nbInvDevDetails,
       "nbInvShelfInfo": nbInvShelfInfo,
       "nbInvShelfIndexTableNum": nbInvShelfIndexTableNum,
       "nbInvShelfIndexId": nbInvShelfIndexId,
       "nbInvShelfTable": nbInvShelfTable,
       "nbInvShelfEntry": nbInvShelfEntry,
       "nbInvShelfIndex": nbInvShelfIndex,
       "nbInvShelfHwVer": nbInvShelfHwVer,
       "nbInvShelfHwSerialUnit": nbInvShelfHwSerialUnit,
       "nbInvShelfHwBackPlaneSN": nbInvShelfHwBackPlaneSN,
       "nbInvShelfHwCpuNumber": nbInvShelfHwCpuNumber,
       "nbInvShelfHwFanNumber": nbInvShelfHwFanNumber,
       "nbInvShelfHwPSNumber": nbInvShelfHwPSNumber,
       "nbInvShelfSwRev": nbInvShelfSwRev,
       "nbInvShelfSwBuildTime": nbInvShelfSwBuildTime,
       "nbInvSlotInfo": nbInvSlotInfo,
       "nbInvSlotIndexTableNum": nbInvSlotIndexTableNum,
       "nbInvSlotIndexId": nbInvSlotIndexId,
       "nbInvSlotTable": nbInvSlotTable,
       "nbInvSlotEntry": nbInvSlotEntry,
       "nbInvSlotIndex": nbInvSlotIndex,
       "nbInvSlotHardwareVer": nbInvSlotHardwareVer,
       "nbInvSlotHwSerialUnit": nbInvSlotHwSerialUnit,
       "nbInvSlotHwPartNumber": nbInvSlotHwPartNumber,
       "nbInvSlotSwFpgaRevision": nbInvSlotSwFpgaRevision,
       "nbInvPortInfo": nbInvPortInfo,
       "nbInvPortIndexTableNum": nbInvPortIndexTableNum,
       "nbInvPortIndexId": nbInvPortIndexId,
       "nbInvPortTable": nbInvPortTable,
       "nbInvPortEntry": nbInvPortEntry,
       "nbInvPortIndex": nbInvPortIndex,
       "nbInvPortIdentifier": nbInvPortIdentifier,
       "nbInvPortConnector": nbInvPortConnector,
       "nbInvPortVendorName": nbInvPortVendorName,
       "nbInvPortVendorOUI": nbInvPortVendorOUI,
       "nbInvPortVendorPN": nbInvPortVendorPN,
       "nbInvPortVendorRev": nbInvPortVendorRev,
       "nbInvPortVendorSN": nbInvPortVendorSN,
       "nbInvPortVendorDate": nbInvPortVendorDate,
       "nbInvPortVendorLotCode": nbInvPortVendorLotCode,
       "nbInvPortAlias": nbInvPortAlias,
       "nbInvPortWavelength": nbInvPortWavelength,
       "nbInvCpuInfo": nbInvCpuInfo,
       "nbInvCpuIndexTableNum": nbInvCpuIndexTableNum,
       "nbInvCpuIndexId": nbInvCpuIndexId,
       "nbInvCpuTable": nbInvCpuTable,
       "nbInvCpuEntry": nbInvCpuEntry,
       "nbInvCpuIndex": nbInvCpuIndex,
       "nbInvCpuSerial": nbInvCpuSerial,
       "nbInvCpuDescr": nbInvCpuDescr,
       "nbInvFanInfo": nbInvFanInfo,
       "nbInvFanIndexTableNum": nbInvFanIndexTableNum,
       "nbInvFanIndexId": nbInvFanIndexId,
       "nbInvFanTable": nbInvFanTable,
       "nbInvFanEntry": nbInvFanEntry,
       "nbInvFanIndex": nbInvFanIndex,
       "nbInvFanDescr": nbInvFanDescr,
       "nbInvPsInfo": nbInvPsInfo,
       "nbInvPsIndexTableNum": nbInvPsIndexTableNum,
       "nbInvPsIndexId": nbInvPsIndexId,
       "nbInvPsTable": nbInvPsTable,
       "nbInvPsEntry": nbInvPsEntry,
       "nbInvPsIndex": nbInvPsIndex,
       "nbInvPsType": nbInvPsType,
       "nbInvPsSerialNumber": nbInvPsSerialNumber,
       "nbInvPsPartNumber": nbInvPsPartNumber,
       "nbInvPsDescr": nbInvPsDescr,
       "nbInvConformance": nbInvConformance,
       "nbInvMIBCompliances": nbInvMIBCompliances,
       "nbInvMIBCompliance": nbInvMIBCompliance,
       "nbInvMIBGroups": nbInvMIBGroups,
       "nbInvIndexGroup": nbInvIndexGroup,
       "nbInvShelfGroup": nbInvShelfGroup,
       "nbInvSlotGroup": nbInvSlotGroup,
       "nbInvPortGroup": nbInvPortGroup,
       "nbInvCPUGroup": nbInvCPUGroup,
       "nbInvFanGroup": nbInvFanGroup,
       "nbInvPSGroup": nbInvPSGroup}
)
