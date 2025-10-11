# SNMP MIB module (FS-SECZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SECZONE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:16 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsSecZoneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54)
)
if mibBuilder.loadTexts:
    fsSecZoneMIB.setRevisions(
        ("2009-08-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSecZoneMIBObjects_ObjectIdentity = ObjectIdentity
fsSecZoneMIBObjects = _FsSecZoneMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1)
)
_FsSecZoneChainTable_Object = MibTable
fsSecZoneChainTable = _FsSecZoneChainTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    fsSecZoneChainTable.setStatus("current")
_FsSecZoneChainEntry_Object = MibTableRow
fsSecZoneChainEntry = _FsSecZoneChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1)
)
fsSecZoneChainEntry.setIndexNames(
    (0, "FS-SECZONE-MIB", "fsSecZoneChainName"),
)
if mibBuilder.loadTexts:
    fsSecZoneChainEntry.setStatus("current")


class _FsSecZoneChainName_Type(DisplayString):
    """Custom type fsSecZoneChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSecZoneChainName_Type.__name__ = "DisplayString"
_FsSecZoneChainName_Object = MibTableColumn
fsSecZoneChainName = _FsSecZoneChainName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 1),
    _FsSecZoneChainName_Type()
)
fsSecZoneChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecZoneChainName.setStatus("current")


class _FsSecZoneLevel_Type(Integer32):
    """Custom type fsSecZoneLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsSecZoneLevel_Type.__name__ = "Integer32"
_FsSecZoneLevel_Object = MibTableColumn
fsSecZoneLevel = _FsSecZoneLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 2),
    _FsSecZoneLevel_Type()
)
fsSecZoneLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneLevel.setStatus("current")


class _FsSecZoneAclName_Type(DisplayString):
    """Custom type fsSecZoneAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSecZoneAclName_Type.__name__ = "DisplayString"
_FsSecZoneAclName_Object = MibTableColumn
fsSecZoneAclName = _FsSecZoneAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 3),
    _FsSecZoneAclName_Type()
)
fsSecZoneAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneAclName.setStatus("current")


class _FsSecZoneViolationNotifyThresh_Type(Integer32):
    """Custom type fsSecZoneViolationNotifyThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSecZoneViolationNotifyThresh_Type.__name__ = "Integer32"
_FsSecZoneViolationNotifyThresh_Object = MibTableColumn
fsSecZoneViolationNotifyThresh = _FsSecZoneViolationNotifyThresh_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 4),
    _FsSecZoneViolationNotifyThresh_Type()
)
fsSecZoneViolationNotifyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneViolationNotifyThresh.setStatus("current")


class _FsSecZoneViolationNotifyAction_Type(Integer32):
    """Custom type fsSecZoneViolationNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_FsSecZoneViolationNotifyAction_Type.__name__ = "Integer32"
_FsSecZoneViolationNotifyAction_Object = MibTableColumn
fsSecZoneViolationNotifyAction = _FsSecZoneViolationNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 5),
    _FsSecZoneViolationNotifyAction_Type()
)
fsSecZoneViolationNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneViolationNotifyAction.setStatus("current")


class _FsSecZoneViolationBlockThresh_Type(Integer32):
    """Custom type fsSecZoneViolationBlockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSecZoneViolationBlockThresh_Type.__name__ = "Integer32"
_FsSecZoneViolationBlockThresh_Object = MibTableColumn
fsSecZoneViolationBlockThresh = _FsSecZoneViolationBlockThresh_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 6),
    _FsSecZoneViolationBlockThresh_Type()
)
fsSecZoneViolationBlockThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneViolationBlockThresh.setStatus("current")


class _FsSecZoneViolationBlockAction_Type(Integer32):
    """Custom type fsSecZoneViolationBlockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_FsSecZoneViolationBlockAction_Type.__name__ = "Integer32"
_FsSecZoneViolationBlockAction_Object = MibTableColumn
fsSecZoneViolationBlockAction = _FsSecZoneViolationBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 7),
    _FsSecZoneViolationBlockAction_Type()
)
fsSecZoneViolationBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneViolationBlockAction.setStatus("current")


class _FsSecZoneViolationBlockTimeout_Type(Integer32):
    """Custom type fsSecZoneViolationBlockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FsSecZoneViolationBlockTimeout_Type.__name__ = "Integer32"
