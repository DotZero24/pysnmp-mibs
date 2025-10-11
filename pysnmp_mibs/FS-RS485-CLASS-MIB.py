# SNMP MIB module (FS-RS485-CLASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-RS485-CLASS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:18 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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


# MODULE-IDENTITY

fsRs485MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149)
)
if mibBuilder.loadTexts:
    fsRs485MIB.setRevisions(
        ("2007-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRs485MIBObjects_ObjectIdentity = ObjectIdentity
fsRs485MIBObjects = _FsRs485MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1)
)
_FsRs485IpAddress_Type = IpAddress
_FsRs485IpAddress_Object = MibScalar
fsRs485IpAddress = _FsRs485IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 1),
    _FsRs485IpAddress_Type()
)
fsRs485IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485IpAddress.setStatus("current")
_FsRs485IpAddressMask_Type = IpAddress
_FsRs485IpAddressMask_Object = MibScalar
fsRs485IpAddressMask = _FsRs485IpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 2),
    _FsRs485IpAddressMask_Type()
)
fsRs485IpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485IpAddressMask.setStatus("current")
_FsRs485Gateway_Type = IpAddress
_FsRs485Gateway_Object = MibScalar
fsRs485Gateway = _FsRs485Gateway_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 3),
    _FsRs485Gateway_Type()
)
fsRs485Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485Gateway.setStatus("current")
_FsRs485Mac_Type = PhysAddress
_FsRs485Mac_Object = MibScalar
fsRs485Mac = _FsRs485Mac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 4),
    _FsRs485Mac_Type()
)
fsRs485Mac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485Mac.setStatus("current")


class _FsRs485ServerMode_Type(Integer32):
    """Custom type fsRs485ServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("client", 0),
          ("server", 1))
    )


_FsRs485ServerMode_Type.__name__ = "Integer32"
_FsRs485ServerMode_Object = MibScalar
fsRs485ServerMode = _FsRs485ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 5),
    _FsRs485ServerMode_Type()
)
fsRs485ServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485ServerMode.setStatus("current")


class _FsRs485SerialNum_Type(Integer32):
    """Custom type fsRs485SerialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsRs485SerialNum_Type.__name__ = "Integer32"
_FsRs485SerialNum_Object = MibScalar
fsRs485SerialNum = _FsRs485SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 6),
    _FsRs485SerialNum_Type()
)
fsRs485SerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485SerialNum.setStatus("current")
_FsRs485TelnetIp_Type = IpAddress
_FsRs485TelnetIp_Object = MibScalar
fsRs485TelnetIp = _FsRs485TelnetIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 7),
    _FsRs485TelnetIp_Type()
)
fsRs485TelnetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485TelnetIp.setStatus("current")
_FsRs485State_Type = Integer32
_FsRs485State_Object = MibScalar
fsRs485State = _FsRs485State_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 8),
    _FsRs485State_Type()
)
fsRs485State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485State.setStatus("current")


class _FsRs485SerialPower1_Type(Integer32):
    """Custom type fsRs485SerialPower1 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_FsRs485SerialPower1_Type.__name__ = "Integer32"
_FsRs485SerialPower1_Object = MibScalar
fsRs485SerialPower1 = _FsRs485SerialPower1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 9),
    _FsRs485SerialPower1_Type()
)
fsRs485SerialPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485SerialPower1.setStatus("current")


class _FsRs485SerialPower2_Type(Integer32):
    """Custom type fsRs485SerialPower2 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_FsRs485SerialPower2_Type.__name__ = "Integer32"
_FsRs485SerialPower2_Object = MibScalar
fsRs485SerialPower2 = _FsRs485SerialPower2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 10),
    _FsRs485SerialPower2_Type()
)
fsRs485SerialPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485SerialPower2.setStatus("current")


class _FsRs485SerialPower3_Type(Integer32):
    """Custom type fsRs485SerialPower3 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_FsRs485SerialPower3_Type.__name__ = "Integer32"
_FsRs485SerialPower3_Object = MibScalar
fsRs485SerialPower3 = _FsRs485SerialPower3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 11),
    _FsRs485SerialPower3_Type()
)
fsRs485SerialPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485SerialPower3.setStatus("current")


class _FsRs485SerialPower4_Type(Integer32):
    """Custom type fsRs485SerialPower4 based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("short", 2),
          ("break", 3))
    )


_FsRs485SerialPower4_Type.__name__ = "Integer32"
_FsRs485SerialPower4_Object = MibScalar
fsRs485SerialPower4 = _FsRs485SerialPower4_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 12),
    _FsRs485SerialPower4_Type()
)
fsRs485SerialPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485SerialPower4.setStatus("current")
_FsRs485VlanTable_Object = MibTable
fsRs485VlanTable = _FsRs485VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13)
)
if mibBuilder.loadTexts:
    fsRs485VlanTable.setStatus("current")
_FsRs485VlanEntry_Object = MibTableRow
fsRs485VlanEntry = _FsRs485VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1)
)
fsRs485VlanEntry.setIndexNames(
    (0, "FS-RS485-CLASS-MIB", "fsRs485SerialPort"),
)
if mibBuilder.loadTexts:
    fsRs485VlanEntry.setStatus("current")
_FsRs485SerialPort_Type = Counter32
_FsRs485SerialPort_Object = MibTableColumn
fsRs485SerialPort = _FsRs485SerialPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 1),
    _FsRs485SerialPort_Type()
)
fsRs485SerialPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485SerialPort.setStatus("current")


class _FsRs485VLANID_Type(Integer32):
    """Custom type fsRs485VLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_FsRs485VLANID_Type.__name__ = "Integer32"
_FsRs485VLANID_Object = MibTableColumn
fsRs485VLANID = _FsRs485VLANID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 2),
    _FsRs485VLANID_Type()
)
fsRs485VLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485VLANID.setStatus("current")


class _FsRs485Baudrate_Type(Integer32):
    """Custom type fsRs485Baudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 999999),
    )


_FsRs485Baudrate_Type.__name__ = "Integer32"
_FsRs485Baudrate_Object = MibTableColumn
fsRs485Baudrate = _FsRs485Baudrate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 3),
    _FsRs485Baudrate_Type()
)
fsRs485Baudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485Baudrate.setStatus("current")


class _FsRs485Parity_Type(Integer32):
    """Custom type fsRs485Parity based on Integer32"""
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
        *(("none", 1),
          ("odd", 2),
          ("even", 3),
          ("mark", 4),
          ("space", 5))
    )


_FsRs485Parity_Type.__name__ = "Integer32"
_FsRs485Parity_Object = MibTableColumn
fsRs485Parity = _FsRs485Parity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 4),
    _FsRs485Parity_Type()
)
fsRs485Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485Parity.setStatus("current")


class _FsClassSerialType_Type(Integer32):
    """Custom type fsClassSerialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rs485", 0),
          ("rs232", 1))
    )


_FsClassSerialType_Type.__name__ = "Integer32"
_FsClassSerialType_Object = MibTableColumn
fsClassSerialType = _FsClassSerialType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 5),
    _FsClassSerialType_Type()
)
fsClassSerialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassSerialType.setStatus("current")


class _FsClassStatus_Type(Integer32):
    """Custom type fsClassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("unnormal", 1))
    )


