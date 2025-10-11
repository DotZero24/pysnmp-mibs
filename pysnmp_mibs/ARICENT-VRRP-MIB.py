# SNMP MIB module (ARICENT-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-VRRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:49 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(vrrpOperEntry,) = mibBuilder.importSymbols(
    "VRRP-MIB",
    "vrrpOperEntry")


# MODULE-IDENTITY

fsvrrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 153)
)
if mibBuilder.loadTexts:
    fsvrrp.setRevisions(
        ("2013-11-18 00:00",
         "2011-09-12 00:00",
         "2011-08-30 00:00",
         "2011-03-11 00:00",
         "2006-08-03 00:00",
         "2006-04-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVrrpSystem_ObjectIdentity = ObjectIdentity
fsVrrpSystem = _FsVrrpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1)
)


class _FsVrrpStatus_Type(Integer32):
    """Custom type fsVrrpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsVrrpStatus_Type.__name__ = "Integer32"
_FsVrrpStatus_Object = MibScalar
fsVrrpStatus = _FsVrrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 1),
    _FsVrrpStatus_Type()
)
fsVrrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpStatus.setStatus("current")
_FsVrrpMaxOperEntries_Type = Integer32
_FsVrrpMaxOperEntries_Object = MibScalar
fsVrrpMaxOperEntries = _FsVrrpMaxOperEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 2),
    _FsVrrpMaxOperEntries_Type()
)
fsVrrpMaxOperEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVrrpMaxOperEntries.setStatus("current")
_FsVrrpOperTable_Object = MibTable
fsVrrpOperTable = _FsVrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 3)
)
if mibBuilder.loadTexts:
    fsVrrpOperTable.setStatus("current")
_FsVrrpOperEntry_Object = MibTableRow
fsVrrpOperEntry = _FsVrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsVrrpOperEntry.setStatus("current")


class _FsVrrpAdminPriority_Type(Integer32):
    """Custom type fsVrrpAdminPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_FsVrrpAdminPriority_Type.__name__ = "Integer32"
_FsVrrpAdminPriority_Object = MibTableColumn
fsVrrpAdminPriority = _FsVrrpAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 3, 1, 1),
    _FsVrrpAdminPriority_Type()
)
fsVrrpAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpAdminPriority.setStatus("current")


class _FsVrrpOperAdvertisementIntervalInMsec_Type(Integer32):
    """Custom type fsVrrpOperAdvertisementIntervalInMsec based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 255000),
    )


_FsVrrpOperAdvertisementIntervalInMsec_Type.__name__ = "Integer32"
_FsVrrpOperAdvertisementIntervalInMsec_Object = MibTableColumn
fsVrrpOperAdvertisementIntervalInMsec = _FsVrrpOperAdvertisementIntervalInMsec_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 3, 1, 2),
    _FsVrrpOperAdvertisementIntervalInMsec_Type()
)
fsVrrpOperAdvertisementIntervalInMsec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpOperAdvertisementIntervalInMsec.setStatus("current")
if mibBuilder.loadTexts:
    fsVrrpOperAdvertisementIntervalInMsec.setUnits("milli seconds")


class _FsVrrpOperTrackGroupId_Type(Unsigned32):
    """Custom type fsVrrpOperTrackGroupId based on Unsigned32"""
    defaultValue = 0


_FsVrrpOperTrackGroupId_Type.__name__ = "Unsigned32"
_FsVrrpOperTrackGroupId_Object = MibTableColumn
fsVrrpOperTrackGroupId = _FsVrrpOperTrackGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 3, 1, 3),
    _FsVrrpOperTrackGroupId_Type()
)
fsVrrpOperTrackGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupId.setStatus("current")


class _FsVrrpOperDecrementPriority_Type(Unsigned32):
    """Custom type fsVrrpOperDecrementPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_FsVrrpOperDecrementPriority_Type.__name__ = "Unsigned32"
_FsVrrpOperDecrementPriority_Object = MibTableColumn
fsVrrpOperDecrementPriority = _FsVrrpOperDecrementPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 3, 1, 4),
    _FsVrrpOperDecrementPriority_Type()
)
fsVrrpOperDecrementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpOperDecrementPriority.setStatus("current")


