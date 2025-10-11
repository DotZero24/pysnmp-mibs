# SNMP MIB module (DHCP-OPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/DHCP-OPTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:12 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcDhcpOption = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41)
)
if mibBuilder.loadTexts:
    rcDhcpOption.setRevisions(
        ("2008-11-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDhcpOptionMibObjects_ObjectIdentity = ObjectIdentity
rcDhcpOptionMibObjects = _RcDhcpOptionMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1)
)
_RcDhcpOption82PortGroup_ObjectIdentity = ObjectIdentity
rcDhcpOption82PortGroup = _RcDhcpOption82PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 1)
)
_RcDhcpOption82PortTable_Object = MibTable
rcDhcpOption82PortTable = _RcDhcpOption82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcDhcpOption82PortTable.setStatus("current")
_RcDhcpOption82PortEntry_Object = MibTableRow
rcDhcpOption82PortEntry = _RcDhcpOption82PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 1, 1, 1)
)
rcDhcpOption82PortEntry.setIndexNames(
    (0, "DHCP-OPTION-MIB", "rcDhcpOption82PortIndex"),
)
if mibBuilder.loadTexts:
    rcDhcpOption82PortEntry.setStatus("current")
_RcDhcpOption82PortIndex_Type = Integer32
_RcDhcpOption82PortIndex_Object = MibTableColumn
rcDhcpOption82PortIndex = _RcDhcpOption82PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 1, 1, 1, 1),
    _RcDhcpOption82PortIndex_Type()
)
rcDhcpOption82PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpOption82PortIndex.setStatus("current")


class _RcDhcpOption82CircuitID_Type(OctetString):
    """Custom type rcDhcpOption82CircuitID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RcDhcpOption82CircuitID_Type.__name__ = "OctetString"
_RcDhcpOption82CircuitID_Object = MibTableColumn
rcDhcpOption82CircuitID = _RcDhcpOption82CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 1, 1, 1, 2),
    _RcDhcpOption82CircuitID_Type()
)
rcDhcpOption82CircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpOption82CircuitID.setStatus("current")
_RcDhcpOption82ConfigGroup_ObjectIdentity = ObjectIdentity
rcDhcpOption82ConfigGroup = _RcDhcpOption82ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 2)
)


class _RcDhcpOption82AttachString_Type(OctetString):
    """Custom type rcDhcpOption82AttachString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RcDhcpOption82AttachString_Type.__name__ = "OctetString"
_RcDhcpOption82AttachString_Object = MibScalar
rcDhcpOption82AttachString = _RcDhcpOption82AttachString_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 2, 1),
    _RcDhcpOption82AttachString_Type()
)
rcDhcpOption82AttachString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpOption82AttachString.setStatus("current")


class _RcDhcpOption82RemoteIDMode_Type(Integer32):
    """Custom type rcDhcpOption82RemoteIDMode based on Integer32"""
    defaultValue = 1

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
        *(("switchmac", 1),
          ("clientmac", 2),
          ("switchmac-string", 3),
          ("clientmac-string", 4),
          ("hostname", 5),
          ("user-defined", 6))
    )


_RcDhcpOption82RemoteIDMode_Type.__name__ = "Integer32"
_RcDhcpOption82RemoteIDMode_Object = MibScalar
rcDhcpOption82RemoteIDMode = _RcDhcpOption82RemoteIDMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 2, 2),
    _RcDhcpOption82RemoteIDMode_Type()
)
rcDhcpOption82RemoteIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpOption82RemoteIDMode.setStatus("current")


