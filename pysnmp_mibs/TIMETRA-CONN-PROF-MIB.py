# SNMP MIB module (TIMETRA-CONN-PROF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-CONN-PROF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:14 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TmnxEncapVal) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TmnxEncapVal")


# MODULE-IDENTITY

timetraConnProfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 75)
)
if mibBuilder.loadTexts:
    timetraConnProfMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2011-02-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxConnProfId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxConnProfConformance_ObjectIdentity = ObjectIdentity
tmnxConnProfConformance = _TmnxConnProfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75)
)
_TmnxConnProfCompliances_ObjectIdentity = ObjectIdentity
tmnxConnProfCompliances = _TmnxConnProfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1)
)
_TmnxConnProfGroups_ObjectIdentity = ObjectIdentity
tmnxConnProfGroups = _TmnxConnProfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2)
)
_TmnxConnV9v0Groups_ObjectIdentity = ObjectIdentity
tmnxConnV9v0Groups = _TmnxConnV9v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1)
)
_TmnxConnV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxConnV14v0Groups = _TmnxConnV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 2)
)
_TmnxConnProfObjs_ObjectIdentity = ObjectIdentity
tmnxConnProfObjs = _TmnxConnProfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75)
)
_TmnxConnProfConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxConnProfConfigTimeStamps = _TmnxConnProfConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1)
)
_TmnxConnProfTblLastChanged_Type = TimeStamp
_TmnxConnProfTblLastChanged_Object = MibScalar
tmnxConnProfTblLastChanged = _TmnxConnProfTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 1),
    _TmnxConnProfTblLastChanged_Type()
)
tmnxConnProfTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfTblLastChanged.setStatus("current")
_TmnxConnProfAtmMemberTblLastChgd_Type = TimeStamp
_TmnxConnProfAtmMemberTblLastChgd_Object = MibScalar
tmnxConnProfAtmMemberTblLastChgd = _TmnxConnProfAtmMemberTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 2),
    _TmnxConnProfAtmMemberTblLastChgd_Type()
)
tmnxConnProfAtmMemberTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfAtmMemberTblLastChgd.setStatus("current")
_TmnxConnProfVlanTblLastChanged_Type = TimeStamp
_TmnxConnProfVlanTblLastChanged_Object = MibScalar
tmnxConnProfVlanTblLastChanged = _TmnxConnProfVlanTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 3),
    _TmnxConnProfVlanTblLastChanged_Type()
)
tmnxConnProfVlanTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfVlanTblLastChanged.setStatus("current")
_TmnxConnProfVlanEthTblLastChgd_Type = TimeStamp
_TmnxConnProfVlanEthTblLastChgd_Object = MibScalar
tmnxConnProfVlanEthTblLastChgd = _TmnxConnProfVlanEthTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 1, 4),
    _TmnxConnProfVlanEthTblLastChgd_Type()
)
tmnxConnProfVlanEthTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthTblLastChgd.setStatus("current")
_TmnxConnProfConfigObjs_ObjectIdentity = ObjectIdentity
tmnxConnProfConfigObjs = _TmnxConnProfConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2)
)
_TmnxConnProfTable_Object = MibTable
tmnxConnProfTable = _TmnxConnProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxConnProfTable.setStatus("current")
_TmnxConnProfEntry_Object = MibTableRow
tmnxConnProfEntry = _TmnxConnProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1)
)
tmnxConnProfEntry.setIndexNames(
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"),
)
if mibBuilder.loadTexts:
    tmnxConnProfEntry.setStatus("current")
_TmnxConnProfId_Type = TmnxConnProfId
_TmnxConnProfId_Object = MibTableColumn
tmnxConnProfId = _TmnxConnProfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 1),
    _TmnxConnProfId_Type()
)
tmnxConnProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxConnProfId.setStatus("current")
_TmnxConnProfRowStatus_Type = RowStatus
_TmnxConnProfRowStatus_Object = MibTableColumn
tmnxConnProfRowStatus = _TmnxConnProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 2),
    _TmnxConnProfRowStatus_Type()
)
tmnxConnProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfRowStatus.setStatus("current")
_TmnxConnProfLastChanged_Type = TimeStamp
_TmnxConnProfLastChanged_Object = MibTableColumn
tmnxConnProfLastChanged = _TmnxConnProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 3),
    _TmnxConnProfLastChanged_Type()
)
tmnxConnProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfLastChanged.setStatus("current")


