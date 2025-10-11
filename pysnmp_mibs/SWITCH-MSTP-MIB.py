# SNMP MIB module (SWITCH-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-MSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:27 2025
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(Vlanset,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "Vlanset")


# MODULE-IDENTITY

rcMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24)
)
if mibBuilder.loadTexts:
    rcMstp.setRevisions(
        ("2007-01-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcMstpTraps_ObjectIdentity = ObjectIdentity
rcMstpTraps = _RcMstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1)
)
_RcMstpBridge_ObjectIdentity = ObjectIdentity
rcMstpBridge = _RcMstpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2)
)


class _RcMstpBridgeAdminStp_Type(TruthValue):
    """Custom type rcMstpBridgeAdminStp based on TruthValue"""
    defaultValue = 2


_RcMstpBridgeAdminStp_Type.__name__ = "TruthValue"
_RcMstpBridgeAdminStp_Object = MibScalar
rcMstpBridgeAdminStp = _RcMstpBridgeAdminStp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 1),
    _RcMstpBridgeAdminStp_Type()
)
rcMstpBridgeAdminStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeAdminStp.setStatus("current")


class _RcMstpBridgeMaxHops_Type(Integer32):
    """Custom type rcMstpBridgeMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_RcMstpBridgeMaxHops_Type.__name__ = "Integer32"
_RcMstpBridgeMaxHops_Object = MibScalar
rcMstpBridgeMaxHops = _RcMstpBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 2),
    _RcMstpBridgeMaxHops_Type()
)
rcMstpBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeMaxHops.setStatus("current")


class _RcMstpBridgeVersionSupported_Type(Bits):
    """Custom type rcMstpBridgeVersionSupported based on Bits"""
    namedValues = NamedValues(
        *(("nonStp", 0),
          ("dot1d1998", 1),
          ("dot1w", 2),
          ("dot1d2004", 3),
          ("dot1s", 4),
          ("dot1q", 5),
          ("unknown", 15))
    )

_RcMstpBridgeVersionSupported_Type.__name__ = "Bits"
_RcMstpBridgeVersionSupported_Object = MibScalar
rcMstpBridgeVersionSupported = _RcMstpBridgeVersionSupported_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 3),
    _RcMstpBridgeVersionSupported_Type()
)
rcMstpBridgeVersionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeVersionSupported.setStatus("current")


class _RcMstpBridgeProtocolVersion_Type(Integer32):
    """Custom type rcMstpBridgeProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              15)
        )
    )
    namedValues = NamedValues(
        *(("forceNonStp", 0),
          ("forceLegacyDot1d", 1),
          ("forceDot1w", 2),
          ("autoDot1s", 3),
          ("unknown", 15))
    )


_RcMstpBridgeProtocolVersion_Type.__name__ = "Integer32"
_RcMstpBridgeProtocolVersion_Object = MibScalar
rcMstpBridgeProtocolVersion = _RcMstpBridgeProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 4),
    _RcMstpBridgeProtocolVersion_Type()
)
rcMstpBridgeProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeProtocolVersion.setStatus("current")


class _RcMstpBridgeRegionFormatSelector_Type(Integer32):
    """Custom type rcMstpBridgeRegionFormatSelector based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcMstpBridgeRegionFormatSelector_Type.__name__ = "Integer32"
_RcMstpBridgeRegionFormatSelector_Object = MibScalar
rcMstpBridgeRegionFormatSelector = _RcMstpBridgeRegionFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 5),
    _RcMstpBridgeRegionFormatSelector_Type()
)
rcMstpBridgeRegionFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionFormatSelector.setStatus("current")


class _RcMstpBridgeRegionName_Type(DisplayString):
    """Custom type rcMstpBridgeRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcMstpBridgeRegionName_Type.__name__ = "DisplayString"
_RcMstpBridgeRegionName_Object = MibScalar
rcMstpBridgeRegionName = _RcMstpBridgeRegionName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 6),
    _RcMstpBridgeRegionName_Type()
)
rcMstpBridgeRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionName.setStatus("current")


class _RcMstpBridgeRegionEditName_Type(DisplayString):
    """Custom type rcMstpBridgeRegionEditName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcMstpBridgeRegionEditName_Type.__name__ = "DisplayString"
_RcMstpBridgeRegionEditName_Object = MibScalar
rcMstpBridgeRegionEditName = _RcMstpBridgeRegionEditName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 7),
    _RcMstpBridgeRegionEditName_Type()
)
rcMstpBridgeRegionEditName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionEditName.setStatus("current")


class _RcMstpBridgeRegionRevLevel_Type(Integer32):
    """Custom type rcMstpBridgeRegionRevLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcMstpBridgeRegionRevLevel_Type.__name__ = "Integer32"
_RcMstpBridgeRegionRevLevel_Object = MibScalar
rcMstpBridgeRegionRevLevel = _RcMstpBridgeRegionRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 8),
    _RcMstpBridgeRegionRevLevel_Type()
)
rcMstpBridgeRegionRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionRevLevel.setStatus("current")


class _RcMstpBridgeRegionEditRevLevel_Type(Integer32):
    """Custom type rcMstpBridgeRegionEditRevLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcMstpBridgeRegionEditRevLevel_Type.__name__ = "Integer32"
_RcMstpBridgeRegionEditRevLevel_Object = MibScalar
rcMstpBridgeRegionEditRevLevel = _RcMstpBridgeRegionEditRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 9),
    _RcMstpBridgeRegionEditRevLevel_Type()
)
rcMstpBridgeRegionEditRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionEditRevLevel.setStatus("current")


class _RcMstpBridgeRegionDigest_Type(OctetString):
    """Custom type rcMstpBridgeRegionDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_RcMstpBridgeRegionDigest_Type.__name__ = "OctetString"
