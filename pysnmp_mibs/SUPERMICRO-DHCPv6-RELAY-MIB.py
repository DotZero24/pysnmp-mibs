# SNMP MIB module (SUPERMICRO-DHCPv6-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DHCPv6-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:21 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsdhcpv6rly = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41)
)
if mibBuilder.loadTexts:
    fsdhcpv6rly.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcp6RlyNotify_ObjectIdentity = ObjectIdentity
fsDhcp6RlyNotify = _FsDhcp6RlyNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 0)
)
_FsDhcp6RlySystem_ObjectIdentity = ObjectIdentity
fsDhcp6RlySystem = _FsDhcp6RlySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1)
)


class _FsDhcp6RlyDebugTrace_Type(DisplayString):
    """Custom type fsDhcp6RlyDebugTrace based on DisplayString"""
    defaultValue = OctetString("critical")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsDhcp6RlyDebugTrace_Type.__name__ = "DisplayString"
_FsDhcp6RlyDebugTrace_Object = MibScalar
fsDhcp6RlyDebugTrace = _FsDhcp6RlyDebugTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 1),
    _FsDhcp6RlyDebugTrace_Type()
)
fsDhcp6RlyDebugTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyDebugTrace.setStatus("current")


class _FsDhcp6RlyTrapAdminControl_Type(Bits):
    """Custom type fsDhcp6RlyTrapAdminControl based on Bits"""
    namedValues = NamedValues(
        *(("none", 0),
          ("trapInvalidPacketIn", 1),
          ("trapMaxHopCount", 2))
    )

_FsDhcp6RlyTrapAdminControl_Type.__name__ = "Bits"
_FsDhcp6RlyTrapAdminControl_Object = MibScalar
fsDhcp6RlyTrapAdminControl = _FsDhcp6RlyTrapAdminControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 2),
    _FsDhcp6RlyTrapAdminControl_Type()
)
fsDhcp6RlyTrapAdminControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyTrapAdminControl.setStatus("current")


class _FsDhcp6RlySysLogAdminStatus_Type(Integer32):
    """Custom type fsDhcp6RlySysLogAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsDhcp6RlySysLogAdminStatus_Type.__name__ = "Integer32"
_FsDhcp6RlySysLogAdminStatus_Object = MibScalar
fsDhcp6RlySysLogAdminStatus = _FsDhcp6RlySysLogAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 3),
    _FsDhcp6RlySysLogAdminStatus_Type()
)
fsDhcp6RlySysLogAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlySysLogAdminStatus.setStatus("current")


class _FsDhcp6RlyListenPort_Type(Integer32):
    """Custom type fsDhcp6RlyListenPort based on Integer32"""
    defaultValue = 547

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDhcp6RlyListenPort_Type.__name__ = "Integer32"
_FsDhcp6RlyListenPort_Object = MibScalar
fsDhcp6RlyListenPort = _FsDhcp6RlyListenPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 4),
    _FsDhcp6RlyListenPort_Type()
)
fsDhcp6RlyListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyListenPort.setStatus("current")


class _FsDhcp6RlyClientTransmitPort_Type(Integer32):
    """Custom type fsDhcp6RlyClientTransmitPort based on Integer32"""
    defaultValue = 546

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDhcp6RlyClientTransmitPort_Type.__name__ = "Integer32"
_FsDhcp6RlyClientTransmitPort_Object = MibScalar
fsDhcp6RlyClientTransmitPort = _FsDhcp6RlyClientTransmitPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 5),
    _FsDhcp6RlyClientTransmitPort_Type()
)
fsDhcp6RlyClientTransmitPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyClientTransmitPort.setStatus("current")


class _FsDhcp6RlyServerTransmitPort_Type(Integer32):
    """Custom type fsDhcp6RlyServerTransmitPort based on Integer32"""
    defaultValue = 547

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsDhcp6RlyServerTransmitPort_Type.__name__ = "Integer32"
_FsDhcp6RlyServerTransmitPort_Object = MibScalar
fsDhcp6RlyServerTransmitPort = _FsDhcp6RlyServerTransmitPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 6),
    _FsDhcp6RlyServerTransmitPort_Type()
)
fsDhcp6RlyServerTransmitPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyServerTransmitPort.setStatus("current")


class _FsDhcp6RlyOption37Control_Type(Integer32):
    """Custom type fsDhcp6RlyOption37Control based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsDhcp6RlyOption37Control_Type.__name__ = "Integer32"
