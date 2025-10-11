# SNMP MIB module (ZTE-AN-VOICE-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VOICE-TRUNK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:33 2025
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

zxAnVoiceTrunkMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
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
_MsagEmConfig_ObjectIdentity = ObjectIdentity
msagEmConfig = _MsagEmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11)
)
_ZxAnEmCfgTable_Object = MibTable
zxAnEmCfgTable = _ZxAnEmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1)
)
if mibBuilder.loadTexts:
    zxAnEmCfgTable.setStatus("current")
_ZxAnEmCfgEntry_Object = MibTableRow
zxAnEmCfgEntry = _ZxAnEmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1)
)
zxAnEmCfgEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-TRUNK-MIB", "zxAnEmRack"),
    (0, "ZTE-AN-VOICE-TRUNK-MIB", "zxAnEmShelf"),
    (0, "ZTE-AN-VOICE-TRUNK-MIB", "zxAnEmSlot"),
)
if mibBuilder.loadTexts:
    zxAnEmCfgEntry.setStatus("current")


class _ZxAnEmRack_Type(Integer32):
    """Custom type zxAnEmRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnEmRack_Type.__name__ = "Integer32"
_ZxAnEmRack_Object = MibTableColumn
zxAnEmRack = _ZxAnEmRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 1),
    _ZxAnEmRack_Type()
)
zxAnEmRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEmRack.setStatus("current")


class _ZxAnEmShelf_Type(Integer32):
    """Custom type zxAnEmShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ZxAnEmShelf_Type.__name__ = "Integer32"
_ZxAnEmShelf_Object = MibTableColumn
zxAnEmShelf = _ZxAnEmShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 2),
    _ZxAnEmShelf_Type()
)
zxAnEmShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEmShelf.setStatus("current")


class _ZxAnEmSlot_Type(Integer32):
    """Custom type zxAnEmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ZxAnEmSlot_Type.__name__ = "Integer32"
_ZxAnEmSlot_Object = MibTableColumn
zxAnEmSlot = _ZxAnEmSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 3),
    _ZxAnEmSlot_Type()
)
zxAnEmSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEmSlot.setStatus("current")


class _ZxAnEmAudioIfType_Type(Integer32):
    """Custom type zxAnEmAudioIfType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("twoWire", 2),
          ("fourWire", 4))
    )


_ZxAnEmAudioIfType_Type.__name__ = "Integer32"
_ZxAnEmAudioIfType_Object = MibTableColumn
zxAnEmAudioIfType = _ZxAnEmAudioIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 4),
    _ZxAnEmAudioIfType_Type()
)
zxAnEmAudioIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEmAudioIfType.setStatus("current")


class _ZxAnEmIfType_Type(Integer32):
    """Custom type zxAnEmIfType based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("emTypeI", 1),
          ("emTypeV", 5))
    )


_ZxAnEmIfType_Type.__name__ = "Integer32"
_ZxAnEmIfType_Object = MibTableColumn
zxAnEmIfType = _ZxAnEmIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 5),
    _ZxAnEmIfType_Type()
)
zxAnEmIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEmIfType.setStatus("current")


class _ZxAnEmOutGain_Type(Integer32):
    """Custom type zxAnEmOutGain based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnEmOutGain_Type.__name__ = "Integer32"
_ZxAnEmOutGain_Object = MibTableColumn
zxAnEmOutGain = _ZxAnEmOutGain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 6),
    _ZxAnEmOutGain_Type()
)
zxAnEmOutGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEmOutGain.setStatus("current")


class _ZxAnEmInGain_Type(Integer32):
    """Custom type zxAnEmInGain based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnEmInGain_Type.__name__ = "Integer32"
_ZxAnEmInGain_Object = MibTableColumn
zxAnEmInGain = _ZxAnEmInGain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 11, 1, 1, 7),
    _ZxAnEmInGain_Type()
)
zxAnEmInGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEmInGain.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VOICE-TRUNK-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnVoiceTrunkMib": zxAnVoiceTrunkMib,
       "msagmajorVersion": msagmajorVersion,
       "msagEmConfig": msagEmConfig,
       "zxAnEmCfgTable": zxAnEmCfgTable,
       "zxAnEmCfgEntry": zxAnEmCfgEntry,
       "zxAnEmRack": zxAnEmRack,
       "zxAnEmShelf": zxAnEmShelf,
       "zxAnEmSlot": zxAnEmSlot,
       "zxAnEmAudioIfType": zxAnEmAudioIfType,
       "zxAnEmIfType": zxAnEmIfType,
       "zxAnEmOutGain": zxAnEmOutGain,
       "zxAnEmInGain": zxAnEmInGain}
)
