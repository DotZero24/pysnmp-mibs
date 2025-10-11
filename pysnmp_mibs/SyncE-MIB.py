# SNMP MIB module (SyncE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SyncE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:53 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

fsSynceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79)
)
if mibBuilder.loadTexts:
    fsSynceMIB.setRevisions(
        ("2013-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSynceObjects_ObjectIdentity = ObjectIdentity
fsSynceObjects = _FsSynceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1)
)
_FsSynceGeneralGroup_ObjectIdentity = ObjectIdentity
fsSynceGeneralGroup = _FsSynceGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1)
)


class _FsSynceGlobalSysCtrl_Type(Integer32):
    """Custom type fsSynceGlobalSysCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsSynceGlobalSysCtrl_Type.__name__ = "Integer32"
_FsSynceGlobalSysCtrl_Object = MibScalar
fsSynceGlobalSysCtrl = _FsSynceGlobalSysCtrl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 1),
    _FsSynceGlobalSysCtrl_Type()
)
fsSynceGlobalSysCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceGlobalSysCtrl.setStatus("current")
_FsSynceTable_Object = MibTable
fsSynceTable = _FsSynceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsSynceTable.setStatus("current")
_FsSynceEntry_Object = MibTableRow
fsSynceEntry = _FsSynceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1)
)
fsSynceEntry.setIndexNames(
    (0, "SyncE-MIB", "fsSynceContextId"),
)
if mibBuilder.loadTexts:
    fsSynceEntry.setStatus("current")


class _FsSynceContextId_Type(Integer32):
    """Custom type fsSynceContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSynceContextId_Type.__name__ = "Integer32"
_FsSynceContextId_Object = MibTableColumn
fsSynceContextId = _FsSynceContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 1),
    _FsSynceContextId_Type()
)
fsSynceContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSynceContextId.setStatus("current")


class _FsSynceTraceOption_Type(Unsigned32):
    """Custom type fsSynceTraceOption based on Unsigned32"""
    defaultValue = 64


_FsSynceTraceOption_Type.__name__ = "Unsigned32"
_FsSynceTraceOption_Object = MibTableColumn
fsSynceTraceOption = _FsSynceTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 2),
    _FsSynceTraceOption_Type()
)
fsSynceTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceTraceOption.setStatus("current")


class _FsSynceQLMode_Type(Integer32):
    """Custom type fsSynceQLMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsSynceQLMode_Type.__name__ = "Integer32"
_FsSynceQLMode_Object = MibTableColumn
fsSynceQLMode = _FsSynceQLMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 3),
    _FsSynceQLMode_Type()
)
fsSynceQLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceQLMode.setStatus("current")


class _FsSynceQLValue_Type(Unsigned32):
    """Custom type fsSynceQLValue based on Unsigned32"""
    defaultValue = 15


_FsSynceQLValue_Type.__name__ = "Unsigned32"
_FsSynceQLValue_Object = MibTableColumn
fsSynceQLValue = _FsSynceQLValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 4),
    _FsSynceQLValue_Type()
)
fsSynceQLValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceQLValue.setStatus("current")


class _FsSynceSSMOptionMode_Type(Integer32):
    """Custom type fsSynceSSMOptionMode based on Integer32"""
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
        *(("option1", 1),
          ("option2Gen1", 2),
          ("option2Gen2", 3))
    )


_FsSynceSSMOptionMode_Type.__name__ = "Integer32"
_FsSynceSSMOptionMode_Object = MibTableColumn
fsSynceSSMOptionMode = _FsSynceSSMOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 5),
    _FsSynceSSMOptionMode_Type()
)
fsSynceSSMOptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceSSMOptionMode.setStatus("current")
_FsSynceSelectedInterface_Type = InterfaceIndex
_FsSynceSelectedInterface_Object = MibTableColumn
fsSynceSelectedInterface = _FsSynceSelectedInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 6),
    _FsSynceSelectedInterface_Type()
)
fsSynceSelectedInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceSelectedInterface.setStatus("current")
_FsSynceContextRowStatus_Type = RowStatus
_FsSynceContextRowStatus_Object = MibTableColumn
fsSynceContextRowStatus = _FsSynceContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 1, 2, 1, 7),
    _FsSynceContextRowStatus_Type()
)
fsSynceContextRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceContextRowStatus.setStatus("current")
_FsSynceInterfaceConfiguration_ObjectIdentity = ObjectIdentity
fsSynceInterfaceConfiguration = _FsSynceInterfaceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2)
)
_FsSynceIfTable_Object = MibTable
fsSynceIfTable = _FsSynceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsSynceIfTable.setStatus("current")
_FsSynceIfEntry_Object = MibTableRow
fsSynceIfEntry = _FsSynceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1)
)
fsSynceIfEntry.setIndexNames(
    (0, "SyncE-MIB", "fsSynceIfIndex"),
)
if mibBuilder.loadTexts:
    fsSynceIfEntry.setStatus("current")
_FsSynceIfIndex_Type = InterfaceIndex
_FsSynceIfIndex_Object = MibTableColumn
fsSynceIfIndex = _FsSynceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 1),
    _FsSynceIfIndex_Type()
)
fsSynceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSynceIfIndex.setStatus("current")


class _FsSynceIfSynceMode_Type(TruthValue):
    """Custom type fsSynceIfSynceMode based on TruthValue"""
    defaultValue = 2


_FsSynceIfSynceMode_Type.__name__ = "TruthValue"
_FsSynceIfSynceMode_Object = MibTableColumn
fsSynceIfSynceMode = _FsSynceIfSynceMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 2),
    _FsSynceIfSynceMode_Type()
)
fsSynceIfSynceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceIfSynceMode.setStatus("current")


class _FsSynceIfEsmcMode_Type(Integer32):
    """Custom type fsSynceIfEsmcMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rx", 1),
          ("tx", 2))
    )


