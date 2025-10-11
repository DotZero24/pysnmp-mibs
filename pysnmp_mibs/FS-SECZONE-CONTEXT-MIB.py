# SNMP MIB module (FS-SECZONE-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SECZONE-CONTEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:46 2025
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

fsSecZoneVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68)
)
if mibBuilder.loadTexts:
    fsSecZoneVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSecZoneVCMIBObjects_ObjectIdentity = ObjectIdentity
fsSecZoneVCMIBObjects = _FsSecZoneVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1)
)
_FsSecZoneChainVCTable_Object = MibTable
fsSecZoneChainVCTable = _FsSecZoneChainVCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1)
)
if mibBuilder.loadTexts:
    fsSecZoneChainVCTable.setStatus("current")
_FsSecZoneChainVCEntry_Object = MibTableRow
fsSecZoneChainVCEntry = _FsSecZoneChainVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1)
)
fsSecZoneChainVCEntry.setIndexNames(
    (0, "FS-SECZONE-CONTEXT-MIB", "fsSecZoneContextNameVC"),
    (0, "FS-SECZONE-CONTEXT-MIB", "fsSecZoneChainNameVC"),
)
if mibBuilder.loadTexts:
    fsSecZoneChainVCEntry.setStatus("current")


class _FsSecZoneContextNameVC_Type(DisplayString):
    """Custom type fsSecZoneContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsSecZoneContextNameVC_Type.__name__ = "DisplayString"
_FsSecZoneContextNameVC_Object = MibTableColumn
fsSecZoneContextNameVC = _FsSecZoneContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 1),
    _FsSecZoneContextNameVC_Type()
)
fsSecZoneContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecZoneContextNameVC.setStatus("current")


class _FsSecZoneChainNameVC_Type(DisplayString):
    """Custom type fsSecZoneChainNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSecZoneChainNameVC_Type.__name__ = "DisplayString"
_FsSecZoneChainNameVC_Object = MibTableColumn
fsSecZoneChainNameVC = _FsSecZoneChainNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 2),
    _FsSecZoneChainNameVC_Type()
)
fsSecZoneChainNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecZoneChainNameVC.setStatus("current")


class _FsSecZoneLevelVC_Type(Integer32):
    """Custom type fsSecZoneLevelVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsSecZoneLevelVC_Type.__name__ = "Integer32"
_FsSecZoneLevelVC_Object = MibTableColumn
fsSecZoneLevelVC = _FsSecZoneLevelVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 3),
    _FsSecZoneLevelVC_Type()
)
fsSecZoneLevelVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneLevelVC.setStatus("current")


class _FsSecZoneAclNameVC_Type(DisplayString):
    """Custom type fsSecZoneAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsSecZoneAclNameVC_Type.__name__ = "DisplayString"
_FsSecZoneAclNameVC_Object = MibTableColumn
fsSecZoneAclNameVC = _FsSecZoneAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 4),
    _FsSecZoneAclNameVC_Type()
)
fsSecZoneAclNameVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneAclNameVC.setStatus("current")


class _FsSecZoneViolationNotifyThreshVC_Type(Integer32):
    """Custom type fsSecZoneViolationNotifyThreshVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSecZoneViolationNotifyThreshVC_Type.__name__ = "Integer32"
_FsSecZoneViolationNotifyThreshVC_Object = MibTableColumn
fsSecZoneViolationNotifyThreshVC = _FsSecZoneViolationNotifyThreshVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 5),
    _FsSecZoneViolationNotifyThreshVC_Type()
)
fsSecZoneViolationNotifyThreshVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneViolationNotifyThreshVC.setStatus("current")


class _FsSecZoneViolationNotifyActionVC_Type(Integer32):
    """Custom type fsSecZoneViolationNotifyActionVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nologtrap", 0),
          ("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_FsSecZoneViolationNotifyActionVC_Type.__name__ = "Integer32"
_FsSecZoneViolationNotifyActionVC_Object = MibTableColumn
fsSecZoneViolationNotifyActionVC = _FsSecZoneViolationNotifyActionVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 6),
    _FsSecZoneViolationNotifyActionVC_Type()
)
fsSecZoneViolationNotifyActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneViolationNotifyActionVC.setStatus("current")


