# SNMP MIB module (FS-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:12 2025
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

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10)
)
if mibBuilder.loadTexts:
    fsInterfaceMIB.setRevisions(
        ("2010-02-01 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIfConfigMIBObjects_ObjectIdentity = ObjectIdentity
fsIfConfigMIBObjects = _FsIfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1)
)
_FsIfTable_Object = MibTable
fsIfTable = _FsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    fsIfTable.setStatus("current")
_FsIfEntry_Object = MibTableRow
fsIfEntry = _FsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1)
)
fsIfEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfIndex"),
)
if mibBuilder.loadTexts:
    fsIfEntry.setStatus("current")
_FsIfIndex_Type = IfIndex
_FsIfIndex_Object = MibTableColumn
fsIfIndex = _FsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 1),
    _FsIfIndex_Type()
)
fsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIndex.setStatus("current")


class _FsIfPortType_Type(Integer32):
    """Custom type fsIfPortType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("port10M100MBASETX", 2),
          ("port100MBASEFXL", 3),
          ("port100MBASEFXS", 4),
          ("port1000MBASESX", 5),
          ("port1000MBASELX", 6),
          ("port1000MBASETX", 7),
          ("portGBIC", 8),
          ("port100MBASEFX", 9),
          ("port1000MBASEFX", 10),
          ("portSFP", 11),
          ("port10GBASESR", 12),
          ("port10GBASELR", 13),
          ("port10GBASEER", 14),
          ("port10GBASELX4", 15),
          ("port10GBASESW", 16),
          ("port10GBASELW", 17),
          ("port10GBASEEW", 18),
          ("port10GBASE", 19),
          ("port40GBASEKR", 20),
          ("port40GBASECR", 21),
          ("port40GBASELR", 22),
          ("port40GBASESR", 23),
          ("port40GBASE", 24),
          ("port100GBASECR", 25),
          ("port100GBASESR", 26),
          ("port100GBASELR", 27),
          ("port100GBASEER", 28),
          ("port100GBASE", 29),
          ("port155MCPOS", 50),
          ("port622MCPOS", 51),
          ("port2G5CPOS", 52),
          ("port10GCPOS", 53),
          ("port155MPOS", 54),
          ("port622MPOS", 55),
          ("port2G5POS", 56),
          ("port10GPOS", 57),
          ("port155MATM", 58),
          ("port622MATM", 59),
          ("port2G5ATM", 60),
          ("port10GATM", 61),
          ("portE1ELC", 62),
          ("port20GBASE", 63),
          ("port25GBASE", 64),
          ("port2500MBASE", 65),
          ("port5000MBASE", 66))
    )


_FsIfPortType_Type.__name__ = "Integer32"
_FsIfPortType_Object = MibTableColumn
fsIfPortType = _FsIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 2),
    _FsIfPortType_Type()
)
fsIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfPortType.setStatus("current")


class _FsIfFlowControlAdminStatus_Type(Integer32):
    """Custom type fsIfFlowControlAdminStatus based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("autonego", 3),
          ("unknown", 4))
    )


_FsIfFlowControlAdminStatus_Type.__name__ = "Integer32"
_FsIfFlowControlAdminStatus_Object = MibTableColumn
fsIfFlowControlAdminStatus = _FsIfFlowControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 3),
    _FsIfFlowControlAdminStatus_Type()
)
fsIfFlowControlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfFlowControlAdminStatus.setStatus("current")
_FsIfFlowControlOperStatus_Type = EnabledStatus
_FsIfFlowControlOperStatus_Object = MibTableColumn
fsIfFlowControlOperStatus = _FsIfFlowControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 4),
    _FsIfFlowControlOperStatus_Type()
)
fsIfFlowControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFlowControlOperStatus.setStatus("current")


class _FsIfAdminSpeed_Type(Integer32):
    """Custom type fsIfAdminSpeed based on Integer32"""
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
        *(("speed10Mb", 1),
          ("speed100Mb", 2),
          ("speed1000Mb", 3),
          ("autonego", 4),
          ("speed10Gb", 5),
          ("unknown", 6),
          ("speed40Gb", 7),
          ("speed100Gb", 8))
    )


_FsIfAdminSpeed_Type.__name__ = "Integer32"
_FsIfAdminSpeed_Object = MibTableColumn
fsIfAdminSpeed = _FsIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 5),
    _FsIfAdminSpeed_Type()
)
fsIfAdminSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfAdminSpeed.setStatus("current")


class _FsIfAdminDuplex_Type(Integer32):
    """Custom type fsIfAdminDuplex based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("autonego", 3),
          ("unknown", 4))
    )


_FsIfAdminDuplex_Type.__name__ = "Integer32"
_FsIfAdminDuplex_Object = MibTableColumn
fsIfAdminDuplex = _FsIfAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 6),
    _FsIfAdminDuplex_Type()
)
fsIfAdminDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfAdminDuplex.setStatus("current")


class _FsIfOperSpeed_Type(Integer32):
    """Custom type fsIfOperSpeed based on Integer32"""
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
        *(("speed10Mb", 1),
          ("speed100Mb", 2),
          ("speed1000Mb", 3),
          ("unknown", 4),
          ("speed10Gb", 5),
          ("speed40Gb", 6),
          ("speed100Gb", 7))
    )


_FsIfOperSpeed_Type.__name__ = "Integer32"
_FsIfOperSpeed_Object = MibTableColumn
fsIfOperSpeed = _FsIfOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 7),
    _FsIfOperSpeed_Type()
)
fsIfOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOperSpeed.setStatus("current")


class _FsIfOperDuplex_Type(Integer32):
    """Custom type fsIfOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("unknown", 3))
    )


_FsIfOperDuplex_Type.__name__ = "Integer32"
_FsIfOperDuplex_Object = MibTableColumn
fsIfOperDuplex = _FsIfOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 8),
    _FsIfOperDuplex_Type()
)
fsIfOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOperDuplex.setStatus("current")


class _FsIfManageStatus_Type(EnabledStatus):
    """Custom type fsIfManageStatus based on EnabledStatus"""
    defaultValue = 1


_FsIfManageStatus_Type.__name__ = "EnabledStatus"
_FsIfManageStatus_Object = MibTableColumn
fsIfManageStatus = _FsIfManageStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 9),
    _FsIfManageStatus_Type()
)
fsIfManageStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfManageStatus.setStatus("current")
_FsIfIpBroadcast_Type = IpAddress
_FsIfIpBroadcast_Object = MibTableColumn
fsIfIpBroadcast = _FsIfIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 10),
    _FsIfIpBroadcast_Type()
)
fsIfIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfIpBroadcast.setStatus("current")


class _FsIfLayer_Type(Integer32):
    """Custom type fsIfLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer-2", 1),
          ("layer-3", 2))
    )


_FsIfLayer_Type.__name__ = "Integer32"
_FsIfLayer_Object = MibTableColumn
fsIfLayer = _FsIfLayer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 11),
    _FsIfLayer_Type()
)
fsIfLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfLayer.setStatus("current")


class _FsIfMode_Type(Integer32):
    """Custom type fsIfMode based on Integer32"""
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
        *(("access", 1),
          ("trunk", 2),
          ("dot1q-tunnel", 3),
          ("hybrid", 4),
          ("other", 5),
          ("uplink", 6),
          ("host", 7),
          ("promiscuous", 8))
    )


_FsIfMode_Type.__name__ = "Integer32"
_FsIfMode_Object = MibTableColumn
fsIfMode = _FsIfMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 12),
    _FsIfMode_Type()
)
fsIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfMode.setStatus("current")
_FsIfCounterClear_Type = Integer32
_FsIfCounterClear_Object = MibTableColumn
fsIfCounterClear = _FsIfCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 13),
    _FsIfCounterClear_Type()
)
fsIfCounterClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfCounterClear.setStatus("current")
_FsIfEntryStatus_Type = ConfigStatus
_FsIfEntryStatus_Object = MibTableColumn
fsIfEntryStatus = _FsIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 14),
    _FsIfEntryStatus_Type()
)
fsIfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfEntryStatus.setStatus("current")


class _FsIfMediumType_Type(Integer32):
    """Custom type fsIfMediumType based on Integer32"""
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
          ("copper", 1),
          ("fiber", 2))
    )


_FsIfMediumType_Type.__name__ = "Integer32"
_FsIfMediumType_Object = MibTableColumn
fsIfMediumType = _FsIfMediumType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 15),
    _FsIfMediumType_Type()
)
fsIfMediumType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfMediumType.setStatus("current")
_FsIfDownCounter_Type = Counter32
_FsIfDownCounter_Object = MibTableColumn
fsIfDownCounter = _FsIfDownCounter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 16),
    _FsIfDownCounter_Type()
)
fsIfDownCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownCounter.setStatus("current")
_FsIfInOctets_Type = Counter64
_FsIfInOctets_Object = MibTableColumn
fsIfInOctets = _FsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 17),
    _FsIfInOctets_Type()
)
fsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInOctets.setStatus("current")
_FsIfOutOctets_Type = Counter64
_FsIfOutOctets_Object = MibTableColumn
fsIfOutOctets = _FsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 18),
    _FsIfOutOctets_Type()
)
fsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutOctets.setStatus("current")
_FsIfBcastInhibit_Type = Integer32
_FsIfBcastInhibit_Object = MibTableColumn
fsIfBcastInhibit = _FsIfBcastInhibit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 19),
    _FsIfBcastInhibit_Type()
)
fsIfBcastInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfBcastInhibit.setStatus("current")


class _FsIfNegotiation_Type(Integer32):
    """Custom type fsIfNegotiation based on Integer32"""
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


_FsIfNegotiation_Type.__name__ = "Integer32"
_FsIfNegotiation_Object = MibTableColumn
fsIfNegotiation = _FsIfNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 20),
    _FsIfNegotiation_Type()
)
fsIfNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfNegotiation.setStatus("current")
_FsIfPhysAddress_Type = MacAddress
_FsIfPhysAddress_Object = MibTableColumn
fsIfPhysAddress = _FsIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 21),
    _FsIfPhysAddress_Type()
)
fsIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfPhysAddress.setStatus("current")


class _FsIfAdminSpeedRW_Type(Integer32):
    """Custom type fsIfAdminSpeedRW based on Integer32"""
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
        *(("speed10Mb", 1),
          ("speed100Mb", 2),
          ("speed1000Mb", 3),
          ("autonego", 4),
          ("speed10Gb", 5),
          ("unknown", 6),
          ("speed40Gb", 7),
          ("speed100Gb", 8))
    )


_FsIfAdminSpeedRW_Type.__name__ = "Integer32"
_FsIfAdminSpeedRW_Object = MibTableColumn
fsIfAdminSpeedRW = _FsIfAdminSpeedRW_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 22),
    _FsIfAdminSpeedRW_Type()
)
fsIfAdminSpeedRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfAdminSpeedRW.setStatus("current")


class _FsIfAdminDuplexRW_Type(Integer32):
    """Custom type fsIfAdminDuplexRW based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("autonego", 3),
          ("unknown", 4))
    )


_FsIfAdminDuplexRW_Type.__name__ = "Integer32"
_FsIfAdminDuplexRW_Object = MibTableColumn
fsIfAdminDuplexRW = _FsIfAdminDuplexRW_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 23),
    _FsIfAdminDuplexRW_Type()
)
fsIfAdminDuplexRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfAdminDuplexRW.setStatus("current")


class _FsIfModeRW_Type(Integer32):
    """Custom type fsIfModeRW based on Integer32"""
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
        *(("access", 1),
          ("trunk", 2),
          ("dot1q-tunnel", 3),
          ("hybrid", 4),
          ("other", 5),
          ("uplink", 6),
          ("host", 7),
          ("promiscuous", 8))
    )


_FsIfModeRW_Type.__name__ = "Integer32"
_FsIfModeRW_Object = MibTableColumn
fsIfModeRW = _FsIfModeRW_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 24),
    _FsIfModeRW_Type()
)
fsIfModeRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfModeRW.setStatus("current")
_FsIfSpeed_Type = Gauge32
_FsIfSpeed_Object = MibTableColumn
fsIfSpeed = _FsIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 25),
    _FsIfSpeed_Type()
)
fsIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfSpeed.setStatus("current")


class _FsifAdminStatus_Type(Integer32):
    """Custom type fsifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminup", 1),
          ("admindown", 2),
          ("admintest", 3))
    )


_FsifAdminStatus_Type.__name__ = "Integer32"
_FsifAdminStatus_Object = MibTableColumn
fsifAdminStatus = _FsifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 26),
    _FsifAdminStatus_Type()
)
fsifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsifAdminStatus.setStatus("current")


class _FsifOperStatus_Type(Integer32):
    """Custom type fsifOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("test", 3),
          ("unknow", 4),
          ("dormant", 5))
    )


_FsifOperStatus_Type.__name__ = "Integer32"
_FsifOperStatus_Object = MibTableColumn
fsifOperStatus = _FsifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 27),
    _FsifOperStatus_Type()
)
fsifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsifOperStatus.setStatus("current")
_FsIfInNUcastPkts_Type = Counter64
_FsIfInNUcastPkts_Object = MibTableColumn
fsIfInNUcastPkts = _FsIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 28),
    _FsIfInNUcastPkts_Type()
)
fsIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInNUcastPkts.setStatus("current")
_FsIfOutNUcastPkts_Type = Counter64
_FsIfOutNUcastPkts_Object = MibTableColumn
fsIfOutNUcastPkts = _FsIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 29),
    _FsIfOutNUcastPkts_Type()
)
fsIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutNUcastPkts.setStatus("current")
_FsIfUpDownTimes_Type = Counter32
_FsIfUpDownTimes_Object = MibTableColumn
fsIfUpDownTimes = _FsIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 30),
    _FsIfUpDownTimes_Type()
)
fsIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUpDownTimes.setStatus("current")


