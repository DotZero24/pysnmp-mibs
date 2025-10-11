# SNMP MIB module (SYNOLOGY-ISCSILUN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-ISCSILUN-MIB
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

synologyiSCSILUN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 104)
)
if mibBuilder.loadTexts:
    synologyiSCSILUN.setRevisions(
        ("2020-08-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_ISCSILUNTable_Object = MibTable
iSCSILUNTable = _ISCSILUNTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1)
)
if mibBuilder.loadTexts:
    iSCSILUNTable.setStatus("current")
_ISCSILUNEntry_Object = MibTableRow
iSCSILUNEntry = _ISCSILUNEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1)
)
iSCSILUNEntry.setIndexNames(
    (0, "SYNOLOGY-ISCSILUN-MIB", "iSCSILUNInfoIndex"),
)
if mibBuilder.loadTexts:
    iSCSILUNEntry.setStatus("current")


class _ISCSILUNInfoIndex_Type(Integer32):
    """Custom type iSCSILUNInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ISCSILUNInfoIndex_Type.__name__ = "Integer32"
_ISCSILUNInfoIndex_Object = MibTableColumn
iSCSILUNInfoIndex = _ISCSILUNInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 1),
    _ISCSILUNInfoIndex_Type()
)
iSCSILUNInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iSCSILUNInfoIndex.setStatus("current")


class _ISCSILUNUUID_Type(OctetString):
    """Custom type iSCSILUNUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ISCSILUNUUID_Type.__name__ = "OctetString"
_ISCSILUNUUID_Object = MibTableColumn
iSCSILUNUUID = _ISCSILUNUUID_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 2),
    _ISCSILUNUUID_Type()
)
iSCSILUNUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNUUID.setStatus("current")


