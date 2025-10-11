# SNMP MIB module (ZTE-AN-PORT-LOCATING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-PORT-LOCATING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:44 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnPortLocatingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZxAnAccessLoopTagType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("suboption81", 0),
          ("suboption82", 1),
          ("suboption83", 2),
          ("suboption84", 3),
          ("suboption85", 4),
          ("suboption86", 5),
          ("suboption87", 6),
          ("suboption88", 7),
          ("suboption89", 8),
          ("suboption8A", 9),
          ("suboption8B", 10),
          ("suboption8C", 11),
          ("suboption8D", 12),
          ("suboption8E", 13))
    )


# MIB Managed Objects in the order of their OIDs



class _ZxAnPortIdAccessNodeName_Type(DisplayString):
    """Custom type zxAnPortIdAccessNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnPortIdAccessNodeName_Type.__name__ = "DisplayString"
_ZxAnPortIdAccessNodeName_Object = MibScalar
zxAnPortIdAccessNodeName = _ZxAnPortIdAccessNodeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 1),
    _ZxAnPortIdAccessNodeName_Type()
)
zxAnPortIdAccessNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdAccessNodeName.setStatus("current")


class _ZxAnPortIdAccessNodeIdType_Type(Integer32):
    """Custom type zxAnPortIdAccessNodeIdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbandMac", 1),
          ("hostname", 2))
    )


_ZxAnPortIdAccessNodeIdType_Type.__name__ = "Integer32"
_ZxAnPortIdAccessNodeIdType_Object = MibScalar
zxAnPortIdAccessNodeIdType = _ZxAnPortIdAccessNodeIdType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 2),
    _ZxAnPortIdAccessNodeIdType_Type()
)
zxAnPortIdAccessNodeIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdAccessNodeIdType.setStatus("current")
_ZxAnPortIdRack_Type = Integer32
_ZxAnPortIdRack_Object = MibScalar
zxAnPortIdRack = _ZxAnPortIdRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 3),
    _ZxAnPortIdRack_Type()
)
zxAnPortIdRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdRack.setStatus("current")
_ZxAnPortIdShelf_Type = Integer32
_ZxAnPortIdShelf_Object = MibScalar
zxAnPortIdShelf = _ZxAnPortIdShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 4),
    _ZxAnPortIdShelf_Type()
)
zxAnPortIdShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdShelf.setStatus("current")


class _ZxAnPortLocatingCircuitIdSyntaxEnable_Type(Integer32):
    """Custom type zxAnPortLocatingCircuitIdSyntaxEnable based on Integer32"""
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


_ZxAnPortLocatingCircuitIdSyntaxEnable_Type.__name__ = "Integer32"
_ZxAnPortLocatingCircuitIdSyntaxEnable_Object = MibScalar
zxAnPortLocatingCircuitIdSyntaxEnable = _ZxAnPortLocatingCircuitIdSyntaxEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 5),
    _ZxAnPortLocatingCircuitIdSyntaxEnable_Type()
)
zxAnPortLocatingCircuitIdSyntaxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdSyntaxEnable.setStatus("current")


class _ZxAnPortLocatingAccessLoopEncapsulationEnable_Type(Integer32):
    """Custom type zxAnPortLocatingAccessLoopEncapsulationEnable based on Integer32"""
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


_ZxAnPortLocatingAccessLoopEncapsulationEnable_Type.__name__ = "Integer32"
_ZxAnPortLocatingAccessLoopEncapsulationEnable_Object = MibScalar
zxAnPortLocatingAccessLoopEncapsulationEnable = _ZxAnPortLocatingAccessLoopEncapsulationEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 6),
    _ZxAnPortLocatingAccessLoopEncapsulationEnable_Type()
)
zxAnPortLocatingAccessLoopEncapsulationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingAccessLoopEncapsulationEnable.setStatus("current")