_FsSecZoneViolationBlockTimeout_Object = MibTableColumn
fsSecZoneViolationBlockTimeout = _FsSecZoneViolationBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 8),
    _FsSecZoneViolationBlockTimeout_Type()
)
fsSecZoneViolationBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneViolationBlockTimeout.setStatus("current")
_FsSecZoneChainEntryStatus_Type = RowStatus
_FsSecZoneChainEntryStatus_Object = MibTableColumn
fsSecZoneChainEntryStatus = _FsSecZoneChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 1, 1, 9),
    _FsSecZoneChainEntryStatus_Type()
)
fsSecZoneChainEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSecZoneChainEntryStatus.setStatus("current")
_FsSecZone2ZoneTable_Object = MibTable
fsSecZone2ZoneTable = _FsSecZone2ZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 2)
)
if mibBuilder.loadTexts:
    fsSecZone2ZoneTable.setStatus("current")
_FsSecZone2ZoneEntry_Object = MibTableRow
fsSecZone2ZoneEntry = _FsSecZone2ZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 2, 1)
)
fsSecZone2ZoneEntry.setIndexNames(
    (0, "FS-SECZONE-MIB", "fsZoneFirstName"),
    (0, "FS-SECZONE-MIB", "fsZoneSecondName"),
    (0, "FS-SECZONE-MIB", "fsZone2ZoneAclName"),
)
if mibBuilder.loadTexts:
    fsSecZone2ZoneEntry.setStatus("current")


class _FsZoneFirstName_Type(DisplayString):
    """Custom type fsZoneFirstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsZoneFirstName_Type.__name__ = "DisplayString"
_FsZoneFirstName_Object = MibTableColumn
fsZoneFirstName = _FsZoneFirstName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 2, 1, 1),
    _FsZoneFirstName_Type()
)
fsZoneFirstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZoneFirstName.setStatus("current")


class _FsZoneSecondName_Type(DisplayString):
    """Custom type fsZoneSecondName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsZoneSecondName_Type.__name__ = "DisplayString"
_FsZoneSecondName_Object = MibTableColumn
fsZoneSecondName = _FsZoneSecondName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 2, 1, 2),
    _FsZoneSecondName_Type()
)
fsZoneSecondName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZoneSecondName.setStatus("current")


class _FsZone2ZoneAclName_Type(DisplayString):
    """Custom type fsZone2ZoneAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsZone2ZoneAclName_Type.__name__ = "DisplayString"
_FsZone2ZoneAclName_Object = MibTableColumn
fsZone2ZoneAclName = _FsZone2ZoneAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 2, 1, 3),
    _FsZone2ZoneAclName_Type()
)
fsZone2ZoneAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZone2ZoneAclName.setStatus("current")
_FsZone2ZoneEntryStauts_Type = RowStatus
_FsZone2ZoneEntryStauts_Object = MibTableColumn
fsZone2ZoneEntryStauts = _FsZone2ZoneEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 2, 1, 4),
    _FsZone2ZoneEntryStauts_Type()
)
fsZone2ZoneEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsZone2ZoneEntryStauts.setStatus("current")
_FsSecZoneBlockingTable_Object = MibTable
fsSecZoneBlockingTable = _FsSecZoneBlockingTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 3)
)
if mibBuilder.loadTexts:
    fsSecZoneBlockingTable.setStatus("current")
_FsSecZoneBlockingEntry_Object = MibTableRow
fsSecZoneBlockingEntry = _FsSecZoneBlockingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 3, 1)
)
fsSecZoneBlockingEntry.setIndexNames(
    (0, "FS-SECZONE-MIB", "fsBockingIP"),
)
if mibBuilder.loadTexts:
    fsSecZoneBlockingEntry.setStatus("current")
_FsBockingIP_Type = IpAddress
_FsBockingIP_Object = MibTableColumn
fsBockingIP = _FsBockingIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 3, 1, 1),
    _FsBockingIP_Type()
)
fsBockingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingIP.setStatus("current")


class _FsBockingCurrentStatus_Type(Integer32):
    """Custom type fsBockingCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_FsBockingCurrentStatus_Type.__name__ = "Integer32"
