# SNMP MIB module (ARICENT-DHCP-RLY-MI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-DHCP-RLY-MI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:33 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futureMIDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92)
)
if mibBuilder.loadTexts:
    futureMIDhcpRelay.setRevisions(
        ("2014-10-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIDhcpRelay_ObjectIdentity = ObjectIdentity
fsMIDhcpRelay = _FsMIDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 1)
)


class _FsMIDhcpConfigGblTraceLevel_Type(Integer32):
    """Custom type fsMIDhcpConfigGblTraceLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIDhcpConfigGblTraceLevel_Type.__name__ = "Integer32"
_FsMIDhcpConfigGblTraceLevel_Object = MibScalar
fsMIDhcpConfigGblTraceLevel = _FsMIDhcpConfigGblTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 1, 1),
    _FsMIDhcpConfigGblTraceLevel_Type()
)
fsMIDhcpConfigGblTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpConfigGblTraceLevel.setStatus("current")
_FsMIDhcpRelayTable_ObjectIdentity = ObjectIdentity
fsMIDhcpRelayTable = _FsMIDhcpRelayTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2)
)
_FsMIDhcpContextTable_Object = MibTable
fsMIDhcpContextTable = _FsMIDhcpContextTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIDhcpContextTable.setStatus("current")
_FsMIDhcpContextEntry_Object = MibTableRow
fsMIDhcpContextEntry = _FsMIDhcpContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1)
)
fsMIDhcpContextEntry.setIndexNames(
    (0, "ARICENT-DHCP-RLY-MI-MIB", "fsMIDhcpContextId"),
)
if mibBuilder.loadTexts:
    fsMIDhcpContextEntry.setStatus("current")


class _FsMIDhcpContextId_Type(Integer32):
    """Custom type fsMIDhcpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDhcpContextId_Type.__name__ = "Integer32"
_FsMIDhcpContextId_Object = MibTableColumn
fsMIDhcpContextId = _FsMIDhcpContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 1),
    _FsMIDhcpContextId_Type()
)
fsMIDhcpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDhcpContextId.setStatus("current")


class _FsMIDhcpRelaying_Type(Integer32):
    """Custom type fsMIDhcpRelaying based on Integer32"""
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


_FsMIDhcpRelaying_Type.__name__ = "Integer32"
_FsMIDhcpRelaying_Object = MibTableColumn
fsMIDhcpRelaying = _FsMIDhcpRelaying_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 2),
    _FsMIDhcpRelaying_Type()
)
fsMIDhcpRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelaying.setStatus("current")


class _FsMIDhcpRelayServersOnly_Type(Integer32):
    """Custom type fsMIDhcpRelayServersOnly based on Integer32"""
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


_FsMIDhcpRelayServersOnly_Type.__name__ = "Integer32"
_FsMIDhcpRelayServersOnly_Object = MibTableColumn
fsMIDhcpRelayServersOnly = _FsMIDhcpRelayServersOnly_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 3),
    _FsMIDhcpRelayServersOnly_Type()
)
fsMIDhcpRelayServersOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayServersOnly.setStatus("current")


class _FsMIDhcpRelaySecsThreshold_Type(Integer32):
    """Custom type fsMIDhcpRelaySecsThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDhcpRelaySecsThreshold_Type.__name__ = "Integer32"
_FsMIDhcpRelaySecsThreshold_Object = MibTableColumn
fsMIDhcpRelaySecsThreshold = _FsMIDhcpRelaySecsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 4),
    _FsMIDhcpRelaySecsThreshold_Type()
)
fsMIDhcpRelaySecsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelaySecsThreshold.setStatus("current")


class _FsMIDhcpRelayHopsThreshold_Type(Integer32):
    """Custom type fsMIDhcpRelayHopsThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FsMIDhcpRelayHopsThreshold_Type.__name__ = "Integer32"
_FsMIDhcpRelayHopsThreshold_Object = MibTableColumn
fsMIDhcpRelayHopsThreshold = _FsMIDhcpRelayHopsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 5),
    _FsMIDhcpRelayHopsThreshold_Type()
)
fsMIDhcpRelayHopsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayHopsThreshold.setStatus("current")


class _FsMIDhcpRelayRAIOptionControl_Type(Integer32):
    """Custom type fsMIDhcpRelayRAIOptionControl based on Integer32"""
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


_FsMIDhcpRelayRAIOptionControl_Type.__name__ = "Integer32"
_FsMIDhcpRelayRAIOptionControl_Object = MibTableColumn
fsMIDhcpRelayRAIOptionControl = _FsMIDhcpRelayRAIOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 6),
    _FsMIDhcpRelayRAIOptionControl_Type()
)
fsMIDhcpRelayRAIOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAIOptionControl.setStatus("current")


