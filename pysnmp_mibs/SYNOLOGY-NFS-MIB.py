# SNMP MIB module (SYNOLOGY-NFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-NFS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:25 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nfs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 107)
)
if mibBuilder.loadTexts:
    nfs.setRevisions(
        ("2018-08-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_NfsTable_Object = MibTable
nfsTable = _NfsTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1)
)
if mibBuilder.loadTexts:
    nfsTable.setStatus("current")
_NfsEntry_Object = MibTableRow
nfsEntry = _NfsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1)
)
nfsEntry.setIndexNames(
    (0, "SYNOLOGY-NFS-MIB", "nfsIndex"),
)
if mibBuilder.loadTexts:
    nfsEntry.setStatus("current")


class _NfsIndex_Type(Integer32):
    """Custom type nfsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NfsIndex_Type.__name__ = "Integer32"
_NfsIndex_Object = MibTableColumn
nfsIndex = _NfsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 1),
    _NfsIndex_Type()
)
nfsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nfsIndex.setStatus("current")
_NfsName_Type = DisplayString
_NfsName_Object = MibTableColumn
nfsName = _NfsName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 2),
    _NfsName_Type()
)
nfsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsName.setStatus("current")
_NfsTotalMaxLatency_Type = Integer32
_NfsTotalMaxLatency_Object = MibTableColumn
nfsTotalMaxLatency = _NfsTotalMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 3),
    _NfsTotalMaxLatency_Type()
)
nfsTotalMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTotalMaxLatency.setStatus("current")
_NfsReadMaxLatency_Type = Integer32
_NfsReadMaxLatency_Object = MibTableColumn
nfsReadMaxLatency = _NfsReadMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 4),
    _NfsReadMaxLatency_Type()
)
nfsReadMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsReadMaxLatency.setStatus("current")
_NfsWriteMaxLatency_Type = Integer32
_NfsWriteMaxLatency_Object = MibTableColumn
nfsWriteMaxLatency = _NfsWriteMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 5),
    _NfsWriteMaxLatency_Type()
)
nfsWriteMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsWriteMaxLatency.setStatus("current")
_NfsTotalOPS_Type = Counter64
_NfsTotalOPS_Object = MibTableColumn
nfsTotalOPS = _NfsTotalOPS_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 6),
    _NfsTotalOPS_Type()
)
nfsTotalOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsTotalOPS.setStatus("current")
_NfsReadOPS_Type = Counter64
_NfsReadOPS_Object = MibTableColumn
nfsReadOPS = _NfsReadOPS_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 7),
    _NfsReadOPS_Type()
)
nfsReadOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsReadOPS.setStatus("current")
_NfsWriteOPS_Type = Counter64
_NfsWriteOPS_Object = MibTableColumn
nfsWriteOPS = _NfsWriteOPS_Object(
    (1, 3, 6, 1, 4, 1, 6574, 107, 1, 1, 8),
    _NfsWriteOPS_Type()
)
nfsWriteOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsWriteOPS.setStatus("current")
_NfsConformance_ObjectIdentity = ObjectIdentity
nfsConformance = _NfsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 107, 2)
)
_NfsCompliances_ObjectIdentity = ObjectIdentity
nfsCompliances = _NfsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 107, 2, 1)
)
_NfsGroups_ObjectIdentity = ObjectIdentity
nfsGroups = _NfsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 107, 2, 2)
)

# Managed Objects groups

nfsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 107, 2, 2, 1)
)
nfsGroup.setObjects(
      *(("SYNOLOGY-NFS-MIB", "nfsName"),
        ("SYNOLOGY-NFS-MIB", "nfsTotalMaxLatency"),
        ("SYNOLOGY-NFS-MIB", "nfsReadMaxLatency"),
        ("SYNOLOGY-NFS-MIB", "nfsWriteMaxLatency"),
        ("SYNOLOGY-NFS-MIB", "nfsTotalOPS"),
        ("SYNOLOGY-NFS-MIB", "nfsReadOPS"),
        ("SYNOLOGY-NFS-MIB", "nfsWriteOPS"))
)
if mibBuilder.loadTexts:
    nfsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nfsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 107, 2, 1, 1)
)
nfsCompliance.setObjects(
    ("SYNOLOGY-NFS-MIB", "nfsGroup")
)
if mibBuilder.loadTexts:
    nfsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-NFS-MIB",
    **{"synology": synology,
       "nfs": nfs,
       "nfsTable": nfsTable,
       "nfsEntry": nfsEntry,
       "nfsIndex": nfsIndex,
       "nfsName": nfsName,
       "nfsTotalMaxLatency": nfsTotalMaxLatency,
       "nfsReadMaxLatency": nfsReadMaxLatency,
       "nfsWriteMaxLatency": nfsWriteMaxLatency,
       "nfsTotalOPS": nfsTotalOPS,
       "nfsReadOPS": nfsReadOPS,
       "nfsWriteOPS": nfsWriteOPS,
       "nfsConformance": nfsConformance,
       "nfsCompliances": nfsCompliances,
       "nfsCompliance": nfsCompliance,
       "nfsGroups": nfsGroups,
       "nfsGroup": nfsGroup}
)
