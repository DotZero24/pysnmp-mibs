# SNMP MIB module (KMCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/kyocera/KMCOMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:49 2025
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(PresentOnOff,
 prtMarkerIndex) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff",
    "prtMarkerIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Kyocera_ObjectIdentity = ObjectIdentity
kyocera = _Kyocera_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347)
)
_KmCommon_ObjectIdentity = ObjectIdentity
kmCommon = _KmCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42)
)
_KmAccounting_ObjectIdentity = ObjectIdentity
kmAccounting = _KmAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1)
)
_KmCounterSet_ObjectIdentity = ObjectIdentity
kmCounterSet = _KmCounterSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1)
)
_KmCounterSetTable_Object = MibTable
kmCounterSetTable = _KmCounterSetTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    kmCounterSetTable.setStatus("mandatory")
_KmCounterSetEntry_Object = MibTableRow
kmCounterSetEntry = _KmCounterSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1)
)
kmCounterSetEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmCounterSetIndex"),
    (0, "KMCOMMON-MIB", "kmCounterSetItemIndex"),
)
if mibBuilder.loadTexts:
    kmCounterSetEntry.setStatus("mandatory")
_KmCounterSetIndex_Type = Integer32
_KmCounterSetIndex_Object = MibTableColumn
kmCounterSetIndex = _KmCounterSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 1),
    _KmCounterSetIndex_Type()
)
kmCounterSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmCounterSetIndex.setStatus("mandatory")
_KmCounterSetItemIndex_Type = Integer32
_KmCounterSetItemIndex_Object = MibTableColumn
kmCounterSetItemIndex = _KmCounterSetItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 2),
    _KmCounterSetItemIndex_Type()
)
kmCounterSetItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmCounterSetItemIndex.setStatus("mandatory")
_KmCounterItem_Type = Integer32
_KmCounterItem_Object = MibTableColumn
kmCounterItem = _KmCounterItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 3),
    _KmCounterItem_Type()
)
kmCounterItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmCounterItem.setStatus("mandatory")
_KmCounterMediaRef_Type = Integer32
_KmCounterMediaRef_Object = MibTableColumn
kmCounterMediaRef = _KmCounterMediaRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 4),
    _KmCounterMediaRef_Type()
)
kmCounterMediaRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmCounterMediaRef.setStatus("mandatory")
_KmCounterColorModeRef_Type = Integer32
_KmCounterColorModeRef_Object = MibTableColumn
kmCounterColorModeRef = _KmCounterColorModeRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 5),
    _KmCounterColorModeRef_Type()
)
kmCounterColorModeRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmCounterColorModeRef.setStatus("mandatory")
_KmAccountBalanceItem_Type = Integer32
_KmAccountBalanceItem_Object = MibTableColumn
kmAccountBalanceItem = _KmAccountBalanceItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 6),
    _KmAccountBalanceItem_Type()
)
kmAccountBalanceItem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmAccountBalanceItem.setStatus("optional")


class _KmAccountBalanceStatus_Type(Integer32):
    """Custom type kmAccountBalanceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("locked", 1))
    )


_KmAccountBalanceStatus_Type.__name__ = "Integer32"
_KmAccountBalanceStatus_Object = MibTableColumn
kmAccountBalanceStatus = _KmAccountBalanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 7),
    _KmAccountBalanceStatus_Type()
)
kmAccountBalanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmAccountBalanceStatus.setStatus("optional")


class _KmAccountRestriction_Type(Integer32):
    """Custom type kmAccountRestriction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KmAccountRestriction_Type.__name__ = "Integer32"
_KmAccountRestriction_Object = MibTableColumn
kmAccountRestriction = _KmAccountRestriction_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 1, 1, 1, 8),
    _KmAccountRestriction_Type()
)
kmAccountRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmAccountRestriction.setStatus("optional")
_KmGroup_ObjectIdentity = ObjectIdentity
kmGroup = _KmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2)
)
_KmGroupLevel1_ObjectIdentity = ObjectIdentity
kmGroupLevel1 = _KmGroupLevel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1)
)
_KmGroupConfigTable_Object = MibTable
kmGroupConfigTable = _KmGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    kmGroupConfigTable.setStatus("mandatory")
_KmGroupConfigEntry_Object = MibTableRow
kmGroupConfigEntry = _KmGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1)
)
kmGroupConfigEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmGroupConfigEntry.setStatus("mandatory")
_KmGroupCodeWidth_Type = Integer32
_KmGroupCodeWidth_Object = MibTableColumn
kmGroupCodeWidth = _KmGroupCodeWidth_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 1),
    _KmGroupCodeWidth_Type()
)
kmGroupCodeWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupCodeWidth.setStatus("mandatory")


class _KmGroupSecurityLock_Type(DisplayString):
    """Custom type kmGroupSecurityLock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KmGroupSecurityLock_Type.__name__ = "DisplayString"
_KmGroupSecurityLock_Object = MibTableColumn
kmGroupSecurityLock = _KmGroupSecurityLock_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 2),
    _KmGroupSecurityLock_Type()
)
kmGroupSecurityLock.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kmGroupSecurityLock.setStatus("mandatory")
_KmGroupUpdateCount_Type = Integer32
_KmGroupUpdateCount_Object = MibTableColumn
kmGroupUpdateCount = _KmGroupUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 3),
    _KmGroupUpdateCount_Type()
)
kmGroupUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupUpdateCount.setStatus("mandatory")


class _KmGroupEntryCreate_Type(DisplayString):
    """Custom type kmGroupEntryCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_KmGroupEntryCreate_Type.__name__ = "DisplayString"
_KmGroupEntryCreate_Object = MibTableColumn
kmGroupEntryCreate = _KmGroupEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 4),
    _KmGroupEntryCreate_Type()
)
kmGroupEntryCreate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kmGroupEntryCreate.setStatus("mandatory")


class _KmGroupEntryPurge_Type(DisplayString):
    """Custom type kmGroupEntryPurge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_KmGroupEntryPurge_Type.__name__ = "DisplayString"
_KmGroupEntryPurge_Object = MibTableColumn
kmGroupEntryPurge = _KmGroupEntryPurge_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 5),
    _KmGroupEntryPurge_Type()
)
kmGroupEntryPurge.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kmGroupEntryPurge.setStatus("mandatory")


class _KmGroupResetAll_Type(DisplayString):
    """Custom type kmGroupResetAll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KmGroupResetAll_Type.__name__ = "DisplayString"