class _FsSecZoneViolationBlockThreshVC_Type(Integer32):
    """Custom type fsSecZoneViolationBlockThreshVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSecZoneViolationBlockThreshVC_Type.__name__ = "Integer32"
_FsSecZoneViolationBlockThreshVC_Object = MibTableColumn
fsSecZoneViolationBlockThreshVC = _FsSecZoneViolationBlockThreshVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 7),
    _FsSecZoneViolationBlockThreshVC_Type()
)
fsSecZoneViolationBlockThreshVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneViolationBlockThreshVC.setStatus("current")


class _FsSecZoneViolationBlockActionVC_Type(Integer32):
    """Custom type fsSecZoneViolationBlockActionVC based on Integer32"""
    defaultValue = 1

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


_FsSecZoneViolationBlockActionVC_Type.__name__ = "Integer32"
_FsSecZoneViolationBlockActionVC_Object = MibTableColumn
fsSecZoneViolationBlockActionVC = _FsSecZoneViolationBlockActionVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 8),
    _FsSecZoneViolationBlockActionVC_Type()
)
fsSecZoneViolationBlockActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneViolationBlockActionVC.setStatus("current")


class _FsSecZoneViolationBlockTimeoutVC_Type(Integer32):
    """Custom type fsSecZoneViolationBlockTimeoutVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FsSecZoneViolationBlockTimeoutVC_Type.__name__ = "Integer32"
_FsSecZoneViolationBlockTimeoutVC_Object = MibTableColumn
fsSecZoneViolationBlockTimeoutVC = _FsSecZoneViolationBlockTimeoutVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 9),
    _FsSecZoneViolationBlockTimeoutVC_Type()
)
fsSecZoneViolationBlockTimeoutVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneViolationBlockTimeoutVC.setStatus("current")
_FsSecZoneChainEntryStatusVC_Type = RowStatus
_FsSecZoneChainEntryStatusVC_Object = MibTableColumn
fsSecZoneChainEntryStatusVC = _FsSecZoneChainEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 1, 1, 10),
    _FsSecZoneChainEntryStatusVC_Type()
)
fsSecZoneChainEntryStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecZoneChainEntryStatusVC.setStatus("current")
_FsSecZone2ZoneVCTable_Object = MibTable
fsSecZone2ZoneVCTable = _FsSecZone2ZoneVCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2)
)
if mibBuilder.loadTexts:
    fsSecZone2ZoneVCTable.setStatus("current")
_FsSecZone2ZoneVCEntry_Object = MibTableRow
fsSecZone2ZoneVCEntry = _FsSecZone2ZoneVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2, 1)
)
fsSecZone2ZoneVCEntry.setIndexNames(
    (0, "FS-SECZONE-CONTEXT-MIB", "fsZone2ZoneContextNameVC"),
    (0, "FS-SECZONE-CONTEXT-MIB", "fsZoneFirstNameVC"),
    (0, "FS-SECZONE-CONTEXT-MIB", "fsZoneSecondNameVC"),
    (0, "FS-SECZONE-CONTEXT-MIB", "fsZone2ZoneAclNameVC"),
)
if mibBuilder.loadTexts:
    fsSecZone2ZoneVCEntry.setStatus("current")


class _FsZone2ZoneContextNameVC_Type(DisplayString):
    """Custom type fsZone2ZoneContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsZone2ZoneContextNameVC_Type.__name__ = "DisplayString"
_FsZone2ZoneContextNameVC_Object = MibTableColumn
fsZone2ZoneContextNameVC = _FsZone2ZoneContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2, 1, 1),
    _FsZone2ZoneContextNameVC_Type()
)
fsZone2ZoneContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZone2ZoneContextNameVC.setStatus("current")


class _FsZoneFirstNameVC_Type(DisplayString):
    """Custom type fsZoneFirstNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsZoneFirstNameVC_Type.__name__ = "DisplayString"
_FsZoneFirstNameVC_Object = MibTableColumn
fsZoneFirstNameVC = _FsZoneFirstNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2, 1, 2),
    _FsZoneFirstNameVC_Type()
)
fsZoneFirstNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZoneFirstNameVC.setStatus("current")


