# SNMP MIB module (ZTE-AN-SHDSL-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-SHDSL-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:01 2025
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

(hdsl2ShdslMIB,
 hdsl2ShdslSpanConfEntry) = mibBuilder.importSymbols(
    "HDSL2-SHDSL-LINE-MIB",
    "hdsl2ShdslMIB",
    "hdsl2ShdslSpanConfEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

zxAnShdslExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002)
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
_ZxAnShdslExtObjects_ObjectIdentity = ObjectIdentity
zxAnShdslExtObjects = _ZxAnShdslExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1)
)
_ZxAnShdslSpanConfExtTable_Object = MibTable
zxAnShdslSpanConfExtTable = _ZxAnShdslSpanConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnShdslSpanConfExtTable.setStatus("current")
_ZxAnShdslSpanConfExtEntry_Object = MibTableRow
zxAnShdslSpanConfExtEntry = _ZxAnShdslSpanConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnShdslSpanConfExtEntry.setStatus("current")


class _ZxAnShdslSpanConfDataPathType_Type(Integer32):
    """Custom type zxAnShdslSpanConfDataPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("efm", 2),
          ("auto", 4))
    )


_ZxAnShdslSpanConfDataPathType_Type.__name__ = "Integer32"
_ZxAnShdslSpanConfDataPathType_Object = MibTableColumn
zxAnShdslSpanConfDataPathType = _ZxAnShdslSpanConfDataPathType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1, 1, 1),
    _ZxAnShdslSpanConfDataPathType_Type()
)
zxAnShdslSpanConfDataPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnShdslSpanConfDataPathType.setStatus("current")


class _ZxAnShdslSpanActualDataPathType_Type(Integer32):
    """Custom type zxAnShdslSpanActualDataPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("efm", 2))
    )


_ZxAnShdslSpanActualDataPathType_Type.__name__ = "Integer32"
_ZxAnShdslSpanActualDataPathType_Object = MibTableColumn
zxAnShdslSpanActualDataPathType = _ZxAnShdslSpanActualDataPathType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1, 1, 2),
    _ZxAnShdslSpanActualDataPathType_Type()
)
zxAnShdslSpanActualDataPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShdslSpanActualDataPathType.setStatus("current")


class _ZxAnShdslSpanConfPamConstellation_Type(Integer32):
    """Custom type zxAnShdslSpanConfPamConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tcpAM16", 1),
          ("tcpAM32", 2),
          ("auto", 4))
    )


_ZxAnShdslSpanConfPamConstellation_Type.__name__ = "Integer32"
_ZxAnShdslSpanConfPamConstellation_Object = MibTableColumn
zxAnShdslSpanConfPamConstellation = _ZxAnShdslSpanConfPamConstellation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1, 1, 3),
    _ZxAnShdslSpanConfPamConstellation_Type()
)
zxAnShdslSpanConfPamConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnShdslSpanConfPamConstellation.setStatus("current")


class _ZxAnShdslSpanActualPamConstellation_Type(Integer32):
    """Custom type zxAnShdslSpanActualPamConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcpAM16", 1),
          ("tcpAM32", 2))
    )


_ZxAnShdslSpanActualPamConstellation_Type.__name__ = "Integer32"
_ZxAnShdslSpanActualPamConstellation_Object = MibTableColumn
zxAnShdslSpanActualPamConstellation = _ZxAnShdslSpanActualPamConstellation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1, 1, 4),
    _ZxAnShdslSpanActualPamConstellation_Type()
)
zxAnShdslSpanActualPamConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShdslSpanActualPamConstellation.setStatus("current")
_ZxAnShdslSpanActualTransmitPower_Type = Integer32
_ZxAnShdslSpanActualTransmitPower_Object = MibTableColumn
zxAnShdslSpanActualTransmitPower = _ZxAnShdslSpanActualTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 1, 1, 1, 5),
    _ZxAnShdslSpanActualTransmitPower_Type()
)
zxAnShdslSpanActualTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShdslSpanActualTransmitPower.setStatus("current")
if mibBuilder.loadTexts:
    zxAnShdslSpanActualTransmitPower.setUnits("0.1 dBm")
_ZxAnShdslExtGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnShdslExtGlobalObjects = _ZxAnShdslExtGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 2)
)


class _ZxAnShdslCapabilities_Type(Bits):
    """Custom type zxAnShdslCapabilities based on Bits"""
    namedValues = NamedValues(
        ("rfc4319", 0)
    )

_ZxAnShdslCapabilities_Type.__name__ = "Bits"
_ZxAnShdslCapabilities_Object = MibScalar
zxAnShdslCapabilities = _ZxAnShdslCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1002, 2, 1),
    _ZxAnShdslCapabilities_Type()
)
zxAnShdslCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShdslCapabilities.setStatus("current")
hdsl2ShdslSpanConfEntry.registerAugmentions(
    ("ZTE-AN-SHDSL-EXT-MIB",
     "zxAnShdslSpanConfExtEntry")
)
zxAnShdslSpanConfExtEntry.setIndexNames(*hdsl2ShdslSpanConfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SHDSL-EXT-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnShdslExtMib": zxAnShdslExtMib,
       "zxAnShdslExtObjects": zxAnShdslExtObjects,
       "zxAnShdslSpanConfExtTable": zxAnShdslSpanConfExtTable,
       "zxAnShdslSpanConfExtEntry": zxAnShdslSpanConfExtEntry,
       "zxAnShdslSpanConfDataPathType": zxAnShdslSpanConfDataPathType,
       "zxAnShdslSpanActualDataPathType": zxAnShdslSpanActualDataPathType,
       "zxAnShdslSpanConfPamConstellation": zxAnShdslSpanConfPamConstellation,
       "zxAnShdslSpanActualPamConstellation": zxAnShdslSpanActualPamConstellation,
       "zxAnShdslSpanActualTransmitPower": zxAnShdslSpanActualTransmitPower,
       "zxAnShdslExtGlobalObjects": zxAnShdslExtGlobalObjects,
       "zxAnShdslCapabilities": zxAnShdslCapabilities}
)
