# SNMP MIB module (H3C-MDC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-MDC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:36 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cMDC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136)
)
if mibBuilder.loadTexts:
    h3cMDC.setRevisions(
        ("2013-03-05 14:48",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cMdcActionValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )



class H3cMdcRunStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("active", 3),
          ("stopping", 4),
          ("updating", 5))
    )



# MIB Managed Objects in the order of their OIDs

_H3cMDCScalarObjects_ObjectIdentity = ObjectIdentity
h3cMDCScalarObjects = _H3cMDCScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 1)
)
_H3cMDCMaxMDCNum_Type = Integer32
_H3cMDCMaxMDCNum_Object = MibScalar
h3cMDCMaxMDCNum = _H3cMDCMaxMDCNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 1, 1),
    _H3cMDCMaxMDCNum_Type()
)
h3cMDCMaxMDCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCMaxMDCNum.setStatus("current")
_H3cMDCCurrentMDCNum_Type = Integer32
_H3cMDCCurrentMDCNum_Object = MibScalar
h3cMDCCurrentMDCNum = _H3cMDCCurrentMDCNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 1, 2),
    _H3cMDCCurrentMDCNum_Type()
)
h3cMDCCurrentMDCNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCCurrentMDCNum.setStatus("current")
_H3cMDCTables_ObjectIdentity = ObjectIdentity
h3cMDCTables = _H3cMDCTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2)
)
_H3cMDCControl_ObjectIdentity = ObjectIdentity
h3cMDCControl = _H3cMDCControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1)
)
_H3cMDCControlTable_Object = MibTable
h3cMDCControlTable = _H3cMDCControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cMDCControlTable.setStatus("current")
_H3cMDCControlEntry_Object = MibTableRow
h3cMDCControlEntry = _H3cMDCControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1, 1)
)
h3cMDCControlEntry.setIndexNames(
    (0, "H3C-MDC-MIB", "h3cMDCIndex"),
)
if mibBuilder.loadTexts:
    h3cMDCControlEntry.setStatus("current")


class _H3cMDCIndex_Type(Integer32):
    """Custom type h3cMDCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cMDCIndex_Type.__name__ = "Integer32"
_H3cMDCIndex_Object = MibTableColumn
h3cMDCIndex = _H3cMDCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1, 1, 1),
    _H3cMDCIndex_Type()
)
h3cMDCIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMDCIndex.setStatus("current")


class _H3cMDCName_Type(DisplayString):
    """Custom type h3cMDCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cMDCName_Type.__name__ = "DisplayString"
_H3cMDCName_Object = MibTableColumn
h3cMDCName = _H3cMDCName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1, 1, 2),
    _H3cMDCName_Type()
)
h3cMDCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMDCName.setStatus("current")


class _H3cMDCAction_Type(H3cMdcActionValue):
    """Custom type h3cMDCAction based on H3cMdcActionValue"""
    defaultValue = 2


_H3cMDCAction_Type.__name__ = "H3cMdcActionValue"
_H3cMDCAction_Object = MibTableColumn
h3cMDCAction = _H3cMDCAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1, 1, 3),
    _H3cMDCAction_Type()
)
h3cMDCAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCAction.setStatus("current")
_H3cMDCStatus_Type = H3cMdcRunStatus
_H3cMDCStatus_Object = MibTableColumn
h3cMDCStatus = _H3cMDCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1, 1, 4),
    _H3cMDCStatus_Type()
)
h3cMDCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCStatus.setStatus("current")
_H3cMDCRowStatus_Type = RowStatus
_H3cMDCRowStatus_Object = MibTableColumn
h3cMDCRowStatus = _H3cMDCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 1, 1, 1, 5),
    _H3cMDCRowStatus_Type()
)
h3cMDCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMDCRowStatus.setStatus("current")
_H3cMDCResource_ObjectIdentity = ObjectIdentity
h3cMDCResource = _H3cMDCResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2)
)
_H3cMDCDISKResourceTable_Object = MibTable
h3cMDCDISKResourceTable = _H3cMDCDISKResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMDCDISKResourceTable.setStatus("current")
_H3cMDCDISKResourceEntry_Object = MibTableRow
h3cMDCDISKResourceEntry = _H3cMDCDISKResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1)
)
h3cMDCDISKResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "H3C-MDC-MIB", "h3cMDCIndex"),
    (0, "H3C-MDC-MIB", "h3cMDCDISKResourceInstance"),
)
if mibBuilder.loadTexts:
    h3cMDCDISKResourceEntry.setStatus("current")