_RcMstpBridgeRegionDigest_Object = MibScalar
rcMstpBridgeRegionDigest = _RcMstpBridgeRegionDigest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 10),
    _RcMstpBridgeRegionDigest_Type()
)
rcMstpBridgeRegionDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionDigest.setStatus("current")
_RcMstpBridgeCistRoot_Type = BridgeId
_RcMstpBridgeCistRoot_Object = MibScalar
rcMstpBridgeCistRoot = _RcMstpBridgeCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 11),
    _RcMstpBridgeCistRoot_Type()
)
rcMstpBridgeCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeCistRoot.setStatus("current")
_RcMstpBridgeCistExternalRootCost_Type = Integer32
_RcMstpBridgeCistExternalRootCost_Object = MibScalar
rcMstpBridgeCistExternalRootCost = _RcMstpBridgeCistExternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 12),
    _RcMstpBridgeCistExternalRootCost_Type()
)
rcMstpBridgeCistExternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpBridgeCistExternalRootCost.setStatus("current")


class _RcMstpBridgeDiameter_Type(Unsigned32):
    """Custom type rcMstpBridgeDiameter based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_RcMstpBridgeDiameter_Type.__name__ = "Unsigned32"
_RcMstpBridgeDiameter_Object = MibScalar
rcMstpBridgeDiameter = _RcMstpBridgeDiameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 13),
    _RcMstpBridgeDiameter_Type()
)
rcMstpBridgeDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeDiameter.setStatus("current")


class _RcMstpBridgeRegionEditBufferOperation_Type(Integer32):
    """Custom type rcMstpBridgeRegionEditBufferOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2))
    )


_RcMstpBridgeRegionEditBufferOperation_Type.__name__ = "Integer32"
_RcMstpBridgeRegionEditBufferOperation_Object = MibScalar
rcMstpBridgeRegionEditBufferOperation = _RcMstpBridgeRegionEditBufferOperation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 2, 14),
    _RcMstpBridgeRegionEditBufferOperation_Type()
)
rcMstpBridgeRegionEditBufferOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBridgeRegionEditBufferOperation.setStatus("current")
_RcMstpPortTable_Object = MibTable
rcMstpPortTable = _RcMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3)
)
if mibBuilder.loadTexts:
    rcMstpPortTable.setStatus("current")
_RcMstpPortEntry_Object = MibTableRow
rcMstpPortEntry = _RcMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1)
)
rcMstpPortEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpPortIndex"),
)
if mibBuilder.loadTexts:
    rcMstpPortEntry.setStatus("current")