class _FsifAdminStatusw_Type(Integer32):
    """Custom type fsifAdminStatusw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("admindown", 1))
    )


_FsifAdminStatusw_Type.__name__ = "Integer32"
_FsifAdminStatusw_Object = MibTableColumn
fsifAdminStatusw = _FsifAdminStatusw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 31),
    _FsifAdminStatusw_Type()
)
fsifAdminStatusw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsifAdminStatusw.setStatus("current")


class _FsifOperStatusw_Type(Integer32):
    """Custom type fsifOperStatusw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("admindown", 2))
    )


_FsifOperStatusw_Type.__name__ = "Integer32"
_FsifOperStatusw_Object = MibTableColumn
fsifOperStatusw = _FsifOperStatusw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 32),
    _FsifOperStatusw_Type()
)
fsifOperStatusw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsifOperStatusw.setStatus("current")
_FsifSpeedw_Type = Integer32
_FsifSpeedw_Object = MibTableColumn
fsifSpeedw = _FsifSpeedw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 33),
    _FsifSpeedw_Type()
)
fsifSpeedw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsifSpeedw.setStatus("current")
_FsifMacAddress_Type = MacAddress
_FsifMacAddress_Object = MibTableColumn
fsifMacAddress = _FsifMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 34),
    _FsifMacAddress_Type()
)
fsifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsifMacAddress.setStatus("current")
_FsifLastChange_Type = TimeTicks
_FsifLastChange_Object = MibTableColumn
fsifLastChange = _FsifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 35),
    _FsifLastChange_Type()
)
fsifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsifLastChange.setStatus("current")
_FsIfInPkts_Type = Counter64
_FsIfInPkts_Object = MibTableColumn
fsIfInPkts = _FsIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 36),
    _FsIfInPkts_Type()
)
fsIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInPkts.setStatus("current")
_FsIfDiscard_Type = Counter64
_FsIfDiscard_Object = MibTableColumn
fsIfDiscard = _FsIfDiscard_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 37),
    _FsIfDiscard_Type()
)
fsIfDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDiscard.setStatus("current")
_FsIfBandwidthUsage_Type = DisplayString
_FsIfBandwidthUsage_Object = MibTableColumn
fsIfBandwidthUsage = _FsIfBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 38),
    _FsIfBandwidthUsage_Type()
)
fsIfBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfBandwidthUsage.setStatus("current")
_FsIfInBitsRate_Type = Counter64
_FsIfInBitsRate_Object = MibTableColumn
fsIfInBitsRate = _FsIfInBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 39),
    _FsIfInBitsRate_Type()
)
fsIfInBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInBitsRate.setStatus("current")
_FsIfInPktRate_Type = Counter64
_FsIfInPktRate_Object = MibTableColumn
fsIfInPktRate = _FsIfInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 40),
    _FsIfInPktRate_Type()
)
fsIfInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInPktRate.setStatus("current")
_FsIfOutBitsRate_Type = Counter64
_FsIfOutBitsRate_Object = MibTableColumn
fsIfOutBitsRate = _FsIfOutBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 41),
    _FsIfOutBitsRate_Type()
)
fsIfOutBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutBitsRate.setStatus("current")
_FsIfOutPktRate_Type = Counter64
_FsIfOutPktRate_Object = MibTableColumn
fsIfOutPktRate = _FsIfOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 42),
    _FsIfOutPktRate_Type()
)
fsIfOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutPktRate.setStatus("current")
_FsIfInBandwidthUsage_Type = DisplayString
_FsIfInBandwidthUsage_Object = MibTableColumn
fsIfInBandwidthUsage = _FsIfInBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 43),
    _FsIfInBandwidthUsage_Type()
)
fsIfInBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInBandwidthUsage.setStatus("current")
_FsIfOutBandwidthUsage_Type = DisplayString
_FsIfOutBandwidthUsage_Object = MibTableColumn
fsIfOutBandwidthUsage = _FsIfOutBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 44),
    _FsIfOutBandwidthUsage_Type()
)
fsIfOutBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutBandwidthUsage.setStatus("current")
_FsIfInErrorPktsRate_Type = DisplayString
_FsIfInErrorPktsRate_Object = MibTableColumn
fsIfInErrorPktsRate = _FsIfInErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 45),
    _FsIfInErrorPktsRate_Type()
)
fsIfInErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInErrorPktsRate.setStatus("current")
_FsIfOutErrorPktsRate_Type = DisplayString
_FsIfOutErrorPktsRate_Object = MibTableColumn
fsIfOutErrorPktsRate = _FsIfOutErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 46),
    _FsIfOutErrorPktsRate_Type()
)
fsIfOutErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutErrorPktsRate.setStatus("current")
_FsIfInDropPktsRate_Type = DisplayString
_FsIfInDropPktsRate_Object = MibTableColumn
fsIfInDropPktsRate = _FsIfInDropPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 47),
    _FsIfInDropPktsRate_Type()
)
fsIfInDropPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInDropPktsRate.setStatus("current")
_FsIfOutDropPktsRate_Type = DisplayString
_FsIfOutDropPktsRate_Object = MibTableColumn
fsIfOutDropPktsRate = _FsIfOutDropPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 48),
    _FsIfOutDropPktsRate_Type()
)
fsIfOutDropPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutDropPktsRate.setStatus("current")
_FsIfOutNoBuffer_Type = Counter64
_FsIfOutNoBuffer_Object = MibTableColumn
fsIfOutNoBuffer = _FsIfOutNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 49),
    _FsIfOutNoBuffer_Type()
)
fsIfOutNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutNoBuffer.setStatus("current")
_FsIfOutPkts_Type = Counter64
_FsIfOutPkts_Object = MibTableColumn
fsIfOutPkts = _FsIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 1, 1, 50),
    _FsIfOutPkts_Type()
)
fsIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutPkts.setStatus("current")
_FsIfIpTable_Object = MibTable
fsIfIpTable = _FsIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    fsIfIpTable.setStatus("current")
_FsIfIpEntry_Object = MibTableRow
fsIfIpEntry = _FsIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2, 1)
)
fsIfIpEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfIpIfIndex"),
    (0, "FS-INTERFACE-MIB", "fsIfIpId"),
    (0, "FS-INTERFACE-MIB", "fsIfIp"),
)
if mibBuilder.loadTexts:
    fsIfIpEntry.setStatus("current")
_FsIfIpIfIndex_Type = IfIndex
_FsIfIpIfIndex_Object = MibTableColumn
fsIfIpIfIndex = _FsIfIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2, 1, 1),
    _FsIfIpIfIndex_Type()
)
fsIfIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIpIfIndex.setStatus("current")


class _FsIfIpId_Type(Integer32):
    """Custom type fsIfIpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_FsIfIpId_Type.__name__ = "Integer32"
_FsIfIpId_Object = MibTableColumn
fsIfIpId = _FsIfIpId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2, 1, 2),
    _FsIfIpId_Type()
)
fsIfIpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIpId.setStatus("current")
_FsIfIp_Type = IpAddress
_FsIfIp_Object = MibTableColumn
fsIfIp = _FsIfIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2, 1, 3),
    _FsIfIp_Type()
)
fsIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIp.setStatus("current")
_FsIfIpMask_Type = IpAddress
_FsIfIpMask_Object = MibTableColumn
fsIfIpMask = _FsIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2, 1, 4),
    _FsIfIpMask_Type()
)
fsIfIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfIpMask.setStatus("current")
_FsIfIpEntryStatus_Type = RowStatus
_FsIfIpEntryStatus_Object = MibTableColumn
fsIfIpEntryStatus = _FsIfIpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 2, 1, 5),
    _FsIfIpEntryStatus_Type()
)
fsIfIpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIfIpEntryStatus.setStatus("current")
_FsIfStatusTable_Object = MibTable
fsIfStatusTable = _FsIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    fsIfStatusTable.setStatus("current")
_FsIfStatusEntry_Object = MibTableRow
fsIfStatusEntry = _FsIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 3, 1)
)
fsIfStatusEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfStatusIndex"),
)
if mibBuilder.loadTexts:
    fsIfStatusEntry.setStatus("current")
_FsIfStatusIndex_Type = IfIndex
_FsIfStatusIndex_Object = MibTableColumn
fsIfStatusIndex = _FsIfStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 3, 1, 1),
    _FsIfStatusIndex_Type()
)
fsIfStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfStatusIndex.setStatus("current")
_FsIfStatusLoopBackExamine_Type = Integer32
_FsIfStatusLoopBackExamine_Object = MibTableColumn
fsIfStatusLoopBackExamine = _FsIfStatusLoopBackExamine_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 3, 1, 2),
    _FsIfStatusLoopBackExamine_Type()
)
fsIfStatusLoopBackExamine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfStatusLoopBackExamine.setStatus("current")


class _FsIfErrorStatus_Type(Integer32):
    """Custom type fsIfErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 1),
          ("err-disable-bpduguard", 2),
          ("err-disable-ptsecurity", 3))
    )


_FsIfErrorStatus_Type.__name__ = "Integer32"
_FsIfErrorStatus_Object = MibTableColumn
fsIfErrorStatus = _FsIfErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 3, 1, 3),
    _FsIfErrorStatus_Type()
)
fsIfErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfErrorStatus.setStatus("current")
_FsIfLineDetect_Type = Integer32
_FsIfLineDetect_Object = MibTableColumn
fsIfLineDetect = _FsIfLineDetect_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 3, 1, 4),
    _FsIfLineDetect_Type()
)
fsIfLineDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLineDetect.setStatus("current")
_FsGlobalIfDisableRecovery_Type = Integer32
_FsGlobalIfDisableRecovery_Object = MibScalar
fsGlobalIfDisableRecovery = _FsGlobalIfDisableRecovery_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 4),
    _FsGlobalIfDisableRecovery_Type()
)
fsGlobalIfDisableRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalIfDisableRecovery.setStatus("current")
_FsPortTypeChooseTable_Object = MibTable
fsPortTypeChooseTable = _FsPortTypeChooseTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 5)
)
if mibBuilder.loadTexts:
    fsPortTypeChooseTable.setStatus("current")
_FsPortTypeChooseEntry_Object = MibTableRow
fsPortTypeChooseEntry = _FsPortTypeChooseEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 5, 1)
)
fsPortTypeChooseEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsPortTypeChooseIndex"),
)
if mibBuilder.loadTexts:
    fsPortTypeChooseEntry.setStatus("current")
_FsPortTypeChooseIndex_Type = IfIndex
_FsPortTypeChooseIndex_Object = MibTableColumn
fsPortTypeChooseIndex = _FsPortTypeChooseIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 5, 1, 1),
    _FsPortTypeChooseIndex_Type()
)
fsPortTypeChooseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPortTypeChooseIndex.setStatus("current")


class _FsPortTypeChooseType_Type(Integer32):
    """Custom type fsPortTypeChooseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("copper", 2))
    )


_FsPortTypeChooseType_Type.__name__ = "Integer32"
_FsPortTypeChooseType_Object = MibTableColumn
fsPortTypeChooseType = _FsPortTypeChooseType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 5, 1, 2),
    _FsPortTypeChooseType_Type()
)
fsPortTypeChooseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPortTypeChooseType.setStatus("current")
_FsIfMTUTable_Object = MibTable
fsIfMTUTable = _FsIfMTUTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 6)
)
if mibBuilder.loadTexts:
    fsIfMTUTable.setStatus("current")
_FsIfMTUEntry_Object = MibTableRow
fsIfMTUEntry = _FsIfMTUEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 6, 1)
)
fsIfMTUEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfMTUIndex"),
)
if mibBuilder.loadTexts:
    fsIfMTUEntry.setStatus("current")
_FsIfMTUIndex_Type = IfIndex
_FsIfMTUIndex_Object = MibTableColumn
fsIfMTUIndex = _FsIfMTUIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 6, 1, 1),
    _FsIfMTUIndex_Type()
)
fsIfMTUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfMTUIndex.setStatus("current")
_FsIfMTU_Type = Integer32
_FsIfMTU_Object = MibTableColumn
fsIfMTU = _FsIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 6, 1, 2),
    _FsIfMTU_Type()
)
fsIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfMTU.setStatus("current")
_FsIfAvailableBWTable_Object = MibTable
fsIfAvailableBWTable = _FsIfAvailableBWTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 7)
)
if mibBuilder.loadTexts:
    fsIfAvailableBWTable.setStatus("current")
_FsIfAvailableBWEntry_Object = MibTableRow
fsIfAvailableBWEntry = _FsIfAvailableBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 7, 1)
)
fsIfAvailableBWEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfAvailableBWIfIndex"),
)
if mibBuilder.loadTexts:
    fsIfAvailableBWEntry.setStatus("current")
_FsIfAvailableBWIfIndex_Type = IfIndex
_FsIfAvailableBWIfIndex_Object = MibTableColumn
fsIfAvailableBWIfIndex = _FsIfAvailableBWIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 7, 1, 1),
    _FsIfAvailableBWIfIndex_Type()
)
fsIfAvailableBWIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfAvailableBWIfIndex.setStatus("current")
_FsIfAvailableBWIfBW_Type = Gauge32
_FsIfAvailableBWIfBW_Object = MibTableColumn
fsIfAvailableBWIfBW = _FsIfAvailableBWIfBW_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 7, 1, 2),
    _FsIfAvailableBWIfBW_Type()
)
fsIfAvailableBWIfBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfAvailableBWIfBW.setStatus("current")
_FsIfSVICreatTable_Object = MibTable
fsIfSVICreatTable = _FsIfSVICreatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 8)
)
if mibBuilder.loadTexts:
    fsIfSVICreatTable.setStatus("current")
_FsIfSVICreatEntry_Object = MibTableRow
fsIfSVICreatEntry = _FsIfSVICreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 8, 1)
)
fsIfSVICreatEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfSVICreatVlanNum"),
)
if mibBuilder.loadTexts:
    fsIfSVICreatEntry.setStatus("current")


class _FsIfSVICreatVlanNum_Type(Integer32):
    """Custom type fsIfSVICreatVlanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIfSVICreatVlanNum_Type.__name__ = "Integer32"