class _FsMIDhcpRelayRAICircuitIDSubOptionControl_Type(Integer32):
    """Custom type fsMIDhcpRelayRAICircuitIDSubOptionControl based on Integer32"""
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


_FsMIDhcpRelayRAICircuitIDSubOptionControl_Type.__name__ = "Integer32"
_FsMIDhcpRelayRAICircuitIDSubOptionControl_Object = MibTableColumn
fsMIDhcpRelayRAICircuitIDSubOptionControl = _FsMIDhcpRelayRAICircuitIDSubOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 7),
    _FsMIDhcpRelayRAICircuitIDSubOptionControl_Type()
)
fsMIDhcpRelayRAICircuitIDSubOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAICircuitIDSubOptionControl.setStatus("current")


class _FsMIDhcpRelayRAIRemoteIDSubOptionControl_Type(Integer32):
    """Custom type fsMIDhcpRelayRAIRemoteIDSubOptionControl based on Integer32"""
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


_FsMIDhcpRelayRAIRemoteIDSubOptionControl_Type.__name__ = "Integer32"
_FsMIDhcpRelayRAIRemoteIDSubOptionControl_Object = MibTableColumn
fsMIDhcpRelayRAIRemoteIDSubOptionControl = _FsMIDhcpRelayRAIRemoteIDSubOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 8),
    _FsMIDhcpRelayRAIRemoteIDSubOptionControl_Type()
)
fsMIDhcpRelayRAIRemoteIDSubOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAIRemoteIDSubOptionControl.setStatus("current")


class _FsMIDhcpRelayRAISubnetMaskSubOptionControl_Type(Integer32):
    """Custom type fsMIDhcpRelayRAISubnetMaskSubOptionControl based on Integer32"""
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


_FsMIDhcpRelayRAISubnetMaskSubOptionControl_Type.__name__ = "Integer32"
_FsMIDhcpRelayRAISubnetMaskSubOptionControl_Object = MibTableColumn
fsMIDhcpRelayRAISubnetMaskSubOptionControl = _FsMIDhcpRelayRAISubnetMaskSubOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 9),
    _FsMIDhcpRelayRAISubnetMaskSubOptionControl_Type()
)
fsMIDhcpRelayRAISubnetMaskSubOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAISubnetMaskSubOptionControl.setStatus("current")
_FsMIDhcpRelayRAIOptionInserted_Type = Counter32
_FsMIDhcpRelayRAIOptionInserted_Object = MibTableColumn
fsMIDhcpRelayRAIOptionInserted = _FsMIDhcpRelayRAIOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 10),
    _FsMIDhcpRelayRAIOptionInserted_Type()
)
fsMIDhcpRelayRAIOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAIOptionInserted.setStatus("current")
_FsMIDhcpRelayRAICircuitIDSubOptionInserted_Type = Counter32
_FsMIDhcpRelayRAICircuitIDSubOptionInserted_Object = MibTableColumn
fsMIDhcpRelayRAICircuitIDSubOptionInserted = _FsMIDhcpRelayRAICircuitIDSubOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 11),
    _FsMIDhcpRelayRAICircuitIDSubOptionInserted_Type()
)
fsMIDhcpRelayRAICircuitIDSubOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAICircuitIDSubOptionInserted.setStatus("current")
_FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Type = Counter32
_FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Object = MibTableColumn
fsMIDhcpRelayRAIRemoteIDSubOptionInserted = _FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 12),
    _FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Type()
)
fsMIDhcpRelayRAIRemoteIDSubOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAIRemoteIDSubOptionInserted.setStatus("current")
_FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Type = Counter32
_FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Object = MibTableColumn
fsMIDhcpRelayRAISubnetMaskSubOptionInserted = _FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 13),
    _FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Type()
)
fsMIDhcpRelayRAISubnetMaskSubOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAISubnetMaskSubOptionInserted.setStatus("current")
_FsMIDhcpRelayRAIOptionWronglySet_Type = Counter32
_FsMIDhcpRelayRAIOptionWronglySet_Object = MibTableColumn
fsMIDhcpRelayRAIOptionWronglySet = _FsMIDhcpRelayRAIOptionWronglySet_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 14),
    _FsMIDhcpRelayRAIOptionWronglySet_Type()
)
fsMIDhcpRelayRAIOptionWronglySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAIOptionWronglySet.setStatus("current")
_FsMIDhcpRelayRAISpaceConstraint_Type = Counter32
_FsMIDhcpRelayRAISpaceConstraint_Object = MibTableColumn
fsMIDhcpRelayRAISpaceConstraint = _FsMIDhcpRelayRAISpaceConstraint_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 15),
    _FsMIDhcpRelayRAISpaceConstraint_Type()
)
fsMIDhcpRelayRAISpaceConstraint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDhcpRelayRAISpaceConstraint.setStatus("current")


