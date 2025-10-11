# SNMP MIB module (WESTERMO-SW6-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-SW6-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:31 2025
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


# MODULE-IDENTITY

firewall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1)
)
if mibBuilder.loadTexts:
    firewall.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1)
)


class _CfgFwEnabled_Type(Integer32):
    """Custom type cfgFwEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgFwEnabled_Type.__name__ = "Integer32"
_CfgFwEnabled_Object = MibScalar
cfgFwEnabled = _CfgFwEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 1),
    _CfgFwEnabled_Type()
)
cfgFwEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwEnabled.setStatus("current")
_CfgFwNat_ObjectIdentity = ObjectIdentity
cfgFwNat = _CfgFwNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2)
)
_CfgFwNatPortForwardTable_Object = MibTable
cfgFwNatPortForwardTable = _CfgFwNatPortForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfgFwNatPortForwardTable.setStatus("current")
_CfgFwNatPortForwardTableEntry_Object = MibTableRow
cfgFwNatPortForwardTableEntry = _CfgFwNatPortForwardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1)
)
cfgFwNatPortForwardTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdIndex"),
)
if mibBuilder.loadTexts:
    cfgFwNatPortForwardTableEntry.setStatus("current")


class _CfgFwNatPrtFwdIndex_Type(Integer32):
    """Custom type cfgFwNatPrtFwdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgFwNatPrtFwdIndex_Type.__name__ = "Integer32"
_CfgFwNatPrtFwdIndex_Object = MibTableColumn
cfgFwNatPrtFwdIndex = _CfgFwNatPrtFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 1),
    _CfgFwNatPrtFwdIndex_Type()
)
cfgFwNatPrtFwdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdIndex.setStatus("current")


class _CfgFwNatPrtFwdEnabled_Type(Integer32):
    """Custom type cfgFwNatPrtFwdEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgFwNatPrtFwdEnabled_Type.__name__ = "Integer32"
_CfgFwNatPrtFwdEnabled_Object = MibTableColumn
cfgFwNatPrtFwdEnabled = _CfgFwNatPrtFwdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 2),
    _CfgFwNatPrtFwdEnabled_Type()
)
cfgFwNatPrtFwdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdEnabled.setStatus("current")


class _CfgFwNatPrtFwdInterface_Type(DisplayString):
    """Custom type cfgFwNatPrtFwdInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgFwNatPrtFwdInterface_Type.__name__ = "DisplayString"
_CfgFwNatPrtFwdInterface_Object = MibTableColumn
cfgFwNatPrtFwdInterface = _CfgFwNatPrtFwdInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 3),
    _CfgFwNatPrtFwdInterface_Type()
)
cfgFwNatPrtFwdInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdInterface.setStatus("current")


class _CfgFwNatPrtFwdProtocol_Type(Integer32):
    """Custom type cfgFwNatPrtFwdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("udp", 1),
          ("tcp", 2),
          ("udptcp", 3))
    )


_CfgFwNatPrtFwdProtocol_Type.__name__ = "Integer32"
_CfgFwNatPrtFwdProtocol_Object = MibTableColumn
cfgFwNatPrtFwdProtocol = _CfgFwNatPrtFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 4),
    _CfgFwNatPrtFwdProtocol_Type()
)
cfgFwNatPrtFwdProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdProtocol.setStatus("current")


class _CfgFwNatPrtFwdSourceAddress_Type(DisplayString):
    """Custom type cfgFwNatPrtFwdSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgFwNatPrtFwdSourceAddress_Type.__name__ = "DisplayString"
_CfgFwNatPrtFwdSourceAddress_Object = MibTableColumn
cfgFwNatPrtFwdSourceAddress = _CfgFwNatPrtFwdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 5),
    _CfgFwNatPrtFwdSourceAddress_Type()
)
cfgFwNatPrtFwdSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdSourceAddress.setStatus("current")


class _CfgFwNatPrtFwdSourcePortStart_Type(DisplayString):
    """Custom type cfgFwNatPrtFwdSourcePortStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CfgFwNatPrtFwdSourcePortStart_Type.__name__ = "DisplayString"
_CfgFwNatPrtFwdSourcePortStart_Object = MibTableColumn
cfgFwNatPrtFwdSourcePortStart = _CfgFwNatPrtFwdSourcePortStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 6),
    _CfgFwNatPrtFwdSourcePortStart_Type()
)
cfgFwNatPrtFwdSourcePortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdSourcePortStart.setStatus("current")


class _CfgFwNatPrtFwdSourcePortEnd_Type(Integer32):
    """Custom type cfgFwNatPrtFwdSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwNatPrtFwdSourcePortEnd_Type.__name__ = "Integer32"