_FsClassStatus_Type.__name__ = "Integer32"
_FsClassStatus_Object = MibTableColumn
fsClassStatus = _FsClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 6),
    _FsClassStatus_Type()
)
fsClassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassStatus.setStatus("current")


class _FsClassIsTeleControl_Type(Integer32):
    """Custom type fsClassIsTeleControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FsClassIsTeleControl_Type.__name__ = "Integer32"
_FsClassIsTeleControl_Object = MibTableColumn
fsClassIsTeleControl = _FsClassIsTeleControl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 13, 1, 7),
    _FsClassIsTeleControl_Type()
)
fsClassIsTeleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassIsTeleControl.setStatus("current")
_FsSSIfTable_Object = MibTable
fsSSIfTable = _FsSSIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14)
)
if mibBuilder.loadTexts:
    fsSSIfTable.setStatus("current")
_FsSSIfEntry_Object = MibTableRow
fsSSIfEntry = _FsSSIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1)
)
fsSSIfEntry.setIndexNames(
    (0, "FS-RS485-CLASS-MIB", "fsSSIfIndex"),
)
if mibBuilder.loadTexts:
    fsSSIfEntry.setStatus("current")
_FsSSIfIndex_Type = Counter32
_FsSSIfIndex_Object = MibTableColumn
fsSSIfIndex = _FsSSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 1),
    _FsSSIfIndex_Type()
)
fsSSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSSIfIndex.setStatus("current")


class _FsSSIfAccessVlan_Type(Integer32):
    """Custom type fsSSIfAccessVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSSIfAccessVlan_Type.__name__ = "Integer32"
_FsSSIfAccessVlan_Object = MibTableColumn
fsSSIfAccessVlan = _FsSSIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 2),
    _FsSSIfAccessVlan_Type()
)
fsSSIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSSIfAccessVlan.setStatus("current")


class _FsSSIfNativeVlan_Type(Integer32):
    """Custom type fsSSIfNativeVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsSSIfNativeVlan_Type.__name__ = "Integer32"
_FsSSIfNativeVlan_Object = MibTableColumn
fsSSIfNativeVlan = _FsSSIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 3),
    _FsSSIfNativeVlan_Type()
)
fsSSIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSSIfNativeVlan.setStatus("current")


class _FsSSIfTrunk_Type(Integer32):
    """Custom type fsSSIfTrunk based on Integer32"""
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


_FsSSIfTrunk_Type.__name__ = "Integer32"
_FsSSIfTrunk_Object = MibTableColumn
fsSSIfTrunk = _FsSSIfTrunk_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 4),
    _FsSSIfTrunk_Type()
)
fsSSIfTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSSIfTrunk.setStatus("current")


class _FsSSIfSpeed_Type(Integer32):
    """Custom type fsSSIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed_10M", 0),
          ("speed_100M", 1),
          ("speed_1000M", 2))
    )


_FsSSIfSpeed_Type.__name__ = "Integer32"
_FsSSIfSpeed_Object = MibTableColumn
fsSSIfSpeed = _FsSSIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 5),
    _FsSSIfSpeed_Type()
)
fsSSIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSSIfSpeed.setStatus("current")


class _FsSSIfDuplex_Type(Integer32):
    """Custom type fsSSIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )


_FsSSIfDuplex_Type.__name__ = "Integer32"
_FsSSIfDuplex_Object = MibTableColumn
fsSSIfDuplex = _FsSSIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 6),
    _FsSSIfDuplex_Type()
)
fsSSIfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSSIfDuplex.setStatus("current")


class _FsSSIfNegotiation_Type(Integer32):
    """Custom type fsSSIfNegotiation based on Integer32"""
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


_FsSSIfNegotiation_Type.__name__ = "Integer32"
_FsSSIfNegotiation_Object = MibTableColumn
fsSSIfNegotiation = _FsSSIfNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 14, 1, 7),
    _FsSSIfNegotiation_Type()
)
fsSSIfNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSSIfNegotiation.setStatus("current")


class _FsRs485IpSetStatus_Type(Integer32):
    """Custom type fsRs485IpSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1),
          ("dhcp", 2))
    )


_FsRs485IpSetStatus_Type.__name__ = "Integer32"
_FsRs485IpSetStatus_Object = MibScalar
fsRs485IpSetStatus = _FsRs485IpSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 15),
    _FsRs485IpSetStatus_Type()
)
fsRs485IpSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485IpSetStatus.setStatus("current")
_FsLabelIDReg_Type = PhysAddress
_FsLabelIDReg_Object = MibScalar
fsLabelIDReg = _FsLabelIDReg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 16),
    _FsLabelIDReg_Type()
)
fsLabelIDReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLabelIDReg.setStatus("current")


class _FsLabelTypeReg_Type(Integer32):
    """Custom type fsLabelTypeReg based on Integer32"""
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
        *(("default", 0),
          ("rfid", 1),
          ("ble", 2),
          ("zibgee", 3))
    )


_FsLabelTypeReg_Type.__name__ = "Integer32"
_FsLabelTypeReg_Object = MibScalar
fsLabelTypeReg = _FsLabelTypeReg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 17),
    _FsLabelTypeReg_Type()
)
fsLabelTypeReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLabelTypeReg.setStatus("current")


class _FsLabelRegStatus_Type(Integer32):
    """Custom type fsLabelRegStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1))
    )


_FsLabelRegStatus_Type.__name__ = "Integer32"
_FsLabelRegStatus_Object = MibScalar
fsLabelRegStatus = _FsLabelRegStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 18),
    _FsLabelRegStatus_Type()
)
fsLabelRegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLabelRegStatus.setStatus("current")
_FsLabelInfoTable_Object = MibTable
fsLabelInfoTable = _FsLabelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19)
)
if mibBuilder.loadTexts:
    fsLabelInfoTable.setStatus("current")
_FsLabelInfoEntry_Object = MibTableRow
fsLabelInfoEntry = _FsLabelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1)
)
fsLabelInfoEntry.setIndexNames(
    (0, "FS-RS485-CLASS-MIB", "fsLabelType"),
    (0, "FS-RS485-CLASS-MIB", "fsLabelID"),
)
if mibBuilder.loadTexts:
    fsLabelInfoEntry.setStatus("current")


class _FsLabelType_Type(Integer32):
    """Custom type fsLabelType based on Integer32"""
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
        *(("unknown", 0),
          ("rfid", 1),
          ("ble", 2),
          ("zigbee", 3))
    )


_FsLabelType_Type.__name__ = "Integer32"
_FsLabelType_Object = MibTableColumn
fsLabelType = _FsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 1),
    _FsLabelType_Type()
)
fsLabelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLabelType.setStatus("current")
_FsLabelID_Type = PhysAddress
_FsLabelID_Object = MibTableColumn
fsLabelID = _FsLabelID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 2),
    _FsLabelID_Type()
)
fsLabelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLabelID.setStatus("current")


class _FsLabelActiveStatus_Type(Integer32):
    """Custom type fsLabelActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("deactive", 2),
          ("active-success-ack", 3),
          ("active-fail-ack", 4),
          ("deactive-success-ack", 5),
          ("deactive-fail-ack", 6))
    )


