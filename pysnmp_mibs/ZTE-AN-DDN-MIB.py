# SNMP MIB module (ZTE-AN-DDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DDN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:39 2025
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

zxAnDDNMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)
if mibBuilder.loadTexts:
    zxAnDDNMib.setRevisions(
        ("2013-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_MsagmajorVersion_ObjectIdentity = ObjectIdentity
msagmajorVersion = _MsagmajorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_MsagDDNConfig_ObjectIdentity = ObjectIdentity
msagDDNConfig = _MsagDDNConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2)
)
_DdnPortTable_Object = MibTable
ddnPortTable = _DdnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ddnPortTable.setStatus("current")
_DdnPortEntry_Object = MibTableRow
ddnPortEntry = _DdnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1)
)
ddnPortEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "ddnPortRack"),
    (0, "ZTE-AN-DDN-MIB", "ddnPortShelf"),
    (0, "ZTE-AN-DDN-MIB", "ddnPortSlot"),
    (0, "ZTE-AN-DDN-MIB", "ddnPortCircuit"),
    (0, "ZTE-AN-DDN-MIB", "ddnPortTs"),
)
if mibBuilder.loadTexts:
    ddnPortEntry.setStatus("current")


class _DdnPortRack_Type(Integer32):
    """Custom type ddnPortRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DdnPortRack_Type.__name__ = "Integer32"
_DdnPortRack_Object = MibTableColumn
ddnPortRack = _DdnPortRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 1),
    _DdnPortRack_Type()
)
ddnPortRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnPortRack.setStatus("current")


class _DdnPortShelf_Type(Integer32):
    """Custom type ddnPortShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DdnPortShelf_Type.__name__ = "Integer32"
_DdnPortShelf_Object = MibTableColumn
ddnPortShelf = _DdnPortShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 2),
    _DdnPortShelf_Type()
)
ddnPortShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnPortShelf.setStatus("current")


class _DdnPortSlot_Type(Integer32):
    """Custom type ddnPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_DdnPortSlot_Type.__name__ = "Integer32"
_DdnPortSlot_Object = MibTableColumn
ddnPortSlot = _DdnPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 3),
    _DdnPortSlot_Type()
)
ddnPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnPortSlot.setStatus("current")


class _DdnPortCircuit_Type(Integer32):
    """Custom type ddnPortCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DdnPortCircuit_Type.__name__ = "Integer32"
_DdnPortCircuit_Object = MibTableColumn
ddnPortCircuit = _DdnPortCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 4),
    _DdnPortCircuit_Type()
)
ddnPortCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnPortCircuit.setStatus("current")


class _DdnPortTs_Type(Integer32):
    """Custom type ddnPortTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdnPortTs_Type.__name__ = "Integer32"
_DdnPortTs_Object = MibTableColumn
ddnPortTs = _DdnPortTs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 5),
    _DdnPortTs_Type()
)
ddnPortTs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnPortTs.setStatus("current")


class _DdnPortName_Type(DisplayString):
    """Custom type ddnPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_DdnPortName_Type.__name__ = "DisplayString"
_DdnPortName_Object = MibTableColumn
ddnPortName = _DdnPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 6),
    _DdnPortName_Type()
)
ddnPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnPortName.setStatus("current")


class _DdnPortMainType_Type(Integer32):
    """Custom type ddnPortMainType based on Integer32"""
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
        *(("type64K", 0),
          ("type2B", 1),
          ("typeHSB", 2),
          ("typeSDM", 3),
          ("typeU", 4),
          ("typeHDB", 5),
          ("typeE1", 6),
          ("typePwe3", 7),
          ("typeShdsl", 8))
    )


_DdnPortMainType_Type.__name__ = "Integer32"
_DdnPortMainType_Object = MibTableColumn
ddnPortMainType = _DdnPortMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 7),
    _DdnPortMainType_Type()
)
ddnPortMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnPortMainType.setStatus("current")


class _DdnPortSubType_Type(Integer32):
    """Custom type ddnPortSubType based on Integer32"""
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
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("type1X64K", 1),
          ("type2X64K", 2),
          ("type3X64K", 3),
          ("type4X64K", 4),
          ("type5X64K", 5),
          ("type6X64K", 6),
          ("type7X64K", 7),
          ("type8X64K", 8),
          ("type9X64K", 9),
          ("type10X64K", 10),
          ("type11X64K", 11),
          ("type12X64K", 12),
          ("type13X64K", 13),
          ("type14X64K", 14),
          ("type15X64K", 15),
          ("type16X64K", 16),
          ("type17X64K", 17),
          ("type18X64K", 18),
          ("type19X64K", 19),
          ("type20X64K", 20),
          ("type21X64K", 21),
          ("type22X64K", 22),
          ("type23X64K", 23),
          ("type24X64K", 24),
          ("type25X64K", 25),
          ("type26X64K", 26),
          ("type27X64K", 27),
          ("type28X64K", 28),
          ("type29X64K", 29),
          ("type30X64K", 30),
          ("type31X64K", 31),
          ("type32X64K", 32),
          ("type24", 33),
          ("type48", 34),
          ("type96", 35),
          ("type192", 36))
    )


_DdnPortSubType_Type.__name__ = "Integer32"
_DdnPortSubType_Object = MibTableColumn
ddnPortSubType = _DdnPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 8),
    _DdnPortSubType_Type()
)
ddnPortSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnPortSubType.setStatus("current")
_DdnPortRowStatus_Type = RowStatus
_DdnPortRowStatus_Object = MibTableColumn
ddnPortRowStatus = _DdnPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 9),
    _DdnPortRowStatus_Type()
)
ddnPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnPortRowStatus.setStatus("current")


class _DdnPortLoopback_Type(Integer32):
    """Custom type ddnPortLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("localLoopback", 2),
          ("remoteLineLoopback", 3),
          ("unsupported", 255))
    )


_DdnPortLoopback_Type.__name__ = "Integer32"
_DdnPortLoopback_Object = MibTableColumn
ddnPortLoopback = _DdnPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 1, 1, 10),
    _DdnPortLoopback_Type()
)
ddnPortLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnPortLoopback.setStatus("current")
_DdnConnectTable_Object = MibTable
ddnConnectTable = _DdnConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ddnConnectTable.setStatus("current")
_DdnConnectEntry_Object = MibTableRow
ddnConnectEntry = _DdnConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1)
)
ddnConnectEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "ddnConPort1Rack"),
    (0, "ZTE-AN-DDN-MIB", "ddnConPort1Shelf"),
    (0, "ZTE-AN-DDN-MIB", "ddnConPort1Slot"),
    (0, "ZTE-AN-DDN-MIB", "ddnConPort1Circuit"),
    (0, "ZTE-AN-DDN-MIB", "ddnConPort1Ts"),
)
if mibBuilder.loadTexts:
    ddnConnectEntry.setStatus("current")


class _DdnConPort1Rack_Type(Integer32):
    """Custom type ddnConPort1Rack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DdnConPort1Rack_Type.__name__ = "Integer32"