class _ZxAnPortIdAccessNodeSlaveId_Type(DisplayString):
    """Custom type zxAnPortIdAccessNodeSlaveId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_ZxAnPortIdAccessNodeSlaveId_Type.__name__ = "DisplayString"
_ZxAnPortIdAccessNodeSlaveId_Object = MibScalar
zxAnPortIdAccessNodeSlaveId = _ZxAnPortIdAccessNodeSlaveId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 7),
    _ZxAnPortIdAccessNodeSlaveId_Type()
)
zxAnPortIdAccessNodeSlaveId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdAccessNodeSlaveId.setStatus("current")
_ZxAnPortIdDhcpV4AccessLoopChar_Type = ZxAnAccessLoopTagType
_ZxAnPortIdDhcpV4AccessLoopChar_Object = MibScalar
zxAnPortIdDhcpV4AccessLoopChar = _ZxAnPortIdDhcpV4AccessLoopChar_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 8),
    _ZxAnPortIdDhcpV4AccessLoopChar_Type()
)
zxAnPortIdDhcpV4AccessLoopChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdDhcpV4AccessLoopChar.setStatus("current")
_ZxAnPortIdPppoeAccessLoopChar_Type = ZxAnAccessLoopTagType
_ZxAnPortIdPppoeAccessLoopChar_Object = MibScalar
zxAnPortIdPppoeAccessLoopChar = _ZxAnPortIdPppoeAccessLoopChar_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 9),
    _ZxAnPortIdPppoeAccessLoopChar_Type()
)
zxAnPortIdPppoeAccessLoopChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdPppoeAccessLoopChar.setStatus("current")
_ZxAnPortLocatingTable_Object = MibTable
zxAnPortLocatingTable = _ZxAnPortLocatingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20)
)
if mibBuilder.loadTexts:
    zxAnPortLocatingTable.setStatus("current")
_ZxAnPortLocatingEntry_Object = MibTableRow
zxAnPortLocatingEntry = _ZxAnPortLocatingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1)
)
zxAnPortLocatingEntry.setIndexNames(
    (0, "ZTE-AN-PORT-LOCATING-MIB", "zxAnPortLocatingIndex"),
)
if mibBuilder.loadTexts:
    zxAnPortLocatingEntry.setStatus("current")
_ZxAnPortLocatingIndex_Type = ZxAnIfindex
_ZxAnPortLocatingIndex_Object = MibTableColumn
zxAnPortLocatingIndex = _ZxAnPortLocatingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 1),
    _ZxAnPortLocatingIndex_Type()
)
zxAnPortLocatingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingIndex.setStatus("current")


class _ZxAnPortIdIfConfFormat_Type(Integer32):
    """Custom type zxAnPortIdIfConfFormat based on Integer32"""
    defaultValue = 1

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("chinaTel", 1),
          ("dslForum", 2),
          ("chinaNet", 3),
          ("turkeyTel", 4),
          ("koreaTel", 5),
          ("telecomItalia", 6),
          ("singTel", 7),
          ("flexibleSyntax", 8),
          ("franceTel", 9),
          ("deutscheTel", 10),
          ("silknet", 11),
          ("vodafone", 12),
          ("bhartiAirtel", 13),
          ("formatProfile", 255))
    )


_ZxAnPortIdIfConfFormat_Type.__name__ = "Integer32"
_ZxAnPortIdIfConfFormat_Object = MibTableColumn
zxAnPortIdIfConfFormat = _ZxAnPortIdIfConfFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 2),
    _ZxAnPortIdIfConfFormat_Type()
)
zxAnPortIdIfConfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdIfConfFormat.setStatus("current")


class _ZxAnPortIdIfConfRidEnable_Type(Integer32):
    """Custom type zxAnPortIdIfConfRidEnable based on Integer32"""
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


_ZxAnPortIdIfConfRidEnable_Type.__name__ = "Integer32"
_ZxAnPortIdIfConfRidEnable_Object = MibTableColumn
zxAnPortIdIfConfRidEnable = _ZxAnPortIdIfConfRidEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 3),
    _ZxAnPortIdIfConfRidEnable_Type()
)
zxAnPortIdIfConfRidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdIfConfRidEnable.setStatus("current")


class _ZxAnPortIdIfConfRid_Type(DisplayString):
    """Custom type zxAnPortIdIfConfRid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnPortIdIfConfRid_Type.__name__ = "DisplayString"
_ZxAnPortIdIfConfRid_Object = MibTableColumn
zxAnPortIdIfConfRid = _ZxAnPortIdIfConfRid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 4),
    _ZxAnPortIdIfConfRid_Type()
)
zxAnPortIdIfConfRid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdIfConfRid.setStatus("current")


class _ZxAnPortLocatingIfaceAccessLoopCharEnable_Type(Integer32):
    """Custom type zxAnPortLocatingIfaceAccessLoopCharEnable based on Integer32"""
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


