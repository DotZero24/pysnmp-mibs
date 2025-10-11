# SNMP MIB module (AricentMIBridge-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/AricentMIBridge-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:33 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

futureMIBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 117)
)
if mibBuilder.loadTexts:
    futureMIBridgeMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



# MIB Managed Objects in the order of their OIDs

_FsMIDot1dFutureBridge_ObjectIdentity = ObjectIdentity
fsMIDot1dFutureBridge = _FsMIDot1dFutureBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1)
)
_FsMIDot1dFutureBase_ObjectIdentity = ObjectIdentity
fsMIDot1dFutureBase = _FsMIDot1dFutureBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1)
)
_FsMIDot1dFutureBaseTable_Object = MibTable
fsMIDot1dFutureBaseTable = _FsMIDot1dFutureBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1dFutureBaseTable.setStatus("current")
_FsMIDot1dFutureBaseEntry_Object = MibTableRow
fsMIDot1dFutureBaseEntry = _FsMIDot1dFutureBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1)
)
fsMIDot1dFutureBaseEntry.setIndexNames(
    (0, "AricentMIBridge-MIB", "fsMIDot1dFutureBaseContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1dFutureBaseEntry.setStatus("current")


class _FsMIDot1dFutureBaseContextId_Type(Integer32):
    """Custom type fsMIDot1dFutureBaseContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1dFutureBaseContextId_Type.__name__ = "Integer32"
_FsMIDot1dFutureBaseContextId_Object = MibTableColumn
fsMIDot1dFutureBaseContextId = _FsMIDot1dFutureBaseContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 1),
    _FsMIDot1dFutureBaseContextId_Type()
)
fsMIDot1dFutureBaseContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dFutureBaseContextId.setStatus("current")


class _FsMIDot1dBridgeSystemControl_Type(Integer32):
    """Custom type fsMIDot1dBridgeSystemControl based on Integer32"""
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


_FsMIDot1dBridgeSystemControl_Type.__name__ = "Integer32"
_FsMIDot1dBridgeSystemControl_Object = MibTableColumn
fsMIDot1dBridgeSystemControl = _FsMIDot1dBridgeSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 2),
    _FsMIDot1dBridgeSystemControl_Type()
)
fsMIDot1dBridgeSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1dBridgeSystemControl.setStatus("current")


class _FsMIDot1dBaseBridgeStatus_Type(Integer32):
    """Custom type fsMIDot1dBaseBridgeStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("downwithallinterfacesdown", 3))
    )


_FsMIDot1dBaseBridgeStatus_Type.__name__ = "Integer32"
_FsMIDot1dBaseBridgeStatus_Object = MibTableColumn
fsMIDot1dBaseBridgeStatus = _FsMIDot1dBaseBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 3),
    _FsMIDot1dBaseBridgeStatus_Type()
)
fsMIDot1dBaseBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1dBaseBridgeStatus.setStatus("current")


class _FsMIDot1dBaseBridgeCRCStatus_Type(Integer32):
    """Custom type fsMIDot1dBaseBridgeCRCStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("withCRC", 1),
          ("withoutCRC", 2))
    )


_FsMIDot1dBaseBridgeCRCStatus_Type.__name__ = "Integer32"
_FsMIDot1dBaseBridgeCRCStatus_Object = MibTableColumn
fsMIDot1dBaseBridgeCRCStatus = _FsMIDot1dBaseBridgeCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 4),
    _FsMIDot1dBaseBridgeCRCStatus_Type()
)
fsMIDot1dBaseBridgeCRCStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1dBaseBridgeCRCStatus.setStatus("current")


class _FsMIDot1dBaseBridgeDebug_Type(Integer32):
    """Custom type fsMIDot1dBaseBridgeDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIDot1dBaseBridgeDebug_Type.__name__ = "Integer32"