_DdnConPort1Rack_Object = MibTableColumn
ddnConPort1Rack = _DdnConPort1Rack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 1),
    _DdnConPort1Rack_Type()
)
ddnConPort1Rack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnConPort1Rack.setStatus("current")


class _DdnConPort1Shelf_Type(Integer32):
    """Custom type ddnConPort1Shelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DdnConPort1Shelf_Type.__name__ = "Integer32"
_DdnConPort1Shelf_Object = MibTableColumn
ddnConPort1Shelf = _DdnConPort1Shelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 2),
    _DdnConPort1Shelf_Type()
)
ddnConPort1Shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnConPort1Shelf.setStatus("current")


class _DdnConPort1Slot_Type(Integer32):
    """Custom type ddnConPort1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_DdnConPort1Slot_Type.__name__ = "Integer32"
_DdnConPort1Slot_Object = MibTableColumn
ddnConPort1Slot = _DdnConPort1Slot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 3),
    _DdnConPort1Slot_Type()
)
ddnConPort1Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnConPort1Slot.setStatus("current")


class _DdnConPort1Circuit_Type(Integer32):
    """Custom type ddnConPort1Circuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DdnConPort1Circuit_Type.__name__ = "Integer32"
_DdnConPort1Circuit_Object = MibTableColumn
ddnConPort1Circuit = _DdnConPort1Circuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 4),
    _DdnConPort1Circuit_Type()
)
ddnConPort1Circuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnConPort1Circuit.setStatus("current")


class _DdnConPort1Ts_Type(Integer32):
    """Custom type ddnConPort1Ts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdnConPort1Ts_Type.__name__ = "Integer32"
_DdnConPort1Ts_Object = MibTableColumn
ddnConPort1Ts = _DdnConPort1Ts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 5),
    _DdnConPort1Ts_Type()
)
ddnConPort1Ts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ddnConPort1Ts.setStatus("current")


class _DdnConPort1Name_Type(DisplayString):
    """Custom type ddnConPort1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_DdnConPort1Name_Type.__name__ = "DisplayString"
_DdnConPort1Name_Object = MibTableColumn
ddnConPort1Name = _DdnConPort1Name_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 6),
    _DdnConPort1Name_Type()
)
ddnConPort1Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort1Name.setStatus("current")


class _DdnConPort2Rack_Type(Integer32):
    """Custom type ddnConPort2Rack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DdnConPort2Rack_Type.__name__ = "Integer32"
_DdnConPort2Rack_Object = MibTableColumn
ddnConPort2Rack = _DdnConPort2Rack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 7),
    _DdnConPort2Rack_Type()
)
ddnConPort2Rack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort2Rack.setStatus("current")


class _DdnConPort2Shelf_Type(Integer32):
    """Custom type ddnConPort2Shelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DdnConPort2Shelf_Type.__name__ = "Integer32"
_DdnConPort2Shelf_Object = MibTableColumn
ddnConPort2Shelf = _DdnConPort2Shelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 8),
    _DdnConPort2Shelf_Type()
)
ddnConPort2Shelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort2Shelf.setStatus("current")


class _DdnConPort2Slot_Type(Integer32):
    """Custom type ddnConPort2Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_DdnConPort2Slot_Type.__name__ = "Integer32"
_DdnConPort2Slot_Object = MibTableColumn
ddnConPort2Slot = _DdnConPort2Slot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 9),
    _DdnConPort2Slot_Type()
)
ddnConPort2Slot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort2Slot.setStatus("current")


class _DdnConPort2Circuit_Type(Integer32):
    """Custom type ddnConPort2Circuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_DdnConPort2Circuit_Type.__name__ = "Integer32"
_DdnConPort2Circuit_Object = MibTableColumn
ddnConPort2Circuit = _DdnConPort2Circuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 10),
    _DdnConPort2Circuit_Type()
)
ddnConPort2Circuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort2Circuit.setStatus("current")


class _DdnConPort2Ts_Type(Integer32):
    """Custom type ddnConPort2Ts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdnConPort2Ts_Type.__name__ = "Integer32"
_DdnConPort2Ts_Object = MibTableColumn
ddnConPort2Ts = _DdnConPort2Ts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 11),
    _DdnConPort2Ts_Type()
)
ddnConPort2Ts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort2Ts.setStatus("current")


class _DdnConPort2Name_Type(DisplayString):
    """Custom type ddnConPort2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_DdnConPort2Name_Type.__name__ = "DisplayString"
_DdnConPort2Name_Object = MibTableColumn
ddnConPort2Name = _DdnConPort2Name_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 12),
    _DdnConPort2Name_Type()
)
ddnConPort2Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConPort2Name.setStatus("current")


class _DdnConName_Type(DisplayString):
    """Custom type ddnConName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_DdnConName_Type.__name__ = "DisplayString"
_DdnConName_Object = MibTableColumn
ddnConName = _DdnConName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 13),
    _DdnConName_Type()
)
ddnConName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConName.setStatus("current")


class _DdnConnExOperType_Type(Integer32):
    """Custom type ddnConnExOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DdnConnExOperType_Type.__name__ = "Integer32"
_DdnConnExOperType_Object = MibTableColumn
ddnConnExOperType = _DdnConnExOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 14),
    _DdnConnExOperType_Type()
)
ddnConnExOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConnExOperType.setStatus("current")
_DdnConRowStatus_Type = RowStatus
_DdnConRowStatus_Object = MibTableColumn
ddnConRowStatus = _DdnConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 2, 1, 15),
    _DdnConRowStatus_Type()
)
ddnConRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ddnConRowStatus.setStatus("current")
_HdbPortConfigTable_Object = MibTable
hdbPortConfigTable = _HdbPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hdbPortConfigTable.setStatus("current")
_HdbPortConfigEntry_Object = MibTableRow
hdbPortConfigEntry = _HdbPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 3, 1)
)
hdbPortConfigEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "hdbPCRack"),
    (0, "ZTE-AN-DDN-MIB", "hdbPCShelf"),
    (0, "ZTE-AN-DDN-MIB", "hdbPCSlot"),
)
if mibBuilder.loadTexts:
    hdbPortConfigEntry.setStatus("current")


class _HdbPCRack_Type(Integer32):
    """Custom type hdbPCRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HdbPCRack_Type.__name__ = "Integer32"
_HdbPCRack_Object = MibTableColumn
hdbPCRack = _HdbPCRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 3, 1, 1),
    _HdbPCRack_Type()
)
hdbPCRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdbPCRack.setStatus("current")


class _HdbPCShelf_Type(Integer32):
    """Custom type hdbPCShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HdbPCShelf_Type.__name__ = "Integer32"
_HdbPCShelf_Object = MibTableColumn
hdbPCShelf = _HdbPCShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 3, 1, 2),
    _HdbPCShelf_Type()
)
hdbPCShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdbPCShelf.setStatus("current")


class _HdbPCSlot_Type(Integer32):
    """Custom type hdbPCSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_HdbPCSlot_Type.__name__ = "Integer32"