_CfgFwNatPrtFwdSourcePortEnd_Object = MibTableColumn
cfgFwNatPrtFwdSourcePortEnd = _CfgFwNatPrtFwdSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 7),
    _CfgFwNatPrtFwdSourcePortEnd_Type()
)
cfgFwNatPrtFwdSourcePortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdSourcePortEnd.setStatus("current")


class _CfgFwNatPrtFwdDestinationAddress_Type(DisplayString):
    """Custom type cfgFwNatPrtFwdDestinationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgFwNatPrtFwdDestinationAddress_Type.__name__ = "DisplayString"
_CfgFwNatPrtFwdDestinationAddress_Object = MibTableColumn
cfgFwNatPrtFwdDestinationAddress = _CfgFwNatPrtFwdDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 8),
    _CfgFwNatPrtFwdDestinationAddress_Type()
)
cfgFwNatPrtFwdDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdDestinationAddress.setStatus("current")


class _CfgFwNatPrtFwdDestinationPortStart_Type(DisplayString):
    """Custom type cfgFwNatPrtFwdDestinationPortStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CfgFwNatPrtFwdDestinationPortStart_Type.__name__ = "DisplayString"
_CfgFwNatPrtFwdDestinationPortStart_Object = MibTableColumn
cfgFwNatPrtFwdDestinationPortStart = _CfgFwNatPrtFwdDestinationPortStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 9),
    _CfgFwNatPrtFwdDestinationPortStart_Type()
)
cfgFwNatPrtFwdDestinationPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdDestinationPortStart.setStatus("current")


class _CfgFwNatPrtFwdDestinationPortEnd_Type(Integer32):
    """Custom type cfgFwNatPrtFwdDestinationPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwNatPrtFwdDestinationPortEnd_Type.__name__ = "Integer32"
_CfgFwNatPrtFwdDestinationPortEnd_Object = MibTableColumn
cfgFwNatPrtFwdDestinationPortEnd = _CfgFwNatPrtFwdDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 10),
    _CfgFwNatPrtFwdDestinationPortEnd_Type()
)
cfgFwNatPrtFwdDestinationPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdDestinationPortEnd.setStatus("current")
_CfgFwNatPrtFwdRedirectDestinationAddress_Type = IpAddress
_CfgFwNatPrtFwdRedirectDestinationAddress_Object = MibTableColumn
cfgFwNatPrtFwdRedirectDestinationAddress = _CfgFwNatPrtFwdRedirectDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 11),
    _CfgFwNatPrtFwdRedirectDestinationAddress_Type()
)
cfgFwNatPrtFwdRedirectDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdRedirectDestinationAddress.setStatus("current")


class _CfgFwNatPrtFwdRedirectDestinationPort_Type(Integer32):
    """Custom type cfgFwNatPrtFwdRedirectDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwNatPrtFwdRedirectDestinationPort_Type.__name__ = "Integer32"
_CfgFwNatPrtFwdRedirectDestinationPort_Object = MibTableColumn
cfgFwNatPrtFwdRedirectDestinationPort = _CfgFwNatPrtFwdRedirectDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 1, 1, 12),
    _CfgFwNatPrtFwdRedirectDestinationPort_Type()
)
cfgFwNatPrtFwdRedirectDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatPrtFwdRedirectDestinationPort.setStatus("current")
_CfgFwNatOutboundTable_Object = MibTable
cfgFwNatOutboundTable = _CfgFwNatOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfgFwNatOutboundTable.setStatus("current")
_CfgFwNatOutboundTableEntry_Object = MibTableRow
cfgFwNatOutboundTableEntry = _CfgFwNatOutboundTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1)
)
cfgFwNatOutboundTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutIndex"),
)
if mibBuilder.loadTexts:
    cfgFwNatOutboundTableEntry.setStatus("current")


class _CfgFwNatOutIndex_Type(Integer32):
    """Custom type cfgFwNatOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgFwNatOutIndex_Type.__name__ = "Integer32"
_CfgFwNatOutIndex_Object = MibTableColumn
cfgFwNatOutIndex = _CfgFwNatOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 1),
    _CfgFwNatOutIndex_Type()
)
cfgFwNatOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFwNatOutIndex.setStatus("current")


class _CfgFwNatOutEnabled_Type(Integer32):
    """Custom type cfgFwNatOutEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgFwNatOutEnabled_Type.__name__ = "Integer32"
_CfgFwNatOutEnabled_Object = MibTableColumn
cfgFwNatOutEnabled = _CfgFwNatOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 2),
    _CfgFwNatOutEnabled_Type()
)
cfgFwNatOutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutEnabled.setStatus("current")


