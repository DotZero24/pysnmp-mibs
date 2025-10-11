# SNMP MIB module (QTECH-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MEMORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:16 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechMemoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35)
)
if mibBuilder.loadTexts:
    qtechMemoryMIB.setRevisions(
        ("2003-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Percent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_QtechMemoryPoolMIBObjects_ObjectIdentity = ObjectIdentity
qtechMemoryPoolMIBObjects = _QtechMemoryPoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1)
)
_QtechMemoryPoolUtilizationTable_Object = MibTable
qtechMemoryPoolUtilizationTable = _QtechMemoryPoolUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    qtechMemoryPoolUtilizationTable.setStatus("current")
_QtechMemoryPoolUtilizationEntry_Object = MibTableRow
qtechMemoryPoolUtilizationEntry = _QtechMemoryPoolUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1)
)
qtechMemoryPoolUtilizationEntry.setIndexNames(
    (0, "QTECH-MEMORY-MIB", "qtechMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    qtechMemoryPoolUtilizationEntry.setStatus("current")
_QtechMemoryPoolIndex_Type = Integer32
_QtechMemoryPoolIndex_Object = MibTableColumn
qtechMemoryPoolIndex = _QtechMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 1),
    _QtechMemoryPoolIndex_Type()
)
qtechMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolIndex.setStatus("current")
_QtechMemoryPoolName_Type = DisplayString
_QtechMemoryPoolName_Object = MibTableColumn
qtechMemoryPoolName = _QtechMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 2),
    _QtechMemoryPoolName_Type()
)
qtechMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolName.setStatus("current")
_QtechMemoryPoolCurrentUtilization_Type = Percent
_QtechMemoryPoolCurrentUtilization_Object = MibTableColumn
qtechMemoryPoolCurrentUtilization = _QtechMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 3),
    _QtechMemoryPoolCurrentUtilization_Type()
)
qtechMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolCurrentUtilization.setStatus("current")
_QtechMemoryPoolLowestUtilization_Type = Percent
_QtechMemoryPoolLowestUtilization_Object = MibTableColumn
qtechMemoryPoolLowestUtilization = _QtechMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 4),
    _QtechMemoryPoolLowestUtilization_Type()
)
qtechMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolLowestUtilization.setStatus("current")
_QtechMemoryPoolLargestUtilization_Type = Percent
_QtechMemoryPoolLargestUtilization_Object = MibTableColumn
qtechMemoryPoolLargestUtilization = _QtechMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 5),
    _QtechMemoryPoolLargestUtilization_Type()
)
qtechMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolLargestUtilization.setStatus("current")
_QtechMemoryPoolSize_Type = Integer32
_QtechMemoryPoolSize_Object = MibTableColumn
qtechMemoryPoolSize = _QtechMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 6),
    _QtechMemoryPoolSize_Type()
)
qtechMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolSize.setStatus("current")
_QtechMemoryPoolUsed_Type = Integer32
_QtechMemoryPoolUsed_Object = MibTableColumn
qtechMemoryPoolUsed = _QtechMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 7),
    _QtechMemoryPoolUsed_Type()
)
qtechMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolUsed.setStatus("current")
_QtechMemoryPoolFree_Type = Integer32
_QtechMemoryPoolFree_Object = MibTableColumn
qtechMemoryPoolFree = _QtechMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 8),
    _QtechMemoryPoolFree_Type()
)
qtechMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolFree.setStatus("current")
_QtechMemoryPoolWarning_Type = Percent
_QtechMemoryPoolWarning_Object = MibTableColumn
qtechMemoryPoolWarning = _QtechMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 9),
    _QtechMemoryPoolWarning_Type()
)
qtechMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMemoryPoolWarning.setStatus("current")
_QtechMemoryPoolCritical_Type = Percent
_QtechMemoryPoolCritical_Object = MibTableColumn
qtechMemoryPoolCritical = _QtechMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 10),
    _QtechMemoryPoolCritical_Type()
)
qtechMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMemoryPoolCritical.setStatus("current")
_QtechMemoryPoolAverageUtilization_Type = Percent
_QtechMemoryPoolAverageUtilization_Object = MibTableColumn
qtechMemoryPoolAverageUtilization = _QtechMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 11),
    _QtechMemoryPoolAverageUtilization_Type()
)
qtechMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolAverageUtilization.setStatus("current")
_QtechMemoryPoolTotalSize_Type = Gauge32
_QtechMemoryPoolTotalSize_Object = MibTableColumn
qtechMemoryPoolTotalSize = _QtechMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 12),
    _QtechMemoryPoolTotalSize_Type()
)
qtechMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolTotalSize.setStatus("current")
_QtechMemoryPoolUsedSize_Type = Gauge32
_QtechMemoryPoolUsedSize_Object = MibTableColumn
qtechMemoryPoolUsedSize = _QtechMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 13),
    _QtechMemoryPoolUsedSize_Type()
)
qtechMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolUsedSize.setStatus("current")
_QtechMemoryPoolFreeSize_Type = Gauge32
_QtechMemoryPoolFreeSize_Object = MibTableColumn
qtechMemoryPoolFreeSize = _QtechMemoryPoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 1, 1, 14),
    _QtechMemoryPoolFreeSize_Type()
)
qtechMemoryPoolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMemoryPoolFreeSize.setStatus("current")
_QtechNodeMemoryPoolTable_Object = MibTable
qtechNodeMemoryPoolTable = _QtechNodeMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolTable.setStatus("current")
_QtechNodeMemoryPoolEntry_Object = MibTableRow
qtechNodeMemoryPoolEntry = _QtechNodeMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1)
)
qtechNodeMemoryPoolEntry.setIndexNames(
    (0, "QTECH-MEMORY-MIB", "qtechNodeMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolEntry.setStatus("current")
_QtechNodeMemoryPoolIndex_Type = Integer32
_QtechNodeMemoryPoolIndex_Object = MibTableColumn
qtechNodeMemoryPoolIndex = _QtechNodeMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 1),
    _QtechNodeMemoryPoolIndex_Type()
)
qtechNodeMemoryPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolIndex.setStatus("current")
_QtechNodeMemoryPoolName_Type = DisplayString
_QtechNodeMemoryPoolName_Object = MibTableColumn
qtechNodeMemoryPoolName = _QtechNodeMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 2),
    _QtechNodeMemoryPoolName_Type()
)
qtechNodeMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolName.setStatus("current")
_QtechNodeMemoryPoolCurrentUtilization_Type = Percent
_QtechNodeMemoryPoolCurrentUtilization_Object = MibTableColumn
qtechNodeMemoryPoolCurrentUtilization = _QtechNodeMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 3),
    _QtechNodeMemoryPoolCurrentUtilization_Type()
)
qtechNodeMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolCurrentUtilization.setStatus("current")
_QtechNodeMemoryPoolLowestUtilization_Type = Percent
_QtechNodeMemoryPoolLowestUtilization_Object = MibTableColumn
qtechNodeMemoryPoolLowestUtilization = _QtechNodeMemoryPoolLowestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 4),
    _QtechNodeMemoryPoolLowestUtilization_Type()
)
qtechNodeMemoryPoolLowestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolLowestUtilization.setStatus("current")
_QtechNodeMemoryPoolLargestUtilization_Type = Percent
_QtechNodeMemoryPoolLargestUtilization_Object = MibTableColumn
qtechNodeMemoryPoolLargestUtilization = _QtechNodeMemoryPoolLargestUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 5),
    _QtechNodeMemoryPoolLargestUtilization_Type()
)
qtechNodeMemoryPoolLargestUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolLargestUtilization.setStatus("current")
_QtechNodeMemoryPoolSize_Type = Integer32
_QtechNodeMemoryPoolSize_Object = MibTableColumn
qtechNodeMemoryPoolSize = _QtechNodeMemoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 6),
    _QtechNodeMemoryPoolSize_Type()
)
qtechNodeMemoryPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolSize.setStatus("current")
_QtechNodeMemoryPoolUsed_Type = Integer32
_QtechNodeMemoryPoolUsed_Object = MibTableColumn
qtechNodeMemoryPoolUsed = _QtechNodeMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 7),
    _QtechNodeMemoryPoolUsed_Type()
)
qtechNodeMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolUsed.setStatus("current")
_QtechNodeMemoryPoolFree_Type = Integer32
_QtechNodeMemoryPoolFree_Object = MibTableColumn
qtechNodeMemoryPoolFree = _QtechNodeMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 8),
    _QtechNodeMemoryPoolFree_Type()
)
qtechNodeMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolFree.setStatus("current")
_QtechNodeMemoryPoolWarning_Type = Percent
_QtechNodeMemoryPoolWarning_Object = MibTableColumn
qtechNodeMemoryPoolWarning = _QtechNodeMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 9),
    _QtechNodeMemoryPoolWarning_Type()
)
qtechNodeMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolWarning.setStatus("current")
_QtechNodeMemoryPoolCritical_Type = Percent
_QtechNodeMemoryPoolCritical_Object = MibTableColumn
qtechNodeMemoryPoolCritical = _QtechNodeMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 10),
    _QtechNodeMemoryPoolCritical_Type()
)
qtechNodeMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolCritical.setStatus("current")
_QtechNodeMemoryPoolTotalSize_Type = Gauge32
_QtechNodeMemoryPoolTotalSize_Object = MibTableColumn
qtechNodeMemoryPoolTotalSize = _QtechNodeMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 11),
    _QtechNodeMemoryPoolTotalSize_Type()
)
qtechNodeMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolTotalSize.setStatus("current")
_QtechNodeMemoryPoolUsedSize_Type = Gauge32
_QtechNodeMemoryPoolUsedSize_Object = MibTableColumn
qtechNodeMemoryPoolUsedSize = _QtechNodeMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 12),
    _QtechNodeMemoryPoolUsedSize_Type()
)
qtechNodeMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolUsedSize.setStatus("current")
_QtechNodeMemoryPoolFreeSize_Type = Gauge32
_QtechNodeMemoryPoolFreeSize_Object = MibTableColumn
qtechNodeMemoryPoolFreeSize = _QtechNodeMemoryPoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 2, 1, 13),
    _QtechNodeMemoryPoolFreeSize_Type()
)
qtechNodeMemoryPoolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolFreeSize.setStatus("current")
_QtechLankApMemoryPoolTable_Object = MibTable
qtechLankApMemoryPoolTable = _QtechLankApMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolTable.setStatus("current")
_QtechLankApMemoryPoolEntry_Object = MibTableRow
qtechLankApMemoryPoolEntry = _QtechLankApMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3, 1)
)
qtechLankApMemoryPoolEntry.setIndexNames(
    (0, "QTECH-MEMORY-MIB", "qtechLankApMemoryPoolMacAddr"),
)
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolEntry.setStatus("current")
_QtechLankApMemoryPoolMacAddr_Type = MacAddress
_QtechLankApMemoryPoolMacAddr_Object = MibTableColumn
qtechLankApMemoryPoolMacAddr = _QtechLankApMemoryPoolMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3, 1, 1),
    _QtechLankApMemoryPoolMacAddr_Type()
)
qtechLankApMemoryPoolMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolMacAddr.setStatus("current")
_QtechLankApMemoryPoolWarning_Type = Percent
_QtechLankApMemoryPoolWarning_Object = MibTableColumn
qtechLankApMemoryPoolWarning = _QtechLankApMemoryPoolWarning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3, 1, 2),
    _QtechLankApMemoryPoolWarning_Type()
)
qtechLankApMemoryPoolWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolWarning.setStatus("current")
_QtechLankApMemoryPoolCritical_Type = Percent
_QtechLankApMemoryPoolCritical_Object = MibTableColumn
qtechLankApMemoryPoolCritical = _QtechLankApMemoryPoolCritical_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3, 1, 3),
    _QtechLankApMemoryPoolCritical_Type()
)
qtechLankApMemoryPoolCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolCritical.setStatus("current")
_QtechLankApMemoryPoolCurrentUtilization_Type = Percent
_QtechLankApMemoryPoolCurrentUtilization_Object = MibTableColumn
qtechLankApMemoryPoolCurrentUtilization = _QtechLankApMemoryPoolCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3, 1, 4),
    _QtechLankApMemoryPoolCurrentUtilization_Type()
)
qtechLankApMemoryPoolCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolCurrentUtilization.setStatus("current")
_QtechLankApMemoryPoolAverageUtilization_Type = Percent
_QtechLankApMemoryPoolAverageUtilization_Object = MibTableColumn
qtechLankApMemoryPoolAverageUtilization = _QtechLankApMemoryPoolAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 1, 3, 1, 5),
    _QtechLankApMemoryPoolAverageUtilization_Type()
)
qtechLankApMemoryPoolAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLankApMemoryPoolAverageUtilization.setStatus("current")
_QtechMemoryMIBConformance_ObjectIdentity = ObjectIdentity
qtechMemoryMIBConformance = _QtechMemoryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 2)
)
_QtechMemoryMIBCompliances_ObjectIdentity = ObjectIdentity
qtechMemoryMIBCompliances = _QtechMemoryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 2, 1)
)
_QtechMemoryMIBGroups_ObjectIdentity = ObjectIdentity
qtechMemoryMIBGroups = _QtechMemoryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 2, 2)
)

