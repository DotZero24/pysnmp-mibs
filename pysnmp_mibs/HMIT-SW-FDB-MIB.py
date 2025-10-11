# SNMP MIB module (HMIT-SW-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SW-FDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:16 2025
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

(hmITSwitchTech,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITSwitchTech")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmITSwFDB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12)
)
if mibBuilder.loadTexts:
    hmITSwFDB.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HmITSwFDBAgingTime_Type(Integer32):
    """Custom type hmITSwFDBAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HmITSwFDBAgingTime_Type.__name__ = "Integer32"
_HmITSwFDBAgingTime_Object = MibScalar
hmITSwFDBAgingTime = _HmITSwFDBAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 1),
    _HmITSwFDBAgingTime_Type()
)
hmITSwFDBAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBAgingTime.setStatus("current")


class _HmITSwFDBSytemMacLimit_Type(Integer32):
    """Custom type hmITSwFDBSytemMacLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HmITSwFDBSytemMacLimit_Type.__name__ = "Integer32"
_HmITSwFDBSytemMacLimit_Object = MibScalar
hmITSwFDBSytemMacLimit = _HmITSwFDBSytemMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 2),
    _HmITSwFDBSytemMacLimit_Type()
)
hmITSwFDBSytemMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBSytemMacLimit.setStatus("current")
_HmITSwFDBVlanMacLearnTable_Object = MibTable
hmITSwFDBVlanMacLearnTable = _HmITSwFDBVlanMacLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 3)
)
if mibBuilder.loadTexts:
    hmITSwFDBVlanMacLearnTable.setStatus("current")
_HmITSwFDBVlanMacLearnEntry_Object = MibTableRow
hmITSwFDBVlanMacLearnEntry = _HmITSwFDBVlanMacLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 3, 1)
)
hmITSwFDBVlanMacLearnEntry.setIndexNames(
    (0, "HMIT-SW-FDB-MIB", "hmITSwFDBmacLearnVlan"),
)
if mibBuilder.loadTexts:
    hmITSwFDBVlanMacLearnEntry.setStatus("current")


class _HmITSwFDBmacLearnVlan_Type(Integer32):
    """Custom type hmITSwFDBmacLearnVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HmITSwFDBmacLearnVlan_Type.__name__ = "Integer32"
_HmITSwFDBmacLearnVlan_Object = MibTableColumn
hmITSwFDBmacLearnVlan = _HmITSwFDBmacLearnVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 3, 1, 1),
    _HmITSwFDBmacLearnVlan_Type()
)
hmITSwFDBmacLearnVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSwFDBmacLearnVlan.setStatus("current")


class _HmITSwFDBmacLearnNum_Type(Integer32):
    """Custom type hmITSwFDBmacLearnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HmITSwFDBmacLearnNum_Type.__name__ = "Integer32"
_HmITSwFDBmacLearnNum_Object = MibTableColumn
hmITSwFDBmacLearnNum = _HmITSwFDBmacLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 3, 1, 2),
    _HmITSwFDBmacLearnNum_Type()
)
hmITSwFDBmacLearnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBmacLearnNum.setStatus("current")
_HmITSwFDBmacLearnStatus_Type = RowStatus
_HmITSwFDBmacLearnStatus_Object = MibTableColumn
hmITSwFDBmacLearnStatus = _HmITSwFDBmacLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 3, 1, 3),
    _HmITSwFDBmacLearnStatus_Type()
)
hmITSwFDBmacLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBmacLearnStatus.setStatus("current")
_HmITSwFDBPortMacLearnTable_Object = MibTable
hmITSwFDBPortMacLearnTable = _HmITSwFDBPortMacLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 9)
)
if mibBuilder.loadTexts:
    hmITSwFDBPortMacLearnTable.setStatus("current")
_HmITSwFDBPortMacLearnEntry_Object = MibTableRow
hmITSwFDBPortMacLearnEntry = _HmITSwFDBPortMacLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 9, 1)
)
hmITSwFDBPortMacLearnEntry.setIndexNames(
    (0, "HMIT-SW-FDB-MIB", "hmITSwFDBmacLearnPort"),
)
if mibBuilder.loadTexts:
    hmITSwFDBPortMacLearnEntry.setStatus("current")