_FsMIDot1dBaseBridgeDebug_Object = MibTableColumn
fsMIDot1dBaseBridgeDebug = _FsMIDot1dBaseBridgeDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 5),
    _FsMIDot1dBaseBridgeDebug_Type()
)
fsMIDot1dBaseBridgeDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1dBaseBridgeDebug.setStatus("current")


class _FsMIDot1dBaseBridgeTrace_Type(Integer32):
    """Custom type fsMIDot1dBaseBridgeTrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIDot1dBaseBridgeTrace_Type.__name__ = "Integer32"
_FsMIDot1dBaseBridgeTrace_Object = MibTableColumn
fsMIDot1dBaseBridgeTrace = _FsMIDot1dBaseBridgeTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 6),
    _FsMIDot1dBaseBridgeTrace_Type()
)
fsMIDot1dBaseBridgeTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1dBaseBridgeTrace.setStatus("current")


class _FsMIDot1dBaseBridgeMaxFwdDbEntries_Type(Integer32):
    """Custom type fsMIDot1dBaseBridgeMaxFwdDbEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIDot1dBaseBridgeMaxFwdDbEntries_Type.__name__ = "Integer32"
_FsMIDot1dBaseBridgeMaxFwdDbEntries_Object = MibTableColumn
fsMIDot1dBaseBridgeMaxFwdDbEntries = _FsMIDot1dBaseBridgeMaxFwdDbEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 1, 1, 7),
    _FsMIDot1dBaseBridgeMaxFwdDbEntries_Type()
)
fsMIDot1dBaseBridgeMaxFwdDbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1dBaseBridgeMaxFwdDbEntries.setStatus("current")
_FsMIDot1dFutureBasePortTable_Object = MibTable
fsMIDot1dFutureBasePortTable = _FsMIDot1dFutureBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsMIDot1dFutureBasePortTable.setStatus("current")
_FsMIDot1dFutureBasePortEntry_Object = MibTableRow
fsMIDot1dFutureBasePortEntry = _FsMIDot1dFutureBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1)
)
fsMIDot1dFutureBasePortEntry.setIndexNames(
    (0, "AricentMIBridge-MIB", "fsMIDot1dFutureBasePort"),
)
if mibBuilder.loadTexts:
    fsMIDot1dFutureBasePortEntry.setStatus("current")


class _FsMIDot1dFutureBasePort_Type(Integer32):
    """Custom type fsMIDot1dFutureBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIDot1dFutureBasePort_Type.__name__ = "Integer32"
_FsMIDot1dFutureBasePort_Object = MibTableColumn
fsMIDot1dFutureBasePort = _FsMIDot1dFutureBasePort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 1),
    _FsMIDot1dFutureBasePort_Type()
)
fsMIDot1dFutureBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dFutureBasePort.setStatus("current")


class _FsMIDot1dBasePortAdminStatus_Type(Integer32):
    """Custom type fsMIDot1dBasePortAdminStatus based on Integer32"""
    defaultValue = 1

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


_FsMIDot1dBasePortAdminStatus_Type.__name__ = "Integer32"
_FsMIDot1dBasePortAdminStatus_Object = MibTableColumn
fsMIDot1dBasePortAdminStatus = _FsMIDot1dBasePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 2),
    _FsMIDot1dBasePortAdminStatus_Type()
)
fsMIDot1dBasePortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortAdminStatus.setStatus("current")


class _FsMIDot1dBasePortOperStatus_Type(Integer32):
    """Custom type fsMIDot1dBasePortOperStatus based on Integer32"""
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


_FsMIDot1dBasePortOperStatus_Type.__name__ = "Integer32"
_FsMIDot1dBasePortOperStatus_Object = MibTableColumn
fsMIDot1dBasePortOperStatus = _FsMIDot1dBasePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 3),
    _FsMIDot1dBasePortOperStatus_Type()
)
fsMIDot1dBasePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortOperStatus.setStatus("current")


class _FsMIDot1dBasePortBcastStatus_Type(Integer32):
    """Custom type fsMIDot1dBasePortBcastStatus based on Integer32"""
    defaultValue = 1

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


_FsMIDot1dBasePortBcastStatus_Type.__name__ = "Integer32"
_FsMIDot1dBasePortBcastStatus_Object = MibTableColumn
fsMIDot1dBasePortBcastStatus = _FsMIDot1dBasePortBcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 4),
    _FsMIDot1dBasePortBcastStatus_Type()
)
fsMIDot1dBasePortBcastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortBcastStatus.setStatus("current")


class _FsMIDot1dBasePortFilterNumber_Type(Integer32):
    """Custom type fsMIDot1dBasePortFilterNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FsMIDot1dBasePortFilterNumber_Type.__name__ = "Integer32"