class _FsZoneSecondNameVC_Type(DisplayString):
    """Custom type fsZoneSecondNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsZoneSecondNameVC_Type.__name__ = "DisplayString"
_FsZoneSecondNameVC_Object = MibTableColumn
fsZoneSecondNameVC = _FsZoneSecondNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2, 1, 3),
    _FsZoneSecondNameVC_Type()
)
fsZoneSecondNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZoneSecondNameVC.setStatus("current")


class _FsZone2ZoneAclNameVC_Type(DisplayString):
    """Custom type fsZone2ZoneAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsZone2ZoneAclNameVC_Type.__name__ = "DisplayString"
_FsZone2ZoneAclNameVC_Object = MibTableColumn
fsZone2ZoneAclNameVC = _FsZone2ZoneAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2, 1, 4),
    _FsZone2ZoneAclNameVC_Type()
)
fsZone2ZoneAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsZone2ZoneAclNameVC.setStatus("current")
_FsZone2ZoneEntryStautsVC_Type = RowStatus
_FsZone2ZoneEntryStautsVC_Object = MibTableColumn
fsZone2ZoneEntryStautsVC = _FsZone2ZoneEntryStautsVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 2, 1, 5),
    _FsZone2ZoneEntryStautsVC_Type()
)
fsZone2ZoneEntryStautsVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsZone2ZoneEntryStautsVC.setStatus("current")
_FsSecZoneBlockingVCTable_Object = MibTable
fsSecZoneBlockingVCTable = _FsSecZoneBlockingVCTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3)
)
if mibBuilder.loadTexts:
    fsSecZoneBlockingVCTable.setStatus("current")
_FsSecZoneBlockingVCEntry_Object = MibTableRow
fsSecZoneBlockingVCEntry = _FsSecZoneBlockingVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3, 1)
)
fsSecZoneBlockingVCEntry.setIndexNames(
    (0, "FS-SECZONE-CONTEXT-MIB", "fsBockingContextNameVC"),
    (0, "FS-SECZONE-CONTEXT-MIB", "fsBockingIPVC"),
)
if mibBuilder.loadTexts:
    fsSecZoneBlockingVCEntry.setStatus("current")


class _FsBockingContextNameVC_Type(DisplayString):
    """Custom type fsBockingContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_FsBockingContextNameVC_Type.__name__ = "DisplayString"
_FsBockingContextNameVC_Object = MibTableColumn
fsBockingContextNameVC = _FsBockingContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3, 1, 1),
    _FsBockingContextNameVC_Type()
)
fsBockingContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingContextNameVC.setStatus("current")
_FsBockingIPVC_Type = IpAddress
_FsBockingIPVC_Object = MibTableColumn
fsBockingIPVC = _FsBockingIPVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3, 1, 2),
    _FsBockingIPVC_Type()
)
fsBockingIPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingIPVC.setStatus("current")


class _FsBockingCurrentStatusVC_Type(Integer32):
    """Custom type fsBockingCurrentStatusVC based on Integer32"""
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


_FsBockingCurrentStatusVC_Type.__name__ = "Integer32"
_FsBockingCurrentStatusVC_Object = MibTableColumn
fsBockingCurrentStatusVC = _FsBockingCurrentStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3, 1, 3),
    _FsBockingCurrentStatusVC_Type()
)
fsBockingCurrentStatusVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingCurrentStatusVC.setStatus("current")


class _FsBockingTryAccessZoneNameVC_Type(DisplayString):
    """Custom type fsBockingTryAccessZoneNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsBockingTryAccessZoneNameVC_Type.__name__ = "DisplayString"
_FsBockingTryAccessZoneNameVC_Object = MibTableColumn
fsBockingTryAccessZoneNameVC = _FsBockingTryAccessZoneNameVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3, 1, 4),
    _FsBockingTryAccessZoneNameVC_Type()
)
fsBockingTryAccessZoneNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBockingTryAccessZoneNameVC.setStatus("current")
_FsBockingEntryStatusVC_Type = ConfigStatus
_FsBockingEntryStatusVC_Object = MibTableColumn
fsBockingEntryStatusVC = _FsBockingEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 1, 3, 1, 5),
    _FsBockingEntryStatusVC_Type()
)
fsBockingEntryStatusVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBockingEntryStatusVC.setStatus("current")
_FsSecZoneVCMIBConformance_ObjectIdentity = ObjectIdentity
fsSecZoneVCMIBConformance = _FsSecZoneVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 3)
)
_FsSecZoneVCMIBCompliances_ObjectIdentity = ObjectIdentity
fsSecZoneVCMIBCompliances = _FsSecZoneVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 3, 1)
)
_FsSecZoneVCMIBGroups_ObjectIdentity = ObjectIdentity
fsSecZoneVCMIBGroups = _FsSecZoneVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 3, 2)
)

