# SNMP MIB module (MX-DIGIT-MAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DIGIT-MAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:28 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

digitMapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55)
)
if mibBuilder.loadTexts:
    digitMapMIB.setRevisions(
        ("2009-10-14 00:00",
         "2008-10-16 00:00",
         "2008-08-25 00:00",
         "2004-11-01 00:00",
         "2003-02-24 00:00",
         "2003-02-17 00:00",
         "2002-11-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DigitMapMIBObjects_ObjectIdentity = ObjectIdentity
digitMapMIBObjects = _DigitMapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1)
)


class _DigitMapProcessDigitsWhenPressed_Type(MxEnableState):
    """Custom type digitMapProcessDigitsWhenPressed based on MxEnableState"""
    defaultValue = 1


_DigitMapProcessDigitsWhenPressed_Type.__name__ = "MxEnableState"
_DigitMapProcessDigitsWhenPressed_Object = MibScalar
digitMapProcessDigitsWhenPressed = _DigitMapProcessDigitsWhenPressed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 1),
    _DigitMapProcessDigitsWhenPressed_Type()
)
digitMapProcessDigitsWhenPressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapProcessDigitsWhenPressed.setStatus("current")
_DigitMapAllowedTable_Object = MibTable
digitMapAllowedTable = _DigitMapAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10)
)
if mibBuilder.loadTexts:
    digitMapAllowedTable.setStatus("current")
_DigitMapAllowedEntry_Object = MibTableRow
digitMapAllowedEntry = _DigitMapAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1)
)
digitMapAllowedEntry.setIndexNames(
    (0, "MX-DIGIT-MAP-MIB", "digitMapAllowedIndex"),
)
if mibBuilder.loadTexts:
    digitMapAllowedEntry.setStatus("current")


class _DigitMapAllowedIndex_Type(Unsigned32):
    """Custom type digitMapAllowedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DigitMapAllowedIndex_Type.__name__ = "Unsigned32"
_DigitMapAllowedIndex_Object = MibTableColumn
digitMapAllowedIndex = _DigitMapAllowedIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 5),
    _DigitMapAllowedIndex_Type()
)
digitMapAllowedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitMapAllowedIndex.setStatus("current")


class _DigitMapAllowedEnable_Type(Integer32):
    """Custom type digitMapAllowedEnable based on Integer32"""
    defaultValue = 1

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


_DigitMapAllowedEnable_Type.__name__ = "Integer32"
_DigitMapAllowedEnable_Object = MibTableColumn
digitMapAllowedEnable = _DigitMapAllowedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 10),
    _DigitMapAllowedEnable_Type()
)
digitMapAllowedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapAllowedEnable.setStatus("current")


class _DigitMapAllowedDigitMap_Type(OctetString):
    """Custom type digitMapAllowedDigitMap based on OctetString"""
    defaultValue = OctetString("x.T")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DigitMapAllowedDigitMap_Type.__name__ = "OctetString"
_DigitMapAllowedDigitMap_Object = MibTableColumn
digitMapAllowedDigitMap = _DigitMapAllowedDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 15),
    _DigitMapAllowedDigitMap_Type()
)
digitMapAllowedDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapAllowedDigitMap.setStatus("current")


class _DigitMapAllowedIsValid_Type(Integer32):
    """Custom type digitMapAllowedIsValid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_DigitMapAllowedIsValid_Type.__name__ = "Integer32"
_DigitMapAllowedIsValid_Object = MibTableColumn
digitMapAllowedIsValid = _DigitMapAllowedIsValid_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 20),
    _DigitMapAllowedIsValid_Type()
)
digitMapAllowedIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitMapAllowedIsValid.setStatus("deprecated")


