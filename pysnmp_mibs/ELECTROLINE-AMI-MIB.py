# SNMP MIB module (ELECTROLINE-AMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-AMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:47 2025
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

(dhtExtensionsMibObjects,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-EXTENSIONS-MIB",
    "dhtExtensionsMibObjects")

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


# MODULE-IDENTITY

amiIdentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17)
)
if mibBuilder.loadTexts:
    amiIdentMIB.setRevisions(
        ("2014-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AmiIdentObjects_ObjectIdentity = ObjectIdentity
amiIdentObjects = _AmiIdentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1)
)
_AmiTables_ObjectIdentity = ObjectIdentity
amiTables = _AmiTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1)
)
_AmiCibTables_ObjectIdentity = ObjectIdentity
amiCibTables = _AmiCibTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1)
)
_AmiCibDiscTable_Object = MibTable
amiCibDiscTable = _AmiCibDiscTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    amiCibDiscTable.setStatus("current")
_AmiCibDiscEntry_Object = MibTableRow
amiCibDiscEntry = _AmiCibDiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1)
)
amiCibDiscEntry.setIndexNames(
    (0, "ELECTROLINE-AMI-MIB", "amiCibDiscClass"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibDiscAddr"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibDiscIndex"),
)
if mibBuilder.loadTexts:
    amiCibDiscEntry.setStatus("current")


class _AmiCibDiscClass_Type(Integer32):
    """Custom type amiCibDiscClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              7,
              8,
              11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ipu", 4),
          ("sag", 6),
          ("apu", 7),
          ("bss", 8),
          ("doc", 11),
          ("xm2", 12),
          ("xm3", 13),
          ("enc", 14),
          ("app", 16),
          ("btq", 17),
          ("utl", 18),
          ("ecm", 19),
          ("ssc", 20))
    )


_AmiCibDiscClass_Type.__name__ = "Integer32"
_AmiCibDiscClass_Object = MibTableColumn
amiCibDiscClass = _AmiCibDiscClass_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 1),
    _AmiCibDiscClass_Type()
)
amiCibDiscClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscClass.setStatus("current")
_AmiCibDiscAddr_Type = Integer32
_AmiCibDiscAddr_Object = MibTableColumn
amiCibDiscAddr = _AmiCibDiscAddr_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 2),
    _AmiCibDiscAddr_Type()
)
amiCibDiscAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscAddr.setStatus("current")
_AmiCibDiscIndex_Type = Integer32
_AmiCibDiscIndex_Object = MibTableColumn
amiCibDiscIndex = _AmiCibDiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 3),
    _AmiCibDiscIndex_Type()
)
amiCibDiscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscIndex.setStatus("current")
_AmiCibDiscName_Type = DisplayString
_AmiCibDiscName_Object = MibTableColumn
amiCibDiscName = _AmiCibDiscName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 4),
    _AmiCibDiscName_Type()
)
amiCibDiscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscName.setStatus("current")
_AmiCibDiscValue_Type = Integer32
_AmiCibDiscValue_Object = MibTableColumn
amiCibDiscValue = _AmiCibDiscValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 5),
    _AmiCibDiscValue_Type()
)
amiCibDiscValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amiCibDiscValue.setStatus("current")
_AmiCibDiscEnum_Type = DisplayString
_AmiCibDiscEnum_Object = MibTableColumn
amiCibDiscEnum = _AmiCibDiscEnum_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 6),
    _AmiCibDiscEnum_Type()
)
amiCibDiscEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscEnum.setStatus("current")


class _AmiCibDiscAccess_Type(Integer32):
    """Custom type amiCibDiscAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              37)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("syswrite", 37))
    )


_AmiCibDiscAccess_Type.__name__ = "Integer32"
_AmiCibDiscAccess_Object = MibTableColumn
amiCibDiscAccess = _AmiCibDiscAccess_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 7),
    _AmiCibDiscAccess_Type()
)
amiCibDiscAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscAccess.setStatus("current")


class _AmiCibDiscAlarm_Type(Integer32):
    """Custom type amiCibDiscAlarm based on Integer32"""
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
        *(("ok", 1),
          ("alarmminor", 2),
          ("alarmmajor", 3),
          ("alarminfo", 4),
          ("alarmwarn", 5))
    )


