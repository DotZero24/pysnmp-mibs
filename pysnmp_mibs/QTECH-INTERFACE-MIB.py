# SNMP MIB module (QTECH-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-INTERFACE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:31 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10)
)
if mibBuilder.loadTexts:
    qtechInterfaceMIB.setRevisions(
        ("2010-02-01 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechIfConfigMIBObjects_ObjectIdentity = ObjectIdentity
qtechIfConfigMIBObjects = _QtechIfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1)
)
_QtechIfTable_Object = MibTable
qtechIfTable = _QtechIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIfTable.setStatus("current")
_QtechIfEntry_Object = MibTableRow
qtechIfEntry = _QtechIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1)
)
qtechIfEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIfEntry.setStatus("current")
_QtechIfIndex_Type = IfIndex
_QtechIfIndex_Object = MibTableColumn
qtechIfIndex = _QtechIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 1),
    _QtechIfIndex_Type()
)
qtechIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfIndex.setStatus("current")


class _QtechIfPortType_Type(Integer32):
    """Custom type qtechIfPortType based on Integer32"""
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
              62)
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
          ("portE1ELC", 62))
    )


_QtechIfPortType_Type.__name__ = "Integer32"
_QtechIfPortType_Object = MibTableColumn
qtechIfPortType = _QtechIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 2),
    _QtechIfPortType_Type()
)
qtechIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfPortType.setStatus("current")


class _QtechIfFlowControlAdminStatus_Type(Integer32):
    """Custom type qtechIfFlowControlAdminStatus based on Integer32"""
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


_QtechIfFlowControlAdminStatus_Type.__name__ = "Integer32"
_QtechIfFlowControlAdminStatus_Object = MibTableColumn
qtechIfFlowControlAdminStatus = _QtechIfFlowControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 3),
    _QtechIfFlowControlAdminStatus_Type()
)
qtechIfFlowControlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfFlowControlAdminStatus.setStatus("current")
_QtechIfFlowControlOperStatus_Type = EnabledStatus
_QtechIfFlowControlOperStatus_Object = MibTableColumn
qtechIfFlowControlOperStatus = _QtechIfFlowControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 4),
    _QtechIfFlowControlOperStatus_Type()
)
qtechIfFlowControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFlowControlOperStatus.setStatus("current")


class _QtechIfAdminSpeed_Type(Integer32):
    """Custom type qtechIfAdminSpeed based on Integer32"""
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


_QtechIfAdminSpeed_Type.__name__ = "Integer32"
_QtechIfAdminSpeed_Object = MibTableColumn
qtechIfAdminSpeed = _QtechIfAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 5),
    _QtechIfAdminSpeed_Type()
)
qtechIfAdminSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfAdminSpeed.setStatus("current")


class _QtechIfAdminDuplex_Type(Integer32):
    """Custom type qtechIfAdminDuplex based on Integer32"""
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


_QtechIfAdminDuplex_Type.__name__ = "Integer32"
_QtechIfAdminDuplex_Object = MibTableColumn
qtechIfAdminDuplex = _QtechIfAdminDuplex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 6),
    _QtechIfAdminDuplex_Type()
)
qtechIfAdminDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfAdminDuplex.setStatus("current")


class _QtechIfOperSpeed_Type(Integer32):
    """Custom type qtechIfOperSpeed based on Integer32"""
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


_QtechIfOperSpeed_Type.__name__ = "Integer32"
_QtechIfOperSpeed_Object = MibTableColumn
qtechIfOperSpeed = _QtechIfOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 7),
    _QtechIfOperSpeed_Type()
)
qtechIfOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfOperSpeed.setStatus("current")


class _QtechIfOperDuplex_Type(Integer32):
    """Custom type qtechIfOperDuplex based on Integer32"""
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


_QtechIfOperDuplex_Type.__name__ = "Integer32"
_QtechIfOperDuplex_Object = MibTableColumn
qtechIfOperDuplex = _QtechIfOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 8),
    _QtechIfOperDuplex_Type()
)
qtechIfOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfOperDuplex.setStatus("current")


class _QtechIfManageStatus_Type(EnabledStatus):
    """Custom type qtechIfManageStatus based on EnabledStatus"""
    defaultValue = 1


_QtechIfManageStatus_Type.__name__ = "EnabledStatus"
_QtechIfManageStatus_Object = MibTableColumn
qtechIfManageStatus = _QtechIfManageStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 9),
    _QtechIfManageStatus_Type()
)
qtechIfManageStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfManageStatus.setStatus("current")
_QtechIfIpBroadcast_Type = IpAddress
_QtechIfIpBroadcast_Object = MibTableColumn
qtechIfIpBroadcast = _QtechIfIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 10),
    _QtechIfIpBroadcast_Type()
)
qtechIfIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfIpBroadcast.setStatus("current")


class _QtechIfLayer_Type(Integer32):
    """Custom type qtechIfLayer based on Integer32"""
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


_QtechIfLayer_Type.__name__ = "Integer32"
_QtechIfLayer_Object = MibTableColumn
qtechIfLayer = _QtechIfLayer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 11),
    _QtechIfLayer_Type()
)
qtechIfLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfLayer.setStatus("current")


class _QtechIfMode_Type(Integer32):
    """Custom type qtechIfMode based on Integer32"""
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


_QtechIfMode_Type.__name__ = "Integer32"
_QtechIfMode_Object = MibTableColumn
qtechIfMode = _QtechIfMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 12),
    _QtechIfMode_Type()
)
qtechIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfMode.setStatus("current")
_QtechIfCounterClear_Type = Integer32
_QtechIfCounterClear_Object = MibTableColumn
qtechIfCounterClear = _QtechIfCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 13),
    _QtechIfCounterClear_Type()
)
qtechIfCounterClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfCounterClear.setStatus("current")
_QtechIfEntryStatus_Type = ConfigStatus
_QtechIfEntryStatus_Object = MibTableColumn
qtechIfEntryStatus = _QtechIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 14),
    _QtechIfEntryStatus_Type()
)
qtechIfEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfEntryStatus.setStatus("current")


class _QtechIfMediumType_Type(Integer32):
    """Custom type qtechIfMediumType based on Integer32"""
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


_QtechIfMediumType_Type.__name__ = "Integer32"
_QtechIfMediumType_Object = MibTableColumn
qtechIfMediumType = _QtechIfMediumType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 15),
    _QtechIfMediumType_Type()
)
qtechIfMediumType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfMediumType.setStatus("current")
_QtechIfDownCounter_Type = Counter32
_QtechIfDownCounter_Object = MibTableColumn
qtechIfDownCounter = _QtechIfDownCounter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 16),
    _QtechIfDownCounter_Type()
)
qtechIfDownCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownCounter.setStatus("current")
_QtechIfInOctets_Type = Counter64
_QtechIfInOctets_Object = MibTableColumn
qtechIfInOctets = _QtechIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 17),
    _QtechIfInOctets_Type()
)
qtechIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfInOctets.setStatus("current")
_QtechIfOutOctets_Type = Counter64
_QtechIfOutOctets_Object = MibTableColumn
qtechIfOutOctets = _QtechIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 18),
    _QtechIfOutOctets_Type()
)
qtechIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfOutOctets.setStatus("current")
_QtechIfBcastInhibit_Type = Integer32
_QtechIfBcastInhibit_Object = MibTableColumn
qtechIfBcastInhibit = _QtechIfBcastInhibit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 19),
    _QtechIfBcastInhibit_Type()
)
qtechIfBcastInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfBcastInhibit.setStatus("current")


class _QtechIfNegotiation_Type(Integer32):
    """Custom type qtechIfNegotiation based on Integer32"""
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


_QtechIfNegotiation_Type.__name__ = "Integer32"
_QtechIfNegotiation_Object = MibTableColumn
qtechIfNegotiation = _QtechIfNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 20),
    _QtechIfNegotiation_Type()
)
qtechIfNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfNegotiation.setStatus("current")
_QtechIfPhysAddress_Type = MacAddress
_QtechIfPhysAddress_Object = MibTableColumn
qtechIfPhysAddress = _QtechIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 21),
    _QtechIfPhysAddress_Type()
)
qtechIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfPhysAddress.setStatus("current")


class _QtechIfAdminSpeedRW_Type(Integer32):
    """Custom type qtechIfAdminSpeedRW based on Integer32"""
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


_QtechIfAdminSpeedRW_Type.__name__ = "Integer32"
_QtechIfAdminSpeedRW_Object = MibTableColumn
qtechIfAdminSpeedRW = _QtechIfAdminSpeedRW_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 22),
    _QtechIfAdminSpeedRW_Type()
)
qtechIfAdminSpeedRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfAdminSpeedRW.setStatus("current")


class _QtechIfAdminDuplexRW_Type(Integer32):
    """Custom type qtechIfAdminDuplexRW based on Integer32"""
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


_QtechIfAdminDuplexRW_Type.__name__ = "Integer32"
_QtechIfAdminDuplexRW_Object = MibTableColumn
qtechIfAdminDuplexRW = _QtechIfAdminDuplexRW_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 23),
    _QtechIfAdminDuplexRW_Type()
)
qtechIfAdminDuplexRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfAdminDuplexRW.setStatus("current")


class _QtechIfModeRW_Type(Integer32):
    """Custom type qtechIfModeRW based on Integer32"""
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


_QtechIfModeRW_Type.__name__ = "Integer32"
_QtechIfModeRW_Object = MibTableColumn
qtechIfModeRW = _QtechIfModeRW_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 24),
    _QtechIfModeRW_Type()
)
qtechIfModeRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfModeRW.setStatus("current")
_QtechIfSpeed_Type = Gauge32
_QtechIfSpeed_Object = MibTableColumn
qtechIfSpeed = _QtechIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 25),
    _QtechIfSpeed_Type()
)
qtechIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfSpeed.setStatus("current")


class _QtechifAdminStatus_Type(Integer32):
    """Custom type qtechifAdminStatus based on Integer32"""
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


_QtechifAdminStatus_Type.__name__ = "Integer32"
_QtechifAdminStatus_Object = MibTableColumn
qtechifAdminStatus = _QtechifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 26),
    _QtechifAdminStatus_Type()
)
qtechifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechifAdminStatus.setStatus("current")


class _QtechifOperStatus_Type(Integer32):
    """Custom type qtechifOperStatus based on Integer32"""
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


_QtechifOperStatus_Type.__name__ = "Integer32"
_QtechifOperStatus_Object = MibTableColumn
qtechifOperStatus = _QtechifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 27),
    _QtechifOperStatus_Type()
)
qtechifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechifOperStatus.setStatus("current")
_QtechIfInNUcastPkts_Type = Counter64
_QtechIfInNUcastPkts_Object = MibTableColumn
qtechIfInNUcastPkts = _QtechIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 28),
    _QtechIfInNUcastPkts_Type()
)
qtechIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfInNUcastPkts.setStatus("current")
_QtechIfOutNUcastPkts_Type = Counter64
_QtechIfOutNUcastPkts_Object = MibTableColumn
qtechIfOutNUcastPkts = _QtechIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 29),
    _QtechIfOutNUcastPkts_Type()
)
qtechIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfOutNUcastPkts.setStatus("current")
_QtechIfUpDownTimes_Type = Counter32
_QtechIfUpDownTimes_Object = MibTableColumn
qtechIfUpDownTimes = _QtechIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 30),
    _QtechIfUpDownTimes_Type()
)
qtechIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUpDownTimes.setStatus("current")


class _QtechifAdminStatusw_Type(Integer32):
    """Custom type qtechifAdminStatusw based on Integer32"""
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