_FsIfSVICreatVlanNum_Object = MibTableColumn
fsIfSVICreatVlanNum = _FsIfSVICreatVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 8, 1, 1),
    _FsIfSVICreatVlanNum_Type()
)
fsIfSVICreatVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfSVICreatVlanNum.setStatus("current")


class _FsIfHandleSVI_Type(Integer32):
    """Custom type fsIfHandleSVI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("create", 0),
          ("delete", 1))
    )


_FsIfHandleSVI_Type.__name__ = "Integer32"
_FsIfHandleSVI_Object = MibTableColumn
fsIfHandleSVI = _FsIfHandleSVI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 8, 1, 2),
    _FsIfHandleSVI_Type()
)
fsIfHandleSVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfHandleSVI.setStatus("current")
_FsIfPhyIntNum_Type = Integer32
_FsIfPhyIntNum_Object = MibScalar
fsIfPhyIntNum = _FsIfPhyIntNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 9),
    _FsIfPhyIntNum_Type()
)
fsIfPhyIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfPhyIntNum.setStatus("current")
_FsIfLinkUPTimesTable_Object = MibTable
fsIfLinkUPTimesTable = _FsIfLinkUPTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 10)
)
if mibBuilder.loadTexts:
    fsIfLinkUPTimesTable.setStatus("current")
_FsIfLinkUPTimesEntry_Object = MibTableRow
fsIfLinkUPTimesEntry = _FsIfLinkUPTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 10, 1)
)
fsIfLinkUPTimesEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    fsIfLinkUPTimesEntry.setStatus("current")
_FsInterfaceIndex_Type = Integer32
_FsInterfaceIndex_Object = MibTableColumn
fsInterfaceIndex = _FsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 10, 1, 1),
    _FsInterfaceIndex_Type()
)
fsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsInterfaceIndex.setStatus("current")
_FsIfLinkUPTimes_Type = Integer32
_FsIfLinkUPTimes_Object = MibTableColumn
fsIfLinkUPTimes = _FsIfLinkUPTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 10, 1, 2),
    _FsIfLinkUPTimes_Type()
)
fsIfLinkUPTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkUPTimes.setStatus("current")
_FsIfEncapsulationTable_Object = MibTable
fsIfEncapsulationTable = _FsIfEncapsulationTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 11)
)
if mibBuilder.loadTexts:
    fsIfEncapsulationTable.setStatus("current")
_FsIfEncapsulationEntry_Object = MibTableRow
fsIfEncapsulationEntry = _FsIfEncapsulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 11, 1)
)
fsIfEncapsulationEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfEncapsulationIndex"),
)
if mibBuilder.loadTexts:
    fsIfEncapsulationEntry.setStatus("current")
_FsIfEncapsulationIndex_Type = IfIndex
_FsIfEncapsulationIndex_Object = MibTableColumn
fsIfEncapsulationIndex = _FsIfEncapsulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 11, 1, 1),
    _FsIfEncapsulationIndex_Type()
)
fsIfEncapsulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfEncapsulationIndex.setStatus("current")
_FsIfEncapsulationVlan_Type = VlanId
_FsIfEncapsulationVlan_Object = MibTableColumn
fsIfEncapsulationVlan = _FsIfEncapsulationVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 11, 1, 2),
    _FsIfEncapsulationVlan_Type()
)
fsIfEncapsulationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfEncapsulationVlan.setStatus("current")
_FsApIfNumberTable_Object = MibTable
fsApIfNumberTable = _FsApIfNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 12)
)
if mibBuilder.loadTexts:
    fsApIfNumberTable.setStatus("current")
_FsApIfNumberEntry_Object = MibTableRow
fsApIfNumberEntry = _FsApIfNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 12, 1)
)
fsApIfNumberEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsApPhyAddress"),
)
if mibBuilder.loadTexts:
    fsApIfNumberEntry.setStatus("current")
_FsApPhyAddress_Type = PhysAddress
_FsApPhyAddress_Object = MibTableColumn
fsApPhyAddress = _FsApPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 12, 1, 1),
    _FsApPhyAddress_Type()
)
fsApPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApPhyAddress.setStatus("current")
_FsApIfNumber_Type = Integer32
_FsApIfNumber_Object = MibTableColumn
fsApIfNumber = _FsApIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 12, 1, 2),
    _FsApIfNumber_Type()
)
fsApIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfNumber.setStatus("current")
_FsApIfPhyIntNum_Type = Integer32
_FsApIfPhyIntNum_Object = MibTableColumn
fsApIfPhyIntNum = _FsApIfPhyIntNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 12, 1, 3),
    _FsApIfPhyIntNum_Type()
)
fsApIfPhyIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfPhyIntNum.setStatus("current")
_FsApIfTable_Object = MibTable
fsApIfTable = _FsApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13)
)
if mibBuilder.loadTexts:
    fsApIfTable.setStatus("current")
_FsApIfEntry_Object = MibTableRow
fsApIfEntry = _FsApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1)
)
fsApIfEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsApPhysAddress"),
    (0, "FS-INTERFACE-MIB", "fsApIfIndex"),
)
if mibBuilder.loadTexts:
    fsApIfEntry.setStatus("current")
_FsApPhysAddress_Type = PhysAddress
_FsApPhysAddress_Object = MibTableColumn
fsApPhysAddress = _FsApPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 1),
    _FsApPhysAddress_Type()
)
fsApPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApPhysAddress.setStatus("current")
_FsApIfIndex_Type = IfIndex
_FsApIfIndex_Object = MibTableColumn
fsApIfIndex = _FsApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 2),
    _FsApIfIndex_Type()
)
fsApIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfIndex.setStatus("current")


class _FsApIfDescr_Type(DisplayString):
    """Custom type fsApIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsApIfDescr_Type.__name__ = "DisplayString"
_FsApIfDescr_Object = MibTableColumn
fsApIfDescr = _FsApIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 3),
    _FsApIfDescr_Type()
)
fsApIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfDescr.setStatus("current")
_FsApIfType_Type = IANAifType
_FsApIfType_Object = MibTableColumn
fsApIfType = _FsApIfType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 4),
    _FsApIfType_Type()
)
fsApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfType.setStatus("current")
_FsApIfMtu_Type = Integer32
_FsApIfMtu_Object = MibTableColumn
fsApIfMtu = _FsApIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 5),
    _FsApIfMtu_Type()
)
fsApIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfMtu.setStatus("current")
_FsApIfSpeed_Type = Gauge32
_FsApIfSpeed_Object = MibTableColumn
fsApIfSpeed = _FsApIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 6),
    _FsApIfSpeed_Type()
)
fsApIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfSpeed.setStatus("current")
_FsApIfPhysAddress_Type = PhysAddress
_FsApIfPhysAddress_Object = MibTableColumn
fsApIfPhysAddress = _FsApIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 7),
    _FsApIfPhysAddress_Type()
)
fsApIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfPhysAddress.setStatus("current")


class _FsApIfAdminStatus_Type(Integer32):
    """Custom type fsApIfAdminStatus based on Integer32"""
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
          ("admindown", 2),
          ("testing", 3))
    )


_FsApIfAdminStatus_Type.__name__ = "Integer32"
_FsApIfAdminStatus_Object = MibTableColumn
fsApIfAdminStatus = _FsApIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 8),
    _FsApIfAdminStatus_Type()
)
fsApIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApIfAdminStatus.setStatus("current")


class _FsApIfOperStatus_Type(Integer32):
    """Custom type fsApIfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("admindown", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_FsApIfOperStatus_Type.__name__ = "Integer32"
_FsApIfOperStatus_Object = MibTableColumn
fsApIfOperStatus = _FsApIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 9),
    _FsApIfOperStatus_Type()
)
fsApIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOperStatus.setStatus("current")
_FsApIfLastChange_Type = TimeTicks
_FsApIfLastChange_Object = MibTableColumn
fsApIfLastChange = _FsApIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 10),
    _FsApIfLastChange_Type()
)
fsApIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfLastChange.setStatus("current")
_FsApIfInOctets_Type = Counter64
_FsApIfInOctets_Object = MibTableColumn
fsApIfInOctets = _FsApIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 11),
    _FsApIfInOctets_Type()
)
fsApIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInOctets.setStatus("current")
_FsApIfInUcastPkts_Type = Counter64
_FsApIfInUcastPkts_Object = MibTableColumn
fsApIfInUcastPkts = _FsApIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 12),
    _FsApIfInUcastPkts_Type()
)
fsApIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInUcastPkts.setStatus("current")
_FsApIfInNUcastPkts_Type = Counter64
_FsApIfInNUcastPkts_Object = MibTableColumn
fsApIfInNUcastPkts = _FsApIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 13),
    _FsApIfInNUcastPkts_Type()
)
fsApIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInNUcastPkts.setStatus("deprecated")
_FsApIfInDiscards_Type = Counter32
_FsApIfInDiscards_Object = MibTableColumn
fsApIfInDiscards = _FsApIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 14),
    _FsApIfInDiscards_Type()
)
fsApIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInDiscards.setStatus("current")
_FsApIfInErrors_Type = Counter32
_FsApIfInErrors_Object = MibTableColumn
fsApIfInErrors = _FsApIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 15),
    _FsApIfInErrors_Type()
)
fsApIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInErrors.setStatus("current")
_FsApIfInUnknownProtos_Type = Counter32
_FsApIfInUnknownProtos_Object = MibTableColumn
fsApIfInUnknownProtos = _FsApIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 16),
    _FsApIfInUnknownProtos_Type()
)
fsApIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInUnknownProtos.setStatus("current")
_FsApIfOutOctets_Type = Counter64
_FsApIfOutOctets_Object = MibTableColumn
fsApIfOutOctets = _FsApIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 17),
    _FsApIfOutOctets_Type()
)
fsApIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutOctets.setStatus("current")
_FsApIfOutUcastPkts_Type = Counter64
_FsApIfOutUcastPkts_Object = MibTableColumn
fsApIfOutUcastPkts = _FsApIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 18),
    _FsApIfOutUcastPkts_Type()
)
fsApIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutUcastPkts.setStatus("current")
_FsApIfOutNUcastPkts_Type = Counter64
_FsApIfOutNUcastPkts_Object = MibTableColumn
fsApIfOutNUcastPkts = _FsApIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 19),
    _FsApIfOutNUcastPkts_Type()
)
fsApIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutNUcastPkts.setStatus("deprecated")
_FsApIfOutDiscards_Type = Counter32
_FsApIfOutDiscards_Object = MibTableColumn
fsApIfOutDiscards = _FsApIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 20),
    _FsApIfOutDiscards_Type()
)
fsApIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutDiscards.setStatus("current")
_FsApIfOutErrors_Type = Counter32
_FsApIfOutErrors_Object = MibTableColumn
fsApIfOutErrors = _FsApIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 21),
    _FsApIfOutErrors_Type()
)
fsApIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutErrors.setStatus("current")
_FsApIfOutQLen_Type = Gauge32
_FsApIfOutQLen_Object = MibTableColumn
fsApIfOutQLen = _FsApIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 22),
    _FsApIfOutQLen_Type()
)
fsApIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutQLen.setStatus("deprecated")
_FsApIfLinkUPTimes_Type = Integer32
_FsApIfLinkUPTimes_Object = MibTableColumn
fsApIfLinkUPTimes = _FsApIfLinkUPTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 23),
    _FsApIfLinkUPTimes_Type()
)
fsApIfLinkUPTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfLinkUPTimes.setStatus("current")
_FsApIfInDataOctets_Type = Counter64
_FsApIfInDataOctets_Object = MibTableColumn
fsApIfInDataOctets = _FsApIfInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 24),
    _FsApIfInDataOctets_Type()
)
fsApIfInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInDataOctets.setStatus("current")
_FsApIfOutDataOctets_Type = Counter64
_FsApIfOutDataOctets_Object = MibTableColumn
fsApIfOutDataOctets = _FsApIfOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 25),
    _FsApIfOutDataOctets_Type()
)
fsApIfOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutDataOctets.setStatus("current")
_FsApIfMgmtUploadOctets_Type = Counter32
_FsApIfMgmtUploadOctets_Object = MibTableColumn
fsApIfMgmtUploadOctets = _FsApIfMgmtUploadOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 26),
    _FsApIfMgmtUploadOctets_Type()
)
fsApIfMgmtUploadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfMgmtUploadOctets.setStatus("current")
_FsApIfMgmtDownloadOctets_Type = Counter32
_FsApIfMgmtDownloadOctets_Object = MibTableColumn
fsApIfMgmtDownloadOctets = _FsApIfMgmtDownloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 27),
    _FsApIfMgmtDownloadOctets_Type()
)
fsApIfMgmtDownloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfMgmtDownloadOctets.setStatus("current")
_FsApIfSpeedw_Type = Integer32
_FsApIfSpeedw_Object = MibTableColumn
fsApIfSpeedw = _FsApIfSpeedw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 28),
    _FsApIfSpeedw_Type()
)
fsApIfSpeedw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfSpeedw.setStatus("current")
_FsApIfMtuw_Type = Integer32
_FsApIfMtuw_Object = MibTableColumn
fsApIfMtuw = _FsApIfMtuw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 29),
    _FsApIfMtuw_Type()
)
fsApIfMtuw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfMtuw.setStatus("current")
_FsApIfPhysAddressw_Type = MacAddress
_FsApIfPhysAddressw_Object = MibTableColumn
fsApIfPhysAddressw = _FsApIfPhysAddressw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 30),
    _FsApIfPhysAddressw_Type()
)
fsApIfPhysAddressw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfPhysAddressw.setStatus("current")
_FsApIfInUcastPktsw_Type = Counter32
_FsApIfInUcastPktsw_Object = MibTableColumn
fsApIfInUcastPktsw = _FsApIfInUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 31),
    _FsApIfInUcastPktsw_Type()
)
fsApIfInUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInUcastPktsw.setStatus("current")
_FsApIfInNUcastPktsw_Type = Counter32
_FsApIfInNUcastPktsw_Object = MibTableColumn
fsApIfInNUcastPktsw = _FsApIfInNUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 32),
    _FsApIfInNUcastPktsw_Type()
)
fsApIfInNUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInNUcastPktsw.setStatus("deprecated")
_FsApIfOutUcastPktsw_Type = Counter32
_FsApIfOutUcastPktsw_Object = MibTableColumn
fsApIfOutUcastPktsw = _FsApIfOutUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 33),
    _FsApIfOutUcastPktsw_Type()
)
fsApIfOutUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutUcastPktsw.setStatus("current")
_FsApIfOutNUcastPktsw_Type = Counter32
_FsApIfOutNUcastPktsw_Object = MibTableColumn
fsApIfOutNUcastPktsw = _FsApIfOutNUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 34),
    _FsApIfOutNUcastPktsw_Type()
)
fsApIfOutNUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutNUcastPktsw.setStatus("deprecated")
_FsApIfLinkUPTimesw_Type = Counter32
_FsApIfLinkUPTimesw_Object = MibTableColumn
fsApIfLinkUPTimesw = _FsApIfLinkUPTimesw_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 35),
    _FsApIfLinkUPTimesw_Type()
)
fsApIfLinkUPTimesw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfLinkUPTimesw.setStatus("current")
_FsApIfInPkts_Type = Counter64
_FsApIfInPkts_Object = MibTableColumn
fsApIfInPkts = _FsApIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 36),
    _FsApIfInPkts_Type()
)
fsApIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInPkts.setStatus("current")
_FsApIfInFlow_Type = Counter32
_FsApIfInFlow_Object = MibTableColumn
fsApIfInFlow = _FsApIfInFlow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 37),
    _FsApIfInFlow_Type()
)
fsApIfInFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInFlow.setStatus("current")
_FsApIfOutFlow_Type = Counter32
_FsApIfOutFlow_Object = MibTableColumn
fsApIfOutFlow = _FsApIfOutFlow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 38),
    _FsApIfOutFlow_Type()
)
fsApIfOutFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutFlow.setStatus("current")
_FsApIfInBrdcastPkts_Type = Counter64
_FsApIfInBrdcastPkts_Object = MibTableColumn
fsApIfInBrdcastPkts = _FsApIfInBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 39),
    _FsApIfInBrdcastPkts_Type()
)
fsApIfInBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInBrdcastPkts.setStatus("current")
_FsApIfOutBrdcastPkts_Type = Counter64
_FsApIfOutBrdcastPkts_Object = MibTableColumn
fsApIfOutBrdcastPkts = _FsApIfOutBrdcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 40),
    _FsApIfOutBrdcastPkts_Type()
)
fsApIfOutBrdcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutBrdcastPkts.setStatus("current")
_FsApIfInMulcastPkts_Type = Counter64
_FsApIfInMulcastPkts_Object = MibTableColumn
fsApIfInMulcastPkts = _FsApIfInMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 41),
    _FsApIfInMulcastPkts_Type()
)
fsApIfInMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInMulcastPkts.setStatus("current")
_FsApIfOutMulcastPkts_Type = Counter64
_FsApIfOutMulcastPkts_Object = MibTableColumn
fsApIfOutMulcastPkts = _FsApIfOutMulcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 42),
    _FsApIfOutMulcastPkts_Type()
)
fsApIfOutMulcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutMulcastPkts.setStatus("current")
_FsApIfInPayloadOctets_Type = Counter64
_FsApIfInPayloadOctets_Object = MibTableColumn
fsApIfInPayloadOctets = _FsApIfInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 43),
    _FsApIfInPayloadOctets_Type()
)
fsApIfInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInPayloadOctets.setStatus("current")
_FsApIfOutPayloadOctets_Type = Counter64
_FsApIfOutPayloadOctets_Object = MibTableColumn
fsApIfOutPayloadOctets = _FsApIfOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 44),
    _FsApIfOutPayloadOctets_Type()
)
fsApIfOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutPayloadOctets.setStatus("current")


class _FsApIfAlias_Type(DisplayString):
    """Custom type fsApIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsApIfAlias_Type.__name__ = "DisplayString"
