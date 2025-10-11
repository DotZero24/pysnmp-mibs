# SNMP MIB module (ZTE-AN-VLAN-STATISTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VLAN-STATISTIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:36 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(VlanId,
 ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnVlanStatisticMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnVlanPerfEnableTable_Object = MibTable
zxAnVlanPerfEnableTable = _ZxAnVlanPerfEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 1)
)
if mibBuilder.loadTexts:
    zxAnVlanPerfEnableTable.setStatus("current")
_ZxAnVlanPerfEnableEntry_Object = MibTableRow
zxAnVlanPerfEnableEntry = _ZxAnVlanPerfEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 1, 1)
)
zxAnVlanPerfEnableEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-STATISTIC-MIB", "zxAnEnVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanPerfEnableEntry.setStatus("current")
_ZxAnEnVlanId_Type = VlanId
_ZxAnEnVlanId_Object = MibTableColumn
zxAnEnVlanId = _ZxAnEnVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 1, 1, 1),
    _ZxAnEnVlanId_Type()
)
zxAnEnVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnVlanId.setStatus("current")


class _ZxVlanPerfEnable_Type(Integer32):
    """Custom type zxVlanPerfEnable based on Integer32"""
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


_ZxVlanPerfEnable_Type.__name__ = "Integer32"
_ZxVlanPerfEnable_Object = MibTableColumn
zxVlanPerfEnable = _ZxVlanPerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 1, 1, 2),
    _ZxVlanPerfEnable_Type()
)
zxVlanPerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxVlanPerfEnable.setStatus("current")