class _FsMIDhcpConfigTraceLevel_Type(Integer32):
    """Custom type fsMIDhcpConfigTraceLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIDhcpConfigTraceLevel_Type.__name__ = "Integer32"
_FsMIDhcpConfigTraceLevel_Object = MibTableColumn
fsMIDhcpConfigTraceLevel = _FsMIDhcpConfigTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 16),
    _FsMIDhcpConfigTraceLevel_Type()
)
fsMIDhcpConfigTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpConfigTraceLevel.setStatus("current")


class _FsMIDhcpConfigDhcpCircuitOption_Type(Bits):
    """Custom type fsMIDhcpConfigDhcpCircuitOption based on Bits"""
    defaultHexValue = "01"

    namedValues = NamedValues(
        *(("routerindex", 0),
          ("vlanid", 1),
          ("recvport", 2))
    )

_FsMIDhcpConfigDhcpCircuitOption_Type.__name__ = "Bits"
_FsMIDhcpConfigDhcpCircuitOption_Object = MibTableColumn
fsMIDhcpConfigDhcpCircuitOption = _FsMIDhcpConfigDhcpCircuitOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 17),
    _FsMIDhcpConfigDhcpCircuitOption_Type()
)
fsMIDhcpConfigDhcpCircuitOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpConfigDhcpCircuitOption.setStatus("current")


class _FsMIDhcpRelayCounterReset_Type(Integer32):
    """Custom type fsMIDhcpRelayCounterReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notset", 2))
    )


_FsMIDhcpRelayCounterReset_Type.__name__ = "Integer32"
_FsMIDhcpRelayCounterReset_Object = MibTableColumn
fsMIDhcpRelayCounterReset = _FsMIDhcpRelayCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 18),
    _FsMIDhcpRelayCounterReset_Type()
)
fsMIDhcpRelayCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayCounterReset.setStatus("current")
_FsMIDhcpRelayContextRowStatus_Type = RowStatus
_FsMIDhcpRelayContextRowStatus_Object = MibTableColumn
fsMIDhcpRelayContextRowStatus = _FsMIDhcpRelayContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 1, 1, 19),
    _FsMIDhcpRelayContextRowStatus_Type()
)
fsMIDhcpRelayContextRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayContextRowStatus.setStatus("current")
_FsMIDhcpRelaySrvAddressTable_Object = MibTable
fsMIDhcpRelaySrvAddressTable = _FsMIDhcpRelaySrvAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 2)
)
if mibBuilder.loadTexts:
    fsMIDhcpRelaySrvAddressTable.setStatus("current")
_FsMIDhcpRelaySrvAddressEntry_Object = MibTableRow
fsMIDhcpRelaySrvAddressEntry = _FsMIDhcpRelaySrvAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 2, 1)
)
fsMIDhcpRelaySrvAddressEntry.setIndexNames(
    (0, "ARICENT-DHCP-RLY-MI-MIB", "fsMIDhcpContextId"),
    (0, "ARICENT-DHCP-RLY-MI-MIB", "fsMIDhcpRelaySrvIpAddress"),
)
if mibBuilder.loadTexts:
    fsMIDhcpRelaySrvAddressEntry.setStatus("current")