_FsApIfAlias_Object = MibTableColumn
fsApIfAlias = _FsApIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 45),
    _FsApIfAlias_Type()
)
fsApIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfAlias.setStatus("current")
_FsApIfInDateRate_Type = Counter64
_FsApIfInDateRate_Object = MibTableColumn
fsApIfInDateRate = _FsApIfInDateRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 46),
    _FsApIfInDateRate_Type()
)
fsApIfInDateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfInDateRate.setStatus("current")
_FsApIfOutDateRate_Type = Counter64
_FsApIfOutDateRate_Object = MibTableColumn
fsApIfOutDateRate = _FsApIfOutDateRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 47),
    _FsApIfOutDateRate_Type()
)
fsApIfOutDateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutDateRate.setStatus("current")
_FsApifInNormalPkts_Type = Counter64
_FsApifInNormalPkts_Object = MibTableColumn
fsApifInNormalPkts = _FsApifInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 48),
    _FsApifInNormalPkts_Type()
)
fsApifInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApifInNormalPkts.setStatus("current")
_FsApIfOutPkts_Type = Counter64
_FsApIfOutPkts_Object = MibTableColumn
fsApIfOutPkts = _FsApIfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 13, 1, 49),
    _FsApIfOutPkts_Type()
)
fsApIfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIfOutPkts.setStatus("current")
_FsIfLinkTable_Object = MibTable
fsIfLinkTable = _FsIfLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14)
)
if mibBuilder.loadTexts:
    fsIfLinkTable.setStatus("current")
_FsIfLinkEntry_Object = MibTableRow
fsIfLinkEntry = _FsIfLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1)
)
fsIfLinkEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfLinkIndex"),
)
if mibBuilder.loadTexts:
    fsIfLinkEntry.setStatus("current")
_FsIfLinkIndex_Type = IfIndex
_FsIfLinkIndex_Object = MibTableColumn
fsIfLinkIndex = _FsIfLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 1),
    _FsIfLinkIndex_Type()
)
fsIfLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkIndex.setStatus("current")
_FsIfUplinkInOctets_Type = Counter32
_FsIfUplinkInOctets_Object = MibTableColumn
fsIfUplinkInOctets = _FsIfUplinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 2),
    _FsIfUplinkInOctets_Type()
)
fsIfUplinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkInOctets.setStatus("current")
_FsIfUplinkInUcastPkts_Type = Counter32
_FsIfUplinkInUcastPkts_Object = MibTableColumn
fsIfUplinkInUcastPkts = _FsIfUplinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 3),
    _FsIfUplinkInUcastPkts_Type()
)
fsIfUplinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkInUcastPkts.setStatus("current")
_FsIfUplinkInNUcastPkts_Type = Counter32
_FsIfUplinkInNUcastPkts_Object = MibTableColumn
fsIfUplinkInNUcastPkts = _FsIfUplinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 4),
    _FsIfUplinkInNUcastPkts_Type()
)
fsIfUplinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkInNUcastPkts.setStatus("deprecated")
_FsIfUplinkInDiscards_Type = Counter32
_FsIfUplinkInDiscards_Object = MibTableColumn
fsIfUplinkInDiscards = _FsIfUplinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 5),
    _FsIfUplinkInDiscards_Type()
)
fsIfUplinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkInDiscards.setStatus("current")
_FsIfUplinkInErrors_Type = Counter32
_FsIfUplinkInErrors_Object = MibTableColumn
fsIfUplinkInErrors = _FsIfUplinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 6),
    _FsIfUplinkInErrors_Type()
)
fsIfUplinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkInErrors.setStatus("current")
_FsIfUplinkOutOctets_Type = Counter32
_FsIfUplinkOutOctets_Object = MibTableColumn
fsIfUplinkOutOctets = _FsIfUplinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 7),
    _FsIfUplinkOutOctets_Type()
)
fsIfUplinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkOutOctets.setStatus("current")
_FsIfUplinkOutUcastPkts_Type = Counter32
_FsIfUplinkOutUcastPkts_Object = MibTableColumn
fsIfUplinkOutUcastPkts = _FsIfUplinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 8),
    _FsIfUplinkOutUcastPkts_Type()
)
fsIfUplinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkOutUcastPkts.setStatus("current")
_FsIfUplinkOutNUcastPkts_Type = Counter32
_FsIfUplinkOutNUcastPkts_Object = MibTableColumn
fsIfUplinkOutNUcastPkts = _FsIfUplinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 9),
    _FsIfUplinkOutNUcastPkts_Type()
)
fsIfUplinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkOutNUcastPkts.setStatus("deprecated")
_FsIfUplinkOutDiscards_Type = Counter32
_FsIfUplinkOutDiscards_Object = MibTableColumn
fsIfUplinkOutDiscards = _FsIfUplinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 10),
    _FsIfUplinkOutDiscards_Type()
)
fsIfUplinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkOutDiscards.setStatus("current")
_FsIfUplinkOutErrors_Type = Counter32
_FsIfUplinkOutErrors_Object = MibTableColumn
fsIfUplinkOutErrors = _FsIfUplinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 11),
    _FsIfUplinkOutErrors_Type()
)
fsIfUplinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkOutErrors.setStatus("current")
_FsIfDownlinkInOctets_Type = Counter32
_FsIfDownlinkInOctets_Object = MibTableColumn
fsIfDownlinkInOctets = _FsIfDownlinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 12),
    _FsIfDownlinkInOctets_Type()
)
fsIfDownlinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkInOctets.setStatus("current")
_FsIfDownlinkInUcastPkts_Type = Counter32
_FsIfDownlinkInUcastPkts_Object = MibTableColumn
fsIfDownlinkInUcastPkts = _FsIfDownlinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 13),
    _FsIfDownlinkInUcastPkts_Type()
)
fsIfDownlinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkInUcastPkts.setStatus("current")
_FsIfDownlinkInNUcastPkts_Type = Counter32
_FsIfDownlinkInNUcastPkts_Object = MibTableColumn
fsIfDownlinkInNUcastPkts = _FsIfDownlinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 14),
    _FsIfDownlinkInNUcastPkts_Type()
)
fsIfDownlinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkInNUcastPkts.setStatus("deprecated")
_FsIfDownlinkInDiscards_Type = Counter32
_FsIfDownlinkInDiscards_Object = MibTableColumn
fsIfDownlinkInDiscards = _FsIfDownlinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 15),
    _FsIfDownlinkInDiscards_Type()
)
fsIfDownlinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkInDiscards.setStatus("current")
_FsIfDownlinkInErrors_Type = Counter32
_FsIfDownlinkInErrors_Object = MibTableColumn
fsIfDownlinkInErrors = _FsIfDownlinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 16),
    _FsIfDownlinkInErrors_Type()
)
fsIfDownlinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkInErrors.setStatus("current")
_FsIfDownlinkOutOctets_Type = Counter32
_FsIfDownlinkOutOctets_Object = MibTableColumn
fsIfDownlinkOutOctets = _FsIfDownlinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 17),
    _FsIfDownlinkOutOctets_Type()
)
fsIfDownlinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkOutOctets.setStatus("current")
_FsIfDownlinkOutUcastPkts_Type = Counter32
_FsIfDownlinkOutUcastPkts_Object = MibTableColumn
fsIfDownlinkOutUcastPkts = _FsIfDownlinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 18),
    _FsIfDownlinkOutUcastPkts_Type()
)
fsIfDownlinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkOutUcastPkts.setStatus("current")
_FsIfDownlinkOutNUcastPkts_Type = Counter32
_FsIfDownlinkOutNUcastPkts_Object = MibTableColumn
fsIfDownlinkOutNUcastPkts = _FsIfDownlinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 19),
    _FsIfDownlinkOutNUcastPkts_Type()
)
fsIfDownlinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkOutNUcastPkts.setStatus("deprecated")
_FsIfDownlinkOutDiscards_Type = Counter32
_FsIfDownlinkOutDiscards_Object = MibTableColumn
fsIfDownlinkOutDiscards = _FsIfDownlinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 20),
    _FsIfDownlinkOutDiscards_Type()
)
fsIfDownlinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkOutDiscards.setStatus("current")
_FsIfDownlinkOutErrors_Type = Counter32
_FsIfDownlinkOutErrors_Object = MibTableColumn
fsIfDownlinkOutErrors = _FsIfDownlinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 21),
    _FsIfDownlinkOutErrors_Type()
)
fsIfDownlinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkOutErrors.setStatus("current")
_FsIfUplinkInBcastPkts_Type = Counter64
_FsIfUplinkInBcastPkts_Object = MibTableColumn
fsIfUplinkInBcastPkts = _FsIfUplinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 22),
    _FsIfUplinkInBcastPkts_Type()
)
fsIfUplinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkInBcastPkts.setStatus("current")
_FsIfUplinkOutBcastPkts_Type = Counter64
_FsIfUplinkOutBcastPkts_Object = MibTableColumn
fsIfUplinkOutBcastPkts = _FsIfUplinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 23),
    _FsIfUplinkOutBcastPkts_Type()
)
fsIfUplinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfUplinkOutBcastPkts.setStatus("current")
_FsIfDownlinkInBcastPkts_Type = Counter64
_FsIfDownlinkInBcastPkts_Object = MibTableColumn
fsIfDownlinkInBcastPkts = _FsIfDownlinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 24),
    _FsIfDownlinkInBcastPkts_Type()
)
fsIfDownlinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkInBcastPkts.setStatus("current")
_FsIfDownlinkOutBcastPkts_Type = Counter64
_FsIfDownlinkOutBcastPkts_Object = MibTableColumn
fsIfDownlinkOutBcastPkts = _FsIfDownlinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 14, 1, 25),
    _FsIfDownlinkOutBcastPkts_Type()
)
fsIfDownlinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDownlinkOutBcastPkts.setStatus("current")
_FsIfTrafficStatisticsObjects_ObjectIdentity = ObjectIdentity
fsIfTrafficStatisticsObjects = _FsIfTrafficStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15)
)
_FsIfLinkTrafficStatistics_ObjectIdentity = ObjectIdentity
fsIfLinkTrafficStatistics = _FsIfLinkTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1)
)
_FsIfLinkTrafficTable_Object = MibTable
fsIfLinkTrafficTable = _FsIfLinkTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    fsIfLinkTrafficTable.setStatus("current")
_FsIfLinkTrafficEntry_Object = MibTableRow
fsIfLinkTrafficEntry = _FsIfLinkTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1)
)
fsIfLinkTrafficEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfLinkTrafficIndex"),
)
if mibBuilder.loadTexts:
    fsIfLinkTrafficEntry.setStatus("current")
