# SNMP MIB module (DES7200-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-CLUSTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:09 2025
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
    "DES7200-SMI",
    "myMgmt")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

myClusterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31)
)
if mibBuilder.loadTexts:
    myClusterMIB.setRevisions(
        ("2003-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyClusterMIBObjects_ObjectIdentity = ObjectIdentity
myClusterMIBObjects = _MyClusterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1)
)
_ScStatus_ObjectIdentity = ObjectIdentity
scStatus = _ScStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1)
)


class _ScStatusClusterName_Type(DisplayString):
    """Custom type scStatusClusterName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ScStatusClusterName_Type.__name__ = "DisplayString"
_ScStatusClusterName_Object = MibScalar
scStatusClusterName = _ScStatusClusterName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 1),
    _ScStatusClusterName_Type()
)
scStatusClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scStatusClusterName.setStatus("current")


class _ScStatusClusterMode_Type(Integer32):
    """Custom type scStatusClusterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commandDevice", 1),
          ("memberDevice", 2),
          ("none", 3))
    )


_ScStatusClusterMode_Type.__name__ = "Integer32"
_ScStatusClusterMode_Object = MibScalar
scStatusClusterMode = _ScStatusClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 2),
    _ScStatusClusterMode_Type()
)
scStatusClusterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scStatusClusterMode.setStatus("current")


class _ScStatusClusterStatus_Type(EnabledStatus):
    """Custom type scStatusClusterStatus based on EnabledStatus"""
    defaultValue = 1


_ScStatusClusterStatus_Type.__name__ = "EnabledStatus"
_ScStatusClusterStatus_Object = MibScalar
scStatusClusterStatus = _ScStatusClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 3),
    _ScStatusClusterStatus_Type()
)
scStatusClusterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scStatusClusterStatus.setStatus("current")
_ScStatusCommanderMacAddress_Type = MacAddress
_ScStatusCommanderMacAddress_Object = MibScalar
scStatusCommanderMacAddress = _ScStatusCommanderMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 4),
    _ScStatusCommanderMacAddress_Type()
)
scStatusCommanderMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scStatusCommanderMacAddress.setStatus("current")


class _ScStatusTimeOfLastChange_Type(TimeStamp):
    """Custom type scStatusTimeOfLastChange based on TimeStamp"""
    defaultValue = 0


_ScStatusTimeOfLastChange_Type.__name__ = "TimeStamp"
_ScStatusTimeOfLastChange_Object = MibScalar
scStatusTimeOfLastChange = _ScStatusTimeOfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 5),
    _ScStatusTimeOfLastChange_Type()
)
scStatusTimeOfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scStatusTimeOfLastChange.setStatus("current")
_ScStatusMaxNumberOfMembers_Type = Unsigned32
_ScStatusMaxNumberOfMembers_Object = MibScalar
scStatusMaxNumberOfMembers = _ScStatusMaxNumberOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 6),
    _ScStatusMaxNumberOfMembers_Type()
)
scStatusMaxNumberOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scStatusMaxNumberOfMembers.setStatus("current")


class _ScStatusLastFailureAddMember_Type(Integer32):
    """Custom type scStatusLastFailureAddMember based on Integer32"""
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
          ("password", 2),
          ("overmax", 3),
          ("noncandidate", 4),
          ("memberNumberInUse", 5),
          ("unreachable", 6),
          ("communityStringFull", 7))
    )


_ScStatusLastFailureAddMember_Type.__name__ = "Integer32"
_ScStatusLastFailureAddMember_Object = MibScalar
scStatusLastFailureAddMember = _ScStatusLastFailureAddMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 1, 7),
    _ScStatusLastFailureAddMember_Type()
)
scStatusLastFailureAddMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scStatusLastFailureAddMember.setStatus("current")
_ScMember_ObjectIdentity = ObjectIdentity
scMember = _ScMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2)
)
_ScMemberTable_Object = MibTable
scMemberTable = _ScMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    scMemberTable.setStatus("current")
_ScMemberEntry_Object = MibTableRow
scMemberEntry = _ScMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1, 1)
)
scMemberEntry.setIndexNames(
    (0, "DES7200-CLUSTER-MIB", "scMemberMacAddress"),
)
if mibBuilder.loadTexts:
    scMemberEntry.setStatus("current")
