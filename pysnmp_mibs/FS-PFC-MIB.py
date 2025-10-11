# SNMP MIB module (FS-PFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PFC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:44 2025
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsPfcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157)
)
if mibBuilder.loadTexts:
    fsPfcMIB.setRevisions(
        ("2017-12-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPfcCounterMIBObjects_ObjectIdentity = ObjectIdentity
fsPfcCounterMIBObjects = _FsPfcCounterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1)
)
_FsPfcIfPriorityCounterTable_Object = MibTable
fsPfcIfPriorityCounterTable = _FsPfcIfPriorityCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1)
)
if mibBuilder.loadTexts:
    fsPfcIfPriorityCounterTable.setStatus("current")
_FsPfcIfPriorityCounterEntry_Object = MibTableRow
fsPfcIfPriorityCounterEntry = _FsPfcIfPriorityCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1)
)
fsPfcIfPriorityCounterEntry.setIndexNames(
    (0, "FS-PFC-MIB", "fsIfIndex"),
    (0, "FS-PFC-MIB", "fsPfcPriority"),
)
if mibBuilder.loadTexts:
    fsPfcIfPriorityCounterEntry.setStatus("current")
_FsIfIndex_Type = IfIndex
_FsIfIndex_Object = MibTableColumn
fsIfIndex = _FsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 1),
    _FsIfIndex_Type()
)
fsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIndex.setStatus("current")
_FsPfcPriority_Type = Integer32
_FsPfcPriority_Object = MibTableColumn
fsPfcPriority = _FsPfcPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 2),
    _FsPfcPriority_Type()
)
fsPfcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcPriority.setStatus("current")
_FsPfcRequests_Type = Counter64
_FsPfcRequests_Object = MibTableColumn
fsPfcRequests = _FsPfcRequests_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 3),
    _FsPfcRequests_Type()
)
fsPfcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequests.setStatus("current")
_FsPfcRequestsRate_Type = Counter64
_FsPfcRequestsRate_Object = MibTableColumn
fsPfcRequestsRate = _FsPfcRequestsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 4),
    _FsPfcRequestsRate_Type()
)
fsPfcRequestsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate.setStatus("current")
_FsPfcRequestsRate1st_Type = Counter64
_FsPfcRequestsRate1st_Object = MibTableColumn
fsPfcRequestsRate1st = _FsPfcRequestsRate1st_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 5),
    _FsPfcRequestsRate1st_Type()
)
fsPfcRequestsRate1st.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate1st.setStatus("current")
_FsPfcRequestsRate1stTime_Type = DisplayString
_FsPfcRequestsRate1stTime_Object = MibTableColumn
fsPfcRequestsRate1stTime = _FsPfcRequestsRate1stTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 6),
    _FsPfcRequestsRate1stTime_Type()
)
fsPfcRequestsRate1stTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate1stTime.setStatus("current")
_FsPfcRequestsRate2nd_Type = Counter64
_FsPfcRequestsRate2nd_Object = MibTableColumn
fsPfcRequestsRate2nd = _FsPfcRequestsRate2nd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 7),
    _FsPfcRequestsRate2nd_Type()
)
fsPfcRequestsRate2nd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate2nd.setStatus("current")
_FsPfcRequestsRate2ndTime_Type = DisplayString
_FsPfcRequestsRate2ndTime_Object = MibTableColumn
fsPfcRequestsRate2ndTime = _FsPfcRequestsRate2ndTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 8),
    _FsPfcRequestsRate2ndTime_Type()
)
fsPfcRequestsRate2ndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate2ndTime.setStatus("current")
_FsPfcRequestsRate3rd_Type = Counter64
_FsPfcRequestsRate3rd_Object = MibTableColumn
fsPfcRequestsRate3rd = _FsPfcRequestsRate3rd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 9),
    _FsPfcRequestsRate3rd_Type()
)
fsPfcRequestsRate3rd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate3rd.setStatus("current")
_FsPfcRequestsRate3rdTime_Type = DisplayString
_FsPfcRequestsRate3rdTime_Object = MibTableColumn
fsPfcRequestsRate3rdTime = _FsPfcRequestsRate3rdTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 10),
    _FsPfcRequestsRate3rdTime_Type()
)
fsPfcRequestsRate3rdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcRequestsRate3rdTime.setStatus("current")
_FsPfcIndications_Type = Counter64
_FsPfcIndications_Object = MibTableColumn
fsPfcIndications = _FsPfcIndications_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 11),
    _FsPfcIndications_Type()
)
fsPfcIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndications.setStatus("current")
_FsPfcIndicationsRate_Type = Counter64
_FsPfcIndicationsRate_Object = MibTableColumn
fsPfcIndicationsRate = _FsPfcIndicationsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 12),
    _FsPfcIndicationsRate_Type()
)
fsPfcIndicationsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate.setStatus("current")
_FsPfcIndicationsRate1st_Type = Counter64
_FsPfcIndicationsRate1st_Object = MibTableColumn
fsPfcIndicationsRate1st = _FsPfcIndicationsRate1st_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 13),
    _FsPfcIndicationsRate1st_Type()
)
fsPfcIndicationsRate1st.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate1st.setStatus("current")
_FsPfcIndicationsRate1stTime_Type = DisplayString
_FsPfcIndicationsRate1stTime_Object = MibTableColumn
fsPfcIndicationsRate1stTime = _FsPfcIndicationsRate1stTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 14),
    _FsPfcIndicationsRate1stTime_Type()
)
fsPfcIndicationsRate1stTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate1stTime.setStatus("current")
_FsPfcIndicationsRate2nd_Type = Counter64
_FsPfcIndicationsRate2nd_Object = MibTableColumn
fsPfcIndicationsRate2nd = _FsPfcIndicationsRate2nd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 15),
    _FsPfcIndicationsRate2nd_Type()
)
fsPfcIndicationsRate2nd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate2nd.setStatus("current")
_FsPfcIndicationsRate2ndTime_Type = DisplayString
_FsPfcIndicationsRate2ndTime_Object = MibTableColumn
fsPfcIndicationsRate2ndTime = _FsPfcIndicationsRate2ndTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 16),
    _FsPfcIndicationsRate2ndTime_Type()
)
fsPfcIndicationsRate2ndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate2ndTime.setStatus("current")
_FsPfcIndicationsRate3rd_Type = Counter64
_FsPfcIndicationsRate3rd_Object = MibTableColumn
fsPfcIndicationsRate3rd = _FsPfcIndicationsRate3rd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 17),
    _FsPfcIndicationsRate3rd_Type()
)
fsPfcIndicationsRate3rd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate3rd.setStatus("current")
_FsPfcIndicationsRate3rdTime_Type = DisplayString
_FsPfcIndicationsRate3rdTime_Object = MibTableColumn
fsPfcIndicationsRate3rdTime = _FsPfcIndicationsRate3rdTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 1, 1, 1, 18),
    _FsPfcIndicationsRate3rdTime_Type()
)
fsPfcIndicationsRate3rdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPfcIndicationsRate3rdTime.setStatus("current")
_FsPfcMIBConformance_ObjectIdentity = ObjectIdentity
fsPfcMIBConformance = _FsPfcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 2)
)

