# SNMP MIB module (LUM-SYSINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SYSINFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:08 2025
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
 lumSysinfoMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSysinfoMIB")

(Integer32WithNA,
 MgmtNameString,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "Integer32WithNA",
    "MgmtNameString",
    "Unsigned32WithNA")

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

lumSysinfoMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 71)
)
if mibBuilder.loadTexts:
    lumSysinfoMIBModule.setRevisions(
        ("2018-06-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSysinfoConfs_ObjectIdentity = ObjectIdentity
lumSysinfoConfs = _LumSysinfoConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1)
)
_LumSysinfoGroups_ObjectIdentity = ObjectIdentity
lumSysinfoGroups = _LumSysinfoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 1)
)
_LumSysinfoCompl_ObjectIdentity = ObjectIdentity
lumSysinfoCompl = _LumSysinfoCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 2)
)
_LumSysinfoMIBObjects_ObjectIdentity = ObjectIdentity
lumSysinfoMIBObjects = _LumSysinfoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2)
)
_SysinfoBoardStartupList_ObjectIdentity = ObjectIdentity
sysinfoBoardStartupList = _SysinfoBoardStartupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1)
)
_SysinfoBoardStartupTable_Object = MibTable
sysinfoBoardStartupTable = _SysinfoBoardStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sysinfoBoardStartupTable.setStatus("current")
_SysinfoBoardStartupEntry_Object = MibTableRow
sysinfoBoardStartupEntry = _SysinfoBoardStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1, 1)
)
sysinfoBoardStartupEntry.setIndexNames(
    (0, "LUM-SYSINFO-MIB", "sysinfoBoardStartupIndex"),
)
if mibBuilder.loadTexts:
    sysinfoBoardStartupEntry.setStatus("current")


class _SysinfoBoardStartupIndex_Type(Unsigned32):
    """Custom type sysinfoBoardStartupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysinfoBoardStartupIndex_Type.__name__ = "Unsigned32"
_SysinfoBoardStartupIndex_Object = MibTableColumn
sysinfoBoardStartupIndex = _SysinfoBoardStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1, 1, 1),
    _SysinfoBoardStartupIndex_Type()
)
sysinfoBoardStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardStartupIndex.setStatus("current")
_SysinfoBoardStartupName_Type = MgmtNameString
_SysinfoBoardStartupName_Object = MibTableColumn
sysinfoBoardStartupName = _SysinfoBoardStartupName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1, 1, 2),
    _SysinfoBoardStartupName_Type()
)
sysinfoBoardStartupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardStartupName.setStatus("current")
_SysinfoBoardStartupUptime_Type = DisplayString
_SysinfoBoardStartupUptime_Object = MibTableColumn
sysinfoBoardStartupUptime = _SysinfoBoardStartupUptime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1, 1, 3),
    _SysinfoBoardStartupUptime_Type()
)
sysinfoBoardStartupUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardStartupUptime.setStatus("current")
_SysinfoBoardStartupUptimeSeconds_Type = Unsigned32
_SysinfoBoardStartupUptimeSeconds_Object = MibTableColumn
sysinfoBoardStartupUptimeSeconds = _SysinfoBoardStartupUptimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1, 1, 4),
    _SysinfoBoardStartupUptimeSeconds_Type()
)
sysinfoBoardStartupUptimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardStartupUptimeSeconds.setStatus("current")


class _SysinfoBoardStartupRebootReason_Type(DisplayString):
    """Custom type sysinfoBoardStartupRebootReason based on DisplayString"""
    defaultValue = OctetString(" ")


_SysinfoBoardStartupRebootReason_Type.__name__ = "DisplayString"
_SysinfoBoardStartupRebootReason_Object = MibTableColumn
sysinfoBoardStartupRebootReason = _SysinfoBoardStartupRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 1, 1, 1, 5),
    _SysinfoBoardStartupRebootReason_Type()
)
sysinfoBoardStartupRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardStartupRebootReason.setStatus("current")
_SysinfoBoardLoadList_ObjectIdentity = ObjectIdentity
sysinfoBoardLoadList = _SysinfoBoardLoadList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2)
)
_SysinfoBoardLoadTable_Object = MibTable
sysinfoBoardLoadTable = _SysinfoBoardLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sysinfoBoardLoadTable.setStatus("current")
_SysinfoBoardLoadEntry_Object = MibTableRow
sysinfoBoardLoadEntry = _SysinfoBoardLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1, 1)
)
sysinfoBoardLoadEntry.setIndexNames(
    (0, "LUM-SYSINFO-MIB", "sysinfoBoardLoadIndex"),
)
if mibBuilder.loadTexts:
    sysinfoBoardLoadEntry.setStatus("current")


class _SysinfoBoardLoadIndex_Type(Unsigned32):
    """Custom type sysinfoBoardLoadIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysinfoBoardLoadIndex_Type.__name__ = "Unsigned32"
