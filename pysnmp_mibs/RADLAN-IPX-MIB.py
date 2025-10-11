# SNMP MIB module (RADLAN-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/RADLAN-IPX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:11:40 2025
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

(rndIPX,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rndIPX")

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


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RndIPXdriver_ObjectIdentity = ObjectIdentity
rndIPXdriver = _RndIPXdriver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 1)
)
_RndIPXRip_ObjectIdentity = ObjectIdentity
rndIPXRip = _RndIPXRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 2)
)
_RndIPXRipFilterGlbTable_Object = MibTable
rndIPXRipFilterGlbTable = _RndIPXRipFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10)
)
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbTable.setStatus("mandatory")
_RndIPXRipFilterGlbEntry_Object = MibTableRow
rndIPXRipFilterGlbEntry = _RndIPXRipFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1)
)
rndIPXRipFilterGlbEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "rndIPXRipFilterGlbFLtype"),
    (0, "RADLAN-IPX-MIB", "rndIPXRipFilterGlbFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbEntry.setStatus("mandatory")


class _RndIPXRipFilterGlbFLtype_Type(Integer32):
    """Custom type rndIPXRipFilterGlbFLtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RndIPXRipFilterGlbFLtype_Type.__name__ = "Integer32"
_RndIPXRipFilterGlbFLtype_Object = MibTableColumn
rndIPXRipFilterGlbFLtype = _RndIPXRipFilterGlbFLtype_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 1),
    _RndIPXRipFilterGlbFLtype_Type()
)
rndIPXRipFilterGlbFLtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLtype.setStatus("mandatory")
_RndIPXRipFilterGlbFLnumber_Type = Integer32
_RndIPXRipFilterGlbFLnumber_Object = MibTableColumn
rndIPXRipFilterGlbFLnumber = _RndIPXRipFilterGlbFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 2),
    _RndIPXRipFilterGlbFLnumber_Type()
)
rndIPXRipFilterGlbFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLnumber.setStatus("mandatory")


class _RndIPXRipFilterGlbFLStatus_Type(Integer32):
    """Custom type rndIPXRipFilterGlbFLStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("underCreation", 3))
    )


_RndIPXRipFilterGlbFLStatus_Type.__name__ = "Integer32"
_RndIPXRipFilterGlbFLStatus_Object = MibTableColumn
rndIPXRipFilterGlbFLStatus = _RndIPXRipFilterGlbFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 3),
    _RndIPXRipFilterGlbFLStatus_Type()
)
rndIPXRipFilterGlbFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLStatus.setStatus("mandatory")


class _RndIPXRipFilterGlbFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXRipFilterGlbFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXRipFilterGlbFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXRipFilterGlbFLnetworkPatern_Object = MibTableColumn
rndIPXRipFilterGlbFLnetworkPatern = _RndIPXRipFilterGlbFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 4),
    _RndIPXRipFilterGlbFLnetworkPatern_Type()
)
rndIPXRipFilterGlbFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLnetworkPatern.setStatus("mandatory")


class _RndIPXRipFilterGlbFLnetworkMask_Type(OctetString):
    """Custom type rndIPXRipFilterGlbFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXRipFilterGlbFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXRipFilterGlbFLnetworkMask_Object = MibTableColumn
rndIPXRipFilterGlbFLnetworkMask = _RndIPXRipFilterGlbFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 5),
    _RndIPXRipFilterGlbFLnetworkMask_Type()
)
rndIPXRipFilterGlbFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLnetworkMask.setStatus("mandatory")


class _RndIPXRipFilterGlbFLaction_Type(Integer32):
    """Custom type rndIPXRipFilterGlbFLaction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RndIPXRipFilterGlbFLaction_Type.__name__ = "Integer32"
_RndIPXRipFilterGlbFLaction_Object = MibTableColumn
rndIPXRipFilterGlbFLaction = _RndIPXRipFilterGlbFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 10, 1, 6),
    _RndIPXRipFilterGlbFLaction_Type()
)
rndIPXRipFilterGlbFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterGlbFLaction.setStatus("mandatory")
_RndIPXRipFilterCircuitTable_Object = MibTable
rndIPXRipFilterCircuitTable = _RndIPXRipFilterCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11)
)
if mibBuilder.loadTexts:
    rndIPXRipFilterCircuitTable.setStatus("mandatory")
_RndIPXRipFilterCircuitEntry_Object = MibTableRow
rndIPXRipFilterCircuitEntry = _RndIPXRipFilterCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1)
)
rndIPXRipFilterCircuitEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "rndIPXRipFilterCircFLIfIndex"),
    (0, "RADLAN-IPX-MIB", "rndIPXRipFilterCircFLType"),
    (0, "RADLAN-IPX-MIB", "rndIPXRipFilterCircFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXRipFilterCircuitEntry.setStatus("mandatory")
_RndIPXRipFilterCircFLIfIndex_Type = Integer32
_RndIPXRipFilterCircFLIfIndex_Object = MibTableColumn
rndIPXRipFilterCircFLIfIndex = _RndIPXRipFilterCircFLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 1),
    _RndIPXRipFilterCircFLIfIndex_Type()
)
rndIPXRipFilterCircFLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLIfIndex.setStatus("mandatory")


class _RndIPXRipFilterCircFLType_Type(Integer32):
    """Custom type rndIPXRipFilterCircFLType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RndIPXRipFilterCircFLType_Type.__name__ = "Integer32"
_RndIPXRipFilterCircFLType_Object = MibTableColumn
rndIPXRipFilterCircFLType = _RndIPXRipFilterCircFLType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 2),
    _RndIPXRipFilterCircFLType_Type()
)
rndIPXRipFilterCircFLType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLType.setStatus("mandatory")
_RndIPXRipFilterCircFLnumber_Type = Integer32
_RndIPXRipFilterCircFLnumber_Object = MibTableColumn
rndIPXRipFilterCircFLnumber = _RndIPXRipFilterCircFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 3),
    _RndIPXRipFilterCircFLnumber_Type()
)
rndIPXRipFilterCircFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLnumber.setStatus("mandatory")


class _RndIPXRipFilterCircFLStatus_Type(Integer32):
    """Custom type rndIPXRipFilterCircFLStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("underCreation", 3))
    )


