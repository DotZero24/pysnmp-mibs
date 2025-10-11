# SNMP MIB module (H3C-ISSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-ISSU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:06 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cIssuUpgrade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133)
)
if mibBuilder.loadTexts:
    h3cIssuUpgrade.setRevisions(
        ("2013-01-15 15:36",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cIssuUpgradeMibObjects_ObjectIdentity = ObjectIdentity
h3cIssuUpgradeMibObjects = _H3cIssuUpgradeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1)
)
_H3cIssuUpgradeGroup_ObjectIdentity = ObjectIdentity
h3cIssuUpgradeGroup = _H3cIssuUpgradeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1)
)
_H3cIssuUpgradeImageTable_Object = MibTable
h3cIssuUpgradeImageTable = _H3cIssuUpgradeImageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIssuUpgradeImageTable.setStatus("current")
_H3cIssuUpgradeImageEntry_Object = MibTableRow
h3cIssuUpgradeImageEntry = _H3cIssuUpgradeImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 1, 1)
)
h3cIssuUpgradeImageEntry.setIndexNames(
    (0, "H3C-ISSU-MIB", "h3cIssuUpgradeImageIndex"),
)
if mibBuilder.loadTexts:
    h3cIssuUpgradeImageEntry.setStatus("current")


class _H3cIssuUpgradeImageIndex_Type(Integer32):
    """Custom type h3cIssuUpgradeImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIssuUpgradeImageIndex_Type.__name__ = "Integer32"
_H3cIssuUpgradeImageIndex_Object = MibTableColumn
h3cIssuUpgradeImageIndex = _H3cIssuUpgradeImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 1, 1, 1),
    _H3cIssuUpgradeImageIndex_Type()
)
h3cIssuUpgradeImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIssuUpgradeImageIndex.setStatus("current")


class _H3cIssuUpgradeImageType_Type(Integer32):
    """Custom type h3cIssuUpgradeImageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("system", 2),
          ("feature", 3),
          ("ipe", 4),
          ("patch", 5))
    )


_H3cIssuUpgradeImageType_Type.__name__ = "Integer32"
_H3cIssuUpgradeImageType_Object = MibTableColumn
h3cIssuUpgradeImageType = _H3cIssuUpgradeImageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 1, 1, 2),
    _H3cIssuUpgradeImageType_Type()
)
h3cIssuUpgradeImageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIssuUpgradeImageType.setStatus("current")


class _H3cIssuUpgradeImageURL_Type(DisplayString):
    """Custom type h3cIssuUpgradeImageURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cIssuUpgradeImageURL_Type.__name__ = "DisplayString"
_H3cIssuUpgradeImageURL_Object = MibTableColumn
h3cIssuUpgradeImageURL = _H3cIssuUpgradeImageURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 1, 1, 3),
    _H3cIssuUpgradeImageURL_Type()
)
h3cIssuUpgradeImageURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIssuUpgradeImageURL.setStatus("current")
_H3cIssuUpgradeImageRowStatus_Type = RowStatus
_H3cIssuUpgradeImageRowStatus_Object = MibTableColumn
h3cIssuUpgradeImageRowStatus = _H3cIssuUpgradeImageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 1, 1, 4),
    _H3cIssuUpgradeImageRowStatus_Type()
)
h3cIssuUpgradeImageRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIssuUpgradeImageRowStatus.setStatus("current")
_H3cIssuOp_ObjectIdentity = ObjectIdentity
h3cIssuOp = _H3cIssuOp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2)
)


class _H3cIssuOpType_Type(Integer32):
    """Custom type h3cIssuOpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("done", 2),
          ("test", 3),
          ("install", 4),
          ("rollback", 5))
    )


_H3cIssuOpType_Type.__name__ = "Integer32"
_H3cIssuOpType_Object = MibScalar
h3cIssuOpType = _H3cIssuOpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 1),
    _H3cIssuOpType_Type()
)
h3cIssuOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIssuOpType.setStatus("current")