class _ISCSILUNName_Type(OctetString):
    """Custom type iSCSILUNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ISCSILUNName_Type.__name__ = "OctetString"
_ISCSILUNName_Object = MibTableColumn
iSCSILUNName = _ISCSILUNName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 3),
    _ISCSILUNName_Type()
)
iSCSILUNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNName.setStatus("current")
_ISCSILUNThroughputReadHigh_Type = Integer32
_ISCSILUNThroughputReadHigh_Object = MibTableColumn
iSCSILUNThroughputReadHigh = _ISCSILUNThroughputReadHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 4),
    _ISCSILUNThroughputReadHigh_Type()
)
iSCSILUNThroughputReadHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNThroughputReadHigh.setStatus("current")
_ISCSILUNThroughputReadLow_Type = Integer32
_ISCSILUNThroughputReadLow_Object = MibTableColumn
iSCSILUNThroughputReadLow = _ISCSILUNThroughputReadLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 5),
    _ISCSILUNThroughputReadLow_Type()
)
iSCSILUNThroughputReadLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNThroughputReadLow.setStatus("current")
_ISCSILUNThroughputWriteHigh_Type = Integer32
_ISCSILUNThroughputWriteHigh_Object = MibTableColumn
iSCSILUNThroughputWriteHigh = _ISCSILUNThroughputWriteHigh_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 6),
    _ISCSILUNThroughputWriteHigh_Type()
)
iSCSILUNThroughputWriteHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNThroughputWriteHigh.setStatus("current")
_ISCSILUNThroughputWriteLow_Type = Integer32
_ISCSILUNThroughputWriteLow_Object = MibTableColumn
iSCSILUNThroughputWriteLow = _ISCSILUNThroughputWriteLow_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 7),
    _ISCSILUNThroughputWriteLow_Type()
)
iSCSILUNThroughputWriteLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNThroughputWriteLow.setStatus("current")
_ISCSILUNIopsRead_Type = Integer32
_ISCSILUNIopsRead_Object = MibTableColumn
iSCSILUNIopsRead = _ISCSILUNIopsRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 8),
    _ISCSILUNIopsRead_Type()
)
iSCSILUNIopsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNIopsRead.setStatus("current")
_ISCSILUNIopsWrite_Type = Integer32
_ISCSILUNIopsWrite_Object = MibTableColumn
iSCSILUNIopsWrite = _ISCSILUNIopsWrite_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 9),
    _ISCSILUNIopsWrite_Type()
)
iSCSILUNIopsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNIopsWrite.setStatus("current")
_ISCSILUNDiskLatencyRead_Type = Integer32
_ISCSILUNDiskLatencyRead_Object = MibTableColumn
iSCSILUNDiskLatencyRead = _ISCSILUNDiskLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 10),
    _ISCSILUNDiskLatencyRead_Type()
)
iSCSILUNDiskLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNDiskLatencyRead.setStatus("current")
_ISCSILUNDiskLatencyWrite_Type = Integer32
_ISCSILUNDiskLatencyWrite_Object = MibTableColumn
iSCSILUNDiskLatencyWrite = _ISCSILUNDiskLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 11),
    _ISCSILUNDiskLatencyWrite_Type()
)
iSCSILUNDiskLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNDiskLatencyWrite.setStatus("current")
_ISCSILUNNetworkLatencyTx_Type = Integer32
_ISCSILUNNetworkLatencyTx_Object = MibTableColumn
iSCSILUNNetworkLatencyTx = _ISCSILUNNetworkLatencyTx_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 12),
    _ISCSILUNNetworkLatencyTx_Type()
)
iSCSILUNNetworkLatencyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNNetworkLatencyTx.setStatus("current")
_ISCSILUNNetworkLatencyRx_Type = Integer32
_ISCSILUNNetworkLatencyRx_Object = MibTableColumn
iSCSILUNNetworkLatencyRx = _ISCSILUNNetworkLatencyRx_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 13),
    _ISCSILUNNetworkLatencyRx_Type()
)
iSCSILUNNetworkLatencyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNNetworkLatencyRx.setStatus("current")
_ISCSILUNIoSizeRead_Type = Integer32
_ISCSILUNIoSizeRead_Object = MibTableColumn
iSCSILUNIoSizeRead = _ISCSILUNIoSizeRead_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 14),
    _ISCSILUNIoSizeRead_Type()
)
iSCSILUNIoSizeRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNIoSizeRead.setStatus("current")
_ISCSILUNIoSizeWrite_Type = Integer32
_ISCSILUNIoSizeWrite_Object = MibTableColumn
iSCSILUNIoSizeWrite = _ISCSILUNIoSizeWrite_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 15),
    _ISCSILUNIoSizeWrite_Type()
)
iSCSILUNIoSizeWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNIoSizeWrite.setStatus("current")
_ISCSILUNQueueDepth_Type = Integer32
_ISCSILUNQueueDepth_Object = MibTableColumn
iSCSILUNQueueDepth = _ISCSILUNQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 16),
    _ISCSILUNQueueDepth_Type()
)
iSCSILUNQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNQueueDepth.setStatus("current")


class _ISCSILUNType_Type(OctetString):
    """Custom type iSCSILUNType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ISCSILUNType_Type.__name__ = "OctetString"
_ISCSILUNType_Object = MibTableColumn
iSCSILUNType = _ISCSILUNType_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 17),
    _ISCSILUNType_Type()
)
iSCSILUNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNType.setStatus("current")
_ISCSILUNDiskLatencyAvg_Type = Integer32
_ISCSILUNDiskLatencyAvg_Object = MibTableColumn
iSCSILUNDiskLatencyAvg = _ISCSILUNDiskLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 18),
    _ISCSILUNDiskLatencyAvg_Type()
)
iSCSILUNDiskLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNDiskLatencyAvg.setStatus("current")
_ISCSILUNThinProvisionVolFreeMBs_Type = Integer32
_ISCSILUNThinProvisionVolFreeMBs_Object = MibTableColumn
iSCSILUNThinProvisionVolFreeMBs = _ISCSILUNThinProvisionVolFreeMBs_Object(
    (1, 3, 6, 1, 4, 1, 6574, 104, 1, 1, 19),
    _ISCSILUNThinProvisionVolFreeMBs_Type()
)
iSCSILUNThinProvisionVolFreeMBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSILUNThinProvisionVolFreeMBs.setStatus("current")
_SynologyiSCSILUNConformance_ObjectIdentity = ObjectIdentity
synologyiSCSILUNConformance = _SynologyiSCSILUNConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 104, 2)
)
_SynologyiSCSILUNCompliances_ObjectIdentity = ObjectIdentity
synologyiSCSILUNCompliances = _SynologyiSCSILUNCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 104, 2, 1)
)
_SynologyiSCSILUNGroups_ObjectIdentity = ObjectIdentity
synologyiSCSILUNGroups = _SynologyiSCSILUNGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 104, 2, 2)
)

