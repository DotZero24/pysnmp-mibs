# SNMP MIB module (FS-IGMP-FILTERINGPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IGMP-FILTERINGPROFILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:29 2025
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

fsIgmpFilteringProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37)
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileMIB.setRevisions(
        ("2003-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIgmpFilteringProfileMIBObjects_ObjectIdentity = ObjectIdentity
fsIgmpFilteringProfileMIBObjects = _FsIgmpFilteringProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1)
)
_FsIgmpFilteringMaxProfiles_Type = Unsigned32
_FsIgmpFilteringMaxProfiles_Object = MibScalar
fsIgmpFilteringMaxProfiles = _FsIgmpFilteringMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 1),
    _FsIgmpFilteringMaxProfiles_Type()
)
fsIgmpFilteringMaxProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpFilteringMaxProfiles.setStatus("current")
_FsIgmpFilteringProfileActionTable_Object = MibTable
fsIgmpFilteringProfileActionTable = _FsIgmpFilteringProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 2)
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileActionTable.setStatus("current")
_FsIgmpFilteringProfileActionEntry_Object = MibTableRow
fsIgmpFilteringProfileActionEntry = _FsIgmpFilteringProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 2, 1)
)
fsIgmpFilteringProfileActionEntry.setIndexNames(
    (0, "FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileActionEntry.setStatus("current")
_FsIgmpFilteringProfileIndex_Type = Unsigned32
_FsIgmpFilteringProfileIndex_Object = MibTableColumn
fsIgmpFilteringProfileIndex = _FsIgmpFilteringProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 2, 1, 1),
    _FsIgmpFilteringProfileIndex_Type()
)
fsIgmpFilteringProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileIndex.setStatus("current")


class _FsIgmpFilteringProfileAction_Type(Integer32):
    """Custom type fsIgmpFilteringProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_FsIgmpFilteringProfileAction_Type.__name__ = "Integer32"
_FsIgmpFilteringProfileAction_Object = MibTableColumn
fsIgmpFilteringProfileAction = _FsIgmpFilteringProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 2, 1, 2),
    _FsIgmpFilteringProfileAction_Type()
)
fsIgmpFilteringProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileAction.setStatus("current")


class _FsIgmpFilteringProfileStatus_Type(Integer32):
    """Custom type fsIgmpFilteringProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_FsIgmpFilteringProfileStatus_Type.__name__ = "Integer32"
_FsIgmpFilteringProfileStatus_Object = MibTableColumn
fsIgmpFilteringProfileStatus = _FsIgmpFilteringProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 2, 1, 3),
    _FsIgmpFilteringProfileStatus_Type()
)
fsIgmpFilteringProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileStatus.setStatus("current")
_FsIgmpFilteringProfileRangeTable_Object = MibTable
fsIgmpFilteringProfileRangeTable = _FsIgmpFilteringProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 3)
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileRangeTable.setStatus("current")
_FsIgmpFilteringProfileRangeEntry_Object = MibTableRow
fsIgmpFilteringProfileRangeEntry = _FsIgmpFilteringProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 3, 1)
)
fsIgmpFilteringProfileRangeEntry.setIndexNames(
    (0, "FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileRangeIndex"),
    (0, "FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfieRangeFSAddress"),
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileRangeEntry.setStatus("current")
_FsIgmpFilteringProfileRangeIndex_Type = Unsigned32
_FsIgmpFilteringProfileRangeIndex_Object = MibTableColumn
fsIgmpFilteringProfileRangeIndex = _FsIgmpFilteringProfileRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 3, 1, 1),
    _FsIgmpFilteringProfileRangeIndex_Type()
)
fsIgmpFilteringProfileRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileRangeIndex.setStatus("current")
_FsIgmpFilteringProfieRangeFSAddress_Type = IpAddress
_FsIgmpFilteringProfieRangeFSAddress_Object = MibTableColumn
fsIgmpFilteringProfieRangeFSAddress = _FsIgmpFilteringProfieRangeFSAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 3, 1, 2),
    _FsIgmpFilteringProfieRangeFSAddress_Type()
)
fsIgmpFilteringProfieRangeFSAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfieRangeFSAddress.setStatus("current")
_FsIgmpFilteringProfieRangeEndAddress_Type = IpAddress
_FsIgmpFilteringProfieRangeEndAddress_Object = MibTableColumn
fsIgmpFilteringProfieRangeEndAddress = _FsIgmpFilteringProfieRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 3, 1, 3),
    _FsIgmpFilteringProfieRangeEndAddress_Type()
)
fsIgmpFilteringProfieRangeEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfieRangeEndAddress.setStatus("current")
_FsIgmpFilteringProfileRangeStatus_Type = RowStatus
_FsIgmpFilteringProfileRangeStatus_Object = MibTableColumn
fsIgmpFilteringProfileRangeStatus = _FsIgmpFilteringProfileRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 1, 3, 1, 4),
    _FsIgmpFilteringProfileRangeStatus_Type()
)
fsIgmpFilteringProfileRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileRangeStatus.setStatus("current")
_FsIgmpFilteringProfileMIBConformance_ObjectIdentity = ObjectIdentity
fsIgmpFilteringProfileMIBConformance = _FsIgmpFilteringProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 2)
)
_FsIgmpFilteringProfileMIBCompliances_ObjectIdentity = ObjectIdentity
fsIgmpFilteringProfileMIBCompliances = _FsIgmpFilteringProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 2, 1)
)
_FsIgmpFilteringProfileMIBGroups_ObjectIdentity = ObjectIdentity
fsIgmpFilteringProfileMIBGroups = _FsIgmpFilteringProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 2, 2)
)