class _DigitMapPrefixedDigitRemovalCount_Type(Unsigned32):
    """Custom type digitMapPrefixedDigitRemovalCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DigitMapPrefixedDigitRemovalCount_Type.__name__ = "Unsigned32"
_DigitMapPrefixedDigitRemovalCount_Object = MibTableColumn
digitMapPrefixedDigitRemovalCount = _DigitMapPrefixedDigitRemovalCount_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 25),
    _DigitMapPrefixedDigitRemovalCount_Type()
)
digitMapPrefixedDigitRemovalCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapPrefixedDigitRemovalCount.setStatus("current")


class _DigitMapPrependedString_Type(OctetString):
    """Custom type digitMapPrependedString based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DigitMapPrependedString_Type.__name__ = "OctetString"
_DigitMapPrependedString_Object = MibTableColumn
digitMapPrependedString = _DigitMapPrependedString_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 30),
    _DigitMapPrependedString_Type()
)
digitMapPrependedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapPrependedString.setStatus("current")


class _DigitMapSuffixStringToRemove_Type(OctetString):
    """Custom type digitMapSuffixStringToRemove based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DigitMapSuffixStringToRemove_Type.__name__ = "OctetString"
_DigitMapSuffixStringToRemove_Object = MibTableColumn
digitMapSuffixStringToRemove = _DigitMapSuffixStringToRemove_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 35),
    _DigitMapSuffixStringToRemove_Type()
)
digitMapSuffixStringToRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapSuffixStringToRemove.setStatus("current")


class _DigitMapAllowedLineToApply_Type(OctetString):
    """Custom type digitMapAllowedLineToApply based on OctetString"""
    defaultValue = OctetString("all")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DigitMapAllowedLineToApply_Type.__name__ = "OctetString"
_DigitMapAllowedLineToApply_Object = MibTableColumn
digitMapAllowedLineToApply = _DigitMapAllowedLineToApply_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 10, 1, 50),
    _DigitMapAllowedLineToApply_Type()
)
digitMapAllowedLineToApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapAllowedLineToApply.setStatus("current")
_DigitMapRefusedTable_Object = MibTable
digitMapRefusedTable = _DigitMapRefusedTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20)
)
if mibBuilder.loadTexts:
    digitMapRefusedTable.setStatus("current")
_DigitMapRefusedEntry_Object = MibTableRow
digitMapRefusedEntry = _DigitMapRefusedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20, 1)
)
digitMapRefusedEntry.setIndexNames(
    (0, "MX-DIGIT-MAP-MIB", "digitMapRefusedIndex"),
)
if mibBuilder.loadTexts:
    digitMapRefusedEntry.setStatus("current")


class _DigitMapRefusedIndex_Type(Unsigned32):
    """Custom type digitMapRefusedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DigitMapRefusedIndex_Type.__name__ = "Unsigned32"
_DigitMapRefusedIndex_Object = MibTableColumn
digitMapRefusedIndex = _DigitMapRefusedIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20, 1, 5),
    _DigitMapRefusedIndex_Type()
)
digitMapRefusedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitMapRefusedIndex.setStatus("current")


class _DigitMapRefusedEnable_Type(Integer32):
    """Custom type digitMapRefusedEnable based on Integer32"""
    defaultValue = 0

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


_DigitMapRefusedEnable_Type.__name__ = "Integer32"
_DigitMapRefusedEnable_Object = MibTableColumn
digitMapRefusedEnable = _DigitMapRefusedEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20, 1, 10),
    _DigitMapRefusedEnable_Type()
)
digitMapRefusedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapRefusedEnable.setStatus("current")


class _DigitMapRefusedDigitMap_Type(OctetString):
    """Custom type digitMapRefusedDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DigitMapRefusedDigitMap_Type.__name__ = "OctetString"
_DigitMapRefusedDigitMap_Object = MibTableColumn
digitMapRefusedDigitMap = _DigitMapRefusedDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20, 1, 15),
    _DigitMapRefusedDigitMap_Type()
)
digitMapRefusedDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapRefusedDigitMap.setStatus("current")


class _DigitMapRefusedIsValid_Type(Integer32):
    """Custom type digitMapRefusedIsValid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_DigitMapRefusedIsValid_Type.__name__ = "Integer32"
