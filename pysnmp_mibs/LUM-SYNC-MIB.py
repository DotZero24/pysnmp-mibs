# SNMP MIB module (LUM-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SYNC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:33 2025
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

(lumModules,
 lumSyncMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSyncMIB")

(AdminStatus,
 BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 PortNumber,
 SlotNumber,
 SubrackNumber,
 SyncSourceMode,
 SyncSourceState) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatus",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber",
    "SyncSourceMode",
    "SyncSourceState")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lumSyncMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 17)
)
if mibBuilder.loadTexts:
    lumSyncMIBModule.setRevisions(
        ("2018-01-25 00:00",
         "2017-09-01 00:00",
         "2017-06-15 00:00",
         "2016-02-01 00:00",
         "2015-01-14 00:00",
         "2012-12-25 12:00",
         "2011-05-31 00:00",
         "2007-11-12 00:00",
         "2002-12-11 00:00",
         "2002-11-20 00:00",
         "2002-05-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSyncConfs_ObjectIdentity = ObjectIdentity
lumSyncConfs = _LumSyncConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1)
)
_LumSyncGroups_ObjectIdentity = ObjectIdentity
lumSyncGroups = _LumSyncGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1)
)
_LumSyncCompl_ObjectIdentity = ObjectIdentity
lumSyncCompl = _LumSyncCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2)
)
_LumSyncMIBObjects_ObjectIdentity = ObjectIdentity
lumSyncMIBObjects = _LumSyncMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2)
)
_SyncGeneral_ObjectIdentity = ObjectIdentity
syncGeneral = _SyncGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1)
)
_SyncGeneralLastChangeTime_Type = DateAndTime
_SyncGeneralLastChangeTime_Object = MibScalar
syncGeneralLastChangeTime = _SyncGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 1),
    _SyncGeneralLastChangeTime_Type()
)
syncGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralLastChangeTime.setStatus("current")
_SyncGeneralStateLastChangeTime_Type = DateAndTime
_SyncGeneralStateLastChangeTime_Object = MibScalar
syncGeneralStateLastChangeTime = _SyncGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 2),
    _SyncGeneralStateLastChangeTime_Type()
)
syncGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralStateLastChangeTime.setStatus("current")
_SyncGeneralSyncGroupTableSize_Type = Unsigned32
_SyncGeneralSyncGroupTableSize_Object = MibScalar
syncGeneralSyncGroupTableSize = _SyncGeneralSyncGroupTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 3),
    _SyncGeneralSyncGroupTableSize_Type()
)
syncGeneralSyncGroupTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralSyncGroupTableSize.setStatus("current")
_SyncGeneralSyncSourceTableSize_Type = Unsigned32
_SyncGeneralSyncSourceTableSize_Object = MibScalar
syncGeneralSyncSourceTableSize = _SyncGeneralSyncSourceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 4),
    _SyncGeneralSyncSourceTableSize_Type()
)
syncGeneralSyncSourceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralSyncSourceTableSize.setStatus("current")
_SyncGeneralSyncSubrackTableSize_Type = Unsigned32
_SyncGeneralSyncSubrackTableSize_Object = MibScalar
syncGeneralSyncSubrackTableSize = _SyncGeneralSyncSubrackTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 5),
    _SyncGeneralSyncSubrackTableSize_Type()
)
syncGeneralSyncSubrackTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralSyncSubrackTableSize.setStatus("deprecated")
_SyncGeneralSyncDomainTableSize_Type = Unsigned32
_SyncGeneralSyncDomainTableSize_Object = MibScalar
syncGeneralSyncDomainTableSize = _SyncGeneralSyncDomainTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 6),
    _SyncGeneralSyncDomainTableSize_Type()
)
syncGeneralSyncDomainTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralSyncDomainTableSize.setStatus("current")
_SyncGeneralSyncBusTableSize_Type = Unsigned32
_SyncGeneralSyncBusTableSize_Object = MibScalar
syncGeneralSyncBusTableSize = _SyncGeneralSyncBusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 7),
    _SyncGeneralSyncBusTableSize_Type()
)
syncGeneralSyncBusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralSyncBusTableSize.setStatus("current")
_SyncGeneralSyncBoardToDomainTableSize_Type = Unsigned32
_SyncGeneralSyncBoardToDomainTableSize_Object = MibScalar
syncGeneralSyncBoardToDomainTableSize = _SyncGeneralSyncBoardToDomainTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 1, 8),
    _SyncGeneralSyncBoardToDomainTableSize_Type()
)
syncGeneralSyncBoardToDomainTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGeneralSyncBoardToDomainTableSize.setStatus("current")
_SyncGroups_ObjectIdentity = ObjectIdentity
syncGroups = _SyncGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2)
)
_SyncGroupTable_Object = MibTable
syncGroupTable = _SyncGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1)
)
if mibBuilder.loadTexts:
    syncGroupTable.setStatus("current")
_SyncGroupEntry_Object = MibTableRow
syncGroupEntry = _SyncGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1)
)
syncGroupEntry.setIndexNames(
    (0, "LUM-SYNC-MIB", "syncGroupIndex"),
)
if mibBuilder.loadTexts:
    syncGroupEntry.setStatus("current")
_SyncGroupIndex_Type = Unsigned32
_SyncGroupIndex_Object = MibTableColumn
syncGroupIndex = _SyncGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 1),
    _SyncGroupIndex_Type()
)
syncGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupIndex.setStatus("current")
_SyncGroupName_Type = MgmtNameString
_SyncGroupName_Object = MibTableColumn
syncGroupName = _SyncGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 2),
    _SyncGroupName_Type()
)
syncGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupName.setStatus("current")
_SyncGroupSubrack_Type = SubrackNumber
_SyncGroupSubrack_Object = MibTableColumn
syncGroupSubrack = _SyncGroupSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 3),
    _SyncGroupSubrack_Type()
)
syncGroupSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupSubrack.setStatus("current")
_SyncGroupSlot_Type = SlotNumber
_SyncGroupSlot_Object = MibTableColumn
syncGroupSlot = _SyncGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 4),
    _SyncGroupSlot_Type()
)
syncGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupSlot.setStatus("current")


class _SyncGroupMode_Type(Integer32):
    """Custom type syncGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_SyncGroupMode_Type.__name__ = "Integer32"
_SyncGroupMode_Object = MibTableColumn
syncGroupMode = _SyncGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 5),
    _SyncGroupMode_Type()
)
syncGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncGroupMode.setStatus("current")


class _SyncGroupManualSource_Type(Unsigned32):
    """Custom type syncGroupManualSource based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SyncGroupManualSource_Type.__name__ = "Unsigned32"
_SyncGroupManualSource_Object = MibTableColumn
syncGroupManualSource = _SyncGroupManualSource_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 6),
    _SyncGroupManualSource_Type()
)
syncGroupManualSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncGroupManualSource.setStatus("current")
_SyncGroupSelectedSource_Type = MgmtNameString
_SyncGroupSelectedSource_Object = MibTableColumn
syncGroupSelectedSource = _SyncGroupSelectedSource_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 7),
    _SyncGroupSelectedSource_Type()
)
syncGroupSelectedSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupSelectedSource.setStatus("current")