_HdbPCSlot_Object = MibTableColumn
hdbPCSlot = _HdbPCSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 3, 1, 3),
    _HdbPCSlot_Type()
)
hdbPCSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hdbPCSlot.setStatus("current")


class _HdbPCPortNumber_Type(Integer32):
    """Custom type hdbPCPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HdbPCPortNumber_Type.__name__ = "Integer32"
_HdbPCPortNumber_Object = MibTableColumn
hdbPCPortNumber = _HdbPCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 3, 1, 4),
    _HdbPCPortNumber_Type()
)
hdbPCPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdbPCPortNumber.setStatus("current")
_AudbPortConfigTable_Object = MibTable
audbPortConfigTable = _AudbPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4)
)
if mibBuilder.loadTexts:
    audbPortConfigTable.setStatus("current")
_AudbPortConfigEntry_Object = MibTableRow
audbPortConfigEntry = _AudbPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1)
)
audbPortConfigEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "audbPCRack"),
    (0, "ZTE-AN-DDN-MIB", "audbPCShelf"),
    (0, "ZTE-AN-DDN-MIB", "audbPCSlot"),
    (0, "ZTE-AN-DDN-MIB", "audbPCCircuit"),
    (0, "ZTE-AN-DDN-MIB", "audbPCTs"),
)
if mibBuilder.loadTexts:
    audbPortConfigEntry.setStatus("current")


class _AudbPCRack_Type(Integer32):
    """Custom type audbPCRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AudbPCRack_Type.__name__ = "Integer32"
_AudbPCRack_Object = MibTableColumn
audbPCRack = _AudbPCRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 1),
    _AudbPCRack_Type()
)
audbPCRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audbPCRack.setStatus("current")


class _AudbPCShelf_Type(Integer32):
    """Custom type audbPCShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AudbPCShelf_Type.__name__ = "Integer32"
_AudbPCShelf_Object = MibTableColumn
audbPCShelf = _AudbPCShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 2),
    _AudbPCShelf_Type()
)
audbPCShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audbPCShelf.setStatus("current")


class _AudbPCSlot_Type(Integer32):
    """Custom type audbPCSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_AudbPCSlot_Type.__name__ = "Integer32"
_AudbPCSlot_Object = MibTableColumn
audbPCSlot = _AudbPCSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 3),
    _AudbPCSlot_Type()
)
audbPCSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audbPCSlot.setStatus("current")


class _AudbPCCircuit_Type(Integer32):
    """Custom type audbPCCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AudbPCCircuit_Type.__name__ = "Integer32"
_AudbPCCircuit_Object = MibTableColumn
audbPCCircuit = _AudbPCCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 4),
    _AudbPCCircuit_Type()
)
audbPCCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audbPCCircuit.setStatus("current")


class _AudbPCTs_Type(Integer32):
    """Custom type audbPCTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 255),
    )


_AudbPCTs_Type.__name__ = "Integer32"
_AudbPCTs_Object = MibTableColumn
audbPCTs = _AudbPCTs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 5),
    _AudbPCTs_Type()
)
audbPCTs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audbPCTs.setStatus("current")


class _AudbPortLineType_Type(Integer32):
    """Custom type audbPortLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twolinetrans", 1),
          ("fourlinetrans", 2))
    )


_AudbPortLineType_Type.__name__ = "Integer32"
_AudbPortLineType_Object = MibTableColumn
audbPortLineType = _AudbPortLineType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 9),
    _AudbPortLineType_Type()
)
audbPortLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audbPortLineType.setStatus("current")


class _AudbPortInputGain_Type(DisplayString):
    """Custom type audbPortInputGain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AudbPortInputGain_Type.__name__ = "DisplayString"
_AudbPortInputGain_Object = MibTableColumn
audbPortInputGain = _AudbPortInputGain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 10),
    _AudbPortInputGain_Type()
)
audbPortInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audbPortInputGain.setStatus("current")


class _AudbPortOutputGain_Type(DisplayString):
    """Custom type audbPortOutputGain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AudbPortOutputGain_Type.__name__ = "DisplayString"
_AudbPortOutputGain_Object = MibTableColumn
audbPortOutputGain = _AudbPortOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 11),
    _AudbPortOutputGain_Type()
)
audbPortOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audbPortOutputGain.setStatus("current")


class _AudbPortLoopState_Type(Integer32):
    """Custom type audbPortLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("notloop", 2))
    )


_AudbPortLoopState_Type.__name__ = "Integer32"
_AudbPortLoopState_Object = MibTableColumn
audbPortLoopState = _AudbPortLoopState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 4, 1, 12),
    _AudbPortLoopState_Type()
)
audbPortLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audbPortLoopState.setStatus("current")
_ZxAnDdnBertMgmtGroup_ObjectIdentity = ObjectIdentity
zxAnDdnBertMgmtGroup = _ZxAnDdnBertMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5)
)
_ZxAnDdnBertConfTable_Object = MibTable
zxAnDdnBertConfTable = _ZxAnDdnBertConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnDdnBertConfTable.setStatus("current")
_ZxAnDdnBertConfEntry_Object = MibTableRow
zxAnDdnBertConfEntry = _ZxAnDdnBertConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1)
)
zxAnDdnBertConfEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertConfRack"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertConfShelf"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertConfSlot"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertConfCircuit"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertConfTs"),
)
if mibBuilder.loadTexts:
    zxAnDdnBertConfEntry.setStatus("current")
_ZxAnDdnBertConfRack_Type = Integer32
_ZxAnDdnBertConfRack_Object = MibTableColumn
zxAnDdnBertConfRack = _ZxAnDdnBertConfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 1),
    _ZxAnDdnBertConfRack_Type()
)
zxAnDdnBertConfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertConfRack.setStatus("current")
_ZxAnDdnBertConfShelf_Type = Integer32
_ZxAnDdnBertConfShelf_Object = MibTableColumn
zxAnDdnBertConfShelf = _ZxAnDdnBertConfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 2),
    _ZxAnDdnBertConfShelf_Type()
)
zxAnDdnBertConfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertConfShelf.setStatus("current")
_ZxAnDdnBertConfSlot_Type = Integer32
_ZxAnDdnBertConfSlot_Object = MibTableColumn
zxAnDdnBertConfSlot = _ZxAnDdnBertConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 3),
    _ZxAnDdnBertConfSlot_Type()
)
zxAnDdnBertConfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertConfSlot.setStatus("current")
_ZxAnDdnBertConfCircuit_Type = Integer32
_ZxAnDdnBertConfCircuit_Object = MibTableColumn
zxAnDdnBertConfCircuit = _ZxAnDdnBertConfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 4),
    _ZxAnDdnBertConfCircuit_Type()
)
zxAnDdnBertConfCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertConfCircuit.setStatus("current")
_ZxAnDdnBertConfTs_Type = Integer32
_ZxAnDdnBertConfTs_Object = MibTableColumn
zxAnDdnBertConfTs = _ZxAnDdnBertConfTs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 5),
    _ZxAnDdnBertConfTs_Type()
)
zxAnDdnBertConfTs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertConfTs.setStatus("current")