class _HmITSwFDBmacLearnPort_Type(Integer32):
    """Custom type hmITSwFDBmacLearnPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmITSwFDBmacLearnPort_Type.__name__ = "Integer32"
_HmITSwFDBmacLearnPort_Object = MibTableColumn
hmITSwFDBmacLearnPort = _HmITSwFDBmacLearnPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 9, 1, 1),
    _HmITSwFDBmacLearnPort_Type()
)
hmITSwFDBmacLearnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSwFDBmacLearnPort.setStatus("current")


class _HmITSwFDBPortmacLearnNum_Type(Integer32):
    """Custom type hmITSwFDBPortmacLearnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_HmITSwFDBPortmacLearnNum_Type.__name__ = "Integer32"
_HmITSwFDBPortmacLearnNum_Object = MibTableColumn
hmITSwFDBPortmacLearnNum = _HmITSwFDBPortmacLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 9, 1, 2),
    _HmITSwFDBPortmacLearnNum_Type()
)
hmITSwFDBPortmacLearnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBPortmacLearnNum.setStatus("current")
_HmITSwFDBPortmacLearnStatus_Type = RowStatus
_HmITSwFDBPortmacLearnStatus_Object = MibTableColumn
hmITSwFDBPortmacLearnStatus = _HmITSwFDBPortmacLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 9, 1, 3),
    _HmITSwFDBPortmacLearnStatus_Type()
)
hmITSwFDBPortmacLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBPortmacLearnStatus.setStatus("current")
_HmITSwFDBFdbTable_Object = MibTable
hmITSwFDBFdbTable = _HmITSwFDBFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10)
)
if mibBuilder.loadTexts:
    hmITSwFDBFdbTable.setStatus("current")
_HmITSwFDBFdbEntry_Object = MibTableRow
hmITSwFDBFdbEntry = _HmITSwFDBFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1)
)
hmITSwFDBFdbEntry.setIndexNames(
    (0, "HMIT-SW-FDB-MIB", "hmITSwFDBfdbMacAddr"),
    (0, "HMIT-SW-FDB-MIB", "hmITSwFDBfdbVlanId"),
    (0, "HMIT-SW-FDB-MIB", "hmITSwFDBfdbPort"),
    (0, "HMIT-SW-FDB-MIB", "hmITSwFDBfdbType"),
)
if mibBuilder.loadTexts:
    hmITSwFDBFdbEntry.setStatus("current")
_HmITSwFDBfdbMacAddr_Type = MacAddress
_HmITSwFDBfdbMacAddr_Object = MibTableColumn
hmITSwFDBfdbMacAddr = _HmITSwFDBfdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1, 1),
    _HmITSwFDBfdbMacAddr_Type()
)
hmITSwFDBfdbMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBfdbMacAddr.setStatus("current")


class _HmITSwFDBfdbVlanId_Type(Integer32):
    """Custom type hmITSwFDBfdbVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HmITSwFDBfdbVlanId_Type.__name__ = "Integer32"
_HmITSwFDBfdbVlanId_Object = MibTableColumn
hmITSwFDBfdbVlanId = _HmITSwFDBfdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1, 2),
    _HmITSwFDBfdbVlanId_Type()
)
hmITSwFDBfdbVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBfdbVlanId.setStatus("current")


class _HmITSwFDBfdbPort_Type(Integer32):
    """Custom type hmITSwFDBfdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmITSwFDBfdbPort_Type.__name__ = "Integer32"
_HmITSwFDBfdbPort_Object = MibTableColumn
hmITSwFDBfdbPort = _HmITSwFDBfdbPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1, 3),
    _HmITSwFDBfdbPort_Type()
)
hmITSwFDBfdbPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBfdbPort.setStatus("current")


class _HmITSwFDBfdbType_Type(Integer32):
    """Custom type hmITSwFDBfdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HmITSwFDBfdbType_Type.__name__ = "Integer32"
_HmITSwFDBfdbType_Object = MibTableColumn
hmITSwFDBfdbType = _HmITSwFDBfdbType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1, 4),
    _HmITSwFDBfdbType_Type()
)
hmITSwFDBfdbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBfdbType.setStatus("current")


class _HmITSwFDBfdbState_Type(Integer32):
    """Custom type hmITSwFDBfdbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HmITSwFDBfdbState_Type.__name__ = "Integer32"
