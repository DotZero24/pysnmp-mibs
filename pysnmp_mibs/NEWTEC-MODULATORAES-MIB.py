# SNMP MIB module (NEWTEC-MODULATORAES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MODULATORAES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:05 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcDvbModulatorAes = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010)
)
if mibBuilder.loadTexts:
    ntcDvbModulatorAes.setRevisions(
        ("2018-02-02 09:00",
         "2016-10-24 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcDvbModAesObjects_ObjectIdentity = ObjectIdentity
ntcDvbModAesObjects = _NtcDvbModAesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModAesObjects.setStatus("current")
_NtcDvbModAesCfgAes_ObjectIdentity = ObjectIdentity
ntcDvbModAesCfgAes = _NtcDvbModAesCfgAes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAes.setStatus("current")


class _NtcDvbModAesCfgAesEnable_Type(Integer32):
    """Custom type ntcDvbModAesCfgAesEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModAesCfgAesEnable_Type.__name__ = "Integer32"
_NtcDvbModAesCfgAesEnable_Object = MibScalar
ntcDvbModAesCfgAesEnable = _NtcDvbModAesCfgAesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 1, 1),
    _NtcDvbModAesCfgAesEnable_Type()
)
ntcDvbModAesCfgAesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesEnable.setStatus("current")


class _NtcDvbModAesCfgAesGlobEncr_Type(NtcEnable):
    """Custom type ntcDvbModAesCfgAesGlobEncr based on NtcEnable"""
    defaultValue = 1


_NtcDvbModAesCfgAesGlobEncr_Type.__name__ = "NtcEnable"
_NtcDvbModAesCfgAesGlobEncr_Object = MibScalar
ntcDvbModAesCfgAesGlobEncr = _NtcDvbModAesCfgAesGlobEncr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 1, 2),
    _NtcDvbModAesCfgAesGlobEncr_Type()
)
ntcDvbModAesCfgAesGlobEncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGlobEncr.setStatus("current")


class _NtcDvbModAesCfgAesKeyStrength_Type(Integer32):
    """Custom type ntcDvbModAesCfgAesKeyStrength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes64", 0),
          ("aes128", 1),
          ("aes256", 2))
    )


_NtcDvbModAesCfgAesKeyStrength_Type.__name__ = "Integer32"
_NtcDvbModAesCfgAesKeyStrength_Object = MibScalar
ntcDvbModAesCfgAesKeyStrength = _NtcDvbModAesCfgAesKeyStrength_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 1, 3),
    _NtcDvbModAesCfgAesKeyStrength_Type()
)
ntcDvbModAesCfgAesKeyStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesKeyStrength.setStatus("current")


class _NtcDvbModAesCfgAesGroupKey_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesGroupKey based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesGroupKey_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesGroupKey_Object = MibScalar
ntcDvbModAesCfgAesGroupKey = _NtcDvbModAesCfgAesGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 1, 4),
    _NtcDvbModAesCfgAesGroupKey_Type()
)
ntcDvbModAesCfgAesGroupKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGroupKey.setStatus("current")


class _NtcDvbModAesCfgAesClearKeys_Type(Integer32):
    """Custom type ntcDvbModAesCfgAesClearKeys based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 0),
          ("clearkeys", 1))
    )


_NtcDvbModAesCfgAesClearKeys_Type.__name__ = "Integer32"
_NtcDvbModAesCfgAesClearKeys_Object = MibScalar
ntcDvbModAesCfgAesClearKeys = _NtcDvbModAesCfgAesClearKeys_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 1, 5),
    _NtcDvbModAesCfgAesClearKeys_Type()
)
ntcDvbModAesCfgAesClearKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesClearKeys.setStatus("current")
_NtcDvbModAesCfgAesGlo_ObjectIdentity = ObjectIdentity
ntcDvbModAesCfgAesGlo = _NtcDvbModAesCfgAesGlo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 2)
)
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGlo.setStatus("current")


class _NtcDvbModAesCfgAesGloKeyPar_Type(Integer32):
    """Custom type ntcDvbModAesCfgAesGloKeyPar based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("even", 0),
          ("odd", 1))
    )