class _ZxAnDdnBertAction_Type(Integer32):
    """Custom type zxAnDdnBertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_ZxAnDdnBertAction_Type.__name__ = "Integer32"
_ZxAnDdnBertAction_Object = MibTableColumn
zxAnDdnBertAction = _ZxAnDdnBertAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 6),
    _ZxAnDdnBertAction_Type()
)
zxAnDdnBertAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertAction.setStatus("current")


class _ZxAnDdnBertTestPattern_Type(Integer32):
    """Custom type zxAnDdnBertTestPattern based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              20)
        )
    )
    namedValues = NamedValues(
        *(("twoE9MinusOne", 1),
          ("twoE11MinusOne", 2),
          ("twoE15MinusOne", 3),
          ("twoE20MinusOne", 4),
          ("twoE23MinusOne", 5),
          ("userPattern", 20))
    )


_ZxAnDdnBertTestPattern_Type.__name__ = "Integer32"
_ZxAnDdnBertTestPattern_Object = MibTableColumn
zxAnDdnBertTestPattern = _ZxAnDdnBertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 7),
    _ZxAnDdnBertTestPattern_Type()
)
zxAnDdnBertTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertTestPattern.setStatus("current")


class _ZxAnDdnBertUserPattern_Type(OctetString):
    """Custom type zxAnDdnBertUserPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_ZxAnDdnBertUserPattern_Type.__name__ = "OctetString"
_ZxAnDdnBertUserPattern_Object = MibTableColumn
zxAnDdnBertUserPattern = _ZxAnDdnBertUserPattern_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 8),
    _ZxAnDdnBertUserPattern_Type()
)
zxAnDdnBertUserPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertUserPattern.setStatus("current")


class _ZxAnDdnBertMode_Type(Integer32):
    """Custom type zxAnDdnBertMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("break", 1),
          ("monitor", 2))
    )


_ZxAnDdnBertMode_Type.__name__ = "Integer32"
_ZxAnDdnBertMode_Object = MibTableColumn
zxAnDdnBertMode = _ZxAnDdnBertMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 9),
    _ZxAnDdnBertMode_Type()
)
zxAnDdnBertMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertMode.setStatus("current")


class _ZxAnDdnBertDuration_Type(Integer32):
    """Custom type zxAnDdnBertDuration based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2880),
    )


_ZxAnDdnBertDuration_Type.__name__ = "Integer32"
_ZxAnDdnBertDuration_Object = MibTableColumn
zxAnDdnBertDuration = _ZxAnDdnBertDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 10),
    _ZxAnDdnBertDuration_Type()
)
zxAnDdnBertDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDdnBertDuration.setUnits("Minutes")


class _ZxAnDdnBertStartDateAndTime_Type(DisplayString):
    """Custom type zxAnDdnBertStartDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnDdnBertStartDateAndTime_Type.__name__ = "DisplayString"
_ZxAnDdnBertStartDateAndTime_Object = MibTableColumn
zxAnDdnBertStartDateAndTime = _ZxAnDdnBertStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 11),
    _ZxAnDdnBertStartDateAndTime_Type()
)
zxAnDdnBertStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertStartDateAndTime.setStatus("current")


class _ZxAnDdnBertOperStatus_Type(Integer32):
    """Custom type zxAnDdnBertOperStatus based on Integer32"""
    defaultValue = 1

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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnDdnBertOperStatus_Type.__name__ = "Integer32"
_ZxAnDdnBertOperStatus_Object = MibTableColumn
zxAnDdnBertOperStatus = _ZxAnDdnBertOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 12),
    _ZxAnDdnBertOperStatus_Type()
)
zxAnDdnBertOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertOperStatus.setStatus("current")


class _ZxAnDdnBertTargetType_Type(Integer32):
    """Custom type zxAnDdnBertTargetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("link", 2))
    )


_ZxAnDdnBertTargetType_Type.__name__ = "Integer32"
_ZxAnDdnBertTargetType_Object = MibTableColumn
zxAnDdnBertTargetType = _ZxAnDdnBertTargetType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 13),
    _ZxAnDdnBertTargetType_Type()
)
zxAnDdnBertTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertTargetType.setStatus("current")
_ZxAnDdnBertRowStatus_Type = RowStatus
_ZxAnDdnBertRowStatus_Object = MibTableColumn
zxAnDdnBertRowStatus = _ZxAnDdnBertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 1, 1, 20),
    _ZxAnDdnBertRowStatus_Type()
)
zxAnDdnBertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDdnBertRowStatus.setStatus("current")
_ZxAnDdnBertStatsTable_Object = MibTable
zxAnDdnBertStatsTable = _ZxAnDdnBertStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2)
)
if mibBuilder.loadTexts:
    zxAnDdnBertStatsTable.setStatus("current")
_ZxAnDdnBertStatsEntry_Object = MibTableRow
zxAnDdnBertStatsEntry = _ZxAnDdnBertStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1)
)
zxAnDdnBertStatsEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertStatsRack"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertStatsShelf"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertStatsSlot"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertStatsCircuit"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnBertStatsTs"),
)
if mibBuilder.loadTexts:
    zxAnDdnBertStatsEntry.setStatus("current")
_ZxAnDdnBertStatsRack_Type = Integer32
_ZxAnDdnBertStatsRack_Object = MibTableColumn
zxAnDdnBertStatsRack = _ZxAnDdnBertStatsRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 1),
    _ZxAnDdnBertStatsRack_Type()
)
zxAnDdnBertStatsRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertStatsRack.setStatus("current")
_ZxAnDdnBertStatsShelf_Type = Integer32
_ZxAnDdnBertStatsShelf_Object = MibTableColumn
zxAnDdnBertStatsShelf = _ZxAnDdnBertStatsShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 2),
    _ZxAnDdnBertStatsShelf_Type()
)
zxAnDdnBertStatsShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertStatsShelf.setStatus("current")
_ZxAnDdnBertStatsSlot_Type = Integer32
_ZxAnDdnBertStatsSlot_Object = MibTableColumn
zxAnDdnBertStatsSlot = _ZxAnDdnBertStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 3),
    _ZxAnDdnBertStatsSlot_Type()
)
zxAnDdnBertStatsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertStatsSlot.setStatus("current")
_ZxAnDdnBertStatsCircuit_Type = Integer32
_ZxAnDdnBertStatsCircuit_Object = MibTableColumn
zxAnDdnBertStatsCircuit = _ZxAnDdnBertStatsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 4),
    _ZxAnDdnBertStatsCircuit_Type()
)
zxAnDdnBertStatsCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertStatsCircuit.setStatus("current")
_ZxAnDdnBertStatsTs_Type = Integer32
_ZxAnDdnBertStatsTs_Object = MibTableColumn
zxAnDdnBertStatsTs = _ZxAnDdnBertStatsTs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 5),
    _ZxAnDdnBertStatsTs_Type()
)
zxAnDdnBertStatsTs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnBertStatsTs.setStatus("current")
_ZxAnDdnBertRxTotalBits_Type = Counter64
_ZxAnDdnBertRxTotalBits_Object = MibTableColumn
zxAnDdnBertRxTotalBits = _ZxAnDdnBertRxTotalBits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 6),
    _ZxAnDdnBertRxTotalBits_Type()
)
zxAnDdnBertRxTotalBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertRxTotalBits.setStatus("current")
_ZxAnDdnBertRxErrorBits_Type = Counter32
_ZxAnDdnBertRxErrorBits_Object = MibTableColumn
zxAnDdnBertRxErrorBits = _ZxAnDdnBertRxErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 7),
    _ZxAnDdnBertRxErrorBits_Type()
)
zxAnDdnBertRxErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertRxErrorBits.setStatus("current")


class _ZxAnDdnBertRxBitErrorRatio_Type(Unsigned32):
    """Custom type zxAnDdnBertRxBitErrorRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnDdnBertRxBitErrorRatio_Type.__name__ = "Unsigned32"