_QtechifAdminStatusw_Type.__name__ = "Integer32"
_QtechifAdminStatusw_Object = MibTableColumn
qtechifAdminStatusw = _QtechifAdminStatusw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 31),
    _QtechifAdminStatusw_Type()
)
qtechifAdminStatusw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechifAdminStatusw.setStatus("current")


class _QtechifOperStatusw_Type(Integer32):
    """Custom type qtechifOperStatusw based on Integer32"""
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


_QtechifOperStatusw_Type.__name__ = "Integer32"
_QtechifOperStatusw_Object = MibTableColumn
qtechifOperStatusw = _QtechifOperStatusw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 32),
    _QtechifOperStatusw_Type()
)
qtechifOperStatusw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechifOperStatusw.setStatus("current")
_QtechifSpeedw_Type = Integer32
_QtechifSpeedw_Object = MibTableColumn
qtechifSpeedw = _QtechifSpeedw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 33),
    _QtechifSpeedw_Type()
)
qtechifSpeedw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechifSpeedw.setStatus("current")
_QtechifMacAddress_Type = MacAddress
_QtechifMacAddress_Object = MibTableColumn
qtechifMacAddress = _QtechifMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 34),
    _QtechifMacAddress_Type()
)
qtechifMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechifMacAddress.setStatus("current")
_QtechifLastChange_Type = TimeTicks
_QtechifLastChange_Object = MibTableColumn
qtechifLastChange = _QtechifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 35),
    _QtechifLastChange_Type()
)
qtechifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechifLastChange.setStatus("current")
_QtechIfInPkts_Type = Counter64
_QtechIfInPkts_Object = MibTableColumn
qtechIfInPkts = _QtechIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 36),
    _QtechIfInPkts_Type()
)
qtechIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfInPkts.setStatus("current")
_QtechIfDiscard_Type = Counter64
_QtechIfDiscard_Object = MibTableColumn
qtechIfDiscard = _QtechIfDiscard_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 37),
    _QtechIfDiscard_Type()
)
qtechIfDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDiscard.setStatus("current")
_QtechIfBandwidthUsage_Type = DisplayString
_QtechIfBandwidthUsage_Object = MibTableColumn
qtechIfBandwidthUsage = _QtechIfBandwidthUsage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 38),
    _QtechIfBandwidthUsage_Type()
)
qtechIfBandwidthUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfBandwidthUsage.setStatus("current")
_QtechIfInBitsRate_Type = Counter64
_QtechIfInBitsRate_Object = MibTableColumn
qtechIfInBitsRate = _QtechIfInBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 39),
    _QtechIfInBitsRate_Type()
)
qtechIfInBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfInBitsRate.setStatus("current")
_QtechIfInPktRate_Type = Counter64
_QtechIfInPktRate_Object = MibTableColumn
qtechIfInPktRate = _QtechIfInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 40),
    _QtechIfInPktRate_Type()
)
qtechIfInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfInPktRate.setStatus("current")
_QtechIfOutBitsRate_Type = Counter64
_QtechIfOutBitsRate_Object = MibTableColumn
qtechIfOutBitsRate = _QtechIfOutBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 41),
    _QtechIfOutBitsRate_Type()
)
qtechIfOutBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfOutBitsRate.setStatus("current")
_QtechIfOutPktRate_Type = Counter64
_QtechIfOutPktRate_Object = MibTableColumn
qtechIfOutPktRate = _QtechIfOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 1, 1, 42),
    _QtechIfOutPktRate_Type()
)
qtechIfOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfOutPktRate.setStatus("current")
_QtechIfIpTable_Object = MibTable
qtechIfIpTable = _QtechIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    qtechIfIpTable.setStatus("current")
_QtechIfIpEntry_Object = MibTableRow
qtechIfIpEntry = _QtechIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2, 1)
)
qtechIfIpEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfIpIfIndex"),
    (0, "QTECH-INTERFACE-MIB", "qtechIfIpId"),
    (0, "QTECH-INTERFACE-MIB", "qtechIfIp"),
)
if mibBuilder.loadTexts:
    qtechIfIpEntry.setStatus("current")
_QtechIfIpIfIndex_Type = IfIndex
_QtechIfIpIfIndex_Object = MibTableColumn
qtechIfIpIfIndex = _QtechIfIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2, 1, 1),
    _QtechIfIpIfIndex_Type()
)
qtechIfIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfIpIfIndex.setStatus("current")


class _QtechIfIpId_Type(Integer32):
    """Custom type qtechIfIpId based on Integer32"""
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


_QtechIfIpId_Type.__name__ = "Integer32"
_QtechIfIpId_Object = MibTableColumn
qtechIfIpId = _QtechIfIpId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2, 1, 2),
    _QtechIfIpId_Type()
)
qtechIfIpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfIpId.setStatus("current")
_QtechIfIp_Type = IpAddress
_QtechIfIp_Object = MibTableColumn
qtechIfIp = _QtechIfIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2, 1, 3),
    _QtechIfIp_Type()
)
qtechIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfIp.setStatus("current")
_QtechIfIpMask_Type = IpAddress
_QtechIfIpMask_Object = MibTableColumn
qtechIfIpMask = _QtechIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2, 1, 4),
    _QtechIfIpMask_Type()
)
qtechIfIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfIpMask.setStatus("current")
_QtechIfIpEntryStatus_Type = RowStatus
_QtechIfIpEntryStatus_Object = MibTableColumn
qtechIfIpEntryStatus = _QtechIfIpEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 2, 1, 5),
    _QtechIfIpEntryStatus_Type()
)
qtechIfIpEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechIfIpEntryStatus.setStatus("current")
_QtechIfStatusTable_Object = MibTable
qtechIfStatusTable = _QtechIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    qtechIfStatusTable.setStatus("current")
_QtechIfStatusEntry_Object = MibTableRow
qtechIfStatusEntry = _QtechIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 3, 1)
)
qtechIfStatusEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfStatusIndex"),
)
if mibBuilder.loadTexts:
    qtechIfStatusEntry.setStatus("current")
_QtechIfStatusIndex_Type = IfIndex
_QtechIfStatusIndex_Object = MibTableColumn
qtechIfStatusIndex = _QtechIfStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 3, 1, 1),
    _QtechIfStatusIndex_Type()
)
qtechIfStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfStatusIndex.setStatus("current")
_QtechIfStatusLoopBackExamine_Type = Integer32
_QtechIfStatusLoopBackExamine_Object = MibTableColumn
qtechIfStatusLoopBackExamine = _QtechIfStatusLoopBackExamine_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 3, 1, 2),
    _QtechIfStatusLoopBackExamine_Type()
)
qtechIfStatusLoopBackExamine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfStatusLoopBackExamine.setStatus("current")


class _QtechIfErrorStatus_Type(Integer32):
    """Custom type qtechIfErrorStatus based on Integer32"""
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


_QtechIfErrorStatus_Type.__name__ = "Integer32"
_QtechIfErrorStatus_Object = MibTableColumn
qtechIfErrorStatus = _QtechIfErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 3, 1, 3),
    _QtechIfErrorStatus_Type()
)
qtechIfErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfErrorStatus.setStatus("current")
_QtechIfLineDetect_Type = Integer32
_QtechIfLineDetect_Object = MibTableColumn
qtechIfLineDetect = _QtechIfLineDetect_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 3, 1, 4),
    _QtechIfLineDetect_Type()
)
qtechIfLineDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLineDetect.setStatus("current")
_QtechGlobalIfDisableRecovery_Type = Integer32
_QtechGlobalIfDisableRecovery_Object = MibScalar
qtechGlobalIfDisableRecovery = _QtechGlobalIfDisableRecovery_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 4),
    _QtechGlobalIfDisableRecovery_Type()
)
qtechGlobalIfDisableRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalIfDisableRecovery.setStatus("current")
_QtechPortTypeChooseTable_Object = MibTable
qtechPortTypeChooseTable = _QtechPortTypeChooseTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 5)
)
if mibBuilder.loadTexts:
    qtechPortTypeChooseTable.setStatus("current")
_QtechPortTypeChooseEntry_Object = MibTableRow
qtechPortTypeChooseEntry = _QtechPortTypeChooseEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 5, 1)
)
qtechPortTypeChooseEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechPortTypeChooseIndex"),
)
if mibBuilder.loadTexts:
    qtechPortTypeChooseEntry.setStatus("current")
_QtechPortTypeChooseIndex_Type = IfIndex
_QtechPortTypeChooseIndex_Object = MibTableColumn
qtechPortTypeChooseIndex = _QtechPortTypeChooseIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 5, 1, 1),
    _QtechPortTypeChooseIndex_Type()
)
qtechPortTypeChooseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPortTypeChooseIndex.setStatus("current")


class _QtechPortTypeChooseType_Type(Integer32):
    """Custom type qtechPortTypeChooseType based on Integer32"""
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


_QtechPortTypeChooseType_Type.__name__ = "Integer32"
_QtechPortTypeChooseType_Object = MibTableColumn
qtechPortTypeChooseType = _QtechPortTypeChooseType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 5, 1, 2),
    _QtechPortTypeChooseType_Type()
)
qtechPortTypeChooseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPortTypeChooseType.setStatus("current")
_QtechIfMTUTable_Object = MibTable
qtechIfMTUTable = _QtechIfMTUTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 6)
)
if mibBuilder.loadTexts:
    qtechIfMTUTable.setStatus("current")
_QtechIfMTUEntry_Object = MibTableRow
qtechIfMTUEntry = _QtechIfMTUEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 6, 1)
)
qtechIfMTUEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfMTUIndex"),
)
if mibBuilder.loadTexts:
    qtechIfMTUEntry.setStatus("current")
_QtechIfMTUIndex_Type = IfIndex
_QtechIfMTUIndex_Object = MibTableColumn
qtechIfMTUIndex = _QtechIfMTUIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 6, 1, 1),
    _QtechIfMTUIndex_Type()
)
qtechIfMTUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfMTUIndex.setStatus("current")
_QtechIfMTU_Type = Integer32
_QtechIfMTU_Object = MibTableColumn
qtechIfMTU = _QtechIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 6, 1, 2),
    _QtechIfMTU_Type()
)
qtechIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfMTU.setStatus("current")
_QtechIfAvailableBWTable_Object = MibTable
qtechIfAvailableBWTable = _QtechIfAvailableBWTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 7)
)
if mibBuilder.loadTexts:
    qtechIfAvailableBWTable.setStatus("current")
_QtechIfAvailableBWEntry_Object = MibTableRow
qtechIfAvailableBWEntry = _QtechIfAvailableBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 7, 1)
)
qtechIfAvailableBWEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfAvailableBWIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIfAvailableBWEntry.setStatus("current")
_QtechIfAvailableBWIfIndex_Type = IfIndex
_QtechIfAvailableBWIfIndex_Object = MibTableColumn
qtechIfAvailableBWIfIndex = _QtechIfAvailableBWIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 7, 1, 1),
    _QtechIfAvailableBWIfIndex_Type()
)
qtechIfAvailableBWIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfAvailableBWIfIndex.setStatus("current")
_QtechIfAvailableBWIfBW_Type = Gauge32
_QtechIfAvailableBWIfBW_Object = MibTableColumn
qtechIfAvailableBWIfBW = _QtechIfAvailableBWIfBW_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 7, 1, 2),
    _QtechIfAvailableBWIfBW_Type()
)
qtechIfAvailableBWIfBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfAvailableBWIfBW.setStatus("current")
_QtechIfSVICreatTable_Object = MibTable
qtechIfSVICreatTable = _QtechIfSVICreatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 8)
)
if mibBuilder.loadTexts:
    qtechIfSVICreatTable.setStatus("current")
