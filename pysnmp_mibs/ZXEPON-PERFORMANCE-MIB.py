# SNMP MIB module (ZXEPON-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXEPON-PERFORMANCE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:31 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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

(zxAnEponMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnEponMib")

(zxAnEponOnuLlid,) = mibBuilder.importSymbols(
    "ZXANEPON-ONUMGMT-MIB",
    "zxAnEponOnuLlid")


# MODULE-IDENTITY

zxAnEponPm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnEponPmInfor_ObjectIdentity = ObjectIdentity
zxAnEponPmInfor = _ZxAnEponPmInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1)
)
_ZxAnEponOltVirtualIfBERStatisticTable_Object = MibTable
zxAnEponOltVirtualIfBERStatisticTable = _ZxAnEponOltVirtualIfBERStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticTable.setStatus("current")
_ZxAnEponOltVirtualIfBERStatisticEntry_Object = MibTableRow
zxAnEponOltVirtualIfBERStatisticEntry = _ZxAnEponOltVirtualIfBERStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 1, 1)
)
zxAnEponOltVirtualIfBERStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticEntry.setStatus("current")


class _ZxAnEponOltVirtualIfBERStatisticOnuBER_Type(OctetString):
    """Custom type zxAnEponOltVirtualIfBERStatisticOnuBER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltVirtualIfBERStatisticOnuBER_Type.__name__ = "OctetString"
_ZxAnEponOltVirtualIfBERStatisticOnuBER_Object = MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuBER = _ZxAnEponOltVirtualIfBERStatisticOnuBER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 1, 1, 1),
    _ZxAnEponOltVirtualIfBERStatisticOnuBER_Type()
)
zxAnEponOltVirtualIfBERStatisticOnuBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticOnuBER.setStatus("current")


class _ZxAnEponOltVirtualIfBERStatisticOnuFER_Type(OctetString):
    """Custom type zxAnEponOltVirtualIfBERStatisticOnuFER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltVirtualIfBERStatisticOnuFER_Type.__name__ = "OctetString"
_ZxAnEponOltVirtualIfBERStatisticOnuFER_Object = MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuFER = _ZxAnEponOltVirtualIfBERStatisticOnuFER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 1, 1, 2),
    _ZxAnEponOltVirtualIfBERStatisticOnuFER_Type()
)
zxAnEponOltVirtualIfBERStatisticOnuFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticOnuFER.setStatus("current")
_ZxAnEponOltPhyPortStatisticTable_Object = MibTable
zxAnEponOltPhyPortStatisticTable = _ZxAnEponOltPhyPortStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticTable.setStatus("current")
_ZxAnEponOltPhyPortStatisticEntry_Object = MibTableRow
zxAnEponOltPhyPortStatisticEntry = _ZxAnEponOltPhyPortStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 2, 1)
)
zxAnEponOltPhyPortStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticEntry.setStatus("current")


class _ZxAnEponOltPhyPortStatisticOltPonAverageBER_Type(OctetString):
    """Custom type zxAnEponOltPhyPortStatisticOltPonAverageBER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltPhyPortStatisticOltPonAverageBER_Type.__name__ = "OctetString"
_ZxAnEponOltPhyPortStatisticOltPonAverageBER_Object = MibTableColumn
zxAnEponOltPhyPortStatisticOltPonAverageBER = _ZxAnEponOltPhyPortStatisticOltPonAverageBER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 2, 1, 1),
    _ZxAnEponOltPhyPortStatisticOltPonAverageBER_Type()
)
zxAnEponOltPhyPortStatisticOltPonAverageBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticOltPonAverageBER.setStatus("current")


class _ZxAnEponOltPhyPortStatisticOltSysAverageBER_Type(OctetString):
    """Custom type zxAnEponOltPhyPortStatisticOltSysAverageBER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltPhyPortStatisticOltSysAverageBER_Type.__name__ = "OctetString"
_ZxAnEponOltPhyPortStatisticOltSysAverageBER_Object = MibTableColumn
zxAnEponOltPhyPortStatisticOltSysAverageBER = _ZxAnEponOltPhyPortStatisticOltSysAverageBER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 2, 1, 2),
    _ZxAnEponOltPhyPortStatisticOltSysAverageBER_Type()
)
zxAnEponOltPhyPortStatisticOltSysAverageBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticOltSysAverageBER.setStatus("current")
_ZxAnEponEtherStatsTable_Object = MibTable
zxAnEponEtherStatsTable = _ZxAnEponEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnEponEtherStatsTable.setStatus("current")
_ZxAnEponEtherStatsEntry_Object = MibTableRow
zxAnEponEtherStatsEntry = _ZxAnEponEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1)
)
zxAnEponEtherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponEtherStatsEntry.setStatus("current")
_ZxAnEponEtherStatsDropEvents_Type = Counter32
_ZxAnEponEtherStatsDropEvents_Object = MibTableColumn
zxAnEponEtherStatsDropEvents = _ZxAnEponEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 1),
    _ZxAnEponEtherStatsDropEvents_Type()
)
zxAnEponEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsDropEvents.setStatus("current")
_ZxAnEponEtherStatsOctets_Type = Counter32
_ZxAnEponEtherStatsOctets_Object = MibTableColumn
zxAnEponEtherStatsOctets = _ZxAnEponEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 2),
    _ZxAnEponEtherStatsOctets_Type()
)
zxAnEponEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOctets.setStatus("current")
_ZxAnEponEtherStatsPkts_Type = Counter32
_ZxAnEponEtherStatsPkts_Object = MibTableColumn
zxAnEponEtherStatsPkts = _ZxAnEponEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 3),
    _ZxAnEponEtherStatsPkts_Type()
)
zxAnEponEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts.setStatus("current")
_ZxAnEponEtherStatsBroadcastPkts_Type = Counter32
_ZxAnEponEtherStatsBroadcastPkts_Object = MibTableColumn
zxAnEponEtherStatsBroadcastPkts = _ZxAnEponEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 4),
    _ZxAnEponEtherStatsBroadcastPkts_Type()
)
zxAnEponEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsBroadcastPkts.setStatus("current")
_ZxAnEponEtherStatsMulticastPkts_Type = Counter32
_ZxAnEponEtherStatsMulticastPkts_Object = MibTableColumn
zxAnEponEtherStatsMulticastPkts = _ZxAnEponEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 5),
    _ZxAnEponEtherStatsMulticastPkts_Type()
)
zxAnEponEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsMulticastPkts.setStatus("current")
_ZxAnEponEtherStatsCRCAlignErrors_Type = Counter32
_ZxAnEponEtherStatsCRCAlignErrors_Object = MibTableColumn
zxAnEponEtherStatsCRCAlignErrors = _ZxAnEponEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 6),
    _ZxAnEponEtherStatsCRCAlignErrors_Type()
)
zxAnEponEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCRCAlignErrors.setStatus("current")
_ZxAnEponEtherStatsUndersizePkts_Type = Counter32
_ZxAnEponEtherStatsUndersizePkts_Object = MibTableColumn
zxAnEponEtherStatsUndersizePkts = _ZxAnEponEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 7),
    _ZxAnEponEtherStatsUndersizePkts_Type()
)
zxAnEponEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsUndersizePkts.setStatus("current")
_ZxAnEponEtherStatsOversizePkts_Type = Counter32
_ZxAnEponEtherStatsOversizePkts_Object = MibTableColumn
zxAnEponEtherStatsOversizePkts = _ZxAnEponEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 8),
    _ZxAnEponEtherStatsOversizePkts_Type()
)
zxAnEponEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOversizePkts.setStatus("current")
_ZxAnEponEtherStatsFragments_Type = Counter32
_ZxAnEponEtherStatsFragments_Object = MibTableColumn
zxAnEponEtherStatsFragments = _ZxAnEponEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 9),
    _ZxAnEponEtherStatsFragments_Type()
)
zxAnEponEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsFragments.setStatus("current")
_ZxAnEponEtherStatsJabbers_Type = Counter32
_ZxAnEponEtherStatsJabbers_Object = MibTableColumn
zxAnEponEtherStatsJabbers = _ZxAnEponEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 10),
    _ZxAnEponEtherStatsJabbers_Type()
)
zxAnEponEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsJabbers.setStatus("current")
_ZxAnEponEtherStatsCollisions_Type = Counter32
_ZxAnEponEtherStatsCollisions_Object = MibTableColumn
zxAnEponEtherStatsCollisions = _ZxAnEponEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 11),
    _ZxAnEponEtherStatsCollisions_Type()
)
zxAnEponEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCollisions.setStatus("current")
_ZxAnEponEtherStatsPkts64Octets_Type = Counter32
_ZxAnEponEtherStatsPkts64Octets_Object = MibTableColumn
zxAnEponEtherStatsPkts64Octets = _ZxAnEponEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 12),
    _ZxAnEponEtherStatsPkts64Octets_Type()
)
zxAnEponEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts64Octets.setStatus("current")
_ZxAnEponEtherStatsPkts65to127Octets_Type = Counter32
_ZxAnEponEtherStatsPkts65to127Octets_Object = MibTableColumn
zxAnEponEtherStatsPkts65to127Octets = _ZxAnEponEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 13),
    _ZxAnEponEtherStatsPkts65to127Octets_Type()
)
zxAnEponEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts65to127Octets.setStatus("current")
_ZxAnEponEtherStatsPkts128to255Octets_Type = Counter32
_ZxAnEponEtherStatsPkts128to255Octets_Object = MibTableColumn
zxAnEponEtherStatsPkts128to255Octets = _ZxAnEponEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 14),
    _ZxAnEponEtherStatsPkts128to255Octets_Type()
)
zxAnEponEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts128to255Octets.setStatus("current")
_ZxAnEponEtherStatsPkts256to511Octets_Type = Counter32
_ZxAnEponEtherStatsPkts256to511Octets_Object = MibTableColumn
zxAnEponEtherStatsPkts256to511Octets = _ZxAnEponEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 15),
    _ZxAnEponEtherStatsPkts256to511Octets_Type()
)
zxAnEponEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts256to511Octets.setStatus("current")
_ZxAnEponEtherStatsPkts512to1023Octets_Type = Counter32
_ZxAnEponEtherStatsPkts512to1023Octets_Object = MibTableColumn
zxAnEponEtherStatsPkts512to1023Octets = _ZxAnEponEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 16),
    _ZxAnEponEtherStatsPkts512to1023Octets_Type()
)
zxAnEponEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts512to1023Octets.setStatus("current")
_ZxAnEponEtherStatsPkts1024to1518Octets_Type = Counter32
_ZxAnEponEtherStatsPkts1024to1518Octets_Object = MibTableColumn
zxAnEponEtherStatsPkts1024to1518Octets = _ZxAnEponEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 3, 1, 17),
    _ZxAnEponEtherStatsPkts1024to1518Octets_Type()
)
zxAnEponEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts1024to1518Octets.setStatus("current")
_ZxAnEponIfTable_Object = MibTable
zxAnEponIfTable = _ZxAnEponIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnEponIfTable.setStatus("current")
_ZxAnEponIfEntry_Object = MibTableRow
zxAnEponIfEntry = _ZxAnEponIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1)
)
zxAnEponIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponIfEntry.setStatus("current")
_ZxAnEponIfInOctets_Type = Counter32
_ZxAnEponIfInOctets_Object = MibTableColumn
zxAnEponIfInOctets = _ZxAnEponIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 1),
    _ZxAnEponIfInOctets_Type()
)
zxAnEponIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInOctets.setStatus("current")
_ZxAnEponIfInUcastPkts_Type = Counter32
_ZxAnEponIfInUcastPkts_Object = MibTableColumn
zxAnEponIfInUcastPkts = _ZxAnEponIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 2),
    _ZxAnEponIfInUcastPkts_Type()
)
zxAnEponIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInUcastPkts.setStatus("current")
_ZxAnEponIfInNUcastPkts_Type = Counter32
_ZxAnEponIfInNUcastPkts_Object = MibTableColumn
zxAnEponIfInNUcastPkts = _ZxAnEponIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 3),
    _ZxAnEponIfInNUcastPkts_Type()
)
zxAnEponIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInNUcastPkts.setStatus("deprecated")
_ZxAnEponIfInDiscards_Type = Counter32
_ZxAnEponIfInDiscards_Object = MibTableColumn
zxAnEponIfInDiscards = _ZxAnEponIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 4),
    _ZxAnEponIfInDiscards_Type()
)
zxAnEponIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInDiscards.setStatus("current")
_ZxAnEponIfInErrors_Type = Counter32
_ZxAnEponIfInErrors_Object = MibTableColumn
zxAnEponIfInErrors = _ZxAnEponIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 5),
    _ZxAnEponIfInErrors_Type()
)
zxAnEponIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInErrors.setStatus("current")
_ZxAnEponIfInUnknownProtos_Type = Counter32
_ZxAnEponIfInUnknownProtos_Object = MibTableColumn
zxAnEponIfInUnknownProtos = _ZxAnEponIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 6),
    _ZxAnEponIfInUnknownProtos_Type()
)
zxAnEponIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInUnknownProtos.setStatus("current")
_ZxAnEponIfOutOctets_Type = Counter32
_ZxAnEponIfOutOctets_Object = MibTableColumn
zxAnEponIfOutOctets = _ZxAnEponIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 7),
    _ZxAnEponIfOutOctets_Type()
)
zxAnEponIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutOctets.setStatus("current")
_ZxAnEponIfOutUcastPkts_Type = Counter32
_ZxAnEponIfOutUcastPkts_Object = MibTableColumn
zxAnEponIfOutUcastPkts = _ZxAnEponIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 8),
    _ZxAnEponIfOutUcastPkts_Type()
)
zxAnEponIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutUcastPkts.setStatus("current")
_ZxAnEponIfOutNUcastPkts_Type = Counter32
_ZxAnEponIfOutNUcastPkts_Object = MibTableColumn
zxAnEponIfOutNUcastPkts = _ZxAnEponIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 9),
    _ZxAnEponIfOutNUcastPkts_Type()
)
zxAnEponIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutNUcastPkts.setStatus("deprecated")
_ZxAnEponIfOutDiscards_Type = Counter32
_ZxAnEponIfOutDiscards_Object = MibTableColumn
zxAnEponIfOutDiscards = _ZxAnEponIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 10),
    _ZxAnEponIfOutDiscards_Type()
)
zxAnEponIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutDiscards.setStatus("current")
_ZxAnEponIfOutErrors_Type = Counter32
_ZxAnEponIfOutErrors_Object = MibTableColumn
zxAnEponIfOutErrors = _ZxAnEponIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 4, 1, 11),
    _ZxAnEponIfOutErrors_Type()
)
zxAnEponIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutErrors.setStatus("current")
_ZxAnEponIfXTable_Object = MibTable
zxAnEponIfXTable = _ZxAnEponIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnEponIfXTable.setStatus("current")
_ZxAnEponIfXEntry_Object = MibTableRow
zxAnEponIfXEntry = _ZxAnEponIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnEponIfXEntry.setStatus("current")
_ZxAnEponIfInMulticastPkts_Type = Counter32
_ZxAnEponIfInMulticastPkts_Object = MibTableColumn
zxAnEponIfInMulticastPkts = _ZxAnEponIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 1),
    _ZxAnEponIfInMulticastPkts_Type()
)
zxAnEponIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInMulticastPkts.setStatus("current")
_ZxAnEponIfInBroadcastPkts_Type = Counter32
_ZxAnEponIfInBroadcastPkts_Object = MibTableColumn
zxAnEponIfInBroadcastPkts = _ZxAnEponIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 2),
    _ZxAnEponIfInBroadcastPkts_Type()
)
zxAnEponIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInBroadcastPkts.setStatus("current")
_ZxAnEponIfOutMulticastPkts_Type = Counter32
_ZxAnEponIfOutMulticastPkts_Object = MibTableColumn
zxAnEponIfOutMulticastPkts = _ZxAnEponIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 3),
    _ZxAnEponIfOutMulticastPkts_Type()
)
zxAnEponIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutMulticastPkts.setStatus("current")
_ZxAnEponIfOutBroadcastPkts_Type = Counter32
_ZxAnEponIfOutBroadcastPkts_Object = MibTableColumn
zxAnEponIfOutBroadcastPkts = _ZxAnEponIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 4),
    _ZxAnEponIfOutBroadcastPkts_Type()
)
zxAnEponIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutBroadcastPkts.setStatus("current")
_ZxAnEponIfHCInOctets_Type = Counter64
_ZxAnEponIfHCInOctets_Object = MibTableColumn
zxAnEponIfHCInOctets = _ZxAnEponIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 5),
    _ZxAnEponIfHCInOctets_Type()
)
zxAnEponIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInOctets.setStatus("current")
_ZxAnEponIfHCInUcastPkts_Type = Counter64
_ZxAnEponIfHCInUcastPkts_Object = MibTableColumn
zxAnEponIfHCInUcastPkts = _ZxAnEponIfHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 6),
    _ZxAnEponIfHCInUcastPkts_Type()
)
zxAnEponIfHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInUcastPkts.setStatus("current")
_ZxAnEponIfHCInMulticastPkts_Type = Counter64
_ZxAnEponIfHCInMulticastPkts_Object = MibTableColumn
zxAnEponIfHCInMulticastPkts = _ZxAnEponIfHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 7),
    _ZxAnEponIfHCInMulticastPkts_Type()
)
zxAnEponIfHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInMulticastPkts.setStatus("current")
_ZxAnEponIfHCInBroadcastPkts_Type = Counter64
_ZxAnEponIfHCInBroadcastPkts_Object = MibTableColumn
zxAnEponIfHCInBroadcastPkts = _ZxAnEponIfHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 8),
    _ZxAnEponIfHCInBroadcastPkts_Type()
)
zxAnEponIfHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInBroadcastPkts.setStatus("current")
_ZxAnEponIfHCOutOctets_Type = Counter64
_ZxAnEponIfHCOutOctets_Object = MibTableColumn
zxAnEponIfHCOutOctets = _ZxAnEponIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 9),
    _ZxAnEponIfHCOutOctets_Type()
)
zxAnEponIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutOctets.setStatus("current")
_ZxAnEponIfHCOutUcastPkts_Type = Counter64
_ZxAnEponIfHCOutUcastPkts_Object = MibTableColumn
zxAnEponIfHCOutUcastPkts = _ZxAnEponIfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 10),
    _ZxAnEponIfHCOutUcastPkts_Type()
)
zxAnEponIfHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutUcastPkts.setStatus("current")
_ZxAnEponIfHCOutMulticastPkts_Type = Counter64
_ZxAnEponIfHCOutMulticastPkts_Object = MibTableColumn
zxAnEponIfHCOutMulticastPkts = _ZxAnEponIfHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 11),
    _ZxAnEponIfHCOutMulticastPkts_Type()
)
zxAnEponIfHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutMulticastPkts.setStatus("current")
_ZxAnEponIfHCOutBroadcastPkts_Type = Counter64
_ZxAnEponIfHCOutBroadcastPkts_Object = MibTableColumn
zxAnEponIfHCOutBroadcastPkts = _ZxAnEponIfHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 5, 1, 12),
    _ZxAnEponIfHCOutBroadcastPkts_Type()
)
zxAnEponIfHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutBroadcastPkts.setStatus("current")
_ZxAnEponDot3PauseTable_Object = MibTable
zxAnEponDot3PauseTable = _ZxAnEponDot3PauseTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnEponDot3PauseTable.setStatus("current")
_ZxAnEponDot3PauseEntry_Object = MibTableRow
zxAnEponDot3PauseEntry = _ZxAnEponDot3PauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 6, 1)
)
zxAnEponDot3PauseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3PauseEntry.setStatus("current")
_ZxAnEponDot3InPauseFrames_Type = Counter32
_ZxAnEponDot3InPauseFrames_Object = MibTableColumn
zxAnEponDot3InPauseFrames = _ZxAnEponDot3InPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 6, 1, 1),
    _ZxAnEponDot3InPauseFrames_Type()
)
zxAnEponDot3InPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3InPauseFrames.setStatus("current")
_ZxAnEponDot3OutPauseFrames_Type = Counter32
_ZxAnEponDot3OutPauseFrames_Object = MibTableColumn
zxAnEponDot3OutPauseFrames = _ZxAnEponDot3OutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 6, 1, 2),
    _ZxAnEponDot3OutPauseFrames_Type()
)
zxAnEponDot3OutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OutPauseFrames.setStatus("current")
_ZxAnEponDot3HCInPauseFrames_Type = Counter64
_ZxAnEponDot3HCInPauseFrames_Object = MibTableColumn
zxAnEponDot3HCInPauseFrames = _ZxAnEponDot3HCInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 6, 1, 3),
    _ZxAnEponDot3HCInPauseFrames_Type()
)
zxAnEponDot3HCInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCInPauseFrames.setStatus("current")
_ZxAnEponDot3HCOutPauseFrames_Type = Counter64
_ZxAnEponDot3HCOutPauseFrames_Object = MibTableColumn
zxAnEponDot3HCOutPauseFrames = _ZxAnEponDot3HCOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 6, 1, 4),
    _ZxAnEponDot3HCOutPauseFrames_Type()
)
zxAnEponDot3HCOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCOutPauseFrames.setStatus("current")
_ZxAnEponDot3HCStatsTable_Object = MibTable
zxAnEponDot3HCStatsTable = _ZxAnEponDot3HCStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsTable.setStatus("current")
_ZxAnEponDot3HCStatsEntry_Object = MibTableRow
zxAnEponDot3HCStatsEntry = _ZxAnEponDot3HCStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1)
)
zxAnEponDot3HCStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsEntry.setStatus("current")
_ZxAnEponDot3HCStatsAlignmentErrors_Type = Counter64
_ZxAnEponDot3HCStatsAlignmentErrors_Object = MibTableColumn
zxAnEponDot3HCStatsAlignmentErrors = _ZxAnEponDot3HCStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1, 1),
    _ZxAnEponDot3HCStatsAlignmentErrors_Type()
)
zxAnEponDot3HCStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsAlignmentErrors.setStatus("current")
_ZxAnEponDot3HCStatsFCSErrors_Type = Counter64
_ZxAnEponDot3HCStatsFCSErrors_Object = MibTableColumn
zxAnEponDot3HCStatsFCSErrors = _ZxAnEponDot3HCStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1, 2),
    _ZxAnEponDot3HCStatsFCSErrors_Type()
)
zxAnEponDot3HCStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsFCSErrors.setStatus("current")
_ZxAnEponDot3HCStatsInternalMacTransmitErrors_Type = Counter64
_ZxAnEponDot3HCStatsInternalMacTransmitErrors_Object = MibTableColumn
zxAnEponDot3HCStatsInternalMacTransmitErrors = _ZxAnEponDot3HCStatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1, 3),
    _ZxAnEponDot3HCStatsInternalMacTransmitErrors_Type()
)
zxAnEponDot3HCStatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsInternalMacTransmitErrors.setStatus("current")
_ZxAnEponDot3HCStatsFrameTooLongs_Type = Counter64
_ZxAnEponDot3HCStatsFrameTooLongs_Object = MibTableColumn
zxAnEponDot3HCStatsFrameTooLongs = _ZxAnEponDot3HCStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1, 4),
    _ZxAnEponDot3HCStatsFrameTooLongs_Type()
)
zxAnEponDot3HCStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsFrameTooLongs.setStatus("current")
_ZxAnEponDot3HCStatsInternalMacReceiveErrors_Type = Counter64
_ZxAnEponDot3HCStatsInternalMacReceiveErrors_Object = MibTableColumn
zxAnEponDot3HCStatsInternalMacReceiveErrors = _ZxAnEponDot3HCStatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1, 5),
    _ZxAnEponDot3HCStatsInternalMacReceiveErrors_Type()
)
zxAnEponDot3HCStatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsInternalMacReceiveErrors.setStatus("current")
_ZxAnEponDot3HCStatsSymbolErrors_Type = Counter64
_ZxAnEponDot3HCStatsSymbolErrors_Object = MibTableColumn
zxAnEponDot3HCStatsSymbolErrors = _ZxAnEponDot3HCStatsSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 7, 1, 6),
    _ZxAnEponDot3HCStatsSymbolErrors_Type()
)
zxAnEponDot3HCStatsSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsSymbolErrors.setStatus("current")
_ZxAnEponIfXOltTable_Object = MibTable
zxAnEponIfXOltTable = _ZxAnEponIfXOltTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnEponIfXOltTable.setStatus("current")
_ZxAnEponIfXOltEntry_Object = MibTableRow
zxAnEponIfXOltEntry = _ZxAnEponIfXOltEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1)
)
if mibBuilder.loadTexts:
    zxAnEponIfXOltEntry.setStatus("current")
