# SNMP MIB module (FS-MMU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MMU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:14 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

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

fsMMUMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141)
)
if mibBuilder.loadTexts:
    fsMMUMIB.setRevisions(
        ("2015-06-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMmuIfVoqInTable_Object = MibTable
fsMmuIfVoqInTable = _FsMmuIfVoqInTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1)
)
if mibBuilder.loadTexts:
    fsMmuIfVoqInTable.setStatus("current")
_FsMmuIfVoqInEntry_Object = MibTableRow
fsMmuIfVoqInEntry = _FsMmuIfVoqInEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1)
)
fsMmuIfVoqInEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsInIfxId"),
    (0, "FS-MMU-MIB", "fsInQueueId"),
    (0, "FS-MMU-MIB", "fsInDevId"),
    (0, "FS-MMU-MIB", "fsInSlotId"),
    (0, "FS-MMU-MIB", "fsInPgId"),
)
if mibBuilder.loadTexts:
    fsMmuIfVoqInEntry.setStatus("current")
_FsInIfxId_Type = IfIndex
_FsInIfxId_Object = MibTableColumn
fsInIfxId = _FsInIfxId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 1),
    _FsInIfxId_Type()
)
fsInIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInIfxId.setStatus("current")
_FsInQueueId_Type = Integer32
_FsInQueueId_Object = MibTableColumn
fsInQueueId = _FsInQueueId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 2),
    _FsInQueueId_Type()
)
fsInQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInQueueId.setStatus("current")
_FsInDevId_Type = Integer32
_FsInDevId_Object = MibTableColumn
fsInDevId = _FsInDevId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 3),
    _FsInDevId_Type()
)
fsInDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInDevId.setStatus("current")
_FsInSlotId_Type = Integer32
_FsInSlotId_Object = MibTableColumn
fsInSlotId = _FsInSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 4),
    _FsInSlotId_Type()
)
fsInSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInSlotId.setStatus("current")
_FsInPgId_Type = Integer32
_FsInPgId_Object = MibTableColumn
fsInPgId = _FsInPgId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 5),
    _FsInPgId_Type()
)
fsInPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInPgId.setStatus("current")
_FsInTransmitPackets_Type = Counter64
_FsInTransmitPackets_Object = MibTableColumn
fsInTransmitPackets = _FsInTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 6),
    _FsInTransmitPackets_Type()
)
fsInTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInTransmitPackets.setStatus("current")
_FsInTransmitBytes_Type = Counter64
_FsInTransmitBytes_Object = MibTableColumn
fsInTransmitBytes = _FsInTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 7),
    _FsInTransmitBytes_Type()
)
fsInTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInTransmitBytes.setStatus("current")
_FsInDropPackets_Type = Counter64
_FsInDropPackets_Object = MibTableColumn
fsInDropPackets = _FsInDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 8),
    _FsInDropPackets_Type()
)
fsInDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInDropPackets.setStatus("current")
_FsInDropBytes_Type = Counter64
_FsInDropBytes_Object = MibTableColumn
fsInDropBytes = _FsInDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 1, 1, 9),
    _FsInDropBytes_Type()
)
fsInDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInDropBytes.setStatus("current")
_FsMmuIfVoqOutTable_Object = MibTable
fsMmuIfVoqOutTable = _FsMmuIfVoqOutTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2)
)
if mibBuilder.loadTexts:
    fsMmuIfVoqOutTable.setStatus("current")
_FsMmuIfVoqOutEntry_Object = MibTableRow
fsMmuIfVoqOutEntry = _FsMmuIfVoqOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1)
)
fsMmuIfVoqOutEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsOutIfxId"),
    (0, "FS-MMU-MIB", "fsOutQueueId"),
    (0, "FS-MMU-MIB", "fsOutDevId"),
    (0, "FS-MMU-MIB", "fsOutSlotId"),
    (0, "FS-MMU-MIB", "fsOutPgId"),
)
if mibBuilder.loadTexts:
    fsMmuIfVoqOutEntry.setStatus("current")
