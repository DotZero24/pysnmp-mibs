# SNMP MIB module (ZXCESPERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXCESPERFORMANCE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:52 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(ZxAnIfindex,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex")

(zxAnCesMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnCesMib")

(zxCesCardIndex,) = mibBuilder.importSymbols(
    "ZXCESCARDPROP-MIB",
    "zxCesCardIndex")

(zxPwIndex,) = mibBuilder.importSymbols(
    "ZXPW-STD-MIB",
    "zxPwIndex")

(zxSonetIfIndex,
 zxSonetVTIfIndex) = mibBuilder.importSymbols(
    "ZXSONETIF-MIB",
    "zxSonetIfIndex",
    "zxSonetVTIfIndex")


# MODULE-IDENTITY

zxAnCesPm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnCesPmInfor_ObjectIdentity = ObjectIdentity
zxAnCesPmInfor = _ZxAnCesPmInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1)
)
_ZxAnCesWanPortStatisticTable_Object = MibTable
zxAnCesWanPortStatisticTable = _ZxAnCesWanPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticTable.setStatus("current")
_ZxAnCesWanPortStatisticEntry_Object = MibTableRow
zxAnCesWanPortStatisticEntry = _ZxAnCesWanPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1)
)
zxAnCesWanPortStatisticEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticEntry.setStatus("current")
_ZxAnCesWanPortStatisticEarlyPkts_Type = Unsigned32
_ZxAnCesWanPortStatisticEarlyPkts_Object = MibTableColumn
zxAnCesWanPortStatisticEarlyPkts = _ZxAnCesWanPortStatisticEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 1),
    _ZxAnCesWanPortStatisticEarlyPkts_Type()
)
zxAnCesWanPortStatisticEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticEarlyPkts.setStatus("current")
_ZxAnCesWanPortStatisticLatePkts_Type = Unsigned32
_ZxAnCesWanPortStatisticLatePkts_Object = MibTableColumn
zxAnCesWanPortStatisticLatePkts = _ZxAnCesWanPortStatisticLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 2),
    _ZxAnCesWanPortStatisticLatePkts_Type()
)
zxAnCesWanPortStatisticLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticLatePkts.setStatus("current")
_ZxAnCesWanPortStatisticUnderrunPkts_Type = Unsigned32
_ZxAnCesWanPortStatisticUnderrunPkts_Object = MibTableColumn
zxAnCesWanPortStatisticUnderrunPkts = _ZxAnCesWanPortStatisticUnderrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 3),
    _ZxAnCesWanPortStatisticUnderrunPkts_Type()
)
zxAnCesWanPortStatisticUnderrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticUnderrunPkts.setStatus("current")
_ZxAnCesWanPortStatisticLostPkts_Type = Unsigned32
_ZxAnCesWanPortStatisticLostPkts_Object = MibTableColumn
zxAnCesWanPortStatisticLostPkts = _ZxAnCesWanPortStatisticLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 4),
    _ZxAnCesWanPortStatisticLostPkts_Type()
)
zxAnCesWanPortStatisticLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticLostPkts.setStatus("current")
_ZxAnCesWanPortStatisticCurQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticCurQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticCurQueLen = _ZxAnCesWanPortStatisticCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 5),
    _ZxAnCesWanPortStatisticCurQueLen_Type()
)
zxAnCesWanPortStatisticCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticCurQueLen.setStatus("current")
_ZxAnCesWanPortStatisticAvgQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticAvgQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticAvgQueLen = _ZxAnCesWanPortStatisticAvgQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 6),
    _ZxAnCesWanPortStatisticAvgQueLen_Type()
)
zxAnCesWanPortStatisticAvgQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticAvgQueLen.setStatus("current")
_ZxAnCesWanPortStatisticMaxQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticMaxQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticMaxQueLen = _ZxAnCesWanPortStatisticMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 7),
    _ZxAnCesWanPortStatisticMaxQueLen_Type()
)
zxAnCesWanPortStatisticMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticMaxQueLen.setStatus("current")
_ZxAnCesWanPortStatisticMinQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticMinQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticMinQueLen = _ZxAnCesWanPortStatisticMinQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 8),
    _ZxAnCesWanPortStatisticMinQueLen_Type()
)
zxAnCesWanPortStatisticMinQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticMinQueLen.setStatus("current")
_ZxAnCesWanPortStatisticPktRxCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticPktRxCnt_Object = MibTableColumn
zxAnCesWanPortStatisticPktRxCnt = _ZxAnCesWanPortStatisticPktRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 9),
    _ZxAnCesWanPortStatisticPktRxCnt_Type()
)
zxAnCesWanPortStatisticPktRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticPktRxCnt.setStatus("current")
_ZxAnCesWanPortStatisticPktTxCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticPktTxCnt_Object = MibTableColumn
zxAnCesWanPortStatisticPktTxCnt = _ZxAnCesWanPortStatisticPktTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 10),
    _ZxAnCesWanPortStatisticPktTxCnt_Type()
)
zxAnCesWanPortStatisticPktTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticPktTxCnt.setStatus("current")
_ZxAnCesWanPortStatisticByteTxCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticByteTxCnt_Object = MibTableColumn
zxAnCesWanPortStatisticByteTxCnt = _ZxAnCesWanPortStatisticByteTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 11),
    _ZxAnCesWanPortStatisticByteTxCnt_Type()
)
zxAnCesWanPortStatisticByteTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticByteTxCnt.setStatus("current")
_ZxAnCesWanPortStatisticLBitCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticLBitCnt_Object = MibTableColumn
zxAnCesWanPortStatisticLBitCnt = _ZxAnCesWanPortStatisticLBitCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 12),
    _ZxAnCesWanPortStatisticLBitCnt_Type()
)
zxAnCesWanPortStatisticLBitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticLBitCnt.setStatus("current")
_ZxAnCesWanPortStatisticLBitSetTime_Type = Unsigned32
_ZxAnCesWanPortStatisticLBitSetTime_Object = MibTableColumn
zxAnCesWanPortStatisticLBitSetTime = _ZxAnCesWanPortStatisticLBitSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 13),
    _ZxAnCesWanPortStatisticLBitSetTime_Type()
)
zxAnCesWanPortStatisticLBitSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticLBitSetTime.setStatus("current")
_ZxAnCesWanPortStatisticRBitCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticRBitCnt_Object = MibTableColumn
zxAnCesWanPortStatisticRBitCnt = _ZxAnCesWanPortStatisticRBitCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 14),
    _ZxAnCesWanPortStatisticRBitCnt_Type()
)
zxAnCesWanPortStatisticRBitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticRBitCnt.setStatus("current")
_ZxAnCesWanPortStatisticRBitSetTime_Type = Unsigned32
_ZxAnCesWanPortStatisticRBitSetTime_Object = MibTableColumn
zxAnCesWanPortStatisticRBitSetTime = _ZxAnCesWanPortStatisticRBitSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 1, 1, 15),
    _ZxAnCesWanPortStatisticRBitSetTime_Type()
)
zxAnCesWanPortStatisticRBitSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticRBitSetTime.setStatus("current")
_ZxAnCesProtocolStatisticTable_Object = MibTable
zxAnCesProtocolStatisticTable = _ZxAnCesProtocolStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticTable.setStatus("current")
_ZxAnCesProtocolStatisticEntry_Object = MibTableRow
zxAnCesProtocolStatisticEntry = _ZxAnCesProtocolStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2, 1)
)
zxAnCesProtocolStatisticEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticEntry.setStatus("current")
_ZxAnCesProtocolStatisticProtMatchCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticProtMatchCnt_Object = MibTableColumn
zxAnCesProtocolStatisticProtMatchCnt = _ZxAnCesProtocolStatisticProtMatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2, 1, 1),
    _ZxAnCesProtocolStatisticProtMatchCnt_Type()
)
zxAnCesProtocolStatisticProtMatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticProtMatchCnt.setStatus("current")
_ZxAnCesProtocolStatisticProtNoMatchCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticProtNoMatchCnt_Object = MibTableColumn
zxAnCesProtocolStatisticProtNoMatchCnt = _ZxAnCesProtocolStatisticProtNoMatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2, 1, 2),
    _ZxAnCesProtocolStatisticProtNoMatchCnt_Type()
)
zxAnCesProtocolStatisticProtNoMatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticProtNoMatchCnt.setStatus("current")
_ZxAnCesProtocolStatisticClaNoMatchCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticClaNoMatchCnt_Object = MibTableColumn
zxAnCesProtocolStatisticClaNoMatchCnt = _ZxAnCesProtocolStatisticClaNoMatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2, 1, 3),
    _ZxAnCesProtocolStatisticClaNoMatchCnt_Type()
)
zxAnCesProtocolStatisticClaNoMatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticClaNoMatchCnt.setStatus("current")
_ZxAnCesProtocolStatisticVerifyFailCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticVerifyFailCnt_Object = MibTableColumn
zxAnCesProtocolStatisticVerifyFailCnt = _ZxAnCesProtocolStatisticVerifyFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2, 1, 4),
    _ZxAnCesProtocolStatisticVerifyFailCnt_Type()
)
zxAnCesProtocolStatisticVerifyFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticVerifyFailCnt.setStatus("current")
_ZxAnCesProtocolStatisticIP4CheckFailCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticIP4CheckFailCnt_Object = MibTableColumn
zxAnCesProtocolStatisticIP4CheckFailCnt = _ZxAnCesProtocolStatisticIP4CheckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 2, 1, 5),
    _ZxAnCesProtocolStatisticIP4CheckFailCnt_Type()
)
zxAnCesProtocolStatisticIP4CheckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticIP4CheckFailCnt.setStatus("current")
_ZxAnCesRfc1213StatisticTable_Object = MibTable
zxAnCesRfc1213StatisticTable = _ZxAnCesRfc1213StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticTable.setStatus("current")
_ZxAnCesRfc1213StatisticEntry_Object = MibTableRow
zxAnCesRfc1213StatisticEntry = _ZxAnCesRfc1213StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1)
)
zxAnCesRfc1213StatisticEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticEntry.setStatus("current")
_ZxAnCesRfc1213StatisticRxOctets_Type = Unsigned32
_ZxAnCesRfc1213StatisticRxOctets_Object = MibTableColumn
zxAnCesRfc1213StatisticRxOctets = _ZxAnCesRfc1213StatisticRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 1),
    _ZxAnCesRfc1213StatisticRxOctets_Type()
)
zxAnCesRfc1213StatisticRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticRxOctets.setStatus("current")
_ZxAnCesRfc1213StatisticRxUnicastPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticRxUnicastPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticRxUnicastPkts = _ZxAnCesRfc1213StatisticRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 2),
    _ZxAnCesRfc1213StatisticRxUnicastPkts_Type()
)
zxAnCesRfc1213StatisticRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticRxUnicastPkts.setStatus("current")
_ZxAnCesRfc1213StatisticRxMulBrdPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticRxMulBrdPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticRxMulBrdPkts = _ZxAnCesRfc1213StatisticRxMulBrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 3),
    _ZxAnCesRfc1213StatisticRxMulBrdPkts_Type()
)
zxAnCesRfc1213StatisticRxMulBrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticRxMulBrdPkts.setStatus("current")
_ZxAnCesRfc1213StatisticRxDiscardPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticRxDiscardPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticRxDiscardPkts = _ZxAnCesRfc1213StatisticRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 4),
    _ZxAnCesRfc1213StatisticRxDiscardPkts_Type()
)
zxAnCesRfc1213StatisticRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticRxDiscardPkts.setStatus("current")
_ZxAnCesRfc1213StatisticRxErrorPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticRxErrorPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticRxErrorPkts = _ZxAnCesRfc1213StatisticRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 5),
    _ZxAnCesRfc1213StatisticRxErrorPkts_Type()
)
zxAnCesRfc1213StatisticRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticRxErrorPkts.setStatus("current")
_ZxAnCesRfc1213StatisticRxUnknowProtPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticRxUnknowProtPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticRxUnknowProtPkts = _ZxAnCesRfc1213StatisticRxUnknowProtPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 6),
    _ZxAnCesRfc1213StatisticRxUnknowProtPkts_Type()
)
zxAnCesRfc1213StatisticRxUnknowProtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticRxUnknowProtPkts.setStatus("current")
_ZxAnCesRfc1213StatisticTxOctets_Type = Unsigned32
_ZxAnCesRfc1213StatisticTxOctets_Object = MibTableColumn
zxAnCesRfc1213StatisticTxOctets = _ZxAnCesRfc1213StatisticTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 7),
    _ZxAnCesRfc1213StatisticTxOctets_Type()
)
zxAnCesRfc1213StatisticTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticTxOctets.setStatus("current")
_ZxAnCesRfc1213StatisticTxUnicastPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticTxUnicastPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticTxUnicastPkts = _ZxAnCesRfc1213StatisticTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 8),
    _ZxAnCesRfc1213StatisticTxUnicastPkts_Type()
)
zxAnCesRfc1213StatisticTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticTxUnicastPkts.setStatus("current")
_ZxAnCesRfc1213StatisticTxMulBrdPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticTxMulBrdPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticTxMulBrdPkts = _ZxAnCesRfc1213StatisticTxMulBrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 9),
    _ZxAnCesRfc1213StatisticTxMulBrdPkts_Type()
)
zxAnCesRfc1213StatisticTxMulBrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticTxMulBrdPkts.setStatus("current")
_ZxAnCesRfc1213StatisticTxDiscardPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticTxDiscardPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticTxDiscardPkts = _ZxAnCesRfc1213StatisticTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 10),
    _ZxAnCesRfc1213StatisticTxDiscardPkts_Type()
)
zxAnCesRfc1213StatisticTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticTxDiscardPkts.setStatus("current")
_ZxAnCesRfc1213StatisticTxErrorPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticTxErrorPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticTxErrorPkts = _ZxAnCesRfc1213StatisticTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 11),
    _ZxAnCesRfc1213StatisticTxErrorPkts_Type()
)
zxAnCesRfc1213StatisticTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticTxErrorPkts.setStatus("current")
_ZxAnCesRfc1213StatisticOutBoundQueLen_Type = Unsigned32
_ZxAnCesRfc1213StatisticOutBoundQueLen_Object = MibTableColumn
zxAnCesRfc1213StatisticOutBoundQueLen = _ZxAnCesRfc1213StatisticOutBoundQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 3, 1, 12),
    _ZxAnCesRfc1213StatisticOutBoundQueLen_Type()
)
zxAnCesRfc1213StatisticOutBoundQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticOutBoundQueLen.setStatus("current")
_ZxAnCesRfc1757StatisticTable_Object = MibTable
zxAnCesRfc1757StatisticTable = _ZxAnCesRfc1757StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticTable.setStatus("current")
_ZxAnCesRfc1757StatisticEntry_Object = MibTableRow
zxAnCesRfc1757StatisticEntry = _ZxAnCesRfc1757StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1)
)
zxAnCesRfc1757StatisticEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticEntry.setStatus("current")
_ZxAnCesRfc1757StatisticDropCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticDropCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticDropCnt = _ZxAnCesRfc1757StatisticDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 1),
    _ZxAnCesRfc1757StatisticDropCnt_Type()
)
zxAnCesRfc1757StatisticDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticDropCnt.setStatus("current")
_ZxAnCesRfc1757StatisticMulticastPkts_Type = Unsigned32
_ZxAnCesRfc1757StatisticMulticastPkts_Object = MibTableColumn
zxAnCesRfc1757StatisticMulticastPkts = _ZxAnCesRfc1757StatisticMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 2),
    _ZxAnCesRfc1757StatisticMulticastPkts_Type()
)
zxAnCesRfc1757StatisticMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticMulticastPkts.setStatus("current")
_ZxAnCesRfc1757StatisticBroadcastPkts_Type = Unsigned32
_ZxAnCesRfc1757StatisticBroadcastPkts_Object = MibTableColumn
zxAnCesRfc1757StatisticBroadcastPkts = _ZxAnCesRfc1757StatisticBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 3),
    _ZxAnCesRfc1757StatisticBroadcastPkts_Type()
)
zxAnCesRfc1757StatisticBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticBroadcastPkts.setStatus("current")
_ZxAnCesRfc1757StatisticUndersizeFrmCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticUndersizeFrmCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticUndersizeFrmCnt = _ZxAnCesRfc1757StatisticUndersizeFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 4),
    _ZxAnCesRfc1757StatisticUndersizeFrmCnt_Type()
)
zxAnCesRfc1757StatisticUndersizeFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticUndersizeFrmCnt.setStatus("current")
_ZxAnCesRfc1757StatisticFragmentsCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticFragmentsCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticFragmentsCnt = _ZxAnCesRfc1757StatisticFragmentsCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 5),
    _ZxAnCesRfc1757StatisticFragmentsCnt_Type()
)
zxAnCesRfc1757StatisticFragmentsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticFragmentsCnt.setStatus("current")
_ZxAnCesRfc1757StatisticPkts64_Type = Unsigned32
_ZxAnCesRfc1757StatisticPkts64_Object = MibTableColumn
zxAnCesRfc1757StatisticPkts64 = _ZxAnCesRfc1757StatisticPkts64_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 6),
    _ZxAnCesRfc1757StatisticPkts64_Type()
)
zxAnCesRfc1757StatisticPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPkts64.setStatus("current")
_ZxAnCesRfc1757StatisticPkts65to127_Type = Unsigned32
_ZxAnCesRfc1757StatisticPkts65to127_Object = MibTableColumn
zxAnCesRfc1757StatisticPkts65to127 = _ZxAnCesRfc1757StatisticPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 7),
    _ZxAnCesRfc1757StatisticPkts65to127_Type()
)
zxAnCesRfc1757StatisticPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPkts65to127.setStatus("current")
_ZxAnCesRfc1757StatisticPkts128to255_Type = Unsigned32
_ZxAnCesRfc1757StatisticPkts128to255_Object = MibTableColumn
zxAnCesRfc1757StatisticPkts128to255 = _ZxAnCesRfc1757StatisticPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 8),
    _ZxAnCesRfc1757StatisticPkts128to255_Type()
)
zxAnCesRfc1757StatisticPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPkts128to255.setStatus("current")
_ZxAnCesRfc1757StatisticPkts256to511_Type = Unsigned32
_ZxAnCesRfc1757StatisticPkts256to511_Object = MibTableColumn
zxAnCesRfc1757StatisticPkts256to511 = _ZxAnCesRfc1757StatisticPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 9),
    _ZxAnCesRfc1757StatisticPkts256to511_Type()
)
zxAnCesRfc1757StatisticPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPkts256to511.setStatus("current")
_ZxAnCesRfc1757StatisticPkts512to1023_Type = Unsigned32
_ZxAnCesRfc1757StatisticPkts512to1023_Object = MibTableColumn
zxAnCesRfc1757StatisticPkts512to1023 = _ZxAnCesRfc1757StatisticPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 10),
    _ZxAnCesRfc1757StatisticPkts512to1023_Type()
)
zxAnCesRfc1757StatisticPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPkts512to1023.setStatus("current")
_ZxAnCesRfc1757StatisticPkts1024to1518_Type = Unsigned32
_ZxAnCesRfc1757StatisticPkts1024to1518_Object = MibTableColumn
zxAnCesRfc1757StatisticPkts1024to1518 = _ZxAnCesRfc1757StatisticPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 11),
    _ZxAnCesRfc1757StatisticPkts1024to1518_Type()
)
zxAnCesRfc1757StatisticPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPkts1024to1518.setStatus("current")
_ZxAnCesRfc1757StatisticPktsOversize_Type = Unsigned32
_ZxAnCesRfc1757StatisticPktsOversize_Object = MibTableColumn
zxAnCesRfc1757StatisticPktsOversize = _ZxAnCesRfc1757StatisticPktsOversize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 12),
    _ZxAnCesRfc1757StatisticPktsOversize_Type()
)
zxAnCesRfc1757StatisticPktsOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticPktsOversize.setStatus("current")
_ZxAnCesRfc1757StatisticJabberFrmCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticJabberFrmCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticJabberFrmCnt = _ZxAnCesRfc1757StatisticJabberFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 13),
    _ZxAnCesRfc1757StatisticJabberFrmCnt_Type()
)
zxAnCesRfc1757StatisticJabberFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticJabberFrmCnt.setStatus("current")
_ZxAnCesRfc1757StatisticBytesRx_Type = Unsigned32
_ZxAnCesRfc1757StatisticBytesRx_Object = MibTableColumn
zxAnCesRfc1757StatisticBytesRx = _ZxAnCesRfc1757StatisticBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 14),
    _ZxAnCesRfc1757StatisticBytesRx_Type()
)
zxAnCesRfc1757StatisticBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticBytesRx.setStatus("current")
_ZxAnCesRfc1757StatisticFramesRx_Type = Unsigned32
_ZxAnCesRfc1757StatisticFramesRx_Object = MibTableColumn
zxAnCesRfc1757StatisticFramesRx = _ZxAnCesRfc1757StatisticFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 15),
    _ZxAnCesRfc1757StatisticFramesRx_Type()
)
zxAnCesRfc1757StatisticFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticFramesRx.setStatus("current")
_ZxAnCesRfc1757StatisticCollosions_Type = Unsigned32
_ZxAnCesRfc1757StatisticCollosions_Object = MibTableColumn
zxAnCesRfc1757StatisticCollosions = _ZxAnCesRfc1757StatisticCollosions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 16),
    _ZxAnCesRfc1757StatisticCollosions_Type()
)
zxAnCesRfc1757StatisticCollosions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticCollosions.setStatus("current")
_ZxAnCesRfc1757StatisticCrcAlignErr_Type = Unsigned32
_ZxAnCesRfc1757StatisticCrcAlignErr_Object = MibTableColumn
zxAnCesRfc1757StatisticCrcAlignErr = _ZxAnCesRfc1757StatisticCrcAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 4, 1, 17),
    _ZxAnCesRfc1757StatisticCrcAlignErr_Type()
)
zxAnCesRfc1757StatisticCrcAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticCrcAlignErr.setStatus("current")
_ZxAnCesSdhRsB1StatisticTable_Object = MibTable
zxAnCesSdhRsB1StatisticTable = _ZxAnCesSdhRsB1StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1StatisticTable.setStatus("current")
_ZxAnCesSdhRsB1StatisticEntry_Object = MibTableRow
zxAnCesSdhRsB1StatisticEntry = _ZxAnCesSdhRsB1StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5, 1)
)
zxAnCesSdhRsB1StatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1StatisticEntry.setStatus("current")
_ZxAnCesSdhRsB1Statistic_Type = Unsigned32
_ZxAnCesSdhRsB1Statistic_Object = MibTableColumn
zxAnCesSdhRsB1Statistic = _ZxAnCesSdhRsB1Statistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5, 1, 1),
    _ZxAnCesSdhRsB1Statistic_Type()
)
zxAnCesSdhRsB1Statistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1Statistic.setStatus("current")
_ZxAnCesSdhRsB1BBEStat_Type = Unsigned32
_ZxAnCesSdhRsB1BBEStat_Object = MibTableColumn
zxAnCesSdhRsB1BBEStat = _ZxAnCesSdhRsB1BBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5, 1, 2),
    _ZxAnCesSdhRsB1BBEStat_Type()
)
zxAnCesSdhRsB1BBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1BBEStat.setStatus("current")
_ZxAnCesSdhRsB1ESStat_Type = Unsigned32
_ZxAnCesSdhRsB1ESStat_Object = MibTableColumn
zxAnCesSdhRsB1ESStat = _ZxAnCesSdhRsB1ESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5, 1, 3),
    _ZxAnCesSdhRsB1ESStat_Type()
)
zxAnCesSdhRsB1ESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1ESStat.setStatus("current")
_ZxAnCesSdhRsB1SESStat_Type = Unsigned32
_ZxAnCesSdhRsB1SESStat_Object = MibTableColumn
zxAnCesSdhRsB1SESStat = _ZxAnCesSdhRsB1SESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5, 1, 4),
    _ZxAnCesSdhRsB1SESStat_Type()
)
zxAnCesSdhRsB1SESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1SESStat.setStatus("current")
_ZxAnCesSdhRsB1UASStat_Type = Unsigned32
_ZxAnCesSdhRsB1UASStat_Object = MibTableColumn
zxAnCesSdhRsB1UASStat = _ZxAnCesSdhRsB1UASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 5, 1, 5),
    _ZxAnCesSdhRsB1UASStat_Type()
)
zxAnCesSdhRsB1UASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1UASStat.setStatus("current")
_ZxAnCesSdhMsB2StatisticTable_Object = MibTable
zxAnCesSdhMsB2StatisticTable = _ZxAnCesSdhMsB2StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2StatisticTable.setStatus("current")
_ZxAnCesSdhMsB2StatisticEntry_Object = MibTableRow
zxAnCesSdhMsB2StatisticEntry = _ZxAnCesSdhMsB2StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6, 1)
)
zxAnCesSdhMsB2StatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2StatisticEntry.setStatus("current")
_ZxAnCesSdhMsB2Statistic_Type = Unsigned32
_ZxAnCesSdhMsB2Statistic_Object = MibTableColumn
zxAnCesSdhMsB2Statistic = _ZxAnCesSdhMsB2Statistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6, 1, 1),
    _ZxAnCesSdhMsB2Statistic_Type()
)
zxAnCesSdhMsB2Statistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2Statistic.setStatus("current")
_ZxAnCesSdhMsB2BBEStat_Type = Unsigned32
_ZxAnCesSdhMsB2BBEStat_Object = MibTableColumn
zxAnCesSdhMsB2BBEStat = _ZxAnCesSdhMsB2BBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6, 1, 2),
    _ZxAnCesSdhMsB2BBEStat_Type()
)
zxAnCesSdhMsB2BBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2BBEStat.setStatus("current")
_ZxAnCesSdhMsB2ESStat_Type = Unsigned32
_ZxAnCesSdhMsB2ESStat_Object = MibTableColumn
zxAnCesSdhMsB2ESStat = _ZxAnCesSdhMsB2ESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6, 1, 3),
    _ZxAnCesSdhMsB2ESStat_Type()
)
zxAnCesSdhMsB2ESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ESStat.setStatus("current")
_ZxAnCesSdhMsB2SESStat_Type = Unsigned32
_ZxAnCesSdhMsB2SESStat_Object = MibTableColumn
zxAnCesSdhMsB2SESStat = _ZxAnCesSdhMsB2SESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6, 1, 4),
    _ZxAnCesSdhMsB2SESStat_Type()
)
zxAnCesSdhMsB2SESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2SESStat.setStatus("current")
_ZxAnCesSdhMsB2UASStat_Type = Unsigned32
_ZxAnCesSdhMsB2UASStat_Object = MibTableColumn
zxAnCesSdhMsB2UASStat = _ZxAnCesSdhMsB2UASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 6, 1, 5),
    _ZxAnCesSdhMsB2UASStat_Type()
)
zxAnCesSdhMsB2UASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2UASStat.setStatus("current")
_ZxAnCesSdhMsB2ReiStatisticTable_Object = MibTable
zxAnCesSdhMsB2ReiStatisticTable = _ZxAnCesSdhMsB2ReiStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiStatisticTable.setStatus("current")
_ZxAnCesSdhMsB2ReiStatisticEntry_Object = MibTableRow
zxAnCesSdhMsB2ReiStatisticEntry = _ZxAnCesSdhMsB2ReiStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7, 1)
)
zxAnCesSdhMsB2ReiStatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiStatisticEntry.setStatus("current")
_ZxAnCesSdhMsB2ReiStatistic_Type = Unsigned32
_ZxAnCesSdhMsB2ReiStatistic_Object = MibTableColumn
zxAnCesSdhMsB2ReiStatistic = _ZxAnCesSdhMsB2ReiStatistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7, 1, 1),
    _ZxAnCesSdhMsB2ReiStatistic_Type()
)
zxAnCesSdhMsB2ReiStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiStatistic.setStatus("current")
_ZxAnCesSdhMsB2ReiBBEStat_Type = Unsigned32
_ZxAnCesSdhMsB2ReiBBEStat_Object = MibTableColumn
zxAnCesSdhMsB2ReiBBEStat = _ZxAnCesSdhMsB2ReiBBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7, 1, 2),
    _ZxAnCesSdhMsB2ReiBBEStat_Type()
)
zxAnCesSdhMsB2ReiBBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiBBEStat.setStatus("current")
_ZxAnCesSdhMsB2ReiESStat_Type = Unsigned32
_ZxAnCesSdhMsB2ReiESStat_Object = MibTableColumn
zxAnCesSdhMsB2ReiESStat = _ZxAnCesSdhMsB2ReiESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7, 1, 3),
    _ZxAnCesSdhMsB2ReiESStat_Type()
)
zxAnCesSdhMsB2ReiESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiESStat.setStatus("current")
_ZxAnCesSdhMsB2ReiSESStat_Type = Unsigned32
_ZxAnCesSdhMsB2ReiSESStat_Object = MibTableColumn
zxAnCesSdhMsB2ReiSESStat = _ZxAnCesSdhMsB2ReiSESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7, 1, 4),
    _ZxAnCesSdhMsB2ReiSESStat_Type()
)
zxAnCesSdhMsB2ReiSESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiSESStat.setStatus("current")
_ZxAnCesSdhMsB2ReiUASStat_Type = Unsigned32
_ZxAnCesSdhMsB2ReiUASStat_Object = MibTableColumn
zxAnCesSdhMsB2ReiUASStat = _ZxAnCesSdhMsB2ReiUASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 7, 1, 5),
    _ZxAnCesSdhMsB2ReiUASStat_Type()
)
zxAnCesSdhMsB2ReiUASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiUASStat.setStatus("current")
_ZxAnCesSdhVc12V5StatisticTable_Object = MibTable
zxAnCesSdhVc12V5StatisticTable = _ZxAnCesSdhVc12V5StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5StatisticTable.setStatus("current")
_ZxAnCesSdhVc12V5StatisticEntry_Object = MibTableRow
zxAnCesSdhVc12V5StatisticEntry = _ZxAnCesSdhVc12V5StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8, 1)
)
zxAnCesSdhVc12V5StatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5StatisticEntry.setStatus("current")
_ZxAnCesSdhVc12V5Statistic_Type = Unsigned32
_ZxAnCesSdhVc12V5Statistic_Object = MibTableColumn
zxAnCesSdhVc12V5Statistic = _ZxAnCesSdhVc12V5Statistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8, 1, 1),
    _ZxAnCesSdhVc12V5Statistic_Type()
)
zxAnCesSdhVc12V5Statistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5Statistic.setStatus("current")
_ZxAnCesSdhVc12V5BBEStat_Type = Unsigned32
_ZxAnCesSdhVc12V5BBEStat_Object = MibTableColumn
zxAnCesSdhVc12V5BBEStat = _ZxAnCesSdhVc12V5BBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8, 1, 2),
    _ZxAnCesSdhVc12V5BBEStat_Type()
)
zxAnCesSdhVc12V5BBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5BBEStat.setStatus("current")
_ZxAnCesSdhVc12V5ESStat_Type = Unsigned32
_ZxAnCesSdhVc12V5ESStat_Object = MibTableColumn
zxAnCesSdhVc12V5ESStat = _ZxAnCesSdhVc12V5ESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8, 1, 3),
    _ZxAnCesSdhVc12V5ESStat_Type()
)
zxAnCesSdhVc12V5ESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ESStat.setStatus("current")
_ZxAnCesSdhVc12V5SESStat_Type = Unsigned32
_ZxAnCesSdhVc12V5SESStat_Object = MibTableColumn
zxAnCesSdhVc12V5SESStat = _ZxAnCesSdhVc12V5SESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8, 1, 4),
    _ZxAnCesSdhVc12V5SESStat_Type()
)
zxAnCesSdhVc12V5SESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5SESStat.setStatus("current")
_ZxAnCesSdhVc12V5UASStat_Type = Unsigned32
_ZxAnCesSdhVc12V5UASStat_Object = MibTableColumn
zxAnCesSdhVc12V5UASStat = _ZxAnCesSdhVc12V5UASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 8, 1, 5),
    _ZxAnCesSdhVc12V5UASStat_Type()
)
zxAnCesSdhVc12V5UASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5UASStat.setStatus("current")
_ZxAnCesSdhVc12V5ReiStatisticTable_Object = MibTable
zxAnCesSdhVc12V5ReiStatisticTable = _ZxAnCesSdhVc12V5ReiStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiStatisticTable.setStatus("current")
_ZxAnCesSdhVc12V5ReiStatisticEntry_Object = MibTableRow
zxAnCesSdhVc12V5ReiStatisticEntry = _ZxAnCesSdhVc12V5ReiStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9, 1)
)
zxAnCesSdhVc12V5ReiStatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiStatisticEntry.setStatus("current")
_ZxAnCesSdhVc12V5ReiStatistic_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiStatistic_Object = MibTableColumn
zxAnCesSdhVc12V5ReiStatistic = _ZxAnCesSdhVc12V5ReiStatistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9, 1, 1),
    _ZxAnCesSdhVc12V5ReiStatistic_Type()
)
zxAnCesSdhVc12V5ReiStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiStatistic.setStatus("current")
_ZxAnCesSdhVc12V5ReiBBEStat_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiBBEStat_Object = MibTableColumn
zxAnCesSdhVc12V5ReiBBEStat = _ZxAnCesSdhVc12V5ReiBBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9, 1, 2),
    _ZxAnCesSdhVc12V5ReiBBEStat_Type()
)
zxAnCesSdhVc12V5ReiBBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiBBEStat.setStatus("current")
_ZxAnCesSdhVc12V5ReiESStat_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiESStat_Object = MibTableColumn
zxAnCesSdhVc12V5ReiESStat = _ZxAnCesSdhVc12V5ReiESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9, 1, 3),
    _ZxAnCesSdhVc12V5ReiESStat_Type()
)
zxAnCesSdhVc12V5ReiESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiESStat.setStatus("current")
_ZxAnCesSdhVc12V5ReiSESStat_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiSESStat_Object = MibTableColumn
zxAnCesSdhVc12V5ReiSESStat = _ZxAnCesSdhVc12V5ReiSESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9, 1, 4),
    _ZxAnCesSdhVc12V5ReiSESStat_Type()
)
zxAnCesSdhVc12V5ReiSESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiSESStat.setStatus("current")
_ZxAnCesSdhVc12V5ReiUASStat_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiUASStat_Object = MibTableColumn
zxAnCesSdhVc12V5ReiUASStat = _ZxAnCesSdhVc12V5ReiUASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 9, 1, 5),
    _ZxAnCesSdhVc12V5ReiUASStat_Type()
)
zxAnCesSdhVc12V5ReiUASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiUASStat.setStatus("current")
_ZxAnCesSdhVc4B3StatisticTable_Object = MibTable
zxAnCesSdhVc4B3StatisticTable = _ZxAnCesSdhVc4B3StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3StatisticTable.setStatus("current")
_ZxAnCesSdhVc4B3StatisticEntry_Object = MibTableRow
zxAnCesSdhVc4B3StatisticEntry = _ZxAnCesSdhVc4B3StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10, 1)
)
zxAnCesSdhVc4B3StatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3StatisticEntry.setStatus("current")
_ZxAnCesSdhVc4B3Statistic_Type = Unsigned32
_ZxAnCesSdhVc4B3Statistic_Object = MibTableColumn
zxAnCesSdhVc4B3Statistic = _ZxAnCesSdhVc4B3Statistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10, 1, 1),
    _ZxAnCesSdhVc4B3Statistic_Type()
)
zxAnCesSdhVc4B3Statistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3Statistic.setStatus("current")
_ZxAnCesSdhVc4B3BBEStat_Type = Unsigned32
_ZxAnCesSdhVc4B3BBEStat_Object = MibTableColumn
zxAnCesSdhVc4B3BBEStat = _ZxAnCesSdhVc4B3BBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10, 1, 2),
    _ZxAnCesSdhVc4B3BBEStat_Type()
)
zxAnCesSdhVc4B3BBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3BBEStat.setStatus("current")
_ZxAnCesSdhVc4B3ESStat_Type = Unsigned32
_ZxAnCesSdhVc4B3ESStat_Object = MibTableColumn
zxAnCesSdhVc4B3ESStat = _ZxAnCesSdhVc4B3ESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10, 1, 3),
    _ZxAnCesSdhVc4B3ESStat_Type()
)
zxAnCesSdhVc4B3ESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ESStat.setStatus("current")
_ZxAnCesSdhVc4B3SESStat_Type = Unsigned32
_ZxAnCesSdhVc4B3SESStat_Object = MibTableColumn
zxAnCesSdhVc4B3SESStat = _ZxAnCesSdhVc4B3SESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10, 1, 4),
    _ZxAnCesSdhVc4B3SESStat_Type()
)
zxAnCesSdhVc4B3SESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3SESStat.setStatus("current")
_ZxAnCesSdhVc4B3UASStat_Type = Unsigned32
_ZxAnCesSdhVc4B3UASStat_Object = MibTableColumn
zxAnCesSdhVc4B3UASStat = _ZxAnCesSdhVc4B3UASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 10, 1, 5),
    _ZxAnCesSdhVc4B3UASStat_Type()
)
zxAnCesSdhVc4B3UASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3UASStat.setStatus("current")
_ZxAnCesSdhVc4B3ReiStatisticTable_Object = MibTable
zxAnCesSdhVc4B3ReiStatisticTable = _ZxAnCesSdhVc4B3ReiStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiStatisticTable.setStatus("current")
_ZxAnCesSdhVc4B3ReiStatisticEntry_Object = MibTableRow
zxAnCesSdhVc4B3ReiStatisticEntry = _ZxAnCesSdhVc4B3ReiStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11, 1)
)
zxAnCesSdhVc4B3ReiStatisticEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiStatisticEntry.setStatus("current")
_ZxAnCesSdhVc4B3ReiStatistic_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiStatistic_Object = MibTableColumn
zxAnCesSdhVc4B3ReiStatistic = _ZxAnCesSdhVc4B3ReiStatistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11, 1, 1),
    _ZxAnCesSdhVc4B3ReiStatistic_Type()
)
zxAnCesSdhVc4B3ReiStatistic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiStatistic.setStatus("current")
_ZxAnCesSdhVc4B3ReiBBEStat_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiBBEStat_Object = MibTableColumn
zxAnCesSdhVc4B3ReiBBEStat = _ZxAnCesSdhVc4B3ReiBBEStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11, 1, 2),
    _ZxAnCesSdhVc4B3ReiBBEStat_Type()
)
zxAnCesSdhVc4B3ReiBBEStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiBBEStat.setStatus("current")
_ZxAnCesSdhVc4B3ReiESStat_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiESStat_Object = MibTableColumn
zxAnCesSdhVc4B3ReiESStat = _ZxAnCesSdhVc4B3ReiESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11, 1, 3),
    _ZxAnCesSdhVc4B3ReiESStat_Type()
)
zxAnCesSdhVc4B3ReiESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiESStat.setStatus("current")
_ZxAnCesSdhVc4B3ReiSESStat_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiSESStat_Object = MibTableColumn
zxAnCesSdhVc4B3ReiSESStat = _ZxAnCesSdhVc4B3ReiSESStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11, 1, 4),
    _ZxAnCesSdhVc4B3ReiSESStat_Type()
)
zxAnCesSdhVc4B3ReiSESStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiSESStat.setStatus("current")
_ZxAnCesSdhVc4B3ReiUASStat_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiUASStat_Object = MibTableColumn
zxAnCesSdhVc4B3ReiUASStat = _ZxAnCesSdhVc4B3ReiUASStat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 11, 1, 5),
    _ZxAnCesSdhVc4B3ReiUASStat_Type()
)
zxAnCesSdhVc4B3ReiUASStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiUASStat.setStatus("current")
_ZxAnCesE1CurrentTable_Object = MibTable
zxAnCesE1CurrentTable = _ZxAnCesE1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 12)
)
if mibBuilder.loadTexts:
    zxAnCesE1CurrentTable.setStatus("current")