_FsLabelActiveStatus_Type.__name__ = "Integer32"
_FsLabelActiveStatus_Object = MibTableColumn
fsLabelActiveStatus = _FsLabelActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 3),
    _FsLabelActiveStatus_Type()
)
fsLabelActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLabelActiveStatus.setStatus("current")


class _FsLabelPowerStatus_Type(Integer32):
    """Custom type fsLabelPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsLabelPowerStatus_Type.__name__ = "Integer32"
_FsLabelPowerStatus_Object = MibTableColumn
fsLabelPowerStatus = _FsLabelPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 4),
    _FsLabelPowerStatus_Type()
)
fsLabelPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLabelPowerStatus.setStatus("current")


class _FsLabelWarningCancel_Type(Integer32):
    """Custom type fsLabelWarningCancel based on Integer32"""
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
        *(("unknown", 0),
          ("cancel-stolen", 1),
          ("cancel-power", 2),
          ("cancel-unnormal", 3))
    )


_FsLabelWarningCancel_Type.__name__ = "Integer32"
_FsLabelWarningCancel_Object = MibTableColumn
fsLabelWarningCancel = _FsLabelWarningCancel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 5),
    _FsLabelWarningCancel_Type()
)
fsLabelWarningCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLabelWarningCancel.setStatus("current")


class _FsLabelUnregStatus_Type(Integer32):
    """Custom type fsLabelUnregStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("apply-unreg", 1),
          ("unreg", 2),
          ("allow-unreg", 3),
          ("not-allow-unreg", 4),
          ("reg-success", 5),
          ("reg-failed", 6))
    )


_FsLabelUnregStatus_Type.__name__ = "Integer32"
_FsLabelUnregStatus_Object = MibTableColumn
fsLabelUnregStatus = _FsLabelUnregStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 6),
    _FsLabelUnregStatus_Type()
)
fsLabelUnregStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLabelUnregStatus.setStatus("current")


class _FsLabelStolenWarningStatus_Type(Integer32):
    """Custom type fsLabelStolenWarningStatus based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("stolen", 2),
          ("unnormal", 3))
    )


_FsLabelStolenWarningStatus_Type.__name__ = "Integer32"
_FsLabelStolenWarningStatus_Object = MibTableColumn
fsLabelStolenWarningStatus = _FsLabelStolenWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 19, 1, 7),
    _FsLabelStolenWarningStatus_Type()
)
fsLabelStolenWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLabelStolenWarningStatus.setStatus("current")
_FsRs485TrapIp_Type = IpAddress
_FsRs485TrapIp_Object = MibScalar
fsRs485TrapIp = _FsRs485TrapIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 20),
    _FsRs485TrapIp_Type()
)
fsRs485TrapIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRs485TrapIp.setStatus("current")


class _FsRs485HeartbeatStatus_Type(Integer32):
    """Custom type fsRs485HeartbeatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("normal", 1))
    )


_FsRs485HeartbeatStatus_Type.__name__ = "Integer32"
_FsRs485HeartbeatStatus_Object = MibScalar
fsRs485HeartbeatStatus = _FsRs485HeartbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 21),
    _FsRs485HeartbeatStatus_Type()
)
fsRs485HeartbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRs485HeartbeatStatus.setStatus("current")


class _FsClassPDUPower1_Type(Integer32):
    """Custom type fsClassPDUPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("break", 1),
          ("normal", 2))
    )


_FsClassPDUPower1_Type.__name__ = "Integer32"
_FsClassPDUPower1_Object = MibScalar
fsClassPDUPower1 = _FsClassPDUPower1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 22),
    _FsClassPDUPower1_Type()
)
fsClassPDUPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassPDUPower1.setStatus("current")


class _FsClassPDUPower2_Type(Integer32):
    """Custom type fsClassPDUPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("break", 1),
          ("normal", 2))
    )


_FsClassPDUPower2_Type.__name__ = "Integer32"
_FsClassPDUPower2_Object = MibScalar
fsClassPDUPower2 = _FsClassPDUPower2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 23),
    _FsClassPDUPower2_Type()
)
fsClassPDUPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassPDUPower2.setStatus("current")


class _FsClassDeviceAddType_Type(Integer32):
    """Custom type fsClassDeviceAddType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("video", 1),
          ("audio", 2),
          ("videoandaudio", 3),
          ("light", 4),
          ("air-con", 5),
          ("record", 6),
          ("projector", 7),
          ("screen", 8),
          ("app-pad", 9),
          ("smart-switch", 10))
    )


_FsClassDeviceAddType_Type.__name__ = "Integer32"
_FsClassDeviceAddType_Object = MibScalar
fsClassDeviceAddType = _FsClassDeviceAddType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 24),
    _FsClassDeviceAddType_Type()
)
fsClassDeviceAddType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceAddType.setStatus("current")
_FsClassDeviceAddID_Type = Integer32
_FsClassDeviceAddID_Object = MibScalar
fsClassDeviceAddID = _FsClassDeviceAddID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 25),
    _FsClassDeviceAddID_Type()
)
fsClassDeviceAddID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceAddID.setStatus("current")


class _FsClassDeviceAddStatus_Type(Integer32):
    """Custom type fsClassDeviceAddStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("add", 1)
    )


_FsClassDeviceAddStatus_Type.__name__ = "Integer32"
_FsClassDeviceAddStatus_Object = MibScalar
fsClassDeviceAddStatus = _FsClassDeviceAddStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 26),
    _FsClassDeviceAddStatus_Type()
)
fsClassDeviceAddStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceAddStatus.setStatus("current")
_FsClassDeviceInfoTable_Object = MibTable
fsClassDeviceInfoTable = _FsClassDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27)
)
if mibBuilder.loadTexts:
    fsClassDeviceInfoTable.setStatus("current")
_FsClassDeviceInfoEntry_Object = MibTableRow
fsClassDeviceInfoEntry = _FsClassDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1)
)
fsClassDeviceInfoEntry.setIndexNames(
    (0, "FS-RS485-CLASS-MIB", "fsClassDeviceType"),
    (0, "FS-RS485-CLASS-MIB", "fsClassDeviceID"),
)
if mibBuilder.loadTexts:
    fsClassDeviceInfoEntry.setStatus("current")


class _FsClassDeviceType_Type(Integer32):
    """Custom type fsClassDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("video", 1),
          ("audio", 2),
          ("videoandaudio", 3),
          ("light", 4),
          ("air-con", 5),
          ("record", 6),
          ("projector", 7),
          ("screen", 8),
          ("app-pad", 9),
          ("smart-switch", 10))
    )


_FsClassDeviceType_Type.__name__ = "Integer32"
_FsClassDeviceType_Object = MibTableColumn
fsClassDeviceType = _FsClassDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 1),
    _FsClassDeviceType_Type()
)
fsClassDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassDeviceType.setStatus("current")
_FsClassDeviceID_Type = Integer32
_FsClassDeviceID_Object = MibTableColumn
fsClassDeviceID = _FsClassDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 2),
    _FsClassDeviceID_Type()
)
fsClassDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassDeviceID.setStatus("current")
_FsClassDeviceIconType_Type = Integer32
_FsClassDeviceIconType_Object = MibTableColumn
fsClassDeviceIconType = _FsClassDeviceIconType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 3),
    _FsClassDeviceIconType_Type()
)
fsClassDeviceIconType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceIconType.setStatus("current")


class _FsClassDeviceName_Type(OctetString):
    """Custom type fsClassDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsClassDeviceName_Type.__name__ = "OctetString"