_FsDhcp6RlyOption37Control_Object = MibScalar
fsDhcp6RlyOption37Control = _FsDhcp6RlyOption37Control_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 1, 7),
    _FsDhcp6RlyOption37Control_Type()
)
fsDhcp6RlyOption37Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyOption37Control.setStatus("current")
_FsDhcp6RlyConfig_ObjectIdentity = ObjectIdentity
fsDhcp6RlyConfig = _FsDhcp6RlyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2)
)
_FsDhcp6RlyIfTable_Object = MibTable
fsDhcp6RlyIfTable = _FsDhcp6RlyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1)
)
if mibBuilder.loadTexts:
    fsDhcp6RlyIfTable.setStatus("current")
_FsDhcp6RlyIfEntry_Object = MibTableRow
fsDhcp6RlyIfEntry = _FsDhcp6RlyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1)
)
fsDhcp6RlyIfEntry.setIndexNames(
    (0, "SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyIfIndex"),
)
if mibBuilder.loadTexts:
    fsDhcp6RlyIfEntry.setStatus("current")


class _FsDhcp6RlyIfIndex_Type(Integer32):
    """Custom type fsDhcp6RlyIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDhcp6RlyIfIndex_Type.__name__ = "Integer32"
_FsDhcp6RlyIfIndex_Object = MibTableColumn
fsDhcp6RlyIfIndex = _FsDhcp6RlyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 1),
    _FsDhcp6RlyIfIndex_Type()
)
fsDhcp6RlyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfIndex.setStatus("current")


class _FsDhcp6RlyIfHopThreshold_Type(Integer32):
    """Custom type fsDhcp6RlyIfHopThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsDhcp6RlyIfHopThreshold_Type.__name__ = "Integer32"
_FsDhcp6RlyIfHopThreshold_Object = MibTableColumn
fsDhcp6RlyIfHopThreshold = _FsDhcp6RlyIfHopThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 3),
    _FsDhcp6RlyIfHopThreshold_Type()
)
fsDhcp6RlyIfHopThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfHopThreshold.setStatus("current")
_FsDhcp6RlyIfInformIn_Type = Counter32
_FsDhcp6RlyIfInformIn_Object = MibTableColumn
fsDhcp6RlyIfInformIn = _FsDhcp6RlyIfInformIn_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 4),
    _FsDhcp6RlyIfInformIn_Type()
)
fsDhcp6RlyIfInformIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfInformIn.setStatus("current")
_FsDhcp6RlyIfRelayForwIn_Type = Counter32
_FsDhcp6RlyIfRelayForwIn_Object = MibTableColumn
fsDhcp6RlyIfRelayForwIn = _FsDhcp6RlyIfRelayForwIn_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 5),
    _FsDhcp6RlyIfRelayForwIn_Type()
)
fsDhcp6RlyIfRelayForwIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRelayForwIn.setStatus("current")
_FsDhcp6RlyIfRelayReplyIn_Type = Counter32
_FsDhcp6RlyIfRelayReplyIn_Object = MibTableColumn
fsDhcp6RlyIfRelayReplyIn = _FsDhcp6RlyIfRelayReplyIn_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 6),
    _FsDhcp6RlyIfRelayReplyIn_Type()
)
fsDhcp6RlyIfRelayReplyIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRelayReplyIn.setStatus("current")
_FsDhcp6RlyIfInvalidPktIn_Type = Counter32
_FsDhcp6RlyIfInvalidPktIn_Object = MibTableColumn
fsDhcp6RlyIfInvalidPktIn = _FsDhcp6RlyIfInvalidPktIn_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 10),
    _FsDhcp6RlyIfInvalidPktIn_Type()
)
fsDhcp6RlyIfInvalidPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfInvalidPktIn.setStatus("current")
_FsDhcp6RlyIfCounterRest_Type = TruthValue
_FsDhcp6RlyIfCounterRest_Object = MibTableColumn
fsDhcp6RlyIfCounterRest = _FsDhcp6RlyIfCounterRest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 11),
    _FsDhcp6RlyIfCounterRest_Type()
)
fsDhcp6RlyIfCounterRest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfCounterRest.setStatus("current")
_FsDhcp6RlyIfRowStatus_Type = RowStatus
_FsDhcp6RlyIfRowStatus_Object = MibTableColumn
fsDhcp6RlyIfRowStatus = _FsDhcp6RlyIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 12),
    _FsDhcp6RlyIfRowStatus_Type()
)
fsDhcp6RlyIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRowStatus.setStatus("current")