_AmiCibDiscAlarm_Type.__name__ = "Integer32"
_AmiCibDiscAlarm_Object = MibTableColumn
amiCibDiscAlarm = _AmiCibDiscAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 1, 1, 8),
    _AmiCibDiscAlarm_Type()
)
amiCibDiscAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibDiscAlarm.setStatus("current")
_AmiCibAnaTable_Object = MibTable
amiCibAnaTable = _AmiCibAnaTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    amiCibAnaTable.setStatus("mandatory")
_AmiCibAnaEntry_Object = MibTableRow
amiCibAnaEntry = _AmiCibAnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1)
)
amiCibAnaEntry.setIndexNames(
    (0, "ELECTROLINE-AMI-MIB", "amiCibAnaClass"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibAnaAddr"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibAnaIndex"),
)
if mibBuilder.loadTexts:
    amiCibAnaEntry.setStatus("mandatory")


class _AmiCibAnaClass_Type(Integer32):
    """Custom type amiCibAnaClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              7,
              8,
              11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ipu", 4),
          ("sag", 6),
          ("apu", 7),
          ("bss", 8),
          ("doc", 11),
          ("xm2", 12),
          ("xm3", 13),
          ("enc", 14),
          ("app", 16),
          ("btq", 17),
          ("utl", 18),
          ("ecm", 19),
          ("ssc", 20))
    )


_AmiCibAnaClass_Type.__name__ = "Integer32"
_AmiCibAnaClass_Object = MibTableColumn
amiCibAnaClass = _AmiCibAnaClass_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 1),
    _AmiCibAnaClass_Type()
)
amiCibAnaClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibAnaClass.setStatus("mandatory")
_AmiCibAnaAddr_Type = Integer32
_AmiCibAnaAddr_Object = MibTableColumn
amiCibAnaAddr = _AmiCibAnaAddr_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 2),
    _AmiCibAnaAddr_Type()
)
amiCibAnaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibAnaAddr.setStatus("mandatory")
_AmiCibAnaIndex_Type = Integer32
_AmiCibAnaIndex_Object = MibTableColumn
amiCibAnaIndex = _AmiCibAnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 3),
    _AmiCibAnaIndex_Type()
)
amiCibAnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibAnaIndex.setStatus("mandatory")
_AmiCibAnaName_Type = DisplayString
_AmiCibAnaName_Object = MibTableColumn
amiCibAnaName = _AmiCibAnaName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 4),
    _AmiCibAnaName_Type()
)
amiCibAnaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibAnaName.setStatus("mandatory")
_AmiCibAnaValue_Type = Integer32
_AmiCibAnaValue_Object = MibTableColumn
amiCibAnaValue = _AmiCibAnaValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 5),
    _AmiCibAnaValue_Type()
)
amiCibAnaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amiCibAnaValue.setStatus("mandatory")
_AmiCibAnaUnits_Type = DisplayString
_AmiCibAnaUnits_Object = MibTableColumn
amiCibAnaUnits = _AmiCibAnaUnits_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 6),
    _AmiCibAnaUnits_Type()
)
amiCibAnaUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibAnaUnits.setStatus("mandatory")


class _AmiCibAnaAccess_Type(Integer32):
    """Custom type amiCibAnaAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              37)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("syswrite", 37))
    )


_AmiCibAnaAccess_Type.__name__ = "Integer32"
_AmiCibAnaAccess_Object = MibTableColumn
amiCibAnaAccess = _AmiCibAnaAccess_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 2, 1, 7),
    _AmiCibAnaAccess_Type()
)
amiCibAnaAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibAnaAccess.setStatus("mandatory")
_AmiCibCountTable_Object = MibTable
amiCibCountTable = _AmiCibCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    amiCibCountTable.setStatus("mandatory")
_AmiCibCountEntry_Object = MibTableRow
amiCibCountEntry = _AmiCibCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1)
)
amiCibCountEntry.setIndexNames(
    (0, "ELECTROLINE-AMI-MIB", "amiCibCountClass"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibCountAddr"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibCountIndex"),
)
if mibBuilder.loadTexts:
    amiCibCountEntry.setStatus("mandatory")