class _ZxVlanIDAllEnable_Type(DisplayString):
    """Custom type zxVlanIDAllEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZxVlanIDAllEnable_Type.__name__ = "DisplayString"
_ZxVlanIDAllEnable_Object = MibTableColumn
zxVlanIDAllEnable = _ZxVlanIDAllEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 1, 1, 3),
    _ZxVlanIDAllEnable_Type()
)
zxVlanIDAllEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxVlanIDAllEnable.setStatus("current")
_ZxAnSwVlanPerfTable_Object = MibTable
zxAnSwVlanPerfTable = _ZxAnSwVlanPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2)
)
if mibBuilder.loadTexts:
    zxAnSwVlanPerfTable.setStatus("current")
_ZxAnSwVlanPerfEntry_Object = MibTableRow
zxAnSwVlanPerfEntry = _ZxAnSwVlanPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1)
)
zxAnSwVlanPerfEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-STATISTIC-MIB", "zxAnSwVlanId"),
)
if mibBuilder.loadTexts:
    zxAnSwVlanPerfEntry.setStatus("current")
_ZxAnSwVlanId_Type = VlanId
_ZxAnSwVlanId_Object = MibTableColumn
zxAnSwVlanId = _ZxAnSwVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 1),
    _ZxAnSwVlanId_Type()
)
zxAnSwVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwVlanId.setStatus("current")
_ZxAnSwVlanInOctets_Type = Counter64
_ZxAnSwVlanInOctets_Object = MibTableColumn
zxAnSwVlanInOctets = _ZxAnSwVlanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 2),
    _ZxAnSwVlanInOctets_Type()
)
zxAnSwVlanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInOctets.setStatus("current")
_ZxAnSwVlanOutOctets_Type = Counter64
_ZxAnSwVlanOutOctets_Object = MibTableColumn
zxAnSwVlanOutOctets = _ZxAnSwVlanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 3),
    _ZxAnSwVlanOutOctets_Type()
)
zxAnSwVlanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutOctets.setStatus("current")
_ZxAnSwVlanInPkts_Type = Counter64
_ZxAnSwVlanInPkts_Object = MibTableColumn
zxAnSwVlanInPkts = _ZxAnSwVlanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 4),
    _ZxAnSwVlanInPkts_Type()
)
zxAnSwVlanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInPkts.setStatus("current")
_ZxAnSwVlanOutPkts_Type = Counter64
_ZxAnSwVlanOutPkts_Object = MibTableColumn
zxAnSwVlanOutPkts = _ZxAnSwVlanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 5),
    _ZxAnSwVlanOutPkts_Type()
)
zxAnSwVlanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutPkts.setStatus("current")
_ZxAnSwVlanInBandwidth_Type = Integer32
_ZxAnSwVlanInBandwidth_Object = MibTableColumn
zxAnSwVlanInBandwidth = _ZxAnSwVlanInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 6),
    _ZxAnSwVlanInBandwidth_Type()
)
zxAnSwVlanInBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwVlanInBandwidth.setUnits("kbps")
_ZxAnSwVlanOutBandwidth_Type = Integer32
_ZxAnSwVlanOutBandwidth_Object = MibTableColumn
zxAnSwVlanOutBandwidth = _ZxAnSwVlanOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 7),
    _ZxAnSwVlanOutBandwidth_Type()
)
zxAnSwVlanOutBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwVlanOutBandwidth.setUnits("kbps")
_ZxAnSwVlanInBandwidthUtility_Type = Integer32
_ZxAnSwVlanInBandwidthUtility_Object = MibTableColumn
zxAnSwVlanInBandwidthUtility = _ZxAnSwVlanInBandwidthUtility_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 8),
    _ZxAnSwVlanInBandwidthUtility_Type()
)
zxAnSwVlanInBandwidthUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInBandwidthUtility.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwVlanInBandwidthUtility.setUnits("%")
_ZxAnSwVlanOutBandwidthUtility_Type = Integer32
_ZxAnSwVlanOutBandwidthUtility_Object = MibTableColumn
zxAnSwVlanOutBandwidthUtility = _ZxAnSwVlanOutBandwidthUtility_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 9),
    _ZxAnSwVlanOutBandwidthUtility_Type()
)
zxAnSwVlanOutBandwidthUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutBandwidthUtility.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwVlanOutBandwidthUtility.setUnits("%")
_ZxAnSwVlanInCurrOctetRate_Type = Gauge32
_ZxAnSwVlanInCurrOctetRate_Object = MibTableColumn
zxAnSwVlanInCurrOctetRate = _ZxAnSwVlanInCurrOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 10),
    _ZxAnSwVlanInCurrOctetRate_Type()
)
zxAnSwVlanInCurrOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInCurrOctetRate.setStatus("current")
_ZxAnSwVlanOutCurrOctetRate_Type = Gauge32
_ZxAnSwVlanOutCurrOctetRate_Object = MibTableColumn
zxAnSwVlanOutCurrOctetRate = _ZxAnSwVlanOutCurrOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 11),
    _ZxAnSwVlanOutCurrOctetRate_Type()
)
zxAnSwVlanOutCurrOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutCurrOctetRate.setStatus("current")
_ZxAnSwVlanInCurrPktRate_Type = Gauge32
_ZxAnSwVlanInCurrPktRate_Object = MibTableColumn
zxAnSwVlanInCurrPktRate = _ZxAnSwVlanInCurrPktRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 12),
    _ZxAnSwVlanInCurrPktRate_Type()
)
zxAnSwVlanInCurrPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInCurrPktRate.setStatus("current")
_ZxAnSwVlanOutCurrPktRate_Type = Gauge32
_ZxAnSwVlanOutCurrPktRate_Object = MibTableColumn
zxAnSwVlanOutCurrPktRate = _ZxAnSwVlanOutCurrPktRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 13),
    _ZxAnSwVlanOutCurrPktRate_Type()
)
zxAnSwVlanOutCurrPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutCurrPktRate.setStatus("current")
_ZxAnSwVlanInUcastPkts_Type = Counter64
_ZxAnSwVlanInUcastPkts_Object = MibTableColumn
zxAnSwVlanInUcastPkts = _ZxAnSwVlanInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 14),
    _ZxAnSwVlanInUcastPkts_Type()
)
zxAnSwVlanInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInUcastPkts.setStatus("current")
_ZxAnSwVlanOutUcastPkts_Type = Counter64
_ZxAnSwVlanOutUcastPkts_Object = MibTableColumn
zxAnSwVlanOutUcastPkts = _ZxAnSwVlanOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 15),
    _ZxAnSwVlanOutUcastPkts_Type()
)
zxAnSwVlanOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutUcastPkts.setStatus("current")
_ZxAnSwVlanInMulticastPkts_Type = Counter64
_ZxAnSwVlanInMulticastPkts_Object = MibTableColumn
zxAnSwVlanInMulticastPkts = _ZxAnSwVlanInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 16),
    _ZxAnSwVlanInMulticastPkts_Type()
)
zxAnSwVlanInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInMulticastPkts.setStatus("current")
_ZxAnSwVlanOutMulticastPkts_Type = Counter64
_ZxAnSwVlanOutMulticastPkts_Object = MibTableColumn
zxAnSwVlanOutMulticastPkts = _ZxAnSwVlanOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 17),
    _ZxAnSwVlanOutMulticastPkts_Type()
)
zxAnSwVlanOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutMulticastPkts.setStatus("current")
_ZxAnSwVlanInNUcastPkts_Type = Counter64
_ZxAnSwVlanInNUcastPkts_Object = MibTableColumn
zxAnSwVlanInNUcastPkts = _ZxAnSwVlanInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 18),
    _ZxAnSwVlanInNUcastPkts_Type()
)
zxAnSwVlanInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInNUcastPkts.setStatus("current")
_ZxAnSwVlanOutNUcastPkts_Type = Counter64
_ZxAnSwVlanOutNUcastPkts_Object = MibTableColumn
zxAnSwVlanOutNUcastPkts = _ZxAnSwVlanOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 19),
    _ZxAnSwVlanOutNUcastPkts_Type()
)
zxAnSwVlanOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutNUcastPkts.setStatus("current")
_ZxAnSwVlanInBroadcastPkts_Type = Counter64
_ZxAnSwVlanInBroadcastPkts_Object = MibTableColumn
zxAnSwVlanInBroadcastPkts = _ZxAnSwVlanInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 20),
    _ZxAnSwVlanInBroadcastPkts_Type()
)
zxAnSwVlanInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInBroadcastPkts.setStatus("current")
_ZxAnSwVlanOutBroadcastPkts_Type = Counter64
_ZxAnSwVlanOutBroadcastPkts_Object = MibTableColumn
zxAnSwVlanOutBroadcastPkts = _ZxAnSwVlanOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 21),
    _ZxAnSwVlanOutBroadcastPkts_Type()
)
zxAnSwVlanOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutBroadcastPkts.setStatus("current")
_ZxAnSwVlanInDiscards_Type = Counter64
_ZxAnSwVlanInDiscards_Object = MibTableColumn
zxAnSwVlanInDiscards = _ZxAnSwVlanInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 22),
    _ZxAnSwVlanInDiscards_Type()
)
zxAnSwVlanInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInDiscards.setStatus("current")
_ZxAnSwVlanOutDiscards_Type = Counter64
_ZxAnSwVlanOutDiscards_Object = MibTableColumn
zxAnSwVlanOutDiscards = _ZxAnSwVlanOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 23),
    _ZxAnSwVlanOutDiscards_Type()
)
zxAnSwVlanOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutDiscards.setStatus("current")
_ZxAnSwVlanInUndersizePkts_Type = Counter64
_ZxAnSwVlanInUndersizePkts_Object = MibTableColumn
zxAnSwVlanInUndersizePkts = _ZxAnSwVlanInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 24),
    _ZxAnSwVlanInUndersizePkts_Type()
)
zxAnSwVlanInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInUndersizePkts.setStatus("current")
_ZxAnSwVlanOutUndersizePkts_Type = Counter64
_ZxAnSwVlanOutUndersizePkts_Object = MibTableColumn
zxAnSwVlanOutUndersizePkts = _ZxAnSwVlanOutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 25),
    _ZxAnSwVlanOutUndersizePkts_Type()
)
zxAnSwVlanOutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutUndersizePkts.setStatus("current")
_ZxAnSwVlanInOversizePkts_Type = Counter64
_ZxAnSwVlanInOversizePkts_Object = MibTableColumn
zxAnSwVlanInOversizePkts = _ZxAnSwVlanInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 26),
    _ZxAnSwVlanInOversizePkts_Type()
)
zxAnSwVlanInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInOversizePkts.setStatus("current")
_ZxAnSwVlanOutOversizePkts_Type = Counter64
_ZxAnSwVlanOutOversizePkts_Object = MibTableColumn
zxAnSwVlanOutOversizePkts = _ZxAnSwVlanOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 27),
    _ZxAnSwVlanOutOversizePkts_Type()
)
zxAnSwVlanOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutOversizePkts.setStatus("current")
_ZxAnSwVlanInCRCAlignErrors_Type = Counter64
_ZxAnSwVlanInCRCAlignErrors_Object = MibTableColumn
zxAnSwVlanInCRCAlignErrors = _ZxAnSwVlanInCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 28),
    _ZxAnSwVlanInCRCAlignErrors_Type()
)
zxAnSwVlanInCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInCRCAlignErrors.setStatus("current")
_ZxAnSwVlanOutCRCAlignErrors_Type = Counter64
_ZxAnSwVlanOutCRCAlignErrors_Object = MibTableColumn
zxAnSwVlanOutCRCAlignErrors = _ZxAnSwVlanOutCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 29),
    _ZxAnSwVlanOutCRCAlignErrors_Type()
)
zxAnSwVlanOutCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutCRCAlignErrors.setStatus("current")
_ZxAnSwVlanInFragments_Type = Counter64
_ZxAnSwVlanInFragments_Object = MibTableColumn
zxAnSwVlanInFragments = _ZxAnSwVlanInFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 30),
    _ZxAnSwVlanInFragments_Type()
)
zxAnSwVlanInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInFragments.setStatus("current")
_ZxAnSwVlanOutFragments_Type = Counter64
_ZxAnSwVlanOutFragments_Object = MibTableColumn
zxAnSwVlanOutFragments = _ZxAnSwVlanOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 31),
    _ZxAnSwVlanOutFragments_Type()
)
zxAnSwVlanOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutFragments.setStatus("current")
_ZxAnSwVlanInJabbers_Type = Counter64
_ZxAnSwVlanInJabbers_Object = MibTableColumn
zxAnSwVlanInJabbers = _ZxAnSwVlanInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 32),
    _ZxAnSwVlanInJabbers_Type()
)
zxAnSwVlanInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInJabbers.setStatus("current")
_ZxAnSwVlanOutJabbers_Type = Counter64
_ZxAnSwVlanOutJabbers_Object = MibTableColumn
zxAnSwVlanOutJabbers = _ZxAnSwVlanOutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 33),
    _ZxAnSwVlanOutJabbers_Type()
)
zxAnSwVlanOutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutJabbers.setStatus("current")
_ZxAnSwVlanInCollisions_Type = Counter64
_ZxAnSwVlanInCollisions_Object = MibTableColumn
zxAnSwVlanInCollisions = _ZxAnSwVlanInCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 34),
    _ZxAnSwVlanInCollisions_Type()
)
zxAnSwVlanInCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInCollisions.setStatus("current")
_ZxAnSwVlanOutCollisions_Type = Counter64
_ZxAnSwVlanOutCollisions_Object = MibTableColumn
zxAnSwVlanOutCollisions = _ZxAnSwVlanOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 35),
    _ZxAnSwVlanOutCollisions_Type()
)
zxAnSwVlanOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutCollisions.setStatus("current")
_ZxAnSwVlanInUnknownProtos_Type = Counter64
_ZxAnSwVlanInUnknownProtos_Object = MibTableColumn
zxAnSwVlanInUnknownProtos = _ZxAnSwVlanInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 36),
    _ZxAnSwVlanInUnknownProtos_Type()
)
zxAnSwVlanInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanInUnknownProtos.setStatus("current")
_ZxAnSwVlanOutUnknownProtos_Type = Counter64
_ZxAnSwVlanOutUnknownProtos_Object = MibTableColumn
zxAnSwVlanOutUnknownProtos = _ZxAnSwVlanOutUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 2, 1, 37),
    _ZxAnSwVlanOutUnknownProtos_Type()
)
zxAnSwVlanOutUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwVlanOutUnknownProtos.setStatus("current")
_ZxAnUserVlanPerfTable_Object = MibTable
zxAnUserVlanPerfTable = _ZxAnUserVlanPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3)
)
if mibBuilder.loadTexts:
    zxAnUserVlanPerfTable.setStatus("current")
_ZxAnUserVlanPerfEntry_Object = MibTableRow
zxAnUserVlanPerfEntry = _ZxAnUserVlanPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1)
)
zxAnUserVlanPerfEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-STATISTIC-MIB", "zxAnUserVlanPortIfIndex"),
    (0, "ZTE-AN-VLAN-STATISTIC-MIB", "zxAnUserVlanId"),
)
if mibBuilder.loadTexts:
    zxAnUserVlanPerfEntry.setStatus("current")
_ZxAnUserVlanPortIfIndex_Type = ZxAnIfindex
_ZxAnUserVlanPortIfIndex_Object = MibTableColumn
zxAnUserVlanPortIfIndex = _ZxAnUserVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 1),
    _ZxAnUserVlanPortIfIndex_Type()
)
zxAnUserVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnUserVlanPortIfIndex.setStatus("current")
_ZxAnUserVlanId_Type = VlanId
_ZxAnUserVlanId_Object = MibTableColumn
zxAnUserVlanId = _ZxAnUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 2),
    _ZxAnUserVlanId_Type()
)
zxAnUserVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnUserVlanId.setStatus("current")


class _ZxAnUserVlanPerfReset_Type(Integer32):
    """Custom type zxAnUserVlanPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("perfReset", 1)
    )


