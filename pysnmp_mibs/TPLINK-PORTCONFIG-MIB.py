# SNMP MIB module (TPLINK-PORTCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-PORTCONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:56:35 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkPortConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8)
)
if mibBuilder.loadTexts:
    tplinkPortConfigMIB.setRevisions(
        ("2012-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPortConfigMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPortConfigMIBObjects = _TplinkPortConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1)
)
_TpPortConfigTable_Object = MibTable
tpPortConfigTable = _TpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tpPortConfigTable.setStatus("current")


class _TpPortConfigJumbo_Type(Integer32):
    """Custom type tpPortConfigJumbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9216),
    )


_TpPortConfigJumbo_Type.__name__ = "Integer32"
_TpPortConfigJumbo_Object = MibScalar
tpPortConfigJumbo = _TpPortConfigJumbo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 1),
    _TpPortConfigJumbo_Type()
)
tpPortConfigJumbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigJumbo.setStatus("current")
_TpPortConfigEntry_Object = MibTableRow
tpPortConfigEntry = _TpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2)
)
tpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPortConfigEntry.setStatus("current")
_TpPortConfigDescription_Type = DisplayString
_TpPortConfigDescription_Object = MibTableColumn
tpPortConfigDescription = _TpPortConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2, 2),
    _TpPortConfigDescription_Type()
)
tpPortConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigDescription.setStatus("current")


class _TpPortConfigStatus_Type(Integer32):
    """Custom type tpPortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPortConfigStatus_Type.__name__ = "Integer32"
_TpPortConfigStatus_Object = MibTableColumn
tpPortConfigStatus = _TpPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2, 3),
    _TpPortConfigStatus_Type()
)
tpPortConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigStatus.setStatus("current")


class _TpPortConfigSpeed_Type(Integer32):
    """Custom type tpPortConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("speed-10Mbps", 0),
          ("speed-100Mbps", 1),
          ("speed-1Gigabps", 2),
          ("speed-10Gigabps", 3),
          ("auto", 4))
    )


_TpPortConfigSpeed_Type.__name__ = "Integer32"
_TpPortConfigSpeed_Object = MibTableColumn
tpPortConfigSpeed = _TpPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2, 4),
    _TpPortConfigSpeed_Type()
)
tpPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigSpeed.setStatus("current")


class _TpPortConfigDuplex_Type(Integer32):
    """Custom type tpPortConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1),
          ("auto", 2))
    )


_TpPortConfigDuplex_Type.__name__ = "Integer32"
_TpPortConfigDuplex_Object = MibTableColumn
tpPortConfigDuplex = _TpPortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2, 5),
    _TpPortConfigDuplex_Type()
)
tpPortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigDuplex.setStatus("current")