class _H3cMDCDISKResourceInstance_Type(Integer32):
    """Custom type h3cMDCDISKResourceInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cMDCDISKResourceInstance_Type.__name__ = "Integer32"
_H3cMDCDISKResourceInstance_Object = MibTableColumn
h3cMDCDISKResourceInstance = _H3cMDCDISKResourceInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 1),
    _H3cMDCDISKResourceInstance_Type()
)
h3cMDCDISKResourceInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceInstance.setStatus("current")


class _H3cMDCDISKResourceInstanceName_Type(DisplayString):
    """Custom type h3cMDCDISKResourceInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cMDCDISKResourceInstanceName_Type.__name__ = "DisplayString"
_H3cMDCDISKResourceInstanceName_Object = MibTableColumn
h3cMDCDISKResourceInstanceName = _H3cMDCDISKResourceInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 2),
    _H3cMDCDISKResourceInstanceName_Type()
)
h3cMDCDISKResourceInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceInstanceName.setStatus("current")


class _H3cMDCDISKResourceMinLimit_Type(Integer32):
    """Custom type h3cMDCDISKResourceMinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cMDCDISKResourceMinLimit_Type.__name__ = "Integer32"
_H3cMDCDISKResourceMinLimit_Object = MibTableColumn
h3cMDCDISKResourceMinLimit = _H3cMDCDISKResourceMinLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 3),
    _H3cMDCDISKResourceMinLimit_Type()
)
h3cMDCDISKResourceMinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceMinLimit.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceMinLimit.setUnits("percent")


class _H3cMDCDISKResourceMaxLimit_Type(Integer32):
    """Custom type h3cMDCDISKResourceMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cMDCDISKResourceMaxLimit_Type.__name__ = "Integer32"
_H3cMDCDISKResourceMaxLimit_Object = MibTableColumn
h3cMDCDISKResourceMaxLimit = _H3cMDCDISKResourceMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 4),
    _H3cMDCDISKResourceMaxLimit_Type()
)
h3cMDCDISKResourceMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceMaxLimit.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceMaxLimit.setUnits("percent")
_H3cMDCDISKResourceReserve_Type = Unsigned32
_H3cMDCDISKResourceReserve_Object = MibTableColumn
h3cMDCDISKResourceReserve = _H3cMDCDISKResourceReserve_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 5),
    _H3cMDCDISKResourceReserve_Type()
)
h3cMDCDISKResourceReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceReserve.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceReserve.setUnits("KB")
_H3cMDCDISKResourceQuota_Type = Unsigned32
_H3cMDCDISKResourceQuota_Object = MibTableColumn
h3cMDCDISKResourceQuota = _H3cMDCDISKResourceQuota_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 6),
    _H3cMDCDISKResourceQuota_Type()
)
h3cMDCDISKResourceQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceQuota.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceQuota.setUnits("KB")
_H3cMDCDISKResourceUsage_Type = Unsigned32
_H3cMDCDISKResourceUsage_Object = MibTableColumn
h3cMDCDISKResourceUsage = _H3cMDCDISKResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 7),
    _H3cMDCDISKResourceUsage_Type()
)
h3cMDCDISKResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceUsage.setUnits("KB")
_H3cMDCDISKResourceAvailable_Type = Unsigned32
_H3cMDCDISKResourceAvailable_Object = MibTableColumn
h3cMDCDISKResourceAvailable = _H3cMDCDISKResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 1, 1, 8),
    _H3cMDCDISKResourceAvailable_Type()
)
h3cMDCDISKResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceAvailable.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCDISKResourceAvailable.setUnits("KB")
_H3cMDCMemoryResourceTable_Object = MibTable
h3cMDCMemoryResourceTable = _H3cMDCMemoryResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2)
)
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceTable.setStatus("current")
_H3cMDCMemoryResourceEntry_Object = MibTableRow
h3cMDCMemoryResourceEntry = _H3cMDCMemoryResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1)
)
h3cMDCMemoryResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "H3C-MDC-MIB", "h3cMDCIndex"),
)
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceEntry.setStatus("current")


class _H3cMDCMemoryResourceMinLimit_Type(Integer32):
    """Custom type h3cMDCMemoryResourceMinLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cMDCMemoryResourceMinLimit_Type.__name__ = "Integer32"
_H3cMDCMemoryResourceMinLimit_Object = MibTableColumn
h3cMDCMemoryResourceMinLimit = _H3cMDCMemoryResourceMinLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1, 1),
    _H3cMDCMemoryResourceMinLimit_Type()
)
h3cMDCMemoryResourceMinLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceMinLimit.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceMinLimit.setUnits("percent")


class _H3cMDCMemoryResourceMaxLimit_Type(Integer32):
    """Custom type h3cMDCMemoryResourceMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cMDCMemoryResourceMaxLimit_Type.__name__ = "Integer32"