_NtcDvbModAesCfgAesGloKeyPar_Type.__name__ = "Integer32"
_NtcDvbModAesCfgAesGloKeyPar_Object = MibScalar
ntcDvbModAesCfgAesGloKeyPar = _NtcDvbModAesCfgAesGloKeyPar_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 2, 1),
    _NtcDvbModAesCfgAesGloKeyPar_Type()
)
ntcDvbModAesCfgAesGloKeyPar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGloKeyPar.setStatus("current")


class _NtcDvbModAesCfgAesGloEncEven_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesGloEncEven based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesGloEncEven_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesGloEncEven_Object = MibScalar
ntcDvbModAesCfgAesGloEncEven = _NtcDvbModAesCfgAesGloEncEven_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 2, 2),
    _NtcDvbModAesCfgAesGloEncEven_Type()
)
ntcDvbModAesCfgAesGloEncEven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGloEncEven.setStatus("current")


class _NtcDvbModAesCfgAesGloEncOdd_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesGloEncOdd based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesGloEncOdd_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesGloEncOdd_Object = MibScalar
ntcDvbModAesCfgAesGloEncOdd = _NtcDvbModAesCfgAesGloEncOdd_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 2, 3),
    _NtcDvbModAesCfgAesGloEncOdd_Type()
)
ntcDvbModAesCfgAesGloEncOdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGloEncOdd.setStatus("current")


class _NtcDvbModAesCfgAesGloEven_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesGloEven based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesGloEven_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesGloEven_Object = MibScalar
ntcDvbModAesCfgAesGloEven = _NtcDvbModAesCfgAesGloEven_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 2, 4),
    _NtcDvbModAesCfgAesGloEven_Type()
)
ntcDvbModAesCfgAesGloEven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGloEven.setStatus("current")


class _NtcDvbModAesCfgAesGloOdd_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesGloOdd based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesGloOdd_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesGloOdd_Object = MibScalar
ntcDvbModAesCfgAesGloOdd = _NtcDvbModAesCfgAesGloOdd_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 2, 5),
    _NtcDvbModAesCfgAesGloOdd_Type()
)
ntcDvbModAesCfgAesGloOdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesGloOdd.setStatus("current")
_NtcDvbModAesCfgAesStrTable_Object = MibTable
ntcDvbModAesCfgAesStrTable = _NtcDvbModAesCfgAesStrTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3)
)
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrTable.setStatus("current")
_NtcDvbModAesCfgAesStrEntry_Object = MibTableRow
ntcDvbModAesCfgAesStrEntry = _NtcDvbModAesCfgAesStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1)
)
ntcDvbModAesCfgAesStrEntry.setIndexNames(
    (0, "NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrName"),
)
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrEntry.setStatus("current")


class _NtcDvbModAesCfgAesStrName_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesStrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcDvbModAesCfgAesStrName_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesStrName_Object = MibTableColumn
ntcDvbModAesCfgAesStrName = _NtcDvbModAesCfgAesStrName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 1),
    _NtcDvbModAesCfgAesStrName_Type()
)
ntcDvbModAesCfgAesStrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrName.setStatus("current")
_NtcDvbModAesCfgAesStrRowStatus_Type = RowStatus
_NtcDvbModAesCfgAesStrRowStatus_Object = MibTableColumn
ntcDvbModAesCfgAesStrRowStatus = _NtcDvbModAesCfgAesStrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 2),
    _NtcDvbModAesCfgAesStrRowStatus_Type()
)
ntcDvbModAesCfgAesStrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrRowStatus.setStatus("current")