class _FsVrrpAuthDeprecate_Type(Integer32):
    """Custom type fsVrrpAuthDeprecate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsVrrpAuthDeprecate_Type.__name__ = "Integer32"
_FsVrrpAuthDeprecate_Object = MibScalar
fsVrrpAuthDeprecate = _FsVrrpAuthDeprecate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 4),
    _FsVrrpAuthDeprecate_Type()
)
fsVrrpAuthDeprecate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpAuthDeprecate.setStatus("current")


class _FsVrrpTraceOption_Type(Integer32):
    """Custom type fsVrrpTraceOption based on Integer32"""
    defaultValue = 0


_FsVrrpTraceOption_Type.__name__ = "Integer32"
_FsVrrpTraceOption_Object = MibScalar
fsVrrpTraceOption = _FsVrrpTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 5),
    _FsVrrpTraceOption_Type()
)
fsVrrpTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVrrpTraceOption.setStatus("current")
_FsVrrpOperTrackGroupTable_Object = MibTable
fsVrrpOperTrackGroupTable = _FsVrrpOperTrackGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 6)
)
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupTable.setStatus("current")
_FsVrrpOperTrackGroupEntry_Object = MibTableRow
fsVrrpOperTrackGroupEntry = _FsVrrpOperTrackGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 6, 1)
)
fsVrrpOperTrackGroupEntry.setIndexNames(
    (0, "ARICENT-VRRP-MIB", "fsVrrpOperTrackGroupIndex"),
)
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupEntry.setStatus("current")
_FsVrrpOperTrackGroupIndex_Type = Unsigned32
_FsVrrpOperTrackGroupIndex_Object = MibTableColumn
fsVrrpOperTrackGroupIndex = _FsVrrpOperTrackGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 6, 1, 1),
    _FsVrrpOperTrackGroupIndex_Type()
)
fsVrrpOperTrackGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupIndex.setStatus("current")


class _FsVrrpOperTrackedGroupTrackedLinks_Type(Unsigned32):
    """Custom type fsVrrpOperTrackedGroupTrackedLinks based on Unsigned32"""
    defaultValue = 0


_FsVrrpOperTrackedGroupTrackedLinks_Type.__name__ = "Unsigned32"
_FsVrrpOperTrackedGroupTrackedLinks_Object = MibTableColumn
fsVrrpOperTrackedGroupTrackedLinks = _FsVrrpOperTrackedGroupTrackedLinks_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 6, 1, 2),
    _FsVrrpOperTrackedGroupTrackedLinks_Type()
)
fsVrrpOperTrackedGroupTrackedLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpOperTrackedGroupTrackedLinks.setStatus("current")
_FsVrrpOperTrackRowStatus_Type = RowStatus
_FsVrrpOperTrackRowStatus_Object = MibTableColumn
fsVrrpOperTrackRowStatus = _FsVrrpOperTrackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 6, 1, 3),
    _FsVrrpOperTrackRowStatus_Type()
)
fsVrrpOperTrackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpOperTrackRowStatus.setStatus("current")
_FsVrrpOperTrackGroupIfTable_Object = MibTable
fsVrrpOperTrackGroupIfTable = _FsVrrpOperTrackGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 7)
)
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupIfTable.setStatus("current")
_FsVrrpOperTrackGroupIfEntry_Object = MibTableRow
fsVrrpOperTrackGroupIfEntry = _FsVrrpOperTrackGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 7, 1)
)
fsVrrpOperTrackGroupIfEntry.setIndexNames(
    (0, "ARICENT-VRRP-MIB", "fsVrrpOperTrackGroupIndex"),
    (0, "ARICENT-VRRP-MIB", "fsVrrpOperTrackGroupIfIndex"),
)
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupIfEntry.setStatus("current")
_FsVrrpOperTrackGroupIfIndex_Type = InterfaceIndexOrZero
_FsVrrpOperTrackGroupIfIndex_Object = MibTableColumn
fsVrrpOperTrackGroupIfIndex = _FsVrrpOperTrackGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 7, 1, 1),
    _FsVrrpOperTrackGroupIfIndex_Type()
)
fsVrrpOperTrackGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupIfIndex.setStatus("current")
_FsVrrpOperTrackGroupIfRowStatus_Type = RowStatus
_FsVrrpOperTrackGroupIfRowStatus_Object = MibTableColumn
fsVrrpOperTrackGroupIfRowStatus = _FsVrrpOperTrackGroupIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 153, 1, 7, 1, 2),
    _FsVrrpOperTrackGroupIfRowStatus_Type()
)
fsVrrpOperTrackGroupIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVrrpOperTrackGroupIfRowStatus.setStatus("current")
vrrpOperEntry.registerAugmentions(
    ("ARICENT-VRRP-MIB",
     "fsVrrpOperEntry")
)
fsVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-VRRP-MIB",
    **{"fsvrrp": fsvrrp,
       "fsVrrpSystem": fsVrrpSystem,
       "fsVrrpStatus": fsVrrpStatus,
       "fsVrrpMaxOperEntries": fsVrrpMaxOperEntries,
       "fsVrrpOperTable": fsVrrpOperTable,
       "fsVrrpOperEntry": fsVrrpOperEntry,
       "fsVrrpAdminPriority": fsVrrpAdminPriority,
       "fsVrrpOperAdvertisementIntervalInMsec": fsVrrpOperAdvertisementIntervalInMsec,
       "fsVrrpOperTrackGroupId": fsVrrpOperTrackGroupId,
       "fsVrrpOperDecrementPriority": fsVrrpOperDecrementPriority,
       "fsVrrpAuthDeprecate": fsVrrpAuthDeprecate,
       "fsVrrpTraceOption": fsVrrpTraceOption,
       "fsVrrpOperTrackGroupTable": fsVrrpOperTrackGroupTable,
       "fsVrrpOperTrackGroupEntry": fsVrrpOperTrackGroupEntry,
       "fsVrrpOperTrackGroupIndex": fsVrrpOperTrackGroupIndex,
       "fsVrrpOperTrackedGroupTrackedLinks": fsVrrpOperTrackedGroupTrackedLinks,
       "fsVrrpOperTrackRowStatus": fsVrrpOperTrackRowStatus,
       "fsVrrpOperTrackGroupIfTable": fsVrrpOperTrackGroupIfTable,
       "fsVrrpOperTrackGroupIfEntry": fsVrrpOperTrackGroupIfEntry,
       "fsVrrpOperTrackGroupIfIndex": fsVrrpOperTrackGroupIfIndex,
       "fsVrrpOperTrackGroupIfRowStatus": fsVrrpOperTrackGroupIfRowStatus}
)
