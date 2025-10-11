# SNMP MIB module (ZXSONETIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXSONETIF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:30 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zxPwCTDM,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxPwCTDM")


# MODULE-IDENTITY

zxSonetIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxSonetCfgTable_Object = MibTable
zxSonetCfgTable = _ZxSonetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxSonetCfgTable.setStatus("current")
_ZxSonetCfgEntry_Object = MibTableRow
zxSonetCfgEntry = _ZxSonetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1)
)
zxSonetCfgEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxSonetCfgEntry.setStatus("current")
_ZxSonetIfIndex_Type = InterfaceIndex
_ZxSonetIfIndex_Object = MibTableColumn
zxSonetIfIndex = _ZxSonetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1, 1),
    _ZxSonetIfIndex_Type()
)
zxSonetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxSonetIfIndex.setStatus("deprecated")


class _ZxSonetLoopBackType_Type(Integer32):
    """Custom type zxSonetLoopBackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("lineLoop", 2),
          ("inwardLoop", 3))
    )


_ZxSonetLoopBackType_Type.__name__ = "Integer32"
_ZxSonetLoopBackType_Object = MibTableColumn
zxSonetLoopBackType = _ZxSonetLoopBackType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1, 2),
    _ZxSonetLoopBackType_Type()
)
zxSonetLoopBackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetLoopBackType.setStatus("current")


class _ZxSonetClockSource_Type(Integer32):
    """Custom type zxSonetClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2))
    )


_ZxSonetClockSource_Type.__name__ = "Integer32"
_ZxSonetClockSource_Object = MibTableColumn
zxSonetClockSource = _ZxSonetClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1, 3),
    _ZxSonetClockSource_Type()
)
zxSonetClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetClockSource.setStatus("current")


class _ZxSonetConfigType_Type(Integer32):
    """Custom type zxSonetConfigType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sonetSts3c", 1),
          ("sonetStm1", 2),
          ("sonetSts12c", 3),
          ("sonetStm4", 4),
          ("sonetSts48c", 5),
          ("sonetStm16", 6),
          ("sonetSts192c", 7),
          ("sonetStm64", 8))
    )


_ZxSonetConfigType_Type.__name__ = "Integer32"
_ZxSonetConfigType_Object = MibTableColumn
zxSonetConfigType = _ZxSonetConfigType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1, 4),
    _ZxSonetConfigType_Type()
)
zxSonetConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxSonetConfigType.setStatus("current")


class _ZxSonetConfigMapType_Type(Integer32):
    """Custom type zxSonetConfigMapType based on Integer32"""
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
        *(("other", 0),
          ("au3tu11", 1),
          ("au3tu12", 2),
          ("au4tu11", 3),
          ("au4tu12", 4))
    )


_ZxSonetConfigMapType_Type.__name__ = "Integer32"
_ZxSonetConfigMapType_Object = MibTableColumn
zxSonetConfigMapType = _ZxSonetConfigMapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1, 5),
    _ZxSonetConfigMapType_Type()
)
zxSonetConfigMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetConfigMapType.setStatus("current")
_ZxSonetCfgInfoSend_Type = TruthValue
_ZxSonetCfgInfoSend_Object = MibTableColumn
zxSonetCfgInfoSend = _ZxSonetCfgInfoSend_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 1, 1, 6),
    _ZxSonetCfgInfoSend_Type()
)
zxSonetCfgInfoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetCfgInfoSend.setStatus("current")
_ZxSonetMediumTable_Object = MibTable
zxSonetMediumTable = _ZxSonetMediumTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxSonetMediumTable.setStatus("current")
_ZxSonetMediumEntry_Object = MibTableRow
zxSonetMediumEntry = _ZxSonetMediumEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1)
)
zxSonetMediumEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetIfIndex"),
)
if mibBuilder.loadTexts:
    zxSonetMediumEntry.setStatus("current")


class _ZxSonetMediumType_Type(Integer32):
    """Custom type zxSonetMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonet", 1),
          ("sdh", 2))
    )


_ZxSonetMediumType_Type.__name__ = "Integer32"
_ZxSonetMediumType_Object = MibTableColumn
zxSonetMediumType = _ZxSonetMediumType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 1),
    _ZxSonetMediumType_Type()
)
zxSonetMediumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetMediumType.setStatus("current")