class _TmnxConnProfDescription_Type(TItemDescription):
    """Custom type tmnxConnProfDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxConnProfDescription_Type.__name__ = "TItemDescription"
_TmnxConnProfDescription_Object = MibTableColumn
tmnxConnProfDescription = _TmnxConnProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 1, 1, 4),
    _TmnxConnProfDescription_Type()
)
tmnxConnProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfDescription.setStatus("current")
_TmnxConnProfAtmMemberTable_Object = MibTable
tmnxConnProfAtmMemberTable = _TmnxConnProfAtmMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxConnProfAtmMemberTable.setStatus("current")
_TmnxConnProfAtmMemberEntry_Object = MibTableRow
tmnxConnProfAtmMemberEntry = _TmnxConnProfAtmMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1)
)
tmnxConnProfAtmMemberEntry.setIndexNames(
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfId"),
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxConnProfAtmMemberEntry.setStatus("current")
_TmnxConnProfAtmMemberEncapValue_Type = TmnxEncapVal
_TmnxConnProfAtmMemberEncapValue_Object = MibTableColumn
tmnxConnProfAtmMemberEncapValue = _TmnxConnProfAtmMemberEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1, 1),
    _TmnxConnProfAtmMemberEncapValue_Type()
)
tmnxConnProfAtmMemberEncapValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxConnProfAtmMemberEncapValue.setStatus("current")
_TmnxConnProfAtmMemberRowStatus_Type = RowStatus
_TmnxConnProfAtmMemberRowStatus_Object = MibTableColumn
tmnxConnProfAtmMemberRowStatus = _TmnxConnProfAtmMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 2, 1, 2),
    _TmnxConnProfAtmMemberRowStatus_Type()
)
tmnxConnProfAtmMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfAtmMemberRowStatus.setStatus("current")
_TmnxConnProfVlanTable_Object = MibTable
tmnxConnProfVlanTable = _TmnxConnProfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxConnProfVlanTable.setStatus("current")
_TmnxConnProfVlanEntry_Object = MibTableRow
tmnxConnProfVlanEntry = _TmnxConnProfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 3, 1)
)
tmnxConnProfVlanEntry.setIndexNames(
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanId"),
)
if mibBuilder.loadTexts:
    tmnxConnProfVlanEntry.setStatus("current")
_TmnxConnProfVlanId_Type = TmnxConnProfId
_TmnxConnProfVlanId_Object = MibTableColumn
tmnxConnProfVlanId = _TmnxConnProfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 3, 1, 1),
    _TmnxConnProfVlanId_Type()
)
tmnxConnProfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxConnProfVlanId.setStatus("current")
_TmnxConnProfVlanRowStatus_Type = RowStatus
_TmnxConnProfVlanRowStatus_Object = MibTableColumn
tmnxConnProfVlanRowStatus = _TmnxConnProfVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 3, 1, 2),
    _TmnxConnProfVlanRowStatus_Type()
)
tmnxConnProfVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfVlanRowStatus.setStatus("current")
_TmnxConnProfVlanLastChanged_Type = TimeStamp
_TmnxConnProfVlanLastChanged_Object = MibTableColumn
tmnxConnProfVlanLastChanged = _TmnxConnProfVlanLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 3, 1, 3),
    _TmnxConnProfVlanLastChanged_Type()
)
tmnxConnProfVlanLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfVlanLastChanged.setStatus("current")


class _TmnxConnProfVlanDescription_Type(TItemDescription):
    """Custom type tmnxConnProfVlanDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxConnProfVlanDescription_Type.__name__ = "TItemDescription"