# Managed Objects groups

fsIgmpFilteringProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 2, 2, 1)
)
fsIgmpFilteringProfileMIBGroup.setObjects(
      *(("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringMaxProfiles"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileIndex"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileAction"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileStatus"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileRangeIndex"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfieRangeFSAddress"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfieRangeEndAddress"),
        ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileRangeStatus"))
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsIgmpFilteringProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 37, 2, 1, 1)
)
fsIgmpFilteringProfileMIBCompliance.setObjects(
    ("FS-IGMP-FILTERINGPROFILE-MIB", "fsIgmpFilteringProfileMIBGroup")
)
if mibBuilder.loadTexts:
    fsIgmpFilteringProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IGMP-FILTERINGPROFILE-MIB",
    **{"fsIgmpFilteringProfileMIB": fsIgmpFilteringProfileMIB,
       "fsIgmpFilteringProfileMIBObjects": fsIgmpFilteringProfileMIBObjects,
       "fsIgmpFilteringMaxProfiles": fsIgmpFilteringMaxProfiles,
       "fsIgmpFilteringProfileActionTable": fsIgmpFilteringProfileActionTable,
       "fsIgmpFilteringProfileActionEntry": fsIgmpFilteringProfileActionEntry,
       "fsIgmpFilteringProfileIndex": fsIgmpFilteringProfileIndex,
       "fsIgmpFilteringProfileAction": fsIgmpFilteringProfileAction,
       "fsIgmpFilteringProfileStatus": fsIgmpFilteringProfileStatus,
       "fsIgmpFilteringProfileRangeTable": fsIgmpFilteringProfileRangeTable,
       "fsIgmpFilteringProfileRangeEntry": fsIgmpFilteringProfileRangeEntry,
       "fsIgmpFilteringProfileRangeIndex": fsIgmpFilteringProfileRangeIndex,
       "fsIgmpFilteringProfieRangeFSAddress": fsIgmpFilteringProfieRangeFSAddress,
       "fsIgmpFilteringProfieRangeEndAddress": fsIgmpFilteringProfieRangeEndAddress,
       "fsIgmpFilteringProfileRangeStatus": fsIgmpFilteringProfileRangeStatus,
       "fsIgmpFilteringProfileMIBConformance": fsIgmpFilteringProfileMIBConformance,
       "fsIgmpFilteringProfileMIBCompliances": fsIgmpFilteringProfileMIBCompliances,
       "fsIgmpFilteringProfileMIBCompliance": fsIgmpFilteringProfileMIBCompliance,
       "fsIgmpFilteringProfileMIBGroups": fsIgmpFilteringProfileMIBGroups,
       "fsIgmpFilteringProfileMIBGroup": fsIgmpFilteringProfileMIBGroup}
)