_ZxAnDdnBertRxBitErrorRatio_Object = MibTableColumn
zxAnDdnBertRxBitErrorRatio = _ZxAnDdnBertRxBitErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 8),
    _ZxAnDdnBertRxBitErrorRatio_Type()
)
zxAnDdnBertRxBitErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertRxBitErrorRatio.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDdnBertRxBitErrorRatio.setUnits("percents")
_ZxAnDdnBertTimeElapsed_Type = Integer32
_ZxAnDdnBertTimeElapsed_Object = MibTableColumn
zxAnDdnBertTimeElapsed = _ZxAnDdnBertTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 9),
    _ZxAnDdnBertTimeElapsed_Type()
)
zxAnDdnBertTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnDdnBertTimeElapsed.setUnits("seconds")
_ZxAnDdnBertEs_Type = Counter32
_ZxAnDdnBertEs_Object = MibTableColumn
zxAnDdnBertEs = _ZxAnDdnBertEs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 10),
    _ZxAnDdnBertEs_Type()
)
zxAnDdnBertEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertEs.setStatus("current")
_ZxAnDdnBertSes_Type = Counter32
_ZxAnDdnBertSes_Object = MibTableColumn
zxAnDdnBertSes = _ZxAnDdnBertSes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 11),
    _ZxAnDdnBertSes_Type()
)
zxAnDdnBertSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertSes.setStatus("current")
_ZxAnDdnBertUas_Type = Counter32
_ZxAnDdnBertUas_Object = MibTableColumn
zxAnDdnBertUas = _ZxAnDdnBertUas_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 12),
    _ZxAnDdnBertUas_Type()
)
zxAnDdnBertUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertUas.setStatus("current")
_ZxAnDdnBertDm_Type = Counter32
_ZxAnDdnBertDm_Object = MibTableColumn
zxAnDdnBertDm = _ZxAnDdnBertDm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 13),
    _ZxAnDdnBertDm_Type()
)
zxAnDdnBertDm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertDm.setStatus("current")
_ZxAnDdnBertBbe_Type = Counter32
_ZxAnDdnBertBbe_Object = MibTableColumn
zxAnDdnBertBbe = _ZxAnDdnBertBbe_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 14),
    _ZxAnDdnBertBbe_Type()
)
zxAnDdnBertBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertBbe.setStatus("current")
_ZxAnDdnBertCses_Type = Counter32
_ZxAnDdnBertCses_Object = MibTableColumn
zxAnDdnBertCses = _ZxAnDdnBertCses_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 5, 2, 1, 15),
    _ZxAnDdnBertCses_Type()
)
zxAnDdnBertCses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnBertCses.setStatus("current")
_ZxAnDdnModemMgmtGroup_ObjectIdentity = ObjectIdentity
zxAnDdnModemMgmtGroup = _ZxAnDdnModemMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7)
)
_ZxAnDdnModemMgmtTable_Object = MibTable
zxAnDdnModemMgmtTable = _ZxAnDdnModemMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1)
)
if mibBuilder.loadTexts:
    zxAnDdnModemMgmtTable.setStatus("current")
_ZxAnDdnModemMgmtEntry_Object = MibTableRow
zxAnDdnModemMgmtEntry = _ZxAnDdnModemMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1)
)
zxAnDdnModemMgmtEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemRack"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemShelf"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemSlot"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemPort"),
)
if mibBuilder.loadTexts:
    zxAnDdnModemMgmtEntry.setStatus("current")
_ZxAnDdnModemRack_Type = Integer32
_ZxAnDdnModemRack_Object = MibTableColumn
zxAnDdnModemRack = _ZxAnDdnModemRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 1),
    _ZxAnDdnModemRack_Type()
)
zxAnDdnModemRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemRack.setStatus("current")
_ZxAnDdnModemShelf_Type = Integer32
_ZxAnDdnModemShelf_Object = MibTableColumn
zxAnDdnModemShelf = _ZxAnDdnModemShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 2),
    _ZxAnDdnModemShelf_Type()
)
zxAnDdnModemShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemShelf.setStatus("current")
_ZxAnDdnModemSlot_Type = Integer32
_ZxAnDdnModemSlot_Object = MibTableColumn
zxAnDdnModemSlot = _ZxAnDdnModemSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 3),
    _ZxAnDdnModemSlot_Type()
)
zxAnDdnModemSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemSlot.setStatus("current")
_ZxAnDdnModemPort_Type = Integer32
_ZxAnDdnModemPort_Object = MibTableColumn
zxAnDdnModemPort = _ZxAnDdnModemPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 4),
    _ZxAnDdnModemPort_Type()
)
zxAnDdnModemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemPort.setStatus("current")


class _ZxAnDdnModemOperStatus_Type(Integer32):
    """Custom type zxAnDdnModemOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_ZxAnDdnModemOperStatus_Type.__name__ = "Integer32"
_ZxAnDdnModemOperStatus_Object = MibTableColumn
zxAnDdnModemOperStatus = _ZxAnDdnModemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 5),
    _ZxAnDdnModemOperStatus_Type()
)
zxAnDdnModemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnModemOperStatus.setStatus("current")
_ZxAnDdnModemConfigData_Type = DisplayString
_ZxAnDdnModemConfigData_Object = MibTableColumn
zxAnDdnModemConfigData = _ZxAnDdnModemConfigData_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 6),
    _ZxAnDdnModemConfigData_Type()
)
zxAnDdnModemConfigData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDdnModemConfigData.setStatus("current")


class _ZxAnDdnModemReset_Type(Integer32):
    """Custom type zxAnDdnModemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZxAnDdnModemReset_Type.__name__ = "Integer32"
_ZxAnDdnModemReset_Object = MibTableColumn
zxAnDdnModemReset = _ZxAnDdnModemReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 7),
    _ZxAnDdnModemReset_Type()
)
zxAnDdnModemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDdnModemReset.setStatus("current")