_KmGroupResetAll_Object = MibTableColumn
kmGroupResetAll = _KmGroupResetAll_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 6),
    _KmGroupResetAll_Type()
)
kmGroupResetAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kmGroupResetAll.setStatus("mandatory")
_KmGroupEntryNumber_Type = Integer32
_KmGroupEntryNumber_Object = MibTableColumn
kmGroupEntryNumber = _KmGroupEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 7),
    _KmGroupEntryNumber_Type()
)
kmGroupEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupEntryNumber.setStatus("mandatory")


class _KmGroupSecurityMode_Type(Integer32):
    """Custom type kmGroupSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("strong", 1))
    )


_KmGroupSecurityMode_Type.__name__ = "Integer32"
_KmGroupSecurityMode_Object = MibTableColumn
kmGroupSecurityMode = _KmGroupSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 8),
    _KmGroupSecurityMode_Type()
)
kmGroupSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupSecurityMode.setStatus("mandatory")
_KmGroupDataStatus_Type = Integer32
_KmGroupDataStatus_Object = MibTableColumn
kmGroupDataStatus = _KmGroupDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 9),
    _KmGroupDataStatus_Type()
)
kmGroupDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupDataStatus.setStatus("mandatory")
_KmGroupAccountMode_Type = Integer32
_KmGroupAccountMode_Object = MibTableColumn
kmGroupAccountMode = _KmGroupAccountMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 10),
    _KmGroupAccountMode_Type()
)
kmGroupAccountMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountMode.setStatus("mandatory")


class _KmGroupChangeAdminCode_Type(DisplayString):
    """Custom type kmGroupChangeAdminCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KmGroupChangeAdminCode_Type.__name__ = "DisplayString"
_KmGroupChangeAdminCode_Object = MibTableColumn
kmGroupChangeAdminCode = _KmGroupChangeAdminCode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 11),
    _KmGroupChangeAdminCode_Type()
)
kmGroupChangeAdminCode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kmGroupChangeAdminCode.setStatus("mandatory")
_KmGroupAccountBalanceBase_Type = Integer32
_KmGroupAccountBalanceBase_Object = MibTableColumn
kmGroupAccountBalanceBase = _KmGroupAccountBalanceBase_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 12),
    _KmGroupAccountBalanceBase_Type()
)
kmGroupAccountBalanceBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupAccountBalanceBase.setStatus("mandatory")
_KmGroupAccountBalanceMax_Type = Integer32
_KmGroupAccountBalanceMax_Object = MibTableColumn
kmGroupAccountBalanceMax = _KmGroupAccountBalanceMax_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 13),
    _KmGroupAccountBalanceMax_Type()
)
kmGroupAccountBalanceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupAccountBalanceMax.setStatus("mandatory")
_KmGroupAccountErrorReport_Type = Integer32
_KmGroupAccountErrorReport_Object = MibTableColumn
kmGroupAccountErrorReport = _KmGroupAccountErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 14),
    _KmGroupAccountErrorReport_Type()
)
kmGroupAccountErrorReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountErrorReport.setStatus("mandatory")
_KmGroupAccountErrorCancel_Type = Integer32
_KmGroupAccountErrorCancel_Object = MibTableColumn
kmGroupAccountErrorCancel = _KmGroupAccountErrorCancel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 15),
    _KmGroupAccountErrorCancel_Type()
)
kmGroupAccountErrorCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountErrorCancel.setStatus("mandatory")


class _KmGroupAccountPrintPermission_Type(Integer32):
    """Custom type kmGroupAccountPrintPermission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prohibit", 0),
          ("permit", 1))
    )


_KmGroupAccountPrintPermission_Type.__name__ = "Integer32"
_KmGroupAccountPrintPermission_Object = MibTableColumn
kmGroupAccountPrintPermission = _KmGroupAccountPrintPermission_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 16),
    _KmGroupAccountPrintPermission_Type()
)
kmGroupAccountPrintPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountPrintPermission.setStatus("mandatory")


class _KmGroupAccountBalancePattern_Type(Integer32):
    """Custom type kmGroupAccountBalancePattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("printCopy", 1),
          ("eachFunction", 2))
    )


_KmGroupAccountBalancePattern_Type.__name__ = "Integer32"
_KmGroupAccountBalancePattern_Object = MibTableColumn
kmGroupAccountBalancePattern = _KmGroupAccountBalancePattern_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 17),
    _KmGroupAccountBalancePattern_Type()
)
kmGroupAccountBalancePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountBalancePattern.setStatus("mandatory")


class _KmGroupAccountModeMain_Type(Integer32):
    """Custom type kmGroupAccountModeMain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KmGroupAccountModeMain_Type.__name__ = "Integer32"
_KmGroupAccountModeMain_Object = MibTableColumn
kmGroupAccountModeMain = _KmGroupAccountModeMain_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 1, 1, 18),
    _KmGroupAccountModeMain_Type()
)
kmGroupAccountModeMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountModeMain.setStatus("mandatory")
_KmGroupTable_Object = MibTable
kmGroupTable = _KmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    kmGroupTable.setStatus("mandatory")
_KmGroupEntry_Object = MibTableRow
kmGroupEntry = _KmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1)
)
kmGroupEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmGroupIndex"),
)
if mibBuilder.loadTexts:
    kmGroupEntry.setStatus("mandatory")
_KmGroupIndex_Type = Integer32
_KmGroupIndex_Object = MibTableColumn
kmGroupIndex = _KmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 1),
    _KmGroupIndex_Type()
)
kmGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmGroupIndex.setStatus("mandatory")


class _KmGroupAccountNumber_Type(DisplayString):
    """Custom type kmGroupAccountNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_KmGroupAccountNumber_Type.__name__ = "DisplayString"
_KmGroupAccountNumber_Object = MibTableColumn
kmGroupAccountNumber = _KmGroupAccountNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 2),
    _KmGroupAccountNumber_Type()
)
kmGroupAccountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupAccountNumber.setStatus("mandatory")