_QtechIfSVICreatEntry_Object = MibTableRow
qtechIfSVICreatEntry = _QtechIfSVICreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 8, 1)
)
qtechIfSVICreatEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfSVICreatVlanNum"),
)
if mibBuilder.loadTexts:
    qtechIfSVICreatEntry.setStatus("current")


class _QtechIfSVICreatVlanNum_Type(Integer32):
    """Custom type qtechIfSVICreatVlanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechIfSVICreatVlanNum_Type.__name__ = "Integer32"
_QtechIfSVICreatVlanNum_Object = MibTableColumn
qtechIfSVICreatVlanNum = _QtechIfSVICreatVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 8, 1, 1),
    _QtechIfSVICreatVlanNum_Type()
)
qtechIfSVICreatVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfSVICreatVlanNum.setStatus("current")


class _QtechIfHandleSVI_Type(Integer32):
    """Custom type qtechIfHandleSVI based on Integer32"""
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


_QtechIfHandleSVI_Type.__name__ = "Integer32"
_QtechIfHandleSVI_Object = MibTableColumn
qtechIfHandleSVI = _QtechIfHandleSVI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 8, 1, 2),
    _QtechIfHandleSVI_Type()
)
qtechIfHandleSVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfHandleSVI.setStatus("current")
_QtechIfPhyIntNum_Type = Integer32
_QtechIfPhyIntNum_Object = MibScalar
qtechIfPhyIntNum = _QtechIfPhyIntNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 9),
    _QtechIfPhyIntNum_Type()
)
qtechIfPhyIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfPhyIntNum.setStatus("current")
_QtechIfLinkUPTimesTable_Object = MibTable
qtechIfLinkUPTimesTable = _QtechIfLinkUPTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 10)
)
if mibBuilder.loadTexts:
    qtechIfLinkUPTimesTable.setStatus("current")
_QtechIfLinkUPTimesEntry_Object = MibTableRow
qtechIfLinkUPTimesEntry = _QtechIfLinkUPTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 10, 1)
)
qtechIfLinkUPTimesEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechInterfaceIndex"),
)
if mibBuilder.loadTexts:
    qtechIfLinkUPTimesEntry.setStatus("current")
_QtechInterfaceIndex_Type = Integer32
_QtechInterfaceIndex_Object = MibTableColumn
qtechInterfaceIndex = _QtechInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 10, 1, 1),
    _QtechInterfaceIndex_Type()
)
qtechInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechInterfaceIndex.setStatus("current")
_QtechIfLinkUPTimes_Type = Integer32
_QtechIfLinkUPTimes_Object = MibTableColumn
qtechIfLinkUPTimes = _QtechIfLinkUPTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 10, 1, 2),
    _QtechIfLinkUPTimes_Type()
)
qtechIfLinkUPTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkUPTimes.setStatus("current")
_QtechIfEncapsulationTable_Object = MibTable
qtechIfEncapsulationTable = _QtechIfEncapsulationTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 11)
)
if mibBuilder.loadTexts:
    qtechIfEncapsulationTable.setStatus("current")
_QtechIfEncapsulationEntry_Object = MibTableRow
qtechIfEncapsulationEntry = _QtechIfEncapsulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 11, 1)
)
qtechIfEncapsulationEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfEncapsulationIndex"),
)
if mibBuilder.loadTexts:
    qtechIfEncapsulationEntry.setStatus("current")
_QtechIfEncapsulationIndex_Type = IfIndex
_QtechIfEncapsulationIndex_Object = MibTableColumn
qtechIfEncapsulationIndex = _QtechIfEncapsulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 11, 1, 1),
    _QtechIfEncapsulationIndex_Type()
)
qtechIfEncapsulationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfEncapsulationIndex.setStatus("current")
_QtechIfEncapsulationVlan_Type = VlanId
_QtechIfEncapsulationVlan_Object = MibTableColumn
qtechIfEncapsulationVlan = _QtechIfEncapsulationVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 11, 1, 2),
    _QtechIfEncapsulationVlan_Type()
)
qtechIfEncapsulationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfEncapsulationVlan.setStatus("current")
_QtechApIfNumberTable_Object = MibTable
qtechApIfNumberTable = _QtechApIfNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 12)
)
if mibBuilder.loadTexts:
    qtechApIfNumberTable.setStatus("current")
_QtechApIfNumberEntry_Object = MibTableRow
qtechApIfNumberEntry = _QtechApIfNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 12, 1)
)
qtechApIfNumberEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechApPhyAddress"),
)
if mibBuilder.loadTexts:
    qtechApIfNumberEntry.setStatus("current")
_QtechApPhyAddress_Type = PhysAddress
_QtechApPhyAddress_Object = MibTableColumn
qtechApPhyAddress = _QtechApPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 12, 1, 1),
    _QtechApPhyAddress_Type()
)
qtechApPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApPhyAddress.setStatus("current")
_QtechApIfNumber_Type = Integer32
_QtechApIfNumber_Object = MibTableColumn
qtechApIfNumber = _QtechApIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 12, 1, 2),
    _QtechApIfNumber_Type()
)
qtechApIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfNumber.setStatus("current")
_QtechApIfPhyIntNum_Type = Integer32
_QtechApIfPhyIntNum_Object = MibTableColumn
qtechApIfPhyIntNum = _QtechApIfPhyIntNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 12, 1, 3),
    _QtechApIfPhyIntNum_Type()
)
qtechApIfPhyIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfPhyIntNum.setStatus("current")
_QtechApIfTable_Object = MibTable
qtechApIfTable = _QtechApIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13)
)
if mibBuilder.loadTexts:
    qtechApIfTable.setStatus("current")
_QtechApIfEntry_Object = MibTableRow
qtechApIfEntry = _QtechApIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1)
)
qtechApIfEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechApPhysAddress"),
    (0, "QTECH-INTERFACE-MIB", "qtechApIfIndex"),
)
if mibBuilder.loadTexts:
    qtechApIfEntry.setStatus("current")
_QtechApPhysAddress_Type = PhysAddress
_QtechApPhysAddress_Object = MibTableColumn
qtechApPhysAddress = _QtechApPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 1),
    _QtechApPhysAddress_Type()
)
qtechApPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApPhysAddress.setStatus("current")
_QtechApIfIndex_Type = IfIndex
_QtechApIfIndex_Object = MibTableColumn
qtechApIfIndex = _QtechApIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 2),
    _QtechApIfIndex_Type()
)
qtechApIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfIndex.setStatus("current")


class _QtechApIfDescr_Type(DisplayString):
    """Custom type qtechApIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechApIfDescr_Type.__name__ = "DisplayString"
_QtechApIfDescr_Object = MibTableColumn
qtechApIfDescr = _QtechApIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 3),
    _QtechApIfDescr_Type()
)
qtechApIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfDescr.setStatus("current")
_QtechApIfType_Type = IANAifType
_QtechApIfType_Object = MibTableColumn
qtechApIfType = _QtechApIfType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 4),
    _QtechApIfType_Type()
)
qtechApIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfType.setStatus("current")
_QtechApIfMtu_Type = Integer32
_QtechApIfMtu_Object = MibTableColumn
qtechApIfMtu = _QtechApIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 5),
    _QtechApIfMtu_Type()
)
qtechApIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfMtu.setStatus("current")
_QtechApIfSpeed_Type = Gauge32
_QtechApIfSpeed_Object = MibTableColumn
qtechApIfSpeed = _QtechApIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 6),
    _QtechApIfSpeed_Type()
)
qtechApIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfSpeed.setStatus("current")
_QtechApIfPhysAddress_Type = PhysAddress
_QtechApIfPhysAddress_Object = MibTableColumn
qtechApIfPhysAddress = _QtechApIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 7),
    _QtechApIfPhysAddress_Type()
)
qtechApIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfPhysAddress.setStatus("current")


class _QtechApIfAdminStatus_Type(Integer32):
    """Custom type qtechApIfAdminStatus based on Integer32"""
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


_QtechApIfAdminStatus_Type.__name__ = "Integer32"
_QtechApIfAdminStatus_Object = MibTableColumn
qtechApIfAdminStatus = _QtechApIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 8),
    _QtechApIfAdminStatus_Type()
)
qtechApIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApIfAdminStatus.setStatus("current")


class _QtechApIfOperStatus_Type(Integer32):
    """Custom type qtechApIfOperStatus based on Integer32"""
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