_FsIfLinkTrafficIndex_Type = Unsigned32
_FsIfLinkTrafficIndex_Object = MibTableColumn
fsIfLinkTrafficIndex = _FsIfLinkTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 1),
    _FsIfLinkTrafficIndex_Type()
)
fsIfLinkTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkTrafficIndex.setStatus("current")


class _FsIfLinkAvgRate_Type(Counter32):
    """Custom type fsIfLinkAvgRate based on Counter32"""
    defaultValue = 0


_FsIfLinkAvgRate_Type.__name__ = "Counter32"
_FsIfLinkAvgRate_Object = MibTableColumn
fsIfLinkAvgRate = _FsIfLinkAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 2),
    _FsIfLinkAvgRate_Type()
)
fsIfLinkAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkAvgRate.setStatus("current")


class _FsIfLinkPeakRate_Type(Counter32):
    """Custom type fsIfLinkPeakRate based on Counter32"""
    defaultValue = 0


_FsIfLinkPeakRate_Type.__name__ = "Counter32"
_FsIfLinkPeakRate_Object = MibTableColumn
fsIfLinkPeakRate = _FsIfLinkPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 3),
    _FsIfLinkPeakRate_Type()
)
fsIfLinkPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkPeakRate.setStatus("current")


class _FsIfLinkAvgBWUtilization_Type(Integer32):
    """Custom type fsIfLinkAvgBWUtilization based on Integer32"""
    defaultValue = 0


_FsIfLinkAvgBWUtilization_Type.__name__ = "Integer32"
_FsIfLinkAvgBWUtilization_Object = MibTableColumn
fsIfLinkAvgBWUtilization = _FsIfLinkAvgBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 4),
    _FsIfLinkAvgBWUtilization_Type()
)
fsIfLinkAvgBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkAvgBWUtilization.setStatus("current")


class _FsIfLinkPeakBWUtilization_Type(Integer32):
    """Custom type fsIfLinkPeakBWUtilization based on Integer32"""
    defaultValue = 0


_FsIfLinkPeakBWUtilization_Type.__name__ = "Integer32"
_FsIfLinkPeakBWUtilization_Object = MibTableColumn
fsIfLinkPeakBWUtilization = _FsIfLinkPeakBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 5),
    _FsIfLinkPeakBWUtilization_Type()
)
fsIfLinkPeakBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfLinkPeakBWUtilization.setStatus("current")
_FsIfLinkQosStatistics_ObjectIdentity = ObjectIdentity
fsIfLinkQosStatistics = _FsIfLinkQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2)
)
_FsLinkQosCtlTable_Object = MibTable
fsLinkQosCtlTable = _FsLinkQosCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    fsLinkQosCtlTable.setStatus("current")
_FsLinkQosCtlEntry_Object = MibTableRow
fsLinkQosCtlEntry = _FsLinkQosCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1)
)
fsLinkQosCtlEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsLinkQosCtlOwnerIndex"),
    (0, "FS-INTERFACE-MIB", "fsLinkQosCtlTestName"),
)
if mibBuilder.loadTexts:
    fsLinkQosCtlEntry.setStatus("current")


class _FsLinkQosCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type fsLinkQosCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLinkQosCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_FsLinkQosCtlOwnerIndex_Object = MibTableColumn
fsLinkQosCtlOwnerIndex = _FsLinkQosCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 1),
    _FsLinkQosCtlOwnerIndex_Type()
)
fsLinkQosCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLinkQosCtlOwnerIndex.setStatus("current")


class _FsLinkQosCtlTestName_Type(SnmpAdminString):
    """Custom type fsLinkQosCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsLinkQosCtlTestName_Type.__name__ = "SnmpAdminString"
_FsLinkQosCtlTestName_Object = MibTableColumn
fsLinkQosCtlTestName = _FsLinkQosCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 2),
    _FsLinkQosCtlTestName_Type()
)
fsLinkQosCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLinkQosCtlTestName.setStatus("current")


class _FsLinkQosCtlTargetAddressType_Type(InetAddressType):
    """Custom type fsLinkQosCtlTargetAddressType based on InetAddressType"""
    defaultValue = 0


_FsLinkQosCtlTargetAddressType_Type.__name__ = "InetAddressType"
_FsLinkQosCtlTargetAddressType_Object = MibTableColumn
fsLinkQosCtlTargetAddressType = _FsLinkQosCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 3),
    _FsLinkQosCtlTargetAddressType_Type()
)
fsLinkQosCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLinkQosCtlTargetAddressType.setStatus("current")


class _FsLinkQosCtlTargetAddress_Type(InetAddress):
    """Custom type fsLinkQosCtlTargetAddress based on InetAddress"""
    defaultHexValue = ""


_FsLinkQosCtlTargetAddress_Type.__name__ = "InetAddress"
_FsLinkQosCtlTargetAddress_Object = MibTableColumn
fsLinkQosCtlTargetAddress = _FsLinkQosCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 4),
    _FsLinkQosCtlTargetAddress_Type()
)
fsLinkQosCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLinkQosCtlTargetAddress.setStatus("current")


class _FsLinkQosCtlAdminStatus_Type(Integer32):
    """Custom type fsLinkQosCtlAdminStatus based on Integer32"""
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


_FsLinkQosCtlAdminStatus_Type.__name__ = "Integer32"
_FsLinkQosCtlAdminStatus_Object = MibTableColumn
fsLinkQosCtlAdminStatus = _FsLinkQosCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 5),
    _FsLinkQosCtlAdminStatus_Type()
)
fsLinkQosCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLinkQosCtlAdminStatus.setStatus("current")
_FsLinkQosCtlRowStatus_Type = RowStatus
_FsLinkQosCtlRowStatus_Object = MibTableColumn
fsLinkQosCtlRowStatus = _FsLinkQosCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 6),
    _FsLinkQosCtlRowStatus_Type()
)
fsLinkQosCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsLinkQosCtlRowStatus.setStatus("current")
_FsLinkQosResultsTable_Object = MibTable
fsLinkQosResultsTable = _FsLinkQosResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    fsLinkQosResultsTable.setStatus("current")
_FsLinkQosResultsEntry_Object = MibTableRow
fsLinkQosResultsEntry = _FsLinkQosResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1)
)
fsLinkQosResultsEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsLinkQosCtlOwnerIndex"),
    (0, "FS-INTERFACE-MIB", "fsLinkQosCtlTestName"),
)
if mibBuilder.loadTexts:
    fsLinkQosResultsEntry.setStatus("current")


class _FsLinkQosResultsOperStatus_Type(Integer32):
    """Custom type fsLinkQosResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("completed", 3))
    )


_FsLinkQosResultsOperStatus_Type.__name__ = "Integer32"
_FsLinkQosResultsOperStatus_Object = MibTableColumn
fsLinkQosResultsOperStatus = _FsLinkQosResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 1),
    _FsLinkQosResultsOperStatus_Type()
)
fsLinkQosResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsOperStatus.setStatus("current")


class _FsLinkQosResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type fsLinkQosResultsIpTargetAddressType based on InetAddressType"""
    defaultValue = 0


_FsLinkQosResultsIpTargetAddressType_Type.__name__ = "InetAddressType"
_FsLinkQosResultsIpTargetAddressType_Object = MibTableColumn
fsLinkQosResultsIpTargetAddressType = _FsLinkQosResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 2),
    _FsLinkQosResultsIpTargetAddressType_Type()
)
fsLinkQosResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsIpTargetAddressType.setStatus("current")


class _FsLinkQosResultsIpTargetAddress_Type(InetAddress):
    """Custom type fsLinkQosResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_FsLinkQosResultsIpTargetAddress_Type.__name__ = "InetAddress"
_FsLinkQosResultsIpTargetAddress_Object = MibTableColumn
fsLinkQosResultsIpTargetAddress = _FsLinkQosResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 3),
    _FsLinkQosResultsIpTargetAddress_Type()
)
fsLinkQosResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsIpTargetAddress.setStatus("current")
_FsLinkQosResultsMaxRtt_Type = Unsigned32
_FsLinkQosResultsMaxRtt_Object = MibTableColumn
fsLinkQosResultsMaxRtt = _FsLinkQosResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 4),
    _FsLinkQosResultsMaxRtt_Type()
)
fsLinkQosResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    fsLinkQosResultsMaxRtt.setUnits("milliseconds")
_FsLinkQosResultsMinRtt_Type = Unsigned32
_FsLinkQosResultsMinRtt_Object = MibTableColumn
fsLinkQosResultsMinRtt = _FsLinkQosResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 5),
    _FsLinkQosResultsMinRtt_Type()
)
fsLinkQosResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    fsLinkQosResultsMinRtt.setUnits("milliseconds")
_FsLinkQosResultsAverageRtt_Type = Unsigned32
_FsLinkQosResultsAverageRtt_Object = MibTableColumn
fsLinkQosResultsAverageRtt = _FsLinkQosResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 6),
    _FsLinkQosResultsAverageRtt_Type()
)
fsLinkQosResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    fsLinkQosResultsAverageRtt.setUnits("milliseconds")
_FsLinkQosResultsDelayJitter_Type = Unsigned32
_FsLinkQosResultsDelayJitter_Object = MibTableColumn
fsLinkQosResultsDelayJitter = _FsLinkQosResultsDelayJitter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 7),
    _FsLinkQosResultsDelayJitter_Type()
)
fsLinkQosResultsDelayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsDelayJitter.setStatus("current")
if mibBuilder.loadTexts:
    fsLinkQosResultsDelayJitter.setUnits("milliseconds")
_FsLinkQosResultsPktsLossRate_Type = Unsigned32
_FsLinkQosResultsPktsLossRate_Object = MibTableColumn
fsLinkQosResultsPktsLossRate = _FsLinkQosResultsPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 8),
    _FsLinkQosResultsPktsLossRate_Type()
)
fsLinkQosResultsPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsPktsLossRate.setStatus("current")
_FsLinkQosResultsNetworkAF_Type = Unsigned32
_FsLinkQosResultsNetworkAF_Object = MibTableColumn
fsLinkQosResultsNetworkAF = _FsLinkQosResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 9),
    _FsLinkQosResultsNetworkAF_Type()
)
fsLinkQosResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLinkQosResultsNetworkAF.setStatus("current")
_FsIfDeviceTrafficStatistics_ObjectIdentity = ObjectIdentity
fsIfDeviceTrafficStatistics = _FsIfDeviceTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3)
)
_FsIfDeviceTrafficTable_Object = MibTable
fsIfDeviceTrafficTable = _FsIfDeviceTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    fsIfDeviceTrafficTable.setStatus("current")
_FsIfDeviceTrafficEntry_Object = MibTableRow
fsIfDeviceTrafficEntry = _FsIfDeviceTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1)
)
fsIfDeviceTrafficEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfDeviceTrafficIndex"),
)
if mibBuilder.loadTexts:
    fsIfDeviceTrafficEntry.setStatus("current")
_FsIfDeviceTrafficIndex_Type = Unsigned32
_FsIfDeviceTrafficIndex_Object = MibTableColumn
fsIfDeviceTrafficIndex = _FsIfDeviceTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 1),
    _FsIfDeviceTrafficIndex_Type()
)
fsIfDeviceTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDeviceTrafficIndex.setStatus("current")
_FsIfFC_Type = Integer32
_FsIfFC_Object = MibTableColumn
fsIfFC = _FsIfFC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 2),
    _FsIfFC_Type()
)
fsIfFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFC.setStatus("current")
_FsIfFCTransRate_Type = Counter32
_FsIfFCTransRate_Object = MibTableColumn
fsIfFCTransRate = _FsIfFCTransRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 3),
    _FsIfFCTransRate_Type()
)
fsIfFCTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCTransRate.setStatus("current")
_FsIfFCTransPktsNum_Type = Counter64
_FsIfFCTransPktsNum_Object = MibTableColumn
fsIfFCTransPktsNum = _FsIfFCTransPktsNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 4),
    _FsIfFCTransPktsNum_Type()
)
fsIfFCTransPktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCTransPktsNum.setStatus("current")
_FsIfFCDiscardRate_Type = Counter32
_FsIfFCDiscardRate_Object = MibTableColumn
fsIfFCDiscardRate = _FsIfFCDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 5),
    _FsIfFCDiscardRate_Type()
)
fsIfFCDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCDiscardRate.setStatus("current")
_FsIfFCDiscardPktsNum_Type = Counter64
_FsIfFCDiscardPktsNum_Object = MibTableColumn
fsIfFCDiscardPktsNum = _FsIfFCDiscardPktsNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 6),
    _FsIfFCDiscardPktsNum_Type()
)
fsIfFCDiscardPktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCDiscardPktsNum.setStatus("current")
_FsIfFCPktsLossRate_Type = Integer32
_FsIfFCPktsLossRate_Object = MibTableColumn
fsIfFCPktsLossRate = _FsIfFCPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 7),
    _FsIfFCPktsLossRate_Type()
)
fsIfFCPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCPktsLossRate.setStatus("current")
_FsIfFCBandwidthRate_Type = Counter32
_FsIfFCBandwidthRate_Object = MibTableColumn
fsIfFCBandwidthRate = _FsIfFCBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 8),
    _FsIfFCBandwidthRate_Type()
)
fsIfFCBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCBandwidthRate.setStatus("current")
_FsIfFCBandwidthPercentage_Type = Integer32
_FsIfFCBandwidthPercentage_Object = MibTableColumn
fsIfFCBandwidthPercentage = _FsIfFCBandwidthPercentage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 9),
    _FsIfFCBandwidthPercentage_Type()
)
fsIfFCBandwidthPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFCBandwidthPercentage.setStatus("current")
_FsIfDeviceFCGathers_Type = Integer32
_FsIfDeviceFCGathers_Object = MibTableColumn
fsIfDeviceFCGathers = _FsIfDeviceFCGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 10),
    _FsIfDeviceFCGathers_Type()
)
fsIfDeviceFCGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDeviceFCGathers.setStatus("current")
_FsIfFullMeshFCGathers_Type = Integer32
_FsIfFullMeshFCGathers_Object = MibTableColumn
fsIfFullMeshFCGathers = _FsIfFullMeshFCGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 11),
    _FsIfFullMeshFCGathers_Type()
)
fsIfFullMeshFCGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFullMeshFCGathers.setStatus("current")
_FsIfClassBasedGathers_Type = Integer32
_FsIfClassBasedGathers_Object = MibTableColumn
fsIfClassBasedGathers = _FsIfClassBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 12),
    _FsIfClassBasedGathers_Type()
)
fsIfClassBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfClassBasedGathers.setStatus("current")
_FsIfNodeBasedGathers_Type = Integer32
_FsIfNodeBasedGathers_Object = MibTableColumn
fsIfNodeBasedGathers = _FsIfNodeBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 13),
    _FsIfNodeBasedGathers_Type()
)
fsIfNodeBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfNodeBasedGathers.setStatus("current")
_FsIfNodeClassBasedGathers_Type = Integer32
_FsIfNodeClassBasedGathers_Object = MibTableColumn
fsIfNodeClassBasedGathers = _FsIfNodeClassBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 14),
    _FsIfNodeClassBasedGathers_Type()
)
fsIfNodeClassBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfNodeClassBasedGathers.setStatus("current")
_FsIfNodeFCBasedGathers_Type = Integer32
_FsIfNodeFCBasedGathers_Object = MibTableColumn
fsIfNodeFCBasedGathers = _FsIfNodeFCBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 15),
    _FsIfNodeFCBasedGathers_Type()
)
fsIfNodeFCBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfNodeFCBasedGathers.setStatus("current")
_FsIfNodeDeviceFCBasedGathers_Type = Integer32
_FsIfNodeDeviceFCBasedGathers_Object = MibTableColumn
fsIfNodeDeviceFCBasedGathers = _FsIfNodeDeviceFCBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 16),
    _FsIfNodeDeviceFCBasedGathers_Type()
)
fsIfNodeDeviceFCBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfNodeDeviceFCBasedGathers.setStatus("current")
_FsIfPhyTable_Object = MibTable
fsIfPhyTable = _FsIfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 16)
)
if mibBuilder.loadTexts:
    fsIfPhyTable.setStatus("current")