class _RcDhcpOption82RemoteIDString_Type(OctetString):
    """Custom type rcDhcpOption82RemoteIDString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RcDhcpOption82RemoteIDString_Type.__name__ = "OctetString"
_RcDhcpOption82RemoteIDString_Object = MibScalar
rcDhcpOption82RemoteIDString = _RcDhcpOption82RemoteIDString_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 2, 3),
    _RcDhcpOption82RemoteIDString_Type()
)
rcDhcpOption82RemoteIDString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpOption82RemoteIDString.setStatus("current")
_RcDhcpOptionGlobalGroup_ObjectIdentity = ObjectIdentity
rcDhcpOptionGlobalGroup = _RcDhcpOptionGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3)
)
_RcDhcpOptionGlobalTable_Object = MibTable
rcDhcpOptionGlobalTable = _RcDhcpOptionGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rcDhcpOptionGlobalTable.setStatus("current")
_RcDhcpOptionGlobalEntry_Object = MibTableRow
rcDhcpOptionGlobalEntry = _RcDhcpOptionGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1, 1)
)
rcDhcpOptionGlobalEntry.setIndexNames(
    (0, "DHCP-OPTION-MIB", "rcDhcpOptionCode"),
)
if mibBuilder.loadTexts:
    rcDhcpOptionGlobalEntry.setStatus("current")
_RcDhcpOptionCode_Type = OctetString
_RcDhcpOptionCode_Object = MibTableColumn
rcDhcpOptionCode = _RcDhcpOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1, 1, 1),
    _RcDhcpOptionCode_Type()
)
rcDhcpOptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpOptionCode.setStatus("current")
_RcDhcpOptionContent_Type = OctetString
_RcDhcpOptionContent_Object = MibTableColumn
rcDhcpOptionContent = _RcDhcpOptionContent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1, 1, 2),
    _RcDhcpOptionContent_Type()
)
rcDhcpOptionContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionContent.setStatus("current")
_RcDhcpOptionLength_Type = OctetString
_RcDhcpOptionLength_Object = MibTableColumn
rcDhcpOptionLength = _RcDhcpOptionLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1, 1, 3),
    _RcDhcpOptionLength_Type()
)
rcDhcpOptionLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionLength.setStatus("current")


class _RcDhcpOptionType_Type(Integer32):
    """Custom type rcDhcpOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asciiString", 1),
          ("hexString", 2),
          ("ipAddress", 3))
    )


_RcDhcpOptionType_Type.__name__ = "Integer32"
_RcDhcpOptionType_Object = MibTableColumn
rcDhcpOptionType = _RcDhcpOptionType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1, 1, 4),
    _RcDhcpOptionType_Type()
)
rcDhcpOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionType.setStatus("current")
_RcDhcpOptionRowStatus_Type = RowStatus
_RcDhcpOptionRowStatus_Object = MibTableColumn
rcDhcpOptionRowStatus = _RcDhcpOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 1, 1, 5),
    _RcDhcpOptionRowStatus_Type()
)
rcDhcpOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionRowStatus.setStatus("current")
_RcDhcp6OptionGlobalTable_Object = MibTable
rcDhcp6OptionGlobalTable = _RcDhcp6OptionGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rcDhcp6OptionGlobalTable.setStatus("current")
_RcDhcp6OptionGlobalEntry_Object = MibTableRow
rcDhcp6OptionGlobalEntry = _RcDhcp6OptionGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2, 1)
)
rcDhcp6OptionGlobalEntry.setIndexNames(
    (0, "DHCP-OPTION-MIB", "rcDhcp6OptionCode"),
)
if mibBuilder.loadTexts:
    rcDhcp6OptionGlobalEntry.setStatus("current")
_RcDhcp6OptionCode_Type = OctetString
_RcDhcp6OptionCode_Object = MibTableColumn
rcDhcp6OptionCode = _RcDhcp6OptionCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2, 1, 1),
    _RcDhcp6OptionCode_Type()
)
rcDhcp6OptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcp6OptionCode.setStatus("current")
_RcDhcp6OptionContent_Type = OctetString
_RcDhcp6OptionContent_Object = MibTableColumn
rcDhcp6OptionContent = _RcDhcp6OptionContent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2, 1, 2),
    _RcDhcp6OptionContent_Type()
)
rcDhcp6OptionContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionContent.setStatus("current")
_RcDhcp6OptionLength_Type = OctetString
_RcDhcp6OptionLength_Object = MibTableColumn
rcDhcp6OptionLength = _RcDhcp6OptionLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2, 1, 3),
    _RcDhcp6OptionLength_Type()
)
rcDhcp6OptionLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionLength.setStatus("current")