class _CfgFwNatOutInterface_Type(DisplayString):
    """Custom type cfgFwNatOutInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CfgFwNatOutInterface_Type.__name__ = "DisplayString"
_CfgFwNatOutInterface_Object = MibTableColumn
cfgFwNatOutInterface = _CfgFwNatOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 3),
    _CfgFwNatOutInterface_Type()
)
cfgFwNatOutInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutInterface.setStatus("current")


class _CfgFwNatOutProtocol_Type(Integer32):
    """Custom type cfgFwNatOutProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("udp", 1),
          ("tcp", 2),
          ("udptcp", 3))
    )


_CfgFwNatOutProtocol_Type.__name__ = "Integer32"
_CfgFwNatOutProtocol_Object = MibTableColumn
cfgFwNatOutProtocol = _CfgFwNatOutProtocol_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 4),
    _CfgFwNatOutProtocol_Type()
)
cfgFwNatOutProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutProtocol.setStatus("current")


class _CfgFwNatOutSourceAddress_Type(DisplayString):
    """Custom type cfgFwNatOutSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgFwNatOutSourceAddress_Type.__name__ = "DisplayString"
_CfgFwNatOutSourceAddress_Object = MibTableColumn
cfgFwNatOutSourceAddress = _CfgFwNatOutSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 5),
    _CfgFwNatOutSourceAddress_Type()
)
cfgFwNatOutSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutSourceAddress.setStatus("current")


class _CfgFwNatOutSourcePortStart_Type(DisplayString):
    """Custom type cfgFwNatOutSourcePortStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CfgFwNatOutSourcePortStart_Type.__name__ = "DisplayString"
_CfgFwNatOutSourcePortStart_Object = MibTableColumn
cfgFwNatOutSourcePortStart = _CfgFwNatOutSourcePortStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 6),
    _CfgFwNatOutSourcePortStart_Type()
)
cfgFwNatOutSourcePortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutSourcePortStart.setStatus("current")


class _CfgFwNatOutSourcePortEnd_Type(Integer32):
    """Custom type cfgFwNatOutSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwNatOutSourcePortEnd_Type.__name__ = "Integer32"
_CfgFwNatOutSourcePortEnd_Object = MibTableColumn
cfgFwNatOutSourcePortEnd = _CfgFwNatOutSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 7),
    _CfgFwNatOutSourcePortEnd_Type()
)
cfgFwNatOutSourcePortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutSourcePortEnd.setStatus("current")


class _CfgFwNatOutDestinationAddress_Type(DisplayString):
    """Custom type cfgFwNatOutDestinationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgFwNatOutDestinationAddress_Type.__name__ = "DisplayString"
_CfgFwNatOutDestinationAddress_Object = MibTableColumn
cfgFwNatOutDestinationAddress = _CfgFwNatOutDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 8),
    _CfgFwNatOutDestinationAddress_Type()
)
cfgFwNatOutDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutDestinationAddress.setStatus("current")


class _CfgFwNatOutDestinationPortStart_Type(DisplayString):
    """Custom type cfgFwNatOutDestinationPortStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_CfgFwNatOutDestinationPortStart_Type.__name__ = "DisplayString"
_CfgFwNatOutDestinationPortStart_Object = MibTableColumn
cfgFwNatOutDestinationPortStart = _CfgFwNatOutDestinationPortStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 9),
    _CfgFwNatOutDestinationPortStart_Type()
)
cfgFwNatOutDestinationPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutDestinationPortStart.setStatus("current")


class _CfgFwNatOutDestinationPortEnd_Type(Integer32):
    """Custom type cfgFwNatOutDestinationPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwNatOutDestinationPortEnd_Type.__name__ = "Integer32"
_CfgFwNatOutDestinationPortEnd_Object = MibTableColumn
cfgFwNatOutDestinationPortEnd = _CfgFwNatOutDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 10),
    _CfgFwNatOutDestinationPortEnd_Type()
)
cfgFwNatOutDestinationPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutDestinationPortEnd.setStatus("current")
_CfgFwNatOutSourceRewriteAddress_Type = IpAddress
_CfgFwNatOutSourceRewriteAddress_Object = MibTableColumn
cfgFwNatOutSourceRewriteAddress = _CfgFwNatOutSourceRewriteAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 11),
    _CfgFwNatOutSourceRewriteAddress_Type()
)
cfgFwNatOutSourceRewriteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutSourceRewriteAddress.setStatus("current")