_QtechApIfOperStatus_Type.__name__ = "Integer32"
_QtechApIfOperStatus_Object = MibTableColumn
qtechApIfOperStatus = _QtechApIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 9),
    _QtechApIfOperStatus_Type()
)
qtechApIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOperStatus.setStatus("current")
_QtechApIfLastChange_Type = TimeTicks
_QtechApIfLastChange_Object = MibTableColumn
qtechApIfLastChange = _QtechApIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 10),
    _QtechApIfLastChange_Type()
)
qtechApIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfLastChange.setStatus("current")
_QtechApIfInOctets_Type = Counter64
_QtechApIfInOctets_Object = MibTableColumn
qtechApIfInOctets = _QtechApIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 11),
    _QtechApIfInOctets_Type()
)
qtechApIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInOctets.setStatus("current")
_QtechApIfInUcastPkts_Type = Counter64
_QtechApIfInUcastPkts_Object = MibTableColumn
qtechApIfInUcastPkts = _QtechApIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 12),
    _QtechApIfInUcastPkts_Type()
)
qtechApIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInUcastPkts.setStatus("current")
_QtechApIfInNUcastPkts_Type = Counter64
_QtechApIfInNUcastPkts_Object = MibTableColumn
qtechApIfInNUcastPkts = _QtechApIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 13),
    _QtechApIfInNUcastPkts_Type()
)
qtechApIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInNUcastPkts.setStatus("deprecated")
_QtechApIfInDiscards_Type = Counter32
_QtechApIfInDiscards_Object = MibTableColumn
qtechApIfInDiscards = _QtechApIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 14),
    _QtechApIfInDiscards_Type()
)
qtechApIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInDiscards.setStatus("current")
_QtechApIfInErrors_Type = Counter32
_QtechApIfInErrors_Object = MibTableColumn
qtechApIfInErrors = _QtechApIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 15),
    _QtechApIfInErrors_Type()
)
qtechApIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInErrors.setStatus("current")
_QtechApIfInUnknownProtos_Type = Counter32
_QtechApIfInUnknownProtos_Object = MibTableColumn
qtechApIfInUnknownProtos = _QtechApIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 16),
    _QtechApIfInUnknownProtos_Type()
)
qtechApIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInUnknownProtos.setStatus("current")
_QtechApIfOutOctets_Type = Counter64
_QtechApIfOutOctets_Object = MibTableColumn
qtechApIfOutOctets = _QtechApIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 17),
    _QtechApIfOutOctets_Type()
)
qtechApIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutOctets.setStatus("current")
_QtechApIfOutUcastPkts_Type = Counter64
_QtechApIfOutUcastPkts_Object = MibTableColumn
qtechApIfOutUcastPkts = _QtechApIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 18),
    _QtechApIfOutUcastPkts_Type()
)
qtechApIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutUcastPkts.setStatus("current")
_QtechApIfOutNUcastPkts_Type = Counter64
_QtechApIfOutNUcastPkts_Object = MibTableColumn
qtechApIfOutNUcastPkts = _QtechApIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 19),
    _QtechApIfOutNUcastPkts_Type()
)
qtechApIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutNUcastPkts.setStatus("deprecated")
_QtechApIfOutDiscards_Type = Counter32
_QtechApIfOutDiscards_Object = MibTableColumn
qtechApIfOutDiscards = _QtechApIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 20),
    _QtechApIfOutDiscards_Type()
)
qtechApIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutDiscards.setStatus("current")
_QtechApIfOutErrors_Type = Counter32
_QtechApIfOutErrors_Object = MibTableColumn
qtechApIfOutErrors = _QtechApIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 21),
    _QtechApIfOutErrors_Type()
)
qtechApIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutErrors.setStatus("current")
_QtechApIfOutQLen_Type = Gauge32
_QtechApIfOutQLen_Object = MibTableColumn
qtechApIfOutQLen = _QtechApIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 22),
    _QtechApIfOutQLen_Type()
)
qtechApIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutQLen.setStatus("deprecated")
_QtechApIfLinkUPTimes_Type = Integer32
_QtechApIfLinkUPTimes_Object = MibTableColumn
qtechApIfLinkUPTimes = _QtechApIfLinkUPTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 23),
    _QtechApIfLinkUPTimes_Type()
)
qtechApIfLinkUPTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfLinkUPTimes.setStatus("current")
_QtechApIfInDataOctets_Type = Counter64
_QtechApIfInDataOctets_Object = MibTableColumn
qtechApIfInDataOctets = _QtechApIfInDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 24),
    _QtechApIfInDataOctets_Type()
)
qtechApIfInDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInDataOctets.setStatus("current")
_QtechApIfOutDataOctets_Type = Counter64
_QtechApIfOutDataOctets_Object = MibTableColumn
qtechApIfOutDataOctets = _QtechApIfOutDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 25),
    _QtechApIfOutDataOctets_Type()
)
qtechApIfOutDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutDataOctets.setStatus("current")
_QtechApIfMgmtUploadOctets_Type = Counter32
_QtechApIfMgmtUploadOctets_Object = MibTableColumn
qtechApIfMgmtUploadOctets = _QtechApIfMgmtUploadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 26),
    _QtechApIfMgmtUploadOctets_Type()
)
qtechApIfMgmtUploadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfMgmtUploadOctets.setStatus("current")
_QtechApIfMgmtDownloadOctets_Type = Counter32
_QtechApIfMgmtDownloadOctets_Object = MibTableColumn
qtechApIfMgmtDownloadOctets = _QtechApIfMgmtDownloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 27),
    _QtechApIfMgmtDownloadOctets_Type()
)
qtechApIfMgmtDownloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfMgmtDownloadOctets.setStatus("current")
_QtechApIfSpeedw_Type = Integer32
_QtechApIfSpeedw_Object = MibTableColumn
qtechApIfSpeedw = _QtechApIfSpeedw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 28),
    _QtechApIfSpeedw_Type()
)
qtechApIfSpeedw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfSpeedw.setStatus("current")
_QtechApIfMtuw_Type = Integer32
_QtechApIfMtuw_Object = MibTableColumn
qtechApIfMtuw = _QtechApIfMtuw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 29),
    _QtechApIfMtuw_Type()
)
qtechApIfMtuw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfMtuw.setStatus("current")
_QtechApIfPhysAddressw_Type = MacAddress
_QtechApIfPhysAddressw_Object = MibTableColumn
qtechApIfPhysAddressw = _QtechApIfPhysAddressw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 30),
    _QtechApIfPhysAddressw_Type()
)
qtechApIfPhysAddressw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfPhysAddressw.setStatus("current")
_QtechApIfInUcastPktsw_Type = Counter32
_QtechApIfInUcastPktsw_Object = MibTableColumn
qtechApIfInUcastPktsw = _QtechApIfInUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 31),
    _QtechApIfInUcastPktsw_Type()
)
qtechApIfInUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInUcastPktsw.setStatus("current")
_QtechApIfInNUcastPktsw_Type = Counter32
_QtechApIfInNUcastPktsw_Object = MibTableColumn
qtechApIfInNUcastPktsw = _QtechApIfInNUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 32),
    _QtechApIfInNUcastPktsw_Type()
)
qtechApIfInNUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInNUcastPktsw.setStatus("deprecated")
_QtechApIfOutUcastPktsw_Type = Counter32
_QtechApIfOutUcastPktsw_Object = MibTableColumn
qtechApIfOutUcastPktsw = _QtechApIfOutUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 33),
    _QtechApIfOutUcastPktsw_Type()
)
qtechApIfOutUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutUcastPktsw.setStatus("current")
_QtechApIfOutNUcastPktsw_Type = Counter32
_QtechApIfOutNUcastPktsw_Object = MibTableColumn
qtechApIfOutNUcastPktsw = _QtechApIfOutNUcastPktsw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 34),
    _QtechApIfOutNUcastPktsw_Type()
)
qtechApIfOutNUcastPktsw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfOutNUcastPktsw.setStatus("deprecated")
_QtechApIfLinkUPTimesw_Type = Counter32
_QtechApIfLinkUPTimesw_Object = MibTableColumn
qtechApIfLinkUPTimesw = _QtechApIfLinkUPTimesw_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 35),
    _QtechApIfLinkUPTimesw_Type()
)
qtechApIfLinkUPTimesw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfLinkUPTimesw.setStatus("current")
_QtechApIfInPkts_Type = Counter64
_QtechApIfInPkts_Object = MibTableColumn
qtechApIfInPkts = _QtechApIfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 13, 1, 36),
    _QtechApIfInPkts_Type()
)
qtechApIfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIfInPkts.setStatus("current")
_QtechIfLinkTable_Object = MibTable
qtechIfLinkTable = _QtechIfLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14)
)
if mibBuilder.loadTexts:
    qtechIfLinkTable.setStatus("current")
_QtechIfLinkEntry_Object = MibTableRow
qtechIfLinkEntry = _QtechIfLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1)
)
qtechIfLinkEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfLinkIndex"),
)
if mibBuilder.loadTexts:
    qtechIfLinkEntry.setStatus("current")
_QtechIfLinkIndex_Type = IfIndex
_QtechIfLinkIndex_Object = MibTableColumn
qtechIfLinkIndex = _QtechIfLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 1),
    _QtechIfLinkIndex_Type()
)
qtechIfLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkIndex.setStatus("current")
_QtechIfUplinkInOctets_Type = Counter32
_QtechIfUplinkInOctets_Object = MibTableColumn
qtechIfUplinkInOctets = _QtechIfUplinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 2),
    _QtechIfUplinkInOctets_Type()
)
qtechIfUplinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkInOctets.setStatus("current")
_QtechIfUplinkInUcastPkts_Type = Counter32
_QtechIfUplinkInUcastPkts_Object = MibTableColumn
qtechIfUplinkInUcastPkts = _QtechIfUplinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 3),
    _QtechIfUplinkInUcastPkts_Type()
)
qtechIfUplinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkInUcastPkts.setStatus("current")
_QtechIfUplinkInNUcastPkts_Type = Counter32
_QtechIfUplinkInNUcastPkts_Object = MibTableColumn
qtechIfUplinkInNUcastPkts = _QtechIfUplinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 4),
    _QtechIfUplinkInNUcastPkts_Type()
)
qtechIfUplinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkInNUcastPkts.setStatus("deprecated")
_QtechIfUplinkInDiscards_Type = Counter32
_QtechIfUplinkInDiscards_Object = MibTableColumn
qtechIfUplinkInDiscards = _QtechIfUplinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 5),
    _QtechIfUplinkInDiscards_Type()
)
qtechIfUplinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkInDiscards.setStatus("current")
_QtechIfUplinkInErrors_Type = Counter32
_QtechIfUplinkInErrors_Object = MibTableColumn
qtechIfUplinkInErrors = _QtechIfUplinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 6),
    _QtechIfUplinkInErrors_Type()
)
qtechIfUplinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkInErrors.setStatus("current")
_QtechIfUplinkOutOctets_Type = Counter32
_QtechIfUplinkOutOctets_Object = MibTableColumn
qtechIfUplinkOutOctets = _QtechIfUplinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 7),
    _QtechIfUplinkOutOctets_Type()
)
qtechIfUplinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkOutOctets.setStatus("current")
_QtechIfUplinkOutUcastPkts_Type = Counter32
_QtechIfUplinkOutUcastPkts_Object = MibTableColumn
qtechIfUplinkOutUcastPkts = _QtechIfUplinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 8),
    _QtechIfUplinkOutUcastPkts_Type()
)
qtechIfUplinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkOutUcastPkts.setStatus("current")
_QtechIfUplinkOutNUcastPkts_Type = Counter32
_QtechIfUplinkOutNUcastPkts_Object = MibTableColumn
qtechIfUplinkOutNUcastPkts = _QtechIfUplinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 9),
    _QtechIfUplinkOutNUcastPkts_Type()
)
qtechIfUplinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkOutNUcastPkts.setStatus("deprecated")
_QtechIfUplinkOutDiscards_Type = Counter32
_QtechIfUplinkOutDiscards_Object = MibTableColumn
qtechIfUplinkOutDiscards = _QtechIfUplinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 10),
    _QtechIfUplinkOutDiscards_Type()
)
qtechIfUplinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkOutDiscards.setStatus("current")
_QtechIfUplinkOutErrors_Type = Counter32
_QtechIfUplinkOutErrors_Object = MibTableColumn
qtechIfUplinkOutErrors = _QtechIfUplinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 11),
    _QtechIfUplinkOutErrors_Type()
)
qtechIfUplinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkOutErrors.setStatus("current")
_QtechIfDownlinkInOctets_Type = Counter32
_QtechIfDownlinkInOctets_Object = MibTableColumn
qtechIfDownlinkInOctets = _QtechIfDownlinkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 12),
    _QtechIfDownlinkInOctets_Type()
)
qtechIfDownlinkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkInOctets.setStatus("current")
_QtechIfDownlinkInUcastPkts_Type = Counter32
_QtechIfDownlinkInUcastPkts_Object = MibTableColumn
qtechIfDownlinkInUcastPkts = _QtechIfDownlinkInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 13),
    _QtechIfDownlinkInUcastPkts_Type()
)
qtechIfDownlinkInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkInUcastPkts.setStatus("current")
_QtechIfDownlinkInNUcastPkts_Type = Counter32
_QtechIfDownlinkInNUcastPkts_Object = MibTableColumn
qtechIfDownlinkInNUcastPkts = _QtechIfDownlinkInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 14),
    _QtechIfDownlinkInNUcastPkts_Type()
)
qtechIfDownlinkInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkInNUcastPkts.setStatus("deprecated")
_QtechIfDownlinkInDiscards_Type = Counter32
_QtechIfDownlinkInDiscards_Object = MibTableColumn
qtechIfDownlinkInDiscards = _QtechIfDownlinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 15),
    _QtechIfDownlinkInDiscards_Type()
)
qtechIfDownlinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkInDiscards.setStatus("current")
_QtechIfDownlinkInErrors_Type = Counter32
_QtechIfDownlinkInErrors_Object = MibTableColumn
qtechIfDownlinkInErrors = _QtechIfDownlinkInErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 16),
    _QtechIfDownlinkInErrors_Type()
)
qtechIfDownlinkInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkInErrors.setStatus("current")
_QtechIfDownlinkOutOctets_Type = Counter32
_QtechIfDownlinkOutOctets_Object = MibTableColumn
qtechIfDownlinkOutOctets = _QtechIfDownlinkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 17),
    _QtechIfDownlinkOutOctets_Type()
)
qtechIfDownlinkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkOutOctets.setStatus("current")
_QtechIfDownlinkOutUcastPkts_Type = Counter32
_QtechIfDownlinkOutUcastPkts_Object = MibTableColumn
qtechIfDownlinkOutUcastPkts = _QtechIfDownlinkOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 18),
    _QtechIfDownlinkOutUcastPkts_Type()
)
qtechIfDownlinkOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkOutUcastPkts.setStatus("current")
_QtechIfDownlinkOutNUcastPkts_Type = Counter32
_QtechIfDownlinkOutNUcastPkts_Object = MibTableColumn
qtechIfDownlinkOutNUcastPkts = _QtechIfDownlinkOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 19),
    _QtechIfDownlinkOutNUcastPkts_Type()
)
qtechIfDownlinkOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkOutNUcastPkts.setStatus("deprecated")
_QtechIfDownlinkOutDiscards_Type = Counter32
_QtechIfDownlinkOutDiscards_Object = MibTableColumn
qtechIfDownlinkOutDiscards = _QtechIfDownlinkOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 20),
    _QtechIfDownlinkOutDiscards_Type()
)
qtechIfDownlinkOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkOutDiscards.setStatus("current")
_QtechIfDownlinkOutErrors_Type = Counter32
_QtechIfDownlinkOutErrors_Object = MibTableColumn
qtechIfDownlinkOutErrors = _QtechIfDownlinkOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 21),
    _QtechIfDownlinkOutErrors_Type()
)
qtechIfDownlinkOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkOutErrors.setStatus("current")
_QtechIfUplinkInBcastPkts_Type = Counter64
_QtechIfUplinkInBcastPkts_Object = MibTableColumn
qtechIfUplinkInBcastPkts = _QtechIfUplinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 22),
    _QtechIfUplinkInBcastPkts_Type()
)
qtechIfUplinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkInBcastPkts.setStatus("current")
_QtechIfUplinkOutBcastPkts_Type = Counter64
_QtechIfUplinkOutBcastPkts_Object = MibTableColumn
qtechIfUplinkOutBcastPkts = _QtechIfUplinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 23),
    _QtechIfUplinkOutBcastPkts_Type()
)
qtechIfUplinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfUplinkOutBcastPkts.setStatus("current")
_QtechIfDownlinkInBcastPkts_Type = Counter64
_QtechIfDownlinkInBcastPkts_Object = MibTableColumn
qtechIfDownlinkInBcastPkts = _QtechIfDownlinkInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 24),
    _QtechIfDownlinkInBcastPkts_Type()
)
qtechIfDownlinkInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkInBcastPkts.setStatus("current")
_QtechIfDownlinkOutBcastPkts_Type = Counter64
_QtechIfDownlinkOutBcastPkts_Object = MibTableColumn
qtechIfDownlinkOutBcastPkts = _QtechIfDownlinkOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 14, 1, 25),
    _QtechIfDownlinkOutBcastPkts_Type()
)
qtechIfDownlinkOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDownlinkOutBcastPkts.setStatus("current")
_QtechIfTrafficStatisticsObjects_ObjectIdentity = ObjectIdentity
qtechIfTrafficStatisticsObjects = _QtechIfTrafficStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15)
)
_QtechIfLinkTrafficStatistics_ObjectIdentity = ObjectIdentity
qtechIfLinkTrafficStatistics = _QtechIfLinkTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1)
)
_QtechIfLinkTrafficTable_Object = MibTable
qtechIfLinkTrafficTable = _QtechIfLinkTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIfLinkTrafficTable.setStatus("current")
_QtechIfLinkTrafficEntry_Object = MibTableRow
qtechIfLinkTrafficEntry = _QtechIfLinkTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1)
)
qtechIfLinkTrafficEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfLinkTrafficIndex"),
)
if mibBuilder.loadTexts:
    qtechIfLinkTrafficEntry.setStatus("current")