class _KmGroupCaption_Type(DisplayString):
    """Custom type kmGroupCaption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmGroupCaption_Type.__name__ = "DisplayString"
_KmGroupCaption_Object = MibTableColumn
kmGroupCaption = _KmGroupCaption_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 3),
    _KmGroupCaption_Type()
)
kmGroupCaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupCaption.setStatus("mandatory")
_KmGroupPrinterCSetRef_Type = Integer32
_KmGroupPrinterCSetRef_Object = MibTableColumn
kmGroupPrinterCSetRef = _KmGroupPrinterCSetRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 4),
    _KmGroupPrinterCSetRef_Type()
)
kmGroupPrinterCSetRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupPrinterCSetRef.setStatus("mandatory")
_KmGroupCopierCSetRef_Type = Integer32
_KmGroupCopierCSetRef_Object = MibTableColumn
kmGroupCopierCSetRef = _KmGroupCopierCSetRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 5),
    _KmGroupCopierCSetRef_Type()
)
kmGroupCopierCSetRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupCopierCSetRef.setStatus("mandatory")
_KmGroupFAXCSetRef_Type = Integer32
_KmGroupFAXCSetRef_Object = MibTableColumn
kmGroupFAXCSetRef = _KmGroupFAXCSetRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 6),
    _KmGroupFAXCSetRef_Type()
)
kmGroupFAXCSetRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupFAXCSetRef.setStatus("mandatory")
_KmGroupScannerCSetRef_Type = Integer32
_KmGroupScannerCSetRef_Object = MibTableColumn
kmGroupScannerCSetRef = _KmGroupScannerCSetRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 7),
    _KmGroupScannerCSetRef_Type()
)
kmGroupScannerCSetRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupScannerCSetRef.setStatus("mandatory")
_KmGroupAccountBalance_Type = Integer32
_KmGroupAccountBalance_Object = MibTableColumn
kmGroupAccountBalance = _KmGroupAccountBalance_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 8),
    _KmGroupAccountBalance_Type()
)
kmGroupAccountBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupAccountBalance.setStatus("mandatory")


class _KmGroupAccountUnit_Type(Integer32):
    """Custom type kmGroupAccountUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("impressions", 7),
          ("sheets", 8))
    )


_KmGroupAccountUnit_Type.__name__ = "Integer32"
_KmGroupAccountUnit_Object = MibTableColumn
kmGroupAccountUnit = _KmGroupAccountUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 9),
    _KmGroupAccountUnit_Type()
)
kmGroupAccountUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupAccountUnit.setStatus("mandatory")


class _KmGroupAccountStatus_Type(Integer32):
    """Custom type kmGroupAccountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("locked", 1))
    )


_KmGroupAccountStatus_Type.__name__ = "Integer32"
_KmGroupAccountStatus_Object = MibTableColumn
kmGroupAccountStatus = _KmGroupAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 10),
    _KmGroupAccountStatus_Type()
)
kmGroupAccountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupAccountStatus.setStatus("mandatory")


class _KmGroupAccountReset_Type(DisplayString):
    """Custom type kmGroupAccountReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KmGroupAccountReset_Type.__name__ = "DisplayString"
_KmGroupAccountReset_Object = MibTableColumn
kmGroupAccountReset = _KmGroupAccountReset_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 11),
    _KmGroupAccountReset_Type()
)
kmGroupAccountReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kmGroupAccountReset.setStatus("mandatory")


class _KmGroupSubCaption_Type(DisplayString):
    """Custom type kmGroupSubCaption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmGroupSubCaption_Type.__name__ = "DisplayString"
_KmGroupSubCaption_Object = MibTableColumn
kmGroupSubCaption = _KmGroupSubCaption_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 12),
    _KmGroupSubCaption_Type()
)
kmGroupSubCaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupSubCaption.setStatus("mandatory")
_KmGroupFAXReceiveCSetRef_Type = Integer32
_KmGroupFAXReceiveCSetRef_Object = MibTableColumn
kmGroupFAXReceiveCSetRef = _KmGroupFAXReceiveCSetRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 13),
    _KmGroupFAXReceiveCSetRef_Type()
)
kmGroupFAXReceiveCSetRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupFAXReceiveCSetRef.setStatus("mandatory")
_KmGroupMediaKindCSetRef_Type = Integer32
_KmGroupMediaKindCSetRef_Object = MibTableColumn
kmGroupMediaKindCSetRef = _KmGroupMediaKindCSetRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 14),
    _KmGroupMediaKindCSetRef_Type()
)
kmGroupMediaKindCSetRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupMediaKindCSetRef.setStatus("mandatory")
_KmGroupFAXSendTime_Type = Integer32
_KmGroupFAXSendTime_Object = MibTableColumn
kmGroupFAXSendTime = _KmGroupFAXSendTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 2, 1, 15),
    _KmGroupFAXSendTime_Type()
)
kmGroupFAXSendTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmGroupFAXSendTime.setStatus("mandatory")
_KmGroupMediaKindTable_Object = MibTable
kmGroupMediaKindTable = _KmGroupMediaKindTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    kmGroupMediaKindTable.setStatus("mandatory")
_KmGroupMediaKindEntry_Object = MibTableRow
kmGroupMediaKindEntry = _KmGroupMediaKindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 3, 1)
)
kmGroupMediaKindEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmGroupMediaKindIndex"),
)
if mibBuilder.loadTexts:
    kmGroupMediaKindEntry.setStatus("mandatory")
_KmGroupMediaKindIndex_Type = Integer32
_KmGroupMediaKindIndex_Object = MibTableColumn
kmGroupMediaKindIndex = _KmGroupMediaKindIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 3, 1, 1),
    _KmGroupMediaKindIndex_Type()
)
kmGroupMediaKindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmGroupMediaKindIndex.setStatus("mandatory")
_KmGroupMediaSizeIndex_Type = Integer32
_KmGroupMediaSizeIndex_Object = MibTableColumn
kmGroupMediaSizeIndex = _KmGroupMediaSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 3, 1, 2),
    _KmGroupMediaSizeIndex_Type()
)
kmGroupMediaSizeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupMediaSizeIndex.setStatus("mandatory")
_KmGroupMediaTypeIndex_Type = Integer32
_KmGroupMediaTypeIndex_Object = MibTableColumn
kmGroupMediaTypeIndex = _KmGroupMediaTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 1, 2, 1, 3, 1, 3),
    _KmGroupMediaTypeIndex_Type()
)
kmGroupMediaTypeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmGroupMediaTypeIndex.setStatus("mandatory")
_KmResource_ObjectIdentity = ObjectIdentity
kmResource = _KmResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2)
)
_KmMedia_ObjectIdentity = ObjectIdentity
kmMedia = _KmMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1)
)
_KmMediaTable_Object = MibTable
kmMediaTable = _KmMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    kmMediaTable.setStatus("mandatory")
_KmMediaEntry_Object = MibTableRow
kmMediaEntry = _KmMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1)
)
kmMediaEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmMediaIndex"),
)
if mibBuilder.loadTexts:
    kmMediaEntry.setStatus("mandatory")
_KmMediaIndex_Type = Integer32
_KmMediaIndex_Object = MibTableColumn
kmMediaIndex = _KmMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1, 1),
    _KmMediaIndex_Type()
)
kmMediaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmMediaIndex.setStatus("mandatory")


class _KmMediaName_Type(DisplayString):
    """Custom type kmMediaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmMediaName_Type.__name__ = "DisplayString"