class _CfgFwNatOutSourceRewritePort_Type(Integer32):
    """Custom type cfgFwNatOutSourceRewritePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwNatOutSourceRewritePort_Type.__name__ = "Integer32"
_CfgFwNatOutSourceRewritePort_Object = MibTableColumn
cfgFwNatOutSourceRewritePort = _CfgFwNatOutSourceRewritePort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 2, 2, 1, 12),
    _CfgFwNatOutSourceRewritePort_Type()
)
cfgFwNatOutSourceRewritePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwNatOutSourceRewritePort.setStatus("current")
_CfgFwL2IpFilter_ObjectIdentity = ObjectIdentity
cfgFwL2IpFilter = _CfgFwL2IpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3)
)


class _CfgFwL2IpFilterEnabled_Type(Integer32):
    """Custom type cfgFwL2IpFilterEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgFwL2IpFilterEnabled_Type.__name__ = "Integer32"
_CfgFwL2IpFilterEnabled_Object = MibScalar
cfgFwL2IpFilterEnabled = _CfgFwL2IpFilterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 1),
    _CfgFwL2IpFilterEnabled_Type()
)
cfgFwL2IpFilterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFilterEnabled.setStatus("current")


class _CfgFwL2IpFilterDefaultAction_Type(Integer32):
    """Custom type cfgFwL2IpFilterDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("drop", 1))
    )


_CfgFwL2IpFilterDefaultAction_Type.__name__ = "Integer32"
_CfgFwL2IpFilterDefaultAction_Object = MibScalar
cfgFwL2IpFilterDefaultAction = _CfgFwL2IpFilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 2),
    _CfgFwL2IpFilterDefaultAction_Type()
)
cfgFwL2IpFilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFilterDefaultAction.setStatus("current")
_CfgFwL2IpFilterTable_Object = MibTable
cfgFwL2IpFilterTable = _CfgFwL2IpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cfgFwL2IpFilterTable.setStatus("current")
_CfgFwL2IpFilterTableEntry_Object = MibTableRow
cfgFwL2IpFilterTableEntry = _CfgFwL2IpFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1)
)
cfgFwL2IpFilterTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrIndex"),
)
if mibBuilder.loadTexts:
    cfgFwL2IpFilterTableEntry.setStatus("current")


class _CfgFwL2IpFltrIndex_Type(Integer32):
    """Custom type cfgFwL2IpFltrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfgFwL2IpFltrIndex_Type.__name__ = "Integer32"
_CfgFwL2IpFltrIndex_Object = MibTableColumn
cfgFwL2IpFltrIndex = _CfgFwL2IpFltrIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 1),
    _CfgFwL2IpFltrIndex_Type()
)
cfgFwL2IpFltrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrIndex.setStatus("current")


class _CfgFwL2IpFltrEnabled_Type(Integer32):
    """Custom type cfgFwL2IpFltrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgFwL2IpFltrEnabled_Type.__name__ = "Integer32"
_CfgFwL2IpFltrEnabled_Object = MibTableColumn
cfgFwL2IpFltrEnabled = _CfgFwL2IpFltrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 2),
    _CfgFwL2IpFltrEnabled_Type()
)
cfgFwL2IpFltrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrEnabled.setStatus("current")


class _CfgFwL2IpFltrBridge_Type(Integer32):
    """Custom type cfgFwL2IpFltrBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_CfgFwL2IpFltrBridge_Type.__name__ = "Integer32"
_CfgFwL2IpFltrBridge_Object = MibTableColumn
cfgFwL2IpFltrBridge = _CfgFwL2IpFltrBridge_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 3),
    _CfgFwL2IpFltrBridge_Type()
)
cfgFwL2IpFltrBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrBridge.setStatus("current")


class _CfgFwL2IpFltrAction_Type(Integer32):
    """Custom type cfgFwL2IpFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("drop", 1))
    )


_CfgFwL2IpFltrAction_Type.__name__ = "Integer32"
_CfgFwL2IpFltrAction_Object = MibTableColumn
cfgFwL2IpFltrAction = _CfgFwL2IpFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 4),
    _CfgFwL2IpFltrAction_Type()
)
cfgFwL2IpFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrAction.setStatus("current")
_CfgFwL2IpFltrPriority_Type = Integer32
_CfgFwL2IpFltrPriority_Object = MibTableColumn
cfgFwL2IpFltrPriority = _CfgFwL2IpFltrPriority_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 5),
    _CfgFwL2IpFltrPriority_Type()
)
cfgFwL2IpFltrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrPriority.setStatus("current")


class _CfgFwL2IpFltrSource_Type(DisplayString):
    """Custom type cfgFwL2IpFltrSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgFwL2IpFltrSource_Type.__name__ = "DisplayString"