class _ZxSonetMediumTimeElapsed_Type(Integer32):
    """Custom type zxSonetMediumTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_ZxSonetMediumTimeElapsed_Type.__name__ = "Integer32"
_ZxSonetMediumTimeElapsed_Object = MibTableColumn
zxSonetMediumTimeElapsed = _ZxSonetMediumTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 2),
    _ZxSonetMediumTimeElapsed_Type()
)
zxSonetMediumTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxSonetMediumTimeElapsed.setStatus("current")


class _ZxSonetMediumValidIntervals_Type(Integer32):
    """Custom type zxSonetMediumValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZxSonetMediumValidIntervals_Type.__name__ = "Integer32"
_ZxSonetMediumValidIntervals_Object = MibTableColumn
zxSonetMediumValidIntervals = _ZxSonetMediumValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 3),
    _ZxSonetMediumValidIntervals_Type()
)
zxSonetMediumValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxSonetMediumValidIntervals.setStatus("current")


class _ZxSonetMediumLineCoding_Type(Integer32):
    """Custom type zxSonetMediumLineCoding based on Integer32"""
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
        *(("sonetMediumOther", 1),
          ("sonetMediumB3ZS", 2),
          ("sonetMediumCMI", 3),
          ("sonetMediumNRZ", 4),
          ("sonetMediumRZ", 5))
    )


_ZxSonetMediumLineCoding_Type.__name__ = "Integer32"
_ZxSonetMediumLineCoding_Object = MibTableColumn
zxSonetMediumLineCoding = _ZxSonetMediumLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 4),
    _ZxSonetMediumLineCoding_Type()
)
zxSonetMediumLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetMediumLineCoding.setStatus("current")


class _ZxSonetMediumLineType_Type(Integer32):
    """Custom type zxSonetMediumLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sonetOther", 1),
          ("sonetShortSingleMode", 2),
          ("sonetLongSingleMode", 3),
          ("sonetMultiMode", 4),
          ("sonetCoax", 5),
          ("sonetUTP", 6))
    )


_ZxSonetMediumLineType_Type.__name__ = "Integer32"
_ZxSonetMediumLineType_Object = MibTableColumn
zxSonetMediumLineType = _ZxSonetMediumLineType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 5),
    _ZxSonetMediumLineType_Type()
)
zxSonetMediumLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetMediumLineType.setStatus("current")


class _ZxSonetMediumCircuitIdentifier_Type(DisplayString):
    """Custom type zxSonetMediumCircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxSonetMediumCircuitIdentifier_Type.__name__ = "DisplayString"
_ZxSonetMediumCircuitIdentifier_Object = MibTableColumn
zxSonetMediumCircuitIdentifier = _ZxSonetMediumCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 6),
    _ZxSonetMediumCircuitIdentifier_Type()
)
zxSonetMediumCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetMediumCircuitIdentifier.setStatus("current")


class _ZxSonetMediumInvalidIntervals_Type(Integer32):
    """Custom type zxSonetMediumInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZxSonetMediumInvalidIntervals_Type.__name__ = "Integer32"
_ZxSonetMediumInvalidIntervals_Object = MibTableColumn
zxSonetMediumInvalidIntervals = _ZxSonetMediumInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 7),
    _ZxSonetMediumInvalidIntervals_Type()
)
zxSonetMediumInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxSonetMediumInvalidIntervals.setStatus("current")


class _ZxSonetMediumLoopbackConfig_Type(Bits):
    """Custom type zxSonetMediumLoopbackConfig based on Bits"""
    namedValues = NamedValues(
        *(("sonetNoLoop", 0),
          ("sonetFacilityLoop", 1),
          ("sonetTerminalLoop", 2),
          ("sonetOtherLoop", 3))
    )

_ZxSonetMediumLoopbackConfig_Type.__name__ = "Bits"
_ZxSonetMediumLoopbackConfig_Object = MibTableColumn
zxSonetMediumLoopbackConfig = _ZxSonetMediumLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 2, 1, 8),
    _ZxSonetMediumLoopbackConfig_Type()
)
zxSonetMediumLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetMediumLoopbackConfig.setStatus("current")
_ZxSonetVTConfigTable_Object = MibTable
zxSonetVTConfigTable = _ZxSonetVTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    zxSonetVTConfigTable.setStatus("current")
_ZxSonetVTConfigEntry_Object = MibTableRow
zxSonetVTConfigEntry = _ZxSonetVTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3, 1)
)
zxSonetVTConfigEntry.setIndexNames(
    (0, "ZXSONETIF-MIB", "zxSonetVTIfIndex"),
)
if mibBuilder.loadTexts:
    zxSonetVTConfigEntry.setStatus("current")
_ZxSonetVTIfIndex_Type = InterfaceIndex
_ZxSonetVTIfIndex_Object = MibTableColumn
zxSonetVTIfIndex = _ZxSonetVTIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3, 1, 1),
    _ZxSonetVTIfIndex_Type()
)
zxSonetVTIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxSonetVTIfIndex.setStatus("deprecated")


class _ZxSonetVTLoopbackConfig_Type(Integer32):
    """Custom type zxSonetVTLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noLoop", 1),
          ("payloadLoop", 2),
          ("lineLoop", 3),
          ("otherLoop", 4),
          ("inwardLoop", 5),
          ("dualLoop", 6))
    )