class _FsDhcp6RlyIfRemoteIdOption_Type(Integer32):
    """Custom type fsDhcp6RlyIfRemoteIdOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("duid", 1),
          ("switchName", 2),
          ("mgmtIp", 3),
          ("userDefined", 4))
    )


_FsDhcp6RlyIfRemoteIdOption_Type.__name__ = "Integer32"
_FsDhcp6RlyIfRemoteIdOption_Object = MibTableColumn
fsDhcp6RlyIfRemoteIdOption = _FsDhcp6RlyIfRemoteIdOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 13),
    _FsDhcp6RlyIfRemoteIdOption_Type()
)
fsDhcp6RlyIfRemoteIdOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRemoteIdOption.setStatus("current")


class _FsDhcp6RlyIfRemoteIdDUID_Type(OctetString):
    """Custom type fsDhcp6RlyIfRemoteIdDUID based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsDhcp6RlyIfRemoteIdDUID_Type.__name__ = "OctetString"
_FsDhcp6RlyIfRemoteIdDUID_Object = MibTableColumn
fsDhcp6RlyIfRemoteIdDUID = _FsDhcp6RlyIfRemoteIdDUID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 14),
    _FsDhcp6RlyIfRemoteIdDUID_Type()
)
fsDhcp6RlyIfRemoteIdDUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRemoteIdDUID.setStatus("current")


class _FsDhcp6RlyIfRemoteIdOptionValue_Type(DisplayString):
    """Custom type fsDhcp6RlyIfRemoteIdOptionValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsDhcp6RlyIfRemoteIdOptionValue_Type.__name__ = "DisplayString"
_FsDhcp6RlyIfRemoteIdOptionValue_Object = MibTableColumn
fsDhcp6RlyIfRemoteIdOptionValue = _FsDhcp6RlyIfRemoteIdOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 15),
    _FsDhcp6RlyIfRemoteIdOptionValue_Type()
)
fsDhcp6RlyIfRemoteIdOptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRemoteIdOptionValue.setStatus("current")


class _FsDhcp6RlyIfRemoteIdUserDefined_Type(DisplayString):
    """Custom type fsDhcp6RlyIfRemoteIdUserDefined based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsDhcp6RlyIfRemoteIdUserDefined_Type.__name__ = "DisplayString"
_FsDhcp6RlyIfRemoteIdUserDefined_Object = MibTableColumn
fsDhcp6RlyIfRemoteIdUserDefined = _FsDhcp6RlyIfRemoteIdUserDefined_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 1, 1, 16),
    _FsDhcp6RlyIfRemoteIdUserDefined_Type()
)
fsDhcp6RlyIfRemoteIdUserDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyIfRemoteIdUserDefined.setStatus("current")
_FsDhcp6RlySrvAddressTable_Object = MibTable
fsDhcp6RlySrvAddressTable = _FsDhcp6RlySrvAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 2)
)
if mibBuilder.loadTexts:
    fsDhcp6RlySrvAddressTable.setStatus("current")
_FsDhcp6RlySrvAddressEntry_Object = MibTableRow
fsDhcp6RlySrvAddressEntry = _FsDhcp6RlySrvAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 2, 1)
)
fsDhcp6RlySrvAddressEntry.setIndexNames(
    (0, "SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyInIfIndex"),
    (0, "SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlySrvAddress"),
)
if mibBuilder.loadTexts:
    fsDhcp6RlySrvAddressEntry.setStatus("current")


class _FsDhcp6RlyInIfIndex_Type(Integer32):
    """Custom type fsDhcp6RlyInIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDhcp6RlyInIfIndex_Type.__name__ = "Integer32"
_FsDhcp6RlyInIfIndex_Object = MibTableColumn
fsDhcp6RlyInIfIndex = _FsDhcp6RlyInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 2, 1, 1),
    _FsDhcp6RlyInIfIndex_Type()
)
fsDhcp6RlyInIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcp6RlyInIfIndex.setStatus("current")


class _FsDhcp6RlySrvAddress_Type(OctetString):
    """Custom type fsDhcp6RlySrvAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsDhcp6RlySrvAddress_Type.__name__ = "OctetString"