class _RcMstpPortIndex_Type(Integer32):
    """Custom type rcMstpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcMstpPortIndex_Type.__name__ = "Integer32"
_RcMstpPortIndex_Object = MibTableColumn
rcMstpPortIndex = _RcMstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 1),
    _RcMstpPortIndex_Type()
)
rcMstpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpPortIndex.setStatus("current")
_RcMstpPortAdminMACEnable_Type = TruthValue
_RcMstpPortAdminMACEnable_Object = MibTableColumn
rcMstpPortAdminMACEnable = _RcMstpPortAdminMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 2),
    _RcMstpPortAdminMACEnable_Type()
)
rcMstpPortAdminMACEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortAdminMACEnable.setStatus("current")
_RcMstpPortOperMACEnable_Type = TruthValue
_RcMstpPortOperMACEnable_Object = MibTableColumn
rcMstpPortOperMACEnable = _RcMstpPortOperMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 3),
    _RcMstpPortOperMACEnable_Type()
)
rcMstpPortOperMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortOperMACEnable.setStatus("current")


class _RcMstpPortAdminEdgePort_Type(Integer32):
    """Custom type rcMstpPortAdminEdgePort based on Integer32"""
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
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_RcMstpPortAdminEdgePort_Type.__name__ = "Integer32"
_RcMstpPortAdminEdgePort_Object = MibTableColumn
rcMstpPortAdminEdgePort = _RcMstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 4),
    _RcMstpPortAdminEdgePort_Type()
)
rcMstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortAdminEdgePort.setStatus("current")


class _RcMstpPortAdminStp_Type(TruthValue):
    """Custom type rcMstpPortAdminStp based on TruthValue"""
    defaultValue = 2


_RcMstpPortAdminStp_Type.__name__ = "TruthValue"
_RcMstpPortAdminStp_Object = MibTableColumn
rcMstpPortAdminStp = _RcMstpPortAdminStp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 5),
    _RcMstpPortAdminStp_Type()
)
rcMstpPortAdminStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortAdminStp.setStatus("current")


class _RcMstpPortOperStp_Type(Integer32):
    """Custom type rcMstpPortOperStp based on Integer32"""
    defaultValue = 2

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


_RcMstpPortOperStp_Type.__name__ = "Integer32"
_RcMstpPortOperStp_Object = MibTableColumn
rcMstpPortOperStp = _RcMstpPortOperStp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 6),
    _RcMstpPortOperStp_Type()
)
rcMstpPortOperStp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortOperStp.setStatus("current")


class _RcMstpPortRootGuard_Type(Integer32):
    """Custom type rcMstpPortRootGuard based on Integer32"""
    defaultValue = 2

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


_RcMstpPortRootGuard_Type.__name__ = "Integer32"
_RcMstpPortRootGuard_Object = MibTableColumn
rcMstpPortRootGuard = _RcMstpPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 7),
    _RcMstpPortRootGuard_Type()
)
rcMstpPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortRootGuard.setStatus("current")
_RcMstpPortRxTcnBpduCounter_Type = Counter32
_RcMstpPortRxTcnBpduCounter_Object = MibTableColumn
rcMstpPortRxTcnBpduCounter = _RcMstpPortRxTcnBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 8),
    _RcMstpPortRxTcnBpduCounter_Type()
)
rcMstpPortRxTcnBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortRxTcnBpduCounter.setStatus("current")
_RcMstpPortRxCfgBpduCounter_Type = Counter32
_RcMstpPortRxCfgBpduCounter_Object = MibTableColumn
rcMstpPortRxCfgBpduCounter = _RcMstpPortRxCfgBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 9),
    _RcMstpPortRxCfgBpduCounter_Type()
)
rcMstpPortRxCfgBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortRxCfgBpduCounter.setStatus("current")
_RcMstpPortRxRstBpduCounter_Type = Counter32
_RcMstpPortRxRstBpduCounter_Object = MibTableColumn
rcMstpPortRxRstBpduCounter = _RcMstpPortRxRstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 10),
    _RcMstpPortRxRstBpduCounter_Type()
)
rcMstpPortRxRstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortRxRstBpduCounter.setStatus("current")
_RcMstpPortRxMstBpduCounter_Type = Counter32
_RcMstpPortRxMstBpduCounter_Object = MibTableColumn
rcMstpPortRxMstBpduCounter = _RcMstpPortRxMstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 11),
    _RcMstpPortRxMstBpduCounter_Type()
)
rcMstpPortRxMstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortRxMstBpduCounter.setStatus("current")
_RcMstpPortTxTcnBpduCounter_Type = Counter32
_RcMstpPortTxTcnBpduCounter_Object = MibTableColumn
rcMstpPortTxTcnBpduCounter = _RcMstpPortTxTcnBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 12),
    _RcMstpPortTxTcnBpduCounter_Type()
)
rcMstpPortTxTcnBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortTxTcnBpduCounter.setStatus("current")
_RcMstpPortTxCfgBpduCounter_Type = Counter32
_RcMstpPortTxCfgBpduCounter_Object = MibTableColumn
rcMstpPortTxCfgBpduCounter = _RcMstpPortTxCfgBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 13),
    _RcMstpPortTxCfgBpduCounter_Type()
)
rcMstpPortTxCfgBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortTxCfgBpduCounter.setStatus("current")
_RcMstpPortTxRstBpduCounter_Type = Counter32
_RcMstpPortTxRstBpduCounter_Object = MibTableColumn
rcMstpPortTxRstBpduCounter = _RcMstpPortTxRstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 14),
    _RcMstpPortTxRstBpduCounter_Type()
)
rcMstpPortTxRstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortTxRstBpduCounter.setStatus("current")
_RcMstpPortTxMstBpduCounter_Type = Counter32
_RcMstpPortTxMstBpduCounter_Object = MibTableColumn
rcMstpPortTxMstBpduCounter = _RcMstpPortTxMstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 15),
    _RcMstpPortTxMstBpduCounter_Type()
)
rcMstpPortTxMstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpPortTxMstBpduCounter.setStatus("current")
_RcMstpPortStatisticsClear_Type = TruthValue
_RcMstpPortStatisticsClear_Object = MibTableColumn
rcMstpPortStatisticsClear = _RcMstpPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 16),
    _RcMstpPortStatisticsClear_Type()
)
rcMstpPortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortStatisticsClear.setStatus("current")


class _RcMstpPortLoopGuard_Type(Integer32):
    """Custom type rcMstpPortLoopGuard based on Integer32"""
    defaultValue = 2

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


_RcMstpPortLoopGuard_Type.__name__ = "Integer32"
_RcMstpPortLoopGuard_Object = MibTableColumn
rcMstpPortLoopGuard = _RcMstpPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 17),
    _RcMstpPortLoopGuard_Type()
)
rcMstpPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortLoopGuard.setStatus("current")


class _RcMstpBpduFilterEnable_Type(TruthValue):
    """Custom type rcMstpBpduFilterEnable based on TruthValue"""
    defaultValue = 2


_RcMstpBpduFilterEnable_Type.__name__ = "TruthValue"
_RcMstpBpduFilterEnable_Object = MibTableColumn
rcMstpBpduFilterEnable = _RcMstpBpduFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 18),
    _RcMstpBpduFilterEnable_Type()
)
rcMstpBpduFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpBpduFilterEnable.setStatus("current")


class _RcMstpPortBpduGuardEnable_Type(TruthValue):
    """Custom type rcMstpPortBpduGuardEnable based on TruthValue"""
    defaultValue = 2


_RcMstpPortBpduGuardEnable_Type.__name__ = "TruthValue"
_RcMstpPortBpduGuardEnable_Object = MibTableColumn
rcMstpPortBpduGuardEnable = _RcMstpPortBpduGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 19),
    _RcMstpPortBpduGuardEnable_Type()
)
rcMstpPortBpduGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortBpduGuardEnable.setStatus("current")


class _RcMstpPortBpduGuardStatus_Type(Integer32):
    """Custom type rcMstpPortBpduGuardStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RcMstpPortBpduGuardStatus_Type.__name__ = "Integer32"