_QtechIfLinkTrafficIndex_Type = Unsigned32
_QtechIfLinkTrafficIndex_Object = MibTableColumn
qtechIfLinkTrafficIndex = _QtechIfLinkTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 1),
    _QtechIfLinkTrafficIndex_Type()
)
qtechIfLinkTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkTrafficIndex.setStatus("current")


class _QtechIfLinkAvgRate_Type(Counter32):
    """Custom type qtechIfLinkAvgRate based on Counter32"""
    defaultValue = 0


_QtechIfLinkAvgRate_Type.__name__ = "Counter32"
_QtechIfLinkAvgRate_Object = MibTableColumn
qtechIfLinkAvgRate = _QtechIfLinkAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 2),
    _QtechIfLinkAvgRate_Type()
)
qtechIfLinkAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkAvgRate.setStatus("current")


class _QtechIfLinkPeakRate_Type(Counter32):
    """Custom type qtechIfLinkPeakRate based on Counter32"""
    defaultValue = 0


_QtechIfLinkPeakRate_Type.__name__ = "Counter32"
_QtechIfLinkPeakRate_Object = MibTableColumn
qtechIfLinkPeakRate = _QtechIfLinkPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 3),
    _QtechIfLinkPeakRate_Type()
)
qtechIfLinkPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkPeakRate.setStatus("current")


class _QtechIfLinkAvgBWUtilization_Type(Integer32):
    """Custom type qtechIfLinkAvgBWUtilization based on Integer32"""
    defaultValue = 0


_QtechIfLinkAvgBWUtilization_Type.__name__ = "Integer32"
_QtechIfLinkAvgBWUtilization_Object = MibTableColumn
qtechIfLinkAvgBWUtilization = _QtechIfLinkAvgBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 4),
    _QtechIfLinkAvgBWUtilization_Type()
)
qtechIfLinkAvgBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkAvgBWUtilization.setStatus("current")


class _QtechIfLinkPeakBWUtilization_Type(Integer32):
    """Custom type qtechIfLinkPeakBWUtilization based on Integer32"""
    defaultValue = 0


_QtechIfLinkPeakBWUtilization_Type.__name__ = "Integer32"
_QtechIfLinkPeakBWUtilization_Object = MibTableColumn
qtechIfLinkPeakBWUtilization = _QtechIfLinkPeakBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 1, 1, 1, 5),
    _QtechIfLinkPeakBWUtilization_Type()
)
qtechIfLinkPeakBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfLinkPeakBWUtilization.setStatus("current")
_QtechIfLinkQosStatistics_ObjectIdentity = ObjectIdentity
qtechIfLinkQosStatistics = _QtechIfLinkQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2)
)
_QtechLinkQosCtlTable_Object = MibTable
qtechLinkQosCtlTable = _QtechLinkQosCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    qtechLinkQosCtlTable.setStatus("current")
_QtechLinkQosCtlEntry_Object = MibTableRow
qtechLinkQosCtlEntry = _QtechLinkQosCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1)
)
qtechLinkQosCtlEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechLinkQosCtlOwnerIndex"),
    (0, "QTECH-INTERFACE-MIB", "qtechLinkQosCtlTestName"),
)
if mibBuilder.loadTexts:
    qtechLinkQosCtlEntry.setStatus("current")


class _QtechLinkQosCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type qtechLinkQosCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechLinkQosCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_QtechLinkQosCtlOwnerIndex_Object = MibTableColumn
qtechLinkQosCtlOwnerIndex = _QtechLinkQosCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 1),
    _QtechLinkQosCtlOwnerIndex_Type()
)
qtechLinkQosCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechLinkQosCtlOwnerIndex.setStatus("current")


class _QtechLinkQosCtlTestName_Type(SnmpAdminString):
    """Custom type qtechLinkQosCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechLinkQosCtlTestName_Type.__name__ = "SnmpAdminString"
_QtechLinkQosCtlTestName_Object = MibTableColumn
qtechLinkQosCtlTestName = _QtechLinkQosCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 2),
    _QtechLinkQosCtlTestName_Type()
)
qtechLinkQosCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechLinkQosCtlTestName.setStatus("current")


class _QtechLinkQosCtlTargetAddressType_Type(InetAddressType):
    """Custom type qtechLinkQosCtlTargetAddressType based on InetAddressType"""
    defaultValue = 0


_QtechLinkQosCtlTargetAddressType_Type.__name__ = "InetAddressType"
_QtechLinkQosCtlTargetAddressType_Object = MibTableColumn
qtechLinkQosCtlTargetAddressType = _QtechLinkQosCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 3),
    _QtechLinkQosCtlTargetAddressType_Type()
)
qtechLinkQosCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechLinkQosCtlTargetAddressType.setStatus("current")


class _QtechLinkQosCtlTargetAddress_Type(InetAddress):
    """Custom type qtechLinkQosCtlTargetAddress based on InetAddress"""
    defaultHexValue = ""


_QtechLinkQosCtlTargetAddress_Type.__name__ = "InetAddress"
_QtechLinkQosCtlTargetAddress_Object = MibTableColumn
qtechLinkQosCtlTargetAddress = _QtechLinkQosCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 4),
    _QtechLinkQosCtlTargetAddress_Type()
)
qtechLinkQosCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechLinkQosCtlTargetAddress.setStatus("current")


class _QtechLinkQosCtlAdminStatus_Type(Integer32):
    """Custom type qtechLinkQosCtlAdminStatus based on Integer32"""
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


_QtechLinkQosCtlAdminStatus_Type.__name__ = "Integer32"
_QtechLinkQosCtlAdminStatus_Object = MibTableColumn
qtechLinkQosCtlAdminStatus = _QtechLinkQosCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 5),
    _QtechLinkQosCtlAdminStatus_Type()
)
qtechLinkQosCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechLinkQosCtlAdminStatus.setStatus("current")
_QtechLinkQosCtlRowStatus_Type = RowStatus
_QtechLinkQosCtlRowStatus_Object = MibTableColumn
qtechLinkQosCtlRowStatus = _QtechLinkQosCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 1, 1, 6),
    _QtechLinkQosCtlRowStatus_Type()
)
qtechLinkQosCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechLinkQosCtlRowStatus.setStatus("current")
_QtechLinkQosResultsTable_Object = MibTable
qtechLinkQosResultsTable = _QtechLinkQosResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    qtechLinkQosResultsTable.setStatus("current")
_QtechLinkQosResultsEntry_Object = MibTableRow
qtechLinkQosResultsEntry = _QtechLinkQosResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1)
)
qtechLinkQosResultsEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechLinkQosCtlOwnerIndex"),
    (0, "QTECH-INTERFACE-MIB", "qtechLinkQosCtlTestName"),
)
if mibBuilder.loadTexts:
    qtechLinkQosResultsEntry.setStatus("current")


class _QtechLinkQosResultsOperStatus_Type(Integer32):
    """Custom type qtechLinkQosResultsOperStatus based on Integer32"""
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


_QtechLinkQosResultsOperStatus_Type.__name__ = "Integer32"
_QtechLinkQosResultsOperStatus_Object = MibTableColumn
qtechLinkQosResultsOperStatus = _QtechLinkQosResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 1),
    _QtechLinkQosResultsOperStatus_Type()
)
qtechLinkQosResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsOperStatus.setStatus("current")


class _QtechLinkQosResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type qtechLinkQosResultsIpTargetAddressType based on InetAddressType"""
    defaultValue = 0


_QtechLinkQosResultsIpTargetAddressType_Type.__name__ = "InetAddressType"
_QtechLinkQosResultsIpTargetAddressType_Object = MibTableColumn
qtechLinkQosResultsIpTargetAddressType = _QtechLinkQosResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 2),
    _QtechLinkQosResultsIpTargetAddressType_Type()
)
qtechLinkQosResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsIpTargetAddressType.setStatus("current")