class _SyncGroupQuality_Type(Unsigned32):
    """Custom type syncGroupQuality based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SyncGroupQuality_Type.__name__ = "Unsigned32"
_SyncGroupQuality_Object = MibTableColumn
syncGroupQuality = _SyncGroupQuality_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 8),
    _SyncGroupQuality_Type()
)
syncGroupQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupQuality.setStatus("current")
_SyncGroupLocalOscActiveW2C_Type = FaultStatus
_SyncGroupLocalOscActiveW2C_Object = MibTableColumn
syncGroupLocalOscActiveW2C = _SyncGroupLocalOscActiveW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 9),
    _SyncGroupLocalOscActiveW2C_Type()
)
syncGroupLocalOscActiveW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupLocalOscActiveW2C.setStatus("deprecated")
_SyncGroupLocalOscActive_Type = FaultStatus
_SyncGroupLocalOscActive_Object = MibTableColumn
syncGroupLocalOscActive = _SyncGroupLocalOscActive_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 10),
    _SyncGroupLocalOscActive_Type()
)
syncGroupLocalOscActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupLocalOscActive.setStatus("current")


class _SyncGroupAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type syncGroupAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_SyncGroupAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_SyncGroupAdminStatus_Object = MibTableColumn
syncGroupAdminStatus = _SyncGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 11),
    _SyncGroupAdminStatus_Type()
)
syncGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncGroupAdminStatus.setStatus("current")


class _SyncGroupOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type syncGroupOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_SyncGroupOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_SyncGroupOperStatus_Object = MibTableColumn
syncGroupOperStatus = _SyncGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 12),
    _SyncGroupOperStatus_Type()
)
syncGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupOperStatus.setStatus("current")


class _SyncGroupRingMode_Type(Integer32):
    """Custom type syncGroupRingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SyncGroupRingMode_Type.__name__ = "Integer32"
_SyncGroupRingMode_Object = MibTableColumn
syncGroupRingMode = _SyncGroupRingMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 13),
    _SyncGroupRingMode_Type()
)
syncGroupRingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncGroupRingMode.setStatus("deprecated")
_SyncGroupLastChangeTime_Type = DateAndTime
_SyncGroupLastChangeTime_Object = MibTableColumn
syncGroupLastChangeTime = _SyncGroupLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 14),
    _SyncGroupLastChangeTime_Type()
)
syncGroupLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupLastChangeTime.setStatus("current")


class _SyncGroupManualSourceName_Type(MgmtNameString):
    """Custom type syncGroupManualSourceName based on MgmtNameString"""
    defaultValue = OctetString("")


_SyncGroupManualSourceName_Type.__name__ = "MgmtNameString"
_SyncGroupManualSourceName_Object = MibTableColumn
syncGroupManualSourceName = _SyncGroupManualSourceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 15),
    _SyncGroupManualSourceName_Type()
)
syncGroupManualSourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncGroupManualSourceName.setStatus("current")


class _SyncGroupConfigurationMode_Type(Integer32):
    """Custom type syncGroupConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neverUseTrunc", 1),
          ("uniDirRingSatellite", 2),
          ("standardG707", 3))
    )


_SyncGroupConfigurationMode_Type.__name__ = "Integer32"
_SyncGroupConfigurationMode_Object = MibTableColumn
syncGroupConfigurationMode = _SyncGroupConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 16),
    _SyncGroupConfigurationMode_Type()
)
syncGroupConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncGroupConfigurationMode.setStatus("current")


class _SyncGroupStatus_Type(Integer32):
    """Custom type syncGroupStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("holdover", 2))
    )


_SyncGroupStatus_Type.__name__ = "Integer32"
_SyncGroupStatus_Object = MibTableColumn
syncGroupStatus = _SyncGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 17),
    _SyncGroupStatus_Type()
)
syncGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupStatus.setStatus("current")
_SyncGroupSourceSwitch_Type = CommandString
_SyncGroupSourceSwitch_Object = MibTableColumn
syncGroupSourceSwitch = _SyncGroupSourceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 18),
    _SyncGroupSourceSwitch_Type()
)
syncGroupSourceSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupSourceSwitch.setStatus("current")


class _SyncGroupSourceSwitchType_Type(Integer32):
    """Custom type syncGroupSourceSwitchType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("forced", 3))
    )


_SyncGroupSourceSwitchType_Type.__name__ = "Integer32"
_SyncGroupSourceSwitchType_Object = MibTableColumn
syncGroupSourceSwitchType = _SyncGroupSourceSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 19),
    _SyncGroupSourceSwitchType_Type()
)
syncGroupSourceSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupSourceSwitchType.setStatus("current")
_SyncGroupHoldover_Type = FaultStatus
_SyncGroupHoldover_Object = MibTableColumn
syncGroupHoldover = _SyncGroupHoldover_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 20),
    _SyncGroupHoldover_Type()
)
syncGroupHoldover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupHoldover.setStatus("current")


class _SyncGroupQualityLevelSelectionMode_Type(Integer32):
    """Custom type syncGroupQualityLevelSelectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SyncGroupQualityLevelSelectionMode_Type.__name__ = "Integer32"
_SyncGroupQualityLevelSelectionMode_Object = MibTableColumn
syncGroupQualityLevelSelectionMode = _SyncGroupQualityLevelSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 2, 1, 1, 21),
    _SyncGroupQualityLevelSelectionMode_Type()
)
syncGroupQualityLevelSelectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncGroupQualityLevelSelectionMode.setStatus("current")
_SyncSources_ObjectIdentity = ObjectIdentity
syncSources = _SyncSources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3)
)
_SyncSourceTable_Object = MibTable
syncSourceTable = _SyncSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1)
)
if mibBuilder.loadTexts:
    syncSourceTable.setStatus("current")
_SyncSourceEntry_Object = MibTableRow
syncSourceEntry = _SyncSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1)
)
syncSourceEntry.setIndexNames(
    (0, "LUM-SYNC-MIB", "syncSourceIndex"),
)
if mibBuilder.loadTexts:
    syncSourceEntry.setStatus("current")


class _SyncSourceIndex_Type(Unsigned32):
    """Custom type syncSourceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_SyncSourceIndex_Type.__name__ = "Unsigned32"
_SyncSourceIndex_Object = MibTableColumn
syncSourceIndex = _SyncSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 1),
    _SyncSourceIndex_Type()
)
syncSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceIndex.setStatus("current")
_SyncSourceName_Type = MgmtNameString
_SyncSourceName_Object = MibTableColumn
syncSourceName = _SyncSourceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 2),
    _SyncSourceName_Type()
)
syncSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceName.setStatus("current")


class _SyncSourceId_Type(Unsigned32):
    """Custom type syncSourceId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SyncSourceId_Type.__name__ = "Unsigned32"
_SyncSourceId_Object = MibTableColumn
syncSourceId = _SyncSourceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 3),
    _SyncSourceId_Type()
)
syncSourceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceId.setStatus("current")


class _SyncSourceRxPort_Type(PortNumber):
    """Custom type syncSourceRxPort based on PortNumber"""
    defaultValue = 0


_SyncSourceRxPort_Type.__name__ = "PortNumber"
_SyncSourceRxPort_Object = MibTableColumn
syncSourceRxPort = _SyncSourceRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 4),
    _SyncSourceRxPort_Type()
)
syncSourceRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceRxPort.setStatus("current")


class _SyncSourceTxPort_Type(PortNumber):
    """Custom type syncSourceTxPort based on PortNumber"""
    defaultValue = 0


_SyncSourceTxPort_Type.__name__ = "PortNumber"
_SyncSourceTxPort_Object = MibTableColumn
syncSourceTxPort = _SyncSourceTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 5),
    _SyncSourceTxPort_Type()
)
syncSourceTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceTxPort.setStatus("current")


class _SyncSourceType_Type(Integer32):
    """Custom type syncSourceType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oscillator", 1),
          ("signal", 2),
          ("external", 3),
          ("bus", 4))
    )


_SyncSourceType_Type.__name__ = "Integer32"
_SyncSourceType_Object = MibTableColumn
syncSourceType = _SyncSourceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 6),
    _SyncSourceType_Type()
)
syncSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceType.setStatus("current")


class _SyncSourceQuality_Type(Unsigned32):
    """Custom type syncSourceQuality based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_SyncSourceQuality_Type.__name__ = "Unsigned32"
_SyncSourceQuality_Object = MibTableColumn
syncSourceQuality = _SyncSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 7),
    _SyncSourceQuality_Type()
)
syncSourceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceQuality.setStatus("current")