_FsOutIfxId_Type = IfIndex
_FsOutIfxId_Object = MibTableColumn
fsOutIfxId = _FsOutIfxId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 1),
    _FsOutIfxId_Type()
)
fsOutIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutIfxId.setStatus("current")
_FsOutQueueId_Type = Integer32
_FsOutQueueId_Object = MibTableColumn
fsOutQueueId = _FsOutQueueId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 2),
    _FsOutQueueId_Type()
)
fsOutQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutQueueId.setStatus("current")
_FsOutDevId_Type = Integer32
_FsOutDevId_Object = MibTableColumn
fsOutDevId = _FsOutDevId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 3),
    _FsOutDevId_Type()
)
fsOutDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutDevId.setStatus("current")
_FsOutSlotId_Type = Integer32
_FsOutSlotId_Object = MibTableColumn
fsOutSlotId = _FsOutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 4),
    _FsOutSlotId_Type()
)
fsOutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutSlotId.setStatus("current")
_FsOutPgId_Type = Integer32
_FsOutPgId_Object = MibTableColumn
fsOutPgId = _FsOutPgId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 5),
    _FsOutPgId_Type()
)
fsOutPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutPgId.setStatus("current")
_FsOutTransmitPackets_Type = Counter64
_FsOutTransmitPackets_Object = MibTableColumn
fsOutTransmitPackets = _FsOutTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 6),
    _FsOutTransmitPackets_Type()
)
fsOutTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutTransmitPackets.setStatus("current")
_FsOutTransmitBytes_Type = Counter64
_FsOutTransmitBytes_Object = MibTableColumn
fsOutTransmitBytes = _FsOutTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 7),
    _FsOutTransmitBytes_Type()
)
fsOutTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutTransmitBytes.setStatus("current")
_FsOutDropPackets_Type = Counter64
_FsOutDropPackets_Object = MibTableColumn
fsOutDropPackets = _FsOutDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 8),
    _FsOutDropPackets_Type()
)
fsOutDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutDropPackets.setStatus("current")
_FsOutDropBytes_Type = Counter64
_FsOutDropBytes_Object = MibTableColumn
fsOutDropBytes = _FsOutDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 2, 1, 9),
    _FsOutDropBytes_Type()
)
fsOutDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOutDropBytes.setStatus("current")
_FsMmuIfWarnTable_Object = MibTable
fsMmuIfWarnTable = _FsMmuIfWarnTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3)
)
if mibBuilder.loadTexts:
    fsMmuIfWarnTable.setStatus("current")
_FsMmuIfWarnEntry_Object = MibTableRow
fsMmuIfWarnEntry = _FsMmuIfWarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1)
)
fsMmuIfWarnEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsWarnIfxId"),
    (0, "FS-MMU-MIB", "fsWarnDevId"),
    (0, "FS-MMU-MIB", "fsWarnSlotId"),
    (0, "FS-MMU-MIB", "fsWarnPgId"),
)
if mibBuilder.loadTexts:
    fsMmuIfWarnEntry.setStatus("current")
_FsWarnIfxId_Type = IfIndex
_FsWarnIfxId_Object = MibTableColumn
fsWarnIfxId = _FsWarnIfxId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 1),
    _FsWarnIfxId_Type()
)
fsWarnIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnIfxId.setStatus("current")
_FsWarnDevId_Type = Integer32
_FsWarnDevId_Object = MibTableColumn
fsWarnDevId = _FsWarnDevId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 2),
    _FsWarnDevId_Type()
)
fsWarnDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnDevId.setStatus("current")
_FsWarnSlotId_Type = Integer32
_FsWarnSlotId_Object = MibTableColumn
fsWarnSlotId = _FsWarnSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 3),
    _FsWarnSlotId_Type()
)
fsWarnSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnSlotId.setStatus("current")
_FsWarnPgId_Type = Integer32
_FsWarnPgId_Object = MibTableColumn
fsWarnPgId = _FsWarnPgId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 4),
    _FsWarnPgId_Type()
)
fsWarnPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnPgId.setStatus("current")
_FsWarnUsedCell_Type = Integer32
_FsWarnUsedCell_Object = MibTableColumn
fsWarnUsedCell = _FsWarnUsedCell_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 5),
    _FsWarnUsedCell_Type()
)
fsWarnUsedCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnUsedCell.setStatus("current")
_FsWarnTotalCell_Type = Integer32
_FsWarnTotalCell_Object = MibTableColumn
fsWarnTotalCell = _FsWarnTotalCell_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 6),
    _FsWarnTotalCell_Type()
)
fsWarnTotalCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnTotalCell.setStatus("current")
_FsWarnLimit_Type = Integer32
_FsWarnLimit_Object = MibTableColumn
fsWarnLimit = _FsWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 7),
    _FsWarnLimit_Type()
)
fsWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnLimit.setStatus("current")
_FsWarnCount_Type = Integer32
_FsWarnCount_Object = MibTableColumn
fsWarnCount = _FsWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 3, 1, 8),
    _FsWarnCount_Type()
)
fsWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWarnCount.setStatus("current")
_FsMmuIfVoqWarnTable_Object = MibTable
fsMmuIfVoqWarnTable = _FsMmuIfVoqWarnTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4)
)
if mibBuilder.loadTexts:
    fsMmuIfVoqWarnTable.setStatus("current")