_FsDhcp6RlySrvAddress_Object = MibTableColumn
fsDhcp6RlySrvAddress = _FsDhcp6RlySrvAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 2, 1, 2),
    _FsDhcp6RlySrvAddress_Type()
)
fsDhcp6RlySrvAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcp6RlySrvAddress.setStatus("current")
_FsDhcp6RlySrvAddressRowStatus_Type = RowStatus
_FsDhcp6RlySrvAddressRowStatus_Object = MibTableColumn
fsDhcp6RlySrvAddressRowStatus = _FsDhcp6RlySrvAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 2, 1, 3),
    _FsDhcp6RlySrvAddressRowStatus_Type()
)
fsDhcp6RlySrvAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlySrvAddressRowStatus.setStatus("current")
_FsDhcp6RlyOutIfTable_Object = MibTable
fsDhcp6RlyOutIfTable = _FsDhcp6RlyOutIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 3)
)
if mibBuilder.loadTexts:
    fsDhcp6RlyOutIfTable.setStatus("current")
_FsDhcp6RlyOutIfEntry_Object = MibTableRow
fsDhcp6RlyOutIfEntry = _FsDhcp6RlyOutIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 3, 1)
)
fsDhcp6RlyOutIfEntry.setIndexNames(
    (0, "SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyInIfIndex"),
    (0, "SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlySrvAddress"),
    (0, "SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyOutIfIndex"),
)
if mibBuilder.loadTexts:
    fsDhcp6RlyOutIfEntry.setStatus("current")