_CfgFwL2IpFltrSource_Object = MibTableColumn
cfgFwL2IpFltrSource = _CfgFwL2IpFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 6),
    _CfgFwL2IpFltrSource_Type()
)
cfgFwL2IpFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrSource.setStatus("current")


class _CfgFwL2IpFltrDestination_Type(DisplayString):
    """Custom type cfgFwL2IpFltrDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 19),
    )


_CfgFwL2IpFltrDestination_Type.__name__ = "DisplayString"
_CfgFwL2IpFltrDestination_Object = MibTableColumn
cfgFwL2IpFltrDestination = _CfgFwL2IpFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 3, 3, 1, 7),
    _CfgFwL2IpFltrDestination_Type()
)
cfgFwL2IpFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwL2IpFltrDestination.setStatus("current")
_CfgFwFilter_ObjectIdentity = ObjectIdentity
cfgFwFilter = _CfgFwFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4)
)


class _CfgFwFltDefaultPolicyInput_Type(Integer32):
    """Custom type cfgFwFltDefaultPolicyInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("accept", 1))
    )


_CfgFwFltDefaultPolicyInput_Type.__name__ = "Integer32"
_CfgFwFltDefaultPolicyInput_Object = MibScalar
cfgFwFltDefaultPolicyInput = _CfgFwFltDefaultPolicyInput_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 1),
    _CfgFwFltDefaultPolicyInput_Type()
)
cfgFwFltDefaultPolicyInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltDefaultPolicyInput.setStatus("current")


class _CfgFwFltDefaultPolicyForward_Type(Integer32):
    """Custom type cfgFwFltDefaultPolicyForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("accept", 1))
    )


_CfgFwFltDefaultPolicyForward_Type.__name__ = "Integer32"
_CfgFwFltDefaultPolicyForward_Object = MibScalar
cfgFwFltDefaultPolicyForward = _CfgFwFltDefaultPolicyForward_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 2),
    _CfgFwFltDefaultPolicyForward_Type()
)
cfgFwFltDefaultPolicyForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltDefaultPolicyForward.setStatus("current")


class _CfgFwFltDefaultPolicyOutput_Type(Integer32):
    """Custom type cfgFwFltDefaultPolicyOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("accept", 1))
    )


_CfgFwFltDefaultPolicyOutput_Type.__name__ = "Integer32"
_CfgFwFltDefaultPolicyOutput_Object = MibScalar
cfgFwFltDefaultPolicyOutput = _CfgFwFltDefaultPolicyOutput_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 3),
    _CfgFwFltDefaultPolicyOutput_Type()
)
cfgFwFltDefaultPolicyOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltDefaultPolicyOutput.setStatus("current")
_CfgFwFilterRulesTable_Object = MibTable
cfgFwFilterRulesTable = _CfgFwFilterRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    cfgFwFilterRulesTable.setStatus("current")
_CfgFwFilterRulesTableEntry_Object = MibTableRow
cfgFwFilterRulesTableEntry = _CfgFwFilterRulesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1)
)
cfgFwFilterRulesTableEntry.setIndexNames(
    (0, "WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutIndex"),
)
if mibBuilder.loadTexts:
    cfgFwFilterRulesTableEntry.setStatus("current")


class _CfgFwFltRIndex_Type(Integer32):
    """Custom type cfgFwFltRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgFwFltRIndex_Type.__name__ = "Integer32"
_CfgFwFltRIndex_Object = MibTableColumn
cfgFwFltRIndex = _CfgFwFltRIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 1),
    _CfgFwFltRIndex_Type()
)
cfgFwFltRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgFwFltRIndex.setStatus("current")


class _CfgFwFltREnabled_Type(Integer32):
    """Custom type cfgFwFltREnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CfgFwFltREnabled_Type.__name__ = "Integer32"
_CfgFwFltREnabled_Object = MibTableColumn
cfgFwFltREnabled = _CfgFwFltREnabled_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 2),
    _CfgFwFltREnabled_Type()
)
cfgFwFltREnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltREnabled.setStatus("current")


class _CfgFwFltRChain_Type(Integer32):
    """Custom type cfgFwFltRChain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("input", 1),
          ("forward", 2),
          ("output", 3))
    )


_CfgFwFltRChain_Type.__name__ = "Integer32"
_CfgFwFltRChain_Object = MibTableColumn
cfgFwFltRChain = _CfgFwFltRChain_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 3),
    _CfgFwFltRChain_Type()
)
cfgFwFltRChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRChain.setStatus("current")


class _CfgFwFltRAction_Type(Integer32):
    """Custom type cfgFwFltRAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("accept", 1))
    )