_RndIPXRipFilterCircFLStatus_Type.__name__ = "Integer32"
_RndIPXRipFilterCircFLStatus_Object = MibTableColumn
rndIPXRipFilterCircFLStatus = _RndIPXRipFilterCircFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 4),
    _RndIPXRipFilterCircFLStatus_Type()
)
rndIPXRipFilterCircFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLStatus.setStatus("mandatory")


class _RndIPXRipFilterCircFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXRipFilterCircFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXRipFilterCircFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXRipFilterCircFLnetworkPatern_Object = MibTableColumn
rndIPXRipFilterCircFLnetworkPatern = _RndIPXRipFilterCircFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 5),
    _RndIPXRipFilterCircFLnetworkPatern_Type()
)
rndIPXRipFilterCircFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLnetworkPatern.setStatus("mandatory")


class _RndIPXRipFilterCircFLnetworkMask_Type(OctetString):
    """Custom type rndIPXRipFilterCircFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXRipFilterCircFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXRipFilterCircFLnetworkMask_Object = MibTableColumn
rndIPXRipFilterCircFLnetworkMask = _RndIPXRipFilterCircFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 6),
    _RndIPXRipFilterCircFLnetworkMask_Type()
)
rndIPXRipFilterCircFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLnetworkMask.setStatus("mandatory")


class _RndIPXRipFilterCircFLaction_Type(Integer32):
    """Custom type rndIPXRipFilterCircFLaction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RndIPXRipFilterCircFLaction_Type.__name__ = "Integer32"
_RndIPXRipFilterCircFLaction_Object = MibTableColumn
rndIPXRipFilterCircFLaction = _RndIPXRipFilterCircFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 2, 11, 1, 7),
    _RndIPXRipFilterCircFLaction_Type()
)
rndIPXRipFilterCircFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXRipFilterCircFLaction.setStatus("mandatory")
_RndIPXSap_ObjectIdentity = ObjectIdentity
rndIPXSap = _RndIPXSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 3)
)
_RndIPXSapFilterGlbTable_Object = MibTable
rndIPXSapFilterGlbTable = _RndIPXSapFilterGlbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10)
)
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbTable.setStatus("mandatory")
_RndIPXSapFilterGlbEntry_Object = MibTableRow
rndIPXSapFilterGlbEntry = _RndIPXSapFilterGlbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1)
)
rndIPXSapFilterGlbEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "rndIPXSapFilterGlbFLtype"),
    (0, "RADLAN-IPX-MIB", "rndIPXSapFilterGlbFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbEntry.setStatus("mandatory")


class _RndIPXSapFilterGlbFLtype_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RndIPXSapFilterGlbFLtype_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLtype_Object = MibTableColumn
rndIPXSapFilterGlbFLtype = _RndIPXSapFilterGlbFLtype_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 1),
    _RndIPXSapFilterGlbFLtype_Type()
)
rndIPXSapFilterGlbFLtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLtype.setStatus("mandatory")
_RndIPXSapFilterGlbFLnumber_Type = Integer32
_RndIPXSapFilterGlbFLnumber_Object = MibTableColumn
rndIPXSapFilterGlbFLnumber = _RndIPXSapFilterGlbFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 2),
    _RndIPXSapFilterGlbFLnumber_Type()
)
rndIPXSapFilterGlbFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLnumber.setStatus("mandatory")


class _RndIPXSapFilterGlbFLStatus_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("underCreation", 3))
    )


_RndIPXSapFilterGlbFLStatus_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLStatus_Object = MibTableColumn
rndIPXSapFilterGlbFLStatus = _RndIPXSapFilterGlbFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 3),
    _RndIPXSapFilterGlbFLStatus_Type()
)
rndIPXSapFilterGlbFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLStatus.setStatus("mandatory")


class _RndIPXSapFilterGlbFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXSapFilterGlbFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXSapFilterGlbFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXSapFilterGlbFLnetworkPatern_Object = MibTableColumn
rndIPXSapFilterGlbFLnetworkPatern = _RndIPXSapFilterGlbFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 4),
    _RndIPXSapFilterGlbFLnetworkPatern_Type()
)
rndIPXSapFilterGlbFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLnetworkPatern.setStatus("mandatory")


class _RndIPXSapFilterGlbFLnetworkMask_Type(OctetString):
    """Custom type rndIPXSapFilterGlbFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXSapFilterGlbFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXSapFilterGlbFLnetworkMask_Object = MibTableColumn
rndIPXSapFilterGlbFLnetworkMask = _RndIPXSapFilterGlbFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 5),
    _RndIPXSapFilterGlbFLnetworkMask_Type()
)
rndIPXSapFilterGlbFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLnetworkMask.setStatus("mandatory")


class _RndIPXSapFilterGlbFLserviceType_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLserviceType based on Integer32"""
    defaultValue = 65535


_RndIPXSapFilterGlbFLserviceType_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLserviceType_Object = MibTableColumn
rndIPXSapFilterGlbFLserviceType = _RndIPXSapFilterGlbFLserviceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 6),
    _RndIPXSapFilterGlbFLserviceType_Type()
)
rndIPXSapFilterGlbFLserviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLserviceType.setStatus("mandatory")


class _RndIPXSapFilterGlbFLserviceName_Type(OctetString):
    """Custom type rndIPXSapFilterGlbFLserviceName based on OctetString"""
    defaultValue = OctetString("*")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RndIPXSapFilterGlbFLserviceName_Type.__name__ = "OctetString"