_HmITSwFDBfdbState_Object = MibTableColumn
hmITSwFDBfdbState = _HmITSwFDBfdbState_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1, 5),
    _HmITSwFDBfdbState_Type()
)
hmITSwFDBfdbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSwFDBfdbState.setStatus("current")
_HmITSwFDBfdbStatus_Type = RowStatus
_HmITSwFDBfdbStatus_Object = MibTableColumn
hmITSwFDBfdbStatus = _HmITSwFDBfdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 10, 1, 6),
    _HmITSwFDBfdbStatus_Type()
)
hmITSwFDBfdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSwFDBfdbStatus.setStatus("current")


class _HmITSwFDBDelPortindex_Type(Integer32):
    """Custom type hmITSwFDBDelPortindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HmITSwFDBDelPortindex_Type.__name__ = "Integer32"
_HmITSwFDBDelPortindex_Object = MibScalar
hmITSwFDBDelPortindex = _HmITSwFDBDelPortindex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 13),
    _HmITSwFDBDelPortindex_Type()
)
hmITSwFDBDelPortindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBDelPortindex.setStatus("current")


class _HmITSwFDBDelVlanindex_Type(Integer32):
    """Custom type hmITSwFDBDelVlanindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HmITSwFDBDelVlanindex_Type.__name__ = "Integer32"
_HmITSwFDBDelVlanindex_Object = MibScalar
hmITSwFDBDelVlanindex = _HmITSwFDBDelVlanindex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 14),
    _HmITSwFDBDelVlanindex_Type()
)
hmITSwFDBDelVlanindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBDelVlanindex.setStatus("current")


class _HmITSwFDBDelPortVlanindex_Type(DisplayString):
    """Custom type hmITSwFDBDelPortVlanindex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_HmITSwFDBDelPortVlanindex_Type.__name__ = "DisplayString"
_HmITSwFDBDelPortVlanindex_Object = MibScalar
hmITSwFDBDelPortVlanindex = _HmITSwFDBDelPortVlanindex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 12, 15),
    _HmITSwFDBDelPortVlanindex_Type()
)
hmITSwFDBDelPortVlanindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmITSwFDBDelPortVlanindex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SW-FDB-MIB",
    **{"hmITSwFDB": hmITSwFDB,
       "hmITSwFDBAgingTime": hmITSwFDBAgingTime,
       "hmITSwFDBSytemMacLimit": hmITSwFDBSytemMacLimit,
       "hmITSwFDBVlanMacLearnTable": hmITSwFDBVlanMacLearnTable,
       "hmITSwFDBVlanMacLearnEntry": hmITSwFDBVlanMacLearnEntry,
       "hmITSwFDBmacLearnVlan": hmITSwFDBmacLearnVlan,
       "hmITSwFDBmacLearnNum": hmITSwFDBmacLearnNum,
       "hmITSwFDBmacLearnStatus": hmITSwFDBmacLearnStatus,
       "hmITSwFDBPortMacLearnTable": hmITSwFDBPortMacLearnTable,
       "hmITSwFDBPortMacLearnEntry": hmITSwFDBPortMacLearnEntry,
       "hmITSwFDBmacLearnPort": hmITSwFDBmacLearnPort,
       "hmITSwFDBPortmacLearnNum": hmITSwFDBPortmacLearnNum,
       "hmITSwFDBPortmacLearnStatus": hmITSwFDBPortmacLearnStatus,
       "hmITSwFDBFdbTable": hmITSwFDBFdbTable,
       "hmITSwFDBFdbEntry": hmITSwFDBFdbEntry,
       "hmITSwFDBfdbMacAddr": hmITSwFDBfdbMacAddr,
       "hmITSwFDBfdbVlanId": hmITSwFDBfdbVlanId,
       "hmITSwFDBfdbPort": hmITSwFDBfdbPort,
       "hmITSwFDBfdbType": hmITSwFDBfdbType,
       "hmITSwFDBfdbState": hmITSwFDBfdbState,
       "hmITSwFDBfdbStatus": hmITSwFDBfdbStatus,
       "hmITSwFDBDelPortindex": hmITSwFDBDelPortindex,
       "hmITSwFDBDelVlanindex": hmITSwFDBDelVlanindex,
       "hmITSwFDBDelPortVlanindex": hmITSwFDBDelPortVlanindex}
)