_RcMstpPortBpduGuardStatus_Object = MibTableColumn
rcMstpPortBpduGuardStatus = _RcMstpPortBpduGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 3, 1, 20),
    _RcMstpPortBpduGuardStatus_Type()
)
rcMstpPortBpduGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpPortBpduGuardStatus.setStatus("current")
_RcMstpXstInstanceTable_Object = MibTable
rcMstpXstInstanceTable = _RcMstpXstInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 4)
)
if mibBuilder.loadTexts:
    rcMstpXstInstanceTable.setStatus("current")
_RcMstpXstInstanceEntry_Object = MibTableRow
rcMstpXstInstanceEntry = _RcMstpXstInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 4, 1)
)
rcMstpXstInstanceEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpXstInstanceId"),
)
if mibBuilder.loadTexts:
    rcMstpXstInstanceEntry.setStatus("current")


class _RcMstpXstInstanceId_Type(Integer32):
    """Custom type rcMstpXstInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RcMstpXstInstanceId_Type.__name__ = "Integer32"
_RcMstpXstInstanceId_Object = MibTableColumn
rcMstpXstInstanceId = _RcMstpXstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 4, 1, 1),
    _RcMstpXstInstanceId_Type()
)
rcMstpXstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstInstanceId.setStatus("current")
_RcMstpXstInstanceVlansMapped_Type = Vlanset
_RcMstpXstInstanceVlansMapped_Object = MibTableColumn
rcMstpXstInstanceVlansMapped = _RcMstpXstInstanceVlansMapped_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 4, 1, 2),
    _RcMstpXstInstanceVlansMapped_Type()
)
rcMstpXstInstanceVlansMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstInstanceVlansMapped.setStatus("current")
_RcMstpXstInstanceEditTable_Object = MibTable
rcMstpXstInstanceEditTable = _RcMstpXstInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 5)
)
if mibBuilder.loadTexts:
    rcMstpXstInstanceEditTable.setStatus("current")
_RcMstpXstInstanceEditEntry_Object = MibTableRow
rcMstpXstInstanceEditEntry = _RcMstpXstInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 5, 1)
)
rcMstpXstInstanceEditEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpXstInstanceEditId"),
)
if mibBuilder.loadTexts:
    rcMstpXstInstanceEditEntry.setStatus("current")


class _RcMstpXstInstanceEditId_Type(Unsigned32):
    """Custom type rcMstpXstInstanceEditId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RcMstpXstInstanceEditId_Type.__name__ = "Unsigned32"
_RcMstpXstInstanceEditId_Object = MibTableColumn
rcMstpXstInstanceEditId = _RcMstpXstInstanceEditId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 5, 1, 1),
    _RcMstpXstInstanceEditId_Type()
)
rcMstpXstInstanceEditId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstInstanceEditId.setStatus("current")
_RcMstpXstInstanceEditVlansMap_Type = Vlanset
_RcMstpXstInstanceEditVlansMap_Object = MibTableColumn
rcMstpXstInstanceEditVlansMap = _RcMstpXstInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 5, 1, 2),
    _RcMstpXstInstanceEditVlansMap_Type()
)
rcMstpXstInstanceEditVlansMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMstpXstInstanceEditVlansMap.setStatus("current")
_RcMstpXstInstanceEditRowStatus_Type = RowStatus
_RcMstpXstInstanceEditRowStatus_Object = MibTableColumn
rcMstpXstInstanceEditRowStatus = _RcMstpXstInstanceEditRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 5, 1, 3),
    _RcMstpXstInstanceEditRowStatus_Type()
)
rcMstpXstInstanceEditRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcMstpXstInstanceEditRowStatus.setStatus("current")
_RcMstpXstTable_Object = MibTable
rcMstpXstTable = _RcMstpXstTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6)
)
if mibBuilder.loadTexts:
    rcMstpXstTable.setStatus("current")
_RcMstpXstEntry_Object = MibTableRow
rcMstpXstEntry = _RcMstpXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1)
)
rcMstpXstEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpXstId"),
)
if mibBuilder.loadTexts:
    rcMstpXstEntry.setStatus("current")