class _ZxAnDdnModemSaveData_Type(Integer32):
    """Custom type zxAnDdnModemSaveData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveData", 1)
    )


_ZxAnDdnModemSaveData_Type.__name__ = "Integer32"
_ZxAnDdnModemSaveData_Object = MibTableColumn
zxAnDdnModemSaveData = _ZxAnDdnModemSaveData_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 8),
    _ZxAnDdnModemSaveData_Type()
)
zxAnDdnModemSaveData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDdnModemSaveData.setStatus("current")


class _ZxAnDdnModemLineStatus_Type(Integer32):
    """Custom type zxAnDdnModemLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13,
              14,
              21)
        )
    )
    namedValues = NamedValues(
        *(("shdslSnrMarginCrossing", 1),
          ("shdslLoopAttenCrossing", 2),
          ("shdslLossOfSyncWord", 3),
          ("e1LossOfSignal", 11),
          ("e1LossOfFrame", 12),
          ("e1CrcError", 13),
          ("v35IfConnectionBroken", 14),
          ("dteIfConnectionBroken", 21))
    )


_ZxAnDdnModemLineStatus_Type.__name__ = "Integer32"
_ZxAnDdnModemLineStatus_Object = MibTableColumn
zxAnDdnModemLineStatus = _ZxAnDdnModemLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 1, 1, 9),
    _ZxAnDdnModemLineStatus_Type()
)
zxAnDdnModemLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnModemLineStatus.setStatus("current")
_ZxAnDdnModemQueryTable_Object = MibTable
zxAnDdnModemQueryTable = _ZxAnDdnModemQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    zxAnDdnModemQueryTable.setStatus("current")
_ZxAnDdnModemQueryEntry_Object = MibTableRow
zxAnDdnModemQueryEntry = _ZxAnDdnModemQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1)
)
zxAnDdnModemQueryEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemQueryRack"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemQueryShelf"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemQuerySlot"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemQueryPort"),
)
if mibBuilder.loadTexts:
    zxAnDdnModemQueryEntry.setStatus("current")
_ZxAnDdnModemQueryRack_Type = Integer32
_ZxAnDdnModemQueryRack_Object = MibTableColumn
zxAnDdnModemQueryRack = _ZxAnDdnModemQueryRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 1),
    _ZxAnDdnModemQueryRack_Type()
)
zxAnDdnModemQueryRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemQueryRack.setStatus("current")
_ZxAnDdnModemQueryShelf_Type = Integer32
_ZxAnDdnModemQueryShelf_Object = MibTableColumn
zxAnDdnModemQueryShelf = _ZxAnDdnModemQueryShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 2),
    _ZxAnDdnModemQueryShelf_Type()
)
zxAnDdnModemQueryShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemQueryShelf.setStatus("current")
_ZxAnDdnModemQuerySlot_Type = Integer32
_ZxAnDdnModemQuerySlot_Object = MibTableColumn
zxAnDdnModemQuerySlot = _ZxAnDdnModemQuerySlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 3),
    _ZxAnDdnModemQuerySlot_Type()
)
zxAnDdnModemQuerySlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemQuerySlot.setStatus("current")
_ZxAnDdnModemQueryPort_Type = Integer32
_ZxAnDdnModemQueryPort_Object = MibTableColumn
zxAnDdnModemQueryPort = _ZxAnDdnModemQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 4),
    _ZxAnDdnModemQueryPort_Type()
)
zxAnDdnModemQueryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemQueryPort.setStatus("current")


class _ZxAnDdnModemQueryType_Type(Integer32):
    """Custom type zxAnDdnModemQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("perf", 2))
    )


_ZxAnDdnModemQueryType_Type.__name__ = "Integer32"
_ZxAnDdnModemQueryType_Object = MibTableColumn
zxAnDdnModemQueryType = _ZxAnDdnModemQueryType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 5),
    _ZxAnDdnModemQueryType_Type()
)
zxAnDdnModemQueryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDdnModemQueryType.setStatus("current")


class _ZxAnDdnModemQueryStatus_Type(Integer32):
    """Custom type zxAnDdnModemQueryStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnDdnModemQueryStatus_Type.__name__ = "Integer32"
_ZxAnDdnModemQueryStatus_Object = MibTableColumn
zxAnDdnModemQueryStatus = _ZxAnDdnModemQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 6),
    _ZxAnDdnModemQueryStatus_Type()
)
zxAnDdnModemQueryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnModemQueryStatus.setStatus("current")
_ZxAnDdnModemQueryResult_Type = DisplayString
_ZxAnDdnModemQueryResult_Object = MibTableColumn
zxAnDdnModemQueryResult = _ZxAnDdnModemQueryResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 2, 1, 7),
    _ZxAnDdnModemQueryResult_Type()
)
zxAnDdnModemQueryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnModemQueryResult.setStatus("current")
_ZxAnDdnModemDiagnoseTable_Object = MibTable
zxAnDdnModemDiagnoseTable = _ZxAnDdnModemDiagnoseTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3)
)
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseTable.setStatus("current")
_ZxAnDdnModemDiagnoseEntry_Object = MibTableRow
zxAnDdnModemDiagnoseEntry = _ZxAnDdnModemDiagnoseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1)
)
zxAnDdnModemDiagnoseEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemDiagnoseRack"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemDiagnoseShelf"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemDiagnoseSlot"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnModemDiagnosePort"),
)
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseEntry.setStatus("current")
_ZxAnDdnModemDiagnoseRack_Type = Integer32
_ZxAnDdnModemDiagnoseRack_Object = MibTableColumn
zxAnDdnModemDiagnoseRack = _ZxAnDdnModemDiagnoseRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1, 1),
    _ZxAnDdnModemDiagnoseRack_Type()
)
zxAnDdnModemDiagnoseRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseRack.setStatus("current")
_ZxAnDdnModemDiagnoseShelf_Type = Integer32
_ZxAnDdnModemDiagnoseShelf_Object = MibTableColumn
zxAnDdnModemDiagnoseShelf = _ZxAnDdnModemDiagnoseShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1, 2),
    _ZxAnDdnModemDiagnoseShelf_Type()
)
zxAnDdnModemDiagnoseShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseShelf.setStatus("current")
_ZxAnDdnModemDiagnoseSlot_Type = Integer32
_ZxAnDdnModemDiagnoseSlot_Object = MibTableColumn
zxAnDdnModemDiagnoseSlot = _ZxAnDdnModemDiagnoseSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1, 3),
    _ZxAnDdnModemDiagnoseSlot_Type()
)
zxAnDdnModemDiagnoseSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseSlot.setStatus("current")
_ZxAnDdnModemDiagnosePort_Type = Integer32
_ZxAnDdnModemDiagnosePort_Object = MibTableColumn
zxAnDdnModemDiagnosePort = _ZxAnDdnModemDiagnosePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1, 4),
    _ZxAnDdnModemDiagnosePort_Type()
)
zxAnDdnModemDiagnosePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnosePort.setStatus("current")


