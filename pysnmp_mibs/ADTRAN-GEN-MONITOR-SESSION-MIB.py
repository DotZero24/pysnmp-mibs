# SNMP MIB module (ADTRAN-GEN-MONITOR-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-MONITOR-SESSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:10 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenMonitorSession,
 adGenMonitorSessionID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMonitorSession",
    "adGenMonitorSessionID")

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

adGenMonitorSessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 61, 1)
)
if mibBuilder.loadTexts:
    adGenMonitorSessionMIB.setRevisions(
        ("2017-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMonitorSessionProv_ObjectIdentity = ObjectIdentity
adGenMonitorSessionProv = _AdGenMonitorSessionProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1)
)
_AdGenMonitorSessionTable_Object = MibTable
adGenMonitorSessionTable = _AdGenMonitorSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMonitorSessionTable.setStatus("current")
_AdGenMonitorSessionEntry_Object = MibTableRow
adGenMonitorSessionEntry = _AdGenMonitorSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 1, 1)
)
adGenMonitorSessionEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GEN-MONITOR-SESSION-MIB", "adGenMonitorSessionNum"),
)
if mibBuilder.loadTexts:
    adGenMonitorSessionEntry.setStatus("current")


class _AdGenMonitorSessionNum_Type(Integer32):
    """Custom type adGenMonitorSessionNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AdGenMonitorSessionNum_Type.__name__ = "Integer32"
_AdGenMonitorSessionNum_Object = MibTableColumn
adGenMonitorSessionNum = _AdGenMonitorSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 1, 1, 1),
    _AdGenMonitorSessionNum_Type()
)
adGenMonitorSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMonitorSessionNum.setStatus("current")


class _AdGenMonitorSessionAdminState_Type(Integer32):
    """Custom type adGenMonitorSessionAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AdGenMonitorSessionAdminState_Type.__name__ = "Integer32"
_AdGenMonitorSessionAdminState_Object = MibTableColumn
adGenMonitorSessionAdminState = _AdGenMonitorSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 1, 1, 2),
    _AdGenMonitorSessionAdminState_Type()
)
adGenMonitorSessionAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMonitorSessionAdminState.setStatus("current")
_AdGenMonitorSessionLastError_Type = DisplayString
_AdGenMonitorSessionLastError_Object = MibTableColumn
adGenMonitorSessionLastError = _AdGenMonitorSessionLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 1, 1, 3),
    _AdGenMonitorSessionLastError_Type()
)
adGenMonitorSessionLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMonitorSessionLastError.setStatus("current")
_AdGenMonitorSessionRowStatus_Type = RowStatus
_AdGenMonitorSessionRowStatus_Object = MibTableColumn
adGenMonitorSessionRowStatus = _AdGenMonitorSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 1, 1, 4),
    _AdGenMonitorSessionRowStatus_Type()
)
adGenMonitorSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMonitorSessionRowStatus.setStatus("current")
_AdGenMonitorSessionSrcProvTable_Object = MibTable
adGenMonitorSessionSrcProvTable = _AdGenMonitorSessionSrcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 2)
)
if mibBuilder.loadTexts:
    adGenMonitorSessionSrcProvTable.setStatus("current")
_AdGenMonitorSessionSrcProvEntry_Object = MibTableRow
adGenMonitorSessionSrcProvEntry = _AdGenMonitorSessionSrcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 2, 1)
)
adGenMonitorSessionSrcProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GEN-MONITOR-SESSION-MIB", "adGenMonitorSessionNum"),
    (0, "ADTRAN-GEN-MONITOR-SESSION-MIB", "adGenMonitorSessionSrcifIndex"),
)
if mibBuilder.loadTexts:
    adGenMonitorSessionSrcProvEntry.setStatus("current")
_AdGenMonitorSessionSrcifIndex_Type = InterfaceIndex
_AdGenMonitorSessionSrcifIndex_Object = MibTableColumn
adGenMonitorSessionSrcifIndex = _AdGenMonitorSessionSrcifIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 2, 1, 1),
    _AdGenMonitorSessionSrcifIndex_Type()
)
adGenMonitorSessionSrcifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMonitorSessionSrcifIndex.setStatus("current")