_H3cMDCMemoryResourceMaxLimit_Object = MibTableColumn
h3cMDCMemoryResourceMaxLimit = _H3cMDCMemoryResourceMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1, 2),
    _H3cMDCMemoryResourceMaxLimit_Type()
)
h3cMDCMemoryResourceMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceMaxLimit.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceMaxLimit.setUnits("percent")
_H3cMDCMemoryResourceReserve_Type = Unsigned32
_H3cMDCMemoryResourceReserve_Object = MibTableColumn
h3cMDCMemoryResourceReserve = _H3cMDCMemoryResourceReserve_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1, 3),
    _H3cMDCMemoryResourceReserve_Type()
)
h3cMDCMemoryResourceReserve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceReserve.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceReserve.setUnits("KB")
_H3cMDCMemoryResourceQuota_Type = Unsigned32
_H3cMDCMemoryResourceQuota_Object = MibTableColumn
h3cMDCMemoryResourceQuota = _H3cMDCMemoryResourceQuota_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1, 4),
    _H3cMDCMemoryResourceQuota_Type()
)
h3cMDCMemoryResourceQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceQuota.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceQuota.setUnits("KB")
_H3cMDCMemoryResourceUsage_Type = Unsigned32
_H3cMDCMemoryResourceUsage_Object = MibTableColumn
h3cMDCMemoryResourceUsage = _H3cMDCMemoryResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1, 5),
    _H3cMDCMemoryResourceUsage_Type()
)
h3cMDCMemoryResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceUsage.setUnits("KB")
_H3cMDCMemoryResourceAvailable_Type = Unsigned32
_H3cMDCMemoryResourceAvailable_Object = MibTableColumn
h3cMDCMemoryResourceAvailable = _H3cMDCMemoryResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 2, 1, 6),
    _H3cMDCMemoryResourceAvailable_Type()
)
h3cMDCMemoryResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceAvailable.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCMemoryResourceAvailable.setUnits("KB")
_H3cMDCCPUResourceTable_Object = MibTable
h3cMDCCPUResourceTable = _H3cMDCCPUResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 3)
)
if mibBuilder.loadTexts:
    h3cMDCCPUResourceTable.setStatus("current")
_H3cMDCCPUResourceEntry_Object = MibTableRow
h3cMDCCPUResourceEntry = _H3cMDCCPUResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 3, 1)
)
h3cMDCCPUResourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "H3C-MDC-MIB", "h3cMDCIndex"),
)
if mibBuilder.loadTexts:
    h3cMDCCPUResourceEntry.setStatus("current")


class _H3cMDCCPUResourceLimit_Type(Integer32):
    """Custom type h3cMDCCPUResourceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_H3cMDCCPUResourceLimit_Type.__name__ = "Integer32"
_H3cMDCCPUResourceLimit_Object = MibTableColumn
h3cMDCCPUResourceLimit = _H3cMDCCPUResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 3, 1, 1),
    _H3cMDCCPUResourceLimit_Type()
)
h3cMDCCPUResourceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCCPUResourceLimit.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCCPUResourceLimit.setUnits("weight")


class _H3cMDCCPUResourceUsage_Type(Integer32):
    """Custom type h3cMDCCPUResourceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cMDCCPUResourceUsage_Type.__name__ = "Integer32"
_H3cMDCCPUResourceUsage_Object = MibTableColumn
h3cMDCCPUResourceUsage = _H3cMDCCPUResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 2, 3, 1, 2),
    _H3cMDCCPUResourceUsage_Type()
)
h3cMDCCPUResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCCPUResourceUsage.setStatus("current")
if mibBuilder.loadTexts:
    h3cMDCCPUResourceUsage.setUnits("percent")
_H3cMDCLocation_ObjectIdentity = ObjectIdentity
h3cMDCLocation = _H3cMDCLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 3)
)
_H3cMDCLocationTable_Object = MibTable
h3cMDCLocationTable = _H3cMDCLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 3, 1)
)
if mibBuilder.loadTexts:
    h3cMDCLocationTable.setStatus("current")