_SysinfoBoardLoadIndex_Object = MibTableColumn
sysinfoBoardLoadIndex = _SysinfoBoardLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1, 1, 1),
    _SysinfoBoardLoadIndex_Type()
)
sysinfoBoardLoadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardLoadIndex.setStatus("current")
_SysinfoBoardLoadName_Type = MgmtNameString
_SysinfoBoardLoadName_Object = MibTableColumn
sysinfoBoardLoadName = _SysinfoBoardLoadName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1, 1, 2),
    _SysinfoBoardLoadName_Type()
)
sysinfoBoardLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardLoadName.setStatus("current")
_SysinfoBoardLoadLoad1Min_Type = Unsigned32
_SysinfoBoardLoadLoad1Min_Object = MibTableColumn
sysinfoBoardLoadLoad1Min = _SysinfoBoardLoadLoad1Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1, 1, 3),
    _SysinfoBoardLoadLoad1Min_Type()
)
sysinfoBoardLoadLoad1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardLoadLoad1Min.setStatus("current")
_SysinfoBoardLoadLoad5Min_Type = Unsigned32
_SysinfoBoardLoadLoad5Min_Object = MibTableColumn
sysinfoBoardLoadLoad5Min = _SysinfoBoardLoadLoad5Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1, 1, 4),
    _SysinfoBoardLoadLoad5Min_Type()
)
sysinfoBoardLoadLoad5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardLoadLoad5Min.setStatus("current")
_SysinfoBoardLoadLoad15Min_Type = Unsigned32
_SysinfoBoardLoadLoad15Min_Object = MibTableColumn
sysinfoBoardLoadLoad15Min = _SysinfoBoardLoadLoad15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 2, 1, 1, 5),
    _SysinfoBoardLoadLoad15Min_Type()
)
sysinfoBoardLoadLoad15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardLoadLoad15Min.setStatus("current")
_SysinfoBoardMemoryList_ObjectIdentity = ObjectIdentity
sysinfoBoardMemoryList = _SysinfoBoardMemoryList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3)
)
_SysinfoBoardMemoryTable_Object = MibTable
sysinfoBoardMemoryTable = _SysinfoBoardMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sysinfoBoardMemoryTable.setStatus("current")
_SysinfoBoardMemoryEntry_Object = MibTableRow
sysinfoBoardMemoryEntry = _SysinfoBoardMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1)
)
sysinfoBoardMemoryEntry.setIndexNames(
    (0, "LUM-SYSINFO-MIB", "sysinfoBoardMemoryIndex"),
)
if mibBuilder.loadTexts:
    sysinfoBoardMemoryEntry.setStatus("current")