_KmMediaName_Object = MibTableColumn
kmMediaName = _KmMediaName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1, 2),
    _KmMediaName_Type()
)
kmMediaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMediaName.setStatus("mandatory")


class _KmMediaSizeUnit_Type(Integer32):
    """Custom type kmMediaSizeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenThousandthsOfInches", 3),
          ("micrometers", 4))
    )


_KmMediaSizeUnit_Type.__name__ = "Integer32"
_KmMediaSizeUnit_Object = MibTableColumn
kmMediaSizeUnit = _KmMediaSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1, 3),
    _KmMediaSizeUnit_Type()
)
kmMediaSizeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMediaSizeUnit.setStatus("mandatory")
_KmMediaLongEdgeSize_Type = Integer32
_KmMediaLongEdgeSize_Object = MibTableColumn
kmMediaLongEdgeSize = _KmMediaLongEdgeSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1, 4),
    _KmMediaLongEdgeSize_Type()
)
kmMediaLongEdgeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMediaLongEdgeSize.setStatus("mandatory")
_KmMediaShortEdgeSize_Type = Integer32
_KmMediaShortEdgeSize_Object = MibTableColumn
kmMediaShortEdgeSize = _KmMediaShortEdgeSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1, 5),
    _KmMediaShortEdgeSize_Type()
)
kmMediaShortEdgeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMediaShortEdgeSize.setStatus("mandatory")
_KmMediaCounterItem_Type = Integer32
_KmMediaCounterItem_Object = MibTableColumn
kmMediaCounterItem = _KmMediaCounterItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 1, 1, 1, 6),
    _KmMediaCounterItem_Type()
)
kmMediaCounterItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMediaCounterItem.setStatus("mandatory")
_KmColorMode_ObjectIdentity = ObjectIdentity
kmColorMode = _KmColorMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 2)
)
_KmColorModeTable_Object = MibTable
kmColorModeTable = _KmColorModeTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    kmColorModeTable.setStatus("mandatory")
_KmColorModeEntry_Object = MibTableRow
kmColorModeEntry = _KmColorModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 2, 1, 1)
)
kmColorModeEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmColorModeIndex"),
)
if mibBuilder.loadTexts:
    kmColorModeEntry.setStatus("mandatory")
_KmColorModeIndex_Type = Integer32
_KmColorModeIndex_Object = MibTableColumn
kmColorModeIndex = _KmColorModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 2, 1, 1, 1),
    _KmColorModeIndex_Type()
)
kmColorModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmColorModeIndex.setStatus("mandatory")


class _KmColorModeName_Type(DisplayString):
    """Custom type kmColorModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmColorModeName_Type.__name__ = "DisplayString"
_KmColorModeName_Object = MibTableColumn
kmColorModeName = _KmColorModeName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 2, 1, 1, 2),
    _KmColorModeName_Type()
)
kmColorModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmColorModeName.setStatus("mandatory")
_KmColorModeCounterItem_Type = Integer32
_KmColorModeCounterItem_Object = MibTableColumn
kmColorModeCounterItem = _KmColorModeCounterItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 2, 2, 1, 1, 3),
    _KmColorModeCounterItem_Type()
)
kmColorModeCounterItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmColorModeCounterItem.setStatus("mandatory")
_KmMFP_ObjectIdentity = ObjectIdentity
kmMFP = _KmMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3)
)
_KmMFPCounter_ObjectIdentity = ObjectIdentity
kmMFPCounter = _KmMFPCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1)
)
_KmMFPCounterTable_Object = MibTable
kmMFPCounterTable = _KmMFPCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 1)
)
if mibBuilder.loadTexts:
    kmMFPCounterTable.setStatus("mandatory")
_KmMFPCounterEntry_Object = MibTableRow
kmMFPCounterEntry = _KmMFPCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 1, 1)
)
kmMFPCounterEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPCounterEntry.setStatus("mandatory")
_KmMFPCounterItem_Type = Integer32
_KmMFPCounterItem_Object = MibTableColumn
kmMFPCounterItem = _KmMFPCounterItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 1, 1, 1),
    _KmMFPCounterItem_Type()
)
kmMFPCounterItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPCounterItem.setStatus("mandatory")
_KmMFPColorModeCounterTable_Object = MibTable
kmMFPColorModeCounterTable = _KmMFPColorModeCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 2)
)
if mibBuilder.loadTexts:
    kmMFPColorModeCounterTable.setStatus("mandatory")
_KmMFPColorModeCounterEntry_Object = MibTableRow
kmMFPColorModeCounterEntry = _KmMFPColorModeCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 2, 1)
)
kmMFPColorModeCounterEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmColorModeIndex"),
)
if mibBuilder.loadTexts:
    kmMFPColorModeCounterEntry.setStatus("mandatory")
_KmMFPColorModeCounterItem_Type = Integer32
_KmMFPColorModeCounterItem_Object = MibTableColumn
kmMFPColorModeCounterItem = _KmMFPColorModeCounterItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 2, 1, 1),
    _KmMFPColorModeCounterItem_Type()
)
kmMFPColorModeCounterItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPColorModeCounterItem.setStatus("mandatory")
_KmMFPScanCounterTable_Object = MibTable
kmMFPScanCounterTable = _KmMFPScanCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 3)
)
if mibBuilder.loadTexts:
    kmMFPScanCounterTable.setStatus("mandatory")