_H3cMDCLocationEntry_Object = MibTableRow
h3cMDCLocationEntry = _H3cMDCLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 3, 1, 1)
)
h3cMDCLocationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "H3C-MDC-MIB", "h3cMDCIndex"),
)
if mibBuilder.loadTexts:
    h3cMDCLocationEntry.setStatus("current")
_H3cMDCLocationStatus_Type = TruthValue
_H3cMDCLocationStatus_Object = MibTableColumn
h3cMDCLocationStatus = _H3cMDCLocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 3, 1, 1, 1),
    _H3cMDCLocationStatus_Type()
)
h3cMDCLocationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCLocationStatus.setStatus("current")
_H3cMDCAllocate_ObjectIdentity = ObjectIdentity
h3cMDCAllocate = _H3cMDCAllocate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4)
)
_H3cMDCGroupIfTable_Object = MibTable
h3cMDCGroupIfTable = _H3cMDCGroupIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 1)
)
if mibBuilder.loadTexts:
    h3cMDCGroupIfTable.setStatus("current")
_H3cMDCGroupIfEntry_Object = MibTableRow
h3cMDCGroupIfEntry = _H3cMDCGroupIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 1, 1)
)
h3cMDCGroupIfEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    h3cMDCGroupIfEntry.setStatus("current")
_H3cMDCGroupIdentity_Type = Integer32
_H3cMDCGroupIdentity_Object = MibTableColumn
h3cMDCGroupIdentity = _H3cMDCGroupIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 1, 1, 2),
    _H3cMDCGroupIdentity_Type()
)
h3cMDCGroupIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCGroupIdentity.setStatus("current")
_H3cMDCAllocateTable_Object = MibTable
h3cMDCAllocateTable = _H3cMDCAllocateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 2)
)
if mibBuilder.loadTexts:
    h3cMDCAllocateTable.setStatus("current")
_H3cMDCAllocateEntry_Object = MibTableRow
h3cMDCAllocateEntry = _H3cMDCAllocateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 2, 1)
)
h3cMDCAllocateEntry.setIndexNames(
    (0, "H3C-MDC-MIB", "h3cMDCAllocateGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cMDCAllocateEntry.setStatus("current")


class _H3cMDCAllocateGroupIndex_Type(Integer32):
    """Custom type h3cMDCAllocateGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_H3cMDCAllocateGroupIndex_Type.__name__ = "Integer32"
_H3cMDCAllocateGroupIndex_Object = MibTableColumn
h3cMDCAllocateGroupIndex = _H3cMDCAllocateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 2, 1, 1),
    _H3cMDCAllocateGroupIndex_Type()
)
h3cMDCAllocateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMDCAllocateGroupIndex.setStatus("current")


class _H3cMDCAllocateGroupDescription_Type(DisplayString):
    """Custom type h3cMDCAllocateGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cMDCAllocateGroupDescription_Type.__name__ = "DisplayString"
_H3cMDCAllocateGroupDescription_Object = MibTableColumn
h3cMDCAllocateGroupDescription = _H3cMDCAllocateGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 2, 1, 2),
    _H3cMDCAllocateGroupDescription_Type()
)
h3cMDCAllocateGroupDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMDCAllocateGroupDescription.setStatus("current")