class _H3cIssuImageFileOverwrite_Type(TruthValue):
    """Custom type h3cIssuImageFileOverwrite based on TruthValue"""
    defaultValue = 1


_H3cIssuImageFileOverwrite_Type.__name__ = "TruthValue"
_H3cIssuImageFileOverwrite_Object = MibScalar
h3cIssuImageFileOverwrite = _H3cIssuImageFileOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 2),
    _H3cIssuImageFileOverwrite_Type()
)
h3cIssuImageFileOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIssuImageFileOverwrite.setStatus("current")


class _H3cIssuOpTrapEnable_Type(TruthValue):
    """Custom type h3cIssuOpTrapEnable based on TruthValue"""
    defaultValue = 1


_H3cIssuOpTrapEnable_Type.__name__ = "TruthValue"
_H3cIssuOpTrapEnable_Object = MibScalar
h3cIssuOpTrapEnable = _H3cIssuOpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 3),
    _H3cIssuOpTrapEnable_Type()
)
h3cIssuOpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIssuOpTrapEnable.setStatus("current")


class _H3cIssuOpStatus_Type(Integer32):
    """Custom type h3cIssuOpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("failure", 2),
          ("inProgress", 3),
          ("success", 4),
          ("rollbackInProgress", 5),
          ("rollbackSuccess", 6))
    )


_H3cIssuOpStatus_Type.__name__ = "Integer32"
_H3cIssuOpStatus_Object = MibScalar
h3cIssuOpStatus = _H3cIssuOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 4),
    _H3cIssuOpStatus_Type()
)
h3cIssuOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuOpStatus.setStatus("current")


class _H3cIssuFailedReason_Type(DisplayString):
    """Custom type h3cIssuFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIssuFailedReason_Type.__name__ = "DisplayString"
_H3cIssuFailedReason_Object = MibScalar
h3cIssuFailedReason = _H3cIssuFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 5),
    _H3cIssuFailedReason_Type()
)
h3cIssuFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuFailedReason.setStatus("current")


class _H3cIssuOpTimeCompleted_Type(DisplayString):
    """Custom type h3cIssuOpTimeCompleted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIssuOpTimeCompleted_Type.__name__ = "DisplayString"
_H3cIssuOpTimeCompleted_Object = MibScalar
h3cIssuOpTimeCompleted = _H3cIssuOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 6),
    _H3cIssuOpTimeCompleted_Type()
)
h3cIssuOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuOpTimeCompleted.setStatus("current")


class _H3cIssuLastOpType_Type(Integer32):
    """Custom type h3cIssuLastOpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("done", 2),
          ("test", 3),
          ("install", 4),
          ("rollback", 5))
    )


_H3cIssuLastOpType_Type.__name__ = "Integer32"
_H3cIssuLastOpType_Object = MibScalar
h3cIssuLastOpType = _H3cIssuLastOpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 7),
    _H3cIssuLastOpType_Type()
)
h3cIssuLastOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuLastOpType.setStatus("current")


class _H3cIssuLastOpStatus_Type(Integer32):
    """Custom type h3cIssuLastOpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("failure", 2),
          ("inProgress", 3),
          ("success", 4),
          ("rollbackInProgress", 5),
          ("rollbackSuccess", 6))
    )


_H3cIssuLastOpStatus_Type.__name__ = "Integer32"
_H3cIssuLastOpStatus_Object = MibScalar
h3cIssuLastOpStatus = _H3cIssuLastOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 8),
    _H3cIssuLastOpStatus_Type()
)
h3cIssuLastOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuLastOpStatus.setStatus("current")


class _H3cIssuLastOpFailedReason_Type(DisplayString):
    """Custom type h3cIssuLastOpFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIssuLastOpFailedReason_Type.__name__ = "DisplayString"
_H3cIssuLastOpFailedReason_Object = MibScalar
h3cIssuLastOpFailedReason = _H3cIssuLastOpFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 9),
    _H3cIssuLastOpFailedReason_Type()
)
h3cIssuLastOpFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuLastOpFailedReason.setStatus("current")