_ZxAnCesE1CurrentEntry_Object = MibTableRow
zxAnCesE1CurrentEntry = _ZxAnCesE1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 12, 1)
)
zxAnCesE1CurrentEntry.setIndexNames(
    (0, "ZXCESPERFORMANCE-MIB", "zxAnCesE1CurrentIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesE1CurrentEntry.setStatus("current")
_ZxAnCesE1CurrentIndex_Type = ZxAnIfindex
_ZxAnCesE1CurrentIndex_Object = MibTableColumn
zxAnCesE1CurrentIndex = _ZxAnCesE1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 12, 1, 1),
    _ZxAnCesE1CurrentIndex_Type()
)
zxAnCesE1CurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCesE1CurrentIndex.setStatus("current")
_ZxAnCesE1Efs_Type = Gauge32
_ZxAnCesE1Efs_Object = MibTableColumn
zxAnCesE1Efs = _ZxAnCesE1Efs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 1, 12, 1, 2),
    _ZxAnCesE1Efs_Type()
)
zxAnCesE1Efs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesE1Efs.setStatus("current")
_ZxAnCesPmHistory_ObjectIdentity = ObjectIdentity
zxAnCesPmHistory = _ZxAnCesPmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2)
)
_ZxAnCesWanPortStatisticHistoryTable_Object = MibTable
zxAnCesWanPortStatisticHistoryTable = _ZxAnCesWanPortStatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryTable.setStatus("current")
_ZxAnCesWanPortStatisticHistoryEntry_Object = MibTableRow
zxAnCesWanPortStatisticHistoryEntry = _ZxAnCesWanPortStatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1)
)
zxAnCesWanPortStatisticHistoryEntry.setIndexNames(
    (0, "ZXPW-STD-MIB", "zxPwIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryEntry.setStatus("current")
_ZxAnCesWanPortStatisticHistoryEarlyPkts_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryEarlyPkts_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryEarlyPkts = _ZxAnCesWanPortStatisticHistoryEarlyPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 1),
    _ZxAnCesWanPortStatisticHistoryEarlyPkts_Type()
)
zxAnCesWanPortStatisticHistoryEarlyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryEarlyPkts.setStatus("current")
_ZxAnCesWanPortStatisticHistoryLatePkts_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryLatePkts_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryLatePkts = _ZxAnCesWanPortStatisticHistoryLatePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 2),
    _ZxAnCesWanPortStatisticHistoryLatePkts_Type()
)
zxAnCesWanPortStatisticHistoryLatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryLatePkts.setStatus("current")
_ZxAnCesWanPortStatisticHistoryUnderrunPkts_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryUnderrunPkts_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryUnderrunPkts = _ZxAnCesWanPortStatisticHistoryUnderrunPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 3),
    _ZxAnCesWanPortStatisticHistoryUnderrunPkts_Type()
)
zxAnCesWanPortStatisticHistoryUnderrunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryUnderrunPkts.setStatus("current")
_ZxAnCesWanPortStatisticHistoryLostPkts_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryLostPkts_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryLostPkts = _ZxAnCesWanPortStatisticHistoryLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 4),
    _ZxAnCesWanPortStatisticHistoryLostPkts_Type()
)
zxAnCesWanPortStatisticHistoryLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryLostPkts.setStatus("current")
_ZxAnCesWanPortStatisticHistoryCurQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryCurQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryCurQueLen = _ZxAnCesWanPortStatisticHistoryCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 5),
    _ZxAnCesWanPortStatisticHistoryCurQueLen_Type()
)
zxAnCesWanPortStatisticHistoryCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryCurQueLen.setStatus("current")
_ZxAnCesWanPortStatisticHistoryAvgQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryAvgQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryAvgQueLen = _ZxAnCesWanPortStatisticHistoryAvgQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 6),
    _ZxAnCesWanPortStatisticHistoryAvgQueLen_Type()
)
zxAnCesWanPortStatisticHistoryAvgQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryAvgQueLen.setStatus("current")
_ZxAnCesWanPortStatisticHistoryMaxQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryMaxQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryMaxQueLen = _ZxAnCesWanPortStatisticHistoryMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 7),
    _ZxAnCesWanPortStatisticHistoryMaxQueLen_Type()
)
zxAnCesWanPortStatisticHistoryMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryMaxQueLen.setStatus("current")
_ZxAnCesWanPortStatisticHistoryMinQueLen_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryMinQueLen_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryMinQueLen = _ZxAnCesWanPortStatisticHistoryMinQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 8),
    _ZxAnCesWanPortStatisticHistoryMinQueLen_Type()
)
zxAnCesWanPortStatisticHistoryMinQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryMinQueLen.setStatus("current")
_ZxAnCesWanPortStatisticHistoryPktRxCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryPktRxCnt_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryPktRxCnt = _ZxAnCesWanPortStatisticHistoryPktRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 9),
    _ZxAnCesWanPortStatisticHistoryPktRxCnt_Type()
)
zxAnCesWanPortStatisticHistoryPktRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryPktRxCnt.setStatus("current")
_ZxAnCesWanPortStatisticHistoryPktTxCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryPktTxCnt_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryPktTxCnt = _ZxAnCesWanPortStatisticHistoryPktTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 10),
    _ZxAnCesWanPortStatisticHistoryPktTxCnt_Type()
)
zxAnCesWanPortStatisticHistoryPktTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryPktTxCnt.setStatus("current")
_ZxAnCesWanPortStatisticHistoryByteTxCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryByteTxCnt_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryByteTxCnt = _ZxAnCesWanPortStatisticHistoryByteTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 11),
    _ZxAnCesWanPortStatisticHistoryByteTxCnt_Type()
)
zxAnCesWanPortStatisticHistoryByteTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryByteTxCnt.setStatus("current")
_ZxAnCesWanPortStatisticHistoryLBitCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryLBitCnt_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryLBitCnt = _ZxAnCesWanPortStatisticHistoryLBitCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 12),
    _ZxAnCesWanPortStatisticHistoryLBitCnt_Type()
)
zxAnCesWanPortStatisticHistoryLBitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryLBitCnt.setStatus("current")
_ZxAnCesWanPortStatisticHistoryLBitSetTime_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryLBitSetTime_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryLBitSetTime = _ZxAnCesWanPortStatisticHistoryLBitSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 13),
    _ZxAnCesWanPortStatisticHistoryLBitSetTime_Type()
)
zxAnCesWanPortStatisticHistoryLBitSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryLBitSetTime.setStatus("current")
_ZxAnCesWanPortStatisticHistoryRBitCnt_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryRBitCnt_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryRBitCnt = _ZxAnCesWanPortStatisticHistoryRBitCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 14),
    _ZxAnCesWanPortStatisticHistoryRBitCnt_Type()
)
zxAnCesWanPortStatisticHistoryRBitCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryRBitCnt.setStatus("current")
_ZxAnCesWanPortStatisticHistoryRBitSetTime_Type = Unsigned32
_ZxAnCesWanPortStatisticHistoryRBitSetTime_Object = MibTableColumn
zxAnCesWanPortStatisticHistoryRBitSetTime = _ZxAnCesWanPortStatisticHistoryRBitSetTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 1, 1, 15),
    _ZxAnCesWanPortStatisticHistoryRBitSetTime_Type()
)
zxAnCesWanPortStatisticHistoryRBitSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesWanPortStatisticHistoryRBitSetTime.setStatus("current")
_ZxAnCesProtocolStatisticHistoryTable_Object = MibTable
zxAnCesProtocolStatisticHistoryTable = _ZxAnCesProtocolStatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryTable.setStatus("current")
_ZxAnCesProtocolStatisticHistoryEntry_Object = MibTableRow
zxAnCesProtocolStatisticHistoryEntry = _ZxAnCesProtocolStatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2, 1)
)
zxAnCesProtocolStatisticHistoryEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryEntry.setStatus("current")
_ZxAnCesProtocolStatisticHistoryProtMatchCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticHistoryProtMatchCnt_Object = MibTableColumn
zxAnCesProtocolStatisticHistoryProtMatchCnt = _ZxAnCesProtocolStatisticHistoryProtMatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2, 1, 1),
    _ZxAnCesProtocolStatisticHistoryProtMatchCnt_Type()
)
zxAnCesProtocolStatisticHistoryProtMatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryProtMatchCnt.setStatus("current")
_ZxAnCesProtocolStatisticHistoryProtNoMatchCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticHistoryProtNoMatchCnt_Object = MibTableColumn
zxAnCesProtocolStatisticHistoryProtNoMatchCnt = _ZxAnCesProtocolStatisticHistoryProtNoMatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2, 1, 2),
    _ZxAnCesProtocolStatisticHistoryProtNoMatchCnt_Type()
)
zxAnCesProtocolStatisticHistoryProtNoMatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryProtNoMatchCnt.setStatus("current")
_ZxAnCesProtocolStatisticHistoryClaNoMatchCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticHistoryClaNoMatchCnt_Object = MibTableColumn
zxAnCesProtocolStatisticHistoryClaNoMatchCnt = _ZxAnCesProtocolStatisticHistoryClaNoMatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2, 1, 3),
    _ZxAnCesProtocolStatisticHistoryClaNoMatchCnt_Type()
)
zxAnCesProtocolStatisticHistoryClaNoMatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryClaNoMatchCnt.setStatus("current")
_ZxAnCesProtocolStatisticHistoryVerifyFailCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticHistoryVerifyFailCnt_Object = MibTableColumn
zxAnCesProtocolStatisticHistoryVerifyFailCnt = _ZxAnCesProtocolStatisticHistoryVerifyFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2, 1, 4),
    _ZxAnCesProtocolStatisticHistoryVerifyFailCnt_Type()
)
zxAnCesProtocolStatisticHistoryVerifyFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryVerifyFailCnt.setStatus("current")
_ZxAnCesProtocolStatisticHistoryIP4CheckFailCnt_Type = Unsigned32
_ZxAnCesProtocolStatisticHistoryIP4CheckFailCnt_Object = MibTableColumn
zxAnCesProtocolStatisticHistoryIP4CheckFailCnt = _ZxAnCesProtocolStatisticHistoryIP4CheckFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 2, 1, 5),
    _ZxAnCesProtocolStatisticHistoryIP4CheckFailCnt_Type()
)
zxAnCesProtocolStatisticHistoryIP4CheckFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesProtocolStatisticHistoryIP4CheckFailCnt.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryTable_Object = MibTable
zxAnCesRfc1213StatisticHistoryTable = _ZxAnCesRfc1213StatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryTable.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryEntry_Object = MibTableRow
zxAnCesRfc1213StatisticHistoryEntry = _ZxAnCesRfc1213StatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1)
)
zxAnCesRfc1213StatisticHistoryEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryEntry.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryRxOctets_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryRxOctets_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryRxOctets = _ZxAnCesRfc1213StatisticHistoryRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 1),
    _ZxAnCesRfc1213StatisticHistoryRxOctets_Type()
)
zxAnCesRfc1213StatisticHistoryRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryRxOctets.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryRxUnicastPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryRxUnicastPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryRxUnicastPkts = _ZxAnCesRfc1213StatisticHistoryRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 2),
    _ZxAnCesRfc1213StatisticHistoryRxUnicastPkts_Type()
)
zxAnCesRfc1213StatisticHistoryRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryRxUnicastPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryRxMulBrdPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryRxMulBrdPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryRxMulBrdPkts = _ZxAnCesRfc1213StatisticHistoryRxMulBrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 3),
    _ZxAnCesRfc1213StatisticHistoryRxMulBrdPkts_Type()
)
zxAnCesRfc1213StatisticHistoryRxMulBrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryRxMulBrdPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryRxDiscardPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryRxDiscardPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryRxDiscardPkts = _ZxAnCesRfc1213StatisticHistoryRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 4),
    _ZxAnCesRfc1213StatisticHistoryRxDiscardPkts_Type()
)
zxAnCesRfc1213StatisticHistoryRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryRxDiscardPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryRxErrorPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryRxErrorPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryRxErrorPkts = _ZxAnCesRfc1213StatisticHistoryRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 5),
    _ZxAnCesRfc1213StatisticHistoryRxErrorPkts_Type()
)
zxAnCesRfc1213StatisticHistoryRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryRxErrorPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryRxUnknowProtPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryRxUnknowProtPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryRxUnknowProtPkts = _ZxAnCesRfc1213StatisticHistoryRxUnknowProtPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 6),
    _ZxAnCesRfc1213StatisticHistoryRxUnknowProtPkts_Type()
)
zxAnCesRfc1213StatisticHistoryRxUnknowProtPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryRxUnknowProtPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryTxOctets_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryTxOctets_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryTxOctets = _ZxAnCesRfc1213StatisticHistoryTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 7),
    _ZxAnCesRfc1213StatisticHistoryTxOctets_Type()
)
zxAnCesRfc1213StatisticHistoryTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryTxOctets.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryTxUnicastPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryTxUnicastPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryTxUnicastPkts = _ZxAnCesRfc1213StatisticHistoryTxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 8),
    _ZxAnCesRfc1213StatisticHistoryTxUnicastPkts_Type()
)
zxAnCesRfc1213StatisticHistoryTxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryTxUnicastPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryTxMulBrdPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryTxMulBrdPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryTxMulBrdPkts = _ZxAnCesRfc1213StatisticHistoryTxMulBrdPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 9),
    _ZxAnCesRfc1213StatisticHistoryTxMulBrdPkts_Type()
)
zxAnCesRfc1213StatisticHistoryTxMulBrdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryTxMulBrdPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryTxDiscardPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryTxDiscardPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryTxDiscardPkts = _ZxAnCesRfc1213StatisticHistoryTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 10),
    _ZxAnCesRfc1213StatisticHistoryTxDiscardPkts_Type()
)
zxAnCesRfc1213StatisticHistoryTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryTxDiscardPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryTxErrorPkts_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryTxErrorPkts_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryTxErrorPkts = _ZxAnCesRfc1213StatisticHistoryTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 11),
    _ZxAnCesRfc1213StatisticHistoryTxErrorPkts_Type()
)
zxAnCesRfc1213StatisticHistoryTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryTxErrorPkts.setStatus("current")
_ZxAnCesRfc1213StatisticHistoryOutBoundQueLen_Type = Unsigned32
_ZxAnCesRfc1213StatisticHistoryOutBoundQueLen_Object = MibTableColumn
zxAnCesRfc1213StatisticHistoryOutBoundQueLen = _ZxAnCesRfc1213StatisticHistoryOutBoundQueLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 3, 1, 12),
    _ZxAnCesRfc1213StatisticHistoryOutBoundQueLen_Type()
)
zxAnCesRfc1213StatisticHistoryOutBoundQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1213StatisticHistoryOutBoundQueLen.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryTable_Object = MibTable
zxAnCesRfc1757StatisticHistoryTable = _ZxAnCesRfc1757StatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryTable.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryEntry_Object = MibTableRow
zxAnCesRfc1757StatisticHistoryEntry = _ZxAnCesRfc1757StatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1)
)
zxAnCesRfc1757StatisticHistoryEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryEntry.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryDropCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryDropCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryDropCnt = _ZxAnCesRfc1757StatisticHistoryDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 1),
    _ZxAnCesRfc1757StatisticHistoryDropCnt_Type()
)
zxAnCesRfc1757StatisticHistoryDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryDropCnt.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryMulticastPkts_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryMulticastPkts_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryMulticastPkts = _ZxAnCesRfc1757StatisticHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 2),
    _ZxAnCesRfc1757StatisticHistoryMulticastPkts_Type()
)
zxAnCesRfc1757StatisticHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryMulticastPkts.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryBroadcastPkts_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryBroadcastPkts_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryBroadcastPkts = _ZxAnCesRfc1757StatisticHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 3),
    _ZxAnCesRfc1757StatisticHistoryBroadcastPkts_Type()
)
zxAnCesRfc1757StatisticHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryBroadcastPkts.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryUndersizeFrmCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryUndersizeFrmCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryUndersizeFrmCnt = _ZxAnCesRfc1757StatisticHistoryUndersizeFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 4),
    _ZxAnCesRfc1757StatisticHistoryUndersizeFrmCnt_Type()
)
zxAnCesRfc1757StatisticHistoryUndersizeFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryUndersizeFrmCnt.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryFragmentsCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryFragmentsCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryFragmentsCnt = _ZxAnCesRfc1757StatisticHistoryFragmentsCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 5),
    _ZxAnCesRfc1757StatisticHistoryFragmentsCnt_Type()
)
zxAnCesRfc1757StatisticHistoryFragmentsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryFragmentsCnt.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPkts64_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPkts64_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPkts64 = _ZxAnCesRfc1757StatisticHistoryPkts64_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 6),
    _ZxAnCesRfc1757StatisticHistoryPkts64_Type()
)
zxAnCesRfc1757StatisticHistoryPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPkts64.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPkts65to127_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPkts65to127_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPkts65to127 = _ZxAnCesRfc1757StatisticHistoryPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 7),
    _ZxAnCesRfc1757StatisticHistoryPkts65to127_Type()
)
zxAnCesRfc1757StatisticHistoryPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPkts65to127.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPkts128to255_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPkts128to255_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPkts128to255 = _ZxAnCesRfc1757StatisticHistoryPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 8),
    _ZxAnCesRfc1757StatisticHistoryPkts128to255_Type()
)
zxAnCesRfc1757StatisticHistoryPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPkts128to255.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPkts256to511_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPkts256to511_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPkts256to511 = _ZxAnCesRfc1757StatisticHistoryPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 9),
    _ZxAnCesRfc1757StatisticHistoryPkts256to511_Type()
)
zxAnCesRfc1757StatisticHistoryPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPkts256to511.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPkts512to1023_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPkts512to1023_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPkts512to1023 = _ZxAnCesRfc1757StatisticHistoryPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 10),
    _ZxAnCesRfc1757StatisticHistoryPkts512to1023_Type()
)
zxAnCesRfc1757StatisticHistoryPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPkts512to1023.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPkts1024to1518_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPkts1024to1518_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPkts1024to1518 = _ZxAnCesRfc1757StatisticHistoryPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 11),
    _ZxAnCesRfc1757StatisticHistoryPkts1024to1518_Type()
)
zxAnCesRfc1757StatisticHistoryPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPkts1024to1518.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryPktsOversize_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryPktsOversize_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryPktsOversize = _ZxAnCesRfc1757StatisticHistoryPktsOversize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 12),
    _ZxAnCesRfc1757StatisticHistoryPktsOversize_Type()
)
zxAnCesRfc1757StatisticHistoryPktsOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryPktsOversize.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryJabberFrmCnt_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryJabberFrmCnt_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryJabberFrmCnt = _ZxAnCesRfc1757StatisticHistoryJabberFrmCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 13),
    _ZxAnCesRfc1757StatisticHistoryJabberFrmCnt_Type()
)
zxAnCesRfc1757StatisticHistoryJabberFrmCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryJabberFrmCnt.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryBytesRx_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryBytesRx_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryBytesRx = _ZxAnCesRfc1757StatisticHistoryBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 14),
    _ZxAnCesRfc1757StatisticHistoryBytesRx_Type()
)
zxAnCesRfc1757StatisticHistoryBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryBytesRx.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryFramesRx_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryFramesRx_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryFramesRx = _ZxAnCesRfc1757StatisticHistoryFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 15),
    _ZxAnCesRfc1757StatisticHistoryFramesRx_Type()
)
zxAnCesRfc1757StatisticHistoryFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryFramesRx.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryCollosions_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryCollosions_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryCollosions = _ZxAnCesRfc1757StatisticHistoryCollosions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 16),
    _ZxAnCesRfc1757StatisticHistoryCollosions_Type()
)
zxAnCesRfc1757StatisticHistoryCollosions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryCollosions.setStatus("current")
_ZxAnCesRfc1757StatisticHistoryCrcAlignErr_Type = Unsigned32
_ZxAnCesRfc1757StatisticHistoryCrcAlignErr_Object = MibTableColumn
zxAnCesRfc1757StatisticHistoryCrcAlignErr = _ZxAnCesRfc1757StatisticHistoryCrcAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 4, 1, 17),
    _ZxAnCesRfc1757StatisticHistoryCrcAlignErr_Type()
)
zxAnCesRfc1757StatisticHistoryCrcAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesRfc1757StatisticHistoryCrcAlignErr.setStatus("current")
_ZxAnCesSdhRsB1StatisticHistoryTable_Object = MibTable
zxAnCesSdhRsB1StatisticHistoryTable = _ZxAnCesSdhRsB1StatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1StatisticHistoryTable.setStatus("current")
_ZxAnCesSdhRsB1StatisticHistoryEntry_Object = MibTableRow
zxAnCesSdhRsB1StatisticHistoryEntry = _ZxAnCesSdhRsB1StatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5, 1)
)
zxAnCesSdhRsB1StatisticHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1StatisticHistoryEntry.setStatus("current")
_ZxAnCesSdhRsB1StatisticHistory_Type = Unsigned32
_ZxAnCesSdhRsB1StatisticHistory_Object = MibTableColumn
zxAnCesSdhRsB1StatisticHistory = _ZxAnCesSdhRsB1StatisticHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5, 1, 1),
    _ZxAnCesSdhRsB1StatisticHistory_Type()
)
zxAnCesSdhRsB1StatisticHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1StatisticHistory.setStatus("current")
_ZxAnCesSdhRsB1BBEStatHistory_Type = Unsigned32
_ZxAnCesSdhRsB1BBEStatHistory_Object = MibTableColumn
zxAnCesSdhRsB1BBEStatHistory = _ZxAnCesSdhRsB1BBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5, 1, 2),
    _ZxAnCesSdhRsB1BBEStatHistory_Type()
)
zxAnCesSdhRsB1BBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1BBEStatHistory.setStatus("current")
_ZxAnCesSdhRsB1ESStatHistory_Type = Unsigned32
_ZxAnCesSdhRsB1ESStatHistory_Object = MibTableColumn
zxAnCesSdhRsB1ESStatHistory = _ZxAnCesSdhRsB1ESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5, 1, 3),
    _ZxAnCesSdhRsB1ESStatHistory_Type()
)
zxAnCesSdhRsB1ESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1ESStatHistory.setStatus("current")
_ZxAnCesSdhRsB1SESStatHistory_Type = Unsigned32
_ZxAnCesSdhRsB1SESStatHistory_Object = MibTableColumn
zxAnCesSdhRsB1SESStatHistory = _ZxAnCesSdhRsB1SESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5, 1, 4),
    _ZxAnCesSdhRsB1SESStatHistory_Type()
)
zxAnCesSdhRsB1SESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1SESStatHistory.setStatus("current")
_ZxAnCesSdhRsB1UASStatHistory_Type = Unsigned32
_ZxAnCesSdhRsB1UASStatHistory_Object = MibTableColumn
zxAnCesSdhRsB1UASStatHistory = _ZxAnCesSdhRsB1UASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 5, 1, 5),
    _ZxAnCesSdhRsB1UASStatHistory_Type()
)
zxAnCesSdhRsB1UASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhRsB1UASStatHistory.setStatus("current")
_ZxAnCesSdhMsB2StatisticHistoryTable_Object = MibTable
zxAnCesSdhMsB2StatisticHistoryTable = _ZxAnCesSdhMsB2StatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2StatisticHistoryTable.setStatus("current")
_ZxAnCesSdhMsB2StatisticHistoryEntry_Object = MibTableRow
zxAnCesSdhMsB2StatisticHistoryEntry = _ZxAnCesSdhMsB2StatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6, 1)
)
zxAnCesSdhMsB2StatisticHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2StatisticHistoryEntry.setStatus("current")
_ZxAnCesSdhMsB2StatisticHistory_Type = Unsigned32
_ZxAnCesSdhMsB2StatisticHistory_Object = MibTableColumn
zxAnCesSdhMsB2StatisticHistory = _ZxAnCesSdhMsB2StatisticHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6, 1, 1),
    _ZxAnCesSdhMsB2StatisticHistory_Type()
)
zxAnCesSdhMsB2StatisticHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2StatisticHistory.setStatus("current")
_ZxAnCesSdhMsB2BBEStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2BBEStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2BBEStatHistory = _ZxAnCesSdhMsB2BBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6, 1, 2),
    _ZxAnCesSdhMsB2BBEStatHistory_Type()
)
zxAnCesSdhMsB2BBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2BBEStatHistory.setStatus("current")
_ZxAnCesSdhMsB2ESStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2ESStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2ESStatHistory = _ZxAnCesSdhMsB2ESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6, 1, 3),
    _ZxAnCesSdhMsB2ESStatHistory_Type()
)
zxAnCesSdhMsB2ESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ESStatHistory.setStatus("current")
_ZxAnCesSdhMsB2SESStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2SESStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2SESStatHistory = _ZxAnCesSdhMsB2SESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6, 1, 4),
    _ZxAnCesSdhMsB2SESStatHistory_Type()
)
zxAnCesSdhMsB2SESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2SESStatHistory.setStatus("current")
_ZxAnCesSdhMsB2UASStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2UASStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2UASStatHistory = _ZxAnCesSdhMsB2UASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 6, 1, 5),
    _ZxAnCesSdhMsB2UASStatHistory_Type()
)
zxAnCesSdhMsB2UASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2UASStatHistory.setStatus("current")
_ZxAnCesSdhMsB2ReiStatisticHistoryTable_Object = MibTable
zxAnCesSdhMsB2ReiStatisticHistoryTable = _ZxAnCesSdhMsB2ReiStatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7)
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiStatisticHistoryTable.setStatus("current")
_ZxAnCesSdhMsB2ReiStatisticHistoryEntry_Object = MibTableRow
zxAnCesSdhMsB2ReiStatisticHistoryEntry = _ZxAnCesSdhMsB2ReiStatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7, 1)
)
zxAnCesSdhMsB2ReiStatisticHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiStatisticHistoryEntry.setStatus("current")
_ZxAnCesSdhMsB2ReiStatisticHistory_Type = Unsigned32
_ZxAnCesSdhMsB2ReiStatisticHistory_Object = MibTableColumn
zxAnCesSdhMsB2ReiStatisticHistory = _ZxAnCesSdhMsB2ReiStatisticHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7, 1, 1),
    _ZxAnCesSdhMsB2ReiStatisticHistory_Type()
)
zxAnCesSdhMsB2ReiStatisticHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiStatisticHistory.setStatus("current")
_ZxAnCesSdhMsB2ReiBBEStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2ReiBBEStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2ReiBBEStatHistory = _ZxAnCesSdhMsB2ReiBBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7, 1, 2),
    _ZxAnCesSdhMsB2ReiBBEStatHistory_Type()
)
zxAnCesSdhMsB2ReiBBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiBBEStatHistory.setStatus("current")
_ZxAnCesSdhMsB2ReiESStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2ReiESStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2ReiESStatHistory = _ZxAnCesSdhMsB2ReiESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7, 1, 3),
    _ZxAnCesSdhMsB2ReiESStatHistory_Type()
)
zxAnCesSdhMsB2ReiESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiESStatHistory.setStatus("current")
_ZxAnCesSdhMsB2ReiSESStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2ReiSESStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2ReiSESStatHistory = _ZxAnCesSdhMsB2ReiSESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7, 1, 4),
    _ZxAnCesSdhMsB2ReiSESStatHistory_Type()
)
zxAnCesSdhMsB2ReiSESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiSESStatHistory.setStatus("current")
_ZxAnCesSdhMsB2ReiUASStatHistory_Type = Unsigned32
_ZxAnCesSdhMsB2ReiUASStatHistory_Object = MibTableColumn
zxAnCesSdhMsB2ReiUASStatHistory = _ZxAnCesSdhMsB2ReiUASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 7, 1, 5),
    _ZxAnCesSdhMsB2ReiUASStatHistory_Type()
)
zxAnCesSdhMsB2ReiUASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhMsB2ReiUASStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5StatisticHistoryTable_Object = MibTable
zxAnCesSdhVc12V5StatisticHistoryTable = _ZxAnCesSdhVc12V5StatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5StatisticHistoryTable.setStatus("current")
_ZxAnCesSdhVc12V5StatisticHistoryEntry_Object = MibTableRow
zxAnCesSdhVc12V5StatisticHistoryEntry = _ZxAnCesSdhVc12V5StatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8, 1)
)
zxAnCesSdhVc12V5StatisticHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5StatisticHistoryEntry.setStatus("current")
_ZxAnCesSdhVc12V5StatisticHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5StatisticHistory_Object = MibTableColumn
zxAnCesSdhVc12V5StatisticHistory = _ZxAnCesSdhVc12V5StatisticHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8, 1, 1),
    _ZxAnCesSdhVc12V5StatisticHistory_Type()
)
zxAnCesSdhVc12V5StatisticHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5StatisticHistory.setStatus("current")
_ZxAnCesSdhVc12V5BBEStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5BBEStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5BBEStatHistory = _ZxAnCesSdhVc12V5BBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8, 1, 2),
    _ZxAnCesSdhVc12V5BBEStatHistory_Type()
)
zxAnCesSdhVc12V5BBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5BBEStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5ESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5ESStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5ESStatHistory = _ZxAnCesSdhVc12V5ESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8, 1, 3),
    _ZxAnCesSdhVc12V5ESStatHistory_Type()
)
zxAnCesSdhVc12V5ESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ESStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5SESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5SESStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5SESStatHistory = _ZxAnCesSdhVc12V5SESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8, 1, 4),
    _ZxAnCesSdhVc12V5SESStatHistory_Type()
)
zxAnCesSdhVc12V5SESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5SESStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5UASStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5UASStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5UASStatHistory = _ZxAnCesSdhVc12V5UASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 8, 1, 5),
    _ZxAnCesSdhVc12V5UASStatHistory_Type()
)
zxAnCesSdhVc12V5UASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5UASStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5ReiStatHistoryTable_Object = MibTable
zxAnCesSdhVc12V5ReiStatHistoryTable = _ZxAnCesSdhVc12V5ReiStatHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiStatHistoryTable.setStatus("current")
_ZxAnCesSdhVc12V5ReiStatHistoryEntry_Object = MibTableRow
zxAnCesSdhVc12V5ReiStatHistoryEntry = _ZxAnCesSdhVc12V5ReiStatHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9, 1)
)
zxAnCesSdhVc12V5ReiStatHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiStatHistoryEntry.setStatus("current")
_ZxAnCesSdhVc12V5ReiStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5ReiStatHistory = _ZxAnCesSdhVc12V5ReiStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9, 1, 1),
    _ZxAnCesSdhVc12V5ReiStatHistory_Type()
)
zxAnCesSdhVc12V5ReiStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5ReiBBEStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiBBEStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5ReiBBEStatHistory = _ZxAnCesSdhVc12V5ReiBBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9, 1, 2),
    _ZxAnCesSdhVc12V5ReiBBEStatHistory_Type()
)
zxAnCesSdhVc12V5ReiBBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiBBEStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5ReiESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiESStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5ReiESStatHistory = _ZxAnCesSdhVc12V5ReiESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9, 1, 3),
    _ZxAnCesSdhVc12V5ReiESStatHistory_Type()
)
zxAnCesSdhVc12V5ReiESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiESStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5ReiSESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiSESStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5ReiSESStatHistory = _ZxAnCesSdhVc12V5ReiSESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9, 1, 4),
    _ZxAnCesSdhVc12V5ReiSESStatHistory_Type()
)
zxAnCesSdhVc12V5ReiSESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiSESStatHistory.setStatus("current")
_ZxAnCesSdhVc12V5ReiUASStatHistory_Type = Unsigned32
_ZxAnCesSdhVc12V5ReiUASStatHistory_Object = MibTableColumn
zxAnCesSdhVc12V5ReiUASStatHistory = _ZxAnCesSdhVc12V5ReiUASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 9, 1, 5),
    _ZxAnCesSdhVc12V5ReiUASStatHistory_Type()
)
zxAnCesSdhVc12V5ReiUASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc12V5ReiUASStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3StatisticHistoryTable_Object = MibTable
zxAnCesSdhVc4B3StatisticHistoryTable = _ZxAnCesSdhVc4B3StatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3StatisticHistoryTable.setStatus("current")
_ZxAnCesSdhVc4B3StatisticHistoryEntry_Object = MibTableRow
zxAnCesSdhVc4B3StatisticHistoryEntry = _ZxAnCesSdhVc4B3StatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10, 1)
)
zxAnCesSdhVc4B3StatisticHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3StatisticHistoryEntry.setStatus("current")
_ZxAnCesSdhVc4B3StatisticHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3StatisticHistory_Object = MibTableColumn
zxAnCesSdhVc4B3StatisticHistory = _ZxAnCesSdhVc4B3StatisticHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10, 1, 1),
    _ZxAnCesSdhVc4B3StatisticHistory_Type()
)
zxAnCesSdhVc4B3StatisticHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3StatisticHistory.setStatus("current")
_ZxAnCesSdhVc4B3BBEStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3BBEStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3BBEStatHistory = _ZxAnCesSdhVc4B3BBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10, 1, 2),
    _ZxAnCesSdhVc4B3BBEStatHistory_Type()
)
zxAnCesSdhVc4B3BBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3BBEStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3ESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3ESStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3ESStatHistory = _ZxAnCesSdhVc4B3ESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10, 1, 3),
    _ZxAnCesSdhVc4B3ESStatHistory_Type()
)
zxAnCesSdhVc4B3ESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ESStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3SESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3SESStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3SESStatHistory = _ZxAnCesSdhVc4B3SESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10, 1, 4),
    _ZxAnCesSdhVc4B3SESStatHistory_Type()
)
zxAnCesSdhVc4B3SESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3SESStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3UASStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3UASStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3UASStatHistory = _ZxAnCesSdhVc4B3UASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 10, 1, 5),
    _ZxAnCesSdhVc4B3UASStatHistory_Type()
)
zxAnCesSdhVc4B3UASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3UASStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3ReiStatisticHistoryTable_Object = MibTable
zxAnCesSdhVc4B3ReiStatisticHistoryTable = _ZxAnCesSdhVc4B3ReiStatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11)
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiStatisticHistoryTable.setStatus("current")
_ZxAnCesSdhVc4B3ReiStatisticHistoryEntry_Object = MibTableRow
zxAnCesSdhVc4B3ReiStatisticHistoryEntry = _ZxAnCesSdhVc4B3ReiStatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11, 1)
)
zxAnCesSdhVc4B3ReiStatisticHistoryEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiStatisticHistoryEntry.setStatus("current")
_ZxAnCesSdhVc4B3ReiStatisticHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiStatisticHistory_Object = MibTableColumn
zxAnCesSdhVc4B3ReiStatisticHistory = _ZxAnCesSdhVc4B3ReiStatisticHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11, 1, 1),
    _ZxAnCesSdhVc4B3ReiStatisticHistory_Type()
)
zxAnCesSdhVc4B3ReiStatisticHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiStatisticHistory.setStatus("current")
_ZxAnCesSdhVc4B3ReiBBEStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiBBEStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3ReiBBEStatHistory = _ZxAnCesSdhVc4B3ReiBBEStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11, 1, 2),
    _ZxAnCesSdhVc4B3ReiBBEStatHistory_Type()
)
zxAnCesSdhVc4B3ReiBBEStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiBBEStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3ReiESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiESStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3ReiESStatHistory = _ZxAnCesSdhVc4B3ReiESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11, 1, 3),
    _ZxAnCesSdhVc4B3ReiESStatHistory_Type()
)
zxAnCesSdhVc4B3ReiESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiESStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3ReiSESStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiSESStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3ReiSESStatHistory = _ZxAnCesSdhVc4B3ReiSESStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11, 1, 4),
    _ZxAnCesSdhVc4B3ReiSESStatHistory_Type()
)
zxAnCesSdhVc4B3ReiSESStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiSESStatHistory.setStatus("current")
_ZxAnCesSdhVc4B3ReiUASStatHistory_Type = Unsigned32
_ZxAnCesSdhVc4B3ReiUASStatHistory_Object = MibTableColumn
zxAnCesSdhVc4B3ReiUASStatHistory = _ZxAnCesSdhVc4B3ReiUASStatHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 6, 2, 11, 1, 5),
    _ZxAnCesSdhVc4B3ReiUASStatHistory_Type()
)
zxAnCesSdhVc4B3ReiUASStatHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCesSdhVc4B3ReiUASStatHistory.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXCESPERFORMANCE-MIB",
    **{"zxAnCesPm": zxAnCesPm,
       "zxAnCesPmInfor": zxAnCesPmInfor,
       "zxAnCesWanPortStatisticTable": zxAnCesWanPortStatisticTable,
       "zxAnCesWanPortStatisticEntry": zxAnCesWanPortStatisticEntry,
       "zxAnCesWanPortStatisticEarlyPkts": zxAnCesWanPortStatisticEarlyPkts,
       "zxAnCesWanPortStatisticLatePkts": zxAnCesWanPortStatisticLatePkts,
       "zxAnCesWanPortStatisticUnderrunPkts": zxAnCesWanPortStatisticUnderrunPkts,
       "zxAnCesWanPortStatisticLostPkts": zxAnCesWanPortStatisticLostPkts,
       "zxAnCesWanPortStatisticCurQueLen": zxAnCesWanPortStatisticCurQueLen,
       "zxAnCesWanPortStatisticAvgQueLen": zxAnCesWanPortStatisticAvgQueLen,
       "zxAnCesWanPortStatisticMaxQueLen": zxAnCesWanPortStatisticMaxQueLen,
       "zxAnCesWanPortStatisticMinQueLen": zxAnCesWanPortStatisticMinQueLen,
       "zxAnCesWanPortStatisticPktRxCnt": zxAnCesWanPortStatisticPktRxCnt,
       "zxAnCesWanPortStatisticPktTxCnt": zxAnCesWanPortStatisticPktTxCnt,
       "zxAnCesWanPortStatisticByteTxCnt": zxAnCesWanPortStatisticByteTxCnt,
       "zxAnCesWanPortStatisticLBitCnt": zxAnCesWanPortStatisticLBitCnt,
       "zxAnCesWanPortStatisticLBitSetTime": zxAnCesWanPortStatisticLBitSetTime,
       "zxAnCesWanPortStatisticRBitCnt": zxAnCesWanPortStatisticRBitCnt,
       "zxAnCesWanPortStatisticRBitSetTime": zxAnCesWanPortStatisticRBitSetTime,
       "zxAnCesProtocolStatisticTable": zxAnCesProtocolStatisticTable,
       "zxAnCesProtocolStatisticEntry": zxAnCesProtocolStatisticEntry,
       "zxAnCesProtocolStatisticProtMatchCnt": zxAnCesProtocolStatisticProtMatchCnt,
       "zxAnCesProtocolStatisticProtNoMatchCnt": zxAnCesProtocolStatisticProtNoMatchCnt,
       "zxAnCesProtocolStatisticClaNoMatchCnt": zxAnCesProtocolStatisticClaNoMatchCnt,
       "zxAnCesProtocolStatisticVerifyFailCnt": zxAnCesProtocolStatisticVerifyFailCnt,
       "zxAnCesProtocolStatisticIP4CheckFailCnt": zxAnCesProtocolStatisticIP4CheckFailCnt,
       "zxAnCesRfc1213StatisticTable": zxAnCesRfc1213StatisticTable,
       "zxAnCesRfc1213StatisticEntry": zxAnCesRfc1213StatisticEntry,
       "zxAnCesRfc1213StatisticRxOctets": zxAnCesRfc1213StatisticRxOctets,
       "zxAnCesRfc1213StatisticRxUnicastPkts": zxAnCesRfc1213StatisticRxUnicastPkts,
       "zxAnCesRfc1213StatisticRxMulBrdPkts": zxAnCesRfc1213StatisticRxMulBrdPkts,
       "zxAnCesRfc1213StatisticRxDiscardPkts": zxAnCesRfc1213StatisticRxDiscardPkts,
       "zxAnCesRfc1213StatisticRxErrorPkts": zxAnCesRfc1213StatisticRxErrorPkts,
       "zxAnCesRfc1213StatisticRxUnknowProtPkts": zxAnCesRfc1213StatisticRxUnknowProtPkts,
       "zxAnCesRfc1213StatisticTxOctets": zxAnCesRfc1213StatisticTxOctets,
       "zxAnCesRfc1213StatisticTxUnicastPkts": zxAnCesRfc1213StatisticTxUnicastPkts,
       "zxAnCesRfc1213StatisticTxMulBrdPkts": zxAnCesRfc1213StatisticTxMulBrdPkts,
       "zxAnCesRfc1213StatisticTxDiscardPkts": zxAnCesRfc1213StatisticTxDiscardPkts,
       "zxAnCesRfc1213StatisticTxErrorPkts": zxAnCesRfc1213StatisticTxErrorPkts,
       "zxAnCesRfc1213StatisticOutBoundQueLen": zxAnCesRfc1213StatisticOutBoundQueLen,
       "zxAnCesRfc1757StatisticTable": zxAnCesRfc1757StatisticTable,
       "zxAnCesRfc1757StatisticEntry": zxAnCesRfc1757StatisticEntry,
       "zxAnCesRfc1757StatisticDropCnt": zxAnCesRfc1757StatisticDropCnt,
       "zxAnCesRfc1757StatisticMulticastPkts": zxAnCesRfc1757StatisticMulticastPkts,
       "zxAnCesRfc1757StatisticBroadcastPkts": zxAnCesRfc1757StatisticBroadcastPkts,
       "zxAnCesRfc1757StatisticUndersizeFrmCnt": zxAnCesRfc1757StatisticUndersizeFrmCnt,
       "zxAnCesRfc1757StatisticFragmentsCnt": zxAnCesRfc1757StatisticFragmentsCnt,
       "zxAnCesRfc1757StatisticPkts64": zxAnCesRfc1757StatisticPkts64,
       "zxAnCesRfc1757StatisticPkts65to127": zxAnCesRfc1757StatisticPkts65to127,
       "zxAnCesRfc1757StatisticPkts128to255": zxAnCesRfc1757StatisticPkts128to255,
       "zxAnCesRfc1757StatisticPkts256to511": zxAnCesRfc1757StatisticPkts256to511,
       "zxAnCesRfc1757StatisticPkts512to1023": zxAnCesRfc1757StatisticPkts512to1023,
       "zxAnCesRfc1757StatisticPkts1024to1518": zxAnCesRfc1757StatisticPkts1024to1518,
       "zxAnCesRfc1757StatisticPktsOversize": zxAnCesRfc1757StatisticPktsOversize,
       "zxAnCesRfc1757StatisticJabberFrmCnt": zxAnCesRfc1757StatisticJabberFrmCnt,
       "zxAnCesRfc1757StatisticBytesRx": zxAnCesRfc1757StatisticBytesRx,
       "zxAnCesRfc1757StatisticFramesRx": zxAnCesRfc1757StatisticFramesRx,
       "zxAnCesRfc1757StatisticCollosions": zxAnCesRfc1757StatisticCollosions,
       "zxAnCesRfc1757StatisticCrcAlignErr": zxAnCesRfc1757StatisticCrcAlignErr,
       "zxAnCesSdhRsB1StatisticTable": zxAnCesSdhRsB1StatisticTable,
       "zxAnCesSdhRsB1StatisticEntry": zxAnCesSdhRsB1StatisticEntry,
       "zxAnCesSdhRsB1Statistic": zxAnCesSdhRsB1Statistic,
       "zxAnCesSdhRsB1BBEStat": zxAnCesSdhRsB1BBEStat,
       "zxAnCesSdhRsB1ESStat": zxAnCesSdhRsB1ESStat,
       "zxAnCesSdhRsB1SESStat": zxAnCesSdhRsB1SESStat,
       "zxAnCesSdhRsB1UASStat": zxAnCesSdhRsB1UASStat,
       "zxAnCesSdhMsB2StatisticTable": zxAnCesSdhMsB2StatisticTable,
       "zxAnCesSdhMsB2StatisticEntry": zxAnCesSdhMsB2StatisticEntry,
       "zxAnCesSdhMsB2Statistic": zxAnCesSdhMsB2Statistic,
       "zxAnCesSdhMsB2BBEStat": zxAnCesSdhMsB2BBEStat,
       "zxAnCesSdhMsB2ESStat": zxAnCesSdhMsB2ESStat,
       "zxAnCesSdhMsB2SESStat": zxAnCesSdhMsB2SESStat,
       "zxAnCesSdhMsB2UASStat": zxAnCesSdhMsB2UASStat,
       "zxAnCesSdhMsB2ReiStatisticTable": zxAnCesSdhMsB2ReiStatisticTable,
       "zxAnCesSdhMsB2ReiStatisticEntry": zxAnCesSdhMsB2ReiStatisticEntry,
       "zxAnCesSdhMsB2ReiStatistic": zxAnCesSdhMsB2ReiStatistic,
       "zxAnCesSdhMsB2ReiBBEStat": zxAnCesSdhMsB2ReiBBEStat,
       "zxAnCesSdhMsB2ReiESStat": zxAnCesSdhMsB2ReiESStat,
       "zxAnCesSdhMsB2ReiSESStat": zxAnCesSdhMsB2ReiSESStat,
       "zxAnCesSdhMsB2ReiUASStat": zxAnCesSdhMsB2ReiUASStat,
       "zxAnCesSdhVc12V5StatisticTable": zxAnCesSdhVc12V5StatisticTable,
       "zxAnCesSdhVc12V5StatisticEntry": zxAnCesSdhVc12V5StatisticEntry,
       "zxAnCesSdhVc12V5Statistic": zxAnCesSdhVc12V5Statistic,
       "zxAnCesSdhVc12V5BBEStat": zxAnCesSdhVc12V5BBEStat,
       "zxAnCesSdhVc12V5ESStat": zxAnCesSdhVc12V5ESStat,
       "zxAnCesSdhVc12V5SESStat": zxAnCesSdhVc12V5SESStat,
       "zxAnCesSdhVc12V5UASStat": zxAnCesSdhVc12V5UASStat,
       "zxAnCesSdhVc12V5ReiStatisticTable": zxAnCesSdhVc12V5ReiStatisticTable,
       "zxAnCesSdhVc12V5ReiStatisticEntry": zxAnCesSdhVc12V5ReiStatisticEntry,
       "zxAnCesSdhVc12V5ReiStatistic": zxAnCesSdhVc12V5ReiStatistic,
       "zxAnCesSdhVc12V5ReiBBEStat": zxAnCesSdhVc12V5ReiBBEStat,
       "zxAnCesSdhVc12V5ReiESStat": zxAnCesSdhVc12V5ReiESStat,
       "zxAnCesSdhVc12V5ReiSESStat": zxAnCesSdhVc12V5ReiSESStat,
       "zxAnCesSdhVc12V5ReiUASStat": zxAnCesSdhVc12V5ReiUASStat,
       "zxAnCesSdhVc4B3StatisticTable": zxAnCesSdhVc4B3StatisticTable,
       "zxAnCesSdhVc4B3StatisticEntry": zxAnCesSdhVc4B3StatisticEntry,
       "zxAnCesSdhVc4B3Statistic": zxAnCesSdhVc4B3Statistic,
       "zxAnCesSdhVc4B3BBEStat": zxAnCesSdhVc4B3BBEStat,
       "zxAnCesSdhVc4B3ESStat": zxAnCesSdhVc4B3ESStat,
       "zxAnCesSdhVc4B3SESStat": zxAnCesSdhVc4B3SESStat,
       "zxAnCesSdhVc4B3UASStat": zxAnCesSdhVc4B3UASStat,
       "zxAnCesSdhVc4B3ReiStatisticTable": zxAnCesSdhVc4B3ReiStatisticTable,
       "zxAnCesSdhVc4B3ReiStatisticEntry": zxAnCesSdhVc4B3ReiStatisticEntry,
       "zxAnCesSdhVc4B3ReiStatistic": zxAnCesSdhVc4B3ReiStatistic,
       "zxAnCesSdhVc4B3ReiBBEStat": zxAnCesSdhVc4B3ReiBBEStat,
       "zxAnCesSdhVc4B3ReiESStat": zxAnCesSdhVc4B3ReiESStat,
       "zxAnCesSdhVc4B3ReiSESStat": zxAnCesSdhVc4B3ReiSESStat,
       "zxAnCesSdhVc4B3ReiUASStat": zxAnCesSdhVc4B3ReiUASStat,
       "zxAnCesE1CurrentTable": zxAnCesE1CurrentTable,
       "zxAnCesE1CurrentEntry": zxAnCesE1CurrentEntry,
       "zxAnCesE1CurrentIndex": zxAnCesE1CurrentIndex,
       "zxAnCesE1Efs": zxAnCesE1Efs,
       "zxAnCesPmHistory": zxAnCesPmHistory,
       "zxAnCesWanPortStatisticHistoryTable": zxAnCesWanPortStatisticHistoryTable,
       "zxAnCesWanPortStatisticHistoryEntry": zxAnCesWanPortStatisticHistoryEntry,
       "zxAnCesWanPortStatisticHistoryEarlyPkts": zxAnCesWanPortStatisticHistoryEarlyPkts,
       "zxAnCesWanPortStatisticHistoryLatePkts": zxAnCesWanPortStatisticHistoryLatePkts,
       "zxAnCesWanPortStatisticHistoryUnderrunPkts": zxAnCesWanPortStatisticHistoryUnderrunPkts,
       "zxAnCesWanPortStatisticHistoryLostPkts": zxAnCesWanPortStatisticHistoryLostPkts,
       "zxAnCesWanPortStatisticHistoryCurQueLen": zxAnCesWanPortStatisticHistoryCurQueLen,
       "zxAnCesWanPortStatisticHistoryAvgQueLen": zxAnCesWanPortStatisticHistoryAvgQueLen,
       "zxAnCesWanPortStatisticHistoryMaxQueLen": zxAnCesWanPortStatisticHistoryMaxQueLen,
       "zxAnCesWanPortStatisticHistoryMinQueLen": zxAnCesWanPortStatisticHistoryMinQueLen,
       "zxAnCesWanPortStatisticHistoryPktRxCnt": zxAnCesWanPortStatisticHistoryPktRxCnt,
       "zxAnCesWanPortStatisticHistoryPktTxCnt": zxAnCesWanPortStatisticHistoryPktTxCnt,
       "zxAnCesWanPortStatisticHistoryByteTxCnt": zxAnCesWanPortStatisticHistoryByteTxCnt,
       "zxAnCesWanPortStatisticHistoryLBitCnt": zxAnCesWanPortStatisticHistoryLBitCnt,
       "zxAnCesWanPortStatisticHistoryLBitSetTime": zxAnCesWanPortStatisticHistoryLBitSetTime,
       "zxAnCesWanPortStatisticHistoryRBitCnt": zxAnCesWanPortStatisticHistoryRBitCnt,
       "zxAnCesWanPortStatisticHistoryRBitSetTime": zxAnCesWanPortStatisticHistoryRBitSetTime,
       "zxAnCesProtocolStatisticHistoryTable": zxAnCesProtocolStatisticHistoryTable,
       "zxAnCesProtocolStatisticHistoryEntry": zxAnCesProtocolStatisticHistoryEntry,
       "zxAnCesProtocolStatisticHistoryProtMatchCnt": zxAnCesProtocolStatisticHistoryProtMatchCnt,
       "zxAnCesProtocolStatisticHistoryProtNoMatchCnt": zxAnCesProtocolStatisticHistoryProtNoMatchCnt,
       "zxAnCesProtocolStatisticHistoryClaNoMatchCnt": zxAnCesProtocolStatisticHistoryClaNoMatchCnt,
       "zxAnCesProtocolStatisticHistoryVerifyFailCnt": zxAnCesProtocolStatisticHistoryVerifyFailCnt,
       "zxAnCesProtocolStatisticHistoryIP4CheckFailCnt": zxAnCesProtocolStatisticHistoryIP4CheckFailCnt,
       "zxAnCesRfc1213StatisticHistoryTable": zxAnCesRfc1213StatisticHistoryTable,
       "zxAnCesRfc1213StatisticHistoryEntry": zxAnCesRfc1213StatisticHistoryEntry,
       "zxAnCesRfc1213StatisticHistoryRxOctets": zxAnCesRfc1213StatisticHistoryRxOctets,
       "zxAnCesRfc1213StatisticHistoryRxUnicastPkts": zxAnCesRfc1213StatisticHistoryRxUnicastPkts,
       "zxAnCesRfc1213StatisticHistoryRxMulBrdPkts": zxAnCesRfc1213StatisticHistoryRxMulBrdPkts,
       "zxAnCesRfc1213StatisticHistoryRxDiscardPkts": zxAnCesRfc1213StatisticHistoryRxDiscardPkts,
       "zxAnCesRfc1213StatisticHistoryRxErrorPkts": zxAnCesRfc1213StatisticHistoryRxErrorPkts,
       "zxAnCesRfc1213StatisticHistoryRxUnknowProtPkts": zxAnCesRfc1213StatisticHistoryRxUnknowProtPkts,
       "zxAnCesRfc1213StatisticHistoryTxOctets": zxAnCesRfc1213StatisticHistoryTxOctets,
       "zxAnCesRfc1213StatisticHistoryTxUnicastPkts": zxAnCesRfc1213StatisticHistoryTxUnicastPkts,
       "zxAnCesRfc1213StatisticHistoryTxMulBrdPkts": zxAnCesRfc1213StatisticHistoryTxMulBrdPkts,
       "zxAnCesRfc1213StatisticHistoryTxDiscardPkts": zxAnCesRfc1213StatisticHistoryTxDiscardPkts,
       "zxAnCesRfc1213StatisticHistoryTxErrorPkts": zxAnCesRfc1213StatisticHistoryTxErrorPkts,
       "zxAnCesRfc1213StatisticHistoryOutBoundQueLen": zxAnCesRfc1213StatisticHistoryOutBoundQueLen,
       "zxAnCesRfc1757StatisticHistoryTable": zxAnCesRfc1757StatisticHistoryTable,
       "zxAnCesRfc1757StatisticHistoryEntry": zxAnCesRfc1757StatisticHistoryEntry,
       "zxAnCesRfc1757StatisticHistoryDropCnt": zxAnCesRfc1757StatisticHistoryDropCnt,
       "zxAnCesRfc1757StatisticHistoryMulticastPkts": zxAnCesRfc1757StatisticHistoryMulticastPkts,
       "zxAnCesRfc1757StatisticHistoryBroadcastPkts": zxAnCesRfc1757StatisticHistoryBroadcastPkts,
       "zxAnCesRfc1757StatisticHistoryUndersizeFrmCnt": zxAnCesRfc1757StatisticHistoryUndersizeFrmCnt,
       "zxAnCesRfc1757StatisticHistoryFragmentsCnt": zxAnCesRfc1757StatisticHistoryFragmentsCnt,
       "zxAnCesRfc1757StatisticHistoryPkts64": zxAnCesRfc1757StatisticHistoryPkts64,
       "zxAnCesRfc1757StatisticHistoryPkts65to127": zxAnCesRfc1757StatisticHistoryPkts65to127,
       "zxAnCesRfc1757StatisticHistoryPkts128to255": zxAnCesRfc1757StatisticHistoryPkts128to255,
       "zxAnCesRfc1757StatisticHistoryPkts256to511": zxAnCesRfc1757StatisticHistoryPkts256to511,
       "zxAnCesRfc1757StatisticHistoryPkts512to1023": zxAnCesRfc1757StatisticHistoryPkts512to1023,
       "zxAnCesRfc1757StatisticHistoryPkts1024to1518": zxAnCesRfc1757StatisticHistoryPkts1024to1518,
       "zxAnCesRfc1757StatisticHistoryPktsOversize": zxAnCesRfc1757StatisticHistoryPktsOversize,
       "zxAnCesRfc1757StatisticHistoryJabberFrmCnt": zxAnCesRfc1757StatisticHistoryJabberFrmCnt,
       "zxAnCesRfc1757StatisticHistoryBytesRx": zxAnCesRfc1757StatisticHistoryBytesRx,
       "zxAnCesRfc1757StatisticHistoryFramesRx": zxAnCesRfc1757StatisticHistoryFramesRx,
       "zxAnCesRfc1757StatisticHistoryCollosions": zxAnCesRfc1757StatisticHistoryCollosions,
       "zxAnCesRfc1757StatisticHistoryCrcAlignErr": zxAnCesRfc1757StatisticHistoryCrcAlignErr,
       "zxAnCesSdhRsB1StatisticHistoryTable": zxAnCesSdhRsB1StatisticHistoryTable,
       "zxAnCesSdhRsB1StatisticHistoryEntry": zxAnCesSdhRsB1StatisticHistoryEntry,
       "zxAnCesSdhRsB1StatisticHistory": zxAnCesSdhRsB1StatisticHistory,
       "zxAnCesSdhRsB1BBEStatHistory": zxAnCesSdhRsB1BBEStatHistory,
       "zxAnCesSdhRsB1ESStatHistory": zxAnCesSdhRsB1ESStatHistory,
       "zxAnCesSdhRsB1SESStatHistory": zxAnCesSdhRsB1SESStatHistory,
       "zxAnCesSdhRsB1UASStatHistory": zxAnCesSdhRsB1UASStatHistory,
       "zxAnCesSdhMsB2StatisticHistoryTable": zxAnCesSdhMsB2StatisticHistoryTable,
       "zxAnCesSdhMsB2StatisticHistoryEntry": zxAnCesSdhMsB2StatisticHistoryEntry,
       "zxAnCesSdhMsB2StatisticHistory": zxAnCesSdhMsB2StatisticHistory,
       "zxAnCesSdhMsB2BBEStatHistory": zxAnCesSdhMsB2BBEStatHistory,
       "zxAnCesSdhMsB2ESStatHistory": zxAnCesSdhMsB2ESStatHistory,
       "zxAnCesSdhMsB2SESStatHistory": zxAnCesSdhMsB2SESStatHistory,
       "zxAnCesSdhMsB2UASStatHistory": zxAnCesSdhMsB2UASStatHistory,
       "zxAnCesSdhMsB2ReiStatisticHistoryTable": zxAnCesSdhMsB2ReiStatisticHistoryTable,
       "zxAnCesSdhMsB2ReiStatisticHistoryEntry": zxAnCesSdhMsB2ReiStatisticHistoryEntry,
       "zxAnCesSdhMsB2ReiStatisticHistory": zxAnCesSdhMsB2ReiStatisticHistory,
       "zxAnCesSdhMsB2ReiBBEStatHistory": zxAnCesSdhMsB2ReiBBEStatHistory,
       "zxAnCesSdhMsB2ReiESStatHistory": zxAnCesSdhMsB2ReiESStatHistory,
       "zxAnCesSdhMsB2ReiSESStatHistory": zxAnCesSdhMsB2ReiSESStatHistory,
       "zxAnCesSdhMsB2ReiUASStatHistory": zxAnCesSdhMsB2ReiUASStatHistory,
       "zxAnCesSdhVc12V5StatisticHistoryTable": zxAnCesSdhVc12V5StatisticHistoryTable,
       "zxAnCesSdhVc12V5StatisticHistoryEntry": zxAnCesSdhVc12V5StatisticHistoryEntry,
       "zxAnCesSdhVc12V5StatisticHistory": zxAnCesSdhVc12V5StatisticHistory,
       "zxAnCesSdhVc12V5BBEStatHistory": zxAnCesSdhVc12V5BBEStatHistory,
       "zxAnCesSdhVc12V5ESStatHistory": zxAnCesSdhVc12V5ESStatHistory,
       "zxAnCesSdhVc12V5SESStatHistory": zxAnCesSdhVc12V5SESStatHistory,
       "zxAnCesSdhVc12V5UASStatHistory": zxAnCesSdhVc12V5UASStatHistory,
       "zxAnCesSdhVc12V5ReiStatHistoryTable": zxAnCesSdhVc12V5ReiStatHistoryTable,
       "zxAnCesSdhVc12V5ReiStatHistoryEntry": zxAnCesSdhVc12V5ReiStatHistoryEntry,
       "zxAnCesSdhVc12V5ReiStatHistory": zxAnCesSdhVc12V5ReiStatHistory,
       "zxAnCesSdhVc12V5ReiBBEStatHistory": zxAnCesSdhVc12V5ReiBBEStatHistory,
       "zxAnCesSdhVc12V5ReiESStatHistory": zxAnCesSdhVc12V5ReiESStatHistory,
       "zxAnCesSdhVc12V5ReiSESStatHistory": zxAnCesSdhVc12V5ReiSESStatHistory,
       "zxAnCesSdhVc12V5ReiUASStatHistory": zxAnCesSdhVc12V5ReiUASStatHistory,
       "zxAnCesSdhVc4B3StatisticHistoryTable": zxAnCesSdhVc4B3StatisticHistoryTable,
       "zxAnCesSdhVc4B3StatisticHistoryEntry": zxAnCesSdhVc4B3StatisticHistoryEntry,
       "zxAnCesSdhVc4B3StatisticHistory": zxAnCesSdhVc4B3StatisticHistory,
       "zxAnCesSdhVc4B3BBEStatHistory": zxAnCesSdhVc4B3BBEStatHistory,
       "zxAnCesSdhVc4B3ESStatHistory": zxAnCesSdhVc4B3ESStatHistory,
       "zxAnCesSdhVc4B3SESStatHistory": zxAnCesSdhVc4B3SESStatHistory,
       "zxAnCesSdhVc4B3UASStatHistory": zxAnCesSdhVc4B3UASStatHistory,
       "zxAnCesSdhVc4B3ReiStatisticHistoryTable": zxAnCesSdhVc4B3ReiStatisticHistoryTable,
       "zxAnCesSdhVc4B3ReiStatisticHistoryEntry": zxAnCesSdhVc4B3ReiStatisticHistoryEntry,
       "zxAnCesSdhVc4B3ReiStatisticHistory": zxAnCesSdhVc4B3ReiStatisticHistory,
       "zxAnCesSdhVc4B3ReiBBEStatHistory": zxAnCesSdhVc4B3ReiBBEStatHistory,
       "zxAnCesSdhVc4B3ReiESStatHistory": zxAnCesSdhVc4B3ReiESStatHistory,
       "zxAnCesSdhVc4B3ReiSESStatHistory": zxAnCesSdhVc4B3ReiSESStatHistory,
       "zxAnCesSdhVc4B3ReiUASStatHistory": zxAnCesSdhVc4B3ReiUASStatHistory}
)