# Managed Objects groups

fsPfcIfPriorityCounterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 157, 2, 1)
)
fsPfcIfPriorityCounterMIBGroup.setObjects(
      *(("FS-PFC-MIB", "fsIfIndex"),
        ("FS-PFC-MIB", "fsPfcPriority"),
        ("FS-PFC-MIB", "fsPfcRequests"),
        ("FS-PFC-MIB", "fsPfcRequestsRate"),
        ("FS-PFC-MIB", "fsPfcRequestsRate1st"),
        ("FS-PFC-MIB", "fsPfcRequestsRate1stTime"),
        ("FS-PFC-MIB", "fsPfcRequestsRate2nd"),
        ("FS-PFC-MIB", "fsPfcRequestsRate2ndTime"),
        ("FS-PFC-MIB", "fsPfcRequestsRate3rd"),
        ("FS-PFC-MIB", "fsPfcRequestsRate3rdTime"),
        ("FS-PFC-MIB", "fsPfcIndications"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate1st"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate1stTime"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate2nd"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate2ndTime"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate3rd"),
        ("FS-PFC-MIB", "fsPfcIndicationsRate3rdTime"))
)
if mibBuilder.loadTexts:
    fsPfcIfPriorityCounterMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PFC-MIB",
    **{"fsPfcMIB": fsPfcMIB,
       "fsPfcCounterMIBObjects": fsPfcCounterMIBObjects,
       "fsPfcIfPriorityCounterTable": fsPfcIfPriorityCounterTable,
       "fsPfcIfPriorityCounterEntry": fsPfcIfPriorityCounterEntry,
       "fsIfIndex": fsIfIndex,
       "fsPfcPriority": fsPfcPriority,
       "fsPfcRequests": fsPfcRequests,
       "fsPfcRequestsRate": fsPfcRequestsRate,
       "fsPfcRequestsRate1st": fsPfcRequestsRate1st,
       "fsPfcRequestsRate1stTime": fsPfcRequestsRate1stTime,
       "fsPfcRequestsRate2nd": fsPfcRequestsRate2nd,
       "fsPfcRequestsRate2ndTime": fsPfcRequestsRate2ndTime,
       "fsPfcRequestsRate3rd": fsPfcRequestsRate3rd,
       "fsPfcRequestsRate3rdTime": fsPfcRequestsRate3rdTime,
       "fsPfcIndications": fsPfcIndications,
       "fsPfcIndicationsRate": fsPfcIndicationsRate,
       "fsPfcIndicationsRate1st": fsPfcIndicationsRate1st,
       "fsPfcIndicationsRate1stTime": fsPfcIndicationsRate1stTime,
       "fsPfcIndicationsRate2nd": fsPfcIndicationsRate2nd,
       "fsPfcIndicationsRate2ndTime": fsPfcIndicationsRate2ndTime,
       "fsPfcIndicationsRate3rd": fsPfcIndicationsRate3rd,
       "fsPfcIndicationsRate3rdTime": fsPfcIndicationsRate3rdTime,
       "fsPfcMIBConformance": fsPfcMIBConformance,
       "fsPfcIfPriorityCounterMIBGroup": fsPfcIfPriorityCounterMIBGroup}
)