_ScMemberMacAddress_Type = MacAddress
_ScMemberMacAddress_Object = MibTableColumn
scMemberMacAddress = _ScMemberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1, 1, 1),
    _ScMemberMacAddress_Type()
)
scMemberMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scMemberMacAddress.setStatus("current")
_ScMemberNumber_Type = Unsigned32
_ScMemberNumber_Object = MibTableColumn
scMemberNumber = _ScMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1, 1, 2),
    _ScMemberNumber_Type()
)
scMemberNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scMemberNumber.setStatus("current")


class _ScMemberOperStatus_Type(Integer32):
    """Custom type scMemberOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ScMemberOperStatus_Type.__name__ = "Integer32"
_ScMemberOperStatus_Object = MibTableColumn
scMemberOperStatus = _ScMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1, 1, 3),
    _ScMemberOperStatus_Type()
)
scMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scMemberOperStatus.setStatus("current")
_ScMemberDeviceID_Type = MacAddress
_ScMemberDeviceID_Object = MibTableColumn
scMemberDeviceID = _ScMemberDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1, 1, 4),
    _ScMemberDeviceID_Type()
)
scMemberDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scMemberDeviceID.setStatus("current")
_ScMemberRowStatus_Type = RowStatus
_ScMemberRowStatus_Object = MibTableColumn
scMemberRowStatus = _ScMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 2, 1, 1, 5),
    _ScMemberRowStatus_Type()
)
scMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scMemberRowStatus.setStatus("current")
_ScCandidate_ObjectIdentity = ObjectIdentity
scCandidate = _ScCandidate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 3)
)
_ScCandidateTable_Object = MibTable
scCandidateTable = _ScCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 3, 1)
)
if mibBuilder.loadTexts:
    scCandidateTable.setStatus("current")
_ScCandidateEntry_Object = MibTableRow
scCandidateEntry = _ScCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 3, 1, 1)
)
scCandidateEntry.setIndexNames(
    (0, "DES7200-CLUSTER-MIB", "scCandidateMacAddress"),
)
if mibBuilder.loadTexts:
    scCandidateEntry.setStatus("current")
_ScCandidateMacAddress_Type = MacAddress
_ScCandidateMacAddress_Object = MibTableColumn
scCandidateMacAddress = _ScCandidateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 1, 3, 1, 1, 1),
    _ScCandidateMacAddress_Type()
)
scCandidateMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scCandidateMacAddress.setStatus("current")
_MyClusterTraps_ObjectIdentity = ObjectIdentity
myClusterTraps = _MyClusterTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 2)
)
_MyClusterMIBConformance_ObjectIdentity = ObjectIdentity
myClusterMIBConformance = _MyClusterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3)
)
_MyClusterMIBCompliances_ObjectIdentity = ObjectIdentity
myClusterMIBCompliances = _MyClusterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 1)
)
_MyClusterMIBGroups_ObjectIdentity = ObjectIdentity
myClusterMIBGroups = _MyClusterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 2)
)

# Managed Objects groups

myClusterStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 2, 1)
)
myClusterStatusGroup.setObjects(
      *(("DES7200-CLUSTER-MIB", "scStatusTimeOfLastChange"),
        ("DES7200-CLUSTER-MIB", "scStatusMaxNumberOfMembers"),
        ("DES7200-CLUSTER-MIB", "scStatusLastFailureAddMember"))
)
if mibBuilder.loadTexts:
    myClusterStatusGroup.setStatus("current")

myClusterMemberStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 2, 2)
)
myClusterMemberStatusGroup.setObjects(
      *(("DES7200-CLUSTER-MIB", "scStatusClusterName"),
        ("DES7200-CLUSTER-MIB", "scStatusClusterMode"),
        ("DES7200-CLUSTER-MIB", "scStatusClusterStatus"),
        ("DES7200-CLUSTER-MIB", "scStatusCommanderMacAddress"))
)
if mibBuilder.loadTexts:
    myClusterMemberStatusGroup.setStatus("current")

myClusterCandidateStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 2, 3)
)
myClusterCandidateStatusGroup.setObjects(
      *(("DES7200-CLUSTER-MIB", "scStatusClusterName"),
        ("DES7200-CLUSTER-MIB", "scStatusClusterMode"),
        ("DES7200-CLUSTER-MIB", "scStatusClusterStatus"))
)
if mibBuilder.loadTexts:
    myClusterCandidateStatusGroup.setStatus("current")

myClusterMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 2, 4)
)
myClusterMemberGroup.setObjects(
      *(("DES7200-CLUSTER-MIB", "scMemberOperStatus"),
        ("DES7200-CLUSTER-MIB", "scMemberNumber"),
        ("DES7200-CLUSTER-MIB", "scMemberDeviceID"),
        ("DES7200-CLUSTER-MIB", "scMemberRowStatus"))
)
if mibBuilder.loadTexts:
    myClusterMemberGroup.setStatus("current")

myClusterCandidateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 2, 5)
)
myClusterCandidateGroup.setObjects(
    ("DES7200-CLUSTER-MIB", "scCandidateMacAddress")
)
if mibBuilder.loadTexts:
    myClusterCandidateGroup.setStatus("current")


# Notification objects

memberStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 2, 1)
)
memberStateChangeTrap.setObjects(
    ("DES7200-CLUSTER-MIB", "scMemberOperStatus")
)
if mibBuilder.loadTexts:
    memberStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myClusterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 31, 3, 1, 1)
)
myClusterCompliance.setObjects(
      *(("DES7200-CLUSTER-MIB", "myClusterStatusGroup"),
        ("DES7200-CLUSTER-MIB", "myClusterMemberStatusGroup"),
        ("DES7200-CLUSTER-MIB", "myClusterMemberGroup"),
        ("DES7200-CLUSTER-MIB", "myClusterCandidateGroup"))
)
if mibBuilder.loadTexts:
    myClusterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-CLUSTER-MIB",
    **{"myClusterMIB": myClusterMIB,
       "myClusterMIBObjects": myClusterMIBObjects,
       "scStatus": scStatus,
       "scStatusClusterName": scStatusClusterName,
       "scStatusClusterMode": scStatusClusterMode,
       "scStatusClusterStatus": scStatusClusterStatus,
       "scStatusCommanderMacAddress": scStatusCommanderMacAddress,
       "scStatusTimeOfLastChange": scStatusTimeOfLastChange,
       "scStatusMaxNumberOfMembers": scStatusMaxNumberOfMembers,
       "scStatusLastFailureAddMember": scStatusLastFailureAddMember,
       "scMember": scMember,
       "scMemberTable": scMemberTable,
       "scMemberEntry": scMemberEntry,
       "scMemberMacAddress": scMemberMacAddress,
       "scMemberNumber": scMemberNumber,
       "scMemberOperStatus": scMemberOperStatus,
       "scMemberDeviceID": scMemberDeviceID,
       "scMemberRowStatus": scMemberRowStatus,
       "scCandidate": scCandidate,
       "scCandidateTable": scCandidateTable,
       "scCandidateEntry": scCandidateEntry,
       "scCandidateMacAddress": scCandidateMacAddress,
       "myClusterTraps": myClusterTraps,
       "memberStateChangeTrap": memberStateChangeTrap,
       "myClusterMIBConformance": myClusterMIBConformance,
       "myClusterMIBCompliances": myClusterMIBCompliances,
       "myClusterCompliance": myClusterCompliance,
       "myClusterMIBGroups": myClusterMIBGroups,
       "myClusterStatusGroup": myClusterStatusGroup,
       "myClusterMemberStatusGroup": myClusterMemberStatusGroup,
       "myClusterCandidateStatusGroup": myClusterCandidateStatusGroup,
       "myClusterMemberGroup": myClusterMemberGroup,
       "myClusterCandidateGroup": myClusterCandidateGroup}
)