# Managed Objects groups

fsSecZoneVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 3, 2, 1)
)
fsSecZoneVCMIBGroup.setObjects(
      *(("FS-SECZONE-CONTEXT-MIB", "fsSecZoneContextNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneChainNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneLevelVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneAclNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneViolationNotifyThreshVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneViolationNotifyActionVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneViolationBlockThreshVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneViolationBlockActionVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneViolationBlockTimeoutVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneChainEntryStatusVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsZone2ZoneContextNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsZoneFirstNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsZoneSecondNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsZone2ZoneAclNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsZone2ZoneEntryStautsVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsBockingContextNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsBockingIPVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsBockingCurrentStatusVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsBockingTryAccessZoneNameVC"),
        ("FS-SECZONE-CONTEXT-MIB", "fsBockingEntryStatusVC"))
)
if mibBuilder.loadTexts:
    fsSecZoneVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsSecZoneVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 68, 3, 1, 1)
)
fsSecZoneVCMIBCompliance.setObjects(
    ("FS-SECZONE-CONTEXT-MIB", "fsSecZoneVCMIBGroup")
)
if mibBuilder.loadTexts:
    fsSecZoneVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SECZONE-CONTEXT-MIB",
    **{"fsSecZoneVCMIB": fsSecZoneVCMIB,
       "fsSecZoneVCMIBObjects": fsSecZoneVCMIBObjects,
       "fsSecZoneChainVCTable": fsSecZoneChainVCTable,
       "fsSecZoneChainVCEntry": fsSecZoneChainVCEntry,
       "fsSecZoneContextNameVC": fsSecZoneContextNameVC,
       "fsSecZoneChainNameVC": fsSecZoneChainNameVC,
       "fsSecZoneLevelVC": fsSecZoneLevelVC,
       "fsSecZoneAclNameVC": fsSecZoneAclNameVC,
       "fsSecZoneViolationNotifyThreshVC": fsSecZoneViolationNotifyThreshVC,
       "fsSecZoneViolationNotifyActionVC": fsSecZoneViolationNotifyActionVC,
       "fsSecZoneViolationBlockThreshVC": fsSecZoneViolationBlockThreshVC,
       "fsSecZoneViolationBlockActionVC": fsSecZoneViolationBlockActionVC,
       "fsSecZoneViolationBlockTimeoutVC": fsSecZoneViolationBlockTimeoutVC,
       "fsSecZoneChainEntryStatusVC": fsSecZoneChainEntryStatusVC,
       "fsSecZone2ZoneVCTable": fsSecZone2ZoneVCTable,
       "fsSecZone2ZoneVCEntry": fsSecZone2ZoneVCEntry,
       "fsZone2ZoneContextNameVC": fsZone2ZoneContextNameVC,
       "fsZoneFirstNameVC": fsZoneFirstNameVC,
       "fsZoneSecondNameVC": fsZoneSecondNameVC,
       "fsZone2ZoneAclNameVC": fsZone2ZoneAclNameVC,
       "fsZone2ZoneEntryStautsVC": fsZone2ZoneEntryStautsVC,
       "fsSecZoneBlockingVCTable": fsSecZoneBlockingVCTable,
       "fsSecZoneBlockingVCEntry": fsSecZoneBlockingVCEntry,
       "fsBockingContextNameVC": fsBockingContextNameVC,
       "fsBockingIPVC": fsBockingIPVC,
       "fsBockingCurrentStatusVC": fsBockingCurrentStatusVC,
       "fsBockingTryAccessZoneNameVC": fsBockingTryAccessZoneNameVC,
       "fsBockingEntryStatusVC": fsBockingEntryStatusVC,
       "fsSecZoneVCMIBConformance": fsSecZoneVCMIBConformance,
       "fsSecZoneVCMIBCompliances": fsSecZoneVCMIBCompliances,
       "fsSecZoneVCMIBCompliance": fsSecZoneVCMIBCompliance,
       "fsSecZoneVCMIBGroups": fsSecZoneVCMIBGroups,
       "fsSecZoneVCMIBGroup": fsSecZoneVCMIBGroup}
)