_KmMFPScanCounterEntry_Object = MibTableRow
kmMFPScanCounterEntry = _KmMFPScanCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 3, 1)
)
kmMFPScanCounterEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPScanCounterEntry.setStatus("mandatory")
_KmMFPScanCounterItem_Type = Integer32
_KmMFPScanCounterItem_Object = MibTableColumn
kmMFPScanCounterItem = _KmMFPScanCounterItem_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 1, 3, 1, 1),
    _KmMFPScanCounterItem_Type()
)
kmMFPScanCounterItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPScanCounterItem.setStatus("mandatory")
_KmMFPDevice_ObjectIdentity = ObjectIdentity
kmMFPDevice = _KmMFPDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2)
)
_KmMFPDevicePrinter_ObjectIdentity = ObjectIdentity
kmMFPDevicePrinter = _KmMFPDevicePrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 1)
)
_KmMFPPrinterGeneralTable_Object = MibTable
kmMFPPrinterGeneralTable = _KmMFPPrinterGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    kmMFPPrinterGeneralTable.setStatus("mandatory")
_KmMFPPrinterGeneralEntry_Object = MibTableRow
kmMFPPrinterGeneralEntry = _KmMFPPrinterGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 1, 1, 1)
)
kmMFPPrinterGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPPrinterGeneralEntry.setStatus("mandatory")


class _KmMFPPrinterLocalization_Type(Integer32):
    """Custom type kmMFPPrinterLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              81)
        )
    )
    namedValues = NamedValues(
        *(("overSea", 1),
          ("japan", 81))
    )


_KmMFPPrinterLocalization_Type.__name__ = "Integer32"
_KmMFPPrinterLocalization_Object = MibTableColumn
kmMFPPrinterLocalization = _KmMFPPrinterLocalization_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 1, 1, 1, 1),
    _KmMFPPrinterLocalization_Type()
)
kmMFPPrinterLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPPrinterLocalization.setStatus("mandatory")
_KmMFPPrinterLocalSubCode_Type = Integer32
_KmMFPPrinterLocalSubCode_Object = MibTableColumn
kmMFPPrinterLocalSubCode = _KmMFPPrinterLocalSubCode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 1, 1, 1, 2),
    _KmMFPPrinterLocalSubCode_Type()
)
kmMFPPrinterLocalSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPPrinterLocalSubCode.setStatus("mandatory")
_KmMFPDeviceCopier_ObjectIdentity = ObjectIdentity
kmMFPDeviceCopier = _KmMFPDeviceCopier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 2)
)
_KmMFPCopierGeneralTable_Object = MibTable
kmMFPCopierGeneralTable = _KmMFPCopierGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    kmMFPCopierGeneralTable.setStatus("mandatory")
_KmMFPCopierGeneralEntry_Object = MibTableRow
kmMFPCopierGeneralEntry = _KmMFPCopierGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 2, 1, 1)
)
kmMFPCopierGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPCopierGeneralEntry.setStatus("mandatory")


class _KmMFPCopierLocalization_Type(Integer32):
    """Custom type kmMFPCopierLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              31,
              61,
              81)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("inch", 1),
          ("europeMetric", 31),
          ("asiaPacific", 61),
          ("japanMetric", 81))
    )


_KmMFPCopierLocalization_Type.__name__ = "Integer32"
_KmMFPCopierLocalization_Object = MibTableColumn
kmMFPCopierLocalization = _KmMFPCopierLocalization_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 2, 1, 1, 1),
    _KmMFPCopierLocalization_Type()
)
kmMFPCopierLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPCopierLocalization.setStatus("mandatory")
_KmMFPCopierLocalSubCode_Type = Integer32
_KmMFPCopierLocalSubCode_Object = MibTableColumn
kmMFPCopierLocalSubCode = _KmMFPCopierLocalSubCode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 2, 1, 1, 2),
    _KmMFPCopierLocalSubCode_Type()
)
kmMFPCopierLocalSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPCopierLocalSubCode.setStatus("mandatory")
_KmMFPDeviceScanner_ObjectIdentity = ObjectIdentity
kmMFPDeviceScanner = _KmMFPDeviceScanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3)
)
_KmMFPScannerGeneralTable_Object = MibTable
kmMFPScannerGeneralTable = _KmMFPScannerGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    kmMFPScannerGeneralTable.setStatus("mandatory")
_KmMFPScannerGeneralEntry_Object = MibTableRow
kmMFPScannerGeneralEntry = _KmMFPScannerGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 1, 1)
)
kmMFPScannerGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPScannerGeneralEntry.setStatus("mandatory")


class _KmMFPScannerLocalization_Type(Integer32):
    """Custom type kmMFPScannerLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              31,
              61,
              81)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("inch", 1),
          ("europeMetric", 31),
          ("asiaPacific", 61),
          ("japanMetric", 81))
    )


_KmMFPScannerLocalization_Type.__name__ = "Integer32"
_KmMFPScannerLocalization_Object = MibTableColumn
kmMFPScannerLocalization = _KmMFPScannerLocalization_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 1, 1, 1),
    _KmMFPScannerLocalization_Type()
)
kmMFPScannerLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPScannerLocalization.setStatus("mandatory")
_KmMFPScannerLocalSubCode_Type = Integer32
_KmMFPScannerLocalSubCode_Object = MibTableColumn
kmMFPScannerLocalSubCode = _KmMFPScannerLocalSubCode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 1, 1, 2),
    _KmMFPScannerLocalSubCode_Type()
)
kmMFPScannerLocalSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPScannerLocalSubCode.setStatus("mandatory")


class _KmMFPScannerAccountMode_Type(Integer32):
    """Custom type kmMFPScannerAccountMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imageScan", 1),
          ("networkScan", 2))
    )


_KmMFPScannerAccountMode_Type.__name__ = "Integer32"
_KmMFPScannerAccountMode_Object = MibTableColumn
kmMFPScannerAccountMode = _KmMFPScannerAccountMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 1, 1, 3),
    _KmMFPScannerAccountMode_Type()
)
kmMFPScannerAccountMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPScannerAccountMode.setStatus("mandatory")
_KmMFPScannerDocProcessorTable_Object = MibTable
kmMFPScannerDocProcessorTable = _KmMFPScannerDocProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    kmMFPScannerDocProcessorTable.setStatus("mandatory")
_KmMFPScannerDocProcessorEntry_Object = MibTableRow
kmMFPScannerDocProcessorEntry = _KmMFPScannerDocProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 2, 1)
)
kmMFPScannerDocProcessorEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KMCOMMON-MIB", "kmMFPDocProcessorIndex"),
)
if mibBuilder.loadTexts:
    kmMFPScannerDocProcessorEntry.setStatus("mandatory")