_ZxAnUserVlanPerfReset_Type.__name__ = "Integer32"
_ZxAnUserVlanPerfReset_Object = MibTableColumn
zxAnUserVlanPerfReset = _ZxAnUserVlanPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 3),
    _ZxAnUserVlanPerfReset_Type()
)
zxAnUserVlanPerfReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUserVlanPerfReset.setStatus("current")
_ZxAnUserVlanRxPkts_Type = Counter64
_ZxAnUserVlanRxPkts_Object = MibTableColumn
zxAnUserVlanRxPkts = _ZxAnUserVlanRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 4),
    _ZxAnUserVlanRxPkts_Type()
)
zxAnUserVlanRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxPkts.setStatus("current")
_ZxAnUserVlanTxPkts_Type = Counter64
_ZxAnUserVlanTxPkts_Object = MibTableColumn
zxAnUserVlanTxPkts = _ZxAnUserVlanTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 5),
    _ZxAnUserVlanTxPkts_Type()
)
zxAnUserVlanTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxPkts.setStatus("current")
_ZxAnUserVlanRxOctetRate_Type = Gauge32
_ZxAnUserVlanRxOctetRate_Object = MibTableColumn
zxAnUserVlanRxOctetRate = _ZxAnUserVlanRxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 6),
    _ZxAnUserVlanRxOctetRate_Type()
)
zxAnUserVlanRxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanRxOctetRate.setUnits("kbps")
_ZxAnUserVlanTxOctetRate_Type = Gauge32
_ZxAnUserVlanTxOctetRate_Object = MibTableColumn
zxAnUserVlanTxOctetRate = _ZxAnUserVlanTxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 7),
    _ZxAnUserVlanTxOctetRate_Type()
)
zxAnUserVlanTxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanTxOctetRate.setUnits("kbps")
_ZxAnUserVlanRxOctetPeakRate_Type = Gauge32
_ZxAnUserVlanRxOctetPeakRate_Object = MibTableColumn
zxAnUserVlanRxOctetPeakRate = _ZxAnUserVlanRxOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 8),
    _ZxAnUserVlanRxOctetPeakRate_Type()
)
zxAnUserVlanRxOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanRxOctetPeakRate.setUnits("kbps")
_ZxAnUserVlanTxOctetPeakRate_Type = Gauge32
_ZxAnUserVlanTxOctetPeakRate_Object = MibTableColumn
zxAnUserVlanTxOctetPeakRate = _ZxAnUserVlanTxOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 9),
    _ZxAnUserVlanTxOctetPeakRate_Type()
)
zxAnUserVlanTxOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanTxOctetPeakRate.setUnits("kbps")
_ZxAnUserVlanRxUcastPkts_Type = Counter64
_ZxAnUserVlanRxUcastPkts_Object = MibTableColumn
zxAnUserVlanRxUcastPkts = _ZxAnUserVlanRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 10),
    _ZxAnUserVlanRxUcastPkts_Type()
)
zxAnUserVlanRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxUcastPkts.setStatus("current")
_ZxAnUserVlanTxUcastPkts_Type = Counter64
_ZxAnUserVlanTxUcastPkts_Object = MibTableColumn
zxAnUserVlanTxUcastPkts = _ZxAnUserVlanTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 11),
    _ZxAnUserVlanTxUcastPkts_Type()
)
zxAnUserVlanTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxUcastPkts.setStatus("current")
_ZxAnUserVlanRxMulticastPkts_Type = Counter64
_ZxAnUserVlanRxMulticastPkts_Object = MibTableColumn
zxAnUserVlanRxMulticastPkts = _ZxAnUserVlanRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 12),
    _ZxAnUserVlanRxMulticastPkts_Type()
)
zxAnUserVlanRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxMulticastPkts.setStatus("current")
_ZxAnUserVlanTxMulticastPkts_Type = Counter64
_ZxAnUserVlanTxMulticastPkts_Object = MibTableColumn
zxAnUserVlanTxMulticastPkts = _ZxAnUserVlanTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 13),
    _ZxAnUserVlanTxMulticastPkts_Type()
)
zxAnUserVlanTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxMulticastPkts.setStatus("current")
_ZxAnUserVlanRxBroadcastPkts_Type = Counter64
_ZxAnUserVlanRxBroadcastPkts_Object = MibTableColumn
zxAnUserVlanRxBroadcastPkts = _ZxAnUserVlanRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 14),
    _ZxAnUserVlanRxBroadcastPkts_Type()
)
zxAnUserVlanRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxBroadcastPkts.setStatus("current")
_ZxAnUserVlanTxBroadcastPkts_Type = Counter64
_ZxAnUserVlanTxBroadcastPkts_Object = MibTableColumn
zxAnUserVlanTxBroadcastPkts = _ZxAnUserVlanTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 15),
    _ZxAnUserVlanTxBroadcastPkts_Type()
)
zxAnUserVlanTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxBroadcastPkts.setStatus("current")
_ZxAnUserVlanRxDiscards_Type = Counter64
_ZxAnUserVlanRxDiscards_Object = MibTableColumn
zxAnUserVlanRxDiscards = _ZxAnUserVlanRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 16),
    _ZxAnUserVlanRxDiscards_Type()
)
zxAnUserVlanRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxDiscards.setStatus("current")
_ZxAnUserVlanTxDiscards_Type = Counter64
_ZxAnUserVlanTxDiscards_Object = MibTableColumn
zxAnUserVlanTxDiscards = _ZxAnUserVlanTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 17),
    _ZxAnUserVlanTxDiscards_Type()
)
zxAnUserVlanTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxDiscards.setStatus("current")
_ZxAnUserVlanRxErrors_Type = Counter64
_ZxAnUserVlanRxErrors_Object = MibTableColumn
zxAnUserVlanRxErrors = _ZxAnUserVlanRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 18),
    _ZxAnUserVlanRxErrors_Type()
)
zxAnUserVlanRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxErrors.setStatus("current")
_ZxAnUserVlanTxErrors_Type = Counter64
_ZxAnUserVlanTxErrors_Object = MibTableColumn
zxAnUserVlanTxErrors = _ZxAnUserVlanTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 19),
    _ZxAnUserVlanTxErrors_Type()
)
zxAnUserVlanTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxErrors.setStatus("current")
_ZxAnUserVlanRxUcastOctetRate_Type = Gauge32
_ZxAnUserVlanRxUcastOctetRate_Object = MibTableColumn
zxAnUserVlanRxUcastOctetRate = _ZxAnUserVlanRxUcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 20),
    _ZxAnUserVlanRxUcastOctetRate_Type()
)
zxAnUserVlanRxUcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxUcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanRxUcastOctetRate.setUnits("kbps")
_ZxAnUserVlanTxUcastOctetRate_Type = Gauge32
_ZxAnUserVlanTxUcastOctetRate_Object = MibTableColumn
zxAnUserVlanTxUcastOctetRate = _ZxAnUserVlanTxUcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 21),
    _ZxAnUserVlanTxUcastOctetRate_Type()
)
zxAnUserVlanTxUcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxUcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanTxUcastOctetRate.setUnits("kbps")
_ZxAnUserVlanRxUcastOctetPeakRate_Type = Gauge32
_ZxAnUserVlanRxUcastOctetPeakRate_Object = MibTableColumn
zxAnUserVlanRxUcastOctetPeakRate = _ZxAnUserVlanRxUcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 22),
    _ZxAnUserVlanRxUcastOctetPeakRate_Type()
)
zxAnUserVlanRxUcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxUcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanRxUcastOctetPeakRate.setUnits("kbps")
_ZxAnUserVlanTxUcastOctetPeakRate_Type = Gauge32
_ZxAnUserVlanTxUcastOctetPeakRate_Object = MibTableColumn
zxAnUserVlanTxUcastOctetPeakRate = _ZxAnUserVlanTxUcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 23),
    _ZxAnUserVlanTxUcastOctetPeakRate_Type()
)
zxAnUserVlanTxUcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxUcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanTxUcastOctetPeakRate.setUnits("kbps")
_ZxAnUserVlanRxMcastOctetRate_Type = Gauge32
_ZxAnUserVlanRxMcastOctetRate_Object = MibTableColumn
zxAnUserVlanRxMcastOctetRate = _ZxAnUserVlanRxMcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 24),
    _ZxAnUserVlanRxMcastOctetRate_Type()
)
zxAnUserVlanRxMcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxMcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanRxMcastOctetRate.setUnits("kbps")
_ZxAnUserVlanTxMcastOctetRate_Type = Gauge32
_ZxAnUserVlanTxMcastOctetRate_Object = MibTableColumn
zxAnUserVlanTxMcastOctetRate = _ZxAnUserVlanTxMcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 25),
    _ZxAnUserVlanTxMcastOctetRate_Type()
)
zxAnUserVlanTxMcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxMcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanTxMcastOctetRate.setUnits("kbps")
_ZxAnUserVlanRxMcastOctetPeakRate_Type = Gauge32
_ZxAnUserVlanRxMcastOctetPeakRate_Object = MibTableColumn
zxAnUserVlanRxMcastOctetPeakRate = _ZxAnUserVlanRxMcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 26),
    _ZxAnUserVlanRxMcastOctetPeakRate_Type()
)
zxAnUserVlanRxMcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanRxMcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanRxMcastOctetPeakRate.setUnits("kbps")
_ZxAnUserVlanTxMcastOctetPeakRate_Type = Gauge32
_ZxAnUserVlanTxMcastOctetPeakRate_Object = MibTableColumn
zxAnUserVlanTxMcastOctetPeakRate = _ZxAnUserVlanTxMcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 27),
    _ZxAnUserVlanTxMcastOctetPeakRate_Type()
)
zxAnUserVlanTxMcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUserVlanTxMcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUserVlanTxMcastOctetPeakRate.setUnits("kbps")
_ZxAnUserVlanPerfRowStatus_Type = RowStatus
_ZxAnUserVlanPerfRowStatus_Object = MibTableColumn
zxAnUserVlanPerfRowStatus = _ZxAnUserVlanPerfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 3, 1, 100),
    _ZxAnUserVlanPerfRowStatus_Type()
)
zxAnUserVlanPerfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUserVlanPerfRowStatus.setStatus("current")
_ZxAnVlanStatTable_Object = MibTable
zxAnVlanStatTable = _ZxAnVlanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4)
)
if mibBuilder.loadTexts:
    zxAnVlanStatTable.setStatus("current")