_FsClassDeviceName_Object = MibTableColumn
fsClassDeviceName = _FsClassDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 4),
    _FsClassDeviceName_Type()
)
fsClassDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceName.setStatus("current")
_FsClassDeviceModelID_Type = Integer32
_FsClassDeviceModelID_Object = MibTableColumn
fsClassDeviceModelID = _FsClassDeviceModelID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 5),
    _FsClassDeviceModelID_Type()
)
fsClassDeviceModelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceModelID.setStatus("current")


class _FsClassDeviceControlSerial_Type(Integer32):
    """Custom type fsClassDeviceControlSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsClassDeviceControlSerial_Type.__name__ = "Integer32"
_FsClassDeviceControlSerial_Object = MibTableColumn
fsClassDeviceControlSerial = _FsClassDeviceControlSerial_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 6),
    _FsClassDeviceControlSerial_Type()
)
fsClassDeviceControlSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceControlSerial.setStatus("current")


class _FsClassDeviceTeleControlPort_Type(Integer32):
    """Custom type fsClassDeviceTeleControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsClassDeviceTeleControlPort_Type.__name__ = "Integer32"
_FsClassDeviceTeleControlPort_Object = MibTableColumn
fsClassDeviceTeleControlPort = _FsClassDeviceTeleControlPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 7),
    _FsClassDeviceTeleControlPort_Type()
)
fsClassDeviceTeleControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceTeleControlPort.setStatus("current")


class _FsClassDeviceIOType_Type(Integer32):
    """Custom type fsClassDeviceIOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 0),
          ("output", 1),
          ("other", 2))
    )


_FsClassDeviceIOType_Type.__name__ = "Integer32"
_FsClassDeviceIOType_Object = MibTableColumn
fsClassDeviceIOType = _FsClassDeviceIOType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 8),
    _FsClassDeviceIOType_Type()
)
fsClassDeviceIOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceIOType.setStatus("current")


class _FsClassDeviceVideoPort_Type(Integer32):
    """Custom type fsClassDeviceVideoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FsClassDeviceVideoPort_Type.__name__ = "Integer32"
_FsClassDeviceVideoPort_Object = MibTableColumn
fsClassDeviceVideoPort = _FsClassDeviceVideoPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 9),
    _FsClassDeviceVideoPort_Type()
)
fsClassDeviceVideoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceVideoPort.setStatus("current")


class _FsClassDeviceAudioPort_Type(Integer32):
    """Custom type fsClassDeviceAudioPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FsClassDeviceAudioPort_Type.__name__ = "Integer32"
_FsClassDeviceAudioPort_Object = MibTableColumn
fsClassDeviceAudioPort = _FsClassDeviceAudioPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 10),
    _FsClassDeviceAudioPort_Type()
)
fsClassDeviceAudioPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceAudioPort.setStatus("current")


class _FsClassDeviceVideoUsedStatus_Type(Integer32):
    """Custom type fsClassDeviceVideoUsedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("used", 1))
    )


_FsClassDeviceVideoUsedStatus_Type.__name__ = "Integer32"
_FsClassDeviceVideoUsedStatus_Object = MibTableColumn
fsClassDeviceVideoUsedStatus = _FsClassDeviceVideoUsedStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 11),
    _FsClassDeviceVideoUsedStatus_Type()
)
fsClassDeviceVideoUsedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceVideoUsedStatus.setStatus("current")


class _FsClassDeviceAudioUsedStatus_Type(Integer32):
    """Custom type fsClassDeviceAudioUsedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("used", 1))
    )


_FsClassDeviceAudioUsedStatus_Type.__name__ = "Integer32"
_FsClassDeviceAudioUsedStatus_Object = MibTableColumn
fsClassDeviceAudioUsedStatus = _FsClassDeviceAudioUsedStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 12),
    _FsClassDeviceAudioUsedStatus_Type()
)
fsClassDeviceAudioUsedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceAudioUsedStatus.setStatus("current")
_FsClassDeviceSwitch_Type = Integer32
_FsClassDeviceSwitch_Object = MibTableColumn
fsClassDeviceSwitch = _FsClassDeviceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 13),
    _FsClassDeviceSwitch_Type()
)
fsClassDeviceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceSwitch.setStatus("current")


class _FsClassDeviceState_Type(Integer32):
    """Custom type fsClassDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("normal", 1),
          ("no-ack", 2))
    )


_FsClassDeviceState_Type.__name__ = "Integer32"
_FsClassDeviceState_Object = MibTableColumn
fsClassDeviceState = _FsClassDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 14),
    _FsClassDeviceState_Type()
)
fsClassDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceState.setStatus("current")
_FsClassDeviceZigbeeID_Type = Integer32
_FsClassDeviceZigbeeID_Object = MibTableColumn
fsClassDeviceZigbeeID = _FsClassDeviceZigbeeID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 15),
    _FsClassDeviceZigbeeID_Type()
)
fsClassDeviceZigbeeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceZigbeeID.setStatus("current")


class _FsClassDeviceSetStatus_Type(Integer32):
    """Custom type fsClassDeviceSetStatus based on Integer32"""
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
        *(("unset", 0),
          ("set", 1),
          ("delete", 2),
          ("update", 3))
    )


_FsClassDeviceSetStatus_Type.__name__ = "Integer32"
_FsClassDeviceSetStatus_Object = MibTableColumn
fsClassDeviceSetStatus = _FsClassDeviceSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 16),
    _FsClassDeviceSetStatus_Type()
)
fsClassDeviceSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceSetStatus.setStatus("current")
_FsClassDeviceIP_Type = IpAddress
_FsClassDeviceIP_Object = MibTableColumn
fsClassDeviceIP = _FsClassDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 17),
    _FsClassDeviceIP_Type()
)
fsClassDeviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeviceIP.setStatus("current")
_FsClassBindDeviceID_Type = Integer32
_FsClassBindDeviceID_Object = MibTableColumn
fsClassBindDeviceID = _FsClassBindDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 18),
    _FsClassBindDeviceID_Type()
)
fsClassBindDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassBindDeviceID.setStatus("current")
_FsClassBatchSupport_Type = Integer32
_FsClassBatchSupport_Object = MibTableColumn
fsClassBatchSupport = _FsClassBatchSupport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 27, 1, 19),
    _FsClassBatchSupport_Type()
)
fsClassBatchSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassBatchSupport.setStatus("current")


