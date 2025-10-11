# SNMP MIB module (CRESTRON-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/crestron/CRESTRON-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:47 2025
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

(Digital,
 crestronCommon) = mibBuilder.importSymbols(
    "CRESTRON-ROOT-MIB",
    "Digital",
    "crestronCommon")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

crestronMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2)
)
if mibBuilder.loadTexts:
    crestronMonitor.setRevisions(
        ("2003-08-18 12:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrestronMonMIBVersion_Type = Integer32
_CrestronMonMIBVersion_Object = MibScalar
crestronMonMIBVersion = _CrestronMonMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 1),
    _CrestronMonMIBVersion_Type()
)
crestronMonMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronMonMIBVersion.setStatus("current")
_CrestronMonAdmin_ObjectIdentity = ObjectIdentity
crestronMonAdmin = _CrestronMonAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 2)
)
_CrestronMonNotifications_ObjectIdentity = ObjectIdentity
crestronMonNotifications = _CrestronMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 3)
)
_CrestronMonTrapMsg_Type = DisplayString
_CrestronMonTrapMsg_Object = MibScalar
crestronMonTrapMsg = _CrestronMonTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 3, 1),
    _CrestronMonTrapMsg_Type()
)
crestronMonTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crestronMonTrapMsg.setStatus("current")
_CrestronMonObjects_ObjectIdentity = ObjectIdentity
crestronMonObjects = _CrestronMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4)
)
_CrestronMonProbes_ObjectIdentity = ObjectIdentity
crestronMonProbes = _CrestronMonProbes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4)
)
_CrestronMonProbesCnt_Type = Counter32
_CrestronMonProbesCnt_Object = MibScalar
crestronMonProbesCnt = _CrestronMonProbesCnt_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 1),
    _CrestronMonProbesCnt_Type()
)
crestronMonProbesCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronMonProbesCnt.setStatus("current")
_CrestronMonProbesTable_Object = MibTable
crestronMonProbesTable = _CrestronMonProbesTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    crestronMonProbesTable.setStatus("current")
_CrestronMonProbesEntry_Object = MibTableRow
crestronMonProbesEntry = _CrestronMonProbesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1)
)
crestronMonProbesEntry.setIndexNames(
    (0, "CRESTRON-MONITOR-MIB", "crestronMonProbeOid"),
)
if mibBuilder.loadTexts:
    crestronMonProbesEntry.setStatus("current")
_CrestronMonProbeOid_Type = ObjectIdentifier
_CrestronMonProbeOid_Object = MibTableColumn
crestronMonProbeOid = _CrestronMonProbeOid_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 1),
    _CrestronMonProbeOid_Type()
)
crestronMonProbeOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeOid.setStatus("current")
_CrestronMonProbeOidLen_Type = Integer32
_CrestronMonProbeOidLen_Object = MibTableColumn
crestronMonProbeOidLen = _CrestronMonProbeOidLen_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 2),
    _CrestronMonProbeOidLen_Type()
)
crestronMonProbeOidLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeOidLen.setStatus("current")
_CrestronMonProbeDesc_Type = DisplayString
_CrestronMonProbeDesc_Object = MibTableColumn
crestronMonProbeDesc = _CrestronMonProbeDesc_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 3),
    _CrestronMonProbeDesc_Type()
)
crestronMonProbeDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeDesc.setStatus("current")
_CrestronMonProbeStringVal_Type = DisplayString
_CrestronMonProbeStringVal_Object = MibTableColumn
crestronMonProbeStringVal = _CrestronMonProbeStringVal_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 4),
    _CrestronMonProbeStringVal_Type()
)
crestronMonProbeStringVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeStringVal.setStatus("current")
_CrestronMonProbeNumVal_Type = Integer32
_CrestronMonProbeNumVal_Object = MibTableColumn
crestronMonProbeNumVal = _CrestronMonProbeNumVal_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 5),
    _CrestronMonProbeNumVal_Type()
)
crestronMonProbeNumVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeNumVal.setStatus("current")
_CrestronMonProbeMatched_Type = Digital
_CrestronMonProbeMatched_Object = MibTableColumn
crestronMonProbeMatched = _CrestronMonProbeMatched_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 6),
    _CrestronMonProbeMatched_Type()
)
crestronMonProbeMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronMonProbeMatched.setStatus("current")
_CrestronMonProbeComparator_Type = DisplayString
_CrestronMonProbeComparator_Object = MibTableColumn
crestronMonProbeComparator = _CrestronMonProbeComparator_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 7),
    _CrestronMonProbeComparator_Type()
)
crestronMonProbeComparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeComparator.setStatus("current")
_CrestronMonProbeStorageType_Type = StorageType
_CrestronMonProbeStorageType_Object = MibTableColumn
crestronMonProbeStorageType = _CrestronMonProbeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 8),
    _CrestronMonProbeStorageType_Type()
)
crestronMonProbeStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeStorageType.setStatus("current")
_CrestronMonProbeRowStatus_Type = RowStatus
_CrestronMonProbeRowStatus_Object = MibTableColumn
crestronMonProbeRowStatus = _CrestronMonProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 4, 4, 2, 1, 9),
    _CrestronMonProbeRowStatus_Type()
)
crestronMonProbeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronMonProbeRowStatus.setStatus("current")
_CrestronMonConformance_ObjectIdentity = ObjectIdentity
crestronMonConformance = _CrestronMonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 5)
)
_CrestronMonCompliances_ObjectIdentity = ObjectIdentity
crestronMonCompliances = _CrestronMonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 5, 1)
)
_CrestronMonGroups_ObjectIdentity = ObjectIdentity
crestronMonGroups = _CrestronMonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 5, 2)
)