_ZxAnEponIfOltInMulticastPkts_Type = Counter32
_ZxAnEponIfOltInMulticastPkts_Object = MibTableColumn
zxAnEponIfOltInMulticastPkts = _ZxAnEponIfOltInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 1),
    _ZxAnEponIfOltInMulticastPkts_Type()
)
zxAnEponIfOltInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltInMulticastPkts.setStatus("current")
_ZxAnEponIfOltInBroadcastPkts_Type = Counter32
_ZxAnEponIfOltInBroadcastPkts_Object = MibTableColumn
zxAnEponIfOltInBroadcastPkts = _ZxAnEponIfOltInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 2),
    _ZxAnEponIfOltInBroadcastPkts_Type()
)
zxAnEponIfOltInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltInBroadcastPkts.setStatus("current")
_ZxAnEponIfOltOutMulticastPkts_Type = Counter32
_ZxAnEponIfOltOutMulticastPkts_Object = MibTableColumn
zxAnEponIfOltOutMulticastPkts = _ZxAnEponIfOltOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 3),
    _ZxAnEponIfOltOutMulticastPkts_Type()
)
zxAnEponIfOltOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltOutMulticastPkts.setStatus("current")
_ZxAnEponIfOltOutBroadcastPkts_Type = Counter32
_ZxAnEponIfOltOutBroadcastPkts_Object = MibTableColumn
zxAnEponIfOltOutBroadcastPkts = _ZxAnEponIfOltOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 4),
    _ZxAnEponIfOltOutBroadcastPkts_Type()
)
zxAnEponIfOltOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltOutBroadcastPkts.setStatus("current")
_ZxAnEponIfOltHCInOctets_Type = Counter64
_ZxAnEponIfOltHCInOctets_Object = MibTableColumn
zxAnEponIfOltHCInOctets = _ZxAnEponIfOltHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 5),
    _ZxAnEponIfOltHCInOctets_Type()
)
zxAnEponIfOltHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInOctets.setStatus("current")
_ZxAnEponIfOltHCInUcastPkts_Type = Counter64
_ZxAnEponIfOltHCInUcastPkts_Object = MibTableColumn
zxAnEponIfOltHCInUcastPkts = _ZxAnEponIfOltHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 6),
    _ZxAnEponIfOltHCInUcastPkts_Type()
)
zxAnEponIfOltHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInUcastPkts.setStatus("current")
_ZxAnEponIfOltHCInMulticastPkts_Type = Counter64
_ZxAnEponIfOltHCInMulticastPkts_Object = MibTableColumn
zxAnEponIfOltHCInMulticastPkts = _ZxAnEponIfOltHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 7),
    _ZxAnEponIfOltHCInMulticastPkts_Type()
)
zxAnEponIfOltHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInMulticastPkts.setStatus("current")
_ZxAnEponIfOltHCInBroadcastPkts_Type = Counter64
_ZxAnEponIfOltHCInBroadcastPkts_Object = MibTableColumn
zxAnEponIfOltHCInBroadcastPkts = _ZxAnEponIfOltHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 8),
    _ZxAnEponIfOltHCInBroadcastPkts_Type()
)
zxAnEponIfOltHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInBroadcastPkts.setStatus("current")
_ZxAnEponIfOltHCOutOctets_Type = Counter64
_ZxAnEponIfOltHCOutOctets_Object = MibTableColumn
zxAnEponIfOltHCOutOctets = _ZxAnEponIfOltHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 9),
    _ZxAnEponIfOltHCOutOctets_Type()
)
zxAnEponIfOltHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutOctets.setStatus("current")
_ZxAnEponIfOltHCOutUcastPkts_Type = Counter64
_ZxAnEponIfOltHCOutUcastPkts_Object = MibTableColumn
zxAnEponIfOltHCOutUcastPkts = _ZxAnEponIfOltHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 10),
    _ZxAnEponIfOltHCOutUcastPkts_Type()
)
zxAnEponIfOltHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutUcastPkts.setStatus("current")
_ZxAnEponIfOltHCOutMulticastPkts_Type = Counter64
_ZxAnEponIfOltHCOutMulticastPkts_Object = MibTableColumn
zxAnEponIfOltHCOutMulticastPkts = _ZxAnEponIfOltHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 11),
    _ZxAnEponIfOltHCOutMulticastPkts_Type()
)
zxAnEponIfOltHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutMulticastPkts.setStatus("current")
_ZxAnEponIfOltHCOutBroadcastPkts_Type = Counter64
_ZxAnEponIfOltHCOutBroadcastPkts_Object = MibTableColumn
zxAnEponIfOltHCOutBroadcastPkts = _ZxAnEponIfOltHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 1, 8, 1, 12),
    _ZxAnEponIfOltHCOutBroadcastPkts_Type()
)
zxAnEponIfOltHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutBroadcastPkts.setStatus("current")
_ZxAnEponPmCurrent_ObjectIdentity = ObjectIdentity
zxAnEponPmCurrent = _ZxAnEponPmCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2)
)
_ZxAnEponDot3MpcpStatCurrentTable_Object = MibTable
zxAnEponDot3MpcpStatCurrentTable = _ZxAnEponDot3MpcpStatCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpStatCurrentTable.setStatus("current")
_ZxAnEponDot3MpcpStatCurrentEntry_Object = MibTableRow
zxAnEponDot3MpcpStatCurrentEntry = _ZxAnEponDot3MpcpStatCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1)
)
zxAnEponDot3MpcpStatCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpStatCurrentEntry.setStatus("current")
_ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Type = Counter64
_ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Object = MibTableColumn
zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent = _ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 1),
    _ZxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent_Type()
)
zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent.setUnits("frames")
_ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Type = Counter64
_ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Object = MibTableColumn
zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent = _ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 2),
    _ZxAnEponDot3MpcpMACCtrlFramesReceivedCurrent_Type()
)
zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent.setUnits("frames")
_ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Type = Counter32
_ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Object = MibTableColumn
zxAnEponDot3MpcpDiscoveryWindowsSentCurrent = _ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 3),
    _ZxAnEponDot3MpcpDiscoveryWindowsSentCurrent_Type()
)
zxAnEponDot3MpcpDiscoveryWindowsSentCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpDiscoveryWindowsSentCurrent.setStatus("current")
_ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Type = Counter32
_ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Object = MibTableColumn
zxAnEponDot3MpcpDiscoveryTimeoutCurrent = _ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 4),
    _ZxAnEponDot3MpcpDiscoveryTimeoutCurrent_Type()
)
zxAnEponDot3MpcpDiscoveryTimeoutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpDiscoveryTimeoutCurrent.setStatus("current")
_ZxAnEponDot3MpcpTxRegRequestCurrent_Type = Counter64
_ZxAnEponDot3MpcpTxRegRequestCurrent_Object = MibTableColumn
zxAnEponDot3MpcpTxRegRequestCurrent = _ZxAnEponDot3MpcpTxRegRequestCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 5),
    _ZxAnEponDot3MpcpTxRegRequestCurrent_Type()
)
zxAnEponDot3MpcpTxRegRequestCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxRegRequestCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxRegRequestCurrent.setUnits("frames")
_ZxAnEponDot3MpcpRxRegRequestCurrent_Type = Counter64
_ZxAnEponDot3MpcpRxRegRequestCurrent_Object = MibTableColumn
zxAnEponDot3MpcpRxRegRequestCurrent = _ZxAnEponDot3MpcpRxRegRequestCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 6),
    _ZxAnEponDot3MpcpRxRegRequestCurrent_Type()
)
zxAnEponDot3MpcpRxRegRequestCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxRegRequestCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxRegRequestCurrent.setUnits("frames")
_ZxAnEponDot3MpcpTxRegAckCurrent_Type = Counter64
_ZxAnEponDot3MpcpTxRegAckCurrent_Object = MibTableColumn
zxAnEponDot3MpcpTxRegAckCurrent = _ZxAnEponDot3MpcpTxRegAckCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 7),
    _ZxAnEponDot3MpcpTxRegAckCurrent_Type()
)
zxAnEponDot3MpcpTxRegAckCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxRegAckCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxRegAckCurrent.setUnits("frames")
_ZxAnEponDot3MpcpRxRegAckCurrent_Type = Counter64
_ZxAnEponDot3MpcpRxRegAckCurrent_Object = MibTableColumn
zxAnEponDot3MpcpRxRegAckCurrent = _ZxAnEponDot3MpcpRxRegAckCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 8),
    _ZxAnEponDot3MpcpRxRegAckCurrent_Type()
)
zxAnEponDot3MpcpRxRegAckCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxRegAckCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxRegAckCurrent.setUnits("frames")
_ZxAnEponDot3MpcpTxReportCurrent_Type = Counter64
_ZxAnEponDot3MpcpTxReportCurrent_Object = MibTableColumn
zxAnEponDot3MpcpTxReportCurrent = _ZxAnEponDot3MpcpTxReportCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 9),
    _ZxAnEponDot3MpcpTxReportCurrent_Type()
)
zxAnEponDot3MpcpTxReportCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxReportCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxReportCurrent.setUnits("frames")
_ZxAnEponDot3MpcpRxReportCurrent_Type = Counter64
_ZxAnEponDot3MpcpRxReportCurrent_Object = MibTableColumn
zxAnEponDot3MpcpRxReportCurrent = _ZxAnEponDot3MpcpRxReportCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 10),
    _ZxAnEponDot3MpcpRxReportCurrent_Type()
)
zxAnEponDot3MpcpRxReportCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxReportCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxReportCurrent.setUnits("frames")
_ZxAnEponDot3MpcpTxGateCurrent_Type = Counter64
_ZxAnEponDot3MpcpTxGateCurrent_Object = MibTableColumn
zxAnEponDot3MpcpTxGateCurrent = _ZxAnEponDot3MpcpTxGateCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 11),
    _ZxAnEponDot3MpcpTxGateCurrent_Type()
)
zxAnEponDot3MpcpTxGateCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxGateCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxGateCurrent.setUnits("frames")
_ZxAnEponDot3MpcpRxGateCurrent_Type = Counter64
_ZxAnEponDot3MpcpRxGateCurrent_Object = MibTableColumn
zxAnEponDot3MpcpRxGateCurrent = _ZxAnEponDot3MpcpRxGateCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 12),
    _ZxAnEponDot3MpcpRxGateCurrent_Type()
)
zxAnEponDot3MpcpRxGateCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxGateCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxGateCurrent.setUnits("frames")
_ZxAnEponDot3MpcpTxRegisterCurrent_Type = Counter64
_ZxAnEponDot3MpcpTxRegisterCurrent_Object = MibTableColumn
zxAnEponDot3MpcpTxRegisterCurrent = _ZxAnEponDot3MpcpTxRegisterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 13),
    _ZxAnEponDot3MpcpTxRegisterCurrent_Type()
)
zxAnEponDot3MpcpTxRegisterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxRegisterCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpTxRegisterCurrent.setUnits("frames")
_ZxAnEponDot3MpcpRxRegisterCurrent_Type = Counter64
_ZxAnEponDot3MpcpRxRegisterCurrent_Object = MibTableColumn
zxAnEponDot3MpcpRxRegisterCurrent = _ZxAnEponDot3MpcpRxRegisterCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 1, 1, 14),
    _ZxAnEponDot3MpcpRxRegisterCurrent_Type()
)
zxAnEponDot3MpcpRxRegisterCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxRegisterCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3MpcpRxRegisterCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationStatCurrentTable_Object = MibTable
zxAnEponDot3OmpEmulationStatCurrentTable = _ZxAnEponDot3OmpEmulationStatCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationStatCurrentTable.setStatus("current")
_ZxAnEponDot3OmpEmulationStatCurrentEntry_Object = MibTableRow
zxAnEponDot3OmpEmulationStatCurrentEntry = _ZxAnEponDot3OmpEmulationStatCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1)
)
zxAnEponDot3OmpEmulationStatCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationStatCurrentEntry.setStatus("current")
_ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationSLDErrorsCurrent = _ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 1),
    _ZxAnEponDot3OmpEmulationSLDErrorsCurrent_Type()
)
zxAnEponDot3OmpEmulationSLDErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationSLDErrorsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationSLDErrorsCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationCRC8ErrorsCurrent = _ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 2),
    _ZxAnEponDot3OmpEmulationCRC8ErrorsCurrent_Type()
)
zxAnEponDot3OmpEmulationCRC8ErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationCRC8ErrorsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationCRC8ErrorsCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationBadLLIDCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationBadLLIDCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationBadLLIDCurrent = _ZxAnEponDot3OmpEmulationBadLLIDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 3),
    _ZxAnEponDot3OmpEmulationBadLLIDCurrent_Type()
)
zxAnEponDot3OmpEmulationBadLLIDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationBadLLIDCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationBadLLIDCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationGoodLLIDCurrent = _ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 4),
    _ZxAnEponDot3OmpEmulationGoodLLIDCurrent_Type()
)
zxAnEponDot3OmpEmulationGoodLLIDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationGoodLLIDCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationGoodLLIDCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent = _ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 5),
    _ZxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent_Type()
)
zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent = _ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 6),
    _ZxAnEponDot3OmpEmulationOltPonCastLLIDCurrent_Type()
)
zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent = _ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 7),
    _ZxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent_Type()
)
zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent = _ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 8),
    _ZxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent_Type()
)
zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent = _ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 9),
    _ZxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent_Type()
)
zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent.setUnits("frames")
_ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Type = Counter64
_ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Object = MibTableColumn
zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent = _ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 2, 1, 10),
    _ZxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent_Type()
)
zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent.setUnits("frames")
_ZxAnEponDot3EponFecCurrentTable_Object = MibTable
zxAnEponDot3EponFecCurrentTable = _ZxAnEponDot3EponFecCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecCurrentTable.setStatus("current")
_ZxAnEponDot3EponFecCurrentEntry_Object = MibTableRow
zxAnEponDot3EponFecCurrentEntry = _ZxAnEponDot3EponFecCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1)
)
zxAnEponDot3EponFecCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecCurrentEntry.setStatus("current")
_ZxAnEponDot3EponFecPCSCodingViolationCurrent_Type = Counter64
_ZxAnEponDot3EponFecPCSCodingViolationCurrent_Object = MibTableColumn
zxAnEponDot3EponFecPCSCodingViolationCurrent = _ZxAnEponDot3EponFecPCSCodingViolationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1, 1),
    _ZxAnEponDot3EponFecPCSCodingViolationCurrent_Type()
)
zxAnEponDot3EponFecPCSCodingViolationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecPCSCodingViolationCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecPCSCodingViolationCurrent.setUnits("octets")