class _FsClassAPPUsername_Type(OctetString):
    """Custom type fsClassAPPUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_FsClassAPPUsername_Type.__name__ = "OctetString"
_FsClassAPPUsername_Object = MibScalar
fsClassAPPUsername = _FsClassAPPUsername_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 28),
    _FsClassAPPUsername_Type()
)
fsClassAPPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassAPPUsername.setStatus("current")


class _FsClassAPPPassword_Type(OctetString):
    """Custom type fsClassAPPPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_FsClassAPPPassword_Type.__name__ = "OctetString"
_FsClassAPPPassword_Object = MibScalar
fsClassAPPPassword = _FsClassAPPPassword_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 29),
    _FsClassAPPPassword_Type()
)
fsClassAPPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassAPPPassword.setStatus("current")


class _FsClassAPPAuth_Type(Integer32):
    """Custom type fsClassAPPAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failed", 1),
          ("success-update", 2),
          ("card-success", 3),
          ("card-failed", 4),
          ("user-info", 5))
    )


_FsClassAPPAuth_Type.__name__ = "Integer32"
_FsClassAPPAuth_Object = MibScalar
fsClassAPPAuth = _FsClassAPPAuth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 30),
    _FsClassAPPAuth_Type()
)
fsClassAPPAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassAPPAuth.setStatus("current")
_FsClassCMDDeviceModelID_Type = Integer32
_FsClassCMDDeviceModelID_Object = MibScalar
fsClassCMDDeviceModelID = _FsClassCMDDeviceModelID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 31),
    _FsClassCMDDeviceModelID_Type()
)
fsClassCMDDeviceModelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassCMDDeviceModelID.setStatus("current")
_FsClassCMDType_Type = Integer32
_FsClassCMDType_Object = MibScalar
fsClassCMDType = _FsClassCMDType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 32),
    _FsClassCMDType_Type()
)
fsClassCMDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassCMDType.setStatus("current")


class _FsClassCommand_Type(OctetString):
    """Custom type fsClassCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsClassCommand_Type.__name__ = "OctetString"
_FsClassCommand_Object = MibScalar
fsClassCommand = _FsClassCommand_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 33),
    _FsClassCommand_Type()
)
fsClassCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassCommand.setStatus("current")


class _FsClassCommandSetStatus_Type(Integer32):
    """Custom type fsClassCommandSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-get", 1),
          ("set", 2),
          ("delete", 3))
    )


_FsClassCommandSetStatus_Type.__name__ = "Integer32"
_FsClassCommandSetStatus_Object = MibScalar
fsClassCommandSetStatus = _FsClassCommandSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 34),
    _FsClassCommandSetStatus_Type()
)
fsClassCommandSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassCommandSetStatus.setStatus("current")


class _FsClassOperAll_Type(Integer32):
    """Custom type fsClassOperAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open-all", 1),
          ("close-all", 2))
    )


_FsClassOperAll_Type.__name__ = "Integer32"
_FsClassOperAll_Object = MibScalar
fsClassOperAll = _FsClassOperAll_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 35),
    _FsClassOperAll_Type()
)
fsClassOperAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassOperAll.setStatus("current")


class _FsClassCardID_Type(OctetString):
    """Custom type fsClassCardID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_FsClassCardID_Type.__name__ = "OctetString"
_FsClassCardID_Object = MibScalar
fsClassCardID = _FsClassCardID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 36),
    _FsClassCardID_Type()
)
fsClassCardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassCardID.setStatus("current")
_FsClassDateTime_Type = Integer32
_FsClassDateTime_Object = MibScalar
fsClassDateTime = _FsClassDateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 37),
    _FsClassDateTime_Type()
)
fsClassDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDateTime.setStatus("current")


class _FsClassAPPUpdateReq_Type(Integer32):
    """Custom type fsClassAPPUpdateReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("device_req", 1),
          ("user_auth_req", 2))
    )


_FsClassAPPUpdateReq_Type.__name__ = "Integer32"
_FsClassAPPUpdateReq_Object = MibScalar
fsClassAPPUpdateReq = _FsClassAPPUpdateReq_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 38),
    _FsClassAPPUpdateReq_Type()
)
fsClassAPPUpdateReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassAPPUpdateReq.setStatus("current")


class _FsClassUpdateFileName_Type(OctetString):
    """Custom type fsClassUpdateFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsClassUpdateFileName_Type.__name__ = "OctetString"
_FsClassUpdateFileName_Object = MibScalar
fsClassUpdateFileName = _FsClassUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 39),
    _FsClassUpdateFileName_Type()
)
fsClassUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassUpdateFileName.setStatus("current")


class _FsClassUpdate_Type(Integer32):
    """Custom type fsClassUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_FsClassUpdate_Type.__name__ = "Integer32"
_FsClassUpdate_Object = MibScalar
fsClassUpdate = _FsClassUpdate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 40),
    _FsClassUpdate_Type()
)
fsClassUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassUpdate.setStatus("current")


class _FsClassSoftVersion_Type(OctetString):
    """Custom type fsClassSoftVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsClassSoftVersion_Type.__name__ = "OctetString"
_FsClassSoftVersion_Object = MibScalar
fsClassSoftVersion = _FsClassSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 41),
    _FsClassSoftVersion_Type()
)
fsClassSoftVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassSoftVersion.setStatus("current")


class _FsClassChannel_Type(OctetString):
    """Custom type fsClassChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FsClassChannel_Type.__name__ = "OctetString"
_FsClassChannel_Object = MibScalar
fsClassChannel = _FsClassChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 42),
    _FsClassChannel_Type()
)
fsClassChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassChannel.setStatus("current")
_FsClassOldDeviceIP_Type = IpAddress
_FsClassOldDeviceIP_Object = MibScalar
fsClassOldDeviceIP = _FsClassOldDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 43),
    _FsClassOldDeviceIP_Type()
)
fsClassOldDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassOldDeviceIP.setStatus("current")


class _FsClassCommunity_Type(OctetString):
    """Custom type fsClassCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsClassCommunity_Type.__name__ = "OctetString"
_FsClassCommunity_Object = MibScalar
fsClassCommunity = _FsClassCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 44),
    _FsClassCommunity_Type()
)
fsClassCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassCommunity.setStatus("current")


class _FsClassUpdateStatus_Type(Integer32):
    """Custom type fsClassUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("scc_update_start", 1),
          ("scc_update_success", 2),
          ("scc_update_crc_error", 3),
          ("scc_update_product_id_error", 4),
          ("scc_update_tftp_timeout_error", 5),
          ("remote_device_update_no_existerror", 6),
          ("scc_update_file_too_big_error", 7))
    )


_FsClassUpdateStatus_Type.__name__ = "Integer32"
_FsClassUpdateStatus_Object = MibScalar
fsClassUpdateStatus = _FsClassUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 45),
    _FsClassUpdateStatus_Type()
)
fsClassUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassUpdateStatus.setStatus("current")