_FsMIDhcpRelaySrvIpAddress_Type = IpAddress
_FsMIDhcpRelaySrvIpAddress_Object = MibTableColumn
fsMIDhcpRelaySrvIpAddress = _FsMIDhcpRelaySrvIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 2, 1, 1),
    _FsMIDhcpRelaySrvIpAddress_Type()
)
fsMIDhcpRelaySrvIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDhcpRelaySrvIpAddress.setStatus("current")
_FsMIDhcpRelaySrvAddressRowStatus_Type = RowStatus
_FsMIDhcpRelaySrvAddressRowStatus_Object = MibTableColumn
fsMIDhcpRelaySrvAddressRowStatus = _FsMIDhcpRelaySrvAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 2, 1, 2),
    _FsMIDhcpRelaySrvAddressRowStatus_Type()
)
fsMIDhcpRelaySrvAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelaySrvAddressRowStatus.setStatus("current")
_FsMIDhcpRelayIfTable_Object = MibTable
fsMIDhcpRelayIfTable = _FsMIDhcpRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIDhcpRelayIfTable.setStatus("current")
_FsMIDhcpRelayIfEntry_Object = MibTableRow
fsMIDhcpRelayIfEntry = _FsMIDhcpRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 3, 1)
)
fsMIDhcpRelayIfEntry.setIndexNames(
    (0, "ARICENT-DHCP-RLY-MI-MIB", "fsMIDhcpContextId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsMIDhcpRelayIfEntry.setStatus("current")
_FsMIDhcpRelayIfCircuitId_Type = Unsigned32
_FsMIDhcpRelayIfCircuitId_Object = MibTableColumn
fsMIDhcpRelayIfCircuitId = _FsMIDhcpRelayIfCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 3, 1, 1),
    _FsMIDhcpRelayIfCircuitId_Type()
)
fsMIDhcpRelayIfCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayIfCircuitId.setStatus("current")
_FsMIDhcpRelayIfRemoteId_Type = DisplayString
_FsMIDhcpRelayIfRemoteId_Object = MibTableColumn
fsMIDhcpRelayIfRemoteId = _FsMIDhcpRelayIfRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 3, 1, 2),
    _FsMIDhcpRelayIfRemoteId_Type()
)
fsMIDhcpRelayIfRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayIfRemoteId.setStatus("current")
_FsMIDhcpRelayIfRowStatus_Type = RowStatus
_FsMIDhcpRelayIfRowStatus_Object = MibTableColumn
fsMIDhcpRelayIfRowStatus = _FsMIDhcpRelayIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 92, 2, 3, 1, 3),
    _FsMIDhcpRelayIfRowStatus_Type()
)
fsMIDhcpRelayIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDhcpRelayIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-DHCP-RLY-MI-MIB",
    **{"futureMIDhcpRelay": futureMIDhcpRelay,
       "fsMIDhcpRelay": fsMIDhcpRelay,
       "fsMIDhcpConfigGblTraceLevel": fsMIDhcpConfigGblTraceLevel,
       "fsMIDhcpRelayTable": fsMIDhcpRelayTable,
       "fsMIDhcpContextTable": fsMIDhcpContextTable,
       "fsMIDhcpContextEntry": fsMIDhcpContextEntry,
       "fsMIDhcpContextId": fsMIDhcpContextId,
       "fsMIDhcpRelaying": fsMIDhcpRelaying,
       "fsMIDhcpRelayServersOnly": fsMIDhcpRelayServersOnly,
       "fsMIDhcpRelaySecsThreshold": fsMIDhcpRelaySecsThreshold,
       "fsMIDhcpRelayHopsThreshold": fsMIDhcpRelayHopsThreshold,
       "fsMIDhcpRelayRAIOptionControl": fsMIDhcpRelayRAIOptionControl,
       "fsMIDhcpRelayRAICircuitIDSubOptionControl": fsMIDhcpRelayRAICircuitIDSubOptionControl,
       "fsMIDhcpRelayRAIRemoteIDSubOptionControl": fsMIDhcpRelayRAIRemoteIDSubOptionControl,
       "fsMIDhcpRelayRAISubnetMaskSubOptionControl": fsMIDhcpRelayRAISubnetMaskSubOptionControl,
       "fsMIDhcpRelayRAIOptionInserted": fsMIDhcpRelayRAIOptionInserted,
       "fsMIDhcpRelayRAICircuitIDSubOptionInserted": fsMIDhcpRelayRAICircuitIDSubOptionInserted,
       "fsMIDhcpRelayRAIRemoteIDSubOptionInserted": fsMIDhcpRelayRAIRemoteIDSubOptionInserted,
       "fsMIDhcpRelayRAISubnetMaskSubOptionInserted": fsMIDhcpRelayRAISubnetMaskSubOptionInserted,
       "fsMIDhcpRelayRAIOptionWronglySet": fsMIDhcpRelayRAIOptionWronglySet,
       "fsMIDhcpRelayRAISpaceConstraint": fsMIDhcpRelayRAISpaceConstraint,
       "fsMIDhcpConfigTraceLevel": fsMIDhcpConfigTraceLevel,
       "fsMIDhcpConfigDhcpCircuitOption": fsMIDhcpConfigDhcpCircuitOption,
       "fsMIDhcpRelayCounterReset": fsMIDhcpRelayCounterReset,
       "fsMIDhcpRelayContextRowStatus": fsMIDhcpRelayContextRowStatus,
       "fsMIDhcpRelaySrvAddressTable": fsMIDhcpRelaySrvAddressTable,
       "fsMIDhcpRelaySrvAddressEntry": fsMIDhcpRelaySrvAddressEntry,
       "fsMIDhcpRelaySrvIpAddress": fsMIDhcpRelaySrvIpAddress,
       "fsMIDhcpRelaySrvAddressRowStatus": fsMIDhcpRelaySrvAddressRowStatus,
       "fsMIDhcpRelayIfTable": fsMIDhcpRelayIfTable,
       "fsMIDhcpRelayIfEntry": fsMIDhcpRelayIfEntry,
       "fsMIDhcpRelayIfCircuitId": fsMIDhcpRelayIfCircuitId,
       "fsMIDhcpRelayIfRemoteId": fsMIDhcpRelayIfRemoteId,
       "fsMIDhcpRelayIfRowStatus": fsMIDhcpRelayIfRowStatus}
)