_ZxAnPortLocatingIfaceAccessLoopCharEnable_Type.__name__ = "Integer32"
_ZxAnPortLocatingIfaceAccessLoopCharEnable_Object = MibTableColumn
zxAnPortLocatingIfaceAccessLoopCharEnable = _ZxAnPortLocatingIfaceAccessLoopCharEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 5),
    _ZxAnPortLocatingIfaceAccessLoopCharEnable_Type()
)
zxAnPortLocatingIfaceAccessLoopCharEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingIfaceAccessLoopCharEnable.setStatus("current")


class _ZxAnPortIdIfConfUserDefinedCid_Type(DisplayString):
    """Custom type zxAnPortIdIfConfUserDefinedCid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnPortIdIfConfUserDefinedCid_Type.__name__ = "DisplayString"
_ZxAnPortIdIfConfUserDefinedCid_Object = MibTableColumn
zxAnPortIdIfConfUserDefinedCid = _ZxAnPortIdIfConfUserDefinedCid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 6),
    _ZxAnPortIdIfConfUserDefinedCid_Type()
)
zxAnPortIdIfConfUserDefinedCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdIfConfUserDefinedCid.setStatus("current")


class _ZxAnPortIdIfConfFormatProfile_Type(DisplayString):
    """Custom type zxAnPortIdIfConfFormatProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnPortIdIfConfFormatProfile_Type.__name__ = "DisplayString"
_ZxAnPortIdIfConfFormatProfile_Object = MibTableColumn
zxAnPortIdIfConfFormatProfile = _ZxAnPortIdIfConfFormatProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 7),
    _ZxAnPortIdIfConfFormatProfile_Type()
)
zxAnPortIdIfConfFormatProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdIfConfFormatProfile.setStatus("current")


class _ZxAnPortIdIfConfRidFormatProfile_Type(DisplayString):
    """Custom type zxAnPortIdIfConfRidFormatProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnPortIdIfConfRidFormatProfile_Type.__name__ = "DisplayString"
_ZxAnPortIdIfConfRidFormatProfile_Object = MibTableColumn
zxAnPortIdIfConfRidFormatProfile = _ZxAnPortIdIfConfRidFormatProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 20, 1, 8),
    _ZxAnPortIdIfConfRidFormatProfile_Type()
)
zxAnPortIdIfConfRidFormatProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortIdIfConfRidFormatProfile.setStatus("current")
_ZxAnPortLocatingCircuitIdSyntaxTable_Object = MibTable
zxAnPortLocatingCircuitIdSyntaxTable = _ZxAnPortLocatingCircuitIdSyntaxTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22)
)
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdSyntaxTable.setStatus("current")
_ZxAnPortLocatingCircuitIdSyntaxEntry_Object = MibTableRow
zxAnPortLocatingCircuitIdSyntaxEntry = _ZxAnPortLocatingCircuitIdSyntaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1)
)
zxAnPortLocatingCircuitIdSyntaxEntry.setIndexNames(
    (0, "ZTE-AN-PORT-LOCATING-MIB", "zxAnPortLocatingCircuitIdSyntaxIndex"),
    (0, "ZTE-AN-PORT-LOCATING-MIB", "zxAnPortLocatingCircuitIdComponentIndex"),
)
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdSyntaxEntry.setStatus("current")
_ZxAnPortLocatingCircuitIdSyntaxIndex_Type = Integer32
_ZxAnPortLocatingCircuitIdSyntaxIndex_Object = MibTableColumn
zxAnPortLocatingCircuitIdSyntaxIndex = _ZxAnPortLocatingCircuitIdSyntaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 1),
    _ZxAnPortLocatingCircuitIdSyntaxIndex_Type()
)
zxAnPortLocatingCircuitIdSyntaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdSyntaxIndex.setStatus("current")
_ZxAnPortLocatingCircuitIdComponentIndex_Type = Integer32
_ZxAnPortLocatingCircuitIdComponentIndex_Object = MibTableColumn
zxAnPortLocatingCircuitIdComponentIndex = _ZxAnPortLocatingCircuitIdComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 2),
    _ZxAnPortLocatingCircuitIdComponentIndex_Type()
)
zxAnPortLocatingCircuitIdComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdComponentIndex.setStatus("current")


class _ZxAnPortLocatingCircuitIdComponentType_Type(Integer32):
    """Custom type zxAnPortLocatingCircuitIdComponentType based on Integer32"""
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
        *(("standardVar", 1),
          ("extendedVar", 2),
          ("separator", 3),
          ("userDefinedString", 4))
    )


_ZxAnPortLocatingCircuitIdComponentType_Type.__name__ = "Integer32"
_ZxAnPortLocatingCircuitIdComponentType_Object = MibTableColumn
zxAnPortLocatingCircuitIdComponentType = _ZxAnPortLocatingCircuitIdComponentType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 3),
    _ZxAnPortLocatingCircuitIdComponentType_Type()
)
zxAnPortLocatingCircuitIdComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdComponentType.setStatus("current")
_ZxAnPortLocatingCircuitIdComponentId_Type = Integer32
_ZxAnPortLocatingCircuitIdComponentId_Object = MibTableColumn
zxAnPortLocatingCircuitIdComponentId = _ZxAnPortLocatingCircuitIdComponentId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 4),
    _ZxAnPortLocatingCircuitIdComponentId_Type()
)
zxAnPortLocatingCircuitIdComponentId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdComponentId.setStatus("current")
_ZxAnPortLocatingCircuitIdComponentWidth_Type = Integer32
_ZxAnPortLocatingCircuitIdComponentWidth_Object = MibTableColumn
zxAnPortLocatingCircuitIdComponentWidth = _ZxAnPortLocatingCircuitIdComponentWidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 5),
    _ZxAnPortLocatingCircuitIdComponentWidth_Type()
)
zxAnPortLocatingCircuitIdComponentWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdComponentWidth.setStatus("current")


class _ZxAnPortLocatingCidComponentStr_Type(DisplayString):
    """Custom type zxAnPortLocatingCidComponentStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_ZxAnPortLocatingCidComponentStr_Type.__name__ = "DisplayString"