class _TpPortConfigFlowCtrl_Type(Integer32):
    """Custom type tpPortConfigFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPortConfigFlowCtrl_Type.__name__ = "Integer32"
_TpPortConfigFlowCtrl_Object = MibTableColumn
tpPortConfigFlowCtrl = _TpPortConfigFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2, 6),
    _TpPortConfigFlowCtrl_Type()
)
tpPortConfigFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortConfigFlowCtrl.setStatus("current")
_TpPortConfigLAG_Type = DisplayString
_TpPortConfigLAG_Object = MibTableColumn
tpPortConfigLAG = _TpPortConfigLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 1, 2, 7),
    _TpPortConfigLAG_Type()
)
tpPortConfigLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortConfigLAG.setStatus("current")
_TpPortCableTestTable_Object = MibTable
tpPortCableTestTable = _TpPortCableTestTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2)
)
if mibBuilder.loadTexts:
    tpPortCableTestTable.setStatus("current")
_TpPortCableTestEntry_Object = MibTableRow
tpPortCableTestEntry = _TpPortCableTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1)
)
tpPortCableTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPortCableTestEntry.setStatus("current")
_TpPairAStatus_Type = DisplayString
_TpPairAStatus_Object = MibTableColumn
tpPairAStatus = _TpPairAStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 2),
    _TpPairAStatus_Type()
)
tpPairAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairAStatus.setStatus("current")
_TpPairALength_Type = DisplayString
_TpPairALength_Object = MibTableColumn
tpPairALength = _TpPairALength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 3),
    _TpPairALength_Type()
)
tpPairALength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairALength.setStatus("current")
_TpPairBStatus_Type = DisplayString
_TpPairBStatus_Object = MibTableColumn
tpPairBStatus = _TpPairBStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 4),
    _TpPairBStatus_Type()
)
tpPairBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairBStatus.setStatus("current")
_TpPairBLength_Type = DisplayString
_TpPairBLength_Object = MibTableColumn
tpPairBLength = _TpPairBLength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 5),
    _TpPairBLength_Type()
)
tpPairBLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairBLength.setStatus("current")
_TpPairCStatus_Type = DisplayString
_TpPairCStatus_Object = MibTableColumn
tpPairCStatus = _TpPairCStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 6),
    _TpPairCStatus_Type()
)
tpPairCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairCStatus.setStatus("current")
_TpPairCLength_Type = DisplayString
_TpPairCLength_Object = MibTableColumn
tpPairCLength = _TpPairCLength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 7),
    _TpPairCLength_Type()
)
tpPairCLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairCLength.setStatus("current")
_TpPairDStatus_Type = DisplayString
_TpPairDStatus_Object = MibTableColumn
tpPairDStatus = _TpPairDStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 8),
    _TpPairDStatus_Type()
)
tpPairDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairDStatus.setStatus("current")
_TpPairDLength_Type = DisplayString
_TpPairDLength_Object = MibTableColumn
tpPairDLength = _TpPairDLength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 2, 1, 9),
    _TpPairDLength_Type()
)
tpPairDLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairDLength.setStatus("current")
_TpPortCableTestCFTable_Object = MibTable
tpPortCableTestCFTable = _TpPortCableTestCFTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3)
)
if mibBuilder.loadTexts:
    tpPortCableTestCFTable.setStatus("current")
_TpPortCableTestFlush_Type = DisplayString
_TpPortCableTestFlush_Object = MibScalar
tpPortCableTestFlush = _TpPortCableTestFlush_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 1),
    _TpPortCableTestFlush_Type()
)
tpPortCableTestFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortCableTestFlush.setStatus("current")
_TpPortCableTestCFEntry_Object = MibTableRow
tpPortCableTestCFEntry = _TpPortCableTestCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2)
)
tpPortCableTestCFEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPortCableTestCFEntry.setStatus("current")
_TpPairAStatusCF_Type = DisplayString
_TpPairAStatusCF_Object = MibTableColumn
tpPairAStatusCF = _TpPairAStatusCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 2),
    _TpPairAStatusCF_Type()
)
tpPairAStatusCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairAStatusCF.setStatus("current")
_TpPairALengthCF_Type = DisplayString
_TpPairALengthCF_Object = MibTableColumn
tpPairALengthCF = _TpPairALengthCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 3),
    _TpPairALengthCF_Type()
)
tpPairALengthCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairALengthCF.setStatus("current")
_TpPairBStatusCF_Type = DisplayString
_TpPairBStatusCF_Object = MibTableColumn
tpPairBStatusCF = _TpPairBStatusCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 4),
    _TpPairBStatusCF_Type()
)
tpPairBStatusCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairBStatusCF.setStatus("current")
_TpPairBLengthCF_Type = DisplayString
_TpPairBLengthCF_Object = MibTableColumn
tpPairBLengthCF = _TpPairBLengthCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 5),
    _TpPairBLengthCF_Type()
)
tpPairBLengthCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairBLengthCF.setStatus("current")
_TpPairCStatusCF_Type = DisplayString
_TpPairCStatusCF_Object = MibTableColumn
tpPairCStatusCF = _TpPairCStatusCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 6),
    _TpPairCStatusCF_Type()
)
tpPairCStatusCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairCStatusCF.setStatus("current")
_TpPairCLengthCF_Type = DisplayString
_TpPairCLengthCF_Object = MibTableColumn
tpPairCLengthCF = _TpPairCLengthCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 7),
    _TpPairCLengthCF_Type()
)
tpPairCLengthCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairCLengthCF.setStatus("current")
_TpPairDStatusCF_Type = DisplayString
_TpPairDStatusCF_Object = MibTableColumn
tpPairDStatusCF = _TpPairDStatusCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 8),
    _TpPairDStatusCF_Type()
)
tpPairDStatusCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairDStatusCF.setStatus("current")
_TpPairDLengthCF_Type = DisplayString
_TpPairDLengthCF_Object = MibTableColumn
tpPairDLengthCF = _TpPairDLengthCF_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 3, 2, 9),
    _TpPairDLengthCF_Type()
)
tpPairDLengthCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPairDLengthCF.setStatus("current")
_TpPortTrafficMonitorTable_Object = MibTable
tpPortTrafficMonitorTable = _TpPortTrafficMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4)
)
if mibBuilder.loadTexts:
    tpPortTrafficMonitorTable.setStatus("current")
_TpPortTrafficMonitorEntry_Object = MibTableRow
tpPortTrafficMonitorEntry = _TpPortTrafficMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1)
)
tpPortTrafficMonitorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpPortTrafficMonitorEntry.setStatus("current")
_TpPortRxPkts_Type = Counter64
_TpPortRxPkts_Object = MibTableColumn
tpPortRxPkts = _TpPortRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 2),
    _TpPortRxPkts_Type()
)
tpPortRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxPkts.setStatus("current")
_TpPortRxBytes_Type = Counter64
_TpPortRxBytes_Object = MibTableColumn
tpPortRxBytes = _TpPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 3),
    _TpPortRxBytes_Type()
)
tpPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxBytes.setStatus("current")
_TpPortRxUcast_Type = Counter64
_TpPortRxUcast_Object = MibTableColumn
tpPortRxUcast = _TpPortRxUcast_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 4),
    _TpPortRxUcast_Type()
)
tpPortRxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxUcast.setStatus("current")
_TpPortRxMcast_Type = Counter64
_TpPortRxMcast_Object = MibTableColumn
tpPortRxMcast = _TpPortRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 5),
    _TpPortRxMcast_Type()
)
tpPortRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxMcast.setStatus("current")
_TpPortRxBcast_Type = Counter64
_TpPortRxBcast_Object = MibTableColumn
tpPortRxBcast = _TpPortRxBcast_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 6),
    _TpPortRxBcast_Type()
)
tpPortRxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxBcast.setStatus("current")
_TpPortRxJumbo_Type = Counter64
_TpPortRxJumbo_Object = MibTableColumn
tpPortRxJumbo = _TpPortRxJumbo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 7),
    _TpPortRxJumbo_Type()
)
tpPortRxJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxJumbo.setStatus("current")
_TpPortRxAlignment_Type = Counter64
_TpPortRxAlignment_Object = MibTableColumn
tpPortRxAlignment = _TpPortRxAlignment_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 8),
    _TpPortRxAlignment_Type()
)
tpPortRxAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxAlignment.setStatus("current")
_TpPortRxUnderSize_Type = Counter64
_TpPortRxUnderSize_Object = MibTableColumn
tpPortRxUnderSize = _TpPortRxUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 9),
    _TpPortRxUnderSize_Type()
)
tpPortRxUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxUnderSize.setStatus("current")
_TpPortRx64Pkts_Type = Counter64
_TpPortRx64Pkts_Object = MibTableColumn
tpPortRx64Pkts = _TpPortRx64Pkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 10),
    _TpPortRx64Pkts_Type()
)
tpPortRx64Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRx64Pkts.setStatus("current")
_TpPortRx65_127Pkts_Type = Counter64
_TpPortRx65_127Pkts_Object = MibTableColumn
tpPortRx65_127Pkts = _TpPortRx65_127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 11),
    _TpPortRx65_127Pkts_Type()
)
tpPortRx65_127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRx65_127Pkts.setStatus("current")
_TpPortRx128_255Pkts_Type = Counter64
_TpPortRx128_255Pkts_Object = MibTableColumn
tpPortRx128_255Pkts = _TpPortRx128_255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 12),
    _TpPortRx128_255Pkts_Type()
)
tpPortRx128_255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRx128_255Pkts.setStatus("current")
_TpPortRx256_511Pkts_Type = Counter64
_TpPortRx256_511Pkts_Object = MibTableColumn
tpPortRx256_511Pkts = _TpPortRx256_511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 13),
    _TpPortRx256_511Pkts_Type()
)
tpPortRx256_511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRx256_511Pkts.setStatus("current")
_TpPortRx512_1023Pkts_Type = Counter64
_TpPortRx512_1023Pkts_Object = MibTableColumn
tpPortRx512_1023Pkts = _TpPortRx512_1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 14),
    _TpPortRx512_1023Pkts_Type()
)
tpPortRx512_1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRx512_1023Pkts.setStatus("current")
_TpPortRxOver1023Pkts_Type = Counter64
_TpPortRxOver1023Pkts_Object = MibTableColumn
tpPortRxOver1023Pkts = _TpPortRxOver1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 15),
    _TpPortRxOver1023Pkts_Type()
)
tpPortRxOver1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortRxOver1023Pkts.setStatus("current")
_TpPortTxPkts_Type = Counter64
_TpPortTxPkts_Object = MibTableColumn
tpPortTxPkts = _TpPortTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 16),
    _TpPortTxPkts_Type()
)
tpPortTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxPkts.setStatus("current")
_TpPortTxBytes_Type = Counter64
_TpPortTxBytes_Object = MibTableColumn
tpPortTxBytes = _TpPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 17),
    _TpPortTxBytes_Type()
)
tpPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxBytes.setStatus("current")
_TpPortTxUcast_Type = Counter64
_TpPortTxUcast_Object = MibTableColumn
tpPortTxUcast = _TpPortTxUcast_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 18),
    _TpPortTxUcast_Type()
)
tpPortTxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxUcast.setStatus("current")
_TpPortTxMcast_Type = Counter64
_TpPortTxMcast_Object = MibTableColumn
tpPortTxMcast = _TpPortTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 19),
    _TpPortTxMcast_Type()
)
tpPortTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxMcast.setStatus("current")
_TpPortTxBcast_Type = Counter64
_TpPortTxBcast_Object = MibTableColumn
tpPortTxBcast = _TpPortTxBcast_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 20),
    _TpPortTxBcast_Type()
)
tpPortTxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxBcast.setStatus("current")
_TpPortTxJumbo_Type = Counter64
_TpPortTxJumbo_Object = MibTableColumn
tpPortTxJumbo = _TpPortTxJumbo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 21),
    _TpPortTxJumbo_Type()
)
tpPortTxJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxJumbo.setStatus("current")
_TpPortTxCollisions_Type = Counter64
_TpPortTxCollisions_Object = MibTableColumn
tpPortTxCollisions = _TpPortTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 22),
    _TpPortTxCollisions_Type()
)
tpPortTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPortTxCollisions.setStatus("current")


class _TpPortTrafficMonitorClear_Type(Integer32):
    """Custom type tpPortTrafficMonitorClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("clear", 2))
    )