_RndIPXSapFilterGlbFLserviceName_Object = MibTableColumn
rndIPXSapFilterGlbFLserviceName = _RndIPXSapFilterGlbFLserviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 7),
    _RndIPXSapFilterGlbFLserviceName_Type()
)
rndIPXSapFilterGlbFLserviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLserviceName.setStatus("mandatory")


class _RndIPXSapFilterGlbFLaction_Type(Integer32):
    """Custom type rndIPXSapFilterGlbFLaction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RndIPXSapFilterGlbFLaction_Type.__name__ = "Integer32"
_RndIPXSapFilterGlbFLaction_Object = MibTableColumn
rndIPXSapFilterGlbFLaction = _RndIPXSapFilterGlbFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 10, 1, 8),
    _RndIPXSapFilterGlbFLaction_Type()
)
rndIPXSapFilterGlbFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterGlbFLaction.setStatus("mandatory")
_RndIPXSapFilterCircuitTable_Object = MibTable
rndIPXSapFilterCircuitTable = _RndIPXSapFilterCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11)
)
if mibBuilder.loadTexts:
    rndIPXSapFilterCircuitTable.setStatus("mandatory")
_RndIPXSapFilterCircuitEntry_Object = MibTableRow
rndIPXSapFilterCircuitEntry = _RndIPXSapFilterCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1)
)
rndIPXSapFilterCircuitEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "rndIPXSapFilterCircFLIfIndex"),
    (0, "RADLAN-IPX-MIB", "rndIPXSapFilterCircFLtype"),
    (0, "RADLAN-IPX-MIB", "rndIPXSapFilterCircFLnumber"),
)
if mibBuilder.loadTexts:
    rndIPXSapFilterCircuitEntry.setStatus("mandatory")
_RndIPXSapFilterCircFLIfIndex_Type = Integer32
_RndIPXSapFilterCircFLIfIndex_Object = MibTableColumn
rndIPXSapFilterCircFLIfIndex = _RndIPXSapFilterCircFLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 1),
    _RndIPXSapFilterCircFLIfIndex_Type()
)
rndIPXSapFilterCircFLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLIfIndex.setStatus("mandatory")


class _RndIPXSapFilterCircFLtype_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_RndIPXSapFilterCircFLtype_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLtype_Object = MibTableColumn
rndIPXSapFilterCircFLtype = _RndIPXSapFilterCircFLtype_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 2),
    _RndIPXSapFilterCircFLtype_Type()
)
rndIPXSapFilterCircFLtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLtype.setStatus("mandatory")
_RndIPXSapFilterCircFLnumber_Type = Integer32
_RndIPXSapFilterCircFLnumber_Object = MibTableColumn
rndIPXSapFilterCircFLnumber = _RndIPXSapFilterCircFLnumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 3),
    _RndIPXSapFilterCircFLnumber_Type()
)
rndIPXSapFilterCircFLnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLnumber.setStatus("mandatory")


class _RndIPXSapFilterCircFLStatus_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("underCreation", 3))
    )


_RndIPXSapFilterCircFLStatus_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLStatus_Object = MibTableColumn
rndIPXSapFilterCircFLStatus = _RndIPXSapFilterCircFLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 4),
    _RndIPXSapFilterCircFLStatus_Type()
)
rndIPXSapFilterCircFLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLStatus.setStatus("mandatory")


class _RndIPXSapFilterCircFLnetworkPatern_Type(OctetString):
    """Custom type rndIPXSapFilterCircFLnetworkPatern based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXSapFilterCircFLnetworkPatern_Type.__name__ = "OctetString"
_RndIPXSapFilterCircFLnetworkPatern_Object = MibTableColumn
rndIPXSapFilterCircFLnetworkPatern = _RndIPXSapFilterCircFLnetworkPatern_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 5),
    _RndIPXSapFilterCircFLnetworkPatern_Type()
)
rndIPXSapFilterCircFLnetworkPatern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLnetworkPatern.setStatus("mandatory")


class _RndIPXSapFilterCircFLnetworkMask_Type(OctetString):
    """Custom type rndIPXSapFilterCircFLnetworkMask based on OctetString"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RndIPXSapFilterCircFLnetworkMask_Type.__name__ = "OctetString"
_RndIPXSapFilterCircFLnetworkMask_Object = MibTableColumn
rndIPXSapFilterCircFLnetworkMask = _RndIPXSapFilterCircFLnetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 6),
    _RndIPXSapFilterCircFLnetworkMask_Type()
)
rndIPXSapFilterCircFLnetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLnetworkMask.setStatus("mandatory")


class _RndIPXSapFilterCircFLserviceType_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLserviceType based on Integer32"""
    defaultValue = 65535


_RndIPXSapFilterCircFLserviceType_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLserviceType_Object = MibTableColumn
rndIPXSapFilterCircFLserviceType = _RndIPXSapFilterCircFLserviceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 7),
    _RndIPXSapFilterCircFLserviceType_Type()
)
rndIPXSapFilterCircFLserviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLserviceType.setStatus("mandatory")


class _RndIPXSapFilterCircFLserviceName_Type(OctetString):
    """Custom type rndIPXSapFilterCircFLserviceName based on OctetString"""
    defaultValue = OctetString("*")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RndIPXSapFilterCircFLserviceName_Type.__name__ = "OctetString"
_RndIPXSapFilterCircFLserviceName_Object = MibTableColumn
rndIPXSapFilterCircFLserviceName = _RndIPXSapFilterCircFLserviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 8),
    _RndIPXSapFilterCircFLserviceName_Type()
)
rndIPXSapFilterCircFLserviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLserviceName.setStatus("mandatory")


