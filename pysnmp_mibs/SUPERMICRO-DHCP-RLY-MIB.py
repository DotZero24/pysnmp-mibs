# SNMP MIB module (SUPERMICRO-DHCP-RLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DHCP-RLY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:55 2025
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

futureDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24)
)
if mibBuilder.loadTexts:
    futureDhcpRelay.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1)
)


class _DhcpRelaying_Type(Integer32):
    """Custom type dhcpRelaying based on Integer32"""
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


_DhcpRelaying_Type.__name__ = "Integer32"
_DhcpRelaying_Object = MibScalar
dhcpRelaying = _DhcpRelaying_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 1),
    _DhcpRelaying_Type()
)
dhcpRelaying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelaying.setStatus("current")


class _DhcpRelayServersOnly_Type(Integer32):
    """Custom type dhcpRelayServersOnly based on Integer32"""
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


_DhcpRelayServersOnly_Type.__name__ = "Integer32"
_DhcpRelayServersOnly_Object = MibScalar
dhcpRelayServersOnly = _DhcpRelayServersOnly_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 2),
    _DhcpRelayServersOnly_Type()
)
dhcpRelayServersOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServersOnly.setStatus("current")


class _DhcpRelaySecsThreshold_Type(Integer32):
    """Custom type dhcpRelaySecsThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpRelaySecsThreshold_Type.__name__ = "Integer32"
_DhcpRelaySecsThreshold_Object = MibScalar
dhcpRelaySecsThreshold = _DhcpRelaySecsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 3),
    _DhcpRelaySecsThreshold_Type()
)
dhcpRelaySecsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelaySecsThreshold.setStatus("current")


class _DhcpRelayHopsThreshold_Type(Integer32):
    """Custom type dhcpRelayHopsThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DhcpRelayHopsThreshold_Type.__name__ = "Integer32"
_DhcpRelayHopsThreshold_Object = MibScalar
dhcpRelayHopsThreshold = _DhcpRelayHopsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 4),
    _DhcpRelayHopsThreshold_Type()
)
dhcpRelayHopsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayHopsThreshold.setStatus("current")


class _DhcpRelayRAIOptionControl_Type(Integer32):
    """Custom type dhcpRelayRAIOptionControl based on Integer32"""
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


_DhcpRelayRAIOptionControl_Type.__name__ = "Integer32"
_DhcpRelayRAIOptionControl_Object = MibScalar
dhcpRelayRAIOptionControl = _DhcpRelayRAIOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 5),
    _DhcpRelayRAIOptionControl_Type()
)
dhcpRelayRAIOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRAIOptionControl.setStatus("current")


class _DhcpRelayRAICircuitIDSubOptionControl_Type(Integer32):
    """Custom type dhcpRelayRAICircuitIDSubOptionControl based on Integer32"""
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


_DhcpRelayRAICircuitIDSubOptionControl_Type.__name__ = "Integer32"
_DhcpRelayRAICircuitIDSubOptionControl_Object = MibScalar
dhcpRelayRAICircuitIDSubOptionControl = _DhcpRelayRAICircuitIDSubOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 6),
    _DhcpRelayRAICircuitIDSubOptionControl_Type()
)
dhcpRelayRAICircuitIDSubOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRAICircuitIDSubOptionControl.setStatus("current")


class _DhcpRelayRAIRemoteIDSubOptionControl_Type(Integer32):
    """Custom type dhcpRelayRAIRemoteIDSubOptionControl based on Integer32"""
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


_DhcpRelayRAIRemoteIDSubOptionControl_Type.__name__ = "Integer32"
_DhcpRelayRAIRemoteIDSubOptionControl_Object = MibScalar
dhcpRelayRAIRemoteIDSubOptionControl = _DhcpRelayRAIRemoteIDSubOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 7),
    _DhcpRelayRAIRemoteIDSubOptionControl_Type()
)
dhcpRelayRAIRemoteIDSubOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRAIRemoteIDSubOptionControl.setStatus("current")


class _DhcpRelayRAISubnetMaskSubOptionControl_Type(Integer32):
    """Custom type dhcpRelayRAISubnetMaskSubOptionControl based on Integer32"""
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