class _ZxAnEponDot3EponFecAbilityCurrent_Type(Integer32):
    """Custom type zxAnEponDot3EponFecAbilityCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("unsupported", 2),
          ("supported", 3))
    )


_ZxAnEponDot3EponFecAbilityCurrent_Type.__name__ = "Integer32"
_ZxAnEponDot3EponFecAbilityCurrent_Object = MibTableColumn
zxAnEponDot3EponFecAbilityCurrent = _ZxAnEponDot3EponFecAbilityCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1, 2),
    _ZxAnEponDot3EponFecAbilityCurrent_Type()
)
zxAnEponDot3EponFecAbilityCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecAbilityCurrent.setStatus("current")


class _ZxAnEponDot3EponFecModeCurrent_Type(Integer32):
    """Custom type zxAnEponDot3EponFecModeCurrent based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_ZxAnEponDot3EponFecModeCurrent_Type.__name__ = "Integer32"
_ZxAnEponDot3EponFecModeCurrent_Object = MibTableColumn
zxAnEponDot3EponFecModeCurrent = _ZxAnEponDot3EponFecModeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1, 3),
    _ZxAnEponDot3EponFecModeCurrent_Type()
)
zxAnEponDot3EponFecModeCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecModeCurrent.setStatus("current")
_ZxAnEponDot3EponFecCorrectedBlocksCurrent_Type = Counter64
_ZxAnEponDot3EponFecCorrectedBlocksCurrent_Object = MibTableColumn
zxAnEponDot3EponFecCorrectedBlocksCurrent = _ZxAnEponDot3EponFecCorrectedBlocksCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1, 4),
    _ZxAnEponDot3EponFecCorrectedBlocksCurrent_Type()
)
zxAnEponDot3EponFecCorrectedBlocksCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecCorrectedBlocksCurrent.setStatus("current")
_ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Type = Counter64
_ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Object = MibTableColumn
zxAnEponDot3EponFecUncorrectableBlocksCurrent = _ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1, 5),
    _ZxAnEponDot3EponFecUncorrectableBlocksCurrent_Type()
)
zxAnEponDot3EponFecUncorrectableBlocksCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecUncorrectableBlocksCurrent.setStatus("current")
_ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Type = Counter64
_ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Object = MibTableColumn
zxAnEponDot3EponFecBufferHeadCodingViolationCurrent = _ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 3, 1, 6),
    _ZxAnEponDot3EponFecBufferHeadCodingViolationCurrent_Type()
)
zxAnEponDot3EponFecBufferHeadCodingViolationCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecBufferHeadCodingViolationCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3EponFecBufferHeadCodingViolationCurrent.setUnits("octets")
_ZxAnEponDot3ExtPkgQueueCurrentTable_Object = MibTable
zxAnEponDot3ExtPkgQueueCurrentTable = _ZxAnEponDot3ExtPkgQueueCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgQueueCurrentTable.setStatus("current")
_ZxAnEponDot3ExtPkgQueueCurrentEntry_Object = MibTableRow
zxAnEponDot3ExtPkgQueueCurrentEntry = _ZxAnEponDot3ExtPkgQueueCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1)
)
zxAnEponDot3ExtPkgQueueCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXEPON-PERFORMANCE-MIB", "zxAnEponDot3QueueIndexCurrent"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgQueueCurrentEntry.setStatus("current")


class _ZxAnEponDot3QueueIndexCurrent_Type(Unsigned32):
    """Custom type zxAnEponDot3QueueIndexCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponDot3QueueIndexCurrent_Type.__name__ = "Unsigned32"
_ZxAnEponDot3QueueIndexCurrent_Object = MibTableColumn
zxAnEponDot3QueueIndexCurrent = _ZxAnEponDot3QueueIndexCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1, 1),
    _ZxAnEponDot3QueueIndexCurrent_Type()
)
zxAnEponDot3QueueIndexCurrent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponDot3QueueIndexCurrent.setStatus("current")


class _ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Type(Unsigned32):
    """Custom type zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Type.__name__ = "Unsigned32"
_ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Object = MibTableColumn
zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent = _ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1, 2),
    _ZxAnEponDot3ExtPkgObjectReportNumThresholdCurrent_Type()
)
zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent.setStatus("current")