class _RndIPXSapFilterCircFLaction_Type(Integer32):
    """Custom type rndIPXSapFilterCircFLaction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_RndIPXSapFilterCircFLaction_Type.__name__ = "Integer32"
_RndIPXSapFilterCircFLaction_Object = MibTableColumn
rndIPXSapFilterCircFLaction = _RndIPXSapFilterCircFLaction_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 3, 11, 1, 9),
    _RndIPXSapFilterCircFLaction_Type()
)
rndIPXSapFilterCircFLaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIPXSapFilterCircFLaction.setStatus("mandatory")
_IpxSystem_ObjectIdentity = ObjectIdentity
ipxSystem = _IpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 4)
)
_IpxBasicSysTable_Object = MibTable
ipxBasicSysTable = _IpxBasicSysTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1)
)
if mibBuilder.loadTexts:
    ipxBasicSysTable.setStatus("mandatory")
_IpxBasicSysEntry_Object = MibTableRow
ipxBasicSysEntry = _IpxBasicSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1)
)
ipxBasicSysEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "ipxBasicSysInstance"),
)
if mibBuilder.loadTexts:
    ipxBasicSysEntry.setStatus("mandatory")
_IpxBasicSysInstance_Type = Integer32
_IpxBasicSysInstance_Object = MibTableColumn
ipxBasicSysInstance = _IpxBasicSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 1),
    _IpxBasicSysInstance_Type()
)
ipxBasicSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysInstance.setStatus("mandatory")


class _IpxBasicSysExistState_Type(Integer32):
    """Custom type ipxBasicSysExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxBasicSysExistState_Type.__name__ = "Integer32"
_IpxBasicSysExistState_Object = MibTableColumn
ipxBasicSysExistState = _IpxBasicSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 2),
    _IpxBasicSysExistState_Type()
)
ipxBasicSysExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysExistState.setStatus("mandatory")
_IpxBasicSysInReceives_Type = Counter32
_IpxBasicSysInReceives_Object = MibTableColumn
ipxBasicSysInReceives = _IpxBasicSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 3),
    _IpxBasicSysInReceives_Type()
)
ipxBasicSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInReceives.setStatus("mandatory")
_IpxBasicSysInHdrErrors_Type = Counter32
_IpxBasicSysInHdrErrors_Object = MibTableColumn
ipxBasicSysInHdrErrors = _IpxBasicSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 4),
    _IpxBasicSysInHdrErrors_Type()
)
ipxBasicSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInHdrErrors.setStatus("mandatory")
_IpxBasicSysInUnknownSockets_Type = Counter32
_IpxBasicSysInUnknownSockets_Object = MibTableColumn
ipxBasicSysInUnknownSockets = _IpxBasicSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 5),
    _IpxBasicSysInUnknownSockets_Type()
)
ipxBasicSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInUnknownSockets.setStatus("mandatory")
_IpxBasicSysInDiscards_Type = Counter32
_IpxBasicSysInDiscards_Object = MibTableColumn
ipxBasicSysInDiscards = _IpxBasicSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 6),
    _IpxBasicSysInDiscards_Type()
)
ipxBasicSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDiscards.setStatus("mandatory")
_IpxBasicSysInDelivers_Type = Counter32
_IpxBasicSysInDelivers_Object = MibTableColumn
ipxBasicSysInDelivers = _IpxBasicSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 7),
    _IpxBasicSysInDelivers_Type()
)
ipxBasicSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDelivers.setStatus("mandatory")
_IpxBasicSysNoRoutes_Type = Counter32
_IpxBasicSysNoRoutes_Object = MibTableColumn
ipxBasicSysNoRoutes = _IpxBasicSysNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 8),
    _IpxBasicSysNoRoutes_Type()
)
ipxBasicSysNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysNoRoutes.setStatus("mandatory")
_IpxBasicSysOutRequests_Type = Counter32
_IpxBasicSysOutRequests_Object = MibTableColumn
ipxBasicSysOutRequests = _IpxBasicSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 9),
    _IpxBasicSysOutRequests_Type()
)
ipxBasicSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutRequests.setStatus("mandatory")
_IpxBasicSysOutMalformedRequests_Type = Counter32
_IpxBasicSysOutMalformedRequests_Object = MibTableColumn
ipxBasicSysOutMalformedRequests = _IpxBasicSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 10),
    _IpxBasicSysOutMalformedRequests_Type()
)
ipxBasicSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutMalformedRequests.setStatus("mandatory")
_IpxBasicSysOutDiscards_Type = Counter32
_IpxBasicSysOutDiscards_Object = MibTableColumn
ipxBasicSysOutDiscards = _IpxBasicSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 11),
    _IpxBasicSysOutDiscards_Type()
)
ipxBasicSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutDiscards.setStatus("mandatory")
_IpxBasicSysOutPackets_Type = Counter32
_IpxBasicSysOutPackets_Object = MibTableColumn
ipxBasicSysOutPackets = _IpxBasicSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 4, 1, 1, 12),
    _IpxBasicSysOutPackets_Type()
)
ipxBasicSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutPackets.setStatus("mandatory")
_IpxCircuit_ObjectIdentity = ObjectIdentity
ipxCircuit = _IpxCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 5)
)
_IpxCircTable_Object = MibTable
ipxCircTable = _IpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ipxCircTable.setStatus("mandatory")
_IpxCircEntry_Object = MibTableRow
ipxCircEntry = _IpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1)
)
ipxCircEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "ipxCircSysInstance"),
    (0, "RADLAN-IPX-MIB", "ipxCircIndex"),
)
if mibBuilder.loadTexts:
    ipxCircEntry.setStatus("mandatory")
_IpxCircSysInstance_Type = Integer32
_IpxCircSysInstance_Object = MibTableColumn
ipxCircSysInstance = _IpxCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 1),
    _IpxCircSysInstance_Type()
)
ipxCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSysInstance.setStatus("mandatory")
_IpxCircIndex_Type = Integer32
_IpxCircIndex_Object = MibTableColumn
ipxCircIndex = _IpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 2),
    _IpxCircIndex_Type()
)
ipxCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIndex.setStatus("mandatory")