class _FsClassScheduleTableName_Type(OctetString):
    """Custom type fsClassScheduleTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsClassScheduleTableName_Type.__name__ = "OctetString"
_FsClassScheduleTableName_Object = MibScalar
fsClassScheduleTableName = _FsClassScheduleTableName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 46),
    _FsClassScheduleTableName_Type()
)
fsClassScheduleTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassScheduleTableName.setStatus("current")


class _FsClassUpdateScheduleTable_Type(Integer32):
    """Custom type fsClassUpdateScheduleTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_FsClassUpdateScheduleTable_Type.__name__ = "Integer32"
_FsClassUpdateScheduleTable_Object = MibScalar
fsClassUpdateScheduleTable = _FsClassUpdateScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 47),
    _FsClassUpdateScheduleTable_Type()
)
fsClassUpdateScheduleTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassUpdateScheduleTable.setStatus("current")


class _FsClassScheduleTableUpdateStatus_Type(Integer32):
    """Custom type fsClassScheduleTableUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("init", 0),
          ("scc_update_start", 1),
          ("scc_update_success", 2),
          ("scc_update_crc_error", 3),
          ("scc_update_product_id_error", 4),
          ("scc_update_tftp_timeout_error", 5),
          ("scc_remote_no_exist_error", 6),
          ("scc_update_file_too_big_error", 7),
          ("scc_update_redo", 8))
    )


_FsClassScheduleTableUpdateStatus_Type.__name__ = "Integer32"
_FsClassScheduleTableUpdateStatus_Object = MibScalar
fsClassScheduleTableUpdateStatus = _FsClassScheduleTableUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 48),
    _FsClassScheduleTableUpdateStatus_Type()
)
fsClassScheduleTableUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassScheduleTableUpdateStatus.setStatus("current")


class _FsClassCheckTableName_Type(OctetString):
    """Custom type fsClassCheckTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsClassCheckTableName_Type.__name__ = "OctetString"
_FsClassCheckTableName_Object = MibScalar
fsClassCheckTableName = _FsClassCheckTableName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 49),
    _FsClassCheckTableName_Type()
)
fsClassCheckTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassCheckTableName.setStatus("current")


class _FsClassReadCheckTable_Type(Integer32):
    """Custom type fsClassReadCheckTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_FsClassReadCheckTable_Type.__name__ = "Integer32"
_FsClassReadCheckTable_Object = MibScalar
fsClassReadCheckTable = _FsClassReadCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 50),
    _FsClassReadCheckTable_Type()
)
fsClassReadCheckTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassReadCheckTable.setStatus("current")


class _FsClassReadCheckTable1UploadStatus_Type(Integer32):
    """Custom type fsClassReadCheckTable1UploadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("scc_update_start", 1),
          ("scc_update_success", 2),
          ("scc_update_crc_error", 3),
          ("scc_update_product_id_error", 4),
          ("scc_update_tftp_timeout_error", 5),
          ("scc_remote_no_exist_error", 6),
          ("scc_update_file_too_big_error", 7))
    )


_FsClassReadCheckTable1UploadStatus_Type.__name__ = "Integer32"
_FsClassReadCheckTable1UploadStatus_Object = MibScalar
fsClassReadCheckTable1UploadStatus = _FsClassReadCheckTable1UploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 51),
    _FsClassReadCheckTable1UploadStatus_Type()
)
fsClassReadCheckTable1UploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassReadCheckTable1UploadStatus.setStatus("current")
_FsClassLampTimeClass_Type = Integer32
_FsClassLampTimeClass_Object = MibScalar
fsClassLampTimeClass = _FsClassLampTimeClass_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 52),
    _FsClassLampTimeClass_Type()
)
fsClassLampTimeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassLampTimeClass.setStatus("current")


class _FsClassDeleteRecordTable_Type(Integer32):
    """Custom type fsClassDeleteRecordTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_FsClassDeleteRecordTable_Type.__name__ = "Integer32"
_FsClassDeleteRecordTable_Object = MibScalar
fsClassDeleteRecordTable = _FsClassDeleteRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 53),
    _FsClassDeleteRecordTable_Type()
)
fsClassDeleteRecordTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassDeleteRecordTable.setStatus("current")
_FsClassSystemTime_Type = Counter32
_FsClassSystemTime_Object = MibScalar
fsClassSystemTime = _FsClassSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 54),
    _FsClassSystemTime_Type()
)
fsClassSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClassSystemTime.setStatus("current")


class _FsClassProjectorFact_Type(OctetString):
    """Custom type fsClassProjectorFact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsClassProjectorFact_Type.__name__ = "OctetString"
_FsClassProjectorFact_Object = MibScalar
fsClassProjectorFact = _FsClassProjectorFact_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 55),
    _FsClassProjectorFact_Type()
)
fsClassProjectorFact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassProjectorFact.setStatus("current")


class _FsClassProjectorModel_Type(OctetString):
    """Custom type fsClassProjectorModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsClassProjectorModel_Type.__name__ = "OctetString"
_FsClassProjectorModel_Object = MibScalar
fsClassProjectorModel = _FsClassProjectorModel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 56),
    _FsClassProjectorModel_Type()
)
fsClassProjectorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassProjectorModel.setStatus("current")


class _FsClassAIOFact_Type(OctetString):
    """Custom type fsClassAIOFact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsClassAIOFact_Type.__name__ = "OctetString"
_FsClassAIOFact_Object = MibScalar
fsClassAIOFact = _FsClassAIOFact_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 57),
    _FsClassAIOFact_Type()
)
fsClassAIOFact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassAIOFact.setStatus("current")


