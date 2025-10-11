# SNMP MIB module (MY-IGMP-FILTERINGPROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-IGMP-FILTERINGPROFILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:33 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "MY-TC",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

myIgmpFilteringProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37)
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileMIB.setRevisions(
        ("2003-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyIgmpFilteringProfileMIBObjects_ObjectIdentity = ObjectIdentity
myIgmpFilteringProfileMIBObjects = _MyIgmpFilteringProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1)
)
_MyIgmpFilteringMaxProfiles_Type = Unsigned32
_MyIgmpFilteringMaxProfiles_Object = MibScalar
myIgmpFilteringMaxProfiles = _MyIgmpFilteringMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 1),
    _MyIgmpFilteringMaxProfiles_Type()
)
myIgmpFilteringMaxProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpFilteringMaxProfiles.setStatus("current")
_MyIgmpFilteringProfileActionTable_Object = MibTable
myIgmpFilteringProfileActionTable = _MyIgmpFilteringProfileActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2)
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileActionTable.setStatus("current")
_MyIgmpFilteringProfileActionEntry_Object = MibTableRow
myIgmpFilteringProfileActionEntry = _MyIgmpFilteringProfileActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1)
)
myIgmpFilteringProfileActionEntry.setIndexNames(
    (0, "MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileIndex"),
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileActionEntry.setStatus("current")
_MyIgmpFilteringProfileIndex_Type = Unsigned32
_MyIgmpFilteringProfileIndex_Object = MibTableColumn
myIgmpFilteringProfileIndex = _MyIgmpFilteringProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1, 1),
    _MyIgmpFilteringProfileIndex_Type()
)
myIgmpFilteringProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpFilteringProfileIndex.setStatus("current")


class _MyIgmpFilteringProfileAction_Type(Integer32):
    """Custom type myIgmpFilteringProfileAction based on Integer32"""
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


_MyIgmpFilteringProfileAction_Type.__name__ = "Integer32"
_MyIgmpFilteringProfileAction_Object = MibTableColumn
myIgmpFilteringProfileAction = _MyIgmpFilteringProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1, 2),
    _MyIgmpFilteringProfileAction_Type()
)
myIgmpFilteringProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpFilteringProfileAction.setStatus("current")


class _MyIgmpFilteringProfileStatus_Type(Integer32):
    """Custom type myIgmpFilteringProfileStatus based on Integer32"""
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


_MyIgmpFilteringProfileStatus_Type.__name__ = "Integer32"
_MyIgmpFilteringProfileStatus_Object = MibTableColumn
myIgmpFilteringProfileStatus = _MyIgmpFilteringProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 2, 1, 3),
    _MyIgmpFilteringProfileStatus_Type()
)
myIgmpFilteringProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpFilteringProfileStatus.setStatus("current")
_MyIgmpFilteringProfileRangeTable_Object = MibTable
myIgmpFilteringProfileRangeTable = _MyIgmpFilteringProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3)
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileRangeTable.setStatus("current")
_MyIgmpFilteringProfileRangeEntry_Object = MibTableRow
myIgmpFilteringProfileRangeEntry = _MyIgmpFilteringProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1)
)
myIgmpFilteringProfileRangeEntry.setIndexNames(
    (0, "MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileRangeIndex"),
    (0, "MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfieRangeMyAddress"),
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileRangeEntry.setStatus("current")
_MyIgmpFilteringProfileRangeIndex_Type = Unsigned32
_MyIgmpFilteringProfileRangeIndex_Object = MibTableColumn
myIgmpFilteringProfileRangeIndex = _MyIgmpFilteringProfileRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 1),
    _MyIgmpFilteringProfileRangeIndex_Type()
)
myIgmpFilteringProfileRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIgmpFilteringProfileRangeIndex.setStatus("current")
_MyIgmpFilteringProfieRangeMyAddress_Type = IpAddress
_MyIgmpFilteringProfieRangeMyAddress_Object = MibTableColumn
myIgmpFilteringProfieRangeMyAddress = _MyIgmpFilteringProfieRangeMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 2),
    _MyIgmpFilteringProfieRangeMyAddress_Type()
)
myIgmpFilteringProfieRangeMyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpFilteringProfieRangeMyAddress.setStatus("current")
_MyIgmpFilteringProfieRangeEndAddress_Type = IpAddress
_MyIgmpFilteringProfieRangeEndAddress_Object = MibTableColumn
myIgmpFilteringProfieRangeEndAddress = _MyIgmpFilteringProfieRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 3),
    _MyIgmpFilteringProfieRangeEndAddress_Type()
)
myIgmpFilteringProfieRangeEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIgmpFilteringProfieRangeEndAddress.setStatus("current")
_MyIgmpFilteringProfileRangeStatus_Type = RowStatus
_MyIgmpFilteringProfileRangeStatus_Object = MibTableColumn
myIgmpFilteringProfileRangeStatus = _MyIgmpFilteringProfileRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 1, 3, 1, 4),
    _MyIgmpFilteringProfileRangeStatus_Type()
)
myIgmpFilteringProfileRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myIgmpFilteringProfileRangeStatus.setStatus("current")
_MyIgmpFilteringProfileMIBConformance_ObjectIdentity = ObjectIdentity
myIgmpFilteringProfileMIBConformance = _MyIgmpFilteringProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2)
)
_MyIgmpFilteringProfileMIBCompliances_ObjectIdentity = ObjectIdentity
myIgmpFilteringProfileMIBCompliances = _MyIgmpFilteringProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 1)
)
_MyIgmpFilteringProfileMIBGroups_ObjectIdentity = ObjectIdentity
myIgmpFilteringProfileMIBGroups = _MyIgmpFilteringProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 2)
)