_CfgFwFltRAction_Type.__name__ = "Integer32"
_CfgFwFltRAction_Object = MibTableColumn
cfgFwFltRAction = _CfgFwFltRAction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 4),
    _CfgFwFltRAction_Type()
)
cfgFwFltRAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRAction.setStatus("current")


class _CfgFwFltRInputInterface_Type(DisplayString):
    """Custom type cfgFwFltRInputInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CfgFwFltRInputInterface_Type.__name__ = "DisplayString"
_CfgFwFltRInputInterface_Object = MibTableColumn
cfgFwFltRInputInterface = _CfgFwFltRInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 5),
    _CfgFwFltRInputInterface_Type()
)
cfgFwFltRInputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRInputInterface.setStatus("current")


class _CfgFwFltROutputInterface_Type(DisplayString):
    """Custom type cfgFwFltROutputInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CfgFwFltROutputInterface_Type.__name__ = "DisplayString"
_CfgFwFltROutputInterface_Object = MibTableColumn
cfgFwFltROutputInterface = _CfgFwFltROutputInterface_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 6),
    _CfgFwFltROutputInterface_Type()
)
cfgFwFltROutputInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltROutputInterface.setStatus("current")


class _CfgFwFltRProtocol_Type(Integer32):
    """Custom type cfgFwFltRProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfgFwFltRProtocol_Type.__name__ = "Integer32"
_CfgFwFltRProtocol_Object = MibTableColumn
cfgFwFltRProtocol = _CfgFwFltRProtocol_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 7),
    _CfgFwFltRProtocol_Type()
)
cfgFwFltRProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRProtocol.setStatus("current")


class _CfgFwFltRSourceAddress_Type(DisplayString):
    """Custom type cfgFwFltRSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CfgFwFltRSourceAddress_Type.__name__ = "DisplayString"
_CfgFwFltRSourceAddress_Object = MibTableColumn
cfgFwFltRSourceAddress = _CfgFwFltRSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 8),
    _CfgFwFltRSourceAddress_Type()
)
cfgFwFltRSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRSourceAddress.setStatus("current")


class _CfgFwFltRSourcePortStart_Type(DisplayString):
    """Custom type cfgFwFltRSourcePortStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CfgFwFltRSourcePortStart_Type.__name__ = "DisplayString"
_CfgFwFltRSourcePortStart_Object = MibTableColumn
cfgFwFltRSourcePortStart = _CfgFwFltRSourcePortStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 9),
    _CfgFwFltRSourcePortStart_Type()
)
cfgFwFltRSourcePortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRSourcePortStart.setStatus("current")


class _CfgFwFltRSourcePortEnd_Type(Integer32):
    """Custom type cfgFwFltRSourcePortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwFltRSourcePortEnd_Type.__name__ = "Integer32"
_CfgFwFltRSourcePortEnd_Object = MibTableColumn
cfgFwFltRSourcePortEnd = _CfgFwFltRSourcePortEnd_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 10),
    _CfgFwFltRSourcePortEnd_Type()
)
cfgFwFltRSourcePortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRSourcePortEnd.setStatus("current")


class _CfgFwFltRDestinationAddress_Type(DisplayString):
    """Custom type cfgFwFltRDestinationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CfgFwFltRDestinationAddress_Type.__name__ = "DisplayString"
_CfgFwFltRDestinationAddress_Object = MibTableColumn
cfgFwFltRDestinationAddress = _CfgFwFltRDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 11),
    _CfgFwFltRDestinationAddress_Type()
)
cfgFwFltRDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRDestinationAddress.setStatus("current")


class _CfgFwFltRDestinationPortStart_Type(DisplayString):
    """Custom type cfgFwFltRDestinationPortStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CfgFwFltRDestinationPortStart_Type.__name__ = "DisplayString"
_CfgFwFltRDestinationPortStart_Object = MibTableColumn
cfgFwFltRDestinationPortStart = _CfgFwFltRDestinationPortStart_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 12),
    _CfgFwFltRDestinationPortStart_Type()
)
cfgFwFltRDestinationPortStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRDestinationPortStart.setStatus("current")


