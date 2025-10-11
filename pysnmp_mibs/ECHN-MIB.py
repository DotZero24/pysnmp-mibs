# SNMP MIB module (ECHN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/ECHN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:47 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsEthChn_ObjectIdentity = ObjectIdentity
nbsEthChn = _NbsEthChn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5)
)
_NbsEthChnRun_ObjectIdentity = ObjectIdentity
nbsEthChnRun = _NbsEthChnRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1)
)
_NbsEthChnRunTable_Object = MibTable
nbsEthChnRunTable = _NbsEthChnRunTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1, 1)
)
if mibBuilder.loadTexts:
    nbsEthChnRunTable.setStatus("mandatory")
_NbsEthChnRunEntry_Object = MibTableRow
nbsEthChnRunEntry = _NbsEthChnRunEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1, 1, 1)
)
nbsEthChnRunEntry.setIndexNames(
    (0, "ECHN-MIB", "nbsEthChnRunIndex"),
)
if mibBuilder.loadTexts:
    nbsEthChnRunEntry.setStatus("mandatory")
_NbsEthChnRunIndex_Type = Integer32
_NbsEthChnRunIndex_Object = MibTableColumn
nbsEthChnRunIndex = _NbsEthChnRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1, 1, 1, 1),
    _NbsEthChnRunIndex_Type()
)
nbsEthChnRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnRunIndex.setStatus("mandatory")


class _NbsEthChnRunStatus_Type(Integer32):
    """Custom type nbsEthChnRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_NbsEthChnRunStatus_Type.__name__ = "Integer32"
_NbsEthChnRunStatus_Object = MibTableColumn
nbsEthChnRunStatus = _NbsEthChnRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1, 1, 1, 2),
    _NbsEthChnRunStatus_Type()
)
nbsEthChnRunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEthChnRunStatus.setStatus("mandatory")
_NbsEthChnRunList_Type = OctetString
_NbsEthChnRunList_Object = MibTableColumn
nbsEthChnRunList = _NbsEthChnRunList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1, 1, 1, 3),
    _NbsEthChnRunList_Type()
)
nbsEthChnRunList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEthChnRunList.setStatus("mandatory")
_NbsEthChnRunLinkList_Type = OctetString
_NbsEthChnRunLinkList_Object = MibTableColumn
nbsEthChnRunLinkList = _NbsEthChnRunLinkList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 1, 1, 1, 4),
    _NbsEthChnRunLinkList_Type()
)
nbsEthChnRunLinkList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnRunLinkList.setStatus("mandatory")
_NbsEthChnPerm_ObjectIdentity = ObjectIdentity
nbsEthChnPerm = _NbsEthChnPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 2)
)
_NbsEthChnPermTable_Object = MibTable
nbsEthChnPermTable = _NbsEthChnPermTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 2, 1)
)
if mibBuilder.loadTexts:
    nbsEthChnPermTable.setStatus("mandatory")
_NbsEthChnPermEntry_Object = MibTableRow
nbsEthChnPermEntry = _NbsEthChnPermEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 2, 1, 1)
)
nbsEthChnPermEntry.setIndexNames(
    (0, "ECHN-MIB", "nbsEthChnPermIndex"),
)
if mibBuilder.loadTexts:
    nbsEthChnPermEntry.setStatus("mandatory")
_NbsEthChnPermIndex_Type = Integer32
_NbsEthChnPermIndex_Object = MibTableColumn
nbsEthChnPermIndex = _NbsEthChnPermIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 2, 1, 1, 1),
    _NbsEthChnPermIndex_Type()
)
nbsEthChnPermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPermIndex.setStatus("mandatory")


class _NbsEthChnPermStatus_Type(Integer32):
    """Custom type nbsEthChnPermStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_NbsEthChnPermStatus_Type.__name__ = "Integer32"
_NbsEthChnPermStatus_Object = MibTableColumn
nbsEthChnPermStatus = _NbsEthChnPermStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 2, 1, 1, 2),
    _NbsEthChnPermStatus_Type()
)
nbsEthChnPermStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEthChnPermStatus.setStatus("mandatory")
_NbsEthChnPermList_Type = OctetString
_NbsEthChnPermList_Object = MibTableColumn
nbsEthChnPermList = _NbsEthChnPermList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 2, 1, 1, 3),
    _NbsEthChnPermList_Type()
)
nbsEthChnPermList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEthChnPermList.setStatus("mandatory")
_NbsEthChnPoss_ObjectIdentity = ObjectIdentity
nbsEthChnPoss = _NbsEthChnPoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3)
)
_NbsEthChnPossTable_Object = MibTable
nbsEthChnPossTable = _NbsEthChnPossTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1)
)
if mibBuilder.loadTexts:
    nbsEthChnPossTable.setStatus("mandatory")
_NbsEthChnPossEntry_Object = MibTableRow
nbsEthChnPossEntry = _NbsEthChnPossEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1, 1)
)
nbsEthChnPossEntry.setIndexNames(
    (0, "ECHN-MIB", "nbsEthChnPossIndex"),
)
if mibBuilder.loadTexts:
    nbsEthChnPossEntry.setStatus("mandatory")
