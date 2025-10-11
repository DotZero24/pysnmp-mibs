# SNMP MIB module (BIANCA-BRICK-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bintec/BIANCA-BRICK-FR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:14 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Fr_ObjectIdentity = ObjectIdentity
fr = _Fr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 13)
)
_FrMprTable_Object = MibTable
frMprTable = _FrMprTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1)
)
if mibBuilder.loadTexts:
    frMprTable.setStatus("mandatory")
_FrMprEntry_Object = MibTableRow
frMprEntry = _FrMprEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1)
)
frMprEntry.setIndexNames(
    (0, "BIANCA-BRICK-FR-MIB", "frMprIfIndex"),
)
if mibBuilder.loadTexts:
    frMprEntry.setStatus("mandatory")


class _FrMprIfIndex_Type(Integer32):
    """Custom type frMprIfIndex based on Integer32"""
    defaultValue = 0


_FrMprIfIndex_Type.__name__ = "Integer32"
_FrMprIfIndex_Object = MibTableColumn
frMprIfIndex = _FrMprIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 1),
    _FrMprIfIndex_Type()
)
frMprIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMprIfIndex.setStatus("mandatory")


class _FrMprMtu_Type(Integer32):
    """Custom type frMprMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 8180),
    )


_FrMprMtu_Type.__name__ = "Integer32"
_FrMprMtu_Object = MibTableColumn
frMprMtu = _FrMprMtu_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 2),
    _FrMprMtu_Type()
)
frMprMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMprMtu.setStatus("mandatory")


class _FrMprEncapsulation_Type(Integer32):
    """Custom type frMprEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mpr", 1),
          ("delete", 7))
    )


_FrMprEncapsulation_Type.__name__ = "Integer32"
_FrMprEncapsulation_Object = MibTableColumn
frMprEncapsulation = _FrMprEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 3),
    _FrMprEncapsulation_Type()
)
frMprEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMprEncapsulation.setStatus("mandatory")


class _FrMprIfcType_Type(Integer32):
    """Custom type frMprIfcType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 1),
          ("point-to-point", 2))
    )


_FrMprIfcType_Type.__name__ = "Integer32"
_FrMprIfcType_Object = MibTableColumn
frMprIfcType = _FrMprIfcType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 4),
    _FrMprIfcType_Type()
)
frMprIfcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMprIfcType.setStatus("mandatory")


class _FrMprInverseArp_Type(Integer32):
    """Custom type frMprInverseArp based on Integer32"""
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


_FrMprInverseArp_Type.__name__ = "Integer32"
_FrMprInverseArp_Object = MibTableColumn
frMprInverseArp = _FrMprInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 5),
    _FrMprInverseArp_Type()
)
frMprInverseArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMprInverseArp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-FR-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "fr": fr,
       "frMprTable": frMprTable,
       "frMprEntry": frMprEntry,
       "frMprIfIndex": frMprIfIndex,
       "frMprMtu": frMprMtu,
       "frMprEncapsulation": frMprEncapsulation,
       "frMprIfcType": frMprIfcType,
       "frMprInverseArp": frMprInverseArp}
)