class _SysinfoBoardMemoryIndex_Type(Unsigned32):
    """Custom type sysinfoBoardMemoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysinfoBoardMemoryIndex_Type.__name__ = "Unsigned32"
_SysinfoBoardMemoryIndex_Object = MibTableColumn
sysinfoBoardMemoryIndex = _SysinfoBoardMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1, 1),
    _SysinfoBoardMemoryIndex_Type()
)
sysinfoBoardMemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardMemoryIndex.setStatus("current")
_SysinfoBoardMemoryName_Type = MgmtNameString
_SysinfoBoardMemoryName_Object = MibTableColumn
sysinfoBoardMemoryName = _SysinfoBoardMemoryName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1, 2),
    _SysinfoBoardMemoryName_Type()
)
sysinfoBoardMemoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardMemoryName.setStatus("current")
_SysinfoBoardMemoryTotalMem_Type = Unsigned32
_SysinfoBoardMemoryTotalMem_Object = MibTableColumn
sysinfoBoardMemoryTotalMem = _SysinfoBoardMemoryTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1, 3),
    _SysinfoBoardMemoryTotalMem_Type()
)
sysinfoBoardMemoryTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardMemoryTotalMem.setStatus("current")
_SysinfoBoardMemoryFreeMem_Type = Unsigned32
_SysinfoBoardMemoryFreeMem_Object = MibTableColumn
sysinfoBoardMemoryFreeMem = _SysinfoBoardMemoryFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1, 4),
    _SysinfoBoardMemoryFreeMem_Type()
)
sysinfoBoardMemoryFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardMemoryFreeMem.setStatus("current")
_SysinfoBoardMemoryAvailableMem_Type = Unsigned32
_SysinfoBoardMemoryAvailableMem_Object = MibTableColumn
sysinfoBoardMemoryAvailableMem = _SysinfoBoardMemoryAvailableMem_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1, 5),
    _SysinfoBoardMemoryAvailableMem_Type()
)
sysinfoBoardMemoryAvailableMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardMemoryAvailableMem.setStatus("current")
_SysinfoBoardMemoryUsageMemPercent_Type = Unsigned32
_SysinfoBoardMemoryUsageMemPercent_Object = MibTableColumn
sysinfoBoardMemoryUsageMemPercent = _SysinfoBoardMemoryUsageMemPercent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 3, 1, 1, 6),
    _SysinfoBoardMemoryUsageMemPercent_Type()
)
sysinfoBoardMemoryUsageMemPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardMemoryUsageMemPercent.setStatus("current")
_SysinfoBoardProcessList_ObjectIdentity = ObjectIdentity
sysinfoBoardProcessList = _SysinfoBoardProcessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4)
)
_SysinfoBoardProcessTable_Object = MibTable
sysinfoBoardProcessTable = _SysinfoBoardProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sysinfoBoardProcessTable.setStatus("current")
_SysinfoBoardProcessEntry_Object = MibTableRow
sysinfoBoardProcessEntry = _SysinfoBoardProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1)
)
sysinfoBoardProcessEntry.setIndexNames(
    (0, "LUM-SYSINFO-MIB", "sysinfoBoardProcessIndex"),
)
if mibBuilder.loadTexts:
    sysinfoBoardProcessEntry.setStatus("current")


class _SysinfoBoardProcessIndex_Type(Unsigned32):
    """Custom type sysinfoBoardProcessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysinfoBoardProcessIndex_Type.__name__ = "Unsigned32"
_SysinfoBoardProcessIndex_Object = MibTableColumn
sysinfoBoardProcessIndex = _SysinfoBoardProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 1),
    _SysinfoBoardProcessIndex_Type()
)
sysinfoBoardProcessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessIndex.setStatus("current")
_SysinfoBoardProcessName_Type = MgmtNameString
_SysinfoBoardProcessName_Object = MibTableColumn
sysinfoBoardProcessName = _SysinfoBoardProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 2),
    _SysinfoBoardProcessName_Type()
)
sysinfoBoardProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessName.setStatus("current")
_SysinfoBoardProcessProcessName_Type = MgmtNameString
_SysinfoBoardProcessProcessName_Object = MibTableColumn
sysinfoBoardProcessProcessName = _SysinfoBoardProcessProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 3),
    _SysinfoBoardProcessProcessName_Type()
)
sysinfoBoardProcessProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessProcessName.setStatus("current")
_SysinfoBoardProcessPid_Type = Integer32
_SysinfoBoardProcessPid_Object = MibTableColumn
sysinfoBoardProcessPid = _SysinfoBoardProcessPid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 4),
    _SysinfoBoardProcessPid_Type()
)
sysinfoBoardProcessPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessPid.setStatus("current")
_SysinfoBoardProcessVmSize_Type = Unsigned32
_SysinfoBoardProcessVmSize_Object = MibTableColumn
sysinfoBoardProcessVmSize = _SysinfoBoardProcessVmSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 5),
    _SysinfoBoardProcessVmSize_Type()
)
sysinfoBoardProcessVmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessVmSize.setStatus("current")
_SysinfoBoardProcessVmRSS_Type = Unsigned32
_SysinfoBoardProcessVmRSS_Object = MibTableColumn
sysinfoBoardProcessVmRSS = _SysinfoBoardProcessVmRSS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 6),
    _SysinfoBoardProcessVmRSS_Type()
)
sysinfoBoardProcessVmRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessVmRSS.setStatus("current")