_FsMIDot1dBasePortFilterNumber_Object = MibTableColumn
fsMIDot1dBasePortFilterNumber = _FsMIDot1dBasePortFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 5),
    _FsMIDot1dBasePortFilterNumber_Type()
)
fsMIDot1dBasePortFilterNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortFilterNumber.setStatus("current")


class _FsMIDot1dBasePortMcastNumber_Type(Integer32):
    """Custom type fsMIDot1dBasePortMcastNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FsMIDot1dBasePortMcastNumber_Type.__name__ = "Integer32"
_FsMIDot1dBasePortMcastNumber_Object = MibTableColumn
fsMIDot1dBasePortMcastNumber = _FsMIDot1dBasePortMcastNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 6),
    _FsMIDot1dBasePortMcastNumber_Type()
)
fsMIDot1dBasePortMcastNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortMcastNumber.setStatus("current")
_FsMIDot1dBasePortBcastOutFrames_Type = Counter32
_FsMIDot1dBasePortBcastOutFrames_Object = MibTableColumn
fsMIDot1dBasePortBcastOutFrames = _FsMIDot1dBasePortBcastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 7),
    _FsMIDot1dBasePortBcastOutFrames_Type()
)
fsMIDot1dBasePortBcastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortBcastOutFrames.setStatus("current")
_FsMIDot1dBasePortMcastOutFrames_Type = Counter32
_FsMIDot1dBasePortMcastOutFrames_Object = MibTableColumn
fsMIDot1dBasePortMcastOutFrames = _FsMIDot1dBasePortMcastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 1, 2, 1, 8),
    _FsMIDot1dBasePortMcastOutFrames_Type()
)
fsMIDot1dBasePortMcastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1dBasePortMcastOutFrames.setStatus("current")
_FsMIDot1dFutureTp_ObjectIdentity = ObjectIdentity
fsMIDot1dFutureTp = _FsMIDot1dFutureTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2)
)
_FsMIDot1dFutureTpPortTable_Object = MibTable
fsMIDot1dFutureTpPortTable = _FsMIDot1dFutureTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1dFutureTpPortTable.setStatus("current")
_FsMIDot1dFutureTpPortEntry_Object = MibTableRow
fsMIDot1dFutureTpPortEntry = _FsMIDot1dFutureTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2, 1, 1)
)
fsMIDot1dFutureTpPortEntry.setIndexNames(
    (0, "AricentMIBridge-MIB", "fsMIDot1dFutureTpPort"),
)
if mibBuilder.loadTexts:
    fsMIDot1dFutureTpPortEntry.setStatus("current")


class _FsMIDot1dFutureTpPort_Type(Integer32):
    """Custom type fsMIDot1dFutureTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIDot1dFutureTpPort_Type.__name__ = "Integer32"
