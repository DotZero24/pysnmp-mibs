# SNMP MIB module (MAIPU-VRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-VRF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:13 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mVrfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89)
)
if mibBuilder.loadTexts:
    mVrfMib.setRevisions(
        ("1904-05-27 10:03",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MVrfMibObjects_ObjectIdentity = ObjectIdentity
mVrfMibObjects = _MVrfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1)
)
_MVrfGlobal_ObjectIdentity = ObjectIdentity
mVrfGlobal = _MVrfGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 1)
)
_MVrfConfiguration1_ObjectIdentity = ObjectIdentity
mVrfConfiguration1 = _MVrfConfiguration1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2)
)
_MVrfConfiguration1Table_Object = MibTable
mVrfConfiguration1Table = _MVrfConfiguration1Table_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mVrfConfiguration1Table.setStatus("current")
_MVrfConfiguration1Entry_Object = MibTableRow
mVrfConfiguration1Entry = _MVrfConfiguration1Entry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2, 1, 1)
)
mVrfConfiguration1Entry.setIndexNames(
    (0, "MAIPU-VRF-MIB", "mVrfConfiguration1NameIndex"),
)
if mibBuilder.loadTexts:
    mVrfConfiguration1Entry.setStatus("current")


class _MVrfConfiguration1Name_Type(DisplayString):
    """Custom type mVrfConfiguration1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MVrfConfiguration1Name_Type.__name__ = "DisplayString"
_MVrfConfiguration1Name_Object = MibTableColumn
mVrfConfiguration1Name = _MVrfConfiguration1Name_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2, 1, 1, 1),
    _MVrfConfiguration1Name_Type()
)
mVrfConfiguration1Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mVrfConfiguration1Name.setStatus("current")


class _MVrfConfiguration1RouteDistinguisher_Type(DisplayString):
    """Custom type mVrfConfiguration1RouteDistinguisher based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_MVrfConfiguration1RouteDistinguisher_Type.__name__ = "DisplayString"
_MVrfConfiguration1RouteDistinguisher_Object = MibTableColumn
mVrfConfiguration1RouteDistinguisher = _MVrfConfiguration1RouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2, 1, 1, 2),
    _MVrfConfiguration1RouteDistinguisher_Type()
)
mVrfConfiguration1RouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mVrfConfiguration1RouteDistinguisher.setStatus("current")


class _MVrfConfiguration1Description_Type(DisplayString):
    """Custom type mVrfConfiguration1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MVrfConfiguration1Description_Type.__name__ = "DisplayString"
_MVrfConfiguration1Description_Object = MibTableColumn
mVrfConfiguration1Description = _MVrfConfiguration1Description_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2, 1, 1, 3),
    _MVrfConfiguration1Description_Type()
)
mVrfConfiguration1Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mVrfConfiguration1Description.setStatus("current")


class _MVrfConfiguration2Type_Type(Integer32):
    """Custom type mVrfConfiguration2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )


_MVrfConfiguration2Type_Type.__name__ = "Integer32"
_MVrfConfiguration2Type_Object = MibTableColumn
mVrfConfiguration2Type = _MVrfConfiguration2Type_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 2, 1, 1, 3),
    _MVrfConfiguration2Type_Type()
)
mVrfConfiguration2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mVrfConfiguration2Type.setStatus("current")
_MVrfConfiguration2_ObjectIdentity = ObjectIdentity
mVrfConfiguration2 = _MVrfConfiguration2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 3)
)
_MVrfConfiguration2Table_Object = MibTable
mVrfConfiguration2Table = _MVrfConfiguration2Table_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mVrfConfiguration2Table.setStatus("current")
_MVrfConfiguration2Entry_Object = MibTableRow
mVrfConfiguration2Entry = _MVrfConfiguration2Entry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 3, 1, 1)
)
mVrfConfiguration2Entry.setIndexNames(
    (0, "MAIPU-VRF-MIB", "mVrfConfiguration2Name"),
    (0, "MAIPU-VRF-MIB", "mVrfConfiguration2Type"),
    (0, "MAIPU-VRF-MIB", "mVrfConfiguration2RouteDistinguisher"),
)
if mibBuilder.loadTexts:
    mVrfConfiguration2Entry.setStatus("current")


class _MVrfConfiguration2Name_Type(DisplayString):
    """Custom type mVrfConfiguration2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MVrfConfiguration2Name_Type.__name__ = "DisplayString"
_MVrfConfiguration2Name_Object = MibTableColumn
mVrfConfiguration2Name = _MVrfConfiguration2Name_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 3, 1, 1, 1),
    _MVrfConfiguration2Name_Type()
)
mVrfConfiguration2Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mVrfConfiguration2Name.setStatus("current")


class _MVrfConfiguration2RouteDistinguisher_Type(DisplayString):
    """Custom type mVrfConfiguration2RouteDistinguisher based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_MVrfConfiguration2RouteDistinguisher_Type.__name__ = "DisplayString"
_MVrfConfiguration2RouteDistinguisher_Object = MibTableColumn
mVrfConfiguration2RouteDistinguisher = _MVrfConfiguration2RouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 89, 1, 3, 1, 1, 3),
    _MVrfConfiguration2RouteDistinguisher_Type()
)
mVrfConfiguration2RouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mVrfConfiguration2RouteDistinguisher.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-VRF-MIB",
    **{"mVrfMib": mVrfMib,
       "mVrfMibObjects": mVrfMibObjects,
       "mVrfGlobal": mVrfGlobal,
       "mVrfConfiguration1": mVrfConfiguration1,
       "mVrfConfiguration1Table": mVrfConfiguration1Table,
       "mVrfConfiguration1Entry": mVrfConfiguration1Entry,
       "mVrfConfiguration1Name": mVrfConfiguration1Name,
       "mVrfConfiguration1RouteDistinguisher": mVrfConfiguration1RouteDistinguisher,
       "mVrfConfiguration1Description": mVrfConfiguration1Description,
       "mVrfConfiguration2Type": mVrfConfiguration2Type,
       "mVrfConfiguration2": mVrfConfiguration2,
       "mVrfConfiguration2Table": mVrfConfiguration2Table,
       "mVrfConfiguration2Entry": mVrfConfiguration2Entry,
       "mVrfConfiguration2Name": mVrfConfiguration2Name,
       "mVrfConfiguration2RouteDistinguisher": mVrfConfiguration2RouteDistinguisher}
)
