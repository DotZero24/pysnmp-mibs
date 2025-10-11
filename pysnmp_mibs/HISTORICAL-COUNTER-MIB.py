# SNMP MIB module (HISTORICAL-COUNTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/HISTORICAL-COUNTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:45:03 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

swHistoryCntMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwHistoryCntCtrl_ObjectIdentity = ObjectIdentity
swHistoryCntCtrl = _SwHistoryCntCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 1)
)
_SwHistoryCntInfo_ObjectIdentity = ObjectIdentity
swHistoryCntInfo = _SwHistoryCntInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2)
)
_SwHistoricalCounter_ObjectIdentity = ObjectIdentity
swHistoricalCounter = _SwHistoricalCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1)
)
_SwHistoryCntPktTable_Object = MibTable
swHistoryCntPktTable = _SwHistoryCntPktTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swHistoryCntPktTable.setStatus("current")
_SwHistoryCntPktEntry_Object = MibTableRow
swHistoryCntPktEntry = _SwHistoryCntPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1)
)
swHistoryCntPktEntry.setIndexNames(
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntPort"),
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntTime"),
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntType"),
)
if mibBuilder.loadTexts:
    swHistoryCntPktEntry.setStatus("current")
_SwHistoryCntPort_Type = Integer32
_SwHistoryCntPort_Object = MibTableColumn
swHistoryCntPort = _SwHistoryCntPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 1),
    _SwHistoryCntPort_Type()
)
swHistoryCntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntPort.setStatus("current")