_DhcpRelayRAISubnetMaskSubOptionControl_Type.__name__ = "Integer32"
_DhcpRelayRAISubnetMaskSubOptionControl_Object = MibScalar
dhcpRelayRAISubnetMaskSubOptionControl = _DhcpRelayRAISubnetMaskSubOptionControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 8),
    _DhcpRelayRAISubnetMaskSubOptionControl_Type()
)
dhcpRelayRAISubnetMaskSubOptionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayRAISubnetMaskSubOptionControl.setStatus("current")
_DhcpRelayRAIOptionInserted_Type = Counter32
_DhcpRelayRAIOptionInserted_Object = MibScalar
dhcpRelayRAIOptionInserted = _DhcpRelayRAIOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 9),
    _DhcpRelayRAIOptionInserted_Type()
)
dhcpRelayRAIOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRAIOptionInserted.setStatus("current")
_DhcpRelayRAICircuitIDSubOptionInserted_Type = Counter32
_DhcpRelayRAICircuitIDSubOptionInserted_Object = MibScalar
dhcpRelayRAICircuitIDSubOptionInserted = _DhcpRelayRAICircuitIDSubOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 10),
    _DhcpRelayRAICircuitIDSubOptionInserted_Type()
)
dhcpRelayRAICircuitIDSubOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRAICircuitIDSubOptionInserted.setStatus("current")
_DhcpRelayRAIRemoteIDSubOptionInserted_Type = Counter32
_DhcpRelayRAIRemoteIDSubOptionInserted_Object = MibScalar
dhcpRelayRAIRemoteIDSubOptionInserted = _DhcpRelayRAIRemoteIDSubOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 11),
    _DhcpRelayRAIRemoteIDSubOptionInserted_Type()
)
dhcpRelayRAIRemoteIDSubOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRAIRemoteIDSubOptionInserted.setStatus("current")
_DhcpRelayRAISubnetMaskSubOptionInserted_Type = Counter32
_DhcpRelayRAISubnetMaskSubOptionInserted_Object = MibScalar
dhcpRelayRAISubnetMaskSubOptionInserted = _DhcpRelayRAISubnetMaskSubOptionInserted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 12),
    _DhcpRelayRAISubnetMaskSubOptionInserted_Type()
)
dhcpRelayRAISubnetMaskSubOptionInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRAISubnetMaskSubOptionInserted.setStatus("current")
_DhcpRelayRAIOptionWronglySet_Type = Counter32
_DhcpRelayRAIOptionWronglySet_Object = MibScalar
dhcpRelayRAIOptionWronglySet = _DhcpRelayRAIOptionWronglySet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 13),
    _DhcpRelayRAIOptionWronglySet_Type()
)
dhcpRelayRAIOptionWronglySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRAIOptionWronglySet.setStatus("current")
_DhcpRelayRAISpaceConstraint_Type = Counter32
_DhcpRelayRAISpaceConstraint_Object = MibScalar
dhcpRelayRAISpaceConstraint = _DhcpRelayRAISpaceConstraint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 14),
    _DhcpRelayRAISpaceConstraint_Type()
)
dhcpRelayRAISpaceConstraint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayRAISpaceConstraint.setStatus("current")


