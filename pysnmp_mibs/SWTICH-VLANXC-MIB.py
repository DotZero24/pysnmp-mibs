# SNMP MIB module (SWTICH-VLANXC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWTICH-VLANXC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:43 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rcVlanxc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RcVlanxcCurrentEntryCount_Type(Integer32):
    """Custom type rcVlanxcCurrentEntryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RcVlanxcCurrentEntryCount_Type.__name__ = "Integer32"
_RcVlanxcCurrentEntryCount_Object = MibScalar
rcVlanxcCurrentEntryCount = _RcVlanxcCurrentEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 1),
    _RcVlanxcCurrentEntryCount_Type()
)
rcVlanxcCurrentEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcVlanxcCurrentEntryCount.setStatus("current")
_RcVlanxcTable_Object = MibTable
rcVlanxcTable = _RcVlanxcTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2)
)
if mibBuilder.loadTexts:
    rcVlanxcTable.setStatus("current")
_RcVlanxcEntry_Object = MibTableRow
rcVlanxcEntry = _RcVlanxcEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2, 1)
)
rcVlanxcEntry.setIndexNames(
    (0, "SWTICH-VLANXC-MIB", "rcVlanxcOuterVid"),
    (0, "SWTICH-VLANXC-MIB", "rcVlanxcInnerVid"),
)
if mibBuilder.loadTexts:
    rcVlanxcEntry.setStatus("current")


class _RcVlanxcOuterVid_Type(Integer32):
    """Custom type rcVlanxcOuterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcVlanxcOuterVid_Type.__name__ = "Integer32"
_RcVlanxcOuterVid_Object = MibTableColumn
rcVlanxcOuterVid = _RcVlanxcOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2, 1, 1),
    _RcVlanxcOuterVid_Type()
)
rcVlanxcOuterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanxcOuterVid.setStatus("current")


class _RcVlanxcInnerVid_Type(Integer32):
    """Custom type rcVlanxcInnerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4096, 4096),
    )


_RcVlanxcInnerVid_Type.__name__ = "Integer32"
_RcVlanxcInnerVid_Object = MibTableColumn
rcVlanxcInnerVid = _RcVlanxcInnerVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2, 1, 2),
    _RcVlanxcInnerVid_Type()
)
rcVlanxcInnerVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanxcInnerVid.setStatus("current")
_RcVlanxcPort1_Type = Integer32
_RcVlanxcPort1_Object = MibTableColumn
rcVlanxcPort1 = _RcVlanxcPort1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2, 1, 3),
    _RcVlanxcPort1_Type()
)
rcVlanxcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanxcPort1.setStatus("current")
_RcVlanxcPort2_Type = Integer32
_RcVlanxcPort2_Object = MibTableColumn
rcVlanxcPort2 = _RcVlanxcPort2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2, 1, 4),
    _RcVlanxcPort2_Type()
)
rcVlanxcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanxcPort2.setStatus("current")
_RcVlanxcRowStatus_Type = RowStatus
_RcVlanxcRowStatus_Object = MibTableColumn
rcVlanxcRowStatus = _RcVlanxcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 2, 1, 5),
    _RcVlanxcRowStatus_Type()
)
rcVlanxcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanxcRowStatus.setStatus("current")
_RcVlanxcVlanTable_Object = MibTable
rcVlanxcVlanTable = _RcVlanxcVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 3)
)
if mibBuilder.loadTexts:
    rcVlanxcVlanTable.setStatus("current")
_RcVlanxcVlanEntry_Object = MibTableRow
rcVlanxcVlanEntry = _RcVlanxcVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 3, 1)
)
rcVlanxcVlanEntry.setIndexNames(
    (0, "SWTICH-VLANXC-MIB", "rcVlanxcVlanIndex"),
)
if mibBuilder.loadTexts:
    rcVlanxcVlanEntry.setStatus("current")


class _RcVlanxcVlanIndex_Type(Integer32):
    """Custom type rcVlanxcVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcVlanxcVlanIndex_Type.__name__ = "Integer32"
_RcVlanxcVlanIndex_Object = MibTableColumn
rcVlanxcVlanIndex = _RcVlanxcVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 3, 1, 1),
    _RcVlanxcVlanIndex_Type()
)
rcVlanxcVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanxcVlanIndex.setStatus("current")


class _RcVlanxcVlanMode_Type(Integer32):
    """Custom type rcVlanxcVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 0),
          ("vlan-xc", 1),
          ("extend-vlan-xc", 2))
    )


_RcVlanxcVlanMode_Type.__name__ = "Integer32"
_RcVlanxcVlanMode_Object = MibTableColumn
rcVlanxcVlanMode = _RcVlanxcVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 3, 1, 2),
    _RcVlanxcVlanMode_Type()
)
rcVlanxcVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanxcVlanMode.setStatus("current")
_RcVlanxcVlanRowStatus_Type = RowStatus
_RcVlanxcVlanRowStatus_Object = MibTableColumn
rcVlanxcVlanRowStatus = _RcVlanxcVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 72, 3, 1, 3),
    _RcVlanxcVlanRowStatus_Type()
)
rcVlanxcVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanxcVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWTICH-VLANXC-MIB",
    **{"rcVlanxc": rcVlanxc,
       "rcVlanxcCurrentEntryCount": rcVlanxcCurrentEntryCount,
       "rcVlanxcTable": rcVlanxcTable,
       "rcVlanxcEntry": rcVlanxcEntry,
       "rcVlanxcOuterVid": rcVlanxcOuterVid,
       "rcVlanxcInnerVid": rcVlanxcInnerVid,
       "rcVlanxcPort1": rcVlanxcPort1,
       "rcVlanxcPort2": rcVlanxcPort2,
       "rcVlanxcRowStatus": rcVlanxcRowStatus,
       "rcVlanxcVlanTable": rcVlanxcVlanTable,
       "rcVlanxcVlanEntry": rcVlanxcVlanEntry,
       "rcVlanxcVlanIndex": rcVlanxcVlanIndex,
       "rcVlanxcVlanMode": rcVlanxcVlanMode,
       "rcVlanxcVlanRowStatus": rcVlanxcVlanRowStatus}
)