_FsBockingCurrentStatus_Object = MibTableColumn
fsBockingCurrentStatus = _FsBockingCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 3, 1, 2),
    _FsBockingCurrentStatus_Type()
)
fsBockingCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingCurrentStatus.setStatus("current")


class _FsBockingTryAccessZoneName_Type(DisplayString):
    """Custom type fsBockingTryAccessZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsBockingTryAccessZoneName_Type.__name__ = "DisplayString"
_FsBockingTryAccessZoneName_Object = MibTableColumn
fsBockingTryAccessZoneName = _FsBockingTryAccessZoneName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 3, 1, 3),
    _FsBockingTryAccessZoneName_Type()
)
fsBockingTryAccessZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingTryAccessZoneName.setStatus("current")
_FsBockingEntryStatus_Type = ConfigStatus
_FsBockingEntryStatus_Object = MibTableColumn
fsBockingEntryStatus = _FsBockingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 3, 1, 4),
    _FsBockingEntryStatus_Type()
)
fsBockingEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBockingEntryStatus.setStatus("current")


class _FsGlobalViolationNotifyThresh_Type(Integer32):
    """Custom type fsGlobalViolationNotifyThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsGlobalViolationNotifyThresh_Type.__name__ = "Integer32"
_FsGlobalViolationNotifyThresh_Object = MibScalar
fsGlobalViolationNotifyThresh = _FsGlobalViolationNotifyThresh_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 4),
    _FsGlobalViolationNotifyThresh_Type()
)
fsGlobalViolationNotifyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalViolationNotifyThresh.setStatus("current")


class _FsGlobalViolationNotifyAction_Type(Integer32):
    """Custom type fsGlobalViolationNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_FsGlobalViolationNotifyAction_Type.__name__ = "Integer32"
_FsGlobalViolationNotifyAction_Object = MibScalar
fsGlobalViolationNotifyAction = _FsGlobalViolationNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 5),
    _FsGlobalViolationNotifyAction_Type()
)
fsGlobalViolationNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalViolationNotifyAction.setStatus("current")


class _FsGlobalViolationBlockThresh_Type(Integer32):
    """Custom type fsGlobalViolationBlockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsGlobalViolationBlockThresh_Type.__name__ = "Integer32"
_FsGlobalViolationBlockThresh_Object = MibScalar
fsGlobalViolationBlockThresh = _FsGlobalViolationBlockThresh_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 6),
    _FsGlobalViolationBlockThresh_Type()
)
fsGlobalViolationBlockThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalViolationBlockThresh.setStatus("current")


class _FsGlobalViolationBlockAction_Type(Integer32):
    """Custom type fsGlobalViolationBlockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_FsGlobalViolationBlockAction_Type.__name__ = "Integer32"
_FsGlobalViolationBlockAction_Object = MibScalar
fsGlobalViolationBlockAction = _FsGlobalViolationBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 7),
    _FsGlobalViolationBlockAction_Type()
)
fsGlobalViolationBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalViolationBlockAction.setStatus("current")


class _FsGlobalViolationBlockTimeout_Type(Integer32):
    """Custom type fsGlobalViolationBlockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FsGlobalViolationBlockTimeout_Type.__name__ = "Integer32"