_FsMIDot1dFutureTpPort_Object = MibTableColumn
fsMIDot1dFutureTpPort = _FsMIDot1dFutureTpPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2, 1, 1, 1),
    _FsMIDot1dFutureTpPort_Type()
)
fsMIDot1dFutureTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dFutureTpPort.setStatus("current")
_FsMIDot1dTpPortInProtoDiscards_Type = Counter32
_FsMIDot1dTpPortInProtoDiscards_Object = MibTableColumn
fsMIDot1dTpPortInProtoDiscards = _FsMIDot1dTpPortInProtoDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2, 1, 1, 2),
    _FsMIDot1dTpPortInProtoDiscards_Type()
)
fsMIDot1dTpPortInProtoDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1dTpPortInProtoDiscards.setStatus("current")
_FsMIDot1dTpPortInFilterDiscards_Type = Counter32
_FsMIDot1dTpPortInFilterDiscards_Object = MibTableColumn
fsMIDot1dTpPortInFilterDiscards = _FsMIDot1dTpPortInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2, 1, 1, 3),
    _FsMIDot1dTpPortInFilterDiscards_Type()
)
fsMIDot1dTpPortInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1dTpPortInFilterDiscards.setStatus("current")


class _FsMIDot1dTpPortProtocolFilterMask_Type(Integer32):
    """Custom type fsMIDot1dTpPortProtocolFilterMask based on Integer32"""
    defaultValue = 0


_FsMIDot1dTpPortProtocolFilterMask_Type.__name__ = "Integer32"
_FsMIDot1dTpPortProtocolFilterMask_Object = MibTableColumn
fsMIDot1dTpPortProtocolFilterMask = _FsMIDot1dTpPortProtocolFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 2, 1, 1, 4),
    _FsMIDot1dTpPortProtocolFilterMask_Type()
)
fsMIDot1dTpPortProtocolFilterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dTpPortProtocolFilterMask.setStatus("current")
_FsMIDot1dFilter_ObjectIdentity = ObjectIdentity
fsMIDot1dFilter = _FsMIDot1dFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3)
)
_FsMIDot1dFilterTable_Object = MibTable
fsMIDot1dFilterTable = _FsMIDot1dFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1dFilterTable.setStatus("current")
_FsMIDot1dFilterEntry_Object = MibTableRow
fsMIDot1dFilterEntry = _FsMIDot1dFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1)
)
fsMIDot1dFilterEntry.setIndexNames(
    (0, "AricentMIBridge-MIB", "fsMIDot1dFutureBaseContextId"),
    (0, "AricentMIBridge-MIB", "fsMIDot1dFilterNumber"),
    (0, "AricentMIBridge-MIB", "fsMIDot1dFilterSrcAddress"),
    (0, "AricentMIBridge-MIB", "fsMIDot1dFilterDstAddress"),
)
if mibBuilder.loadTexts:
    fsMIDot1dFilterEntry.setStatus("current")


class _FsMIDot1dFilterNumber_Type(Integer32):
    """Custom type fsMIDot1dFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsMIDot1dFilterNumber_Type.__name__ = "Integer32"
_FsMIDot1dFilterNumber_Object = MibTableColumn
fsMIDot1dFilterNumber = _FsMIDot1dFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1, 1),
    _FsMIDot1dFilterNumber_Type()
)
fsMIDot1dFilterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dFilterNumber.setStatus("current")
_FsMIDot1dFilterSrcAddress_Type = MacAddress
_FsMIDot1dFilterSrcAddress_Object = MibTableColumn
fsMIDot1dFilterSrcAddress = _FsMIDot1dFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1, 2),
    _FsMIDot1dFilterSrcAddress_Type()
)
fsMIDot1dFilterSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dFilterSrcAddress.setStatus("current")


class _FsMIDot1dFilterSrcMask_Type(MacAddress):
    """Custom type fsMIDot1dFilterSrcMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_FsMIDot1dFilterSrcMask_Type.__name__ = "MacAddress"
_FsMIDot1dFilterSrcMask_Object = MibTableColumn
fsMIDot1dFilterSrcMask = _FsMIDot1dFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1, 3),
    _FsMIDot1dFilterSrcMask_Type()
)
fsMIDot1dFilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dFilterSrcMask.setStatus("current")
_FsMIDot1dFilterDstAddress_Type = MacAddress
_FsMIDot1dFilterDstAddress_Object = MibTableColumn
fsMIDot1dFilterDstAddress = _FsMIDot1dFilterDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1, 4),
    _FsMIDot1dFilterDstAddress_Type()
)
fsMIDot1dFilterDstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dFilterDstAddress.setStatus("current")