class _RcDhcp6OptionType_Type(Integer32):
    """Custom type rcDhcp6OptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asciiString", 1),
          ("hexString", 2),
          ("ipAddress", 3))
    )


_RcDhcp6OptionType_Type.__name__ = "Integer32"
_RcDhcp6OptionType_Object = MibTableColumn
rcDhcp6OptionType = _RcDhcp6OptionType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2, 1, 4),
    _RcDhcp6OptionType_Type()
)
rcDhcp6OptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionType.setStatus("current")
_RcDhcp6OptionRowStatus_Type = RowStatus
_RcDhcp6OptionRowStatus_Object = MibTableColumn
rcDhcp6OptionRowStatus = _RcDhcp6OptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 3, 2, 1, 5),
    _RcDhcp6OptionRowStatus_Type()
)
rcDhcp6OptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionRowStatus.setStatus("current")
_RcDhcpOptionPortGroup_ObjectIdentity = ObjectIdentity
rcDhcpOptionPortGroup = _RcDhcpOptionPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4)
)
_RcDhcpOptionPortTable_Object = MibTable
rcDhcpOptionPortTable = _RcDhcpOptionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rcDhcpOptionPortTable.setStatus("current")
_RcDhcpOptionPortEntry_Object = MibTableRow
rcDhcpOptionPortEntry = _RcDhcpOptionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1)
)
rcDhcpOptionPortEntry.setIndexNames(
    (0, "DHCP-OPTION-MIB", "rcDhcpOptionPortIndex"),
    (0, "DHCP-OPTION-MIB", "rcDhcpOptionPortCode"),
)
if mibBuilder.loadTexts:
    rcDhcpOptionPortEntry.setStatus("current")
_RcDhcpOptionPortIndex_Type = Integer32
_RcDhcpOptionPortIndex_Object = MibTableColumn
rcDhcpOptionPortIndex = _RcDhcpOptionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1, 1),
    _RcDhcpOptionPortIndex_Type()
)
rcDhcpOptionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpOptionPortIndex.setStatus("current")
_RcDhcpOptionPortCode_Type = OctetString
_RcDhcpOptionPortCode_Object = MibTableColumn
rcDhcpOptionPortCode = _RcDhcpOptionPortCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1, 2),
    _RcDhcpOptionPortCode_Type()
)
rcDhcpOptionPortCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpOptionPortCode.setStatus("current")
_RcDhcpOptionPortContent_Type = OctetString
_RcDhcpOptionPortContent_Object = MibTableColumn
rcDhcpOptionPortContent = _RcDhcpOptionPortContent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1, 3),
    _RcDhcpOptionPortContent_Type()
)
rcDhcpOptionPortContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionPortContent.setStatus("current")
_RcDhcpOptionPortLength_Type = OctetString
_RcDhcpOptionPortLength_Object = MibTableColumn
rcDhcpOptionPortLength = _RcDhcpOptionPortLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1, 4),
    _RcDhcpOptionPortLength_Type()
)
rcDhcpOptionPortLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionPortLength.setStatus("current")


class _RcDhcpOptionPortType_Type(Integer32):
    """Custom type rcDhcpOptionPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asciiString", 1),
          ("hexString", 2),
          ("ipAddress", 3))
    )


_RcDhcpOptionPortType_Type.__name__ = "Integer32"
_RcDhcpOptionPortType_Object = MibTableColumn
rcDhcpOptionPortType = _RcDhcpOptionPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1, 5),
    _RcDhcpOptionPortType_Type()
)
rcDhcpOptionPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionPortType.setStatus("current")
_RcDhcpOptionPortRowStatus_Type = RowStatus
_RcDhcpOptionPortRowStatus_Object = MibTableColumn
rcDhcpOptionPortRowStatus = _RcDhcpOptionPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 1, 1, 6),
    _RcDhcpOptionPortRowStatus_Type()
)
rcDhcpOptionPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcpOptionPortRowStatus.setStatus("current")
_RcDhcp6OptionPortTable_Object = MibTable
rcDhcp6OptionPortTable = _RcDhcp6OptionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rcDhcp6OptionPortTable.setStatus("current")
_RcDhcp6OptionPortEntry_Object = MibTableRow
rcDhcp6OptionPortEntry = _RcDhcp6OptionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1)
)
rcDhcp6OptionPortEntry.setIndexNames(
    (0, "DHCP-OPTION-MIB", "rcDhcp6OptionPortIndex"),
    (0, "DHCP-OPTION-MIB", "rcDhcp6OptionPortCode"),
)
if mibBuilder.loadTexts:
    rcDhcp6OptionPortEntry.setStatus("current")
_RcDhcp6OptionPortIndex_Type = Integer32
_RcDhcp6OptionPortIndex_Object = MibTableColumn
rcDhcp6OptionPortIndex = _RcDhcp6OptionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1, 1),
    _RcDhcp6OptionPortIndex_Type()
)
rcDhcp6OptionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcp6OptionPortIndex.setStatus("current")
_RcDhcp6OptionPortCode_Type = OctetString
_RcDhcp6OptionPortCode_Object = MibTableColumn
rcDhcp6OptionPortCode = _RcDhcp6OptionPortCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1, 2),
    _RcDhcp6OptionPortCode_Type()
)
rcDhcp6OptionPortCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcp6OptionPortCode.setStatus("current")
_RcDhcp6OptionPortContent_Type = OctetString
_RcDhcp6OptionPortContent_Object = MibTableColumn
rcDhcp6OptionPortContent = _RcDhcp6OptionPortContent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1, 3),
    _RcDhcp6OptionPortContent_Type()
)
rcDhcp6OptionPortContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionPortContent.setStatus("current")
_RcDhcp6OptionPortLength_Type = OctetString
_RcDhcp6OptionPortLength_Object = MibTableColumn
rcDhcp6OptionPortLength = _RcDhcp6OptionPortLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1, 4),
    _RcDhcp6OptionPortLength_Type()
)
rcDhcp6OptionPortLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionPortLength.setStatus("current")