# Managed Objects groups

crestronMonAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 5, 2, 1)
)
crestronMonAllObjects.setObjects(
      *(("CRESTRON-MONITOR-MIB", "crestronMonMIBVersion"),
        ("CRESTRON-MONITOR-MIB", "crestronMonTrapMsg"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbesCnt"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeOid"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeStorageType"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeRowStatus"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeDesc"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeOidLen"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeStringVal"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeNumVal"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeMatched"),
        ("CRESTRON-MONITOR-MIB", "crestronMonProbeComparator"))
)
if mibBuilder.loadTexts:
    crestronMonAllObjects.setStatus("current")


# Notification objects

crestronMonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 3, 2)
)
crestronMonTrap.setObjects(
    ("CRESTRON-MONITOR-MIB", "crestronMonTrapMsg")
)
if mibBuilder.loadTexts:
    crestronMonTrap.setStatus(
        "current"
    )


# Notifications groups

crestronMonAllTraps = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3212, 6, 2, 5, 2, 6)
)
crestronMonAllTraps.setObjects(
    ("CRESTRON-MONITOR-MIB", "crestronMonTrap")
)
if mibBuilder.loadTexts:
    crestronMonAllTraps.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRESTRON-MONITOR-MIB",
    **{"crestronMonitor": crestronMonitor,
       "crestronMonMIBVersion": crestronMonMIBVersion,
       "crestronMonAdmin": crestronMonAdmin,
       "crestronMonNotifications": crestronMonNotifications,
       "crestronMonTrapMsg": crestronMonTrapMsg,
       "crestronMonTrap": crestronMonTrap,
       "crestronMonObjects": crestronMonObjects,
       "crestronMonProbes": crestronMonProbes,
       "crestronMonProbesCnt": crestronMonProbesCnt,
       "crestronMonProbesTable": crestronMonProbesTable,
       "crestronMonProbesEntry": crestronMonProbesEntry,
       "crestronMonProbeOid": crestronMonProbeOid,
       "crestronMonProbeOidLen": crestronMonProbeOidLen,
       "crestronMonProbeDesc": crestronMonProbeDesc,
       "crestronMonProbeStringVal": crestronMonProbeStringVal,
       "crestronMonProbeNumVal": crestronMonProbeNumVal,
       "crestronMonProbeMatched": crestronMonProbeMatched,
       "crestronMonProbeComparator": crestronMonProbeComparator,
       "crestronMonProbeStorageType": crestronMonProbeStorageType,
       "crestronMonProbeRowStatus": crestronMonProbeRowStatus,
       "crestronMonConformance": crestronMonConformance,
       "crestronMonCompliances": crestronMonCompliances,
       "crestronMonGroups": crestronMonGroups,
       "crestronMonAllObjects": crestronMonAllObjects,
       "crestronMonAllTraps": crestronMonAllTraps}
)