_KmMFPDocProcessorIndex_Type = Integer32
_KmMFPDocProcessorIndex_Object = MibTableColumn
kmMFPDocProcessorIndex = _KmMFPDocProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 2, 1, 1),
    _KmMFPDocProcessorIndex_Type()
)
kmMFPDocProcessorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kmMFPDocProcessorIndex.setStatus("mandatory")


class _KmMFPDocProcessorModel_Type(DisplayString):
    """Custom type kmMFPDocProcessorModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmMFPDocProcessorModel_Type.__name__ = "DisplayString"
_KmMFPDocProcessorModel_Object = MibTableColumn
kmMFPDocProcessorModel = _KmMFPDocProcessorModel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 2, 1, 2),
    _KmMFPDocProcessorModel_Type()
)
kmMFPDocProcessorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPDocProcessorModel.setStatus("mandatory")


class _KmMFPDocProcessorAbsolteModel_Type(DisplayString):
    """Custom type kmMFPDocProcessorAbsolteModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmMFPDocProcessorAbsolteModel_Type.__name__ = "DisplayString"
_KmMFPDocProcessorAbsolteModel_Object = MibTableColumn
kmMFPDocProcessorAbsolteModel = _KmMFPDocProcessorAbsolteModel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 3, 2, 1, 3),
    _KmMFPDocProcessorAbsolteModel_Type()
)
kmMFPDocProcessorAbsolteModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPDocProcessorAbsolteModel.setStatus("mandatory")
_KmMFPDeviceFAX_ObjectIdentity = ObjectIdentity
kmMFPDeviceFAX = _KmMFPDeviceFAX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 4)
)
_KmMFPFAXGeneralTable_Object = MibTable
kmMFPFAXGeneralTable = _KmMFPFAXGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    kmMFPFAXGeneralTable.setStatus("mandatory")
_KmMFPFAXGeneralEntry_Object = MibTableRow
kmMFPFAXGeneralEntry = _KmMFPFAXGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 4, 1, 1)
)
kmMFPFAXGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPFAXGeneralEntry.setStatus("mandatory")


class _KmMFPFAXLocalization_Type(Integer32):
    """Custom type kmMFPFAXLocalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              31,
              61,
              81)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("inch", 1),
          ("europeMetric", 31),
          ("asiaPacific", 61),
          ("japanMetric", 81))
    )


_KmMFPFAXLocalization_Type.__name__ = "Integer32"
_KmMFPFAXLocalization_Object = MibTableColumn
kmMFPFAXLocalization = _KmMFPFAXLocalization_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 4, 1, 1, 1),
    _KmMFPFAXLocalization_Type()
)
kmMFPFAXLocalization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPFAXLocalization.setStatus("mandatory")
_KmMFPFAXLocalSubCode_Type = Integer32
_KmMFPFAXLocalSubCode_Object = MibTableColumn
kmMFPFAXLocalSubCode = _KmMFPFAXLocalSubCode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 4, 1, 1, 2),
    _KmMFPFAXLocalSubCode_Type()
)
kmMFPFAXLocalSubCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPFAXLocalSubCode.setStatus("mandatory")
_KmMFPDeviceGeneral_ObjectIdentity = ObjectIdentity
kmMFPDeviceGeneral = _KmMFPDeviceGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 5)
)
_KmMFPGeneralTable_Object = MibTable
kmMFPGeneralTable = _KmMFPGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    kmMFPGeneralTable.setStatus("mandatory")
_KmMFPGeneralEntry_Object = MibTableRow
kmMFPGeneralEntry = _KmMFPGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 5, 1, 1)
)
kmMFPGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmMFPGeneralEntry.setStatus("mandatory")
_KmMFPFunctionControl_Type = Integer32
_KmMFPFunctionControl_Object = MibTableColumn
kmMFPFunctionControl = _KmMFPFunctionControl_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 5, 1, 1, 1),
    _KmMFPFunctionControl_Type()
)
kmMFPFunctionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmMFPFunctionControl.setStatus("optional")


class _KmMFPDeviceDateTime_Type(DisplayString):
    """Custom type kmMFPDeviceDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_KmMFPDeviceDateTime_Type.__name__ = "DisplayString"
_KmMFPDeviceDateTime_Object = MibTableColumn
kmMFPDeviceDateTime = _KmMFPDeviceDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 3, 2, 5, 1, 1, 2),
    _KmMFPDeviceDateTime_Type()
)
kmMFPDeviceDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmMFPDeviceDateTime.setStatus("optional")
_KmGeneral_ObjectIdentity = ObjectIdentity
kmGeneral = _KmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5)
)
_KmGeneralTable_Object = MibTable
kmGeneralTable = _KmGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1)
)
if mibBuilder.loadTexts:
    kmGeneralTable.setStatus("mandatory")
_KmGeneralEntry_Object = MibTableRow
kmGeneralEntry = _KmGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1)
)
kmGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kmGeneralEntry.setStatus("mandatory")


class _KmProductName_Type(DisplayString):
    """Custom type kmProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmProductName_Type.__name__ = "DisplayString"
_KmProductName_Object = MibTableColumn
kmProductName = _KmProductName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 1),
    _KmProductName_Type()
)
kmProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmProductName.setStatus("mandatory")


class _KmAbsoluteName_Type(DisplayString):
    """Custom type kmAbsoluteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KmAbsoluteName_Type.__name__ = "DisplayString"
_KmAbsoluteName_Object = MibTableColumn
kmAbsoluteName = _KmAbsoluteName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 2),
    _KmAbsoluteName_Type()
)
kmAbsoluteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmAbsoluteName.setStatus("mandatory")


class _KmDefaultAgent_Type(Integer32):
    """Custom type kmDefaultAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("status", 1),
          ("copy", 2),
          ("send", 3),
          ("docbox", 4))
    )


_KmDefaultAgent_Type.__name__ = "Integer32"
_KmDefaultAgent_Object = MibTableColumn
kmDefaultAgent = _KmDefaultAgent_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 3),
    _KmDefaultAgent_Type()
)
kmDefaultAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmDefaultAgent.setStatus("mandatory")
_KmAgentResumeMode_Type = PresentOnOff
_KmAgentResumeMode_Object = MibTableColumn
kmAgentResumeMode = _KmAgentResumeMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 4),
    _KmAgentResumeMode_Type()
)
kmAgentResumeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmAgentResumeMode.setStatus("mandatory")


class _KmAgentResumeTimeout_Type(Integer32):
    """Custom type kmAgentResumeTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_KmAgentResumeTimeout_Type.__name__ = "Integer32"