class _SyncSourcePriority_Type(Unsigned32):
    """Custom type syncSourcePriority based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SyncSourcePriority_Type.__name__ = "Unsigned32"
_SyncSourcePriority_Object = MibTableColumn
syncSourcePriority = _SyncSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 8),
    _SyncSourcePriority_Type()
)
syncSourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncSourcePriority.setStatus("current")


class _SyncSourceAdminStatus_Type(AdminStatus):
    """Custom type syncSourceAdminStatus based on AdminStatus"""
    defaultValue = 1


_SyncSourceAdminStatus_Type.__name__ = "AdminStatus"
_SyncSourceAdminStatus_Object = MibTableColumn
syncSourceAdminStatus = _SyncSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 9),
    _SyncSourceAdminStatus_Type()
)
syncSourceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncSourceAdminStatus.setStatus("current")


class _SyncSourceOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type syncSourceOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_SyncSourceOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_SyncSourceOperStatus_Object = MibTableColumn
syncSourceOperStatus = _SyncSourceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 10),
    _SyncSourceOperStatus_Type()
)
syncSourceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceOperStatus.setStatus("current")
_SyncSourceIsSelected_Type = TruthValue
_SyncSourceIsSelected_Object = MibTableColumn
syncSourceIsSelected = _SyncSourceIsSelected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 11),
    _SyncSourceIsSelected_Type()
)
syncSourceIsSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceIsSelected.setStatus("current")


class _SyncSourceAlwaysSendDoNotUse_Type(Integer32):
    """Custom type syncSourceAlwaysSendDoNotUse based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SyncSourceAlwaysSendDoNotUse_Type.__name__ = "Integer32"
_SyncSourceAlwaysSendDoNotUse_Object = MibTableColumn
syncSourceAlwaysSendDoNotUse = _SyncSourceAlwaysSendDoNotUse_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 12),
    _SyncSourceAlwaysSendDoNotUse_Type()
)
syncSourceAlwaysSendDoNotUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncSourceAlwaysSendDoNotUse.setStatus("current")


class _SyncSourceStaticQuality_Type(Unsigned32):
    """Custom type syncSourceStaticQuality based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SyncSourceStaticQuality_Type.__name__ = "Unsigned32"
_SyncSourceStaticQuality_Object = MibTableColumn
syncSourceStaticQuality = _SyncSourceStaticQuality_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 13),
    _SyncSourceStaticQuality_Type()
)
syncSourceStaticQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncSourceStaticQuality.setStatus("current")
_SyncSourceFilterState_Type = SyncSourceState
_SyncSourceFilterState_Object = MibTableColumn
syncSourceFilterState = _SyncSourceFilterState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 14),
    _SyncSourceFilterState_Type()
)
syncSourceFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceFilterState.setStatus("current")


class _SyncSourceMode_Type(SyncSourceMode):
    """Custom type syncSourceMode based on SyncSourceMode"""
    defaultValue = 0


_SyncSourceMode_Type.__name__ = "SyncSourceMode"
_SyncSourceMode_Object = MibTableColumn
syncSourceMode = _SyncSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 15),
    _SyncSourceMode_Type()
)
syncSourceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncSourceMode.setStatus("current")
_SyncSourceClearWaitToRestore_Type = CommandString
_SyncSourceClearWaitToRestore_Object = MibTableColumn
syncSourceClearWaitToRestore = _SyncSourceClearWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 16),
    _SyncSourceClearWaitToRestore_Type()
)
syncSourceClearWaitToRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceClearWaitToRestore.setStatus("current")
_SyncSourceClockWanderExceeded_Type = FaultStatus
_SyncSourceClockWanderExceeded_Object = MibTableColumn
syncSourceClockWanderExceeded = _SyncSourceClockWanderExceeded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 17),
    _SyncSourceClockWanderExceeded_Type()
)
syncSourceClockWanderExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceClockWanderExceeded.setStatus("current")
_SyncSourceNonSyncEClock_Type = FaultStatus
_SyncSourceNonSyncEClock_Object = MibTableColumn
syncSourceNonSyncEClock = _SyncSourceNonSyncEClock_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 18),
    _SyncSourceNonSyncEClock_Type()
)
syncSourceNonSyncEClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSourceNonSyncEClock.setStatus("current")


class _SyncSourceIfNo_Type(PortNumber):
    """Custom type syncSourceIfNo based on PortNumber"""
    defaultValue = 1


_SyncSourceIfNo_Type.__name__ = "PortNumber"
_SyncSourceIfNo_Object = MibTableColumn
syncSourceIfNo = _SyncSourceIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 19),
    _SyncSourceIfNo_Type()
)
syncSourceIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceIfNo.setStatus("current")


class _SyncSourceUpPortId_Type(Integer32):
    """Custom type syncSourceUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SyncSourceUpPortId_Type.__name__ = "Integer32"
_SyncSourceUpPortId_Object = MibTableColumn
syncSourceUpPortId = _SyncSourceUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 20),
    _SyncSourceUpPortId_Type()
)
syncSourceUpPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceUpPortId.setStatus("current")