class _RcMstpXstId_Type(Integer32):
    """Custom type rcMstpXstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RcMstpXstId_Type.__name__ = "Integer32"
_RcMstpXstId_Object = MibTableColumn
rcMstpXstId = _RcMstpXstId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 1),
    _RcMstpXstId_Type()
)
rcMstpXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstId.setStatus("current")
_RcMstpXstBridgeId_Type = BridgeId
_RcMstpXstBridgeId_Object = MibTableColumn
rcMstpXstBridgeId = _RcMstpXstBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 2),
    _RcMstpXstBridgeId_Type()
)
rcMstpXstBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstBridgeId.setStatus("current")
_RcMstpXstDesignatedRoot_Type = BridgeId
_RcMstpXstDesignatedRoot_Object = MibTableColumn
rcMstpXstDesignatedRoot = _RcMstpXstDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 3),
    _RcMstpXstDesignatedRoot_Type()
)
rcMstpXstDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstDesignatedRoot.setStatus("current")
_RcMstpXstInternalRootCost_Type = Integer32
_RcMstpXstInternalRootCost_Object = MibTableColumn
rcMstpXstInternalRootCost = _RcMstpXstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 4),
    _RcMstpXstInternalRootCost_Type()
)
rcMstpXstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstInternalRootCost.setStatus("current")
_RcMstpXstRootPort_Type = Unsigned32
_RcMstpXstRootPort_Object = MibTableColumn
rcMstpXstRootPort = _RcMstpXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 5),
    _RcMstpXstRootPort_Type()
)
rcMstpXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstRootPort.setStatus("current")
_RcMstpXstMasterPort_Type = Unsigned32
_RcMstpXstMasterPort_Object = MibTableColumn
rcMstpXstMasterPort = _RcMstpXstMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 6),
    _RcMstpXstMasterPort_Type()
)
rcMstpXstMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstMasterPort.setStatus("current")
_RcMstpXstTimeSinceTopologyChange_Type = TimeTicks
_RcMstpXstTimeSinceTopologyChange_Object = MibTableColumn
rcMstpXstTimeSinceTopologyChange = _RcMstpXstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 7),
    _RcMstpXstTimeSinceTopologyChange_Type()
)
rcMstpXstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstTimeSinceTopologyChange.setStatus("current")
_RcMstpXstTopologyChangesCount_Type = Counter32
_RcMstpXstTopologyChangesCount_Object = MibTableColumn
rcMstpXstTopologyChangesCount = _RcMstpXstTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 8),
    _RcMstpXstTopologyChangesCount_Type()
)
rcMstpXstTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstTopologyChangesCount.setStatus("current")
_RcMstpXstTopologyChangeFlag_Type = TruthValue
_RcMstpXstTopologyChangeFlag_Object = MibTableColumn
rcMstpXstTopologyChangeFlag = _RcMstpXstTopologyChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 6, 1, 9),
    _RcMstpXstTopologyChangeFlag_Type()
)
rcMstpXstTopologyChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstTopologyChangeFlag.setStatus("current")
_RcMstpXstConfigTable_Object = MibTable
rcMstpXstConfigTable = _RcMstpXstConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 7)
)
if mibBuilder.loadTexts:
    rcMstpXstConfigTable.setStatus("current")
_RcMstpXstConfigEntry_Object = MibTableRow
rcMstpXstConfigEntry = _RcMstpXstConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 7, 1)
)
rcMstpXstConfigEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpCfgXstId"),
)
if mibBuilder.loadTexts:
    rcMstpXstConfigEntry.setStatus("current")


class _RcMstpCfgXstId_Type(Integer32):
    """Custom type rcMstpCfgXstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RcMstpCfgXstId_Type.__name__ = "Integer32"
_RcMstpCfgXstId_Object = MibTableColumn
rcMstpCfgXstId = _RcMstpCfgXstId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 7, 1, 1),
    _RcMstpCfgXstId_Type()
)
rcMstpCfgXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpCfgXstId.setStatus("current")


class _RcMstpXstBridgePriority_Type(Integer32):
    """Custom type rcMstpXstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_RcMstpXstBridgePriority_Type.__name__ = "Integer32"
_RcMstpXstBridgePriority_Object = MibTableColumn
rcMstpXstBridgePriority = _RcMstpXstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 7, 1, 2),
    _RcMstpXstBridgePriority_Type()
)
rcMstpXstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpXstBridgePriority.setStatus("current")
_RcMstpXstPrimaryRoot_Type = TruthValue
_RcMstpXstPrimaryRoot_Object = MibTableColumn
rcMstpXstPrimaryRoot = _RcMstpXstPrimaryRoot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 7, 1, 3),
    _RcMstpXstPrimaryRoot_Type()
)
rcMstpXstPrimaryRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpXstPrimaryRoot.setStatus("current")
_RcMstpXstSecondaryRoot_Type = TruthValue
_RcMstpXstSecondaryRoot_Object = MibTableColumn
rcMstpXstSecondaryRoot = _RcMstpXstSecondaryRoot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 7, 1, 4),
    _RcMstpXstSecondaryRoot_Type()
)
rcMstpXstSecondaryRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpXstSecondaryRoot.setStatus("current")
_RcMstpXstPortTable_Object = MibTable
rcMstpXstPortTable = _RcMstpXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8)
)
if mibBuilder.loadTexts:
    rcMstpXstPortTable.setStatus("current")
_RcMstpXstPortEntry_Object = MibTableRow
rcMstpXstPortEntry = _RcMstpXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1)
)
rcMstpXstPortEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpXstPortXstId"),
    (0, "SWITCH-MSTP-MIB", "rcMstpXstPortIndex"),
)
if mibBuilder.loadTexts:
    rcMstpXstPortEntry.setStatus("current")


class _RcMstpXstPortXstId_Type(Integer32):
    """Custom type rcMstpXstPortXstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RcMstpXstPortXstId_Type.__name__ = "Integer32"
_RcMstpXstPortXstId_Object = MibTableColumn
rcMstpXstPortXstId = _RcMstpXstPortXstId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 1),
    _RcMstpXstPortXstId_Type()
)
rcMstpXstPortXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstPortXstId.setStatus("current")


class _RcMstpXstPortIndex_Type(Integer32):
    """Custom type rcMstpXstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcMstpXstPortIndex_Type.__name__ = "Integer32"
_RcMstpXstPortIndex_Object = MibTableColumn
rcMstpXstPortIndex = _RcMstpXstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 2),
    _RcMstpXstPortIndex_Type()
)
rcMstpXstPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstPortIndex.setStatus("current")


class _RcMstpXstPortState_Type(Integer32):
    """Custom type rcMstpXstPortState based on Integer32"""
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
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("unknown", 4))
    )


_RcMstpXstPortState_Type.__name__ = "Integer32"
_RcMstpXstPortState_Object = MibTableColumn
rcMstpXstPortState = _RcMstpXstPortState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 3),
    _RcMstpXstPortState_Type()
)
rcMstpXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortState.setStatus("current")


class _RcMstpXstPortRole_Type(Integer32):
    """Custom type rcMstpXstPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("alternate", 2),
          ("backup", 3),
          ("root", 4),
          ("designated", 5),
          ("master", 6),
          ("unknown", 7))
    )