_FsGlobalViolationBlockTimeout_Object = MibScalar
fsGlobalViolationBlockTimeout = _FsGlobalViolationBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 8),
    _FsGlobalViolationBlockTimeout_Type()
)
fsGlobalViolationBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalViolationBlockTimeout.setStatus("current")
_ViolationTime_Type = DisplayString
_ViolationTime_Object = MibScalar
violationTime = _ViolationTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 9),
    _ViolationTime_Type()
)
violationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationTime.setStatus("current")
_ViolationSrcIP_Type = IpAddress
_ViolationSrcIP_Object = MibScalar
violationSrcIP = _ViolationSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 10),
    _ViolationSrcIP_Type()
)
violationSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationSrcIP.setStatus("current")
_ViolationDestIP_Type = IpAddress
_ViolationDestIP_Object = MibScalar
violationDestIP = _ViolationDestIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 11),
    _ViolationDestIP_Type()
)
violationDestIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationDestIP.setStatus("current")
_ViolationProtocol_Type = Integer32
_ViolationProtocol_Object = MibScalar
violationProtocol = _ViolationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 12),
    _ViolationProtocol_Type()
)
violationProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationProtocol.setStatus("current")
_ViolationL4Key_Type = Integer32
_ViolationL4Key_Object = MibScalar
violationL4Key = _ViolationL4Key_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 1, 13),
    _ViolationL4Key_Type()
)
violationL4Key.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationL4Key.setStatus("current")
_FsSecZoneMIBTraps_ObjectIdentity = ObjectIdentity
fsSecZoneMIBTraps = _FsSecZoneMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 2)
)
_FsSecZoneMIBConformance_ObjectIdentity = ObjectIdentity
fsSecZoneMIBConformance = _FsSecZoneMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3)
)
_FsSecZoneMIBCompliances_ObjectIdentity = ObjectIdentity
fsSecZoneMIBCompliances = _FsSecZoneMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3, 1)
)
_FsSecZoneMIBGroups_ObjectIdentity = ObjectIdentity
fsSecZoneMIBGroups = _FsSecZoneMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3, 2)
)

# Managed Objects groups

fsSecZoneMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3, 2, 1)
)
fsSecZoneMIBGroup.setObjects(
      *(("FS-SECZONE-MIB", "fsSecZoneChainName"),
        ("FS-SECZONE-MIB", "fsSecZoneLevel"),
        ("FS-SECZONE-MIB", "fsSecZoneAclName"),
        ("FS-SECZONE-MIB", "fsSecZoneViolationNotifyThresh"),
        ("FS-SECZONE-MIB", "fsSecZoneViolationNotifyAction"),
        ("FS-SECZONE-MIB", "fsSecZoneViolationBlockThresh"),
        ("FS-SECZONE-MIB", "fsSecZoneViolationBlockAction"),
        ("FS-SECZONE-MIB", "fsSecZoneViolationBlockTimeout"),
        ("FS-SECZONE-MIB", "fsSecZoneChainEntryStatus"),
        ("FS-SECZONE-MIB", "fsZoneFirstName"),
        ("FS-SECZONE-MIB", "fsZoneSecondName"),
        ("FS-SECZONE-MIB", "fsZone2ZoneAclName"),
        ("FS-SECZONE-MIB", "fsZone2ZoneEntryStauts"),
        ("FS-SECZONE-MIB", "fsBockingIP"),
        ("FS-SECZONE-MIB", "fsBockingCurrentStatus"),
        ("FS-SECZONE-MIB", "fsBockingTryAccessZoneName"),
        ("FS-SECZONE-MIB", "fsBockingEntryStatus"),
        ("FS-SECZONE-MIB", "fsGlobalViolationNotifyThresh"),
        ("FS-SECZONE-MIB", "fsGlobalViolationNotifyAction"),
        ("FS-SECZONE-MIB", "fsGlobalViolationBlockThresh"),
        ("FS-SECZONE-MIB", "fsGlobalViolationBlockAction"),
        ("FS-SECZONE-MIB", "fsGlobalViolationBlockTimeout"))
)
if mibBuilder.loadTexts:
    fsSecZoneMIBGroup.setStatus("current")

fsSecZoneNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3, 2, 2)
)
fsSecZoneNotifObjectsGroup.setObjects(
      *(("FS-SECZONE-MIB", "violationTime"),
        ("FS-SECZONE-MIB", "violationSrcIP"),
        ("FS-SECZONE-MIB", "violationDestIP"),
        ("FS-SECZONE-MIB", "violationProtocol"),
        ("FS-SECZONE-MIB", "violationL4Key"))
)
if mibBuilder.loadTexts:
    fsSecZoneNotifObjectsGroup.setStatus("current")


# Notification objects

fsSecZoneViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 2, 1)
)
fsSecZoneViolationTrap.setObjects(
      *(("FS-SECZONE-MIB", "violationTime"),
        ("FS-SECZONE-MIB", "violationSrcIP"),
        ("FS-SECZONE-MIB", "violationDestIP"),
        ("FS-SECZONE-MIB", "violationProtocol"),
        ("FS-SECZONE-MIB", "violationL4Key"),
        ("FS-SECZONE-MIB", "fsZoneFirstName"),
        ("FS-SECZONE-MIB", "fsZoneSecondName"))
)
if mibBuilder.loadTexts:
    fsSecZoneViolationTrap.setStatus(
        "current"
    )