class _H3cIssuLastOpTimeCompleted_Type(DisplayString):
    """Custom type h3cIssuLastOpTimeCompleted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIssuLastOpTimeCompleted_Type.__name__ = "DisplayString"
_H3cIssuLastOpTimeCompleted_Object = MibScalar
h3cIssuLastOpTimeCompleted = _H3cIssuLastOpTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 1, 2, 10),
    _H3cIssuLastOpTimeCompleted_Type()
)
h3cIssuLastOpTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuLastOpTimeCompleted.setStatus("current")
_H3cIssuUpgradeResultGroup_ObjectIdentity = ObjectIdentity
h3cIssuUpgradeResultGroup = _H3cIssuUpgradeResultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2)
)
_H3cIssuCompatibleResult_ObjectIdentity = ObjectIdentity
h3cIssuCompatibleResult = _H3cIssuCompatibleResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 1)
)


class _H3cIssuCompatibleResultStatus_Type(Integer32):
    """Custom type h3cIssuCompatibleResultStatus based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("inCompatible", 2),
          ("compatible", 3),
          ("failure", 4))
    )


_H3cIssuCompatibleResultStatus_Type.__name__ = "Integer32"
_H3cIssuCompatibleResultStatus_Object = MibScalar
h3cIssuCompatibleResultStatus = _H3cIssuCompatibleResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 1, 1),
    _H3cIssuCompatibleResultStatus_Type()
)
h3cIssuCompatibleResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuCompatibleResultStatus.setStatus("current")


class _H3cIssuCompatibleResultFailedReason_Type(DisplayString):
    """Custom type h3cIssuCompatibleResultFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIssuCompatibleResultFailedReason_Type.__name__ = "DisplayString"
_H3cIssuCompatibleResultFailedReason_Object = MibScalar
h3cIssuCompatibleResultFailedReason = _H3cIssuCompatibleResultFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 1, 2),
    _H3cIssuCompatibleResultFailedReason_Type()
)
h3cIssuCompatibleResultFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuCompatibleResultFailedReason.setStatus("current")
_H3cIssuTestResultTable_Object = MibTable
h3cIssuTestResultTable = _H3cIssuTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIssuTestResultTable.setStatus("current")
_H3cIssuTestResultEntry_Object = MibTableRow
h3cIssuTestResultEntry = _H3cIssuTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2, 1)
)
h3cIssuTestResultEntry.setIndexNames(
    (0, "H3C-ISSU-MIB", "h3cIssuTestResultIndex"),
)
if mibBuilder.loadTexts:
    h3cIssuTestResultEntry.setStatus("current")


class _H3cIssuTestResultIndex_Type(Integer32):
    """Custom type h3cIssuTestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cIssuTestResultIndex_Type.__name__ = "Integer32"
_H3cIssuTestResultIndex_Object = MibTableColumn
h3cIssuTestResultIndex = _H3cIssuTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2, 1, 1),
    _H3cIssuTestResultIndex_Type()
)
h3cIssuTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIssuTestResultIndex.setStatus("current")


class _H3cIssuTestDeviceChassisID_Type(Integer32):
    """Custom type h3cIssuTestDeviceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIssuTestDeviceChassisID_Type.__name__ = "Integer32"
_H3cIssuTestDeviceChassisID_Object = MibTableColumn
h3cIssuTestDeviceChassisID = _H3cIssuTestDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2, 1, 2),
    _H3cIssuTestDeviceChassisID_Type()
)
h3cIssuTestDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuTestDeviceChassisID.setStatus("current")


class _H3cIssuTestDeviceSlotID_Type(Integer32):
    """Custom type h3cIssuTestDeviceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIssuTestDeviceSlotID_Type.__name__ = "Integer32"
_H3cIssuTestDeviceSlotID_Object = MibTableColumn
h3cIssuTestDeviceSlotID = _H3cIssuTestDeviceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2, 1, 3),
    _H3cIssuTestDeviceSlotID_Type()
)
h3cIssuTestDeviceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuTestDeviceSlotID.setStatus("current")


