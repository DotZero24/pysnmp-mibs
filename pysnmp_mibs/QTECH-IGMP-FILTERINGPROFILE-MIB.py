# SNMP MIB module (QTECH-IGMP-FILTERINGPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IGMP-FILTERINGPROFILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:38 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechIgmpFilteringProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37)
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileMIB.setRevisions(
        ("2003-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechIgmpFilteringProfileMIBObjects_ObjectIdentity = ObjectIdentity
qtechIgmpFilteringProfileMIBObjects = _QtechIgmpFilteringProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1)
)
_QtechIgmpFilteringMaxProfiles_Type = Unsigned32
_QtechIgmpFilteringMaxProfiles_Object = MibScalar
qtechIgmpFilteringMaxProfiles = _QtechIgmpFilteringMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 1),
    _QtechIgmpFilteringMaxProfiles_Type()
)
qtechIgmpFilteringMaxProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpFilteringMaxProfiles.setStatus("current")
_QtechIgmpFilteringProfileActionTable_Object = MibTable
qtechIgmpFilteringProfileActionTable = _QtechIgmpFilteringProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 2)
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileActionTable.setStatus("current")
_QtechIgmpFilteringProfileActionEntry_Object = MibTableRow
qtechIgmpFilteringProfileActionEntry = _QtechIgmpFilteringProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 2, 1)
)
qtechIgmpFilteringProfileActionEntry.setIndexNames(
    (0, "QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileIndex"),
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileActionEntry.setStatus("current")
_QtechIgmpFilteringProfileIndex_Type = Unsigned32
_QtechIgmpFilteringProfileIndex_Object = MibTableColumn
qtechIgmpFilteringProfileIndex = _QtechIgmpFilteringProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 2, 1, 1),
    _QtechIgmpFilteringProfileIndex_Type()
)
qtechIgmpFilteringProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileIndex.setStatus("current")


class _QtechIgmpFilteringProfileAction_Type(Integer32):
    """Custom type qtechIgmpFilteringProfileAction based on Integer32"""
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


_QtechIgmpFilteringProfileAction_Type.__name__ = "Integer32"
_QtechIgmpFilteringProfileAction_Object = MibTableColumn
qtechIgmpFilteringProfileAction = _QtechIgmpFilteringProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 2, 1, 2),
    _QtechIgmpFilteringProfileAction_Type()
)
qtechIgmpFilteringProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileAction.setStatus("current")


class _QtechIgmpFilteringProfileStatus_Type(Integer32):
    """Custom type qtechIgmpFilteringProfileStatus based on Integer32"""
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


_QtechIgmpFilteringProfileStatus_Type.__name__ = "Integer32"
_QtechIgmpFilteringProfileStatus_Object = MibTableColumn
qtechIgmpFilteringProfileStatus = _QtechIgmpFilteringProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 2, 1, 3),
    _QtechIgmpFilteringProfileStatus_Type()
)
qtechIgmpFilteringProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileStatus.setStatus("current")
_QtechIgmpFilteringProfileRangeTable_Object = MibTable
qtechIgmpFilteringProfileRangeTable = _QtechIgmpFilteringProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 3)
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileRangeTable.setStatus("current")
_QtechIgmpFilteringProfileRangeEntry_Object = MibTableRow
qtechIgmpFilteringProfileRangeEntry = _QtechIgmpFilteringProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 3, 1)
)
qtechIgmpFilteringProfileRangeEntry.setIndexNames(
    (0, "QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileRangeIndex"),
    (0, "QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfieRangeQtechAddress"),
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileRangeEntry.setStatus("current")
_QtechIgmpFilteringProfileRangeIndex_Type = Unsigned32
_QtechIgmpFilteringProfileRangeIndex_Object = MibTableColumn
qtechIgmpFilteringProfileRangeIndex = _QtechIgmpFilteringProfileRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 3, 1, 1),
    _QtechIgmpFilteringProfileRangeIndex_Type()
)
qtechIgmpFilteringProfileRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileRangeIndex.setStatus("current")
_QtechIgmpFilteringProfieRangeQtechAddress_Type = IpAddress
_QtechIgmpFilteringProfieRangeQtechAddress_Object = MibTableColumn
qtechIgmpFilteringProfieRangeQtechAddress = _QtechIgmpFilteringProfieRangeQtechAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 3, 1, 2),
    _QtechIgmpFilteringProfieRangeQtechAddress_Type()
)
qtechIgmpFilteringProfieRangeQtechAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfieRangeQtechAddress.setStatus("current")
_QtechIgmpFilteringProfieRangeEndAddress_Type = IpAddress
_QtechIgmpFilteringProfieRangeEndAddress_Object = MibTableColumn
qtechIgmpFilteringProfieRangeEndAddress = _QtechIgmpFilteringProfieRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 3, 1, 3),
    _QtechIgmpFilteringProfieRangeEndAddress_Type()
)
qtechIgmpFilteringProfieRangeEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfieRangeEndAddress.setStatus("current")
_QtechIgmpFilteringProfileRangeStatus_Type = RowStatus
_QtechIgmpFilteringProfileRangeStatus_Object = MibTableColumn
qtechIgmpFilteringProfileRangeStatus = _QtechIgmpFilteringProfileRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 1, 3, 1, 4),
    _QtechIgmpFilteringProfileRangeStatus_Type()
)
qtechIgmpFilteringProfileRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileRangeStatus.setStatus("current")
_QtechIgmpFilteringProfileMIBConformance_ObjectIdentity = ObjectIdentity
qtechIgmpFilteringProfileMIBConformance = _QtechIgmpFilteringProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 2)
)
_QtechIgmpFilteringProfileMIBCompliances_ObjectIdentity = ObjectIdentity
qtechIgmpFilteringProfileMIBCompliances = _QtechIgmpFilteringProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 2, 1)
)
_QtechIgmpFilteringProfileMIBGroups_ObjectIdentity = ObjectIdentity
qtechIgmpFilteringProfileMIBGroups = _QtechIgmpFilteringProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 2, 2)
)