class _IpxCircExistState_Type(Integer32):
    """Custom type ipxCircExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("sleeping", 3))
    )


_IpxCircExistState_Type.__name__ = "Integer32"
_IpxCircExistState_Object = MibTableColumn
ipxCircExistState = _IpxCircExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 3),
    _IpxCircExistState_Type()
)
ipxCircExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircExistState.setStatus("mandatory")


class _IpxCircOperState_Type(Integer32):
    """Custom type ipxCircOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("dormant", 3))
    )


_IpxCircOperState_Type.__name__ = "Integer32"
_IpxCircOperState_Object = MibTableColumn
ipxCircOperState = _IpxCircOperState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 4),
    _IpxCircOperState_Type()
)
ipxCircOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircOperState.setStatus("mandatory")
_IpxCircIfIndex_Type = Integer32
_IpxCircIfIndex_Object = MibTableColumn
ipxCircIfIndex = _IpxCircIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 5),
    _IpxCircIfIndex_Type()
)
ipxCircIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircIfIndex.setStatus("mandatory")
_IpxCircNetNumber_Type = NetNumber
_IpxCircNetNumber_Object = MibTableColumn
ipxCircNetNumber = _IpxCircNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 6),
    _IpxCircNetNumber_Type()
)
ipxCircNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetNumber.setStatus("mandatory")


class _IpxCircTimeToNet_Type(Integer32):
    """Custom type ipxCircTimeToNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpxCircTimeToNet_Type.__name__ = "Integer32"
_IpxCircTimeToNet_Object = MibTableColumn
ipxCircTimeToNet = _IpxCircTimeToNet_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 7),
    _IpxCircTimeToNet_Type()
)
ipxCircTimeToNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircTimeToNet.setStatus("mandatory")


class _IpxCircEncaps_Type(Integer32):
    """Custom type ipxCircEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("novell", 1),
          ("ethernet", 2),
          ("llc", 3),
          ("snap", 4),
          ("none", 10))
    )


_IpxCircEncaps_Type.__name__ = "Integer32"
_IpxCircEncaps_Object = MibTableColumn
ipxCircEncaps = _IpxCircEncaps_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 8),
    _IpxCircEncaps_Type()
)
ipxCircEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircEncaps.setStatus("mandatory")


class _IpxCircNetbiosDeliver_Type(Integer32):
    """Custom type ipxCircNetbiosDeliver based on Integer32"""
    defaultValue = 1

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


_IpxCircNetbiosDeliver_Type.__name__ = "Integer32"
_IpxCircNetbiosDeliver_Object = MibTableColumn
ipxCircNetbiosDeliver = _IpxCircNetbiosDeliver_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 5, 1, 1, 9),
    _IpxCircNetbiosDeliver_Type()
)
ipxCircNetbiosDeliver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetbiosDeliver.setStatus("mandatory")
_IpxForwarding_ObjectIdentity = ObjectIdentity
ipxForwarding = _IpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 6)
)
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("mandatory")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1)
)
ipxDestEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "ipxDestSysInstance"),
    (0, "RADLAN-IPX-MIB", "ipxDestNetNum"),
    (0, "RADLAN-IPX-MIB", "ipxDestNextHopCircIndex"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("mandatory")
_IpxDestSysInstance_Type = Integer32
_IpxDestSysInstance_Object = MibTableColumn
ipxDestSysInstance = _IpxDestSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 1),
    _IpxDestSysInstance_Type()
)
ipxDestSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestSysInstance.setStatus("mandatory")
_IpxDestNetNum_Type = NetNumber
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 2),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("mandatory")
_IpxDestNextHopCircIndex_Type = Integer32
_IpxDestNextHopCircIndex_Object = MibTableColumn
ipxDestNextHopCircIndex = _IpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 3),
    _IpxDestNextHopCircIndex_Type()
)
ipxDestNextHopCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopCircIndex.setStatus("mandatory")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("rip", 3),
          ("nlsp", 4),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 4),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("mandatory")
_IpxDestTicks_Type = Integer32
_IpxDestTicks_Object = MibTableColumn
ipxDestTicks = _IpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 5),
    _IpxDestTicks_Type()
)
ipxDestTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestTicks.setStatus("mandatory")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 6),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("mandatory")
_IpxDestNextHopNICAddress_Type = PhysAddress
_IpxDestNextHopNICAddress_Object = MibTableColumn
ipxDestNextHopNICAddress = _IpxDestNextHopNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 7),
    _IpxDestNextHopNICAddress_Type()
)
ipxDestNextHopNICAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNICAddress.setStatus("mandatory")
_IpxDestNextHopNetNum_Type = NetNumber
_IpxDestNextHopNetNum_Object = MibTableColumn
ipxDestNextHopNetNum = _IpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 8),
    _IpxDestNextHopNetNum_Type()
)
ipxDestNextHopNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNetNum.setStatus("mandatory")


class _IpxDestExistState_Type(Integer32):
    """Custom type ipxDestExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxDestExistState_Type.__name__ = "Integer32"
_IpxDestExistState_Object = MibTableColumn
ipxDestExistState = _IpxDestExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 6, 1, 1, 9),
    _IpxDestExistState_Type()
)
ipxDestExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestExistState.setStatus("mandatory")
_IpxServices_ObjectIdentity = ObjectIdentity
ipxServices = _IpxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 7)
)
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("mandatory")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1)
)
ipxServEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "ipxServSysInstance"),
    (0, "RADLAN-IPX-MIB", "ipxServType"),
    (1, "RADLAN-IPX-MIB", "ipxServName"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("mandatory")
_IpxServSysInstance_Type = Integer32
_IpxServSysInstance_Object = MibTableColumn
ipxServSysInstance = _IpxServSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 1),
    _IpxServSysInstance_Type()
)
ipxServSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServSysInstance.setStatus("mandatory")


class _IpxServType_Type(OctetString):
    """Custom type ipxServType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxServType_Type.__name__ = "OctetString"
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 2),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServType.setStatus("mandatory")