_ZxAnPortLocatingCidComponentStr_Object = MibTableColumn
zxAnPortLocatingCidComponentStr = _ZxAnPortLocatingCidComponentStr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 6),
    _ZxAnPortLocatingCidComponentStr_Type()
)
zxAnPortLocatingCidComponentStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortLocatingCidComponentStr.setStatus("current")
_ZxAnPortLocatingCircuitIdComponentRowStatus_Type = RowStatus
_ZxAnPortLocatingCircuitIdComponentRowStatus_Object = MibTableColumn
zxAnPortLocatingCircuitIdComponentRowStatus = _ZxAnPortLocatingCircuitIdComponentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 22, 1, 20),
    _ZxAnPortLocatingCircuitIdComponentRowStatus_Type()
)
zxAnPortLocatingCircuitIdComponentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortLocatingCircuitIdComponentRowStatus.setStatus("current")
_ZxAnVlanPortLocatingObjects_ObjectIdentity = ObjectIdentity
zxAnVlanPortLocatingObjects = _ZxAnVlanPortLocatingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 25)
)


class _ZxAnVlanPortLocatingEnable_Type(TruthValue):
    """Custom type zxAnVlanPortLocatingEnable based on TruthValue"""
    defaultValue = 2


_ZxAnVlanPortLocatingEnable_Type.__name__ = "TruthValue"
_ZxAnVlanPortLocatingEnable_Object = MibScalar
zxAnVlanPortLocatingEnable = _ZxAnVlanPortLocatingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 25, 1),
    _ZxAnVlanPortLocatingEnable_Type()
)
zxAnVlanPortLocatingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVlanPortLocatingEnable.setStatus("current")
_ZxAnVlanPortLocatingTable_Object = MibTable
zxAnVlanPortLocatingTable = _ZxAnVlanPortLocatingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 25, 2)
)
if mibBuilder.loadTexts:
    zxAnVlanPortLocatingTable.setStatus("current")
_ZxAnVlanPortLocatingEntry_Object = MibTableRow
zxAnVlanPortLocatingEntry = _ZxAnVlanPortLocatingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 25, 2, 1)
)
zxAnVlanPortLocatingEntry.setIndexNames(
    (0, "ZTE-AN-PORT-LOCATING-MIB", "zxAnPortLocatingVlan"),
)
if mibBuilder.loadTexts:
    zxAnVlanPortLocatingEntry.setStatus("current")