_ZxSonetVTLoopbackConfig_Type.__name__ = "Integer32"
_ZxSonetVTLoopbackConfig_Object = MibTableColumn
zxSonetVTLoopbackConfig = _ZxSonetVTLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3, 1, 2),
    _ZxSonetVTLoopbackConfig_Type()
)
zxSonetVTLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetVTLoopbackConfig.setStatus("current")


class _ZxSonetVTTransmitClockSource_Type(Integer32):
    """Custom type zxSonetVTTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("enhancedAdaptive", 5),
          ("differential", 6))
    )


_ZxSonetVTTransmitClockSource_Type.__name__ = "Integer32"
_ZxSonetVTTransmitClockSource_Object = MibTableColumn
zxSonetVTTransmitClockSource = _ZxSonetVTTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3, 1, 3),
    _ZxSonetVTTransmitClockSource_Type()
)
zxSonetVTTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetVTTransmitClockSource.setStatus("current")


class _ZxSonetVTClockStatus_Type(Integer32):
    """Custom type zxSonetVTClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ZxSonetVTClockStatus_Type.__name__ = "Integer32"
_ZxSonetVTClockStatus_Object = MibTableColumn
zxSonetVTClockStatus = _ZxSonetVTClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3, 1, 4),
    _ZxSonetVTClockStatus_Type()
)
zxSonetVTClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxSonetVTClockStatus.setStatus("current")
_ZxSonetVTCfgInfoSend_Type = TruthValue
_ZxSonetVTCfgInfoSend_Object = MibTableColumn
zxSonetVTCfgInfoSend = _ZxSonetVTCfgInfoSend_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1, 3, 3, 1, 5),
    _ZxSonetVTCfgInfoSend_Type()
)
zxSonetVTCfgInfoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxSonetVTCfgInfoSend.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXSONETIF-MIB",
    **{"zxSonetIfMIB": zxSonetIfMIB,
       "zxSonetCfgTable": zxSonetCfgTable,
       "zxSonetCfgEntry": zxSonetCfgEntry,
       "zxSonetIfIndex": zxSonetIfIndex,
       "zxSonetLoopBackType": zxSonetLoopBackType,
       "zxSonetClockSource": zxSonetClockSource,
       "zxSonetConfigType": zxSonetConfigType,
       "zxSonetConfigMapType": zxSonetConfigMapType,
       "zxSonetCfgInfoSend": zxSonetCfgInfoSend,
       "zxSonetMediumTable": zxSonetMediumTable,
       "zxSonetMediumEntry": zxSonetMediumEntry,
       "zxSonetMediumType": zxSonetMediumType,
       "zxSonetMediumTimeElapsed": zxSonetMediumTimeElapsed,
       "zxSonetMediumValidIntervals": zxSonetMediumValidIntervals,
       "zxSonetMediumLineCoding": zxSonetMediumLineCoding,
       "zxSonetMediumLineType": zxSonetMediumLineType,
       "zxSonetMediumCircuitIdentifier": zxSonetMediumCircuitIdentifier,
       "zxSonetMediumInvalidIntervals": zxSonetMediumInvalidIntervals,
       "zxSonetMediumLoopbackConfig": zxSonetMediumLoopbackConfig,
       "zxSonetVTConfigTable": zxSonetVTConfigTable,
       "zxSonetVTConfigEntry": zxSonetVTConfigEntry,
       "zxSonetVTIfIndex": zxSonetVTIfIndex,
       "zxSonetVTLoopbackConfig": zxSonetVTLoopbackConfig,
       "zxSonetVTTransmitClockSource": zxSonetVTTransmitClockSource,
       "zxSonetVTClockStatus": zxSonetVTClockStatus,
       "zxSonetVTCfgInfoSend": zxSonetVTCfgInfoSend}
)