class _SyncSourceLocalId_Type(Integer32):
    """Custom type syncSourceLocalId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SyncSourceLocalId_Type.__name__ = "Integer32"
_SyncSourceLocalId_Object = MibTableColumn
syncSourceLocalId = _SyncSourceLocalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 3, 1, 1, 21),
    _SyncSourceLocalId_Type()
)
syncSourceLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSourceLocalId.setStatus("current")
_LumentisSyncNotifications_ObjectIdentity = ObjectIdentity
lumentisSyncNotifications = _LumentisSyncNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 4)
)
_SyncNotifyPrefix_ObjectIdentity = ObjectIdentity
syncNotifyPrefix = _SyncNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 4, 0)
)
_SyncSubracks_ObjectIdentity = ObjectIdentity
syncSubracks = _SyncSubracks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5)
)
_SyncSubrackTable_Object = MibTable
syncSubrackTable = _SyncSubrackTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1)
)
if mibBuilder.loadTexts:
    syncSubrackTable.setStatus("deprecated")
_SyncSubrackEntry_Object = MibTableRow
syncSubrackEntry = _SyncSubrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1)
)
syncSubrackEntry.setIndexNames(
    (0, "LUM-SYNC-MIB", "syncSubrackIndex"),
)
if mibBuilder.loadTexts:
    syncSubrackEntry.setStatus("deprecated")
_SyncSubrackIndex_Type = Unsigned32
_SyncSubrackIndex_Object = MibTableColumn
syncSubrackIndex = _SyncSubrackIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 1),
    _SyncSubrackIndex_Type()
)
syncSubrackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSubrackIndex.setStatus("deprecated")
_SyncSubrackName_Type = MgmtNameString
_SyncSubrackName_Object = MibTableColumn
syncSubrackName = _SyncSubrackName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 2),
    _SyncSubrackName_Type()
)
syncSubrackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSubrackName.setStatus("deprecated")
_SyncSubrackSubrack_Type = SubrackNumber
_SyncSubrackSubrack_Object = MibTableColumn
syncSubrackSubrack = _SyncSubrackSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 3),
    _SyncSubrackSubrack_Type()
)
syncSubrackSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSubrackSubrack.setStatus("deprecated")
_SyncSubrackMasterBusA_Type = SlotNumber
_SyncSubrackMasterBusA_Object = MibTableColumn
syncSubrackMasterBusA = _SyncSubrackMasterBusA_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 4),
    _SyncSubrackMasterBusA_Type()
)
syncSubrackMasterBusA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSubrackMasterBusA.setStatus("deprecated")
_SyncSubrackMasterBusB_Type = SlotNumber
_SyncSubrackMasterBusB_Object = MibTableColumn
syncSubrackMasterBusB = _SyncSubrackMasterBusB_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 5),
    _SyncSubrackMasterBusB_Type()
)
syncSubrackMasterBusB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncSubrackMasterBusB.setStatus("deprecated")
_SyncSubrackConfigureLocalBus_Type = CommandString
_SyncSubrackConfigureLocalBus_Object = MibTableColumn
syncSubrackConfigureLocalBus = _SyncSubrackConfigureLocalBus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 6),
    _SyncSubrackConfigureLocalBus_Type()
)
syncSubrackConfigureLocalBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSubrackConfigureLocalBus.setStatus("deprecated")
_SyncSubrackGroupMasterBusA_Type = DisplayString
_SyncSubrackGroupMasterBusA_Object = MibTableColumn
syncSubrackGroupMasterBusA = _SyncSubrackGroupMasterBusA_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 7),
    _SyncSubrackGroupMasterBusA_Type()
)
syncSubrackGroupMasterBusA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSubrackGroupMasterBusA.setStatus("deprecated")
_SyncSubrackGroupMasterBusB_Type = DisplayString
_SyncSubrackGroupMasterBusB_Object = MibTableColumn
syncSubrackGroupMasterBusB = _SyncSubrackGroupMasterBusB_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 5, 1, 1, 8),
    _SyncSubrackGroupMasterBusB_Type()
)
syncSubrackGroupMasterBusB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncSubrackGroupMasterBusB.setStatus("deprecated")
_SyncDomains_ObjectIdentity = ObjectIdentity
syncDomains = _SyncDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6)
)
_SyncDomainTable_Object = MibTable
syncDomainTable = _SyncDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1)
)
if mibBuilder.loadTexts:
    syncDomainTable.setStatus("current")
_SyncDomainEntry_Object = MibTableRow
syncDomainEntry = _SyncDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1)
)
syncDomainEntry.setIndexNames(
    (0, "LUM-SYNC-MIB", "syncDomainIndex"),
)
if mibBuilder.loadTexts:
    syncDomainEntry.setStatus("current")
_SyncDomainIndex_Type = Unsigned32
_SyncDomainIndex_Object = MibTableColumn
syncDomainIndex = _SyncDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 1),
    _SyncDomainIndex_Type()
)
syncDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncDomainIndex.setStatus("current")
_SyncDomainNumber_Type = Unsigned32
_SyncDomainNumber_Object = MibTableColumn
syncDomainNumber = _SyncDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 2),
    _SyncDomainNumber_Type()
)
syncDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncDomainNumber.setStatus("current")
_SyncDomainName_Type = MgmtNameString
_SyncDomainName_Object = MibTableColumn
syncDomainName = _SyncDomainName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 3),
    _SyncDomainName_Type()
)
syncDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncDomainName.setStatus("current")


class _SyncDomainQualityLevelSelectionMode_Type(Integer32):
    """Custom type syncDomainQualityLevelSelectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SyncDomainQualityLevelSelectionMode_Type.__name__ = "Integer32"
_SyncDomainQualityLevelSelectionMode_Object = MibTableColumn
syncDomainQualityLevelSelectionMode = _SyncDomainQualityLevelSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 4),
    _SyncDomainQualityLevelSelectionMode_Type()
)
syncDomainQualityLevelSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncDomainQualityLevelSelectionMode.setStatus("current")


class _SyncDomainWaitToRestore_Type(Unsigned32):
    """Custom type syncDomainWaitToRestore based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SyncDomainWaitToRestore_Type.__name__ = "Unsigned32"
_SyncDomainWaitToRestore_Object = MibTableColumn
syncDomainWaitToRestore = _SyncDomainWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 5),
    _SyncDomainWaitToRestore_Type()
)
syncDomainWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncDomainWaitToRestore.setStatus("current")


class _SyncDomainHoldOff_Type(Unsigned32):
    """Custom type syncDomainHoldOff based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SyncDomainHoldOff_Type.__name__ = "Unsigned32"
_SyncDomainHoldOff_Object = MibTableColumn
syncDomainHoldOff = _SyncDomainHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 6),
    _SyncDomainHoldOff_Type()
)
syncDomainHoldOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncDomainHoldOff.setStatus("current")
_SyncDomainSource_Type = MgmtNameString
_SyncDomainSource_Object = MibTableColumn
syncDomainSource = _SyncDomainSource_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 7),
    _SyncDomainSource_Type()
)
syncDomainSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncDomainSource.setStatus("current")


class _SyncDomainQuality_Type(Unsigned32):
    """Custom type syncDomainQuality based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SyncDomainQuality_Type.__name__ = "Unsigned32"
_SyncDomainQuality_Object = MibTableColumn
syncDomainQuality = _SyncDomainQuality_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 8),
    _SyncDomainQuality_Type()
)
syncDomainQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncDomainQuality.setStatus("current")
_SyncDomainAssociateBoard_Type = CommandString
_SyncDomainAssociateBoard_Object = MibTableColumn
syncDomainAssociateBoard = _SyncDomainAssociateBoard_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 6, 1, 1, 9),
    _SyncDomainAssociateBoard_Type()
)
syncDomainAssociateBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncDomainAssociateBoard.setStatus("current")
_SyncBuses_ObjectIdentity = ObjectIdentity
syncBuses = _SyncBuses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7)
)
_SyncBusTable_Object = MibTable
syncBusTable = _SyncBusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1)
)
if mibBuilder.loadTexts:
    syncBusTable.setStatus("current")
_SyncBusEntry_Object = MibTableRow
syncBusEntry = _SyncBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1)
)
syncBusEntry.setIndexNames(
    (0, "LUM-SYNC-MIB", "syncBusIndex"),
)
if mibBuilder.loadTexts:
    syncBusEntry.setStatus("current")
_SyncBusIndex_Type = Unsigned32
_SyncBusIndex_Object = MibTableColumn
syncBusIndex = _SyncBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 1),
    _SyncBusIndex_Type()
)
syncBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBusIndex.setStatus("current")
_SyncBusName_Type = MgmtNameString
_SyncBusName_Object = MibTableColumn
syncBusName = _SyncBusName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 2),
    _SyncBusName_Type()
)
syncBusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBusName.setStatus("current")
_SyncBusSubrack_Type = Unsigned32
_SyncBusSubrack_Object = MibTableColumn
syncBusSubrack = _SyncBusSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 3),
    _SyncBusSubrack_Type()
)
syncBusSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBusSubrack.setStatus("current")


class _SyncBusDomain_Type(Unsigned32):
    """Custom type syncBusDomain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_SyncBusDomain_Type.__name__ = "Unsigned32"
_SyncBusDomain_Object = MibTableColumn
syncBusDomain = _SyncBusDomain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 4),
    _SyncBusDomain_Type()
)
syncBusDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncBusDomain.setStatus("current")


class _SyncBusDomainIndex_Type(Unsigned32):
    """Custom type syncBusDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SyncBusDomainIndex_Type.__name__ = "Unsigned32"
_SyncBusDomainIndex_Object = MibTableColumn
syncBusDomainIndex = _SyncBusDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 5),
    _SyncBusDomainIndex_Type()
)
syncBusDomainIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncBusDomainIndex.setStatus("current")
_SyncBusStaticMasterSlot_Type = SlotNumber
_SyncBusStaticMasterSlot_Object = MibTableColumn
syncBusStaticMasterSlot = _SyncBusStaticMasterSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 6),
    _SyncBusStaticMasterSlot_Type()
)
syncBusStaticMasterSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncBusStaticMasterSlot.setStatus("current")


class _SyncBusStaticMasterIndex_Type(Unsigned32):
    """Custom type syncBusStaticMasterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SyncBusStaticMasterIndex_Type.__name__ = "Unsigned32"