class _IpxServName_Type(OctetString):
    """Custom type ipxServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "OctetString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 3),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServName.setStatus("mandatory")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("nlsp", 4),
          ("static", 5),
          ("sap", 6))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 4),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("mandatory")
_IpxServNetNum_Type = NetNumber
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 5),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("mandatory")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 6),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("mandatory")


class _IpxServSocket_Type(OctetString):
    """Custom type ipxServSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_IpxServSocket_Type.__name__ = "OctetString"
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 7),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("mandatory")
_IpxServHopCount_Type = Integer32
_IpxServHopCount_Object = MibTableColumn
ipxServHopCount = _IpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 8),
    _IpxServHopCount_Type()
)
ipxServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServHopCount.setStatus("mandatory")


class _IpxServExistState_Type(Integer32):
    """Custom type ipxServExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxServExistState_Type.__name__ = "Integer32"
_IpxServExistState_Object = MibTableColumn
ipxServExistState = _IpxServExistState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 7, 1, 1, 9),
    _IpxServExistState_Type()
)
ipxServExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServExistState.setStatus("mandatory")
_Ripsap_ObjectIdentity = ObjectIdentity
ripsap = _Ripsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 8)
)
_RipsapSystem_ObjectIdentity = ObjectIdentity
ripsapSystem = _RipsapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1)
)
_RipSysTable_Object = MibTable
ripSysTable = _RipSysTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ripSysTable.setStatus("mandatory")
_RipSysEntry_Object = MibTableRow
ripSysEntry = _RipSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1)
)
ripSysEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "ripSysInstance"),
)
if mibBuilder.loadTexts:
    ripSysEntry.setStatus("mandatory")
_RipSysInstance_Type = Integer32
_RipSysInstance_Object = MibTableColumn
ripSysInstance = _RipSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1, 1),
    _RipSysInstance_Type()
)
ripSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSysInstance.setStatus("mandatory")


class _RipSysState_Type(Integer32):
    """Custom type ripSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RipSysState_Type.__name__ = "Integer32"
_RipSysState_Object = MibTableColumn
ripSysState = _RipSysState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1, 2),
    _RipSysState_Type()
)
ripSysState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSysState.setStatus("mandatory")
_RipSysIncorrectPackets_Type = Counter32
_RipSysIncorrectPackets_Object = MibTableColumn
ripSysIncorrectPackets = _RipSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 1, 1, 3),
    _RipSysIncorrectPackets_Type()
)
ripSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripSysIncorrectPackets.setStatus("mandatory")
_SapSysTable_Object = MibTable
sapSysTable = _SapSysTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2)
)
if mibBuilder.loadTexts:
    sapSysTable.setStatus("mandatory")
_SapSysEntry_Object = MibTableRow
sapSysEntry = _SapSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1)
)
sapSysEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "sapSysInstance"),
)
if mibBuilder.loadTexts:
    sapSysEntry.setStatus("mandatory")
_SapSysInstance_Type = Integer32
_SapSysInstance_Object = MibTableColumn
sapSysInstance = _SapSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1, 1),
    _SapSysInstance_Type()
)
sapSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapSysInstance.setStatus("mandatory")


class _SapSysState_Type(Integer32):
    """Custom type sapSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SapSysState_Type.__name__ = "Integer32"
_SapSysState_Object = MibTableColumn
sapSysState = _SapSysState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1, 2),
    _SapSysState_Type()
)
sapSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapSysState.setStatus("mandatory")
_SapSysIncorrectPackets_Type = Counter32
_SapSysIncorrectPackets_Object = MibTableColumn
sapSysIncorrectPackets = _SapSysIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 1, 2, 1, 3),
    _SapSysIncorrectPackets_Type()
)
sapSysIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapSysIncorrectPackets.setStatus("mandatory")
_RipsapCircuit_ObjectIdentity = ObjectIdentity
ripsapCircuit = _RipsapCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2)
)
_RipCircTable_Object = MibTable
ripCircTable = _RipCircTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1)
)
if mibBuilder.loadTexts:
    ripCircTable.setStatus("mandatory")
_RipCircEntry_Object = MibTableRow
ripCircEntry = _RipCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1)
)
ripCircEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "ripCircSysInstance"),
    (0, "RADLAN-IPX-MIB", "ripCircIndex"),
)
if mibBuilder.loadTexts:
    ripCircEntry.setStatus("mandatory")
_RipCircSysInstance_Type = Integer32
_RipCircSysInstance_Object = MibTableColumn
ripCircSysInstance = _RipCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 1),
    _RipCircSysInstance_Type()
)
ripCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircSysInstance.setStatus("mandatory")
_RipCircIndex_Type = Integer32
_RipCircIndex_Object = MibTableColumn
ripCircIndex = _RipCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 2),
    _RipCircIndex_Type()
)
ripCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircIndex.setStatus("mandatory")


class _RipCircState_Type(Integer32):
    """Custom type ripCircState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_RipCircState_Type.__name__ = "Integer32"
_RipCircState_Object = MibTableColumn
ripCircState = _RipCircState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 3),
    _RipCircState_Type()
)
ripCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircState.setStatus("mandatory")


class _RipCircUpdate_Type(Integer32):
    """Custom type ripCircUpdate based on Integer32"""
    defaultValue = 60


_RipCircUpdate_Type.__name__ = "Integer32"
_RipCircUpdate_Object = MibTableColumn
ripCircUpdate = _RipCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 4),
    _RipCircUpdate_Type()
)
ripCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircUpdate.setStatus("mandatory")


class _RipCircAgeMultiplier_Type(Integer32):
    """Custom type ripCircAgeMultiplier based on Integer32"""
    defaultValue = 4