_ZxAnVlanStatEntry_Object = MibTableRow
zxAnVlanStatEntry = _ZxAnVlanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1)
)
zxAnVlanStatEntry.setIndexNames(
    (0, "ZTE-AN-VLAN-STATISTIC-MIB", "zxAnSVlanId"),
    (0, "ZTE-AN-VLAN-STATISTIC-MIB", "zxAnCVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanStatEntry.setStatus("current")
_ZxAnSVlanId_Type = VlanId
_ZxAnSVlanId_Object = MibTableColumn
zxAnSVlanId = _ZxAnSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 1),
    _ZxAnSVlanId_Type()
)
zxAnSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSVlanId.setStatus("current")


class _ZxAnCVlanId_Type(Integer32):
    """Custom type zxAnCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnCVlanId_Type.__name__ = "Integer32"
_ZxAnCVlanId_Object = MibTableColumn
zxAnCVlanId = _ZxAnCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 2),
    _ZxAnCVlanId_Type()
)
zxAnCVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCVlanId.setStatus("current")
_ZxAnVlanRxOctets_Type = Counter64
_ZxAnVlanRxOctets_Object = MibTableColumn
zxAnVlanRxOctets = _ZxAnVlanRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 3),
    _ZxAnVlanRxOctets_Type()
)
zxAnVlanRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxOctets.setStatus("current")
_ZxAnVlanTxOctets_Type = Counter64
_ZxAnVlanTxOctets_Object = MibTableColumn
zxAnVlanTxOctets = _ZxAnVlanTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 4),
    _ZxAnVlanTxOctets_Type()
)
zxAnVlanTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxOctets.setStatus("current")
_ZxAnVlanRxPkts_Type = Counter64
_ZxAnVlanRxPkts_Object = MibTableColumn
zxAnVlanRxPkts = _ZxAnVlanRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 5),
    _ZxAnVlanRxPkts_Type()
)
zxAnVlanRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxPkts.setStatus("current")
_ZxAnVlanTxPkts_Type = Counter64
_ZxAnVlanTxPkts_Object = MibTableColumn
zxAnVlanTxPkts = _ZxAnVlanTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 6),
    _ZxAnVlanTxPkts_Type()
)
zxAnVlanTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxPkts.setStatus("current")
_ZxAnVlanRxPktRate_Type = Gauge32
_ZxAnVlanRxPktRate_Object = MibTableColumn
zxAnVlanRxPktRate = _ZxAnVlanRxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 7),
    _ZxAnVlanRxPktRate_Type()
)
zxAnVlanRxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxPktRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxPktRate.setUnits("pps")
_ZxAnVlanTxPktRate_Type = Gauge32
_ZxAnVlanTxPktRate_Object = MibTableColumn
zxAnVlanTxPktRate = _ZxAnVlanTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 8),
    _ZxAnVlanTxPktRate_Type()
)
zxAnVlanTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxPktRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxPktRate.setUnits("pps")
_ZxAnVlanRxDiscardPkts_Type = Counter64
_ZxAnVlanRxDiscardPkts_Object = MibTableColumn
zxAnVlanRxDiscardPkts = _ZxAnVlanRxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 9),
    _ZxAnVlanRxDiscardPkts_Type()
)
zxAnVlanRxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxDiscardPkts.setStatus("current")
_ZxAnVlanTxDiscardPkts_Type = Counter64
_ZxAnVlanTxDiscardPkts_Object = MibTableColumn
zxAnVlanTxDiscardPkts = _ZxAnVlanTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 10),
    _ZxAnVlanTxDiscardPkts_Type()
)
zxAnVlanTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxDiscardPkts.setStatus("current")
_ZxAnVlanLackOfBufferDiscards_Type = Counter64
_ZxAnVlanLackOfBufferDiscards_Object = MibTableColumn
zxAnVlanLackOfBufferDiscards = _ZxAnVlanLackOfBufferDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 11),
    _ZxAnVlanLackOfBufferDiscards_Type()
)
zxAnVlanLackOfBufferDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanLackOfBufferDiscards.setStatus("current")
_ZxAnVlanDelayExceededDiscards_Type = Counter64
_ZxAnVlanDelayExceededDiscards_Object = MibTableColumn
zxAnVlanDelayExceededDiscards = _ZxAnVlanDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 12),
    _ZxAnVlanDelayExceededDiscards_Type()
)
zxAnVlanDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanDelayExceededDiscards.setStatus("current")
_ZxAnVlanErrorDiscards_Type = Counter64
_ZxAnVlanErrorDiscards_Object = MibTableColumn
zxAnVlanErrorDiscards = _ZxAnVlanErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 13),
    _ZxAnVlanErrorDiscards_Type()
)
zxAnVlanErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanErrorDiscards.setStatus("current")
_ZxAnVlanIngressFilterDiscards_Type = Counter64
_ZxAnVlanIngressFilterDiscards_Object = MibTableColumn
zxAnVlanIngressFilterDiscards = _ZxAnVlanIngressFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 14),
    _ZxAnVlanIngressFilterDiscards_Type()
)
zxAnVlanIngressFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanIngressFilterDiscards.setStatus("current")
_ZxAnVlanRxOctetRate_Type = Gauge32
_ZxAnVlanRxOctetRate_Object = MibTableColumn
zxAnVlanRxOctetRate = _ZxAnVlanRxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 15),
    _ZxAnVlanRxOctetRate_Type()
)
zxAnVlanRxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxOctetRate.setUnits("kbps")
_ZxAnVlanTxOctetRate_Type = Gauge32
_ZxAnVlanTxOctetRate_Object = MibTableColumn
zxAnVlanTxOctetRate = _ZxAnVlanTxOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 16),
    _ZxAnVlanTxOctetRate_Type()
)
zxAnVlanTxOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxOctetRate.setUnits("kbps")
_ZxAnVlanRxOctetPeakRate_Type = Gauge32
_ZxAnVlanRxOctetPeakRate_Object = MibTableColumn
zxAnVlanRxOctetPeakRate = _ZxAnVlanRxOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 17),
    _ZxAnVlanRxOctetPeakRate_Type()
)
zxAnVlanRxOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxOctetPeakRate.setUnits("kbps")
_ZxAnVlanTxOctetPeakRate_Type = Gauge32
_ZxAnVlanTxOctetPeakRate_Object = MibTableColumn
zxAnVlanTxOctetPeakRate = _ZxAnVlanTxOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 18),
    _ZxAnVlanTxOctetPeakRate_Type()
)
zxAnVlanTxOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxOctetPeakRate.setUnits("kbps")
_ZxAnVlanRxUcastPkts_Type = Counter64
_ZxAnVlanRxUcastPkts_Object = MibTableColumn
zxAnVlanRxUcastPkts = _ZxAnVlanRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 19),
    _ZxAnVlanRxUcastPkts_Type()
)
zxAnVlanRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastPkts.setStatus("current")
_ZxAnVlanTxUcastPkts_Type = Counter64
_ZxAnVlanTxUcastPkts_Object = MibTableColumn
zxAnVlanTxUcastPkts = _ZxAnVlanTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 20),
    _ZxAnVlanTxUcastPkts_Type()
)
zxAnVlanTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastPkts.setStatus("current")
_ZxAnVlanRxUcastOctets_Type = Counter64
_ZxAnVlanRxUcastOctets_Object = MibTableColumn
zxAnVlanRxUcastOctets = _ZxAnVlanRxUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 21),
    _ZxAnVlanRxUcastOctets_Type()
)
zxAnVlanRxUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastOctets.setUnits("bytes")
_ZxAnVlanTxUcastOctets_Type = Counter64
_ZxAnVlanTxUcastOctets_Object = MibTableColumn
zxAnVlanTxUcastOctets = _ZxAnVlanTxUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 22),
    _ZxAnVlanTxUcastOctets_Type()
)
zxAnVlanTxUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastOctets.setUnits("bytes")
_ZxAnVlanRxUcastOctetRate_Type = Gauge32
_ZxAnVlanRxUcastOctetRate_Object = MibTableColumn
zxAnVlanRxUcastOctetRate = _ZxAnVlanRxUcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 23),
    _ZxAnVlanRxUcastOctetRate_Type()
)
zxAnVlanRxUcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastOctetRate.setUnits("kbps")
_ZxAnVlanTxUcastOctetRate_Type = Gauge32
_ZxAnVlanTxUcastOctetRate_Object = MibTableColumn
zxAnVlanTxUcastOctetRate = _ZxAnVlanTxUcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 24),
    _ZxAnVlanTxUcastOctetRate_Type()
)
zxAnVlanTxUcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastOctetRate.setUnits("kbps")
_ZxAnVlanRxUcastOctetPeakRate_Type = Gauge32
_ZxAnVlanRxUcastOctetPeakRate_Object = MibTableColumn
zxAnVlanRxUcastOctetPeakRate = _ZxAnVlanRxUcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 25),
    _ZxAnVlanRxUcastOctetPeakRate_Type()
)
zxAnVlanRxUcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxUcastOctetPeakRate.setUnits("kbps")
_ZxAnVlanTxUcastOctetPeakRate_Type = Gauge32
_ZxAnVlanTxUcastOctetPeakRate_Object = MibTableColumn
zxAnVlanTxUcastOctetPeakRate = _ZxAnVlanTxUcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 26),
    _ZxAnVlanTxUcastOctetPeakRate_Type()
)
zxAnVlanTxUcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxUcastOctetPeakRate.setUnits("kbps")
_ZxAnVlanRxMcastPkts_Type = Counter64
_ZxAnVlanRxMcastPkts_Object = MibTableColumn
zxAnVlanRxMcastPkts = _ZxAnVlanRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 27),
    _ZxAnVlanRxMcastPkts_Type()
)
zxAnVlanRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastPkts.setStatus("current")
_ZxAnVlanTxMcastPkts_Type = Counter64
_ZxAnVlanTxMcastPkts_Object = MibTableColumn
zxAnVlanTxMcastPkts = _ZxAnVlanTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 28),
    _ZxAnVlanTxMcastPkts_Type()
)
zxAnVlanTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastPkts.setStatus("current")
_ZxAnVlanRxMcastOctets_Type = Counter64
_ZxAnVlanRxMcastOctets_Object = MibTableColumn
zxAnVlanRxMcastOctets = _ZxAnVlanRxMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 29),
    _ZxAnVlanRxMcastOctets_Type()
)
zxAnVlanRxMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastOctets.setUnits("bytes")
_ZxAnVlanTxMcastOctets_Type = Counter64
_ZxAnVlanTxMcastOctets_Object = MibTableColumn
zxAnVlanTxMcastOctets = _ZxAnVlanTxMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 30),
    _ZxAnVlanTxMcastOctets_Type()
)
zxAnVlanTxMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastOctets.setUnits("bytes")
_ZxAnVlanRxMcastOctetRate_Type = Gauge32
_ZxAnVlanRxMcastOctetRate_Object = MibTableColumn
zxAnVlanRxMcastOctetRate = _ZxAnVlanRxMcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 31),
    _ZxAnVlanRxMcastOctetRate_Type()
)
zxAnVlanRxMcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastOctetRate.setUnits("kbps")
_ZxAnVlanTxMcastOctetRate_Type = Gauge32
_ZxAnVlanTxMcastOctetRate_Object = MibTableColumn
zxAnVlanTxMcastOctetRate = _ZxAnVlanTxMcastOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 32),
    _ZxAnVlanTxMcastOctetRate_Type()
)
zxAnVlanTxMcastOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastOctetRate.setUnits("kbps")
_ZxAnVlanRxMcastOctetPeakRate_Type = Gauge32
_ZxAnVlanRxMcastOctetPeakRate_Object = MibTableColumn
zxAnVlanRxMcastOctetPeakRate = _ZxAnVlanRxMcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 33),
    _ZxAnVlanRxMcastOctetPeakRate_Type()
)
zxAnVlanRxMcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxMcastOctetPeakRate.setUnits("kbps")
_ZxAnVlanTxMcastOctetPeakRate_Type = Gauge32
_ZxAnVlanTxMcastOctetPeakRate_Object = MibTableColumn
zxAnVlanTxMcastOctetPeakRate = _ZxAnVlanTxMcastOctetPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 34),
    _ZxAnVlanTxMcastOctetPeakRate_Type()
)
zxAnVlanTxMcastOctetPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastOctetPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxMcastOctetPeakRate.setUnits("kbps")
_ZxAnVlanRxBcastPkts_Type = Counter64
_ZxAnVlanRxBcastPkts_Object = MibTableColumn
zxAnVlanRxBcastPkts = _ZxAnVlanRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 35),
    _ZxAnVlanRxBcastPkts_Type()
)
zxAnVlanRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxBcastPkts.setStatus("current")
_ZxAnVlanTxBcastPkts_Type = Counter64
_ZxAnVlanTxBcastPkts_Object = MibTableColumn
zxAnVlanTxBcastPkts = _ZxAnVlanTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 36),
    _ZxAnVlanTxBcastPkts_Type()
)
zxAnVlanTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxBcastPkts.setStatus("current")
_ZxAnVlanRxBcastOctets_Type = Counter64
_ZxAnVlanRxBcastOctets_Object = MibTableColumn
zxAnVlanRxBcastOctets = _ZxAnVlanRxBcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 37),
    _ZxAnVlanRxBcastOctets_Type()
)
zxAnVlanRxBcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxBcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxBcastOctets.setUnits("bytes")
_ZxAnVlanTxBcastOctets_Type = Counter64
_ZxAnVlanTxBcastOctets_Object = MibTableColumn
zxAnVlanTxBcastOctets = _ZxAnVlanTxBcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 38),
    _ZxAnVlanTxBcastOctets_Type()
)
zxAnVlanTxBcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxBcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxBcastOctets.setUnits("bytes")
_ZxAnVlanRxFloodPkts_Type = Counter64
_ZxAnVlanRxFloodPkts_Object = MibTableColumn
zxAnVlanRxFloodPkts = _ZxAnVlanRxFloodPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 39),
    _ZxAnVlanRxFloodPkts_Type()
)
zxAnVlanRxFloodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxFloodPkts.setStatus("current")
_ZxAnVlanTxFloodPkts_Type = Counter64
_ZxAnVlanTxFloodPkts_Object = MibTableColumn
zxAnVlanTxFloodPkts = _ZxAnVlanTxFloodPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 40),
    _ZxAnVlanTxFloodPkts_Type()
)
zxAnVlanTxFloodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxFloodPkts.setStatus("current")
_ZxAnVlanRxFloodOctets_Type = Counter64
_ZxAnVlanRxFloodOctets_Object = MibTableColumn
zxAnVlanRxFloodOctets = _ZxAnVlanRxFloodOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 41),
    _ZxAnVlanRxFloodOctets_Type()
)
zxAnVlanRxFloodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanRxFloodOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanRxFloodOctets.setUnits("bytes")
_ZxAnVlanTxFloodOctets_Type = Counter64
_ZxAnVlanTxFloodOctets_Object = MibTableColumn
zxAnVlanTxFloodOctets = _ZxAnVlanTxFloodOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 42),
    _ZxAnVlanTxFloodOctets_Type()
)
zxAnVlanTxFloodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVlanTxFloodOctets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVlanTxFloodOctets.setUnits("bytes")
_ZxAnVlanStatRowStatus_Type = RowStatus
_ZxAnVlanStatRowStatus_Object = MibTableColumn
zxAnVlanStatRowStatus = _ZxAnVlanStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 191, 4, 1, 101),
    _ZxAnVlanStatRowStatus_Type()
)
zxAnVlanStatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanStatRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VLAN-STATISTIC-MIB",
    **{"zxAnVlanStatisticMib": zxAnVlanStatisticMib,
       "zxAnVlanPerfEnableTable": zxAnVlanPerfEnableTable,
       "zxAnVlanPerfEnableEntry": zxAnVlanPerfEnableEntry,
       "zxAnEnVlanId": zxAnEnVlanId,
       "zxVlanPerfEnable": zxVlanPerfEnable,
       "zxVlanIDAllEnable": zxVlanIDAllEnable,
       "zxAnSwVlanPerfTable": zxAnSwVlanPerfTable,
       "zxAnSwVlanPerfEntry": zxAnSwVlanPerfEntry,
       "zxAnSwVlanId": zxAnSwVlanId,
       "zxAnSwVlanInOctets": zxAnSwVlanInOctets,
       "zxAnSwVlanOutOctets": zxAnSwVlanOutOctets,
       "zxAnSwVlanInPkts": zxAnSwVlanInPkts,
       "zxAnSwVlanOutPkts": zxAnSwVlanOutPkts,
       "zxAnSwVlanInBandwidth": zxAnSwVlanInBandwidth,
       "zxAnSwVlanOutBandwidth": zxAnSwVlanOutBandwidth,
       "zxAnSwVlanInBandwidthUtility": zxAnSwVlanInBandwidthUtility,
       "zxAnSwVlanOutBandwidthUtility": zxAnSwVlanOutBandwidthUtility,
       "zxAnSwVlanInCurrOctetRate": zxAnSwVlanInCurrOctetRate,
       "zxAnSwVlanOutCurrOctetRate": zxAnSwVlanOutCurrOctetRate,
       "zxAnSwVlanInCurrPktRate": zxAnSwVlanInCurrPktRate,
       "zxAnSwVlanOutCurrPktRate": zxAnSwVlanOutCurrPktRate,
       "zxAnSwVlanInUcastPkts": zxAnSwVlanInUcastPkts,
       "zxAnSwVlanOutUcastPkts": zxAnSwVlanOutUcastPkts,
       "zxAnSwVlanInMulticastPkts": zxAnSwVlanInMulticastPkts,
       "zxAnSwVlanOutMulticastPkts": zxAnSwVlanOutMulticastPkts,
       "zxAnSwVlanInNUcastPkts": zxAnSwVlanInNUcastPkts,
       "zxAnSwVlanOutNUcastPkts": zxAnSwVlanOutNUcastPkts,
       "zxAnSwVlanInBroadcastPkts": zxAnSwVlanInBroadcastPkts,
       "zxAnSwVlanOutBroadcastPkts": zxAnSwVlanOutBroadcastPkts,
       "zxAnSwVlanInDiscards": zxAnSwVlanInDiscards,
       "zxAnSwVlanOutDiscards": zxAnSwVlanOutDiscards,
       "zxAnSwVlanInUndersizePkts": zxAnSwVlanInUndersizePkts,
       "zxAnSwVlanOutUndersizePkts": zxAnSwVlanOutUndersizePkts,
       "zxAnSwVlanInOversizePkts": zxAnSwVlanInOversizePkts,
       "zxAnSwVlanOutOversizePkts": zxAnSwVlanOutOversizePkts,
       "zxAnSwVlanInCRCAlignErrors": zxAnSwVlanInCRCAlignErrors,
       "zxAnSwVlanOutCRCAlignErrors": zxAnSwVlanOutCRCAlignErrors,
       "zxAnSwVlanInFragments": zxAnSwVlanInFragments,
       "zxAnSwVlanOutFragments": zxAnSwVlanOutFragments,
       "zxAnSwVlanInJabbers": zxAnSwVlanInJabbers,
       "zxAnSwVlanOutJabbers": zxAnSwVlanOutJabbers,
       "zxAnSwVlanInCollisions": zxAnSwVlanInCollisions,
       "zxAnSwVlanOutCollisions": zxAnSwVlanOutCollisions,
       "zxAnSwVlanInUnknownProtos": zxAnSwVlanInUnknownProtos,
       "zxAnSwVlanOutUnknownProtos": zxAnSwVlanOutUnknownProtos,
       "zxAnUserVlanPerfTable": zxAnUserVlanPerfTable,
       "zxAnUserVlanPerfEntry": zxAnUserVlanPerfEntry,
       "zxAnUserVlanPortIfIndex": zxAnUserVlanPortIfIndex,
       "zxAnUserVlanId": zxAnUserVlanId,
       "zxAnUserVlanPerfReset": zxAnUserVlanPerfReset,
       "zxAnUserVlanRxPkts": zxAnUserVlanRxPkts,
       "zxAnUserVlanTxPkts": zxAnUserVlanTxPkts,
       "zxAnUserVlanRxOctetRate": zxAnUserVlanRxOctetRate,
       "zxAnUserVlanTxOctetRate": zxAnUserVlanTxOctetRate,
       "zxAnUserVlanRxOctetPeakRate": zxAnUserVlanRxOctetPeakRate,
       "zxAnUserVlanTxOctetPeakRate": zxAnUserVlanTxOctetPeakRate,
       "zxAnUserVlanRxUcastPkts": zxAnUserVlanRxUcastPkts,
       "zxAnUserVlanTxUcastPkts": zxAnUserVlanTxUcastPkts,
       "zxAnUserVlanRxMulticastPkts": zxAnUserVlanRxMulticastPkts,
       "zxAnUserVlanTxMulticastPkts": zxAnUserVlanTxMulticastPkts,
       "zxAnUserVlanRxBroadcastPkts": zxAnUserVlanRxBroadcastPkts,
       "zxAnUserVlanTxBroadcastPkts": zxAnUserVlanTxBroadcastPkts,
       "zxAnUserVlanRxDiscards": zxAnUserVlanRxDiscards,
       "zxAnUserVlanTxDiscards": zxAnUserVlanTxDiscards,
       "zxAnUserVlanRxErrors": zxAnUserVlanRxErrors,
       "zxAnUserVlanTxErrors": zxAnUserVlanTxErrors,
       "zxAnUserVlanRxUcastOctetRate": zxAnUserVlanRxUcastOctetRate,
       "zxAnUserVlanTxUcastOctetRate": zxAnUserVlanTxUcastOctetRate,
       "zxAnUserVlanRxUcastOctetPeakRate": zxAnUserVlanRxUcastOctetPeakRate,
       "zxAnUserVlanTxUcastOctetPeakRate": zxAnUserVlanTxUcastOctetPeakRate,
       "zxAnUserVlanRxMcastOctetRate": zxAnUserVlanRxMcastOctetRate,
       "zxAnUserVlanTxMcastOctetRate": zxAnUserVlanTxMcastOctetRate,
       "zxAnUserVlanRxMcastOctetPeakRate": zxAnUserVlanRxMcastOctetPeakRate,
       "zxAnUserVlanTxMcastOctetPeakRate": zxAnUserVlanTxMcastOctetPeakRate,
       "zxAnUserVlanPerfRowStatus": zxAnUserVlanPerfRowStatus,
       "zxAnVlanStatTable": zxAnVlanStatTable,
       "zxAnVlanStatEntry": zxAnVlanStatEntry,
       "zxAnSVlanId": zxAnSVlanId,
       "zxAnCVlanId": zxAnCVlanId,
       "zxAnVlanRxOctets": zxAnVlanRxOctets,
       "zxAnVlanTxOctets": zxAnVlanTxOctets,
       "zxAnVlanRxPkts": zxAnVlanRxPkts,
       "zxAnVlanTxPkts": zxAnVlanTxPkts,
       "zxAnVlanRxPktRate": zxAnVlanRxPktRate,
       "zxAnVlanTxPktRate": zxAnVlanTxPktRate,
       "zxAnVlanRxDiscardPkts": zxAnVlanRxDiscardPkts,
       "zxAnVlanTxDiscardPkts": zxAnVlanTxDiscardPkts,
       "zxAnVlanLackOfBufferDiscards": zxAnVlanLackOfBufferDiscards,
       "zxAnVlanDelayExceededDiscards": zxAnVlanDelayExceededDiscards,
       "zxAnVlanErrorDiscards": zxAnVlanErrorDiscards,
       "zxAnVlanIngressFilterDiscards": zxAnVlanIngressFilterDiscards,
       "zxAnVlanRxOctetRate": zxAnVlanRxOctetRate,
       "zxAnVlanTxOctetRate": zxAnVlanTxOctetRate,
       "zxAnVlanRxOctetPeakRate": zxAnVlanRxOctetPeakRate,
       "zxAnVlanTxOctetPeakRate": zxAnVlanTxOctetPeakRate,
       "zxAnVlanRxUcastPkts": zxAnVlanRxUcastPkts,
       "zxAnVlanTxUcastPkts": zxAnVlanTxUcastPkts,
       "zxAnVlanRxUcastOctets": zxAnVlanRxUcastOctets,
       "zxAnVlanTxUcastOctets": zxAnVlanTxUcastOctets,
       "zxAnVlanRxUcastOctetRate": zxAnVlanRxUcastOctetRate,
       "zxAnVlanTxUcastOctetRate": zxAnVlanTxUcastOctetRate,
       "zxAnVlanRxUcastOctetPeakRate": zxAnVlanRxUcastOctetPeakRate,
       "zxAnVlanTxUcastOctetPeakRate": zxAnVlanTxUcastOctetPeakRate,
       "zxAnVlanRxMcastPkts": zxAnVlanRxMcastPkts,
       "zxAnVlanTxMcastPkts": zxAnVlanTxMcastPkts,
       "zxAnVlanRxMcastOctets": zxAnVlanRxMcastOctets,
       "zxAnVlanTxMcastOctets": zxAnVlanTxMcastOctets,
       "zxAnVlanRxMcastOctetRate": zxAnVlanRxMcastOctetRate,
       "zxAnVlanTxMcastOctetRate": zxAnVlanTxMcastOctetRate,
       "zxAnVlanRxMcastOctetPeakRate": zxAnVlanRxMcastOctetPeakRate,
       "zxAnVlanTxMcastOctetPeakRate": zxAnVlanTxMcastOctetPeakRate,
       "zxAnVlanRxBcastPkts": zxAnVlanRxBcastPkts,
       "zxAnVlanTxBcastPkts": zxAnVlanTxBcastPkts,
       "zxAnVlanRxBcastOctets": zxAnVlanRxBcastOctets,
       "zxAnVlanTxBcastOctets": zxAnVlanTxBcastOctets,
       "zxAnVlanRxFloodPkts": zxAnVlanRxFloodPkts,
       "zxAnVlanTxFloodPkts": zxAnVlanTxFloodPkts,
       "zxAnVlanRxFloodOctets": zxAnVlanRxFloodOctets,
       "zxAnVlanTxFloodOctets": zxAnVlanTxFloodOctets,
       "zxAnVlanStatRowStatus": zxAnVlanStatRowStatus}
)