_SyncBusStaticMasterIndex_Object = MibTableColumn
syncBusStaticMasterIndex = _SyncBusStaticMasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 7, 1, 1, 7),
    _SyncBusStaticMasterIndex_Type()
)
syncBusStaticMasterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncBusStaticMasterIndex.setStatus("current")
_SyncBoardToDomain_ObjectIdentity = ObjectIdentity
syncBoardToDomain = _SyncBoardToDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8)
)
_SyncBoardToDomainTable_Object = MibTable
syncBoardToDomainTable = _SyncBoardToDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1)
)
if mibBuilder.loadTexts:
    syncBoardToDomainTable.setStatus("current")
_SyncBoardToDomainEntry_Object = MibTableRow
syncBoardToDomainEntry = _SyncBoardToDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1)
)
syncBoardToDomainEntry.setIndexNames(
    (0, "LUM-SYNC-MIB", "syncBoardToDomainIndex"),
)
if mibBuilder.loadTexts:
    syncBoardToDomainEntry.setStatus("current")
_SyncBoardToDomainIndex_Type = Unsigned32
_SyncBoardToDomainIndex_Object = MibTableColumn
syncBoardToDomainIndex = _SyncBoardToDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1, 1),
    _SyncBoardToDomainIndex_Type()
)
syncBoardToDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBoardToDomainIndex.setStatus("current")
_SyncBoardToDomainName_Type = MgmtNameString
_SyncBoardToDomainName_Object = MibTableColumn
syncBoardToDomainName = _SyncBoardToDomainName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1, 2),
    _SyncBoardToDomainName_Type()
)
syncBoardToDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBoardToDomainName.setStatus("current")


class _SyncBoardToDomainDomainIndex_Type(Unsigned32):
    """Custom type syncBoardToDomainDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SyncBoardToDomainDomainIndex_Type.__name__ = "Unsigned32"
_SyncBoardToDomainDomainIndex_Object = MibTableColumn
syncBoardToDomainDomainIndex = _SyncBoardToDomainDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1, 3),
    _SyncBoardToDomainDomainIndex_Type()
)
syncBoardToDomainDomainIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncBoardToDomainDomainIndex.setStatus("current")
_SyncBoardToDomainDomainName_Type = MgmtNameString
_SyncBoardToDomainDomainName_Object = MibTableColumn
syncBoardToDomainDomainName = _SyncBoardToDomainDomainName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1, 4),
    _SyncBoardToDomainDomainName_Type()
)
syncBoardToDomainDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBoardToDomainDomainName.setStatus("current")


class _SyncBoardToDomainBoardIndex_Type(Unsigned32):
    """Custom type syncBoardToDomainBoardIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SyncBoardToDomainBoardIndex_Type.__name__ = "Unsigned32"
_SyncBoardToDomainBoardIndex_Object = MibTableColumn
syncBoardToDomainBoardIndex = _SyncBoardToDomainBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1, 5),
    _SyncBoardToDomainBoardIndex_Type()
)
syncBoardToDomainBoardIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncBoardToDomainBoardIndex.setStatus("current")
_SyncBoardToDomainBoardName_Type = MgmtNameString
_SyncBoardToDomainBoardName_Object = MibTableColumn
syncBoardToDomainBoardName = _SyncBoardToDomainBoardName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 8, 1, 1, 6),
    _SyncBoardToDomainBoardName_Type()
)
syncBoardToDomainBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncBoardToDomainBoardName.setStatus("current")

# Managed Objects groups

syncGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 1)
)
syncGeneralGroup.setObjects(
    ("LUM-SYNC-MIB", "syncGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    syncGeneralGroup.setStatus("deprecated")

syncGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 2)
)
syncGroupGroup.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActiveW2C"))
)
if mibBuilder.loadTexts:
    syncGroupGroup.setStatus("deprecated")

syncSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 3)
)
syncSourceGroup.setObjects(
      *(("LUM-SYNC-MIB", "syncSourceIndex"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncSourceRxPort"),
        ("LUM-SYNC-MIB", "syncSourceTxPort"),
        ("LUM-SYNC-MIB", "syncSourceType"),
        ("LUM-SYNC-MIB", "syncSourceQuality"),
        ("LUM-SYNC-MIB", "syncSourcePriority"),
        ("LUM-SYNC-MIB", "syncSourceAdminStatus"),
        ("LUM-SYNC-MIB", "syncSourceOperStatus"),
        ("LUM-SYNC-MIB", "syncSourceIsSelected"))
)
if mibBuilder.loadTexts:
    syncSourceGroup.setStatus("current")

syncGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 4)
)
syncGeneralGroupV2.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    syncGeneralGroupV2.setStatus("deprecated")

syncGroupGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 5)
)
syncGroupGroupV2.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActiveW2C"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV2.setStatus("deprecated")

syncGroupGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 6)
)
syncGroupGroupV3.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActiveW2C"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"),
        ("LUM-SYNC-MIB", "syncGroupRingMode"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV3.setStatus("deprecated")

syncSourceGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 7)
)
syncSourceGroupV2.setObjects(
      *(("LUM-SYNC-MIB", "syncSourceIndex"),
        ("LUM-SYNC-MIB", "syncSourceId"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncSourceRxPort"),
        ("LUM-SYNC-MIB", "syncSourceTxPort"),
        ("LUM-SYNC-MIB", "syncSourceType"),
        ("LUM-SYNC-MIB", "syncSourceQuality"),
        ("LUM-SYNC-MIB", "syncSourcePriority"),
        ("LUM-SYNC-MIB", "syncSourceAdminStatus"),
        ("LUM-SYNC-MIB", "syncSourceOperStatus"),
        ("LUM-SYNC-MIB", "syncSourceIsSelected"))
)
if mibBuilder.loadTexts:
    syncSourceGroupV2.setStatus("deprecated")

syncGroupGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 9)
)
syncGroupGroupV4.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActiveW2C"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"),
        ("LUM-SYNC-MIB", "syncGroupRingMode"),
        ("LUM-SYNC-MIB", "syncGroupLastChangeTime"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV4.setStatus("deprecated")

syncSourceGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 10)
)
syncSourceGroupV3.setObjects(
      *(("LUM-SYNC-MIB", "syncSourceIndex"),
        ("LUM-SYNC-MIB", "syncSourceId"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncSourceRxPort"),
        ("LUM-SYNC-MIB", "syncSourceTxPort"),
        ("LUM-SYNC-MIB", "syncSourceType"),
        ("LUM-SYNC-MIB", "syncSourceQuality"),
        ("LUM-SYNC-MIB", "syncSourcePriority"),
        ("LUM-SYNC-MIB", "syncSourceAdminStatus"),
        ("LUM-SYNC-MIB", "syncSourceOperStatus"),
        ("LUM-SYNC-MIB", "syncSourceIsSelected"),
        ("LUM-SYNC-MIB", "syncSourceAlwaysSendDoNotUse"))
)
if mibBuilder.loadTexts:
    syncSourceGroupV3.setStatus("deprecated")

syncGroupGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 12)
)
syncGroupGroupV6.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActive"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"),
        ("LUM-SYNC-MIB", "syncGroupRingMode"),
        ("LUM-SYNC-MIB", "syncGroupLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGroupManualSourceName"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV6.setStatus("deprecated")

syncGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 13)
)
syncGeneralGroupV3.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGeneralStateLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGeneralSyncGroupTableSize"),
        ("LUM-SYNC-MIB", "syncGeneralSyncSourceTableSize"),
        ("LUM-SYNC-MIB", "syncGeneralSyncSubrackTableSize"))
)
if mibBuilder.loadTexts:
    syncGeneralGroupV3.setStatus("current")

syncGroupGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 14)
)
syncGroupGroupV7.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActive"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"),
        ("LUM-SYNC-MIB", "syncGroupRingMode"),
        ("LUM-SYNC-MIB", "syncGroupLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGroupManualSourceName"),
        ("LUM-SYNC-MIB", "syncGroupConfigurationMode"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV7.setStatus("deprecated")

syncSubrackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 15)
)
syncSubrackGroup.setObjects(
      *(("LUM-SYNC-MIB", "syncSubrackIndex"),
        ("LUM-SYNC-MIB", "syncSubrackSubrack"),
        ("LUM-SYNC-MIB", "syncSubrackName"),
        ("LUM-SYNC-MIB", "syncSubrackMasterBusA"),
        ("LUM-SYNC-MIB", "syncSubrackMasterBusB"),
        ("LUM-SYNC-MIB", "syncSubrackConfigureLocalBus"))
)
if mibBuilder.loadTexts:
    syncSubrackGroup.setStatus("deprecated")

syncGroupGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 16)
)
syncGroupGroupV8.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActive"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"),
        ("LUM-SYNC-MIB", "syncGroupRingMode"),
        ("LUM-SYNC-MIB", "syncGroupLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGroupManualSourceName"),
        ("LUM-SYNC-MIB", "syncGroupConfigurationMode"),
        ("LUM-SYNC-MIB", "syncGroupStatus"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV8.setStatus("current")

syncSubrackGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 17)
)
syncSubrackGroupV2.setObjects(
      *(("LUM-SYNC-MIB", "syncSubrackIndex"),
        ("LUM-SYNC-MIB", "syncSubrackSubrack"),
        ("LUM-SYNC-MIB", "syncSubrackName"),
        ("LUM-SYNC-MIB", "syncSubrackMasterBusA"),
        ("LUM-SYNC-MIB", "syncSubrackMasterBusB"),
        ("LUM-SYNC-MIB", "syncSubrackConfigureLocalBus"),
        ("LUM-SYNC-MIB", "syncSubrackGroupMasterBusA"),
        ("LUM-SYNC-MIB", "syncSubrackGroupMasterBusB"))
)
if mibBuilder.loadTexts:
    syncSubrackGroupV2.setStatus("current")

syncSourceGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 18)
)
syncSourceGroupV4.setObjects(
      *(("LUM-SYNC-MIB", "syncSourceIndex"),
        ("LUM-SYNC-MIB", "syncSourceId"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncSourceRxPort"),
        ("LUM-SYNC-MIB", "syncSourceTxPort"),
        ("LUM-SYNC-MIB", "syncSourceType"),
        ("LUM-SYNC-MIB", "syncSourceQuality"),
        ("LUM-SYNC-MIB", "syncSourcePriority"),
        ("LUM-SYNC-MIB", "syncSourceAdminStatus"),
        ("LUM-SYNC-MIB", "syncSourceOperStatus"),
        ("LUM-SYNC-MIB", "syncSourceIsSelected"),
        ("LUM-SYNC-MIB", "syncSourceAlwaysSendDoNotUse"),
        ("LUM-SYNC-MIB", "syncSourceStaticQuality"),
        ("LUM-SYNC-MIB", "syncSourceFilterState"))
)
if mibBuilder.loadTexts:
    syncSourceGroupV4.setStatus("deprecated")

syncDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 19)
)
syncDomainGroup.setObjects(
      *(("LUM-SYNC-MIB", "syncDomainIndex"),
        ("LUM-SYNC-MIB", "syncDomainName"),
        ("LUM-SYNC-MIB", "syncDomainNumber"),
        ("LUM-SYNC-MIB", "syncDomainQualityLevelSelectionMode"),
        ("LUM-SYNC-MIB", "syncDomainWaitToRestore"),
        ("LUM-SYNC-MIB", "syncDomainHoldOff"),
        ("LUM-SYNC-MIB", "syncDomainSource"),
        ("LUM-SYNC-MIB", "syncDomainQuality"),
        ("LUM-SYNC-MIB", "syncDomainAssociateBoard"))
)
if mibBuilder.loadTexts:
    syncDomainGroup.setStatus("current")

syncBusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 20)
)
syncBusGroup.setObjects(
      *(("LUM-SYNC-MIB", "syncBusIndex"),
        ("LUM-SYNC-MIB", "syncBusName"),
        ("LUM-SYNC-MIB", "syncBusSubrack"),
        ("LUM-SYNC-MIB", "syncBusDomain"),
        ("LUM-SYNC-MIB", "syncBusDomainIndex"),
        ("LUM-SYNC-MIB", "syncBusStaticMasterSlot"),
        ("LUM-SYNC-MIB", "syncBusStaticMasterIndex"))
)
if mibBuilder.loadTexts:
    syncBusGroup.setStatus("current")

syncBoardToDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 21)
)
syncBoardToDomainGroup.setObjects(
      *(("LUM-SYNC-MIB", "syncBoardToDomainIndex"),
        ("LUM-SYNC-MIB", "syncBoardToDomainName"),
        ("LUM-SYNC-MIB", "syncBoardToDomainDomainIndex"),
        ("LUM-SYNC-MIB", "syncBoardToDomainDomainName"),
        ("LUM-SYNC-MIB", "syncBoardToDomainBoardIndex"),
        ("LUM-SYNC-MIB", "syncBoardToDomainBoardName"))
)
if mibBuilder.loadTexts:
    syncBoardToDomainGroup.setStatus("current")

syncGroupGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 22)
)
syncGroupGroupV9.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupSubrack"),
        ("LUM-SYNC-MIB", "syncGroupSlot"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupMode"),
        ("LUM-SYNC-MIB", "syncGroupManualSource"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncGroupQuality"),
        ("LUM-SYNC-MIB", "syncGroupLocalOscActive"),
        ("LUM-SYNC-MIB", "syncGroupAdminStatus"),
        ("LUM-SYNC-MIB", "syncGroupOperStatus"),
        ("LUM-SYNC-MIB", "syncGroupRingMode"),
        ("LUM-SYNC-MIB", "syncGroupLastChangeTime"),
        ("LUM-SYNC-MIB", "syncGroupManualSourceName"),
        ("LUM-SYNC-MIB", "syncGroupConfigurationMode"),
        ("LUM-SYNC-MIB", "syncGroupStatus"),
        ("LUM-SYNC-MIB", "syncGroupSourceSwitch"),
        ("LUM-SYNC-MIB", "syncGroupSourceSwitchType"),
        ("LUM-SYNC-MIB", "syncGroupHoldover"),
        ("LUM-SYNC-MIB", "syncGroupQualityLevelSelectionMode"))
)
if mibBuilder.loadTexts:
    syncGroupGroupV9.setStatus("current")

syncSourceGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 23)
)
syncSourceGroupV5.setObjects(
      *(("LUM-SYNC-MIB", "syncSourceIndex"),
        ("LUM-SYNC-MIB", "syncSourceId"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncSourceRxPort"),
        ("LUM-SYNC-MIB", "syncSourceTxPort"),
        ("LUM-SYNC-MIB", "syncSourceType"),
        ("LUM-SYNC-MIB", "syncSourceQuality"),
        ("LUM-SYNC-MIB", "syncSourcePriority"),
        ("LUM-SYNC-MIB", "syncSourceAdminStatus"),
        ("LUM-SYNC-MIB", "syncSourceOperStatus"),
        ("LUM-SYNC-MIB", "syncSourceIsSelected"),
        ("LUM-SYNC-MIB", "syncSourceAlwaysSendDoNotUse"),
        ("LUM-SYNC-MIB", "syncSourceStaticQuality"),
        ("LUM-SYNC-MIB", "syncSourceFilterState"),
        ("LUM-SYNC-MIB", "syncSourceClockWanderExceeded"),
        ("LUM-SYNC-MIB", "syncSourceNonSyncEClock"))
)
if mibBuilder.loadTexts:
    syncSourceGroupV5.setStatus("deprecated")

syncSourceGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 24)
)
syncSourceGroupV6.setObjects(
      *(("LUM-SYNC-MIB", "syncSourceIndex"),
        ("LUM-SYNC-MIB", "syncSourceId"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncSourceRxPort"),
        ("LUM-SYNC-MIB", "syncSourceTxPort"),
        ("LUM-SYNC-MIB", "syncSourceType"),
        ("LUM-SYNC-MIB", "syncSourceQuality"),
        ("LUM-SYNC-MIB", "syncSourcePriority"),
        ("LUM-SYNC-MIB", "syncSourceAdminStatus"),
        ("LUM-SYNC-MIB", "syncSourceOperStatus"),
        ("LUM-SYNC-MIB", "syncSourceIsSelected"),
        ("LUM-SYNC-MIB", "syncSourceAlwaysSendDoNotUse"),
        ("LUM-SYNC-MIB", "syncSourceStaticQuality"),
        ("LUM-SYNC-MIB", "syncSourceFilterState"),
        ("LUM-SYNC-MIB", "syncSourceClockWanderExceeded"),
        ("LUM-SYNC-MIB", "syncSourceNonSyncEClock"),
        ("LUM-SYNC-MIB", "syncSourceIfNo"),
        ("LUM-SYNC-MIB", "syncSourceUpPortId"),
        ("LUM-SYNC-MIB", "syncSourceLocalId"))
)
if mibBuilder.loadTexts:
    syncSourceGroupV6.setStatus("current")


# Notification objects

syncGroupSourceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 2, 4, 0, 1)
)
syncGroupSourceChanged.setObjects(
      *(("LUM-SYNC-MIB", "syncGroupIndex"),
        ("LUM-SYNC-MIB", "syncGroupName"),
        ("LUM-SYNC-MIB", "syncGroupSelectedSource"),
        ("LUM-SYNC-MIB", "syncSourceName"),
        ("LUM-SYNC-MIB", "syncGroupLastChangeTime"),
        ("LUM-SYNC-MIB", "syncSourceQuality"))
)
if mibBuilder.loadTexts:
    syncGroupSourceChanged.setStatus(
        "current"
    )


# Notifications groups

syncNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 1, 8)
)
syncNotificationGroup.setObjects(
    ("LUM-SYNC-MIB", "syncGroupSourceChanged")
)
if mibBuilder.loadTexts:
    syncNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumSyncBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 1)
)
lumSyncBasicComplV1.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroup"),
        ("LUM-SYNC-MIB", "syncGroupGroup"),
        ("LUM-SYNC-MIB", "syncSourceGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV1.setStatus(
        "deprecated"
    )

lumSyncBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 2)
)
lumSyncBasicComplV2.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroup"),
        ("LUM-SYNC-MIB", "syncSourceGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV2.setStatus(
        "deprecated"
    )

lumSyncBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 3)
)
lumSyncBasicComplV3.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV2"),
        ("LUM-SYNC-MIB", "syncSourceGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV3.setStatus(
        "deprecated"
    )

lumSyncBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 4)
)
lumSyncBasicComplV4.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV3"),
        ("LUM-SYNC-MIB", "syncSourceGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV4.setStatus(
        "deprecated"
    )

lumSyncBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 5)
)
lumSyncBasicComplV5.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV3"),
        ("LUM-SYNC-MIB", "syncSourceGroupV2"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV5.setStatus(
        "deprecated"
    )

lumSyncBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 6)
)
lumSyncBasicComplV6.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV3"),
        ("LUM-SYNC-MIB", "syncSourceGroupV2"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV6.setStatus(
        "deprecated"
    )

lumSyncBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 7)
)
lumSyncBasicComplV7.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV4"),
        ("LUM-SYNC-MIB", "syncSourceGroupV2"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV7.setStatus(
        "deprecated"
    )

lumSyncBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 8)
)
lumSyncBasicComplV8.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV4"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV8.setStatus(
        "deprecated"
    )

lumSyncBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 9)
)
lumSyncBasicComplV9.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV2"),
        ("LUM-SYNC-MIB", "syncGroupGroupV6"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV9.setStatus(
        "deprecated"
    )

lumSyncBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 10)
)
lumSyncBasicComplV10.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV6"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV10.setStatus(
        "deprecated"
    )

lumSyncBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 11)
)
lumSyncBasicComplV11.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV6"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV11.setStatus(
        "deprecated"
    )

lumSyncBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 12)
)
lumSyncBasicComplV12.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV7"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV12.setStatus(
        "deprecated"
    )

lumSyncBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 13)
)
lumSyncBasicComplV13.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV8"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"),
        ("LUM-SYNC-MIB", "syncSubrackGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV13.setStatus(
        "deprecated"
    )

lumSyncBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 14)
)
lumSyncBasicComplV14.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV8"),
        ("LUM-SYNC-MIB", "syncSourceGroupV3"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"),
        ("LUM-SYNC-MIB", "syncSubrackGroupV2"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV14.setStatus(
        "deprecated"
    )

lumSyncBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 15)
)
lumSyncBasicComplV15.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV9"),
        ("LUM-SYNC-MIB", "syncSourceGroupV4"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"),
        ("LUM-SYNC-MIB", "syncDomainGroup"),
        ("LUM-SYNC-MIB", "syncBusGroup"),
        ("LUM-SYNC-MIB", "syncBoardToDomainGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV15.setStatus(
        "deprecated"
    )

lumSyncBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 16)
)
lumSyncBasicComplV16.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV9"),
        ("LUM-SYNC-MIB", "syncSourceGroupV5"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"),
        ("LUM-SYNC-MIB", "syncDomainGroup"),
        ("LUM-SYNC-MIB", "syncBusGroup"),
        ("LUM-SYNC-MIB", "syncBoardToDomainGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV16.setStatus(
        "current"
    )

lumSyncBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 16, 1, 2, 17)
)
lumSyncBasicComplV17.setObjects(
      *(("LUM-SYNC-MIB", "syncGeneralGroupV3"),
        ("LUM-SYNC-MIB", "syncGroupGroupV9"),
        ("LUM-SYNC-MIB", "syncSourceGroupV6"),
        ("LUM-SYNC-MIB", "syncNotificationGroup"),
        ("LUM-SYNC-MIB", "syncDomainGroup"),
        ("LUM-SYNC-MIB", "syncBusGroup"),
        ("LUM-SYNC-MIB", "syncBoardToDomainGroup"))
)
if mibBuilder.loadTexts:
    lumSyncBasicComplV17.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SYNC-MIB",
    **{"lumSyncMIBModule": lumSyncMIBModule,
       "lumSyncConfs": lumSyncConfs,
       "lumSyncGroups": lumSyncGroups,
       "syncGeneralGroup": syncGeneralGroup,
       "syncGroupGroup": syncGroupGroup,
       "syncSourceGroup": syncSourceGroup,
       "syncGeneralGroupV2": syncGeneralGroupV2,
       "syncGroupGroupV2": syncGroupGroupV2,
       "syncGroupGroupV3": syncGroupGroupV3,
       "syncSourceGroupV2": syncSourceGroupV2,
       "syncNotificationGroup": syncNotificationGroup,
       "syncGroupGroupV4": syncGroupGroupV4,
       "syncSourceGroupV3": syncSourceGroupV3,
       "syncGroupGroupV6": syncGroupGroupV6,
       "syncGeneralGroupV3": syncGeneralGroupV3,
       "syncGroupGroupV7": syncGroupGroupV7,
       "syncSubrackGroup": syncSubrackGroup,
       "syncGroupGroupV8": syncGroupGroupV8,
       "syncSubrackGroupV2": syncSubrackGroupV2,
       "syncSourceGroupV4": syncSourceGroupV4,
       "syncDomainGroup": syncDomainGroup,
       "syncBusGroup": syncBusGroup,
       "syncBoardToDomainGroup": syncBoardToDomainGroup,
       "syncGroupGroupV9": syncGroupGroupV9,
       "syncSourceGroupV5": syncSourceGroupV5,
       "syncSourceGroupV6": syncSourceGroupV6,
       "lumSyncCompl": lumSyncCompl,
       "lumSyncBasicComplV1": lumSyncBasicComplV1,
       "lumSyncBasicComplV2": lumSyncBasicComplV2,
       "lumSyncBasicComplV3": lumSyncBasicComplV3,
       "lumSyncBasicComplV4": lumSyncBasicComplV4,
       "lumSyncBasicComplV5": lumSyncBasicComplV5,
       "lumSyncBasicComplV6": lumSyncBasicComplV6,
       "lumSyncBasicComplV7": lumSyncBasicComplV7,
       "lumSyncBasicComplV8": lumSyncBasicComplV8,
       "lumSyncBasicComplV9": lumSyncBasicComplV9,
       "lumSyncBasicComplV10": lumSyncBasicComplV10,
       "lumSyncBasicComplV11": lumSyncBasicComplV11,
       "lumSyncBasicComplV12": lumSyncBasicComplV12,
       "lumSyncBasicComplV13": lumSyncBasicComplV13,
       "lumSyncBasicComplV14": lumSyncBasicComplV14,
       "lumSyncBasicComplV15": lumSyncBasicComplV15,
       "lumSyncBasicComplV16": lumSyncBasicComplV16,
       "lumSyncBasicComplV17": lumSyncBasicComplV17,
       "lumSyncMIBObjects": lumSyncMIBObjects,
       "syncGeneral": syncGeneral,
       "syncGeneralLastChangeTime": syncGeneralLastChangeTime,
       "syncGeneralStateLastChangeTime": syncGeneralStateLastChangeTime,
       "syncGeneralSyncGroupTableSize": syncGeneralSyncGroupTableSize,
       "syncGeneralSyncSourceTableSize": syncGeneralSyncSourceTableSize,
       "syncGeneralSyncSubrackTableSize": syncGeneralSyncSubrackTableSize,
       "syncGeneralSyncDomainTableSize": syncGeneralSyncDomainTableSize,
       "syncGeneralSyncBusTableSize": syncGeneralSyncBusTableSize,
       "syncGeneralSyncBoardToDomainTableSize": syncGeneralSyncBoardToDomainTableSize,
       "syncGroups": syncGroups,
       "syncGroupTable": syncGroupTable,
       "syncGroupEntry": syncGroupEntry,
       "syncGroupIndex": syncGroupIndex,
       "syncGroupName": syncGroupName,
       "syncGroupSubrack": syncGroupSubrack,
       "syncGroupSlot": syncGroupSlot,
       "syncGroupMode": syncGroupMode,
       "syncGroupManualSource": syncGroupManualSource,
       "syncGroupSelectedSource": syncGroupSelectedSource,
       "syncGroupQuality": syncGroupQuality,
       "syncGroupLocalOscActiveW2C": syncGroupLocalOscActiveW2C,
       "syncGroupLocalOscActive": syncGroupLocalOscActive,
       "syncGroupAdminStatus": syncGroupAdminStatus,
       "syncGroupOperStatus": syncGroupOperStatus,
       "syncGroupRingMode": syncGroupRingMode,
       "syncGroupLastChangeTime": syncGroupLastChangeTime,
       "syncGroupManualSourceName": syncGroupManualSourceName,
       "syncGroupConfigurationMode": syncGroupConfigurationMode,
       "syncGroupStatus": syncGroupStatus,
       "syncGroupSourceSwitch": syncGroupSourceSwitch,
       "syncGroupSourceSwitchType": syncGroupSourceSwitchType,
       "syncGroupHoldover": syncGroupHoldover,
       "syncGroupQualityLevelSelectionMode": syncGroupQualityLevelSelectionMode,
       "syncSources": syncSources,
       "syncSourceTable": syncSourceTable,
       "syncSourceEntry": syncSourceEntry,
       "syncSourceIndex": syncSourceIndex,
       "syncSourceName": syncSourceName,
       "syncSourceId": syncSourceId,
       "syncSourceRxPort": syncSourceRxPort,
       "syncSourceTxPort": syncSourceTxPort,
       "syncSourceType": syncSourceType,
       "syncSourceQuality": syncSourceQuality,
       "syncSourcePriority": syncSourcePriority,
       "syncSourceAdminStatus": syncSourceAdminStatus,
       "syncSourceOperStatus": syncSourceOperStatus,
       "syncSourceIsSelected": syncSourceIsSelected,
       "syncSourceAlwaysSendDoNotUse": syncSourceAlwaysSendDoNotUse,
       "syncSourceStaticQuality": syncSourceStaticQuality,
       "syncSourceFilterState": syncSourceFilterState,
       "syncSourceMode": syncSourceMode,
       "syncSourceClearWaitToRestore": syncSourceClearWaitToRestore,
       "syncSourceClockWanderExceeded": syncSourceClockWanderExceeded,
       "syncSourceNonSyncEClock": syncSourceNonSyncEClock,
       "syncSourceIfNo": syncSourceIfNo,
       "syncSourceUpPortId": syncSourceUpPortId,
       "syncSourceLocalId": syncSourceLocalId,
       "lumentisSyncNotifications": lumentisSyncNotifications,
       "syncNotifyPrefix": syncNotifyPrefix,
       "syncGroupSourceChanged": syncGroupSourceChanged,
       "syncSubracks": syncSubracks,
       "syncSubrackTable": syncSubrackTable,
       "syncSubrackEntry": syncSubrackEntry,
       "syncSubrackIndex": syncSubrackIndex,
       "syncSubrackName": syncSubrackName,
       "syncSubrackSubrack": syncSubrackSubrack,
       "syncSubrackMasterBusA": syncSubrackMasterBusA,
       "syncSubrackMasterBusB": syncSubrackMasterBusB,
       "syncSubrackConfigureLocalBus": syncSubrackConfigureLocalBus,
       "syncSubrackGroupMasterBusA": syncSubrackGroupMasterBusA,
       "syncSubrackGroupMasterBusB": syncSubrackGroupMasterBusB,
       "syncDomains": syncDomains,
       "syncDomainTable": syncDomainTable,
       "syncDomainEntry": syncDomainEntry,
       "syncDomainIndex": syncDomainIndex,
       "syncDomainNumber": syncDomainNumber,
       "syncDomainName": syncDomainName,
       "syncDomainQualityLevelSelectionMode": syncDomainQualityLevelSelectionMode,
       "syncDomainWaitToRestore": syncDomainWaitToRestore,
       "syncDomainHoldOff": syncDomainHoldOff,
       "syncDomainSource": syncDomainSource,
       "syncDomainQuality": syncDomainQuality,
       "syncDomainAssociateBoard": syncDomainAssociateBoard,
       "syncBuses": syncBuses,
       "syncBusTable": syncBusTable,
       "syncBusEntry": syncBusEntry,
       "syncBusIndex": syncBusIndex,
       "syncBusName": syncBusName,
       "syncBusSubrack": syncBusSubrack,
       "syncBusDomain": syncBusDomain,
       "syncBusDomainIndex": syncBusDomainIndex,
       "syncBusStaticMasterSlot": syncBusStaticMasterSlot,
       "syncBusStaticMasterIndex": syncBusStaticMasterIndex,
       "syncBoardToDomain": syncBoardToDomain,
       "syncBoardToDomainTable": syncBoardToDomainTable,
       "syncBoardToDomainEntry": syncBoardToDomainEntry,
       "syncBoardToDomainIndex": syncBoardToDomainIndex,
       "syncBoardToDomainName": syncBoardToDomainName,
       "syncBoardToDomainDomainIndex": syncBoardToDomainDomainIndex,
       "syncBoardToDomainDomainName": syncBoardToDomainDomainName,
       "syncBoardToDomainBoardIndex": syncBoardToDomainBoardIndex,
       "syncBoardToDomainBoardName": syncBoardToDomainBoardName}
)