_RipCircAgeMultiplier_Type.__name__ = "Integer32"
_RipCircAgeMultiplier_Object = MibTableColumn
ripCircAgeMultiplier = _RipCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 5),
    _RipCircAgeMultiplier_Type()
)
ripCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripCircAgeMultiplier.setStatus("mandatory")
_RipCircOutPackets_Type = Counter32
_RipCircOutPackets_Object = MibTableColumn
ripCircOutPackets = _RipCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 6),
    _RipCircOutPackets_Type()
)
ripCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCircOutPackets.setStatus("mandatory")
_RipCircInPackets_Type = Counter32
_RipCircInPackets_Object = MibTableColumn
ripCircInPackets = _RipCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 1, 1, 7),
    _RipCircInPackets_Type()
)
ripCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripCircInPackets.setStatus("mandatory")
_SapCircTable_Object = MibTable
sapCircTable = _SapCircTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2)
)
if mibBuilder.loadTexts:
    sapCircTable.setStatus("mandatory")
_SapCircEntry_Object = MibTableRow
sapCircEntry = _SapCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1)
)
sapCircEntry.setIndexNames(
    (0, "RADLAN-IPX-MIB", "sapCircSysInstance"),
    (0, "RADLAN-IPX-MIB", "sapCircIndex"),
)
if mibBuilder.loadTexts:
    sapCircEntry.setStatus("mandatory")
_SapCircSysInstance_Type = Integer32
_SapCircSysInstance_Object = MibTableColumn
sapCircSysInstance = _SapCircSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 1),
    _SapCircSysInstance_Type()
)
sapCircSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircSysInstance.setStatus("mandatory")
_SapCircIndex_Type = Integer32
_SapCircIndex_Object = MibTableColumn
sapCircIndex = _SapCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 2),
    _SapCircIndex_Type()
)
sapCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircIndex.setStatus("mandatory")


class _SapCircState_Type(Integer32):
    """Custom type sapCircState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SapCircState_Type.__name__ = "Integer32"
_SapCircState_Object = MibTableColumn
sapCircState = _SapCircState_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 3),
    _SapCircState_Type()
)
sapCircState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircState.setStatus("mandatory")


class _SapCircUpdate_Type(Integer32):
    """Custom type sapCircUpdate based on Integer32"""
    defaultValue = 60


_SapCircUpdate_Type.__name__ = "Integer32"
_SapCircUpdate_Object = MibTableColumn
sapCircUpdate = _SapCircUpdate_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 4),
    _SapCircUpdate_Type()
)
sapCircUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircUpdate.setStatus("mandatory")


class _SapCircAgeMultiplier_Type(Integer32):
    """Custom type sapCircAgeMultiplier based on Integer32"""
    defaultValue = 4


_SapCircAgeMultiplier_Type.__name__ = "Integer32"
_SapCircAgeMultiplier_Object = MibTableColumn
sapCircAgeMultiplier = _SapCircAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 5),
    _SapCircAgeMultiplier_Type()
)
sapCircAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircAgeMultiplier.setStatus("mandatory")


class _SapCircGetNearestServerReply_Type(Integer32):
    """Custom type sapCircGetNearestServerReply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SapCircGetNearestServerReply_Type.__name__ = "Integer32"