class _H3cIssuTestDeviceCpuID_Type(Integer32):
    """Custom type h3cIssuTestDeviceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cIssuTestDeviceCpuID_Type.__name__ = "Integer32"
_H3cIssuTestDeviceCpuID_Object = MibTableColumn
h3cIssuTestDeviceCpuID = _H3cIssuTestDeviceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2, 1, 4),
    _H3cIssuTestDeviceCpuID_Type()
)
h3cIssuTestDeviceCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuTestDeviceCpuID.setStatus("current")


class _H3cIssuTestDeviceUpgradeWay_Type(Integer32):
    """Custom type h3cIssuTestDeviceUpgradeWay based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("reboot", 2),
          ("sequenceReboot", 3),
          ("issuReboot", 4),
          ("serviceUpgrade", 5),
          ("fileUpgrade", 6),
          ("incompatibleUpgrade", 7))
    )


_H3cIssuTestDeviceUpgradeWay_Type.__name__ = "Integer32"
_H3cIssuTestDeviceUpgradeWay_Object = MibTableColumn
h3cIssuTestDeviceUpgradeWay = _H3cIssuTestDeviceUpgradeWay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 2, 1, 5),
    _H3cIssuTestDeviceUpgradeWay_Type()
)
h3cIssuTestDeviceUpgradeWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuTestDeviceUpgradeWay.setStatus("current")
_H3cIssuUpgradeResultTable_Object = MibTable
h3cIssuUpgradeResultTable = _H3cIssuUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cIssuUpgradeResultTable.setStatus("current")
_H3cIssuUpgradeResultEntry_Object = MibTableRow
h3cIssuUpgradeResultEntry = _H3cIssuUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1)
)
h3cIssuUpgradeResultEntry.setIndexNames(
    (0, "H3C-ISSU-MIB", "h3cIssuUpgradeResultIndex"),
)
if mibBuilder.loadTexts:
    h3cIssuUpgradeResultEntry.setStatus("current")


class _H3cIssuUpgradeResultIndex_Type(Integer32):
    """Custom type h3cIssuUpgradeResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cIssuUpgradeResultIndex_Type.__name__ = "Integer32"
_H3cIssuUpgradeResultIndex_Object = MibTableColumn
h3cIssuUpgradeResultIndex = _H3cIssuUpgradeResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 1),
    _H3cIssuUpgradeResultIndex_Type()
)
h3cIssuUpgradeResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIssuUpgradeResultIndex.setStatus("current")


class _H3cIssuUpgradeDeviceChassisID_Type(Integer32):
    """Custom type h3cIssuUpgradeDeviceChassisID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIssuUpgradeDeviceChassisID_Type.__name__ = "Integer32"
_H3cIssuUpgradeDeviceChassisID_Object = MibTableColumn
h3cIssuUpgradeDeviceChassisID = _H3cIssuUpgradeDeviceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 2),
    _H3cIssuUpgradeDeviceChassisID_Type()
)
h3cIssuUpgradeDeviceChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuUpgradeDeviceChassisID.setStatus("current")


class _H3cIssuUpgradeDeviceSlotID_Type(Integer32):
    """Custom type h3cIssuUpgradeDeviceSlotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cIssuUpgradeDeviceSlotID_Type.__name__ = "Integer32"
_H3cIssuUpgradeDeviceSlotID_Object = MibTableColumn
h3cIssuUpgradeDeviceSlotID = _H3cIssuUpgradeDeviceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 3),
    _H3cIssuUpgradeDeviceSlotID_Type()
)
h3cIssuUpgradeDeviceSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuUpgradeDeviceSlotID.setStatus("current")


class _H3cIssuUpgradeDeviceCpuID_Type(Integer32):
    """Custom type h3cIssuUpgradeDeviceCpuID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cIssuUpgradeDeviceCpuID_Type.__name__ = "Integer32"