class _FsMIDot1dFilterDstMask_Type(MacAddress):
    """Custom type fsMIDot1dFilterDstMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_FsMIDot1dFilterDstMask_Type.__name__ = "MacAddress"
_FsMIDot1dFilterDstMask_Object = MibTableColumn
fsMIDot1dFilterDstMask = _FsMIDot1dFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1, 5),
    _FsMIDot1dFilterDstMask_Type()
)
fsMIDot1dFilterDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dFilterDstMask.setStatus("current")


class _FsMIDot1dFilterPermiss_Type(Integer32):
    """Custom type fsMIDot1dFilterPermiss based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("allow", 2),
          ("invalid", 3))
    )


_FsMIDot1dFilterPermiss_Type.__name__ = "Integer32"
_FsMIDot1dFilterPermiss_Object = MibTableColumn
fsMIDot1dFilterPermiss = _FsMIDot1dFilterPermiss_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 3, 1, 1, 6),
    _FsMIDot1dFilterPermiss_Type()
)
fsMIDot1dFilterPermiss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dFilterPermiss.setStatus("current")
_FsMIDot1dMcast_ObjectIdentity = ObjectIdentity
fsMIDot1dMcast = _FsMIDot1dMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 4)
)
_FsMIDot1dMcastTable_Object = MibTable
fsMIDot1dMcastTable = _FsMIDot1dMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1dMcastTable.setStatus("current")
_FsMIDot1dMcastEntry_Object = MibTableRow
fsMIDot1dMcastEntry = _FsMIDot1dMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 4, 1, 1)
)
fsMIDot1dMcastEntry.setIndexNames(
    (0, "AricentMIBridge-MIB", "fsMIDot1dFutureBaseContextId"),
    (0, "AricentMIBridge-MIB", "fsMIDot1dMcastMacaddress"),
    (0, "AricentMIBridge-MIB", "fsMIDot1dMlistNumber"),
)
if mibBuilder.loadTexts:
    fsMIDot1dMcastEntry.setStatus("current")


class _FsMIDot1dMlistNumber_Type(Integer32):
    """Custom type fsMIDot1dMlistNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsMIDot1dMlistNumber_Type.__name__ = "Integer32"
_FsMIDot1dMlistNumber_Object = MibTableColumn
fsMIDot1dMlistNumber = _FsMIDot1dMlistNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 4, 1, 1, 1),
    _FsMIDot1dMlistNumber_Type()
)
fsMIDot1dMlistNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dMlistNumber.setStatus("current")
_FsMIDot1dMcastMacaddress_Type = MacAddress
_FsMIDot1dMcastMacaddress_Object = MibTableColumn
fsMIDot1dMcastMacaddress = _FsMIDot1dMcastMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 4, 1, 1, 2),
    _FsMIDot1dMcastMacaddress_Type()
)
fsMIDot1dMcastMacaddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1dMcastMacaddress.setStatus("current")


class _FsMIDot1dMcastPermiss_Type(Integer32):
    """Custom type fsMIDot1dMcastPermiss based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("allow", 2),
          ("invalid", 3))
    )