_FsMmuIfVoqWarnEntry_Object = MibTableRow
fsMmuIfVoqWarnEntry = _FsMmuIfVoqWarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1)
)
fsMmuIfVoqWarnEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsVoqWarnIfxId"),
    (0, "FS-MMU-MIB", "fsVoqWarnQueueId"),
    (0, "FS-MMU-MIB", "fsVoqWarnDevId"),
    (0, "FS-MMU-MIB", "fsVoqWarnSlotId"),
    (0, "FS-MMU-MIB", "fsVoqWarnPgId"),
)
if mibBuilder.loadTexts:
    fsMmuIfVoqWarnEntry.setStatus("current")
_FsVoqWarnIfxId_Type = IfIndex
_FsVoqWarnIfxId_Object = MibTableColumn
fsVoqWarnIfxId = _FsVoqWarnIfxId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 1),
    _FsVoqWarnIfxId_Type()
)
fsVoqWarnIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnIfxId.setStatus("current")
_FsVoqWarnQueueId_Type = Integer32
_FsVoqWarnQueueId_Object = MibTableColumn
fsVoqWarnQueueId = _FsVoqWarnQueueId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 2),
    _FsVoqWarnQueueId_Type()
)
fsVoqWarnQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnQueueId.setStatus("current")
_FsVoqWarnDevId_Type = Integer32
_FsVoqWarnDevId_Object = MibTableColumn
fsVoqWarnDevId = _FsVoqWarnDevId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 3),
    _FsVoqWarnDevId_Type()
)
fsVoqWarnDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnDevId.setStatus("current")
_FsVoqWarnSlotId_Type = Integer32
_FsVoqWarnSlotId_Object = MibTableColumn
fsVoqWarnSlotId = _FsVoqWarnSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 4),
    _FsVoqWarnSlotId_Type()
)
fsVoqWarnSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnSlotId.setStatus("current")
_FsVoqWarnPgId_Type = Integer32
_FsVoqWarnPgId_Object = MibTableColumn
fsVoqWarnPgId = _FsVoqWarnPgId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 5),
    _FsVoqWarnPgId_Type()
)
fsVoqWarnPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnPgId.setStatus("current")
_FsVoqWarnUsedcells_Type = Counter64
_FsVoqWarnUsedcells_Object = MibTableColumn
fsVoqWarnUsedcells = _FsVoqWarnUsedcells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 6),
    _FsVoqWarnUsedcells_Type()
)
fsVoqWarnUsedcells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnUsedcells.setStatus("current")
_FsVoqWarnAvailablecells_Type = Counter64
_FsVoqWarnAvailablecells_Object = MibTableColumn
fsVoqWarnAvailablecells = _FsVoqWarnAvailablecells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 7),
    _FsVoqWarnAvailablecells_Type()
)
fsVoqWarnAvailablecells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnAvailablecells.setStatus("current")
_FsVoqWarnTotalcells_Type = Counter64
_FsVoqWarnTotalcells_Object = MibTableColumn
fsVoqWarnTotalcells = _FsVoqWarnTotalcells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 8),
    _FsVoqWarnTotalcells_Type()
)
fsVoqWarnTotalcells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnTotalcells.setStatus("current")
_FsVoqWarnUsage_Type = Counter64
_FsVoqWarnUsage_Object = MibTableColumn
fsVoqWarnUsage = _FsVoqWarnUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 9),
    _FsVoqWarnUsage_Type()
)
fsVoqWarnUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnUsage.setStatus("current")
_FsVoqWarnUsagewarnlimit_Type = Counter64
_FsVoqWarnUsagewarnlimit_Object = MibTableColumn
fsVoqWarnUsagewarnlimit = _FsVoqWarnUsagewarnlimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 10),
    _FsVoqWarnUsagewarnlimit_Type()
)
fsVoqWarnUsagewarnlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnUsagewarnlimit.setStatus("current")
_FsVoqWarnUsagewarncount_Type = Counter64
_FsVoqWarnUsagewarncount_Object = MibTableColumn
fsVoqWarnUsagewarncount = _FsVoqWarnUsagewarncount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 11),
    _FsVoqWarnUsagewarncount_Type()
)
fsVoqWarnUsagewarncount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnUsagewarncount.setStatus("current")
_FsVoqWarnPeakedcells_Type = Counter64
_FsVoqWarnPeakedcells_Object = MibTableColumn
fsVoqWarnPeakedcells = _FsVoqWarnPeakedcells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 4, 1, 12),
    _FsVoqWarnPeakedcells_Type()
)
fsVoqWarnPeakedcells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVoqWarnPeakedcells.setStatus("current")
_FsMmuIfQueueSupportTable_Object = MibTable
fsMmuIfQueueSupportTable = _FsMmuIfQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5)
)
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportTable.setStatus("current")
_FsMmuIfQueueSupportEntry_Object = MibTableRow
fsMmuIfQueueSupportEntry = _FsMmuIfQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1)
)
fsMmuIfQueueSupportEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsMmuIfIndex"),
    (0, "FS-MMU-MIB", "fsMmuIfQueueIndex"),
    (0, "FS-MMU-MIB", "fsMmuIfSliceIndex"),
)
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportEntry.setStatus("current")
_FsMmuIfIndex_Type = IfIndex
_FsMmuIfIndex_Object = MibTableColumn
fsMmuIfIndex = _FsMmuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 1),
    _FsMmuIfIndex_Type()
)
fsMmuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfIndex.setStatus("current")
_FsMmuIfQueueIndex_Type = Integer32
_FsMmuIfQueueIndex_Object = MibTableColumn
fsMmuIfQueueIndex = _FsMmuIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 2),
    _FsMmuIfQueueIndex_Type()
)
fsMmuIfQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueIndex.setStatus("current")
_FsMmuIfSliceIndex_Type = Integer32
_FsMmuIfSliceIndex_Object = MibTableColumn
fsMmuIfSliceIndex = _FsMmuIfSliceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 3),
    _FsMmuIfSliceIndex_Type()
)
fsMmuIfSliceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfSliceIndex.setStatus("current")
_FsMmuIfQueueSupportUsedCells_Type = Counter64
_FsMmuIfQueueSupportUsedCells_Object = MibTableColumn
fsMmuIfQueueSupportUsedCells = _FsMmuIfQueueSupportUsedCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 4),
    _FsMmuIfQueueSupportUsedCells_Type()
)
fsMmuIfQueueSupportUsedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportUsedCells.setStatus("current")
_FsMmuIfQueueSupportAvailableCells_Type = Counter64
_FsMmuIfQueueSupportAvailableCells_Object = MibTableColumn
fsMmuIfQueueSupportAvailableCells = _FsMmuIfQueueSupportAvailableCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 5),
    _FsMmuIfQueueSupportAvailableCells_Type()
)
fsMmuIfQueueSupportAvailableCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportAvailableCells.setStatus("current")
_FsMmuIfQueueSupportTotalCells_Type = Counter64
_FsMmuIfQueueSupportTotalCells_Object = MibTableColumn
fsMmuIfQueueSupportTotalCells = _FsMmuIfQueueSupportTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 6),
    _FsMmuIfQueueSupportTotalCells_Type()
)
fsMmuIfQueueSupportTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportTotalCells.setStatus("current")
_FsMmuIfQueueSupportUsage_Type = Counter64
_FsMmuIfQueueSupportUsage_Object = MibTableColumn
fsMmuIfQueueSupportUsage = _FsMmuIfQueueSupportUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 7),
    _FsMmuIfQueueSupportUsage_Type()
)
fsMmuIfQueueSupportUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportUsage.setStatus("current")
_FsMmuIfQueueSupportUsageWarnLimit_Type = Counter64
_FsMmuIfQueueSupportUsageWarnLimit_Object = MibTableColumn
fsMmuIfQueueSupportUsageWarnLimit = _FsMmuIfQueueSupportUsageWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 8),
    _FsMmuIfQueueSupportUsageWarnLimit_Type()
)
fsMmuIfQueueSupportUsageWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportUsageWarnLimit.setStatus("current")
_FsMmuIfQueueSupportUsageWarnCount_Type = Counter64
_FsMmuIfQueueSupportUsageWarnCount_Object = MibTableColumn
fsMmuIfQueueSupportUsageWarnCount = _FsMmuIfQueueSupportUsageWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 9),
    _FsMmuIfQueueSupportUsageWarnCount_Type()
)
fsMmuIfQueueSupportUsageWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportUsageWarnCount.setStatus("current")
_FsMmuIfQueueSupportPeakedCells_Type = Counter64
_FsMmuIfQueueSupportPeakedCells_Object = MibTableColumn
fsMmuIfQueueSupportPeakedCells = _FsMmuIfQueueSupportPeakedCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 5, 1, 10),
    _FsMmuIfQueueSupportPeakedCells_Type()
)
fsMmuIfQueueSupportPeakedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfQueueSupportPeakedCells.setStatus("current")
_FsMmuIfMulticastQueueSupportTable_Object = MibTable
fsMmuIfMulticastQueueSupportTable = _FsMmuIfMulticastQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6)
)
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportTable.setStatus("current")
_FsMmuIfMulticastQueueSupportEntry_Object = MibTableRow
fsMmuIfMulticastQueueSupportEntry = _FsMmuIfMulticastQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1)
)
fsMmuIfMulticastQueueSupportEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsMmuIfIndexMulticast"),
    (0, "FS-MMU-MIB", "fsMmuIfMulticastQueueIndex"),
    (0, "FS-MMU-MIB", "fsMmuIfSliceIndexMulticast"),
)
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportEntry.setStatus("current")
_FsMmuIfIndexMulticast_Type = IfIndex
_FsMmuIfIndexMulticast_Object = MibTableColumn
fsMmuIfIndexMulticast = _FsMmuIfIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 1),
    _FsMmuIfIndexMulticast_Type()
)
fsMmuIfIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfIndexMulticast.setStatus("current")
_FsMmuIfMulticastQueueIndex_Type = Integer32
_FsMmuIfMulticastQueueIndex_Object = MibTableColumn
fsMmuIfMulticastQueueIndex = _FsMmuIfMulticastQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 2),
    _FsMmuIfMulticastQueueIndex_Type()
)
fsMmuIfMulticastQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueIndex.setStatus("current")
_FsMmuIfSliceIndexMulticast_Type = Integer32
_FsMmuIfSliceIndexMulticast_Object = MibTableColumn
fsMmuIfSliceIndexMulticast = _FsMmuIfSliceIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 3),
    _FsMmuIfSliceIndexMulticast_Type()
)
fsMmuIfSliceIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfSliceIndexMulticast.setStatus("current")
_FsMmuIfMulticastQueueSupportUsedCells_Type = Counter64
_FsMmuIfMulticastQueueSupportUsedCells_Object = MibTableColumn
fsMmuIfMulticastQueueSupportUsedCells = _FsMmuIfMulticastQueueSupportUsedCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 4),
    _FsMmuIfMulticastQueueSupportUsedCells_Type()
)
fsMmuIfMulticastQueueSupportUsedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportUsedCells.setStatus("current")
_FsMmuIfMulticastQueueSupportAvailableCells_Type = Counter64
_FsMmuIfMulticastQueueSupportAvailableCells_Object = MibTableColumn
fsMmuIfMulticastQueueSupportAvailableCells = _FsMmuIfMulticastQueueSupportAvailableCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 5),
    _FsMmuIfMulticastQueueSupportAvailableCells_Type()
)
fsMmuIfMulticastQueueSupportAvailableCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportAvailableCells.setStatus("current")
_FsMmuIfMulticastQueueSupportTotalCells_Type = Counter64
_FsMmuIfMulticastQueueSupportTotalCells_Object = MibTableColumn
fsMmuIfMulticastQueueSupportTotalCells = _FsMmuIfMulticastQueueSupportTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 6),
    _FsMmuIfMulticastQueueSupportTotalCells_Type()
)
fsMmuIfMulticastQueueSupportTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportTotalCells.setStatus("current")
_FsMmuIfMulticastQueueSupportUsage_Type = Counter64
_FsMmuIfMulticastQueueSupportUsage_Object = MibTableColumn
fsMmuIfMulticastQueueSupportUsage = _FsMmuIfMulticastQueueSupportUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 7),
    _FsMmuIfMulticastQueueSupportUsage_Type()
)
fsMmuIfMulticastQueueSupportUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportUsage.setStatus("current")
_FsMmuIfMulticastQueueSupportUsageWarnLimit_Type = Counter64
_FsMmuIfMulticastQueueSupportUsageWarnLimit_Object = MibTableColumn
fsMmuIfMulticastQueueSupportUsageWarnLimit = _FsMmuIfMulticastQueueSupportUsageWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 8),
    _FsMmuIfMulticastQueueSupportUsageWarnLimit_Type()
)
fsMmuIfMulticastQueueSupportUsageWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportUsageWarnLimit.setStatus("current")
_FsMmuIfMulticastQueueSupportUsageWarnCount_Type = Counter64
_FsMmuIfMulticastQueueSupportUsageWarnCount_Object = MibTableColumn
fsMmuIfMulticastQueueSupportUsageWarnCount = _FsMmuIfMulticastQueueSupportUsageWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 9),
    _FsMmuIfMulticastQueueSupportUsageWarnCount_Type()
)
fsMmuIfMulticastQueueSupportUsageWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportUsageWarnCount.setStatus("current")
_FsMmuIfMulticastQueueSupportPeakedCells_Type = Counter64
_FsMmuIfMulticastQueueSupportPeakedCells_Object = MibTableColumn
fsMmuIfMulticastQueueSupportPeakedCells = _FsMmuIfMulticastQueueSupportPeakedCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 6, 1, 10),
    _FsMmuIfMulticastQueueSupportPeakedCells_Type()
)
fsMmuIfMulticastQueueSupportPeakedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfMulticastQueueSupportPeakedCells.setStatus("current")
_FsMmuIfPriorityGroupSupportTable_Object = MibTable
fsMmuIfPriorityGroupSupportTable = _FsMmuIfPriorityGroupSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7)
)
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportTable.setStatus("current")
_FsMmuIfPriorityGroupSupportEntry_Object = MibTableRow
fsMmuIfPriorityGroupSupportEntry = _FsMmuIfPriorityGroupSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1)
)
fsMmuIfPriorityGroupSupportEntry.setIndexNames(
    (0, "FS-MMU-MIB", "fsMmuIfIndexPriorityGroup"),
    (0, "FS-MMU-MIB", "fsMmuIfPriorityGroupIdIndex"),
    (0, "FS-MMU-MIB", "fsMmuIfSliceIndexPriorityGroup"),
)
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportEntry.setStatus("current")
_FsMmuIfIndexPriorityGroup_Type = IfIndex
_FsMmuIfIndexPriorityGroup_Object = MibTableColumn
fsMmuIfIndexPriorityGroup = _FsMmuIfIndexPriorityGroup_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 1),
    _FsMmuIfIndexPriorityGroup_Type()
)
fsMmuIfIndexPriorityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfIndexPriorityGroup.setStatus("current")
_FsMmuIfPriorityGroupIdIndex_Type = Integer32
_FsMmuIfPriorityGroupIdIndex_Object = MibTableColumn
fsMmuIfPriorityGroupIdIndex = _FsMmuIfPriorityGroupIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 2),
    _FsMmuIfPriorityGroupIdIndex_Type()
)
fsMmuIfPriorityGroupIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupIdIndex.setStatus("current")
_FsMmuIfSliceIndexPriorityGroup_Type = Integer32
_FsMmuIfSliceIndexPriorityGroup_Object = MibTableColumn
fsMmuIfSliceIndexPriorityGroup = _FsMmuIfSliceIndexPriorityGroup_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 3),
    _FsMmuIfSliceIndexPriorityGroup_Type()
)
fsMmuIfSliceIndexPriorityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfSliceIndexPriorityGroup.setStatus("current")
_FsMmuIfPriorityGroupSupportUsedCells_Type = Counter64
_FsMmuIfPriorityGroupSupportUsedCells_Object = MibTableColumn
fsMmuIfPriorityGroupSupportUsedCells = _FsMmuIfPriorityGroupSupportUsedCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 4),
    _FsMmuIfPriorityGroupSupportUsedCells_Type()
)
fsMmuIfPriorityGroupSupportUsedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportUsedCells.setStatus("current")
_FsMmuIfPriorityGroupSupportAvailableCells_Type = Counter64
_FsMmuIfPriorityGroupSupportAvailableCells_Object = MibTableColumn
fsMmuIfPriorityGroupSupportAvailableCells = _FsMmuIfPriorityGroupSupportAvailableCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 5),
    _FsMmuIfPriorityGroupSupportAvailableCells_Type()
)
fsMmuIfPriorityGroupSupportAvailableCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportAvailableCells.setStatus("current")
_FsMmuIfPriorityGroupSupportTotalCells_Type = Counter64
_FsMmuIfPriorityGroupSupportTotalCells_Object = MibTableColumn
fsMmuIfPriorityGroupSupportTotalCells = _FsMmuIfPriorityGroupSupportTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 6),
    _FsMmuIfPriorityGroupSupportTotalCells_Type()
)
fsMmuIfPriorityGroupSupportTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportTotalCells.setStatus("current")
_FsMmuIfPriorityGroupSupportUsage_Type = Counter64
_FsMmuIfPriorityGroupSupportUsage_Object = MibTableColumn
fsMmuIfPriorityGroupSupportUsage = _FsMmuIfPriorityGroupSupportUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 7),
    _FsMmuIfPriorityGroupSupportUsage_Type()
)
fsMmuIfPriorityGroupSupportUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportUsage.setStatus("current")
_FsMmuIfPriorityGroupSupportPeakedCells_Type = Counter64
_FsMmuIfPriorityGroupSupportPeakedCells_Object = MibTableColumn
fsMmuIfPriorityGroupSupportPeakedCells = _FsMmuIfPriorityGroupSupportPeakedCells_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 8),
    _FsMmuIfPriorityGroupSupportPeakedCells_Type()
)
fsMmuIfPriorityGroupSupportPeakedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportPeakedCells.setStatus("current")
_FsMmuIfPriorityGroupSupportUsedHeadroom_Type = Counter64
_FsMmuIfPriorityGroupSupportUsedHeadroom_Object = MibTableColumn
fsMmuIfPriorityGroupSupportUsedHeadroom = _FsMmuIfPriorityGroupSupportUsedHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 9),
    _FsMmuIfPriorityGroupSupportUsedHeadroom_Type()
)
fsMmuIfPriorityGroupSupportUsedHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportUsedHeadroom.setStatus("current")
_FsMmuIfPriorityGroupSupportAvailableHeadroom_Type = Counter64
_FsMmuIfPriorityGroupSupportAvailableHeadroom_Object = MibTableColumn
fsMmuIfPriorityGroupSupportAvailableHeadroom = _FsMmuIfPriorityGroupSupportAvailableHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 10),
    _FsMmuIfPriorityGroupSupportAvailableHeadroom_Type()
)
fsMmuIfPriorityGroupSupportAvailableHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportAvailableHeadroom.setStatus("current")
_FsMmuIfPriorityGroupSupportPeakedHeadroom_Type = Counter64
_FsMmuIfPriorityGroupSupportPeakedHeadroom_Object = MibTableColumn
fsMmuIfPriorityGroupSupportPeakedHeadroom = _FsMmuIfPriorityGroupSupportPeakedHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 141, 7, 1, 11),
    _FsMmuIfPriorityGroupSupportPeakedHeadroom_Type()
)
fsMmuIfPriorityGroupSupportPeakedHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMmuIfPriorityGroupSupportPeakedHeadroom.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MMU-MIB",
    **{"fsMMUMIB": fsMMUMIB,
       "fsMmuIfVoqInTable": fsMmuIfVoqInTable,
       "fsMmuIfVoqInEntry": fsMmuIfVoqInEntry,
       "fsInIfxId": fsInIfxId,
       "fsInQueueId": fsInQueueId,
       "fsInDevId": fsInDevId,
       "fsInSlotId": fsInSlotId,
       "fsInPgId": fsInPgId,
       "fsInTransmitPackets": fsInTransmitPackets,
       "fsInTransmitBytes": fsInTransmitBytes,
       "fsInDropPackets": fsInDropPackets,
       "fsInDropBytes": fsInDropBytes,
       "fsMmuIfVoqOutTable": fsMmuIfVoqOutTable,
       "fsMmuIfVoqOutEntry": fsMmuIfVoqOutEntry,
       "fsOutIfxId": fsOutIfxId,
       "fsOutQueueId": fsOutQueueId,
       "fsOutDevId": fsOutDevId,
       "fsOutSlotId": fsOutSlotId,
       "fsOutPgId": fsOutPgId,
       "fsOutTransmitPackets": fsOutTransmitPackets,
       "fsOutTransmitBytes": fsOutTransmitBytes,
       "fsOutDropPackets": fsOutDropPackets,
       "fsOutDropBytes": fsOutDropBytes,
       "fsMmuIfWarnTable": fsMmuIfWarnTable,
       "fsMmuIfWarnEntry": fsMmuIfWarnEntry,
       "fsWarnIfxId": fsWarnIfxId,
       "fsWarnDevId": fsWarnDevId,
       "fsWarnSlotId": fsWarnSlotId,
       "fsWarnPgId": fsWarnPgId,
       "fsWarnUsedCell": fsWarnUsedCell,
       "fsWarnTotalCell": fsWarnTotalCell,
       "fsWarnLimit": fsWarnLimit,
       "fsWarnCount": fsWarnCount,
       "fsMmuIfVoqWarnTable": fsMmuIfVoqWarnTable,
       "fsMmuIfVoqWarnEntry": fsMmuIfVoqWarnEntry,
       "fsVoqWarnIfxId": fsVoqWarnIfxId,
       "fsVoqWarnQueueId": fsVoqWarnQueueId,
       "fsVoqWarnDevId": fsVoqWarnDevId,
       "fsVoqWarnSlotId": fsVoqWarnSlotId,
       "fsVoqWarnPgId": fsVoqWarnPgId,
       "fsVoqWarnUsedcells": fsVoqWarnUsedcells,
       "fsVoqWarnAvailablecells": fsVoqWarnAvailablecells,
       "fsVoqWarnTotalcells": fsVoqWarnTotalcells,
       "fsVoqWarnUsage": fsVoqWarnUsage,
       "fsVoqWarnUsagewarnlimit": fsVoqWarnUsagewarnlimit,
       "fsVoqWarnUsagewarncount": fsVoqWarnUsagewarncount,
       "fsVoqWarnPeakedcells": fsVoqWarnPeakedcells,
       "fsMmuIfQueueSupportTable": fsMmuIfQueueSupportTable,
       "fsMmuIfQueueSupportEntry": fsMmuIfQueueSupportEntry,
       "fsMmuIfIndex": fsMmuIfIndex,
       "fsMmuIfQueueIndex": fsMmuIfQueueIndex,
       "fsMmuIfSliceIndex": fsMmuIfSliceIndex,
       "fsMmuIfQueueSupportUsedCells": fsMmuIfQueueSupportUsedCells,
       "fsMmuIfQueueSupportAvailableCells": fsMmuIfQueueSupportAvailableCells,
       "fsMmuIfQueueSupportTotalCells": fsMmuIfQueueSupportTotalCells,
       "fsMmuIfQueueSupportUsage": fsMmuIfQueueSupportUsage,
       "fsMmuIfQueueSupportUsageWarnLimit": fsMmuIfQueueSupportUsageWarnLimit,
       "fsMmuIfQueueSupportUsageWarnCount": fsMmuIfQueueSupportUsageWarnCount,
       "fsMmuIfQueueSupportPeakedCells": fsMmuIfQueueSupportPeakedCells,
       "fsMmuIfMulticastQueueSupportTable": fsMmuIfMulticastQueueSupportTable,
       "fsMmuIfMulticastQueueSupportEntry": fsMmuIfMulticastQueueSupportEntry,
       "fsMmuIfIndexMulticast": fsMmuIfIndexMulticast,
       "fsMmuIfMulticastQueueIndex": fsMmuIfMulticastQueueIndex,
       "fsMmuIfSliceIndexMulticast": fsMmuIfSliceIndexMulticast,
       "fsMmuIfMulticastQueueSupportUsedCells": fsMmuIfMulticastQueueSupportUsedCells,
       "fsMmuIfMulticastQueueSupportAvailableCells": fsMmuIfMulticastQueueSupportAvailableCells,
       "fsMmuIfMulticastQueueSupportTotalCells": fsMmuIfMulticastQueueSupportTotalCells,
       "fsMmuIfMulticastQueueSupportUsage": fsMmuIfMulticastQueueSupportUsage,
       "fsMmuIfMulticastQueueSupportUsageWarnLimit": fsMmuIfMulticastQueueSupportUsageWarnLimit,
       "fsMmuIfMulticastQueueSupportUsageWarnCount": fsMmuIfMulticastQueueSupportUsageWarnCount,
       "fsMmuIfMulticastQueueSupportPeakedCells": fsMmuIfMulticastQueueSupportPeakedCells,
       "fsMmuIfPriorityGroupSupportTable": fsMmuIfPriorityGroupSupportTable,
       "fsMmuIfPriorityGroupSupportEntry": fsMmuIfPriorityGroupSupportEntry,
       "fsMmuIfIndexPriorityGroup": fsMmuIfIndexPriorityGroup,
       "fsMmuIfPriorityGroupIdIndex": fsMmuIfPriorityGroupIdIndex,
       "fsMmuIfSliceIndexPriorityGroup": fsMmuIfSliceIndexPriorityGroup,
       "fsMmuIfPriorityGroupSupportUsedCells": fsMmuIfPriorityGroupSupportUsedCells,
       "fsMmuIfPriorityGroupSupportAvailableCells": fsMmuIfPriorityGroupSupportAvailableCells,
       "fsMmuIfPriorityGroupSupportTotalCells": fsMmuIfPriorityGroupSupportTotalCells,
       "fsMmuIfPriorityGroupSupportUsage": fsMmuIfPriorityGroupSupportUsage,
       "fsMmuIfPriorityGroupSupportPeakedCells": fsMmuIfPriorityGroupSupportPeakedCells,
       "fsMmuIfPriorityGroupSupportUsedHeadroom": fsMmuIfPriorityGroupSupportUsedHeadroom,
       "fsMmuIfPriorityGroupSupportAvailableHeadroom": fsMmuIfPriorityGroupSupportAvailableHeadroom,
       "fsMmuIfPriorityGroupSupportPeakedHeadroom": fsMmuIfPriorityGroupSupportPeakedHeadroom}
)