_FsSynceIfEsmcMode_Type.__name__ = "Integer32"
_FsSynceIfEsmcMode_Object = MibTableColumn
fsSynceIfEsmcMode = _FsSynceIfEsmcMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 3),
    _FsSynceIfEsmcMode_Type()
)
fsSynceIfEsmcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceIfEsmcMode.setStatus("current")


class _FsSynceIfPriority_Type(Integer32):
    """Custom type fsSynceIfPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsSynceIfPriority_Type.__name__ = "Integer32"
_FsSynceIfPriority_Object = MibTableColumn
fsSynceIfPriority = _FsSynceIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 4),
    _FsSynceIfPriority_Type()
)
fsSynceIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceIfPriority.setStatus("current")


class _FsSynceIfQLValue_Type(Integer32):
    """Custom type fsSynceIfQLValue based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("qlPRC", 1),
          ("qlSSUA", 2),
          ("qlSSUB", 3),
          ("qlSEC", 4),
          ("qlDNU", 5),
          ("qlPRS", 6),
          ("qlSTU", 7),
          ("qlST2", 8),
          ("qlTNC", 9),
          ("qlST3E", 10),
          ("qlST3", 11),
          ("qlSMC", 12),
          ("qlRES", 13),
          ("qlPROV", 14),
          ("qlDUS", 15))
    )


_FsSynceIfQLValue_Type.__name__ = "Integer32"
_FsSynceIfQLValue_Object = MibTableColumn
fsSynceIfQLValue = _FsSynceIfQLValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 5),
    _FsSynceIfQLValue_Type()
)
fsSynceIfQLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceIfQLValue.setStatus("current")
_FsSynceIfIsRxQLForced_Type = TruthValue
_FsSynceIfIsRxQLForced_Object = MibTableColumn
fsSynceIfIsRxQLForced = _FsSynceIfIsRxQLForced_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 6),
    _FsSynceIfIsRxQLForced_Type()
)
fsSynceIfIsRxQLForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceIfIsRxQLForced.setStatus("current")


class _FsSynceIfLockoutStatus_Type(TruthValue):
    """Custom type fsSynceIfLockoutStatus based on TruthValue"""
    defaultValue = 2