_ZxAnPortLocatingVlan_Type = Integer32
_ZxAnPortLocatingVlan_Object = MibTableColumn
zxAnPortLocatingVlan = _ZxAnPortLocatingVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 25, 2, 1, 1),
    _ZxAnPortLocatingVlan_Type()
)
zxAnPortLocatingVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingVlan.setStatus("current")
_ZxAnPortLocatingVlanRowStatus_Type = RowStatus
_ZxAnPortLocatingVlanRowStatus_Object = MibTableColumn
zxAnPortLocatingVlanRowStatus = _ZxAnPortLocatingVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 25, 2, 1, 20),
    _ZxAnPortLocatingVlanRowStatus_Type()
)
zxAnPortLocatingVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortLocatingVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-PORT-LOCATING-MIB",
    **{"ZxAnAccessLoopTagType": ZxAnAccessLoopTagType,
       "zxAnPortLocatingMib": zxAnPortLocatingMib,
       "zxAnPortIdAccessNodeName": zxAnPortIdAccessNodeName,
       "zxAnPortIdAccessNodeIdType": zxAnPortIdAccessNodeIdType,
       "zxAnPortIdRack": zxAnPortIdRack,
       "zxAnPortIdShelf": zxAnPortIdShelf,
       "zxAnPortLocatingCircuitIdSyntaxEnable": zxAnPortLocatingCircuitIdSyntaxEnable,
       "zxAnPortLocatingAccessLoopEncapsulationEnable": zxAnPortLocatingAccessLoopEncapsulationEnable,
       "zxAnPortIdAccessNodeSlaveId": zxAnPortIdAccessNodeSlaveId,
       "zxAnPortIdDhcpV4AccessLoopChar": zxAnPortIdDhcpV4AccessLoopChar,
       "zxAnPortIdPppoeAccessLoopChar": zxAnPortIdPppoeAccessLoopChar,
       "zxAnPortLocatingTable": zxAnPortLocatingTable,
       "zxAnPortLocatingEntry": zxAnPortLocatingEntry,
       "zxAnPortLocatingIndex": zxAnPortLocatingIndex,
       "zxAnPortIdIfConfFormat": zxAnPortIdIfConfFormat,
       "zxAnPortIdIfConfRidEnable": zxAnPortIdIfConfRidEnable,
       "zxAnPortIdIfConfRid": zxAnPortIdIfConfRid,
       "zxAnPortLocatingIfaceAccessLoopCharEnable": zxAnPortLocatingIfaceAccessLoopCharEnable,
       "zxAnPortIdIfConfUserDefinedCid": zxAnPortIdIfConfUserDefinedCid,
       "zxAnPortIdIfConfFormatProfile": zxAnPortIdIfConfFormatProfile,
       "zxAnPortIdIfConfRidFormatProfile": zxAnPortIdIfConfRidFormatProfile,
       "zxAnPortLocatingCircuitIdSyntaxTable": zxAnPortLocatingCircuitIdSyntaxTable,
       "zxAnPortLocatingCircuitIdSyntaxEntry": zxAnPortLocatingCircuitIdSyntaxEntry,
       "zxAnPortLocatingCircuitIdSyntaxIndex": zxAnPortLocatingCircuitIdSyntaxIndex,
       "zxAnPortLocatingCircuitIdComponentIndex": zxAnPortLocatingCircuitIdComponentIndex,
       "zxAnPortLocatingCircuitIdComponentType": zxAnPortLocatingCircuitIdComponentType,
       "zxAnPortLocatingCircuitIdComponentId": zxAnPortLocatingCircuitIdComponentId,
       "zxAnPortLocatingCircuitIdComponentWidth": zxAnPortLocatingCircuitIdComponentWidth,
       "zxAnPortLocatingCidComponentStr": zxAnPortLocatingCidComponentStr,
       "zxAnPortLocatingCircuitIdComponentRowStatus": zxAnPortLocatingCircuitIdComponentRowStatus,
       "zxAnVlanPortLocatingObjects": zxAnVlanPortLocatingObjects,
       "zxAnVlanPortLocatingEnable": zxAnVlanPortLocatingEnable,
       "zxAnVlanPortLocatingTable": zxAnVlanPortLocatingTable,
       "zxAnVlanPortLocatingEntry": zxAnVlanPortLocatingEntry,
       "zxAnPortLocatingVlan": zxAnPortLocatingVlan,
       "zxAnPortLocatingVlanRowStatus": zxAnPortLocatingVlanRowStatus}
)