_RcMstpXstPortRole_Type.__name__ = "Integer32"
_RcMstpXstPortRole_Object = MibTableColumn
rcMstpXstPortRole = _RcMstpXstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 4),
    _RcMstpXstPortRole_Type()
)
rcMstpXstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortRole.setStatus("current")
_RcMstpXstPortDesignatedRoot_Type = BridgeId
_RcMstpXstPortDesignatedRoot_Object = MibTableColumn
rcMstpXstPortDesignatedRoot = _RcMstpXstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 5),
    _RcMstpXstPortDesignatedRoot_Type()
)
rcMstpXstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortDesignatedRoot.setStatus("current")
_RcMstpXstPortExternalRootCost_Type = Integer32
_RcMstpXstPortExternalRootCost_Object = MibTableColumn
rcMstpXstPortExternalRootCost = _RcMstpXstPortExternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 6),
    _RcMstpXstPortExternalRootCost_Type()
)
rcMstpXstPortExternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortExternalRootCost.setStatus("current")
_RcMstpXstPortRegionalRoot_Type = BridgeId
_RcMstpXstPortRegionalRoot_Object = MibTableColumn
rcMstpXstPortRegionalRoot = _RcMstpXstPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 7),
    _RcMstpXstPortRegionalRoot_Type()
)
rcMstpXstPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortRegionalRoot.setStatus("current")
_RcMstpXstPortInternalRootCost_Type = Integer32
_RcMstpXstPortInternalRootCost_Object = MibTableColumn
rcMstpXstPortInternalRootCost = _RcMstpXstPortInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 8),
    _RcMstpXstPortInternalRootCost_Type()
)
rcMstpXstPortInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortInternalRootCost.setStatus("current")
_RcMstpXstPortDesignatedBridge_Type = BridgeId
_RcMstpXstPortDesignatedBridge_Object = MibTableColumn
rcMstpXstPortDesignatedBridge = _RcMstpXstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 9),
    _RcMstpXstPortDesignatedBridge_Type()
)
rcMstpXstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortDesignatedBridge.setStatus("current")
_RcMstpXstPortDesignatedPort_Type = Integer32
_RcMstpXstPortDesignatedPort_Object = MibTableColumn
rcMstpXstPortDesignatedPort = _RcMstpXstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 10),
    _RcMstpXstPortDesignatedPort_Type()
)
rcMstpXstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortDesignatedPort.setStatus("current")
_RcMstpXstPortOperInternalPathCost_Type = Integer32
_RcMstpXstPortOperInternalPathCost_Object = MibTableColumn
rcMstpXstPortOperInternalPathCost = _RcMstpXstPortOperInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 11),
    _RcMstpXstPortOperInternalPathCost_Type()
)
rcMstpXstPortOperInternalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortOperInternalPathCost.setStatus("current")


class _RcMstpXstPortRootGuardState_Type(Integer32):
    """Custom type rcMstpXstPortRootGuardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RcMstpXstPortRootGuardState_Type.__name__ = "Integer32"
_RcMstpXstPortRootGuardState_Object = MibTableColumn
rcMstpXstPortRootGuardState = _RcMstpXstPortRootGuardState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 12),
    _RcMstpXstPortRootGuardState_Type()
)
rcMstpXstPortRootGuardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortRootGuardState.setStatus("current")


class _RcMstpXstPortLoopGuardState_Type(Integer32):
    """Custom type rcMstpXstPortLoopGuardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RcMstpXstPortLoopGuardState_Type.__name__ = "Integer32"
_RcMstpXstPortLoopGuardState_Object = MibTableColumn
rcMstpXstPortLoopGuardState = _RcMstpXstPortLoopGuardState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 8, 1, 13),
    _RcMstpXstPortLoopGuardState_Type()
)
rcMstpXstPortLoopGuardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMstpXstPortLoopGuardState.setStatus("current")
_RcMstpXstPortConfigTable_Object = MibTable
rcMstpXstPortConfigTable = _RcMstpXstPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 9)
)
if mibBuilder.loadTexts:
    rcMstpXstPortConfigTable.setStatus("current")
_RcMstpXstPortConfigEntry_Object = MibTableRow
rcMstpXstPortConfigEntry = _RcMstpXstPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 9, 1)
)
rcMstpXstPortConfigEntry.setIndexNames(
    (0, "SWITCH-MSTP-MIB", "rcMstpXstPortCfgXstId"),
    (0, "SWITCH-MSTP-MIB", "rcMstpXstPortCfgIndex"),
)
if mibBuilder.loadTexts:
    rcMstpXstPortConfigEntry.setStatus("current")


class _RcMstpXstPortCfgXstId_Type(Integer32):
    """Custom type rcMstpXstPortCfgXstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RcMstpXstPortCfgXstId_Type.__name__ = "Integer32"
_RcMstpXstPortCfgXstId_Object = MibTableColumn
rcMstpXstPortCfgXstId = _RcMstpXstPortCfgXstId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 9, 1, 1),
    _RcMstpXstPortCfgXstId_Type()
)
rcMstpXstPortCfgXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstPortCfgXstId.setStatus("current")


class _RcMstpXstPortCfgIndex_Type(Integer32):
    """Custom type rcMstpXstPortCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcMstpXstPortCfgIndex_Type.__name__ = "Integer32"