class _SysinfoBoardProcessSetReference_Type(Integer32):
    """Custom type sysinfoBoardProcessSetReference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("setReference", 2))
    )


_SysinfoBoardProcessSetReference_Type.__name__ = "Integer32"
_SysinfoBoardProcessSetReference_Object = MibTableColumn
sysinfoBoardProcessSetReference = _SysinfoBoardProcessSetReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 7),
    _SysinfoBoardProcessSetReference_Type()
)
sysinfoBoardProcessSetReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysinfoBoardProcessSetReference.setStatus("current")
_SysinfoBoardProcessVmSizeReference_Type = Unsigned32WithNA
_SysinfoBoardProcessVmSizeReference_Object = MibTableColumn
sysinfoBoardProcessVmSizeReference = _SysinfoBoardProcessVmSizeReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 8),
    _SysinfoBoardProcessVmSizeReference_Type()
)
sysinfoBoardProcessVmSizeReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessVmSizeReference.setStatus("current")
_SysinfoBoardProcessVmRSSReference_Type = Unsigned32WithNA
_SysinfoBoardProcessVmRSSReference_Object = MibTableColumn
sysinfoBoardProcessVmRSSReference = _SysinfoBoardProcessVmRSSReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 9),
    _SysinfoBoardProcessVmRSSReference_Type()
)
sysinfoBoardProcessVmRSSReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessVmRSSReference.setStatus("current")
_SysinfoBoardProcessVmSizeDiff_Type = Integer32WithNA
_SysinfoBoardProcessVmSizeDiff_Object = MibTableColumn
sysinfoBoardProcessVmSizeDiff = _SysinfoBoardProcessVmSizeDiff_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 10),
    _SysinfoBoardProcessVmSizeDiff_Type()
)
sysinfoBoardProcessVmSizeDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessVmSizeDiff.setStatus("current")
_SysinfoBoardProcessVmRSSDiff_Type = Integer32WithNA
_SysinfoBoardProcessVmRSSDiff_Object = MibTableColumn
sysinfoBoardProcessVmRSSDiff = _SysinfoBoardProcessVmRSSDiff_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 11),
    _SysinfoBoardProcessVmRSSDiff_Type()
)
sysinfoBoardProcessVmRSSDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessVmRSSDiff.setStatus("current")


class _SysinfoBoardProcessReferenceTime_Type(DisplayString):
    """Custom type sysinfoBoardProcessReferenceTime based on DisplayString"""
    defaultValue = OctetString("Not set")


_SysinfoBoardProcessReferenceTime_Type.__name__ = "DisplayString"
_SysinfoBoardProcessReferenceTime_Object = MibTableColumn
sysinfoBoardProcessReferenceTime = _SysinfoBoardProcessReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 2, 4, 1, 1, 12),
    _SysinfoBoardProcessReferenceTime_Type()
)
sysinfoBoardProcessReferenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysinfoBoardProcessReferenceTime.setStatus("current")

# Managed Objects groups

sysinfoBoardStartupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 1, 1)
)
sysinfoBoardStartupGroup.setObjects(
      *(("LUM-SYSINFO-MIB", "sysinfoBoardStartupIndex"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardStartupName"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardStartupUptime"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardStartupUptimeSeconds"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardStartupRebootReason"))
)
if mibBuilder.loadTexts:
    sysinfoBoardStartupGroup.setStatus("current")

sysinfoBoardLoadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 1, 2)
)
sysinfoBoardLoadGroup.setObjects(
      *(("LUM-SYSINFO-MIB", "sysinfoBoardLoadIndex"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardLoadName"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardLoadLoad1Min"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardLoadLoad5Min"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardLoadLoad15Min"))
)
if mibBuilder.loadTexts:
    sysinfoBoardLoadGroup.setStatus("current")

sysinfoBoardMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 1, 3)
)
sysinfoBoardMemoryGroup.setObjects(
      *(("LUM-SYSINFO-MIB", "sysinfoBoardMemoryIndex"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardMemoryName"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardMemoryTotalMem"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardMemoryFreeMem"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardMemoryAvailableMem"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardMemoryUsageMemPercent"))
)
if mibBuilder.loadTexts:
    sysinfoBoardMemoryGroup.setStatus("current")

sysinfoBoardProcessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 1, 4)
)
sysinfoBoardProcessGroup.setObjects(
      *(("LUM-SYSINFO-MIB", "sysinfoBoardProcessIndex"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessName"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessProcessName"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessPid"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessVmSize"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessVmRSS"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessSetReference"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessVmSizeReference"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessVmRSSReference"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessVmSizeDiff"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessVmRSSDiff"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessReferenceTime"))
)
if mibBuilder.loadTexts:
    sysinfoBoardProcessGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumSysinfoBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 71, 1, 2, 1)
)
lumSysinfoBasicComplV1.setObjects(
      *(("LUM-SYSINFO-MIB", "sysinfoBoardStartupGroup"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardLoadGroup"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardMemoryGroup"),
        ("LUM-SYSINFO-MIB", "sysinfoBoardProcessGroup"))
)
if mibBuilder.loadTexts:
    lumSysinfoBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SYSINFO-MIB",
    **{"lumSysinfoMIBModule": lumSysinfoMIBModule,
       "lumSysinfoConfs": lumSysinfoConfs,
       "lumSysinfoGroups": lumSysinfoGroups,
       "sysinfoBoardStartupGroup": sysinfoBoardStartupGroup,
       "sysinfoBoardLoadGroup": sysinfoBoardLoadGroup,
       "sysinfoBoardMemoryGroup": sysinfoBoardMemoryGroup,
       "sysinfoBoardProcessGroup": sysinfoBoardProcessGroup,
       "lumSysinfoCompl": lumSysinfoCompl,
       "lumSysinfoBasicComplV1": lumSysinfoBasicComplV1,
       "lumSysinfoMIBObjects": lumSysinfoMIBObjects,
       "sysinfoBoardStartupList": sysinfoBoardStartupList,
       "sysinfoBoardStartupTable": sysinfoBoardStartupTable,
       "sysinfoBoardStartupEntry": sysinfoBoardStartupEntry,
       "sysinfoBoardStartupIndex": sysinfoBoardStartupIndex,
       "sysinfoBoardStartupName": sysinfoBoardStartupName,
       "sysinfoBoardStartupUptime": sysinfoBoardStartupUptime,
       "sysinfoBoardStartupUptimeSeconds": sysinfoBoardStartupUptimeSeconds,
       "sysinfoBoardStartupRebootReason": sysinfoBoardStartupRebootReason,
       "sysinfoBoardLoadList": sysinfoBoardLoadList,
       "sysinfoBoardLoadTable": sysinfoBoardLoadTable,
       "sysinfoBoardLoadEntry": sysinfoBoardLoadEntry,
       "sysinfoBoardLoadIndex": sysinfoBoardLoadIndex,
       "sysinfoBoardLoadName": sysinfoBoardLoadName,
       "sysinfoBoardLoadLoad1Min": sysinfoBoardLoadLoad1Min,
       "sysinfoBoardLoadLoad5Min": sysinfoBoardLoadLoad5Min,
       "sysinfoBoardLoadLoad15Min": sysinfoBoardLoadLoad15Min,
       "sysinfoBoardMemoryList": sysinfoBoardMemoryList,
       "sysinfoBoardMemoryTable": sysinfoBoardMemoryTable,
       "sysinfoBoardMemoryEntry": sysinfoBoardMemoryEntry,
       "sysinfoBoardMemoryIndex": sysinfoBoardMemoryIndex,
       "sysinfoBoardMemoryName": sysinfoBoardMemoryName,
       "sysinfoBoardMemoryTotalMem": sysinfoBoardMemoryTotalMem,
       "sysinfoBoardMemoryFreeMem": sysinfoBoardMemoryFreeMem,
       "sysinfoBoardMemoryAvailableMem": sysinfoBoardMemoryAvailableMem,
       "sysinfoBoardMemoryUsageMemPercent": sysinfoBoardMemoryUsageMemPercent,
       "sysinfoBoardProcessList": sysinfoBoardProcessList,
       "sysinfoBoardProcessTable": sysinfoBoardProcessTable,
       "sysinfoBoardProcessEntry": sysinfoBoardProcessEntry,
       "sysinfoBoardProcessIndex": sysinfoBoardProcessIndex,
       "sysinfoBoardProcessName": sysinfoBoardProcessName,
       "sysinfoBoardProcessProcessName": sysinfoBoardProcessProcessName,
       "sysinfoBoardProcessPid": sysinfoBoardProcessPid,
       "sysinfoBoardProcessVmSize": sysinfoBoardProcessVmSize,
       "sysinfoBoardProcessVmRSS": sysinfoBoardProcessVmRSS,
       "sysinfoBoardProcessSetReference": sysinfoBoardProcessSetReference,
       "sysinfoBoardProcessVmSizeReference": sysinfoBoardProcessVmSizeReference,
       "sysinfoBoardProcessVmRSSReference": sysinfoBoardProcessVmRSSReference,
       "sysinfoBoardProcessVmSizeDiff": sysinfoBoardProcessVmSizeDiff,
       "sysinfoBoardProcessVmRSSDiff": sysinfoBoardProcessVmRSSDiff,
       "sysinfoBoardProcessReferenceTime": sysinfoBoardProcessReferenceTime}
)