class _FsClassAIOModel_Type(OctetString):
    """Custom type fsClassAIOModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsClassAIOModel_Type.__name__ = "OctetString"
_FsClassAIOModel_Object = MibScalar
fsClassAIOModel = _FsClassAIOModel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 1, 58),
    _FsClassAIOModel_Type()
)
fsClassAIOModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClassAIOModel.setStatus("current")
_FsRs485MIBTrap_ObjectIdentity = ObjectIdentity
fsRs485MIBTrap = _FsRs485MIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2)
)

# Managed Objects groups


# Notification objects

fsRs485StateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 0)
)
fsRs485StateChange.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485State")
)
if mibBuilder.loadTexts:
    fsRs485StateChange.setStatus(
        "current"
    )

fsRs485Power1Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 1)
)
fsRs485Power1Change.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485SerialPower1")
)
if mibBuilder.loadTexts:
    fsRs485Power1Change.setStatus(
        "current"
    )

fsRs485Power2Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 2)
)
fsRs485Power2Change.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485SerialPower2")
)
if mibBuilder.loadTexts:
    fsRs485Power2Change.setStatus(
        "current"
    )

fsRs485Power3Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 3)
)
fsRs485Power3Change.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485SerialPower3")
)
if mibBuilder.loadTexts:
    fsRs485Power3Change.setStatus(
        "current"
    )

fsRs485Power4Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 4)
)
fsRs485Power4Change.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485SerialPower4")
)
if mibBuilder.loadTexts:
    fsRs485Power4Change.setStatus(
        "current"
    )

fsRs485TelnetFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 5)
)
fsRs485TelnetFail.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485TelnetIp")
)
if mibBuilder.loadTexts:
    fsRs485TelnetFail.setStatus(
        "current"
    )

fsLabelActiveACK = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 6)
)
fsLabelActiveACK.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsLabelType"),
        ("FS-RS485-CLASS-MIB", "fsLabelID"),
        ("FS-RS485-CLASS-MIB", "fsLabelActiveStatus"))
)
if mibBuilder.loadTexts:
    fsLabelActiveACK.setStatus(
        "current"
    )

fsLabelLowPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 7)
)
fsLabelLowPower.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsLabelType"),
        ("FS-RS485-CLASS-MIB", "fsLabelID"),
        ("FS-RS485-CLASS-MIB", "fsLabelPowerStatus"))
)
if mibBuilder.loadTexts:
    fsLabelLowPower.setStatus(
        "current"
    )

fsLabelStolen = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 8)
)
fsLabelStolen.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsLabelType"),
        ("FS-RS485-CLASS-MIB", "fsLabelID"),
        ("FS-RS485-CLASS-MIB", "fsLabelStolenWarningStatus"))
)
if mibBuilder.loadTexts:
    fsLabelStolen.setStatus(
        "current"
    )

fsLabelUnregACK = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 9)
)
fsLabelUnregACK.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsLabelType"),
        ("FS-RS485-CLASS-MIB", "fsLabelID"),
        ("FS-RS485-CLASS-MIB", "fsLabelUnregStatus"))
)
if mibBuilder.loadTexts:
    fsLabelUnregACK.setStatus(
        "current"
    )

fsRs485Heartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 10)
)
fsRs485Heartbeat.setObjects(
    ("FS-RS485-CLASS-MIB", "fsRs485HeartbeatStatus")
)
if mibBuilder.loadTexts:
    fsRs485Heartbeat.setStatus(
        "current"
    )

fsLabelRegACK = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 11)
)
fsLabelRegACK.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsLabelType"),
        ("FS-RS485-CLASS-MIB", "fsLabelID"),
        ("FS-RS485-CLASS-MIB", "fsLabelUnregStatus"))
)
if mibBuilder.loadTexts:
    fsLabelRegACK.setStatus(
        "current"
    )

fsClassAPPLoginREQ = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 12)
)
fsClassAPPLoginREQ.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassAPPUsername"),
        ("FS-RS485-CLASS-MIB", "fsClassAPPPassword"),
        ("FS-RS485-CLASS-MIB", "fsClassDateTime"))
)
if mibBuilder.loadTexts:
    fsClassAPPLoginREQ.setStatus(
        "current"
    )

fsClassAPPOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 13)
)
fsClassAPPOperation.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassDeviceType"),
        ("FS-RS485-CLASS-MIB", "fsClassDeviceID"),
        ("FS-RS485-CLASS-MIB", "fsClassDeviceSwitch"),
        ("FS-RS485-CLASS-MIB", "fsClassDeviceState"))
)
if mibBuilder.loadTexts:
    fsClassAPPOperation.setStatus(
        "current"
    )

fsClassTelecommand = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 14)
)
fsClassTelecommand.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassDeviceType"),
        ("FS-RS485-CLASS-MIB", "fsClassCMDType"),
        ("FS-RS485-CLASS-MIB", "fsClassCommand"))
)
if mibBuilder.loadTexts:
    fsClassTelecommand.setStatus(
        "current"
    )

fsClassSwipeCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 15)
)
fsClassSwipeCard.setObjects(
    ("FS-RS485-CLASS-MIB", "fsClassCardID")
)
if mibBuilder.loadTexts:
    fsClassSwipeCard.setStatus(
        "current"
    )

fsClassUpdateReq = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 16)
)
fsClassUpdateReq.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassAPPUpdateReq"),
        ("FS-RS485-CLASS-MIB", "fsClassDateTime"))
)
if mibBuilder.loadTexts:
    fsClassUpdateReq.setStatus(
        "current"
    )

fsClassOperationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 17)
)
fsClassOperationAll.setObjects(
    ("FS-RS485-CLASS-MIB", "fsClassOperAll")
)
if mibBuilder.loadTexts:
    fsClassOperationAll.setStatus(
        "current"
    )

fsClassChannelToServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 18)
)
fsClassChannelToServer.setObjects(
    ("FS-RS485-CLASS-MIB", "fsClassChannel")
)
if mibBuilder.loadTexts:
    fsClassChannelToServer.setStatus(
        "current"
    )

fsClassDevIPChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 19)
)
fsClassDevIPChange.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassOldDeviceIP"),
        ("FS-RS485-CLASS-MIB", "fsRs485IpAddress"),
        ("FS-RS485-CLASS-MIB", "fsRs485Mac"))
)
if mibBuilder.loadTexts:
    fsClassDevIPChange.setStatus(
        "current"
    )

fsClassCardOperationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 20)
)
fsClassCardOperationAll.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassCardID"),
        ("FS-RS485-CLASS-MIB", "fsClassOperAll"))
)
if mibBuilder.loadTexts:
    fsClassCardOperationAll.setStatus(
        "current"
    )

fsClassAccountOperationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 21)
)
fsClassAccountOperationAll.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassAPPUsername"),
        ("FS-RS485-CLASS-MIB", "fsClassAPPPassword"),
        ("FS-RS485-CLASS-MIB", "fsClassOperAll"))
)
if mibBuilder.loadTexts:
    fsClassAccountOperationAll.setStatus(
        "current"
    )

fsClassTableRedo = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 22)
)
fsClassTableRedo.setObjects(
    ("FS-RS485-CLASS-MIB", "fsClassScheduleTableUpdateStatus")
)
if mibBuilder.loadTexts:
    fsClassTableRedo.setStatus(
        "current"
    )

fsClassDeviceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 149, 2, 23)
)
fsClassDeviceStateChange.setObjects(
      *(("FS-RS485-CLASS-MIB", "fsClassDeviceID"),
        ("FS-RS485-CLASS-MIB", "fsClassDeviceState"))
)
if mibBuilder.loadTexts:
    fsClassDeviceStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-RS485-CLASS-MIB",
    **{"fsRs485MIB": fsRs485MIB,
       "fsRs485MIBObjects": fsRs485MIBObjects,
       "fsRs485IpAddress": fsRs485IpAddress,
       "fsRs485IpAddressMask": fsRs485IpAddressMask,
       "fsRs485Gateway": fsRs485Gateway,
       "fsRs485Mac": fsRs485Mac,
       "fsRs485ServerMode": fsRs485ServerMode,
       "fsRs485SerialNum": fsRs485SerialNum,
       "fsRs485TelnetIp": fsRs485TelnetIp,
       "fsRs485State": fsRs485State,
       "fsRs485SerialPower1": fsRs485SerialPower1,
       "fsRs485SerialPower2": fsRs485SerialPower2,
       "fsRs485SerialPower3": fsRs485SerialPower3,
       "fsRs485SerialPower4": fsRs485SerialPower4,
       "fsRs485VlanTable": fsRs485VlanTable,
       "fsRs485VlanEntry": fsRs485VlanEntry,
       "fsRs485SerialPort": fsRs485SerialPort,
       "fsRs485VLANID": fsRs485VLANID,
       "fsRs485Baudrate": fsRs485Baudrate,
       "fsRs485Parity": fsRs485Parity,
       "fsClassSerialType": fsClassSerialType,
       "fsClassStatus": fsClassStatus,
       "fsClassIsTeleControl": fsClassIsTeleControl,
       "fsSSIfTable": fsSSIfTable,
       "fsSSIfEntry": fsSSIfEntry,
       "fsSSIfIndex": fsSSIfIndex,
       "fsSSIfAccessVlan": fsSSIfAccessVlan,
       "fsSSIfNativeVlan": fsSSIfNativeVlan,
       "fsSSIfTrunk": fsSSIfTrunk,
       "fsSSIfSpeed": fsSSIfSpeed,
       "fsSSIfDuplex": fsSSIfDuplex,
       "fsSSIfNegotiation": fsSSIfNegotiation,
       "fsRs485IpSetStatus": fsRs485IpSetStatus,
       "fsLabelIDReg": fsLabelIDReg,
       "fsLabelTypeReg": fsLabelTypeReg,
       "fsLabelRegStatus": fsLabelRegStatus,
       "fsLabelInfoTable": fsLabelInfoTable,
       "fsLabelInfoEntry": fsLabelInfoEntry,
       "fsLabelType": fsLabelType,
       "fsLabelID": fsLabelID,
       "fsLabelActiveStatus": fsLabelActiveStatus,
       "fsLabelPowerStatus": fsLabelPowerStatus,
       "fsLabelWarningCancel": fsLabelWarningCancel,
       "fsLabelUnregStatus": fsLabelUnregStatus,
       "fsLabelStolenWarningStatus": fsLabelStolenWarningStatus,
       "fsRs485TrapIp": fsRs485TrapIp,
       "fsRs485HeartbeatStatus": fsRs485HeartbeatStatus,
       "fsClassPDUPower1": fsClassPDUPower1,
       "fsClassPDUPower2": fsClassPDUPower2,
       "fsClassDeviceAddType": fsClassDeviceAddType,
       "fsClassDeviceAddID": fsClassDeviceAddID,
       "fsClassDeviceAddStatus": fsClassDeviceAddStatus,
       "fsClassDeviceInfoTable": fsClassDeviceInfoTable,
       "fsClassDeviceInfoEntry": fsClassDeviceInfoEntry,
       "fsClassDeviceType": fsClassDeviceType,
       "fsClassDeviceID": fsClassDeviceID,
       "fsClassDeviceIconType": fsClassDeviceIconType,
       "fsClassDeviceName": fsClassDeviceName,
       "fsClassDeviceModelID": fsClassDeviceModelID,
       "fsClassDeviceControlSerial": fsClassDeviceControlSerial,
       "fsClassDeviceTeleControlPort": fsClassDeviceTeleControlPort,
       "fsClassDeviceIOType": fsClassDeviceIOType,
       "fsClassDeviceVideoPort": fsClassDeviceVideoPort,
       "fsClassDeviceAudioPort": fsClassDeviceAudioPort,
       "fsClassDeviceVideoUsedStatus": fsClassDeviceVideoUsedStatus,
       "fsClassDeviceAudioUsedStatus": fsClassDeviceAudioUsedStatus,
       "fsClassDeviceSwitch": fsClassDeviceSwitch,
       "fsClassDeviceState": fsClassDeviceState,
       "fsClassDeviceZigbeeID": fsClassDeviceZigbeeID,
       "fsClassDeviceSetStatus": fsClassDeviceSetStatus,
       "fsClassDeviceIP": fsClassDeviceIP,
       "fsClassBindDeviceID": fsClassBindDeviceID,
       "fsClassBatchSupport": fsClassBatchSupport,
       "fsClassAPPUsername": fsClassAPPUsername,
       "fsClassAPPPassword": fsClassAPPPassword,
       "fsClassAPPAuth": fsClassAPPAuth,
       "fsClassCMDDeviceModelID": fsClassCMDDeviceModelID,
       "fsClassCMDType": fsClassCMDType,
       "fsClassCommand": fsClassCommand,
       "fsClassCommandSetStatus": fsClassCommandSetStatus,
       "fsClassOperAll": fsClassOperAll,
       "fsClassCardID": fsClassCardID,
       "fsClassDateTime": fsClassDateTime,
       "fsClassAPPUpdateReq": fsClassAPPUpdateReq,
       "fsClassUpdateFileName": fsClassUpdateFileName,
       "fsClassUpdate": fsClassUpdate,
       "fsClassSoftVersion": fsClassSoftVersion,
       "fsClassChannel": fsClassChannel,
       "fsClassOldDeviceIP": fsClassOldDeviceIP,
       "fsClassCommunity": fsClassCommunity,
       "fsClassUpdateStatus": fsClassUpdateStatus,
       "fsClassScheduleTableName": fsClassScheduleTableName,
       "fsClassUpdateScheduleTable": fsClassUpdateScheduleTable,
       "fsClassScheduleTableUpdateStatus": fsClassScheduleTableUpdateStatus,
       "fsClassCheckTableName": fsClassCheckTableName,
       "fsClassReadCheckTable": fsClassReadCheckTable,
       "fsClassReadCheckTable1UploadStatus": fsClassReadCheckTable1UploadStatus,
       "fsClassLampTimeClass": fsClassLampTimeClass,
       "fsClassDeleteRecordTable": fsClassDeleteRecordTable,
       "fsClassSystemTime": fsClassSystemTime,
       "fsClassProjectorFact": fsClassProjectorFact,
       "fsClassProjectorModel": fsClassProjectorModel,
       "fsClassAIOFact": fsClassAIOFact,
       "fsClassAIOModel": fsClassAIOModel,
       "fsRs485MIBTrap": fsRs485MIBTrap,
       "fsRs485StateChange": fsRs485StateChange,
       "fsRs485Power1Change": fsRs485Power1Change,
       "fsRs485Power2Change": fsRs485Power2Change,
       "fsRs485Power3Change": fsRs485Power3Change,
       "fsRs485Power4Change": fsRs485Power4Change,
       "fsRs485TelnetFail": fsRs485TelnetFail,
       "fsLabelActiveACK": fsLabelActiveACK,
       "fsLabelLowPower": fsLabelLowPower,
       "fsLabelStolen": fsLabelStolen,
       "fsLabelUnregACK": fsLabelUnregACK,
       "fsRs485Heartbeat": fsRs485Heartbeat,
       "fsLabelRegACK": fsLabelRegACK,
       "fsClassAPPLoginREQ": fsClassAPPLoginREQ,
       "fsClassAPPOperation": fsClassAPPOperation,
       "fsClassTelecommand": fsClassTelecommand,
       "fsClassSwipeCard": fsClassSwipeCard,
       "fsClassUpdateReq": fsClassUpdateReq,
       "fsClassOperationAll": fsClassOperationAll,
       "fsClassChannelToServer": fsClassChannelToServer,
       "fsClassDevIPChange": fsClassDevIPChange,
       "fsClassCardOperationAll": fsClassCardOperationAll,
       "fsClassAccountOperationAll": fsClassAccountOperationAll,
       "fsClassTableRedo": fsClassTableRedo,
       "fsClassDeviceStateChange": fsClassDeviceStateChange}
)