_RcMstpXstPortCfgIndex_Object = MibTableColumn
rcMstpXstPortCfgIndex = _RcMstpXstPortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 9, 1, 2),
    _RcMstpXstPortCfgIndex_Type()
)
rcMstpXstPortCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMstpXstPortCfgIndex.setStatus("current")


class _RcMstpXstPortPriority_Type(Integer32):
    """Custom type rcMstpXstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcMstpXstPortPriority_Type.__name__ = "Integer32"
_RcMstpXstPortPriority_Object = MibTableColumn
rcMstpXstPortPriority = _RcMstpXstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 9, 1, 3),
    _RcMstpXstPortPriority_Type()
)
rcMstpXstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpXstPortPriority.setStatus("current")


class _RcMstpXstPortAdminInternalPathCost_Type(Integer32):
    """Custom type rcMstpXstPortAdminInternalPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_RcMstpXstPortAdminInternalPathCost_Type.__name__ = "Integer32"
_RcMstpXstPortAdminInternalPathCost_Object = MibTableColumn
rcMstpXstPortAdminInternalPathCost = _RcMstpXstPortAdminInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 9, 1, 4),
    _RcMstpXstPortAdminInternalPathCost_Type()
)
rcMstpXstPortAdminInternalPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMstpXstPortAdminInternalPathCost.setStatus("current")

# Managed Objects groups


# Notification objects

rcMstpNewRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1, 1)
)
rcMstpNewRootBridge.setObjects(
    ("SWITCH-MSTP-MIB", "rcMstpXstId")
)
if mibBuilder.loadTexts:
    rcMstpNewRootBridge.setStatus(
        "current"
    )

rcMstpNewRootPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1, 2)
)
rcMstpNewRootPort.setObjects(
      *(("SWITCH-MSTP-MIB", "rcMstpXstPortXstId"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortIndex"))
)
if mibBuilder.loadTexts:
    rcMstpNewRootPort.setStatus(
        "current"
    )

rcMstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1, 3)
)
rcMstpTopologyChange.setObjects(
      *(("SWITCH-MSTP-MIB", "rcMstpXstPortXstId"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortIndex"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortState"))
)
if mibBuilder.loadTexts:
    rcMstpTopologyChange.setStatus(
        "current"
    )

rcMstpRootGuardStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1, 4)
)
rcMstpRootGuardStateChange.setObjects(
      *(("SWITCH-MSTP-MIB", "rcMstpXstPortXstId"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortIndex"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortRootGuardState"))
)
if mibBuilder.loadTexts:
    rcMstpRootGuardStateChange.setStatus(
        "current"
    )

rcMstpLoopGuardStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1, 5)
)
rcMstpLoopGuardStateChange.setObjects(
      *(("SWITCH-MSTP-MIB", "rcMstpXstPortXstId"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortIndex"),
        ("SWITCH-MSTP-MIB", "rcMstpXstPortLoopGuardState"))
)
if mibBuilder.loadTexts:
    rcMstpLoopGuardStateChange.setStatus(
        "current"
    )

rcMstpBpduGuardStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 24, 1, 6)
)
rcMstpBpduGuardStateChange.setObjects(
      *(("SWITCH-MSTP-MIB", "rcMstpPortIndex"),
        ("SWITCH-MSTP-MIB", "rcMstpPortBpduGuardEnable"),
        ("SWITCH-MSTP-MIB", "rcMstpPortBpduGuardStatus"))
)
if mibBuilder.loadTexts:
    rcMstpBpduGuardStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-MSTP-MIB",
    **{"rcMstp": rcMstp,
       "rcMstpTraps": rcMstpTraps,
       "rcMstpNewRootBridge": rcMstpNewRootBridge,
       "rcMstpNewRootPort": rcMstpNewRootPort,
       "rcMstpTopologyChange": rcMstpTopologyChange,
       "rcMstpRootGuardStateChange": rcMstpRootGuardStateChange,
       "rcMstpLoopGuardStateChange": rcMstpLoopGuardStateChange,
       "rcMstpBpduGuardStateChange": rcMstpBpduGuardStateChange,
       "rcMstpBridge": rcMstpBridge,
       "rcMstpBridgeAdminStp": rcMstpBridgeAdminStp,
       "rcMstpBridgeMaxHops": rcMstpBridgeMaxHops,
       "rcMstpBridgeVersionSupported": rcMstpBridgeVersionSupported,
       "rcMstpBridgeProtocolVersion": rcMstpBridgeProtocolVersion,
       "rcMstpBridgeRegionFormatSelector": rcMstpBridgeRegionFormatSelector,
       "rcMstpBridgeRegionName": rcMstpBridgeRegionName,
       "rcMstpBridgeRegionEditName": rcMstpBridgeRegionEditName,
       "rcMstpBridgeRegionRevLevel": rcMstpBridgeRegionRevLevel,
       "rcMstpBridgeRegionEditRevLevel": rcMstpBridgeRegionEditRevLevel,
       "rcMstpBridgeRegionDigest": rcMstpBridgeRegionDigest,
       "rcMstpBridgeCistRoot": rcMstpBridgeCistRoot,
       "rcMstpBridgeCistExternalRootCost": rcMstpBridgeCistExternalRootCost,
       "rcMstpBridgeDiameter": rcMstpBridgeDiameter,
       "rcMstpBridgeRegionEditBufferOperation": rcMstpBridgeRegionEditBufferOperation,
       "rcMstpPortTable": rcMstpPortTable,
       "rcMstpPortEntry": rcMstpPortEntry,
       "rcMstpPortIndex": rcMstpPortIndex,
       "rcMstpPortAdminMACEnable": rcMstpPortAdminMACEnable,
       "rcMstpPortOperMACEnable": rcMstpPortOperMACEnable,
       "rcMstpPortAdminEdgePort": rcMstpPortAdminEdgePort,
       "rcMstpPortAdminStp": rcMstpPortAdminStp,
       "rcMstpPortOperStp": rcMstpPortOperStp,
       "rcMstpPortRootGuard": rcMstpPortRootGuard,
       "rcMstpPortRxTcnBpduCounter": rcMstpPortRxTcnBpduCounter,
       "rcMstpPortRxCfgBpduCounter": rcMstpPortRxCfgBpduCounter,
       "rcMstpPortRxRstBpduCounter": rcMstpPortRxRstBpduCounter,
       "rcMstpPortRxMstBpduCounter": rcMstpPortRxMstBpduCounter,
       "rcMstpPortTxTcnBpduCounter": rcMstpPortTxTcnBpduCounter,
       "rcMstpPortTxCfgBpduCounter": rcMstpPortTxCfgBpduCounter,
       "rcMstpPortTxRstBpduCounter": rcMstpPortTxRstBpduCounter,
       "rcMstpPortTxMstBpduCounter": rcMstpPortTxMstBpduCounter,
       "rcMstpPortStatisticsClear": rcMstpPortStatisticsClear,
       "rcMstpPortLoopGuard": rcMstpPortLoopGuard,
       "rcMstpBpduFilterEnable": rcMstpBpduFilterEnable,
       "rcMstpPortBpduGuardEnable": rcMstpPortBpduGuardEnable,
       "rcMstpPortBpduGuardStatus": rcMstpPortBpduGuardStatus,
       "rcMstpXstInstanceTable": rcMstpXstInstanceTable,
       "rcMstpXstInstanceEntry": rcMstpXstInstanceEntry,
       "rcMstpXstInstanceId": rcMstpXstInstanceId,
       "rcMstpXstInstanceVlansMapped": rcMstpXstInstanceVlansMapped,
       "rcMstpXstInstanceEditTable": rcMstpXstInstanceEditTable,
       "rcMstpXstInstanceEditEntry": rcMstpXstInstanceEditEntry,
       "rcMstpXstInstanceEditId": rcMstpXstInstanceEditId,
       "rcMstpXstInstanceEditVlansMap": rcMstpXstInstanceEditVlansMap,
       "rcMstpXstInstanceEditRowStatus": rcMstpXstInstanceEditRowStatus,
       "rcMstpXstTable": rcMstpXstTable,
       "rcMstpXstEntry": rcMstpXstEntry,
       "rcMstpXstId": rcMstpXstId,
       "rcMstpXstBridgeId": rcMstpXstBridgeId,
       "rcMstpXstDesignatedRoot": rcMstpXstDesignatedRoot,
       "rcMstpXstInternalRootCost": rcMstpXstInternalRootCost,
       "rcMstpXstRootPort": rcMstpXstRootPort,
       "rcMstpXstMasterPort": rcMstpXstMasterPort,
       "rcMstpXstTimeSinceTopologyChange": rcMstpXstTimeSinceTopologyChange,
       "rcMstpXstTopologyChangesCount": rcMstpXstTopologyChangesCount,
       "rcMstpXstTopologyChangeFlag": rcMstpXstTopologyChangeFlag,
       "rcMstpXstConfigTable": rcMstpXstConfigTable,
       "rcMstpXstConfigEntry": rcMstpXstConfigEntry,
       "rcMstpCfgXstId": rcMstpCfgXstId,
       "rcMstpXstBridgePriority": rcMstpXstBridgePriority,
       "rcMstpXstPrimaryRoot": rcMstpXstPrimaryRoot,
       "rcMstpXstSecondaryRoot": rcMstpXstSecondaryRoot,
       "rcMstpXstPortTable": rcMstpXstPortTable,
       "rcMstpXstPortEntry": rcMstpXstPortEntry,
       "rcMstpXstPortXstId": rcMstpXstPortXstId,
       "rcMstpXstPortIndex": rcMstpXstPortIndex,
       "rcMstpXstPortState": rcMstpXstPortState,
       "rcMstpXstPortRole": rcMstpXstPortRole,
       "rcMstpXstPortDesignatedRoot": rcMstpXstPortDesignatedRoot,
       "rcMstpXstPortExternalRootCost": rcMstpXstPortExternalRootCost,
       "rcMstpXstPortRegionalRoot": rcMstpXstPortRegionalRoot,
       "rcMstpXstPortInternalRootCost": rcMstpXstPortInternalRootCost,
       "rcMstpXstPortDesignatedBridge": rcMstpXstPortDesignatedBridge,
       "rcMstpXstPortDesignatedPort": rcMstpXstPortDesignatedPort,
       "rcMstpXstPortOperInternalPathCost": rcMstpXstPortOperInternalPathCost,
       "rcMstpXstPortRootGuardState": rcMstpXstPortRootGuardState,
       "rcMstpXstPortLoopGuardState": rcMstpXstPortLoopGuardState,
       "rcMstpXstPortConfigTable": rcMstpXstPortConfigTable,
       "rcMstpXstPortConfigEntry": rcMstpXstPortConfigEntry,
       "rcMstpXstPortCfgXstId": rcMstpXstPortCfgXstId,
       "rcMstpXstPortCfgIndex": rcMstpXstPortCfgIndex,
       "rcMstpXstPortPriority": rcMstpXstPortPriority,
       "rcMstpXstPortAdminInternalPathCost": rcMstpXstPortAdminInternalPathCost}
)