class _FsDhcp6RlyOutIfIndex_Type(Integer32):
    """Custom type fsDhcp6RlyOutIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsDhcp6RlyOutIfIndex_Type.__name__ = "Integer32"
_FsDhcp6RlyOutIfIndex_Object = MibTableColumn
fsDhcp6RlyOutIfIndex = _FsDhcp6RlyOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 3, 1, 1),
    _FsDhcp6RlyOutIfIndex_Type()
)
fsDhcp6RlyOutIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcp6RlyOutIfIndex.setStatus("current")
_FsDhcp6RlyOutIfRowStatus_Type = RowStatus
_FsDhcp6RlyOutIfRowStatus_Object = MibTableColumn
fsDhcp6RlyOutIfRowStatus = _FsDhcp6RlyOutIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 2, 3, 1, 2),
    _FsDhcp6RlyOutIfRowStatus_Type()
)
fsDhcp6RlyOutIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcp6RlyOutIfRowStatus.setStatus("current")
_FsDhcp6RlyTraps_ObjectIdentity = ObjectIdentity
fsDhcp6RlyTraps = _FsDhcp6RlyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 3)
)
_FsDhcp6RlyTrapIfIndex_Type = Integer32
_FsDhcp6RlyTrapIfIndex_Object = MibScalar
fsDhcp6RlyTrapIfIndex = _FsDhcp6RlyTrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 3, 1),
    _FsDhcp6RlyTrapIfIndex_Type()
)
fsDhcp6RlyTrapIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDhcp6RlyTrapIfIndex.setStatus("current")
_FsDhcp6RlyTrapInvalidMsgType_Type = Integer32
_FsDhcp6RlyTrapInvalidMsgType_Object = MibScalar
fsDhcp6RlyTrapInvalidMsgType = _FsDhcp6RlyTrapInvalidMsgType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 3, 2),
    _FsDhcp6RlyTrapInvalidMsgType_Type()
)
fsDhcp6RlyTrapInvalidMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDhcp6RlyTrapInvalidMsgType.setStatus("current")

# Managed Objects groups


# Notification objects

fsDhcp6RlyRlyInvalidPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 0, 1)
)
fsDhcp6RlyRlyInvalidPacketTrap.setObjects(
      *(("SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyTrapInvalidMsgType"),
        ("SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyTrapIfIndex"))
)
if mibBuilder.loadTexts:
    fsDhcp6RlyRlyInvalidPacketTrap.setStatus(
        "current"
    )

fsDhcp6RlyRlyMaxHopCountTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 41, 0, 2)
)
fsDhcp6RlyRlyMaxHopCountTrap.setObjects(
    ("SUPERMICRO-DHCPv6-RELAY-MIB", "fsDhcp6RlyTrapIfIndex")
)
if mibBuilder.loadTexts:
    fsDhcp6RlyRlyMaxHopCountTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DHCPv6-RELAY-MIB",
    **{"fsdhcpv6rly": fsdhcpv6rly,
       "fsDhcp6RlyNotify": fsDhcp6RlyNotify,
       "fsDhcp6RlyRlyInvalidPacketTrap": fsDhcp6RlyRlyInvalidPacketTrap,
       "fsDhcp6RlyRlyMaxHopCountTrap": fsDhcp6RlyRlyMaxHopCountTrap,
       "fsDhcp6RlySystem": fsDhcp6RlySystem,
       "fsDhcp6RlyDebugTrace": fsDhcp6RlyDebugTrace,
       "fsDhcp6RlyTrapAdminControl": fsDhcp6RlyTrapAdminControl,
       "fsDhcp6RlySysLogAdminStatus": fsDhcp6RlySysLogAdminStatus,
       "fsDhcp6RlyListenPort": fsDhcp6RlyListenPort,
       "fsDhcp6RlyClientTransmitPort": fsDhcp6RlyClientTransmitPort,
       "fsDhcp6RlyServerTransmitPort": fsDhcp6RlyServerTransmitPort,
       "fsDhcp6RlyOption37Control": fsDhcp6RlyOption37Control,
       "fsDhcp6RlyConfig": fsDhcp6RlyConfig,
       "fsDhcp6RlyIfTable": fsDhcp6RlyIfTable,
       "fsDhcp6RlyIfEntry": fsDhcp6RlyIfEntry,
       "fsDhcp6RlyIfIndex": fsDhcp6RlyIfIndex,
       "fsDhcp6RlyIfHopThreshold": fsDhcp6RlyIfHopThreshold,
       "fsDhcp6RlyIfInformIn": fsDhcp6RlyIfInformIn,
       "fsDhcp6RlyIfRelayForwIn": fsDhcp6RlyIfRelayForwIn,
       "fsDhcp6RlyIfRelayReplyIn": fsDhcp6RlyIfRelayReplyIn,
       "fsDhcp6RlyIfInvalidPktIn": fsDhcp6RlyIfInvalidPktIn,
       "fsDhcp6RlyIfCounterRest": fsDhcp6RlyIfCounterRest,
       "fsDhcp6RlyIfRowStatus": fsDhcp6RlyIfRowStatus,
       "fsDhcp6RlyIfRemoteIdOption": fsDhcp6RlyIfRemoteIdOption,
       "fsDhcp6RlyIfRemoteIdDUID": fsDhcp6RlyIfRemoteIdDUID,
       "fsDhcp6RlyIfRemoteIdOptionValue": fsDhcp6RlyIfRemoteIdOptionValue,
       "fsDhcp6RlyIfRemoteIdUserDefined": fsDhcp6RlyIfRemoteIdUserDefined,
       "fsDhcp6RlySrvAddressTable": fsDhcp6RlySrvAddressTable,
       "fsDhcp6RlySrvAddressEntry": fsDhcp6RlySrvAddressEntry,
       "fsDhcp6RlyInIfIndex": fsDhcp6RlyInIfIndex,
       "fsDhcp6RlySrvAddress": fsDhcp6RlySrvAddress,
       "fsDhcp6RlySrvAddressRowStatus": fsDhcp6RlySrvAddressRowStatus,
       "fsDhcp6RlyOutIfTable": fsDhcp6RlyOutIfTable,
       "fsDhcp6RlyOutIfEntry": fsDhcp6RlyOutIfEntry,
       "fsDhcp6RlyOutIfIndex": fsDhcp6RlyOutIfIndex,
       "fsDhcp6RlyOutIfRowStatus": fsDhcp6RlyOutIfRowStatus,
       "fsDhcp6RlyTraps": fsDhcp6RlyTraps,
       "fsDhcp6RlyTrapIfIndex": fsDhcp6RlyTrapIfIndex,
       "fsDhcp6RlyTrapInvalidMsgType": fsDhcp6RlyTrapInvalidMsgType}
)