class _SwHistoryCntTime_Type(Integer32):
    """Custom type swHistoryCntTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteen-minute", 1),
          ("one-day", 2))
    )


_SwHistoryCntTime_Type.__name__ = "Integer32"
_SwHistoryCntTime_Object = MibTableColumn
swHistoryCntTime = _SwHistoryCntTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 2),
    _SwHistoryCntTime_Type()
)
swHistoryCntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntTime.setStatus("current")


class _SwHistoryCntType_Type(Integer32):
    """Custom type swHistoryCntType based on Integer32"""
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
        *(("slot1", 1),
          ("slot2", 2),
          ("slot3", 3),
          ("slot4", 4),
          ("slot5", 5))
    )


_SwHistoryCntType_Type.__name__ = "Integer32"
_SwHistoryCntType_Object = MibTableColumn
swHistoryCntType = _SwHistoryCntType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 3),
    _SwHistoryCntType_Type()
)
swHistoryCntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntType.setStatus("current")
_SwHistoryCntPktsTx_Type = Counter64
_SwHistoryCntPktsTx_Object = MibTableColumn
swHistoryCntPktsTx = _SwHistoryCntPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 4),
    _SwHistoryCntPktsTx_Type()
)
swHistoryCntPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntPktsTx.setStatus("current")
_SwHistoryCntBytesTx_Type = Counter64
_SwHistoryCntBytesTx_Object = MibTableColumn
swHistoryCntBytesTx = _SwHistoryCntBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 5),
    _SwHistoryCntBytesTx_Type()
)
swHistoryCntBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntBytesTx.setStatus("current")
_SwHistoryCntPktsRx_Type = Counter64
_SwHistoryCntPktsRx_Object = MibTableColumn
swHistoryCntPktsRx = _SwHistoryCntPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 6),
    _SwHistoryCntPktsRx_Type()
)
swHistoryCntPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntPktsRx.setStatus("current")
_SwHistoryCntBytesRx_Type = Counter64
_SwHistoryCntBytesRx_Object = MibTableColumn
swHistoryCntBytesRx = _SwHistoryCntBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 7),
    _SwHistoryCntBytesRx_Type()
)
swHistoryCntBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntBytesRx.setStatus("current")
_SwHistoryCnt64Rx_Type = Counter64
_SwHistoryCnt64Rx_Object = MibTableColumn
swHistoryCnt64Rx = _SwHistoryCnt64Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 8),
    _SwHistoryCnt64Rx_Type()
)
swHistoryCnt64Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCnt64Rx.setStatus("current")
_SwHistoryCnt65to127Rx_Type = Counter64
_SwHistoryCnt65to127Rx_Object = MibTableColumn
swHistoryCnt65to127Rx = _SwHistoryCnt65to127Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 9),
    _SwHistoryCnt65to127Rx_Type()
)
swHistoryCnt65to127Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCnt65to127Rx.setStatus("current")
_SwHistoryCnt128to255Rx_Type = Counter64
_SwHistoryCnt128to255Rx_Object = MibTableColumn
swHistoryCnt128to255Rx = _SwHistoryCnt128to255Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 10),
    _SwHistoryCnt128to255Rx_Type()
)
swHistoryCnt128to255Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCnt128to255Rx.setStatus("current")
_SwHistoryCnt256to511Rx_Type = Counter64
_SwHistoryCnt256to511Rx_Object = MibTableColumn
swHistoryCnt256to511Rx = _SwHistoryCnt256to511Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 11),
    _SwHistoryCnt256to511Rx_Type()
)
swHistoryCnt256to511Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCnt256to511Rx.setStatus("current")
_SwHistoryCnt512to1023Rx_Type = Counter64
_SwHistoryCnt512to1023Rx_Object = MibTableColumn
swHistoryCnt512to1023Rx = _SwHistoryCnt512to1023Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 12),
    _SwHistoryCnt512to1023Rx_Type()
)
swHistoryCnt512to1023Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCnt512to1023Rx.setStatus("current")
_SwHistoryCnt1024to1518Rx_Type = Counter64
_SwHistoryCnt1024to1518Rx_Object = MibTableColumn
swHistoryCnt1024to1518Rx = _SwHistoryCnt1024to1518Rx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 13),
    _SwHistoryCnt1024to1518Rx_Type()
)
swHistoryCnt1024to1518Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCnt1024to1518Rx.setStatus("current")
_SwHistoryCntUnicastRx_Type = Counter64
_SwHistoryCntUnicastRx_Object = MibTableColumn
swHistoryCntUnicastRx = _SwHistoryCntUnicastRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 14),
    _SwHistoryCntUnicastRx_Type()
)
swHistoryCntUnicastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntUnicastRx.setStatus("current")
_SwHistoryCntMulticastRx_Type = Counter64
_SwHistoryCntMulticastRx_Object = MibTableColumn
swHistoryCntMulticastRx = _SwHistoryCntMulticastRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 15),
    _SwHistoryCntMulticastRx_Type()
)
swHistoryCntMulticastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntMulticastRx.setStatus("current")
_SwHistoryCntBroadcastRx_Type = Counter64
_SwHistoryCntBroadcastRx_Object = MibTableColumn
swHistoryCntBroadcastRx = _SwHistoryCntBroadcastRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 16),
    _SwHistoryCntBroadcastRx_Type()
)
swHistoryCntBroadcastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntBroadcastRx.setStatus("current")
_SwHistoryCntStartTime_Type = DateAndTime
_SwHistoryCntStartTime_Object = MibTableColumn
swHistoryCntStartTime = _SwHistoryCntStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 17),
    _SwHistoryCntStartTime_Type()
)
swHistoryCntStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntStartTime.setStatus("current")
_SwHistoryCntEndTime_Type = DateAndTime
_SwHistoryCntEndTime_Object = MibTableColumn
swHistoryCntEndTime = _SwHistoryCntEndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 1, 1, 18),
    _SwHistoryCntEndTime_Type()
)
swHistoryCntEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntEndTime.setStatus("current")
_SwHistoryCntErrTable_Object = MibTable
swHistoryCntErrTable = _SwHistoryCntErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2)
)
if mibBuilder.loadTexts:
    swHistoryCntErrTable.setStatus("current")
_SwHistoryCntErrEntry_Object = MibTableRow
swHistoryCntErrEntry = _SwHistoryCntErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1)
)
swHistoryCntErrEntry.setIndexNames(
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntPort"),
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntTime"),
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntType"),
)
if mibBuilder.loadTexts:
    swHistoryCntErrEntry.setStatus("current")
_SwHistoryCntFragmentRx_Type = Counter64
_SwHistoryCntFragmentRx_Object = MibTableColumn
swHistoryCntFragmentRx = _SwHistoryCntFragmentRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 1),
    _SwHistoryCntFragmentRx_Type()
)
swHistoryCntFragmentRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntFragmentRx.setStatus("current")
_SwHistoryCntJabberPktsRx_Type = Counter64
_SwHistoryCntJabberPktsRx_Object = MibTableColumn
swHistoryCntJabberPktsRx = _SwHistoryCntJabberPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 2),
    _SwHistoryCntJabberPktsRx_Type()
)
swHistoryCntJabberPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntJabberPktsRx.setStatus("current")
_SwHistoryCntOversizePktsRx_Type = Counter64
_SwHistoryCntOversizePktsRx_Object = MibTableColumn
swHistoryCntOversizePktsRx = _SwHistoryCntOversizePktsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 3),
    _SwHistoryCntOversizePktsRx_Type()
)
swHistoryCntOversizePktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntOversizePktsRx.setStatus("current")
_SwHistoryCntUndersizePktsRx_Type = Counter64
_SwHistoryCntUndersizePktsRx_Object = MibTableColumn
swHistoryCntUndersizePktsRx = _SwHistoryCntUndersizePktsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 4),
    _SwHistoryCntUndersizePktsRx_Type()
)
swHistoryCntUndersizePktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntUndersizePktsRx.setStatus("current")
_SwHistoryCntAlignmentErrorsRx_Type = Counter64
_SwHistoryCntAlignmentErrorsRx_Object = MibTableColumn
swHistoryCntAlignmentErrorsRx = _SwHistoryCntAlignmentErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 5),
    _SwHistoryCntAlignmentErrorsRx_Type()
)
swHistoryCntAlignmentErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntAlignmentErrorsRx.setStatus("current")
_SwHistoryCntUnknownCtrlPktsRx_Type = Counter64
_SwHistoryCntUnknownCtrlPktsRx_Object = MibTableColumn
swHistoryCntUnknownCtrlPktsRx = _SwHistoryCntUnknownCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 6),
    _SwHistoryCntUnknownCtrlPktsRx_Type()
)
swHistoryCntUnknownCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntUnknownCtrlPktsRx.setStatus("current")
_SwHistoryCntCollisionTx_Type = Counter64
_SwHistoryCntCollisionTx_Object = MibTableColumn
swHistoryCntCollisionTx = _SwHistoryCntCollisionTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 7),
    _SwHistoryCntCollisionTx_Type()
)
swHistoryCntCollisionTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntCollisionTx.setStatus("current")
_SwHistoryCntDropedPkts_Type = Counter64
_SwHistoryCntDropedPkts_Object = MibTableColumn
swHistoryCntDropedPkts = _SwHistoryCntDropedPkts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 8),
    _SwHistoryCntDropedPkts_Type()
)
swHistoryCntDropedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntDropedPkts.setStatus("current")
_SwHistoryCntErrStartTime_Type = DateAndTime
_SwHistoryCntErrStartTime_Object = MibTableColumn
swHistoryCntErrStartTime = _SwHistoryCntErrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 9),
    _SwHistoryCntErrStartTime_Type()
)
swHistoryCntErrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntErrStartTime.setStatus("current")
_SwHistoryCntErrEndTime_Type = DateAndTime
_SwHistoryCntErrEndTime_Object = MibTableColumn
swHistoryCntErrEndTime = _SwHistoryCntErrEndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 1, 2, 1, 10),
    _SwHistoryCntErrEndTime_Type()
)
swHistoryCntErrEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryCntErrEndTime.setStatus("current")
_SwHistoricalUtilization_ObjectIdentity = ObjectIdentity
swHistoricalUtilization = _SwHistoricalUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2)
)
_SwHistoryUtilTable_Object = MibTable
swHistoryUtilTable = _SwHistoryUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swHistoryUtilTable.setStatus("current")
_SwHistoryUtilEntry_Object = MibTableRow
swHistoryUtilEntry = _SwHistoryUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2, 1, 1)
)
swHistoryUtilEntry.setIndexNames(
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntTime"),
    (0, "HISTORICAL-COUNTER-MIB", "swHistoryCntType"),
)
if mibBuilder.loadTexts:
    swHistoryUtilEntry.setStatus("current")
_SwHistoryUtilCPU_Type = Integer32
_SwHistoryUtilCPU_Object = MibTableColumn
swHistoryUtilCPU = _SwHistoryUtilCPU_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2, 1, 1, 1),
    _SwHistoryUtilCPU_Type()
)
swHistoryUtilCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryUtilCPU.setStatus("current")
_SwHistoryUtilMemory_Type = Integer32
_SwHistoryUtilMemory_Object = MibTableColumn
swHistoryUtilMemory = _SwHistoryUtilMemory_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2, 1, 1, 2),
    _SwHistoryUtilMemory_Type()
)
swHistoryUtilMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryUtilMemory.setStatus("current")
_SwHistoryUtilStartTime_Type = DateAndTime
_SwHistoryUtilStartTime_Object = MibTableColumn
swHistoryUtilStartTime = _SwHistoryUtilStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2, 1, 1, 3),
    _SwHistoryUtilStartTime_Type()
)
swHistoryUtilStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryUtilStartTime.setStatus("current")
_SwHistoryUtilEndTime_Type = DateAndTime
_SwHistoryUtilEndTime_Object = MibTableColumn
swHistoryUtilEndTime = _SwHistoryUtilEndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 2, 2, 1, 1, 4),
    _SwHistoryUtilEndTime_Type()
)
swHistoryUtilEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHistoryUtilEndTime.setStatus("current")
_SwHistoryCntMgmt_ObjectIdentity = ObjectIdentity
swHistoryCntMgmt = _SwHistoryCntMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 66, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HISTORICAL-COUNTER-MIB",
    **{"swHistoryCntMIB": swHistoryCntMIB,
       "swHistoryCntCtrl": swHistoryCntCtrl,
       "swHistoryCntInfo": swHistoryCntInfo,
       "swHistoricalCounter": swHistoricalCounter,
       "swHistoryCntPktTable": swHistoryCntPktTable,
       "swHistoryCntPktEntry": swHistoryCntPktEntry,
       "swHistoryCntPort": swHistoryCntPort,
       "swHistoryCntTime": swHistoryCntTime,
       "swHistoryCntType": swHistoryCntType,
       "swHistoryCntPktsTx": swHistoryCntPktsTx,
       "swHistoryCntBytesTx": swHistoryCntBytesTx,
       "swHistoryCntPktsRx": swHistoryCntPktsRx,
       "swHistoryCntBytesRx": swHistoryCntBytesRx,
       "swHistoryCnt64Rx": swHistoryCnt64Rx,
       "swHistoryCnt65to127Rx": swHistoryCnt65to127Rx,
       "swHistoryCnt128to255Rx": swHistoryCnt128to255Rx,
       "swHistoryCnt256to511Rx": swHistoryCnt256to511Rx,
       "swHistoryCnt512to1023Rx": swHistoryCnt512to1023Rx,
       "swHistoryCnt1024to1518Rx": swHistoryCnt1024to1518Rx,
       "swHistoryCntUnicastRx": swHistoryCntUnicastRx,
       "swHistoryCntMulticastRx": swHistoryCntMulticastRx,
       "swHistoryCntBroadcastRx": swHistoryCntBroadcastRx,
       "swHistoryCntStartTime": swHistoryCntStartTime,
       "swHistoryCntEndTime": swHistoryCntEndTime,
       "swHistoryCntErrTable": swHistoryCntErrTable,
       "swHistoryCntErrEntry": swHistoryCntErrEntry,
       "swHistoryCntFragmentRx": swHistoryCntFragmentRx,
       "swHistoryCntJabberPktsRx": swHistoryCntJabberPktsRx,
       "swHistoryCntOversizePktsRx": swHistoryCntOversizePktsRx,
       "swHistoryCntUndersizePktsRx": swHistoryCntUndersizePktsRx,
       "swHistoryCntAlignmentErrorsRx": swHistoryCntAlignmentErrorsRx,
       "swHistoryCntUnknownCtrlPktsRx": swHistoryCntUnknownCtrlPktsRx,
       "swHistoryCntCollisionTx": swHistoryCntCollisionTx,
       "swHistoryCntDropedPkts": swHistoryCntDropedPkts,
       "swHistoryCntErrStartTime": swHistoryCntErrStartTime,
       "swHistoryCntErrEndTime": swHistoryCntErrEndTime,
       "swHistoricalUtilization": swHistoricalUtilization,
       "swHistoryUtilTable": swHistoryUtilTable,
       "swHistoryUtilEntry": swHistoryUtilEntry,
       "swHistoryUtilCPU": swHistoryUtilCPU,
       "swHistoryUtilMemory": swHistoryUtilMemory,
       "swHistoryUtilStartTime": swHistoryUtilStartTime,
       "swHistoryUtilEndTime": swHistoryUtilEndTime,
       "swHistoryCntMgmt": swHistoryCntMgmt}
)