class _NtcDvbModAesCfgAesStrEnable_Type(Integer32):
    """Custom type ntcDvbModAesCfgAesStrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcDvbModAesCfgAesStrEnable_Type.__name__ = "Integer32"
_NtcDvbModAesCfgAesStrEnable_Object = MibTableColumn
ntcDvbModAesCfgAesStrEnable = _NtcDvbModAesCfgAesStrEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 3),
    _NtcDvbModAesCfgAesStrEnable_Type()
)
ntcDvbModAesCfgAesStrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrEnable.setStatus("current")
_NtcDvbModAesCfgAesStrIsi_Type = Unsigned32
_NtcDvbModAesCfgAesStrIsi_Object = MibTableColumn
ntcDvbModAesCfgAesStrIsi = _NtcDvbModAesCfgAesStrIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 4),
    _NtcDvbModAesCfgAesStrIsi_Type()
)
ntcDvbModAesCfgAesStrIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrIsi.setStatus("current")


class _NtcDvbModAesCfgAesStrKeyPar_Type(Integer32):
    """Custom type ntcDvbModAesCfgAesStrKeyPar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("even", 0),
          ("odd", 1))
    )


_NtcDvbModAesCfgAesStrKeyPar_Type.__name__ = "Integer32"
_NtcDvbModAesCfgAesStrKeyPar_Object = MibTableColumn
ntcDvbModAesCfgAesStrKeyPar = _NtcDvbModAesCfgAesStrKeyPar_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 5),
    _NtcDvbModAesCfgAesStrKeyPar_Type()
)
ntcDvbModAesCfgAesStrKeyPar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrKeyPar.setStatus("current")


class _NtcDvbModAesCfgAesStrEncEven_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesStrEncEven based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesStrEncEven_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesStrEncEven_Object = MibTableColumn
ntcDvbModAesCfgAesStrEncEven = _NtcDvbModAesCfgAesStrEncEven_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 6),
    _NtcDvbModAesCfgAesStrEncEven_Type()
)
ntcDvbModAesCfgAesStrEncEven.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrEncEven.setStatus("current")


class _NtcDvbModAesCfgAesStrEncOdd_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesStrEncOdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesStrEncOdd_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesStrEncOdd_Object = MibTableColumn
ntcDvbModAesCfgAesStrEncOdd = _NtcDvbModAesCfgAesStrEncOdd_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 7),
    _NtcDvbModAesCfgAesStrEncOdd_Type()
)
ntcDvbModAesCfgAesStrEncOdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrEncOdd.setStatus("current")


class _NtcDvbModAesCfgAesStrEven_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesStrEven based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesStrEven_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesStrEven_Object = MibTableColumn
ntcDvbModAesCfgAesStrEven = _NtcDvbModAesCfgAesStrEven_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 8),
    _NtcDvbModAesCfgAesStrEven_Type()
)
ntcDvbModAesCfgAesStrEven.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrEven.setStatus("current")