class _AmiCibCountClass_Type(Integer32):
    """Custom type amiCibCountClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              8,
              12,
              14,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ibm", 6),
          ("bss", 8),
          ("xm2", 12),
          ("sys", 14),
          ("ecm", 19))
    )


_AmiCibCountClass_Type.__name__ = "Integer32"
_AmiCibCountClass_Object = MibTableColumn
amiCibCountClass = _AmiCibCountClass_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 1),
    _AmiCibCountClass_Type()
)
amiCibCountClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibCountClass.setStatus("mandatory")
_AmiCibCountAddr_Type = Integer32
_AmiCibCountAddr_Object = MibTableColumn
amiCibCountAddr = _AmiCibCountAddr_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 2),
    _AmiCibCountAddr_Type()
)
amiCibCountAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibCountAddr.setStatus("mandatory")
_AmiCibCountIndex_Type = Integer32
_AmiCibCountIndex_Object = MibTableColumn
amiCibCountIndex = _AmiCibCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 3),
    _AmiCibCountIndex_Type()
)
amiCibCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibCountIndex.setStatus("mandatory")
_AmiCibCountName_Type = DisplayString
_AmiCibCountName_Object = MibTableColumn
amiCibCountName = _AmiCibCountName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 4),
    _AmiCibCountName_Type()
)
amiCibCountName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibCountName.setStatus("mandatory")
_AmiCibCountValue_Type = Integer32
_AmiCibCountValue_Object = MibTableColumn
amiCibCountValue = _AmiCibCountValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 5),
    _AmiCibCountValue_Type()
)
amiCibCountValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amiCibCountValue.setStatus("mandatory")
_AmiCibCountUnits_Type = DisplayString
_AmiCibCountUnits_Object = MibTableColumn
amiCibCountUnits = _AmiCibCountUnits_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 6),
    _AmiCibCountUnits_Type()
)
amiCibCountUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibCountUnits.setStatus("mandatory")


class _AmiCibCountAccess_Type(Integer32):
    """Custom type amiCibCountAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              37)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("syswrite", 37))
    )


_AmiCibCountAccess_Type.__name__ = "Integer32"
_AmiCibCountAccess_Object = MibTableColumn
amiCibCountAccess = _AmiCibCountAccess_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 3, 1, 7),
    _AmiCibCountAccess_Type()
)
amiCibCountAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibCountAccess.setStatus("mandatory")
_AmiCibTextTable_Object = MibTable
amiCibTextTable = _AmiCibTextTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    amiCibTextTable.setStatus("mandatory")
_AmiCibTextEntry_Object = MibTableRow
amiCibTextEntry = _AmiCibTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 4, 1)
)
amiCibTextEntry.setIndexNames(
    (0, "ELECTROLINE-AMI-MIB", "amiCibTextIndex"),
)
if mibBuilder.loadTexts:
    amiCibTextEntry.setStatus("mandatory")
_AmiCibTextIndex_Type = Integer32
_AmiCibTextIndex_Object = MibTableColumn
amiCibTextIndex = _AmiCibTextIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 4, 1, 1),
    _AmiCibTextIndex_Type()
)
amiCibTextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibTextIndex.setStatus("mandatory")
_AmiCibTextName_Type = DisplayString
_AmiCibTextName_Object = MibTableColumn
amiCibTextName = _AmiCibTextName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 4, 1, 2),
    _AmiCibTextName_Type()
)
amiCibTextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibTextName.setStatus("mandatory")
_AmiCibTextValue_Type = DisplayString
_AmiCibTextValue_Object = MibTableColumn
amiCibTextValue = _AmiCibTextValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 4, 1, 3),
    _AmiCibTextValue_Type()
)
amiCibTextValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amiCibTextValue.setStatus("mandatory")


class _AmiCibTextAccess_Type(Integer32):
    """Custom type amiCibTextAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              37)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("syswrite", 37))
    )


_AmiCibTextAccess_Type.__name__ = "Integer32"
_AmiCibTextAccess_Object = MibTableColumn
amiCibTextAccess = _AmiCibTextAccess_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 4, 1, 4),
    _AmiCibTextAccess_Type()
)
amiCibTextAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibTextAccess.setStatus("mandatory")
_AmiCibVersionTable_Object = MibTable
amiCibVersionTable = _AmiCibVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    amiCibVersionTable.setStatus("mandatory")
_AmiCibVersionEntry_Object = MibTableRow
amiCibVersionEntry = _AmiCibVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 5, 1)
)
amiCibVersionEntry.setIndexNames(
    (0, "ELECTROLINE-AMI-MIB", "amiCibVersionClass"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibVersionAddr"),
    (0, "ELECTROLINE-AMI-MIB", "amiCibVersionIndex"),
)
if mibBuilder.loadTexts:
    amiCibVersionEntry.setStatus("mandatory")


class _AmiCibVersionClass_Type(Integer32):
    """Custom type amiCibVersionClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              7,
              8,
              11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ipu", 4),
          ("sag", 6),
          ("apu", 7),
          ("bss", 8),
          ("doc", 11),
          ("xm2", 12),
          ("xm3", 13),
          ("enc", 14),
          ("app", 16),
          ("btq", 17),
          ("utl", 18),
          ("ecm", 19),
          ("ssc", 20))
    )


