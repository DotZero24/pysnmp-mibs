# SNMP MIB module (RAISECOM-VLANMACCOPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-VLANMACCOPY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:51 2025
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

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(Vlanset,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "Vlanset")


# MODULE-IDENTITY

rcMacConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcVlanMacCopyMibObjects_ObjectIdentity = ObjectIdentity
rcVlanMacCopyMibObjects = _RcVlanMacCopyMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5)
)
_RcVlanMacCopyTable_Object = MibTable
rcVlanMacCopyTable = _RcVlanMacCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    rcVlanMacCopyTable.setStatus("current")
_RcVlanMacCopyEntry_Object = MibTableRow
rcVlanMacCopyEntry = _RcVlanMacCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1)
)
rcVlanMacCopyEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-VLANMACCOPY-MIB", "rcMacCopyTableIndex"),
)
if mibBuilder.loadTexts:
    rcVlanMacCopyEntry.setStatus("current")
_RcMacCopyTableIndex_Type = Integer32
_RcMacCopyTableIndex_Object = MibTableColumn
rcMacCopyTableIndex = _RcMacCopyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 1),
    _RcMacCopyTableIndex_Type()
)
rcMacCopyTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMacCopyTableIndex.setStatus("current")
_RcMacCopyDestVlanList_Type = Vlanset
_RcMacCopyDestVlanList_Object = MibTableColumn
rcMacCopyDestVlanList = _RcMacCopyDestVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 2),
    _RcMacCopyDestVlanList_Type()
)
rcMacCopyDestVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMacCopyDestVlanList.setStatus("current")
_RcMacCopySourceVlanList_Type = Vlanset
_RcMacCopySourceVlanList_Object = MibTableColumn
rcMacCopySourceVlanList = _RcMacCopySourceVlanList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 3),
    _RcMacCopySourceVlanList_Type()
)
rcMacCopySourceVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMacCopySourceVlanList.setStatus("current")
_RcMacCopyRowStatus_Type = RowStatus
_RcMacCopyRowStatus_Object = MibTableColumn
rcMacCopyRowStatus = _RcMacCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 3, 5, 1, 1, 4),
    _RcMacCopyRowStatus_Type()
)
rcMacCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMacCopyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-VLANMACCOPY-MIB",
    **{"rcMacConfig": rcMacConfig,
       "rcVlanMacCopyMibObjects": rcVlanMacCopyMibObjects,
       "rcVlanMacCopyTable": rcVlanMacCopyTable,
       "rcVlanMacCopyEntry": rcVlanMacCopyEntry,
       "rcMacCopyTableIndex": rcMacCopyTableIndex,
       "rcMacCopyDestVlanList": rcMacCopyDestVlanList,
       "rcMacCopySourceVlanList": rcMacCopySourceVlanList,
       "rcMacCopyRowStatus": rcMacCopyRowStatus}
)