class _NtcDvbModAesCfgAesStrOdd_Type(DisplayString):
    """Custom type ntcDvbModAesCfgAesStrOdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcDvbModAesCfgAesStrOdd_Type.__name__ = "DisplayString"
_NtcDvbModAesCfgAesStrOdd_Object = MibTableColumn
ntcDvbModAesCfgAesStrOdd = _NtcDvbModAesCfgAesStrOdd_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 1, 3, 1, 9),
    _NtcDvbModAesCfgAesStrOdd_Type()
)
ntcDvbModAesCfgAesStrOdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcDvbModAesCfgAesStrOdd.setStatus("current")
_NtcDvbModAesConformance_ObjectIdentity = ObjectIdentity
ntcDvbModAesConformance = _NtcDvbModAesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 2)
)
if mibBuilder.loadTexts:
    ntcDvbModAesConformance.setStatus("current")
_NtcDvbModAesConfCompliance_ObjectIdentity = ObjectIdentity
ntcDvbModAesConfCompliance = _NtcDvbModAesConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 2, 1)
)
if mibBuilder.loadTexts:
    ntcDvbModAesConfCompliance.setStatus("current")
_NtcDvbModAesConfGroup_ObjectIdentity = ObjectIdentity
ntcDvbModAesConfGroup = _NtcDvbModAesConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 2, 2)
)
if mibBuilder.loadTexts:
    ntcDvbModAesConfGroup.setStatus("current")

# Managed Objects groups

ntcDvbModAesConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 2, 2, 1)
)
ntcDvbModAesConfGrpV1Standard.setObjects(
      *(("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesEnable"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGlobEncr"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesKeyStrength"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGroupKey"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesClearKeys"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGloKeyPar"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGloEncEven"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGloEncOdd"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGloEven"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesGloOdd"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrRowStatus"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrEnable"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrIsi"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrKeyPar"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrEncEven"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrEncOdd"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrEven"),
        ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesCfgAesStrOdd"))
)
if mibBuilder.loadTexts:
    ntcDvbModAesConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcDvbModAesConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1010, 2, 1, 1)
)
ntcDvbModAesConfCompV1Standard.setObjects(
    ("NEWTEC-MODULATORAES-MIB", "ntcDvbModAesConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcDvbModAesConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MODULATORAES-MIB",
    **{"ntcDvbModulatorAes": ntcDvbModulatorAes,
       "ntcDvbModAesObjects": ntcDvbModAesObjects,
       "ntcDvbModAesCfgAes": ntcDvbModAesCfgAes,
       "ntcDvbModAesCfgAesEnable": ntcDvbModAesCfgAesEnable,
       "ntcDvbModAesCfgAesGlobEncr": ntcDvbModAesCfgAesGlobEncr,
       "ntcDvbModAesCfgAesKeyStrength": ntcDvbModAesCfgAesKeyStrength,
       "ntcDvbModAesCfgAesGroupKey": ntcDvbModAesCfgAesGroupKey,
       "ntcDvbModAesCfgAesClearKeys": ntcDvbModAesCfgAesClearKeys,
       "ntcDvbModAesCfgAesGlo": ntcDvbModAesCfgAesGlo,
       "ntcDvbModAesCfgAesGloKeyPar": ntcDvbModAesCfgAesGloKeyPar,
       "ntcDvbModAesCfgAesGloEncEven": ntcDvbModAesCfgAesGloEncEven,
       "ntcDvbModAesCfgAesGloEncOdd": ntcDvbModAesCfgAesGloEncOdd,
       "ntcDvbModAesCfgAesGloEven": ntcDvbModAesCfgAesGloEven,
       "ntcDvbModAesCfgAesGloOdd": ntcDvbModAesCfgAesGloOdd,
       "ntcDvbModAesCfgAesStrTable": ntcDvbModAesCfgAesStrTable,
       "ntcDvbModAesCfgAesStrEntry": ntcDvbModAesCfgAesStrEntry,
       "ntcDvbModAesCfgAesStrName": ntcDvbModAesCfgAesStrName,
       "ntcDvbModAesCfgAesStrRowStatus": ntcDvbModAesCfgAesStrRowStatus,
       "ntcDvbModAesCfgAesStrEnable": ntcDvbModAesCfgAesStrEnable,
       "ntcDvbModAesCfgAesStrIsi": ntcDvbModAesCfgAesStrIsi,
       "ntcDvbModAesCfgAesStrKeyPar": ntcDvbModAesCfgAesStrKeyPar,
       "ntcDvbModAesCfgAesStrEncEven": ntcDvbModAesCfgAesStrEncEven,
       "ntcDvbModAesCfgAesStrEncOdd": ntcDvbModAesCfgAesStrEncOdd,
       "ntcDvbModAesCfgAesStrEven": ntcDvbModAesCfgAesStrEven,
       "ntcDvbModAesCfgAesStrOdd": ntcDvbModAesCfgAesStrOdd,
       "ntcDvbModAesConformance": ntcDvbModAesConformance,
       "ntcDvbModAesConfCompliance": ntcDvbModAesConfCompliance,
       "ntcDvbModAesConfCompV1Standard": ntcDvbModAesConfCompV1Standard,
       "ntcDvbModAesConfGroup": ntcDvbModAesConfGroup,
       "ntcDvbModAesConfGrpV1Standard": ntcDvbModAesConfGrpV1Standard}
)