class _CfgFwFltRDestinationPortEnd_Type(Integer32):
    """Custom type cfgFwFltRDestinationPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CfgFwFltRDestinationPortEnd_Type.__name__ = "Integer32"
_CfgFwFltRDestinationPortEnd_Object = MibTableColumn
cfgFwFltRDestinationPortEnd = _CfgFwFltRDestinationPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 1, 4, 10, 1, 13),
    _CfgFwFltRDestinationPortEnd_Type()
)
cfgFwFltRDestinationPortEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgFwFltRDestinationPortEnd.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1)
)
_GroupConfiguration_ObjectIdentity = ObjectIdentity
groupConfiguration = _GroupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1, 1)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 2)
)

# Managed Objects groups

groupCfgFirewall = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1, 1, 1)
)
groupCfgFirewall.setObjects(
    ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwEnabled")
)
if mibBuilder.loadTexts:
    groupCfgFirewall.setStatus("current")

groupCfgFirewallPortForward = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1, 1, 2)
)
groupCfgFirewallPortForward.setObjects(
      *(("WESTERMO-SW6-FIREWALL-MIB", "cfgFwEnabled"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdEnabled"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdInterface"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdProtocol"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdSourceAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdSourcePortStart"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdSourcePortEnd"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdDestinationAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdDestinationPortStart"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdDestinationPortEnd"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdRedirectDestinationAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatPrtFwdRedirectDestinationPort"))
)
if mibBuilder.loadTexts:
    groupCfgFirewallPortForward.setStatus("current")

groupCfgFirewallOutboundNat = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1, 1, 3)
)
groupCfgFirewallOutboundNat.setObjects(
      *(("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutEnabled"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutInterface"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutProtocol"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutSourceAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutSourcePortStart"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutSourcePortEnd"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutDestinationAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutDestinationPortStart"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutDestinationPortEnd"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutSourceRewriteAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwNatOutSourceRewritePort"))
)
if mibBuilder.loadTexts:
    groupCfgFirewallOutboundNat.setStatus("current")

groupCfgFirewallL2IpFilter = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1, 1, 4)
)
groupCfgFirewallL2IpFilter.setObjects(
      *(("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFilterEnabled"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFilterDefaultAction"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrEnabled"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrBridge"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrAction"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrPriority"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrSource"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwL2IpFltrDestination"))
)
if mibBuilder.loadTexts:
    groupCfgFirewallL2IpFilter.setStatus("current")

groupCfgFirewallFilter = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 1, 1, 5)
)
groupCfgFirewallFilter.setObjects(
      *(("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltDefaultPolicyInput"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltDefaultPolicyForward"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltDefaultPolicyOutput"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltREnabled"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRChain"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRAction"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRInputInterface"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltROutputInterface"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRProtocol"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRSourceAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRSourcePortStart"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRSourcePortEnd"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRDestinationAddress"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRDestinationPortStart"),
        ("WESTERMO-SW6-FIREWALL-MIB", "cfgFwFltRDestinationPortEnd"))
)
if mibBuilder.loadTexts:
    groupCfgFirewallFilter.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 2, 1, 10000, 2, 1)
)
compliance.setObjects(
      *(("WESTERMO-SW6-FIREWALL-MIB", "groupCfgFirewall"),
        ("WESTERMO-SW6-FIREWALL-MIB", "groupCfgFirewallPortForward"),
        ("WESTERMO-SW6-FIREWALL-MIB", "groupCfgFirewallOutboundNat"),
        ("WESTERMO-SW6-FIREWALL-MIB", "groupCfgFirewallL2IpFilter"),
        ("WESTERMO-SW6-FIREWALL-MIB", "groupCfgFirewallFilter"))
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-SW6-FIREWALL-MIB",
    **{"firewall": firewall,
       "configuration": configuration,
       "cfgFwEnabled": cfgFwEnabled,
       "cfgFwNat": cfgFwNat,
       "cfgFwNatPortForwardTable": cfgFwNatPortForwardTable,
       "cfgFwNatPortForwardTableEntry": cfgFwNatPortForwardTableEntry,
       "cfgFwNatPrtFwdIndex": cfgFwNatPrtFwdIndex,
       "cfgFwNatPrtFwdEnabled": cfgFwNatPrtFwdEnabled,
       "cfgFwNatPrtFwdInterface": cfgFwNatPrtFwdInterface,
       "cfgFwNatPrtFwdProtocol": cfgFwNatPrtFwdProtocol,
       "cfgFwNatPrtFwdSourceAddress": cfgFwNatPrtFwdSourceAddress,
       "cfgFwNatPrtFwdSourcePortStart": cfgFwNatPrtFwdSourcePortStart,
       "cfgFwNatPrtFwdSourcePortEnd": cfgFwNatPrtFwdSourcePortEnd,
       "cfgFwNatPrtFwdDestinationAddress": cfgFwNatPrtFwdDestinationAddress,
       "cfgFwNatPrtFwdDestinationPortStart": cfgFwNatPrtFwdDestinationPortStart,
       "cfgFwNatPrtFwdDestinationPortEnd": cfgFwNatPrtFwdDestinationPortEnd,
       "cfgFwNatPrtFwdRedirectDestinationAddress": cfgFwNatPrtFwdRedirectDestinationAddress,
       "cfgFwNatPrtFwdRedirectDestinationPort": cfgFwNatPrtFwdRedirectDestinationPort,
       "cfgFwNatOutboundTable": cfgFwNatOutboundTable,
       "cfgFwNatOutboundTableEntry": cfgFwNatOutboundTableEntry,
       "cfgFwNatOutIndex": cfgFwNatOutIndex,
       "cfgFwNatOutEnabled": cfgFwNatOutEnabled,
       "cfgFwNatOutInterface": cfgFwNatOutInterface,
       "cfgFwNatOutProtocol": cfgFwNatOutProtocol,
       "cfgFwNatOutSourceAddress": cfgFwNatOutSourceAddress,
       "cfgFwNatOutSourcePortStart": cfgFwNatOutSourcePortStart,
       "cfgFwNatOutSourcePortEnd": cfgFwNatOutSourcePortEnd,
       "cfgFwNatOutDestinationAddress": cfgFwNatOutDestinationAddress,
       "cfgFwNatOutDestinationPortStart": cfgFwNatOutDestinationPortStart,
       "cfgFwNatOutDestinationPortEnd": cfgFwNatOutDestinationPortEnd,
       "cfgFwNatOutSourceRewriteAddress": cfgFwNatOutSourceRewriteAddress,
       "cfgFwNatOutSourceRewritePort": cfgFwNatOutSourceRewritePort,
       "cfgFwL2IpFilter": cfgFwL2IpFilter,
       "cfgFwL2IpFilterEnabled": cfgFwL2IpFilterEnabled,
       "cfgFwL2IpFilterDefaultAction": cfgFwL2IpFilterDefaultAction,
       "cfgFwL2IpFilterTable": cfgFwL2IpFilterTable,
       "cfgFwL2IpFilterTableEntry": cfgFwL2IpFilterTableEntry,
       "cfgFwL2IpFltrIndex": cfgFwL2IpFltrIndex,
       "cfgFwL2IpFltrEnabled": cfgFwL2IpFltrEnabled,
       "cfgFwL2IpFltrBridge": cfgFwL2IpFltrBridge,
       "cfgFwL2IpFltrAction": cfgFwL2IpFltrAction,
       "cfgFwL2IpFltrPriority": cfgFwL2IpFltrPriority,
       "cfgFwL2IpFltrSource": cfgFwL2IpFltrSource,
       "cfgFwL2IpFltrDestination": cfgFwL2IpFltrDestination,
       "cfgFwFilter": cfgFwFilter,
       "cfgFwFltDefaultPolicyInput": cfgFwFltDefaultPolicyInput,
       "cfgFwFltDefaultPolicyForward": cfgFwFltDefaultPolicyForward,
       "cfgFwFltDefaultPolicyOutput": cfgFwFltDefaultPolicyOutput,
       "cfgFwFilterRulesTable": cfgFwFilterRulesTable,
       "cfgFwFilterRulesTableEntry": cfgFwFilterRulesTableEntry,
       "cfgFwFltRIndex": cfgFwFltRIndex,
       "cfgFwFltREnabled": cfgFwFltREnabled,
       "cfgFwFltRChain": cfgFwFltRChain,
       "cfgFwFltRAction": cfgFwFltRAction,
       "cfgFwFltRInputInterface": cfgFwFltRInputInterface,
       "cfgFwFltROutputInterface": cfgFwFltROutputInterface,
       "cfgFwFltRProtocol": cfgFwFltRProtocol,
       "cfgFwFltRSourceAddress": cfgFwFltRSourceAddress,
       "cfgFwFltRSourcePortStart": cfgFwFltRSourcePortStart,
       "cfgFwFltRSourcePortEnd": cfgFwFltRSourcePortEnd,
       "cfgFwFltRDestinationAddress": cfgFwFltRDestinationAddress,
       "cfgFwFltRDestinationPortStart": cfgFwFltRDestinationPortStart,
       "cfgFwFltRDestinationPortEnd": cfgFwFltRDestinationPortEnd,
       "conformance": conformance,
       "groups": groups,
       "groupConfiguration": groupConfiguration,
       "groupCfgFirewall": groupCfgFirewall,
       "groupCfgFirewallPortForward": groupCfgFirewallPortForward,
       "groupCfgFirewallOutboundNat": groupCfgFirewallOutboundNat,
       "groupCfgFirewallL2IpFilter": groupCfgFirewallL2IpFilter,
       "groupCfgFirewallFilter": groupCfgFirewallFilter,
       "compliances": compliances,
       "compliance": compliance}
)