_TmnxConnProfVlanDescription_Object = MibTableColumn
tmnxConnProfVlanDescription = _TmnxConnProfVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 3, 1, 4),
    _TmnxConnProfVlanDescription_Type()
)
tmnxConnProfVlanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfVlanDescription.setStatus("current")
_TmnxConnProfVlanEthTable_Object = MibTable
tmnxConnProfVlanEthTable = _TmnxConnProfVlanEthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthTable.setStatus("current")
_TmnxConnProfVlanEthEntry_Object = MibTableRow
tmnxConnProfVlanEthEntry = _TmnxConnProfVlanEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 4, 1)
)
tmnxConnProfVlanEthEntry.setIndexNames(
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanId"),
    (0, "TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanEthRangeStart"),
)
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthEntry.setStatus("current")


class _TmnxConnProfVlanEthRangeStart_Type(Integer32):
    """Custom type tmnxConnProfVlanEthRangeStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_TmnxConnProfVlanEthRangeStart_Type.__name__ = "Integer32"
_TmnxConnProfVlanEthRangeStart_Object = MibTableColumn
tmnxConnProfVlanEthRangeStart = _TmnxConnProfVlanEthRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 4, 1, 1),
    _TmnxConnProfVlanEthRangeStart_Type()
)
tmnxConnProfVlanEthRangeStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthRangeStart.setStatus("current")
_TmnxConnProfVlanEthRowStatus_Type = RowStatus
_TmnxConnProfVlanEthRowStatus_Object = MibTableColumn
tmnxConnProfVlanEthRowStatus = _TmnxConnProfVlanEthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 4, 1, 2),
    _TmnxConnProfVlanEthRowStatus_Type()
)
tmnxConnProfVlanEthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthRowStatus.setStatus("current")


class _TmnxConnProfVlanEthRangeEnd_Type(Integer32):
    """Custom type tmnxConnProfVlanEthRangeEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_TmnxConnProfVlanEthRangeEnd_Type.__name__ = "Integer32"
_TmnxConnProfVlanEthRangeEnd_Object = MibTableColumn
tmnxConnProfVlanEthRangeEnd = _TmnxConnProfVlanEthRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 4, 1, 3),
    _TmnxConnProfVlanEthRangeEnd_Type()
)
tmnxConnProfVlanEthRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthRangeEnd.setStatus("current")
_TmnxConnProfVlanEthLastChanged_Type = TimeStamp
_TmnxConnProfVlanEthLastChanged_Object = MibTableColumn
tmnxConnProfVlanEthLastChanged = _TmnxConnProfVlanEthLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 75, 2, 4, 1, 4),
    _TmnxConnProfVlanEthLastChanged_Type()
)
tmnxConnProfVlanEthLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxConnProfVlanEthLastChanged.setStatus("current")
_TmnxConnProfNtfyPrefix_ObjectIdentity = ObjectIdentity
tmnxConnProfNtfyPrefix = _TmnxConnProfNtfyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 75)
)
_TmnxConnProfNotifications_ObjectIdentity = ObjectIdentity
tmnxConnProfNotifications = _TmnxConnProfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 75, 0)
)

# Managed Objects groups

tmnxConnProfTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 1)
)
tmnxConnProfTimeStampGroup.setObjects(
      *(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfTblLastChanged"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberTblLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxConnProfTimeStampGroup.setStatus("current")

tmnxConnProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 2)
)
tmnxConnProfGroup.setObjects(
      *(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfRowStatus"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfLastChanged"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfDescription"))
)
if mibBuilder.loadTexts:
    tmnxConnProfGroup.setStatus("current")

tmnxConnProfAtmMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 1, 3)
)
tmnxConnProfAtmMemberGroup.setObjects(
    ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberRowStatus")
)
if mibBuilder.loadTexts:
    tmnxConnProfAtmMemberGroup.setStatus("current")

tmnxConnProfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 2, 2, 1)
)
tmnxConnProfVlanGroup.setObjects(
      *(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanRowStatus"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanLastChanged"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanDescription"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanEthRangeEnd"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanEthRowStatus"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanEthLastChanged"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanEthTblLastChgd"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxConnProfVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxConnProfV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1, 1)
)
tmnxConnProfV9v0Compliance.setObjects(
      *(("TIMETRA-CONN-PROF-MIB", "tmnxConnProfTimeStampGroup"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfGroup"),
        ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfAtmMemberGroup"))
)
if mibBuilder.loadTexts:
    tmnxConnProfV9v0Compliance.setStatus(
        "current"
    )

tmnxConnProfV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 75, 1, 2)
)
tmnxConnProfV14v0Compliance.setObjects(
    ("TIMETRA-CONN-PROF-MIB", "tmnxConnProfVlanGroup")
)
if mibBuilder.loadTexts:
    tmnxConnProfV14v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CONN-PROF-MIB",
    **{"TmnxConnProfId": TmnxConnProfId,
       "timetraConnProfMIBModule": timetraConnProfMIBModule,
       "tmnxConnProfConformance": tmnxConnProfConformance,
       "tmnxConnProfCompliances": tmnxConnProfCompliances,
       "tmnxConnProfV9v0Compliance": tmnxConnProfV9v0Compliance,
       "tmnxConnProfV14v0Compliance": tmnxConnProfV14v0Compliance,
       "tmnxConnProfGroups": tmnxConnProfGroups,
       "tmnxConnV9v0Groups": tmnxConnV9v0Groups,
       "tmnxConnProfTimeStampGroup": tmnxConnProfTimeStampGroup,
       "tmnxConnProfGroup": tmnxConnProfGroup,
       "tmnxConnProfAtmMemberGroup": tmnxConnProfAtmMemberGroup,
       "tmnxConnV14v0Groups": tmnxConnV14v0Groups,
       "tmnxConnProfVlanGroup": tmnxConnProfVlanGroup,
       "tmnxConnProfObjs": tmnxConnProfObjs,
       "tmnxConnProfConfigTimeStamps": tmnxConnProfConfigTimeStamps,
       "tmnxConnProfTblLastChanged": tmnxConnProfTblLastChanged,
       "tmnxConnProfAtmMemberTblLastChgd": tmnxConnProfAtmMemberTblLastChgd,
       "tmnxConnProfVlanTblLastChanged": tmnxConnProfVlanTblLastChanged,
       "tmnxConnProfVlanEthTblLastChgd": tmnxConnProfVlanEthTblLastChgd,
       "tmnxConnProfConfigObjs": tmnxConnProfConfigObjs,
       "tmnxConnProfTable": tmnxConnProfTable,
       "tmnxConnProfEntry": tmnxConnProfEntry,
       "tmnxConnProfId": tmnxConnProfId,
       "tmnxConnProfRowStatus": tmnxConnProfRowStatus,
       "tmnxConnProfLastChanged": tmnxConnProfLastChanged,
       "tmnxConnProfDescription": tmnxConnProfDescription,
       "tmnxConnProfAtmMemberTable": tmnxConnProfAtmMemberTable,
       "tmnxConnProfAtmMemberEntry": tmnxConnProfAtmMemberEntry,
       "tmnxConnProfAtmMemberEncapValue": tmnxConnProfAtmMemberEncapValue,
       "tmnxConnProfAtmMemberRowStatus": tmnxConnProfAtmMemberRowStatus,
       "tmnxConnProfVlanTable": tmnxConnProfVlanTable,
       "tmnxConnProfVlanEntry": tmnxConnProfVlanEntry,
       "tmnxConnProfVlanId": tmnxConnProfVlanId,
       "tmnxConnProfVlanRowStatus": tmnxConnProfVlanRowStatus,
       "tmnxConnProfVlanLastChanged": tmnxConnProfVlanLastChanged,
       "tmnxConnProfVlanDescription": tmnxConnProfVlanDescription,
       "tmnxConnProfVlanEthTable": tmnxConnProfVlanEthTable,
       "tmnxConnProfVlanEthEntry": tmnxConnProfVlanEthEntry,
       "tmnxConnProfVlanEthRangeStart": tmnxConnProfVlanEthRangeStart,
       "tmnxConnProfVlanEthRowStatus": tmnxConnProfVlanEthRowStatus,
       "tmnxConnProfVlanEthRangeEnd": tmnxConnProfVlanEthRangeEnd,
       "tmnxConnProfVlanEthLastChanged": tmnxConnProfVlanEthLastChanged,
       "tmnxConnProfNtfyPrefix": tmnxConnProfNtfyPrefix,
       "tmnxConnProfNotifications": tmnxConnProfNotifications}
)