_NbsEthChnPossIndex_Type = Integer32
_NbsEthChnPossIndex_Object = MibTableColumn
nbsEthChnPossIndex = _NbsEthChnPossIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1, 1, 1),
    _NbsEthChnPossIndex_Type()
)
nbsEthChnPossIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPossIndex.setStatus("mandatory")


class _NbsEthChnPossRunStatus_Type(Integer32):
    """Custom type nbsEthChnPossRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_NbsEthChnPossRunStatus_Type.__name__ = "Integer32"
_NbsEthChnPossRunStatus_Object = MibTableColumn
nbsEthChnPossRunStatus = _NbsEthChnPossRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1, 1, 2),
    _NbsEthChnPossRunStatus_Type()
)
nbsEthChnPossRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPossRunStatus.setStatus("mandatory")


class _NbsEthChnPossPermStatus_Type(Integer32):
    """Custom type nbsEthChnPossPermStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_NbsEthChnPossPermStatus_Type.__name__ = "Integer32"
_NbsEthChnPossPermStatus_Object = MibTableColumn
nbsEthChnPossPermStatus = _NbsEthChnPossPermStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1, 1, 3),
    _NbsEthChnPossPermStatus_Type()
)
nbsEthChnPossPermStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPossPermStatus.setStatus("mandatory")
_NbsEthChnPossPortMaxNum_Type = Integer32
_NbsEthChnPossPortMaxNum_Object = MibTableColumn
nbsEthChnPossPortMaxNum = _NbsEthChnPossPortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1, 1, 4),
    _NbsEthChnPossPortMaxNum_Type()
)
nbsEthChnPossPortMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPossPortMaxNum.setStatus("mandatory")
_NbsEthChnPossList_Type = OctetString
_NbsEthChnPossList_Object = MibTableColumn
nbsEthChnPossList = _NbsEthChnPossList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 3, 1, 1, 5),
    _NbsEthChnPossList_Type()
)
nbsEthChnPossList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPossList.setStatus("mandatory")


class _NbsEthChnEnable_Type(Integer32):
    """Custom type nbsEthChnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_NbsEthChnEnable_Type.__name__ = "Integer32"
_NbsEthChnEnable_Object = MibScalar
nbsEthChnEnable = _NbsEthChnEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 4),
    _NbsEthChnEnable_Type()
)
nbsEthChnEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnEnable.setStatus("mandatory")
_NbsEthChnPossNum_Type = Integer32
_NbsEthChnPossNum_Object = MibScalar
nbsEthChnPossNum = _NbsEthChnPossNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 5),
    _NbsEthChnPossNum_Type()
)
nbsEthChnPossNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPossNum.setStatus("mandatory")
_NbsEthChnMaxNum_Type = Integer32
_NbsEthChnMaxNum_Object = MibScalar
nbsEthChnMaxNum = _NbsEthChnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 6),
    _NbsEthChnMaxNum_Type()
)
nbsEthChnMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnMaxNum.setStatus("mandatory")
_NbsEthChnRunNum_Type = Integer32
_NbsEthChnRunNum_Object = MibScalar
nbsEthChnRunNum = _NbsEthChnRunNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 7),
    _NbsEthChnRunNum_Type()
)
nbsEthChnRunNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnRunNum.setStatus("mandatory")
_NbsEthChnPermNum_Type = Integer32
_NbsEthChnPermNum_Object = MibScalar
nbsEthChnPermNum = _NbsEthChnPermNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 5, 8),
    _NbsEthChnPermNum_Type()
)
nbsEthChnPermNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEthChnPermNum.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECHN-MIB",
    **{"nbsEthChn": nbsEthChn,
       "nbsEthChnRun": nbsEthChnRun,
       "nbsEthChnRunTable": nbsEthChnRunTable,
       "nbsEthChnRunEntry": nbsEthChnRunEntry,
       "nbsEthChnRunIndex": nbsEthChnRunIndex,
       "nbsEthChnRunStatus": nbsEthChnRunStatus,
       "nbsEthChnRunList": nbsEthChnRunList,
       "nbsEthChnRunLinkList": nbsEthChnRunLinkList,
       "nbsEthChnPerm": nbsEthChnPerm,
       "nbsEthChnPermTable": nbsEthChnPermTable,
       "nbsEthChnPermEntry": nbsEthChnPermEntry,
       "nbsEthChnPermIndex": nbsEthChnPermIndex,
       "nbsEthChnPermStatus": nbsEthChnPermStatus,
       "nbsEthChnPermList": nbsEthChnPermList,
       "nbsEthChnPoss": nbsEthChnPoss,
       "nbsEthChnPossTable": nbsEthChnPossTable,
       "nbsEthChnPossEntry": nbsEthChnPossEntry,
       "nbsEthChnPossIndex": nbsEthChnPossIndex,
       "nbsEthChnPossRunStatus": nbsEthChnPossRunStatus,
       "nbsEthChnPossPermStatus": nbsEthChnPossPermStatus,
       "nbsEthChnPossPortMaxNum": nbsEthChnPossPortMaxNum,
       "nbsEthChnPossList": nbsEthChnPossList,
       "nbsEthChnEnable": nbsEthChnEnable,
       "nbsEthChnPossNum": nbsEthChnPossNum,
       "nbsEthChnMaxNum": nbsEthChnMaxNum,
       "nbsEthChnRunNum": nbsEthChnRunNum,
       "nbsEthChnPermNum": nbsEthChnPermNum}
)