class _ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Type(Unsigned32):
    """Custom type zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Type.__name__ = "Unsigned32"
_ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Object = MibTableColumn
zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent = _ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1, 3),
    _ZxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent_Type()
)
zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent.setStatus("current")
_ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Type = Counter64
_ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Object = MibTableColumn
zxAnEponDot3ExtPkgStatTxFramesQueueCurrent = _ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1, 4),
    _ZxAnEponDot3ExtPkgStatTxFramesQueueCurrent_Type()
)
zxAnEponDot3ExtPkgStatTxFramesQueueCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgStatTxFramesQueueCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgStatTxFramesQueueCurrent.setUnits("frames")
_ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Type = Counter64
_ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Object = MibTableColumn
zxAnEponDot3ExtPkgStatRxFramesQueueCurrent = _ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1, 5),
    _ZxAnEponDot3ExtPkgStatRxFramesQueueCurrent_Type()
)
zxAnEponDot3ExtPkgStatRxFramesQueueCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgStatRxFramesQueueCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgStatRxFramesQueueCurrent.setUnits("frames")
_ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Type = Counter64
_ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Object = MibTableColumn
zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent = _ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 4, 1, 6),
    _ZxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent_Type()
)
zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent.setUnits("frames")
_ZxAnEponDot3OamStatsCurrentTable_Object = MibTable
zxAnEponDot3OamStatsCurrentTable = _ZxAnEponDot3OamStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnEponDot3OamStatsCurrentTable.setStatus("current")
_ZxAnEponDot3OamStatsCurrentEntry_Object = MibTableRow
zxAnEponDot3OamStatsCurrentEntry = _ZxAnEponDot3OamStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1)
)
zxAnEponDot3OamStatsCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3OamStatsCurrentEntry.setStatus("current")
_ZxAnEponDot3OamInformationTxCurrent_Type = Counter32
_ZxAnEponDot3OamInformationTxCurrent_Object = MibTableColumn
zxAnEponDot3OamInformationTxCurrent = _ZxAnEponDot3OamInformationTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 1),
    _ZxAnEponDot3OamInformationTxCurrent_Type()
)
zxAnEponDot3OamInformationTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamInformationTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamInformationTxCurrent.setUnits("frames")
_ZxAnEponDot3OamInformationRxCurrent_Type = Counter32
_ZxAnEponDot3OamInformationRxCurrent_Object = MibTableColumn
zxAnEponDot3OamInformationRxCurrent = _ZxAnEponDot3OamInformationRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 2),
    _ZxAnEponDot3OamInformationRxCurrent_Type()
)
zxAnEponDot3OamInformationRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamInformationRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamInformationRxCurrent.setUnits("frames")
_ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Type = Counter32
_ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Object = MibTableColumn
zxAnEponDot3OamUniqueEventNotificationTxCurrent = _ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 3),
    _ZxAnEponDot3OamUniqueEventNotificationTxCurrent_Type()
)
zxAnEponDot3OamUniqueEventNotificationTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUniqueEventNotificationTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUniqueEventNotificationTxCurrent.setUnits("frames")
_ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Type = Counter32
_ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Object = MibTableColumn
zxAnEponDot3OamUniqueEventNotificationRxCurrent = _ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 4),
    _ZxAnEponDot3OamUniqueEventNotificationRxCurrent_Type()
)
zxAnEponDot3OamUniqueEventNotificationRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUniqueEventNotificationRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUniqueEventNotificationRxCurrent.setUnits("frames")
_ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Type = Counter32
_ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Object = MibTableColumn
zxAnEponDot3OamDuplicateEventNotificationTxCurrent = _ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 5),
    _ZxAnEponDot3OamDuplicateEventNotificationTxCurrent_Type()
)
zxAnEponDot3OamDuplicateEventNotificationTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamDuplicateEventNotificationTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamDuplicateEventNotificationTxCurrent.setUnits("frames")
_ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Type = Counter32
_ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Object = MibTableColumn
zxAnEponDot3OamDuplicateEventNotificationRxCurrent = _ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 6),
    _ZxAnEponDot3OamDuplicateEventNotificationRxCurrent_Type()
)
zxAnEponDot3OamDuplicateEventNotificationRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamDuplicateEventNotificationRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamDuplicateEventNotificationRxCurrent.setUnits("frames")
_ZxAnEponDot3OamLoopbackControlTxCurrent_Type = Counter32
_ZxAnEponDot3OamLoopbackControlTxCurrent_Object = MibTableColumn
zxAnEponDot3OamLoopbackControlTxCurrent = _ZxAnEponDot3OamLoopbackControlTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 7),
    _ZxAnEponDot3OamLoopbackControlTxCurrent_Type()
)
zxAnEponDot3OamLoopbackControlTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamLoopbackControlTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamLoopbackControlTxCurrent.setUnits("frames")
_ZxAnEponDot3OamLoopbackControlRxCurrent_Type = Counter32
_ZxAnEponDot3OamLoopbackControlRxCurrent_Object = MibTableColumn
zxAnEponDot3OamLoopbackControlRxCurrent = _ZxAnEponDot3OamLoopbackControlRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 8),
    _ZxAnEponDot3OamLoopbackControlRxCurrent_Type()
)
zxAnEponDot3OamLoopbackControlRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamLoopbackControlRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamLoopbackControlRxCurrent.setUnits("frames")
_ZxAnEponDot3OamVariableRequestTxCurrent_Type = Counter32
_ZxAnEponDot3OamVariableRequestTxCurrent_Object = MibTableColumn
zxAnEponDot3OamVariableRequestTxCurrent = _ZxAnEponDot3OamVariableRequestTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 9),
    _ZxAnEponDot3OamVariableRequestTxCurrent_Type()
)
zxAnEponDot3OamVariableRequestTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableRequestTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableRequestTxCurrent.setUnits("frames")
_ZxAnEponDot3OamVariableRequestRxCurrent_Type = Counter32
_ZxAnEponDot3OamVariableRequestRxCurrent_Object = MibTableColumn
zxAnEponDot3OamVariableRequestRxCurrent = _ZxAnEponDot3OamVariableRequestRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 10),
    _ZxAnEponDot3OamVariableRequestRxCurrent_Type()
)
zxAnEponDot3OamVariableRequestRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableRequestRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableRequestRxCurrent.setUnits("frames")
_ZxAnEponDot3OamVariableResponseTxCurrent_Type = Counter32
_ZxAnEponDot3OamVariableResponseTxCurrent_Object = MibTableColumn
zxAnEponDot3OamVariableResponseTxCurrent = _ZxAnEponDot3OamVariableResponseTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 11),
    _ZxAnEponDot3OamVariableResponseTxCurrent_Type()
)
zxAnEponDot3OamVariableResponseTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableResponseTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableResponseTxCurrent.setUnits("frames")
_ZxAnEponDot3OamVariableResponseRxCurrent_Type = Counter32
_ZxAnEponDot3OamVariableResponseRxCurrent_Object = MibTableColumn
zxAnEponDot3OamVariableResponseRxCurrent = _ZxAnEponDot3OamVariableResponseRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 12),
    _ZxAnEponDot3OamVariableResponseRxCurrent_Type()
)
zxAnEponDot3OamVariableResponseRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableResponseRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamVariableResponseRxCurrent.setUnits("frames")
_ZxAnEponDot3OamOrgSpecificTxCurrent_Type = Counter32
_ZxAnEponDot3OamOrgSpecificTxCurrent_Object = MibTableColumn
zxAnEponDot3OamOrgSpecificTxCurrent = _ZxAnEponDot3OamOrgSpecificTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 13),
    _ZxAnEponDot3OamOrgSpecificTxCurrent_Type()
)
zxAnEponDot3OamOrgSpecificTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamOrgSpecificTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamOrgSpecificTxCurrent.setUnits("frames")
_ZxAnEponDot3OamOrgSpecificRxCurrent_Type = Counter32
_ZxAnEponDot3OamOrgSpecificRxCurrent_Object = MibTableColumn
zxAnEponDot3OamOrgSpecificRxCurrent = _ZxAnEponDot3OamOrgSpecificRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 14),
    _ZxAnEponDot3OamOrgSpecificRxCurrent_Type()
)
zxAnEponDot3OamOrgSpecificRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamOrgSpecificRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamOrgSpecificRxCurrent.setUnits("frames")
_ZxAnEponDot3OamUnsupportedCodesTxCurrent_Type = Counter32
_ZxAnEponDot3OamUnsupportedCodesTxCurrent_Object = MibTableColumn
zxAnEponDot3OamUnsupportedCodesTxCurrent = _ZxAnEponDot3OamUnsupportedCodesTxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 15),
    _ZxAnEponDot3OamUnsupportedCodesTxCurrent_Type()
)
zxAnEponDot3OamUnsupportedCodesTxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUnsupportedCodesTxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUnsupportedCodesTxCurrent.setUnits("frames")
_ZxAnEponDot3OamUnsupportedCodesRxCurrent_Type = Counter32
_ZxAnEponDot3OamUnsupportedCodesRxCurrent_Object = MibTableColumn
zxAnEponDot3OamUnsupportedCodesRxCurrent = _ZxAnEponDot3OamUnsupportedCodesRxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 16),
    _ZxAnEponDot3OamUnsupportedCodesRxCurrent_Type()
)
zxAnEponDot3OamUnsupportedCodesRxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUnsupportedCodesRxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamUnsupportedCodesRxCurrent.setUnits("frames")
_ZxAnEponDot3OamFramesLostDueToOamCurrent_Type = Counter32
_ZxAnEponDot3OamFramesLostDueToOamCurrent_Object = MibTableColumn
zxAnEponDot3OamFramesLostDueToOamCurrent = _ZxAnEponDot3OamFramesLostDueToOamCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 5, 1, 17),
    _ZxAnEponDot3OamFramesLostDueToOamCurrent_Type()
)
zxAnEponDot3OamFramesLostDueToOamCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OamFramesLostDueToOamCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponDot3OamFramesLostDueToOamCurrent.setUnits("frames")
_ZxAnEponOltVirtualIfBERStatisticCurrentTable_Object = MibTable
zxAnEponOltVirtualIfBERStatisticCurrentTable = _ZxAnEponOltVirtualIfBERStatisticCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticCurrentTable.setStatus("current")
_ZxAnEponOltVirtualIfBERStatisticCurrentEntry_Object = MibTableRow
zxAnEponOltVirtualIfBERStatisticCurrentEntry = _ZxAnEponOltVirtualIfBERStatisticCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 6, 1)
)
zxAnEponOltVirtualIfBERStatisticCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticCurrentEntry.setStatus("current")
_ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Type = Counter32
_ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Object = MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuBERCurrent = _ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 6, 1, 1),
    _ZxAnEponOltVirtualIfBERStatisticOnuBERCurrent_Type()
)
zxAnEponOltVirtualIfBERStatisticOnuBERCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticOnuBERCurrent.setStatus("current")
_ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Type = Counter32
_ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Object = MibTableColumn
zxAnEponOltVirtualIfBERStatisticOnuFERCurrent = _ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 6, 1, 2),
    _ZxAnEponOltVirtualIfBERStatisticOnuFERCurrent_Type()
)
zxAnEponOltVirtualIfBERStatisticOnuFERCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticOnuFERCurrent.setStatus("current")
_ZxAnEponOltPhyPortStatisticCurrentTable_Object = MibTable
zxAnEponOltPhyPortStatisticCurrentTable = _ZxAnEponOltPhyPortStatisticCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 7)
)
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticCurrentTable.setStatus("current")
_ZxAnEponOltPhyPortStatisticCurrentEntry_Object = MibTableRow
zxAnEponOltPhyPortStatisticCurrentEntry = _ZxAnEponOltPhyPortStatisticCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 7, 1)
)
zxAnEponOltPhyPortStatisticCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticCurrentEntry.setStatus("current")
_ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Type = Counter32
_ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Object = MibTableColumn
zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent = _ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 7, 1, 1),
    _ZxAnEponOltPhyPortStatisticOltPonAverageBERCurrent_Type()
)
zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent.setStatus("current")
_ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Type = Counter32
_ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Object = MibTableColumn
zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent = _ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 7, 1, 2),
    _ZxAnEponOltPhyPortStatisticOltSysAverageBERCurrent_Type()
)
zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent.setStatus("current")
_ZxAnEponEtherStatsCurrentTable_Object = MibTable
zxAnEponEtherStatsCurrentTable = _ZxAnEponEtherStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8)
)
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCurrentTable.setStatus("current")
_ZxAnEponEtherStatsCurrentEntry_Object = MibTableRow
zxAnEponEtherStatsCurrentEntry = _ZxAnEponEtherStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1)
)
zxAnEponEtherStatsCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCurrentEntry.setStatus("current")
_ZxAnEponEtherStatsDropEventsCurrent_Type = Counter32
_ZxAnEponEtherStatsDropEventsCurrent_Object = MibTableColumn
zxAnEponEtherStatsDropEventsCurrent = _ZxAnEponEtherStatsDropEventsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 1),
    _ZxAnEponEtherStatsDropEventsCurrent_Type()
)
zxAnEponEtherStatsDropEventsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsDropEventsCurrent.setStatus("current")
_ZxAnEponEtherStatsOctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsOctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsOctetsCurrent = _ZxAnEponEtherStatsOctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 2),
    _ZxAnEponEtherStatsOctetsCurrent_Type()
)
zxAnEponEtherStatsOctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsPktsCurrent_Type = Counter32
_ZxAnEponEtherStatsPktsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPktsCurrent = _ZxAnEponEtherStatsPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 3),
    _ZxAnEponEtherStatsPktsCurrent_Type()
)
zxAnEponEtherStatsPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPktsCurrent.setStatus("current")
_ZxAnEponEtherStatsBroadcastPktsCurrent_Type = Counter32
_ZxAnEponEtherStatsBroadcastPktsCurrent_Object = MibTableColumn
zxAnEponEtherStatsBroadcastPktsCurrent = _ZxAnEponEtherStatsBroadcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 4),
    _ZxAnEponEtherStatsBroadcastPktsCurrent_Type()
)
zxAnEponEtherStatsBroadcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsBroadcastPktsCurrent.setStatus("current")
_ZxAnEponEtherStatsMulticastPktsCurrent_Type = Counter32
_ZxAnEponEtherStatsMulticastPktsCurrent_Object = MibTableColumn
zxAnEponEtherStatsMulticastPktsCurrent = _ZxAnEponEtherStatsMulticastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 5),
    _ZxAnEponEtherStatsMulticastPktsCurrent_Type()
)
zxAnEponEtherStatsMulticastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsMulticastPktsCurrent.setStatus("current")
_ZxAnEponEtherStatsCRCAlignErrorsCurrent_Type = Counter32
_ZxAnEponEtherStatsCRCAlignErrorsCurrent_Object = MibTableColumn
zxAnEponEtherStatsCRCAlignErrorsCurrent = _ZxAnEponEtherStatsCRCAlignErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 6),
    _ZxAnEponEtherStatsCRCAlignErrorsCurrent_Type()
)
zxAnEponEtherStatsCRCAlignErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCRCAlignErrorsCurrent.setStatus("current")
_ZxAnEponEtherStatsUndersizePktsCurrent_Type = Counter32
_ZxAnEponEtherStatsUndersizePktsCurrent_Object = MibTableColumn
zxAnEponEtherStatsUndersizePktsCurrent = _ZxAnEponEtherStatsUndersizePktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 7),
    _ZxAnEponEtherStatsUndersizePktsCurrent_Type()
)
zxAnEponEtherStatsUndersizePktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsUndersizePktsCurrent.setStatus("current")
_ZxAnEponEtherStatsOversizePktsCurrent_Type = Counter32
_ZxAnEponEtherStatsOversizePktsCurrent_Object = MibTableColumn
zxAnEponEtherStatsOversizePktsCurrent = _ZxAnEponEtherStatsOversizePktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 8),
    _ZxAnEponEtherStatsOversizePktsCurrent_Type()
)
zxAnEponEtherStatsOversizePktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOversizePktsCurrent.setStatus("current")
_ZxAnEponEtherStatsFragmentsCurrent_Type = Counter32
_ZxAnEponEtherStatsFragmentsCurrent_Object = MibTableColumn
zxAnEponEtherStatsFragmentsCurrent = _ZxAnEponEtherStatsFragmentsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 9),
    _ZxAnEponEtherStatsFragmentsCurrent_Type()
)
zxAnEponEtherStatsFragmentsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsFragmentsCurrent.setStatus("current")
_ZxAnEponEtherStatsJabbersCurrent_Type = Counter32
_ZxAnEponEtherStatsJabbersCurrent_Object = MibTableColumn
zxAnEponEtherStatsJabbersCurrent = _ZxAnEponEtherStatsJabbersCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 10),
    _ZxAnEponEtherStatsJabbersCurrent_Type()
)
zxAnEponEtherStatsJabbersCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsJabbersCurrent.setStatus("current")
_ZxAnEponEtherStatsCollisionsCurrent_Type = Counter32
_ZxAnEponEtherStatsCollisionsCurrent_Object = MibTableColumn
zxAnEponEtherStatsCollisionsCurrent = _ZxAnEponEtherStatsCollisionsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 11),
    _ZxAnEponEtherStatsCollisionsCurrent_Type()
)
zxAnEponEtherStatsCollisionsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCollisionsCurrent.setStatus("current")
_ZxAnEponEtherStatsPkts64OctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsPkts64OctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPkts64OctetsCurrent = _ZxAnEponEtherStatsPkts64OctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 12),
    _ZxAnEponEtherStatsPkts64OctetsCurrent_Type()
)
zxAnEponEtherStatsPkts64OctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts64OctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsPkts65to127OctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsPkts65to127OctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPkts65to127OctetsCurrent = _ZxAnEponEtherStatsPkts65to127OctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 13),
    _ZxAnEponEtherStatsPkts65to127OctetsCurrent_Type()
)
zxAnEponEtherStatsPkts65to127OctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts65to127OctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsPkts128to255OctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsPkts128to255OctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPkts128to255OctetsCurrent = _ZxAnEponEtherStatsPkts128to255OctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 14),
    _ZxAnEponEtherStatsPkts128to255OctetsCurrent_Type()
)
zxAnEponEtherStatsPkts128to255OctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts128to255OctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsPkts256to511OctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsPkts256to511OctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPkts256to511OctetsCurrent = _ZxAnEponEtherStatsPkts256to511OctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 15),
    _ZxAnEponEtherStatsPkts256to511OctetsCurrent_Type()
)
zxAnEponEtherStatsPkts256to511OctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts256to511OctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPkts512to1023OctetsCurrent = _ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 16),
    _ZxAnEponEtherStatsPkts512to1023OctetsCurrent_Type()
)
zxAnEponEtherStatsPkts512to1023OctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts512to1023OctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Type = Counter32
_ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Object = MibTableColumn
zxAnEponEtherStatsPkts1024to1518OctetsCurrent = _ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 17),
    _ZxAnEponEtherStatsPkts1024to1518OctetsCurrent_Type()
)
zxAnEponEtherStatsPkts1024to1518OctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts1024to1518OctetsCurrent.setStatus("current")
_ZxAnEponEtherStatsOwnerCurrent_Type = OwnerString
_ZxAnEponEtherStatsOwnerCurrent_Object = MibTableColumn
zxAnEponEtherStatsOwnerCurrent = _ZxAnEponEtherStatsOwnerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 18),
    _ZxAnEponEtherStatsOwnerCurrent_Type()
)
zxAnEponEtherStatsOwnerCurrent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOwnerCurrent.setStatus("current")
_ZxAnEponEtherStatsStatusCurrent_Type = EntryStatus
_ZxAnEponEtherStatsStatusCurrent_Object = MibTableColumn
zxAnEponEtherStatsStatusCurrent = _ZxAnEponEtherStatsStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 8, 1, 19),
    _ZxAnEponEtherStatsStatusCurrent_Type()
)
zxAnEponEtherStatsStatusCurrent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsStatusCurrent.setStatus("current")
_ZxAnEponIfCurrentTable_Object = MibTable
zxAnEponIfCurrentTable = _ZxAnEponIfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9)
)
if mibBuilder.loadTexts:
    zxAnEponIfCurrentTable.setStatus("current")
_ZxAnEponIfCurrentEntry_Object = MibTableRow
zxAnEponIfCurrentEntry = _ZxAnEponIfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1)
)
zxAnEponIfCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponIfCurrentEntry.setStatus("current")
_ZxAnEponIfInOctetsCurrent_Type = Counter32
_ZxAnEponIfInOctetsCurrent_Object = MibTableColumn
zxAnEponIfInOctetsCurrent = _ZxAnEponIfInOctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 1),
    _ZxAnEponIfInOctetsCurrent_Type()
)
zxAnEponIfInOctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInOctetsCurrent.setStatus("current")
_ZxAnEponIfInUcastPktsCurrent_Type = Counter32
_ZxAnEponIfInUcastPktsCurrent_Object = MibTableColumn
zxAnEponIfInUcastPktsCurrent = _ZxAnEponIfInUcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 2),
    _ZxAnEponIfInUcastPktsCurrent_Type()
)
zxAnEponIfInUcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInUcastPktsCurrent.setStatus("current")
_ZxAnEponIfInNUcastPktsCurrent_Type = Counter32
_ZxAnEponIfInNUcastPktsCurrent_Object = MibTableColumn
zxAnEponIfInNUcastPktsCurrent = _ZxAnEponIfInNUcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 3),
    _ZxAnEponIfInNUcastPktsCurrent_Type()
)
zxAnEponIfInNUcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInNUcastPktsCurrent.setStatus("deprecated")
_ZxAnEponIfInDiscardsCurrent_Type = Counter32
_ZxAnEponIfInDiscardsCurrent_Object = MibTableColumn
zxAnEponIfInDiscardsCurrent = _ZxAnEponIfInDiscardsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 4),
    _ZxAnEponIfInDiscardsCurrent_Type()
)
zxAnEponIfInDiscardsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInDiscardsCurrent.setStatus("current")
_ZxAnEponIfInErrorsCurrent_Type = Counter32
_ZxAnEponIfInErrorsCurrent_Object = MibTableColumn
zxAnEponIfInErrorsCurrent = _ZxAnEponIfInErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 5),
    _ZxAnEponIfInErrorsCurrent_Type()
)
zxAnEponIfInErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInErrorsCurrent.setStatus("current")
_ZxAnEponIfInUnknownProtosCurrent_Type = Counter32
_ZxAnEponIfInUnknownProtosCurrent_Object = MibTableColumn
zxAnEponIfInUnknownProtosCurrent = _ZxAnEponIfInUnknownProtosCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 6),
    _ZxAnEponIfInUnknownProtosCurrent_Type()
)
zxAnEponIfInUnknownProtosCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInUnknownProtosCurrent.setStatus("current")
_ZxAnEponIfOutOctetsCurrent_Type = Counter32
_ZxAnEponIfOutOctetsCurrent_Object = MibTableColumn
zxAnEponIfOutOctetsCurrent = _ZxAnEponIfOutOctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 7),
    _ZxAnEponIfOutOctetsCurrent_Type()
)
zxAnEponIfOutOctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutOctetsCurrent.setStatus("current")
_ZxAnEponIfOutUcastPktsCurrent_Type = Counter32
_ZxAnEponIfOutUcastPktsCurrent_Object = MibTableColumn
zxAnEponIfOutUcastPktsCurrent = _ZxAnEponIfOutUcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 8),
    _ZxAnEponIfOutUcastPktsCurrent_Type()
)
zxAnEponIfOutUcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutUcastPktsCurrent.setStatus("current")
_ZxAnEponIfOutNUcastPktsCurrent_Type = Counter32
_ZxAnEponIfOutNUcastPktsCurrent_Object = MibTableColumn
zxAnEponIfOutNUcastPktsCurrent = _ZxAnEponIfOutNUcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 9),
    _ZxAnEponIfOutNUcastPktsCurrent_Type()
)
zxAnEponIfOutNUcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutNUcastPktsCurrent.setStatus("deprecated")
_ZxAnEponIfOutDiscardsCurrent_Type = Counter32
_ZxAnEponIfOutDiscardsCurrent_Object = MibTableColumn
zxAnEponIfOutDiscardsCurrent = _ZxAnEponIfOutDiscardsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 10),
    _ZxAnEponIfOutDiscardsCurrent_Type()
)
zxAnEponIfOutDiscardsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutDiscardsCurrent.setStatus("current")
_ZxAnEponIfOutErrorsCurrent_Type = Counter32
_ZxAnEponIfOutErrorsCurrent_Object = MibTableColumn
zxAnEponIfOutErrorsCurrent = _ZxAnEponIfOutErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 9, 1, 11),
    _ZxAnEponIfOutErrorsCurrent_Type()
)
zxAnEponIfOutErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutErrorsCurrent.setStatus("current")
_ZxAnEponIfXCurrentTable_Object = MibTable
zxAnEponIfXCurrentTable = _ZxAnEponIfXCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10)
)
if mibBuilder.loadTexts:
    zxAnEponIfXCurrentTable.setStatus("current")
_ZxAnEponIfXCurrentEntry_Object = MibTableRow
zxAnEponIfXCurrentEntry = _ZxAnEponIfXCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1)
)
if mibBuilder.loadTexts:
    zxAnEponIfXCurrentEntry.setStatus("current")
_ZxAnEponIfInMulticastPktsCurrent_Type = Counter32
_ZxAnEponIfInMulticastPktsCurrent_Object = MibTableColumn
zxAnEponIfInMulticastPktsCurrent = _ZxAnEponIfInMulticastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 1),
    _ZxAnEponIfInMulticastPktsCurrent_Type()
)
zxAnEponIfInMulticastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInMulticastPktsCurrent.setStatus("current")
_ZxAnEponIfInBroadcastPktsCurrent_Type = Counter32
_ZxAnEponIfInBroadcastPktsCurrent_Object = MibTableColumn
zxAnEponIfInBroadcastPktsCurrent = _ZxAnEponIfInBroadcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 2),
    _ZxAnEponIfInBroadcastPktsCurrent_Type()
)
zxAnEponIfInBroadcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInBroadcastPktsCurrent.setStatus("current")
_ZxAnEponIfOutMulticastPktsCurrent_Type = Counter32
_ZxAnEponIfOutMulticastPktsCurrent_Object = MibTableColumn
zxAnEponIfOutMulticastPktsCurrent = _ZxAnEponIfOutMulticastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 3),
    _ZxAnEponIfOutMulticastPktsCurrent_Type()
)
zxAnEponIfOutMulticastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutMulticastPktsCurrent.setStatus("current")
_ZxAnEponIfOutBroadcastPktsCurrent_Type = Counter32
_ZxAnEponIfOutBroadcastPktsCurrent_Object = MibTableColumn
zxAnEponIfOutBroadcastPktsCurrent = _ZxAnEponIfOutBroadcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 4),
    _ZxAnEponIfOutBroadcastPktsCurrent_Type()
)
zxAnEponIfOutBroadcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutBroadcastPktsCurrent.setStatus("current")
_ZxAnEponIfHCInOctetsCurrent_Type = Counter64
_ZxAnEponIfHCInOctetsCurrent_Object = MibTableColumn
zxAnEponIfHCInOctetsCurrent = _ZxAnEponIfHCInOctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 5),
    _ZxAnEponIfHCInOctetsCurrent_Type()
)
zxAnEponIfHCInOctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInOctetsCurrent.setStatus("current")
_ZxAnEponIfHCInUcastPktsCurrent_Type = Counter64
_ZxAnEponIfHCInUcastPktsCurrent_Object = MibTableColumn
zxAnEponIfHCInUcastPktsCurrent = _ZxAnEponIfHCInUcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 6),
    _ZxAnEponIfHCInUcastPktsCurrent_Type()
)
zxAnEponIfHCInUcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInUcastPktsCurrent.setStatus("current")
_ZxAnEponIfHCInMulticastPktsCurrent_Type = Counter64
_ZxAnEponIfHCInMulticastPktsCurrent_Object = MibTableColumn
zxAnEponIfHCInMulticastPktsCurrent = _ZxAnEponIfHCInMulticastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 7),
    _ZxAnEponIfHCInMulticastPktsCurrent_Type()
)
zxAnEponIfHCInMulticastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInMulticastPktsCurrent.setStatus("current")
_ZxAnEponIfHCInBroadcastPktsCurrent_Type = Counter64
_ZxAnEponIfHCInBroadcastPktsCurrent_Object = MibTableColumn
zxAnEponIfHCInBroadcastPktsCurrent = _ZxAnEponIfHCInBroadcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 8),
    _ZxAnEponIfHCInBroadcastPktsCurrent_Type()
)
zxAnEponIfHCInBroadcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInBroadcastPktsCurrent.setStatus("current")
_ZxAnEponIfHCOutOctetsCurrent_Type = Counter64
_ZxAnEponIfHCOutOctetsCurrent_Object = MibTableColumn
zxAnEponIfHCOutOctetsCurrent = _ZxAnEponIfHCOutOctetsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 9),
    _ZxAnEponIfHCOutOctetsCurrent_Type()
)
zxAnEponIfHCOutOctetsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutOctetsCurrent.setStatus("current")
_ZxAnEponIfHCOutUcastPktsCurrent_Type = Counter64
_ZxAnEponIfHCOutUcastPktsCurrent_Object = MibTableColumn
zxAnEponIfHCOutUcastPktsCurrent = _ZxAnEponIfHCOutUcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 10),
    _ZxAnEponIfHCOutUcastPktsCurrent_Type()
)
zxAnEponIfHCOutUcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutUcastPktsCurrent.setStatus("current")
_ZxAnEponIfHCOutMulticastPktsCurrent_Type = Counter64
_ZxAnEponIfHCOutMulticastPktsCurrent_Object = MibTableColumn
zxAnEponIfHCOutMulticastPktsCurrent = _ZxAnEponIfHCOutMulticastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 11),
    _ZxAnEponIfHCOutMulticastPktsCurrent_Type()
)
zxAnEponIfHCOutMulticastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutMulticastPktsCurrent.setStatus("current")
_ZxAnEponIfHCOutBroadcastPktsCurrent_Type = Counter64
_ZxAnEponIfHCOutBroadcastPktsCurrent_Object = MibTableColumn
zxAnEponIfHCOutBroadcastPktsCurrent = _ZxAnEponIfHCOutBroadcastPktsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 10, 1, 12),
    _ZxAnEponIfHCOutBroadcastPktsCurrent_Type()
)
zxAnEponIfHCOutBroadcastPktsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutBroadcastPktsCurrent.setStatus("current")
_ZxAnEponDot3PauseCurrentTable_Object = MibTable
zxAnEponDot3PauseCurrentTable = _ZxAnEponDot3PauseCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 11)
)
if mibBuilder.loadTexts:
    zxAnEponDot3PauseCurrentTable.setStatus("current")
_ZxAnEponDot3PauseCurrentEntry_Object = MibTableRow
zxAnEponDot3PauseCurrentEntry = _ZxAnEponDot3PauseCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 11, 1)
)
zxAnEponDot3PauseCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3PauseCurrentEntry.setStatus("current")
_ZxAnEponDot3InPauseFramesCurrent_Type = Counter32
_ZxAnEponDot3InPauseFramesCurrent_Object = MibTableColumn
zxAnEponDot3InPauseFramesCurrent = _ZxAnEponDot3InPauseFramesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 11, 1, 1),
    _ZxAnEponDot3InPauseFramesCurrent_Type()
)
zxAnEponDot3InPauseFramesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3InPauseFramesCurrent.setStatus("current")
_ZxAnEponDot3OutPauseFramesCurrent_Type = Counter32
_ZxAnEponDot3OutPauseFramesCurrent_Object = MibTableColumn
zxAnEponDot3OutPauseFramesCurrent = _ZxAnEponDot3OutPauseFramesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 11, 1, 2),
    _ZxAnEponDot3OutPauseFramesCurrent_Type()
)
zxAnEponDot3OutPauseFramesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3OutPauseFramesCurrent.setStatus("current")
_ZxAnEponDot3HCInPauseFramesCurrent_Type = Counter64
_ZxAnEponDot3HCInPauseFramesCurrent_Object = MibTableColumn
zxAnEponDot3HCInPauseFramesCurrent = _ZxAnEponDot3HCInPauseFramesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 11, 1, 3),
    _ZxAnEponDot3HCInPauseFramesCurrent_Type()
)
zxAnEponDot3HCInPauseFramesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCInPauseFramesCurrent.setStatus("current")
_ZxAnEponDot3HCOutPauseFramesCurrent_Type = Counter64
_ZxAnEponDot3HCOutPauseFramesCurrent_Object = MibTableColumn
zxAnEponDot3HCOutPauseFramesCurrent = _ZxAnEponDot3HCOutPauseFramesCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 11, 1, 4),
    _ZxAnEponDot3HCOutPauseFramesCurrent_Type()
)
zxAnEponDot3HCOutPauseFramesCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCOutPauseFramesCurrent.setStatus("current")
_ZxAnEponDot3HCStatsCurrentTable_Object = MibTable
zxAnEponDot3HCStatsCurrentTable = _ZxAnEponDot3HCStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12)
)
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsCurrentTable.setStatus("current")
_ZxAnEponDot3HCStatsCurrentEntry_Object = MibTableRow
zxAnEponDot3HCStatsCurrentEntry = _ZxAnEponDot3HCStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1)
)
zxAnEponDot3HCStatsCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsCurrentEntry.setStatus("current")
_ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Type = Counter64
_ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Object = MibTableColumn
zxAnEponDot3HCStatsAlignmentErrorsCurrent = _ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1, 1),
    _ZxAnEponDot3HCStatsAlignmentErrorsCurrent_Type()
)
zxAnEponDot3HCStatsAlignmentErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsAlignmentErrorsCurrent.setStatus("current")
_ZxAnEponDot3HCStatsFCSErrorsCurrent_Type = Counter64
_ZxAnEponDot3HCStatsFCSErrorsCurrent_Object = MibTableColumn
zxAnEponDot3HCStatsFCSErrorsCurrent = _ZxAnEponDot3HCStatsFCSErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1, 2),
    _ZxAnEponDot3HCStatsFCSErrorsCurrent_Type()
)
zxAnEponDot3HCStatsFCSErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsFCSErrorsCurrent.setStatus("current")
_ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Type = Counter64
_ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Object = MibTableColumn
zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent = _ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1, 3),
    _ZxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent_Type()
)
zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent.setStatus("current")
_ZxAnEponDot3HCStatsFrameTooLongsCurrent_Type = Counter64
_ZxAnEponDot3HCStatsFrameTooLongsCurrent_Object = MibTableColumn
zxAnEponDot3HCStatsFrameTooLongsCurrent = _ZxAnEponDot3HCStatsFrameTooLongsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1, 4),
    _ZxAnEponDot3HCStatsFrameTooLongsCurrent_Type()
)
zxAnEponDot3HCStatsFrameTooLongsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsFrameTooLongsCurrent.setStatus("current")
_ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Type = Counter64
_ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Object = MibTableColumn
zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent = _ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1, 5),
    _ZxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent_Type()
)
zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent.setStatus("current")
_ZxAnEponDot3HCStatsSymbolErrorsCurrent_Type = Counter64
_ZxAnEponDot3HCStatsSymbolErrorsCurrent_Object = MibTableColumn
zxAnEponDot3HCStatsSymbolErrorsCurrent = _ZxAnEponDot3HCStatsSymbolErrorsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 12, 1, 6),
    _ZxAnEponDot3HCStatsSymbolErrorsCurrent_Type()
)
zxAnEponDot3HCStatsSymbolErrorsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponDot3HCStatsSymbolErrorsCurrent.setStatus("current")
_ZxAnEponOnuLlidStatTable_Object = MibTable
zxAnEponOnuLlidStatTable = _ZxAnEponOnuLlidStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13)
)
if mibBuilder.loadTexts:
    zxAnEponOnuLlidStatTable.setStatus("current")
_ZxAnEponOnuLlidStatEntry_Object = MibTableRow
zxAnEponOnuLlidStatEntry = _ZxAnEponOnuLlidStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1)
)
zxAnEponOnuLlidStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuLlid"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuLlidStatEntry.setStatus("current")
_ZxAnEponOnuLlidRxFrames_Type = Counter64
_ZxAnEponOnuLlidRxFrames_Object = MibTableColumn
zxAnEponOnuLlidRxFrames = _ZxAnEponOnuLlidRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 1),
    _ZxAnEponOnuLlidRxFrames_Type()
)
zxAnEponOnuLlidRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidRxFrames.setStatus("current")
_ZxAnEponOnuLlidRxOctets_Type = Counter64
_ZxAnEponOnuLlidRxOctets_Object = MibTableColumn
zxAnEponOnuLlidRxOctets = _ZxAnEponOnuLlidRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 2),
    _ZxAnEponOnuLlidRxOctets_Type()
)
zxAnEponOnuLlidRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidRxOctets.setStatus("current")
_ZxAnEponOnuLlidRxMulticastFrames_Type = Counter64
_ZxAnEponOnuLlidRxMulticastFrames_Object = MibTableColumn
zxAnEponOnuLlidRxMulticastFrames = _ZxAnEponOnuLlidRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 3),
    _ZxAnEponOnuLlidRxMulticastFrames_Type()
)
zxAnEponOnuLlidRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidRxMulticastFrames.setStatus("current")
_ZxAnEponOnuLlidRxBroadcastFrames_Type = Counter64
_ZxAnEponOnuLlidRxBroadcastFrames_Object = MibTableColumn
zxAnEponOnuLlidRxBroadcastFrames = _ZxAnEponOnuLlidRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 4),
    _ZxAnEponOnuLlidRxBroadcastFrames_Type()
)
zxAnEponOnuLlidRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidRxBroadcastFrames.setStatus("current")
_ZxAnEponOnuLlidTxFrames_Type = Counter64
_ZxAnEponOnuLlidTxFrames_Object = MibTableColumn
zxAnEponOnuLlidTxFrames = _ZxAnEponOnuLlidTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 5),
    _ZxAnEponOnuLlidTxFrames_Type()
)
zxAnEponOnuLlidTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidTxFrames.setStatus("current")
_ZxAnEponOnuLlidTxOctets_Type = Counter64
_ZxAnEponOnuLlidTxOctets_Object = MibTableColumn
zxAnEponOnuLlidTxOctets = _ZxAnEponOnuLlidTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 6),
    _ZxAnEponOnuLlidTxOctets_Type()
)
zxAnEponOnuLlidTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidTxOctets.setStatus("current")
_ZxAnEponOnuLlidTxMulticastFrames_Type = Counter64
_ZxAnEponOnuLlidTxMulticastFrames_Object = MibTableColumn
zxAnEponOnuLlidTxMulticastFrames = _ZxAnEponOnuLlidTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 7),
    _ZxAnEponOnuLlidTxMulticastFrames_Type()
)
zxAnEponOnuLlidTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidTxMulticastFrames.setStatus("current")
_ZxAnEponOnuLlidTxBroadcastFrames_Type = Counter64
_ZxAnEponOnuLlidTxBroadcastFrames_Object = MibTableColumn
zxAnEponOnuLlidTxBroadcastFrames = _ZxAnEponOnuLlidTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 8),
    _ZxAnEponOnuLlidTxBroadcastFrames_Type()
)
zxAnEponOnuLlidTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidTxBroadcastFrames.setStatus("current")
_ZxAnEponOnuLlidCrcErrors_Type = Counter64
_ZxAnEponOnuLlidCrcErrors_Object = MibTableColumn
zxAnEponOnuLlidCrcErrors = _ZxAnEponOnuLlidCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 9),
    _ZxAnEponOnuLlidCrcErrors_Type()
)
zxAnEponOnuLlidCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidCrcErrors.setStatus("current")
_ZxAnEponOnuLlidFecCrctedBlocks_Type = Counter64
_ZxAnEponOnuLlidFecCrctedBlocks_Object = MibTableColumn
zxAnEponOnuLlidFecCrctedBlocks = _ZxAnEponOnuLlidFecCrctedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 10),
    _ZxAnEponOnuLlidFecCrctedBlocks_Type()
)
zxAnEponOnuLlidFecCrctedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidFecCrctedBlocks.setStatus("current")
_ZxAnEponOnuLlidFecUncrctedBlocks_Type = Counter64
_ZxAnEponOnuLlidFecUncrctedBlocks_Object = MibTableColumn
zxAnEponOnuLlidFecUncrctedBlocks = _ZxAnEponOnuLlidFecUncrctedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 11),
    _ZxAnEponOnuLlidFecUncrctedBlocks_Type()
)
zxAnEponOnuLlidFecUncrctedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidFecUncrctedBlocks.setStatus("current")
_ZxAnEponOnuLlidMpcpRxGateFrames_Type = Counter64
_ZxAnEponOnuLlidMpcpRxGateFrames_Object = MibTableColumn
zxAnEponOnuLlidMpcpRxGateFrames = _ZxAnEponOnuLlidMpcpRxGateFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 12),
    _ZxAnEponOnuLlidMpcpRxGateFrames_Type()
)
zxAnEponOnuLlidMpcpRxGateFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidMpcpRxGateFrames.setStatus("current")
_ZxAnEponOnuLlidMpcpRxCtrlFrames_Type = Counter64
_ZxAnEponOnuLlidMpcpRxCtrlFrames_Object = MibTableColumn
zxAnEponOnuLlidMpcpRxCtrlFrames = _ZxAnEponOnuLlidMpcpRxCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 13),
    _ZxAnEponOnuLlidMpcpRxCtrlFrames_Type()
)
zxAnEponOnuLlidMpcpRxCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidMpcpRxCtrlFrames.setStatus("current")
_ZxAnEponOnuLlidMpcpRxRegFrames_Type = Counter64
_ZxAnEponOnuLlidMpcpRxRegFrames_Object = MibTableColumn
zxAnEponOnuLlidMpcpRxRegFrames = _ZxAnEponOnuLlidMpcpRxRegFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 14),
    _ZxAnEponOnuLlidMpcpRxRegFrames_Type()
)
zxAnEponOnuLlidMpcpRxRegFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidMpcpRxRegFrames.setStatus("current")
_ZxAnEponOnuLlidMpcpTxCtrlFrames_Type = Counter64
_ZxAnEponOnuLlidMpcpTxCtrlFrames_Object = MibTableColumn
zxAnEponOnuLlidMpcpTxCtrlFrames = _ZxAnEponOnuLlidMpcpTxCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 15),
    _ZxAnEponOnuLlidMpcpTxCtrlFrames_Type()
)
zxAnEponOnuLlidMpcpTxCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidMpcpTxCtrlFrames.setStatus("current")
_ZxAnEponOnuLlidMpcpTxReqFrames_Type = Counter64
_ZxAnEponOnuLlidMpcpTxReqFrames_Object = MibTableColumn
zxAnEponOnuLlidMpcpTxReqFrames = _ZxAnEponOnuLlidMpcpTxReqFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 16),
    _ZxAnEponOnuLlidMpcpTxReqFrames_Type()
)
zxAnEponOnuLlidMpcpTxReqFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidMpcpTxReqFrames.setStatus("current")
_ZxAnEponOnuLlidMpcpTxRepFrames_Type = Counter64
_ZxAnEponOnuLlidMpcpTxRepFrames_Object = MibTableColumn
zxAnEponOnuLlidMpcpTxRepFrames = _ZxAnEponOnuLlidMpcpTxRepFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 2, 13, 1, 17),
    _ZxAnEponOnuLlidMpcpTxRepFrames_Type()
)
zxAnEponOnuLlidMpcpTxRepFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidMpcpTxRepFrames.setStatus("current")
_ZxAnEponPmHistory_ObjectIdentity = ObjectIdentity
zxAnEponPmHistory = _ZxAnEponPmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3)
)
_ZxAnEponOltVirtualIfBERStatisticHistoryTable_Object = MibTable
zxAnEponOltVirtualIfBERStatisticHistoryTable = _ZxAnEponOltVirtualIfBERStatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticHistoryTable.setStatus("current")
_ZxAnEponOltVirtualIfBERStatisticHistoryEntry_Object = MibTableRow
zxAnEponOltVirtualIfBERStatisticHistoryEntry = _ZxAnEponOltVirtualIfBERStatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 1, 1)
)
zxAnEponOltVirtualIfBERStatisticHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticHistoryEntry.setStatus("current")


class _ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Type(OctetString):
    """Custom type zxAnEponOltVirtualIfBERStatisticHistoryOnuBER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Type.__name__ = "OctetString"
_ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Object = MibTableColumn
zxAnEponOltVirtualIfBERStatisticHistoryOnuBER = _ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 1, 1, 1),
    _ZxAnEponOltVirtualIfBERStatisticHistoryOnuBER_Type()
)
zxAnEponOltVirtualIfBERStatisticHistoryOnuBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticHistoryOnuBER.setStatus("current")


class _ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Type(OctetString):
    """Custom type zxAnEponOltVirtualIfBERStatisticHistoryOnuFER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Type.__name__ = "OctetString"
_ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Object = MibTableColumn
zxAnEponOltVirtualIfBERStatisticHistoryOnuFER = _ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 1, 1, 2),
    _ZxAnEponOltVirtualIfBERStatisticHistoryOnuFER_Type()
)
zxAnEponOltVirtualIfBERStatisticHistoryOnuFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltVirtualIfBERStatisticHistoryOnuFER.setStatus("current")
_ZxAnEponOltPhyPortStatisticHistoryTable_Object = MibTable
zxAnEponOltPhyPortStatisticHistoryTable = _ZxAnEponOltPhyPortStatisticHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticHistoryTable.setStatus("current")
_ZxAnEponOltPhyPortStatisticHistoryEntry_Object = MibTableRow
zxAnEponOltPhyPortStatisticHistoryEntry = _ZxAnEponOltPhyPortStatisticHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 2, 1)
)
zxAnEponOltPhyPortStatisticHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticHistoryEntry.setStatus("current")


class _ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Type(OctetString):
    """Custom type zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Type.__name__ = "OctetString"
_ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Object = MibTableColumn
zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER = _ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 2, 1, 1),
    _ZxAnEponOltPhyPortStatisticHistoryOltPonAverageBER_Type()
)
zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER.setStatus("current")


class _ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Type(OctetString):
    """Custom type zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Type.__name__ = "OctetString"
_ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Object = MibTableColumn
zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER = _ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 2, 1, 2),
    _ZxAnEponOltPhyPortStatisticHistoryOltSysAverageBER_Type()
)
zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER.setStatus("current")
_ZxAnEponEtherStatsHistoryTable_Object = MibTable
zxAnEponEtherStatsHistoryTable = _ZxAnEponEtherStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnEponEtherStatsHistoryTable.setStatus("current")
_ZxAnEponEtherStatsHistoryEntry_Object = MibTableRow
zxAnEponEtherStatsHistoryEntry = _ZxAnEponEtherStatsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1)
)
zxAnEponEtherStatsHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponEtherStatsHistoryEntry.setStatus("current")
_ZxAnEponEtherStatsDropEventsHistory_Type = Counter32
_ZxAnEponEtherStatsDropEventsHistory_Object = MibTableColumn
zxAnEponEtherStatsDropEventsHistory = _ZxAnEponEtherStatsDropEventsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 1),
    _ZxAnEponEtherStatsDropEventsHistory_Type()
)
zxAnEponEtherStatsDropEventsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsDropEventsHistory.setStatus("current")
_ZxAnEponEtherStatsOctetsHistory_Type = Counter32
_ZxAnEponEtherStatsOctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsOctetsHistory = _ZxAnEponEtherStatsOctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 2),
    _ZxAnEponEtherStatsOctetsHistory_Type()
)
zxAnEponEtherStatsOctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOctetsHistory.setStatus("current")
_ZxAnEponEtherStatsPktsHistory_Type = Counter32
_ZxAnEponEtherStatsPktsHistory_Object = MibTableColumn
zxAnEponEtherStatsPktsHistory = _ZxAnEponEtherStatsPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 3),
    _ZxAnEponEtherStatsPktsHistory_Type()
)
zxAnEponEtherStatsPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPktsHistory.setStatus("current")
_ZxAnEponEtherStatsBroadcastPktsHistory_Type = Counter32
_ZxAnEponEtherStatsBroadcastPktsHistory_Object = MibTableColumn
zxAnEponEtherStatsBroadcastPktsHistory = _ZxAnEponEtherStatsBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 4),
    _ZxAnEponEtherStatsBroadcastPktsHistory_Type()
)
zxAnEponEtherStatsBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsBroadcastPktsHistory.setStatus("current")
_ZxAnEponEtherStatsMulticastPktsHistory_Type = Counter32
_ZxAnEponEtherStatsMulticastPktsHistory_Object = MibTableColumn
zxAnEponEtherStatsMulticastPktsHistory = _ZxAnEponEtherStatsMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 5),
    _ZxAnEponEtherStatsMulticastPktsHistory_Type()
)
zxAnEponEtherStatsMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsMulticastPktsHistory.setStatus("current")
_ZxAnEponEtherStatsCRCAlignErrorsHistory_Type = Counter32
_ZxAnEponEtherStatsCRCAlignErrorsHistory_Object = MibTableColumn
zxAnEponEtherStatsCRCAlignErrorsHistory = _ZxAnEponEtherStatsCRCAlignErrorsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 6),
    _ZxAnEponEtherStatsCRCAlignErrorsHistory_Type()
)
zxAnEponEtherStatsCRCAlignErrorsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCRCAlignErrorsHistory.setStatus("current")
_ZxAnEponEtherStatsUndersizePktsHistory_Type = Counter32
_ZxAnEponEtherStatsUndersizePktsHistory_Object = MibTableColumn
zxAnEponEtherStatsUndersizePktsHistory = _ZxAnEponEtherStatsUndersizePktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 7),
    _ZxAnEponEtherStatsUndersizePktsHistory_Type()
)
zxAnEponEtherStatsUndersizePktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsUndersizePktsHistory.setStatus("current")
_ZxAnEponEtherStatsOversizePktsHistory_Type = Counter32
_ZxAnEponEtherStatsOversizePktsHistory_Object = MibTableColumn
zxAnEponEtherStatsOversizePktsHistory = _ZxAnEponEtherStatsOversizePktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 8),
    _ZxAnEponEtherStatsOversizePktsHistory_Type()
)
zxAnEponEtherStatsOversizePktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsOversizePktsHistory.setStatus("current")
_ZxAnEponEtherStatsFragmentsHistory_Type = Counter32
_ZxAnEponEtherStatsFragmentsHistory_Object = MibTableColumn
zxAnEponEtherStatsFragmentsHistory = _ZxAnEponEtherStatsFragmentsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 9),
    _ZxAnEponEtherStatsFragmentsHistory_Type()
)
zxAnEponEtherStatsFragmentsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsFragmentsHistory.setStatus("current")
_ZxAnEponEtherStatsJabbersHistory_Type = Counter32
_ZxAnEponEtherStatsJabbersHistory_Object = MibTableColumn
zxAnEponEtherStatsJabbersHistory = _ZxAnEponEtherStatsJabbersHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 10),
    _ZxAnEponEtherStatsJabbersHistory_Type()
)
zxAnEponEtherStatsJabbersHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsJabbersHistory.setStatus("current")
_ZxAnEponEtherStatsCollisionsHistory_Type = Counter32
_ZxAnEponEtherStatsCollisionsHistory_Object = MibTableColumn
zxAnEponEtherStatsCollisionsHistory = _ZxAnEponEtherStatsCollisionsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 11),
    _ZxAnEponEtherStatsCollisionsHistory_Type()
)
zxAnEponEtherStatsCollisionsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsCollisionsHistory.setStatus("current")
_ZxAnEponEtherStatsPkts64OctetsHistory_Type = Counter32
_ZxAnEponEtherStatsPkts64OctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsPkts64OctetsHistory = _ZxAnEponEtherStatsPkts64OctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 12),
    _ZxAnEponEtherStatsPkts64OctetsHistory_Type()
)
zxAnEponEtherStatsPkts64OctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts64OctetsHistory.setStatus("current")
_ZxAnEponEtherStatsPkts65to127OctetsHistory_Type = Counter32
_ZxAnEponEtherStatsPkts65to127OctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsPkts65to127OctetsHistory = _ZxAnEponEtherStatsPkts65to127OctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 13),
    _ZxAnEponEtherStatsPkts65to127OctetsHistory_Type()
)
zxAnEponEtherStatsPkts65to127OctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts65to127OctetsHistory.setStatus("current")
_ZxAnEponEtherStatsPkts128to255OctetsHistory_Type = Counter32
_ZxAnEponEtherStatsPkts128to255OctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsPkts128to255OctetsHistory = _ZxAnEponEtherStatsPkts128to255OctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 14),
    _ZxAnEponEtherStatsPkts128to255OctetsHistory_Type()
)
zxAnEponEtherStatsPkts128to255OctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts128to255OctetsHistory.setStatus("current")
_ZxAnEponEtherStatsPkts256to511OctetsHistory_Type = Counter32
_ZxAnEponEtherStatsPkts256to511OctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsPkts256to511OctetsHistory = _ZxAnEponEtherStatsPkts256to511OctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 15),
    _ZxAnEponEtherStatsPkts256to511OctetsHistory_Type()
)
zxAnEponEtherStatsPkts256to511OctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts256to511OctetsHistory.setStatus("current")
_ZxAnEponEtherStatsPkts512to1023OctetsHistory_Type = Counter32
_ZxAnEponEtherStatsPkts512to1023OctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsPkts512to1023OctetsHistory = _ZxAnEponEtherStatsPkts512to1023OctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 16),
    _ZxAnEponEtherStatsPkts512to1023OctetsHistory_Type()
)
zxAnEponEtherStatsPkts512to1023OctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts512to1023OctetsHistory.setStatus("current")
_ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Type = Counter32
_ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Object = MibTableColumn
zxAnEponEtherStatsPkts1024to1518OctetsHistory = _ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 3, 1, 17),
    _ZxAnEponEtherStatsPkts1024to1518OctetsHistory_Type()
)
zxAnEponEtherStatsPkts1024to1518OctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponEtherStatsPkts1024to1518OctetsHistory.setStatus("current")
_ZxAnEponIfXHistoryTable_Object = MibTable
zxAnEponIfXHistoryTable = _ZxAnEponIfXHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4)
)
if mibBuilder.loadTexts:
    zxAnEponIfXHistoryTable.setStatus("current")
_ZxAnEponIfXHistoryEntry_Object = MibTableRow
zxAnEponIfXHistoryEntry = _ZxAnEponIfXHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnEponIfXHistoryEntry.setStatus("current")
_ZxAnEponIfInMulticastPktsHistory_Type = Counter32
_ZxAnEponIfInMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfInMulticastPktsHistory = _ZxAnEponIfInMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 1),
    _ZxAnEponIfInMulticastPktsHistory_Type()
)
zxAnEponIfInMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInMulticastPktsHistory.setStatus("current")
_ZxAnEponIfInBroadcastPktsHistory_Type = Counter32
_ZxAnEponIfInBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfInBroadcastPktsHistory = _ZxAnEponIfInBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 2),
    _ZxAnEponIfInBroadcastPktsHistory_Type()
)
zxAnEponIfInBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfInBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfOutMulticastPktsHistory_Type = Counter32
_ZxAnEponIfOutMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfOutMulticastPktsHistory = _ZxAnEponIfOutMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 3),
    _ZxAnEponIfOutMulticastPktsHistory_Type()
)
zxAnEponIfOutMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutMulticastPktsHistory.setStatus("current")
_ZxAnEponIfOutBroadcastPktsHistory_Type = Counter32
_ZxAnEponIfOutBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfOutBroadcastPktsHistory = _ZxAnEponIfOutBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 4),
    _ZxAnEponIfOutBroadcastPktsHistory_Type()
)
zxAnEponIfOutBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOutBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfHCInOctetsHistory_Type = Counter64
_ZxAnEponIfHCInOctetsHistory_Object = MibTableColumn
zxAnEponIfHCInOctetsHistory = _ZxAnEponIfHCInOctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 5),
    _ZxAnEponIfHCInOctetsHistory_Type()
)
zxAnEponIfHCInOctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInOctetsHistory.setStatus("current")
_ZxAnEponIfHCInUcastPktsHistory_Type = Counter64
_ZxAnEponIfHCInUcastPktsHistory_Object = MibTableColumn
zxAnEponIfHCInUcastPktsHistory = _ZxAnEponIfHCInUcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 6),
    _ZxAnEponIfHCInUcastPktsHistory_Type()
)
zxAnEponIfHCInUcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInUcastPktsHistory.setStatus("current")
_ZxAnEponIfHCInMulticastPktsHistory_Type = Counter64
_ZxAnEponIfHCInMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfHCInMulticastPktsHistory = _ZxAnEponIfHCInMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 7),
    _ZxAnEponIfHCInMulticastPktsHistory_Type()
)
zxAnEponIfHCInMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInMulticastPktsHistory.setStatus("current")
_ZxAnEponIfHCInBroadcastPktsHistory_Type = Counter64
_ZxAnEponIfHCInBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfHCInBroadcastPktsHistory = _ZxAnEponIfHCInBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 8),
    _ZxAnEponIfHCInBroadcastPktsHistory_Type()
)
zxAnEponIfHCInBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCInBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfHCOutOctetsHistory_Type = Counter64
_ZxAnEponIfHCOutOctetsHistory_Object = MibTableColumn
zxAnEponIfHCOutOctetsHistory = _ZxAnEponIfHCOutOctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 9),
    _ZxAnEponIfHCOutOctetsHistory_Type()
)
zxAnEponIfHCOutOctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutOctetsHistory.setStatus("current")
_ZxAnEponIfHCOutUcastPktsHistory_Type = Counter64
_ZxAnEponIfHCOutUcastPktsHistory_Object = MibTableColumn
zxAnEponIfHCOutUcastPktsHistory = _ZxAnEponIfHCOutUcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 10),
    _ZxAnEponIfHCOutUcastPktsHistory_Type()
)
zxAnEponIfHCOutUcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutUcastPktsHistory.setStatus("current")
_ZxAnEponIfHCOutMulticastPktsHistory_Type = Counter64
_ZxAnEponIfHCOutMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfHCOutMulticastPktsHistory = _ZxAnEponIfHCOutMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 11),
    _ZxAnEponIfHCOutMulticastPktsHistory_Type()
)
zxAnEponIfHCOutMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutMulticastPktsHistory.setStatus("current")
_ZxAnEponIfHCOutBroadcastPktsHistory_Type = Counter64
_ZxAnEponIfHCOutBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfHCOutBroadcastPktsHistory = _ZxAnEponIfHCOutBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 4, 1, 12),
    _ZxAnEponIfHCOutBroadcastPktsHistory_Type()
)
zxAnEponIfHCOutBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfHCOutBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfXOltHistoryTable_Object = MibTable
zxAnEponIfXOltHistoryTable = _ZxAnEponIfXOltHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5)
)
if mibBuilder.loadTexts:
    zxAnEponIfXOltHistoryTable.setStatus("current")
_ZxAnEponIfXOltHistoryEntry_Object = MibTableRow
zxAnEponIfXOltHistoryEntry = _ZxAnEponIfXOltHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnEponIfXOltHistoryEntry.setStatus("current")
_ZxAnEponIfOltInMulticastPktsHistory_Type = Counter32
_ZxAnEponIfOltInMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfOltInMulticastPktsHistory = _ZxAnEponIfOltInMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 1),
    _ZxAnEponIfOltInMulticastPktsHistory_Type()
)
zxAnEponIfOltInMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltInMulticastPktsHistory.setStatus("current")
_ZxAnEponIfOltInBroadcastPktsHistory_Type = Counter32
_ZxAnEponIfOltInBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfOltInBroadcastPktsHistory = _ZxAnEponIfOltInBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 2),
    _ZxAnEponIfOltInBroadcastPktsHistory_Type()
)
zxAnEponIfOltInBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltInBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfOltOutMulticastPktsHistory_Type = Counter32
_ZxAnEponIfOltOutMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfOltOutMulticastPktsHistory = _ZxAnEponIfOltOutMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 3),
    _ZxAnEponIfOltOutMulticastPktsHistory_Type()
)
zxAnEponIfOltOutMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltOutMulticastPktsHistory.setStatus("current")
_ZxAnEponIfOltOutBroadcastPktsHistory_Type = Counter32
_ZxAnEponIfOltOutBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfOltOutBroadcastPktsHistory = _ZxAnEponIfOltOutBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 4),
    _ZxAnEponIfOltOutBroadcastPktsHistory_Type()
)
zxAnEponIfOltOutBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltOutBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfOltHCInOctetsHistory_Type = Counter64
_ZxAnEponIfOltHCInOctetsHistory_Object = MibTableColumn
zxAnEponIfOltHCInOctetsHistory = _ZxAnEponIfOltHCInOctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 5),
    _ZxAnEponIfOltHCInOctetsHistory_Type()
)
zxAnEponIfOltHCInOctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInOctetsHistory.setStatus("current")
_ZxAnEponIfOltHCInUcastPktsHistory_Type = Counter64
_ZxAnEponIfOltHCInUcastPktsHistory_Object = MibTableColumn
zxAnEponIfOltHCInUcastPktsHistory = _ZxAnEponIfOltHCInUcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 6),
    _ZxAnEponIfOltHCInUcastPktsHistory_Type()
)
zxAnEponIfOltHCInUcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInUcastPktsHistory.setStatus("current")
_ZxAnEponIfOltHCInMulticastPktsHistory_Type = Counter64
_ZxAnEponIfOltHCInMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfOltHCInMulticastPktsHistory = _ZxAnEponIfOltHCInMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 7),
    _ZxAnEponIfOltHCInMulticastPktsHistory_Type()
)
zxAnEponIfOltHCInMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInMulticastPktsHistory.setStatus("current")
_ZxAnEponIfOltHCInBroadcastPktsHistory_Type = Counter64
_ZxAnEponIfOltHCInBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfOltHCInBroadcastPktsHistory = _ZxAnEponIfOltHCInBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 8),
    _ZxAnEponIfOltHCInBroadcastPktsHistory_Type()
)
zxAnEponIfOltHCInBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCInBroadcastPktsHistory.setStatus("current")
_ZxAnEponIfOltHCOutOctetsHistory_Type = Counter64
_ZxAnEponIfOltHCOutOctetsHistory_Object = MibTableColumn
zxAnEponIfOltHCOutOctetsHistory = _ZxAnEponIfOltHCOutOctetsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 9),
    _ZxAnEponIfOltHCOutOctetsHistory_Type()
)
zxAnEponIfOltHCOutOctetsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutOctetsHistory.setStatus("current")
_ZxAnEponIfOltHCOutUcastPktsHistory_Type = Counter64
_ZxAnEponIfOltHCOutUcastPktsHistory_Object = MibTableColumn
zxAnEponIfOltHCOutUcastPktsHistory = _ZxAnEponIfOltHCOutUcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 10),
    _ZxAnEponIfOltHCOutUcastPktsHistory_Type()
)
zxAnEponIfOltHCOutUcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutUcastPktsHistory.setStatus("current")
_ZxAnEponIfOltHCOutMulticastPktsHistory_Type = Counter64
_ZxAnEponIfOltHCOutMulticastPktsHistory_Object = MibTableColumn
zxAnEponIfOltHCOutMulticastPktsHistory = _ZxAnEponIfOltHCOutMulticastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 11),
    _ZxAnEponIfOltHCOutMulticastPktsHistory_Type()
)
zxAnEponIfOltHCOutMulticastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutMulticastPktsHistory.setStatus("current")
_ZxAnEponIfOltHCOutBroadcastPktsHistory_Type = Counter64
_ZxAnEponIfOltHCOutBroadcastPktsHistory_Object = MibTableColumn
zxAnEponIfOltHCOutBroadcastPktsHistory = _ZxAnEponIfOltHCOutBroadcastPktsHistory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 9, 3, 5, 1, 12),
    _ZxAnEponIfOltHCOutBroadcastPktsHistory_Type()
)
zxAnEponIfOltHCOutBroadcastPktsHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponIfOltHCOutBroadcastPktsHistory.setStatus("current")
zxAnEponIfEntry.registerAugmentions(
    ("ZXEPON-PERFORMANCE-MIB",
     "zxAnEponIfXEntry")
)
zxAnEponIfXEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
zxAnEponIfEntry.registerAugmentions(
    ("ZXEPON-PERFORMANCE-MIB",
     "zxAnEponIfXOltEntry")
)
zxAnEponIfXOltEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
zxAnEponIfCurrentEntry.registerAugmentions(
    ("ZXEPON-PERFORMANCE-MIB",
     "zxAnEponIfXCurrentEntry")
)
zxAnEponIfXCurrentEntry.setIndexNames(*zxAnEponIfCurrentEntry.getIndexNames())
zxAnEponIfEntry.registerAugmentions(
    ("ZXEPON-PERFORMANCE-MIB",
     "zxAnEponIfXHistoryEntry")
)
zxAnEponIfXHistoryEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())
zxAnEponIfEntry.registerAugmentions(
    ("ZXEPON-PERFORMANCE-MIB",
     "zxAnEponIfXOltHistoryEntry")
)
zxAnEponIfXOltHistoryEntry.setIndexNames(*zxAnEponIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXEPON-PERFORMANCE-MIB",
    **{"zxAnEponPm": zxAnEponPm,
       "zxAnEponPmInfor": zxAnEponPmInfor,
       "zxAnEponOltVirtualIfBERStatisticTable": zxAnEponOltVirtualIfBERStatisticTable,
       "zxAnEponOltVirtualIfBERStatisticEntry": zxAnEponOltVirtualIfBERStatisticEntry,
       "zxAnEponOltVirtualIfBERStatisticOnuBER": zxAnEponOltVirtualIfBERStatisticOnuBER,
       "zxAnEponOltVirtualIfBERStatisticOnuFER": zxAnEponOltVirtualIfBERStatisticOnuFER,
       "zxAnEponOltPhyPortStatisticTable": zxAnEponOltPhyPortStatisticTable,
       "zxAnEponOltPhyPortStatisticEntry": zxAnEponOltPhyPortStatisticEntry,
       "zxAnEponOltPhyPortStatisticOltPonAverageBER": zxAnEponOltPhyPortStatisticOltPonAverageBER,
       "zxAnEponOltPhyPortStatisticOltSysAverageBER": zxAnEponOltPhyPortStatisticOltSysAverageBER,
       "zxAnEponEtherStatsTable": zxAnEponEtherStatsTable,
       "zxAnEponEtherStatsEntry": zxAnEponEtherStatsEntry,
       "zxAnEponEtherStatsDropEvents": zxAnEponEtherStatsDropEvents,
       "zxAnEponEtherStatsOctets": zxAnEponEtherStatsOctets,
       "zxAnEponEtherStatsPkts": zxAnEponEtherStatsPkts,
       "zxAnEponEtherStatsBroadcastPkts": zxAnEponEtherStatsBroadcastPkts,
       "zxAnEponEtherStatsMulticastPkts": zxAnEponEtherStatsMulticastPkts,
       "zxAnEponEtherStatsCRCAlignErrors": zxAnEponEtherStatsCRCAlignErrors,
       "zxAnEponEtherStatsUndersizePkts": zxAnEponEtherStatsUndersizePkts,
       "zxAnEponEtherStatsOversizePkts": zxAnEponEtherStatsOversizePkts,
       "zxAnEponEtherStatsFragments": zxAnEponEtherStatsFragments,
       "zxAnEponEtherStatsJabbers": zxAnEponEtherStatsJabbers,
       "zxAnEponEtherStatsCollisions": zxAnEponEtherStatsCollisions,
       "zxAnEponEtherStatsPkts64Octets": zxAnEponEtherStatsPkts64Octets,
       "zxAnEponEtherStatsPkts65to127Octets": zxAnEponEtherStatsPkts65to127Octets,
       "zxAnEponEtherStatsPkts128to255Octets": zxAnEponEtherStatsPkts128to255Octets,
       "zxAnEponEtherStatsPkts256to511Octets": zxAnEponEtherStatsPkts256to511Octets,
       "zxAnEponEtherStatsPkts512to1023Octets": zxAnEponEtherStatsPkts512to1023Octets,
       "zxAnEponEtherStatsPkts1024to1518Octets": zxAnEponEtherStatsPkts1024to1518Octets,
       "zxAnEponIfTable": zxAnEponIfTable,
       "zxAnEponIfEntry": zxAnEponIfEntry,
       "zxAnEponIfInOctets": zxAnEponIfInOctets,
       "zxAnEponIfInUcastPkts": zxAnEponIfInUcastPkts,
       "zxAnEponIfInNUcastPkts": zxAnEponIfInNUcastPkts,
       "zxAnEponIfInDiscards": zxAnEponIfInDiscards,
       "zxAnEponIfInErrors": zxAnEponIfInErrors,
       "zxAnEponIfInUnknownProtos": zxAnEponIfInUnknownProtos,
       "zxAnEponIfOutOctets": zxAnEponIfOutOctets,
       "zxAnEponIfOutUcastPkts": zxAnEponIfOutUcastPkts,
       "zxAnEponIfOutNUcastPkts": zxAnEponIfOutNUcastPkts,
       "zxAnEponIfOutDiscards": zxAnEponIfOutDiscards,
       "zxAnEponIfOutErrors": zxAnEponIfOutErrors,
       "zxAnEponIfXTable": zxAnEponIfXTable,
       "zxAnEponIfXEntry": zxAnEponIfXEntry,
       "zxAnEponIfInMulticastPkts": zxAnEponIfInMulticastPkts,
       "zxAnEponIfInBroadcastPkts": zxAnEponIfInBroadcastPkts,
       "zxAnEponIfOutMulticastPkts": zxAnEponIfOutMulticastPkts,
       "zxAnEponIfOutBroadcastPkts": zxAnEponIfOutBroadcastPkts,
       "zxAnEponIfHCInOctets": zxAnEponIfHCInOctets,
       "zxAnEponIfHCInUcastPkts": zxAnEponIfHCInUcastPkts,
       "zxAnEponIfHCInMulticastPkts": zxAnEponIfHCInMulticastPkts,
       "zxAnEponIfHCInBroadcastPkts": zxAnEponIfHCInBroadcastPkts,
       "zxAnEponIfHCOutOctets": zxAnEponIfHCOutOctets,
       "zxAnEponIfHCOutUcastPkts": zxAnEponIfHCOutUcastPkts,
       "zxAnEponIfHCOutMulticastPkts": zxAnEponIfHCOutMulticastPkts,
       "zxAnEponIfHCOutBroadcastPkts": zxAnEponIfHCOutBroadcastPkts,
       "zxAnEponDot3PauseTable": zxAnEponDot3PauseTable,
       "zxAnEponDot3PauseEntry": zxAnEponDot3PauseEntry,
       "zxAnEponDot3InPauseFrames": zxAnEponDot3InPauseFrames,
       "zxAnEponDot3OutPauseFrames": zxAnEponDot3OutPauseFrames,
       "zxAnEponDot3HCInPauseFrames": zxAnEponDot3HCInPauseFrames,
       "zxAnEponDot3HCOutPauseFrames": zxAnEponDot3HCOutPauseFrames,
       "zxAnEponDot3HCStatsTable": zxAnEponDot3HCStatsTable,
       "zxAnEponDot3HCStatsEntry": zxAnEponDot3HCStatsEntry,
       "zxAnEponDot3HCStatsAlignmentErrors": zxAnEponDot3HCStatsAlignmentErrors,
       "zxAnEponDot3HCStatsFCSErrors": zxAnEponDot3HCStatsFCSErrors,
       "zxAnEponDot3HCStatsInternalMacTransmitErrors": zxAnEponDot3HCStatsInternalMacTransmitErrors,
       "zxAnEponDot3HCStatsFrameTooLongs": zxAnEponDot3HCStatsFrameTooLongs,
       "zxAnEponDot3HCStatsInternalMacReceiveErrors": zxAnEponDot3HCStatsInternalMacReceiveErrors,
       "zxAnEponDot3HCStatsSymbolErrors": zxAnEponDot3HCStatsSymbolErrors,
       "zxAnEponIfXOltTable": zxAnEponIfXOltTable,
       "zxAnEponIfXOltEntry": zxAnEponIfXOltEntry,
       "zxAnEponIfOltInMulticastPkts": zxAnEponIfOltInMulticastPkts,
       "zxAnEponIfOltInBroadcastPkts": zxAnEponIfOltInBroadcastPkts,
       "zxAnEponIfOltOutMulticastPkts": zxAnEponIfOltOutMulticastPkts,
       "zxAnEponIfOltOutBroadcastPkts": zxAnEponIfOltOutBroadcastPkts,
       "zxAnEponIfOltHCInOctets": zxAnEponIfOltHCInOctets,
       "zxAnEponIfOltHCInUcastPkts": zxAnEponIfOltHCInUcastPkts,
       "zxAnEponIfOltHCInMulticastPkts": zxAnEponIfOltHCInMulticastPkts,
       "zxAnEponIfOltHCInBroadcastPkts": zxAnEponIfOltHCInBroadcastPkts,
       "zxAnEponIfOltHCOutOctets": zxAnEponIfOltHCOutOctets,
       "zxAnEponIfOltHCOutUcastPkts": zxAnEponIfOltHCOutUcastPkts,
       "zxAnEponIfOltHCOutMulticastPkts": zxAnEponIfOltHCOutMulticastPkts,
       "zxAnEponIfOltHCOutBroadcastPkts": zxAnEponIfOltHCOutBroadcastPkts,
       "zxAnEponPmCurrent": zxAnEponPmCurrent,
       "zxAnEponDot3MpcpStatCurrentTable": zxAnEponDot3MpcpStatCurrentTable,
       "zxAnEponDot3MpcpStatCurrentEntry": zxAnEponDot3MpcpStatCurrentEntry,
       "zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent": zxAnEponDot3MpcpMACCtrlFramesTransmittedCurrent,
       "zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent": zxAnEponDot3MpcpMACCtrlFramesReceivedCurrent,
       "zxAnEponDot3MpcpDiscoveryWindowsSentCurrent": zxAnEponDot3MpcpDiscoveryWindowsSentCurrent,
       "zxAnEponDot3MpcpDiscoveryTimeoutCurrent": zxAnEponDot3MpcpDiscoveryTimeoutCurrent,
       "zxAnEponDot3MpcpTxRegRequestCurrent": zxAnEponDot3MpcpTxRegRequestCurrent,
       "zxAnEponDot3MpcpRxRegRequestCurrent": zxAnEponDot3MpcpRxRegRequestCurrent,
       "zxAnEponDot3MpcpTxRegAckCurrent": zxAnEponDot3MpcpTxRegAckCurrent,
       "zxAnEponDot3MpcpRxRegAckCurrent": zxAnEponDot3MpcpRxRegAckCurrent,
       "zxAnEponDot3MpcpTxReportCurrent": zxAnEponDot3MpcpTxReportCurrent,
       "zxAnEponDot3MpcpRxReportCurrent": zxAnEponDot3MpcpRxReportCurrent,
       "zxAnEponDot3MpcpTxGateCurrent": zxAnEponDot3MpcpTxGateCurrent,
       "zxAnEponDot3MpcpRxGateCurrent": zxAnEponDot3MpcpRxGateCurrent,
       "zxAnEponDot3MpcpTxRegisterCurrent": zxAnEponDot3MpcpTxRegisterCurrent,
       "zxAnEponDot3MpcpRxRegisterCurrent": zxAnEponDot3MpcpRxRegisterCurrent,
       "zxAnEponDot3OmpEmulationStatCurrentTable": zxAnEponDot3OmpEmulationStatCurrentTable,
       "zxAnEponDot3OmpEmulationStatCurrentEntry": zxAnEponDot3OmpEmulationStatCurrentEntry,
       "zxAnEponDot3OmpEmulationSLDErrorsCurrent": zxAnEponDot3OmpEmulationSLDErrorsCurrent,
       "zxAnEponDot3OmpEmulationCRC8ErrorsCurrent": zxAnEponDot3OmpEmulationCRC8ErrorsCurrent,
       "zxAnEponDot3OmpEmulationBadLLIDCurrent": zxAnEponDot3OmpEmulationBadLLIDCurrent,
       "zxAnEponDot3OmpEmulationGoodLLIDCurrent": zxAnEponDot3OmpEmulationGoodLLIDCurrent,
       "zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent": zxAnEponDot3OmpEmulationOnuPonCastLLIDCurrent,
       "zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent": zxAnEponDot3OmpEmulationOltPonCastLLIDCurrent,
       "zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent": zxAnEponDot3OmpEmulationBroadcastBitNotOnuLlidCurrent,
       "zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent": zxAnEponDot3OmpEmulationOnuLLIDNotBroadcastCurrent,
       "zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent": zxAnEponDot3OmpEmulationBroadcastBitPlusOnuLlidCurrent,
       "zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent": zxAnEponDot3OmpEmulationNotBroadcastBitNotOnuLlidCurrent,
       "zxAnEponDot3EponFecCurrentTable": zxAnEponDot3EponFecCurrentTable,
       "zxAnEponDot3EponFecCurrentEntry": zxAnEponDot3EponFecCurrentEntry,
       "zxAnEponDot3EponFecPCSCodingViolationCurrent": zxAnEponDot3EponFecPCSCodingViolationCurrent,
       "zxAnEponDot3EponFecAbilityCurrent": zxAnEponDot3EponFecAbilityCurrent,
       "zxAnEponDot3EponFecModeCurrent": zxAnEponDot3EponFecModeCurrent,
       "zxAnEponDot3EponFecCorrectedBlocksCurrent": zxAnEponDot3EponFecCorrectedBlocksCurrent,
       "zxAnEponDot3EponFecUncorrectableBlocksCurrent": zxAnEponDot3EponFecUncorrectableBlocksCurrent,
       "zxAnEponDot3EponFecBufferHeadCodingViolationCurrent": zxAnEponDot3EponFecBufferHeadCodingViolationCurrent,
       "zxAnEponDot3ExtPkgQueueCurrentTable": zxAnEponDot3ExtPkgQueueCurrentTable,
       "zxAnEponDot3ExtPkgQueueCurrentEntry": zxAnEponDot3ExtPkgQueueCurrentEntry,
       "zxAnEponDot3QueueIndexCurrent": zxAnEponDot3QueueIndexCurrent,
       "zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent": zxAnEponDot3ExtPkgObjectReportNumThresholdCurrent,
       "zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent": zxAnEponDot3ExtPkgObjectReportMaximumNumThresholdCurrent,
       "zxAnEponDot3ExtPkgStatTxFramesQueueCurrent": zxAnEponDot3ExtPkgStatTxFramesQueueCurrent,
       "zxAnEponDot3ExtPkgStatRxFramesQueueCurrent": zxAnEponDot3ExtPkgStatRxFramesQueueCurrent,
       "zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent": zxAnEponDot3ExtPkgStatDroppedFramesQueueCurrent,
       "zxAnEponDot3OamStatsCurrentTable": zxAnEponDot3OamStatsCurrentTable,
       "zxAnEponDot3OamStatsCurrentEntry": zxAnEponDot3OamStatsCurrentEntry,
       "zxAnEponDot3OamInformationTxCurrent": zxAnEponDot3OamInformationTxCurrent,
       "zxAnEponDot3OamInformationRxCurrent": zxAnEponDot3OamInformationRxCurrent,
       "zxAnEponDot3OamUniqueEventNotificationTxCurrent": zxAnEponDot3OamUniqueEventNotificationTxCurrent,
       "zxAnEponDot3OamUniqueEventNotificationRxCurrent": zxAnEponDot3OamUniqueEventNotificationRxCurrent,
       "zxAnEponDot3OamDuplicateEventNotificationTxCurrent": zxAnEponDot3OamDuplicateEventNotificationTxCurrent,
       "zxAnEponDot3OamDuplicateEventNotificationRxCurrent": zxAnEponDot3OamDuplicateEventNotificationRxCurrent,
       "zxAnEponDot3OamLoopbackControlTxCurrent": zxAnEponDot3OamLoopbackControlTxCurrent,
       "zxAnEponDot3OamLoopbackControlRxCurrent": zxAnEponDot3OamLoopbackControlRxCurrent,
       "zxAnEponDot3OamVariableRequestTxCurrent": zxAnEponDot3OamVariableRequestTxCurrent,
       "zxAnEponDot3OamVariableRequestRxCurrent": zxAnEponDot3OamVariableRequestRxCurrent,
       "zxAnEponDot3OamVariableResponseTxCurrent": zxAnEponDot3OamVariableResponseTxCurrent,
       "zxAnEponDot3OamVariableResponseRxCurrent": zxAnEponDot3OamVariableResponseRxCurrent,
       "zxAnEponDot3OamOrgSpecificTxCurrent": zxAnEponDot3OamOrgSpecificTxCurrent,
       "zxAnEponDot3OamOrgSpecificRxCurrent": zxAnEponDot3OamOrgSpecificRxCurrent,
       "zxAnEponDot3OamUnsupportedCodesTxCurrent": zxAnEponDot3OamUnsupportedCodesTxCurrent,
       "zxAnEponDot3OamUnsupportedCodesRxCurrent": zxAnEponDot3OamUnsupportedCodesRxCurrent,
       "zxAnEponDot3OamFramesLostDueToOamCurrent": zxAnEponDot3OamFramesLostDueToOamCurrent,
       "zxAnEponOltVirtualIfBERStatisticCurrentTable": zxAnEponOltVirtualIfBERStatisticCurrentTable,
       "zxAnEponOltVirtualIfBERStatisticCurrentEntry": zxAnEponOltVirtualIfBERStatisticCurrentEntry,
       "zxAnEponOltVirtualIfBERStatisticOnuBERCurrent": zxAnEponOltVirtualIfBERStatisticOnuBERCurrent,
       "zxAnEponOltVirtualIfBERStatisticOnuFERCurrent": zxAnEponOltVirtualIfBERStatisticOnuFERCurrent,
       "zxAnEponOltPhyPortStatisticCurrentTable": zxAnEponOltPhyPortStatisticCurrentTable,
       "zxAnEponOltPhyPortStatisticCurrentEntry": zxAnEponOltPhyPortStatisticCurrentEntry,
       "zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent": zxAnEponOltPhyPortStatisticOltPonAverageBERCurrent,
       "zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent": zxAnEponOltPhyPortStatisticOltSysAverageBERCurrent,
       "zxAnEponEtherStatsCurrentTable": zxAnEponEtherStatsCurrentTable,
       "zxAnEponEtherStatsCurrentEntry": zxAnEponEtherStatsCurrentEntry,
       "zxAnEponEtherStatsDropEventsCurrent": zxAnEponEtherStatsDropEventsCurrent,
       "zxAnEponEtherStatsOctetsCurrent": zxAnEponEtherStatsOctetsCurrent,
       "zxAnEponEtherStatsPktsCurrent": zxAnEponEtherStatsPktsCurrent,
       "zxAnEponEtherStatsBroadcastPktsCurrent": zxAnEponEtherStatsBroadcastPktsCurrent,
       "zxAnEponEtherStatsMulticastPktsCurrent": zxAnEponEtherStatsMulticastPktsCurrent,
       "zxAnEponEtherStatsCRCAlignErrorsCurrent": zxAnEponEtherStatsCRCAlignErrorsCurrent,
       "zxAnEponEtherStatsUndersizePktsCurrent": zxAnEponEtherStatsUndersizePktsCurrent,
       "zxAnEponEtherStatsOversizePktsCurrent": zxAnEponEtherStatsOversizePktsCurrent,
       "zxAnEponEtherStatsFragmentsCurrent": zxAnEponEtherStatsFragmentsCurrent,
       "zxAnEponEtherStatsJabbersCurrent": zxAnEponEtherStatsJabbersCurrent,
       "zxAnEponEtherStatsCollisionsCurrent": zxAnEponEtherStatsCollisionsCurrent,
       "zxAnEponEtherStatsPkts64OctetsCurrent": zxAnEponEtherStatsPkts64OctetsCurrent,
       "zxAnEponEtherStatsPkts65to127OctetsCurrent": zxAnEponEtherStatsPkts65to127OctetsCurrent,
       "zxAnEponEtherStatsPkts128to255OctetsCurrent": zxAnEponEtherStatsPkts128to255OctetsCurrent,
       "zxAnEponEtherStatsPkts256to511OctetsCurrent": zxAnEponEtherStatsPkts256to511OctetsCurrent,
       "zxAnEponEtherStatsPkts512to1023OctetsCurrent": zxAnEponEtherStatsPkts512to1023OctetsCurrent,
       "zxAnEponEtherStatsPkts1024to1518OctetsCurrent": zxAnEponEtherStatsPkts1024to1518OctetsCurrent,
       "zxAnEponEtherStatsOwnerCurrent": zxAnEponEtherStatsOwnerCurrent,
       "zxAnEponEtherStatsStatusCurrent": zxAnEponEtherStatsStatusCurrent,
       "zxAnEponIfCurrentTable": zxAnEponIfCurrentTable,
       "zxAnEponIfCurrentEntry": zxAnEponIfCurrentEntry,
       "zxAnEponIfInOctetsCurrent": zxAnEponIfInOctetsCurrent,
       "zxAnEponIfInUcastPktsCurrent": zxAnEponIfInUcastPktsCurrent,
       "zxAnEponIfInNUcastPktsCurrent": zxAnEponIfInNUcastPktsCurrent,
       "zxAnEponIfInDiscardsCurrent": zxAnEponIfInDiscardsCurrent,
       "zxAnEponIfInErrorsCurrent": zxAnEponIfInErrorsCurrent,
       "zxAnEponIfInUnknownProtosCurrent": zxAnEponIfInUnknownProtosCurrent,
       "zxAnEponIfOutOctetsCurrent": zxAnEponIfOutOctetsCurrent,
       "zxAnEponIfOutUcastPktsCurrent": zxAnEponIfOutUcastPktsCurrent,
       "zxAnEponIfOutNUcastPktsCurrent": zxAnEponIfOutNUcastPktsCurrent,
       "zxAnEponIfOutDiscardsCurrent": zxAnEponIfOutDiscardsCurrent,
       "zxAnEponIfOutErrorsCurrent": zxAnEponIfOutErrorsCurrent,
       "zxAnEponIfXCurrentTable": zxAnEponIfXCurrentTable,
       "zxAnEponIfXCurrentEntry": zxAnEponIfXCurrentEntry,
       "zxAnEponIfInMulticastPktsCurrent": zxAnEponIfInMulticastPktsCurrent,
       "zxAnEponIfInBroadcastPktsCurrent": zxAnEponIfInBroadcastPktsCurrent,
       "zxAnEponIfOutMulticastPktsCurrent": zxAnEponIfOutMulticastPktsCurrent,
       "zxAnEponIfOutBroadcastPktsCurrent": zxAnEponIfOutBroadcastPktsCurrent,
       "zxAnEponIfHCInOctetsCurrent": zxAnEponIfHCInOctetsCurrent,
       "zxAnEponIfHCInUcastPktsCurrent": zxAnEponIfHCInUcastPktsCurrent,
       "zxAnEponIfHCInMulticastPktsCurrent": zxAnEponIfHCInMulticastPktsCurrent,
       "zxAnEponIfHCInBroadcastPktsCurrent": zxAnEponIfHCInBroadcastPktsCurrent,
       "zxAnEponIfHCOutOctetsCurrent": zxAnEponIfHCOutOctetsCurrent,
       "zxAnEponIfHCOutUcastPktsCurrent": zxAnEponIfHCOutUcastPktsCurrent,
       "zxAnEponIfHCOutMulticastPktsCurrent": zxAnEponIfHCOutMulticastPktsCurrent,
       "zxAnEponIfHCOutBroadcastPktsCurrent": zxAnEponIfHCOutBroadcastPktsCurrent,
       "zxAnEponDot3PauseCurrentTable": zxAnEponDot3PauseCurrentTable,
       "zxAnEponDot3PauseCurrentEntry": zxAnEponDot3PauseCurrentEntry,
       "zxAnEponDot3InPauseFramesCurrent": zxAnEponDot3InPauseFramesCurrent,
       "zxAnEponDot3OutPauseFramesCurrent": zxAnEponDot3OutPauseFramesCurrent,
       "zxAnEponDot3HCInPauseFramesCurrent": zxAnEponDot3HCInPauseFramesCurrent,
       "zxAnEponDot3HCOutPauseFramesCurrent": zxAnEponDot3HCOutPauseFramesCurrent,
       "zxAnEponDot3HCStatsCurrentTable": zxAnEponDot3HCStatsCurrentTable,
       "zxAnEponDot3HCStatsCurrentEntry": zxAnEponDot3HCStatsCurrentEntry,
       "zxAnEponDot3HCStatsAlignmentErrorsCurrent": zxAnEponDot3HCStatsAlignmentErrorsCurrent,
       "zxAnEponDot3HCStatsFCSErrorsCurrent": zxAnEponDot3HCStatsFCSErrorsCurrent,
       "zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent": zxAnEponDot3HCStatsInternalMacTransmitErrorsCurrent,
       "zxAnEponDot3HCStatsFrameTooLongsCurrent": zxAnEponDot3HCStatsFrameTooLongsCurrent,
       "zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent": zxAnEponDot3HCStatsInternalMacReceiveErrorsCurrent,
       "zxAnEponDot3HCStatsSymbolErrorsCurrent": zxAnEponDot3HCStatsSymbolErrorsCurrent,
       "zxAnEponOnuLlidStatTable": zxAnEponOnuLlidStatTable,
       "zxAnEponOnuLlidStatEntry": zxAnEponOnuLlidStatEntry,
       "zxAnEponOnuLlidRxFrames": zxAnEponOnuLlidRxFrames,
       "zxAnEponOnuLlidRxOctets": zxAnEponOnuLlidRxOctets,
       "zxAnEponOnuLlidRxMulticastFrames": zxAnEponOnuLlidRxMulticastFrames,
       "zxAnEponOnuLlidRxBroadcastFrames": zxAnEponOnuLlidRxBroadcastFrames,
       "zxAnEponOnuLlidTxFrames": zxAnEponOnuLlidTxFrames,
       "zxAnEponOnuLlidTxOctets": zxAnEponOnuLlidTxOctets,
       "zxAnEponOnuLlidTxMulticastFrames": zxAnEponOnuLlidTxMulticastFrames,
       "zxAnEponOnuLlidTxBroadcastFrames": zxAnEponOnuLlidTxBroadcastFrames,
       "zxAnEponOnuLlidCrcErrors": zxAnEponOnuLlidCrcErrors,
       "zxAnEponOnuLlidFecCrctedBlocks": zxAnEponOnuLlidFecCrctedBlocks,
       "zxAnEponOnuLlidFecUncrctedBlocks": zxAnEponOnuLlidFecUncrctedBlocks,
       "zxAnEponOnuLlidMpcpRxGateFrames": zxAnEponOnuLlidMpcpRxGateFrames,
       "zxAnEponOnuLlidMpcpRxCtrlFrames": zxAnEponOnuLlidMpcpRxCtrlFrames,
       "zxAnEponOnuLlidMpcpRxRegFrames": zxAnEponOnuLlidMpcpRxRegFrames,
       "zxAnEponOnuLlidMpcpTxCtrlFrames": zxAnEponOnuLlidMpcpTxCtrlFrames,
       "zxAnEponOnuLlidMpcpTxReqFrames": zxAnEponOnuLlidMpcpTxReqFrames,
       "zxAnEponOnuLlidMpcpTxRepFrames": zxAnEponOnuLlidMpcpTxRepFrames,
       "zxAnEponPmHistory": zxAnEponPmHistory,
       "zxAnEponOltVirtualIfBERStatisticHistoryTable": zxAnEponOltVirtualIfBERStatisticHistoryTable,
       "zxAnEponOltVirtualIfBERStatisticHistoryEntry": zxAnEponOltVirtualIfBERStatisticHistoryEntry,
       "zxAnEponOltVirtualIfBERStatisticHistoryOnuBER": zxAnEponOltVirtualIfBERStatisticHistoryOnuBER,
       "zxAnEponOltVirtualIfBERStatisticHistoryOnuFER": zxAnEponOltVirtualIfBERStatisticHistoryOnuFER,
       "zxAnEponOltPhyPortStatisticHistoryTable": zxAnEponOltPhyPortStatisticHistoryTable,
       "zxAnEponOltPhyPortStatisticHistoryEntry": zxAnEponOltPhyPortStatisticHistoryEntry,
       "zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER": zxAnEponOltPhyPortStatisticHistoryOltPonAverageBER,
       "zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER": zxAnEponOltPhyPortStatisticHistoryOltSysAverageBER,
       "zxAnEponEtherStatsHistoryTable": zxAnEponEtherStatsHistoryTable,
       "zxAnEponEtherStatsHistoryEntry": zxAnEponEtherStatsHistoryEntry,
       "zxAnEponEtherStatsDropEventsHistory": zxAnEponEtherStatsDropEventsHistory,
       "zxAnEponEtherStatsOctetsHistory": zxAnEponEtherStatsOctetsHistory,
       "zxAnEponEtherStatsPktsHistory": zxAnEponEtherStatsPktsHistory,
       "zxAnEponEtherStatsBroadcastPktsHistory": zxAnEponEtherStatsBroadcastPktsHistory,
       "zxAnEponEtherStatsMulticastPktsHistory": zxAnEponEtherStatsMulticastPktsHistory,
       "zxAnEponEtherStatsCRCAlignErrorsHistory": zxAnEponEtherStatsCRCAlignErrorsHistory,
       "zxAnEponEtherStatsUndersizePktsHistory": zxAnEponEtherStatsUndersizePktsHistory,
       "zxAnEponEtherStatsOversizePktsHistory": zxAnEponEtherStatsOversizePktsHistory,
       "zxAnEponEtherStatsFragmentsHistory": zxAnEponEtherStatsFragmentsHistory,
       "zxAnEponEtherStatsJabbersHistory": zxAnEponEtherStatsJabbersHistory,
       "zxAnEponEtherStatsCollisionsHistory": zxAnEponEtherStatsCollisionsHistory,
       "zxAnEponEtherStatsPkts64OctetsHistory": zxAnEponEtherStatsPkts64OctetsHistory,
       "zxAnEponEtherStatsPkts65to127OctetsHistory": zxAnEponEtherStatsPkts65to127OctetsHistory,
       "zxAnEponEtherStatsPkts128to255OctetsHistory": zxAnEponEtherStatsPkts128to255OctetsHistory,
       "zxAnEponEtherStatsPkts256to511OctetsHistory": zxAnEponEtherStatsPkts256to511OctetsHistory,
       "zxAnEponEtherStatsPkts512to1023OctetsHistory": zxAnEponEtherStatsPkts512to1023OctetsHistory,
       "zxAnEponEtherStatsPkts1024to1518OctetsHistory": zxAnEponEtherStatsPkts1024to1518OctetsHistory,
       "zxAnEponIfXHistoryTable": zxAnEponIfXHistoryTable,
       "zxAnEponIfXHistoryEntry": zxAnEponIfXHistoryEntry,
       "zxAnEponIfInMulticastPktsHistory": zxAnEponIfInMulticastPktsHistory,
       "zxAnEponIfInBroadcastPktsHistory": zxAnEponIfInBroadcastPktsHistory,
       "zxAnEponIfOutMulticastPktsHistory": zxAnEponIfOutMulticastPktsHistory,
       "zxAnEponIfOutBroadcastPktsHistory": zxAnEponIfOutBroadcastPktsHistory,
       "zxAnEponIfHCInOctetsHistory": zxAnEponIfHCInOctetsHistory,
       "zxAnEponIfHCInUcastPktsHistory": zxAnEponIfHCInUcastPktsHistory,
       "zxAnEponIfHCInMulticastPktsHistory": zxAnEponIfHCInMulticastPktsHistory,
       "zxAnEponIfHCInBroadcastPktsHistory": zxAnEponIfHCInBroadcastPktsHistory,
       "zxAnEponIfHCOutOctetsHistory": zxAnEponIfHCOutOctetsHistory,
       "zxAnEponIfHCOutUcastPktsHistory": zxAnEponIfHCOutUcastPktsHistory,
       "zxAnEponIfHCOutMulticastPktsHistory": zxAnEponIfHCOutMulticastPktsHistory,
       "zxAnEponIfHCOutBroadcastPktsHistory": zxAnEponIfHCOutBroadcastPktsHistory,
       "zxAnEponIfXOltHistoryTable": zxAnEponIfXOltHistoryTable,
       "zxAnEponIfXOltHistoryEntry": zxAnEponIfXOltHistoryEntry,
       "zxAnEponIfOltInMulticastPktsHistory": zxAnEponIfOltInMulticastPktsHistory,
       "zxAnEponIfOltInBroadcastPktsHistory": zxAnEponIfOltInBroadcastPktsHistory,
       "zxAnEponIfOltOutMulticastPktsHistory": zxAnEponIfOltOutMulticastPktsHistory,
       "zxAnEponIfOltOutBroadcastPktsHistory": zxAnEponIfOltOutBroadcastPktsHistory,
       "zxAnEponIfOltHCInOctetsHistory": zxAnEponIfOltHCInOctetsHistory,
       "zxAnEponIfOltHCInUcastPktsHistory": zxAnEponIfOltHCInUcastPktsHistory,
       "zxAnEponIfOltHCInMulticastPktsHistory": zxAnEponIfOltHCInMulticastPktsHistory,
       "zxAnEponIfOltHCInBroadcastPktsHistory": zxAnEponIfOltHCInBroadcastPktsHistory,
       "zxAnEponIfOltHCOutOctetsHistory": zxAnEponIfOltHCOutOctetsHistory,
       "zxAnEponIfOltHCOutUcastPktsHistory": zxAnEponIfOltHCOutUcastPktsHistory,
       "zxAnEponIfOltHCOutMulticastPktsHistory": zxAnEponIfOltHCOutMulticastPktsHistory,
       "zxAnEponIfOltHCOutBroadcastPktsHistory": zxAnEponIfOltHCOutBroadcastPktsHistory}
)