# Notifications groups

fsSecZoneNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3, 2, 3)
)
fsSecZoneNotificationsGroup.setObjects(
    ("FS-SECZONE-MIB", "fsSecZoneViolationTrap")
)
if mibBuilder.loadTexts:
    fsSecZoneNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsSecZoneMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 54, 3, 1, 1)
)
fsSecZoneMIBCompliance.setObjects(
      *(("FS-SECZONE-MIB", "fsSecZoneMIBGroup"),
        ("FS-SECZONE-MIB", "fsSecZoneNotifObjectsGroup"),
        ("FS-SECZONE-MIB", "fsSecZoneNotificationsGroup"))
)
if mibBuilder.loadTexts:
    fsSecZoneMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SECZONE-MIB",
    **{"fsSecZoneMIB": fsSecZoneMIB,
       "fsSecZoneMIBObjects": fsSecZoneMIBObjects,
       "fsSecZoneChainTable": fsSecZoneChainTable,
       "fsSecZoneChainEntry": fsSecZoneChainEntry,
       "fsSecZoneChainName": fsSecZoneChainName,
       "fsSecZoneLevel": fsSecZoneLevel,
       "fsSecZoneAclName": fsSecZoneAclName,
       "fsSecZoneViolationNotifyThresh": fsSecZoneViolationNotifyThresh,
       "fsSecZoneViolationNotifyAction": fsSecZoneViolationNotifyAction,
       "fsSecZoneViolationBlockThresh": fsSecZoneViolationBlockThresh,
       "fsSecZoneViolationBlockAction": fsSecZoneViolationBlockAction,
       "fsSecZoneViolationBlockTimeout": fsSecZoneViolationBlockTimeout,
       "fsSecZoneChainEntryStatus": fsSecZoneChainEntryStatus,
       "fsSecZone2ZoneTable": fsSecZone2ZoneTable,
       "fsSecZone2ZoneEntry": fsSecZone2ZoneEntry,
       "fsZoneFirstName": fsZoneFirstName,
       "fsZoneSecondName": fsZoneSecondName,
       "fsZone2ZoneAclName": fsZone2ZoneAclName,
       "fsZone2ZoneEntryStauts": fsZone2ZoneEntryStauts,
       "fsSecZoneBlockingTable": fsSecZoneBlockingTable,
       "fsSecZoneBlockingEntry": fsSecZoneBlockingEntry,
       "fsBockingIP": fsBockingIP,
       "fsBockingCurrentStatus": fsBockingCurrentStatus,
       "fsBockingTryAccessZoneName": fsBockingTryAccessZoneName,
       "fsBockingEntryStatus": fsBockingEntryStatus,
       "fsGlobalViolationNotifyThresh": fsGlobalViolationNotifyThresh,
       "fsGlobalViolationNotifyAction": fsGlobalViolationNotifyAction,
       "fsGlobalViolationBlockThresh": fsGlobalViolationBlockThresh,
       "fsGlobalViolationBlockAction": fsGlobalViolationBlockAction,
       "fsGlobalViolationBlockTimeout": fsGlobalViolationBlockTimeout,
       "violationTime": violationTime,
       "violationSrcIP": violationSrcIP,
       "violationDestIP": violationDestIP,
       "violationProtocol": violationProtocol,
       "violationL4Key": violationL4Key,
       "fsSecZoneMIBTraps": fsSecZoneMIBTraps,
       "fsSecZoneViolationTrap": fsSecZoneViolationTrap,
       "fsSecZoneMIBConformance": fsSecZoneMIBConformance,
       "fsSecZoneMIBCompliances": fsSecZoneMIBCompliances,
       "fsSecZoneMIBCompliance": fsSecZoneMIBCompliance,
       "fsSecZoneMIBGroups": fsSecZoneMIBGroups,
       "fsSecZoneMIBGroup": fsSecZoneMIBGroup,
       "fsSecZoneNotifObjectsGroup": fsSecZoneNotifObjectsGroup,
       "fsSecZoneNotificationsGroup": fsSecZoneNotificationsGroup}
)