# Managed Objects groups

synologyiSCSILUNGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 104, 2, 2, 1)
)
synologyiSCSILUNGroup.setObjects(
      *(("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNUUID"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNName"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputReadHigh"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputReadLow"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputWriteHigh"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThroughputWriteLow"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIopsRead"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIopsWrite"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNDiskLatencyRead"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNDiskLatencyWrite"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNNetworkLatencyTx"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNNetworkLatencyRx"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIoSizeRead"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNIoSizeWrite"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNQueueDepth"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNType"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNDiskLatencyAvg"),
        ("SYNOLOGY-ISCSILUN-MIB", "iSCSILUNThinProvisionVolFreeMBs"))
)
if mibBuilder.loadTexts:
    synologyiSCSILUNGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyiSCSILUNCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 104, 2, 1, 1)
)
synologyiSCSILUNCompliance.setObjects(
    ("SYNOLOGY-ISCSILUN-MIB", "synologyiSCSILUNGroup")
)
if mibBuilder.loadTexts:
    synologyiSCSILUNCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-ISCSILUN-MIB",
    **{"synology": synology,
       "synologyiSCSILUN": synologyiSCSILUN,
       "iSCSILUNTable": iSCSILUNTable,
       "iSCSILUNEntry": iSCSILUNEntry,
       "iSCSILUNInfoIndex": iSCSILUNInfoIndex,
       "iSCSILUNUUID": iSCSILUNUUID,
       "iSCSILUNName": iSCSILUNName,
       "iSCSILUNThroughputReadHigh": iSCSILUNThroughputReadHigh,
       "iSCSILUNThroughputReadLow": iSCSILUNThroughputReadLow,
       "iSCSILUNThroughputWriteHigh": iSCSILUNThroughputWriteHigh,
       "iSCSILUNThroughputWriteLow": iSCSILUNThroughputWriteLow,
       "iSCSILUNIopsRead": iSCSILUNIopsRead,
       "iSCSILUNIopsWrite": iSCSILUNIopsWrite,
       "iSCSILUNDiskLatencyRead": iSCSILUNDiskLatencyRead,
       "iSCSILUNDiskLatencyWrite": iSCSILUNDiskLatencyWrite,
       "iSCSILUNNetworkLatencyTx": iSCSILUNNetworkLatencyTx,
       "iSCSILUNNetworkLatencyRx": iSCSILUNNetworkLatencyRx,
       "iSCSILUNIoSizeRead": iSCSILUNIoSizeRead,
       "iSCSILUNIoSizeWrite": iSCSILUNIoSizeWrite,
       "iSCSILUNQueueDepth": iSCSILUNQueueDepth,
       "iSCSILUNType": iSCSILUNType,
       "iSCSILUNDiskLatencyAvg": iSCSILUNDiskLatencyAvg,
       "iSCSILUNThinProvisionVolFreeMBs": iSCSILUNThinProvisionVolFreeMBs,
       "synologyiSCSILUNConformance": synologyiSCSILUNConformance,
       "synologyiSCSILUNCompliances": synologyiSCSILUNCompliances,
       "synologyiSCSILUNCompliance": synologyiSCSILUNCompliance,
       "synologyiSCSILUNGroups": synologyiSCSILUNGroups,
       "synologyiSCSILUNGroup": synologyiSCSILUNGroup}
)