class _H3cMDCAllocateMDCId_Type(Integer32):
    """Custom type h3cMDCAllocateMDCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cMDCAllocateMDCId_Type.__name__ = "Integer32"
_H3cMDCAllocateMDCId_Object = MibTableColumn
h3cMDCAllocateMDCId = _H3cMDCAllocateMDCId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 2, 4, 2, 1, 3),
    _H3cMDCAllocateMDCId_Type()
)
h3cMDCAllocateMDCId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMDCAllocateMDCId.setStatus("current")
_H3cMDCNotification_ObjectIdentity = ObjectIdentity
h3cMDCNotification = _H3cMDCNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 3)
)
_H3cMDCNotificationObjects_ObjectIdentity = ObjectIdentity
h3cMDCNotificationObjects = _H3cMDCNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 3, 0)
)

# Managed Objects groups


# Notification objects

h3cMDCStateChangeToActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 3, 0, 1)
)
h3cMDCStateChangeToActive.setObjects(
      *(("H3C-MDC-MIB", "h3cMDCIndex"),
        ("H3C-MDC-MIB", "h3cMDCName"))
)
if mibBuilder.loadTexts:
    h3cMDCStateChangeToActive.setStatus(
        "current"
    )

h3cMDCStateChangeToInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 136, 3, 0, 2)
)
h3cMDCStateChangeToInactive.setObjects(
      *(("H3C-MDC-MIB", "h3cMDCIndex"),
        ("H3C-MDC-MIB", "h3cMDCName"))
)
if mibBuilder.loadTexts:
    h3cMDCStateChangeToInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MDC-MIB",
    **{"H3cMdcActionValue": H3cMdcActionValue,
       "H3cMdcRunStatus": H3cMdcRunStatus,
       "h3cMDC": h3cMDC,
       "h3cMDCScalarObjects": h3cMDCScalarObjects,
       "h3cMDCMaxMDCNum": h3cMDCMaxMDCNum,
       "h3cMDCCurrentMDCNum": h3cMDCCurrentMDCNum,
       "h3cMDCTables": h3cMDCTables,
       "h3cMDCControl": h3cMDCControl,
       "h3cMDCControlTable": h3cMDCControlTable,
       "h3cMDCControlEntry": h3cMDCControlEntry,
       "h3cMDCIndex": h3cMDCIndex,
       "h3cMDCName": h3cMDCName,
       "h3cMDCAction": h3cMDCAction,
       "h3cMDCStatus": h3cMDCStatus,
       "h3cMDCRowStatus": h3cMDCRowStatus,
       "h3cMDCResource": h3cMDCResource,
       "h3cMDCDISKResourceTable": h3cMDCDISKResourceTable,
       "h3cMDCDISKResourceEntry": h3cMDCDISKResourceEntry,
       "h3cMDCDISKResourceInstance": h3cMDCDISKResourceInstance,
       "h3cMDCDISKResourceInstanceName": h3cMDCDISKResourceInstanceName,
       "h3cMDCDISKResourceMinLimit": h3cMDCDISKResourceMinLimit,
       "h3cMDCDISKResourceMaxLimit": h3cMDCDISKResourceMaxLimit,
       "h3cMDCDISKResourceReserve": h3cMDCDISKResourceReserve,
       "h3cMDCDISKResourceQuota": h3cMDCDISKResourceQuota,
       "h3cMDCDISKResourceUsage": h3cMDCDISKResourceUsage,
       "h3cMDCDISKResourceAvailable": h3cMDCDISKResourceAvailable,
       "h3cMDCMemoryResourceTable": h3cMDCMemoryResourceTable,
       "h3cMDCMemoryResourceEntry": h3cMDCMemoryResourceEntry,
       "h3cMDCMemoryResourceMinLimit": h3cMDCMemoryResourceMinLimit,
       "h3cMDCMemoryResourceMaxLimit": h3cMDCMemoryResourceMaxLimit,
       "h3cMDCMemoryResourceReserve": h3cMDCMemoryResourceReserve,
       "h3cMDCMemoryResourceQuota": h3cMDCMemoryResourceQuota,
       "h3cMDCMemoryResourceUsage": h3cMDCMemoryResourceUsage,
       "h3cMDCMemoryResourceAvailable": h3cMDCMemoryResourceAvailable,
       "h3cMDCCPUResourceTable": h3cMDCCPUResourceTable,
       "h3cMDCCPUResourceEntry": h3cMDCCPUResourceEntry,
       "h3cMDCCPUResourceLimit": h3cMDCCPUResourceLimit,
       "h3cMDCCPUResourceUsage": h3cMDCCPUResourceUsage,
       "h3cMDCLocation": h3cMDCLocation,
       "h3cMDCLocationTable": h3cMDCLocationTable,
       "h3cMDCLocationEntry": h3cMDCLocationEntry,
       "h3cMDCLocationStatus": h3cMDCLocationStatus,
       "h3cMDCAllocate": h3cMDCAllocate,
       "h3cMDCGroupIfTable": h3cMDCGroupIfTable,
       "h3cMDCGroupIfEntry": h3cMDCGroupIfEntry,
       "h3cMDCGroupIdentity": h3cMDCGroupIdentity,
       "h3cMDCAllocateTable": h3cMDCAllocateTable,
       "h3cMDCAllocateEntry": h3cMDCAllocateEntry,
       "h3cMDCAllocateGroupIndex": h3cMDCAllocateGroupIndex,
       "h3cMDCAllocateGroupDescription": h3cMDCAllocateGroupDescription,
       "h3cMDCAllocateMDCId": h3cMDCAllocateMDCId,
       "h3cMDCNotification": h3cMDCNotification,
       "h3cMDCNotificationObjects": h3cMDCNotificationObjects,
       "h3cMDCStateChangeToActive": h3cMDCStateChangeToActive,
       "h3cMDCStateChangeToInactive": h3cMDCStateChangeToInactive}
)