_H3cIssuUpgradeDeviceCpuID_Object = MibTableColumn
h3cIssuUpgradeDeviceCpuID = _H3cIssuUpgradeDeviceCpuID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 4),
    _H3cIssuUpgradeDeviceCpuID_Type()
)
h3cIssuUpgradeDeviceCpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuUpgradeDeviceCpuID.setStatus("current")


class _H3cIssuUpgradeState_Type(Integer32):
    """Custom type h3cIssuUpgradeState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("loading", 2),
          ("loaded", 3),
          ("switching", 4),
          ("switchover", 5),
          ("committing", 6),
          ("committed", 7),
          ("rollbacking", 8),
          ("rollbacked", 9))
    )


_H3cIssuUpgradeState_Type.__name__ = "Integer32"
_H3cIssuUpgradeState_Object = MibTableColumn
h3cIssuUpgradeState = _H3cIssuUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 5),
    _H3cIssuUpgradeState_Type()
)
h3cIssuUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuUpgradeState.setStatus("current")


class _H3cIssuDeviceUpgradeWay_Type(Integer32):
    """Custom type h3cIssuDeviceUpgradeWay based on Integer32"""
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
        *(("none", 1),
          ("reboot", 2),
          ("sequenceReboot", 3),
          ("issuReboot", 4),
          ("serviceUpgrade", 5),
          ("fileUpgrade", 6),
          ("incompatibleUpgrade", 7))
    )


_H3cIssuDeviceUpgradeWay_Type.__name__ = "Integer32"
_H3cIssuDeviceUpgradeWay_Object = MibTableColumn
h3cIssuDeviceUpgradeWay = _H3cIssuDeviceUpgradeWay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 6),
    _H3cIssuDeviceUpgradeWay_Type()
)
h3cIssuDeviceUpgradeWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuDeviceUpgradeWay.setStatus("current")


class _H3cIssuUpgradeDeviceStatus_Type(Integer32):
    """Custom type h3cIssuUpgradeDeviceStatus based on Integer32"""
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
        *(("waitingUpgrade", 1),
          ("inProcess", 2),
          ("success", 3),
          ("failure", 4))
    )


_H3cIssuUpgradeDeviceStatus_Type.__name__ = "Integer32"
_H3cIssuUpgradeDeviceStatus_Object = MibTableColumn
h3cIssuUpgradeDeviceStatus = _H3cIssuUpgradeDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 7),
    _H3cIssuUpgradeDeviceStatus_Type()
)
h3cIssuUpgradeDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuUpgradeDeviceStatus.setStatus("current")


class _H3cIssuUpgradeFailedReason_Type(DisplayString):
    """Custom type h3cIssuUpgradeFailedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cIssuUpgradeFailedReason_Type.__name__ = "DisplayString"