class _QtechLinkQosResultsIpTargetAddress_Type(InetAddress):
    """Custom type qtechLinkQosResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_QtechLinkQosResultsIpTargetAddress_Type.__name__ = "InetAddress"
_QtechLinkQosResultsIpTargetAddress_Object = MibTableColumn
qtechLinkQosResultsIpTargetAddress = _QtechLinkQosResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 3),
    _QtechLinkQosResultsIpTargetAddress_Type()
)
qtechLinkQosResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsIpTargetAddress.setStatus("current")
_QtechLinkQosResultsMaxRtt_Type = Unsigned32
_QtechLinkQosResultsMaxRtt_Object = MibTableColumn
qtechLinkQosResultsMaxRtt = _QtechLinkQosResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 4),
    _QtechLinkQosResultsMaxRtt_Type()
)
qtechLinkQosResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    qtechLinkQosResultsMaxRtt.setUnits("milliseconds")
_QtechLinkQosResultsMinRtt_Type = Unsigned32
_QtechLinkQosResultsMinRtt_Object = MibTableColumn
qtechLinkQosResultsMinRtt = _QtechLinkQosResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 5),
    _QtechLinkQosResultsMinRtt_Type()
)
qtechLinkQosResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    qtechLinkQosResultsMinRtt.setUnits("milliseconds")
_QtechLinkQosResultsAverageRtt_Type = Unsigned32
_QtechLinkQosResultsAverageRtt_Object = MibTableColumn
qtechLinkQosResultsAverageRtt = _QtechLinkQosResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 6),
    _QtechLinkQosResultsAverageRtt_Type()
)
qtechLinkQosResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    qtechLinkQosResultsAverageRtt.setUnits("milliseconds")
_QtechLinkQosResultsDelayJitter_Type = Unsigned32
_QtechLinkQosResultsDelayJitter_Object = MibTableColumn
qtechLinkQosResultsDelayJitter = _QtechLinkQosResultsDelayJitter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 7),
    _QtechLinkQosResultsDelayJitter_Type()
)
qtechLinkQosResultsDelayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsDelayJitter.setStatus("current")
if mibBuilder.loadTexts:
    qtechLinkQosResultsDelayJitter.setUnits("milliseconds")
_QtechLinkQosResultsPktsLossRate_Type = Unsigned32
_QtechLinkQosResultsPktsLossRate_Object = MibTableColumn
qtechLinkQosResultsPktsLossRate = _QtechLinkQosResultsPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 8),
    _QtechLinkQosResultsPktsLossRate_Type()
)
qtechLinkQosResultsPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsPktsLossRate.setStatus("current")
_QtechLinkQosResultsNetworkAF_Type = Unsigned32
_QtechLinkQosResultsNetworkAF_Object = MibTableColumn
qtechLinkQosResultsNetworkAF = _QtechLinkQosResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 2, 2, 1, 9),
    _QtechLinkQosResultsNetworkAF_Type()
)
qtechLinkQosResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLinkQosResultsNetworkAF.setStatus("current")
_QtechIfDeviceTrafficStatistics_ObjectIdentity = ObjectIdentity
qtechIfDeviceTrafficStatistics = _QtechIfDeviceTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3)
)
_QtechIfDeviceTrafficTable_Object = MibTable
qtechIfDeviceTrafficTable = _QtechIfDeviceTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    qtechIfDeviceTrafficTable.setStatus("current")
_QtechIfDeviceTrafficEntry_Object = MibTableRow
qtechIfDeviceTrafficEntry = _QtechIfDeviceTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1)
)
qtechIfDeviceTrafficEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfDeviceTrafficIndex"),
)
if mibBuilder.loadTexts:
    qtechIfDeviceTrafficEntry.setStatus("current")
_QtechIfDeviceTrafficIndex_Type = Unsigned32
_QtechIfDeviceTrafficIndex_Object = MibTableColumn
qtechIfDeviceTrafficIndex = _QtechIfDeviceTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 1),
    _QtechIfDeviceTrafficIndex_Type()
)
qtechIfDeviceTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDeviceTrafficIndex.setStatus("current")
_QtechIfFC_Type = Integer32
_QtechIfFC_Object = MibTableColumn
qtechIfFC = _QtechIfFC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 2),
    _QtechIfFC_Type()
)
qtechIfFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFC.setStatus("current")
_QtechIfFCTransRate_Type = Counter32
_QtechIfFCTransRate_Object = MibTableColumn
qtechIfFCTransRate = _QtechIfFCTransRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 3),
    _QtechIfFCTransRate_Type()
)
qtechIfFCTransRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCTransRate.setStatus("current")
_QtechIfFCTransPktsNum_Type = Counter64
_QtechIfFCTransPktsNum_Object = MibTableColumn
qtechIfFCTransPktsNum = _QtechIfFCTransPktsNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 4),
    _QtechIfFCTransPktsNum_Type()
)
qtechIfFCTransPktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCTransPktsNum.setStatus("current")
_QtechIfFCDiscardRate_Type = Counter32
_QtechIfFCDiscardRate_Object = MibTableColumn
qtechIfFCDiscardRate = _QtechIfFCDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 5),
    _QtechIfFCDiscardRate_Type()
)
qtechIfFCDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCDiscardRate.setStatus("current")
_QtechIfFCDiscardPktsNum_Type = Counter64
_QtechIfFCDiscardPktsNum_Object = MibTableColumn
qtechIfFCDiscardPktsNum = _QtechIfFCDiscardPktsNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 6),
    _QtechIfFCDiscardPktsNum_Type()
)
qtechIfFCDiscardPktsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCDiscardPktsNum.setStatus("current")
_QtechIfFCPktsLossRate_Type = Integer32
_QtechIfFCPktsLossRate_Object = MibTableColumn
qtechIfFCPktsLossRate = _QtechIfFCPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 7),
    _QtechIfFCPktsLossRate_Type()
)
qtechIfFCPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCPktsLossRate.setStatus("current")
_QtechIfFCBandwidthRate_Type = Counter32
_QtechIfFCBandwidthRate_Object = MibTableColumn
qtechIfFCBandwidthRate = _QtechIfFCBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 8),
    _QtechIfFCBandwidthRate_Type()
)
qtechIfFCBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCBandwidthRate.setStatus("current")
_QtechIfFCBandwidthPercentage_Type = Integer32
_QtechIfFCBandwidthPercentage_Object = MibTableColumn
qtechIfFCBandwidthPercentage = _QtechIfFCBandwidthPercentage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 9),
    _QtechIfFCBandwidthPercentage_Type()
)
qtechIfFCBandwidthPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFCBandwidthPercentage.setStatus("current")
_QtechIfDeviceFCGathers_Type = Integer32
_QtechIfDeviceFCGathers_Object = MibTableColumn
qtechIfDeviceFCGathers = _QtechIfDeviceFCGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 10),
    _QtechIfDeviceFCGathers_Type()
)
qtechIfDeviceFCGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfDeviceFCGathers.setStatus("current")
_QtechIfFullMeshFCGathers_Type = Integer32
_QtechIfFullMeshFCGathers_Object = MibTableColumn
qtechIfFullMeshFCGathers = _QtechIfFullMeshFCGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 11),
    _QtechIfFullMeshFCGathers_Type()
)
qtechIfFullMeshFCGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfFullMeshFCGathers.setStatus("current")
_QtechIfClassBasedGathers_Type = Integer32
_QtechIfClassBasedGathers_Object = MibTableColumn
qtechIfClassBasedGathers = _QtechIfClassBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 12),
    _QtechIfClassBasedGathers_Type()
)
qtechIfClassBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfClassBasedGathers.setStatus("current")
_QtechIfNodeBasedGathers_Type = Integer32
_QtechIfNodeBasedGathers_Object = MibTableColumn
qtechIfNodeBasedGathers = _QtechIfNodeBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 13),
    _QtechIfNodeBasedGathers_Type()
)
qtechIfNodeBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfNodeBasedGathers.setStatus("current")
_QtechIfNodeClassBasedGathers_Type = Integer32
_QtechIfNodeClassBasedGathers_Object = MibTableColumn
qtechIfNodeClassBasedGathers = _QtechIfNodeClassBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 14),
    _QtechIfNodeClassBasedGathers_Type()
)
qtechIfNodeClassBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfNodeClassBasedGathers.setStatus("current")
_QtechIfNodeFCBasedGathers_Type = Integer32
_QtechIfNodeFCBasedGathers_Object = MibTableColumn
qtechIfNodeFCBasedGathers = _QtechIfNodeFCBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 15),
    _QtechIfNodeFCBasedGathers_Type()
)
qtechIfNodeFCBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfNodeFCBasedGathers.setStatus("current")
_QtechIfNodeDeviceFCBasedGathers_Type = Integer32
_QtechIfNodeDeviceFCBasedGathers_Object = MibTableColumn
qtechIfNodeDeviceFCBasedGathers = _QtechIfNodeDeviceFCBasedGathers_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 1, 15, 3, 1, 1, 16),
    _QtechIfNodeDeviceFCBasedGathers_Type()
)
qtechIfNodeDeviceFCBasedGathers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfNodeDeviceFCBasedGathers.setStatus("current")
_QtechInterfaceTraps_ObjectIdentity = ObjectIdentity
qtechInterfaceTraps = _QtechInterfaceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 2)
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 2, 1),
    _LineDetectStatus_Type()
)
lineDetectStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectStatus.setStatus("current")
_LineDetectPosition_Type = Integer32
_LineDetectPosition_Object = MibScalar
lineDetectPosition = _LineDetectPosition_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 2, 2),
    _LineDetectPosition_Type()
)
lineDetectPosition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lineDetectPosition.setStatus("current")
_QtechInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
qtechInterfaceMIBConformance = _QtechInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3)
)
_QtechInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
qtechInterfaceMIBCompliances = _QtechInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 1)
)
_QtechInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
qtechInterfaceMIBGroups = _QtechInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 2)
)

# Managed Objects groups

qtechInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 2, 1)
)
qtechInterfaceMIBGroup.setObjects(
      *(("QTECH-INTERFACE-MIB", "qtechIfIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfPortType"),
        ("QTECH-INTERFACE-MIB", "qtechIfFlowControlAdminStatus"),
        ("QTECH-INTERFACE-MIB", "qtechIfFlowControlOperStatus"),
        ("QTECH-INTERFACE-MIB", "qtechIfAdminSpeed"),
        ("QTECH-INTERFACE-MIB", "qtechIfAdminDuplex"),
        ("QTECH-INTERFACE-MIB", "qtechIfOperSpeed"),
        ("QTECH-INTERFACE-MIB", "qtechIfOperDuplex"),
        ("QTECH-INTERFACE-MIB", "qtechIfManageStatus"),
        ("QTECH-INTERFACE-MIB", "qtechIfIpBroadcast"),
        ("QTECH-INTERFACE-MIB", "qtechIfLayer"),
        ("QTECH-INTERFACE-MIB", "qtechIfMode"),
        ("QTECH-INTERFACE-MIB", "qtechIfCounterClear"),
        ("QTECH-INTERFACE-MIB", "qtechIfEntryStatus"),
        ("QTECH-INTERFACE-MIB", "qtechIfMediumType"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownCounter"),
        ("QTECH-INTERFACE-MIB", "qtechIfInOctets"),
        ("QTECH-INTERFACE-MIB", "qtechIfOutOctets"),
        ("QTECH-INTERFACE-MIB", "qtechIfBcastInhibit"),
        ("QTECH-INTERFACE-MIB", "qtechIfNegotiation"),
        ("QTECH-INTERFACE-MIB", "qtechIfPhysAddress"),
        ("QTECH-INTERFACE-MIB", "qtechIfAdminSpeedRW"),
        ("QTECH-INTERFACE-MIB", "qtechIfAdminDuplexRW"),
        ("QTECH-INTERFACE-MIB", "qtechIfModeRW"),
        ("QTECH-INTERFACE-MIB", "qtechIfSpeed"),
        ("QTECH-INTERFACE-MIB", "qtechifAdminStatus"),
        ("QTECH-INTERFACE-MIB", "qtechifOperStatus"),
        ("QTECH-INTERFACE-MIB", "qtechIfInNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfOutNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfUpDownTimes"),
        ("QTECH-INTERFACE-MIB", "qtechifAdminStatusw"),
        ("QTECH-INTERFACE-MIB", "qtechifOperStatusw"),
        ("QTECH-INTERFACE-MIB", "qtechifSpeedw"),
        ("QTECH-INTERFACE-MIB", "qtechifMacAddress"),
        ("QTECH-INTERFACE-MIB", "qtechifLastChange"),
        ("QTECH-INTERFACE-MIB", "qtechIfInPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDiscard"),
        ("QTECH-INTERFACE-MIB", "qtechIfBandwidthUsage"),
        ("QTECH-INTERFACE-MIB", "qtechIfInBitsRate"),
        ("QTECH-INTERFACE-MIB", "qtechIfInPktRate"),
        ("QTECH-INTERFACE-MIB", "qtechIfOutBitsRate"),
        ("QTECH-INTERFACE-MIB", "qtechIfOutPktRate"),
        ("QTECH-INTERFACE-MIB", "qtechIfIpIfIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfIpId"),
        ("QTECH-INTERFACE-MIB", "qtechIfIp"),
        ("QTECH-INTERFACE-MIB", "qtechIfIpMask"),
        ("QTECH-INTERFACE-MIB", "qtechIfIpEntryStatus"),
        ("QTECH-INTERFACE-MIB", "qtechIfStatusIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfStatusLoopBackExamine"),
        ("QTECH-INTERFACE-MIB", "qtechIfErrorStatus"),
        ("QTECH-INTERFACE-MIB", "qtechGlobalIfDisableRecovery"),
        ("QTECH-INTERFACE-MIB", "qtechIfSVICreatVlanNum"),
        ("QTECH-INTERFACE-MIB", "qtechIfHandleSVI"),
        ("QTECH-INTERFACE-MIB", "qtechIfEncapsulationIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfEncapsulationVlan"),
        ("QTECH-INTERFACE-MIB", "qtechApPhyAddress"),
        ("QTECH-INTERFACE-MIB", "qtechApIfNumber"),
        ("QTECH-INTERFACE-MIB", "qtechApIfPhyIntNum"),
        ("QTECH-INTERFACE-MIB", "qtechApPhysAddress"),
        ("QTECH-INTERFACE-MIB", "qtechApIfIndex"),
        ("QTECH-INTERFACE-MIB", "qtechApIfDescr"),
        ("QTECH-INTERFACE-MIB", "qtechApIfType"),
        ("QTECH-INTERFACE-MIB", "qtechApIfMtu"),
        ("QTECH-INTERFACE-MIB", "qtechApIfSpeed"),
        ("QTECH-INTERFACE-MIB", "qtechApIfPhysAddress"),
        ("QTECH-INTERFACE-MIB", "qtechApIfAdminStatus"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOperStatus"),
        ("QTECH-INTERFACE-MIB", "qtechApIfLastChange"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInOctets"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInDiscards"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInErrors"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInUnknownProtos"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutOctets"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutDiscards"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutErrors"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutQLen"),
        ("QTECH-INTERFACE-MIB", "qtechApIfLinkUPTimes"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInDataOctets"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutDataOctets"),
        ("QTECH-INTERFACE-MIB", "qtechApIfMgmtUploadOctets"),
        ("QTECH-INTERFACE-MIB", "qtechApIfMgmtDownloadOctets"),
        ("QTECH-INTERFACE-MIB", "qtechApIfSpeedw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfMtuw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfPhysAddressw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInUcastPktsw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInNUcastPktsw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutUcastPktsw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfOutNUcastPktsw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfLinkUPTimesw"),
        ("QTECH-INTERFACE-MIB", "qtechApIfInPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfLinkIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkInOctets"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkInUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkInNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkInDiscards"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkInErrors"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkOutOctets"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkOutUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkOutNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkOutDiscards"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkOutErrors"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkInOctets"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkInUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkInNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkInDiscards"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkInErrors"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkOutOctets"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkOutUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkOutNUcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkOutDiscards"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkOutErrors"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkInBcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfUplinkOutBcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkInBcastPkts"),
        ("QTECH-INTERFACE-MIB", "qtechIfDownlinkOutBcastPkts"))
)
if mibBuilder.loadTexts:
    qtechInterfaceMIBGroup.setStatus("current")

qtechPortTypeChooseMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 2, 2)
)
qtechPortTypeChooseMibGroup.setObjects(
      *(("QTECH-INTERFACE-MIB", "qtechPortTypeChooseIndex"),
        ("QTECH-INTERFACE-MIB", "qtechPortTypeChooseType"))
)
if mibBuilder.loadTexts:
    qtechPortTypeChooseMibGroup.setStatus("current")

qtechIfMTUMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 2, 3)
)
qtechIfMTUMibGroup.setObjects(
      *(("QTECH-INTERFACE-MIB", "qtechIfMTUIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfMTU"))
)
if mibBuilder.loadTexts:
    qtechIfMTUMibGroup.setStatus("current")

qtechIfLineDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 2, 4)
)
qtechIfLineDetectGroup.setObjects(
    ("QTECH-INTERFACE-MIB", "qtechIfLineDetect")
)
if mibBuilder.loadTexts:
    qtechIfLineDetectGroup.setStatus("current")

qtechIfAvailableBWMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 2, 5)
)
qtechIfAvailableBWMibGroup.setObjects(
      *(("QTECH-INTERFACE-MIB", "qtechIfAvailableBWIfIndex"),
        ("QTECH-INTERFACE-MIB", "qtechIfAvailableBWIfBW"))
)
if mibBuilder.loadTexts:
    qtechIfAvailableBWMibGroup.setStatus("current")


# Notification objects

lineQualityDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 2, 3)
)
lineQualityDetect.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("QTECH-INTERFACE-MIB", "lineDetectStatus"),
        ("QTECH-INTERFACE-MIB", "lineDetectPosition"))
)
if mibBuilder.loadTexts:
    lineQualityDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 10, 3, 1, 1)
)
qtechInterfaceMIBCompliance.setObjects(
      *(("QTECH-INTERFACE-MIB", "qtechInterfaceMIBGroup"),
        ("QTECH-INTERFACE-MIB", "qtechPortTypeChooseMibGroup"),
        ("QTECH-INTERFACE-MIB", "qtechIfMTUMibGroup"),
        ("QTECH-INTERFACE-MIB", "qtechIfLineDetectGroup"),
        ("QTECH-INTERFACE-MIB", "qtechIfAvailableBWMibGroup"))
)
if mibBuilder.loadTexts:
    qtechInterfaceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-INTERFACE-MIB",
    **{"qtechInterfaceMIB": qtechInterfaceMIB,
       "qtechIfConfigMIBObjects": qtechIfConfigMIBObjects,
       "qtechIfTable": qtechIfTable,
       "qtechIfEntry": qtechIfEntry,
       "qtechIfIndex": qtechIfIndex,
       "qtechIfPortType": qtechIfPortType,
       "qtechIfFlowControlAdminStatus": qtechIfFlowControlAdminStatus,
       "qtechIfFlowControlOperStatus": qtechIfFlowControlOperStatus,
       "qtechIfAdminSpeed": qtechIfAdminSpeed,
       "qtechIfAdminDuplex": qtechIfAdminDuplex,
       "qtechIfOperSpeed": qtechIfOperSpeed,
       "qtechIfOperDuplex": qtechIfOperDuplex,
       "qtechIfManageStatus": qtechIfManageStatus,
       "qtechIfIpBroadcast": qtechIfIpBroadcast,
       "qtechIfLayer": qtechIfLayer,
       "qtechIfMode": qtechIfMode,
       "qtechIfCounterClear": qtechIfCounterClear,
       "qtechIfEntryStatus": qtechIfEntryStatus,
       "qtechIfMediumType": qtechIfMediumType,
       "qtechIfDownCounter": qtechIfDownCounter,
       "qtechIfInOctets": qtechIfInOctets,
       "qtechIfOutOctets": qtechIfOutOctets,
       "qtechIfBcastInhibit": qtechIfBcastInhibit,
       "qtechIfNegotiation": qtechIfNegotiation,
       "qtechIfPhysAddress": qtechIfPhysAddress,
       "qtechIfAdminSpeedRW": qtechIfAdminSpeedRW,
       "qtechIfAdminDuplexRW": qtechIfAdminDuplexRW,
       "qtechIfModeRW": qtechIfModeRW,
       "qtechIfSpeed": qtechIfSpeed,
       "qtechifAdminStatus": qtechifAdminStatus,
       "qtechifOperStatus": qtechifOperStatus,
       "qtechIfInNUcastPkts": qtechIfInNUcastPkts,
       "qtechIfOutNUcastPkts": qtechIfOutNUcastPkts,
       "qtechIfUpDownTimes": qtechIfUpDownTimes,
       "qtechifAdminStatusw": qtechifAdminStatusw,
       "qtechifOperStatusw": qtechifOperStatusw,
       "qtechifSpeedw": qtechifSpeedw,
       "qtechifMacAddress": qtechifMacAddress,
       "qtechifLastChange": qtechifLastChange,
       "qtechIfInPkts": qtechIfInPkts,
       "qtechIfDiscard": qtechIfDiscard,
       "qtechIfBandwidthUsage": qtechIfBandwidthUsage,
       "qtechIfInBitsRate": qtechIfInBitsRate,
       "qtechIfInPktRate": qtechIfInPktRate,
       "qtechIfOutBitsRate": qtechIfOutBitsRate,
       "qtechIfOutPktRate": qtechIfOutPktRate,
       "qtechIfIpTable": qtechIfIpTable,
       "qtechIfIpEntry": qtechIfIpEntry,
       "qtechIfIpIfIndex": qtechIfIpIfIndex,
       "qtechIfIpId": qtechIfIpId,
       "qtechIfIp": qtechIfIp,
       "qtechIfIpMask": qtechIfIpMask,
       "qtechIfIpEntryStatus": qtechIfIpEntryStatus,
       "qtechIfStatusTable": qtechIfStatusTable,
       "qtechIfStatusEntry": qtechIfStatusEntry,
       "qtechIfStatusIndex": qtechIfStatusIndex,
       "qtechIfStatusLoopBackExamine": qtechIfStatusLoopBackExamine,
       "qtechIfErrorStatus": qtechIfErrorStatus,
       "qtechIfLineDetect": qtechIfLineDetect,
       "qtechGlobalIfDisableRecovery": qtechGlobalIfDisableRecovery,
       "qtechPortTypeChooseTable": qtechPortTypeChooseTable,
       "qtechPortTypeChooseEntry": qtechPortTypeChooseEntry,
       "qtechPortTypeChooseIndex": qtechPortTypeChooseIndex,
       "qtechPortTypeChooseType": qtechPortTypeChooseType,
       "qtechIfMTUTable": qtechIfMTUTable,
       "qtechIfMTUEntry": qtechIfMTUEntry,
       "qtechIfMTUIndex": qtechIfMTUIndex,
       "qtechIfMTU": qtechIfMTU,
       "qtechIfAvailableBWTable": qtechIfAvailableBWTable,
       "qtechIfAvailableBWEntry": qtechIfAvailableBWEntry,
       "qtechIfAvailableBWIfIndex": qtechIfAvailableBWIfIndex,
       "qtechIfAvailableBWIfBW": qtechIfAvailableBWIfBW,
       "qtechIfSVICreatTable": qtechIfSVICreatTable,
       "qtechIfSVICreatEntry": qtechIfSVICreatEntry,
       "qtechIfSVICreatVlanNum": qtechIfSVICreatVlanNum,
       "qtechIfHandleSVI": qtechIfHandleSVI,
       "qtechIfPhyIntNum": qtechIfPhyIntNum,
       "qtechIfLinkUPTimesTable": qtechIfLinkUPTimesTable,
       "qtechIfLinkUPTimesEntry": qtechIfLinkUPTimesEntry,
       "qtechInterfaceIndex": qtechInterfaceIndex,
       "qtechIfLinkUPTimes": qtechIfLinkUPTimes,
       "qtechIfEncapsulationTable": qtechIfEncapsulationTable,
       "qtechIfEncapsulationEntry": qtechIfEncapsulationEntry,
       "qtechIfEncapsulationIndex": qtechIfEncapsulationIndex,
       "qtechIfEncapsulationVlan": qtechIfEncapsulationVlan,
       "qtechApIfNumberTable": qtechApIfNumberTable,
       "qtechApIfNumberEntry": qtechApIfNumberEntry,
       "qtechApPhyAddress": qtechApPhyAddress,
       "qtechApIfNumber": qtechApIfNumber,
       "qtechApIfPhyIntNum": qtechApIfPhyIntNum,
       "qtechApIfTable": qtechApIfTable,
       "qtechApIfEntry": qtechApIfEntry,
       "qtechApPhysAddress": qtechApPhysAddress,
       "qtechApIfIndex": qtechApIfIndex,
       "qtechApIfDescr": qtechApIfDescr,
       "qtechApIfType": qtechApIfType,
       "qtechApIfMtu": qtechApIfMtu,
       "qtechApIfSpeed": qtechApIfSpeed,
       "qtechApIfPhysAddress": qtechApIfPhysAddress,
       "qtechApIfAdminStatus": qtechApIfAdminStatus,
       "qtechApIfOperStatus": qtechApIfOperStatus,
       "qtechApIfLastChange": qtechApIfLastChange,
       "qtechApIfInOctets": qtechApIfInOctets,
       "qtechApIfInUcastPkts": qtechApIfInUcastPkts,
       "qtechApIfInNUcastPkts": qtechApIfInNUcastPkts,
       "qtechApIfInDiscards": qtechApIfInDiscards,
       "qtechApIfInErrors": qtechApIfInErrors,
       "qtechApIfInUnknownProtos": qtechApIfInUnknownProtos,
       "qtechApIfOutOctets": qtechApIfOutOctets,
       "qtechApIfOutUcastPkts": qtechApIfOutUcastPkts,
       "qtechApIfOutNUcastPkts": qtechApIfOutNUcastPkts,
       "qtechApIfOutDiscards": qtechApIfOutDiscards,
       "qtechApIfOutErrors": qtechApIfOutErrors,
       "qtechApIfOutQLen": qtechApIfOutQLen,
       "qtechApIfLinkUPTimes": qtechApIfLinkUPTimes,
       "qtechApIfInDataOctets": qtechApIfInDataOctets,
       "qtechApIfOutDataOctets": qtechApIfOutDataOctets,
       "qtechApIfMgmtUploadOctets": qtechApIfMgmtUploadOctets,
       "qtechApIfMgmtDownloadOctets": qtechApIfMgmtDownloadOctets,
       "qtechApIfSpeedw": qtechApIfSpeedw,
       "qtechApIfMtuw": qtechApIfMtuw,
       "qtechApIfPhysAddressw": qtechApIfPhysAddressw,
       "qtechApIfInUcastPktsw": qtechApIfInUcastPktsw,
       "qtechApIfInNUcastPktsw": qtechApIfInNUcastPktsw,
       "qtechApIfOutUcastPktsw": qtechApIfOutUcastPktsw,
       "qtechApIfOutNUcastPktsw": qtechApIfOutNUcastPktsw,
       "qtechApIfLinkUPTimesw": qtechApIfLinkUPTimesw,
       "qtechApIfInPkts": qtechApIfInPkts,
       "qtechIfLinkTable": qtechIfLinkTable,
       "qtechIfLinkEntry": qtechIfLinkEntry,
       "qtechIfLinkIndex": qtechIfLinkIndex,
       "qtechIfUplinkInOctets": qtechIfUplinkInOctets,
       "qtechIfUplinkInUcastPkts": qtechIfUplinkInUcastPkts,
       "qtechIfUplinkInNUcastPkts": qtechIfUplinkInNUcastPkts,
       "qtechIfUplinkInDiscards": qtechIfUplinkInDiscards,
       "qtechIfUplinkInErrors": qtechIfUplinkInErrors,
       "qtechIfUplinkOutOctets": qtechIfUplinkOutOctets,
       "qtechIfUplinkOutUcastPkts": qtechIfUplinkOutUcastPkts,
       "qtechIfUplinkOutNUcastPkts": qtechIfUplinkOutNUcastPkts,
       "qtechIfUplinkOutDiscards": qtechIfUplinkOutDiscards,
       "qtechIfUplinkOutErrors": qtechIfUplinkOutErrors,
       "qtechIfDownlinkInOctets": qtechIfDownlinkInOctets,
       "qtechIfDownlinkInUcastPkts": qtechIfDownlinkInUcastPkts,
       "qtechIfDownlinkInNUcastPkts": qtechIfDownlinkInNUcastPkts,
       "qtechIfDownlinkInDiscards": qtechIfDownlinkInDiscards,
       "qtechIfDownlinkInErrors": qtechIfDownlinkInErrors,
       "qtechIfDownlinkOutOctets": qtechIfDownlinkOutOctets,
       "qtechIfDownlinkOutUcastPkts": qtechIfDownlinkOutUcastPkts,
       "qtechIfDownlinkOutNUcastPkts": qtechIfDownlinkOutNUcastPkts,
       "qtechIfDownlinkOutDiscards": qtechIfDownlinkOutDiscards,
       "qtechIfDownlinkOutErrors": qtechIfDownlinkOutErrors,
       "qtechIfUplinkInBcastPkts": qtechIfUplinkInBcastPkts,
       "qtechIfUplinkOutBcastPkts": qtechIfUplinkOutBcastPkts,
       "qtechIfDownlinkInBcastPkts": qtechIfDownlinkInBcastPkts,
       "qtechIfDownlinkOutBcastPkts": qtechIfDownlinkOutBcastPkts,
       "qtechIfTrafficStatisticsObjects": qtechIfTrafficStatisticsObjects,
       "qtechIfLinkTrafficStatistics": qtechIfLinkTrafficStatistics,
       "qtechIfLinkTrafficTable": qtechIfLinkTrafficTable,
       "qtechIfLinkTrafficEntry": qtechIfLinkTrafficEntry,
       "qtechIfLinkTrafficIndex": qtechIfLinkTrafficIndex,
       "qtechIfLinkAvgRate": qtechIfLinkAvgRate,
       "qtechIfLinkPeakRate": qtechIfLinkPeakRate,
       "qtechIfLinkAvgBWUtilization": qtechIfLinkAvgBWUtilization,
       "qtechIfLinkPeakBWUtilization": qtechIfLinkPeakBWUtilization,
       "qtechIfLinkQosStatistics": qtechIfLinkQosStatistics,
       "qtechLinkQosCtlTable": qtechLinkQosCtlTable,
       "qtechLinkQosCtlEntry": qtechLinkQosCtlEntry,
       "qtechLinkQosCtlOwnerIndex": qtechLinkQosCtlOwnerIndex,
       "qtechLinkQosCtlTestName": qtechLinkQosCtlTestName,
       "qtechLinkQosCtlTargetAddressType": qtechLinkQosCtlTargetAddressType,
       "qtechLinkQosCtlTargetAddress": qtechLinkQosCtlTargetAddress,
       "qtechLinkQosCtlAdminStatus": qtechLinkQosCtlAdminStatus,
       "qtechLinkQosCtlRowStatus": qtechLinkQosCtlRowStatus,
       "qtechLinkQosResultsTable": qtechLinkQosResultsTable,
       "qtechLinkQosResultsEntry": qtechLinkQosResultsEntry,
       "qtechLinkQosResultsOperStatus": qtechLinkQosResultsOperStatus,
       "qtechLinkQosResultsIpTargetAddressType": qtechLinkQosResultsIpTargetAddressType,
       "qtechLinkQosResultsIpTargetAddress": qtechLinkQosResultsIpTargetAddress,
       "qtechLinkQosResultsMaxRtt": qtechLinkQosResultsMaxRtt,
       "qtechLinkQosResultsMinRtt": qtechLinkQosResultsMinRtt,
       "qtechLinkQosResultsAverageRtt": qtechLinkQosResultsAverageRtt,
       "qtechLinkQosResultsDelayJitter": qtechLinkQosResultsDelayJitter,
       "qtechLinkQosResultsPktsLossRate": qtechLinkQosResultsPktsLossRate,
       "qtechLinkQosResultsNetworkAF": qtechLinkQosResultsNetworkAF,
       "qtechIfDeviceTrafficStatistics": qtechIfDeviceTrafficStatistics,
       "qtechIfDeviceTrafficTable": qtechIfDeviceTrafficTable,
       "qtechIfDeviceTrafficEntry": qtechIfDeviceTrafficEntry,
       "qtechIfDeviceTrafficIndex": qtechIfDeviceTrafficIndex,
       "qtechIfFC": qtechIfFC,
       "qtechIfFCTransRate": qtechIfFCTransRate,
       "qtechIfFCTransPktsNum": qtechIfFCTransPktsNum,
       "qtechIfFCDiscardRate": qtechIfFCDiscardRate,
       "qtechIfFCDiscardPktsNum": qtechIfFCDiscardPktsNum,
       "qtechIfFCPktsLossRate": qtechIfFCPktsLossRate,
       "qtechIfFCBandwidthRate": qtechIfFCBandwidthRate,
       "qtechIfFCBandwidthPercentage": qtechIfFCBandwidthPercentage,
       "qtechIfDeviceFCGathers": qtechIfDeviceFCGathers,
       "qtechIfFullMeshFCGathers": qtechIfFullMeshFCGathers,
       "qtechIfClassBasedGathers": qtechIfClassBasedGathers,
       "qtechIfNodeBasedGathers": qtechIfNodeBasedGathers,
       "qtechIfNodeClassBasedGathers": qtechIfNodeClassBasedGathers,
       "qtechIfNodeFCBasedGathers": qtechIfNodeFCBasedGathers,
       "qtechIfNodeDeviceFCBasedGathers": qtechIfNodeDeviceFCBasedGathers,
       "qtechInterfaceTraps": qtechInterfaceTraps,
       "lineDetectStatus": lineDetectStatus,
       "lineDetectPosition": lineDetectPosition,
       "lineQualityDetect": lineQualityDetect,
       "qtechInterfaceMIBConformance": qtechInterfaceMIBConformance,
       "qtechInterfaceMIBCompliances": qtechInterfaceMIBCompliances,
       "qtechInterfaceMIBCompliance": qtechInterfaceMIBCompliance,
       "qtechInterfaceMIBGroups": qtechInterfaceMIBGroups,
       "qtechInterfaceMIBGroup": qtechInterfaceMIBGroup,
       "qtechPortTypeChooseMibGroup": qtechPortTypeChooseMibGroup,
       "qtechIfMTUMibGroup": qtechIfMTUMibGroup,
       "qtechIfLineDetectGroup": qtechIfLineDetectGroup,
       "qtechIfAvailableBWMibGroup": qtechIfAvailableBWMibGroup}
)
