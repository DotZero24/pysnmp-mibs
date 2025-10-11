# SNMP MIB module (FS-PATCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PATCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:35 2025
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
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

fsPatchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151)
)
if mibBuilder.loadTexts:
    fsPatchMIB.setRevisions(
        ("2016-09-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPatchMIBObjects_ObjectIdentity = ObjectIdentity
fsPatchMIBObjects = _FsPatchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1)
)
_FsPatchTable_Object = MibTable
fsPatchTable = _FsPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1)
)
if mibBuilder.loadTexts:
    fsPatchTable.setStatus("current")
_FsPatchEntry_Object = MibTableRow
fsPatchEntry = _FsPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1)
)
fsPatchEntry.setIndexNames(
    (0, "FS-PATCH-MIB", "fsPatchDevIndex"),
    (0, "FS-PATCH-MIB", "fsPatchCmpntIndex"),
)
if mibBuilder.loadTexts:
    fsPatchEntry.setStatus("current")
_FsPatchDevIndex_Type = Integer32
_FsPatchDevIndex_Object = MibTableColumn
fsPatchDevIndex = _FsPatchDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 1),
    _FsPatchDevIndex_Type()
)
fsPatchDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchDevIndex.setStatus("current")
_FsPatchCmpntIndex_Type = Integer32
_FsPatchCmpntIndex_Object = MibTableColumn
fsPatchCmpntIndex = _FsPatchCmpntIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 2),
    _FsPatchCmpntIndex_Type()
)
fsPatchCmpntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchCmpntIndex.setStatus("current")
_FsPatchDevId_Type = Integer32
_FsPatchDevId_Object = MibTableColumn
fsPatchDevId = _FsPatchDevId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 3),
    _FsPatchDevId_Type()
)
fsPatchDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchDevId.setStatus("current")
_FsPatchSlotId_Type = Integer32
_FsPatchSlotId_Object = MibTableColumn
fsPatchSlotId = _FsPatchSlotId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 4),
    _FsPatchSlotId_Type()
)
fsPatchSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchSlotId.setStatus("current")
_FsPatchCpuId_Type = Integer32
_FsPatchCpuId_Object = MibTableColumn
fsPatchCpuId = _FsPatchCpuId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 5),
    _FsPatchCpuId_Type()
)
fsPatchCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchCpuId.setStatus("current")
_FsPatchExist_Type = DisplayString
_FsPatchExist_Object = MibTableColumn
fsPatchExist = _FsPatchExist_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 6),
    _FsPatchExist_Type()
)
fsPatchExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchExist.setStatus("current")
_FsPatchName_Type = DisplayString
_FsPatchName_Object = MibTableColumn
fsPatchName = _FsPatchName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 7),
    _FsPatchName_Type()
)
fsPatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchName.setStatus("current")
_FsPatchBranch_Type = DisplayString
_FsPatchBranch_Object = MibTableColumn
fsPatchBranch = _FsPatchBranch_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 8),
    _FsPatchBranch_Type()
)
fsPatchBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchBranch.setStatus("current")
_FsPatchCmpntName_Type = DisplayString
_FsPatchCmpntName_Object = MibTableColumn
fsPatchCmpntName = _FsPatchCmpntName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 9),
    _FsPatchCmpntName_Type()
)
fsPatchCmpntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchCmpntName.setStatus("current")
_FsPatchSize_Type = Counter64
_FsPatchSize_Object = MibTableColumn
fsPatchSize = _FsPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 10),
    _FsPatchSize_Type()
)
fsPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchSize.setStatus("current")
_FsPatchStatus_Type = DisplayString
_FsPatchStatus_Object = MibTableColumn
fsPatchStatus = _FsPatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 11),
    _FsPatchStatus_Type()
)
fsPatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchStatus.setStatus("current")
_FsPatchVersion_Type = DisplayString
_FsPatchVersion_Object = MibTableColumn
fsPatchVersion = _FsPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 12),
    _FsPatchVersion_Type()
)
fsPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchVersion.setStatus("current")
_FsPatchInstallTime_Type = DisplayString
_FsPatchInstallTime_Object = MibTableColumn
fsPatchInstallTime = _FsPatchInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 13),
    _FsPatchInstallTime_Type()
)
fsPatchInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchInstallTime.setStatus("current")
_FsPatchDescription_Type = DisplayString
_FsPatchDescription_Object = MibTableColumn
fsPatchDescription = _FsPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 151, 1, 1, 1, 14),
    _FsPatchDescription_Type()
)
fsPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPatchDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PATCH-MIB",
    **{"fsPatchMIB": fsPatchMIB,
       "fsPatchMIBObjects": fsPatchMIBObjects,
       "fsPatchTable": fsPatchTable,
       "fsPatchEntry": fsPatchEntry,
       "fsPatchDevIndex": fsPatchDevIndex,
       "fsPatchCmpntIndex": fsPatchCmpntIndex,
       "fsPatchDevId": fsPatchDevId,
       "fsPatchSlotId": fsPatchSlotId,
       "fsPatchCpuId": fsPatchCpuId,
       "fsPatchExist": fsPatchExist,
       "fsPatchName": fsPatchName,
       "fsPatchBranch": fsPatchBranch,
       "fsPatchCmpntName": fsPatchCmpntName,
       "fsPatchSize": fsPatchSize,
       "fsPatchStatus": fsPatchStatus,
       "fsPatchVersion": fsPatchVersion,
       "fsPatchInstallTime": fsPatchInstallTime,
       "fsPatchDescription": fsPatchDescription}
)