# Managed Objects groups

myIgmpFilteringProfileMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 2, 1)
)
myIgmpFilteringProfileMIBGroup.setObjects(
      *(("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringMaxProfiles"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileIndex"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileAction"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileStatus"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileRangeIndex"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfieRangeMyAddress"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfieRangeEndAddress"),
        ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileRangeStatus"))
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myIgmpFilteringProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 37, 2, 1, 1)
)
myIgmpFilteringProfileMIBCompliance.setObjects(
    ("MY-IGMP-FILTERINGPROFILE-MIB", "myIgmpFilteringProfileMIBGroup")
)
if mibBuilder.loadTexts:
    myIgmpFilteringProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-IGMP-FILTERINGPROFILE-MIB",
    **{"myIgmpFilteringProfileMIB": myIgmpFilteringProfileMIB,
       "myIgmpFilteringProfileMIBObjects": myIgmpFilteringProfileMIBObjects,
       "myIgmpFilteringMaxProfiles": myIgmpFilteringMaxProfiles,
       "myIgmpFilteringProfileActionTable": myIgmpFilteringProfileActionTable,
       "myIgmpFilteringProfileActionEntry": myIgmpFilteringProfileActionEntry,
       "myIgmpFilteringProfileIndex": myIgmpFilteringProfileIndex,
       "myIgmpFilteringProfileAction": myIgmpFilteringProfileAction,
       "myIgmpFilteringProfileStatus": myIgmpFilteringProfileStatus,
       "myIgmpFilteringProfileRangeTable": myIgmpFilteringProfileRangeTable,
       "myIgmpFilteringProfileRangeEntry": myIgmpFilteringProfileRangeEntry,
       "myIgmpFilteringProfileRangeIndex": myIgmpFilteringProfileRangeIndex,
       "myIgmpFilteringProfieRangeMyAddress": myIgmpFilteringProfieRangeMyAddress,
       "myIgmpFilteringProfieRangeEndAddress": myIgmpFilteringProfieRangeEndAddress,
       "myIgmpFilteringProfileRangeStatus": myIgmpFilteringProfileRangeStatus,
       "myIgmpFilteringProfileMIBConformance": myIgmpFilteringProfileMIBConformance,
       "myIgmpFilteringProfileMIBCompliances": myIgmpFilteringProfileMIBCompliances,
       "myIgmpFilteringProfileMIBCompliance": myIgmpFilteringProfileMIBCompliance,
       "myIgmpFilteringProfileMIBGroups": myIgmpFilteringProfileMIBGroups,
       "myIgmpFilteringProfileMIBGroup": myIgmpFilteringProfileMIBGroup}
)