_H3cIssuUpgradeFailedReason_Object = MibTableColumn
h3cIssuUpgradeFailedReason = _H3cIssuUpgradeFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 1, 2, 3, 1, 8),
    _H3cIssuUpgradeFailedReason_Type()
)
h3cIssuUpgradeFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIssuUpgradeFailedReason.setStatus("current")
_H3cIssuUpgradeNotify_ObjectIdentity = ObjectIdentity
h3cIssuUpgradeNotify = _H3cIssuUpgradeNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 2)
)
_H3cIssuUpgradeTrapPrefix_ObjectIdentity = ObjectIdentity
h3cIssuUpgradeTrapPrefix = _H3cIssuUpgradeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cIssuUpgradeOpCompletionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 133, 2, 0, 1)
)
h3cIssuUpgradeOpCompletionNotify.setObjects(
      *(("H3C-ISSU-MIB", "h3cIssuOpType"),
        ("H3C-ISSU-MIB", "h3cIssuOpStatus"),
        ("H3C-ISSU-MIB", "h3cIssuFailedReason"),
        ("H3C-ISSU-MIB", "h3cIssuOpTimeCompleted"))
)
if mibBuilder.loadTexts:
    h3cIssuUpgradeOpCompletionNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-ISSU-MIB",
    **{"h3cIssuUpgrade": h3cIssuUpgrade,
       "h3cIssuUpgradeMibObjects": h3cIssuUpgradeMibObjects,
       "h3cIssuUpgradeGroup": h3cIssuUpgradeGroup,
       "h3cIssuUpgradeImageTable": h3cIssuUpgradeImageTable,
       "h3cIssuUpgradeImageEntry": h3cIssuUpgradeImageEntry,
       "h3cIssuUpgradeImageIndex": h3cIssuUpgradeImageIndex,
       "h3cIssuUpgradeImageType": h3cIssuUpgradeImageType,
       "h3cIssuUpgradeImageURL": h3cIssuUpgradeImageURL,
       "h3cIssuUpgradeImageRowStatus": h3cIssuUpgradeImageRowStatus,
       "h3cIssuOp": h3cIssuOp,
       "h3cIssuOpType": h3cIssuOpType,
       "h3cIssuImageFileOverwrite": h3cIssuImageFileOverwrite,
       "h3cIssuOpTrapEnable": h3cIssuOpTrapEnable,
       "h3cIssuOpStatus": h3cIssuOpStatus,
       "h3cIssuFailedReason": h3cIssuFailedReason,
       "h3cIssuOpTimeCompleted": h3cIssuOpTimeCompleted,
       "h3cIssuLastOpType": h3cIssuLastOpType,
       "h3cIssuLastOpStatus": h3cIssuLastOpStatus,
       "h3cIssuLastOpFailedReason": h3cIssuLastOpFailedReason,
       "h3cIssuLastOpTimeCompleted": h3cIssuLastOpTimeCompleted,
       "h3cIssuUpgradeResultGroup": h3cIssuUpgradeResultGroup,
       "h3cIssuCompatibleResult": h3cIssuCompatibleResult,
       "h3cIssuCompatibleResultStatus": h3cIssuCompatibleResultStatus,
       "h3cIssuCompatibleResultFailedReason": h3cIssuCompatibleResultFailedReason,
       "h3cIssuTestResultTable": h3cIssuTestResultTable,
       "h3cIssuTestResultEntry": h3cIssuTestResultEntry,
       "h3cIssuTestResultIndex": h3cIssuTestResultIndex,
       "h3cIssuTestDeviceChassisID": h3cIssuTestDeviceChassisID,
       "h3cIssuTestDeviceSlotID": h3cIssuTestDeviceSlotID,
       "h3cIssuTestDeviceCpuID": h3cIssuTestDeviceCpuID,
       "h3cIssuTestDeviceUpgradeWay": h3cIssuTestDeviceUpgradeWay,
       "h3cIssuUpgradeResultTable": h3cIssuUpgradeResultTable,
       "h3cIssuUpgradeResultEntry": h3cIssuUpgradeResultEntry,
       "h3cIssuUpgradeResultIndex": h3cIssuUpgradeResultIndex,
       "h3cIssuUpgradeDeviceChassisID": h3cIssuUpgradeDeviceChassisID,
       "h3cIssuUpgradeDeviceSlotID": h3cIssuUpgradeDeviceSlotID,
       "h3cIssuUpgradeDeviceCpuID": h3cIssuUpgradeDeviceCpuID,
       "h3cIssuUpgradeState": h3cIssuUpgradeState,
       "h3cIssuDeviceUpgradeWay": h3cIssuDeviceUpgradeWay,
       "h3cIssuUpgradeDeviceStatus": h3cIssuUpgradeDeviceStatus,
       "h3cIssuUpgradeFailedReason": h3cIssuUpgradeFailedReason,
       "h3cIssuUpgradeNotify": h3cIssuUpgradeNotify,
       "h3cIssuUpgradeTrapPrefix": h3cIssuUpgradeTrapPrefix,
       "h3cIssuUpgradeOpCompletionNotify": h3cIssuUpgradeOpCompletionNotify}
)