_SapCircGetNearestServerReply_Object = MibTableColumn
sapCircGetNearestServerReply = _SapCircGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 6),
    _SapCircGetNearestServerReply_Type()
)
sapCircGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCircGetNearestServerReply.setStatus("mandatory")
_SapCircOutPackets_Type = Counter32
_SapCircOutPackets_Object = MibTableColumn
sapCircOutPackets = _SapCircOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 7),
    _SapCircOutPackets_Type()
)
sapCircOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCircOutPackets.setStatus("mandatory")
_SapCircInPackets_Type = Counter32
_SapCircInPackets_Object = MibTableColumn
sapCircInPackets = _SapCircInPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 12, 8, 2, 2, 1, 8),
    _SapCircInPackets_Type()
)
sapCircInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCircInPackets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-IPX-MIB",
    **{"NetNumber": NetNumber,
       "rndIPXdriver": rndIPXdriver,
       "rndIPXRip": rndIPXRip,
       "rndIPXRipFilterGlbTable": rndIPXRipFilterGlbTable,
       "rndIPXRipFilterGlbEntry": rndIPXRipFilterGlbEntry,
       "rndIPXRipFilterGlbFLtype": rndIPXRipFilterGlbFLtype,
       "rndIPXRipFilterGlbFLnumber": rndIPXRipFilterGlbFLnumber,
       "rndIPXRipFilterGlbFLStatus": rndIPXRipFilterGlbFLStatus,
       "rndIPXRipFilterGlbFLnetworkPatern": rndIPXRipFilterGlbFLnetworkPatern,
       "rndIPXRipFilterGlbFLnetworkMask": rndIPXRipFilterGlbFLnetworkMask,
       "rndIPXRipFilterGlbFLaction": rndIPXRipFilterGlbFLaction,
       "rndIPXRipFilterCircuitTable": rndIPXRipFilterCircuitTable,
       "rndIPXRipFilterCircuitEntry": rndIPXRipFilterCircuitEntry,
       "rndIPXRipFilterCircFLIfIndex": rndIPXRipFilterCircFLIfIndex,
       "rndIPXRipFilterCircFLType": rndIPXRipFilterCircFLType,
       "rndIPXRipFilterCircFLnumber": rndIPXRipFilterCircFLnumber,
       "rndIPXRipFilterCircFLStatus": rndIPXRipFilterCircFLStatus,
       "rndIPXRipFilterCircFLnetworkPatern": rndIPXRipFilterCircFLnetworkPatern,
       "rndIPXRipFilterCircFLnetworkMask": rndIPXRipFilterCircFLnetworkMask,
       "rndIPXRipFilterCircFLaction": rndIPXRipFilterCircFLaction,
       "rndIPXSap": rndIPXSap,
       "rndIPXSapFilterGlbTable": rndIPXSapFilterGlbTable,
       "rndIPXSapFilterGlbEntry": rndIPXSapFilterGlbEntry,
       "rndIPXSapFilterGlbFLtype": rndIPXSapFilterGlbFLtype,
       "rndIPXSapFilterGlbFLnumber": rndIPXSapFilterGlbFLnumber,
       "rndIPXSapFilterGlbFLStatus": rndIPXSapFilterGlbFLStatus,
       "rndIPXSapFilterGlbFLnetworkPatern": rndIPXSapFilterGlbFLnetworkPatern,
       "rndIPXSapFilterGlbFLnetworkMask": rndIPXSapFilterGlbFLnetworkMask,
       "rndIPXSapFilterGlbFLserviceType": rndIPXSapFilterGlbFLserviceType,
       "rndIPXSapFilterGlbFLserviceName": rndIPXSapFilterGlbFLserviceName,
       "rndIPXSapFilterGlbFLaction": rndIPXSapFilterGlbFLaction,
       "rndIPXSapFilterCircuitTable": rndIPXSapFilterCircuitTable,
       "rndIPXSapFilterCircuitEntry": rndIPXSapFilterCircuitEntry,
       "rndIPXSapFilterCircFLIfIndex": rndIPXSapFilterCircFLIfIndex,
       "rndIPXSapFilterCircFLtype": rndIPXSapFilterCircFLtype,
       "rndIPXSapFilterCircFLnumber": rndIPXSapFilterCircFLnumber,
       "rndIPXSapFilterCircFLStatus": rndIPXSapFilterCircFLStatus,
       "rndIPXSapFilterCircFLnetworkPatern": rndIPXSapFilterCircFLnetworkPatern,
       "rndIPXSapFilterCircFLnetworkMask": rndIPXSapFilterCircFLnetworkMask,
       "rndIPXSapFilterCircFLserviceType": rndIPXSapFilterCircFLserviceType,
       "rndIPXSapFilterCircFLserviceName": rndIPXSapFilterCircFLserviceName,
       "rndIPXSapFilterCircFLaction": rndIPXSapFilterCircFLaction,
       "ipxSystem": ipxSystem,
       "ipxBasicSysTable": ipxBasicSysTable,
       "ipxBasicSysEntry": ipxBasicSysEntry,
       "ipxBasicSysInstance": ipxBasicSysInstance,
       "ipxBasicSysExistState": ipxBasicSysExistState,
       "ipxBasicSysInReceives": ipxBasicSysInReceives,
       "ipxBasicSysInHdrErrors": ipxBasicSysInHdrErrors,
       "ipxBasicSysInUnknownSockets": ipxBasicSysInUnknownSockets,
       "ipxBasicSysInDiscards": ipxBasicSysInDiscards,
       "ipxBasicSysInDelivers": ipxBasicSysInDelivers,
       "ipxBasicSysNoRoutes": ipxBasicSysNoRoutes,
       "ipxBasicSysOutRequests": ipxBasicSysOutRequests,
       "ipxBasicSysOutMalformedRequests": ipxBasicSysOutMalformedRequests,
       "ipxBasicSysOutDiscards": ipxBasicSysOutDiscards,
       "ipxBasicSysOutPackets": ipxBasicSysOutPackets,
       "ipxCircuit": ipxCircuit,
       "ipxCircTable": ipxCircTable,
       "ipxCircEntry": ipxCircEntry,
       "ipxCircSysInstance": ipxCircSysInstance,
       "ipxCircIndex": ipxCircIndex,
       "ipxCircExistState": ipxCircExistState,
       "ipxCircOperState": ipxCircOperState,
       "ipxCircIfIndex": ipxCircIfIndex,
       "ipxCircNetNumber": ipxCircNetNumber,
       "ipxCircTimeToNet": ipxCircTimeToNet,
       "ipxCircEncaps": ipxCircEncaps,
       "ipxCircNetbiosDeliver": ipxCircNetbiosDeliver,
       "ipxForwarding": ipxForwarding,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestSysInstance": ipxDestSysInstance,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestNextHopCircIndex": ipxDestNextHopCircIndex,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestTicks": ipxDestTicks,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopNICAddress": ipxDestNextHopNICAddress,
       "ipxDestNextHopNetNum": ipxDestNextHopNetNum,
       "ipxDestExistState": ipxDestExistState,
       "ipxServices": ipxServices,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServSysInstance": ipxServSysInstance,
       "ipxServType": ipxServType,
       "ipxServName": ipxServName,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "ipxServHopCount": ipxServHopCount,
       "ipxServExistState": ipxServExistState,
       "ripsap": ripsap,
       "ripsapSystem": ripsapSystem,
       "ripSysTable": ripSysTable,
       "ripSysEntry": ripSysEntry,
       "ripSysInstance": ripSysInstance,
       "ripSysState": ripSysState,
       "ripSysIncorrectPackets": ripSysIncorrectPackets,
       "sapSysTable": sapSysTable,
       "sapSysEntry": sapSysEntry,
       "sapSysInstance": sapSysInstance,
       "sapSysState": sapSysState,
       "sapSysIncorrectPackets": sapSysIncorrectPackets,
       "ripsapCircuit": ripsapCircuit,
       "ripCircTable": ripCircTable,
       "ripCircEntry": ripCircEntry,
       "ripCircSysInstance": ripCircSysInstance,
       "ripCircIndex": ripCircIndex,
       "ripCircState": ripCircState,
       "ripCircUpdate": ripCircUpdate,
       "ripCircAgeMultiplier": ripCircAgeMultiplier,
       "ripCircOutPackets": ripCircOutPackets,
       "ripCircInPackets": ripCircInPackets,
       "sapCircTable": sapCircTable,
       "sapCircEntry": sapCircEntry,
       "sapCircSysInstance": sapCircSysInstance,
       "sapCircIndex": sapCircIndex,
       "sapCircState": sapCircState,
       "sapCircUpdate": sapCircUpdate,
       "sapCircAgeMultiplier": sapCircAgeMultiplier,
       "sapCircGetNearestServerReply": sapCircGetNearestServerReply,
       "sapCircOutPackets": sapCircOutPackets,
       "sapCircInPackets": sapCircInPackets}
)