_TpPortTrafficMonitorClear_Type.__name__ = "Integer32"
_TpPortTrafficMonitorClear_Object = MibTableColumn
tpPortTrafficMonitorClear = _TpPortTrafficMonitorClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 4, 1, 23),
    _TpPortTrafficMonitorClear_Type()
)
tpPortTrafficMonitorClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPortTrafficMonitorClear.setStatus("current")
_TpEEETable_Object = MibTable
tpEEETable = _TpEEETable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 5)
)
if mibBuilder.loadTexts:
    tpEEETable.setStatus("current")
_TpEEEEntry_Object = MibTableRow
tpEEEEntry = _TpEEEEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 5, 1)
)
tpEEEEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpEEEEntry.setStatus("current")
_TpEEEPort_Type = DisplayString
_TpEEEPort_Object = MibTableColumn
tpEEEPort = _TpEEEPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 5, 1, 1),
    _TpEEEPort_Type()
)
tpEEEPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpEEEPort.setStatus("current")


class _TpEEEStatus_Type(Integer32):
    """Custom type tpEEEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpEEEStatus_Type.__name__ = "Integer32"
_TpEEEStatus_Object = MibTableColumn
tpEEEStatus = _TpEEEStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 5, 1, 2),
    _TpEEEStatus_Type()
)
tpEEEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpEEEStatus.setStatus("current")
_TpEEEPortLag_Type = DisplayString
_TpEEEPortLag_Object = MibTableColumn
tpEEEPortLag = _TpEEEPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 1, 5, 1, 3),
    _TpEEEPortLag_Type()
)
tpEEEPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpEEEPortLag.setStatus("current")
_TplinkPortConfigNotifications_ObjectIdentity = ObjectIdentity
tplinkPortConfigNotifications = _TplinkPortConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 8, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PORTCONFIG-MIB",
    **{"tplinkPortConfigMIB": tplinkPortConfigMIB,
       "tplinkPortConfigMIBObjects": tplinkPortConfigMIBObjects,
       "tpPortConfigTable": tpPortConfigTable,
       "tpPortConfigJumbo": tpPortConfigJumbo,
       "tpPortConfigEntry": tpPortConfigEntry,
       "tpPortConfigDescription": tpPortConfigDescription,
       "tpPortConfigStatus": tpPortConfigStatus,
       "tpPortConfigSpeed": tpPortConfigSpeed,
       "tpPortConfigDuplex": tpPortConfigDuplex,
       "tpPortConfigFlowCtrl": tpPortConfigFlowCtrl,
       "tpPortConfigLAG": tpPortConfigLAG,
       "tpPortCableTestTable": tpPortCableTestTable,
       "tpPortCableTestEntry": tpPortCableTestEntry,
       "tpPairAStatus": tpPairAStatus,
       "tpPairALength": tpPairALength,
       "tpPairBStatus": tpPairBStatus,
       "tpPairBLength": tpPairBLength,
       "tpPairCStatus": tpPairCStatus,
       "tpPairCLength": tpPairCLength,
       "tpPairDStatus": tpPairDStatus,
       "tpPairDLength": tpPairDLength,
       "tpPortCableTestCFTable": tpPortCableTestCFTable,
       "tpPortCableTestFlush": tpPortCableTestFlush,
       "tpPortCableTestCFEntry": tpPortCableTestCFEntry,
       "tpPairAStatusCF": tpPairAStatusCF,
       "tpPairALengthCF": tpPairALengthCF,
       "tpPairBStatusCF": tpPairBStatusCF,
       "tpPairBLengthCF": tpPairBLengthCF,
       "tpPairCStatusCF": tpPairCStatusCF,
       "tpPairCLengthCF": tpPairCLengthCF,
       "tpPairDStatusCF": tpPairDStatusCF,
       "tpPairDLengthCF": tpPairDLengthCF,
       "tpPortTrafficMonitorTable": tpPortTrafficMonitorTable,
       "tpPortTrafficMonitorEntry": tpPortTrafficMonitorEntry,
       "tpPortRxPkts": tpPortRxPkts,
       "tpPortRxBytes": tpPortRxBytes,
       "tpPortRxUcast": tpPortRxUcast,
       "tpPortRxMcast": tpPortRxMcast,
       "tpPortRxBcast": tpPortRxBcast,
       "tpPortRxJumbo": tpPortRxJumbo,
       "tpPortRxAlignment": tpPortRxAlignment,
       "tpPortRxUnderSize": tpPortRxUnderSize,
       "tpPortRx64Pkts": tpPortRx64Pkts,
       "tpPortRx65-127Pkts": tpPortRx65_127Pkts,
       "tpPortRx128-255Pkts": tpPortRx128_255Pkts,
       "tpPortRx256-511Pkts": tpPortRx256_511Pkts,
       "tpPortRx512-1023Pkts": tpPortRx512_1023Pkts,
       "tpPortRxOver1023Pkts": tpPortRxOver1023Pkts,
       "tpPortTxPkts": tpPortTxPkts,
       "tpPortTxBytes": tpPortTxBytes,
       "tpPortTxUcast": tpPortTxUcast,
       "tpPortTxMcast": tpPortTxMcast,
       "tpPortTxBcast": tpPortTxBcast,
       "tpPortTxJumbo": tpPortTxJumbo,
       "tpPortTxCollisions": tpPortTxCollisions,
       "tpPortTrafficMonitorClear": tpPortTrafficMonitorClear,
       "tpEEETable": tpEEETable,
       "tpEEEEntry": tpEEEEntry,
       "tpEEEPort": tpEEEPort,
       "tpEEEStatus": tpEEEStatus,
       "tpEEEPortLag": tpEEEPortLag,
       "tplinkPortConfigNotifications": tplinkPortConfigNotifications}
)