_KmAgentResumeTimeout_Object = MibTableColumn
kmAgentResumeTimeout = _KmAgentResumeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 5),
    _KmAgentResumeTimeout_Type()
)
kmAgentResumeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmAgentResumeTimeout.setStatus("mandatory")
_KmOneTouchKeyNum_Type = Integer32
_KmOneTouchKeyNum_Object = MibTableColumn
kmOneTouchKeyNum = _KmOneTouchKeyNum_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 8),
    _KmOneTouchKeyNum_Type()
)
kmOneTouchKeyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmOneTouchKeyNum.setStatus("mandatory")
_KmOneTouchShiftNum_Type = Integer32
_KmOneTouchShiftNum_Object = MibTableColumn
kmOneTouchShiftNum = _KmOneTouchShiftNum_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 9),
    _KmOneTouchShiftNum_Type()
)
kmOneTouchShiftNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmOneTouchShiftNum.setStatus("mandatory")


class _KmLocalTime_Type(OctetString):
    """Custom type kmLocalTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_KmLocalTime_Type.__name__ = "OctetString"
_KmLocalTime_Object = MibTableColumn
kmLocalTime = _KmLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 10),
    _KmLocalTime_Type()
)
kmLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmLocalTime.setStatus("mandatory")


class _KmTimeFormat_Type(OctetString):
    """Custom type kmTimeFormat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_KmTimeFormat_Type.__name__ = "OctetString"
_KmTimeFormat_Object = MibTableColumn
kmTimeFormat = _KmTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 11),
    _KmTimeFormat_Type()
)
kmTimeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kmTimeFormat.setStatus("mandatory")
_KmTimeZone_Type = Integer32
_KmTimeZone_Object = MibTableColumn
kmTimeZone = _KmTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 12),
    _KmTimeZone_Type()
)
kmTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmTimeZone.setStatus("mandatory")


class _KmPanelSizeUnit_Type(Integer32):
    """Custom type kmPanelSizeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenThousandthsOfInches", 3),
          ("micrometers", 4))
    )


_KmPanelSizeUnit_Type.__name__ = "Integer32"
_KmPanelSizeUnit_Object = MibTableColumn
kmPanelSizeUnit = _KmPanelSizeUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 13),
    _KmPanelSizeUnit_Type()
)
kmPanelSizeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmPanelSizeUnit.setStatus("mandatory")
_KmPrescribeEscape_Type = Integer32
_KmPrescribeEscape_Object = MibTableColumn
kmPrescribeEscape = _KmPrescribeEscape_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 14),
    _KmPrescribeEscape_Type()
)
kmPrescribeEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmPrescribeEscape.setStatus("mandatory")


class _KmConsoleDisableEx_Type(Integer32):
    """Custom type kmConsoleDisableEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("partialLock", 1),
          ("enabled", 3),
          ("disabled", 4))
    )