# Managed Objects groups

qtechMemoryPoolUtilizationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 2, 2, 1)
)
qtechMemoryPoolUtilizationMIBGroup.setObjects(
      *(("QTECH-MEMORY-MIB", "qtechMemoryPoolIndex"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolName"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolCurrentUtilization"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolLowestUtilization"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolLargestUtilization"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolSize"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolUsed"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolFree"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolWarning"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolCritical"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolAverageUtilization"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolTotalSize"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolUsedSize"),
        ("QTECH-MEMORY-MIB", "qtechMemoryPoolFreeSize"))
)
if mibBuilder.loadTexts:
    qtechMemoryPoolUtilizationMIBGroup.setStatus("current")

qtechNodeMemoryPoolMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 2, 2, 2)
)
qtechNodeMemoryPoolMIBGroup.setObjects(
      *(("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolIndex"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolName"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolCurrentUtilization"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolLowestUtilization"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolLargestUtilization"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolSize"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolUsed"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolFree"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolWarning"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolCritical"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolTotalSize"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolUsedSize"),
        ("QTECH-MEMORY-MIB", "qtechNodeMemoryPoolFreeSize"))
)
if mibBuilder.loadTexts:
    qtechNodeMemoryPoolMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechMemoryMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 35, 2, 1, 1)
)
qtechMemoryMIBCompliance.setObjects(
    ("QTECH-MEMORY-MIB", "qtechMemoryPoolUtilizationMIBGroup")
)
if mibBuilder.loadTexts:
    qtechMemoryMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MEMORY-MIB",
    **{"Percent": Percent,
       "qtechMemoryMIB": qtechMemoryMIB,
       "qtechMemoryPoolMIBObjects": qtechMemoryPoolMIBObjects,
       "qtechMemoryPoolUtilizationTable": qtechMemoryPoolUtilizationTable,
       "qtechMemoryPoolUtilizationEntry": qtechMemoryPoolUtilizationEntry,
       "qtechMemoryPoolIndex": qtechMemoryPoolIndex,
       "qtechMemoryPoolName": qtechMemoryPoolName,
       "qtechMemoryPoolCurrentUtilization": qtechMemoryPoolCurrentUtilization,
       "qtechMemoryPoolLowestUtilization": qtechMemoryPoolLowestUtilization,
       "qtechMemoryPoolLargestUtilization": qtechMemoryPoolLargestUtilization,
       "qtechMemoryPoolSize": qtechMemoryPoolSize,
       "qtechMemoryPoolUsed": qtechMemoryPoolUsed,
       "qtechMemoryPoolFree": qtechMemoryPoolFree,
       "qtechMemoryPoolWarning": qtechMemoryPoolWarning,
       "qtechMemoryPoolCritical": qtechMemoryPoolCritical,
       "qtechMemoryPoolAverageUtilization": qtechMemoryPoolAverageUtilization,
       "qtechMemoryPoolTotalSize": qtechMemoryPoolTotalSize,
       "qtechMemoryPoolUsedSize": qtechMemoryPoolUsedSize,
       "qtechMemoryPoolFreeSize": qtechMemoryPoolFreeSize,
       "qtechNodeMemoryPoolTable": qtechNodeMemoryPoolTable,
       "qtechNodeMemoryPoolEntry": qtechNodeMemoryPoolEntry,
       "qtechNodeMemoryPoolIndex": qtechNodeMemoryPoolIndex,
       "qtechNodeMemoryPoolName": qtechNodeMemoryPoolName,
       "qtechNodeMemoryPoolCurrentUtilization": qtechNodeMemoryPoolCurrentUtilization,
       "qtechNodeMemoryPoolLowestUtilization": qtechNodeMemoryPoolLowestUtilization,
       "qtechNodeMemoryPoolLargestUtilization": qtechNodeMemoryPoolLargestUtilization,
       "qtechNodeMemoryPoolSize": qtechNodeMemoryPoolSize,
       "qtechNodeMemoryPoolUsed": qtechNodeMemoryPoolUsed,
       "qtechNodeMemoryPoolFree": qtechNodeMemoryPoolFree,
       "qtechNodeMemoryPoolWarning": qtechNodeMemoryPoolWarning,
       "qtechNodeMemoryPoolCritical": qtechNodeMemoryPoolCritical,
       "qtechNodeMemoryPoolTotalSize": qtechNodeMemoryPoolTotalSize,
       "qtechNodeMemoryPoolUsedSize": qtechNodeMemoryPoolUsedSize,
       "qtechNodeMemoryPoolFreeSize": qtechNodeMemoryPoolFreeSize,
       "qtechLankApMemoryPoolTable": qtechLankApMemoryPoolTable,
       "qtechLankApMemoryPoolEntry": qtechLankApMemoryPoolEntry,
       "qtechLankApMemoryPoolMacAddr": qtechLankApMemoryPoolMacAddr,
       "qtechLankApMemoryPoolWarning": qtechLankApMemoryPoolWarning,
       "qtechLankApMemoryPoolCritical": qtechLankApMemoryPoolCritical,
       "qtechLankApMemoryPoolCurrentUtilization": qtechLankApMemoryPoolCurrentUtilization,
       "qtechLankApMemoryPoolAverageUtilization": qtechLankApMemoryPoolAverageUtilization,
       "qtechMemoryMIBConformance": qtechMemoryMIBConformance,
       "qtechMemoryMIBCompliances": qtechMemoryMIBCompliances,
       "qtechMemoryMIBCompliance": qtechMemoryMIBCompliance,
       "qtechMemoryMIBGroups": qtechMemoryMIBGroups,
       "qtechMemoryPoolUtilizationMIBGroup": qtechMemoryPoolUtilizationMIBGroup,
       "qtechNodeMemoryPoolMIBGroup": qtechNodeMemoryPoolMIBGroup}
)