class _AdGenMonitorSessionSrcDirection_Type(Integer32):
    """Custom type adGenMonitorSessionSrcDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1),
          ("both", 2))
    )


_AdGenMonitorSessionSrcDirection_Type.__name__ = "Integer32"
_AdGenMonitorSessionSrcDirection_Object = MibTableColumn
adGenMonitorSessionSrcDirection = _AdGenMonitorSessionSrcDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 2, 1, 2),
    _AdGenMonitorSessionSrcDirection_Type()
)
adGenMonitorSessionSrcDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMonitorSessionSrcDirection.setStatus("current")
_AdGenMonitorSessionSrcLastError_Type = DisplayString
_AdGenMonitorSessionSrcLastError_Object = MibTableColumn
adGenMonitorSessionSrcLastError = _AdGenMonitorSessionSrcLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 2, 1, 3),
    _AdGenMonitorSessionSrcLastError_Type()
)
adGenMonitorSessionSrcLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMonitorSessionSrcLastError.setStatus("current")
_AdGenMonitorSessionSrcRowStatus_Type = RowStatus
_AdGenMonitorSessionSrcRowStatus_Object = MibTableColumn
adGenMonitorSessionSrcRowStatus = _AdGenMonitorSessionSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 2, 1, 4),
    _AdGenMonitorSessionSrcRowStatus_Type()
)
adGenMonitorSessionSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMonitorSessionSrcRowStatus.setStatus("current")
_AdGenMonitorSessionDestProvTable_Object = MibTable
adGenMonitorSessionDestProvTable = _AdGenMonitorSessionDestProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 3)
)
if mibBuilder.loadTexts:
    adGenMonitorSessionDestProvTable.setStatus("current")
_AdGenMonitorSessionDestProvEntry_Object = MibTableRow
adGenMonitorSessionDestProvEntry = _AdGenMonitorSessionDestProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 3, 1)
)
adGenMonitorSessionDestProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GEN-MONITOR-SESSION-MIB", "adGenMonitorSessionNum"),
    (0, "ADTRAN-GEN-MONITOR-SESSION-MIB", "adGenMonitorSessionDestifIndex"),
)
if mibBuilder.loadTexts:
    adGenMonitorSessionDestProvEntry.setStatus("current")
_AdGenMonitorSessionDestifIndex_Type = InterfaceIndex
_AdGenMonitorSessionDestifIndex_Object = MibTableColumn
adGenMonitorSessionDestifIndex = _AdGenMonitorSessionDestifIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 3, 1, 1),
    _AdGenMonitorSessionDestifIndex_Type()
)
adGenMonitorSessionDestifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMonitorSessionDestifIndex.setStatus("current")
_AdGenMonitorSessionDestLastError_Type = DisplayString
_AdGenMonitorSessionDestLastError_Object = MibTableColumn
adGenMonitorSessionDestLastError = _AdGenMonitorSessionDestLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 3, 1, 2),
    _AdGenMonitorSessionDestLastError_Type()
)
adGenMonitorSessionDestLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMonitorSessionDestLastError.setStatus("current")
_AdGenMonitorSessionDestRowStatus_Type = RowStatus
_AdGenMonitorSessionDestRowStatus_Object = MibTableColumn
adGenMonitorSessionDestRowStatus = _AdGenMonitorSessionDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 61, 1, 3, 1, 3),
    _AdGenMonitorSessionDestRowStatus_Type()
)
adGenMonitorSessionDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMonitorSessionDestRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-MONITOR-SESSION-MIB",
    **{"adGenMonitorSessionProv": adGenMonitorSessionProv,
       "adGenMonitorSessionTable": adGenMonitorSessionTable,
       "adGenMonitorSessionEntry": adGenMonitorSessionEntry,
       "adGenMonitorSessionNum": adGenMonitorSessionNum,
       "adGenMonitorSessionAdminState": adGenMonitorSessionAdminState,
       "adGenMonitorSessionLastError": adGenMonitorSessionLastError,
       "adGenMonitorSessionRowStatus": adGenMonitorSessionRowStatus,
       "adGenMonitorSessionSrcProvTable": adGenMonitorSessionSrcProvTable,
       "adGenMonitorSessionSrcProvEntry": adGenMonitorSessionSrcProvEntry,
       "adGenMonitorSessionSrcifIndex": adGenMonitorSessionSrcifIndex,
       "adGenMonitorSessionSrcDirection": adGenMonitorSessionSrcDirection,
       "adGenMonitorSessionSrcLastError": adGenMonitorSessionSrcLastError,
       "adGenMonitorSessionSrcRowStatus": adGenMonitorSessionSrcRowStatus,
       "adGenMonitorSessionDestProvTable": adGenMonitorSessionDestProvTable,
       "adGenMonitorSessionDestProvEntry": adGenMonitorSessionDestProvEntry,
       "adGenMonitorSessionDestifIndex": adGenMonitorSessionDestifIndex,
       "adGenMonitorSessionDestLastError": adGenMonitorSessionDestLastError,
       "adGenMonitorSessionDestRowStatus": adGenMonitorSessionDestRowStatus,
       "adGenMonitorSessionMIB": adGenMonitorSessionMIB}
)