class _RcDhcp6OptionPortType_Type(Integer32):
    """Custom type rcDhcp6OptionPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asciiString", 1),
          ("hexString", 2),
          ("ipAddress", 3))
    )


_RcDhcp6OptionPortType_Type.__name__ = "Integer32"
_RcDhcp6OptionPortType_Object = MibTableColumn
rcDhcp6OptionPortType = _RcDhcp6OptionPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1, 5),
    _RcDhcp6OptionPortType_Type()
)
rcDhcp6OptionPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionPortType.setStatus("current")
_RcDhcp6OptionPortRowStatus_Type = RowStatus
_RcDhcp6OptionPortRowStatus_Object = MibTableColumn
rcDhcp6OptionPortRowStatus = _RcDhcp6OptionPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 41, 1, 4, 2, 1, 6),
    _RcDhcp6OptionPortRowStatus_Type()
)
rcDhcp6OptionPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcDhcp6OptionPortRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-OPTION-MIB",
    **{"rcDhcpOption": rcDhcpOption,
       "rcDhcpOptionMibObjects": rcDhcpOptionMibObjects,
       "rcDhcpOption82PortGroup": rcDhcpOption82PortGroup,
       "rcDhcpOption82PortTable": rcDhcpOption82PortTable,
       "rcDhcpOption82PortEntry": rcDhcpOption82PortEntry,
       "rcDhcpOption82PortIndex": rcDhcpOption82PortIndex,
       "rcDhcpOption82CircuitID": rcDhcpOption82CircuitID,
       "rcDhcpOption82ConfigGroup": rcDhcpOption82ConfigGroup,
       "rcDhcpOption82AttachString": rcDhcpOption82AttachString,
       "rcDhcpOption82RemoteIDMode": rcDhcpOption82RemoteIDMode,
       "rcDhcpOption82RemoteIDString": rcDhcpOption82RemoteIDString,
       "rcDhcpOptionGlobalGroup": rcDhcpOptionGlobalGroup,
       "rcDhcpOptionGlobalTable": rcDhcpOptionGlobalTable,
       "rcDhcpOptionGlobalEntry": rcDhcpOptionGlobalEntry,
       "rcDhcpOptionCode": rcDhcpOptionCode,
       "rcDhcpOptionContent": rcDhcpOptionContent,
       "rcDhcpOptionLength": rcDhcpOptionLength,
       "rcDhcpOptionType": rcDhcpOptionType,
       "rcDhcpOptionRowStatus": rcDhcpOptionRowStatus,
       "rcDhcp6OptionGlobalTable": rcDhcp6OptionGlobalTable,
       "rcDhcp6OptionGlobalEntry": rcDhcp6OptionGlobalEntry,
       "rcDhcp6OptionCode": rcDhcp6OptionCode,
       "rcDhcp6OptionContent": rcDhcp6OptionContent,
       "rcDhcp6OptionLength": rcDhcp6OptionLength,
       "rcDhcp6OptionType": rcDhcp6OptionType,
       "rcDhcp6OptionRowStatus": rcDhcp6OptionRowStatus,
       "rcDhcpOptionPortGroup": rcDhcpOptionPortGroup,
       "rcDhcpOptionPortTable": rcDhcpOptionPortTable,
       "rcDhcpOptionPortEntry": rcDhcpOptionPortEntry,
       "rcDhcpOptionPortIndex": rcDhcpOptionPortIndex,
       "rcDhcpOptionPortCode": rcDhcpOptionPortCode,
       "rcDhcpOptionPortContent": rcDhcpOptionPortContent,
       "rcDhcpOptionPortLength": rcDhcpOptionPortLength,
       "rcDhcpOptionPortType": rcDhcpOptionPortType,
       "rcDhcpOptionPortRowStatus": rcDhcpOptionPortRowStatus,
       "rcDhcp6OptionPortTable": rcDhcp6OptionPortTable,
       "rcDhcp6OptionPortEntry": rcDhcp6OptionPortEntry,
       "rcDhcp6OptionPortIndex": rcDhcp6OptionPortIndex,
       "rcDhcp6OptionPortCode": rcDhcp6OptionPortCode,
       "rcDhcp6OptionPortContent": rcDhcp6OptionPortContent,
       "rcDhcp6OptionPortLength": rcDhcp6OptionPortLength,
       "rcDhcp6OptionPortType": rcDhcp6OptionPortType,
       "rcDhcp6OptionPortRowStatus": rcDhcp6OptionPortRowStatus}
)