_FsIfPhyEntry_Object = MibTableRow
fsIfPhyEntry = _FsIfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 16, 1)
)
fsIfPhyEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfPhyIndex"),
)
if mibBuilder.loadTexts:
    fsIfPhyEntry.setStatus("current")
_FsIfPhyIndex_Type = IfIndex
_FsIfPhyIndex_Object = MibTableColumn
fsIfPhyIndex = _FsIfPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 16, 1, 1),
    _FsIfPhyIndex_Type()
)
fsIfPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfPhyIndex.setStatus("current")


class _FsifPhyOperStatus_Type(Integer32):
    """Custom type fsifPhyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("admindown", 2))
    )


_FsifPhyOperStatus_Type.__name__ = "Integer32"
_FsifPhyOperStatus_Object = MibTableColumn
fsifPhyOperStatus = _FsifPhyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 16, 1, 2),
    _FsifPhyOperStatus_Type()
)
fsifPhyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsifPhyOperStatus.setStatus("current")
_FsIfPeakRateTable_Object = MibTable
fsIfPeakRateTable = _FsIfPeakRateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17)
)
if mibBuilder.loadTexts:
    fsIfPeakRateTable.setStatus("current")
_FsIfPeakRateEntry_Object = MibTableRow
fsIfPeakRateEntry = _FsIfPeakRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17, 1)
)
fsIfPeakRateEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfPeakRateIndex"),
)
if mibBuilder.loadTexts:
    fsIfPeakRateEntry.setStatus("current")
_FsIfPeakRateIndex_Type = IfIndex
_FsIfPeakRateIndex_Object = MibTableColumn
fsIfPeakRateIndex = _FsIfPeakRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17, 1, 1),
    _FsIfPeakRateIndex_Type()
)
fsIfPeakRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfPeakRateIndex.setStatus("current")
_FsIfRxPeakRate_Type = Counter64
_FsIfRxPeakRate_Object = MibTableColumn
fsIfRxPeakRate = _FsIfRxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17, 1, 2),
    _FsIfRxPeakRate_Type()
)
fsIfRxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfRxPeakRate.setStatus("current")
_FsIfRxPeakRateTime_Type = DisplayString
_FsIfRxPeakRateTime_Object = MibTableColumn
fsIfRxPeakRateTime = _FsIfRxPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17, 1, 3),
    _FsIfRxPeakRateTime_Type()
)
fsIfRxPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfRxPeakRateTime.setStatus("current")
_FsIfTxPeakRate_Type = Counter64
_FsIfTxPeakRate_Object = MibTableColumn
fsIfTxPeakRate = _FsIfTxPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17, 1, 4),
    _FsIfTxPeakRate_Type()
)
fsIfTxPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfTxPeakRate.setStatus("current")
_FsIfTxPeakRateTime_Type = DisplayString
_FsIfTxPeakRateTime_Object = MibTableColumn
fsIfTxPeakRateTime = _FsIfTxPeakRateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 17, 1, 5),
    _FsIfTxPeakRateTime_Type()
)
fsIfTxPeakRateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfTxPeakRateTime.setStatus("current")
_FsApInfoTable_Object = MibTable
fsApInfoTable = _FsApInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18)
)
if mibBuilder.loadTexts:
    fsApInfoTable.setStatus("current")
_FsApInfoEntry_Object = MibTableRow
fsApInfoEntry = _FsApInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18, 1)
)
fsApInfoEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsApInfoAddress"),
)
if mibBuilder.loadTexts:
    fsApInfoEntry.setStatus("current")
_FsApInfoAddress_Type = PhysAddress
_FsApInfoAddress_Object = MibTableColumn
fsApInfoAddress = _FsApInfoAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18, 1, 1),
    _FsApInfoAddress_Type()
)
fsApInfoAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApInfoAddress.setStatus("current")
_FsApInfoWireInRate_Type = Counter64
_FsApInfoWireInRate_Object = MibTableColumn
fsApInfoWireInRate = _FsApInfoWireInRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18, 1, 2),
    _FsApInfoWireInRate_Type()
)
fsApInfoWireInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApInfoWireInRate.setStatus("current")
_FsApInfoWireOutRate_Type = Counter64
_FsApInfoWireOutRate_Object = MibTableColumn
fsApInfoWireOutRate = _FsApInfoWireOutRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18, 1, 3),
    _FsApInfoWireOutRate_Type()
)
fsApInfoWireOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApInfoWireOutRate.setStatus("current")
_FsApInfoWireInOctets_Type = Counter64
_FsApInfoWireInOctets_Object = MibTableColumn
fsApInfoWireInOctets = _FsApInfoWireInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18, 1, 4),
    _FsApInfoWireInOctets_Type()
)
fsApInfoWireInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApInfoWireInOctets.setStatus("current")
_FsApInfoWireOutOctets_Type = Counter64
_FsApInfoWireOutOctets_Object = MibTableColumn
fsApInfoWireOutOctets = _FsApInfoWireOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 18, 1, 5),
    _FsApInfoWireOutOctets_Type()
)
fsApInfoWireOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApInfoWireOutOctets.setStatus("current")
_FsIfDropTable_Object = MibTable
fsIfDropTable = _FsIfDropTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19)
)
if mibBuilder.loadTexts:
    fsIfDropTable.setStatus("current")
_FsIfDropEntry_Object = MibTableRow
fsIfDropEntry = _FsIfDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1)
)
fsIfDropEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfDropIndex"),
)
if mibBuilder.loadTexts:
    fsIfDropEntry.setStatus("current")
_FsIfDropIndex_Type = Unsigned32
_FsIfDropIndex_Object = MibTableColumn
fsIfDropIndex = _FsIfDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 1),
    _FsIfDropIndex_Type()
)
fsIfDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfDropIndex.setStatus("current")
_FsIfInDropPkts_Type = Counter64
_FsIfInDropPkts_Object = MibTableColumn
fsIfInDropPkts = _FsIfInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 2),
    _FsIfInDropPkts_Type()
)
fsIfInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInDropPkts.setStatus("current")
_FsIfInResLackPkts_Type = Counter64
_FsIfInResLackPkts_Object = MibTableColumn
fsIfInResLackPkts = _FsIfInResLackPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 3),
    _FsIfInResLackPkts_Type()
)
fsIfInResLackPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInResLackPkts.setStatus("current")
_FsIfInQosDropPkts_Type = Counter64
_FsIfInQosDropPkts_Object = MibTableColumn
fsIfInQosDropPkts = _FsIfInQosDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 4),
    _FsIfInQosDropPkts_Type()
)
fsIfInQosDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfInQosDropPkts.setStatus("current")
_FsIfFwdEntryDropPkts_Type = Counter64
_FsIfFwdEntryDropPkts_Object = MibTableColumn
fsIfFwdEntryDropPkts = _FsIfFwdEntryDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 5),
    _FsIfFwdEntryDropPkts_Type()
)
fsIfFwdEntryDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfFwdEntryDropPkts.setStatus("current")
_FsIfOutDropPkts_Type = Counter64
_FsIfOutDropPkts_Object = MibTableColumn
fsIfOutDropPkts = _FsIfOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 6),
    _FsIfOutDropPkts_Type()
)
fsIfOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutDropPkts.setStatus("current")
_FsIfOutResLackPkts_Type = Counter64
_FsIfOutResLackPkts_Object = MibTableColumn
fsIfOutResLackPkts = _FsIfOutResLackPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 7),
    _FsIfOutResLackPkts_Type()
)
fsIfOutResLackPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOutResLackPkts.setStatus("current")
_FsIfNoBufferConut_Type = Counter64
_FsIfNoBufferConut_Object = MibTableColumn
fsIfNoBufferConut = _FsIfNoBufferConut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 8),
    _FsIfNoBufferConut_Type()
)
fsIfNoBufferConut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfNoBufferConut.setStatus("current")
_FsIfOBMDropPkts_Type = Counter64
_FsIfOBMDropPkts_Object = MibTableColumn
fsIfOBMDropPkts = _FsIfOBMDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 1, 19, 1, 9),
    _FsIfOBMDropPkts_Type()
)
fsIfOBMDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfOBMDropPkts.setStatus("current")
_FsInterfaceTraps_ObjectIdentity = ObjectIdentity
fsInterfaceTraps = _FsInterfaceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 2)
)


class _LineDetectStatus_Type(Integer32):
    """Custom type lineDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("open", 2),
          ("short", 3))
    )


_LineDetectStatus_Type.__name__ = "Integer32"
_LineDetectStatus_Object = MibScalar
lineDetectStatus = _LineDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 2, 1),
    _LineDetectStatus_Type()
)
lineDetectStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectStatus.setStatus("current")
_LineDetectPosition_Type = Integer32
_LineDetectPosition_Object = MibScalar
lineDetectPosition = _LineDetectPosition_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 2, 2),
    _LineDetectPosition_Type()
)
lineDetectPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectPosition.setStatus("current")
_FsInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
fsInterfaceMIBConformance = _FsInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3)
)
_FsInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
fsInterfaceMIBCompliances = _FsInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 1)
)
_FsInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
fsInterfaceMIBGroups = _FsInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 2)
)

# Managed Objects groups

fsInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 2, 1)
)
fsInterfaceMIBGroup.setObjects(
      *(("FS-INTERFACE-MIB", "fsIfIndex"),
        ("FS-INTERFACE-MIB", "fsIfPortType"),
        ("FS-INTERFACE-MIB", "fsIfFlowControlAdminStatus"),
        ("FS-INTERFACE-MIB", "fsIfFlowControlOperStatus"),
        ("FS-INTERFACE-MIB", "fsIfAdminSpeed"),
        ("FS-INTERFACE-MIB", "fsIfAdminDuplex"),
        ("FS-INTERFACE-MIB", "fsIfOperSpeed"),
        ("FS-INTERFACE-MIB", "fsIfOperDuplex"),
        ("FS-INTERFACE-MIB", "fsIfManageStatus"),
        ("FS-INTERFACE-MIB", "fsIfIpBroadcast"),
        ("FS-INTERFACE-MIB", "fsIfLayer"),
        ("FS-INTERFACE-MIB", "fsIfMode"),
        ("FS-INTERFACE-MIB", "fsIfCounterClear"),
        ("FS-INTERFACE-MIB", "fsIfEntryStatus"),
        ("FS-INTERFACE-MIB", "fsIfMediumType"),
        ("FS-INTERFACE-MIB", "fsIfDownCounter"),
        ("FS-INTERFACE-MIB", "fsIfInOctets"),
        ("FS-INTERFACE-MIB", "fsIfOutOctets"),
        ("FS-INTERFACE-MIB", "fsIfBcastInhibit"),
        ("FS-INTERFACE-MIB", "fsIfNegotiation"),
        ("FS-INTERFACE-MIB", "fsIfPhysAddress"),
        ("FS-INTERFACE-MIB", "fsIfAdminSpeedRW"),
        ("FS-INTERFACE-MIB", "fsIfAdminDuplexRW"),
        ("FS-INTERFACE-MIB", "fsIfModeRW"),
        ("FS-INTERFACE-MIB", "fsIfSpeed"),
        ("FS-INTERFACE-MIB", "fsifAdminStatus"),
        ("FS-INTERFACE-MIB", "fsifOperStatus"),
        ("FS-INTERFACE-MIB", "fsIfInNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfOutNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfUpDownTimes"),
        ("FS-INTERFACE-MIB", "fsifAdminStatusw"),
        ("FS-INTERFACE-MIB", "fsifOperStatusw"),
        ("FS-INTERFACE-MIB", "fsifSpeedw"),
        ("FS-INTERFACE-MIB", "fsifMacAddress"),
        ("FS-INTERFACE-MIB", "fsifLastChange"),
        ("FS-INTERFACE-MIB", "fsIfInPkts"),
        ("FS-INTERFACE-MIB", "fsIfDiscard"),
        ("FS-INTERFACE-MIB", "fsIfBandwidthUsage"),
        ("FS-INTERFACE-MIB", "fsIfInBitsRate"),
        ("FS-INTERFACE-MIB", "fsIfInPktRate"),
        ("FS-INTERFACE-MIB", "fsIfOutBitsRate"),
        ("FS-INTERFACE-MIB", "fsIfOutPktRate"),
        ("FS-INTERFACE-MIB", "fsIfInBandwidthUsage"),
        ("FS-INTERFACE-MIB", "fsIfOutBandwidthUsage"),
        ("FS-INTERFACE-MIB", "fsIfInErrorPktsRate"),
        ("FS-INTERFACE-MIB", "fsIfOutErrorPktsRate"),
        ("FS-INTERFACE-MIB", "fsIfInDropPktsRate"),
        ("FS-INTERFACE-MIB", "fsIfOutDropPktsRate"),
        ("FS-INTERFACE-MIB", "fsIfIpIfIndex"),
        ("FS-INTERFACE-MIB", "fsIfIpId"),
        ("FS-INTERFACE-MIB", "fsIfIp"),
        ("FS-INTERFACE-MIB", "fsIfIpMask"),
        ("FS-INTERFACE-MIB", "fsIfIpEntryStatus"),
        ("FS-INTERFACE-MIB", "fsIfStatusIndex"),
        ("FS-INTERFACE-MIB", "fsIfStatusLoopBackExamine"),
        ("FS-INTERFACE-MIB", "fsIfErrorStatus"),
        ("FS-INTERFACE-MIB", "fsGlobalIfDisableRecovery"),
        ("FS-INTERFACE-MIB", "fsIfSVICreatVlanNum"),
        ("FS-INTERFACE-MIB", "fsIfHandleSVI"),
        ("FS-INTERFACE-MIB", "fsIfEncapsulationIndex"),
        ("FS-INTERFACE-MIB", "fsIfEncapsulationVlan"),
        ("FS-INTERFACE-MIB", "fsApPhyAddress"),
        ("FS-INTERFACE-MIB", "fsApIfNumber"),
        ("FS-INTERFACE-MIB", "fsApIfPhyIntNum"),
        ("FS-INTERFACE-MIB", "fsApPhysAddress"),
        ("FS-INTERFACE-MIB", "fsApIfIndex"),
        ("FS-INTERFACE-MIB", "fsApIfDescr"),
        ("FS-INTERFACE-MIB", "fsApIfType"),
        ("FS-INTERFACE-MIB", "fsApIfMtu"),
        ("FS-INTERFACE-MIB", "fsApIfSpeed"),
        ("FS-INTERFACE-MIB", "fsApIfPhysAddress"),
        ("FS-INTERFACE-MIB", "fsApIfAdminStatus"),
        ("FS-INTERFACE-MIB", "fsApIfOperStatus"),
        ("FS-INTERFACE-MIB", "fsApIfLastChange"),
        ("FS-INTERFACE-MIB", "fsApIfInOctets"),
        ("FS-INTERFACE-MIB", "fsApIfInUcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfInNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfInDiscards"),
        ("FS-INTERFACE-MIB", "fsApIfInErrors"),
        ("FS-INTERFACE-MIB", "fsApIfInUnknownProtos"),
        ("FS-INTERFACE-MIB", "fsApIfOutOctets"),
        ("FS-INTERFACE-MIB", "fsApIfOutUcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfOutNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfOutDiscards"),
        ("FS-INTERFACE-MIB", "fsApIfOutErrors"),
        ("FS-INTERFACE-MIB", "fsApIfOutQLen"),
        ("FS-INTERFACE-MIB", "fsApIfLinkUPTimes"),
        ("FS-INTERFACE-MIB", "fsApIfInDataOctets"),
        ("FS-INTERFACE-MIB", "fsApIfOutDataOctets"),
        ("FS-INTERFACE-MIB", "fsApIfMgmtUploadOctets"),
        ("FS-INTERFACE-MIB", "fsApIfMgmtDownloadOctets"),
        ("FS-INTERFACE-MIB", "fsApIfSpeedw"),
        ("FS-INTERFACE-MIB", "fsApIfMtuw"),
        ("FS-INTERFACE-MIB", "fsApIfPhysAddressw"),
        ("FS-INTERFACE-MIB", "fsApIfInUcastPktsw"),
        ("FS-INTERFACE-MIB", "fsApIfInNUcastPktsw"),
        ("FS-INTERFACE-MIB", "fsApIfOutUcastPktsw"),
        ("FS-INTERFACE-MIB", "fsApIfOutNUcastPktsw"),
        ("FS-INTERFACE-MIB", "fsApIfLinkUPTimesw"),
        ("FS-INTERFACE-MIB", "fsApIfInPkts"),
        ("FS-INTERFACE-MIB", "fsApIfInFlow"),
        ("FS-INTERFACE-MIB", "fsApIfOutFlow"),
        ("FS-INTERFACE-MIB", "fsApIfInBrdcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfOutBrdcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfInMulcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfOutMulcastPkts"),
        ("FS-INTERFACE-MIB", "fsApIfInPayloadOctets"),
        ("FS-INTERFACE-MIB", "fsApIfOutPayloadOctets"),
        ("FS-INTERFACE-MIB", "fsApIfAlias"),
        ("FS-INTERFACE-MIB", "fsApIfInDateRate"),
        ("FS-INTERFACE-MIB", "fsApIfOutDateRate"),
        ("FS-INTERFACE-MIB", "fsApifInNormalPkts"),
        ("FS-INTERFACE-MIB", "fsApIfOutPkts"),
        ("FS-INTERFACE-MIB", "fsIfLinkIndex"),
        ("FS-INTERFACE-MIB", "fsIfUplinkInOctets"),
        ("FS-INTERFACE-MIB", "fsIfUplinkInUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfUplinkInNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfUplinkInDiscards"),
        ("FS-INTERFACE-MIB", "fsIfUplinkInErrors"),
        ("FS-INTERFACE-MIB", "fsIfUplinkOutOctets"),
        ("FS-INTERFACE-MIB", "fsIfUplinkOutUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfUplinkOutNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfUplinkOutDiscards"),
        ("FS-INTERFACE-MIB", "fsIfUplinkOutErrors"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkInOctets"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkInUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkInNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkInDiscards"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkInErrors"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkOutOctets"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkOutUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkOutNUcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkOutDiscards"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkOutErrors"),
        ("FS-INTERFACE-MIB", "fsIfUplinkInBcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfUplinkOutBcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkInBcastPkts"),
        ("FS-INTERFACE-MIB", "fsIfDownlinkOutBcastPkts"))
)
if mibBuilder.loadTexts:
    fsInterfaceMIBGroup.setStatus("current")

fsPortTypeChooseMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 2, 2)
)
fsPortTypeChooseMibGroup.setObjects(
      *(("FS-INTERFACE-MIB", "fsPortTypeChooseIndex"),
        ("FS-INTERFACE-MIB", "fsPortTypeChooseType"))
)
if mibBuilder.loadTexts:
    fsPortTypeChooseMibGroup.setStatus("current")

fsIfMTUMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 2, 3)
)
fsIfMTUMibGroup.setObjects(
      *(("FS-INTERFACE-MIB", "fsIfMTUIndex"),
        ("FS-INTERFACE-MIB", "fsIfMTU"))
)
if mibBuilder.loadTexts:
    fsIfMTUMibGroup.setStatus("current")

fsIfLineDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 2, 4)
)
fsIfLineDetectGroup.setObjects(
    ("FS-INTERFACE-MIB", "fsIfLineDetect")
)
if mibBuilder.loadTexts:
    fsIfLineDetectGroup.setStatus("current")

fsIfAvailableBWMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 2, 5)
)
fsIfAvailableBWMibGroup.setObjects(
      *(("FS-INTERFACE-MIB", "fsIfAvailableBWIfIndex"),
        ("FS-INTERFACE-MIB", "fsIfAvailableBWIfBW"))
)
if mibBuilder.loadTexts:
    fsIfAvailableBWMibGroup.setStatus("current")


# Notification objects

lineQualityDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 2, 3)
)
lineQualityDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("FS-INTERFACE-MIB", "lineDetectStatus"),
        ("FS-INTERFACE-MIB", "lineDetectPosition"))
)
if mibBuilder.loadTexts:
    lineQualityDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 10, 3, 1, 1)
)
fsInterfaceMIBCompliance.setObjects(
      *(("FS-INTERFACE-MIB", "fsInterfaceMIBGroup"),
        ("FS-INTERFACE-MIB", "fsPortTypeChooseMibGroup"),
        ("FS-INTERFACE-MIB", "fsIfMTUMibGroup"),
        ("FS-INTERFACE-MIB", "fsIfLineDetectGroup"),
        ("FS-INTERFACE-MIB", "fsIfAvailableBWMibGroup"))
)
if mibBuilder.loadTexts:
    fsInterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-INTERFACE-MIB",
    **{"fsInterfaceMIB": fsInterfaceMIB,
       "fsIfConfigMIBObjects": fsIfConfigMIBObjects,
       "fsIfTable": fsIfTable,
       "fsIfEntry": fsIfEntry,
       "fsIfIndex": fsIfIndex,
       "fsIfPortType": fsIfPortType,
       "fsIfFlowControlAdminStatus": fsIfFlowControlAdminStatus,
       "fsIfFlowControlOperStatus": fsIfFlowControlOperStatus,
       "fsIfAdminSpeed": fsIfAdminSpeed,
       "fsIfAdminDuplex": fsIfAdminDuplex,
       "fsIfOperSpeed": fsIfOperSpeed,
       "fsIfOperDuplex": fsIfOperDuplex,
       "fsIfManageStatus": fsIfManageStatus,
       "fsIfIpBroadcast": fsIfIpBroadcast,
       "fsIfLayer": fsIfLayer,
       "fsIfMode": fsIfMode,
       "fsIfCounterClear": fsIfCounterClear,
       "fsIfEntryStatus": fsIfEntryStatus,
       "fsIfMediumType": fsIfMediumType,
       "fsIfDownCounter": fsIfDownCounter,
       "fsIfInOctets": fsIfInOctets,
       "fsIfOutOctets": fsIfOutOctets,
       "fsIfBcastInhibit": fsIfBcastInhibit,
       "fsIfNegotiation": fsIfNegotiation,
       "fsIfPhysAddress": fsIfPhysAddress,
       "fsIfAdminSpeedRW": fsIfAdminSpeedRW,
       "fsIfAdminDuplexRW": fsIfAdminDuplexRW,
       "fsIfModeRW": fsIfModeRW,
       "fsIfSpeed": fsIfSpeed,
       "fsifAdminStatus": fsifAdminStatus,
       "fsifOperStatus": fsifOperStatus,
       "fsIfInNUcastPkts": fsIfInNUcastPkts,
       "fsIfOutNUcastPkts": fsIfOutNUcastPkts,
       "fsIfUpDownTimes": fsIfUpDownTimes,
       "fsifAdminStatusw": fsifAdminStatusw,
       "fsifOperStatusw": fsifOperStatusw,
       "fsifSpeedw": fsifSpeedw,
       "fsifMacAddress": fsifMacAddress,
       "fsifLastChange": fsifLastChange,
       "fsIfInPkts": fsIfInPkts,
       "fsIfDiscard": fsIfDiscard,
       "fsIfBandwidthUsage": fsIfBandwidthUsage,
       "fsIfInBitsRate": fsIfInBitsRate,
       "fsIfInPktRate": fsIfInPktRate,
       "fsIfOutBitsRate": fsIfOutBitsRate,
       "fsIfOutPktRate": fsIfOutPktRate,
       "fsIfInBandwidthUsage": fsIfInBandwidthUsage,
       "fsIfOutBandwidthUsage": fsIfOutBandwidthUsage,
       "fsIfInErrorPktsRate": fsIfInErrorPktsRate,
       "fsIfOutErrorPktsRate": fsIfOutErrorPktsRate,
       "fsIfInDropPktsRate": fsIfInDropPktsRate,
       "fsIfOutDropPktsRate": fsIfOutDropPktsRate,
       "fsIfOutNoBuffer": fsIfOutNoBuffer,
       "fsIfOutPkts": fsIfOutPkts,
       "fsIfIpTable": fsIfIpTable,
       "fsIfIpEntry": fsIfIpEntry,
       "fsIfIpIfIndex": fsIfIpIfIndex,
       "fsIfIpId": fsIfIpId,
       "fsIfIp": fsIfIp,
       "fsIfIpMask": fsIfIpMask,
       "fsIfIpEntryStatus": fsIfIpEntryStatus,
       "fsIfStatusTable": fsIfStatusTable,
       "fsIfStatusEntry": fsIfStatusEntry,
       "fsIfStatusIndex": fsIfStatusIndex,
       "fsIfStatusLoopBackExamine": fsIfStatusLoopBackExamine,
       "fsIfErrorStatus": fsIfErrorStatus,
       "fsIfLineDetect": fsIfLineDetect,
       "fsGlobalIfDisableRecovery": fsGlobalIfDisableRecovery,
       "fsPortTypeChooseTable": fsPortTypeChooseTable,
       "fsPortTypeChooseEntry": fsPortTypeChooseEntry,
       "fsPortTypeChooseIndex": fsPortTypeChooseIndex,
       "fsPortTypeChooseType": fsPortTypeChooseType,
       "fsIfMTUTable": fsIfMTUTable,
       "fsIfMTUEntry": fsIfMTUEntry,
       "fsIfMTUIndex": fsIfMTUIndex,
       "fsIfMTU": fsIfMTU,
       "fsIfAvailableBWTable": fsIfAvailableBWTable,
       "fsIfAvailableBWEntry": fsIfAvailableBWEntry,
       "fsIfAvailableBWIfIndex": fsIfAvailableBWIfIndex,
       "fsIfAvailableBWIfBW": fsIfAvailableBWIfBW,
       "fsIfSVICreatTable": fsIfSVICreatTable,
       "fsIfSVICreatEntry": fsIfSVICreatEntry,
       "fsIfSVICreatVlanNum": fsIfSVICreatVlanNum,
       "fsIfHandleSVI": fsIfHandleSVI,
       "fsIfPhyIntNum": fsIfPhyIntNum,
       "fsIfLinkUPTimesTable": fsIfLinkUPTimesTable,
       "fsIfLinkUPTimesEntry": fsIfLinkUPTimesEntry,
       "fsInterfaceIndex": fsInterfaceIndex,
       "fsIfLinkUPTimes": fsIfLinkUPTimes,
       "fsIfEncapsulationTable": fsIfEncapsulationTable,
       "fsIfEncapsulationEntry": fsIfEncapsulationEntry,
       "fsIfEncapsulationIndex": fsIfEncapsulationIndex,
       "fsIfEncapsulationVlan": fsIfEncapsulationVlan,
       "fsApIfNumberTable": fsApIfNumberTable,
       "fsApIfNumberEntry": fsApIfNumberEntry,
       "fsApPhyAddress": fsApPhyAddress,
       "fsApIfNumber": fsApIfNumber,
       "fsApIfPhyIntNum": fsApIfPhyIntNum,
       "fsApIfTable": fsApIfTable,
       "fsApIfEntry": fsApIfEntry,
       "fsApPhysAddress": fsApPhysAddress,
       "fsApIfIndex": fsApIfIndex,
       "fsApIfDescr": fsApIfDescr,
       "fsApIfType": fsApIfType,
       "fsApIfMtu": fsApIfMtu,
       "fsApIfSpeed": fsApIfSpeed,
       "fsApIfPhysAddress": fsApIfPhysAddress,
       "fsApIfAdminStatus": fsApIfAdminStatus,
       "fsApIfOperStatus": fsApIfOperStatus,
       "fsApIfLastChange": fsApIfLastChange,
       "fsApIfInOctets": fsApIfInOctets,
       "fsApIfInUcastPkts": fsApIfInUcastPkts,
       "fsApIfInNUcastPkts": fsApIfInNUcastPkts,
       "fsApIfInDiscards": fsApIfInDiscards,
       "fsApIfInErrors": fsApIfInErrors,
       "fsApIfInUnknownProtos": fsApIfInUnknownProtos,
       "fsApIfOutOctets": fsApIfOutOctets,
       "fsApIfOutUcastPkts": fsApIfOutUcastPkts,
       "fsApIfOutNUcastPkts": fsApIfOutNUcastPkts,
       "fsApIfOutDiscards": fsApIfOutDiscards,
       "fsApIfOutErrors": fsApIfOutErrors,
       "fsApIfOutQLen": fsApIfOutQLen,
       "fsApIfLinkUPTimes": fsApIfLinkUPTimes,
       "fsApIfInDataOctets": fsApIfInDataOctets,
       "fsApIfOutDataOctets": fsApIfOutDataOctets,
       "fsApIfMgmtUploadOctets": fsApIfMgmtUploadOctets,
       "fsApIfMgmtDownloadOctets": fsApIfMgmtDownloadOctets,
       "fsApIfSpeedw": fsApIfSpeedw,
       "fsApIfMtuw": fsApIfMtuw,
       "fsApIfPhysAddressw": fsApIfPhysAddressw,
       "fsApIfInUcastPktsw": fsApIfInUcastPktsw,
       "fsApIfInNUcastPktsw": fsApIfInNUcastPktsw,
       "fsApIfOutUcastPktsw": fsApIfOutUcastPktsw,
       "fsApIfOutNUcastPktsw": fsApIfOutNUcastPktsw,
       "fsApIfLinkUPTimesw": fsApIfLinkUPTimesw,
       "fsApIfInPkts": fsApIfInPkts,
       "fsApIfInFlow": fsApIfInFlow,
       "fsApIfOutFlow": fsApIfOutFlow,
       "fsApIfInBrdcastPkts": fsApIfInBrdcastPkts,
       "fsApIfOutBrdcastPkts": fsApIfOutBrdcastPkts,
       "fsApIfInMulcastPkts": fsApIfInMulcastPkts,
       "fsApIfOutMulcastPkts": fsApIfOutMulcastPkts,
       "fsApIfInPayloadOctets": fsApIfInPayloadOctets,
       "fsApIfOutPayloadOctets": fsApIfOutPayloadOctets,
       "fsApIfAlias": fsApIfAlias,
       "fsApIfInDateRate": fsApIfInDateRate,
       "fsApIfOutDateRate": fsApIfOutDateRate,
       "fsApifInNormalPkts": fsApifInNormalPkts,
       "fsApIfOutPkts": fsApIfOutPkts,
       "fsIfLinkTable": fsIfLinkTable,
       "fsIfLinkEntry": fsIfLinkEntry,
       "fsIfLinkIndex": fsIfLinkIndex,
       "fsIfUplinkInOctets": fsIfUplinkInOctets,
       "fsIfUplinkInUcastPkts": fsIfUplinkInUcastPkts,
       "fsIfUplinkInNUcastPkts": fsIfUplinkInNUcastPkts,
       "fsIfUplinkInDiscards": fsIfUplinkInDiscards,
       "fsIfUplinkInErrors": fsIfUplinkInErrors,
       "fsIfUplinkOutOctets": fsIfUplinkOutOctets,
       "fsIfUplinkOutUcastPkts": fsIfUplinkOutUcastPkts,
       "fsIfUplinkOutNUcastPkts": fsIfUplinkOutNUcastPkts,
       "fsIfUplinkOutDiscards": fsIfUplinkOutDiscards,
       "fsIfUplinkOutErrors": fsIfUplinkOutErrors,
       "fsIfDownlinkInOctets": fsIfDownlinkInOctets,
       "fsIfDownlinkInUcastPkts": fsIfDownlinkInUcastPkts,
       "fsIfDownlinkInNUcastPkts": fsIfDownlinkInNUcastPkts,
       "fsIfDownlinkInDiscards": fsIfDownlinkInDiscards,
       "fsIfDownlinkInErrors": fsIfDownlinkInErrors,
       "fsIfDownlinkOutOctets": fsIfDownlinkOutOctets,
       "fsIfDownlinkOutUcastPkts": fsIfDownlinkOutUcastPkts,
       "fsIfDownlinkOutNUcastPkts": fsIfDownlinkOutNUcastPkts,
       "fsIfDownlinkOutDiscards": fsIfDownlinkOutDiscards,
       "fsIfDownlinkOutErrors": fsIfDownlinkOutErrors,
       "fsIfUplinkInBcastPkts": fsIfUplinkInBcastPkts,
       "fsIfUplinkOutBcastPkts": fsIfUplinkOutBcastPkts,
       "fsIfDownlinkInBcastPkts": fsIfDownlinkInBcastPkts,
       "fsIfDownlinkOutBcastPkts": fsIfDownlinkOutBcastPkts,
       "fsIfTrafficStatisticsObjects": fsIfTrafficStatisticsObjects,
       "fsIfLinkTrafficStatistics": fsIfLinkTrafficStatistics,
       "fsIfLinkTrafficTable": fsIfLinkTrafficTable,
       "fsIfLinkTrafficEntry": fsIfLinkTrafficEntry,
       "fsIfLinkTrafficIndex": fsIfLinkTrafficIndex,
       "fsIfLinkAvgRate": fsIfLinkAvgRate,
       "fsIfLinkPeakRate": fsIfLinkPeakRate,
       "fsIfLinkAvgBWUtilization": fsIfLinkAvgBWUtilization,
       "fsIfLinkPeakBWUtilization": fsIfLinkPeakBWUtilization,
       "fsIfLinkQosStatistics": fsIfLinkQosStatistics,
       "fsLinkQosCtlTable": fsLinkQosCtlTable,
       "fsLinkQosCtlEntry": fsLinkQosCtlEntry,
       "fsLinkQosCtlOwnerIndex": fsLinkQosCtlOwnerIndex,
       "fsLinkQosCtlTestName": fsLinkQosCtlTestName,
       "fsLinkQosCtlTargetAddressType": fsLinkQosCtlTargetAddressType,
       "fsLinkQosCtlTargetAddress": fsLinkQosCtlTargetAddress,
       "fsLinkQosCtlAdminStatus": fsLinkQosCtlAdminStatus,
       "fsLinkQosCtlRowStatus": fsLinkQosCtlRowStatus,
       "fsLinkQosResultsTable": fsLinkQosResultsTable,
       "fsLinkQosResultsEntry": fsLinkQosResultsEntry,
       "fsLinkQosResultsOperStatus": fsLinkQosResultsOperStatus,
       "fsLinkQosResultsIpTargetAddressType": fsLinkQosResultsIpTargetAddressType,
       "fsLinkQosResultsIpTargetAddress": fsLinkQosResultsIpTargetAddress,
       "fsLinkQosResultsMaxRtt": fsLinkQosResultsMaxRtt,
       "fsLinkQosResultsMinRtt": fsLinkQosResultsMinRtt,
       "fsLinkQosResultsAverageRtt": fsLinkQosResultsAverageRtt,
       "fsLinkQosResultsDelayJitter": fsLinkQosResultsDelayJitter,
       "fsLinkQosResultsPktsLossRate": fsLinkQosResultsPktsLossRate,
       "fsLinkQosResultsNetworkAF": fsLinkQosResultsNetworkAF,
       "fsIfDeviceTrafficStatistics": fsIfDeviceTrafficStatistics,
       "fsIfDeviceTrafficTable": fsIfDeviceTrafficTable,
       "fsIfDeviceTrafficEntry": fsIfDeviceTrafficEntry,
       "fsIfDeviceTrafficIndex": fsIfDeviceTrafficIndex,
       "fsIfFC": fsIfFC,
       "fsIfFCTransRate": fsIfFCTransRate,
       "fsIfFCTransPktsNum": fsIfFCTransPktsNum,
       "fsIfFCDiscardRate": fsIfFCDiscardRate,
       "fsIfFCDiscardPktsNum": fsIfFCDiscardPktsNum,
       "fsIfFCPktsLossRate": fsIfFCPktsLossRate,
       "fsIfFCBandwidthRate": fsIfFCBandwidthRate,
       "fsIfFCBandwidthPercentage": fsIfFCBandwidthPercentage,
       "fsIfDeviceFCGathers": fsIfDeviceFCGathers,
       "fsIfFullMeshFCGathers": fsIfFullMeshFCGathers,
       "fsIfClassBasedGathers": fsIfClassBasedGathers,
       "fsIfNodeBasedGathers": fsIfNodeBasedGathers,
       "fsIfNodeClassBasedGathers": fsIfNodeClassBasedGathers,
       "fsIfNodeFCBasedGathers": fsIfNodeFCBasedGathers,
       "fsIfNodeDeviceFCBasedGathers": fsIfNodeDeviceFCBasedGathers,
       "fsIfPhyTable": fsIfPhyTable,
       "fsIfPhyEntry": fsIfPhyEntry,
       "fsIfPhyIndex": fsIfPhyIndex,
       "fsifPhyOperStatus": fsifPhyOperStatus,
       "fsIfPeakRateTable": fsIfPeakRateTable,
       "fsIfPeakRateEntry": fsIfPeakRateEntry,
       "fsIfPeakRateIndex": fsIfPeakRateIndex,
       "fsIfRxPeakRate": fsIfRxPeakRate,
       "fsIfRxPeakRateTime": fsIfRxPeakRateTime,
       "fsIfTxPeakRate": fsIfTxPeakRate,
       "fsIfTxPeakRateTime": fsIfTxPeakRateTime,
       "fsApInfoTable": fsApInfoTable,
       "fsApInfoEntry": fsApInfoEntry,
       "fsApInfoAddress": fsApInfoAddress,
       "fsApInfoWireInRate": fsApInfoWireInRate,
       "fsApInfoWireOutRate": fsApInfoWireOutRate,
       "fsApInfoWireInOctets": fsApInfoWireInOctets,
       "fsApInfoWireOutOctets": fsApInfoWireOutOctets,
       "fsIfDropTable": fsIfDropTable,
       "fsIfDropEntry": fsIfDropEntry,
       "fsIfDropIndex": fsIfDropIndex,
       "fsIfInDropPkts": fsIfInDropPkts,
       "fsIfInResLackPkts": fsIfInResLackPkts,
       "fsIfInQosDropPkts": fsIfInQosDropPkts,
       "fsIfFwdEntryDropPkts": fsIfFwdEntryDropPkts,
       "fsIfOutDropPkts": fsIfOutDropPkts,
       "fsIfOutResLackPkts": fsIfOutResLackPkts,
       "fsIfNoBufferConut": fsIfNoBufferConut,
       "fsIfOBMDropPkts": fsIfOBMDropPkts,
       "fsInterfaceTraps": fsInterfaceTraps,
       "lineDetectStatus": lineDetectStatus,
       "lineDetectPosition": lineDetectPosition,
       "lineQualityDetect": lineQualityDetect,
       "fsInterfaceMIBConformance": fsInterfaceMIBConformance,
       "fsInterfaceMIBCompliances": fsInterfaceMIBCompliances,
       "fsInterfaceMIBCompliance": fsInterfaceMIBCompliance,
       "fsInterfaceMIBGroups": fsInterfaceMIBGroups,
       "fsInterfaceMIBGroup": fsInterfaceMIBGroup,
       "fsPortTypeChooseMibGroup": fsPortTypeChooseMibGroup,
       "fsIfMTUMibGroup": fsIfMTUMibGroup,
       "fsIfLineDetectGroup": fsIfLineDetectGroup,
       "fsIfAvailableBWMibGroup": fsIfAvailableBWMibGroup}
)