_FsMIDot1dMcastPermiss_Type.__name__ = "Integer32"
_FsMIDot1dMcastPermiss_Object = MibTableColumn
fsMIDot1dMcastPermiss = _FsMIDot1dMcastPermiss_Object(
    (1, 3, 6, 1, 4, 1, 2076, 117, 1, 4, 1, 1, 3),
    _FsMIDot1dMcastPermiss_Type()
)
fsMIDot1dMcastPermiss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIDot1dMcastPermiss.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AricentMIBridge-MIB",
    **{"BridgeId": BridgeId,
       "futureMIBridgeMIB": futureMIBridgeMIB,
       "fsMIDot1dFutureBridge": fsMIDot1dFutureBridge,
       "fsMIDot1dFutureBase": fsMIDot1dFutureBase,
       "fsMIDot1dFutureBaseTable": fsMIDot1dFutureBaseTable,
       "fsMIDot1dFutureBaseEntry": fsMIDot1dFutureBaseEntry,
       "fsMIDot1dFutureBaseContextId": fsMIDot1dFutureBaseContextId,
       "fsMIDot1dBridgeSystemControl": fsMIDot1dBridgeSystemControl,
       "fsMIDot1dBaseBridgeStatus": fsMIDot1dBaseBridgeStatus,
       "fsMIDot1dBaseBridgeCRCStatus": fsMIDot1dBaseBridgeCRCStatus,
       "fsMIDot1dBaseBridgeDebug": fsMIDot1dBaseBridgeDebug,
       "fsMIDot1dBaseBridgeTrace": fsMIDot1dBaseBridgeTrace,
       "fsMIDot1dBaseBridgeMaxFwdDbEntries": fsMIDot1dBaseBridgeMaxFwdDbEntries,
       "fsMIDot1dFutureBasePortTable": fsMIDot1dFutureBasePortTable,
       "fsMIDot1dFutureBasePortEntry": fsMIDot1dFutureBasePortEntry,
       "fsMIDot1dFutureBasePort": fsMIDot1dFutureBasePort,
       "fsMIDot1dBasePortAdminStatus": fsMIDot1dBasePortAdminStatus,
       "fsMIDot1dBasePortOperStatus": fsMIDot1dBasePortOperStatus,
       "fsMIDot1dBasePortBcastStatus": fsMIDot1dBasePortBcastStatus,
       "fsMIDot1dBasePortFilterNumber": fsMIDot1dBasePortFilterNumber,
       "fsMIDot1dBasePortMcastNumber": fsMIDot1dBasePortMcastNumber,
       "fsMIDot1dBasePortBcastOutFrames": fsMIDot1dBasePortBcastOutFrames,
       "fsMIDot1dBasePortMcastOutFrames": fsMIDot1dBasePortMcastOutFrames,
       "fsMIDot1dFutureTp": fsMIDot1dFutureTp,
       "fsMIDot1dFutureTpPortTable": fsMIDot1dFutureTpPortTable,
       "fsMIDot1dFutureTpPortEntry": fsMIDot1dFutureTpPortEntry,
       "fsMIDot1dFutureTpPort": fsMIDot1dFutureTpPort,
       "fsMIDot1dTpPortInProtoDiscards": fsMIDot1dTpPortInProtoDiscards,
       "fsMIDot1dTpPortInFilterDiscards": fsMIDot1dTpPortInFilterDiscards,
       "fsMIDot1dTpPortProtocolFilterMask": fsMIDot1dTpPortProtocolFilterMask,
       "fsMIDot1dFilter": fsMIDot1dFilter,
       "fsMIDot1dFilterTable": fsMIDot1dFilterTable,
       "fsMIDot1dFilterEntry": fsMIDot1dFilterEntry,
       "fsMIDot1dFilterNumber": fsMIDot1dFilterNumber,
       "fsMIDot1dFilterSrcAddress": fsMIDot1dFilterSrcAddress,
       "fsMIDot1dFilterSrcMask": fsMIDot1dFilterSrcMask,
       "fsMIDot1dFilterDstAddress": fsMIDot1dFilterDstAddress,
       "fsMIDot1dFilterDstMask": fsMIDot1dFilterDstMask,
       "fsMIDot1dFilterPermiss": fsMIDot1dFilterPermiss,
       "fsMIDot1dMcast": fsMIDot1dMcast,
       "fsMIDot1dMcastTable": fsMIDot1dMcastTable,
       "fsMIDot1dMcastEntry": fsMIDot1dMcastEntry,
       "fsMIDot1dMlistNumber": fsMIDot1dMlistNumber,
       "fsMIDot1dMcastMacaddress": fsMIDot1dMcastMacaddress,
       "fsMIDot1dMcastPermiss": fsMIDot1dMcastPermiss}
)