class _ZxAnDdnModemDiagnoseType_Type(Integer32):
    """Custom type zxAnDdnModemDiagnoseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("selfDiagnose", 1)
    )


_ZxAnDdnModemDiagnoseType_Type.__name__ = "Integer32"
_ZxAnDdnModemDiagnoseType_Object = MibTableColumn
zxAnDdnModemDiagnoseType = _ZxAnDdnModemDiagnoseType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1, 5),
    _ZxAnDdnModemDiagnoseType_Type()
)
zxAnDdnModemDiagnoseType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseType.setStatus("current")


class _ZxAnDdnModemDiagnoseStatus_Type(Integer32):
    """Custom type zxAnDdnModemDiagnoseStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnDdnModemDiagnoseStatus_Type.__name__ = "Integer32"
_ZxAnDdnModemDiagnoseStatus_Object = MibTableColumn
zxAnDdnModemDiagnoseStatus = _ZxAnDdnModemDiagnoseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 7, 3, 1, 6),
    _ZxAnDdnModemDiagnoseStatus_Type()
)
zxAnDdnModemDiagnoseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnDdnModemDiagnoseStatus.setStatus("current")
_ZxAnDdnGhdbCardTable_Object = MibTable
zxAnDdnGhdbCardTable = _ZxAnDdnGhdbCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 8)
)
if mibBuilder.loadTexts:
    zxAnDdnGhdbCardTable.setStatus("current")
_ZxAnDdnGhdbCardEntry_Object = MibTableRow
zxAnDdnGhdbCardEntry = _ZxAnDdnGhdbCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 8, 1)
)
zxAnDdnGhdbCardEntry.setIndexNames(
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnGhdbRack"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnGhdbShelf"),
    (0, "ZTE-AN-DDN-MIB", "zxAnDdnGhdbSlot"),
)
if mibBuilder.loadTexts:
    zxAnDdnGhdbCardEntry.setStatus("current")
_ZxAnDdnGhdbRack_Type = Integer32
_ZxAnDdnGhdbRack_Object = MibTableColumn
zxAnDdnGhdbRack = _ZxAnDdnGhdbRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 8, 1, 1),
    _ZxAnDdnGhdbRack_Type()
)
zxAnDdnGhdbRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnGhdbRack.setStatus("current")
_ZxAnDdnGhdbShelf_Type = Integer32
_ZxAnDdnGhdbShelf_Object = MibTableColumn
zxAnDdnGhdbShelf = _ZxAnDdnGhdbShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 8, 1, 2),
    _ZxAnDdnGhdbShelf_Type()
)
zxAnDdnGhdbShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnGhdbShelf.setStatus("current")
_ZxAnDdnGhdbSlot_Type = Integer32
_ZxAnDdnGhdbSlot_Object = MibTableColumn
zxAnDdnGhdbSlot = _ZxAnDdnGhdbSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 8, 1, 3),
    _ZxAnDdnGhdbSlot_Type()
)
zxAnDdnGhdbSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDdnGhdbSlot.setStatus("current")


class _ZxAnDdnGhdbWorkMode_Type(Integer32):
    """Custom type zxAnDdnGhdbWorkMode based on Integer32"""
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
        *(("tdm", 1),
          ("e1Transparent", 2),
          ("narrowbandConvergence", 3),
          ("cesopsn", 4),
          ("satop", 5),
          ("mixed", 6))
    )


_ZxAnDdnGhdbWorkMode_Type.__name__ = "Integer32"
_ZxAnDdnGhdbWorkMode_Object = MibTableColumn
zxAnDdnGhdbWorkMode = _ZxAnDdnGhdbWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 8, 1, 4),
    _ZxAnDdnGhdbWorkMode_Type()
)
zxAnDdnGhdbWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDdnGhdbWorkMode.setStatus("current")
_ZxAnDdnTrapObjects_ObjectIdentity = ObjectIdentity
zxAnDdnTrapObjects = _ZxAnDdnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 100)
)
_ZxAnDdnModemTrapGroup_ObjectIdentity = ObjectIdentity
zxAnDdnModemTrapGroup = _ZxAnDdnModemTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 100, 1)
)

# Managed Objects groups


# Notification objects

zxAnDdnModemLineStatusAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 100, 1, 1)
)
zxAnDdnModemLineStatusAbnormal.setObjects(
    ("ZTE-AN-DDN-MIB", "zxAnDdnModemLineStatus")
)
if mibBuilder.loadTexts:
    zxAnDdnModemLineStatusAbnormal.setStatus(
        "current"
    )

zxAnDdnModemLineStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 100, 1, 2)
)
zxAnDdnModemLineStatusNormal.setObjects(
    ("ZTE-AN-DDN-MIB", "zxAnDdnModemLineStatus")
)
if mibBuilder.loadTexts:
    zxAnDdnModemLineStatusNormal.setStatus(
        "current"
    )

zxAnDdnPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 100, 1, 3)
)
zxAnDdnPortLinkDown.setObjects(
    ("ZTE-AN-DDN-MIB", "zxAnDdnModemOperStatus")
)
if mibBuilder.loadTexts:
    zxAnDdnPortLinkDown.setStatus(
        "current"
    )

zxAnDdnPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 2, 100, 1, 4)
)
zxAnDdnPortLinkUp.setObjects(
    ("ZTE-AN-DDN-MIB", "zxAnDdnModemOperStatus")
)
if mibBuilder.loadTexts:
    zxAnDdnPortLinkUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DDN-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnDDNMib": zxAnDDNMib,
       "msagmajorVersion": msagmajorVersion,
       "msagDDNConfig": msagDDNConfig,
       "ddnPortTable": ddnPortTable,
       "ddnPortEntry": ddnPortEntry,
       "ddnPortRack": ddnPortRack,
       "ddnPortShelf": ddnPortShelf,
       "ddnPortSlot": ddnPortSlot,
       "ddnPortCircuit": ddnPortCircuit,
       "ddnPortTs": ddnPortTs,
       "ddnPortName": ddnPortName,
       "ddnPortMainType": ddnPortMainType,
       "ddnPortSubType": ddnPortSubType,
       "ddnPortRowStatus": ddnPortRowStatus,
       "ddnPortLoopback": ddnPortLoopback,
       "ddnConnectTable": ddnConnectTable,
       "ddnConnectEntry": ddnConnectEntry,
       "ddnConPort1Rack": ddnConPort1Rack,
       "ddnConPort1Shelf": ddnConPort1Shelf,
       "ddnConPort1Slot": ddnConPort1Slot,
       "ddnConPort1Circuit": ddnConPort1Circuit,
       "ddnConPort1Ts": ddnConPort1Ts,
       "ddnConPort1Name": ddnConPort1Name,
       "ddnConPort2Rack": ddnConPort2Rack,
       "ddnConPort2Shelf": ddnConPort2Shelf,
       "ddnConPort2Slot": ddnConPort2Slot,
       "ddnConPort2Circuit": ddnConPort2Circuit,
       "ddnConPort2Ts": ddnConPort2Ts,
       "ddnConPort2Name": ddnConPort2Name,
       "ddnConName": ddnConName,
       "ddnConnExOperType": ddnConnExOperType,
       "ddnConRowStatus": ddnConRowStatus,
       "hdbPortConfigTable": hdbPortConfigTable,
       "hdbPortConfigEntry": hdbPortConfigEntry,
       "hdbPCRack": hdbPCRack,
       "hdbPCShelf": hdbPCShelf,
       "hdbPCSlot": hdbPCSlot,
       "hdbPCPortNumber": hdbPCPortNumber,
       "audbPortConfigTable": audbPortConfigTable,
       "audbPortConfigEntry": audbPortConfigEntry,
       "audbPCRack": audbPCRack,
       "audbPCShelf": audbPCShelf,
       "audbPCSlot": audbPCSlot,
       "audbPCCircuit": audbPCCircuit,
       "audbPCTs": audbPCTs,
       "audbPortLineType": audbPortLineType,
       "audbPortInputGain": audbPortInputGain,
       "audbPortOutputGain": audbPortOutputGain,
       "audbPortLoopState": audbPortLoopState,
       "zxAnDdnBertMgmtGroup": zxAnDdnBertMgmtGroup,
       "zxAnDdnBertConfTable": zxAnDdnBertConfTable,
       "zxAnDdnBertConfEntry": zxAnDdnBertConfEntry,
       "zxAnDdnBertConfRack": zxAnDdnBertConfRack,
       "zxAnDdnBertConfShelf": zxAnDdnBertConfShelf,
       "zxAnDdnBertConfSlot": zxAnDdnBertConfSlot,
       "zxAnDdnBertConfCircuit": zxAnDdnBertConfCircuit,
       "zxAnDdnBertConfTs": zxAnDdnBertConfTs,
       "zxAnDdnBertAction": zxAnDdnBertAction,
       "zxAnDdnBertTestPattern": zxAnDdnBertTestPattern,
       "zxAnDdnBertUserPattern": zxAnDdnBertUserPattern,
       "zxAnDdnBertMode": zxAnDdnBertMode,
       "zxAnDdnBertDuration": zxAnDdnBertDuration,
       "zxAnDdnBertStartDateAndTime": zxAnDdnBertStartDateAndTime,
       "zxAnDdnBertOperStatus": zxAnDdnBertOperStatus,
       "zxAnDdnBertTargetType": zxAnDdnBertTargetType,
       "zxAnDdnBertRowStatus": zxAnDdnBertRowStatus,
       "zxAnDdnBertStatsTable": zxAnDdnBertStatsTable,
       "zxAnDdnBertStatsEntry": zxAnDdnBertStatsEntry,
       "zxAnDdnBertStatsRack": zxAnDdnBertStatsRack,
       "zxAnDdnBertStatsShelf": zxAnDdnBertStatsShelf,
       "zxAnDdnBertStatsSlot": zxAnDdnBertStatsSlot,
       "zxAnDdnBertStatsCircuit": zxAnDdnBertStatsCircuit,
       "zxAnDdnBertStatsTs": zxAnDdnBertStatsTs,
       "zxAnDdnBertRxTotalBits": zxAnDdnBertRxTotalBits,
       "zxAnDdnBertRxErrorBits": zxAnDdnBertRxErrorBits,
       "zxAnDdnBertRxBitErrorRatio": zxAnDdnBertRxBitErrorRatio,
       "zxAnDdnBertTimeElapsed": zxAnDdnBertTimeElapsed,
       "zxAnDdnBertEs": zxAnDdnBertEs,
       "zxAnDdnBertSes": zxAnDdnBertSes,
       "zxAnDdnBertUas": zxAnDdnBertUas,
       "zxAnDdnBertDm": zxAnDdnBertDm,
       "zxAnDdnBertBbe": zxAnDdnBertBbe,
       "zxAnDdnBertCses": zxAnDdnBertCses,
       "zxAnDdnModemMgmtGroup": zxAnDdnModemMgmtGroup,
       "zxAnDdnModemMgmtTable": zxAnDdnModemMgmtTable,
       "zxAnDdnModemMgmtEntry": zxAnDdnModemMgmtEntry,
       "zxAnDdnModemRack": zxAnDdnModemRack,
       "zxAnDdnModemShelf": zxAnDdnModemShelf,
       "zxAnDdnModemSlot": zxAnDdnModemSlot,
       "zxAnDdnModemPort": zxAnDdnModemPort,
       "zxAnDdnModemOperStatus": zxAnDdnModemOperStatus,
       "zxAnDdnModemConfigData": zxAnDdnModemConfigData,
       "zxAnDdnModemReset": zxAnDdnModemReset,
       "zxAnDdnModemSaveData": zxAnDdnModemSaveData,
       "zxAnDdnModemLineStatus": zxAnDdnModemLineStatus,
       "zxAnDdnModemQueryTable": zxAnDdnModemQueryTable,
       "zxAnDdnModemQueryEntry": zxAnDdnModemQueryEntry,
       "zxAnDdnModemQueryRack": zxAnDdnModemQueryRack,
       "zxAnDdnModemQueryShelf": zxAnDdnModemQueryShelf,
       "zxAnDdnModemQuerySlot": zxAnDdnModemQuerySlot,
       "zxAnDdnModemQueryPort": zxAnDdnModemQueryPort,
       "zxAnDdnModemQueryType": zxAnDdnModemQueryType,
       "zxAnDdnModemQueryStatus": zxAnDdnModemQueryStatus,
       "zxAnDdnModemQueryResult": zxAnDdnModemQueryResult,
       "zxAnDdnModemDiagnoseTable": zxAnDdnModemDiagnoseTable,
       "zxAnDdnModemDiagnoseEntry": zxAnDdnModemDiagnoseEntry,
       "zxAnDdnModemDiagnoseRack": zxAnDdnModemDiagnoseRack,
       "zxAnDdnModemDiagnoseShelf": zxAnDdnModemDiagnoseShelf,
       "zxAnDdnModemDiagnoseSlot": zxAnDdnModemDiagnoseSlot,
       "zxAnDdnModemDiagnosePort": zxAnDdnModemDiagnosePort,
       "zxAnDdnModemDiagnoseType": zxAnDdnModemDiagnoseType,
       "zxAnDdnModemDiagnoseStatus": zxAnDdnModemDiagnoseStatus,
       "zxAnDdnGhdbCardTable": zxAnDdnGhdbCardTable,
       "zxAnDdnGhdbCardEntry": zxAnDdnGhdbCardEntry,
       "zxAnDdnGhdbRack": zxAnDdnGhdbRack,
       "zxAnDdnGhdbShelf": zxAnDdnGhdbShelf,
       "zxAnDdnGhdbSlot": zxAnDdnGhdbSlot,
       "zxAnDdnGhdbWorkMode": zxAnDdnGhdbWorkMode,
       "zxAnDdnTrapObjects": zxAnDdnTrapObjects,
       "zxAnDdnModemTrapGroup": zxAnDdnModemTrapGroup,
       "zxAnDdnModemLineStatusAbnormal": zxAnDdnModemLineStatusAbnormal,
       "zxAnDdnModemLineStatusNormal": zxAnDdnModemLineStatusNormal,
       "zxAnDdnPortLinkDown": zxAnDdnPortLinkDown,
       "zxAnDdnPortLinkUp": zxAnDdnPortLinkUp}
)