_KmConsoleDisableEx_Type.__name__ = "Integer32"
_KmConsoleDisableEx_Object = MibTableColumn
kmConsoleDisableEx = _KmConsoleDisableEx_Object(
    (1, 3, 6, 1, 4, 1, 1347, 42, 5, 1, 1, 15),
    _KmConsoleDisableEx_Type()
)
kmConsoleDisableEx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kmConsoleDisableEx.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KMCOMMON-MIB",
    **{"kyocera": kyocera,
       "kmCommon": kmCommon,
       "kmAccounting": kmAccounting,
       "kmCounterSet": kmCounterSet,
       "kmCounterSetTable": kmCounterSetTable,
       "kmCounterSetEntry": kmCounterSetEntry,
       "kmCounterSetIndex": kmCounterSetIndex,
       "kmCounterSetItemIndex": kmCounterSetItemIndex,
       "kmCounterItem": kmCounterItem,
       "kmCounterMediaRef": kmCounterMediaRef,
       "kmCounterColorModeRef": kmCounterColorModeRef,
       "kmAccountBalanceItem": kmAccountBalanceItem,
       "kmAccountBalanceStatus": kmAccountBalanceStatus,
       "kmAccountRestriction": kmAccountRestriction,
       "kmGroup": kmGroup,
       "kmGroupLevel1": kmGroupLevel1,
       "kmGroupConfigTable": kmGroupConfigTable,
       "kmGroupConfigEntry": kmGroupConfigEntry,
       "kmGroupCodeWidth": kmGroupCodeWidth,
       "kmGroupSecurityLock": kmGroupSecurityLock,
       "kmGroupUpdateCount": kmGroupUpdateCount,
       "kmGroupEntryCreate": kmGroupEntryCreate,
       "kmGroupEntryPurge": kmGroupEntryPurge,
       "kmGroupResetAll": kmGroupResetAll,
       "kmGroupEntryNumber": kmGroupEntryNumber,
       "kmGroupSecurityMode": kmGroupSecurityMode,
       "kmGroupDataStatus": kmGroupDataStatus,
       "kmGroupAccountMode": kmGroupAccountMode,
       "kmGroupChangeAdminCode": kmGroupChangeAdminCode,
       "kmGroupAccountBalanceBase": kmGroupAccountBalanceBase,
       "kmGroupAccountBalanceMax": kmGroupAccountBalanceMax,
       "kmGroupAccountErrorReport": kmGroupAccountErrorReport,
       "kmGroupAccountErrorCancel": kmGroupAccountErrorCancel,
       "kmGroupAccountPrintPermission": kmGroupAccountPrintPermission,
       "kmGroupAccountBalancePattern": kmGroupAccountBalancePattern,
       "kmGroupAccountModeMain": kmGroupAccountModeMain,
       "kmGroupTable": kmGroupTable,
       "kmGroupEntry": kmGroupEntry,
       "kmGroupIndex": kmGroupIndex,
       "kmGroupAccountNumber": kmGroupAccountNumber,
       "kmGroupCaption": kmGroupCaption,
       "kmGroupPrinterCSetRef": kmGroupPrinterCSetRef,
       "kmGroupCopierCSetRef": kmGroupCopierCSetRef,
       "kmGroupFAXCSetRef": kmGroupFAXCSetRef,
       "kmGroupScannerCSetRef": kmGroupScannerCSetRef,
       "kmGroupAccountBalance": kmGroupAccountBalance,
       "kmGroupAccountUnit": kmGroupAccountUnit,
       "kmGroupAccountStatus": kmGroupAccountStatus,
       "kmGroupAccountReset": kmGroupAccountReset,
       "kmGroupSubCaption": kmGroupSubCaption,
       "kmGroupFAXReceiveCSetRef": kmGroupFAXReceiveCSetRef,
       "kmGroupMediaKindCSetRef": kmGroupMediaKindCSetRef,
       "kmGroupFAXSendTime": kmGroupFAXSendTime,
       "kmGroupMediaKindTable": kmGroupMediaKindTable,
       "kmGroupMediaKindEntry": kmGroupMediaKindEntry,
       "kmGroupMediaKindIndex": kmGroupMediaKindIndex,
       "kmGroupMediaSizeIndex": kmGroupMediaSizeIndex,
       "kmGroupMediaTypeIndex": kmGroupMediaTypeIndex,
       "kmResource": kmResource,
       "kmMedia": kmMedia,
       "kmMediaTable": kmMediaTable,
       "kmMediaEntry": kmMediaEntry,
       "kmMediaIndex": kmMediaIndex,
       "kmMediaName": kmMediaName,
       "kmMediaSizeUnit": kmMediaSizeUnit,
       "kmMediaLongEdgeSize": kmMediaLongEdgeSize,
       "kmMediaShortEdgeSize": kmMediaShortEdgeSize,
       "kmMediaCounterItem": kmMediaCounterItem,
       "kmColorMode": kmColorMode,
       "kmColorModeTable": kmColorModeTable,
       "kmColorModeEntry": kmColorModeEntry,
       "kmColorModeIndex": kmColorModeIndex,
       "kmColorModeName": kmColorModeName,
       "kmColorModeCounterItem": kmColorModeCounterItem,
       "kmMFP": kmMFP,
       "kmMFPCounter": kmMFPCounter,
       "kmMFPCounterTable": kmMFPCounterTable,
       "kmMFPCounterEntry": kmMFPCounterEntry,
       "kmMFPCounterItem": kmMFPCounterItem,
       "kmMFPColorModeCounterTable": kmMFPColorModeCounterTable,
       "kmMFPColorModeCounterEntry": kmMFPColorModeCounterEntry,
       "kmMFPColorModeCounterItem": kmMFPColorModeCounterItem,
       "kmMFPScanCounterTable": kmMFPScanCounterTable,
       "kmMFPScanCounterEntry": kmMFPScanCounterEntry,
       "kmMFPScanCounterItem": kmMFPScanCounterItem,
       "kmMFPDevice": kmMFPDevice,
       "kmMFPDevicePrinter": kmMFPDevicePrinter,
       "kmMFPPrinterGeneralTable": kmMFPPrinterGeneralTable,
       "kmMFPPrinterGeneralEntry": kmMFPPrinterGeneralEntry,
       "kmMFPPrinterLocalization": kmMFPPrinterLocalization,
       "kmMFPPrinterLocalSubCode": kmMFPPrinterLocalSubCode,
       "kmMFPDeviceCopier": kmMFPDeviceCopier,
       "kmMFPCopierGeneralTable": kmMFPCopierGeneralTable,
       "kmMFPCopierGeneralEntry": kmMFPCopierGeneralEntry,
       "kmMFPCopierLocalization": kmMFPCopierLocalization,
       "kmMFPCopierLocalSubCode": kmMFPCopierLocalSubCode,
       "kmMFPDeviceScanner": kmMFPDeviceScanner,
       "kmMFPScannerGeneralTable": kmMFPScannerGeneralTable,
       "kmMFPScannerGeneralEntry": kmMFPScannerGeneralEntry,
       "kmMFPScannerLocalization": kmMFPScannerLocalization,
       "kmMFPScannerLocalSubCode": kmMFPScannerLocalSubCode,
       "kmMFPScannerAccountMode": kmMFPScannerAccountMode,
       "kmMFPScannerDocProcessorTable": kmMFPScannerDocProcessorTable,
       "kmMFPScannerDocProcessorEntry": kmMFPScannerDocProcessorEntry,
       "kmMFPDocProcessorIndex": kmMFPDocProcessorIndex,
       "kmMFPDocProcessorModel": kmMFPDocProcessorModel,
       "kmMFPDocProcessorAbsolteModel": kmMFPDocProcessorAbsolteModel,
       "kmMFPDeviceFAX": kmMFPDeviceFAX,
       "kmMFPFAXGeneralTable": kmMFPFAXGeneralTable,
       "kmMFPFAXGeneralEntry": kmMFPFAXGeneralEntry,
       "kmMFPFAXLocalization": kmMFPFAXLocalization,
       "kmMFPFAXLocalSubCode": kmMFPFAXLocalSubCode,
       "kmMFPDeviceGeneral": kmMFPDeviceGeneral,
       "kmMFPGeneralTable": kmMFPGeneralTable,
       "kmMFPGeneralEntry": kmMFPGeneralEntry,
       "kmMFPFunctionControl": kmMFPFunctionControl,
       "kmMFPDeviceDateTime": kmMFPDeviceDateTime,
       "kmGeneral": kmGeneral,
       "kmGeneralTable": kmGeneralTable,
       "kmGeneralEntry": kmGeneralEntry,
       "kmProductName": kmProductName,
       "kmAbsoluteName": kmAbsoluteName,
       "kmDefaultAgent": kmDefaultAgent,
       "kmAgentResumeMode": kmAgentResumeMode,
       "kmAgentResumeTimeout": kmAgentResumeTimeout,
       "kmOneTouchKeyNum": kmOneTouchKeyNum,
       "kmOneTouchShiftNum": kmOneTouchShiftNum,
       "kmLocalTime": kmLocalTime,
       "kmTimeFormat": kmTimeFormat,
       "kmTimeZone": kmTimeZone,
       "kmPanelSizeUnit": kmPanelSizeUnit,
       "kmPrescribeEscape": kmPrescribeEscape,
       "kmConsoleDisableEx": kmConsoleDisableEx}
)