_FsSynceIfLockoutStatus_Type.__name__ = "TruthValue"
_FsSynceIfLockoutStatus_Object = MibTableColumn
fsSynceIfLockoutStatus = _FsSynceIfLockoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 7),
    _FsSynceIfLockoutStatus_Type()
)
fsSynceIfLockoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceIfLockoutStatus.setStatus("current")
_FsSynceIfSignalFail_Type = TruthValue
_FsSynceIfSignalFail_Object = MibTableColumn
fsSynceIfSignalFail = _FsSynceIfSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 8),
    _FsSynceIfSignalFail_Type()
)
fsSynceIfSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceIfSignalFail.setStatus("current")
_FsSynceIfPktsTx_Type = Unsigned32
_FsSynceIfPktsTx_Object = MibTableColumn
fsSynceIfPktsTx = _FsSynceIfPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 9),
    _FsSynceIfPktsTx_Type()
)
fsSynceIfPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceIfPktsTx.setStatus("current")
_FsSynceIfPktsRx_Type = Unsigned32
_FsSynceIfPktsRx_Object = MibTableColumn
fsSynceIfPktsRx = _FsSynceIfPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 10),
    _FsSynceIfPktsRx_Type()
)
fsSynceIfPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceIfPktsRx.setStatus("current")
_FsSynceIfPktsRxDropped_Type = Unsigned32
_FsSynceIfPktsRxDropped_Object = MibTableColumn
fsSynceIfPktsRxDropped = _FsSynceIfPktsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 11),
    _FsSynceIfPktsRxDropped_Type()
)
fsSynceIfPktsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceIfPktsRxDropped.setStatus("current")
_FsSynceIfPktsRxErrored_Type = Unsigned32
_FsSynceIfPktsRxErrored_Object = MibTableColumn
fsSynceIfPktsRxErrored = _FsSynceIfPktsRxErrored_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 12),
    _FsSynceIfPktsRxErrored_Type()
)
fsSynceIfPktsRxErrored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSynceIfPktsRxErrored.setStatus("current")
_FsSynceIfRowStatus_Type = RowStatus
_FsSynceIfRowStatus_Object = MibTableColumn
fsSynceIfRowStatus = _FsSynceIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 1, 2, 1, 1, 13),
    _FsSynceIfRowStatus_Type()
)
fsSynceIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSynceIfRowStatus.setStatus("current")
_FsSynceNotifications_ObjectIdentity = ObjectIdentity
fsSynceNotifications = _FsSynceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 79, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SyncE-MIB",
    **{"fsSynceMIB": fsSynceMIB,
       "fsSynceObjects": fsSynceObjects,
       "fsSynceGeneralGroup": fsSynceGeneralGroup,
       "fsSynceGlobalSysCtrl": fsSynceGlobalSysCtrl,
       "fsSynceTable": fsSynceTable,
       "fsSynceEntry": fsSynceEntry,
       "fsSynceContextId": fsSynceContextId,
       "fsSynceTraceOption": fsSynceTraceOption,
       "fsSynceQLMode": fsSynceQLMode,
       "fsSynceQLValue": fsSynceQLValue,
       "fsSynceSSMOptionMode": fsSynceSSMOptionMode,
       "fsSynceSelectedInterface": fsSynceSelectedInterface,
       "fsSynceContextRowStatus": fsSynceContextRowStatus,
       "fsSynceInterfaceConfiguration": fsSynceInterfaceConfiguration,
       "fsSynceIfTable": fsSynceIfTable,
       "fsSynceIfEntry": fsSynceIfEntry,
       "fsSynceIfIndex": fsSynceIfIndex,
       "fsSynceIfSynceMode": fsSynceIfSynceMode,
       "fsSynceIfEsmcMode": fsSynceIfEsmcMode,
       "fsSynceIfPriority": fsSynceIfPriority,
       "fsSynceIfQLValue": fsSynceIfQLValue,
       "fsSynceIfIsRxQLForced": fsSynceIfIsRxQLForced,
       "fsSynceIfLockoutStatus": fsSynceIfLockoutStatus,
       "fsSynceIfSignalFail": fsSynceIfSignalFail,
       "fsSynceIfPktsTx": fsSynceIfPktsTx,
       "fsSynceIfPktsRx": fsSynceIfPktsRx,
       "fsSynceIfPktsRxDropped": fsSynceIfPktsRxDropped,
       "fsSynceIfPktsRxErrored": fsSynceIfPktsRxErrored,
       "fsSynceIfRowStatus": fsSynceIfRowStatus,
       "fsSynceNotifications": fsSynceNotifications}
)