_DigitMapRefusedIsValid_Object = MibTableColumn
digitMapRefusedIsValid = _DigitMapRefusedIsValid_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20, 1, 20),
    _DigitMapRefusedIsValid_Type()
)
digitMapRefusedIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitMapRefusedIsValid.setStatus("deprecated")


class _DigitMapRefusedLineToApply_Type(OctetString):
    """Custom type digitMapRefusedLineToApply based on OctetString"""
    defaultValue = OctetString("all")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DigitMapRefusedLineToApply_Type.__name__ = "OctetString"
_DigitMapRefusedLineToApply_Object = MibTableColumn
digitMapRefusedLineToApply = _DigitMapRefusedLineToApply_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 20, 1, 50),
    _DigitMapRefusedLineToApply_Type()
)
digitMapRefusedLineToApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapRefusedLineToApply.setStatus("current")
_DigitMapTimeouts_ObjectIdentity = ObjectIdentity
digitMapTimeouts = _DigitMapTimeouts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 30)
)


class _DigitMapTimeoutCompletion_Type(Unsigned32):
    """Custom type digitMapTimeoutCompletion based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_DigitMapTimeoutCompletion_Type.__name__ = "Unsigned32"
_DigitMapTimeoutCompletion_Object = MibScalar
digitMapTimeoutCompletion = _DigitMapTimeoutCompletion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 30, 5),
    _DigitMapTimeoutCompletion_Type()
)
digitMapTimeoutCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapTimeoutCompletion.setStatus("current")


class _DigitMapTimeoutFirstDigit_Type(Unsigned32):
    """Custom type digitMapTimeoutFirstDigit based on Unsigned32"""
    defaultValue = 20000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 180000),
    )


_DigitMapTimeoutFirstDigit_Type.__name__ = "Unsigned32"
_DigitMapTimeoutFirstDigit_Object = MibScalar
digitMapTimeoutFirstDigit = _DigitMapTimeoutFirstDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 30, 10),
    _DigitMapTimeoutFirstDigit_Type()
)
digitMapTimeoutFirstDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapTimeoutFirstDigit.setStatus("current")


class _DigitMapTimeoutInterDigit_Type(Unsigned32):
    """Custom type digitMapTimeoutInterDigit based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_DigitMapTimeoutInterDigit_Type.__name__ = "Unsigned32"
_DigitMapTimeoutInterDigit_Object = MibScalar
digitMapTimeoutInterDigit = _DigitMapTimeoutInterDigit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 1, 30, 15),
    _DigitMapTimeoutInterDigit_Type()
)
digitMapTimeoutInterDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitMapTimeoutInterDigit.setStatus("current")
_DigitMapConformance_ObjectIdentity = ObjectIdentity
digitMapConformance = _DigitMapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2)
)
_DigitMapCompliances_ObjectIdentity = ObjectIdentity
digitMapCompliances = _DigitMapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2, 1)
)
_DigitMapGroups_ObjectIdentity = ObjectIdentity
digitMapGroups = _DigitMapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2, 2)
)

# Managed Objects groups

digitMapAllowedVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2, 2, 1)
)
digitMapAllowedVer1.setObjects(
      *(("MX-DIGIT-MAP-MIB", "digitMapAllowedIndex"),
        ("MX-DIGIT-MAP-MIB", "digitMapAllowedEnable"),
        ("MX-DIGIT-MAP-MIB", "digitMapAllowedDigitMap"),
        ("MX-DIGIT-MAP-MIB", "digitMapAllowedIsValid"),
        ("MX-DIGIT-MAP-MIB", "digitMapPrefixedDigitRemovalCount"),
        ("MX-DIGIT-MAP-MIB", "digitMapPrependedString"),
        ("MX-DIGIT-MAP-MIB", "digitMapSuffixStringToRemove"),
        ("MX-DIGIT-MAP-MIB", "digitMapAllowedLineToApply"))
)
if mibBuilder.loadTexts:
    digitMapAllowedVer1.setStatus("current")

digitMapRefusedVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2, 2, 2)
)
digitMapRefusedVer1.setObjects(
      *(("MX-DIGIT-MAP-MIB", "digitMapRefusedIndex"),
        ("MX-DIGIT-MAP-MIB", "digitMapRefusedEnable"),
        ("MX-DIGIT-MAP-MIB", "digitMapRefusedDigitMap"),
        ("MX-DIGIT-MAP-MIB", "digitMapRefusedIsValid"),
        ("MX-DIGIT-MAP-MIB", "digitMapRefusedLineToApply"))
)
if mibBuilder.loadTexts:
    digitMapRefusedVer1.setStatus("current")

digitMapTimeoutVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2, 2, 3)
)
digitMapTimeoutVer1.setObjects(
      *(("MX-DIGIT-MAP-MIB", "digitMapTimeoutCompletion"),
        ("MX-DIGIT-MAP-MIB", "digitMapTimeoutFirstDigit"),
        ("MX-DIGIT-MAP-MIB", "digitMapTimeoutInterDigit"))
)
if mibBuilder.loadTexts:
    digitMapTimeoutVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

digitMapComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 55, 2, 1, 1)
)
digitMapComplVer1.setObjects(
      *(("MX-DIGIT-MAP-MIB", "digitMapAllowedVer1"),
        ("MX-DIGIT-MAP-MIB", "digitMapRefusedVer1"),
        ("MX-DIGIT-MAP-MIB", "digitMapTimeoutVer1"))
)
if mibBuilder.loadTexts:
    digitMapComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-DIGIT-MAP-MIB",
    **{"digitMapMIB": digitMapMIB,
       "digitMapMIBObjects": digitMapMIBObjects,
       "digitMapProcessDigitsWhenPressed": digitMapProcessDigitsWhenPressed,
       "digitMapAllowedTable": digitMapAllowedTable,
       "digitMapAllowedEntry": digitMapAllowedEntry,
       "digitMapAllowedIndex": digitMapAllowedIndex,
       "digitMapAllowedEnable": digitMapAllowedEnable,
       "digitMapAllowedDigitMap": digitMapAllowedDigitMap,
       "digitMapAllowedIsValid": digitMapAllowedIsValid,
       "digitMapPrefixedDigitRemovalCount": digitMapPrefixedDigitRemovalCount,
       "digitMapPrependedString": digitMapPrependedString,
       "digitMapSuffixStringToRemove": digitMapSuffixStringToRemove,
       "digitMapAllowedLineToApply": digitMapAllowedLineToApply,
       "digitMapRefusedTable": digitMapRefusedTable,
       "digitMapRefusedEntry": digitMapRefusedEntry,
       "digitMapRefusedIndex": digitMapRefusedIndex,
       "digitMapRefusedEnable": digitMapRefusedEnable,
       "digitMapRefusedDigitMap": digitMapRefusedDigitMap,
       "digitMapRefusedIsValid": digitMapRefusedIsValid,
       "digitMapRefusedLineToApply": digitMapRefusedLineToApply,
       "digitMapTimeouts": digitMapTimeouts,
       "digitMapTimeoutCompletion": digitMapTimeoutCompletion,
       "digitMapTimeoutFirstDigit": digitMapTimeoutFirstDigit,
       "digitMapTimeoutInterDigit": digitMapTimeoutInterDigit,
       "digitMapConformance": digitMapConformance,
       "digitMapCompliances": digitMapCompliances,
       "digitMapComplVer1": digitMapComplVer1,
       "digitMapGroups": digitMapGroups,
       "digitMapAllowedVer1": digitMapAllowedVer1,
       "digitMapRefusedVer1": digitMapRefusedVer1,
       "digitMapTimeoutVer1": digitMapTimeoutVer1}
)