_AmiCibVersionClass_Type.__name__ = "Integer32"
_AmiCibVersionClass_Object = MibTableColumn
amiCibVersionClass = _AmiCibVersionClass_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 5, 1, 1),
    _AmiCibVersionClass_Type()
)
amiCibVersionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibVersionClass.setStatus("mandatory")


class _AmiCibVersionAddr_Type(Integer32):
    """Custom type amiCibVersionAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AmiCibVersionAddr_Type.__name__ = "Integer32"
_AmiCibVersionAddr_Object = MibTableColumn
amiCibVersionAddr = _AmiCibVersionAddr_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 5, 1, 2),
    _AmiCibVersionAddr_Type()
)
amiCibVersionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibVersionAddr.setStatus("mandatory")


class _AmiCibVersionIndex_Type(Integer32):
    """Custom type amiCibVersionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AmiCibVersionIndex_Type.__name__ = "Integer32"
_AmiCibVersionIndex_Object = MibTableColumn
amiCibVersionIndex = _AmiCibVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 5, 1, 3),
    _AmiCibVersionIndex_Type()
)
amiCibVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibVersionIndex.setStatus("mandatory")
_AmiCibVersionText_Type = DisplayString
_AmiCibVersionText_Object = MibTableColumn
amiCibVersionText = _AmiCibVersionText_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 17, 1, 1, 1, 5, 1, 4),
    _AmiCibVersionText_Type()
)
amiCibVersionText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amiCibVersionText.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-AMI-MIB",
    **{"amiIdentMIB": amiIdentMIB,
       "amiIdentObjects": amiIdentObjects,
       "amiTables": amiTables,
       "amiCibTables": amiCibTables,
       "amiCibDiscTable": amiCibDiscTable,
       "amiCibDiscEntry": amiCibDiscEntry,
       "amiCibDiscClass": amiCibDiscClass,
       "amiCibDiscAddr": amiCibDiscAddr,
       "amiCibDiscIndex": amiCibDiscIndex,
       "amiCibDiscName": amiCibDiscName,
       "amiCibDiscValue": amiCibDiscValue,
       "amiCibDiscEnum": amiCibDiscEnum,
       "amiCibDiscAccess": amiCibDiscAccess,
       "amiCibDiscAlarm": amiCibDiscAlarm,
       "amiCibAnaTable": amiCibAnaTable,
       "amiCibAnaEntry": amiCibAnaEntry,
       "amiCibAnaClass": amiCibAnaClass,
       "amiCibAnaAddr": amiCibAnaAddr,
       "amiCibAnaIndex": amiCibAnaIndex,
       "amiCibAnaName": amiCibAnaName,
       "amiCibAnaValue": amiCibAnaValue,
       "amiCibAnaUnits": amiCibAnaUnits,
       "amiCibAnaAccess": amiCibAnaAccess,
       "amiCibCountTable": amiCibCountTable,
       "amiCibCountEntry": amiCibCountEntry,
       "amiCibCountClass": amiCibCountClass,
       "amiCibCountAddr": amiCibCountAddr,
       "amiCibCountIndex": amiCibCountIndex,
       "amiCibCountName": amiCibCountName,
       "amiCibCountValue": amiCibCountValue,
       "amiCibCountUnits": amiCibCountUnits,
       "amiCibCountAccess": amiCibCountAccess,
       "amiCibTextTable": amiCibTextTable,
       "amiCibTextEntry": amiCibTextEntry,
       "amiCibTextIndex": amiCibTextIndex,
       "amiCibTextName": amiCibTextName,
       "amiCibTextValue": amiCibTextValue,
       "amiCibTextAccess": amiCibTextAccess,
       "amiCibVersionTable": amiCibVersionTable,
       "amiCibVersionEntry": amiCibVersionEntry,
       "amiCibVersionClass": amiCibVersionClass,
       "amiCibVersionAddr": amiCibVersionAddr,
       "amiCibVersionIndex": amiCibVersionIndex,
       "amiCibVersionText": amiCibVersionText}
)