class _DhcpConfigTraceLevel_Type(Integer32):
    """Custom type dhcpConfigTraceLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpConfigTraceLevel_Type.__name__ = "Integer32"
_DhcpConfigTraceLevel_Object = MibScalar
dhcpConfigTraceLevel = _DhcpConfigTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 15),
    _DhcpConfigTraceLevel_Type()
)
dhcpConfigTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpConfigTraceLevel.setStatus("current")


class _DhcpConfigDhcpCircuitOption_Type(Bits):
    """Custom type dhcpConfigDhcpCircuitOption based on Bits"""
    defaultHexValue = "01"

    namedValues = NamedValues(
        *(("routerindex", 0),
          ("vlanid", 1),
          ("recvport", 2))
    )

_DhcpConfigDhcpCircuitOption_Type.__name__ = "Bits"
_DhcpConfigDhcpCircuitOption_Object = MibScalar
dhcpConfigDhcpCircuitOption = _DhcpConfigDhcpCircuitOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 16),
    _DhcpConfigDhcpCircuitOption_Type()
)
dhcpConfigDhcpCircuitOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpConfigDhcpCircuitOption.setStatus("current")


class _DhcpRelayCounterReset_Type(Integer32):
    """Custom type dhcpRelayCounterReset based on Integer32"""
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


_DhcpRelayCounterReset_Type.__name__ = "Integer32"
_DhcpRelayCounterReset_Object = MibScalar
dhcpRelayCounterReset = _DhcpRelayCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 1, 17),
    _DhcpRelayCounterReset_Type()
)
dhcpRelayCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayCounterReset.setStatus("current")
_DhcpRelayTable_ObjectIdentity = ObjectIdentity
dhcpRelayTable = _DhcpRelayTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2)
)
_DhcpRelaySrvAddressTable_Object = MibTable
dhcpRelaySrvAddressTable = _DhcpRelaySrvAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRelaySrvAddressTable.setStatus("current")
_DhcpRelaySrvAddressEntry_Object = MibTableRow
dhcpRelaySrvAddressEntry = _DhcpRelaySrvAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 1, 1)
)
dhcpRelaySrvAddressEntry.setIndexNames(
    (0, "SUPERMICRO-DHCP-RLY-MIB", "dhcpRelaySrvIpAddress"),
)
if mibBuilder.loadTexts:
    dhcpRelaySrvAddressEntry.setStatus("current")
_DhcpRelaySrvIpAddress_Type = IpAddress
_DhcpRelaySrvIpAddress_Object = MibTableColumn
dhcpRelaySrvIpAddress = _DhcpRelaySrvIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 1, 1, 1),
    _DhcpRelaySrvIpAddress_Type()
)
dhcpRelaySrvIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelaySrvIpAddress.setStatus("current")
_DhcpRelaySrvAddressRowStatus_Type = RowStatus
_DhcpRelaySrvAddressRowStatus_Object = MibTableColumn
dhcpRelaySrvAddressRowStatus = _DhcpRelaySrvAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 1, 1, 2),
    _DhcpRelaySrvAddressRowStatus_Type()
)
dhcpRelaySrvAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelaySrvAddressRowStatus.setStatus("current")
_DhcpRelayIfTable_Object = MibTable
dhcpRelayIfTable = _DhcpRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 2)
)
if mibBuilder.loadTexts:
    dhcpRelayIfTable.setStatus("current")
_DhcpRelayIfEntry_Object = MibTableRow
dhcpRelayIfEntry = _DhcpRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 2, 1)
)
dhcpRelayIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelayIfEntry.setStatus("current")
_DhcpRelayIfCircuitId_Type = Unsigned32
_DhcpRelayIfCircuitId_Object = MibTableColumn
dhcpRelayIfCircuitId = _DhcpRelayIfCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 2, 1, 1),
    _DhcpRelayIfCircuitId_Type()
)
dhcpRelayIfCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayIfCircuitId.setStatus("current")
_DhcpRelayIfRemoteId_Type = DisplayString
_DhcpRelayIfRemoteId_Object = MibTableColumn
dhcpRelayIfRemoteId = _DhcpRelayIfRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 2, 1, 2),
    _DhcpRelayIfRemoteId_Type()
)
dhcpRelayIfRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayIfRemoteId.setStatus("current")
_DhcpRelayIfRowStatus_Type = RowStatus
_DhcpRelayIfRowStatus_Object = MibTableColumn
dhcpRelayIfRowStatus = _DhcpRelayIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 24, 2, 2, 1, 3),
    _DhcpRelayIfRowStatus_Type()
)
dhcpRelayIfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DHCP-RLY-MIB",
    **{"futureDhcpRelay": futureDhcpRelay,
       "dhcpRelay": dhcpRelay,
       "dhcpRelaying": dhcpRelaying,
       "dhcpRelayServersOnly": dhcpRelayServersOnly,
       "dhcpRelaySecsThreshold": dhcpRelaySecsThreshold,
       "dhcpRelayHopsThreshold": dhcpRelayHopsThreshold,
       "dhcpRelayRAIOptionControl": dhcpRelayRAIOptionControl,
       "dhcpRelayRAICircuitIDSubOptionControl": dhcpRelayRAICircuitIDSubOptionControl,
       "dhcpRelayRAIRemoteIDSubOptionControl": dhcpRelayRAIRemoteIDSubOptionControl,
       "dhcpRelayRAISubnetMaskSubOptionControl": dhcpRelayRAISubnetMaskSubOptionControl,
       "dhcpRelayRAIOptionInserted": dhcpRelayRAIOptionInserted,
       "dhcpRelayRAICircuitIDSubOptionInserted": dhcpRelayRAICircuitIDSubOptionInserted,
       "dhcpRelayRAIRemoteIDSubOptionInserted": dhcpRelayRAIRemoteIDSubOptionInserted,
       "dhcpRelayRAISubnetMaskSubOptionInserted": dhcpRelayRAISubnetMaskSubOptionInserted,
       "dhcpRelayRAIOptionWronglySet": dhcpRelayRAIOptionWronglySet,
       "dhcpRelayRAISpaceConstraint": dhcpRelayRAISpaceConstraint,
       "dhcpConfigTraceLevel": dhcpConfigTraceLevel,
       "dhcpConfigDhcpCircuitOption": dhcpConfigDhcpCircuitOption,
       "dhcpRelayCounterReset": dhcpRelayCounterReset,
       "dhcpRelayTable": dhcpRelayTable,
       "dhcpRelaySrvAddressTable": dhcpRelaySrvAddressTable,
       "dhcpRelaySrvAddressEntry": dhcpRelaySrvAddressEntry,
       "dhcpRelaySrvIpAddress": dhcpRelaySrvIpAddress,
       "dhcpRelaySrvAddressRowStatus": dhcpRelaySrvAddressRowStatus,
       "dhcpRelayIfTable": dhcpRelayIfTable,
       "dhcpRelayIfEntry": dhcpRelayIfEntry,
       "dhcpRelayIfCircuitId": dhcpRelayIfCircuitId,
       "dhcpRelayIfRemoteId": dhcpRelayIfRemoteId,
       "dhcpRelayIfRowStatus": dhcpRelayIfRowStatus}
)