# Managed Objects groups

qtechIgmpFilteringProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 2, 2, 1)
)
qtechIgmpFilteringProfileMIBGroup.setObjects(
      *(("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringMaxProfiles"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileIndex"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileAction"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileStatus"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileRangeIndex"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfieRangeQtechAddress"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfieRangeEndAddress"),
        ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileRangeStatus"))
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechIgmpFilteringProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 37, 2, 1, 1)
)
qtechIgmpFilteringProfileMIBCompliance.setObjects(
    ("QTECH-IGMP-FILTERINGPROFILE-MIB", "qtechIgmpFilteringProfileMIBGroup")
)
if mibBuilder.loadTexts:
    qtechIgmpFilteringProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IGMP-FILTERINGPROFILE-MIB",
    **{"qtechIgmpFilteringProfileMIB": qtechIgmpFilteringProfileMIB,
       "qtechIgmpFilteringProfileMIBObjects": qtechIgmpFilteringProfileMIBObjects,
       "qtechIgmpFilteringMaxProfiles": qtechIgmpFilteringMaxProfiles,
       "qtechIgmpFilteringProfileActionTable": qtechIgmpFilteringProfileActionTable,
       "qtechIgmpFilteringProfileActionEntry": qtechIgmpFilteringProfileActionEntry,
       "qtechIgmpFilteringProfileIndex": qtechIgmpFilteringProfileIndex,
       "qtechIgmpFilteringProfileAction": qtechIgmpFilteringProfileAction,
       "qtechIgmpFilteringProfileStatus": qtechIgmpFilteringProfileStatus,
       "qtechIgmpFilteringProfileRangeTable": qtechIgmpFilteringProfileRangeTable,
       "qtechIgmpFilteringProfileRangeEntry": qtechIgmpFilteringProfileRangeEntry,
       "qtechIgmpFilteringProfileRangeIndex": qtechIgmpFilteringProfileRangeIndex,
       "qtechIgmpFilteringProfieRangeQtechAddress": qtechIgmpFilteringProfieRangeQtechAddress,
       "qtechIgmpFilteringProfieRangeEndAddress": qtechIgmpFilteringProfieRangeEndAddress,
       "qtechIgmpFilteringProfileRangeStatus": qtechIgmpFilteringProfileRangeStatus,
       "qtechIgmpFilteringProfileMIBConformance": qtechIgmpFilteringProfileMIBConformance,
       "qtechIgmpFilteringProfileMIBCompliances": qtechIgmpFilteringProfileMIBCompliances,
       "qtechIgmpFilteringProfileMIBCompliance": qtechIgmpFilteringProfileMIBCompliance,
       "qtechIgmpFilteringProfileMIBGroups": qtechIgmpFilteringProfileMIBGroups,
       "qtechIgmpFilteringProfileMIBGroup": qtechIgmpFilteringProfileMIBGroup}
)
